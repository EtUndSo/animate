"""Prüft ein Arbeitsheft-PDF maschinell, damit niemand es Seite für Seite als Bild lesen muss.

    python tools/pdf_pruefen.py <heft.pdf> <ausgabeordner> [--blatt]

Meldet:
  * fehlende Verweise ("??" im Text),
  * Text oder Zeichnungen, die rechts oder links über den Satzspiegel ragen,
  * Beschriftungen, die einander überlappen (typisch für TikZ-Abbildungen).
Schreibt nach <ausgabeordner>:
  * text.txt: der Text aller Seiten (für Grep; viel billiger als Seitenbilder),
  * stelle_<n>.png: ein kleiner Ausschnitt um jede gemeldete Stelle,
  * mit --blatt zusätzlich blatt_<k>.png: Übersicht aller Seiten mit Abbildungen, sechs Seiten je Bild.
Ein Bild ansehen kostet etwa so viel wie eine ganze Seite Text. Deshalb nur die Ausschnitte ansehen und das Blatt höchstens einmal.
"""
import sys
import unicodedata
from collections import Counter
from pathlib import Path

import fitz  # PyMuPDF

sys.stdout.reconfigure(encoding="utf-8")

RAND_TOL = 5.0          # pt, so viel darf etwas über den Satzspiegel ragen (microtype hängt Anführungszeichen und Trennstriche bis ~4 pt hinaus)
UEBERLAPP_ANTEIL = 0.25  # Anteil der kleineren Box, ab dem zwei Beschriftungen als überlappend gelten
ZU_DICHT = 1.5           # pt; zwei Textzeilen auf gleicher Höhe mit kleinerer Lücke wirken wie ein Text


def satzspiegel(doc):
    """Linker und rechter Rand des Fließtexts: die äußersten Zeilenkanten, die häufig vorkommen.
    (Nicht die häufigste Kante: In Heften mit vielen Kästen ist das der eingerückte Kastenrand.)"""
    links, rechts = Counter(), Counter()
    for page in doc:
        breite = page.rect.width
        for b in page.get_text("dict")["blocks"]:
            for l in b.get("lines", []):
                x0, _, x1, _ = l["bbox"]
                if x1 - x0 > 0.5 * breite:
                    links[round(x0)] += 1
                    rechts[round(x1)] += 1
    schwelle = max(5, 0.03 * sum(rechts.values()))
    return (min(x for x, c in links.items() if c >= schwelle),
            max(x for x, c in rechts.items() if c >= schwelle))


def zeichen(t):
    """Zahl der echten Buchstaben und Ziffern (ohne Modifikatorzeichen wie ˆ ¯ ˜, die als Akzente dienen)."""
    return sum(unicodedata.category(c) in ("Lu", "Ll", "Lo", "Nd") for c in t)


def kern(b):
    """Box ohne den Leerraum von Ober- und Unterlänge der Schrift."""
    x0, y0, x1, y1 = b
    h = y1 - y0
    return fitz.Rect(x0 + 0.8, y0 + 0.22 * h, x1 - 0.8, y1 - 0.22 * h)


def pruefen(pdf, aus, blatt):
    doc = fitz.open(pdf)
    aus.mkdir(parents=True, exist_ok=True)
    L, R = satzspiegel(doc)
    stellen, text = [], []

    for page in doc:
        n = page.number + 1
        d = page.get_text("dict")
        spans, zeilen = [], []
        for b in d["blocks"]:
            for li, l in enumerate(b.get("lines", [])):
                zt = "".join(s["text"] for s in l["spans"]).strip()
                if zeichen(zt) >= 2:
                    zeilen.append((zt, fitz.Rect(l["bbox"])))
                for s in l["spans"]:
                    t = s["text"].strip()
                    if not t or s.get("alpha", 255) == 0:      # unsichtbar (ausgeblendeter Text einer animierten Szene)
                        continue
                    spans.append((t, fitz.Rect(s["bbox"]), id(l)))
                    if s["bbox"][2] > R + RAND_TOL or s["bbox"][0] < L - RAND_TOL:
                        stellen.append((n, "ragt über den Rand", t[:60], fitz.Rect(s["bbox"])))
        for z in page.get_drawings():
            r = z["rect"]
            if r.width > 1 and (r.x1 > R + RAND_TOL or r.x0 < L - RAND_TOL):
                stellen.append((n, "Zeichnung ragt über den Rand", f"{r.x0:.0f}–{r.x1:.0f} pt (Satzspiegel {L}–{R})", r))
        seitentext = page.get_text()
        text.append(f"===== Seite {n} =====\n{seitentext}")
        if "??" in seitentext:
            i = seitentext.index("??")
            stellen.append((n, "fehlender Verweis ??", seitentext[max(0, i - 40):i + 10].replace("\n", " "), None))
        # Überlappungen: nur Beschriftungen mit mindestens zwei Buchstaben oder Ziffern
        # (Indizes, Akzente und Klammerteile von \underbrace, die als „{z“ oder „}|“ im PDF stehen, ausgenommen)
        kand = [(t, kern(r), zl) for t, r, zl in spans if zeichen(t) >= 2 and r.height < 30]
        for i in range(len(kand)):
            t1, r1, z1 = kand[i]
            for j in range(i + 1, len(kand)):
                t2, r2, z2 = kand[j]
                if z1 == z2:
                    continue
                schnitt = r1 & r2
                if schnitt.is_empty:
                    continue
                kleiner = min(r1.get_area(), r2.get_area()) or 1
                if schnitt.get_area() / kleiner > UEBERLAPP_ANTEIL:
                    stellen.append((n, "Beschriftungen überlappen", f"„{t1[:30]}“ / „{t2[:30]}“", r1 | r2))
        # Zwei Beschriftungen auf gleicher Höhe, die (fast) aneinanderstoßen, lesen sich als eine:
        # „x1 + x2 = 1x1 + x2 = 3“. Nur in Abbildungen (Bereiche mit vielen Vektorpfaden) und nur kurze
        # Beschriftungen; im Fließtext zerfallen Brüche und Indizes in mehrere Zeilen, das wäre kein Fehler.
        zeichnungen = page.get_drawings()
        bereiche = [c for c in page.cluster_drawings(drawings=zeichnungen)
                    if sum(1 for z in zeichnungen if z["rect"] in c) >= 8 and c.width < 0.95 * (R - L)]
        def in_abb(r):
            m = fitz.Point((r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2)
            return next((k for k, c in enumerate(bereiche) if m in c + (-8, -8, 8, 8)), None)
        etiketten = [(t, r, in_abb(r)) for t, r in zeilen if r.width < 0.4 * (R - L)]
        etiketten = [e for e in etiketten if e[2] is not None]
        for i in range(len(etiketten)):
            t1, r1, a1 = etiketten[i]
            for t2, r2, a2 in etiketten[i + 1:]:
                if a1 != a2:
                    continue
                links, rechts = (r1, r2) if r1.x0 <= r2.x0 else (r2, r1)
                luecke = rechts.x0 - links.x1
                hoehe = min(r1.y1, r2.y1) - max(r1.y0, r2.y0)
                # tiefer ineinander (Lücke < −1 pt) sind Bruchteile wie „C = 1/3 F“; echtes Überlappen meldet die Prüfung oben
                if -1.0 < luecke < ZU_DICHT and hoehe > 0.6 * min(r1.height, r2.height):
                    stellen.append((n, "Beschriftungen stoßen aneinander", f"„{t1[:30]}“ / „{t2[:30]}“ (Lücke {luecke:.1f} pt)", r1 | r2))

    (aus / "text.txt").write_text("\n".join(text), encoding="utf-8")

    for k, (n, art, info, r) in enumerate(stellen, 1):
        print(f"S. {n}: {art}: {info}")
        if r is not None and k <= 40:
            page = doc[n - 1]
            clip = fitz.Rect(r.x0 - 60, r.y0 - 40, r.x1 + 60, r.y1 + 40) & page.rect
            page.get_pixmap(matrix=fitz.Matrix(2, 2), clip=clip).save(aus / f"stelle_{k}.png")
    print(f"{len(doc)} Seiten, Satzspiegel {L}–{R} pt, {len(stellen)} Stellen gemeldet"
          + (f" (Ausschnitte stelle_1 bis stelle_{min(len(stellen), 40)}.png)" if stellen else ""))

    if blatt:
        # Seiten mit Abbildungen: viele Vektorpfade (TikZ) oder eingebettete Bilder
        seiten = [p.number for p in doc if len(p.get_drawings()) > 25 or p.get_images()]
        for k in range(0, len(seiten), 6):
            gruppe = seiten[k:k + 6]
            bilder = [doc[i].get_pixmap(matrix=fitz.Matrix(0.9, 0.9)) for i in gruppe]
            w, h = bilder[0].width, bilder[0].height
            ziel = fitz.Pixmap(fitz.csRGB, fitz.IRect(0, 0, 3 * w + 20, 2 * h + 10), False)
            ziel.clear_with(160)
            for m, (i, pix) in enumerate(zip(gruppe, bilder)):
                pix.set_origin((m % 3) * (w + 10), (m // 3) * (h + 10))
                ziel.copy(pix, pix.irect)
            ziel.save(aus / f"blatt_{k // 6 + 1}.png")
            print(f"blatt_{k // 6 + 1}.png: Seiten {', '.join(str(i + 1) for i in gruppe)}")


if __name__ == "__main__":
    pruefen(sys.argv[1], Path(sys.argv[2]), "--blatt" in sys.argv)

"""Kennzahlen eines Artikels für die Selbstprüfung (ERKLAER_PROMPT §3.3 und §11).

Hauptpfad = sichtbarer Text ohne Herleitungskästen, Antworten der Frage-Kästen (beide eingeklappt), Beispiele und
Quiz; die Frage selbst (erste Zeile eines Frage-Kastens) zählt mit. Abgesetzte Formeln zählen nicht,
eine Inline-Formel zählt als ein Wort, rohe HTML-Zeilen (Abbildungen) zählen nicht.
Aufruf: python -I tools/artikel_kennzahlen.py <artikel.md> [<artikel.md> …]
"""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
WPM = 170
VERBOTEN = [r"\bbekanntlich\b", r"\boffensichtlich\b", r"\bnatürlich\b", r"\bwie man leicht sieht\b",
            r"\btrivialerweise\b", r"\beinfach\b"]


def woerter(text):
    text = re.sub(r"\$\$.+?\$\$", " ", text, flags=re.S)
    text = re.sub(r"\$[^$\n]+\$", " X ", text)
    text = re.sub(r"[*_|#>`]", " ", text)
    return len([w for w in text.split() if re.search(r"[A-Za-zÄÖÜäöüß0-9]", w)])


def analyse(path):
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    i = 0
    if lines and lines[0].strip() == "---":                      # Frontmatter überspringen
        i = 1
        while i < len(lines) and lines[i].strip() != "---":
            i += 1
        i += 1
    haupt, herl, bsp, antw, quiz_n = [], [], [], [], 0
    sektionen, akt = [], None
    kaesten, abb, formeln, grafik = {}, 0, 0, 0
    modus = None                                                 # None | herleitung | beispiel | quiz | frage | box
    frage_zeile = False
    for ln in lines[i:]:
        s = ln.strip()
        if modus == "beispiel":                                  # ::::beispiel … :::: (darf ::: enthalten)
            if s == "::::":
                modus = None
            else:
                bsp.append(ln)
            continue
        if modus in ("herleitung", "quiz", "box", "frage"):
            if s == ":::":
                modus = None
                continue
            if modus == "herleitung":
                herl.append(ln)
            elif modus == "quiz":
                quiz_n += bool(re.match(r"(F|Q|Frage)\s*[:.]", s))
            elif modus == "frage" and not (frage_zeile and s):
                antw.append(ln)                                  # Antwort: eingeklappt
            else:
                frage_zeile = False if modus == "frage" else frage_zeile
                haupt.append(ln)
                if akt is not None:
                    akt[1].append(ln)
            continue
        m4 = re.match(r"::::\s*beispiel\b", s)
        m3 = re.match(r":::\s*([a-zA-Z]+)", s)
        if m4:
            modus = "beispiel"
            kaesten["beispiel"] = kaesten.get("beispiel", 0) + 1
            continue
        if m3:
            art = m3.group(1).lower()
            kaesten[art] = kaesten.get(art, 0) + 1
            if art == "formel":
                formeln += 1
            if art == "grafik":
                grafik += 1
            modus = {"herleitung": "herleitung", "quiz": "quiz", "frage": "frage"}.get(art, "box")
            frage_zeile = art == "frage"
            continue
        if s.startswith("<"):
            abb += s.count("<figure")
            continue
        h = re.match(r"##\s+(.*)$", s)
        if h and not s.startswith("###"):
            akt = (h.group(1).strip(), [])
            sektionen.append(akt)
            continue
        haupt.append(ln)
        if akt is not None:
            akt[1].append(ln)
    text = "\n".join(haupt)
    w = woerter(text)
    striche = len(re.findall(r"\s[–—]\s", text))
    nicht_sondern = len(re.findall(r"\bnicht\b[^.;:!?]{0,80}\bsondern\b", text))
    print(f"\n{path}")
    print(f"  Hauptpfad:        {w} Wörter, Lesezeit ≈ {w / WPM:.0f} min")
    print(f"  Herleitungen:     {kaesten.get('herleitung', 0)} Kästen, {woerter(chr(10).join(herl))} Wörter")
    print(f"  Frage-Antworten:  {kaesten.get('frage', 0)} Kästen, {woerter(chr(10).join(antw))} Wörter (eingeklappt)")
    print(f"  Beispiele:        {kaesten.get('beispiel', 0)}, {woerter(chr(10).join(bsp))} Wörter")
    print(f"  Quiz-Fragen:      {quiz_n}")
    print(f"  Abbildungen:      {abb}  (eine je {w / abb:.0f} Wörter)" if abb else "  Abbildungen:      0")
    print(f"  Formel-Boxen:     {formeln}")
    print(f"  :::grafik:        {grafik}  (Soll: 0)")
    andere = {k: v for k, v in sorted(kaesten.items()) if k not in ("herleitung", "beispiel", "quiz", "formel", "grafik")}
    print(f"  Kästen:           {andere}")
    print(f"  Gedankenstriche:  {striche} ({1000 * striche / max(w, 1):.1f} je 1000 Wörter)")
    print(f"  „nicht … sondern“: {nicht_sondern}")
    treffer = [(p, len(re.findall(p, text, flags=re.I))) for p in VERBOTEN]
    treffer = [(p.strip('\\b'), n) for p, n in treffer if n]
    print(f"  Verbotsliste:     {treffer if treffer else 'keine Treffer'}")
    print("  Abschnitte (Wörter im Hauptpfad):")
    for name, inhalt in sektionen:
        print(f"    {woerter(chr(10).join(inhalt)):5d}  {name}")


for p in sys.argv[1:]:
    analyse(p)

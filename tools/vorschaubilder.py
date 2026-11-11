"""Vorschaubilder für soziale Medien (og:image, 1200×630 PNG): eines je Kapitel und Sprache, dazu ein Standardbild je
Sprache für Seiten ohne Kapitel (Startseite, Übersicht, Modul- und Bereichsseiten, Editor).

    python tools/vorschaubilder.py              nur fehlende oder geänderte Bilder (der Normalfall, nach neuen Kapiteln)
    python tools/vorschaubilder.py --alle       alle neu
    python tools/vorschaubilder.py --lang de    nur diese Sprache(n), mehrfach möglich
    python tools/vorschaubilder.py --check      nur melden, was entstünde oder wegfiele; nichts schreiben
    python tools/vorschaubilder.py --muster DIR je Sprache ein Kapitelbild und das Standardbild nach DIR (Gestaltung prüfen)

Läuft NICHT bei jedem Build. Ein Bild entsteht neu, wenn sich sein Fingerabdruck ändert: Hash über Gestaltung (VORLAGE),
Sprache, Kapitelname, Modul und die Datei der Abbildung. Er steht im Bild selbst (PNG-Textfeld „etundso-vorschau“), es
gibt also keine Liste daneben. Bilder von Kapiteln, die es nicht mehr gibt, löscht das Skript.

Ablage (build_wissen.vorschau_rel): web/vorschau/<l>/<Kapiteladresse ohne Sprachkürzel>.png und web/vorschau/<l>.png.
build_wissen.py verweist auf das Kapitelbild, wenn es existiert, sonst auf das Standardbild der Sprache.

Gestaltung wie die Seite (Vorlage „Grüne Leiste“, Variante B): links die dunkelgrüne Leiste mit Logo, Modul und Kapitel
(Kapitelnummer orange, Titel weiß), rechts auf weißem Grund das Endbild der ersten Abbildung des Kapitels
(web/abbildungen/<l>/<szene>.svg; fehlt sie in der Sprache, ist die Leiste so breit wie das Bild). Das Standardbild zeigt
den Untertitel der Startseite und deren erste Abbildung. Gerastert mit Playwright (Chromium, Systemschriften), danach
mit Pillow auf eine Palette verkleinert (Ziel: unter etwa 80 KB je Bild).
"""
import argparse
import base64
import hashlib
import html
import io
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.stdout.reconfigure(encoding="utf-8")

import build_wissen as bw  # noqa: E402  (Baum, Adressen und Ablage aus einer Quelle)

VORLAGE = "2"                                          # bei geänderter Gestaltung erhöhen: dann entstehen alle Bilder neu
B, H = 1200, 630
TEXT_SCHLUESSEL = "etundso-vorschau"
FARBEN = 128                                           # Palette (flache Grafik, Kantenglättung bleibt sichtbar sauber)
ABB_RE = re.compile(r"(?m)^:::abbildung[ \t]+(\S+)")
SCHRIFT = {"zh": "'Microsoft YaHei', 'PingFang SC', 'Noto Sans CJK SC', 'Segoe UI', system-ui, sans-serif"}
SCHRIFT_STANDARD = "'Segoe UI', system-ui, -apple-system, Roboto, 'Noto Sans', Arial, sans-serif"

SEITE = """<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><style>
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:{B}px;height:{H}px;overflow:hidden;background:#ffffff}}
body{{display:flex;font-family:{schrift};-webkit-font-smoothing:antialiased}}
.leiste{{width:{breite}px;height:100%;background:#123d29;color:#eaf3ec;display:flex;flex-direction:column;padding:52px 56px 46px}}
.logo{{font-family:'Segoe UI',system-ui,sans-serif;font-weight:800;font-size:40px;letter-spacing:-0.02em;color:#ff9650;line-height:1}}
.logo span{{color:#eaf3ec}} .logo span.so{{color:#ff4d4d}}
.block{{flex:1;display:flex;flex-direction:column;justify-content:center;min-height:0;overflow:hidden;padding:18px 0}}
.marke{{font-size:27px;font-weight:700;color:#ff9650;letter-spacing:0.01em;margin-bottom:16px}}
.titel{{font-size:56px;font-weight:700;line-height:1.12;color:#ffffff;letter-spacing:-0.01em;overflow-wrap:normal;hyphens:manual}}
.modul{{font-size:24px;line-height:1.35;color:#b7d3c2;margin-top:22px}}
.fuss{{display:flex;align-items:center;gap:14px;font-size:21px;color:#9fc2ad}}
.fuss i{{display:block;width:44px;height:5px;border-radius:3px;background:#ff9650}}
.bild{{flex:1;height:100%;display:flex;align-items:center;justify-content:center;padding:40px 44px;background:#ffffff}}
.bild img{{max-width:100%;max-height:100%;width:auto;height:auto;object-fit:contain}}
</style></head><body>
<div class="leiste"><div class="logo">Et<span>Und</span><span class="so">So</span></div>
<div class="block"><div class="marke">{marke}</div><div class="titel">{titel}</div>{modul}</div>
<div class="fuss"><i></i>etundso.de</div></div>{bild}
<script>
(function(){{var t=document.querySelector(".titel"),b=document.querySelector(".block"),m=document.querySelector(".modul"),
  fs=parseFloat(getComputedStyle(t).fontSize);
  function zu(){{return b.scrollHeight>b.clientHeight+1||t.scrollWidth>t.clientWidth+1;}}   // auch kein Wort breiter als die Leiste
  while(zu()&&fs>30){{fs-=2;t.style.fontSize=fs+"px";}}
  if(zu()&&m){{m.style.fontSize="20px";}}
  while(zu()&&fs>20){{fs-=2;t.style.fontSize=fs+"px";}}
  if(zu()){{t.style.overflowWrap="anywhere";}}
  window.fertig=true;}})();
</script></body></html>"""


def kapitel_liste(trees, langs):
    """[(Sprache, Datei relativ zu web/vorschau, Marke, Titel, Modul, SVG-Pfad oder None)] je Kapitel, in Lesefolge."""
    out = []
    for lang in langs:
        tree = trees.get(lang)
        if not tree:
            continue
        kap = {}
        for a in bw.flatten(tree):
            kap.setdefault(bw.kapitel_ordner(a["path"]), []).append(a)
        for ordner, arts in kap.items():
            crumbs = [nm for nm, _ in arts[0]["crumbs"]]
            name = bw.klartext(crumbs[-1]) if crumbs else ""
            teile = re.split(r"\s*[:：]\s*", name, maxsplit=1)
            nummer, titel = (teile[0], teile[1]) if len(teile) == 2 else ("", name)
            modul = bw.klartext(crumbs[-2]) if len(crumbs) > 1 else ""
            kurz, _, voll = modul.partition(" – ")         # „ET3 – Grundgebiete …“: Kurzname oben, voller Name unten
            if not voll and len(crumbs) > 2:               # „Mathematische Grundlagen“: darunter die Reihe (Machine Learning)
                voll = bw.klartext(crumbs[-3])
            marke = " · ".join(x for x in (kurz, nummer) if x)
            svg = None
            for a in arts:
                for szene in ABB_RE.findall(a["body"]):
                    p = bw.ABB_DIR / lang / (szene + ".svg")
                    if bw.SZENE_NAME_RE.fullmatch(szene) and p.is_file():
                        svg = p
                        break
                if svg:
                    break
            out.append((lang, bw.vorschau_rel(lang, ordner), marke, titel, voll, svg))
    return out


def standard_liste(langs):
    """Standardbild je Sprache: Untertitel der Startseite und ihre erste Abbildung (in der Sprache, sonst ohne Bild)."""
    vorlage = (ROOT / "web" / "index.html").read_text(encoding="utf-8")
    de_titel = html.unescape(re.search(r"<title[^>]*>(.*?)</title>", vorlage, re.S).group(1)).strip()
    erste = re.search(r'src="/abbildungen/de/([^"]+\.svg)"', vorlage)
    out = []
    for lang in langs:
        titel = de_titel if lang == "de" else bw.STARTSEITE_TEXTE.get(lang, {}).get("titel", de_titel)
        untertitel = titel.split(" — ", 1)[1] if " — " in titel else titel
        svg = bw.ABB_DIR / lang / erste.group(1) if erste else None
        out.append((lang, f"{lang}.png", "", untertitel, "", svg if svg and svg.is_file() else None))
    return out


def fingerabdruck(lang, marke, titel, modul, svg):
    h = hashlib.sha256()
    h.update(json.dumps([VORLAGE, lang, marke, titel, modul, svg.relative_to(ROOT).as_posix() if svg else ""],
                        ensure_ascii=False).encode("utf-8"))
    if svg:
        h.update(svg.read_bytes())
    return h.hexdigest()[:20]


def gespeichert(pfad):
    """Fingerabdruck im vorhandenen Bild (PNG-Textfeld), sonst None."""
    from PIL import Image
    try:
        with Image.open(pfad) as im:
            return im.text.get(TEXT_SCHLUESSEL)
    except (OSError, ValueError, AttributeError):
        return None


def seite_html(lang, marke, titel, modul, svg):
    bild = ""
    if svg:
        daten = base64.b64encode(svg.read_bytes()).decode("ascii")
        bild = f'<div class="bild"><img alt="" src="data:image/svg+xml;base64,{daten}"/></div>'
    return SEITE.format(lang=lang, B=B, H=H, schrift=SCHRIFT.get(lang, SCHRIFT_STANDARD), breite=540 if svg else B,
                        marke=html.escape(marke), titel=html.escape(titel),
                        modul=f'<div class="modul">{html.escape(modul)}</div>' if modul else "", bild=bild)


def png_klein(roh, abdruck):
    """Bildschirmfoto -> PNG mit Palette und Fingerabdruck."""
    from PIL import Image, PngImagePlugin
    im = Image.open(io.BytesIO(roh)).convert("RGB")
    info = PngImagePlugin.PngInfo()
    info.add_text(TEXT_SCHLUESSEL, abdruck)
    pal = im.quantize(colors=FARBEN, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)
    buf = io.BytesIO()
    pal.save(buf, format="PNG", optimize=True, pnginfo=info)
    return buf.getvalue()


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--alle", action="store_true", help="alle Bilder neu")
    ap.add_argument("--lang", action="append", choices=bw.LANGS, help="nur diese Sprache(n)")
    ap.add_argument("--check", action="store_true", help="nur melden, nichts schreiben")
    ap.add_argument("--muster", metavar="DIR", help="je Sprache ein Kapitelbild und das Standardbild nach DIR")
    args = ap.parse_args()
    langs = tuple(args.lang or bw.LANGS)
    trees = bw.collect()
    auftraege = standard_liste(langs) + kapitel_liste(trees, langs)
    ziel_dir = bw.VORSCHAU_DIR
    if args.muster:
        ziel_dir = Path(args.muster)
        erste = {}
        for a in auftraege:
            if a[1].count("/") and a[0] not in erste:
                erste[a[0]] = a
        auftraege = [a for a in auftraege if "/" not in a[1]] + list(erste.values())
    zu_tun = []
    for lang, rel, marke, titel, modul, svg in auftraege:
        abdruck = fingerabdruck(lang, marke, titel, modul, svg)
        ziel = ziel_dir / rel
        if args.alle or args.muster or not ziel.is_file() or gespeichert(ziel) != abdruck:
            zu_tun.append((ziel, abdruck, seite_html(lang, marke, titel, modul, svg)))
    gueltig = {(bw.VORSCHAU_DIR / a[1]).resolve() for a in standard_liste(bw.LANGS) + kapitel_liste(trees, bw.LANGS)}
    alt = [] if args.muster else [p for p in sorted(bw.VORSCHAU_DIR.rglob("*.png")) if p.resolve() not in gueltig
                                  and (args.lang is None or p.relative_to(bw.VORSCHAU_DIR).parts[0].split(".")[0] in langs)]
    print(f"Vorschaubilder: {len(auftraege)} gesamt, {len(zu_tun)} neu oder geändert, {len(alt)} veraltet")
    if args.check:
        for z, _, _ in zu_tun:
            print("  neu:", z.relative_to(ROOT) if ROOT in z.parents else z)
        for p in alt:
            print("  weg:", p.relative_to(ROOT))
        return
    if zu_tun:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as pw:
            browser = pw.chromium.launch()
            page = browser.new_page(viewport={"width": B, "height": H}, device_scale_factor=1)
            for k, (ziel, abdruck, seite) in enumerate(zu_tun, 1):
                page.set_content(seite, wait_until="load")
                page.evaluate("async () => { await document.fonts.ready; for (const i of document.images) "
                              "{ try { await i.decode(); } catch (e) {} } }")
                page.wait_for_function("window.fertig === true")
                daten = png_klein(page.screenshot(type="png", clip={"x": 0, "y": 0, "width": B, "height": H}), abdruck)
                ziel.parent.mkdir(parents=True, exist_ok=True)
                ziel.write_bytes(daten)
                print(f"  {k}/{len(zu_tun)} {ziel.relative_to(ROOT) if ROOT in ziel.parents else ziel}: {len(daten) // 1024} KB")
            browser.close()
    for p in alt:
        p.unlink()
    for d in sorted((d for d in bw.VORSCHAU_DIR.rglob("*") if d.is_dir()), key=lambda d: -len(d.parts)):
        if not any(d.iterdir()):
            d.rmdir()
    if bw.VORSCHAU_DIR.is_dir():
        alle = list(bw.VORSCHAU_DIR.rglob("*.png"))
        print(f"web/vorschau: {len(alle)} Bilder, {sum(p.stat().st_size for p in alle) / 1024:.0f} KB,"
              f" größtes {max((p.stat().st_size for p in alle), default=0) / 1024:.0f} KB")


if __name__ == "__main__":
    main()

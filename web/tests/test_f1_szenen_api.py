"""F1 „Bildschirme und Fenster“ (12.11.2026): die Szenen-API in tools/szenen_lib.py. Raster und Terminal: Spalten-
Funktionen (x, xr, xm, y, anker, felder, trenner, finde) treffen genau die Zellen, die Engine und Export zeichnen;
markieren liegt unter dem Raster-Text, klammer, teil (deckungsgleich, beim Terminal mit seinen Farben), wert, faerben;
Terminal-Abläufe (eingabe, befehl, prompt, warten, leeren, setze, schliessen) als Schritte der Zeitachse; top, Pager,
Datei-Ansicht, Schloss; Schutz vor Ankern, die eine spätere Fenstergröße nicht mehr treffen; automatische Schriftgröße;
Prüfung der Mindestschriftgröße im Export. Run from web/:  python tests/test_f1_szenen_api.py"""
import io
import json
import re
import sys
from contextlib import redirect_stdout
from pathlib import Path

sys.path.insert(0, "."); sys.path.insert(0, "py")
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools")); sys.path.insert(0, str(ROOT / "tools" / "szenen")); sys.path.insert(0, str(ROOT))
from engine.scene_model import ModelScene  # noqa: E402
from engine import export as ex  # noqa: E402
import export_szenen as es  # noqa: E402
from szenen_lib import Szene, ORANGE, GRAU, BLAU, PX, farbig, fett, invers  # noqa: E402

ok = True


def check(name, cond, extra=""):
    global ok
    print(("  OK   " if cond else " FAIL  ") + name + (("  :: " + str(extra)[:300]) if extra != "" and not cond else ""))
    ok = ok and bool(cond)


DEF, KINDS = es.load_editor_tables()


def bauen(s, ende=True):
    m = es.python_model(json.loads(json.dumps(s.model())), DEF, KINDS, "de", [])
    sc = ModelScene(m)
    sc.animating = True
    sc.build_timeline()
    sc.seek(sc.duration if ende else 0.0)
    return sc


def svg(sc):
    return ex.render(sc.objectList, sc.camera, background=(1, 1, 1), raw_settings={"mode": "canvas"})[0]


def px(x):
    return 960 + x * PX


def py_(y):
    return 540 - y * PX


def zeile(svg_text, enthaelt):
    """(x-Liste, y) der Schreibmaschinenzeile, deren Text enthaelt (ohne Tags) enthält."""
    for xs, y, body in re.findall(r'<text x="([^"]+)" y="([^"]+)"[^>]*>(.*?)</text>', svg_text):
        if enthaelt in re.sub(r"<[^>]+>", "", body) and len(xs.split()) > 1:
            return [float(v) for v in xs.split()], float(y)
    return None, None


# ---------------------------------------------------------------- 1. Raster
s = Szene("t/raster", reihenfolge="anlegen")
P = "student:x:1000:1000:Student:/home/student:/bin/bash"
g = s.raster([P, "sudo:x:27:student"], (-3.0, 1.0), groesse=20)
mk = g.markieren(0, 8, 11, ORANGE)
check("markieren: Hinterlegung liegt vor der ersten Zeile in der Objektliste (unter dem Text)",
      [o["id"] for o in s.objects].index(mk) < [o["id"] for o in s.objects].index(g.ids[0]))
fl = g.felder(0, ":")
check("felder(':'): sieben Felder mit Spalten", len(fl) == 7 and fl[2] == (10, 13, "1000") and fl[0].text == "student", fl[:3])
check("felder(): durch Leerraum", s.raster("a  bb c", (0, 0)).felder(0) == [(0, 0, "a"), (3, 4, "bb"), (6, 6, "c")])
check("trenner(':'): sechs Doppelpunkte", g.trenner(0, ":") == [7, 9, 14, 19, 27, 41])
check("finde: zweites Vorkommen, regulärer Ausdruck", g.finde(0, "student", 2) == (34, 40)
      and g.finde(1, r"\d+", regex=True) == (7, 8))
try:
    g.finde(1, "anna")
    check("finde: fehlt -> Fehlermeldung", False)
except ValueError:
    check("finde: fehlt -> Fehlermeldung", True)
k, kt = g.klammer(0, 8, 11, "UID", seite="oben", farbe=BLAU)
ko = next(o for o in s.objects if o["id"] == k)
pts = [tuple(map(float, p.split(","))) for p in ko["props"]["points"].split(";")]
check("klammer oben: ein offener Linienzug (Shape), Schenkel zum Text, Beschriftung darüber",
      ko["type"] == "Shape" and ko["props"]["closed"] is False and len(pts) == 4 and pts[1][1] > pts[0][1]
      and abs(pts[0][0] - (g.x(8) + 0.02)) < 1e-4 and next(o for o in s.objects if o["id"] == kt)["props"]["position"][1] > pts[1][1])
tl = g.teil(0, 10, 13)
sc = bauen(s)
out = svg(sc)
xs, y = zeile(out, P)
cw = 0.6 * 20
check("x(sp): Zellmitte = gezeichnete Zeichenmitte (alle 50 Spalten)",
      all(abs(px(g.xm(c)) - xs[c]) < 0.02 for c in range(len(P))), (px(g.xm(0)), xs[0]))
check("y(z): Zeilenmitte = gezeichnete Grundlinie (central)", abs(py_(g.y(0)) - y) < 0.02 and
      abs(g.y(0) - g.y(1) - 1.35 * 20 / PX) < 1e-4)
xs2, _ = zeile(out.replace(P, ""), "1000")
check("teil: deckungsgleiche Kopie (dieselben x wie die Spalten 8..11 der Zeile)", xs2 is not None and
      [round(v, 1) for v in xs2] == [round(v, 1) for v in xs[10:14]], (xs2, xs[10:14]))
a = g.anker(0, 8, 11, "oben")
check("anker: oben = Mitte der Spalten, Oberkante der Zeile", a == (g.xm(8, 11), g.oben(0)))
check("anker: unten_links", g.anker(1, 0, 3, "unten_links") == (g.x(0), g.unten(1)))
# wert und faerben
s = Szene("t/wert", reihenfolge="anlegen")
g = s.raster("-rw-r--r-- 1 1000 1000 25 notizen.txt", (-3, 0), groesse=20)
tid, an = g.wert(0, 13, 16, "student")
g.faerben(0, [(0, 9, ORANGE)], rest=GRAU)
out = svg(bauen(s))
check("wert: Zeile mit Lücke, der Teil wird ersetzt (student an Spalte 13)", "-rw-r--r-- 1      1000 25" in out.replace("&amp;", "&")
      or "1      1000" in out, out[-600:])
xs3, _ = zeile(out, "student")
check("wert: neuer Wert beginnt an derselben Spalte", xs3 is not None and abs(xs3[0] - px(g.xm(13))) < 0.02)
check("faerben: Abschnitt orange (24 Bit), Rest grau, in einer Zeile", '<tspan fill="#eb6834">-rw-r--r--</tspan>' in out
      and '<tspan fill="#7f7f7f"> 1' in out, re.findall(r"<tspan[^>]*>[^<]*</tspan>", out)[:3])

# ---------------------------------------------------------------- 2. Terminal
s = Szene("t/term", reihenfolge="anlegen")
t = s.terminal(pos=(-3.4, 1.6))
a1 = t.eingabe("cd /etc")
a2 = t.prompt(pfad="/etc")
t.befehl("ls", "hostname  passwd")
t.warten()
t.leeren()
t.setze(0, 0, "X")
t.schliessen()
m = s.model()
anims = m["model"]["animations"]
par = next(o for o in m["model"]["objects"] if o["type"] == "Parameter")
tprops = next(o for o in m["model"]["objects"] if o["type"] == "Terminal")["props"]
check("Terminal: ein Parameter (term1), state nennt ihn", par["props"]["name"] == "term1" and tprops["state"] == "term1")
check("Terminal: je Schritt ein ChangeValue (linear) auf 1, 2, 3, …", [a["value"] for a in anims] == list(range(1, 9))
      and all(a["type"] == "ChangeValue" and a.get("rate") == "linear" for a in anims), [a.get("value") for a in anims])
check("eingabe: Dauer = Zeichen / 14 (cd /etc⏎ = 8 Zeichen)", abs(anims[0]["run_time"] - 8 / 14) < 1e-3)
check("Inhalt: Marken \\e| und \\e>, Prompt mit Pfad, leeren, setze mit Cursor sichern, schließen",
      tprops["text"].count("\\e|") == 8 and "\\e|\\e>cd /etc\n" in tprops["text"] and "\\e|student@labor:/etc$ " in tprops["text"]
      and "\\e[H\\e[2J" in tprops["text"] and "\\e[s\\e[1;1HX\\e[u" in tprops["text"] and tprops["text"].endswith("\\e|\\e!"))
check("Titel aus dem Prompt: student@labor: ~", tprops["title"] == "student@labor: ~")
# Anker des Terminals = gezeichnete Zellen
s = Szene("t/anker", reihenfolge="anlegen")
t = s.terminal(pos=(-3.4, 1.6), spalten=40, zeilen=4)
t.befehl("ls -l", "-rw-r--r-- 1 student student 25 a.txt")
sc = bauen(s)
out = svg(sc)
xs, y = zeile(out, "-rw-r--r--")
check("Terminal: x/y der Bildschirmzellen = gezeichnete Zeichen", abs(px(t.xm(0)) - xs[0]) < 0.02 and
      abs(px(t.xm(5)) - xs[5]) < 0.02 and abs(py_(t.y(1)) - y) < 0.02, (px(t.xm(0)), xs[0], py_(t.y(1)), y))
check("Terminal: felder der Bildschirmzeile im Endzustand", t.felder(1)[2] == (13, 19, "student"))
check("Terminal: zeilen(zustand) liest frühere Zustände", t.zeilen(0)[0] == "student@labor:~$" and t.zeilen()[2] == "student@labor:~$")
tid = t.teil(0, 0, 12)
tp = next(o for o in s.objects if o["id"] == tid)["props"]
check("Terminal: teil übernimmt Farben und Fettschrift (ANSI 24 Bit, grün fett)", tp.get("ansi") is True
      and "\\e[0;1;38;2;51;218;122m" in tp["text"], tp["text"][:60])
try:
    t.teil(3, 0, 5)                                   # Zeile 3 ist leer
    check("teil auf leeren Zellen -> Fehler (erst nach dem Schritt aufrufen, der sie schreibt)", False)
except ValueError:
    check("teil auf leeren Zellen -> Fehler (erst nach dem Schritt aufrufen, der sie schreibt)", True)
b, h = t.groesse
check("Terminal: Fensterkanten (links, rechts, oben_kante, unten_kante) passen zur Größe",
      abs(t.rechts - t.links - b) < 1e-3 and abs(t.oben_kante - t.unten_kante - h) < 1e-3 and t.links == -3.4)
t2 = s.terminal(pos=(0, 0))                           # Größe nach Bedarf
t2.x(3)                                               # Anker abgefragt: Fenstergröße festgehalten
try:
    t2.ausgabe("eine sehr lange Zeile, die das Fenster breiter machen würde")
    check("Schutz: Schritt nach Ankerabfrage, der die Fenstergröße ändert -> Fehler", False)
except ValueError:
    check("Schutz: Schritt nach Ankerabfrage, der die Fenstergröße ändert -> Fehler", True)
s = Szene("t/anker2")
t = s.terminal()
t.x(0)
t._ext_fest = (5, 1)                                  # so tun, als wären die Anker bei einer anderen Größe abgefragt
try:
    s._fenster_pruefen()                              # (das prüft speichern() vor dem Schreiben)
    check("speichern prüft die Fenstergröße der Anker", False)
except ValueError:
    check("speichern prüft die Fenstergröße der Anker", True)
# automatische Schriftgröße und Warnung
s = Szene("t/breit")
buf = io.StringIO()
with redirect_stdout(buf):
    t = s.terminal(text="x" * 84, spalten=84)
check("groesse=None: 84 Spalten passen in 6,9 Einheiten (Schrift ≥ 17 px, keine Warnung)",
      t.props["font_size"] >= 17 and t.groesse[0] <= 6.9 and "⚠" not in buf.getvalue(), (t.props["font_size"], t.groesse))
with redirect_stdout(buf):
    s.terminal(text="x" * 120, spalten=120)
check("zu viele Spalten: Warnung (Schrift unter 17 px)", "kleiner als 17" in buf.getvalue(), buf.getvalue())

# ---------------------------------------------------------------- 3. Datei, top, Pager, Schloss, Kürzel
s = Szene("t/datei")
d = s.datei("/etc/hostname", "labor")
check("datei: hell, Rahmen datei, nur ×, kein Cursor, keine Prompt-Farben", d.props["theme"] == "hell" and d.props["frame"] == "datei"
      and d.props["buttons"] == "x" and d.props["cursor"] is False and d.props["prompt_colors"] is False and d.props["title"] == "/etc/hostname")
d.zeile_dazu("neu")
check("datei: zeile_dazu = neue Zeile als Schritt", d.props["text"].endswith("\\e|\nneu"))
s = Szene("t/top")
tp = s.top(["top - 10:00:00 up 1 min", "Tasks:  70 total"], ["  PID USER  COMMAND", "    1 root  systemd-journald-sehr-lang"],
           spalten=26)
check("top: Cursor aus, Zahlen im Kopf fett, Spaltenzeile invers über die ganze Breite, lange Zeile mit +",
      tp.props["text"].startswith("\\e[?25l") and "\\e[1m70\\e[22m" in tp.props["text"]
      and "\\e[7m  PID USER  COMMAND       \\e[27m" in tp.props["text"] and "systemd-journ+" in tp.props["text"], tp.props["text"])
tp.bild(kopf=["top - 10:00:03 up 1 min", "Tasks:  70 total"])
schritt = tp.props["text"].split("\\e|")[1]
check("top.bild: nur geänderte Zeilen werden neu geschrieben", schritt == "\\e[1;1H\\e[Ktop - 10:00:03 up 1 min", schritt)
s = Szene("t/pager")
pg = s.pager(["a", "b", "c", "d", "e"], sichtbar=3)
check("Pager: Statuszeile invers „lines 1-3/5“", pg.props["text"].endswith("\\e[7mlines 1-3/5\\e[27m") and pg.props["rows"] == 4)
pg.weiter(5)
pg.weiter(-1)
teile = pg.props["text"].split("\\e|")
check("Pager: weiter blättert bis zum Ende (END) und zurück", "lines 3-5/5 (END)" in teile[1] and "lines 2-4/5" in teile[2])
s = Szene("t/schloss")
l1 = s.schloss((1, 2), groesse=0.5, offen=True)
lo = next(o for o in s.objects if o["id"] == l1)
check("schloss: Objekt Lock mit center, size, open, color", lo["type"] == "Lock" and lo["props"]["size"] == 0.5 and lo["props"]["open"])
check("farbig / fett / invers: ANSI-Kürzel", farbig("x", "gruen", True) == "\\e[1;32mx\\e[0m" and farbig("y", "#eb6834")
      == "\\e[38;2;235;104;52my\\e[0m" and fett("z") == "\\e[1mz\\e[22m" and invers("i") == "\\e[7mi\\e[27m")

# ---------------------------------------------------------------- 4. Mindestschriftgröße im Export
s = Szene("t/klein")
s.text(None, "winzig", (0, 0), 16)
s.text(None, "normal", (0, -1), 24)
sc = bauen(s)
_, info = ex.render(sc.objectList, sc.camera, background=(1, 1, 1))
k = es.kleinste_schrift(sc, info)
check("Export: kleinste Schrift 16 Szenenpixel -> 8,8 px im Artikel, unter dem Mindestmaß 9,3 px",
      k is not None and abs(k[0] - 8.8) < 1e-9 and k[1] == 16 and k[0] < ex.MIN_TEXT_PX, k)

print("\nF1 SZENEN-API TESTS " + ("PASSED" if ok else "FAILED"))
sys.exit(0 if ok else 1)

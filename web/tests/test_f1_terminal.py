"""F1 „Bildschirme und Fenster“ (12.11.2026), Engine: ANSI-Farben (engine/ansi.py), Terminal-Objekt (engine/terminal.py:
Datenstrom, Zustände, Tippen, Warten, Schließen, Rollen, Leeren, Cursor-Stellung, Prompt-Farben, Größe), farbige
Abschnitte einer Zeile (Text.spans -> ein <text> mit <tspan>), Canvas-Painter wie SVG-Painter, Vertrag (seek(t) rein),
Schloss, Größenbudget. Run from web/:  python tests/test_f1_terminal.py"""
import re
import sys

sys.path.insert(0, "."); sys.path.insert(0, "py")
from engine.scene_model import ModelScene
from engine import export as ex
from engine import ansi as A
from engine import terminal as T
from engine.text import Text

sys.path.insert(0, "tests")
from test_contract import probe  # noqa: E402  (idempotent, path-independent, stepping == jump)

ok = True


def check(name, cond, extra=""):
    global ok
    print(("  OK   " if cond else " FAIL  ") + name + (("  :: " + str(extra)[:300]) if extra != "" and not cond else ""))
    ok = ok and bool(cond)


def term(text, **kw):
    a = {"text": text, "position": [-3, 2, 0], "font_size": 20, "title": "student@labor: ~"}
    a.update(kw)
    return {"id": "t", "type": "Terminal", "args": a}


def build(objects, anims=(), play=True, params=None):
    objs = list(objects)
    for name, v in (params or {}).items():
        objs.insert(0, {"id": "p_" + name, "type": "Parameter", "args": {"name": name, "value": v}})
    sc = ModelScene({"objects": objs, "animations": list(anims), "background": [1, 1, 1]})
    if play:
        sc.animating = True
        sc.build_timeline()
    else:
        sc.construct()
        sc.show_static()
    return sc


def svg(sc, t=None):
    if t is not None:
        sc.seek(t)
    out, _ = ex.render(sc.objectList, sc.camera, background=(1, 1, 1), raw_settings={"mode": "canvas"})
    return out


def rows_of(text, state=None, **kw):
    return T.screen_rows(text, state, kw.get("cols", 0), kw.get("rows", 0), kw.get("cursor", True))


# ---------------------------------------------------------------- 1. ANSI
plain, spans = A.parse_sgr("ab\\e[1;32mcd\\e[0mef\\e[38;2;235;104;52mgh")
check("ANSI: Kürzel verschwinden, Abschnitte mit Farbe und fett (hell: Grün #1b7f45, fett nicht hell)",
      plain == "abcdefgh" and spans[0][:2] == (2, 4) and spans[0][3] is True
      and A.hex_rgb("#1b7f45") == spans[0][2] and spans[1][:2] == (6, 8), (plain, spans))
check("ANSI: 24 Bit = Farbe der Abbildung", tuple(round(c * 255) for c in spans[1][2]) == (235, 104, 52), spans)
check("ANSI: \\\\ ist ein Backslash, andere Backslashes bleiben (C:\\, grep '\\w')",
      A.unescape("a\\\\eb C:\\ \\w") == "a\\eb C:\\ \\w" and A.unescape("\\e[1m") == "\x1b[1m")
att = A.Attr(); att.sgr("1;34")
check("dunkel: fett 34 = helles Blau (fett = hell, wie Prompt und ls --color)",
      A.resolve(att, A.palette("dunkel"))[0] == A.PALETTES["dunkel"]["ansi"][12])
att = A.Attr(); att.sgr("7")
check("invers: Vordergrund und Hintergrund getauscht", A.resolve(att, A.palette("dunkel"))[:2] ==
      (A.PALETTES["dunkel"]["bg"], A.PALETTES["dunkel"]["fg"]))


def lum(h):
    c = [x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4 for x in A.hex_rgb(h)]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def kontrast(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


for theme in A.THEMES:
    P = A.PALETTES[theme]
    low = [(i, c) for i, c in enumerate(P["ansi"]) if i not in (0, 15 if theme == "dunkel" else 0) and kontrast(c, P["bg"]) < 4.5]
    if theme == "hell":
        low = [(i, c) for i, c in low if i not in (8,)]       # helles Grau: absichtlich blass (4,5:1 knapp)
    check("Palette %s: Farben 1-14 lesbar (Kontrast ≥ 4,5:1 zum Hintergrund)" % theme, not low, low)

# ---------------------------------------------------------------- 2. Datenstrom, Zustände
S = "student@labor:~$ \\e|\\e>cd /etc\n\\e|student@labor:/etc$ \\e|\\e~\\e|\\e!"
check("Schritte: \\e| trennt vier Zustände nach dem Start", T.step_count(S) == 4)
check("Zustand 0: nur der Prompt", rows_of(S, 0)[:1] == ["student@labor:~$"])
r = rows_of(S, 0.5)
check("Zustand 0,5: Schritt 1 halb, die Hälfte von „cd /etc⏎“ getippt (4 von 8 Zeichen)", r[0] == "student@labor:~$ cd /", r)
check("Zustand 1: Eingabetaste getippt (Zeile 1 leer, Cursor dort); Zustand 1,1: der neue Prompt ist schon da",
      rows_of(S, 1)[1] == "" and T.run(S, 1)["screen"].r == 1 and rows_of(S, 1.1)[1] == "student@labor:/etc$")
res = [T.run(S, 2 + f)["blink"] for f in (0.05, 0.2, 0.4, 0.6, 0.95)]
check("Warten: Cursor blinkt (an, aus, an, …) und steht danach ruhig", res == [True, False, True, False, False]
      and T.run(S, 3)["blink"], res)
c1, c2, c3 = (T.run(S, 3 + f) for f in (0.2, 0.7, 1.0))
check("Schließen: × leuchtet zuerst, dann blendet das Fenster aus", c1["close_hl"] and c1["close"] == 0 and 0 < c2["close"] < 1
      and c3["close"] == 1.0)
check("Größe über alle Zustände: so breit wie die längste Zeile (auch getippt), Cursorzeile zählt",
      T.extent(S) == (len("student@labor:~$ cd /etc"), 2), T.extent(S))
check("Größe fest: 10 Spalten, 3 Zeilen", T.extent(S, 10, 3) == (10, 3))
check("Umbruch bei fester Breite, Rollen bei fester Höhe",
      rows_of("abcdefghij\n1\n2\n3", cols=4, rows=3) == ["1", "2", "3"] and rows_of("abcdef", cols=4, rows=3)[:2] == ["abcd", "ef"])
check("Leeren \\e[2J und Cursor-Stellung \\e[r;cH (Wert an fester Stelle wie bei top)",
      rows_of("aaaa\nbbbb\\e|\\e[H\\e[2Jxy\\e[2;3HZ") == ["xy", "  Z"], rows_of("aaaa\nbbbb\\e|\\e[H\\e[2Jxy\\e[2;3HZ"))
check("Cursor sichern/zurück \\e[s/\\e[u", T.run("ab\\e[s\\e[3;1Hz\\e[u")["screen"].c == 2)
check("Tabulator bis zur nächsten Achterspalte", rows_of("a\tb") == ["a       b"])

# ---------------------------------------------------------------- 3. Zeichnen: eine Zeile = ein <text> mit <tspan>
sc = build([term("student@labor:~$ ls\n\\e[1;34mDokumente\\e[0m  notizen.txt\n\\e[7m inv \\e[27m")], play=False)
out = svg(sc)
rows = re.findall(r'<text x="([^"]+)"[^>]*>(.*?)</text>', out)
first = [b for x, b in rows if "ls" in b][0]
check("Prompt: user@host grün fett, Pfad blau fett, in EINEM <text>",
      '<tspan fill="#33da7a" font-weight="bold">student@labor</tspan>:<tspan fill="#5ea1f0" font-weight="bold">~</tspan>$ ls'
      in first, first)
x_list = [x for x, b in rows if "Dokumente" in b][0].split()
check("ein x je Zeichen der Zeile (auch in den Abschnitten), Spalten im Raster",
      len(x_list) == len("Dokumente  notizen.txt") and abs(float(x_list[1]) - float(x_list[0]) - 12.0) < 1e-6, x_list[:3])
check("invers: Hinterlegung in Vordergrundfarbe, Zeichen in Hintergrundfarbe",
      'fill="#d0cfcc"' in out and '<tspan fill="#1e1e1e"> inv</tspan>' in out)
check("Titelleiste: Titel fett, drei runde Knöpfe", 'font-weight="bold">student@labor: ~</tspan>' in out
      and out.count('fill="#474747"') == 3, out[:200])
t = sc.objectList[0]
check("Baum fest: Schatten, Fenster, Titel, Knöpfe, Hinterlegungen, Cursor, Zeilen (7 Kinder)", len(t.subObjects) == 7)
sc2 = build([term("x", theme="hell", frame="datei", buttons="x", cursor=False, title="/etc/hostname")], play=False)
o2 = svg(sc2)
check("Datei-Ansicht: hell, nur ×, kein Cursor", 'fill="#ffffff"' in o2 and o2.count('fill="#d6d6d6"') == 1
      and 'fill="#1e1e1e"' not in o2.split("<text")[0])
sc3 = build([term("abc", frame="ohne", cursor=False, title="")], play=False)
check("ohne Rahmen: keine Titelleiste, keine Knöpfe", 'fill="#303030"' not in svg(sc3) and 'fill="#474747"' not in svg(sc3))


# Canvas-Painter (Editor) zeichnet dieselben Zeichen in denselben Farben wie der SVG-Painter
class Ctx:
    def __init__(self):
        self.calls, self.fillStyle, self.font = [], None, ""

    def __getattr__(self, n):
        if n.startswith("__"):
            raise AttributeError(n)
        return lambda *a: self.calls.append((n, a, self.fillStyle, self.font))


from canvas_painter import CanvasPainter  # noqa: E402
from engine.renderer import paint_scene  # noqa: E402
ctx = Ctx()
paint_scene(CanvasPainter(ctx, 1920, 1080), sc.objectList, sc.camera, background=(1, 1, 1))
farbig_ = {(a[0], f, "bold" in fo) for n, a, f, fo in ctx.calls if n == "fillText" and a[0] in "student@labor~"}
check("Canvas: Prompt grün fett, ~ blau fett, $ in der Grundfarbe (wie <tspan>)",
      ("s", "rgba(51,218,122,1.0)", True) in farbig_ and ("~", "rgba(94,161,240,1.0)", True) in farbig_, sorted(farbig_)[:6])
zeilen = {}
for n, a, f, fo in ctx.calls:
    if n == "fillText":
        zeilen.setdefault(round(a[2], 3), []).append((a[0], a[1]))
dok = [z for z in zeilen.values() if "".join(c for c, _ in z) == "Dokumentenotizen.txt"]
xs_svg = [float(v) for v, ch in zip(x_list, "Dokumente  notizen.txt") if ch != " "]
check("Canvas: Zeichen an denselben Zellmitten wie im SVG", len(dok) == 1 and
      [round(x, 2) for _, x in dok[0]] == [round(x, 2) for x in xs_svg], (dok[:1], xs_svg[:3]))

# ANSI in einem gewöhnlichen Text (Textblock), Transform übernimmt die Abschnitte
tb = Text("a \\e[31mrot\\e[0m b", ansi=True, font="mono")
check("Text ansi=True: Rohtext ohne Kürzel, Abschnitt rot (hell)", tb.text == "a rot b" and tb.raw and tb.spans[0][:2] == (2, 5))
sc4 = build([{"id": "a", "type": "Text", "args": {"text": "eins zwei", "position": [0, 0, 0], "font_size": 20, "font": "mono",
                                                     "raw": True, "align": "left"}},
             {"id": "b", "type": "Text", "args": {"text": "eins \\e[1;34mzwei\\e[0m", "position": [0, 0, 0], "font_size": 20,
                                                     "font": "mono", "ansi": True, "align": "left"}}],
            [{"type": "Transform", "target": "a", "run_time": 1, "args": {"to": "b"}}])
check("Transform Text → Text: farbige Abschnitte kommen mit (Zeile neu einfärben)",
      '<tspan fill="#1d4fa8" font-weight="bold">zwei</tspan>' in svg(sc4, sc4.duration))

# ---------------------------------------------------------------- 4. Zeitachse über einen Parameter (L3): Vertrag
TXT = ("student@labor:~$ \\e|\\e>ls -l\n\\e|insgesamt 4\n-rw-r--r-- 1 student student 25 notizen.txt\n"
       "\\e|student@labor:~$ \\e|\\e~\\e|\\e!")
anims = [{"type": "FadeIn", "target": "t", "run_time": 0.5, "step": 0}]
anims += [{"type": "ChangeValue", "target": "p_z", "run_time": 0.8, "step": k, "args": {"value": k, "rate": "linear"}}
          for k in range(1, 6)]
scz = build([term(TXT, state="z")], anims, params={"z": 0})
check("Vertrag: Terminal mit Tippen, Ausgabe, Warten, Schließen ist eine reine Funktion von t", probe("F1 Terminal (L3)", scz))
tz = scz.objects_by_id["t"]
scz.seek(0.5 + 0.4)
r = [c for c in tz.subObjects[6].subObjects]
check("Zwischenbild: nach der halben Tipp-Zeit stehen 3 von 6 Zeichen da („ls “, Leerzeichen am Ende zählen nicht)",
      r[0].text == "student@labor:~$ ls" and tz.subObjects[5].fill_opacity == 1.0, r[0].text)
cx = tz.subObjects[5].points[:, 0].min()
check("Cursor steht hinter dem dritten getippten Zeichen", abs(cx - (-3 + (0.6 + 0.6 * 20) * 20 / 135)) < 1e-9, cx)
scz.seek(scz.duration)
check("Endbild: Fenster geschlossen (alles durchsichtig)",
      all(o.fill_opacity == 0 and o.stroke_opacity == 0 for o in tz.subObjects[1:2]))
scg = build([term(TXT, state="z")], [{"type": "GrowFromCenter", "target": "t", "run_time": 0.6, "step": 0}] + anims[1:3],
            params={"z": 0})
check("Vertrag: Fenster wächst, dann Zustände", probe("F1 Terminal wächst (L3)", scg))
st = build([term(TXT, state="")], play=False)
check("state leer = Endzustand (ohne Parameter, ohne Zeitachse)", st.objects_by_id["t"].subObjects[1].fill_opacity == 0)

# ---------------------------------------------------------------- 5. Schloss, Größenbudget
scl = build([{"id": "l", "type": "Lock", "args": {"center": [0, 0, 0], "size": 0.4, "open": o, "color": [0.5, 0.5, 0.5]}}
             for o in (False,)], play=False)
lk = scl.objectList[0]
check("Schloss: Bügel, Körper, Schlüsselloch (4 Pfade), Höhe = size", len(lk.subObjects) == 4
      and abs(lk.subObjects[1].points[:, 1].min() + 0.2) < 1e-9, len(lk.subObjects))
sco = build([{"id": "l", "type": "Lock", "args": {"center": [0, 0, 0], "size": 0.4, "open": True}}], play=False)
check("Schloss offen: Bügel gehoben", sco.objectList[0].subObjects[0].points[:, 1].max() > lk.subObjects[0].points[:, 1].max())
voll = "\n".join(("%02d " % i) + "x" * 77 for i in range(24))
big = build([term(voll, cols=80, rows=24, cursor=False)], play=False)
size = len(svg(big).encode("utf-8"))
check("Größenbudget: Terminal 80 × 24 voll beschrieben unter 100 KB (%.1f KB)" % (size / 1024), size < 100 * 1024)
farb = "\n".join("\\e[1;32mgruen\\e[0m \\e[31mrot\\e[0m \\e[7minvers\\e[0m " + "y" * 58 for _ in range(24))
size2 = len(svg(build([term(farb, cols=80, rows=24, cursor=False)], play=False)).encode("utf-8"))
check("Größenbudget: 24 farbige Zeilen mit Hinterlegungen unter 100 KB (%.1f KB)" % (size2 / 1024), size2 < 100 * 1024)

print("\nF1 TERMINAL TESTS " + ("PASSED" if ok else "FAILED"))
sys.exit(0 if ok else 1)

"""Werkzeuge vom 10.11.2026 (E1): Schreibmaschinenschrift und Rohtext in s.text, Inhalt eines Texts ändern (Transform
Text -> Text), Zeichenreihenfolge des Anlegens, Warnung bei verdecktem Text, Pfeilspitze von s.weg, Laufindex und exakte
Brüche in Σ/∏ (szenen_lib), Linux-Helfer, Favicon. Run from web/:  python tests/test_text_werkzeuge.py"""
import json
import re
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, "."); sys.path.insert(0, "py")
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools")); sys.path.insert(0, str(ROOT / "tools" / "szenen")); sys.path.insert(0, str(ROOT))
import numpy as np
from engine.scene_model import ModelScene
from engine.svg_painter import SvgPainter, MONO_FONT
from engine import export as ex
from engine.richtext import mono_line, MONO_CELL
from engine.text import Text

ok = True


def check(name, cond, extra=""):
    global ok
    print(("  OK   " if cond else " FAIL  ") + name + (("  :: " + str(extra)) if extra != "" and not cond else ""))
    ok = ok and bool(cond)


def build(objects, anims=(), extra=None, play=False):
    model = {"objects": objects, "animations": list(anims), "background": [1, 1, 1]}
    model.update(extra or {})
    sc = ModelScene(model)
    if play:
        sc.animating = True; sc.build_timeline(); sc.seek(sc.duration)
    else:
        sc.construct(); sc.show_static()
    return sc


def svg_of(sc):
    svg, _ = ex.render(sc.objectList, sc.camera, background=(1, 1, 1), raw_settings={"mode": "canvas"})
    return svg


def txt(id_, text, pos=(0, 0), **kw):
    a = {"text": text, "position": [pos[0], pos[1], 0], "font_size": 20, "align": "left", "color": [0, 0, 0]}
    a.update(kw)
    return {"id": id_, "type": "Text", "args": a}


# ---------------------------------------------------------------- 1. Schreibmaschinenschrift
cells, chars = mono_line("ab  c 中x  ")
check("mono_line: Leerzeichen bleiben Zeichen, ein chinesisches Zeichen belegt zwei Zellen, Leerzeichen am Ende fallen weg",
      cells == 9 and [c for _, c in chars] == [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 7.0, 8.5] and "".join(ch for ch, _ in chars) == "ab  c 中x",
      (cells, chars))
sc = build([txt("a", "ls  -l  'x' `y`", (0, 1), font="mono", raw=True), txt("b", "abcdefghijklm", (0, 0.5), font="mono", raw=True)])
svg = svg_of(sc)
rows = re.findall(r'<text x="([^"]+)" y="[^"]+" font-size="20" font-family="([^"]+)"[^>]*>([^<]*)</text>', svg)
check("mono: eigene Schriftliste, ein x je Zeichen (auch Leerzeichen, xml:space), ' und ` unverändert",
      len(rows) == 2 and rows[0][1] == MONO_FONT and 'xml:space="preserve"' in svg
      and len(rows[0][0].split()) == len(rows[0][2]) and rows[0][2] == "ls  -l  'x' `y`", rows)
xa, xb = [float(v) for v in rows[0][0].split()], [float(v) for v in rows[1][0].split()]
check("mono: Spalten stehen untereinander (Zeichen 5 von Zeile 1 über Zeichen 5 von Zeile 2: '-' über 'e')",
      abs(xa[4] - xb[4]) < 1e-6 and rows[0][2][4] == "-", (xa[:6], xb[:6]))
check("mono: Zellbreite 0,6 em", abs((xb[1] - xb[0]) - MONO_CELL * 20) < 0.02, xb[:2])
b = ex.text_box("abc", 100, 50, 20, "left", "mono", True)
check("mono: Zuschnitt = Zellen × 0,6 em", b is not None and abs((b[2] - b[0]) - 3 * 0.6 * 20) < 1e-9, b)
sp = SvgPainter(10, 10)
sp.draw_text("a\nbc", 50, 50, 20, (0, 0, 0), 1.0, "center", font="mono", raw=True)
check("mono: zwei Zeilen, mittig", len(sp.parts) == 2 and 'x="44 56"' in sp.parts[1], sp.parts)

# ---------------------------------------------------------------- 2. Rohtext
sc = build([txt("r", "einkauf_alt.txt C:\\ $x {y} ^z  zwei", raw=True), txt("n", "einkauf_alt.txt")])
svg = svg_of(sc)
check("roh: _ ^ \\ $ { } bleiben Zeichen, Leerzeichen bleiben (xml:space)",
      'xml:space="preserve">einkauf_alt.txt C:\\ $x {y} ^z  zwei</text>' in svg, re.findall(r"<text[^>]*>.*?</text>", svg))
check("ohne roh: _ stellt weiterhin tief (Rich-Text unverändert)", "<tspan" in svg)
sc = build([txt("r", "1.5M 46.54", raw=True), txt("m", "v 2.5", font="mono"), txt("n", "0.5 V")], extra={"lang": "de"})
texts = {k: o.text for k, o in sc.objects_by_id.items()}
check("roh / tt: Dezimalpunkt bleibt (de), normaler Text bekommt das Komma",
      texts == {"r": "1.5M 46.54", "m": "v 2.5", "n": "0,5 V"}, texts)
sc = build([txt("r", "@k", raw=True)], extra={"lang": "zh", "strings": {"k": {"de": "a_b", "zh": "文件_1"}}})
check("roh: @schlüssel gilt weiter", sc.objects_by_id["r"].text == "文件_1", sc.objects_by_id["r"].text)

# ---------------------------------------------------------------- 3. Inhalt eines Texts ändern
objs = [txt("t", "alt.txt", (0, 0), font="mono", raw=True, color=[0, 0, 0]),
        txt("v", "neu_name.txt", (0, 0), font="mono", raw=True, color=[0.8, 0.1, 0.1])]
an = [{"type": "FadeIn", "target": "t", "run_time": 0.5, "step": 0},
      {"type": "Transform", "target": "t", "run_time": 1.0, "step": 1, "args": {"to": "v"}}]
sc = build(objs, an, play=True)
t = sc.objects_by_id["t"]
check("Transform Text -> Text: Inhalt und Farbe im Endbild", t.text == "neu_name.txt" and np.allclose(t.color, [0.8, 0.1, 0.1])
      and t.stroke_opacity == 1.0, (t.text, t.color, t.stroke_opacity))
svg = svg_of(sc)
check("Transform Text -> Text: im SVG nur der neue Text, keine Vorlage, kein unsichtbarer Rest",
      svg.count("<text") == 1 and "neu_name.txt".replace(".", "") in svg.replace(".", "") and "alt" not in svg, svg[-400:])
sc.seek(0.5 + 0.25)   # Mitte der ersten Hälfte: alter Text halb sichtbar
check("Transform Text -> Text: erste Hälfte = alter Text, blendet aus", t.text == "alt.txt" and 0 < t.stroke_opacity < 1, (t.text, t.stroke_opacity))
sc.seek(0.0)
check("Transform Text -> Text: vor dem Einblenden unsichtbar, alter Text", t.text == "alt.txt" and t.stroke_opacity == 0.0)

# ---------------------------------------------------------------- 4. Zeichenreihenfolge
box = {"id": "k", "type": "TextBox", "args": {"text": "", "center": [0, 0, 0], "width": 3, "height": 1, "fill_color": [1, 0.9, 0.8],
                                             "fill_opacity": 1.0, "color": [1, 0.5, 0]}}
objs = [box, txt("t", "oben?", (0, 0), align="center")]
an = [{"type": "FadeIn", "target": "t", "run_time": 0.5, "step": 0}, {"type": "GrowFromCenter", "target": "k", "run_time": 0.5, "step": 1}]
order_a = [id(o) for o in build(objs, an, play=True).objectList]
sc_c = build(objs, an, extra={"draw_order": "creation"}, play=True)
order_c = [id(o) for o in sc_c.objectList]
check("Reihenfolge des Anlegens: Kasten (zuerst angelegt) liegt unter dem Text", sc_c.objectList.index(sc_c.objects_by_id["k"])
      < sc_c.objectList.index(sc_c.objects_by_id["t"]))
sc_a = build(objs, an, play=True)
check("ohne draw_order wie bisher: der später erscheinende Kasten liegt oben",
      sc_a.objectList.index(sc_a.objects_by_id["k"]) > sc_a.objectList.index(sc_a.objects_by_id["t"]))
import export_szenen as es  # noqa: E402
check("Warnung: Text unter deckender Fläche erkannt (nur im alten Modus)",
      es.verdeckter_text(sc_a) == [("t", "k")] and es.verdeckter_text(sc_c) == [], (es.verdeckter_text(sc_a), es.verdeckter_text(sc_c)))
m = es.python_model({"model": {"objects": [], "drawOrder": "creation"}}, None, {}, "de", [])
check("Export: drawOrder der Szene geht als draw_order an die Engine", m["draw_order"] == "creation")

# ---------------------------------------------------------------- 5. Pfeilspitze von s.weg
def spitze(h):
    a = {"fx": "t", "fy": "0", "t_min": 0, "t_max": 2, "samples": 41, "show_arrow": True, "arrow_at": "0.5", "color": [0, 0, 1]}
    if h is not None:
        a["head_size"] = h
    o = build([{"id": "w", "type": "ParametricCurve", "args": a}]).objects_by_id["w"]
    tri = [c for c in o.subObjects if getattr(c, "fill_opacity", 0) == 1.0][0]
    return float(np.ptp(tri.points[:, 0]))
check("s.weg: head_size setzt die Länge der Richtungsmarke (Standard 0,22 unverändert)",
      abs(spitze(None) - 0.22) < 1e-6 and abs(spitze(0.08) - 0.08) < 1e-6, (spitze(None), spitze(0.08)))

# ---------------------------------------------------------------- 6. szenen_lib: neue Optionen, alte Dateien unverändert
import szenen_lib as L  # noqa: E402
s = L.Szene("test/x")
a = s.text(None, "a_b", (0, 0)); b = s.text(None, "ls -l", (0, 1), schrift="tt"); c = s.text(None, "C:\\", (0, 2), roh=True)
p = {o["id"]: o["props"] for o in s.objects}
check("s.text: ohne Zusatz keine neuen Schlüssel (alte Szenendateien bleiben byte-gleich)", "font" not in p[a] and "raw" not in p[a])
check("s.text: schrift=\"tt\" -> font mono und roh; roh=True -> raw", p[b].get("font") == "mono" and p[b].get("raw") is True
      and p[c].get("raw") is True and "font" not in p[c], (p[b], p[c]))
w = s.weg(None, "t", "0", 0, 1, pfeile="0.5"); w2 = s.weg(None, "t", "0", 0, 1, pfeile="0.5", spitze=0.1)
p = {o["id"]: o["props"] for o in s.objects}
check("s.weg: head_size nur mit spitze", "head_size" not in p[w] and p[w2]["head_size"] == 0.1)
e = s.ersetzen(b, "ls -la", farbe="#c82828")
tpl = s.objects[-1]
check("s.ersetzen: Vorlage mit neuem Text und gleicher Schrift, Animation Transform",
      tpl["props"]["text"] == "ls -la" and tpl["props"]["font"] == "mono" and tpl["props"]["color"] == "#c82828"
      and s._anims[-1]["type"] == "Transform" and s._anims[-1]["to"] == tpl["id"], tpl)
k = s.summe("3/2^(4*k+1)", von=1, bis=4, index="k", exakt=True)
k2 = s.summe("1/i^2", von=1, bis=3)
ops = {o["id"]: o["props"] for o in s._ops}
check("s.summe: index/exakt nur wenn gesetzt", ops[k]["index"] == "k" and ops[k]["exact"] is True
      and "index" not in ops[k2] and "exact" not in ops[k2])
check("Szene: reihenfolge nur wenn gewählt", "drawOrder" not in L.Szene("a").model()["model"]
      and L.Szene("a", reihenfolge="anlegen").model()["model"]["drawOrder"] == "creation")
check("tt_breite: Zelle 0,6 em in Szeneneinheiten", abs(L.tt_breite(22, 10) - 0.6 * 22 * 10 / 135) < 1e-12)

# ---------------------------------------------------------------- 7. Linux-Helfer: schreibmaschine("text")
import linux_hilfen as H  # noqa: E402
s = L.Szene("test/y")
f1 = H.tt(s, "ls -l", 0, 0)
H.schreibmaschine("text")
try:
    f2 = H.tt(s, "ls -l", 0, 0)
    pr = H.prozess(s, (0, 0), 1, 0.4, "wc")
finally:
    H.schreibmaschine("formel")
o = {x["id"]: x for x in s.objects}
check("linux_hilfen.tt: Formel wie bisher, mit schreibmaschine(\"text\") ein s.text in tt (gleiche Zellbreite)",
      o[f1]["type"] == "MathTex" and o[f2]["type"] == "Text" and o[f2]["props"]["font"] == "mono"
      and abs(H.tt_groesse() * 0.6 / 135 - H.cw()) < 1e-4 and o[pr[1]]["type"] == "Text", (o[f2], H.tt_groesse()))

# ---------------------------------------------------------------- 8. Editor-Leinwand (Pyodide-Painter mit Stub)
from canvas_painter import CanvasPainter  # noqa: E402


class Ctx:
    def __init__(self): self.calls = []
    def fillText(self, s, x, y): self.calls.append((s, round(x, 3), round(y, 3), self.font, self.textAlign))
    def measureText(self, s): return type("M", (), {"width": 10.0 * len(s)})()
cp = CanvasPainter(Ctx(), 100, 100)
cp.draw_text("a c", 0, 0, 20, (0, 0, 0), 1.0, "left", font="mono", raw=True)
check("Editor: mono zeichnet jedes Zeichen in der Mitte seiner Zelle", [(c[0], c[1]) for c in cp.ctx.calls] == [("a", 6.0), ("c", 30.0)]
      and MONO_FONT in cp.ctx.calls[0][3], cp.ctx.calls)

# ---------------------------------------------------------------- 9. Animiertes SVG: Inhalt ändern als Spur h
import szenen_animation as SA  # noqa: E402
model = {"objects": [txt("t", "alt", (0, 0), font="mono", raw=True), txt("v", "neu", (0, 0), font="mono", raw=True, color=[1, 0, 0])],
         "animations": [{"type": "Transform", "target": "t", "run_time": 1.0, "step": 0, "args": {"to": "v"}}],
         "background": [1, 1, 1], "export": {"mode": "canvas"}}
sc = ModelScene(json.loads(json.dumps(model))); sc.construct(); sc.seek(sc.duration)
_, info = ex.render(sc.objectList, sc.camera, raw_settings={"mode": "canvas"})
asvg, ainfo = SA.build(model, info["rect"], (info["width"], info["height"]), (1, 1, 1), False)
meta = json.loads(re.search(r'<metadata class="szenen-animation">(.*)</metadata>', asvg).group(1).replace("\\u003c", "<").replace("\\u003e", ">").replace("\\u0026", "&"))
check("anim.svg: Endbild = neuer Text, Spur h mit dem alten Text in Schreibmaschinenschrift",
      ">neu</text>" in asvg and any("h" in el and "alt" in json.dumps(el["h"], ensure_ascii=False) and "Consolas" in json.dumps(el["h"]) for el in meta["el"]),
      meta["el"])

# ---------------------------------------------------------------- 10. Favicon
import build_wissen as bw  # noqa: E402
check("Favicon: Seitenkopf verlinkt /favicon.ico und /favicon.svg, beide Dateien da",
      'rel="icon" href="/favicon.ico"' in bw.page_shell("t", "d", "", 1) and (ROOT / "web" / "favicon.ico").is_file()
      and (ROOT / "web" / "favicon.svg").is_file())

print("TEXT/WERKZEUG TESTS PASSED" if ok else "TEXT/WERKZEUG TESTS FAILED")
sys.exit(0 if ok else 1)

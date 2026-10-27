"""Vorlagen des Editors (Elektrotechnik): definiert die Vorlagen-Szenen und fügt sie in web/editor.js ein
(TEMPLATES + TEMPLATE_GROUPS, zwischen Markierungskommentaren, wiederholbar).
Aufruf (aus dem Repo): python tools/editor_vorlagen.py [--json <ordner>]
--json schreibt jede Vorlage zusätzlich als Szene (Speicherformat des Editors) für tools/editor_shot.py.
Nur die vom Standard abweichenden Eigenschaften stehen hier; migrateModel() im Editor ergänzt den Rest."""
import json
import sys
from pathlib import Path

BLACK, BLUE, RED, GREEN, PURPLE, GREY = "#111111", "#1f77b4", "#d62728", "#2ca02c", "#9467bd", "#888888"


def o(key, t, on=None, **props):
    d = {"key": key, "type": t, "props": props}
    if on:
        d["on"] = on
    return d


def bare(key="pa"):
    """A bare panel with 1:1 data = world units over the whole canvas (schematics, sections, blocks)."""
    return o(key, "Axes", x_range=[-7, 7], y_range=[-4, 4], x_length=14, y_length=8, show_axes=False)


T = {}

# 1. MOSFET output characteristics with load line and operating point (Parameter U_B moves it)
curve = "where(x < k-1, 2*((k-1)*x - x^2/2), (k-1)^2)"
T["Kennlinienfeld mit Arbeitspunkt"] = {"objects": [
    o("ax", "Axes", x_range=[0, 6], y_range=[0, 10], x_length=9.6, y_length=5.8, origin=[-0.6, -0.2],
      x_label="U_{DS} / V", y_label="I_D / mA", arrows=True, axis_width=2.5, number_size=22, label_size=26,
      grid_x=True, grid_y=True, grid_color="#e2e2e2"),
    o("ub", "Parameter", name="UB", value=5.0, min=2.0, max=6.0, step=0.1),
    o("fam", "CurveFamily", "ax", func=curve, param="k", values="2;2.5;3;3.5;4",
      labels="U_{GS} = 2 V;2,5 V;3 V;3,5 V;4 V", x_min=0, x_max=6, samples=200, fade=False, font_size=20,
      color=GREEN, stroke_width=3),
    o("gr", "FunctionGraph", "ax", func="x^2", x_range=[0, 3.2], color=GREY, stroke_width=2, dash="6,5"),
    o("ll", "FunctionGraph", "ax", func="2*(UB - x)", x_range=[0, 6], color=PURPLE, stroke_width=3),
    o("ap", "Marker", "ax", point=[3, 0, 0], func="where(x < 2, 2*(2*x - x^2/2), 4)", func2="2*(UB - x)",
      label="AP", label_pos="ne", show_guides=True, radius=0.09, font_size=24, color=RED),
    o("t1", "Text", "ax", text="Arbeitsgerade", position=[0.15, 9.3, 0], font_size=22, align="left", color=PURPLE),
    o("t2", "Text", "ax", text="Sättigungsgrenze", position=[3.15, 9.6, 0], font_size=20, align="left", color=GREY),
]}

# 2. Diode characteristic on a semi-log axis with the slope triangle (one decade per 59.5 mV)
diode = "1e-16*(exp(x/0.02585)-1)"
T["Diodenkennlinie halblogarithmisch"] = {"objects": [
    o("ax", "Axes", x_range=[0, 0.9], y_range=[1e-12, 1e-2], x_length=9.6, y_length=5.8, origin=[-0.6, -0.2],
      x_label="U / V", y_label="I / A", y_log=True, arrows=True, axis_width=2.5, number_size=22, label_size=26,
      grid_x=True, grid_y=True, grid_color="#e2e2e2"),
    o("g", "FunctionGraph", "ax", func=diode, x_range=[0, 0.9], color=BLUE, stroke_width=3),
    o("tg", "TangentLine", "ax", func=diode, x0=0.55, half_len=0.12, show_point=False, triangle_dx=0.0595,
      dx_label="59,5 mV", dy_label="×10", font_size=20, color=RED, stroke_width=2, dash="7,5"),
    o("m", "Marker", "ax", point=[0.7738, 0, 0], func=diode, label="1 mA bei 774 mV", label_pos="nw",
      show_guides=True, radius=0.08, font_size=20, color=BLACK),
]}

# 3. Bode diagram of an RC low-pass: magnitude and phase stacked on the same log frequency axis
mag = "-10*log10(1+(x/fg)^2)"
T["Bode-Diagramm Tiefpass"] = {"objects": [
    o("a1", "Axes", x_range=[10, 100000], y_range=[-60, 10], x_length=10, y_length=3.0, origin=[-0.3, 1.95],
      x_label="", y_label="|H| / dB", x_log=True, x_numbers=False, axis_width=2.5, number_size=20, label_size=24,
      grid_x=True, grid_y=True, grid_color="#e2e2e2"),
    o("a2", "Axes", x_range=[10, 100000], y_range=[-90, 0], x_length=10, y_length=3.0, origin=[-0.3, -1.85],
      x_label="f / Hz", y_label="φ / °", x_log=True, x_axis_at="bottom", axis_width=2.5, number_size=20,
      label_size=24, grid_x=True, grid_y=True, grid_color="#e2e2e2"),
    o("fg", "Parameter", name="fg", value=1000.0, min=100.0, max=10000.0, step=100.0),
    o("h", "FunctionGraph", "a1", func=mag, x_range=[10, 100000], color=BLUE, stroke_width=3),
    o("as", "FunctionGraph", "a1", func="where(x < fg, 0, -20*log10(x/fg))", x_range=[10, 100000], color=GREY,
      stroke_width=2, dash="7,5"),
    o("m3", "Marker", "a1", point=[1000, 0, 0], x_expr="fg", func=mag, label="−3 dB", label_pos="sw",
      show_guides=False, radius=0.08, font_size=20, color=RED),
    o("sl", "Text", "a1", text="−20 dB/Dekade", position=[15000, -13, 0], font_size=20, align="left", color=GREY),
    o("p", "FunctionGraph", "a2", func="-arctan(x/fg)*180/pi", x_range=[10, 100000], color=BLUE, stroke_width=3),
    o("m4", "Marker", "a2", point=[1000, 0, 0], x_expr="fg", func="-arctan(x/fg)*180/pi", label="−45°",
      label_pos="ne", show_guides=False, radius=0.08, font_size=20, color=RED),
]}

# 4. Common-emitter stage (schematic): voltage divider, R_C, R_E, coupling capacitors
T["Schaltplan Emitterschaltung"] = {"objects": [
    bare(),
    o("t", "Device", "pa", kind="npn", center=[1, 0, 0], label="T_1", size=1.0, font_size=24),
    o("r1", "Component", "pa", kind="resistor", start=[-1, 3, 0], end=[-1, 0, 0], label="R_1", size=0.9, font_size=24),
    o("r2", "Component", "pa", kind="resistor", start=[-1, 0, 0], end=[-1, -3, 0], label="R_2", size=0.9, font_size=24),
    o("rc", "Component", "pa", kind="resistor", start=[1.5, 3, 0], end=[1.5, 1, 0], label="R_C", current="I_C",
      size=0.9, font_size=24),
    o("re", "Component", "pa", kind="resistor", start=[1.5, -1, 0], end=[1.5, -3, 0], label="R_E", size=0.9, font_size=24),
    o("c1", "Component", "pa", kind="capacitor", start=[-3.5, 0, 0], end=[-1, 0, 0], label="C_1", size=0.9, font_size=24),
    o("c2", "Component", "pa", kind="capacitor", start=[1.5, 1, 0], end=[4, 1, 0], label="C_2", size=0.9, font_size=24),
    o("wb", "Wire", "pa", points="-1,0;0,0", dots="0"),
    o("wv", "Wire", "pa", points="-1,3;4,3", dots="1"),
    o("wg", "Wire", "pa", points="-1,-3;1.5,-3", dots=""),
    o("wc", "Wire", "pa", points="1.5,1;1.5,1", dots="0"),
    o("gnd", "Device", "pa", kind="ground", center=[0.25, -3, 0], label="", size=1.0),
    o("dg", "Node", "pa", center=[0.25, -3, 0], label="", dot=True),
    o("ti", "Device", "pa", kind="terminal", center=[-3.5, 0, 0], label="u_e", size=1.0, font_size=24),
    o("to", "Device", "pa", kind="terminal", center=[4, 1, 0], label="u_a", size=1.0, font_size=24),
    o("tv", "Device", "pa", kind="terminal", center=[4, 3, 0], label="+U_B", size=1.0, font_size=24),
]}

# 5. Small-signal equivalent circuit of the bipolar transistor (r_be, g_m u_be, r_ce)
T["Kleinsignal-Ersatzschaltbild"] = {"objects": [
    bare(),
    o("rbe", "Component", "pa", kind="resistor", start=[-3, 1.2, 0], end=[-3, -1.6, 0], label="r_{BE}",
      voltage="u_{BE}", size=0.9, font_size=24),
    o("gm", "Component", "pa", kind="vccs", start=[0.5, 1.2, 0], end=[0.5, -1.6, 0], label="g_m u_{BE}", size=1.0,
      font_size=24),
    o("rce", "Component", "pa", kind="resistor", start=[2.8, 1.2, 0], end=[2.8, -1.6, 0], label="r_{CE}", size=0.9,
      font_size=24),
    o("w1", "Wire", "pa", points="-5,1.2;-3,1.2"),
    o("w2", "Wire", "pa", points="0.5,1.2;5,1.2", dots=""),
    o("w2b", "Wire", "pa", points="2.8,1.2;2.8,1.2", dots="0"),
    o("w3", "Wire", "pa", points="-5,-1.6;5,-1.6", dots=""),
    o("d1", "Node", "pa", center=[-3, -1.6, 0], label="", dot=True),
    o("d2", "Node", "pa", center=[0.5, -1.6, 0], label="", dot=True),
    o("d3", "Node", "pa", center=[2.8, -1.6, 0], label="", dot=True),
    o("tb", "Device", "pa", kind="terminal", center=[-5, 1.2, 0], label="B", font_size=24),
    o("te", "Device", "pa", kind="terminal", center=[-5, -1.6, 0], label="E", font_size=24),
    o("tc", "Device", "pa", kind="terminal", center=[5, 1.2, 0], label="C", font_size=24),
    o("te2", "Device", "pa", kind="terminal", center=[5, -1.6, 0], label="E", font_size=24),
    o("uce", "LabeledArrow", "pa", start=[5.5, 1.0, 0], end=[5.5, -1.4, 0], label="u_{CE}", head_size=0.25,
      font_size=24, color=BLACK, stroke_width=2),
    o("ib", "LabeledArrow", "pa", start=[-4.6, 1.6, 0], end=[-3.6, 1.6, 0], label="i_B", head_size=0.22,
      font_size=22, color=BLACK, stroke_width=2),
]}

# 6. NMOS cross-section (technology section) with channel electrons and labelled terminals
T["Querschnitt NMOS"] = {"objects": [
    bare(),
    o("sub", "Shape", "pa", points="-5,-3;5,-3;5,0;-5,0", material="p", label="", color="#666666", stroke_width=1.5),
    o("ns", "Shape", "pa", points="-4,-0.9;-1.6,-0.9;-1.6,0;-4,0", material="n+", label="n^+", font_size=24,
      color="#666666", stroke_width=1.5),
    o("nd", "Shape", "pa", points="1.6,-0.9;4,-0.9;4,0;1.6,0", material="n+", label="n^+", font_size=24,
      color="#666666", stroke_width=1.5),
    o("ox", "Shape", "pa", points="-1.8,0;1.8,0;1.8,0.18;-1.8,0.18", material="oxide", label="", color="#666666",
      stroke_width=1.0),
    o("gp", "Shape", "pa", points="-1.8,0.18;1.8,0.18;1.8,0.9;-1.8,0.9", material="poly", label="Poly-Si",
      font_size=22, color="#666666", stroke_width=1.5),
    o("ms", "Shape", "pa", points="-3.4,0;-2.2,0;-2.2,0.6;-3.4,0.6", material="metal", label="", color="#666666",
      stroke_width=1.5),
    o("md", "Shape", "pa", points="2.2,0;3.4,0;3.4,0.6;2.2,0.6", material="metal", label="", color="#666666",
      stroke_width=1.5),
    o("ch", "PointCloud", "pa", n=40, x_min=-1.55, x_max=1.55, y_min=-0.16, y_max=-0.04, seed=7, radius=0.04,
      color=BLUE, stroke_width=1),
    o("ls", "Text", "pa", text="S", position=[-2.8, 1.0, 0], font_size=28, color=BLACK),
    o("lg", "Text", "pa", text="G", position=[0, 1.3, 0], font_size=28, color=BLACK),
    o("ld", "Text", "pa", text="D", position=[2.8, 1.0, 0], font_size=28, color=BLACK),
    o("lb", "Text", "pa", text="p-Substrat (Bulk)", position=[0, -2.3, 0], font_size=24, color="#444444"),
    o("lk", "Text", "pa", text="Kanal", position=[0, -0.55, 0], font_size=20, color=BLUE),
    o("lL", "LabeledArrow", "pa", start=[-1.6, -1.35, 0], end=[1.6, -1.35, 0], label="L", double=True,
      head_size=0.22, font_size=24, color=BLACK, stroke_width=2),
]}

# 7. Chain of effect (block diagram) with a closed negative-feedback loop
T["Wirkungskette Gegenkopplung"] = {"objects": [
    bare(),
    o("b0", "TextBox", "pa", text="Temperatur\\\\steigt", center=[-5, 1.6, 0], shape="round", font_size=24,
      fill_color="#fff1d6"),
    o("b1", "TextBox", "pa", text="I_C steigt", center=[-1, 1.6, 0], font_size=24, fill_color="#e8f1fb"),
    o("b2", "TextBox", "pa", text="U_{RE} = R_E I_C\\\\steigt", center=[3.6, 1.6, 0], font_size=24,
      fill_color="#e8f1fb"),
    o("b3", "TextBox", "pa", text="U_{BE} sinkt", center=[3.6, -1.6, 0], font_size=24, fill_color="#e8f1fb"),
    o("b4", "TextBox", "pa", text="I_C sinkt", center=[-1, -1.6, 0], font_size=24, fill_color="#e8f1fb"),
    o("a0", "LabeledArrow", "pa", start=[-3.75, 1.6, 0], end=[-2.05, 1.6, 0], label="", head_size=0.25,
      color=BLACK, stroke_width=2.5),
    o("a1", "LabeledArrow", "pa", start=[0.05, 1.6, 0], end=[1.85, 1.6, 0], label="", head_size=0.25,
      color=BLACK, stroke_width=2.5),
    o("a2", "LabeledArrow", "pa", start=[3.6, 0.9, 0], end=[3.6, -1.15, 0], label="", head_size=0.25,
      color=BLACK, stroke_width=2.5),
    o("a3", "LabeledArrow", "pa", start=[2.35, -1.6, 0], end=[0.05, -1.6, 0], label="", head_size=0.25,
      color=BLACK, stroke_width=2.5),
    o("a4", "LabeledArrow", "pa", start=[-1, -1.15, 0], end=[-1, 1.15, 0], label="Gegenkopplung", head_size=0.25,
      font_size=22, color=RED, stroke_width=2.5, dash="7,5"),
    o("lp", "LoopArrow", "pa", center=[1.3, 0, 0], radius=0.7, start_angle=200, end_angle=500, label="−",
      font_size=34, color=RED, stroke_width=2.5),
]}


# ---------------------------------------------------------------------------------------------
# Output: insert into web/editor.js (TEMPLATES + TEMPLATE_GROUPS, between marker comments, idempotent);
# with --json <dir> also write each template as an editor scene (for tools/editor_shot.py).
GROUP = "Elektrotechnik · Vorlagen"
ROOT = Path(__file__).resolve().parent.parent
JS = ROOT / "web" / "editor.js"


def _block(s, b0, b1, body, anchor, after_anchor):
    if b0 in s:
        a = s.index(b0)
        b = s.index(b1) + len(b1)
        return s[:a] + b0 + body + b1 + s[b:]
    assert s.count(anchor) == 1, "Anker nicht eindeutig: " + anchor[:40]
    i = s.index(anchor) + (len(anchor) if after_anchor else 1)
    return s[:i] + b0 + body + b1 + s[i:]


snippet = "".join("  " + json.dumps(name, ensure_ascii=False) + ": " + json.dumps(tpl, ensure_ascii=False) + ",\n"
                  for name, tpl in T.items())
group = "  " + json.dumps(GROUP, ensure_ascii=False) + ": " + json.dumps(list(T), ensure_ascii=False) + ",\n"
src = JS.read_text(encoding="utf-8")
src = _block(src, "  // >>> ET-Vorlagen (generiert)\n", "  // <<< ET-Vorlagen\n", snippet,
             "\n};\n\n// Shown once when the editor opens", False)
src = _block(src, "  // >>> ET-Vorlagen-Gruppe\n", "  // <<< ET-Vorlagen-Gruppe\n", group,
             '  "Mathematik · 3D": ["3D solids"],\n', True)
JS.write_text(src, encoding="utf-8")
print("editor.js: %d Vorlagen eingefügt" % len(T))

if "--json" in sys.argv:
    out = Path(sys.argv[sys.argv.index("--json") + 1])
    out.mkdir(parents=True, exist_ok=True)
    for n, (name, tpl) in enumerate(T.items(), 1):
        objs = []
        for d in tpl["objects"]:
            m = {"id": d["key"], "type": d["type"], "props": d["props"]}
            if "on" in d:
                m["on"] = d["on"]
            objs.append(m)
        model = {"objects": objs, "animations": [], "computations": [],
                 "background": {"color": "#ffffff", "transparent": False, "shadows": True, "axes_on_top": False},
                 "camera": {"mode": "2d", "theta": 0.6, "phi": 1.0, "zoom": 1.0}}
        (out / ("vorlage_%d.json" % n)).write_text(json.dumps({"v": 1, "model": model}, ensure_ascii=False), encoding="utf-8")
    print("Szenen:", out)

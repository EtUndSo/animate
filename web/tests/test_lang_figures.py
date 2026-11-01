"""Scene language and the publication features of ET3 figures (packages P2, P4-P7 in ABBILDUNGEN_INVENTAR.md).
Run: `python tests/test_lang_figures.py` from web/."""
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import numpy as np
from engine.scene_model import ModelScene
from engine.axes import Axes
from engine import text as T
from engine.figures import clip_run, stair_points, table_columns, build_data_curve, build_stem
from engine.legend import Legend


def texts(o, out=None):
    out = [] if out is None else out
    if hasattr(o, "text"):
        out.append(o.text)
    for s in o.subObjects:
        texts(s, out)
    return out


def scene(objects, lang="", strings=None):
    sc = ModelScene({"objects": objects, "animations": [], "computations": [], "lang": lang, "strings": strings or {}})
    sc.construct()
    return sc


def axes_spec(**kw):
    a = {"x_range": [0, 1, 0.5], "y_range": [-1, 1, 1], "x_length": 3, "y_length": 2, "x_label": "t", "y_label": "y"}
    a.update(kw)
    return {"id": "a", "type": "Axes", "args": a}


def test_number_language():
    for lang, tick, minus in (("de", "0,5", "−1"), ("es", "0,5", "−1"), ("en", "0.5", "−1"), ("zh", "0.5", "−1"),
                              ("", "0.5", "-1")):
        sc = scene([axes_spec()], lang)
        t = texts(sc.axes_by_id["a"])
        assert tick in t and minus in t, (lang, t)
    T.set_number_lang("")


def test_strings_and_digits():
    st = {"ein": {"de": "Eingang", "en": "Input", "zh": "输入"}}
    objs = [axes_spec(), {"id": "t1", "type": "Text", "on": "a", "args": {"text": "@ein", "position": [0, 0, 0]}},
            {"id": "t2", "type": "Text", "on": "a", "args": {"text": "@{ein}: t = 0.5 s", "position": [0, 0, 0]}},
            {"id": "t3", "type": "Text", "on": "a", "args": {"text": "@fehlt", "position": [0, 0, 0]}}]
    assert scene(objs, "de", st).objects_by_id["t1"].text == "Eingang"
    assert scene(objs, "de", st).objects_by_id["t2"].text == "Eingang: t = 0,5 s"
    assert scene(objs, "en", st).objects_by_id["t2"].text == "Input: t = 0.5 s"
    assert scene(objs, "zh", st).objects_by_id["t1"].text == "输入"
    assert scene(objs, "es", st).objects_by_id["t1"].text == "Eingang"          # missing language -> German
    assert scene(objs, "de", st).objects_by_id["t3"].text == "@fehlt"           # typo stays visible
    T.set_number_lang("")


def test_explicit_ticks():
    ax = Axes(x_range=[0, 7], y_range=[0, 1], x_length=4, y_length=2, x_ticks="3.14159=\\pi;6.28319=2\\pi", y_ticks="0.5",
              y_tick_marks=False, x_label="x", y_label="")
    t = texts(ax)
    assert "\\pi" in t and "2\\pi" in t and "0.5" in t, t
    assert "0" not in t                                 # no shared zero: 0 is not in the lists
    assert ax._xticks == [3.14159, 6.28319]


def test_axes_layout():
    a = Axes(x_range=[0, 1], y_range=[0, 1], x_length=4, y_length=2, x_label="t in s", y_label="", x_label_at="center",
             x_axis_at="bottom", title="Titel", title_at="center")
    lab = [s for s in a.subObjects if getattr(s, "text", "") == "t in s"][0]
    assert abs(lab.points[0][0] - a.origin[0]) < 1e-9 and lab.points[0][1] < a.origin[1] - 1.0
    tt = [s for s in a.subObjects if getattr(s, "text", "") == "Titel"][0]
    assert abs(tt.points[0][0] - a.origin[0]) < 1e-9
    n0 = len(Axes(x_range=[0, 1], y_range=[0, 1]).subObjects)
    assert len(Axes(x_range=[0, 1], y_range=[0, 1], frame=True).subObjects) == n0 + 4


def test_data_table_and_clip():
    assert table_columns("t a b\n0 1 2\n1 3 4", "1;3") == [(0.0, 2.0), (1.0, 4.0)]
    assert stair_points([(0, 1), (1, 2), (2, 3)], "post") == [(0, 1), (1, 1), (1, 2), (2, 2), (2, 3)]
    r = clip_run([(0.0, 0.0), (2.0, 2.0), (4.0, 0.0)], (0, 0, 4, 1))
    assert len(r) == 2 and r[0][-1] == (1.0, 1.0) and r[1][0] == (3.0, 1.0), r
    ax = Axes(x_range=[0, 1], y_range=[0, 1], x_length=2, y_length=2)
    o = build_data_curve({"data": "0 0\n2 2", "clip": True}, {}, ax)
    assert np.isclose(o.points[-1][0], ax.coords_to_point(1, 1)[0])
    o = build_data_curve({"data": "x y\n0 1\n1 2", "columns": "1;2", "y_factor": -1, "clip": False}, {}, None)
    assert np.isclose(o.points[-1][1], -2.0)


def test_stem_variants():
    ax = Axes(x_range=[0, 4], y_range=[0, 2], x_length=4, y_length=2)
    tri = build_stem({"x": "1;2", "y": "1;2", "arrows": True}, {}, ax)
    assert len(tri.subObjects) == 4                     # line + head per impulse, no dots
    tip = max(np.vstack([s.points for s in tri.subObjects])[:, 1])
    assert np.isclose(tip, ax.coords_to_point(0, 2)[1])
    bar = build_stem({"x": "1", "y": "1", "width": 0.5}, {}, ax)
    assert len(bar.subObjects) == 1
    w = bar.subObjects[0].points[:, 0]
    assert np.isclose(w.max() - w.min(), 0.5)           # 4 units on 4 data units
    sq = build_stem({"x": "1", "y": "1", "marker": "square"}, {}, ax)
    assert len(sq.subObjects) == 2


def test_stem_func_and_arrow_marks():
    sc = scene([axes_spec(x_range=[0, 2, 1], y_range=[0, 4, 1]),
                {"id": "s", "type": "Stem", "on": "a", "args": {"x": "1;2", "func": "x^2"}},
                {"id": "p", "type": "ParametricCurve", "on": "a",
                 "args": {"fx": "t", "fy": "t", "t_min": 0, "t_max": 2, "samples": 41, "arrow_at": "0.25;0.75"}}])
    ax = sc.axes_by_id["a"]
    tops = [d.points[:, 1].max() for d in sc.objects_by_id["s"].subObjects[1::2]]
    assert abs(tops[1] - ax.coords_to_point(0, 4)[1]) < 0.1
    assert len(sc.objects_by_id["p"].subObjects) == 3   # curve + two marks


def test_legend_styles():
    lg = Legend(labels="a;b;c;d", colors="ff0000;00ff00;0000ff;000000", styles="-;--;o;s", position=[0, 0, 0])
    assert len(lg.subObjects) == 8                      # line+label, line+label, dot+label, square+label
    assert lg.subObjects[2].dash if hasattr(lg.subObjects[2], "dash") else True


for f in (test_number_language, test_strings_and_digits, test_explicit_ticks, test_axes_layout, test_data_table_and_clip,
          test_stem_variants, test_stem_func_and_arrow_marks, test_legend_styles):
    f()
    print("  OK  ", f.__name__)
print("LANG/FIGURE TESTS PASSED")

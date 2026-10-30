"""Stapel-Export: Editor-Szenen als Artikelbilder (SVG), ohne Browser.

Aufruf (vom Repo-Root):
    python tools/export_szenen.py                     alle Szenen unter web/szenen/
    python tools/export_szenen.py et3/k1-bode demo    nur diese (Name = Pfad unter web/szenen/ ohne .json)
Optionen:
    --out DIR     Zielordner, Standard web/abbildungen (die Artikelseiten laden /abbildungen/<sprache>/<szene>.svg)
    --lang de     Sprache der Beschriftung; heute gibt es nur de. Paket P2 (mehrsprachige Texte, Dezimalkomma je
                  Sprache) ergänzt weitere Werte; die Szene bekommt die Sprache schon jetzt als model["lang"].
    --check       nur bauen und prüfen, nichts schreiben
Ausgabe: <out>/<lang>/<szene>.svg, je Szene eine Zeile mit Größe und Schriftgröße in der Artikelspalte.

Das Bild entsteht genau wie der SVG-Export im Editor (engine/export.py: Zuschnitt, Maßstab, Hintergrund):
- Die Szene wird wie beim Laden im Editor ergänzt: fehlende Props aus dem Katalog von web/editor.js (über node),
  alte Bauteile mit start/end auf Mitte/Drehung/Länge umgerechnet (editor.js ensureDefaults/migrateModel).
- Danach wird sie wie editor.js toPythonModel in das Modell der Engine übersetzt.
Grenzen: MathTex-Formeln und Σ/∏-Operationen im Zahlenmodus setzt nur der Browser (MathJax/KaTeX); sie fehlen
im Bild, das Skript meldet sie. Ohne node werden fehlende Props nicht ergänzt (Meldung).
"""
import argparse
import json
import math
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WEB = ROOT / "web"
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(WEB))
sys.stdout.reconfigure(encoding="utf-8")

from build_wissen import SZENEN, ABB_DIR, SZENE_NAME_RE  # noqa: E402  (eine Quelle für Pfade und Namensregel)
from engine import export as _export  # noqa: E402
from engine.scene_model import ModelScene  # noqa: E402

LANGS = ("de",)                                   # P2 ergänzt "en", "es", "zh"

_NODE_JS = r"""
const fs = require("fs");
const src = fs.readFileSync(process.argv[1], "utf8");
function slice(from, to){ const a = src.indexOf(from), b = src.indexOf(to, a); if(a < 0 || b < 0) throw new Error("not found: " + from); return src.slice(a, b); }
const CATALOG = new Function(slice("const CATALOG = {", "\nconst TEMPLATES") + "\nreturn CATALOG;")();
const COMPUTATIONS = new Function(slice("const SHAPE_TYPES", "\nconst COMP_DEFS") + "\nreturn COMPUTATIONS;")();
process.stdout.write(JSON.stringify({ CATALOG, COMPUTATIONS }));
"""


# Operation kinds of editor.js COMPUTATIONS, used only when node is missing (otherwise read from editor.js).
_KINDS_FALLBACK = {"Summation": "summation", "BigProduct": "product", "Addition": "numbers",
                   "Subtraction": "numbers", "Multiplication": "numbers", "Division": "numbers"}


def load_editor_tables():
    """(OBJ_DEFAULTS, kind per operation type) exactly as editor.js builds them; without node (None, fallback)."""
    node = shutil.which("node")
    if not node:
        return None, dict(_KINDS_FALLBACK)
    r = subprocess.run([node, "-e", _NODE_JS, str(WEB / "editor.js")], capture_output=True, text=True, encoding="utf-8")
    if r.returncode != 0:
        raise RuntimeError("editor.js-Katalog nicht lesbar: " + r.stderr.strip()[-400:])
    t = json.loads(r.stdout)
    defaults = {}
    for grp in t["CATALOG"].values():                       # editor.js OBJ_DEFAULTS: the first entry of a type wins
        for name, d in grp.items():
            typ = d.get("_type", name)
            if typ not in defaults:
                defaults[typ] = {k: v for k, v in d.items() if k != "_type"}
    kinds = {}
    for grp in t["COMPUTATIONS"].values():
        for d in grp.values():
            kinds[d["type"]] = d.get("kind")
    return defaults, kinds


def ensure_defaults(o, defaults):
    """editor.js ensureDefaults: migrate start/end components, backfill missing catalogue props."""
    p = o.get("props")
    if o.get("type") == "Component" and isinstance(p, dict) and isinstance(p.get("start"), list) \
            and isinstance(p.get("end"), list) and not isinstance(p.get("center"), list):
        x0, y0 = p["start"][0], p["start"][1]
        x1, y1 = p["end"][0], p["end"][1]
        rot = round(math.atan2(y1 - y0, x1 - x0) * 180 / math.pi * 100) / 100
        if rot < 0:
            rot += 360
        p["center"] = [(x0 + x1) / 2, (y0 + y1) / 2, 0]
        p["length"] = round(math.hypot(x1 - x0, y1 - y0) * 1e6) / 1e6
        p["rotation"] = rot
        del p["start"], p["end"]
    if o.get("type") == "Surface":
        o["type"] = "FunctionGraph"
    d = (defaults or {}).get(o.get("type"))
    if d and isinstance(p, dict):
        for k, v in d.items():
            if k not in p:
                p[k] = json.loads(json.dumps(v))
    if o.get("type") == "Axes" and isinstance(p, dict):
        p.pop("show_grid", None)
    if o.get("type") == "FunctionGraph" and isinstance(p, dict):
        p.pop("y_range", None)
    for c in o.get("children") or []:
        ensure_defaults(c, defaults)


def _hex_to_rgb(h):
    """editor.js hexToRgb: parseInt(h.slice(1), 16) -> [r, g, b] in 0..1."""
    m = re.match(r"[0-9a-fA-F]+", h[1:])
    n = int(m.group(0), 16) if m else 0
    return [((n >> 16) & 255) / 255, ((n >> 8) & 255) / 255, (n & 255) / 255]


def _to_args(props):
    return {k: (_hex_to_rgb(v) if isinstance(v, str) and v.startswith("#") else v) for k, v in (props or {}).items()}


def _obj_spec(o):
    spec = {"id": o.get("id"), "type": o.get("type"), "args": _to_args(o.get("props"))}
    if o.get("visible") is False:
        spec["visible"] = False
    for k in ("result", "a", "b", "on"):
        if o.get(k):
            spec[k] = o[k]
    if o.get("children"):
        spec["children"] = [_obj_spec(c) for c in o["children"]]
    return spec


def python_model(data, defaults, kinds, lang, notes):
    """The editor's saved scene ({v, counters, model} or a bare model) -> the engine model (editor.js applyScene +
    migrateModel + toPythonModel). `notes` collects what a browser-free export cannot draw."""
    m = (data or {}).get("model", data) or {}
    objects = m.get("objects") or []
    for o in objects:
        ensure_defaults(o, defaults)
    bgm = {"color": "#ffffff", "transparent": False, "shadows": True, "axes_on_top": False}
    bgm.update(m.get("background") or {})
    play_mode = m.get("playMode") or "sequential"
    anims = []
    for i, a in enumerate(x for x in (m.get("animations") or []) if x.get("visible") is not False):
        t = a.get("type")
        args = ({"vector": a.get("vector")} if t == "Shift" else {"point": a.get("point")} if t == "MoveTo"
                else {"angle": (a.get("angle") or 0) * math.pi / 180} if t == "Rotate"
                else {"factor": a.get("factor")} if t == "Scale" else {})
        spec = {"type": t, "target": a.get("target"), "step": 0 if play_mode == "parallel" else i,
                "args": {k: v for k, v in args.items() if v is not None}}
        if a.get("run_time") is not None:
            spec["run_time"] = a["run_time"]
        anims.append(spec)
    comps = []
    for c in m.get("computations") or []:
        spec = {"id": c.get("id"), "type": c.get("type"), "props": _to_args(c.get("props"))}
        if c.get("visible") is False:
            spec["visible"] = False
        kind = (kinds or {}).get(c.get("type"))
        if kind == "numbers":
            spec["numbers"] = c.get("numbers")
        elif kind in ("summation", "product"):
            if (c.get("props") or {}).get("sum_mode", "number") != "function" and c.get("visible") is not False:
                notes.append(f"Operation {c.get('type')} ({c.get('id')}) im Zahlenmodus setzt nur der Browser — fehlt im Bild")
        else:
            spec["inputs"] = c.get("inputs")
            if c.get("children"):
                spec["children"] = [_obj_spec(ch) for ch in c["children"]]
        comps.append(spec)

    def scan(o):
        if o.get("type") == "MathTex" and o.get("visible") is not False:
            notes.append(f"MathTex {o.get('id')} braucht MathJax im Browser — fehlt im Bild")
        for ch in o.get("children") or []:
            scan(ch)
    for o in objects:
        scan(o)
    return {"objects": [_obj_spec(o) for o in objects], "animations": anims, "computations": comps,
            "background": None if bgm.get("transparent") else _hex_to_rgb(bgm.get("color") or "#ffffff"),
            "shadows": bool(bgm.get("shadows")), "axes_on_top": bgm.get("axes_on_top") is True,
            "angle_unit": m.get("angleUnit") or "rad", "domain": m.get("domain") or "real",
            "camera": m.get("camera") or {"mode": "2d", "theta": 0.6, "phi": 1.0},
            "gl": False, "export": m.get("export"), "lang": lang}


def export_scene(name, out_dir, lang, defaults, kinds, write=True):
    """Build one scene and write <out_dir>/<lang>/<name>.svg. Returns (info, notes)."""
    data = json.loads((SZENEN / (name + ".json")).read_text(encoding="utf-8"))
    notes = []
    model = python_model(data, defaults, kinds, lang, notes)
    sc = ModelScene(model)
    sc.construct()
    sc.show_static()
    svg, info = _export.render(sc.objectList, sc.camera, background=model["background"],
                               axes_on_top=model["axes_on_top"], raw_settings=model["export"])
    if write:
        dest = out_dir / lang / (name + ".svg")
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(svg, encoding="utf-8", newline="\n")
    return info, notes


def all_names():
    return sorted(p.relative_to(SZENEN).with_suffix("").as_posix() for p in SZENEN.rglob("*.json"))


def _de(v, nd=1):
    return f"{v:.{nd}f}".replace(".", ",")


def main(argv=None):
    ap = argparse.ArgumentParser(description="Editor-Szenen als Artikelbilder (SVG) exportieren, ohne Browser.")
    ap.add_argument("szenen", nargs="*", help="Szenennamen (Pfad unter web/szenen/ ohne .json); leer = alle")
    ap.add_argument("--out", default=str(ABB_DIR), help="Zielordner (Standard: web/abbildungen)")
    ap.add_argument("--lang", default="de", choices=LANGS, help="Sprache der Beschriftung (heute nur de)")
    ap.add_argument("--check", action="store_true", help="nur prüfen, nichts schreiben")
    a = ap.parse_args(argv)
    names = a.szenen or all_names()
    out_dir = Path(a.out)
    defaults, kinds = load_editor_tables()
    if defaults is None:
        print("⚠ node nicht gefunden: fehlende Props werden nicht aus dem Editor-Katalog ergänzt")
    fails = 0
    for name in names:
        name = name[:-5] if name.endswith(".json") else name
        if not SZENE_NAME_RE.fullmatch(name):
            print(f"✗ {name}: ungültiger Name (erlaubt: a-z A-Z 0-9 _ - und / als Ordnertrenner)"); fails += 1; continue
        if not (SZENEN / (name + ".json")).is_file():
            print(f"✗ {name}: web/szenen/{name}.json fehlt"); fails += 1; continue
        try:
            info, notes = export_scene(name, out_dir, a.lang, defaults, kinds, write=not a.check)
        except Exception as e:  # noqa: BLE001  (eine kaputte Szene soll die anderen nicht aufhalten)
            print(f"✗ {name}: {type(e).__name__}: {e}"); fails += 1; continue
        size = f"{info['width']}×{info['height']} px"
        txt = f"Text {info['ref_text']} px → {_de(info['text_px'])} px"
        if info["fits"]:
            print(f"✓ {name}: {size}, {txt} ({info['mode']})")
        else:
            print(f"⚠ {name}: {size} ist breiter als die Spalte ({info['column']} px), {txt}; "
                  f"Zeichnung schmaler machen ({info['mode']})")
        for n in notes:
            print(f"    ⚠ {n}")
    where = "geprüft" if a.check else f"→ {out_dir / a.lang}"
    print(f"{len(names) - fails} von {len(names)} Szenen {where}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())

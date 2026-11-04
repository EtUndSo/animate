"""Stapel-Export: Editor-Szenen als Artikelbilder (SVG).

Aufruf (vom Repo-Root):
    python tools/export_szenen.py                     alle Szenen unter web/szenen/
    python tools/export_szenen.py et3/k1-bode demo    nur diese (Name = Pfad unter web/szenen/ ohne .json)
Optionen:
    --out DIR     Zielordner, Standard web/abbildungen (die Artikelseiten laden /abbildungen/<sprache>/<szene>.svg)
    --lang de     nur diese Sprache der Beschriftung; Standard: alle vier (de, en, es, zh). Texte kommen aus der
                  Tabelle `strings` der Szene (@schluessel im Label), das Zahlformat folgt der Sprache.
    --check       nur bauen und prüfen, nichts schreiben
Ausgabe: <out>/<lang>/<szene>.svg, je Szene eine Zeile mit Größe und Schriftgröße in der Artikelspalte.

Das Bild entsteht genau wie der SVG-Export im Editor (engine/export.py: Zuschnitt, Maßstab, Hintergrund):
- Die Szene wird wie beim Laden im Editor ergänzt: fehlende Props aus dem Katalog von web/editor.js (über node),
  alte Bauteile mit start/end auf Mitte/Drehung/Länge umgerechnet (editor.js ensureDefaults/migrateModel).
- Danach wird sie wie editor.js toPythonModel in das Modell der Engine übersetzt.
Formeln (Σ, ∏ und Skalarprodukt im Zahlenmodus, MathTex): Die Einzelteile in LaTeX baut derselbe Code wie im
Editor (Block „series-spec“ in web/editor.js, über node). LaTeX setzt MathJax wie im Editor: in einem
Headless-Chromium (Playwright) mit dem Block „tex-glyphs“ aus web/editor.js und der MathJax-Version aus
web/editor.html. Die Glyphen landen in tools/tex_glyphen_cache.json; danach braucht dieselbe Formel weder Browser
noch Netz. Ohne Playwright oder ohne Netz fehlt die Formel im Bild, das Skript meldet sie.
Ohne node werden fehlende Props nicht ergänzt (Meldung).
"""
import argparse
import hashlib
import json
import math
import os
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

LANGS = ("de", "en", "es", "zh")
TEX_CACHE = ROOT / "tools" / "tex_glyphen_cache.json"

_NODE_JS = r"""
const fs = require("fs");
const src = fs.readFileSync(process.argv[1], "utf8");
function slice(from, to){ const a = src.indexOf(from), b = src.indexOf(to, a); if(a < 0 || b < 0) throw new Error("not found: " + from); return src.slice(a, b); }
const CATALOG = new Function(slice("const CATALOG = {", "\nconst TEMPLATES") + "\nreturn CATALOG;")();
const COMPUTATIONS = new Function(slice("const SHAPE_TYPES", "\nconst COMP_DEFS") + "\nreturn COMPUTATIONS;")();
process.stdout.write(JSON.stringify({ CATALOG, COMPUTATIONS }));
"""

# The LaTeX pieces of Σ / ∏ / scalar product, built by the editor's own block "series-spec" (pure JS, no DOM).
# stdin: [{c: <editor operation>, lang}], stdout: [spec | null].
_SPEC_JS = r"""
const fs = require("fs");
const src = fs.readFileSync(process.argv[1], "utf8");
const a = src.indexOf("// >>> series-spec"), b = src.indexOf("// <<< series-spec");
if(a < 0 || b < 0) throw new Error("block series-spec not found in editor.js");
const api = new Function(src.slice(a, b) + "\nreturn { seriesSpec };")();
const req = JSON.parse(fs.readFileSync(0, "utf8"));
process.stdout.write(JSON.stringify(req.map(r => api.seriesSpec(r.c, r.lang))));
"""

# Operation kinds of editor.js COMPUTATIONS, used only when node is missing (otherwise read from editor.js).
_KINDS_FALLBACK = {"Summation": "summation", "BigProduct": "product", "DotProduct": "dotproduct", "Addition": "numbers",
                   "Subtraction": "numbers", "Multiplication": "numbers", "Division": "numbers"}
SERIES_KINDS = ("summation", "product", "dotproduct")    # editor.js SERIES_KINDS: step-by-step Σ-type operations


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


def _visible_mathtex(specs, out):
    """Every MathTex spec that is drawn (hidden ones and their children are not)."""
    for s in specs:
        if s.get("type") == "MathTex" and s.get("visible") is not False:
            out.append(s)
        _visible_mathtex(s.get("children") or [], out)
    return out


# ---------------------------------------------------------------------------- formulas (LaTeX -> glyphs)
def _spec_latex(spec):
    """Every LaTeX piece of a series spec (editor.js buildChoreo `need`)."""
    need = [spec["head"]] + ([spec["vectors"]] if spec.get("vectors") else [])
    for col in spec["cols"]:
        if col["t"] == "term":
            need += [col[k] for k in ("abstract", "index", "subst", "value") if col.get(k) is not None]
        else:
            need.append(col["g"])
    return need


def choreo_from_spec(spec, g):
    """editor.js choreoFromSpec: the LaTeX spec -> the engine's choreography (glyph data per piece)."""
    out = {"head": g(spec["head"]), "var": spec.get("var"), "stages": spec.get("stages"), "cols": []}
    for col in spec["cols"]:
        if col["t"] != "term":
            out["cols"].append({"t": col["t"], "g": g(col["g"])})
            continue
        o = {"t": "term", "abstract": g(col["abstract"]), "subst": g(col["subst"]),
             "value": g(col["value"]) if col.get("value") is not None else None}
        if col.get("index") is not None:
            o["index"] = g(col["index"])
        if col.get("row") is not None:
            o["row"] = col["row"]
        out["cols"].append(o)
    if spec.get("vectors"):
        out["vectors"] = g(spec["vectors"])
        out["rows"] = spec.get("rows")
    return out


class TexGlyphen:
    """LaTeX -> MathJax glyph data, as the editor makes it (texToGlyphs), with a file cache. The browser (Playwright,
    headless Chromium) starts only for a formula that is not in the cache yet and stays open until close()."""

    def __init__(self, cache_path=TEX_CACHE):
        self.path = Path(cache_path)
        js = (WEB / "editor.js").read_text(encoding="utf-8")
        a, b = js.find("// >>> tex-glyphs"), js.find("// <<< tex-glyphs")
        if a < 0 or b < 0:
            raise RuntimeError("Block tex-glyphs fehlt in web/editor.js")
        self.code = js[a:b]
        html = (WEB / "editor.html").read_text(encoding="utf-8")
        cfg = re.search(r"<script>(window\.MathJax=.*?)</script>", html, re.S)
        src = re.search(r'<script[^>]*\bsrc="([^"]*tex-svg[^"]*\.js)"', html)
        if not cfg or not src:
            raise RuntimeError("MathJax-Einbindung in web/editor.html nicht gefunden")
        self.page_html = (f'<!doctype html><meta charset="utf-8"><body><script>{cfg.group(1)}</script>'
                          f'<script src="{src.group(1)}"></script></body>')
        self.version = hashlib.sha1((self.page_html + "\n" + self.code).encode("utf-8")).hexdigest()[:16]
        self.cache, self.new = self._load(), {}
        self._pw = self._browser = self._page = None
        self.used = 0

    def _load(self):
        try:
            d = json.loads(self.path.read_text(encoding="utf-8"))
            return dict(d.get("glyphs") or {}) if d.get("version") == self.version else {}
        except (OSError, ValueError):
            return {}

    def _start(self):
        from playwright.sync_api import sync_playwright   # only needed for formulas that are not cached yet
        self._pw = sync_playwright().start()
        self._browser = self._pw.chromium.launch()
        self._page = self._browser.new_page()
        self._page.set_content(self.page_html, wait_until="load", timeout=60000)
        self._page.wait_for_function("window.MathJax && MathJax.startup && MathJax.startup.promise"
                                     " && typeof MathJax.tex2svg === 'function'", timeout=60000)
        self._page.add_script_tag(content=self.code)       # _glyphChar, _tex2glyphs, texToGlyphs as page globals

    def glyphs(self, latex_list):
        """{latex: glyph list} for every piece; MathJax runs once for all pieces that are not cached."""
        want = list(dict.fromkeys(str(x) for x in latex_list))
        miss = [x for x in want if x not in self.cache]
        if miss:
            if self._page is None:
                self._start()
            got = self._page.evaluate("async (list) => { await MathJax.startup.promise; const out = {};"
                                      " for (const t of list) out[t] = await texToGlyphs(t); return out; }", miss)
            for x in miss:
                self.cache[x] = self.new[x] = got.get(x) or []
        self.used += len(want)
        return {x: self.cache[x] for x in want}

    def series_specs(self, comps, lang):
        node = shutil.which("node")
        if not node:
            raise RuntimeError("node fehlt (baut die LaTeX-Teile wie der Editor)")
        r = subprocess.run([node, "-e", _SPEC_JS, str(WEB / "editor.js")], input=json.dumps([{"c": c, "lang": lang} for c in comps]),
                           capture_output=True, text=True, encoding="utf-8")
        if r.returncode != 0:
            raise RuntimeError("series-spec: " + r.stderr.strip()[-400:])
        return json.loads(r.stdout)

    def fill(self, series, texs, lang):
        """Put the glyphs in: series = [(engine spec, editor operation)] gets props.choreo (editor toPythonModel),
        texs = MathTex specs get args.glyphs instead of args.tex (editor injectTexGlyphs). Returns the operations
        that have nothing to draw (scalar product with lists of different length)."""
        specs = self.series_specs([c for _, c in series], lang) if series else []
        need = [x for sp in specs if sp for x in _spec_latex(sp)] + [str(s["args"].get("tex") or "") for s in texs]
        got = self.glyphs(need)
        g = lambda x: got.get(str(x)) or []
        empty = []
        for (spec, c), sp in zip(series, specs):
            if sp:
                spec["props"]["choreo"] = choreo_from_spec(sp, g)
            else:
                empty.append(c)
        for s in texs:
            s["args"]["glyphs"] = g(s["args"].pop("tex", "") or "")
        return empty

    def close(self):
        if self.new:                                      # merge with what another run may have written meanwhile
            merged = self._load()
            merged.update(self.cache)
            tmp = self.path.with_suffix(".tmp")
            tmp.write_text(json.dumps({"version": self.version, "glyphs": merged}, ensure_ascii=False, separators=(",", ":")),
                           encoding="utf-8", newline="\n")
            os.replace(tmp, self.path)
            self.new = {}
        for stop in ((self._browser.close if self._browser else None), (self._pw.stop if self._pw else None)):
            try:
                if stop:
                    stop()
            except Exception:  # noqa: BLE001  (closing must not hide the export result)
                pass
        self._pw = self._browser = self._page = None


def python_model(data, defaults, kinds, lang, notes, tex=None):
    """The editor's saved scene ({v, counters, model} or a bare model) -> the engine model (editor.js applyScene +
    migrateModel + toPythonModel). `notes` collects what cannot be drawn. tex (TexGlyphen) sets the formulas
    (Σ/∏/scalar product in number mode, MathTex); without it they are reported as missing."""
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
    comps, series = [], []
    for c in m.get("computations") or []:
        spec = {"id": c.get("id"), "type": c.get("type"), "props": _to_args(c.get("props"))}
        if c.get("visible") is False:
            spec["visible"] = False
        kind = (kinds or {}).get(c.get("type"))
        if kind == "numbers":
            spec["numbers"] = c.get("numbers")
        elif kind in SERIES_KINDS:
            number_mode = kind == "dotproduct" or (c.get("props") or {}).get("sum_mode", "number") != "function"
            if number_mode and c.get("visible") is not False:
                series.append((spec, c))
        else:
            spec["inputs"] = c.get("inputs")
            if c.get("children"):
                spec["children"] = [_obj_spec(ch) for ch in c["children"]]
        comps.append(spec)
    obj_specs = [_obj_spec(o) for o in objects]
    texs = _visible_mathtex(obj_specs, [])
    if tex is None:
        for _, c in series:
            notes.append(f"Operation {c.get('type')} ({c.get('id')}) im Zahlenmodus setzt nur der Browser — fehlt im Bild")
        for s in texs:
            notes.append(f"MathTex {s.get('id')} braucht MathJax im Browser — fehlt im Bild")
    elif series or texs:
        try:
            for c in tex.fill(series, texs, lang):
                notes.append(f"Operation {c.get('type')} ({c.get('id')}): u und v brauchen gleich viele Zahlen — nichts zu zeichnen")
        except Exception as e:  # noqa: BLE001  (kein Browser / kein Netz: das Bild entsteht ohne die Formeln)
            notes.append(f"Formeln nicht gesetzt ({type(e).__name__}: {str(e).splitlines()[0][:160]}) — "
                         f"{len(series)} Operation(en), {len(texs)} MathTex fehlen im Bild")
    return {"objects": obj_specs, "animations": anims, "computations": comps,
            "background": None if bgm.get("transparent") else _hex_to_rgb(bgm.get("color") or "#ffffff"),
            "shadows": bool(bgm.get("shadows")), "axes_on_top": bgm.get("axes_on_top") is True,
            "angle_unit": m.get("angleUnit") or "rad", "domain": m.get("domain") or "real",
            "camera": m.get("camera") or {"mode": "2d", "theta": 0.6, "phi": 1.0},
            "gl": False, "export": m.get("export"), "lang": lang, "strings": m.get("strings") or {}}


def export_scene(name, out_dir, lang, defaults, kinds, write=True, tex=None):
    """Build one scene and write <out_dir>/<lang>/<name>.svg. Returns (info, notes)."""
    data = json.loads((SZENEN / (name + ".json")).read_text(encoding="utf-8"))
    notes = []
    model = python_model(data, defaults, kinds, lang, notes, tex=tex)
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
    ap = argparse.ArgumentParser(description="Editor-Szenen als Artikelbilder (SVG) exportieren.")
    ap.add_argument("szenen", nargs="*", help="Szenennamen (Pfad unter web/szenen/ ohne .json); leer = alle")
    ap.add_argument("--out", default=str(ABB_DIR), help="Zielordner (Standard: web/abbildungen)")
    ap.add_argument("--lang", default="", choices=LANGS + ("",), help="nur diese Sprache (Standard: alle vier)")
    ap.add_argument("--check", action="store_true", help="nur prüfen, nichts schreiben")
    a = ap.parse_args(argv)
    names = a.szenen or all_names()
    out_dir = Path(a.out)
    defaults, kinds = load_editor_tables()
    if defaults is None:
        print("⚠ node nicht gefunden: fehlende Props werden nicht aus dem Editor-Katalog ergänzt")
    try:
        tex = TexGlyphen()
    except Exception as e:  # noqa: BLE001
        tex = None
        print(f"⚠ Formeln werden nicht gesetzt: {e}")
    fails = 0
    langs = (a.lang,) if a.lang else LANGS
    try:
        for name in names:
            name = name[:-5] if name.endswith(".json") else name
            if not SZENE_NAME_RE.fullmatch(name):
                print(f"✗ {name}: ungültiger Name (erlaubt: a-z A-Z 0-9 _ - und / als Ordnertrenner)"); fails += 1; continue
            if not (SZENEN / (name + ".json")).is_file():
                print(f"✗ {name}: web/szenen/{name}.json fehlt"); fails += 1; continue
            for lang in langs:
                try:
                    info, notes = export_scene(name, out_dir, lang, defaults, kinds, write=not a.check, tex=tex)
                except Exception as e:  # noqa: BLE001  (eine kaputte Szene soll die anderen nicht aufhalten)
                    print(f"✗ {name} [{lang}]: {type(e).__name__}: {e}"); fails += 1; continue
                size = f"{info['width']}×{info['height']} px"
                txt = f"Text {info['ref_text']} px → {_de(info['text_px'])} px"
                if info["fits"]:
                    print(f"✓ {name} [{lang}]: {size}, {txt} ({info['mode']})")
                else:
                    print(f"⚠ {name} [{lang}]: {size} ist breiter als die Spalte ({info['column']} px), {txt}; "
                          f"Zeichnung schmaler machen ({info['mode']})")
                for n in notes:
                    print(f"    ⚠ {n}")
    finally:
        if tex is not None:
            if tex.used:
                print(f"Formeln: {tex.used} LaTeX-Teile gesetzt, davon {len(tex.new)} neu mit MathJax → {TEX_CACHE.name}")
            tex.close()
    where = "geprüft" if a.check else f"→ {out_dir}"
    print(f"{len(names) * len(langs) - fails} von {len(names) * len(langs)} Bildern {where}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())

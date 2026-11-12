"""F1 „Bildschirme und Fenster“ (12.11.2026): Vertragstest je Baustein, Export = Editor.
Jeder Baustein (Terminal mit Zeitachse, Datei-Ansicht, top, Pager, Textblock mit ANSI, Schloss, Raster) wird mit
tools/szenen_lib.py als Szenendatei geschrieben und auf zwei Wegen in das Modell der Engine übersetzt:
  Export: tools/export_szenen.py python_model (wie der Stapel-Export für Website und PDF),
  Editor: die Funktionen aus web/editor.js selbst (ensureDefaults mit dem Katalog, toArgs, objToSpec, animSteps,
          animArgs), in node ausgeführt, wie toPythonModel sie beim Laden einer Szene aufruft.
Beide Modelle müssen gleich sein und zu jedem Zeitpunkt dasselbe SVG ergeben; der Canvas-Painter des Editors zeichnet
dieselben Zeichen in denselben Farben an dieselben Stellen wie der SVG-Painter. Dazu die Palette-Einträge der Gruppe
„Bildschirm & Fenster“ (bauen, zeichnen etwas, Zustände wie die Engine zählt).
Run from web/:  python tests/test_f1_bausteine.py   (braucht node)"""
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, "."); sys.path.insert(0, "py")
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools")); sys.path.insert(0, str(ROOT / "tools" / "szenen")); sys.path.insert(0, str(ROOT))
from engine.scene_model import ModelScene  # noqa: E402
from engine import export as ex  # noqa: E402
from engine import terminal as T  # noqa: E402
from engine.renderer import paint_scene  # noqa: E402
from canvas_painter import CanvasPainter  # noqa: E402
import export_szenen as es  # noqa: E402
from szenen_lib import Szene, ORANGE, BLAU, GRAU, farbig  # noqa: E402

ok = True


def check(name, cond, extra=""):
    global ok
    print(("  OK   " if cond else " FAIL  ") + name + (("  :: " + str(extra)[:300]) if extra != "" and not cond else ""))
    ok = ok and bool(cond)


EDITOR = ROOT / "web" / "editor.js"
NODE_JS = r"""
const fs = require("fs");
const src = fs.readFileSync(process.argv[1], "utf8");
function grab(a, b){ const i = src.indexOf(a), j = src.indexOf(b, i); if(i < 0 || j < 0) throw new Error("not found: " + a); return src.slice(i, j); }
const code = [grab("const CATALOG = {", "\nconst TEMPLATES"), grab("const OBJ_DEFAULTS = {};", "\nconst CIRCUIT_TYPES"),
              grab("function hexToRgb(h)", "\nfunction toPythonModel"), grab("const L5_TYPES", "\nconst ANIM_TYPES"),
              grab("function terminalSegments(text)", "\nfunction terminalParam")].join("\n");
const api = new Function(code + "\nreturn { CATALOG, OBJ_DEFAULTS, ensureDefaults, objToSpec, animSteps, animArgs, terminalSegments, terminalStepTime };")();
const req = JSON.parse(fs.readFileSync(0, "utf8"));
const out = {};
for(const [name, data] of Object.entries(req.scenes)){
  const m = data.model || data;
  for(const o of m.objects) api.ensureDefaults(o);
  const shown = (m.animations || []).filter(a => a.visible !== false);
  const steps = api.animSteps(shown, m.playMode || "sequential");
  out[name] = { objects: m.objects.map(api.objToSpec),
    animations: shown.map((a, i) => ({ type: a.type, target: a.target, run_time: a.run_time, step: steps[i], args: api.animArgs(a) })),
    draw_order: m.drawOrder === "creation" ? "creation" : "appearance" };
}
const presets = {};
for(const [label, d] of Object.entries(api.CATALOG["Bildschirm & Fenster"] || {})){
  const type = d._type || label, props = { ...d }; delete props._type;
  const o = { id: "p1", type, props }; api.ensureDefaults(o);
  presets[label] = { spec: api.objToSpec(o), segments: type === "Terminal" ? api.terminalSegments(props.text).length - 1 : null,
                     times: type === "Terminal" ? api.terminalSegments(props.text).slice(1).map(api.terminalStepTime) : null };
}
process.stdout.write(JSON.stringify({ models: out, presets }));
"""


def bausteine():
    """Szenendateien (Modelle) je Baustein, mit szenen_lib geschrieben."""
    out = {}
    s = Szene("t/terminal", reihenfolge="anlegen")
    t = s.terminal(pos=(-3.4, 1.8), spalten=30, zeilen=5)
    s.einblenden(t.id)
    t.befehl("ls --color", farbig("Dokumente", "blau", True) + "  notizen.txt")
    t.warten(0.9)
    t.setze(1, 0, "\\e[7mDOK\\e[0m")
    t.schliessen(0.8)
    out["Terminal"] = s.model()
    s = Szene("t/datei", reihenfolge="anlegen")
    d = s.datei("/etc/group", "root:x:0:\nsudo:x:27:student")
    s.einblenden(d.id)
    d.zeile_dazu("anna:x:1001:")
    s.einblenden(d.markieren(2, 0, 3, ORANGE))
    out["Datei-Ansicht"] = s.model()
    s = Szene("t/top", reihenfolge="anlegen")
    kopf = ["top - 10:00:00 up 1 min,  1 user,  load average: 0.10, 0.05, 0.01",
            "Tasks:  70 total,   1 running,  69 sleeping,   0 stopped,   0 zombie"]
    tab = ["    PID USER      %CPU COMMAND", "      1 root       0.0 systemd", "    112 root       0.0 cron"]
    tp = s.top(kopf, tab)
    s.einblenden(tp.id)
    tp.bild(tabelle=[tab[0], "    301 student   99.0 yes"] + tab[1:])
    out["top"] = s.model()
    s = Szene("t/pager", reihenfolge="anlegen")
    pg = s.pager([farbig("●", "gruen", True) + " cron.service - daemon", "   Loaded: loaded", "   Active: "
                  + farbig("active (running)", "gruen", True), "   CGroup: /system.slice/cron.service",
                  "           " + farbig("└─", "grau") + "112 /usr/sbin/cron -f -P"], sichtbar=3)
    s.einblenden(pg.id)
    pg.weiter(2)
    out["Pager"] = s.model()
    s = Szene("t/textblock", reihenfolge="anlegen")
    tb = s.text(None, "drwxr-xr-x 2 student " + farbig("Dokumente", "blau", True), (-3, 0), 20, schrift="tt", ansi=True)
    s.einblenden(tb)
    out["Textblock"] = s.model()
    s = Szene("t/schloss", reihenfolge="anlegen")
    l1, l2 = s.schloss((-1, 0)), s.schloss((1, 0), offen=True, farbe=ORANGE)
    s.einblenden(l1, l2)
    out["Schloss"] = s.model()
    s = Szene("t/raster", reihenfolge="anlegen")
    g = s.raster(["root:x:0:0:root:/root:/bin/bash", "student:x:1000:1000::/home/student:/bin/bash"], (0, 0.5),
                 ausrichtung="mitte", groesse=22)
    mk = [g.markieren(0, k, k, ORANGE) for k in g.trenner(0, ":")]
    kl = g.klammer(1, *g.felder(1, ":")[2][:2], "UID", seite="unten", farbe=BLAU)
    teil = g.teil(1, 8, 11)
    s.einblenden(*g.ids)
    s.einblenden(*mk)
    s.zeichnen(kl[0])
    s.einblenden(kl[1])
    s.verschieben(teil, 0, -1.0)
    g.faerben(0, [(0, 3, ORANGE)], rest=GRAU)
    out["Raster"] = s.model()
    return out


def editor_models(scenes):
    node = shutil.which("node")
    r = subprocess.run([node, "-e", NODE_JS, str(EDITOR)], input=json.dumps({"scenes": scenes}), capture_output=True,
                       text=True, encoding="utf-8")
    if r.returncode != 0:
        raise RuntimeError(r.stderr[-800:])
    return json.loads(r.stdout)


def engine_model(objects, animations, draw_order):
    return {"objects": objects, "animations": animations, "computations": [], "background": [1, 1, 1], "shadows": True,
            "axes_on_top": False, "draw_order": draw_order, "angle_unit": "rad", "domain": "real",
            "camera": {"mode": "2d", "theta": 0.6, "phi": 1.0}, "gl": False, "export": None, "lang": "de", "strings": {}}


def frames(model, n=6):
    sc = ModelScene(json.loads(json.dumps(model)))
    sc.animating = True
    sc.build_timeline()
    out = []
    for k in range(n + 1):
        sc.seek(sc.duration * k / n)
        svg, _ = ex.render(sc.objectList, sc.camera, background=(1, 1, 1), raw_settings={"mode": "canvas"})
        out.append(svg)
    return sc, out


_TAG = re.compile(r'<text x="([^"]+)" y="([^"]+)"[^>]*fill="(#[0-9a-f]{6})"[^>]*>(.*?)</text>', re.S)
_PART = re.compile(r'<tspan([^>]*)>(.*?)</tspan>|([^<]+)', re.S)


def svg_chars(svg):
    """{(x, y, Zeichen, Farbe, fett)} aller Zeichen in Schreibmaschinenschrift (x-Liste je Zeichen)."""
    out = set()
    for xs, y, fill, body in _TAG.findall(svg):
        xs = xs.split()
        if len(xs) < 2 and len(re.sub(r"<[^>]+>", "", body)) > 1:
            continue                                    # normale Schrift: keine Zellen
        i = 0
        for attrs, inner, plain in _PART.findall(body):
            txt = inner if attrs or inner else plain
            m = re.search(r'fill="(#[0-9a-f]{6})"', attrs or "")
            col, bold = (m.group(1) if m else fill), "bold" in (attrs or "")
            for ch in txt.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">"):
                if i < len(xs) and ch != " ":
                    out.add((round(float(xs[i]), 2), round(float(y), 2), ch, col, bold))
                i += 1
    return out


class Ctx:
    def __init__(self):
        self.calls, self.fillStyle, self.font = [], "", ""

    def __getattr__(self, n):
        if n.startswith("__"):
            raise AttributeError(n)
        return lambda *a: self.calls.append((n, a, self.fillStyle, self.font))


def canvas_chars(sc):
    ctx = Ctx()
    paint_scene(CanvasPainter(ctx, 1920, 1080), sc.objectList, sc.camera, background=(1, 1, 1))
    out = set()
    for n, a, fill, font in ctx.calls:
        if n == "fillText" and len(a[0]) == 1 and "Consolas" in font and a[0] != " ":
            r, g, b = (int(v) for v in re.findall(r"\d+", fill)[:3])
            out.add((round(a[1], 2), round(a[2], 2), a[0], "#%02x%02x%02x" % (r, g, b), font.startswith("bold")))
    return out


defaults, kinds = es.load_editor_tables()
scenes = bausteine()
ed = editor_models(scenes)
for name, data in scenes.items():
    pm = es.python_model(json.loads(json.dumps(data)), defaults, kinds, "de", [])
    em = engine_model(**ed["models"][name])
    same = pm["objects"] == em["objects"] and pm["animations"] == em["animations"]   # 1.0 == 1 (JSON aus node)
    check(f"{name}: Modell aus dem Editor-Weg = Modell aus dem Export-Weg (Objekte, Zeitachse)", same)
    sa, fa = frames(pm)
    sb, fb = frames(em)
    diff = next((("Bild %d" % i, [l for l in x.splitlines() if l not in y.splitlines()][:2])
                 for i, (x, y) in enumerate(zip(fa, fb)) if x != y), "")
    check(f"{name}: gleiche SVGs zu 7 Zeitpunkten (Dauer {sa.duration:.1f} s)", fa == fb and abs(sa.duration - sb.duration) < 1e-9,
          (diff, sa.duration, sb.duration))
    check(f"{name}: die Zeitachse ändert das Bild", len(set(fa)) > 1)
    sa.seek(sa.duration)
    a, b = svg_chars(fa[-1]), canvas_chars(sa)
    check(f"{name}: Canvas (Editor) zeichnet dieselben Zeichen, Farben, Fettschrift an denselben Stellen wie das SVG "
          f"({len(a)} Zeichen)", a == b, (sorted(a - b)[:3], sorted(b - a)[:3]))
    svg, info = ex.render(sa.objectList, sa.camera, background=(1, 1, 1))
    if ex.content_box(sa.objectList, sa.camera, False) is not None:      # (Terminal: am Ende geschlossen, nichts zu sehen)
        check(f"{name}: Artikelbild höchstens 548 px breit ({info['width']} px)", info["fits"])

# Palette-Einträge des Editors
pre = ed["presets"]
check("Editor-Palette „Bildschirm & Fenster“: Terminal, Datei-Ansicht, TUI: top, TUI: Pager, Textblock, Schloss",
      list(pre) == ["Terminal", "Datei-Ansicht", "TUI: top", "TUI: Pager", "Textblock", "Schloss"], list(pre))
for label, p in pre.items():
    m = engine_model([p["spec"]], [], "creation")
    sc = ModelScene(m)
    sc.construct()
    sc.show_static()
    svg, info = ex.render(sc.objectList, sc.camera, background=(1, 1, 1))
    check(f"Palette {label}: baut und zeichnet ({info['width']}×{info['height']} px)", "<path" in svg or "<text" in svg)
    if p["segments"] is not None:
        check(f"Palette {label}: Editor zählt so viele Zustände wie die Engine ({p['segments']})",
              p["segments"] == T.step_count(p["spec"]["args"]["text"]))
check("Editor: Dauer je Zustand (Tippen „cd Dokumente⏎“ mit 14 Zeichen/s, sonst 0,6 s)",
      pre["Terminal"]["times"] == [0.93, 0.6], pre["Terminal"]["times"])
js = EDITOR.read_text(encoding="utf-8")
check("Editor lädt engine/ansi.py und engine/terminal.py", '"ansi.py"' in js and '"terminal.py"' in js)
check("Editor: Auswahllisten für frame, theme, buttons", all(k in js for k in ('"Terminal.frame"', '"Terminal.theme"', '"Terminal.buttons"')))
# Farbe ist genau #rrggbb: ein Text, der mit # beginnt, bleibt Text (Kommentarzeile, #!/bin/bash, root-Prompt)
s = Szene("t/hash")
d = s.datei("skript.sh", "#!/bin/bash\n# Kommentar\necho hallo")
pm = es.python_model(json.loads(json.dumps(s.model())), defaults, kinds, "de", [])
em = engine_model(**editor_models({"h": s.model()})["models"]["h"])
check("Text, der mit # beginnt, bleibt Text (Export und Editor)", pm["objects"][0]["args"]["text"].startswith("#!/bin/bash")
      and em["objects"][0]["args"]["text"] == pm["objects"][0]["args"]["text"])

print("\nF1 BAUSTEINE TESTS " + ("PASSED" if ok else "FAILED"))
sys.exit(0 if ok else 1)

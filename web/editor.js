// Editor UI: palette (click to add) + background + click-to-select + live preview
// via the Python engine (Pyodide). Pyodide runs on the main thread, so previews are debounced.

const ENGINE_FILES = [
  "__init__.py", "constants.py", "camera.py", "renderer.py", "AnimObject.py",
  "bezier.py", "plotting.py", "simpleShape.py", "text.py", "svg.py", "axes.py", "threed.py", "value_tracker.py",
  "results.py", "calc.py", "geometry.py", "processes.py", "arithmetic.py", "animation.py", "rate_functions.py", "scene.py", "scene_model.py",
];

// Mirror of engine/results.py: which results each object type offers (static scalar ones for now).
// prefix is the "symbol = formula = " text; the interpreter fills the number after it.
const RESULT_CATALOG = {
  Circle: [
    { key:"radius", label:"Radius", prefix:"r = " },
    { key:"area", label:"Area", prefix:"A = πr² = " },
    { key:"circumference", label:"Circumference", prefix:"C = 2πr = " },
  ],
  Rectangle: [
    { key:"width", label:"Width", prefix:"w = " }, { key:"height", label:"Height", prefix:"h = " },
    { key:"area", label:"Area", prefix:"A = w·h = " },
    { key:"perimeter", label:"Perimeter", prefix:"P = 2(w+h) = " },
    { key:"diagonal", label:"Diagonal", prefix:"d = √(w²+h²) = " },
  ],
  Square: [
    { key:"side", label:"Side", prefix:"a = " },
    { key:"area", label:"Area", prefix:"A = a² = " },
    { key:"perimeter", label:"Perimeter", prefix:"P = 4a = " },
    { key:"diagonal", label:"Diagonal", prefix:"d = a√2 = " },
  ],
  Line: [
    { key:"length", label:"Length", prefix:"L = " },
    { key:"slope", label:"Slope", prefix:"m = " },
  ],
  FunctionGraph: [
    { key:"integral", label:"Integral (area)", prefix:"∫ = " },
  ],
  Riemann: [
    { key:"area", label:"Area (approx.)", prefix:"A ≈ " },
    { key:"error", label:"Error vs exact", prefix:"|Δ| = " },
  ],
};
const WEB_PY = ["canvas_painter.py", "editor_backend.py"];
// Engine/Python files are fetched fresh each load (unique URL) so a cached .py can never go
// stale against a newer editor.js — the "expected 3, got 2" class of bug cannot recur.
const BUILD = Date.now();

// Palette + each type's editable properties (input type inferred from the default value).
// Fill shapes start with fill_color == color (outline), so after creation the two match; the
// user can then split them. stroke_width = pen thickness. show_center = little centre dot.
// Objects, sorted by SUBJECT (Fach) -> TOPIC (Themenbereich).
const CATALOG = {
  "Mathematik · Geometrie": {
    Circle:    { center:[0,0,0], radius:1.0, color:"#59a0eb", fill_color:"#59a0eb", fill_opacity:0.5, stroke_width:4, show_center:false },
    Dot:       { center:[0,0,0], radius:0.08, color:"#111111", stroke_width:4, show_center:false },
    Line:      { start:[-1,0,0], end:[1,0,0], color:"#111111", stroke_width:4, show_center:false },
    Rectangle: { center:[0,0,0], width:2.0, height:1.0, color:"#111111", fill_color:"#111111", fill_opacity:0.5, stroke_width:4, show_center:false },
    Square:    { center:[0,0,0], side:1.0, color:"#111111", fill_color:"#111111", fill_opacity:0.5, stroke_width:4, show_center:false },
    Vector:    { end:[2,1,0], start:[0,0,0], color:"#111111", stroke_width:4 },   // 2D & 3D
  },
  "Mathematik · Funktionen & Achsen": {
    // One coordinate system, always 3D-capable: the z-axis is hidden in 2D view and appears when
    // you orbit into 3D. Fixed on-screen size (x/y/z_length); the range only rescales.
    Axes:          { x_range:[-10,10], y_range:[-10,10], z_range:[-10,10], x_length:7, y_length:7, z_length:7, x_color:"#000000", y_color:"#000000", z_color:"#000000", grid_x:false, grid_y:false, grid_z:false, grid_color:"#000000", grid_width:1 },
    FunctionGraph: { func:"sin(x)", x_range:[-10,10], adaptive:false, res_max:64, res_min:15, color:"#59a0eb", stroke_width:4, stroke_opacity:0.5, grid_color:"#ffffff", grid_width:0.5 },
  },
  "Mathematik · 3D-Flächen & Körper": {   // Surface uses the axes; solids live in world coordinates
    Surface:    { func:"sin(x)*cos(y)", adaptive:false, res_max:64, res_min:15, color:"#59a0eb", fill_opacity:1.0, grid_color:"#ffffff", grid_width:0.5 },
    Sphere:     { radius:1.0, center:[0,0,0], resolution:10, color:"#59a0eb", fill_opacity:0.5 },
    Box:        { width:1.5, height:1.0, depth:1.0, center:[0,0,0], color:"#59a0eb", fill_opacity:0.5 },
    Cube:       { side:1.2, center:[0,0,0], color:"#59a0eb", fill_opacity:0.5 },
    Pyramid:    { base:1.5, height:2.0, center:[0,0,0], color:"#59a0eb", fill_opacity:0.5 },
  },
  "Elektrotechnik · Signale": {   // presets: same FunctionGraph type, different standard signal (t = variable)
    "ε(t) step":      { _type:"FunctionGraph", func:"epsilon(t)", x_range:[-4,4], color:"#59a0eb", stroke_width:4 },
    "rect(t)":        { _type:"FunctionGraph", func:"rect(t)", x_range:[-4,4], color:"#59a0eb", stroke_width:4 },
    "tri(t)":         { _type:"FunctionGraph", func:"tri(t)", x_range:[-4,4], color:"#59a0eb", stroke_width:4 },
    "si(t)=sin t / t":{ _type:"FunctionGraph", func:"si(t)", x_range:[-12,12], color:"#59a0eb", stroke_width:4 },
    "sinc(t)":        { _type:"FunctionGraph", func:"sinc(t)", x_range:[-6,6], color:"#59a0eb", stroke_width:4 },
    "ramp(t)":        { _type:"FunctionGraph", func:"ramp(t)", x_range:[-4,4], color:"#59a0eb", stroke_width:4 },
  },
  "Allgemein · Text & LaTeX": {
    Text:   { text:"Text", position:[0,0,0], font_size:40, color:"#111111" },
    MathTex:{ tex:"\\frac{a}{b}", height:1.2, position:[0,0,0], color:"#111111" },   // real LaTeX via MathJax -> VMobjects
  },
};

// Ready-made scenes. Each is an editor model (objects + animations) the user can load and then
// tweak. `key` links an object to animations that target it (ids are assigned fresh on load).
// Only scenes buildable with today's engine are here; Faltung (convolution) etc. follow once
// ValueTracker/updaters land (see ROADMAP).
const TEMPLATES = {
  "Empty axes": {
    objects: [{ type:"Axes", props:{ x_range:[-6,6], y_range:[-3,3], x_length:12, y_length:6 } }],
  },
  "Sine (drawn)": {
    objects: [
      { type:"Axes", props:{ x_range:[-6,6], y_range:[-2,2], x_length:12, y_length:5 } },
      { key:"g", type:"FunctionGraph", props:{ func:"sin(x)", x_range:[-6,6] } },   // style = current catalog defaults
    ],
    animations: [{ type:"Create", targetKey:"g", run_time:2.0 }],
  },
  "Parabola + point": {
    objects: [
      { type:"Axes", props:{ x_range:[-3,3], y_range:[-1,5], x_length:10, y_length:6 } },
      { type:"FunctionGraph", props:{ func:"x**2", x_range:[-3,3] } },
      { key:"p", type:"Dot", props:{ center:[1,1,0] } },
    ],
    animations: [{ type:"GrowFromCenter", targetKey:"p", run_time:1.0 }],
  },
  "Riemann approximation": {
    objects: [
      { type:"Axes", props:{ x_range:[0,3.2], y_range:[-0.2,1.2], x_length:12, y_length:6 } },
      { type:"Riemann", props:{ func:"sin(x)", count:12, color:"#59a0eb", fill_opacity:0.5 },
        children:[ { type:"DecimalNumber", props:{ position:[2.5,1.0,0], font_size:38, color:"#111111", decimals:3, prefix:"A ≈ " }, result:{ key:"area" }, visible:true } ] },
      { key:"g", type:"FunctionGraph", props:{ func:"sin(x)", x_range:[0,3.2], color:"#111111", stroke_width:5 } },
    ],
    animations: [{ type:"Create", targetKey:"g", run_time:2.0 }],
  },
  "Unit circle": {
    objects: [
      { type:"Axes", props:{ x_range:[-2,2], y_range:[-2,2], x_length:7, y_length:7 } },
      { type:"Circle", props:{ center:[0,0,0], radius:1.0, fill_opacity:0.15, show_center:true } },   // thin fill + centre dot are the point here
    ],
  },
  "Function f(x) (2D)": {              // replaces the former 3D Surface template (a plain 2D graph)
    objects: [
      { type:"Axes", props:{ x_range:[-6,6], y_range:[-1.3,1.3], x_length:12, y_length:5 } },
      { key:"g", type:"FunctionGraph", props:{ func:"exp(-x^2/8)*cos(3*x)", x_range:[-6,6] } },
    ],
    animations: [{ type:"Create", targetKey:"g", run_time:2.5 }],
  },
  "3D solids": {
    camera: { mode:"3d", theta:0.6, phi:1.0 },
    objects: [
      { type:"Axes", props:{ x_range:[-4,4], y_range:[-3,3], z_range:[-3,3], x_length:8, y_length:6, z_length:6 } },
      { type:"Sphere", props:{ radius:1.0, center:[-2,0,0], resolution:10, color:"#e03a2f", fill_opacity:0.5 } },
      { type:"Cube", props:{ side:1.4, center:[0,0,0], color:"#2f9e44", fill_opacity:0.5 } },
      { type:"Pyramid", props:{ base:1.6, height:2.0, center:[2,0,0], color:"#f08c00", fill_opacity:0.5 } },
    ],
  },
  "Convolution f∗g (animated)": {
    objects: [
      { type:"Axes", props:{ x_range:[-5,5], y_range:[-0.3,1.4], x_length:12, y_length:5 } },
      { key:"f", type:"FunctionGraph", props:{ func:"exp(-x^2)", x_range:[-5,5], color:"#59a0eb", stroke_width:4 } },
      { key:"g", type:"FunctionGraph", props:{ func:"exp(-x^2)", x_range:[-5,5], color:"#2f9e44", stroke_width:4 } },
    ],
    computations: [
      { type:"Convolution", inputs:{ f:"f", g:"g" }, props:{ run_time:6, tau_range:[-5,5], color:"#e03a2f", stroke_width:5 } },
    ],
  },
  "Intersection of two circles": {
    objects: [
      { key:"c1", type:"Circle", props:{ center:[-0.7,0,0], radius:1.3, color:"#59a0eb", fill_color:"#59a0eb", fill_opacity:0.22, stroke_width:4, show_center:false } },
      { key:"c2", type:"Circle", props:{ center:[0.7,0,0], radius:1.3, color:"#e03a2f", fill_color:"#e03a2f", fill_opacity:0.22, stroke_width:4, show_center:false } },
    ],
    computations: [
      { type:"Intersection", inputs:{ a:"c1", b:"c2" }, props:{ color:"#8b2fd6", fill_color:"#8b2fd6", fill_opacity:0.55, stroke_width:3 },
        children:[ { type:"DecimalNumber", props:{ position:[0,1.9,0], font_size:32, color:"#111111", decimals:3, prefix:"Intersection area = " }, result:{ key:"area" }, visible:true } ] },
    ],
  },
};

// Shown once when the editor opens with no saved scene, so the user starts from a concrete 3D example
// rather than an empty canvas. A surface z = sin(x)+cos(y), viewed in 3D. Only the resolution is pinned
// (a moderate 24×24 = snappy greeting, not the heavy 64² default); all other styling comes from catalog
// defaults via ensureDefaults.
const START_EXAMPLE = {
  camera: { mode:"3d", theta:0.6, phi:1.0 },
  objects: [
    { type:"Axes", props:{ x_range:[-5,5], y_range:[-5,5], z_range:[-3,3], x_length:8, y_length:8, z_length:5 } },
    { type:"Surface", props:{ func:"sin(x)+cos(y)", adaptive:false, res_max:24 } },
  ],
};

// Computations = OPERATIONS over objects, shown as animated processes. Each references existing
// objects as operands (type-checked). Categorised by subject -> topic.
const SHAPE_TYPES = ["Circle", "Rectangle", "Square", "Triangle", "Polygon"];
// Operations, sorted: first whether they need OTHER objects as operands (standalone first), then by the
// kind of mathematical object they work on (numbers/series vs functions vs geometry).
const COMPUTATIONS = {
  "Eigenständig · Reihen (Σ ∏)": {   // no operands; over an index i, from i=start to i=end (number or symbolic 'n')
    "Summation  (Σ)": { type:"Summation", kind:"summation",
      props:{ sum_mode:"number", term:"1/i^2", from:1, to:"n", show_terms:3, run_time:5, size:1.4, position:[0,0,0],
              color:"#111111", var_color:"#ff7f0e", value_color:"#2ca02c", end_color:"#9467bd", pulse_color:"#66b3ff", bound_color:"#d62728" } },
    "Product  (∏)": { type:"BigProduct", kind:"product",
      props:{ sum_mode:"number", term:"i", from:1, to:"n", show_terms:3, run_time:5, size:1.4, position:[0,0,0],
              color:"#111111", var_color:"#ff7f0e", value_color:"#2ca02c", end_color:"#9467bd", pulse_color:"#66b3ff", bound_color:"#d62728" } },
  },
  "Eigenständig · Zahlen (Arithmetik)": {   // typed-in numbers; shown as squares or on a number line
    "Addition  (a + b)":       { type:"Addition",       kind:"numbers", numbers:[10,4], props:{ run_time:4, mode:"squares" } },
    "Subtraction  (a − b)":    { type:"Subtraction",    kind:"numbers", numbers:[10,4], props:{ run_time:4, mode:"squares" } },
    "Multiplication  (a × b)": { type:"Multiplication", kind:"numbers", numbers:[3,4],  props:{ run_time:4, mode:"squares" } },
    "Division  (a ÷ b)":       { type:"Division",       kind:"numbers", numbers:[12,3], props:{ run_time:4, mode:"squares" } },
  },
  "Operanden · Funktionen": {   // need existing FunctionGraphs as operands
    "Convolution  (f ∗ g)": { type:"Convolution", inputs:[{role:"f",label:"Function f",accept:["FunctionGraph"]},{role:"g",label:"Function g",accept:["FunctionGraph"]}], props:{ run_time:6, tau_range:[-5,5], color:"#e03a2f", stroke_width:5 } },
    "Product  (f · g)":     { type:"Product",     inputs:[{role:"f",label:"f",accept:["FunctionGraph"]},{role:"g",label:"g",accept:["FunctionGraph"]}], props:{ color:"#8b2fd6", stroke_width:4 } },
    "Sum  (f + g)":         { type:"Sum",         inputs:[{role:"f",label:"f",accept:["FunctionGraph"]},{role:"g",label:"g",accept:["FunctionGraph"]}], props:{ color:"#8b2fd6", stroke_width:4 } },
    "Difference  (f − g)":  { type:"Difference",  inputs:[{role:"f",label:"f",accept:["FunctionGraph"]},{role:"g",label:"g",accept:["FunctionGraph"]}], props:{ color:"#8b2fd6", stroke_width:4 } },
  },
  "Operanden · Geometrie": {   // need existing shapes as operands
    "Intersection  (A ∩ B)":{ type:"Intersection", inputs:[{role:"a",label:"Shape A",accept:SHAPE_TYPES},{role:"b",label:"Shape B",accept:SHAPE_TYPES}], props:{ color:"#8b2fd6", fill_color:"#8b2fd6", fill_opacity:0.55, stroke_width:3 }, result:[{key:"area",prefix:"Intersection area = "}] },
  },
};
const COMP_DEFS = {};
for (const grp of Object.values(COMPUTATIONS)) for (const [name, def] of Object.entries(grp)) COMP_DEFS[def.type] = { ...def, name };

// Default props per OBJECT type (from the catalog). Used to BACKFILL older/saved/template objects that
// predate newer props (e.g. an Axes saved before show_grid/grid_color/grid_width existed) so the
// properties panel always shows every current setting.
const OBJ_DEFAULTS = {};
for (const grp of Object.values(CATALOG)) for (const [name, def] of Object.entries(grp)) {
  const type = def._type || name;
  if (!(type in OBJ_DEFAULTS)) { const d = { ...def }; delete d._type; OBJ_DEFAULTS[type] = d; }
}
function ensureDefaults(o){
  const d = OBJ_DEFAULTS[o.type];
  if (d && o.props) for (const k in d) if (!(k in o.props)) o.props[k] = structuredClone(d[k]);
  if (o.type === "Axes" && o.props) delete o.props.show_grid;         // obsolete: replaced by grid_x/grid_y/grid_z
  if (o.type === "FunctionGraph" && o.props) delete o.props.y_range;  // obsolete: y range now comes from the Axes
  if (o.children) for (const c of o.children) ensureDefaults(c);
}
function migrateModel(){ for (const o of (model.objects || [])) ensureDefaults(o); }

const BG_ID = "__bg__";
const $ = (id) => document.getElementById(id);
const setStatus = (m) => { $("status").textContent = m; };

let renderModel = null, pickFn = null, preparePlay = null, playFrame = null;
let playing = false, playStart = 0, playDuration = 0, rafId = null;
// Animations, grouped by KIND OF MOTION (appear/disappear vs. move).
const ANIM_GROUPS = {
  "Erscheinen": ["Create", "FadeIn", "Write", "GrowFromCenter"],
  "Bewegen":    ["Shift", "MoveTo", "Rotate", "Scale"],
  "Betonen":    ["Indicate"],
};
const ANIM_TYPES = Object.values(ANIM_GROUPS).flat();     // flat list (used where grouping isn't needed)
const model = { objects: [], animations: [], computations: [], background: { color:"#ffffff", transparent:false, shadows:true, axes_on_top:false }, selectedId: null, selectedComp: null, playMode: "sequential", angleUnit: "rad", domain: "real", camera: { mode:"2d", theta:0.6, phi:1.0, zoom:1.0 } };
let nextId = 1, nextAnimId = 1, nextCompId = 1;
let clipboard = null;                 // last copied object spec {type, props}, for paste/duplicate
let orbitFn = null;                   // fast 3D re-aim (set after Pyodide boot)
let zoomFn = null;                    // fast zoom repaint (set after Pyodide boot)
let beginLodFn = null, endLodFn = null;   // enter/leave reduced-detail during camera moves
let unprojFn = null, bboxFn = null, projFn = null;   // pixel<->world + object's screen bbox (move-gizmo + box)
let nudgeFn = null;                   // fast object translate during a drag (no rebuild)
let bgFn = null;                      // fast background recolour (theme toggle / bg picker, no rebuild)

// ---------- model -> python ----------
function hexToRgb(h){ const n=parseInt(h.slice(1),16); return [((n>>16)&255)/255,((n>>8)&255)/255,(n&255)/255]; }
function toArgs(props){
  const a={};
  for(const [k,v] of Object.entries(props)) a[k] = (typeof v==="string" && v.startsWith("#")) ? hexToRgb(v) : v;
  return a;
}
function objToSpec(o){                                 // editor node -> interpreter spec (recursive)
  const spec = { id:o.id, type:o.type, args:toArgs(o.props) };
  if(o.visible===false) spec.visible = false;
  if(o.result) spec.result = o.result;
  if(o.a) spec.a = o.a;                                // object references (e.g. Intersection)
  if(o.b) spec.b = o.b;
  if(o.children && o.children.length) spec.children = o.children.map(objToSpec);
  return spec;
}
function toPythonModel(){
  const objects = model.objects.map(objToSpec);
  const bg = model.background.transparent ? null : hexToRgb(model.background.color);
  // Global play mode: "parallel" -> all animations share one step (run together);
  // "sequential" -> each its own step (run one after another, in list order).
  const animations = model.animations.filter(a=>a.visible!==false).map((a,i)=>({   // eye-hidden -> skipped
    type:a.type, target:a.target, run_time:a.run_time,
    step: model.playMode==="parallel" ? 0 : i,
    args: a.type==="Shift"  ? { vector:a.vector }
        : a.type==="MoveTo" ? { point:a.point }
        : a.type==="Rotate" ? { angle:(a.angle||0)*Math.PI/180 }   // store degrees, send radians
        : a.type==="Scale"  ? { factor:a.factor }
        : {},
  }));
  const computations = model.computations.map(c=>{
    const def = COMP_DEFS[c.type];
    const spec = { id:c.id, type:c.type, props:toArgs(c.props) };
    if(c.visible===false) spec.visible = false;
    if(def && def.kind==="numbers"){
      spec.numbers = c.numbers;
    } else if(def && (def.kind==="summation" || def.kind==="product")){
      // number mode: resolve the step-by-step choreography pieces (abstract -> substitute -> compute)
      if((c.props.sum_mode||"number")!=="function"){
        const ch = buildChoreo(c);
        if(ch) spec.props = { ...spec.props, choreo: ch };   // not ready -> omit; KaTeX overlay shows meanwhile
      }
    } else {
      spec.inputs = c.inputs;
      if(c.children && c.children.length) spec.children = c.children.map(objToSpec);
    }
    return spec;
  });
  injectTexGlyphs(objects);                   // MathTex: resolve `tex` -> glyph data (async, cached)
  return { objects, animations, computations, background: bg, shadows: !!model.background.shadows,
           axes_on_top: model.background.axes_on_top === true,
           angle_unit: model.angleUnit, domain: model.domain, camera: model.camera };
}

// ---------- 3D level-of-detail (LOD) ----------
// Our renderer is a CPU painter (no GPU z-buffer), like matplotlib's mplot3d. Beyond ~2500 faces the
// per-quad Canvas draw calls make an orbit drag stutter. So, like GeoGebra/CAD tools, we render at
// REDUCED detail WHILE rotating and snap back to full detail on release. Only surfaces/solids with a
// resolution above the cap are heavy enough to bother.
const ORBIT_DETAIL_CAP = 28;
function _hasY(f){ return /(^|[^A-Za-z0-9_])y([^A-Za-z0-9_]|$)/.test(String(f||"")); }
function needsLOD(){
  let hit=false;
  const scan=(o)=>{
    const r=o&&o.props&&(o.props.res_max||o.props.resolution);
    if(typeof r==="number" && r>ORBIT_DETAIL_CAP &&
       (o.type==="Surface" || o.type==="Sphere" || (o.type==="FunctionGraph" && _hasY(o.props.func)))) hit=true;
    if(o&&o.children) o.children.forEach(scan);
  };
  model.objects.forEach(scan);
  return hit;
}
function _capResolution(x){                         // cap every resolution field in a model tree
  if(Array.isArray(x)){ x.forEach(_capResolution); }
  else if(x && typeof x==="object"){
    for(const k in x){
      if((k==="res_max"||k==="resolution"||k==="res_min") && typeof x[k]==="number" && x[k]>ORBIT_DETAIL_CAP) x[k]=ORBIT_DETAIL_CAP;
      else _capResolution(x[k]);
    }
  }
}
function lowDetailModelJson(){ const m=toPythonModel(); _capResolution(m); return JSON.stringify(m); }
// Level-of-detail for ANY camera action (orbit drag, zoom, ViewCube snap): once a camera move starts,
// rebuild the scene ONCE at reduced resolution so re-aiming/zooming stays smooth; snap back to full
// detail when the move ends.
let _lowDetail=false;
function enterLowDetail(){
  if(_lowDetail || playing || !beginLodFn) return;
  _lowDetail=true;
  if(typeof clearMoveGizmo==="function") clearMoveGizmo();   // hide the move arrows while the camera moves
  try{ beginLodFn(lowDetailModelJson()); }catch(_){}   // build a reduced copy once; end_lod restores (no rebuild)
}
function exitLowDetail(){
  if(_lowDetail){
    _lowDetail=false;
    if(endLodFn){ try{ endLodFn(); }catch(_){} }    // restore the already-built full scene (no rebuild -> instant)
  }
  if(typeof refreshMoveGizmo==="function") refreshMoveGizmo();   // reposition the move arrows for the new camera
  saveLocal();                                      // persist the new camera either way
}

// ---------- ViewCube (CAD-style navigation gizmo, top-right) ----------
// Mirrors the camera orientation and rotates with it. Each face is a distinctly coloured side of the
// 3D world; hovering highlights it, clicking SNAPS the camera to look straight along that axis - an
// axis-aligned ("2D") view of the scene from that side. Inspired by AutoCAD / Fusion 360 ViewCubes.
const VC_POLE = Math.PI/2 - 0.001;      // just shy of the pole (avoids the look-at degeneracy)
const VC_FACES = [
  { key:"RIGHT",  label:"RIGHT", col:[226,104,92],  normal:[ 1,0,0], corners:[[1,-1,-1],[1,1,-1],[1,1,1],[1,-1,1]],     theta:0,            phi:0 },
  { key:"LEFT",   label:"LEFT",  col:[224,152,66],  normal:[-1,0,0], corners:[[-1,1,-1],[-1,-1,-1],[-1,-1,1],[-1,1,1]], theta:Math.PI,      phi:0 },
  { key:"BACK",   label:"BACK",  col:[104,174,100], normal:[0, 1,0], corners:[[1,1,-1],[-1,1,-1],[-1,1,1],[1,1,1]],     theta:Math.PI/2,    phi:0 },
  { key:"FRONT",  label:"FRONT", col:[82,156,232],  normal:[0,-1,0], corners:[[-1,-1,-1],[1,-1,-1],[1,-1,1],[-1,-1,1]], theta:-Math.PI/2,   phi:0 },
  { key:"TOP",    label:"TOP",   col:[168,138,214], normal:[0,0, 1], corners:[[-1,-1,1],[1,-1,1],[1,1,1],[-1,1,1]],     theta:-Math.PI/2,   phi:VC_POLE },
  { key:"BOTTOM", label:"BOT",   col:[120,122,134], normal:[0,0,-1], corners:[[-1,1,-1],[1,1,-1],[1,-1,-1],[-1,-1,-1]], theta:-Math.PI/2,   phi:-VC_POLE },
];
let vcHover = null;

function _vcRot(theta, phi){                       // same z-up look-at frame as engine/camera.py
  const ct=Math.cos(theta), st=Math.sin(theta), ce=Math.cos(phi), se=Math.sin(phi);
  const cam=[ce*ct, ce*st, se], fwd=[-cam[0],-cam[1],-cam[2]];
  let right=[fwd[1], -fwd[0], 0];                  // cross(fwd, worldUp=[0,0,1])
  const rn=Math.hypot(right[0],right[1],right[2]); right = rn>1e-9 ? [right[0]/rn,right[1]/rn,right[2]/rn] : [1,0,0];
  let up=[right[1]*fwd[2]-right[2]*fwd[1], right[2]*fwd[0]-right[0]*fwd[2], right[0]*fwd[1]-right[1]*fwd[0]];
  const un=Math.hypot(up[0],up[1],up[2]); up=[up[0]/un,up[1]/un,up[2]/un];
  return {right, up, cam};
}
function _vcProjectFace(R, corners, S){
  const s=S*0.26, c=S/2;
  return corners.map(p=>[ c + (R.right[0]*p[0]+R.right[1]*p[1]+R.right[2]*p[2])*s,
                          c - (R.up[0]*p[0]+R.up[1]*p[1]+R.up[2]*p[2])*s ]);
}
function _vcDepth(R, n){ return R.cam[0]*n[0]+R.cam[1]*n[1]+R.cam[2]*n[2]; }   // >0 => faces the viewer
function _vcMouse(e){ const cv=$("viewcube"), r=cv.getBoundingClientRect(); return [ (e.clientX-r.left)*cv.width/r.width, (e.clientY-r.top)*cv.height/r.height ]; }
function _pointInPoly(x,y,poly){
  let inside=false;
  for(let i=0,j=poly.length-1;i<poly.length;j=i++){
    const xi=poly[i][0],yi=poly[i][1],xj=poly[j][0],yj=poly[j][1];
    if(((yi>y)!==(yj>y)) && (x < (xj-xi)*(y-yi)/(yj-yi)+xi)) inside=!inside;
  }
  return inside;
}
function _vcFaceAt(mx,my){
  const S=$("viewcube").width, R=_vcRot(model.camera.theta, model.camera.phi);
  let best=null, bestd=0;
  for(const f of VC_FACES){
    const d=_vcDepth(R,f.normal); if(d<=0) continue;                 // back-facing -> not pickable
    if(_pointInPoly(mx,my,_vcProjectFace(R,f.corners,S)) && d>bestd){ best=f; bestd=d; }
  }
  return best;
}
function viewCubeVisible(){ return model.camera.mode==="3d"; }
function drawViewCube(){
  const cv=$("viewcube"); if(!cv) return;
  if(!viewCubeVisible()){ cv.style.display="none"; return; }
  cv.style.display="block";
  const ctx=cv.getContext("2d"), S=cv.width;
  ctx.clearRect(0,0,S,S);
  const R=_vcRot(model.camera.theta, model.camera.phi);
  const vis=VC_FACES.map(f=>({f,d:_vcDepth(R,f.normal)})).filter(o=>o.d>0).sort((a,b)=>a.d-b.d);  // far->near
  ctx.lineJoin="round"; ctx.font="bold "+Math.round(S*0.11)+"px sans-serif"; ctx.textAlign="center"; ctx.textBaseline="middle";
  for(const {f,d} of vis){
    const poly=_vcProjectFace(R,f.corners,S);
    ctx.beginPath(); ctx.moveTo(poly[0][0],poly[0][1]);
    for(let i=1;i<poly.length;i++) ctx.lineTo(poly[i][0],poly[i][1]);
    ctx.closePath();
    const hl=(vcHover===f.key), bright=0.60+0.40*Math.min(1,d);       // more face-on => brighter
    const rgb=f.col.map(x=>Math.min(255,Math.round(x*bright+(hl?55:0))));
    ctx.fillStyle=`rgb(${rgb[0]},${rgb[1]},${rgb[2]})`; ctx.fill();
    ctx.strokeStyle="rgba(28,28,38,.9)"; ctx.lineWidth=S*0.012; ctx.stroke();
    if(d>0.55){                                                        // label the front-most face
      const cx=poly.reduce((s,p)=>s+p[0],0)/poly.length, cy=poly.reduce((s,p)=>s+p[1],0)/poly.length;
      ctx.fillStyle="rgba(255,255,255,.95)"; ctx.fillText(f.label,cx,cy);
    }
  }
}
function _tweenCamera(tTheta, tPhi){
  const t0=model.camera.theta, p0=model.camera.phi;
  let dT=((tTheta-t0+Math.PI)%(2*Math.PI)+2*Math.PI)%(2*Math.PI)-Math.PI;  // shortest angular path
  const dP=tPhi-p0, T=320, start=performance.now();
  enterLowDetail();                                                 // reduce detail while the camera flies
  (function step(now){
    let a=(now-start)/T; if(a>1) a=1;
    const e=a<.5 ? 2*a*a : 1-Math.pow(-2*a+2,2)/2;                   // easeInOutQuad
    model.camera.theta=t0+dT*e; model.camera.phi=p0+dP*e;
    if(orbitFn) orbitFn(model.camera.theta, model.camera.phi);
    drawViewCube(); drawCamGizmo();
    if(a<1) requestAnimationFrame(step); else exitLowDetail();      // snap back to full detail at the end
  })(performance.now());
}
function initViewCube(){
  const cv=$("viewcube"); if(!cv) return;
  cv.onpointermove=(e)=>{ const [mx,my]=_vcMouse(e); const f=_vcFaceAt(mx,my); const k=f?f.key:null;
    if(k!==vcHover){ vcHover=k; cv.style.cursor=k?"pointer":"default"; drawViewCube(); } };
  cv.onpointerleave=()=>{ if(vcHover){ vcHover=null; drawViewCube(); } };
  cv.onclick=(e)=>{ if(playing) return; const [mx,my]=_vcMouse(e); const f=_vcFaceAt(mx,my);
    if(f) _tweenCamera(f.theta, f.phi); };
  drawViewCube();
}

// ---------- Camera rotation gizmo (an arcball, below the ViewCube) ----------
// A rotation BALL like other 3D programs: a sphere wrapped in three great-circle rings (X red / Y green /
// Z blue) that show the current orientation and turn WITH the camera. Grab a ring and drag to rotate the
// camera around that axis; grab the ball itself to orbit freely. A circular-arrow button resets to the
// default 3D view.
const GIZ_LIMIT = Math.PI/2 - 0.03;                  // elevation clamp (matches the canvas orbit)
const GIZ_DEF_THETA = 0.6, GIZ_DEF_PHI = 1.0;        // default 3D view (matches model.camera defaults)
const GIZ_RINGS = [                                   // each ring = a great circle in the plane ⟂ its axis
  { k:"X", axis:[1,0,0], pt:(t)=>[0, Math.cos(t), Math.sin(t)], col:[226,96,84]  },   // YZ plane
  { k:"Y", axis:[0,1,0], pt:(t)=>[Math.sin(t), 0, Math.cos(t)], col:[104,174,100]},   // ZX plane
  { k:"Z", axis:[0,0,1], pt:(t)=>[Math.cos(t), Math.sin(t), 0], col:[82,140,232] },   // XY plane
];
let gizHover=null, gizDrag=null, gizPrevAng=0;   // gizDrag: {ring} while turning a ring, else null

function camGizmoVisible(){ return model.camera.mode==="3d"; }
function _camVec(theta,phi){ const ce=Math.cos(phi); return [ce*Math.cos(theta), ce*Math.sin(theta), Math.sin(phi)]; }
function _setCamVec(v){                               // camera direction -> (theta, phi), elevation clamped
  const n=Math.hypot(v[0],v[1],v[2])||1; const z=Math.max(-1,Math.min(1, v[2]/n));
  model.camera.phi = Math.max(-GIZ_LIMIT, Math.min(GIZ_LIMIT, Math.asin(z)));
  model.camera.theta = Math.atan2(v[1], v[0]);
}
function _rotAround(v, a, d){                          // Rodrigues: rotate vector v around unit axis a by d
  const co=Math.cos(d), si=Math.sin(d), dot=a[0]*v[0]+a[1]*v[1]+a[2]*v[2];
  const cx=a[1]*v[2]-a[2]*v[1], cy=a[2]*v[0]-a[0]*v[2], cz=a[0]*v[1]-a[1]*v[0];
  return [ v[0]*co+cx*si+a[0]*dot*(1-co), v[1]*co+cy*si+a[1]*dot*(1-co), v[2]*co+cz*si+a[2]*dot*(1-co) ];
}
function _gizMouse(e){ const cv=$("camgizmo"), r=cv.getBoundingClientRect(); return [ (e.clientX-r.left)*cv.width/r.width, (e.clientY-r.top)*cv.height/r.height ]; }
function _gizBall(){ const cv=$("camgizmo"), W=cv.width, H=cv.height;
  return { W, H, cx:W/2, cy:H*0.39, r:W*0.40, R:_vcRot(model.camera.theta, model.camera.phi) }; }
function _gizProject(b, v){                            // 3D point on the unit sphere -> [screenX, screenY, depth]
  return [ b.cx + (b.R.right[0]*v[0]+b.R.right[1]*v[1]+b.R.right[2]*v[2])*b.r,
           b.cy - (b.R.up[0]*v[0]+b.R.up[1]*v[1]+b.R.up[2]*v[2])*b.r,
           b.R.cam[0]*v[0]+b.R.cam[1]*v[1]+b.R.cam[2]*v[2] ];     // depth: >0 = front (toward viewer)
}
function _ringPoints(b, ring, n){ const out=[]; for(let i=0;i<=n;i++) out.push(_gizProject(b, ring.pt(i/n*2*Math.PI))); return out; }
function _gizResetGeom(){ const cv=$("camgizmo"), W=cv.width, H=cv.height; return { x:W/2, y:H-W*0.20, r:W*0.10 }; }
function _gizRingAt(mx,my){                            // nearest ring (preferring the front-facing side)
  const b=_gizBall(); let best=null, bd=b.W*0.085;
  for(const ring of GIZ_RINGS) for(const p of _ringPoints(b,ring,54)){
    if(p[2] < -0.12) continue;                         // ignore the far back of the ring
    const dd=Math.hypot(p[0]-mx, p[1]-my); if(dd<bd){ bd=dd; best=ring; }
  }
  return best;
}
function _gizInReset(mx,my){ const g=_gizResetGeom(); return Math.hypot(mx-g.x, my-g.y) <= g.r*1.3; }
function _gizReset(){ _tweenCamera(GIZ_DEF_THETA, GIZ_DEF_PHI); }   // fly back (also repaints cube + gizmo)
function drawCamGizmo(){
  const cv=$("camgizmo"); if(!cv) return;
  if(!camGizmoVisible()){ cv.style.display="none"; return; }
  cv.style.display="block";
  const b=_gizBall(), ctx=cv.getContext("2d"), W=b.W, H=b.H;
  ctx.clearRect(0,0,W,H);
  ctx.fillStyle="rgba(120,132,155,.12)"; ctx.beginPath(); ctx.arc(b.cx,b.cy,b.r,0,2*Math.PI); ctx.fill();   // sphere
  ctx.lineWidth=W*0.008; ctx.strokeStyle="rgba(120,132,155,.40)"; ctx.stroke();
  ctx.lineCap="round";
  for(const ring of GIZ_RINGS){                        // each ring: segment-by-segment, back dim / front bright
    const pts=_ringPoints(b, ring, 72), hl=(gizHover===ring.k), c=ring.col;
    for(let i=1;i<pts.length;i++){ const a=pts[i-1], p=pts[i], front=((a[2]+p[2])*0.5)>0;
      ctx.strokeStyle=`rgba(${c[0]},${c[1]},${c[2]},${front?(hl?1:0.9):(hl?0.4:0.22)})`;
      ctx.lineWidth=(front?W*0.03:W*0.02)*(hl?1.35:1);
      ctx.beginPath(); ctx.moveTo(a[0],a[1]); ctx.lineTo(p[0],p[1]); ctx.stroke(); }
    const tip=_gizProject(b, ring.axis);               // little axis label at the +axis pole (front only)
    if(tip[2]>0.2){ ctx.fillStyle=`rgb(${c[0]},${c[1]},${c[2]})`; ctx.font="bold "+Math.round(W*0.11)+"px sans-serif";
      ctx.textAlign="center"; ctx.textBaseline="middle"; ctx.fillText(ring.k, tip[0], tip[1]); }
  }
  _gizDrawReset(ctx, _gizResetGeom(), gizHover==="reset");
}
function _gizDrawReset(ctx, b, hl){                    // circular-arrow "reset rotation" button
  const col = hl ? "rgb(50,50,62)" : "rgba(95,95,108,.92)";
  ctx.lineCap="round"; ctx.lineWidth=b.r*0.24; ctx.strokeStyle=col; ctx.fillStyle=col;
  const a0=-Math.PI*0.40, a1=Math.PI*1.12;             // ~270° arc, gap at the top-right for the arrowhead
  ctx.beginPath(); ctx.arc(b.x,b.y,b.r,a0,a1); ctx.stroke();
  // symmetric arrowhead at the a0 end, pointing along the (clockwise) tangent
  const hx=b.x+Math.cos(a0)*b.r, hy=b.y+Math.sin(a0)*b.r;
  const dir=a0-Math.PI/2, ah=b.r*0.72, perp=dir+Math.PI/2, hw=ah*0.62;
  const tip=[hx+Math.cos(dir)*ah*0.6, hy+Math.sin(dir)*ah*0.6];
  const bx=hx-Math.cos(dir)*ah*0.4, by=hy-Math.sin(dir)*ah*0.4;   // base centre, behind the tip
  ctx.beginPath();
  ctx.moveTo(tip[0], tip[1]);
  ctx.lineTo(bx+Math.cos(perp)*hw, by+Math.sin(perp)*hw);
  ctx.lineTo(bx-Math.cos(perp)*hw, by-Math.sin(perp)*hw);
  ctx.closePath(); ctx.fill();
}
function initCamGizmo(){
  const cv=$("camgizmo"); if(!cv) return;
  cv.onpointermove=(e)=>{
    const [mx,my]=_gizMouse(e);
    if(gizDrag){                                       // drag a ring -> rotate around THAT axis only (precise)
      const b=_gizBall(); let ang=Math.atan2(my-b.cy, mx-b.cx);
      let d=ang-gizPrevAng; d=((d+Math.PI)%(2*Math.PI)+2*Math.PI)%(2*Math.PI)-Math.PI; gizPrevAng=ang;
      _setCamVec(_rotAround(_camVec(model.camera.theta, model.camera.phi), gizDrag.ring.axis, d));
      if(orbitFn) orbitFn(model.camera.theta, model.camera.phi);
      drawViewCube(); drawCamGizmo();
      return;
    }
    const ring=_gizRingAt(mx,my);
    const k = ring ? ring.k : (_gizInReset(mx,my) ? "reset" : null);
    if(k!==gizHover){ gizHover=k; cv.style.cursor=k?"pointer":"default"; drawCamGizmo(); }
  };
  cv.onpointerdown=(e)=>{
    if(playing) return;
    const [mx,my]=_gizMouse(e);
    if(_gizInReset(mx,my)){ _gizReset(); return; }
    const b=_gizBall(), ring=_gizRingAt(mx,my);
    if(!ring) return;                                  // gizmo = PRECISE axis rotation only; free orbit = mouse-drag in the canvas
    cv.setPointerCapture(e.pointerId); cv.style.cursor="grabbing";
    gizDrag = { ring }; gizPrevAng=Math.atan2(my-b.cy, mx-b.cx);
    enterLowDetail();                                  // reduce detail while rotating
  };
  const end=()=>{ if(gizDrag){ gizDrag=null; exitLowDetail(); } cv.style.cursor=gizHover?"pointer":"default"; };
  cv.onpointerup=end; cv.onpointercancel=end;
  cv.onpointerleave=()=>{ if(!gizDrag && gizHover){ gizHover=null; drawCamGizmo(); } };
  drawCamGizmo();
}

// ---------- preview (debounced) ----------
let _timer = null;
function renderPreview(){ if(!renderModel) return; clearTimeout(_timer); _timer = setTimeout(_doRender, 70); }
function _doRender(){
  if(playing) return;                 // the player loop owns the canvas while playing
  let res;
  try { res = renderModel(JSON.stringify(toPythonModel())); }
  catch(e){ console.error(e); setStatus("Render error: " + e.message); return; }
  setStatus(String(res).startsWith("error") ? "⚠ " + res + " (last frame kept)" : "Ready ✓");
  if(typeof drawViewCube==="function") drawViewCube();   // keep the nav-cube in sync with the camera
  if(typeof drawCamGizmo==="function") drawCamGizmo();   // and the rotation gizmo
  if(typeof refreshMoveGizmo==="function") refreshMoveGizmo();   // and the selected object's move arrows
  if(typeof updateSumOverlay==="function") updateSumOverlay(null);   // Σ overlay: full (static) view
  saveLocal();                         // autosave so a scene survives closing the page
}

// ---------- model ops (objects form a TREE: each object may have .children = result objects) ----------
function findNode(id, list=model.objects){
  for(const o of list){
    if(o.id===id) return o;
    if(o.children){ const r=findNode(id, o.children); if(r) return r; }
  }
  return null;
}
function parentListOf(id, list=model.objects){                 // the array that directly contains id
  if(list.some(o=>o.id===id)) return list;
  for(const o of list){ if(o.children){ const r=parentListOf(id, o.children); if(r) return r; } }
  return null;
}
function cloneSpec(o){                                         // deep copy with fresh ids (incl. children)
  const c = { id:"o"+(nextId++), type:o.type, props:structuredClone(o.props) };
  if(o.visible!==undefined) c.visible = o.visible;
  if(o.expanded!==undefined) c.expanded = o.expanded;
  if(o.result) c.result = structuredClone(o.result);
  if(o.a) c.a = o.a;                                  // keep references to the original objects
  if(o.b) c.b = o.b;
  if(o.children) c.children = o.children.map(cloneSpec);
  return c;
}
const selected = () => (model.selectedId===BG_ID ? null : findNode(model.selectedId));
// GeoGebra-style: each new coloured object cycles to the next palette colour, so two objects of the
// same kind (e.g. two function graphs) are automatically distinct. Text/LaTeX keep their colour (black).
const AUTO_COLORS = ["#1f77b4","#e8820c","#2ca02c","#d62728","#9467bd","#17becf","#8c564b","#e377c2"];
let autoColorIdx = 0;
// Every colour an object currently uses (recursively) — so a COPY can be given one nobody else has.
function usedColors(list=model.objects, acc=new Set()){
  for(const o of list){ if(o.props && typeof o.props.color==="string") acc.add(o.props.color.toLowerCase()); if(o.children) usedColors(o.children, acc); }
  return acc;
}
function freshColor(){
  const used = usedColors();
  return AUTO_COLORS.find(c=>!used.has(c.toLowerCase())) || AUTO_COLORS[autoColorIdx++ % AUTO_COLORS.length];   // all taken -> cycle
}
// Give a copied spec a colour no other element has (mirrors addObject's auto-colour). Text/LaTeX keep black.
function recolorFresh(spec){
  if(spec.type!=="Text" && spec.type!=="MathTex" && spec.props && typeof spec.props.color==="string"){
    const c = freshColor(); spec.props.color = c;
    if("fill_color" in spec.props) spec.props.fill_color = c;      // keep fill in step with the outline
  }
  return spec;
}
function addObject(type, defaults){
  const id = "o"+(nextId++);
  const props = structuredClone(defaults);
  if(props.color && type!=="Text" && type!=="MathTex"){
    const c = AUTO_COLORS[autoColorIdx++ % AUTO_COLORS.length];
    props.color = c;
    if("fill_color" in props) props.fill_color = c;       // keep fill in step with the outline
  }
  model.objects.push({ id, type, props });
  model.selectedId = id;
  renderSceneObjs(); renderProps(); renderPreview();
}
function deleteObject(id){
  const list = parentListOf(id); if(!list) return;
  list.splice(list.findIndex(o=>o.id===id), 1);
  model.animations = model.animations.filter(a=>a.target!==id);        // drop animations targeting it
  for(const c of model.computations) for(const k in c.inputs){ if(c.inputs[k]===id) c.inputs[k]=undefined; }  // clear operand refs
  if(model.selectedId===id) model.selectedId = null;
  renderSceneObjs(); renderComputations(); renderProps(); renderPreview();
}
function selectObject(id){ model.selectedId = id; model.selectedComp = null; renderSceneObjs(); renderComputations(); renderProps(); if(typeof refreshMoveGizmo==="function") refreshMoveGizmo(); }
function deselect(){ model.selectedId = null; model.selectedComp = null; renderSceneObjs(); renderComputations(); renderProps(); if(typeof refreshMoveGizmo==="function") refreshMoveGizmo(); }   // click outside -> clear selection + hide move-gizmo

// ---------- computations (operations over objects) ----------
function addComputation(def){
  const c = { id:"k"+(nextCompId++), type:def.type, props:structuredClone(def.props||{}) };
  if(def.kind==="numbers"){
    c.numbers = (def.numbers||[2,2]).slice();           // number operands (typed in), not object refs
  } else if(def.kind==="summation" || def.kind==="product"){
    /* nothing extra: term / bounds live in props */
  } else {
    c.inputs = {};
    if(def.result) c.children = def.result.map(r=>({ id:"o"+(nextId++), type:"DecimalNumber", result:{ key:r.key }, visible:true,
      props:{ position:[0,2,0], font_size:30, color:"#111111", decimals:3, prefix:r.prefix } }));
  }
  model.computations.push(c);
  model.selectedComp = c.id; model.selectedId = null;
  renderComputations(); renderSceneObjs(); renderProps(); renderPreview();
}
function selectComputation(id){ model.selectedComp = id; model.selectedId = null; renderComputations(); renderSceneObjs(); renderProps(); }
function deleteComputation(id){
  model.computations = model.computations.filter(c=>c.id!==id);
  if(model.selectedComp===id) model.selectedComp = null;
  renderComputations(); renderProps(); renderPreview();
}
function duplicateObject(id){
  const list = parentListOf(id); if(!list) return;
  const i = list.findIndex(o=>o.id===id);
  const copy = recolorFresh(cloneSpec(list[i]));               // all properties + children come along; fresh colour
  list.splice(i+1, 0, copy);                                  // insert right after the original
  model.selectedId = copy.id;
  renderSceneObjs(); renderProps(); renderPreview();
}

function instantiate(spec, keyToId){                           // template spec -> live node (recursive)
  const node = { id:"o"+(nextId++), type:spec.type, props:structuredClone(spec.props) };
  if(spec.key) keyToId[spec.key] = node.id;
  if(spec.visible!==undefined) node.visible = spec.visible;
  if(spec.result) node.result = structuredClone(spec.result);
  if(spec.a) node.a = keyToId[spec.a];                // remap object references (defined earlier)
  if(spec.b) node.b = keyToId[spec.b];
  if(spec.children) node.children = spec.children.map(c=>instantiate(c, keyToId));
  return node;
}
function loadTemplate(tpl){
  stopPlay();
  model.objects = []; model.animations = []; model.computations = []; model.selectedComp = null;
  const keyToId = {};
  for(const o of tpl.objects) model.objects.push(instantiate(o, keyToId));
  for(const a of (tpl.animations || [])){
    const anim = { id:"a"+(nextAnimId++), type:a.type, target:keyToId[a.targetKey], run_time:a.run_time ?? 1.0 };
    if(a.type==="Shift") anim.vector = a.vector ? a.vector.slice() : [2,0,0];
    model.animations.push(anim);
  }
  for(const cs of (tpl.computations || [])){
    const c = { id:"k"+(nextCompId++), type:cs.type, props:structuredClone(cs.props || {}) };
    if(cs.numbers){
      c.numbers = cs.numbers.slice();
    } else {
      c.inputs = {};
      for(const [role, key] of Object.entries(cs.inputs || {})) c.inputs[role] = keyToId[key];
      if(cs.children) c.children = cs.children.map(ch=>instantiate(ch, keyToId));
    }
    model.computations.push(c);
  }
  if(tpl.background) model.background = structuredClone(tpl.background);
  model.background = Object.assign({ color:"#ffffff", transparent:false, shadows:true, axes_on_top:false }, model.background||{});
  migrateModel();                                   // backfill props the template spec omits (grid_color, …)
  if(tpl.playMode) model.playMode = tpl.playMode;
  model.camera = tpl.camera ? structuredClone(tpl.camera) : { mode:"2d", theta:0.6, phi:1.0 };
  const vm = $("view-mode"); if(vm) vm.value = model.camera.mode;      // sync the 2D/3D toggle
  model.selectedId = model.objects.length ? model.objects[0].id : null;
  renderSceneObjs(); renderComputations(); renderProps(); renderPreview();
}

function addAnimation(type){
  if(!selected()) return;
  const a = { id:"a"+(nextAnimId++), type, target:model.selectedId, run_time:1.0 };
  if(type==="Shift") a.vector=[2,0,0];
  else if(type==="MoveTo") a.point=[0,0,0];
  else if(type==="Rotate") a.angle=90;          // degrees
  else if(type==="Scale") a.factor=1.5;
  model.animations.push(a);
  renderProps(); renderSceneAnims(); renderPreview();
}
function deleteAnimation(id){ model.animations = model.animations.filter(a=>a.id!==id); renderProps(); renderSceneAnims(); renderPreview(); }

// Transport: Play runs the animated scene once from the current position to the end (operators run
// their process, operands are taken over). Pause freezes. Reset returns to the static EDIT view
// (all objects as inserted). End jumps to the final frame.
let playT = 0;                        // current animation time (seconds)
let paused = false;                   // true only while paused (so ▶ resumes instead of restarting)
function _prepare(){ playDuration = preparePlay(JSON.stringify(toPythonModel())); return playDuration > 0; }
function startPlay(){
  if(playing || !preparePlay) return;
  if(!_prepare()){ setStatus("Nothing to play — add an animation, or an animated operation."); return; }
  if(!paused || playT >= playDuration) playT = 0;        // fresh play from the start, unless resuming a pause
  paused = false;
  playing = true; const startWall = performance.now() - playT*1000; setStatus("Playing …");
  const loop = (now)=>{
    if(!playing) return;
    playT = (now - startWall)/1000;
    if(playT >= playDuration){ playT = playDuration; playFrame(playT); updateSumOverlay(1); playing = false; setStatus("Ended ✓"); return; }
    playFrame(playT); updateSumOverlay(playT/Math.max(1e-6,playDuration)); rafId = requestAnimationFrame(loop);
  };
  rafId = requestAnimationFrame(loop);
}
function pausePlay(){ if(!playing) return; playing = false; paused = true; if(rafId) cancelAnimationFrame(rafId); setStatus("Paused"); }
function stopPlay(){ playing = false; paused = false; if(rafId) cancelAnimationFrame(rafId); playT = 0; }   // used on edits/settings
function resetPlay(){ stopPlay(); renderPreview(); setStatus("Reset — edit view"); }         // back to static view
function endPlay(){
  if(!preparePlay || !_prepare()) return;
  playing = false; paused = false; if(rafId) cancelAnimationFrame(rafId);
  playT = playDuration; playFrame(playDuration); updateSumOverlay(1); setStatus("End ✓");
}

// ---------- save / load (download a .json, re-open it, + autosave to the browser) ----------
const LS_KEY = "animate.scene.v1";
function sceneData(){
  return { v:1, counters:{ nextId, nextAnimId, nextCompId },
    model:{ objects:model.objects, animations:model.animations, computations:model.computations,
            background:model.background, playMode:model.playMode, angleUnit:model.angleUnit, domain:model.domain, camera:model.camera } };
}
function applyScene(data){
  const m = (data && data.model) || data || {};
  model.objects = m.objects || [];
  model.animations = m.animations || [];
  model.computations = m.computations || [];
  model.background = Object.assign({ color:"#ffffff", transparent:false, shadows:true, axes_on_top:false }, m.background || {});
  model.playMode = m.playMode || "sequential";
  model.angleUnit = m.angleUnit || "rad";
  model.domain = m.domain || "real";
  model.camera = m.camera || { mode:"2d", theta:0.6, phi:1.0 };
  migrateModel();                                   // backfill any props added since the scene was saved
  model.selectedId = model.objects.length ? model.objects[0].id : null;
  model.selectedComp = null;
  const cc = data && data.counters;
  if(cc){ nextId=Math.max(nextId, cc.nextId||1); nextAnimId=Math.max(nextAnimId, cc.nextAnimId||1); nextCompId=Math.max(nextCompId, cc.nextCompId||1); }
  const set=(id,v)=>{ const e=$(id); if(e) e.value=v; };
  set("play-mode",model.playMode); set("angle-unit",model.angleUnit); set("domain-mode",model.domain); set("view-mode",model.camera.mode);
  renderSceneObjs(); renderComputations(); renderProps(); renderPreview();
}
function saveScene(){
  const blob=new Blob([JSON.stringify(sceneData(),null,2)],{type:"application/json"});
  const a=document.createElement("a"); a.href=URL.createObjectURL(blob); a.download="szene.animate.json"; a.click(); URL.revokeObjectURL(a.href);
  setStatus("Scene saved ✓");
}
function loadSceneFile(file){
  const r=new FileReader();
  r.onload=()=>{ try{ applyScene(JSON.parse(r.result)); setStatus("Scene loaded ✓"); } catch(e){ setStatus("Load failed: "+e.message); } };
  r.readAsText(file);
}
function saveLocal(){ try{ localStorage.setItem(LS_KEY, JSON.stringify(sceneData())); } catch(e){} }

// ---------- UI ----------
function buildPalette(){
  const el=$("palette"); el.innerHTML="";
  for(const [group,types] of Object.entries(CATALOG)){
    const d=document.createElement("details"); d.className="group"; d.open=false;   // collapsed by default
    const s=document.createElement("summary"); s.textContent=group; d.appendChild(s);
    for(const [label,defaults] of Object.entries(types)){
      const type = defaults._type || label;              // presets: display label + explicit _type
      const props = {...defaults}; delete props._type;
      const b=document.createElement("span"); b.className="palette-item"; b.textContent=label;
      b.onclick=()=>addObject(type,props); d.appendChild(b);
    }
    el.appendChild(d);
  }
}
// Templates sorted by subject -> topic (shown as <optgroup>s).
const TEMPLATE_GROUPS = {
  "Mathematik · Analysis": ["Empty axes","Sine (drawn)","Function f(x) (2D)","Parabola + point","Riemann approximation","Convolution f∗g (animated)"],
  "Mathematik · Geometrie": ["Unit circle","Intersection of two circles"],
  "Mathematik · 3D": ["3D solids"],
};
function buildTemplates(){
  const sel=$("templates"); sel.innerHTML="";
  const ph=document.createElement("option"); ph.value=""; ph.textContent="— choose template —"; sel.appendChild(ph);
  const seen=new Set();
  const addOpt=(og,name)=>{ const o=document.createElement("option"); o.value=name; o.textContent=name; og.appendChild(o); seen.add(name); };
  for(const [grp,names] of Object.entries(TEMPLATE_GROUPS)){
    const og=document.createElement("optgroup"); og.label=grp;
    for(const name of names) if(TEMPLATES[name]) addOpt(og,name);
    if(og.children.length) sel.appendChild(og);
  }
  const rest=Object.keys(TEMPLATES).filter(n=>!seen.has(n));   // any uncategorised template
  if(rest.length){ const og=document.createElement("optgroup"); og.label="Weitere"; for(const name of rest) addOpt(og,name); sel.appendChild(og); }
  sel.onchange=()=>{ const t=TEMPLATES[sel.value]; if(t) loadTemplate(t); sel.value=""; };
}
// Categorised "add computation" palette (subject -> topic). Click adds a skeleton (no operands yet).
function buildCompPalette(){
  const el=$("comp-palette"); el.innerHTML="";
  for(const [group,items] of Object.entries(COMPUTATIONS)){
    const d=document.createElement("details"); d.className="group"; d.open=false;   // collapsed by default
    const s=document.createElement("summary"); s.textContent=group; d.appendChild(s);
    for(const [name,def] of Object.entries(items)){
      const b=document.createElement("span"); b.className="palette-item"; b.textContent=name;
      b.onclick=()=>addComputation(def); d.appendChild(b);
    }
    el.appendChild(d);
  }
}
function compConfigured(c){
  const def=COMP_DEFS[c.type];
  if(def.kind==="numbers") return (c.numbers||[]).length>=1;
  if(def.kind==="summation" || def.kind==="product") return true;   // no object operands; always runnable
  return def.inputs.every(inp=>{ const o=c.inputs[inp.role] && findNode(c.inputs[inp.role]); return o && inp.accept.includes(o.type); });
}
function renderComputations(){
  const el=$("computations"); el.innerHTML="";
  if(model.computations.length===0){ el.innerHTML='<div class="hint">No operations yet.</div>'; return; }
  for(const c of model.computations){
    const def=COMP_DEFS[c.type]; const ok=compConfigured(c);
    const row=document.createElement("div"); row.className="obj-row"+(c.id===model.selectedComp?" sel":"");
    row.onclick=()=>selectComputation(c.id);
    const left=document.createElement("span"); left.className="label";
    const name=document.createElement("span"); name.className="nm"; name.textContent=def.name+(ok?"":"  ⚠ incomplete");
    if(!ok) name.style.color="#b45309";
    if(c.visible===false) name.style.opacity="0.45";
    left.appendChild(name);
    const ops=document.createElement("div"); ops.className="ops";
    const eye=document.createElement("button"); eye.className="eye"; eye.innerHTML=eyeIcon(c.visible!==false);
    eye.title = c.visible!==false ? "Visible (click to hide)" : "Hidden (click to show)";
    eye.onclick=(e)=>{ e.stopPropagation(); c.visible=(c.visible===false); renderComputations(); renderPreview(); };
    const del=document.createElement("button"); del.className="del"; del.textContent="✕"; del.title="Delete"; del.onclick=(e)=>{ e.stopPropagation(); deleteComputation(c.id); };
    ops.appendChild(eye); ops.appendChild(del);
    row.appendChild(left); row.appendChild(ops); el.appendChild(row);
  }
}
// Config panel for a computation: pick the operand objects (type-checked) + tune the parameters.
function renderCompProps(container, c){
  const def=COMP_DEFS[c.type];
  const h=document.createElement("div"); h.style="font-weight:600;margin-bottom:6px"; h.textContent=def.name; container.appendChild(h);
  if(def.kind==="numbers"){
    if("mode" in c.props){                                // representation: squares or number line
      const sel=document.createElement("select");
      for(const [val,txt] of [["squares","Squares"],["numberline","Number line"]]){ const o=document.createElement("option"); o.value=val; o.textContent=txt; sel.appendChild(o); }
      sel.value=c.props.mode; sel.onchange=()=>{ c.props.mode=sel.value; renderPreview(); };
      container.appendChild(propRow("Representation", sel));
    }
    renderNumberList(container, c);
  } else if(def.kind==="summation" || def.kind==="product"){
    if(def.kind==="summation"){                             // function (Fourier) mode is sum-only
      const sel=document.createElement("select");
      for(const [val,txt] of [["number","Number series  Σ aᵢ"],["function","Function partial sum (Fourier)"]]){ const o=document.createElement("option"); o.value=val; o.textContent=txt; sel.appendChild(o); }
      sel.value=c.props.sum_mode||"number"; sel.onchange=()=>{ c.props.sum_mode=sel.value; renderPreview(); };
      container.appendChild(propRow("Mode", sel));
    }
    const hint=document.createElement("div"); hint.className="hint";
    hint.textContent = (def.kind==="product")
      ? "Index i; upper limit 'to' may be a number or 'n'. ∏ multiplies the term over i (e.g. term i → factorial)."
      : "Index i; upper limit 'to' may be a number or 'n' (symbolic). Term uses i (function mode: i and x).";
    container.appendChild(hint);
  } else {
    for(const inp of def.inputs){
      const candidates=model.objects.filter(o=>inp.accept.includes(o.type));
      const sel=document.createElement("select");
      const ph=document.createElement("option"); ph.value=""; ph.textContent="— choose object —"; sel.appendChild(ph);
      for(const o of candidates){ const op=document.createElement("option"); op.value=o.id; op.textContent=`${o.type} · ${o.id}`; sel.appendChild(op); }
      sel.value=c.inputs[inp.role]||"";
      sel.onchange=()=>{ c.inputs[inp.role]=sel.value||undefined; renderComputations(); renderPreview(); };
      container.appendChild(propRow(inp.label, sel));
      if(candidates.length===0){ const hint=document.createElement("div"); hint.className="hint"; hint.textContent="No suitable object ("+inp.accept.join(", ")+") — add one first."; container.appendChild(hint); }
    }
  }
  for(const [k,v] of Object.entries(c.props)){ if(k==="mode"||k==="sum_mode") continue; container.appendChild(propInput(c,k,v)); }
}
// Number operands (Arithmetic): up to ten typed-in numbers, each shown as coloured squares on play.
function renderNumberList(container, c){
  const title=document.createElement("div"); title.className="hint"; title.textContent="Numbers (up to 10) — each becomes a coloured group:"; container.appendChild(title);
  c.numbers.forEach((v,i)=>{
    const row=document.createElement("div"); row.className="prop";
    const l=document.createElement("label"); l.textContent="#"+(i+1); row.appendChild(l);
    const inp=document.createElement("input"); inp.type="number"; inp.step="1"; inp.value=v;
    inp.onchange=()=>{ c.numbers[i]=parseInt(inp.value||"0",10)||0; renderPreview(); }; commitOnEnter(inp);
    row.appendChild(inp);
    const del=document.createElement("button"); del.textContent="✕"; del.title="Remove"; del.style="border:none;background:none;color:#ef4444;cursor:pointer";
    del.onclick=()=>{ c.numbers.splice(i,1); renderComputations(); renderProps(); renderPreview(); };
    row.appendChild(del); container.appendChild(row);
  });
  if(c.numbers.length<10){
    const add=document.createElement("span"); add.className="palette-item"; add.textContent="+ number";
    add.onclick=()=>{ c.numbers.push(1); renderProps(); renderPreview(); }; container.appendChild(add);
  }
}
// Eye (visible) / eye-off (hidden) icon — Feather-style inline SVG, so it renders everywhere.
function eyeIcon(visible){
  const s = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">';
  return visible
    ? s + '<path d="M1 12s4-7 11-7 11 7 11 7-4 7-11 7-11-7-11-7z"/><circle cx="12" cy="12" r="3"/></svg>'
    : s + '<path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"/><line x1="1" y1="1" x2="23" y2="23"/></svg>';
}
function renderSceneObjs(){
  const el=$("scene-objs"); el.innerHTML="";
  const bgRow=document.createElement("div"); bgRow.className="obj-row"+(model.selectedId===BG_ID?" sel":"");
  bgRow.textContent="Settings"; bgRow.onclick=()=>selectObject(BG_ID);              // whole row
  el.appendChild(bgRow);
  if(model.objects.length===0){ const h=document.createElement("div"); h.className="hint"; h.textContent="No objects yet."; el.appendChild(h); }
  const renderNode=(o, depth)=>{
    const row=document.createElement("div"); row.className="obj-row"+(o.id===model.selectedId?" sel":"");
    row.style.paddingLeft=(8+depth*16)+"px";                                          // indent children
    row.onclick=()=>selectObject(o.id);                                              // whole row selects
    const left=document.createElement("span"); left.className="label";
    const kids = o.children && o.children.length;
    if(kids){                                                                        // expand/collapse caret
      const car=document.createElement("button"); car.className="caret"; car.textContent = (o.expanded!==false) ? "▾" : "▸";
      car.onclick=(e)=>{ e.stopPropagation(); o.expanded = (o.expanded===false); renderSceneObjs(); };
      left.appendChild(car);
    } else { const sp=document.createElement("span"); sp.className="caret"; left.appendChild(sp); }  // align
    const name=document.createElement("span"); name.className="nm"; name.textContent=`${o.type} · ${o.id}`;
    if(o.visible===false) name.style.opacity="0.45";                                 // hidden -> dimmed
    left.appendChild(name);
    const ops=document.createElement("div"); ops.className="ops";
    const eye=document.createElement("button"); eye.className="eye"; eye.innerHTML=eyeIcon(o.visible!==false);
    eye.title = o.visible!==false ? "Visible (click to hide)" : "Hidden (click to show)";
    eye.onclick=(e)=>{ e.stopPropagation(); o.visible = (o.visible===false); renderSceneObjs(); if(model.selectedId===o.id) renderProps(); renderPreview(); };
    const dup=document.createElement("button"); dup.textContent="⧉"; dup.title="Duplicate"; dup.onclick=(e)=>{ e.stopPropagation(); duplicateObject(o.id); };
    const del=document.createElement("button"); del.className="del"; del.textContent="✕"; del.title="Delete"; del.onclick=(e)=>{ e.stopPropagation(); deleteObject(o.id); };
    ops.appendChild(eye); ops.appendChild(dup); ops.appendChild(del);
    row.appendChild(left); row.appendChild(ops); el.appendChild(row);
    if(kids && o.expanded!==false){ for(const c of o.children) renderNode(c, depth+1); }
  };
  for(const o of model.objects) renderNode(o, 0);
  renderSceneAnims();
}

// Animations overview inside the Scene box: a FLAT, ordered list whose order IS the sequential play
// order. Each row has an eye (hide = skip in playback) and a ✕, and can be DRAGGED up/down to reorder
// (= reorder the sequential execution). Click a row to select its object.
function renderSceneAnims(){
  const el=$("scene-anims"); if(!el) return; el.innerHTML="";
  const anims=model.animations||[];
  if(anims.length===0){ el.innerHTML='<div class="hint">Noch keine Animationen — Objekt wählen und in dessen Properties eine hinzufügen.</div>'; return; }
  if(model.playMode!=="parallel"){ const h=document.createElement("div"); h.className="hint"; h.style.marginBottom="4px";
    h.textContent="Reihenfolge = Abspielreihenfolge · ziehen zum Umsortieren"; el.appendChild(h); }
  anims.forEach((a,idx)=>{
    const o=findNode(a.target);
    const row=document.createElement("div"); row.className="obj-row anim-row"+(model.selectedId===a.target?" sel":"");
    row.draggable=true;
    row.ondragstart=(e)=>{ e.dataTransfer.setData("text/plain", String(idx)); e.dataTransfer.effectAllowed="move"; row.classList.add("dragging"); };
    row.ondragend=()=>row.classList.remove("dragging");
    row.ondragover=(e)=>{ e.preventDefault(); row.classList.add("drop-target"); };
    row.ondragleave=()=>row.classList.remove("drop-target");
    row.ondrop=(e)=>{ e.preventDefault(); row.classList.remove("drop-target"); const from=parseInt(e.dataTransfer.getData("text/plain"),10); if(!isNaN(from)&&from!==idx) reorderAnimation(from, idx); };
    const left=document.createElement("span"); left.className="label";
    const grip=document.createElement("span"); grip.textContent="⠿"; grip.style.cssText="cursor:grab;color:var(--muted);margin-right:6px"; left.appendChild(grip);
    const nm=document.createElement("span"); nm.className="nm"; nm.textContent = a.type + " · " + (o?`${o.type} · ${o.id}`:"(deleted)");
    if(a.visible===false) nm.style.opacity="0.45";
    left.appendChild(nm);
    if(a.run_time!=null){ const t=document.createElement("span"); t.className="hint"; t.style.marginLeft="6px"; t.textContent=a.run_time+"s"; left.appendChild(t); }
    row.onclick=()=>{ if(o) selectObject(a.target); };
    const ops=document.createElement("div"); ops.className="ops";
    const eye=document.createElement("button"); eye.className="eye"; eye.innerHTML=eyeIcon(a.visible!==false);
    eye.title = a.visible!==false ? "Sichtbar (klicken zum Ausblenden)" : "Ausgeblendet (klicken zum Einblenden)";
    eye.onclick=(e)=>{ e.stopPropagation(); a.visible=(a.visible===false); renderSceneAnims(); renderPreview(); };
    const del=document.createElement("button"); del.className="del"; del.textContent="✕"; del.title="Animation entfernen";
    del.onclick=(e)=>{ e.stopPropagation(); deleteAnimation(a.id); };
    ops.appendChild(eye); ops.appendChild(del);
    row.appendChild(left); row.appendChild(ops); el.appendChild(row);
  });
}
function reorderAnimation(from, to){
  const arr=model.animations; if(from<0||from>=arr.length||to<0||to>=arr.length) return;
  const [item]=arr.splice(from,1);
  arr.splice(to,0,item);                                  // drop onto a row = place at that position
  renderSceneAnims(); renderPreview();
}
function commitOnEnter(i){ i.addEventListener("keydown",(e)=>{ if(e.key==="Enter"){ e.preventDefault(); i.blur(); } }); }  // Enter = accept value + leave field
// Values commit on CHANGE (Enter -> blur, or clicking outside the field), NOT on every keystroke — so
// typing a number no longer re-renders (and stutters) on each digit. onchange fires exactly once, on commit.
function numberInput(value, on){ const i=document.createElement("input"); i.type="number"; i.step="0.1"; i.value=value; i.onchange=()=>on(parseFloat(i.value)); commitOnEnter(i); return i; }
function propRow(key, inputEl){ const w=document.createElement("div"); w.className="prop"; const l=document.createElement("label"); l.textContent=key; w.appendChild(l); w.appendChild(inputEl); return w; }
function propInput(obj,key,val){
  if(Array.isArray(val)){
    const vec=document.createElement("div"); vec.className="vec";
    val.forEach((comp,i)=> vec.appendChild(numberInput(comp, (x)=>{ obj.props[key][i]=x; renderPreview(); })));
    return propRow(key, vec);
  }
  if(typeof val==="boolean"){ const i=document.createElement("input"); i.type="checkbox"; i.checked=val; i.onchange=()=>{ obj.props[key]=i.checked; renderPreview(); }; return propRow(key,i); }
  if(typeof val==="number") return propRow(key, numberInput(val, (x)=>{ obj.props[key]=x; renderPreview(); }));
  if(typeof val==="string" && val.startsWith("#")){ const i=document.createElement("input"); i.type="color"; i.value=val; i.oninput=()=>{ obj.props[key]=i.value; renderPreview(); }; return propRow(key,i); }
  const i=document.createElement("input"); i.type="text"; i.value=val; i.onchange=()=>{ obj.props[key]=i.value; renderPreview(); }; commitOnEnter(i); return propRow(key,i);
}
function renderProps(){
  renderObjectProps();        // -> Properties > Object
  renderOperationProps();     // -> Properties > Operation
}
function renderOperationProps(){
  const el=$("comp-props"); el.innerHTML="";
  const c = model.selectedComp && model.computations.find(x=>x.id===model.selectedComp);
  if(!c){ el.innerHTML='<span class="hint">No operation selected.</span>'; return; }
  renderCompProps(el, c);
}
function renderObjectProps(){
  const el=$("props"); el.innerHTML="";
  if(model.selectedComp){ el.innerHTML='<span class="hint">An operation is selected.</span>'; return; }
  if(model.selectedId===BG_ID){
    const h=document.createElement("div"); h.style="font-weight:600;margin-bottom:6px"; h.textContent="Settings"; el.appendChild(h);
    const ti=document.createElement("input"); ti.type="checkbox"; ti.checked=model.background.transparent;
    ti.onchange=()=>{ model.background.transparent=ti.checked; renderPreview(); };
    const ci=document.createElement("input"); ci.type="color"; ci.value=model.background.color;
    // no renderProps() here -> the colour dialog stays open, the picker circle can be moved freely
    ci.oninput=()=>{ model.background.color=ci.value; if(model.background.transparent){ model.background.transparent=false; ti.checked=false; } if(!repaintBg()) renderPreview(); saveLocal(); };   // instant recolour, no rebuild
    const si=document.createElement("input"); si.type="checkbox"; si.checked=!!model.background.shadows;
    si.onchange=()=>{ model.background.shadows=si.checked; renderPreview(); };
    const ax=document.createElement("input"); ax.type="checkbox"; ax.checked=model.background.axes_on_top!==false;
    ax.onchange=()=>{ model.background.axes_on_top=ax.checked; renderPreview(); };
    el.appendChild(propRow("color", ci));
    el.appendChild(propRow("transparent", ti));
    el.appendChild(propRow("shadows (3D surface shading)", si));
    el.appendChild(propRow("axes on top (off = realistic depth)", ax));
    return;
  }
  const o=selected();
  if(!o){ el.innerHTML='<span class="hint">No object selected.</span>'; return; }
  const h=document.createElement("div"); h.style="font-weight:600;margin-bottom:6px"; h.textContent=o.type; el.appendChild(h);
  const skip=new Set();
  const put=(k)=>{ if(k in o.props && !skip.has(k)){ el.appendChild(propInput(o,k,o.props[k])); skip.add(k); } };
  if((o.type==="FunctionGraph"||o.type==="Surface") && ("adaptive" in o.props)){
    // Ordered layout: 1) the function equation, 2) domain, 3) resolution, 4) colours, 5) the rest.
    put("func"); put("x_range"); skip.add("y_range");     // y value range comes from the Axes, not per-function
    skip.add("adaptive"); skip.add("res_max"); skip.add("res_min");     // resolution block (rendered specially)
    const sel=document.createElement("select");
    for(const [val,txt] of [["adaptive","Adaptive (curvature)"],["static","Static (uniform)"]]){ const op=document.createElement("option"); op.value=val; op.textContent=txt; sel.appendChild(op); }
    sel.value = o.props.adaptive===false ? "static" : "adaptive";
    sel.onchange=()=>{ o.props.adaptive = (sel.value==="adaptive"); renderProps(); renderPreview(); };
    el.appendChild(propRow("resolution mode", sel));
    if(o.props.adaptive!==false){ el.appendChild(propInput(o,"res_min", o.props.res_min)); el.appendChild(propInput(o,"res_max", o.props.res_max)); }
    else { el.appendChild(propInput(o,"res_max", o.props.res_max)); }
    ["color","grid_color","grid_width","stroke_width","stroke_opacity","fill_opacity"].forEach(put);   // colours / line look
  }
  for(const [k,v] of Object.entries(o.props)){ if(skip.has(k)) continue; el.appendChild(propInput(o,k,v)); }
  renderResults(el, o);
  renderAnimations(el, o);
}

// A rough anchor (data coords) for auto-placing a result near its object.
function objAnchor(o){
  const p=o.props;
  if(p.center) return p.center;
  if(p.position) return p.position;
  if(p.start && p.end) return [(p.start[0]+p.end[0])/2, (p.start[1]+p.end[1])/2, 0];
  return [0,0,0];
}

// ---------- Move-gizmo: axis arrows at a selected object's bounding box (D + I) ----------
// Dragging an object's BODY would be ambiguous in 3D (no depth under the cursor -> chaos), so a selected,
// movable object instead shows a dashed bounding box with three axis arrows (X red / Y green / Z blue) at
// its lower-left corner. In 2D the z-arrow is edge-on, so only two show. Each arrow moves the object ONLY
// along that world axis (like the rotation gizmo) and lights up on hover. Drawn on the #editgizmo overlay
// (so hover highlight is cheap and the Python render underneath is untouched).
const WORLD_TYPES = new Set(["Sphere","Box","Cube","Pyramid"]);   // centre is world units, not axes data
const MOVE_AXES = [
  { k:"x", v:[1,0,0], col:[226,96,84]  },
  { k:"y", v:[0,1,0], col:[104,174,100]},
  { k:"z", v:[0,0,1], col:[82,140,232] },
];
const MOVE_LEN = 72;                                 // arrow length in canvas pixels (1920×1080 buffer space)
let moveHover = null, moveDrag = null, _moveGizmoCache = null, _moveRAF = 0;

function movablePosKeys(o){
  const p=(o&&o.props)||{};
  if(Array.isArray(p.center)) return ["center"];
  if(Array.isArray(p.position)) return ["position"];
  if(Array.isArray(p.start) && Array.isArray(p.end)) return ["start","end"];
  return [];                                          // FunctionGraph / Axes / Riemann / Surface: not point-positioned
}
function axesScale(){
  const ax=(model.objects||[]).find(o=>o.type==="Axes"); if(!ax) return {x:1,y:1,z:1};
  const p=ax.props||{}, xr=p.x_range||[-6,6], yr=p.y_range||[-3,3], zr=p.z_range||[-3,3];
  const xl=p.x_length!=null?p.x_length:12, yl=p.y_length!=null?p.y_length:6, zl=p.z_length!=null?p.z_length:6;
  const d=(r)=>((r[1]-r[0])||1);
  return { x:xl/d(xr), y:yl/d(yr), z:zl/d(zr) };
}
function _moveHandles(){                              // screen geometry of the arrows for the SELECTED object, or null
  const o=selected();
  if(!o || !movablePosKeys(o).length || !bboxFn || !projFn || !unprojFn) return null;
  let bb; try{ bb=bboxFn(o.id); }catch(e){ bb=null; } if(!bb) return null;
  const ax=bb[0], ay=bb[3];                           // lower-left screen corner (min x, max y)
  const aw=unprojFn(ax,ay);                           // its world point = the arrows' anchor
  const handles=[];
  for(const A of MOVE_AXES){
    const tp=projFn(aw[0]+A.v[0], aw[1]+A.v[1], aw[2]+A.v[2]);   // project a +1 world-unit step along the axis
    const dx=tp[0]-ax, dy=tp[1]-ay, len=Math.hypot(dx,dy);
    if(len<5) continue;                               // edge-on (z-axis in 2D) -> omit, so 2D shows two arrows
    const u=[dx/len, dy/len];
    handles.push({ axis:A, a:[ax,ay], u, tip:[ax+u[0]*MOVE_LEN, ay+u[1]*MOVE_LEN], worldPerPx:1/len });
  }
  return { o, bb, handles };
}
function _distToSeg(px,py,x0,y0,x1,y1){
  const dx=x1-x0, dy=y1-y0, L2=dx*dx+dy*dy;
  let t=L2 ? ((px-x0)*dx+(py-y0)*dy)/L2 : 0; t=Math.max(0,Math.min(1,t));
  return Math.hypot(px-(x0+dx*t), py-(y0+dy*t));
}
function _moveHandleAt(px,py){                        // uses the cache (no Pyodide calls) -> cheap on hover/press
  if(!_moveGizmoCache) return null;
  let best=null, bd=22;
  for(const h of _moveGizmoCache.handles){ const d=_distToSeg(px,py,h.a[0],h.a[1],h.tip[0],h.tip[1]); if(d<bd){ bd=d; best=h; } }
  return best;
}
function _drawArrow(ctx,a,t,col,hl){
  const c=hl?col.map(x=>Math.min(255,x+55)):col;
  ctx.strokeStyle=`rgb(${c[0]},${c[1]},${c[2]})`; ctx.fillStyle=ctx.strokeStyle;
  ctx.lineCap="round"; ctx.lineWidth=hl?8:6;
  ctx.beginPath(); ctx.moveTo(a[0],a[1]); ctx.lineTo(t[0],t[1]); ctx.stroke();
  const ang=Math.atan2(t[1]-a[1],t[0]-a[0]), ah=hl?22:18;
  ctx.beginPath(); ctx.moveTo(t[0],t[1]);
  ctx.lineTo(t[0]-ah*Math.cos(ang-0.42), t[1]-ah*Math.sin(ang-0.42));
  ctx.lineTo(t[0]-ah*Math.cos(ang+0.42), t[1]-ah*Math.sin(ang+0.42));
  ctx.closePath(); ctx.fill();
}
function clearMoveGizmo(){ const cv=$("editgizmo"); if(cv){ cv.getContext("2d").clearRect(0,0,cv.width,cv.height); } }
function drawMoveGizmoFromCache(){
  const cv=$("editgizmo"); if(!cv) return; const ctx=cv.getContext("2d"); ctx.clearRect(0,0,cv.width,cv.height);
  if(playing || !_moveGizmoCache) return;
  const g=_moveGizmoCache, [x0,y0,x1,y1]=g.bb, pad=10;
  ctx.strokeStyle="rgba(90,150,240,0.9)"; ctx.lineWidth=2.5; ctx.setLineDash([12,8]);
  ctx.strokeRect(x0-pad,y0-pad,(x1-x0)+2*pad,(y1-y0)+2*pad); ctx.setLineDash([]);
  for(const h of g.handles) _drawArrow(ctx,h.a,h.tip,h.axis.col, moveHover===h.axis.k);
}
function refreshMoveGizmo(){ _moveGizmoCache=_moveHandles(); drawMoveGizmoFromCache(); }   // recompute (Pyodide) + draw
function _startAxisMove(h,e,spx,spy){
  const o=selected(); const keys=movablePosKeys(o); if(!keys.length) return;
  const startVals={}; for(const k of keys) startVals[k]=(o.props[k]||[0,0,0]).slice();
  moveDrag={ o, keys, axis:h.axis, u:h.u, worldPerPx:h.worldPerPx, startVals, isWorld:WORLD_TYPES.has(o.type), s0:[spx,spy], along:0, _alongPrev:0 };
  $("view").setPointerCapture(e.pointerId); $("view").style.cursor="grabbing";
}
function _applyAxisMove(cpx,cpy){
  const md=moveDrag; const dpx=cpx-md.s0[0], dpy=cpy-md.s0[1];
  const along=(dpx*md.u[0]+dpy*md.u[1])*md.worldPerPx;    // world units along the dragged axis
  const k=md.axis.k, s=axesScale();
  const comp = md.isWorld ? along : along/(k==="x"?s.x:k==="y"?s.y:s.z);   // -> data units for on-axes objects
  const d=[0,0,0]; d[k==="x"?0:k==="y"?1:2]=comp;
  for(const key of md.keys){ const sv=md.startVals[key]; md.o.props[key]=[ sv[0]+d[0], sv[1]+d[1], (sv[2]!=null?sv[2]:0)+d[2] ]; }
  md.along=along;                                     // world distance since press (for the fast nudge)
}
// Re-render during a drag: translate the ALREADY-BUILT object by the incremental world delta (no scene
// rebuild — so dragging a heavy mesh like a Sphere stays smooth; the full, authoritative rebuild happens
// once on release). Falls back to a full rebuild only if the fast path isn't wired yet.
function _moveRerender(){ if(_moveRAF) return; _moveRAF=requestAnimationFrame(()=>{ _moveRAF=0;
  const md=moveDrag; if(!md){ return; }
  if(nudgeFn){
    const av=md.axis.v, da=(md.along||0)-(md._alongPrev||0);     // world delta along the axis since last frame
    if(da!==0){ try{ nudgeFn(md.o.id, av[0]*da, av[1]*da, av[2]*da); }catch(e){} md._alongPrev=md.along; }
  } else {
    try{ renderModel(JSON.stringify(toPythonModel())); }catch(e){}
  }
  refreshMoveGizmo(); }); }
// "Ergebnisse" section: checkboxes for the results this object type offers (see RESULT_CATALOG).
// Checking one adds a configurable DecimalNumber child placed near the object; the interpreter
// fills in the computed value after the "symbol = formula = " prefix.
function renderResults(container, o){
  const defs = RESULT_CATALOG[o.type]; if(!defs) return;
  const wrap=document.createElement("div"); wrap.style="margin-top:10px;border-top:1px solid var(--border);padding-top:8px;";
  const title=document.createElement("div"); title.style="font-weight:600;margin-bottom:6px;font-size:13px"; title.textContent="Results"; wrap.appendChild(title);
  for(const def of defs){
    const row=document.createElement("label"); row.className="prop"; row.style.cursor="pointer";
    const chk=document.createElement("input"); chk.type="checkbox";
    chk.checked = !!(o.children && o.children.some(c=>c.result && c.result.key===def.key));
    chk.onchange=()=> chk.checked ? addResult(o, def) : removeResult(o, def.key);
    const lab=document.createElement("span"); lab.textContent=def.label;
    row.appendChild(chk); row.appendChild(lab); wrap.appendChild(row);
  }
  container.appendChild(wrap);
}
function addResult(o, def){
  if(!o.children) o.children = [];
  const a = objAnchor(o);
  o.children.push({ id:"o"+(nextId++), type:"DecimalNumber", result:{ key:def.key }, visible:true,
    props:{ position:[a[0], a[1]+0.6, 0], font_size:30, color:"#111111", decimals:2, prefix:def.prefix } });
  o.expanded = true;
  renderSceneObjs(); renderProps(); renderPreview();
}
function removeResult(o, key){
  if(!o.children) return;
  o.children = o.children.filter(c=>!(c.result && c.result.key===key));
  renderSceneObjs(); renderProps(); renderPreview();
}

// The animations that target the selected object: list them (with timing + Shift vector),
// let the user delete them, and offer a button per animation type to add one.
function renderAnimations(container, o){
  const wrap=document.createElement("div"); wrap.style="margin-top:10px;border-top:1px solid var(--border);padding-top:8px;";
  const title=document.createElement("div"); title.style="font-weight:600;margin-bottom:6px;font-size:13px"; title.textContent="Animations"; wrap.appendChild(title);
  const mine=model.animations.filter(a=>a.target===o.id);
  if(mine.length===0){ const hint=document.createElement("div"); hint.className="hint"; hint.textContent="None — add below."; wrap.appendChild(hint); }
  for(const a of mine){
    const row=document.createElement("div"); row.className="prop";
    const l=document.createElement("label"); l.textContent=a.type; row.appendChild(l);
    row.appendChild(numberInput(a.run_time, (x)=>{ a.run_time=x; renderPreview(); }));       // seconds
    const del=document.createElement("button"); del.textContent="✕"; del.style="border:none;background:none;color:#ef4444;cursor:pointer"; del.onclick=()=>deleteAnimation(a.id);
    row.appendChild(del); wrap.appendChild(row);
    if(a.type==="Shift" || a.type==="MoveTo"){
      const key = a.type==="Shift" ? "vector" : "point";
      if(!Array.isArray(a[key])) a[key]=[a.type==="Shift"?2:0,0,0];
      const vr=document.createElement("div"); vr.className="prop";
      const vl=document.createElement("label"); vl.textContent=key; vr.appendChild(vl);
      const vec=document.createElement("div"); vec.className="vec";
      a[key].forEach((comp,i)=> vec.appendChild(numberInput(comp, (x)=>{ a[key][i]=x; renderPreview(); })));
      vr.appendChild(vec); wrap.appendChild(vr);
    } else if(a.type==="Rotate"){
      const vr=document.createElement("div"); vr.className="prop";
      const vl=document.createElement("label"); vl.textContent="angle°"; vr.appendChild(vl);
      vr.appendChild(numberInput(a.angle!=null?a.angle:90, (x)=>{ a.angle=x; renderPreview(); }));
      wrap.appendChild(vr);
    } else if(a.type==="Scale"){
      const vr=document.createElement("div"); vr.className="prop";
      const vl=document.createElement("label"); vl.textContent="factor"; vr.appendChild(vl);
      vr.appendChild(numberInput(a.factor!=null?a.factor:1.5, (x)=>{ a.factor=x; renderPreview(); }));
      wrap.appendChild(vr);
    }
  }
  const adder=document.createElement("div"); adder.style="margin-top:6px";
  for(const [grp,types] of Object.entries(ANIM_GROUPS)){                // grouped by kind of motion
    const h=document.createElement("div"); h.className="hint"; h.style="margin:4px 0 2px"; h.textContent=grp; adder.appendChild(h);
    for(const t of types){ const b=document.createElement("span"); b.className="palette-item"; b.textContent="+ "+t; b.onclick=()=>addAnimation(t); adder.appendChild(b); }
  }
  wrap.appendChild(adder); container.appendChild(wrap);
}

// ---------- Σ summation: real LaTeX via KaTeX, revealed step by step over the play clock ----------
// A canvas cannot match LaTeX typesetting, so the summation's typography is rendered by KaTeX as an
// overlay above the canvas (the Python engine only reserves the play duration for number mode, and
// draws the partial-sum curve for function mode).
// Substitute the running variable i with `rep`. i counts as the running variable when it is not part
// of a longer name (sin, pi, min keep their i) EXCEPT right after '_' , so an index like a_i IS hit
// (a_i -> a_1). The '_' is deliberately absent from the lookbehind set for exactly this reason.
function _substI(src, rep){ return String(src).replace(/(?<![A-Za-z0-9])i(?![A-Za-z0-9_])/g, rep); }

// Known function / constant names (everything else that is alphabetic is a FREE symbol, e.g. the a in
// 1/a_i). A term with a free symbol can't yield a number - we then keep the substituted expression and
// never print a (meaningless) numeric value or total.
const _SUM_KNOWN=new Set(["i","pi","e","E","PI","sin","cos","tan","asin","acos","atan","atan2","exp",
  "log","ln","sqrt","abs","sinh","cosh","tanh","floor","ceil","round","sign","max","min","pow"]);
function _termHasFreeSymbol(term){
  const ids=String(term||"").match(/[A-Za-z_][A-Za-z_0-9]*/g)||[];
  return ids.some(id=> !_SUM_KNOWN.has(id));
}

function exprToLatex(src){                 // our expression syntax -> LaTeX ( / -> \frac, ^ -> ^{}, * -> \cdot )
  const s=String(src||""); let p=0;
  const peek=()=>s[p], eat=()=>s[p++], skip=()=>{ while(p<s.length && s[p]===" ") p++; };
  function expr(){ let l=term(); for(;;){ skip(); const c=peek(); if(c==="+"||c==="-"){ eat(); l=l+(c==="+"?" + ":" - ")+term(); } else break; } return l; }
  function term(){ let l=factor(); for(;;){ skip(); const c=peek();
      if(c==="*"){ eat(); l=l+" \\cdot "+factor(); }
      else if(c==="/"){ eat(); l="\\frac{"+l+"}{"+factor()+"}"; }
      else break; } return l; }
  function factor(){ let b=base(); skip(); if(peek()==="^"){ eat(); return b+"^{"+factor()+"}"; } return b; }
  function base(){ skip(); const c=peek();
    if(c==="("){ eat(); const e=expr(); skip(); if(peek()===")") eat(); return "\\left("+e+"\\right)"; }
    if(c==="-"){ eat(); return "-"+base(); }
    let m=/^[0-9]*\.?[0-9]+/.exec(s.slice(p)); if(m){ p+=m[0].length; return m[0]; }
    m=/^[A-Za-z_][A-Za-z_0-9]*/.exec(s.slice(p));
    if(m){ p+=m[0].length; const nm=m[0]; skip();
      if(peek()==="("){ eat(); const e=expr(); skip(); if(peek()===")") eat(); return "\\"+nm+"\\left("+e+"\\right)"; }
      const greek={pi:"\\pi",theta:"\\theta",phi:"\\phi",omega:"\\omega",infty:"\\infty"}; return greek[nm]||nm; }
    eat(); return ""; }
  try { return expr()||s; } catch(e){ return s; }
}

function evalExprJS(src){                   // our syntax -> f(i) numeric (for the computed values)
  let js=String(src||"0").replace(/\^/g,"**").replace(/\bpi\b/g,"PI").replace(/\be\b/g,"E");
  let fn; try { fn=new Function("i","with(Math){return ("+js+");}"); } catch(e){ fn=()=>NaN; }
  return (i)=>{ try{ const v=fn(i); return (typeof v==="number"&&isFinite(v))?v:NaN; }catch(e){ return NaN; } };
}
// Prefer an exact-looking FRACTION over a decimal (reads far better under a Σ: 1/4 shows where it came
// from, 0.25 hides it). Recover p/q from the float via continued fractions, capped denominator; fall
// back to a short decimal only for genuinely irrational values (sqrt, pi, ...).
function _approxFrac(x, maxDen=10000, tol=1e-9){
  if(!isFinite(x)) return null;
  const sign=x<0?-1:1; x=Math.abs(x);
  let h0=0,h1=1,k0=1,k1=0,b=x;
  for(let it=0; it<40; it++){
    const a=Math.floor(b), h2=a*h1+h0, k2=a*k1+k0;
    if(k2>maxDen) break;
    h0=h1; h1=h2; k0=k1; k1=k2;
    if(k1>0 && Math.abs(h1/k1 - x) < tol) return [sign*h1, k1];
    const fr=b-a; if(fr<1e-12) break; b=1/fr;
  }
  // only a GENUINE rational (matches to ~1e-9 within the denominator cap) prints as a fraction;
  // irrationals (sqrt2, pi, ...) fall through to a decimal instead of an ugly near-fraction.
  return (k1>0 && Math.abs(h1/k1 - x) < tol) ? [sign*h1, k1] : null;
}
function _fmtNum(v){
  if(!isFinite(v)) return "?";
  const f=_approxFrac(v);
  if(f){ const [p,q]=f; if(q===1) return String(p); return (p<0?"-":"")+"\\frac{"+Math.abs(p)+"}{"+q+"}"; }
  return String(+v.toPrecision(5));
}
function _decStr(v){ return isFinite(v) ? String(+v.toPrecision(6)) : "?"; }   // decimal form of the total
function _isProperFrac(v){ const f=_approxFrac(v); return !!(f && f[1]!==1); }   // true -> show "fraction = decimal"

// Series operator differences (everything else is shared): Σ joins with '+' and reduces by addition;
// ∏ (BigProduct) joins with '·' and reduces by multiplication. The SAME step-by-step choreography and
// the SAME engine code (summation_choreo) render both - only the head symbol and the join/reduce differ.
function _seriesOps(c){
  return (c && c.type==="BigProduct")
    ? { opHead:"\\prod", join:"\\cdot", reduce:(a,b)=>a*b, init:1 }
    : { opHead:"\\sum",  join:"+",      reduce:(a,b)=>a+b, init:0 };
}

function sumStages(c){
  const p=c.props||{}, a=parseInt(p.from)||0, endRaw=String(p.to==null?"n":p.to).trim();
  const endNum=/^-?\d+$/.test(endRaw)?parseInt(endRaw):null, symbolic=endNum===null;
  const B=symbolic?(endRaw||"n"):String(endNum), k=Math.min(5,Math.max(1,parseInt(p.show_terms)||3)), term=p.term||"";
  const O=_seriesOps(c);
  const head=O.opHead+"_{i="+a+"}^{"+B+"} "+exprToLatex(term);  // no \color (MathJax-reliable); colours come later via per-piece stages
  let entries=[];
  if(symbolic){ for(let i=a;i<a+k;i++) entries.push({t:"num",i}); entries.push({t:"ell"}); entries.push({t:"sym",lab:B+"-1"}); entries.push({t:"sym",lab:B}); }
  else { const b=endNum; if(b-a+1<=k+2){ for(let i=a;i<=b;i++) entries.push({t:"num",i}); }
    else { for(let i=a;i<a+k;i++) entries.push({t:"num",i}); entries.push({t:"ell"}); entries.push({t:"num",i:b-1}); entries.push({t:"num",i:b}); } }
  const ev=evalExprJS(term), resolved=[];
  for(const e of entries){                                    // SUBSTITUTED expressions, not raw numbers
    if(e.t==="ell"){ resolved.push("\\cdots"); continue; }
    if(e.t==="sym"){ resolved.push(exprToLatex(_substI(term,"("+e.lab+")"))); continue; }
    resolved.push(exprToLatex(_substI(term,String(e.i))));
  }
  let ground=head + (resolved.length ? " = "+resolved.join(" "+O.join+" ") : "");
  if(!symbolic && !_termHasFreeSymbol(term)){ let tot=O.init; for(let i=a;i<=endNum;i++){ const vv=ev(i); if(isFinite(vv)) tot=O.reduce(tot,vv); }
    ground += " = "+_fmtNum(tot) + (_isProperFrac(tot) ? " = "+_decStr(tot) : ""); }   // fraction, then = decimal
  return { stages:[head, ground], head, ground, color:p.color||"#111111", mode:p.sum_mode||"number" };
}
// Step-by-step choreography spec (LaTeX per piece): Σ head, then columns = terms (abstract summand ->
// i substituted -> computed value) joined by '+', with ⋯ and a final '= total'.
function sumChoreoSpec(c){
  const p=c.props||{}, a=parseInt(p.from)||0, endRaw=String(p.to==null?"n":p.to).trim();
  const endNum=/^-?\d+$/.test(endRaw)?parseInt(endRaw):null, symbolic=endNum===null;
  const B=symbolic?(endRaw||"n"):String(endNum), k=Math.min(5,Math.max(1,parseInt(p.show_terms)||3)), term=p.term||"";
  const O=_seriesOps(c), Lt=exprToLatex(term), head=O.opHead+"_{i="+a+"}^{"+B+"} "+Lt;
  let entries=[];
  if(symbolic){ for(let i=a;i<a+k;i++) entries.push({t:"num",i}); entries.push({t:"ell"}); entries.push({t:"sym",lab:B+"-1"}); entries.push({t:"sym",lab:B}); }
  else { const b=endNum; if(b-a+1<=k+2){ for(let i=a;i<=b;i++) entries.push({t:"num",i}); }
    else { for(let i=a;i<a+k;i++) entries.push({t:"num",i}); entries.push({t:"ell"}); entries.push({t:"num",i:b-1}); entries.push({t:"num",i:b}); } }
  // A term with a free symbol (e.g. 1/a_i) can't be computed to a number: keep the substituted
  // expression as the final form (value=null) and print no total - instead of a meaningless "?".
  const symTerm=_termHasFreeSymbol(term);
  const ev=evalExprJS(term), cols=[{t:"op",g:"="}]; let first=true;
  for(const e of entries){
    if(e.t==="ell"){ if(!first) cols.push({t:"plus",g:O.join}); cols.push({t:"ell",g:"\\cdots"}); continue; }
    if(!first) cols.push({t:"plus",g:O.join}); first=false;
    if(e.t==="sym"||symTerm) cols.push({t:"term", abstract:Lt, subst:exprToLatex(_substI(term, e.t==="sym"?"("+e.lab+")":String(e.i))), value:null});
    else cols.push({t:"term", abstract:Lt, subst:exprToLatex(_substI(term,String(e.i))), value:_fmtNum(ev(e.i))});
  }
  if(!symbolic && !symTerm){ let tot=O.init; for(let i=a;i<=endNum;i++){const v=ev(i); if(isFinite(v)) tot=O.reduce(tot,v);}
    cols.push({t:"op",g:"="}); cols.push({t:"total",g:_fmtNum(tot)});
    if(_isProperFrac(tot)){ cols.push({t:"op",g:"="}); cols.push({t:"total",g:_decStr(tot)}); }   // fraction, then = decimal
  }
  return {head, cols};
}
function buildChoreo(c){                    // resolve every piece's glyphs; null until ALL are ready
  const spec=sumChoreoSpec(c), need=[spec.head];
  for(const col of spec.cols){ if(col.t==="term"){ need.push(col.abstract, col.subst); if(col.value!=null) need.push(col.value); } else need.push(col.g); }
  let ready=true;
  for(const lx of need){ if(ensureGlyphs(lx)===null) ready=false; }   // kicks off async for any missing
  if(!ready) return null;
  const g=(lx)=>_texCache[lx]||[];
  return {head:g(spec.head), cols:spec.cols.map(col=> col.t==="term"
    ? {t:"term", abstract:g(col.abstract), subst:g(col.subst), value: col.value!=null? g(col.value): null}
    : {t:col.t, g:g(col.g)})};
}
function activeSum(){ return (model.computations||[]).find(c=>(c.type==="Summation"||c.type==="BigProduct") && c.visible!==false) || null; }
function _cssColor(x){ return Array.isArray(x) ? "rgb("+x.map(v=>Math.round(v*255)).join(",")+")" : x; }
function _groundLatex(st){ return st.mode==="function" ? st.head : st.stages[st.stages.length-1]; }

// The Σ is now a real VECTOR formula (MathTex) drawn by the engine in the scene graph. The KaTeX
// overlay is only a graceful fallback: it shows the formula statically while MathJax is still turning
// it into glyph VMobjects (and if MathJax never loads). Once the glyphs are cached, the engine draws
// (and animates) the Σ on the canvas and the overlay hides. Function mode shows just the Σ head.
function updateSumOverlay(frac){
  const el=$("sum-overlay"); if(!el) return;
  const c=activeSum();
  if(!c){ el.style.display="none"; el.innerHTML=""; el.dataset.key=""; return; }
  const st=sumStages(c);
  const isFn=(st.mode==="function");
  const latex=isFn ? st.head : _groundLatex(st);
  // number mode: hide the fallback once the choreography glyphs are ready -> the engine draws/animates
  // the vector Σ. While MathJax is still resolving, show the KaTeX ground state as a placeholder.
  if(!isFn && buildChoreo(c)){ el.style.display="none"; el.innerHTML=""; el.dataset.key=""; return; }
  const key=(isFn?"fn":"load")+"|"+latex;
  el.style.display="block"; el.style.color=_cssColor(st.color);
  if(el.dataset.key===key) return;
  el.dataset.key=key;
  if(window.katex){ try{ katex.render(latex, el, {displayMode:true, throwOnError:false}); } catch(e){ el.textContent=latex; } }
  else el.textContent=latex;
}

// ---------- LaTeX -> vector glyphs (MathJax SVG). Each glyph becomes {d, m:[a,b,c,d,e,f], c:char}
// which the Python MathTex turns into Bézier VMobjects living in the scene graph (so they paint,
// Transform, zoom, orbit like any object). This is Manim's Tex->SVG->VMobject, browser edition. ----------
// MathJax tags each glyph with data-c = a HEX codepoint. Math-mode letters are Mathematical
// Alphanumeric Symbols (italic i = U+1D456, italic h = U+210E, ...), NOT plain ASCII. NFKD folds them
// back ("𝑖"->"i"), so the engine can tell which glyph is the running variable i (and TransformMatchingTex
// matches 'i' across contexts). Non-letters (=, +, Σ, digits) are unaffected.
function _glyphChar(dc){
  if(!dc) return "";
  const cp=parseInt(dc,16);
  if(!isFinite(cp)) return String(dc);
  try { return String.fromCodePoint(cp).normalize("NFKD"); } catch(e){ return ""; }
}
function _tex2glyphs(latex){            // one MathJax render -> glyph list (sync; must run in the DOM)
  const glyphs = [];
  let node;
  try { node = MathJax.tex2svg(String(latex || ""), {display:true}); } catch(e){ return glyphs; }
  const svg = node && node.querySelector("svg");
  if(!svg) return glyphs;
  const holder = document.createElement("div");
  holder.style.cssText = "position:absolute;left:-99999px;top:0;visibility:hidden";
  holder.appendChild(svg); document.body.appendChild(holder);   // must be in the DOM for getCTM()
  const arr = (m)=> m ? [m.a,m.b,m.c,m.d,m.e,m.f] : [1,0,0,1,0,0];
  const rectD = (el)=>{ const x=+el.getAttribute("x")||0,y=+el.getAttribute("y")||0,w=+el.getAttribute("width")||0,h=+el.getAttribute("height")||0;
    return (w>0&&h>0) ? `M${x} ${y} h${w} v${h} h${-w} Z` : null; };
  try {
    // Walk the RENDERED drawables in document order; resolve <use> (big operators like Σ are a <use> of
    // a glyph in <defs>); SKIP <defs> (unplaced definitions). This gives every glyph its real position
    // AND size (so Σ is not tiny), consistently - via each element's getCTM to the SVG viewport.
    svg.querySelectorAll("path, rect, use").forEach(el=>{
      if(el.closest("defs")) return;
      const tag = el.tagName.toLowerCase();
      if(tag === "use"){
        const href = el.getAttribute("href") || el.getAttribute("xlink:href") || "";
        const ref = href ? svg.querySelector(href) : null;
        if(!ref) return;
        let m = el.getCTM(); if(!m) return;
        const ux = parseFloat(el.getAttribute("x")||"0")||0, uy = parseFloat(el.getAttribute("y")||"0")||0;
        if(ux || uy) m = m.translate(ux, uy);            // <use> x/y shift the referenced content
        const rt = ref.tagName.toLowerCase();
        if(rt === "path"){ const d=ref.getAttribute("d"); if(d) glyphs.push({d, m:arr(m), c:_glyphChar(ref.getAttribute("data-c")||el.getAttribute("data-c")||"")}); }
        else if(rt === "rect"){ const d=rectD(ref); if(d) glyphs.push({d, m:arr(m), c:""}); }
      } else if(tag === "rect"){
        const d=rectD(el); if(d) glyphs.push({d, m:arr(el.getCTM()), c:""});
      } else {                                           // inline <path>
        const d=el.getAttribute("d"); if(d) glyphs.push({d, m:arr(el.getCTM()), c:_glyphChar(el.getAttribute("data-c")||"")});
      }
    });
  } catch(e){}
  document.body.removeChild(holder);
  return glyphs;
}
async function texToGlyphs(latex){
  if(!window.MathJax || !MathJax.tex2svg) return [];
  try { await MathJax.startup.promise; } catch(e){}
  let g = _tex2glyphs(latex);
  if(g.length === 0){                  // MathJax choked (e.g. on \color) -> retry WITHOUT colour so it still renders
    g = _tex2glyphs(String(latex || "").replace(/\\color\{[^}]*\}/g, ""));
  }
  return g;
}
const _texCache={}, _texPending={};
function ensureGlyphs(latex){                 // cached glyphs, or null while MathJax resolves (then re-render)
  const key=String(latex||"");
  if(key in _texCache) return _texCache[key];
  if(!_texPending[key]){
    _texPending[key]=true;
    texToGlyphs(key).then(g=>{ _texCache[key]=g; delete _texPending[key]; renderPreview(); })
                    .catch(()=>{ _texCache[key]=[]; delete _texPending[key]; });
  }
  return null;
}
function injectTexGlyphs(specs){              // turn each MathTex spec's `tex` into resolved glyph data
  for(const s of specs||[]){
    if(s.type==="MathTex"){ const g=ensureGlyphs(s.args && s.args.tex); if(s.args){ s.args.glyphs=g||[]; delete s.args.tex; } }
    if(s.children) injectTexGlyphs(s.children);
  }
}

async function fetchText(p){ const r=await fetch(p); if(!r.ok) throw new Error(`fetch ${p} (${r.status})`); return r.text(); }

async function boot(){
  buildPalette(); buildTemplates(); buildCompPalette(); renderSceneObjs(); renderComputations(); renderProps();
  setStatus("Loading Pyodide …");
  const pyodide = await loadPyodide({ indexURL:"https://cdn.jsdelivr.net/pyodide/v0.27.2/full/" });
  setStatus("Loading numpy …"); await pyodide.loadPackage("numpy");
  setStatus("Loading engine …");
  pyodide.FS.mkdir("engine");
  for(const f of ENGINE_FILES) pyodide.FS.writeFile(`engine/${f}`, await fetchText(`engine/${f}?v=${BUILD}`));
  for(const f of WEB_PY) pyodide.FS.writeFile(f, await fetchText(`py/${f}?v=${BUILD}`));
  const canvas=$("view");
  pyodide.globals.set("js_ctx", canvas.getContext("2d"));
  pyodide.globals.set("js_w", canvas.width);
  pyodide.globals.set("js_h", canvas.height);
  await pyodide.runPythonAsync(await fetchText(`py/editor_backend.py?v=${BUILD}`));
  renderModel = pyodide.globals.get("render_model");
  pickFn = pyodide.globals.get("pick");
  preparePlay = pyodide.globals.get("prepare_play");
  playFrame = pyodide.globals.get("play_frame");
  orbitFn = pyodide.globals.get("orbit");
  zoomFn = pyodide.globals.get("zoom_to");
  beginLodFn = pyodide.globals.get("begin_lod");
  endLodFn = pyodide.globals.get("end_lod");
  unprojFn = pyodide.globals.get("unproj");
  bboxFn = pyodide.globals.get("obj_screen_bbox");
  projFn = pyodide.globals.get("proj");
  nudgeFn = pyodide.globals.get("nudge_object");
  bgFn = pyodide.globals.get("set_background");
  // Canvas interaction: in 3D, drag = orbit the camera (fast repaint); a click without dragging
  // selects (pick). In 2D, a click selects. The mouse wheel zooms in/out in both modes.
  const VC_LIMIT = Math.PI/2 - 0.03;        // vertical orbit limit (both above and below the plane)
  let dragging=false, moved=false, sx=0, sy=0, th0=0, ph0=0;
  const pxy=(e)=>{ const r=canvas.getBoundingClientRect(); return [(e.clientX-r.left)/r.width*canvas.width, (e.clientY-r.top)/r.height*canvas.height]; };
  let _holdTimer=null;
  const HOLD_MS=1;                            // ~instant: the only drag action is orbiting, so apply LOD at once
  canvas.onpointerdown = (e)=>{
    sx=e.clientX; sy=e.clientY; moved=false;
    const [mpx,mpy]=pxy(e);
    const h=_moveHandleAt(mpx,mpy);               // an axis arrow of the selected object? (2D and 3D)
    if(h){ _startAxisMove(h,e,mpx,mpy); return; } // -> axis-constrained move; no orbit, no body-drag
    if(model.camera.mode==="3d"){
      dragging=true; th0=model.camera.theta; ph0=model.camera.phi; canvas.setPointerCapture(e.pointerId);
      clearTimeout(_holdTimer);               // predictive LOD: a held press (even before moving) = orbit intent
      _holdTimer=setTimeout(()=>{ if(dragging) enterLowDetail(); }, HOLD_MS);
      return;
    }
    if(pickFn){ const id=String(pickFn(mpx,mpy)); if(id) selectObject(id); }   // 2D: select on press -> gizmo appears
  };
  canvas.onpointermove = (e)=>{
    if(moveDrag){                                 // dragging an axis arrow -> move the object along that axis
      const [cpx,cpy]=pxy(e);
      if(Math.abs(e.clientX-sx)+Math.abs(e.clientY-sy)>2) moved=true;
      _applyAxisMove(cpx,cpy); _moveRerender();
      return;
    }
    if(dragging){
      const dx=e.clientX-sx, dy=e.clientY-sy;
      if(Math.abs(dx)+Math.abs(dy)>3) moved=true;
      if(moved){ clearTimeout(_holdTimer); enterLowDetail(); }   // moving -> low detail now (idempotent)
      model.camera.theta = th0 - dx*0.01;
      // phi = elevation above the ground plane: 0 = horizon (side view), +/-pi/2 = straight down/up.
      // Direct-manipulation feel: dragging UP tilts the camera DOWN (grab-and-pull), hence + dy.
      model.camera.phi = Math.max(-VC_LIMIT, Math.min(VC_LIMIT, ph0 + dy*0.01));
      if(orbitFn) orbitFn(model.camera.theta, model.camera.phi);      // re-aim only, no rebuild
      drawViewCube(); drawCamGizmo();
      return;
    }
    if(!playing){                                 // hover: highlight an axis arrow under the cursor
      const [hpx,hpy]=pxy(e); const h=_moveHandleAt(hpx,hpy); const k=h?h.axis.k:null;
      if(k!==moveHover){ moveHover=k; canvas.style.cursor=k?"grab":"default"; drawMoveGizmoFromCache(); }
    }
  };
  canvas.onpointerup = (e)=>{
    clearTimeout(_holdTimer);
    if(moveDrag){ moveDrag=null; canvas.style.cursor=moveHover?"grab":"default"; if(moved){ renderProps(); renderPreview(); } return; }   // one authoritative rebuild reconciles the live nudges
    if(dragging){
      dragging=false;
      if(moved){ exitLowDetail(); return; }       // orbited -> back to full detail
      if(_lowDetail) exitLowDetail();             // long hold without moving -> restore, then treat as click
    }
    if(!pickFn) return;                                                      // otherwise it was a click -> pick
    const [px,py]=pxy(e); const id=String(pickFn(px,py)); if(id) selectObject(id); else deselect();   // empty click -> deselect
  };
  canvas.onpointercancel = ()=>{ clearTimeout(_holdTimer); dragging=false; moveDrag=null; if(_lowDetail) exitLowDetail(); };
  // Mouse-wheel zoom: scale camera.zoom about 1.0, low-detail + fast-repaint while scrolling, full on settle.
  let _zoomTimer=null;
  canvas.onwheel = (e)=>{
    if(playing) return;
    e.preventDefault();
    enterLowDetail();                                       // reduce detail while zooming
    const f = Math.exp(-e.deltaY * 0.0015);                 // smooth multiplicative zoom
    model.camera.zoom = Math.max(0.2, Math.min(8, (model.camera.zoom||1) * f));
    if(zoomFn) zoomFn(model.camera.zoom);                   // fast repaint (no rebuild)
    clearTimeout(_zoomTimer); _zoomTimer=setTimeout(()=>{ exitLowDetail(); renderPreview(); saveLocal(); }, 180);  // rebuild -> axis ticks refine to the zoom
  };
  initViewCube(); initCamGizmo();
  setStatus("Ready ✓ — add an element on the left, or click in the view.");
  let restored=false;                  // restore the autosaved scene, else show the start example
  try{ const raw=localStorage.getItem(LS_KEY); if(raw){ const data=JSON.parse(raw); if(data && data.model && (data.model.objects||[]).length){ applyScene(data); restored=true; } } }catch(e){}
  if(!restored) loadTemplate(START_EXAMPLE);        // greet with a 3D surface (not an empty editor)
  syncThemeBg(); renderPreview();                   // canvas bg follows the theme: grey by night, white by day
}

$("reset-btn").onclick = () => resetPlay();
$("play-btn").onclick = () => startPlay();
$("pause-btn").onclick = () => pausePlay();
$("end-btn").onclick = () => endPlay();
$("save-btn").onclick = () => saveScene();
$("load-input").onchange = (e) => { if(e.target.files[0]) loadSceneFile(e.target.files[0]); e.target.value=""; };

$("play-mode").value = model.playMode;
$("play-mode").onchange = (e) => { model.playMode = e.target.value; if(playing) stopPlay(); };

$("angle-unit").value = model.angleUnit;
$("angle-unit").onchange = (e) => { model.angleUnit = e.target.value; stopPlay(); renderPreview(); };

$("domain-mode").value = model.domain;
$("domain-mode").onchange = (e) => { model.domain = e.target.value; stopPlay(); renderPreview(); };

$("view-mode").value = model.camera.mode;
$("view-mode").onchange = (e) => { model.camera.mode = e.target.value; stopPlay(); renderPreview(); };

// Copy (Ctrl/Cmd+C) the selected object and paste (Ctrl/Cmd+V) a full clone — keeps all properties.
document.addEventListener("keydown", (e)=>{
  const tag = document.activeElement && document.activeElement.tagName;
  if(tag==="INPUT" || tag==="SELECT" || tag==="TEXTAREA") return;      // don't hijack typing
  const mod = e.ctrlKey || e.metaKey;
  if(mod && e.key==="c"){ const o=selected(); if(o){ clipboard=cloneSpec(o); setStatus("Kopiert: "+o.type); } }
  else if(mod && e.key==="v"){ if(clipboard){ const copy=recolorFresh(cloneSpec(clipboard)); model.objects.push(copy); model.selectedId=copy.id; renderSceneObjs(); renderProps(); renderPreview(); } }
});

// ---------- Export: Photo (image) + Animation (video), each with a format dropdown (▾) ----------
// Video is captured with captureStream(0) + track.requestFrame(): EVERY rendered frame is pushed as one
// video frame (no dropped frames), so the result is smooth no matter how long a frame takes to render -
// unlike captureStream(fps), which drops frames when rendering can't keep up (that was the stutter).
const IMG_FORMATS = [
  { label:"PNG",  mime:"image/png",  ext:"png" },
  { label:"JPEG", mime:"image/jpeg", ext:"jpg" },
  { label:"WebP", mime:"image/webp", ext:"webp" },
  { label:"AVIF", mime:"image/avif", ext:"avif" },
  { label:"BMP",  mime:"image/bmp",  ext:"bmp" },
];
const VID_FORMATS = [
  { label:"MP4 (H.264)", mime:"video/mp4;codecs=avc1.42E01E",   ext:"mp4" },
  { label:"WebM (VP9)",  mime:"video/webm;codecs=vp9",          ext:"webm" },
  { label:"WebM (VP8)",  mime:"video/webm;codecs=vp8",          ext:"webm" },
  { label:"WebM (AV1)",  mime:"video/webm;codecs=av01.0.04M.08", ext:"webm" },
  { label:"MP4 (AV1)",   mime:"video/mp4;codecs=av01.0.04M.08",  ext:"mp4" },
];
function _imgSupported(mime){ try{ return document.createElement("canvas").toDataURL(mime).indexOf("data:"+mime)===0; }catch(e){ return false; } }
function _vidSupported(mime){ try{ return typeof MediaRecorder!=="undefined" && MediaRecorder.isTypeSupported(mime); }catch(e){ return false; } }

function exportPng(f){
  f = f || IMG_FORMATS[0];
  $("view").toBlob((blob)=>{
    if(!blob){ setStatus("⚠ Export fehlgeschlagen"); return; }
    const a=document.createElement("a"); a.href=URL.createObjectURL(blob); a.download="scene."+f.ext; a.click(); URL.revokeObjectURL(a.href);
    setStatus("Bild gespeichert ✓ (scene."+f.ext+")");
  }, f.mime, 0.95);
}

let _recording = false;
function exportVideo(f){
  if(playing || _recording){ setStatus("Busy — erst die Wiedergabe stoppen."); return; }
  if(!preparePlay || !_prepare()){ setStatus("Nichts aufzunehmen — füge eine Animation oder animierte Operation hinzu."); return; }
  const canvas=$("view");
  if(!canvas.captureStream || typeof MediaRecorder==="undefined"){ setStatus("⚠ Video wird von diesem Browser nicht unterstützt."); return; }
  f = f || VID_FORMATS.find(v=>_vidSupported(v.mime)) || { mime:"", ext:"webm" };
  const fps=30;
  let stream, track, manual=false;
  try{ stream=canvas.captureStream(0); track=stream.getVideoTracks()[0]; manual=!!(track && track.requestFrame); }catch(e){ stream=null; }
  if(!stream || !manual){ try{ stream=canvas.captureStream(fps); track=stream.getVideoTracks()[0]; }catch(e){ setStatus("⚠ captureStream nicht verfügbar."); return; } manual=false; }
  let rec; try{ rec=new MediaRecorder(stream, f.mime?{mimeType:f.mime, videoBitsPerSecond:12000000}:{}); }
  catch(e){ setStatus("⚠ Recorder: "+e.message); return; }
  const chunks=[];
  rec.ondataavailable=(e)=>{ if(e.data && e.data.size) chunks.push(e.data); };
  rec.onstop=()=>{
    const blob=new Blob(chunks, {type:(f.mime||"video/webm").split(";")[0]});
    const a=document.createElement("a"); a.href=URL.createObjectURL(blob); a.download="animation."+f.ext; a.click(); URL.revokeObjectURL(a.href);
    _recording=false; playing=false; setStatus("Animation gespeichert ✓ (animation."+f.ext+")"); renderPreview();
  };
  _recording=true; playing=true;                         // block edits / LOD / other playback while capturing
  playFrame(0); updateSumOverlay(0);
  try{ rec.start(); }catch(e){ _recording=false; playing=false; setStatus("⚠ "+e.message); return; }
  setStatus("● Nehme Animation auf …");
  const startWall=performance.now();
  let frame=0; const total=Math.max(1, Math.ceil(playDuration*fps));
  const step=()=>{
    if(!_recording) return;
    const t=Math.min(frame/fps, playDuration);
    playFrame(t); updateSumOverlay(t/Math.max(1e-6,playDuration));
    if(manual && track.requestFrame) track.requestFrame();   // push THIS rendered frame -> never dropped
    frame++;
    if(frame>total){ setTimeout(()=>{ if(rec.state!=="inactive") rec.stop(); }, 120); return; }
    const targetWall = startWall + (frame/fps)*1000;           // pace to real time (correct speed when rendering keeps up)
    setTimeout(step, Math.max(0, targetWall - performance.now()));
  };
  requestAnimationFrame(step);
}

function _buildExportMenu(menuId, formats, supported, onPick){
  const menu=$(menuId); if(!menu) return [];
  let avail = formats.filter(f=>supported(f.mime));
  if(avail.length===0) avail = [formats[0]];              // always at least the first (browser falls back)
  const use = avail.slice(0,5);
  menu.innerHTML="";
  for(const f of use){ const it=document.createElement("div"); it.className="export-item"; it.textContent=f.label;
    it.onclick=()=>{ menu.classList.remove("open"); onPick(f); }; menu.appendChild(it); }
  return use;
}
(function setupExports(){
  const pngUse=_buildExportMenu("dl-png-menu", IMG_FORMATS, _imgSupported, (f)=>{ pngFmt=f; exportPng(f); });
  const vidUse=_buildExportMenu("dl-video-menu", VID_FORMATS, _vidSupported, (f)=>{ vidFmt=f; exportVideo(f); });
  let pngFmt=pngUse[0], vidFmt=vidUse[0];
  $("dl-png").onclick   = ()=> exportPng(pngFmt);
  $("dl-video").onclick = ()=> exportVideo(vidFmt);
  const toggle=(id)=>{ const m=$(id); if(!m) return; document.querySelectorAll(".export-menu.open").forEach(x=>{ if(x!==m) x.classList.remove("open"); }); m.classList.toggle("open"); };
  const pc=$("dl-png-caret"), vc=$("dl-video-caret");
  if(pc) pc.onclick=(e)=>{ e.stopPropagation(); toggle("dl-png-menu"); };
  if(vc) vc.onclick=(e)=>{ e.stopPropagation(); toggle("dl-video-menu"); };
  document.addEventListener("click", ()=> document.querySelectorAll(".export-menu.open").forEach(x=>x.classList.remove("open")));
})();

// Canvas (editor window) background follows the theme: WHITE by day, a soft GREY by night. We only
// auto-switch when the background is still at the OTHER theme's default — a custom colour the user picked
// is left untouched (and a transparent background stays transparent).
const THEME_BG = { light:"#ffffff", dark:"#d4d7dc" };
function syncThemeBg(){
  if(model.background.transparent) return false;
  const dark = document.documentElement.getAttribute("data-theme")!=="light";
  const want = dark ? THEME_BG.dark : THEME_BG.light;
  const other = dark ? THEME_BG.light : THEME_BG.dark;
  const cur = (model.background.color||"").toLowerCase();
  if(!cur || cur===other.toLowerCase()){ model.background.color=want; return true; }   // still a default -> follow theme
  return false;
}
// Repaint ONLY the backdrop colour (no scene rebuild) — instant theme/bg-colour switching. Falls back
// to a full renderPreview if the fast path isn't wired yet.
function repaintBg(){
  if(!bgFn) return false;
  const bg = model.background.transparent ? null : hexToRgb(model.background.color);
  try{ bgFn(JSON.stringify(bg)); }catch(e){ return false; }
  return true;
}

// Day/night theme switch (day is the default). The saved theme is applied before paint by a tiny
// inline script in the <head>; here we wire the toggle button and keep its icon in sync.
(function themeToggle(){
  const btn=$("theme-toggle"); if(!btn) return;
  btn.onclick=()=>{
    const light=document.documentElement.getAttribute("data-theme")==="light";
    if(light) document.documentElement.removeAttribute("data-theme");
    else document.documentElement.setAttribute("data-theme","light");
    try{ localStorage.setItem("animate-theme", light?"dark":"light"); }catch(e){}
    syncThemeBg();                                   // canvas bg: white by day, grey by night
    if(!repaintBg()) renderPreview();                // INSTANT recolour (no rebuild); fallback = full render
    saveLocal();
  };
})();

boot().catch(e=>{ console.error(e); setStatus("Fehler: " + e.message); });

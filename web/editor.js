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
const CATALOG = {
  "Shapes": {
    Circle:    { center:[0,0,0], radius:1.0, color:"#59a0eb", fill_color:"#59a0eb", fill_opacity:0.5, stroke_width:4, show_center:false },
    Dot:       { center:[0,0,0], radius:0.08, color:"#111111", stroke_width:4, show_center:false },
    Line:      { start:[-1,0,0], end:[1,0,0], color:"#111111", stroke_width:4, show_center:false },
    Rectangle: { center:[0,0,0], width:2.0, height:1.0, color:"#111111", fill_color:"#111111", fill_opacity:0.5, stroke_width:4, show_center:false },
    Square:    { center:[0,0,0], side:1.0, color:"#111111", fill_color:"#111111", fill_opacity:0.5, stroke_width:4, show_center:false },
    Vector:    { end:[2,1,0], start:[0,0,0], color:"#111111", stroke_width:4 },   // 2D & 3D
  },
  "Axes & Graphs": {
    // One coordinate system, always 3D-capable: the z-axis is hidden in 2D view and appears when
    // you orbit into 3D. Fixed on-screen size (x/y/z_length); the range only rescales.
    Axes:          { x_range:[-6,6], y_range:[-3,3], z_range:[-3,3], x_length:12, y_length:6, z_length:6 },
    FunctionGraph: { func:"sin(x)", x_range:[-4,4], resolution:50, color:"#59a0eb", stroke_width:4, stroke_opacity:0.5 },
  },
  "Signals (ET3)": {   // presets: same FunctionGraph type, different standard signal (t = variable)
    "ε(t) step":      { _type:"FunctionGraph", func:"epsilon(t)", x_range:[-4,4], color:"#59a0eb", stroke_width:4 },
    "rect(t)":        { _type:"FunctionGraph", func:"rect(t)", x_range:[-4,4], color:"#59a0eb", stroke_width:4 },
    "tri(t)":         { _type:"FunctionGraph", func:"tri(t)", x_range:[-4,4], color:"#59a0eb", stroke_width:4 },
    "si(t)=sin t / t":{ _type:"FunctionGraph", func:"si(t)", x_range:[-12,12], color:"#59a0eb", stroke_width:4 },
    "sinc(t)":        { _type:"FunctionGraph", func:"sinc(t)", x_range:[-6,6], color:"#59a0eb", stroke_width:4 },
    "ramp(t)":        { _type:"FunctionGraph", func:"ramp(t)", x_range:[-4,4], color:"#59a0eb", stroke_width:4 },
  },
  "3D (set view to 3D)": {   // Surface uses the axes; solids live in world coordinates
    Surface:    { func:"sin(x)*cos(y)", resolution:18, color:"#59a0eb", fill_opacity:1.0 },
    Sphere:     { radius:1.0, center:[0,0,0], resolution:10, color:"#59a0eb", fill_opacity:0.5 },
    Box:        { width:1.5, height:1.0, depth:1.0, center:[0,0,0], color:"#59a0eb", fill_opacity:0.5 },
    Cube:       { side:1.2, center:[0,0,0], color:"#59a0eb", fill_opacity:0.5 },
    Pyramid:    { base:1.5, height:2.0, center:[0,0,0], color:"#59a0eb", fill_opacity:0.5 },
  },
  "Text": {
    Text: { text:"Text", position:[0,0,0], font_size:40, color:"#111111" },
  },
  "LaTeX": {   // real LaTeX, typeset by MathJax -> vector glyphs (VMobjects) in the scene graph
    MathTex: { tex:"\\frac{a}{b}", height:1.2, position:[0,0,0], color:"#111111" },
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
      { key:"g", type:"FunctionGraph", props:{ func:"sin(x)", x_range:[-6,6], color:"#59a0eb", stroke_width:4 } },
    ],
    animations: [{ type:"Create", targetKey:"g", run_time:2.0 }],
  },
  "Parabola + point": {
    objects: [
      { type:"Axes", props:{ x_range:[-3,3], y_range:[-1,5], x_length:10, y_length:6 } },
      { type:"FunctionGraph", props:{ func:"x**2", x_range:[-3,3], color:"#59a0eb", stroke_width:4 } },
      { key:"p", type:"Dot", props:{ center:[1,1,0], radius:0.1, color:"#e03a2f", stroke_width:4, show_center:false } },
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
      { type:"Circle", props:{ center:[0,0,0], radius:1.0, color:"#59a0eb", fill_color:"#59a0eb", fill_opacity:0.15, stroke_width:5, show_center:true } },
    ],
  },
  "Surface z=f(x,y) (3D)": {
    camera: { mode:"3d", theta:0.6, phi:1.0 },
    objects: [
      { type:"Axes", props:{ x_range:[-3,3], y_range:[-3,3], z_range:[-1.5,1.5], x_length:8, y_length:8, z_length:5 } },
      { type:"Surface", props:{ func:"sin(x)*cos(y)", resolution:22, color:"#59a0eb", fill_opacity:1.0 } },
    ],
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

// Computations = OPERATIONS over objects, shown as animated processes. Each references existing
// objects as operands (type-checked). Categorised by subject -> topic.
const SHAPE_TYPES = ["Circle", "Rectangle", "Square", "Triangle", "Polygon"];
const COMPUTATIONS = {
  "Math — Functions": {
    "Convolution  (f ∗ g)": { type:"Convolution", inputs:[{role:"f",label:"Function f",accept:["FunctionGraph"]},{role:"g",label:"Function g",accept:["FunctionGraph"]}], props:{ run_time:6, tau_range:[-5,5], color:"#e03a2f", stroke_width:5 } },
    "Product  (f · g)":     { type:"Product",     inputs:[{role:"f",label:"f",accept:["FunctionGraph"]},{role:"g",label:"g",accept:["FunctionGraph"]}], props:{ color:"#8b2fd6", stroke_width:4 } },
    "Sum  (f + g)":         { type:"Sum",         inputs:[{role:"f",label:"f",accept:["FunctionGraph"]},{role:"g",label:"g",accept:["FunctionGraph"]}], props:{ color:"#8b2fd6", stroke_width:4 } },
    "Difference  (f − g)":  { type:"Difference",  inputs:[{role:"f",label:"f",accept:["FunctionGraph"]},{role:"g",label:"g",accept:["FunctionGraph"]}], props:{ color:"#8b2fd6", stroke_width:4 } },
  },
  "Geometry": {
    "Intersection  (A ∩ B)":{ type:"Intersection", inputs:[{role:"a",label:"Shape A",accept:SHAPE_TYPES},{role:"b",label:"Shape B",accept:SHAPE_TYPES}], props:{ color:"#8b2fd6", fill_color:"#8b2fd6", fill_opacity:0.55, stroke_width:3 }, result:[{key:"area",prefix:"Intersection area = "}] },
  },
  "Arithmetic — numbers (kids)": {   // operate on typed-in numbers; shown as squares or on a number line
    "Addition  (a + b)":       { type:"Addition",       kind:"numbers", numbers:[10,4], props:{ run_time:4, mode:"squares" } },
    "Subtraction  (a − b)":    { type:"Subtraction",    kind:"numbers", numbers:[10,4], props:{ run_time:4, mode:"squares" } },
    "Multiplication  (a × b)": { type:"Multiplication", kind:"numbers", numbers:[3,4],  props:{ run_time:4, mode:"squares" } },
    "Division  (a ÷ b)":       { type:"Division",       kind:"numbers", numbers:[12,3], props:{ run_time:4, mode:"squares" } },
  },
  "Series — sums (Σ)": {   // Σ over an index i, from i=start to i=end (a number, or symbolic 'n')
    "Summation  (Σ)": { type:"Summation", kind:"summation",
      props:{ sum_mode:"number", term:"1/i^2", from:1, to:"n", show_terms:3, run_time:5, color:"#e03a2f" } },
  },
};
const COMP_DEFS = {};
for (const grp of Object.values(COMPUTATIONS)) for (const [name, def] of Object.entries(grp)) COMP_DEFS[def.type] = { ...def, name };

const BG_ID = "__bg__";
const $ = (id) => document.getElementById(id);
const setStatus = (m) => { $("status").textContent = m; };

let renderModel = null, pickFn = null, preparePlay = null, playFrame = null;
let playing = false, playStart = 0, playDuration = 0, rafId = null;
const ANIM_TYPES = ["Create", "FadeIn", "GrowFromCenter", "Shift"];
const model = { objects: [], animations: [], computations: [], background: { color:"#ffffff", transparent:false, shadows:true }, selectedId: null, selectedComp: null, playMode: "sequential", angleUnit: "rad", domain: "real", camera: { mode:"2d", theta:0.6, phi:1.0, zoom:1.0 } };
let nextId = 1, nextAnimId = 1, nextCompId = 1;
let clipboard = null;                 // last copied object spec {type, props}, for paste/duplicate
let orbitFn = null;                   // fast 3D re-aim (set after Pyodide boot)
let zoomFn = null;                    // fast zoom repaint (set after Pyodide boot)

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
  const animations = model.animations.map((a,i)=>({
    type:a.type, target:a.target, run_time:a.run_time,
    step: model.playMode==="parallel" ? 0 : i,
    args: a.type==="Shift" ? { vector:a.vector } : {},
  }));
  const computations = model.computations.map(c=>{
    const def = COMP_DEFS[c.type];
    const spec = { id:c.id, type:c.type, props:toArgs(c.props) };
    if(c.visible===false) spec.visible = false;
    if(def && def.kind==="numbers"){
      spec.numbers = c.numbers;
    } else if(def && def.kind==="summation"){
      // number mode: resolve the ground-state LaTeX -> MathJax glyph data for a real vector Σ
      if((c.props.sum_mode||"number")!=="function"){
        const g = ensureGlyphs(_groundLatex(sumStages(c)));
        spec.props = { ...spec.props, glyphs: g || [] };
      }
    } else {
      spec.inputs = c.inputs;
      if(c.children && c.children.length) spec.children = c.children.map(objToSpec);
    }
    return spec;
  });
  injectTexGlyphs(objects);                   // MathTex: resolve `tex` -> glyph data (async, cached)
  return { objects, animations, computations, background: bg, shadows: !!model.background.shadows,
           angle_unit: model.angleUnit, domain: model.domain, camera: model.camera };
}

// ---------- 3D level-of-detail (LOD) ----------
// Our renderer is a CPU painter (no GPU z-buffer), like matplotlib's mplot3d. Beyond ~2500 faces the
// per-quad Canvas draw calls make an orbit drag stutter. So, like GeoGebra/CAD tools, we render at
// REDUCED detail WHILE rotating and snap back to full detail on release. Only surfaces/solids with a
// resolution above the cap are heavy enough to bother.
const ORBIT_DETAIL_CAP = 40;
function _hasY(f){ return /(^|[^A-Za-z0-9_])y([^A-Za-z0-9_]|$)/.test(String(f||"")); }
function needsLOD(){
  let hit=false;
  const scan=(o)=>{
    const r=o&&o.props&&o.props.resolution;
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
      if(k==="resolution" && typeof x[k]==="number" && x[k]>ORBIT_DETAIL_CAP) x[k]=ORBIT_DETAIL_CAP;
      else _capResolution(x[k]);
    }
  }
}
function lowDetailModelJson(){ const m=toPythonModel(); _capResolution(m); return JSON.stringify(m); }

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
  (function step(now){
    let a=(now-start)/T; if(a>1) a=1;
    const e=a<.5 ? 2*a*a : 1-Math.pow(-2*a+2,2)/2;                   // easeInOutQuad
    model.camera.theta=t0+dT*e; model.camera.phi=p0+dP*e;
    if(orbitFn) orbitFn(model.camera.theta, model.camera.phi);
    drawViewCube();
    if(a<1) requestAnimationFrame(step); else renderPreview();      // final full-detail frame
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
function addObject(type, defaults){
  const id = "o"+(nextId++);
  model.objects.push({ id, type, props: structuredClone(defaults) });
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
function selectObject(id){ model.selectedId = id; model.selectedComp = null; renderSceneObjs(); renderComputations(); renderProps(); }

// ---------- computations (operations over objects) ----------
function addComputation(def){
  const c = { id:"k"+(nextCompId++), type:def.type, props:structuredClone(def.props||{}) };
  if(def.kind==="numbers"){
    c.numbers = (def.numbers||[2,2]).slice();           // number operands (typed in), not object refs
  } else if(def.kind==="summation"){
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
  const copy = cloneSpec(list[i]);                             // all properties + children come along
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
  model.animations.push(a);
  renderProps(); renderPreview();
}
function deleteAnimation(id){ model.animations = model.animations.filter(a=>a.id!==id); renderProps(); renderPreview(); }

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
  model.background = m.background || { color:"#ffffff", transparent:false };
  model.playMode = m.playMode || "sequential";
  model.angleUnit = m.angleUnit || "rad";
  model.domain = m.domain || "real";
  model.camera = m.camera || { mode:"2d", theta:0.6, phi:1.0 };
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
function buildTemplates(){
  const sel=$("templates"); sel.innerHTML="";
  const ph=document.createElement("option"); ph.value=""; ph.textContent="— choose template —"; sel.appendChild(ph);
  for(const name of Object.keys(TEMPLATES)){ const o=document.createElement("option"); o.value=name; o.textContent=name; sel.appendChild(o); }
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
  if(def.kind==="summation") return true;                 // no object operands; always runnable
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
  } else if(def.kind==="summation"){
    const sel=document.createElement("select");
    for(const [val,txt] of [["number","Number series  Σ aᵢ"],["function","Function partial sum (Fourier)"]]){ const o=document.createElement("option"); o.value=val; o.textContent=txt; sel.appendChild(o); }
    sel.value=c.props.sum_mode||"number"; sel.onchange=()=>{ c.props.sum_mode=sel.value; renderPreview(); };
    container.appendChild(propRow("Mode", sel));
    const hint=document.createElement("div"); hint.className="hint";
    hint.textContent = "Index i; upper limit 'to' may be a number or 'n' (symbolic). Term uses i (function mode: i and x).";
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
    inp.oninput=()=>{ c.numbers[i]=parseInt(inp.value||"0",10)||0; renderPreview(); }; commitOnEnter(inp);
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
  bgRow.textContent="Background"; bgRow.onclick=()=>selectObject(BG_ID);              // whole row
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
}
function commitOnEnter(i){ i.addEventListener("keydown",(e)=>{ if(e.key==="Enter"){ e.preventDefault(); i.blur(); } }); }  // Enter = accept value + leave field
function numberInput(value, on){ const i=document.createElement("input"); i.type="number"; i.step="0.1"; i.value=value; i.oninput=()=>on(parseFloat(i.value)); commitOnEnter(i); return i; }
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
  const i=document.createElement("input"); i.type="text"; i.value=val; i.oninput=()=>{ obj.props[key]=i.value; renderPreview(); }; return propRow(key,i);
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
    const h=document.createElement("div"); h.style="font-weight:600;margin-bottom:6px"; h.textContent="Background"; el.appendChild(h);
    const ti=document.createElement("input"); ti.type="checkbox"; ti.checked=model.background.transparent;
    ti.onchange=()=>{ model.background.transparent=ti.checked; renderPreview(); };
    const ci=document.createElement("input"); ci.type="color"; ci.value=model.background.color;
    // no renderProps() here -> the colour dialog stays open, the picker circle can be moved freely
    ci.oninput=()=>{ model.background.color=ci.value; if(model.background.transparent){ model.background.transparent=false; ti.checked=false; } renderPreview(); };
    const si=document.createElement("input"); si.type="checkbox"; si.checked=!!model.background.shadows;
    si.onchange=()=>{ model.background.shadows=si.checked; renderPreview(); };
    el.appendChild(propRow("color", ci));
    el.appendChild(propRow("transparent", ti));
    el.appendChild(propRow("shadows (3D surface shading)", si));
    return;
  }
  const o=selected();
  if(!o){ el.innerHTML='<span class="hint">No object selected.</span>'; return; }
  const h=document.createElement("div"); h.style="font-weight:600;margin-bottom:6px"; h.textContent=o.type; el.appendChild(h);
  for(const [k,v] of Object.entries(o.props)) el.appendChild(propInput(o,k,v));   // visibility: eye icon in the list
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
    if(a.type==="Shift"){
      const vr=document.createElement("div"); vr.className="prop";
      const vl=document.createElement("label"); vl.textContent="vector"; vr.appendChild(vl);
      const vec=document.createElement("div"); vec.className="vec";
      a.vector.forEach((comp,i)=> vec.appendChild(numberInput(comp, (x)=>{ a.vector[i]=x; renderPreview(); })));
      vr.appendChild(vec); wrap.appendChild(vr);
    }
  }
  const adder=document.createElement("div"); adder.style="margin-top:6px";
  for(const t of ANIM_TYPES){ const b=document.createElement("span"); b.className="palette-item"; b.textContent="+ "+t; b.onclick=()=>addAnimation(t); adder.appendChild(b); }
  wrap.appendChild(adder); container.appendChild(wrap);
}

// ---------- Σ summation: real LaTeX via KaTeX, revealed step by step over the play clock ----------
// A canvas cannot match LaTeX typesetting, so the summation's typography is rendered by KaTeX as an
// overlay above the canvas (the Python engine only reserves the play duration for number mode, and
// draws the partial-sum curve for function mode).
function _substI(src, rep){ return String(src).replace(/(?<![A-Za-z0-9_])i(?![A-Za-z0-9_])/g, rep); }

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
function _fmtNum(v){ if(!isFinite(v)) return "?"; return String(+v.toPrecision(5)); }

function sumStages(c){                       // ordered LaTeX strings revealed one by one
  const p=c.props||{}, a=parseInt(p.from)||0, endRaw=String(p.to==null?"n":p.to).trim();
  const endNum=/^-?\d+$/.test(endRaw)?parseInt(endRaw):null, symbolic=endNum===null;
  const B=symbolic?(endRaw||"n"):String(endNum), k=Math.max(1,parseInt(p.show_terms)||3), term=p.term||"";
  const head="\\sum_{i="+a+"}^{"+B+"} "+exprToLatex(term);
  let entries=[];
  if(symbolic){ for(let i=a;i<a+k;i++) entries.push({t:"num",i}); entries.push({t:"ell"}); entries.push({t:"sym",lab:B+"-1"}); entries.push({t:"sym",lab:B}); }
  else { const b=endNum; if(b-a+1<=k+2){ for(let i=a;i<=b;i++) entries.push({t:"num",i}); }
    else { for(let i=a;i<a+k;i++) entries.push({t:"num",i}); entries.push({t:"ell"}); entries.push({t:"num",i:b-1}); entries.push({t:"num",i:b}); } }
  const ev=evalExprJS(term), stages=[head], resolved=[];   // leading terms are numeric even when the limit is 'n'
  for(const e of entries){
    if(e.t==="ell"){ resolved.push("\\cdots"); stages.push(head+" = "+resolved.join(" + ")); continue; }
    if(e.t==="sym"){ const sub=exprToLatex(_substI(term,"("+e.lab+")")); stages.push(head+" = "+resolved.concat([sub]).join(" + ")); resolved.push(sub); continue; }
    const sub=exprToLatex(_substI(term,String(e.i)));
    stages.push(head+" = "+resolved.concat([sub]).join(" + "));
    const v=_fmtNum(ev(e.i)); stages.push(head+" = "+resolved.concat([v]).join(" + ")); resolved.push(v);
  }
  if(!symbolic){ let tot=0; for(let i=a;i<=endNum;i++){ const vv=ev(i); if(isFinite(vv)) tot+=vv; } stages.push(head+" = "+resolved.join(" + ")+" = "+_fmtNum(tot)); }
  return { stages, head, color:p.color||"#e03a2f", mode:p.sum_mode||"number" };
}
function activeSum(){ return (model.computations||[]).find(c=>c.type==="Summation" && c.visible!==false) || null; }
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
  // number mode: once the vector glyphs are ready, the engine draws it -> hide the fallback overlay
  if(!isFn && (latex in _texCache)){ el.style.display="none"; el.innerHTML=""; el.dataset.key=""; return; }
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
async function texToGlyphs(latex){
  if(!window.MathJax || !MathJax.tex2svg) return [];
  try { await MathJax.startup.promise; } catch(e){}
  const node = MathJax.tex2svg(String(latex||""), {display:true});
  const svg = node.querySelector("svg");
  if(!svg) return [];
  const holder = document.createElement("div");
  holder.style.cssText = "position:absolute;left:-99999px;top:0;visibility:hidden";
  holder.appendChild(svg); document.body.appendChild(holder);   // must be in the DOM for getCTM()
  const glyphs = [];
  const mat = (el)=>{ const m=el.getCTM(); return m ? [m.a,m.b,m.c,m.d,m.e,m.f] : [1,0,0,1,0,0]; };
  try {
    svg.querySelectorAll("path").forEach(p=>{ const d=p.getAttribute("d"); if(d) glyphs.push({d, m:mat(p), c:p.getAttribute("data-c")||""}); });
    svg.querySelectorAll("rect").forEach(r=>{  // fraction bars / sqrt lines -> a rectangle path
      const x=+r.getAttribute("x")||0, y=+r.getAttribute("y")||0, w=+r.getAttribute("width")||0, h=+r.getAttribute("height")||0;
      if(w>0 && h>0) glyphs.push({d:`M${x} ${y} h${w} v${h} h${-w} Z`, m:mat(r), c:""});
    });
  } catch(e){}
  document.body.removeChild(holder);
  return glyphs;
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
  // Canvas interaction: in 3D, drag = orbit the camera (fast repaint); a click without dragging
  // selects (pick). In 2D, a click selects. The mouse wheel zooms in/out in both modes.
  const VC_LIMIT = Math.PI/2 - 0.03;        // vertical orbit limit (both above and below the plane)
  let dragging=false, moved=false, sx=0, sy=0, th0=0, ph0=0, lodOn=false;
  const pxy=(e)=>{ const r=canvas.getBoundingClientRect(); return [(e.clientX-r.left)/r.width*canvas.width, (e.clientY-r.top)/r.height*canvas.height]; };
  canvas.onpointerdown = (e)=>{
    sx=e.clientX; sy=e.clientY; moved=false; lodOn=false;
    if(model.camera.mode==="3d"){ dragging=true; th0=model.camera.theta; ph0=model.camera.phi; canvas.setPointerCapture(e.pointerId); }
  };
  canvas.onpointermove = (e)=>{
    if(!dragging) return;
    const dx=e.clientX-sx, dy=e.clientY-sy;
    if(Math.abs(dx)+Math.abs(dy)>3) moved=true;
    if(moved && !lodOn){                       // first real movement: drop to low detail ONCE (smooth orbit)
      lodOn=true;
      if(renderModel && needsLOD()){ try{ renderModel(lowDetailModelJson()); }catch(_){} }
    }
    model.camera.theta = th0 - dx*0.01;
    // phi = elevation above the ground plane: 0 = horizon (side view), +/-pi/2 = straight down/up.
    // Direct-manipulation feel: dragging UP tilts the camera DOWN (grab-and-pull), hence + dy.
    model.camera.phi = Math.max(-VC_LIMIT, Math.min(VC_LIMIT, ph0 + dy*0.01));
    if(orbitFn) orbitFn(model.camera.theta, model.camera.phi);      // re-aim only, no rebuild
    drawViewCube();
  };
  canvas.onpointerup = (e)=>{
    if(dragging){ dragging=false; if(moved){ renderPreview(); return; } }   // sync full render after orbit
    if(!pickFn) return;                                                      // otherwise it was a click -> pick
    const [px,py]=pxy(e); const id=String(pickFn(px,py)); if(id) selectObject(id);
  };
  // Mouse-wheel zoom: scale camera.zoom about 1.0, fast-repaint while scrolling, full render on settle.
  let _zoomTimer=null;
  canvas.onwheel = (e)=>{
    if(playing) return;
    e.preventDefault();
    const f = Math.exp(-e.deltaY * 0.0015);                 // smooth multiplicative zoom
    model.camera.zoom = Math.max(0.2, Math.min(8, (model.camera.zoom||1) * f));
    if(zoomFn) zoomFn(model.camera.zoom);                   // fast repaint (no rebuild)
    clearTimeout(_zoomTimer); _zoomTimer=setTimeout(()=>{ renderPreview(); saveLocal(); }, 180);
  };
  initViewCube();
  setStatus("Ready ✓ — add an element on the left, or click in the view.");
  let restored=false;                  // restore the autosaved scene, else start with an axes
  try{ const raw=localStorage.getItem(LS_KEY); if(raw){ const data=JSON.parse(raw); if(data && data.model && (data.model.objects||[]).length){ applyScene(data); restored=true; } } }catch(e){}
  if(!restored) addObject("Axes", CATALOG["Axes & Graphs"].Axes);
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
  else if(mod && e.key==="v"){ if(clipboard){ const copy=cloneSpec(clipboard); model.objects.push(copy); model.selectedId=copy.id; renderSceneObjs(); renderProps(); renderPreview(); } }
});

$("dl-png").onclick = () => {
  $("view").toBlob((blob)=>{ const a=document.createElement("a"); a.href=URL.createObjectURL(blob); a.download="scene.png"; a.click(); URL.revokeObjectURL(a.href); });
};

boot().catch(e=>{ console.error(e); setStatus("Fehler: " + e.message); });

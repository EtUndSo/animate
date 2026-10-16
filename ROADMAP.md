# Roadmap

## Done
- [x] Engine core (Bézier objects, transforms, groups) — shared design in both projects
- [x] Local project (Cairo + ffmpeg): shapes, Axes + graphs, Text, animations, image/video export
- [x] Animations: `Create`, `FadeIn`, `Shift`, `GrowFromCenter`, `Refine` (1→n, e.g. Riemann)
- [x] Declarative **scene model** + interpreter + codegen (editor ↔ code bridge)
- [x] **Camera** abstraction (3D-ready: projection is the only place that is 2D)
- [x] Renderer split into backend-agnostic core + painters (Cairo / Canvas)
- [x] **Batch 1 — Web:** Pyodide loads the engine, renders "Hello Sine" via Canvas ✓

## Web (building toward the editor app)
- [x] **Batch 2** — Full scenes **and animation** in the browser (real-time Canvas player): timeline + seek (scrubbable) verified; browser playback to confirm
- [x] **Batch 3** — Editor UI: palette + click-to-add + property forms + **live preview** + PNG download + **click-on-canvas to select** + **background (colour / transparent)** + debounced rendering
  - [x] **Fixed-size axes + dynamic ticks** — x_length/y_length are the on-screen size; range only rescales; tick step auto-chosen (`_nice_step`). Objects are placed in the axes' DATA coords (`Axes.place`), so center=(1,0) sits on tick "1" at any range.
  - [x] **Per-object style** — `stroke_width` (pen thickness) on all shapes; separate **fill_color** vs outline `color` (equal on creation); **show_center** dot (positioning aid, render-only).
  - [x] **Batch 3c** — assign animations to objects in the editor (Create/FadeIn/GrowFromCenter/Shift + timing) + ▶ play in preview
  - [x] **Templates box** — ready scenes (Leere Achse, Sinus-Create, Parabel+Punkt, Riemann, Einheitskreis); `Riemann` now exists in the declarative model
  - [x] **Sequential / simultaneous animations** — engine groups animations into STEPS (same step = one `play()` = together; ascending steps = sequence); each animation keeps its own run_time within a step (`seek` on per-anim clock). Editor: global "Animationen: nacheinander / gleichzeitig" toggle above ▶.
  - [x] **Duplicate / copy-paste objects** — ⧉ button per scene row + Ctrl/Cmd+C/V; clones all properties (incl. children).
  - [x] **Object tree + result children** — scene box is a tree: objects expand to show their child/result objects; each child is fully configurable (shown?, position, size, colour — same props as shapes) + per-object "angezeigt" (visible) toggle. Interpreter builds children as sub-objects and honours visibility. First computed result wired: `Riemann` exposes its **area** as a `DecimalNumber` child.
  - [x] **Result registry (static scalar results)** — `engine/results.py` `RESULTS[type][key]→compute`; `result`-tagged DecimalNumber child shows "symbol = formula = value" (e.g. `A = πr² = 3.14`); editor "Ergebnisse" section (checkboxes) adds/removes them, auto-placed near the object. Done: Circle, Rectangle, Square, Line, FunctionGraph (integral), Riemann (area, error). Replaces the hard-coded Riemann→area. See **RESULTS.md**.
    - [ ] **next:** geometric results (roots/extrema → Dots, midpoint/center → Dot), dynamic (animation-driven) results, and the abstract (symbol-only) display mode.
  - [x] **Smooth graphs** — `smooth_points` (Catmull-Rom → Bézier) for `axes.plot` / `FunctionGraph`: handles from the local tangent, so curves like sin(3x) are smooth, not straight-segment polylines.
  - [x] **Eye toggle per object** — 👁 / 👁-off icon in every scene row toggles visibility (editor + result); replaces the visibility checkbox.
  - [x] **GeoGebra-grade plotting** (`engine/plotting.py` `plot_graph`) — combined (uniform+adaptive) sampling à la GeoGebra's CurvePlotter (ref: Bayer 2018, "Efficient plotting … combined sampling"): recursive subdivision with a **5° bend-angle** criterion (dense in curvature, sparse on straights), a **uniform seed phase** (d_min), **randomised split points** r∈[0.45,0.55] (seeded by x-range → reproducible) that break periodic aliasing — so sin(1000x) is densely/honestly drawn, never a fake slow wave — and **discontinuity splitting** at poles/NaN (tan is cut into pieces, no vertical line across the asymptote). Open paths → Create draws L→R. Replaced fixed/adaptive point sampling and the min/max band (both had issues). Correctness is the #1 project rule.
  - [x] **Angle unit (Bogenmaß/Grad)** — selector bottom-right of the preview; `_ANGLE_UNIT` makes trig in user expressions degree-aware.
  - [x] **GeoGebra-style input** — `normalize_expr`: `^`→`**`, implicit multiplication (`3x`, `2sin(x)`, `x(x+1)`, `(x+1)(x-1)`, `2pi`) while keeping function calls intact.
  - [x] **Cache-bust** engine `.py` fetches (`?v=BUILD`) so a stale cached file can't break a newer editor.js. Wider preview canvas (1.5×).
  - [ ] **Batch 3b** — drag-and-drop from palette, grid + snap to integers
  - [ ] **More templates** — Faltung (convolution), area-between-curves, phasor, sampling … (blocked on the computation layer + ValueTracker below)
  - [ ] **LaTeX object** (`Tex`) — renders math via **KaTeX** (web) / mathtext (local); behaves like Text
  - [x] **3D view + 3D objects** — orbit camera (Manim-style spherical θ/φ, θ=φ=0 ≡ 2D view) in `camera.py`; renderer depth-sorts faces (painter's algorithm) in 3D. Objects (`threed.py`): `Sphere`, `Box`, `Cube`, `Pyramid`, `Vector` (2D+3D arrow). Editor: **View 2D/3D** toggle, **drag = orbit** (fast re-aim via `orbit()` without rebuild).
  - [x] **Unified axes (always 3D) + clean surfaces** — ONE `Axes` (no separate ThreeDAxes): x/y with ticks+numbers+labels, **plus a z-axis** built the same way, tagged `_only_3d` so it is hidden in 2D view and appears (labelled) when you orbit. `coords_to_point(x,y,z)` scales z from the plane. **`axes.plot_surface`** draws z=f(x,y) through the axes (scaled) with **Lambert shading** per face (matplotlib/GeoGebra-style: painter's algorithm + per-normal lighting) so the form reads. Solids stay in world coords (`_WORLD_TYPES`, not axis-placed). Templates use the unified Axes.
    - [ ] **next 3D:** perspective + zoom, height colormap, 3D grid, cone/cylinder, Create/Transform for solids.
  - [x] **Robust against dangling references** — a deleted object no longer blanks the editor: the interpreter skips animations whose target is gone; deleting an object also drops animations targeting it and clears operand references.

- [~] **Computation layer — computations are OPERATIONS over objects, shown as ANIMATED PROCESSES (not just numbers).**
  - [x] **Architecture:** computations are a separate model list (`model.computations`), each referencing existing objects as **operands** (type-checked), with its own **editor box** ("Berechnungen" list + categorised "Berechnung hinzufügen" by subject→topic) and a **config panel** (pick operand objects via type-filtered dropdowns, tune params incl. animation `run_time`). Interpreter `_run_computation` validates + dispatches; unconfigured = dead (drawn as nothing). `FunctionGraph` stashes `_func_expr` so function ops read it.
  - [x] **Animated convolution** (`engine/processes.py`): slides g(t−τ) across f (entering from the far left), fills the overlap product, and **traces the result curve** (f∗g)(t) with a live value — ValueTracker on the timeline, speed = `run_time`, operand colours reused. **Edit vs play:** operands an animated operator consumes (`_COMP_CONSUMES`) are shown statically in the edit view but **taken over** by the operator while playing (`ModelScene.animating`); the edit view shows the finished result curve instead.
  - [x] **Transport controls** — ⏮ Reset (back to the static edit view, all objects as inserted), ▶ Play (runs once to the end), ⏸ Pause, ⏭ End (jump to final frame). Non-looping. Fixed: ▶ now always starts from 0 (unless resuming a pause) — a leftover playT no longer made a replay start near the end.
  - [x] **Eye toggle on operations too** — each operation in the list has the 👁 show/hide icon (hidden operations aren't run; their consumed operands then show statically).
  - [x] Convolution g now slides fully across: in from −∞ (left) **and out to +∞** (off the right).
  - [x] Multiplication (squares) redesigned: a groups of b appear one after another (different colours), move together into one group (like +), then take one colour.
  - [x] **Geometry intersection** (`engine/geometry.py`): Sutherland–Hodgman (exact for convex) + shoelace **area** result child (verified vs the lens formula). Template "Schnitt zweier Kreise".
  - [x] **Function ops** `Product`/`Sum`/`Difference` (static for now).
  - [x] **Arithmetic number operators (kids)** (`engine/arithmetic.py`) — Addition/Subtraction/Multiplication/Division between TYPED-IN numbers (up to 10 per operator, own editor config — a number list, not object refs). On play the numbers become coloured squares (size ∝ total): **+** merge into one group, **−** sit diagonally then annihilate, **×** arrows from each square grow a second-size group at the tip, **÷** reflow into columns. New "Arithmetic" palette category + `kind:"numbers"` config.
    - [x] **Number-line mode** (Cuisenaire-rod style, ref: Cuisenaire / Mathigon Polypad): a per-operator toggle **Squares / Number line** — numbers become coloured bars on a line; **+** lays them end-to-end (a "train"), **−** overlaps and removes the covered part, **×** repeats the bar, **÷** partitions it into equal segments.
    - [x] **Visual polish**: + recolours all squares to one colour at the end; ÷ colours the columns differently.
  - [x] **Seek correctness (two-pass)** — fixed a fundamental timeline bug: objects animated only in a LATER segment (e.g. squares that annihilate) were left in their end-state when rewound. seek now resets every future animation to its start first (latest-first so the earliest wins), then applies past/current. Fixes subtraction (result shown too early / squares appearing then vanishing) and any multi-step animation.
  - [x] **Convolution result curve correctness & smoothness** — trace now sampled uniformly in x and revealed exactly to the slide position k (was revealed by Bézier parameter on an adaptive curve → raced ahead, showing values before overlap); finer integration (adaptive-quadrature-grade, GeoGebra-style) → no wobble. Verified: rect∗rect = triangle, flat before overlap.
  - **Guiding rule:** EVERY operator gets a thorough, step-by-step animation that genuinely teaches the mechanic (level fits the topic). Research each operator (GeoGebra first, else specialised professional tools) before building.
- [x] **Unified function graph** — a `FunctionGraph` whose expression uses two variables (e.g. `sin(x)*cos(y)`) is automatically drawn as a **surface** (a surface *is* the graph of a function); one variable → curve.
  - [ ] **next:** animate the other processes (summation Σ term-by-term, Riemann refine, intersection sweep, derivative tangent-slide); `Union`/`Difference` geometry via **Greiner–Hormann**; `Integral`/`Derivative` ops.

- [x] **Save / load scenes** — download the scene as `.json` and re-open it; **autosave to the browser** (localStorage) so a scene survives closing the page. (editor.js `saveScene`/`applyScene`/`saveLocal`.)

- [x] **Editor UI reorganised + English** — three colour-coded big boxes: **Add Elements** (Templates / Objects / Operations, groups collapsed by default), **Scene** (objects list + operations list), **Properties** (object props + operation props). Whole UI in English.

- [x] **ET3 standard signals + complex domain** — `epsilon`/`step`/`u` (ε), `rect`, `tri`, `ramp`, `si`, `sinc` in the expression namespace (vectorised), `t` works as the variable, palette group "Signale (ET3)". **Zahlenbereich** selector reell/komplex: `j` = imaginary unit; in complex mode a `FunctionGraph` (e.g. `exp(j*t)`) draws **Re (chosen colour) + Im (orange)**.
  - [ ] **next complex:** complex plane / phasor view, |·| & arg, complex-valued convolution & Fourier.

- [ ] **Process simulations — show as many maths/science procedures as possible, graphically.** Built on the computation layer. Goal: not just function graphs, but *procedures/dynamics*:
  - **Linear algebra (3B1B-style):** matrix · vector, matrix · matrix, basis/grid transformation (animate the plane under A), determinant as signed area, eigenvectors, rotation/shear/projection.
  - **Numerical methods:** Newton's method, Euler/RK integration, Riemann refine (1→n), gradient descent, bisection, fixed-point iteration — step-by-step with the current estimate drawn each step.
  - **More:** vector fields + flow, complex maps, probability/sampling, simple ODE/physics (pendulum, spring), graph/tree algorithms.
  - **DUAL MODE (hard requirement):** every process runs **abstract — only symbols/variables, no numbers** *and* **numeric — with values the user types in**. Same scene, a toggle; the abstract view shows the structure (e.g. A·v with entries a₁₁…, v₁…), the numeric view the concrete result. (Needs the symbolic side of the computation layer + ValueTracker + `Transform`/morphing + Arrow/Grid objects.)

- [ ] **Research: catalogue of simulation processes to build.** This tool makes *simulations*, so first survey what to simulate, then design how each maps onto our engine (objects + updaters + ValueTracker + Transform). Mine 3Blue1Brown's catalogue and go beyond:
  - **3B1B-style:** linear transformations / change of basis, matrix·vector & matrix·matrix, determinant as area, eigenvectors, dot/cross product, vectors; calculus (derivative/slope, integral/area, Taylor series), ε-δ; Fourier series / epicycles, Fourier transform; complex functions & transformations; convolution; probability (Bayes, distributions, central limit); linear-ODE / phase space; neural-network forward pass; grad/div/curl fields.
  - **Beyond:** numerical methods (Newton, Euler/RK, gradient descent, bisection, fixed-point), sampling/aliasing, root locus / Bode / Nyquist (ET3!), pendulum/spring/orbit physics, graph & sorting algorithms, cellular automata.
  - **Output of this batch:** a prioritised list (effort × teaching value, ET3 first) + for each the required engine primitive, feeding concrete templates. Each entry must support the **abstract + numeric dual mode** (see Process simulations).

- [ ] **Batch 4** — View/camera 2D: **pan + zoom** on the canvas (+ "reset view"); preview camera vs. export camera
- [ ] **Batch 5** — Code view (Monaco) + two-way sync model ↔ code (AST), "Editor | Code | Both" tabs
- [ ] **Batch 6** — Render + download (Foto/Video, independent choice) + timeline scrubber
- [ ] **Batch 7** — 3D: perspective camera + **orbit controls** (Three.js/Blender style) + first 3D objects (Sphere, 3D axes)

## Engine features for ET3 content (both projects)
- [x] **ValueTracker + updaters** (web) — `ValueTracker` (invisible number on the timeline), `obj.add_updater(fn)` re-run each frame after `seek` (via `Scene.run_updaters`), `always_redraw(builder)` (rebuild from live state), `ChangeValue` animation, `DecimalNumber` (live on-screen value). Verified: one `ChangeValue` drives dot + number + graph in lockstep. *(code-level for now; editor UI for updaters + mirror to local still open)*
- [ ] Filled area (under / between curves) — convolution, integral, filter bands
- [ ] `Transform` / morphing (needs `align_points` + bézier resampling — `split_cubic`/`partial_bezier` already exist)
- [ ] Arrow / Stem objects (Dirac, sampling, phasors)
- [ ] More easing (ease-in/out, there-and-back), `FadeOut`, `MoveAlongPath`

## Infrastructure
- [x] One repo, two independent projects (`local/` Cairo, `web/` Canvas)
- [ ] GitHub repo + Cloudflare Pages (root dir = `web`) auto-deploy, all-inkl domain via Cloudflare

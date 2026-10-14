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
- [ ] **Batch 2** — Full scenes **and animation** in the browser (real-time Canvas player, not just a static frame)
- [ ] **Batch 3** — Editor UI: object palette (grouped, collapsible) + drag + properties forms + live preview; grid + snap to integers
- [ ] **Batch 4** — View/camera 2D: **pan + zoom** on the canvas (+ "reset view"); preview camera vs. export camera
- [ ] **Batch 5** — Code view (Monaco) + two-way sync model ↔ code (AST), "Editor | Code | Both" tabs
- [ ] **Batch 6** — Render + download (Foto/Video, independent choice) + timeline scrubber
- [ ] **Batch 7** — 3D: perspective camera + **orbit controls** (Three.js/Blender style) + first 3D objects (Sphere, 3D axes)

## Engine features for ET3 content (both projects)
- [ ] **ValueTracker + updaters** (drives convolution, coupled time↔frequency plots) — unlocks the most ET3 animations
- [ ] Filled area (under / between curves) — convolution, integral, filter bands
- [ ] `Transform` / morphing (needs `align_points` + bézier resampling — `split_cubic`/`partial_bezier` already exist)
- [ ] Arrow / Stem objects (Dirac, sampling, phasors)
- [ ] More easing (ease-in/out, there-and-back), `FadeOut`, `MoveAlongPath`

## Infrastructure
- [x] One repo, two independent projects (`local/` Cairo, `web/` Canvas)
- [ ] GitHub repo + Cloudflare Pages (root dir = `web`) auto-deploy, all-inkl domain via Cloudflare

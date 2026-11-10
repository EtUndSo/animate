# Engine Contract — the watertight foundation

The single rule that makes the whole engine safe:

> **The drawable state at time `t` is a PURE function of `t`.**
> It must not depend on which times were visited before, how many times, or in what order.

Everything below exists to guarantee that. The automated proof is `tests/test_contract.py`
(idempotent · path-independent · stepping == jump). **Every new object, animation or operation MUST be
added there and pass** before it is considered done.

## The two phases
1. **Build** (once): `Scene.construct()` creates the objects and records an ordered **timeline** of
   segments `{anims, dur}`. `ModelScene` builds this from the editor's JSON model.
2. **Seek** (per frame): `Scene.seek(t)` sets every object's state for global time `t`. It is the only
   thing the player/renderer calls. It must be a pure, repeatable function of `t`.

## Time steps (when what happens)
- The timeline is an ordered list of **segments**. Segments run **in sequence**; animations **within one
  segment run in parallel**. (`play(a, b)` = one segment, parallel; two `play()` calls = two segments,
  sequential. In the model, animations are grouped by `step`: same step → parallel, ascending → sequence.)
- A segment spanning `[t0, t1)` gives each of its animations progress `α = clamp((t − t0) / run_time, 0, 1)`
  (an animation shorter than the segment simply holds at `α = 1` for the rest).
- `seek(t)` is **two-pass**: first every *future* animation is reset to its start (`α = 0`, latest-first so
  the earliest reset wins), then every *past/current* animation is applied (`α = 1` if finished, else its
  eased `α`). Finally `run_updaters()` settles updater-driven objects.

## The animation contract (what every `Animation` must satisfy)
1. `begin()` is called **once at build time**, in timeline order, and snapshots the start state
   (`self.start = self.target.copy()`). Any **structural** change to the target (adding/replacing
   sub-objects, as `Transform`/`TransformMatchingTex`/`Refine` do) happens **only in `begin()`**.
2. `interpolate(α)` sets the target's state as a **pure function of `α`** reconstructed from that snapshot.
   It must be valid for any `α ∈ [0,1]`, called in any order, any number of times — never read wall-clock,
   never depend on the previous `α`.
3. Appearance animations set `appears = True`; their target is hidden before the segment (the backward
   reset pass sets `α = 0`, which for `Create`/`FadeIn`/`GrowFromCenter` means "not yet there").

## Updaters & ValueTracker
- Updaters run **after** all animations each frame and derive state from `ValueTracker`s (driven by
  `ChangeValue`). An object is **either** animation-driven **or** updater-driven for a given quantity —
  never both (the one that runs last would silently win).

## Operations (computations) are just animations
- A computation director (convolution, Σ, arithmetic, …) only **adds objects and animations/updaters to
  the timeline using the same primitives**. It gets no special timing. Static (edit) view: it draws the
  finished result with no timeline entry. This keeps operations under the exact same contract.

## Labels and draw order (10.11.2026)
- A `Text` has no path to morph. `Transform`/`TransformMatchingTex` between two labels changes the label's **state**
  as a pure function of α (anchor, size, colour lerp; old text fading out for α < ½, the template's text, align, font,
  raw fading in for α ≥ ½); `begin()` only snapshots. The probe `snap()` therefore records a label's text and size.
- `Text.font` ("sans" | "mono") and `Text.raw` are build-time state. Painters receive them as keyword arguments only
  when set (`text.text_style`): `draw_text(..., align, font="mono", raw=True)`. A new painter must accept both.
- `draw_order: "creation"` sorts `objectList` once at the end of `construct()` by the order of the object list. It
  changes only what lies on top, never the timeline, so seek(t) stays pure. Without it (older scenes) an appearing
  object is appended by `play()` and lies on top of everything drawn before.

## Parameters over time (L3, 10.11.2026)
- A model object `Parameter` (`name`, `value`, optional `integer`) is a `ValueTracker`; its value is also the build-time
  constant of every expression that names it (`_PARAMS`). The animation `ChangeValue` (target = the Parameter, args
  `value` = number or expression, `rate` = "smooth" | "linear") moves it as a pure function of α. With `integer` it
  jumps through the whole numbers, each for an equal share of the run time.
- An object whose props name a **moving** parameter (target of a ChangeValue) gets exactly one updater
  (`scene_model._ParamLink`). It is rebuilt from its spec in every frame with the current values, under the scene's
  saved build settings (`_scene_ctx`: language, angle unit, parameter values, …), so another scene built in between
  cannot leak in.
- Purity: `ModelScene.seek(t)` first returns every such object to its build state (`_mirror(obj, base)`: shape AND
  tree), then runs the two passes, then the updaters. While all its parameters stand at their build values the updater
  does nothing (the object is animation-driven). Otherwise it mirrors the fresh build onto the object, keeping the node
  objects (the animated export keys elements by object; missing nodes are added, surplus nodes emptied) and applying
  this frame's visibility factor (FadeIn/FadeOut) and drawing progress (`Create` stores `_create_alpha`).
- Split of roles (the "never both" rule above): the parameter drives the shape, text and tree; FadeIn/FadeOut/Create
  drive visibility and progress. Shift/Rotate/Scale/MoveTo/Indicate/Transform act on such an object only while its
  parameters are at their build values. Axes, MathTex and computations are never rebuilt (a parameter in an Axes range
  or as an operand of a convolution stays at its start value).
- While built under a parameter, a 2D FunctionGraph samples `samples` (default `PARAM_SAMPLES` = 121) evenly spaced
  points (`Axes.plot(samples=…)`, Catmull-Rom), an Area gets a smooth top edge: same point count in every frame.
- `local/engine` is frozen (local/FROZEN.md) and has no ValueTracker; it is not part of this.
- Contract cases: four "L3 …" models in `tests/test_contract.py` plus `l3_checks()` (whole-number shares, number
  format, scene file → `python_model` → engine).

## Adding a new primitive — checklist
- [ ] Geometry lives in `points` (cubic Bézier, `N = 3k+1`); multi-contour glyphs keep contours in one
      leaf via `_contours` (even-odd fill).
- [ ] Structural mutation only in `begin()`; `interpolate(α)` pure in `α`.
- [ ] If it reveals/erases, use opacity or `partial_bezier`/point interpolation — not wall-clock.
- [ ] Add a case to `tests/test_contract.py` and confirm **OK** (idempotent, path-independent, stepping==jump).
- [ ] Keep names Manim-compatible (`Mobject`/`VMobject`, `Create`, `Transform`, …).

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

## Adding a new primitive — checklist
- [ ] Geometry lives in `points` (cubic Bézier, `N = 3k+1`); multi-contour glyphs keep contours in one
      leaf via `_contours` (even-odd fill).
- [ ] Structural mutation only in `begin()`; `interpolate(α)` pure in `α`.
- [ ] If it reveals/erases, use opacity or `partial_bezier`/point interpolation — not wall-clock.
- [ ] Add a case to `tests/test_contract.py` and confirm **OK** (idempotent, path-independent, stepping==jump).
- [ ] Keep names Manim-compatible (`Mobject`/`VMobject`, `Create`, `Transform`, …).

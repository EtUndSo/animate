# Results catalogue — which objects/animations expose which results

The tool is a graphical layer over real maths, so objects (and the animations on them) can expose
**computed results**. A result shows up as a **child object** in the scene tree and is fully
configurable like any shape (shown?, position, size, colour). This file fixes *which* results each
object type offers — because different types admit different meaningful quantities.

## Two kinds of result

- **Static** — depends only on the object; computed once at build time (like `Riemann.area` today).
  Always available for that type. Child is usually a `DecimalNumber`, sometimes a geometric marker
  (`Dot` at a point, `Line` for a length).
- **Dynamic** — depends on an **animation's progress**; recomputed every frame via an updater
  (needs ValueTracker/updater machinery, already built). Only offered when the object actually has
  that animation. Example: *Create* on a graph → the value at the moving draw-front.

## Mechanism (how a result becomes a child)

A result child spec carries a `result` tag so the interpreter knows what to compute:

```json
{ "type": "DecimalNumber", "props": {…}, "result": { "source": "<parentId>", "key": "area" } }
```

- **Registry:** `RESULTS[object_type] = [ ResultDef … ]`, each `ResultDef = { key, label, kind,
  child_type, compute }`.
  - `kind` = `"static"` or `"dynamic"`.
  - `child_type` = default child (`DecimalNumber`, `Dot`, `Line`, …).
  - `compute(parent, ctx)` → a number/point (static), or, for dynamic, a function of the animation
    alpha that an updater calls each frame.
- **Build:** after building a parent, for each of its `result`-tagged children the interpreter runs
  `compute` and either sets the child's value once (static) or attaches an updater (dynamic).
- **Editor:** the properties panel gets a **"Ergebnisse"** section listing the available results for
  the selected object's type (static always; dynamic only if the matching animation is present).
  A checkbox adds/removes the child; once added it is an ordinary, configurable child in the tree.

This generalises today's hard-coded `Riemann → area` into a registry.

## The catalogue (to confirm / adjust)

Labels are the German UI text. "—" = no results for that type.

| Object | key | label | kind | child | value |
|---|---|---|---|---|---|
| **Circle** | `radius` | Radius | static | DecimalNumber | r |
| | `area` | Flächeninhalt | static | DecimalNumber | π·r² |
| | `circumference` | Umfang | static | DecimalNumber | 2π·r |
| | `center` | Mittelpunkt | static | Dot | (x, y) |
| **Rectangle / Square** | `width` / `height` | Breite / Höhe | static | DecimalNumber | w, h |
| | `area` | Flächeninhalt | static | DecimalNumber | w·h |
| | `perimeter` | Umfang | static | DecimalNumber | 2(w+h) |
| | `diagonal` | Diagonale | static | DecimalNumber + Line | √(w²+h²) |
| **Line** | `length` | Länge | static | DecimalNumber | ‖p₂−p₁‖ |
| | `slope` | Steigung | static | DecimalNumber | Δy/Δx |
| | `midpoint` | Mittelpunkt | static | Dot | (p₁+p₂)/2 |
| **FunctionGraph** | `roots` | Nullstellen | static | Dots | x with f(x)=0 (numeric) |
| | `extrema` | Extrema | static | Dots | f′(x)=0 |
| | `integral` | Integral/Fläche | static | DecimalNumber + fill | ∫ f dx over range |
| | `value_at` | Wert bei x | static | DecimalNumber + Dot | f(x₀), user x₀ |
| | `draw_front` | aktueller Wert (Create) | **dynamic** | DecimalNumber + Dot | f(x) at the draw-front |
| **Riemann** | `area` | Fläche (Näherung) | static | DecimalNumber | Σ f(x_c)·dx  *(built)* |
| | `error` | Fehler vs. exakt | static | DecimalNumber | \|Σ − ∫\| |
| **ValueTracker** | `value` | Wert | dynamic | DecimalNumber | current value |
| **Axes / Text / DecimalNumber** | — | — | — | — | — |

### Animation-driven (dynamic) results, by animation

| Animation | on | result | shows |
|---|---|---|---|
| `Create` | FunctionGraph / Line | `draw_front` | value/point at the growing front |
| `GrowFromCenter` | Circle / Rectangle | `live_area`, `live_radius` | size growing with the animation |
| `Shift` | any | `live_position` | current (x, y) while moving |
| `ChangeValue` | ValueTracker | `value` | the number, live *(built)* |

## Open decisions for you

1. Confirm/trim the lists above (e.g. drop `extrema`/`center` if not wanted yet).
2. Numeric vs. abstract: each value also needs an **abstract form** (symbol, e.g. "A = πr²") for the
   abstract display mode — do we show label+symbol+number, or number only, per result? *(ties into the
   Process-simulations dual mode.)*
3. Default placement of a new result child (near the object vs. a fixed corner).

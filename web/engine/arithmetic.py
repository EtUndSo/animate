"""Child-friendly arithmetic between NUMBERS (up to ten per operator), visualised with little
coloured squares OR as coloured bars on a number line (Cuisenaire-rod style; ref: Cuisenaire rods /
Mathigon Polypad). Operations are RECURSIVE over the list of numbers:
  +  the groups join one after another into one big group (then one colour)
  -  each next number is laid on the end of the running result and annihilates it (left to right)
  x  repeated: `res` groups of the next number, merged -> new running product, for each factor
  /  repeated: the running result is partitioned into `d` columns, for each divisor
Convention: a x b = a groups of b (NOT commutative in the picture); a / b = a split into b parts.
"""
import numpy as np

from .simpleShape import Square, Rectangle, Line
from .text import Text
from .animation import FadeIn, FadeOut, Shift, GrowFromCenter, Recolor
from .constants import RIGHT, UP

_PALETTE = [(0.26, 0.52, 0.96), (0.92, 0.26, 0.21), (0.30, 0.69, 0.31), (0.98, 0.60, 0.0),
            (0.61, 0.35, 0.71), (0.0, 0.60, 0.60), (0.85, 0.33, 0.60), (0.55, 0.43, 0.20),
            (0.20, 0.63, 0.79), (0.50, 0.50, 0.50)]


def _size_for(total):
    return float(np.clip(4.0 / np.sqrt(max(total, 1) + 1), 0.16, 0.6))


def _cols(n):
    return max(1, int(np.ceil(np.sqrt(max(n, 1)))))


def _square(center, size, color):
    s = Square(center=np.asarray(center, dtype=float), side=size * 0.82)
    s.fill_color = color
    s.fill_opacity = 1.0
    s.color = (0.12, 0.12, 0.12)
    s.stroke_width = max(1.0, size * 4.0)
    return s


def _block(n, size, bottom_left, color, cols):
    bl = np.asarray(bottom_left, dtype=float)
    return [_square(bl + (c + 0.5) * size * RIGHT + (r + 0.5) * size * UP, size, color)
            for i in range(n) for r, c in [divmod(i, cols)]]


def _label(text, y, size):
    t = Text(text, np.array([0.0, y, 0.0]), font_size=int(np.clip(size * 80, 22, 44)))
    t.color = (0.1, 0.1, 0.1)
    return t


# ===========================================================================
#  SQUARES
# ===========================================================================
def _value_label(text, center, size, color):
    t = Text(text, np.asarray(center, dtype=float), font_size=int(np.clip(size * 80, 22, 44)))
    t.color = color
    return t


def addition(scene, nums, run_time, animating):
    nums = [n for n in nums if n > 0] or [0]
    total = sum(nums)
    size = _size_for(total)
    gap = size * 1.3
    base_y = -0.2                                          # blocks sit here and grow UP
    val_y = base_y - size * 1.7                            # value numbers UNDER the blocks
    expr_y = val_y - size * 2.2                            # expression text even further down

    # per-summand blocks laid left-to-right, each in its own colour
    groups, centers, colors, x = [], [], [], 0.0
    for gi, n in enumerate(nums):
        col = _PALETTE[gi % len(_PALETTE)]
        c = _cols(n)
        groups.append(_block(n, size, [x, 0, 0], col, c))
        centers.append(x + c * size / 2.0)
        colors.append(col)
        x += c * size + gap
    totw = x - gap
    offx = -totw / 2.0
    shift0 = np.array([offx, base_y, 0.0])
    for g in groups:
        for s in g:
            s.shift(shift0)
            scene.add(s)

    # each summand's VALUE under its block, in the block's colour
    sumlabels = []
    for gi, n in enumerate(nums):
        lab = _value_label(str(n), [centers[gi] + offx, val_y, 0.0], size, colors[gi])
        sumlabels.append(lab)
        scene.add(lab)

    # the textual expression at the very bottom (blocks grow up -> never covered)
    scene.add(_label(" + ".join(map(str, nums)) + " = " + str(total), expr_y, size))

    if not animating:
        return

    # target = ONE clean, even grid for the result (centred), instead of ragged pushed-together blocks
    C = _cols(total)
    gbl = np.array([-C * size / 2.0, base_y, 0.0])
    targets = [gbl + (i % C + 0.5) * size * RIGHT + (i // C + 0.5) * size * UP for i in range(total)]
    allsq = [s for g in groups for s in g]
    result_col = _PALETTE[0]
    totlabel = _value_label(str(total), [0.0, val_y, 0.0], size, result_col)
    scene.add(totlabel)

    seg = max(run_time / 2.0, 0.4)
    # 1) reflow every square into the clean result grid
    scene.play(*[Shift(allsq[i], targets[i] - allsq[i].get_center()) for i in range(total)], run_time=seg)
    # 2) become one group (one colour); swap the summand numbers for the total (each in its colour)
    scene.play(*([Recolor(s, result_col) for s in allsq]
                 + [FadeOut(t) for t in sumlabels]
                 + [FadeIn(totlabel)]), run_time=seg)


def subtraction(scene, nums, run_time, animating):
    a = nums[0] if nums else 0
    rest = [n for n in nums[1:]]
    size = _size_for(a + sum(rest))
    cols = _cols(a)
    A = _block(a, size, [0, 0, 0], _PALETTE[0], cols)
    shift0 = np.array([-(cols * size) / 2 - 0.8, -1.0, 0.0])
    for s in A:
        s.shift(shift0)
        scene.add(s)
    scene.add(_label(" − ".join([str(a)] + [str(n) for n in rest]) + " = " + str(a - sum(rest)), 2.2, size))
    alive = list(A)
    if not animating:
        return
    seg = max(run_time / max(len(rest) * 2, 1), 0.3)
    bx = cols * size + 1.2
    for ri, ni in enumerate(rest):                         # subtract each number in turn
        B = _block(ni, size, [bx + ri * (size + 0.3), 0, 0], _PALETTE[(ri + 1) % len(_PALETTE)], _cols(ni))
        for s in B:
            s.shift(shift0)
            scene.add(s)
        k = min(len(alive), ni)
        if k == 0:
            continue
        scene.play(*[Shift(B[i], alive[len(alive) - k + i].get_center()
                            + np.array([size * 0.35, size * 0.35, 0]) - B[i].get_center()) for i in range(k)],
                   run_time=seg)
        scene.wait(0.4)
        scene.play(*([FadeOut(alive[len(alive) - k + i]) for i in range(k)] + [FadeOut(B[i]) for i in range(k)]),
                   run_time=seg)
        alive = alive[:len(alive) - k]


def _groups_of(scene, count, size_each, gap, color_by, cols):
    """Build `count` groups laid left-to-right; return (list-of-groups, total width)."""
    groups, x = [], 0.0
    for gi in range(count):
        groups.append(_block(size_each, _SZ[0], [x, 0, 0], color_by(gi), cols))
        x += cols * _SZ[0] + gap
    return groups, x - gap


_SZ = [0.5]   # current square size (set per op)


def multiplication(scene, nums, run_time, animating):
    nums = [n for n in nums] or [1]
    total = int(np.prod(nums))
    _SZ[0] = _size_for(max(total, 1))
    size = _SZ[0]
    gap = size * 1.3
    scene.add(_label(" × ".join(map(str, nums)) + " = " + str(total), 2.3, size))
    factors = nums[1:] if len(nums) > 1 else [1]
    rt = run_time / max(len(factors), 1)
    res = nums[0]
    prev = None
    for m in factors:                                      # repeat: `res` groups of `m`, merged
        cols = _cols(m)
        groups, width = _groups_of(scene, res, m, gap, lambda gi: _PALETTE[gi % len(_PALETTE)], cols)
        shift0 = np.array([-width / 2, -1.0, 0.0])
        allsq = [s for g in groups for s in g]
        for s in allsq:
            s.shift(shift0)
        if not animating:
            for s in allsq:
                scene.add(s)
            return
        if prev:
            scene.play(*[FadeOut(s) for s in prev], run_time=rt * 0.25)
        for s in allsq:
            scene.add(s)
        step = rt / 3.0
        if res <= 6:                                       # groups appear one after another
            for g in groups:
                scene.play(*[FadeIn(s) for s in g], run_time=max(step / res, 0.12))
        else:
            scene.play(*[FadeIn(s) for s in allsq], run_time=step)
        scene.play(*[Shift(s, np.array([-gi * gap, 0, 0])) for gi, g in enumerate(groups) for s in g], run_time=step)
        scene.play(*[Recolor(s, _PALETTE[0]) for s in allsq], run_time=step)
        prev = allsq
        res *= m


def division(scene, nums, run_time, animating):
    a = nums[0] if nums else 0
    divisors = [max(d, 1) for d in nums[1:]] or [1]
    size = _size_for(max(a, 1))
    gap = size * 0.4
    # final result label
    res_val, rem_parts = a, []
    for d in divisors:
        rem_parts.append(res_val % d)
        res_val //= d
    scene.add(_label(" ÷ ".join([str(a)] + [str(d) for d in nums[1:]]) + " = " + str(res_val), 2.2, size))
    res = a
    prev = None
    rt = run_time / max(len(divisors), 1)
    for d in divisors:                                     # partition the running result into d columns
        cols = _cols(res)
        A = _block(res, size, [0, 0, 0], _PALETTE[0], cols)
        for s in A:
            s.shift(np.array([-(cols * size) / 2, -1.0, 0.0]))
        if not animating:
            for s in A:
                scene.add(s)
            return
        if prev:
            scene.play(*[FadeOut(s) for s in prev], run_time=rt * 0.25)
        for s in A:
            scene.add(s)
        colw = size * 1.4
        x0 = -(d * colw) / 2
        moves = [Shift(A[i], np.array([x0 + (i % d + 0.5) * colw, -2.6 + (i // d + 0.5) * size, 0]) - A[i].get_center())
                 for i in range(res)]
        scene.play(*moves, run_time=rt * 0.5)
        scene.play(*[Recolor(A[i], _PALETTE[(i % d) % len(_PALETTE)]) for i in range(res)], run_time=rt * 0.3)
        prev = A
        res = res // d


# ===========================================================================
#  NUMBER LINE (Cuisenaire bars)
# ===========================================================================
_BARH = 0.34


def _numline(scene, maxv):
    y = -2.2
    unit = min(0.9, 9.5 / max(maxv, 1))
    x0 = -4.8
    X = lambda v: x0 + v * unit
    ln = Line([X(0), y, 0], [X(maxv) + 0.4 * unit, y, 0]); ln.color = (0.2, 0.2, 0.2); ln.stroke_width = 2
    scene.add(ln)
    for v in range(0, int(np.floor(maxv)) + 1):
        tk = Line([X(v), y - 0.12, 0], [X(v), y + 0.12, 0]); tk.color = (0.2, 0.2, 0.2); tk.stroke_width = 2
        scene.add(tk)
        t = Text(str(v), np.array([X(v), y - 0.42, 0.0]), font_size=22); t.color = (0.2, 0.2, 0.2)
        scene.add(t)
    return X, unit, y


def _bar(X, a, b, y, color):
    r = Rectangle(center=np.array([(X(a) + X(b)) / 2.0, y, 0.0]), width=max(X(b) - X(a), 1e-6), height=_BARH)
    r.color = (0.1, 0.1, 0.1); r.fill_color = color; r.fill_opacity = 1.0; r.stroke_width = 1.5
    return r


def addition_nl(scene, nums, run_time, animating):
    nums = [n for n in nums if n > 0] or [0]
    total = sum(nums)
    X, unit, y = _numline(scene, total)
    bars, off = [], 0
    for gi, n in enumerate(nums):
        yrow = y + 0.9 + gi * (_BARH + 0.12)
        bars.append((_bar(X, 0, n, yrow, _PALETTE[gi % len(_PALETTE)]), off, yrow)); off += n
    for bar, _o, _yr in bars:
        scene.add(bar)
    scene.add(_label(" + ".join(map(str, nums)) + " = " + str(total), 2.5, 0.5))
    if animating:
        seg = max(run_time / max(len(bars), 1), 0.3)
        for bar, cum, yrow in bars:                        # drop each onto the line in turn
            scene.play(Shift(bar, np.array([X(cum) - X(0), y - yrow, 0])), run_time=seg)


def subtraction_nl(scene, nums, run_time, animating):
    a = nums[0] if nums else 0
    rest = [n for n in nums[1:]]
    X, unit, y = _numline(scene, max([a] + rest + [1]))
    base = _bar(X, 0, a, y + 0.5, _PALETTE[0])
    scene.add(base)
    scene.add(_label(" − ".join([str(a)] + [str(n) for n in rest]) + " = " + str(a - sum(rest)), 2.5, 0.5))
    if not animating:
        return
    seg = max(run_time / max(len(rest) * 2, 1), 0.3)
    cur = a
    base_end = a                                           # right end of the remaining bar
    for ri, ni in enumerate(rest):
        k = min(cur, ni)
        B = _bar(X, 0, ni, y + 1.4, _PALETTE[(ri + 1) % len(_PALETTE)])
        scene.add(B)
        scene.play(Shift(B, np.array([X(base_end - k) - X(0), (y + 0.5 + _BARH + 0.04) - (y + 1.4), 0])),
                   run_time=seg)                            # lay onto the end
        scene.wait(0.4)
        # shrink the base to cur-k by covering: fade B and draw the shortened base
        new = _bar(X, 0, max(cur - k, 0), y + 0.5, _PALETTE[0])
        scene.add(new)
        scene.play(FadeOut(B), FadeOut(base), run_time=seg)
        base = new
        cur -= k
        base_end = cur


def multiplication_nl(scene, nums, run_time, animating):
    nums = [n for n in nums] or [1]
    total = int(np.prod(nums))
    X, unit, y = _numline(scene, max(total, 1))
    scene.add(_label(" × ".join(map(str, nums)) + " = " + str(total), 2.5, 0.5))
    unitlen = nums[1] if len(nums) > 1 else 1               # a x b -> a segments of length b
    counts = [nums[0]] + nums[2:] if len(nums) > 1 else [nums[0]]
    seglen = unitlen
    prev = None
    rt = run_time / max(len(counts), 1)
    for m in counts:                                       # `m` copies of the current segment length
        pieces = [_bar(X, i * seglen, (i + 1) * seglen, y + 0.6, _PALETTE[i % len(_PALETTE)]) for i in range(m)]
        if not animating:
            for p in pieces:
                scene.add(p)
            return
        if prev:
            scene.play(*[FadeOut(p) for p in prev], run_time=rt * 0.25)
        for p in pieces:
            scene.add(p)
        scene.play(*[FadeIn(p) for p in pieces], run_time=rt * 0.75)
        prev = pieces
        seglen *= m


def division_nl(scene, nums, run_time, animating):
    a = nums[0] if nums else 0
    divisors = [max(d, 1) for d in nums[1:]] or [1]
    X, unit, y = _numline(scene, max(a, 1))
    res_val = a
    for d in divisors:
        res_val //= d
    scene.add(_label(" ÷ ".join([str(a)] + [str(d) for d in nums[1:]]) + " = " + str(res_val), 2.5, 0.5))
    length = float(a)
    prev = None
    rt = run_time / max(len(divisors), 1)
    for d in divisors:                                     # split the current bar into d equal segments
        seg = length / d
        pieces = [_bar(X, i * seg, (i + 1) * seg, y + 0.6, _PALETTE[i % len(_PALETTE)]) for i in range(d)]
        marks = []
        for i in range(1, d):
            m = Line([X(i * seg), y + 0.6 - _BARH, 0], [X(i * seg), y + 0.6 + _BARH, 0])
            m.color = (0.1, 0.1, 0.1); m.stroke_width = 2
            marks.append(m)
        if not animating:
            for p in pieces:
                scene.add(p)
            for m in marks:
                scene.add(m)
            return
        if prev:
            scene.play(*[FadeOut(p) for p in prev], run_time=rt * 0.25)
        for p in pieces:
            scene.add(p)
        for m in marks:
            scene.add(m)
        scene.play(*([FadeIn(p) for p in pieces] + [GrowFromCenter(m) for m in marks]), run_time=rt * 0.75)
        prev = pieces
        length = length / d


_OPS = {"Addition": addition, "Subtraction": subtraction,
        "Multiplication": multiplication, "Division": division}
_OPS_NL = {"Addition": addition_nl, "Subtraction": subtraction_nl,
           "Multiplication": multiplication_nl, "Division": division_nl}


def run(op, scene, nums, run_time=4.0, animating=False, mode="squares"):
    nums = [int(round(float(n))) for n in nums]
    (_OPS_NL if mode == "numberline" else _OPS)[op](scene, nums, float(run_time), animating)

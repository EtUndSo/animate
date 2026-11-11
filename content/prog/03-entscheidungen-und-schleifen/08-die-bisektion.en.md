---
title: Bisection
pfad: Computer Science / Programming / Python / Decisions and Loops
adresse: informatik/programmieren/python/entscheidungen-und-schleifen
knoten: Chapter 3: Decisions and Loops
order: 6040800
summary: The stepping method feels its way toward the solution with fixed steps and is therefore slow.
tags: continuous, Bisection, loop invariant
lang: en
---

<span class="anker" id="stufe-7"></span>

:::zweck
The stepping method feels its way toward the solution with fixed steps and is therefore slow. This section shows a method that halves the range in which the solution must lie in every step, and determines how many steps it needs.
:::

:::::vorwissen What you need for this: the intermediate value theorem

<span class="anker" id="stufe-7-1"></span>

The square root $\sqrt a$ is the positive zero of the function $f(x)=x^2-a$, because $f(\sqrt a)=0$. So instead of searching for a square root, you can search for a zero. How do you recognize that an interval contains a zero?

A function is called __continuous__ on an interval $[x_1,x_2]$ if its graph runs there without a jump, that is, if you can draw it without lifting the pen. For such functions, the following holds:

:::satz Theorem 7.1 (Intermediate value theorem, version for zeros)
<span class="anker" id="satz-7-1"></span>

If $f$ is continuous on $[x_1,x_2]$ and $f(x_1)$ and $f(x_2)$ have different signs, then there is at least one number $x^*$ with $x_1<x^*<x_2$ and $f(x^*)=0$.
:::

Intuitively: if you draw from below the $x$-axis to above it without lifting the pen, you have to cross it somewhere. The theorem is covered in detail in HöMa1, Chapter 5, Section 8.

::::beispiel
$f(x)=x^2-2$ is continuous, and $f(0)=-2<0$ and $f(2)=2>0$. So $f$ has a zero between 0 and 2, namely $\sqrt2$.
::::

⁠**In short:** If a continuous function changes sign between two points, there is a zero in between.

:::::

### The bisection method

<span class="anker" id="stufe-7-2"></span>

The intermediate value theorem says that there is a zero in the interval, but not where. Bisection finds it by dividing the interval again and again.

**Guessing a number with “higher or lower”.** Someone thinks of a number between 1 and 100 and answers only with “higher” or “lower”. If you always guess the middle of the range that is still possible, you halve it with every answer and have the number after at most 7 questions, because $2^7=128\ge100$. Bisection guesses in the same way; the sign of $f$ at the midpoint gives it the answer (Fig. [8](#abb-8)).

:::abbildung prog/k3bisektion 8
Bisection for $\sqrt2$ as nested intervals. Each row shows the interval before a step (blue) and its midpoint (black tick). If the square of the midpoint is less than 2, the midpoint becomes the new left endpoint, otherwise the new right one. Each interval is half as wide as the previous one and always contains $\sqrt2$ (dashed red).
:::

:::definition Definition 7.2 (Bisection)
<span class="anker" id="satz-7-2"></span>

Given are a continuous function $f$, two numbers $\mathit{lo}<\mathit{hi}$ with $f(\mathit{lo})<0\le f(\mathit{hi})$ and a tolerance $\varepsilon>0$. __Bisection__ repeats the following as long as $\mathit{hi}-\mathit{lo}>\varepsilon$:

<ol>

<li>

Compute the midpoint $m=(\mathit{lo}+\mathit{hi})/2$.

</li>

<li>

If $f(m)<0$, set $\mathit{lo}=m$, otherwise $\mathit{hi}=m$.

</li>

</ol>

The result is the midpoint of the last interval. If the signs are the other way around, $f(\mathit{lo})>0\ge f(\mathit{hi})$, you swap the two cases in step 2.
:::

After every step, $f(\mathit{lo})<0\le f(\mathit{hi})$ holds again: the endpoint that is replaced by the midpoint is always the one with the same sign as $f(m)$. By the intermediate value theorem, the interval therefore always contains a zero, or its right endpoint is one itself.

::::beispiel
The first six steps for $f(x)=x^2-2$ with $\mathit{lo}=0$ and $\mathit{hi}=2$:

| Step | $\mathit{lo}$ | $\mathit{hi}$ | $m$ | $m^2$ | new interval |
|---|---|---|---|---|---|
| 1 | 0 | 2 | 1 | 1 | $[1,\,2]$ |
| 2 | 1 | 2 | 1.5 | 2.25 | $[1,\,1.5]$ |
| 3 | 1 | 1.5 | 1.25 | 1.5625 | $[1.25,\,1.5]$ |
| 4 | 1.25 | 1.5 | 1.375 | 1.890625 | $[1.375,\,1.5]$ |
| 5 | 1.375 | 1.5 | 1.4375 | 2.06640625 | $[1.375,\,1.4375]$ |
| 6 | 1.375 | 1.4375 | 1.40625 | 1.9775390625 | $[1.40625,\,1.4375]$ |

After six steps, the interval is $2/2^6=0.03125$ wide, and $\sqrt2\approx1.4142$ lies inside it.
::::

⁠**In short:** In every step, bisection replaces the endpoint that lies on the same side of the zero as the midpoint by the midpoint.

:::hintergrund Why bisection cannot miss: the loop invariant
To show that a loop computes the right thing, you look for a statement that holds before the first iteration and that every iteration preserves. Such a statement is called a __loop invariant__. For bisection, it is “$f(\mathit{lo})<0\le f(\mathit{hi})$”. It holds at the start by assumption, and every iteration preserves it, as shown above. So it also holds after the last iteration. In addition, the stopping condition then holds, $\mathit{hi}-\mathit{lo}\le\varepsilon$. Together, the two say: the interval $(\mathit{lo},\mathit{hi}]$ of width at most $\varepsilon$ contains a zero, and the midpoint is at most $\varepsilon/2$ away from it. That the loop ends at all follows from a second observation: the width halves in every iteration and therefore at some point becomes smaller than any positive $\varepsilon$. This approach, an invariant plus a quantity that is certain to decrease, is the usual way of justifying loops, not only for bisection.
:::

### The square root by bisection

<span class="anker" id="stufe-7-3"></span>

As a script, bisection for $\sqrt a$ needs a starting interval with a sign change. On the left, $\mathit{lo}=0$ always works, because $f(0)=-a<0$. On the right, $\mathit{hi}=\max(1,a)$ works: for $a\ge1$, $a^2\ge a$, so $f(a)\ge0$; for $a<1$, $f(1)=1-a>0$.

```python wurzel_bisektion.py
# Square root by bisection: zero of f(x) = x*x - a in the interval [lo, hi]
a = float(input("a = "))
eps = float(input("Toleranz eps = "))     # desired width of the interval
lo = 0.0                                  # f(lo) < 0
hi = max(1.0, a)                          # f(hi) >= 0, since the root never lies above max(1, a)
schritte = 0
while hi - lo > eps:
    mitte = (lo + hi) / 2
    if mitte * mitte < a:                 # f(mitte) < 0: zero lies right of the midpoint mitte
        lo = mitte
    else:                                 # otherwise it lies left of mitte or exactly there
        hi = mitte
    schritte = schritte + 1
print("Näherung:", (lo + hi) / 2, "nach", schritte, "Schritten")
print("Intervall:", lo, "bis", hi)
```

```console Linux
$ python3 wurzel_bisektion.py
a = 2
Toleranz eps = 1e-12
Näherung: 1.414213562372879 nach 41 Schritten
Intervall: 1.4142135623724243 bis 1.4142135623733338
$ python3 wurzel_bisektion.py
a = 25
Toleranz eps = 0.01
Näherung: 5.0018310546875 nach 12 Schritten
Intervall: 4.998779296875 bis 5.0048828125
```

For $\sqrt2$, 41 steps are enough, and the result deviates from $\sqrt2$ by only $2.2\cdot10^{-13}$. For $\sqrt{25}$ with the tolerance 0.01, it takes 12 steps instead of the 49 990 of the stepping method. The tolerance means something different here than there: it limits the width of the interval for $g$, not the distance of $g^2$ from $a$.

⁠**In short:** With the starting interval $[0,\max(1,a)]$, bisection finds $\sqrt2$ to twelve digits in 41 steps.

### The number of steps of bisection

<span class="anker" id="stufe-7-4"></span>

41 and 12: these numbers can be calculated before the start.

:::satz Theorem 7.3 (Number of steps of bisection)
<span class="anker" id="satz-7-3"></span>

If bisection starts with an interval of width $L=\mathit{hi}-\mathit{lo}$, the interval is $L/2^n$ wide after $n$ steps. If $L>\varepsilon$, bisection ends after

$$n=\Bigl\lceil\log_2\frac{L}{\varepsilon}\Bigr\rceil$$

steps, and the midpoint it returns is at most $\varepsilon/2$ away from a zero.
:::

:::beweis Halving
Every step replaces an endpoint by the midpoint, so the interval becomes exactly half as wide. After $n$ steps, it is $L/2^n$ wide. The loop runs as long as the width is greater than $\varepsilon$, and it ends after the first $n$ with $L/2^n\le\varepsilon$, that is, with $2^n\ge L/\varepsilon$ or $n\ge\log_2(L/\varepsilon)$. The smallest such $n$ is the rounded-up number $\lceil\log_2(L/\varepsilon)\rceil$. By the loop invariant, the last interval contains a zero, and the midpoint is at most half the width, that is, at most $\varepsilon/2$, away from every point of the interval.
:::

The proof calculates with exact midpoints. In the examples of this section, the midpoints can be represented exactly as `float`, because they are fractions with powers of two in the denominator and have fewer than 53 binary digits. With endpoints such as 0.02, which are already stored rounded themselves, the midpoint is rounded, too, but by at most one smallest step of the floating-point numbers. The number of steps from the theorem then still holds, except when $L/2^n$ is almost exactly $\varepsilon$.

::::beispiel
For $\sqrt2$ with $[0,2]$ and $\varepsilon=10^{-12}$, $L/\varepsilon=2\cdot10^{12}$ and $\log_2(2\cdot10^{12})=40.86$, rounded up 41. For $\sqrt{25}$ with $[0,25]$ and $\varepsilon=0.01$, $\log_2 2500=11.29$, rounded up 12. Both are exactly the numbers of steps of the scripts.
::::

⁠**In short:** Bisection needs $\lceil\log_2(L/\varepsilon)\rceil$ steps; every tenfold increase in accuracy costs only about 3.3 more steps.

:::hintergrund Why halving is so much faster than scanning
The stepping method from Section [6](losungen-durch-probieren-raten-und-prufen-naherung-mit-toleranz.html#stufe-6) shrinks the range in which the solution can still lie by a fixed amount $h$ in every step; the number of steps therefore grows like $L/h$. Bisection halves the range. With $n$ steps, it distinguishes $2^n$ subintervals of equal width, and the $n$ yes-no answers determine which of them contains the solution. Ten steps already distinguish $2^{10}=1024$, that is, about $10^3$ subintervals, which is three decimal places. For twelve digits, you need about $4\cdot10=40$ steps, instead of $2\cdot10^{12}$ when scanning with step size $\varepsilon$.

You can see what these answers are in the table in subsection [7.2](#stufe-7-2). If you write a 1 for “the midpoint becomes the left endpoint” and a 0 for “the midpoint becomes the right endpoint”, the first twelve steps for $\sqrt2$ give the sequence `1 0 1 1 0 1 0 1 0 0 0 0`. These are exactly the first twelve binary digits of $\sqrt2=1.01101010000\ldots_2$ ([Chapter 2, Section 3.6](/wissen/en/informatik/programmieren/python/werte-typen-und-variablen/zahlen-im-binarsystem.html#stufe-3-6)). So every step of bisection determines one more bit of the solution, no more and no less.
:::

:::hintergrund How small the tolerance may be
The width of the interval cannot fall below the spacing of adjacent `float` values. For $\sqrt2$, this spacing is $\varepsilon_{\mathrm M}=2.2\cdot10^{-16}$. If you ask for $\varepsilon=10^{-17}$, $\mathit{lo}$ and $\mathit{hi}$ are neighbors after 53 steps, `1.414213562373095` and `1.4142135623730951`. Their rounded midpoint is again one of the two, the interval no longer gets smaller, and the condition `hi - lo > eps` stays true forever: an infinite loop. The remedy is either a tolerance that fits the size of the solution, such as `hi - lo > 1e-15 * hi` as in the comparison with a relative tolerance in [Chapter 2, Section 7.4](/wissen/en/informatik/programmieren/python/werte-typen-und-variablen/wahrheitswerte-und-vergleiche.html#stufe-7-4), or a maximum number of steps as an emergency brake.
:::

### Exercises for Section [7](#stufe-7)

<span class="anker" id="stufe-7-5"></span>

:::aufgabe Exercise 27 ★ Bisection by hand
<span class="anker" id="aufg-27"></span>

Carry out four steps of bisection for $\sqrt3$ by hand, with $f(x)=x^2-3$ and the starting interval $[1,2]$. Make a table as in subsection [7.2](#stufe-7-2). How wide is the last interval, and which approximation does its midpoint give?

:::loesung
| Step | $\mathit{lo}$ | $\mathit{hi}$ | $m$ | $m^2$ | new interval |
|---|---|---|---|---|---|
| 1 | 1 | 2 | 1.5 | 2.25 | $[1.5,\,2]$ |
| 2 | 1.5 | 2 | 1.75 | 3.0625 | $[1.5,\,1.75]$ |
| 3 | 1.5 | 1.75 | 1.625 | 2.640625 | $[1.625,\,1.75]$ |
| 4 | 1.625 | 1.75 | 1.6875 | 2.84765625 | $[1.6875,\,1.75]$ |

The last interval is $1/2^4=0.0625$ wide. Its midpoint 1.71875 deviates from $\sqrt3\approx1.73205$ by 0.013, less than half the width, 0.03125, as Theorem [7.3](#satz-7-3) promises.
:::
:::

:::aufgabe Exercise 28 ★★ Predicting numbers of steps
<span class="anker" id="aufg-28"></span>

Use Theorem [7.3](#satz-7-3) to calculate how many steps `wurzel_bisektion.py` needs, and then check on the computer: (a) $a=10$, $\varepsilon=10^{-6}$; (b) $a=1000$, $\varepsilon=10^{-9}$; (c) $a=2$, $\varepsilon=5\cdot10^{-13}$; (d) $a=2$, $\varepsilon=10^{-13}$. How many steps does each halving of $\varepsilon$ cost, and how many each division by ten?

:::loesung
With $L=\max(1,a)$: (a) $\lceil\log_2(10/10^{-6})\rceil=\lceil23.25\rceil=24$; (b) $\lceil\log_2(1000/10^{-9})\rceil=\lceil39.86\rceil=40$; (c) $\lceil\log_2(2/(5\cdot10^{-13}))\rceil=\lceil41.86\rceil=42$; (d) $\lceil\log_2(2/10^{-13})\rceil=\lceil44.19\rceil=45$.

```console Linux
$ python3 wurzel_bisektion.py
a = 10
Toleranz eps = 1e-6
Näherung: 3.162277638912201 nach 24 Schritten
Intervall: 3.162277340888977 bis 3.162277936935425
$ python3 wurzel_bisektion.py
a = 1000
Toleranz eps = 1e-9
Näherung: 31.62277660203472 nach 40 Schritten
Intervall: 31.62277660157997 bis 31.622776602489466
$ python3 wurzel_bisektion.py
a = 2
Toleranz eps = 5e-13
Näherung: 1.4142135623731065 nach 42 Schritten
Intervall: 1.414213562372879 bis 1.4142135623733338
$ python3 wurzel_bisektion.py
a = 2
Toleranz eps = 1e-13
Näherung: 1.414213562373078 nach 45 Schritten
Intervall: 1.4142135623730496 bis 1.4142135623731065
```

Each halving of $\varepsilon$ costs exactly one step (from 41 to 42), because $\log_2(2x)=\log_2x+1$. Each division by ten costs $\log_2 10\approx3.32$ steps, that is, three or four (from 42 at $5\cdot10^{-13}$ to 45 at $10^{-13}$, it is three, because the factor there is only 5; from 41 at $10^{-12}$ to 45 at $10^{-13}$, it is four).
:::
:::

:::aufgabe Exercise 29 ★★ Zeros without a square root
<span class="anker" id="aufg-29"></span>

Bisection works for every continuous function with a sign change.

<ol class="al">

<li>

Use bisection to find the number $x$ with $\cos x=x$ in the interval $[0,1]$, that is, the zero of $f(x)=\cos x-x$, with $\varepsilon=10^{-12}$. Check the sign change first. Caution: here, $f(\mathit{lo})>0$.

</li>

<li>

Likewise, find the zero of $x^3-x-1$ in $[1,2]$.

</li>

</ol>

:::loesung
(a) $f(0)=\cos0-0=1>0$ and $f(1)=\cos1-1\approx-0.46<0$: there is a sign change. Because $f(\mathit{lo})>0$, `lo` is replaced if $f$ is still positive at the midpoint:

```python bisektion_cos.py
# Bisection for cos(x) = x, that is, the zero of f(x) = cos(x) - x in [0, 1]; here f(lo) > 0
import math
lo = 0.0                                  # f(0) = 1 > 0
hi = 1.0                                  # f(1) = cos(1) - 1 < 0
eps = 1e-12
schritte = 0
while hi - lo > eps:
    mitte = (lo + hi) / 2
    if math.cos(mitte) - mitte > 0:       # f(mitte) > 0: the zero lies to the right of mitte
        lo = mitte
    else:
        hi = mitte
    schritte = schritte + 1
x = (lo + hi) / 2
print("x =", x, "nach", schritte, "Schritten, cos(x) - x =", math.cos(x) - x)
```

```console Linux
$ python3 bisektion_cos.py
x = 0.7390851332152124 nach 40 Schritten, cos(x) - x = -8.659739592076221e-14
```

The number of steps is $\lceil\log_2(1/10^{-12})\rceil=\lceil39.86\rceil=40$.

(b) $f(1)=-1<0$, $f(2)=5>0$, as with the square root:

```python bisektion_kubisch.py
# Bisection for the zero of f(x) = x**3 - x - 1 in [1, 2]
lo = 1.0                                  # f(1) = -1 < 0
hi = 2.0                                  # f(2) = 5 > 0
eps = 1e-12
schritte = 0
while hi - lo > eps:
    mitte = (lo + hi) / 2
    if mitte ** 3 - mitte - 1 < 0:
        lo = mitte
    else:
        hi = mitte
    schritte = schritte + 1
x = (lo + hi) / 2
print("x =", x, "nach", schritte, "Schritten")
```

```console Linux
$ python3 bisektion_kubisch.py
x = 1.3247179572449568 nach 40 Schritten
```

Again 40 steps, because the interval is again 1 wide. Bisection needs only the sign of the function; whether it is a square root, a cosine or a polynomial does not matter.
:::
:::

:::aufgabe Exercise 30 ★★★ A tolerance that is too small
<span class="anker" id="aufg-30"></span>

Start bisection for $\sqrt2$ with $\varepsilon=10^{-17}$ and an emergency brake after 200 steps. After the loop, print `lo`, `hi`, `hi - lo` and the number of steps. Explain the result. Then replace the condition by `hi - lo > 1e-15 * hi` and determine the number of steps, also with Theorem [7.3](#satz-7-3).

:::loesung
```python bisektion_eps.py
# Bisection for the square root of 2 with a tolerance that is too small, with an emergency brake after 200 steps
lo = 0.0
hi = 2.0
eps = 1e-17
schritte = 0
while hi - lo > eps and schritte < 200:
    mitte = (lo + hi) / 2
    if mitte * mitte < 2:
        lo = mitte
    else:
        hi = mitte
    schritte = schritte + 1
print("lo =", lo, " hi =", hi)
print("hi - lo =", hi - lo, " Schritte:", schritte)

lo = 0.0                                  # the same with a relative tolerance
hi = 2.0
schritte = 0
while hi - lo > 1e-15 * hi:
    mitte = (lo + hi) / 2
    if mitte * mitte < 2:
        lo = mitte
    else:
        hi = mitte
    schritte = schritte + 1
print("relativ: Näherung", (lo + hi) / 2, "nach", schritte, "Schritten")
```

```console Linux
$ python3 bisektion_eps.py
lo = 1.414213562373095  hi = 1.4142135623730951
hi - lo = 2.220446049250313e-16  Schritte: 200
relativ: Näherung 1.4142135623730954 nach 51 Schritten
```

With $\varepsilon=10^{-17}$, the loop ends only through the emergency brake. `lo` and `hi` are neighboring `float` values with the spacing $\varepsilon_{\mathrm M}=2.2\cdot10^{-16}$; their midpoint cannot be represented and is rounded to one of the two, so that nothing changes anymore. With the relative tolerance, the loop ends as soon as the width is at most $10^{-15}\cdot\mathit{hi}\approx1.41\cdot10^{-15}$. By Theorem [7.3](#satz-7-3) with this $\varepsilon$: $\lceil\log_2(2/(1.41\cdot10^{-15}))\rceil=\lceil50.3\rceil=51$. The approximation `1.4142135623730954` is the neighbor above `math.sqrt(2)`, that is, one step away from the best value and well within the required accuracy.
:::
:::

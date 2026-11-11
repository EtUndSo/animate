---
title: Newton's method
pfad: Computer Science / Programming / Python / Decisions and Loops
adresse: informatik/programmieren/python/entscheidungen-und-schleifen
knoten: Chapter 3: Decisions and Loops
order: 6040900
summary: In every step, bisection asks only for the sign of f and thereby gains one bit.
tags: tangent line, Newton's method, quadratic convergence
lang: en
---

<span class="anker" id="stufe-8"></span>

:::zweck
In every step, bisection asks only for the sign of $f$ and thereby gains one bit. This section shows a method that also uses the slope of $f$ and thereby roughly doubles the number of significant digits in every step. It is Heron's method from [Chapter 1](/wissen/en/informatik/programmieren/python/programme-und-der-python-interpreter/programme-und-der-python-interpreter.html), now with the reason why it is so fast and when it fails.
:::

:::::vorwissen What you need for this: derivative and tangent line

<span class="anker" id="stufe-8-1"></span>

The derivative $f'(g)$ of a function at the point $g$ is the slope of its graph there. The __tangent line__ at the point $g$ is the straight line through the point $(g, f(g))$ with this slope:

$$t(x)=f(g)+f'(g)\,(x-g).$$

Near $g$, the graph hardly differs from its tangent line. For the square root, you need only one derivative from school: for $f(x)=x^2-a$ with a fixed number $a$, $f'(x)=2x$.

::::beispiel
For $f(x)=x^2-2$ at the point $g=2$, $f(2)=2$ and $f'(2)=4$, so the tangent line is $t(x)=2+4(x-2)$. It crosses the $x$-axis where $t(x)=0$: $x=2-2/4=1.5$.
::::

⁠**In short:** The tangent line is the straight line that hugs the graph at one point; its slope is the derivative.

:::::

### Newton's method

<span class="anker" id="stufe-8-2"></span>

The zero of a curve is hard to find, whereas the zero of a straight line is easy to find. Newton's method therefore replaces the curve by its tangent line in every step.

**Following the tangent.** You stand on the graph above an estimate $g$, draw the tangent line and follow it down to the $x$-axis. The crossing point is the new estimate. If the estimate is already close to the zero, the tangent line hugs the curve closely all the way there, and you land very close to the true zero (Fig. [9](#abb-9)).

:::abbildung prog/k3newton 9
Two steps of Newton's method for $f(x)=x^2-2$. The tangent line at $g_0=2$ (orange) crosses the axis at $g_1=1.5$, the tangent line at $g_1$ (green) at $g_2=1.41\overline{6}$. The red dot is $\sqrt2\approx1.41421$; $g_2$ already lies so close to it that the two points can hardly be told apart in this plot.
:::

:::definition Definition 8.1 (Newton's method)
<span class="anker" id="satz-8-1"></span>

__Newton's method__ for a zero of a differentiable function $f$ starts with a starting value $g_0$ and from it computes one after another

$$g_{n+1}=g_n-\frac{f(g_n)}{f'(g_n)},$$

as long as $|f(g_n)|$ is greater than a tolerance $\varepsilon$. $g_{n+1}$ is the zero of the tangent line at the point $g_n$; for this, $f'(g_n)\ne0$ must hold.
:::

The formula follows directly from the tangent line: $t(x)=f(g_n)+f'(g_n)(x-g_n)=0$ gives $x=g_n-f(g_n)/f'(g_n)$.

::::beispiel
For $f(x)=x^2-2$ with $g_0=2$, $g_1=1.5$ as in subsection [8.1](#stufe-8-1). In the next step, $f(1.5)=0.25$ and $f'(1.5)=3$, so $g_2=1.5-0.25/3=1.41\overline6$.
::::

⁠**In short:** In every step, Newton's method jumps to the zero of the tangent line.

### The square root by Newton's method

<span class="anker" id="stufe-8-3"></span>

For $f(g)=g^2-a$, $f'(g)=2g$, and the Newton step is

$$g_{n+1}=g_n-\frac{g_n^2-a}{2g_n}=\frac{2g_n^2-g_n^2+a}{2g_n}=\frac12\Bigl(g_n+\frac{a}{g_n}\Bigr).$$

This is exactly Heron's method from [Chapter 1, Sections 1.1](/wissen/en/informatik/programmieren/python/programme-und-der-python-interpreter/programme-und-programmiersprachen.html#stufe-1-1) and [4.5](/wissen/en/informatik/programmieren/python/programme-und-der-python-interpreter/der-interaktive-modus.html#stufe-4-5): the old recipe for the square root is Newton's method for $x^2-a$. As a script with a loop that stops as soon as $|g^2-a|\le10^{-12}$:

```python wurzel_newton.py
# Square root with Newton's method: g -> g - f(g)/f'(g) with f(g) = g*g - a and f'(g) = 2*g
a = float(input("a = "))
eps = 1e-12                               # tolerance for |g*g - a|
g = max(1.0, a)                           # starting value
schritte = 0
while abs(g * g - a) > eps:
    g = g - (g * g - a) / (2 * g)
    schritte = schritte + 1
    print(f"Schritt {schritte}: g = {g}")
print("Näherung:", g, "nach", schritte, "Schritten")
```

```console Linux
$ python3 wurzel_newton.py
a = 2
Schritt 1: g = 1.5
Schritt 2: g = 1.4166666666666667
Schritt 3: g = 1.4142156862745099
Schritt 4: g = 1.4142135623746899
Schritt 5: g = 1.4142135623730951
Näherung: 1.4142135623730951 nach 5 Schritten
```

Five steps instead of 41. The correct digits grow visibly: one after step 1 (`1.5`), three after step 2 (`1.416`), six after step 3, twelve after step 4, and step 5 hits the `float` closest to $\sqrt2$. The script takes the starting value $\max(1,a)$ from bisection; it certainly does not lie below the square root.

⁠**In short:** For the square root, the Newton step is Heron's recipe $\frac12(g+a/g)$, and it needs five steps for $\sqrt2$.

:::hintergrund Why Heron's recipe from Chapter 1 landed one step off
In [Chapter 1, Section 4.5](/wissen/en/informatik/programmieren/python/programme-und-der-python-interpreter/der-interaktive-modus.html#stufe-4-5), the recipe in the form `(g + 2/g) / 2` ended at `1.414213562373095`, one smallest step away from `2 ** 0.5`. The script here calculates with the form `g - (g*g - 2)/(2*g)` and stops after step 5 at `1.4142135623730951`. Both forms are mathematically equal, but they round differently, just as ten times `+ 0.1` and `* 10` do in [Chapter 2, Section 5.1](/wissen/en/informatik/programmieren/python/werte-typen-und-variablen/rechnen-mit-gleitkommazahlen.html#stufe-5-1). Very close to the target, something else comes into play with the second form: in `g*g - 2`, two almost equal numbers are subtracted from each other, and the result consists almost entirely of rounding errors, as with cancellation in [Chapter 2, Section 5.4](/wissen/en/informatik/programmieren/python/werte-typen-und-variablen/rechnen-mit-gleitkommazahlen.html#stufe-5-4). If you let this form keep running, $g$ would therefore jump back and forth between `1.4142135623730951` and `1.414213562373095` without end; when the script stopped, it happened to catch the better of the two. The Heron form, by contrast, stays at `1.414213562373095`. For $\sqrt3$, both forms hit the best value with the script's stopping rule. In a test with 100 000 numbers between 0.01 and 1000, both forms were never more than one step away from the best `float` after many steps; the Newton form oscillated between two neighbors in a good quarter of the cases. A method that itself calculates with rounded numbers can hardly promise more, and tolerances such as $10^{-12}$ are much coarser than one step anyway.
:::

### The speed of convergence

<span class="anker" id="stufe-8-4"></span>

That the number of correct digits roughly doubles in every step is no coincidence of the number 2. For the square root, you can calculate it exactly.

:::satz Theorem 8.2 (Error of the Newton step for the square root)
<span class="anker" id="satz-8-2"></span>

Let $a>0$, $g_n>0$ and $g_{n+1}=\frac12(g_n+a/g_n)$. The errors $d_n=g_n-\sqrt a$ satisfy

$$d_{n+1}=\frac{d_n^2}{2g_n}.$$
:::

:::beweis Direct calculation
$d_{n+1}=\dfrac{g_n^2+a}{2g_n}-\sqrt a=\dfrac{g_n^2-2\sqrt a\,g_n+a}{2g_n}=\dfrac{(g_n-\sqrt a)^2}{2g_n}=\dfrac{d_n^2}{2g_n}$.
:::

Two consequences. First, $d_{n+1}\ge0$: after the first step, every estimate lies above $\sqrt a$ or on it. Second, the error is squared in every step, apart from the factor $1/(2g_n)$, which is about $1/(2\sqrt a)$ near the solution. For the relative error $\delta_n=d_n/\sqrt a$, this together with $g_n\ge\sqrt a$ gives the estimate $\delta_{n+1}=\delta_n^2\sqrt a/(2g_n)\le\delta_n^2/2$. If $\delta_n$ is about $10^{-p}$, so that $g_n$ has about $p$ significant decimal digits, then $\delta_{n+1}$ is at most about $10^{-2p}/2$: $p$ significant digits become about $2p$. This property is called __quadratic convergence__.

::::beispiel
The errors of the script for $\sqrt2$ with $g_0=2$, recalculated with the theorem:

| $n$ | $d_n=g_n-\sqrt2$ | $d_n^2/(2g_n)$ |
|---|---|---|
| 0 | $0.586$ | $0.0858$ |
| 1 | $0.0858$ | $0.00245$ |
| 2 | $0.00245$ | $2.12\cdot10^{-6}$ |
| 3 | $2.12\cdot10^{-6}$ | $1.59\cdot10^{-12}$ |
| 4 | $1.59\cdot10^{-12}$ | $9\cdot10^{-25}$, smaller than the spacing of the `float` values |

Each row correctly predicts the error of the next one. Fig. [10](#abb-10) puts the three methods side by side.

:::abbildung prog/k3fehler 10
Error versus the number of steps for $\sqrt2$, on a logarithmic scale. The stepping method with step size 0.01 has hardly come any closer after 42 steps. Bisection (error of the midpoint after $n$ steps) follows the dashed line on average: halving is a straight line on the logarithmic axis. Newton falls off more and more steeply, because every step squares the error; after step 4, the error can no longer be plotted, because it is zero.
:::
::::

⁠**In short:** With Newton's method, the error is squared in every step, and the number of significant digits doubles.

:::hintergrund Why Newton doubles the digits
The theorem does not hold only for the square root. Taylor's formula with remainder, applied to a twice differentiable function $f$ at the point $g$, gives for a zero $x^*$

$$0=f(x^*)=f(g)+f'(g)\,(x^*-g)+\tfrac12f''(\xi)\,(x^*-g)^2$$

with a number $\xi$ between $g$ and $x^*$. The tangent line leaves out the last term; so its error is quadratic in the distance. Dividing by $f'(g)$ and substituting the Newton step $g'=g-f(g)/f'(g)$ leaves

$$g'-x^*=\frac{f''(\xi)}{2f'(g)}\,(g-x^*)^2 .$$

For $f(x)=x^2-a$, $f''=2$ and $f'(g)=2g$, and you get exactly Theorem [8.2](#satz-8-2). The mechanism: the method replaces the function by a straight line, and a smooth function differs from its tangent line only by an error that grows with the square of the distance. Bisection uses only the sign of $f$, one bit per step. Newton uses the value and the slope, that is, much more information about the location of the zero, and therefore gains more. This holds as long as $f'(x^*)\ne0$ and you start close enough to the zero; the next subsection shows what happens otherwise.
:::

### The limits of Newton's method

<span class="anker" id="stufe-8-5"></span>

With a sign change, bisection always finds a zero. Newton's method is much faster, but it has no such guarantee.

**The slope is zero.** If $f'(g)=0$, the tangent line is horizontal and does not cross the axis. For the square root, this happens at the starting value $g=0$:

```console
>>> g = 0.0
>>> g - (g * g - 2) / (2 * g)
Traceback (most recent call last):
  File "<python-input-1>", line 1, in <module>
    g - (g * g - 2) / (2 * g)
        ~~~~~~~~~~~~^~~~~~~~~
ZeroDivisionError: division by zero
```

Python 3.13 reports `float division by zero` here.

**A cycle.** For some functions and starting values, the estimates jump back and forth without approaching the zero. For $f(x)=x^3-2x+2$ with $f'(x)=3x^2-2$ and the starting value 0, the method returns to the start after two steps. The only real zero lies at about $-1.77$, far away from both values:

```python newton_zyklus.py
# Newton for f(x) = x**3 - 2*x + 2 with starting value 0: six steps
x = 0.0
for schritt in range(1, 7):
    x = x - (x ** 3 - 2 * x + 2) / (3 * x ** 2 - 2)
    print(f"Schritt {schritt}: x = {x}")
```

```console Linux
$ python3 newton_zyklus.py
Schritt 1: x = 1.0
Schritt 2: x = 0.0
Schritt 3: x = 1.0
Schritt 4: x = 0.0
Schritt 5: x = 1.0
Schritt 6: x = 0.0
```

With a `while` loop and the condition $|f(x)|>\varepsilon$, this would be an infinite loop.

**A tolerance that is never reached.** The condition `abs(g * g - a) > 1e-12` compares with a fixed number. For large $a$, however, even the spacings of adjacent `float` values near $g^2$ are larger than $10^{-12}$. For $a=123456789$, the method comes to rest at a value where $g^2-a$ is about $-1.5\cdot10^{-8}$, and the next step no longer changes $g$:

```console
>>> a = 123456789.0
>>> g = 11111.111060555555
>>> g * g - a
-1.4901161193847656e-08
>>> g - (g * g - a) / (2 * g)
11111.111060555555
```

`wurzel_newton.py` would never stop for this $a$. As with bisection, the remedy is a relative tolerance, `abs(g * g - a) > 1e-12 * a` ([Chapter 2, Section 7.4](/wissen/en/informatik/programmieren/python/werte-typen-und-variablen/wahrheitswerte-und-vergleiche.html#stufe-7-4)).

**Far away, it is slow.** Quadratic convergence holds only near the zero. For $\sqrt{25}$ with the starting value 25, the error shrinks only by a small factor in the first steps, from 20 to 8 and then to about 2.5, before the digits begin to double:

```console Linux
$ python3 wurzel_newton.py
a = 25
Schritt 1: g = 13.0
Schritt 2: g = 7.461538461538462
Schritt 3: g = 5.406026962727994
Schritt 4: g = 5.015247601944898
Schritt 5: g = 5.000023178253949
Schritt 6: g = 5.000000000053723
Schritt 7: g = 5.0
Näherung: 5.0 nach 7 Schritten
```

For $g_n\gg\sqrt a$, $\frac12(g_n+a/g_n)\approx g_n/2$: far above the square root, every step only halves the estimate and therefore also roughly the error, which there is almost as large as the estimate itself.

⁠**In short:** Newton needs a nonzero derivative, a starting value close to the solution and a suitable tolerance; then it is very fast, otherwise it can cycle, crawl or run forever.

### The ready-made way: `math.sqrt`

<span class="anker" id="stufe-8-6"></span>

For the square root itself, in practice you do not write a loop but call `math.sqrt` ([Chapter 2, Section 8.2](/wissen/en/informatik/programmieren/python/werte-typen-und-variablen/module-math-und-sys.html#stufe-8-2)). The following script puts the ways by hand and the ready-made way side by side, with the same tolerance:

```python wurzel_vergleich.py
# Square root of 2 by hand (bisection, Newton) and ready-made (math.sqrt), same tolerance 1e-12
import math
a = 2.0
eps = 1e-12

lo = 0.0                                  # bisection
hi = max(1.0, a)
schritte_b = 0
while hi - lo > eps:
    mitte = (lo + hi) / 2
    if mitte * mitte < a:
        lo = mitte
    else:
        hi = mitte
    schritte_b = schritte_b + 1
bisektion = (lo + hi) / 2

g = max(1.0, a)                           # Newton
schritte_n = 0
while abs(g * g - a) > eps:
    g = g - (g * g - a) / (2 * g)
    schritte_n = schritte_n + 1

fertig = math.sqrt(a)                     # ready-made way
print(f"Bisektion:  {bisektion}  nach {schritte_b} Schritten, Abstand zu math.sqrt {abs(bisektion - fertig):.1e}")
print(f"Newton:     {g}  nach {schritte_n} Schritten, Abstand zu math.sqrt {abs(g - fertig):.1e}")
print(f"math.sqrt:  {fertig}")
print("Newton == math.sqrt:", g == fertig)
```

```console Linux
$ python3 wurzel_vergleich.py
Bisektion:  1.414213562372879  nach 41 Schritten, Abstand zu math.sqrt 2.2e-13
Newton:     1.4142135623730951  nach 5 Schritten, Abstand zu math.sqrt 0.0e+00
math.sqrt:  1.4142135623730951
Newton == math.sqrt: True
```

This completes the path “first by hand, then ready-made” for the square root:

| Method | Effort | Result |
|---|---|---|
| Guess and check | about $\sqrt a$ steps | only integer square roots (subsection [6.1](losungen-durch-probieren-raten-und-prufen-naherung-mit-toleranz.html#stufe-6-1)) |
| Stepping method | about $a/\varepsilon$ steps | $\sqrt{25}$: 49 990 steps for $\varepsilon=0.01$; $\sqrt2$ to twelve digits: over two days (subsection [6.3](losungen-durch-probieren-raten-und-prufen-naherung-mit-toleranz.html#stufe-6-3)) |
| Bisection | $\lceil\log_2(L/\varepsilon)\rceil$ steps | $\sqrt2$: 41 steps, deviation $2.2\cdot10^{-13}$ (Section [7](die-bisektion.html#stufe-7)) |
| Newton | a few steps near the solution | $\sqrt2$: 5 steps, exactly the `float` of `math.sqrt` (subsection [8.3](#stufe-8-3)) |
| `math.sqrt` | one call | the `float` closest to $\sqrt a$ |

What `math.sqrt` does in addition: it is fast and accurate for every number, without your having to choose a starting value, a tolerance or an emergency brake, and for negative numbers it reports an error instead of letting a loop run forever.

⁠**In short:** `math.sqrt` delivers in one call the result that the methods by hand reach only approximately and with a carefully chosen tolerance.

:::hintergrund What `math.sqrt` does in the processor
The module `math` passes most functions on to the math library of the C language. For the square root, common PC processors (x86-64) have an instruction of their own, and the C library uses it. The IEEE 754 standard requires the same for the square root as for the four basic arithmetic operations: the result is the exact value, rounded to the nearest `float` ([Chapter 2, Section 5.1](/wissen/en/informatik/programmieren/python/werte-typen-und-variablen/rechnen-mit-gleitkommazahlen.html#stufe-5-1)). For $\sqrt2$, you can check this: `1.4142135623730951` lies $9.7\cdot10^{-17}$ above $\sqrt2$, and its neighbor `1.414213562373095` lies $1.25\cdot10^{-16}$ below it. How the instruction calculates internally is up to the processor. Depending on its design, it determines the square root digit by digit, similar to a calculation with pen and paper, or with a Newton-like iteration, in both cases with enough extra digits to be able to round correctly.
:::

### Exercises for Section [8](#stufe-8)

<span class="anker" id="stufe-8-7"></span>

:::aufgabe Exercise 31 ★ Newton by hand
<span class="anker" id="aufg-31"></span>

Calculate three Newton steps for $\sqrt3$ with the starting value $g_0=2$ by hand, as a fraction and as a decimal number. Calculate the errors $d_0$ to $d_3$ and check Theorem [8.2](#satz-8-2) for $d_1$ and $d_2$. How many steps would bisection on $[1,2]$ need for the same accuracy as $g_3$?

:::loesung
With $g_{n+1}=\frac12(g_n+3/g_n)$:

$$\begin{aligned} g_1&=\tfrac12\bigl(2+\tfrac32\bigr)=\tfrac74=1.75,\\ g_2&=\tfrac12\bigl(\tfrac74+\tfrac{12}7\bigr)=\tfrac{97}{56}\approx1.7321429,\\ g_3&=\tfrac12\bigl(\tfrac{97}{56}+\tfrac{168}{97}\bigr)=\tfrac{18817}{10864}\approx1.7320508100 . \end{aligned}$$

With $\sqrt3=1.7320508075\ldots$, the errors are $d_0=0.26795$, $d_1=0.017949$, $d_2=9.205\cdot10^{-5}$ and $d_3=2.446\cdot10^{-9}$. Theorem [8.2](#satz-8-2): $d_0^2/(2g_0)=0.26795^2/4=0.017949=d_1$ and $d_1^2/(2g_1)=0.017949^2/3.5=9.205\cdot10^{-5}=d_2$. The correct digits grow from 0 through 2 and 4 to 8: `2`, `1.7`, `1.732`, `1.7320508`.

Bisection on $[1,2]$ yields a midpoint with an error of at most $\varepsilon/2$. For $d_3=2.4\cdot10^{-9}$, it needs $\varepsilon\le4.9\cdot10^{-9}$, that is, $\lceil\log_2(1/(4.9\cdot10^{-9}))\rceil=\lceil27.6\rceil=28$ steps instead of three.
:::
:::

:::aufgabe Exercise 32 ★★ The cube root with Newton's method
<span class="anker" id="aufg-32"></span>

The cube root $\sqrt[3]{10}$ is the zero of $f(g)=g^3-10$. Derive the Newton step, write a script with the starting value 10 and the stopping condition $|g^3-10|\le10^{-12}\cdot10$ that prints every step, and compare the result with `10 ** (1/3)`. From which step on do the digits double?

:::loesung
With $f(g)=g^3-10$ and $f'(g)=3g^2$, the step is $g_{n+1}=g_n-\dfrac{g_n^3-10}{3g_n^2}=\dfrac13\Bigl(2g_n+\dfrac{10}{g_n^2}\Bigr)$.

```python kubik_newton.py
# Cube root of 10 with Newton: f(g) = g**3 - a, f'(g) = 3*g**2
a = 10.0
g = a                                     # starting value
schritte = 0
while abs(g ** 3 - a) > 1e-12 * a:
    g = g - (g ** 3 - a) / (3 * g ** 2)
    schritte = schritte + 1
    print(f"Schritt {schritte}: g = {g}")
print("Vergleich 10 ** (1/3):", a ** (1 / 3))
```

```console Linux
$ python3 kubik_newton.py
Schritt 1: g = 6.7
Schritt 2: g = 4.540922254399644
Schritt 3: g = 3.188937050342083
Schritt 4: g = 2.453741355711228
Schritt 5: g = 2.189459564816151
Schritt 6: g = 2.154991996711556
Schritt 7: g = 2.154434834145626
Schritt 8: g = 2.154434690031893
Vergleich 10 ** (1/3): 2.154434690031884
```

Far above the root, $g$ decreases in each step by only about a third, because for large $g$, $\frac13(2g+10/g^2)\approx\frac23g$. From step 5 on, the digits double: the error falls from $3.5\cdot10^{-2}$ through $5.6\cdot10^{-4}$ and $1.4\cdot10^{-7}$ to about $10^{-14}$. The last digits differ from `10 ** (1/3)` because the tolerance $|g^3-10|\le10^{-11}$ allows an error of about $10^{-12}$ in $g$; the result meets the required accuracy.
:::
:::

:::aufgabe Exercise 33 ★★ Newton with a relative tolerance
<span class="anker" id="aufg-33"></span>

Change `wurzel_newton.py` so that the condition reads `abs(g * g - a) > 1e-12 * a` and only the final result is printed. Test it with $a=2$, $a=25$, $a=123456789$ and $a=0.0001$. How many steps does it need in each case? Why does $a=0.0001$ need a few more steps despite being a small number?

:::loesung
```python newton_relativ.py
# Newton for the square root with a relative tolerance: ends for large and small a, too
a = float(input("a = "))
g = max(1.0, a)
schritte = 0
while abs(g * g - a) > 1e-12 * a:
    g = g - (g * g - a) / (2 * g)
    schritte = schritte + 1
print("Näherung:", g, "nach", schritte, "Schritten")
```

```console Linux
$ python3 newton_relativ.py
a = 2
Näherung: 1.4142135623730951 nach 5 Schritten
$ python3 newton_relativ.py
a = 25
Näherung: 5.0 nach 7 Schritten
$ python3 newton_relativ.py
a = 123456789
Näherung: 11111.111060555555 nach 18 Schritten
$ python3 newton_relativ.py
a = 0.0001
Näherung: 0.01 nach 11 Schritten
```

For $a=123456789$, the loop now ends: the allowed deviation is $10^{-12}\cdot a\approx1.2\cdot10^{-4}$, much more than the $1.5\cdot10^{-8}$ that remain. The 18 steps come from the starting value $a$, which lies far above the root; the first steps only halve. For $a=0.0001$, the starting value 1 is a hundred times as large as the root 0.01. Here, too, the first steps only halve, about $\log_2 100\approx7$ times, before quadratic convergence sets in.
:::
:::

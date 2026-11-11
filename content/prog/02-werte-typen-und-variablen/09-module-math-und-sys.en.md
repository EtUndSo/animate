---
title: Modules: `math` and `sys`
pfad: Computer Science / Programming / Python / Values, Types and Variables
adresse: informatik/programmieren/python/werte-typen-und-variablen
knoten: Chapter 2: Values, Types and Variables
order: 6030900
summary: Square root, sine, logarithm, the limits of the type float : Python comes with ready-made functions and values for these, sorted into modules.
tags: module
lang: en
---

<span class="anker" id="stufe-8"></span>

:::zweck
Square root, sine, logarithm, the limits of the type `float`: Python comes with ready-made functions and values for these, sorted into modules. This section shows how to load a module and uses the modules `math` and `sys` to confirm the results of the last sections the ready-made way.
:::

### The module and `import`

<span class="anker" id="stufe-8-1"></span>

Python knows thousands of ready-made functions. If all their names were always present, it would get crowded: two functions with the same name could push each other out, and Python would have to load everything at startup.

**A toolbox you fetch first.** The functions are therefore kept in labeled toolboxes. You fetch a box when you need it and then reach into it by its name: “from the box `math`, the square root”.

:::definition Definition 8.1 (Module)
<span class="anker" id="satz-8-1"></span>

A __module__ is a file with ready-made Python definitions, such as functions and values. The statement `import math` loads the module `math` and binds the name `math` to the module object. You access its contents with a dot: `math.sqrt` is the function `sqrt` from the module `math`.
:::

The dot has the same meaning as with a method (subsection [1.4](objekte-und-typen.html#stufe-1-4)): “the thing attached to this object”. The module object is an object like any other, with the type `module`.

::::beispiel
Before the `import`, Python does not know the name; afterward, only `math` is new, not the names inside it:

```console
>>> math.sqrt(2)
Traceback (most recent call last):
  File "<python-input-0>", line 1, in <module>
    math.sqrt(2)
    ^^^^
NameError: name 'math' is not defined. Did you forget to import 'math'?
>>> import math
>>> math.sqrt(2)
1.4142135623730951
>>> type(math)
<class 'module'>
>>> sqrt(2)
Traceback (most recent call last):
  File "<python-input-4>", line 1, in <module>
    sqrt(2)
    ^^^^
NameError: name 'sqrt' is not defined
```

`math.sqrt(2)` returns the same `float` as `2 ** 0.5` in [Chapter 1, Section 4.5](/wissen/en/informatik/programmieren/python/programme-und-der-python-interpreter/der-interaktive-modus.html#stufe-4-5). An `import` applies until the end of the session or the script; in a script, it usually stands at the very top.
::::

⁠**In short:** `import modul` loads a module and binds its name; `modul.name` accesses its contents.

### The module `math`

<span class="anker" id="stufe-8-2"></span>

For technical calculations, you need the functions from the calculator: square root, exponential function, logarithms, trigonometric functions. The module `math` contains them for `float`.

| Name | Meaning |
|---|---|
| `math.pi`, `math.e` | the numbers $\pi$ and $\mathrm{e}$ as `float` |
| `math.inf`, `math.nan` | the special values `inf` and `nan` |
| `math.sqrt(x)` | square root $\sqrt x$ |
| `math.exp(x)` | $\mathrm{e}^x$ |
| `math.log(x)`, `math.log10(x)` | natural logarithm, base-10 logarithm |
| `math.sin(x)`, `math.cos(x)`, `math.tan(x)` | trigonometric functions, $x$ in radians |
| `math.degrees(x)`, `math.radians(x)` | radians to degrees and back |
| `math.hypot(x, y)` | $\sqrt{x^2+y^2}$ |
| `math.floor(x)`, `math.ceil(x)` | round down, round up to an integer |

::::beispiel
A base-10 logarithm, a value of the exponential function and a sine:

```console
>>> math.log10(1000)
3.0
>>> math.exp(-1)
0.36787944117144233
>>> math.sin(math.radians(30))
0.49999999999999994
>>> math.sin(math.pi)
1.2246467991473532e-16
```

$\mathrm{e}^{-1}\approx36.8\,\%$ occurs, for example, in cooling: the temperature difference between a hot cup of tea and the room shrinks approximately like an exponential function and, after a certain time, has dropped to $\mathrm{e}^{-1}$ of its initial value. The last two lines again show rounding errors: $\sin30^\circ$ is $0.5$, and $\sin\pi$ is 0. But neither $30^\circ$ in radians nor $\pi$ itself is exact as a `float`; `math.pi` is merely the `float` closest to $\pi$.
::::

⁠**In short:** `math` contains the calculator functions for `float`; angles are given in radians.

:::hintergrund Why $\sin\pi$ comes out as $1.22\cdot10^{-16}$ of all values
`math.pi` is slightly smaller than $\pi$: $\texttt{math.pi}=\pi-\delta$ with $\delta\approx1.2246\cdot10^{-16}$. For small $\delta$, $\sin(\pi-\delta)=\sin\delta\approx\delta$. So the function `math.sin` does not calculate wrongly; on the contrary, it returns the sine of the number it received, accurate to the last digit. The result even reveals the representation error of `math.pi`. The error lies in the input, not in the function.
:::

### The tolerance comparison, ready-made: `math.isclose`

<span class="anker" id="stufe-8-3"></span>

You need the comparison with a tolerance from subsection [7.4](wahrheitswerte-und-vergleiche.html#stufe-7-4) so often that `math` comes with it ready-made.

**Ready-made.** `math.isclose(a, b)` checks $|a-b|\le\max\bigl(r\cdot\max(|a|,|b|),\ t_{\mathrm{abs}}\bigr)$ with the relative tolerance $r=10^{-9}$ and the absolute tolerance $t_{\mathrm{abs}}=0$. You pass other tolerances by their names inside the parentheses, as `rel_tol=` and `abs_tol=`:

```console
>>> math.isclose(0.1 + 0.2, 0.3)
True
>>> math.isclose(1e-20, 0.0)
False
>>> math.isclose(1e-20, 0.0, abs_tol=1e-12)
True
>>> math.isclose(718, 750, rel_tol=0.05)
True
>>> math.isclose(math.nan, math.nan)
False
>>> math.isclose(math.inf, math.inf)
True
```

**Comparison.** The expression by hand from subsection [7.4](wahrheitswerte-und-vergleiche.html#stufe-7-4) and `math.isclose` both return `True` for $0.1+0.2$ and $0.3$, and both fail at zero without an absolute tolerance. The ready-made way is shorter, checks the tolerances for sensible values and treats `inf` and `nan` by fixed rules: `nan` is close to nothing, `inf` only to itself.

⁠**In short:** `math.isclose` is the ready-made tolerance comparison with $r=10^{-9}$ and no absolute tolerance.

:::hintergrund Why $10^{-9}$ in particular, and why no absolute tolerance is preset
The default $10^{-9}$ demands about nine matching decimal digits, roughly half of the almost 16 that a `float` has. This leaves room for the rounding errors of many calculation steps, and real differences still stand out. An absolute tolerance, on the other hand, cannot be preset sensibly for all cases, because it has a unit: the same numerical value $10^{-9}$ is tiny for amounts of money in euros, but almost $9500\,\mathrm{km}$ for distances in light-years (subsection [7.4](wahrheitswerte-und-vergleiche.html#stufe-7-4)). That is why it is 0, and if you compare with 0, you have to decide for yourself which order of magnitude counts as “practically zero”.
:::

### The limits of the type `float`, ready-made: `sys.float_info`

<span class="anker" id="stufe-8-4"></span>

Section [5](rechnen-mit-gleitkommazahlen.html#stufe-5) determined machine epsilon and the largest `float` by hand. Python also keeps these numbers ready-made.

**Ready-made.** The module `sys` contains information about the running Python. In it, `sys.float_info` describes the type `float`. In addition, the module `math` has functions for the spacing of neighboring `float` values: `math.ulp(x)` is the distance from $x$ to the next `float` of larger magnitude (*unit in the last place*), and `math.nextafter(x, y)` is the next `float` after $x$ in the direction of $y$:

```console
>>> import sys
>>> sys.float_info.epsilon
2.220446049250313e-16
>>> sys.float_info.max
1.7976931348623157e+308
>>> sys.float_info.min
2.2250738585072014e-308
>>> sys.float_info.mant_dig
53
>>> sys.float_info.dig
15
>>> math.ulp(1.0)
2.220446049250313e-16
>>> math.ulp(1e16)
2.0
>>> math.nextafter(0.1, 1)
0.10000000000000002
```

**Comparison.** All values agree with the results by hand:

| Quantity | by hand | ready-made |
|---|---|---|
| machine epsilon $\varepsilon_{\mathrm M}$ | `2 ** -52` (subsection [5.2](rechnen-mit-gleitkommazahlen.html#stufe-5-2)) | `sys.float_info.epsilon` |
| spacing at $10^{16}$ | $2^{-52}\cdot2^{53}=2$ (subsection [5.2](rechnen-mit-gleitkommazahlen.html#stufe-5-2)) | `math.ulp(1e16)` |
| largest `float` | $(2-2^{-52})\cdot2^{1023}$ (subsection [5.5](rechnen-mit-gleitkommazahlen.html#stufe-5-5)) | `sys.float_info.max` |
| smallest ordinary `float` | $2^{-1022}$ | `sys.float_info.min` |
| digits of the significand | $p=53$ (subsection [4.2](gleitkommazahlen-der-typ-float.html#stufe-4-2)) | `sys.float_info.mant_dig` |

The ready-made way tells you what actually applies on the running computer. The way by hand explains where the numbers come from.

⁠**In short:** `sys.float_info` describes the type `float`, `math.ulp` the spacing of neighboring `float` values; both confirm the calculations by hand.

:::hintergrund When it has to be exact: the modules `fractions` and `decimal`
For calculations that cannot tolerate any rounding error, there are two further modules with number types of their own. `fractions` calculates with fractions of two `int` values, and therefore exactly. `decimal` calculates in the decimal system, as you do on paper; there, $0.1$ is exact, and you can set the number of digits. You pass the value as a string, because a `float` such as `0.1` already carries its representation error. If you pass it in as a `float` anyway, `decimal` shows exactly the stored value, the same digits that the calculation with $5^{55}$ produced in subsection [4.6](gleitkommazahlen-der-typ-float.html#stufe-4-6):

```console
>>> import fractions
>>> fractions.Fraction(1, 10) + fractions.Fraction(2, 10)
Fraction(3, 10)
>>> import decimal
>>> decimal.Decimal("0.1") + decimal.Decimal("0.2")
Decimal('0.3')
>>> decimal.Decimal(0.1)
Decimal('0.1000000000000000055511151231257827021181583404541015625')
```

Both types are considerably slower than `float`, because the processor cannot handle them directly. For measured quantities such as lengths or temperatures, which have only a few significant digits anyway, `float` is the right choice; you need exact types for amounts of money, for example.
:::

### Exercises for Section [8](#stufe-8)

<span class="anker" id="stufe-8-5"></span>

:::aufgabe Exercise 29 ★ Three ways to the hypotenuse
<span class="anker" id="aufg-29"></span>

Calculate $\sqrt{3^2+4^2}$ with `math.sqrt`, with `** 0.5` and with `math.hypot`. In the same way, calculate $\sqrt{x^2+x^2}$ for the `float` `x = 1e200` in all three ways. What goes wrong, and why does `math.hypot` help?

:::loesung
```console
>>> import math
>>> math.sqrt(3 ** 2 + 4 ** 2)
5.0
>>> (3 ** 2 + 4 ** 2) ** 0.5
5.0
>>> math.hypot(3, 4)
5.0
>>> x = 1e200
>>> math.sqrt(x * x + x * x)
inf
>>> math.hypot(x, x)
1.414213562373095e+200
```

For $x=10^{200}$, even $x^2=10^{400}$ is larger than the largest `float`: `x * x` gives `inf`, and $\sqrt\infty=\infty$. With `x ** 2`, the calculation even stops with an `OverflowError` (subsection [5.5](rechnen-mit-gleitkommazahlen.html#stufe-5-5)). The result $\sqrt2\cdot10^{200}$ itself, however, is harmless. `math.hypot` calculates in such a way that no intermediate result overflows. The idea is shown by the transformation $\sqrt{x^2+y^2}=|x|\sqrt{1+(y/x)^2}$ for $|x|\ge|y|$: under the square root, there are only numbers between 1 and 2.
:::
:::

:::aufgabe Exercise 30 ★★ Sound levels in decibels
<span class="anker" id="aufg-30"></span>

Sound consists of small, rapid fluctuations of air pressure. Their strength is called sound pressure and is measured in pascals (Pa). A conversation produces about $0.02\,\mathrm{Pa}$ at a distance of one meter, a lawn mower close by about $1.2\,\mathrm{Pa}$. By how many decibels the loud sound is louder is given by $20\log_{10}(p_\mathrm{loud}/p_\mathrm{quiet})$.

<ol class="al">

<li>

Calculate the difference with variables and `math.log10`.

</li>

<li>

If only half as many cars drive on a road, the noise drops by about $3\,\mathrm{dB}$. By what factor does the sound pressure drop? Solve $20\log_{10}x=-3$ for $x$ and calculate with `10 ** (...)`. Compare with $1/\sqrt2$.

</li>

</ol>

:::loesung
(a)

```console
>>> import math
>>> p_leise = 0.02
>>> p_laut = 1.2
>>> 20 * math.log10(p_laut / p_leise)
35.56302500767287
```

The sound pressure of the lawn mower is 60 times as large; that is $35.6\,\mathrm{dB}$ more.

(b) $20\log_{10}x=-3$ gives $x=10^{-3/20}$:

```console
>>> 10 ** (-3 / 20)
0.7079457843841379
>>> 1 / math.sqrt(2)
0.7071067811865475
```

$-3\,\mathrm{dB}$ is a factor of $0.708$, almost exactly $1/\sqrt2\approx0.707$. This fits the half as many cars: the energy that sound carries through an area per second grows with the square of the sound pressure, and $(1/\sqrt2)^2=\frac12$. Half the energy therefore means the sound pressure times $1/\sqrt2$; exactly, that is $20\log_{10}(1/\sqrt2)\approx-3.01\,\mathrm{dB}$.
:::
:::

:::aufgabe Exercise 31 ★★★ The representation error of $\pi$
<span class="anker" id="aufg-31"></span>

<ol class="al">

<li>

Use the approximation $\sin(\pi-\delta)\approx\delta$ to show that `math.sin(math.pi)` returns approximately the distance $\delta=\pi-\texttt{math.pi}$.

</li>

<li>

The decimal digits of $\pi$ begin with $3.1415926535897932384626433832795028841971$. Determine $\delta$ with `decimal`: write these digits as a string into `decimal.Decimal`, subtract `decimal.Decimal(math.pi)` from it and compare with (a).

</li>

<li>

Is `math.pi` above or below $\pi$? What does the sign of `math.sin(math.pi)` reveal?

</li>

</ol>

:::loesung
(a) `math.pi` is the `float` next to $\pi$, so $\texttt{math.pi}=\pi-\delta$ with a small $\delta$. With $\sin(\pi-\delta)=\sin\delta$ and $\sin\delta\approx\delta$ for small $\delta$, `math.sin(math.pi)` returns the value $\delta$ up to an error of size $\delta^3/6\approx3\cdot10^{-49}$, which lies far below any rounding.

(b)

```console
>>> import math
>>> import decimal
>>> decimal.Decimal("3.1415926535897932384626433832795028841971") - decimal.Decimal(math.pi)
Decimal('1.224646799147353177226065238E-16')
>>> math.sin(math.pi)
1.2246467991473532e-16
```

Both agree in all 17 displayed digits. In its default setting, `decimal` calculates with 28 significant digits; that is why the result ends there.

(c) $\delta$ is positive, so `math.pi` lies *below* $\pi$. The sign of `math.sin(math.pi)` reveals it: the sine is positive to the left of $\pi$.
:::
:::

:::aufgabe Exercise 32 ★ By hand or ready-made?
<span class="anker" id="aufg-32"></span>

Use `sys.float_info` and `math.ulp` to confirm three statements: (a) $\varepsilon_{\mathrm M}=2^{-52}$, (b) the spacing of neighboring `float` values at $2^{53}$ is 2, (c) at $0.1$, it is $2^{-56}$. First justify (b) and (c) with the exponent of the number, as in subsection [5.2](rechnen-mit-gleitkommazahlen.html#stufe-5-2). In each case, calculate the value by hand with `**` and compare with `==`. Why is `==`, as an exception, the right comparison here?

:::loesung
```console
>>> import sys
>>> import math
>>> sys.float_info.epsilon == 2 ** -52
True
>>> math.ulp(2.0 ** 53) == 2
True
>>> math.ulp(0.1) == 2 ** -56
True
```

(b) At $2^{53}$, the exponent is 53, and the spacing is $2^{-52}\cdot2^{53}=2$. (c) $0.1$ lies between $2^{-4}$ and $2^{-3}$; the spacing is $2^{-52}\cdot2^{-4}=2^{-56}$. Here, `==` is the right comparison, because neither side carries a rounding error: all values are powers of two, so they can be represented exactly, and `2 ** -52` is computed exactly. The question is explicitly whether the values agree down to the last bit.
:::
:::

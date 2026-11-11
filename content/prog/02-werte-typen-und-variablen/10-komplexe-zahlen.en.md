---
title: Complex numbers
pfad: Computer Science / Programming / Python / Values, Types and Variables
adresse: informatik/programmieren/python/werte-typen-und-variablen
knoten: Chapter 2: Values, Types and Variables
order: 6031000
summary: With complex numbers, negative numbers have a square root, too, and every point of the plane becomes a single number that you can calculate with.
tags: attribute
lang: en
---

<span class="anker" id="stufe-9"></span>

:::zweck
With complex numbers, negative numbers have a square root, too, and every point of the plane becomes a single number that you can calculate with. This section shows how Python stores complex numbers and how to determine the absolute value and phase by hand and ready-made; at the end, it rotates a point in the plane with a single multiplication.
:::

:::::vorwissen What you need for this: complex numbers

<span class="anker" id="stufe-9-1"></span>

This subsection collects what the chapter uses from the mathematics of complex numbers; it is covered in detail in [HöMa1, Chapter 2](/wissen/en/elektrotechnik/1-semester/hohere-mathematik-1/komplexe-zahlen/komplexe-zahlen.html).

**Real and imaginary part.** A complex number $z=x+\mathrm jy$ consists of the real part $x=\operatorname{Re}z$ and the imaginary part $y=\operatorname{Im}z$, both real numbers. For the imaginary unit, $\mathrm j^2=-1$. Mathematics usually writes it as $i$; this chapter writes $\mathrm j$ because Python writes it that way.

**The complex plane.** You plot $x$ to the right and $y$ upward. Then $z$ is a point of the plane, or an arrow from the origin to this point. The *complex conjugate* of $z$, the number $z^*=x-\mathrm jy$, is its mirror image in the horizontal axis.

**Absolute value and phase.** The absolute value $|z|=\sqrt{x^2+y^2}$ is the length of the arrow. The phase $\varphi$, also called the argument, is the angle of the arrow measured from the positive real axis, positive counterclockwise, with $-\pi<\varphi\le\pi$. It satisfies $\tan\varphi=y/x$, but $\arctan(y/x)$ returns only angles between $-\frac\pi2$ and $\frac\pi2$; if $z$ lies to the left of the vertical axis, you have to add or subtract $\pi$.

**Polar form.** With Euler's formula $\mathrm{e}^{\mathrm j\varphi}=\cos\varphi+\mathrm j\sin\varphi$, you get $z=|z|\,\mathrm{e}^{\mathrm j\varphi}$. When you multiply, the absolute values multiply and the phases add; when you divide, the absolute values divide and the phases subtract.

::::beispiel
$z=3+4\mathrm j$ has $|z|=\sqrt{9+16}=5$ and $\varphi=\arctan\frac43\approx0.9273\approx53.13^\circ$. Its conjugate is $z^*=3-4\mathrm j$, and $z\cdot z^*=9+16=25=|z|^2$.
::::

⁠**In short:** $z=x+\mathrm jy=|z|\,\mathrm{e}^{\mathrm j\varphi}$ with $|z|=\sqrt{x^2+y^2}$ and the phase $\varphi$ as the angle of the arrow.

:::::

### The type `complex`

<span class="anker" id="stufe-9-2"></span>

A point of the plane has two coordinates, a complex number has two parts. Python needs a type that stores both together as one number and calculates with it according to the rules of complex arithmetic.

**A pair of floating-point numbers.** Python stores a complex number as two `float` values side by side, the real part and the imaginary part, and writes the imaginary unit as `j`.

:::definition Definition 9.1 (The type `complex`)
<span class="anker" id="satz-9-1"></span>

An object of type `complex` stores a complex number as a pair of two `float` values, the real part and the imaginary part. A number with an appended `j` is imaginary: `4j` means $4\mathrm j$. The function `complex(x, y)` creates $x+\mathrm jy$.
:::

::::beispiel
`3 + 4j` is a calculation: `int` plus imaginary number gives `complex`. Python displays complex numbers in parentheses:

```console
>>> z = 3 + 4j
>>> z
(3+4j)
>>> type(z)
<class 'complex'>
>>> complex(3, 4)
(3+4j)
>>> 1j * 1j
(-1+0j)
>>> (1 + 2j) * (3 - 4j)
(11+2j)
>>> (1 + 2j) / (3 - 4j)
(-0.2+0.4j)
>>> j
Traceback (most recent call last):
  File "<python-input-7>", line 1, in <module>
    j
NameError: name 'j' is not defined
```

The last input shows a trap: for Python, `j` on its own is a name, not a number. You write the imaginary unit as `1j`. The basic arithmetic operations and `**` work with `complex`; floor division, remainder and the comparisons `<` and `>` do not exist, because complex numbers have no order.
::::

⁠**In short:** `complex` stores the real and imaginary parts as two `float` values; the imaginary unit is written `1j`.

:::hintergrund Why Python writes `j` and not `i`
Mathematics usually writes $i$; engineering and parts of physics write $\mathrm j$, because there $i$ is already taken by another quantity. Python follows these fields. In the discussion of a change request, developers of the language justified this by saying that this notation has long been common there and that switching would break existing programs. Instead of `j`, you may also write `J`, but not `i`.
:::

### The attribute: real and imaginary part

<span class="anker" id="stufe-9-3"></span>

You often want only the real or only the imaginary part of a complex number, for example the horizontal coordinate of a point. You need no calculation for this: both parts are stored ready-made in the object.

**What is attached to the object.** A method is attached to an object and is called with a dot and parentheses (subsection [1.4](objekte-und-typen.html#stufe-1-4)). But simple values can also be attached to an object, and you read them off without parentheses.

:::definition Definition 9.2 (Attribute)
<span class="anker" id="satz-9-2"></span>

An __attribute__ is a name that is attached to an object and accessed with a dot: *object*`.`*name*. Methods are attributes that you call; other attributes are simply values.
:::

This is where the name of the exception `AttributeError` from subsection [1.4](objekte-und-typen.html#stufe-1-4) comes from: no attribute with the requested name was attached to the object.

::::beispiel
`real` and `imag` are attributes that hold the two parts as `float`; `conjugate` is a method and returns the complex conjugate:

```console
>>> z.real
3.0
>>> z.imag
4.0
>>> z.conjugate()
(3-4j)
>>> z * z.conjugate()
(25+0j)
>>> z.real = 5
Traceback (most recent call last):
  File "<python-input-12>", line 1, in <module>
    z.real = 5
    ^^^^^^
AttributeError: readonly attribute
```

The last line shows that the attributes can only be read. A `complex` never changes its value, just like every number (subsection [1.3](objekte-und-typen.html#stufe-1-3)).
::::

⁠**In short:** An attribute is a name attached to an object; `z.real` and `z.imag` return the real and imaginary parts.

### The module `cmath`

<span class="anker" id="stufe-9-4"></span>

The functions from `math` work only with real numbers. That is why `math.sqrt(-1)` is an error, even though $\sqrt{-1}=\mathrm j$ would be a sensible answer.

**A second toolbox.** For complex numbers, there is a module of its own with the same function names. Because each module has its own names, `math.sqrt` and `cmath.sqrt` can exist side by side.

:::definition Definition 9.3 (The module `cmath`)
<span class="anker" id="satz-9-3"></span>

The module `cmath` contains mathematical functions for complex numbers, among them `sqrt`, `exp`, `log`, `sin`, `cos` as well as `phase`, `polar` and `rect` for the polar form. The functions that calculate a value return a `complex`; `phase` returns a `float`, and `polar` two `float` values.
:::

::::beispiel
With `math`, the square root of $-1$ fails:

```console
>>> import math
>>> math.sqrt(-1)
Traceback (most recent call last):
  File "<python-input-1>", line 1, in <module>
    math.sqrt(-1)
    ~~~~~~~~~^^^^
ValueError: expected a nonnegative input, got -1.0
```

In Python 3.13, the description is shorter: `math domain error`. With `cmath`, the square root succeeds, and so does Euler's formula for $\varphi=\pi$. The session with `z` continues here:

```console
>>> import math
>>> import cmath
>>> cmath.sqrt(-1)
1j
>>> cmath.exp(1j * math.pi)
(-1+1.2246467991473532e-16j)
>>> (-1) ** 0.5
(6.123233995736766e-17+1j)
```

$\mathrm{e}^{\mathrm j\pi}$ is $-1$; the imaginary part $1.22\cdot10^{-16}$ is the rounding residue of `math.pi`, the same as with `math.sin(math.pi)` in subsection [8.2](module-math-und-sys.html#stufe-8-2). The last line is a trap: a negative number raised to a non-integer exponent returns a `complex` without any warning, and this one, too, carries a rounding residue in its real part.
::::

⁠**In short:** `cmath` is `math` for complex numbers; there, even $\sqrt{-1}$ has a result.

### Absolute value and phase: first by hand, then ready-made

<span class="anker" id="stufe-9-5"></span>

For a point of the plane, the absolute value and phase often say more than the real and imaginary parts: the absolute value is its distance from the origin, the phase is the direction in which it lies. This is also how you describe a location with “5 km toward the northeast”.

**The arrow.** Fig. [10](#abb-10) shows $z=3+4\mathrm j$ as an arrow. The absolute value is its length, the phase its angle with the real axis. The real and imaginary parts are the two legs of a right triangle, and the absolute value is the hypotenuse.

:::abbildung prog/k2zeiger 10
The complex number $z=3+4\mathrm j$ as an arrow in the complex plane, dashed: the complex conjugate $z^*$. On the right: the Python expression that gives each quantity.
:::

**By hand.** The Pythagorean theorem gives the absolute value. For the phase, `math` has the function `math.atan2(y, x)`: it receives the imaginary and real parts separately, in this order, and can therefore determine the correct quadrant. `math.atan(y / x)` sees only the quotient and returns the same angle for $-3-4\mathrm j$ as for $3+4\mathrm j$:

```console
>>> (z.real ** 2 + z.imag ** 2) ** 0.5
5.0
>>> math.atan2(z.imag, z.real)
0.9272952180016122
>>> math.degrees(math.atan2(z.imag, z.real))
53.13010235415598
>>> w = -3 - 4j
>>> math.atan(w.imag / w.real)
0.9272952180016122
>>> math.atan2(w.imag, w.real)
-2.214297435588181
```

$-2.2143$ is $-126.87^\circ$: the arrow of $w$ points to the lower left, and that is correct.

**Ready-made.** For a `complex`, the built-in function `abs` returns the absolute value, `cmath.phase` the phase, and `cmath.polar` both at once. `cmath.rect` turns the absolute value and phase back into the real and imaginary parts:

```console
>>> abs(z)
5.0
>>> cmath.phase(z)
0.9272952180016122
>>> cmath.phase(w)
-2.214297435588181
>>> cmath.polar(z)
(5.0, 0.9272952180016122)
>>> cmath.rect(5, 0.9272952180016122)
(3.0000000000000004+3.9999999999999996j)
```

**Comparison.** By hand and ready-made give the same `float` values: $5.0$ for the absolute value, $0.9272952180016122$ and $-2.214297435588181$ for the phases. `cmath.phase` chooses the quadrant itself and always returns an angle from $-\pi$ to $\pi$. The way back with `rect` hits $3+4\mathrm j$ except for rounding residues in the last digit, because the cosine and sine of the rounded phase are rounded again.

⁠**In short:** The absolute value by hand with Pythagoras, the phase with `math.atan2(y, x)`; ready-made with `abs`, `cmath.phase` and `cmath.polar`.

### Application: rotating a point in the plane

<span class="anker" id="stufe-9-6"></span>

With variables, `math` and `complex`, you can now solve a problem from geometry completely in Python. Games, maps and drawing programs constantly rotate points about a center. With complex numbers, every such rotation is a single multiplication.

**The idea.** The center lies at the origin, the point at $z$. The number $\mathrm{e}^{\mathrm j\alpha}$ has the absolute value 1 and the phase $\alpha$. When you multiply, the absolute values multiply and the phases add (subsection [9.1](#stufe-9-1)). That is why

$$z_{\mathrm{new}}=z\cdot\mathrm{e}^{\mathrm j\alpha}$$

has the same absolute value as $z$, and its phase is larger by $\alpha$: the point has rotated by the angle $\alpha$ about the origin, counterclockwise for $\alpha>0$, clockwise for $\alpha<0$. In Python, `cmath.rect(1, alpha)` returns the number $\mathrm{e}^{\mathrm j\alpha}$, with $\alpha$ in radians.

**The clock.** A clock app draws the minute hand as an arrow from the center of the clock to the tip of the hand. The hand is 10 cm long and points straight up at 12:00; its tip is then at $z=10\mathrm j$. Every minute, it rotates by $6^\circ$ clockwise, so after $m$ minutes by $\alpha=-6^\circ\cdot m$. Where is the tip at 12:20?

```console
>>> spitze = 10j
>>> m = 20
>>> drehung = cmath.rect(1, math.radians(-6 * m))
>>> drehung
(-0.4999999999999998-0.8660254037844387j)
>>> spitze_neu = spitze * drehung
>>> spitze_neu
(8.660254037844387-4.999999999999998j)
>>> abs(spitze_neu)
10.0
>>> math.degrees(cmath.phase(spitze_neu))
-29.999999999999993
>>> math.degrees(cmath.phase(spitze_neu / spitze))
-119.99999999999999
```

At 12:20, the tip lies $8.66$ cm to the right of the center and 5 cm below it, where the 4 is on the dial (Fig. [11](#abb-11)). Its distance from the center is still 10 cm, and its phase is $-30^\circ$: $90^\circ$ at the start, turned back by $120^\circ$. If you divide the new position by the old one, the phases subtract, and what remains is the angle of rotation, $-120^\circ$. The residues in the last digits come from `math.pi` in `math.radians` and from the cosine and sine that `cmath.rect` calculates.

:::abbildung prog/k2drehen 11
The minute hand as an arrow in the complex plane, with the center of the clock at the origin; the tick marks indicate the twelve hours. At 12:00, the tip is at $z=10\mathrm j$, at 12:20 at $8.66-5\mathrm j$. Multiplying by $\mathrm{e}^{\mathrm j\alpha}$, $\alpha=-120^\circ$, rotates the arrow clockwise and leaves its length unchanged.
:::

As a script with comments and units:

```python drehen.py
# Minute hand of a clock: position of the tip m minutes after 12:00
import cmath
import math

laenge = 10.0    # length of the hand in cm
m = 20           # minutes after 12:00

spitze = laenge * 1j                 # at 12:00 it points up
alpha = math.radians(-6 * m)         # minus: clockwise
spitze_neu = spitze * cmath.rect(1, alpha)   # rotate = multiply

print("Spitze in cm:", spitze_neu)
print("Abstand vom Mittelpunkt in cm:", abs(spitze_neu))
print("Phase in Grad:", math.degrees(cmath.phase(spitze_neu)))
```

```console Linux
$ python3 drehen.py
Spitze in cm: (8.660254037844387-4.999999999999998j)
Abstand vom Mittelpunkt in cm: 10.0
Phase in Grad: -29.999999999999993
```

For a different time, you change only the line with `m`. On Windows (`py drehen.py`), the same output appears. That is not a matter of course: Python calculates the cosine and sine in `cmath.rect` and the absolute value in `abs` with functions from the system library, and these do not round the same way on every system. With other numbers, the last digit therefore differs between Windows and Linux; Exercise [35](#aufg-35) shows an example.

⁠**In short:** `z * cmath.rect(1, alpha)` rotates the point $z$ by the angle $\alpha$ about the origin; `abs` and `cmath.phase` show its distance and direction.

### Exercises for Section [9](#stufe-9)

<span class="anker" id="stufe-9-7"></span>

:::aufgabe Exercise 33 ★ Calculating with `complex`
<span class="anker" id="aufg-33"></span>

Predict and check: (a) `(2 + 3j) + (1 - 1j)`, (b) `(2 + 3j) * 1j`, (c) `(1 + 1j) ** 2`, (d) `abs(-5j)`, (e) `(3 + 4j).conjugate().imag`. Interpret (b) using the arrow: what does multiplying by $\mathrm j$ do?

:::loesung
```console
>>> (2 + 3j) + (1 - 1j)
(3+2j)
>>> (2 + 3j) * 1j
(-3+2j)
>>> (1 + 1j) ** 2
2j
>>> abs(-5j)
5.0
>>> (3 + 4j).conjugate().imag
-4.0
```

(a) The real parts and the imaginary parts add up. (b) $(2+3\mathrm j)\mathrm j=2\mathrm j+3\mathrm j^2=-3+2\mathrm j$. Using the arrow: $\mathrm j=\mathrm{e}^{\mathrm j\pi/2}$ has absolute value 1 and phase $90^\circ$; the multiplication rotates the arrow by $90^\circ$ counterclockwise and leaves its length unchanged. (c) $(1+\mathrm j)^2=1+2\mathrm j+\mathrm j^2=2\mathrm j$; Python displays a purely imaginary number without a real part. (d) The absolute value of $-5\mathrm j$ is 5. (e) Conjugating flips the sign of the imaginary part.
:::
:::

:::aufgabe Exercise 34 ★★ The correct quadrant
<span class="anker" id="aufg-34"></span>

Determine the phase of $1+\mathrm j$, $-1+\mathrm j$, $-1-\mathrm j$ and $1-\mathrm j$ in degrees, once with `math.atan` of $y/x$ and once with `cmath.phase`. For which numbers do the results differ, and by how much?

:::loesung
```console
>>> import math
>>> import cmath
>>> math.degrees(math.atan(1 / 1)), math.degrees(cmath.phase(1 + 1j))
(45.0, 45.0)
>>> math.degrees(math.atan(1 / -1)), math.degrees(cmath.phase(-1 + 1j))
(-45.0, 135.0)
>>> math.degrees(math.atan(-1 / -1)), math.degrees(cmath.phase(-1 - 1j))
(45.0, -135.0)
>>> math.degrees(math.atan(-1 / 1)), math.degrees(cmath.phase(1 - 1j))
(-45.0, -45.0)
```

With a comma between two expressions, the interactive mode displays both values side by side. For $1+\mathrm j$ and $1-\mathrm j$, to the right of the vertical axis, both ways agree. For $-1+\mathrm j$ and $-1-\mathrm j$, `atan` is off by $180^\circ$: the quotient $y/x$ is the same as for the number opposite, but the arrow points in the opposite direction. `cmath.phase` and `math.atan2` both see the two parts separately and choose the correct quadrant.
:::
:::

:::aufgabe Exercise 35 ★★ More positions of the hands
<span class="anker" id="aufg-35"></span>

<ol class="al">

<li>

The hour hand of the same clock is 6 cm long and points horizontally to the right at 3:00; its tip is then at $z=6$. Every hour, it rotates by $30^\circ$ clockwise. Calculate the position of its tip at 5:00, its distance from the center and its phase in degrees.

</li>

<li>

After how many minutes does the minute hand from subsection [9.6](#stufe-9-6) first point exactly diagonally up and to the right, so that the real and imaginary parts of its tip are equal? What phase does the tip have then? Check with Python, using a suitable comparison.

</li>

</ol>

:::loesung
(a) At 5:00, the hour hand has rotated by two hours since 3:00, that is, by $\alpha=-2\cdot30^\circ=-60^\circ$:

```console
>>> import math
>>> import cmath
>>> stunde = 6
>>> stunde_neu = stunde * cmath.rect(1, math.radians(-30 * 2))
>>> stunde_neu
(3.000000000000001-5.196152422706632j)
>>> abs(stunde_neu)
6.000000000000001
>>> math.degrees(cmath.phase(stunde_neu))
-59.99999999999999
```

The tip lies at $(3-5.196\,\mathrm j)$ cm, that is, 3 cm to the right of and $5.2$ cm below the center, where the 5 is. Its distance from the center is 6 cm and its phase $-60^\circ$, both up to rounding residues in the last digit.

(b) The real and imaginary parts are equal and positive when the phase is $45^\circ$. The tip starts at $90^\circ$ and loses $6^\circ$ per minute; so it reaches $45^\circ$ after $45/6=7.5$ minutes, at 12:07:30. Because the real and imaginary parts are rounded values, you check their equality with a tolerance:

```console
>>> spitze_neu = 10j * cmath.rect(1, math.radians(-6 * 7.5))
>>> math.isclose(spitze_neu.real, spitze_neu.imag)
True
```

Python displays the two parts themselves differently depending on the system; on Windows, like this:

```console
>>> spitze_neu
(7.0710678118654755+7.0710678118654755j)
>>> math.degrees(cmath.phase(spitze_neu))
45.0
```

On Linux, like this:

```console
>>> spitze_neu
(7.071067811865475+7.0710678118654755j)
>>> math.degrees(cmath.phase(spitze_neu))
45.00000000000001
```

Mathematically, both parts are $10\cdot\frac{\sqrt2}2\approx7.07$, and the phase is $45^\circ$. But `cmath.rect` calculates the cosine and sine with the system library (subsection [9.6](#stufe-9-6)), and on Linux, the real part comes out slightly smaller in the last digit. A comparison with `==` would therefore have returned `True` on Windows and `False` on Linux; the comparison with a tolerance returns `True` everywhere.
:::
:::

:::aufgabe Exercise 36 ★★★ A quadratic equation without a real solution
<span class="anker" id="aufg-36"></span>

The equation $x^2+x+1=0$ has no real solution: in the quadratic formula $x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$, the number under the square root is $1-4=-3$. Calculate both complex solutions with `cmath.sqrt`, together with their absolute value and phase in degrees. Substitute them into the equation and check that they satisfy it, using a suitable comparison.

:::loesung
With $a=b=c=1$, the number under the square root is $b^2-4ac=-3$, and `cmath.sqrt` returns $\sqrt3\,\mathrm j$:

```console
>>> import math
>>> import cmath
>>> a = 1
>>> b = 1
>>> c = 1
>>> w = cmath.sqrt(b ** 2 - 4 * a * c)
>>> w
1.7320508075688772j
>>> x1 = (-b + w) / (2 * a)
>>> x2 = (-b - w) / (2 * a)
>>> x1
(-0.5+0.8660254037844386j)
>>> x2
(-0.5-0.8660254037844386j)
>>> math.degrees(cmath.phase(x1))
120.00000000000001
>>> math.degrees(cmath.phase(x2))
-120.00000000000001
>>> rest = a * x1 ** 2 + b * x1 + c
>>> rest
(1.1102230246251565e-16+0j)
>>> rest == 0
False
>>> abs(rest) <= 1e-12
True
>>> abs(a * x2 ** 2 + b * x2 + c) <= 1e-12
True
```

The solutions are $x_{1,2}=-\frac12\pm\frac{\sqrt3}2\,\mathrm j$ with the phases $\pm120^\circ$. The phases fit Vieta's formulas, according to which $x_1x_2=\frac ca=1$: phases add up when you multiply, and $120^\circ+(-120^\circ)=0^\circ$ is the phase of the number 1. When you substitute the solutions, a residue of $1.1\cdot10^{-16}$ remains: rounding residues from several calculation steps, because $\frac{\sqrt3}2$ is not exact as a `float`. `==` therefore returns `False`. The comparison is with 0, so the relative comparison fails as well (subsection [7.4](wahrheitswerte-und-vergleiche.html#stufe-7-4)). The suitable comparison is the one with an absolute tolerance, for complex numbers using the absolute value. $10^{-12}$ lies far above the rounding residues of numbers of size 1 and far below anything that would count as a real deviation.

The absolute value of both solutions is exactly 1, because $\frac14+\frac34=1$. Python displays it differently depending on the system; on Windows, like this:

```console
>>> abs(x1)
0.9999999999999999
```

On Linux, like this:

```console
>>> abs(x1)
1.0
```

Python calculates the absolute value of a complex number with a function from the system library, and this function does not round the same way on every system (subsection [9.6](#stufe-9-6)).
:::
:::

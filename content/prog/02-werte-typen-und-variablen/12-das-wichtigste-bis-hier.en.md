---
title: Key points so far
pfad: Computer Science / Programming / Python / Values, Types and Variables
adresse: informatik/programmieren/python/werte-typen-und-variablen
knoten: Chapter 2: Values, Types and Variables
order: 6031200
summary: Integers, floating-point numbers and complex numbers, names for objects, text, input and output
tags: 
lang: en
---

:::kern Key points so far
<ul>

<li>

Every value is an object with a type, an identity and a value; `type` and `id` show the type and identity. The type determines what is allowed; you call methods with `objekt.name()`.

</li>

<li>

`int` is exact and of arbitrary size. `/` always returns a `float`; `//` rounds toward $-\infty$, and $a=(a\,/\!/\,b)\cdot b+a\,\%\,b$ holds, with the remainder taking the sign of $b$. `**` comes before the sign and groups from the right.

</li>

<li>

Binary number: $\sum b_i2^i$; bit, byte (8 bits, 0 to 255), hexadecimal (4 bits per digit). A fraction terminates in binary exactly when its denominator in lowest terms is a power of two; $0.1=0.0\,0011\,0011\ldots{}_2$.

</li>

<li>

`float` = binary64: $x=(-1)^s(1+t/2^{52})\cdot2^{c-1023}$, 53 digits of significand, range up to $1.8\cdot10^{308}$. What is stored is the nearest `float`, in a tie the one with the even significand; `0.1` is $3602879701896397/2^{55}$. What is displayed is the shortest decimal number that gives the same `float`.

</li>

<li>

Every calculation is rounded, relatively by at most $\varepsilon_{\mathrm M}/2=2^{-53}$; $\varepsilon_{\mathrm M}=2^{-52}\approx2.2\cdot10^{-16}$. Errors add up, small summands are absorbed, almost equal numbers cancel. Overflow gives `inf`, invalid calculations give `nan`.

</li>

<li>

An assignment binds a name to an object and copies nothing. Names: letters, digits, `_`, no digit at the start, no keyword. `x += a` means `x = x + (a)`.

</li>

<li>

Comparisons return `bool`. You compare floating-point numbers with a tolerance, $|a-b|\le\max(r\max(|a|,|b|),t_{\mathrm{abs}})$, ready-made with `math.isclose`. `is` checks the identity, for example `x is None`.

</li>

<li>

`import modul` binds a module name; `math` for real functions, `cmath` for complex ones, `sys.float_info` for the limits of the `float`.

</li>

<li>

`complex`: two `float` values, imaginary unit `1j`, attributes `real` and `imag`; absolute value `abs`, phase `cmath.phase` or, by hand, `math.atan2(y, x)`.

</li>

<li>

Text: `+` concatenates, `*` repeats, `len` counts; f-strings with format specifiers; `input` always returns `str`; `int`, `float`, `str` convert; `round` rounds to the nearest number, for halves to the even one.

</li>

</ul>
:::

:::merke The answer in three sentences
<ol>

<li>

Every value is an object whose type determines how the value is stored and what you can do with it; names are only tags that an assignment attaches to objects.

</li>

<li>

An `int` stores integers exactly with any number of digits, while a `float` stores every number as a binary fraction with 53 digits times a power of two; that is why even $0.1$ is only approximated and every result of a calculation is rounded, relatively by up to $2^{-53}$.

</li>

<li>

From this follow the working rules: compare floating-point numbers with a tolerance, expect rounding errors over many steps and when subtracting almost equal numbers, and convert text and numbers into each other explicitly.

</li>

</ol>
:::

**One principle behind all the results.** Almost everything in this chapter follows from the fact that the type of an object determines how its value is stored in memory: as a sequence of digits of any length, as a binary fraction with 53 digits and an exponent, as a pair of such binary fractions or as a sequence of characters. The rules of calculation follow from this representation.

| Result | Where it comes from |
|---|---|
| `"2" + 3` is an error | the type determines what `+` means (Sections [1](objekte-und-typen.html#stufe-1) and [10](zeichenketten-eingabe-und-ausgabe.html#stufe-10)) |
| `int` never overflows | digits in base $2^{30}$, as many as needed (Section [2](ganze-zahlen-und-rechenoperatoren.html#stufe-2)) |
| `//` and `%` round toward $-\infty$ | for $b>0$, the remainder should lie between 0 and $b-1$ (Section [2](ganze-zahlen-und-rechenoperatoren.html#stufe-2)) |
| $0.1$ is not exact | the denominator 10 contains the prime factor 5, a `float` only powers of two (Sections [3](zahlen-im-binarsystem.html#stufe-3) and [4](gleitkommazahlen-der-typ-float.html#stufe-4)) |
| `0.1` is displayed as `0.1` | shortest decimal number that gives the same `float` (Section [4](gleitkommazahlen-der-typ-float.html#stufe-4)) |
| the spacing of `float` values grows with their magnitude | fixed number of 53 significand digits (Sections [4](gleitkommazahlen-der-typ-float.html#stufe-4) and [5](rechnen-mit-gleitkommazahlen.html#stufe-5)) |
| `0.1 + 0.2 != 0.3` | every calculation is rounded, here a tie resolved to the even significand (Sections [5](rechnen-mit-gleitkommazahlen.html#stufe-5) and [7](wahrheitswerte-und-vergleiche.html#stufe-7)) |
| comparison with a tolerance | rounding errors are relative to the magnitude (Sections [7](wahrheitswerte-und-vergleiche.html#stufe-7) and [8](module-math-und-sys.html#stufe-8)) |
| `y = x` does not copy | names are tags on objects (Section [6](variablen-namen-fur-objekte.html#stufe-6)) |
| `abs` and `cmath.phase` for points of the plane | `complex` is a pair of `float` values (Section [9](komplexe-zahlen.html#stufe-9)) |
| `round(2.5)` gives 2 | rounding to the even number, the same rule as when storing (Section [10](zeichenketten-eingabe-und-ausgabe.html#stufe-10)) |

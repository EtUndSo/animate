---
title: Calculating with floating-point numbers
pfad: Computer Science / Programming / Python / Values, Types and Variables
adresse: informatik/programmieren/python/werte-typen-und-variablen
knoten: Chapter 2: Values, Types and Variables
order: 6030600
summary: Not only typing in a number, but every calculation with float is rounded.
tags: rounding error, Machine epsilon, absorbed, Cancellation, overflow
lang: en
---

<span class="anker" id="stufe-5"></span>

:::zweck
Not only typing in a number, but every calculation with `float` is rounded. This section determines how large this error can be at most, when it becomes visible and what happens when a result becomes too large or invalid.
:::

### The rounding error of a calculation

<span class="anker" id="stufe-5-1"></span>

The sum of two `float` values generally has more binary digits than a `float` can hold. Python has to squeeze the result of every calculation back into the format.

**Calculate exactly, then round.** You can imagine that the processor forms the exact result from the two stored values, with as many digits as necessary, and then rounds it to the nearest `float`.

:::definition Definition 5.1 (Correctly rounded calculation)
<span class="anker" id="satz-5-1"></span>

For the basic arithmetic operations $+$, $-$, $\cdot$, $/$ and the square root, IEEE 754 requires: the result is the exact result of the stored values, rounded by the same rule as when storing, that is, to the nearest `float` and, in a tie, to the even significand. The difference that arises is called the __rounding error__ of the calculation.
:::

::::beispiel $0.1+0.2$
The stored values are slightly larger than $0.1$ and $0.2$. Their exact sum is

$$0.3000000000000000166533453693773481063544750213623046875 .$$

It lies between two neighboring `float` values:

|  |  |
|---|---|
| left neighbor, the `float` for `0.3` | $0.299999999999999988897769753748434595763683319091796875$ |
| exact sum | $0.3000000000000000166533453693773481063544750213623046875$ |
| right neighbor, displayed as `0.30000000000000004` | $0.3000000000000000444089209850062616169452667236328125$ |

The two distances are exactly equal, $2.78\cdot10^{-17}$: a tie. The rule decides in favor of the even significand. The significand field of the left neighbor ends in `3`, that is, in the bit 1; that of the right neighbor ends in `4`, that is, in the bit 0. That is why the result is the right neighbor, and `0.1 + 0.2` is not the `float` that Python stores for `0.3`.
::::

::::beispiel ten times $0.1$
With many calculation steps, every intermediate result is rounded, and the errors can add up. With the underscore `_` for the last result ([Chapter 1, Section 4.4](/wissen/en/informatik/programmieren/python/programme-und-der-python-interpreter/der-interaktive-modus.html#stufe-4-4)) and the up arrow key, you add $0.1$ ten times in interactive mode:

```console
>>> 0.1
0.1
>>> _ + 0.1
0.2
>>> _ + 0.1
0.30000000000000004
>>> _ + 0.1
0.4
>>> _ + 0.1
0.5
>>> _ + 0.1
0.6
>>> _ + 0.1
0.7
>>> _ + 0.1
0.7999999999999999
>>> _ + 0.1
0.8999999999999999
>>> _ + 0.1
0.9999999999999999
>>> 0.1 * 10
1.0
```

After ten additions, one unit in the last place is still missing to reach 1. The multiplication `0.1 * 10`, on the other hand, is a single calculation step, and its exact result lies so close to 1 that rounding hits 1 exactly. The same quantity, calculated in two ways, gives two different `float` values.
::::

⁠**In short:** Every calculation is computed exactly and then rounded; the errors of individual steps can add up over many steps.

:::hintergrund Forming sums more accurately: compensated summation
When you add a small value to a large intermediate sum, the trailing digits of the small value are lost. In 1965, the mathematician William Kahan proposed computing this lost rest at each step and collecting it in a second number, the correction: you compute the new sum, subtract the old sum from it and compare the result with the value you wanted to add. The difference is exactly what rounding swallowed. In 1974, Arnold Neumaier improved the method for the case that a summand is larger than the sum so far.

Python uses this method: the built-in function `sum`, which adds many values at once, has worked with Neumaier's correction since Python 3.12 and gives exactly `1.0` for ten times $0.1$. If you want to see the rounding error in summation, you therefore have to add step by step as above. Older teaching texts that show the error with `sum` apply to Python up to 3.11.
:::

### Machine epsilon

<span class="anker" id="stufe-5-2"></span>

How large can a rounding error be at most? That depends on the spacing of neighboring `float` values, and you can read this spacing off particularly easily at one place: at 1.

**The first step after 1.** $1=1.000\ldots0_2\cdot2^0$ has the significand field 0. The next larger `float` has a 1 in the last, the 52nd, position of the significand field. It is larger by $2^{-52}$.

:::definition Definition 5.2 (Machine epsilon)
<span class="anker" id="satz-5-2"></span>

__Machine epsilon__ $\varepsilon_{\mathrm M}$ is the distance from 1 to the next larger `float`:

$$\varepsilon_{\mathrm M}=2^{-52}\approx2.22\cdot10^{-16}.$$
:::

:::satz Theorem 5.3 (Size of the rounding error)
<span class="anker" id="satz-5-3"></span>

If a number $x\ne0$ lies in the range of the ordinary `float` values, the rounded value $\tilde x$ differs from $x$ by at most

$$|\tilde x-x|\le\frac{\varepsilon_{\mathrm M}}{2}\,|x|=2^{-53}\,|x|\approx1.11\cdot10^{-16}\,|x| .$$

So a `float` has about 16 significant decimal digits.
:::

:::beweis half the spacing
Let $2^E\le|x|<2^{E+1}$. In this range, all `float` values have the exponent $E$, and their significands differ in steps of $2^{-52}$. So neighboring `float` values there have the spacing $2^{-52}\cdot2^E$. When rounding to the nearest, the error is at most half the spacing: $|\tilde x-x|\le2^{-53}\cdot2^E\le2^{-53}\,|x|$, because $2^E\le|x|$.
:::

::::beispiel
If you add the value $2^{-52}$ to 1, you get the neighbor of 1. If you add only half of it, $2^{-53}$, the exact result lies exactly halfway between 1 and the neighbor, and rounding to the even significand gives 1 again:

```console
>>> 1.0 + 2 ** -52
1.0000000000000002
>>> 1.0 + 2 ** -53
1.0
>>> 2 ** -52
2.220446049250313e-16
```

The spacing grows with the number. At $10^{16}$, it is already 2: $10^{16}$ lies between $2^{53}$ and $2^{54}$, so the spacing is $2^{-52}\cdot2^{53}=2$. The number $10^{16}+1$ cannot exist as a `float`:

```console
>>> 1e16 + 1
1e+16
>>> 1e16 + 2
1.0000000000000002e+16
>>> 2 ** 53 + 1.0
9007199254740992.0
```

The last line shows one consequence of this: all integers up to $2^{53}=9\,007\,199\,254\,740\,992$ are exact as `float` values; above that, not every one is.
::::

**The observation from [Chapter 1](/wissen/en/informatik/programmieren/python/programme-und-der-python-interpreter/programme-und-der-python-interpreter.html).** Heron's recipe ended at `1.414213562373095`, while the ready-made way `2 ** 0.5` gave `1.4142135623730951` ([Chapter 1, Section 4.5](/wissen/en/informatik/programmieren/python/programme-und-der-python-interpreter/der-interaktive-modus.html#stufe-4-5)). Between 1 and 2, neighboring `float` values have exactly the spacing $\varepsilon_{\mathrm M}$, and that is how far apart the two results are:

```console
>>> 1.4142135623730951 - 1.414213562373095
2.220446049250313e-16
```

So the two ways land on neighboring `float` values, one smallest step apart. Each pass of the recipe rounds several times, and the rounding errors make it come to rest one step away from the `float` closest to $\sqrt2$.

⁠**In short:** $\varepsilon_{\mathrm M}=2^{-52}$ is the distance from 1 to the next `float`; each rounding changes a number by at most the fraction $\varepsilon_{\mathrm M}/2$ of its magnitude.

### Absorption

<span class="anker" id="stufe-5-3"></span>

In mathematics, $(a+b)-a=b$. With `float`, something completely different can come out if $a$ and $b$ differ greatly in size.

**A grain of sand on a truck scale.** If you put a grain of sand on a scale that displays weights in steps of 10 kg, the display does not change. The grain of sand is there, but the scale cannot represent it.

:::definition Definition 5.4 (Absorption)
<span class="anker" id="satz-5-4"></span>

If $|b|$ is smaller than half the spacing of the `float` values near $a$, then $a+b$ gives $a$ again: the small summand is lost completely. It is said to be __absorbed__.
:::

::::beispiel
At $10^{16}$, the spacing is 2, and 1 is exactly half the spacing. The tie is rounded to the even significand, and that is $10^{16}$ itself:

```console
>>> 1e16 + 1 - 1e16
0.0
>>> 1e16 - 1e16 + 1
1.0
```

The same three numbers, combined in a different order, give different results. So with `float`, the associative law of addition does not hold: it matters what you calculate first. If you add many small values to a large one, you should add up the small ones first.
::::

⁠**In short:** A summand that is smaller than half the spacing of the `float` values near the other summand disappears in the addition.

### Cancellation

<span class="anker" id="stufe-5-4"></span>

If you subtract two almost equal numbers from each other to obtain a small difference, the result can be much less accurate than the two numbers. Weighing a letter by stepping on the bathroom scale once with it and once without it works poorly for the same reason: two large, slightly inaccurate readings give a small, very inaccurate difference.

**The leading digits cancel.** $1.0000000000000011$ minus $1$: the first 15 decimal places are equal and disappear. Only the last digits remain, and they are exactly where the rounding error of the input sits.

:::definition Definition 5.5 (Cancellation)
<span class="anker" id="satz-5-5"></span>

__Cancellation__ is the loss of significant digits when you subtract two almost equal numbers that already carry rounding errors. The subtraction itself is often exact; but the existing errors become large relative to the small result.
:::

::::beispiel
$1+10^{-15}$ is rounded to a multiple of $2^{-52}$ when it is stored. If you subtract 1 again, you see exactly this rounding:

```console
>>> (1 + 1e-15) - 1
1.1102230246251565e-15
```

The result should be $10^{-15}$ but is 11 % too large. The error in storing $1+10^{-15}$ was tiny, relative to 1 about $10^{-16}$. Relative to the result $10^{-15}$, however, the same error is huge. Of the 16 significant digits, only one is still correct after the subtraction.
::::

⁠**In short:** When you subtract almost equal, rounded numbers, only the erroneous trailing digits remain.

### Overflow: `inf`

<span class="anker" id="stufe-5-5"></span>

The exponent field has 11 bits; the largest exponent is 1023. What happens when a result becomes larger than the largest `float`?

**A value for “too large”.** IEEE 754 has reserved a value of its own for this: infinity. It is stored with the exponent field $c=2047$ and the significand field 0.

:::definition Definition 5.6 (Overflow and `inf`)
<span class="anker" id="satz-5-6"></span>

The largest `float` is $(2-2^{-52})\cdot2^{1023}\approx1.797\cdot10^{308}$. If the rounded result of a calculation is larger, this is called __overflow__, and the result is the special value `inf` (infinity), for negative results `-inf`.
:::

::::beispiel
A number in the source code that is too large also becomes `inf`. Python continues to calculate with `inf` as with $\infty$:

```console
>>> 1e308 * 10
inf
>>> 1e309
inf
>>> -1e309
-inf
>>> 1e309 + 1
inf
>>> 1 / 1e309
0.0
```

The power operator `**` behaves differently: in an overflow, it raises the exception `OverflowError` instead of returning `inf`. The description comes from the operating system and reads `(34, 'Result too large')` on Windows and `(34, 'Numerical result out of range')` on Linux:

```console
>>> 2.0 ** 1024
Traceback (most recent call last):
  File "<python-input-0>", line 1, in <module>
    2.0 ** 1024
    ~~~~^^~~~~~
OverflowError: (34, 'Numerical result out of range')
```
::::

⁠**In short:** Results above $1.797\cdot10^{308}$ become `inf`; Python continues to calculate with `inf` as with $\infty$, only `**` raises an `OverflowError`.

:::hintergrund At the other end: what happens to very small numbers
The smallest ordinary `float` is $2^{-1022}\approx2.2\cdot10^{-308}$. Without special provisions, the numbers would end abruptly below it, and between 0 and $2^{-1022}$ there would be a gap like the one between 0 and $0.5$ in Fig. [6](gleitkommazahlen-der-typ-float.html#abb-6). IEEE 754 fills this gap with the exponent field $c=0$: then the leading 1 of the significand is missing, and the numbers lie at equal spacing of $2^{-1074}$ all the way down to 0. They have fewer significant digits the closer they come to 0; in return, a result sinks gradually toward 0 instead of suddenly dropping to 0. The smallest positive `float` is $2^{-1074}\approx4.9\cdot10^{-324}$, and Python displays it as `5e-324`. A result at most half that size becomes 0: `1e-300 * 1e-300` gives `0.0`. Zero itself also has the exponent field $c=0$, with significand field 0, and it exists with both signs, `0.0` and `-0.0`; in comparisons, both count as equal.
:::

### The invalid result: `nan`

<span class="anker" id="stufe-5-6"></span>

What is $\infty-\infty$? There is no meaningful number as an answer. Nevertheless, a long calculation should not simply come to a halt at this point.

**A placeholder for “not a number”.** IEEE 754 reserves a second special value for this: exponent field $c=2047$ and a significand field other than 0.

:::definition Definition 5.7 (`nan`)
<span class="anker" id="satz-5-7"></span>

`nan` (short for *not a number*) is the `float` that a calculation without a meaningful result returns, for example $\infty-\infty$ or $0\cdot\infty$. Almost every calculation with `nan` gives `nan` again.
:::

::::beispiel
Two calculations without a meaningful result, then one that passes the `nan` on:

```console
>>> 1e309 - 1e309
nan
>>> 0 * 1e309
nan
>>> 1e309 - 1e309 + 1
nan
```

A `nan` at the end of a long calculation indicates that something invalid happened somewhere along the way, even if you can no longer see where.
::::

⁠**In short:** `nan` is the result of invalid calculations and infects every further calculation.

:::hintergrund Why `inf` and `nan` exist, and why Python still stops at a division by zero
Without special values, a computer would have to halt the program at every overflow and every invalid operation. In a simulation that computes a million values, this would often be the worst solution: a single invalid value would drag all the others down with it. IEEE 754 therefore lets the calculation continue with `inf` or `nan`, and the program can check at the end which results are usable. According to the standard, $1/0$ would also simply be $\infty$ and $0/0$ simply `nan`.

Python deviates from this: for `/`, `//` and `%` by zero, it always raises a `ZeroDivisionError`, even with `float`. This has a practical advantage: in an ordinary program, a division by zero is usually a mistake, and the exception with its traceback immediately shows where it is; a silent `inf` would make it visible only many lines later.
:::

### Exercises for Section [5](#stufe-5)

<span class="anker" id="stufe-5-7"></span>

:::aufgabe Exercise 17 ★★ Finding machine epsilon yourself
<span class="anker" id="aufg-17"></span>

In interactive mode, search for the smallest power of two $2^{-k}$ for which `1.0 + 2 ** -k` does not give `1.0`. Start at $k=50$ and increase $k$ step by step with the up arrow key. Explain why the limit lies exactly at this $k$, and why the result for $k=53$ is `1.0` even though $2^{-53}$ is not 0.

:::loesung
```console
>>> 1.0 + 2 ** -50
1.0000000000000009
>>> 1.0 + 2 ** -51
1.0000000000000004
>>> 1.0 + 2 ** -52
1.0000000000000002
>>> 1.0 + 2 ** -53
1.0
```

The smallest power of two that still changes 1 is $2^{-52}$, so $k=52$. It is exactly the spacing from 1 to the next `float`, machine epsilon. For $k=53$, $1+2^{-53}$ lies exactly in the middle between 1 and $1+2^{-52}$. In a tie, the result is rounded to the even significand, and the significand field of 1 is 0, that is, even. That is why 1 comes out, even though $2^{-53}\ne0$. Every even smaller power of two lies even closer to 1.
:::
:::

:::aufgabe Exercise 18 ★★ Building a time axis
<span class="anker" id="aufg-18"></span>

A stopwatch app is supposed to display the time every $0.1$ s, that is, generate the points in time $t_k=k\cdot0.1\,\mathrm{s}$. Approach A adds `0.1` to the last point in time again and again; Approach B computes `k * 0.1` directly.

<ol class="al">

<li>

Use both approaches to compute $t_3$ and $t_8$ (Approach A with `_ + 0.1` in interactive mode).

</li>

<li>

Which approach is more accurate, and why? How many roundings are contained in $t_k$ with Approach A, and how many with Approach B?

</li>

</ol>

:::loesung
(a) Approach A in interactive mode, Approach B directly:

```console
>>> 0.1
0.1
>>> _ + 0.1
0.2
>>> _ + 0.1
0.30000000000000004
>>> 3 * 0.1
0.30000000000000004
>>> 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1
0.7999999999999999
>>> 8 * 0.1
0.8
```

For $t_3$, both approaches return the same `float`; for $t_8$, they do not: Approach A gives $0.7999999999999999\,\mathrm s$, Approach B $0.8\,\mathrm s$. The long sum in one line calculates from left to right, exactly like the repeated `_ + 0.1`.

(b) Approach B is more accurate. $t_k$ from Approach A contains the representation error of `0.1` and $k-1$ rounded additions; the errors can add up and grow with $k$. With Approach B, there are the representation error and a single rounding; the relative error always stays below about $2\varepsilon_{\mathrm M}$. Good programs therefore compute points in time from the step number, not by summing up.
:::
:::

:::aufgabe Exercise 19 ★ Absorption or cancellation?
<span class="anker" id="aufg-19"></span>

For each expression, predict the result and assign it to one of the two effects. Then check on the computer.

<ol class="al">

<li>

`1e20 + 1000 - 1e20`

</li>

<li>

`(1 + 1e-10) - 1`

</li>

<li>

`1e20 - 1e20 + 1000`

</li>

<li>

`(2 ** 53 + 1.0) - 2 ** 53`

</li>

</ol>

:::loesung
```console
>>> 1e20 + 1000 - 1e20
0.0
>>> (1 + 1e-10) - 1
1.000000082740371e-10
>>> 1e20 - 1e20 + 1000
1000.0
>>> (2 ** 53 + 1.0) - 2 ** 53
0.0
```

(a) Absorption: at $10^{20}$, the spacing of the `float` values is $2^{-52}\cdot2^{66}=16384$, because $2^{66}\le10^{20}<2^{67}$. 1000 is less than half the spacing and is lost. (b) Cancellation: $1+10^{-10}$ is distorted by up to $1.1\cdot10^{-16}$ when it is stored; after subtracting the 1, this is a relative error of about $8\cdot10^{-8}$ in the result $10^{-10}$, leaving only seven correct digits. (c) No effect: first, exactly 0 is calculated, then 1000 is added. (d) Absorption: $2^{53}+1$ lies exactly in the middle between $2^{53}$ and $2^{53}+2$ and is rounded to the even significand, that is, to $2^{53}$.
:::
:::

:::aufgabe Exercise 20 ★ Edge cases
<span class="anker" id="aufg-20"></span>

Predict what Python displays: (a) `1e308 + 1e308`, (b) `-1e309 * 2`, (c) `1e309 * 0`, (d) `1e-320 / 1e10`, (e) `1.0 / 0`. Assign each result to a subsection of this section.

:::loesung
```console
>>> 1e308 + 1e308
inf
>>> -1e309 * 2
-inf
>>> 1e309 * 0
nan
>>> 1e-320 / 1e10
0.0
>>> 1.0 / 0
Traceback (most recent call last):
  File "<python-input-4>", line 1, in <module>
    1.0 / 0
    ~~~~^~~
ZeroDivisionError: division by zero
```

(a) Overflow, subsection [5.5](#stufe-5-5): $2\cdot10^{308}$ is larger than the largest `float`. (b) Calculating with `-inf`, also subsection [5.5](#stufe-5-5). (c) $\infty\cdot0$ has no meaningful answer: `nan`, subsection [5.6](#stufe-5-6). (d) $10^{-330}$ lies below the smallest positive `float` $4.9\cdot10^{-324}$ and becomes 0; background in subsection [5.5](#stufe-5-5). (e) For a division by zero, Python raises an exception instead of returning `inf`; background in subsection [5.6](#stufe-5-6). Under Python 3.13, the description reads `float division by zero`.
:::
:::

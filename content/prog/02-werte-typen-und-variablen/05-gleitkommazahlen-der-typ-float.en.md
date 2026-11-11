---
title: Floating-point numbers: the type `float`
pfad: Computer Science / Programming / Python / Values, Types and Variables
adresse: informatik/programmieren/python/werte-typen-und-variablen
knoten: Chapter 2: Values, Types and Variables
order: 6030500
summary: Quantities from everyday life and science range from the thickness of a hair to the distance to the sun, and they have decimal places.
tags: floating-point number, significand, exponent, exponent field, significand field, representation error
lang: en
---

<span class="anker" id="stufe-4"></span>

:::zweck
Quantities from everyday life and science range from the thickness of a hair to the distance to the sun, and they have decimal places. This section shows how Python stores such numbers in 64 bits, and why a small error arises as soon as you type in `0.1`.
:::

### The floating-point representation

<span class="anker" id="stufe-4-1"></span>

A human hair is about $7.5\cdot10^{-5}\,\mathrm m$ thick; the sun is about $1.5\cdot10^{11}\,\mathrm m$ away from the earth. There are 16 powers of ten between them. If you wanted to store both values with a fixed number of digits before and after the decimal point, you would need dozens of digits, almost all of which would be zero.

**Scientific notation.** Science and engineering solve this with scientific notation: a few significant digits and a power of ten that says where the point is. $7.5\cdot10^{-5}$ and $1.5\cdot10^{11}$ both need only two digits and an exponent. The point “floats” to the right position with the exponent. Computers do the same, only in the binary system and with a fixed number of binary digits.

:::definition Definition 4.1 (Floating-point number)
<span class="anker" id="satz-4-1"></span>

A __floating-point number__ with $p$ binary digits is a number of the form $\pm\,m\cdot2^E$.

Here, the __significand__ $m$ (also called the mantissa) is a binary number with $p$ digits and exactly one digit before the point, which is 1: $m=1.\ldots{}_2$, so $1\le m<2$.

The __exponent__ $E$ is an integer from a fixed range.
:::

::::beispiel a toy format
With only $p=3$ digits, there are four significands: $1.00_2=1$, $1.01_2=1.25$, $1.10_2=1.5$ and $1.11_2=1.75$. If you allow the exponents $E=-1,0,1,2$, you get 16 positive numbers:

| $E$ | $m=1$ | $m=1.25$ | $m=1.5$ | $m=1.75$ | Spacing |
|---|---|---|---|---|---|
| $-1$ | $0.5$ | $0.625$ | $0.75$ | $0.875$ | $0.125$ |
| $0$ | $1$ | $1.25$ | $1.5$ | $1.75$ | $0.25$ |
| $1$ | $2$ | $2.5$ | $3$ | $3.5$ | $0.5$ |
| $2$ | $4$ | $5$ | $6$ | $7$ | $1$ |

On the number line, they are not evenly spaced (Fig. [6](#abb-6)). Between 1 and 2, neighbors are $0.25$ apart; between 4 and 8, they are 1 apart: with each power of two, the spacing doubles. A number such as $6.5$ does not occur in this format; if you want to store it, you have to round it to one of the neighboring numbers 6 or 7.

:::abbildung prog/k2zahlenstrahl 6
The 16 positive numbers of a floating-point format with three binary digits and the exponents $-1$ to $2$. Each range from one power of two to the next contains the same number of values, four; that is why their spacing doubles with each power of two. No number of the format lies between 0 and $0.5$.
:::
::::

⁠**In short:** A floating-point number is a significand times a power of two; with a fixed number of digits, the spacing of neighboring numbers grows with their magnitude.

:::hintergrund Why growing spacing is exactly right
The spacing of neighboring numbers grows in the same proportion as the numbers themselves. The *relative* spacing, that is, spacing divided by magnitude, therefore stays roughly the same: in the toy format, it lies between $\frac17$ and $\frac14$, no matter whether you look at $0.5$ or at 6. From $0.5$ to its neighbor, the distance is $0.125$, a quarter of $0.5$, and from $3.5$ to its neighbor 4, it is $0.5$, a seventh of $3.5$. This is also how people talk in everyday life: a big city has “1.5 million inhabitants”, a village “850 inhabitants”. In both statements, two or three digits count, and nobody gives the population of the big city down to the last person. A fixed spacing would be too coarse for small values and unnecessarily fine for large ones. Floating-point numbers distribute their precision so that every number has roughly the same number of significant digits.
:::

### The type `float`

<span class="anker" id="stufe-4-2"></span>

The toy format has only 16 numbers. A computer needs a format with many more digits and a much larger range of exponents, and all computers should use the same format so that programs give the same results everywhere.

**A word of 64 bits.** Python stores every floating-point number in exactly 64 bits, that is, 8 bytes. These 64 bits are divided into three fields: one bit for the sign, 11 bits for the exponent, 52 bits for the significand (Fig. [7](#abb-7)).

:::definition Definition 4.2 (The type `float`)
<span class="anker" id="satz-4-2"></span>

An object of type `float` stores a floating-point number in the *binary64* format of the IEEE 754 standard. The significand has $p=53$ binary digits, and the exponent lies in the range $-1022\le E\le1023$. The number occupies 64 bits, divided into three fields:

<ul>

<li>

a 1-bit sign $s$: $s=0$ for positive, $s=1$ for negative numbers;

</li>

<li>

an 11-bit exponent field $c$;

</li>

<li>

a 52-bit significand field $t$.

</li>

</ul>
:::

The IEEE 754 standard specifies how computers store floating-point numbers and calculate with them; almost all processors since the 1980s comply with it. The name *binary64* says: base 2, 64 bits. The format is also called “double precision”.

:::abbildung prog/k2bitfelder 7
The 64 bits of a `float`, at the top for the number $6.5$, at the bottom for the number that Python stores when you type in `0.1`. On the left the sign bit (bit 63), then 11 bits of exponent field, on the right 52 bits of significand field (bits 51 to 0).
:::

⁠**In short:** A `float` is a floating-point number with a significand of 53 binary digits, stored in 64 bits: sign, exponent field, significand field.

:::hintergrund Where the standard comes from
Until the 1980s, almost every computer manufacturer calculated differently: with different numbers of digits, different rounding rules, different answers to overflows. The same program gave different results on two machines, and numerical software could hardly be carried over from one machine to another. A committee of the IEEE, a worldwide professional association of engineers and computer scientists, therefore worked out a common standard; it appeared in 1985 as IEEE 754. A key contributor was the mathematician William Kahan from Berkeley, who received the Turing Award for it in 1989. The standard was revised in 2008 and 2019; the 2019 version is the one in force today.
:::

### The exponent field

<span class="anker" id="stufe-4-3"></span>

The exponent can be negative, from $-1022$ to $1023$. The 11 bits of the exponent field, however, are an ordinary binary number without a sign, from 0 to $2^{11}-1=2047$.

**A shifted zero point.** You shift the zero point, as on a temperature scale: instead of the exponent itself, you store the exponent plus 1023. The smallest exponent $-1022$ thus becomes 1, and the exponent 0 becomes 1023.

:::definition Definition 4.3 (Exponent field)
<span class="anker" id="satz-4-3"></span>

The __exponent field__ $c$ of a `float` stores the exponent shifted by 1023:

$$c=E+1023,\qquad E=c-1023 .$$

Ordinary numbers have $1\le c\le2046$. The values $c=0$ and $c=2047$ are reserved for special cases.
:::

The number 1023 is called the bias of the exponent.

::::beispiel
In Fig. [7](#abb-7), $6.5$ has the exponent field $10000000001_2=1025$, so $E=1025-1023=2$. Indeed, $6.5=1.625\cdot2^2$. The bottom row has $c=01111111011_2=\mathtt{3fb}_{16}=1019$, so $E=-4$.
::::

⁠**In short:** The exponent field stores $E+1023$; this way, it does without a sign.

:::hintergrund Why the exponent is stored shifted
The fields come in the order sign, exponent, significand, and the exponent is shifted, so it is never negative. Together, this has a practical consequence: if you read the 64 bits of two positive `float` values as ordinary integers without a sign, the larger integer is also the larger `float`. A larger exponent gives a larger exponent field and thus a larger bit pattern, and for equal exponents, the significand decides. A computer can therefore compare and sort floating-point numbers with the same fast instructions as integers; only the sign needs separate handling. With an exponent in a signed representation, this would not work.
:::

### The significand field

<span class="anker" id="stufe-4-4"></span>

The significand has 53 binary digits, but only 52 bits are available for it.

**The first digit is always 1.** By the definition of a floating-point number, the digit before the point of the significand is always a 1. What is always the same need not be stored. The significand field therefore contains only the 52 digits after the point.

:::definition Definition 4.4 (Significand field)
<span class="anker" id="satz-4-4"></span>

The __significand field__ $t$ of a `float` contains the 52 binary digits of the significand after the point. If you read them as an integer $t$, the significand is

$$m=1+\frac{t}{2^{52}} .$$
:::

The 1 before the point is called the hidden bit because it is not stored in memory. With the exponent field and the significand field together, the value of a `float` with $1\le c\le2046$ is

<span class="anker" id="gl-4-1"></span>
$$x=(-1)^s\cdot\Bigl(1+\frac{t}{2^{52}}\Bigr)\cdot2^{\,c-1023}. \tag{4.1}$$

::::beispiel
For $6.5$, the significand field in Fig. [7](#abb-7) begins with $101$, followed only by zeros. So the significand is $m=1.101_2=1+\frac12+\frac18=1.625$, and with $E=2$ and $s=0$, this gives $x=1.625\cdot4=6.5$.
::::

⁠**In short:** The significand field stores the 52 digits after the point; you add the leading 1 when reading it.

### Splitting a `float` into its fields

<span class="anker" id="stufe-4-5"></span>

To see what Python has actually stored, you need the three fields. Fig. [7](#abb-7) is tedious to read; Python provides the same information more compactly.

**The method `hex`.** Every `float` has a method `hex`. It writes the number as a significand times a power of two, with the significand in hexadecimal:

```console
>>> (6.5).hex()
'0x1.a000000000000p+2'
>>> (-0.75).hex()
'-0x1.8000000000000p-1'
```

This is how you read the string:

<ul>

<li>

a minus sign at the beginning if $s=1$;

</li>

<li>

`0x1.` is the hidden bit, a 1 before the point, written here in hexadecimal;

</li>

<li>

the 13 hexadecimal digits after it are the significand field $t$, four bits per digit, 52 bits in total;

</li>

<li>

after `p` comes the exponent $E$ as a decimal number, that is, not the field $c$ but $c-1023$.

</li>

</ul>

::::beispiel
For $6.5$, the significand field is $\mathtt{a000000000000}_{16}$, the digit $\mathtt a=1010_2$ followed only by zeros: $m=1.1010_2=1.625$. With $E=2$, this gives $6.5$, as in Fig. [7](#abb-7). For $-0.75$, $s=1$ and $\mathtt{8}=1000_2$, so $m=1.1_2=1.5$, and $E=-1$: $x=-1.5\cdot\frac12=-0.75$.
::::

⁠**In short:** `hex` shows a `float` as $\pm$`0x1.`*significand field*`p`*exponent*.

### The representation error

<span class="anker" id="stufe-4-6"></span>

In the binary system, $0.1$ has infinitely many digits (subsection [3.7](zahlen-im-binarsystem.html#stufe-3-7)). But a `float` has only 53. What does Python store when you type in `0.1`?

**The nearest neighbor.** If a number lies between two representable numbers, like $6.5$ in Fig. [6](#abb-6), Python has to take one of the two. It takes the closer one.

:::definition Definition 4.5 (Rounding and representation error)
<span class="anker" id="satz-4-5"></span>

If a number $x$ cannot be represented as a `float`, Python stores the `float` closest to $x$. If $x$ lies exactly halfway between two `float` values, Python takes the one whose last significand bit is 0. The difference between the stored value and $x$ is called the __representation error__.
:::

The rule for the midpoint is called “round half to even”. In the toy format, $6.5$ lies exactly between $6=1.10_2\cdot2^2$ and $7=1.11_2\cdot2^2$; it is rounded to 6 because the last significand bit of 6 is 0.

**By hand: predicting the fields of $0.1$.** From the doubling method,

$$0.1=0.0001\,1001\,1001\,1001\ldots{}_2=1.1001\,1001\,1001\ldots{}_2\cdot2^{-4}.$$

The point has moved four positions to the right, so $E=-4$. After the point of the significand, $1001$ repeats, in hexadecimal the digit `9`. Of the infinitely many digits, 52 fit into the significand field; that is 13 hexadecimal digits: $\mathtt{9999999999999}$. The first digit that no longer fits is a 1, and more ones follow after it. So the cut-off rest is more than half a unit in the last place, and the nearest representable number lies above: the last digit is rounded up, and `9` becomes `a`. The prediction is `0x1.999999999999ap-4`.

**Ready-made: what Python has stored.** The method `hex` confirms the prediction. The method `as_integer_ratio` from subsection [1.4](objekte-und-typen.html#stufe-1-4) returns the stored value as a fraction in lowest terms:

```console
>>> (0.1).hex()
'0x1.999999999999ap-4'
>>> (0.1).as_integer_ratio()
(3602879701896397, 36028797018963968)
>>> 2 ** 55
36028797018963968
```

The denominator is $2^{55}$. So what is stored is not $\frac1{10}$ but $\frac{3602879701896397}{2^{55}}$. Equation [(4.1)](#gl-4-1) gives the same result from the fields (Fig. [8](#abb-8)): $s=0$, $c=1019$, and the significand field is $\mathtt{999999999999a}_{16}=2702159776422298$.

:::abbildung prog/k2rfloat 8
The value that Python stores for `0.1`, computed from the three fields: sign $s=0$, exponent field $c=1019$, significand field $t=\mathtt{999999999999a}_{16}$; $2^{52}=4503599627370496$, $2^{55}=36028797018963968$.
:::

**Writing out the stored value exactly.** A fraction with the denominator $2^{55}$ can be written as a finite decimal fraction, because $\frac{1}{2^{55}}=\frac{5^{55}}{10^{55}}$. If you multiply the numerator by $5^{55}$, the decimal digits appear. With `int`, this is an exact calculation:

```console
>>> 3602879701896397 * 5 ** 55
1000000000000000055511151231257827021181583404541015625
```

With the point placed 55 digits from the right:

$$\mathtt{0.1}\ \text{stored}=0.1000000000000000055511151231257827021181583404541015625 .$$

So the representation error is about $5.55\cdot10^{-18}$, relative to $0.1$ about $5.55\cdot10^{-17}$.

**Comparison.** The calculation by hand and the ready-made result agree: the doubling method gives the pattern $1001$, rounding turns the last digit into an `a`, and Python shows exactly these fields.

⁠**In short:** Python stores the nearest `float`; for `0.1`, that is $\frac{3602879701896397}{2^{55}}$, too large by about $5.6\cdot10^{-18}$.

:::hintergrund A representation error with consequences: the air defense system in Dhahran
On February 25, 1991, a Patriot air defense system in Dhahran (Saudi Arabia) missed an incoming missile; 28 soldiers died in the impact. In its investigation, the U.S. General Accounting Office found the cause in the time calculation. The system counted the time in tenths of a second as an integer and converted it to seconds by multiplying by $0.1$. This $0.1$ was held in a 24-bit register, that is, with even fewer digits than a `float`, and was therefore too small by about $9.5\cdot10^{-8}$. After more than 100 hours of continuous operation, that is, after more than 3.6 million tenths of a second, this had grown into a time error of $0.34\,\mathrm s$. The investigation puts a number on the consequence: the area in which the system expected the missile was 687 meters away from it. The error did harm because two parts of the program converted the time with different accuracy; as a result, the errors no longer canceled out when two points in time were subtracted.

The case teaches two things: a tiny representation error becomes large when it is multiplied by a large number. And the system did not calculate with IEEE 754 floating-point numbers but with a fixed number of digits. The problem lies not in a particular format but in the fact that $\frac1{10}$ is exact in *no* binary format.
:::

### The shortest representation

<span class="anker" id="stufe-4-7"></span>

If Python has stored $0.1000000000000000055511\ldots$, why does interactive mode display `0.1`? And why does it suddenly show 17 digits for `0.1 + 0.2`?

**A label that must be unique.** Between two neighboring `float` values, there are infinitely many decimal numbers. All those that lie closer to the stored value than to its neighbors lead to exactly this `float` when typed in. Python picks the one with the fewest digits among them and displays it as a label.

:::definition Definition 4.6 (Shortest representation)
<span class="anker" id="satz-4-6"></span>

Interactive mode and `print` display a `float` as the shortest decimal number that gives exactly this `float` when typed in.
:::

So what is displayed is not the stored value but a unique mark for it. If you type in the displayed number again, you get exactly the same `float`.

::::beispiel
For the stored value of `0.1`, the shortest such decimal number is $0.1$ itself; that is why `0.1` appears. With `0.1 + 0.2`, things are different:

```console
>>> 0.1 + 0.2
0.30000000000000004
>>> 0.3
0.3
>>> (0.1 + 0.2).hex()
'0x1.3333333333334p-2'
>>> (0.3).hex()
'0x1.3333333333333p-2'
```

The sum is a different `float` from the one Python stores for `0.3`: the significand fields differ in the last digit; the two numbers are neighbors. The label `0.3` is already taken, so the sum needs a longer one, and the shortest one that fits the sum and none of its neighbors has 17 digits.
::::

⁠**In short:** What is displayed is the shortest decimal number that gives the same `float`; displayed is not the same as stored.

:::hintergrund How many digits are needed, and what was displayed before Python 3.1
Two fixed numbers apply to the binary64 format. Every decimal number with at most 15 significant digits survives the trip into a `float` and, rounded to 15 digits, back unchanged. And 17 significant digits are always enough to identify a `float` uniquely. Up to Python 3.0, interactive mode therefore rounded every display to 17 significant digits and wrote the number `0.10000000000000001` for `0.1`. Since Python 3.1, a method that goes back to the mathematician David Gay has searched for the shortest matching number. This changed nothing about the stored value, only its label. Precisely for this reason, the representation error today becomes noticeable only when a calculation leads away from the value you typed in.
:::

### Exercises for Section [4](#stufe-4)

<span class="anker" id="stufe-4-8"></span>

:::aufgabe Exercise 13 ★ Reading the fields
<span class="anker" id="aufg-13"></span>

Use `hex` to determine the sign, the exponent $E$, the exponent field $c$ and the significand $m$ of `1.0`, `3.0`, `-0.5` and `0.75`. From the fields, calculate the value back using Equation [(4.1)](#gl-4-1).

:::loesung
```console
>>> (1.0).hex()
'0x1.0000000000000p+0'
>>> (3.0).hex()
'0x1.8000000000000p+1'
>>> (-0.5).hex()
'-0x1.0000000000000p-1'
>>> (0.75).hex()
'0x1.8000000000000p-1'
```

| Number | $s$ | $E$ | $c=E+1023$ | $m$ |
|---|---|---|---|---|
| $1.0$ | 0 | 0 | 1023 | $1.0$ |
| $3.0$ | 0 | 1 | 1024 | $1.1_2=1.5$ |
| $-0.5$ | 1 | $-1$ | 1022 | $1.0$ |
| $0.75$ | 0 | $-1$ | 1022 | $1.1_2=1.5$ |

The digit `8` is $1000_2$; it stands for the first digit after the binary point, that is, $\frac12$. Calculated back with [(4.1)](#gl-4-1): $1\cdot2^0=1$, $1.5\cdot2^1=3$, $-1\cdot2^{-1}=-0.5$, $1.5\cdot2^{-1}=0.75$. All four numbers are exact, because their significands have only one digit after the binary point.
:::
:::

:::aufgabe Exercise 14 ★★ Predicting $0.2$ and $0.3$
<span class="anker" id="aufg-14"></span>

<ol class="al">

<li>

$0.2=2\cdot0.1$. Predict without a computer what `(0.2).hex()` displays.

</li>

<li>

Use your binary digits from Exercise [12](zahlen-im-binarsystem.html#aufg-12) to predict what `(0.3).hex()` displays. Is the last hexadecimal digit rounded up or down? Justify your answer with the first digit that no longer fits into the significand field.

</li>

<li>

Check both predictions on the computer.

</li>

</ol>

:::loesung
(a) Doubling only increases the exponent by 1; the significand stays the same. The rounding is the same, because the same binary digits are cut off. Prediction:

`0x1.999999999999ap-3`

(b) From Exercise [12](zahlen-im-binarsystem.html#aufg-12): $0.3=0.01\,0011\,0011\ldots{}_2=1.0011\,0011\ldots{}_2\cdot2^{-2}$. After the point of the significand, $0011$ repeats, hexadecimal `3`. The 13 hexadecimal digits are `3333333333333`. The first digit that no longer fits begins a new group $0011$, so it is 0: the cut-off rest is smaller than half a unit in the last place, and the result is rounded down. Prediction: `0x1.3333333333333p-2`.

(c)

```console
>>> (0.2).hex()
'0x1.999999999999ap-3'
>>> (0.3).hex()
'0x1.3333333333333p-2'
```

Both predictions are correct. So the stored value of `0.3` is slightly *smaller* than $0.3$, and that of `0.1` and `0.2` slightly larger. This, too, explains why `0.1 + 0.2` does not land on the `float` for `0.3`.
:::
:::

:::aufgabe Exercise 15 ★★ Which numbers are exact?
<span class="anker" id="aufg-15"></span>

For each number, decide whether Python stores it exactly: $0.5$, $0.25$, $0.2$, $1024.0$, $1.1$. Check with `as_integer_ratio`: how can you tell from the answer whether the number was stored exactly?

:::loesung
```console
>>> (0.5).as_integer_ratio()
(1, 2)
>>> (0.25).as_integer_ratio()
(1, 4)
>>> (0.2).as_integer_ratio()
(3602879701896397, 18014398509481984)
>>> (1024.0).as_integer_ratio()
(1024, 1)
>>> (1.1).as_integer_ratio()
(2476979795053773, 2251799813685248)
```

`as_integer_ratio` returns the stored value as a fraction in lowest terms. If this fraction is the intended number, the number was stored exactly: $\frac12$, $\frac14$ and $\frac{1024}1$ are correct. For $0.2=\frac15$ and $1.1=\frac{11}{10}$, on the other hand, you get a huge fraction with a power of two in the denominator ($2^{54}$ and $2^{51}$), that is, a different value. The denominator of a stored `float` is always a power of two; exactly those numbers whose denominator in lowest terms is a power of two and that also fit into 53 digits are exact.
:::
:::

:::aufgabe Exercise 16 ★★★ Large integers as `float`
<span class="anker" id="aufg-16"></span>

<ol class="al">

<li>

$10^{22}=2^{22}\cdot5^{22}$. Show with Python that $5^{22}<2^{53}$, and conclude that `1e22` is stored exactly.

</li>

<li>

Why does this not hold for $10^{23}$?

</li>

<li>

Check with `int(1e22)` and `int(1e23)`. Here, the function `int` turns the stored `float` into the integer that it actually represents.

</li>

</ol>

:::loesung
(a) and (b):

```console
>>> 5 ** 22
2384185791015625
>>> 2 ** 53
9007199254740992
>>> 5 ** 23
11920928955078125
```

$10^{22}=5^{22}\cdot2^{22}$. The factor $2^{22}$ goes into the exponent. So the significand has to represent the integer $5^{22}$, and this is smaller than $2^{53}$, so it fits into 53 binary digits. Hence `1e22` is exact. For $10^{23}=5^{23}\cdot2^{23}$, however, $5^{23}>2^{53}$, and because $5^{23}$ is odd, no factor 2 can be shifted into the exponent either: the number would need 54 binary digits and is rounded.

(c)

```console
>>> int(1e22)
10000000000000000000000
>>> int(1e23)
99999999999999991611392
```

As a `float`, `1e23` is smaller than $10^{23}$ by $8\,388\,608=2^{23}$. This is half the spacing of neighboring `float` values at this magnitude, and `int` shows it as an exact integer.
:::
:::

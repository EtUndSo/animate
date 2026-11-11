---
title: Integers and arithmetic operators
pfad: Computer Science / Programming / Python / Values, Types and Variables
adresse: informatik/programmieren/python/werte-typen-und-variablen
knoten: Chapter 2: Values, Types and Variables
order: 6030300
summary: Integers are Python's simplest number type.
tags: operator, operands, floor division, remainder, precedence
lang: en
---

<span class="anker" id="stufe-2"></span>

:::zweck
Integers are Python's simplest number type. This section shows how large they can become, which arithmetic operators Python knows and how it divides with a whole-number result, also with negative numbers.
:::

### The type `int`

<span class="anker" id="stufe-2-1"></span>

Item counts, scores, page numbers, account numbers: many things in everyday life are whole numbers. There, you want to calculate exactly, without any rounding, even when the numbers become very large.

**Digits, as many as needed.** On paper, you write an integer with as many digits as it needs. A three-digit number needs three digits, a thirty-digit number thirty. Python handles integers in exactly this way.

:::definition Definition 2.1 (The type `int`)
<span class="anker" id="satz-2-1"></span>

The type `int` comprises the integers $\ldots,-2,-1,0,1,2,\ldots$ An object of type `int` has no fixed size: it grows as large as the number requires and is limited only by main memory. Adding, subtracting and multiplying two `int` values always yields the exact result as an `int`.
:::

You write an `int` as a sequence of digits without a point, negative numbers with a minus sign in front. Long numbers may be structured with underscores: `1_000_000` is the same number as `1000000`.

::::beispiel
$2^{100}$ has 31 digits and is computed exactly. Even a calculation in which a small number stands between two huge ones loses nothing:

```console
>>> 2 ** 100
1267650600228229401496703205376
>>> 10 ** 20 + 1 - 10 ** 20
1
>>> 1_000_000 * 1_000_000
1000000000000
```
::::

⁠**In short:** An `int` is an integer of arbitrary size; Python calculates with it exactly.

:::hintergrund Why an `int` never overflows in Python
A processor calculates with integers of a fixed size. A common size reaches up to $18\,446\,744\,073\,709\,551\,615$; the machine instruction cuts off anything beyond that, and the result is wrong. The integer types of the C language have such fixed limits.

That is why CPython does not store an `int` as a single machine number but like a number on paper: as a sequence of digits. Only the base is not 10 but $2^{30}=1\,073\,741\,824$. Each “digit” is a number from 0 to $2^{30}-1$ and occupies a memory word of its own; the sign is stored separately in front. When a number grows, CPython appends further digits. The arithmetic works like the written arithmetic you learned at school: digit by digit with carries, each step with ordinary machine instructions. The price is time: an addition of large numbers needs many machine instructions instead of a single one.
:::

:::hintergrund There is a limit after all: 4300 decimal digits when converting to text
Python can calculate with arbitrarily large `int` values. For display, however, it has to convert the number into decimal digits, and for huge numbers this is much more costly than any addition: the effort grows considerably faster than the number of digits. An attacker could send a server that reads numbers from texts a number with millions of digits and thus keep it busy for a long time. Since Python 3.11, Python therefore refuses conversions with more than 4300 decimal digits. The vulnerability is publicly described under the identifier CVE-2020-10735.

```console
>>> 10 ** 5000
Traceback (most recent call last):
  File "<python-input-0>", line 1, in <module>
    10 ** 5000
    ~~~^^~~~~~
ValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit
```

The number has been computed; only the display fails. The message names the way to shift the limit. Conversions into systems with a power of two as the base are exempt, because they are fast.
:::

### Operator and operand

<span class="anker" id="stufe-2-2"></span>

[Chapter 1](/wissen/en/informatik/programmieren/python/programme-und-der-python-interpreter/programme-und-der-python-interpreter.html) used the symbols `+ - * / **` for calculating ([Chapter 1, Section 4.4](/wissen/en/informatik/programmieren/python/programme-und-der-python-interpreter/der-interaktive-modus.html#stufe-4-4)). Python knows further such symbols, and there is a general name for them.

**A small machine.** An arithmetic symbol takes in values and puts out a new value, like a small machine with inputs and one output.

:::definition Definition 2.2 (Operator and operand)
<span class="anker" id="satz-2-2"></span>

An __operator__ is a symbol that computes a new value from values.

The values an operator acts on are called its __operands__.
:::

An operator with two operands is called binary, one with only one operand unary. In `7 - 2`, the minus is binary; in `-7`, it is unary: it turns 7 into the number $-7$.

Python has seven arithmetic operators:

| Operator | Meaning | Example |
|---|---|---|
| `+` | addition | `7 + 2` gives `9` |
| `-` | subtraction; unary: sign | `7 - 2` gives `5` |
| `*` | multiplication | `7 * 2` gives `14` |
| `/` | division | `7 / 2` gives `3.5` |
| `//` | floor division | `7 // 2` gives `3` |
| `%` | remainder | `7 % 2` gives `1` |
| `**` | power | `7 ** 2` gives `49` |

**Which type the result has.** If both operands are an `int`, the result is also an `int`, with one exception: division `/` always returns a `float`. If at least one operand is a `float`, Python turns the other one into a `float` as well, and the result is a `float`:

```console
>>> 7 + 2
9
>>> 7 + 0.5
7.5
>>> 2 * 3.0
6.0
```

⁠**In short:** An operator computes a new value from its operands; if one operand is a `float`, so is the result.

### Division

<span class="anker" id="stufe-2-3"></span>

Price divided by weight, distance divided by time: you need ordinary division all the time, and it should return the result you know from mathematics.

:::definition Definition 2.3 (Division)
<span class="anker" id="satz-2-3"></span>

The operator `/` divides the left operand by the right one. The result is always a `float`, even if both operands are an `int` and the division leaves no remainder.
:::

::::beispiel
This explains the observation from [Chapter 1](/wissen/en/informatik/programmieren/python/programme-und-der-python-interpreter/programme-und-der-python-interpreter.html) that `12 / 4` gives the answer `3.0`:

```console
>>> 7 / 2
3.5
>>> 12 / 4
3.0
>>> 1 / 3
0.3333333333333333
>>> 7 / 0
Traceback (most recent call last):
  File "<python-input-3>", line 1, in <module>
    7 / 0
    ~~^~~
ZeroDivisionError: division by zero
```

Dividing by zero is not possible; Python reports a `ZeroDivisionError`. If you divide a `float` by zero, the description in Python 3.13 is `float division by zero`; from Python 3.14 on, it is `division by zero`, as with integers.
::::

⁠**In short:** `/` divides as in mathematics and always returns a `float`.

:::hintergrund Why `/` returns a `float` even for integers
In the old versions 2.x of the Python language, `7 / 2` gave the integer 3, as in C: two integers were divided with a whole-number result, floating-point numbers in the ordinary way. The result thus depended on which type the values happened to have, and not on what the programmer meant. A calculation such as “sum of the grades divided by their count” gave the value 4.5 for the grades `4.0` and `5.0`, but silently gave the value 4 for the same grades written as `4` and `5`. Because nowhere in Python do you fix which type a value must have, integers easily slipped into such calculations.

With Python 3.0 (2008), the two meanings were therefore separated: `/` always divides as in mathematics, and if you want a whole-number division, you write a separate operator for it. Since then, an expression means the same thing regardless of whether integers or floating-point numbers go into it.
:::

### Floor division and remainder

<span class="anker" id="stufe-2-4"></span>

125 minutes are 2 hours and 5 minutes. For such calculations, you need two numbers: how many times 60 fits completely into 125, and what is left over.

**Multiples on the number line.** Mark all multiples of the divisor on the number line, for example all multiples of 2. Every integer $a$ then lies either on a multiple or between two of them. The nearest multiple to the left of $a$ (or $a$ itself) is $q\cdot2$; the distance from there to $a$ is the remainder (Fig. [2](#abb-2)). For $a=7$, the multiple is $6=3\cdot2$ and the remainder is 1. For $a=-7$, the nearest multiple to the left is $-8=(-4)\cdot2$, not $-6$, and the remainder is again 1.

:::abbildung prog/k2rest 2
Floor division by 2 on the number line. Each number $a$ has a nearest multiple of 2 to its left, $q\cdot2$; the distance to $a$ is the remainder. For $a=7$, $q=3$; for $a=-7$, $q=-4$. In both cases, the remainder is 1.
:::

:::definition Definition 2.4 (Floor division and remainder)
<span class="anker" id="satz-2-4"></span>

For integers $a$ and $b\ne0$, `a // b` is the largest integer that is not greater than $a/b$. This is the quotient rounded down, that is, toward $-\infty$.

The remainder is `a % b` $=a-(a\,/\!/\,b)\cdot b$.
:::

The operator `//` is called __floor division__; the operator `%` returns the __remainder__. Two rules follow from the definition that are worth remembering.

:::satz Theorem 2.5 (Floor division and remainder)
<span class="anker" id="satz-2-5"></span>

For all integers $a$ and $b\ne0$,

<span class="anker" id="gl-2-1"></span>
$$a = (a\,/\!/\,b)\cdot b + a\,\%\,b . \tag{2.1}$$

For $b>0$, the remainder lies in the range $0\le a\,\%\,b<b$; for $b<0$, in the range $b<a\,\%\,b\le0$. So the remainder always has the sign of $b$ or is zero.
:::

:::beweis from the definition
[(2.1)](#gl-2-1) is the definition of the remainder, solved for $a$. Let $b>0$ and $q=a\,/\!/\,b$. Because $q$ is the largest integer with $q\le a/b$, we have $q\le a/b<q+1$. Multiplying by $b>0$ gives $qb\le a<qb+b$, so $0\le a-qb<b$, and $a-qb$ is the remainder. For $b<0$, the multiplication reverses both inequalities: $qb\ge a>qb+b$, so $0\ge a-qb>b$.
:::

::::beispiel
First positive numbers, then negative ones:

```console
>>> 125 // 60
2
>>> 125 % 60
5
>>> -7 // 2
-4
>>> -7 % 2
1
>>> 7 // -2
-4
>>> 7 % -2
-1
```

The check with [(2.1)](#gl-2-1): $2\cdot60+5=125$, $(-4)\cdot2+1=-7$ and $(-4)\cdot(-2)+(-1)=7$. For $-7\,/\!/\,2$, we have $-7/2=-3.5$, and the largest integer that is not greater is $-4$, not $-3$.
::::

The built-in function `divmod` returns both results at once, first the quotient, then the remainder. Both operators also work with floating-point numbers:

```console
>>> divmod(125, 60)
(2, 5)
>>> divmod(-7, 2)
(-4, 1)
>>> 7.5 // 2
3.0
>>> 7.5 % 2
1.5
```

⁠**In short:** `//` rounds the quotient down, toward $-\infty$; `%` is the matching remainder and has the sign of the right operand.

:::hintergrund Why Python rounds toward $-\infty$ and not toward zero
In C, integer division rounds toward zero: there, $-7/2=-3$, and for Equation [(2.1)](#gl-2-1) to hold, the remainder must be $-1$. Python rounds down because then, for $b>0$, the remainder always lies between 0 and $b-1$, whatever the sign of $a$. This is exactly the property you need for everything that repeats periodically:

<ul>

<li>

⁠**Time of day:** If a clock counts seconds since a reference time, `t % 86400` is the second of the day, even for times before the reference time, that is, for negative $t$. One second before midnight is `-1 % 86400`, which gives 86399, that is, 23:59:59.

</li>

<li>

⁠**Angles:** A rotation by $-90^\circ$ ends in the same direction as a rotation by $270^\circ$. `-90 % 360` gives 270; every angle lands in the range from $0^\circ$ to below $360^\circ$.

</li>

</ul>

Once you have decided on this remainder, the quotient is fixed: by [(2.1)](#gl-2-1), $q=(a-r)/b$, and that is the rounded-down quotient. The same choice is common in number theory. That C calculates differently probably has historical reasons: the arithmetic units of the processors of the time divided toward zero, and since 1999 the C language standard has strictly prescribed this rounding.
:::

### The power

<span class="anker" id="stufe-2-5"></span>

Powers of ten for very large and very small numbers, powers of two for memory sizes, squares for areas, compound interest: powers occur in many calculations. [Chapter 1](/wissen/en/informatik/programmieren/python/programme-und-der-python-interpreter/programme-und-der-python-interpreter.html) used `**` with positive integer exponents and `2 ** 0.5` for the square root. For the type of the result, for negative exponents and for minus signs nearby, rules of their own apply.

:::definition Definition 2.6 (Power)
<span class="anker" id="satz-2-6"></span>

`a ** b` is $a$ to the power of $b$. If $a$ and $b$ are an `int` and $b\ge0$, the result is an `int`; if $b$ is a negative `int`, it is a `float`. If one of the operands is a `float`, the result is also a `float`; only a negative base with a non-integer exponent returns something else. In addition:

<ul>

<li>

`**` binds more tightly than a minus sign to its left: `-2 ** 2` is $-(2^2)=-4$.

</li>

<li>

Python evaluates several `**` from right to left: `2 ** 3 ** 2` is $2^{(3^2)}=2^9=512$.

</li>

</ul>
:::

::::beispiel
Negative exponents, minus signs and towers of powers:

```console
>>> 2 ** -1
0.5
>>> 10 ** -3
0.001
>>> -2 ** 2
-4
>>> (-2) ** 2
4
>>> 2 ** 3 ** 2
512
>>> (2 ** 3) ** 2
64
>>> 0 ** 0
1
```

`0 ** 0` is defined as 1 in Python, as in most programming languages.
::::

⁠**In short:** `**` binds more tightly than a minus sign in front of it and is evaluated from right to left; a negative exponent returns a `float`.

:::hintergrund Why Python reads powers the way mathematics does
Both rules come from mathematical notation. There, $-2^2$ means $-(2^2)=-4$; if you mean $(-2)^2$, you use parentheses. A tower of powers $a^{b^c}$ means $a^{(b^c)}$, because the other reading needs no tower: $(a^b)^c=a^{b\cdot c}$ is written more simply with a single exponent. Python adopts both so that formulas from the textbook can move into source code without rethinking. A minus sign to the *right* of the operator, on the other hand, belongs to the exponent: `2 ** -1` is $2^{-1}=0.5$.
:::

### Precedence

<span class="anker" id="stufe-2-6"></span>

An expression such as `2 + 3 * 4 ** 2 // 5` contains four operators. Python needs a fixed rule for the order in which it applies them.

:::definition Definition 2.7 (Precedence)
<span class="anker" id="satz-2-7"></span>

The __precedence__ of the operators determines which operator in an expression without parentheses is carried out first. For the arithmetic operators, from strongest to weakest:

| Rank | Operators | for equal rank |
|---|---|---|
| 1 | `**` | from right to left |
| 2 | unary `+` and `-` |  |
| 3 | `*` `/` `//` `%` | from left to right |
| 4 | binary `+` and `-` | from left to right |

Parentheses take precedence over everything.
:::

::::beispiel
Python evaluates `2 + 3 * 4 ** 2 // 5` like this: first the power $4^2=16$, then from left to right $3\cdot16=48$ and $48\,/\!/\,5=9$, finally $2+9=11$. In `12 / 3 / 2`, both operators have the same rank, so $(12/3)/2=2$:

```console
>>> 2 + 3 * 4 ** 2 // 5
11
>>> 100 - 7 % 3 * 2
98
>>> 12 / 3 / 2
2.0
>>> -3 ** 2
-9
```

In the second line, $7\,\%\,3=1$, then $1\cdot2=2$, finally $100-2=98$.
::::

⁠**In short:** Power before sign before multiplication and division (`* / // %`) before addition and subtraction; parentheses come first, and when in doubt, you add them.

### Exercises for Section [2](#stufe-2)

<span class="anker" id="stufe-2-7"></span>

:::aufgabe Exercise 4 ★ Predicting results
<span class="anker" id="aufg-4"></span>

For each expression, write down its value and type. Then check on the computer.

<ol class="al">

<li>

`7 / 2` (b) `7 // 2` (c) `-7 // 2` (d) `-7 % 3` (e) `7 % -3`

</li>

<li>

⁠**(f)** `2 ** -1` (g) `-2 ** 2` (h) `2 ** 3 ** 2` (i) `6 / 2` (j) `7.5 // 2`

</li>

</ol>

:::loesung
```console
>>> 7 / 2
3.5
>>> 7 // 2
3
>>> -7 // 2
-4
>>> -7 % 3
2
>>> 7 % -3
-2
>>> 2 ** -1
0.5
>>> -2 ** 2
-4
>>> 2 ** 3 ** 2
512
>>> 6 / 2
3.0
>>> 7.5 // 2
3.0
```

Types: (a), (f), (i), (j) are `float`, all others `int`. Reasons: `/` always returns a `float`, even for `6 / 2`. $-7/2=-3.5$, rounded down $-4$. $-7\,/\!/\,3=-3$, so $-7\,\%\,3=-7-(-3)\cdot3=2$; the remainder has the sign of $3$. $7\,/\!/\,(-3)=-3$, so $7\,\%\,(-3)=7-(-3)(-3)=-2$, with the sign of $-3$. A negative exponent gives a `float`. `**` binds more strongly than the minus in front of it and groups from the right: $-(2^2)$ and $2^{(3^2)}$. `7.5 // 2` rounds $3.75$ down to 3; because one operand is a `float`, so is the result.
:::
:::

:::aufgabe Exercise 5 ★★ Checking the equation for quotient and remainder
<span class="anker" id="aufg-5"></span>

For the pairs $(a,b)=(17,5)$, $(-17,5)$, $(17,-5)$ and $(-17,-5)$, determine $a\,/\!/\,b$ and $a\,\%\,b$ by hand. For each pair, check Equation [(2.1)](#gl-2-1) and the sign rule from Theorem [2.5](#satz-2-5). Then compare with `divmod`.

:::loesung
The quotient is $a/b$, rounded down; the remainder follows from $r=a-q\cdot b$:

| $a$ | $b$ | $a/b$ | $q=a\,/\!/\,b$ | $r=a\,\%\,b$ | Check $q\cdot b+r$ |
|---|---|---|---|---|---|
| 17 | 5 | $3.4$ | 3 | 2 | $15+2=17$ |
| $-17$ | 5 | $-3.4$ | $-4$ | 3 | $-20+3=-17$ |
| 17 | $-5$ | $-3.4$ | $-4$ | $-3$ | $20-3=17$ |
| $-17$ | $-5$ | $3.4$ | 3 | $-2$ | $-15-2=-17$ |

Sign rule: for $b=5$, the remainders 2 and 3 lie in $0\le r<5$; for $b=-5$, the remainders $-3$ and $-2$ lie in $-5<r\le0$. With `divmod`:

```console
>>> divmod(17, 5)
(3, 2)
>>> divmod(-17, 5)
(-4, 3)
>>> divmod(17, -5)
(-4, -3)
>>> divmod(-17, -5)
(3, -2)
```

What stands out is $-17\,/\!/\,5=-4$ and not $-3$: Python rounds toward $-\infty$. In C, it would be $-3$ with the remainder $-2$.
:::
:::

:::aufgabe Exercise 6 ★★ Seconds into days, hours, minutes
<span class="anker" id="aufg-6"></span>

A laptop has been running for $100\,000$ s without a restart.

<ol class="al">

<li>

Split the duration into days, hours, minutes and seconds using `//` and `%`.

</li>

<li>

Calculate the same with `divmod`, step by step in interactive mode.

</li>

<li>

A timestamp counts seconds from midnight of a reference day. Which time of day belongs to $t=-3600$ s? Answer the question with a single expression.

</li>

</ol>

:::loesung
(a) A day has $86\,400\,\mathrm s$, an hour $3600\,\mathrm s$. First the whole days, then continue with the remainder:

```console
>>> 100000 // 86400
1
>>> 100000 % 86400
13600
>>> 13600 // 3600
3
>>> 13600 % 3600
2800
>>> 2800 // 60
46
>>> 2800 % 60
40
```

Result: 1 day, 3 hours, 46 minutes, 40 seconds. Check: $86\,400+3\cdot3600+46\cdot60+40=100\,000$.

(b) `divmod` returns both parts at once:

```console
>>> divmod(100000, 86400)
(1, 13600)
>>> divmod(13600, 3600)
(3, 2800)
>>> divmod(2800, 60)
(46, 40)
```

(c) The second of the day is the remainder of the division by $86\,400$:

```console
>>> -3600 % 86400
82800
>>> 82800 // 3600
23
```

$82\,800\,\mathrm s=23\,\mathrm h$, so the time of day is 23:00:00 on the previous day. This works only because, for a positive divisor, `%` always returns a remainder between 0 and $86\,399$, even for negative $t$.
:::
:::

:::aufgabe Exercise 7 ★ Angles in the range from $0^\circ$ to $360^\circ$
<span class="anker" id="aufg-7"></span>

A program for a compass display computes directions in degrees that can lie outside $0^\circ$ to $360^\circ$. Bring $-90^\circ$, $450^\circ$, $-450^\circ$ and $720^\circ$ into this range with one operator. What result would you have gotten for $-90^\circ$ if `%` calculated as in C?

:::loesung
The remainder of the division by 360 always lies in the range from 0 to 359:

```console
>>> -90 % 360
270
>>> 450 % 360
90
>>> -450 % 360
270
>>> 720 % 360
0
```

If `%` rounded toward zero as in C, the quotient of $-90/360=-0.25$ would be the number 0 and the remainder $-90-0\cdot360=-90$. The angle would stay negative, and you would need an additional case distinction.
:::
:::

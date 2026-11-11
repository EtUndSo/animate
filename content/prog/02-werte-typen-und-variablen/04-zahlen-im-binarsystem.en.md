---
title: Numbers in the binary system
pfad: Computer Science / Programming / Python / Values, Types and Variables
adresse: informatik/programmieren/python/werte-typen-und-variablen
knoten: Chapter 2: Values, Types and Variables
order: 6030400
summary: Computers store numbers as sequences of zeros and ones.
tags: base, binary number, bit, byte, hexadecimal number, binary fraction, doubling method
lang: en
---

<span class="anker" id="stufe-3"></span>

:::zweck
Computers store numbers as sequences of zeros and ones. This section explains the binary system, shows how to convert by hand and with Python, and clarifies which fractions can be written with finitely many digits in the binary system.
:::

### The positional numeral system

<span class="anker" id="stufe-3-1"></span>

To understand how a computer stores numbers, you first have to say precisely what a sequence of digits such as 4705 actually means. Then the same idea can be carried over to bases other than 10.

**Thousands, hundreds, tens, ones.** In 4705, the 4 stands for four thousands, the 7 for seven hundreds, the 0 for no tens and the 5 for five ones. Each position is worth ten times as much as the one to its right.

:::definition Definition 3.1 (Positional numeral system)
<span class="anker" id="satz-3-1"></span>

Let $B\ge2$ be a natural number, the __base__. In the positional numeral system with base $B$, a sequence of digits $z_{n-1}\ldots z_1z_0$ with $0\le z_i<B$ stands for the number

$$z_{n-1}B^{n-1}+\dots+z_1B^1+z_0B^0=\sum_{i=0}^{n-1}z_i\,B^i .$$

The number $B^i$ is called the place value of position $i$. Positions are counted from the right, starting at $i=0$.
:::

::::beispiel
In the familiar decimal system, $B=10$: $4705=4\cdot10^3+7\cdot10^2+0\cdot10^1+5\cdot10^0=4000+700+0+5$.
::::

⁠**In short:** In a positional numeral system, each digit is multiplied by the place value of its position, and everything is added up.

### The binary number

<span class="anker" id="stufe-3-2"></span>

A memory cell of the computer distinguishes only two states, like a light switch: on or off. For numbers, you therefore need a positional numeral system with only two digits.

**Switches that double.** Picture a row of switches. The rightmost one counts 1, the next 2, then 4, 8, 16: each counts twice as much as its right neighbor. The number is the sum of the values of all switches that are on.

:::definition Definition 3.2 (Binary number)
<span class="anker" id="satz-3-2"></span>

A __binary number__ is a number in the positional numeral system with base $B=2$. Its digits are 0 and 1.
:::

A digit of a binary number is called a __bit__, short for *binary digit*. This chapter denotes the bits of a number by $b_i$, counted from the right starting at $i=0$. So that a binary number is not confused with a decimal number, you write the base as a small number after it: $10011_2$. The value is

$$b_{n-1}\ldots b_1b_0\,{}_2=\sum_{i=0}^{n-1}b_i\,2^i .$$

::::beispiel
$10011_2$ has the bits $b_4=1$, $b_3=0$, $b_2=0$, $b_1=1$, $b_0=1$. The calculation is shown step by step in Fig. [3](#abb-3): the number is 19.

:::abbildung prog/k2rbinaer 3
The value of the binary number $10011_2$: each bit times its place value, then add.
:::
::::

In Python, you write a binary number with the prefix `0b`. The interactive mode displays it as a decimal number, because the object is an ordinary `int`:

```console
>>> 0b10011
19
>>> type(0b10011)
<class 'int'>
```

The method `bit_length` of an `int` tells how many bits the number needs without leading zeros:

```console
>>> (19).bit_length()
5
```

⁠**In short:** A binary number has only the digits 0 and 1, the bits; each bit counts $2^i$.

### The byte

<span class="anker" id="stufe-3-3"></span>

A single bit can distinguish only two values. Memory and data transmission therefore work with groups of bits of a fixed size.

:::definition Definition 3.3 (Byte)
<span class="anker" id="satz-3-3"></span>

A __byte__ is a group of 8 bits.
:::

With $n$ bits, you can form $2^n$ different patterns, because each bit doubles the number of possibilities. A byte thus has $2^8=256$ patterns and can represent the integers from 0 to 255. Memory sizes are counted in bytes: a 64-bit number occupies 8 bytes.

::::beispiel
The largest number in a byte has all eight bits set. Its value is the sum of all eight place values (Fig. [4](#abb-4)):

:::abbildung prog/k2rbyte 4
The largest value of a byte: all eight bits are 1, and the place values $2^0$ to $2^7$ are added. The result is $255=2^8-1$.
:::
::::

The result is one less than the next place value $2^8=256$. This holds for every number made of ones only: $n$ ones give $2^n-1$, just as $999=10^3-1$ in the decimal system.

⁠**In short:** A byte is 8 bits; it can take 256 different values, the numbers 0 to 255.

### Converting to binary: first by hand, then ready-made

<span class="anker" id="stufe-3-4"></span>

Fig. [3](#abb-3) converts from binary to decimal. For the opposite direction, there is a method that needs only floor division and remainder.

**The idea.** If you divide an integer $n\ge0$ by 2, the remainder is the last bit $b_0$: all other place values $2,4,8,\ldots$ are even; only $b_0\cdot1$ can contribute an odd part. The quotient $n\,/\!/\,2$ contains the remaining bits, moved one position to the right. If you divide it by 2 again, the remainder is $b_1$, and so on, until the quotient is 0.

**By hand.** The remainders, read from bottom to top, are the bits. In interactive mode, `divmod` does each step:

```console
>>> divmod(19, 2)
(9, 1)
>>> divmod(9, 2)
(4, 1)
>>> divmod(4, 2)
(2, 0)
>>> divmod(2, 2)
(1, 0)
>>> divmod(1, 2)
(0, 1)
```

| $n$ | $n\,/\!/\,2$ | $n\,\%\,2$ | Bit |
|---|---|---|---|
| 19 | 9 | 1 | $b_0$ |
| 9 | 4 | 1 | $b_1$ |
| 4 | 2 | 0 | $b_2$ |
| 2 | 1 | 0 | $b_3$ |
| 1 | 0 | 1 | $b_4$ |

Read from the bottom: $b_4b_3b_2b_1b_0=10011$, so $19=10011_2$.

**Ready-made.** Python comes with the conversion. The function `bin` returns the binary representation as a string with the prefix `0b`; the function `format` with the specifier `"b"` returns it without the prefix, and with `"08b"` padded to eight digits with leading zeros. For the way back, the function `int` takes a string and the base:

```console
>>> bin(19)
'0b10011'
>>> format(19, "b")
'10011'
>>> format(19, "08b")
'00010011'
>>> int("10011", 2)
19
>>> bin(-19)
'-0b10011'
```

Python writes negative numbers with a minus sign before the prefix, just as you also write them in the decimal system.

**Comparison.** By hand and ready-made, the same bits appear: $10011$. The ready-made way is shorter and makes no reading errors when reversing the remainders; you need the way by hand to understand why the remainders are the bits.

⁠**In short:** Repeated division by 2 yields the bits as remainders, the last bit first; ready-made, `bin` and `format` do the job.

### The hexadecimal number

<span class="anker" id="stufe-3-5"></span>

Bit sequences quickly become long and hard to read: nobody reads out $0011111111111011$ without errors. You need a shorter notation from which you can still read off the bits immediately.

**Four bits are one digit.** Four bits have $2^4=16$ patterns. If you give each of these 16 patterns a character of its own, you can split any bit sequence into groups of four and replace each group by one character.

:::definition Definition 3.4 (Hexadecimal number)
<span class="anker" id="satz-3-4"></span>

A __hexadecimal number__ is a number in the positional numeral system with base $B=16$. The digits are `0` to `9` and `a` to `f` for the values 10 to 15.
:::

Because $16=2^4$, each hexadecimal digit stands for exactly four bits:

| `0` | `1` | `2` | `3` | `4` | `5` | `6` | `7` |
|---|---|---|---|---|---|---|---|
| `8` | `9` | `a` | `b` | `c` | `d` | `e` | `f` |
| 1000 | 1001 | 1010 | 1011 | 1100 | 1101 | 1110 | 1111 |

So a byte is exactly two hexadecimal digits.

::::beispiel
$255=1111\,1111_2$ is $\mathtt{ff}_{16}$ in hexadecimal, because $15\cdot16+15=255$. You split the long bit sequence from the beginning of this subsection into groups of four, starting from the right: $0011\;1111\;1111\;1011_2=\mathtt{3ffb}_{16}$. In Python, you write hexadecimal numbers with the prefix `0x`; `hex` converts, and `int` with the base 16 converts back:

```console
>>> 0xff
255
>>> hex(255)
'0xff'
>>> int("3ffb", 16)
16379
>>> bin(0x3ffb)
'0b11111111111011'
```

In the output of `bin`, the two leading zeros of the first group of four are missing; Python leaves out leading zeros.
::::

⁠**In short:** Hexadecimal is base 16; each digit stands for four bits, a byte for two digits.

### Binary fractions

<span class="anker" id="stufe-3-6"></span>

Prices, weights and temperatures have decimal places. A computer must be able to write them with zeros and ones, too.

**Digits to the right of the point.** In the decimal system, the digits to the right of the decimal point mean tenths, hundredths, thousandths. In the binary system, the place value halves from position to position: halves, quarters, eighths, sixteenths.

:::definition Definition 3.5 (Binary fraction)
<span class="anker" id="satz-3-5"></span>

A __binary fraction__ is a number in the binary system with digits to the right of the point, the binary point. Position $k$ to the right of the point has the place value $2^{-k}$:

$$0.b_{-1}b_{-2}\ldots b_{-m}\,{}_2=\sum_{k=1}^{m}b_{-k}\,2^{-k} .$$
:::

::::beispiel
$0.101_2=1\cdot\tfrac12+0\cdot\tfrac14+1\cdot\tfrac18=\tfrac58=0.625$ and $0.011_2=\tfrac14+\tfrac18=\tfrac38=0.375$.
::::

Not every fraction can be written as a finite binary fraction. In the decimal system, this is familiar: $\frac14=0.25$ terminates, $\frac13=0.333\ldots$ does not. The following theorem says which numbers terminate in the binary system.

:::satz Theorem 3.6 (Finite binary fractions)
<span class="anker" id="satz-3-6"></span>

A number $x$ can be written as a binary fraction with finitely many digits exactly when there is an integer $p\ge0$ such that $x\cdot2^p$ is an integer.
:::

:::beweis Shifting the point
In the binary system, multiplying by $2^p$ shifts the point $p$ positions to the right, just as multiplying by $10^p$ does in the decimal system.

If $x$ has at most $p$ digits to the right of the point, then after the shift no digit is left to the right of the point, and $x\cdot2^p$ is an integer.

Conversely, if $x\cdot2^p=n$ is an integer, $n$ has a finite binary representation. Shifting the point in it $p$ positions to the left gives $x=n\cdot2^{-p}$ with at most $p$ digits to the right of the point.
:::

**Applying it to $\frac38$ and $\frac1{10}$.** $\frac38\cdot2^3=3$ is an integer, so the binary fraction terminates, namely after three digits. For $\frac1{10}$, we get $\frac1{10}\cdot2^p=\frac{2^{p}}{10}=\frac{2^{p-1}}{5}$. But a power of two is never divisible by 5, because its only prime factors are twos. For no $p$ is this an integer: *in the binary system, $0.1$ has infinitely many digits.* The same holds for every fraction in lowest terms whose denominator contains a prime factor other than 2, for example $0.2=\frac15$ and $0.3=\frac3{10}$.

⁠**In short:** A binary fraction terminates exactly when the denominator in lowest terms is a power of two; $0.1$ does not terminate.

### The doubling method

<span class="anker" id="stufe-3-7"></span>

What do the infinitely many binary digits of $0.1$ look like? For the digits to the right of the point, there is a method that corresponds to dividing by 2 for integers.

**The idea.** If you multiply a binary fraction $0.b_{-1}b_{-2}b_{-3}\ldots{}_2$ by 2, the point moves one position to the right: the result is $b_{-1}.b_{-2}b_{-3}\ldots{}_2$. In front of the point there is now the first digit $b_{-1}$, that is, 0 or 1, and behind it the rest. You repeat this with the rest.

:::definition Definition 3.7 (Doubling method)
<span class="anker" id="satz-3-7"></span>

For $0\le x<1$, the __doubling method__ determines the binary digits of $x$: you double $x$. The integer part of the result, 0 or 1, is the next digit; you continue with the part to the right of the point. The method ends when this part is 0.
:::

::::beispiel [Example 1] $0.625$
$2\cdot0.625=1.25$, digit 1, continue with $0.25$. $2\cdot0.25=0.5$, digit 0. $2\cdot0.5=1.0$, digit 1, rest 0, done: $0.625=0.101_2$, as in the previous subsection.
::::

::::beispiel [Example 2] $0.1$
To keep rounding from creeping in, you calculate with the fraction $\frac{z}{10}$ and double only the integer numerator $z$. If $2z\ge10$, the digit is 1 and you subtract 10; otherwise, the digit is 0:

| Step | Fraction | doubled | Digit |
|---|---|---|---|
| 1 | $1/10$ | $2/10$ | 0 |
| 2 | $2/10$ | $4/10$ | 0 |
| 3 | $4/10$ | $8/10$ | 0 |
| 4 | $8/10$ | $16/10=1+6/10$ | 1 |
| 5 | $6/10$ | $12/10=1+2/10$ | 1 |
| 6 | $2/10$ | $4/10$ | 0 |
| 7 | $4/10$ | $8/10$ | 0 |
| 8 | $8/10$ | $16/10=1+6/10$ | 1 |
| 9 | $6/10$ | $12/10=1+2/10$ | 1 |

In step 6, the same fraction $2/10$ appears as in step 2. From there on, everything repeats, and the digits $0011$ come back endlessly:

$$0.1=0.0\,0011\,0011\,0011\ldots{}_2 .$$

How close you get to $0.1$ with the first digits is shown by the sum of the place values. The ones come in pairs: at positions 4 and 5, then 8 and 9, then 12 and 13, and so on. A pair at positions $4k$ and $4k+1$ is worth $2^{-4k}+2^{-(4k+1)}=3\cdot2^{-(4k+1)}$. The first four pairs, that is, the first 17 digits, give (Fig. [5](#abb-5))

:::abbildung prog/k2rnull 5
The first four pairs of ones in the binary fraction of $0.1$, as the sum of their place values. After 17 digits, about $1.5\cdot10^{-6}$ is still missing to reach $0.1$, and with each further group of four digits, the rest shrinks to one sixteenth.
:::
::::

The sum comes ever closer to $0.1$ but does not reach it with any finite number of digits. The error after the 17 digits is $0.1-\frac{13107}{131072}=\frac{1}{655360}=0.1\cdot2^{-16}$: after digit 17, the same pattern as in $0.1$ itself follows again, only moved 16 positions to the right.

⁠**In short:** Doubling moves the next binary digit in front of the point; for $0.1$, this gives the infinite sequence $0.0\,0011\,0011\ldots{}_2$.

:::hintergrund Why the digits have to repeat
In the method for $0.1$, each step leaves a fraction $\frac{z}{10}$ with a numerator $z$ from 0 to 9. So there are only ten possible states. After ten steps at the latest, one of them must occur for the second time, and because each step depends only on the current fraction, everything repeats from there on. The same argument shows that every fraction $\frac{z}{q}$ in every positional numeral system either terminates or becomes periodic, with a period of fewer than $q$ digits. In the decimal system, you know this from $\frac17=0.\overline{142857}$.
:::

### Exercises for Section [3](#stufe-3)

<span class="anker" id="stufe-3-8"></span>

:::aufgabe Exercise 8 ★ Binary to decimal and back
<span class="anker" id="aufg-8"></span>

<ol class="al">

<li>

Compute the value of $101101_2$ and of $1000000_2$ by hand. Check with `0b`.

</li>

<li>

Convert 2026 to binary by hand using repeated division. Check with `bin`.

</li>

<li>

How many bits does 2026 need? Check with the method `bit_length`.

</li>

</ol>

:::loesung
(a) $101101_2=32+8+4+1=45$ and $1000000_2=2^6=64$.

(b) Repeated division by 2, remainders from bottom to top:

| $n$ | $n\,/\!/\,2$ | $n\,\%\,2$ | $n$ | $n\,/\!/\,2$ | $n\,\%\,2$ |
|---|---|---|---|---|---|
| 2026 | 1013 | 0 | 31 | 15 | 1 |
| 1013 | 506 | 1 | 15 | 7 | 1 |
| 506 | 253 | 0 | 7 | 3 | 1 |
| 253 | 126 | 1 | 3 | 1 | 1 |
| 126 | 63 | 0 | 1 | 0 | 1 |
| 63 | 31 | 1 |  |  |  |

Read from the bottom: $2026=11111101010_2$.

(c) Eleven bits. Everything checked together:

```console
>>> 0b101101
45
>>> 0b1000000
64
>>> bin(2026)
'0b11111101010'
>>> (2026).bit_length()
11
```

Check: $2^{10}=1024\le2026<2048=2^{11}$, so 2026 needs eleven digits.
:::
:::

:::aufgabe Exercise 9 ★ Reading hexadecimal
<span class="anker" id="aufg-9"></span>

<ol class="al">

<li>

Write $\mathtt{c8}_{16}$ and $\mathtt{3fb}_{16}$ as bit sequences and as decimal numbers.

</li>

<li>

How many hexadecimal digits does a 64-bit number need?

</li>

<li>

Check (a) with `int` and `bin`.

</li>

</ol>

:::loesung
(a) Each hexadecimal digit gives four bits: $\mathtt{c8}_{16}=1100\,1000_2=12\cdot16+8=200$ and $\mathtt{3fb}_{16}=0011\,1111\,1011_2=3\cdot256+15\cdot16+11=1019$. This is the exponent field of $0.1$ from Fig. [7](gleitkommazahlen-der-typ-float.html#abb-7).

(b) $64/4=16$ hexadecimal digits.

(c)

```console
>>> int("c8", 16)
200
>>> bin(0xc8)
'0b11001000'
>>> int("3fb", 16)
1019
>>> bin(0x3fb)
'0b1111111011'
```

For $\mathtt{3fb}$, `bin` leaves out the two leading zeros.
:::
:::

:::aufgabe Exercise 10 ★★ Finite or not?
<span class="anker" id="aufg-10"></span>

Use Theorem [3.6](#satz-3-6) to decide which numbers have a finite binary fraction, and give it where it exists: $0.75$, $0.2$, $0.375$, $\frac13$, $0.05$, $12.5$.

:::loesung
According to Theorem [3.6](#satz-3-6), what matters is whether the denominator in lowest terms is a power of two:

<ul>

<li>

$0.75=\frac34$, denominator $4=2^2$: finite, $0.11_2$.

</li>

<li>

$0.2=\frac15$: denominator 5, not finite.

</li>

<li>

$0.375=\frac38$, denominator $2^3$: finite, $0.011_2$.

</li>

<li>

$\frac13$: denominator 3, not finite.

</li>

<li>

$0.05=\frac1{20}$, denominator $20=4\cdot5$ contains 5: not finite.

</li>

<li>

$12.5=\frac{25}2$: finite, $12.5=8+4+\frac12=1100.1_2$.

</li>

</ul>
:::
:::

:::aufgabe Exercise 11 ★★ How finely does a kitchen scale weigh?
<span class="anker" id="aufg-11"></span>

A digital kitchen scale stores each weight as a 12-bit integer. The range from 0 to $5\,\mathrm{kg}$ is divided into steps of equal width, one step for each bit pattern.

<ol class="al">

<li>

How many steps are there, and what is the largest number the scale stores?

</li>

<li>

How wide is one step in grams? Calculate with Python.

</li>

<li>

Is the step width in kilograms a finite binary fraction? Justify your answer with Theorem [3.6](#satz-3-6).

</li>

</ol>

:::loesung
(a) 12 bits have $2^{12}=4096$ patterns, so there are 4096 steps. The largest number is $4095=2^{12}-1$, twelve ones.

(b)

```console
>>> 2 ** 12
4096
>>> 5 / 4096 * 1000
1.220703125
```

One step is $1.220703125\,\mathrm g$ wide: this scale cannot reliably tell apart weights that are less than one step apart.

(c) $\frac5{4096}\cdot2^{12}=5$ is an integer, so the step width is a finite binary fraction: $\frac{5}{4096}=101_2\cdot2^{-12}=0.000000000101_2$. That is also why Python shows no rounding digits: the result is exact, because $1.220703125=\frac{625}{512}$, too, has a denominator that is a power of two.
:::
:::

:::aufgabe Exercise 12 ★★ $0.3$ by hand
<span class="anker" id="aufg-12"></span>

Use the doubling method to determine the first twelve binary digits of $0.3$. As in the example, calculate with fractions $\frac{z}{10}$. From which step on does the pattern repeat, and how long is the period?

:::loesung
You double the numerator of $\frac{z}{10}$; from 10 on, the digit is 1, and 10 is subtracted:

| Step | Fraction | Doubled | Digit | Step | Fraction | Doubled | Digit |
|---|---|---|---|---|---|---|---|
| 1 | $3/10$ | $6/10$ | 0 | 7 | $2/10$ | $4/10$ | 0 |
| 2 | $6/10$ | $1+2/10$ | 1 | 8 | $4/10$ | $8/10$ | 0 |
| 3 | $2/10$ | $4/10$ | 0 | 9 | $8/10$ | $1+6/10$ | 1 |
| 4 | $4/10$ | $8/10$ | 0 | 10 | $6/10$ | $1+2/10$ | 1 |
| 5 | $8/10$ | $1+6/10$ | 1 | 11 | $2/10$ | $4/10$ | 0 |
| 6 | $6/10$ | $1+2/10$ | 1 | 12 | $4/10$ | $8/10$ | 0 |

The first twelve digits: $0.3=0.010011001100\ldots{}_2$. In step 7, $\frac2{10}$ appears again, as in step 3; from there on, everything repeats. So the period begins at step 3 and has length 4: $0.01\,0011\,0011\ldots{}_2$. It is the same period $0011$ as for $0.1$, only at a different position, because $0.3=0.2+0.1$ and both have the sequence of numerators $2,4,8,6$.
:::
:::

---
title: Strings, input and output
pfad: Computer Science / Programming / Python / Values, Types and Variables
adresse: informatik/programmieren/python/werte-typen-und-variablen
knoten: Chapter 2: Values, Types and Variables
order: 6031100
summary: A program should ask for values and output results neatly formatted.
tags: concatenation, f-string, type conversion
lang: en
---

<span class="anker" id="stufe-10"></span>

:::zweck
A program should ask for values and output results neatly formatted. This section shows how to calculate with strings, insert numbers into text with a chosen format, read input, convert text and numbers into each other, and round. At the end, you build a small running pace calculator.
:::

### Concatenating and repeating strings

<span class="anker" id="stufe-10-1"></span>

[Chapter 1](/wissen/en/informatik/programmieren/python/programme-und-der-python-interpreter/programme-und-der-python-interpreter.html) introduced the string as a value made of text ([Chapter 1, Section 4.6](/wissen/en/informatik/programmieren/python/programme-und-der-python-interpreter/der-interaktive-modus.html#stufe-4-6)); its type is called `str`. You can do some calculating with text, too: join pieces together, build lines out of dashes, determine the length.

:::definition Definition 10.1 (Operators and length of strings)
<span class="anker" id="satz-10-1"></span>

For strings, `+` means joining end to end, called __concatenation__: `"Regen" + "schirm"` is `"Regenschirm"` (German for “umbrella”). `*` with an `int` repeats the string. The built-in function `len` returns the number of characters.
:::

::::beispiel
Concatenating, repeating, counting:

```console
>>> "Regen" + "schirm"
'Regenschirm'
>>> "ha" * 3
'hahaha'
>>> "-" * 20
'--------------------'
>>> len("Regen")
5
>>> len("Größe")
5
>>> len("")
0
>>> "4" + "2"
'42'
```

`""` is the empty string, with zero characters. `"4" + "2"` gives the text `'42'`, not the number 6: for `str`, `+` means concatenation, no matter what is inside the string.
::::

⁠**In short:** For strings, `+` concatenates, `*` repeats, and `len` counts the characters.

### The f-string

<span class="anker" id="stufe-10-2"></span>

`print("Preis pro kg in Euro:", kilopreis)` prints 16 digits where two decimal places are enough. For neat output, you want to put numbers in the middle of a text and decide how many digits appear.

**A form with blanks.** You write the text down once and leave blanks; each blank receives a calculated value, in the desired form.

:::definition Definition 10.2 (f-string)
<span class="anker" id="satz-10-2"></span>

An __f-string__ is a string with an `f` before the opening quotation mark. Every expression in curly braces `{...}` is evaluated, and its value is inserted as text at this position.
:::

After the expression, separated by a colon, there can be a format specifier. It determines how the value appears as text:

| Format specifier | Meaning | Example and result |
|---|---|---|
| `.2f` | 2 decimal places | `f"{3.14159:.2f}"` gives `3.14` |
| `.3e` | scientific notation | `f"{0.0125:.3e}"` gives `1.250e-02` |
| `8.3f` | at least 8 characters wide | `f"{3.14159:8.3f}"` gives ` 3.142` |
| `5d` | integer, 5 characters wide | `f"{42:5d}"` gives ` 42` |
| `,.2f` | with thousands separator | `f"{1234567.891:,.2f}"` gives `1,234,567.89` |
| `.1%` | as a percentage | `f"{0.256:.1%}"` gives `25.6%` |
| `08b` | binary with 8 digits | `f"{19:08b}"` gives `00010011` |
| `x` | hexadecimal | `f"{255:x}"` gives `ff` |

If the expression is followed by an equals sign, `f"{gewicht=}"`, Python inserts the expression itself, an `=` and the value; this is handy for looking at intermediate values. The format specifiers are the same as for the function `format` from subsection [3.4](zahlen-im-binarsystem.html#stufe-3-4). As in all Python output, the decimal point is written as a point and the thousands separator as a comma.

::::beispiel
Lines for the receipt at the cheese counter, with the price per kilogram and the weight:

```console
>>> kilopreis = 26.4
>>> gewicht = 0.125
>>> f"Gewicht = {gewicht} kg, also {gewicht * 1000:.1f} g"
'Gewicht = 0.125 kg, also 125.0 g'
>>> f"Preis = {kilopreis * gewicht:.2f} Euro"
'Preis = 3.30 Euro'
>>> f"Pro Gramm: {kilopreis / 1000:.3e} Euro"
'Pro Gramm: 2.640e-02 Euro'
>>> f"{gewicht=}"
'gewicht=0.125'
>>> print(f"Zu zahlen: {kilopreis * gewicht:.2f} Euro")
Zu zahlen: 3.30 Euro
```

The interactive mode displays an f-string as a string in single quotes; only `print` outputs the bare text.
::::

**The stored value of `0.1`, ready-made.** In subsection [4.6](gleitkommazahlen-der-typ-float.html#stufe-4-6), the calculation with $5^{55}$ by hand gave the 55 decimal places of the stored value of `0.1`. With a format specifier, you get them directly:

```console
>>> f"{0.1:.20f}"
'0.10000000000000000555'
>>> f"{0.1:.55f}"
'0.1000000000000000055511151231257827021181583404541015625'
```

The same digits as by hand. A format specifier rounds only the display; the value of the object stays as it is.

⁠**In short:** An f-string inserts the values in `{...}` into a text; after the colon, a format specifier determines the digits and the form.

### Input with `input`

<span class="anker" id="stufe-10-3"></span>

So far, all values have been in the source code. But a calculator for everyday use should ask for the numbers it calculates with.

:::definition Definition 10.3 (`input`)
<span class="anker" id="satz-10-3"></span>

The built-in function `input` writes the text in its parentheses to the terminal as a question, waits until the user types a line and presses Enter, and returns this line as a string, without the Enter.
:::

::::beispiel
In interactive mode, the question appears (here: the number of guests), and after it you type the answer, here `5`:

```console
>>> gaeste = input("Anzahl Gäste: ")
Anzahl Gäste: 5
>>> gaeste
'5'
>>> type(gaeste)
<class 'str'>
>>> gaeste * 2
'55'
```

`input` *always* returns a string, even if you type in a number. That is why `gaeste * 2` repeats the text instead of calculating. Calculating with an input requires a further step.
::::

⁠**In short:** `input` asks for a line and returns it as a `str`.

### Type conversion

<span class="anker" id="stufe-10-4"></span>

The text `'5'` should become the number 5, the number 42 the text `'42'`. Python never converts on its own (subsection [1.2](objekte-und-typen.html#stufe-1-2)); you have to ask for it explicitly.

:::definition Definition 10.4 (Type conversion)
<span class="anker" id="satz-10-4"></span>

The functions `int`, `float` and `str` create a new object from a value, with the type of their name. This is called __type conversion__.

<ul>

<li>

`int(text)` and `float(text)` read a number from a string; spaces at the edges are allowed. If the text does not fit, they raise a `ValueError`.

</li>

<li>

`int(x)` turns a `float` into an integer by cutting off the decimal places, that is, by rounding toward zero.

</li>

<li>

`str(x)` returns the text that `print` would output for $x$.

</li>

</ul>
:::

::::beispiel
Conversions that succeed, and two that fail:

```console
>>> int("42")
42
>>> int(" 42 ")
42
>>> float("4.2")
4.2
>>> float("1e3")
1000.0
>>> int("4.2")
Traceback (most recent call last):
  File "<python-input-4>", line 1, in <module>
    int("4.2")
    ~~~^^^^^^^
ValueError: invalid literal for int() with base 10: '4.2'
>>> float("2,5")
Traceback (most recent call last):
  File "<python-input-5>", line 1, in <module>
    float("2,5")
    ~~~~~^^^^^^^
ValueError: could not convert string to float: '2,5'
>>> str(42) + "1"
'421'
>>> int(3.99)
3
>>> int(-3.99)
-3
```

`int("4.2")` fails because `4.2` is not an integer; `int(float("4.2"))` would work. `float("2,5")` fails because of the comma: Python expects the decimal point, in input as well, so keep this in mind if you are used to writing a decimal comma. For numbers from `input`, the typical pattern is therefore `float(input("..."))`.
::::

⁠**In short:** `int`, `float` and `str` convert explicitly; `int` cuts off the decimal places.

:::hintergrund Why Python does not convert between text and numbers on its own
What should `"2" + 3` give, the text `'23'` or the number 5? Some languages silently choose one of the two possibilities, JavaScript, for example, chooses `'23'`. Then a program calculates wrongly with numbers it has read in, without anyone noticing. Python follows the principle of not guessing in the face of ambiguity: it raises a `TypeError` and forces you to say what you mean with `int`, `float` or `str`. Between numeric types, on the other hand, Python does convert on its own (subsection [2.2](ganze-zahlen-und-rechenoperatoren.html#stufe-2-2)), because there the meaning is unambiguous: $2+3.0$ is $5.0$.
:::

### Rounding: first by hand, then ready-made

<span class="anker" id="stufe-10-5"></span>

`3 * 1.1` gives `3.3000000000000003`, the price of three notebooks at €$1.10$ each, with a rounding residue. You want to round such a result to an integer or to a few digits, and not only in the display, but as a value that you continue calculating with.

**By hand.** `int` cuts off. If you add $0.5$ first, cutting off turns into rounding: $2.7+0.5=3.2$ becomes 3, $2.2+0.5=2.7$ becomes 2. This is the rule taught at school, “round up from 5”:

```console
>>> int(2.7 + 0.5)
3
>>> int(2.5 + 0.5)
3
>>> int(3.5 + 0.5)
4
>>> int(-2.7 + 0.5)
-2
```

The last line is wrong: $-2.7$ is closer to $-3$. Because `int` cuts off toward zero, the trick works only for positive numbers.

**Ready-made.** The built-in function `round` rounds correctly, including negative numbers.

:::definition Definition 10.5 (`round`)
<span class="anker" id="satz-10-5"></span>

`round(x)` returns the integer closest to $x$. If $x$ lies exactly halfway between two integers, `round` returns the even one of the two. `round(x, n)` rounds to $n$ decimal places and returns a `float`.
:::

```console
>>> round(2.7)
3
>>> round(-2.7)
-3
>>> round(2.5)
2
>>> round(3.5)
4
>>> round(-2.5)
-2
>>> round(3.14159, 2)
3.14
>>> round(2.675, 2)
2.67
>>> f"{2.675:.20f}"
'2.67499999999999982236'
```

`round(2.675, 2)` gives $2.67$ and not $2.68$, and that is not an error: the stored value of `2.675` lies just below $2.675$, as the last line shows, so $2.67$ is the nearest number with two decimal places. If you want to round down or round up, use `math.floor` or `math.ceil`.

**Comparison.**

| $x$ | `int(x + 0.5)` | `round(x)` |
|---|---|---|
| $2.7$ | 3 | 3 |
| $2.5$ | 3 | 2 |
| $3.5$ | 4 | 4 |
| $-2.5$ | $-2$ | $-2$ |
| $-2.7$ | $-2$ | $-3$ |

The two ways differ in two places: for exact halves such as $2.5$, where `round` goes to the even number, and for negative numbers, where the way by hand is wrong. The ready-made way is correct for all numbers and follows the same rule as the rounding of `float` values in subsection [4.6](gleitkommazahlen-der-typ-float.html#stufe-4-6).

⁠**In short:** `round` rounds to the nearest number and, for exact halves, to the even one; `int(x + 0.5)` works only for positive numbers and always rounds halves up.

:::hintergrund Why rounding goes to the even number
The rule from school rounds every exact half up. With many rounded values, this adds up to an error that always points in the same direction. An example: $0.5+1.5+2.5+3.5=8$. Rounded by the school rule, the sum becomes $1+2+3+4=10$. Rounded to the even number, it becomes $0+2+2+4=8$: half of the cases go up, the other half down, and on average the errors cancel out. That is why IEEE 754, in its default setting, rounds every calculation with `float` to the even significand in a tie, and Python adopts the same rule for `round`. It also prevents a value that you repeatedly subtract and add back from slowly drifting in one direction.
:::

### Application: a running pace calculator

<span class="anker" id="stufe-10-6"></span>

With `input`, `float` and an f-string, you can write a small tool for runners: it asks for the distance and time of a run and outputs the pace in two forms, in kilometers per hour and in minutes per kilometer, the measure common in running. If you divide the minutes by the kilometers, the second measure comes out directly; for the first, you convert the minutes to hours beforehand.

```python tempo.py
# Pace calculator: the pace of a run in two forms
strecke = float(input("Strecke in km: "))
zeit = float(input("Zeit in min: "))

km_pro_h = strecke / (zeit / 60)     # convert minutes to hours
min_pro_km = zeit / strecke          # min / km gives min per km

print(f"Tempo: {km_pro_h:.2f} km/h")
print(f"Zeit pro km: {min_pro_km:.2f} min")
```

When started, the script asks for the two values one after the other; here, 5.2 and 27 are typed in:

```console Windows (PowerShell)
PS> py tempo.py
Strecke in km: 5.2
Zeit in min: 27
Tempo: 11.56 km/h
Zeit pro km: 5.19 min
```

```console Linux
$ python3 tempo.py
Strecke in km: 5.2
Zeit in min: 27
Tempo: 11.56 km/h
Zeit pro km: 5.19 min
```

If you type `5,2` with a decimal comma, the script aborts with the `ValueError` from subsection [10.4](#stufe-10-4). Catching such inputs and asking again is a skill of its own that this chapter does not need.

⁠**In short:** `float(input(...))` reads a number, and an f-string outputs the result with a suitable number of digits.

### Exercises for Section [10](#stufe-10)

<span class="anker" id="stufe-10-7"></span>

:::aufgabe Exercise 37 ★ Text and number
<span class="anker" id="aufg-37"></span>

Predict and check: (a) `"ab" * 3`, (b) `"Bus" + str(42)`, (c) `len("Bahn") * 2`, (d) `int("7") + int("3")`, (e) `"7" + "3"`, (f) `str(1 / 4)`.

:::loesung
```console
>>> "ab" * 3
'ababab'
>>> "Bus" + str(42)
'Bus42'
>>> len("Bahn") * 2
8
>>> int("7") + int("3")
10
>>> "7" + "3"
'73'
>>> str(1 / 4)
'0.25'
```

(b) `str` turns the number into text; only then does `+` work. (c) `len` returns 4, an `int`, and $4\cdot2=8$ is a calculation, not a repetition. (d) and (e) show the difference: after the conversion into numbers, `+` calculates; with text, it concatenates.
:::
:::

:::aufgabe Exercise 38 ★★ Formatting
<span class="anker" id="aufg-38"></span>

For each line, write an f-string that produces exactly this text from the given variables.

<ol class="al">

<li>

`strecke = 4700` (in meters) $\to$ `Strecke = 4.70 km`

</li>

<li>

`menschen = 8.1e9` $\to$ `Menschen auf der Erde: 8.10e+09`

</li>

<li>

`anteil = 0.125` $\to$ `Anteil: 12.5%`

</li>

<li>

`c_feld = 1019` $\to$ `0x3fb` and `01111111011`

</li>

</ol>

:::loesung
```console
>>> strecke = 4700
>>> f"Strecke = {strecke / 1000:.2f} km"
'Strecke = 4.70 km'
>>> menschen = 8.1e9
>>> f"Menschen auf der Erde: {menschen:.2e}"
'Menschen auf der Erde: 8.10e+09'
>>> anteil = 0.125
>>> f"Anteil: {anteil:.1%}"
'Anteil: 12.5%'
>>> c_feld = 1019
>>> f"{c_feld:#x}"
'0x3fb'
>>> f"{c_feld:011b}"
'01111111011'
```

(a) A whole expression may stand in the curly braces, here the conversion from meters to kilometers. (b) `.2e` writes the number in scientific notation with two decimal places. (c) The specifier `%` multiplies by 100 and appends the percent sign. (d) `#x` adds the prefix `0x`; `011b` pads with zeros to 11 digits, as in the exponent field of $0.1$ in Fig. [7](gleitkommazahlen-der-typ-float.html#abb-7).
:::
:::

:::aufgabe Exercise 39 ★★ Rounding by hand and ready-made
<span class="anker" id="aufg-39"></span>

Fill in the table for $x=0.5$, $1.5$, $-0.5$, $-1.5$, $4.49$ with the columns `int(x + 0.5)`, `round(x)`, `math.floor(x)`, `int(x)`. Predict first, then check. For which values do all four columns give the same result?

:::loesung
```console
>>> import math
>>> int(0.5 + 0.5), round(0.5), math.floor(0.5), int(0.5)
(1, 0, 0, 0)
>>> int(1.5 + 0.5), round(1.5), math.floor(1.5), int(1.5)
(2, 2, 1, 1)
>>> int(-0.5 + 0.5), round(-0.5), math.floor(-0.5), int(-0.5)
(0, 0, -1, 0)
>>> int(-1.5 + 0.5), round(-1.5), math.floor(-1.5), int(-1.5)
(-1, -2, -2, -1)
>>> int(4.49 + 0.5), round(4.49), math.floor(4.49), int(4.49)
(4, 4, 4, 4)
```

| $x$ | `int(x + 0.5)` | `round(x)` | `math.floor(x)` | `int(x)` |
|---|---|---|---|---|
| $0.5$ | 1 | 0 | 0 | 0 |
| $1.5$ | 2 | 2 | 1 | 1 |
| $-0.5$ | 0 | 0 | $-1$ | 0 |
| $-1.5$ | $-1$ | $-2$ | $-2$ | $-1$ |
| $4.49$ | 4 | 4 | 4 | 4 |

Only for $4.49$ do all four agree: the number is positive, not an exact half, and its fractional part is smaller than $0.5$. For halves, `round` goes to the even number ($0.5\to0$, $1.5\to2$, $-1.5\to-2$). The method by hand, `int` after adding 0.5, always rounds halves up, that is, toward the larger number, and therefore turns $-1.5$ into $-1$. `math.floor` rounds down, `int` toward zero; the two differ only for negative numbers.
:::
:::

:::aufgabe Exercise 40 ★★ A sound level calculator
<span class="anker" id="aufg-40"></span>

Write a script `pegel.py` that asks for two sound pressures in pascals, a quiet one and a loud one, and outputs by what factor the loud one is larger (with two decimal places) and by how many decibels (with one decimal place), $20\log_{10}(p_\mathrm{loud}/p_\mathrm{quiet})$ as in Exercise [30](module-math-und-sys.html#aufg-30). Test it with $0.02\,\mathrm{Pa}$ and $1.2\,\mathrm{Pa}$.

:::loesung
```python pegel.py
# Sound level calculator: two sound pressures as factor and in dB
import math

p_leise = float(input("Leiser Schalldruck in Pa: "))
p_laut = float(input("Lauter Schalldruck in Pa: "))

faktor = p_laut / p_leise
pegel_db = 20 * math.log10(faktor)    # difference in dB

print(f"Faktor: {faktor:.2f}")
print(f"Unterschied: {pegel_db:.1f} dB")
```

```console Windows (PowerShell)
PS> py pegel.py
Leiser Schalldruck in Pa: 0.02
Lauter Schalldruck in Pa: 1.2
Faktor: 60.00
Unterschied: 35.6 dB
```

On Linux, `python3 pegel.py` gives the same. The result fits Exercise [30](module-math-und-sys.html#aufg-30): factor 60, that is, $35.6\,\mathrm{dB}$.
:::
:::

:::aufgabe Exercise 41 ★ An error when reading input
<span class="anker" id="aufg-41"></span>

A script contains the lines `strecke = input("Strecke in km: ")` and `print("Doppelte Strecke:", strecke * 2)`. For the input 5, it outputs `55`. Explain this behavior and fix the error. What does your improved script output for the input `2.5`?

:::loesung
`input` always returns a `str` (subsection [10.3](#stufe-10-3)). `strecke * 2` therefore repeats the text `'5'` instead of calculating. The fix: convert the input with `float`.

```python einlesen.py
# Read in a distance and double it, with type conversion
strecke = float(input("Strecke in km: "))
print("Doppelte Strecke:", strecke * 2)
```

```console Linux
$ python3 einlesen.py
Strecke in km: 2.5
Doppelte Strecke: 5.0
```

With `int` instead of `float`, the input `2.5` would have failed with a `ValueError`; that is why `float` is the right choice for distances and other numbers with decimal places.
:::
:::

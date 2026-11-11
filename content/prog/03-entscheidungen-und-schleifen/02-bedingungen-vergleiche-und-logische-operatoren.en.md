---
title: Conditions: comparisons and logical operators
pfad: Computer Science / Programming / Python / Decisions and Loops
adresse: informatik/programmieren/python/entscheidungen-und-schleifen
knoten: Chapter 3: Decisions and Loops
order: 6040200
summary: A program that is supposed to decide needs a question to which the only answers are yes or no: Is the temperature in the desired range?
tags: chained comparison, short-circuit evaluation, truth value
lang: en
---

<span class="anker" id="stufe-1"></span>

:::zweck
A program that is supposed to decide needs a question to which the only answers are yes or no: Is the temperature in the desired range? Is the humidity below the limit? This section shows how to write such questions in Python, how to combine several of them and which values Python regards as yes and which as no.
:::

### Review: truth values and comparisons

<span class="anker" id="stufe-1-1"></span>

[Chapter 2](/wissen/en/informatik/programmieren/python/werte-typen-und-variablen/werte-typen-und-variablen.html) already provided the building blocks. The type `bool` has exactly two values, `True` and `False`. The six comparison operators return such a value:

| Operator | Meaning | Operator | Meaning |
|---|---|---|---|
| `==` | equal to | `!=` | not equal to |
| `<` | less than | `<=` | less than or equal to |
| `>` | greater than | `>=` | greater than or equal to |

Comparisons have a lower precedence than all arithmetic operators: in `temp + 2 > 23`, Python first calculates `temp + 2`. You do not test floating-point numbers for equality with `==` but with a tolerance, ready-made with `math.isclose`. Whether a name is bound to `None` is tested with `is`. In detail: [Chapter 2, Section 7](/wissen/en/informatik/programmieren/python/werte-typen-und-variablen/wahrheitswerte-und-vergleiche.html#stufe-7).

```console
>>> temp = 21.5
>>> temp > 20
True
>>> type(temp > 20)
<class 'bool'>
>>> 0.1 + 0.2 == 0.3
False
```

⁠**In short:** A comparison is an expression whose value is `True` or `False`.

### Chained comparisons

<span class="anker" id="stufe-1-2"></span>

A room should be between 20 °C and 23 °C. Whether a measured temperature $T$ lies in this range is written in mathematics as $20\,{}^\circ\mathrm C\le T\le23\,{}^\circ\mathrm C$.

**Two marks on the number line.** The chain $20\le T\le23$ contains two comparisons that must both hold: $T$ lies to the right of the lower mark and to the left of the upper one. Python allows exactly this notation.

:::definition Definition 1.1 (Chained comparison)
<span class="anker" id="satz-1-1"></span>

If several comparison operators stand one after another, such as `a < b <= c`, the expression is called a __chained comparison__. It yields `True` if and only if each of the individual comparisons `a < b` and `b <= c` yields `True`. Python evaluates the middle expression `b` only once, and if an earlier comparison already yields `False`, it does not evaluate the remaining ones.
:::

::::beispiel
A temperature in the range and one above it:

```console
>>> temp = 21.5
>>> 20 <= temp <= 23
True
>>> temp = 24.5
>>> 20 <= temp <= 23
False
>>> 1 < 3 > 2
True
```

The last line is allowed, because `1 < 3` and `3 > 2` are both true. But it reads poorly, because it does not describe a range. Chained comparisons are best used only in the form `untere <= wert <= obere`.
::::

⁠**In short:** `a <= x <= b` checks, as in mathematics, whether `x` lies between `a` and `b`.

:::hintergrund Why the same line is always true in C
In C, the language in which CPython itself is written, a comparison does not return a truth value of its own but the integer 1 for true and 0 for false. C evaluates several comparisons in a row from left to right, one after the other. There, `20 <= temp <= 23` becomes `(20 <= temp) <= 23`: first 0 or 1 results, and both are less than 23. So the condition is always satisfied, even for `temp = 100`. That is why the compiler gcc warns about such chains with the option `-Wall`. Python chose the meaning from mathematics because it is what you expect when reading.
:::

### Comparing strings

<span class="anker" id="stufe-1-3"></span>

Text has to be compared too, for example when a program checks whether someone has typed `ja` or is supposed to sort names alphabetically.

**As in a dictionary.** In a dictionary, “Regen” (German for “rain”) comes before “Sonne” (“sun”), because the first letter already decides. If the first letters are the same, the second one decides, and so on. A word that is the beginning of a longer one comes before it: “Sonne” before “Sonnenschein” (“sunshine”).

:::definition Definition 1.2 (Comparison of strings)
<span class="anker" id="satz-1-2"></span>

Two strings are equal (`==`) if they consist of the same characters in the same order; uppercase and lowercase letters are different characters. For `<` and the other order comparisons, Python goes through the two strings character by character from the left. At the first character in which they differ, the number of the character decides: the string with the smaller number is the smaller one. If one string is the beginning of the other, it is the smaller one.
:::

The number of a character is the number fixed worldwide from [Chapter 1, Section 6.1](/wissen/en/informatik/programmieren/python/programme-und-der-python-interpreter/fehler-lesen-und-verstehen.html#stufe-6-1), its code point, for example U+201E for the low quotation mark that opens a quotation in German. For the order, it is enough to know three ranges: the digits `0` to `9` have the numbers U+0030 to U+0039, the uppercase letters `A` to `Z` U+0041 to U+005A and the lowercase letters `a` to `z` U+0061 to U+007A. So digits come before uppercase letters, and uppercase letters before lowercase letters.

::::beispiel
Five comparisons of strings:

```console
>>> "Sonne" == "sonne"
False
>>> "Regen" < "Sonne"
True
>>> "Z" < "a"
True
>>> "Sonne" < "Sonnenschein"
True
>>> "10" < "9"
True
```

The last line deserves a second look. `"10"` and `"9"` are text, not numbers. Python compares the first character `1` (U+0031) with `9` (U+0039), and `1` has the smaller number. This becomes a trap when a program compares inputs, because `input` always returns a string ([Chapter 2, Section 10.3](/wissen/en/informatik/programmieren/python/werte-typen-und-variablen/zeichenketten-eingabe-und-ausgabe.html#stufe-10-3)). Only after the type conversion does Python compare numbers (`eingabe` is German for “input”):

```console
>>> eingabe = "10"
>>> eingabe < "9"
True
>>> float(eingabe) < 9
False
>>> eingabe == 10
False
>>> eingabe < 9
Traceback (most recent call last):
  File "<python-input-4>", line 1, in <module>
    eingabe < 9
TypeError: '<' not supported between instances of 'str' and 'int'
```

Equality between text and a number is simply false, because a text is never equal to a number. An order comparison between the two, on the other hand, is rejected by Python, because there is no meaningful answer.
::::

⁠**In short:** Python compares strings character by character by their numbers; `"10" < "9"` is true, so convert inputs first, then compare.

### The operator `not`

<span class="anker" id="stufe-1-4"></span>

Sometimes the opposite question is the interesting one: not “is the temperature in the range?” but “is it not in the range?”.

**The word “not”.** The sentence “It is not raining” is true if and only if the sentence “It is raining” is false. So the word “not” swaps true and false, and the operator `not` does the same with truth values.

:::definition Definition 1.3 (`not`)
<span class="anker" id="satz-1-3"></span>

`not` is a unary operator. `not x` yields `True` if `x` has the value `False`, and `False` if `x` has the value `True`.
:::

| `x` | `not x` |
|---|---|
| `False` | `True` |
| `True` | `False` |

`not` has a lower precedence than the comparisons: `not temp > 23` means `not (temp > 23)`.

::::beispiel
A temperature of 24.5 °C is not in the range:

```console
>>> temp = 24.5
>>> not 20 <= temp <= 23
True
>>> not True
False
```
::::

⁠**In short:** `not` negates a truth value.

### The operator `and`

<span class="anker" id="stufe-1-5"></span>

A room is pleasant only if two things hold at the same time: the temperature is in the range, and the humidity does not exceed the limit.

**Two locks on one door.** A door with two locks opens only if both are unlocked. If one of them is still locked, the door stays shut.

:::definition Definition 1.4 (`and`)
<span class="anker" id="satz-1-4"></span>

`and` is a binary operator. `a and b` yields `True` if and only if `a` and `b` are both `True`.
:::

| `a` | `b` | `a and b` |
|---|---|---|
| `False` | `False` | `False` |
| `False` | `True` | `False` |
| `True` | `False` | `False` |
| `True` | `True` | `True` |

A chained comparison is a shorthand for `and`: `a < b < c` has the same value as `a < b and b < c`, except that `b` is evaluated only once (Subsection [1.2](#stufe-1-2)).

::::beispiel
The temperature is right, but at 72 % the humidity is higher than the permitted 60 %:

```console
>>> temp = 21.5
>>> feuchte = 72
>>> 20 <= temp <= 23 and feuchte <= 60
False
```
::::

⁠**In short:** `a and b` is true only if both are true.

### The operator `or`

<span class="anker" id="stufe-1-6"></span>

A warning should appear if it is too cold in the room or if it is too warm; one of the two is enough.

**Two doors into a room.** You can get into a room with two doors as soon as at least one of the two is open.

:::definition Definition 1.5 (`or`)
<span class="anker" id="satz-1-5"></span>

`or` is a binary operator. `a or b` yields `True` if and only if at least one of the two operands is `True`.
:::

| `a` | `b` | `a or b` |
|---|---|---|
| `False` | `False` | `False` |
| `False` | `True` | `True` |
| `True` | `False` | `True` |
| `True` | `True` | `True` |

::::beispiel
The warning from the introduction, once with `or` and once as the negation of the range:

```console
>>> temp = 24.5
>>> temp < 20 or temp > 23
True
>>> not 20 <= temp <= 23
True
```

Both lines ask the same thing: a temperature lies outside the range if and only if it is below the lower limit or above the upper one.
::::

⁠**In short:** `a or b` is true as soon as one of the two is true.

### The precedence of the logical operators

<span class="anker" id="stufe-1-7"></span>

What does `a or b and c` mean: `(a or b) and c` or `a or (b and c)`? As with multiplication and division before addition and subtraction, a precedence determines what applies first.

:::definition Definition 1.6 (Precedence)
<span class="anker" id="satz-1-6"></span>

From tighter to looser binding: arithmetic operators, then comparisons, then `not`, then `and`, and finally `or`. So `and` binds more tightly than `or`, just as times binds more tightly than plus.
:::

::::beispiel
Without parentheses, Python first calculates `False and False`:

```console
>>> True or False and False
True
>>> (True or False) and False
False
```

If you build a condition from `and` and `or`, it is best to use parentheses, even where they are not needed. They cost nothing and save the reader from looking things up.
::::

⁠**In short:** `not` before `and` before `or`, all after the comparisons; when in doubt, use parentheses.

### Short-circuit evaluation

<span class="anker" id="stufe-1-8"></span>

Some conditions have a second half that only makes sense if the first one holds. In `n != 0 and 10 / n > 1`, the division may only take place if `n` is not zero.

**If you know the answer, you stop reading.** If A is already false in “A and B”, the whole is false, whatever B is. If A is already true in “A or B”, the whole is true. In both cases, you no longer need to look at B.

:::definition Definition 1.7 (Short-circuit evaluation)
<span class="anker" id="satz-1-7"></span>

Python evaluates `a and b` and `a or b` from the left and stops as soon as the result is certain. In `a and b`, `b` is evaluated only if `a` is true; in `a or b`, only if `a` is false. This rule is called __short-circuit evaluation__.
:::

::::beispiel
The expression `1 / 0` raises an exception as soon as Python evaluates it. It lets you see whether the right-hand side is evaluated:

```console
>>> False and 1 / 0
False
>>> True or 1 / 0
True
>>> True and 1 / 0
Traceback (most recent call last):
  File "<python-input-2>", line 1, in <module>
    True and 1 / 0
             ~~^~~
ZeroDivisionError: division by zero
```

In the first two lines, the result is certain after the left operand, and `1 / 0` is never calculated. Exactly this makes the condition from the beginning safe. The order of the two halves matters, though:

```console
>>> n = 0
>>> n != 0 and 10 / n > 1
False
>>> 10 / n > 1 and n != 0
Traceback (most recent call last):
  File "<python-input-2>", line 1, in <module>
    10 / n > 1 and n != 0
    ~~~^~~
ZeroDivisionError: division by zero
```

The check that makes a calculation possible in the first place must be on the left.
::::

⁠**In short:** `and` and `or` evaluate the right operand only if it can still change the result; the protecting condition therefore belongs on the left.

:::hintergrund Why `and` and `or` cannot be functions
In a function call such as `print(a, b)`, Python first calculates all the values in the parentheses and then passes them on. A function “and” would therefore always receive both values, including the one that raises an exception. That is why `and` and `or` are part of the language itself. When translating into bytecode ([Chapter 1, Section 2.4](/wissen/en/informatik/programmieren/python/programme-und-der-python-interpreter/vom-quelltext-zur-ausfuhrung-compiler-und-interpreter.html#stufe-2-4)), `a and b` becomes a jump: Python calculates `a`, checks its truth value and, if `a` is false, jumps past the instructions for `b`. The instructions for `b` are in the bytecode, but they are skipped.
:::

### The truth value of objects

<span class="anker" id="stufe-1-9"></span>

The operators `not`, `and` and `or` accept not only `True` and `False` but any value. So Python has to know whether, say, the number 0 or the string `""` counts as yes or as no. [Chapter 2](/wissen/en/informatik/programmieren/python/werte-typen-und-variablen/werte-typen-und-variablen.html) left this question open.

**Is there anything in it?** The rule follows a simple question: does the value contain anything? A zero and an empty string contain nothing and count as no; every other number and every text with at least one character count as yes.

:::definition Definition 1.8 (Truth value)
<span class="anker" id="satz-1-8"></span>

Every object has a __truth value__, `True` or `False`; the type conversion `bool(x)` shows it. Of the values known so far, exactly these have the truth value `False`: `False`, `None`, the zero of every number type (`0`, `0.0`, `-0.0`, `0j`) and the empty string `""`. All others have the truth value `True`. Where Python expects a condition, for example with `not`, it uses the truth value of the object.
:::

::::beispiel
`bool` shows the truth value of various values:

```console
>>> bool(0)
False
>>> bool(0.0)
False
>>> bool("")
False
>>> bool(None)
False
>>> bool("0")
True
>>> bool(" ")
True
>>> bool("False")
True
>>> bool(-1)
True
>>> bool(1e-300)
True
>>> bool(0.1 + 0.2 - 0.3)
True
>>> not ""
True
```

`"0"`, `" "` and `"False"` are strings with at least one character, so they are true; what the characters mean does not matter. `0.1 + 0.2 - 0.3` is not zero but about $5.55\cdot10^{-17}$, because every calculation is rounded ([Chapter 2, Section 5.1](/wissen/en/informatik/programmieren/python/werte-typen-und-variablen/rechnen-mit-gleitkommazahlen.html#stufe-5-1)), and it therefore counts as true.
::::

⁠**In short:** Of the values known so far, zero, `None`, `False` and the empty string count as false, and all others as true.

:::hintergrund Who decides what counts as false
The truth value is determined by the type of an object, just as the type also determines what `+` means ([Chapter 2, Section 1.2](/wissen/en/informatik/programmieren/python/werte-typen-und-variablen/objekte-und-typen.html#stufe-1-2)). For the number types, it is zero; for `str`, the empty string. The rule comes from older languages: in C, the number 0 counts as false in a condition, and every other number as true. Python carries this idea over from “zero” to “empty”. That way, you can ask whether a text contains anything without calculating its length.
:::

### What `and` and `or` return as a result

<span class="anker" id="stufe-1-10"></span>

A game asks for the player's name. If the input stays empty, a default name should apply. There is a short notation for this that uses a property of `and` and `or`.

:::definition Definition 1.9 (Result of `and` and `or`)
<span class="anker" id="satz-1-9"></span>

`a and b` yields `a` itself if `a` is false, and `b` otherwise. `a or b` yields `a` itself if `a` is true, and `b` otherwise. So the result is always one of the two operands, unchanged. `not x`, in contrast, always yields `True` or `False`.
:::

If both operands are of type `bool`, the result is exactly the tables from Subsections [1.5](#stufe-1-5) and [1.6](#stufe-1-6).

::::beispiel
With numbers and strings as operands:

```console
>>> 3 and 4
4
>>> 0 and 4
0
>>> 0 or "leer"
'leer'
>>> "" or "Standard"
'Standard'
>>> "Anna" or "Standard"
'Anna'
>>> None or 0
0
>>> not "Regen"
False
```

With `name = eingabe or "Standard"`, `name` gets the typed text if it is not empty, and `"Standard"` otherwise.
::::

**The trap with zero.** With numbers, the same notation is dangerous. The line `temp = messung or 20.0` is supposed to replace a missing measurement of the outdoor temperature with 20 °C. A genuine measurement of `0.0`, nothing unusual on a winter day, also has the truth value `False`, however, and is silently replaced by `20.0`. So whether a value is missing is tested with `messung is None` and not via its truth value.

⁠**In short:** `and` and `or` return one of their operands; `wert or ersatz` replaces every false value, even a genuine zero.

:::hintergrund Why `and` and `or` return an operand
Because of short-circuit evaluation, with `a and b` and `a or b`, there is in the end one operand that decided the result: if `a` is false in `and`, `a` decides; otherwise `b` decides, because the whole is true if and only if `b` is true. This deciding operand has the same truth value as the result. Python therefore returns it unchanged instead of converting it to `True` or `False`: used as a condition, it behaves exactly like the converted value, and it loses no information that you may still need, as with the default name. With `not`, there is no such operand, because no existing value stands for the opposite. That is why `not` has to create a new value, and that value is always a `bool`.
:::

### Exercises for Section [1](#stufe-1)

<span class="anker" id="stufe-1-11"></span>

:::aufgabe Exercise 1 ★ Predicting truth values
<span class="anker" id="aufg-1"></span>

For each expression, predict what interactive mode displays, then check on the computer: (a) `bool("0")`, (b) `bool("")`, (c) `0 or "x"`, (d) `3 and 4`, (e) `1 < 5 < 3`, (f) `"10" < "9"`, (g) `not 0.0`, (h) `None or 0`, (i) `"Regen" == "regen" or 2 > 1`.

:::loesung
```console
>>> bool("0")
True
>>> bool("")
False
>>> 0 or "x"
'x'
>>> 3 and 4
4
>>> 1 < 5 < 3
False
>>> "10" < "9"
True
>>> not 0.0
True
>>> None or 0
0
>>> "Regen" == "regen" or 2 > 1
True
```

(a) `"0"` is a string with one character, so it is true; what the character means does not matter. (b) The empty string is false. (c) `0` is false, so `or` returns the right operand. (d) `3` is true, so `and` returns the right operand. (e) `1 < 5` holds, `5 < 3` does not; a chained comparison is true only if all parts hold. (f) Text is compared character by character, and `1` has a smaller code point than `9`. (g) `0.0` is false, and `not` turns it into `True`. (h) `None` is false, so the result is the right operand `0`, although it is false, too. (i) The comparison on the left is `False` (uppercase and lowercase letters differ), the one on the right `True`; `or` returns it.
:::
:::

:::aufgabe Exercise 2 ★★ Conditions for an outing
<span class="anker" id="aufg-2"></span>

A bike tour takes place if the temperature is between 10 °C and 30 °C, the start time between 8:00 and 20:00 and the probability of rain at most 30 %.

<ol class="al">

<li>

Write an expression that, for the names `temp`, `uhr` and `regen`, yields `True` if and only if all three values fit.

</li>

<li>

Write an expression for “at least one value does not fit” without using `not`.

</li>

<li>

Check both for 22 °C, 14:00 and a 40 % probability of rain.

</li>

</ol>

:::loesung
(a) Two ranges and an upper limit, combined with `and`:

```python
10 <= temp <= 30 and 8 <= uhr <= 20 and regen <= 30
```

(b) “At least one value does not fit” means that one of the limits is exceeded. Without `not`, you write each violation separately and combine them with `or`:

```python
temp < 10 or temp > 30 or uhr < 8 or uhr > 20 or regen > 30
```

(c)

```console
>>> temp = 22
>>> uhr = 14
>>> regen = 40
>>> 10 <= temp <= 30 and 8 <= uhr <= 20 and regen <= 30
False
>>> temp < 10 or temp > 30 or uhr < 8 or uhr > 20 or regen > 30
True
```

The temperature and the start time fit, the probability of rain does not. That is why (a) is false and (b) is true. The two expressions always yield opposite values, because (b) describes exactly the opposite of (a).
:::
:::

:::aufgabe Exercise 3 ★★ De Morgan's laws
<span class="anker" id="aufg-3"></span>

In interactive mode, check for all four combinations of `a` and `b` from `True` and `False` that `not (a and b)` has the same value as `not a or not b`, and that `not (a or b)` has the same value as `not a and not b`. Explain the first law with the two locks on one door.

:::loesung
For each of the four combinations, both comparisons yield `True`; here are the first and the last:

```console
>>> a = False
>>> b = False
>>> (not (a and b)) == (not a or not b)
True
>>> (not (a or b)) == (not a and not b)
True
>>> a = True
>>> b = True
>>> (not (a and b)) == (not a or not b)
True
>>> (not (a or b)) == (not a and not b)
True
```

With `a = False, b = True` and `a = True, b = False`, the result is also `True` twice. The parentheses around `not (a and b)` are necessary because `==` binds more strongly than `not`.

With the two locks on one door: `a` and `b` mean “lock 1 is unlocked” and “lock 2 is unlocked”, and `a and b` means “the door opens”. `not (a and b)` means “the door stays shut”, and that is the case if and only if at least one of the locks is locked, that is, `not a or not b`. The second law is the same thing for the two doors into a room: you cannot get in if and only if both doors are shut.
:::
:::

:::aufgabe Exercise 4 ★★ Protection through order
<span class="anker" id="aufg-4"></span>

Which of the following expressions raise an exception for `n = 0`, and which do not? Give reasons, then check. (a) `n != 0 and 1 / n < 0.5`, (b) `1 / n < 0.5 and n != 0`, (c) `n == 0 or 1 / n < 0.5`, (d) `n == 0 and 1 / n < 0.5`. (e) After `import math` and `x = -1`: what does `x >= 0 and math.sqrt(x) < 3` yield?

:::loesung
(a) `n != 0` is false, so `and` does not evaluate the division: `False`, no exception. (b) The division is on the left and is evaluated first: `ZeroDivisionError`. (c) `n == 0` is true, so `or` does not evaluate the rest: `True`. (d) `n == 0` is true, and `and` therefore has to evaluate the right part: `ZeroDivisionError`. (e) `x >= 0` is false, and `math.sqrt(-1)` is never called: `False`.

```console
>>> n = 0
>>> n != 0 and 1 / n < 0.5
False
>>> n == 0 or 1 / n < 0.5
True
>>> n == 0 and 1 / n < 0.5
Traceback (most recent call last):
  File "<python-input-3>", line 1, in <module>
    n == 0 and 1 / n < 0.5
               ~~^~~
ZeroDivisionError: division by zero
>>> import math
>>> x = -1
>>> x >= 0 and math.sqrt(x) < 3
False
```

A condition can protect only if it is on the left and is built so that it already settles the result in the dangerous case: for `and` by “false”, for `or` by “true”.
:::
:::

:::aufgabe Exercise 5 ★★ Two traps with `or`
<span class="anker" id="aufg-5"></span>

<ol class="al">

<li>

`temp = messung or 20.0` is supposed to replace missing measurements. What does the line yield for `messung = 4.5`, for `messung = None` and for `messung = 0.0`? Which result is wrong, and why?

</li>

<li>

For `einheit = "kg"`, `einheit == "m" or "s"` does not yield `False`. What does it yield, and what is the expression that really asks whether `einheit` is equal to `"m"` or equal to `"s"`?

</li>

</ol>

:::loesung
(a)

```console
>>> messung = 4.5
>>> messung or 20.0
4.5
>>> messung = None
>>> messung or 20.0
20.0
>>> messung = 0.0
>>> messung or 20.0
20.0
```

The third result is wrong: 0 °C is a valid measurement, but `0.0` has the truth value `False`, and `or` replaces it. What was meant is “is the value missing?”, and that is what `messung is None` checks. With the tools from Section [2](entscheidungen-if-elif-und-else.html#stufe-2), you write:

```python
if messung is None:
    temp = 20.0
else:
    temp = messung
```

(b)

```console
>>> einheit = "kg"
>>> einheit == "m" or "s"
's'
>>> einheit == "m" or einheit == "s"
False
```

`==` binds more strongly than `or`. Python reads `(einheit == "m") or "s"`; the left part is `False`, so `or` returns the right operand `"s"`, and as a nonempty string, it is true. Each comparison has to be written out in full.
:::
:::

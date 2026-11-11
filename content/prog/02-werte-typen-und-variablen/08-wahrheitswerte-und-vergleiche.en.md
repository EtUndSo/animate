---
title: Truth values and comparisons
pfad: Computer Science / Programming / Python / Values, Types and Variables
adresse: informatik/programmieren/python/werte-typen-und-variablen
knoten: Chapter 2: Values, Types and Variables
order: 6030800
summary: Whether a temperature exceeds a limit and whether two results agree are questions with the answer yes or no.
tags: comparison operators, equal up to the relative tolerance
lang: en
---

<span class="anker" id="stufe-7"></span>

:::zweck
Whether a temperature exceeds a limit and whether two results agree are questions with the answer yes or no. This section introduces the type for such answers and shows how to compare numbers, why you should not test floating-point numbers for equality when doing so and what the value `None` means.
:::

### The type `bool`

<span class="anker" id="stufe-7-1"></span>

“Is it warmer than $30\,{}^\circ\mathrm C$ outside?” The answer is not a numerical value but yes or no. Python needs values that express exactly that.

**A switch with two positions.** Like a single bit, a truth value has only two states: true and false.

:::definition Definition 7.1 (The type `bool`)
<span class="anker" id="satz-7-1"></span>

The type `bool` has exactly two values, `True` and `False`. Both are keywords.
:::

The name recalls George Boole, who founded calculating with true and false in the 19th century. If you calculate with truth values, Python treats `True` like 1 and `False` like 0.

::::beispiel
The type of `True`, and calculating with truth values:

```console
>>> type(True)
<class 'bool'>
>>> True + True
2
>>> True * 10
10
```
::::

⁠**In short:** `bool` has the values `True` and `False`; in calculations, they count as 1 and 0.

### The comparison operators

<span class="anker" id="stufe-7-2"></span>

Where do truth values come from? Usually from a comparison of two values.

:::definition Definition 7.2 (Comparison operators)
<span class="anker" id="satz-7-2"></span>

The __comparison operators__ compare two values and return a `bool`:

|  |  |  |  |
|---|---|---|---|
| `==` | equal to | `!=` | not equal to |
| `<` | less than | `<=` | less than or equal to |
| `>` | greater than | `>=` | greater than or equal to |

They have a lower rank than all arithmetic operators: Python first calculates both sides and then compares.
:::

The double `==` compares; the single `=` binds a name. If you accidentally write `x == 5` where an assignment was meant, Python binds nothing: it only compares and, in interactive mode, displays `True` or `False`.

::::beispiel
Python compares numbers of different types by their value; a number and a string are never equal:

```console
>>> 7 > 5
True
>>> 2 + 3 == 5
True
>>> 3 != 3
False
>>> 1 == 1.0
True
>>> "2" == 2
False
>>> temperatur = 31.5
>>> temperatur > 30
True
```
::::

⁠**In short:** `==`, `!=`, `<`, `<=`, `>`, `>=` compare two values and return `True` or `False`.

### Do not test floating-point numbers for equality

<span class="anker" id="stufe-7-3"></span>

With the operator `==`, you can now check what Section [5](rechnen-mit-gleitkommazahlen.html#stufe-5) showed.

:::satz Theorem 7.3 (Equality of `float` values)
<span class="anker" id="satz-7-3"></span>

For `==`, two `float` values are equal if and only if they have the same value, that is, agree down to the last binary digit. Two ways of calculating that give the same result mathematically often return different `float` values because of rounding. And `nan` is not equal to any value, not even to itself.
:::

::::beispiel
Three comparisons after a calculation, then `nan`:

```console
>>> 0.1 + 0.2 == 0.3
False
>>> 0.1 * 3 == 0.3
False
>>> 0.1 * 10 == 1.0
True
>>> nan = 1e309 - 1e309
>>> nan == nan
False
>>> nan != nan
True
```

So whether `==` returns `True` or `False` for floating-point numbers depends on the luck of rounding. The third line happens to be true, the first two happen to be false. For results of calculations, `==` is therefore not a usable test.
::::

⁠**In short:** Never compare results of floating-point calculations with `==`.

### Comparison with a tolerance

<span class="anker" id="stufe-7-4"></span>

If `==` is no good, how do you check whether a result is right? You do not ask “equal?” but “close enough?”.

**As when weighing in the kitchen.** If a recipe calls for $500\,\mathrm g$ of flour, $510\,\mathrm g$ is no problem. If it calls for $5\,\mathrm g$ of salt, $10\,\mathrm g$ more, that is, $15\,\mathrm g$, would be far too much. What counts as “accurate enough” is a *proportion* of the value, say 2 %, not a fixed number of grams. Floating-point numbers are compared in just the same way.

:::definition Definition 7.4 (Comparison with a relative tolerance)
<span class="anker" id="satz-7-4"></span>

Two numbers $a$ and $b$ are __equal up to the relative tolerance__ $r$ if

$$|a-b|\le r\cdot\max(|a|,|b|) .$$
:::

The factor $\max(|a|,|b|)$ makes the comparison symmetric: it does not matter which of the two numbers you call $a$. A common choice is $r=10^{-9}$. This is far more than the rounding errors of a calculation of moderate size, which according to Theorem [5.3](rechnen-mit-gleitkommazahlen.html#satz-5-3) are about $10^{-16}$ per step, and it still demands nine matching digits.

**First by hand.** Python comes with the built-in function `abs` for the absolute value and the built-in function `max` for the largest of several values. With them, you can write down the definition directly:

```console
>>> abs(-3.5)
3.5
>>> max(2, 7.5, 3)
7.5
>>> a = 0.1 + 0.2
>>> b = 0.3
>>> abs(a - b) <= 1e-9 * max(abs(a), abs(b))
True
```

**The limit of the relative comparison.** If one of the two numbers is 0, the relative comparison fails: then $\max(|a|,|b|)=|a-b|$, and for $r<1$, the condition $|a-b|\le r\,|a-b|$ is satisfied only if both numbers are exactly 0. A result such as $10^{-20}$ is then never “close enough” to 0. For comparisons with 0, you additionally need an *absolute* tolerance $t_{\mathrm{abs}}$ that has the unit of the quantity:

$$|a-b|\le\max\bigl(r\cdot\max(|a|,|b|),\ t_{\mathrm{abs}}\bigr).$$

Which value of $t_{\mathrm{abs}}$ fits depends on the quantity and its unit: for amounts of money in euros, $10^{-9}$ is far less than a cent; for distances in light-years, $10^{-9}$ would already be almost $9500\,\mathrm{km}$, so there you need much less.

⁠**In short:** You compare floating-point numbers with a relative tolerance, $|a-b|\le r\max(|a|,|b|)$; near 0, you additionally need an absolute tolerance.

:::hintergrund The same test ends calculation recipes
Heron's recipe from [Chapter 1, Section 1.1](/wissen/en/informatik/programmieren/python/programme-und-der-python-interpreter/programme-und-programmiersprachen.html#stufe-1-1) improves an estimate $g$ of $\sqrt a$ with each pass: $g$ becomes $\frac12\bigl(g+\frac ag\bigr)$. A program that repeats such passes by itself has to decide when to stop. The usual rule: when the estimate no longer changes noticeably. Whether it still does, the program checks with exactly this kind of comparison between the old estimate $g_{\mathrm{old}}$ and the new one $g_{\mathrm{new}}$:

$$|g_{\mathrm{new}}-g_{\mathrm{old}}|\le\max\bigl(r\cdot\max(|g_{\mathrm{new}}|,|g_{\mathrm{old}}|),\ t_{\mathrm{abs}}\bigr).$$

You need the absolute tolerance for the same reason as above. For $a=0$, $\frac ag=0$, and each pass merely halves the estimate. The change is then always exactly half of the old value, and a purely relative comparison with $r<\frac12$ is never satisfied, even though the estimate is practically 0 very soon. Without an absolute tolerance, the recipe, starting from $g=1$, would run for 1075 passes until the estimate falls below the smallest positive `float` and becomes exactly 0; in the next pass, $\frac ag$ then fails with a division by zero. Some programs also add the two tolerances instead of taking the larger one; this changes the permitted deviation by at most a factor of 2.
:::

### The identity comparison

<span class="anker" id="stufe-7-5"></span>

The comparison operators ask about the value. Sometimes, however, you want to know whether two names are attached to the same object, that is, whether two tags are stuck to the same box.

:::definition Definition 7.5 (Identity comparison)
<span class="anker" id="satz-7-5"></span>

The operator `is` returns `True` if its two operands are the same object, that is, have the same identity. `is not` is its negation.
:::

::::beispiel
Two numbers with the same value, typed in separately, are two objects here:

```console
>>> x = 1000.5
>>> y = 1000.5
>>> x == y
True
>>> x is y
False
>>> z = x
>>> z is x
True
```

`x` and `y` have the same value but are attached to two different boxes. `z = x` attaches a second tag to the box of `x`.
::::

For numbers and strings, `is` is the wrong operator. Whether Python creates one object or two for two equal values is not specified and can change from version to version. You compare numbers with `==`, floating-point numbers with a tolerance.

⁠**In short:** `is` asks whether two names mean the same object; `==` asks whether two values are equal.

:::hintergrund Why `is` sometimes returns `True` for small numbers
At startup, CPython creates the integers from $-5$ to 256 as objects and reuses them again and again instead of creating a new object each time; small numbers occur constantly in almost every program. That is why, in interactive mode, after `x = 256` and `y = 256`, the comparison `x is y` is true, but not for 257. The limit is a property of CPython, not a rule of the language, and in newer development versions of CPython, the range is larger. Python even warns you if you use `is` directly with a number in the source code:

```console
>>> x = 257
>>> x is 257
<python-input-1>:1: SyntaxWarning: "is" with 'int' literal. Did you mean "=="?
  x is 257
False
```
:::

### The value `None`

<span class="anker" id="stufe-7-6"></span>

Some functions have no result that they could return. `print`, for example, writes something to the terminal, but what is the value of the call `print("Hallo")`? Python needs a value that means “no value”.

:::definition Definition 7.6 (`None`)
<span class="anker" id="satz-7-6"></span>

`None` is the only value of the type `NoneType`. It stands for “no value”. Functions without an actual result, such as `print`, return `None`.
:::

There is only one single object `None`. That is why you check whether a name is bound to `None` with `is`: `x is None`.

::::beispiel
The value of a `print` call:

```console
>>> ergebnis = print("Hallo")
Hallo
>>> ergebnis
>>> print(ergebnis)
None
>>> type(ergebnis)
<class 'NoneType'>
>>> ergebnis is None
True
```

The first line writes `Hallo` and binds `ergebnis` to the value of the call, that is, to `None`. The interactive mode does not display `None`; that is the reason why no second line appears after a `print` call ([Chapter 1, Section 4.8](/wissen/en/informatik/programmieren/python/programme-und-der-python-interpreter/der-interaktive-modus.html#stufe-4-8)). Only `print` makes `None` visible.
::::

⁠**In short:** `None` means “no value”; you test for it with `is None`.

### Exercises for Section [7](#stufe-7)

<span class="anker" id="stufe-7-7"></span>

:::aufgabe Exercise 25 ★ Predicting truth values
<span class="anker" id="aufg-25"></span>

Predict and check: (a) `3 == 3.0`, (b) `"3" == 3`, (c) `2 ** 10 > 1000`, (d) `7 // 2 == 3.5`, (e) `True + True + True`, (f) `0.5 + 0.25 == 0.75`, (g) `0.1 + 0.7 == 0.8`. Why is (f) true, although you should not test floating-point numbers for equality?

:::loesung
```console
>>> 3 == 3.0
True
>>> "3" == 3
False
>>> 2 ** 10 > 1000
True
>>> 7 // 2 == 3.5
False
>>> True + True + True
3
>>> 0.5 + 0.25 == 0.75
True
>>> 0.1 + 0.7 == 0.8
False
```

(a) Numbers are compared by their value. (b) A text is never equal to a number. (c) $1024>1000$. (d) $7\,/\!/\,2=3$. (e) `True` counts as 1. (f) $0.5$, $0.25$ and $0.75$ are finite binary fractions, all stored exactly, and their sum can be represented exactly, too: no rounding error arises. But that is luck with the chosen numbers; in general, you do not know whether all the values involved are exact. (g) `0.1 + 0.7` gives `0.7999999999999999`.
:::
:::

:::aufgabe Exercise 26 ★★ Is the bread acceptable?
<span class="anker" id="aufg-26"></span>

A bakery bakes loaves of bread with the target weight $750\,\mathrm g$ and permits a deviation of 5 %. Two loaves are weighed, at $718\,\mathrm g$ and $709\,\mathrm g$.

<ol class="al">

<li>

Check both weights with an expression that returns `True` or `False`. The 5 % refer to the target weight.

</li>

<li>

How does your expression differ from the definition in subsection [7.4](#stufe-7-4)? For which pair of measured weight and target weight do the two forms give different answers? Give an example.

</li>

</ol>

:::loesung
(a) The permitted deviation is $5\,\%$ of $750\,\mathrm g$, that is, $37.5\,\mathrm g$:

```console
>>> soll = 750
>>> abs(718 - soll) <= 0.05 * soll
True
>>> abs(709 - soll) <= 0.05 * soll
False
```

The loaf at $718\,\mathrm g$ deviates by $32\,\mathrm g$ and is acceptable; the one at $709\,\mathrm g$ deviates by $41\,\mathrm g$ and is not.

(b) Here, the 5 % refer to the target weight; in the definition, they refer to the larger of the two absolute values. If the measured weight is larger than the target weight, the permitted deviation in the definition is slightly larger. Example $789\,\mathrm g$: the deviation is $39\,\mathrm g$; relative to the target weight, only $37.5\,\mathrm g$ are permitted, but relative to $\max(789,750)$, it is $39.45\,\mathrm g$:

```console
>>> abs(789 - soll) <= 0.05 * soll
False
>>> abs(789 - soll) <= 0.05 * max(abs(789), abs(soll))
True
```

For rounding errors with $r=10^{-9}$, the difference does not matter; with a requirement like the bakery's, you have to stick to the specification that it refers to the target weight.
:::
:::

:::aufgabe Exercise 27 ★★ Comparisons near zero
<span class="anker" id="aufg-27"></span>

A program converts recipes and checks whether nothing is left of an ingredient. It calculates in kilograms, and the smallest ingredients weigh a few grams, that is, a few $10^{-3}\,\mathrm{kg}$. The result was `rest = 3e-19`.

<ol class="al">

<li>

What do `rest == 0` and the relative comparison with $r=10^{-9}$ return?

</li>

<li>

Choose a sensible absolute tolerance for amounts in kilograms when the smallest amounts weigh a few grams, and check with the formula with both tolerances.

</li>

</ol>

:::loesung
(a)

```console
>>> rest = 3e-19
>>> rest == 0
False
>>> abs(rest - 0) <= 1e-9 * max(abs(rest), abs(0))
False
```

Both say “not zero”. In the relative comparison, the right-hand side is $10^{-9}\cdot3\cdot10^{-19}$, and that is smaller than $3\cdot10^{-19}$: at zero, the relative comparison always fails.

(b) Amounts of a few grams, that is, a few $10^{-3}\,\mathrm{kg}$, carry rounding errors of about $10^{-3}\cdot10^{-16}=10^{-19}\,\mathrm{kg}$. An absolute tolerance of $10^{-12}\,\mathrm{kg}$, a billionth of a gram, lies far above that and far below any amount that matters in a kitchen:

```console
>>> abs(rest - 0) <= max(1e-9 * max(abs(rest), abs(0)), 1e-12)
True
```
:::
:::

:::aufgabe Exercise 28 ★ What does `print` return?
<span class="anker" id="aufg-28"></span>

Predict what the interactive mode displays for each line, and check:

```python
x = print(42)
x
print(x)
x is None
print(print("a"))
```

:::loesung
```console
>>> x = print(42)
42
>>> x
>>> print(x)
None
>>> x is None
True
>>> print(print("a"))
a
None
```

The first line writes 42 and binds `x` to `None`, the value of the call. `x` alone shows nothing, because the interactive mode does not display `None`. `print(x)` makes `None` visible. In the last line, Python first evaluates the inner `print("a")`: it writes `a` and returns `None`. The outer `print` then writes this `None`.
:::
:::

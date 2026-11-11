---
title: Interactive mode
pfad: Computer Science / Programming / Python / Programs and the Python Interpreter
adresse: informatik/programmieren/python/programme-und-der-python-interpreter
knoten: Chapter 1: Programs and the Python Interpreter
order: 6020500
summary: Python can be used like a calculator: you type in a line and immediately see the result.
tags: interactive mode, value, expression, evaluation, string, function, function call
lang: en
---

<span class="anker" id="stufe-4"></span>

:::zweck
Python can be used like a calculator: you type in a line and immediately see the result. This section shows this way of working and the first building blocks of Python: values, expressions, strings and calling a function.
:::

### Interactive mode

<span class="anker" id="stufe-4-1"></span>

To try out a single line, you do not want to create a file. Python offers a way of working of its own for this.

**A calculator.** On a calculator, you type a calculation, press “=” and read off the result. Then you type the next calculation. Python works exactly like this when you start it without a file name.

:::definition Definition 4.1 (Interactive mode)
<span class="anker" id="satz-4-1"></span>

In __interactive mode__, Python reads an input, runs it, displays the result and then waits for the next input.
:::

The prompt of the interactive mode is `>>>`. This cycle of reading, running and displaying is called the *read–eval–print loop*, REPL for short.

::::beispiel
In the terminal, start `py` (Windows) or `python3` (Linux) without anything after it. Python reports its version and waits for input:

```console Windows (PowerShell)
PS> py
Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 2 + 3
5
>>> 7 * 6
42
>>> exit
```

```console Linux
$ python3
Python 3.14.4 (main, Aug 20 2026, 10:41:58) [GCC 15.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 2 + 3
5
>>> 7 * 6
42
>>> exit
```

After each `>>>`, type a line and press Enter. Python answers on the next line and shows `>>>` again. A few useful moves:

<ul>

<li>

⁠**Exiting:** type `exit` (from Python 3.13 on; `exit()` with parentheses works in every version), or press Ctrl+D on Linux, Ctrl+Z and then Enter on Windows. After that, the prompt of the terminal appears again.

</li>

<li>

⁠**Earlier inputs:** The up arrow key brings back the last input; you can change it and send it again with Enter.

</li>

<li>

⁠**Incomplete input:** If something is still missing, such as a closing parenthesis, Python shows `...` instead of `>>>` and waits for the rest of the input.

</li>

</ul>

From Python 3.13 on, the interactive mode is in color; in this chapter, the sessions are printed without colors.
::::

⁠**In short:** In interactive mode, you type a line after `>>>`, and Python answers immediately.

:::hintergrund Where the interactive mode comes from
The name *read–eval–print loop* comes from the programming language Lisp. In the 1960s, Lisp systems already had exactly this cycle: read an input (*read*), compute it (*evaluate*), output the result (*print*), start over (*loop*). Many languages have adopted it because it lets you try out a language without writing a whole program.

Since Python 3.13, CPython has come with a revised interactive mode: the prompt and the error messages are in color, you can edit multi-line inputs as a whole, `exit` and `help` work without parentheses, and the keys F1, F2 and F3 open the help, the history and a mode for pasting longer texts. From Python 3.14 on, it also colors the typed lines according to their syntax. In older versions and in some environments, the simpler earlier version appears; what it computes is the same.
:::

### The value

<span class="anker" id="stufe-4-2"></span>

A calculator works with numbers. Python, too, needs a name for the data it works with.

:::definition Definition 4.2 (Value)
<span class="anker" id="satz-4-2"></span>

A __value__ is a single piece of data that Python works with, for example the number 42 or the number 0.5.
:::

In Python, numbers with decimal places are written with a point, not with a comma: `0.5`, not 0,5. In this chapter, numbers in running text also use a decimal point, just as in Python lines and in the answers from Python.

::::beispiel
If you type in a number, the interactive mode shows its value. It writes the value the way Python itself would write it and, for example, leaves out a superfluous zero at the end:

```console
>>> 42
42
>>> 0.5
0.5
>>> 2.50
2.5
```
::::

⁠**In short:** A value is a piece of data such as the number 42; in Python, decimal places come after a point.

### The expression

<span class="anker" id="stufe-4-3"></span>

Usually, you do not type in a finished value but a calculation whose value Python has yet to determine.

:::definition Definition 4.3 (Expression)
<span class="anker" id="satz-4-3"></span>

An __expression__ is a piece of source code that Python can compute to a value.
:::

Computing the value of an expression is called __evaluation__.

::::beispiel
`2 + 3` is an expression with the value 5. A single number such as `42` is also an expression, the simplest one of all: its value is the number itself. The interactive mode evaluates every expression you type in and displays the value on the next line. So the sessions above are nothing but pairs of expression and value.
::::

⁠**In short:** An expression is source code that yields a value; the interactive mode displays this value immediately.

### Calculating as on a calculator

<span class="anker" id="stufe-4-4"></span>

Python has its own symbols for the basic arithmetic operations and for powers.

| Symbol | Meaning | Example | Value |
|---|---|---|---|
| `+` | plus | `7 + 2` | `9` |
| `-` | minus | `7 - 2` | `5` |
| `*` | times | `7 * 2` | `14` |
| `/` | divided by | `7 / 2` | `3.5` |
| `**` | to the power of | `2 ** 10` | `1024` |

**Rules.**

<ul>

<li>

Python calculates as in mathematics: powers before multiplication and division, multiplication and division before addition and subtraction. `100 + 220 * 2` gives 540; if you want to add first, you use parentheses: `(100 + 220) * 2` gives 640.

</li>

<li>

Only round parentheses group a calculation. Square brackets and curly braces have other meanings in Python.

</li>

<li>

Spaces around the operators are allowed but not necessary; they make a line easier to read.

</li>

<li>

Python always writes the result of `/` with a point, even when the division comes out even: `12 / 4` gives `3.0`.

</li>

<li>

Powers of ten are written with `e`: `2.5e-3` means $2.5\cdot10^{-3}=0.0025$, that is, 2.5 g if the number is a weight in kilograms. Likewise, `4.7e3` is the number 4700.

</li>

<li>

Python displays results with decimal places with up to 17 significant digits. How many of them are meaningful is up to you when you read off the result.

</li>

<li>

Python knows no units. You have to keep track of the unit of a number in your head.

</li>

</ul>

::::beispiel three everyday calculations
First: A 450 g jar of chocolate spread costs €4.49. What does one kilogram cost? You divide the price by the weight in kilograms, that is, by 0.45.

Second: €1000 sits in a savings account for ten years at 2 % interest per year. The interest stays in the account and earns interest itself in the following year. So every year, the balance is multiplied by 1.02, and after ten years by $1.02^{10}$ in total.

Third: A sheet of printer paper is about 0.1 mm thick, that is $0.0001\,\mathrm m=10^{-4}\,\mathrm m$, in Python `1e-4`. How high is a pack of 500 sheets?

```console
>>> 4.49 / 0.45
9.977777777777778
>>> 1000 * 1.02 ** 10
1218.9944199947574
>>> 500 * 1e-4
0.05
```

In the second line, Python first computes the power `1.02 ** 10` and then multiplies it by 1000, powers before multiplication. Read off: the kilogram costs about €9.98, after ten years there is about €1219 in the account, and the pack is 0.05 m, that is, 5 cm high.
::::

**The last result.** The interactive mode remembers the last displayed value under the symbol `_` (underscore), like the ANS key of a calculator. After the session above, `_ * 100` therefore gives `5.0`, the height of the pack in centimeters. This works only in interactive mode.

**Careful with the comma.** If you are used to a decimal comma and type `2,5 * 2` instead of `2.5 * 2` out of habit, you get no error message but a wrong result:

```console
>>> 2,5 * 2
(2, 10)
```

Python reads the comma as a separator between two values: `2` and `5 * 2`. It displays both in parentheses instead of computing 5.0.

⁠**In short:** Python calculates with `+ - * / **` and round parentheses according to the rules of mathematics; decimal places come after a point, and it knows no units.

:::hintergrund Why the power is `**` and not `^`
For “to the power of”, no single symbol has become established in programming languages. Python follows the notation `**`, which the language Fortran already used in the 1950s. The symbol `^`, on the other hand, Python took over from the language C, where it means an operation on individual binary digits that has nothing to do with powers. That is why `2 ^ 3` gives 1 in Python and not 8, and it does so without an error message. If you are used to the symbol `^` from spreadsheets or calculators, watch out for this.
:::

### The recipe in interactive mode: first by hand, then ready-made

<span class="anker" id="stufe-4-5"></span>

With what has been explained so far, you can run Heron's recipe from Subsection [1.1](programme-und-programmiersprachen.html#stufe-1-1) in interactive mode: first by hand, pass by pass, then with the ready-made way that comes with Python.

**By hand.** The first pass with $g=1$ is `(1 + 2/1) / 2`. For every further pass, you need the last result as the new $g$; `_` stands for it. With the up arrow key, you bring back the line `(_ + 2/_) / 2` and send it again:

```console
>>> (1 + 2/1) / 2
1.5
>>> (_ + 2/_) / 2
1.4166666666666665
>>> (_ + 2/_) / 2
1.4142156862745097
>>> (_ + 2/_) / 2
1.4142135623746899
>>> (_ + 2/_) / 2
1.414213562373095
>>> (_ + 2/_) / 2
1.414213562373095
```

After the fifth pass, nothing changes anymore: the recipe has reached its goal.

**Ready-made.** The square root is the power with the exponent $\frac12$. Python can therefore compute it without a recipe:

```console
>>> 2 ** 0.5
1.4142135623730951
```

**Comparison.** Both ways agree in the first 15 decimal places:

| Way | Result |
|---|---|
| Heron by hand, from the 5th pass on | `1.414213562373095` |
| ready-made with `2 ** 0.5` | `1.4142135623730951` |
| true value $\sqrt2$ | $1.414\,213\,562\,373\,095\,048\,8\ldots$ |

The difference in the 16th decimal place has a simple cause: Python does not calculate with infinitely many digits but rounds every intermediate result to a fixed number of digits. Between two neighboring rounded numbers, there is therefore a smallest step. The recipe rounds several times in each pass and in the end stays one such step away from the built-in result. Here the ready-made way lies closer to the true value and needs no passes and no starting estimate; that is why you use it whenever it exists.

By hand, every pass had to be sent off individually. Taking exactly such repetitions off your hands is what a program is for.

⁠**In short:** Heron's recipe runs in interactive mode pass by pass and, after five passes, arrives at the built-in result of `2 ** 0.5` except for the last digit.

### Text as a value: the string

<span class="anker" id="stufe-4-6"></span>

Programs output not only numbers but also text, such as “Price in euros:” before a result. Text must therefore be able to be a value, too.

:::definition Definition 4.4 (String)
<span class="anker" id="satz-4-4"></span>

A __string__ is a value that consists of text. In source code, it stands between two straight quotation marks, `"Hallo"`, or between two apostrophes, `'Hallo'`.
:::

::::beispiel
Three inputs in interactive mode:

```console
>>> "Hallo"
'Hallo'
>>> "7 * 6"
'7 * 6'
>>> 7 * 6
42
```

The interactive mode displays a string with apostrophes, even if you typed it with quotation marks; both mean the same. The second line is more important: `"7 * 6"` is not computed. Between quotation marks, `7 * 6` is just a sequence of five characters.
::::

The quotation marks must be the straight ones from the keyboard. The typographic (curly) quotes from a word processor, “ and ” in English or „ and “ in German, are different characters for Python.

⁠**In short:** Text in straight quotation marks is a string, that is, a value that Python does not calculate with.

:::hintergrund Why the interactive mode writes the quotation marks too
The interactive mode displays every value the way you would write it in source code. That is why `'7 * 6'` appears there with apostrophes and `42` without: you can see at once whether the result is a number or a text. Without this marking, the number 42 and the text made of the characters “4” and “2” could not be told apart on the screen.
:::

### The function

<span class="anker" id="stufe-4-7"></span>

Many tasks occur in almost every program, for example writing something on the screen. For these, Python comes with ready-made subprograms.

**A key on the calculator.** The $\sqrt{\ }$ key of a calculator triggers a small built-in program. You do not need to know how it calculates; you put a number in and get the square root out.

:::definition Definition 4.5 (Function)
<span class="anker" id="satz-4-5"></span>

A __function__ is a ready-made subprogram with a name that you can have run when needed.
:::

::::beispiel
Python comes with the function named `print`. It writes values as text to the terminal.
::::

⁠**In short:** A function is a ready-made subprogram with a name.

### The function call: `print`

<span class="anker" id="stufe-4-8"></span>

A function does something only when you have it run. There is a fixed notation for this.

:::definition Definition 4.6 (Function call)
<span class="anker" id="satz-4-6"></span>

A __function call__ has a function run. You write its name, followed by round parentheses, and inside the parentheses the values that the function is to work with, separated by commas.
:::

::::beispiel
The function `print` writes the values in its parentheses on one line, separated by one space each. Strings appear without quotation marks. If there is an expression in the parentheses, Python evaluates it first and then outputs its value.

```console
>>> print("Hallo")
Hallo
>>> print(7 * 6)
42
>>> print("7 * 6")
7 * 6
>>> print("Preis pro kg in Euro:", 4.49 / 0.45)
Preis pro kg in Euro: 9.977777777777778
```

A call without values, `print()`, writes an empty line.
::::

In interactive mode, `"Hallo"` and `print("Hallo")` look similar but are different. In the first case, the interactive mode displays the value of an expression, with apostrophes. In the second case, the function `print` itself writes the text to the terminal, without apostrophes. Afterwards, the call of `print` has no value that the interactive mode would still display.

⁠**In short:** You call a function with its name and round parentheses; `print` writes the values in the parentheses to the terminal.

### Exercises for Section [4](#stufe-4)

<span class="anker" id="stufe-4-9"></span>

:::aufgabe Exercise 10 ★ Python as a calculator
<span class="anker" id="aufg-10"></span>

Calculate in interactive mode and give the results with a sensible number of digits and with a unit.

<ol class="al">

<li>

A car needs 45 liters of gasoline for 750 km. How many liters does it need for one kilometer?

</li>

<li>

A square room with a side length of 4.5 m is to be tiled. A tile of 60 cm by 60 cm covers $0.36\,\mathrm m^2$. What is the minimum number of tiles you need? Compute the area with `**`.

</li>

<li>

A hair on your head grows about 0.35 mm per day. How much does it grow in a year of 365 days? Calculate in meters and write the 0.35 mm with `e` for this.

</li>

<li>

Directly after (a), continue calculating with `_` and give the consumption in liters per 100 kilometers.

</li>

</ol>

:::loesung
```console
>>> 45 / 750
0.06
>>> _ * 100
6.0
>>> 4.5 ** 2 / 0.36
56.25
>>> 365 * 3.5e-4
0.12775
```

(a) Liters divided by kilometers: $45/750=0.06$ liters per kilometer.

(b) The area of the room is $4.5^2=20.25\,\mathrm m^2$, and $20.25/0.36=56.25$. Python computes the power first, so parentheses are not needed. You cannot buy partial tiles: you need at least 57 tiles, and the ones at the edge are cut to size.

(c) $0.35\,\mathrm{mm}=0.000\,35\,\mathrm m=3.5\cdot10^{-4}\,\mathrm m$, in Python `3.5e-4`. In one year, that makes $0.127\,75\,\mathrm m$, or just under 13 cm.

(d) Directly after (a), `_` holds the value `0.06`; `_ * 100` gives `6.0`, that is, 6 liters per 100 kilometers. If you calculate (b) or (c) first, `_` holds their result, because `_` always holds only the most recently displayed value.
:::
:::

:::aufgabe Exercise 11 ★★ The square root of 3 by hand and ready-made
<span class="anker" id="aufg-11"></span>

<ol class="al">

<li>

Run Heron's recipe for $\sqrt3$ in interactive mode: start with `(1 + 3/1) / 2` and repeat `(_ + 3/_) / 2` until the result no longer changes. How many passes do you need?

</li>

<li>

Compute $\sqrt3$ the ready-made way and compare.

</li>

<li>

For $\sqrt2$, the two ways differed in the last digit. What about here?

</li>

</ol>

:::loesung
```console
>>> (1 + 3/1) / 2
2.0
>>> (_ + 3/_) / 2
1.75
>>> (_ + 3/_) / 2
1.7321428571428572
>>> (_ + 3/_) / 2
1.7320508100147274
>>> (_ + 3/_) / 2
1.7320508075688772
>>> (_ + 3/_) / 2
1.7320508075688772
>>> 3 ** 0.5
1.7320508075688772
```

(a) After five passes, the result no longer changes; the sixth only confirms this.

(b) `3 ** 0.5` gives `1.7320508075688772`.

(c) This time, the two ways agree down to the last digit. Whether the recipe lands exactly on the built-in result or one smallest step next to it depends on how the individual roundings turn out; for $\sqrt2$ it stayed just off, for $\sqrt3$ it hits. In both cases, the ready-made way is the more reliable one.
:::
:::

:::aufgabe Exercise 12 ★★ What does the interactive mode show?
<span class="anker" id="aufg-12"></span>

For each input, write down what the interactive mode displays. Then check on the computer.

<ol class="al">

<li>

`12 / 3`

</li>

<li>

`"12 / 3"`

</li>

<li>

`print(12 / 3)`

</li>

<li>

`print("12 / 3 =", 12 / 3)`

</li>

<li>

`2,5 + 1`

</li>

<li>

`2 ** 3 * 2`

</li>

</ol>

:::loesung
```console
>>> 12 / 3
4.0
>>> "12 / 3"
'12 / 3'
>>> print(12 / 3)
4.0
>>> print("12 / 3 =", 12 / 3)
12 / 3 = 4.0
>>> 2,5 + 1
(2, 6)
>>> 2 ** 3 * 2
16
```

(a) The result of `/` is always written with a point, even when the division comes out even.

(b) Nothing is calculated between quotation marks; the interactive mode shows the string with apostrophes.

(c) `print` first evaluates the expression and then writes the value.

(d) `print` writes the string without quotation marks, then a space, and then the value.

(e) The comma separates two values, `2` and `5 + 1`. Python shows both in parentheses, without an error message.

(f) The power comes before multiplication and division: $2^3=8$, then $8\cdot2=16$.
:::
:::

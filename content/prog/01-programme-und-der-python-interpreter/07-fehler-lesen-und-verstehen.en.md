---
title: Reading and understanding errors
pfad: Computer Science / Programming / Python / Programs and the Python Interpreter
adresse: informatik/programmieren/python/programme-und-der-python-interpreter
knoten: Chapter 1: Programs and the Python Interpreter
order: 6020700
summary: Everyone who programs makes mistakes.
tags: syntax error, runtime error, exception, traceback, logic error
lang: en
---

<span class="anker" id="stufe-6"></span>

:::zweck
Everyone who programs makes mistakes. This section distinguishes three kinds of errors and shows when Python notices them and how to read its error messages.
:::

### The syntax error

<span class="anker" id="stufe-6-1"></span>

The first kind of error concerns the form of the source code.

**An illegible recipe.** A cook who comes across an illegible sentence while reading through a recipe does not even start cooking. First, they report which sentence cannot be read.

:::definition Definition 6.1 (Syntax error)
<span class="anker" id="satz-6-1"></span>

A __syntax error__ is a place in the source code that violates the syntax of the language. Python reports it before any line of the file is run.
:::

This follows from the two phases from Subsection [2.4](vom-quelltext-zur-ausfuhrung-compiler-und-interpreter.html#stufe-2-4): first the whole file is translated, and with a syntax error, no bytecode is produced that could run.

::::beispiel
The closing parenthesis is missing in the third line:

```python syntaxfehler.py
print("Zeile 1")
print("Zeile 2")
print("Zeile 3"
```

```console Linux
$ python3 syntaxfehler.py
  File "/home/student/python-kurs/syntaxfehler.py", line 3
    print("Zeile 3"
         ^
SyntaxError: '(' was never closed
```

```console Windows (PowerShell)
PS> py syntaxfehler.py
  File "C:\Users\student\python-kurs\syntaxfehler.py", line 3
    print("Zeile 3"
         ^
SyntaxError: '(' was never closed
```

Although the first two lines are free of errors, not even “Zeile 1” (German for “line 1”) appears. The message consists of four lines: the file and line number, the affected line, a `^` character below the place where Python pins down the error, and finally the error type `SyntaxError` with a description, here that the parenthesis was never closed.
::::

Further common syntax errors and their messages:

| Line | Message and cause |
|---|---|
| `print("Ende)` | `unterminated string literal`: The string is never closed. |
| `print("Hallo"))` | `unmatched ')'`: A parenthesis is closed that was never opened. |
| `print(„Hallo“)` | `invalid character '„' (U+201E)`: a typographic instead of a straight quotation mark. |
| a line that begins with spaces | `IndentationError: unexpected indent`: Spaces at the beginning of a line have a meaning in Python and must not stand there without a reason. |

In interactive mode, a syntax error affects only that one input; after that, `>>>` appears again.

⁠**In short:** A syntax error violates the form; Python reports it before the start, and no line of the file runs.

:::hintergrund Why typographic quotation marks are a syntax error
The syntax of Python allows only the straight quotation mark `"` and the apostrophe `'` as the beginning and end of a string. The curly quotes that a word processor inserts while you type, “ and ” in English or „ and “ in German, are completely different characters for Python. They are allowed inside a string; outside of one, they do not belong to any component of the language. Python therefore rejects a file with the line `print(„Hallo“)` as early as during translation:

```text
  File "/home/student/python-kurs/anfuehrungszeichen.py", line 1
    print(„Hallo“)
          ^
SyntaxError: invalid character '„' (U+201E)
```

The message names the forbidden character together with its number: every written character has a number that is fixed worldwide, and U+201E is the number of the low quotation mark that opens a quotation in German. On the screen, the characters „ and `"` look similar; the number tells them apart unambiguously.
:::

### The runtime error

<span class="anker" id="stufe-6-2"></span>

Source code can be completely correct in its form and still demand something that cannot be carried out.

**A missing ingredient.** The cook has read the recipe and begins. At step 2, they discover that the eggs are missing. By then, they have already done step 1; they get no further than step 2.

:::definition Definition 6.2 (Runtime error)
<span class="anker" id="satz-6-2"></span>

A __runtime error__ is an error that occurs only when a line is run. All lines before it have already run; the program aborts at this point.
:::

::::beispiel
Division by zero is allowed in its form but cannot be carried out:

```python laufzeitfehler.py
print("Zeile 1")
print(5 / 0)
print("Zeile 3")
```

```console Linux
$ python3 laufzeitfehler.py
Zeile 1
Traceback (most recent call last):
  File "/home/student/python-kurs/laufzeitfehler.py", line 2, in <module>
    print(5 / 0)
          ~~^~~
ZeroDivisionError: division by zero
```

```console Windows (PowerShell)
PS> py laufzeitfehler.py
Zeile 1
Traceback (most recent call last):
  File "C:\Users\student\python-kurs\laufzeitfehler.py", line 2, in <module>
    print(5 / 0)
          ~~^~~
ZeroDivisionError: division by zero
```

This time, “Zeile 1” appears: the file was translated without errors, and the first line has run. In the second line, the division fails, the program aborts, and “Zeile 3” never appears. Figure [4](#abb-4) contrasts the two cases.

:::abbildung prog/k1fehlerarten 4
Syntax error and runtime error. On the left, an error of form in line 3 prevents even the translation; no line runs. On the right, the translation succeeds, line 1 runs, and the error occurs only when line 2 is run.
:::
::::

⁠**In short:** A runtime error occurs when a line is run; everything before it has run, nothing after it has.

:::hintergrund Why a syntax error stops everything, but a runtime error only from its own line on
The reason is the two phases of CPython (Subsection [2.4](vom-quelltext-zur-ausfuhrung-compiler-und-interpreter.html#stufe-2-4)). In the first phase, the translator checks only the form, and it does so for the whole file. Without a valid form, no bytecode is produced, and the second phase does not even begin. Whether a line can actually be run only becomes apparent in the second phase, when the interpreter loop reaches it.

This is remarkable in the case of `5 / 0`. The translator does compute fixed numeric expressions such as `2 + 3` in advance (Subsection [2.4](vom-quelltext-zur-ausfuhrung-compiler-und-interpreter.html#stufe-2-4)), but not the division by zero: it deliberately leaves it in the bytecode. Its meaning is defined as “an error occurs when this line is run”. If the translator computed it in advance and failed in doing so, line 1 would not run either, and the program would behave differently from what the semantics prescribes.
:::

### The exception

<span class="anker" id="stufe-6-3"></span>

Python needs a uniform way to report an error and to stop the program at that point.

:::definition Definition 6.3 (Exception)
<span class="anker" id="satz-6-3"></span>

An __exception__ is the event with which Python reports an error. It has a type, for example `ZeroDivisionError`, and a description, for example `division by zero`. If it occurs while the program is running, it aborts the program at that point.
:::

So a runtime error raises an exception. Python also reports a syntax error as an exception, with the type `SyntaxError`, only already during translation.

::::beispiel
Three types of exceptions that occur in this chapter:

<ul>

<li>

`SyntaxError`: The source code violates the syntax.

</li>

<li>

`ZeroDivisionError`: A division by zero.

</li>

<li>

`NameError`: Python does not know a name. This typically happens when the quotation marks around a text are missing. Without quotation marks, Python takes a word to be a name, as `print` is one, and looks for something with that name:

</li>

</ul>

```python namefehler.py
print("Zeile 1")
print(Hallo)
```

```console Linux
$ python3 namefehler.py
Zeile 1
Traceback (most recent call last):
  File "/home/student/python-kurs/namefehler.py", line 2, in <module>
    print(Hallo)
          ^^^^^
NameError: name 'Hallo' is not defined
```

The description sometimes depends on the version. If you divide a number with decimal places by zero, Python 3.13 on Windows reports `ZeroDivisionError: float division by zero`, while Python 3.14 on Linux reports only `ZeroDivisionError: division by zero`. The type stays the same.
::::

⁠**In short:** An exception reports an error with a type and a description; while the program is running, it aborts the program.

### The traceback

<span class="anker" id="stufe-6-4"></span>

When an exception aborts a program, you want to know what happened, where and why. Python provides a report with a fixed structure for this.

:::definition Definition 6.4 (Traceback)
<span class="anker" id="satz-6-4"></span>

The __traceback__ is the report that Python outputs when an exception aborts a program while it is running. It names the place in the source code where the exception occurred and, in its last line, the type and the description of the exception.
:::

::::beispiel
Figure [5](#abb-5) breaks the traceback of `laufzeitfehler.py` down into its parts.

:::abbildung prog/k1traceback 5
A traceback broken down into its parts (Linux; on Windows, line 2 contains the Windows path). You read it from the bottom: first the exception (5), then the location (2 to 4).
:::
::::

You read a traceback *from the bottom*: the last line says what happened, the lines above it say where. In longer programs, there are further location lines above the error location, because the traceback traces the whole path to the error location; the lowest location line is always the place where the exception actually occurred.

The marker below the line has existed since Python 3.11. If the error concerns the whole line, Python leaves the marker out. In interactive mode, instead of a file name, there is `<python-input-0>`, counted from the first input; in the simpler earlier version of the interactive mode, it says `<stdin>`:

```console
>>> 5 / 0
Traceback (most recent call last):
  File "<python-input-0>", line 1, in <module>
    5 / 0
    ~~^~~
ZeroDivisionError: division by zero
>>>
```

After the traceback, the interactive mode simply waits for the next input.

⁠**In short:** A traceback names the location and the type of an exception; you read it from the bottom.

:::hintergrund Why the most important line is at the bottom
The header already says it: *most recent call last*, the most recent step comes last. A traceback is in chronological order. It begins where the program started and ends where it failed. In the programs in this chapter, this path is only one step long. Larger programs consist of parts that call each other; then the traceback lists every part on the way to the error location, and the list becomes long. For finding the error, however, the end of the path is almost always what matters first. That is why you read from the bottom.

A practical side effect: in the terminal, the output scrolls away upward, and the last lines remain visible. With a long traceback, the most important part is therefore exactly where your eye looks after the program has ended.
:::

### The logic error

<span class="anker" id="stufe-6-5"></span>

Python does not report the most dangerous kind of error at all.

**The wrong recipe.** A cook follows a recipe that says “salt” instead of “sugar”. Every step is readable and can be carried out; the cake even turns out fine, it just does not taste good.

:::definition Definition 6.5 (Logic error)
<span class="anker" id="satz-6-5"></span>

A __logic error__ is an error in which a program runs without an error message but does not compute what was intended.
:::

::::beispiel there and back
If you drive a route at 60 km/h there and at 40 km/h back, your average speed is not 50 km/h but lower: on the way back, you are on the road longer, so the slow speed counts for longer. If each direction is 120 km long, the way there takes 2 hours and the way back 3. For 240 km, you then need 5 hours, so on average $240/5=48$ km/h. In general, the average speed is $v=\frac{2v_1v_2}{v_1+v_2}$, where $v_1$ is the speed on the way there and $v_2$ the speed on the way back. Here this gives $\frac{2\cdot60\cdot40}{60+40}=48$. In the following script, the parentheses around the denominator are missing:

```python schnitt.py
# Average speed: there at 60 km/h, back at 40 km/h
# Formula: v = 2 * v1 * v2 / (v1 + v2)
print("Durchschnitt in km/h:", 2 * 60 * 40 / 60 + 40)
```

```console Linux
$ python3 schnitt.py
Durchschnitt in km/h: 120.0
```

Following its rules, Python calculates $2\cdot60\cdot40/60+40=80+40=120$ and is right to do so; something else was intended. The average must lie between the two speeds, that is, between 40 and 60 km/h; 120 km/h cannot be right. With `2 * 60 * 40 / (60 + 40)`, the result is `48.0`.
::::

Further typical logic errors from this chapter:

<ul>

<li>

a comma instead of a point: `2,5 * 2` gives two values instead of 5.0 (Subsection [4.4](der-interaktive-modus.html#stufe-4-4));

</li>

<li>

`^` instead of `**`: `2 ^ 3` gives 1 instead of 8;

</li>

<li>

a wrong unit: a price in euros is labeled “cents”.

</li>

</ul>

**What helps against it.** Check every result with a case whose answer you know, or with a rough estimate. For the average, two equal speeds are suitable: if you drive at 50 km/h there and back, your average speed is 50 km/h. The correct formula gives 50, the wrong one 150.

⁠**In short:** A logic error runs without a message and yields a wrong result; you find it only by checking results.

:::hintergrund Why no tool can find all logic errors
Python checks the form during translation and, while the program runs, whether each line can be run. What the author meant is written nowhere in the source code, so Python cannot check it either.

Behind this lies a fundamental limit. Computer science has proven that there can be no method that decides, for every arbitrary program, whether its behavior has a particular property that some programs have and others do not, such as “always outputs the correct average speed”. This is Rice's theorem from 1953. Tools can find many typical errors, but never all of them. Comparing results with known cases therefore remains indispensable.
:::

### Exercises for Section [6](#stufe-6)

<span class="anker" id="stufe-6-6"></span>

:::aufgabe Exercise 16 ★ Reading a traceback
<span class="anker" id="aufg-16"></span>

A script `strecke.py` produced the following output (in German, *Tempo* means speed, *Fahrzeit* travel time and *Strecke* distance):

```console Linux
$ python3 strecke.py
Tempo 18 km/h, Fahrzeit 2 h 30 min
Strecke in km: 45.0
Traceback (most recent call last):
  File "/home/student/python-kurs/strecke.py", line 4, in <module>
    print("Strecke in m:", Strecke * 1000)
                           ^^^^^^^
NameError: name 'Strecke' is not defined
```

<ol class="al">

<li>

What type of exception occurred, and in which line?

</li>

<li>

Which lines of the script have run? How can you tell?

</li>

<li>

What did the author probably mean, and what is the correct line if the distance is to be output in meters?

</li>

</ol>

:::loesung
(a) A `NameError` in line 4 (`line 4` in the location line, the type in the last line).

(b) Lines 1 to 3. Line 1 is a comment and does nothing; the output of lines 2 and 3 appears before the traceback. Line 4 is where the error occurred; it has output nothing, because Python wanted to evaluate the expression `Strecke * 1000` before calling `print`.

(c) The author probably meant the distance from line 3, 45 km. But the name `Strecke` does not occur anywhere; Python does not know it. The correct fix is to write out the expression itself, with 2.5 hours for 2 h 30 min: `print("Strecke in m:", 18 * 2.5 * 1000)`. Then `Strecke in m: 45000.0` appears.
:::
:::

:::aufgabe Exercise 17 ★★ Predicting errors
<span class="anker" id="aufg-17"></span>

For each of the three scripts, write down what it outputs, and assign the error to one of the three kinds. Then check on the computer.

```python fehler_a.py
print("Start")
print("Liter pro km:", 45 / 750)
print("Ende)
```

```python fehler_b.py
print("Start")
print("Liter pro km:", 45 / 0)
print("Ende")
```

```python fehler_c.py
print("Start")
print("Liter pro 100 km:", 45 / 750)
print("Ende")
```

For `fehler_b.py`, pay close attention to whether “Liter pro km:” still appears.

:::loesung
⁠**`fehler_a.py`** has a syntax error: in line 3, the string is never closed. Therefore no line runs; not even “Start” appears:

```console Linux
$ python3 fehler_a.py
  File "/home/student/python-kurs/fehler_a.py", line 3
    print("Ende)
          ^
SyntaxError: unterminated string literal (detected at line 3)
```

⁠**`fehler_b.py`** has a runtime error: line 1 runs, line 2 aborts. “Liter pro km:” does *not* appear, because Python first evaluates all values in the parentheses, including `45 / 0`, and only after that would `print` write anything. The marker points to the division:

```console Linux
$ python3 fehler_b.py
Start
Traceback (most recent call last):
  File "/home/student/python-kurs/fehler_b.py", line 2, in <module>
    print("Liter pro km:", 45 / 0)
                           ~~~^~~
ZeroDivisionError: division by zero
```

⁠**`fehler_c.py`** runs through without a message but contains a logic error: `45 / 750` is the consumption for one kilometer, but it is labeled as the consumption for 100 kilometers.

```console Linux
$ python3 fehler_c.py
Start
Liter pro 100 km: 0.06
Ende
```

The correct line would be `print("Liter pro 100 km:", 45 / 750 * 100)` with the output `6.0`, or the label “Liter pro km:”. On Windows, all three outputs are the same; only the location lines name the Windows path.
:::
:::

:::aufgabe Exercise 18 ★★ Finding a logic error
<span class="anker" id="aufg-18"></span>

Anna and Ben buy a lottery ticket together. Anna pays €1, Ben €2. The ticket wins €12, and the prize is divided in proportion to the stakes: Ben's share is the prize times Ben's stake divided by the sum of both stakes.

```python gewinn.py
# Prize 12 euros; stakes: Anna 1 euro, Ben 2 euros
# Ben's share = prize * Ben's stake / (Anna's stake + Ben's stake)
print("Bens Anteil in Euro:", 12 * 2 / 1 + 2)
```

<ol class="al">

<li>

The script outputs `Bens Anteil in Euro: 26.0`. How can you tell without calculating that this cannot be right?

</li>

<li>

Find the error and correct the line.

</li>

<li>

Check the corrected formula with a case whose result you know.

</li>

</ol>

:::loesung
(a) A share can never be larger than the whole prize, here €12. €26 for Ben is therefore impossible.

(b) The denominator lacks parentheses. Python computes $12\cdot2/1+2=24+2=26$. Correct:

```python
print("Bens Anteil in Euro:", 12 * 2 / (1 + 2))
```

Output: `Bens Anteil in Euro: 8.0`. Ben gets €8, Anna the remaining €4; that fits, because Ben paid in twice as much.

(c) With equal stakes, each must get exactly half: `12 * 1 / (1 + 1)` gives `6.0`. A second known case: if Ben pays much more than Anna, he gets almost the whole prize; if he pays nothing, he gets nothing.
:::
:::

:::aufgabe Exercise 19 ★★★ Observing the bytecode
<span class="anker" id="aufg-19"></span>

Python comes with a tool that displays the bytecode of a file without running it. You call it in the terminal with `py -m dis` or `python3 -m dis`, followed by the file name. For this, save this script:

```python rechnung.py
# This comment is only there for humans.
print(2 + 3)
print(5 / 0)
```

<ol class="al">

<li>

Have the bytecode displayed: `python3 -m dis rechnung.py` (Linux) or `py -m dis rechnung.py` (Windows). Each group of instructions begins with the number of the source code line it comes from. Can you find the comment again?

</li>

<li>

Look for the instructions for line 2. Is there still an addition, or already the number 5?

</li>

<li>

Look for the instructions for line 3. Has `5 / 0` been computed in advance? Use the Background box in Subsection [6.2](#stufe-6-2) to explain why.

</li>

<li>

Then run the script. What appears before the traceback comes?

</li>

</ol>

The names of the instructions depend on the Python version; the observations do not.

:::loesung
The output on the two test computers:

```console Windows (PowerShell), Python 3.13
PS> py -m dis rechnung.py
  0           RESUME                   0

  2           LOAD_NAME                0 (print)
              PUSH_NULL
              LOAD_CONST               0 (5)
              CALL                     1
              POP_TOP

  3           LOAD_NAME                0 (print)
              PUSH_NULL
              LOAD_CONST               0 (5)
              LOAD_CONST               1 (0)
              BINARY_OP               11 (/)
              CALL                     1
              POP_TOP
              RETURN_CONST             2 (None)
```

```console Linux, Python 3.14
$ python3 -m dis rechnung.py
  0           RESUME                   0

  2           LOAD_NAME                0 (print)
              PUSH_NULL
              LOAD_SMALL_INT           5
              CALL                     1
              POP_TOP

  3           LOAD_NAME                0 (print)
              PUSH_NULL
              LOAD_SMALL_INT           5
              LOAD_SMALL_INT           0
              BINARY_OP               11 (/)
              CALL                     1
              POP_TOP
              LOAD_CONST               1 (None)
              RETURN_VALUE
```

(a) There are no instructions for line 1; the comment disappeared during translation. The first group after the start instruction `RESUME` begins with the line number 2.

(b) In line 2, there is no addition. The translator has already computed `2 + 3`: Python 3.13 loads the finished number with `LOAD_CONST 0 (5)`, Python 3.14 with `LOAD_SMALL_INT 5`. After that comes the call of `print` (`CALL`).

(c) In line 3, 5 and 0 are loaded individually, followed by `BINARY_OP 11 (/)`: the division takes place only during execution. The translator computes in advance only what succeeds. If it computed `5 / 0` already during translation, the error would occur before line 2 runs. The semantics, however, require that the error occur exactly when line 3 is run, after everything before it has run.

(d) First, `5` from line 2 appears, then the traceback with `ZeroDivisionError` in line 3:

```console Linux
$ python3 rechnung.py
5
Traceback (most recent call last):
  File "/home/student/python-kurs/rechnung.py", line 3, in <module>
    print(5 / 0)
          ~~^~~
ZeroDivisionError: division by zero
```

The fact that the instruction names of the two versions differ (`LOAD_CONST` versus `LOAD_SMALL_INT`, `RETURN_CONST` versus `LOAD_CONST` and `RETURN_VALUE`) shows that the bytecode is an internal tool of CPython that may change with every version.
:::
:::

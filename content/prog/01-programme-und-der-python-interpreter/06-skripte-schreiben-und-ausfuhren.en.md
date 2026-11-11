---
title: Writing and running scripts
pfad: Computer Science / Programming / Python / Programs and the Python Interpreter
adresse: informatik/programmieren/python/programme-und-der-python-interpreter
knoten: Chapter 1: Programs and the Python Interpreter
order: 6020600
summary: Whatever you type in interactive mode is lost when you exit.
tags: editor, script, comment
lang: en
---

<span class="anker" id="stufe-5"></span>

:::zweck
Whatever you type in interactive mode is lost when you exit. This section shows how to save a program in a file, which tool you use to write this file and how to run it.
:::

### The editor

<span class="anker" id="stufe-5-1"></span>

Saving a program in a file requires a program with which you write and save plain text without anything being added.

**Plain text.** A program file may contain only the characters you type. A word processor such as Word, on the other hand, also saves fonts, page margins and paragraph formats, and while you type, it replaces straight quotation marks with typographic ones. Python, however, does not recognize typographic quotation marks as the beginning or end of a string. A word processor is therefore unsuitable for programs.

:::definition Definition 5.1 (Editor)
<span class="anker" id="satz-5-1"></span>

An __editor__ is a program with which you write and save plain text files. An editor for programmers also helps you write source code: it colors the code according to its syntax, marks violations of the syntax while you type and can run a program at the push of a button.
:::

::::beispiel two editors for this chapter
<ul>

<li>

⁠**Visual Studio Code** (VS Code for short) is a free editor for Windows and Linux, which you can get at `code.visualstudio.com`. On Ubuntu, you can alternatively install it with `sudo snap install --classic code`. After the first start, install the “Python” extension from Microsoft via the Extensions icon on the left edge. It provides the coloring, the error marking and the button for running a program; it does not contain Python itself.

</li>

<li>

⁠**IDLE** is a simple editor that is part of Python. On Windows, the Python install manager creates the entry “IDLE (Python 3.14)” in the Start menu, matching the installed version. On Ubuntu, you install it with `sudo apt install idle` and start it with the command `idle`. You begin a new program with “File”, “New File”.

</li>

</ul>

For the programs in this chapter, create a folder `python-kurs` in your home folder and save all files there. In VS Code, you open this folder with “File”, “Open Folder”; you then create new files in it.
::::

On Windows, File Explorer often hides file name extensions. Turn them on (“View”, “Show”, “File name extensions”) so that you can see whether a file is really called `hallo.py` and not `hallo.py.txt`.

⁠**In short:** You write programs with an editor that saves plain text, ideally with an editor for programmers such as VS Code or IDLE.

:::hintergrund How an editor for programmers knows the syntax
While you type, an editor for programmers constantly reads the source code along and splits it up the same way the translator of CPython does in its first phase (Subsection [2.4](vom-quelltext-zur-ausfuhrung-compiler-und-interpreter.html#stufe-2-4)): into numbers, operators, parentheses, strings and names. Each kind of component gets its own color; a string that is never closed therefore visibly colors the rest of the line as well. Then the editor checks the components against the grammar of the language and underlines every place where the grammar is violated. This check is the same kind of check that CPython performs before running a program; the editor merely does it earlier, namely while you are writing. What will happen when the program runs, on the other hand, it cannot fully foresee.
:::

### The script

<span class="anker" id="stufe-5-2"></span>

With an editor, you can write the source code of a program into a file and run it as often as you like.

:::definition Definition 5.2 (Script)
<span class="anker" id="satz-5-2"></span>

A __script__ is a text file with Python source code whose name ends in `.py`. Python runs a script by translating the file and then running each of its lines once, from top to bottom.
:::

**Preparing the folder.** Two commands are enough, and they are the same on Windows and Linux: `mkdir python-kurs` creates the folder `python-kurs`, and `cd python-kurs` changes into it in the terminal. A newly opened terminal is in your home folder; that is where the folder is created. If you have already created it in the editor, you can skip `mkdir`. In detail: Linux, Chapter 2.

::::beispiel
In the editor, write these three lines and save them as `hallo.py` in the folder `python-kurs`:

```python hallo.py
print("Hallo, Welt!")
print(2 + 3)
print("2 + 3")
```

In the terminal, you change into the folder and start the script by writing the file name after `py` or `python3`:

```console Windows (PowerShell)
PS> cd python-kurs
PS> py hallo.py
Hallo, Welt!
5
2 + 3
```

```console Linux
$ cd python-kurs
$ python3 hallo.py
Hallo, Welt!
5
2 + 3
```

Python translates the file, runs the three lines in order and ends; after that, the prompt of the terminal appears again. The second line outputs the value of `2 + 3`, the third outputs the string `"2 + 3"` literally. In VS Code, the button with the triangle at the top right (“Run Python File”) runs the same command in the terminal at the bottom of the window.
::::

**In a script, only `print` displays anything.** This script shows the most important difference from interactive mode:

```python ausdruck.py
print("Vorher")
2 + 3
print("Nachher")
```

```console Linux
$ python3 ausdruck.py
Vorher
Nachher
```

The line `2 + 3` is run, but its value appears nowhere. In interactive mode, the same line would have displayed `5`. In a script, only what a call of `print` outputs appears. Figure [3](#abb-3) shows both ways of working side by side. On Windows, the output looks exactly the same.

:::abbildung prog/k1modi 3
Two ways of working. Left, the interactive mode: it reads an input, evaluates it, displays the value and starts over. Right, a script: Python translates the whole file and then runs the lines one after another; only what `print` outputs becomes visible.
:::

⁠**In short:** A script is a `.py` file that you run with `py datei.py` or `python3 datei.py`; only what `print` outputs becomes visible in it.

:::hintergrund Why a script does not display the values of its lines
The rule is stated this way in the Python Language Reference: if a line is just an expression, its value is displayed in interactive mode; in a script, it is computed and discarded. Technically, the interactive mode translates each input in a separate mode of operation that appends an instruction “display value” at the end; when a script is translated, this instruction is missing. With `2 + 3`, the translator goes even further: it computes the line in advance, recognizes that its value is not needed anywhere and leaves it out of the bytecode entirely.

The reason for the rule is practical. A program should output exactly what its author wants. If a script with a hundred lines of calculation displayed every intermediate result, the actual result would get lost among them. When trying things out in interactive mode, on the other hand, you want to see every value immediately.
:::

### The comment

<span class="anker" id="stufe-5-3"></span>

A script is read more often than it is written, and after a few weeks, even you no longer know what `500 / 4 * 6` was supposed to mean. You need room for explanations that do not disturb Python.

:::definition Definition 5.3 (Comment)
<span class="anker" id="satz-5-3"></span>

A __comment__ begins with the character `#` and extends to the end of the line. Python skips it completely.
:::

::::beispiel converting a recipe
A recipe for pizza dough serves 4 people and needs 500 g of flour and 300 ml of water. For 6 people, you divide each amount by 4, which gives the amount for one person, and multiply it by 6:

```python rezept.py
# Pizza dough for 6 instead of 4 people
# Assumptions: the recipe for 4 people needs 500 g flour and 300 ml water.
# For one person, it is therefore one quarter of that.
print("Mehl in g:", 500 / 4 * 6)      # amount per person times 6
print("Wasser in ml:", 300 / 4 * 6)   # amount per person times 6
```

```console Linux
$ python3 rezept.py
Mehl in g: 750.0
Wasser in ml: 450.0
```

On Windows (`py rezept.py`), the same output appears. The first three lines are entirely comments. In the last two, the comment comes after the statement: Python runs the call of `print` and skips the rest of the line from `#` on.
::::

Good comments say what a number means and why something is calculated, not what is written there anyway. In the example, they state the assumptions and the units, because Python does not know those. With a `#` at the beginning of a line, you can also switch off a line temporarily without deleting it.

⁠**In short:** A comment begins with `#`, applies up to the end of the line and is there only for humans.

:::hintergrund Where the comment goes
During translation, CPython first splits the source code up into its smallest components: numbers, names, operators, parentheses, strings. A comment is thrown away in this very first step. It no longer appears in the bytecode, and therefore it costs no time when the program runs, however long it is.

A `#` inside a string does not start a comment, because there it belongs to the text: `print("Nr. # 5")` outputs `Nr. # 5`.
:::

### Exercises for Section [5](#stufe-5)

<span class="anker" id="stufe-5-4"></span>

:::aufgabe Exercise 13 ★ The first script
<span class="anker" id="aufg-13"></span>

Using an editor, write the script `hallo.py` from Subsection [5.2](#stufe-5-2) and add `7 * 6` as a fourth line.

<ol class="al">

<li>

Write down what the script will output before you start it.

</li>

<li>

Start it in the terminal and compare.

</li>

<li>

Change the fourth line so that its value appears as well.

</li>

</ol>

:::loesung
(a) and (b) The script outputs three lines; the fourth line, `7 * 6`, is computed, but its value does not appear, because in a script only `print` displays anything:

```console Linux
$ python3 hallo.py
Hallo, Welt!
5
2 + 3
```

On Windows (`py hallo.py`), the output is the same.

(c) The fourth line must read `print(7 * 6)`; then `42` appears as well.
:::
:::

:::aufgabe Exercise 14 ★★ The recipe for 10 people
<span class="anker" id="aufg-14"></span>

Following the model of `rezept.py`, write a script `rezept10.py` that converts the pizza dough for 10 people. Besides 500 g of flour and 300 ml of water, the recipe for 4 people contains 10 g of salt. The script should output all three amounts with their units. Comment the assumptions and the calculation. As a check, redo the calculation in your head.

:::loesung
```python rezept10.py
# Pizza dough for 10 instead of 4 people
# Assumptions: the recipe for 4 people needs 500 g flour, 300 ml water
# and 10 g salt. For one person, it is therefore one quarter of that.
print("Mehl in g:", 500 / 4 * 10)     # amount per person times 10
print("Wasser in ml:", 300 / 4 * 10)  # amount per person times 10
print("Salz in g:", 10 / 4 * 10)      # amount per person times 10
```

```console Linux
$ python3 rezept10.py
Mehl in g: 1250.0
Wasser in ml: 750.0
Salz in g: 25.0
```

Check in your head: for one person, it is 125 g of flour, 75 ml of water and 2.5 g of salt, so for ten people ten times as much. The 1250 g of flour are a little more than a standard 1-kg bag. On Windows, the output is the same.
:::
:::

:::aufgabe Exercise 15 ★★ From interactive mode to a script
<span class="anker" id="aufg-15"></span>

A liter of gasoline costs €1.80. For the car from Exercise [10](der-interaktive-modus.html#aufg-10), which needs 45 liters for 750 km, someone calculated in interactive mode:

```console
>>> 45 / 750
0.06
>>> _ * 100
6.0
>>> 45 * 1.8
81.0
```

Write a script `verbrauch.py` that outputs the same three results with explanatory text, such as `Liter pro km: 0.06`. Why can you not use `_` here? Replace it with an expression that does without `_`.

:::loesung
```python verbrauch.py
# A car needs 45 liters of gasoline for 750 km; a liter costs 1.80 euros.
print("Liter pro km:", 45 / 750)
print("Liter pro 100 km:", 45 / 750 * 100)
print("Kosten in Euro:", 45 * 1.8)          # 45 liters at 1.80 euros each
```

```console Linux
$ python3 verbrauch.py
Liter pro km: 0.06
Liter pro 100 km: 6.0
Kosten in Euro: 81.0
```

On Windows, the output is the same. Only the interactive mode keeps track of `_`; in a script there is no “most recently displayed result”, because a script does not display values at all. If you nevertheless write `print("Liter pro 100 km:", _ * 100)` in a script, it aborts with `NameError: name '_' is not defined`. That is why the second line contains the whole expression `45 / 750 * 100`.
:::
:::

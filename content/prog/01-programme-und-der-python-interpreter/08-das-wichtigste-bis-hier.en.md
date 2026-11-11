---
title: Key points so far
pfad: Computer Science / Programming / Python / Programs and the Python Interpreter
adresse: informatik/programmieren/python/programme-und-der-python-interpreter
knoten: Chapter 1: Programs and the Python Interpreter
order: 6020800
summary: What a program is, how Python runs it, computing interactively, writing scripts and reading error messages
tags: 
lang: en
---

:::kern Key points so far
<ul>

<li>

A program is a sequence of unambiguous steps (statements) that a computer carries out without asking back. The processor understands only machine instructions; people write source code in a programming language with a fixed syntax (form) and semantics (meaning).

</li>

<li>

A compiler translates the whole source code once, in advance, into an executable file; an interpreter runs the source code itself. CPython, the program `python`, translates the whole file into bytecode at every start and then runs this bytecode in its interpreter loop.

</li>

<li>

Windows: Python install manager, command `py`. Linux: preinstalled `python3`; leave the system Python alone. Version numbers such as 3.14.4 are compared part by part.

</li>

<li>

Interactive mode (`>>>`): every expression is evaluated and its value displayed. Operators `+ - * / **`, parentheses as in mathematics, a point, not a comma, for decimals, `e` for powers of ten, `_` for the last result.

</li>

<li>

Strings are written in straight quotation marks. A function call is a name plus round parentheses; `print` writes values to the terminal.

</li>

<li>

A script is a `.py` file, written with an editor and started with `py datei.py` or `python3 datei.py`; only what `print` outputs becomes visible. Comments begin with `#`.

</li>

<li>

Syntax error: before the start, no line runs. Runtime error: while running, an exception aborts the program, and everything before it has run. Logic error: no message, wrong result. You read a traceback from the bottom.

</li>

</ul>
:::

:::merke The answer in three sentences
<ol>

<li>

A program is a recipe of unambiguous steps that you write down as source code in a programming language, because the processor understands only machine instructions and everyday language is ambiguous.

</li>

<li>

You either type Python source code line by line in interactive mode, which displays every value immediately, or you save it as a script, which you start with `py` or `python3` and which outputs something only with `print`.

</li>

<li>

CPython first translates the whole file and then runs it; that is why a syntax error prevents any execution, a runtime error aborts only in its own line, and a logic error is noticed only if you check the result.

</li>

</ol>
:::

**One principle behind all the results.** Almost everything in this chapter follows from the fact that CPython works in two phases: first it translates the whole file, then it runs the bytecode. The form is checked before the start, whether a line can be run is checked while running, and the intention of the author is never checked.

| Result | Where it comes from |
|---|---|
| Python programs run on every computer with CPython | the bytecode is the same on all processors; only CPython itself is compiled (Section [2](vom-quelltext-zur-ausfuhrung-compiler-und-interpreter.html#stufe-2)) |
| fixed expressions such as `2 + 3` are already in the bytecode as 5 | the translator computes in advance in the first phase (Section [2](vom-quelltext-zur-ausfuhrung-compiler-und-interpreter.html#stufe-2)) |
| in a script, only `print` displays anything | the script is translated without the instruction “display value” (Section [5](skripte-schreiben-und-ausfuhren.html#stufe-5)) |
| comments cost nothing when the program runs | they are dropped as early as when the source code is split up (Section [5](skripte-schreiben-und-ausfuhren.html#stufe-5)) |
| a syntax error prevents any execution | without a valid form, no bytecode is produced (Section [6](fehler-lesen-und-verstehen.html#stufe-6)) |
| a runtime error aborts only in its own line | running happens only in the second phase, line by line (Section [6](fehler-lesen-und-verstehen.html#stufe-6)) |
| `5 / 0` is not computed in advance | the error must occur exactly when the line is run (Section [6](fehler-lesen-und-verstehen.html#stufe-6)) |
| nobody reports logic errors | Python checks form and whether lines can be run, not intention (Section [6](fehler-lesen-und-verstehen.html#stufe-6)) |

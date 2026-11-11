---
title: From source code to execution: compiler and interpreter
pfad: Computer Science / Programming / Python / Programs and the Python Interpreter
adresse: informatik/programmieren/python/programme-und-der-python-interpreter
knoten: Chapter 1: Programs and the Python Interpreter
order: 6020300
summary: The processor understands only machine code; people write source code.
tags: compiler, executable file, interpreter, Python, CPython, Bytecode, interpreter loop
lang: en
---

<span class="anker" id="stufe-2"></span>

:::zweck
The processor understands only machine code; people write source code. This section shows the two basic ways of closing this gap, and which way Python takes.
:::

### The compiler

<span class="anker" id="stufe-2-1"></span>

Source code has to be translated into machine code. A program can take on this job.

**A book translator.** A book is translated completely once, then printed and sold. The readers of the translation no longer need the translator; they hold a finished book in their hands.

:::definition Definition 2.1 (Compiler)
<span class="anker" id="satz-2-1"></span>

A __compiler__ is a program that translates a source code completely into machine code before that code is run. The result is saved as a separate file that runs without the compiler.
:::

Such a file is called an __executable file__. On Windows, its name usually ends in `.exe`.

::::beispiel
Programs in the C language are translated this way. From the source code `hallo.c`, the compiler `gcc` produces the executable file `hallo.exe` (Windows) or `hallo` (Linux). You then start this file directly, as often as you like and without the compiler. It contains machine code for a particular processor family and a particular operating system; for a different computer, you have to translate again.
::::

⁠**In short:** A compiler translates the whole source code once, in advance, into an executable file of machine code.

### The interpreter

<span class="anker" id="stufe-2-2"></span>

It also works without an executable file: a program can read the source code and itself do what it says.

**A human interpreter.** In a conversation between two languages, an interpreter sits in and translates while people are speaking. No written result is produced; at the next conversation, the interpreter has to be there again. (The picture captures the role of an interpreter program, not every detail of how it works.)

:::definition Definition 2.2 (Interpreter)
<span class="anker" id="satz-2-2"></span>

An __interpreter__ is a program that reads a source code and itself carries out the steps described in it. It produces no executable file and therefore has to be present every time the program is started.
:::

::::beispiel
Python programs run this way. You start the source code `hallo.py` with a command such as `python hallo.py`. The program `python` is the interpreter: it reads the file and carries out what it says. All the while, the processor runs the machine code of the interpreter, never the Python source code itself.
::::

The two ways compared:

|  | Compiler | Interpreter |
|---|---|---|
| translation happens | once, before any start | at every start |
| result | executable file | no file, only the effect |
| what you pass on | the executable file | the source code; the recipient needs the interpreter |
| runs on | the processor family and the operating system it was translated for | any computer for which the interpreter exists |
| speed | fast | slower, because the interpreter does work at every step |

⁠**In short:** An interpreter runs the source code itself, without producing an executable file.

:::hintergrund Why Python uses an interpreter
An interpreter has two advantages that are decisive for Python. You can type in a line and immediately see what it does, without a translation step in between. And the same source code runs unchanged on Windows, Linux and macOS, on the processor of a PC as well as on the completely different processor of a newer Mac; only the interpreter itself has to exist for each system.

The price is speed. At every step, the interpreter first has to do work of its own before the actual calculation happens. Computation-heavy programs are therefore often written so that the heavy parts run in ready-made, translated machine code that Python merely calls.
:::

### Python and CPython

<span class="anker" id="stufe-2-3"></span>

The word “Python” refers to two different things: a language and a program.

:::definition Definition 2.3 (Python and CPython)
<span class="anker" id="satz-2-3"></span>

__Python__ is a programming language; its syntax and semantics are laid down in the Python Language Reference. __CPython__ is the program that runs Python source code and is offered on `python.org`; it is itself written in the C language.
:::

CPython is the original and by far the most widely used program of this kind. New language features usually appear there first.

::::beispiel
There are other programs that run Python source code, for example PyPy, which runs many programs faster. They follow the same language reference, that is, the same syntax and semantics. In this series, the program `python` always means CPython.
::::

⁠**In short:** Python is the language; CPython is the program that runs it.

### Bytecode

<span class="anker" id="stufe-2-4"></span>

CPython is an interpreter, but it does not read the source code line by line like a human interpreter. It works in two phases.

**A cook with index cards.** A cook first reads through the whole recipe and writes each step on index cards in their own shorthand. If they come across an illegible sentence while doing so, they do not even start. Only when all the cards are finished do they work through them in order. (A picture; what the “cards” and the “shorthand” are in CPython follows now.)

:::definition Definition 2.4 (Bytecode)
<span class="anker" id="satz-2-4"></span>

__Bytecode__ is a sequence of simple instructions into which CPython translates the entire source code before it begins running it. The instructions are designed for an imaginary machine, not for a real processor.
:::

A part of CPython then works through the bytecode instruction by instruction: the __interpreter loop__.

So a Python program runs like this (Figure [2](#abb-2), left):

<ol>

<li>

⁠**Translate.** CPython reads the whole file, checks its syntax and generates bytecode from it. Nothing is run yet.

</li>

<li>

⁠**Run.** The interpreter loop takes one bytecode instruction after another. For each instruction, the processor runs a piece of machine code that is part of CPython and implements exactly this instruction.

</li>

</ol>

For a program that you start, CPython creates the bytecode only in main memory. No executable file is produced. The picture of the human interpreter from Subsection [2.2](#stufe-2-2) is therefore only half right: CPython first translates the whole file and then runs it.

:::abbildung prog/k1wege 2
Two ways from source code to execution. Left, Python: the program `python` (CPython) translates the whole file into bytecode at every start and then works through it in its interpreter loop. Right, C: the compiler translates once in advance into an executable file, which the processor then runs without the compiler.
:::

::::beispiel
The line `(1 + 2 / 1) / 2` gives rise to bytecode instructions such as “provide the number 1”, “divide”, “add”. The translator even goes one step further: an expression that consists only of fixed numbers is already computed during translation. The bytecode then contains the number 1.5 directly, and there is nothing left to compute when it runs. What the bytecode looks like exactly depends on the Python version; it is an internal tool of CPython and can change with every new version.
::::

One consequence of the two phases matters in practice: if any part of the file violates the syntax, no bytecode is produced at all. Then not a single line runs, not even the first.

⁠**In short:** CPython first translates the whole file into bytecode and then runs this bytecode instruction by instruction.

:::hintergrund Why CPython takes the detour via bytecode
Splitting up a text and checking its syntax takes a lot of work. If CPython read the text anew at every step, it would have to split up the same line a thousand times when it is run a thousand times. With bytecode, the splitting up happens once at the beginning. After that, the bytecode instructions are simple and uniform, and the interpreter loop can recognize and run each of them quickly.

In addition, the bytecode is the same on all processors. Only CPython itself has to be translated once with a compiler for each processor family and each operating system; after that, it runs the same bytecode everywhere. That is why Python is said to be interpreted, even though it contains a small translator. For Python, the line between “compiled” and “interpreted” is blurred.
:::

:::hintergrund The interpreter loop plays processor
At its core, the interpreter loop is a single loop in the C source code of CPython: fetch the next bytecode instruction, look up which instruction it is, run the matching piece of machine code, start over. This is the same cycle that the processor runs through with its machine instructions: fetch, decode, execute (Subsection [1.2](programme-und-programmiersprachen.html#stufe-1-2)). That is why one speaks of an imaginary or *virtual* machine: in software, CPython plays a processor whose instructions are the bytecode.
:::

### Exercises for Section [2](#stufe-2)

<span class="anker" id="stufe-2-5"></span>

:::aufgabe Exercise 4 ★ Compiler, interpreter or CPython?
<span class="anker" id="aufg-4"></span>

To which of the three kinds of programs does each statement apply: a compiler such as `gcc`, an interpreter that, like a human interpreter, translates line by line and runs each line immediately, or CPython? Several answers are possible.

<ol class="al">

<li>

A file is produced that runs without the translating program.

</li>

<li>

The program has to be present at every start.

</li>

<li>

The entire source code is translated before the first statement is run.

</li>

<li>

The processor runs the translation of the source code directly.

</li>

</ol>

:::loesung
(a) Only the compiler: it produces an executable file. CPython creates the bytecode only in main memory, and the line-by-line interpreter (the one that works like a human interpreter) produces no translation result at all.

(b) The line-by-line interpreter and CPython. Both run the program themselves and therefore have to be present at every start.

(c) The compiler and CPython. In its first phase, CPython translates the entire file into bytecode before the first line runs. Only the line-by-line interpreter translates each line only when it gets to it.

(d) Only the compiler: its executable file contains machine code that the processor runs directly. CPython's bytecode is run not by the processor but by the interpreter loop; meanwhile, the processor runs the machine code of CPython.
:::
:::

:::aufgabe Exercise 5 ★★ Passing programs on
<span class="anker" id="aufg-5"></span>

On Windows, you have written two small programs that do the same thing: `rechner.c` in C, from which you produced `rechner.exe` with the compiler, and `rechner.py` in Python. A friend uses Linux and has Python installed, but no C compiler.

<ol class="al">

<li>

Can she start `rechner.exe`? Explain.

</li>

<li>

Can she run `rechner.py`? What does she need for that?

</li>

<li>

What would she have to do to use the C program?

</li>

</ol>

:::loesung
(a) No. `rechner.exe` is an executable file for Windows. It has the Windows file format and uses services of Windows; a Linux system cannot start it directly, even if the processor belongs to the same family.

(b) Yes. She only needs a Python interpreter, which she has, in a version that knows all the language features used. She starts the program with `python3 rechner.py`. The source code is the same for all systems.

(c) She needs the source code `rechner.c` and a C compiler for Linux, for example `gcc`. With it, she translates the source code anew on her computer and starts the resulting executable file. The file `rechner.exe` does not help her with this.
:::
:::

:::aufgabe Exercise 6 ★★ When is the error noticed?
<span class="anker" id="aufg-6"></span>

A Python program has 1000 lines. Line 1000 is missing a closing parenthesis; all other lines are fine.

<ol class="al">

<li>

How many lines does CPython run before it reports the error? Justify your answer with the two phases.

</li>

<li>

How many lines would an interpreter run that really works like a human interpreter, that is, translates each line only when it gets to it?

</li>

<li>

Which behavior would you prefer if the program overwrites a file in line 500? Why?

</li>

</ol>

:::loesung
(a) Not a single one. In the first phase, CPython translates the entire file. The syntax error in line 1000 prevents bytecode from being produced, and without bytecode the second phase does not begin. The message appears before line 1 runs.

(b) 999 lines. Such an interpreter notices the error only when it gets to line 1000; it has already run everything before it.

(c) The behavior of CPython. With a line-by-line interpreter, the file would already have been overwritten in line 500 when the program aborts in line 1000: a half-finished state would be left behind. With CPython, a program with a syntax error does not even start running and therefore cannot leave anything half done. This does not protect against runtime errors, though: they occur only during execution.
:::
:::

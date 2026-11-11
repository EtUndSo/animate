---
title: Programs and programming languages
pfad: Computer Science / Programming / Python / Programs and the Python Interpreter
adresse: informatik/programmieren/python/programme-und-der-python-interpreter
knoten: Chapter 1: Programs and the Python Interpreter
order: 6020200
summary: A computer does only what it is told to do, step by step.
tags: program, statement, processor, machine instruction, machine code, programming language, syntax, semantics
lang: en
---

<span class="anker" id="stufe-1"></span>

:::zweck
A computer does only what it is told to do, step by step. This section explains what a program is, which instructions the processor of a computer understands, and why programs are written down in a language of their own.
:::

### The program

<span class="anker" id="stufe-1-1"></span>

A computer can calculate very fast, but it decides nothing on its own. Before it does anything useful, someone has to tell it exactly which steps to carry out and in which order.

**A recipe.** A cooking recipe is such a sequence of steps: “Bring water to a boil. Add the pasta. Wait nine minutes. Drain.” Whoever follows it does not need to know why pasta needs nine minutes. They only need to understand each step unambiguously and keep to the order.

**Knowing what something is, and knowing how to find it.** The sentence “The square root of 2 is the positive number that, multiplied by itself, gives 2” describes $\sqrt2$ completely. But it does not say how to find this number. A recipe that delivers the number step by step is knowledge of a different kind: it describes a method. A computer can only do something with knowledge of this second kind.

:::definition Definition 1.1 (Program)
<span class="anker" id="satz-1-1"></span>

A __program__ is a sequence of unambiguously described steps that a computer carries out one after another, without asking questions.
:::

A single step of a program is called a __statement__.

::::beispiel a recipe for the square root of 2
The following recipe is called Heron's method, after Heron of Alexandria, who described it in the first century. It needs only the basic arithmetic operations:

<ol>

<li>

Choose a first estimate $g$, for example $g=1$.

</li>

<li>

Compute $2/g$ and form the mean $\frac12\bigl(g+2/g\bigr)$. This mean is the new estimate $g$.

</li>

<li>

Repeat step 2 until $g$ no longer changes in the digits you are interested in.

</li>

</ol>

By hand with a calculator, you get:

| Pass | $g$ | $2/g$ | new estimate $\frac12\bigl(g+2/g\bigr)$ |
|---|---|---|---|
| 1 | $1$ | $2$ | $1.5$ |
| 2 | $1.5$ | $1.333\,333$ | $1.416\,667$ |
| 3 | $1.416\,667$ | $1.411\,765$ | $1.414\,216$ |
| 4 | $1.414\,216$ | $1.414\,211$ | $1.414\,214$ |

After three passes, $g=1.414\,216$ and $g^2=2.000\,006$; after four passes, the first six decimal places agree with $\sqrt2=1.414\,213\,56\ldots$. Figure [1](#abb-1) shows what happens: $g$ and $2/g$ always lie on different sides of $\sqrt2$, and their mean moves closer each time.

:::abbildung prog/k1heron 1
Heron's method for $\sqrt2$ on the number line. In each pass, the estimate $g$ (blue) and $2/g$ (orange) lie on different sides of $\sqrt2$, because their product is 2. Their mean (tick mark) becomes the new estimate. The distance between the two points shrinks from $1$ via $0.17$ to $0.005$; in the third pass, they almost coincide in this picture.
:::
::::

Whoever follows the recipe does not need to know why it works. Every step is so unambiguous that even a machine can carry it out. That is exactly what turns a recipe into a program.

⁠**In short:** A program is a recipe of unambiguous steps that a computer can carry out without asking back.

:::hintergrund Why the recipe works
If an estimate is too large, $g>\sqrt2$, then $2/g$ is too small, because the product $g\cdot(2/g)$ is always 2. The root therefore lies between $2/g$ and $g$, and the mean of the two is a reasonable next try.

A short calculation shows how fast this goes. For the new estimate $g'=\frac12(g+2/g)$,

$$g'^2-2=\frac{g^2+4+4/g^2}{4}-2=\frac{g^2-4+4/g^2}{4}=\frac{(g-2/g)^2}{4}=\frac{(g^2-2)^2}{4g^2}.$$

Two things follow from this:

<ul>

<li>

The right-hand side is never negative. From the first pass on, every estimate is therefore at least as large as $\sqrt2$, and $2/g$ lies below it.

</li>

<li>

The error $g^2-2$ is squared in every pass and additionally divided by $4g^2$, that is, from the second pass on by at least 8. Starting with $g=1$, $g^2-2$ is successively $0.25$, then $0.0069$, then $0.000\,006$, then $4.5\cdot10^{-12}$. The number of correct digits roughly doubles in each pass.

</li>

</ul>

If you know Newton's method from mathematics: Heron's method is Newton's method for the zero of $f(x)=x^2-2$. Its step $x-f(x)/f'(x)=x-\frac{x^2-2}{2x}$ is exactly $\frac12(x+2/x)$.
:::

### What the processor understands: machine instructions

<span class="anker" id="stufe-1-2"></span>

In a computer, the steps of a program are carried out by the __processor__, a chip that calculates and controls the sequence of steps. Its instructions are much simpler than “form the mean of $g$ and $2/g$”.

**A very literal worker.** You can picture the processor as an extremely fast worker with a tiny vocabulary. It understands instructions such as “fetch the number from memory cell 12”, “add two numbers”, “divide two numbers” or “continue at instruction 3”. It cannot do more than that, but it manages billions of these every second. (The picture is only an aid to imagination; the processor understands nothing in the human sense, but carries out its instructions mechanically.)

:::definition Definition 1.2 (Machine instruction)
<span class="anker" id="satz-1-2"></span>

A __machine instruction__ is an instruction that the processor can carry out directly. It is stored in memory as a number; from this number the processor recognizes what to do.
:::

A program that consists only of machine instructions is called __machine code__.

::::beispiel
Step 2 of Heron's recipe breaks down into machine instructions roughly like this:

<ol>

<li>

Fetch the number $g$ from memory.

</li>

<li>

Divide 2 by this number.

</li>

<li>

Add $g$ to the result.

</li>

<li>

Divide the result by 2.

</li>

<li>

Store the result in memory as the new $g$.

</li>

</ol>

Each of these instructions is a number in memory. Which number means which instruction is defined differently for each family of processors. The processors of most PCs understand different numbers than those of a smartphone. Machine code for one therefore does not run on the other.
::::

⁠**In short:** The processor understands only very simple machine instructions, which are stored as numbers in memory, and each processor family has its own.

:::hintergrund Why the processor knows only such simple instructions
Every machine instruction is permanently built into the processor chip. One part of the processor, the arithmetic unit, adds two numbers, for example. Another part, the control unit, reads the number of the next instruction and connects the matching parts with each other, such as “memory cell 12 to the input of the arithmetic unit, result back to memory”. The fewer and simpler the instructions, the smaller, faster and more economical the chip can be built. Everything complicated arises from many simple instructions running one after another, just as you can build a whole castle from a few kinds of Lego bricks.

The processor always runs through the same cycle: fetch the instruction, decode the instruction, execute the instruction, move on to the next instruction.
:::

### The programming language

<span class="anker" id="stufe-1-3"></span>

Machine code is a long sequence of numbers. People can hardly read it, and it applies to only one processor family. A recipe in everyday language would be more convenient, but everyday language is ambiguous.

**Ambiguity.** “I saw the man with the binoculars.” Did I have the binoculars, or did the man? A person guesses the intended meaning from the context. A computer cannot do that; it needs exactly one meaning for every sentence.

:::definition Definition 1.3 (Programming language)
<span class="anker" id="satz-1-3"></span>

A __programming language__ is an artificial language in which it is precisely defined which texts are allowed and what each allowed text does.
:::

::::beispiel
Python, C and C++ are programming languages. In Python, you write the first pass of Heron's recipe with $g=1$ like this:

```python
(1 + 2 / 1) / 2
```

The character `/` means “divided by”, `+` means “plus”, and the parentheses work as in mathematics. In Python, this line has exactly one meaning: divide 2 by 1, add 1, divide the result by 2.
::::

⁠**In short:** A programming language is an artificial language without ambiguity in which programs are written down.

### Syntax

<span class="anker" id="stufe-1-4"></span>

With a programming language, two questions have to be kept apart: Is a text allowed at all? And what does it do? The first question concerns only the form.

**Form without meaning.** The sentence “The wulp blinks the graffel.” is grammatically well built: subject, verb, object. It just means nothing. “Graffel the blinks wulp the.”, on the other hand, is wrong even in its form. Whether a sentence is well built can be checked without knowing its meaning.

:::definition Definition 1.4 (Syntax)
<span class="anker" id="satz-1-4"></span>

The __syntax__ of a programming language is the set of all rules that determine which texts are allowed in it.
:::

::::beispiel
In Python, `(1 + 2 / 1) / 2` is allowed. The following lines violate the syntax:

<ul>

<li>

`(1 + 2 / 1 / 2`: A parenthesis is opened and never closed.

</li>

<li>

`1 + / 2`: A number is missing between `+` and `/`.

</li>

</ul>
::::

⁠**In short:** The syntax determines the allowed form, regardless of what a text means.

### Semantics

<span class="anker" id="stufe-1-5"></span>

A text in an allowed form must also have a defined effect.

:::definition Definition 1.5 (Semantics)
<span class="anker" id="satz-1-5"></span>

The __semantics__ of a programming language determines what an allowed text means, that is, what happens when it is run.
:::

::::beispiel
The line `7 / 2` is allowed in Python and in C, so it has the correct form in both languages. In Python it means “divide 7 by 2”, and the result is 3.5. In C, with whole numbers, the same text means “divide and drop the remainder”, and the result is 3. Same form, different meaning.

A second example: if you want to compute the mean of 3 and 4 and write `3 + 4 / 2`, you have written an allowed text. But its defined meaning is $3+\frac42=5$, not the intended mean $3.5$. The semantics follows the text, not the intention.
::::

⁠**In short:** The semantics determines what an allowed text does.

:::hintergrund How Python knows which texts are allowed
The syntax of Python is written down as a formal grammar: a list of rules such as “an expression in parentheses is an opening parenthesis, then an expression, then a closing parenthesis”. It is given in full in the Python Language Reference. The program that runs Python texts contains a part that is generated from exactly this grammar and checks every text against its rules. The semantics, by contrast, is described in words: for every allowed form, the language reference says what it does.
:::

### Source code

<span class="anker" id="stufe-1-6"></span>

What a person writes down in a programming language needs a name to distinguish it from machine code.

:::definition Definition 1.6 (Source code)
<span class="anker" id="satz-1-6"></span>

The __source code__ of a program is its text in a programming language, the way people write and read it.
:::

::::beispiel
The line `(1 + 2 / 1) / 2` is a very short piece of Python source code. A processor cannot run it, because it understands only machine instructions. So something has to translate between the source code and the processor.
::::

⁠**In short:** Source code is the program in the form in which people write it; the processor cannot run it directly.

### Exercises for Section [1](#stufe-1)

<span class="anker" id="stufe-1-7"></span>

:::aufgabe Exercise 1 ★ The recipe by hand
<span class="anker" id="aufg-1"></span>

Use Heron's recipe and a calculator to compute the square root of 10. To do so, replace the number 2 in the recipe by 10, that is, $g'=\frac12(g+10/g)$.

<ol class="al">

<li>

Start with $g=3$ and carry out three passes. Write down $g$ each time with six decimal places.

</li>

<li>

Compute $g^2$ after each pass. How close is it to 10?

</li>

<li>

In each pass, compare $g$ and $10/g$. Which of the two numbers is larger?

</li>

</ol>

:::loesung
Here the recipe reads $g'=\frac12(g+10/g)$; the true value is $\sqrt{10}=3.162\,277\,66\ldots$

| Pass | $g$ before | $10/g$ | $g$ after | $g^2$ after |
|---|---|---|---|---|
| 1 | $3$ | $3.333\,333$ | $3.166\,667$ | $10.027\,778$ |
| 2 | $3.166\,667$ | $3.157\,895$ | $3.162\,281$ | $10.000\,019$ |
| 3 | $3.162\,281$ | $3.162\,275$ | $3.162\,278$ | $10.000\,000$ |

(a) After three passes, $g=3.162\,278$; all six decimal places agree with $\sqrt{10}$.

(b) After the first pass, $g^2$ lies $0.028$ above 10, after the second $0.000\,019$, after the third less than $10^{-11}$. The gap shrinks drastically each time because, according to the Background box in Subsection [1.1](#stufe-1-1), it is squared and divided: $0.028^2/(4\cdot10.03)\approx0.000\,019$.

(c) Before the first pass, $g=3$ is smaller than $10/g=3.333$: the starting estimate is too small. From then on, $g$ is always the larger number ($3.166\,667>3.157\,895$ and $3.162\,281>3.162\,275$). The reason: the product $g\cdot(10/g)$ is always 10, so $\sqrt{10}$ always lies between the two numbers; and after one pass, $g$ is never too small again, as the Background box in Subsection [1.1](#stufe-1-1) shows.
:::
:::

:::aufgabe Exercise 2 ★ Form or meaning?
<span class="anker" id="aufg-2"></span>

For each case, decide whether the syntax is violated, whether an allowed text means something other than intended, or whether the text is ambiguous.

<ol class="al">

<li>

In Python: `(3 + 4 / 2`.

</li>

<li>

In Python, the mean of 3 and 4 is to be computed: `3 + 4 / 2`.

</li>

<li>

In Python: `3 + * 4`.

</li>

<li>

A request: “Photograph the woman with the camera.”

</li>

<li>

A program in C contains `7 / 2` and is supposed to give 3.5.

</li>

</ol>

:::loesung
(a) Syntax violated: the opened parenthesis is never closed.

(b) An allowed text that means something other than intended. Python does multiplication and division before addition and subtraction, so $3+4/2=3+2=5$. What was meant is `(3 + 4) / 2`, with the value 3.5.

(c) Syntax violated: after `+`, a number is missing before `*` follows.

(d) Ambiguous: is the woman holding a camera in her hand, or are you supposed to use the camera? A human asks back or decides from the context; in a programming language, there must be no such spot.

(e) An allowed text that means something other than intended. Under the semantics of C, `7 / 2` with whole numbers gives 3, not 3.5. If you want 3.5 in C, you have to write at least one of the numbers with a decimal place, for instance `7.0 / 2`.
:::
:::

:::aufgabe Exercise 3 ★★ A recipe in machine instructions
<span class="anker" id="aufg-3"></span>

The mean of three numbers $a$, $b$ and $c$ that are stored in memory is to be computed and stored in memory. Break the calculation down into instructions of the kind “fetch a number from memory”, “add”, “divide by a number” and “store in memory”, as in the example in Subsection [1.2](#stufe-1-2). How many instructions do you need? Fetch each number only once.

:::loesung
One possible sequence:

<ol>

<li>

Fetch $a$ from memory.

</li>

<li>

Fetch $b$ from memory.

</li>

<li>

Add the two numbers; result $a+b$.

</li>

<li>

Fetch $c$ from memory.

</li>

<li>

Add $c$; result $a+b+c$.

</li>

<li>

Divide the result by 3.

</li>

<li>

Store the result in memory.

</li>

</ol>

These are seven instructions: three for fetching, two additions, one division, one store. A single line of source code such as `(a + b + c) / 3` therefore becomes several machine instructions. Exactly how many depends on the processor family; some processors, for example, can fetch a number from memory and add it in the same instruction.
:::
:::

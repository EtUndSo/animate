---
title: Objects and types
pfad: Computer Science / Programming / Python / Values, Types and Variables
adresse: informatik/programmieren/python/werte-typen-und-variablen
knoten: Chapter 2: Values, Types and Variables
order: 6030200
summary: Everything Python calculates with lies in main memory as an object.
tags: object, type, identity, method
lang: en
---

<span class="anker" id="stufe-1"></span>

:::zweck
Everything Python calculates with lies in main memory as an object. This section clarifies what an object is, how Python recognizes what you are allowed to do with an object and how you tell two objects apart.
:::

### The object

<span class="anker" id="stufe-1-1"></span>

[Chapter 1](/wissen/en/informatik/programmieren/python/programme-und-der-python-interpreter/programme-und-der-python-interpreter.html) called numbers such as 42 and texts such as `"Hallo"` values ([Chapter 1, Section 4.2](/wissen/en/informatik/programmieren/python/programme-und-der-python-interpreter/der-interaktive-modus.html#stufe-4-2)). While Python works with a value, this value has to be stored somewhere. And Python has to know what kind of value it is: you can calculate with the number 42, but not with the text made of the characters 4 and 2.

**A labeled box.** You can picture main memory as a long row of compartments. Python puts each value into a box of its own. On the box, it writes what kind of value lies inside, and each box stands at a fixed place with a place number (Fig. [1](#abb-1)). This is a picture for orientation: how memory is built technically does not matter for what follows.

:::abbildung prog/k2objekt 1
Three objects in main memory, drawn as boxes. Each box carries a label saying what kind of value it contains, and it stands at a fixed place. On the screen, the first and the third number look the same; for Python, they are different things. The place numbers are made up.
:::

:::definition Definition 1.1 (Object)
<span class="anker" id="satz-1-1"></span>

An __object__ is a piece of main memory in which Python stores a value, together with the information about what kind of value is stored there.
:::

Every value Python works with is contained in an object: every number, every string, even every intermediate result of a calculation.

::::beispiel
If you type `42`, `4.0` and `"42"` one after the other in interactive mode, Python calculates with three objects as in Fig. [1](#abb-1):

```console
>>> 42
42
>>> 4.0
4.0
>>> "42"
'42'
```

The first contains the integer 42, the second a number with decimal places, the third the text made of the characters 4 and 2. The interactive mode already shows the kind in the notation: without a point, with a point, with apostrophes.
::::

⁠**In short:** An object is a value in main memory that carries the information about its kind with it.

### The type

<span class="anker" id="stufe-1-2"></span>

Before Python combines two values, it has to know what is allowed with them. The plus sign means something different for two numbers than for two texts, and for a number and a text it means nothing at all.

**The label on the box.** In Fig. [1](#abb-1), each box says what kind of value it contains. In Python, this label has a name of its own.

:::definition Definition 1.2 (Type)
<span class="anker" id="satz-1-2"></span>

The __type__ of an object is the kind of its value. It determines which values the object can have and what you can do with it. The function `type` returns the type of an object.
:::

::::beispiel
The three objects from Fig. [1](#abb-1) have three different types:

```console
>>> type(42)
<class 'int'>
>>> type(4.0)
<class 'float'>
>>> type("42")
<class 'str'>
```

`<class 'int'>` is Python's way of writing “the type `int`”; the word `class` stands for a type here. The three names are abbreviations:

| Type | short for | meaning | examples |
|---|---|---|---|
| `int` | integer | whole number | `42`, `-7`, `0` |
| `float` | floating-point number | number with decimal places | `4.0`, `0.5`, `2.5e-3` |
| `str` | string | sequence of characters | `"42"`, `'Regen'` |

Which type a number gets is decided by its notation alone: without a point and without `e`, it is an `int`; with a point or with `e`, it is a `float`. That is why `4e3` is also a `float`, although the value 4000 is a whole number:

```console
>>> 4e3
4000.0
>>> type(4e3)
<class 'float'>
```

The plus sign shows what the type does. For two objects of type `int`, it adds; for two objects of type `str`, it joins the texts together; and for a `str` and an `int`, Python knows no rule:

```console
>>> 2 + 3
5
>>> "2" + "3"
'23'
>>> "2" + 3
Traceback (most recent call last):
  File "<python-input-2>", line 1, in <module>
    "2" + 3
    ~~~~^~~
TypeError: can only concatenate str (not "int") to str
```

The exception ([Chapter 1, Section 6.3](/wissen/en/informatik/programmieren/python/programme-und-der-python-interpreter/fehler-lesen-und-verstehen.html#stufe-6-3)) is of type `TypeError`. The description gives the reason: a `str` can only be extended by another `str`, not by an `int`. So Python does not convert the number 3 into the text `"3"` on its own.
::::

⁠**In short:** The type says what kind of value an object contains and what you can do with it; `type` displays it.

:::hintergrund How Python knows at run time what the plus sign should do
Main memory holds nothing but patterns of numbers. The same pattern can mean a number or a sequence of letters, depending on how you read it. That is why, in CPython, every object carries a reference to its type, right at the beginning of its memory area. When the interpreter loop ([Chapter 1, Section 2.4](/wissen/en/informatik/programmieren/python/programme-und-der-python-interpreter/vom-quelltext-zur-ausfuhrung-compiler-und-interpreter.html#stufe-2-4)) encounters a plus sign, it looks up the type of both values and carries out the addition rule that belongs to these types. If there is no matching rule, it raises a `TypeError`.

In the C language, this is different: there, you write down in the source code which type each memory cell has, and the compiler already chooses the matching machine instruction during translation. In the finished program, the type no longer appears anywhere. This makes C faster, because nothing has to be looked up. Python pays for the lookup with time on every calculation and gains flexibility in return: the same line of source code can work once with integers, once with floating-point numbers and once with text.
:::

### The identity

<span class="anker" id="stufe-1-3"></span>

Two objects can have the same type and the same value and still be two different boxes. To tell them apart, each object needs a mark that only it has.

**The place number.** In Fig. [1](#abb-1), each box stands at a place of its own. You recognize two boxes with the same label and the same content by their different place numbers.

:::definition Definition 1.3 (Identity)
<span class="anker" id="satz-1-3"></span>

The __identity__ of an object is an integer that distinguishes the object from all other objects that exist at the same time. It does not change as long as the object exists. The function `id` returns it.
:::

::::beispiel
The identity is a long number that looks random:

```console
>>> id(42)
11371408
>>> id("Regen")
140493353858800
```

On your computer, other numbers appear, and different ones again the next time Python starts. That does not matter: the numerical value never matters, only whether two objects have the same identity.
::::

For numbers and strings, moreover, the value of an object stays the same forever. A calculation does not change any existing object. It returns a new object that contains the result: `2 + 3` leaves the objects 2 and 3 untouched and returns an object with the value 5.

⁠**In short:** The identity is the fixed number of an object; `id` displays it.

:::hintergrund What the number means in CPython
In CPython, the identity is the address at which the object begins in main memory. Hence the large numbers. Other programs that run Python may assign other numbers; the language only requires that the number is unique and does not change.

Unique means: unique among the objects that exist at the same time. CPython frees an object that no part of the program needs anymore, and its place can be used for a new object. Two objects that exist one after the other can therefore get the same number. So if you compare identities, you have to make sure that both objects still exist.
:::

### The method

<span class="anker" id="stufe-1-4"></span>

Some abilities of a type do not fit any arithmetic symbol: converting a text to capital letters or writing a number as a fraction. For this, every type comes with functions of its own.

**Functions that belong to the box.** A function is a ready-made subprogram with a name ([Chapter 1, Section 4.7](/wissen/en/informatik/programmieren/python/programme-und-der-python-interpreter/der-interaktive-modus.html#stufe-4-7)). Some functions are attached to a type like buttons on a device: you press them on a particular object, and they work with exactly this object.

:::definition Definition 1.4 (Method)
<span class="anker" id="satz-1-4"></span>

A __method__ is a function that belongs to a type. You call it for an object by writing a dot, the name of the method and parentheses after the object.
:::

::::beispiel
The type `str` has a method `upper` that returns the text in capital letters. The type `float` has a method `as_integer_ratio` that writes the number as a fraction of numerator and denominator:

```console
>>> "Regen".upper()
'REGEN'
>>> (2.5).as_integer_ratio()
(5, 2)
>>> (2.5).upper()
Traceback (most recent call last):
  File "<python-input-2>", line 1, in <module>
    (2.5).upper()
    ^^^^^^^^^^^
AttributeError: 'float' object has no attribute 'upper'
```

The answer `(5, 2)` consists of two values in parentheses: the numerator 5 and the denominator 2, because $2.5=5/2$. The last input shows that each method belongs to its type: a `float` has no method `upper`. Python reports this as an `AttributeError`: nothing named `upper` is attached to the object. The parentheses around `2.5` ensure that Python does not take the dot before the method name for a decimal point. For an integer, you need them: without parentheses, Python would read `19.` as the beginning of the number $19.0$.
::::

⁠**In short:** A method is a function of a type; you call it with `objekt.name()`.

### Exercises for Section [1](#stufe-1)

<span class="anker" id="stufe-1-5"></span>

:::aufgabe Exercise 1 ★ Predicting types
<span class="anker" id="aufg-1"></span>

What type do these values have? First write down your prediction, then check it with `type`.

(a) `7` (b) `7.0` (c) `"7"` (d) `7e0` (e) `70e-1` (f) `"7.0"` (g) `-0`

:::loesung
The type is decided by the notation alone (subsection [1.2](#stufe-1-2)):

```console
>>> type(7)
<class 'int'>
>>> type(7.0)
<class 'float'>
>>> type("7")
<class 'str'>
>>> type(7e0)
<class 'float'>
>>> type(70e-1)
<class 'float'>
>>> type("7.0")
<class 'str'>
>>> type(-0)
<class 'int'>
```

(a) Digits without a point: `int`. (b) A point: `float`. (c) and (f) Anything in quotes is text, no matter what it looks like: `str`. (d) and (e) An `e` makes the number a `float`, even if its value is whole: `7e0` and `70e-1` are both `7.0`. (g) `-0` is the unary minus in front of the integer 0, so it is an `int` with the value 0.
:::
:::

:::aufgabe Exercise 2 ★ What does the type allow?
<span class="anker" id="aufg-2"></span>

Predict what the interactive mode displays, and check on the computer. Explain each error message using the concept of type.

<ol class="al">

<li>

`"Regen" + "bogen"`

</li>

<li>

`"Regen" + 1`

</li>

<li>

`"kilo".upper()`

</li>

<li>

`(0.75).as_integer_ratio()`

</li>

<li>

`(4.0).upper()`

</li>

</ol>

:::loesung
```console
>>> "Regen" + "bogen"
'Regenbogen'
>>> "Regen" + 1
Traceback (most recent call last):
  File "<python-input-1>", line 1, in <module>
    "Regen" + 1
    ~~~~~~~~^~~
TypeError: can only concatenate str (not "int") to str
>>> "kilo".upper()
'KILO'
>>> (0.75).as_integer_ratio()
(3, 4)
>>> (4.0).upper()
Traceback (most recent call last):
  File "<python-input-4>", line 1, in <module>
    (4.0).upper()
    ^^^^^^^^^^^
AttributeError: 'float' object has no attribute 'upper'
```

(a) Two `str`: for this type, `+` means joining the texts together. (b) For a `str` and an `int`, the plus sign has no rule; the type of the right operand does not fit, hence the `TypeError`. (c) `upper` is a method of the type `str`. (d) $0.75=\frac34$; `as_integer_ratio` is a method of the type `float`. (e) The type `float` has no method `upper`, hence the `AttributeError`: the type determines which methods exist.
:::
:::

:::aufgabe Exercise 3 ★★ Value, type, identity
<span class="anker" id="aufg-3"></span>

Two objects both have the type `float` and the value $0.5$. Using the picture of the boxes, explain how Python can still tell them apart. Why is the value alone not enough for this, and why are value and type together not enough either?

:::loesung
The picture shows two boxes with the label `float` and the content $0.5$ at two different places. Python tells them apart by their identity, the place number that `id` displays. The value alone is not enough, because both have the same value; value and type together are not enough either, because the types are the same, too. Only the identity is different for each object, as long as both exist at the same time. Whether two such objects exist separately at all or whether Python uses a single one is up to Python itself; but the question of how they differ arises as soon as there are two.
:::
:::

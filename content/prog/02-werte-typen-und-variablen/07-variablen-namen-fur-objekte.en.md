---
title: Variables: names for objects
pfad: Computer Science / Programming / Python / Values, Types and Variables
adresse: informatik/programmieren/python/werte-typen-und-variablen
knoten: Chapter 2: Values, Types and Variables
order: 6030700
summary: A calculation becomes readable when the values have names: preis / gewicht (German for “price / weight”) instead of 4.49 / 0.45 .
tags: assignment, variable, augmented assignment
lang: en
---

<span class="anker" id="stufe-6"></span>

:::zweck
A calculation becomes readable when the values have names: `preis / gewicht` (German for “price / weight”) instead of `4.49 / 0.45`. This section shows how Python connects a name with an object, which names are allowed and why an assignment copies nothing.
:::

### The assignment

<span class="anker" id="stufe-6-1"></span>

In interactive mode, the underscore `_` holds on to the last result ([Chapter 1, Section 4.4](/wissen/en/informatik/programmieren/python/programme-und-der-python-interpreter/der-interaktive-modus.html#stufe-4-4)), but only this one result and only until the next calculation. If you need a value several times, you want to keep it under a name of your own choosing.

**Attaching a tag to the box.** An object is a box in main memory (Fig. [1](objekte-und-typen.html#abb-1)). You can write a word on a tag and attach the tag to a box. Through the word, you find the box again later. Python takes a word without quotation marks to be such a name; the `NameError` in [Chapter 1](/wissen/en/informatik/programmieren/python/programme-und-der-python-interpreter/programme-und-der-python-interpreter.html) already showed this ([Chapter 1, Section 6.3](/wissen/en/informatik/programmieren/python/programme-und-der-python-interpreter/fehler-lesen-und-verstehen.html#stufe-6-3)).

:::definition Definition 6.1 (Assignment)
<span class="anker" id="satz-6-1"></span>

An __assignment__ is a statement of the form

⁠*name* `=` *expression*

Python evaluates the expression on the right and then connects the name on the left with the object that has been created in the process. The name is said to be *bound* to the object.
:::

Here, the equals sign does not state an equation as in mathematics; it is an instruction: “Attach the name on the left to the result on the right.” The direction is fixed: the name always stands on the left.

::::beispiel
Price, weight and price per kilogram of the chocolate spread from [Chapter 1, Section 4.4](/wissen/en/informatik/programmieren/python/programme-und-der-python-interpreter/der-interaktive-modus.html#stufe-4-4), plus the price for 100 g:

```console
>>> preis = 4.49
>>> gewicht = 0.45
>>> preis / gewicht
9.977777777777778
>>> kilopreis = preis / gewicht
>>> kilopreis / 10
0.9977777777777778
```

After an assignment, the interactive mode displays nothing. An assignment is a statement ([Chapter 1, Section 1.1](/wissen/en/informatik/programmieren/python/programme-und-der-python-interpreter/programme-und-programmiersprachen.html#stufe-1-1)), not an expression; it has no value that could be displayed. Its only effect is that the name means something from now on.
::::

⁠**In short:** `name = ausdruck` evaluates the expression and binds the name to the result.

### The variable

<span class="anker" id="stufe-6-2"></span>

After a few assignments, there are several names, each attached to an object. This pair of name and object needs a word of its own.

**A diagram of names and arrows.** You draw the names on the left, the objects on the right and an arrow from each name to its object. Such a picture is called a state diagram: it shows the state of the program at one moment (Fig. [9](#abb-9), left).

:::definition Definition 6.2 (Variable)
<span class="anker" id="satz-6-2"></span>

A name that is bound to an object is called a __variable__. The value of the variable is the value of this object.
:::

A variable comes into being with its first assignment. Before that, the name is unknown, and Python reports a `NameError`.

::::beispiel
The session from the previous subsection continues:

```console
>>> kg_fuer_zehn
Traceback (most recent call last):
  File "<python-input-5>", line 1, in <module>
    kg_fuer_zehn
NameError: name 'kg_fuer_zehn' is not defined
>>> kg_fuer_zehn = 10 / kilopreis
>>> kg_fuer_zehn
1.0022271714922049
```

Only the assignment turns the name `kg_fuer_zehn` (German for “kg for ten”) into a variable: this is how many kilograms of chocolate spread you get for €10. After that, the state diagram contains a fourth name with an arrow to a `float` object with the value $1.002$.
::::

⁠**In short:** A variable is a name that is bound to an object; it comes into being with the first assignment.

### Rebinding instead of copying

<span class="anker" id="stufe-6-3"></span>

What happens with `y = x`? Does `y` get a copy of the value of `x`? And what happens to `y` if you change `x` afterward?

**Moving tags.** In the picture of tags, the answer is simple: `y = x` attaches a second tag to the *same* box. `x = x + 1` calculates with the box to which `x` is attached, puts the result into a new box and moves the tag `x` there. The tag `y` stays where it was (Fig. [9](#abb-9)).

:::abbildung prog/k2etikett 9
State diagrams. Left: after `y = x`, both names are bound to the same object; nothing was copied. Right: `x = x + 1` creates a new object with the value 6 and binds `x` to it. The object 5 remains unchanged, and `y` is still attached to it.
:::

:::satz Theorem 6.3 (Assignment does not copy)
<span class="anker" id="satz-6-3"></span>

An assignment never creates a copy of an object. `y = x` binds `y` to the same object to which `x` is bound. A later assignment to `x` rebinds only `x`; `y` stays with its object.
:::

::::beispiel
The identity (subsection [1.3](objekte-und-typen.html#stufe-1-3)) reveals which object is behind a name:

```console
>>> x = 5
>>> y = x
>>> id(x)
11370224
>>> id(y)
11370224
>>> x = x + 1
>>> x
6
>>> y
5
>>> id(x)
11370256
```

After `y = x`, both names have the same identity: one object, two tags. After `x = x + 1`, `x` has a new identity and `y` the old one. The object 5 has not changed; it cannot change either, because the value of a number stays the same forever (subsection [1.3](objekte-und-typen.html#stufe-1-3)).
::::

⁠**In short:** An assignment attaches a tag to an object or moves the tag to another object; it copies nothing.

:::hintergrund Box or tag: the difference from C
In C, a variable is a fixed place in memory, a small box with a particular type. There, `y = x` copies the content of the box `x` into the box `y`; afterward, there are two independent copies. In Python, by contrast, a variable is a name that refers to an object. The object carries the type, the name does not. That is why the same name may be bound first to a number and then to a string, which would not be possible in C.

With numbers, the difference goes unnoticed: whether `y` has a copy of the 5 or points to the same 5 makes no difference, because a number never changes. Still, it pays to have the right picture in mind from the start, that is, tags instead of boxes. It explains the identities in the session above, and it remains correct for all other types as well.
:::

### The naming rules

<span class="anker" id="stufe-6-4"></span>

Not every word can serve as a name. During translation, Python has to be able to tell a name apart from a number, an operator and the fixed words of the language.

:::definition Definition 6.4 (Naming rules)
<span class="anker" id="satz-6-4"></span>

A name consists of letters, digits and the underscore `_`. It must not begin with a digit and must not be a keyword. Uppercase and lowercase letters are different: `Wert` and `wert` are two names.
:::

A keyword is a word that has a fixed meaning in Python. Python 3.13 and 3.14 have 35 of them:

|  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
| `False` | `None` | `True` | `and` | `as` | `assert` | `async` |
| `await` | `break` | `class` | `continue` | `def` | `del` | `elif` |
| `else` | `except` | `finally` | `for` | `from` | `global` | `if` |
| `import` | `in` | `is` | `lambda` | `nonlocal` | `not` | `or` |
| `pass` | `raise` | `return` | `try` | `while` | `with` | `yield` |

Letters with umlauts are allowed in names; `größe` (German for “size”) is a valid name. The usual style, however, is names made of lowercase letters without umlauts, with words separated by underscores: `preis_pro_kg`, `gewicht_g`. The programs in this chapter follow this style; for German words, they write ae, oe, ue and ss instead of ä, ö, ü and ß, as in `kg_fuer_zehn`.

::::beispiel
Three violations, each with its message:

```console
>>> 3d = 4
  File "<python-input-0>", line 1
    3d = 4
    ^
SyntaxError: invalid decimal literal
>>> mein-wert = 4
  File "<python-input-1>", line 1
    mein-wert = 4
    ^^^^^^^^^
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
>>> class = 4
  File "<python-input-2>", line 1
    class = 4
          ^
SyntaxError: invalid syntax
```

`3d` begins with a digit; Python reads the beginning as a number and stumbles over the `d`. Python reads `mein-wert` as the calculation `mein` minus `wert`, and you cannot bind anything to a calculation. The suggestion with `==` does not help here; what was meant is a name, so `mein_wert`. `class` is a keyword.
::::

**A trap: overwriting built-in names.** `print`, `type`, `id` and the other built-in functions are names too, but not keywords. You may rebind them, and then they are gone:

```console
>>> print = 5
>>> print("Hallo")
Traceback (most recent call last):
  File "<python-input-1>", line 1, in <module>
    print("Hallo")
    ~~~~~^^^^^^^^^
TypeError: 'int' object is not callable
```

The name `print` is now attached to the number 5, and you cannot call a number. The remedy: choose a different name and restart the interactive mode.

⁠**In short:** Names consist of letters, digits and `_`, do not begin with a digit and are not keywords; you should not rebind built-in names.

### The augmented assignment

<span class="anker" id="stufe-6-5"></span>

Counting up counters and adding up values happen so often that Python has a shorthand for them. `zaehler = zaehler + 1` mentions the name of the counter twice.

:::definition Definition 6.5 (Augmented assignment)
<span class="anker" id="satz-6-5"></span>

For an arithmetic operator $\circ$ from `+ - * / // % **`, the __augmented assignment__ *name* $\circ$`=` *expression* means the same for numbers as *name* `=` *name* $\circ$ `(`*expression*`)`.
:::

The parentheses are important: the entire expression on the right is evaluated first. `x *= 2 + 3` multiplies `x` by five.

::::beispiel
A counter and a sum built from steps of $0.1$, as in subsection [5.1](rechnen-mit-gleitkommazahlen.html#stufe-5-1):

```console
>>> zaehler = 0
>>> zaehler += 1
>>> zaehler += 1
>>> zaehler
2
>>> summe = 0.0
>>> summe += 0.1
>>> summe += 0.1
>>> summe += 0.1
>>> summe
0.30000000000000004
>>> x = 10
>>> x *= 2 + 3
>>> x
50
```

An augmented assignment also rebinds the name: `zaehler += 1` creates a new `int` object and attaches the tag `zaehler` to it.
::::

⁠**In short:** For numbers, `x += a` is the short form of `x = x + (a)`; likewise `-=`, `*=`, `/=`, `//=`, `%=` and `**=`.

### Variables in a script

<span class="anker" id="stufe-6-6"></span>

With variables, a script becomes a reusable calculation: the assumptions are at the top, each one once, and the formulas below them read like those in a textbook. [Chapter 1](/wissen/en/informatik/programmieren/python/programme-und-der-python-interpreter/programme-und-der-python-interpreter.html) converted a recipe for pizza dough from 4 to 6 people using fixed numbers ([Chapter 1, Section 5.3](/wissen/en/informatik/programmieren/python/programme-und-der-python-interpreter/skripte-schreiben-und-ausfuhren.html#stufe-5-3)). With names, the same script looks like this:

```python rezept_variablen.py
# Convert pizza dough, with a name for each quantity
personen = 6          # this many people eat
personen_rezept = 4   # the recipe serves this many
mehl_rezept = 500     # flour in the recipe in g
wasser_rezept = 300   # water in the recipe in ml

faktor = personen / personen_rezept   # how often you need the recipe
mehl = mehl_rezept * faktor
wasser = wasser_rezept * faktor

print("Mehl in g:", mehl)
print("Wasser in ml:", wasser)
```

```console Windows (PowerShell)
PS> py rezept_variablen.py
Mehl in g: 750.0
Wasser in ml: 450.0
```

```console Linux
$ python3 rezept_variablen.py
Mehl in g: 750.0
Wasser in ml: 450.0
```

For a different number of guests, you change only the second line. Each name says what the number means, and the unit is in the comment after it, because Python knows nothing about units.

⁠**In short:** Variables turn fixed numbers into named assumptions; the formulas below them calculate with the names.

### Exercises for Section [6](#stufe-6)

<span class="anker" id="stufe-6-7"></span>

:::aufgabe Exercise 21 ★ Predicting state diagrams
<span class="anker" id="aufg-21"></span>

Draw the state diagram after each line and state the values of `a`, `b` and `c` at the end. Check in interactive mode and compare the identities with `id`.

```python
a = 10
b = a
a = a * 2
c = b
b = b - 1
```

:::loesung
| after the line | bindings | new object? |
|---|---|---|
| `a = 10` | `a` $\to$ 10 | yes, 10 |
| `b = a` | `a`, `b` $\to$ 10 | no |
| `a = a * 2` | `a` $\to$ 20, `b` $\to$ 10 | yes, 20 |
| `c = b` | `a` $\to$ 20, `b`, `c` $\to$ 10 | no |
| `b = b - 1` | `a` $\to$ 20, `b` $\to$ 9, `c` $\to$ 10 | yes, 9 |

At the end, $a=20$, $b=9$, $c=10$. In interactive mode:

```console
>>> a = 10
>>> b = a
>>> a = a * 2
>>> c = b
>>> b = b - 1
>>> a
20
>>> b
9
>>> c
10
>>> id(c)
11370384
>>> id(b)
11370352
```

`c` hangs on the original object 10, which first carried the tag `a` and then `b`. No line changed an object; each calculation created a new one, and the assignments only moved tags.
:::
:::

:::aufgabe Exercise 22 ★ Allowed names
<span class="anker" id="aufg-22"></span>

Which names are allowed, which are not, and which are allowed but a poor choice? Give reasons.

`preis_1`, `1preis`, `T_max`, `T-max`, `for`, `For`, `_zwischen`, `größe`, `type`

:::loesung
<ul>

<li>

`preis_1`: allowed and good.

</li>

<li>

`1preis`: not allowed, begins with a digit.

</li>

<li>

`T_max`: allowed; lowercase letters would be usual, `t_max`. In a formula with formula symbols, for instance $T$ for a temperature, the capital letter can make sense, though.

</li>

<li>

`T-max`: not allowed; Python reads `T` minus `max`.

</li>

<li>

`for`: not allowed, keyword.

</li>

<li>

`For`: allowed, because upper and lower case matter, but confusingly close to the keyword.

</li>

<li>

`_zwischen`: allowed; an underscore at the beginning is permitted.

</li>

<li>

`größe`: allowed, but against the usual practice of writing names without umlauts.

</li>

<li>

`type`: allowed, but a poor choice: afterward, the name of the built-in function `type` is hidden.

</li>

</ul>
:::
:::

:::aufgabe Exercise 23 ★★ Augmented assignments
<span class="anker" id="aufg-23"></span>

Predict the value of `x` after each line. Then check in interactive mode.

```python
x = 7
x //= 2
x **= 3
x %= 5
x -= 2 * 3
x /= 4
```

:::loesung
```console
>>> x = 7
>>> x //= 2
>>> x
3
>>> x **= 3
>>> x
27
>>> x %= 5
>>> x
2
>>> x -= 2 * 3
>>> x
-4
>>> x /= 4
>>> x
-1.0
```

$7\,/\!/\,2=3$; $3^3=27$; $27\,\%\,5=2$; $2-(2\cdot3)=-4$, the right-hand side is calculated in full first; $-4/4=-1.0$, a `float`, because `/` always returns a `float`.
:::
:::

:::aufgabe Exercise 24 ★★ Modifying the recipe script
<span class="anker" id="aufg-24"></span>

<ol class="al">

<li>

Change `rezept_variablen.py` for 9 people and a bread dough: the recipe is for 4 people and needs $600\,\mathrm g$ of flour and $400\,\mathrm{ml}$ of water. Which lines do you have to change?

</li>

<li>

Add a variable `mehl_kg` for the flour in kilograms and output it as well. Why is it better to calculate it from `mehl` than to type in the number 1.35 by hand?

</li>

</ol>

:::loesung
(a) Only the assumptions at the top change, here three of them: `personen`, `mehl_rezept` and `wasser_rezept`; the recipe is still for 4 people. The formulas stay the same. (b) `mehl_kg` is calculated from `mehl`. If you later change the number of people, the display in kilograms automatically stays correct, and there is no second place where you could forget to change the number:

```python rezept_brot.py
# Convert bread dough, with a name for each quantity
personen = 9          # this many people eat
personen_rezept = 4   # the recipe serves this many
mehl_rezept = 600     # flour in the recipe in g
wasser_rezept = 400   # water in the recipe in ml

faktor = personen / personen_rezept   # how often you need the recipe
mehl = mehl_rezept * faktor
wasser = wasser_rezept * faktor
mehl_kg = mehl / 1000                 # flour in kg, computed from mehl

print("Mehl in kg:", mehl_kg)
print("Mehl in g:", mehl)
print("Wasser in ml:", wasser)
```

```console Linux
$ python3 rezept_brot.py
Mehl in kg: 1.35
Mehl in g: 1350.0
Wasser in ml: 900.0
```

Mental check: 9 people are $2.25$ times 4 people, and $2.25\cdot600\,\mathrm g=1350\,\mathrm g$, $2.25\cdot400\,\mathrm{ml}=900\,\mathrm{ml}$. On Windows (`py rezept_brot.py`), the same output appears.
:::
:::

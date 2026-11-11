---
title: Decisions: if, elif and else
pfad: Computer Science / Programming / Python / Decisions and Loops
adresse: informatik/programmieren/python/entscheidungen-und-schleifen
knoten: Chapter 3: Decisions and Loops
order: 6040300
summary: A condition alone does not make anything happen yet; a script still runs line by line from top to bottom (Chapter 1, Section 5.2).
tags: conditional statement, header line, block
lang: en
---

<span class="anker" id="stufe-2"></span>

:::zweck
A condition alone does not make anything happen yet; a script still runs line by line from top to bottom ([Chapter 1, Section 5.2](/wissen/en/informatik/programmieren/python/programme-und-der-python-interpreter/skripte-schreiben-und-ausfuhren.html#stufe-5-2)). This section shows how a script executes lines only if a condition is satisfied, how Python recognizes which lines belong to it and how to choose between several cases.
:::

### The conditional statement `if`

<span class="anker" id="stufe-2-1"></span>

A script reads in the temperature in a room. It should print a warning only if it is warmer than 23 °C there.

**A fork in the flow.** A flowchart draws the flow of a program: a box stands for a statement, a diamond for a question, and the arrows show what comes next. Two arrows lead out of the diamond, one for yes and one for no (Fig. [1](#abb-1), left). On the no path, the box with the warning is simply bypassed.

:::abbildung prog/k3if 1
Flowcharts of a decision. Left, `if`: if the condition is satisfied, the box below the diamond runs; otherwise it is bypassed. Right, `if` with `else`: exactly one of the two boxes runs. In both cases, the flow then continues at the same place.
:::

:::definition Definition 2.1 (Conditional statement)
<span class="anker" id="satz-2-1"></span>

A __conditional statement__ has the form

`if Bedingung:` ` Anweisungen`

The first line is called the __header line__; it begins with `if` and ends with a colon. Below it are one or more statements, indented further than the header line. Python evaluates the condition and determines its truth value (Subsection [1.9](bedingungen-vergleiche-und-logische-operatoren.html#stufe-1-9)). If it is `True`, Python executes the indented statements; otherwise it skips them. In both cases, execution then continues with the next line that again starts as far to the left as the header line.
:::

::::beispiel
The script asks for the temperature and checks it (“Achtung: zu warm” is German for “Caution: too warm”, “fertig” for “done”):

```python temperatur_if.py
# Check the room temperature: at most 23 degrees are wanted
temp = float(input("Temperatur in Grad: "))
if temp > 23:
    print("Achtung: zu warm")
print("fertig")
```

Started twice, once with 24.5 °C and once with 22 °C:

```console Linux
$ python3 temperatur_if.py
Temperatur in Grad: 24.5
Achtung: zu warm
fertig
$ python3 temperatur_if.py
Temperatur in Grad: 22
fertig
```

```console Windows (PowerShell)
PS> py temperatur_if.py
Temperatur in Grad: 24.5
Achtung: zu warm
fertig
```

The last line of the script runs in both cases, because it no longer belongs to the condition.
::::

⁠**In short:** `if Bedingung:` executes the indented lines below it only if the condition is true.

### The block and indentation

<span class="anker" id="stufe-2-2"></span>

Often several statements depend on the same condition. Python must then recognize where they end and where the script continues for all cases.

**Like an outline.** In an outline, subitems are indented; whatever starts further to the left no longer belongs to them. Python reads indentation in the same way (Fig. [2](#abb-2)).

:::abbildung prog/k3block 2
A block can be recognized by its indentation. The two indented lines (blue background) belong to the header line above them; the last line again starts as far to the left as the header line and always runs.
:::

:::definition Definition 2.2 (Block)
<span class="anker" id="satz-2-2"></span>

A __block__ is a sequence of statements that are all indented by the same amount and follow a header line, that is, a line with a colon at the end. It ends before the first line that is indented less. A block may itself contain header lines with their own blocks, indented even further. Four spaces per level are usual; this is what the style guide for Python, PEP 8, recommends.
:::

::::beispiel
Two statements in the block:

```python temperatur_block.py
# Two statements depend on the same condition
temp = float(input("Temperatur in Grad: "))
if temp > 23:
    zuviel = temp - 23
    print(f"Achtung: um {zuviel:.1f} Grad zu warm")
print("fertig")
```

```console Linux
$ python3 temperatur_block.py
Temperatur in Grad: 24.5
Achtung: um 1.5 Grad zu warm
fertig
```
::::

**Blocks in interactive mode.** You can enter a block there too. After the header line, Python shows the continuation prompt `...` instead of `>>>` ([Chapter 1, Section 4.1](/wissen/en/informatik/programmieren/python/programme-und-der-python-interpreter/der-interaktive-modus.html#stufe-4-1)). As of Python 3.13, interactive mode indents the next line by four spaces on its own; you only type the statement. An empty line ends the input; only then does the block run. Here the block contains a second header line with its own block, indented more deeply:

```console
>>> temp = 24.5
>>> if temp > 20:
...     print("nicht zu kalt")
...     if temp > 23:
...         print("aber zu warm")
...
nicht zu kalt
aber zu warm
```

**Errors in the indentation.** If an indentation is wrong, Python rejects the whole script while translating it, as with any syntax error ([Chapter 1, Section 6.1](/wissen/en/informatik/programmieren/python/programme-und-der-python-interpreter/fehler-lesen-und-verstehen.html#stufe-6-1)). If the block after a header line is missing, the message is:

```python einrueckung_fehlt.py
temp = 24.5
if temp > 23:
print("Achtung: zu warm")
```

```console Linux
$ python3 einrueckung_fehlt.py
  File "/home/student/python-kurs/einrueckung_fehlt.py", line 3
    print("Achtung: zu warm")
    ^^^^^
IndentationError: expected an indented block after 'if' statement on line 2
```

If a line moves back to a depth that did not exist before, Python finds no block to which it belongs:

```python einrueckung_uneben.py
temp = 24.5
if temp > 23:
    print("Achtung: zu warm")
  print("Bitte lüften")
```

```console Linux
$ python3 einrueckung_uneben.py
  File "/home/student/python-kurs/einrueckung_uneben.py", line 4
    print("Bitte lüften")
                         ^
IndentationError: unindent does not match any outer indentation level
```

A third message, `TabError: inconsistent use of tabs and spaces in indentation`, appears if a file mixes tabs and spaces in such a way that the meaning would depend on the width of a tab. Good editors insert four spaces when you press the Tab key; then this cannot happen.

⁠**In short:** The indentation determines which lines belong to a header line; a block ends where a line starts further to the left again.

:::hintergrund Why Python forms blocks by indentation
Many languages group a block with braces, C for example with `{` and `}`. Without braces, only the first statement belongs to the condition in C, no matter how the lines are indented. In

```c
if (temp > 23)
    fenster_auf = 1;
    heizung_aus();
```

`heizung_aus();` therefore always runs, even though the indentation claims the opposite. Whoever reads the code sees one grouping, the compiler another, and such errors are hard to find. In Python, this cannot happen: there are no braces for blocks, so readers and translator cannot see the grouping differently. The indentation that a good programmer would write anyway is itself the rule. As a side effect, the dispute over where the braces belong disappears, and programs become shorter.
:::

:::hintergrund What the translator makes of the indentation
When splitting a file into its tokens, CPython turns the indentation into two invisible tokens, “indent” and “dedent”, which play exactly the role of the braces in C. For this, it keeps a stack of indentation depths on which initially only the 0 lies. If a new line is indented more deeply than the top number on the stack, it puts the line's depth on top and produces an “indent”. If the line is indented less deeply, it takes numbers off, producing one “dedent” for each, until the top number equals the new depth. If this depth is not on the stack, that is exactly the error “unindent does not match any outer indentation level”. When the depth is measured, a tab counts up to the next multiple of 8. Because other programs often display a tab four characters wide, Python rejects files whose meaning would depend on this width; that is where the `TabError` comes from.
:::

### The alternative `else`

<span class="anker" id="stufe-2-3"></span>

The script should not only warn but, in the other case, confirm that the temperature is right. So there are two paths, and exactly one of them should run.

**Two paths out of the diamond.** In the right flowchart of Fig. [1](#abb-1), each of the two arrows leads to a box of its own; afterward, the paths meet again.

:::definition Definition 2.3 (`else`)
<span class="anker" id="satz-2-3"></span>

The block of a conditional statement may be followed by a line `else:`, indented exactly as far as the corresponding `if`, and then by a block of its own. This block runs if and only if the condition is false. So of the two blocks, exactly one always runs.
:::

::::beispiel
The script from Subsection [2.1](#stufe-2-1) with a second path:

```python temperatur_else.py
# Check the temperature: warning or confirmation, exactly one
temp = float(input("Temperatur in Grad: "))
if temp > 23:
    print("Achtung: zu warm")
else:
    print("Temperatur in Ordnung")
print("fertig")
```

```console Windows (PowerShell)
PS> py temperatur_else.py
Temperatur in Grad: 22
Temperatur in Ordnung
fertig
```

`else` has no condition, because it is exactly the case in which the condition of the `if` does not hold.
::::

⁠**In short:** `else` specifies the block that runs if the condition is false.

### Several cases: `elif`

<span class="anker" id="stufe-2-4"></span>

The room can be too cold, OK or too warm. For three or more cases, a single `else` is not enough.

**Questions one after another.** You ask the questions in order, and the first one answered with yes decides (Fig. [3](#abb-3)). Whatever comes after it is not asked at all.

:::abbildung prog/k3elif 3
Flowchart of `if`, `elif` and `else`. The questions are asked from top to bottom; the first one with the answer yes selects its box, and all the others are skipped. If no answer is yes, the `else` box runs. Afterward, the flow continues at a common place.
:::

:::definition Definition 2.4 (`elif`)
<span class="anker" id="satz-2-4"></span>

Between the block of an `if` and an optional `else`, any number of lines `elif Bedingung:` may stand, each with a block, all indented as far as the `if`. `elif` is short for “else if”. Python checks the conditions from top to bottom. It executes the block of the first condition that is true and skips all the others. If none is true, the block after `else` runs, if there is one.
:::

::::beispiel
The three cases of the room temperature (“zu kalt”, “in Ordnung” and “zu warm” are German for “too cold”, “OK” and “too warm”):

```python temperatur_elif.py
# Classify the room temperature: 20 to 23 degrees are wanted
temp = float(input("Temperatur in Grad: "))
if temp < 20:
    print("zu kalt")
elif temp <= 23:
    print("in Ordnung")
else:
    print("zu warm")
```

```console Linux
$ python3 temperatur_elif.py
Temperatur in Grad: 18.5
zu kalt
$ python3 temperatur_elif.py
Temperatur in Grad: 21.5
in Ordnung
$ python3 temperatur_elif.py
Temperatur in Grad: 24.5
zu warm
```

The second condition checks only the upper limit. That is enough, because Python reaches it only if the first one was false, that is, if `temp` is at least 20. The order of the cases therefore matters: if you swap them, you get a different program.
::::

Two typing errors are common. `else if` instead of `elif` gives `SyntaxError: expected ':'`. An `elif` after the `else` is also a syntax error; Python 3.14 says so explicitly with `'elif' block follows an 'else' block`, Python 3.13 only with `invalid syntax`.

⁠**In short:** With `if`, `elif` and `else`, exactly the block of the first true condition runs, otherwise the `else` block.

:::hintergrund A choice among fixed values: `match`
Since Python 3.10, there has been another notation for the common case in which a value is compared with a series of fixed values. After `match` comes the value, after each `case` a possible value; the underscore `_` matches anything and takes on the role of `else`:

```python einheit.py
# Explain unit symbols: multiple choice with match (since Python 3.10)
zeichen = input("Einheitenzeichen: ")
match zeichen:
    case "m":
        print("Meter, die Einheit der Länge")
    case "s":
        print("Sekunde, die Einheit der Zeit")
    case "kg":
        print("Kilogramm, die Einheit der Masse")
    case _:
        print("unbekannt")
```

```console Linux
$ python3 einheit.py
Einheitenzeichen: s
Sekunde, die Einheit der Zeit
$ python3 einheit.py
Einheitenzeichen: x
unbekannt
```

A chain `if zeichen == "m": … elif zeichen == "s": …` does the same. Python also checks the `case` lines from top to bottom, and only the block of the first matching one runs. `match` can do much more, such as taking values apart; for comparisons with ranges, as with the temperature, `elif` remains the usual form.
:::

### Typical errors in conditions

<span class="anker" id="stufe-2-5"></span>

Most errors in decisions have one of the following causes.

<ul>

<li>

⁠**`=` instead of `==`.** `if temp = 20:` is an assignment in the place of a condition. Python reports `SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?`.

</li>

<li>

⁠**The colon is missing.** `if temp > 23` without a colon gives `SyntaxError: expected ':'`.

</li>

<li>

⁠**`or` with a single value.** `if einheit == "m" or "s":` does not ask whether `einheit` is one of the two values. Python reads `(einheit == "m") or "s"`, and `"s"` is true:

```console
>>> einheit = "kg"
>>> einheit == "m" or "s"
's'
>>> einheit == "m" or einheit == "s"
False
```

</li>

<li>

⁠**Floating-point numbers with `==`.** `if 0.1 + 0.2 == 0.3:` is never satisfied; floating-point numbers are compared with a tolerance ([Chapter 2, Section 7.4](/wissen/en/informatik/programmieren/python/werte-typen-und-variablen/wahrheitswerte-und-vergleiche.html#stufe-7-4)).

</li>

<li>

⁠**Text instead of a number.** Without a type conversion, `if eingabe < "9":` compares text (Subsection [1.3](bedingungen-vergleiche-und-logische-operatoren.html#stufe-1-3)), and `if eingabe < 9:` aborts with `TypeError`.

</li>

</ul>

⁠**In short:** `==` instead of `=`, a colon at the end, every partial condition written out in full, floating-point numbers with a tolerance, inputs converted first.

### Application: a scale with underflow and overflow

<span class="anker" id="stufe-2-6"></span>

A digital kitchen scale stores every weight as an integer, as in the exercise on the kitchen scale in [Chapter 2, Section 3](/wissen/en/informatik/programmieren/python/werte-typen-und-variablen/zahlen-im-binarsystem.html#stufe-3). Here, this number is called the raw value. A scale with 12 bits and the range 0 kg to 5 kg divides the range into $2^{12}=4096$ equal steps of $5\,\mathrm{kg}/4096=1.220703125$ g each. The raw value of a weight $m$ is the number of full steps below it, $\lfloor m/(1.220703125\,\mathrm{g})\rfloor$; the largest raw value is 4095. The scale cannot represent weights outside the range. It reports an underflow, for example if you have set it to zero with a bowl on it and then take the bowl off, or an overflow.

The three cases call for `if`, `elif` and `else`. The integer conversion `int` cuts off the decimal places ([Chapter 2, Section 10.4](/wissen/en/informatik/programmieren/python/werte-typen-und-variablen/zeichenketten-eingabe-und-ausgabe.html#stufe-10-4)); for positive numbers, that is exactly rounding down.

```python waage.py
# Kitchen scale with 12 bits and the range 0 kg to 5 kg
gewicht = float(input("Gewicht in kg: "))
stufe = 5.0 / 4096                   # weight per step in kg
if gewicht < 0:
    print("Unterlauf: Rohwert 0")
elif gewicht >= 5.0:
    print("Überlauf: Rohwert 4095")
else:
    rohwert = int(gewicht / stufe)
    print(f"Rohwert {rohwert}, hexadezimal {rohwert:03x}")
```

```console Linux
$ python3 waage.py
Gewicht in kg: 2.5
Rohwert 2048, hexadezimal 800
$ python3 waage.py
Gewicht in kg: 1.0
Rohwert 819, hexadezimal 333
$ python3 waage.py
Gewicht in kg: 5.2
Überlauf: Rohwert 4095
$ python3 waage.py
Gewicht in kg: -0.1
Unterlauf: Rohwert 0
```

Half the maximum weight, 2.5 kg, gives exactly $2048=2^{11}$, hexadecimal `800`: the top one of the 12 bits is set, and all the others are zero. 1 kg corresponds to $819.2$ steps, that is, to the raw value 819.

⁠**In short:** Three mutually exclusive ranges of a quantity call for `if`, `elif` and `else`.

### Exercises for Section [2](#stufe-2)

<span class="anker" id="stufe-2-7"></span>

:::aufgabe Exercise 6 ★ Predicting the output
<span class="anker" id="aufg-6"></span>

A script contains this decision:

```python
if temp > 20:
    print("in Ordnung")
elif temp > 23:
    print("zu warm")
else:
    print("zu kalt")
```

What does it print for `temp = 18.5`, `temp = 22.0` and `temp = 24.5`? Which case can never occur, and why? Change the order so that all three cases are recognized correctly.

:::loesung
For `temp = 18.5`, the first condition is false, and so is the second, so `else` runs: “zu kalt”. For `temp = 22.0`, the first condition is true: “in Ordnung”. For `temp = 24.5`, the first condition is true as well, because $24.5>20$: “in Ordnung”, and that is wrong. The case “zu warm” can never occur: every temperature above 23 is also above 20 and is already taken by the first case; `elif` is then not even checked.

It becomes correct when the narrower condition comes first:

```python
if temp > 23:
    print("zu warm")
elif temp > 20:
    print("in Ordnung")
else:
    print("zu kalt")
```

Now the second case only receives temperatures up to 23 °C. The order from bottom to top, as in `temperatur_elif.py`, with `temp < 20` first, is just as correct. The two versions differ only at the limit 20: here, exactly 20 °C counts as “zu kalt”, in `temperatur_elif.py` as “in Ordnung”.
:::
:::

:::aufgabe Exercise 7 ★★ Finding the errors
<span class="anker" id="aufg-7"></span>

The script `fehler_if.py` contains three errors:

```python fehler_if.py
temp = float(input("Temperatur in Grad: "))
if temp = 20.0
    print("genau 20 Grad")
else if temp > 20.0:
    print("mehr als 20 Grad")
```

Which error does Python report first, and why only this one? Fix the errors one after another and note down the next message each time. Why is `temp == 20.0` nevertheless not a good condition for a measured temperature?

:::loesung
Python translates the whole file before it executes a single line, and it stops at the first syntax error ([Chapter 1, Section 6.1](/wissen/en/informatik/programmieren/python/programme-und-der-python-interpreter/fehler-lesen-und-verstehen.html#stufe-6-1)). That is why only one message ever appears, and no line runs, not even the `input` in line 1:

```console Linux
$ python3 fehler_if.py
  File "/home/student/python-kurs/fehler_if.py", line 2
    if temp = 20.0
       ^^^^^^^^^^^
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
```

With `if temp == 20.0` (file `fehler_if2.py`), the next error appears, the missing colon:

```console Linux
$ python3 fehler_if2.py
  File "/home/student/python-kurs/fehler_if2.py", line 2
    if temp == 20.0
                   ^
SyntaxError: expected ':'
```

With the colon (`fehler_if3.py`), `else if` remains. Python reads `else` and then immediately expects the colon:

```console Linux
$ python3 fehler_if3.py
  File "/home/student/python-kurs/fehler_if3.py", line 4
    else if temp > 20.0:
         ^^
SyntaxError: expected ':'
```

With `elif`, the script runs:

```python fehler_if_ok.py
temp = float(input("Temperatur in Grad: "))
if temp == 20.0:
    print("genau 20 Grad")
elif temp > 20.0:
    print("mehr als 20 Grad")
```

```console Linux
$ python3 fehler_if_ok.py
Temperatur in Grad: 20.0
genau 20 Grad
$ python3 fehler_if_ok.py
Temperatur in Grad: 20.000001
mehr als 20 Grad
```

For a measurement, `temp == 20.0` is nevertheless not a good condition. A thermometer almost never delivers exactly 20.000000, and a calculated result carries rounding errors ([Chapter 2, Section 7.3](/wissen/en/informatik/programmieren/python/werte-typen-und-variablen/wahrheitswerte-und-vergleiche.html#stufe-7-3)). A comparison with a tolerance makes sense, such as `abs(temp - 20.0) <= 0.1` or `math.isclose(temp, 20.0, abs_tol=0.1)`. For 20.000001, the second output shows how narrowly a measurement can miss equality.
:::
:::

:::aufgabe Exercise 8 ★★ The result of an exam
<span class="anker" id="aufg-8"></span>

Write a script `klausur.py` that asks for the score in an exam with at most 100 points and prints: below 50 points “nicht bestanden”, below 85 “bestanden”, up to and including 100 “mit Auszeichnung”, above that “ungültig” (German for “failed”, “passed”, “with distinction” and “invalid”). Test it with 49.5, 50, 70 and 101 points.

:::loesung
The cases are delimited from bottom to top; each condition needs only the upper limit, because Python reaches it only if the previous one was false.

```python klausur.py
# Result of an exam from the score (0 to 100)
punkte = float(input("Punkte: "))
if punkte < 50:
    print("nicht bestanden")
elif punkte < 85:
    print("bestanden")
elif punkte <= 100:
    print("mit Auszeichnung")
else:
    print("ungültig")
```

```console Linux
$ python3 klausur.py
Punkte: 49.5
nicht bestanden
$ python3 klausur.py
Punkte: 50
bestanden
$ python3 klausur.py
Punkte: 70
bestanden
$ python3 klausur.py
Punkte: 101
ungültig
```

The test with exactly 50 points checks the limit: “below 50” is false there, so “bestanden” applies.
:::
:::

:::aufgabe Exercise 9 ★★ Leap years
<span class="anker" id="aufg-9"></span>

A year is a leap year if it is divisible by 4, unless it is divisible by 100; years divisible by 400, however, are leap years again.

<ol class="al">

<li>

Write the rule as a single expression with `%`, `and` and `or`, and check it for 2024, 2026, 1900 and 2000.

</li>

<li>

Write a script `schaltjahr.py` that makes the same decision with `if`, `elif` and `else`, one condition per line.

</li>

</ol>

:::loesung
(a) The rule is “divisible by 4 and not by 100, or by 400”. Because `and` binds more strongly than `or`, the expression needs no parentheses:

```console
>>> jahr = 2024
>>> jahr % 4 == 0 and jahr % 100 != 0 or jahr % 400 == 0
True
>>> jahr = 2026
>>> jahr % 4 == 0 and jahr % 100 != 0 or jahr % 400 == 0
False
>>> jahr = 1900
>>> jahr % 4 == 0 and jahr % 100 != 0 or jahr % 400 == 0
False
>>> jahr = 2000
>>> jahr % 4 == 0 and jahr % 100 != 0 or jahr % 400 == 0
True
```

(b) With `elif`, you check the strongest rule first, then the exception, then the basic rule:

```python schaltjahr.py
# Leap year in the Gregorian calendar, one condition per line
jahr = int(input("Jahr: "))
if jahr % 400 == 0:
    print(jahr, "ist ein Schaltjahr")
elif jahr % 100 == 0:
    print(jahr, "ist kein Schaltjahr")
elif jahr % 4 == 0:
    print(jahr, "ist ein Schaltjahr")
else:
    print(jahr, "ist kein Schaltjahr")
```

```console Linux
$ python3 schaltjahr.py
Jahr: 1900
1900 ist kein Schaltjahr
$ python3 schaltjahr.py
Jahr: 2000
2000 ist ein Schaltjahr
```

The order is crucial: if `jahr % 4 == 0` came first, 1900 would be a leap year.
:::
:::

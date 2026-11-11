---
title: Variables, command substitution and arithmetic expansion
pfad: Computer Science / Linux and the Command Line / How the Shell Reads a Command Line: Expansion, Quoting, Variables, Environment
adresse: informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung
knoten: Chapter 5: How the Shell Reads a Command Line: Expansion, Quoting, Variables, Environment
order: 6100300
summary: The expansions from Section 1 replace text according to fixed rules.
tags: shell variable, assignment, Parameter expansion, parameter, Command substitution, Arithmetic expansion
lang: en
---

<span class="anker" id="stufe-2"></span>

:::zweck
The expansions from Section [1](expansion-muster-klammern-und-tilde.html#stufe-1) replace text according to fixed rules. This section introduces expansions that insert values: the value of a variable, the output of a command and the result of a calculation.
:::

### The shell variable

<span class="anker" id="stufe-2-1"></span>

Some pieces of information you need in several commands in a row: a long path, a name, a result. Instead of typing them again each time, you would like to remember them under a short name.

As a picture for orientation: a drawer with a label. The label shows the name, and in the drawer lies a note with text. You can exchange the note at any time, and whoever names the name gets the text that is currently inside. Figure [6](#abb-6) shows such a drawer.

:::abbildung linux/k5variable 6
A shell variable as a drawer. The assignment `wohnort=Hamburg` puts the text `Hamburg` into the drawer with the label `wohnort` (German for “place of residence”). In `echo Ich wohne in $wohnort` (“Ich wohne in” is German for “I live in”), the shell replaces `$wohnort` with the contents of the drawer before `echo` starts.
:::

:::definition Definition 2.1 (Shell variable, assignment)
<span class="anker" id="satz-2-1"></span>

A __shell variable__ is a name under which the running shell stores a text, the *value* of the variable. You create a variable or change its value with an __assignment__ of the form `NAME=value`; there is no space before or after the equals sign. The name consists of letters without umlauts or other accents, digits and the underscore, and it does not begin with a digit; uppercase and lowercase letters are different.
:::

If `$NAME` appears in a command line, the shell inserts the value there. The value is always text, even if it looks like a number. If it contains spaces, it needs quotes so that it stays a single word, like a file name with spaces.

::::beispiel Place of residence, greeting and path
```console
$ wohnort=Hamburg
$ echo Ich wohne in $wohnort
Ich wohne in Hamburg
$ gruss="Guten Morgen"
$ echo $gruss
Guten Morgen
$ ordner=~/linuxk5
$ echo $ordner
/home/student/linuxk5
```

An assignment outputs nothing. In the last assignment, the shell replaced the tilde directly after the equals sign; the variable holds the full path. This is the exception to the rule from subsection [1.7](expansion-muster-klammern-und-tilde.html#stufe-1-7): in an assignment, the shell also replaces a tilde directly after the equals sign and after every colon, and bash even does this for an argument that looks like an assignment, such as `echo x=~`.
::::

The space around the equals sign is the most common mistake with variables. Figure [7](#abb-7) shows what the shell makes of the line.

:::abbildung linux/k5zuweisung 7
At the top, `wohnort=Hamburg`: a single word with an equals sign, that is, an assignment. At the bottom, `wohnort = Hamburg`: the shell splits the line at the spaces into three words; the first is the command `wohnort`, the other two are its arguments.
:::

::::beispiel One space too many
```console
$ wohnort = Hamburg
wohnort: command not found
$ echo $?
127
```

The shell looks for a program named `wohnort`, finds none and reports this with exit status 127.
::::

⁠**In short:** A shell variable stores a text under a name; `NAME=value` without spaces stores it.

:::hintergrund Variables in the shell and in Python
If you know variables from Python ([Python, Chapter 2, Section 6.2](/wissen/en/informatik/programmieren/python/werte-typen-und-variablen/variablen-namen-fur-objekte.html#stufe-6-2)), you will recognize the idea: a name for a value. Two differences are important. First, the shell has no types: every value is text, and only a command decides whether it interprets the value as a number. Second, in the shell the space is not decoration but separates words; `x = 5` is an assignment in Python, but in the shell it is the call of a command `x`.
:::

### Parameter expansion: `$NAME` and `${NAME}`

<span class="anker" id="stufe-2-2"></span>

If further text follows the name of a variable directly, such as a digit or an extension, the shell has to decide where the name ends. And what happens if a variable does not exist at all?

:::definition Definition 2.2 (Parameter expansion)
<span class="anker" id="satz-2-2"></span>

__Parameter expansion__ replaces `$NAME` or `${NAME}` with the value of the variable. Without curly braces, the shell takes as many characters for the name as a name can have; with braces, the name ends at the closing brace. If the variable has no value, the shell inserts empty text, without an error message.
:::

In general, anything that stores a value which the shell inserts with a preceding dollar sign is called a __parameter__. Variables are parameters with a name; other parameters carry a number or a special character instead of a name. `$?` from [Chapter 4](/wissen/en/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/stroeme-umleitung-pipes-und-exit-status.html) is a special parameter that the shell sets itself; it is inserted in the same way. The builtin command `unset` removes a variable.

::::beispiel Where the name ends
```console
$ echo Wert: $gibtsnicht Ende
Wert: Ende
$ datei=foto
$ echo $datei1.jpg
.jpg
$ echo ${datei}1.jpg
foto1.jpg
$ unset wohnort
$ echo Wohnort: $wohnort Ende
Wohnort: Ende
```

In `$datei1.jpg`, the `1` still belongs to the name, because digits may occur in names. So the shell looks for a variable `datei1`, finds none and inserts empty text; what remains is `.jpg`. The braces in `${datei}1.jpg` end the name before the `1`. After `unset`, `wohnort` is empty, and here, too, there is no error message.
::::

⁠**In short:** `$NAME` inserts the value of a variable, `${NAME}` marks off the name; an unknown variable yields empty text.

:::hintergrund Default values and lengths
The curly braces can do more than just mark off the name. `${NAME:-default}` inserts the value or, if the variable is empty or missing, the text `default`. `${#NAME}` inserts the number of characters of the value:

```console
$ echo ${wohnort:-unbekannt}
unbekannt
$ wohnort=Hamburg
$ echo ${wohnort:-unbekannt} ${#wohnort}
Hamburg 7
```

There are many more forms, for example for cutting off extensions; the bash manual describes them in the part “Parameter Expansion” (`man bash`).
:::

### Command substitution

<span class="anker" id="stufe-2-3"></span>

Sometimes you do not know a value in advance, but a command can output it: how many files are in the directory, who is logged in, on which day of the week a date falls. You would like to insert this output directly into another command line. Figure [8](#abb-8) shows how the shell does this.

:::abbildung linux/k5befehlsersetzung 8
Command substitution in `echo Angemeldet ist $(whoami)` (“Angemeldet ist” is German for “Logged in is”): first, the shell runs `whoami` in a separate process and captures its standard output `student` together with the line end. The line end at the end is removed, and the rest replaces `$(whoami)`. Only then does `echo` start.
:::

:::definition Definition 2.3 (Command substitution)
<span class="anker" id="satz-2-3"></span>

__Command substitution__ `$(command)` executes the command in the parentheses in a separate process and replaces itself with that command's standard output. In doing so, the shell removes line ends at the end of the output.
:::

::::beispiel User, computer, entries and a day of the week
```console
$ echo Angemeldet ist $(whoami) auf $(hostname)
Angemeldet ist student auf labor
$ anzahl=$(ls | wc -l)
$ echo Im Verzeichnis liegen $anzahl Einträge
Im Verzeichnis liegen 6 Einträge
$ echo Heiligabend 2026 ist ein $(date -d 2026-12-24 +%A)
Heiligabend 2026 ist ein Thursday
```

`whoami` names the user, `hostname` the name of the computer. In the second command line, a whole pipeline even runs inside the command substitution; its result ends up in a variable. Six entries are counted: five files and the directory `urlaub`; `ls` does not show the hidden file. `date -d` computes with the given date instead of today's (“Heiligabend” is German for “Christmas Eve”), and `+%A` asks for the name of the day of the week; because the test system is set to English, it is `Thursday`.
::::

⁠**In short:** `$(command)` inserts the output of a command into the command line, without the line ends at the end.

:::hintergrund The old notation with backquotes
Older guides write command substitution with two backquotes, the grave accent that leans to the left: `` `command` ``.

```console
$ echo `whoami`
student
```

This form still works, but it is considered outdated. It is hard to tell apart from the apostrophe, and with it, nested command substitutions need additional backslashes; with `$(…)`, you simply nest parentheses.
:::

### Arithmetic expansion

<span class="anker" id="stufe-2-4"></span>

For a quick calculation, you do not need to start a program of its own: the shell can calculate with integers itself. This, too, is an expansion: the shell inserts the result of the calculation into the line.

:::definition Definition 2.4 (Arithmetic expansion)
<span class="anker" id="satz-2-4"></span>

__Arithmetic expansion__ `$((expression))` computes the expression in the double parentheses with integers and inserts the result as text. Allowed are, among others, `+`, `-`, `*` (times), `/` (divided by), `%` (remainder of the division), `**` (to the power of) and parentheses; multiplication and division come before addition and subtraction. `/` drops the remainder. In the expression, you refer to variables by their name; a `$` is not needed there.
:::

A `*` inside `$((…))` is not a pattern but the multiplication sign. Spaces are allowed in the expression.

::::beispiel A purchase in cents
Three rolls at 45 cents each and two liters of milk at 119 cents each: how much does that cost in euros and cents? Because the shell knows only integers, you calculate in cents:

```console
$ echo $((3 * 45))
135
$ summe=$((3*45 + 2*119))
$ echo $summe
373
$ echo $((summe / 100)) Euro und $((summe % 100)) Cent
3 Euro und 73 Cent
```

Figure [9](#abb-9) checks the calculation step by step. In `summe / 100`, there is no `$` before the name; the shell looks it up in the expression itself.

:::abbildung linux/k5rechnung 9
The calculation of the purchase: $3 \cdot 45 + 2 \cdot 119 = 135 + 238 = 373$ cents. Whole-number division by 100 gives 3 euros, and the remainder is 73 cents; as a check, $3 \cdot 100 + 73 = 373$.
:::
::::

::::beispiel [Second example] Dividing without a decimal point
```console
$ echo $((7 / 2)) $((7 % 2)) $((-7 / 2))
3 1 -3
$ echo $((2 ** 10))
1024
$ echo $(( (3 + 4) * 2 )) $(( 3 + 4 * 2 ))
14 11
```

$7/2$ would be 3.5; the shell cuts off the digits after the decimal point and returns 3, and the remainder is 1. With $-7/2$, it likewise cuts off; the result is $-3$, not $-4$. The parentheses change the order of the calculation, as at school.
::::

⁠**In short:** `$((…))` calculates with integers and inserts the result; `/` drops the remainder, `%` returns it.

:::hintergrund Why only integers, and how large?
The shell calculates with integers of fixed size, as the processor handles them directly; the standard for Unix shells requires signed integers for this. It does not know numbers with decimal places, it reports a division by zero as an error, and on the test system the numbers have 64 bits. The largest is $2^{63} - 1$; one more, and the result jumps into the negative without warning:

```console
$ echo $((7 / 2.5))
bash: 7 / 2.5: arithmetic syntax error: invalid arithmetic operator (error token is ".5")
$ echo $((1 / 0))
bash: 1 / 0: division by 0 (error token is "0")
$ echo $((2 ** 63 - 1)) $((2 ** 63))
9223372036854775807 -9223372036854775808
```

For numbers with decimal places, you use a different tool, such as Python ([Python, Chapter 2](/wissen/en/informatik/programmieren/python/werte-typen-und-variablen/werte-typen-und-variablen.html)). For the shell itself, integers are usually enough: it counts files, lines and repetitions.
:::

### Exercises for Section [2](#stufe-2)

<span class="anker" id="stufe-2-5"></span>

:::aufgabe Exercise 5 ★ A name with an extension
<span class="anker" id="aufg-5"></span>

(a) Create the variables `vorname` (German for “first name”) with the value `Lea` and `nachname` (“last name”) with the value `Berg`, and have `echo` write the sentence `Hallo, Lea Berg`. (b) Predict what `echo $vorname_notizen.txt` outputs, and explain it. (c) With `touch`, create an empty file whose name consists of the first name and the ending `_notizen.txt`, that is, `Lea_notizen.txt`, without writing out the first name.

:::loesung
```console
$ vorname=Lea
$ nachname=Berg
$ echo Hallo, $vorname $nachname
Hallo, Lea Berg
$ echo $vorname_notizen.txt
.txt
$ touch ${vorname}_notizen.txt
$ ls *notizen*
Lea_notizen.txt
```

(a) Two assignments without spaces around the equals sign; then the shell inserts the two values for `echo`. (b) The underscore may appear in names, so the shell looks for a variable `vorname_notizen`. There is no such variable; it becomes empty text, and what remains is `.txt`. (c) The curly braces end the name before the underscore: `${vorname}_notizen.txt` yields `Lea_notizen.txt`.
:::
:::

:::aufgabe Exercise 6 ★ Three wrong assignments
<span class="anker" id="aufg-6"></span>

The variable `wohnort` has the value `Hamburg`. Someone wants to change it to `Köln` and tries three lines: (a) `wohnort = Köln` (b) `Wohnort=Köln` (c) `$wohnort=Köln`. For each one, predict whether the shell looks for a program and under which name, and check it. What value does `wohnort` have afterward?

:::loesung
```console
$ wohnort=Hamburg
$ wohnort = Köln
wohnort: command not found
$ Wohnort=Köln
$ $wohnort=Köln
Hamburg=Köln: command not found
$ echo $wohnort $Wohnort
Hamburg Köln
```

(a) Three words; the first one, `wohnort`, is the command. (b) A single word with an equals sign and a valid name in front of it, so it is an assignment; the shell does not look for a program and reports nothing. But because uppercase and lowercase letters are different, a new variable `Wohnort` comes into being, and `wohnort` remains untouched. (c) `$wohnort` is first replaced with `Hamburg`. After that, the word `Hamburg=Köln` is not an assignment, because the shell decides whether a word is an assignment as early as when it splits the line, when the word still read `$wohnort=Köln`; and a name does not begin with `$`. So it is a command name. In all three cases, `wohnort` keeps the value `Hamburg`; the last line shows both variables. The correct line would be `wohnort=Köln`.
:::
:::

:::aufgabe Exercise 7 ★★ Calculating with integers
<span class="anker" id="aufg-7"></span>

(a) A trip takes 437 minutes. Have the shell output how many hours and minutes that is. (b) Three grades are 2, 3 and 2. What does `echo $(( (2 + 3 + 2) / 3 ))` return, and how far is that from the true average? (c) Why does `$((10 / 3 * 3))` not give the same result as `$((10 * 3 / 3))`?

:::loesung
```console
$ echo $((437 / 60)) Stunden und $((437 % 60)) Minuten
7 Stunden und 17 Minuten
$ echo $(( (2 + 3 + 2) / 3 ))
2
$ echo $((10 / 3 * 3)) $((10 * 3 / 3))
9 10
```

(a) An hour has 60 minutes (`Stunden` and `Minuten` in the output are German for “hours” and “minutes”). The whole-number division $437 / 60$ yields the full hours, 7; the remainder $437 - 7 \cdot 60 = 17$ gives the minutes. (b) The sum is 7, and $7/3 = 2.33\ldots$; the shell drops the remainder and returns 2. The error is one third. If you want a more precise result, calculate in smaller units, for example in hundredths: `$(( (2 + 3 + 2) * 100 / 3 ))` yields 233, that is, 2.33. (c) The shell evaluates operators of equal precedence from left to right. On the left, the division comes first: $10/3 = 3$, the remainder is lost, and $3 \cdot 3 = 9$. On the right, the multiplication comes first: $10 \cdot 3 = 30$ and $30/3 = 10$. With integers, you should therefore divide as late as possible.
:::
:::

:::aufgabe Exercise 8 ★★ Values from commands
<span class="anker" id="aufg-8"></span>

(a) Store the number of files with the extension `.jpg` in your practice directory in a variable `anzahl`, and have a sentence such as `Es gibt 3 Fotos` (German for “There are 3 photos”) output. (b) With a single line, have the shell output on which day of the week 17 May 2027 falls.

:::loesung
```console
$ anzahl=$(ls *.jpg | wc -l)
$ echo Es gibt $anzahl Fotos
Es gibt 3 Fotos
$ echo Der 17. Mai 2027 ist ein $(date -d 2027-05-17 +%A)
Der 17. Mai 2027 ist ein Monday
```

(a) Pathname expansion gives `ls` the three photos; `ls` writes them into the pipe one per line, `wc -l` counts three lines, and command substitution stores the number in the variable. (b) `date -d` works with the given day, and `+%A` asks for the day of the week (“Der 17. Mai 2027 ist ein” is German for “May 17, 2027 is a”). On a system set to German it would be `Montag`.
:::
:::

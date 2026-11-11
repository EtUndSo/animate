---
title: Regular expressions: characters, classes and anchors
pfad: Computer Science / Linux and the Command Line / Text Tools and Regular Expressions
adresse: informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke
knoten: Chapter 6: Text Tools and Regular Expressions
order: 6110700
summary: So far, grep has searched for fixed words.
tags: string, regular expression, match, dot, bracket expression, character class, anchor
lang: en
---

<span class="anker" id="stufe-6"></span>

:::zweck
So far, `grep` has searched for fixed words. But many questions concern a form: a date from a particular week, a time under 30 minutes, a number with a decimal point. This section introduces the notation used to describe such forms, and its first building blocks: any single character, a selection of characters and the positions at the beginning and at the end of a line.
:::

### The regular expression

<span class="anker" id="stufe-6-1"></span>

How do you find all runs that took longer than 99 minutes? There is no fixed search text for this; `128` is only one of 900 three-digit numbers. What is needed is a description such as “a comma, then three digits, then the line end”, and a tool that compares every line with this description. A __string__ here is simply a sequence of characters, such as a word, a number or a whole line.

:::definition Definition 6.1 (Regular expression, match)
<span class="anker" id="satz-6-1"></span>

A __regular expression__ is a text that describes a set of strings. It consists of ordinary characters, which stand for themselves, and of special characters with a meaning of their own. A line matches a regular expression if a contiguous piece of it belongs to this set; this piece is called the __match__.
:::

The search text of `grep` has always been a regular expression; so far, it consisted only of ordinary characters. The name “regular expression” is often shortened to “regex”.

::::beispiel An expression without special characters
The expression `Clara` contains only ordinary characters. It describes a set with exactly one string, `Clara`. The line `2026-11-03,Clara,7.2,41` matches, because its piece from position 12 to 16 is exactly this string; that is the match. This is exactly how `grep Clara laeufe.csv` worked in subsection [5.1](suchen-mit-grep.html#stufe-5-1).
::::

Many special characters of regular expressions also mean something to the shell: `*`, `?`, `[`, `$`, `\`, `|`, parentheses. But the shell is supposed to pass the expression on to the program unchanged. According to the rule from [Chapter 5, Section 3.8](/wissen/en/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/worttrennung-und-quoting.html#stufe-3-8), text that a program is to receive unchanged belongs in single quotes. From now on, every regular expression with special characters in this chapter therefore stands between `'` and `'`; for a simple word such as `Clara`, this is not necessary, but it does no harm.

⁠**In short:** A regular expression describes a set of strings; a line matches if a piece of it belongs to the set, and on the command line the expression stands in single quotes.

### The dot: any single character

<span class="anker" id="stufe-6-2"></span>

The simplest special character leaves a position open: “any character here”. Figure [18](#abb-18) shows which set this creates and which lines match.

:::abbildung linux/k6menge 18
On the left the expression `5.0`, on the right the set it describes: all strings of three characters that begin with 5 and end with 0, among them `5.0`, `5x0`, `520` and `5,0`. Below, four lines. In `5.0`, `5x0` and `520`, a piece that belongs to the set lights up; `50` has no such piece and stays gray.
:::

:::definition Definition 6.2 (Dot)
<span class="anker" id="satz-6-2"></span>

The __dot__ `.` in a regular expression matches any single character.
:::

So the dot always stands for exactly one position, not for none and not for several.

::::beispiel The dot in a number
```console
$ printf '%s\n' 5.0 5x0 520 50 | grep '5.0'
5.0
5x0
520
```

Perhaps the number 5.0 was meant, but `5x0` and `520` are found as well: the dot matches every character between 5 and 0. `50` does not match, because a character is missing between 5 and 0.
::::

⁠**In short:** A dot matches any single character.

### Taking special characters literally: the backslash and grep -F

<span class="anker" id="stufe-6-3"></span>

In the running log, the decimal numbers are written with a dot. Anyone searching for `5.0` usually really wants a dot and not just any character. So there has to be a way to take away a special character's meaning.

:::definition Definition 6.3 (Backslash in the expression, grep -F)
<span class="anker" id="satz-6-3"></span>

A backslash `\` before a special character turns it into an ordinary character in a regular expression: `\.` matches only a dot. With the option `-F`, `grep` takes the whole search text as a fixed string in which no character has a special meaning.
:::

Between single quotes, the shell leaves the backslash where it is ([Chapter 5, Section 3.4](/wissen/en/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/worttrennung-und-quoting.html#stufe-3-4)); so it reaches `grep`.

::::beispiel Only the real dot
```console
$ printf '%s\n' 5.0 5x0 520 50 | grep '5\.0'
5.0
$ printf '%s\n' 5.0 5x0 520 50 | grep -F '5.0'
5.0
```

Both ways now find only the line with the dot.
::::

⁠**In short:** `\` before a special character makes it ordinary; `grep -F` takes the whole search text literally.

:::hintergrund Why a forgotten backslash rarely stands out
A dot without a backslash also matches a dot. All the lines you wanted to find are therefore still found, and the mistake shows only in additional matches that are easy to overlook: a search for `bericht.txt` also finds `berichtXtxt`. This is a consequence of an expression describing a set: without the backslash, the set is larger, but it still contains the intended string. If you are looking for a fixed text that contains dots or other special characters, such as a file name, it is therefore best to use `grep -F` right away.
:::

### A selection of characters: the bracket expression

<span class="anker" id="stufe-6-4"></span>

The dot allows every character. Often, however, only a particular selection should be allowed at a position, such as only the days 2, 3 or 4. Figure [19](#abb-19) shows how a square bracket describes such a selection for a single position.

:::abbildung linux/k6klammer 19
The expression `2026-11-0[2-4]` above the date `2026-11-03`. All characters up to the last position must match exactly; the last position is a box with the allowed characters 2, 3 and 4. The 3 fits into it and lights up. With the date `2026-11-07`, the 7 does not fit into the box.
:::

:::definition Definition 6.4 (Bracket expression)
<span class="anker" id="satz-6-4"></span>

A __bracket expression__ is a list of characters in square brackets; it matches exactly one character that is in the list. Two characters with a hyphen between them stand for all characters from the one to the other, such as `[0-9]` for a digit. If a `^` comes directly after the opening bracket, the expression matches exactly one character that is not in the list.
:::

Inside the brackets, the dot, the star, the dollar sign and the backslash are ordinary characters; `[.]` matches only a dot. A hyphen counts as an ordinary character if it comes first or last in the list, a closing square bracket if it comes first: `[]-]` matches `]` or `-`. The file name patterns from [Chapter 3, Section 6.6](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/kopieren-verschieben-loschen.html#stufe-6-6) know the same brackets; there, however, negation uses `!`, here `^`.

::::beispiel Three days, two people, no dot
```console
$ grep '2026-11-0[2-4]' laeufe.csv
2026-11-02,Anna,5.0,28
2026-11-02,Ben,10.5,62
2026-11-03,Clara,7.2,41
2026-11-04,Anna,6.4,35
$ grep -c ',[AB]' laeufe.csv
7
$ printf '%s\n' 5.0 5x0 520 | grep '5[^.]0'
5x0
520
```

The runs from 2 to 4 November; seven lines in which a comma is followed by an A or a B, that is, the runs of Anna and Ben; and all lines in which something other than a dot stands between 5 and 0.
::::

⁠**In short:** `[…]` matches exactly one character from the list, `[^…]` exactly one that is not in it; `a-z` in the list is a range.

:::hintergrund Why ranges call for caution
What “all characters from a to z” are depends on the order of the characters, that is, on the locale from subsection [3.4](sortieren-und-zahlen-sort-und-uniq.html#stufe-3-4). In the locales `C` and `C.UTF-8`, the order is that of the character numbers, and `[a-z]` means exactly the 26 lowercase letters without umlauts. The standard for Unix shells and their tools defines ranges only for the locale `C` and leaves their meaning open in all others. On older systems with dictionary order, uppercase and lowercase letters alternated, a, A, b, B, and `[A-Z]` then also included almost all lowercase letters. For digits, a range is harmless; for letters, there is a safer notation with names instead of ranges.
:::

### Character classes: [[:digit:]] and its relatives

<span class="anker" id="stufe-6-5"></span>

“Any letter” is more than a to z: there are uppercase letters, umlauts and letters of other languages. Instead of listing them, you give the selection a name. Figure [20](#abb-20) applies three such names to a line.

:::abbildung linux/k6klassen 20
The line `2026-11-03,Clara,7.2,41` character by character. One after another, the characters light up that belong to `[[:digit:]]` (all digits), to `[[:alpha:]]` (the letters of `Clara`) and to `[[:punct:]]` (hyphens, commas and the dot). Each character belongs to exactly one of the three classes.
:::

:::definition Definition 6.5 (Character class)
<span class="anker" id="satz-6-5"></span>

A __character class__ is a named group of characters that you write inside a bracket expression as `[:name:]`. Important names are `digit` for digits, `alpha` for letters, `upper` and `lower` for uppercase and lowercase letters, `alnum` for letters and digits, `space` for the space and related characters such as tab, newline and carriage return, `blank` only for space and tab, and `punct` for punctuation marks. Which characters belong to a class is determined by the locale.
:::

The inner brackets belong to the name, the outer ones to the bracket expression. A single digit is therefore written `[[:digit:]]` with double brackets; with `[[:digit:].]`, the expression matches a digit or a dot.

::::beispiel Lines with and without digits
```console
$ grep -c '[[:digit:]]' laeufe.csv
9
$ grep -v '[[:digit:]]' laeufe.csv
datum,name,km,minuten
```

Nine lines contain a digit, the header line none.
::::

::::beispiel [Second example] Is ä a letter?
```console
$ echo 'ä' | grep -c '[[:alpha:]]'
1
$ echo 'ä' | LC_ALL=C grep -c '[[:alpha:]]'
0
```

Under `C.UTF-8`, the two bytes of the ä are one character and a letter. Under `C`, every byte is a character of its own, and neither of the two is a letter. This shows that the locale even determines what a character is.
::::

⁠**In short:** `[[:digit:]]`, `[[:alpha:]]` and their relatives select characters by kind; the locale determines what belongs to them.

### Start and end of the line: the anchors

<span class="anker" id="stufe-6-6"></span>

`grep ',2[0-9]'` is supposed to find the runs under 30 minutes, that is, those with a time between 20 and 29. But the piece `,2` followed by a digit also occurs in `,21.1`, the distance of Ben's half marathon. What is meant is “at the end of the line”. Figure [21](#abb-21) shows how an expression can require a position in the line.

:::abbildung linux/k6anker 21
The line `2026-11-08,Ben,21.1,128` as a sequence of characters. Between the characters lie positions, drawn as vertical strokes. The stroke before the first character is the position of `^`, the one after the last is that of `$`. The expression `,2[0-9]` finds a match at `,21`; with `$` after it, the match would have to end directly before the last stroke, and it does not.
:::

:::definition Definition 6.6 (Anchor)
<span class="anker" id="satz-6-6"></span>

An __anchor__ matches not a character but a position in the line. `^` at the beginning of an expression matches the position before the first character of the line, `$` at the end of an expression the position after the last character, directly before the line end.
:::

So `^d` matches only lines that begin with d, `,28$` only lines that end with `,28`, and `^$` only empty lines. The word comes from the picture of an anchor that fastens the expression to one end of the line.

::::beispiel Header line, short runs, empty lines
```console
$ grep '^d' laeufe.csv
datum,name,km,minuten
$ grep ',2[0-9]' laeufe.csv
2026-11-02,Anna,5.0,28
2026-11-08,Ben,21.1,128
2026-11-09,Anna,5.0,27
$ grep ',2[0-9]$' laeufe.csv
2026-11-02,Anna,5.0,28
2026-11-09,Anna,5.0,27
$ grep -c '^$' laeufe.csv
0
```

Without `$`, Ben's half marathon slips through; with `$`, the two runs under 30 minutes remain. The file has no empty lines.
::::

::::beispiel [Second example] The anchor and the Windows line end
```console
$ grep -c ',28$' laeufe.csv windows.csv
laeufe.csv:1
windows.csv:0
```

Both files contain the line with `,28`. In `windows.csv`, however, the carriage return from subsection [1.4](textdaten-datensatze-felder-und-zeilenenden.html#stufe-1-4) still stands between `28` and the line end. The last character of the line is therefore not an `8`, and with `$` the expression finds no match. After `tr -d '\r'` from subsection [2.2](spalten-ausschneiden-und-zeichen-ersetzen-cut-tr-und-paste.html#stufe-2-2), the line would have been found.
::::

⁠**In short:** `^` anchors an expression at the start of the line, `$` at the end of the line; both match positions, not characters.

### Exercises for Section [6](#stufe-6)

<span class="anker" id="stufe-6-7"></span>

:::aufgabe Exercise 15 ★ A date range, a duration
<span class="anker" id="aufg-15"></span>

(a) Output all runs from 5 to 9 November. (b) Output all runs that took between 40 and 49 minutes.

:::loesung
```console
$ grep '^2026-11-0[5-9]' laeufe.csv
2026-11-05,Ben,5.0,31
2026-11-06,Anna,12.0,70
2026-11-07,Clara,8.0,44
2026-11-08,Ben,21.1,128
2026-11-09,Anna,5.0,27
$ grep ',4[0-9]$' laeufe.csv
2026-11-03,Clara,7.2,41
2026-11-07,Clara,8.0,44
```

(a) The bracket expression `[5-9]` allows the digits 5 to 9 for the last position of the day; the anchor makes sure that the date is at the start of the line. (b) A comma, a 4, any digit and then the end of the line: the time in the last field lies between 40 and 49. Without `$`, a distance such as `,42.0` would also match, if there were one.
:::
:::

:::aufgabe Exercise 16 ★★ The dot
<span class="anker" id="aufg-16"></span>

You are looking for runs of exactly 1.0 km. (a) Predict what `grep -c '1.0' laeufe.csv` reports, and explain the result. (b) Write two commands that search correctly, one with a regular expression and one with `-F`.

:::loesung
```console
$ grep -c '1.0' laeufe.csv
9
$ grep '1.0' laeufe.csv | head -n 1
2026-11-02,Anna,5.0,28
$ grep -c ',1\.0,' laeufe.csv
0
$ grep -cF ',1.0,' laeufe.csv
0
```

(a) All nine runs match, although none of them was 1.0 km long. The dot matches any single character, and the date contains `11-0`: a 1, a hyphen, a 0. (b) With `\.`, the expression means only the dot; with `-F`, the whole search text is literal. The commas before and after it make sure that exactly the field is meant; without them, a distance such as `11.0` would also match, for example. The result in both cases: no run of exactly 1.0 km.
:::
:::

:::aufgabe Exercise 17 ★★ Anchor and Windows file
<span class="anker" id="aufg-17"></span>

(a) Using `grep -c ',62$'`, count the matches in `laeufe.csv` and in `windows.csv` with a single command. (b) Explain the difference. (c) Count correctly in `windows.csv` without creating a new file.

:::loesung
```console
$ grep -c ',62$' laeufe.csv windows.csv
laeufe.csv:1
windows.csv:0
$ tr -d '\r' < windows.csv | grep -c ',62$'
1
```

(a) With two files, `grep -c` counts for each one separately. (b) In `windows.csv`, the carriage return stands between `62` and the line end; the last character of the line is not a `2`, and `$` matches only after the carriage return. (c) `tr` removes the carriage returns in the stream, and `grep`, without a file name, receives the cleaned-up lines through the pipe; no new file is created.
:::
:::

---
title: Cutting out columns and replacing characters: cut, tr and paste
pfad: Computer Science / Linux and the Command Line / Text Tools and Regular Expressions
adresse: informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke
knoten: Chapter 6: Text Tools and Regular Expressions
order: 6110300
summary: Many questions concern only one column: Who ran, and how far?
tags: cut, tr, paste
lang: en
---

<span class="anker" id="stufe-2"></span>

:::zweck
Many questions concern only one column: Who ran, and how far? This section shows a tool that cuts out columns, one that replaces or deletes individual characters, and one that puts columns side by side again. With them, you can also remove the Windows line ends from Section [1](textdaten-datensatze-felder-und-zeilenenden.html#stufe-1) and add up a column of numbers.
:::

### Cutting out columns: cut

<span class="anker" id="stufe-2-1"></span>

To see who ran, you only need field 2 of each line. Figure [5](#abb-5) shows how a tool cuts a column out of all records at once.

:::abbildung linux/k6cut 5
The running log as a block of lines. `cut -d, -f2` splits each line into fields at the commas; the fields number 2 light up and move out to the right as a narrow column: `name`, `Anna`, `Ben`, `Clara` and so on. The rest of each line stays behind in gray.
:::

:::definition Definition 2.1 (cut)
<span class="anker" id="satz-2-1"></span>

The command __cut__ writes out only selected parts of each line of its input. With `-d` and a character, you set the separator; with `-f` and a list, the fields that are kept. The list consists of numbers and ranges, separated by commas: `2`, `1,3`, `2-4`, `2-` for “from field 2 on”. Without `-d`, the tab is the separator.
:::

`cut` reads the files given as arguments, otherwise its standard input; so it is a filter. `-d,` is the contracted form of `-d ,`, as with every short option with a value ([Chapter 2, Section 2.6](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/der-aufbau-einer-befehlszeile.html#stufe-2-6)).

::::beispiel Names, date and distance
```console
$ cut -d, -f2 laeufe.csv
name
Anna
Ben
Clara
Anna
Ben
Anna
Clara
Ben
Anna
```

Field 2 of each line, including the header line. Several fields and ranges work the same way; `cut` writes them with the separator in between:

```console
$ cut -d, -f1,3 laeufe.csv | head -n 3
datum,km
2026-11-02,5.0
2026-11-02,10.5
$ cut -d, -f2- laeufe.csv | head -n 2
name,km,minuten
Anna,5.0,28
```
::::

Instead of fields, `cut` can also cut out character positions in the line: `-c` with a list of positions, counted from the left starting at 1. This suits values of fixed width such as the date, where the day is always at positions 9 and 10:

```console
$ tail -n 3 laeufe.csv | cut -c9-10
07
08
09
```

::::beispiel [Counterexample] The forgotten separator
Without `-d,`, `cut` looks for tabs. It outputs a line that contains no separator at all unchanged:

```console
$ cut -f2 laeufe.csv | head -n 2
datum,name,km,minuten
2026-11-02,Anna,5.0,28
```

Instead of the names, whole lines come out, without an error message. If you would rather leave out such lines, add `-s`.
::::

⁠**In short:** `cut -d, -f2` cuts the second comma-separated field out of each line; `-c` cuts by character positions.

:::hintergrund On the test system, character positions are bytes
With an umlaut, you can see what `cut -c` really counts:

```console
$ echo 'Jürgen,7' | cut -c1-3
Jü
$ echo 'Jürgen,7' | gnucut -c1-3
Jü
```

Three characters were wanted, `Jür`; three bytes were delivered, because the ü takes up two ([Chapter 3, Section 4.1](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-ansehen.html#stufe-4-1)). Both implementations on the test system, uutils 0.8 and GNU 9.7, count this way. The GNU implementation has counted real characters only since version 9.11 from 2026; in older versions, positions are bytes. For text with umlauts or other accented letters, it is therefore safer to cut by fields than by positions. A second limit of `cut`: it always writes the fields in their original order; `-f3,1` gives the same as `-f1,3`.
:::

### Replacing and deleting characters: tr

<span class="anker" id="stufe-2-2"></span>

Sometimes a single character gets in the way everywhere in a file: a carriage return at the end of every line, commas where another program expects semicolons, lowercase letters where uppercase letters are wanted. [Chapter 4, Section 3.3](/wissen/en/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/eingaben-umleiten.html#stufe-3-3) already used `tr` to turn lowercase letters into uppercase letters. Figure [6](#abb-6) shows the rule by which it does this.

:::abbildung linux/k6tr 6
`tr a-z A-Z` as a mapping: at the top, the characters of the first set `a b c … z` side by side, below them those of the second set `A B C … Z`; arrows connect the characters at the same position. A text runs through character by character: each character that occurs at the top is replaced by its counterpart at the bottom; digits and commas pass through unchanged.
:::

:::definition Definition 2.2 (tr)
<span class="anker" id="satz-2-2"></span>

The command __tr__ reads its standard input character by character and writes it out changed. `tr set1 set2` replaces each character that stands at a certain position in the first set with the character at the same position in the second set. `tr -d set` deletes all characters of the set; `tr -s set` squeezes several identical characters of the set in a row into one.
:::

You write a set as a sequence of characters, such as `',;'`, with ranges such as `a-z` or with names such as `[:lower:]` for all lowercase letters and `[:digit:]` for all digits. `tr` itself understands the notations `\n` for the newline, `\t` for the tab and `\r` for the carriage return. So that the shell changes none of this, the sets are enclosed in single quotes.

::::beispiel Replacing, squeezing, deleting
```console
$ head -n 2 laeufe.csv | tr ',' ';'
datum;name;km;minuten
2026-11-02;Anna;5.0;28
$ head -n 2 laeufe.csv | tr a-z A-Z
DATUM,NAME,KM,MINUTEN
2026-11-02,ANNA,5.0,28
$ echo 'viel    Platz' | tr -s ' '
viel Platz
$ echo Hallo | tr -d l
Hao
```

Digits, dots and hyphens occur in no set and stay as they are.
::::

`tr` does not accept file names; the file comes in with `<` or through a pipe. A file name as a third argument leads to a message:

```console
$ tr a-z A-Z laeufe.csv
tr: extra operand 'laeufe.csv'
Try 'tr --help' for more information.
```

With `-d`, `tr` also solves the problem from subsection [1.4](textdaten-datensatze-felder-und-zeilenenden.html#stufe-1-4): it deletes every carriage return from the Windows file. You compare the result with `cmp`, which compares two files byte by byte, outputs nothing if they are the same and reports exit status 0:

```console
$ tr -d '\r' < windows.csv > linux.csv
$ cat -A linux.csv
datum,name,km,minuten$
2026-11-02,Anna,5.0,28$
2026-11-02,Ben,10.5,62$
$ cmp linux.csv drei.csv && echo gleich
gleich
```

`gleich` is German for “equal”: the cleaned-up file `linux.csv` is byte for byte the same as the first three lines of the running log.

⁠**In short:** `tr` replaces characters according to two sets, deletes them with `-d` or squeezes repetitions with `-s`; `tr -d '\r'` removes Windows line ends.

:::hintergrund Why tr does not convert umlauts
```console
$ echo 'Anna läuft' | tr a-z A-Z
ANNA LäUFT
$ echo 'Anna läuft' | tr '[:lower:]' '[:upper:]'
ANNA LäUFT
```

The ä stays lowercase, even with the names of the sets. On the test system, `tr` works byte by byte, in the uutils implementation as well as in the GNU implementation, whose manual states this explicitly. In UTF-8, an ä consists of two bytes that are not letters on their own, so `tr` finds nothing in them to replace. For the digits, commas and ASCII letters that this chapter is mostly about, this does not matter. Incidentally, the sets of `tr` are not patterns like those for file names from [Chapter 3, Section 6.6](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/kopieren-verschieben-loschen.html#stufe-6-6): a star or a question mark in them stands for itself; only the hyphen between two characters, the backslash as in `\n` and the names in `[:…:]` have a special meaning.
:::

### Joining columns: paste

<span class="anker" id="stufe-2-3"></span>

`cut` takes a table apart into columns. Sometimes you need the opposite: putting two lists that belong together line by line side by side to form a table. Figure [7](#abb-7) shows this.

:::abbildung linux/k6paste 7
Two narrow columns, on the left the names from `namen.txt`, on the right the minutes from `minuten.txt`. `paste` pushes them together: the first line on the left and the first on the right become one line with a tab in between, then the second lines and so on. Below that, `paste -s`: a single column is turned into one line.
:::

:::definition Definition 2.3 (paste)
<span class="anker" id="satz-2-3"></span>

The command __paste__ reads several files at the same time and writes the first line of each file side by side in one line, then the second lines and so on. Between the parts, it puts a tab or, with `-d`, another character. With `-s`, it instead puts all lines of a file one after the other in a single line.
:::

First save the two columns in files of their own with `cut`:

```console
$ cut -d, -f2 laeufe.csv > namen.txt
$ cut -d, -f4 laeufe.csv > minuten.txt
$ paste namen.txt minuten.txt | head -n 3
name    minuten
Anna    28
Ben     62
$ paste -d, namen.txt minuten.txt | head -n 3
name,minuten
Anna,28
Ben,62
```

In the terminal, the tab appears as a jump to the next column. With `-d,`, the result is CSV again.

::::beispiel A column as a line
`paste -s` reads its standard input when it gets no file name:

```console
$ tail -n +2 namen.txt | paste -s -d,
Anna,Ben,Clara,Anna,Ben,Anna,Clara,Ben,Anna
```

The nine names are now in one line, separated by commas.
::::

::::beispiel Adding up the minutes
How long was the running club out in total? If you put a plus sign between the minutes, you get a calculation that the shell's arithmetic from [Chapter 5, Section 2.4](/wissen/en/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/variablen-befehlsersetzung-und-arithmetik.html#stufe-2-4) can work out:

```console
$ tail -n +2 minuten.txt | paste -s -d+
28+62+41+35+31+70+44+128+27
$ echo $(( $(tail -n +2 minuten.txt | paste -s -d+) ))
466
```

The command substitution puts the calculation between the double parentheses, and the shell calculates. Figure [8](#abb-8) adds up the nine values step by step: in total, it was 466 minutes, that is, 7 hours and 46 minutes. This approach does not work for decimal numbers such as the kilometers, because the shell calculates only with whole numbers.

:::abbildung linux/k6minuten 8
The sum of the minutes: $28 + 62 + 41 + 35 + 31 + 70 + 44 + 128 + 27$. The running totals keep pace from left to right: 90, 131, 166, 197, 267, 311, 439 and finally 466.
:::
::::

⁠**In short:** `paste` puts lines of several files side by side, `paste -s` puts all lines of a file into one line, with `-d` setting the separator.

### Exercises for Section [2](#stufe-2)

<span class="anker" id="stufe-2-4"></span>

:::aufgabe Exercise 4 ★ Cutting out columns
<span class="anker" id="aufg-4"></span>

(a) Output the date and the minutes of all runs without the header line. (b) Output only the day of the month of all runs in one line, once with `cut -c` and once with fields only. (c) Predict what `cut -d, -f5 laeufe.csv` outputs, and check it with `cat -A`.

:::loesung
```console
$ tail -n +2 laeufe.csv | cut -d, -f1,4 | head -n 3
2026-11-02,28
2026-11-02,62
2026-11-03,41
$ tail -n +2 laeufe.csv | cut -c9-10 | paste -s -d' '
02 02 03 04 05 06 07 08 09
$ tail -n +2 laeufe.csv | cut -d, -f1 | cut -d- -f3 | paste -s -d' '
02 02 03 04 05 06 07 08 09
$ cut -d, -f5 laeufe.csv | head -n 2 | cat -A
$
$
```

(a) `tail -n +2` removes the header line, and `cut -d, -f1,4` keeps the date and the minutes; `head -n 3` only shortens the output here, and without it nine lines appear. (b) The day is at character positions 9 and 10 of the date. Without character positions, you first cut out the date as field 1 and then split it a second time, this time at the hyphen; there, the day is field 3. `paste -s -d' '` puts the days into one line. (c) The lines have only four fields. For a fifth, `cut` writes nothing, only the line end; `cat -A` therefore shows lines that consist of nothing but `$`.
:::
:::

:::aufgabe Exercise 5 ★★ Cleaning up a Windows file
<span class="anker" id="aufg-5"></span>

Clean up `gruss.txt` from Exercise [2](textdaten-datensatze-felder-und-zeilenenden.html#aufg-2). (a) Write the result to `gruss_linux.txt` and check it with `wc -c` and `cat -A`. (b) Why must you not write `tr -d '\r' < gruss.txt > gruss.txt`? Try it on a copy. (c) How do you still get the cleaned-up version under the old name?

:::loesung
```console
$ tr -d '\r' < gruss.txt > gruss_linux.txt
$ wc -c gruss_linux.txt
11 gruss_linux.txt
$ cat -A gruss_linux.txt
Hallo$
Welt$
```

(a) Two carriage returns fewer, that is, $13 - 2 = 11$ bytes, and `cat -A` no longer shows any `^M`. (b) This is the truncation trap from [Chapter 4, Section 2.7](/wissen/en/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/ausgaben-umleiten.html#stufe-2-7): the shell empties the file for the redirection before `tr` starts, and `tr` then reads an empty file.

```console
$ cp gruss.txt kopie.txt
$ tr -d '\r' < kopie.txt > kopie.txt
$ wc -c kopie.txt
0 kopie.txt
$ tr -d '\r' < gruss.txt > zwischen.txt && mv zwischen.txt gruss.txt
$ cat -A gruss.txt
Hallo$
Welt$
```

(c) You write to an intermediate file and rename it afterward. The `&&` ensures that `mv` runs only if `tr` succeeded; otherwise, the old file would remain untouched.
:::
:::

:::aufgabe Exercise 6 ★★ Reassembling the table
<span class="anker" id="aufg-6"></span>

You want a CSV file with the columns distance and name, in this order. (a) Why does this not work with `cut -d, -f3,2 laeufe.csv`? (b) Build it with `cut` and `paste`.

:::loesung
```console
$ cut -d, -f3,2 laeufe.csv | head -n 2
name,km
Anna,5.0
$ cut -d, -f3 laeufe.csv > km.txt
$ paste -d, km.txt namen.txt | head -n 3
km,name
5.0,Anna
10.5,Ben
```

(a) `cut` always writes the selected fields in the order in which they appear in the line; for `cut`, `3,2` is the same selection as `2,3`. (b) First put the distances into a file of their own, then place them side by side with `paste` in the desired order, `km.txt` first. `namen.txt` comes from subsection [2.3](#stufe-2-3).
:::
:::

---
title: Numbering, sequences of numbers and differences: nl, seq and diff
pfad: Computer Science / Linux and the Command Line / Text Tools and Regular Expressions
adresse: informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke
knoten: Chapter 6: Text Tools and Regular Expressions
order: 6110500
summary: Three small tools round off the toolbox: one numbers lines, one generates sequences of numbers, and one shows how two files differ.
tags: nl, seq, diff
lang: en
---

<span class="anker" id="stufe-4"></span>

:::zweck
Three small tools round off the toolbox: one numbers lines, one generates sequences of numbers, and one shows how two files differ.
:::

### Numbering lines: nl

<span class="anker" id="stufe-4-1"></span>

When you talk to others about a file, you want to be able to point to lines: “There is a typo in line 7.” For that, you need the numbers in front of the lines.

:::definition Definition 4.1 (nl)
<span class="anker" id="satz-4-1"></span>

The command __nl__ writes out each line of its input with a running number in front of it, separated by a tab. Without an option, it numbers only lines that are not empty; with `-ba`, it numbers all of them.
:::

The name stands for “number lines”.

::::beispiel Numbers with and without empty lines
```console
$ nl laeufe.csv | head -n 3
     1  datum,name,km,minuten
     2  2026-11-02,Anna,5.0,28
     3  2026-11-02,Ben,10.5,62
```

The numbers are right-aligned in a column six characters wide. Without an option, an empty line gets no number:

```console
$ printf '%s\n' Anna '' Ben | nl
     1  Anna

     2  Ben
$ printf '%s\n' Anna '' Ben | nl -ba
     1  Anna
     2
     3  Ben
```

`printf` has turned the empty argument `''` into an empty line. Without an option, `nl` skips it when counting; with `-ba`, it does not.
::::

⁠**In short:** `nl` puts line numbers in front of the lines; it counts empty lines only with `-ba`.

### Generating sequences of numbers: seq

<span class="anker" id="stufe-4-2"></span>

For trying things out, you often need a sequence of numbers: the days of a month, the numbers from 1 to 100, kilometer marks 0.5 apart. The brace expansion from [Chapter 5, Section 1.6](/wissen/en/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/expansion-muster-klammern-und-tilde.html#stufe-1-6) can do this only with whole numbers, and it happens before variables are substituted. A program that writes numbers to its standard output has neither of these limitations. Figure [13](#abb-13) shows how it forms a sequence.

:::abbildung linux/k6seq 13
A number line from 0 to 10. `seq 1 4 10` sets a mark at 1 and jumps 4 further to 5 and to 9; the next jump would land at 13, beyond the 10, and stays gray. Below it, `seq 0 0.5 2` with marks 0.5 apart up to exactly 2.
:::

:::definition Definition 4.2 (seq)
<span class="anker" id="satz-4-2"></span>

The command __seq__ writes a sequence of numbers, one per line. `seq end` counts from 1 to `end`, `seq start end` from `start` to `end`, `seq start step end` in steps of the given size. The sequence ends with the last number that does not exceed `end`. `-s` sets a separator other than the line end, `-w` pads with leading zeros to equal width.
:::

::::beispiel Sequences
```console
$ seq 3
1
2
3
$ seq -s' ' 2 2 10
2 4 6 8 10
$ seq -s' ' 0 0.5 2
0.0 0.5 1.0 1.5 2.0
$ seq -w -s' ' 8 11
08 09 10 11
$ seq -s' ' 1 4 10
1 5 9
```

With a step of 0.5, `seq` writes all numbers with one decimal place. The last sequence ends at 9, because 13 would be above 10.
::::

::::beispiel [Second example] A limit from a variable
[Chapter 5, Section 3.9](/wissen/en/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/worttrennung-und-quoting.html#stufe-3-9) showed that `{1..$n}` does not work, because brace expansion comes before parameter expansion. `seq`, by contrast, receives the limit as an ordinary argument, after the shell has substituted `$n`:

```console
$ n=5
$ echo {1..$n}
{1..5}
$ seq -s' ' 1 $n
1 2 3 4 5
```
::::

⁠**In short:** `seq start step end` writes a sequence of numbers, also with decimal numbers and with limits from variables.

### Finding differences: diff

<span class="anker" id="stufe-4-3"></span>

Two versions of a file look almost the same: an older and a newer one, your own and one from the internet. Comparing them line by line by eye is tedious and error-prone. Figure [14](#abb-14) shows what a tool reports instead.

:::abbildung linux/k6diff 14
On the left, the first five lines of the running log; on the right, the same five lines with a lowercase b in `ben`. Identical lines are connected by gray lines. Only line 3 differs, `Ben` versus `ben`; it lights up on both sides. Below that appears the message from `diff`: `3c3`, the old line with `<`, three dashes, the new line with `>`.
:::

:::definition Definition 4.3 (diff)
<span class="anker" id="satz-4-3"></span>

The command __diff__ compares two text files line by line and outputs what you would have to change in the first one to get the second one. Each change begins with a line of line numbers and a letter: `a` for add, `c` for change, `d` for delete. Below it are the affected lines of the first file with `<` in front of them and those of the second with `>`. The exit status is 0 for identical files, 1 for differences and 2 for an error.
:::

To the left of the letter is the line number in the first file, to the right the one in the second; a range is written with a comma, `6,10`. If the files are identical, `diff` writes nothing.

For the comparisons, create two shorter files: `kurz.csv` (German for “short”) with the first five lines of the running log and `klein.csv` (German for “small”), in which, in addition, every uppercase B is written in lowercase:

```console
$ head -n 5 laeufe.csv > kurz.csv
$ head -n 5 laeufe.csv | tr B b > klein.csv
```

::::beispiel Adding, deleting, changing
`neu.csv` from subsection [1.6](textdaten-datensatze-felder-und-zeilenenden.html#stufe-1-6) has one run more than `laeufe.csv`:

```console
$ diff laeufe.csv neu.csv
10a11
> 2026-11-10,Clara,6.0,33
$ echo $?
1
$ diff laeufe.csv laeufe.csv
$ echo $?
0
```

`10a11`: after line 10 of the first file, add what is line 11 in the second. Now the running log against its first five lines:

```console
$ diff laeufe.csv kurz.csv
6,10d5
< 2026-11-05,Ben,5.0,31
< 2026-11-06,Anna,12.0,70
< 2026-11-07,Clara,8.0,44
< 2026-11-08,Ben,21.1,128
< 2026-11-09,Anna,5.0,27
```

`6,10d5`: lines 6 to 10 of the first file are to be deleted; after that, it matches the second one up to that file's line 5. Finally, the two short files:

```console
$ diff kurz.csv klein.csv
3c3
< 2026-11-02,Ben,10.5,62
---
> 2026-11-02,ben,10.5,62
```

`3c3`: line 3 is to be changed; the three dashes separate the old version from the new one.
::::

⁠**In short:** `diff a b` uses `a`, `c` and `d` to show which lines you would have to add, change or delete in `a` to get `b`; the exit status tells whether there are differences.

:::hintergrund The format for proposed changes: diff -u
With `-u`, `diff` writes a more detailed format that developers use to exchange changes:

```console
$ diff -u kurz.csv klein.csv
--- kurz.csv    2026-11-10 11:10:24.238033361 +0100
+++ klein.csv   2026-11-10 11:10:24.842034058 +0100
@@ -1,5 +1,5 @@
 datum,name,km,minuten
 2026-11-02,Anna,5.0,28
-2026-11-02,Ben,10.5,62
+2026-11-02,ben,10.5,62
 2026-11-03,Clara,7.2,41
 2026-11-04,Anna,6.4,35
```

The header lines name both files with their modification time. `@@ -1,5 +1,5 @@` means: five lines starting at line 1 in both files. Lines with `-` are removed, lines with `+` are added, and lines with a space at the beginning are included for orientation. The program `patch` can apply such a diff to another copy of the first file. This is how developers send each other changes instead of sending whole files.
:::

### Exercises for Section [4](#stufe-4)

<span class="anker" id="stufe-4-4"></span>

:::aufgabe Exercise 11 ★★ Generating and numbering
<span class="anker" id="aufg-11"></span>

(a) What does `seq -s+ 10` output? (b) Use `seq` and the shell's arithmetic to calculate the sum of the numbers from 1 to 100, and check the result with the formula $n(n+1)/2$. (c) Number the lines `Anna`, an empty line and `Ben` with `cat -n`. Which form of `nl` does the result match?

:::loesung
```console
$ seq -s+ 10
1+2+3+4+5+6+7+8+9+10
$ echo $(( $(seq -s+ 100) ))
5050
$ printf '%s\n' Anna '' Ben | cat -n
     1  Anna
     2
     3  Ben
```

(a) The numbers from 1 to 10, separated by plus signs instead of line ends. (b) The same calculation up to 100 inserts the command substitution into the shell's arithmetic: 5050. The formula gives $100 \cdot 101 / 2 = 5050$. (c) `cat -n` numbers every line, including the empty one; this matches `nl -ba`, not `nl` without an option.
:::
:::

:::aufgabe Exercise 12 ★★ What has changed?
<span class="anker" id="aufg-12"></span>

Use `printf` to create a shopping list `liste1.txt` with Milch, Brot, Äpfel and a `liste2.txt` with Milch, Butter, Äpfel, Kaffee (German for “milk”, “bread”, “apples”, “butter”, “coffee”), one entry per line. (a) Predict what `diff liste1.txt liste2.txt` outputs and which exit status it reports. (b) Which exit status does `diff` report if the second file is missing?

:::loesung
```console
$ printf '%s\n' Milch Brot Äpfel > liste1.txt
$ printf '%s\n' Milch Butter Äpfel Kaffee > liste2.txt
$ diff liste1.txt liste2.txt
2c2
< Brot
---
> Butter
3a4
> Kaffee
$ echo $?
1
$ diff liste1.txt fehlt.txt
diff: fehlt.txt: No such file or directory
$ echo $?
2
```

(a) Line 2 must be changed, Brot becomes Butter; after line 3, Kaffee must be added, which is line 4 in the second list. The files differ, so the exit status is 1. (b) If a file is missing, that is an error: exit status 2 and a message on standard error.
:::
:::

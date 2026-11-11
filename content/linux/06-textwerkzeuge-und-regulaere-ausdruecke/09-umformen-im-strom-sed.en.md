---
title: Transforming in the stream: sed
pfad: Computer Science / Linux and the Command Line / Text Tools and Regular Expressions
adresse: informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke
knoten: Chapter 6: Text Tools and Regular Expressions
order: 6110900
summary: grep selects lines, tr replaces single characters.
tags: sed, line address, backreference
lang: en
---

<span class="anker" id="stufe-8"></span>

:::zweck
`grep` selects lines, `tr` replaces single characters. Often, however, you want to transform whole pieces of a line: a date into German notation, commas into semicolons, two fields swapped. This section shows a tool that edits lines as they pass through, substitutes with regular expressions, selects and deletes lines and, if needed, changes the file itself.
:::

### The stream editor sed

<span class="anker" id="stufe-8-1"></span>

You operate a text editor such as `nano` from [Chapter 3](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-verzeichnisse-und-pfade.html) by hand: place the cursor, type, save. For a hundred identical changes in a thousand lines, that is too tedious. An editor without a screen that applies the same commands to every line of a stream does this in one go. Figure [26](#abb-26) shows how it proceeds.

:::abbildung linux/k6sed 26
The cycle of `sed`: a line comes from the input into a buffer. The commands run over the buffer one after another, here `s/,/;/`: the first comma becomes a semicolon. Then the buffer is output and the next line is fetched. The file being read stays gray and unchanged.
:::

:::definition Definition 8.1 (sed)
<span class="anker" id="satz-8-1"></span>

The command __sed__, short for “stream editor”, reads its input line by line. It puts each line into a buffer, applies to it, one after another, the commands that are in its first argument after the options, and then writes out the buffer. It does not change the files it reads.
:::

The first argument is put in single quotes because it usually contains regular expressions. Without file names, `sed` reads its standard input; it is therefore a filter.

::::beispiel One comma per line
```console
$ sed 's/,/;/' laeufe.csv | head -n 3
datum;name,km,minuten
2026-11-02;Anna,5.0,28
2026-11-02;Ben,10.5,62
```

In every line, the command `s/,/;/` has replaced the first comma with a semicolon. `laeufe.csv` itself is unchanged.
::::

⁠**In short:** `sed` applies its commands to every line of a stream and writes out the result without changing the file.

### Substituting: the s command

<span class="anker" id="stufe-8-2"></span>

The most important command of `sed` searches the line with a regular expression and replaces the match.

:::definition Definition 8.2 (The s command)
<span class="anker" id="satz-8-2"></span>

`s/expression/replacement/` replaces the first match of the regular expression in every line with the replacement text. With the flag `g` after it, `s/expression/replacement/g`, it replaces all matches in the line. An `&` in the replacement text stands for the match found. Instead of the slash, any other character except the backslash and the newline may separate the three parts.
:::

Without an option, `sed` uses the basic form from subsection [7.5](regulare-ausdrucke-wiederholungen-gruppen-und-alternativen.html#stufe-7-5), with `-E` the extended form. The rule of the longest match from subsection [7.6](regulare-ausdrucke-wiederholungen-gruppen-und-alternativen.html#stufe-7-6) applies to the match.

::::beispiel All commas, numbers in brackets, paths
```console
$ sed 's/,/;/g' laeufe.csv | head -n 3
datum;name;km;minuten
2026-11-02;Anna;5.0;28
2026-11-02;Ben;10.5;62
$ echo 'Anna lief 5 km' | sed 's/[0-9][0-9]*/[&]/'
Anna lief [5] km
$ echo '/home/student/linuxk6' | sed 's|/|:|g'
:home:student:linuxk6
```

With `g`, all commas become semicolons, just as a spreadsheet program set to German expects. `[0-9][0-9]*` is “one digit and any number of further ones” in the basic form; `&` puts the number found in square brackets. In the last command, vertical bars separate the parts because the slashes themselves are to be replaced.
::::

⁠**In short:** `s/expression/replacement/` replaces the first match per line, with `g` all of them; `&` is the match itself.

### Selecting lines: line addresses, -n and p

<span class="anker" id="stufe-8-3"></span>

Not every change should affect every line: only the header line, only Ben's runs, only lines 2 to 4. Besides, `sed` can not only change lines but also select them, like `grep`, `head` or `tail`. Figure [27](#abb-27) shows four ways of selecting lines.

:::abbildung linux/k6zeilenadressen 27
The ten lines of the running log, four times side by side. With `2,4`, lines 2 to 4 light up, with `$` the last line, with `/Clara/` the two lines with Clara, with `1` the header line. Above each column is the line address, below it which lines a command with this address affects.
:::

:::definition Definition 8.3 (Line address, -n, p)
<span class="anker" id="satz-8-3"></span>

A __line address__ in front of a command selects the lines it acts on: a line number, `$` for the last line, `/expression/` for all lines with a match or two line addresses with a comma in between for all lines from the one to the other. Without a line address, a command acts on every line. The option `-n` turns off the output after each line; then only the command `p` writes out lines.
:::

So `sed -n '2,4p'` writes only lines 2 to 4. Without `-n`, they would appear twice, once through `p` and once through the ordinary output.

::::beispiel Selecting and changing selectively
```console
$ sed -n '2,4p' laeufe.csv
2026-11-02,Anna,5.0,28
2026-11-02,Ben,10.5,62
2026-11-03,Clara,7.2,41
$ sed -n '/Clara/p' laeufe.csv
2026-11-03,Clara,7.2,41
2026-11-07,Clara,8.0,44
$ sed -n '$p' laeufe.csv
2026-11-09,Anna,5.0,27
$ sed '/Ben/s/,/;/g' laeufe.csv | head -n 4
datum,name,km,minuten
2026-11-02,Anna,5.0,28
2026-11-02;Ben;10.5;62
2026-11-03,Clara,7.2,41
```

The first three commands do what `head` with `tail`, `grep` and `tail -n 1` do. In the last one, the substitution acts only on lines with `Ben`; the others pass through unchanged.
::::

⁠**In short:** A line address such as `3`, `$`, `/expression/` or `2,4` limits a command to certain lines; `-n` with `p` outputs only these.

### Deleting lines: the d command

<span class="anker" id="stufe-8-4"></span>

The counterpart of selecting is leaving out: the header line, all runs of one person.

:::definition Definition 8.4 (The d command)
<span class="anker" id="satz-8-4"></span>

The command `d` deletes the buffer, outputs nothing and starts immediately with the next line. With a line address in front of it, exactly the selected lines drop out of the stream.
:::

The deletion happens only in the stream, not in the file.

::::beispiel Header line gone, Anna gone
```console
$ sed '1d' laeufe.csv | head -n 2
2026-11-02,Anna,5.0,28
2026-11-02,Ben,10.5,62
$ sed '/Anna/d' laeufe.csv
datum,name,km,minuten
2026-11-02,Ben,10.5,62
2026-11-03,Clara,7.2,41
2026-11-05,Ben,5.0,31
2026-11-07,Clara,8.0,44
2026-11-08,Ben,21.1,128
```

`sed '1d'` does the same as `tail -n +2`, `sed '/Anna/d'` the same as `grep -v Anna`.
::::

⁠**In short:** `d` drops the selected lines from the stream; `1d` removes the header line.

:::hintergrund Stopping early: the q command
The command `q` ends `sed` after the current line has been output. `sed 3q` therefore writes the first three lines and stops reading, like `head -n 3`:

```console
$ sed 3q laeufe.csv
datum,name,km,minuten
2026-11-02,Anna,5.0,28
2026-11-02,Ben,10.5,62
```

Because `sed` does not read any further after that, this is fast even with huge files.
:::

### Groups and backreferences

<span class="anker" id="stufe-8-5"></span>

The date in the running log is written as `2026-11-02`; if you want it in German date notation, `02.11.2026`, you have to insert parts of the match again in a different order. Figure [28](#abb-28) shows how that works.

:::abbildung linux/k6gruppen 28
At the top, the date `2026-11-02` and the expression `^([0-9]{4})-([0-9]{2})-([0-9]{2})`. The three groups each color one piece of the date: `2026` as 1, `11` as 2, `02` as 3. At the bottom, the replacement `\3.\2.\1`: the colored pieces move to their places in the new order, with dots in between. The result is `02.11.2026`.
:::

:::definition Definition 8.5 (Backreference)
<span class="anker" id="satz-8-5"></span>

Each group of an expression remembers the piece it matched. In the replacement text of `s`, a __backreference__ `\1` to `\9` inserts the piece of the first to the ninth group; the opening parentheses are counted from the left.
:::

In the extended form, with `sed -E`, you write the groups with plain parentheses.

::::beispiel Reversing the date, swapping fields
```console
$ sed -E 's/^([0-9]{4})-([0-9]{2})-([0-9]{2})/\3.\2.\1/' laeufe.csv | head -n 3
datum,name,km,minuten
02.11.2026,Anna,5.0,28
02.11.2026,Ben,10.5,62
$ sed -E 's/^([^,]*),([^,]*)/\2,\1/' laeufe.csv | head -n 3
name,datum,km,minuten
Anna,2026-11-02,5.0,28
Ben,2026-11-02,10.5,62
```

The header line contains no date, so there is no match, and it stays as it was. In the second command, `[^,]*` is a field, a sequence of characters without a comma; the first two fields swap places, in every line, including the header line.
::::

⁠**In short:** Groups remember their matches, and `\1` to `\9` insert them again in the replacement text in any order.

:::hintergrund The same substitution in the basic form, and backreferences in the expression
In the basic form, every parenthesis and curly brace needs a backslash, and the command becomes hard to read:

```console
$ sed 's/^\([0-9]\{4\}\)-\([0-9]\{2\}\)-\([0-9]\{2\}\)/\3.\2.\1/' laeufe.csv | sed -n 2p
02.11.2026,Anna,5.0,28
```

Backreferences work not only in the replacement text but also in the expression itself. `\(.\)\1` means: any single character and then the same character once more. Which name contains a double letter?

```console
$ cut -d, -f2 laeufe.csv | sort -u | grep '\(.\)\1'
Anna
```

Such an expression has to remember what it has read, and that is exactly what a finite automaton from subsection [7.7](regulare-ausdrucke-wiederholungen-gruppen-und-alternativen.html#stufe-7-7) cannot do. Backreferences in the expression therefore go beyond regular expressions in the mathematical sense. The standard for Unix tools knows them only in the basic form; GNU `grep` and `sed` also allow them in the extended form. The GNU `grep` manual warns that they can slow down a search considerably.
:::

### Editing the file itself: sed -i

<span class="anker" id="stufe-8-6"></span>

So far, `sed` has written only to standard output. If you want the result in the file, redirecting into the same file seems the obvious choice.

:::warnung sed with redirection into the same file
`sed 's/Ben/Benjamin/' kopie.csv > kopie.csv` leaves an empty file: the shell empties `kopie.csv` for the redirection before `sed` starts, and `sed` then has nothing left to read. This is the truncation trap from [Chapter 4, Section 2.7](/wissen/en/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/ausgaben-umleiten.html#stufe-2-7); it applies to every tool, not just to `sed`.
:::

:::definition Definition 8.6 (sed -i)
<span class="anker" id="satz-8-6"></span>

With the option `-i`, `sed` writes the result not to standard output but into a new file and then replaces the file it has read with this new file. If an extension follows directly after `-i`, such as `-i.bak`, `sed` keeps the old version under the name with this extension.
:::

The “i” stands for “in place”. Figure [29](#abb-29) shows why nothing is lost in the process.

:::abbildung linux/k6sedi 29
`sed -i` on the file `kopie.csv`: `sed` reads the old file line by line and writes each edited line into a new file next to it; the old file stays unchanged in the meantime. Only at the end does the new file take over the name `kopie.csv`, and the old one disappears.
:::

::::beispiel Changing in place, with a backup
```console
$ cp laeufe.csv kopie.csv
$ sed -i 's/Ben/Benjamin/' kopie.csv
$ grep -c Benjamin kopie.csv
3
```

`sed` writes nothing to the terminal; the three changes are in the file. With an extension, the old version is kept:

```console
$ sed -i.bak '1d' kopie.csv
$ head -n 1 kopie.csv kopie.csv.bak
==> kopie.csv <==
2026-11-02,Anna,5.0,28

==> kopie.csv.bak <==
datum,name,km,minuten
```

With two files, `head` writes the name above each one. The header line is now missing from `kopie.csv`; the backup still has it.
::::

:::warnung sed -i does not ask
`sed -i` changes the file without asking and without a trash to restore it from. A typo in the expression can delete or destroy lines. So try a command without `-i` first, look at the output, and only then add `-i` or `-i.bak`.
:::

⁠**In short:** `sed -i` writes the result into a new file that replaces the old one; `-i.bak` keeps the old version. A redirection into the same file, by contrast, empties it.

:::hintergrund sed -i and a second name
The fact that `sed -i` creates a new file has a consequence for hard links from [Chapter 3, Section 8.3](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/inode-und-links.html#stufe-8-3). If you give a fresh copy a second name and then change the file with `sed -i`, the change applies only under the one name:

```console
$ cp laeufe.csv kopie.csv
$ ln kopie.csv zweitname.csv
$ ls -l kopie.csv zweitname.csv
-rw-r--r-- 2 student student 232 Nov 10 11:10 kopie.csv
-rw-r--r-- 2 student student 232 Nov 10 11:10 zweitname.csv
$ sed -i 's/Clara/Klara/' kopie.csv
$ grep -c Klara kopie.csv zweitname.csv
kopie.csv:2
zweitname.csv:0
$ ls -l kopie.csv zweitname.csv
-rw-r--r-- 1 student student 232 Nov 10 11:10 kopie.csv
-rw-r--r-- 1 student student 232 Nov 10 11:10 zweitname.csv
```

Before, both names pointed to the same inode; the link count was 2. `sed -i` created a new file and gave it the name `kopie.csv`; `zweitname.csv` (German for “second name”) still points to the old, unchanged inode, and both counts are now 1. For symbolic links from [Chapter 3, Section 8.5](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/inode-und-links.html#stufe-8-5), the GNU `sed` manual explicitly names the same consequence: without a further option, `sed -i` replaces the link with a regular file, and the target of the link stays unchanged.
:::

### Exercises for Section [8](#stufe-8)

<span class="anker" id="stufe-8-7"></span>

:::aufgabe Exercise 22 ★★ Reshaping for a spreadsheet program
<span class="anker" id="aufg-22"></span>

A spreadsheet program set to German expects semicolons and no header line. (a) Produce this version with two calls of `sed` in a pipeline. (b) Produce it with a single call; you separate several commands in the first argument with a semicolon. (c) In addition, swap date and name, as in the example on backreferences.

:::loesung
```console
$ sed '1d' laeufe.csv | sed 's/,/;/g' | head -n 3
2026-11-02;Anna;5.0;28
2026-11-02;Ben;10.5;62
2026-11-03;Clara;7.2;41
$ sed '1d; s/,/;/g' laeufe.csv | head -n 3
2026-11-02;Anna;5.0;28
2026-11-02;Ben;10.5;62
2026-11-03;Clara;7.2;41
$ sed -E '1d; s/^([^,]*),([^,]*)/\2,\1/; s/,/;/g' laeufe.csv | head -n 3
Anna;2026-11-02;5.0;28
Ben;2026-11-02;10.5;62
Clara;2026-11-03;7.2;41
```

(a) The first `sed` deletes the header line, the second replaces all commas. (b) Both commands in one call: for each line, `sed` carries them out in turn; for line 1, `d` ends the work on this line before `s` gets its turn. `head -n 3` only shortens the display. (c) The order of the commands matters: first swap while commas still separate the fields, then replace the commas. The other way around, the expression with `[^,]` would no longer find any commas and would take the whole line as one field.
:::
:::

:::aufgabe Exercise 23 ★★ A short date
<span class="anker" id="aufg-23"></span>

Use `sed -E` to convert the date into the notation `02.11.26` with a two-digit year. Which groups do you need, and which part of the year belongs in no group?

:::loesung
```console
$ sed -E 's/^[0-9]{2}([0-9]{2})-([0-9]{2})-([0-9]{2})/\3.\2.\1/' laeufe.csv | head -n 3
datum,name,km,minuten
02.11.26,Anna,5.0,28
02.11.26,Ben,10.5,62
```

Three groups: the last two digits of the year, the month and the day. The first two digits of the year, `20`, must belong to the match so that they are replaced as well and disappear, but they are in no group, because they do not occur in the result. The header line stays, because it does not begin with digits.
:::
:::

:::aufgabe Exercise 24 ★★★ -n and -i together
<span class="anker" id="aufg-24"></span>

Copy `laeufe.csv` to `probe2.csv`. Predict what the file contains after `sed -n -i 's/Ben/B./p' probe2.csv`, and check it. Why is this combination dangerous?

:::loesung
```console
$ cp laeufe.csv probe2.csv
$ sed -n -i 's/Ben/B./p' probe2.csv
$ cat probe2.csv
2026-11-02,B.,10.5,62
2026-11-05,B.,5.0,31
2026-11-08,B.,21.1,128
```

Only the three changed lines remain in the file; the other seven are lost. `-n` switches off the ordinary output; only `p` writes, and only for lines in which `s` has replaced something. Without `-i`, this would be a convenient way to look at only the changed lines. With `-i`, exactly this output ends up in the file, and all other lines are gone. The manual of GNU `sed` explicitly warns against this combination; it is one reason to add `-i` only once the command without `-i` outputs what you want.
:::
:::

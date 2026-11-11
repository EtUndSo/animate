---
title: Searching with grep
pfad: Computer Science / Linux and the Command Line / Text Tools and Regular Expressions
adresse: informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke
knoten: Chapter 6: Text Tools and Regular Expressions
order: 6110600
summary: In Chapter 4, grep picked out lines with a word.
tags: grep
lang: en
---

<span class="anker" id="stufe-5"></span>

:::zweck
In [Chapter 4](/wissen/en/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/stroeme-umleitung-pipes-und-exit-status.html), `grep` picked out lines with a word. This section shows what `grep` does exactly and how its most important options invert a search, count, number, restrict it to the matches and extend it to whole directories.
:::

### Lines with a search text: grep

<span class="anker" id="stufe-5-1"></span>

From a long file, you often want only the lines that contain something specific: all of Clara's runs, all messages of a program on a particular day.

:::definition Definition 5.1 (grep)
<span class="anker" id="satz-5-1"></span>

After the options, the command __grep__ receives a search text as its first argument and then files. It writes out every line of these files in which the search text occurs anywhere and leaves out the others. Without files, it reads its standard input. Its exit status is 0 if at least one line matched, 1 if none matched and 2 for an error.
:::

Case matters: `clara` is a different search text from `Clara`. [Chapter 4, Section 5.2](/wissen/en/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/der-exit-status.html#stufe-5-2) showed how to use the exit status of `grep -q`, which produces no output, for decisions.

::::beispiel Clara's runs
```console
$ grep Clara laeufe.csv
2026-11-03,Clara,7.2,41
2026-11-07,Clara,8.0,44
$ grep clara laeufe.csv
$ echo $?
1
```

With a lowercase c, `grep` finds nothing, writes nothing and reports exit status 1.
::::

⁠**In short:** `grep searchtext file` writes the lines that contain the search text; the exit status tells whether there were any.

:::hintergrund Where the name grep comes from
The name comes from the text editor `ed`, which was used to edit files in the early years of Unix. There, the command that outputs all lines with a particular content was called `g/re/p`: `g` for “global”, all lines, `re` for the search expression and `p` for “print”. Around 1973, Ken Thompson turned this one command into a small program of its own that you can use with any file and after any pipe, entirely in the spirit of the Unix philosophy from [Chapter 4, Section 4.5](/wissen/en/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/pipes-und-filter.html#stufe-4-5).
:::

### Inverting, counting, numbering: -i, -v, -c and -n

<span class="anker" id="stufe-5-2"></span>

Often the question is put a little differently from “which lines contain the word”: Which ones do not contain it? How many are there? Where in the file are they? Figure [15](#abb-15) shows how four options change the same search.

:::abbildung linux/k6grep 15
The running log with its ten lines and the search text `Anna`. Without an option, the four lines with Anna light up. `-v` inverts: now the other six light up. `-c` replaces the lines with their count, 4. `-n` puts in front of each matching line its number: 2, 5, 7 and 10.
:::

:::definition Definition 5.2 (Options of grep)
<span class="anker" id="satz-5-2"></span>

`-i` ignores case in the comparison. `-v` inverts the selection and writes the lines in which the search text does not occur. `-c` writes only the number of lines instead of the lines themselves. `-n` puts in front of each output line its number in the file and a colon.
:::

::::beispiel Four questions for the running log
```console
$ grep -i clara laeufe.csv
2026-11-03,Clara,7.2,41
2026-11-07,Clara,8.0,44
$ grep -v Anna laeufe.csv
datum,name,km,minuten
2026-11-02,Ben,10.5,62
2026-11-03,Clara,7.2,41
2026-11-05,Ben,5.0,31
2026-11-07,Clara,8.0,44
2026-11-08,Ben,21.1,128
$ grep -n Ben laeufe.csv
3:2026-11-02,Ben,10.5,62
6:2026-11-05,Ben,5.0,31
9:2026-11-08,Ben,21.1,128
$ grep -c Anna laeufe.csv
4
```

`-v` also delivers the header line, because `Anna` does not occur in it either. The numbers with `-n` count the header line as line 1.
::::

::::beispiel [Second example] grep as the first stage
As a filter, `grep` fits at the beginning of a pipeline. Which distances did Anna run?

```console
$ grep Anna laeufe.csv | cut -d, -f3 | paste -s -d' '
5.0 6.4 12.0 5.0
```
::::

⁠**In short:** `-i` ignores case, `-v` gives the other lines, `-c` their count, `-n` adds line numbers.

### Outputting only the match: -o

<span class="anker" id="stufe-5-3"></span>

`grep` normally writes the whole line. Sometimes, however, only the piece that matched is of interest, for example to count how often something occurs rather than in how many lines. Figure [16](#abb-16) shows the difference.

:::abbildung linux/k6grepo 16
The line `Anna und Anna` (German for “Anna and Anna”) with two matches for `Anna`. `grep -c` counts lines and reports 1. `grep -o` picks out the two matches and writes each on a line of its own; `wc -l` counts these lines and reports 2.
:::

:::definition Definition 5.3 (grep -o)
<span class="anker" id="satz-5-3"></span>

With the option `-o`, `grep` writes, instead of the whole line, only the pieces that match the search text, each on a line of its own. If the search text occurs several times in a line, several output lines result.
:::

::::beispiel Counting lines or counting matches
```console
$ echo 'Anna und Anna' | grep -c Anna
1
$ echo 'Anna und Anna' | grep -o Anna
Anna
Anna
$ echo 'Anna und Anna' | grep -o Anna | wc -l
2
```

One line, two matches. With a fixed search text, every match looks the same; `-o` then serves mainly for counting.
::::

⁠**In short:** `grep -o` writes only the matching pieces, one per line; with `wc -l`, you thus count matches instead of lines.

### Searching in many files: -r and -l

<span class="anker" id="stufe-5-4"></span>

Where was Clara's run again, in which file? With several files or a whole directory tree, `grep` must also say where a line comes from. Figure [17](#abb-17) shows how it goes about this.

:::abbildung linux/k6grepr 17
A small directory tree: the practice directory with a few files and the subdirectory `archiv` with `november.csv`. `grep -r Clara` visits every file, including the one in the subdirectory; each matching line appears on the right with the file path and a colon in front of it. With `-l`, the output shrinks to one line per file with a match.
:::

:::definition Definition 5.4 (grep with several files, -r, -l)
<span class="anker" id="satz-5-4"></span>

If `grep` receives more than one file, it puts the file name and a colon in front of each output line. With `-r`, it searches all files in the given directories and their subdirectories. With `-l`, it writes, instead of the lines, only the names of the files in which it found something, each one once.
:::

::::beispiel Clara in several files
```console
$ grep Clara laeufe.csv neu.csv
laeufe.csv:2026-11-03,Clara,7.2,41
laeufe.csv:2026-11-07,Clara,8.0,44
neu.csv:2026-11-03,Clara,7.2,41
neu.csv:2026-11-07,Clara,8.0,44
neu.csv:2026-11-10,Clara,6.0,33
$ grep -c Clara laeufe.csv neu.csv
laeufe.csv:2
neu.csv:3
```

With several files, `-c` counts for each one separately. For `-r`, create a subdirectory with a copy:

```console
$ mkdir archiv
$ cp laeufe.csv archiv/november.csv
$ grep -r Clara archiv
archiv/november.csv:2026-11-03,Clara,7.2,41
archiv/november.csv:2026-11-07,Clara,8.0,44
$ grep -rl Clara . | sort
./archiv/november.csv
./klein.csv
./kurz.csv
./laeufe.csv
./namen.txt
./neu.csv
```

`.` is the working directory; `-rl` names all files below it in which Clara occurs, including the list of names from subsection [2.3](spalten-ausschneiden-und-zeichen-ersetzen-cut-tr-und-paste.html#stufe-2-3). `grep -r` goes through the files in the order in which they are stored in the directory, unsorted like `find` in [Chapter 3, Section 10.1](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-finden-und-platz-messen.html#stufe-10-1); the `sort` after it makes the list easy to read. If you have solved the exercises in the practice directory, the list also names their files, such as `probe.csv`.
::::

⁠**In short:** With several files, `grep` names the origin of each line; `-r` searches whole directory trees, `-l` names only the file names.

### Exercises for Section [5](#stufe-5)

<span class="anker" id="stufe-5-5"></span>

:::aufgabe Exercise 13 ★ grep in the running log
<span class="anker" id="aufg-13"></span>

(a) How many runs did Ben have? (b) Output all runs that are not Anna's, without the header line. (c) In which line is the run of 7 November?

:::loesung
```console
$ grep -c Ben laeufe.csv
3
$ grep -v Anna laeufe.csv | grep -v datum
2026-11-02,Ben,10.5,62
2026-11-03,Clara,7.2,41
2026-11-05,Ben,5.0,31
2026-11-07,Clara,8.0,44
2026-11-08,Ben,21.1,128
$ grep -n 2026-11-07 laeufe.csv
8:2026-11-07,Clara,8.0,44
```

(a) Three lines with Ben. (b) `grep -v Anna` also lets the header line through; a second `grep -v` with a word from the header line removes it. A `tail -n +2` in front would work just as well. (c) Line 8, counting the header line.
:::
:::

:::aufgabe Exercise 14 ★★ Lines or matches?
<span class="anker" id="aufg-14"></span>

Predict which of the two numbers is larger, `grep -c 0 laeufe.csv` or the number that `grep -o 0 laeufe.csv | wc -l` returns, and give your reasons. Check on the computer and explain the two values.

:::loesung
```console
$ grep -c 0 laeufe.csv
9
$ grep -o 0 laeufe.csv | wc -l
25
```

`grep -c` counts lines in which at least one 0 occurs; these are all nine runs, because every date contains one, and the header line contains none. `grep -o` writes every single 0 on a line of its own. Every date contains two, in `2026` and in the day `0x`; in addition, there are the zeros in `5.0` (three times), `10.5`, `12.0`, `70` and `8.0`. Together, $9 \cdot 2 + 3 + 1 + 2 + 1 = 25$. The second number is at least as large as the first, because every line counted has at least one match.
:::
:::

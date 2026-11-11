---
title: Sorting and counting: sort and uniq
pfad: Computer Science / Linux and the Command Line / Text Tools and Regular Expressions
adresse: informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke
knoten: Chapter 6: Text Tools and Regular Expressions
order: 6110400
summary: Who ran most often, which run was the longest?
tags: sort, sort key, locale, uniq
lang: en
---

<span class="anker" id="stufe-3"></span>

:::zweck
Who ran most often, which run was the longest? For questions like these, you put the lines in order and count identical ones. This section shows how `sort` compares lines, how it sorts numbers and individual columns, why the order depends on the language setting and how to count identical lines with `uniq`.
:::

### How sort compares: the character order

<span class="anker" id="stufe-3-1"></span>

In [Chapter 4, Section 4.2](/wissen/en/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/pipes-und-filter.html#stufe-4-2), `sort` put the lines of a list in order. With words, the result looks like a dictionary; with numbers, sometimes it does not. To predict the result, you need to know how `sort` compares two lines.

:::definition Definition 3.1 (sort)
<span class="anker" id="satz-3-1"></span>

The command __sort__ reads all lines of its input and writes them out in order. It compares two lines character by character from the left; the first character in which they differ decides, according to the order of the characters. If one line is the beginning of the other, the shorter one comes first. With `-r`, `sort` reverses the order.
:::

Under the language setting of the test system, which [Chapter 5, Section 1.3](/wissen/en/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/expansion-muster-klammern-und-tilde.html#stufe-1-3) mentioned in connection with the order of file names, the order of the characters is the order of their numbers. In it, among other things, the digits come before the uppercase letters, these come before the lowercase letters, and umlauts such as ä come after them. Python compares strings the same way ([Python, Chapter 3, Section 1.3](/wissen/en/informatik/programmieren/python/entscheidungen-und-schleifen/bedingungen-vergleiche-und-logische-operatoren.html#stufe-1-3)).

::::beispiel Numbers as text, date before header line
```console
$ printf '%s\n' 10 9 100 | sort
10
100
9
$ sort laeufe.csv
2026-11-02,Anna,5.0,28
2026-11-02,Ben,10.5,62
2026-11-03,Clara,7.2,41
2026-11-04,Anna,6.4,35
2026-11-05,Ben,5.0,31
2026-11-06,Anna,12.0,70
2026-11-07,Clara,8.0,44
2026-11-08,Ben,21.1,128
2026-11-09,Anna,5.0,27
datum,name,km,minuten
```

`10` and `100` begin with `1`, `9` with `9`; the 1 comes before the 9, so both come before the 9. `10` is the beginning of `100` and comes first. In the running log, every record begins with a digit, the header line with the letter `d`; digits come before letters, which is why the header line ends up at the end. The runs themselves are in date order, because a date of the form year-month-day sorts correctly character by character.
::::

```console
$ printf '%s\n' 10 9 100 | sort -r
9
100
10
```

`-r` simply turns the same order around.

⁠**In short:** `sort` compares lines character by character from the left according to the order of the characters; that is why `10` comes before `9`.

### Sorting numerically: sort -n

<span class="anker" id="stufe-3-2"></span>

For distances and minutes, the character order is wrong: a run of 10.5 km is longer than one of 5 km, even though `1` comes before `5`. Figure [9](#abb-9) puts the two ways of comparing side by side.

:::abbildung linux/k6lexnum 9
At the top, `sort` compares the texts `10.5` and `5.0` character by character: the very first character decides, `1` is less than `5`, so `10.5` comes first. At the bottom, `sort -n` reads a number at the beginning of each line and compares the numeric values: 5.0 is less than 10.5, so `5.0` comes first.
:::

:::definition Definition 3.2 (sort -n)
<span class="anker" id="satz-3-2"></span>

With the option `-n`, `sort` reads a number at the beginning of each line, with an optional minus sign and an optional decimal point, and compares the lines by the value of this number. A line that does not begin with a number counts as the number 0. If the values are equal, the character order of the whole line decides.
:::

::::beispiel Numbers by their value
```console
$ printf '%s\n' 10 9 100 | sort -n
9
10
100
$ printf '%s\n' 2.5 -3 10 abc | sort -n
-3
abc
2.5
10
```

`abc` has no number at the beginning, counts as 0 and ends up between $-3$ and $2.5$. The difference is especially clear in the column of distances; `paste -s -d' '` puts the result into one line to save space:

```console
$ cut -d, -f3 laeufe.csv | sort | paste -s -d' '
10.5 12.0 21.1 5.0 5.0 5.0 6.4 7.2 8.0 km
$ cut -d, -f3 laeufe.csv | sort -n | paste -s -d' '
km 5.0 5.0 5.0 6.4 7.2 8.0 10.5 12.0 21.1
```

Without `-n`, the two-digit distances come first and `km` from the header line comes last; with `-n`, it is the other way around: `km` counts as 0, and the distances are in the order of their values.
::::

⁠**In short:** `sort -n` compares the number at the beginning of the line by its value; lines without a number count as 0.

### Sorting by a column: -t and -k

<span class="anker" id="stufe-3-3"></span>

In the running log, the distance is not at the beginning but in field 3. You could cut it out with `cut`, but then the date and the name would be lost. What you want is to sort the whole records by a single field. Figure [10](#abb-10) shows the idea.

:::abbildung linux/k6schluessel 10
The records of the running log one below the other; in each line, field 3, the distance, has a colored background: the key. `sort -t, -k3,3n` compares only these highlighted pieces, as numbers. The whole lines move to their new places until the distances grow from top to bottom; for the three runs of 5.0 km, the whole line decides.
:::

:::definition Definition 3.3 (Sort key)
<span class="anker" id="satz-3-3"></span>

`-t` and a character set the separator at which `sort` splits the lines into fields. `-k A,B` makes the fields from number $A$ to number $B$ the __sort key__: `sort` compares only this piece of the line. Letters such as `n` or `r` directly after the specification, as in `-k3,3n`, apply only to this key. If `,B` is missing, the key extends to the end of the line. Several `-k` are compared one after the other; if all keys are equal, the whole line decides.
:::

So `-k3,3` means “from field 3 to field 3”, only this one field. Without `-t`, a new field begins where spaces or tabs follow another character; these spaces belong to the new field.

::::beispiel By distance, short and long
```console
$ sort -t, -k3,3n laeufe.csv
datum,name,km,minuten
2026-11-02,Anna,5.0,28
2026-11-05,Ben,5.0,31
2026-11-09,Anna,5.0,27
2026-11-04,Anna,6.4,35
2026-11-03,Clara,7.2,41
2026-11-07,Clara,8.0,44
2026-11-02,Ben,10.5,62
2026-11-06,Anna,12.0,70
2026-11-08,Ben,21.1,128
```

The header line has the text `km` in field 3, counts as 0 and comes first. The three runs of 5.0 km have the same key; among them, the whole line decides, that is, the date. In descending order and cut down to three lines, this gives the leaderboard:

```console
$ sort -t, -k3,3nr laeufe.csv | head -n 3
2026-11-08,Ben,21.1,128
2026-11-06,Anna,12.0,70
2026-11-02,Ben,10.5,62
```

The longest run was Ben's half marathon of 21.1 km.
::::

::::beispiel Two keys
Ordered by name and, for each name, the longest runs first; `tail -n +2` removes the header line beforehand:

```console
$ tail -n +2 laeufe.csv | sort -t, -k2,2 -k3,3nr
2026-11-06,Anna,12.0,70
2026-11-04,Anna,6.4,35
2026-11-02,Anna,5.0,28
2026-11-09,Anna,5.0,27
2026-11-08,Ben,21.1,128
2026-11-02,Ben,10.5,62
2026-11-05,Ben,5.0,31
2026-11-07,Clara,8.0,44
2026-11-03,Clara,7.2,41
```

The first key orders by name, the second, only within identical names, by distance, in descending order.
::::

⁠**In short:** `sort -t, -k3,3n` sorts whole lines by the value of field 3; further `-k` decide in the case of a tie.

:::hintergrund Why -k2 and -k2,2 sort differently
Without an end, a key extends to the end of the line. You notice this only when the values of the field are equal:

```console
$ tail -n +2 laeufe.csv | sort -t, -k2 | head -n 2
2026-11-06,Anna,12.0,70
2026-11-09,Anna,5.0,27
$ tail -n +2 laeufe.csv | sort -t, -k2,2 | head -n 2
2026-11-02,Anna,5.0,28
2026-11-04,Anna,6.4,35
```

With `-k2`, `sort` compares pieces such as `Anna,12.0,70` and `Anna,5.0,27`; after `Anna,`, the `1` decides against the `5`, a text comparison of the distance. With `-k2,2`, all four keys `Anna` are equal, and the whole line, that is, the date, decides. With numbers, this is especially treacherous: `-k2n` instead of `-k2,2n` makes everything from field 2 to the end of the line the key for the numeric comparison, and the manual of the GNU implementation explicitly warns that this rarely does what you expect. If you mean a single field, write `-k2,2`. The option `--debug` underlines in each line the piece that `sort` uses as the key.
:::

### The locale

<span class="anker" id="stufe-3-4"></span>

The same file can come out sorted differently on two computers. This is not due to `sort` but to the language setting, which has so far come up only in passing. It determines which language's rules are used to handle text.

:::definition Definition 3.4 (Locale)
<span class="anker" id="satz-3-4"></span>

The __locale__, the language setting, is a set of rules for a language and a country. Among other things, it determines which bytes together form a character, which characters are letters, in which order characters are sorted and which character is the decimal separator. A program learns it from environment variables, above all from `LANG` and `LC_ALL`; if `LC_ALL` is set, it takes priority.
:::

A locale has a name such as `de_DE.UTF-8` for German in Germany with UTF-8. Two special ones are called `C` and `C.UTF-8`: they sort by the numbers of the characters and are the same everywhere. You can use only locales that are installed on the system; `locale -a` shows them.

::::beispiel The locale of the test system
```console
$ echo $LANG
C.UTF-8
$ locale -a
C
C.utf8
POSIX
```

WSL starts Ubuntu with `C.UTF-8`, and nothing more is installed on the test system; `POSIX` is a second name for `C`. With this setting, `sort` sorts uppercase letters before lowercase letters and the umlaut to the end. `-f` treats lowercase letters like uppercase letters; `LC_ALL=C` before the command forces the setting `C` for this one call:

```console
$ printf '%s\n' b ä B a A Z | sort | paste -s -d' '
A B Z a b ä
$ printf '%s\n' b ä B a A Z | sort -f | paste -s -d' '
A a B b Z ä
$ printf '%s\n' b ä B a A Z | LC_ALL=C sort | paste -s -d' '
A B Z a b ä
```

`C` and `C.UTF-8` both order by the numbers of the characters; that is why the first and the last line are the same.
::::

On a computer with a German desktop, `de_DE.UTF-8` is usually set. According to the documentation of the GNU tools, `sort` sorts like a dictionary there: case and umlauts count only when the letters are otherwise the same, and the list would come out as a, A, ä, b, B, Z. This is not verified here, because this locale is missing on the test system.

⁠**In short:** The locale determines how `sort` orders; `C` and `C.UTF-8` order by character numbers, and `LC_ALL=C sort` makes a result the same on every computer.

:::hintergrund The decimal separator and sort -n
The locale also determines which character `sort -n` reads as the decimal separator; this is how the manual of the GNU implementation describes it. Under `de_DE.UTF-8`, it is a comma, and the dot separates thousands there, as in `1.050`. The GNU implementation of `sort -n` then reads a distance such as `10.5` as 105; on the test system, this cannot be shown, because this locale is missing. If you sort files with a decimal point, you therefore write `LC_ALL=C sort -n`. The same is advisable in anything that is supposed to deliver the same result on different computers. The option `--debug` names the rules by which `sort` is currently comparing:

```console
$ printf '%s\n' b a | sort --debug
sort: text ordering performed using simple byte comparison
a
_
b
_
$ printf '%s\n' b a | gnusort --debug
gnusort: text ordering performed using ‘C.UTF-8’ sorting rules
a
_
b
_
```

As of the uutils implementation in Ubuntu 26.04: under `C.UTF-8`, it reports a simple comparison of the bytes, the GNU implementation the rules of `C.UTF-8`. Both result in the same order, because in UTF-8 the bytes of the characters follow the same order as their numbers. The dashes under each line are the underlining of the key, here the whole line.
:::

### Identical adjacent lines: uniq

<span class="anker" id="stufe-3-5"></span>

[Chapter 4, Sections 4.2](/wissen/en/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/pipes-und-filter.html#stufe-4-2) and [4.3](/wissen/en/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/pipes-und-filter.html#stufe-4-3) showed that `uniq` removes repetitions only if `sort` has brought identical lines together beforehand. With an option, removing turns into counting. Figure [11](#abb-11) shows how `uniq` works and why it depends on neighbors.

:::abbildung linux/k6uniq 11
`uniq -c` reads a stream of names, line by line from the top. Next to the stream, there is a single note with the previous line and a counter. If the new line is the same, the counter grows; if it is different, `uniq` writes out the counter and the note and starts over. With the unsorted sequence Anna, Ben, Clara, Anna, every line therefore comes out with 1; with the sorted sequence Anna, Anna, Anna, Anna, Ben …, the counts 4, 3 and 2 result.
:::

:::definition Definition 3.5 (uniq)
<span class="anker" id="satz-3-5"></span>

The command __uniq__ compares each line of its input with the line directly before it and, of several identical lines in a row, writes out only one. With `-c`, it puts in front of each output line how often it occurred in a row. `-d` outputs only lines that occurred several times in a row, `-u` only those that stood alone.
:::

::::beispiel Counting with and without sort
```console
$ cut -d, -f2 laeufe.csv | uniq -c
      1 name
      1 Anna
      1 Ben
      1 Clara
      1 Anna
      1 Ben
      1 Anna
      1 Clara
      1 Ben
      1 Anna
$ cut -d, -f2 laeufe.csv | sort | uniq -c
      4 Anna
      3 Ben
      2 Clara
      1 name
```

Nowhere in the running log are two identical names one below the other, so `uniq` counts each line on its own. After `sort`, identical names stand together, and the counters are right: Anna ran four times, Ben three times, Clara twice.
::::

::::beispiel [Second example] Duplicate and single distances
```console
$ cut -d, -f3 laeufe.csv | sort | uniq -d
5.0
$ cut -d, -f3 laeufe.csv | sort | uniq -u | paste -s -d' '
10.5 12.0 21.1 6.4 7.2 8.0 km
```

Only the distance 5.0 occurs more than once. All other values stand alone, including `km` from the header line.
::::

⁠**In short:** `uniq` combines identical lines that stand directly one below the other; `-c` counts them, `-d` and `-u` select repeated or single ones.

:::hintergrund Why uniq compares only neighbors
`uniq` reads its stream exactly once from front to back and remembers only one line, the previous one. It needs no more than that to recognize identical neighbors, and that is why its memory requirement depends only on the length of a line, not on the number of lines. It can output each line as soon as the next one is different, and it even works behind `tail -f` with a stream that never ends. Finding identical lines in arbitrary places, by contrast, would mean remembering all previous lines. This work is left to `sort`, which has to read everything anyway: the smallest line may be at the very end, so `sort` cannot output any line before it has seen the last one. For large inputs, the GNU implementation sorts pieces in memory, stores them in temporary files and merges them afterward. Neither the standard for Unix shells and their tools nor the manuals explicitly justify the restriction to neighbors; the reasoning above is a derivation of our own from the way the two tools work.
:::

### Counting frequencies: sort, uniq -c, sort -rn

<span class="anker" id="stufe-3-6"></span>

The question “What occurs how often, and what occurs most often?” comes up so often that a fixed sequence of tools has become established for it. Figure [12](#abb-12) shows what the three steps do with the column of distances.

:::abbildung linux/k6haeufigkeit 12
The nine distances of the running log, unsorted. `sort` orders them and pushes the three values `5.0` together into a block; the other six values stand alone. `uniq -c` turns each block into a line with its length in front: once `3 5.0`, six times a 1. `sort -rn` orders these lines by the number, and `3 5.0` moves from the middle to the top.
:::

:::satz Theorem 3.6 (Frequency table)
<span class="anker" id="satz-3-6"></span>

The pipeline `sort | uniq -c | sort -rn` turns a list of values, one per line, into a table of the different values with their frequency, the most frequent first. The first `sort` brings identical values together, `uniq -c` counts them, `sort -rn` orders by the count in descending order.
:::

The second `sort` needs `-n`, because the lines now begin with a number; `uniq -c` indents them to the right, and `sort -n` skips leading spaces.

::::beispiel Who runs most often?
```console
$ tail -n +2 laeufe.csv | cut -d, -f2 | sort | uniq -c | sort -rn
      4 Anna
      3 Ben
      2 Clara
```

First the header line goes, then the names are cut out, then comes the frequency table. With field 3 instead of field 2 and `head -n 1` at the end, the same pipeline asks for the most frequent distance:

```console
$ tail -n +2 laeufe.csv | cut -d, -f3 | sort | uniq -c | sort -rn | head -n 1
      3 5.0
```
::::

If you need only the different values without a count, you can write `sort | uniq` more briefly: `sort -u` writes out only one of several identical lines.

```console
$ tail -n +2 laeufe.csv | cut -d, -f2 | sort -u
Anna
Ben
Clara
```

⁠**In short:** `sort | uniq -c | sort -rn` counts how often each value occurs and puts the most frequent one at the top; `sort -u` delivers only the different values.

### Exercises for Section [3](#stufe-3)

<span class="anker" id="stufe-3-7"></span>

:::aufgabe Exercise 7 ★ Sorting numbers
<span class="anker" id="aufg-7"></span>

(a) Predict in which order `sort` and `sort -n` output the lines `8`, `75`, `120` and `7.5`, and check it. (b) Output the longest run. (c) Output the shortest run without the header line getting in the way. Why is it this particular one of the three runs of 5.0 km?

:::loesung
```console
$ printf '%s\n' 8 75 120 7.5 | sort | paste -s -d' '
120 7.5 75 8
$ printf '%s\n' 8 75 120 7.5 | sort -n | paste -s -d' '
7.5 8 75 120
$ sort -t, -k3,3nr laeufe.csv | head -n 1
2026-11-08,Ben,21.1,128
$ tail -n +2 laeufe.csv | sort -t, -k3,3n | head -n 1
2026-11-02,Anna,5.0,28
```

(a) Without `-n`, `sort` compares character by character: `120` begins with the smallest digit and comes first, `8` begins with the largest and comes last. `7.5` and `75` both begin with 7; at the second position, the dot decides, and in the order of the characters it comes before the digits. With `-n`, the value counts. (b) Field 3 by value in descending order; the first line is the half marathon. (c) In ascending order, the header line would come first, because its `km` counts as 0, followed by the three runs of 5.0 km. Without the header line, these three stay at the front; their key is the same, and the whole line decides. `2026-11-02,Anna` is smaller in the character order than `2026-11-05,Ben` and `2026-11-09,Anna`, so the run of 2 November comes first.
:::
:::

:::aufgabe Exercise 8 ★★ How often?
<span class="anker" id="aufg-8"></span>

(a) How often does each distance occur? (b) How many different people ran? (c) On how many different days did someone run? Answer each question with a pipeline.

:::loesung
```console
$ tail -n +2 laeufe.csv | cut -d, -f3 | sort | uniq -c | sort -rn
      3 5.0
      1 8.0
      1 7.2
      1 6.4
      1 21.1
      1 12.0
      1 10.5
$ tail -n +2 laeufe.csv | cut -d, -f2 | sort -u | wc -l
3
$ tail -n +2 laeufe.csv | cut -d, -f1 | sort -u | wc -l
8
```

(a) The frequency table from subsection [3.6](#stufe-3-6) for field 3: 5.0 km three times, every other distance once. The lines with the count 1 are in reverse character order, because for the same count the whole line decides, and `-r` reverses this comparison as well. (b) `sort -u` leaves each name once, and `wc -l` counts them: three people. (c) The same with the date: nine runs on eight days, because two people ran on 2 November.
:::
:::

:::aufgabe Exercise 9 ★★ Neighbors
<span class="anker" id="aufg-9"></span>

(a) Predict what `printf '%s\n' Anna Anna Ben Anna | uniq -c` outputs. (b) `tail -n +2 laeufe.csv | cut -d, -f1 | uniq -c` counts the runs per day correctly, even though there is no `sort` in front of it. Why?

:::loesung
```console
$ printf '%s\n' Anna Anna Ben Anna | uniq -c
      2 Anna
      1 Ben
      1 Anna
$ tail -n +2 laeufe.csv | cut -d, -f1 | uniq -c | head -n 3
      2 2026-11-02
      1 2026-11-03
      1 2026-11-04
```

(a) The first two lines are identical neighbors and become `2 Anna`. Then comes Ben, then Anna again; this Anna has a different predecessor and is counted anew. (b) The running log is ordered by date, so identical days are already next to each other. `uniq` does not need `sort` if identical values already stand together in the input; `sort` only makes sure that this is the case.
:::
:::

:::aufgabe Exercise 10 ★★★ Two keys
<span class="anker" id="aufg-10"></span>

(a) Sort the runs without the header line by name and, for the same name, by time, the longest first. (b) In the example “Two keys” in subsection [3.3](#stufe-3-3), Anna's two runs of 5.0 km appear in the order 28 before 27 minutes. Which rule determines this?

:::loesung
```console
$ tail -n +2 laeufe.csv | sort -t, -k2,2 -k4,4nr
2026-11-06,Anna,12.0,70
2026-11-04,Anna,6.4,35
2026-11-02,Anna,5.0,28
2026-11-09,Anna,5.0,27
2026-11-08,Ben,21.1,128
2026-11-02,Ben,10.5,62
2026-11-05,Ben,5.0,31
2026-11-07,Clara,8.0,44
2026-11-03,Clara,7.2,41
```

(a) The first key is field 2 alone, the second is field 4 as a number and in descending order. (b) With `-k2,2 -k3,3nr`, both keys are equal for Anna's runs of 5.0 km: the same name, the same distance. Then, as a last resort, `sort` compares the whole lines, and it does so in ascending order, because the `r` belongs only to the second key. `2026-11-02` is smaller than `2026-11-09`, so the run of 28 minutes comes first. In part (a), the two appear in the same order, but for a different reason: there, the second key is the time, and 28 is greater than 27.
:::
:::

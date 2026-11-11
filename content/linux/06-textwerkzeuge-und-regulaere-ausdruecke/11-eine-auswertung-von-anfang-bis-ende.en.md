---
title: An analysis from start to finish
pfad: Computer Science / Linux and the Command Line / Text Tools and Regular Expressions
adresse: informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke
knoten: Chapter 6: Text Tools and Regular Expressions
order: 6111100
summary: Now the whole toolbox is ready.
tags: 
lang: en
---

<span class="anker" id="stufe-10"></span>

:::zweck
Now the whole toolbox is ready. This section shows which tool fits which part of a question, how to build an analysis step by step without getting lost and, with a famous pipeline, how little you need for a surprisingly difficult question.
:::

### Which tool for what

<span class="anker" id="stufe-10-1"></span>

A text file with records is a table. The tools in this chapter differ in what they do with this table. Figure [34](#abb-34) arranges them accordingly.

:::abbildung linux/k6werkzeuge 34
The running log as a table. `grep` and `sed -n` pick out whole lines; `cut` one column; `sort` puts the lines in a new order; `tr` and `sed` change characters in the cells; `uniq -c` and `awk` turn many lines into a few result lines. Each tool appears with its effect on the same table.
:::

:::satz Theorem 10.1 (Choosing a tool)
<span class="anker" id="satz-10-1"></span>

You select lines by content with `grep`, by number with `head`, `tail` or `sed -n`. You select columns with `cut` or `awk`. `tr` replaces characters, `sed` parts of lines. `sort` takes care of ordering, `sort | uniq -c` of counting identical lines. `awk` takes care of calculating with fields and collecting per group.
:::

`awk` can do almost all of this on its own; still, for simple subtasks, you reach for the simple tool because the command is shorter and readable at a glance.

⁠**In short:** For every part of a question, there is a suitable small tool; `awk` is the most versatile, but not always the simplest.

### Building a pipeline step by step

<span class="anker" id="stufe-10-2"></span>

Who ran the farthest in total, and who was the fastest? For questions like these, you do not write the pipeline down in one go; you build it stage by stage and check after each stage whether the intermediate result is correct.

:::satz Theorem 10.2 (Building step by step)
<span class="anker" id="satz-10-2"></span>

Build an analysis stage by stage. After each new stage, look at the intermediate result, with `head` for long outputs. Save an intermediate result that several questions need in a file.
:::

::::beispiel The longest total distance and the fastest pace
Step 1: without the header line, take a quick look.

```console
$ tail -n +2 laeufe.csv | head -n 3
2026-11-02,Anna,5.0,28
2026-11-02,Ben,10.5,62
2026-11-03,Clara,7.2,41
```

Step 2: add up kilometers and minutes per person, save them sorted in a file.

```console
$ tail -n +2 laeufe.csv | awk -F, '{km[$2] += $3; min[$2] += $4} END {for (p in km) print p, km[p], min[p]}' | sort > summen.txt
$ cat summen.txt
Anna 28.4 160
Ben 36.6 221
Clara 15.2 85
```

Step 3: the pace, minutes per kilometer. `summen.txt` (German for “sums”) separates with spaces, so no `-F`.

```console
$ awk '{printf "%s %.1f %.2f\n", $1, $2, $3 / $2}' summen.txt > tempo.txt
$ cat tempo.txt
Anna 28.4 5.63
Ben 36.6 6.04
Clara 15.2 5.59
```

Step 4: sort twice, depending on the question.

```console
$ sort -k2,2nr tempo.txt | head -n 1
Ben 36.6 6.04
$ sort -k3,3n tempo.txt | head -n 1
Clara 15.2 5.59
```

Ben ran the farthest with 36.6 km; Clara was the fastest on average with 5.59 minutes per kilometer. Without `-t`, `sort` splits at spaces, which suits `tempo.txt` (German for “pace”).
::::

⁠**In short:** A pipeline grows stage by stage, every intermediate result is checked, and whatever is needed more than once goes into a file.

### Counting words: a famous pipeline

<span class="anker" id="stufe-10-3"></span>

Which words occur most often in a text? The question sounds like a program of its own with a dictionary and counters. With the tools in this chapter, one line is enough. As the text, we use the license GPL-3 from [Chapter 3, Section 4.3](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-ansehen.html#stufe-4-3), which is present on every Ubuntu system.

::::beispiel The most frequent words of the license
First, the text has to become a list with one word per line. For this, `tr` with `-c` takes the complement of the first set, that is, everything except letters, and `-s` squeezes repetitions. Every sequence of characters that are not letters thus becomes a single newline:

```console
$ tr -cs 'A-Za-z' '\n' < /usr/share/common-licenses/GPL-3 | head -n 4

GNU
GENERAL
PUBLIC
```

The first line is empty because the license begins with spaces. Then come the words, one per line. The rest is the frequency table from subsection [3.6](sortieren-und-zahlen-sort-und-uniq.html#stufe-3-6), with a `tr` beforehand that turns all uppercase letters into lowercase:

```console
$ tr -cs 'A-Za-z' '\n' < /usr/share/common-licenses/GPL-3 | tr A-Z a-z | sort | uniq -c | sort -rn | head -n 5
    345 the
    221 of
    192 to
    184 a
    151 or
```

`the` occurs 345 times in the license. Each stage of this pipeline does one small job: separating the words, converting to lowercase, sorting, counting, sorting by count, keeping the first five. None of them knows anything about words or licenses.
::::

⁠**In short:** Six small tools in a pipeline answer a question for which you would otherwise write a whole program.

:::hintergrund Six lines against a whole program
This pipeline is famous. In the journal Communications of the ACM, Jon Bentley wrote the column “Programming Pearls”. For an installment in 1986, he asked the computer scientist Donald Knuth for a program that outputs the $k$ most frequent words of a text. Knuth wrote a carefully explained program several pages long with an ingenious data structure, entirely from scratch. Doug McIlroy, from whom the idea of the pipe from [Chapter 4](/wissen/en/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/stroeme-umleitung-pipes-und-exit-status.html) comes, was to review it. He acknowledged the careful presentation and set six lines of shell beside it, essentially the pipeline above, only with `sed` and its command `q` instead of `head` at the end. His point was the Unix philosophy from [Chapter 4, Section 4.5](/wissen/en/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/pipes-und-filter.html#stufe-4-5): instead of programming everything anew, you connect existing small tools that read and write text, and you are often done within a few minutes.
:::

**For further practice.** The freely accessible learning platform pwn.college offers short exercises in the browser under the name “Linux Luminarium”; the module “Data Manipulation” matches this chapter. It runs on someone else's computer, not on your own.

### Exercises for Section [10](#stufe-10)

<span class="anker" id="stufe-10-4"></span>

:::aufgabe Exercise 28 ★★★ An analysis of your own
<span class="anker" id="aufg-28"></span>

(a) On which day were the most kilometers run in total, and on which day the second most? (b) On which day did several people run? Answer each question with a pipeline and build it stage by stage.

:::loesung
```console
$ awk -F, 'NR > 1 {t[$1] += $3} END {for (d in t) print d, t[d]}' laeufe.csv | sort -k2,2nr | head -n 2
2026-11-08 21.1
2026-11-02 15.5
```

(a) Stage by stage: first the `awk` program alone, which sums up the distances per date and outputs one line per day; then `sort -k2,2nr` by the sum in descending order; finally `head -n 2`. On 8 November, Ben's half marathon made up 21.1 km; on 2 November, two runs came to $5.0 + 10.5 = 15.5$ km.

```console
$ tail -n +2 laeufe.csv | cut -d, -f1 | sort | uniq -d
2026-11-02
```

(b) The dates of all runs, sorted; `uniq -d` writes only values that occur several times in a row. Only on 2 November did two people run.
:::
:::

:::aufgabe Exercise 29 ★★ Words in another license
<span class="anker" id="aufg-29"></span>

Another license is in `/usr/share/common-licenses/Apache-2.0`. (a) What are its three most frequent words? (b) How many different words does it contain? Pay attention to what difference the empty first line makes.

:::loesung
```console
$ tr -cs 'A-Za-z' '\n' < /usr/share/common-licenses/Apache-2.0 | tr A-Z a-z | sort | uniq -c | sort -rn | head -n 3
    100 the
     69 or
     67 of
$ tr -cs 'A-Za-z' '\n' < /usr/share/common-licenses/Apache-2.0 | tr A-Z a-z | sort -u | wc -l
442
$ tr -cs 'A-Za-z' '\n' < /usr/share/common-licenses/Apache-2.0 | head -n 2 | cat -A
$
Apache$
```

(a) The same pipeline as in subsection [10.3](#stufe-10-3), only with a different file: `the`, `or` and `of`. (b) `sort -u` leaves each word once, and `wc -l` counts 442 lines. Like the GPL, this license also begins with spaces, and the first line of the word list is empty, as `cat -A` shows; this empty line is not a word. So the license contains 441 different words.
:::
:::

---
title: Calculating with columns: awk
pfad: Computer Science / Linux and the Command Line / Text Tools and Regular Expressions
adresse: informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke
knoten: Chapter 6: Text Tools and Regular Expressions
order: 6111000
summary: How many kilometers were run in total, how far did each person run on average, how fast was each run?
tags: awk, rules, associative array
lang: en
---

<span class="anker" id="stufe-9"></span>

:::zweck
How many kilometers were run in total, how far did each person run on average, how fast was each run? For this, you have to calculate with fields, including decimal numbers, and collect values separately for each person. This section shows a tool that is built for exactly this: a small language for columns and sums.
:::

### The program awk: condition and action

<span class="anker" id="stufe-9-1"></span>

`grep` selects lines, `cut` fields, `sed` transforms. So far, only the shell has calculated, and only with integers. A tool that selects lines, knows fields and calculates combines all three tasks. Figure [30](#abb-30) shows how it applies a program made of rules to a file.

:::abbildung linux/k6regeln 30
On the left, an awk program with two rules, `/Clara/ {print "Clara ist gelaufen"}` and `{print "Zeile gelesen"}` (German for “Clara went running” and “line read”). On the right, the lines arrive one after another. For each line, both rules are checked from the top: if the condition matches, the rule lights up and its action writes a line to the output; the second rule, with no condition, lights up for every line.
:::

:::definition Definition 9.1 (awk, rule)
<span class="anker" id="satz-9-1"></span>

The command __awk__ runs a small program that is in its first argument after the options. The program consists of __rules__ of the form `condition {action}`. `awk` reads its input line by line and checks every rule for each line in turn: if the condition is met, it carries out the action. If the condition is missing, the rule applies to every line; if the action is missing, `awk` writes out the line.
:::

A simple condition is a regular expression between slashes; it is met if the line contains a match. `awk` uses the extended form for this. The action `print` writes something out, text in double quotes. The whole program is put in single quotes so that the shell changes nothing in it.

::::beispiel Only a condition, condition and action
```console
$ awk '/Clara/' laeufe.csv
2026-11-03,Clara,7.2,41
2026-11-07,Clara,8.0,44
$ awk '/Clara/ {print "Clara ist gelaufen"}' laeufe.csv
Clara ist gelaufen
Clara ist gelaufen
```

Without an action, `awk` works like `grep`. With an action, it writes the fixed text for each matching line.
::::

⁠**In short:** An awk program consists of rules `condition {action}`, which `awk` applies to every line.

:::hintergrund Where the name comes from
`awk` was created in 1977 at Bell Labs, where Unix was also developed. The name consists of the initials of the last names of its three developers, Alfred Aho, Peter Weinberger and Brian Kernighan. It shares the idea “first select lines, then do something with them” with the line addresses of `sed`; unlike `sed`, it has had variables, calculations and fields built in from the start. There are several implementations of the same language. On the test system, `awk` is the GNU implementation gawk; some systems come with the leaner implementation mawk instead. All examples in this chapter give the same results with both.
:::

### Fields: `$1`, `$0`, `NF` and `-F`

<span class="anker" id="stufe-9-2"></span>

What distinguishes `awk` from `grep` and `sed`: it splits every line into fields on its own, without your having to ask. Figure [31](#abb-31) shows how you address these fields.

:::abbildung linux/k6awkfelder 31
The line `2026-11-08,Ben,21.1,128` with `-F,`. Above the four fields appear their names `$1`, `$2`, `$3`, `$4`; an arc over the whole line carries `$0`. On the right is `NF = 4`, and `$NF` points to the same field as `$4`. On the left is the line number `NR = 9`.
:::

:::definition Definition 9.2 (Fields in awk)
<span class="anker" id="satz-9-2"></span>

`awk` splits every line into fields. `$1`, `$2` and so on are the fields from the left, `$0` is the whole line, and `NF` contains the number of fields, so `$NF` is the last field. Without an option, `awk` splits at sequences of spaces and tabs and skips them at the beginning and at the end of the line. With `-F` and a character, it splits at exactly this character.
:::

In `awk`, the dollar sign means “field number”, not “value of the variable” as in the shell. That is exactly why the program must be in single quotes: between double quotes, the shell would insert its own, usually empty value for `$1` ([Chapter 5, Section 3.5](/wissen/en/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/worttrennung-und-quoting.html#stufe-3-5)). `print` with several values separated by commas writes them with a space in between.

::::beispiel Names and distances, spaces, number of fields
```console
$ awk -F, '{print $2, $3}' laeufe.csv | head -n 3
name km
Anna 5.0
Ben 10.5
$ echo '  Anna   lief  5 km' | awk '{print NF, $1, $NF}'
4 Anna km
```

Without `-F`, `awk` splits the sentence at the spaces, no matter how many there are, into four fields. You check that every line of the running log has exactly four fields like this:

```console
$ awk -F, '{print NF}' laeufe.csv | sort -u
4
```
::::

⁠**In short:** `$1` to `$NF` are the fields of a line, `$0` the whole line, `NF` their number; `-F,` splits at commas.

### Line number and conditions: NR

<span class="anker" id="stufe-9-3"></span>

A regular expression as a condition checks the whole line. For questions such as “runs over 10 km”, you need conditions on a single field and on the position of the line in the file.

:::definition Definition 9.3 (NR, conditions)
<span class="anker" id="satz-9-3"></span>

`NR` contains the number of the line that `awk` is currently processing, counted from 1. Comparisons with `==`, `!=`, `<`, `<=`, `>` and `>=` serve as conditions; you combine them with `&&` for “and”, `||` for “or” and `!` for “not”. `field ~ /expression/` is met if the field contains a match for the regular expression. `awk` compares a field that looks like a number with a number by its value, otherwise as text.
:::

`NR > 1` thus leaves out the header line. Text in a comparison is put in double quotes: `$2 == "Anna"`.

::::beispiel Long runs, names with A or B
```console
$ awk -F, 'NR > 1 && $3 > 10' laeufe.csv
2026-11-02,Ben,10.5,62
2026-11-06,Anna,12.0,70
2026-11-08,Ben,21.1,128
$ awk -F, '$2 ~ /^[AB]/ {print NR, $2}' laeufe.csv | head -n 3
2 Anna
3 Ben
5 Anna
```

Three runs over 10 km. In the second program, field 2 matches “begins with A or B”, and `awk` writes the line number and the name.
::::

::::beispiel [Counterexample] The header line slips through
```console
$ awk -F, '$3 > 10' laeufe.csv
datum,name,km,minuten
2026-11-02,Ben,10.5,62
2026-11-06,Anna,12.0,70
2026-11-08,Ben,21.1,128
```

Without `NR > 1`, the header line appears. Its field 3 is `km`, not a number; `awk` therefore compares as text, `km` with `10`, and because k comes after 1 in the character order, `km` is “greater”.
::::

⁠**In short:** `NR` is the line number; conditions compare fields with numbers or text and are combined with `&&`, `||` and `!`.

### Variables, sums and END

<span class="anker" id="stufe-9-4"></span>

For a sum, `awk` has to remember something from line to line and output the result at the end, when all lines have been read. It can also calculate with decimal numbers:

```console
$ awk -F, 'NR > 1 {print $1, $2, $4 / $3}' laeufe.csv | head -n 3
2026-11-02 Anna 5.6
2026-11-02 Ben 5.90476
2026-11-03 Clara 5.69444
```

Minutes divided by kilometers gives the pace, minutes per kilometer: on 2 November, Anna needed 5.6 minutes for each kilometer.

:::definition Definition 9.4 (Variable in awk, BEGIN, END)
<span class="anker" id="satz-9-4"></span>

A variable in `awk` is a name made of letters, digits and underscores, without a `$` in front. Before its first assignment, it has the value 0 or the empty string, depending on how you use it. `s += $3` adds field 3 to `s`, `n++` increases `n` by 1. A rule with the condition `END` is carried out once after the last line has been read, one with `BEGIN` once before the first one is read.
:::

A semicolon separates several statements in an action. For neat output, there is `printf` with a format, like the shell's `printf` from [Chapter 5, Section 3.1](/wissen/en/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/worttrennung-und-quoting.html#stufe-3-1): `%d` stands for an integer, `%.2f` for a decimal number with two digits after the point, and you write the newline yourself as `\n`.

::::beispiel Total distance and means
```console
$ awk -F, 'NR > 1 {s += $3; n++} END {print s, n, s / n}' laeufe.csv
80.2 9 8.91111
$ awk -F, '$2 == "Anna" {s += $3; n++} END {printf "Anna: %.2f km im Mittel aus %d Läufen\n", s / n, n}' laeufe.csv
Anna: 7.10 km im Mittel aus 4 Läufen
```

Together, the three ran 80.2 km in nine runs, on average 8.91 km. For Anna (`km im Mittel aus 4 Läufen` is German for “km on average over 4 runs”), `awk` counts only the lines whose field 2 is exactly `Anna`; this excludes the header line automatically. Figure [32](#abb-32) recalculates her mean.

:::abbildung linux/k6mittel 32
Anna's mean distance: $(5.0 + 6.4 + 12.0 + 5.0) / 4$. First the sum grows step by step, 5.0, 11.4, 23.4, 28.4; then it is divided by the number of runs: $28.4 / 4 = 7.1$.
:::
::::

::::beispiel [Second example] A heading with BEGIN
```console
$ awk -F, 'BEGIN {print "Name km"} NR > 1 {print $2, $3}' laeufe.csv | head -n 3
Name km
Anna 5.0
Ben 10.5
```
::::

⁠**In short:** awk variables collect values over all lines and start at 0; `END` outputs the result after the last line, `printf` formats it.

### Collecting values by name: associative arrays

<span class="anker" id="stufe-9-5"></span>

Calculating the means for each person separately would mean running the program once each for Anna, Ben and Clara. With a hundred people, that no longer works. You need a variable that holds many values under different names. Figure [33](#abb-33) shows how it fills up during reading.

:::abbildung linux/k6array 33
On the left, the records come in one after another. On the right, a table with the columns key, `s` and `n`. Anna's first run creates the row Anna with 5.0 and 1, Ben's the row Ben, Clara's the row Clara; every further run increases the values in the row of its name. At the end, the table shows Anna 28.4 and 4, Ben 36.6 and 3, Clara 15.2 and 2.
:::

:::definition Definition 9.5 (Associative array)
<span class="anker" id="satz-9-5"></span>

An __associative array__ is a variable in `awk` that stores any number of values, each under a key of its own: `s["Anna"]` is the value under the key `Anna`. The key may be any text, including a field such as `$2`; a new key comes into being when it is first used, with the value 0 or the empty string like every new variable. `for (k in s)` executes a statement for each existing key, in an order that `awk` determines itself.
:::

Because the order is not fixed, you usually append a `sort`.

::::beispiel Runs and means per person
```console
$ awk -F, 'NR > 1 {n[$2]++} END {for (p in n) print n[p], p}' laeufe.csv | sort -rn
4 Anna
3 Ben
2 Clara
$ awk -F, 'NR > 1 {s[$2] += $3; n[$2]++} END {for (p in s) printf "%s %.2f %d\n", p, s[p] / n[p], n[p]}' laeufe.csv | sort
Anna 7.10 4
Ben 12.20 3
Clara 7.60 2
```

The first program counts the runs per person, the same result as the frequency table from subsection [3.6](sortieren-und-zahlen-sort-und-uniq.html#stufe-3-6). The second one collects the distances per person in `s` and the number of runs in `n` and divides at the end: Ben ran 12.2 km on average.
::::

⁠**In short:** An associative array stores values under keys such as `$2`; this is how `awk` collects sums and counters per group in a single pass.

:::hintergrund awk or sort and uniq?
Both ways count the runs per person. `sort | uniq -c` first has to order all lines so that identical names stand next to each other; for this, `sort` holds on to all lines or moves them out to temporary files. `awk` reads each line exactly once and remembers only one counter per key; its memory grows with the number of different names, not with the number of lines. On the other hand, an associative array has no order: internally, `awk` distributes the keys so that it can find each one again quickly, and `for (k in s)` goes through them in this internal arrangement. The gawk manual states explicitly that you cannot rely on this order. A `sort` afterward therefore provides ordered output, and it only has to deal with one line per person.
:::

### Exercises for Section [9](#stufe-9)

<span class="anker" id="stufe-9-6"></span>

:::aufgabe Exercise 25 ★ Outputting fields
<span class="anker" id="aufg-25"></span>

(a) For all runs over 40 minutes, output the name and the date, in this order. (b) Check that every line of `/etc/passwd` has the same number of fields separated by colons. (c) The last field of every line of `/etc/passwd` is the user's shell. Create a frequency table of these shells.

:::loesung
```console
$ awk -F, 'NR > 1 && $4 > 40 {print $2, $1}' laeufe.csv
Ben 2026-11-02
Clara 2026-11-03
Anna 2026-11-06
Clara 2026-11-07
Ben 2026-11-08
$ awk -F: '{print NF}' /etc/passwd | sort -u
7
$ awk -F: '{print $NF}' /etc/passwd | sort | uniq -c | sort -rn
     24 /usr/sbin/nologin
      2 /bin/bash
      1 /bin/sync
      1 /bin/false
```

(a) Unlike `cut`, `awk` writes the fields in any order you like. (b) Every line has seven fields; `sort -u` leaves only one value. (c) `$NF` is the last field. On the test system, 24 of the 28 accounts have `/usr/sbin/nologin`: these are accounts for services, which nobody is supposed to log in with. Only two have a shell for working, root and student; `/bin/sync` and `/bin/false` are not shells: one carries out a single task and ends, the other ends immediately. On your system, the numbers may be different.
:::
:::

:::aufgabe Exercise 26 ★★★ Means per person
<span class="anker" id="aufg-26"></span>

(a) For each person, calculate the mean time of a run in minutes, with one decimal place. (b) For each person, output their longest run in kilometers. Hint: a comparison with an array entry that has not been used yet compares with 0.

:::loesung
```console
$ awk -F, 'NR > 1 {m[$2] += $4; n[$2]++} END {for (p in m) printf "%s %.1f\n", p, m[p] / n[p]}' laeufe.csv | sort
Anna 40.0
Ben 73.7
Clara 42.5
$ awk -F, 'NR > 1 && $3 > max[$2] {max[$2] = $3} END {for (p in max) print p, max[p]}' laeufe.csv | sort
Anna 12.0
Ben 21.1
Clara 8.0
```

(a) As in the example from subsection [9.5](#stufe-9-5), only with field 4: Anna $160 / 4 = 40.0$, Ben $221 / 3 \approx 73.7$, Clara $85 / 2 = 42.5$ minutes. (b) The condition checks whether the distance is greater than the person's previous maximum; for a person's first run, there is no entry yet, and the comparison finds 0. Then the maximum is replaced. At the end, each person's longest run is left. `awk` writes the values as they were in the field, hence `12.0` and not `12`.
:::
:::

:::aufgabe Exercise 27 ★★ Number or text
<span class="anker" id="aufg-27"></span>

Predict how many lines the three commands output, and check it: (a) `awk -F, '$4 > 100' laeufe.csv`, (b) `awk -F, 'NR > 1 && $4 > 100' laeufe.csv`, (c) `awk -F, '$2 > "B"' laeufe.csv`. For each one, explain whether `awk` compares as a number or as text.

:::loesung
```console
$ awk -F, '$4 > 100' laeufe.csv
datum,name,km,minuten
2026-11-08,Ben,21.1,128
$ awk -F, 'NR > 1 && $4 > 100' laeufe.csv
2026-11-08,Ben,21.1,128
$ awk -F, '$2 > "B"' laeufe.csv | wc -l
6
```

(a) Two lines. In the header line, field 4 is `minuten`, not a number, so `awk` compares as text: m comes after 1 in the character order, so `minuten` is “greater” than `100`. In the other lines, field 4 is a number, and only 128 is greater than 100. (b) One line; `NR > 1` excludes the header line. (c) Six lines. A comparison with a text in quotes is always a text comparison. `Ben` is greater than `B`, because `B` is its beginning; `Clara` begins with C, which comes after B; `name` begins with a lowercase letter, and these come after all uppercase letters. `Anna` is smaller. So that makes three runs by Ben, two by Clara and the header line.
:::
:::

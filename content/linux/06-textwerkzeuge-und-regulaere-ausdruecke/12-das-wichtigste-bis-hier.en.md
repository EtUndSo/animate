---
title: Key points so far
pfad: Computer Science / Linux and the Command Line / Text Tools and Regular Expressions
adresse: informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke
knoten: Chapter 6: Text Tools and Regular Expressions
order: 6111200
summary: Selecting lines, cutting out columns, sorting, counting, transforming and calculating, and how to search for the form of a text instead of fixed words
tags: 
lang: en
---

:::kern Key points so far
<ul>

<li>

A table as text consists of records, one per line, and fields, separated by a separator; a CSV file separates with commas and often has a header line. Windows puts a carriage return before every newline, which `cat -A` shows as `^M` and `tr -d '\r'` removes.

</li>

<li>

`tail -n +2` removes the header line, `tail -f` follows a growing file. `cut -d, -f2` cuts out fields, `tr` replaces or deletes characters, `paste` puts columns side by side.

</li>

<li>

`sort` compares character by character, `-n` by numeric value, `-t, -k3,3` by one field; the locale determines the order, `LC_ALL=C` makes it the same everywhere. `uniq` compares only neighbors; `sort | uniq -c | sort -rn` counts frequencies.

</li>

<li>

`nl` numbers lines, `seq` generates sequences of numbers, `diff` uses `a`, `c` and `d` to show what differs between two files.

</li>

<li>

`grep` writes the lines with a match; `-i -v -c -n -o -r -l` change what it searches for and what it outputs.

</li>

<li>

A regular expression describes a set of strings: `.` any single character, `[…]` one from a list, `[[:digit:]]` a class, `^` and `$` start and end, `*` `+` `?` `{n,m}` repetitions, `( )` groups, `|` alternatives; `\` or `grep -F` take characters literally. The basic form needs a backslash before `{ }` and `( )`, `-E` turns on the extended form.

</li>

<li>

The match that begins furthest to the left wins, and from there the longest one. An expression checks form, not meaning. File name patterns are evaluated by the shell, regular expressions by the program; that is why expressions are put in single quotes.

</li>

<li>

`sed` edits a stream line by line: `s/expression/replacement/g` substitutes, `\1` inserts groups, line addresses select lines, `d` deletes, `-n` with `p` outputs. `sed -i` changes the file by way of a new file; a redirection into the same file empties it.

</li>

<li>

`awk` applies rules `condition {action}` to every line, knows the fields `$1` to `$NF` and the line number `NR`, calculates with decimal numbers, collects in variables and associative arrays and outputs the result in `END`.

</li>

</ul>
:::

:::merke The answer in three sentences
<ol>

<li>

You answer questions about a text file with small tools in a pipeline: select lines with `grep`, cut out columns with `cut`, order with `sort`, count with `uniq -c`, transform with `tr` and `sed`, calculate with `awk`.

</li>

<li>

Instead of fixed words, regular expressions describe the form of the strings you are looking for, with wildcards, selections, anchors, repetitions and alternatives.

</li>

<li>

The tools read line by line and character by character and know only characters, not meaning; their surprises follow from this, from `10` before `9` to the invisible carriage return.

</li>

</ol>
:::

**One principle behind all the results.** Almost everything in this chapter follows from two ideas. First: the tools see characters, not meaning. They read a stream line by line, compare character by character and do not know whether a sequence of digits is a number, a date or a name unless you tell them explicitly. Second: small tools that read text and write text can be combined into answers to questions that no one had in mind when any of them was built.

| Result | Where it comes from |
|---|---|
| `grep -c ',28$'` does not find the line in the Windows file | the carriage return stands before the newline (Sections [1](textdaten-datensatze-felder-und-zeilenenden.html#stufe-1) and [6](regulare-ausdrucke-zeichen-klassen-und-anker.html#stufe-6)) |
| `cut -f2` delivers whole lines | without `-d`, `cut` splits only at tabs (Section [2](spalten-ausschneiden-und-zeichen-ersetzen-cut-tr-und-paste.html#stufe-2)) |
| `tr a-z A-Z` leaves the ä lowercase | `tr` works byte by byte (Section [2](spalten-ausschneiden-und-zeichen-ersetzen-cut-tr-und-paste.html#stufe-2)) |
| `sort` puts `10` before `9` | comparison character by character (Section [3](sortieren-und-zahlen-sort-und-uniq.html#stufe-3)) |
| with `sort -n`, the header line comes first | text without a number counts as 0 (Section [3](sortieren-und-zahlen-sort-und-uniq.html#stufe-3)) |
| the same list sorts differently on another computer | the locale determines the order (Section [3](sortieren-und-zahlen-sort-und-uniq.html#stufe-3)) |
| `uniq -c` without `sort` counts each line separately | `uniq` compares only neighbors (Section [3](sortieren-und-zahlen-sort-und-uniq.html#stufe-3)) |
| `grep '5.0'` also finds `520` | the dot is any single character (Section [6](regulare-ausdrucke-zeichen-klassen-und-anker.html#stufe-6)) |
| `grep -c 'a*'` counts every line | the star allows zero repetitions (Section [7](regulare-ausdrucke-wiederholungen-gruppen-und-alternativen.html#stufe-7)) |
| `grep ',[0-9]{3}$'` finds nothing | in the basic form, `{ }` are ordinary characters (Section [7](regulare-ausdrucke-wiederholungen-gruppen-und-alternativen.html#stufe-7)) |
| `A.*km` reaches up to the last `km` | the longest match wins (Section [7](regulare-ausdrucke-wiederholungen-gruppen-und-alternativen.html#stufe-7)) |
| `2026-13-45` matches the expression for a date | an expression checks form, not meaning (Section [7](regulare-ausdrucke-wiederholungen-gruppen-und-alternativen.html#stufe-7)) |
| `grep -c Ann*` reports 0 | without quotes, the shell turns it into a pattern (Section [7](regulare-ausdrucke-wiederholungen-gruppen-und-alternativen.html#stufe-7)) |
| `sed … file > file` leaves an empty file | the shell empties it before the start, `sed -i` does not (Section [8](umformen-im-strom-sed.html#stufe-8)) |
| `awk '$3 > 10'` includes the header line | `km` is not a number and is compared as text (Section [9](rechnen-mit-spalten-awk.html#stufe-9)) |
| `for (p in n)` outputs in no particular order | an associative array has no order (Section [9](rechnen-mit-spalten-awk.html#stufe-9)) |

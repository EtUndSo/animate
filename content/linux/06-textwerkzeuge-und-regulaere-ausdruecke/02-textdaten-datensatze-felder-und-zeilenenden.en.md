---
title: Text data: records, fields and line ends
pfad: Computer Science / Linux and the Command Line / Text Tools and Regular Expressions
adresse: informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke
knoten: Chapter 6: Text Tools and Regular Expressions
order: 6110200
summary: Before you analyze data, you need to know how it is stored in a text file.
tags: record, fields, separator, column, CSV file, header line, carriage return
lang: en
---

<span class="anker" id="stufe-1"></span>

:::zweck
Before you analyze data, you need to know how it is stored in a text file. This section shows what a table looks like as text, creates the file that the whole chapter works with, explains why files from Windows have one invisible character more, and shows how to pick out parts of a file and watch a growing file as it grows.
:::

:::::vorwissen What you need for this: text file, filter, pipeline and quoting

<span class="anker" id="stufe-1-1"></span>

This chapter assumes [Chapters 1](/wissen/en/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/ein-linux-zum-ueben.html) to 5. From them, you mainly need the following.

<ul>

<li>

A text file consists only of characters and is divided into lines; each line ends with the line end, the byte 10, also called newline and written `\n`. A letter with an umlaut takes up two bytes in UTF-8 ([Chapter 3, Section 4.1](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-ansehen.html#stufe-4-1)). `cat` outputs files, `head` and `tail` show the beginning and the end, `wc` counts lines, words and bytes, `file` determines the type of a file ([Chapter 3, Sections 4.2](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-ansehen.html#stufe-4-2) to 4.6).

</li>

<li>

A program reads its standard input and writes to its standard output. `>` redirects the output into a file, `<` takes the input from a file, a here document supplies several typed lines as input ([Chapter 4, Sections 2.1](/wissen/en/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/ausgaben-umleiten.html#stufe-2-1), 3.1 and 3.2). If you write with `>` into the same file you are reading from, you find it empty: the truncation trap ([Chapter 4, Section 2.7](/wissen/en/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/ausgaben-umleiten.html#stufe-2-7)).

</li>

<li>

A pipe `|` connects the output of one program to the input of the next. A filter reads its standard input, transforms it and writes out the result; several filters in a row form a pipeline ([Chapter 4, Sections 4.1](/wissen/en/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/pipes-und-filter.html#stufe-4-1) to 4.3). You saw `sort`, `uniq`, `grep` and `tr` there in their simplest form. Every command reports with its exit status whether it succeeded; `$?` shows it ([Chapter 4, Sections 5.1](/wissen/en/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/der-exit-status.html#stufe-5-1) and [5.2](/wissen/en/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/der-exit-status.html#stufe-5-2)).

</li>

<li>

`printf` writes text according to a format; `%s` stands for the next argument, and the format is repeated as long as arguments remain ([Chapter 5, Section 3.1](/wissen/en/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/worttrennung-und-quoting.html#stufe-3-1)). Between single quotes, the shell takes every character literally ([Chapter 5, Section 3.4](/wissen/en/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/worttrennung-und-quoting.html#stufe-3-4)). `$(command)` inserts the output of a command, `$((…))` the result of a calculation with whole numbers ([Chapter 5, Sections 2.3](/wissen/en/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/variablen-befehlsersetzung-und-arithmetik.html#stufe-2-3) and [2.4](/wissen/en/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/variablen-befehlsersetzung-und-arithmetik.html#stufe-2-4)). `NAME=value command` sets a variable for this one command only ([Chapter 5, Section 4.6](/wissen/en/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/umgebung-und-vererbung.html#stufe-4-6)).

</li>

<li>

Ctrl+C aborts a running program ([Chapter 2, Section 5.4](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/schneller-arbeiten-vervollstandigung-verlauf-tastenkurzel.html#stufe-5-4)). With the prefix `gnu`, you call the GNU implementation of a core command under Ubuntu 26.04, such as `gnusort` ([Chapter 2, Section 7.3](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/zwei-fassungen-der-grundbefehle-gnu-und-uutils.html#stufe-7-3)).

</li>

</ul>

⁠**In short:** You need text files and line ends, the commands from [Chapter 3](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-verzeichnisse-und-pfade.html) for viewing files, redirection, pipe and filter, `printf`, single quotes and calculation with `$((…))`.

:::warnung Only in your own practice directory
Some commands in this chapter create files, change them or empty them. So create a practice directory of your own and work there:

```console
$ mkdir ~/linuxk6
$ cd ~/linuxk6
```

All file names in the examples refer to this directory.
:::

:::::

### Record and field

<span class="anker" id="stufe-1-2"></span>

After every run, a running club writes down when, who, how far and how long someone ran. On paper or in a spreadsheet program, this would be a table with rows and columns. A text file, however, knows no boxes, only characters and line ends. Figure [1](#abb-1) shows how a table still fits into a text file.

:::abbildung linux/k6tabelle 1
At the top, a small table with the columns date, name, distance in kilometers and time in minutes. Below, the same values as text: each row of the table becomes a line of the file, and the values of a row stand one after the other, separated by commas. The commas light up, then the four values of the line `2026-11-02,Ben,10.5,62` get their numbers 1 to 4.
:::

:::definition Definition 1.1 (Record, field)
<span class="anker" id="satz-1-1"></span>

A __record__ is a line of a text file that contains the values of one table row. Its individual values are called __fields__; they stand one after the other in a fixed order. Between any two fields there is an agreed character, the __separator__. The fields of a record are counted from the left, starting with 1.
:::

Whoever writes the file decides which character separates; common choices are the comma, the semicolon, the colon and the tab. A separator must not occur in the values themselves; otherwise it would no longer be clear where a field ends. The fields with the same number in all records together form a __column__.

::::beispiel A record taken apart
In the record `2026-11-02,Ben,10.5,62`, three commas separate four fields. Field 1 is the date `2026-11-02`, field 2 the name `Ben`, field 3 the distance `10.5` in kilometers and field 4 the time `62` in minutes. Decimal numbers are written with a decimal point, the way most programs write them; with a decimal comma, as in `10,5`, the comma could not be told apart from a separator. The user list `/etc/passwd` from [Chapter 3, Section 4.4](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-ansehen.html#stufe-4-4) also consists of records; there, a colon separates the seven fields.
::::

⁠**In short:** A line with the values of a table row is a record; its values are the fields, separated by a separator and counted from the left.

### The CSV file and its header line

<span class="anker" id="stufe-1-3"></span>

For tables in text form, there is a format that almost every program can read and write, from spreadsheet programs to online banking. In this format, you now create the running log that the chapter works with until the end.

:::definition Definition 1.2 (CSV file, header line)
<span class="anker" id="satz-1-2"></span>

A __CSV file__ is a text file in which each line is a record and the comma separates the fields. The name stands for “comma-separated values”. Often the first line contains the names of the columns instead of values; it is called the __header line__.
:::

The header line is meant for people and for programs that address columns by their names. The tools in this chapter treat it like any other line; where it gets in the way, you remove it beforehand.

You create the running log with a here document from [Chapter 4, Section 3.2](/wissen/en/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/eingaben-umleiten.html#stufe-3-2). Type the first line, then the ten lines of the table and finally `ENDE` (German for “end”); the shell shows a `>` before each continuation line:

```console
$ cat > laeufe.csv <<ENDE
> datum,name,km,minuten
> 2026-11-02,Anna,5.0,28
> 2026-11-02,Ben,10.5,62
> 2026-11-03,Clara,7.2,41
> 2026-11-04,Anna,6.4,35
> 2026-11-05,Ben,5.0,31
> 2026-11-06,Anna,12.0,70
> 2026-11-07,Clara,8.0,44
> 2026-11-08,Ben,21.1,128
> 2026-11-09,Anna,5.0,27
> ENDE
$ head -n 3 laeufe.csv
datum,name,km,minuten
2026-11-02,Anna,5.0,28
2026-11-02,Ben,10.5,62
```

The file `laeufe.csv` (German for “runs”) has a header line, `datum,name,km,minuten` (German for “date,name,km,minutes”), and nine records: nine runs by Anna, Ben and Clara between 2 and 9 November 2026. The date has the form year-month-day so that it sorts correctly as text.

⁠**In short:** A CSV file is a table as text with one record per line and commas between the fields; the first line often names the columns.

:::hintergrund Why CSV does not look the same everywhere
There is no binding standard for CSV, only a description that appeared in 2005 as RFC 4180 and records widespread practice. According to it, a field that itself contains a comma, a quotation mark or a line end may be enclosed in double quotes, for example `"Berg, Anna"`. The simple tools in this chapter do not know this rule; for them, every comma is a separator. For files with such fields, there are dedicated programs that understand CSV completely. Spreadsheet programs set to German often separate with semicolons when saving as CSV, because there the comma is the decimal separator. So if you analyze a CSV file from someone else, first look into it with `head` to see which separator it uses and whether fields are enclosed in quotes.
:::

### The line end under Windows

<span class="anker" id="stufe-1-4"></span>

CSV files often come from a Windows computer, from a spreadsheet program or from a download. Such files look completely normal in the terminal and still sometimes behave strangely. The reason is a character that you cannot see. Figure [2](#abb-2) shows it.

:::abbildung linux/k6zeilenende 2
The end of the line `2026-11-02,Anna,5.0,28` as bytes, at the top in a Linux file, at the bottom in a Windows file. Up to the 8, both are the same (gray). After that, under Linux only the newline 10 follows; under Windows, it is preceded by the carriage return 13, which lights up. For a program that reads up to the newline, it belongs to the last field: the program reads `28` and an invisible character.
:::

:::definition Definition 1.3 (Carriage return, Windows line end)
<span class="anker" id="satz-1-3"></span>

The __carriage return__ is an invisible character with the value 13, often written `\r` in programs. In text files, Windows ends every line with two bytes, the carriage return and the newline, that is, 13 and 10. Linux and the other Unix systems use only the newline.
:::

A Linux program takes the carriage return for an ordinary character at the end of the line. That is why it belongs to the last field of a record and causes trouble as soon as a tool compares this field with a value or searches for something that is supposed to stand directly before the line end.

You create a small file with Windows line ends using `printf`. The format `'%s\r\n'` writes each argument, a carriage return and a newline; `printf` applies it to each of the three arguments. The command `cat` with the option `-A` makes invisible characters visible: it writes the carriage return as `^M` and puts a `$` at every line end.

```console
$ printf '%s\r\n' datum,name,km,minuten 2026-11-02,Anna,5.0,28 2026-11-02,Ben,10.5,62 > windows.csv
$ cat windows.csv
datum,name,km,minuten
2026-11-02,Anna,5.0,28
2026-11-02,Ben,10.5,62
$ cat -A windows.csv
datum,name,km,minuten^M$
2026-11-02,Anna,5.0,28^M$
2026-11-02,Ben,10.5,62^M$
```

Without `-A`, the file looks like the first three lines of `laeufe.csv`. Only `cat -A` reveals the carriage return before every line end. For comparison, save the first three lines of the running log in a file of their own and count the bytes:

```console
$ head -n 3 laeufe.csv > drei.csv
$ wc -c drei.csv windows.csv
 68 drei.csv
 71 windows.csv
139 total
```

Three lines, three bytes more: one carriage return per line.

::::beispiel The bytes one by one
`od -c` from [Chapter 3, Section 4.1](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-ansehen.html#stufe-4-1) shows each byte as a character; it writes the carriage return as `\r`:

```console
$ od -An -c windows.csv | head -n 2
   d   a   t   u   m   ,   n   a   m   e   ,   k   m   ,   m   i
   n   u   t   e   n  \r  \n   2   0   2   6   -   1   1   -   0
```

After `minuten` come `\r` and `\n`, then the next line begins. And `file`? It considers both files CSV and reveals nothing here:

```console
$ file laeufe.csv windows.csv
laeufe.csv:  CSV ASCII text
windows.csv: CSV ASCII text
```

For an ordinary text file, such as a short greeting, by contrast, `file` reports Windows line ends with the addition “with CRLF line terminators”. For CSV files, therefore, rely on `cat -A`.
::::

⁠**In short:** Windows ends lines with a carriage return and a newline; under Linux, the invisible carriage return becomes the last character of every line, and `cat -A` shows it as `^M`.

:::hintergrund Why there are two characters and Linux manages with one
The names come from teleprinters, on which the first computers printed their output. The carriage return (CR for short) moved the print head back to the start of the line, and the line feed (LF for short, our newline) advanced the paper by one line. For a new line, the device needed both. Windows took over this pairing from its predecessors and stores it in every file. Unix went a different way: the file contains only one character, and only the terminal driver turns it into what the device needs when writing output. This translation is still a setting of the terminal today:

```console
$ stty -a | grep onlcr
opost -olcuc -ocrnl onlcr -onocr -onlret -ofdel nl0 cr0 tab0 bs0 vt0 ff0
```

`onlcr` without a minus in front means: on output (o for “output”), every newline (nl for “newline”) becomes a carriage return followed by a newline (cr for “carriage return”, then nl). Files thus stay shorter and simpler, and every program needs to know only one character as the line end.
:::

### From a given line on: tail -n +K and head -n -K

<span class="anker" id="stufe-1-5"></span>

The header line gets in the way as soon as you want to count or calculate: it is not a run. `head -n K` and `tail -n K` from [Chapter 3, Section 4.4](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-ansehen.html#stufe-4-4) take a fixed number of lines at the beginning or at the end. What is needed, however, is “everything from line 2 on”, no matter how long the file is. Figure [3](#abb-3) shows how a sign reverses the direction of counting.

:::abbildung linux/k6ausschnitt 3
The ten lines of the running log twice as a stack. Left, `tail -n +8`: it counts from the beginning up to line 8 and takes everything from there on, lines 8 to 10. Right, `head -n -7`: it counts off seven lines from the end and takes everything before them, lines 1 to 3.
:::

:::definition Definition 1.4 (tail -n +K, head -n -K)
<span class="anker" id="satz-1-4"></span>

`tail -n +K` writes all lines from line number $K$ to the end. `head -n -K` writes all lines except the last $K$.
:::

So the plus sign turns “the last $K$ lines” into “from line $K$ on”, and the minus sign turns “the first $K$ lines” into “all but the last $K$”. `tail -n +2` is therefore the usual way to cut off a header line.

::::beispiel Counting runs, beginning and end
```console
$ wc -l laeufe.csv
10 laeufe.csv
$ tail -n +2 laeufe.csv | wc -l
9
$ tail -n +8 laeufe.csv
2026-11-07,Clara,8.0,44
2026-11-08,Ben,21.1,128
2026-11-09,Anna,5.0,27
$ head -n -7 laeufe.csv
datum,name,km,minuten
2026-11-02,Anna,5.0,28
2026-11-02,Ben,10.5,62
```

The file has ten lines; without the header line, nine runs remain. `tail -n +8` returns lines 8 to 10, `head -n -7` lines 1 to 3.
::::

⁠**In short:** `tail -n +K` starts at line $K$, `head -n -K` stops $K$ lines before the end; `tail -n +2` removes a header line.

### Following a growing file: tail -f

<span class="anker" id="stufe-1-6"></span>

Some files grow while you read them: logs into which a program writes its messages, or a diary to which someone appends new entries. You then do not want to call `tail` again and again; you want to see what is added as soon as it is added. Figure [4](#abb-4) shows what the option does for this.

:::abbildung linux/k6tailf 4
Left, a file as a stack of lines; right, the terminal with `tail -n 2 -f`. First the last two lines appear, then `tail` waits. At the bottom, a new line is appended to the file; it appears in the terminal immediately as well. Only Ctrl+C ends the waiting.
:::

:::definition Definition 1.5 (tail -f)
<span class="anker" id="satz-1-5"></span>

`tail -f file` first writes the last lines of the file as usual. After that, it does not end but waits and writes everything that is later appended to the file as soon as it arrives there. It runs until you abort it with Ctrl+C.
:::

The letter stands for “follow”. So that the running log itself stays unchanged, you try it out on a copy:

```console
$ cp laeufe.csv neu.csv
```

In the first terminal, start `tail` with the last two lines. Then open a second terminal window, change to the practice directory there with `cd ~/linuxk6` and append a new run:

```console
$ echo 2026-11-10,Clara,6.0,33 >> neu.csv
```

In the first terminal, the new line appears immediately below the two old ones. Then end `tail` with Ctrl+C:

```console
$ tail -n 2 -f neu.csv
2026-11-08,Ben,21.1,128
2026-11-09,Anna,5.0,27
2026-11-10,Clara,6.0,33
^C
```

The first two lines were already in the file; the third came from the second terminal. `neu.csv` (German for “new”) now has one run more than `laeufe.csv`.

⁠**In short:** `tail -f` shows the end of a file and then everything that is appended, until Ctrl+C.

:::hintergrund How tail notices that something is added
Under Linux, both implementations of `tail` on the test system ask the kernel to notify them as soon as the file changes; the output then comes without delay. Where that is not possible, the GNU implementation checks once per second whether the file has grown. For log files, there is a subtlety: many systems rename a full log file at regular intervals and start a new one under the old name. `tail -f` follows the file it has opened and then gets stuck on the renamed old one. `tail -F`, by contrast, follows the name and opens the new file as soon as it appears.
:::

### Exercises for Section [1](#stufe-1)

<span class="anker" id="stufe-1-7"></span>

:::aufgabe Exercise 1 ★ Measuring the running log
<span class="anker" id="aufg-1"></span>

(a) How many lines and how many bytes does `laeufe.csv` have? Use a single call of `wc`. (b) Output lines 4 to 6, once with `head` before `tail` and once the other way around. (c) How many bytes would the file have if it had Windows line ends? Give your reasoning without the computer.

:::loesung
```console
$ wc -l -c laeufe.csv
 10 232 laeufe.csv
$ head -n 6 laeufe.csv | tail -n 3
2026-11-03,Clara,7.2,41
2026-11-04,Anna,6.4,35
2026-11-05,Ben,5.0,31
$ tail -n +4 laeufe.csv | head -n 3
2026-11-03,Clara,7.2,41
2026-11-04,Anna,6.4,35
2026-11-05,Ben,5.0,31
```

(a) Ten lines and 232 bytes; `wc` writes the numbers in the order lines, bytes, regardless of the order of the options. (b) First way: `head -n 6` keeps lines 1 to 6, and `tail -n 3` keeps the last three of them, that is, 4 to 6. Second way: `tail -n +4` begins at line 4, and `head -n 3` keeps three lines. (c) Each of the ten lines would get a carriage return before its line end, that is, one byte more: $232 + 10 = 242$ bytes. It was the same with `drei.csv` and `windows.csv` in subsection [1.4](#stufe-1-4): three lines, three bytes more.
:::
:::

:::aufgabe Exercise 2 ★★ Recognizing Windows line ends
<span class="anker" id="aufg-2"></span>

Use `printf` to create a file `gruss.txt` (German for “greeting”) with the two lines `Hallo` and `Welt` (“hello”/“world”) in Windows format. (a) Predict how many bytes `wc -c` reports. (b) Check with `cat -A` and `od -An -c`. (c) What does `file` report for this file?

:::loesung
```console
$ printf 'Hallo\r\nWelt\r\n' > gruss.txt
$ wc -c gruss.txt
13 gruss.txt
$ cat -A gruss.txt
Hallo^M$
Welt^M$
$ od -An -c gruss.txt
   H   a   l   l   o  \r  \n   W   e   l   t  \r  \n
$ file gruss.txt
gruss.txt: ASCII text, with CRLF line terminators
```

(a) `Hallo` has 5 characters, `Welt` has 4, and each line ends with two bytes: $5 + 2 + 4 + 2 = 13$. (b) `cat -A` shows a `^M` before each `$`, and `od` shows the bytes `\r` and `\n` one by one. (c) For this ordinary text file, `file` explicitly mentions the Windows line ends, unlike for the CSV file in subsection [1.4](#stufe-1-4).
:::
:::

:::aufgabe Exercise 3 ★★ Following a file
<span class="anker" id="aufg-3"></span>

Copy `laeufe.csv` to `probe.csv` (German for “test”). (a) Start `tail -n 0 -f probe.csv`. What appears immediately, and why? (b) Append two runs in the second terminal. What does the first terminal show? (c) Why does `tail -f` not end on its own when the end of the file is reached, whereas `tail` without `-f` does?

:::loesung
In the first terminal, you start `tail -n 0 -f probe.csv`; in the second, you append two runs:

```console
$ echo 2026-11-10,Ben,8.4,49 >> probe.csv
```

```console
$ echo 2026-11-10,Anna,5.0,26 >> probe.csv
```

After that, until you press Ctrl+C, the first terminal shows:

```console
$ cp laeufe.csv probe.csv
$ tail -n 0 -f probe.csv
2026-11-10,Ben,8.4,49
2026-11-10,Anna,5.0,26
^C
```

(a) Nothing appears immediately: `-n 0` asks for zero of the existing lines. (b) Each appended line appears as soon as it is in the file. (c) `tail` without `-f` reads up to the end of the file, writes the last lines and is done. `tail -f` expects that something will still be appended at the end; for it, the end of the file is only where things stand right now. It cannot know when nobody is writing anymore, so only Ctrl+C ends the waiting.
:::
:::

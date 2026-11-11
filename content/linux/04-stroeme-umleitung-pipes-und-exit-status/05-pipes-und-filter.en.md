---
title: Pipes and filters
pfad: Computer Science / Linux and the Command Line / Streams, Redirection, Pipes and Exit Status
adresse: informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status
knoten: Chapter 4: Streams, Redirection, Pipes and Exit Status
order: 6090500
summary: So far, the output of a program has led to the screen or into a file.
tags: pipe, filter, pipeline, tee, Unix philosophy
lang: en
---

<span class="anker" id="stufe-4"></span>

:::zweck
So far, the output of a program has led to the screen or into a file. This section connects the standard output of one program directly to the standard input of another. It explains the pipe, the programs that are suited to such connections, chains of many programs, a branch that captures an intermediate result and the principle by which Unix programs are built.
:::

### The pipe

<span class="anker" id="stufe-4-1"></span>

How many programs are there in `/usr/bin`? `ls` can list them, and `wc -l` can count lines. With what Sections [2](ausgaben-umleiten.html#stufe-2) and [3](eingaben-umleiten.html#stufe-3) have shown, this works by way of an intermediate file:

```console
$ ls /usr/bin > liste.txt
$ wc -l < liste.txt
1018
$ rm liste.txt
```

That is three commands and a file that you have to delete again afterward. It would be more convenient to plug the standard output of `ls` directly into the standard input of `wc`. Figure [14](#abb-14) shows this connection.

:::abbildung linux/k4pipe 14
The pipe `ls /usr/bin | wc -l`: Both processes are running at the same time. What `ls` writes to descriptor 1 collects in a buffer in the kernel, from which `wc` reads through descriptor 0. At the end, `wc` writes the number 1018 to the screen.
:::

:::definition Definition 4.1 (Pipe)
<span class="anker" id="satz-4-1"></span>

A __pipe__ connects the standard output of one process to the standard input of another. The notation `command1 | command2` tells the shell to start both programs at the same time, each in a process of its own, and to connect descriptor 1 of the first to descriptor 0 of the second. The bytes pass through a buffer in the kernel, not through a file.
:::

The character `|` is called a vertical bar; on a US keyboard, you type it with Shift and the backslash key, on a German keyboard with AltGr+<. As with a redirection, the two programs notice nothing of the connection: `ls` writes to descriptor 1, and `wc` reads from descriptor 0.

::::beispiel Counting the programs in /usr/bin
```console
$ ls /usr/bin | wc -l
1018
```

The same number as by way of the intermediate file, with a single command and without a file. On your computer, the number depends on what is installed.
::::

The shell connects the pipe before it carries out the redirections of the individual commands. If the first command itself has a redirection, such as `ls > liste.txt | wc -l`, this redirection therefore takes effect after the pipe and wins: descriptor 1 then leads into the file, and nothing comes through the pipe.

A pipe connects only descriptor 1 to descriptor 0. Standard error of the first program still leads to the screen. If it is to go through the pipe as well, you write `2>&1` as the last redirection before the `|`. bash has the short form `|&` for this; it works exactly as if `2>&1` stood after all redirections of the first command, immediately before the `|`. Figure [15](#abb-15) shows both cases.

:::abbildung linux/k4pipefehler 15
Top, `ls /gibtsnicht | wc -l`: The message from `ls` goes through descriptor 2 past the pipe to the screen, nothing comes through the pipe, and `wc` counts 0. Bottom, with `|&`: Descriptor 2 also leads into the pipe, and `wc` counts the message as one line.
:::

::::beispiel [Second example] The message goes past the pipe
```console
$ ls /gibtsnicht | wc -l
ls: cannot access '/gibtsnicht': No such file or directory
0
$ ls /gibtsnicht |& wc -l
1
```

On the first call, `wc` counts zero lines, because nothing came through the pipe; the message appears on the screen. On the second, the message came through the pipe, and `wc` counts it as one line. This is exactly why standard error is separate: messages are not supposed to end up in the data of the next program.
::::

⁠**In short:** `command1 | command2` connects the standard output of the first program to the standard input of the second; both run at the same time, and the messages still go to the screen.

:::warnung Do not confuse > and |
`>` connects a program to a file, `|` to another program. If you type `ls > wc`, you do not start `wc`; instead, the output of `ls` goes into a file named `wc`. If a file of that name already existed there, it would be overwritten:

```console
$ ls > wc
$ ls
alles.txt   einkauf.txt  gruss.txt   leer.txt  obst.txt   probe2.txt
beides.txt  fehler.txt   inhalt.txt  nur.txt   probe.txt  wc
$ rm wc
```

In a directory full of programs such as `/usr/bin`, the same typo made as root ([Chapter 2, Section 1.4](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/terminal-und-shell.html#stufe-1-4)) could destroy a program of the system.
:::

:::hintergrund How a pipe works in the kernel
A pipe is a buffer in the kernel with two ends, one for writing and one for reading; on Linux, it usually holds 65 536 bytes. The shell creates the pipe before it starts the two programs and gives each process the matching end as descriptor 1 or 0, respectively. After that, the kernel manages the traffic: if the buffer is empty, the reader waits until bytes arrive; if it is full, the writer waits until the reader has made room. In this way, both programs run at the same time, and even a huge output never needs more than this small buffer. Once the writer has closed its end, for example because it is finished, and the buffer is empty, the next read request returns zero bytes: the reader sees the end of the stream. Conversely, if a writer wants to write into a pipe that nobody reads anymore, the kernel ends it with an interrupt message ([Chapter 2, Section 5.4](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/schneller-arbeiten-vervollstandigung-verlauf-tastenkurzel.html#stufe-5-4)). That is why the following pipeline ends, even though the command `yes` writes lines containing `y` without end:

```console
$ yes | head -n 3
y
y
y
```

`head` stops after three lines and thereby closes the read end; at the next attempt to write, the kernel ends `yes`.
:::

:::hintergrund Where the pipe comes from
The idea is older than Unix. In 1964, Doug McIlroy wrote in a memo at Bell Labs that it should be possible to connect programs like a garden hose, screwing in another segment when the data is to be processed in another way. It was put into practice only in 1972 or 1973, when Ken Thompson added the system call for the pipe to Unix in a single night; the sources give different years. The first notation still used the same characters as redirection and lasted only a few months; then came the vertical bar. Dennis Ritchie saw the stroke of genius in the fact that a pipeline consists of exactly the programs that you use individually every day anyway.
:::

### The filter

<span class="anker" id="stufe-4-2"></span>

Not every program fits behind a pipe. `wc` fits, because it reads its standard input when it does not get a file name. `ls`, on the other hand, never reads its standard input; whatever you send it through a pipe never arrives. Programs of the first kind have a name of their own. Figure [16](#abb-16) shows four of them on the same input.

:::abbildung linux/k4filter 16
Four filters, the same input: the seven lines of the fruit list. `sort` sorts them, `head -n 2` keeps the first two, `grep Apfel` keeps only the lines with `Apfel`, and `uniq` changes nothing here, because no two equal lines are directly next to each other.
:::

:::definition Definition 4.2 (Filter)
<span class="anker" id="satz-4-2"></span>

A __filter__ is a program that reads data from its standard input, transforms it and writes the result to its standard output. Most filters read files instead if you give them their names as arguments.
:::

This chapter uses the following filters, each of them here only in its simplest form:

<ul>

<li>

`sort` sorts the lines;

</li>

<li>

`head -n number` keeps the first lines ([Chapter 3, Section 4.4](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-ansehen.html#stufe-4-4));

</li>

<li>

`wc` counts lines, words and bytes ([Chapter 3, Section 4.5](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-ansehen.html#stufe-4-5));

</li>

<li>

`grep word` keeps only the lines in which `word` occurs;

</li>

<li>

`uniq` keeps only one of several equal lines that are directly next to each other;

</li>

<li>

`tr` replaces characters (subsection [3.3](eingaben-umleiten.html#stufe-3-3)).

</li>

</ul>

`ls`, `echo`, `mkdir`, `cp` and `rm` are not filters: they do not read any data from their standard input.

::::beispiel Four filters on the fruit list
```console
$ sort obst.txt
Apfel
Apfel
Apfel
Banane
Birne
Birne
Kiwi
$ head -n 2 obst.txt
Apfel
Birne
$ grep Apfel obst.txt
Apfel
Apfel
Apfel
$ uniq obst.txt
Apfel
Birne
Apfel
Kiwi
Banane
Apfel
Birne
```

`uniq` has kept all seven lines, because nowhere in the fruit list are two equal lines directly next to each other.
::::

::::beispiel [Second example] A filter reads its standard input
Here `sort` gets no file name; the fruit list arrives through the redirection from subsection [3.1](eingaben-umleiten.html#stufe-3-1), and the result goes through a pipe to `head`:

```console
$ sort < obst.txt | head -n 2
Apfel
Apfel
```
::::

⁠**In short:** A filter reads its standard input, transforms it and writes the result to its standard output; that is why it fits behind a pipe.

### The pipeline

<span class="anker" id="stufe-4-3"></span>

How many different kinds of fruit are on the list? This takes three steps: sort the lines so that equal ones are next to each other, delete the repetitions and count the remaining lines. Each step is a filter, and the filters can be plugged together one after the other like the stations of an assembly line. Figure [17](#abb-17) shows the assembly line with the intermediate result after each station.

:::abbildung linux/k4fliessband 17
The pipeline `sort obst.txt | uniq | wc -l` as an assembly line. Under each pipe is what is flowing through it: after `sort` the seven sorted lines, after `uniq` the four kinds and at the end the number 4.
:::

:::definition Definition 4.3 (Pipeline)
<span class="anker" id="satz-4-3"></span>

A __pipeline__ is a sequence of commands connected by `|`. The shell starts all commands at the same time, each in a process of its own, and connects the standard output of each command to the standard input of the next. The standard output of the last command leads where it would have led without a pipeline; it can be redirected like any other.
:::

To the shell, a single command without `|` is also a pipeline, one with only one stage. The order of the stages matters: `uniq` compares each line only with the one directly before it, so `sort` has to bring equal lines together first.

::::beispiel The kinds on the fruit list
```console
$ sort obst.txt | uniq
Apfel
Banane
Birne
Kiwi
$ sort obst.txt | uniq | wc -l
4
```

The first pipeline shows the four kinds, each once. The second appends `wc -l` and answers the question with a number. Without `sort`, `uniq` would have deleted nothing, as the example in subsection [4.2](#stufe-4-2) showed, and `wc -l` would have counted 7.
::::

The simplest way to bring a file to the start of a pipeline is to give its name to the first filter as an argument, as in `sort obst.txt`, or to use `<`. The notation `cat obst.txt | sort` also works, but it starts one more process that only passes the data on.

⁠**In short:** A pipeline lines up filters like the stations of an assembly line; each station works with what the previous one delivers.

### The branch: tee

<span class="anker" id="stufe-4-4"></span>

Sometimes you want to keep an intermediate result of a pipeline and still process it further, for example save the list of kinds and count them at the same time. This would not work with `>`, because then nothing would arrive at the next filter anymore. What is needed is a branch in the line, as Figure [18](#abb-18) shows.

:::abbildung linux/k4tee 18
`tee` as a T-piece in the line: What arrives from the left flows on unchanged to the right to the next filter and at the same time down into the file `sorten.txt` (German for “kinds”).
:::

:::definition Definition 4.4 (tee)
<span class="anker" id="satz-4-4"></span>

The command __tee__ reads its standard input and writes everything it reads both to its standard output and to every file named as an argument. It creates these files or empties them first; with the option `-a`, it appends.
:::

The name comes from the T-piece in plumbing, called a *tee*, which splits one stream into two paths.

::::beispiel Saving and counting the kinds
```console
$ sort obst.txt | uniq | tee sorten.txt | wc -l
4
$ cat sorten.txt
Apfel
Banane
Birne
Kiwi
```

`wc -l` counted the four lines that `tee` passed on; the same four lines are in `sorten.txt`.
::::

⁠**In short:** `tee file` passes its input on unchanged and at the same time writes a copy into the file.

### The Unix philosophy

<span class="anker" id="stufe-4-5"></span>

Why is there no program “count kinds of fruit”, but three small ones that you have to connect? Behind this way of building lies a principle that has shaped the tools of Unix and Linux since the 1970s.

:::definition Definition 4.5 (Unix philosophy)
<span class="anker" id="satz-4-5"></span>

The __Unix philosophy__ is a principle for building programs. Each program should do one thing well. Programs should read and write text, without unnecessary extras, so that the output of every program can become the input of another. You solve new tasks by connecting existing programs instead of writing a big new one.
:::

The advantage shows as soon as the question changes. Connected in new ways, the same small programs answer completely different questions for which nobody has written a program of its own.

::::beispiel New questions, old programs
How often is `Apfel` on the fruit list, and how many entries does the shopping list have?

```console
$ grep Apfel obst.txt | wc -l
3
$ wc -l < einkauf.txt
5
```

`grep` searches, `wc` counts; neither of the two knows anything about fruit or shopping. For this to work, filters write only their data and no headings or notices in between that the next filter would take for data.
::::

⁠**In short:** Small programs that do one thing well and read and write text can be connected into ever new tool chains.

:::hintergrund The principle in the original
In 1978, Doug McIlroy and two colleagues wrote down a few rules of style in the foreword to a collection of papers on Unix; to this day, they are regarded as the core of the Unix philosophy. In essence, they say: Each program should do one thing well; for a new task, it is better to build a new program than to overload an old one with additional features. You should expect the output of every program to become the input of another one that does not even exist yet; therefore, no extraneous information in the output, no input formats with rigid columns or made of binary data, and no program should insist on getting its input in a dialog with a person. Many peculiarities that came up in this chapter follow from this: into a file, `ls` writes one name per line and no columns; messages go into a stream of their own; and the programs are small enough to be combined in one line. The common language is text in lines: every program that reads lines and writes lines can be connected to every other program of this kind.
:::

### Exercises for Section [4](#stufe-4)

<span class="anker" id="stufe-4-6"></span>

:::aufgabe Exercise 13 ★★ Building pipelines
<span class="anker" id="aufg-13"></span>

(a) How many entries do `/usr/sbin` and `/etc` have? Write one pipeline for each. (b) Which five files in `/usr/bin` are the largest? Use `ls -S` from [Chapter 3, Section 3.6](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/den-inhalt-eines-verzeichnisses-anzeigen.html#stufe-3-6) and `head`. (c) Extend (b) so that the five names also end up in the file `gross.txt` (German for “large”) and only their number appears on the screen.

:::loesung
```console
$ ls /usr/sbin | wc -l
176
$ ls /etc | wc -l
174
$ ls -S /usr/bin | head -n 5
x86_64-linux-gnu-lto-dump-15
snap
shellcheck
coreutils
gdb
$ ls -S /usr/bin | head -n 5 | tee gross.txt | wc -l
5
$ cat gross.txt
x86_64-linux-gnu-lto-dump-15
snap
shellcheck
coreutils
gdb
```

(a) On the test system, 176 and 174 entries; on your computer, the numbers depend on what is installed. Without `-a`, `ls` does not count hidden entries. (b) `ls -S` sorts by size, largest first, and `head -n 5` keeps the first five. That `coreutils` is among them fits [Chapter 2, Section 7.2](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/zwei-fassungen-der-grundbefehle-gnu-und-uutils.html#stufe-7-2): this one file contains all the core commands of the uutils implementation. (c) `tee` writes the five names into `gross.txt` and passes them on to `wc -l`, which shows only the count on the screen.
:::
:::

:::aufgabe Exercise 14 ★★ What flows through the pipes?
<span class="anker" id="aufg-14"></span>

For `sort obst.txt | uniq | head -n 2`, write down what flows through the first pipe, what flows through the second and what appears at the end. What changes if you swap `sort` and `uniq`?

:::loesung
Through the first pipe flow the seven lines of the fruit list, sorted: `Apfel` three times, `Banane`, `Birne` twice, `Kiwi`. `uniq` removes the repetitions; through the second pipe flow `Apfel`, `Banane`, `Birne`, `Kiwi`. `head -n 2` keeps the first two.

```console
$ sort obst.txt | uniq | head -n 2
Apfel
Banane
$ uniq obst.txt | sort
Apfel
Apfel
Apfel
Banane
Birne
Birne
Kiwi
$ uniq obst.txt | sort | head -n 2
Apfel
Apfel
```

Swapped, `uniq` works first. In the unsorted list, no two equal lines are directly next to each other, so it removes nothing; `sort` then sorts all seven lines, and `head -n 2` shows `Apfel` twice. The order of the stages is part of the meaning of a pipeline.
:::
:::

:::aufgabe Exercise 15 ★ A typo
<span class="anker" id="aufg-15"></span>

Someone wanted to see the first two lines of the sorted fruit list and typed `sort obst.txt > head -n 2`. What appears on the screen, and which file exists in the practice directory afterward? What is the correct command?

:::loesung
```console
$ sort obst.txt > head -n 2
sort: cannot read: 2: No such file or directory
$ ls
a.txt    c.txt        fehler2.txt  obst.txt   zahlen.txt
aus.txt  d.txt        gross.txt    tag.txt
b.txt    einkauf.txt  head         woche.txt
$ cat head
$ rm head
```

The shell read `> head` as a redirection into a file named `head` and removed the redirection from the line. What remained was `sort obst.txt -n 2`: `sort` got the option `-n` and two file names, `obst.txt` and `2`. The file `2` does not exist; `sort` reports this and outputs nothing, and the file `head` is empty. What was meant was `sort obst.txt | head -n 2`. The list on your computer looks different, depending on which exercises you have already done.
:::
:::

:::aufgabe Exercise 16 ★★★ A message and a pipe
<span class="anker" id="aufg-16"></span>

Predict what `echo "Achtung" >&2 | wc -l` outputs, and check it. Explain both lines of the output. What changes with `|&` instead of `|`?

:::loesung
```console
$ echo "Achtung" >&2 | wc -l
Achtung
0
$ echo "Achtung" >&2 |& wc -l
Achtung
0
```

The shell first connects descriptor 1 of `echo` to the pipe. Then it carries out the redirection `>&2`: descriptor 1 becomes a copy of descriptor 2 and thus leads to the terminal. So `echo` writes to the terminal, and `Achtung` appears there. Nothing comes through the pipe; `wc -l` counts 0 lines.

With `|&`, nothing changes, which is surprising at first. `|&` works like `2>&1` after all redirections that belong to the command itself (subsection [4.1](#stufe-4-1)). At that point, descriptor 1 already leads to the terminal because of `>&2`, so descriptor 2 gets the terminal as well. Here, too, the rule holds: each copy takes over the target that is there at that moment.
:::
:::

:::aufgabe Exercise 17 ★★★ The descriptors in a pipe
<span class="anker" id="aufg-17"></span>

Run `ls -l /proc/self/fd` three times: once as it is, once as `ls -l /proc/self/fd | cat` and once as `ls -l /proc/self/fd 2> /dev/null | cat`. Where do descriptors 0, 1 and 2 of `ls` lead in each case? Explain each difference with what the shell set up before the start.

:::loesung
Directly in the terminal, 0, 1 and 2 lead to the terminal, as in subsection [1.7](prozesse-und-ihre-drei-strome.html#stufe-1-7). In the pipelines:

```console
$ ls -l /proc/self/fd | cat
total 0
lrwx------ 1 student student 64 Nov 10 05:32 0 -> /dev/pts/2
l-wx------ 1 student student 64 Nov 10 05:32 1 -> pipe:[9901]
lrwx------ 1 student student 64 Nov 10 05:32 2 -> /dev/pts/2
lr-x------ 1 student student 64 Nov 10 05:32 3 -> /proc/719/fd
$ ls -l /proc/self/fd 2> /dev/null | cat
total 0
lrwx------ 1 student student 64 Nov 10 05:32 0 -> /dev/pts/2
l-wx------ 1 student student 64 Nov 10 05:32 1 -> pipe:[9903]
l-wx------ 1 student student 64 Nov 10 05:32 2 -> /dev/null
lr-x------ 1 student student 64 Nov 10 05:32 3 -> /proc/721/fd
```

In the first pipeline, descriptor 1 leads to a pipe; the number in square brackets is its number in the kernel. The shell set this up before the start because `|` follows. Descriptors 0 and 2 still lead to the terminal, because a pipe connects only standard output. In the second pipeline, descriptor 2 also leads to `/dev/null`, because of `2> /dev/null`. In all three cases, `ls` notices none of this; it writes its list to descriptor 1 as always.
:::
:::

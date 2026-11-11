---
title: Turning output into arguments
pfad: Computer Science / Linux and the Command Line / Streams, Redirection, Pipes and Exit Status
adresse: informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status
knoten: Chapter 4: Streams, Redirection, Pipes and Exit Status
order: 6090800
summary: A pipe delivers data to standard input.
tags: xargs, argument list limit
lang: en
---

<span class="anker" id="stufe-7"></span>

:::zweck
A pipe delivers data to standard input. Some programs, however, do not read their standard input but expect file names as arguments. This section shows how to turn a list of names from a pipe into arguments, how to manage this with names that contain spaces and how `find` passes its matches to a command itself.
:::

### Stream or argument

<span class="anker" id="stufe-7-1"></span>

If a pipe delivers a list of file names, it seems natural to pass it straight on to `rm` or `wc`. That goes wrong, and in two different ways. Figure [26](#abb-26) shows why: a process receives data through two separate ways in.

:::abbildung linux/k4stromargument 26
Two separate ways into a process: the shell fixes the arguments at the start; standard input is a stream that flows afterward. With `echo probe2.txt | rm`, the name arrives in the stream, and the argument list of `rm` stays empty. With `echo einkauf.txt | wc -l`, `wc` reads the name as one line of data.
:::

:::satz Theorem 7.1 (Stream and argument)
<span class="anker" id="satz-7-1"></span>

A pipe connects streams, not arguments. What comes through the pipe is in the standard input of the next program and never in its argument list. A program that does not read its standard input sees none of it; a filter treats it as data, not as file names.
:::

::::beispiel Two ways of talking past each other
```console
$ echo probe2.txt | rm
rm: missing operand
Try 'rm --help' for more information.
$ echo einkauf.txt | wc -l
1
```

`rm` does not read its standard input, got no argument and complains that the name is missing. `wc -l` read its standard input and counted one line in it, namely the line `einkauf.txt`; it never opened the file itself. That file has five lines.
::::

⁠**In short:** What comes through a pipe is input, not an argument; programs without input do not see it, and filters take it for data.

### The command xargs

<span class="anker" id="stufe-7-2"></span>

So between the pipe and the program, a translator is missing that takes the words from the stream and appends them to the program as arguments. Figure [27](#abb-27) shows it at work.

:::abbildung linux/k4xargs 27
`xargs` as a translator: the words `einkauf.txt` and `obst.txt` come from standard input. `xargs` appends them to the command line `wc -l` and starts `wc -l einkauf.txt obst.txt` as a new process.
:::

:::definition Definition 7.2 (xargs)
<span class="anker" id="satz-7-2"></span>

The command __xargs__ reads its standard input and splits it into words at spaces, tabs and line ends. Then it starts the command that follows it as arguments and appends these words at the end as additional arguments. Without a command, it uses `echo`.
:::

::::beispiel Counting two files
```console
$ echo einkauf.txt obst.txt | xargs wc -l
 5 einkauf.txt
 7 obst.txt
12 total
```

`xargs` started `wc -l einkauf.txt obst.txt`; `wc` opened both files and counted their lines.
::::

::::beispiel [Second example] All the text files that find finds
Only together with `find` ([Chapter 3, Section 10.1](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-finden-und-platz-messen.html#stufe-10-1)) does `xargs` show what it is good for: the list of names comes into being during the search, and nobody has to type it.

```console
$ find . -name "*.txt" | xargs wc -l
  5 ./probe.txt
  7 ./obst.txt
  0 ./leer.txt
...
  5 ./einkauf.txt
  2 ./alles.txt
  2 ./beides.txt
 54 total
```

`find` writes each match on a line of its own; `xargs` turns all the lines into arguments for a single call of `wc -l`. The order is the one in which `find` comes across the entries.
::::

⁠**In short:** `xargs command` turns the words of its standard input into arguments for the command.

### Batches: xargs -n and the argument list limit

<span class="anker" id="stufe-7-3"></span>

Some commands take only one argument at a time, and no command tolerates arbitrarily many: the kernel has an upper limit for all the arguments of a program start together. `xargs` can therefore divide the words into batches and start the command several times. Figure [28](#abb-28) shows this.

:::abbildung linux/k4portionen 28
Three words, two ways to divide them into batches. Top, without `-n`: one call with all three words. Bottom, with `-n 1`: three calls with one word each.
:::

:::definition Definition 7.3 (Argument list limit, xargs -n)
<span class="anker" id="satz-7-3"></span>

The kernel limits how many bytes all the arguments of a program start may have together; `getconf ARG_MAX` shows this __argument list limit__. `xargs` keeps to it on its own and starts the command as often as necessary. With `-n number`, it passes at most `number` words per call.
:::

Besides the arguments, a few further pieces of information that every program receives at its start also count toward the limit. If a program start fails because of the limit, the shell reports “Argument list too long”.

::::beispiel One call or three
```console
$ echo Apfel Birne Kiwi | xargs -n 1 echo Obst:
Obst: Apfel
Obst: Birne
Obst: Kiwi
$ echo Apfel Birne Kiwi | xargs echo Obst:
Obst: Apfel Birne Kiwi
```

With `-n 1`, `xargs` started `echo Obst:` three times, each time with one word; without `-n`, it started it once with all three.
::::

::::beispiel [Second example] How large the limit is
```console
$ getconf ARG_MAX
2097152
```

That is $2\,097\,152$ bytes, exactly 2 MiB. The thousand names from `/usr/bin` need only a small part of it; with hundreds of thousands of files, however, the limit is reached quickly.
::::

⁠**In short:** There is an upper limit for the arguments of a program start; `xargs` distributes the words over several calls on its own, and with `-n` in batches of a fixed size.

:::hintergrund Where the limit comes from
When loading a program with `exec`, the kernel copies all the arguments into the memory of the process, namely into the area that the program also uses for its ongoing work, the so-called stack. So that enough room remains for this work, the arguments may occupy at most a quarter of the stack on Linux. On the test system, the stack is 8 MiB in size; a quarter of that is 2 MiB, exactly the value that `getconf ARG_MAX` shows. If you set the stack larger, you may also pass more arguments, though not arbitrarily many.
:::

### Names with spaces: the null byte as a separator

<span class="anker" id="stufe-7-4"></span>

`xargs` separates the words at spaces. A file name like `mein foto.jpg` (German for “my photo.jpg”) falls apart into two words, and `xargs` passes two names, neither of which exists. What is needed is a separator that never occurs in file names. Figure [29](#abb-29) shows the difference.

:::abbildung linux/k4leerzeichen 29
Top: `xargs` splits at spaces and line ends; `./mein foto.jpg` becomes the two wrong names `./mein` and `foto.jpg`. Bottom: null bytes stand between the names, and `xargs -0` splits only there; both names stay whole.
:::

:::definition Definition 7.4 (-print0 and xargs -0)
<span class="anker" id="satz-7-4"></span>

The action `-print0` of `find` writes a null byte, that is, the byte with the value 0, after each match instead of a line end. The option `-0` makes `xargs` split its input only at null bytes; spaces and line ends then belong to the name.
:::

This always works, because a file name may contain any character except the slash and the null byte ([Chapter 3, Section 3.7](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/den-inhalt-eines-verzeichnisses-anzeigen.html#stufe-3-7)). The null byte can therefore never stand in the middle of a name.

::::beispiel A vacation photo with a space
```console
$ touch "mein foto.jpg" urlaub.jpg
$ find . -name "*.jpg" | xargs ls
ls: cannot access './mein': No such file or directory
ls: cannot access 'foto.jpg': No such file or directory
./urlaub.jpg
$ find . -name "*.jpg" -print0 | xargs -0 ls
'./mein foto.jpg'   ./urlaub.jpg
```

In the first attempt, `ls` got three names, two of which do not exist. In the second, it got the two correct ones; `ls` added the quotation marks itself when displaying them, so that you can see that the space belongs to the name.
::::

Without `-0`, `xargs` also interprets quotation marks and the backslash in its input as characters meant to prevent splitting. A name with a single apostrophe therefore throws it off completely:

```console
$ echo "Gabi's Café.jpg" | xargs ls
xargs: unmatched single quote; by default quotes are special to xargs unless you use the -0 option
```

`xargs` took the apostrophe for the start of a quoted section whose end is missing, and did not even start `ls`. With `-print0` and `-0`, this problem does not occur either.

⁠**In short:** With `find -print0` and `xargs -0`, the null byte separates the names, and spaces remain part of the name.

:::warnung xargs with rm only with -print0 and -0
With `rm`, splitting at spaces can become dangerous: if splitting `alte liste.txt` (German for “old list.txt”) produces the word `liste.txt`, `rm` deletes a file of that name, if there is one, and it is a completely different file from the one intended. Anyone who passes matches from `find` to `rm` therefore always uses `-print0` and `-0` and tries the command with `ls` instead of `rm` beforehand.
:::

### The way without a pipe: find -exec

<span class="anker" id="stufe-7-5"></span>

`find` can also pass its matches to a command itself, without a pipe and without `xargs`. [Chapter 3, Section 10.6](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-finden-und-platz-messen.html#stufe-10-6) already showed actions such as `-print` and `-delete`; another one starts any command you like.

:::definition Definition 7.5 (-exec)
<span class="anker" id="satz-7-5"></span>

The action `-exec command {} \;` of `find` starts the command once for each match and puts the name of the match in place of `{}`. The action `-exec command {} +` collects the names like `xargs` and starts the command as rarely as possible, with many names at once; here `{}` must stand directly before the `+`.
:::

The semicolon at the end needs a backslash in front of it: without it, the shell would take it for the semicolon from subsection [6.1](befehle-verketten.html#stufe-6-1) and would not pass it on to `find` at all. Because `find` passes the names directly as arguments, without sending them through a stream, spaces cause no problems.

::::beispiel One at a time and collected
```console
$ find . -name "*.jpg" -exec ls {} \;
./urlaub.jpg
'./mein foto.jpg'
$ find . -name "*.jpg" -exec ls {} +
'./mein foto.jpg'   ./urlaub.jpg
```

With `\;`, `ls` ran twice, each time with one name, and wrote each name on a line of its own. With `+`, it ran once with both names, sorted them and put them side by side.
::::

⁠**In short:** `find … -exec command {} +` passes the matches directly as arguments to a command, names with spaces included; with `\;` instead of `+`, one at a time.

:::hintergrund An output that looks like a file
Some programs insist on file names and do not read standard input, or they are supposed to get two inputs at once. For this, bash knows another notation, process substitution: `<(command)` starts the command with its standard output in a pipe and puts in its place a file name under which the read end of this pipe can be reached.

```console
$ wc -l <(ls /usr/bin) <(ls /usr/sbin)
   1018 /dev/fd/63
    176 /dev/fd/62
   1194 total
$ ls -l <(true)
lr-x------ 1 student student 64 Nov 10 05:15 /dev/fd/63 -> 'pipe:[3582]'
```

`wc` counted two “files”, `/dev/fd/63` and `/dev/fd/62`. These are descriptors 63 and 62, which the shell opened for the two pipes and which `wc` inherited; `ls -l` shows that a pipe is behind such a name. Here the basic idea that everything is a file pays off: `wc` opens a name and reads, without knowing that a program is writing at the other end.
:::

### Exercises for Section [7](#stufe-7)

<span class="anker" id="stufe-7-6"></span>

:::aufgabe Exercise 23 ★ With and without xargs
<span class="anker" id="aufg-23"></span>

Predict what `echo obst.txt | wc -l` and `echo obst.txt | xargs wc -l` output, and check it. Explain the difference in one sentence.

:::loesung
```console
$ echo obst.txt | wc -l
1
$ echo obst.txt | xargs wc -l
7 obst.txt
```

Without `xargs`, `wc` counts the one line that comes through the pipe; with `xargs`, it gets `obst.txt` as an argument, opens the file and counts its seven lines.
:::
:::

:::aufgabe Exercise 24 ★★ All the words of all the lists
<span class="anker" id="aufg-24"></span>

With a single command line, count the words of all the files in your practice directory whose name ends in `.txt`, including the subdirectories. Solve it once with `find` and `xargs` and once with `find -exec`. Why is the total the same with both ways?

:::loesung
```console
$ find . -name "*.txt" | xargs wc -w
  9 ./fehler2.txt
  1 ./aus.txt
...
  5 ./einkauf.txt
 73 total
$ find . -name "*.txt" -exec wc -w {} +
  9 ./fehler2.txt
  1 ./aus.txt
...
  5 ./einkauf.txt
 73 total
```

Which files and which total appear depends on what is in your practice directory; here there were 13 files with 73 words in all. Both ways start `wc -w` once with all the names, in the order in which `find` finds them. So in both cases, `wc` gets the same arguments and calculates the same total. With `xargs`, this goes so smoothly only as long as no name contains a space; the way via `-exec … +` is safe even then.
:::
:::

:::aufgabe Exercise 25 ★★★ The old list
<span class="anker" id="aufg-25"></span>

Create two files in the practice directory: `touch "alte liste.txt" liste.txt`. (a) Predict what `find . -name "alte*" | xargs rm` does: Which file is deleted, which message appears, which file remains? (b) Check it with `ls`. (c) Create the deleted file again and delete `alte liste.txt` in two safe ways.

:::loesung
(a) Prediction: `xargs` splits `./alte liste.txt` into the words `./alte` and `liste.txt` and starts `rm ./alte liste.txt`. `./alte` does not exist, and `rm` reports that. `liste.txt` does exist, and `rm` deletes it, although nobody wanted to delete it. `alte liste.txt` remains.

(b)

```console
$ touch "alte liste.txt" liste.txt
$ find . -name "alte*" | xargs rm
rm: cannot remove './alte': No such file or directory
$ ls
 a.txt             b.txt   einkauf.txt   obst.txt    woche.txt
'alte liste.txt'   c.txt   fehler2.txt   sicherung   zahlen.txt
 aus.txt           d.txt   gross.txt     tag.txt
```

`liste.txt` is missing, and `alte liste.txt` is still there. This is exactly what the box in subsection [7.4](#stufe-7-4) warns about.

(c) With the null byte as a separator or with `-exec … +`:

```console
$ touch liste.txt
$ find . -name "alte*" -print0 | xargs -0 rm
$ ls
a.txt    c.txt        fehler2.txt  obst.txt   woche.txt
aus.txt  d.txt        gross.txt    sicherung  zahlen.txt
b.txt    einkauf.txt  liste.txt    tag.txt
$ touch "alte liste.txt"
$ find . -name "alte*" -exec rm {} +
$ ls
a.txt    c.txt        fehler2.txt  obst.txt   woche.txt
aus.txt  d.txt        gross.txt    sicherung  zahlen.txt
b.txt    einkauf.txt  liste.txt    tag.txt
```

Both times, only `alte liste.txt` disappears, and `liste.txt` stays. For a single known file, it of course also works without `find`: `rm "alte liste.txt"`.
:::
:::

**For further practice.** The freely accessible learning platform pwn.college offers short exercises in the browser under the name “Linux Luminarium”; the modules “Practicing Piping” and “Chaining Commands” match this chapter. They run on someone else's computer, not on your own.

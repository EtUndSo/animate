---
title: Processes and their three streams
pfad: Computer Science / Linux and the Command Line / Streams, Redirection, Pipes and Exit Status
adresse: informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status
knoten: Chapter 4: Streams, Redirection, Pipes and Exit Status
order: 6090200
summary: Before you can direct the output of a program into a file or connect two programs, you need a picture of what a running program is and by which paths data gets in and out.
tags: process, process ID, stream, end of the stream, Standard input, Standard output, Standard error, file descriptor
lang: en
---

<span class="anker" id="stufe-1"></span>

:::zweck
Before you can direct the output of a program into a file or connect two programs, you need a picture of what a running program is and by which paths data gets in and out. This section introduces the process, the stream, the three standard streams of every process and the numbers by which a process knows its streams.
:::

:::::vorwissen What you need for this: kernel, shell and files

<span class="anker" id="stufe-1-1"></span>

This chapter assumes [Chapters 1](/wissen/en/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/ein-linux-zum-ueben.html) to 3. From them, you mainly need the following.

<ul>

<li>

The kernel manages the hardware and all files. A program that wants to open, read or write to a file asks the kernel to do so with a system call ([Chapter 1, Section 1.4](/wissen/en/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/betriebssystem-kernel-und-distribution.html#stufe-1-4)).

</li>

<li>

The shell splits a command line into words at the spaces. The first word is the command, the others are its arguments ([Chapter 2, Section 2](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/der-aufbau-einer-befehlszeile.html#stufe-2)). If the command is a program file, the shell has the program run and waits until it is finished; it handles a builtin command such as `cd` itself ([Chapter 2, Sections 3.1](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/arten-von-befehlen.html#stufe-3-1) and [3.3](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/arten-von-befehlen.html#stufe-3-3)).

</li>

<li>

Ctrl+C aborts a running program. Ctrl+D at the start of a line tells a program that is waiting for keyboard input that the input has ended ([Chapter 2, Sections 5.4](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/schneller-arbeiten-vervollstandigung-verlauf-tastenkurzel.html#stufe-5-4) and [5.5](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/schneller-arbeiten-vervollstandigung-verlauf-tastenkurzel.html#stufe-5-5)).

</li>

<li>

A file is a sequence of bytes under a name; a text file consists of lines, and each line ends with the byte 10, the line end ([Chapter 3, Sections 1.2](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-verzeichnisse-und-der-verzeichnisbaum.html#stufe-1-2) and [4.1](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-ansehen.html#stufe-4-1)). `cat`, `head` and `wc` show and count the contents of files ([Chapter 3, Section 4](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-ansehen.html#stufe-4)).

</li>

<li>

`/dev` contains device files, among them `/dev/null`; in `/proc`, the kernel creates a directory for every running program, and its name is a number ([Chapter 3, Sections 7.7](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/die-verzeichnisstruktur-von-linux.html#stufe-7-7) and [7.8](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/die-verzeichnisstruktur-von-linux.html#stufe-7-8)). `mkdir`, `cp`, `mv` and `rm` create, copy, move and delete ([Chapter 3, Sections 5](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-und-verzeichnisse-anlegen.html#stufe-5) and [6](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/kopieren-verschieben-loschen.html#stufe-6)).

</li>

</ul>

::::beispiel The bytes of a small file
[Chapter 3](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-verzeichnisse-und-pfade.html) looked at the file `/etc/hostname` byte by byte. `od -An -tu1` shows each byte as a number:

```console
$ od -An -tu1 /etc/hostname
 108  97  98 111 114  10
```

These are the letters `l`, `a`, `b`, `o`, `r` and the line end, six bytes in all. These six numbers come up again later in this section.
::::

⁠**In short:** You need the kernel and its system calls, the structure of a command line, Ctrl+C and Ctrl+D, files as sequences of bytes and the directories `/dev` and `/proc`.

:::::

### The process

<span class="anker" id="stufe-1-2"></span>

So far, this series has spoken of the “running program”. That is no longer enough as soon as the same program runs several times: if you open two terminal windows and start the editor `nano` in both, two instances of the same program work side by side, each with its own file and its own position in the text. Such a single instance needs a word of its own.

As a picture for orientation: a recipe in a cookbook corresponds to the program. Every time someone cooks from the recipe, a cooking session begins with its own pots, its own ingredients and its own state of how far along it is; two people can cook from the same recipe at the same time without getting in each other's way. Figure [1](#abb-1) shows the same for a program.

:::abbildung linux/k4prozess 1
A program file on the storage device and two processes that were started from it. Each process has its own memory, its own open files and its own working directory. When a process ends, only the process disappears; the program file remains.
:::

:::definition Definition 1.1 (Process)
<span class="anker" id="satz-1-1"></span>

A __process__ is a program that is currently being executed, together with everything that belongs to exactly this execution: its own area in main memory, the files it has opened and its working directory. The kernel keeps each process separate from all others. It gives each process a number, the __process ID__.
:::

A program is therefore a file stored on the storage device; a process comes into being only when the program is started, and it disappears when the program ends. For every program that the shell is to run, it starts a new process and waits until that process ends. A builtin command, by contrast, the shell runs itself, without a new process. This also explains why `cd` has to be built in ([Chapter 2, Section 3.3](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/arten-von-befehlen.html#stufe-3-3)): every process has its own working directory, and a new process could change only its own, not the shell's.

The directories in `/proc` whose names are numbers belong to the running processes; the number is the process ID. Alongside them is the entry `/proc/self`. It is a symbolic link ([Chapter 3, Section 8.5](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/inode-und-links.html#stufe-8-5)); for every process that reads it, the kernel makes it point to that process's own directory.

::::beispiel Each command a new process
The command `readlink` shows where a symbolic link points. Applied twice in a row to `/proc/self`:

```console
$ readlink /proc/self
443
$ readlink /proc/self
444
```

Each `readlink` saw a different number, namely its own: the shell started a new process for each call. On your computer, the numbers will be different. The entry `comm` in this directory contains the name of the program, and so does the first line of `status`:

```console
$ cat /proc/self/comm
cat
$ head -n 1 /proc/self/status
Name:   head
```

Whoever reads sees itself: `cat` finds `cat` there, `head` finds `head`.
::::

⁠**In short:** A program is a file; a process is a running execution of it, with its own memory, its own open files, its own working directory and its own number.

### The stream

<span class="anker" id="stufe-1-3"></span>

A program such as `cat` should be able to read text from a file, from the keyboard or, as you will see, from other sources. It would be tedious if it needed separate commands for each source. It is simpler if all sources look the same to the program: as bytes that arrive one after another.

A conveyor belt serves as a picture for orientation. The bytes lie on it one behind the other and arrive at the receiver one at a time. What has passed is gone; the receiver cannot turn the belt back, and it cannot see where the belt comes from. Figure [2](#abb-2) shows this.

:::abbildung linux/k4strom 2
A stream: bytes travel in order from the writing process to the reading process. The reader sees only the bytes, not where they come from. When nothing more arrives, the next read request returns zero bytes, and the reader knows: this is the end of the stream.
:::

:::definition Definition 1.2 (Stream, end of the stream)
<span class="anker" id="satz-1-2"></span>

A __stream__ is a sequence of bytes that a process reads or writes in order. The process sees only the bytes themselves, not where they come from or where they go. If nothing more arrives during reading and nothing more can arrive, the __end of the stream__ has been reached; the kernel tells the reading process by having a read request return zero bytes.
:::

So the end of the stream is not a special character that stands in the stream, but the answer “nothing more” to a read request. [Chapter 2, Section 5.5](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/schneller-arbeiten-vervollstandigung-verlauf-tastenkurzel.html#stufe-5-5) saw the same thing with the end of input.

::::beispiel The stream from /etc/hostname
`cat /etc/hostname` reads the file as a stream. The first read request returns the six bytes 108, 97, 98, 111, 114 and 10 from the example in subsection [1.1](#stufe-1-1); `cat` passes them on, and `labor` (German for “lab”) appears in the terminal. The second read request returns zero bytes. From this, `cat` recognizes the end of the stream and stops. [Chapter 1, Section 1.4](/wissen/en/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/betriebssystem-kernel-und-distribution.html#stufe-1-4) made exactly these two read requests visible with the tool `strace`: the first returned six bytes, the second zero.
::::

⁠**In short:** A stream is a sequence of bytes that a process reads or writes in order without knowing where they come from; when a read request returns zero bytes, the stream has ended.

### Standard input

<span class="anker" id="stufe-1-4"></span>

Many programs need data. If they get a file name as an argument, they read the file. If they get none, they still have to read from somewhere. For this, every process has a fixed way in from the very start.

:::definition Definition 1.3 (Standard input)
<span class="anker" id="satz-1-3"></span>

__Standard input__ (*stdin* for short) is the stream from which a process reads when it is not told otherwise. If you start a program in the terminal, its standard input is the terminal: what you type arrives in this stream as a line once you press Enter.
:::

`cat`, `wc`, `head` and many other programs follow the same rule: given file names, they read those files; without file names, they read their standard input. If you start them in the terminal without an argument, they seem to hang. In fact, they are waiting for input. Ctrl+D at the start of a line ends the stream, and the program carries on properly with what it has received. Ctrl+C, by contrast, aborts the program; it then outputs no result.

::::beispiel cat without an argument
Type `cat` and Enter, then `Hallo` (German for “hello”), Enter, `Welt` (“world”), Enter and finally Ctrl+D:

```console
$ cat
Hallo
Hallo
Welt
Welt
```

Each line appears twice. The first is displayed by the terminal as you type; the second was written by `cat` after it had read the line from its standard input. Figure [3](#abb-3) traces the path of one line. Ctrl+D itself does not appear; afterward `cat` ends, and the prompt returns.

:::abbildung linux/k4cateingabe 3
The path of the typed line `Hallo`: the terminal displays it while it is being typed and, after the Enter key, sends it into the standard input of `cat`. `cat` writes it to its standard output, and the terminal shows it a second time. Ctrl+D ends the stream, and `cat` ends.
:::
::::

::::beispiel [Second example] wc counts typed lines
Type `wc -l`, then the three lines `Milch`, `Brot`, `Kaffee` (German for “milk”, “bread” and “coffee”) and Ctrl+D:

```console
$ wc -l
Milch
Brot
Kaffee
3
```

You typed the three lines. `wc` answers only when the stream has ended, because until then it does not know whether more lines are coming; then it writes the number 3. Since it had no file name, none follows the number either. With Ctrl+C instead of Ctrl+D, `wc` would have been aborted without a result.
::::

⁠**In short:** Standard input is the way in to a process; in the terminal it is the keyboard, and Ctrl+D ends the stream.

### Standard output

<span class="anker" id="stufe-1-5"></span>

A program also has to get rid of its results: the names that `ls` finds, the contents that `cat` reads, the numbers that `wc` counts. There is a fixed way out for this.

:::definition Definition 1.4 (Standard output)
<span class="anker" id="satz-1-4"></span>

__Standard output__ (*stdout* for short) is the stream to which a process writes its results. If you start a program in the terminal, its standard output is the terminal, which displays everything that arrives there.
:::

Almost everything you saw in [Chapters 2](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/die-shell-erste-befehle.html) and 3 as the response of a command came through standard output. The second line `Hallo` in the example on standard input was also written by `cat` to its standard output.

::::beispiel echo writes its arguments
The builtin command `echo` from [Chapter 2](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/die-shell-erste-befehle.html) writes its arguments, separated by spaces, with a line end to standard output:

```console
$ echo Hallo Linux
Hallo Linux
```

`echo` reads nothing; it does not use its standard input, only the way out.
::::

⁠**In short:** Standard output is the way out for the results of a process; in the terminal it ends up on the screen.

### Standard error

<span class="anker" id="stufe-1-6"></span>

Not everything a program writes is a result. If `ls` cannot find a file, it reports this. This message is not part of the data you asked for. That is why every process has a second way out.

:::definition Definition 1.5 (Standard error)
<span class="anker" id="satz-1-5"></span>

__Standard error__ (*stderr* for short) is a second output stream to which a process writes error messages, warnings and notices. If you start a program in the terminal, this stream goes to the terminal, too.
:::

So in the terminal both ways out end up on the same screen, and you cannot tell from a line which one it came through. Figure [4](#abb-4) shows a process with its three standard streams, drawn, as a picture for orientation, like three tubes: one leads in, two lead out.

:::abbildung linux/k4rohre 4
A process with its three standard streams. Standard input comes from the keyboard; standard output and standard error both go to the screen. With `ls /etc/hostname /gibtsnicht` (German for “doesnotexist”), the result runs through one way out and the error message through the other; on the screen the two lines appear one below the other.
:::

::::beispiel A result and an error message
`ls` gets two names, only the first of which exists:

```console
$ ls /etc/hostname /gibtsnicht
ls: cannot access '/gibtsnicht': No such file or directory
/etc/hostname
```

The first line is an error message and came through standard error; the second is the result and came through standard output. `ls` reports problems with the arguments first. On the screen, the lines look no different; Section [2](ausgaben-umleiten.html#stufe-2) separates them.
::::

⁠**In short:** Standard error is a separate way out for messages; in the terminal it mixes with standard output.

:::hintergrund Why there is a separate stream for errors
In the early years of Unix, all programs wrote their messages to standard output. That was already a nuisance when you had the output written to a file: error messages then sat in the middle of the data, and you saw nothing of them on the screen. It became untenable once the output of one program could be fed directly to another program, because that program took the message for data and went on processing it. Even so, people lived with it for a few more years. Shortly after the Sixth Edition of Unix, released in 1975, Dennis Ritchie introduced standard error. Since then, the division of labor has been: data to standard output, error messages and notices for the person at the terminal to standard error. This keeps the data clean, and the messages reach the person even when the data goes somewhere else.
:::

### The file descriptor

<span class="anker" id="stufe-1-7"></span>

A process often has more than three streams open: a copy program reads from one file and writes to another, and it has the three standard streams as well. When it asks the kernel to read or write, it has to specify which of its open files it means. File names would be cumbersome for this, because some streams have no name at all.

A coat check serves as a picture for orientation. If you hand in your coat, you get a ticket with a number; later, the number is enough to get exactly this coat back. In the same way, the kernel keeps a list of open files for each process, and the process gives only the number of the entry. Figure [5](#abb-5) shows such a list.

:::abbildung linux/k4deskriptoren 5
The list of descriptors of a process. Numbers 0, 1 and 2 lead to the terminal, number 3 to a file that the process has opened itself. When reading and writing, the process gives the kernel only the number; the kernel knows what is behind it.
:::

:::definition Definition 1.6 (File descriptor)
<span class="anker" id="satz-1-6"></span>

A __file descriptor__, descriptor for short, is a small integer under which the kernel keeps track of an open file for a process. The three standard streams have fixed numbers: 0 is standard input, 1 standard output, 2 standard error. Every further file that the process opens gets the lowest number that is currently free, so 3 comes first.
:::

So a program does not write its result “to the screen”; instead, it asks the kernel: “Write these bytes to descriptor 1.” In [Chapter 1, Section 1.4](/wissen/en/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/betriebssystem-kernel-und-distribution.html#stufe-1-4), exactly this appeared in the output of `strace`: the GNU implementation of `cat` opened `/etc/hostname` and got number 3, read from descriptor 3 and wrote to descriptor 1 with `write(1, …)`.

Where do 0, 1 and 2 come from if a program has never opened them itself? A new process inherits the open descriptors of the process that starts it. For the shell in the terminal window, 0, 1 and 2 lead to the terminal; every program that the shell starts therefore finds these three descriptors already in place. In the directory `fd` under `/proc/self`, there is a symbolic link for each descriptor, with the number as its name; it shows where the descriptor leads.

::::beispiel The descriptors of ls
```console
$ ls -l /proc/self/fd
total 0
lrwx------ 1 student student 64 Nov 10 05:14 0 -> /dev/pts/2
lrwx------ 1 student student 64 Nov 10 05:14 1 -> /dev/pts/2
lrwx------ 1 student student 64 Nov 10 05:14 2 -> /dev/pts/2
lr-x------ 1 student student 64 Nov 10 05:14 3 -> /proc/454/fd
```

Descriptors 0, 1 and 2 all lead to `/dev/pts/2`. This is the device file of the terminal window in which the shell runs; on your computer, there may be a different number at the end. `ls` opened descriptor 3 itself: it is the directory whose contents it is currently listing, namely `/proc/454/fd`, its own. 3 was the lowest free number.
::::

⁠**In short:** A descriptor is the number by which a process refers to an open file when dealing with the kernel; 0, 1 and 2 are the three standard streams.

:::hintergrund Everything is a file
In the example, descriptors 0, 1 and 2 lead to a device file and descriptor 3 to a directory. For the program, this makes no difference: it always reads and writes with the same system calls and gives only the number. This is a consequence of the basic idea of Unix that almost everything a program works with appears as a file ([Chapter 3, Section 7.7](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/die-verzeichnisstruktur-von-linux.html#stufe-7-7)). The kernel makes sure that a write request to a terminal, to a file on the hard disk or to `/dev/null` does the right thing in each case. A program such as `cat` therefore contains not a single line that deals with terminals; it writes to descriptor 1, and someone else decides what is behind it.
:::

### Exercises for Section [1](#stufe-1)

<span class="anker" id="stufe-1-8"></span>

:::aufgabe Exercise 1 ★ Program or process?
<span class="anker" id="aufg-1"></span>

(a) The file `/usr/bin/nano` is on your computer. Is it a program or a process? (b) You start `nano` in three terminal windows. How many programs and how many processes are involved? (c) You quit two of the three. What is still there afterward? (d) Does the shell start a new process when you type `cd /etc`? Explain why.

:::loesung
(a) A program: `/usr/bin/nano` is a file on the storage device. As long as nobody starts it, nothing runs.

(b) One program and three processes. Each start creates a process of its own with its own number, its own memory and its own open file; all three execute the same program code.

(c) The program file and one process. The two processes that ended are gone; the file `/usr/bin/nano` stays where it is, unchanged.

(d) No. `cd` is a builtin command that the shell executes itself. It has to be this way: each process has its own working directory, and a new process could change only its own, not that of the shell.
:::
:::

:::aufgabe Exercise 2 ★★ Reading to the end
<span class="anker" id="aufg-2"></span>

(a) Start `wc -w` without an argument, type the line `Heute gibt es Kuchen` (German for “There is cake today”) and then Ctrl+D. What appears, and why only after Ctrl+D? (b) Repeat it, but this time end with Ctrl+C. What is different, and why? (c) Why did the terminal show each line twice in the example with `cat`, but only once with `wc -l`?

:::loesung
(a) After Ctrl+D, the number 4 appears:

```console
$ wc -w
Heute gibt es Kuchen
4
```

You typed the line. `wc` counts the words of its entire stream and can write the result only when it knows that nothing more is coming, that is, after the end of the stream. Before that, more lines could still follow.

(b) With Ctrl+C, no number appears:

```console
$ wc -w
Heute gibt es Kuchen
^C
```

Ctrl+C does not end the stream; it aborts `wc`. A program that has been aborted no longer writes a result.

(c) `cat` reads each line and immediately writes it back to its standard output, that is, to the terminal; it was already shown there once, because the terminal shows what is typed. `wc -l` does not write the lines back, only the number at the end.
:::
:::

:::aufgabe Exercise 3 ★★ Which line takes which way out?
<span class="anker" id="aufg-3"></span>

For `cat /etc/hostname /gibtsnicht /etc/timezone`, predict which lines appear and through which of the two ways out each of them comes. Check the lines on the computer. Why can you not tell from the screen alone whether your assignment is correct?

:::loesung
Prediction: `labor` through standard output, then the message about `/gibtsnicht` through standard error, then `Europe/Berlin` through standard output. On the computer:

```console
$ cat /etc/hostname /gibtsnicht /etc/timezone
labor
Europe/Berlin
cat: /gibtsnicht: No such file or directory
$ gnucat /etc/hostname /gibtsnicht /etc/timezone
labor
gnucat: /gibtsnicht: No such file or directory
Europe/Berlin
```

The assignment to the ways out is correct, but the order on the screen is not the same in every implementation. As of Ubuntu 26.04, the uutils implementation of `cat` collects the messages and writes them only at the end; the GNU implementation, which can be called as `gnucat` under Ubuntu 26.04, reports the error at the point where it occurs. From the screen alone, you cannot tell through which way out a line came, because both lead to the same terminal and look the same. Only a redirection can prove it, as in subsection [2.3](ausgaben-umleiten.html#stufe-2-3): `cat /etc/hostname /gibtsnicht /etc/timezone 2> /dev/null` shows only the two lines of standard output.
:::
:::

:::aufgabe Exercise 4 ★★★ Counting the descriptors
<span class="anker" id="aufg-4"></span>

Run `ls -l /proc/self/fd` twice in a row. (a) Which parts of the output change, which stay the same, and why? (b) Why does the directory that `ls` lists have number 3 and not, say, 7? (c) Then run `cat /proc/self/comm /proc/self/comm` and explain why the same name appears twice.

:::loesung
(a) What stays the same are the numbers 0 to 3 and the targets of descriptors 0, 1 and 2, namely the terminal. It is the same terminal because both `ls` were started by the same shell and inherited its descriptors. What changes are the time, if a minute has passed in the meantime, and the number in the target of descriptor 3, for example `/proc/454/fd` and a higher one the next time: each `ls` is a new process with its own number and lists its own directory.

(b) When a new process opens something, it gets the lowest free number. 0, 1 and 2 are already taken, so 3 is the lowest free one. A 7 would occur only if 3 to 6 were already taken.

(c)

```console
$ cat /proc/self/comm /proc/self/comm
cat
cat
```

Both arguments are read by the same process, namely this one `cat`. `/proc/self` therefore points to the same directory both times, and the name stored there is `cat`.
:::
:::

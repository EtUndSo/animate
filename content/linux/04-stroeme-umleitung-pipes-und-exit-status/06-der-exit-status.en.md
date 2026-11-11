---
title: The exit status
pfad: Computer Science / Linux and the Command Line / Streams, Redirection, Pipes and Exit Status
adresse: informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status
knoten: Chapter 4: Streams, Redirection, Pipes and Exit Status
order: 6090600
summary: Every command ends either with success or with failure, and the next step often depends on which.
tags: exit status
lang: en
---

<span class="anker" id="stufe-5"></span>

:::zweck
Every command ends either with success or with failure, and the next step often depends on which. This section shows how a process leaves behind a number when it ends, how you query it and what the different numbers mean.
:::

### The exit status

<span class="anker" id="stufe-5-1"></span>

Whether a command worked can often be read from its messages. That is enough for a person, but not for the shell: it should be able to make the next command depend on it without interpreting texts that differ from program to program and from language to language. This requires a simple, uniform answer from every process. Figure [19](#abb-19) shows where it comes from.

:::abbildung linux/k4exitstatus 19
A process ends and leaves behind a number. The kernel passes it on to the shell, which has been waiting for the end; the shell remembers the number, and `echo $?` shows it.
:::

:::definition Definition 5.1 (Exit status)
<span class="anker" id="satz-5-1"></span>

When it ends, every process leaves behind an integer from 0 to 255, its __exit status__. The number 0 means success, every other number means failure. The shell, which has waited for the process to end, receives the number from the kernel and remembers it until the next command ends.
:::

You query the exit status with the character sequence `$?`. Before the shell executes a command line, it replaces `$?` in it with the exit status of the most recently ended command. So `echo $?` writes out this number.

::::beispiel Success and failure of ls
```console
$ ls /usr/bin > /dev/null
$ echo $?
0
$ ls /gibtsnicht
ls: cannot access '/gibtsnicht': No such file or directory
$ echo $?
2
$ echo $?
0
```

The first `ls` succeeded; its output went to `/dev/null`. The second failed with exit status 2. The last `echo $?` shows 0, because the most recently ended command was now the previous `echo`, and it succeeded. So if you need an exit status, you have to query it immediately.
::::

::::beispiel [Second example] true and false
The builtin commands `true` and `false` do nothing except end with 0 and 1, respectively:

```console
$ true
$ echo $?
0
$ false
$ echo $?
1
```
::::

If a program specifies a number greater than 255 when it ends, only the remainder of its division by 256 is left. You can try this with a second shell: `bash -c '…'` starts another bash that runs the text in the quotes as a command line, and the builtin command `exit` ends it with the given number.

```console
$ bash -c 'exit 3'
$ echo $?
3
$ bash -c 'exit 300'
$ echo $?
44
```

300 becomes 44, because $300 = 256 + 44$.

⁠**In short:** Every process ends with a number from 0 to 255; 0 means success, and `$?` returns the number of the most recently ended command.

:::hintergrund Why 0, of all numbers, means success
If you think of truth values, you might expect 1 to stand for “it worked”. With the exit status, it is the other way around, and there is a simple reason for this: there is exactly one kind of success but many kinds of failure. With 0 for success, all other numbers remain free to distinguish different errors. That only 0 to 255 are possible is due to the path the number takes. When a program ends, it does pass an arbitrary integer to the kernel, but on Linux, only its lowest byte, that is, eight bits, arrives at the waiting shell; this corresponds exactly to the remainder of division by 256. The waiting shell learns the number through a system call with which a process waits for the end of a process that it started.
:::

### What the nonzero numbers mean

<span class="anker" id="stufe-5-2"></span>

“Failure” can mean different things: a search found nothing, or the file that was to be searched does not even exist. A program that knows more than one kind of failure can distinguish them with different numbers. Figure [20](#abb-20) shows this with the search program `grep`.

:::abbildung linux/k4grepstatus 20
Three outcomes of a search with `grep -q`: The word occurs in the file, exit status 0; it does not occur, exit status 1; the file is missing, exit status 2. Only in the third case is there a message.
:::

:::satz Theorem 5.2 (Meaning of the nonzero numbers)
<span class="anker" id="satz-5-2"></span>

Which nonzero number means which failure is determined by each program itself; the manual page describes it in its EXIT STATUS part ([Chapter 2, Section 4.3](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/hilfe-finden.html#stufe-4-3)). Many programs report every failure with 1. Programs that distinguish several kinds usually use 1 for a “no” result or a minor error and 2 for a serious error or an incorrect call.
:::

The option `-q` (short for *quiet*) makes `grep` output nothing and answer only with its exit status; it still writes error messages, though.

::::beispiel Found, not found, error
```console
$ grep -q Apfel obst.txt
$ echo $?
0
$ grep -q Mango obst.txt
$ echo $?
1
$ grep -q Apfel fehlt.txt
grep: fehlt.txt: No such file or directory
$ echo $?
2
```

`grep` distinguishes three cases. The 1 is not an error in the strict sense but the answer “does not occur”; only the 2 reports that the search was not possible at all.
::::

::::beispiel [Second example] cat knows only one kind
```console
$ cat fehlt.txt
cat: fehlt.txt: No such file or directory
$ echo $?
1
```

`cat` reports every failure with 1. In the previous subsection, `ls` ended with 2 because a file that had been explicitly asked for did not exist; it reports minor problems with 1.
::::

⁠**In short:** The nonzero number says which failure it was; what it means is stated in the program's manual page.

### The shell's numbers: 126, 127 and 128 + n

<span class="anker" id="stufe-5-3"></span>

Sometimes a program never gets to leave a number behind: the command does not exist, the file cannot be executed, or the process is aborted in the middle of its work. For these cases, the shell itself puts in numbers that are worth remembering. Figure [21](#abb-21) places them on the number line.

:::abbildung linux/k4nummern 21
The number line of the exit status from 0 to 255: 0 for success, the small numbers for errors reported by the program itself, 126 and 127 for commands that could not start and, from 129 upward, aborts by an interrupt message, such as 130 for Ctrl+C.
:::

:::definition Definition 5.3 (Exit statuses set by the shell)
<span class="anker" id="satz-5-3"></span>

The shell itself sets an exit status in three cases:

<ul>

<li>

127 if the command does not exist;

</li>

<li>

126 if the file does exist but cannot be executed as a program;

</li>

<li>

$128 + n$ if the process was ended by the interrupt message with the number $n$.

</li>

</ul>
:::

Each kind of interrupt message has a number. The message that Ctrl+C triggers ([Chapter 2, Section 5.4](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/schneller-arbeiten-vervollstandigung-verlauf-tastenkurzel.html#stufe-5-4)) has the number 2; a process aborted with Ctrl+C therefore leaves behind $128 + 2 = 130$.

::::beispiel Not found, not executable, aborted
```console
$ gibtsnicht
gibtsnicht: command not found
$ echo $?
127
```

A command `gibtsnicht` exists neither as a builtin nor in the search path. Next, the shell is to execute the directory `/etc`:

```console
$ /etc
bash: /etc: Is a directory
$ echo $?
126
```

`/etc` exists, but a directory is not a program. Finally, `sleep 10` waits ten seconds; type Ctrl+C before they are up:

```console
$ sleep 10
^C
$ echo $?
130
```

The terminal shows Ctrl+C as `^C`. `sleep` was ended by message number 2, so $128 + 2 = 130$.
::::

⁠**In short:** 127 means “not found”, 126 “not executable”, and $128 + n$ means “ended by interrupt message $n$”, such as 130 after Ctrl+C.

:::hintergrund Why 128 + n
The kernel tells the waiting shell exactly how a process ended: either by itself, with a number from 0 to 255, or by an interrupt message, with the number of that message. But the shell has only a single number that it can store in `$?`. It therefore maps the second case to $128 + n$. Because programs almost always use small numbers for their own errors, a value above 128 indicates an abort from outside. This is not unambiguous: a program could itself end with 130. The standard for Unix shells only requires a value greater than 128 after an abort. bash uses $128 + n$, and so does the smaller shell dash, which Ubuntu provides under the name `/bin/sh`; on the test system, a command aborted with Ctrl+C returns 130 in both. Other shells may differ: the KornShell ksh93 uses $256 + n$, so the same abort results in 258 there. 126 and 127 are also numbers that the shell assigns when the desired program could not even be started; programs should therefore not use them for their own purposes.
:::

### Exercises for Section [5](#stufe-5)

<span class="anker" id="stufe-5-4"></span>

:::aufgabe Exercise 18 ★ Predicting the exit status
<span class="anker" id="aufg-18"></span>

For each command, predict the exit status and check it with `echo $?`, typed directly afterward: (a) `ls /etc > /dev/null` (b) `cat einkauf.txt gibtsnicht.txt` (c) `grep -q Milch einkauf.txt` (d) `grep -q Tee einkauf.txt` (`Tee` is German for “tea”) (e) `Ls /etc` (f) `/usr`.

:::loesung
```console
$ ls /etc > /dev/null
$ echo $?
0
$ cat einkauf.txt gibtsnicht.txt
Milch
Brot
Äpfel
Kaffee
Butter
cat: gibtsnicht.txt: No such file or directory
$ echo $?
1
$ grep -q Milch einkauf.txt
$ echo $?
0
$ grep -q Tee einkauf.txt
$ echo $?
1
$ Ls /etc
Ls: command not found
$ echo $?
127
$ /usr
bash: /usr: Is a directory
$ echo $?
126
```

(a) 0, success. (b) 1: `cat` output the first file and failed on the second, and a single failure is enough for a nonzero exit status. (c) 0, found. (d) 1, not found. (e) 127, because `Ls` with a capital L does not exist; Linux distinguishes between uppercase and lowercase letters. (f) 126, because `/usr` exists, but a directory cannot be executed.
:::
:::

:::aufgabe Exercise 19 ★★ Working back from the numbers
<span class="anker" id="aufg-19"></span>

(a) What exit status do `bash -c 'exit 256'` and `bash -c 'exit 513'` leave behind? Calculate first, then check. (b) A process ended with 137. What was the number of the interrupt message? (c) In subsection [5.1](#stufe-5-1), the second `echo $?` showed a 0. How could you have displayed the exit status 2 of the failed `ls` twice?

:::loesung
(a) $256 = 1 \cdot 256 + 0$, remainder 0; $513 = 2 \cdot 256 + 1$, remainder 1:

```console
$ bash -c 'exit 256'
$ echo $?
0
$ bash -c 'exit 513'
$ echo $?
1
```

The first case is remarkable: `exit 256` reports success, although the number is not 0.

(b) $137 - 128 = 9$. The process was ended by interrupt message number 9.

(c) You have to query the exit status before another command ends. The shell replaces both occurrences of `$?` in a single line before `echo` runs:

```console
$ ls /gibtsnicht
ls: cannot access '/gibtsnicht': No such file or directory
$ echo $? $?
2 2
```
:::
:::

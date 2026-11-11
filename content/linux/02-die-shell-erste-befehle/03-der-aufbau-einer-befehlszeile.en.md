---
title: The structure of a command line
pfad: Computer Science / Linux and the Command Line / The Shell: First Commands
adresse: informatik/linux-und-kommandozeile/die-shell-erste-befehle
knoten: Chapter 2: The Shell: First Commands
order: 6070300
summary: A command line is not free text; it follows a few fixed rules.
tags: command line, words, command, argument, option, short option, long option, option with a value
lang: en
---

<span class="anker" id="stufe-2"></span>

:::zweck
A command line is not free text; it follows a few fixed rules. This section shows how the shell splits a line into words, which word names the command, which ones tell it what to work with and how, and how you pass a word that looks like an option as an ordinary word anyway.
:::

### The command line

<span class="anker" id="stufe-2-1"></span>

Before the shell can run anything, it has to find out which parts the typed line consists of. There is a simple, fixed rule for this.

**Words, not letters.** The shell does not read the line letter by letter as a whole; it first splits it at the spaces into separate pieces. Only then does it look at what the first piece means. Figure [5](#abb-5) shows this for the line `uname -r`.

:::abbildung linux/k2woerter 5
The shell splits the command line `uname -r` at the spaces into the words `uname` and `-r`. Only then does it look at what the words mean.
:::

:::definition Definition 2.1 (Command line and word)
<span class="anker" id="satz-2-1"></span>

A __command line__ is everything you type after the prompt before you press Enter. The shell splits it at spaces into __words__; several spaces in a row separate like a single one.
:::

::::beispiel Counting words
`uname -r` consists of the two words `uname` and `-r`. `echo Hallo` (German for “hello”) also consists of two words, because the three spaces separate like a single one. `uname-r`, by contrast, is a single word, because there is no space in it; the hyphen separates nothing.
::::

⁠**In short:** The shell splits every command line into words at the spaces.

### The command

<span class="anker" id="stufe-2-2"></span>

Above all, a line to the shell has to say what is to happen. As in a short sentence, this most important part comes first.

:::definition Definition 2.2 (Command)
<span class="anker" id="satz-2-2"></span>

The first word of a command line is the __command__: the name of what is to be run. The shell looks up only this word; it passes all the others on to the command.
:::

Upper and lower case matter: `uname` and `UNAME` are different names to the shell. If the space is missing, two words become one, and the shell looks for a command with this long name.

::::beispiel Three commands and two typos
The first three lines consist of nothing but a command. `uname` names the operating system, `whoami` (“who am I?”) the user, `hostname` the name of the computer:

```console
$ uname
Linux
$ whoami
student
$ hostname
labor
$ UNAME -r
UNAME: command not found
$ uname-r
uname-r: command not found
```

In the last two lines, the shell reports that it knows no command of this name: once because of the capital letters, once because `uname-r` without a space is a single word. For some typos, Ubuntu also suggests similar-sounding commands; you do not need to install anything for this chapter.
::::

⁠**In short:** The first word of the line is the command, and in its name every letter counts, including whether it is upper or lower case.

### The argument

<span class="anker" id="stufe-2-3"></span>

Many commands need more than their name: Which file should be displayed, which text printed? This information is in the remaining words of the line.

**The shell passes on words, not spaces.** The command `echo` simply writes out the words it receives, separated by one space each. With it, you can see exactly what the shell makes of a line. Figure [6](#abb-6) shows this for a line with many spaces.

:::abbildung linux/k2argumente 6
The shell turns `echo Hallo Welt` into three words. `echo` receives only the two words `Hallo` and `Welt` and writes them with a single space between them.
:::

:::definition Definition 2.3 (Argument)
<span class="anker" id="satz-2-3"></span>

Every word of the command line after the command is an __argument__. The shell passes the arguments to the command in the order in which they appear. What an argument means is determined by the command itself.
:::

::::beispiel Printing words and showing a file
`echo` receives two arguments, the German words for “hello” and “world”, and writes them out. How many spaces there were between the words, `echo` never learns:

```console
$ echo Hallo Welt
Hallo Welt
$ echo Hallo      Welt
Hallo Welt
```

The command `cat` shows the contents of the files whose names it receives as arguments. The argument `/etc/hostname` names the file `hostname` in the system folder `/etc`; the slash separates the folder from the name of the file. The file contains the name of the computer:

```console
$ cat /etc/hostname
labor
$ cat /etc/Hostname
cat: /etc/Hostname: No such file or directory
```

Upper and lower case matter in file names, too: there is no file `Hostname`. The error message begins with the name of the command so that you know who is complaining.
::::

⁠**In short:** The words after the command are its arguments; the shell passes them on in order, and the command decides what they mean.

:::hintergrund The shell splits, the program interprets
The shell passes a command a list of words, without the spaces between them. For `echo Hallo Welt`, the list is `echo`, `Hallo`, `Welt`; the first element is the name under which the command was called. If the shell starts a program for this, it hands the list to the kernel with a system call, and the kernel places it in the new program's memory. The program never sees the line you typed, only this list. That is why `echo` cannot reproduce the many spaces, and that is why it is entirely up to the program whether it understands a word as a file name, a number or text. The shell only determines where one word ends and the next one begins.
:::

### The option

<span class="anker" id="stufe-2-4"></span>

Sometimes the same command should work a little differently: print more, print less, sort in reverse. For this, there is a special kind of argument that does not say *what* a command works with, but *how*.

**Switches on a machine.** A washing machine always washes laundry, but with switches you choose the temperature and the spin speed (a picture for orientation). Options are such switches, and you recognize them by the minus sign at the front. Figure [7](#abb-7) shows three switches of `uname`, separately and bundled.

:::abbildung linux/k2buendeln 7
Three short options of `uname`, separate and bundled behind a single shared minus sign. All the ways of writing them mean the same thing, and the order of the output is set by the program, not by the order of the letters.
:::

:::definition Definition 2.4 (Option)
<span class="anker" id="satz-2-4"></span>

An __option__ is an argument that begins with a minus sign and determines how the command works. A __short option__ consists of a minus sign and a single letter, such as `-r`. Several short options without a value may be bundled behind a single minus sign: `-srm` means the same as `-s -r -m`.
:::

Which options exist and what a letter means is up to each program. For `uname`, `-r` means “version of the kernel”; other programs use the same letter for entirely different things. If a program does not know an option, it stops with an error message.

::::beispiel Everything uname reveals
Without an option, `uname` prints only the name of the kernel. `-s` explicitly does the same, `-r` prints the version of the kernel and `-m` the processor type:

```console
$ uname -s
Linux
$ uname -r
6.6.87.2-microsoft-standard-WSL2
$ uname -m
x86_64
$ uname -s -r -m
Linux 6.6.87.2-microsoft-standard-WSL2 x86_64
$ uname -srm
Linux 6.6.87.2-microsoft-standard-WSL2 x86_64
$ uname -mrs
Linux 6.6.87.2-microsoft-standard-WSL2 x86_64
```

The last three commands produce exactly the same output. The program first collects all the switches and then writes the information in its own fixed order. To an option that it does not know, `uname` responds with an error message:

```console
$ uname -x
error: unexpected argument '-x' found

Usage: uname [OPTION]...

For more information, try '--help'.
```

The wording of the message differs slightly from one Linux to another; its meaning is the same everywhere.
::::

⁠**In short:** Options begin with a minus sign and set how a command works; short options can be bundled.

### The long option

<span class="anker" id="stufe-2-5"></span>

A single letter is quick to type but hard to remember: does `-r` stand for “release”, “recursive” or “reverse”? If you write down a command that others are meant to read, you would rather use whole words.

:::definition Definition 2.5 (Long option)
<span class="anker" id="satz-2-5"></span>

A __long option__ begins with two minus signs followed by a whole word, such as `--kernel-release`. Many short options have an equivalent long form. Long options cannot be bundled; each one is a word of its own.
:::

Almost all programs understand two long options: `--help` shows a short help text, `--version` the version of the program, as just now with `bash --version`.

::::beispiel The same question in long form
```console
$ uname --kernel-name --kernel-release
Linux 6.6.87.2-microsoft-standard-WSL2
$ uname --machine
x86_64
```

The first line corresponds to `uname -s -r`. For a short command at your own terminal, you type the short form; in instructions that someone else is meant to understand, the long form is often the better choice.
::::

⁠**In short:** Long options begin with two minus signs and a whole word; they are longer but self-explanatory.

:::hintergrund Abbreviated long options
Many programs also accept a long option in abbreviated form, as long as the abbreviation is unique: `uname --kernel-r` works like `uname --kernel-release`. If it is ambiguous, you get an error, because `--kernel` could mean `--kernel-name`, `--kernel-release` or `--kernel-version`. In instructions and saved commands, you still write long options out in full: if a new version of the program gets another option with the same beginning, an abbreviation that was unique until then becomes ambiguous.
:::

### The option with a value

<span class="anker" id="stufe-2-6"></span>

Some switches need an additional piece of information. “Show the first lines” is incomplete as long as nobody says how many.

:::definition Definition 2.6 (Option with a value)
<span class="anker" id="satz-2-6"></span>

An __option with a value__ requires an additional piece of information, such as a number. With a short option, the value follows as the next word or is attached directly: `-n 2` or `-n2`. With a long option, it follows an equals sign or comes as the next word: `--lines=2` or `--lines 2`.
:::

The command `head` shows the first lines of a file, ten without an option. With the option `-n` and a value, you set the number. Figure [8](#abb-8) takes such a line apart completely.

:::abbildung linux/k2zerlegt 8
The command line `head -n 2 /etc/os-release`, fully taken apart: the command, a short option with its value and an ordinary argument that names the file.
:::

::::beispiel Four ways of writing it, one result
You know the file `/etc/os-release` from [Chapter 1, Section 2.3](/wissen/en/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/drei-wege-zu-einem-eigenen-linux.html#stufe-2-3). Its first two lines, requested in four ways:

```console
$ head -n 2 /etc/os-release
PRETTY_NAME="Ubuntu 26.04.1 LTS"
NAME="Ubuntu"
$ head -n2 /etc/os-release
PRETTY_NAME="Ubuntu 26.04.1 LTS"
NAME="Ubuntu"
$ head --lines=2 /etc/os-release
PRETTY_NAME="Ubuntu 26.04.1 LTS"
NAME="Ubuntu"
$ head --lines 2 /etc/os-release
PRETTY_NAME="Ubuntu 26.04.1 LTS"
NAME="Ubuntu"
```

In the first line, `head` received three arguments: `-n`, `2` and `/etc/os-release`. `head` knows that the `2` belongs to the option and is not a file name because it has itself specified that `-n` requires a value.
::::

⁠**In short:** Some options require a value, which comes as the next word, is attached directly or follows an equals sign.

:::hintergrund Where the common conventions come from
It is no coincidence that almost all programs treat options the same way. The POSIX standard, which Unix-like systems have agreed on, recommends in its rules for the usage syntax of programs: options consist of a minus sign and a letter, several of them may be bundled behind one minus sign, and options come before the remaining arguments. The GNU project added the long options with two minus signs. Most programs do not split up their arguments themselves but leave that to a ready-made function that implements these rules. It comes from a program library, a collection of ready-made program parts that many programs share. On Linux, these functions usually even allow you to write options after the remaining arguments: `head /etc/os-release -n 1` works. On other Unix systems, this does not always work; if you want to be right everywhere, write the options first.
:::

### The end of options

<span class="anker" id="stufe-2-7"></span>

A program recognizes options by the minus sign. But what if an ordinary argument itself begins with a minus sign, such as a file that someone has named `-l`? The program would take it for an option.

:::abbildung linux/k2ende 9
The word `--` is a boundary: before it, the program checks whether a word is an option; after it, every word is an ordinary argument, even `-l`.
:::

:::definition Definition 2.7 (End of options)
<span class="anker" id="satz-2-7"></span>

The argument `--`, two minus signs on their own, ends the options. The program treats all the words after it as ordinary arguments, even if they begin with a minus sign. The `--` itself does not count as an argument.
:::

Almost all programs follow this convention, because it belongs to the same common conventions as bundling short options.

::::beispiel A file named -l
The command `ls` shows which files exist; its option `-l` turns this into a detailed list. With `--` in front of it, `-l` is no longer an option but the name of a file that `ls` looks for. Because the file does not exist, it reports an error, and that is exactly how you can tell that `-l` now counts as a name:

```console
$ ls -- -l
ls: cannot access '-l': No such file or directory
```

Some programs point out this way out themselves. `cat` has no option `-l` and, on Ubuntu 26.04, suggests passing the word as a file name with `--`:

```console
$ cat -l
error: unexpected argument '-l' found

  tip: to pass '-l' as a value, use '-- -l'

Usage: cat [OPTION]... [FILE]...

For more information, try '--help'.
```
::::

⁠**In short:** After `--`, every word is an ordinary argument, even if it begins with a minus sign.

:::merke Typical typing mistakes
<ul>

<li>

⁠**Forgotten space:** `uname-r` is a single word and thus an unknown command.

</li>

<li>

⁠**One space too many:** `uname - r` passes a lone minus sign and an `r`; `uname` knows neither of them and reports an error.

</li>

<li>

⁠**Upper and lower case mixed up:** `UNAME` is a different name from `uname`, and `-R` is a different option from `-r`.

</li>

<li>

⁠**Wrong slash:** Linux separates folders with `/`, not with `\` as Windows does.

</li>

</ul>
:::

### Exercises for Section [2](#stufe-2)

<span class="anker" id="stufe-2-8"></span>

:::aufgabe Exercise 4 ★ Taking command lines apart
<span class="anker" id="aufg-4"></span>

Split each line into the command, options (with their value, if they have one) and remaining arguments. You do not need to know the commands for this. (a) `ls -la /etc` (b) `cp -r urlaub sicherung` (c) `grep -i fehler protokoll.txt` (d) `head --lines=5 notizen.txt` (e) `tail -n 3 -- -liste.txt`

:::loesung
<ol class="al">

<li>

Command `ls`; the bundled short options `-l` and `-a`; argument `/etc`.

</li>

<li>

Command `cp`; option `-r`; arguments `urlaub` and `sicherung`.

</li>

<li>

Command `grep`; option `-i`; arguments `fehler` and `protokoll.txt`.

</li>

<li>

Command `head`; long option `--lines` with the value `5`; argument `notizen.txt`.

</li>

<li>

Command `tail`; short option `-n` with the value `3`; after that, `--` ends the options, and `-liste.txt` is an ordinary argument, even though it begins with a minus sign.

</li>

</ol>

What the options do is not the question here; the split follows solely from the rules for words, minus signs and values. Only for (d) and (e) do you need to know that `--lines` and `-n` require a value; the short help of each program tells you that.
:::
:::

:::aufgabe Exercise 5 ★★ Predict and check
<span class="anker" id="aufg-5"></span>

Predict what each line prints, and then check it on the computer: (a) `uname -mr` (b) `uname -r -s` (c) `uname --machine --kernel-name` (d) `uname - m` (e) `Uname -m` (f) `echo eins zwei drei` (German for “one two three”)

:::loesung
```console
$ uname -mr
6.6.87.2-microsoft-standard-WSL2 x86_64
$ uname -r -s
Linux 6.6.87.2-microsoft-standard-WSL2
$ uname --machine --kernel-name
Linux x86_64
$ echo   eins zwei     drei
eins zwei drei
```

In (a) to (c), `uname` determines the order itself: first the kernel name, then the version, last the processor type, no matter in which order the options are given. (d) `uname - m` passes the two arguments `-` and `m`; `uname` knows neither of them and reports `error: unexpected argument '-' found`. (e) `Uname` with a capital U is an unknown command. The shell finds nothing, and Ubuntu additionally suggests that there is a command `uname`; you do not need to install anything, you have just made a typo. (f) `echo` receives the three words `eins`, `zwei`, `drei` and writes them with a single space between them; it never learns about the spaces in the input.
:::
:::

:::aufgabe Exercise 6 ★★ Three lines in four ways
<span class="anker" id="aufg-6"></span>

Use `head` to display the first three lines of `/etc/os-release`, in four different ways of writing the option. Which of the following lines also work, and why? (a) `head /etc/os-release -n 3` (b) `head -n -- 3 /etc/os-release` (c) `head -- -n 3 /etc/os-release`

:::loesung
Four ways of writing it:

<ul>

<li>

`head -n 3 /etc/os-release`

</li>

<li>

`head -n3 /etc/os-release`

</li>

<li>

`head --lines=3 /etc/os-release`

</li>

<li>

`head --lines 3 /etc/os-release`

</li>

</ul>

All of them show the lines `PRETTY_NAME`, `NAME` and `VERSION_ID`.

(a) Works under Linux. The program library that parses the options also allows options after the remaining arguments (background box “Where the common conventions come from”):

```console
$ head /etc/os-release -n 3
PRETTY_NAME="Ubuntu 26.04.1 LTS"
NAME="Ubuntu"
VERSION_ID="26.04"
```

(b) Does not work. `-n` requires a value and takes the next word for it, that is, `--`. That is not a number, and `head` aborts:

```console
$ head -n -- 3 /etc/os-release
head: invalid number of lines: '-'
```

There is a reason why the message shows only one minus sign: for `head`, a minus sign in front of the number has a meaning of its own, as `head --help` reveals. So `head` removes the first minus sign from `--` and then finds only `-`. GNU `head` reports the same. The crucial point: here, `--` was not the end of options but the value of `-n`.

(c) Runs, but does something else. After `--`, `-n` and `3` are ordinary arguments, that is, file names. These files do not exist, and `head` reports two errors. The third file does exist; because `head` has received several file names, it writes a heading with the name in front of the lines and, without an option, shows the usual ten lines:

```console
$ head -- -n 3 /etc/os-release
head: cannot open '-n' for reading: No such file or directory
head: cannot open '3' for reading: No such file or directory
==> /etc/os-release <==
PRETTY_NAME="Ubuntu 26.04.1 LTS"
NAME="Ubuntu"
VERSION_ID="26.04"
VERSION="26.04.1 LTS (Resolute Raccoon)"
VERSION_CODENAME=resolute
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
```
:::
:::

:::aufgabe Exercise 7 ★★★ Who decides what?
<span class="anker" id="aufg-7"></span>

Explain, using the background box “The shell splits, the program interprets”: (a) Why does `uname -mrs` output the information in the same order as `uname -srm`? (b) Why can `echo` not know how many spaces there were between two words? (c) In `head -n 2 /etc/os-release`, how does `head` know that the `2` is not a file name?

:::loesung
(a) The shell passes `uname` the list `uname`, `-mrs`. What the letters mean and in which order the information appears is decided by `uname` alone. It first notes which pieces of information are requested and then writes them in its fixed order. The order of the letters plays no role in this.

(b) The shell splits the line before it starts `echo` and passes on only the words; the spaces between them serve only as separators and are not passed on. So `echo` receives `echo`, `Hallo`, `Welt` and knows nothing about the spaces.

(c) The shell does not know, and it does not need to know; it passes on three arguments of equal rank. `head` itself is programmed so that `-n` requires a value, and it therefore takes the next word, the `2`, as this value. Only `/etc/os-release` is a file name for `head`.
:::
:::

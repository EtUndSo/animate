---
title: Finding help
pfad: Computer Science / Linux and the Command Line / The Shell: First Commands
adresse: informatik/linux-und-kommandozeile/die-shell-erste-befehle
knoten: Chapter 2: The Shell: First Commands
order: 6070500
summary: Nobody knows all the options of all commands, and nobody has to.
tags: short help, help, manual page, man, pager, sections, apropos
lang: en
---

<span class="anker" id="stufe-4"></span>

:::zweck
Nobody knows all the options of all commands, and nobody has to. Linux comes with instructions for almost every command, in three forms: a short help from the program itself, the shell's help for builtin commands and a detailed manual with a search function. This section shows all three and when to use which.
:::

### The short help

<span class="anker" id="stufe-4-1"></span>

Often you know exactly which command you need but have forgotten an option. Then a cheat sheet that you can read at a glance is enough.

:::definition Definition 4.1 (Short help)
<span class="anker" id="satz-4-1"></span>

The __short help__ is a brief description that a program outputs when you call it with the option `--help`. It names the usage and the options, each with one line of explanation; then the program ends without doing anything else.
:::

::::beispiel The short help of uname
```console
$ uname --help
Print certain system information.
With no OPTION, same as -s.

Usage: uname [OPTION]...

Options:
  -a, --all               Behave as though all of the options -mnrsvo were specified.
  -s, --kernel-name       print the kernel name.
  -n, --nodename          print the nodename (the nodename may be a name that the system is known by
                          to a communications network).
  -r, --kernel-release    print the operating system release.
  -v, --kernel-version    print the operating system version.
  -m, --machine           print the machine hardware name.
  -o, --operating-system  print the operating system name.
  -h, --help              Print help
  -V, --version           Print version
```

Each line names a short option and its long form. The line `Usage:` shows the usage: `uname`, followed by any number of options. On other Linux systems, the wording is slightly different; the options are the same.
::::

⁠**In short:** `command --help` shows a program's options at a glance.

### Help for builtins

<span class="anker" id="stufe-4-2"></span>

Builtin commands are not program files. Usually, they also have no entry in the manual that the next subsection introduces: `man cd` only answers `No manual entry for cd`. The shell itself carries their instructions.

:::definition Definition 4.2 (help)
<span class="anker" id="satz-4-2"></span>

The builtin command __help__ shows the instructions for the shell's builtin commands. With a name as an argument, it describes that command; with the option `-d`, in a single line; without an argument, it lists all builtin commands.
:::

::::beispiel What cd, echo and type do
```console
$ help -d cd echo type
cd - Change the shell working directory.
echo - Write arguments to the standard output.
type - Display information about command type.
$ help cd
cd: cd [-L|[-P [-e]]] [-@] [dir]
    Change the shell working directory.

    Change the current directory to DIR.  The default DIR is the value of the
...
```

The first line of `help cd` shows the usage, the second one the purpose. Below them follow a good 30 more lines with all the details, which the chapter leaves out here. The usage contains optional parts in square brackets; the next subsection explains how to read them.
::::

⁠**In short:** For builtin commands, you ask the shell: `help` *name*.

### The manual page

<span class="anker" id="stufe-4-3"></span>

The short help is a cheat sheet. If you want to understand what exactly a command does, which files it reads and what its messages mean, you need the complete instructions. For this purpose, Unix systems have had a built-in manual for more than fifty years, divided into individual pages.

**Always the same layout.** Every page of the manual has the same structure so that you can quickly find your way around. Figure [14](#abb-14) shows the structure using the page for `uname`.

:::abbildung linux/k2manpage 14
The structure of a manual page, using `uname` as an example: a header line with the name and section number, then NAME, SYNOPSIS, DESCRIPTION, OPTIONS and more parts in a fixed order.
:::

:::definition Definition 4.3 (Manual page)
<span class="anker" id="satz-4-3"></span>

A __manual page__, or man page for short, is the detailed description of a command, a file format, a system call or another part of the system, collected in the manual that every Linux comes with. The command __man__ with the name as an argument displays it.
:::

The parts of a manual page always appear in the same order, although not every page has all of them:

<ul>

<li>

⁠**NAME:** the name and a one-line description.

</li>

<li>

⁠**SYNOPSIS:** the usage.

</li>

<li>

⁠**DESCRIPTION:** what the command does, often in detail.

</li>

<li>

⁠**OPTIONS:** every option with an explanation.

</li>

<li>

⁠**EXIT STATUS:** how the command reports success or failure.

</li>

<li>

⁠**FILES, ENVIRONMENT:** which files and settings it uses.

</li>

<li>

⁠**EXAMPLES:** examples, unfortunately not on every page.

</li>

<li>

⁠**SEE ALSO:** related pages.

</li>

</ul>

::::beispiel The page for uname
If you call `man uname`, the page fills the window. This is how it begins in a window 81 characters wide; in a wider or narrower window, `man` wraps the lines differently:

```text
UNAME(1)                     General Commands Manual                    UNAME(1)

NAME
       uname - Print certain system information.  With no OPTION, same as -s.

SYNOPSIS
       uname [-a|--all] [-s|--kernel-name] [-n|--nodename] [-r|--kernel-release]
       [-v|--kernel-version]  [-m|--machine] [-o|--operating-system] [-h|--help]
       [-V|--version]

DESCRIPTION
       Print certain system information.  With no OPTION, same as -s.

OPTIONS
       -a, --all
              Behave as though all of the options -mnrsvo were specified.

       -s, --kernel-name
              print the kernel name.

       -n, --nodename
              print the nodename (the nodename may be a name that the system  is
              known by to a communications network).
```

The header line names the page and, in parentheses, the number of the part of the manual in which it appears; this is the topic of subsection [4.5](#stufe-4-5).
::::

**Reading the usage.** The line under SYNOPSIS uses a compact notation that also appears in short help texts. Figure [15](#abb-15) shows it with two examples.

<ul>

<li>

Anything in **square brackets** may be left out.

</li>

<li>

A **vertical bar** separates alternatives, of which you choose one: `[-a|--all]` means “`-a` or `--all` or neither”.

</li>

<li>

⁠**Three dots** mean: the preceding item may be repeated. `[OPTION]...` stands for any number of options, including none.

</li>

<li>

In the terminal, text printed in **bold** is to be typed exactly as shown; **underlined** text or text in capital letters such as `FILE` is a placeholder that you replace with something suitable, such as a file name.

</li>

</ul>

:::abbildung linux/k2synopsis 15
Two usage lines, read step by step: `uname [-a|--all] [-s|--kernel-name] …` and `cat [OPTION]... [FILE]...`. Square brackets mean “may be left out”, the vertical bar “choose one of them”, three dots “may be repeated” and capital letters “put in something suitable here”.
:::

⁠**In short:** `man` *name* shows the complete instructions in a fixed layout; you read the usage under SYNOPSIS with the help of the characters `[ ]`, `|` and `...`.

:::hintergrund Where the manual pages come from
On 3 November 1971, the first edition of the “UNIX Programmer's Manual” by Ken Thompson and Dennis Ritchie appeared. It was already divided into numbered parts, from part I with the commands through the system calls to the file formats, and every entry had the same format with name, usage and description. Even then, a square bracket in the usage meant “may be left out” and three dots meant “may be repeated”. The pages were made from plain text files with formatting commands mixed in, from which a program typeset the finished page, and it is still like that today: every manual page is stored as a small, usually compressed text file with formatting commands in one of the folders `/usr/share/man/man1` to `man8`, and `man` typesets it when you call it, to fit the width of your window. Because the format has stayed the same for more than fifty years, you can read a manual page of today with the knowledge of back then. Not every page is easy: the page for bash has more than 7 000 lines.
:::

### The pager

<span class="anker" id="stufe-4-4"></span>

Even the short page for `uname` fills the window, and most manual pages are much longer. If `man` simply output a page, its beginning would scroll out of the top of the window before you could read it. That is why `man` does not display the page itself but passes it on to another program.

**A book you leaf through.** As in a book, you only ever see one page, leaf forward and back and can search for a word (a picture for orientation). The text stays as it is; only the part visible in the window moves.

:::definition Definition 4.4 (Pager)
<span class="anker" id="satz-4-4"></span>

A __pager__ is a program that shows a long text one screen at a time and lets you scroll and search in it. `man` passes every manual page to a pager; on Linux, this is usually the program `less`.
:::

Table [2](#tab-2) lists the most important keys of `less`. After `q`, you are back at the prompt.

<span class="anker" id="tab-2"></span>

**Table 2:** The most important keys in the pager `less`, in which `man` shows the manual pages.

| Key | Effect |
|---|---|
| Space bar, Page Down | one screen forward |
| `b`, Page Up | one screen back |
| Arrow keys | line by line |
| `/`*word* and Enter | search forward for *word* |
| `n` or `N` | next or previous hit |
| `g` or `G` | to the start or to the end |
| `h` | help on all keys |
| `q` | quit |

::::beispiel Finding an option in the manual page
You are looking for the option of `uname` that names the processor type, but all you remember is the word “machine”. Type `man uname`, then `/machine` and Enter. The pager jumps to the first hit and highlights it; it is already the line `[-m|--machine]` in SYNOPSIS. `n` jumps to the next hit, the explanation `-m, --machine` under OPTIONS. `q` ends the display.
::::

⁠**In short:** `man` shows its pages in the pager `less`: the Space bar pages forward, `/` searches, `q` quits.

### The sections of the manual

<span class="anker" id="stufe-4-5"></span>

The same name can refer to different things in the system. `uname` is a command, but it is also the name of the system call with which this command asks the kernel for its information. Both have a manual page, and the manual has to keep them apart.

:::abbildung linux/k2abschnitte 16
The manual as a shelf with numbered compartments. Under the name `uname`, there is one page in compartment 1 (commands) and one in compartment 2 (system calls); under `passwd`, one in compartment 1 and one in compartment 5 (file formats).
:::

:::definition Definition 4.5 (Section of the manual)
<span class="anker" id="satz-4-5"></span>

The manual is divided into numbered __sections__, one for each kind of content (Table [3](#tab-3)). You write a page together with its section as *name*(*number*), for example `uname(1)` for the command and `uname(2)` for the system call. `man` with a number before the name shows the page from that section; without a number, it shows the first page it finds, searching in a fixed order that starts with section 1.
:::

<span class="anker" id="tab-3"></span>

**Table 3:** The sections of the Linux manual. For work on the command line, you mainly need 1, 5 and 8.

| No. | Content | Example |
|---|---|---|
| 1 | Commands for all users | `uname(1)`, `ls(1)` |
| 2 | System calls of the kernel | `uname(2)`, `chdir(2)` |
| 3 | Functions of program libraries | `printf(3)` |
| 4 | Device files | `null(4)` |
| 5 | File formats | `passwd(5)`, `os-release(5)` |
| 6 | Games | `intro(6)` |
| 7 | Overviews and conventions | `man-pages(7)` |
| 8 | Commands for system administration | `lsblk(8)` |

::::beispiel uname twice, passwd twice
For a name, `whatis` lists the NAME line of every matching page, with its section; `man -f` does the same:

```console
$ whatis uname
uname (1)            - Print certain system information. With no OPTION, same...
uname (2)            - get name and information about current kernel
$ man -f passwd
passwd (1)           - change user password
passwd (1ssl)        - OpenSSL application commands
passwd (5)           - the password file
```

`passwd(1)` is the command you use to change your password; `passwd(5)` describes the file `/etc/passwd`, in which the system records its user accounts. `1ssl` is a subsection of 1 for the commands of the encryption program OpenSSL. You get the page from section 5 only with the number:

```text
PASSWD(5)                File Formats and Configuration               PASSWD(5)

NAME
       passwd - the password file

DESCRIPTION
       /etc/passwd contains one line for each user account, with seven fields
       delimited by colons (“:”). These fields are:
```

You type the command for this as `man 5 passwd`; `man passwd` alone shows the page from section 1.
::::

⁠**In short:** The manual has numbered sections; if a name occurs more than once, `man 5 passwd` selects the page from section 5.

### Searching the manual

<span class="anker" id="stufe-4-6"></span>

`man` helps only if you already know the name of a command. Often, though, you only know what you want to do: show the free memory, change the computer's name. Then you need a search across all pages.

:::abbildung linux/k2apropos 17
`apropos` searches a database of all NAME lines. The keyword `host name` matches two lines; each names the page, section and short description.
:::

:::definition Definition 4.6 (apropos)
<span class="anker" id="satz-4-6"></span>

The command __apropos__ searches the names and short descriptions of all manual pages for a keyword and lists the hits with their section. `man -k` does the same.
:::

The search covers only the one line under NAME, not the whole text of the pages, and these lines are in English. You write a keyword that consists of several words in straight quotes so that it arrives as a single argument.

::::beispiel Finding commands whose names you do not know
```console
$ apropos "host name"
hostname (1)         - show or set the system's host name
rust-hostname (1)    - Display or set the system's host name.
$ man -k "free and used"
free (1)             - Display amount of free and used memory in the system
$ apropos uptime
proc_uptime (5)      - system uptime
rust-uptime (1)      - Display the current time, the length of time the syste...
uptime (1)           - Tell how long the system has been running.
$ apropos xyzzy
xyzzy: nothing appropriate.
```

The hits whose names begin with `rust-` are a peculiarity of Ubuntu 26.04, which ships many core commands in a rewritten implementation; for your search, you read them like the page without `rust-`. For the last line, there is no page whose short description contains the word.
::::

⁠**In short:** `apropos` *keyword* finds manual pages whose short description contains the keyword.

:::hintergrund Why apropos sometimes finds nothing
`apropos` does not read the manual pages themselves; with thousands of pages, that would be too slow. It searches a small database that contains only the name, the section and the NAME line of each page. The program `mandb` builds this database, and Ubuntu brings it up to date after every installation of new programs. This results in three reasons for an empty search: the keyword appears in the text but not in the short description, as with `disk usage`; it is in another language, German for example, while the descriptions are in English; or the database is not yet up to date. If a word does not help, try a related one, such as `memory` instead of `RAM`.
:::

### Which help for what

<span class="anker" id="stufe-4-7"></span>

The three kinds of help complement one another. Which one fits depends on what you already know and what kind of command you are dealing with. Figure [18](#abb-18) sums up the way to the right one.

:::abbildung linux/k2hilfeweg 18
Which help for what: if you do not know the name, you search with `apropos`. If the command is built in, you ask `help`. For a program file, `--help` is often enough; `man` shows the complete instructions.
:::

::::beispiel Three questions, three ways
You want to know how long the computer has been running and do not know a command for it: `apropos uptime` or `apropos running` leads to `uptime(1)`. You have forgotten how `cd` jumps back to the previous folder: `type cd` says “builtin”, so `help cd`. You are looking for the option of `head` that sets the number of lines: `head --help` shows it as the second entry in the list.
::::

⁠**In short:** Name unknown: `apropos`; builtin: `help`; program file: `--help` for the overview, `man` for everything.

### Exercises for Section [4](#stufe-4)

<span class="anker" id="stufe-4-8"></span>

:::aufgabe Exercise 12 ★ The right help
<span class="anker" id="aufg-12"></span>

Which kind of help works for which command: `man`, `--help` or `help`? Try all three for `cd`, `uname`, `history` and `head`, and note which of them give an answer. Explain the pattern using Section [3](arten-von-befehlen.html#stufe-3).

:::loesung
| Command | `man` | `--help` | `help` |
|---|---|---|---|
| `cd` | no page | yes | yes |
| `uname` | yes | yes | no |
| `history` | wrong page | yes | yes |
| `head` | yes | yes | no |

The pattern follows from Section [3](arten-von-befehlen.html#stufe-3). `cd` and `history` are built in, so `help` knows them, and for builtins, bash also answers `--help`. `uname` and `head` are program files with their own short help and manual page; `help` does not know them and answers `no help topics match`. `man cd` finds nothing. `man history`, by contrast, shows a page from section 3 about the program library that programs use to manage a history, not the builtin command. This is a good reminder to ask `help` first for a builtin command.
:::
:::

:::aufgabe Exercise 13 ★★ Finding an option in the manual
<span class="anker" id="aufg-13"></span>

Open `man ls`. Using the pager's search, find the option with which `ls` sorts the files by size. Which option shows sizes in easily readable units such as `K` and `M`? Try `ls -S /etc` and compare it with `ls /etc`.

:::loesung
After `man ls`, you type `/size` and press Enter, and you jump from hit to hit with `n`. Under OPTIONS, it says:

```text
       -S     Sort by file size, largest first.
```

The easily readable units come from `-h`, long form `--human-readable`: `Print human readable file sizes (e.g. 1K 234M 56G)`. Under Ubuntu 26.04, this is the manual page of the uutils implementation; on a GNU system, the text reads differently, but the options `-S` and `-h` are the same. `ls /etc` shows the names alphabetically, `ls -S /etc` the largest first.
:::
:::

:::aufgabe Exercise 14 ★★ Same names, different pages
<span class="anker" id="aufg-14"></span>

(a) What do `printf(1)` and `printf(3)` describe? Find out with `whatis`. (b) Why does `man printf` show the page from section 1 and not the one from section 3? (c) In which section is the page for `os-release`, and what does it describe?

:::loesung
(a)

```console
$ whatis printf
printf (1)           - Print output based off of the format string and procee...
printf (3)           - formatted output conversion
```

`printf(1)` is a command that outputs text according to a template; `printf(3)` is a function in the program library of the C language that does the same inside a program.

(b) Without a number, `man` searches the sections in a fixed order that begins with section 1; section 3 comes only later. For the page from section 3, you type `man 3 printf`.

(c) `os-release(5)`, short description `Operating system identification`: the page describes the structure of the file `/etc/os-release` from [Chapter 1, Section 2.3](/wissen/en/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/drei-wege-zu-einem-eigenen-linux.html#stufe-2-3), that is, a file, and therefore it is in section 5.
:::
:::

:::aufgabe Exercise 15 ★★ Searching for commands
<span class="anker" id="aufg-15"></span>

Use `apropos` to find one command each that (a) shows the computer's name, (b) shows the used and free main memory, (c) shows the storage devices as a list. Note down your keyword. Why does `apropos festplatte` (`festplatte` is German for “hard disk”) find nothing?

:::loesung
```console
$ apropos "host name"
hostname (1)         - show or set the system's host name
rust-hostname (1)    - Display or set the system's host name.
$ man -k "free and used"
free (1)             - Display amount of free and used memory in the system
```

(a) `hostname`. (b) `free`; the keyword `memory` alone finds it too, but among more than a hundred other hits. (c) `apropos "block devices"` leads to `lsblk (8) - list block devices`; in Linux terminology, storage devices are called block devices. `apropos festplatte` reports `festplatte: nothing appropriate.`, because `apropos` searches only the short descriptions, and they are in English.
:::
:::

:::aufgabe Exercise 16 ★★★ Reading usage lines
<span class="anker" id="aufg-16"></span>

On an ordinary GNU system, the usage of `head` is `head [OPTION]... [FILE]...`. Which of the following lines match this form? (a) `head` (b) `head /etc/hostname /etc/os-release` (c) `head -n 1 -v /etc/hostname` (d) `head /etc/hostname -n 1`. How do you read `[-a|--all]` in the usage of `uname`, and may you write `uname -a --all`?

:::loesung
(a) matches: the options and the file names are both in square brackets, so they may be omitted; without file names, `head` then reads what you type. (b) matches: `[FILE]...` allows any number of file names. (c) matches: two options, `-n` with a value and `-v`, then a file name. (d) does not match the form, which puts the options before the file names; under Linux, the line works anyway, because the option parsing also allows them after the file names.

`[-a|--all]` means: `-a` or `--all` or neither of them, but not both. uutils takes this literally:

```console
$ uname -a --all
error: the argument '--all' cannot be used multiple times

For more information, try '--help'.
```

GNU `uname` is more lenient and simply outputs all the information for `gnuuname -a --all`. So the usage describes what is sure to work everywhere.
:::
:::

If you would like extra practice, the learning platform pwn.college offers short exercises in its course “Linux Luminarium”; the modules “Hello Hackers” and “Digesting Documentation” match this chapter: [https://pwn.college/linux-luminarium/](https://pwn.college/linux-luminarium/).

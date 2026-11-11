---
title: How the shell finds programs: PATH
pfad: Computer Science / Linux and the Command Line / How the Shell Reads a Command Line: Expansion, Quoting, Variables, Environment
adresse: informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung
knoten: Chapter 5: How the Shell Reads a Command Line: Expansion, Quoting, Variables, Environment
order: 6100600
summary: Chapter 2 introduced the search path, the list of directories in which the shell looks for programs.
tags: PATH
lang: en
---

<span class="anker" id="stufe-5"></span>

:::zweck
[Chapter 2](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/die-shell-erste-befehle.html) introduced the search path, the list of directories in which the shell looks for programs. This section shows that an environment variable lies behind it, by which rules the shell searches, why a program in the working directory does not simply start and how to change the search path.
:::

:::::vorwissen What you need for this: search path and kinds of commands

<span class="anker" id="stufe-5-1"></span>

<ul>

<li>

The search path is the list of directories in which the shell looks for a program file with the name of the command; it starts the first one it finds. Builtin commands and aliases need no search. `type` shows what lies behind a name ([Chapter 2, Sections 3.2](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/arten-von-befehlen.html#stufe-3-2) to 3.5).

</li>

<li>

On Ubuntu, `/bin` is merely a second name for `/usr/bin` ([Chapter 3, Section 8.6](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/inode-und-links.html#stufe-8-6)). `tree` draws a directory tree ([Chapter 3, Section 5.4](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-und-verzeichnisse-anlegen.html#stufe-5-4)). `ls -l` shows the permissions of a file as nine characters ([Chapter 3, Section 3.4](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/den-inhalt-eines-verzeichnisses-anzeigen.html#stufe-3-4)).

</li>

<li>

`tr` replaces characters in its standard input ([Chapter 4, Section 3.3](/wissen/en/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/eingaben-umleiten.html#stufe-3-3)). Exit status 127 means “command not found” ([Chapter 4, Section 5.3](/wissen/en/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/der-exit-status.html#stufe-5-3)).

</li>

</ul>

⁠**In short:** You need the search path, the kinds of commands with `type`, `tree`, `tr` and exit status 127.

:::::

### The variable PATH

<span class="anker" id="stufe-5-2"></span>

How does the shell know which directories belong to the search path? The answer is an environment variable that you can read and change like any other. Figure [20](#abb-20) shows how its value becomes a list.

:::abbildung linux/k5path 20
The value of `PATH` is one single text. The colons in it separate the directories; read from left to right, they give the order in which the shell searches.
:::

:::definition Definition 5.1 (PATH)
<span class="anker" id="satz-5-1"></span>

The environment variable __PATH__ contains the search path as text: the directories, separated by colons, in the order in which the shell searches them. An empty entry, that is, two colons in a row or a colon at the beginning or at the end, stands for the working directory.
:::

The standard for Unix shells lists the empty entry only as a leftover from old times; anyone who means the working directory should write `.`. Because `PATH` is an environment variable, every child receives the search path of its parent process.

::::beispiel Reading the search path
The value is long. So that each directory stands on a line of its own, `tr` replaces each colon with a line end; `head` shows the first nine:

```console
$ echo "$PATH" | tr ':' '\n' | head -n 9
/usr/local/sbin
/usr/local/bin
/usr/sbin
/usr/bin
/sbin
/bin
/usr/games
/usr/local/games
/usr/lib/wsl/lib
```

The first eight entries come from Ubuntu's default settings; `/usr/lib/wsl/lib` and the many Windows directories that follow it under WSL 2 are appended by WSL. Because `/bin` is a second name for `/usr/bin`, the shell finds some programs twice:

```console
$ type -a ls
ls is aliased to `ls --color=auto'
ls is /usr/bin/ls
ls is /bin/ls
```

`type -a` names all matches in the order of the search. The first one is started: the alias from [Chapter 2, Section 3.4](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/arten-von-befehlen.html#stufe-3-4) leads to `ls`, and the shell finds it in `/usr/bin`. The builtin command `command -v` answers more briefly: for each name, it writes only what the shell would start, the path for a program and the name for a builtin command.

```console
$ command -v tree cd
/usr/bin/tree
cd
```
::::

⁠**In short:** `PATH` is the search path as text, the directories separated by colons and in the order of the search.

### Command search

<span class="anker" id="stufe-5-3"></span>

With `PATH`, the rules of the search can be stated completely, including the case in which the name already contains a path.

:::satz Theorem 5.2 (Command search)
<span class="anker" id="satz-5-2"></span>

If the command name contains no slash, the shell, after checking for an alias, keyword, function and builtin command ([Chapter 2, Section 3.5](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/arten-von-befehlen.html#stufe-3-5)), goes through the directories from `PATH` from left to right and starts the first executable file with this name; it remembers the path it found for later. If it finds none, it reports the error and sets exit status 127. If the command name contains a slash, the shell does not search at all but starts exactly the file that the path designates.
:::

Figure [21](#abb-21) summarizes the way from the name to the started program as a decision tree.

:::abbildung linux/k5befehlssuche 21
Command search as a decision tree. First question: does the name contain a slash? Yes: the shell starts exactly this file. No: is it an alias, a keyword, a function or a builtin command? Then the shell handles it itself. Otherwise, it goes through the directories from `PATH` from left to right: as soon as it finds the program, it starts it and remembers the path; if it finds nothing, it reports “command not found” and sets exit status 127.
:::

::::beispiel With a path, there is no search
```console
$ /usr/bin/echo Hallo
Hallo
```

`echo` alone would be the builtin command. With the path `/usr/bin/echo`, the shell instead starts the program file of the same name, without searching.
::::

⁠**In short:** Without a slash, the shell searches in `PATH` and takes the first match; with a slash, it starts exactly the named file.

:::hintergrund The shell remembers programs it has found
So that it does not have to go through all the directories on every call, bash creates an entry in a table for every program it finds. The builtin command `hash` shows this table, and for a remembered program, `type` says “is hashed”. If you move a program after the shell has remembered it, the shell keeps trying the old location and reports that the file does not exist there; only `hash -r` empties the table, and the search starts anew. Every new assignment to `PATH` empties it as well.
:::

### A program in the working directory: ./

<span class="anker" id="stufe-5-4"></span>

If you put a program of your own in a directory that is not in the search path, the shell does not find it, even though it is right in front of you. For an experiment, you need a program. With the usual default settings, `cp` gives the copy the permissions of the original, including the indication that the file may be started as a program; a copy of `tree` is therefore again a program that can be started. Create such a copy named `meinbaum` (German for “mytree”) in your practice directory:

```console
$ cp /usr/bin/tree ./meinbaum
```

Figure [22](#abb-22) shows what the shell does with two ways of writing this name.

:::abbildung linux/k5punktslash 22
At the top, `meinbaum`: no slash, so the shell searches the directories from `PATH`. The working directory `/home/student/linuxk5` is not among them; the search ends with no match and exit status 127. At the bottom, `./meinbaum`: the slash turns the name into a path, and the shell starts the file in the working directory directly.
:::

::::beispiel With and without ./
```console
$ meinbaum
meinbaum: command not found
$ echo $?
127
$ ./meinbaum urlaub
urlaub
├── 2025
│   ├── sommer
│   └── winter
└── 2026
    ├── sommer
    └── winter

7 directories, 0 files
```

Without a path, the shell does not find `meinbaum`. With `./` in front, it is a path relative to the working directory ([Chapter 3, Section 2.5](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/das-arbeitsverzeichnis-und-pfade.html#stufe-2-5)), and the program draws the tree that brace expansion created in subsection [1.6](expansion-muster-klammern-und-tilde.html#stufe-1-6); `tree` counts the starting directory too.
::::

:::satz Theorem 5.3 (Program outside the search path)
<span class="anker" id="satz-5-3"></span>

You start a program that is not in any directory from `PATH` with a path that contains a slash: `./program` in the working directory, otherwise with an absolute or relative path.
:::

:::warnung Not every program tolerates a new name
This applies to the uutils implementation in Ubuntu 26.04: most core commands there are one single multicall program that recognizes from the name it was called by which command it is supposed to be ([Chapter 2, Section 7.2](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/zwei-fassungen-der-grundbefehle-gnu-und-uutils.html#stufe-7-2)). A renamed copy of it no longer knows what to do:

```console
$ cp /usr/bin/date ./meindatum
$ ./meindatum -d 2026-12-24 +%A
coreutils: unknown program 'meindatum'
$ cp /usr/bin/gnudate ./meindatum2
$ ./meindatum2 -d 2026-12-24 +%A
Thursday
```

The GNU implementation `gnudate` is a program of its own and also works under a new name; on systems with GNU coreutils, such as Debian, this also applies to `date` itself. For experiments of this kind, you therefore use a standalone program such as `tree`.
:::

⁠**In short:** The working directory is not part of the search path; you start a program there with `./`.

:::hintergrund Why the working directory is not in the search path
It used to be different. In the guide to the Bourne shell from 1978, the shell searches the current directory first by default, then `/bin` and `/usr/bin`, and the example there begins `PATH` with a colon, that is, with the working directory. Today, the working directory is missing from the default settings of the distributions; since its version 2.24 from 2016, the program library glibc, on which almost all Linux programs are built, also no longer searches it when it starts other programs and `PATH` is missing.

The manuals give hardly any reasons for this. Reasoning it out yields two. First, a command should mean the same program everywhere: `ls` is `/usr/bin/ls` in every directory, no matter where you are. If the working directory were in the search path, the meaning of a command would depend on which files happen to be there. Second, it would be dangerous. If someone put a program named `ls` in a directory that others also enter, such as `/tmp`, then anyone who typed `ls` there would start this foreign program, and with their own permissions. If the working directory were at the end of the search path, the real `ls` would win, but a program named after a typo, such as `sl`, would still run. The small effort of typing `./` is the price for commands that always mean the same thing.
:::

### Changing PATH

<span class="anker" id="stufe-5-5"></span>

For your own programs, `./` becomes tedious in the long run, and from another directory you would have to type the whole path. It is more convenient to add the directory with your own programs to the search path. Because `PATH` is a variable, this works with an assignment.

::::beispiel For one command and for the whole session
With an assignment before the command, the changed search path applies only to this one command:

```console
$ PATH="$PWD:$PATH" meinbaum urlaub
urlaub
├── 2025
│   ├── sommer
│   └── winter
└── 2026
    ├── sommer
    └── winter

7 directories, 0 files
$ meinbaum
meinbaum: command not found
```

`$PWD` inserts the working directory, `$PATH` the old search path; a colon stands between them. Afterward, everything is as before. For the whole session, you create a directory of your own for programs and put it at the front of the search path:

```console
$ mkdir bin
$ cp /usr/bin/tree bin/baum
$ PATH="$HOME/linuxk5/bin:$PATH"
$ baum urlaub
urlaub
├── 2025
│   ├── sommer
│   └── winter
└── 2026
    ├── sommer
    └── winter

7 directories, 0 files
$ type baum
baum is hashed (/home/student/linuxk5/bin/baum)
```

An `export` is not necessary, because `PATH` was already in the shell's environment when the shell started and is therefore marked (subsection [4.4](umgebung-und-vererbung.html#stufe-4-4)). `type` reports that the shell has remembered the path. The change applies until the shell ends.
::::

The assignment builds the new value from the old one: parameter expansion inserts the previous text for `$PATH`, and in front of it come the new directory and a colon. Figure [23](#abb-23) shows this and, next to it, what happens when the old text is missing. The place where you insert the directory decides the priority. If it is at the front, its programs win even against programs of the system with the same name; if it is at the back, as in `PATH="$PATH:$HOME/linuxk5/bin"`, the system's programs win.

:::abbildung linux/k5pathneu 23
How an assignment changes the search path. At the top, `PATH="$HOME/linuxk5/bin:$PATH"`: the shell inserts the old text for `$PATH` and puts the new directory in front of it with a colon; the old entries remain and move back one place. At the bottom, `PATH=/gibtsnicht` (German for “doesnotexist”): the old text does not appear in the assignment, and the list consists only of this one entry.
:::

:::warnung Do not damage the search path
Always append new directories to the old value, as above with `$PATH`. An assignment that replaces the old value takes all programs away from the shell:

```console
$ PATH=/gibtsnicht ls
Command 'ls' is available in the following places
 * /bin/ls
 * /usr/bin/ls
The command could not be located because '/usr/bin:/bin' is not included in the PATH environment variable.
ls: command not found
$ ls notiz.txt
notiz.txt
```

Here the broken search path applied only to one command; afterward, `ls` works again. The whole message comes from a helper program that Ubuntu sets up for this case: if the shell does not find a command, it calls the helper program, which looks for programs of that name. Without this helper program, for example on Debian, bash itself reports only `bash: ls: command not found`. If the search path is damaged for the whole session, close the terminal and open a new one. Also, never put `.` or an empty entry into the search path.
:::

⁠**In short:** `PATH="directory:$PATH"` puts a directory of your own at the front of the search path; at the front means priority, and the old value must be kept.

### Exercises for Section [5](#stufe-5)

<span class="anker" id="stufe-5-6"></span>

:::aufgabe Exercise 17 ★ Exploring your own search path
<span class="anker" id="aufg-17"></span>

(a) How many directories are in your `PATH`? Count them with a pipeline. (b) Which directory does the shell search first? (c) Where are `tree` and `bash`? Use `type -a`, and explain why each one appears twice.

:::loesung
```console
$ echo "$PATH" | tr ':' '\n' | wc -l
53
$ echo "$PATH" | tr ':' '\n' | head -n 1
/usr/local/sbin
$ type -a tree bash
tree is /usr/bin/tree
tree is /bin/tree
bash is /usr/bin/bash
bash is /bin/bash
```

(a) `tr` turns each colon into a line end, and `wc -l` counts the lines. On the test system, there are 53, because WSL appends many directories from Windows; on a Linux without WSL, there are usually eight to ten. (b) The first one is `/usr/local/sbin`. (c) Both are in `/usr/bin`. Because `/bin` is a second name for `/usr/bin` and both are in the search path, `type -a` finds each program twice; the first match is the one that gets started.
:::
:::

:::aufgabe Exercise 18 ★★ Three ways to a program
<span class="anker" id="aufg-18"></span>

Copy `tree` as `meinbaum` into your practice directory if it is not already there. Predict which of these lines start the program, and check it with the subdirectory `urlaub/2025` as the argument: (a) `meinbaum` (b) `./meinbaum` (c) `PATH="$PWD:$PATH" meinbaum` (d) from your home directory, `linuxk5/meinbaum`. Which exit status does (a) leave behind? Why does (d) work even though the path does not begin with `./`?

:::loesung
```console
$ cp /usr/bin/tree ./meinbaum
$ meinbaum
meinbaum: command not found
$ echo $?
127
$ ./meinbaum urlaub/2025
urlaub/2025
├── sommer
└── winter

3 directories, 0 files
$ PATH="$PWD:$PATH" meinbaum urlaub/2025
urlaub/2025
├── sommer
└── winter

3 directories, 0 files
$ cd ..
$ linuxk5/meinbaum linuxk5/urlaub/2025
linuxk5/urlaub/2025
├── sommer
└── winter

3 directories, 0 files
$ cd linuxk5
```

(a) Without a slash, the shell searches only the directories from `PATH`; the practice directory is not one of them. Exit status 127. (b) The slash turns the name into a path, and the shell starts the file directly. (c) For this one command, the working directory is at the front of the search path. (d) `linuxk5/meinbaum` contains a slash, so the shell does not search but follows the relative path from the home directory. What matters is not `./` but only the slash.
:::
:::

:::aufgabe Exercise 19 ★★★ A fake cat
<span class="anker" id="aufg-19"></span>

In the practice directory, create a directory `falle` (German for “trap”) and copy `tree` into it, this time under the name `cat`. Predict what `PATH="$PWD/falle:$PATH" cat einkauf.txt` outputs, and check it. What does `cat einkauf.txt` output afterward, without the assignment? Use the result to explain what would happen if the working directory were at the front of the search path and someone put a file named `cat` in a directory that you enter.

:::loesung
```console
$ mkdir falle
$ cp /usr/bin/tree falle/cat
$ PATH="$PWD/falle:$PATH" cat einkauf.txt
einkauf.txt  [error opening dir]

0 directories, 1 file
$ cat einkauf.txt
Milch
Brot
Äpfel
Kaffee
```

For the first command, `falle` is at the front of the search path. The shell finds a file named `cat` there first and starts it; in truth, it is `tree`, which tries to open `einkauf.txt` as a directory and fails. Without the assignment, the normal search path applies again, and the real `cat` shows the list. If the working directory were at the front of the search path, every directory you enter would be such a trap: if it contained a file `cat`, that file would run instead of the real program, with your permissions. Here the program was harmless; a foreign program could change files unnoticed and then call the real `cat`, so that you notice nothing.
:::
:::

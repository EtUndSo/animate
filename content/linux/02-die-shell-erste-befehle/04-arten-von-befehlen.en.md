---
title: Kinds of commands
pfad: Computer Science / Linux and the Command Line / The Shell: First Commands
adresse: informatik/linux-und-kommandozeile/die-shell-erste-befehle
knoten: Chapter 2: The Shell: First Commands
order: 6070400
summary: Different things can be behind the first word of a command line: a program of its own on the disk, a command that the shell handles itself or a short name for a longer command.
tags: program file, search path, builtin command, alias
lang: en
---

<span class="anker" id="stufe-3"></span>

:::zweck
Different things can be behind the first word of a command line: a program of its own on the disk, a command that the shell handles itself or a short name for a longer command. This section introduces the three kinds, explains why some commands have to be part of the shell and shows how to find out what is behind a name.
:::

### The program file

<span class="anker" id="stufe-3-1"></span>

When you type `uname`, a program runs that is not part of the shell. It is stored as a file on the storage device, like a photo or a letter, except that it contains instructions for the processor.

:::definition Definition 3.1 (Program file)
<span class="anker" id="satz-3-1"></span>

A __program file__ is a file that contains an executable program. Most commands are program files; on Linux, they are mainly in the folder `/usr/bin`.
:::

::::beispiel Starting a program by its full name
The full name of the program file of `uname` is `/usr/bin/uname`: the file `uname` in the folder `/usr/bin`. You can also start it by this name, with the same result:

```console
$ /usr/bin/uname -r
6.6.87.2-microsoft-standard-WSL2
```

Nobody types this in everyday work; `uname` alone is enough. So the shell finds the file by itself.
::::

⁠**In short:** Most commands are program files, files with an executable program in them.

### The search path

<span class="anker" id="stufe-3-2"></span>

When you type just `uname`, the shell has to find the right file by itself. Searching the entire storage device would be far too slow, and there could be several files with this name.

**A fixed list of folders.** The shell does not search the entire storage device, only a short list of folders that contain programs, and always in the same order. Figure [10](#abb-10) shows the search for `uname`.

:::abbildung linux/k2suche 10
The shell searches for the command `uname` in the folders of the search path, one after another. In `/usr/bin`, it finds the program file `uname` and starts it; it no longer looks at the remaining folders.
:::

:::definition Definition 3.2 (Search path)
<span class="anker" id="satz-3-2"></span>

The __search path__ is the list of folders in which the shell looks for a program file with the name of the command; it starts the first one it finds. On Ubuntu, it includes `/usr/local/bin`, `/usr/bin` and `/bin`, among others.
:::

The command `which` names the program file that the shell would find for a name in the search path. Under WSL 2, WSL also appends the folders of the Windows programs to the end of the search path; that is why a Windows program such as `explorer.exe` from [Chapter 1, Section 4.6](/wissen/en/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/wsl-2-linux-neben-windows.html#stufe-4-6) also starts there.

::::beispiel Where the programs are
```console
$ which uname
/usr/bin/uname
$ which head
/usr/bin/head
$ which bash
/usr/bin/bash
```

The shell itself is an ordinary program file, too: `/usr/bin/bash`.
::::

⁠**In short:** The shell looks for program files in the folders of the search path, one after another, and starts the first one that matches.

### The builtin command

<span class="anker" id="stufe-3-3"></span>

If you ask `which` about `cd` on Ubuntu, you get no answer, and yet `cd` reliably changes the folder. So there are commands that are not files.

```console
$ which cd
```

:::definition Definition 3.3 (Builtin command)
<span class="anker" id="satz-3-3"></span>

A __builtin command__ is a command that the shell runs itself, without starting another program. Its program code is part of the shell, not of a file of its own.
:::

The command `type`, itself a builtin, tells you whether a name is a builtin command. For program files, it names the location of the file.

::::beispiel Builtin or file?
```console
$ type cd
cd is a shell builtin
$ type exit
exit is a shell builtin
$ type type
type is a shell builtin
$ type uname
uname is /usr/bin/uname
```

“Shell builtin” is the usual technical term for a builtin command. bash handles `cd`, `exit` and `type` itself; for `uname`, it starts the file `/usr/bin/uname`.
::::

**Why cd has to be built in.** Every running program has its own current folder, just as each shell in subsection [1.5](terminal-und-shell.html#stufe-1-5) had its own. When the shell starts a program, the program receives a copy of the shell's current folder. If the program changes this folder, it changes only its copy, and when it ends, the copy is lost. A program `/usr/bin/cd` could therefore achieve nothing: it would change the folder and end immediately, and the shell would be exactly where it was before. Figure [11](#abb-11) shows both cases. Only the shell itself can change its own folder, so `cd` has to be part of the shell. The same applies to `exit`, which is supposed to end the shell itself.

:::abbildung linux/k2cd 11
Left: an imagined program `cd`. It changes only its own copy of the folder and ends; the shell stays in `~`. Right: the builtin command. The shell changes its own folder, and the prompt shows `/etc`.
:::

⁠**In short:** The shell handles builtin commands itself; commands such as `cd` and `exit`, which change the shell itself, have to be built in.

:::hintergrund What system calls and the standard say about it
The kernel manages the current folder separately for each running program. The system call with which a program changes it is called `chdir`, and according to its description, it affects only the calling program itself. A newly started program inherits a copy of the folder of the program that started it, but it can never change that program's folder in return. The POSIX standard explicitly concludes from this that `cd` must always be built into the shell, because it affects the environment of the shell itself. For the same reason, `exit`, `history` and `type` are built in: the first ends the shell, the second reads its list of typed commands, and the third asks what the shell would do with a name. Other commands are built in only for speed; see the next box.
:::

:::hintergrund Why some commands exist twice
With the option `-a`, `type` shows all locations of a name, not just the first:

```console
$ type -a echo
echo is a shell builtin
echo is /usr/bin/echo
echo is /bin/echo
```

So `echo` exists both as a builtin and as a file. The builtin version is faster because the shell does not have to start a new program for it, and it wins because the shell checks builtin commands before the search path. You still need the file: some programs start other programs themselves, and they can start only files, not parts of a shell. POSIX therefore requires that standard commands such as `echo`, `printf`, `pwd` and `test` also exist as files; `cd` is exempt because a file with this name could achieve nothing. Older versions of the standard required a file for it, too; that is why some distributions, such as Fedora, still ship a file `/usr/bin/cd`, which of course cannot change the shell's folder either. Both `/usr/bin/echo` and `/bin/echo` appear because on today's systems, `/bin` is just a second name for the folder `/usr/bin` and both are in the search path; it is the same file.
:::

### The alias

<span class="anker" id="stufe-3-4"></span>

If you ask `type` about `ls` on Ubuntu, you get a third answer, neither “builtin” nor a file:

```console
$ type ls
ls is aliased to `ls --color=auto'
```

So if you type `ls`, you do not get exactly `ls` at all.

**A shortcut that gets replaced.** Like a text shortcut on a phone that replaces “omw” with “On my way!” as you type, the shell swaps certain command names for a stored text before it processes the line any further (a picture for orientation). Figure [12](#abb-12) shows the swap.

:::abbildung linux/k2alias 12
The alias `ls`: while reading the line, the shell replaces the first word with the stored text `ls --color=auto`. Only then does it search for the command `ls` and find the program file.
:::

:::definition Definition 3.4 (Alias)
<span class="anker" id="satz-3-4"></span>

An __alias__ is a name that the shell replaces with a stored text while reading a command line if the name stands at the start as a command. Only then does the shell search for the command at the front of the replaced text.
:::

Ubuntu stores a few aliases in every session. `ls` becomes `ls --color=auto` so that the list appears in color, and `ll` becomes `ls -alF`, a detailed list. Aliases apply only in sessions in which a person types; a program that starts `ls` itself gets the ordinary program file.

::::beispiel Ubuntu's shortcuts
```console
$ type ll
ll is aliased to `ls -alF'
$ type la
la is aliased to `ls -A'
```

There is no command `ll` as a file. It exists only as an alias in your session, and before the search, the shell turns it into `ls -alF`, which the alias `ls` in turn makes into `ls --color=auto -alF`.
::::

⁠**In short:** An alias is a shortcut that the shell replaces with a longer command before the search.

### What is behind a name: type and which

<span class="anker" id="stufe-3-5"></span>

With `type` and `which`, there are two tools for finding out what is behind a command name. They do not always give the same answer, and the reason for this tells you a lot about the shell.

:::abbildung linux/k2arten 13
How the shell resolves a name, as a decision chart: first alias, then keyword, function and builtin command, and finally the search path. `type` knows all the steps because it is part of the shell; `which` is a program file of its own and sees only the search path.
:::

`type` is built into the shell and therefore knows everything the shell knows: aliases, builtin commands and the program files in the search path. `which`, by contrast, is itself a program file, `/usr/bin/which`. As a program of its own, it sees only the folders of the search path, not the inside of the shell that started it. For builtin commands and aliases, it therefore finds nothing, or only the file that would never be used. Table [1](#tab-1) compares the two.

<span class="anker" id="tab-1"></span>

**Table 1:** `type` and `which` compared. Only `type` describes what really happens when you type the name.

| Name | `type` answers | `which` answers |
|---|---|---|
| `uname` | `uname is /usr/bin/uname` | `/usr/bin/uname` |
| `cd` | `cd is a shell builtin` | nothing |
| `echo` | `echo is a shell builtin` | `/usr/bin/echo`, which is not used when you type the name |
| `ls` | `` ls is aliased to `ls --color=auto' `` | `/usr/bin/ls`, without the alias |
| `ll` | `` ll is aliased to `ls -alF' `` | nothing |

::::beispiel The short answer and all answers
With `-t`, `type` answers with a single word per name; with `-a`, it names all locations in the order in which the shell checks them:

```console
$ type -t ls cd uname
alias
builtin
file
$ type -a ls
ls is aliased to `ls --color=auto'
ls is /usr/bin/ls
ls is /bin/ls
$ which ls
/usr/bin/ls
```

The word `file` stands for a program file. The first line of `type -a ls` is the one that applies when you type the name.
::::

⁠**In short:** `type` says what the shell does with a name; `which` only finds program files in the search path.

:::hintergrund How the shell finds a command
For the first word of a line, bash proceeds in a fixed order.

<ol>

<li>

While still reading the line, it replaces an alias with its text. That is why the alias comes before all other steps.

</li>

<li>

If the word is a keyword of the shell language, such as `if`, it processes it itself; `type if` answers `if is a shell keyword`.

</li>

<li>

If someone has defined a *function* with this name in the session, a small command made of shell commands, it runs the function. This chapter does not define any.

</li>

<li>

If it is a builtin command, it runs it.

</li>

<li>

Only then does it search the search path. When it has found a name once, it remembers the location so that it does not have to search the next time.

</li>

</ol>

If the word contains a slash, such as `/usr/bin/uname`, it does not search at all but starts exactly this file. If it finds nothing, it reports `command not found`; on Ubuntu, a small helper program then also checks whether a command with a similar name could be installed. It fits the picture that on Debian and Ubuntu, `which` is itself just a short file of shell commands that queries the folders of the search path; its manual page says explicitly that it searches only the search path. So if you want to know what really happens when you type a name, ask `type`, which the POSIX standard provides for exactly this purpose.
:::

### Exercises for Section [3](#stufe-3)

<span class="anker" id="stufe-3-6"></span>

:::aufgabe Exercise 8 ★ Classifying eight names
<span class="anker" id="aufg-8"></span>

Use `type` to find out what is behind these names, and assign each of them to one of the three kinds: `cd`, `ls`, `echo`, `pwd`, `type`, `uname`, `history`, `ll`. Which of them also exist as program files? Check with `type -a`.

:::loesung
```console
$ type -a cd ls echo pwd type uname history ll
cd is a shell builtin
ls is aliased to `ls --color=auto'
ls is /usr/bin/ls
ls is /bin/ls
echo is a shell builtin
echo is /usr/bin/echo
echo is /bin/echo
pwd is a shell builtin
pwd is /usr/bin/pwd
pwd is /bin/pwd
type is a shell builtin
uname is /usr/bin/uname
uname is /bin/uname
history is a shell builtin
ll is aliased to `ls -alF'
```

`cd`, `echo`, `pwd`, `type` and `history` are built in. `ls` and `ll` are aliases. `uname` is a program file. `echo`, `pwd` and, behind the alias, `ls` also exist as program files. Each file appears twice, under `/usr/bin` and under `/bin`, because both folders are in the search path and `/bin` is only a second name for `/usr/bin`. The first line for each name is the one that applies when you type it.
:::
:::

:::aufgabe Exercise 9 ★★ type versus which
<span class="anker" id="aufg-9"></span>

Predict what `which` outputs for `cd`, `ll`, `uname` and `echo`, and check. For which names does `which` give a misleading answer, and why?

:::loesung
```console
$ which cd
$ which ll
$ which uname
/usr/bin/uname
$ which echo
/usr/bin/echo
```

For `cd` and `ll`, `which` outputs nothing: `cd` is built in, `ll` is only an alias, and `which`, as a separate program, can see neither of them. For `uname`, the answer is correct. It is misleading for `echo`: when you type it, the builtin version runs, not `/usr/bin/echo`. Equally misleading is `which ls` with `/usr/bin/ls`, because when you type it, the alias `ls --color=auto` applies first. The reason is the same in both cases: `which` searches only the folders of the search path and knows nothing about the inside of the shell that started it.
:::
:::

:::aufgabe Exercise 10 ★★ A program named cd
<span class="anker" id="aufg-10"></span>

Suppose there were a program file `/usr/bin/cd` that changes the current folder when it starts and then exits. Describe step by step what happens when you type `/usr/bin/cd /etc`; the slash at the front makes sure that the shell starts exactly this file. Where is the shell afterward? Why would it not help if the program ran longer?

:::loesung
The shell finds no alias and no builtin command, because the name contains a slash, and it starts the file `/usr/bin/cd` as a new program with the argument `/etc`. The program receives a copy of the shell's current folder, that is, `/home/student`. It changes its own current folder to `/etc` and exits. With that, its copy is gone as well. The shell shows the prompt again, and with `~`, because its own folder was never touched. A program that runs longer does not help either: it could change its own folder as often as it likes, but it never reaches the shell's, because the kernel gives each running program a current folder of its own and the system call `chdir` affects only the calling program.
:::
:::

:::aufgabe Exercise 11 ★★★ What has to be built in?
<span class="anker" id="aufg-11"></span>

For each command, decide whether it *has to* be built in, is built in only for speed or could just as well be a program file, and give your reasons: (a) `exit`, (b) `echo`, (c) `history`, (d) `uname`, (e) `type`.

:::loesung
(a) `exit` has to be built in. It is supposed to end the shell itself; another program could only end itself.

(b) `echo` is built in only for speed. A program `/usr/bin/echo` does the same job, but it first has to be started for that. The builtin version saves this effort, which counts when there are many calls.

(c) `history` has to be built in. The history is in the shell's main memory; no other program can get at this memory. At most, it could read the file `.bash_history`, and that file is written only at the end of the session.

(d) `uname` can be a program file without any problem, and it is one: it asks the kernel for information about the system and needs nothing from the shell for this.

(e) `type` has to be built in. It is supposed to say what the shell would do with a name, and for that it needs the shell's aliases and its list of builtin commands. A separate program such as `which` sees neither of them.
:::
:::

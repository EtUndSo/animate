---
title: Startup files and aliases
pfad: Computer Science / Linux and the Command Line / How the Shell Reads a Command Line: Expansion, Quoting, Variables, Environment
adresse: informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung
knoten: Chapter 5: How the Shell Reads a Command Line: Expansion, Quoting, Variables, Environment
order: 6100700
summary: Everything that you have set up in a shell so far disappears with it.
tags: startup file, source, login shell, alias
lang: en
---

<span class="anker" id="stufe-6"></span>

:::zweck
Everything that you have set up in a shell so far disappears with it. This section shows which files the shell reads every time it starts, how to set up variables, the search path and aliases in them permanently and how to make a changed file take effect immediately.
:::

### The startup file

<span class="anker" id="stufe-6-1"></span>

A new shell starts almost from scratch: it receives the environment of its parent process, nothing else. It does not know a variable that you have not exported:

```console
$ wohnort=Hamburg
$ bash -i -c 'echo Wohnort: $wohnort Ende'
Wohnort: Ende
```

The option `-i` makes the new bash an interactive shell, like the shell you type into. Even so, it does not know `wohnort`. And yet every new shell has the aliases `ll` and `la` from [Chapter 2, Section 3.4](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/arten-von-befehlen.html#stufe-3-4). It must get these settings from somewhere every time it starts. Figure [24](#abb-24) shows where from.

:::abbildung linux/k5startdatei 24
The start of an interactive bash. Before the first prompt appears, the shell reads the file `~/.bashrc` line by line and runs each line as if it had been typed, among them `alias ll='ls -alF'` and `alias la='ls -A'`. Only then does it wait for your commands, and the aliases are there.
:::

:::definition Definition 6.1 (Startup file)
<span class="anker" id="satz-6-1"></span>

A __startup file__ is a text file with commands for the shell that the shell reads and runs when it starts, as if you had typed the lines. If you start a new interactive bash in a terminal, it reads the file `~/.bashrc` in your home directory.
:::

The ending “rc” (short for “run commands”) is common on Unix for files with startup commands; the dot at the beginning makes the file a hidden file. On Ubuntu, bash first reads the file `/etc/bash.bashrc`, which applies to all users. Ubuntu creates a `~/.bashrc` with sensible default settings for every new user.

::::beispiel Where the aliases come from
```console
$ grep -n "alias l" ~/.bashrc
78:    alias ls='ls --color=auto'
91:alias ll='ls -alF'
92:alias la='ls -A'
93:alias l='ls -CF'
```

`grep` shows the lines of the file that contain `alias l`, with their number in front. This is where the aliases that [Chapter 2](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/die-shell-erste-befehle.html) found already in place come from: every new interactive bash runs these lines. The indented line 78 is in a part of the file that the shell runs only if the helper program `dircolors` for the colors of `ls` exists; on Ubuntu, that is the case.
::::

⁠**In short:** A startup file contains commands that the shell runs every time it starts; a new interactive bash reads `~/.bashrc`.

:::hintergrund Why ~/.bashrc does nothing without a terminal
Ubuntu's `~/.bashrc` begins with a check whether the shell is interactive and stops immediately if it is not. A shell that runs a text with `bash -c` usually does not read the file at all. There is one exception, however: if bash starts without a terminal over a network connection, for example because someone sends a single command from another computer, it does read `~/.bashrc`. The check is there for this case. That way, settings for working at the terminal, such as aliases and the look of the prompt, do not interfere with commands that run without a terminal.
:::

### source

<span class="anker" id="stufe-6-2"></span>

A change to `~/.bashrc` takes effect only in the next shell, because the running shell already read the file when it started. You could open a new terminal. It is simpler to have the running shell read the file again.

:::definition Definition 6.2 (source)
<span class="anker" id="satz-6-2"></span>

The builtin command __source__ `file` reads the file and runs its lines in the running shell, as if you had typed them. A single dot is a short form: `. file` means the same.
:::

What matters is “in the running shell”: no child process comes into being. Assignments, `export` and aliases from the file therefore remain in effect in your shell after the file has been read to the end. Figure [25](#abb-25) contrasts this with a child process.

:::abbildung linux/k5source 25
The same file `farbe.txt` with the line `farbe=blau` (`farbe` is German for “color”, `blau` for “blue”), read twice. At the top in a child shell: the assignment ends up in the child's copy and disappears with the child. At the bottom with `source`: the line runs in the shell itself, and `farbe` stays set afterward.
:::

::::beispiel In the child and in the shell
```console
$ echo farbe=blau > farbe.txt
$ bash -c 'source ./farbe.txt; echo Im Kind: $farbe'
Im Kind: blau
$ echo In der Shell: $farbe Ende
In der Shell: Ende
$ source ./farbe.txt
$ echo In der Shell: $farbe
In der Shell: blau
```

The child shell read the file and knew `farbe`; the variable disappeared with the child. Only `source` in the shell itself sets it permanently for this session. The `./` in front of the name tells `source` that the file is in the working directory. Without a slash, `source` looks for the file like a command, first in the directories from `PATH`, and bash only then in the working directory; with `./`, there can be no mix-up.
::::

⁠**In short:** `source file` runs a file in the running shell; its settings remain because no child process comes into being.

### The login shell

<span class="anker" id="stufe-6-3"></span>

Not every shell starts in the same way. A shell that runs right after logging in has additional tasks, such as setting up the search path, which then applies to the whole session.

:::definition Definition 6.3 (Login shell)
<span class="anker" id="satz-6-3"></span>

A __login shell__ is a shell that starts at a login, for example after a user name and password on a text console, for a connection from another computer or when you open the WSL terminal. bash then first reads `/etc/profile` and after that the first existing one of the files `~/.bash_profile`, `~/.bash_login` and `~/.profile`; it does not read `~/.bashrc` on its own.
:::

Ubuntu creates only `~/.profile`, and this file reads in `~/.bashrc` itself. Figure [26](#abb-26) shows the three usual cases. In the terminal of a graphical desktop, bash usually starts without a login, reads only `~/.bashrc` and inherits the rest of its environment from the program that started it. The builtin command `shopt` shows options of bash; `shopt login_shell` reveals whether the running bash is a login shell. The option `-l` starts a bash as a login shell.

:::abbildung linux/k5startdateien 26
Which startup files bash reads. Login shell, for example in the WSL terminal: `/etc/profile`, then `~/.profile`, which on Ubuntu reads in `~/.bashrc`. Interactive shell without a login, for example a new `bash` in the terminal: `/etc/bash.bashrc`, then `~/.bashrc`. `bash -c '…'`: no startup file.
:::

::::beispiel With and without a login
```console
$ shopt login_shell
login_shell             off
$ bash -l -c 'shopt login_shell'
login_shell             on
```

The shell in which the examples of this chapter ran was not a login shell. If you type the first line in the WSL terminal, you see `on`, because WSL starts a login shell there. Lines 11 to 17 show how `~/.profile` on Ubuntu reads in the file `~/.bashrc`:

```console
$ head -n 17 ~/.profile | tail -n 7
```

```text
# if running bash
if [ -n "$BASH_VERSION" ]; then
    # include .bashrc if it exists
    if [ -f "$HOME/.bashrc" ]; then
        . "$HOME/.bashrc"
    fi
fi
```

Lines with `#` at the beginning are comments, which the shell skips. The remaining lines mean: if bash is running and the file `~/.bashrc` exists, it is read; the single dot is the short form of `source` from subsection [6.2](#stufe-6-2). Because `source` does not start a child process, everything from `~/.bashrc` takes effect in the login shell itself. At the end of the file, `~/.profile` sets up the search path for your own programs:

```console
$ tail -n 9 ~/.profile
```

```text
# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/bin" ] ; then
    PATH="$HOME/bin:$PATH"
fi

# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/.local/bin" ] ; then
    PATH="$HOME/.local/bin:$PATH"
fi
```

If a directory `~/bin` or `~/.local/bin` exists at login, it goes at the front of the search path, just like `~/linuxk5/bin` in subsection [5.5](wie-die-shell-programme-findet-path.html#stufe-5-5).
::::

⁠**In short:** A login shell reads `/etc/profile` and `~/.profile`, which on Ubuntu reads in `~/.bashrc`; an interactive shell without a login reads only `~/.bashrc`.

:::hintergrund One file that pushes the other aside
A login shell reads only the first existing one of the three files `~/.bash_profile`, `~/.bash_login` and `~/.profile`. If someone creates a `~/.bash_profile`, for example following instructions for another distribution, bash no longer reads `~/.profile`, and with it, the search path for your own programs and the reading in of `~/.bashrc` are lost. The comment in the first lines of Ubuntu's `~/.profile` points out exactly this. How a shell recognizes that it is a login shell: the program that handles the login starts it under a name that begins with a minus sign, that is, `-bash`; a call with `-l` has the same effect.
:::

### Making a setting permanent

<span class="anker" id="stufe-6-4"></span>

Now you can set up a setting so that every new shell has it: you write it into `~/.bashrc` and have the running shell read the file again with `source`. The environment variable `EDITOR` serves as an example. Many programs that need a text from you along the way start the editor whose name is in `EDITOR`; you know `nano` from [Chapter 3, Section 5.3](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-und-verzeichnisse-anlegen.html#stufe-5-3).

:::warnung Back up first, then change
A broken `~/.bashrc` disrupts every new shell. Before every change, make a backup copy, here in your practice directory:

```console
$ cp ~/.bashrc ~/linuxk5/bashrc.sicherung
```

Append new lines only with `>>`. A single `>` instead of `>>` empties the file before the new line goes in ([Chapter 4, Section 2.1](/wissen/en/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/ausgaben-umleiten.html#stufe-2-1)). If you prefer to work in the editor, open the file with `nano ~/.bashrc` and write the line at the end.
:::

::::beispiel Setting EDITOR permanently
```console
$ echo 'export EDITOR=nano' >> ~/.bashrc
$ tail -n 1 ~/.bashrc
export EDITOR=nano
$ echo Editor: $EDITOR Ende
Editor: Ende
$ bash -i -c 'echo Editor: $EDITOR'
Editor: nano
$ source ~/.bashrc
$ echo Editor: $EDITOR
Editor: nano
```

The single quotes pass the line to `echo` unchanged. Afterward, it is at the end of the file. The running shell does not know `EDITOR` yet, but a new interactive bash does, because it reads the file when it starts. After `source`, the running shell has the value too. Figure [27](#abb-27) shows the sequence of events.

:::abbildung linux/k5dauerhaft 27
A setting becomes permanent. 1: The line `export EDITOR=nano` goes at the end of `~/.bashrc`; the running shell stays unchanged, because it already read the file when it started. 2: A new shell reads the file when it starts and has `EDITOR`. 3: `source ~/.bashrc` has the running shell read the file again; now it has the value too.
:::
::::

For your own programs, Ubuntu offers the directory `~/.local/bin`. If this directory exists, `~/.profile` adds it at the front of the search path at the next login. Without logging out and back in, you can check this with a login shell:

```console
$ mkdir -p ~/.local/bin
$ bash -l -c 'echo "$PATH"' | tr ':' '\n' | head -n 1
/home/student/.local/bin
```

A program that you copy to `~/.local/bin` starts from the next login on with its name alone, from any directory. Instead of relying on `~/.profile`, you can also extend the search path with a line such as `export PATH="$HOME/bin:$PATH"` in `~/.bashrc`; then, however, every shell that starts within another one puts the directory in front once more.

⁠**In short:** Permanent settings belong in `~/.bashrc`, your own programs in `~/.local/bin`; `source ~/.bashrc` makes changes take effect immediately.

### The alias

<span class="anker" id="stufe-6-5"></span>

[Chapter 2, Section 3.4](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/arten-von-befehlen.html#stufe-3-4) introduced aliases as abbreviations that the shell replaces with stored text when it reads in a line. Now you can define your own and know where they are kept permanently.

:::definition Definition 6.4 (Defining an alias)
<span class="anker" id="satz-6-4"></span>

The builtin command __alias__ `name='text'` defines an alias: if `name` is the first word of a command, the shell replaces it with `text`. `unalias name` removes the alias, and `alias` without arguments shows all of them. Aliases apply only in the shell in which they were defined, and only in interactive shells.
:::

The single quotes hold the text together as one word and prevent the shell from replacing anything in it already when the alias is defined; a tilde in the text is replaced only each time the alias is used.

::::beispiel An alias for the shopping list
```console
$ alias einkauf='cat ~/linuxk5/einkauf.txt'
$ einkauf
Milch
Brot
Äpfel
Kaffee
$ type einkauf
einkauf is aliased to `cat ~/linuxk5/einkauf.txt'
$ bash -c einkauf
bash: line 1: einkauf: command not found
$ unalias einkauf
$ einkauf
einkauf: command not found
```

The child shell from `bash -c` does not know the alias: it is not interactive, and aliases are not inherited anyway. After `unalias`, the alias has disappeared from the shell itself as well.
::::

An alias becomes permanent like any other setting, via `~/.bashrc`. Because the line itself contains single quotes, double quotes protect it here on its way into the file:

```console
$ echo "alias einkauf='cat ~/linuxk5/einkauf.txt'" >> ~/.bashrc
$ tail -n 1 ~/.bashrc
alias einkauf='cat ~/linuxk5/einkauf.txt'
$ source ~/.bashrc
$ einkauf
Milch
Brot
Äpfel
Kaffee
```

If you want to get rid of the appended lines again, copy the backup back. What the running shell has already read remains in it until it ends; new shells no longer have it:

```console
$ cp ~/linuxk5/bashrc.sicherung ~/.bashrc
$ tail -n 1 ~/.bashrc
fi
```

`fi` is the last line of Ubuntu's original `~/.bashrc`.

⁠**In short:** `alias name='text'` defines an abbreviation for the running interactive shell; it becomes permanent in `~/.bashrc`.

:::hintergrund A separate file for aliases
Ubuntu's `~/.bashrc` contains lines that read in a file `~/.bash_aliases` with `source` if it exists. If you have many aliases of your own, you write them there and leave `~/.bashrc` unchanged. For abbreviations that need arguments at a particular place, aliases are too simple: the shell replaces only the first word and appends everything else unchanged.
:::

### Exercises for Section [6](#stufe-6)

<span class="anker" id="stufe-6-6"></span>

:::aufgabe Exercise 20 ★ Which startup file?
<span class="anker" id="aufg-20"></span>

Which startup files does bash read in these cases, and does the shell then have the settings from `~/.bashrc`? (a) On Windows, you open the WSL terminal. (b) On an Ubuntu desktop, you open the program “Terminal”. (c) In a terminal, you type `bash` and press Enter. (d) A command `bash -c 'll'` runs.

:::loesung
(a) The WSL terminal starts a login shell. bash reads `/etc/profile`, which on Ubuntu reads in `/etc/bash.bashrc`, and after that `~/.profile`, which reads in `~/.bashrc`. So the settings are there. (b) The terminal of a graphical desktop usually starts an interactive shell without a login; it reads `/etc/bash.bashrc` and `~/.bashrc`. The settings are there. (c) A new bash in the terminal is likewise interactive and without a login; it reads the same files as in (b). (d) `bash -c` is not interactive and reads no startup file. The alias `ll` from `~/.bashrc` is therefore missing, and even if it were defined, a non-interactive shell would not replace it; the line ends with “command not found”.
:::
:::

:::aufgabe Exercise 21 ★★ Setting things up permanently
<span class="anker" id="aufg-21"></span>

(a) Back up your `~/.bashrc` to your practice directory. (b) Append two lines: `export LIEBLINGSOBST=Mango` (`LIEBLINGSOBST` is German for “FAVORITEFRUIT”) and an alias `wo` (German for “where”) that runs `pwd`. (c) Before and after `source ~/.bashrc`, check whether the running shell knows `LIEBLINGSOBST`, and try out `wo`. (d) Predict what `bash -c 'echo Obst: $LIEBLINGSOBST; wo'` outputs, and explain the difference between a variable and an alias. (e) Restore the original file from the backup, and check with `cmp` and `$?` that both files are the same; `cmp` compares two files byte by byte and reports only differences.

:::loesung
```console
$ cp ~/.bashrc ~/linuxk5/bashrc.sicherung
$ echo 'export LIEBLINGSOBST=Mango' >> ~/.bashrc
$ echo "alias wo='pwd'" >> ~/.bashrc
$ echo Obst: $LIEBLINGSOBST Ende
Obst: Ende
$ source ~/.bashrc
$ echo Obst: $LIEBLINGSOBST
Obst: Mango
$ wo
/home/student/linuxk5
$ bash -c 'echo Obst: $LIEBLINGSOBST; wo'
Obst: Mango
bash: line 1: wo: command not found
$ cp ~/linuxk5/bashrc.sicherung ~/.bashrc
$ cmp ~/linuxk5/bashrc.sicherung ~/.bashrc
$ echo $?
0
```

(a) and (b) The backup first, then two lines with `>>`. The second line contains single quotes and is therefore itself enclosed in double quotes. (c) Before `source`, the running shell does not know the variable; afterward it does, and the alias works too. (d) The child shell from `bash -c` receives `LIEBLINGSOBST` through the environment, because the line in `~/.bashrc` exports the variable. It does not know the alias: aliases are not inherited, and a non-interactive shell does not replace them anyway. (e) `cmp` writes nothing and ends with exit status 0: the files are the same, and the original `~/.bashrc` is restored.
:::
:::

:::aufgabe Exercise 22 ★★ The dot as a command
<span class="anker" id="aufg-22"></span>

Create a small file with `echo haustier=Hund > tier.txt`. Predict what `bash -c '. ./tier.txt; echo Im Kind: $haustier'` outputs and what `echo In der Shell: $haustier Ende` shows afterward. What changes if you enter `. ./tier.txt` directly in your shell? What do the two dots in `. ./tier.txt` mean?

:::loesung
```console
$ echo haustier=Hund > tier.txt
$ bash -c '. ./tier.txt; echo Im Kind: $haustier'
Im Kind: Hund
$ echo In der Shell: $haustier Ende
In der Shell: Ende
$ . ./tier.txt
$ echo In der Shell: $haustier
In der Shell: Hund
```

The child shell reads the file in its own process; the variable lives only there and disappears with the child. Entered directly in the shell, the command carries out the assignment in the shell itself, and the variable remains. The first dot is the command, the short form of `source`. The second dot belongs to the path `./tier.txt` and means the working directory ([Chapter 3, Section 2.5](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/das-arbeitsverzeichnis-und-pfade.html#stufe-2-5)).
:::
:::

:::aufgabe Exercise 23 ★★★ An alias comes too late
<span class="anker" id="aufg-23"></span>

Predict what these two lines output, and check it:

```console
$ alias begruessung='echo Guten Tag'; begruessung
$ begruessung
```

Explain the result of the first line with step 1 of the order from subsection [3.9](worttrennung-und-quoting.html#stufe-3-9).

:::loesung
```console
$ alias begruessung='echo Guten Tag'; begruessung
begruessung: command not found
$ begruessung
Guten Tag
```

The shell replaces aliases in step 1, when it splits the line into words. It reads the first line completely before it executes any part of it; at that moment, the alias did not exist yet, so `begruessung` (German for “welcome”) remained an ordinary word for which the shell looks for a program. The alias came into being only when the line was executed. The shell reads the second line after that, and now it replaces the word. That is why an alias definition belongs on a line of its own.
:::
:::

**For further practice.** The freely accessible learning platform pwn.college offers short exercises in the browser under the name “Linux Luminarium”; the modules “File Globbing”, “Shell Variables” and “Pondering PATH” match this chapter. They run on someone else's computer, not on your own.

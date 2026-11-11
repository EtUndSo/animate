---
title: Environment and inheritance
pfad: Computer Science / Linux and the Command Line / How the Shell Reads a Command Line: Expansion, Quoting, Variables, Environment
adresse: informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung
knoten: Chapter 5: How the Shell Reads a Command Line: Expansion, Quoting, Variables, Environment
order: 6100500
summary: Variables live in the shell; programs run in processes of their own.
tags: child process, parent process, environment, environment variable, export, env
lang: en
---

<span class="anker" id="stufe-4"></span>

:::zweck
Variables live in the shell; programs run in processes of their own. This section clarifies which values a program receives from the shell when it starts: the environment. It shows how to add a variable to the environment, why a started program receives only a copy and cannot pass anything back and how to give a single command a setting of its own.
:::

:::::vorwissen What you need for this: processes and bash -c

<span class="anker" id="stufe-4-1"></span>

<ul>

<li>

A process has its own memory and its own working directory; the kernel keeps processes separate from one another. For every program, the shell starts a new process; it runs a builtin command itself. That is why `cd` has to be built in ([Chapter 4, Section 1.2](/wissen/en/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/prozesse-und-ihre-drei-strome.html#stufe-1-2); [Chapter 2, Section 3.3](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/arten-von-befehlen.html#stufe-3-3)).

</li>

<li>

`bash -c '…'` starts another bash that runs the text in the quotes as a command line ([Chapter 4, Section 5.1](/wissen/en/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/der-exit-status.html#stufe-5-1)).

</li>

<li>

Between single quotes, the shell inserts nothing; between double quotes, it inserts values with `$` (subsections [3.4](worttrennung-und-quoting.html#stufe-3-4) and [3.5](worttrennung-und-quoting.html#stufe-3-5)).

</li>

</ul>

⁠**In short:** You need the process with its own memory, `bash -c` and the difference between single and double quotes.

:::::

### The child process

<span class="anker" id="stufe-4-2"></span>

A variable that you create in the shell lies in the memory of the shell process. A program that the shell starts runs in a different process with its own memory. Does it know the shell's variables?

:::definition Definition 4.1 (Child process, parent process)
<span class="anker" id="satz-4-1"></span>

If a process starts another one, the new process is a __child process__ of the first. The starting process is called its __parent process__.
:::

Every program that you start in the shell is a child process of the shell, including a second bash that you start with `bash -c`. Figure [15](#abb-15) shows what happens when such a child needs a variable of the shell.

:::abbildung linux/k5kind 15
The shell with the variable `obst=Apfel` (`obst` is German for “fruit”, `Apfel` for “apple”) starts a child twice. At the top with single quotes: the child receives the text `echo Obst: $obst`, looks up `obst` itself and finds nothing. At the bottom with double quotes: the shell inserts the value before the start, and the child already receives `echo Obst: Apfel`.
:::

::::beispiel Who inserts the value?
```console
$ obst=Apfel
$ bash -c 'echo Obst: $obst'
Obst:
$ bash -c "echo Obst: $obst"
Obst: Apfel
```

In the first line, the single quotes prevent the shell from replacing `$obst`; the child shell receives the text unchanged and knows no variable `obst`. In the second line, the shell replaces `$obst` before the start; the child no longer has to look anything up. In neither case did it receive the variable itself.
::::

⁠**In short:** A process that another process starts is its child process; it does not automatically receive the shell's variables.

### The environment

<span class="anker" id="stufe-4-3"></span>

Almost every program needs certain information: where the home directory is, what the user is called, in which language messages should appear. For this, there is a fixed path from process to process. As a picture for orientation: every program receives two notes when it starts, one with its arguments and one with general settings; Figure [16](#abb-16) shows both.

:::abbildung linux/k5umgebung 16
What a process receives when it starts: on the left, the argument list, here `printenv HOME USER`; on the right, the environment, a list of entries of the form `NAME=value` such as `HOME=/home/student` and `LANG=C.UTF-8`. `printenv` picks out the entries for its arguments from the environment.
:::

:::definition Definition 4.2 (Environment)
<span class="anker" id="satz-4-2"></span>

The __environment__ of a process is a list of texts of the form `NAME=value` that the process receives when it starts, in addition to its arguments. Each program decides for itself which entries it takes into account.
:::

The command `printenv` writes the environment, one line per entry. With names as arguments, it writes only their values; if a name is missing from the environment, it writes nothing and ends with exit status 1.

::::beispiel Entries of the environment
```console
$ printenv HOME USER SHELL LANG
/home/student
student
/bin/bash
C.UTF-8
$ printenv obst
$ echo $?
1
```

`HOME` names the home directory, `USER` the user, `SHELL` the shell that starts at login and `LANG` the language setting. The variable `obst` is not in the environment of `printenv`, even though the shell knows it.
::::

Tilde expansion also uses such an entry: for a tilde without a user name, the shell inserts the value of `HOME`, which it received in its own environment when it started.

⁠**In short:** The environment is a list of entries `NAME=value` that every process receives when it starts; `printenv` shows it.

### The environment variable: export

<span class="anker" id="stufe-4-4"></span>

So the shell knows variables that do not end up in the environment of its children. If a program is to receive a value, you have to tell the shell to pass it on. Figure [17](#abb-17) shows what this changes in the shell.

:::abbildung linux/k5export 17
The shell holds variables, and some of them carry a mark for passing on. `export obst` puts the mark on `obst` as well. When a child starts, the shell writes exactly the marked variables into its environment; variables that are not marked stay in the shell.
:::

:::definition Definition 4.3 (Environment variable, export)
<span class="anker" id="satz-4-3"></span>

An __environment variable__ is a shell variable that is marked for passing on; the shell writes all marked variables into the environment of every child process. The builtin command __export__ marks a variable: `export NAME` marks an existing one, `export NAME=value` assigns and marks in one step. Variables that the shell finds in its environment when it starts are marked from the beginning.
:::

That is why every program knows `HOME` and `USER`: the shell itself already received them in its environment and passes them on. A habit prevents mix-ups: the system's environment variables have names in uppercase letters, and you write your own variables in lowercase, as in this chapter.

::::beispiel A value for the children
```console
$ export obst
$ bash -c 'echo Obst: $obst'
Obst: Apfel
$ printenv obst
Apfel
$ export gemuese=Karotte
$ bash -c 'echo Gemüse: $gemuese'
Gemüse: Karotte
```

The same line as in subsection [4.2](#stufe-4-2) now finds a value, because `obst` is in the environment of the child shell. `printenv` now sees the variable too.
::::

⁠**In short:** `export` marks a shell variable as an environment variable; every child receives it in its environment.

:::hintergrund Unmarking and removing variables
`export -n NAME` takes the mark away again; the variable stays in the shell, but children no longer receive it. `unset NAME` removes the variable entirely.

```console
$ export -n gemuese
$ bash -c 'echo Gemüse: $gemuese Ende'
Gemüse: Ende
$ echo Gemüse: $gemuese
Gemüse: Karotte
$ unset gemuese
$ echo Gemüse: $gemuese Ende
Gemüse: Ende
```
:::

### Inheritance as a copy

<span class="anker" id="stufe-4-5"></span>

If a child receives its environment, the reverse question arises: what happens when the child changes a value? Does the change reach the shell? Figure [18](#abb-18) shows the sequence of events.

:::abbildung linux/k5vererbung 18
Inheritance of the environment as a timeline. At the start, the child receives a copy of the shell's environment, with `obst=Apfel`. The child changes its copy to `obst=Birne`. The way back to the shell is crossed out: when the child ends, its copy disappears, and the shell still has `obst=Apfel`.
:::

:::satz Theorem 4.4 (Inheritance of the environment)
<span class="anker" id="satz-4-4"></span>

A child process receives a copy of its parent process's environment when it starts. Whatever it changes in its variables afterward changes only its copy; none of it gets back to the parent process. Likewise, a later change in the parent process no longer reaches a child that is already running.
:::

::::beispiel The child changes only its copy
```console
$ bash -c 'obst=Birne; echo Im Kind: $obst'
Im Kind: Birne
$ echo In der Shell: $obst
In der Shell: Apfel
$ bash -c 'export neu=Zitrone; echo Im Kind: $neu'
Im Kind: Zitrone
$ echo In der Shell: $neu Ende
In der Shell: Ende
```

The child shell changed `obst` and even exported a new variable. None of this arrived at the shell. An `export` in the child affects only the child's own children.
::::

From this follows a rule that often comes as a surprise: no program that you start can change the variables of your shell, not even a second shell. It is the same separation that requires `cd` to be built in.

⁠**In short:** A child inherits a copy of the environment; it can change the copy but cannot pass anything back.

:::hintergrund Why there is only a copy
On Linux, a new process comes into being in two steps, which [Chapter 4, Section 2.1](/wissen/en/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/ausgaben-umleiten.html#stufe-2-1) already described for redirections. With `fork`, the kernel creates a copy of the parent process with its own memory; the environment lies in this memory and is therefore copied along. With `exec`, the child process then loads the new program; in doing so, it passes on the environment, in the case of a shell the list of its exported variables, as texts `NAME=value`, and the kernel places them in the memory of the new program. From this moment on, there are two separate lists in two separate memories. The kernel keeps the memories of the processes separate: an ordinary program cannot write into the memory of another, and there is no system call that changes the environment of the parent process.

That this is intended was already stated in the guide with which Stephen Bourne introduced his shell in 1978: for an invoked program, copies of the exported variables are made, and changes to them do not affect the invoking shell. A program should not be able to change the state of whoever invoked it unless the caller explicitly asks for it. As a picture for orientation: the child receives a photocopy and not the original; what it writes on its copy does not appear on the original.
:::

### A variable for one command only

<span class="anker" id="stufe-4-6"></span>

Sometimes only a single command is to get a different setting. One example is the time zone: the environment variable `TZ` determines in which time zone programs such as `date` show the time. If it is not set, the system's time zone applies. If you want to know what time it is in Tokyo right now, you do not want to change the setting of the whole shell for that. Figure [19](#abb-19) shows how the shell solves this.

:::abbildung linux/k5einbefehl 19
`TZ=Asia/Tokyo date`: the shell gives the child `date` a copy of its environment and appends the entry `TZ=Asia/Tokyo`. The environment of the shell itself stays without `TZ`; the next command no longer receives the entry.
:::

:::definition Definition 4.5 (Assignment before a command)
<span class="anker" id="satz-4-5"></span>

If one or more assignments `NAME=value` come before the command name, they go only into the environment of this one command. The shell itself keeps its variables as they were.
:::

Such assignments take effect only after the shell has expanded the remaining words of the line; a `$NAME` in the same line therefore still receives the shell's value.

::::beispiel What time is it elsewhere?
```console
$ date +%H:%M
07:26
$ TZ=Asia/Tokyo date +%H:%M
15:26
$ TZ=America/New_York date +%H:%M
01:26
$ echo TZ: $TZ Ende
TZ: Ende
```

`+%H:%M` asks only for the hour and minute. The test system is in Berlin; in November, Tokyo is eight hours ahead and New York six hours behind. The names of the time zones have the form `Continent/City`; they correspond to files under `/usr/share/zoneinfo`. After the two commands, the shell still has no `TZ`. On your computer, the times will be different; the differences stay the same as long as none of the cities has just changed its clocks.
::::

::::beispiel [Second example] A cherry for the child only
```console
$ obst=Kirsche bash -c 'echo Obst: $obst'
Obst: Kirsche
$ echo Obst: $obst
Obst: Apfel
```

The child shell sees `Kirsche`, the shell itself keeps `Apfel`.
::::

⁠**In short:** `NAME=value command` gives only this command a setting of its own; the shell stays unchanged.

### env and printenv

<span class="anker" id="stufe-4-7"></span>

To understand what a program reads from its environment, it helps to change the environment in a targeted way: leave out one entry or start entirely without an environment.

:::definition Definition 4.6 (env)
<span class="anker" id="satz-4-6"></span>

The command __env__ starts a command with a modified environment. `env NAME=value command` adds entries, `env -u NAME command` leaves one out and `env -i command` starts the command with an empty environment. Without a command, `env` writes the environment like `printenv`.
:::

In bash, you achieve the same as `env NAME=value command` with an assignment before the command. `env`, however, is a program of its own and therefore also works where no shell reads the line.

::::beispiel Empty and without one entry
```console
$ env -i printenv
$ env -i bash -c printenv
PWD=/home/student/linuxk5
SHLVL=0
_=/usr/bin/printenv
$ env -u obst bash -c 'echo Obst: $obst Ende'
Obst: Ende
```

With an empty environment, `printenv` finds nothing. A bash that starts with an empty environment creates three entries itself: the working directory `PWD`, the nesting depth `SHLVL` and, in `_`, the path of the program that it starts. In the last line, `obst` is missing from the child's environment, even though the shell has exported the variable.
::::

Table [2](#tab-2) lists environment variables that you will often come across.

<span class="anker" id="tab-2"></span>

**Table 2:** Common environment variables.

| Variable | Meaning |
|---|---|
| `HOME` | home directory; the tilde is replaced by this value |
| `USER` | name of the user |
| `SHELL` | the shell that starts when the user logs in |
| `PWD` | working directory; `cd` keeps the value up to date |
| `LANG` | language setting: language of messages, order when sorting; on the test system `C.UTF-8` |
| `LC_ALL` | overrides `LANG` if set; usually empty |
| `TERM` | type of terminal, so that programs send colors and control characters correctly |
| `TZ` | time zone, usually not set |
| `PATH` | the search path from Chapter 2, Section 3.2 |

⁠**In short:** `printenv` shows the environment, `env` starts a command with a modified or empty environment.

### Exercises for Section [4](#stufe-4)

<span class="anker" id="stufe-4-8"></span>

:::aufgabe Exercise 13 ★ Who does the inserting?
<span class="anker" id="aufg-13"></span>

In your shell, `tier=Katze` is set (`tier` and `Katze` are German for “animal” and “cat”); the variable is not exported. Predict what these three lines output, and check it: (a) `bash -c 'echo Tier: $tier'` (b) `bash -c "echo Tier: $tier"` (c) `bash -c 'echo Heim: $HOME'`. In particular, explain why (c) shows a value but (a) does not.

:::loesung
```console
$ tier=Katze
$ bash -c 'echo Tier: $tier'
Tier:
$ bash -c "echo Tier: $tier"
Tier: Katze
$ bash -c 'echo Heim: $HOME'
Heim: /home/student
```

(a) The single quotes pass the text unchanged to the child shell; it looks for `tier` among its variables and finds nothing, because `tier` is not exported. (b) The shell inserts `Katze` before the child even starts. (c) Here, too, it is the child shell that does the replacing, but `HOME` is an environment variable: the shell found it in its environment when it started itself, so it is marked, and the child receives it in its environment.
:::
:::

:::aufgabe Exercise 14 ★★ Inheritance step by step
<span class="anker" id="aufg-14"></span>

Run the following one after another (`gruss` is German for “greeting”, `hallo`, `servus` and `tschüss` for “hello”, “hi” and “bye”), and before each line with `echo`, predict the result: `gruss=hallo`, `bash -c 'echo Gruß: $gruss'`, `export gruss`, the same line again, `gruss=servus bash -c 'echo Gruß: $gruss'`, `echo Gruß: $gruss`, `bash -c 'gruss=tschüss; export gruss'`, `echo Gruß: $gruss`. Then explain in two sentences why a program that uses `export` internally cannot change the variables of your shell.

:::loesung
```console
$ gruss=hallo
$ bash -c 'echo Gruß: $gruss'
Gruß:
$ export gruss
$ bash -c 'echo Gruß: $gruss'
Gruß: hallo
$ gruss=servus bash -c 'echo Gruß: $gruss'
Gruß: servus
$ echo Gruß: $gruss
Gruß: hallo
$ bash -c 'gruss=tschüss; export gruss'
$ echo Gruß: $gruss
Gruß: hallo
```

Before `export`, `gruss` is only a shell variable, and the child does not receive it. Afterward, it is in the environment of every child. The assignment before the command applies only to this one child; the shell keeps `hallo`. The last child shell changes and exports `gruss`, but only in its own copy. The explanation: when a program starts, it receives a copy of the environment in its own memory. An `export` in it changes only this copy and affects at most the children of this program, never the shell that started it.
:::
:::

:::aufgabe Exercise 15 ★★ World clock
<span class="anker" id="aufg-15"></span>

With three lines, have the current time in Tokyo, New York and Sydney output (time zones `Asia/Tokyo`, `America/New_York`, `Australia/Sydney`). Why is `TZ` still empty in your shell afterward? By how many hours is Sydney ahead of Berlin in November?

:::loesung
```console
$ TZ=Asia/Tokyo date +%H:%M
15:29
$ TZ=America/New_York date +%H:%M
01:29
$ TZ=Australia/Sydney date +%H:%M
17:29
$ echo TZ: $TZ Ende
TZ: Ende
```

The times depend on when you run the lines. Each time, `TZ` was only in the environment of the one `date` process; the shell itself did not get a variable `TZ`. The test session ran at 7:29 a.m. Berlin time. Sydney showed 17:29, so it is ten hours ahead: in November, Berlin is on standard time, one hour ahead of UTC, whereas Sydney is on daylight saving time, eleven hours ahead of UTC.
:::
:::

:::aufgabe Exercise 16 ★★★ The cherry that never arrives
<span class="anker" id="aufg-16"></span>

In your shell, `obst=Apfel` is set. Predict what (a) `obst=Kirsche echo Obst: $obst`, (b) `obst=Kirsche printenv obst` and (c) `obst=Kirsche bash -c 'echo Obst: $obst'` output, and check it. Explain the result of (a) with the order in which the shell processes a line.

:::loesung
```console
$ obst=Apfel
$ obst=Kirsche echo Obst: $obst
Obst: Apfel
$ obst=Kirsche printenv obst
Kirsche
$ obst=Kirsche bash -c 'echo Obst: $obst'
Obst: Kirsche
```

(a) The shell first expands the words of the line that are not assignments; in doing so, it replaces `$obst` with the shell's value, `Apfel`. Only after that does `obst=Kirsche` (`Kirsche` is German for “cherry”) take effect for the command, and by then `echo` already has its argument. `echo` does not read the environment at all; it only writes its arguments. (b) `printenv` reads the environment, which contains `obst=Kirsche`. (c) The single quotes move the inserting into the child shell, and its environment contains `obst=Kirsche`.
:::
:::

---
title: Key points so far
pfad: Computer Science / Linux and the Command Line / The Shell: First Commands
adresse: informatik/linux-und-kommandozeile/die-shell-erste-befehle
knoten: Chapter 2: The Shell: First Commands
order: 6070900
summary: Terminal and shell, how a command is built, help for every command and the first steps through your own system
tags: 
lang: en
---

:::kern Key points so far
<ul>

<li>

Two programs work in the terminal window: the terminal emulator draws characters and passes keystrokes on, and the shell reads command lines and has them run. In Ubuntu, the shell is bash, an ordinary program in user mode.

</li>

<li>

The prompt shows the user, the computer and the current folder; `$` stands for an ordinary user, `#` for root. Each window has its own shell and therefore its own session.

</li>

<li>

The shell splits a line at the spaces into words. The first one is the command, and the rest are arguments; options begin with `-` or `--`, short ones can be bundled, some require a value, and after `--` every word is an ordinary argument. What a word means is decided by the program.

</li>

<li>

A command is an alias, a builtin command or a program file in the search path; `type` tells you which, while `which` sees only the search path. Commands that change the shell itself, such as `cd` and `exit`, have to be built in.

</li>

<li>

Help comes in three forms: `--help` for an overview, `help` for builtins, `man` for the complete manual page with a fixed layout and numbered sections; `apropos` finds pages by their short description.

</li>

<li>

The Tab key completes, the history remembers every line, and Ctrl+R searches it. Ctrl+C interrupts, and Ctrl+D reports the end of input; while a program is running, the kernel handles both keys in the pseudoterminal before the program reads them.

</li>

<li>

`uname`, `whoami`, `id`, `date`, `uptime`, `free` and `df` make up a fact sheet of the system. Ubuntu 26.04 ships most core commands as uutils; there, the GNU implementation is called `gnu`….

</li>

</ul>
:::

:::merke The answer in three sentences
<ol>

<li>

You talk to a computer that understands only text through the shell: it reads a command line, splits it into words, finds the command as an alias, builtin command or program file and has it run.

</li>

<li>

What the words are and what they mean is defined by each program itself, following common conventions for options and arguments; you can look it up at any time with `--help`, `help` or `man`.

</li>

<li>

Completion, history and keyboard shortcuts save typing, and just a few commands reveal the kernel, distribution, user, memory and disk space of your own system.

</li>

</ol>
:::

**One principle behind all the results.** Almost everything in this chapter follows from one idea: the shell mediates; it does not do the work itself. It splits lines, looks up commands and starts programs; what a word means is decided by the program, and whatever concerns the hardware or the terminal is handled by the kernel. Only what the shell has to change about itself does it do itself.

| Result | Where it comes from |
|---|---|
| the terminal can be swapped without anything changing about the commands | the window only draws characters; only the shell understands them (Section [1](terminal-und-shell.html#stufe-1)) |
| two windows have different current folders | each window has its own shell and session (Section [1](terminal-und-shell.html#stufe-1)) |
| `echo Hallo Welt` prints only one space | the shell passes on words, not spaces (Section [2](der-aufbau-einer-befehlszeile.html#stufe-2)) |
| `uname -mrs` and `uname -srm` print the same | the program interprets the options and chooses the order (Section [2](der-aufbau-einer-befehlszeile.html#stufe-2)) |
| after `--`, `-l` is a file name | common conventions for options, which the program implements (Section [2](der-aufbau-einer-befehlszeile.html#stufe-2)) |
| `cd` and `exit` are built in | only the shell can change its own folder and end itself (Section [3](arten-von-befehlen.html#stufe-3)) |
| `which cd` finds nothing in Ubuntu, but `type cd` does | `which` is a separate program and sees only the search path (Section [3](arten-von-befehlen.html#stufe-3)) |
| `type ls` reports an alias in Ubuntu | the shell replaces aliases as early as when it reads the line (Section [3](arten-von-befehlen.html#stufe-3)) |
| `man cd` finds nothing, but `help cd` does | the shell itself describes builtin commands (Section [4](hilfe-finden.html#stufe-4)) |
| `man passwd` shows the command, not the file | without a number, the first matching section wins (Section [4](hilfe-finden.html#stufe-4)) |
| Ctrl+C also interrupts a program that pays no attention to keys | the kernel handles the key in the pseudoterminal (Section [5](schneller-arbeiten-vervollstandigung-verlauf-tastenkurzel.html#stufe-5)) |
| Ctrl+D ends `cat` and, on an empty line, the shell, too | a read with zero characters means “end of input”; bash handles the key the same way (Section [5](schneller-arbeiten-vervollstandigung-verlauf-tastenkurzel.html#stufe-5)) |
| `free` is small, `available` large | the kernel uses free memory as a cache for files (Section [6](das-system-erkunden.html#stufe-6)) |
| `ls` and `uname` are the same file in Ubuntu 26.04 | the multicall program reads the name under which it was started (Section [7](zwei-fassungen-der-grundbefehle-gnu-und-uutils.html#stufe-7)) |

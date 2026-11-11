---
title: Two implementations of the core commands: GNU and uutils
pfad: Computer Science / Linux and the Command Line / The Shell: First Commands
adresse: informatik/linux-und-kommandozeile/die-shell-erste-befehle
knoten: Chapter 2: The Shell: First Commands
order: 6070800
summary: Most commands in this chapter belong to a collection of core commands that every Linux system comes with.
tags: coreutils, uutils coreutils, prefix gnu
lang: en
---

<span class="anker" id="stufe-7"></span>

:::zweck
Most commands in this chapter belong to a collection of core commands that every Linux system comes with. Ubuntu 26.04 ships them in a newly written implementation and additionally the previous one. This section shows how to tell the two apart, how to run the previous one and where they differ.
:::

### The core commands: coreutils

<span class="anker" id="stufe-7-1"></span>

`uname`, `head`, `cat`, `date` and `ls` are not individual pieces from different makers; they come from a shared collection. If you know this collection, you know which commands you can expect on any Linux system. Figure [29](#abb-29) shows an excerpt.

:::abbildung linux/k2coreutils 29
An excerpt from the collection of core commands, ordered by task: commands for files such as `ls` and `cp`, for text such as `cat` and `head`, for information about the system such as `uname`, `date` and `df`. In all, there are over a hundred.
:::

:::definition Definition 7.1 (coreutils)
<span class="anker" id="satz-7-1"></span>

The __coreutils__ (“core utilities”) are a collection of over a hundred basic commands for files, text and system information, including `ls`, `cat`, `head`, `cp`, `uname`, `date` and `df`. The classic implementation comes from the GNU project and is called GNU coreutils.
:::

Every Linux distribution contains an implementation of the coreutils. Because the GNU implementation has been the standard for decades, countless sets of instructions, scripts and help forums are based on its behavior. With `--version`, each of these commands reveals which collection it comes from.

::::beispiel Who wrote cp?
```console
$ cp --version
cp (GNU coreutils) 9.7
Packaged by Ubuntu (9.7-3ubuntu2)
Copyright (C) 2025 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by Torbjörn Granlund, David MacKenzie, and Jim Meyering.
```

The copy command `cp` comes from GNU coreutils, version 9.7, packaged by Ubuntu.
::::

⁠**In short:** The coreutils are the collection of core commands; the classic implementation comes from the GNU project.

:::hintergrund Where the GNU coreutils come from
In 1983, the GNU project set out to write a free Unix-like operating system, command by command. For a long time, the core commands were in three separate packages: for files, for text and for the shell; in 2002, they were merged into the coreutils. Together with the Linux kernel, these programs form the core of the systems that [Chapter 1, Section 1.5](/wissen/en/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/betriebssystem-kernel-und-distribution.html#stufe-1-5) calls “GNU/Linux”, which is also why `GNU/Linux` appears at the end of `uname -a`.
:::

### uutils: the rewrite in Rust

<span class="anker" id="stufe-7-2"></span>

If you ask `ls` for its version under Ubuntu 26.04, you get an unexpected answer:

```console
$ ls --version
ls (uutils coreutils) 0.8.0
```

It is not the GNU implementation that answers here, but a different one.

:::abbildung linux/k2zweifassungen 30
Two toolboxes on an Ubuntu 26.04 system. Under the familiar names such as `ls`, `cat` and `uname`, the commands from uutils run; `cp`, `mv`, `rm` and `df` still come from GNU coreutils. Under names with the prefix `gnu`, all GNU implementations are ready to use.
:::

:::definition Definition 7.2 (uutils coreutils)
<span class="anker" id="satz-7-2"></span>

__uutils coreutils__, uutils for short, is a rewrite of the coreutils in the programming language Rust that is meant to behave like the GNU implementation. The open source project has existed since 2013. Ubuntu has used it for most core commands since release 25.10; in Ubuntu 26.04, only `cp`, `mv`, `rm`, `df` and `true` still come from GNU coreutils.
:::

Other distributions such as Debian, Fedora and Kali continue to use the GNU implementation. For almost all tasks, this makes no difference: the commands have the same names, almost always understand the same options and deliver the same results. Differences show up mainly in the wording of help texts and error messages.

::::beispiel Which command comes from where?
```console
$ uname --version
uname (uutils coreutils) 0.8.0
$ head --version
head (uutils coreutils) 0.8.0
$ df --version
df (GNU coreutils) 9.7
Packaged by Ubuntu (9.7-3ubuntu2)
Copyright (C) 2025 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by Torbjörn Granlund, David MacKenzie, and Paul Eggert.
```

`uname` and `head` from this chapter are uutils; `df` is GNU.
::::

⁠**In short:** Ubuntu 26.04 uses uutils, a rewrite in Rust, for most core commands; `--version` shows which implementation answers.

:::hintergrund Why Ubuntu is having the core commands rewritten
The GNU coreutils are written in the programming language C. C gives the program full control over main memory, and a small mistake in handling it can crash a program or turn it into a security vulnerability. Rust checks while the program is being compiled that certain errors of this kind cannot occur. Canonical, the company behind Ubuntu, therefore justified the switch mainly with security and resilience; speed, it said, was not the main reason. New code, however, brings new bugs with it: before the release of Ubuntu 26.04, an independent audit of uutils found over a hundred defects of varying severity, including security vulnerabilities, which have been fixed bit by bit since then. `cp`, `mv` and `rm` stayed with GNU for the time being because of bugs that were still open.
:::

:::hintergrund One program, many names
uutils is a single program file of just over eleven megabytes that is registered in the system under over a hundred names: `/usr/bin/ls`, `/usr/bin/cat`, `/usr/bin/uname` and many more all lead to it. How does it know whether it should play `ls` or `date`? From the first word of the list it receives at startup, that is, the name under which it was called (background box “The shell splits, the program interprets” in subsection [2.3](der-aufbau-einer-befehlszeile.html#stufe-2-3)). That is why `ls --version` reports the name `ls` and `uname --version` the name `uname`, although the same file answers. Such a program is called a multicall program. A copy of the file under a new, unknown name therefore does not work: the program does not recognize the name and does not know which role to play.
:::

### Running the GNU implementation

<span class="anker" id="stufe-7-3"></span>

Sometimes a set of instructions requires exactly the behavior of the GNU implementation, or you want to compare a surprising output. For this, you need to get at the GNU implementation without rebuilding the system.

:::definition Definition 7.3 (The prefix gnu)
<span class="anker" id="satz-7-3"></span>

Ubuntu 26.04 also installs the GNU implementation of the coreutils, under names with the __prefix gnu__: `gnuls` is GNU's `ls`, `gnuuname` its `uname`, `gnudate` its `date` and so on.
:::

There are manual pages for these names, too: `man gnuls` shows the page of the GNU implementation, and `man ls` the page of the uutils implementation, which is stored under the name `rust-ls`; this explains the hits with the prefix `rust-` for `apropos` in subsection [4.6](hilfe-finden.html#stufe-4-6). On distributions with the GNU implementation, the names with `gnu` do not exist; there, `ls` already is the GNU implementation.

::::beispiel The same ls, twice
```console
$ gnuls --version
ls (GNU coreutils) 9.7
Packaged by Ubuntu (9.7-3ubuntu2)
Copyright (C) 2025 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by Richard M. Stallman and David MacKenzie.
```

The GNU implementation calls itself `ls`, not `gnuls`: it is the same program that sits under the name `ls` on Debian or Kali.
::::

⁠**In short:** In Ubuntu 26.04, you reach the GNU implementation of each core command with the prefix `gnu`, for example `gnuls`.

### What differs

<span class="anker" id="stufe-7-4"></span>

The two implementations are meant to behave the same, and in ordinary work they do. If you look closely, however, you find differences in three places.

:::abbildung linux/k2fehlermeldung 31
The same wrong option, two answers. On the left, the error message from uutils with the word `error` and a usage line; on the right, the one from GNU with the pointer to `--help`. Both mean: the option `-x` does not exist.
:::

<ul>

<li>

⁠**Error messages.** uutils writes `error:` and often a tip; GNU names the program and refers to `--help`.

</li>

<li>

⁠**Help texts and manual pages.** The wording and structure differ; the options are the same.

</li>

<li>

⁠**Strictness in edge cases.** uutils rejects some things that GNU silently accepts, such as the same option twice.

</li>

</ul>

::::beispiel One wrong option, two messages
```console
$ uname -x
error: unexpected argument '-x' found

Usage: uname [OPTION]...

For more information, try '--help'.
$ gnuuname -x
gnuuname: invalid option -- 'x'
Try 'gnuuname --help' for more information.
```

On Debian or Kali, the second message would look exactly the same, only with `uname` instead of `gnuuname`. If you type an error message into a search engine, you should therefore know which implementation wrote it.
::::

⁠**In short:** uutils and GNU deliver the same results but word help texts and error messages differently.

### Exercises for Section [7](#stufe-7)

<span class="anker" id="stufe-7-5"></span>

:::aufgabe Exercise 25 ★ Which implementation?
<span class="anker" id="aufg-25"></span>

Use `--version` to check which collection `ls`, `cat`, `cp`, `rm`, `date` and `df` come from on your system. Does the result match the definition in subsection [7.2](#stufe-7-2)? If you do not use Ubuntu 26.04: what do you expect, and what do you see?

:::loesung
Under Ubuntu 26.04, `ls`, `cat` and `date` report the origin `uutils coreutils`, whereas `cp`, `rm` and `df` report the origin `GNU coreutils`. This matches the definition: except for `cp`, `mv`, `rm`, `df` and `true`, the core commands come from uutils. On Debian, Fedora or Kali, all six report `GNU coreutils`; the version numbers depend on the distribution.
:::
:::

:::aufgabe Exercise 26 ★★ Comparing uutils and GNU
<span class="anker" id="aufg-26"></span>

Under Ubuntu 26.04, compare the uutils and the GNU implementation in each case: (a) `ls --version` and `gnuls --version`, (b) `ls /gibtsnicht` (German for “doesnotexist”) and `gnuls /gibtsnicht`, (c) `head --lines=x /etc/hostname` and `gnuhead --lines=x /etc/hostname`, (d) `uname -a --all` and `gnuuname -a --all`. Where do the answers differ, and where does only the program name differ?

:::loesung
(a) `ls (uutils coreutils) 0.8.0` versus `ls (GNU coreutils) 9.7` with information on the license and the authors: different programs, each with its own version numbering.

(b) The same except for the program name:

```console
$ ls /gibtsnicht
ls: cannot access '/gibtsnicht': No such file or directory
$ gnuls /gibtsnicht
gnuls: cannot access '/gibtsnicht': No such file or directory
```

(c) Almost the same. Both report `invalid number of lines`, but uutils puts the `x` in straight single quotes, and GNU in typographic single quotation marks, as is customary in English.

(d) Different. uutils rejects the duplicate with `error: the argument '--all' cannot be used multiple times`, while GNU outputs all the information. Error messages and strictness differ; the actual results of a correct call do not.
:::
:::

:::aufgabe Exercise 27 ★★★ A program that reads its name
<span class="anker" id="aufg-27"></span>

Using the background box “One program, many names”, explain why `uname --version` begins with `uname` and `head --version` with `head`, although the same file answers. Which piece of information from the word list that the shell passes on does the program use for this? Why would a copy of this file with the name `meinbefehl` (German for “mycommand”) not work?

:::loesung
The shell passes each program a list of words, the first of which is the name under which the program was called. For `uname --version`, the list is `uname`, `--version`; for `head --version`, it is `head`, `--version`. Both names lead to the same program file of uutils. This file first reads the first word, looks up in its list of known commands which command has this name and then behaves like this command; that is also why it gives this name in its answer. A copy with the name `meinbefehl` would receive `meinbefehl` as its first word. It does not find this name in its list and therefore does not know which command to play; it reports an error instead of doing anything.
:::
:::

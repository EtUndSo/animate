---
title: Key points so far
pfad: Computer Science / Linux and the Command Line / Streams, Redirection, Pipes and Exit Status
adresse: informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status
knoten: Chapter 4: Streams, Redirection, Pipes and Exit Status
order: 6090900
summary: What a running program reads and writes, how to send output into files, connect programs into chains and react to success and failure
tags: 
lang: en
---

:::kern Key points so far
<ul>

<li>

A process is a running execution of a program with its own memory, its own open files and its own number. The shell starts a new process for each program.

</li>

<li>

Every process has three standard streams: standard input (descriptor 0), standard output for results (1) and standard error for messages (2). In the terminal, all three lead to the terminal; a descriptor is the number by which the process refers to an open file in its requests to the kernel.

</li>

<li>

Redirections connect descriptors to files before the program starts: `>` (empty and write), `>>` (append), `2>` (standard error), `2>&1` (copy of a descriptor), `&>` (both), `<` (input), `<<ENDE` and `<<<` (text as input). `/dev/null` swallows everything.

</li>

<li>

Redirections take effect from left to right, hence `> file 2>&1`. The shell empties the target file before the start, so never `command file > file`.

</li>

<li>

A pipe connects the standard output of one program to the standard input of the next; a pipeline lines up filters such as `sort`, `uniq`, `grep`, `head` and `wc`, and `tee` branches off a copy. Messages go past the pipe.

</li>

<li>

Every process ends with an exit status from 0 to 255; 0 means success, and `$?` returns the last one. The shell sets 127 (not found), 126 (not executable) and $128 + n$ (aborted by interrupt message $n$).

</li>

<li>

`;` runs commands one after another, `&&` only on success, `||` only on failure; `a && b || c` is not a safe “if, then, else”. A pipeline has the exit status of its last command; `PIPESTATUS` and `pipefail` reveal earlier errors.

</li>

<li>

`xargs` turns a stream into arguments, with `-n` in batches; `find -print0 | xargs -0` and `find -exec … +` also pass names with spaces correctly.

</li>

</ul>
:::

:::merke The answer in three sentences
<ol>

<li>

Every program runs as a process with three standard streams that it knows only by the numbers 0, 1 and 2; where they lead is set by the shell before the start.

</li>

<li>

With redirections, you connect them to files, with pipes to other programs, and in this way small filters become tool chains that together answer questions for which no dedicated program exists.

</li>

<li>

From the exit status, the shell recognizes success and failure and, with `&&` and `||`, makes the next step depend on it.

</li>

</ol>
:::

**One principle behind all the results.** Almost everything in this chapter follows from one idea: a program reads and writes only through its descriptors, and the shell decides before the start where they lead. The program therefore does not need to know anything about files, terminals or other programs, and the same small tools can be connected in ever new ways.

| Result | Where it comes from |
|---|---|
| `readlink /proc/self` shows a different number every time | every command runs in a new process with its own number (Section [1](prozesse-und-ihre-drei-strome.html#stufe-1)) |
| an error message appears on the screen despite `>` | it goes through descriptor 2; only 1 was redirected (Sections [1](prozesse-und-ihre-drei-strome.html#stufe-1) and [2](ausgaben-umleiten.html#stufe-2)) |
| `echo Hallo > gruss.txt` writes only `Hallo` into the file | the shell removes the redirection from the arguments (Section [2](ausgaben-umleiten.html#stufe-2)) |
| `2>&1 > file` leaves the message on the screen | redirections take effect from left to right; `2>&1` copies the current target (Section [2](ausgaben-umleiten.html#stufe-2)) |
| `sort a > a` leaves an empty file behind | the shell empties `a` before `sort` reads (Section [2](ausgaben-umleiten.html#stufe-2)) |
| `wc -l < file` writes no name | `wc` gets only a stream (Section [3](eingaben-umleiten.html#stufe-3)) |
| `wc -l < fehlt.txt` reports an error from bash | the shell opens the file; `wc` does not even start (Section [3](eingaben-umleiten.html#stufe-3)) |
| `ls /gibtsnicht \| wc -l` counts 0 | the pipe connects only descriptor 1 to 0; the message goes to the screen (Section [4](pipes-und-filter.html#stufe-4)) |
| `uniq` needs a `sort` in front of it | it compares each line only with the one directly before it (Section [4](pipes-und-filter.html#stufe-4)) |
| the second `echo $?` shows 0 | `$?` always applies to the most recently ended command (Section [5](der-exit-status.html#stufe-5)) |
| Ctrl+C leaves behind 130 | aborted by message 2, and $128 + 2 = 130$ (Section [5](der-exit-status.html#stufe-5)) |
| `sort fehlt.txt \| head` reports success | a pipeline has the exit status of its last command (Section [6](befehle-verketten.html#stufe-6)) |
| `a && b \|\| c` runs `c` although `a` succeeded | both operators have equal precedence and apply from the left (Section [6](befehle-verketten.html#stufe-6)) |
| `echo file \| rm` deletes nothing | a pipe delivers input, not arguments (Section [7](aus-einer-ausgabe-argumente-machen.html#stufe-7)) |
| `xargs` splits `mein foto.jpg` into two names | it separates at spaces; only the null byte occurs in no name (Section [7](aus-einer-ausgabe-argumente-machen.html#stufe-7)) |

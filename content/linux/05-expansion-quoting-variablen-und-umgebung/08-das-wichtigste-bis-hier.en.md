---
title: Key points so far
pfad: Computer Science / Linux and the Command Line / How the Shell Reads a Command Line: Expansion, Quoting, Variables, Environment
adresse: informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung
knoten: Chapter 5: How the Shell Reads a Command Line: Expansion, Quoting, Variables, Environment
order: 6100800
summary: What the shell makes of a line before a program starts, how to control that with quotes, what a program receives from the shell and how the shell finds it
tags: 
lang: en
---

:::kern Key points so far
<ul>

<li>

Between typing and the start of the program, the shell rewrites the line: expansion. The program receives only the finished argument list.

</li>

<li>

Pathname expansion replaces patterns with the sorted matching names; hidden files match only with a dot in the pattern, and with no match, the pattern stays. Brace expansion produces words without looking at files; tilde expansion inserts home directories.

</li>

<li>

`NAME=value` without spaces creates a shell variable; `$NAME` or `${NAME}` inserts its value, `$(command)` the output of a command, `$((…))` the result of a calculation with integers.

</li>

<li>

Word splitting splits the results of unprotected expansions at spaces, tabs and line ends; after that, pattern characters in them take effect. Single quotes protect everything, double quotes everything except `$`, `` ` `` and `\`, a backslash one character; at the end, the shell removes the typed quotes.

</li>

<li>

Order: splitting into words, braces, then tilde, parameters, arithmetic, command substitution, then word splitting, patterns, quote removal. Rule: `"$variable"` and `"$(command)"`.

</li>

<li>

Every process receives an environment of entries `NAME=value` when it starts. `export` adds a variable to it, `NAME=value command` applies to one command only, `env` and `printenv` show and modify it. A child receives a copy and cannot pass anything back.

</li>

<li>

`PATH` is the search path: directories with colons, searched from left to right, only for names without a slash. The working directory is not part of it, hence `./program`.

</li>

<li>

A new interactive bash reads `~/.bashrc`, a login shell `/etc/profile` and `~/.profile`. `source` runs a file in the running shell. Aliases apply only in interactive shells.

</li>

</ul>
:::

:::merke The answer in three sentences
<ol>

<li>

Before it starts a program, the shell replaces patterns, braces, tildes, variables, commands and calculations, splits the results into words and removes the quotes, in a fixed order; with quotes and the backslash, you determine which of this happens.

</li>

<li>

The program receives the finished words as arguments and, in addition, a copy of the environment with all exported variables; it cannot pass any of it back.

</li>

<li>

A program is found via the directories in `PATH`, and everything that a shell is to know every time it starts is in startup files such as `~/.bashrc`.

</li>

</ol>
:::

**One principle behind all the results.** Almost everything in this chapter follows from two ideas. First: the shell prepares, the program executes. Everything that happens to the typed line is done by the shell before the program starts, and the program sees only the result. Second: a process inherits; it cannot pass anything back. A child receives a copy, and what it does with it stays with the child.

| Result | Where it comes from |
|---|---|
| `ls` cannot tell whether `*.txt` or the names were typed | the shell replaces the pattern before the start (Section [1](expansion-muster-klammern-und-tilde.html#stufe-1)) |
| `rm *.bak` reports a name with an asterisk | with no match, the pattern stays (Section [1](expansion-muster-klammern-und-tilde.html#stufe-1)) |
| `ls foto{1,2,3}.jpg` reports a missing file | braces produce words without looking at files (Section [1](expansion-muster-klammern-und-tilde.html#stufe-1)) |
| `wohnort = Hamburg` results in “command not found” | the first word is the command (Section [2](variablen-befehlsersetzung-und-arithmetik.html#stufe-2)) |
| `$datei1.jpg` results in `.jpg` | without braces, the 1 belongs to the name (Section [2](variablen-befehlsersetzung-und-arithmetik.html#stufe-2)) |
| `$((7 / 2))` results in 3 | the shell calculates only with integers (Section [2](variablen-befehlsersetzung-und-arithmetik.html#stufe-2)) |
| `ls $datei` looks for `mein` and `bericht.txt` | word splitting of the inserted value (Section [3](worttrennung-und-quoting.html#stufe-3)) |
| `echo $(cat einkauf.txt)` writes one line | word splitting also splits at line ends (Section [3](worttrennung-und-quoting.html#stufe-3)) |
| `{1..$n}` stays as it is | brace expansion comes before parameter expansion (Section [3](worttrennung-und-quoting.html#stufe-3)) |
| `bash -c 'echo $obst'` shows nothing | the child receives only exported variables (Section [4](umgebung-und-vererbung.html#stufe-4)) |
| an `export` in the child does not change the shell | the child has only a copy (Section [4](umgebung-und-vererbung.html#stufe-4)) |
| `TZ=Asia/Tokyo date` does not change the shell | the assignment applies only to this command (Section [4](umgebung-und-vererbung.html#stufe-4)) |
| `meinbaum` is not found, but `./meinbaum` is | without a slash, only a search in `PATH` (Section [5](wie-die-shell-programme-findet-path.html#stufe-5)) |
| a new variable is missing in the next terminal | every shell starts afresh; only startup files remain (Section [6](startdateien-und-aliase.html#stufe-6)) |
| `source ~/.bashrc` takes effect, a child shell does not | `source` runs in the same process (Section [6](startdateien-und-aliase.html#stufe-6)) |

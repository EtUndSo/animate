---
title: Expansion: patterns, braces and the tilde
pfad: Computer Science / Linux and the Command Line / How the Shell Reads a Command Line: Expansion, Quoting, Variables, Environment
adresse: informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung
knoten: Chapter 5: How the Shell Reads a Command Line: Expansion, Quoting, Variables, Environment
order: 6100200
summary: Chapter 3 showed that the shell replaces patterns such as .jpg and the tilde with names before a command starts.
tags: Expansion, expansion, Pathname expansion, Brace expansion, Tilde expansion
lang: en
---

<span class="anker" id="stufe-1"></span>

:::zweck
[Chapter 3](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-verzeichnisse-und-pfade.html) showed that the shell replaces patterns such as `*.jpg` and the tilde with names before a command starts. This section gives this step its name, expansion, and takes a closer look at the replacements: how the shell resolves patterns, what happens with hidden files and with patterns that have no match, how braces create many words at once and when the tilde is replaced.
:::

:::::vorwissen What you need for this: words, patterns and processes

<span class="anker" id="stufe-1-1"></span>

This chapter assumes [Chapters 1](/wissen/en/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/ein-linux-zum-ueben.html) to 4. From them, you mainly need the following.

<ul>

<li>

The shell splits a command line into words at the spaces. The first word is the command, the others are its arguments ([Chapter 2, Section 2](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/der-aufbau-einer-befehlszeile.html#stufe-2)). The builtin command `echo` writes its arguments, separated by spaces, to standard output and therefore shows which arguments it has received.

</li>

<li>

A pattern is a word with `*`, `?` or `[…]`; the shell replaces it with the matching file names before the command starts ([Chapter 3, Section 6.6](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/kopieren-verschieben-loschen.html#stufe-6-6)). Names that begin with a dot are hidden files ([Chapter 3, Section 3.2](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/den-inhalt-eines-verzeichnisses-anzeigen.html#stufe-3-2)). The tilde `~` at the beginning of a word stands for the home directory ([Chapter 3, Section 2.6](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/das-arbeitsverzeichnis-und-pfade.html#stufe-2-6)).

</li>

<li>

You keep a file name with spaces together as one word with quotes or with a backslash before the space; the shell removes the quotes before the program starts ([Chapter 3, Section 3.7](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/den-inhalt-eines-verzeichnisses-anzeigen.html#stufe-3-7)).

</li>

<li>

A process is a running program with its own memory; the shell starts a new process for every program ([Chapter 4, Section 1.2](/wissen/en/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/prozesse-und-ihre-drei-strome.html#stufe-1-2)). `>` and `>>` redirect standard output into a file, `|` connects two programs ([Chapter 4, Sections 2.1](/wissen/en/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/ausgaben-umleiten.html#stufe-2-1), 2.2 and 4.1). `$?` returns the exit status of the last command; 127 means “command not found” ([Chapter 4, Sections 5.1](/wissen/en/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/der-exit-status.html#stufe-5-1) and [5.3](/wissen/en/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/der-exit-status.html#stufe-5-3)).

</li>

</ul>

⁠**In short:** You need command and arguments, `echo`, patterns, hidden files and the tilde, quotes in file names, the process, redirection and the pipe as well as the exit status.

:::warnung Only in your own practice directory
Some commands in this chapter create or delete files. So create a practice directory of your own and work there:

```console
$ mkdir ~/linuxk5
$ cd ~/linuxk5
```

All file names in the examples refer to this directory.
:::

In it, create the files that the chapter works with: three empty photo files, an empty note, a hidden file and the shopping list from [Chapter 4](/wissen/en/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/stroeme-umleitung-pipes-und-exit-status.html). For the list, after `cat > einkauf.txt` (`einkauf` is German for “shopping”), you type the four lines `Milch`, `Brot`, `Äpfel`, `Kaffee` and finally Ctrl+D:

```console
$ touch notiz.txt foto1.jpg foto2.jpg foto10.jpg .einstellungen
$ cat > einkauf.txt
Milch
Brot
Äpfel
Kaffee
$ ls -A
.einstellungen  einkauf.txt  foto1.jpg  foto10.jpg  foto2.jpg  notiz.txt
```

:::::

### Expansion

<span class="anker" id="stufe-1-2"></span>

Patterns and the tilde have something in common: what you type is not what the program receives. The shell rewrites the line beforehand. It does this not only with patterns and the tilde but with a whole series of characters, and it always does it in the same step.

[Chapter 2](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/die-shell-erste-befehle.html) compared the shell to a server in a restaurant. In the same picture for orientation: you write down an order with abbreviations, such as “2× daily special”. Before the slip goes to the kitchen, the server writes out every abbreviation in full. The kitchen receives only the written-out slip and never learns what the order originally looked like. Figure [1](#abb-1) shows the same for a command line.

:::abbildung linux/k5expansion 1
The expansion of `ls *.txt`: the shell splits the line into the words `ls` and `*.txt`, replaces the pattern with the matching names `einkauf.txt` and `notiz.txt` and only then starts `ls` with these two arguments. The program never sees the pattern.
:::

:::definition Definition 1.1 (Expansion)
<span class="anker" id="satz-1-1"></span>

__Expansion__ is the step in which the shell replaces certain parts of the words of a command line with other text. It happens after the shell has split the line into words and before it executes the command; the program receives only the result as its arguments.
:::

Expansion comprises several kinds of replacement. Each of these kinds is itself called an __expansion__, with a word in front that names the kind; every “… expansion” in this chapter is therefore one kind of expansion. Replacing a pattern is one expansion, replacing the tilde another; this chapter introduces more of them. From the result of an expansion, you cannot tell what was originally typed.

::::beispiel Pattern or names, the program cannot tell the difference
```console
$ echo *.txt
einkauf.txt notiz.txt
$ ls *.txt
einkauf.txt  notiz.txt
$ ls einkauf.txt notiz.txt
einkauf.txt  notiz.txt
```

`echo` shows what has become of the pattern: two names. In the second and in the third line, `ls` receives exactly the same two arguments; it cannot know whether you typed the pattern or the names.
::::

⁠**In short:** During expansion, the shell rewrites parts of the command line before the program starts; the program sees only the result.

:::hintergrund Why does the shell resolve patterns and not each program itself?
Even in the first Unix systems, it was not the individual programs that resolved patterns. The sixth edition of the Unix manual from 1975 has a helper program of its own for this, named `glob`: the shell of that time called it as soon as an argument contained `*`, `?` or `[`; it replaced the patterns with the matching names and then started the actual command. Later, this work moved into the shell itself. The old name lives on: patterns are often called *globs*.

Under Windows, things are different. There, a program receives the typed line as a whole and decides for itself whether it interprets `*.txt` as a pattern. Programs that are built in the C language with Microsoft's tools do not do this on their own; it has to be turned on specifically when building. Whether a pattern works there therefore depends on the individual program.

A derivation of our own, which is not found in this form in the manuals, explains the advantage of the Unix solution: because a single place resolves the patterns, they behave the same in every program, and no program needs a single line of code for it. The price is that a program never gets to see the pattern itself. If a program such as `find` is to evaluate a pattern itself, you have to protect the pattern from the shell, as with `find -name "*.txt"` in [Chapter 3, Section 10.2](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-finden-und-platz-messen.html#stufe-10-2).
:::

### Pathname expansion

<span class="anker" id="stufe-1-3"></span>

In [Chapter 3](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-verzeichnisse-und-pfade.html), patterns mostly stood alone and referred to the working directory. But a pattern may also be part of a path, and the matches come in a fixed order. Both deserve a closer look.

:::definition Definition 1.2 (Pathname expansion)
<span class="anker" id="satz-1-2"></span>

__Pathname expansion__ is the expansion that replaces a pattern with the names of the existing files and directories that it matches; each match becomes a word of its own. The matches appear sorted. If the pattern contains slashes, the shell checks each part of the path separately; a slash must appear in the pattern itself, because `*`, `?` and `[…]` never stand for it.
:::

Sorting follows the language setting. On the test system of this chapter, it compares the names character by character by the numbers of the characters, as with the shopping list in [Chapter 4, Section 2.7](/wissen/en/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/ausgaben-umleiten.html#stufe-2-7). That is why `foto10.jpg` comes before `foto2.jpg`: both names begin with `foto`, after that the next character decides, and the digit `1` has a lower number than the `2`. `foto1.jpg` comes even earlier, because the dot has a lower number than any digit.

::::beispiel Matches in the working directory and in /etc
```console
$ echo *.jpg
foto1.jpg foto10.jpg foto2.jpg
$ echo foto?.jpg
foto1.jpg foto2.jpg
$ echo foto[12].jpg
foto1.jpg foto2.jpg
$ echo /etc/host*
/etc/host.conf /etc/hostname /etc/hosts
```

The last pattern refers to the directory `/etc`: the part `/etc` contains no pattern character and stays as it is; only `host*` is compared with the names in `/etc`. The matches come back with the full path, just as the pattern was written.
::::

⁠**In short:** Pathname expansion replaces a pattern with the sorted names that match it, in paths as well; no pattern character stands for a slash.

### Hidden files and patterns

<span class="anker" id="stufe-1-4"></span>

With `rm *`, you delete all files of a directory, but not quite all: hidden files often contain settings, and it would be annoying if every pattern took them along. [Chapter 3](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-verzeichnisse-und-pfade.html) stated the rule for this in one sentence; Figure [2](#abb-2) shows it with the files of the practice directory.

:::abbildung linux/k5versteckt 2
Two patterns laid over the same names. `*` matches all visible names, `.einstellungen` (German for “settings”) stays gray. `.*` matches only `.einstellungen`; the entries `.` and `..` would have the right form, but they are skipped.
:::

:::satz Theorem 1.3 (Hidden files in patterns)
<span class="anker" id="satz-1-3"></span>

A name that begins with a dot matches a pattern only if the pattern itself has a dot at this position, that is, at its beginning or directly after a slash. With its default settings, bash never returns the entries `.` and `..` as matches.
:::

::::beispiel Visible and hidden matches
```console
$ echo *
einkauf.txt foto1.jpg foto10.jpg foto2.jpg notiz.txt
$ echo .*
.einstellungen
```

`*` captures everything except `.einstellungen`. `.*` captures only the hidden file, although `.` and `..` also begin with a dot.
::::

⁠**In short:** A pattern captures hidden files only if it itself has a dot at this position; `.` and `..` are never among the matches.

:::hintergrund What used to happen with .*
That `.` and `..` do not match `.*` is governed in bash by the option `globskipdots`, which has been turned on since version 5.2 from 2022. Older versions of bash and some other shells return the two entries as well. A command that works on entire directories would then also receive the parent directory as an argument via `..` and might act far beyond the intended directory. If you want to capture hidden files safely on older systems too, write `.[!.]*`: a dot, then a character that is not a dot, then any number of characters; only names that begin with two dots escape it. Conversely, `shopt -s dotglob` makes bash include hidden files with `*` as well; `shopt -u dotglob` turns this off again. The option applies only to the current session.
:::

### A pattern with no match

<span class="anker" id="stufe-1-5"></span>

What happens if a pattern does not match a single name? You might expect it to simply disappear. The shell does it differently, as Figure [3](#abb-3) shows.

:::abbildung linux/k5ohnetreffer 3
`rm *.bak` in a directory without a matching file. The shell compares the pattern with all names, finds no match and leaves the word unchanged. `rm` receives the text `*.bak` as an argument, looks for a file with exactly this name and reports that it does not exist.
:::

:::satz Theorem 1.4 (Pattern with no match)
<span class="anker" id="satz-1-4"></span>

If a pattern matches no name, the shell leaves the word unchanged. The program then receives the pattern as ordinary text.
:::

::::beispiel No PDF, no backup copy
```console
$ echo *.pdf
*.pdf
$ ls *.pdf
ls: cannot access '*.pdf': No such file or directory
$ rm *.bak
rm: cannot remove '*.bak': No such file or directory
```

The messages from `ls` and `rm` name the pattern itself. This proves that both programs received the text `*.pdf` and `*.bak`, respectively, and looked for a file with exactly this name.
::::

⁠**In short:** With no match, a pattern stays as it was typed, and the program receives it literally.

:::hintergrund Making a pattern with no match disappear
The rule comes from the standard for Unix shells; bash and dash follow it. The shell zsh, which Kali Linux and macOS, among others, use as their default shell, instead reports an error on its own when there is no match and does not start the command. bash offers two options that change the rule. With `nullglob`, a pattern with no match disappears completely; with `failglob`, the shell reports the error itself and does not start the command at all. `shopt -s` turns an option on, `shopt -u` turns it off again:

```console
$ shopt -s nullglob
$ echo Treffer: *.pdf
Treffer:
$ shopt -u nullglob
$ shopt -s failglob
$ echo Treffer: *.pdf
bash: no match: *.pdf
$ shopt -u failglob
```

With `nullglob`, `echo` received only the word `Treffer:`. With `failglob`, the message came from bash itself; `echo` did not run at all. Both options apply only to the current session. In everyday work at the command line, you usually leave them off; with `nullglob`, for example, `ls *.pdf` with no match would turn into `ls` without an argument and show the whole directory.
:::

### Brace expansion

<span class="anker" id="stufe-1-6"></span>

A pattern finds only names that already exist. Often, however, you need new names that follow a scheme: twelve directories for twelve months, a file for each day of the week, the same subdirectories for two years. For this, there is an expansion that creates words without looking at the files at all. As a picture for orientation: it works like a menu on which every dish may be combined with every side dish; Figure [4](#abb-4) shows this with two pairs of braces.

:::abbildung linux/k5klammer 4
Brace expansion of `urlaub/{2025,2026}/{sommer,winter}`: each element of the first pair of braces is joined with each element of the second, in the order in which they are written. One word becomes $2 \cdot 2 = 4$ words. No directory has to exist for this.
:::

:::definition Definition 1.5 (Brace expansion)
<span class="anker" id="satz-1-5"></span>

__Brace expansion__ turns a word with curly braces into several words. Inside the braces is either a list with commas, `{a,b,c}`, or a sequence `{x..y}` or `{x..y..s}` of integers or single letters, with the step $s$. Each element of the list or sequence yields one word; what stands in the word before the braces goes in front of each element, what stands after them goes behind each one. The words appear in the written order, not sorted.
:::

Brace expansion only replaces text and does not check whether files of this name exist. If a number in the sequence begins with a zero, all numbers get the same number of digits. If the braces contain neither a comma nor a valid sequence, the word stays as it is. Several pairs of braces in one word are combined with each other.

::::beispiel Lists and sequences
```console
$ echo foto{1,2,3}.jpg
foto1.jpg foto2.jpg foto3.jpg
$ echo {1..5} {a..e}
1 2 3 4 5 a b c d e
$ echo {01..12}
01 02 03 04 05 06 07 08 09 10 11 12
$ echo {0..20..5}
0 5 10 15 20
$ echo {a}
{a}
```

`foto3.jpg` does not exist, and yet the name appears. `{01..12}` writes every number with two digits, because the first one begins with a zero. `{a}` contains neither a comma nor a sequence and stays as it is.
::::

In this way, a single line creates a small directory tree for vacation photos in the practice directory, which the chapter continues to use. Afterward, a pattern with two pattern parts finds all four subdirectories:

```console
$ mkdir -p urlaub/{2025,2026}/{sommer,winter}
$ echo urlaub/*/*
urlaub/2025/sommer urlaub/2025/winter urlaub/2026/sommer urlaub/2026/winter
```

`mkdir` has received the four paths from Figure [4](#abb-4) as arguments; `-p` also creates missing parent directories ([Chapter 3, Section 5.1](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-und-verzeichnisse-anlegen.html#stufe-5-1)). In the pattern `urlaub/*/*`, the shell checks each part of the path separately: the first `*` matches `2025` and `2026`, the second matches `sommer` and `winter` in each of them. Figure [5](#abb-5) shows this walk through the levels.

:::abbildung linux/k5pfadmuster 5
Pathname expansion of `urlaub/*/*`, level by level. The part `urlaub` contains no pattern character and stays. The first `*` is compared with the names in `urlaub` and matches `2025` and `2026`; the second `*` is compared in each of these directories and matches `sommer` and `winter` in each. The result is four paths, sorted.
:::

::::beispiel [Counterexample] Braces are not a pattern
```console
$ ls foto[123].jpg
foto1.jpg  foto2.jpg
$ ls foto{1,2,3}.jpg
ls: cannot access 'foto3.jpg': No such file or directory
foto1.jpg  foto2.jpg
```

The pattern `foto[123].jpg` returns only the two existing names. The braces create all three names, and `ls` reports the missing one.
::::

⁠**In short:** Brace expansion creates several words from a list or sequence in curly braces, in the written order and without looking at files.

### Tilde expansion

<span class="anker" id="stufe-1-7"></span>

You know the tilde from [Chapter 3, Section 2.6](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/das-arbeitsverzeichnis-und-pfade.html#stufe-2-6). It, too, is an expansion, and with this knowledge its rules can be stated more precisely.

:::definition Definition 1.6 (Tilde expansion)
<span class="anker" id="satz-1-6"></span>

__Tilde expansion__ replaces a tilde at the beginning of a word. Everything from the tilde up to the first slash or to the end of the word is evaluated: if nothing follows the tilde, the shell inserts the path of your home directory; if a user name follows, it inserts the path of that user's home directory. If there is no such user, the text stays unchanged; a tilde in the middle of a word, as a rule, stays as it is too.
:::

::::beispiel Where the tilde is replaced
```console
$ echo ~ ~/linuxk5 ~root
/home/student /home/student/linuxk5 /root
$ echo a~ ~gibtsnicht
a~ ~gibtsnicht
```

With `~/linuxk5`, the evaluated part ends at the slash, and the rest stays attached. With `a~`, the tilde is not at the beginning of the word, and there is no user `gibtsnicht` on the test system.
::::

⁠**In short:** Tilde expansion replaces a tilde at the beginning of a word with a home directory, your own or that of the named user.

### Exercises for Section [1](#stufe-1)

<span class="anker" id="stufe-1-8"></span>

:::aufgabe Exercise 1 ★ What does echo receive?
<span class="anker" id="aufg-1"></span>

For your practice directory, predict what these commands output, and check it afterward: (a) `echo *.txt` (b) `echo foto*` (c) `echo f*.txt` (d) `echo *.gibts` (e) `echo .*` (f) `echo ~`.

:::loesung
```console
$ echo *.txt
einkauf.txt notiz.txt
$ echo foto*
foto1.jpg foto10.jpg foto2.jpg
$ echo f*.txt
f*.txt
$ echo *.gibts
*.gibts
$ echo .*
.einstellungen
$ echo ~
/home/student
```

(a) The two text files, sorted. (b) All three photos; `foto10.jpg` comes before `foto2.jpg` because the names are compared character by character, and the `1` comes before the `2`. (c) No name begins with `f` and ends in `.txt`; the photos end in `.jpg`. With no match, the pattern stays as it is. (d) Likewise. (e) Only the hidden file, because bash does not return `.` and `..` as matches. (f) The tilde on its own becomes the home directory. In all cases, `echo` received only the finished words.
:::
:::

:::aufgabe Exercise 2 ★ Counting braces
<span class="anker" id="aufg-2"></span>

(a) How many words does `echo {a,b,c}{1..4}` create, and in what order are they? (b) What does `echo {1..3}{a,b}` output? (c) In your practice directory, create the twelve directories `monat01` to `monat12` with a single line, and check the result with a pattern.

:::loesung
```console
$ echo {a,b,c}{1..4}
a1 a2 a3 a4 b1 b2 b3 b4 c1 c2 c3 c4
$ echo {1..3}{a,b}
1a 1b 2a 2b 3a 3b
$ mkdir monat{01..12}
$ echo monat*
monat01 monat02 monat03 monat04 monat05 monat06 monat07 monat08 monat09 monat10 monat11 monat12
```

(a) Each of the three elements in the first pair of braces is combined with each of the four in the second, so there are $3 \cdot 4 = 12$ words. The order follows the notation: the first pair of braces changes most slowly. (b) The same rule with $3 \cdot 2 = 6$ words. (c) `{01..12}` writes all numbers with two digits because the first one begins with a zero; `mkdir` receives twelve names. The pattern `monat*` finds them again (`monat` is German for “month”). Two-digit numbers have an advantage: when sorted, the months are in the right order, `monat10` after `monat09`.
:::
:::

:::aufgabe Exercise 3 ★★ Braces first, then patterns
<span class="anker" id="aufg-3"></span>

Predict what (a) `echo foto{10,2,1}.jpg` and (b) `echo foto{10,2,1}*` output in your practice directory, and check it. Explain the order of the names and why one name appears twice in (b).

:::loesung
```console
$ echo foto{10,2,1}.jpg
foto10.jpg foto2.jpg foto1.jpg
$ echo foto{10,2,1}*
foto10.jpg foto2.jpg foto1.jpg foto10.jpg
```

(a) Brace expansion creates three words in the written order: `foto10.jpg`, `foto2.jpg`, `foto1.jpg`. None of them contains a pattern character, so nothing gets sorted. (b) Here, brace expansion first creates the three patterns `foto10*`, `foto2*` and `foto1*`. Then pathname expansion replaces each pattern separately with its matches: `foto10*` matches `foto10.jpg`, `foto2*` matches `foto2.jpg`, and `foto1*` matches `foto1.jpg` and `foto10.jpg`. Sorting happens only within the matches of one pattern, not across all words; that is why `foto10.jpg` appears twice.
:::
:::

:::aufgabe Exercise 4 ★★ What is left
<span class="anker" id="aufg-4"></span>

Create a subdirectory `probe` with the files `a.txt` and `.b`: `mkdir probe` and `touch probe/a.txt probe/.b`. (a) Predict which file is still there after `rm probe/*`, and check it with `ls -A probe`. (b) What does `echo probe/*` output afterward, and why?

:::loesung
```console
$ mkdir probe
$ touch probe/a.txt probe/.b
$ rm probe/*
$ ls -A probe
.b
$ echo probe/*
probe/*
```

(a) `probe/*` matches only `probe/a.txt`. The name `.b` begins with a dot directly after the slash, and at this position the pattern has no dot; `rm` therefore never receives it as an argument, and the hidden file stays. (b) After that, there is no visible name left in `probe`. The pattern has no match and stays unchanged; `echo` writes it literally.
:::
:::

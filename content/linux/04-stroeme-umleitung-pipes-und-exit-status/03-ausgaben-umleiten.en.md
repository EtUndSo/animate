---
title: Redirecting output
pfad: Computer Science / Linux and the Command Line / Streams, Redirection, Pipes and Exit Status
adresse: informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status
knoten: Chapter 4: Streams, Redirection, Pipes and Exit Status
order: 6090300
summary: Until now, every output ended up on the screen.
tags: redirection, appending, copy
lang: en
---

<span class="anker" id="stufe-2"></span>

:::zweck
Until now, every output ended up on the screen. This section shows how to instruct the shell to direct the standard output and the standard error of a program into files instead, to append them to files or to throw them away, why the order matters and what trap lies in wait when you redirect into the very file you are reading.
:::

:::warnung Only in your own practice directory
The commands in this section and the following ones create files and overwrite them without asking. So create a practice directory of your own and work only there:

```console
$ mkdir ~/linuxk4
$ cd ~/linuxk4
```

All file names in the examples refer to this directory. Never write with `>` to a file whose contents you do not want to lose.
:::

### Output redirection: >

<span class="anker" id="stufe-2-1"></span>

Some results you want to keep instead of just watching them scroll past: a list of files, a shopping list, a log. For this, standard output would have to lead to a file instead of the terminal.

This is exactly what the shell can set up. In terms of the tubes from Figure [4](prozesse-und-ihre-drei-strome.html#abb-4): before it starts the program, it pulls the tube of standard output off the screen and plugs it into a file. The program writes to descriptor 1 as always; it does not notice that the bytes now end up in a file. Figure [6](#abb-6) shows the process.

:::abbildung linux/k4umleitung 6
The redirection `ls /usr > inhalt.txt`: the shell connects descriptor 1 of the new process to the file `inhalt.txt` instead of the screen; only then does `ls` start. The names flow into the file; nothing appears on the screen.
:::

:::definition Definition 2.1 (Redirection, output redirection)
<span class="anker" id="satz-2-1"></span>

A __redirection__ is an instruction to the shell to connect a descriptor of the new process to a different file before the program starts. The notation `command > file` connects standard output to the file `file`. If the file does not exist yet, the shell creates it; if it already exists, the shell empties it first.
:::

The characters `> file` are not arguments of the program. The shell evaluates them and removes them from the command line before it starts the program; the program gets only the remaining words. Spaces around the `>` character are allowed but not necessary.

::::beispiel Keeping the contents of /usr
```console
$ ls /usr > inhalt.txt
$ cat inhalt.txt
bin
games
include
lib
lib64
libexec
local
sbin
share
src
```

Nothing appears after the first command, because everything went into the file. In a file, the names are listed one below the other, one per line; `ls` arranges them side by side in columns only when it writes directly to a terminal.
::::

::::beispiel [Second example] echo never sees the redirection
```console
$ echo Hallo > gruss.txt
$ cat gruss.txt
Hallo
```

The file contains only `Hallo`. `echo` got `Hallo` as its only argument; it knows nothing about `> gruss.txt`.
::::

In [Chapter 3](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-verzeichnisse-und-pfade.html), you needed the editor `nano` for a file with contents. With a redirection, `cat` is enough: without an argument, it reads the keyboard, and its standard output goes into the file. This is how you create the shopping list that the following sections work with. Type `cat > einkauf.txt` (`einkauf` is German for “shopping”), then the four lines `Milch`, `Brot`, `Äpfel` (“apples”), `Kaffee` and finally Ctrl+D:

```console
$ cat > einkauf.txt
Milch
Brot
Äpfel
Kaffee
$ cat einkauf.txt
Milch
Brot
Äpfel
Kaffee
$ wc -c einkauf.txt
25 einkauf.txt
```

This time, each line appears only once, namely while you type it; what `cat` writes goes into the file. The list has 25 bytes, just like the one written with `nano` in [Chapter 3, Section 5.3](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-und-verzeichnisse-anlegen.html#stufe-5-3): four lines with their line ends and one umlaut letter, which takes up two bytes.

A redirection without a command empties a file or creates an empty file:

```console
$ > leer.txt
$ wc -c leer.txt
0 leer.txt
```

⁠**In short:** `command > file` sends standard output into a file that the shell creates or empties beforehand; the program notices nothing of this.

:::warnung > overwrites without asking
If the file already exists, its old contents are gone as soon as the shell sets up the redirection. There is no confirmation prompt. Try it on a copy:

```console
$ cp einkauf.txt probe.txt
$ echo Tee > probe.txt
$ cat probe.txt
Tee
```

Nothing is left of the shopping list in `probe.txt`. If you type the name of an important file instead of `probe.txt`, you lose it.
:::

:::hintergrund How the shell sets up a redirection
The shell needs a new process for every program, and it sets up the redirection at exactly the moment when this process already exists but the new program is not yet running in it. The decisive steps are three system calls:

<ol>

<li>

With `fork`, the kernel creates an almost exact copy of the shell process, with a number of its own. The copy inherits the open descriptors, including 0, 1 and 2, which lead to the terminal.

</li>

<li>

In the copy, the shell opens the target file, for `>` with the instruction to empty it; the file gets the lowest free number, say 3. Then it puts this file on descriptor 1 with the system call `dup2` and closes 3 again. Now descriptor 1 of the copy leads to the file, while descriptor 1 of the actual shell still leads to the terminal.

</li>

<li>

With `exec`, the copy loads the desired program, say `ls`, in place of the shell code. The open descriptors are kept. `ls` starts running, writes to descriptor 1 as always, and the bytes end up in the file.

</li>

</ol>

Meanwhile, the actual shell waits until the new process ends. Unix splits creating a process (`fork`) and loading a program (`exec`) into two steps precisely for cases like this: between the two steps, the shell can set up what the future program starts with, such as where its descriptors lead, without the program needing a single line of code for it. And because a terminal and a file look the same to a program (subsection [1.7](prozesse-und-ihre-drei-strome.html#stufe-1-7)), redirection works with every program.
:::

:::hintergrund A guard against accidental overwriting
The shell can refuse to overwrite an existing file with `>`. The command `set -o noclobber` turns this setting on for the current session, and `set +o noclobber` turns it off again. If you do want to overwrite a file in that case, you write `>|` instead of `>`:

```console
$ set -o noclobber
$ echo Tee > probe.txt
bash: probe.txt: cannot overwrite existing file
$ echo Tee >| probe.txt
$ set +o noclobber
```

The message comes from the shell itself: `echo` never even ran.
:::

### Appending: >>

<span class="anker" id="stufe-2-2"></span>

A shopping list grows, and a log gets new lines every day. The old contents should stay, and the new lines should be added at the end. This is not possible with `>`, because it empties the file first. Figure [7](#abb-7) puts the two ways side by side.

:::abbildung linux/k4anhaengen 7
The same file with four lines, written to twice. Top, with `>`: the old lines disappear before the new line arrives. Bottom, with `>>`: the old lines stay, and the new one is added at the end.
:::

:::definition Definition 2.2 (Appending)
<span class="anker" id="satz-2-2"></span>

The notation `command >> file` connects standard output to the file for __appending__: every byte written goes after the existing contents, and nothing is deleted. If the file does not exist, the shell creates it.
:::

In this way, the shopping list gets a fifth line:

```console
$ echo Butter >> einkauf.txt
$ cat einkauf.txt
Milch
Brot
Äpfel
Kaffee
Butter
```

The four old lines have stayed, and `Butter` is below them. The file now has 32 bytes, seven more: six letters and a line end.

⁠**In short:** `>>` appends standard output to a file without touching the old contents.

### Redirection of standard error: 2>

<span class="anker" id="stufe-2-3"></span>

Sometimes you want to keep the messages of a program for later, for example to look up what went wrong, or you want to keep them off the screen. For this, you have to be able to tell the shell which way out it should plug in elsewhere.

:::definition Definition 2.3 (Redirection of standard error)
<span class="anker" id="satz-2-3"></span>

The number of a descriptor may stand in front of `>` and `>>`, with no space in between. `command 2> file` redirects standard error into the file, and `command 2>> file` appends it to the file. Without a number, 1 applies: `>` means the same as `1>`.
:::

::::beispiel The message in a file of its own
```console
$ ls /etc/hostname /gibtsnicht 2> fehler.txt
/etc/hostname
$ cat fehler.txt
ls: cannot access '/gibtsnicht': No such file or directory
```

Only the result is still on the screen; the message went into the file. This also proves what subsection [1.6](prozesse-und-ihre-drei-strome.html#stufe-1-6) claimed: the two lines came through different ways out.
::::

⁠**In short:** `2>` redirects standard error; a number in front of `>` selects the descriptor.

### The file that swallows everything: /dev/null

<span class="anker" id="stufe-2-4"></span>

Often you do not want to keep an output but simply get rid of it: messages you already know, or results you do not need. Creating a file for this and deleting it again would be cumbersome. Figure [8](#abb-8) shows where the error output can go instead.

:::abbildung linux/k4zweidateien 8
Two targets for the error output. Left: standard output leads to `aus.txt`, standard error to `fehler.txt`; each line ends up in its own file. Right: standard error leads to `/dev/null`, and the messages are discarded.
:::

The target is the device file `/dev/null` from [Chapter 3, Section 7.7](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/die-verzeichnisstruktur-von-linux.html#stufe-7-7): it accepts everything that is written to it and discards it; anyone who reads from it reaches the end of the stream at once, which is why `cat /dev/null` outputs nothing.

:::definition Definition 2.4 (Discarding output)
<span class="anker" id="satz-2-4"></span>

`command 2> /dev/null` discards the messages of a program, `command > /dev/null` its results. The program notices nothing of this: every write request succeeds.
:::

::::beispiel Hiding messages
`find` searches `/etc` for entries named `hostname` ([Chapter 3, Section 10.1](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-finden-und-platz-messen.html#stufe-10-1)). An ordinary user may not read some of the directories; the reason does not matter here. `find` reports each of them:

```console
$ find /etc -name hostname
/etc/apparmor.d/hostname
find: ‘/etc/credstore’: Permission denied
find: ‘/etc/credstore.encrypted’: Permission denied
/etc/hostname
find: ‘/etc/polkit-1/rules.d’: Permission denied
find: ‘/etc/ssl/private’: Permission denied
$ find /etc -name hostname 2> /dev/null
/etc/apparmor.d/hostname
/etc/hostname
```

The messages about the locked directories disappear, and the two matches remain. The matches are also no longer hidden among the messages.
::::

⁠**In short:** `/dev/null` swallows everything that is written to it; `2> /dev/null` hides messages.

### Copying a descriptor: 2>&1 and &>

<span class="anker" id="stufe-2-5"></span>

For a complete log, results and messages should go into the same file, in the order in which they arise. Opening the same file twice with `>` would go wrong, because two descriptors would then write to the start of the file independently of each other and overwrite each other. Instead, descriptor 2 should simply lead to where descriptor 1 already leads.

:::definition Definition 2.5 (Copying a descriptor)
<span class="anker" id="satz-2-5"></span>

The notation `n>&m` makes descriptor $n$ a __copy__ of descriptor $m$: afterward, $n$ leads to the same open file as $m$ at that moment. So `2>&1` means: standard error should lead to where standard output currently leads. Without a number in front of the symbol, 1 applies again: `>&2` makes standard output a copy of standard error.
:::

The `&` tells the shell that `>` is followed by the number of a descriptor and not by a file name. For the most common case, both ways out into one file, bash has a short form: `command &> file` means the same as `command > file 2>&1`, and `command &>> file` appends both. Not all shells understand the short form, but every shell understands the long form.

::::beispiel Result and message in one file
```console
$ ls /etc/hostname /gibtsnicht > alles.txt 2>&1
$ cat alles.txt
ls: cannot access '/gibtsnicht': No such file or directory
/etc/hostname
$ ls /etc/hostname /gibtsnicht &> beides.txt
$ cat beides.txt
ls: cannot access '/gibtsnicht': No such file or directory
/etc/hostname
```

Nothing appears on the screen for either call. Both files contain both lines, in the order in which `ls` wrote them.
::::

::::beispiel [Second example] Your own message to standard error
If you want to output a warning yourself, send it to standard error with `>&2`, as is proper for messages:

```console
$ echo "Achtung: Die Liste ist leer." >&2
Achtung: Die Liste ist leer.
```

On the screen, this looks like any other output, because descriptor 2 also leads to the terminal. The quotation marks hold the sentence (German for “Caution: The list is empty.”) together as a single argument, as with file names that contain spaces ([Chapter 3, Section 3.7](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/den-inhalt-eines-verzeichnisses-anzeigen.html#stufe-3-7)).
::::

⁠**In short:** `2>&1` makes the error output lead to where standard output currently leads; `&>` is the short form for both ways out into one file.

### The order of redirections

<span class="anker" id="stufe-2-6"></span>

`> alles.txt 2>&1` and `2>&1 > alles.txt` contain exactly the same characters. Even so, they do different things, and the difference surprises almost everyone who sees it for the first time. Figure [9](#abb-9) goes through both lines step by step.

:::abbildung linux/k4reihenfolge 9
Where descriptors 1 and 2 lead after each step. Top, `> alles.txt 2>&1`: first 1 leads to the file, then 2 takes over this target. Bottom, `2>&1 > nur.txt`: first 2 takes over the target of 1, which is still the terminal; then only 1 switches to the file, and 2 stays with the terminal.
:::

:::satz Theorem 2.6 (Order of redirections)
<span class="anker" id="satz-2-6"></span>

The shell carries out the redirections of a command line from left to right, one after the other. With `2>&1`, descriptor 2 takes over the target that descriptor 1 has at exactly that moment; later redirections of descriptor 1 no longer change anything about descriptor 2.
:::

::::beispiel Two lines, two results
In the previous subsection, everything ended up in the file with `> alles.txt 2>&1`. With the reverse order:

```console
$ ls /etc/hostname /gibtsnicht 2>&1 > nur.txt
ls: cannot access '/gibtsnicht': No such file or directory
$ cat nur.txt
/etc/hostname
```

The message appears on the screen; only the result is in the file. The lower half of Figure [9](#abb-9) follows where the two descriptors lead after each step. In this order, `2>&1` changes nothing at all, because descriptor 2 already led to the terminal. Only afterward does descriptor 1 switch to the file, and this switch does not take descriptor 2 along.
::::

⁠**In short:** Redirections take effect from left to right; `2>&1` copies the target that 1 has at that moment, which is why it goes after `> file`.

:::hintergrund Why the copy does not move along
The shell carries out `2>&1` with the system call `dup2`. In the list of descriptors, it enters at number 2 the same open file that is at number 1. It does not set up a link “2 always follows 1”; instead, it copies the entry as it is at that moment. As a picture for orientation: if you copy down a friend's address, you then have an address on your note; if the friend moves, the note is no longer correct. If descriptor 1 is afterward connected to a different file, it gets a new entry, and the copied entry at 2 stays as it was. The picture has a limit: afterward, both descriptors really share the same open file, including the position at which the next write takes place. That is why the result and the message in `alles.txt` do not overwrite each other but come one after the other.
:::

### The truncation trap

<span class="anker" id="stufe-2-7"></span>

A list is to be sorted, and the result is to be stored under the same name again. The obvious command for this destroys the list. The command `sort` sorts the lines of the files you name and writes them to standard output; this example needs nothing more from it. Figure [10](#abb-10) shows what happens, step by step, with `sort probe.txt > probe.txt`.

:::abbildung linux/k4kuerzung 10
The truncation trap as a timeline. First the shell opens `probe.txt` for the redirection and empties the file in the process: 32 bytes become 0. Then `sort` starts, reads the empty file and writes nothing. In the end, the list is lost.
:::

:::satz Theorem 2.7 (Truncation trap)
<span class="anker" id="satz-2-7"></span>

With `command file > file`, the file is empty before the command starts. The shell sets up the redirection before the program starts, and `>` empties the file in the process. The program then reads an empty file; the old contents are lost.
:::

::::beispiel A list becomes empty
Try it on a copy of the shopping list:

```console
$ cp einkauf.txt probe.txt
$ wc -c probe.txt
32 probe.txt
$ sort probe.txt > probe.txt
$ wc -c probe.txt
0 probe.txt
```

32 bytes have become zero. There was no error message, because from the point of view of `sort`, everything went right: it sorted an empty file.
::::

There are two safe ways. Either you first write the result to a different file and then rename that file ([Chapter 3, Section 6.3](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/kopieren-verschieben-loschen.html#stufe-6-3)), or you use the option `-o` of `sort`: it writes the result to the named file and opens that file only once everything has been read.

```console
$ cp einkauf.txt probe.txt
$ sort probe.txt > sortiert.txt
$ mv sortiert.txt probe.txt
$ cat probe.txt
Brot
Butter
Kaffee
Milch
Äpfel
$ cp einkauf.txt probe2.txt
$ sort -o probe2.txt probe2.txt
$ cat probe2.txt
Brot
Butter
Kaffee
Milch
Äpfel
```

`Äpfel` comes last because of the language setting of the test system, which sorts by the numbers of the characters; `Ä` has a higher number than all letters without an umlaut.

⁠**In short:** Never read from a file and write with `>` into the same file; the shell empties it before the program can read it.

:::hintergrund Why the file is empty before the program even starts
The shell processes a command line in a fixed order: it splits the line into words, prepares the words, then sets up the redirections and only at the very end starts the program. When setting up `>`, it opens the target file with the instruction to the kernel to truncate it to length zero; this happens in the new process between `fork` and `exec` (subsection [2.1](#stufe-2-1)). By the time `sort` begins to read, the truncation has long since happened. `sort -o` avoids this because there `sort` itself decides when to open the target file: only after it has read the entire input. With `>>` instead of `>`, the file is not emptied, but then a program may keep reading what it has just written to the end itself, and the file grows until the storage device is full. `cat` therefore checks for this and refuses, in the uutils implementation of Ubuntu 26.04 as well as in the GNU implementation:

```console
$ cat probe.txt >> probe.txt
cat: probe.txt: input file is output file
$ gnucat probe.txt >> probe.txt
gnucat: probe.txt: input file is output file
```

Do not rely on this caution: most programs do not check for it.
:::

### Exercises for Section [2](#stufe-2)

<span class="anker" id="stufe-2-8"></span>

:::aufgabe Exercise 5 ★ Separating the streams
<span class="anker" id="aufg-5"></span>

In your practice directory, run `ls /etc/hostname /gibtsnicht > aus.txt 2> fehler2.txt`. (a) What appears on the screen? (b) What is in `aus.txt`, and what is in `fehler2.txt`? (c) What changes if you write the redirection `2> /dev/null` instead of `2> fehler2.txt`?

:::loesung
```console
$ ls /etc/hostname /gibtsnicht > aus.txt 2> fehler2.txt
$ cat aus.txt
/etc/hostname
$ cat fehler2.txt
ls: cannot access '/gibtsnicht': No such file or directory
$ ls /etc/hostname /gibtsnicht > aus.txt 2> /dev/null
$ cat aus.txt
/etc/hostname
```

(a) Nothing appears on the screen, because both ways out are redirected. (b) `aus.txt` (German for “out”) contains the result `/etc/hostname`, `fehler2.txt` (`fehler` is German for “error”) the message. (c) The message disappears into `/dev/null`; `aus.txt` contains the same as before, because `>` emptied the file and wrote it anew.
:::
:::

:::aufgabe Exercise 6 ★ What is in the file at the end?
<span class="anker" id="aufg-6"></span>

Predict what `tag.txt` contains after these four lines, and check it:

```console
$ echo Montag > tag.txt
$ echo Dienstag >> tag.txt
$ echo Mittwoch > tag.txt
$ echo Donnerstag >> tag.txt
```

:::loesung
```console
$ cat tag.txt
Mittwoch
Donnerstag
```

After the first two lines, the file contains `Montag` and `Dienstag`. The third line uses `>`: the shell empties the file, and afterward it contains only `Mittwoch`. The fourth appends `Donnerstag`.
:::
:::

:::aufgabe Exercise 7 ★★ Predicting the order
<span class="anker" id="aufg-7"></span>

Each line uses the command `ls /etc/hostname /gibtsnicht` with different redirections. Predict what appears on the screen and what is in the file; to do so, write down the targets of descriptors 1 and 2 after each step, as in Figure [9](#abb-9), and check on the computer: (a) `> a.txt 2>&1` (b) `2>&1 > b.txt` (c) `2> c.txt 1>&2` (d) `1>&2 2> d.txt`.

:::loesung
```console
$ ls /etc/hostname /gibtsnicht > a.txt 2>&1
$ cat a.txt
ls: cannot access '/gibtsnicht': No such file or directory
/etc/hostname
$ ls /etc/hostname /gibtsnicht 2>&1 > b.txt
ls: cannot access '/gibtsnicht': No such file or directory
$ cat b.txt
/etc/hostname
$ ls /etc/hostname /gibtsnicht 2> c.txt 1>&2
$ cat c.txt
ls: cannot access '/gibtsnicht': No such file or directory
/etc/hostname
$ ls /etc/hostname /gibtsnicht 1>&2 2> d.txt
/etc/hostname
$ cat d.txt
ls: cannot access '/gibtsnicht': No such file or directory
```

At the start, 1 and 2 lead to the terminal (T).

<ul>

<li>

(a) `> a.txt`: 1 → `a.txt`, 2 → T. `2>&1`: 2 → `a.txt`. Nothing on the screen, both lines in the file.

</li>

<li>

(b) `2>&1`: 2 → T, because that is the target of 1. `> b.txt`: 1 → `b.txt`, 2 stays with T. The message on the screen, the result in the file.

</li>

<li>

(c) `2> c.txt`: 2 → `c.txt`, 1 → T. `1>&2`: 1 → `c.txt`. Like (a) with the roles swapped: nothing on the screen, both lines in the file.

</li>

<li>

(d) `1>&2`: 1 → T, because that is the target of 2. `2> d.txt`: 2 → `d.txt`, 1 stays with T. Like (b) with the roles swapped: the result on the screen, the message in the file.

</li>

</ul>

In all four cases, what decides is the target behind the copied descriptor at the moment of the copy; later redirections change nothing about a copy.
:::
:::

:::aufgabe Exercise 8 ★★ The truncation trap
<span class="anker" id="aufg-8"></span>

(a) Use `cat > zahlen.txt` to create a file with the lines `3`, `1`, `2`. Predict what `sort zahlen.txt > zahlen.txt` does, and check it with `wc -c`. (b) Create the file again and sort it in two safe ways. (c) `head -n 2 zahlen.txt > zahlen.txt` is supposed to keep only the first two lines. What really happens, and why does it not help that `head` needs only two lines?

:::loesung
(a) Prediction: the file is empty afterward. The check:

```console
$ cat > zahlen.txt
3
1
2
$ sort zahlen.txt > zahlen.txt
$ wc -c zahlen.txt
0 zahlen.txt
```

The shell emptied `zahlen.txt` (German for “numbers”) for the redirection before `sort` started; `sort` sorted an empty file.

(b) Via an intermediate file that replaces the old one only on success, or with `sort -o`. Here, as a shortcut, the file is created anew with `printf`, which writes the sequence `\n` as a line end; `cat >` with three typed lines does the same:

```console
$ printf '3\n1\n2\n' > zahlen.txt
$ sort zahlen.txt > sortiert.txt && mv sortiert.txt zahlen.txt
$ cat zahlen.txt
1
2
3
$ printf '3\n1\n2\n' > zahlen.txt
$ sort -o zahlen.txt zahlen.txt
$ cat zahlen.txt
1
2
3
```

(c) Here, too, an empty file remains:

```console
$ head -n 2 zahlen.txt > zahlen.txt
$ wc -c zahlen.txt
0 zahlen.txt
```

It does not matter how much a program reads. The file is emptied before `head` even starts; by the time it reads, nothing is left, not even the first two lines.
:::
:::

:::aufgabe Exercise 9 ★★★ The forgotten &
<span class="anker" id="aufg-9"></span>

Someone wants to send the error message to standard output with `ls /gibtsnicht 2>1`. Predict what appears on the screen and which file is new in the practice directory afterward, and check it. Using the definition from subsection [2.5](#stufe-2-5), explain what the `&` is for.

:::loesung
```console
$ ls /gibtsnicht 2>1
$ cat 1
ls: cannot access '/gibtsnicht': No such file or directory
$ rm 1
```

Nothing appears on the screen, and afterward the practice directory contains a file named `1` that holds the message. Without `&`, the word after `2>` is a file name, even if it consists of only one digit. Only `2>&1` tells the shell that the 1 means a descriptor of which descriptor 2 is to become a copy.
:::
:::

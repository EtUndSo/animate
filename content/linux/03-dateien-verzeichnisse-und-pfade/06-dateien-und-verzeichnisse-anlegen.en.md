---
title: Creating files and directories
pfad: Computer Science / Linux and the Command Line / Files, Directories and Paths
adresse: informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade
knoten: Chapter 3: Files, Directories and Paths
order: 6080600
summary: So far, you have only looked.
tags: mkdir, -p, touch, text editor, nano, tree
lang: en
---

<span class="anker" id="stufe-5"></span>

:::zweck
So far, you have only looked. From here on, you change the tree: you create directories, make files, write text into them and view the result as a tree. Along the way, a small playground for practice comes into being.
:::

:::warnung Work only in your own practice directory
From now on, the commands change files. Create everything in the practice directory `~/linuxk3`, which this section sets up, and use commands that change something only there. As an ordinary user, you cannot change the system's files anyway; so in this chapter, never type a command preceded by `sudo`, which would make you the user `root`. Under WSL 2, the practice directory belongs in the Linux part, not under `/mnt/c` ([Chapter 1, Section 4.7](/wissen/en/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/wsl-2-linux-neben-windows.html#stufe-4-7)).
:::

### Creating a directory: mkdir

<span class="anker" id="stufe-5-1"></span>

If you want to keep things in order, you first create directories: one for recipes, one for photos. There is a command of its own for this.

:::definition Definition 5.1 (mkdir)
<span class="anker" id="satz-5-1"></span>

The command __mkdir__ (short for “make directory”) creates a new, empty directory for each argument. The parent directory must already exist, and the name must not already be taken in it.
:::

A new directory is not completely empty: from the start, it contains the entries `.` and `..`. A directory that has only these two counts as empty.

::::beispiel The practice directory
```text
student@labor:~$ cd
student@labor:~$ mkdir linuxk3
student@labor:~$ cd linuxk3
student@labor:~/linuxk3$ mkdir rezepte fotos
student@labor:~/linuxk3$ ls -F
fotos/  rezepte/
student@labor:~/linuxk3$ mkdir rezepte
mkdir: rezepte: File exists
```

One call may create several directories. The second attempt to create `rezepte` (German for “recipes”) fails because the name is taken. The GNU implementation, which an ordinary Linux such as Debian uses and which is called `gnumkdir` under Ubuntu 26.04 ([Chapter 2, Section 7.3](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/zwei-fassungen-der-grundbefehle-gnu-und-uutils.html#stufe-7-3)), reports the same thing in more detail: `cannot create directory ‘rezepte’: File exists`. The terse form reflects the state of uutils version 0.8 in Ubuntu 26.04; later versions may bring their messages in line with GNU.
::::

**With intermediate directories: mkdir -p.** If you want to create several levels at once, `mkdir` fails because the parent directory is still missing. The option __-p__ (short for “parents”) also creates missing intermediate directories and reports no error if a directory already exists. Figure [17](#abb-17) shows how one level after another comes into being.

:::abbildung linux/k3mkdirp 17
`mkdir fotos/urlaub/2026` fails because `urlaub` is missing. `mkdir -p` creates `urlaub` and then `2026`; the directories that are already there are left untouched.
:::

::::beispiel [Second example] Three levels at once
```console
$ mkdir fotos/urlaub/2026
mkdir: No such file or directory
$ mkdir -p fotos/urlaub/2026 rezepte/kuchen rezepte/suppen
$ ls -F fotos fotos/urlaub
fotos:
urlaub/

fotos/urlaub:
2026/
```

Under Ubuntu 26.04, the first message currently does not even name the path; the GNU implementation writes `cannot create directory ‘fotos/urlaub/2026’: No such file or directory`. In both cases, the meaning is: a directory is missing along the way. With `-p`, it works, and `rezepte/kuchen` and `rezepte/suppen` are created in passing.
::::

⁠**In short:** `mkdir` creates directories; with `-p`, it also creates all missing levels above them.

### Creating an empty file: touch

<span class="anker" id="stufe-5-2"></span>

Sometimes you need a file before you write anything into it, for example as a placeholder for a list that you are about to fill. The command for this actually has a different main task; Figure [18](#abb-18) shows both.

:::abbildung linux/k3touch 18
`touch` on a new name creates an empty file with 0 bytes. `touch` on an existing file leaves the contents unchanged and only sets the clock of the last modification to now.
:::

:::definition Definition 5.2 (touch)
<span class="anker" id="satz-5-2"></span>

The command __touch__ sets the time of the last modification and of the last access of each file named to the current time. If the file does not exist yet, it creates it as an empty file with 0 bytes.
:::

`touch` never changes the contents of an existing file, even if its name suggests otherwise. With the option `-t`, you can enter any time instead of the current time, written as `YYYYMMDDhhmm`.

::::beispiel A placeholder for the shopping list
```console
$ touch einkauf.txt
$ ls -l einkauf.txt
-rw-r--r-- 1 student student 0 Nov 10 02:41 einkauf.txt
```

The new file belongs to you (`student`) and has 0 bytes.
::::

::::beispiel [Second example] Setting the clock back and forward again
```console
$ touch -t 202611091830 einkauf.txt
$ ls -l einkauf.txt
-rw-r--r-- 1 student student 0 Nov  9 18:30 einkauf.txt
$ touch einkauf.txt
$ ls -l einkauf.txt
-rw-r--r-- 1 student student 0 Nov 10 02:41 einkauf.txt
```

First, `touch` enters the evening of the previous day, then the current time again. The size stays 0. Under GNU, the option `-d` with a time such as `"2026-11-09 18:30"` does the same; however, uutils version 0.8 in Ubuntu 26.04 interprets such a time as UTC and therefore shifts it: in winter in Germany, the result is one hour later. This is a bug in this version that may disappear with an update. `-t` behaves the same in both implementations.
::::

⁠**In short:** `touch` creates an empty file or, for an existing one, only sets the modification time to now.

:::hintergrund Three timestamps per file
Linux keeps track of several times for each file. The modification time, which `ls -l` shows, belongs to the last write of the contents. The access time belongs to the last read; so that not every read triggers a write to the storage device, Linux usually updates it only if it is older than the modification time or older than one day. A third time, the status change time, advances with every change to the file's administrative information, such as the permissions or the name; it cannot be set back, not even with `touch`. Many file systems also store the creation time. Backup programs use the modification time to copy only what has changed since the last time; with `touch`, you can therefore make them believe that a file is new.
:::

### The text editor nano

<span class="anker" id="stufe-5-3"></span>

An empty file is only the beginning; now text should go into it. A graphical program such as Windows Notepad does not exist in the terminal, but there are editors that run in the terminal window itself.

:::definition Definition 5.3 (Text editor, nano)
<span class="anker" id="satz-5-3"></span>

A __text editor__ is a program with which you create and change text files; it stores only the characters, no font and no formatting. __nano__ is a simple text editor that runs in the terminal and constantly shows the most important shortcuts at the bottom edge.
:::

You start it with `nano file`. If the file exists, nano shows its contents; if it does not, nano starts with an empty page and creates the file only when you save. You type as in any editor; the arrow keys move the cursor. The commands work through shortcuts that nano lists at the bottom: there, the character `^` stands for the Ctrl key, `M-` for the Alt key. Under Ubuntu 26.04, these lines are in English as long as the system language is English. Figure [19](#abb-19) shows the structure of the window.

:::abbildung linux/k3nano 19
The nano window as a diagram: at the top, a title bar with program and file name (an asterisk means “unsaved”); in the middle, the text with the cursor; at the bottom, a status bar for messages and two lines with shortcuts. One after another, the shortcuts for saving and for quitting light up.
:::

You need these shortcuts all the time:

<ul>

<li>

⁠**Ctrl+O** saves (“Write Out”); nano asks for the file name at the bottom, and Enter confirms it.

</li>

<li>

⁠**Ctrl+X** quits nano; if the text is unsaved, nano first asks whether it should save it (`Y` for yes, `N` for no).

</li>

<li>

⁠**Ctrl+K** cuts the line the cursor is on, **Ctrl+U** pastes it back in.

</li>

<li>

⁠**Ctrl+F** searches for a word, **Ctrl+G** shows the help.

</li>

</ul>

::::beispiel Writing the shopping list
In the practice directory, type `nano einkauf.txt`. Write the four lines `Milch`, `Brot`, `Äpfel` and `Kaffee` (milk, bread, apples and coffee), pressing Enter after each of the first three. After the last line, you do not press Enter; nano adds the line end itself when saving. This is what the window looks like when you have finished typing, here 72 characters wide and 16 lines high:

```text
  GNU nano 8.7.1                  einkauf.txt *
Milch
Brot
Äpfel
Kaffee
...
^G Help       ^O Write Out  ^F Where Is   ^K Cut        ^T Execute
^X Exit       ^R Read File  ^\ Replace    ^U Paste      ^J Justify
```

Ctrl+O asks `Write to File: einkauf.txt` at the bottom; after Enter, nano reports `[ Wrote 4 lines ]`, and the asterisk in the title bar disappears. Ctrl+X quits nano. Back at the prompt, you check the result:

```console
$ cat einkauf.txt
Milch
Brot
Äpfel
Kaffee
$ wc einkauf.txt
 4  4 25 einkauf.txt
```

Four lines, four words, 25 bytes. There are only 24 characters, because the `Ä` takes two bytes (subsection [4.1](dateien-ansehen.html#stufe-4-1)): including the line end, `Milch` has 6 characters and 6 bytes, `Brot` 5 and 5, `Kaffee` 7 and 7, but `Äpfel` 6 characters and 7 bytes. Figure [20](#abb-20) adds up the bytes line by line: $6 + 5 + 7 + 7 = 25$.

:::abbildung linux/k3einkauf 20
The bytes of the shopping list, counted line by line: `Milch` 6, `Brot` 5, `Äpfel` 7, `Kaffee` 7, each including the line end. The sum is 25, as `wc` reports.
:::

Create three recipes in the same way, `rezepte/kuchen/apfelkuchen.txt`, `rezepte/kuchen/kaesekuchen.txt` and `rezepte/suppen/kuerbissuppe.txt` (apple cake, cheesecake and pumpkin soup), each with a few lines of ingredients. You simply give nano the path as an argument.
::::

⁠**In short:** `nano file` opens a text editor in the terminal; Ctrl+O saves, Ctrl+X quits.

:::hintergrund Other editors and why you need one in the terminal
Many servers have no graphical desktop, and over a network connection, you often reach the computer only through a terminal. An editor that runs in the terminal works there just as it does at your own desk. nano is available on almost every Linux and is easy to use. Many professionals use vim instead, a more powerful editor with its own operating logic: there, you first type commands instead of text. If you get lost in vim, you leave it without saving by pressing Esc, then typing `:q!` and pressing Enter. Under WSL 2, you can also edit Linux files with editors on Windows, for example with Visual Studio Code and its WSL extension; Windows Notepad is less suitable for this because under certain circumstances it writes a different line end.
:::

### The tree at a glance: tree

<span class="anker" id="stufe-5-4"></span>

After a few rounds of `mkdir` and `nano`, it is easy to lose track of what is where. `ls` always shows only one level; the whole tree would be nicer.

:::definition Definition 5.4 (tree)
<span class="anker" id="satz-5-4"></span>

The command __tree__ draws the directory tree starting at the directory named, or without an argument starting at the working directory, with lines for the levels, and at the end counts the directories and files. With `-a`, it also shows hidden entries.
:::

`tree` is not preinstalled on Ubuntu. If the shell reports `command not found`, type the following command once; it is the only exception to the rule in the caution box above:

```console
$ sudo apt install tree
```

`sudo` runs the command with the privileges of `root` and for this asks for the password that you chose when setting up your Linux account ([Chapter 1, Section 4.2](/wissen/en/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/wsl-2-linux-neben-windows.html#stufe-4-2)); no characters appear as you type. `apt` is Ubuntu's package manager ([Chapter 1, Section 1.6](/wissen/en/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/betriebssystem-kernel-und-distribution.html#stufe-1-6)) and installs the program from the distribution's package sources. If that is not possible, for example on someone else's computer, `ls -R` from subsection [3.6](den-inhalt-eines-verzeichnisses-anzeigen.html#stufe-3-6) shows the same entries, only directory by directory instead of as a tree.

::::beispiel The playground
First create a few empty photo files and a hidden settings file; then `tree` shows everything:

```console
$ cd fotos/urlaub/2026
$ touch strand_1.jpg strand_2.jpg strand_10.jpg berg_1.jpg berg_2.jpg notiz.txt
$ ls
berg_1.jpg  notiz.txt     strand_10.jpg
berg_2.jpg  strand_1.jpg  strand_2.jpg
$ cd ~/linuxk3
$ touch .einstellungen
```

```console
$ tree
.
├── einkauf.txt
├── fotos
│   └── urlaub
│       └── 2026
│           ├── berg_1.jpg
│           ├── berg_2.jpg
│           ├── notiz.txt
│           ├── strand_1.jpg
│           ├── strand_10.jpg
│           └── strand_2.jpg
└── rezepte
    ├── kuchen
    │   ├── apfelkuchen.txt
    │   └── kaesekuchen.txt
    └── suppen
        └── kuerbissuppe.txt

7 directories, 10 files
```

Seven directories are counted, including the working directory `.`, and ten files. `.einstellungen` is missing because it is hidden; `tree -a` shows it as well. The examples in the following sections run on this playground.
::::

⁠**In short:** `tree` shows a subtree with all its levels at once.

### Exercises for Section [5](#stufe-5)

<span class="anker" id="stufe-5-5"></span>

:::aufgabe Exercise 14 ★ Intermediate directories
<span class="anker" id="aufg-14"></span>

In the practice directory, you type `mkdir projekt/daten/roh` although `projekt` does not exist. What happens? How do you create all three levels with a single command? What does the same command report if you type it a second time?

:::loesung
`mkdir projekt/daten/roh` fails because `projekt` and `daten` are missing; Ubuntu 26.04 reports only `mkdir: No such file or directory`. `mkdir -p projekt/daten/roh` creates all three levels. A second `mkdir -p` with the same path reports nothing, because `-p` accepts existing directories. Only without `-p` would there be a message again:

```console
$ mkdir projekt/daten/roh
mkdir: No such file or directory
$ mkdir -p projekt/daten/roh
$ mkdir -p projekt/daten/roh
$ mkdir projekt/daten/roh
mkdir: projekt/daten/roh: File exists
```
:::
:::

:::aufgabe Exercise 15 ★★ A second playground
<span class="anker" id="aufg-15"></span>

In the practice directory, create the directory `verein` for a sports club with the subdirectories `mitglieder` and `termine`, and in it the empty files `mitglieder/liste.txt`, `termine/sommerfest.txt`, `beitraege.csv` and the hidden file `.einstellungen`. Then, in `verein`, compare the outputs of `ls`, `ls -a`, `ls -F` and `tree -a`. What does each one show, and what does it not show?

:::loesung
```console
$ mkdir -p verein/mitglieder verein/termine
$ cd verein
$ touch mitglieder/liste.txt termine/sommerfest.txt beitraege.csv .einstellungen
$ ls
beitraege.csv  mitglieder  termine
$ ls -a
.  ..  .einstellungen  beitraege.csv  mitglieder  termine
$ ls -F
beitraege.csv  mitglieder/  termine/
$ tree -a
.
├── .einstellungen
├── beitraege.csv
├── mitglieder
│   └── liste.txt
└── termine
    └── sommerfest.txt

3 directories, 4 files
$ cd ..
```

`ls` shows only the visible entries of the top level and does not reveal which ones are directories. `ls -a` additionally shows `.`, `..` and the hidden file. `ls -F` marks the two directories with `/`. Only `tree -a` shows all levels at once, including the hidden file and the files in the subdirectories.
:::
:::

:::aufgabe Exercise 16 ★★ The last line in nano
<span class="anker" id="aufg-16"></span>

Use nano to write a file `drei.txt` with the lines `eins`, `zwei`, `drei` (German for “one”, “two”, “three”) without pressing Enter after `drei`, and a file `vier.txt` with the same lines but with Enter after `drei`. Predict what `wc -l drei.txt vier.txt` reports, and check it. Afterward, delete both files with `rm drei.txt vier.txt`; the command `rm` removes the files named.

:::loesung
Prediction: `drei.txt` has three line ends, so 3 lines; nano added the last one itself. In `vier.txt`, `drei` is followed by the line end that the Enter key produced, and after it by an empty line, to which nano likewise appends a line end when saving: 4 lines, the last one empty.

```console
$ wc -l drei.txt vier.txt
 3 drei.txt
 4 vier.txt
 7 total
$ rm drei.txt vier.txt
```

`wc -l` counts line ends, and the empty line has one.
:::
:::

:::aufgabe Exercise 17 ★ touch on an existing file
<span class="anker" id="aufg-17"></span>

What does `touch einkauf.txt` change if the shopping list already contains four lines? What stays the same? Think first, then check with `ls -l` before and after and with `cat`.

:::loesung
For an existing file, `touch` changes only timestamps: the modification time and the access time jump to now, and with them the status change time. The contents, the size, the name, the owner and the permissions stay the same. Afterward, `ls -l` shows a new time with an unchanged size; `cat` shows the same four lines as before.
:::
:::

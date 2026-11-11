---
title: Files, directories and the directory tree
pfad: Computer Science / Linux and the Command Line / Files, Directories and Paths
adresse: informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade
knoten: Chapter 3: Files, Directories and Paths
order: 6080200
summary: Before you learn commands for files, you need a picture of what a file is and how Linux organizes many files.
tags: file, directory, directory tree, root directory, parent directory, subdirectory
lang: en
---

<span class="anker" id="stufe-1"></span>

:::zweck
Before you learn commands for files, you need a picture of what a file is and how Linux organizes many files. This section establishes three basic concepts: the file, the directory and the one tree in which all directories hang.
:::

:::::vorwissen What you need for this: shell, command and current folder

<span class="anker" id="stufe-1-1"></span>

This chapter assumes [Chapter 2](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/die-shell-erste-befehle.html). From it, you mainly need five things.

<ul>

<li>

The shell reads a command line and splits it into words at the spaces. The first word is the command, the others are arguments; arguments that begin with `-` are called options ([Chapter 2, Section 2](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/der-aufbau-einer-befehlszeile.html#stufe-2)).

</li>

<li>

The shell always works in a particular folder, the current folder. The prompt shows it, `cd` changes it, and `cd` without anything after it takes you to your home folder `/home/student`, which the prompt abbreviates as `~` ([Chapter 2, Section 1.4](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/terminal-und-shell.html#stufe-1-4)).

</li>

<li>

`cd` is a builtin command of the shell, because only the shell itself can change its own folder ([Chapter 2, Section 3.3](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/arten-von-befehlen.html#stufe-3-3)).

</li>

<li>

The pager `less` shows long text page by page; the Space bar pages forward, `q` quits it ([Chapter 2, Section 4.4](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/hilfe-finden.html#stufe-4-4)).

</li>

<li>

The Tab key completes commands and names that you have started to type ([Chapter 2, Section 5.1](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/schneller-arbeiten-vervollstandigung-verlauf-tastenkurzel.html#stufe-5-1)).

</li>

</ul>

In addition, you need one concept from computer science. A *byte* is the smallest unit in which a computer stores data: eight bits, that is, a whole number from 0 to 255 (in detail: [Python, Chapter 2, Section 3.3](/wissen/en/informatik/programmieren/python/werte-typen-und-variablen/zahlen-im-binarsystem.html#stufe-3-3)).

::::beispiel A quick test
Open a terminal and type `cat /etc/hostname`. The command `cat` shows the contents of whatever follows as an argument; [Chapter 2](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/die-shell-erste-befehle.html) already used it. The answer is the name of your computer, here `labor` (German for “lab”).

```console
$ cat /etc/hostname
labor
```
::::

⁠**In short:** You need the shell, the structure of a command line, the current folder with `cd`, the pager and the byte as a number from 0 to 255.

:::::

### The file

<span class="anker" id="stufe-1-2"></span>

A computer is supposed to keep things, even when it is switched off: a letter, a vacation photo, a program. This requires a unit that you can put away, find again and open.

**A row of numbers with a name.** You can picture a file as a strip of small boxes, each box holding a number from 0 to 255, with a name tag stuck on the strip. Figure [1](#abb-1) shows the file from the example above in this way: six boxes, with the letters that the numbers stand for below them.

:::abbildung linux/k3bytes 1
The file `/etc/hostname` as a sequence of six bytes. Each number stands for a character: 108 for `l`, 97 for `a` and so on; the 10 at the end marks the end of the line. The name tag is not part of the bytes.
:::

:::definition Definition 1.1 (File)
<span class="anker" id="satz-1-1"></span>

A __file__ is a sequence of bytes that is stored permanently under a name. What the bytes mean, whether text, image or program, is not determined by the system but by the program that reads the file.
:::

To the operating system, a file is therefore just a series of numbers with a length. Whether it contains a letter or a photo becomes apparent only to a program that interprets the numbers in its own way: a text editor turns them into characters, an image viewer into colored dots.

::::beispiel The bytes of a file
The command `od` (short for “octal dump”, output as numbers) shows the bytes of a file as numbers. The option `-An` omits the position information at the start of each line, and `-tu1` requests each byte individually as a decimal number:

```console
$ od -An -tu1 /etc/hostname
 108  97  98 111 114  10
```

The file consists of exactly six bytes. The first five are the characters `l`, `a`, `b`, `o`, `r`; each character is stored as a number, according to a fixed table. The 10 at the end is not a visible character but the character for “a line ends here”. `cat` sent the same six bytes to the terminal, and only the terminal turned them into the letters `labor` and a line break.
::::

⁠**In short:** A file is a stored sequence of bytes with a name; what the bytes mean is decided by the program that reads them.

:::hintergrund Why the system does not know what is in a file
An operating system could store files separately by kind, for example texts differently from images. Unix, the model for Linux, deliberately decided against this in the early 1970s: a file is just a sequence of bytes, without any structure that the system would have to know. The only task of the file system is to store the bytes permanently and to return exactly the same bytes the next time they are read. As a result, every program can handle every file: a program that counts or copies bytes works for letters, photos and programs alike, without understanding them. The price is paid by the program that reads the file: it has to recognize for itself what it is dealing with.
:::

### The directory

<span class="anker" id="stufe-1-3"></span>

A system with thousands of files needs order. In [Chapter 2](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/die-shell-erste-befehle.html), the means for this was called a folder. On Linux, the usual name is directory, and this name reveals how it works.

**A list of names.** At its core, a directory is a list, similar to a telephone directory: on the left is a name, on the right the reference to what belongs to it (a picture for orientation). Figure [2](#abb-2) shows the directory `/usr` as such a list. Each entry leads either to a file or to another directory, which is again a list.

:::abbildung linux/k3verzeichnis 2
A directory as a list of entries. Each entry links a name to what belongs to it; here each entry of `/usr` leads to another directory, and the entry `bin` in turn opens a list that includes the file `bash`.
:::

:::definition Definition 1.2 (Directory)
<span class="anker" id="satz-1-2"></span>

A __directory__ is a list of entries. Each entry links a name to a file or to another directory.
:::

“Directory” and “folder” mean the same thing; from now on, the chapter says directory. What [Chapter 2](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/die-shell-erste-befehle.html) called the current folder is therefore a directory. The name of an entry is also simply called a file name, even if it leads to a directory.

::::beispiel The entries of /usr
The command `ls` (short for “list”) shows the names that are entered in a directory:

```console
$ ls /usr
bin  games  include  lib  lib64  libexec  local  sbin  share  src
```

The directory `/usr` contains ten entries. This short list does not reveal whether they lead to files or to directories.
::::

⁠**In short:** A directory is a list that links names to files or to further directories.

### The directory tree and the root

<span class="anker" id="stufe-1-4"></span>

Because a directory can contain further directories, you get level upon level. So that every location can still be named unambiguously, this arrangement needs a fixed starting point.

**A tree that grows downward.** The directories are drawn like a family tree: at the top a single directory, below it the directories that it contains, below those their contents. Figure [3](#abb-3) builds up a section of this tree level by level.

:::abbildung linux/k3baum 3
The directory tree grows from top to bottom. At the very top is the root directory `/`; every other directory hangs from exactly one directory above it. Shown is a section with `/etc`, `/home/student`, `/tmp` and `/usr` with `bin`, `lib` and `share`. At the end, `/usr` is highlighted: one arrow up to `/`, three arrows down.
:::

:::definition Definition 1.3 (Directory tree, root directory)
<span class="anker" id="satz-1-3"></span>

The directories of a Linux system form a single __directory tree__: every directory except one is entered under its name in exactly one other directory. The one directory that is not entered in any other is called the __root directory__; it is written as a single slash `/`.
:::

Two words for positions in the tree come up all the time. The directory in which another one is entered is called its __parent directory__. Conversely, every directory that is entered in another one is a __subdirectory__ of it. Thus `/usr` is the parent directory of `/usr/bin`, and `/usr/bin` is a subdirectory of `/usr`. At the end of Figure [3](#abb-3), the arrow up points to the parent directory of `/usr` and the arrows down point to its subdirectories: every directory except the root has exactly one parent directory but any number of subdirectories.

**No drive letters.** Windows gives each drive a tree of its own with its own beginning, `C:\` or `D:\`. Linux has exactly one tree, no matter how many storage devices are connected. Another storage device does not get a letter; instead, it is mounted on a directory of the tree, and its contents then appear below this directory ([Chapter 1, Section 8.1](/wissen/en/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/das-live-system.html#stufe-8-1)). This is how, under WSL 2, the Windows drive C: appears under `/mnt/c` ([Chapter 1, Section 4.5](/wissen/en/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/wsl-2-linux-neben-windows.html#stufe-4-5)). Figure [4](#abb-4) puts the two arrangements side by side.

:::abbildung linux/k3laufwerke 4
Left, Windows: two drives, two trees, each with its own letter. Right, Linux under WSL 2: a single tree with the root `/`; drive C: hangs as a subtree under `/mnt/c`.
:::

::::beispiel The top level
`ls /` shows the entries of the root directory:

```console
$ ls /
bin   dev  home  lib    lost+found  mnt  proc  run   snap  sys  usr
boot  etc  init  lib64  media       opt  root  sbin  srv   tmp  var
```

These are all the directories of the top level; every file of the system is stored somewhere below them. No entry is called C: or D:. The entry `init` exists only under WSL.
::::

⁠**In short:** All directories hang in a single tree with the root `/`; further storage devices are mounted instead of getting a letter.

:::hintergrund Why Linux has a single tree
Unix introduced the single tree back in the 1970s, and Linux adopted it. The advantage: a location in the tree always has the same name, regardless of which storage device it happens to be on. A program that looks for its configuration in `/etc` does not need to know whether `/etc` is on the first or the second hard disk; the system administrator can move a subtree to a larger storage device without a single name changing. With drive letters, the storage device would be part of every name, and a move would invalidate every reference that contains it. Windows inherited its letters from MS-DOS, from the days of the floppy disk drives A: and B:. Incidentally, Windows can also attach a storage device to a folder instead of a letter, but this is not common there.
:::

### Exercises for Section [1](#stufe-1)

<span class="anker" id="stufe-1-5"></span>

:::aufgabe Exercise 1 ★ File, directory or neither?
<span class="anker" id="aufg-1"></span>

Classify each of the following: (a) a vacation photo, (b) the list of names in `/usr`, (c) the root directory, (d) the name `hostname`, (e) the program `bash`, (f) drive C: on Windows. Justify each answer in one sentence.

:::loesung
(a) A file: the photo is a stored sequence of bytes with a name; only an image viewer turns the bytes into colored dots.

(b) A directory, more precisely its contents: the list of names with their references is exactly what makes up a directory.

(c) A directory, namely the only one that is not entered in any other.

(d) Neither: `hostname` is a name, that is, an entry in the directory `/etc`. It leads to a file but is not the file itself.

(e) A file: a program is a sequence of bytes that the processor can execute as instructions.

(f) Neither: on Windows, C: is a drive with a tree of its own. Linux has nothing of the kind; under WSL 2, the drive appears as a subtree under the directory `/mnt/c`.
:::
:::

:::aufgabe Exercise 2 ★★ Predicting bytes
<span class="anker" id="aufg-2"></span>

The file `/etc/timezone` names the time zone of your computer; on the test computer, it is `Europe/Berlin`. (a) Show its contents with `cat`. (b) Predict how many bytes it consists of and which byte is at the end. (c) Check with `od -An -tu1 /etc/timezone`. Which number belongs to the slash?

:::loesung
(a) `cat /etc/timezone` shows `Europe/Berlin`. (b) `Europe/Berlin` has 13 characters, each one byte; the line end comes on top of that. Prediction: 14 bytes, and the last one is 10. (c) The check:

```console
$ od -An -tu1 /etc/timezone
  69 117 114 111 112 101  47  66 101 114 108 105 110  10
```

14 numbers, and the last one is 10. The slash is in seventh place, between `Europe` and `Berlin`; it is the 47. If your computer has a different time zone, count its characters and add 1.
:::
:::

:::aufgabe Exercise 3 ★ Drawing a piece of the tree
<span class="anker" id="aufg-3"></span>

Run `ls /`, `ls /usr` and `ls /home` and use the results to draw a section of the directory tree with three levels. Mark the root directory, a parent directory and one of its subdirectories.

:::loesung
A possible section with three levels, indented instead of drawn:

```text
/                  <- root directory
    home
        student
    usr            <- parent directory of bin
        bin        <- subdirectory of usr
        share
        lib
    etc
    tmp
```

In the drawing, `/` is at the top, and each directory hangs from exactly one directory above it. `/usr` is the parent directory of `/usr/bin`, and `/usr/bin` is a subdirectory of `/usr`. Likewise, `/home` is the parent directory of `/home/student`.
:::
:::

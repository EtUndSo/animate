---
title: The working directory and paths
pfad: Computer Science / Linux and the Command Line / Files, Directories and Paths
adresse: informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade
knoten: Chapter 3: Files, Directories and Paths
order: 6080300
summary: There is no mouse in the terminal to point at a file.
tags: working directory, path, absolute path, relative path, home directory, tilde, cd
lang: en
---

<span class="anker" id="stufe-2"></span>

:::zweck
There is no mouse in the terminal to point at a file. You name a file by writing down its route through the tree. This section shows where you currently are, how to write down such routes, from the top of the tree or from your own location, and how to move around with `cd`.
:::

### The working directory

<span class="anker" id="stufe-2-1"></span>

Anyone moving around a large building has to know where they are standing before they can describe a route. The same is true in the directory tree.

**A location in the tree.** You can imagine that you are standing in exactly one directory of the tree. From there, you see the entries of this directory, the way up to the parent directory and the ways down into the subdirectories. Figure [5](#abb-5) marks this location and shows how it moves when you change directories.

:::abbildung linux/k3arbeitsverzeichnis 5
The working directory as a location in the tree. At first, the marker is in `/home/student`; after `cd /usr/bin`, it jumps to `/usr/bin`, and each time `pwd` names the route from the root to the marker.
:::

:::definition Definition 2.1 (Working directory)
<span class="anker" id="satz-2-1"></span>

The __working directory__ of a running program is the directory in which it is currently working. If you do not give a command a location, it refers to this directory.
:::

For the shell, the working directory is exactly the current folder from [Chapter 2, Section 1.4](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/terminal-und-shell.html#stufe-1-4). Every running program has a working directory of its own; that is why two terminal windows can be in different directories. The command `pwd` (short for “print working directory”) prints the shell's working directory.

::::beispiel Where am I?
A freshly opened terminal is in your personal directory. This time, the box shows the full prompt so that you can see how it moves along:

```text
student@labor:~$ pwd
/home/student
student@labor:~$ cd /usr/bin
student@labor:/usr/bin$ pwd
/usr/bin
```

`pwd` prints the full route; the prompt shows the same, except that it abbreviates `/home/student` as `~`.
::::

⁠**In short:** The working directory is the location in the tree to which commands without a location refer; `pwd` names it.

### The path

<span class="anker" id="stufe-2-2"></span>

To name a file that is not in the working directory, you have to describe the route to it. There is a concise notation for this.

**Directions made of names.** A route through the tree is a sequence of branches: first into this directory, then into that one, then to the file. You write the names one after another and separate them with slashes. Figure [6](#abb-6) reads the path `/usr/bin/bash` step by step.

:::abbildung linux/k3pfad 6
The path `/usr/bin/bash`, read step by step: from the root directory into the entry `usr`, from there into the entry `bin`, and there to the entry `bash`. Each slash is a branch.
:::

:::definition Definition 2.2 (Path)
<span class="anker" id="satz-2-2"></span>

A __path__ is a sequence of names, separated by slashes `/`, that describes the route through the directory tree to a file or a directory. Every name except the last must denote a directory.
:::

The slash thus has two tasks: at the beginning of a path, it stands for the root directory; between two names, it separates them. Windows uses the backslash `\` as the separator; on Linux, that is a completely different character.

::::beispiel Reading a path
The path `/usr/share/doc` means: start in the root directory, go into its entry `usr`, in there into the entry `share` and in there into the entry `doc`. `usr` and `share` must be directories, otherwise the route could not continue; `doc` is the destination and here also a directory.
::::

⁠**In short:** A path is a set of directions through the tree: names, separated by slashes.

### The absolute path

<span class="anker" id="stufe-2-3"></span>

Some directions are meant to work everywhere, no matter where you currently are, like a complete postal address with street, house number and town.

:::definition Definition 2.3 (Absolute path)
<span class="anker" id="satz-2-3"></span>

An __absolute path__ begins with `/`. It describes the route from the root directory and therefore denotes the same location from every working directory.
:::

`/etc/hostname`, `/usr/bin` and `/home/student` are absolute paths. `pwd` always prints an absolute path, because only an absolute path states unambiguously where you are.

::::beispiel The same location from two places
`cat /etc/timezone` shows the computer's time zone. The absolute path leads to the same file from every working directory:

```text
student@labor:~$ cat /etc/timezone
Europe/Berlin
student@labor:~$ cd /usr/share
student@labor:/usr/share$ cat /etc/timezone
Europe/Berlin
```
::::

⁠**In short:** An absolute path begins with `/` and is valid from everywhere.

### The relative path

<span class="anker" id="stufe-2-4"></span>

Absolute paths get long when you work deep in the tree. Directions from your own location are often shorter, like “second door on the left” in a building that you have already entered.

:::abbildung linux/k3absolutrelativ 7
Two routes to the same file `/usr/bin/bash`. The absolute path starts at the root. The relative path `bin/bash` starts in the working directory `/usr`; from the working directory `/home/student`, the same relative path leads nowhere.
:::

:::definition Definition 2.4 (Relative path)
<span class="anker" id="satz-2-4"></span>

A __relative path__ does not begin with `/`. It describes the route from the working directory; which location it denotes therefore depends on where you currently are.
:::

A single name such as `bash` is the shortest relative path: the entry `bash` in the working directory. Figure [7](#abb-7) shows how the same relative path leads to different results from two locations.

::::beispiel The same relative path, two locations
```text
student@labor:~$ cd /usr
student@labor:/usr$ ls bin/bash
bin/bash
student@labor:/usr$ cd
student@labor:~$ ls bin/bash
ls: cannot access 'bin/bash': No such file or directory
```

In `/usr`, `bin/bash` leads to the file `/usr/bin/bash`; `ls` confirms this by repeating the name. In `/home/student`, there is no entry `bin`, so `ls` finds nothing and reports “No such file or directory”.
::::

⁠**In short:** A relative path begins without `/` and is valid from the working directory.

### The special names . and ..

<span class="anker" id="stufe-2-5"></span>

With relative paths, you can only go down, into subdirectories. To get up, you need a name for the parent directory, and sometimes one for the directory you are standing in.

:::definition Definition 2.5 (The entries . and ..)
<span class="anker" id="satz-2-5"></span>

Every directory contains two special entries: `.` (one dot) denotes the directory itself, `..` (two dots) its parent directory. In the root directory, `..` denotes the root directory itself.
:::

In a path, `..` works like any other name: `../..` means “two levels up”, `../share` means “one level up and then into `share`”. The single dot seems superfluous, because `./bin` and `bin` mean the same thing. However, it is needed when a command insists on a directory as an argument and the working directory is meant. Figure [8](#abb-8) follows a series of steps upward.

:::abbildung linux/k3punkte 8
Steps up with `..`: from `/usr/share/doc` one level up to `/usr/share`, with `../..` two levels up to the root. Another step `..` stays in `/`: there is nothing above the root.
:::

::::beispiel Upward until you can go no further
```text
student@labor:~$ cd /usr/share/doc
student@labor:/usr/share/doc$ cd ..
student@labor:/usr/share$ pwd
/usr/share
student@labor:/usr/share$ cd ../..
student@labor:/$ pwd
/
student@labor:/$ cd ..
student@labor:/$ pwd
/
```

The last `cd ..` reports no error; it simply stays in the root directory.
::::

⁠**In short:** `.` is the directory itself, `..` the parent directory; in the root, `..` leads back to the root.

:::hintergrund How a path is resolved step by step
Translating a path into a file is the kernel's task, not the shell's. Every program that wants to open a file passes the path to the kernel with a system call ([Chapter 1, Section 1.4](/wissen/en/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/betriebssystem-kernel-und-distribution.html#stufe-1-4)), and the kernel goes through it name by name. If the path begins with `/`, the kernel starts in the root directory, otherwise in the program's working directory. Then it looks up each name in the directory reached so far. If a name is missing, the route fails with the message “No such file or directory”. If a name that is not the last one is not a directory at all, the route fails with “Not a directory”, because you cannot look up another name in a regular file:

```console
$ ls /etc/hostname/x
ls: cannot access '/etc/hostname/x': Not a directory
```

The names `.` and `..` always have their fixed meaning, regardless of how a file system stores them. Because all programs go through this one mechanism, all programs understand paths in the same way: `ls`, `cat` and every text editor.
:::

### The home directory and the tilde

<span class="anker" id="stufe-2-6"></span>

Every person who uses a computer needs a place of their own for their files, just as every roommate has a room of their own. Because you need this place all the time, it has an abbreviation.

:::definition Definition 2.6 (Home directory)
<span class="anker" id="satz-2-6"></span>

A user's __home directory__ is the directory that belongs to them for their own files. On Linux, it is usually `/home/<name>`, so for the user `student`, it is `/home/student`.
:::

The home directory is the home folder from [Chapter 2](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/die-shell-erste-befehle.html); a new terminal starts in it. As an ordinary user, you may essentially create and change files only there; you may read most of the system's directories, but not change them. The abbreviation for it is the __tilde__ `~`: if it is at the beginning of a word, the shell replaces it with the path of your home directory before it starts the command. That is why it works with every command. `~/fotos` then means `/home/student/fotos`, and `~root` means “the home directory of the user `root`”. In the middle of a word, the tilde remains an ordinary character.

::::beispiel What the shell makes of the tilde
The command `echo` simply prints its arguments ([Chapter 2, Section 2.3](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/der-aufbau-einer-befehlszeile.html#stufe-2-3)). It therefore shows what the shell made of the tilde before `echo` started:

```console
$ echo ~ ~/fotos ~root
/home/student /home/student/fotos /root
```

The directory `/home/student/fotos` does not have to exist for this; the shell only replaces text. The home directory of `root` is not under `/home`; it is `/root`.
::::

⁠**In short:** The home directory is your own place in the tree; `~` at the beginning of a word stands for its path.

### Changing the directory: cd

<span class="anker" id="stufe-2-7"></span>

With paths, you can now describe any location. To work there without writing out the path every time, you change the working directory.

:::definition Definition 2.7 (cd)
<span class="anker" id="satz-2-7"></span>

The builtin command __cd__ (short for “change directory”) makes the directory that its argument denotes the shell's new working directory. Without an argument, it changes to the home directory; with the argument `-`, it changes back to the previous working directory.
:::

The argument may be an absolute or a relative path. On success, `cd` prints nothing; the new prompt shows the new location. Only `cd -` states where it has changed to, to be on the safe side. Figure [5](#abb-5) already shows how the marker of the working directory jumps.

::::beispiel Back and forth
```text
student@labor:~$ cd /etc
student@labor:/etc$ cd -
/home/student
student@labor:~$ cd -
/etc
student@labor:/etc$ cd ~
student@labor:~$ cd /etc/hostname
bash: cd: /etc/hostname: Not a directory
student@labor:~$ cd Etc
bash: cd: Etc: No such file or directory
```

`cd -` switches back and forth between the last two locations. The last two attempts fail: `/etc/hostname` is a file, not a directory, and `Etc` does not exist in the home directory. The message begins with `bash: cd:` because the shell itself runs the command.
::::

⁠**In short:** `cd` changes the working directory: `cd path` goes there, `cd` goes home, `cd -` goes back, `cd ..` goes one level up.

### Exercises for Section [2](#stufe-2)

<span class="anker" id="stufe-2-8"></span>

:::aufgabe Exercise 4 ★ Predicting paths
<span class="anker" id="aufg-4"></span>

Your working directory is `/usr/share/doc`. Which absolute path does each of the following paths denote? (a) `..` (b) `../..` (c) `~/x` (d) `/etc` (e) `../../../../etc` (f) `./bash` (g) `../doc/../man`. Check (e) and (g) on the computer with `cd` and `pwd`.

:::loesung
The starting point is `/usr/share/doc`.

<ol class="al">

<li>

`..` is one level up: `/usr/share`.

</li>

<li>

`../..` is two levels up: `/usr`.

</li>

<li>

`~/x` does not depend on the working directory, because the shell replaces the tilde with the home directory: `/home/student/x`. Whether `x` exists does not matter for the path.

</li>

<li>

`/etc` is absolute and stays `/etc`.

</li>

<li>

Step by step: `..` leads to `/usr/share`, the second `..` to `/usr`, the third to `/`, and the fourth stays in `/`, because there is nothing above the root; then comes `etc`. Result: `/etc`.

</li>

<li>

`./bash` is the entry `bash` in the working directory: `/usr/share/doc/bash`.

</li>

<li>

`..` leads to `/usr/share`, `doc` back to `/usr/share/doc`, `..` back to `/usr/share` and `man` to `/usr/share/man`.

</li>

</ol>

The check for (e) and (g):

```text
student@labor:~/linuxk3$ cd /usr/share/doc
student@labor:/usr/share/doc$ cd ../../../../etc
student@labor:/etc$ pwd
/etc
student@labor:/etc$ cd /usr/share/doc
student@labor:/usr/share/doc$ cd ../doc/../man
student@labor:/usr/share/man$ pwd
/usr/share/man
```
:::
:::

:::aufgabe Exercise 5 ★★ Converting between absolute and relative
<span class="anker" id="aufg-5"></span>

(a) Your working directory is `/usr`. Write the absolute path `/usr/share/man` as the shortest possible relative path. (b) Your working directory is `/usr/share/man`. Write `/usr/bin` as a relative path. (c) Your working directory is `/home/student`. When is the absolute path `/etc/hosts` shorter than any relative one?

:::loesung
(a) From `/usr`, `share/man` leads to the target; it cannot be any shorter.

(b) From `/usr/share/man`, you have to go two levels up to `/usr` and then down into `bin`: `../../bin`.

(c) From `/home/student`, the relative route is `../../etc/hosts`, two levels up to the root and then down; that is 15 characters against 10 for `/etc/hosts`. In general, the absolute path is shorter when the working directory and the target meet only high up in the tree, so that the relative route needs many `..`. If the target is below the working directory, the relative path is almost always shorter.
:::
:::

:::aufgabe Exercise 6 ★★ Error messages from cd
<span class="anker" id="aufg-6"></span>

Explain each message: (a) `cd /ETC` reports “No such file or directory”, (b) `cd ~root` reports “Permission denied”, (c) `cd /etc/hostname` reports “Not a directory”. Which of the three messages comes from a missing entry, which from an entry of the wrong kind and which from a prohibition?

:::loesung
```text
student@labor:~/linuxk3$ cd /ETC
bash: cd: /ETC: No such file or directory
student@labor:~/linuxk3$ cd ~root
bash: cd: /root: Permission denied
```

(a) A missing entry: `/` contains `etc` but not `ETC`, and Linux distinguishes between uppercase and lowercase letters. (b) A prohibition: the shell replaced `~root` with `/root`, as the message shows. The directory exists, but the user `student` may not enter it; `ls /root` showed the same message in subsection [7.4](die-verzeichnisstruktur-von-linux.html#stufe-7-4). (c) An entry of the wrong kind: `/etc/hostname` exists, but it is a file, and you cannot change into a file (example in subsection [2.7](#stufe-2-7)).
:::
:::

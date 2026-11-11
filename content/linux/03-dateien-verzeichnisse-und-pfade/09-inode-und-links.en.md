---
title: Inodes and links
pfad: Computer Science / Linux and the Command Line / Files, Directories and Paths
adresse: informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade
knoten: Chapter 3: Files, Directories and Paths
order: 6080900
summary: So far, a file name was simply the name of a file.
tags: inode, hard link, link count, symbolic link, usr-merge
lang: en
---

<span class="anker" id="stufe-8"></span>

:::zweck
So far, a file name was simply the name of a file. This section looks underneath: the name and the file are two different things, connected only by an entry in the directory. From this follows why a file can have several names, why `rm` knows no trash and why there are two kinds of references to files.
:::

### The inode

<span class="anker" id="stufe-8-1"></span>

A file has more properties than its contents: an owner, a size, timestamps, permissions. This information has to be stored somewhere, and it turns out that the name is not part of it.

:::abbildung linux/k3inode 29
The route from a name to the data. The entry `einkauf.txt` in the directory contains only a number. Under this number, the file system finds the inode with all the information about the file, and the inode points to the blocks of the storage device in which the contents are stored.
:::

:::definition Definition 8.1 (Inode)
<span class="anker" id="satz-8-1"></span>

An __inode__ is the administrative record of a file in the file system. It contains all the information about the file except its name: type, permissions, owner and group, size, timestamps, the number of its names and the location of the blocks in which the contents are stored. Each inode has a number, the inode number, which is unique within a file system.
:::

Figure [29](#abb-29) shows the three stages: name, inode, data. Directories also have an inode, and so do device files. The option `-i` makes `ls` put the inode number in front of each name. The command `stat` shows what is in the inode.

::::beispiel The inode of the shopping list
```console
$ ls -i einkauf.txt
95361 einkauf.txt
$ stat einkauf.txt
  File: einkauf.txt
  size: 25              Blocks: 8          IO Block: 4096   regular file
Device: 8,48    Inode: 95361       Links: 1
Access: (0644/-rw-r--r--)  Uid: ( 1000/ student)   Gid: ( 1000/ student)
Access: 2026-11-10 02:41:57.014971387 +0100
Modify: 2026-11-10 02:41:56.714971764 +0100
Change: 2026-11-10 02:41:56.714971764 +0100
 Birth: 2026-11-10 02:41:54.890987095 +0100
```

The shopping list has the inode 95361. `stat` reads from it: 25 bytes, stored in blocks, a regular file; `Links: 1` means that it has one name; the permissions as a number and as characters; owner and group with their IDs from [Chapter 2, Section 6.2](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/das-system-erkunden.html#stufe-6-2); and the four timestamps from the background box in subsection [5.2](dateien-und-verzeichnisse-anlegen.html#stufe-5-2). `Device: 8,48` is the storage device, the same two numbers as for `/dev/sdd`. The GNU implementation of `stat` writes `Size` with a capital S; the lowercase s is a quirk of uutils version 0.8 in Ubuntu 26.04, and otherwise both outputs look the same.
::::

⁠**In short:** The inode is the administrative record of a file with all the information except the name; `ls -i` shows its number, `stat` its contents.

:::hintergrund Where the name inode comes from
The word goes back to the first description of Unix, which Dennis Ritchie and Ken Thompson published in 1974. There, a directory entry is nothing but a name and a number, the “i-number”, short for index number. The number is an index into a table at a fixed location on the storage device, and the entry in this table that describes the file is called the “i-node”. The authors themselves called this table an unusual feature of their system. Today's file systems such as ext4 store inodes more cleverly, but the idea has remained: the file is managed via a number, and the name is only a signpost to this number.
:::

### The directory as a table

<span class="anker" id="stufe-8-2"></span>

Subsection [1.3](dateien-verzeichnisse-und-der-verzeichnisbaum.html#stufe-1-3) described the directory as a list that connects names with files. With the inode, you can say exactly what this connection consists of.

:::abbildung linux/k3tabelle 30
The directory `rezepte` as a table with two columns, name and inode number. The entry `.` carries `rezepte`'s own number, the entry `..` the number of the parent directory, `kuchen` and `suppen` the numbers of these subdirectories. Arrows lead from each number to the matching inode.
:::

:::satz Theorem 8.2 (Directory entry)
<span class="anker" id="satz-8-2"></span>

An entry in a directory consists of a name and an inode number. The size, the owner and all other information are in the inode to which the number points.
:::

Many file systems, ext4 among them, also store the type in the entry, file or directory, so that programs learn it faster; the inode remains authoritative. A file name is therefore not a property of the file, but an entry in a table that points to it. The names `.` and `..` are such entries as well: `.` points to the inode of the directory itself, `..` to that of the parent directory. Figure [30](#abb-30) draws a directory as a table.

::::beispiel Comparing numbers
```console
$ ls -ai rezepte
95355 .  95352 ..  95359 kuchen  95360 suppen
$ ls -id rezepte rezepte/kuchen rezepte/suppen
95355 rezepte  95359 rezepte/kuchen  95360 rezepte/suppen
$ ls -ai rezepte/kuchen
95359 .  95355 ..  95362 apfelkuchen.txt  95363 kaesekuchen.txt
```

In `rezepte`, `.` carries the number 95355, the same as `rezepte` itself. In `rezepte/kuchen`, `..` carries the number 95355: it points back to `rezepte`. The special names from subsection [2.5](das-arbeitsverzeichnis-und-pfade.html#stufe-2-5) are therefore ordinary entries with a matching number.
::::

⁠**In short:** A directory is a table of names and inode numbers; a file name is only an entry that points to an inode.

:::hintergrund Why ls -l has more work to do than ls
Because a directory essentially contains only names and numbers, `ls` without options can read the names directly from the table. For `ls -l`, that is not enough: the size, owner and time are in the inodes, so `ls` must additionally query the inode of each entry. In a directory with a hundred thousand files, you notice the difference. The resolution of a path from subsection [2.5](das-arbeitsverzeichnis-und-pfade.html#stufe-2-5) can now also be described exactly: the kernel reads the entry `usr` in the root directory and receives an inode number, reads in this inode where the table of `usr` is located, looks up the next name in it, and so on up to the last one. Without looking anything up, it knows only two inodes: that of the root directory and that of the working directory. Every resolution starts there.
:::

### The hard link

<span class="anker" id="stufe-8-3"></span>

If a name is only an entry that points to an inode, a question suggests itself: can two entries point to the same inode? They can, and this has useful consequences.

:::abbildung linux/k3hartlink 31
A second name for the same file. `ln einkauf.txt liste.txt` creates a second entry that points to the same inode, and the count of names in the inode jumps from 1 to 2. After `rm einkauf.txt`, only the first entry is gone; the count drops to 1, and the data stay.
:::

:::definition Definition 8.3 (Hard link, link count)
<span class="anker" id="satz-8-3"></span>

A __hard link__ is a further directory entry for an existing inode, that is, an additional name for the same file. The command `ln target name` creates it. The inode keeps count of how many entries point to it; this number is called the __link count__.
:::

After `ln`, there is no longer any difference between the old and the new name: both are entries with equal rights, and neither is the “original”. If you change the file through one name, you see the change through the other, because it is the same inode with the same data blocks. Now you can also read the number in the second column of `ls -l` that subsection [3.4](den-inhalt-eines-verzeichnisses-anzeigen.html#stufe-3-4) left open: it is the link count.

::::beispiel Two names, one list
```console
$ ln einkauf.txt liste.txt
$ ls -li einkauf.txt liste.txt
95361 -rw-r--r-- 2 student student 25 Nov 10 02:41 einkauf.txt
95361 -rw-r--r-- 2 student student 25 Nov 10 02:41 liste.txt
```

Both names carry the inode number 95361 and the link count 2. Now open `nano liste.txt`, append the line `Butter` and save. Then the other name shows the new contents:

```console
$ cat einkauf.txt
Milch
Brot
Äpfel
Kaffee
Butter
```
::::

**The link count of a directory.** A directory always has at least two names: its entry in the parent directory and its own entry `.`. In addition, each of its subdirectories has an entry `..` that also points to it. The link count of a directory is therefore 2 plus the number of its subdirectories:

```console
$ ls -ld rezepte rezepte/kuchen
drwxr-xr-x 4 student student 4096 Nov 10 02:42 rezepte
drwxr-xr-x 2 student student 4096 Nov 10 02:41 rezepte/kuchen
```

`rezepte` has two subdirectories, so $2 + 2 = 4$; `kuchen` has none, so 2. The `/etc` of the test computer with the count 93 from subsection [3.4](den-inhalt-eines-verzeichnisses-anzeigen.html#stufe-3-4) therefore has 91 subdirectories.

⁠**In short:** A hard link is a second name for the same inode; the link count in the second column of `ls -l` counts the names.

### Deleting means removing a name

<span class="anker" id="stufe-8-4"></span>

If a file has two names with equal rights, what does `rm` delete? The answer also explains why there is no trash on the command line.

:::satz Theorem 8.4 (Deleting)
<span class="anker" id="satz-8-4"></span>

`rm` removes only the named directory entry and decreases the link count of the inode by 1. Only when the count is 0 and no running program still has the file open does the file system free the inode and its data blocks.
:::

As long as a name is left, the file is therefore not deleted, just one name poorer. Figure [31](#abb-31) shows this at the end of its animation.

::::beispiel Deleting the first name
```console
$ rm einkauf.txt
$ ls -li liste.txt
95361 -rw-r--r-- 1 student student 32 Nov 10 02:42 liste.txt
$ cat liste.txt
Milch
Brot
Äpfel
Kaffee
Butter
```

The name `einkauf.txt` is gone, while the list is completely there under `liste.txt`; the link count has dropped to 1. The size is now 32 bytes, because `Butter` with its line end added seven bytes.
::::

**mv keeps the inode.** `mv`, too, works only with entries, as the background box in subsection [6.3](kopieren-verschieben-loschen.html#stufe-6-3) said. The inode number confirms this:

```console
$ ls -i liste.txt
95361 liste.txt
$ mv liste.txt einkauf.txt
$ ls -i einkauf.txt
95361 einkauf.txt
```

The file is called `einkauf.txt` again and is the same inode as before; not a single byte of its contents was moved.

⁠**In short:** `rm` removes a name; the file disappears only with its last name.

:::hintergrund Why rm has no trash
The system call behind `rm` is not called “delete” but `unlink`: removing a link. You can check this yourself. The tool `strace` shows the system calls of a program; with `-e trace=`, you limit the display to particular ones:

```console
$ touch muell.txt
$ strace -e trace=unlink,unlinkat rm muell.txt
unlinkat(AT_FDCWD, "muell.txt", 0)      = 0
+++ exited with 0 +++
```

`rm` calls `unlinkat` exactly once, the present-day form of `unlink`, and the result 0 means success. The kernel removes the entry and counts the link count down; if it is at 0, the file system marks the inode and the blocks as free. An intermediate step “into the trash” does not exist at this level, and this is exactly the level that `rm` uses. Incidentally, the bytes are not overwritten in the process, only released for reuse. That is why remnants of deleted files can sometimes be recovered; you cannot rely on it, though, because the space is reused at the next opportunity. The exception for open files has a practical reason: a program that is currently reading from a file should not suddenly grasp at nothing in the middle of reading. The data remain until it closes the file.
:::

### The symbolic link

<span class="anker" id="stufe-8-5"></span>

A hard link is a full-fledged name. In everyday use, you often need something else: a signpost that points to a file or a directory without being the file itself, similar to a shortcut on Windows.

:::abbildung linux/k3symlink 32
A symbolic link is a small file of its own that contains a path. `zettel.txt` (German for “note”) contains the text `einkauf.txt`; whoever opens `zettel.txt` is redirected to `einkauf.txt`. If the target disappears, the path is still in the link, but it leads nowhere.
:::

:::definition Definition 8.5 (Symbolic link)
<span class="anker" id="satz-8-5"></span>

A __symbolic link__ is a file of its own of type `l` whose only contents are a path. Almost every access to the link is redirected to the location that this path denotes. The command `ln -s target name` creates it.
:::

A relative path in the link is resolved from the link's directory, not from the working directory of whoever creates it. The target does not have to exist; then the link leads nowhere, and it is called dangling. `ls -l` shows the link with `l` in the first column and the path after an arrow `->`; its size is the length of this path in bytes. `ls -F` appends an `@` to its name. `rm` deletes the link itself, never its target.

::::beispiel A signpost to the shopping list
```console
$ ln -s einkauf.txt zettel.txt
$ ls -li einkauf.txt zettel.txt
95361 -rw-r--r-- 1 student student 32 Nov 10 02:42 einkauf.txt
95257 lrwxrwxrwx 1 student student 11 Nov 10 02:42 zettel.txt -> einkauf.txt
$ cat zettel.txt
Milch
Brot
Äpfel
Kaffee
Butter
$ ls -F
einkauf.txt  fotos/  rezepte/  zettel.txt@
```

The link has an inode of its own, 95257, and is 11 bytes in size, as long as the text `einkauf.txt`. The link count of the shopping list stays 1: a symbolic link is not a further name of the file. `cat` reads the list through the link.
::::

::::beispiel [Second example] A relative path in the wrong place
The same link is now to be placed in `rezepte`:

```console
$ ln -s einkauf.txt rezepte/zettel.txt
$ cat rezepte/zettel.txt
cat: rezepte/zettel.txt: No such file or directory
$ ls -l rezepte/zettel.txt
lrwxrwxrwx 1 student student 11 Nov 10 02:42 rezepte/zettel.txt -> einkauf.txt
$ rm rezepte/zettel.txt
$ ln -s ../einkauf.txt rezepte/zettel.txt
$ cat rezepte/zettel.txt
Milch
Brot
Äpfel
Kaffee
Butter
```

The first link contains `einkauf.txt` and therefore looks for the file in `rezepte`, where it does not exist; `ln` did not check this. The second contains `../einkauf.txt`, one level up from the location of the link, and works.
::::

::::beispiel [Third example] A dangling link and a link to a directory
```console
$ touch entwurf.txt
$ ln -s entwurf.txt aktuell.txt
$ rm entwurf.txt
$ ls -l aktuell.txt
lrwxrwxrwx 1 student student 11 Nov 10 02:42 aktuell.txt -> entwurf.txt
$ cat aktuell.txt
cat: aktuell.txt: No such file or directory
```

(`entwurf` is German for “draft”, `aktuell` for “current”.) After the target has been deleted, the link is still there unchanged and points nowhere. A link to a directory is more useful, for example to the photo directory of the current year:

```console
$ ln -s fotos/urlaub/2026 urlaub
$ ls urlaub
berge  notiz.txt  strand_1.jpg  strand_10.jpg  strand_2.jpg
$ ls -l urlaub
lrwxrwxrwx 1 student student 17 Nov 10 02:42 urlaub -> fotos/urlaub/2026
```

Next year, you delete the link and create it anew, pointing to `fotos/urlaub/2027`; everything that works through `urlaub` then ends up in the new year.
::::

⁠**In short:** A symbolic link is a small file with a path in it; it redirects accesses and can point nowhere if the target is missing.

### A symbolic link in the system: /bin

<span class="anker" id="stufe-8-6"></span>

[Chapter 2, Section 3.3](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/arten-von-befehlen.html#stufe-3-3) said that on Ubuntu, `/bin` is only a second name for `/usr/bin`. Now you can say exactly what kind of name that is; Figure [33](#abb-33) shows the step from earlier to today.

:::abbildung linux/k3usrmerge 33
The merging of `/bin` with `/usr/bin`. Earlier, two directories, each with its own programs; today, `/bin` is a symbolic link with the contents `usr/bin`, and every path through `/bin` ends in the same directory. Likewise `/sbin` and `/lib`.
:::

:::definition Definition 8.6 (usr-merge)
<span class="anker" id="satz-8-6"></span>

The __usr-merge__, the merging of `/usr`, is the arrangement common today in which the directories `/bin`, `/sbin` and `/lib` are symbolic links to `usr/bin`, `usr/sbin` and `usr/lib`. All programs and libraries are then located under `/usr`.
:::

The links remain so that old paths such as `/bin/bash`, which appear in countless programs and instructions, keep working. Fedora introduced the merge in 2012, Debian has required it since version 12, released in 2023, and Ubuntu 26.04 has it as well. The FHS of 2015 still describes separate directories.

::::beispiel Checking the links
```console
$ ls -ld /bin /sbin /lib
lrwxrwxrwx 1 root root 7 Apr 20  2026 /bin -> usr/bin
lrwxrwxrwx 1 root root 7 Apr 20  2026 /lib -> usr/lib
lrwxrwxrwx 1 root root 8 Apr 20  2026 /sbin -> usr/sbin
$ ls -l /etc/os-release
lrwxrwxrwx 1 root root 21 Aug 24 12:33 /etc/os-release -> ../usr/lib/os-release
```

The links contain relative paths: `usr/bin` is resolved from the location of the link, that is, from `/`, and leads to `/usr/bin`. `/etc/os-release`, which [Chapter 2](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/die-shell-erste-befehle.html) read, is also a link, here to a file under `/usr/lib`.
::::

⁠**In short:** `/bin`, `/sbin` and `/lib` are symbolic links to `/usr` today; old paths keep working.

:::hintergrund Why there were once /bin and /usr/bin
The separation dates from a time when storage devices were small. What you needed to boot and repair the system was on the first storage device under `/bin`, `/sbin` and `/lib`; everything else was on a second one, which was mounted at `/usr`. Today, storage devices hold many times as much, and where `/usr` does sit on a storage device of its own, the system mounts it right at the beginning of the boot process. The original reason therefore no longer applies. In return, the merge has advantages: everything the distribution delivers is located under a single directory, which can be write-protected, backed up or provided to several computers as a whole, and scripts find a program under both paths.
:::

### Hard and symbolic links compared

<span class="anker" id="stufe-8-7"></span>

Both kinds of links give a file a further way in, but in fundamentally different ways. Table [3](#tab-3) puts them side by side.

<span class="anker" id="tab-3"></span>

**Table 3:** Hard and symbolic links.

|  | hard link | symbolic link |
|---|---|---|
| what it is | a further entry for the same inode | a file of its own with a path in it |
| own inode | no | yes |
| link count of the target | increases by 1 | stays the same |
| target deleted | data remain reachable through the link | link points nowhere |
| to directories | not allowed | allowed |
| into another file system | not possible | possible |
| in `ls -l` | like any regular file, link count greater than 1 | type `l`, arrow to the target |
| created with | `ln target name` | `ln -s target name` |

Two rows of the table are prohibitions for hard links. A hard link to a directory is not allowed, and a hard link cannot lead into another file system. On the test system, `/tmp` is in a file system of its own in main memory (subsection [7.6](die-verzeichnisstruktur-von-linux.html#stufe-7-6)); a hard link there therefore fails:

::::beispiel Two forbidden hard links
```console
$ ln rezepte rezepte2
ln: rezepte: hard link not allowed for directory
$ ln einkauf.txt /tmp/einkauf.txt
ln: failed to create hard link 'einkauf.txt' => '/tmp/einkauf.txt': Invalid cross-device link
```

“Invalid cross-device link” means that a link across the boundary of a file system is not allowed; “device” stands for the file system here. The GNU implementation of `ln` reports the same thing but names the two paths in reverse order, the new name first. The order above reflects the state of uutils version 0.8 in Ubuntu 26.04.
::::

⁠**In short:** A hard link is a name with equal rights for the same inode, only in the same file system and only for files; a symbolic link is a signpost that may point anywhere, even nowhere.

:::hintergrund Why hard links have these limits
The boundary between file systems follows directly from the inode number: it is unique only within one file system. An entry in a directory of one file system cannot point to an inode of another, because the number would mean something completely different there. A symbolic link, by contrast, contains a path, and a path may cross any boundary. The prohibition for directories protects the tree. If a directory were allowed to contain a hard link to a higher directory, a cycle would arise, and any program that walks through the tree level by level could go around in it endlessly. The inventors of Unix already named a second reason: with arbitrary links to directories, it would be hard to determine when a subtree no longer has any connection to the root, that is, when it has become unreachable even though its link count is not yet 0. Only the entries `.` and `..` are created by the system itself, and from them it recognizes how the tree is structured.
:::

### Exercises for Section [8](#stufe-8)

<span class="anker" id="stufe-8-8"></span>

:::aufgabe Exercise 27 ★★ The link experiment
<span class="anker" id="aufg-27"></span>

In a new directory `links`, use nano to create a file `original.txt` with the line `Zeile eins` (German for “line one”). Create a hard link `hart.txt` and a symbolic link `weich.txt` to it (`hart` and `weich` are German for “hard” and “soft”). (a) Compare the inode numbers and link counts with `ls -li` and with `stat -c "%i %h %n" original.txt hart.txt weich.txt`. (b) Delete `original.txt` and read both links with `cat`. Explain each result with Figure [31](#abb-31) and Figure [32](#abb-32). Remove the directory afterward.

:::loesung
```console
$ cd links
$ ln original.txt hart.txt
$ ln -s original.txt weich.txt
$ ls -li
total 8
95388 -rw-r--r-- 2 student student 11 Nov 10 02:42 hart.txt
95388 -rw-r--r-- 2 student student 11 Nov 10 02:42 original.txt
95389 lrwxrwxrwx 1 student student 12 Nov 10 02:42 weich.txt -> original.txt
$ stat -c "%i %h %n" original.txt hart.txt weich.txt
95388 2 original.txt
95388 2 hart.txt
95389 1 weich.txt
$ rm original.txt
$ cat hart.txt
Zeile eins
$ cat weich.txt
cat: weich.txt: No such file or directory
$ ls -li
total 4
95388 -rw-r--r-- 1 student student 11 Nov 10 02:42 hart.txt
95389 lrwxrwxrwx 1 student student 12 Nov 10 02:42 weich.txt -> original.txt
$ cd ..
$ rm -r links
```

(a) `original.txt` and `hart.txt` have the same inode number and the link count 2: two entries for one inode. `weich.txt` has an inode of its own with the link count 1 and is 12 bytes in size, as long as the text `original.txt`. `stat -c` prints only the requested information: `%i` the inode number, `%h` the link count, `%n` the name. (b) After `rm original.txt`, one entry is gone, the count drops to 1, and the data can be read in full through `hart.txt` (Figure [31](#abb-31)). `weich.txt` still contains the path `original.txt`, but nothing exists under this name anymore; the link is dangling (Figure [32](#abb-32)). The inode numbers on your computer are different.
:::
:::

:::aufgabe Exercise 28 ★ How many names does a directory have?
<span class="anker" id="aufg-28"></span>

Predict which link count `ls -ld fotos/urlaub/2026` shows after you created the directory `berge` in it in subsection [6.6](kopieren-verschieben-loschen.html#stufe-6-6). Which entries point to this inode? Check on the computer.

:::loesung
Prediction: 3. The inode of `fotos/urlaub/2026` is pointed to by the entry `2026` in `fotos/urlaub`, the entry `.` in `2026` itself and the entry `..` in `berge`, so $2 + 1$:

```console
$ ls -ld fotos/urlaub/2026
drwxr-xr-x 3 student student 4096 Nov 10 02:42 fotos/urlaub/2026
```
:::
:::

:::aufgabe Exercise 29 ★★ Copy, rename, link
<span class="anker" id="aufg-29"></span>

You type `cp einkauf.txt kopie.txt`, `mv kopie.txt neu.txt` and `ln neu.txt hart.txt` one after another. Which of the names `einkauf.txt`, `neu.txt` and `hart.txt` have the same inode number at the end? Justify your answer with what each command changes in the directories, and check with `ls -i`. Then delete `neu.txt` and `hart.txt`.

:::loesung
`cp` creates a new file and thus a new inode: `kopie.txt` has a different number than `einkauf.txt`. `mv` only moves the entry, and the inode stays: `neu.txt` has the number of `kopie.txt`. `ln` creates a second entry for the same inode: `hart.txt` has the same number as `neu.txt`.

```console
$ cp einkauf.txt kopie.txt
$ mv kopie.txt neu.txt
$ ln neu.txt hart.txt
$ ls -i einkauf.txt neu.txt hart.txt
95361 einkauf.txt  95387 hart.txt  95387 neu.txt
$ rm neu.txt hart.txt
```

`neu.txt` and `hart.txt` share the inode 95387; `einkauf.txt` has its own.
:::
:::

:::aufgabe Exercise 30 ★★★ What cp does with a link
<span class="anker" id="aufg-30"></span>

Copy the symbolic link `zettel.txt` once with `cp zettel.txt zettel_kopie.txt` and once with `cp -P zettel.txt zettel_link.txt`. Compare the three entries with `ls -l`. What did `cp` copy in each case, the link or its target? Why is the behavior without `-P` the right one for most purposes?

:::loesung
```console
$ cp zettel.txt zettel_kopie.txt
$ cp -P zettel.txt zettel_link.txt
$ ls -l zettel.txt zettel_kopie.txt zettel_link.txt
lrwxrwxrwx 1 student student 11 Nov 10 02:42 zettel.txt -> einkauf.txt
-rw-r--r-- 1 student student 32 Nov 10 02:43 zettel_kopie.txt
lrwxrwxrwx 1 student student 11 Nov 10 02:43 zettel_link.txt -> einkauf.txt
$ rm zettel_kopie.txt zettel_link.txt
```

Without `-P`, `cp` followed the link and copied its target: `zettel_kopie.txt` is a regular file with the 32 bytes of the shopping list. With `-P` (short for “no dereference”, do not follow), it copied the link itself: `zettel_link.txt` is again a link with the contents `einkauf.txt`. The behavior without the option fits what you usually want: if you copy a file, you want to keep its contents. A copied link would contain only a path, and a relative path can lead nowhere at the new location, as the second example in subsection [8.5](#stufe-8-5) showed.
:::
:::

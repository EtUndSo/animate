---
title: Finding files and measuring space
pfad: Computer Science / Linux and the Command Line / Files, Directories and Paths
adresse: informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade
knoten: Chapter 3: Files, Directories and Paths
order: 6081100
summary: Sooner or later, you no longer know where a file is, or space is running low and you look for what is using it.
tags: find, -name pattern, -type type, -size n, -mtime n, !, -maxdepth n, action
lang: en
---

<span class="anker" id="stufe-10"></span>

:::zweck
Sooner or later, you no longer know where a file is, or space is running low and you look for what is using it. This section shows `find`, which searches a subtree by name, type, size and age, and `du`, which adds up the space used.
:::

### Searching with find

<span class="anker" id="stufe-10-1"></span>

`ls` shows what is in a directory; `ls -R` and `tree` show whole subtrees. But if you are looking only for certain files, you do not want to read thousands of lines; you want a selection.

:::abbildung linux/k3find 37
How `find` works: it enters the starting directory and goes through each entry, descends into each subdirectory and then returns. At each entry, it checks the conditions; whatever meets them is printed.
:::

:::definition Definition 10.1 (find)
<span class="anker" id="satz-10-1"></span>

The command __find__ walks through the subtree below each given starting directory, entry by entry and level by level. For each entry, it checks the conditions that follow the starting directories, the so-called tests, and prints the path of every entry that passes all tests. Without tests, it prints every entry.
:::

The paths begin with the starting directory, exactly as you typed it. The order is the one in which the entries are stored in the directories; it is not sorted. Figure [37](#abb-37) shows the route through the tree.

::::beispiel Everything under rezepte
```console
$ find rezepte
rezepte
rezepte/kuchen
rezepte/kuchen/apfelkuchen.txt
rezepte/kuchen/kaesekuchen.txt
rezepte/zettel.txt
rezepte/suppen
rezepte/suppen/kuerbissuppe.txt
```

`find` begins with the starting directory itself, descends into `kuchen`, returns, takes the link `zettel.txt` along and descends into `suppen`.
::::

⁠**In short:** `find start tests` walks through a subtree and prints the paths of the entries that pass all tests.

### Searching by name: -name

<span class="anker" id="stufe-10-2"></span>

Usually you remember part of the name: the file ended in `.txt`, or “strand” appeared somewhere in it. For this, there is a test that understands patterns.

:::abbildung linux/k3quoting 38
Two ways to type the same pattern. Without quotes, the shell replaces `*.txt` with the matching names in the working directory before the command even starts, and `find` gets a wrong condition. With quotes, the pattern reaches `find` unchanged, and `find` tests it against every name in the whole subtree.
:::

:::definition Definition 10.2 (-name, -iname)
<span class="anker" id="satz-10-2"></span>

The test __-name pattern__ passes if the name of an entry, that is, the last part of its path, matches the pattern; the pattern follows the same rules as in subsection [6.6](kopieren-verschieben-loschen.html#stufe-6-6). The test `-iname` does the same but does not distinguish between uppercase and lowercase letters.
:::

Here it is not the shell that applies the pattern but `find`, and it does so to every name in the subtree it walks through. For the pattern to reach `find`, you have to put it in quotes; otherwise the shell replaces it beforehand with names from the working directory, as Figure [38](#abb-38) shows.

::::beispiel All text files, all beach photos
```console
$ find . -name "*.txt"
./aktuell.txt
./zettel.txt
./rezepte/kuchen/apfelkuchen.txt
./rezepte/kuchen/kaesekuchen.txt
./rezepte/zettel.txt
./rezepte/suppen/kuerbissuppe.txt
./fotos/urlaub/2026/notiz.txt
./einkauf.txt
$ find . -iname "STRAND*"
./fotos/urlaub/2026/strand_10.jpg
./fotos/urlaub/2026/strand_1.jpg
./fotos/urlaub/2026/strand_2.jpg
```

The starting directory `.` is the working directory `~/linuxk3`. The links `aktuell.txt` and `zettel.txt` are found as well, because `-name` checks only the name, not the type. `-iname` finds the beach photos, although the pattern is typed in uppercase letters.
::::

::::beispiel [Counterexample] The pattern without quotes
```console
$ find . -name *.txt
find: paths must precede expression: `einkauf.txt'
find: possible unquoted pattern after predicate `-name'?
```

The working directory contains three names ending in `.txt`: `aktuell.txt`, `einkauf.txt` and `zettel.txt`. The shell replaced the pattern with these three, and `find` received `-name aktuell.txt einkauf.txt zettel.txt`. It does not know what to do with the extra `einkauf.txt`, and it even guesses correctly that a pattern without quotes is to blame.
::::

⁠**In short:** `-name "pattern"` searches by name; the quotes make sure that `find`, not the shell, applies the pattern.

### Searching by type: -type

<span class="anker" id="stufe-10-3"></span>

Sometimes you are not looking for a particular file but for all directories of a subtree or all symbolic links, for example to find dangling ones.

:::definition Definition 10.3 (-type)
<span class="anker" id="satz-10-3"></span>

The test __-type type__ passes if an entry is of the given type: `f` for a regular file, `d` for a directory, `l` for a symbolic link, `b` and `c` for device files.
:::

The letters correspond to those in the first column of `ls -l`, except that `f` instead of `-` stands for the regular file.

::::beispiel Directories and links of the playground
```console
$ find . -type d
.
./rezepte
./rezepte/kuchen
./rezepte/suppen
./fotos
./fotos/urlaub
./fotos/urlaub/2026
./fotos/urlaub/2026/berge
$ find . -type l
./aktuell.txt
./zettel.txt
./rezepte/zettel.txt
./urlaub
```

Eight directories, including the starting directory, and four symbolic links. The link `urlaub` points to a directory but is counted as a link; `find` does not follow symbolic links but looks at the links themselves.
::::

⁠**In short:** `-type f`, `-type d` and `-type l` select regular files, directories or symbolic links.

### Searching by size: -size

<span class="anker" id="stufe-10-4"></span>

When space is running low, you look for the big chunks. Conversely, empty files help you track down forgotten placeholders.

:::abbildung linux/k3findsize 39
How `-size` rounds: files of 0, 32, 1024 and 1025 bytes on a number line, above them their size in whole KiB, rounded up. `-size -1k` requires less than 1 and matches only the empty file; `-size -2k` matches everything up to 1024 bytes.
:::

:::definition Definition 10.4 (-size)
<span class="anker" id="satz-10-4"></span>

The test __-size n__ compares the size of an entry with `n`; `+n` means greater than `n`, `-n` less than `n`, and `n` alone exactly `n`. A letter after the number gives the unit: `c` for bytes, `k` for 1024 bytes, `M` for $1024^2$, `G` for $1024^3$; without a letter, the old unit of 512 bytes applies. Before comparing, `find` rounds the size up to whole units.
:::

Rounding up is a trap. A file with 32 bytes counts as 1 KiB, because a unit that has been started counts in full. `-size -1k` requires “less than 1 KiB” and therefore matches only empty files, not all files under 1024 bytes as you might expect. Figure [39](#abb-39) shows the rounding on the number line.

::::beispiel Large programs and empty files
```console
$ find /usr/bin -size +10M
/usr/bin/shellcheck
/usr/bin/x86_64-linux-gnu-lto-dump-15
/usr/bin/coreutils
/usr/bin/snap
/usr/bin/gdb
$ find . -type f -size 0
./.einstellungen
./fotos/urlaub/2026/strand_10.jpg
./fotos/urlaub/2026/strand_1.jpg
./fotos/urlaub/2026/strand_2.jpg
./fotos/urlaub/2026/berge/berg_2.jpg
./fotos/urlaub/2026/berge/berg_1.jpg
./fotos/urlaub/2026/notiz.txt
```

On the test computer, five programs are larger than 10 MiB, among them `coreutils`, the multicall program of uutils from [Chapter 2, Section 7.2](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/zwei-fassungen-der-grundbefehle-gnu-und-uutils.html#stufe-7-2). The placeholders for the photos and the hidden settings file are empty; `find` always shows hidden entries as well.
::::

::::beispiel [Second example] The rounding trap
```console
$ find . -type f -size -1k
./.einstellungen
./fotos/urlaub/2026/strand_10.jpg
./fotos/urlaub/2026/strand_1.jpg
./fotos/urlaub/2026/strand_2.jpg
./fotos/urlaub/2026/berge/berg_2.jpg
./fotos/urlaub/2026/berge/berg_1.jpg
./fotos/urlaub/2026/notiz.txt
$ find . -type f -size -2k
./.einstellungen
./rezepte/kuchen/apfelkuchen.txt
./rezepte/kuchen/kaesekuchen.txt
./rezepte/suppen/kuerbissuppe.txt
./fotos/urlaub/2026/strand_10.jpg
./fotos/urlaub/2026/strand_1.jpg
./fotos/urlaub/2026/strand_2.jpg
./fotos/urlaub/2026/berge/berg_2.jpg
./fotos/urlaub/2026/berge/berg_1.jpg
./fotos/urlaub/2026/notiz.txt
./einkauf.txt
```

`-size -1k` returns exactly the same as `-size 0`. Only `-size -2k` also finds the recipes and the shopping list with their few dozen bytes, 32 to 59 on the test computer. If you are looking for files under 1024 bytes, the safest way is to write `-size -1024c`.
::::

⁠**In short:** `-size +n` and `-size -n` search by size; because `find` rounds up to whole units, you use bytes (`c`) for exact limits.

### Searching by age: -mtime, -mmin and -newer

<span class="anker" id="stufe-10-5"></span>

“The file from yesterday” is often the only thing you remember about a file. `find` can search for that, too, using the time of the last modification of the contents. Figure [40](#abb-40) shows how it counts the age.

:::abbildung linux/k3findzeit 40
A time axis that reaches from now to the left into the past, divided into whole days of 24 hours. `-mtime -1` marks the most recent day, `-mtime +7` everything that lies at least eight whole days back; the cheesecake from October 1 is far to the left.
:::

:::definition Definition 10.5 (-mtime, -mmin, -newer)
<span class="anker" id="satz-10-5"></span>

The test __-mtime n__ compares the age of the last modification in whole days of 24 hours with `n`; partial days are dropped, and `+n` and `-n` mean more and less, as with `-size`. `-mmin n` does the same in minutes. `-newer file` passes if an entry was modified later than the given file.
:::

So `-mtime -1` means “changed in the last 24 hours”, and `-mtime +7` means “at least eight whole days ago”, because an age of seven days and a few hours counts as 7 and is not greater than 7. With `-newer`, you can create a reference file and later find everything that has changed since then.

::::beispiel Old and fresh files
With `touch -t`, the cheesecake gets a modification time in October:

```console
$ touch -t 202610011200 rezepte/kuchen/kaesekuchen.txt
$ find . -type f -mtime +7
./rezepte/kuchen/kaesekuchen.txt
$ find rezepte -type f -mmin -60
rezepte/kuchen/apfelkuchen.txt
rezepte/suppen/kuerbissuppe.txt
```

Only the cheesecake is older than seven whole days; the other two recipes were changed in the last hour.
::::

::::beispiel [Second example] What has changed since the reference file?
```console
$ touch merker
$ touch rezepte/kuchen/apfelkuchen.txt
$ find rezepte -newer merker
rezepte/kuchen/apfelkuchen.txt
$ rm merker
```

Only the apple cake was changed after the reference file `merker` (German for “marker”). Backup programs work on the same principle.
::::

⁠**In short:** `-mtime` and `-mmin` search by age in whole days or minutes, `-newer` by comparison with another file.

### Combining tests and processing matches

<span class="anker" id="stufe-10-6"></span>

A search becomes really useful only when you combine conditions: regular files that end in `.txt` and are no older than a week. And often you want to do more with the matches than display them.

:::definition Definition 10.6 (Combining, -maxdepth, action)
<span class="anker" id="satz-10-6"></span>

If several tests follow one another, an entry must pass all of them. A __!__ in front of a test negates it. The option __-maxdepth n__ directly after the starting directories limits the search to `n` levels below the starting directory. What `find` does with a match is determined by an __action__; if none is given, it is `-print`, which prints the path.
:::

Two more actions are useful: `-ls` prints each match in a form similar to `ls -l`, and `-delete` deletes it. The test `-samefile file` goes with Section [8](inode-und-links.html#stufe-8): it finds all names of the same inode, that is, all hard links of a file.

::::beispiel Searching shallowly, negating, finding hard links
```console
$ find /etc -maxdepth 1 -name "h*"
/etc/host.conf
/etc/hosts
/etc/hostname
$ find . -type f ! -name "*.jpg"
./.einstellungen
./rezepte/kuchen/apfelkuchen.txt
./rezepte/kuchen/kaesekuchen.txt
./rezepte/suppen/kuerbissuppe.txt
./fotos/urlaub/2026/notiz.txt
./einkauf.txt
```

With `-maxdepth 1`, `find` stays in `/etc` itself and does not descend into any of its 91 subdirectories. The second search returns all regular files whose name does not end in `.jpg`. For `-samefile`, the shopping list needs a second name:

```console
$ ln einkauf.txt fotos/liste.txt
$ find . -samefile einkauf.txt
./fotos/liste.txt
./einkauf.txt
$ rm fotos/liste.txt
```
::::

:::warnung -delete only after a trial run
`-delete` deletes everything that passes the tests without asking, and if you are in the wrong directory or a test is too broad, it hits much more than intended. So always run the same line without `-delete` first and check the list. `-delete` belongs at the end of the line: if it comes before the tests, `find` deletes every entry before it checks it.
:::

::::beispiel [Second example] Cleaning up with a trial run
```console
$ touch rezepte/a.tmp rezepte/suppen/b.tmp
$ find . -name "*.tmp"
./rezepte/a.tmp
./rezepte/suppen/b.tmp
$ find . -name "*.tmp" -delete
$ find . -name "*.tmp"
```

The trial run shows exactly the two files that are to go; the same line with `-delete` removes them, and a second trial run finds nothing more.
::::

⁠**In short:** Tests in a row must all pass, `!` negates one, `-maxdepth` limits the depth; use `-delete` only after a trial run without it.

:::hintergrund Or, parentheses and a faster way to a name
Besides the silent “and”, `find` also knows an “or”: `-o`. Because “and” binds more strongly, you often need parentheses, and you must protect them from the shell, for example with a backslash: `find . \( -name "*.jpg" -o -name "*.png" \)` finds both kinds of images. `find` evaluates the tests from left to right and stops as soon as the result is certain; that is why the order matters, and that is why a `-delete` at the beginning deletes everything. Because `find` walks through the whole subtree for every search, it can take a long time on large storage devices. Some systems also have the command `locate`, which searches a list of all paths that is usually rebuilt once a day: much faster, but without the files that have been added since the list was last built.
:::

### Measuring disk usage: du

<span class="anker" id="stufe-10-7"></span>

`df` tells you how full an entire file system is. If you want to free up space, you need to know which directory is using it.

:::definition Definition 10.7 (du)
<span class="anker" id="satz-10-7"></span>

The command __du__ (short for “disk usage”) adds up, for each given directory and each subdirectory in it, the space that the files occupy on the storage device, in units of 1024 bytes. With `-s`, it prints only the total for each argument, with `-h` human-readable units like `ls -h`.
:::

`du` counts the space used, not the number of bytes in the contents. A file system allocates space in blocks, usually of 4096 bytes each with ext4; a file always occupies whole blocks, even if the last one is only partly used. A file with 32 bytes therefore occupies 4 KiB. With `--apparent-size`, `du` instead counts the bytes of the contents, like `ls -l`. A file with several hard links is counted only once by `du`.

:::abbildung linux/k3du 41
The space of the directory `rezepte`, added up: the directory itself 4 KiB, `kuchen` with two recipes $4 + 4 + 4 = 12$ KiB, `suppen` with one $4 + 4 = 8$ KiB, the symbolic link 0. Together $4 + 12 + 8 = 24$ KiB.
:::

::::beispiel Who is using the space?
```console
$ du rezepte
12      rezepte/kuchen
8       rezepte/suppen
24      rezepte
$ du -sh rezepte fotos
24K     rezepte
16K     fotos
$ du -sh ~/linuxk3
48K     /home/student/linuxk3
```

`kuchen` occupies 12 KiB: one block for the directory itself and one each for the two recipes. With its own block, `rezepte` comes to 24, as Figure [41](#abb-41) calculates. `fotos` occupies 16 KiB, namely four directories of one block each; the empty photo files occupy nothing.
::::

::::beispiel [Second example] Contents and space of a small file
```console
$ ls -l einkauf.txt
-rw-r--r-- 1 student student 32 Nov 10 02:42 einkauf.txt
$ du -h einkauf.txt
4.0K    einkauf.txt
$ du -h --apparent-size einkauf.txt
32      einkauf.txt
```

32 bytes of contents, but a whole block of 4096 bytes occupied. `stat` showed the same in subsection [8.1](inode-und-links.html#stufe-8-1): `Blocks: 8` counts in old units of 512 bytes, and $8 \cdot 512 = 4096$.
::::

⁠**In short:** `du -sh` shows how much space a directory occupies; whole blocks are counted, which is why even a tiny file occupies 4 KiB.

:::hintergrund Why a file system counts in blocks
A file system could manage every byte individually, but then it would need a huge list for each file stating where its bytes are. Instead, it divides the storage device into blocks of equal size and records in the inode only which blocks a file occupies. Large blocks keep this administrative data small and make reading large files fast, but they waste space with small files; 4096 bytes are a compromise that matches the page size with which the processor manages main memory. This also explains why `du` and `df` do not always agree: `du` counts up what the files of a subtree occupy, while `df` asks the file system for its administrative data. A deleted file that a program still has open is no longer found by `du`, because it has no name; `df`, however, continues to report its space as used until the program closes it (subsection [8.4](inode-und-links.html#stufe-8-4)).
:::

### Exercises for Section [10](#stufe-10)

<span class="anker" id="stufe-10-8"></span>

:::aufgabe Exercise 34 ★★ Search tasks
<span class="anker" id="aufg-34"></span>

For each task, write a command line with `find` and run it: (a) all files in `/etc` itself, not in subdirectories, whose name ends in `.conf`; (b) all directories of your playground; (c) all files in `/usr/bin` that are larger than 1 MiB; (d) all regular files in `~/linuxk3` that were changed in the last 24 hours.

:::loesung
(a) `find /etc -maxdepth 1 -name "*.conf"`. (b) `find ~/linuxk3 -type d`; subsection [10.3](#stufe-10-3) shows the output. (c) `find /usr/bin -size +1M`; because of the rounding up, `+1M` means “more than 1 MiB”. (d) `find ~/linuxk3 -type f -mtime -1`. On the test computer, shortened:

```console
$ find /etc -maxdepth 1 -name "*.conf"
/etc/xattr.conf
/etc/host.conf
/etc/pam.conf
...
/etc/debconf.conf
/etc/wsl-distribution.conf
$ find /usr/bin -size +1M
/usr/bin/x86_64-linux-gnu-gcc-15
/usr/bin/strace
...
/usr/bin/gdb
/usr/bin/perl
$ find ~/linuxk3 -type f -mtime -1
/home/student/linuxk3/.einstellungen
/home/student/linuxk3/verein/mitglieder/liste.txt
...
/home/student/linuxk3/einkauf.txt
```

There are 27 configuration files and 23 programs over 1 MiB. In (d), the cheesecake is missing, because its modification time is in October; because `find` does not sort by name, the matches appear in the order of the directories.
:::
:::

:::aufgabe Exercise 35 ★★ The forgotten quotes
<span class="anker" id="aufg-35"></span>

Change to `~/linuxk3/fotos/urlaub/2026`, which contains exactly one file ending in `.txt`, and compare `find ~/linuxk3 -name *.txt` with `find ~/linuxk3 -name "*.txt"`. Why does the first line report no error this time but return too little? Why does the second line return the same in every working directory?

:::loesung
```console
$ cd fotos/urlaub/2026
$ find ~/linuxk3 -name *.txt
/home/student/linuxk3/fotos/urlaub/2026/notiz.txt
$ find ~/linuxk3 -name "*.txt"
/home/student/linuxk3/aktuell.txt
/home/student/linuxk3/verein/mitglieder/liste.txt
...
/home/student/linuxk3/einkauf.txt
$ cd ~/linuxk3
```

The working directory contains exactly one name ending in `.txt`: `notiz.txt`. The shell replaces the unquoted pattern with this one name, and `find` gets `-name notiz.txt`. That is a valid condition, so there is no error, but now only files named `notiz.txt` are searched for. With quotes, `find` gets the pattern itself and applies it to every name in the subtree. Because the shell never replaces a pattern in quotes, the result then does not depend on which files happen to be in the working directory.
:::
:::

:::aufgabe Exercise 36 ★★★ The rounding trap of -size
<span class="anker" id="aufg-36"></span>

Predict what `find rezepte -type f -size -1M` and `find rezepte -type f -size -1024k` print, and check it. Explain the difference with the rounding up. How do you reliably find all files that are smaller than 1 MiB?

:::loesung
```console
$ find rezepte -type f -size -1M
$ find rezepte -type f -size -1024k
rezepte/kuchen/apfelkuchen.txt
rezepte/kuchen/kaesekuchen.txt
rezepte/suppen/kuerbissuppe.txt
```

With `-1M`, `find` rounds every size up to whole MiB: the recipes with a few dozen bytes count as 1 MiB, and 1 is not less than 1. Only an empty file would match, and there is none in `rezepte`. With `-1024k`, it rounds up to whole KiB: the recipes count as 1 KiB, and that is less than 1024. The reliable way is to give the size in bytes, where nothing is rounded: `find rezepte -type f -size -1048576c` finds all files under $1024^2 = 1\,048\,576$ bytes.
:::
:::

:::aufgabe Exercise 37 ★★ How much space does a small file occupy?
<span class="anker" id="aufg-37"></span>

For `rezepte/kuchen/kaesekuchen.txt`, compare the size from `ls -l` with the space from `du -h` and `du -h --apparent-size`. How much space would a hundred such files occupy, and how many bytes of contents would they have together? How large would a file have to be at least for it to occupy two blocks?

:::loesung
```console
$ ls -l rezepte/kuchen/kaesekuchen.txt
-rw-r--r-- 1 student student 32 Oct  1 12:00 rezepte/kuchen/kaesekuchen.txt
$ du -h rezepte/kuchen/kaesekuchen.txt
4.0K    rezepte/kuchen/kaesekuchen.txt
$ du -h --apparent-size rezepte/kuchen/kaesekuchen.txt
32      rezepte/kuchen/kaesekuchen.txt
```

The file has 32 bytes of contents and occupies one block of 4096 bytes. A hundred such files would occupy $100 \cdot 4 = 400$ KiB, although together they would contain only $100 \cdot 32 = 3200$ bytes, just over 3 KiB. A file occupies two blocks from $4096 + 1 = 4097$ bytes on, because then one block is no longer enough. Your recipes probably have different lengths; as long as they stay under 4097 bytes, each one occupies exactly 4 KiB.
:::
:::

**For further practice.** The freely accessible learning platform pwn.college offers short exercises in the browser under the name “Linux Luminarium”; the modules “Pondering Paths” and “File Globbing” match this chapter. They run on someone else's computer, not on your own.

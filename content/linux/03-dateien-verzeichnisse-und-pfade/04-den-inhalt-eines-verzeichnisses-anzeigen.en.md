---
title: Showing the contents of a directory
pfad: Computer Science / Linux and the Command Line / Files, Directories and Paths
adresse: informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade
knoten: Chapter 3: Files, Directories and Paths
order: 6080400
summary: ls is the command people type most often at the command line: it shows what is in a directory.
tags: ls, hidden file, -F, -l, regular file, -h
lang: en
---

<span class="anker" id="stufe-3"></span>

:::zweck
`ls` is the command people type most often at the command line: it shows what is in a directory. With a few options, it also reveals hidden entries, the type of each entry, size and age. Along with it come the rules for which names a file may have at all.
:::

### The command ls

<span class="anker" id="stufe-3-1"></span>

Section [1](dateien-verzeichnisse-und-der-verzeichnisbaum.html#stufe-1) already used `ls` to show the names in `/usr` and `/`. Here, the focus is on exactly what it does with its arguments.

:::definition Definition 3.1 (ls)
<span class="anker" id="satz-3-1"></span>

The command __ls__ prints, for each directory given as an argument, the names of its entries, sorted by name, and for every other file its name. Without an argument, it shows the working directory.
:::

If you name several directories, `ls` puts the name of the directory and a colon before each list. If an argument does not exist, `ls` reports this and continues with the others. In a terminal, `ls` arranges the names in columns to save space.

::::beispiel Several arguments
```console
$ ls /usr /home
/home:
student

/usr:
bin  games  include  lib  lib64  libexec  local  sbin  share  src
$ ls /usr/bin/bash
/usr/bin/bash
$ ls /gibtsnicht
ls: cannot access '/gibtsnicht': No such file or directory
```

The directories appear in alphabetical order, not in the order in which they were typed. For the file `/usr/bin/bash`, `ls` only repeats its name: this is the confirmation that it exists.
::::

⁠**In short:** `ls` lists the entries of directories; for a regular file, it gives its name.

### The hidden file

<span class="anker" id="stufe-3-2"></span>

Many programs store configuration files in the home directory. If these files appeared with every `ls`, your own files would get lost among them. That is why there is a convention that keeps such files out of the normal listing. Figure [9](#abb-9) shows a directory that looks empty without an option.

:::abbildung linux/k3versteckt 9
The same directory `/etc/skel` listed twice. Without an option, the list stays empty; with `-a`, `.`, `..` and three files whose names begin with a dot appear. The files were there all along.
:::

:::definition Definition 3.2 (Hidden file)
<span class="anker" id="satz-3-2"></span>

A __hidden file__ is a file or directory whose name begins with a dot. `ls` shows such entries only with the option `-a` (short for “all”); `-A` shows them as well but leaves out `.` and `..`.
:::

“Hidden” only means: not in the ordinary list. Anyone who is otherwise allowed to read the file can read it; there is nothing secret about it.

::::beispiel The template for new users
The directory `/etc/skel` contains the files that Linux copies into a new user's home directory when it creates the user:

```console
$ ls /etc/skel
$ ls -a /etc/skel
.  ..  .bash_logout  .bashrc  .profile
$ ls -A /etc/skel
.bash_logout  .bashrc  .profile
```

Without an option, the directory looks empty. With `-a`, three configuration files of the shell appear, along with the two special entries from subsection [2.5](das-arbeitsverzeichnis-und-pfade.html#stufe-2-5); so these are real entries of every directory. Copies of the three files are also in your home directory; `ls -a ~` shows them alongside further hidden files.
::::

⁠**In short:** A name with a dot at the start makes a file invisible to the ordinary `ls`; `ls -a` shows everything.

:::hintergrund Hidden is only a convention
A hidden file has no special attribute that would be stored in the system. There is only the rule that `ls` and many other programs skip names that begin with a dot. Graphical file managers follow it as well and have a switch such as “Show Hidden Files”. Windows is different: there, “hidden” is an attribute that you can give to or take from each file individually, regardless of its name. On Linux, you make a file visible by renaming it.
:::

### The type of an entry: ls -F

<span class="anker" id="stufe-3-3"></span>

In the ordinary list, a directory and a file look the same. But if you want to move around the tree, you have to be able to tell them apart.

:::definition Definition 3.3 (ls -F)
<span class="anker" id="satz-3-3"></span>

With the option __-F__ (long form `--classify`), `ls` appends a character to each name that reveals the type of the entry: `/` for a directory, `*` for an executable file, that is, a program, and a few other characters for rarer types. Regular files get no character.
:::

The character is not part of the name; `ls` only adds it in the display. Ubuntu also colors the names in the terminal, directories blue and programs green, for example; but the characters from `-F` work without colors as well, for instance in a transcript or in this chapter.

::::beispiel Directories and a program
```console
$ ls -F /usr
bin/    include/  lib64/    local/  share/
games/  lib/      libexec/  sbin/   src/
$ ls -F /usr/bin/bash
/usr/bin/bash*
```

All entries of `/usr` are directories. `/usr/bin/bash` is a program, the shell itself.
::::

⁠**In short:** `ls -F` marks directories with `/` and programs with `*`.

### The long format: ls -l

<span class="anker" id="stufe-3-4"></span>

Often you want to know more than the name: How big is a file, when was it last modified, is it a directory? For this, the long format gives each entry a line of its own.

:::abbildung linux/k3lsl 10
A line of `ls -l`, taken apart column by column: type of the entry, permissions, a number, owner, group, size in bytes, the time the contents were last modified and name. This section explains the type, owner and group, the size, the time and the name.
:::

:::definition Definition 3.4 (ls -l)
<span class="anker" id="satz-3-4"></span>

With the option __-l__ (short for “long”), `ls` prints each entry on a line of its own with seven pieces of information: type and permissions, a number, owner, group, size in bytes, the time of the last modification of the contents and name.
:::

Figure [10](#abb-10) takes such a line apart. The details:

<ul>

<li>

The first character gives the type. A `-` stands for a __regular file__, that is, a file with contents such as a text or a program; a `d` stands for a directory. There are further letters for rarer types.

</li>

<li>

The next nine characters are the permissions: they determine who may read, change or execute the file. How to read them is a topic of its own; for this chapter, it is enough that they are there.

</li>

<li>

The number after them is usually 1 for regular files and larger for directories. This section does not deal with it.

</li>

<li>

Owner and group name the user to whom the file belongs and a group of users to which it is assigned (users and groups: [Chapter 2, Section 6.2](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/das-system-erkunden.html#stufe-6-2)).

</li>

<li>

The size counts the bytes of the contents.

</li>

<li>

The time is the last modification of the contents; if it lies more than half a year in the past, `ls` shows the year instead of the time of day.

</li>

</ul>

Before the list, there is a line `total`: it states how much space the entries shown take up together on the storage device, in units of 1024 bytes.

::::beispiel The template in long format
```console
$ ls -la /etc/skel
total 20
drwxr-xr-x  2 root root 4096 Aug 27 16:10 .
drwxr-xr-x 93 root root 4096 Nov 10 02:36 ..
-rw-r--r--  1 root root  220 Feb 13  2026 .bash_logout
-rw-r--r--  1 root root 3771 Feb 13  2026 .bashrc
-rw-r--r--  1 root root  807 Feb 13  2026 .profile
```

The options `-l` and `-a` are bundled ([Chapter 2, Section 2.4](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/der-aufbau-einer-befehlszeile.html#stufe-2-4)). The first two lines are directories (`d`): `.` is `/etc/skel` itself, `..` is `/etc`. The other three are regular files (`-`) of the user `root`; at 3771 bytes, `.bashrc` is the largest. Their contents were last modified in February 2026, when Ubuntu built this template.
::::

**Viewing a directory itself.** If you give `ls -l` a directory, it shows the directory's contents. If you want the information about the directory itself, you add the option `-d` (short for “directory”):

```console
$ ls -l /usr/bin/bash
-rwxr-xr-x 1 root root 1540520 Feb 13  2026 /usr/bin/bash
$ ls -ld /etc
drwxr-xr-x 93 root root 4096 Nov 10 02:36 /etc
```

The shell `bash` is a regular file with just over one and a half million bytes; `/etc` is a directory. That it is exactly 4096 bytes in size is due to the way a file system allocates space: in fixed pieces of this size. Only a directory with very many entries needs several of them; `/usr/bin`, with over a thousand entries, is 36 864 bytes in size on the test computer.

⁠**In short:** `ls -l` shows the type, permissions, owner, group, size, modification time and name of each entry; `-d` shows the directory itself instead of its contents.

### Human-readable sizes: ls -h

<span class="anker" id="stufe-3-5"></span>

A number like 1540520 first has to be split into groups of three in your head before you can judge it. For a quick glance, there is a shorter notation.

:::definition Definition 3.5 (ls -h)
<span class="anker" id="satz-3-5"></span>

Together with `-l`, the option __-h__ (short for “human-readable”) makes `ls` print each size in the largest suitable unit: `K` for 1024 bytes, `M` for $1024^2$ bytes, `G` for $1024^3$ bytes. Below 10, there is one decimal place, and rounding is always up.
:::

So the letters denote powers of two, just like KiB, MiB and GiB from [Chapter 1, Section 5.1](/wissen/en/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/datentrager-abbild-und-prufsumme.html#stufe-5-1); `ls` just does not write the `i`. Because it rounds up, you never see a size that is smaller than the real one.

::::beispiel The size of the shell
```console
$ ls -lh /usr/bin/bash
-rwxr-xr-x 1 root root 1.5M Feb 13  2026 /usr/bin/bash
```

1 540 520 bytes become $1\,540\,520 / 1024 \approx 1504.4$ KiB and from that $1504.4 / 1024 \approx 1.469$ MiB. Because the value is below 10, it gets one decimal place, rounded up: `1.5M`. Like almost all tools, `ls` writes a decimal point, even in languages that use a decimal comma.
::::

⁠**In short:** `ls -lh` writes sizes with `K`, `M`, `G` of 1024 each and rounds up.

### Sorting and further options

<span class="anker" id="stufe-3-6"></span>

By default, `ls` sorts by name. Often a different order is more useful: the largest files first when space is running low, or the newest when you are looking for the file you just worked on. Table [1](#tab-1) collects the options you need most often; all of them can be bundled.

<span class="anker" id="tab-1"></span>

**Table 1:** Common options of `ls`.

| Option | long | Effect |
|---|---|---|
| `-a` | `--all` | hidden entries too, plus `.` and `..` |
| `-A` | `--almost-all` | hidden entries too, without `.` and `..` |
| `-F` | `--classify` | append a character for the type (`/` directory, `*` program) |
| `-l` |  | long format, one line per entry |
| `-h` | `--human-readable` | sizes with `K`, `M`, `G` (of 1024), rounded up |
| `-d` | `--directory` | the directory itself instead of its contents |
| `-S` |  | sort by size, largest first |
| `-t` |  | sort by modification time, newest first |
| `-r` | `--reverse` | reverse the order |
| `-R` | `--recursive` | also list all subdirectories, level by level |

Figure [11](#abb-11) shows how the same entries swap places with `-S`, `-t` and `-r`.

:::abbildung linux/k3sortieren 11
Four files as cards with name, size and time. Without an option, they are sorted by name; with `-S`, the largest move to the top, with `-t` the most recently modified ones, and `-r` reverses the respective order.
:::

::::beispiel The largest license texts
`/usr/share/common-licenses` contains the texts of widely used open source licenses. `-lhS` shows them by size, with human-readable numbers:

```console
$ ls -lhS /usr/share/common-licenses
total 260K
-rw-r--r-- 1 root root  35K Sep 30  2017 GPL-3
-rw-r--r-- 1 root root  26K Sep 18  2024 LGPL-2.1
-rw-r--r-- 1 root root  26K Apr  3  2017 MPL-1.1
...
-rw-r--r-- 1 root root 6.0K Dec 16  1996 Artistic
-rw-r--r-- 1 root root 1.5K Aug 26  1999 BSD
...
```

At 35 KiB, the GNU General Public License in version 3 is the largest; at 1.5 KiB, the BSD license is the smallest of those shown.
::::

⁠**In short:** `-S` sorts by size, `-t` by time, `-r` reverses, `-R` descends into all subdirectories.

### File names

<span class="anker" id="stufe-3-7"></span>

On Windows, you learn at some point which characters are forbidden in a file name. Linux is more generous, and that is exactly what sets traps as soon as you type names into a command line. Figure [12](#abb-12) shows the most common one, the space.

:::abbildung linux/k3namen 12
How the shell splits a line with the name `Program Files`. Without quotes, it becomes two words and thus two arguments; with quotes, the name stays a single word.
:::

:::satz Theorem 3.6 (Rules for file names)
<span class="anker" id="satz-3-6"></span>

A file name on Linux may contain any character except the slash `/` and the null byte, the byte with the value 0; on the usual file systems such as ext4, it is at most 255 bytes long. Uppercase and lowercase letters are distinct: `Brief.txt` and `brief.txt` are two files. A file name extension such as `.txt` or `.jpg` is just part of the name; the system does not interpret it.
:::

So the space is allowed, too. But the shell splits every line into words at spaces ([Chapter 2, Section 2.1](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/der-aufbau-einer-befehlszeile.html#stufe-2-1)), and a name with a space would become two arguments. To keep it a single word, you enclose it in quotes: `"mein urlaub.txt"` (German for “my vacation.txt”). The shell removes the quotes before it starts the command; the program receives the name without them. The Tab key does this automatically by putting a backslash before the space: `mein\ urlaub.txt` means the same.

A dash at the start of a name is similarly annoying: every program takes `-liste.txt` for an option. The remedy is the end of options `--` from [Chapter 2, Section 2.7](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/der-aufbau-einer-befehlszeile.html#stufe-2-7), or a path that does not begin with the dash, such as `./-liste.txt`.

**Good names.** The simplest rule is not to let such cases arise in the first place. When you name your own files, use lowercase letters, digits, dot, hyphen and underscore: `urlaub_2026.txt` instead of `Urlaub 2026.txt`. You can type such names without quotes, and they work on every system.

::::beispiel A Windows directory with a space
Under WSL 2, you can try this with the Windows directory `Program Files` without changing anything. The option `-d` shows the directory itself:

```console
$ ls -d /mnt/c/Program Files
ls: cannot access '/mnt/c/Program': No such file or directory
ls: cannot access 'Files': No such file or directory
$ ls -d "/mnt/c/Program Files"
 '/mnt/c/Program Files'
$ ls /ETC
ls: cannot access '/ETC': No such file or directory
```

Without quotes, `ls` receives two arguments and finds neither of them. With quotes, it is a single argument. In its output, `ls` itself puts the name in single quotes so that you can see the space and can copy the name back into a command line as it is; the space before the name only serves to align the columns. `/ETC` does not exist, because the directory is called `/etc`. In a virtual machine or in the live system, there is no `/mnt/c`; there, you can only read through the first part of the example.
::::

⁠**In short:** File names may contain anything except `/` and distinguish between uppercase and lowercase; spaces and a dash at the start cause trouble, so you avoid them.

:::hintergrund Why the slash, of all characters, is forbidden
In a path, the slash separates the names from one another. If a name could contain one itself, the kernel would no longer know whether `a/b` means “the file `b` in the directory `a`” or “the file with the name `a/b`”. The null byte is forbidden because the kernel and most programs use it internally to mark the end of a name. Windows forbids more characters, namely `\ : * ? " < > |`, as well as names such as `CON` or `NUL`, and it does not distinguish between uppercase and lowercase. This matters as soon as files move between the two worlds: under `/mnt/c`, the rules of Windows apply ([Chapter 1, Section 4.5](/wissen/en/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/wsl-2-linux-neben-windows.html#stufe-4-5)), and two Linux files `Brief.txt` and `brief.txt` cannot be stored there side by side.
:::

### Exercises for Section [3](#stufe-3)

<span class="anker" id="stufe-3-8"></span>

:::aufgabe Exercise 7 ★ Reading a line of ls -l
<span class="anker" id="aufg-7"></span>

Read the line `-rw-r--r-- 1 root root 3771 Feb 13 2026 .bashrc` from the example in subsection [3.4](#stufe-3-4): What type of entry is it, to whom does it belong, how big is it, when were its contents last modified and why does it not appear with `ls /etc/skel`?

:::loesung
The first character `-` marks a regular file. It belongs to the user `root` and the group `root`. It is 3771 bytes in size, just under 3.7 KiB. Its contents were last modified on February 13, 2026; because that was more than half a year ago, `ls` shows the year instead of the time of day. It does not appear with `ls /etc/skel` because its name begins with a dot: it is a hidden file, and only `ls -a` or `ls -A` show it.
:::
:::

:::aufgabe Exercise 8 ★★ Hidden files at home
<span class="anker" id="aufg-8"></span>

Compare `ls ~`, `ls -a ~` and `ls -A ~`. How many hidden entries does your home directory have? Which of them come from `/etc/skel`? Which entries does `-a` show in addition to `-A`, and why does every directory have exactly these two?

:::loesung
`ls ~` shows your visible entries, after this chapter for example `linuxk3`. `ls -A ~` also shows the hidden ones, at least `.bash_logout`, `.bashrc` and `.profile`: these are the copies from `/etc/skel` that were made when your account was created. Depending on what you have already used, there are more, such as `.bash_history` with the history from [Chapter 2, Section 5.2](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/schneller-arbeiten-vervollstandigung-verlauf-tastenkurzel.html#stufe-5-2). The number of hidden entries is the number of names with a dot at the start in the output of `ls -A`. `ls -a` additionally shows `.` and `..`. Every directory has exactly these two, because every directory needs a name for itself and one for its parent directory so that relative paths such as `../file` work; in the root, `..` points to the root itself.
:::
:::

:::aufgabe Exercise 9 ★★ The right option
<span class="anker" id="aufg-9"></span>

Which command line shows (a) the entries of `/var/log` with the most recently modified file first, (b) the same entries with the most recently modified one at the end, (c) the information about the directory `/var/log` itself in long format, (d) all entries of `/usr/share/common-licenses` with human-readable sizes, smallest first? Try them out.

:::loesung
(a) `ls -lt /var/log`: the long format, sorted by modification time, newest first. (b) `ls -ltr /var/log`: the same order reversed, with the newest at the end; this is practical, because the interesting part is then directly above the prompt. (c) `ls -ld /var/log`: `-d` shows the directory itself instead of its contents:

```console
$ ls -ld /var/log
drwxrwxr-x 9 root syslog 4096 Nov 10 03:06 /var/log
```

(d) `ls -lhSr /usr/share/common-licenses`: `-S` sorts by size with the largest first, and `-r` reverses that; the file `BSD` at 1.5 KiB is then the first regular file, preceded only by three entries of a few bytes with an arrow (symbolic links, which this chapter explains later), and `GPL-3` is at the bottom. There are no hidden entries in this directory; otherwise, you would add `-A`.
:::
:::

:::aufgabe Exercise 10 ★ Good and bad file names
<span class="anker" id="aufg-10"></span>

Which names are allowed, which cause trouble at the command line and which would you choose for your own files? (a) `einkauf.txt` (b) `Einkauf.TXT` (c) `mein einkauf.txt` (d) `-einkauf.txt` (e) `einkauf/montag.txt` (f) `einkauf_montag.txt`. If (a) and (b) are in the same directory, how many files are there? (`einkauf` is German for “shopping”, `montag` for “Monday”.)

:::loesung
<ol class="al">

<li>

`einkauf.txt` is allowed and a good name.

</li>

<li>

`Einkauf.TXT` is allowed but impractical: you have to type uppercase letters exactly as they are. In the same directory as (a), it is a second, separate file, because Linux distinguishes between uppercase and lowercase; so there are two files.

</li>

<li>

`mein einkauf.txt` is allowed but causes trouble: without quotes, the name becomes two words at the command line.

</li>

<li>

`-einkauf.txt` is allowed, but every command takes it for an option; you need `--` or `./-einkauf.txt`.

</li>

<li>

`einkauf/montag.txt` is not a file name, because the slash is forbidden. Read as a path, it is the file `montag.txt` in the directory `einkauf`.

</li>

<li>

`einkauf_montag.txt` is allowed and a good name: lowercase letters, an underscore instead of a space.

</li>

</ol>

For your own files, (a) and (f) are suitable.
:::
:::

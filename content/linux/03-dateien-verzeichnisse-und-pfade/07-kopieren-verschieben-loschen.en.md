---
title: Copying, moving, deleting
pfad: Computer Science / Linux and the Command Line / Files, Directories and Paths
adresse: informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade
knoten: Chapter 3: Files, Directories and Paths
order: 6080700
summary: You do not only work with files; you also rearrange them: making a backup copy, changing a name, throwing away what is old.
tags: cp, -r, mv, rm, rmdir, pattern
lang: en
---

<span class="anker" id="stufe-6"></span>

:::zweck
You do not only work with files; you also rearrange them: making a backup copy, changing a name, throwing away what is old. This section shows the commands for this, warns about their pitfalls and introduces patterns with which one command affects many files at once. All examples run in the practice directory `~/linuxk3`.
:::

### Copying: cp

<span class="anker" id="stufe-6-1"></span>

Before you rework a file, it is a good idea to keep the old version. For that, you need a second, independent file with the same contents. Figure [21](#abb-21) shows what “independent” means here.

:::abbildung linux/k3cp 21
After `cp einkauf.txt einkauf_alt.txt`, there are two files with the same contents. If one of them is changed afterwards, the other stays as it was: the copy is independent.
:::

:::definition Definition 6.1 (cp)
<span class="anker" id="satz-6-1"></span>

The command __cp__ (short for “copy”) copies a file: `cp source target` creates a new file with the same contents under the name `target`. If `target` is an existing directory, the copy lands in it under the old name. If you name several sources, the last argument must be a directory.
:::

If a file `target` already exists, `cp` overwrites it without asking; its old contents are then lost. The option `-i` (short for “interactive”) makes `cp` ask first; `-v` (short for “verbose”) reports each copy.

::::beispiel A backup copy and a copy into a directory
```console
$ cp einkauf.txt einkauf_alt.txt
$ cp einkauf.txt rezepte
$ ls rezepte
einkauf.txt  kuchen  suppen
$ cp einkauf.txt einkauf_alt.txt neu.txt
cp: target 'neu.txt': No such file or directory
```

The first line creates a copy under a new name, the second a copy in `rezepte` under the old name. The last one fails: with three arguments, `cp` expects the target to be a directory `neu.txt`, and it does not exist.
::::

::::beispiel [Second example] Ask first, then report
```console
$ cp -i einkauf.txt einkauf_alt.txt
cp: overwrite 'einkauf_alt.txt'? n
$ cp -v einkauf.txt einkauf_alt.txt
'einkauf.txt' -> 'einkauf_alt.txt'
```

With `-i`, `cp` asks whether it should overwrite `einkauf_alt.txt`; `n` and Enter leave the file alone, `y` would have overwritten it. Without `-i`, the second command overwrites without comment; `-v` at least says what happened.
::::

⁠**In short:** `cp source target` creates an independent copy and overwrites an existing target without asking; `-i` asks first.

### Copying directories: cp -r

<span class="anker" id="stufe-6-2"></span>

A backup often has to cover a whole directory, with all its subdirectories and files. Without a special option, however, `cp` refuses to touch directories.

:::abbildung linux/k3cpr 22
`cp -r rezepte sicherung` twice in a row (`sicherung` is German for “backup”). The first time, `sicherung` does not exist yet: it is created as a copy of `rezepte`. The second time, `sicherung` already exists: the copy lands inside it as `sicherung/rezepte`.
:::

:::definition Definition 6.2 (cp -r)
<span class="anker" id="satz-6-2"></span>

With the option __-r__ (short for “recursive”), `cp` copies a directory together with everything in it, level by level. If the target does not exist yet, it becomes the copy; if the target is an existing directory, the copy lands in it.
:::

“Recursive” means that `cp` does the same thing again for each subdirectory until no level is left. The behavior at the target follows the same rule as for files and still surprises many people, as Figure [22](#abb-22) shows.

::::beispiel The same line twice
```console
$ cp rezepte sicherung
cp: -r not specified; omitting directory 'rezepte'
$ cp -r rezepte sicherung
$ ls sicherung
einkauf.txt  kuchen  suppen
$ cp -r rezepte sicherung
$ ls sicherung
einkauf.txt  kuchen  rezepte  suppen
```

Without `-r`, `cp` omits the directory and says so. The first `cp -r` creates `sicherung` with the same contents as `rezepte`. The second time, `sicherung` already exists, so another copy lands in it as `sicherung/rezepte`.
::::

⁠**In short:** `cp -r` copies whole directories; if the target already exists, the copy is created inside it.

:::hintergrund What a copy does not take along
A copy gets a new timestamp and belongs to whoever made it. For a backup, this is impractical, because later you want to see when the original was last changed. The option `-a` (short for “archive”) copies recursively like `-r` and keeps the timestamps, the permissions and, as far as allowed, the owner. So if you want to back up a directory, you usually use `cp -a`.
:::

### Moving and renaming: mv

<span class="anker" id="stufe-6-3"></span>

A file is to get a better name or move to another directory. On Linux, both are the same operation, and there is a single command for it. Figure [23](#abb-23) shows why.

:::abbildung linux/k3mv 23
`mv` changes only entries. When renaming, the entry gets a new name; when moving, it disappears from one list and appears in another. The data of the file stay where they are.
:::

:::definition Definition 6.3 (mv)
<span class="anker" id="satz-6-3"></span>

The command __mv__ (short for “move”) gives a file or a directory a new name or a new location: `mv source target` renames `source` to `target`. If `target` is an existing directory, `mv` moves the source into it and keeps its name.
:::

Afterward, the old name no longer exists. `mv` overwrites an existing file `target` without asking, just like `cp`; here, too, `-i` asks first. Unlike `cp`, `mv` needs no option for directories.

::::beispiel Renaming, moving, renaming a directory
```console
$ mv einkauf_alt.txt einkauf_montag.txt
$ mv einkauf_montag.txt sicherung
$ ls
einkauf.txt  fotos  rezepte  sicherung
$ mv sicherung archiv
$ ls -F
archiv/  einkauf.txt  fotos/  rezepte/
```

The first line renames. The second moves, because `sicherung` is a directory. The fourth renames the directory `sicherung` together with its contents to `archiv`, because `archiv` does not exist yet; if there were a directory `archiv`, `sicherung` would land in it.
::::

⁠**In short:** `mv` renames or moves, depending on whether the target is an existing directory; an existing target is replaced without asking.

:::hintergrund Why mv is done instantly
A directory is a list of entries (subsection [1.3](dateien-verzeichnisse-und-der-verzeichnisbaum.html#stufe-1-3)). If you move a file within the same file system ([Chapter 1, Section 5.3](/wissen/en/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/datentrager-abbild-und-prufsumme.html#stufe-5-3)), `mv` does not have to touch any data: it enters the name in the target list and removes it from the old one. There is a single system call for this, and the kernel as a rule carries it out in such a way that even a crash in the middle leaves no half-finished state: afterward, there is either the old name or the new one. That is why a file of many gigabytes is moved just as quickly as an empty one. It is different when the source and the target are in different file systems, for example on two storage devices. Then the kernel cannot move an entry from one list to the other, and `mv` copies the data like `cp -a` and then deletes the original. That takes as long as a copy.
:::

### Deleting: rm

<span class="anker" id="stufe-6-4"></span>

What you no longer need should go. If you come from Windows, you expect a Recycle Bin from which you can retrieve mistakes. On the command line, there is none; Figure [24](#abb-24) compares the two ways.

:::abbildung linux/k3papierkorb 24
Two ways to get rid of a file. At the top, the Trash of a graphical desktop: the file is only moved into a special directory and can be restored. At the bottom, `rm`: the entry disappears from the directory, and there is no way back.
:::

:::definition Definition 6.4 (rm)
<span class="anker" id="satz-6-4"></span>

The command __rm__ (short for “remove”) removes the named files from their directories, immediately and usually without asking. There is no command that undoes this. Without a further option, `rm` leaves directories alone.
:::

`rm -i` asks before each file, `rm -v` reports each deleted one. For Linux, an `rm` without asking is the normal case: whoever types the command is expected to know what they are doing.

:::warnung No trash
What `rm` removes is gone. Before every `rm`, check the name, ideally with `ls` and exactly the same argument; the Tab key prevents typos. Back up important files with `cp` beforehand. Under WSL 2, `rm` under `/mnt/c` also deletes Windows files permanently, bypassing any Windows Recycle Bin.
:::

::::beispiel Deleting a file, and two failed attempts
```console
$ rm rezepte/einkauf.txt
$ rm gibtsnicht.txt
rm: cannot remove 'gibtsnicht.txt': No such file or directory
$ rm archiv
rm: cannot remove 'archiv': Is a directory
```

The copy in `rezepte` has disappeared without any message. `rm` cannot remove a file that does not exist, and it does not touch a directory without an option.
::::

::::beispiel [Second example] With a confirmation prompt
```console
$ rm -i einkauf.txt
rm: remove regular file 'einkauf.txt'? n
```

`rm` names the type of the file, a regular file, and waits. The answer `n` leaves the shopping list where it is.
::::

⁠**In short:** `rm` deletes files immediately and permanently; `rm -i` asks first.

:::hintergrund What the trash of a desktop really is
Graphical desktops on Linux have a trash, too. It is not part of the kernel but a convention between the file managers: moving a file “to the trash” means moving it into the directory `~/.local/share/Trash/files` and writing a small text file with the original path and the time into `~/.local/share/Trash/info`. From this, the file manager can put the file back in its old place. So a trash is an `mv`, not a deletion. `rm` does not know this convention; it really deletes.
:::

### Deleting directories: rmdir and rm -r

<span class="anker" id="stufe-6-5"></span>

Sooner or later, you also want to get rid of directories. There are two ways to do this: a careful one that removes only empty directories and a thorough one that takes everything with it.

:::definition Definition 6.5 (rmdir, rm -r)
<span class="anker" id="satz-6-5"></span>

The command __rmdir__ (short for “remove directory”) removes a directory only if it is empty. `rm` with the option __-r__ removes a directory together with everything in it, level by level and without asking.
:::

The option `-f` (short for “force”) additionally makes `rm` never ask and stay silent about missing files. That is why the line `rm -rf` appears in many instructions, and it is the most dangerous command in this chapter: one wrong path, and a whole subtree is lost.

::::beispiel Removing the archive
```console
$ rmdir archiv
rmdir: failed to remove 'archiv': Directory not empty
$ rm -r archiv
$ mkdir leer
$ rmdir leer
$ ls -F
einkauf.txt  fotos/  rezepte/
```

`rmdir` refuses because `archiv` contains files; `rm -r` removes it with everything in it. `rmdir` removes the freshly created, empty directory `leer` (German for “empty”) without an error message.
::::

⁠**In short:** `rmdir` deletes only empty directories, `rm -r` whole subtrees without asking.

:::warnung rm -r only with a checked path
Before every `rm -r`, have `ls` or `tree` show you what is underneath, and type the path with the Tab key. Never give `rm -r` a path that begins with `/` unless you know exactly why. If you are unsure, use `rm -ri` and answer each question individually.
:::

:::hintergrund Why rmdir deletes only empty directories
Removing a directory can affect far more data than a single file. The system call that removes a directory therefore requires it to be empty, that is, to contain only `.` and `..`; otherwise it fails. `rmdir` is only a thin wrapper around this call. `rm -r`, on the other hand, walks through the tree itself from the bottom up: it first deletes all the files in a directory, then the now empty directory, and so on up to the topmost one. So the safeguard in the kernel remains in place; `rm -r` merely satisfies it by doing the preparatory work itself.
:::

### Patterns for file names

<span class="anker" id="stufe-6-6"></span>

Moving twenty vacation photos into a directory one by one is tedious. It would be nicer to have a command that says: all files that end in `.jpg`. Figure [25](#abb-25) shows how a pattern selects names.

:::abbildung linux/k3muster 25
A pattern selects names from a list. One after another, `*.jpg`, `strand_?.jpg` and `*_[12].jpg` are laid over the six files in `fotos/urlaub/2026`; the matching names light up, the others stay gray.
:::

:::definition Definition 6.6 (File name pattern)
<span class="anker" id="satz-6-6"></span>

A __pattern__ is a word of the command line that contains one of the characters `*`, `?` or `[`. Before the command starts, the shell replaces it with all matching names, sorted by name. Here `*` stands for any sequence of characters, even none, `?` for exactly one arbitrary character, `[abc]` for exactly one of the characters in the brackets, `[0-9]` for exactly one from a range and `[!abc]` for exactly one character that is not in the brackets.
:::

A pattern acts like a sieve through which the names of the directory fall (a picture for orientation). It catches names that begin with a dot only if it begins with a dot itself; so hidden files stay hidden here, too. What matters is who does the work: the shell, not the command. `ls` never gets to see the pattern, only the finished list of names, as if you had typed them one by one. That is why patterns work with every command that takes file names as arguments.

::::beispiel Selecting photos
```console
$ cd fotos/urlaub/2026
$ ls
berg_1.jpg  notiz.txt     strand_10.jpg
berg_2.jpg  strand_1.jpg  strand_2.jpg
$ ls *.jpg
berg_1.jpg  berg_2.jpg  strand_1.jpg  strand_10.jpg  strand_2.jpg
$ ls strand_?.jpg
strand_1.jpg  strand_2.jpg
$ ls strand_*.jpg
strand_1.jpg  strand_10.jpg  strand_2.jpg
$ ls [bn]*
berg_1.jpg  berg_2.jpg  notiz.txt
$ ls *_[12].jpg
berg_1.jpg  berg_2.jpg  strand_1.jpg  strand_2.jpg
$ ls strand_[!1]*
strand_2.jpg
```

`strand_?.jpg` does not match `strand_10.jpg`, because `10` is two characters; `strand_*.jpg` matches it. `[bn]*` selects all names that begin with `b` or `n`. `strand_[!1]*` requires a character after `strand_` that is not a 1.
::::

::::beispiel [Second example] Seeing what the command gets
Because `echo` merely repeats its arguments, it shows the list that the shell has made from a pattern:

```console
$ echo strand_?.jpg
strand_1.jpg strand_2.jpg
$ echo *.txt
notiz.txt
```

`echo` received two arguments, not the pattern. In the same way, you can move all the mountain photos (`berg` is German for “mountain”, `strand` for “beach”) into a directory of their own:

```console
$ mkdir berge
$ mv berg_*.jpg berge
$ ls -F
berge/  notiz.txt  strand_1.jpg  strand_10.jpg  strand_2.jpg
$ cd ~/linuxk3
```

`mv` received three arguments, `berg_1.jpg`, `berg_2.jpg` and `berge`; the last one is a directory, so the two photos move into it.
::::

⁠**In short:** Patterns with `*`, `?` and `[…]` select many names at once; the shell replaces them with the matching names before the command starts.

:::warnung One space too many
If you want to delete all the text files in a directory, you type `rm *.txt`. If a space slips in between `*` and `.txt`, two words result: `*` matches all names in the directory, and `rm` deletes all the files among them before it complains about a missing file `.txt`. So try out a pattern with `ls` or `echo` first; then bring the line back with the Up arrow key and replace only the command with `rm`.
:::

### Exercises for Section [6](#stufe-6)

<span class="anker" id="stufe-6-7"></span>

:::aufgabe Exercise 18 ★ Copy or move?
<span class="anker" id="aufg-18"></span>

The working directory contains the file `brief.txt` and the directory `briefe`, but no file `brief2.txt`. What does each line do, and which names exist afterward? (a) `cp brief.txt brief2.txt` (b) `mv brief.txt briefe` (c) `mv briefe post` (d) `cp briefe kopie` (e) `cp -r briefe kopie`

:::loesung
Each line is considered from the initial state.

<ol class="al">

<li>

An independent copy `brief2.txt` is created; `brief.txt` remains.

</li>

<li>

`briefe` is an existing directory, so `brief.txt` moves into it and is then called `briefe/brief.txt`; the working directory no longer has an entry `brief.txt`.

</li>

<li>

`post` does not exist, so `briefe` is renamed to `post`, contents and all.

</li>

<li>

Nothing happens except for a message: without `-r`, `cp` omits the directory (`-r not specified; omitting directory 'briefe'`).

</li>

<li>

`kopie` does not exist, so `kopie` is created as a complete copy of `briefe`.

</li>

</ol>
:::
:::

:::aufgabe Exercise 19 ★★ Predicting patterns
<span class="anker" id="aufg-19"></span>

A directory contains `bild1.png`, `bild2.png`, `bild10.png`, `Bild3.png`, `bild_a.png` and `text.txt`. Which names does `echo` print for (a) `bild?.png`, (b) `bild*.png`, (c) `[Bb]ild[0-9].png`, (d) `*[!0-9].png`? Check in a directory `muster` of your own, which you remove with `rm -r` afterward.

:::loesung
```console
$ mkdir muster
$ cd muster
$ touch bild1.png bild2.png bild10.png Bild3.png bild_a.png text.txt
$ echo bild?.png
bild1.png bild2.png
$ echo bild*.png
bild1.png bild10.png bild2.png bild_a.png
$ echo [Bb]ild[0-9].png
Bild3.png bild1.png bild2.png
$ echo *[!0-9].png
bild_a.png
$ cd ..
$ rm -r muster
```

(a) `?` requires exactly one character between `bild` and `.png`: `bild10.png` has two there, as does `bild_a.png`, and `Bild3.png` begins with a capital `B`. (b) `*` allows any number of characters; only `Bild3.png` drops out because of the capital `B`. (c) The first bracket allows both spellings, the second exactly one digit; `bild10.png` has two. That `Bild3.png` comes first is due to the sorting: here, uppercase letters come before lowercase letters. (d) What is required is a character that is not a digit, directly before `.png`; that applies only to the `a` in `bild_a.png`.
:::
:::

:::aufgabe Exercise 20 ★★ An image with the wrong extension
<span class="anker" id="aufg-20"></span>

Copy the image `/usr/share/pixmaps/ubuntu-logo-text.png` into your practice directory under the name `urlaub.txt`. What does `file urlaub.txt` report? What harm would `cat urlaub.txt` do, and why? Delete the file afterward.

:::loesung
```console
$ cp /usr/share/pixmaps/ubuntu-logo-text.png urlaub.txt
$ file urlaub.txt
urlaub.txt: PNG image data, 187 x 72, 8-bit/color RGBA, non-interlaced
$ rm urlaub.txt
```

`file` recognizes the PNG image by its first bytes; the extension `.txt` is only part of the name and does not fool it. `cat urlaub.txt` would write the bytes of the image to the terminal. For the terminal, some of them are control commands, and afterward it may show nothing but strange characters until you type `reset` (the caution box in subsection [4.2](dateien-ansehen.html#stufe-4-2)).
:::
:::

:::aufgabe Exercise 21 ★★ A name with a space
<span class="anker" id="aufg-21"></span>

Use `touch` to create a file `mein urlaub.txt`. How does `ls` show it? Then try `rm mein urlaub.txt` and explain both error messages. How do you delete the file correctly? Find two ways of writing it.

:::loesung
```console
$ touch "mein urlaub.txt"
$ ls
 aktuell.txt   fotos              rezepte   verein
 einkauf.txt  'mein urlaub.txt'   urlaub    zettel.txt
$ rm mein urlaub.txt
rm: cannot remove 'mein': No such file or directory
rm: cannot remove 'urlaub.txt': No such file or directory
$ rm "mein urlaub.txt"
```

`ls` puts the name in single quotes so that you can see the space; it indents the other names by one character so that the columns stay aligned. With `rm mein urlaub.txt`, the shell splits the line into three words, and `rm` gets two arguments, `mein` and `urlaub.txt`. Neither of the two files exists, hence the two messages; the intended file remains untouched. The correct way is `rm "mein urlaub.txt"` or `rm mein\ urlaub.txt`; the Tab key also produces the second form.
:::
:::

:::aufgabe Exercise 22 ★★★ One space too many
<span class="anker" id="aufg-22"></span>

Someone wants to delete the contents of `~/projekt` and types `rm -r ~/projekt /*` instead of `rm -r ~/projekt/*`. Without running it, explain which arguments `rm` gets and what would happen if the command ran as `root`. Why does it still cause damage when run as an ordinary user?

:::loesung
The shell replaces `~/projekt` with `/home/student/projekt` and the pattern `/*` with all entries of the root directory: `/bin`, `/boot`, `/dev`, `/etc`, `/home` and so on. So `rm -r` gets the project directory itself and, in addition, every top-level directory as arguments, not the contents of the project. As `root`, the command would delete the entire system: programs, configuration, all home directories, and under WSL 2 even the files on the Windows drive under `/mnt/c`. As an ordinary user, `rm` fails at the system directories, but not everywhere: it deletes `~/projekt` completely, and with the argument `/home`, it descends into `/home/student`, which belongs to you, and deletes the entire contents of your home directory; only the empty directory itself remains, because its entry is in `/home`, which you may not change. Under WSL 2, `/mnt` adds to the damage, because you can usually delete the files under `/mnt/c` as well. A single space thus turns “delete the contents of a directory” into “delete almost everything I am allowed to delete”.
:::
:::

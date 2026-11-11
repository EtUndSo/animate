---
title: Key points so far
pfad: Computer Science / Linux and the Command Line / Files, Directories and Paths
adresse: informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade
knoten: Chapter 3: Files, Directories and Paths
order: 6081200
summary: The directory tree; creating, viewing, copying and deleting files; what lies behind a file name and how to find files again
tags: 
lang: en
---

:::kern Key points so far
<ul>

<li>

A file is a stored sequence of bytes, a directory a list of entries. All directories hang in a single tree with the root `/`; further file systems are mounted on directories instead of getting a drive letter.

</li>

<li>

A path describes a route through the tree: absolute from `/`, relative from the working directory. `.` is the directory itself, `..` the parent directory, `~` the home directory; `pwd` shows your location, `cd` changes it.

</li>

<li>

`ls` shows entries, with `-a` also hidden ones, with `-F` their type, with `-l` type, permissions, link count, owner, size and time, with `-h` human-readable sizes. File names may contain anything except `/` and the null byte and distinguish between uppercase and lowercase.

</li>

<li>

`cat`, `less`, `head`, `tail` and `wc` show and measure text files; `file` determines the type of a file from its first bytes, not from the extension.

</li>

<li>

`mkdir -p`, `touch` and `nano` create; `cp`, `cp -r` and `mv` copy and move, overwriting without asking; `rm`, `rm -r` and `rmdir` delete permanently. The shell replaces patterns with `*`, `?` and `[…]` with matching names before the command starts.

</li>

<li>

The FHS organizes the system: programs in `/usr`, configuration in `/etc`, users in `/home`, variable data in `/var`, temporary files in `/tmp`, devices in `/dev`, information from the kernel in `/proc` and `/sys`.

</li>

<li>

A directory entry connects a name with an inode, which contains all the other information. A hard link is another name for the same inode, a symbolic link a file containing a path; `rm` removes only a name, and the data disappear with the last one.

</li>

<li>

`lsblk`, `findmnt` and `df` show storage devices, mount points and usage; `find` searches by name, type, size and age, and `du` counts the blocks used.

</li>

</ul>
:::

:::merke The answer in three sentences
<ol>

<li>

Linux organizes all files in a single tree in which every location has a path and every additional storage device is mounted on a directory; the FHS defines which directory is for what.

</li>

<li>

With paths and a few commands, you move through this tree, view files, create, copy, move and delete them, select many at once with patterns and find them again with `find`.

</li>

<li>

A file name is just an entry in a directory that points to an inode; from this follow hard and symbolic links, the instant `mv` and the permanent `rm`.

</li>

</ol>
:::

**One principle behind all the results.** Almost everything in this chapter follows from one idea: names and files are separate. A file is an inode with data blocks, a name just an entry in a list that is itself a file, and the whole tree is a network of such lists, connected across storage devices by mounting.

| Result | Where it comes from |
|---|---|
| there are no drive letters | further file systems are mounted on directories of the one tree (Sections [1](dateien-verzeichnisse-und-der-verzeichnisbaum.html#stufe-1) and [9](datentrager-und-einhangen.html#stufe-9)) |
| `cd ..` in `/` stays in `/` | `..` is an entry that, in the root, points to the root itself (Section [2](das-arbeitsverzeichnis-und-pfade.html#stufe-2)) |
| the same relative path leads to different files in two places | the kernel resolves it from the working directory (Section [2](das-arbeitsverzeichnis-und-pfade.html#stufe-2)) |
| a hidden file appears in an ordinary `ls` only after renaming | “hidden” is only a rule for names with a dot (Section [3](den-inhalt-eines-verzeichnisses-anzeigen.html#stufe-3)) |
| `file` recognizes an image even under the name `urlaub.txt` | the type is in the first bytes; the name is just an entry (Section [4](dateien-ansehen.html#stufe-4)) |
| `ls` never gets to see a pattern | the shell replaces it beforehand with names from the directory (Section [6](kopieren-verschieben-loschen.html#stufe-6)) |
| `mv` of a large file is done instantly | it only moves an entry; the inode stays (Sections [6](kopieren-verschieben-loschen.html#stufe-6) and [8](inode-und-links.html#stufe-8)) |
| `/proc/version` has the size 0 and yet has contents | the kernel creates the file only when it is read (Section [7](die-verzeichnisstruktur-von-linux.html#stufe-7)) |
| a directory with two subdirectories has the link count 4 | its entry, its `.` and two `..` point to its inode (Section [8](inode-und-links.html#stufe-8)) |
| after `rm` of the original, the hard link can still be read | `rm` removes only a name; the inode lives until the last one is gone (Section [8](inode-und-links.html#stufe-8)) |
| there is no trash | `rm` calls `unlink`; a trash would be a move (Sections [6](kopieren-verschieben-loschen.html#stufe-6) and [8](inode-und-links.html#stufe-8)) |
| a symbolic link can point nowhere | it contains only a path that nobody checks (Section [8](inode-und-links.html#stufe-8)) |
| no hard link to `/tmp` or `/mnt/c` | inode numbers are valid only within their own file system (Sections [8](inode-und-links.html#stufe-8) and [9](datentrager-und-einhangen.html#stufe-9)) |
| `find . -name *.txt` fails | the shell replaced the pattern before `find` started (Section [10](dateien-finden-und-platz-messen.html#stufe-10)) |
| a file with 32 bytes occupies 4 KiB | the file system allocates space in whole blocks (Section [10](dateien-finden-und-platz-messen.html#stufe-10)) |

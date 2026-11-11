---
title: Storage devices and mounting
pfad: Computer Science / Linux and the Command Line / Files, Directories and Paths
adresse: informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade
knoten: Chapter 3: Files, Directories and Paths
order: 6081000
summary: The one directory tree from Section 1 is assembled from several file systems that are mounted on directories.
tags: lsblk, findmnt, df, /mnt/c
lang: en
---

<span class="anker" id="stufe-9"></span>

:::zweck
The one directory tree from Section [1](dateien-verzeichnisse-und-der-verzeichnisbaum.html#stufe-1) is assembled from several file systems that are mounted on directories. This section shows how to see which storage devices exist, which file system is mounted where and how full it is, and what this means for WSL 2 and the Windows drive. All commands here only read.
:::

:::::vorwissen What you need for this: storage device, file system and mounting

<span class="anker" id="stufe-9-1"></span>

[Chapter 1](/wissen/en/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/ein-linux-zum-ueben.html) introduced the concepts that this section needs. A storage device is a device that stores data permanently, such as an SSD or a USB stick, and it is divided into sectors of usually 512 bytes ([Chapter 1, Section 5.1](/wissen/en/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/datentrager-abbild-und-prufsumme.html#stufe-5-1)). A partition is a contiguous section of a storage device that is treated like a storage device of its own ([Chapter 1, Section 5.2](/wissen/en/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/datentrager-abbild-und-prufsumme.html#stufe-5-2)). A file system is the order according to which files, directories and their administrative information are stored on a storage device or a partition, under Linux usually ext4 ([Chapter 1, Section 5.3](/wissen/en/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/datentrager-abbild-und-prufsumme.html#stufe-5-3)). Finally, mounting means attaching a file system to an existing directory of the tree; this directory is called the mount point, and the contents of the file system appear below it ([Chapter 1, Section 8.1](/wissen/en/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/das-live-system.html#stufe-8-1)).

::::beispiel A USB stick in the tree
A USB stick with a file system on it first appears as a device file, for example `/dev/sdb1` for its first partition. You see its files only when the file system is mounted, on an Ubuntu with a graphical desktop, for example, under `/media/student/STICK`. A file `urlaub.jpg` on the stick then has the path `/media/student/STICK/urlaub.jpg`. Figure [34](#abb-34) shows the process.

:::abbildung linux/k3einhaengen 34
Mounting a USB stick. On the left, the tree before, with the empty directory `/media/student/STICK`; to its right, the file system of the stick with its own root. When the stick is mounted, its root is placed at the directory, and its files appear below it. After unmounting, the directory is empty again.
:::
::::

⁠**In short:** Storage devices carry file systems, and mounted file systems together form the one tree.

:::::

### Showing the storage devices: lsblk

<span class="anker" id="stufe-9-2"></span>

Before asking where a file system is mounted, you want to know which storage devices are connected at all. [Chapter 1, Sections 8.1](/wissen/en/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/das-live-system.html#stufe-8-1) and [9.7](/wissen/en/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/der-live-usb-stick-vorbereiten-schreiben-starten.html#stufe-9-7), used a command for this as a recipe; now you can read its output completely.

:::definition Definition 9.1 (lsblk)
<span class="anker" id="satz-9-1"></span>

The command __lsblk__ (short for “list block devices”) lists the storage devices and their partitions, that is, the device files of type `b`, with size, type and the directories at which their file systems are mounted.
:::

The columns mean: `NAME` the name of the device file in `/dev`; `MAJ:MIN` the two device numbers that `ls -l` also shows; `RM` a 1 for removable storage devices such as USB sticks; `SIZE` the size in units based on 1024; `RO` a 1 for read-only storage devices; `TYPE` `disk` for an entire storage device, `part` for a partition; `MOUNTPOINTS` the mount points.

::::beispiel The storage devices of WSL 2
```console
$ lsblk
NAME MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
sda    8:0    0 388.6M  1 disk
sdb    8:16   0   186M  1 disk
sdc    8:32   0     8G  0 disk [SWAP]
sdd    8:48   0     1T  0 disk /mnt/wslg/distro
                               /
```

`sda` and `sdb` are small, read-only images that WSL itself brings along. `sdc` is the swap space, to which Linux writes parts of main memory when it runs short; it is not mounted but in use as `[SWAP]`. `sdd` is your Ubuntu: 1 TiB in size, as `/sys/block/sdd/size` showed in subsection [7.8](die-verzeichnisstruktur-von-linux.html#stufe-7-8), mounted at `/` and a second time, read-only, for the graphical programs of WSL. There are no partitions here; WSL puts the file system directly on the entire virtual storage device. On an ordinary PC, you would see, for example, `nvme0n1` with the partitions `nvme0n1p1`, `nvme0n1p2` and so on.
::::

⁠**In short:** `lsblk` shows storage devices and partitions with size and mount point.

### What is mounted where: findmnt

<span class="anker" id="stufe-9-3"></span>

`lsblk` shows only storage devices. But the tree also includes file systems without a storage device, such as `/proc` or `/tmp`. To find out for any path in which file system it is located, you need a different tool.

:::definition Definition 9.2 (findmnt)
<span class="anker" id="satz-9-2"></span>

The command __findmnt__ lists the mounted file systems with mount point (`TARGET`), source (`SOURCE`), type (`FSTYPE`) and options (`OPTIONS`). With `-T path`, it names only the file system in which the path is located, with `-t type` only file systems of one type, and with `-o`, you choose the columns.
:::

Without arguments, `findmnt` shows all mounted file systems as a tree; under WSL 2, there are several dozen. The older command `mount` without arguments prints the same list, with one long line for each.

::::beispiel Three paths, three file systems
```console
$ findmnt -T ~ -o TARGET,SOURCE,FSTYPE
TARGET SOURCE   FSTYPE
/      /dev/sdd ext4
$ findmnt -T /mnt/c -o TARGET,SOURCE,FSTYPE
TARGET SOURCE FSTYPE
/mnt/c C:\    9p
$ findmnt -T /tmp -o TARGET,SOURCE,FSTYPE
TARGET SOURCE FSTYPE
/tmp   tmpfs  tmpfs
```

Your home directory is in the ext4 file system on `/dev/sdd`, which is mounted at the root. `/mnt/c` is the Windows drive C:, mounted with the type 9p. `/tmp` is a tmpfs in main memory, without a storage device behind it.
::::

::::beispiel [Second example] All file systems on storage devices
```console
$ findmnt -t ext4,9p -o TARGET,SOURCE,FSTYPE
TARGET                 SOURCE   FSTYPE
/                      /dev/sdd ext4
├─/usr/lib/wsl/drivers drivers  9p
├─/mnt/wslg/distro     /dev/sdd ext4
└─/mnt/c               C:\      9p
```

The lines show under which mount point another one lies: all three are below the root. `/usr/lib/wsl/drivers` passes drivers from Windows through to Linux.
::::

⁠**In short:** `findmnt` shows which file system is mounted at which directory; `findmnt -T path` answers the question for a single path.

:::hintergrund What happens to the contents of the mount point
A mount point is an ordinary directory and may contain files beforehand. When something is mounted there, they are not deleted but hidden: as long as the other file system is mounted, the path of the directory leads to that file system's root, and the old entries are unreachable. After unmounting, they are back. The kernel achieves this when resolving a path (subsection [8.2](inode-und-links.html#stufe-8-2)): it keeps a table of mount points, and when it encounters one of them, it jumps to the root of the mounted file system instead of reading on in the directory's table. That is why you usually choose an empty directory as the mount point.
:::

:::hintergrund How a USB stick gets into the tree
On a Linux with a graphical desktop, a helper program mounts an inserted stick automatically, usually under `/media/<user>/<name of the stick>`. By hand, you need administrator privileges for this: `sudo mount /dev/sdb1 /mnt` mounts the first partition of the stick at `/mnt`, and `sudo umount /mnt` unmounts it again. Unmounting before unplugging is important: Linux often writes changes to the storage device only after some delay, and only on unmounting is it certain that everything has arrived. Under WSL 2, USB sticks do not appear as storage devices in Linux ([Chapter 1, Section 4.8](/wissen/en/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/wsl-2-linux-neben-windows.html#stufe-4-8)); there, their files are easiest to work with from Windows.
:::

### How full a file system is: df with paths

<span class="anker" id="stufe-9-4"></span>

[Chapter 2, Section 6.5](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/das-system-erkunden.html#stufe-6-5) used `df -h /` to show how much space is free on the system's storage device. With what you now know about mounted file systems, you can ask the same question for any place in the tree. Figure [35](#abb-35) shows which file systems make up the tree under WSL 2.

:::abbildung linux/k3wslbaum 35
The tree of WSL 2, assembled from three file systems: the ext4 file system on `/dev/sdd` as the base, the tmpfs at `/tmp` in main memory and Windows drive C: at `/mnt/c`. Each subtree is shaded in the color of its file system.
:::

:::definition Definition 9.3 (df with paths)
<span class="anker" id="satz-9-3"></span>

If __df__ receives paths as arguments, it shows for each path the file system in which it is located, with size, used and free space. The option `-T` adds the type of the file system.
:::

So for a path, what counts is not where it stands in the tree, but which file system it is on. Two directories right next to each other can be on different storage devices and have different amounts of space.

::::beispiel Space in three places
```console
$ df -hT ~ /tmp /mnt/c
Filesystem     Type   Size  Used Avail Use% Mounted on
/dev/sdd       ext4  1007G  4.2G  952G   1% /
tmpfs          tmpfs   16G     0   16G   0% /tmp
C:\            9p     475G  319G  156G  68% /mnt/c
```

The home directory has 952 GiB free, `/tmp` only 16 GiB, because it lives in main memory and may occupy at most half of it. For `/mnt/c`, `df` reports the usage of the Windows drive. That the file system on `/dev/sdd` is only 1007 GiB in size instead of 1024 is due to its own administrative data, which occupy part of the storage device; for the free space, the reserve for `root` from [Chapter 2, Section 6.5](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/das-system-erkunden.html#stufe-6-5) is subtracted as well.
::::

⁠**In short:** `df -hT path` shows the type, size and free space of the file system in which a path is located.

### The Windows drive under WSL 2: /mnt/c

<span class="anker" id="stufe-9-5"></span>

Under WSL 2, the tree includes a file system that is not in Linux at all: the Windows drive C:. In several respects, it behaves differently from the rest of the tree.

:::abbildung linux/k3grenze 36
Boundaries between file systems. A hard link from `/home/student` to `/tmp` or `/mnt/c` bounces off the boundary; a symbolic link crosses it, because it contains only a path; `mv` across the boundary turns into copying and deleting.
:::

:::definition Definition 9.4 (/mnt/c under WSL 2)
<span class="anker" id="satz-9-4"></span>

Under WSL 2, the Windows drive C: is mounted at __/mnt/c__, as a file system of type 9p. Every access to it is passed on as a request to a file server in Windows, which reads or writes the file on the Windows drive.
:::

From this follow the quirks that [Chapter 1, Sections 4.5](/wissen/en/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/wsl-2-linux-neben-windows.html#stufe-4-5) and [4.7](/wissen/en/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/wsl-2-linux-neben-windows.html#stufe-4-7) already mentioned. Accesses are slower, especially with many small files, because each request travels between Linux and Windows. The Windows rules for names apply, and uppercase and lowercase are not distinguished. And because `/mnt/c` is a file system of its own, the limits from this chapter apply: a hard link from your home directory to it is impossible, and `mv` between the two copies and deletes instead of just moving an entry. Figure [36](#abb-36) summarizes the boundaries.

::::beispiel How to recognize the boundary
Whether two paths are in the same file system is revealed by `findmnt -T` or `df`: if the column `TARGET` or `Mounted on` shows a different mount point, there is a boundary between them. For `~` and `/mnt/c`, the example in subsection [9.4](#stufe-9-4) showed the mount points `/` and `/mnt/c`. A hard link from `~/linuxk3/einkauf.txt` to `/mnt/c` must therefore fail for the same reason as the one to `/tmp` in subsection [8.7](inode-und-links.html#stufe-8-7).
::::

⁠**In short:** Under WSL 2, `/mnt/c` is a file system of its own with the rules of Windows; for Linux work, everything belongs in the home directory.

### Exercises for Section [9](#stufe-9)

<span class="anker" id="stufe-9-6"></span>

:::aufgabe Exercise 31 ★ Reading an output of lsblk
<span class="anker" id="aufg-31"></span>

Among other things, `lsblk` on a laptop shows the line `nvme0n1 259:0 0 476.9G 0 disk`, below it `nvme0n1p1 259:1 0 260M 0 part /boot/efi` and `nvme0n1p2 259:2 0 476.6G 0 part /`, and also `sda 8:0 1 7.5G 0 disk` with `sda1 8:1 1 7.5G 0 part /media/mira/STICK`. How many storage devices and how many partitions are there? Which storage device is removable? Where do the stick's files appear in the tree?

:::loesung
There are two storage devices with `TYPE disk`: `nvme0n1` with 476.9 GiB and `sda` with 7.5 GiB. In addition, there are three partitions: `nvme0n1p1`, `nvme0n1p2` and `sda1`. `sda` is removable, as the 1 in the column `RM` shows; it is a USB stick. Its only partition is mounted at `/media/mira/STICK`, so its files are there, for example `/media/mira/STICK/urlaub.jpg`. The large partition `nvme0n1p2` is mounted at the root and holds the system.
:::
:::

:::aufgabe Exercise 32 ★★ Which file system?
<span class="anker" id="aufg-32"></span>

Use `findmnt -T path -o TARGET,SOURCE,FSTYPE` to determine for `/proc`, `/home/student/linuxk3`, `/tmp` and `/usr/bin` in which file system each is located. Which of them are on a storage device, and which are not? Between which of the four places is a hard link possible?

:::loesung
`/home/student/linuxk3` and `/usr/bin` are both in the ext4 file system on `/dev/sdd`, which is mounted at `/` (example in subsection [9.3](#stufe-9-3)). `/tmp` is a tmpfs in main memory, `/proc` a virtual file system without a storage device:

```console
$ findmnt -T /proc -o TARGET,SOURCE,FSTYPE
TARGET SOURCE FSTYPE
/proc  proc   proc
```

So only the first two are on a storage device. A hard link is technically possible only between `/home/student/linuxk3` and `/usr/bin`, because only these two are in the same file system. You still cannot create one: an ordinary user may not create entries in `/usr/bin`, and in its default setting, Ubuntu also forbids hard links to files that belong to another user and that you may not both read and write.
:::
:::

:::aufgabe Exercise 33 ★★ Hard no, symbolic yes
<span class="anker" id="aufg-33"></span>

`ln einkauf.txt /tmp/einkauf.txt` failed in subsection [8.7](inode-und-links.html#stufe-8-7). Would `ln -s ~/linuxk3/einkauf.txt /tmp/einkauf.txt` work? Justify your answer with what the new file would contain. On the test system, what would have happened to the link after a restart, and what to the shopping list?

:::loesung
Yes. The symbolic link would be a new small file in `/tmp` whose contents are the text `/home/student/linuxk3/einkauf.txt`; the shell has replaced the tilde beforehand. A path may cross any boundary between file systems, because it is resolved only when it is accessed. On the test system, `/tmp` is in main memory; after a restart, the link would therefore be gone, but the shopping list would be untouched, because a symbolic link is not a connection that its target knows about. The chapter did not create this link so as not to change anything outside the practice directory.
:::
:::

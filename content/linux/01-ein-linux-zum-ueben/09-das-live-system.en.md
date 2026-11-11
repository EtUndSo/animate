---
title: The live system
pfad: Computer Science / Linux and the Command Line / A Linux to Practice On: WSL, Virtual Machine, Live USB Stick
adresse: informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick
knoten: Chapter 1: A Linux to Practice On: WSL, Virtual Machine, Live USB Stick
order: 6060900
summary: A Linux that starts from a USB stick does not use the built-in SSD, and yet you can create files and try out programs in it.
tags: Mounting, mount point, live system, squashfs, tmpfs, overlay, persistence
lang: en
---

<span class="anker" id="stufe-8"></span>

:::zweck
A Linux that starts from a USB stick does not use the built-in SSD, and yet you can create files and try out programs in it. This section explains how this works: the system is in a write-protected image, and everything that changes ends up in a layer in main memory. It also follows from this why everything is gone after switching off.
:::

:::::vorwissen What you need for this: mounting

<span class="anker" id="stufe-8-1"></span>

Subsection [4.5](wsl-2-linux-neben-windows.html#stufe-4-5) showed that Linux arranges all files in a single tree with the root directory `/` and shows drive C: of Windows under `/mnt/c`. How do the contents of a storage device get to a place in this tree?

:::definition Definition 8.1 (Mounting, mount point)
<span class="anker" id="satz-8-1"></span>

__Mounting__ means making a file system visible at a place in the directory tree: from then on, the folder at this place shows the contents of the file system. The folder is called the __mount point__. Programs do not use a file system that is not mounted anywhere; they do not read or write any files there.
:::

::::beispiel The storage devices in WSL 2
The command `lsblk` lists the storage devices that the kernel sees, with their size and their mount point:

```console Linux (WSL 2)
$ lsblk -o NAME,SIZE,TYPE,MOUNTPOINTS
NAME   SIZE TYPE MOUNTPOINTS
sda  388.6M disk
sdb    186M disk
sdc      8G disk [SWAP]
sdd      1T disk /mnt/wslg/distro
                 /
```

Linux names storage devices `sda`, `sdb` and so on. All four are virtual hard disks of the WSL 2 VM. The file system on `sdd`, the ext4 file from subsection [4.6](wsl-2-linux-neben-windows.html#stufe-4-6), is mounted at the root directory `/` and additionally at a second place; it contains the whole of Ubuntu. `sda` and `sdb` have no mount point in Ubuntu; WSL needs them for its own purposes outside the distribution. `sdc` contains no file system: `[SWAP]` stands for an area to which the kernel can move parts of main memory, and the kernel uses it without mounting. Drive C: is not in the list, because it is not a storage device of the VM; it comes from the Windows side via the file server from Figure [8](wsl-2-linux-neben-windows.html#abb-8) and is mounted under `/mnt/c`.
::::

⁠**In short:** A file system is mounted at a folder; no program uses what is not mounted anywhere.

:::::

### The live system

<span class="anker" id="stufe-8-2"></span>

A Linux should start from the stick, be fully usable and not touch the internal SSD. Still, you should be able to create files, and the system should appear fresh again after every start.

Figure [11](#abb-11) shows how a live system achieves this: with two layers that the system places one on top of the other.

:::abbildung linux/k1live 11
The layers of a live system. At the bottom is the system as a compressed, write-protected image from the stick, above it a writable layer in main memory. Together, they result in the directory tree that the programs see. The internal SSD is not mounted.
:::

:::definition Definition 8.2 (Live system)
<span class="anker" id="satz-8-2"></span>

A __live system__ is an operating system that starts and runs entirely from a removable storage device without mounting the computer's built-in storage devices. Its system is stored write-protected on the removable storage device; all changes during the session end up in main memory.
:::

::::beispiel Trying Ubuntu
If you start an Ubuntu stick and choose “Try Ubuntu” in the installer, Ubuntu runs as a live system. You can browse the web, create files and use the terminal. The SSD with Windows remains untouched, and after a restart without the stick, Windows starts as before.
::::

⁠**In short:** A live system runs from the stick and from main memory and leaves the internal SSD alone.

### The compressed image: squashfs

<span class="anker" id="stufe-8-3"></span>

A complete Ubuntu with a browser, office programs and drivers takes up many gigabytes. So that it fits on a stick and is read quickly, it is stored compressed in a file.

:::definition Definition 8.3 (squashfs)
<span class="anker" id="satz-8-3"></span>

__squashfs__ is a file system that stores its entire contents compressed in a single file and can only be read, not written to. It is created once, when the image is built.
:::

::::beispiel squashfs on the Ubuntu stick
In the Ubuntu image, the system is stored in squashfs files in the folder `casper`. At startup, the live system mounts them, and from then on, it reads every program you start from the compressed image, unpacked piece by piece in main memory. Nothing in it can be changed.
::::

⁠**In short:** squashfs is a compressed file system that can only be read.

:::hintergrund Why a compressed file system is write-protected
The reason lies in its structure. squashfs compresses the files in blocks, by default of 128 KiB each, and stores the compressed blocks one after the other without gaps. How much space a block then needs depends on its contents. If you change a few bytes in a file, its compressed block almost always becomes longer or shorter. Then it no longer fits in its old place, and all the following blocks, together with the references to them, would have to be moved. A file system that is never changed, on the other hand, can afford the densest arrangement, and that is exactly what you need for a system that is supposed to fit on a stick and remain unchanged. Writable file systems with compression exist too; for this, they leave space free between the blocks or write changed blocks to a new place and manage the space in a correspondingly more complex way.
:::

### A file system in main memory: tmpfs

<span class="anker" id="stufe-8-4"></span>

If the system itself cannot be written to and the SSD is off-limits, a live system needs another place for everything that changes: new files, changed settings, logs.

:::definition Definition 8.4 (tmpfs)
<span class="anker" id="satz-8-4"></span>

__tmpfs__ is a file system whose files are in main memory. It can be read and written to like any other file system. Its contents disappear as soon as it is unmounted or the computer is switched off.
:::

::::beispiel tmpfs in WSL
An ordinary Linux also uses tmpfs, for example for files that are needed only until the next restart. In WSL 2, for example, the folder `/run` is a tmpfs. How much main memory a tmpfs may take up at most is set when it is mounted; but it takes up only as much as its files actually need.
::::

⁠**In short:** tmpfs is a file system in main memory, writable and volatile.

### Two layers on top of each other: the overlay

<span class="anker" id="stufe-8-5"></span>

Now the live system has two file systems: the system in the squashfs, which can only be read, and an empty tmpfs, which can be written to. But the programs should see a single directory tree that contains the system and in which you can nevertheless change everything.

:::definition Definition 8.5 (Overlay)
<span class="anker" id="satz-8-5"></span>

An __overlay__ places two file systems on top of each other and shows them as one: a lower, read-only layer and an upper, writable layer. When a file is read, it first looks in the upper layer and, if the file is missing there, in the lower one. If a file of the lower layer is to be changed, it first copies the file to the upper layer and changes the copy there. If a file of the lower layer is deleted, it enters a marker in the upper layer that hides the file. The lower layer remains unchanged in every case.
:::

::::beispiel Three files in the live system
The lower layer is the squashfs of the system, the upper one a tmpfs. (1) You create the new file `notiz.txt`: it is created only in the upper layer. (2) You change a settings file of the system: the overlay copies it from the squashfs to the tmpfs and changes the copy; from now on, all programs see the changed version, because the upper layer takes precedence. (3) You delete a file of the system: a marker is created in the upper layer, and the file can no longer be seen, although it is still present in the squashfs. After a restart, the tmpfs is empty, and all three changes have disappeared.
::::

⁠**In short:** The overlay shows a read-only and a writable layer as one tree; all changes end up at the top.

:::hintergrund Who assembles the layers at startup
When the boot loader starts the kernel, it additionally loads a small file system into main memory, the *initramfs*. In it runs a program that builds the layers before the actual system starts; in Ubuntu, it is called `casper`. It searches for the storage device on which the live system is located, mounts its squashfs files, creates a tmpfs and combines both into an overlay. It makes this overlay the root directory `/` of the system and hands over to the first program of the actual system. For all programs that start afterward, the live system looks like an ordinarily installed Linux.
:::

### What happens when you switch off

<span class="anker" id="stufe-8-6"></span>

The behavior of a live system when it is switched off follows directly from the layers. The upper layer is in main memory, and main memory loses its contents without power. The lower layer was never changed. At the next start, the system is therefore exactly as it is on the stick.

::::beispiel A file that does not survive the restart
For this chapter, a very small live system, Alpine Linux version 3.24, was started from its image in a test VM. The list of mounted file systems shows the layers: the boot medium with its ISO file system, read-only (`ro`), the root directory `/` as a tmpfs, and part of the system as a squashfs, also read-only:

```console Alpine Linux, live system in a test VM
# mount | grep -E ' on / |/media/|modloop'
/dev/sda on /media/sda type iso9660 (ro,relatime,nojoliet,check=s,map=n,blocksize=2048,iocharset=utf8)
tmpfs on / type tmpfs (rw,relatime,mode=755,inode64)
/dev/loop0 on /.modloop type squashfs (ro,relatime,errors=continue)
# echo 'Notiz aus der Live-Sitzung' > /root/notiz.txt
# cat /root/notiz.txt
Notiz aus der Live-Sitzung
```

Here, the character `#` at the beginning of the line is the prompt, because in this test VM you work as the administrator. In the same session, the program `lsblk` was also installed afterward from the internet. After a restart of the VM, both are gone:

```console Alpine Linux, after the restart
# cat /root/notiz.txt
cat: can't open '/root/notiz.txt': No such file or directory
# lsblk
-sh: lsblk: not found
```
::::

Alpine puts the whole system into a tmpfs at startup and mounts only part of it as a squashfs; Ubuntu, on the other hand, as described in subsection [8.5](#stufe-8-5), places a tmpfs as an overlay over its squashfs files. The result is the same: everything that changes during the session is in main memory. The same applies to programs that you install afterward in the live system: they also end up in main memory and are gone after the restart.

⁠**In short:** After switching off, everything you changed in the live system is gone, and every start is fresh again.

### Persistence

<span class="anker" id="stufe-8-7"></span>

That a live system forgets everything is usually an advantage. But if you work with the same stick regularly, you sometimes want to keep your files and settings.

:::definition Definition 8.6 (Persistence)
<span class="anker" id="satz-8-6"></span>

For a live system, __persistence__ means that it stores changes not in main memory but in an additional storage area on the stick, so that they survive the restart. In Ubuntu, this is a partition or file labeled `casper-rw`, which the live system uses as the upper layer when it is started with the boot option `persistent`.
:::

::::beispiel Persistence with Rufus
The Windows program Rufus, with which you write images to USB sticks, offers a slider for the size of such a persistence partition when writing an Ubuntu stick. Ubuntu's guides do not describe this; Rufus itself has had to fix the function repeatedly for individual Ubuntu releases. Whether it works reliably with Ubuntu 26.04 is not certain.
::::

⁠**In short:** Persistence turns the stick into a system that remembers, but in Ubuntu, it is a poorly maintained add-on.

:::hintergrund Why a VM is better for permanent work
With persistence, the stick loses exactly the properties that distinguish a live system: it is no longer fresh at every start, and an error persists. In addition, all files are stored unencrypted on the stick, and if you lose it, you expose them to anyone who finds it. A USB stick is also neither fast nor durable for many small write operations. If you need a Linux for permanent work, you are better served by WSL 2 or a VM; the live stick is there for trying things out and for a clean restart.
:::

### Exercises for Section [8](#stufe-8)

<span class="anker" id="stufe-8-8"></span>

:::aufgabe Exercise 23 ★ What survives the restart?
<span class="anker" id="aufg-23"></span>

You are working in the Ubuntu live system without persistence. Which of the following is still there at the next start from the same stick? (a) A bookmark in the browser, (b) a file that you saved in your home folder, (c) a file that you saved on a second USB stick, (d) a file that you uploaded to your cloud storage, (e) a program that you installed afterward. Justify each answer with the layers.

:::loesung
(a) Gone. The bookmark is stored in a file in the home folder, that is, in the upper layer in main memory. (b) Gone, for the same reason. (c) Still there. The second stick is a separate storage device that you mounted and wrote to directly; it does not belong to the overlay. (d) Still there. The file is on a server on the internet. (e) Gone. The program's files were written to the upper layer; the squashfs on the stick is unchanged.
:::
:::

:::aufgabe Exercise 24 ★★ Tracing the overlay
<span class="anker" id="aufg-24"></span>

The lower layer of an overlay contains the files `a`, `b` and `c`; the upper layer is empty. The following happens in sequence: `a` is changed, `b` is deleted, `d` is newly created, `d` is changed. What is then in the upper layer, what is in the lower one, and which files do the programs see? What do they see after a restart?

:::loesung
Step by step:

<ul>

<li>

Changing `a`: The overlay copies `a` to the upper layer and changes the copy there.

</li>

<li>

Deleting `b`: A marker is created in the upper layer that hides `b`.

</li>

<li>

Creating `d`: `d` is created only in the upper layer.

</li>

<li>

Changing `d`: The file is already in the upper layer and is changed there; no copy is needed.

</li>

</ul>

Afterward, the upper layer contains the changed copy of `a`, the marker for `b` and the changed file `d`. The lower layer contains `a`, `b` and `c`, unchanged. The programs see `a` in the changed version, `c` and `d`; they do not see `b`. After a restart, the upper layer is empty: The programs again see `a` in the original version, `b` and `c`, and `d` does not exist.
:::
:::

:::aufgabe Exercise 25 ★ When main memory becomes full
<span class="anker" id="aufg-25"></span>

A computer with 8 GB of memory is running the live system. You download a 5 GB file into your home folder. Why can the live system get into difficulties in the process, although the USB stick still has space and the internal SSD has 300 GB free?

:::loesung
The home folder is in the overlay, and everything you save there ends up in the upper layer, that is, in the tmpfs in main memory. The 5 GB of the downloaded file therefore occupy 5 GB of main memory, in addition to what the running system, the browser and the download itself need. With 8 GB, main memory becomes scarce or runs full, or the tmpfs reaches the maximum size that was set when it was mounted. Then the download aborts with an error, or the whole system becomes sluggish.

The free space on the stick does not help, because the live system without persistence writes nothing there; the lower layer is read-only. The free space on the SSD does not help, because the SSD is not mounted. In the live system, you therefore save large files on a second USB stick or upload them directly to cloud storage.
:::
:::

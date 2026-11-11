---
title: The directory structure of Linux
pfad: Computer Science / Linux and the Command Line / Files, Directories and Paths
adresse: informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade
knoten: Chapter 3: Files, Directories and Paths
order: 6080800
summary: In / , there are a good twenty directories with short, puzzling names.
tags: Filesystem Hierarchy Standard, /usr, library, /etc, /home, /root, /var, log files
lang: en
---

<span class="anker" id="stufe-7"></span>

:::zweck
In `/`, there are a good twenty directories with short, puzzling names. They follow a plan that is the same on almost all Linux systems. If you know it, you know on any unfamiliar system where the programs, the configuration and the logs are. This section goes through the most important directories.
:::

### The standard for the directory structure

<span class="anker" id="stufe-7-1"></span>

For programs to find their parts on every Linux, all distributions have to agree on fixed locations. This agreement is written down.

:::abbildung linux/k3fhs 26
The top level of the directory tree, colored by purpose: programs and libraries (`/usr`, `/opt`), configuration (`/etc`), users (`/home`, `/root`), variable data (`/var`, `/tmp`), booting (`/boot`), mount points (`/mnt`, `/media`) and directories that the kernel creates (`/dev`, `/proc`, `/sys`, `/run`).
:::

:::definition Definition 7.1 (Filesystem Hierarchy Standard)
<span class="anker" id="satz-7-1"></span>

The __Filesystem Hierarchy Standard__, FHS for short, specifies which directories a Linux system should have and which kind of files belongs in which of them. The current version, 3.0, appeared in 2015; today it is maintained by freedesktop.org, a joint project of open source developers.
:::

The major distributions largely follow it, though not always in every detail. Table [2](#tab-2) lists the top-level directories; Figure [26](#abb-26) arranges them by purpose.

<span class="anker" id="tab-2"></span>

**Table 2:** The top-level directories according to the FHS.

| Directory | Contents |
|---|---|
| `/usr` | Programs, libraries and data that come with the system |
| `/etc` | Configuration of the whole system, almost exclusively text files |
| `/home` | Home directories of the users |
| `/root` | Home directory of `root` |
| `/var` | Data that change during operation, such as logs in `/var/log` |
| `/tmp` | Temporary files, writable for everyone |
| `/boot` | Kernel and files for booting the system |
| `/dev` | Devices as files |
| `/proc`, `/sys` | Information from the kernel about running programs and devices |
| `/run` | Information since the last boot, in main memory |
| `/mnt`, `/media` | Mount points for further storage devices |
| `/opt` | Add-on programs that are not part of the distribution |
| `/srv` | Data for services that the computer offers to others |
| `/bin`, `/sbin`, `/lib` | Formerly separate directories for the most important programs and libraries; today found under `/usr` |

::::beispiel A tour with a few commands
For a tour, `cd`, `ls -l`, `file` and `less` are enough: change into a directory, look at the entries, check the type of an interesting file and read a text file. You cannot destroy anything along the way, because as an ordinary user, you may only read in the system's directories. Where even that is forbidden, Linux reports “Permission denied”, and you simply move on.
::::

⁠**In short:** The FHS specifies which directory is there for what; that is why all Linux systems look alike in their basic outline.

### Programs and libraries: /usr

<span class="anker" id="stufe-7-2"></span>

The largest part of a Linux system is the programs it comes with. They are collected in one subtree.

:::definition Definition 7.2 (/usr)
<span class="anker" id="satz-7-2"></span>

The directory __/usr__ contains the programs, libraries and unchanging data that come with the distribution. The programs are in `/usr/bin`, programs for system administration in `/usr/sbin`, libraries in `/usr/lib` and data such as manual pages and documentation in `/usr/share`.
:::

A __library__ is a file with program parts that many programs share instead of each containing them itself. You know `/usr/bin` as the location of the program files from [Chapter 2, Section 3.1](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/arten-von-befehlen.html#stufe-3-1); on the test computer, it holds more than a thousand entries. Two further locations are intended for software that does not come from the distribution: `/usr/local` for programs that the system administrator installs by hand, and `/opt` for larger add-on programs, often from companies, that bring everything along in a subdirectory of their own.

::::beispiel Where the manual pages are
```console
$ ls /usr/share/man
ar  de  fr  id  ko    man3  man6  nl  pt_BR  sk  sv  zh
cs  es  hr  it  man1  man4  man7  pl  ro     sl  tr  zh_CN
da  fi  hu  ja  man2  man5  man8  pt  ru     sr  uk  zh_TW
```

`man1` to `man8` are the eight sections of the manual from [Chapter 2, Section 4.5](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/hilfe-finden.html#stufe-4-5); the other directories contain translations, `de`, for example, the German ones.
::::

⁠**In short:** Under `/usr` is everything that the distribution brings along in programs and fixed data; your own add-on software belongs in `/usr/local` or `/opt`.

:::hintergrund Why fixed and variable data are kept separate
The FHS sorts files by two questions. First: do they change during operation? Programs and manual pages change only when someone installs new software; they are called static. Logs, queues and intermediate results change constantly; they are called variable. Second: could several computers share them? A program is the same on every computer, the configuration of one particular computer is not. The division follows from both questions:

|  | shareable | tied to one computer |
|---|---|---|
| static | `/usr`, `/opt` | `/etc`, `/boot` |
| variable | `/var/mail` | `/var/run`, `/var/lock` |

The benefit: `/usr` can be on a write-protected storage device or be provided over the network for many computers, and a backup mainly has to cover `/etc`, `/home` and parts of `/var`.
:::

### Configuration: /etc

<span class="anker" id="stufe-7-3"></span>

Every system is set up a little differently: a different host name, a different time zone, different users. These differences are kept in a single place.

:::definition Definition 7.3 (/etc)
<span class="anker" id="satz-7-3"></span>

The directory __/etc__ contains the configuration that applies to the whole system. Almost all files in it are text files that you can read and, with administrator privileges, change in a text editor.
:::

You already know three files from `/etc`: `/etc/hostname` with the host name, `/etc/timezone` with the time zone and `/etc/passwd` with the list of users. Many programs have a file of their own in `/etc`, whose name often ends in `.conf`, or a subdirectory of their own.

::::beispiel Finding configuration files
With a pattern from subsection [6.6](kopieren-verschieben-loschen.html#stufe-6-6), you find files with a common beginning:

```console
$ ls /etc/h*
/etc/host.conf  /etc/hostname  /etc/hosts
```

Besides `hostname`, there is `hosts`, a list of host names and their addresses on the network, and `host.conf`, which controls how names are looked up. All three are text files; `less` shows them.
::::

⁠**In short:** `/etc` is the place for the configuration of the whole system, in the form of text files.

### The users: /home and /root

<span class="anker" id="stufe-7-4"></span>

The personal files of the people who use a computer do not belong among the programs. They get a subtree of their own.

:::definition Definition 7.4 (/home, /root)
<span class="anker" id="satz-7-4"></span>

The directory __/home__ contains a home directory for each ordinary user, named after that user. The home directory of `root` is kept apart from it in __/root__.
:::

Because `/root` is directly under the root directory, the administrator can reach their files even when `/home` is on a separate storage device that is not mounted at the moment. Other users' home directories are usually not readable, or only to a limited extent.

::::beispiel Who lives here?
```console
$ ls /home
student
$ ls /root
ls: cannot open directory '/root': Permission denied
```

On the test computer, there is a single ordinary user. This user may not look into `/root`.
::::

⁠**In short:** The users live in `/home/<name>`, `root` lives in `/root`.

### Variable data: /var and the logs

<span class="anker" id="stufe-7-5"></span>

While the system is running, data are created all the time: programs record what they have done, queues fill up, intermediate results are stored. These data need a place that is allowed to grow.

:::definition Definition 7.5 (/var, log file)
<span class="anker" id="satz-7-5"></span>

The directory __/var__ (short for “variable”) contains data that change while the system is running. An important part of it is `/var/log` with the __log files__: files to whose end a program continuously writes what happens, each entry with the date and time.
:::

Because new entries are always appended at the bottom, you usually read a log from the end with `tail`: the last lines are the most recent. Some logs only `root` may read, because they contain information about logins and other sensitive events.

::::beispiel Looking into the log of software installations
```console
$ ls /var/log
README            chrony        dmesg.3.gz      landscape
alternatives.log  dist-upgrade  dmesg.4.gz      lastlog
apt               dmesg         dpkg.log        private
auth.log          dmesg.0       fontconfig.log  syslog
bootstrap.log     dmesg.1.gz    journal         unattended-upgrades
btmp              dmesg.2.gz    kern.log        wtmp
$ tail -n 3 /var/log/dpkg.log
2026-11-09 16:35:28 status config-files ubuntu-helper-virt-hwe:all 1:10.2.1+ds-1ubuntu4.4
2026-11-09 16:35:28 status not-installed ubuntu-helper-virt-hwe:all <none>
2026-11-09 16:35:28 startup packages configure
```

`dpkg.log` is written by the program that installs and removes software on Ubuntu. Each line begins with the date and time. Files with the extension `.gz` are older, compressed logs that take up less space.
::::

⁠**In short:** `/var` takes in everything that changes during operation; the logs are in `/var/log`.

### Temporary files: /tmp

<span class="anker" id="stufe-7-6"></span>

Many programs briefly need a file, for example for an intermediate result that nobody needs once they have finished. There is a shared place for this.

:::definition Definition 7.6 (/tmp)
<span class="anker" id="satz-7-6"></span>

The directory __/tmp__ is intended for temporary files. Every user may create files there; when the system restarts, the contents may disappear.
:::

On the test system, Ubuntu 26.04 under WSL 2, `/tmp` is in main memory, as a file system of type tmpfs ([Chapter 1, Section 8.4](/wissen/en/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/das-live-system.html#stufe-8-4)); when the computer is switched off, the contents are gone. Other systems put `/tmp` on the storage device and empty it at boot. Files that are to survive a restart belong in `/var/tmp`. Your own files that you want to keep go in neither place but in your home directory.

::::beispiel Two directories for temporary files
```console
$ ls -ld /tmp /var/tmp
drwxrwxrwt 7 root root  140 Nov 10 02:42 /tmp
drwxrwxrwt 5 root root 4096 Nov 10 02:42 /var/tmp
```

Both belong to `root`, and the permissions end in a `t` instead of an `x`; this has to do with the fact that everyone may write there. The size of `/tmp` is not 4096 but 140: a file system in main memory calculates the size of a directory differently from one on a storage device.
::::

⁠**In short:** `/tmp` is a shared place for short-lived files; what is to stay belongs in the home directory.

### Devices as files: /dev

<span class="anker" id="stufe-7-7"></span>

Programs have to talk to devices: to hard disks, to the terminal, to random number generators. On Linux, they need no special commands for this; devices look like files, as Figure [27](#abb-27) shows.

:::abbildung linux/k3dev 27
Device files are doors to the kernel. A program reads from `/dev/zero`, `/dev/urandom` or `/dev/sdd` by the same means as from a regular file; behind the door, however, what answers is not stored contents but a driver in the kernel.
:::

:::definition Definition 7.7 (Device file)
<span class="anker" id="satz-7-7"></span>

A __device file__ is an entry in the directory tree behind which there are no stored contents but a device that a driver in the kernel manages. Reading from it or writing to it means talking to this device. The device files are in `/dev`.
:::

`ls -l` marks them with letters of their own: `c` for a device that delivers data character by character, `b` for one that works in blocks, like a storage device. Instead of a size, there are two numbers with which the kernel selects the driver and the device. Four device files are particularly well known: `/dev/null` swallows everything written into it and delivers nothing when read; `/dev/zero` delivers any number of null bytes; `/dev/urandom` delivers random bytes; `/dev/sdd` is, on the test computer, the storage device on which the Linux is installed.

::::beispiel Reading from devices
```console
$ ls -l /dev/null /dev/zero /dev/urandom /dev/sdd
crw-rw-rw- 1 root root 1,  3 Nov 10 02:41 /dev/null
brw-rw---- 1 root disk 8, 48 Nov 10 02:41 /dev/sdd
crw-rw-rw- 1 root root 1,  9 Nov 10 02:41 /dev/urandom
crw-rw-rw- 1 root root 1,  5 Nov 10 02:41 /dev/zero
$ wc -c /dev/null
0 /dev/null
$ od -An -tu1 -N8 /dev/zero
   0   0   0   0   0   0   0   0
$ od -An -tu1 -N8 /dev/urandom
  14 237 103 241 210 228 133 123
```

`/dev/null` has zero bytes when read. Only zeros come out of `/dev/zero`, and different numbers each time out of `/dev/urandom`; yours will look different. Only `root` and the group `disk` may read `/dev/sdd`, because anyone who reads the storage device directly sees all the files on it.
::::

⁠**In short:** In `/dev`, devices appear as files; you read and write them with the same tools as regular files.

:::hintergrund “Everything is a file”
One of the basic ideas of Unix is this: almost everything a program works with appears as a file in the one tree. This has a tangible advantage. A program needs only a handful of system calls, namely open, read, write and close, and with them it can process regular files and devices alike. In the example, `od` did not know that it was reading from a random number generator; for `od`, `/dev/urandom` was a file like any other. The common naming is just as important: because devices have names in the tree, the same paths and permissions apply to them as to files. The principle has limits, since some devices, such as network cards, have no entry in `/dev` on Linux; as a guiding principle, it still shapes the system today.
:::

### The kernel as a file system: /proc and /sys

<span class="anker" id="stufe-7-8"></span>

How long has the computer been running, which processor is in it, how large is the storage device? The kernel knows this information. So that you can query it without a special tool, it provides it as files. Figure [28](#abb-28) shows how such a file comes about.

:::abbildung linux/k3proc 28
A file that exists only when it is read. `cat /proc/uptime` asks the kernel; only at that moment does it create the line of text with the uptime and hand it back. This file is on no storage device.
:::

:::definition Definition 7.8 (Virtual file system)
<span class="anker" id="satz-7-8"></span>

A __virtual file system__ is a file system whose files are not on any storage device; the kernel creates their contents at the moment a program reads them. `/proc` is such a file system with information about the kernel and about every running program, `/sys` one with information about devices and drivers.
:::

In `/proc`, every running program has a directory whose name is a number. Besides these, there are files such as `/proc/version` with the version of the kernel, `/proc/uptime` with the uptime in seconds and `/proc/cpuinfo` with information about the processor. The commands `uptime` and `free` from [Chapter 2, Sections 6.3](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/das-system-erkunden.html#stufe-6-3) and [6.4](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/das-system-erkunden.html#stufe-6-4), read their information from `/proc/uptime` and `/proc/meminfo`.

::::beispiel Querying the kernel
```console
$ cat /proc/version
Linux version 6.6.87.2-microsoft-standard-WSL2 (root@439a258ad544) (gcc (GCC) 11.2.0, GNU ld (GNU Binutils) 2.37) #1 SMP PREEMPT_DYNAMIC Thu Jun  5 18:30:46 UTC 2025
$ ls -l /proc/version
-r--r--r-- 1 root root 0 Nov 10 02:42 /proc/version
$ cat /proc/uptime
46.54 642.08
$ ls -d /proc/[0-9]*
/proc/1    /proc/178  /proc/221  /proc/327  /proc/397  /proc/87
/proc/158  /proc/181  /proc/222  /proc/328  /proc/43
/proc/159  /proc/2    /proc/238  /proc/329  /proc/435
/proc/160  /proc/203  /proc/246  /proc/371  /proc/6
/proc/170  /proc/206  /proc/326  /proc/373  /proc/80
```

According to `ls -l`, `/proc/version` has the size 0 and still delivers a long line: the contents are created only when it is read. The first number in `/proc/uptime` is the uptime in seconds, here 46.5; the second counts how long all processor cores together have been idle. The pattern `[0-9]*` selects all entries that begin with a digit: one directory per running program.
::::

::::beispiel [Second example] The size of the storage device from /sys
For each storage device, there is a directory under `/sys/block`; the file `size` gives its size in sectors of 512 bytes (sector: [Chapter 1, Section 5.1](/wissen/en/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/datentrager-abbild-und-prufsumme.html#stufe-5-1)):

```console
$ cat /sys/block/sdd/size
2147483648
```

$2\,147\,483\,648 \cdot 512 = 1\,099\,511\,627\,776$ bytes. With powers of two, it is quicker: $2\,147\,483\,648 = 2^{31}$ and $512 = 2^9$, together $2^{31} \cdot 2^9 = 2^{40}$ bytes, exactly 1 TiB.
::::

⁠**In short:** `/proc` and `/sys` are windows into the kernel: their files are created when they are read and reveal the uptime, the processor, the devices and the running programs.

:::hintergrund Why a file of size 0 can have contents
The size that `ls -l` shows is a piece of information from the file system's administrative data. For regular files, it matches the number of stored bytes. In `/proc`, nothing is stored: when a program reads `/proc/uptime`, the kernel calls a small function that turns the uptime into text and returns this text as the contents. The kernel knows how long it will be only when it creates it; that is why it reports the size as 0. Programs that read files to the end, such as `cat`, cope with this; a program that relies on the size would read nothing. The idea of representing running programs as files comes from Unix research in 1984; Linux has extended it into a window onto almost everything the kernel knows.
:::

### Exercises for Section [7](#stufe-7)

<span class="anker" id="stufe-7-9"></span>

:::aufgabe Exercise 23 ★★ A tour
<span class="anker" id="aufg-23"></span>

For each of the following locations, write one sentence about what it is and what it is for, and check your answer with `ls -ld`, `file` or `head`: (a) `/etc/hostname`, (b) `/var/log`, (c) `/dev/null`, (d) `/proc/cpuinfo`, (e) `/usr/bin`.

:::loesung
(a) `/etc/hostname` is a text file in `/etc` with the name of the computer. (b) `/var/log` is the directory of the log files. (c) `/dev/null` is a device file that swallows everything written into it and returns nothing when read. (d) `/proc/cpuinfo` is a file of the virtual file system `/proc` with information about the processor; the kernel creates it when it is read. (e) `/usr/bin` is the directory with the distribution's programs. The check:

```console
$ file /etc/hostname /var/log /dev/null /proc/cpuinfo /usr/bin
/etc/hostname: ASCII text
/var/log:      directory
/dev/null:     character special (1/3)
/proc/cpuinfo: empty
/usr/bin:      directory
```

(d) is remarkable: `file` considers `/proc/cpuinfo` empty because the file reports the size 0. Nevertheless, `head -n 5 /proc/cpuinfo` shows contents, because `head` simply reads until nothing more comes. For `/dev/null`, `file` calls the device “character special” with the two device numbers 1 and 3, which `ls -l` also shows.
:::
:::

:::aufgabe Exercise 24 ★ Where does the file belong?
<span class="anker" id="aufg-24"></span>

According to the FHS, which directory does each of the following belong in: (a) a program's configuration file for the whole system, (b) the log of a service, (c) a program that comes with the distribution, (d) your own vacation photo, (e) a file that a program needs only while it is running, (f) an add-on program from a company that brings everything along in a directory of its own?

:::loesung
(a) `/etc`. (b) `/var/log`. (c) `/usr/bin`. (d) Your home directory, for example `/home/student/fotos`, under `/home`. (e) `/tmp`. (f) `/opt`.
:::
:::

:::aufgabe Exercise 25 ★★ Uptime from /proc
<span class="anker" id="aufg-25"></span>

Read `/proc/uptime` and convert the first number into hours and minutes. Compare it with the output of `uptime` from [Chapter 2, Section 6.3](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/das-system-erkunden.html#stufe-6-3). Why do the two agree, although `/proc/uptime` is empty according to `ls -l`?

:::loesung
```console
$ cat /proc/uptime
83.80 1163.22
$ uptime
 02:42:54 up 1 min,  1 user,  load average: 0.00, 0.00, 0.00
```

83.80 seconds is one minute and 23.8 seconds, that is, 0 hours and 1 minute; `uptime` shows exactly that as `up 1 min`, rounded down to whole minutes. The WSL VM of the test computer had only just been started here; on your computer, it is probably hours. The two agree because `uptime` reads its value from `/proc/uptime`. That the file has the size 0 according to `ls -l` does not matter: its contents come into being only when it is read, fresh from the kernel's clock.
:::
:::

:::aufgabe Exercise 26 ★★ The size of the storage device
<span class="anker" id="aufg-26"></span>

On another computer, `/sys/block/sda/size` returns the value `1000215216`. How many bytes does the storage device have, how many GB and how many GiB? Which of the two numbers would a seller print on the packaging?

:::loesung
$1\,000\,215\,216 \cdot 512 = 512\,110\,190\,592$ bytes. Divided by $10^9$, that is 512.11 GB; divided by $1024^3$, it is 476.94 GiB. The packaging would say “512 GB”, because manufacturers count in powers of ten ([Chapter 1, Section 5.1](/wissen/en/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/datentrager-abbild-und-prufsumme.html#stufe-5-1)). `lsblk` would show 476.9G and `ls -h` 477G, because above 10 it rounds up to whole units; both mean the same number of bytes.
:::
:::

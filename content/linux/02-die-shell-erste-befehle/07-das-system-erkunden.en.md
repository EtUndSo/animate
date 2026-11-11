---
title: Exploring the system
pfad: Computer Science / Linux and the Command Line / The Shell: First Commands
adresse: informatik/linux-und-kommandozeile/die-shell-erste-befehle
knoten: Chapter 2: The Shell: First Commands
order: 6070700
summary: Equipped with commands, options and help, you can now question your system.
tags: 
lang: en
---

<span class="anker" id="stufe-6"></span>

:::zweck
Equipped with commands, options and help, you can now question your system. This section presents a handful of commands that every Linux computer knows: they name the kernel and the distribution, the user, the date and uptime, the main memory and the disk space. Together, they make up a fact sheet of the computer.
:::

### Kernel and distribution

<span class="anker" id="stufe-6-1"></span>

When there is a problem, every set of instructions and every help forum asks first: which kernel, which distribution? Two commands answer this.

:::abbildung linux/k2uname 24
The output of `uname -a`, taken apart: kernel name, host name, kernel version, details of the kernel build with date, processor type and the name of the operating system.
:::

The option `-a`, long form `--all`, makes `uname` print all of its information on one line. The kernel does not write the name of the distribution, because it does not know it; the name is in the file `/etc/os-release` ([Chapter 1, Section 2.3](/wissen/en/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/drei-wege-zu-einem-eigenen-linux.html#stufe-2-3)), in Ubuntu on the first line.

::::beispiel The fact sheet begins
```console
$ uname -a
Linux labor 6.6.87.2-microsoft-standard-WSL2 #1 SMP PREEMPT_DYNAMIC Thu Jun  5 18:30:46 UTC 2025 x86_64 GNU/Linux
$ head -n 1 /etc/os-release
PRETTY_NAME="Ubuntu 26.04.1 LTS"
```

The kernel name `Linux` is followed by the host name `labor`, then the version. `#1 SMP PREEMPT_DYNAMIC` and the date describe when and how the kernel was built: `#1` is the sequential number of the build, and `SMP` means that it uses several processor cores. Next come the processor type and `GNU/Linux` as the name of the operating system. Under WSL 2, this is Microsoft's kernel from [Chapter 1, Section 4.1](/wissen/en/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/wsl-2-linux-neben-windows.html#stufe-4-1); in a virtual machine or in the live system, you see an Ubuntu kernel whose version ends in `generic`.
::::

⁠**In short:** `uname -a` names the kernel, the computer and the processor; the first line of `/etc/os-release` names the distribution.

### The user: whoami and id

<span class="anker" id="stufe-6-2"></span>

What you are allowed to do on a Linux system depends on who you are to the system. `whoami` gives only the name; `id` reveals how the system keeps track of you internally.

:::abbildung linux/k2id 25
The output of `id`, taken apart: the user ID with the name `student`, the group ID of the primary group and the list of all groups, including `sudo`.
:::

To the kernel, a user is not a name but a number, the *user ID*; the name is only a label for humans. In Ubuntu, the first user you create during setup gets the number 1000. In addition, every user belongs to one or more *groups*, named sets of users to whom the system can grant something collectively. Groups have numbers, too.

::::beispiel Who am I?
```console
$ whoami
student
$ id
uid=1000(student) gid=1000(student) groups=1000(student),27(sudo)
```

`uid` is the user ID. `gid` is the group ID of the primary group, the one group that is permanently assigned to each user; in Ubuntu, it has the same name as the user. `groups` lists all groups. The group `sudo` with the number 27 is a permission: its members may run individual commands with the privileges of root. How and when you do this is a topic of its own; this chapter does not need it.
::::

⁠**In short:** `whoami` gives your name, `id` your user ID and your groups.

### Date and running time: date and uptime

<span class="anker" id="stufe-6-3"></span>

You often need the time and date, for example to record an output or to build a file name. And sometimes you want to know how long the computer has been running and how busy it is.

::::beispiel The system clock
`date` gives the date and time in the configured time zone, with `-u` in Coordinated Universal Time (UTC). For `date`, an argument that begins with a plus sign is a template for the output; in it, `%F` stands for the date in the form year-month-day:

```console
$ date
Tue Nov 10 00:31:31 CET 2026
$ date -u
Mon Nov  9 23:31:31 UTC 2026
$ date +%F
2026-11-10
```

Shortly after midnight Central European Time, it is still the previous day in UTC. The English names for the day of the week and the month come from the language setting of the test system; on a computer with a German language setting, `date` writes them in German. The form `2026-11-10`, by contrast, is the same everywhere and sorts correctly, which is why people like to use it for file names.
::::

:::abbildung linux/k2uptime 26
The output of `uptime`, taken apart: time, uptime since startup, logged-in users and the three load values, averaged over 1, 5 and 15 minutes.
:::

`uptime` gives the time, how long the system has been running since startup, how many users are logged in and three numbers for the *load*. A load value is the average number of running programs that are currently computing, waiting for a free processor core or waiting for the storage device, averaged over the last minute, the last five and the last fifteen minutes. More precisely, it is a moving average in which recent moments count more than earlier ones. Whether a value is high can only be seen by comparing it with the number of processor cores, which `nproc` gives.

::::beispiel How long has the computer been running?
```console
$ uptime
 00:31:31 up 1 min,  1 user,  load average: 2.47, 0.87, 0.31
$ nproc
14
```

WSL 2 starts its small virtual machine only when you open a terminal, and it shuts the machine down again soon after the last window is closed; hence the one minute. At 2.47, the load value for the last minute is higher than the other two, because many programs start running at the same time during startup. With 14 cores, even that is little: on average, more than eleven cores would still have had nothing to do.
::::

⁠**In short:** `date` gives the date and time, `uptime` the uptime and the load of the last 1, 5 and 15 minutes.

### Main memory: free

<span class="anker" id="stufe-6-4"></span>

When a computer becomes sluggish, the first question is whether there is enough main memory. The answer from `free` is confusing at first glance and very revealing at second glance.

:::abbildung linux/k2free 27
The output of `free -h`: total, used, free, shared, used as cache and available. The cache does not count as free, but most of it is available.
:::

`free` shows the main memory as a table, and the option `-h` (“human”) shows it in easily readable units. The units `Mi` and `Gi` are mebibytes and gibibytes, that is, multiples of $2^{20}$ and $2^{30}$ bytes ([Chapter 1, Section 5.1](/wissen/en/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/datentrager-abbild-und-prufsumme.html#stufe-5-1)). The most important columns:

<ul>

<li>

`total`: all the main memory that the system has.

</li>

<li>

`used`: what is not available, mainly because running programs and the kernel occupy it; `free` calculates it as `total` minus `available`.

</li>

<li>

`free`: what is not used at all.

</li>

<li>

`buff/cache`: what the kernel uses as a *cache* for files so that it does not have to fetch them from the storage device again the next time they are read.

</li>

<li>

`available`: what newly started programs could get without anything having to be swapped out to the storage device.

</li>

</ul>

The line `Swap` describes an area on the storage device to which the kernel can move rarely used memory contents when main memory runs short.

::::beispiel How much memory is free?
```console
$ free -h
               total        used        free      shared  buff/cache   available
Mem:            31Gi       765Mi        30Gi       3.5Mi       429Mi        30Gi
Swap:          8.0Gi          0B       8.0Gi
```

The WSL 2 virtual machine has 31 GiB, just under half of the test computer's main memory ([Chapter 1, Section 4.1](/wissen/en/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/wsl-2-linux-neben-windows.html#stufe-4-1)). 765 MiB are used, 429 MiB serve as cache, and 30 GiB are available to new programs.
::::

⁠**In short:** `free -h` shows the main memory; the column that matters is `available`, not `free`.

:::hintergrund Why Linux seems to have no free memory
On a computer that has been running for a while, the column `free` often shows an alarmingly small value and `buff/cache` a large one. This is intentional. Unused main memory would be wasted, so the kernel keeps the contents of files that have already been read in it. If a program reads them again, they come from main memory instead of from the much slower storage device. If a program needs more memory, the kernel releases the cache immediately. That is why `free` counts most of the cache as available memory in `available`, and that is why this column is the right one when you want to know whether there is enough memory.
:::

### Disk space: df

<span class="anker" id="stufe-6-5"></span>

If the storage device is full, programs fail in surprising ways, for example when saving or installing. `df` (“disk free”) shows, for each mounted file system, how much space it has and how much of it is used.

:::abbildung linux/k2df 28
One line of `df`, twice: with `-h` in multiples of 1024, with `-H` in multiples of 1000. The same 1 081 101 176 832 bytes appear as `1007G` and as `1.1T`.
:::

You know the terms file system and mounting from [Chapter 1, Sections 5.3](/wissen/en/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/datentrager-abbild-und-prufsumme.html#stufe-5-3) and [8.1](/wissen/en/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/das-live-system.html#stufe-8-1). Without an argument, `df` lists all mounted file systems; under WSL 2, there are about twenty. With a folder as an argument, it shows only the file system in which this folder lies; `/` is the root of the entire Linux file tree. Here, too, `-h` makes the numbers readable, but with a catch: `df -h` calculates in multiples of 1024 and still writes only `G`; what it means is GiB. The option `-H` calculates in multiples of 1000.

::::beispiel Space under Linux and under Windows
```console
$ df -h /
Filesystem      Size  Used Avail Use% Mounted on
/dev/sdd       1007G  4.2G  952G   1% /
$ df -H /
Filesystem      Size  Used Avail Use% Mounted on
/dev/sdd        1.1T  4.5G  1.1T   1% /
$ df -h /mnt/c
Filesystem      Size  Used Avail Use% Mounted on
C:\             475G  318G  158G  67% /mnt/c
```

The Linux file system of WSL 2 is 1 081 101 176 832 bytes in size and lies on the storage device `/dev/sdd`. Divided by $2^{30}$, that is 1006.85 GiB, and `df -h` rounds this to `1007G`. Divided by $10^{12}$, it is 1.08 TB, and `df -H` rounds up to one decimal place: `1.1T`. The fact that size minus used space gives more than the free space is due to a reserve of about five percent that the Linux file system holds back for the root account. The third line shows the Windows drive C:, which is mounted under `/mnt/c` ([Chapter 1, Section 4.5](/wissen/en/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/wsl-2-linux-neben-windows.html#stufe-4-5)).
::::

`lsblk` shows which storage devices are connected at all; [Chapter 1, Section 8.1](/wissen/en/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/das-live-system.html#stufe-8-1) explains its output under WSL 2.

⁠**In short:** `df -h /` shows the size, used space and free space of the file system; `-h` calculates in multiples of 1024, `-H` in multiples of 1000.

### Exercises for Section [6](#stufe-6)

<span class="anker" id="stufe-6-6"></span>

:::aufgabe Exercise 21 ★ A fact sheet of your system
<span class="anker" id="aufg-21"></span>

For your own Linux, find out the following with one command each: kernel version, distribution with its release, your user name and your user ID, your groups, the total and the available main memory, the size and the free space of the file system `/`, the number of processor cores. Note down each command and answer in a table.

:::loesung
On the test system:

| Question | Command | Answer |
|---|---|---|
| Kernel version | `uname -r` | `6.6.87.2-microsoft-standard-WSL2` |
| Distribution | `head -n 1 /etc/os-release` | `Ubuntu 26.04.1 LTS` |
| User name | `whoami` | `student` |
| User ID, groups | `id` | `uid=1000`, groups `student` and `sudo` |
| Main memory | `free -h` | total `31Gi`, available `30Gi` |
| Space on `/` | `df -h /` | size `1007G`, free `952G` |
| Processor cores | `nproc` | `14` |

Your values will differ; in a virtual machine or in the live system, the kernel version ends in `generic`; in a virtual machine, the memory and cores are the ones you assigned to it, and in the live system, those of the computer itself.
:::
:::

:::aufgabe Exercise 22 ★★ Checking the units
<span class="anker" id="aufg-22"></span>

`free -b` shows the memory in bytes. On the test system, it reported 33 393 664 000 bytes as `total`. Check by calculation that `free -h` shows `31Gi` for this. What would `free -h --si` show, which calculates in multiples of 1000? Also check: `df` reported 4 439 998 464 bytes as used. Why does `df -h` show `4.2G` for this, although the exact calculation gives 4.13 GiB?

:::loesung
$33\,393\,664\,000 / 2^{30} = 31.10$, so about 31 GiB; `free -h` shows `31Gi`. In multiples of 1000, it is $33\,393\,664\,000 / 10^{9} = 33.39$ GB; `free -h --si` shows `33G`.

$4\,439\,998\,464 / 2^{30} = 4.135$ GiB. With `-h` and `-H`, `df` does not round to the nearest value but always rounds up; this is how 4.135 becomes `4.2G`. With `-H`, it is $4\,439\,998\,464 / 10^{9} = 4.44$ GB, rounded up `4.5G`, as in the example in subsection [6.5](#stufe-6-5).
:::
:::

:::aufgabe Exercise 23 ★★ Dates from a template
<span class="anker" id="aufg-23"></span>

Use `date --help` or `man date` to find out how to make it print (a) only the time in the format hours:minutes:seconds, (b) the day of the week written out in full, (c) the number of the calendar week. Why is `+%F` an argument and not an option?

:::loesung
In the list of templates that `date --help` shows, you find `%T` for the time, `%A` for the day of the week written out in full and `%V` for the calendar week according to ISO, in which the week begins on Monday:

```console
$ date +%T
00:40:54
$ date +%A
Tuesday
$ date +%V
46
```

`+%F` does not begin with a minus sign, so by the rules from Section [2](der-aufbau-einer-befehlszeile.html#stufe-2) it is not an option but an ordinary argument. That an argument with a plus sign is a template is something `date` itself has defined; to the shell, it is a word like any other.
:::
:::

:::aufgabe Exercise 24 ★★★ Interpreting load
<span class="anker" id="aufg-24"></span>

A server with 4 processor cores reports the load values `6.10, 3.95, 1.20` for `uptime`. Another one with 32 cores reports `6.10, 6.05, 6.12`. In each case, what do the three numbers say about how the last quarter of an hour went? Which computer is working at full capacity?

:::loesung
The server with 4 cores: over the last quarter of an hour, the load averaged 1.20; over the last five minutes, 3.95; over the last minute, 6.10. So the load is rising sharply right now. On average, 6.10 programs wanted to compute or were waiting for the storage device, but only 4 cores were available: a good two had to wait all the time. This computer is overloaded at the moment.

The server with 32 cores: the three values are almost the same; the load has been steady for a quarter of an hour. On average, 6 of 32 cores are busy, that is, just under a fifth. This computer has plenty of reserves, even though its load values are just as high as those of the first one.
:::
:::

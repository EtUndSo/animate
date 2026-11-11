---
title: Operating system, kernel and distribution
pfad: Computer Science / Linux and the Command Line / A Linux to Practice On: WSL, Virtual Machine, Live USB Stick
adresse: informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick
knoten: Chapter 1: A Linux to Practice On: WSL, Virtual Machine, Live USB Stick
order: 6060200
summary: Before you set up a Linux, you need to know what it actually is that you are setting up.
tags: operating system, application program, kernel mode, user mode, privileged instruction, kernel, drivers, system call
lang: en
---

<span class="anker" id="stufe-1"></span>

:::zweck
Before you set up a Linux, you need to know what it actually is that you are setting up. This section clarifies what an operating system does, which part of it really controls the hardware, how ordinary programs get access to that part's services and what exactly the word “Linux” refers to.
:::

### The operating system

<span class="anker" id="stufe-1-1"></span>

A laptop runs a browser, an editor, a music program and perhaps a program that is saving photos from a phone, all at the same time. All of them need the processor, the main memory, the SSD, the network and the screen. Someone has to share out this hardware and make sure that the browser does not accidentally overwrite the photos. And none of these programs should have to know exactly which SSD is installed.

Figure [1](#abb-1) shows where this task is handled: in a layer of its own between the hardware and the programs you work with.

:::abbildung linux/k1schichten 1
The operating system lies as a layer between the hardware and the programs. The programs request services from it; only the operating system controls the hardware.
:::

:::definition Definition 1.1 (Operating system)
<span class="anker" id="satz-1-1"></span>

The __operating system__ is the software that manages a computer's hardware, makes it available to the other programs through uniform services and keeps the programs apart from one another.
:::

A program that runs under an operating system and performs a task for the user is called an __application program__, or program for short. Well-known operating systems are Windows, macOS, Android and the Linux systems that this series is about.

::::beispiel Saving a file
In the editor, you press Ctrl+S. The editor does not know whether the file ends up on an SSD, a USB stick or a network drive, and it does not need to know. It asks the operating system: “Write these 2 000 characters to the file `notiz.txt`.” The operating system looks for free space on the storage device, writes the data, remembers where it is and reports to the editor whether it worked. If a second program saves another file at the same time, the operating system makes sure that the two write operations do not get in each other's way.
::::

⁠**In short:** The operating system manages the hardware, offers services to the programs and keeps them apart from one another.

:::hintergrund Why there is a management layer at all
The tasks of an operating system can be traced back to three ideas.

<ul>

<li>

⁠**Abstraction.** An SSD knows only numbered blocks of 512 or 4 096 bytes each. The operating system turns them into files with names and folders. Every program works with files, and only the operating system needs to know the blocks.

</li>

<li>

⁠**Sharing.** A processor core can run only one program at any one time. The operating system switches back and forth between the programs many times per second, and each one gets a region of main memory of its own. This way, each program seems to have a computer of its own.

</li>

<li>

⁠**Protection.** Because all accesses to the hardware go through the operating system, it can check whether a program is allowed to do something. A program that crashes then does not take the others down with it.

</li>

</ul>

The second idea is remarkable: from a single set of hardware, the operating system creates the illusion of many machines.
:::

### Two operating modes of the processor

<span class="anker" id="stufe-1-2"></span>

Protection works only if a program cannot simply get around it. After all, a malicious or faulty program could try to address the SSD itself instead of asking the operating system. Only the hardware can prevent this, namely the processor itself.

**Two levels of permission.** You can picture the processor as a machine with a key switch. In one position, it may do everything; in the other, only what is harmless. You can switch over only in the “everything” position.

:::definition Definition 1.2 (Kernel mode and user mode)
<span class="anker" id="satz-1-2"></span>

A processor has at least two operating modes. In __kernel mode__, the running program may execute any instruction of the processor. In __user mode__, certain instructions are blocked, such as direct access to devices and setting which program may use which part of main memory. Such a blocked instruction is called a __privileged instruction__. If a program in user mode attempts a privileged instruction, the processor does not execute it: it interrupts the program and hands control to the operating system.
:::

::::beispiel A program accesses the SSD itself
A program in user mode contains an instruction that is supposed to send data directly to the SSD. The processor recognizes the blocked instruction and does not execute it, but jumps into the operating system instead. The operating system determines that the program has tried something forbidden and terminates it. The SSD has noticed nothing of the attempt.
::::

⁠**In short:** The processor itself ensures that ordinary programs cannot touch the hardware directly.

### The kernel

<span class="anker" id="stufe-1-3"></span>

If everything is allowed only in kernel mode, there must be a part of the operating system that runs in this mode. This part is so important that it has a name of its own.

:::definition Definition 1.3 (Kernel)
<span class="anker" id="satz-1-3"></span>

The __kernel__ (the core of the system) is the part of the operating system that runs in kernel mode. It controls the hardware directly, divides the processor and main memory among the programs, manages the files and checks for every access whether it is allowed. All other programs run in user mode.
:::

The __drivers__ also belong to the kernel: pieces of software that can control a particular device, such as a particular network card or a particular SSD. Other parts of an operating system, by contrast, for example the window in which you type commands or the programs for copying files, run in user mode like any application program.

::::beispiel Who does what when a video plays
A video program reads a file, converts the stored data into images and displays them. The kernel reads the file, using the SSD's driver. In this example, the video program converts the data into images itself, in user mode, because this requires no devices, only arithmetic instructions. The finished image is again brought to the screen by the kernel, using the graphics driver.
::::

⁠**In short:** The kernel is the only part of the system that is allowed to control the hardware directly.

### The system call

<span class="anker" id="stufe-1-4"></span>

A program in user mode is not allowed to touch the SSD, but it still has to read and write files. So it needs a way to ask the kernel for a service without entering kernel mode itself.

**A counter with fixed forms.** As at the counter of a government office, you cannot go behind the counter; you fill in one of the forms provided and hand it through. The office checks the application and either handles it or rejects it (a picture, not a mechanism). Figure [2](#abb-2) shows the mechanism.

:::abbildung linux/k1systemaufruf 2
A program gets to the hardware only through a system call: it states the number of the desired service and the details for it, a special processor instruction switches to kernel mode, and the kernel checks and carries out the request. The processor blocks any direct access from user mode.
:::

:::definition Definition 1.4 (System call)
<span class="anker" id="satz-1-4"></span>

A __system call__ is a request from a program to the kernel to perform a particular service, for example to open a file, read data or provide memory. The program puts the number of the service and the necessary details in place and executes a special processor instruction. This instruction switches to kernel mode and jumps to a location in the kernel that the kernel itself set when the computer started. The kernel checks the request, handles it, switches back to user mode and gives the program the result.
:::

::::beispiel What a small program wants from the kernel
Linux has a tool called `strace` that records every system call of a program. Here it is attached to the program `gnucat`, the classic version of a program that displays the contents of a file; the file shown is the one that contains the computer's name. You can see the calls for opening, reading, writing and closing:

```text
openat(AT_FDCWD, "/etc/hostname", O_RDONLY) = 3
read(3, "labor\n", 262144)              = 6
write(1, "labor\n", 6)                  = 6
read(3, "", 262144)                     = 0
close(3)                                = 0
```

The first line asks the kernel to open the file `/etc/hostname` for reading; it replies with the number 3, under which the program then refers to the file. The second line reads up to 262 144 bytes; the kernel delivers 6 bytes, the word `labor` and a line end. The third line writes these 6 bytes to the output with the number 1, which is the window in which the program runs. The second read attempt delivers 0 bytes: the file has come to an end. Finally, the program closes the file. In total, this tiny program makes 114 system calls; the others mainly serve to load parts of the program at startup.
::::

⁠**In short:** Programs get hardware services only by asking the kernel for them through a system call.

:::hintergrund Why the program may not decide for itself where it jumps in the kernel
A system call raises the processor's privileges. If the program could freely choose the address in the kernel, it could jump into the middle of a kernel function, right behind the point where the kernel checks the permission, and would thus have all privileges. That is why, at startup, when the processor is running in kernel mode anyway, the kernel sets a fixed entry point in the processor: every system call jumps exactly there. A program can only name the number of a service. At the entry point, the kernel itself looks up in its table of services which kernel function belongs to this number, and it checks the details before carrying it out. Setting the entry point is itself a privileged instruction, and the table lies in a memory region that programs in user mode are not allowed to write to. The only way into kernel mode thus leads through a gate that the kernel itself has built and guards.
:::

### Linux

<span class="anker" id="stufe-1-5"></span>

People use the word “Linux” for two different things: sometimes a whole system with windows and programs, sometimes only one very specific part of it. For this chapter, the difference matters.

:::definition Definition 1.5 (Linux)
<span class="anker" id="satz-1-5"></span>

__Linux__ is a kernel. Linus Torvalds began it in 1991 as a student in Helsinki; today it is maintained by thousands of developers, at companies, at universities and in their spare time. Its source code is freely available under the GNU General Public License (GPL), version 2. In the strict sense, “Linux” refers only to this kernel; in everyday language, people often mean the whole system built on it.
:::

::::beispiel One kernel, many systems
The same Linux kernel, slightly adapted in each case, is found in very different devices: in most servers on the internet, in Android smartphones, in many Wi-Fi routers and TVs and in the Linux systems for PCs. So an Android phone and an Ubuntu laptop both use Linux as their kernel, but they have almost no other programs in common.
::::

⁠**In short:** Strictly speaking, Linux is only the kernel of an operating system.

:::hintergrund Why there are so many different Linux systems
The GPL allows anyone to use, modify and pass on the source code of the kernel, even for money. In return, it requires that anyone who passes on a modified version also makes its source code available under the same license. That is why any company and any group can build a system of its own around the kernel, and improvements flow back into the common kernel. The programs that a Linux system needs around the kernel come to a large extent from the GNU project, which Richard Stallman had started in 1983 to create a free operating system; at the beginning of the 1990s, the only thing it still lacked was a kernel. That is why some people speak of “GNU/Linux”.
:::

### The distribution

<span class="anker" id="stufe-1-6"></span>

A kernel on its own cannot talk to you. It has no window into which you could type something, no programs for copying files and no browser. For a usable system to come about, someone has to assemble thousands of programs to match the kernel, coordinate them with one another and supply them with bug fixes for years.

:::definition Definition 1.6 (Distribution)
<span class="anker" id="satz-1-6"></span>

A __distribution__ is a complete operating system that a vendor or a community assembles from the Linux kernel, tools, application programs and default settings and maintains as a whole. Every distribution comes with a __package manager__: a program with which you install, update and remove software from the distribution's sources. Chapter 9 explains how it works.
:::

::::beispiel [Examples] Four distributions
Table [1](#tab-1) lists four distributions that appear in this series.

<span class="anker" id="tab-1"></span>

**Table 1:** Four distributions. All of them use the Linux kernel, but they differ in their selection of programs, in their package manager and in how long a release is supported.

| Distribution | Maintained by | Characteristics |
|---|---|---|
| Debian | a worldwide community of volunteers | very stable, basis of many other distributions |
| Ubuntu | the company Canonical together with a community | builds on Debian, widely used, well documented; this series uses Ubuntu 26.04 LTS |
| Fedora | a community, supported by the company Red Hat | brings new software early, basis for Red Hat Enterprise Linux |
| Kali Linux | the company OffSec | builds on Debian, contains hundreds of tools for security testing; its publishers explicitly advise Linux newcomers against it |
::::

⁠**In short:** Linux is the kernel; a distribution turns it into a complete system.

:::hintergrund Why this series uses Ubuntu
For a practice system, three things count: that it runs on almost any computer, that you can find help when there are problems and that it is maintained for a long time. Ubuntu is one of the most widely used distributions for desktops and servers, its documentation is freely available, and Windows comes with its own way to a Linux, which sets up Ubuntu by default. Because Ubuntu builds on Debian, almost everything you learn here also applies to Debian and Kali Linux.
:::

### Releases and long-term support

<span class="anker" id="stufe-1-7"></span>

A distribution keeps appearing in new releases. If you set up a practice system, you have to choose one, and with Ubuntu, the version number already tells you almost everything you need to know.

:::definition Definition 1.7 (Ubuntu release, LTS)
<span class="anker" id="satz-1-7"></span>

An Ubuntu release is named after the year and month in which it appeared: `26.04` appeared in April 2026. In addition, each release has a code name; `26.04` is called “Resolute Raccoon”. Every two years in April, an __LTS release__ (Long Term Support) appears, for which Canonical supplies security fixes and bug fixes for five years. In between, interim releases appear, which are supported for only nine months. A number like `26.04.1` denotes a __point release__: the same system with the fixes collected up to that point and new installation media.
:::

::::beispiel Classifying three releases
Ubuntu 26.04 LTS appeared on 23 April 2026 and is supported until April 2031; its first point release, 26.04.1, appeared on 27 August 2026. Ubuntu 26.10 appeared in October 2026 and is an interim release; it is supported until July 2027. Ubuntu 24.04 LTS, the previous long-term release, is still supported until April 2029. This series uses 26.04 LTS.
::::

⁠**In short:** For a practice system, you choose the current LTS release, because it receives fixes for five years.

:::hintergrund Why there are long-term releases
New releases bring new programs, but also new bugs and changes in how things are operated. Anyone who runs a server, a lab or a course wants a system that behaves the same way for years and still gets every newly discovered security vulnerability closed. An LTS release separates the two: for five years, it receives fixes, but no new features that could change anything. For even longer support, Canonical offers an add-on called Ubuntu Pro.
:::

### Exercises for Section [1](#stufe-1)

<span class="anker" id="stufe-1-8"></span>

:::aufgabe Exercise 1 ★ Who does what?
<span class="anker" id="aufg-1"></span>

Classify each activity: Does it run in user mode or in kernel mode? Is a system call involved?

<ol class="al">

<li>

A spreadsheet program calculates the average of 1 000 numbers that are already in main memory.

</li>

<li>

The spreadsheet program saves the spreadsheet.

</li>

<li>

The SSD's driver writes the blocks of the spreadsheet to the SSD.

</li>

<li>

A browser asks for 200 MB of additional main memory.

</li>

</ol>

:::loesung
(a) User mode, no system call. The numbers are already in the program's main memory, and adding and dividing are ordinary arithmetic instructions that every program may execute. The kernel is not involved.

(b) The spreadsheet program itself runs in user mode, but saving means getting data onto a storage device, and the program is not allowed to do that itself. It makes system calls, for example to open the file, to write and to close it. The actual work is then done by the kernel in kernel mode.

(c) Kernel mode. The driver is part of the kernel and addresses the device directly. It does not make a system call itself; instead, it carries out the request that came in with a system call in (b).

(d) System call. Which program may use which part of main memory is set only by the kernel; this is a privileged operation. So the browser asks the kernel via a system call, the kernel sets up the memory in kernel mode and tells the browser where it is.
:::
:::

:::aufgabe Exercise 2 ★ Kernel or distribution?
<span class="anker" id="aufg-2"></span>

Is the statement true? Justify each answer in one sentence.

<ol class="al">

<li>

“Android is a Linux.”

</li>

<li>

“Ubuntu and Kali Linux use the same kernel, so they are the same system.”

</li>

<li>

“If you install Linux, you install a distribution.”

</li>

<li>

“The package manager is part of the kernel.”

</li>

</ol>

:::loesung
(a) In the strict sense, it is true: Android uses the Linux kernel. But Android is not a Linux distribution like Ubuntu, because around the kernel there are almost exclusively other programs. If you mean “Linux” in the everyday sense, that is, a system with a terminal and the usual tools, then Android is something different.

(b) False. Both use the Linux kernel, but each builds it itself in its own version, and everything around the kernel, the selection of programs, the default settings and the maintenance, differs. The same kernel alone does not make the same system.

(c) True. A kernel alone is not usable; what you download and install is always a distribution with a kernel, tools and a package manager.

(d) False. The package manager is an ordinary program of the distribution and runs in user mode. When it installs files, it makes system calls for this like any other program.
:::
:::

:::aufgabe Exercise 3 ★★ Can a program get around the kernel?
<span class="anker" id="aufg-3"></span>

A program in user mode tries three things, one after another: (1) to send data directly to the network card, (2) to change the entry point for system calls or the table of services so that a system call jumps into its own code, (3) to make a system call with a number that does not exist at all. What happens in each case, and why can the program not gain control of the computer by any of the three routes?

:::loesung
(1) Direct access to the network card is a privileged instruction. In user mode, the processor does not execute it; instead, it interrupts the program and hands over to the kernel, and the kernel terminates the program.

(2) Setting the entry point is a privileged instruction; such an attempt ends the same way as (1). The table of services is in a memory region of the kernel that programs in user mode are not allowed to write to; this attempt, too, is interrupted by the processor. The kernel set up both at startup in kernel mode, and nobody can change them from user mode.

(3) The system call itself is allowed. In the process, the processor jumps to the fixed entry point of the kernel, not to a location that the program chooses. There, the kernel looks up the number in its table, finds no service for it and returns an error code to the program. The program keeps running but has achieved nothing.

The reason for all three: There are exactly two ways to get into kernel mode, namely an interruption, for example when the processor traps a blocked instruction, or a system call, and both end up at locations that the kernel itself has set. Everything with which you could change these locations or reach the hardware directly is blocked in user mode.
:::
:::

:::aufgabe Exercise 4 ★ Classifying releases
<span class="anker" id="aufg-4"></span>

For each release, state whether it is an LTS release, in which month it appeared and until when it is supported: 24.04, 25.10, 26.04.1, 26.10. Which one would you choose on 9 November 2026 for a practice system that you want to use for three years?

:::loesung
| Release | LTS? | appeared | supported until |
|---|---|---|---|
| 24.04 | yes | April 2024 | April 2029 |
| 25.10 | no | October 2025 | July 2026, expired |
| 26.04.1 | yes (point release) | August 2026 | April 2031 |
| 26.10 | no | October 2026 | July 2027 |

25.10 was supported for nine months; 26.04.1 is the first point release of 26.04, which appeared in April 2026. For three years from November 2026, that is, until November 2029, only Ubuntu 26.04 LTS comes into question, set up from the media of 26.04.1. Release 24.04 reaches its end in April 2029, and 26.10 as early as July 2027. A point release is not a release of its own: If you install 26.04 and update it, you afterward have the same state as with 26.04.1.
:::
:::

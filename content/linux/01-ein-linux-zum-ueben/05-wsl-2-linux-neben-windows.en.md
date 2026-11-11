---
title: WSL 2: Linux alongside Windows
pfad: Computer Science / Linux and the Command Line / A Linux to Practice On: WSL, Virtual Machine, Live USB Stick
adresse: informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick
knoten: Chapter 1: A Linux to Practice On: WSL, Virtual Machine, Live USB Stick
order: 6060500
summary: The quickest way to a Linux under Windows is WSL 2.
tags: Windows Subsystem for Linux
lang: en
---

<span class="anker" id="stufe-4"></span>

:::zweck
The quickest way to a Linux under Windows is WSL 2. This section explains what WSL 2 is, namely a small virtual machine that Windows manages itself, how to set it up and check it, how Windows and Linux get at each other's files and where the limits of this way lie.
:::

### The Windows Subsystem for Linux

<span class="anker" id="stufe-4-1"></span>

For work on the command line, you do not want a separate window with a whole second computer, but a Linux terminal that feels like any other program on Windows. That is exactly what WSL 2 offers, and under the surface, it is a virtual machine.

Figure [8](#abb-8) shows its structure.

:::abbildung linux/k1wsl 8
WSL 2. Via the Microsoft hypervisor, Windows starts a small virtual machine with a real Linux kernel, in which the distribution runs. Files cross the boundary of the VM in both directions: Linux sees drive C: under `/mnt/c`, and Windows sees the Linux files in File Explorer.
:::

:::definition Definition 4.1 (WSL 2)
<span class="anker" id="satz-4-1"></span>

The __Windows Subsystem for Linux__, version 2 (WSL 2), is a component of Windows that starts a real Linux kernel in a small virtual machine, which Windows itself creates, starts and stops. One or more distributions run in this VM, each kept apart from the others. Microsoft builds the Linux kernel from the official Linux source code and delivers it with updates; the distribution comes from its vendor, in the case of Ubuntu from Canonical.
:::

::::beispiel The VM behind WSL 2
By default, the WSL 2 VM gets at most half of the computer's memory. On this chapter's test computer, Windows reports 63.5 GB of memory; the Ubuntu in WSL 2 reports 31 GB of it, just under half. A program that runs under Windows notices nothing of this VM; a program in Linux sees only the VM and not the rest of the computer.
::::

⁠**In short:** WSL 2 is a real Linux in a small VM that Windows manages itself.

:::hintergrund WSL 1 and WSL 2
The first version of WSL, now called WSL 1, had no Linux kernel. It translated every system call of a Linux program into suitable calls to the Windows kernel. This was elegant, but never complete: some system calls had no counterpart under Windows, and programs that needed them did not run. WSL 2 takes the opposite approach. Because a real Linux kernel runs in it, it understands every system call, and every Linux program runs. The price is that Linux and Windows now live in two separate machines and have to exchange files across a boundary. If you set up WSL today, you get WSL 2.
:::

### Setting up WSL 2

<span class="anker" id="stufe-4-2"></span>

Setting it up consists of a single command, a few minutes of waiting and a restart. After that, you create a user in Ubuntu.

**Requirements.** You need Windows 11 or Windows 10 version 2004 or later, administrator privileges on your computer and an internet connection. Windows Home is sufficient.

**Steps.** This is how you set up WSL 2 with Ubuntu 26.04:

<ol>

<li>

Right-click the Start button and select “Terminal (Admin)”, on Windows 10 “Windows PowerShell (Admin)”; confirm the User Account Control prompt. A PowerShell with administrator privileges opens.

</li>

<li>

Type the following command and press Enter:

```console
PS> wsl --install -d Ubuntu-26.04
```

Windows switches on the necessary features, downloads the Linux kernel and the distribution and sets up both.

</li>

<li>

Restart the computer when you are prompted to.

</li>

<li>

After the restart, Ubuntu opens by itself; otherwise, you start it from the Start menu. On the first start, Ubuntu asks for a user name and a password. Choose a short name in lowercase letters without spaces, such as `student`. When you type the password, no characters appear; this is intentional. Remember the password well: Linux asks for it later when you carry out system administration tasks.

</li>

</ol>

If WSL is already set up on the computer, for example with another distribution, `wsl --install` only displays a help text. In that case, the command from step 2 still installs the distribution, and `wsl --list --online` shows which ones are available.

::::beispiel What WSL downloads during setup
The distribution comes as a single file that contains all the files of an Ubuntu system. For Ubuntu 26.04.1, Canonical provides it under the name `ubuntu-26.04.1-wsl-amd64.wsl`, about 400 MB in size. During setup, WSL unpacks it into a virtual hard disk, which from then on contains the Linux system.
::::

⁠**In short:** `wsl --install -d Ubuntu-26.04` in an administrator PowerShell, restart, create a user.

:::hintergrund Who owns the Linux account
The user you create on the first start belongs only to this one distribution and has nothing to do with your Windows account. In Ubuntu, this user is an administrator of the system: with their password, they may carry out tasks that require special privileges, such as installing software. Chapter 7 explains how this works. If you have forgotten the password, it can be reset from Windows, because Windows, as the host, has complete control over the VM.
:::

### Listing the distributions

<span class="anker" id="stufe-4-3"></span>

After setting it up, you want to know whether everything worked. Three commands in an ordinary PowerShell, without administrator privileges, provide the information.

::::beispiel What WSL reveals about itself
The first command lists the distributions on this computer, the second the version numbers, the third all distributions that you could set up (shortened here):

```console Windows (PowerShell)
PS> wsl -l -v
  NAME            STATE           VERSION
* Ubuntu-26.04    Stopped         2
PS> wsl --version
WSL-Version: 2.6.3.0
Kernelversion: 6.6.87.2-1
WSLg-Version: 1.0.71
MSRDC-Version: 1.2.6353
Direct3D-Version: 1.611.1-81528511
DXCore-Version: 10.0.26100.1-240331-1435.ge-release
Windows-Version: 10.0.26200.9711
PS> wsl -l -o
Im Folgenden finden Sie eine Liste gültiger Distributionen, die installiert werden können.
Mit "wsl.exe --install <Distro>" installieren.

NAME                            FRIENDLY NAME
Ubuntu                          Ubuntu
Ubuntu-26.04                    Ubuntu 26.04 LTS
Ubuntu-24.04                    Ubuntu 24.04 LTS
Ubuntu-22.04                    Ubuntu 22.04 LTS
kali-linux                      Kali Linux Rolling
Debian                          Debian GNU/Linux
archlinux                       Arch Linux
FedoraLinux-45                  Fedora Linux 45
```

The first list contains a distribution named `Ubuntu-26.04`; the asterisk marks it as the default, that is, the one that WSL starts when nothing else is specified. `STATE` says whether it is currently running (`Running`) or stopped (`Stopped`), and `VERSION 2` confirms WSL 2. The second command gives the version of WSL itself and, in the line “Kernelversion” (“Kernel version” on an English Windows), the version of Microsoft's Linux kernel; on your computer, the numbers may be newer. In the third list, `Ubuntu` without a number stands for whichever LTS release is the latest, `Ubuntu-26.04` for exactly this one.
::::

⁠**In short:** `wsl -l -v` shows which distributions are set up and whether they run under WSL 2.

### Opening and checking the terminal

<span class="anker" id="stufe-4-4"></span>

You open a Linux terminal in WSL in one of three ways: from the Start menu, which lists the distribution by its name; in the Windows app “Terminal”, via the arrow next to the plus sign and the entry `Ubuntu-26.04`; or in a PowerShell with the command `wsl`. The prompt `student@labor:~$` appears, with your user name in place of `student` and the name of your computer in place of `labor`.

::::beispiel Three commands for checking
You know the first command from subsection [2.3](drei-wege-zu-einem-eigenen-linux.html#stufe-2-3), here only with the first line; the second gives the version of the running kernel, the third whether the system runs in a virtual machine:

```console Linux (WSL 2)
$ cat /etc/os-release
PRETTY_NAME="Ubuntu 26.04.1 LTS"
...
$ uname -r
6.6.87.2-microsoft-standard-WSL2
$ systemd-detect-virt
wsl
```

The three dots stand for the remaining lines of the file. The kernel has `microsoft` in its name, because Microsoft built it; it is a different kernel from the one Ubuntu uses on a real PC. The third command confirms that Linux runs in the WSL VM.
::::

⁠**In short:** In the WSL terminal, `cat /etc/os-release` shows the distribution and `uname -r` shows Microsoft's kernel.

### Windows files in Linux: /mnt/c

<span class="anker" id="stufe-4-5"></span>

A file that you want to edit in Linux is often already on Windows, for example in the “Downloads” folder. Linux in WSL can get at the whole of drive C:, but under an unfamiliar name.

**A tree without drive letters.** Linux has no drive letters like C: or D:. All files and folders hang in a single tree whose root is called `/`; a folder in it is described with slashes, such as `/etc` or `/home/student`. Chapter 3 explains how to move around in this tree. WSL shows the Windows drive C: in the folder `/mnt/c`, D: under `/mnt/d` and so on.

::::beispiel A Windows folder, seen from Linux
The command `ls` shows what is in a folder. The folder `/mnt` contains the drives, and a folder deep in the Windows directory contains files that Windows needs for the network:

```console Linux (WSL 2)
$ ls /mnt
c  wsl  wslg
$ ls /mnt/c/Windows/System32/drivers/etc
hosts  hosts.ics  lmhosts.sam  networks  protocol  services
```

The rule is: drive letter in lowercase under `/mnt`, slashes instead of backslashes. In this way, the Windows folder `C:\Windows\System32\drivers\etc` becomes the following folder in Linux: `/mnt/c/Windows/System32/drivers/etc`.
::::

There is one special feature under `/mnt/c`. Everywhere else, Linux distinguishes between uppercase and lowercase letters; `Notiz.txt` and `notiz.txt` are two different files. On the Windows drive, however, the rules of Windows apply, and there the case does not matter: `/mnt/c/windows/system32` leads to the same folder as `/mnt/c/Windows/System32`.

⁠**In short:** Linux in WSL finds drive C: under `/mnt/c`.

### Linux files in Windows: File Explorer

<span class="anker" id="stufe-4-6"></span>

Conversely, you sometimes want to open a file that was created in Linux with a Windows program. For this, the Windows File Explorer shows an entry “Linux” in the navigation pane on the left; below it is every distribution that is set up, with its whole tree.

In File Explorer, the address of a Linux folder begins with `\\wsl.localhost\` and the name of the distribution. The home folder of `student` in Ubuntu-26.04 is therefore called `\\wsl.localhost\Ubuntu-26.04\home\student`. Older instructions write `\\wsl$\` instead of `\\wsl.localhost\`; both forms lead to the same place. From within a Linux terminal, the command `explorer.exe .` opens File Explorer in exactly the folder you are currently working in; the dot at the end is part of the command.

::::beispiel A Linux file, seen from Windows
In the home folder in Ubuntu, there is a folder `linuxk1` and in it a folder `pruefung` with three small files. PowerShell displays them under the File Explorer address:

```console Windows (PowerShell)
PS> Get-ChildItem \\wsl.localhost\Ubuntu-26.04\home\student\linuxk1\pruefung

    Verzeichnis: \\wsl.localhost\Ubuntu-26.04\home\student\linuxk1\pruefung


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
------        09.11.2026     16:32             12 gruss2.txt
------        09.11.2026     16:32             76 PRUEFSUMMEN
------        09.11.2026     16:32             12 gruss.txt
```

The order of the files here is not alphabetical, but the one in which the file server on the Linux side delivers them.
::::

:::warnung Touch the WSL files only via `\\wsl.localhost`
The entire Linux system of WSL is contained in a single file named `ext4.vhdx`, which Windows stores deep in the `AppData` folder of your Windows user. Never open, move or delete this file with Windows programs, and do not edit anything in its folder: this can damage the distribution so badly that it no longer starts. The safe way to Linux files always leads through the entry “Linux” in File Explorer, that is, via `\\wsl.localhost`.
:::

⁠**In short:** Windows sees the Linux files in File Explorer under “Linux”; the address is `\\wsl.localhost\Ubuntu-26.04`.

### Where should the practice files go?

<span class="anker" id="stufe-4-7"></span>

Because each side can get at the files of both, the question naturally arises where best to store your practice files. The answer is clear: in the Linux part, for example in the home folder `/home/student`, and not under `/mnt/c`, if you mainly work with them in Linux. Microsoft recommends this too.

::::beispiel The same copying, measured twice
For this chapter, a folder with 3 559 small files, 52 MB in total, was copied twice in WSL: once into the home folder in Linux and once into a folder on C: under `/mnt/c`. In the Linux part, this took between 0.13 and 0.69 seconds; under `/mnt/c`, about 37 seconds each time. That is roughly fifty to three hundred times as long, or about 10 milliseconds for each individual file. The script for this is included with the code files of this chapter.
::::

⁠**In short:** Files that you work with in Linux belong in the Linux part, not in `/mnt/c`.

:::hintergrund Why the trip across the boundary takes so much longer
Linux and Windows run in two separate machines, and neither can read the other's storage devices directly. When Linux accesses `/mnt/c`, every single step, that is, creating, opening, writing and closing a file and setting its properties, becomes a message to a program on the Windows side. This program, a file server, carries out the step with the Windows kernel and sends the reply back. The messages follow a fixed protocol called 9P. When many small files are copied, the work consists almost entirely of such individual steps, and each one costs a round trip across the boundary of the VM. In the Linux part, by contrast, the Linux kernel carries out the same steps directly on its own virtual hard disk. In the opposite direction, when Windows reads Linux files via `\\wsl.localhost`, a file server on the Linux side works in the same way.
:::

### Limits of WSL 2

<span class="anker" id="stufe-4-8"></span>

WSL 2 is sufficient for everything this series shows on the command line, in programming and in data analysis. In three places, however, you notice that Linux lives in a VM of its own.

<ul>

<li>

⁠**Network.** The WSL 2 VM is connected to Windows in the NAT mode from subsection [3.6](virtuelle-maschinen-der-rechner-im-rechner.html#stufe-3-6) and gets an address of its own, which can change at every restart. Linux gets onto the internet; without additional settings, it cannot be reached from other devices in the home network. Linux does not see the traffic of the computer's real network card.

</li>

<li>

⁠**Devices.** Linux does not see USB devices, such as a USB Wi-Fi stick or a card reader, on its own. You can pass them through to WSL with an add-on program called usbipd-win; as long as they are attached to WSL, Windows cannot use them.

</li>

<li>

⁠**Updates.** Windows updates WSL and the Linux kernel, but not the programs of the distribution. You update those yourself in Linux, as Chapter 9 shows.

</li>

</ul>

If you want to build several computers in a network of your own or examine the network traffic of the real network card, use a VM with VirtualBox or the live USB stick.

⁠**In short:** WSL 2 is ideal for the command line and programming; for network labs and your own devices, it is too far removed from the hardware.

### Exercises for Section [4](#stufe-4)

<span class="anker" id="stufe-4-9"></span>

:::aufgabe Exercise 11 ★★ Setting up and checking WSL 2
<span class="anker" id="aufg-11"></span>

Set up WSL 2 with Ubuntu 26.04 as described in subsection [4.2](#stufe-4-2). Then open an ordinary PowerShell and run `wsl -l -v`, then in the Ubuntu terminal `cat /etc/os-release` and `uname -r`. How can you tell from the three outputs that (a) Ubuntu 26.04 is set up, (b) it runs under WSL 2 and (c) the kernel comes from Microsoft?

:::loesung
On this chapter's test computer, the outputs look like this:

```console Windows (PowerShell)
PS> wsl -l -v
  NAME            STATE           VERSION
* Ubuntu-26.04    Stopped         2
```

```console Linux (WSL 2)
$ cat /etc/os-release
PRETTY_NAME="Ubuntu 26.04.1 LTS"
...
$ uname -r
6.6.87.2-microsoft-standard-WSL2
```

(a) `PRETTY_NAME="Ubuntu 26.04.1 LTS"` and `VERSION_ID="26.04"` in `/etc/os-release` show Ubuntu 26.04. (b) The column `VERSION` of `wsl -l -v` shows `2`. If the distribution is currently running, `STATE` shows `Running`. (c) The kernel name contains `microsoft-standard-WSL2`: it is the kernel of the WSL 2 VM, built by Microsoft. The numbers in front of it may be newer on your computer.
:::
:::

:::aufgabe Exercise 12 ★ Files across the boundary
<span class="anker" id="aufg-12"></span>

<ol class="al">

<li>

On Windows, use Notepad to create a small text file `hallo.txt` in the “Documents” folder. What is its name in Linux? Display the contents of the folder with `ls`. (Your Windows user name appears in File Explorer in the address of the folder.)

</li>

<li>

In the Ubuntu terminal, open File Explorer with `explorer.exe .`. Which address does it show?

</li>

</ol>

:::loesung
(a) If the file is at `C:\Users\<Name>\Documents\hallo.txt` on Windows, its name in Linux is `/mnt/c/Users/<Name>/Documents/hallo.txt`; `<Name>` is your Windows user name. Note: On a Windows in another language, File Explorer may show the folder under a translated name, a German Windows, for example, as “Dokumente”, but its real name on the disk is `Documents`. If you click in the address bar of File Explorer, the real path appears. The command is then, for example, `ls /mnt/c/Users/<Name>/Documents`, and its output includes `hallo.txt`. If folder backup to OneDrive is switched on for you, however, “Documents” is in the OneDrive folder, and the path begins with `/mnt/c/Users/<Name>/OneDrive`.

(b) File Explorer opens the folder in which the terminal is currently working. Right after opening the terminal, that is your home folder. The address is then the following, where your Linux user name takes the place of the part in angle brackets: `\\wsl.localhost\Ubuntu-26.04\home\<dein Linux-Name>`.
:::
:::

:::aufgabe Exercise 13 ★★ Is WSL 2 really a VM?
<span class="anker" id="aufg-13"></span>

In your WSL terminal, collect three indications that Linux runs in a virtual machine. Use `systemd-detect-virt`, `uname -r` and the command `lsblk -o NAME,SIZE,MODEL`, which lists the system's storage devices with their size and model. What do you notice about the model of the storage devices? How does the size of the largest storage device compare with the free space on your real SSD?

:::loesung
On this chapter's test computer, the three commands answer like this:

```console Linux (WSL 2)
$ systemd-detect-virt
wsl
$ uname -r
6.6.87.2-microsoft-standard-WSL2
$ lsblk -o NAME,SIZE,MODEL
NAME   SIZE MODEL
sda  388.6M Virtual Disk
sdb    186M Virtual Disk
sdc      8G Virtual Disk
sdd      1T Virtual Disk
```

First indication: `systemd-detect-virt` recognizes the environment and reports `wsl`; on a real computer, it would report `none`. Second indication: The kernel comes from Microsoft and not from Ubuntu. Third indication: All storage devices are called `Virtual Disk`; they are virtual hard disks that WSL provides to the VM as files, not real devices. The size of `sdd`, `1T`, that is, 1 TiB, is neither the size of your SSD nor the free space on it, but the maximum size up to which the file `ext4.vhdx` may grow. In fact, it occupies only as much space on the SSD as Linux has written into it as data.
:::
:::

:::aufgabe Exercise 14 ★★ Where should the project go?
<span class="anker" id="aufg-14"></span>

A fellow student stores his Python project with 2 000 small files under `C:\Users\max\projekt` and works in WSL in the folder `/mnt/c/Users/max/projekt`. He is surprised that every test run takes half a minute. Explain to him what is probably causing this, use the measured times from subsection [4.7](#stufe-4-7) to estimate how much time it costs just to create all the files across the boundary once, and suggest a better place to store them. How does he then get at his files from Windows?

:::loesung
The project is on the Windows side, and the tests run in Linux. Every file access of the tests therefore travels as a message across the boundary of the VM to the file server on the Windows side and back. With many small files, this takes many times as long.

Estimate with the measurement from subsection [4.7](#stufe-4-7): 37 seconds for 3 559 files is about 10 ms per file. Just creating 2 000 files across the boundary once therefore takes roughly

$$2\,000\cdot10\ \mathrm{ms}=20\ \mathrm{s}.$$

This is only an estimate, because reading, writing and checking cost different amounts depending on the kind of access; but it shows that half a minute per test run can easily arise from the boundary alone.

Better: Move the project into the Linux part, for example to `/home/max/projekt`, and work there. From Windows, Max then reaches it in File Explorer under “Linux” or at `\\wsl.localhost\Ubuntu-26.04\home\max\projekt`. Now the way across the boundary is taken only when he opens a file from Windows, not on every test run.
:::
:::

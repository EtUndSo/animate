---
title: A virtual machine with VirtualBox
pfad: Computer Science / Linux and the Command Line / A Linux to Practice On: WSL, Virtual Machine, Live USB Stick
adresse: informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick
knoten: Chapter 1: A Linux to Practice On: WSL, Virtual Machine, Live USB Stick
order: 6060800
summary: This section sets up the second way: a virtual machine with VirtualBox in which Ubuntu 26.04 is installed.
tags: 
lang: en
---

<span class="anker" id="stufe-7"></span>

:::zweck
This section sets up the second way: a virtual machine with VirtualBox in which Ubuntu 26.04 is installed. It assumes the concepts from Section [3](virtuelle-maschinen-der-rechner-im-rechner.html#stufe-3), the image from Section [5](datentrager-abbild-und-prufsumme.html#stufe-5) and the boot chain from Section [6](wie-ein-pc-startet.html#stufe-6). At the end, you have a Linux to practice on with a snapshot that you can return to at any time.
:::

### Setting up VirtualBox

<span class="anker" id="stufe-7-1"></span>

VirtualBox is the hypervisor this way works with. It is free of charge, runs on Windows, macOS and Linux and, at its core, is open source software under the GNU General Public License, version 3.

**Steps.** This is how you set up VirtualBox:

<ol>

<li>

On [https://www.virtualbox.org](https://www.virtualbox.org), download the “Windows hosts” package under “Downloads”. This series uses VirtualBox 7.2.

</li>

<li>

Run the file and follow the installer with the suggested settings. It asks for administrator privileges and sets up a virtual network device; the network connection may drop briefly in the process.

</li>

<li>

You do not need the *Extension Pack*, which is offered on the same page. It contains additional functions that play no role for a Linux to practice on, and it is under a license of its own that limits free use to personal and educational purposes.

</li>

</ol>

::::beispiel VirtualBox alongside WSL 2
If WSL 2 is set up on the computer, or if a security function that uses the Microsoft hypervisor is active, VirtualBox cannot access hardware virtualization directly itself. It then uses the Microsoft hypervisor as its foundation, as described in the “Background” box in subsection [3.3](virtuelle-maschinen-der-rechner-im-rechner.html#stufe-3-3). The VM still runs, but noticeably more slowly; VirtualBox indicates this with a small green turtle at the bottom right of the VM window. For a Linux to practice on, this is not an obstacle.
::::

⁠**In short:** Install VirtualBox from [https://www.virtualbox.org](https://www.virtualbox.org), without the Extension Pack.

### Switching on hardware virtualization

<span class="anker" id="stufe-7-2"></span>

If Task Manager shows “Virtualization: Enabled” (Exercise [7](virtuelle-maschinen-der-rechner-im-rechner.html#aufg-7)), skip this subsection. If it says “Disabled”, the hardware virtualization from subsection [3.4](virtuelle-maschinen-der-rechner-im-rechner.html#stufe-3-4) must be switched on in the firmware.

:::warnung Change only that one setting
A change in the firmware is an intervention in the boot chain. Back up the recovery key beforehand, as described in subsection [6.5](wie-ein-pc-startet.html#stufe-6-5). In the firmware, change only the setting for virtualization and nothing else, not Secure Boot or the boot order either; Microsoft expressly advises changing only what you really need in the firmware. If you are unsure, leave the firmware without saving.
:::

**Steps.** Open the firmware via Settings $\to$ System $\to$ Recovery $\to$ Advanced startup $\to$ “Restart now” $\to$ “Troubleshoot” $\to$ “Advanced options” $\to$ “UEFI Firmware Settings”. Depending on the manufacturer, the setting is called something like “Intel Virtualization Technology”, “Intel VT-x”, “SVM Mode” or “AMD-V” and is usually found under “Advanced”, “CPU Configuration” or “Security”. Set it to “Enabled”, save and restart. Afterward, Task Manager shows “Enabled”.

⁠**In short:** If hardware virtualization is off, you switch on only this one setting in the firmware, with the recovery key backed up.

### Creating a VM

<span class="anker" id="stufe-7-3"></span>

For the VM, you need the image `ubuntu-26.04.1-desktop-amd64.iso` from [https://ubuntu.com/download/desktop](https://ubuntu.com/download/desktop), checked as in subsection [5.6](datentrager-abbild-und-prufsumme.html#stufe-5-6). Then you create a new VM in VirtualBox.

**Steps.** In VirtualBox, click “New”. The wizard asks, one after the other, for the following:

<ol>

<li>

⁠**Name and image.** Enter a name, such as `ubuntu-labor`, and select the checked ISO image. From it, VirtualBox recognizes the type and version of the system.

</li>

<li>

⁠**Skipping unattended installation.** VirtualBox offers to install Ubuntu by itself. Decline: depending on the version, you either check “Skip Unattended Installation” or clear the check box for unattended installation. It does not always work with new Ubuntu releases, and by hand, you see what happens.

</li>

<li>

⁠**Memory and processors.** According to the vendor, Ubuntu 26.04 needs at least 6 GB of memory and a processor with two cores. Give the VM 6 GB (6 144 MB) and 2 processors if your computer has 16 GB or more.

</li>

<li>

⁠**Hard disk.** Create a new virtual hard disk with at least 25 GB. Keep the default that the file grows only with its contents.

</li>

</ol>

Whether the VM starts with UEFI or in the old BIOS mode makes no difference for Ubuntu; keep the default.

::::beispiel Planning memory
On a computer with 16 GB, a VM with 6 GB still leaves 10 GB for Windows and its programs; that is enough. With 32 GB, you can also give the VM 8 GB, and 24 GB remain. On a computer with only 8 GB, a mere 2 GB would remain for Windows, and both systems would become painfully slow. There, it is better to use WSL 2, which takes memory as needed and releases it again.
::::

⁠**In short:** A new VM with the checked image, without unattended installation, with 6 GB of memory, 2 processors and a 25 GB disk.

:::hintergrund Why a 25-GB disk takes up hardly any space at first
The file of a new virtual hard disk initially contains only its management data. Only when the guest writes to a sector does VirtualBox allocate the space for it in the file. Sectors that have never been written to are read by the guest as zeros, without being stored anywhere. On Linux, the same principle exists for ordinary files: in the experiments for this chapter, an image file the size of a 512-GB SSD that contained only a partition table took up just 40 KiB on the real disk.
:::

### Installing Ubuntu in the VM

<span class="anker" id="stufe-7-4"></span>

When you start the new VM, it behaves like a newly bought computer with a DVD inserted: its virtual firmware finds nothing on the empty hard disk and starts from the virtual DVD drive that holds the image. The Ubuntu installer appears.

**Steps.** In the installer, you choose, one after the other, the language, accessibility, the keyboard layout and the internet connection; in NAT mode, the VM already has a connection. Then comes the choice between “Try Ubuntu” and “Install Ubuntu”: here, in the VM, choose to install. For the type of installation, choose the simple option that uses the entire hard disk, then the user name, password and time zone. After the installation, the VM restarts; VirtualBox usually removes the image from the virtual DVD drive by itself in the process.

::::beispiel “Erase disk” in the VM
The installer offers to erase the entire hard disk and install Ubuntu on it. On a real computer, this would destroy Windows with all its data. In the VM, it affects only the virtual hard disk, that is, the new, empty file from subsection [7.3](#stufe-7-3). The guest does not even see the host's SSD, so it cannot erase it either.
::::

⁠**In short:** In the VM, you install Ubuntu quite normally, because everything the installer erases is the virtual hard disk.

### The first snapshot

<span class="anker" id="stufe-7-5"></span>

Right after the installation, the system is clean. You capture this state before you try out anything.

**Steps.** Shut down Ubuntu in the VM. In VirtualBox, select the VM and open the “Snapshots” view via the menu next to its name. Create a new snapshot there and name it `sauber`. If you want to go back later, select it in the same view and restore it; in the process, VirtualBox offers to save the current state as a snapshot first.

:::warnung Restoring discards everything that came afterward
If you return to a snapshot, everything that the VM has saved since this snapshot is gone, including your own files. If you want to keep something, save it beforehand as a new snapshot or copy it out of the VM.
:::

⁠**In short:** After the installation, create a snapshot “sauber”; you can return to it at any time, but you lose everything that came later.

### The terminal in the VM

<span class="anker" id="stufe-7-6"></span>

In Ubuntu, you open the terminal with the key combination Ctrl+Alt+T or via the app overview (Show Apps), in which you type “Terminal”. There, as with WSL 2, you check the distribution and the kernel with `cat /etc/os-release` and `uname -r`. The distribution reports with the same lines as in subsection [2.3](drei-wege-zu-einem-eigenen-linux.html#stufe-2-3). The kernel, however, is a different one than in WSL 2: in the VM, the kernel that Ubuntu itself builds for PCs is running. Its name does not contain `microsoft`; for Ubuntu on desktop computers, it ends in `-generic`.

The VM is connected to the network in the NAT mode from subsection [3.6](virtuelle-maschinen-der-rechner-im-rechner.html#stufe-3-6): it can reach the internet, but it cannot be reached from outside.

⁠**In short:** Ctrl+Alt+T opens the terminal in Ubuntu; there, `uname -r` shows Ubuntu's kernel.

### Exercises for Section [7](#stufe-7)

<span class="anker" id="stufe-7-7"></span>

:::aufgabe Exercise 21 ★★ A VM with a snapshot
<span class="anker" id="aufg-21"></span>

Set up VirtualBox, create a VM with Ubuntu 26.04, install Ubuntu in it and create the snapshot `sauber`. Check with `cat /etc/os-release` and `uname -r` in the terminal of the VM. Then create a file `test.txt` on the desktop of the VM, shut down the VM and return to the snapshot `sauber`. What do you expect before you start the VM again? Check it.

:::loesung
After returning to the snapshot `sauber`, `test.txt` has disappeared. The file was created after the snapshot and was therefore in the differencing image, which is discarded when restoring. The VM starts in the state directly after the installation. In the terminal output of the VM, `cat /etc/os-release` shows the same lines as in subsection [2.3](drei-wege-zu-einem-eigenen-linux.html#stufe-2-3), and `uname -r` shows a kernel whose name ends in `-generic` and does not contain `microsoft`.
:::
:::

:::aufgabe Exercise 22 ★★ Why “Erase disk” is harmless in the VM
<span class="anker" id="aufg-22"></span>

Using the concepts guest, hypervisor and virtual hard disk, explain why choosing “Erase disk and install Ubuntu” in the VM does not endanger the files of Windows. Which file on the host does the guest actually change in the process? What would have to happen for the guest to be able to write to the host's SSD after all?

:::loesung
The guest sees only the hardware that the hypervisor simulates for it. As its hard disk, it sees the virtual hard disk, and on the host, that is an ordinary file, in VirtualBox by default `ubuntu-labor.vdi` in the folder `VirtualBox VMs\ubuntu-labor` of the Windows user. When the installer “erases the whole disk”, the guest kernel writes new partitions and file systems to this virtual hard disk. Each of these write accesses is a privileged device access that the hypervisor traps and writes into this one file. The host's SSD with Windows is not a device of the VM; the guest does not even know that it exists.

For the guest to be able to write to the host's SSD, you would have to assign the SSD to it explicitly as a device; VirtualBox can do that, but only via a setting for experts that you never use here. The guest could also get at individual files of the host if you share a folder of the host with it; this, too, happens only if you explicitly ask for it. Otherwise, the only remaining possibility would be a bug in the hypervisor itself that breaks the separation between guest and host.
:::
:::

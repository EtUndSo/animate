---
title: Virtual machines: the computer within the computer
pfad: Computer Science / Linux and the Command Line / A Linux to Practice On: WSL, Virtual Machine, Live USB Stick
adresse: informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick
knoten: Chapter 1: A Linux to Practice On: WSL, Virtual Machine, Live USB Stick
order: 6060400
summary: Two of the three ways rest on the same idea: a program simulates a whole computer in which a second operating system runs.
tags: virtual machine, host, guest, hypervisor, Hardware virtualization, snapshot, address, NAT mode
lang: en
---

<span class="anker" id="stufe-3"></span>

:::zweck
Two of the three ways rest on the same idea: a program simulates a whole computer in which a second operating system runs. This section explains how this works, why the guest does not notice, how you capture such a computer in a particular state and how it gets onto the internet without being reachable from there.
:::

### The virtual machine

<span class="anker" id="stufe-3-1"></span>

A second PC for trying things out would be ideal: you could install anything on it, change any setting and, in the worst case, start over without your own computer taking any harm. Such a second PC can also be built in software.

Figure [5](#abb-5) shows the idea. The real computer runs Windows as usual. Within it, a program provides a second, simulated computer with its own processor, main memory, hard disk and network card. Linux runs in this simulated computer as if it were sitting on real hardware.

:::abbildung linux/k1vm 5
A virtual machine. The hypervisor, a program on the host, gives the guest simulated hardware. The guest kernel controls this virtual hardware as if it were real; its hard disk is actually a file on the host's SSD.
:::

:::definition Definition 3.1 (Virtual machine)
<span class="anker" id="satz-3-1"></span>

A __virtual machine__ (VM) is a computer simulated by software, with its own processor, main memory, storage devices and network card. It runs a complete operating system with its own kernel, which behaves as if it were running on real hardware.
:::

::::beispiel What a VM gets from a laptop
A laptop has 8 processor cores, 16 GB of memory and a 512 GB SSD. A VM for Ubuntu gets 2 cores, 6 GB of memory and a 25 GB hard disk of this. For the Ubuntu in the VM, there are only these 2 cores, these 6 GB and these 25 GB; it does not see the rest of the laptop. On the laptop, the VM's 25 GB hard disk is a single file that is initially only as large as the data actually stored in it.
::::

⁠**In short:** A virtual machine is a computer made of software in which a whole operating system runs.

### Host and guest

<span class="anker" id="stufe-3-2"></span>

As soon as two operating systems run on one computer, you need names to tell them apart.

:::definition Definition 3.2 (Host, guest)
<span class="anker" id="satz-3-2"></span>

The __host__ is the real computer with the operating system under which the virtual machine runs. The __guest__ is the operating system that runs in the virtual machine.
:::

::::beispiel One host, several guests
A laptop with Windows 11 runs two virtual machines, one with Ubuntu 26.04 and one with Debian. Windows 11 is the host; Ubuntu and Debian are two guests. If the Debian guest crashes, Windows and the Ubuntu guest keep running, because each guest has its own kernel in its own virtual machine.
::::

⁠**In short:** The host is the real computer, the guest is the system in the VM.

### The hypervisor

<span class="anker" id="stufe-3-3"></span>

Some program has to provide the virtual hardware, allot the guest a share of the real hardware and make sure that it does not get more.

:::definition Definition 3.3 (Hypervisor)
<span class="anker" id="satz-3-3"></span>

A __hypervisor__ is the software that creates and runs virtual machines. It allots them processor time, main memory and storage devices, simulates their devices and separates them from one another and from the host.
:::

::::beispiel [Examples] Four hypervisors
For Windows computers, these are the main hypervisors to consider: **VirtualBox** from Oracle, open source and free of charge; **VMware Workstation Pro**, free of charge for everyone since November 2024; **Hyper-V** from Microsoft, which is included in the Pro, Enterprise and Education editions of Windows 10 and 11, but not in Windows Home; and **QEMU**, an open source hypervisor that is used mainly under Linux. This chapter sets up a VM with VirtualBox.
::::

⁠**In short:** The hypervisor builds the virtual machines and watches over them.

:::hintergrund Two kinds of hypervisors
A hypervisor like VirtualBox is an ordinary program that runs under Windows and uses its kernel to access the hardware. It is called a *type 2 hypervisor*. A *type 1 hypervisor*, by contrast, starts directly on the hardware, before any operating system, and all operating systems run on top of it. Hyper-V is such a type 1 hypervisor. When it is switched on, even Windows itself no longer runs directly on the hardware, but in a special area above the hypervisor, which Microsoft calls the root partition; there, however, it is the only system with direct access to the devices. This is not an exotic case. The hypervisor itself, on which Hyper-V is built, is also included in Windows Home; only the programs with which you create VMs of your own are missing there. Many Windows computers switch on this Microsoft hypervisor for security features and for WSL 2 without the user noticing. If it is running, VirtualBox uses it as its foundation instead of accessing the hardware directly itself.
:::

### Hardware virtualization

<span class="anker" id="stufe-3-4"></span>

The guest kernel is an ordinary Linux kernel. It wants to run in kernel mode and execute privileged instructions, for example to set where a system call jumps or to address a device. But if it really ran in the kernel mode of the real processor, it could control the whole real machine, and the hypervisor would no longer have any say.

**How the guest runs fast and is still locked in.** The way out is the same as with the system call in subsection [1.4](betriebssystem-kernel-und-distribution.html#stufe-1-4), only one level lower. The guest kernel runs directly on the processor, instruction by instruction, and therefore almost as fast as on real hardware. However, the processor runs it in a separate operating mode for guests. Settings that the guest kernel makes in this mode apply only to its VM. As soon as it wants to do something that would affect the real machine, such as addressing a device, the processor stops it and hands control to the hypervisor. The hypervisor looks at what the guest wanted, carries it out on the virtual hardware and lets the guest continue. The guest notices nothing of this.

:::definition Definition 3.4 (Hardware virtualization)
<span class="anker" id="satz-3-4"></span>

__Hardware virtualization__ is an extension of the processor with which a hypervisor lets guest systems run directly on the processor and itself gets control as soon as a guest wants to do something that would affect the real machine. At Intel it is called VT-x (Virtualization Technology), at AMD it is called AMD-V. All of today's PC processors have it; on some computers, however, it is switched off at the factory and must be switched on in the computer's basic settings.
:::

::::beispiel Whether hardware virtualization is switched on
On Windows, open Task Manager (Ctrl+Shift+Esc), select “Performance” on the left and then “CPU”. At the bottom right, it says “Virtualization: Enabled” or “Disabled”. If it says “Enabled”, both ways with a VM are possible. The command `systeminfo` in PowerShell gives a second indication. If a Microsoft hypervisor is already running on the computer, for example because WSL 2 is set up, its long output contains the line “Hyper-V Requirements: A hypervisor has been detected.” In that case, hardware virtualization is switched on anyway, because without it, no hypervisor would run.
::::

⁠**In short:** With hardware virtualization, a guest kernel runs directly on the processor, but everything that would affect the real machine ends up with the hypervisor.

:::hintergrund Why PC processors needed an extension for this
Without a separate operating mode for guests, a hypervisor has only one option: it lets the guest kernel run in user mode and traps its privileged instructions. This method, “execute directly, trap privileged instructions”, works only if every instruction that can change the state of the machine or depends on it is actually trapped in user mode. Gerald Popek and Robert Goldberg formulated this condition precisely in 1974. The x86 processors of PCs did not meet it for a long time: about seventeen instructions simply behaved differently in user mode instead of triggering a trap. One example is the instruction `POPF`, which among other things determines whether interrupts from devices are allowed; in user mode, it silently ignores this part. A guest kernel that uses it would thus get a wrong result, and the hypervisor would learn nothing about it. Early hypervisors therefore had to rewrite the guest's code before running it. Since 2005 and 2006, Intel and AMD have provided a separate operating mode for guests, in which the processor passes exactly the necessary instructions on to the hypervisor.
:::

### The snapshot

<span class="anker" id="stufe-3-5"></span>

The greatest advantage of a VM for a lab is that you can undo mistakes. You capture the state before you try something out and return to it afterward, no matter what you have done in the meantime.

Figure [6](#abb-6) shows how this works for the VM's hard disk without the hypervisor having to copy the whole disk.

:::abbildung linux/k1snapshot 6
How a snapshot captures the hard disk of a VM. The previous image file is frozen; all later write accesses go to a new file, the differencing image. When reading, the hypervisor looks there first and otherwise in the base image. Returning to the snapshot throws the differencing image away.
:::

:::definition Definition 3.5 (Snapshot)
<span class="anker" id="satz-3-5"></span>

A __snapshot__ is a saved state of a virtual machine to which you can return at any time. It comprises the settings of the VM and the contents of all its virtual hard disks; if you take it while the VM is running, it also contains the contents of its main memory.
:::

::::beispiel Resetting a lab
After installing Ubuntu in the VM, you create a snapshot named “sauber” (German for “clean”). Then you try out settings, accidentally delete important system files, and the VM no longer starts. You return to the snapshot “sauber”: the VM is exactly as it was directly after the installation. A file that you created after the snapshot has disappeared too, because it was stored in the discarded differencing image.
::::

⁠**In short:** A snapshot freezes the state of a VM, and restoring it discards everything that came afterward.

:::hintergrund Why a snapshot is ready instantly and needs hardly any space
A snapshot copies nothing. The hypervisor merely declares the previous image file unchangeable and creates an empty new file, in which from now on it records every block that is written; the method is called *copy on write*. The differencing image therefore grows only as much as the guest actually changes. Several snapshots in a row result in a chain of such files. If you delete a snapshot without returning to it, the hypervisor has to merge its changes into the neighboring file; with large changes, this can take a while and temporarily need a lot of space.
:::

### The virtual network: NAT

<span class="anker" id="stufe-3-6"></span>

A VM should be able to get onto the internet, for example to download updates. On the other hand, nobody from outside should be able to get at the practice system, on which you may be trying out something insecure at that very moment.

**Like a router at home.** Every device in a network has a number under which others reach it, its __address__. At home, your laptop and phone have addresses in a small private network that are not valid on the internet. The router sends their requests to the internet under its own address, remembers which device asked and passes the reply on to that device. A request that comes from outside without any device inside having started it cannot be assigned to anyone by the router. Figure [7](#abb-7) shows that a hypervisor can play exactly this role for its VM.

:::abbildung linux/k1nat 7
NAT mode. The VM has an address in a small network that exists only between it and the hypervisor. The hypervisor sends its connections out under the host's address and passes the replies back. A connection that starts from outside does not reach the VM.
:::

:::definition Definition 3.6 (NAT mode)
<span class="anker" id="satz-3-6"></span>

In __NAT mode__ (Network Address Translation), the hypervisor works like a router for the VM. The VM has an address of its own in a private network that exists only between it and the hypervisor. The hypervisor forwards the VM's connections under the host's address and passes the replies back to the VM. Connections that start from outside do not reach the VM as long as you do not set up forwarding.
:::

::::beispiel What works with NAT and what does not
An Ubuntu VM in VirtualBox runs in NAT mode; this is the default, and the VM usually gets the address 10.0.2.15. From inside the VM, you can open web pages and download updates, because the VM starts these connections itself. A phone on the same Wi-Fi network, on the other hand, cannot reach a web server in the VM: it does not know the address 10.0.2.15, and even a request to the laptop could not be assigned to anyone by the hypervisor.
::::

⁠**In short:** In NAT mode, the VM gets out onto the network, but nobody gets in from outside.

:::hintergrund Why NAT protects against access from outside without you having to set anything
The protection is a side effect of the translation. So that the hypervisor can deliver a reply to the right VM, it keeps a table: Which VM started which connection to which destination? When a packet comes from outside, it searches this table. If no VM started the connection, there is no entry, and the packet has no destination. Besides NAT, VirtualBox has other networking modes, in which a VM is connected differently to the host, to other VMs or to the home network; the Cybersecurity series covers which of them are suitable for an isolated practice lab. For a first Linux to practice on, NAT is the right choice.
:::

### Exercises for Section [3](#stufe-3)

<span class="anker" id="stufe-3-7"></span>

:::aufgabe Exercise 7 ★ A fact sheet for your computer
<span class="anker" id="aufg-7"></span>

On Windows, collect four pieces of information about your computer. You do not change anything in the process.

<ol class="al">

<li>

The edition and version of Windows: Settings $\to$ System $\to$ About, section “Windows specifications”.

</li>

<li>

The installed memory: in the same place under “Device specifications”.

</li>

<li>

The free space on drive C:, in File Explorer under “This PC”.

</li>

<li>

Whether hardware virtualization is switched on, as in the example in subsection [3.4](#stufe-3-4).

</li>

</ol>

In a VM, Ubuntu 26.04 needs at least 6 GB of memory and 25 GB of space. Is your computer sufficient for this if Windows is to keep at least 8 GB for itself alongside the VM? Is Hyper-V available to you?

:::loesung
The values depend on your computer. This is how you evaluate them:

<ul>

<li>

⁠**Memory.** The VM needs 6 GB, and Windows is to keep 8 GB, so 14 GB together. With 16 GB, that is enough; with 8 GB, it is not, and then WSL 2 is the better way.

</li>

<li>

⁠**Space on C:.** The VM needs 25 GB, the image another 6.5 GB. With less than about 35 GB free, it gets tight.

</li>

<li>

⁠**Virtualization.** If Task Manager says “Enabled”, everything is ready. If it says “Disabled”, the setting must be switched on in the firmware; Section [7](eine-virtuelle-maschine-mit-virtualbox.html#stufe-7) shows how.

</li>

<li>

⁠**Hyper-V.** If “Windows specifications” lists a Pro, Enterprise or Education edition, you can use Hyper-V; with Windows Home, you cannot. VirtualBox and WSL 2 run on all editions.

</li>

</ul>

For comparison, this chapter's test computer: Windows 11 Home, 63.5 GB of memory. Memory and space are more than enough; Hyper-V as a feature of its own does not exist on Home. Nevertheless, Microsoft's hypervisor runs on this computer: `systeminfo` reports “A hypervisor has been detected”, because a security feature of Windows and WSL 2 use it.
:::
:::

:::aufgabe Exercise 8 ★★ What the guest kernel is allowed to do
<span class="anker" id="aufg-8"></span>

A guest kernel wants to (a) double a number in its VM's main memory, (b) set the location in its kernel to which a system call jumps, (c) write a block to its hard disk. Who does the work in each case, the processor directly or the hypervisor, and for whom does the result apply? Why would it be dangerous if the guest kernel were allowed to carry out (b) itself in the real kernel mode?

:::loesung
(a) The processor directly. Doubling a number in the VM's main memory is an ordinary arithmetic instruction on memory that the hypervisor has assigned to the VM anyway. It runs without a detour, and that is why the VM is almost as fast as real hardware.

(b) The setting applies only to the guest. In the operating mode for guests, the processor keeps a separate set of such settings for each guest; depending on the processor and the hypervisor, it makes the setting there directly, or it stops the guest and hands over to the hypervisor, which manages the setting for the guest. In both cases, system calls of the programs in the guest end up at the guest kernel, and the host's setting remains untouched.

(c) The hypervisor. A write access to a device is privileged. The hypervisor traps it and writes the block into the image file of the virtual hard disk; as a type 2 hypervisor, it uses a system call of the host for this.

If the guest kernel were allowed to carry out (b) in the real kernel mode, it would overwrite the entry point of the real processor. Then the system calls of all programs, including the programs of the host, would end up in its code, and it would have the whole machine in its hands. This is exactly what hardware virtualization prevents.
:::
:::

:::aufgabe Exercise 9 ★★ Tracking snapshots
<span class="anker" id="aufg-9"></span>

A VM goes through the following steps in order: install Ubuntu; snapshot “A”; create file `x.txt`; snapshot “B”; create file `y.txt`; delete `x.txt`; back to “B”; create file `z.txt`; back to “A”. Which of the three files exist at the end? How many differencing images did the hypervisor create along the way, and which ones did it discard?

:::loesung
At the end, none of the three files exists. The way there, with the model from Figure [6](#abb-6): A snapshot freezes the current image and creates a new differencing image; restoring discards the current differencing image and creates a new, empty one on top of the snapshot's state.

<ol>

<li>

Snapshot “A”: The base image with the freshly installed Ubuntu is frozen, and differencing image 1 is created.

</li>

<li>

`x.txt` is written to differencing image 1.

</li>

<li>

Snapshot “B”: Differencing image 1 is frozen and from now on belongs to “B”; differencing image 2 is created.

</li>

<li>

Creating `y.txt` and deleting `x.txt`: both in differencing image 2.

</li>

<li>

Back to “B”: Differencing image 2 is discarded, and differencing image 3 is created on top of the state of “B”. Now `x.txt` exists again, `y.txt` does not.

</li>

<li>

`z.txt` is written to differencing image 3.

</li>

<li>

Back to “A”: Differencing image 3 is discarded, and differencing image 4 is created directly on top of the base image. The state is the one directly after the installation: none of the three files.

</li>

</ol>

So four differencing images were created and two were discarded (numbers 2 and 3). Number 1 is kept, because snapshot “B” still exists; you could return to it at any time and would find `x.txt` there.
:::
:::

:::aufgabe Exercise 10 ★ What can a VM in NAT mode reach?
<span class="anker" id="aufg-10"></span>

A VM runs in VirtualBox in NAT mode. Does it work, and why (or why not)? (a) The VM downloads updates from the internet. (b) A laptop on the same Wi-Fi network calls up a web page offered by a program in the VM. (c) The VM opens a web page offered by a program on a phone on the same Wi-Fi network.

:::loesung
(a) Works. The VM starts the connection itself; the hypervisor sends it on under the host's address, remembers the connection and passes the replies back.

(b) Does not work. The connection starts from outside. The other laptop does not know the address of the VM, and even a request to the host could not be assigned to any VM by the hypervisor, because none of them started it. Only a configured forwarding would change that.

(c) Works. Here, too, the VM starts the connection; to the phone, it looks as if the laptop were asking. Whether the destination is on the internet or on your own Wi-Fi network makes no difference.
:::
:::

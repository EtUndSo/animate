---
title: Key points so far
pfad: Computer Science / Linux and the Command Line / A Linux to Practice On: WSL, Virtual Machine, Live USB Stick
adresse: informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick
knoten: Chapter 1: A Linux to Practice On: WSL, Virtual Machine, Live USB Stick
order: 6061100
summary: WSL 2, virtual machine and live USB stick: what happens inside the computer and how to do it safely
tags: 
lang: en
---

:::kern Key points so far
<ul>

<li>

The operating system manages the hardware; its core, the kernel, is the only part that runs in kernel mode. Programs run in user mode and get hardware services only via system calls.

</li>

<li>

Linux is a kernel; a distribution such as Ubuntu 26.04 LTS turns it into a complete system and maintains it for five years as an LTS release.

</li>

<li>

A virtual machine is a computer made of software. The hypervisor allocates hardware to it; thanks to hardware virtualization, the guest runs directly on the processor, and everything that would affect the real machine ends up with the hypervisor. A snapshot freezes the state; NAT lets the VM out, but nobody in.

</li>

<li>

WSL 2 is a real Linux kernel in a small VM that Windows manages. Linux sees C: under `/mnt/c`, and Windows sees the Linux files under `\\wsl.localhost`; practice files belong in the Linux part.

</li>

<li>

An image is an entire storage device in a file. The SHA-256 checksum proves that it is unchanged, but not that it is genuine; only a signature establishes that.

</li>

<li>

At startup, the firmware loads the boot loader, and the boot loader loads the kernel; Secure Boot admits only boot programs with a valid signature. Windows device encryption depends on this chain, which is why you back up the recovery key before any intervention.

</li>

<li>

A live system places a writable tmpfs in main memory as an overlay over a write-protected squashfs; after switching off, everything is gone, and the internal SSD stays unmounted.

</li>

<li>

With the live stick, almost all risks arise from a wrong storage device or from changes to the boot chain: unplug other storage, recognize the stick by its size, “Restart”, boot menu, Secure Boot on, “Try Ubuntu”.

</li>

</ul>
:::

:::merke The answer in three sentences
<ol>

<li>

On Windows, you get a Linux of your own to practice on in three ways: with WSL 2 as a small VM alongside Windows, with a virtual machine in VirtualBox or as a live system from a USB stick.

</li>

<li>

All three protect Windows because there is a boundary between the Linux you practice on and the Windows data: the hypervisor for WSL 2 and the VM, and main memory instead of the SSD for the live system.

</li>

<li>

It becomes dangerous only where you cross this boundary yourself, when writing to a storage device and when changing the boot chain, and what helps against this is a checked image, the correctly identified stick, the unchanged start via the boot menu and a backed-up recovery key.

</li>

</ol>
:::

**One principle behind all the results.** Almost everything in this chapter follows from one idea: security comes from layers that protect a lower one from an upper one, and each layer is only as secure as the path through it. The kernel protects the hardware from the programs, the hypervisor the host from the guest, the signature check the boot chain from unknown programs, and the write-protected layer the live system from changes.

| Result | Where it comes from |
|---|---|
| programs cannot get to the SSD directly | kernel mode and user mode, system call as the only gate (Section [1](betriebssystem-kernel-und-distribution.html#stufe-1)) |
| Ubuntu and Kali share the kernel, not the system | Linux is the kernel, the distribution is the whole (Section [1](betriebssystem-kernel-und-distribution.html#stufe-1)) |
| a guest cannot control the host | what would affect the real machine ends up with the hypervisor (Section [3](virtuelle-maschinen-der-rechner-im-rechner.html#stufe-3)) |
| a snapshot is ready immediately | differencing image following the copy on write principle (Section [3](virtuelle-maschinen-der-rechner-im-rechner.html#stufe-3)) |
| a VM in NAT mode cannot be reached from outside | the hypervisor delivers only replies to the VM's own requests (Section [3](virtuelle-maschinen-der-rechner-im-rechner.html#stufe-3)) |
| `uname -r` shows a kernel from Microsoft in WSL 2 | WSL 2 is a VM with its own Linux kernel (Section [4](wsl-2-linux-neben-windows.html#stufe-4)) |
| copying under `/mnt/c` takes many times as long | every file access becomes a message across the boundary of the VM (Section [4](wsl-2-linux-neben-windows.html#stufe-4)) |
| a matching checksum proves no origin | whoever swaps the file can also swap the list (Section [5](datentrager-abbild-und-prufsumme.html#stufe-5)) |
| an unknown stick starts without any setup | fixed boot path for removable storage devices in UEFI (Section [6](wie-ein-pc-startet.html#stufe-6)) |
| Ubuntu starts with Secure Boot, Kali does not | signed chain `shim`, GRUB, kernel (Section [6](wie-ein-pc-startet.html#stufe-6)) |
| a change to the firmware can make Windows demand the recovery key | the key is released only if the boot chain is unchanged (Section [6](wie-ein-pc-startet.html#stufe-6)) |
| in the live system, everything is gone after switching off | changes end up in the tmpfs above the squashfs (Section [8](das-live-system.html#stufe-8)) |
| the wrong storage device is the greatest risk | a writing tool replaces the entire selected storage device (Section [9](der-live-usb-stick-vorbereiten-schreiben-starten.html#stufe-9)) |

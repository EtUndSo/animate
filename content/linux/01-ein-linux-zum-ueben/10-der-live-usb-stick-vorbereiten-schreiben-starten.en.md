---
title: The live USB stick: preparing, writing, starting
pfad: Computer Science / Linux and the Command Line / A Linux to Practice On: WSL, Virtual Machine, Live USB Stick
adresse: informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick
knoten: Chapter 1: A Linux to Practice On: WSL, Virtual Machine, Live USB Stick
order: 6061000
summary: This section sets up the third way: Ubuntu 26.04 as a live system on a USB stick.
tags: Fast Startup, writing tool
lang: en
---

<span class="anker" id="stufe-9"></span>

:::zweck
This section sets up the third way: Ubuntu 26.04 as a live system on a USB stick. Here, you write to a storage device and start the computer in an unusual way; that is why the risks and how to guard against them come first. The section assumes Sections [5](datentrager-abbild-und-prufsumme.html#stufe-5), [6](wie-ein-pc-startet.html#stufe-6) and [8](das-live-system.html#stufe-8).
:::

### The risks at a glance

<span class="anker" id="stufe-9-1"></span>

Almost everything that can go wrong with the live stick has one of two causes: you write to the wrong storage device, or you change something in the boot chain. Table [4](#tab-4) lists the individual dangers with their safeguards; the following subsections explain them.

<span class="anker" id="tab-4"></span>

**Table 4:** The dangers of the live USB stick and how to guard against them.

| Danger | Cause | Safeguard |
|---|---|---|
| wrong storage device overwritten | the writing tool replaces the entire selected storage device | unplug other USB storage, recognize the stick by its size (subsection [9.2](#stufe-9-2)) |
| recovery key prompt | change to the boot chain | back up the key beforehand, use only the boot menu, Secure Boot on (subsection [6.5](wie-ein-pc-startet.html#stufe-6-5)) |
| Windows data damaged | after “Shut down” with Fast Startup, Windows is at rest (hibernated) | “Restart” instead of “Shut down”, do not touch the Windows partitions (subsection [9.3](#stufe-9-3)) |
| Ubuntu installed by mistake | “Install Ubuntu” chosen instead of “Try” | only “Try Ubuntu” (subsection [9.6](#stufe-9-6)) |
| stick formatted | after writing, Windows offers to format the stick | close the message with “Cancel” (subsection [9.5](#stufe-9-5)) |
| trouble with other people's devices | computers of a university or employer | start only your own computers from the stick |

⁠**In short:** If you write to the right storage device and do not change the boot chain, you take hardly any risk with the live stick.

### Recognizing the right storage device

<span class="anker" id="stufe-9-2"></span>

The writing tool completely overwrites the storage device you specify, from the partition table to the last sector. If that is accidentally the internal SSD or an external hard disk with your backup, its data is lost. This is the greatest risk of the whole way.

Windows shows all storage devices in the program “Disk Management”; you open it by right-clicking the Start button and choosing “Disk Management”. Figure [12](#abb-12) shows schematically what you see there when an 8-GB stick is plugged in.

:::abbildung linux/k1datentraeger 12
Windows Disk Management, schematically. Disk 0 is the internal SSD with the EFI system partition, drive C: and the recovery partition; Disk 1 is the stick, a removable medium with 7.45 GB. Only Disk 1 may be the target of the writing tool.
:::

:::warnung Recognize the stick reliably before writing
<ol>

<li>

Unplug all other USB storage: external hard disks, memory cards, other sticks. Then the writing tool cannot hit them.

</li>

<li>

Use a stick with at least 8 GB whose contents may be erased. Back up beforehand everything you want to keep from it.

</li>

<li>

Plug in the stick and check in Disk Management: the stick is labeled “Removable” and has the size you expect according to subsection [5.1](datentrager-abbild-und-prufsumme.html#stufe-5-1), that is, about 7.45 GB for 8 GB. The disk with drive C:, the EFI system partition and the recovery partition is the internal SSD; its partitions must never be changed.

</li>

<li>

Note the drive letter and the size of the stick, and compare both in the writing tool before you start.

</li>

</ol>
:::

⁠**In short:** Unplug other storage and recognize the stick by “Removable” and its size; only then write.

### Fast Startup in Windows

<span class="anker" id="stufe-9-3"></span>

On most computers, “Shut down” does not end Windows completely. This matters for starting from the stick, for two reasons.

:::definition Definition 9.1 (Fast Startup)
<span class="anker" id="satz-9-1"></span>

__Fast Startup__ is a function of Windows that, when shutting down, ends the programs but writes the state of the Windows kernel and its drivers to a file on drive C: and resumes from there at the next power-on instead of starting anew. It is switched on by default in Windows and takes effect only when shutting down, not with “Restart”.
:::

**Why “Restart” is the right way to the stick.** After “Shut down” with Fast Startup, the firmware at the next power-on often passes so quickly over the moment in which it responds to the key for the boot menu that you miss it. And drive C: remains in a half-used state, which Windows expects to find exactly like that when it resumes. If another system changed something there, the saved state and the disk would no longer match, and Windows could damage files. That is why Linux mounts a Windows partition that is at rest like this read-only at most. “Restart”, on the other hand, ends Windows completely and leads immediately through the firmware, where the key for the boot menu reliably works.

⁠**In short:** Go to the stick via “Restart”, not via “Shut down”, and do not touch the Windows partitions in the live system.

### Downloading and checking the image

<span class="anker" id="stufe-9-4"></span>

For the stick, you need the same image as for the VM.

**Steps.** This is how you download and check the image:

<ol>

<li>

Download the file `ubuntu-26.04.1-desktop-amd64.iso`, 6.48 GB, from [https://ubuntu.com/download/desktop](https://ubuntu.com/download/desktop).

</li>

<li>

From [https://releases.ubuntu.com/26.04/](https://releases.ubuntu.com/26.04/), download the file `SHA256SUMS` into the same folder, usually “Downloads”.

</li>

<li>

Open a PowerShell in this folder; in File Explorer, you do this by right-clicking an empty area of the folder and choosing “Open in Terminal”. Then compare with the value from the fourth line of `SHA256SUMS`:

```console Windows (PowerShell)
PS> (Get-FileHash .\ubuntu-26.04.1-desktop-amd64.iso).Hash -eq "601e30fbf5d97759367c632e2c33630665039b7e2158fd068403da3ccf1bda1f"
```

The answer must be `True`. Calculating takes a while for 6.5 GB.

</li>

<li>

If it says `False`, download the image again and do not use it under any circumstances.

</li>

</ol>

⁠**In short:** Download the image and `SHA256SUMS` from Ubuntu, compare the checksum and continue only if the answer is `True`.

### The writing tool

<span class="anker" id="stufe-9-5"></span>

An image is not copied but written (subsection [5.4](datentrager-abbild-und-prufsumme.html#stufe-5-4)). There are dedicated programs for this.

:::definition Definition 9.2 (Writing tool)
<span class="anker" id="satz-9-2"></span>

A __writing tool__ is a program that writes an image sector by sector onto an entire storage device. In doing so, it replaces the partition table and all the data of the storage device; whatever was on it before is lost afterward.
:::

Figure [13](#abb-13) shows a stick before and after writing.

:::abbildung linux/k1stick 13
An 8-GB stick before and after writing the Ubuntu image, schematic and not to scale. Before: a partition table and a FAT32 partition with files. After: a new partition table from the image, the ISO file system with the system and a small EFI system partition; the rest of the stick remains unused. The old files can no longer be found.
:::

::::beispiel [Examples] Two writing tools
⁠**balenaEtcher** ([https://etcher.balena.io](https://etcher.balena.io)) is the simplest tool and runs on Windows, macOS and Linux. By default, it does not even display system drives, and after writing, it checks whether every byte has arrived correctly. Operating it takes three steps: “Flash from file” and select the image, “Select target” and select the stick, “Flash!” and confirm the prompt from Windows.

⁠**Rufus** ([https://rufus.ie](https://rufus.ie)) runs only on Windows and has more settings. Rufus follows the language of Windows; the names here are those of the English interface. After starting it, check in the “Device” field that the stick is listed there with its letter and its size. With “SELECT”, you choose the image; leave the other settings as they are and click “START”. Rufus then asks whether it may download missing boot files (“Yes”) and in which mode it should write the image; keep “Write in ISO Image mode”. Finally, it warns that all data on the drive will be destroyed. At this moment, check the drive once more, then confirm. After about ten minutes, “READY” appears.
::::

:::warnung After writing: cancel “Format disk”
After writing, Windows often reports that you need to format the disk in a drive before you can use it. The reason is harmless: Windows cannot read the partitions from the Linux image. Click “Cancel”, never “Format disk”, otherwise the freshly written stick is empty again.
:::

⁠**In short:** A writing tool such as balenaEtcher or Rufus turns the stick into a copy of the image; everything that was on it before is gone.

:::hintergrund A stick before and after writing, measured
For this chapter, writing was simulated on an image file the size of an 8-GB stick, with the small Alpine Linux image from subsection [8.6](das-live-system.html#stufe-8-6). Before, the partition table contained a single FAT32 partition spanning the whole stick. Afterward, it contained the table from the image:

```text
Device     Boot Start    End Sectors  Size Id Type
stick.img1 *        0 137215  137216   67M  0 Empty
stick.img2        220   3099    2880  1.4M ef EFI (FAT-12/16/32)
```

Partition 1 covers the entire image with the ISO file system; partition 2 lies in the middle of it and contains the boot files for UEFI. The remaining 7.4 GiB of the stick no longer belong to any partition. The old FAT32 partition is no longer entered; its files, insofar as they lay beyond the end of the image, have not yet been overwritten, but without their file system they can no longer be found. With Ubuntu, the layout is somewhat different, but the principle is the same.
:::

:::hintergrund Why this chapter does not recommend Ventoy
A third tool, Ventoy, sets up the stick once; afterward, you simply copy any number of images onto it as files. That is convenient, but in its default setting, Ventoy bypasses the Secure Boot check, and with its own key you permanently allow the computer to start arbitrary boot programs via Ventoy. For experienced users, this can make sense; for a first live stick, balenaEtcher and Rufus are enough.
:::

### Starting from the stick: “Try Ubuntu”

<span class="anker" id="stufe-9-6"></span>

Now you start the computer from the stick. Check the warning in subsection [6.5](wie-ein-pc-startet.html#stufe-6-5) beforehand: if your drive is encrypted, the recovery key must be backed up.

:::warnung Do not install
The installer on the stick can install Ubuntu on the internal SSD and, in doing so, erase Windows with all its data. Therefore, always choose “Try Ubuntu” and never “Install Ubuntu”. Even in the running live system, an icon for installing remains visible, depending on the version in the dock at the edge of the screen or on the desktop; do not click it.
:::

**Steps.** This is how you start Ubuntu from the stick:

<ol>

<li>

Save all open files in Windows. Plug in the stick.

</li>

<li>

In the Start menu, choose “Restart”, not “Shut down” (subsection [9.3](#stufe-9-3)).

</li>

<li>

Immediately after the restart, press the key for the boot menu several times (subsection [6.2](wie-ein-pc-startet.html#stufe-6-2)), or use the way via Advanced startup.

</li>

<li>

In the boot menu, choose the entry with the name of the stick. If it appears twice, take the one that begins with “UEFI”; the other one starts in the old BIOS mode.

</li>

<li>

GRUB shows its menu; the first entry starts Ubuntu. After a while, the installer appears.

</li>

<li>

Choose the language, accessibility, keyboard layout and, if you like, a Wi-Fi network. On the page “Try or install Ubuntu”, click “Try Ubuntu”.

</li>

</ol>

Then the Ubuntu desktop appears. If Linux now runs with graphics, Wi-Fi and sound, your computer will also get along with an installed Ubuntu. For trying it out, Ubuntu uses only drivers that are available as open source software; some graphics cards therefore run more slowly than later in an installation.

⁠**In short:** “Restart”, boot menu, the “UEFI” entry with the stick, “Try Ubuntu”, never “Install”.

### In the live system: terminal and storage devices

<span class="anker" id="stufe-9-7"></span>

In the live system, you open the terminal as in the VM with Ctrl+Alt+T. `cat /etc/os-release` shows the same lines as in subsection [2.3](drei-wege-zu-einem-eigenen-linux.html#stufe-2-3), and `uname -r` shows Ubuntu's kernel. More interesting here is a look at the storage devices, because now Linux sees the real hardware.

::::beispiel The internal SSD remains untouched
The command `lsblk` with a selection of columns shows each storage device with its size, type, connection (`TRAN`, such as `usb` or `nvme`), whether it is removable (`RM`, 1 means yes) and its mount point. The following output comes from the test VM from subsection [8.6](das-live-system.html#stufe-8-6): there, the Alpine image was plugged in as a virtual USB stick, and an empty virtual SSD was partitioned like the SSD of a Windows computer.

```console Alpine Linux, live system in a test VM
# lsblk -o NAME,SIZE,TYPE,TRAN,RM,MOUNTPOINTS
NAME          SIZE TYPE TRAN   RM MOUNTPOINTS
fd0             0B disk         1
loop0        21.9M loop         0 /.modloop
sda           7.5G disk usb     1 /media/sda
├─sda1         67M part         1
└─sda2        1.4M part         1
sr0          1024M rom  ata     1
nvme0n1     476.9G disk nvme    0
├─nvme0n1p1   260M part nvme    0
├─nvme0n1p2    16M part nvme    0
├─nvme0n1p3   474G part nvme    0
└─nvme0n1p4   2.7G part nvme    0
```

The stick is `sda`: connected via USB, removable, 7.5 GiB in size and mounted under `/media/sda`, because the live system reads from it. Its two partitions come from the image. `loop0` is the squashfs from subsection [8.6](das-live-system.html#stufe-8-6): a file from the stick that Linux treats like a storage device is called a storage device of type `loop`. `fd0` and `sr0` are a floppy disk drive and a CD drive that the test VM simulates on its own. Linux calls the SSD `nvme0n1` and its partitions `nvme0n1p1` to `nvme0n1p4`. None of them has a mount point: the live system does not use the SSD. On a real computer with Ubuntu, the list looks similar; there are usually several entries of type `loop`, one for each squashfs file.
::::

:::warnung Do not mount the Windows partitions in the live system
Ubuntu also displays the partitions of the internal SSD in its file manager and mounts them when you click on them. Leave them alone: if Windows is at rest with Fast Startup, you could damage drive C:, and if it is encrypted, you cannot get to the files without the recovery key anyway. For this series, you need nothing from the internal SSD.
:::

⁠**In short:** In the live system, `lsblk` shows the internal SSD without a mount point, that is, unused.

### Finishing and converting the stick back

<span class="anker" id="stufe-9-8"></span>

To finish, choose “Power Off” or “Restart” in Ubuntu's menu at the top right. Ubuntu asks you to remove the stick, and you confirm with Enter. Without the stick, the computer starts Windows again, exactly as before. Everything you created in the live system is gone (subsection [8.6](das-live-system.html#stufe-8-6)).

You can keep the stick for further starts. If you need it as an ordinary stick again, you write it anew with a writing tool or have Rufus or Windows Disk Management create a new partition with FAT32 or exFAT. Both require the same care as writing: the target is the stick, recognized by its size, and nothing else.

⁠**In short:** Switch off, unplug the stick, and Windows starts as before; convert the stick back with the same care as when writing.

### Exercises for Section [9](#stufe-9)

<span class="anker" id="stufe-9-9"></span>

:::aufgabe Exercise 26 ★★★ A live USB stick with Ubuntu
<span class="anker" id="aufg-26"></span>

Set up the third way completely. For each step, note how you recognized that it succeeded.

<ol class="al">

<li>

Preparation: Check whether your drive is encrypted and, if necessary, back up the recovery key. Have a stick with at least 8 GB ready whose contents you no longer need, and unplug all other USB storage.

</li>

<li>

Download the image and `SHA256SUMS` and check the checksum.

</li>

<li>

Write the stick with balenaEtcher or Rufus. Identify the stick in Disk Management beforehand.

</li>

<li>

Start from the stick via “Restart” and the boot menu and choose “Try Ubuntu”. Open the terminal and run `cat /etc/os-release`.

</li>

</ol>

Checkpoints at the end: the recovery key was ready before step (c); the checksum matched; Secure Boot stayed switched on; after switching off, Windows starts as before.

:::loesung
The individual steps have succeeded if you observed the following:

<ol class="al">

<li>

The settings page shows whether device encryption or BitLocker is switched on. If so, there is a key for your computer at [https://aka.ms/myrecoverykey](https://aka.ms/myrecoverykey), and you have it on paper or on another device. Only the stick for Ubuntu is still plugged into the computer.

</li>

<li>

`(Get-FileHash .\ubuntu-26.04.1-desktop-amd64.iso).Hash -eq "601e..."` with the complete value from the fourth line of `SHA256SUMS` answers `True`.

</li>

<li>

In Disk Management, the stick was a removable medium with about 7.45 GB (for an 8 GB stick). balenaEtcher reports at the end that the writing and the subsequent verification succeeded; Rufus shows “READY”. You answered Windows' question whether to format the stick with “Cancel”.

</li>

<li>

In the boot menu, you chose the entry “UEFI:” with the name of the stick, and in the installer “Try Ubuntu”. In the terminal, `cat /etc/os-release` shows the line `PRETTY_NAME="Ubuntu 26.04.1 LTS"`.

</li>

</ol>

Secure Boot was switched on throughout, because you did not change anything in the firmware, and after switching off and unplugging the stick, Windows starts without asking anything.
:::
:::

:::aufgabe Exercise 27 ★ Observing the SSD in the live system
<span class="anker" id="aufg-27"></span>

In the live system, run `lsblk -o NAME,SIZE,TYPE,TRAN,RM,MOUNTPOINTS`. How do you recognize (a) the stick, (b) the internal SSD, (c) that the live system does not use the SSD? How many partitions does your SSD have, and do they match what Disk Management shows on Windows?

:::loesung
This is how you read the output:

<ol class="al">

<li>

You recognize the stick by `TRAN usb`, by `RM 1` (removable) and by its size, about `7.5G` for an 8 GB stick. The stick itself or one of its partitions has a mount point, because the live system reads its system from there.

</li>

<li>

The internal SSD is called `nvme0n1` if it is an NVMe SSD, and `sda` or `sdb` if it is an SSD or hard disk connected via SATA. It has `RM 0` and the size that you expect from subsection [5.1](datentrager-abbild-und-prufsumme.html#stufe-5-1), about `476.9G` for 512 GB.

</li>

<li>

No partition of the SSD has a mount point. So the system neither reads nor writes anything there.

</li>

</ol>

A typical Windows computer shows four partitions: the EFI system partition, a small reserved partition, drive C: and the recovery partition. Windows Disk Management shows only three of them; it hides the small reserved partition.
:::
:::

:::aufgabe Exercise 28 ★★ Troubleshooting the start
<span class="anker" id="aufg-28"></span>

What has probably happened in each case, and what do you do? (a) After “Shut down” and switching on, Windows starts immediately, although you pressed the key for the boot menu. (b) In the boot menu, the stick appears twice, once with “UEFI:” in front; you chose the other entry, and only a black screen appears. (c) The firmware reports “Secure Boot Violation”. (d) After writing, Windows asks whether it should format the stick. (e) After trying out Ubuntu, Windows starts and demands a 48-digit key.

:::loesung
(a) After “Shut down”, Windows with Fast Startup was only at rest, and the firmware ran through so quickly that the key no longer had any effect. Remedy: Choose “Restart” in Windows and press the key several times immediately, or choose “Use a device” via Advanced startup.

(b) The other entry starts the stick in the old BIOS mode, which many new computers no longer support at all or which is blocked when Secure Boot is switched on. Remedy: Switch off the computer, start again via the boot menu and choose the entry with “UEFI:”.

(c) The firmware did not accept a boot program on the stick: its seal does not match the firmware's verification keys. Possible causes are a damaged stick or one of unknown origin, or a certificate that the firmware does not know (background in subsection [6.4](wie-ein-pc-startet.html#stufe-6-4)). Remedy: Check the checksum of the image once more and rewrite the stick, then install all updates of Windows and the firmware. You do not switch off Secure Boot for Ubuntu.

(d) Windows cannot read the partitions from the Linux image and therefore considers the stick unformatted. Remedy: “Cancel”. If you format it, you empty the stick again and have to rewrite it.

(e) Windows demands the recovery key because, from its point of view, the boot chain has changed, for example because a setting in the firmware was changed after all. Remedy: Enter the backed-up key from [https://aka.ms/myrecoverykey](https://aka.ms/myrecoverykey); Windows then starts and continues to run normally. Afterward, check whether something has been changed in the firmware, such as Secure Boot or the boot order, and set it back; for this, the key may be needed once more.
:::
:::

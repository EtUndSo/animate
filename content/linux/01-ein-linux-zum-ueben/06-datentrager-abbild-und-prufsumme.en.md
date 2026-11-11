---
title: Storage device, image and checksum
pfad: Computer Science / Linux and the Command Line / A Linux to Practice On: WSL, Virtual Machine, Live USB Stick
adresse: informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick
knoten: Chapter 1: A Linux to Practice On: WSL, Virtual Machine, Live USB Stick
order: 6060600
summary: For a virtual machine and for the live USB stick, you download a whole operating system as a single file.
tags: storage device, sectors, partition, partition table, file system, image, ISO image, checksum
lang: en
---

<span class="anker" id="stufe-5"></span>

:::zweck
For a virtual machine and for the live USB stick, you download a whole operating system as a single file. This section explains what such a file contains and how to use a checksum to determine that it was not changed on the way. For this, you first need three basic concepts about storage devices.
:::

:::::vorwissen What you need for this: the storage device

<span class="anker" id="stufe-5-1"></span>

Main memory forgets everything as soon as the power is gone. Whatever is to remain must be on a device that holds it permanently.

:::definition Definition 5.1 (Storage device)
<span class="anker" id="satz-5-1"></span>

A __storage device__ is a device that stores data permanently without power, such as an SSD, a hard disk, a USB stick or a memory card. To the operating system, it is a long row of numbered blocks of equal size, usually 512 bytes each; these blocks are called __sectors__.
:::

::::beispiel How large is an 8 GB stick?
A USB stick labeled “8 GB” has, for example, 15 633 408 sectors of 512 bytes, that is, 8 004 304 896 bytes. Manufacturers count in powers of ten: $1\,\mathrm{GB}=10^9$ bytes, so the stick has 8.00 GB. Windows and many Linux programs, on the other hand, calculate in powers of two, $1\,\mathrm{GiB}=2^{30}\,\mathrm{bytes}=1\,073\,741\,824$ bytes. In this unit, the stick has

$$\frac{8\,004\,304\,896\ \mathrm{bytes}}{1\,073\,741\,824\ \mathrm{bytes/GiB}}=7.45\ \mathrm{GiB}.$$

Windows writes “7.45 GB” for this, although it means GiB. An SSD labeled “512 GB” usually has slightly more than $512\cdot10^9$ bytes, namely 512 110 190 592 bytes, and therefore appears as 476.9 GB. Numbers like these let you reliably recognize a storage device in a list.
::::

⁠**In short:** A storage device is a long row of numbered blocks that keep their contents even without power.

:::::

:::::vorwissen What you need for this: the partition

<span class="anker" id="stufe-5-2"></span>

An SSD often has to serve several purposes: an area for the operating system, one for the boot files and one for recovery in an emergency. That is why it is divided into sections.

:::definition Definition 5.2 (Partition)
<span class="anker" id="satz-5-2"></span>

A __partition__ is a contiguous section of a storage device that the operating system treats like a storage device of its own. Where each partition begins and ends is recorded in the __partition table__ at the beginning of the storage device. Today, a table following the GPT scheme is common; older storage devices and many USB sticks use the older MBR scheme.
:::

::::beispiel The SSD of a Windows laptop
The SSD of a typical Windows computer holds four partitions: at the front, a small EFI system partition of a few hundred MB that contains the boot files; a tiny partition that Windows reserves for its own purposes; the large partition that Windows shows as drive C:; and at the end, a recovery partition with tools for emergencies. Only drive C: has a letter; the other three do not appear in File Explorer.
::::

⁠**In short:** A partition is a section of a storage device; the partition table at the beginning says where each one lies.

:::::

:::::vorwissen What you need for this: the file system

<span class="anker" id="stufe-5-3"></span>

At first, a partition is merely a row of sectors. That it contains files with names and folders is an order that only the operating system brings into it.

:::definition Definition 5.3 (File system)
<span class="anker" id="satz-5-3"></span>

A __file system__ is the order according to which an operating system stores files and folders in the sectors of a partition. It determines where the names are, in which sectors the contents of each file lie and where there is still free space; many file systems also record who may read a file.
:::

::::beispiel [Examples] Five file systems
Windows uses the NTFS file system for drive C:. USB sticks and memory cards are usually set up with FAT32 or exFAT, because almost every device can read them. Linux usually uses ext4 for its own partitions; the virtual hard disk of WSL 2 also contains an ext4. The boot files in the EFI system partition are in a FAT file system. Finally, CDs and DVDs use the ISO 9660 file system. When Windows “formats” a stick, it creates a new, empty file system on it; afterward, the old files can no longer be found.
::::

⁠**In short:** The file system turns the sectors of a partition into files and folders.

:::::

### The image

<span class="anker" id="stufe-5-4"></span>

An operating system consists of thousands of files, plus a partition table and the boot files without which a computer cannot start it. To distribute it, all of this is packed into a single file, and in such a way that this file can be turned back into a bootable storage device.

:::definition Definition 5.4 (Image, ISO image)
<span class="anker" id="satz-5-4"></span>

An __image__ is a file that contains the contents of an entire storage device sector by sector, with partition table, file systems and boot files. An __ISO image__ is an image in the format of a CD or DVD; it has the extension `.iso`.
:::

The ISO images of Ubuntu and many other distributions are built so that the same file works as a DVD and as a USB stick, on older and on newer computers.

::::beispiel The image of Ubuntu 26.04.1
Ubuntu provides the system for desktop computers as `ubuntu-26.04.1-desktop-amd64.iso`. The file is 6 482 409 472 bytes in size, that is, 6.48 GB or 6.04 GiB. It fits on an 8 GB stick, with a good 1.5 GB to spare; a 4 GB stick would be too small. The name also reveals which processors the image is built for: `amd64` stands for the 64-bit processors of PCs, from Intel as well as from AMD.
::::

The hard disk of a virtual machine from subsection [3.1](virtuelle-maschinen-der-rechner-im-rechner.html#stufe-3-1) and the WSL 2 file `ext4.vhdx` are also images in a broader sense: files that represent an entire storage device for their guest. However, they do not contain it sector by sector, but in a format of their own that stores only the areas that have been written to.

⁠**In short:** An image is an entire storage device in a single file.

:::warnung An image is written, not copied
If you simply copy the ISO file onto a USB stick, you then have a stick with a file on it, and no computer starts from it. For the stick itself to become the storage device from the image, a dedicated program must write the contents of the file onto the stick sector by sector. In the process, everything that was on the stick before is lost.
:::

:::hintergrund How one file can be both a DVD and a USB stick
A DVD and a USB stick are read in different ways at startup. For DVDs, there is a standard of its own that provides for a reference to the boot files at the beginning of the ISO 9660 file system. A USB stick, on the other hand, is read like a hard disk: the computer's startup software looks for a partition table at the front and, in it, a partition with boot files. The Ubuntu images contain both at the same time. In the first sectors, which the DVD format leaves free, a partition table is additionally entered, and one of its partitions points to a small area with the boot files. Depending on whether the file is read as a DVD or as a disk, the computer finds one structure or the other. Such images are called *hybrid*.
:::

### The checksum

<span class="anker" id="stufe-5-5"></span>

A 6.5 GB download can be damaged on the way, and a single wrong bit can make a boot program unusable. Worse would be an image into which someone has deliberately built malware. So you want to check whether the downloaded file is exactly the one that the publisher released, without having to compare the 6.5 GB byte by byte with the original.

**A fingerprint of the file.** The idea: from the contents of the file, a fixed method calculates a short number, a kind of fingerprint. The publisher publishes the fingerprint of its file, you calculate that of your copy, and if the two match, the copy is unchanged. Figure [9](#abb-9) shows that even the smallest change results in a completely different fingerprint.

:::abbildung linux/k1pruefsumme 9
The checksum as a fingerprint. Two files that differ in a single letter result in two completely different values with the SHA-256 method (shortened here). Conversely, an equal value means: equal contents.
:::

:::definition Definition 5.5 (Checksum, SHA-256)
<span class="anker" id="satz-5-5"></span>

A __checksum__ is a short value that a fixed method calculates from the contents of a file. The images of Linux distributions use the __SHA-256__ method, which is specified by the U.S. standard FIPS 180-4. From every file, no matter how large, it yields a value of 256 bits, written as 64 hexadecimal digits `0`–`9` and `a`–`f`. The same contents always result in the same value. SHA-256 is built so that every change, even that of a single bit, results in a completely different value and that, as far as is known today, nobody can deliberately produce a second file with the same value.
:::

::::beispiel One letter different
The file `gruss.txt` contains the line `Hallo Linux`, the file `gruss2.txt` the line `Hallo Linuy`. On Linux, the command `sha256sum` calculates the checksum of a file:

```console Linux
$ sha256sum gruss.txt
99fe677717755bcd765dabb7092a68d674ecb79d8e1885a042ca5c90157c1098  gruss.txt
$ sha256sum gruss2.txt
bcfef736955e8b5f649a111842d4a17f4d9b8c9bf1ed32ea6ef7c179d102bdd5  gruss2.txt
```

Of the 64 positions, only 5 match by chance; for two completely unrelated values, on average $64/16=4$ would be equal. A single letter of difference has thus changed the value as thoroughly as if it came from a completely different file.
::::

⁠**In short:** The checksum is the fingerprint of a file: same contents, same value; any change, a different value.

:::hintergrund Why a cryptographic hash function is used for this
A simple checksum, such as the sum of all bytes, would often detect random transmission errors. But it has two weaknesses. If you swap two bytes, the sum stays the same. And anyone who changes something deliberately can adjust a byte elsewhere so that the sum is correct again. SHA-256 is one of the *cryptographic hash functions*, which are built to withstand both. Every bit of the result depends in an intricate way on every bit of the input, so that a small change flips half of all result bits on average. And no way is known to find a matching file for a given value that would be significantly faster than blind trial and error. With $2^{256}\approx1.16\cdot10^{77}$ possible values, blind trial and error is hopeless. The Cybersecurity series covers how such functions are built.
:::

### Checking: first by eye, then with the tool

<span class="anker" id="stufe-5-6"></span>

The publisher publishes the checksums of its images in a small text file next to the images. For Ubuntu, it is called `SHA256SUMS`. For Ubuntu 26.04, it looks like this:

```text SHA256SUMS
487f87faaf547ea30e0aba4d5b53346292571256b25333a978db1692bcee9dd2 *ubuntu-26.04-desktop-amd64.iso
dec49008a71f6098d0bcfc822021f4d042d5f2db279e4d75bdd981304f1ca5d9 *ubuntu-26.04-live-server-amd64.iso
96c7f5fb28a7fe28245331f9bfbe4375f18dd29a4850116ad3c4f60f6700c55c *ubuntu-26.04-wsl-amd64.wsl
601e30fbf5d97759367c632e2c33630665039b7e2158fd068403da3ccf1bda1f *ubuntu-26.04.1-desktop-amd64.iso
cc8a95cde20f6ced61a322420de00f10cc3c90ced545daa46cb9c1a117f1d927 *ubuntu-26.04.1-live-server-amd64.iso
48d56724b5c8e60f24893e83e73bbb58c60b3ca22fba3da977075420acd54104 *ubuntu-26.04.1-wsl-amd64.wsl
```

Each line contains a checksum, a space, an asterisk and the file name. The asterisk only says that the file is to be read as a sequence of bytes. The value for the image from subsection [5.4](#stufe-5-4) is in the fourth line.

**By eye.** The simplest way: you calculate the checksum of your copy and compare it character by character with the line in `SHA256SUMS`. That is tedious with 64 characters, and it tempts you to compare only the beginning and the end. Against a random transmission error, that would be enough. Against a deliberate forgery, it is not: if you compare only the first and last four characters, you check 8 hexadecimal digits, and an attacker finds a forgery that matches in exactly these 8 digits by trial and error after about $16^8=2^{32}\approx4.3$ billion attempts. Each attempt succeeds only with probability $1/16^8$, which is why exactly that many attempts are needed on average. A computer that manages one billion attempts per second needs about 4 seconds on average for this. So either you compare all 64 characters, or you let the tool do the comparison.

**With the tool on Linux.** The command `sha256sum -c` reads a file like `SHA256SUMS`, calculates the checksum for each file listed in it and does the comparison itself. The following example shows this with the small file `gruss.txt`.

::::beispiel Checking a checksum list of your own
The file `PRUEFSUMMEN` (German for “checksums”) contains a single line in the same format as `SHA256SUMS`. Then `gruss.txt` is changed to `Hallo Linuy` and checked again:

```console Linux
$ cat PRUEFSUMMEN
99fe677717755bcd765dabb7092a68d674ecb79d8e1885a042ca5c90157c1098  gruss.txt
$ sha256sum -c PRUEFSUMMEN
gruss.txt: OK
$ sha256sum -c PRUEFSUMMEN
gruss.txt: FAILED
sha256sum: WARNING: 1 computed checksum did NOT match
```

`OK` means: same checksum, unchanged contents. `FAILED` means: the file is no longer the one whose checksum is in the list.
::::

For the Ubuntu image, you put `SHA256SUMS` in the same folder as the ISO file and type `sha256sum -c SHA256SUMS --ignore-missing`. The option `--ignore-missing` skips the files in the list that you have not downloaded. If `ubuntu-26.04.1-desktop-amd64.iso: OK` then appears, the image is unchanged. If the tool instead reports `no file was verified`, the ISO file is not in the same folder as the list.

**With the tool on Windows.** In PowerShell, `Get-FileHash` calculates the checksum, using SHA-256 by default. The addition `| Format-List` writes the result as a list, one line below the other, so that the long value is not cut off.

::::beispiel The same file on Windows
The file `gruss.txt` is now in the “Downloads” folder of the Windows user `student`:

```console Windows (PowerShell)
PS> Get-FileHash .\gruss.txt | Format-List

Algorithm : SHA256
Hash      : 99FE677717755BCD765DABB7092A68D674ECB79D8E1885A042CA5C90157C1098
Path      : C:\Users\student\Downloads\gruss.txt

PS> (Get-FileHash .\gruss.txt).Hash -eq "99fe677717755bcd765dabb7092a68d674ecb79d8e1885a042ca5c90157c1098"
True
```

The value is the same as on Linux, only in uppercase letters. The second line has PowerShell do the comparison: between the quotation marks, you paste the value from `SHA256SUMS`. The comparison `-eq` ignores the difference between uppercase and lowercase and answers `True` if the values are equal and `False` otherwise.
::::

⁠**In short:** Compare checksums completely, preferably with `sha256sum -c` or with `Get-FileHash` and `-eq`.

### What the checksum proves and what it does not

<span class="anker" id="stufe-5-7"></span>

If the checksum matches, the file is exactly the one whose value is in `SHA256SUMS`. This proves that nothing was damaged during the download. But it does not prove that the file comes from the publisher.

::::beispiel A swapped mirror server
Many people do not download large files directly from the publisher, but from a mirror server, for example at a university that provides copies. Suppose an attacker has taken over such a server and swapped the image there for one with built-in malware. Then the attacker also swaps the file `SHA256SUMS` next to it and enters the checksum of the forged image. Anyone who downloads both from this server gets a reassuring `OK` when checking: after all, the file matches the list. Except that the file and the list are both forged.
::::

So the checksum proves the __integrity__ of the file with respect to the list, not its origin. That the list itself is genuine is only established by a __digital signature__ from the publisher: a kind of forgery-proof seal that only the owner of a secret key can apply and that anyone can check with a matching public verification key. For Ubuntu, the signature of the list is in the file `SHA256SUMS.gpg`; the Cybersecurity series explains how a signature works mathematically and how to verify it. For this chapter, it is enough to do the following: download the image and `SHA256SUMS` from the publisher's official site, for Ubuntu from [https://ubuntu.com/download/desktop](https://ubuntu.com/download/desktop) or [https://releases.ubuntu.com](https://releases.ubuntu.com), and always check the checksum.

⁠**In short:** A matching checksum proves that the file is unchanged, but not that it is genuine.

### Exercises for Section [5](#stufe-5)

<span class="anker" id="stufe-5-8"></span>

:::aufgabe Exercise 15 ★ A checksum on both sides
<span class="anker" id="aufg-15"></span>

On Windows, use Notepad to create a text file with a line of your choice. Calculate its checksum in PowerShell with `Get-FileHash`. If you have set up WSL 2, also calculate it in Linux with `sha256sum`; there, the path begins with `/mnt/c`. Do the values match? Then change a single character, save and calculate the checksum again.

:::loesung
Both tools read the same bytes of the file and apply the same method, SHA-256, to them; the values therefore match, on Windows in uppercase letters, on Linux in lowercase letters. If the file is, for example, at `C:\Users\<Name>\Documents\notiz.txt`, the command in Linux is `sha256sum /mnt/c/Users/<Name>/Documents/notiz.txt`. After changing a single character, the value is completely different, as in the example “One letter different”.

If the values did not match before the change, the two tools did not read the same file, for example because Notepad had not yet saved the file or because two files with similar names exist. Checksums compare bytes, not the visible text: An invisible difference, such as an additional space at the end of a line, results in a different value.
:::
:::

:::aufgabe Exercise 16 ★★ How much does part of the value reveal?
<span class="anker" id="aufg-16"></span>

<ol class="al">

<li>

In the two checksums from the example “One letter different”, count the positions at which both values have the same digit. How many equal positions do you expect on average for two random values, and why?

</li>

<li>

Someone compares only the first six characters. Roughly how many attempts does an attacker need to find a forgery whose checksum begins with the same six characters? How many would it be if all 64 characters were compared?

</li>

</ol>

:::loesung
(a) The two values

```text
99fe677717755bcd765dabb7092a68d674ecb79d8e1885a042ca5c90157c1098
bcfef736955e8b5f649a111842d4a17f4d9b8c9bf1ed32ea6ef7c179d102bdd5
```

match at 5 of the 64 positions. If two values are unrelated, each position is independently one of the 16 hexadecimal digits, and the probability that they match at a given position is $1/16$. On average, you therefore expect $64\cdot\frac1{16}=4$ equal positions. A count of 5 is a perfectly ordinary random result; the two checksums behave like two unrelated values, although the files differ in only one letter.

(b) Six hexadecimal digits can take $16^6=2^{24}=16\,777\,216$ different values. An attacker who keeps varying a forgery at an unimportant place therefore hits a checksum with the same six initial characters after about 17 million attempts, which for a computer is a matter of fractions of a second to seconds. For all 64 characters, the attacker would need about $16^{64}=2^{256}\approx1.16\cdot10^{77}$ attempts; no conceivable computer can manage that. A partial comparison therefore protects against random errors, but not against intent.
:::
:::

:::aufgabe Exercise 17 ★ Does the image fit on the stick?
<span class="anker" id="aufg-17"></span>

An image is 6 482 409 472 bytes in size. Windows displays the sizes 3.72 GB, 7.45 GB and 14.9 GB for three sticks. Which sticks does the image fit on? To find out, convert the size of the image into the same unit that Windows uses.

:::loesung
In the unit that Windows uses, the image has

$$\frac{6\,482\,409\,472\ \mathrm{bytes}}{1\,073\,741\,824\ \mathrm{bytes/GiB}}=6.04\ \mathrm{GiB}.$$

So it does not fit on the stick with 3.72 (a stick labeled 4 GB), but it does fit on the sticks with 7.45 (8 GB) and 14.9 (16 GB). If you instead compare 6.48, the size the publisher states for the image, with 7.45 from the Windows display, you arrive at the same result here, but you are comparing two different units; in close cases, this leads you astray.
:::
:::

:::aufgabe Exercise 18 ★★ What helps against the swapped server?
<span class="anker" id="aufg-18"></span>

In the example with the mirror server, the image and `SHA256SUMS` have the same flaw. Which of the following measures would have uncovered the forgery, and which would not? (a) `sha256sum -c` instead of comparison by eye, (b) `SHA256SUMS` from [https://releases.ubuntu.com](https://releases.ubuntu.com), the image from the mirror server, (c) downloading the image and the list twice, (d) checking the signature `SHA256SUMS.gpg`.

:::loesung
(a) Does not uncover the forgery. `sha256sum -c` only compares more precisely than the eye; since the image and the list match each other, it reports `OK`.

(b) Uncovers it. The genuine list from [https://releases.ubuntu.com](https://releases.ubuntu.com) contains the checksum of the genuine image; the forged image has a different one, and the comparison reports `FAILED` or `False`. The prerequisite is that the official server itself has not been tampered with.

(c) Does not uncover it. The mirror server delivers the same forged file and the same forged list both times.

(d) Uncovers it. Only someone who has Ubuntu's secret key can produce a valid signature over `SHA256SUMS`; the attacker does not have it. A forged list is therefore noticed when the signature is checked, provided that you check with Ubuntu's genuine verification key.
:::
:::

---
title: How a PC starts
pfad: Computer Science / Linux and the Command Line / A Linux to Practice On: WSL, Virtual Machine, Live USB Stick
adresse: informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick
knoten: Chapter 1: A Linux to Practice On: WSL, Virtual Machine, Live USB Stick
order: 6060700
summary: If you want to start Linux from a USB stick, or from an image in a virtual machine, you need to know what happens between pressing the power button and the running kernel.
tags: firmware, UEFI, EFI system partition, boot order, boot menu, boot loader, GRUB, Secure Boot
lang: en
---

<span class="anker" id="stufe-6"></span>

:::zweck
If you want to start Linux from a USB stick, or from an image in a virtual machine, you need to know what happens between pressing the power button and the running kernel. This section follows this chain link by link, as far as you need it to start safely from the stick: What starts first, how do you choose the storage device, what loads the kernel, how does the computer check whether it can trust the boot program, and why does the encryption of Windows depend on this chain?
:::

### The firmware

<span class="anker" id="stufe-6-1"></span>

After switching on, main memory is empty, and no operating system is running yet. Nevertheless, the computer finds Windows on the SSD after a few seconds. So some program must already be there beforehand and know where to look.

:::definition Definition 6.1 (Firmware, UEFI)
<span class="anker" id="satz-6-1"></span>

The __firmware__ is a program that is stored permanently in a memory chip on the main circuit board (the motherboard) and runs first when the computer is switched on. It checks and starts the hardware and then loads a boot program from a storage device. Today's PCs use firmware following the __UEFI__ standard (Unified Extensible Firmware Interface); its predecessor was called BIOS, and many people still call the firmware “BIOS” today.
:::

A UEFI firmware reads its boot programs from a small, dedicated partition with a FAT file system, the __EFI system partition__; it is the first of the four partitions from the example in subsection [5.2](datentrager-abbild-und-prufsumme.html#stufe-5-2). In its own memory, the firmware keeps a list of boot entries, each with the storage device and the path of a boot file. For Windows, an entry named “Windows Boot Manager” points to the file `\EFI\Microsoft\Boot\bootmgfw.efi` in the EFI system partition of the SSD.

::::beispiel Which firmware does my computer have?
PowerShell knows a value that Windows takes over from the firmware at startup:

```console Windows (PowerShell)
PS> $env:firmware_type
UEFI
```

On older computers, it says `Legacy` here; then the computer starts in the old BIOS mode. Computers with Windows 11 practically always start with UEFI.
::::

⁠**In short:** The firmware runs first after switching on and loads a boot program from the EFI system partition.

:::hintergrund Why an unknown USB stick starts without an entry
A USB stick that is plugged into a computer for the first time does not yet have a boot entry in that computer's firmware. So that every stick can nevertheless start on every computer, the UEFI standard specifies a fixed path for removable storage devices: if the firmware finds an EFI system partition on such a storage device, it looks there for the file `\EFI\BOOT\BOOTX64.EFI` (for 64-bit PCs) and starts it. A bootable Linux stick contains exactly this file. That is why you do not need to set anything up in the firmware to start from the stick; you only need to select it.
:::

### Boot order and boot menu

<span class="anker" id="stufe-6-2"></span>

If an SSD with Windows and a USB stick with Linux are both in the computer, the firmware has to decide what to start from. Normally, that should be Windows, and only as an exception the stick. In this context, starting a computer is usually called *booting*.

:::definition Definition 6.2 (Boot order, boot menu)
<span class="anker" id="satz-6-2"></span>

The __boot order__ is the list of boot entries in the order in which the firmware tries them at power-on. The __boot menu__ is a selection that the firmware displays when you press a key at power-on; in it, you choose an entry once, without changing the boot order.
:::

::::beispiel The key for the boot menu
Which key opens the boot menu depends on the manufacturer; Table [3](#tab-3) lists the most common ones. You press it several times right after switching on, before the Windows logo appears.

<span class="anker" id="tab-3"></span>

**Table 3:** Keys for the boot menu for common manufacturers. Individual models may differ; the device's manual is authoritative.

| Manufacturer | Key for the boot menu |
|---|---|
| Dell | F12 |
| HP | Esc, then F9 |
| Lenovo | F12, on many IdeaPads Fn+F12, or the small Novo button |
| ASUS (laptop) | hold down Esc while switching on |
| MSI | F11 |
| Acer | F12, must first be enabled in the firmware on some devices |

If no key helps, there is a way via Windows: Settings $\to$ System $\to$ Recovery $\to$ Advanced startup $\to$ “Restart now”. In the blue menu that appears afterward, many computers offer the item “Use a device”, with which you start directly from the stick. Otherwise, “Troubleshoot” $\to$ “Advanced options” $\to$ “UEFI Firmware Settings” leads to the settings of the firmware.
::::

⁠**In short:** For a one-time start from the stick, you use the boot menu and leave the boot order as it is.

### The boot loader

<span class="anker" id="stufe-6-3"></span>

The firmware knows its way around partitions and the FAT file system, but not around a Linux kernel and its settings. That is why another program stands between the firmware and the kernel.

:::definition Definition 6.3 (Boot loader)
<span class="anker" id="satz-6-3"></span>

A __boot loader__ is the boot program that the firmware loads and that in turn loads the kernel of the operating system into main memory and starts it. In doing so, it can display a menu in which you choose between several systems or startup variants.
:::

Linux distributions usually use the __GRUB__ boot loader.

::::beispiel [Examples] Two boot loaders
Windows uses the Windows Boot Manager, the file from subsection [6.1](#stufe-6-1), and Ubuntu uses the GRUB boot loader. When you start an Ubuntu stick, GRUB displays a short menu after a few seconds; the first entry starts Ubuntu and is preselected. Once the kernel is loaded, it takes control, and the boot loader has done its job.
::::

⁠**In short:** The firmware loads the boot loader, and the boot loader loads the kernel.

### Secure Boot

<span class="anker" id="stufe-6-4"></span>

The boot program runs before the operating system and any virus scanner are even there, and it determines which kernel is loaded. A secretly replaced boot loader would therefore have the whole computer in its hands. A check in the firmware protects against this.

**A seal on the boot program.** The check is based on the digital signature from subsection [5.7](datentrager-abbild-und-prufsumme.html#stufe-5-7), the forgery-proof seal that only the owner of a secret key can apply and that anyone can check with the matching verification key. If a signed file is afterward changed by even a single bit, the seal no longer matches.

:::definition Definition 6.4 (Secure Boot)
<span class="anker" id="satz-6-4"></span>

__Secure Boot__ is a function of the UEFI firmware that runs a boot program only if it carries a valid digital signature whose verification key is stored in the firmware as trusted and has not been revoked. Secure Boot is a check of authenticity, not encryption: it hides nothing, it only prevents modified or unknown boot programs from starting.
:::

Figure [10](#abb-10) shows how an Ubuntu stick starts with Secure Boot switched on. In almost all PCs, verification keys from Microsoft are stored at the factory. That is why Ubuntu comes with a small program called `shim` as its first boot program, which Microsoft has signed. `shim` contains Canonical's verification key, with which `shim` checks the GRUB boot loader, and GRUB checks the kernel in the same way.

:::abbildung linux/k1bootkette 10
The boot chain of an Ubuntu stick with Secure Boot. Each link checks the seal of the next one before handing control over to it. The firmware trusts Microsoft, Microsoft has signed `shim`, and `shim` carries Canonical's key onward.
:::

::::beispiel Which systems start with Secure Boot and which do not
An Ubuntu stick starts with Secure Boot switched on, because every link in its chain is suitably signed; you do not need to change anything in the firmware. Kali Linux, on the other hand, comes with a kernel without a signature; to start it from the stick, you would have to switch off Secure Boot in the firmware. For this chapter, Secure Boot always stays switched on.
::::

⁠**In short:** Secure Boot starts only boot programs with a valid seal; it checks authenticity and encrypts nothing.

:::hintergrund When a stick does not start because of a “Security Violation”
The verification keys in the firmware are contained in certificates with an expiration date. The certificate with which Microsoft has signed the boot programs of other vendors, such as `shim`, since 2011 expired on 27 June 2026; its successor dates from 2023. The expiration alone does not prevent any start, because the firmware checks the seal against the stored certificate and not against the date. Problems arise in two places. A very new computer whose firmware knows only the 2023 certificate does not start a boot program that is signed only with the old one. Conversely, an older computer whose firmware was never updated does not start a boot program that is signed only with the new one. According to Canonical, the installation media of Ubuntu 26.04 need the 2011 certificate in the firmware. If a computer reports a security violation when starting from the stick, you first install all updates for the firmware, from Windows and from the manufacturer, and try again, instead of switching off Secure Boot.
:::

### Windows device encryption

<span class="anker" id="stufe-6-5"></span>

On many Windows computers, the SSD is encrypted, often without the owners knowing it. In normal operation, you notice nothing of this. But if you change something in the boot chain, Windows may demand a long key at the next startup, and anyone who does not have it can no longer get to their data.

:::definition Definition 6.5 (BitLocker, recovery key)
<span class="anker" id="satz-6-5"></span>

__BitLocker__ is the drive encryption of Windows; in Windows Home, it is called *device encryption*. It encrypts drive C:, and Windows decrypts it by itself at startup if the boot chain is unchanged. If the boot chain has been changed, Windows demands the __recovery key__, a 48-digit number that was generated when the encryption was switched on.
:::

Windows 11 switches on device encryption by itself on suitable computers as soon as you sign in with a Microsoft account, and it stores the recovery key in this account. Since version 24H2, this applies to considerably more computers than before. You can see whether your drive is encrypted under Settings $\to$ Privacy & security $\to$ Device encryption; if this item is missing, the function is not available on your computer. In the Pro and Enterprise editions, you can also find the encryption in Control Panel under the name “BitLocker Drive Encryption”.

::::beispiel What triggers the prompt and what does not
Microsoft names, among others, these triggers for the recovery key prompt: changes to the Windows Boot Manager, a firmware update, changes to settings that are included in the check of the boot chain, which includes Secure Boot, and, on older computers with a security chip of version 1.2, a changed boot order. A one-time start from the stick via the boot menu, with Secure Boot switched on and without any change to the firmware, is not on this list; afterward, Windows normally starts as always. Even so, you back up the key beforehand, because not all computers behave the same way.
::::

:::warnung Back up the recovery key before you do anything to the boot chain
Before you start from the stick or change any setting in the firmware, check whether your drive is encrypted. If it is, back up the recovery key so that you can read it without this computer:

<ul>

<li>

On another device, such as your phone, sign in at [https://aka.ms/myrecoverykey](https://aka.ms/myrecoverykey) with your Microsoft account and check that a key for your computer is listed there. Write it down on paper or print it out.

</li>

<li>

If the computer is a device of your university or your employer, the key is held by its IT department. Do not start such a device from a stick without their permission.

</li>

</ul>

If you have to change a setting in the firmware, Microsoft advises temporarily suspending the encryption beforehand; after the next restart, it switches itself back on. In the Pro and Enterprise editions, you do this in Control Panel under “BitLocker Drive Encryption” with “Suspend protection”. Windows Home has no switch for this; there, the backed-up key is the safeguard.
:::

⁠**In short:** Before you do anything to the boot chain, you back up the 48-digit recovery key.

:::hintergrund Why the encryption depends on the boot chain
The key with which Windows decrypts the drive is released only by a security chip on the motherboard, the TPM (Trusted Platform Module). During startup, the firmware writes a kind of fingerprint of each loaded boot program and of important settings, such as whether Secure Boot is switched on, into this chip. The chip releases the key only if these fingerprints are exactly the same as when the encryption was switched on. That way, someone who starts the computer with a boot program of their own cannot grab the key; the flip side is that even a harmless change locks the key. The Cybersecurity series explains how the TPM measures the boot chain.
:::

### Exercises for Section [6](#stufe-6)

<span class="anker" id="stufe-6-6"></span>

:::aufgabe Exercise 19 ★ The firmware and encryption of your computer
<span class="anker" id="aufg-19"></span>

Find out, without changing anything: (a) Does your computer start with UEFI? Use `$env:firmware_type` in PowerShell. (b) Is Secure Boot switched on? The program “System Information” (type `msinfo32` in the Start menu) shows it in the line “Secure Boot State”. (c) Is your drive encrypted, and can you find the recovery key at [https://aka.ms/myrecoverykey](https://aka.ms/myrecoverykey)? (d) Which key opens the boot menu of your computer? Look it up in the manufacturer's manual instead of trying it out.

:::loesung
The values depend on your computer. On this chapter's test computer, the answer to (a) is:

```console Windows (PowerShell)
PS> $env:firmware_type
UEFI
```

(b) System Information shows “Secure Boot State: On” if Secure Boot is switched on, and “Off” if not; “Unsupported” appears on computers that start in the old BIOS mode. (c) Under Settings $\to$ Privacy & security $\to$ Device encryption or BitLocker, you can see whether the drive is encrypted; at [https://aka.ms/myrecoverykey](https://aka.ms/myrecoverykey), there is a 48-digit key for every encrypted device that is linked to your Microsoft account. If you find none there although encryption is switched on, clear this up before you change anything at all in the boot process. (d) The key is given in the manual or on the manufacturer's support page, usually under “Boot Menu” or “Startup Menu”; Table [3](#tab-3) lists the most common ones.
:::
:::

:::aufgabe Exercise 20 ★★ Where does the chain break?
<span class="anker" id="aufg-20"></span>

A computer has Secure Boot switched on. At which link of the chain from Figure [10](#abb-10) does booting stop, or does the system start? (a) Someone has changed a byte in GRUB on the stick. (b) The stick contains a kernel that nobody has signed. (c) An Ubuntu stick is plugged into a computer whose firmware does not contain Microsoft's verification key for third-party boot programs. (d) An Ubuntu stick is started via the boot menu. Does (d) trigger a recovery key prompt on an encrypted Windows?

:::loesung
(a) Booting stops at the transition from `shim` to GRUB. `shim` checks GRUB's seal with Canonical's verification key; after the change, the seal no longer matches.

(b) Booting stops at the transition from GRUB to the kernel, because GRUB finds no valid seal on the kernel. This is exactly why you have to switch off Secure Boot for a kernel without a signature, such as that of Kali Linux.

(c) The very first link fails: The firmware does not know the verification key with which Microsoft signed `shim`, and does not start `shim`. Some computers come with their firmware set up like this. The remedy is a setting in the firmware that allows this key; this is a change to the boot chain, for which the recovery key must be backed up beforehand.

(d) The system starts: firmware, `shim`, GRUB and kernel are suitably signed. A recovery key prompt is normally not to be expected at the next start of Windows. The boot menu changes neither the Windows Boot Manager nor a setting of the firmware; at the next start, the boot chain of Windows is the same as before. Only on older computers with a security chip of version 1.2 can a changed boot order trigger the prompt. Nevertheless, you have backed up the key, in case a computer behaves differently.
:::
:::

---
title: Three ways to a Linux of your own
pfad: Computer Science / Linux and the Command Line / A Linux to Practice On: WSL, Virtual Machine, Live USB Stick
adresse: informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick
knoten: Chapter 1: A Linux to Practice On: WSL, Virtual Machine, Live USB Stick
order: 6060300
summary: There are three proven ways to get a Linux to practice on under Windows.
tags: terminal, prompt
lang: en
---

<span class="anker" id="stufe-2"></span>

:::zweck
There are three proven ways to get a Linux to practice on under Windows. This section sets them side by side, helps you choose with a decision tree and explains what is at the end of each way: a window into which you type commands.
:::

### The three ways at a glance

<span class="anker" id="stufe-2-1"></span>

A Linux to practice on should do two things: it should be a real Linux on which everything the series shows works, and it should not put Windows and your files at risk. Figure [3](#abb-3) shows the three ways that do both, each in its own way.

:::abbildung linux/k1wege 3
Three ways to a Linux on a Windows computer. WSL 2 runs Linux invisibly alongside Windows, a virtual machine simulates a whole computer, and from the live USB stick, the computer itself starts a Linux while Windows rests untouched on the disk.
:::

<ul>

<li>

⁠**WSL 2.** In the background, Windows starts a small, invisible computer within the computer, in which a Linux runs. You open a window and work in Linux while the familiar Windows programs keep running alongside it. This is the fastest way, and it is enough for programming, data analysis and all exercises on the command line.

</li>

<li>

⁠**Virtual machine.** A program like VirtualBox simulates a complete computer, in which you install Linux as on a real PC. This computer is separate from the real one; you can save its state and bring it back at any time. This is the way for labs in which you are allowed to break things.

</li>

<li>

⁠**Live USB stick.** You write a Linux onto a USB stick and start the computer from it. Then Linux runs directly on the real hardware, and Windows rests untouched on the internal disk. After you switch off, everything is as before. This is the first real Linux practice on your own device; however, it requires the most care, because you write to a storage device and start the computer in an unfamiliar way.

</li>

</ul>

Table [2](#tab-2) compares the three ways.

<span class="anker" id="tab-2"></span>

**Table 2:** The three ways compared.

|  | WSL 2 | virtual machine | live USB stick |
|---|---|---|---|
| runs | alongside Windows | in a window under Windows | instead of Windows |
| good for | command line, programming, data analysis | labs, trying things out with a way back | experiencing Linux on real hardware |
| needs | Windows 10 version 2004 or later, or Windows 11 | enough memory and disk space | a USB stick of 8 GB or more |
| limits | its own small network, no direct access to USB devices | slower than the real computer | without an add-on, everything is gone after switching off |
| risk for Windows | very low | very low | low if you heed the warnings |

⁠**In short:** WSL 2 is the fastest way, the virtual machine is the lab and the live USB stick is real Linux on real hardware.

### The decision tree

<span class="anker" id="stufe-2-2"></span>

Which way is right depends on what you plan to do with Linux. The decision tree in Figure [4](#abb-4) asks two questions.

:::abbildung linux/k1entscheidung 4
Which way fits? If you need Linux for programming, for data analysis or for practicing on the command line, you end up with WSL 2. Next to each way, you can see which sections of this chapter it needs; Sections 1 and 2 apply to all of them.
:::

The ways do not exclude one another. Many people work with WSL 2 day to day and keep a virtual machine ready for experiments in which something is allowed to go wrong. If you want to see a Linux on real hardware for the first time, start it once from the stick, even if you otherwise use WSL 2.

::::beispiel Three students, three ways
Lea wants to program in Python and analyze data; her laptop has Windows 11. WSL 2 is right for her: she does not have to restart anything, and her files can be reached from Windows and from Linux. Jonas wants to examine network traffic between two computers without disturbing his home network, and in doing so, he also wants to try out settings that can damage the system. He needs a virtual machine. Mira wants to know whether her laptop gets along with Linux at all, whether Wi-Fi, graphics and sound work. She starts Linux from the USB stick, because only then does it run on her real hardware.
::::

⁠**In short:** For programming and the command line, you choose WSL 2, for labs a virtual machine and for real Linux on real hardware the live USB stick.

:::hintergrund Why there is no single best way
The three ways lie on a scale between two goals that contradict each other. The closer to the real hardware a Linux runs, the more real the experience: on the live stick, Linux controls the network card, the graphics and the USB ports itself. The more software lies between Linux and the hardware, the better it is isolated and the easier it is to undo mistakes. WSL 2 sacrifices some isolation for convenience, because it shares files with Windows. Each of the three ways is a different compromise between the two goals.
:::

### The terminal

<span class="anker" id="stufe-2-3"></span>

All three ways end at the same place: at a window into which you type commands. Most of the work in this series happens there, because a typed command is exact, repeatable and can be written down.

:::definition Definition 2.1 (Terminal)
<span class="anker" id="satz-2-1"></span>

A __terminal__ is a program with a window into which you type commands as text and in which the computer's responses appear as text. When it is ready, it shows a __prompt__ at the beginning of the line.
:::

In a Linux terminal, the prompt looks something like this: `student@labor:~$`. Before the `@` is the user name, after it the computer name; the symbol `~` stands for the user's home folder. On Windows, the corresponding program is called PowerShell; its prompt reads something like `PS C:\Users\student>`. [Python, Chapter 1, Section 3.1](/wissen/en/informatik/programmieren/python/programme-und-der-python-interpreter/python-einrichten.html#stufe-3-1) shows the Windows terminal in more detail.

This chapter shortens the prompt: `$` for Linux and `PS>` for Windows. Type the few commands in this chapter exactly as they appear and then press Enter. Chapter 2 explains what exactly a command is and how it is structured.

::::beispiel Which system is running here?
The command `cat /etc/os-release` displays the contents of a file in which every distribution enters its name and its version. This is how Ubuntu 26.04.1 replies:

```console
$ cat /etc/os-release
PRETTY_NAME="Ubuntu 26.04.1 LTS"
NAME="Ubuntu"
VERSION_ID="26.04"
VERSION="26.04.1 LTS (Resolute Raccoon)"
VERSION_CODENAME=resolute
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=resolute
LOGO=ubuntu-logo
```

The line `VERSION` contains the point release and the code name from subsection [1.7](betriebssystem-kernel-und-distribution.html#stufe-1-7), and `ID_LIKE=debian` says which distribution Ubuntu builds on. This output is the same with each of the three ways, because the file belongs to the distribution.
::::

⁠**In short:** The terminal is the window in which you talk to the system in text form; at the end of each way, you open one.

### Exercises for Section [2](#stufe-2)

<span class="anker" id="stufe-2-4"></span>

:::aufgabe Exercise 5 ★ Choosing the right way
<span class="anker" id="aufg-5"></span>

Use the decision tree to choose a way, and justify it in two sentences.

<ol class="al">

<li>

Tom has a Windows 11 laptop and wants to learn Python next semester.

</li>

<li>

In an IT security course, Sara wants to try out settings that can damage a system, and afterward start cleanly again each time.

</li>

<li>

Ali is considering switching his old laptop entirely to Linux and wants to see beforehand whether Wi-Fi and graphics work.

</li>

<li>

And you? Which way do you choose, and why?

</li>

</ol>

:::loesung
(a) WSL 2. Tom needs a Linux for the command line and for programming, not for the hardware and not for a lab. With Windows 11, WSL 2 is set up in a few minutes, and he can use Windows and Linux at the same time.

(b) A virtual machine. Sara wants to try out things that can damage a system and afterward start cleanly again; that is exactly what a snapshot provides. In the process, the VM is separated from the host.

(c) The live USB stick. Only with it does Linux run directly on Ali's real hardware and have to control Wi-Fi and graphics itself. In a VM or in WSL 2, Linux would see only virtual devices and would reveal nothing about the real hardware.

(d) There is no wrong answer here, as long as the justification matches the question in the decision tree. If you read this series for programming or data analysis, take WSL 2; if you follow the Cybersecurity series, also set up a VM and start once from the stick.
:::
:::

:::aufgabe Exercise 6 ★ Reading prompts
<span class="anker" id="aufg-6"></span>

What do these two prompts reveal? `anna@werkbank:~$` and `PS C:\Users\anna\Documents>`. What do you type when the chapter shows a line `$ uname -r`?

:::loesung
`anna@werkbank:~$` is the prompt of a Linux terminal: The user is called `anna`, the computer `werkbank`, `~` shows that the terminal is currently working in the home folder of `anna`, and `$` ends the prompt. `PS C:\Users\anna\Documents>` is PowerShell on Windows; it is currently working in the folder `C:\Users\anna\Documents`.

If the chapter shows `$ uname -r`, you type only `uname -r` and press Enter. The `$` and the space after it are already part of the prompt.
:::
:::

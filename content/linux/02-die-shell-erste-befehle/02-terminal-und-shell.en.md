---
title: Terminal and shell
pfad: Computer Science / Linux and the Command Line / The Shell: First Commands
adresse: informatik/linux-und-kommandozeile/die-shell-erste-befehle
knoten: Chapter 2: The Shell: First Commands
order: 6070200
summary: In Chapter 1, the window into which you type commands was simply called the terminal.
tags: terminal emulator, shell, bash, prompt, current folder, root, session
lang: en
---

<span class="anker" id="stufe-1"></span>

:::zweck
In [Chapter 1](/wissen/en/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/ein-linux-zum-ueben.html), the window into which you type commands was simply called the terminal. More precisely, two programs with separate tasks work together in it. This section separates the two, explains what the prompt reveals and shows when a working session begins and ends.
:::

:::::vorwissen What you need for this: the terminal from Chapter 1

<span class="anker" id="stufe-1-1"></span>

[Chapter 1, Section 2.3](/wissen/en/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/drei-wege-zu-einem-eigenen-linux.html#stufe-2-3) introduced the terminal: a program with a window into which you type commands as text and in which the computer's responses appear as text. When it is ready, it shows a prompt at the start of the line, in Ubuntu something like `student@labor:~$`. The chapter abbreviates it as `$`.

Under WSL 2, you open the terminal from the Start menu, in the Windows app “Terminal” via the entry `Ubuntu-26.04`, or with the command `wsl` in PowerShell ([Chapter 1, Section 4.4](/wissen/en/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/wsl-2-linux-neben-windows.html#stufe-4-4)). In a virtual machine or in the live system, you open Ubuntu's “Terminal” app, fastest with Ctrl+Alt+T.

You also need three concepts from [Chapter 1, Section 1](/wissen/en/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/betriebssystem-kernel-und-distribution.html#stufe-1). The kernel is the only part of the system that controls the hardware directly. All other programs run in user mode, in which the processor blocks certain instructions. They get services such as “read this file” only by asking the kernel for them with a system call.

::::beispiel A first command
Open a terminal, type `uname -r` and press Enter. The computer replies with the version of its kernel; under WSL 2, it ends in `WSL2`, in a virtual machine or in the live system in `generic`.

```console
$ uname -r
6.6.87.2-microsoft-standard-WSL2
```
::::

⁠**In short:** In the terminal, you type commands as text; the prompt shows that it is ready.

:::::

### The terminal emulator

<span class="anker" id="stufe-1-2"></span>

When you type `uname -r`, something has to draw the letters into the window, and something has to understand that this is a command. These are two different tasks, and on Linux, two different programs handle them. The first one is responsible for the window.

**A device, rebuilt as a program.** Before personal computers took over, a terminal was a device of its own: a screen with a keyboard, connected by a cable to a large computer that many people shared. The device itself could not compute anything. It sent each keystroke over the cable as a character and displayed each character that came back. Today, an ordinary program imitates this device. Figure [1](#abb-1) shows where it sits.

:::abbildung linux/k2schichten 1
From keystroke to kernel. The terminal emulator passes each keystroke to the shell as a character and draws whatever comes back. The shell understands the line and has the command run; it, too, reaches the hardware only through system calls to the kernel.
:::

:::definition Definition 1.1 (Terminal emulator)
<span class="anker" id="satz-1-1"></span>

A __terminal emulator__ is a program that shows a window with lines of text, passes each keystroke as a character to another program and displays in the window each character that this program sends back. It does not understand what the characters mean.
:::

On Windows, this is usually the Windows app “Terminal” (full name: Windows Terminal), in which WSL 2 also runs; this chapter calls it Windows Terminal. Ubuntu comes with a program of its own, called “Terminal” in the menu; since Ubuntu 25.10, this is the program Ptyxis. Other Linux systems have others, such as “Konsole”. In everyday use, all of them are simply called the terminal, and the chapter does the same when it is talking about the window.

::::beispiel What the window does with a command
You type `u`. The terminal emulator sends the character `u` on, and only when it comes back from the other side does it draw it into the window. The same happens with `name -r`. The Enter key sends the character for the end of the line. Then the reply `6.6.87.2-microsoft-standard-WSL2` comes back as a sequence of characters, and the terminal emulator draws it letter by letter. It never learned that this was a command.
::::

⁠**In short:** The terminal emulator is only the window: it passes on keystrokes and draws characters without understanding them.

:::hintergrund How the window and the shell are connected
Between the terminal emulator and the program that understands the characters, there is no longer a cable but a *pseudoterminal*: a pair of devices that consist only of software and that the kernel provides. What the terminal emulator writes into one side, the program on the other side can read as if it were sitting at a real terminal of the old days, and vice versa. On Linux, the program side is called `/dev/pts/0`, `/dev/pts/1` and so on; the command `tty` shows which one your own shell is attached to. Because the kernel sits in the middle, it can handle certain key combinations itself before they reach the program. So for the program behind the window, every terminal is the same, whether it is Windows Terminal, Ubuntu's terminal or a connection over the network.
:::

### The shell

<span class="anker" id="stufe-1-3"></span>

The window does not understand commands. A second program has to read the typed line, figure out what is meant, make sure that it happens and then wait for the next line. This program is the real conversation partner at the command line.

**A loop.** You can picture this program as a server in a restaurant who takes an order, passes it on to the kitchen, brings the result to the table and asks for the next request (a picture, not a mechanism). Figure [2](#abb-2) shows the loop that this program runs through again and again.

:::abbildung linux/k2schleife 2
The shell's loop: show the prompt, read a line, find the command, run it (or have it run), wait for the end and start over.
:::

:::definition Definition 1.2 (Shell)
<span class="anker" id="satz-1-2"></span>

A __shell__ is a program that accepts commands as text, runs them or has other programs run them, and then waits for the next command. It shows the prompt as soon as it is ready for the next command.
:::

There are many shells. On Ubuntu, Debian and Fedora, the terminal opens the shell __bash__, short for “Bourne-Again Shell”. Kali Linux and macOS use the very similar zsh. Everything in this chapter applies to bash; almost everything also applies to zsh.

::::beispiel Which bash is running here?
The shell is itself a command, and like many commands, it states its version with `--version`:

```console
$ bash --version
GNU bash, version 5.3.9(1)-release (x86_64-pc-linux-gnu)
Copyright (C) 2025 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>

This is free software; you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
```

Ubuntu 26.04 ships bash version 5.3.9. `x86_64` denotes the processor type for which the program is compiled, the common 64-bit family from Intel and AMD.
::::

⁠**In short:** The shell is the program that reads your commands and has them run; on Ubuntu, it is bash.

:::hintergrund The shell is an ordinary program
The shell is not part of the kernel. It runs in user mode like a text editor and reaches files, the screen and other programs only through system calls ([Chapter 1, Section 1.4](/wissen/en/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/betriebssystem-kernel-und-distribution.html#stufe-1-4)). To start a program such as `uname`, it uses system calls to ask the kernel to create a new running program from the file that contains the program, and it waits until that program has finished; then it shows the prompt again. Because the shell is just one program among many, you can replace it without changing anything else in the system; the file `/etc/shells` lists the shells that a user on this computer may choose as their shell.

The name is a picture: just as the shell of a nut surrounds its kernel, the shell surrounds the core of the system, the kernel. The computer scientist Louis Pouzin coined the term in late 1964 or early 1965 for the operating system Multics. Ken Thompson wrote the first Unix shell in 1971; in 1979, it was followed by Stephen Bourne's shell, which is still the model today. bash appeared in 1989 as a free reimplementation for the GNU project, and its name is a pun: “Bourne-Again” sounds like “born again”, a reborn Bourne shell.
:::

:::hintergrund Why type commands at all
A graphical interface shows what is possible; you do not have to remember anything. The command line requires you to know the command. In return, it has four advantages that grow with every task.

<ul>

<li>

⁠**Precise.** A command states completely what is to happen. Instructions such as “click the gear icon at the top right” go out of date with the next version of the program; a command line usually does not.

</li>

<li>

⁠**Repeatable.** A typed command can be copied, saved and run any number of times, by other people as well.

</li>

<li>

⁠**Automatable.** If you want to rename 800 vacation photos by date and spend 15 seconds clicking for each photo, you need 12 000 seconds, that is, 3 hours and 20 minutes. A single command that renames the photos one after another does the same work in seconds, and it does not get tired.

</li>

<li>

⁠**Remotely controllable.** Text can be sent over the network with very little data. Servers in a data center often have no screen at all; they are operated exclusively through a shell.

</li>

</ul>

That is why many tools in computer science exist only for the command line.
:::

### The prompt

<span class="anker" id="stufe-1-4"></span>

The shell has to tell you when it is ready. Ubuntu uses this opportunity to tell you at the same time who you are, which computer you are working on and where you currently are.

:::abbildung linux/k2prompt 3
Ubuntu's prompt, taken apart: user, computer, current folder and the end character. Below it, the same spot for the account `root`, which may do anything: the end character is `#`.
:::

:::definition Definition 1.3 (Prompt)
<span class="anker" id="satz-1-3"></span>

The __prompt__ is the text that the shell writes at the start of a line when it is ready to read the next command. In Ubuntu, it consists of the user name, the character `@`, the name of the computer, a colon, the current folder and an end character.
:::

The shell always works in a particular folder. This folder is called the __current folder__. After you open a terminal, it is your home folder, which the prompt abbreviates as `~`; written out, it is `/home/student`. If you change the folder, the prompt changes with it. The command `cd` changes it; `cd` without anything after it takes you back to your home folder. Ubuntu colors the user and computer green and the folder blue.

::::beispiel The prompt moves along
This is what it looks like in the window when you first change to the system folder `/etc` and then back. This time, the whole prompt is shown, not just its end character:

```text
student@labor:~$ cd /etc
student@labor:/etc$ cd
student@labor:~$
```
::::

**The end character.** Every Linux system has a user account that may do anything: read anyone else's files, change system files, install programs. This account is called __root__. If the shell runs as root, the prompt ends with `#` instead of `$`, for example `root@labor:~#`. The character is a warning: a typo as root can damage the system, because nobody stops you. Ordinary work is therefore done as an ordinary user with `$`, and none of the commands in this chapter need special privileges.

⁠**In short:** The prompt shows the user, the computer and the current folder; `$` means ordinary user, `#` means root.

### The session

<span class="anker" id="stufe-1-5"></span>

You can open several terminal windows at the same time, and each one shows its own prompt. That is no coincidence: a separate shell runs in each window. What a shell remembers therefore applies only in its own window and only as long as it is running.

:::abbildung linux/k2sitzungen 4
Two windows, two shells, two sessions. If the left shell changes to `/etc`, the right one stays in its folder; if the left one ends with `exit`, the right one keeps running.
:::

:::definition Definition 1.4 (Session)
<span class="anker" id="satz-1-4"></span>

A __session__ is the time from the start of a shell in a terminal until its end. Each session has its own current folder and its own list of the commands typed so far; two sessions know nothing about each other.
:::

You can end a session with the command `exit`. The shell then ends, and the terminal usually closes its window or its tab. Conversely, if you close the window, that also ends the shell in it.

::::beispiel Two windows side by side
Open two terminal windows, in Windows Terminal for instance with a second tab. In the first one, you type `cd /etc`; the prompt there ends in `/etc$`. The second window still shows `~$`, because its shell never changed the folder. If you type `exit` in the first window, it disappears; in the second one, you keep working undisturbed.
::::

⁠**In short:** Each terminal window has its own shell and thus its own session, which ends with `exit`.

### Exercises for Section [1](#stufe-1)

<span class="anker" id="stufe-1-6"></span>

:::aufgabe Exercise 1 ★ Window or shell?
<span class="anker" id="aufg-1"></span>

Which program does the job: the terminal emulator, the shell or both? (a) Drawing the letter `u` into the window. (b) Recognizing that `uname` is a command. (c) Producing the text `student@labor:~$`. (d) Drawing it into the window. (e) Running in user mode. (f) Being replaceable by another program without any change to the kernel.

:::loesung
(a) The terminal emulator. It draws every character that comes back from the shell; so the `u` appears because the shell sent it back, but it was the window that drew it.

(b) The shell. The terminal emulator knows no commands; to it, `uname` is a sequence of five characters.

(c) The shell. The prompt is text that the shell writes as soon as it is ready; the user, the computer and the current folder are pieces of information that only the shell knows.

(d) The terminal emulator, just as with every other character in the window.

(e) Both. Neither the window nor the shell is part of the kernel; both are ordinary programs and can reach the screen and the keyboard only through the kernel.

(f) Both. You can use a different terminal program without anything changing about the commands, and you can start a different shell instead of bash without touching the kernel. That is exactly the advantage of the separation: each of the two programs can be replaced independently of the other.
:::
:::

:::aufgabe Exercise 2 ★ Reading prompts
<span class="anker" id="aufg-2"></span>

What does each of these prompts reveal? With which one would you be especially careful, and why? (a) `mira@notebook:~$` (b) `student@labor:/etc$` (c) `root@server:/var/log#` (d) `PS C:\Users\mira>`

:::loesung
(a) User `mira` on the computer `notebook`, in the home folder, as an ordinary user (`$`).

(b) User `student` on the computer `labor`, in the system folder `/etc`, as an ordinary user. Because `/etc` holds the settings of the whole system, you only look here; an ordinary user can hardly change anything there anyway.

(c) The account `root` on a computer named `server`, in the folder `/var/log`. The end character `#` shows: this shell may do anything. Special care is needed here, because every typo is carried out without the system asking for confirmation or refusing anything.

(d) This is not a Linux shell but Windows PowerShell ([Chapter 1, Section 2.3](/wissen/en/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/drei-wege-zu-einem-eigenen-linux.html#stufe-2-3)), in the folder `C:\Users\mira`. Linux commands such as `uname` do not exist there.
:::
:::

:::aufgabe Exercise 3 ★★ Two sessions
<span class="anker" id="aufg-3"></span>

Open two terminal windows or two tabs. In the first one, type `cd /etc` and compare the two prompts. Then type `exit` in the first one. Describe what you see and explain it with the concept of a session. What does the second window show when you enter `cd /etc` and then `cd` there?

:::loesung
After `cd /etc`, the first window shows `student@labor:/etc$`, and the second still shows `student@labor:~$`. After `exit`, the first window or its tab closes; the second remains unchanged and keeps working. The reason: a shell of its own runs in each window, each shell forms a session of its own with its own current folder, and the end of one session does not affect the other. In the second window, the prompt also shows `/etc` after `cd /etc` and `~` again after `cd`, just as in the session from subsection [1.4](#stufe-1-4).
:::
:::

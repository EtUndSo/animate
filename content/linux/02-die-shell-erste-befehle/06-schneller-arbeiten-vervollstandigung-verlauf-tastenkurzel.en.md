---
title: Working faster: completion, history, keyboard shortcuts
pfad: Computer Science / Linux and the Command Line / The Shell: First Commands
adresse: informatik/linux-und-kommandozeile/die-shell-erste-befehle
knoten: Chapter 2: The Shell: First Commands
order: 6070600
summary: People who work a lot on the command line still type very little.
tags: Completion, history, reverse search, Ctrl+C, Ctrl+D, keyboard shortcut
lang: en
---

<span class="anker" id="stufe-5"></span>

:::zweck
People who work a lot on the command line still type very little. The shell completes partly typed names, remembers every line, finds old commands again and knows keyboard shortcuts for interrupting, ending and editing. This section presents these aids and explains who handles the keys behind the scenes.
:::

### Completion

<span class="anker" id="stufe-5-1"></span>

Long command and file names are tedious to type, and every typo leads to `command not found` or `No such file`. Yet the shell already knows the names: it knows which commands exist and which files are in a folder.

:::abbildung linux/k2tab 19
Completion with the Tab key. If the beginning is unique, the shell completes the name at once. If several names fit, it completes the common part, and pressing the key a second time shows all the possibilities.
:::

:::definition Definition 5.1 (Completion)
<span class="anker" id="satz-5-1"></span>

__Completion__ finishes a partly typed word as soon as you press the Tab key. In the first word of a line, the shell completes command names; in the other words, mostly file names. If only one name fits, it writes it out in full; if several fit, it completes only the part they all have in common, and pressing the key a second time lists all the possibilities.
:::

::::beispiel Once unique, once ambiguous
Type `unam` and press the Tab key. There is only one command that begins like this, and the shell writes it out with a space after it:

```text
student@labor:~$ uname
```

You add `-r` and press Enter. Then you type `cat /etc/host` and press the Tab key twice. Three files begin like this, so the shell cannot decide and shows all three; below them is your partly typed line, unchanged:

```text
student@labor:~$ uname -r
6.6.87.2-microsoft-standard-WSL2
student@labor:~$ cat /etc/host
host.conf  hostname   hosts
student@labor:~$ cat /etc/host
```

An `n` makes the beginning unique. Press the Tab key once more, then Enter:

```text
student@labor:~$ cat /etc/hostname
labor
```

The shell completed the rest of the file name, and a typo in it was impossible.
::::

⁠**In short:** The Tab key completes command and file names; pressed twice, it shows all the possibilities.

### The history

<span class="anker" id="stufe-5-2"></span>

You type many commands several times, often with small changes. Instead of typing them again, you bring them back, because the shell has written down every line.

:::abbildung linux/k2verlauf 20
The history as a numbered list in the shell's memory. With the Up arrow key, you move backward through the list. At the end of the session, the shell writes the list to the file `~/.bash_history`; Ubuntu does not even record a line that begins with a space.
:::

:::definition Definition 5.2 (History)
<span class="anker" id="satz-5-2"></span>

The __history__ is the numbered list of recently typed command lines that the shell keeps in its memory. The Up arrow key brings back the previous line, and each further press an older one; the Down arrow key goes forward again. The builtin command `history` shows the list. At the end of the session, bash writes the history to the file `.bash_history` in your home folder, and the next session reads it back in from there.
:::

Ubuntu sets up the history so that the shell remembers the last 1 000 lines and the file keeps at most 2 000 lines. Two more default settings: a line that is exactly the same as the previous one is not recorded again, and a line that begins with a space is not recorded at all.

::::beispiel Three commands, one of them invisible
This session starts with an empty history. The third line begins with a space:

```text
student@labor:~$ whoami
student
student@labor:~$ uname -m
x86_64
student@labor:~$  echo geheim
geheim
student@labor:~$ history
    1  whoami
    2  uname -m
    3  history
```

`echo geheim` (“geheim” is German for “secret”) is missing from the list; `history` itself is an entry, too. Pressing the Up arrow key twice brings back the second entry, ready for editing or running:

```text
student@labor:~$ uname -m
```

In your own terminal, the numbers are higher, because there the history also contains the lines of earlier sessions.
::::

**Repeating lines with exclamation marks.** The shell also knows shortcuts that refer to the history: `!!` stands for the previous line, `!`*n* for the entry with the number *n*. The shell writes out the substituted line before running it so that you can see what happens:

```text
student@labor:~$ !!
history
    1  whoami
    2  uname -m
    3  history
```

⁠**In short:** The shell remembers every line in the history; the Up arrow key and `history` bring it back.

:::warnung No secrets on the command line
Everything you type on the command line ends up in the history and, at the end of the session, as plain text in `~/.bash_history`. So never type a password or an access key as an argument. Programs that need a password ask for it themselves and do not display what you type; this input does not get into the history. The space at the start of the line is not reliable protection: it works only because Ubuntu sets it up that way by default, and often not on other systems.
:::

### Reverse search

<span class="anker" id="stufe-5-3"></span>

If the command you are looking for is a hundred lines back, the arrow key is too slow. Usually, though, you remember a piece of the command, such as its name.

:::abbildung linux/k2rsuche 21
Reverse search with Ctrl+R. Each typed character narrows the search, and the shell shows the newest line of the history that contains what you typed. Another Ctrl+R jumps to the next older hit.
:::

:::definition Definition 5.3 (Reverse search)
<span class="anker" id="satz-5-3"></span>

The __reverse search__ searches the history from the newest line to the oldest for the text you type; you start it with Ctrl+R. Each further character narrows the search, and each further Ctrl+R jumps to the next older hit. Enter runs the command found, an arrow key takes it over for editing, and Ctrl+G cancels the search.
:::

::::beispiel Search twice, run once
The history contains `uname -r`, `whoami`, `uname -m` and `head -n 1 /etc/os-release`. After Ctrl+R and the letters `un`, the shell shows the newest matching line:

```text
(reverse-i-search)`un': uname -m
```

A second Ctrl+R jumps to the older line that contains `un`:

```text
(reverse-i-search)`un': uname -r
```

Enter runs it as if you had typed it again:

```text
student@labor:~$ uname -r
6.6.87.2-microsoft-standard-WSL2
```

If there is no older hit, the shell writes `failed` in front of the search and stays with the last one.
::::

⁠**In short:** Ctrl+R searches backward in the history for what you type; Enter runs the hit.

### Interrupting with Ctrl+C

<span class="anker" id="stufe-5-4"></span>

Sometimes a command runs longer than expected or waits for something that never comes, or you realize in the middle of a line that you wanted something else. Then you need an emergency exit that almost always works.

:::abbildung linux/k2strgcd 22
Two key combinations that do not arrive as ordinary characters. Ctrl+C becomes a request to the running program to stop immediately. Ctrl+D tells the reading program that no more input is coming.
:::

:::definition Definition 5.4 (Interrupting with Ctrl+C)
<span class="anker" id="satz-5-4"></span>

The key combination __Ctrl+C__ asks the program that is currently running in the terminal to stop immediately; almost all programs then stop, and the shell shows the prompt again. If no program is running, Ctrl+C discards the partly typed line. When you press it, `^C` appears in the window.
:::

::::beispiel A waiting program and half a line
The command `sleep 30` does nothing for 30 seconds and then ends; it is ideal for trying things out. Here, it was interrupted with Ctrl+C after one second. After that, `uname -r` was typed and, instead of Enter being pressed, discarded with Ctrl+C:

```text
student@labor:~$ sleep 30
^C
student@labor:~$ uname -r^C
student@labor:~$
```

The discarded line was not run.
::::

⁠**In short:** Ctrl+C interrupts the running program or discards the partly typed line.

:::warnung Ctrl+C does not copy in the terminal
In almost all programs, Ctrl+C copies the selected text; in the terminal, it interrupts. There, copy and paste work with **Ctrl+Shift+C** and **Ctrl+Shift+V**, in Ubuntu's terminal as well as in Windows Terminal. Windows Terminal additionally copies with Ctrl+C, but only while text is selected; without a selection, it sends Ctrl+C to the running program. If you get used to the variant with Shift, you never interrupt anything by accident.
:::

:::hintergrund Why Ctrl+C does not reach the shell
Every Ctrl combination with a letter produces a control character from the ASCII character table, which dates back to the era of teleprinters. Ctrl+C produces the character with the number 3, which is called “End of Text” there; the capital letter C has the number 67, and Ctrl subtracts 64. This character goes from the terminal emulator into the pseudoterminal from subsection [1.2](terminal-und-shell.html#stufe-1-2). There, the kernel handles it before any program reads it: it turns it into an interrupt message to the program that is currently running in the foreground of the terminal. Most programs then end immediately. Because the kernel does this, Ctrl+C works even with a program that no longer pays any attention to keys. The command `stty -a` shows the assignment in the line `intr = ^C`; “intr” stands for interrupt. This meaning in the terminal is older than the graphical interfaces in which Ctrl+C later came to mean copy.
:::

### The end of input with Ctrl+D

<span class="anker" id="stufe-5-5"></span>

Some programs read what you type, line by line, until you tell them that nothing more is coming. A word cannot do this, because any word could be part of the input. It takes a key of its own for “end”.

:::definition Definition 5.5 (End of input with Ctrl+D)
<span class="anker" id="satz-5-5"></span>

The key combination __Ctrl+D__ at the start of a line tells the program that is currently reading that no more input follows. A program that reads until the end of input is then finished. The shell itself also reads input; Ctrl+D on an empty command line therefore ends the session like `exit`.
:::

::::beispiel First for cat, then for the shell
`cat` without a file name reads what you type and prints each line again immediately. Here, `Hallo` and `Welt` were typed, each followed by Enter, and then Ctrl+D:

```text
student@labor:~$ cat
Hallo
Hallo
Welt
Welt
student@labor:~$
```

Each line appears twice: once as you typed it, once as `cat` printed it. After Ctrl+D, `cat` was finished, and the shell showed the prompt again. A second Ctrl+D on this empty line ends the shell; it writes `exit` as a farewell:

```text
student@labor:~$
exit
```
::::

⁠**In short:** Ctrl+D tells the reading program “no more input”; on the empty command line, it ends the shell.

:::hintergrund Ctrl+D is not an interrupt but an empty read
A program reads input by asking the kernel for the next characters with a system call. The kernel replies with the characters and their number. By fixed convention, a reply with zero characters means: the input has ended, just as at the end of a file. Ctrl+D produces control character number 4, “End of Transmission”, and the terminal driver in the kernel turns it into exactly this reply with zero characters, provided the line is still empty; `stty -a` shows it as `eof = ^D`, “end of file”. So the program is not interrupted as with Ctrl+C. It reads an end and stops of its own accord after it has finished its work. bash handles the key somewhat differently because it edits the line itself, but it reaches the same result: on an empty line, Ctrl+D counts as the end; on a line with text, it deletes the character under the cursor.
:::

### Keyboard shortcuts for the command line

<span class="anker" id="stufe-5-6"></span>

A long command line with a typo at the beginning: going back character by character with the arrow keys takes time. The shell knows keyboard shortcuts that make the cursor jump and delete whole pieces of the line.

:::abbildung linux/k2tasten 23
A command line with the cursor in the middle. Ctrl+A and Ctrl+E jump to the start and to the end, Ctrl+U deletes everything to the left of the cursor, Ctrl+K everything to the right of it, Ctrl+W the word before it.
:::

:::definition Definition 5.6 (Command-line keyboard shortcuts)
<span class="anker" id="satz-5-6"></span>

A __keyboard shortcut__ of the command line is a key combination that the shell does not write into the line as a character but carries out as an instruction to edit the line or the window. Table [4](#tab-4) lists the most important ones.
:::

<span class="anker" id="tab-4"></span>

**Table 4:** The most important keyboard shortcuts on the bash command line. The last row is handled not by the shell but by the terminal emulator.

| Keys | Effect |
|---|---|
| Tab key | complete names (subsection [5.1](#stufe-5-1)) |
| Up or Down arrow | older or newer line from the history (subsection [5.2](#stufe-5-2)) |
| Ctrl+R | search backward in the history (subsection [5.3](#stufe-5-3)) |
| Ctrl+C | interrupt the running program, discard the line (subsection [5.4](#stufe-5-4)) |
| Ctrl+D | end of input; on an empty line, end the shell (subsection [5.5](#stufe-5-5)) |
| Ctrl+L | clear the window; the current line stays at the top |
| Ctrl+A or Ctrl+E | to the start or to the end of the line |
| Ctrl+U | delete everything to the left of the cursor |
| Ctrl+K | delete everything to the right of the cursor |
| Ctrl+W | delete the word to the left of the cursor |
| Ctrl+Shift+C or V | copy or paste in the terminal |

::::beispiel Fixing a typo at the start of the line
You have typed `unme -n 2 /etc/os-release` and notice before pressing Enter that the command should have been `head`. Ctrl+A jumps to the start, pressing Del four times deletes `unme`, you type `head`, and Enter runs the line; where the cursor is at that moment does not matter. If you would rather start over, Ctrl+U discards everything to the left of the cursor, so after Ctrl+E the whole line. Ctrl+L then clears a full window without touching the line.
::::

⁠**In short:** Ctrl+A and Ctrl+E jump to the start and the end, Ctrl+U, Ctrl+K and Ctrl+W delete parts of the line, Ctrl+L clears the window.

:::hintergrund Who handles the keys: the Readline library
bash does not program completion, history, reverse search and the keyboard shortcuts for editing the line itself; it takes them from the program library GNU Readline, a collection of ready-made program code for editing an input line. Readline switches off the terminal driver's line-by-line processing, receives each keystroke individually and assembles the line itself; only when you press Enter does it pass the line on to bash. By default, the key bindings follow the text editor Emacs, hence the somewhat arbitrary-looking letters; useful memory aids are A for the beginning of the alphabet, E for end and K for kill, that is, cut away. If you prefer the editor vi, `set -o vi` switches to its keys. Because other programs with an input line also use Readline, the same shortcuts work there, too.
:::

### Exercises for Section [5](#stufe-5)

<span class="anker" id="stufe-5-7"></span>

:::aufgabe Exercise 17 ★ Completing instead of typing
<span class="anker" id="aufg-17"></span>

What is the smallest number of keys you need to type `cat /etc/os-release` with the help of the Tab key? Try `cat /etc/os`, once pressing the Tab key once and once pressing it twice. What does the shell show after `who` and pressing Tab twice, and why does it not complete right away?

:::loesung
`/etc/os` is unique, because only the file `os-release` begins with these letters. A single press of the Tab key completes it right away:

```text
student@labor:~$ cat /etc/os-release
```

A second press is then no longer needed. With `cat /etc/os`, one Tab and Enter, that makes 13 keys instead of 20. It can be done with even fewer, because in the top-level folder only `etc` begins with `e`: `cat /e`, Tab (giving `cat /etc/`), `os`, Tab, Enter make 11 keys. Just `o` instead of `os` is not enough, because `/etc` also contains the folder `opt`. For `who`, the shell cannot complete anything, because several commands begin like this, and `who` itself is already one of them. The second press lists them:

```text
student@labor:~$ who
who     whoami  whois
student@labor:~$ who
```

Under WSL 2, `whoami.exe` also appears, a Windows program, because WSL appends the folders of the Windows programs to the search path (subsection [3.2](arten-von-befehlen.html#stufe-3-2)).
:::
:::

:::aufgabe Exercise 18 ★★ Your own history
<span class="anker" id="aufg-18"></span>

In a new session, type `whoami`, `whoami` again, `uname -r` and ` echo test` (with a leading space) one after another, then `history`. Which entries appear at the end of the list, and why are two lines missing? What is at the end of the output of `history` after `exit` and a new session?

:::loesung
In a new session, these entries are at the end of the list:

```text
student@labor:~$ whoami
student
student@labor:~$ whoami
student
student@labor:~$ uname -r
6.6.87.2-microsoft-standard-WSL2
student@labor:~$  echo test
test
student@labor:~$ history
    1  cat
    2  whoami
    3  uname -r
    4  history
```

In this session, `cat` was already in the history before; on your system, the lines from your earlier sessions are there, and the numbers are higher. The second `whoami` is missing because Ubuntu does not record a line again if it is the same as the previous one; `echo test` is missing because of the space at the start. After `exit`, bash writes the history to `~/.bash_history`, including the line `exit`. A new session reads the file in, and at the end, `history` shows `whoami`, `uname -r`, `history`, `exit` and, as the newest entry, the new `history`.
:::
:::

:::aufgabe Exercise 19 ★★ Interrupt or end?
<span class="anker" id="aufg-19"></span>

Start `cat` without an argument, type a line and press Enter. End `cat` once with Ctrl+C and once with Ctrl+D. What looks the same to you in the window? Using the background boxes, explain what is different for `cat` in the two cases. What happens if you press Ctrl+D while a line with text is on the screen?

:::loesung
In the window, both look the same: `cat` ends, and the prompt appears again; with Ctrl+C, there is also a `^C`.

```text
student@labor:~$ cat
Hallo
Hallo
^C
student@labor:~$
```

For `cat`, it is different. With Ctrl+C, the kernel sends an interrupt message, and `cat` is ended in the middle of its work without deciding anything itself. With Ctrl+D, `cat` receives the reply “zero characters” to its read request, recognizes the end of input from this and ends itself after it has output everything it has read. For `cat`, this makes no visible difference; for a program that still has to save something at the end, it does.

If there is already text in the line when you press Ctrl+D, the kernel passes this text to `cat` without a line ending, and `cat` outputs it immediately; in the window, it then appears twice in a row. Only a second Ctrl+D meets an empty input and ends `cat`. Because the output had no line ending, the prompt appears directly after it. The input was `abc`, then Ctrl+D twice:

```text
student@labor:~$ cat
abcabcstudent@labor:~$
```
:::
:::

:::aufgabe Exercise 20 ★★★ Key arithmetic
<span class="anker" id="aufg-20"></span>

In the ASCII character table, the capital letter A has the number 65. Which numbers do Ctrl+A, Ctrl+D, Ctrl+L and Ctrl+R produce if Ctrl reduces the number by 64? Among other things, `stty -a` reports `susp = ^Z` and `kill = ^U`. Which numbers are these? Check your answer for Ctrl+U with Table [4](#tab-4): who deletes the line when bash is running?

:::loesung
Ctrl+A gives $65-64=1$, Ctrl+D $68-64=4$, Ctrl+L $76-64=12$, Ctrl+R $82-64=18$. Z has the number 90, so Ctrl+Z gives $26$; U has 85, so Ctrl+U gives $21$. According to `stty -a`, the kernel interprets Ctrl+U in the pseudoterminal as “kill”: it deletes the partly typed line as long as it manages the line itself, for example while `cat` is reading. If, on the other hand, bash is running at the prompt, Readline has switched off the kernel's line-by-line processing and receives the key itself; according to Table [4](#tab-4), it deletes everything to the left of the cursor. If the cursor is at the end of the line, both look the same.
:::
:::

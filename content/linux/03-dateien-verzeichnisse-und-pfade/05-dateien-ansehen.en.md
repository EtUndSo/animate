---
title: Viewing files
pfad: Computer Science / Linux and the Command Line / Files, Directories and Paths
adresse: informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade
knoten: Chapter 3: Files, Directories and Paths
order: 6080500
summary: Many files of a Linux system are text that you can read directly: configuration files, logs, instructions.
tags: text file, line end, cat, less, head, tail, wc, file
lang: en
---

<span class="anker" id="stufe-4"></span>

:::zweck
Many files of a Linux system are text that you can read directly: configuration files, logs, instructions. This section explains what makes a file a text file and shows the tools with which you view files in full, page by page, at the beginning or at the end, measure them and determine their type.
:::

:::::vorwissen What you need for this: the text file

<span class="anker" id="stufe-4-1"></span>

The tools in this section work with lines and characters. For this, it must be clear how lines and characters are contained in the bytes of a file.

**Characters as numbers.** Subsection [1.2](dateien-verzeichnisse-und-der-verzeichnisbaum.html#stufe-1-2) showed that every character is stored as a number. The rule by which Linux today translates characters into bytes is called UTF-8. For the letters without accents, the digits and the usual punctuation marks, UTF-8 needs exactly one byte per character. For umlauts, accents and other scripts, it needs two to four bytes; the `Ä`, for example, becomes the two bytes 195 and 132.

:::abbildung linux/k3text 13
A text file with two lines as a sequence of bytes. After each line comes the byte 10, the line end; an umlaut takes two bytes. Below, the same bytes as a program shows them as text.
:::

:::definition Definition 4.1 (Text file, line end)
<span class="anker" id="satz-4-1"></span>

A __text file__ is a file whose bytes represent nothing but characters. It is divided into lines: at the end of each line is the invisible character __line end__, the byte with the value 10, which programs often write as `\n`.
:::

So what is called a line is everything up to and including a line end. Figure [13](#abb-13) shows a small text file as bytes. A file that does not consist only of characters, such as a photo or a program, is by contrast called a binary file.

::::beispiel The time zone as characters
`od -c` shows each byte as a character; the line end appears as `\n`:

```console
$ od -An -c /etc/timezone
   E   u   r   o   p   e   /   B   e   r   l   i   n  \n
```

The file has a single line with 13 characters and the line end, 14 bytes in total.
::::

⁠**In short:** A text file consists only of characters; each line ends with the byte 10.

:::::

### Showing the entire contents: cat

<span class="anker" id="stufe-4-2"></span>

For a short file, it is enough to write the entire contents to the terminal at once. The simplest command in this section does exactly that.

:::definition Definition 4.2 (cat)
<span class="anker" id="satz-4-2"></span>

The command __cat__ reads the files given as arguments in turn and writes out their bytes unchanged, one after the other.
:::

The name comes from “concatenate”, to chain together: with several arguments, `cat` joins the contents byte by byte, without putting anything in between. For long files, `cat` is impractical, because the beginning rushes past the top edge of the window.

::::beispiel Two files one after the other
```console
$ cat /etc/hostname /etc/timezone
labor
Europe/Berlin
```

Because each of the two files ends with a line end, the contents appear on two lines.
::::

⁠**In short:** `cat` writes out the contents of files one after the other; for short files, this is the quickest look inside.

:::warnung Do not output binary files with cat
`cat` also writes the bytes of a program or photo to the terminal. For the terminal, some of these bytes are control commands; afterward, it may show nothing but strange characters. The command `reset`, which you type blind and send with Enter, gets you out of this state, as does a new window. So do not blindly output a file whose contents you do not know with `cat`.
:::

### Reading page by page: less

<span class="anker" id="stufe-4-3"></span>

It is better to read a long file like a book, page by page, with the option of paging back and searching for a word. The pager from [Chapter 2, Section 4.4](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/hilfe-finden.html#stufe-4-4) does exactly that.

:::definition Definition 4.3 (less with a file)
<span class="anker" id="satz-4-3"></span>

If __less__ receives a file as an argument, it shows the file's contents page by page. It does not change the file and does not load it all at once; that is why it opens even very large files immediately.
:::

In `less`, the same keys apply as for the manual pages ([Chapter 2, Section 4.4](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/hilfe-finden.html#stufe-4-4)). If `less` notices that a file is not a text file, it asks before showing it.

::::beispiel Reading a license text
Type `less /usr/share/common-licenses/GPL-3`. The first screen of the license appears, with the file name at the bottom. Type `/Distribution` and Enter, the search from [Chapter 2](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/die-shell-erste-befehle.html): `less` jumps to the first place with this word and highlights it. With `q`, you are back at the prompt, and the file is unchanged.
::::

⁠**In short:** `less file` shows a file page by page, with paging and search, without changing it.

### Beginning and end: head and tail

<span class="anker" id="stufe-4-4"></span>

For many files, only one piece is of interest: the head with a heading or the end, where the newest entries of a log are.

:::abbildung linux/k3headtail 14
A file as a stack of lines. `head -n 3` highlights the first three, `tail -n 2` the last two; the lines in between stay gray.
:::

:::definition Definition 4.4 (head, tail)
<span class="anker" id="satz-4-4"></span>

The command __head__ writes out the first lines of a file, the command __tail__ the last ones. Without an option, it is ten lines each; with the option `-n` and a number, you set how many.
:::

You already know `head -n 1` from [Chapter 2, Section 6.1](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/das-system-erkunden.html#stufe-6-1). Figure [14](#abb-14) shows which lines the two commands pick out of the same file.

::::beispiel Head of a license, end of a user list
The file `/etc/passwd` contains one user of the system on each line; the user created last is far down.

```console
$ head -n 3 /usr/share/common-licenses/GPL-3
                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

$ tail -n 2 /etc/passwd
student:x:1000:1000::/home/student:/bin/bash
tcpdump:x:986:986:tcpdump:/nonexistent:/usr/sbin/nologin
```

The third line of the license is empty; you see two lines of text and an empty line. In the user list, the fields are separated by colons; you can recognize the name `student` and the home directory `/home/student`.
::::

::::beispiel [Second example] The first ten lines
Without `-n`, `head` shows ten lines. `/etc/os-release` has thirteen:

```console
$ head /etc/os-release
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
```
::::

⁠**In short:** `head` shows the beginning, `tail` the end of a file, ten lines each or as many as `-n` says.

### Counting: wc

<span class="anker" id="stufe-4-5"></span>

How long is a file? Depending on the purpose, this means lines, words or bytes. One command delivers all three numbers at once.

:::abbildung linux/k3wc 15
`wc` counts three things in a small text: the line ends, the words, that is, sequences of characters between whitespace, and the bytes. Each number appears in its own column.
:::

:::definition Definition 4.5 (wc)
<span class="anker" id="satz-4-5"></span>

The command __wc__ (short for “word count”) prints three numbers for each file named: the number of lines, counted as the number of line ends, the number of words, that is, of the character sequences between spaces, tabs and line ends, and the number of bytes. With `-l`, `-w` or `-c`, it prints only lines, words or bytes.
:::

Several files get one line each, and at the end there is a sum with the word `total`. Figure [15](#abb-15) counts the three quantities in a small text.

::::beispiel Measuring the license
```console
$ wc /usr/share/common-licenses/GPL-3
  674  5644 35149 /usr/share/common-licenses/GPL-3
$ wc -l /etc/passwd
28 /etc/passwd
$ wc -c /etc/hostname
6 /etc/hostname
```

The license has 674 lines, 5644 words and 35 149 bytes; `ls -lh` showed 35K for it, rounded up from 34.3 KiB. On the test computer, there are 28 user accounts. `/etc/hostname` has the six bytes from subsection [1.2](dateien-verzeichnisse-und-der-verzeichnisbaum.html#stufe-1-2).
::::

⁠**In short:** `wc` counts lines, words and bytes; `-l`, `-w`, `-c` select one of the numbers.

### Determining the file type: file

<span class="anker" id="stufe-4-6"></span>

Because the system does not record what is in a file, and because the extension is only part of the name, you need a tool that recognizes the type of a file by its contents.

:::definition Definition 4.6 (file)
<span class="anker" id="satz-4-6"></span>

The command __file__ examines each file named and describes what it contains, such as text, an image in a particular format, a program or a directory. It judges by the contents, not by the name.
:::

First, `file` checks whether it is dealing with a special type such as a directory. Then it compares the first bytes with a long list of known signatures, and only at the end does it check whether the bytes form text. The first check that matches provides the answer. Figure [16](#abb-16) shows the middle step.

:::abbildung linux/k3magie 16
How `file` recognizes a file: it reads the first bytes and compares them with known signatures. For `/usr/bin/bash`, the bytes 127, `E`, `L`, `F` match the signature for programs; for the Ubuntu logo, the bytes 137, `P`, `N`, `G` match the signature for PNG images; the file name does not matter.
:::

::::beispiel Three kinds of files
```console
$ file /etc/passwd /usr/bin/bash /etc
/etc/passwd:   ASCII text
/usr/bin/bash: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=a292b52b679fb438b940f1c17e2e4951ac52ac89, for GNU/Linux 3.2.0, stripped
/etc:          directory
$ file /usr/share/pixmaps/ubuntu-logo-text.png
/usr/share/pixmaps/ubuntu-logo-text.png: PNG image data, 187 x 72, 8-bit/color RGBA, non-interlaced
```

`/etc/passwd` is text from the ASCII character set, that is, only characters with one byte each. `/usr/bin/bash` is a program in the ELF format, the format for programs on Linux, compiled for 64-bit processors of the x86-64 family; the name has no extension, and `file` recognizes it anyway. The image is a PNG graphic with 187 by 72 pixels.
::::

With that, you also have the tool for the caution box in subsection [4.2](#stufe-4-2): before you output an unknown file with `cat`, you ask `file` whether it contains text.

⁠**In short:** `file` determines the type of a file from its contents, regardless of name and extension.

:::hintergrund How file recognizes a file
Many file formats begin with a fixed sequence of bytes, a kind of signature called a magic number. Programs in the ELF format begin with the byte 127 and the letters `E`, `L`, `F`; PNG images with the byte 137 and the letters `P`, `N`, `G`. `od -c` shows this; it writes bytes that are not printable characters as octal numbers, that is, in base 8 instead of 10 ($177_8 = 127$, $211_8 = 137$):

```console
$ od -An -c -N4 /usr/bin/bash
 177   E   L   F
$ od -An -c -N4 /usr/share/pixmaps/ubuntu-logo-text.png
 211   P   N   G
```

The option `-N4` reads only the first four bytes. `file` has a collection of thousands of such markers, together with rules for which further bytes it should evaluate, such as the image size for PNG. There is a practical reason why the marker is at the very beginning: a program only has to read a few bytes to know whether it can do anything with the file. The kernel itself also checks the first bytes when a program is started, before it runs it.
:::

### Exercises for Section [4](#stufe-4)

<span class="anker" id="stufe-4-7"></span>

:::aufgabe Exercise 11 ★ Which command?
<span class="anker" id="aufg-11"></span>

Which command from this section do you use to (a) see the last five lines of a log, (b) read a text with 2000 lines at your leisure and search for a word in it, (c) find out whether a file named `urlaub.jpg` really is a photo, (d) count how many lines a file has, (e) read two short files directly one after the other?

:::loesung
(a) `tail -n 5 file`. (b) `less file`, and in it `/word` to search. (c) `file urlaub.jpg`; the extension proves nothing. (d) `wc -l file`. (e) `cat file1 file2`.
:::
:::

:::aufgabe Exercise 12 ★★ Measuring the license
<span class="anker" id="aufg-12"></span>

Work with `/usr/share/common-licenses/GPL-3`. (a) How many words are there on average per line? (b) Show the last three lines. (c) How many bytes does a line have on average, counting the line end? (d) Why does the number from `wc -c` match the size from `ls -l` but not the one from `ls -lh`?

:::loesung
(a) $5644 / 674 \approx 8.37$ words per line; the blank lines of the license pull the average down.

(b) The last three lines:

```console
$ tail -n 3 /usr/share/common-licenses/GPL-3
the library.  If this is what you want to do, use the GNU Lesser General
Public License instead of this License.  But first, please read
<https://www.gnu.org/licenses/why-not-lgpl.html>.
```

(c) $35\,149 / 674 \approx 52.1$ bytes per line, counting the line end.

(d) `wc -c` counts the bytes of the contents, and `ls -l` also shows the number of bytes of the contents as the size; both say 35 149. `ls -lh` converts to units of 1024 bytes and rounds up: $35\,149 / 1024 \approx 34.3$ becomes `35K`.
:::
:::

:::aufgabe Exercise 13 ★★★ Recognizing the type by the first bytes
<span class="anker" id="aufg-13"></span>

Use `od -An -c -N2` to show the first two bytes of `/usr/share/pixmaps/debian-logo.bmp`. Which letters appear? Then check with `file` which format it is, and explain why a program that displays images would not even need the extension `.bmp`.

:::loesung
```console
$ od -An -c -N2 /usr/share/pixmaps/debian-logo.bmp
   B   M
$ file /usr/share/pixmaps/debian-logo.bmp
/usr/share/pixmaps/debian-logo.bmp: PC bitmap, Windows 98/2000 and newer format, 48 x 48 x 32, cbSize 9354, bits offset 138
```

The file begins with the letters `B` and `M`, the signature of the image format BMP; `file` calls it “PC bitmap” and reads the image size of 48 by 48 pixels from the following bytes. A program that displays images can proceed in the same way: read the first bytes and recognize from the marker which format it is. It does not need the extension `.bmp` for this; the extension helps people and file managers that want to suggest a suitable program from the name alone, without opening the file.
:::
:::

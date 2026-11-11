---
title: Redirecting input
pfad: Computer Science / Linux and the Command Line / Streams, Redirection, Pipes and Exit Status
adresse: informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status
knoten: Chapter 4: Streams, Redirection, Pipes and Exit Status
order: 6090400
summary: What works for output also works for input: the shell can connect the standard input of a program to a file or give it a few lines of text that are written directly in the command line.
tags: here document, here string
lang: en
---

<span class="anker" id="stufe-3"></span>

:::zweck
What works for output also works for input: the shell can connect the standard input of a program to a file or give it a few lines of text that are written directly in the command line. This section shows three ways to do this.
:::

### Input redirection: <

<span class="anker" id="stufe-3-1"></span>

`wc -l einkauf.txt` counts the lines and writes the file name after the count. If you want only the number, for example to process it further, you have to give the file to `wc` in such a way that it never learns its name. Figure [11](#abb-11) puts the two ways side by side.

:::abbildung linux/k4eingabe 11
Two ways to count a file. Left, `wc -l einkauf.txt`: `wc` gets the name as an argument, opens the file itself and writes the name after the number. Right, `wc -l < einkauf.txt`: the shell opens the file and connects it to descriptor 0; `wc` reads only a stream without a name and writes only the number.
:::

:::definition Definition 3.1 (Input redirection)
<span class="anker" id="satz-3-1"></span>

The notation `command < file` opens the file for reading and connects it to the standard input of the new process. The program gets no file name, only the stream.
:::

::::beispiel With and without a name
```console
$ wc -l einkauf.txt
5 einkauf.txt
$ wc -l < einkauf.txt
5
```

In the second call, `wc` got no argument, so it reads its standard input; it does not know that `einkauf.txt` is behind it.
::::

::::beispiel [Second example] Who reports the error?
```console
$ wc -l < fehlt.txt
bash: fehlt.txt: No such file or directory
```

The message begins with `bash`, not with `wc`. The shell could not open the file `fehlt.txt` (German for “missing”) and therefore never started `wc` at all. This shows once more who sets up a redirection.
::::

⁠**In short:** `command < file` makes a file the standard input; the program reads a stream and does not know the name.

### The here document

<span class="anker" id="stufe-3-2"></span>

Sometimes a program needs only a few lines as input, and it is not worth creating a file for them first. It would be convenient to write the lines directly into the command line and tell the shell where they end. Figure [12](#abb-12) shows how the shell collects such lines.

:::abbildung linux/k4heredoc 12
A here document: the shell reads the lines after `cat <<ENDE` until a line contains only `ENDE`. It gives the collected lines, without the end line, to `cat` as standard input.
:::

:::definition Definition 3.2 (Here document)
<span class="anker" id="satz-3-2"></span>

A __here document__ is a redirection of the form `command <<ENDMARKER`, followed by lines of text and finally a line that contains only the end marker. The shell collects the lines in between and gives them to the command as standard input; the line with the end marker is not part of it.
:::

The name describes the idea: the document is right “here”, where the text is needed. You can choose the end marker freely; `ENDE` (German for “end”) and `EOF`, short for “end of file”, are common. If you type a here document in the terminal, the shell shows the character `>` before each further line as a sign that the command is not yet complete; you do not type this `>`, and it has nothing to do with redirection.

::::beispiel Two lines for cat
Type `cat <<ENDE`, then the lines `Milch`, `Brot` and `ENDE`:

```console
$ cat <<ENDE
> Milch
> Brot
> ENDE
Milch
Brot
```

Only after the line `ENDE` does `cat` start; it reads the two lines from its standard input and writes them out.
::::

Redirections can be combined: the here document supplies the input, and `>` sends the output into a file. In this way, you create the fruit list that the following sections work with: `obst.txt` (German for “fruit”), with `Apfel`, `Birne` and `Banane` (German for “apple”, “pear” and “banana”). Create it in your practice directory:

```console
$ cat > obst.txt <<ENDE
> Apfel
> Birne
> Apfel
> Kiwi
> Banane
> Apfel
> Birne
> ENDE
$ wc -l obst.txt
7 obst.txt
```

⁠**In short:** A here document gives a command the following lines, up to the end marker, as standard input.

:::hintergrund A dollar sign in a here document
The shell does not take the text of a here document entirely literally: to the shell, a `$` introduces a substitution, in which it puts in, at this point, a value that it has remembered; for `$5`, it has none here, and nothing remains. If the end marker is in quotation marks, the shell takes the text character for character:

```console
$ cat <<ENDE
> Eis: $5 pro Kugel
> ENDE
Eis:  pro Kugel
$ cat <<'ENDE'
> Eis: $5 pro Kugel
> ENDE
Eis: $5 pro Kugel
```

In the first case, the price has disappeared (the line is German for “Ice cream: $5 per scoop”); with `'ENDE'`, the text stays as it is.
:::

### The here string

<span class="anker" id="stufe-3-3"></span>

If the input is only a single line, even a here document with an end line is cumbersome. There is a shorter form for this. Figure [13](#abb-13) shows what stream the shell makes from it.

:::abbildung linux/k4herestring 13
From `<<< "Linux"`, the shell makes a stream of six bytes: the five letters and an appended line end. `wc -c` therefore counts 6.
:::

:::definition Definition 3.3 (Here string)
<span class="anker" id="satz-3-3"></span>

A __here string__ is a redirection of the form `command <<< "text"`. The shell gives the command the text as standard input and appends a line end.
:::

::::beispiel Counting words, swapping letters
```console
$ wc -w <<< "Heute gibt es Kuchen"
4
$ tr a-z A-Z <<< "hallo linux"
HALLO LINUX
$ wc -c <<< "Linux"
6
```

`wc -w` counts four words. The command `tr` reads its standard input and replaces each character from the first list with the character at the same position in the second; `a-z` stands for all lowercase letters from a to z, `A-Z` for the uppercase letters. `wc -c` counts six bytes for a word of five letters: the sixth is the line end that the shell appended.
::::

⁠**In short:** A here string gives a command one line of text as standard input, with a line end appended.

### Exercises for Section [3](#stufe-3)

<span class="anker" id="stufe-3-4"></span>

:::aufgabe Exercise 10 ★ With or without a name
<span class="anker" id="aufg-10"></span>

Compare `wc -c einkauf.txt` and `wc -c < einkauf.txt`. (a) What is the same, and what is different? (b) Why can `wc` not output the name at all in the second case? (c) What does `wc -c < gibtsnicht.txt` report, and which program writes the message?

:::loesung
```console
$ wc -c einkauf.txt
32 einkauf.txt
$ wc -c < einkauf.txt
32
$ wc -c < gibtsnicht.txt
bash: gibtsnicht.txt: No such file or directory
```

(a) The number is the same, 32 bytes. The difference is that only the first call writes the name after it. (b) In the second call, `wc` did not get an argument; the shell opened the file and connected it to descriptor 0. `wc` reads a stream, and a stream has no name. (c) The message is written by the shell, recognizable by the beginning `bash:`. It could not open the file and therefore did not start `wc`.
:::
:::

:::aufgabe Exercise 11 ★★ A week as a here document
<span class="anker" id="aufg-11"></span>

(a) Use a here document to create the file `woche.txt`, which contains the seven days of the week, each on a line of its own. (b) Check with `wc -l` that there are seven lines. (c) Use a second here document to append the lines `Feiertag` and `Urlaub` to `woche.txt` without losing the days of the week, and check with `wc -l` that there are now nine lines.

:::loesung
```console
$ cat > woche.txt <<ENDE
> Montag
> Dienstag
> Mittwoch
> Donnerstag
> Freitag
> Samstag
> Sonntag
> ENDE
$ wc -l woche.txt
7 woche.txt
$ cat >> woche.txt <<ENDE
> Feiertag
> Urlaub
> ENDE
$ wc -l woche.txt
9 woche.txt
```

(a) and (b): The here document delivers the seven lines as the standard input of `cat`, and `>` sends them into the file. The line `ENDE` is not part of it, which is why there are seven lines and not eight. (c) The input again comes from a here document; this time the output goes into the file with `>>`, so the shell does not empty it, and the two new lines go after the seven old ones. With `>`, only `Feiertag` and `Urlaub` would be left in it afterward.
:::
:::

:::aufgabe Exercise 12 ★ Bytes in a here string
<span class="anker" id="aufg-12"></span>

Predict what `wc -c <<< "Kaffee"` and `wc -c <<< "Äpfel"` output, and check it. Explain both numbers.

:::loesung
```console
$ wc -c <<< "Kaffee"
7
$ wc -c <<< "Äpfel"
7
```

`Kaffee` has six letters of one byte each, plus the line end that the here string appends: 7. `Äpfel` has only five letters, but the `Ä` takes up two bytes in UTF-8 ([Chapter 3, Section 4.1](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-ansehen.html#stufe-4-1)): $2 + 4 + 1 = 7$.
:::
:::

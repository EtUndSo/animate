---
title: Word splitting and quoting
pfad: Computer Science / Linux and the Command Line / How the Shell Reads a Command Line: Expansion, Quoting, Variables, Environment
adresse: informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung
knoten: Chapter 5: How the Shell Reads a Command Line: Expansion, Quoting, Variables, Environment
order: 6100400
summary: After the expansions, the shell splits some results into words once more.
tags: printf, Word splitting, Quoting, backslash
lang: en
---

<span class="anker" id="stufe-3"></span>

:::zweck
After the expansions, the shell splits some results into words once more. That is the reason for the surprise with `mein bericht.txt` from “What this is about”. This section shows when the shell does this, how you use quotes and the backslash to control what it may change and in which order all the steps of expansion take place.
:::

### Showing arguments one by one: printf

<span class="anker" id="stufe-3-1"></span>

`echo` writes its arguments with one space between each of them. From the output, you cannot tell whether it received one argument with a space in it or two arguments. For this section, however, you need exactly that: the boundaries between the arguments. Figure [10](#abb-10) shows a tool that makes them visible.

:::abbildung linux/k5printf 10
`printf "[%s]\n" eins zwei`: `printf` applies its format to the first remaining argument and writes `[eins]` with a line end. Because one argument is still left, it applies the format a second time and writes `[zwei]`. Each line of the output is one argument.
:::

:::definition Definition 3.1 (printf)
<span class="anker" id="satz-3-1"></span>

The builtin command __printf__ writes text according to a format, its first argument. In the format, `%s` stands for the next argument and `\n` for a line end. If arguments are still left after the pass through the format, `printf` applies the format again.
:::

With the format `"[%s]\n"`, `printf` therefore writes each argument in square brackets on a line of its own. The quotes hold the format together as one argument and protect the square brackets and the backslash from the shell, just like the quotes around the pattern in `find -name "*.txt"` in [Chapter 3, Section 10.2](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-finden-und-platz-messen.html#stufe-10-2); this section shows exactly what they do.

::::beispiel Two words, two arguments
```console
$ echo eins    zwei
eins zwei
$ printf "[%s]\n" eins    zwei
[eins]
[zwei]
```

The four spaces between `eins` and `zwei` (German for “one” and “two”) only separate two words; when writing, `echo` puts a single space between them. `printf` shows the two arguments as two lines.
::::

⁠**In short:** `printf "[%s]\n"` writes each argument in brackets on a line of its own and thus makes visible which arguments a command receives.

### Word splitting

<span class="anker" id="stufe-3-2"></span>

Two observations do not fit together at first. The shopping list has four lines, but `echo $(cat einkauf.txt)` writes them on a single line. And a variable that contains the name `mein bericht.txt` is of no help to `ls`:

```console
$ echo $(cat einkauf.txt)
Milch Brot Äpfel Kaffee
$ touch "mein bericht.txt"
$ datei="mein bericht.txt"
$ ls $datei
ls: cannot access 'mein': No such file or directory
ls: cannot access 'bericht.txt': No such file or directory
```

The file `mein bericht.txt` exists, the variable contains exactly this name, and yet `ls` looks for two files. Both puzzles have the same cause, which Figure [11](#abb-11) shows.

:::abbildung linux/k5worttrennung 11
`ls $datei` with the value `mein bericht.txt`. Parameter expansion inserts the value, one word with a space in it. Then word splitting splits this result at the space into two words, and `ls` receives two arguments. Below, `ls "$datei"`: the quotes prevent the splitting, and `ls` receives one argument.
:::

:::definition Definition 3.2 (Word splitting)
<span class="anker" id="satz-3-2"></span>

__Word splitting__ splits the results of parameter expansion, command substitution and arithmetic expansion into separate words, provided these expansions were not within double quotes. The splitting happens at spaces, tabs and line ends; several of them in a row count as one, and at the beginning and at the end they are dropped. Text that you typed yourself is not split a second time by word splitting.
:::

The words that result then still go through pathname expansion: if such a word contains a pattern character, it is replaced with file names like a typed pattern. A result that is completely empty or consists only of such separator characters produces no word at all.

::::beispiel The puzzles solved
```console
$ liste=$(cat einkauf.txt)
$ printf "[%s]\n" $liste
[Milch]
[Brot]
[Äpfel]
[Kaffee]
```

The variable `liste` holds the four lines, separated by line ends; command substitution removed only the last one. Without quotes, word splitting splits the value at the line ends into four words; `echo` would have written them on one line with spaces between them. The same happens to the file name at the space:

```console
$ printf "[%s]\n" $datei
[mein]
[bericht.txt]
```
::::

::::beispiel [Second example] Empty values and patterns in variables
```console
$ leer=
$ printf "[%s]\n" $leer Ende
[Ende]
$ muster="*.jpg"
$ echo $muster
foto1.jpg foto10.jpg foto2.jpg
```

The empty variable produces no word; `printf` receives only `Ende` (German for “end”). `muster` (German for “pattern”) holds the text `*.jpg`; after word splitting, it goes through pathname expansion, and `echo` receives the names of the photos.
::::

⁠**In short:** Word splitting splits the results of expansions without double quotes at spaces, tabs and line ends; after that, pattern characters in them take effect as well.

:::hintergrund Where the shell gets the separator characters
The characters at which word splitting splits are stored in a shell variable named `IFS` (short for “internal field separator”). `printf` with the format `%q` writes a value in such a way that you can recognize invisible characters:

```console
$ printf "%q\n" "$IFS"
$' \t\n'
```

Between `$'` and `'`, there are a space, `\t` for the tab and `\n` for the line end. Older shells used these characters to split every word of a line, including typed ones. Today's standard for Unix shells restricts word splitting to the results of expansions; its rationale explicitly names security as a reason, too. You can change `IFS`, for example to a colon; in the interactive shell, however, this affects every following command, so it is better to leave it alone there.
:::

### Quoting

<span class="anker" id="stufe-3-3"></span>

Expansion and word splitting are usually wanted, but sometimes not: a file name should remain one word, a pattern should reach `find` unchanged, a dollar sign should be a dollar sign. So you need a way to tell the shell: please take these characters literally.

:::definition Definition 3.3 (Quoting)
<span class="anker" id="satz-3-3"></span>

__Quoting__ means marking characters of a command line so that the shell takes them literally instead of giving them a special meaning. The three basic means for this are single quotes, double quotes and the backslash. What is marked in this way stays together when the line is split into words.
:::

“To quote” here means to put something in quotes. The three means differ in how much they protect. In all three cases, the shell removes the quotes and backslashes before the program starts.

::::beispiel The same name three times
```console
$ printf "[%s]\n" 'mein bericht.txt' "mein bericht.txt" mein\ bericht.txt
[mein bericht.txt]
[mein bericht.txt]
[mein bericht.txt]
```

All three notations produce the same single argument, without quotes and without a backslash.
::::

⁠**In short:** Quoting marks characters that the shell is to take literally; there are single and double quotes and the backslash.

:::hintergrund A fourth form: $'…'
bash and, since 2024, the standard for Unix shells as well know another form: single quotes with a dollar sign in front. Inside them, notations such as `\n` for a line end and `\t` for a tab apply; otherwise everything is literal, as between single quotes:

```console
$ echo $'Milch\nBrot'
Milch
Brot
```

`printf` used the same form in the background box on word splitting to show the invisible characters in `IFS`.
:::

### Single quotes

<span class="anker" id="stufe-3-4"></span>

You need the strongest means when a text is to reach the program exactly as it is written: a pattern for `find`, a sentence with dollar signs.

:::definition Definition 3.4 (Single quotes)
<span class="anker" id="satz-3-4"></span>

Between single quotes `'…'`, the shell takes every character literally. No expansion takes place, and everything in between stays one word. A single quote itself cannot occur inside them, not even with a backslash in front of it.
:::

::::beispiel Everything stays as it is
```console
$ echo '$HOME ~ *.txt {a,b} $((1+1))'
$HOME ~ *.txt {a,b} $((1+1))
$ echo Preis: $5
Preis:
$ echo 'Preis: $5'
Preis: $5
$ echo 'Gabi'\''s Café'
Gabi's Café
```

Without quotes, the shell takes `$5` for a parameter like `$?` that has no value here, and the price disappears (“Preis” is German for “price”). An apostrophe in the text takes a detour: you end the single quotes, write `\'` and start new ones. The shell joins the pieces into one word.
::::

⁠**In short:** Between single quotes, everything is literal; only a single quote itself is not possible there.

### Double quotes

<span class="anker" id="stufe-3-5"></span>

Often you want both: a value is to be inserted but not fall apart afterward. That is exactly the case with `ls $datei`.

:::definition Definition 3.5 (Double quotes)
<span class="anker" id="satz-3-5"></span>

Between double quotes `"…"`, the shell takes all characters literally except three: `$` still introduces a parameter expansion, a command substitution or an arithmetic expansion, `` ` `` a command substitution in the old notation, and `\` still has an effect before `$`, `` ` ``, `"`, `\` and the line end. Word splitting, pathname expansion, tilde expansion and brace expansion do not take place; the whole stays one word.
:::

::::beispiel Inserting yes, splitting no
```console
$ ls "$datei"
'mein bericht.txt'
$ echo "$HOME ~ *.txt {a,b} $((1+1))"
/home/student ~ *.txt {a,b} 2
$ echo "$(cat einkauf.txt)"
Milch
Brot
Äpfel
Kaffee
$ echo "Preis: \$5"
Preis: $5
$ echo "Gabi's Café"
Gabi's Café
```

Now `ls` finds the file; you know the quotes that it puts around the name from [Chapter 3, Section 3.7](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/den-inhalt-eines-verzeichnisses-anzeigen.html#stufe-3-7). In the second line, `$HOME` and `$((1+1))` are inserted, while the tilde, pattern and braces stay as they are. The shopping list keeps its line ends because word splitting does not happen. The backslash turns the dollar sign in `$5` into an ordinary character, and an apostrophe is an ordinary character between double quotes.
::::

⁠**In short:** Between double quotes, the shell inserts values with `$` but does not split them, and it does not evaluate patterns, tildes or braces.

:::hintergrund The exclamation mark
In interactive bash, the exclamation mark has a special role: it recalls earlier commands from the history, like `!!` in [Chapter 2, Section 5.2](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/schneller-arbeiten-vervollstandigung-verlauf-tastenkurzel.html#stufe-5-2). It keeps this meaning even between double quotes:

```console
$ echo "Achtung!Neu"
bash: !Neu: event not found
$ echo 'Achtung!Neu'
Achtung!Neu
```

In the first line, the shell searched the history for a command that begins with `Neu`, found none and discarded the whole line; `echo` did not run. Between single quotes, the exclamation mark is an ordinary character. If the exclamation mark is followed by a space or stands directly before the closing quote, it stays harmless even between double quotes.
:::

### The backslash

<span class="anker" id="stufe-3-6"></span>

Sometimes only a single character is to lose its special meaning: a space in a name, an asterisk, a dollar sign. Quotes around the whole word would be more than necessary for that.

:::definition Definition 3.6 (Backslash)
<span class="anker" id="satz-3-6"></span>

A __backslash__ `\` outside of quotes removes the special meaning of the character directly after it. If it stands at the end of a line, it joins that line with the next one into a single command line.
:::

The Tab key inserts it automatically before spaces in file names ([Chapter 3, Section 3.7](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/den-inhalt-eines-verzeichnisses-anzeigen.html#stufe-3-7)). If you end a line with `\` and press Enter, the shell shows a `>` at the beginning of the next line, as with the here document in [Chapter 4, Section 3.2](/wissen/en/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/eingaben-umleiten.html#stufe-3-2), and waits for the rest.

::::beispiel Protecting single characters
```console
$ echo \$HOME \* \~
$HOME * ~
$ ls mein\ bericht.txt
'mein bericht.txt'
$ echo Milch Brot \
> Äpfel Kaffee
Milch Brot Äpfel Kaffee
```

In the first line, the dollar sign, asterisk and tilde remain ordinary characters. In the last one, the backslash joins two typed lines; `echo` receives four arguments.
::::

Table [1](#tab-1) summarizes what the three means of quoting prevent.

<span class="anker" id="tab-1"></span>

**Table 1:** What the shell still does with a word, depending on the quoting. “yes” means: the shell evaluates the character; “no”: it takes it literally.

|  | none | `"…"` | `'…'` | `\` before the character |
|---|---|---|---|---|
| Space separates words | yes | no | no | no |
| Patterns `*` `?` `[…]` | yes | no | no | no |
| Tilde and braces `{…}` | yes | no | no | no |
| `$NAME`, `$(…)`, `$((…))` | yes | yes | no | no |
| Word splitting of the inserted value | yes | no | n/a | n/a |

⁠**In short:** The backslash protects exactly one character; at the end of a line, it continues the command line on the next line.

### Quote removal

<span class="anker" id="stufe-3-7"></span>

The quotes do not reach the program; [Chapter 3](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-verzeichnisse-und-pfade.html) already said that. What remains open is what happens to quotes that are strung together, that enclose nothing or that are part of a value. Figure [12](#abb-12) shows the last step of expansion.

:::abbildung linux/k5entfernen 12
The typed word `"mein "'bericht'.txt` consists of three pieces: a piece in double quotes, one in single quotes and one without. The shell removes the four quotes and joins the pieces; what remains is the one argument `mein bericht.txt`.
:::

:::definition Definition 3.7 (Quote removal)
<span class="anker" id="satz-3-7"></span>

As the last step of expansion, the shell removes all quotes and backslashes that you typed and that are not themselves protected. Characters of this kind that only entered the line through an expansion, for example from the value of a variable, stay in place.
:::

::::beispiel Joined, empty and in a value
```console
$ printf "[%s]\n" "mein "'bericht'.txt
[mein bericht.txt]
$ printf "[%s]\n" "" Ende
[]
[Ende]
$ x='"a b"'
$ printf "[%s]\n" $x
["a]
[b"]
```

Pieces without spaces between them form one word. Two quotes with nothing in between produce an empty argument that is kept, unlike an empty variable without quotes in subsection [3.2](#stufe-3-2). The quotes in the value of `x`, by contrast, are data: they protect nothing, word splitting splits the value at the space, and the quotes end up in the arguments.
::::

⁠**In short:** At the end, the shell removes the typed quotes and backslashes and joins the pieces of a word; quotes from values remain ordinary characters.

### The rule: expansions in double quotes

<span class="anker" id="stufe-3-8"></span>

The last subsections lead to a habit that prevents many errors. An experiment in which the wrong files disappear without it shows how important it is.

:::satz Theorem 3.8 (Rule for quoting)
<span class="anker" id="satz-3-8"></span>

Put every parameter expansion and every command substitution in double quotes, that is, `"$datei"` and `"$(command)"`, unless you explicitly want its result to fall apart into words. Put text that a program is to receive unchanged, such as a pattern for `find`, in single quotes.
:::

:::warnung rm $datei without quotes
Without quotes, `rm` can delete files other than the intended one. Try this only in your practice directory. `mein bericht.txt` is there, and `datei` (German for “file”) contains this name. In addition, create two files named `mein` and `bericht.txt`:

```console
$ touch mein bericht.txt
$ ls
 bericht.txt   foto1.jpg    foto2.jpg  'mein bericht.txt'   urlaub
 einkauf.txt   foto10.jpg   mein        notiz.txt
$ rm $datei
$ ls
 einkauf.txt   foto10.jpg  'mein bericht.txt'   urlaub
 foto1.jpg     foto2.jpg    notiz.txt
```

`mein bericht.txt` was intended; `mein` and `bericht.txt` were deleted, without asking and without a message. Figure [13](#abb-13) shows how this came about. With `rm "$datei"`, exactly the intended file would have disappeared.
:::

:::abbildung linux/k5datensteuerung 13
`rm $datei` with the value `mein bericht.txt` in a directory that also contains `mein` and `bericht.txt`. The two arguments that word splitting made from the one name hit two other files: `rm` deletes them, and the intended one stays.
:::

⁠**In short:** Expansions belong in double quotes, text for programs in single quotes; otherwise a value can turn into several arguments.

:::hintergrund Data turns into control
What goes wrong with `rm $datei` follows a general pattern. The value of the variable is meant as data, as a single file name. Without quotes, the shell interprets parts of it as control characters: the space as a boundary between arguments, an asterisk as a pattern. A minus sign at the beginning of the value, on the other hand, is interpreted only by the program, as the start of an option, and that happens even between quotes; only `--` from [Chapter 2, Section 2.7](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/der-aufbau-einer-befehlszeile.html#stufe-2-7) protects against this. Whoever determines the value, for example through a cleverly chosen file name, thus has a say in what the command does. The same confusion of data and command lies behind many security vulnerabilities in programs that build text from outside into commands; the Cybersecurity series takes this up. The remedy here is always the same: mark data so that it stays data. Experienced users therefore stick to the simple rule of putting every expansion in double quotes when in doubt.
:::

### The order of all steps

<span class="anker" id="stufe-3-9"></span>

Now you know all the expansions. Some surprises can only be explained once you know in which order the shell carries them out. As a picture for orientation, this is a workshop with several stations through which every command line passes in turn; only at the end is the program started with the finished list of arguments. Figure [14](#abb-14) sends a line through it.

:::abbildung linux/k5werkstatt 14
The shell's workshop. The line `ls -l {foto,notiz}* "$HOME"` passes through the stations: splitting into words, brace expansion (`foto* notiz*`), parameter expansion (`/home/student`), word splitting (changes nothing here), pathname expansion (the names of the photos and `notiz.txt`), quote removal. At the bottom is the finished argument list with which `ls` starts.
:::

:::satz Theorem 3.9 (Order of expansion)
<span class="anker" id="satz-3-9"></span>

The shell processes a command line in this order:

<ol>

<li>

It splits the line into words, taking the quoting into account; if the first word is an alias, it replaces it ([Chapter 2, Section 3.4](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/arten-von-befehlen.html#stufe-3-4)).

</li>

<li>

Brace expansion.

</li>

<li>

Tilde expansion, parameter expansion, arithmetic expansion and command substitution, in one pass from left to right.

</li>

<li>

Word splitting of the results from step 3 that are not within double quotes.

</li>

<li>

Pathname expansion.

</li>

<li>

Quote removal.

</li>

</ol>

After that, it sets up the redirections ([Chapter 4, Section 2](/wissen/en/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/ausgaben-umleiten.html#stufe-2)) and runs the command.
:::

Each step works only with what the previous one has left. What a later step produces, an earlier one never sees. With `printf`, you can check the finished argument list from Figure [14](#abb-14); instead of `ls`, `printf` receives the same words:

```console
$ printf "[%s]\n" -l {foto,notiz}* "$HOME"
[-l]
[foto1.jpg]
[foto10.jpg]
[foto2.jpg]
[notiz.txt]
[/home/student]
```

::::beispiel What follows from the order
```console
$ n=3
$ echo {1..$n}
{1..3}
$ ordner="~/linuxk5"
$ ls $ordner
ls: cannot access '~/linuxk5': No such file or directory
$ muster="*.jpg"
$ echo $muster "$muster"
foto1.jpg foto10.jpg foto2.jpg *.jpg
```

Brace expansion comes before parameter expansion; it saw `{1..$n}` and found no valid sequence in it, and when `$n` then became `3`, its step was over. Because of the quotes, `ordner` (German for “folder”) holds a real tilde; tilde expansion, however, replaces only typed tildes, not those that an expansion inserted. Pathname expansion comes after word splitting and therefore affects the unprotected `$muster`, not `"$muster"`.
::::

⁠**In short:** Splitting, braces, then tilde, parameters, arithmetic expansion and command substitution from left to right, then word splitting, patterns and finally quote removal.

:::hintergrund Not every shell knows braces
The standard for Unix shells describes steps 1 and 3 to 6. Brace expansion is a special feature of bash and some other shells. On Ubuntu, the command `sh` starts the small shell dash, which sticks closely to the standard:

```console
$ bash -c 'echo {a,b}'
a b
$ sh -c 'echo {a,b}'
{a,b}
```

`bash -c` and `sh -c` run the text in the single quotes in a new shell. dash leaves the braces as they are. Anyone who writes commands for other shells therefore does not rely on braces.
:::

### Exercises for Section [3](#stufe-3)

<span class="anker" id="stufe-3-10"></span>

:::aufgabe Exercise 9 ★ HOME three times
<span class="anker" id="aufg-9"></span>

Predict what `echo "$HOME" '$HOME' \$HOME "~" ~ "*.txt" *.txt` outputs in your practice directory, and check it. For each of the seven words, state which expansion took effect and which one the quoting prevented.

:::loesung
```console
$ echo "$HOME" '$HOME' \$HOME "~" ~ "*.txt" *.txt
/home/student $HOME $HOME ~ /home/student *.txt Lea_notizen.txt einkauf.txt notiz.txt
```

`"$HOME"`: parameter expansion, even within double quotes. `'$HOME'`: single quotes prevent any expansion. `\$HOME`: the backslash takes away the special meaning of the dollar sign. `"~"`: within double quotes, there is no tilde expansion. `~`: tilde expansion. `"*.txt"`: within double quotes, there is no pathname expansion. `*.txt`: pathname expansion to the text files; in the test session, `Lea_notizen.txt` from Exercise [5](variablen-befehlsersetzung-und-arithmetik.html#aufg-5) was still there. The seven typed words thus became nine arguments.
:::
:::

:::aufgabe Exercise 10 ★★ A name with a space
<span class="anker" id="aufg-10"></span>

In your practice directory, create a subdirectory `versuch`, change into it and create the file `mein bericht.txt` there. Assign the name to the variable `datei`. (a) Predict what `ls $datei` and `ls "$datei"` report, and check it. (b) You want to create a copy named `sicherung.txt` (German for “backup”). What does `cp $datei sicherung.txt` report, and why? What is the correct line? (c) Assign `X="a b"` and compare `printf "[%s]\n" $X` with `printf "[%s]\n" "$X"`.

:::loesung
```console
$ mkdir versuch
$ cd versuch
$ touch "mein bericht.txt"
$ datei="mein bericht.txt"
$ ls $datei
ls: cannot access 'mein': No such file or directory
ls: cannot access 'bericht.txt': No such file or directory
$ ls "$datei"
'mein bericht.txt'
$ cp $datei sicherung.txt
cp: target 'sicherung.txt': No such file or directory
$ cp "$datei" sicherung.txt
$ ls
'mein bericht.txt'   sicherung.txt
$ X="a   b"
$ printf "[%s]\n" $X
[a]
[b]
$ printf "[%s]\n" "$X"
[a   b]
$ cd ..
```

(a) Without quotes, word splitting breaks the value apart at the space; `ls` looks for `mein` and `bericht.txt`. With quotes, it receives one argument and finds the file. (b) `cp` receives three arguments: `mein`, `bericht.txt` and `sicherung.txt`. With more than two arguments, the last one must be a directory into which the others are copied ([Chapter 3, Section 6.1](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/kopieren-verschieben-loschen.html#stufe-6-1)); there is no directory `sicherung.txt`, so `cp` aborts. The correct line is `cp "$datei" sicherung.txt`. (c) Without quotes, the value falls apart into two words, and the three spaces disappear; with quotes, it stays one word, including all its spaces.
:::
:::

:::aufgabe Exercise 11 ★★ Counting arguments
<span class="anker" id="aufg-11"></span>

The variable `leer` (German for “empty”) has an empty value. How many arguments does `printf` receive in this line, and what are they? Check your answer on the computer.

```console
$ printf "[%s]\n" a"b c"d 'e f'g "" h\ i $leer
```

:::loesung
Four arguments: `ab cd`, `e fg`, an empty one and `h i`.

```console
$ printf "[%s]\n" a"b c"d 'e f'g "" h\ i $leer
[ab cd]
[e fg]
[]
[h i]
```

`a"b c"d` consists of three pieces with no spaces between them, so it is one word; the space within the quotes is part of it. The same goes for `'e f'g`. `""` is an empty but existing argument. In `h\ i`, the space is protected. `$leer` without quotes yields no word at all after word splitting.
:::
:::

:::aufgabe Exercise 12 ★★★ Three surprises
<span class="anker" id="aufg-12"></span>

Explain each of the three results with the order from subsection [3.9](#stufe-3-9), and state how to do it correctly, as far as that is possible with the means of this chapter: (a) After `n=5`, `echo {1..$n}` does not output the numbers 1 to 5. (b) After `muster='*.txt'`, `ls $muster` shows files, whereas `ls "$muster"` shows an error message. (c) After `ordner='~/linuxk5'`, `cd $ordner` fails.

:::loesung
```console
$ n=5
$ echo {1..$n}
{1..5}
$ muster='*.txt'
$ ls $muster
Lea_notizen.txt  einkauf.txt  notiz.txt
$ ls "$muster"
ls: cannot access '*.txt': No such file or directory
$ ordner='~/linuxk5'
$ cd $ordner
bash: cd: ~/linuxk5: No such file or directory
$ ordner=~/linuxk5
$ cd $ordner
$ pwd
/home/student/linuxk5
```

(a) Brace expansion is step 2, parameter expansion is step 3. When the braces were checked, the word still read `{1..$n}`, which is not a valid sequence; after that, `$n` was replaced, but step 2 was already over. This cannot be solved with brace expansion alone: it accepts only limits that stand in the line as numbers, such as `{1..5}`. (b) `muster` contains the text `*.txt`. Without quotes, the result of parameter expansion goes through word splitting and pathname expansion (steps 4 and 5) and turns into file names. With quotes, both steps are left out; `ls` receives the text `*.txt` and looks for a file with this name. (c) The single quotes put a real tilde into the variable. But tilde expansion acts only on typed tildes at the beginning of a word, not on text that an expansion has inserted. The correct way is `ordner=~/linuxk5` without quotes, so that the shell replaces the tilde as early as the assignment, or `ordner="$HOME/linuxk5"`.
:::
:::

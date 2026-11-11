---
title: Regular expressions: repetitions, groups and alternatives
pfad: Computer Science / Linux and the Command Line / Text Tools and Regular Expressions
adresse: informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke
knoten: Chapter 6: Text Tools and Regular Expressions
order: 6110800
summary: A character, a selection, a position: with these, you can write expressions of fixed length.
tags: star, basic form, extended form, quantifier, group, alternative
lang: en
---

<span class="anker" id="stufe-7"></span>

:::zweck
A character, a selection, a position: with these, you can write expressions of fixed length. This section adds repetitions, groups and alternatives, shows the two notations in which they exist and explains three peculiarities: which match wins, why an expression checks only the form and how regular expressions differ from file name patterns.
:::

### Any number of times: the star

<span class="anker" id="stufe-7-1"></span>

Numbers have different numbers of digits, names different numbers of letters. An expression therefore needs a way to say: “any number of these”.

:::definition Definition 7.1 (Star)
<span class="anker" id="satz-7-1"></span>

A __star__ `*` after an ordinary character, a dot or a bracket expression matches any number of repetitions of it in a row, including none at all.
:::

So `a*` matches the empty string, `a`, `aa`, `aaa` and so on. `.*` matches any sequence of characters; it is the usual way to write “and anything in between”.

::::beispiel Repeated characters and anything in between
```console
$ printf '%s\n' b ab aab ac | grep '^a*b$'
b
ab
aab
$ grep 'Anna.*5\.0' laeufe.csv
2026-11-02,Anna,5.0,28
2026-11-09,Anna,5.0,27
```

The first expression requires, from the start to the end, any number of a's and then a b; `b` alone matches with zero a's. The second looks for lines in which `5.0` follows somewhere after `Anna`.
::::

::::beispiel [Counterexample] A star without a hold
```console
$ printf '%s\n' b ab aab ac | grep -c 'a*'
4
```

`a*` matches in every line, even in `b`, because every line contains the empty string, that is, zero a's. An expression that consists of nothing but one element with a star therefore searches for nothing; only anchors or fixed characters next to it give it a hold.
::::

⁠**In short:** `x*` means “any number of x, including none”; `.*` matches any sequence of characters.

### The extended form: grep -E

<span class="anker" id="stufe-7-2"></span>

For “at least one digit” or “exactly three digits”, there are special characters of their own. An attempt without preparation goes wrong, though:

```console
$ grep ',[0-9]{3}$' laeufe.csv
$ echo $?
1
$ grep -E ',[0-9]{3}$' laeufe.csv
2026-11-08,Ben,21.1,128
```

Without an option, `grep` finds nothing; with `-E`, it finds the run of 128 minutes. There are two notations for regular expressions; Figure [22](#abb-22) shows how they read the same text differently.

:::abbildung linux/k6grundform 22
The expression `,[0-9]{3}$` twice. At the top, without an option, `{`, `3` and `}` are three ordinary characters that would have to stand in the line; the comparison with `,128` fails at the curly brace. At the bottom, with `-E`, `{3}` becomes an instruction: the digit before it three times. The three digits `128` light up.
:::

:::definition Definition 7.2 (Basic form, extended form)
<span class="anker" id="satz-7-2"></span>

The __basic form__ of regular expressions is the notation that `grep` uses without an option; it is called “basic regular expressions”, BRE for short. In it, the characters `+ ? { } ( ) |` are ordinary characters. In the __extended form__, called “extended regular expressions”, ERE for short, they are special characters as well; `grep -E` turns it on.
:::

In the basic form, `grep` therefore searched for the text `{3}`, which does not occur in the running log. Everything from Section [6](regulare-ausdrucke-zeichen-klassen-und-anker.html#stufe-6) and the star apply in the same way in both forms.

⁠**In short:** `grep -E` turns on the extended form, in which `+ ? { } ( ) |` are special characters; without `-E`, they are ordinary characters.

### Counting repetitions: +, ? and {n,m}

<span class="anker" id="stufe-7-3"></span>

The star allows any number, including zero. Often, however, what is meant is “at least one”, “perhaps one” or “exactly three”. Figure [23](#abb-23) applies the four possibilities to the same strings.

:::abbildung linux/k6quantor 23
Four expressions, each applied to the strings `b`, `ab`, `aab` and `aaab`, with an anchor at both ends: `a*b` matches all four, `a+b` all except `b`, `a?b` only `b` and `ab`, `a{2,3}b` only `aab` and `aaab`. Matching strings light up, the others stay gray.
:::

:::definition Definition 7.3 (Quantifier)
<span class="anker" id="satz-7-3"></span>

A __quantifier__ stands after an element of an expression and determines how often the element may occur in a row. In the extended form, besides the star, there are: `+` for at least once, `?` for zero times or once, `{n}` for exactly $n$ times, `{n,m}` for $n$ to $m$ times and `{n,}` for at least $n$ times.
:::

::::beispiel Decimal numbers, two-digit distances, a plural
```console
$ grep -Eo '[0-9]+\.[0-9]+' laeufe.csv | paste -s -d' '
5.0 10.5 7.2 6.4 5.0 12.0 8.0 21.1 5.0
$ grep -E ',[0-9]{2}\.' laeufe.csv
2026-11-02,Ben,10.5,62
2026-11-06,Anna,12.0,70
2026-11-08,Ben,21.1,128
$ printf '%s\n' Minute Minuten Minutenzeiger | grep -E '^Minuten?$'
Minute
Minuten
```

`[0-9]+\.[0-9]+` describes digits, a dot and digits again; with `-o`, `grep` cuts exactly the distance out of each line, because nowhere else is there a dot between digits. `,[0-9]{2}\.` finds distances with two digits before the decimal point. In the German words `Minute`, `Minuten` and `Minutenzeiger` (“minute”, “minutes”, “minute hand”), `n?` leaves the n open; the anchors rule out the longer word.
::::

⁠**In short:** `+` at least once, `?` at most once, `{n,m}` between $n$ and $m$ times; plus the star for any number of times.

### Group and alternative

<span class="anker" id="stufe-7-4"></span>

A quantifier acts only on the element directly before it. If a whole piece of a word is to be repeated or left open, or if either one thing or another may stand at a position, you need parentheses and a vertical bar.

:::definition Definition 7.4 (Group, alternative)
<span class="anker" id="satz-7-4"></span>

Parentheses combine part of an expression into a __group__; a quantifier after the group acts on it as a whole. The vertical bar forms an __alternative__: `a|b` matches where `a` matches or where `b` matches. The bar binds more weakly than anything else: it splits the whole expression or the group in which it stands.
:::

`^Anna|Ben` therefore means “Anna at the start of the line or Ben anywhere”; “Anna or Ben at the start of the line” is written `^(Anna|Ben)`.

::::beispiel Two people, two days, two spellings
```console
$ grep -E 'Anna|Clara' laeufe.csv | wc -l
6
$ grep -E '^2026-11-0(2|9),' laeufe.csv
2026-11-02,Anna,5.0,28
2026-11-02,Ben,10.5,62
2026-11-09,Anna,5.0,27
$ echo 'Kilometer km' | grep -oE 'k(ilo)?m(eter)?'
km
```

Six runs by Anna or Clara; the runs of 2 and 9 November. In the third example, the groups make `ilo` and `eter` optional as a whole; the expression matches `km` and `Kilometer` with a lowercase k. Because the word in the text begins with an uppercase K, `-o` cuts out only `km`.
::::

⁠**In short:** `(…)` turns a part into one unit for quantifiers, `a|b` offers a choice; the bar binds most weakly.

### Basic form and extended form compared

<span class="anker" id="stufe-7-5"></span>

Some tools know only one of the two forms, and you come across both in instructions. That is why it is worth taking a close look at how to write the same thing in the basic form.

:::satz Theorem 7.5 (Basic form and extended form)
<span class="anker" id="satz-7-5"></span>

What the extended form expresses with `{ }` and `( )`, the basic form writes with a backslash in front: `\{n,m\}` and `\(…\)`. Whether `\+`, `\?` and `\|` are special characters in the basic form, the standard for Unix shells and their tools leaves to each tool; the GNU tools understand them that way. Conversely, in the extended form, a character such as `+` with a backslash in front is ordinary.
:::

Table [1](#tab-1) compares the notations. Without an option, `grep` uses the basic form.

<span class="anker" id="tab-1"></span>

**Table 1:** The same expressions in the extended form and in the basic form. The dot, bracket expressions, character classes, anchors and the star are the same in both. The GNU tools understand the forms marked (GNU); other tools need not know them.

| Meaning | extended form (`grep -E`) | basic form (`grep`) |
|---|---|---|
| any number of times | `x*` | `x*` |
| at least once | `x+` | `x\+` (GNU) |
| zero times or once | `x?` | `x\?` (GNU) |
| $n$ to $m$ times | `x{n,m}` | `x\{n,m\}` |
| group | `(ab)` | `\(ab\)` |
| alternative | `a\|b` | `a\\|b` (GNU) |
| the character `+` itself | `\+` | `+` |

::::beispiel The same search in the basic form
```console
$ grep ',[0-9]\{3\}$' laeufe.csv
2026-11-08,Ben,21.1,128
$ grep 'Clara\|Ben' laeufe.csv | wc -l
5
```

With backslashes before the curly braces, the basic form finds the run of 128 minutes, and GNU `grep` also understands `\|`: five runs by Clara or Ben.
::::

⁠**In short:** In the basic form, `{ }` and `( )` get a backslash in front, and `\+ \? \|` are an extra of the GNU tools there; when in doubt, write `-E`.

:::hintergrund Why there are two forms
The basic form is the older one. It comes from the editor `ed` and the first `grep`, which did not yet know `+`, `?` and `|` as special characters. When a second program named `egrep` added these characters, old search texts with an ordinary `+` would suddenly have meant something different. So the basic form stayed as it was, and the extended form was added as a second notation. The manual page `regex` in section 7 of the manual ([Chapter 2, Section 4.5](/wissen/en/informatik/linux-und-kommandozeile/die-shell-erste-befehle/hilfe-finden.html#stufe-4-5)) openly calls having two kinds of expressions a botch; but there is no getting rid of it anymore. In GNU `grep`, both forms can do the same things; they differ only in notation. `egrep` is considered obsolete today; since version 3.8, GNU `grep` outputs a warning and recommends `grep -E`.
:::

### The longest match

<span class="anker" id="stufe-7-6"></span>

If an expression matches at several places in a line or to different lengths, the tool has to decide on one match. With `grep` without `-o`, you notice none of this, because it writes the whole line anyway. With `grep -o` and when replacing, it matters. Figure [24](#abb-24) shows the rule with a sentence.

:::abbildung linux/k6gierig 24
The sentence `Anna lief 5 km, Ben lief 10 km` (German for “Anna ran 5 km, Ben ran 10 km”) and the expression `A.*km`. The match begins at the A on the far left. A first arc reaches to the first `km`, a second, longer one to the last; the longer one wins and lights up. Below it, `A[^,]*km`: the comma must not occur, and the arc ends at the first `km`.
:::

:::satz Theorem 7.6 (Longest match)
<span class="anker" id="satz-7-6"></span>

Among all matches of an expression in a line, the one that begins furthest to the left counts. If there are several from this position on, the longest one counts.
:::

::::beispiel Up to the last km
```console
$ echo 'Anna lief 5 km, Ben lief 10 km' | grep -o 'A.*km'
Anna lief 5 km, Ben lief 10 km
$ echo 'Anna lief 5 km, Ben lief 10 km' | grep -o 'A[^,]*km'
Anna lief 5 km
```

`.*` takes as much as it can, and the match reaches to the last `km`. If you only want to go up to the first one, forbid, within the repetition, the character at which it is to stop: `[^,]*` does not run past the comma.
::::

⁠**In short:** The match that begins furthest to the left wins, and from there the longest one; you can limit it with a negated bracket expression.

:::hintergrund Greedy and shortest matches in programming languages
Many programming languages, Python for example, search differently: they try the possibilities of an expression one after another and take the first one that matches; each quantifier takes as much as it can and is therefore called greedy. Usually this gives the same match, but not with an alternative: in the line `ab`, Python finds only `a` with `a|ab`, whereas `grep` finds the longest match:

```console
$ echo ab | grep -oE 'a|ab'
ab
```

These languages also know a notation with a question mark after the quantifier, such as `.*?`, which takes as little as possible. The standard for Unix shells and their tools adopted it for the extended form in 2024, there as the shortest match. GNU `grep` 3.12 on the test system still treats it like the ordinary star:

```console
$ echo 'Anna lief 5 km, Ben lief 10 km' | grep -oE 'A.*?km'
Anna lief 5 km, Ben lief 10 km
```

The negated bracket expression is therefore the way that works everywhere.
:::

### Form, not meaning

<span class="anker" id="stufe-7-7"></span>

An expression for a date seems easy: four digits, hyphen, two digits, hyphen, two digits. Whether it also finds only real dates is shown by an experiment:

```console
$ printf '%s\n' 2026-11-09 2026-13-45 9.11.2026 | grep -E '^[0-9]{4}-[0-9]{2}-[0-9]{2}$'
2026-11-09
2026-13-45
```

The 45th day of the 13th month does not exist, and yet it matches. The German date notation `9.11.2026` (day.month.year) does not match, although it is a real date.

:::satz Theorem 7.7 (Form, not meaning)
<span class="anker" id="satz-7-7"></span>

A regular expression checks only which characters stand in which order. What these characters mean, whether a number is large or small, whether a date exists, it does not know. Every rule about meaning has to be translated, if this is possible at all, into rules about characters.
:::

::::beispiel Pinning down the month more precisely
Months go from 01 to 12. As a rule about characters, this means: a 0 and a digit from 1 to 9, or a 1 and a digit from 0 to 2.

```console
$ printf '%s\n' 2026-11-09 2026-13-45 2026-00-10 | grep -E '^[0-9]{4}-(0[1-9]|1[0-2])-[0-9]{2}$'
2026-11-09
```

Month 13 and month 00 now drop out. The same would work for the days, but the fact that February has only 28 days, 29 in leap years, quickly makes the expression unreadable. If you want to check the meaning, it is better to compare numbers with a tool that can calculate.
::::

Why an expression sees only forms becomes clear when you look at how a tool checks it. Figure [25](#abb-25) shows this for the expression `[0-9]+\.[0-9]+` for decimal numbers from subsection [7.3](#stufe-7-3): a tool such as `grep` can read the line character by character from the left and, while doing so, remember only where in the expression it currently is. Whether it has read “twelve” or “twenty”, it does not remember, only “I am in the number before the dot”.

:::abbildung linux/k6automat 25
The expression `[0-9]+\.[0-9]+` as a small machine with four circles, the states “start”, “in the number”, “after the dot” and “goal”. Arrows carry the characters that lead from one circle to the next: a digit from the start into the number, further digits back around into the same circle, a dot onward, a digit into the goal, further digits in the goal back around into the goal. The string `10.5` travels through character by character; at the 5, the goal is reached. The machine remembers only the circle it is in.
:::

⁠**In short:** A regular expression checks the form of a string, not its meaning; `2026-13-45` has the form of a date.

:::hintergrund Regular expressions and finite automata
In computer science, the machine from Figure [25](#abb-25) is called a finite automaton: a fixed, finite number of states, and one input character after another determines the next state. In the early 1950s, the mathematician Stephen Kleene showed that regular expressions in the mathematical sense, built only from single characters, concatenation, alternative and star, describe exactly the sets of strings that a finite automaton can recognize; the theorem bears his name today. The word “regular” also comes from him. In 1968, Ken Thompson published a method that translates an expression into such an automaton and reads the text only once from left to right, following all possibilities at the same time. Automata of this kind are still the basis of fast search tools such as `grep` today. A limit follows from this: a finite automaton has finitely many states and therefore cannot count arbitrarily far. No regular expression describes the set of all strings made of a number of opening parentheses followed by just as many closing ones. Some extensions of the tools go beyond this limit, such as the requirement that a piece found earlier occurs once more; then the fast methods fail, and the search can become very much slower.
:::

### File name patterns and regular expressions

<span class="anker" id="stufe-7-8"></span>

You know `*`, `?` and square brackets from file name patterns ([Chapter 3, Section 6.6](/wissen/en/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/kopieren-verschieben-loschen.html#stufe-6-6) and [Chapter 5, Section 1.3](/wissen/en/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/expansion-muster-klammern-und-tilde.html#stufe-1-3)). The same characters occur in regular expressions, with a different meaning. If you mix the two up, you search for something other than what you mean.

:::satz Theorem 7.8 (Pattern and regular expression)
<span class="anker" id="satz-7-8"></span>

A file name pattern is evaluated by the shell before a command starts; a regular expression is evaluated by the program, such as `grep`. In the pattern, `*` stands for any sequence of characters and `?` for any single character; in the regular expression, `*` repeats the element before it, `.` stands for any single character, and `?` makes the element before it optional in the extended form. A pattern matches only the whole name, an expression without anchors already matches a piece of the line.
:::

Table [2](#tab-2) translates the most important patterns into regular expressions. The anchors are necessary because a pattern always means the whole name.

<span class="anker" id="tab-2"></span>

**Table 2:** File name patterns and the equivalent regular expressions. A dot is an ordinary character in the pattern; in the expression, it needs a backslash.

| Meaning | file name pattern | regular expression |
|---|---|---|
| any sequence of characters | `*` | `.*` |
| any single character | `?` | `.` |
| one character from a list | `[abc]` | `[abc]` |
| one character not from the list | `[!abc]` | `[^abc]` |
| all names ending in `.csv` | `*.csv` | `^.*\.csv$` |
| `foto` and one character, then `.jpg` | `foto?.jpg` | `^foto.\.jpg$` |

::::beispiel The same name, two readings
```console
$ ls *.csv
drei.csv   kurz.csv    linux.csv  windows.csv
klein.csv  laeufe.csv  neu.csv
$ printf '%s\n' laeufe.csv laeufeXcsv | grep '^laeufe.csv$'
laeufe.csv
laeufeXcsv
$ printf '%s\n' laeufe.csv laeufeXcsv | grep '^laeufe\.csv$'
laeufe.csv
```

In the pattern `*.csv`, the dot is a dot. In the expression, it matches every character, including the X; only `\.` means the dot. If you have solved the exercises in the practice directory, `ls` names further files.
::::

::::beispiel [Counterexample] An expression without quotes
This shows why regular expressions belong in single quotes. For a moment, there is a file `Anna.txt` in the practice directory:

```console
$ touch Anna.txt
$ echo grep -c Ann* laeufe.csv
grep -c Anna.txt laeufe.csv
$ grep -c Ann* laeufe.csv
0
$ grep -c 'Ann*' laeufe.csv
4
$ rm Anna.txt
```

Without quotes, the shell takes `Ann*` for a pattern and replaces it with the matching file name, as `echo` shows. `grep` then searches for `Anna.txt` and finds nothing. With quotes, the expression arrives: `An` and any number of `n`, in four lines. If there were no matching file, the pattern would stay as it is ([Chapter 5, Section 1.5](/wissen/en/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/expansion-muster-klammern-und-tilde.html#stufe-1-5)), and the mistake would not be noticed at all until one day a matching file is in the directory.
::::

⁠**In short:** The shell evaluates patterns against file names, the program evaluates regular expressions against lines; `*`, `?` and the dot mean different things in the two.

### Exercises for Section [7](#stufe-7)

<span class="anker" id="stufe-7-9"></span>

:::aufgabe Exercise 18 ★★ Long runs, large numbers
<span class="anker" id="aufg-18"></span>

(a) Using a quantifier, output all runs that took at least 100 minutes. (b) Output all distances that have two digits before the decimal point, without the other fields of the line.

:::loesung
```console
$ grep -E ',[0-9]{3,}$' laeufe.csv
2026-11-08,Ben,21.1,128
$ cut -d, -f3 laeufe.csv | grep -E '^[0-9]{2}\.'
10.5
12.0
21.1
```

(a) At least three digits between the last comma and the end of the line, that is, at least 100 minutes. (b) `cut` supplies only the distances, one per line; the expression requires exactly two digits at the start of the line and then a dot. Because `grep` outputs whole lines and each line now consists of just one distance, there is no need for `-o`.
:::
:::

:::aufgabe Exercise 19 ★★ Form, not meaning, with addresses
<span class="anker" id="aufg-19"></span>

The addresses of devices in a network from [Chapter 1, Section 3.6](/wissen/en/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/virtuelle-maschinen-der-rechner-im-rechner.html#stufe-3-6) are written as four numbers with dots between them, such as `192.168.178.1`; each of the four numbers lies between 0 and 255. Create a file `adressen.txt` (German for “addresses”) with the lines `192.168.178.1`, `10.0.2.15`, `999.1.1.1`, `1.2.3` and `256.0.0.1`. (a) Which lines does `grep -E '^([0-9]{1,3}\.){3}[0-9]{1,3}$'` find? Explain the expression piece by piece. (b) Which of the lines found are not valid addresses, and why does the expression find them anyway? (c) ★★★ Write an expression that allows only 0 to 255 for each of the four numbers.

:::loesung
```console
$ printf '%s\n' 192.168.178.1 10.0.2.15 999.1.1.1 1.2.3 256.0.0.1 > adressen.txt
$ grep -E '^([0-9]{1,3}\.){3}[0-9]{1,3}$' adressen.txt
192.168.178.1
10.0.2.15
999.1.1.1
256.0.0.1
$ grep -E '^((25[0-5]|2[0-4][0-9]|1?[0-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1?[0-9]?[0-9])$' adressen.txt
192.168.178.1
10.0.2.15
```

(a) The expression reads from the left: start of the line; then three times the group of one to three digits and a dot; then one to three digits once more; then the end of the line. It finds all lines except `1.2.3`, which is missing a number. (b) `999.1.1.1` and `256.0.0.1` have the form of an address, but numbers above 255. The expression checks only “up to three digits” and knows nothing about numeric values: form, not meaning. (c) The rule “0 to 255” has to be translated into rules about digits: `25` and a digit from 0 to 5, or `2`, a digit from 0 to 4 and any digit, or a number with at most three digits whose first digit, if there are three, is a 1; this is what `1?[0-9]?[0-9]` expresses. This group appears four times, three times with a dot. The expression is correct, but hardly readable anymore; for such checks, you are better off with a tool that calculates with numbers.
:::
:::

:::aufgabe Exercise 20 ★★★ The longest match
<span class="anker" id="aufg-20"></span>

Predict what `grep -o` outputs for these inputs, and check it: (a) `'a.*a'` on the line `Anna lief mit Clara` (German for “Anna ran with Clara”); (b) `'n*'` on the same line; (c) `grep -oE '[0-9]+'` on the line `2026-11-02,Anna,5.0,28`.

:::loesung
```console
$ echo 'Anna lief mit Clara' | grep -o 'a.*a'
a lief mit Clara
$ echo 'Anna lief mit Clara' | grep -o 'n*'
nn
$ echo '2026-11-02,Anna,5.0,28' | grep -oE '[0-9]+' | paste -s -d' '
2026 11 02 5 0 28
```

(a) The first lowercase a is at the end of `Anna`, because the uppercase A does not match. From there, the longest match wins, up to the last a in `Clara`. (b) `n*` matches at every position, if need be with zero n's. However, `grep -o` writes only matches that are not empty; the only one is `nn` in `Anna`, where the longest match comprises both n's. (c) After each match, `grep -o` continues searching behind it. Each match is a longest sequence of digits; hyphens, commas and the dot end it. So the line falls apart into six numbers.
:::
:::

:::aufgabe Exercise 21 ★★ Translating
<span class="anker" id="aufg-21"></span>

(a) Translate the patterns `foto?.jpg`, `*.csv` and `[!0-9]*` into regular expressions for `grep` and check them on a file with the lines `foto1.jpg`, `foto10.jpg`, `foto2.png`, `bericht.csv` and `3plan.txt`. (b) Write `grep -E '(Anna|Ben),[0-9]{2}\.'` in the basic form.

:::loesung
```console
$ printf '%s\n' foto1.jpg foto10.jpg foto2.png bericht.csv 3plan.txt > namensliste.txt
$ grep '^foto.\.jpg$' namensliste.txt
foto1.jpg
$ grep '\.csv$' namensliste.txt
bericht.csv
$ grep '^[^0-9]' namensliste.txt
foto1.jpg
foto10.jpg
foto2.png
bericht.csv
$ grep -E '(Anna|Ben),[0-9]{2}\.' laeufe.csv
2026-11-02,Ben,10.5,62
2026-11-06,Anna,12.0,70
2026-11-08,Ben,21.1,128
$ grep '\(Anna\|Ben\),[0-9]\{2\}\.' laeufe.csv
2026-11-02,Ben,10.5,62
2026-11-06,Anna,12.0,70
2026-11-08,Ben,21.1,128
```

(a) `foto?.jpg` becomes `^foto.\.jpg$`: the question mark becomes a dot, the dot of the extension needs a backslash, and the anchors require the whole name; `foto10.jpg` has two characters after `foto` and drops out. `*.csv` becomes `^.*\.csv$`; because `^.*` matches any beginning, `\.csv$` is enough. `[!0-9]*` becomes `^[^0-9]`: a first character that is not a digit; the rest is arbitrary and needs no expression. (b) In the basic form, parentheses, the vertical bar and curly braces get a backslash; `\|` is an extra of the GNU tools. Both forms find the same three runs of at least 10 km by Anna or Ben.
:::
:::

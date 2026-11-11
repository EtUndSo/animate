---
title: Chaining commands
pfad: Computer Science / Linux and the Command Line / Streams, Redirection, Pipes and Exit Status
adresse: informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status
knoten: Chapter 4: Streams, Redirection, Pipes and Exit Status
order: 6090700
summary: With the exit status, the shell can decide whether to continue.
tags: AND list, OR list
lang: en
---

<span class="anker" id="stufe-6"></span>

:::zweck
With the exit status, the shell can decide whether to continue. This section shows how to write several commands in one line: simply one after another, only on success, only on failure or in combination. Finally, it clarifies which exit status a pipeline has in which several processes end.
:::

### One after another: the semicolon

<span class="anker" id="stufe-6-1"></span>

Sometimes you want to send off several commands at once without waiting for the prompt after each one.

:::definition Definition 6.1 (Semicolon)
<span class="anker" id="satz-6-1"></span>

The notation `command1 ; command2` first runs `command1`, waits until it ends and then runs `command2`, regardless of the exit status with which `command1` ended. The exit status of the whole line is that of the last command.
:::

The semicolon therefore acts like the Enter key between two lines. Spaces around the semicolon are allowed but not necessary.

::::beispiel The error in the middle stops nothing
```console
$ echo Start; ls fehlt.txt; echo Ende
Start
ls: cannot access 'fehlt.txt': No such file or directory
Ende
```

Although `ls` failed, the second `echo` runs.
::::

⁠**In short:** The semicolon runs commands one after another without paying attention to whether they succeed.

:::hintergrund Several commands, one redirection
If the output of several commands is to go into the same file, you do not have to redirect each one separately. Curly braces combine them into a group, and a redirection after the group applies to all the commands in it:

```console
$ { echo "Einkauf:"; cat einkauf.txt; } > zettel.txt
$ cat zettel.txt
Einkauf:
Milch
Brot
Äpfel
Kaffee
Butter
```

The shell is strict here: after `{` there must be a space, and the last command before `}` also ends with a semicolon. The exit status of the group is that of its last command.
:::

### Only on success: &&

<span class="anker" id="stufe-6-2"></span>

Often the second step makes sense only if the first one worked: a file should be copied into a directory only if the directory exists; the old list should be replaced only if the sorting worked.

:::definition Definition 6.2 (AND list)
<span class="anker" id="satz-6-2"></span>

The notation `command1 && command2` is an __AND list__: the shell runs `command2` only if `command1` ended with exit status 0. The exit status of the AND list is that of the last command executed.
:::

The name fits: the whole list succeeds only if the first AND the second command succeed. If the first one already fails, the result is settled, and the shell skips the second. If you know Python, you will find the same idea there in `and` ([Python, Chapter 3, Section 1.8](/wissen/en/informatik/programmieren/python/entscheidungen-und-schleifen/bedingungen-vergleiche-und-logische-operatoren.html#stufe-1-8)); in the shell, however, the exit status decides, and 0 counts as success.

::::beispiel First the directory, then the copy
```console
$ mkdir -p archiv && cp einkauf.txt archiv/
$ ls archiv
einkauf.txt
$ cp fehlt.txt archiv/ && echo kopiert
cp: cannot stat 'fehlt.txt': No such file or directory
```

In the first case, `mkdir -p` succeeded, so `cp` ran. In the second, `cp` failed, and the `echo` did not run; `kopiert` (German for “copied”) does not appear.
::::

::::beispiel [Second example] The safe way to sort a file
The solution to the truncation trap from subsection [2.7](ausgaben-umleiten.html#stufe-2-7) becomes safer with `&&`: the original file is replaced only if `sort` succeeded; if it fails, `mv` does not run, and the old list stays intact.

```console
$ cp einkauf.txt probe.txt
$ sort probe.txt > sortiert.txt && mv sortiert.txt probe.txt
$ cat probe.txt
Brot
Butter
Kaffee
Milch
Äpfel
```
::::

⁠**In short:** `command1 && command2` runs the second command only if the first one succeeded.

### Only on failure: ||

<span class="anker" id="stufe-6-3"></span>

You need the counterpart for the case that something goes wrong: then a message should appear or a fallback should take over. Figure [22](#abb-22) shows both operators side by side as railroad switches.

:::abbildung linux/k4weichen 22
Two switches that are set by the exit status of the first command. Left, `&&`: at 0, the way leads to the second command, otherwise past it. Right, `||`: at a nonzero number, the way leads to the second command, at 0 past it.
:::

:::definition Definition 6.3 (OR list)
<span class="anker" id="satz-6-3"></span>

The notation `command1 || command2` is an __OR list__: the shell runs `command2` only if `command1` ended with a nonzero exit status. The exit status of the OR list is that of the last command executed.
:::

Here, too, the name fits: the list succeeds if the first OR the second command succeeds. If the first one already succeeded, the second is no longer needed.

::::beispiel A message when something is missing
```console
$ grep -q Mango obst.txt || echo "Keine Mangos da."
Keine Mangos da.
$ grep -q Kiwi obst.txt || echo "Keine Kiwis da."
```

Mangoes are not on the list, `grep -q` ends with 1, and the message appears (“Keine Mangos da.” is German for “No mangoes here.”). Kiwis are on it, `grep -q` ends with 0, and the shell skips the `echo`.
::::

⁠**In short:** `command1 || command2` runs the second command only if the first one failed.

### && and || in one line

<span class="anker" id="stufe-6-4"></span>

With both operators together, you can write “if …, then …, else …” in one line. This works almost always, but not always, and the borderline case is one of the most common traps in the shell. Figure [23](#abb-23) shows all the paths through such a line.

:::abbildung linux/k4kette 23
The paths through `a && b || c` as a decision tree. If `a` fails, `c` runs. If `a` succeeds, `b` runs; if `b` also succeeds, the line is done. But if `b` fails, `c` runs as well: the path marked in red, which is easy to overlook.
:::

:::satz Theorem 6.4 (Evaluation of && and ||)
<span class="anker" id="satz-6-4"></span>

`&&` and `||` have equal precedence and are evaluated from left to right. `a && b || c` therefore means: first `a && b` as a whole, then `c` if this whole failed. So `c` runs if `a` fails, and also if `a` succeeds and `b` fails.
:::

::::beispiel If, then, else
```console
$ grep -q Apfel obst.txt && echo "Äpfel da." || echo "Keine Äpfel."
Äpfel da.
$ grep -q Mango obst.txt && echo "Mangos da." || echo "Keine Mangos."
Keine Mangos.
```

Here the line behaves like “if, then, else”, because `echo` practically always succeeds.
::::

::::beispiel [Counterexample] When the middle command fails
```console
$ grep -q Apfel obst.txt && cat fehlt.txt || echo "Keine Äpfel."
cat: fehlt.txt: No such file or directory
Keine Äpfel.
```

There are apples, so `cat` ran. It failed, so `grep … && cat …` failed as a whole, and the shell also ran the `echo`. The message “Keine Äpfel.” (German for “No apples.”) is wrong.
::::

⁠**In short:** `a && b || c` is an “if, then, else” only if `b` cannot fail; otherwise `c` also runs after a failed `b`.

### The exit status of a pipeline

<span class="anker" id="stufe-6-5"></span>

In a pipeline, several processes end, and each leaves behind its own exit status. But only one number fits into `$?`. Which one it is determines whether `&&` and `||` do the right thing after a pipeline. Figure [24](#abb-24) shows the answer with an example.

:::abbildung linux/k4pipestatus 24
The pipeline `sort fehlt.txt | head -n 3`: `sort` ends with 2, `head` with 0. Only the 0 of the last command ends up in `$?`; `PIPESTATUS` records both numbers; with `pipefail`, `$?` becomes 2.
:::

:::satz Theorem 6.5 (Exit status of a pipeline)
<span class="anker" id="satz-6-5"></span>

The exit status of a pipeline is the exit status of its last command. If the setting `pipefail` is turned on, it is instead the exit status of the rightmost command that failed, or 0 if all of them succeeded.
:::

Without `pipefail`, errors in earlier stages therefore get lost. So that they are not gone for good, bash remembers the exit status of every stage after each pipeline under the name `PIPESTATUS`. The line `echo "${PIPESTATUS[@]}"` shows the status of each stage, from left to right; for now, take this notation as a fixed recipe. `pipefail` is turned on with `set -o pipefail` and turned off with `set +o pipefail`; the setting applies until the end of the session.

::::beispiel An error that gets lost
```console
$ sort fehlt.txt | head -n 3
sort: cannot read: fehlt.txt: No such file or directory
$ echo $?
0
$ sort fehlt.txt | head -n 3
sort: cannot read: fehlt.txt: No such file or directory
$ echo "${PIPESTATUS[@]}"
2 0
```

The pipeline reports success, although `sort` failed: `head` properly passed on zero lines and ended with 0. `PIPESTATUS` shows both numbers, the 2 from `sort` and the 0 from `head`. With `pipefail`:

```console
$ set -o pipefail
$ sort fehlt.txt | head -n 3
sort: cannot read: fehlt.txt: No such file or directory
$ echo $?
2
$ set +o pipefail
```
::::

::::beispiel [Second example] An abort that is not an error
```console
$ yes | head -n 1
y
$ echo "${PIPESTATUS[@]}"
141 0
```

The command `yes` writes lines containing `y` without end. After `head` had read one line, it ended; when `yes` next tried to write, nobody was reading anymore, and the kernel ended `yes` with interrupt message number 13, which stands for exactly this situation. According to subsection [5.3](der-exit-status.html#stufe-5-3), this gives $128 + 13 = 141$. Figure [25](#abb-25) shows the sequence of events. This was exactly what was wanted: one line.

:::abbildung linux/k4yeshead 25
`yes | head -n 1` as a timeline. `yes` writes lines into the pipe; `head` reads one, prints it and ends with 0. When `yes` next tries to write, nobody reads anymore; the kernel ends `yes` with message 13, and `PIPESTATUS` shows `141 0`.
:::

With `pipefail`, this pipeline would nevertheless have counted as failed.
::::

⁠**In short:** A pipeline has the exit status of its last command; `PIPESTATUS` shows all of them, and `pipefail` makes earlier errors count as well.

:::hintergrund Why only the last command counts
To this day, the standard for Unix shells requires only that the shell wait for the last command of a pipeline; it may wait for the others but does not have to. Consistently, it defines the exit status by the last command, whose result is also the one you see. At first, `pipefail` existed only in individual shells such as the KornShell and bash; in 2024, it was added to the standard. It is not turned on by default anywhere, and the second example shows one reason: an early command aborting because a later one has read enough is commonplace in pipelines and not an error.
:::

### Exercises for Section [6](#stufe-6)

<span class="anker" id="stufe-6-6"></span>

:::aufgabe Exercise 20 ★★ Setting the switches
<span class="anker" id="aufg-20"></span>

Predict for each line what appears, and check it in your practice directory: (a) `grep -q Milch einkauf.txt && echo "Milch steht drauf."` (b) `grep -q Tee einkauf.txt && echo "Tee steht drauf."` (c) `mkdir -p sicherung && cp einkauf.txt sicherung/ && ls sicherung` (d) `ls fehlt.txt 2> /dev/null || echo "fehlt.txt fehlt."` (e) `true || echo eins; false || echo zwei`.

:::loesung
```console
$ grep -q Milch einkauf.txt && echo "Milch steht drauf."
Milch steht drauf.
$ grep -q Tee einkauf.txt && echo "Tee steht drauf."
$ mkdir -p sicherung && cp einkauf.txt sicherung/ && ls sicherung
einkauf.txt
$ ls fehlt.txt 2> /dev/null || echo "fehlt.txt fehlt."
fehlt.txt fehlt.
$ true || echo eins; false || echo zwei
zwei
```

(a) Milk is on the list, `grep -q` ends with 0, and the `echo` runs. (b) Tea is not on it, `grep -q` ends with 1, the `echo` does not run, and nothing appears. (c) Every stage succeeds, so the next one runs: at the end, `ls` shows the copy. (d) `ls` fails, its message disappears into `/dev/null`, and the `echo` after `||` runs. (e) Two OR lists, separated by a semicolon: `true` succeeds, so `echo eins` does not run; `false` fails, so `echo zwei` runs (`eins` and `zwei` are German for “one” and “two”).
:::
:::

:::aufgabe Exercise 21 ★★ Spotting the trap
<span class="anker" id="aufg-21"></span>

Someone writes `cp einkauf.txt /gibtsnicht/ && echo "Kopiert." || echo "Ziel fehlt."` (German for “Copied.” and “Target missing.”) and considers it a safe “if, then, else”. (a) What appears? (b) Is there a case for this line in which both `echo` commands run? (c) Why is the same construction with `grep -q Apfel obst.txt && cat fehlt.txt `| echo "Keine Äpfel."| dangerous?

:::loesung
(a)

```console
$ cp einkauf.txt /gibtsnicht/ && echo "Kopiert." || echo "Ziel fehlt."
cp: cannot create regular file '/gibtsnicht/': Not a directory
Ziel fehlt.
```

`cp` fails, so the first `echo` does not run, but the second one does.

(b) Both run only if `cp` succeeds and `echo "Kopiert."` then fails. In practice, this does not happen, because `echo` fails only if it cannot write, for example because its standard output leads to a full storage device. For this line, the construction is therefore almost safe.

(c) In that line, `cat fehlt.txt` stands in the middle, a command that easily fails. Then the `echo` after `||` runs as well, and the message “Keine Äpfel.” is wrong, although apples are on the list (subsection [6.4](#stufe-6-4)). `a && b || c` is safe only if `b` cannot fail.
:::
:::

:::aufgabe Exercise 22 ★★★ The status of pipelines
<span class="anker" id="aufg-22"></span>

For each pipeline, predict `$?` and `${PIPESTATUS[@]}` and check both; after each run of a pipeline, query only one of them, because the first `echo` overwrites both. (a) `false | true | false` (b) `ls /gibtsnicht | sort | wc -l` (c) `sort obst.txt | grep Mango` (d) as (c), but after `set -o pipefail`; turn the setting off again afterward.

:::loesung
```console
$ false | true | false
$ echo $?
1
$ false | true | false
$ echo "${PIPESTATUS[@]}"
1 0 1
$ ls /gibtsnicht | sort | wc -l
ls: cannot access '/gibtsnicht': No such file or directory
0
$ echo $?
0
$ ls /gibtsnicht | sort | wc -l
ls: cannot access '/gibtsnicht': No such file or directory
0
$ echo "${PIPESTATUS[@]}"
2 0 0
$ sort obst.txt | grep Mango
$ echo $?
1
$ sort obst.txt | grep Mango
$ echo "${PIPESTATUS[@]}"
0 1
$ set -o pipefail
$ sort obst.txt | grep Mango
$ echo $?
1
$ set +o pipefail
```

(a) `$?` is 1, the status of the last `false`; `PIPESTATUS` shows all three. (b) `$?` is 0, because `wc` successfully counted zero lines; `PIPESTATUS` reveals that `ls` failed with 2. (c) `$?` is 1, because the last command, `grep`, found nothing; this time the failure is in the last stage and does not get lost. (d) With `pipefail`, it stays 1: the rightmost command that failed is the last one anyway. `pipefail` changes something only if an earlier stage fails and the last one succeeds, as in (b).
:::
:::

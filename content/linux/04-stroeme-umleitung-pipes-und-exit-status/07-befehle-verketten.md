---
title: Befehle verketten
pfad: Informatik / Linux und Kommandozeile / Ströme, Umleitung, Pipes und Exit-Status
adresse: informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status
knoten: Kapitel 4: Ströme, Umleitung, Pipes und Exit-Status
order: 6090700
summary: Mit dem Exit-Status kann die Shell entscheiden, ob es weitergeht.
tags: UND-Verknüpfung, ODER-Verknüpfung
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Mit dem Exit-Status kann die Shell entscheiden, ob es weitergeht. Dieser Abschnitt zeigt, wie man mehrere Befehle in eine Zeile schreibt: einfach nacheinander, nur bei Erfolg, nur bei Misserfolg oder in Kombination. Zum Schluss klärt er, welchen Exit-Status eine Pipeline hat, in der mehrere Prozesse enden.
:::

### Hintereinander: das Semikolon

<span class="anker" id="stufe-6-1"></span>

Manchmal will man mehrere Befehle auf einmal abschicken, ohne nach jedem auf die Eingabeaufforderung zu warten.

:::definition Definition 6.1 (Semikolon)
<span class="anker" id="satz-6-1"></span>

Die Schreibweise `befehl1 ; befehl2` führt zuerst `befehl1` aus, wartet, bis er endet, und führt dann `befehl2` aus, gleichgültig, mit welchem Exit-Status `befehl1` endete. Der Exit-Status der ganzen Zeile ist der des letzten Befehls.
:::

Das Semikolon wirkt also wie die Eingabetaste zwischen zwei Zeilen. Leerzeichen um das Semikolon sind erlaubt, aber nicht nötig.

::::beispiel Der Fehler in der Mitte hält nichts auf
```console
$ echo Start; ls fehlt.txt; echo Ende
Start
ls: cannot access 'fehlt.txt': No such file or directory
Ende
```

Obwohl `ls` gescheitert ist, läuft das zweite `echo`.
::::

⁠**Kurz gesagt:** Das Semikolon führt Befehle nacheinander aus, ohne auf ihren Erfolg zu achten.

:::hintergrund Mehrere Befehle, eine Umleitung
Sollen die Ausgaben mehrerer Befehle in dieselbe Datei, muss man nicht jeden einzeln umleiten. Geschweifte Klammern fassen sie zu einer Gruppe zusammen, und eine Umleitung hinter der Gruppe gilt für alle darin:

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

Die Shell ist dabei streng: Nach `{` muss ein Leerzeichen stehen, und auch der letzte Befehl vor `}` endet mit einem Semikolon. Der Exit-Status der Gruppe ist der ihres letzten Befehls.
:::

### Nur bei Erfolg: &&

<span class="anker" id="stufe-6-2"></span>

Oft ist der zweite Schritt nur sinnvoll, wenn der erste geklappt hat: Eine Datei soll nur dann in ein Verzeichnis kopiert werden, wenn es das Verzeichnis gibt; die alte Liste soll nur dann ersetzt werden, wenn das Sortieren funktioniert hat.

:::definition Definition 6.2 (UND-Verknüpfung)
<span class="anker" id="satz-6-2"></span>

Die Schreibweise `befehl1 && befehl2` ist eine __UND-Verknüpfung__: Die Shell führt `befehl2` nur aus, wenn `befehl1` mit dem Exit-Status 0 endete. Der Exit-Status der Verknüpfung ist der des zuletzt ausgeführten Befehls.
:::

Der Name passt: Die ganze Verknüpfung hat nur dann Erfolg, wenn der erste UND der zweite Befehl Erfolg haben. Scheitert schon der erste, steht das Ergebnis fest, und die Shell spart sich den zweiten. Wer Python kennt, findet dort dieselbe Idee bei `and` ([Python, Kapitel 3, Abschnitt 1.8](/wissen/informatik/programmieren/python/entscheidungen-und-schleifen/bedingungen-vergleiche-und-logische-operatoren.html#stufe-1-8)); in der Shell entscheidet allerdings der Exit-Status, und 0 zählt als Erfolg.

::::beispiel Erst das Verzeichnis, dann die Kopie
```console
$ mkdir -p archiv && cp einkauf.txt archiv/
$ ls archiv
einkauf.txt
$ cp fehlt.txt archiv/ && echo kopiert
cp: cannot stat 'fehlt.txt': No such file or directory
```

Im ersten Fall gelang `mkdir -p`, also lief `cp`. Im zweiten scheiterte `cp`, und das `echo` lief nicht; `kopiert` erscheint nicht.
::::

::::beispiel [Zweites Beispiel] Die sichere Art, eine Datei zu sortieren
Die Lösung zur Kürzungsfalle aus Unterabschnitt [2.7](ausgaben-umleiten.html#stufe-2-7) wird mit `&&` sicherer: Die Originaldatei wird nur ersetzt, wenn `sort` Erfolg hatte; scheitert es, läuft `mv` nicht, und die alte Liste bleibt unversehrt.

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

⁠**Kurz gesagt:** `befehl1 && befehl2` führt den zweiten Befehl nur aus, wenn der erste Erfolg hatte.

### Nur bei Misserfolg: ||

<span class="anker" id="stufe-6-3"></span>

Das Gegenstück braucht man für den Fall, dass etwas schiefgeht: Dann soll eine Meldung erscheinen oder ein Ersatz geschehen. Abbildung [22](#abb-22) stellt beide Verknüpfungen als Weichen nebeneinander.

:::abbildung linux/k4weichen 22
Zwei Weichen, die nach dem Exit-Status des ersten Befehls stellen. Links `&&`: Bei 0 geht es zum zweiten Befehl, sonst daran vorbei. Rechts `||`: Bei einer Zahl ungleich 0 geht es zum zweiten Befehl, bei 0 daran vorbei.
:::

:::definition Definition 6.3 (ODER-Verknüpfung)
<span class="anker" id="satz-6-3"></span>

Die Schreibweise `befehl1 || befehl2` ist eine __ODER-Verknüpfung__: Die Shell führt `befehl2` nur aus, wenn `befehl1` mit einem Exit-Status ungleich 0 endete. Der Exit-Status der Verknüpfung ist der des zuletzt ausgeführten Befehls.
:::

Auch hier passt der Name: Die Verknüpfung hat Erfolg, wenn der erste ODER der zweite Befehl Erfolg hat. Hatte schon der erste Erfolg, braucht es den zweiten nicht mehr.

::::beispiel Eine Meldung, wenn etwas fehlt
```console
$ grep -q Mango obst.txt || echo "Keine Mangos da."
Keine Mangos da.
$ grep -q Kiwi obst.txt || echo "Keine Kiwis da."
```

Mangos stehen nicht auf der Liste, `grep -q` endet mit 1, und die Meldung erscheint. Kiwis stehen darauf, `grep -q` endet mit 0, und die Shell überspringt das `echo`.
::::

⁠**Kurz gesagt:** `befehl1 || befehl2` führt den zweiten Befehl nur aus, wenn der erste scheiterte.

### && und || in einer Zeile

<span class="anker" id="stufe-6-4"></span>

Mit beiden Verknüpfungen zusammen lässt sich „wenn …, dann …, sonst …“ in eine Zeile schreiben. Das klappt fast immer, aber nicht immer, und der Grenzfall ist eine der häufigsten Fallen der Shell. Abbildung [23](#abb-23) zeigt alle Wege durch eine solche Zeile.

:::abbildung linux/k4kette 23
Die Wege durch `a && b || c` als Entscheidungsbaum. Scheitert `a`, läuft `c`. Gelingt `a`, läuft `b`; gelingt auch `b`, ist Schluss. Scheitert aber `b`, läuft ebenfalls `c`: der rot markierte Weg, den man leicht übersieht.
:::

:::satz Satz 6.4 (Auswertung von && und ||)
<span class="anker" id="satz-6-4"></span>

`&&` und `||` haben denselben Rang und werden von links nach rechts ausgewertet. `a && b || c` bedeutet deshalb: zuerst `a && b` als Ganzes, dann `c`, falls dieses Ganze scheiterte. `c` läuft also, wenn `a` scheitert, und auch, wenn `a` gelingt und `b` scheitert.
:::

::::beispiel Wenn, dann, sonst
```console
$ grep -q Apfel obst.txt && echo "Äpfel da." || echo "Keine Äpfel."
Äpfel da.
$ grep -q Mango obst.txt && echo "Mangos da." || echo "Keine Mangos."
Keine Mangos.
```

Hier verhält sich die Zeile wie „wenn, dann, sonst“, denn `echo` hat praktisch immer Erfolg.
::::

::::beispiel [Gegenbeispiel] Wenn der mittlere Befehl scheitert
```console
$ grep -q Apfel obst.txt && cat fehlt.txt || echo "Keine Äpfel."
cat: fehlt.txt: No such file or directory
Keine Äpfel.
```

Äpfel gibt es, also lief `cat`. Es scheiterte, damit scheiterte `grep … && cat …` als Ganzes, und die Shell führte auch noch das `echo` aus. Die Meldung „Keine Äpfel.“ ist falsch.
::::

⁠**Kurz gesagt:** `a && b || c` ist nur dann ein „wenn, dann, sonst“, wenn `b` nicht scheitern kann; sonst läuft `c` auch nach einem gescheiterten `b`.

### Der Exit-Status einer Pipeline

<span class="anker" id="stufe-6-5"></span>

In einer Pipeline enden mehrere Prozesse, und jeder hinterlässt seinen eigenen Exit-Status. In `$?` passt aber nur eine Zahl. Welche das ist, entscheidet, ob `&&` und `||` hinter einer Pipeline das Richtige tun. Abbildung [24](#abb-24) zeigt die Antwort an einem Beispiel.

:::abbildung linux/k4pipestatus 24
Die Pipeline `sort fehlt.txt | head -n 3`: `sort` endet mit 2, `head` mit 0. In `$?` landet nur die 0 des letzten Befehls; `PIPESTATUS` hält beide Zahlen fest; mit `pipefail` wird `$?` zur 2.
:::

:::satz Satz 6.5 (Exit-Status einer Pipeline)
<span class="anker" id="satz-6-5"></span>

Der Exit-Status einer Pipeline ist der Exit-Status ihres letzten Befehls. Ist die Einstellung `pipefail` eingeschaltet, ist er stattdessen der Exit-Status des am weitesten rechts stehenden Befehls, der gescheitert ist, oder 0, wenn alle Erfolg hatten.
:::

Fehler in früheren Stufen gehen ohne `pipefail` also unter. Damit sie trotzdem nicht verloren sind, merkt sich bash nach jeder Pipeline den Exit-Status jeder Stufe unter dem Namen `PIPESTATUS`. Die Zeile `echo "${PIPESTATUS[@]}"` zeigt den Status jeder Stufe, von links nach rechts; die Schreibweise übernimmt man hier als festes Rezept. Eingeschaltet wird `pipefail` mit `set -o pipefail`, ausgeschaltet mit `set +o pipefail`; die Einstellung gilt bis zum Ende der Sitzung.

::::beispiel Ein Fehler, der untergeht
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

Die Pipeline meldet Erfolg, obwohl `sort` gescheitert ist: `head` hat ordnungsgemäß null Zeilen weitergegeben und mit 0 geendet. `PIPESTATUS` zeigt beide Zahlen, die 2 von `sort` und die 0 von `head`. Mit `pipefail`:

```console
$ set -o pipefail
$ sort fehlt.txt | head -n 3
sort: cannot read: fehlt.txt: No such file or directory
$ echo $?
2
$ set +o pipefail
```
::::

::::beispiel [Zweites Beispiel] Ein Abbruch, der kein Fehler ist
```console
$ yes | head -n 1
y
$ echo "${PIPESTATUS[@]}"
141 0
```

Der Befehl `yes` schreibt ohne Ende Zeilen mit `y`. Nachdem `head` eine Zeile gelesen hatte, endete es; beim nächsten Schreibversuch von `yes` las niemand mehr, und der Kernel beendete `yes` mit der Unterbrechungsnachricht Nummer 13, die genau das meldet. Nach Unterabschnitt [5.3](der-exit-status.html#stufe-5-3) ergibt das $128 + 13 = 141$. Abbildung [25](#abb-25) zeigt den Ablauf. Gewollt war genau das: eine Zeile.

:::abbildung linux/k4yeshead 25
`yes | head -n 1` als Zeitleiste. `yes` schreibt Zeilen in die Pipe, `head` liest eine, schreibt sie aus und endet mit 0. Beim nächsten Schreibversuch von `yes` liest niemand mehr; der Kernel beendet `yes` mit der Nachricht 13, und `PIPESTATUS` zeigt `141 0`.
:::

Mit `pipefail` hätte diese Pipeline trotzdem als gescheitert gegolten.
::::

⁠**Kurz gesagt:** Eine Pipeline hat den Exit-Status ihres letzten Befehls; `PIPESTATUS` zeigt alle, und `pipefail` lässt auch frühere Fehler zählen.

:::hintergrund Warum nur der letzte Befehl zählt
Der Standard für Unix-Shells verlangt bis heute nur, dass die Shell auf den letzten Befehl einer Pipeline wartet; auf die übrigen darf sie warten, muss es aber nicht. Folgerichtig legt er den Exit-Status nach dem letzten Befehl fest, dessen Ergebnis man ja auch sieht. `pipefail` gab es zuerst nur in einzelnen Shells wie der KornShell und bash; 2024 wurde es in den Standard aufgenommen. Eingeschaltet ist es nirgends von selbst, und das zweite Beispiel zeigt einen Grund: Dass ein früher Befehl abbricht, weil ein späterer genug gelesen hat, ist bei Pipelines alltäglich und kein Fehler.
:::

### Aufgaben zu Abschnitt [6](#stufe-6)

<span class="anker" id="stufe-6-6"></span>

:::aufgabe Aufgabe 20 ★★ Weichen stellen
<span class="anker" id="aufg-20"></span>

Sage für jede Zeile voraus, was erscheint, und prüfe es in deinem Übungsverzeichnis: (a) `grep -q Milch einkauf.txt && echo "Milch steht drauf."` (b) `grep -q Tee einkauf.txt && echo "Tee steht drauf."` (c) `mkdir -p sicherung && cp einkauf.txt sicherung/ && ls sicherung` (d) `ls fehlt.txt 2> /dev/null || echo "fehlt.txt fehlt."` (e) `true || echo eins; false || echo zwei`.

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

(a) Milch steht auf der Liste, `grep -q` endet mit 0, das `echo` läuft. (b) Tee steht nicht darauf, `grep -q` endet mit 1, das `echo` läuft nicht, und es erscheint nichts. (c) Jede Stufe gelingt, also läuft die nächste: Am Ende zeigt `ls` die Kopie. (d) `ls` scheitert, seine Meldung verschwindet in `/dev/null`, und das `echo` hinter `||` läuft. (e) Zwei Verknüpfungen, durch ein Semikolon getrennt: `true` gelingt, also läuft `echo eins` nicht; `false` scheitert, also läuft `echo zwei`.
:::
:::

:::aufgabe Aufgabe 21 ★★ Die Falle erkennen
<span class="anker" id="aufg-21"></span>

Jemand schreibt `cp einkauf.txt /gibtsnicht/ && echo "Kopiert." || echo "Ziel fehlt."` und hält das für ein sicheres „wenn, dann, sonst“. (a) Was erscheint? (b) Gibt es für diese Zeile einen Fall, in dem beide `echo` laufen? (c) Warum ist dieselbe Bauweise mit `grep -q Apfel obst.txt && cat fehlt.txt `| echo "Keine Äpfel."| gefährlich?

:::loesung
(a)

```console
$ cp einkauf.txt /gibtsnicht/ && echo "Kopiert." || echo "Ziel fehlt."
cp: cannot create regular file '/gibtsnicht/': Not a directory
Ziel fehlt.
```

`cp` scheitert, also läuft das erste `echo` nicht, wohl aber das zweite.

(b) Beide laufen nur, wenn `cp` gelingt und danach `echo "Kopiert."` scheitert. Das kommt praktisch nicht vor, denn `echo` scheitert nur, wenn es nicht schreiben kann, etwa weil seine Standardausgabe auf einen vollen Datenträger führt. Für diese Zeile ist die Bauweise deshalb fast sicher.

(c) Dort steht in der Mitte `cat fehlt.txt`, ein Befehl, der leicht scheitert. Dann läuft auch das `echo` hinter `||`, und die Meldung „Keine Äpfel.“ ist falsch, obwohl Äpfel auf der Liste stehen (Unterabschnitt [6.4](#stufe-6-4)). Sicher ist `a && b || c` nur, wenn `b` nicht scheitern kann.
:::
:::

:::aufgabe Aufgabe 22 ★★★ Der Status von Pipelines
<span class="anker" id="aufg-22"></span>

Sage für jede Pipeline `$?` und `${PIPESTATUS[@]}` voraus und prüfe beides; frage für jede Pipeline nur eines davon ab, denn das erste `echo` überschreibt beide. (a) `false | true | false` (b) `ls /gibtsnicht | sort | wc -l` (c) `sort obst.txt | grep Mango` (d) wie (c), aber nach `set -o pipefail`; schalte die Einstellung danach wieder aus.

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

(a) `$?` ist 1, der Status des letzten `false`; `PIPESTATUS` zeigt alle drei. (b) `$?` ist 0, denn `wc` hat mit Erfolg null Zeilen gezählt; `PIPESTATUS` verrät, dass `ls` mit 2 gescheitert ist. (c) `$?` ist 1, denn der letzte Befehl `grep` hat nichts gefunden; diesmal steckt der Misserfolg in der letzten Stufe und geht nicht unter. (d) Mit `pipefail` bleibt es bei 1: Der am weitesten rechts stehende gescheiterte Befehl ist ohnehin der letzte. `pipefail` ändert nur etwas, wenn eine frühere Stufe scheitert und die letzte Erfolg hat, wie in (b).
:::
:::

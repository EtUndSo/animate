---
title: Der Exit-Status
pfad: Informatik / Linux und Kommandozeile / Ströme, Umleitung, Pipes und Exit-Status
adresse: informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status
knoten: Kapitel 4: Ströme, Umleitung, Pipes und Exit-Status
order: 6090600
summary: Jeder Befehl endet entweder mit Erfolg oder mit einem Misserfolg, und oft hängt der nächste Schritt davon ab.
tags: Exit-Status
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Jeder Befehl endet entweder mit Erfolg oder mit einem Misserfolg, und oft hängt der nächste Schritt davon ab. Dieser Abschnitt zeigt, wie ein Prozess beim Ende eine Zahl hinterlässt, wie man sie abfragt und was die verschiedenen Zahlen bedeuten.
:::

### Der Exit-Status

<span class="anker" id="stufe-5-1"></span>

Ob ein Befehl geklappt hat, kann man oft an seinen Meldungen ablesen. Für einen Menschen genügt das, für die Shell nicht: Sie soll den nächsten Befehl davon abhängig machen können, ohne Texte zu deuten, die je nach Programm und Sprache anders lauten. Dafür braucht es eine einfache, einheitliche Antwort jedes Prozesses. Abbildung [19](#abb-19) zeigt, woher sie kommt.

:::abbildung linux/k4exitstatus 19
Ein Prozess endet und hinterlässt eine Zahl. Der Kernel gibt sie an die Shell weiter, die auf das Ende gewartet hat; die Shell merkt sich die Zahl, und `echo $?` zeigt sie an.
:::

:::definition Definition 5.1 (Exit-Status)
<span class="anker" id="satz-5-1"></span>

Jeder Prozess hinterlässt, wenn er endet, eine ganze Zahl von 0 bis 255, seinen __Exit-Status__. Die Zahl 0 bedeutet Erfolg, jede andere Zahl einen Misserfolg. Die Shell, die auf das Ende des Prozesses gewartet hat, bekommt die Zahl vom Kernel und merkt sie sich, bis der nächste Befehl endet.
:::

Abfragen kann man den Exit-Status mit der Zeichenfolge `$?`. Die Shell ersetzt `$?` in einer Befehlszeile, bevor sie den Befehl ausführt, durch den Exit-Status des zuletzt beendeten Befehls. `echo $?` schreibt diese Zahl also aus.

::::beispiel Erfolg und Misserfolg von ls
```console
$ ls /usr/bin > /dev/null
$ echo $?
0
$ ls /gibtsnicht
ls: cannot access '/gibtsnicht': No such file or directory
$ echo $?
2
$ echo $?
0
```

Das erste `ls` hatte Erfolg, seine Ausgabe ging nach `/dev/null`. Das zweite scheiterte mit dem Exit-Status 2. Das letzte `echo $?` zeigt 0, denn der zuletzt beendete Befehl war jetzt das vorige `echo`, und das hatte Erfolg. Wer einen Exit-Status braucht, muss ihn also sofort abfragen.
::::

::::beispiel [Zweites Beispiel] true und false
Die eingebauten Befehle `true` und `false` tun nichts, außer mit 0 beziehungsweise 1 zu enden:

```console
$ true
$ echo $?
0
$ false
$ echo $?
1
```
::::

Gibt ein Programm beim Beenden eine größere Zahl als 255 an, bleibt davon nur der Rest bei der Division durch 256. Das lässt sich mit einer zweiten Shell ausprobieren: `bash -c '…'` startet eine weitere bash, die den Text in den Anführungszeichen als Befehlszeile ausführt, und der eingebaute Befehl `exit` beendet sie mit der genannten Zahl.

```console
$ bash -c 'exit 3'
$ echo $?
3
$ bash -c 'exit 300'
$ echo $?
44
```

Aus 300 wird 44, denn $300 = 256 + 44$.

⁠**Kurz gesagt:** Jeder Prozess endet mit einer Zahl von 0 bis 255; 0 heißt Erfolg, und `$?` liefert die Zahl des zuletzt beendeten Befehls.

:::hintergrund Warum ausgerechnet 0 Erfolg bedeutet
Wer an Wahrheitswerte denkt, erwartet vielleicht, dass 1 für „hat geklappt“ steht. Beim Exit-Status ist es umgekehrt, und das hat einen einfachen Grund: Es gibt genau eine Art von Erfolg, aber viele Arten von Misserfolg. Mit der 0 für Erfolg bleiben alle übrigen Zahlen frei, um verschiedene Fehler zu unterscheiden. Dass nur 0 bis 255 möglich sind, liegt am Weg der Zahl. Ein Programm übergibt beim Beenden zwar eine beliebige ganze Zahl an den Kernel, doch unter Linux kommt bei der wartenden Shell nur ihr unterstes Byte an, also acht Bit; das entspricht genau dem Rest bei der Division durch 256. Die wartende Shell erfährt die Zahl über einen Systemaufruf, mit dem ein Prozess auf das Ende eines von ihm gestarteten Prozesses wartet.
:::

### Was die Zahlen ungleich null bedeuten

<span class="anker" id="stufe-5-2"></span>

„Misserfolg“ kann Verschiedenes heißen: Eine Suche hat nichts gefunden, oder die Datei, in der gesucht werden sollte, gibt es gar nicht. Ein Programm, das mehr als eine Art von Misserfolg kennt, kann sie mit verschiedenen Zahlen unterscheiden. Abbildung [20](#abb-20) zeigt das am Suchprogramm `grep`.

:::abbildung linux/k4grepstatus 20
Drei Ausgänge einer Suche mit `grep -q`: Das Wort kommt in der Datei vor, Exit-Status 0; es kommt nicht vor, Exit-Status 1; die Datei fehlt, Exit-Status 2. Nur im dritten Fall gibt es eine Meldung.
:::

:::satz Satz 5.2 (Bedeutung der Zahlen ungleich null)
<span class="anker" id="satz-5-2"></span>

Welche Zahl ungleich null welchen Misserfolg bedeutet, legt jedes Programm selbst fest; die Handbuchseite beschreibt es im Teil EXIT STATUS ([Kapitel 2, Abschnitt 4.3](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/hilfe-finden.html#stufe-4-3)). Viele Programme melden jeden Misserfolg mit 1. Programme, die mehrere Arten unterscheiden, benutzen meist 1 für ein Ergebnis „nein“ oder einen leichten Fehler und 2 für einen schweren Fehler oder einen falschen Aufruf.
:::

Die Option `-q` (für englisch *quiet*, still) sorgt dafür, dass `grep` nichts ausgibt und nur mit seinem Exit-Status antwortet; Fehlermeldungen schreibt es trotzdem.

::::beispiel Gefunden, nicht gefunden, Fehler
```console
$ grep -q Apfel obst.txt
$ echo $?
0
$ grep -q Mango obst.txt
$ echo $?
1
$ grep -q Apfel fehlt.txt
grep: fehlt.txt: No such file or directory
$ echo $?
2
```

`grep` unterscheidet drei Fälle. Die 1 ist dabei kein Fehler im engeren Sinn, sondern die Antwort „kommt nicht vor“; erst die 2 meldet, dass die Suche gar nicht möglich war.
::::

::::beispiel [Zweites Beispiel] cat kennt nur eine Art
```console
$ cat fehlt.txt
cat: fehlt.txt: No such file or directory
$ echo $?
1
```

`cat` meldet jeden Misserfolg mit 1. `ls` endete im vorigen Unterabschnitt mit 2, weil es eine Datei, nach der ausdrücklich gefragt war, nicht gab; kleinere Probleme meldet es mit 1.
::::

⁠**Kurz gesagt:** Die Zahl ungleich null sagt, welcher Misserfolg es war; was sie bedeutet, steht in der Handbuchseite des Programms.

### Die Zahlen der Shell: 126, 127 und 128 + n

<span class="anker" id="stufe-5-3"></span>

Manchmal kommt ein Programm gar nicht dazu, eine Zahl zu hinterlassen: Es gibt den Befehl nicht, die Datei lässt sich nicht ausführen, oder der Prozess wird mitten in der Arbeit abgebrochen. Für diese Fälle setzt die Shell selbst Zahlen ein, die man sich merken sollte. Abbildung [21](#abb-21) ordnet sie auf dem Zahlenstrahl ein.

:::abbildung linux/k4nummern 21
Der Zahlenstrahl des Exit-Status von 0 bis 255: 0 für Erfolg, die kleinen Zahlen für Fehler, die das Programm selbst meldet, 126 und 127 für Befehle, die nicht starten konnten, und ab 129 die Abbrüche durch eine Unterbrechungsnachricht, etwa 130 für Strg+C.
:::

:::definition Definition 5.3 (Exit-Status der Shell)
<span class="anker" id="satz-5-3"></span>

Die Shell setzt in drei Fällen selbst einen Exit-Status:

<ul>

<li>

127, wenn es den Befehl nicht gibt;

</li>

<li>

126, wenn es die Datei zwar gibt, sie sich aber nicht als Programm ausführen lässt;

</li>

<li>

$128 + n$, wenn der Prozess durch die Unterbrechungsnachricht mit der Nummer $n$ beendet wurde.

</li>

</ul>
:::

Jede Art von Unterbrechungsnachricht hat eine Nummer. Die Nachricht, die Strg+C auslöst ([Kapitel 2, Abschnitt 5.4](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/schneller-arbeiten-vervollstandigung-verlauf-tastenkurzel.html#stufe-5-4)), hat die Nummer 2; ein mit Strg+C abgebrochener Prozess hinterlässt also $128 + 2 = 130$.

::::beispiel Nicht gefunden, nicht ausführbar, abgebrochen
```console
$ gibtsnicht
gibtsnicht: command not found
$ echo $?
127
```

Einen Befehl `gibtsnicht` gibt es weder eingebaut noch im Suchpfad. Als Nächstes soll die Shell das Verzeichnis `/etc` ausführen:

```console
$ /etc
bash: /etc: Is a directory
$ echo $?
126
```

`/etc` gibt es, aber ein Verzeichnis ist kein Programm. Zum Schluss wartet `sleep 10` zehn Sekunden; tippe vorher Strg+C:

```console
$ sleep 10
^C
$ echo $?
130
```

Das Terminal zeigt Strg+C als `^C`. `sleep` wurde durch die Nachricht Nummer 2 beendet, also $128 + 2 = 130$.
::::

⁠**Kurz gesagt:** 127 heißt „nicht gefunden“, 126 „nicht ausführbar“, und $128 + n$ heißt „durch die Unterbrechungsnachricht $n$ beendet“, etwa 130 nach Strg+C.

:::hintergrund Warum 128 + n
Der Kernel teilt der wartenden Shell genau mit, wie ein Prozess geendet hat: entweder selbst, mit einer Zahl von 0 bis 255, oder durch eine Unterbrechungsnachricht, mit deren Nummer. Die Shell hat aber nur eine einzige Zahl, die sie in `$?` ablegen kann. Sie bildet deshalb den zweiten Fall auf $128 + n$ ab. Weil Programme für ihre eigenen Fehler fast immer kleine Zahlen benutzen, erkennt man an einem Wert über 128 einen Abbruch von außen. Eindeutig ist das nicht: Ein Programm könnte selbst mit 130 enden. Der Standard für Unix-Shells verlangt nach einem Abbruch nur einen Wert größer als 128. bash nimmt $128 + n$, ebenso die kleinere Shell dash, die Ubuntu unter dem Namen `/bin/sh` bereithält; auf dem Testsystem liefert ein mit Strg+C abgebrochener Befehl in beiden 130. Andere Shells dürfen abweichen: Die KornShell ksh93 nimmt $256 + n$, dort ergibt derselbe Abbruch 258. Auch 126 und 127 sind Zahlen, die die Shell vergibt, wenn das gewünschte Programm gar nicht erst gestartet werden konnte; Programme sollten sie deshalb nicht für eigene Zwecke verwenden.
:::

### Aufgaben zu Abschnitt [5](#stufe-5)

<span class="anker" id="stufe-5-4"></span>

:::aufgabe Aufgabe 18 ★ Den Exit-Status vorhersagen
<span class="anker" id="aufg-18"></span>

Sage für jeden Befehl den Exit-Status voraus und prüfe ihn mit `echo $?`, das du direkt danach tippst: (a) `ls /etc > /dev/null` (b) `cat einkauf.txt gibtsnicht.txt` (c) `grep -q Milch einkauf.txt` (d) `grep -q Tee einkauf.txt` (e) `Ls /etc` (f) `/usr`.

:::loesung
```console
$ ls /etc > /dev/null
$ echo $?
0
$ cat einkauf.txt gibtsnicht.txt
Milch
Brot
Äpfel
Kaffee
Butter
cat: gibtsnicht.txt: No such file or directory
$ echo $?
1
$ grep -q Milch einkauf.txt
$ echo $?
0
$ grep -q Tee einkauf.txt
$ echo $?
1
$ Ls /etc
Ls: command not found
$ echo $?
127
$ /usr
bash: /usr: Is a directory
$ echo $?
126
```

(a) 0, Erfolg. (b) 1: `cat` hat die erste Datei ausgegeben, an der zweiten ist es gescheitert, und ein einziger Misserfolg genügt für einen Exit-Status ungleich 0. (c) 0, gefunden. (d) 1, nicht gefunden. (e) 127, denn `Ls` mit großem L gibt es nicht; Linux unterscheidet Groß- und Kleinschreibung. (f) 126, denn `/usr` gibt es, aber ein Verzeichnis lässt sich nicht ausführen.
:::
:::

:::aufgabe Aufgabe 19 ★★ Zahlen zurückrechnen
<span class="anker" id="aufg-19"></span>

(a) Welchen Exit-Status hinterlassen `bash -c 'exit 256'` und `bash -c 'exit 513'`? Rechne zuerst, prüfe dann. (b) Ein Prozess endete mit 137. Welche Nummer hatte die Unterbrechungsnachricht? (c) In Unterabschnitt [5.1](#stufe-5-1) zeigte das zweite `echo $?` eine 0. Wie hättest du den Exit-Status 2 des gescheiterten `ls` zweimal anzeigen können?

:::loesung
(a) $256 = 1 \cdot 256 + 0$, Rest 0; $513 = 2 \cdot 256 + 1$, Rest 1:

```console
$ bash -c 'exit 256'
$ echo $?
0
$ bash -c 'exit 513'
$ echo $?
1
```

Bemerkenswert ist der erste Fall: `exit 256` meldet Erfolg, obwohl die Zahl nicht 0 ist.

(b) $137 - 128 = 9$. Der Prozess wurde durch die Unterbrechungsnachricht Nummer 9 beendet.

(c) Man muss den Exit-Status abfragen, bevor ein anderer Befehl endet. Beide Vorkommen von `$?` in einer einzigen Zeile ersetzt die Shell, bevor `echo` läuft:

```console
$ ls /gibtsnicht
ls: cannot access '/gibtsnicht': No such file or directory
$ echo $? $?
2 2
```
:::
:::

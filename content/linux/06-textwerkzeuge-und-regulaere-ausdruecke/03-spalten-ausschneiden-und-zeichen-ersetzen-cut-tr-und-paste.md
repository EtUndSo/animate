---
title: Spalten ausschneiden und Zeichen ersetzen: cut, tr und paste
pfad: Informatik / Linux und Kommandozeile / Textwerkzeuge und reguläre Ausdrücke
adresse: informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke
knoten: Kapitel 6: Textwerkzeuge und reguläre Ausdrücke
order: 6110300
summary: Viele Fragen betreffen nur eine Spalte: Wer ist gelaufen, wie weit?
tags: cut, tr, paste
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Viele Fragen betreffen nur eine Spalte: Wer ist gelaufen, wie weit? Dieser Abschnitt zeigt ein Werkzeug, das Spalten herausschneidet, eines, das einzelne Zeichen ersetzt oder löscht, und eines, das Spalten wieder nebeneinanderlegt. Damit lassen sich auch die Windows-Zeilenenden aus Abschnitt [1](textdaten-datensatze-felder-und-zeilenenden.html#stufe-1) entfernen und eine Spalte von Zahlen zusammenzählen.
:::

### Spalten ausschneiden: cut

<span class="anker" id="stufe-2-1"></span>

Um zu sehen, wer gelaufen ist, braucht man nur Feld 2 jeder Zeile. Abbildung [5](#abb-5) zeigt, wie ein Werkzeug eine Spalte aus allen Datensätzen auf einmal schneidet.

:::abbildung linux/k6cut 5
Das Lauftagebuch als Block von Zeilen. `cut -d, -f2` zerlegt jede Zeile an den Kommas in Felder; die Felder Nummer 2 leuchten auf und rücken als schmale Spalte nach rechts heraus: `name`, `Anna`, `Ben`, `Clara` und so weiter. Der Rest jeder Zeile bleibt grau zurück.
:::

:::definition Definition 2.1 (cut)
<span class="anker" id="satz-2-1"></span>

Der Befehl __cut__ schreibt aus jeder Zeile seiner Eingabe nur ausgewählte Teile aus. Mit `-d` und einem Zeichen legt man das Trennzeichen fest, mit `-f` und einer Liste die Felder, die erhalten bleiben. Die Liste besteht aus Nummern und Bereichen, durch Kommas getrennt: `2`, `1,3`, `2-4`, `2-` für „ab Feld 2“. Ohne `-d` ist der Tabulator das Trennzeichen.
:::

`cut` liest die Dateien, die als Argumente genannt sind, sonst seine Standardeingabe; es ist also ein Filter. `-d,` ist die zusammengezogene Form von `-d ,`, wie bei jeder kurzen Option mit Wert ([Kapitel 2, Abschnitt 2.6](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/der-aufbau-einer-befehlszeile.html#stufe-2-6)).

::::beispiel Namen, Datum und Strecke
```console
$ cut -d, -f2 laeufe.csv
name
Anna
Ben
Clara
Anna
Ben
Anna
Clara
Ben
Anna
```

Feld 2 jeder Zeile, auch der Kopfzeile. Mehrere Felder und Bereiche gehen ebenso; `cut` schreibt sie mit dem Trennzeichen dazwischen:

```console
$ cut -d, -f1,3 laeufe.csv | head -n 3
datum,km
2026-11-02,5.0
2026-11-02,10.5
$ cut -d, -f2- laeufe.csv | head -n 2
name,km,minuten
Anna,5.0,28
```
::::

Statt Feldern kann `cut` auch Stellen in der Zeile ausschneiden: `-c` mit einer Liste von Positionen, von links ab 1 gezählt. Das passt zu Werten fester Breite wie dem Datum, bei dem der Tag immer an Stelle 9 und 10 steht:

```console
$ tail -n 3 laeufe.csv | cut -c9-10
07
08
09
```

::::beispiel [Gegenbeispiel] Das vergessene Trennzeichen
Ohne `-d,` sucht `cut` nach Tabulatoren. Eine Zeile, die gar kein Trennzeichen enthält, gibt es unverändert aus:

```console
$ cut -f2 laeufe.csv | head -n 2
datum,name,km,minuten
2026-11-02,Anna,5.0,28
```

Statt der Namen kommen ganze Zeilen heraus, ohne Fehlermeldung. Wer solche Zeilen lieber weglässt, gibt zusätzlich `-s` an.
::::

⁠**Kurz gesagt:** `cut -d, -f2` schneidet aus jeder Zeile das zweite durch Kommas getrennte Feld; `-c` schneidet nach Stellen.

:::hintergrund Stellen sind auf dem Testsystem Bytes
Bei einem Umlaut zeigt sich, was `cut -c` wirklich zählt:

```console
$ echo 'Jürgen,7' | cut -c1-3
Jü
$ echo 'Jürgen,7' | gnucut -c1-3
Jü
```

Gewünscht waren drei Zeichen, `Jür`; geliefert wurden drei Bytes, denn das ü belegt zwei ([Kapitel 3, Abschnitt 4.1](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-ansehen.html#stufe-4-1)). Beide Fassungen auf dem Testsystem, uutils 0.8 und GNU 9.7, zählen so. Die GNU-Fassung zählt erst seit Version 9.11 aus dem Jahr 2026 wirklich Zeichen, bei älteren Fassungen sind Stellen Bytes. Für Texte mit Umlauten schneidet man deshalb sicherer nach Feldern als nach Stellen. Eine zweite Grenze von `cut`: Es schreibt die Felder immer in ihrer ursprünglichen Reihenfolge; `-f3,1` ergibt dasselbe wie `-f1,3`.
:::

### Zeichen ersetzen und löschen: tr

<span class="anker" id="stufe-2-2"></span>

Manchmal stört ein einzelnes Zeichen überall in einer Datei: ein Wagenrücklauf am Ende jeder Zeile, Kommas, wo ein anderes Programm Semikolons erwartet, Kleinbuchstaben, wo Großbuchstaben gewünscht sind. [Kapitel 4, Abschnitt 3.3](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/eingaben-umleiten.html#stufe-3-3) hat `tr` schon benutzt, um Kleinbuchstaben in Großbuchstaben zu verwandeln. Abbildung [6](#abb-6) zeigt, nach welcher Regel es das tut.

:::abbildung linux/k6tr 6
`tr a-z A-Z` als Zuordnung: Oben die Zeichen der ersten Menge `a b c … z` nebeneinander, darunter die der zweiten `A B C … Z`; Pfeile verbinden die Zeichen an gleicher Stelle. Ein Text läuft Zeichen für Zeichen hindurch: Jedes Zeichen, das oben vorkommt, wird durch sein Gegenstück unten ersetzt, Ziffern und Kommas laufen unverändert durch.
:::

:::definition Definition 2.2 (tr)
<span class="anker" id="satz-2-2"></span>

Der Befehl __tr__ liest seine Standardeingabe Zeichen für Zeichen und schreibt sie verändert aus. `tr menge1 menge2` ersetzt jedes Zeichen, das in der ersten Menge an einer bestimmten Stelle steht, durch das Zeichen an derselben Stelle der zweiten Menge. `tr -d menge` löscht alle Zeichen der Menge, `tr -s menge` fasst mehrere gleiche Zeichen der Menge hintereinander zu einem zusammen.
:::

Eine Menge schreibt man als Folge von Zeichen, etwa `',;'`, mit Bereichen wie `a-z` oder mit Namen wie `[:lower:]` für alle Kleinbuchstaben und `[:digit:]` für alle Ziffern. `tr` versteht selbst die Schreibweisen `\n` für das Zeilenende, `\t` für den Tabulator und `\r` für den Wagenrücklauf. Damit die Shell nichts davon verändert, stehen die Mengen in einfachen Anführungszeichen.

::::beispiel Ersetzen, Zusammenfassen, Löschen
```console
$ head -n 2 laeufe.csv | tr ',' ';'
datum;name;km;minuten
2026-11-02;Anna;5.0;28
$ head -n 2 laeufe.csv | tr a-z A-Z
DATUM,NAME,KM,MINUTEN
2026-11-02,ANNA,5.0,28
$ echo 'viel    Platz' | tr -s ' '
viel Platz
$ echo Hallo | tr -d l
Hao
```

Ziffern, Punkte und Bindestriche kommen in keiner Menge vor und bleiben, wie sie sind.
::::

`tr` nimmt keine Dateinamen an; die Datei kommt mit `<` oder über eine Pipe. Ein Dateiname als drittes Argument führt zu einer Meldung:

```console
$ tr a-z A-Z laeufe.csv
tr: extra operand 'laeufe.csv'
Try 'tr --help' for more information.
```

Mit `-d` löst `tr` auch das Problem aus Unterabschnitt [1.4](textdaten-datensatze-felder-und-zeilenenden.html#stufe-1-4): Es löscht jeden Wagenrücklauf aus der Windows-Datei. Das Ergebnis vergleichst du mit `cmp`, das zwei Dateien Byte für Byte vergleicht, bei Gleichheit nichts ausgibt und den Exit-Status 0 meldet:

```console
$ tr -d '\r' < windows.csv > linux.csv
$ cat -A linux.csv
datum,name,km,minuten$
2026-11-02,Anna,5.0,28$
2026-11-02,Ben,10.5,62$
$ cmp linux.csv drei.csv && echo gleich
gleich
```

Die bereinigte Datei `linux.csv` ist Byte für Byte gleich den ersten drei Zeilen des Lauftagebuchs.

⁠**Kurz gesagt:** `tr` ersetzt Zeichen nach zwei Mengen, löscht sie mit `-d` oder fasst Wiederholungen mit `-s` zusammen; `tr -d '\r'` entfernt Windows-Zeilenenden.

:::hintergrund Warum tr keine Umlaute umwandelt
```console
$ echo 'Anna läuft' | tr a-z A-Z
ANNA LäUFT
$ echo 'Anna läuft' | tr '[:lower:]' '[:upper:]'
ANNA LäUFT
```

Das ä bleibt klein, auch mit den Namen der Mengen. `tr` arbeitet auf dem Testsystem Byte für Byte, in der uutils-Fassung ebenso wie in der GNU-Fassung, deren Handbuch das ausdrücklich nennt. Ein ä besteht in UTF-8 aus zwei Bytes, die einzeln keine Buchstaben sind, also findet `tr` darin nichts zum Ersetzen. Für die Ziffern, Kommas und ASCII-Buchstaben, um die es in diesem Kapitel meist geht, spielt das keine Rolle. Die Mengen von `tr` sind übrigens keine Muster wie die für Dateinamen aus [Kapitel 3, Abschnitt 6.6](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/kopieren-verschieben-loschen.html#stufe-6-6): Ein Stern oder ein Fragezeichen steht darin für sich selbst; eine besondere Bedeutung haben nur der Bindestrich zwischen zwei Zeichen, der umgekehrte Schrägstrich wie in `\n` und die Namen in `[:…:]`.
:::

### Spalten zusammenfügen: paste

<span class="anker" id="stufe-2-3"></span>

`cut` zerlegt eine Tabelle in Spalten. Manchmal braucht man den umgekehrten Weg: zwei Listen, die Zeile für Zeile zusammengehören, nebeneinander zu einer Tabelle legen. Abbildung [7](#abb-7) zeigt das.

:::abbildung linux/k6paste 7
Zwei schmale Spalten, links die Namen aus `namen.txt`, rechts die Minuten aus `minuten.txt`. `paste` schiebt sie zusammen: Die erste Zeile links und die erste rechts werden eine Zeile mit einem Tabulator dazwischen, dann die zweiten und so weiter. Darunter `paste -s`: Eine einzige Spalte wird zu einer Zeile umgelegt.
:::

:::definition Definition 2.3 (paste)
<span class="anker" id="satz-2-3"></span>

Der Befehl __paste__ liest mehrere Dateien gleichzeitig und schreibt die erste Zeile jeder Datei nebeneinander in eine Zeile, dann die zweiten Zeilen und so weiter. Zwischen die Teile setzt er einen Tabulator oder mit `-d` ein anderes Zeichen. Mit `-s` legt er stattdessen alle Zeilen einer Datei hintereinander in eine einzige Zeile.
:::

Die beiden Spalten speicherst du zuerst mit `cut` in eigene Dateien:

```console
$ cut -d, -f2 laeufe.csv > namen.txt
$ cut -d, -f4 laeufe.csv > minuten.txt
$ paste namen.txt minuten.txt | head -n 3
name    minuten
Anna    28
Ben     62
$ paste -d, namen.txt minuten.txt | head -n 3
name,minuten
Anna,28
Ben,62
```

Der Tabulator erscheint im Terminal als Sprung zur nächsten Spalte. Mit `-d,` entsteht wieder CSV.

::::beispiel Eine Spalte als eine Zeile
`paste -s` liest seine Standardeingabe, wenn es keinen Dateinamen bekommt:

```console
$ tail -n +2 namen.txt | paste -s -d,
Anna,Ben,Clara,Anna,Ben,Anna,Clara,Ben,Anna
```

Die neun Namen stehen jetzt in einer Zeile, durch Kommas getrennt.
::::

::::beispiel Minuten zusammenzählen
Wie lange war der Lauftreff insgesamt unterwegs? Setzt man zwischen die Minuten ein Pluszeichen, entsteht eine Rechnung, die die Arithmetik der Shell aus [Kapitel 5, Abschnitt 2.4](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/variablen-befehlsersetzung-und-arithmetik.html#stufe-2-4) ausrechnen kann:

```console
$ tail -n +2 minuten.txt | paste -s -d+
28+62+41+35+31+70+44+128+27
$ echo $(( $(tail -n +2 minuten.txt | paste -s -d+) ))
466
```

Die Befehlsersetzung setzt die Rechnung zwischen die doppelten Klammern, und die Shell rechnet. Abbildung [8](#abb-8) zählt die neun Werte Schritt für Schritt zusammen: Zusammen waren es 466 Minuten, 7 Stunden und 46 Minuten. Für Kommazahlen wie die Kilometer taugt dieser Weg nicht, denn die Shell rechnet nur mit ganzen Zahlen.

:::abbildung linux/k6minuten 8
Die Summe der Minuten: $28 + 62 + 41 + 35 + 31 + 70 + 44 + 128 + 27$. Die Zwischensummen laufen von links nach rechts mit: 90, 131, 166, 197, 267, 311, 439 und zuletzt 466.
:::
::::

⁠**Kurz gesagt:** `paste` legt Zeilen mehrerer Dateien nebeneinander, `paste -s` alle Zeilen einer Datei in eine Zeile, mit `-d` als Trennzeichen.

### Aufgaben zu Abschnitt [2](#stufe-2)

<span class="anker" id="stufe-2-4"></span>

:::aufgabe Aufgabe 4 ★ Spalten ausschneiden
<span class="anker" id="aufg-4"></span>

(a) Gib Datum und Minuten aller Läufe ohne Kopfzeile aus. (b) Gib nur den Tag des Monats aller Läufe in einer Zeile aus, einmal mit `cut -c` und einmal nur mit Feldern. (c) Sage voraus, was `cut -d, -f5 laeufe.csv` ausgibt, und prüfe es mit `cat -A`.

:::loesung
```console
$ tail -n +2 laeufe.csv | cut -d, -f1,4 | head -n 3
2026-11-02,28
2026-11-02,62
2026-11-03,41
$ tail -n +2 laeufe.csv | cut -c9-10 | paste -s -d' '
02 02 03 04 05 06 07 08 09
$ tail -n +2 laeufe.csv | cut -d, -f1 | cut -d- -f3 | paste -s -d' '
02 02 03 04 05 06 07 08 09
$ cut -d, -f5 laeufe.csv | head -n 2 | cat -A
$
$
```

(a) `tail -n +2` entfernt die Kopfzeile, `cut -d, -f1,4` behält Datum und Minuten; `head -n 3` kürzt hier nur die Ausgabe, ohne es stehen neun Zeilen da. (b) Der Tag steht im Datum an den Stellen 9 und 10. Ohne Stellen schneidet man zuerst das Datum als Feld 1 aus und zerlegt es dann ein zweites Mal, diesmal am Bindestrich; der Tag ist dort Feld 3. `paste -s -d' '` legt die Tage in eine Zeile. (c) Die Zeilen haben nur vier Felder. Für ein fünftes schreibt `cut` nichts, nur das Zeilenende; `cat -A` zeigt deshalb Zeilen, die nur aus `$` bestehen.
:::
:::

:::aufgabe Aufgabe 5 ★★ Eine Windows-Datei bereinigen
<span class="anker" id="aufg-5"></span>

Bereinige `gruss.txt` aus Aufgabe [2](textdaten-datensatze-felder-und-zeilenenden.html#aufg-2). (a) Schreibe das Ergebnis nach `gruss_linux.txt` und prüfe es mit `wc -c` und `cat -A`. (b) Warum darfst du nicht `tr -d '\r' < gruss.txt > gruss.txt` schreiben? Probiere es an einer Kopie. (c) Wie bekommst du die bereinigte Fassung trotzdem unter dem alten Namen?

:::loesung
```console
$ tr -d '\r' < gruss.txt > gruss_linux.txt
$ wc -c gruss_linux.txt
11 gruss_linux.txt
$ cat -A gruss_linux.txt
Hallo$
Welt$
```

(a) Zwei Wagenrückläufe weniger, also $13 - 2 = 11$ Bytes, und `cat -A` zeigt kein `^M` mehr. (b) Das ist die Kürzungsfalle aus [Kapitel 4, Abschnitt 2.7](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/ausgaben-umleiten.html#stufe-2-7): Die Shell leert die Datei für die Umleitung, bevor `tr` startet, und `tr` liest dann eine leere Datei.

```console
$ cp gruss.txt kopie.txt
$ tr -d '\r' < kopie.txt > kopie.txt
$ wc -c kopie.txt
0 kopie.txt
$ tr -d '\r' < gruss.txt > zwischen.txt && mv zwischen.txt gruss.txt
$ cat -A gruss.txt
Hallo$
Welt$
```

(c) Man schreibt in eine Zwischendatei und benennt sie danach um. Das `&&` sorgt dafür, dass `mv` nur läuft, wenn `tr` Erfolg hatte; sonst bliebe die alte Datei unangetastet.
:::
:::

:::aufgabe Aufgabe 6 ★★ Die Tabelle neu zusammensetzen
<span class="anker" id="aufg-6"></span>

Du möchtest eine CSV-Datei mit den Spalten Strecke und Name, in dieser Reihenfolge. (a) Warum gelingt das nicht mit `cut -d, -f3,2 laeufe.csv`? (b) Baue sie mit `cut` und `paste`.

:::loesung
```console
$ cut -d, -f3,2 laeufe.csv | head -n 2
name,km
Anna,5.0
$ cut -d, -f3 laeufe.csv > km.txt
$ paste -d, km.txt namen.txt | head -n 3
km,name
5.0,Anna
10.5,Ben
```

(a) `cut` schreibt die gewählten Felder immer in der Reihenfolge, in der sie in der Zeile stehen; `3,2` ist für `cut` dieselbe Auswahl wie `2,3`. (b) Erst die Strecken in eine eigene Datei, dann mit `paste` in der gewünschten Reihenfolge nebeneinander, `km.txt` zuerst. `namen.txt` stammt aus Unterabschnitt [2.3](#stufe-2-3).
:::
:::

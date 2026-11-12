---
title: Wie der Kernel Rechte prüft
pfad: Informatik / Linux und Kommandozeile / Benutzer, Gruppen und Rechte
adresse: informatik/linux-und-kommandozeile/benutzer-gruppen-und-rechte
knoten: Kapitel 7: Benutzer, Gruppen und Rechte
order: 6120600
summary: Jetzt kennst du alle Teile: die Nummern eines Prozesses, Besitzer und Gruppe einer Datei, die neun Rechte an Dateien und Verzeichnissen.
tags: 
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Jetzt kennst du alle Teile: die Nummern eines Prozesses, Besitzer und Gruppe einer Datei, die neun Rechte an Dateien und Verzeichnissen. Dieser Abschnitt setzt sie zu dem Verfahren zusammen, mit dem der Kernel jeden Zugriff entscheidet, und zeigt zwei Folgen, die viele überraschen.
:::

### Der Weg durch den Pfad

<span class="anker" id="stufe-5-1"></span>

Um eine Datei zu öffnen, gibt ein Programm dem Kernel einen Pfad wie `weg/innen/zettel.txt`. Der Kernel geht diesen Pfad Verzeichnis für Verzeichnis entlang und schlägt in jeder Tabelle den nächsten Namen nach. Für jeden dieser Schritte braucht der Prozess das Recht aus Unterabschnitt [4.2](rechte-bei-verzeichnissen.html#stufe-4-2).

:::satz Satz 5.1 (Suchrecht auf dem Pfad)
<span class="anker" id="satz-5-1"></span>

Um auf eine Datei zuzugreifen, braucht ein Prozess an jedem Verzeichnis auf ihrem Pfad das Ausführungsrecht. Fehlt es an einem einzigen Verzeichnis, scheitert der Zugriff, ganz gleich, welche Rechte die Datei selbst hat.
:::

Abbildung [13](#abb-13) zeigt den Gang durch einen Pfad mit einer verschlossenen Tür.

:::abbildung linux/k7pfad 13
Der Pfad `weg/innen/zettel.txt` als Kette von Kästen: `linuxk7` (rwx), `weg` (`rw-`), `innen` (rwx), `zettel.txt` (`rw-r--r--`). Ein Punkt wandert von links nach rechts; an jedem Verzeichnis wird das x geprüft. Bei `linuxk7` leuchtet es grün, bei `weg` rot, und der Punkt bleibt stehen; die beiden Kästen dahinter bleiben grau, obwohl ihre Rechte ausreichen würden.
:::

```console
$ mkdir -p weg/innen
$ echo Hallo > weg/innen/zettel.txt
$ chmod 600 weg
$ ls -ld weg
drw------- 3 student student 4096 Nov 10 12:32 weg
$ cat weg/innen/zettel.txt
cat: weg/innen/zettel.txt: Permission denied
$ chmod 755 weg
$ cat weg/innen/zettel.txt
Hallo
```

`innen` und `zettel.txt` hatten die ganze Zeit gewöhnliche Rechte. Erst als `weg` sein Ausführungsrecht zurückbekam, kam `cat` durch. Dasselbe gilt für alle Benutzer: Wer in dein Heimatverzeichnis nicht hineinkommt, kommt auch an keine Datei darin, egal wie freizügig ihre Rechte sind.

⁠**Kurz gesagt:** Jedes Verzeichnis auf dem Pfad braucht das Ausführungsrecht; ein einziges fehlendes versperrt den Weg.

### Die erste passende Klasse

<span class="anker" id="stufe-5-2"></span>

Am Ende des Pfads steht die Datei selbst. Der Kernel muss nun entscheiden, welche der neun Rechte für den Prozess gelten. Die Antwort ist ein festes Verfahren mit vier Schritten, das Abbildung [14](#abb-14) als Entscheidungsbaum zeigt.

:::abbildung linux/k7entscheidung 14
Ein Entscheidungsbaum von oben nach unten. Erste Frage: Ist die Benutzernummer des Prozesses 0? Ja → erlaubt (beim Starten nur, wenn ein x gesetzt ist). Nein → zweite Frage: Ist sie die des Besitzers? Ja → nur die drei u-Bits zählen. Nein → dritte Frage: Ist die Gruppe der Datei eine Gruppe des Prozesses? Ja → nur die g-Bits. Nein → die o-Bits. Am Ende leuchtet der Weg für `student` und die Datei `----r--r--` auf: zweite Frage ja, u-Bits `---`, verboten, obwohl g und o lesen dürften.
:::

:::satz Satz 5.2 (Rechteprüfung)
<span class="anker" id="satz-5-2"></span>

Will ein Prozess eine Datei lesen, schreiben oder ausführen, entscheidet der Kernel so:

<ol>

<li>

Hat der Prozess die Benutzernummer 0, ist der Zugriff erlaubt. Ausführen darf er eine gewöhnliche Datei aber nur, wenn mindestens eines ihrer drei x-Bits gesetzt ist.

</li>

<li>

Sonst: Ist die Benutzernummer des Prozesses die des Besitzers, gelten nur die drei Bits der Klasse Besitzer.

</li>

<li>

Sonst: Ist die Gruppe der Datei die Hauptgruppe oder eine Zusatzgruppe des Prozesses, gelten nur die drei Bits der Klasse Gruppe.

</li>

<li>

Sonst gelten die drei Bits der Klasse andere.

</li>

</ol>

Der Zugriff ist erlaubt, wenn in den geltenden drei Bits jedes verlangte Recht gesetzt ist. Die anderen sechs Bits schaut der Kernel nicht an.
:::

Daraus folgt etwas, das man leicht falsch erwartet: Es gilt die erste Klasse, auf die der Prozess passt, nicht die großzügigste.

::::beispiel Der Besitzer, der nicht lesen darf
Gib der Einkaufsliste `----r--r--`, also 044: Besitzer nichts, Gruppe und andere lesen.

```console
$ chmod 044 einkauf.txt
$ ls -l einkauf.txt
----r--r-- 1 student student 25 Nov 10 12:32 einkauf.txt
$ cat einkauf.txt
cat: einkauf.txt: Permission denied
$ chmod 644 einkauf.txt
$ head -n 1 einkauf.txt
Milch
```

`student` ist Besitzer, also zählen nur die drei u-Bits, und die sind `---`. Dass `student` auch in der Gruppe `student` ist und dass alle anderen lesen dürften, fragt der Kernel gar nicht mehr. Die Rechte zurücksetzen konnte `student` trotzdem, denn `chmod` darf der Besitzer immer, unabhängig von den neun Bits.
::::

⁠**Kurz gesagt:** Der Kernel prüft root, dann Besitzer, dann Gruppe, dann andere, und nimmt die Bits der ersten passenden Klasse, nicht die großzügigsten.

:::hintergrund Wozu die erste passende Klasse nützlich ist
Die Regel wirkt zuerst wie eine Falle, sie hat aber einen Nutzen: Man kann einer Gruppe gezielt weniger erlauben als allen anderen. Eine Datei mit 604 dürfen alle lesen, nur die Mitglieder ihrer Gruppe nicht, und der Besitzer darf lesen und schreiben. Würde der Kernel die großzügigste Klasse nehmen, ließe sich so etwas nicht ausdrücken. Außerdem ist die Regel schnell: Der Kernel vergleicht höchstens zwei Nummern und eine kurze Liste von Gruppen, dann weiß er, welche drei Bits gelten. Die Regel selbst ist in der Beschreibung der Pfadauflösung des Linux-Kernels festgelegt; die beiden Begründungen hier sind eine eigene Herleitung.
:::

### Geprüft wird beim Öffnen

<span class="anker" id="stufe-5-3"></span>

Ein Programm liest eine Datei nicht in einem Zug, sondern öffnet sie, liest Stück für Stück und schließt sie wieder. Bleibt die Frage, wann der Kernel die Rechte prüft: einmal oder bei jedem Stück?

:::satz Satz 5.3 (Prüfung beim Öffnen)
<span class="anker" id="satz-5-3"></span>

Der Kernel prüft die Rechte an einer Datei, wenn ein Prozess sie öffnet. Danach liest oder schreibt der Prozess über seinen Dateideskriptor, und der Kernel prüft dabei nur noch, ob der Deskriptor zum Lesen oder Schreiben geöffnet wurde. Ändert jemand die Rechte, nachdem die Datei geöffnet ist, gilt das erst für das nächste Öffnen.
:::

Abbildung [15](#abb-15) stellt die beiden Zeitpunkte nebeneinander.

:::abbildung linux/k7oeffnen 15
Eine Zeitachse von links nach rechts. Links öffnet `tail -f` die Datei `tagebuch.txt`; an diesem Zeitpunkt prüft der Kernel `r` (grünes Häkchen) und gibt einen Deskriptor aus, dargestellt als Eintrittskarte. In der Mitte ändert ein zweites Terminal die Rechte auf `-w-------`. Danach liest `tail` mit seiner Karte weiter, ohne erneute Prüfung, und die neue Zeile erscheint. Rechts versucht `cat`, die Datei neu zu öffnen; die Prüfung schlägt fehl (rotes Kreuz).
:::

Ausprobieren lässt sich das mit `tail -f` aus [Kapitel 6, Abschnitt 1.6](/wissen/informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke/textdaten-datensatze-felder-und-zeilenenden.html#stufe-1-6) und einem zweiten Terminal. Lege zuerst ein kleines Lauftagebuch an:

```console
$ echo "Montag: 5 km" > tagebuch.txt
```

Starte im ersten Terminal `tail -f tagebuch.txt`. Öffne ein zweites Terminal, wechsle mit `cd ~/linuxk7` ins Übungsverzeichnis und nimm dir dort selbst das Leserecht; das Schreibrecht behältst du:

```console
$ chmod 200 tagebuch.txt
$ echo "Dienstag: 7 km" >> tagebuch.txt
$ cat tagebuch.txt
cat: tagebuch.txt: Permission denied
```

Im ersten Terminal ist die neue Zeile trotzdem erschienen. Beende `tail` dort mit Strg+C:

```console
$ tail -f tagebuch.txt
Montag: 5 km
Dienstag: 7 km
^C
```

`cat` musste die Datei neu öffnen und wurde abgewiesen. `tail` hatte sie geöffnet, als das Leserecht noch da war, und las mit seinem Deskriptor einfach weiter. Gib der Datei ihre Rechte zurück:

```console
$ ls -l tagebuch.txt
--w------- 1 student student 28 Nov 10 12:33 tagebuch.txt
$ chmod 644 tagebuch.txt
$ cat tagebuch.txt
Montag: 5 km
Dienstag: 7 km
```

⁠**Kurz gesagt:** Die Rechte zählen im Augenblick des Öffnens; ein offener Deskriptor behält seinen Zugriff, auch wenn die Rechte danach entzogen werden.

:::hintergrund Warum nur beim Öffnen geprüft wird
Lesen und Schreiben geschehen ständig, oft tausendfach je Sekunde. Bei jedem Zugriff den Pfad, den Besitzer und die Klassen erneut zu prüfen, würde den Rechner spürbar bremsen. Deshalb prüft der Kernel einmal beim Öffnen und hält das Ergebnis im Deskriptor fest, der wie eine Eintrittskarte wirkt: Wer sie hat, kommt hinein, ohne erneut kontrolliert zu werden. Das hat eine Kehrseite. Der Grundsatz der lückenlosen Prüfung verlangt, jeden Zugriff jedes Mal zu prüfen ([Cybersecurity, Kapitel 1, Abschnitt 5.5](/wissen/informatik/cybersecurity/sicherheit-schutzziele-und-spielregeln/sicherheitsprinzipien-rechte-vergeben-und-prufen.html#stufe-5-5)). Linux erfüllt ihn nur beim Öffnen. Wer einem Programm Rechte entzieht, das die Datei schon offen hat, muss das Programm beenden, damit der Entzug wirklich greift.

Dass sich kein Programm an der Prüfung vorbeimogeln kann, hat einen einfachen Grund: Ein Programm im Benutzermodus kommt an Dateien nur über einen Systemaufruf, und dessen Einsprungstelle legt der Kernel fest ([Kapitel 1, Abschnitt 1.4](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/betriebssystem-kernel-und-distribution.html#stufe-1-4)). Die Prüfung sitzt im Kernel an dieser einzigen Tür.
:::

:::hintergrund Mehr als neun Bits: Zugriffslisten
Für Fälle, die drei Klassen nicht ausdrücken können, kennt Linux eine Erweiterung: Zugriffslisten, englisch „access control lists“, kurz ACL. Sie hängen an eine Datei zusätzliche Einträge für einzelne Benutzer oder Gruppen. Der Befehl `getfacl` zeigt die Liste einer Datei; ohne Erweiterung enthält sie genau die drei Klassen:

```console
$ getfacl einkauf.txt
```

```text
# file: einkauf.txt
# owner: student
# group: student
user::rw-
group::r--
other::r--
```

`user::`, `group::` und `other::` sind die bekannten Klassen. Mit dem Befehl `setfacl` könnte man Zeilen wie `user:anna:rw-` hinzufügen; `ls -l` zeigt dann ein `+` hinter den neun Zeichen. Die meisten Systeme kommen ohne solche Listen aus, und dieses Kapitel benutzt sie nicht weiter.
:::

### Aufgaben zu Abschnitt [5](#stufe-5)

<span class="anker" id="stufe-5-4"></span>

:::aufgabe Aufgabe 10 ★★ Die erste passende Klasse
<span class="anker" id="aufg-10"></span>

(a) Gib `probe.txt` die Rechte 044. Kannst du die Datei lesen? Kannst du ihre Rechte zurücksetzen? Begründe beides mit dem Satz zur Rechteprüfung. (b) Gib ihr 404. Wer darf jetzt lesen? (c) Gib ihr 640 zurück.

:::loesung
```console
$ chmod 044 probe.txt
$ cat probe.txt
cat: probe.txt: Permission denied
$ chmod 404 probe.txt
$ cat probe.txt
$ ls -l probe.txt
-r-----r-- 1 student student 0 Nov 10 12:52 probe.txt
$ chmod 640 probe.txt
```

(a) `student` ist Besitzer, also zählen nur die u-Bits `---`; dass Gruppe und andere lesen dürften, spielt keine Rolle. Die Rechte zurücksetzen darf er trotzdem, denn `chmod` darf der Besitzer immer, unabhängig von den neun Bits. (b) Mit 404 liest der Besitzer wieder (`cat` meldet keinen Fehler; die Datei ist nur leer), die Mitglieder der Gruppe `student` außer ihm dürfen nichts, alle anderen dürfen lesen. (c) `chmod 640` stellt den Ausgangszustand her.
:::
:::

:::aufgabe Aufgabe 11 ★★ Wer darf lesen?
<span class="anker" id="aufg-11"></span>

Die Datei `plan.txt` gehört `anna` und der Gruppe `kochclub`. `ben` ist Mitglied von `kochclub`, `clara` nicht. Alle Verzeichnisse auf dem Pfad erlauben allen das Durchgehen. Wer von `anna`, `ben` und `clara` darf die Datei lesen, wenn sie die Rechte (a) 640, (b) 604, (c) 064, (d) 400 hat?

:::loesung
Der Kernel bestimmt für jeden zuerst die Klasse und schaut dann nur deren drei Bits an. `anna` ist Besitzerin, `ben` gehört zur Klasse Gruppe, `clara` zur Klasse andere.

<ul>

<li>

(a) 640 = `rw-r-----`: `anna` und `ben` dürfen lesen, `clara` nicht.

</li>

<li>

(b) 604 = `rw----r--`: `anna` und `clara` dürfen lesen, `ben` nicht, obwohl er zur Gruppe gehört.

</li>

<li>

(c) 064 = `---rw-r--`: `ben` und `clara` dürfen lesen, ausgerechnet die Besitzerin `anna` nicht. Sie könnte sich die Rechte aber mit `chmod` zurückgeben.

</li>

<li>

(d) 400 = `r--------`: nur `anna` darf lesen.

</li>

</ul>
:::
:::

:::aufgabe Aufgabe 12 ★★★ Alle Rechte auf einem Pfad
<span class="anker" id="aufg-12"></span>

Welche Rechte braucht `student` an welchen Verzeichnissen und Dateien, um (a) `/home/student/linuxk7/fach/neu.txt` zu lesen, (b) diese Datei zu löschen, (c) eine neue Datei `/home/student/linuxk7/fach/zwei.txt` anzulegen? Nenne für jedes Verzeichnis ab `/` das nötige Recht.

:::loesung
(a) Zum Lesen braucht `student` das Ausführungsrecht an jedem Verzeichnis auf dem Pfad, also an `/`, `/home`, `/home/student`, `/home/student/linuxk7` und `/home/student/linuxk7/fach`, und das Leserecht an `neu.txt` selbst. An `/` und `/home`, die root gehören, gilt für ihn die Klasse andere; beide haben dort `r-x`. (b) Zum Löschen braucht er das Ausführungsrecht an denselben fünf Verzeichnissen und zusätzlich das Schreibrecht an `fach`; an `neu.txt` selbst braucht er kein Recht. (c) Zum Anlegen von `zwei.txt` gilt dasselbe wie in (b): Ausführungsrecht auf dem ganzen Pfad, Schreibrecht an `fach`.
:::
:::

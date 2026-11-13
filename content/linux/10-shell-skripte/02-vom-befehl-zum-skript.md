---
title: Vom Befehl zum Skript
pfad: Informatik / Linux und Kommandozeile / Shell-Skripte
adresse: informatik/linux-und-kommandozeile/shell-skripte
knoten: Kapitel 10: Shell-Skripte
order: 6150200
summary: Dieser Abschnitt zeigt, wie man Befehle in eine Datei schreibt und die Shell diese Datei abarbeiten lässt.
tags: Shell-Skript, Interpreter, Kommentar, Shebang-Zeile
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Dieser Abschnitt zeigt, wie man Befehle in eine Datei schreibt und die Shell diese Datei abarbeiten lässt. Er erklärt, in welchem Prozess das geschieht, woran der Kernel erkennt, welches Programm eine solche Datei ausführt, und warum eine unter Windows bearbeitete Datei daran scheitern kann.
:::

:::::vorwissen Was du dafür brauchst: Editor, Ausführungsrecht und Kindprozess

<span class="anker" id="stufe-1-1"></span>

Dieses Kapitel setzt die [Kapitel 4](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/stroeme-umleitung-pipes-und-exit-status.html) bis 8 voraus und bündelt vieles daraus. Für den Anfang brauchst du vor allem diese Dinge.

<ul>

<li>

Mit dem Texteditor `nano` legst du eine Textdatei an oder änderst sie: `nano datei` öffnet sie, Strg+O speichert, Strg+X beendet den Editor ([Kapitel 3, Abschnitt 5.3](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-und-verzeichnisse-anlegen.html#stufe-5-3)).

</li>

<li>

Jeder Befehl endet mit einem Exit-Status, einer Zahl von 0 bis 255; 0 heißt Erfolg. Die Shell legt ihn in `$?` ab ([Kapitel 4, Abschnitt 5.1](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/der-exit-status.html#stufe-5-1)).

</li>

<li>

Eine Datei darf nur dann als Programm gestartet werden, wenn ihr Ausführungsrecht `x` gesetzt ist; `chmod +x datei` setzt es ([Kapitel 7, Abschnitte 2.3](/wissen/informatik/linux-und-kommandozeile/benutzer-gruppen-und-rechte/die-rechte-einer-datei.html#stufe-2-3) und [9.1](/wissen/informatik/linux-und-kommandozeile/benutzer-gruppen-und-rechte/programme-ausfuhren-und-besondere-rechte.html#stufe-9-1)). Ein Programm im Arbeitsverzeichnis startet man mit `./programm`, weil die Shell das Arbeitsverzeichnis nicht nach Programmen durchsucht ([Kapitel 5, Abschnitt 5.4](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/wie-die-shell-programme-findet-path.html#stufe-5-4)).

</li>

<li>

Ein Prozess, den ein anderer Prozess startet, heißt Kindprozess. Er bekommt eine Kopie von Umgebung und Arbeitsverzeichnis seines Elternprozesses und kann beim Elternprozess nichts zurückändern ([Kapitel 5, Abschnitte 4.2](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/umgebung-und-vererbung.html#stufe-4-2) und [4.5](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/umgebung-und-vererbung.html#stufe-4-5)).

</li>

<li>

`bash -c 'befehle'` startet eine neue bash als Kindprozess, die die Befehle in den Anführungszeichen ausführt ([Kapitel 5, Abschnitt 4.1](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/umgebung-und-vererbung.html#stufe-4-1)).

</li>

</ul>

⁠**Kurz gesagt:** Du brauchst `nano`, den Exit-Status, das Ausführungsrecht samt `./programm` und die Regel, dass ein Kindprozess nur eine Kopie bekommt.

:::warnung Nur im eigenen Übungsverzeichnis
Skripte führen Befehle selbstständig aus, auch Befehle, die Dateien löschen. Alle Übungen dieses Kapitels arbeiten deshalb in einem eigenen Übungsverzeichnis mit eigenen Testdateien. Lege es jetzt an, wechsle hinein und lege zwei kleine Einkaufslisten an:

```console
$ mkdir ~/linuxk10
$ cd ~/linuxk10
$ printf '%s\n' Milch Brot Äpfel Kaffee > einkauf.txt
$ printf '%s\n' Tomaten Nudeln Basilikum > "mein einkauf.txt"
```

`printf` wiederholt seine Vorlage für jedes weitere Argument und schreibt so jedes Wort in eine eigene Zeile ([Kapitel 5, Abschnitt 3.1](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/worttrennung-und-quoting.html#stufe-3-1)). Der zweite Dateiname enthält absichtlich ein Leerzeichen: Er zeigt im ganzen Kapitel, ob ein Skript mit solchen Namen richtig umgeht. Führe ein Skript, das Dateien löscht oder verschiebt, nie in einem Verzeichnis aus, dessen Inhalt dir wichtig ist.
:::

:::::

### Das Skript

<span class="anker" id="stufe-1-2"></span>

Angenommen, du willst dir öfter einen kurzen Überblick verschaffen: als wer du angemeldet bist, in welchem Verzeichnis du stehst und was darin liegt. Das sind drei Befehle, jedes Mal dieselben. Statt sie zu tippen, schreibst du sie einmal in eine Datei und lässt die Shell diese Datei abarbeiten.

Ein Bild zur Orientierung: ein Rezept auf einem Zettel. Wer kocht, liest Zeile für Zeile und führt jeden Schritt aus. Der Zettel selbst tut nichts; erst jemand, der ihn liest, macht daraus ein Essen.

:::definition Definition 1.1 (Shell-Skript)
<span class="anker" id="satz-1-1"></span>

Ein __Shell-Skript__, kurz Skript, ist eine Textdatei, in der Befehle für die Shell stehen, so wie man sie auch in die Befehlszeile tippen würde. Die Shell liest die Datei Zeile für Zeile und führt jeden Befehl aus, als wäre er getippt worden.
:::

Alles, was in der Befehlszeile geht, geht auch im Skript: Variablen, Umleitungen, Pipes, Expansion, Quoting. Umgekehrt lassen sich fast alle Mittel, die dieses Kapitel für Skripte einführt, auch direkt in der Befehlszeile benutzen. Die Endung `.sh` ist nur eine Gewohnheit, die Menschen zeigt, worum es sich handelt; Linux selbst wertet sie nicht aus.

Öffne mit `nano ueberblick.sh` eine neue Datei, tippe die folgenden vier Zeilen ab, speichere mit Strg+O und beende den Editor mit Strg+X:

```bash ueberblick.sh
echo "Benutzer: $USER"
echo "Verzeichnis: $PWD"
echo "Inhalt:"
ls
```

`$USER` und `$PWD` sind Variablen der Umgebung mit deinem Benutzernamen und dem Arbeitsverzeichnis ([Kapitel 5, Abschnitt 4.7](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/umgebung-und-vererbung.html#stufe-4-7)). Der Befehl `bash ueberblick.sh` startet eine bash, die nicht von der Tastatur liest, sondern aus dieser Datei:

```console
$ bash ueberblick.sh
Benutzer: student
Verzeichnis: /home/student/linuxk10
Inhalt:
 einkauf.txt  'mein einkauf.txt'   ueberblick.sh
```

`ls` setzt den Namen mit Leerzeichen in einfache Anführungszeichen und rückt die übrigen ein, damit man sieht, wo ein Name beginnt und endet; so zeigt es Namen nur an, wenn es in ein Terminal schreibt. Abbildung [1](#abb-1) zeigt, was beim Abarbeiten geschieht.

:::abbildung linux/k10skript 1
Ein Skript wird abgearbeitet. Oben die Datei `ueberblick.sh` mit vier nummerierten Zeilen, darunter das Terminal. Ein Lesezeichen wandert von Zeile zu Zeile; zu jeder Zeile erscheint unten die passende Ausgabe (`Benutzer: student`, `Verzeichnis: /home/student/linuxk10`, `Inhalt:`, die Liste der Dateien). Darüber das Etikett „bash liest die Datei Zeile für Zeile“.
:::

⁠**Kurz gesagt:** Ein Skript ist eine Textdatei mit Befehlen, die eine Shell der Reihe nach ausführt, als wären sie getippt worden.

### Der Interpreter

<span class="anker" id="stufe-1-3"></span>

Ein Skript ist kein Maschinencode, den der Prozessor direkt ausführen könnte, sondern Text. Es braucht ein Programm, das diesen Text liest und umsetzt.

:::definition Definition 1.2 (Interpreter)
<span class="anker" id="satz-1-2"></span>

Ein __Interpreter__ ist ein Programm, das eine Textdatei mit Anweisungen einliest und die Anweisungen nacheinander selbst ausführt, ohne vorher ein eigenständiges Programm daraus zu erzeugen.
:::

Für Shell-Skripte ist die Shell der Interpreter, in diesem Kapitel also `/usr/bin/bash`. Andere Sprachen haben andere Interpreter: Python-Programme führt der Interpreter `python3` aus ([Python, Kapitel 1](/wissen/informatik/programmieren/python/programme-und-der-python-interpreter/programme-und-der-python-interpreter.html)). Welcher Interpreter eine Datei bekommt, ist entscheidend, denn jeder versteht nur seine eigene Sprache.

::::beispiel Dieselbe Datei, ein anderer Interpreter
Gibt man `ueberblick.sh` an `python3` statt an `bash`, scheitert schon die erste Zeile, denn `echo "Benutzer: $USER"` ist für Python kein gültiger Satz. Eine Textdatei mit Befehlen ist also erst zusammen mit dem passenden Interpreter ein Programm.
::::

⁠**Kurz gesagt:** Ein Interpreter liest Anweisungen aus einer Textdatei und führt sie selbst aus; für Shell-Skripte ist das die bash.

### Der Kommentar

<span class="anker" id="stufe-1-4"></span>

Wer ein Skript nach Wochen wieder öffnet, weiß oft nicht mehr, wozu es dient und warum eine Zeile so aussieht. Dafür gibt es Text, den die Shell überliest.

:::definition Definition 1.3 (Kommentar)
<span class="anker" id="satz-1-3"></span>

Ein __Kommentar__ beginnt mit dem Zeichen `#` am Anfang eines Worts und reicht bis zum Ende der Zeile. Die Shell überspringt ihn beim Lesen.
:::

Ein Kommentar darf eine eigene Zeile füllen oder hinter einem Befehl stehen, dann mit mindestens einem Leerzeichen davor. In Anführungszeichen ist `#` ein gewöhnliches Zeichen. Die erweiterte Fassung von `ueberblick.sh` sagt in der ersten Zeile, was das Skript tut:

```bash ueberblick.sh
# ueberblick.sh: zeigt, wer ich bin, wo ich bin und was hier liegt
echo "Benutzer: $USER"
echo "Verzeichnis: $PWD"
echo "Inhalt:"
ls    # ohne Argument zeigt ls das Arbeitsverzeichnis
```

Die Ausgabe von `bash ueberblick.sh` bleibt Zeichen für Zeichen dieselbe wie im vorigen Unterabschnitt; die beiden Kommentare ändern nichts am Ablauf.

⁠**Kurz gesagt:** Ab einem `#` am Wortanfang ist der Rest der Zeile ein Kommentar für Menschen; die Shell überliest ihn.

### Ein Skript läuft in einem eigenen Prozess

<span class="anker" id="stufe-1-5"></span>

Der Befehl `bash ueberblick.sh` startet ein Programm, nämlich eine neue bash. Diese bash ist ein Kindprozess der Shell, in der du tippst. Was bedeutet das für Variablen und Verzeichniswechsel im Skript?

Ein Bild zur Orientierung: Du gibst einem Helfer eine Fotokopie deines Notizblocks und schickst ihn los. Was er auf seine Kopie schreibt und wohin er geht, ändert weder deinen Block noch deinen Standort.

:::satz Satz 1.4 (Ein Skript als Kindprozess)
<span class="anker" id="satz-1-4"></span>

Ein Skript, das mit `bash skript` gestartet wird, läuft in einer neuen bash, einem Kindprozess der aufrufenden Shell. Es bekommt eine Kopie von Umgebung und Arbeitsverzeichnis. Was es an Variablen setzt und wohin es mit `cd` wechselt, gilt nur in diesem Kindprozess und ist verloren, sobald das Skript endet.
:::

::::beispiel Ein Skript, das das Verzeichnis wechselt
Das Skript `wechsle.sh` wechselt nach `/tmp` und setzt eine Variable:

```bash wechsle.sh
# wechsle.sh: wechselt das Verzeichnis und setzt eine Variable
cd /tmp
ziel=erreicht
echo "Im Skript: $PWD, ziel=$ziel"
```

Nach dem Lauf steht die aufrufende Shell noch im Übungsverzeichnis, und die Variable `ziel` kennt sie nicht:

```console
$ bash wechsle.sh
Im Skript: /tmp, ziel=erreicht
$ pwd
/home/student/linuxk10
$ echo "ziel=$ziel"
ziel=
```
::::

Will man, dass Befehle aus einer Datei in der eigenen Shell wirken, liest man die Datei mit `source` ([Kapitel 5, Abschnitt 6.2](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/startdateien-und-aliase.html#stufe-6-2)). Dann gibt es keinen Kindprozess, und der Verzeichniswechsel bleibt bestehen:

```console
$ source wechsle.sh
Im Skript: /tmp, ziel=erreicht
$ pwd
/tmp
$ cd ~/linuxk10
```

Für gewöhnliche Skripte ist der eigene Prozess gerade erwünscht: Ein Skript kann in seinem Inneren Verzeichnisse wechseln und Variablen setzen, ohne die Shell zu verstellen, aus der es gestartet wurde. Abbildung [2](#abb-2) stellt beide Wege nebeneinander.

:::abbildung linux/k10eigeneshell 2
Zwei Wege, eine Datei mit Befehlen auszuführen. Links `bash wechsle.sh`: Aus der Shell (Kasten „Shell, Verzeichnis ~/linuxk10“) wächst ein Kindprozess mit einer Kopie des Kastens; in der Kopie springt das Verzeichnis auf `/tmp` und eine Schublade `ziel=erreicht` erscheint. Am Ende verschwindet der Kindprozess, der Kasten der Shell ist unverändert. Rechts `source wechsle.sh`: kein Kindprozess, die Änderungen landen direkt im Kasten der Shell, das Verzeichnis zeigt danach `/tmp`.
:::

⁠**Kurz gesagt:** `bash skript` arbeitet in einem Kindprozess mit Kopien; `cd` und Variablen im Skript wirken nicht auf die aufrufende Shell, `source` dagegen schon.

### Die Shebang-Zeile

<span class="anker" id="stufe-1-6"></span>

Bisher musste man beim Aufruf selbst sagen, welcher Interpreter die Datei bekommt: `bash ueberblick.sh`. Bequemer wäre es, wenn die Datei das selbst angeben könnte, so dass man sie starten kann wie jedes andere Programm.

:::definition Definition 1.5 (Shebang-Zeile)
<span class="anker" id="satz-1-5"></span>

Die __Shebang-Zeile__ ist die erste Zeile eines Skripts, wenn sie mit den beiden Zeichen `#!` beginnt. Hinter `#!` steht der absolute Pfad des Interpreters, für bash-Skripte also `#!/bin/bash`. Startet man die Datei direkt als Programm, führt Linux den hier genannten Interpreter aus und übergibt ihm die Datei.
:::

Der Name ist eine Zusammenziehung der englischen Namen der beiden Zeichen, „hash“ oder „sharp“ für `#` und „bang“ für `!`. Für die bash selbst ist die Zeile ein gewöhnlicher Kommentar, denn sie beginnt mit `#`. Sie muss wirklich die allererste Zeile sein, ohne Leerzeile oder Leerzeichen davor. Mit Shebang-Zeile sieht `ueberblick.sh` so aus:

```bash ueberblick.sh
#!/bin/bash
# ueberblick.sh: zeigt, wer ich bin, wo ich bin und was hier liegt
echo "Benutzer: $USER"
echo "Verzeichnis: $PWD"
echo "Inhalt:"
ls    # ohne Argument zeigt ls das Arbeitsverzeichnis
```

`/bin/bash` ist derselbe Interpreter wie `/usr/bin/bash`: Seit der Zusammenlegung der Verzeichnisse ist `/bin` nur ein zweiter Name für `/usr/bin` ([Kapitel 3, Abschnitt 8.6](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/inode-und-links.html#stufe-8-6)). Häufig sieht man auch die Form `#!/usr/bin/env bash`. Dort ist der Interpreter das Programm `env`, und `env` sucht `bash` im Suchpfad `PATH` ([Kapitel 5, Abschnitt 4.7](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/umgebung-und-vererbung.html#stufe-4-7)). Das hilft auf Systemen, auf denen die bash nicht unter `/bin` liegt, etwa wenn sie nachinstalliert wurde.

⁠**Kurz gesagt:** Die Shebang-Zeile `#!/bin/bash` ganz oben nennt den Interpreter, der das Skript ausführen soll, wenn man es direkt startet.

### Ein Skript direkt starten

<span class="anker" id="stufe-1-7"></span>

Ein Skript mit Shebang-Zeile soll sich starten lassen wie ein Programm, also mit `./ueberblick.sh`. Der erste Versuch scheitert:

```console
$ ./ueberblick.sh
bash: ./ueberblick.sh: Permission denied
$ echo $?
126
$ ls -l ueberblick.sh
-rw-r--r-- 1 student student 196 Nov 12 23:44 ueberblick.sh
$ chmod +x ueberblick.sh
$ ls -l ueberblick.sh
-rwxr-xr-x 1 student student 196 Nov 12 23:44 ueberblick.sh
$ ./ueberblick.sh
Benutzer: student
Verzeichnis: /home/student/linuxk10
Inhalt:
 einkauf.txt  'mein einkauf.txt'   ueberblick.sh   wechsle.sh
```

Der Editor hat die Datei mit den Rechten `rw-r--r--` angelegt, also ohne Ausführungsrecht, und der Exit-Status 126 heißt „gefunden, aber nicht ausführbar“ ([Kapitel 4, Abschnitt 5.3](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/der-exit-status.html#stufe-5-3)). Nach `chmod +x` läuft das Skript.

:::satz Satz 1.6 (Zwei Arten, ein Skript zu starten)
<span class="anker" id="satz-1-6"></span>

<ul>

<li>

`bash skript` startet das Programm `bash`; die Skriptdatei ist für die bash nur eine Datei, die sie liest. Dafür genügt das Leserecht an der Datei. Die Shebang-Zeile ist dabei ein Kommentar.

</li>

<li>

`./skript` startet die Skriptdatei selbst als Programm. Der Kernel prüft das Ausführungsrecht der Datei, liest die Shebang-Zeile und startet den dort genannten Interpreter; dabei setzt er den Pfad des Skripts als zusätzliches Argument vor die Argumente des Aufrufs. Der Interpreter muss die Datei danach lesen; nötig sind also Ausführungsrecht und Leserecht.

</li>

</ul>
:::

Man kann dem Kernel dabei zusehen. Das Skript `wer.sh` zeigt mit `ps`, mit welcher Befehlszeile sein eigener Prozess gestartet wurde; `$$` ist die Prozessnummer der bash, die das Skript ausführt ([Kapitel 8, Abschnitt 1.4](/wissen/informatik/linux-und-kommandozeile/prozesse-signale-und-dienste/prozesse-und-ihre-verwandtschaft.html#stufe-1-4)):

```bash wer.sh
#!/bin/bash
# wer.sh: zeigt, mit welcher Befehlszeile dieser Prozess gestartet wurde
ps -o args= -p "$$"
```

```console
$ chmod +x wer.sh
$ ./wer.sh eins zwei
/bin/bash ./wer.sh eins zwei
$ bash wer.sh eins zwei
bash wer.sh eins zwei
```

Getippt wurde `./wer.sh eins zwei`, gestartet hat der Kernel `/bin/bash ./wer.sh eins zwei`: den Interpreter aus der Shebang-Zeile, dahinter den Pfad des Skripts und dann die Argumente. Abbildung [3](#abb-3) zeigt den Weg Schritt für Schritt.

:::abbildung linux/k10ablauf 3
Was bei `./wer.sh eins zwei` geschieht. (1) Die Shell findet die Datei über den Pfad mit Schrägstrich und bittet den Kernel, sie als Programm zu starten. (2) Der Kernel prüft das Ausführungsrecht (Haken an `x`). (3) Er liest die ersten Bytes der Datei: `#!/bin/bash`. Ein Schild „kein Maschinenprogramm, sondern ein Skript“. (4) Er startet stattdessen `/bin/bash` mit der Argumentliste `/bin/bash ./wer.sh eins zwei`; die Teile erscheinen als Kärtchen, `./wer.sh` farbig als „neu eingefügt“. (5) Die bash öffnet `./wer.sh` zum Lesen (Haken an `r`) und arbeitet die Zeilen ab.
:::

:::hintergrund Woran der Kernel ein Skript erkennt
Wird eine Datei als Programm gestartet, liest der Kernel ihre ersten Bytes. Ein übersetztes Programm beginnt mit dem Byte 127 und den Buchstaben `E`, `L`, `F`, einer magischen Zahl ([Kapitel 3, Abschnitt 4.6](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-ansehen.html#stufe-4-6)). Beginnt die Datei dagegen mit den beiden Bytes 35 und 33, den Zeichen `#` und `!`, liest der Kernel den Rest der ersten Zeile bis zum Zeilenende als Pfad des Interpreters und startet diesen. Die Argumentliste baut er dabei um: Vorne steht der Interpreter, dann ein Argument aus der Shebang-Zeile, falls es eines gibt, dann der Pfad des Skripts, dann die ursprünglichen Argumente. Unter Linux wird alles hinter dem Interpreternamen als *ein* Argument übergeben, auch wenn es Leerzeichen enthält. Der Kernel liest hinter `#!` höchstens 255 Zeichen, vor Linux 5.1 waren es 127; was darüber hinausgeht, beachtet er nicht. Der Interpreter darf seinerseits ein Skript sein, bis zu einer Tiefe von vier solchen Stufen. Weil der Interpreter die Datei anschließend wie jede andere Datei öffnet, braucht ein direkt gestartetes Skript zusätzlich das Leserecht. Fehlt es, kommt die Meldung von der bash, die der Kernel schon gestartet hat:

```console
$ chmod u-r wer.sh
$ ls -l wer.sh
--wxr-xr-x 1 student student 105 Nov 12 23:44 wer.sh
$ ./wer.sh
/bin/bash: ./wer.sh: Permission denied
$ chmod u+r wer.sh
```

Die Meldung beginnt mit `/bin/bash:` statt mit `bash:`: Der Kernel hat das Ausführungsrecht akzeptiert und den Interpreter gestartet, erst dieser scheitert beim Lesen. Dieselbe Trennung zwischen Starten und Lesen ist der Grund, warum Linux das SUID-Bit bei Skripten nicht beachtet ([Kapitel 7, Abschnitt 9.5](/wissen/informatik/linux-und-kommandozeile/benutzer-gruppen-und-rechte/programme-ausfuhren-und-besondere-rechte.html#stufe-9-5)).
:::

:::hintergrund Und ohne Shebang-Zeile?
Startet man eine ausführbare Textdatei ohne Shebang-Zeile, lehnt der Kernel sie als „unbekanntes Format“ ab. Die bash fängt diesen Fall ab: Sie nimmt an, dass es sich um ein Shell-Skript handelt, und führt die Datei in einer neuen bash selbst aus. Deshalb läuft auch `wechsle.sh` direkt:

```console
$ chmod +x wechsle.sh
$ ./wechsle.sh
Im Skript: /tmp, ziel=erreicht
```

Verlassen sollte man sich darauf nicht. Startet ein anderes Programm als die bash die Datei, etwa eine andere Shell oder ein Dienst, entscheidet dieses Programm, was geschieht; die übliche Shell `sh` ist unter Ubuntu `dash`, die viele Möglichkeiten der bash nicht kennt. Eine Shebang-Zeile legt den Interpreter eindeutig fest.
:::

:::hintergrund Woher die Shebang-Zeile kommt
Die frühen Unix-Systeme kannten keine Shebang-Zeile; dort entschied die Shell selbst, eine ausführbare Textdatei als Shell-Skript zu lesen, so wie es die bash heute noch als Rückfall tut. Im Januar 1980 kündigte Dennis Ritchie bei den Bell Labs an, dass der Kernel Dateien, die mit `#!` beginnen, an den genannten Interpreter weiterreicht. Als Vorteile nannte er, dass sich Skripte damit starten lassen wie übersetzte Programme, dass jede Sprache einen Interpreter angeben kann und dass in der Prozessliste der Name des Skripts erscheint. Das Verfahren verbreitete sich über die BSD-Systeme und ist heute auf allen Unix-artigen Systemen üblich. Einen offiziellen Namen hat es nie bekommen. Ritchie selbst schrieb 2009, er könne sich nicht erinnern, dass man ihm je einen gegeben habe; die Idee habe er wohl von jemandem auf einer Tagung über das Unix aus Berkeley übernommen.
:::

⁠**Kurz gesagt:** `./skript` braucht Ausführungs- und Leserecht, weil der Kernel die Datei startet und dann die bash sie liest; `bash skript` braucht nur das Leserecht.

### Ein Skript wie einen Befehl aufrufen

<span class="anker" id="stufe-1-8"></span>

Mit `./ueberblick.sh` läuft das Skript nur, wenn man im richtigen Verzeichnis steht. Eigene Befehle möchte man aber von überall aufrufen, wie `ls`.

Die Shell sucht ein Programm, dessen Name keinen Schrägstrich enthält, der Reihe nach in den Verzeichnissen der Variablen `PATH` ([Kapitel 5, Abschnitt 5.3](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/wie-die-shell-programme-findet-path.html#stufe-5-3)). Ein Skript wird also zu einem gewöhnlichen Befehl, sobald es ausführbar in einem dieser Verzeichnisse liegt. Üblich ist für eigene Skripte das Verzeichnis `~/.local/bin`; Ubuntu nimmt es bei der Anmeldung in den Suchpfad auf, sobald es existiert ([Kapitel 5, Abschnitt 6.4](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/startdateien-und-aliase.html#stufe-6-4)). Im Übungsverzeichnis lässt sich das mit einem eigenen Verzeichnis `bin` nachstellen, das man für die laufende Shell vorn in den Suchpfad setzt ([Kapitel 5, Abschnitt 5.5](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/wie-die-shell-programme-findet-path.html#stufe-5-5)):

```console
$ mkdir bin
$ cp ueberblick.sh bin/ueberblick
$ ueberblick
ueberblick: command not found
$ PATH="$HOME/linuxk10/bin:$PATH"
$ type ueberblick
ueberblick is /home/student/linuxk10/bin/ueberblick
$ cd bin
$ ueberblick
Benutzer: student
Verzeichnis: /home/student/linuxk10/bin
Inhalt:
ueberblick
$ cd ..
```

`cp` übernimmt das Ausführungsrecht der Quelle. Für Befehle lässt man die Endung `.sh` meist weg, denn wer den Befehl aufruft, muss nicht wissen, in welcher Sprache er geschrieben ist. Das Skript zeigt das Verzeichnis, in dem man es aufruft, nicht das, in dem es liegt: Es arbeitet im Arbeitsverzeichnis seines Aufrufers.

⁠**Kurz gesagt:** Ein ausführbares Skript in einem Verzeichnis des Suchpfads, üblich ist `~/.local/bin`, ruft man wie jeden Befehl nur mit seinem Namen auf.

### Die Zeilenenden-Falle

<span class="anker" id="stufe-1-9"></span>

Wer unter Windows arbeitet, bearbeitet Skripte gern mit einem Windows-Editor und startet sie dann in WSL. Das kann mit einer rätselhaften Meldung scheitern, obwohl die Datei im Editor tadellos aussieht.

[Kapitel 6, Abschnitt 1.4](/wissen/informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke/textdaten-datensatze-felder-und-zeilenenden.html#stufe-1-4) hat den Grund gezeigt: Windows beendet jede Zeile mit den zwei Zeichen Wagenrücklauf und Zeilenende (`\r\n`), Linux nur mit dem Zeilenende (`\n`). Für ein Skript ist der zusätzliche Wagenrücklauf kein unsichtbarer Schmuck, sondern ein Zeichen, das zur Zeile gehört. Eine Datei mit Windows-Zeilenenden lässt sich mit `printf` nachbauen:

```console
$ printf '#!/bin/bash\r\necho "Hallo aus Windows"\r\nls einkauf.txt\r\n' > windows.sh
$ chmod +x windows.sh
$ ./windows.sh
bash: ./windows.sh: /bin/bash^M: bad interpreter: No such file or directory
$ echo $?
126
```

:::satz Satz 1.7 (Die Zeilenenden-Falle)
<span class="anker" id="satz-1-7"></span>

Hat ein Skript Windows-Zeilenenden, endet die Shebang-Zeile mit einem Wagenrücklauf. Der Kernel liest den Interpreternamen bis zum Zeilenende und sucht deshalb das Programm `/bin/bash` mit einem Wagenrücklauf am Ende, das es nicht gibt. Die bash meldet das als `bad interpreter` und zeigt den Wagenrücklauf als `^M`. Startet man die Datei mit `bash skript`, endet stattdessen jeder Befehl mit einem Wagenrücklauf, der als Teil des letzten Worts gelesen wird.
:::

Der zweite Weg zeigt das Problem an einem Argument. Die bash startet, aber `ls` soll die Datei `einkauf.txt` mit einem Wagenrücklauf am Ende auflisten; `ls` schreibt das unsichtbare Zeichen als `\r` in der Schreibweise `$'…'` ([Kapitel 5, Abschnitt 3.3](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/worttrennung-und-quoting.html#stufe-3-3)):

```console
$ bash windows.sh
Hallo aus Windows
ls: cannot access $'einkauf.txt\r': No such file or directory
```

Erkennen und entfernen lässt sich der Wagenrücklauf mit den Werkzeugen aus [Kapitel 6](/wissen/informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke/textwerkzeuge-und-regulaere-ausdruecke.html): `file` meldet die Windows-Zeilenenden, `od -c` zeigt sie als `\r`, und `sed -i 's/\r$//'` löscht am Ende jeder Zeile einen Wagenrücklauf ([Kapitel 6, Abschnitt 8.6](/wissen/informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke/umformen-im-strom-sed.html#stufe-8-6)):

```console
$ file windows.sh
windows.sh: Bourne-Again shell script, ASCII text executable, with CRLF line terminators
$ head -n 1 windows.sh | od -c
0000000   #   !   /   b   i   n   /   b   a   s   h  \r  \n
0000015
```

```console
$ sed -i 's/\r$//' windows.sh
$ file windows.sh
windows.sh: Bourne-Again shell script, ASCII text executable
$ ./windows.sh
Hallo aus Windows
einkauf.txt
```

Vorbeugen ist einfacher als reparieren: Fast jeder Editor unter Windows kann Dateien mit Linux-Zeilenenden speichern; Visual Studio Code etwa zeigt unten rechts `CRLF` oder `LF` und schaltet per Klick um. Das Programm `dos2unix` erledigt dieselbe Reparatur wie `sed`, ist unter Ubuntu aber nicht vorinstalliert. Abbildung [4](#abb-4) zeigt, wo genau das Zeichen stört.

:::abbildung linux/k10crlf 4
Die erste Zeile von `windows.sh` als Reihe von Byte-Kästchen: `# ! / b i n / b a s h \r \n`. Eine Klammer „Name des Interpreters“ reicht vom `/` bis vor das `\n` und schließt das rot markierte `\r` ein. Daneben ein Verzeichnis `/bin` mit dem Eintrag `bash`: Der gesuchte Name `bash\r` passt nicht, Ergebnis „No such file or directory“. Darunter dieselbe Zeile nach `sed`: ohne `\r`, die Klammer endet bei `h`, der Name passt.
:::

:::hintergrund Dieselbe Falle mit `env`
Steht in der Shebang-Zeile `#!/usr/bin/env bash`, findet der Kernel `env` ohne Probleme, denn der Wagenrücklauf hängt am Argument `bash`. Dann scheitert `env` mit der Meldung, es gebe kein Programm `bash\r`, und endet mit dem Status 127 („nicht gefunden“). Die Ursache ist dieselbe, nur meldet sie ein anderes Programm. Unter Ubuntu 26.04 ist `env` die uutils-Fassung; ihre Meldung beginnt mit `env:`, die GNU-Fassung mit `/usr/bin/env:`.
:::

⁠**Kurz gesagt:** Windows-Zeilenenden machen aus `#!/bin/bash` einen Interpreter mit einem unsichtbaren Zeichen am Ende; `file` erkennt die Falle, `sed -i 's/\r$//'` behebt sie.

:::aufgabe Aufgabe 1 ★ Zwei Wege, drei Rechte
<span class="anker" id="aufg-1"></span>

Eine Skriptdatei `probe.sh` mit Shebang-Zeile gehört dir. Sage für jede der drei Rechte-Angaben `r--`, `--x` und `r-x` in der Besitzerspalte voraus, ob `bash probe.sh` und ob `./probe.sh` läuft. Wer gibt jeweils die Fehlermeldung aus, die Shell, in der du tippst, oder die bash, die der Kernel gestartet hat?

:::loesung
`bash probe.sh` startet die bash; sie öffnet die Skriptdatei zum Lesen und braucht nur das Leserecht. `./probe.sh` startet die Datei selbst: Der Kernel verlangt das Ausführungsrecht, danach muss die bash die Datei lesen. Also:

<ul>

<li>

`r--`: `bash probe.sh` läuft; `./probe.sh` scheitert, und die Meldung beginnt mit `bash:`. Sie kommt von der Shell, in der du tippst, denn der Kernel hat den Start abgelehnt.

</li>

<li>

`--x`: Beide scheitern. `bash probe.sh` scheitert beim Lesen (Meldung `bash: probe.sh`); bei `./probe.sh` startet der Kernel `/bin/bash`, die dann nicht lesen darf, deshalb beginnt die Meldung mit `/bin/bash:`.

</li>

<li>

`r-x`: Beide laufen.

</li>

</ul>

```console
$ printf '#!/bin/bash\necho Hallo\n' > probe.sh
$ chmod 400 probe.sh
$ bash probe.sh
Hallo
$ ./probe.sh
bash: ./probe.sh: Permission denied
$ chmod 100 probe.sh
$ bash probe.sh
bash: probe.sh: Permission denied
$ ./probe.sh
/bin/bash: ./probe.sh: Permission denied
$ chmod 500 probe.sh
$ bash probe.sh
Hallo
$ ./probe.sh
Hallo
```
:::
:::

:::aufgabe Aufgabe 2 ★★ Ein Steckbrief des Systems
<span class="anker" id="aufg-2"></span>

Schreibe ein Skript `steckbrief.sh` mit Shebang-Zeile und einem Kommentar, das untereinander deinen Benutzernamen, die Kernelversion, die Zahl der Prozessorkerne und den freien Platz im Heimatverzeichnis ausgibt. Die Befehle dafür kennst du aus [Kapitel 2, Abschnitt 6](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/das-system-erkunden.html#stufe-6). Starte es einmal mit `bash` und einmal direkt.

:::loesung
Jede Zeile setzt die Ausgabe eines Befehls mit der Befehlsersetzung in einen Text ein. Den freien Platz liefert `df -h ~`; seine zweite Zeile enthält im vierten Feld den freien Platz, und `awk` schneidet ihn heraus ([Kapitel 6, Abschnitt 9.2](/wissen/informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke/rechnen-mit-spalten-awk.html#stufe-9-2)):

```bash steckbrief.sh
#!/bin/bash
# steckbrief.sh: ein kurzer Steckbrief dieses Systems
echo "Benutzer:  $(whoami)"
echo "Kernel:    $(uname -r)"
echo "Kerne:     $(nproc)"
echo "Frei in ~: $(df -h ~ | awk 'NR == 2 { print $4 }')"
```

```console
$ bash steckbrief.sh
Benutzer:  student
Kernel:    6.6.87.2-microsoft-standard-WSL2
Kerne:     14
Frei in ~: 952G
$ chmod +x steckbrief.sh
$ ./steckbrief.sh
Benutzer:  student
Kernel:    6.6.87.2-microsoft-standard-WSL2
Kerne:     14
Frei in ~: 952G
```

Beide Wege liefern dasselbe; der direkte braucht vorher `chmod +x`. Die Tilde steht in `df -h ~` ohne Anführungszeichen, damit die Shell sie ersetzt; in den doppelten Anführungszeichen von `echo` ist `~` dagegen nur ein Zeichen.
:::
:::

:::aufgabe Aufgabe 3 ★★ Die Zeilenenden-Falle nachstellen
<span class="anker" id="aufg-3"></span>

Lege mit `printf` ein Skript `hallo.sh` mit Windows-Zeilenenden an, das `Hallo` ausgibt. Starte es direkt und erkläre jeden Teil der Meldung. Repariere die Datei diesmal nicht mit `sed -i`, sondern mit `tr -d '\r'` und einer Umleitung in eine neue Datei ([Kapitel 6, Abschnitt 2.2](/wissen/informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke/spalten-ausschneiden-und-zeichen-ersetzen-cut-tr-und-paste.html#stufe-2-2)), und prüfe das Ergebnis mit `file`.

:::loesung
```console
$ printf '#!/bin/bash\r\necho Hallo\r\n' > hallo.sh
$ chmod +x hallo.sh
$ ./hallo.sh
bash: ./hallo.sh: /bin/bash^M: bad interpreter: No such file or directory
$ tr -d '\r' < hallo.sh > hallo_linux.sh
$ chmod +x hallo_linux.sh
$ file hallo.sh hallo_linux.sh
hallo.sh:       Bourne-Again shell script, ASCII text executable, with CRLF line terminators
hallo_linux.sh: Bourne-Again shell script, ASCII text executable
$ ./hallo_linux.sh
Hallo
```

Die Meldung besteht aus vier Teilen: `bash:` ist die Shell, in der du tippst; `./hallo.sh` das Skript, das sie starten wollte; `/bin/bash^M: bad interpreter` der Interpreter, den der Kernel aus der Shebang-Zeile gelesen hat, mit dem Wagenrücklauf als `^M`; `No such file or directory` der Grund, denn ein Programm dieses Namens gibt es nicht. `tr -d '\r'` löscht jeden Wagenrücklauf, wo immer er steht, und kann nur aus der Standardeingabe lesen, deshalb die Umleitungen. Die neue Datei bekommt die Rechte der umask, also ohne `x`; daher das zweite `chmod +x`.
:::
:::

:::aufgabe Aufgabe 4 ★★★ Ein Skript, das nicht wechseln kann
<span class="anker" id="aufg-4"></span>

Jemand schreibt ein Skript `geh.sh` mit der einzigen Zeile `cd ~/linuxk10/bin`, macht es ausführbar und ruft es auf. Danach steht er im selben Verzeichnis wie vorher. Erkläre, warum das so sein muss, und nenne einen Weg, mit dem dieselbe Datei das Verzeichnis der eigenen Shell doch wechselt. Warum würde auch ein `export` im Skript nichts an Variablen der aufrufenden Shell ändern?

:::loesung
`./geh.sh` läuft in einem Kindprozess. Der wechselt sein eigenes Arbeitsverzeichnis, und wenn er endet, ist dieser Zustand verloren; das Arbeitsverzeichnis der aufrufenden Shell hat er nie berührt (Abschnitt [1.5](#stufe-1-5)). `source geh.sh` führt dieselbe Zeile in der eigenen Shell aus:

```console
$ printf 'cd ~/linuxk10/bin\n' > geh.sh
$ chmod +x geh.sh
$ ./geh.sh
$ pwd
/home/student/linuxk10
$ source geh.sh
$ pwd
/home/student/linuxk10/bin
$ cd ~/linuxk10
```

Ein `export` im Skript markiert eine Variable nur für die Kindprozesse des Skripts. Die Umgebung wird beim Start als Kopie nach unten weitergegeben, nie nach oben zurück ([Kapitel 5, Abschnitt 4.5](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/umgebung-und-vererbung.html#stufe-4-5)); einen Weg vom Kind- zum Elternprozess gibt es dafür nicht.
:::
:::

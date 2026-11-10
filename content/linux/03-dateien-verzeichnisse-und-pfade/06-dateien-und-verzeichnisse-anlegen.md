---
title: Dateien und Verzeichnisse anlegen
pfad: Informatik / Linux und Kommandozeile / Dateien, Verzeichnisse und Pfade
adresse: informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade
knoten: Kapitel 3: Dateien, Verzeichnisse und Pfade
order: 6080600
summary: Bisher hast du nur geschaut.
tags: mkdir, -p, touch, Texteditor, nano, tree
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Bisher hast du nur geschaut. Ab hier veränderst du den Baum: Du legst Verzeichnisse an, erzeugst Dateien, schreibst Text hinein und betrachtest das Ergebnis als Baum. Dabei entsteht eine kleine Spielwiese zum Üben.
:::

:::warnung Nur im eigenen Übungsverzeichnis arbeiten
Ab jetzt verändern die Befehle Dateien. Lege alles im Übungsverzeichnis `~/linuxk3` an, das dieser Abschnitt erzeugt, und benutze Befehle, die etwas verändern, nur dort. Als gewöhnlicher Benutzer kannst du die Dateien des Systems ohnehin nicht verändern; tippe deshalb in diesem Kapitel nie einen Befehl mit vorangestelltem `sudo`, der dich zum Benutzer `root` machen würde. Unter WSL 2 gehört das Übungsverzeichnis in den Linux-Teil, nicht unter `/mnt/c` ([Kapitel 1, Abschnitt 4.7](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/wsl-2-linux-neben-windows.html#stufe-4-7)).
:::

### Ein Verzeichnis anlegen: mkdir

<span class="anker" id="stufe-5-1"></span>

Wer Ordnung halten will, legt zuerst Verzeichnisse an: eines für Rezepte, eines für Fotos. Dafür gibt es einen eigenen Befehl.

:::definition Definition 5.1 (mkdir)
<span class="anker" id="satz-5-1"></span>

Der Befehl __mkdir__ (kurz für „make directory“) legt für jedes Argument ein neues, leeres Verzeichnis an. Das übergeordnete Verzeichnis muss es schon geben, und der Name darf darin noch nicht vergeben sein.
:::

Ein neues Verzeichnis ist nicht ganz leer: Es enthält von Anfang an die Einträge `.` und `..`. Als leer gilt ein Verzeichnis, das nur diese beiden hat.

::::beispiel Das Übungsverzeichnis
```text
student@labor:~$ cd
student@labor:~$ mkdir linuxk3
student@labor:~$ cd linuxk3
student@labor:~/linuxk3$ mkdir rezepte fotos
student@labor:~/linuxk3$ ls -F
fotos/  rezepte/
student@labor:~/linuxk3$ mkdir rezepte
mkdir: rezepte: File exists
```

Ein Aufruf darf mehrere Verzeichnisse anlegen. Der zweite Versuch, `rezepte` anzulegen, scheitert, weil der Name vergeben ist. Die GNU-Fassung, die ein gewöhnliches Linux wie Debian benutzt und die unter Ubuntu 26.04 `gnumkdir` heißt ([Kapitel 2, Abschnitt 7.3](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/zwei-fassungen-der-grundbefehle-gnu-und-uutils.html#stufe-7-3)), meldet dasselbe ausführlicher: `cannot create directory ‘rezepte’: File exists`. Die knappe Form ist ein Stand der uutils-Fassung 0.8 in Ubuntu 26.04; spätere Fassungen können ihre Meldungen an GNU angleichen.
::::

**Mit Zwischenverzeichnissen: mkdir -p.** Will man mehrere Ebenen auf einmal anlegen, scheitert `mkdir`, weil das übergeordnete Verzeichnis noch fehlt. Die Option __-p__ (kurz für „parents“) legt fehlende Zwischenverzeichnisse mit an und meldet keinen Fehler, wenn ein Verzeichnis schon existiert. Abbildung [17](#abb-17) zeigt, wie dabei Ebene für Ebene entsteht.

:::abbildung linux/k3mkdirp 17
`mkdir fotos/urlaub/2026` scheitert, weil `urlaub` fehlt. `mkdir -p` legt der Reihe nach `urlaub` und `2026` an; die schon vorhandenen Verzeichnisse bleiben unberührt.
:::

::::beispiel [Zweites Beispiel] Drei Ebenen auf einmal
```console
$ mkdir fotos/urlaub/2026
mkdir: No such file or directory
$ mkdir -p fotos/urlaub/2026 rezepte/kuchen rezepte/suppen
$ ls -F fotos fotos/urlaub
fotos:
urlaub/

fotos/urlaub:
2026/
```

Die erste Meldung nennt unter Ubuntu 26.04 derzeit nicht einmal den Pfad; die GNU-Fassung schreibt `cannot create directory ‘fotos/urlaub/2026’: No such file or directory`. Gemeint ist in beiden Fällen: Auf dem Weg fehlt ein Verzeichnis. Mit `-p` klappt es, und nebenbei entstehen `rezepte/kuchen` und `rezepte/suppen`.
::::

⁠**Kurz gesagt:** `mkdir` legt Verzeichnisse an; mit `-p` auch alle fehlenden Ebenen darüber.

### Eine leere Datei anlegen: touch

<span class="anker" id="stufe-5-2"></span>

Manchmal braucht man eine Datei, bevor man etwas hineinschreibt, etwa als Platzhalter für eine Liste, die man gleich füllen will. Der Befehl dafür hat eigentlich eine andere Hauptaufgabe; Abbildung [18](#abb-18) zeigt beide.

:::abbildung linux/k3touch 18
`touch` auf einen neuen Namen legt eine leere Datei mit 0 Bytes an. `touch` auf eine vorhandene Datei lässt den Inhalt in Ruhe und stellt nur die Uhr der letzten Änderung auf jetzt.
:::

:::definition Definition 5.2 (touch)
<span class="anker" id="satz-5-2"></span>

Der Befehl __touch__ setzt für jede genannte Datei den Zeitpunkt der letzten Änderung und des letzten Zugriffs auf die aktuelle Uhrzeit. Gibt es die Datei noch nicht, legt er sie als leere Datei mit 0 Bytes an.
:::

`touch` verändert den Inhalt einer vorhandenen Datei nie, auch wenn der Name das nahelegt. Mit der Option `-t` kann man statt der aktuellen Uhrzeit einen beliebigen Zeitpunkt eintragen, geschrieben als `JJJJMMTThhmm`.

::::beispiel Ein Platzhalter für die Einkaufsliste
```console
$ touch einkauf.txt
$ ls -l einkauf.txt
-rw-r--r-- 1 student student 0 Nov 10 02:41 einkauf.txt
```

Die neue Datei gehört dir (`student`) und hat 0 Bytes.
::::

::::beispiel [Zweites Beispiel] Die Uhr zurück- und wieder vorstellen
```console
$ touch -t 202611091830 einkauf.txt
$ ls -l einkauf.txt
-rw-r--r-- 1 student student 0 Nov  9 18:30 einkauf.txt
$ touch einkauf.txt
$ ls -l einkauf.txt
-rw-r--r-- 1 student student 0 Nov 10 02:41 einkauf.txt
```

Erst trägt `touch` den Abend des Vortags ein, dann wieder die aktuelle Uhrzeit. Die Größe bleibt 0. Die Option `-d` mit einer Zeitangabe wie `"2026-11-09 18:30"` leistet unter GNU dasselbe; die uutils-Fassung 0.8 in Ubuntu 26.04 deutet eine solche Angabe aber als Weltzeit (UTC) und verschiebt sie deshalb, im deutschen Winter um eine Stunde nach hinten. Das ist ein Fehler dieser Fassung, der mit einer Aktualisierung verschwinden kann. `-t` verhält sich in beiden Fassungen gleich.
::::

⁠**Kurz gesagt:** `touch` legt eine leere Datei an oder stellt bei einer vorhandenen nur die Änderungszeit auf jetzt.

:::hintergrund Drei Zeitstempel je Datei
Linux merkt sich zu jeder Datei mehrere Zeitpunkte. Die Änderungszeit, die `ls -l` zeigt, gehört zum letzten Schreiben des Inhalts. Die Zugriffszeit gehört zum letzten Lesen; damit nicht jedes Lesen einen Schreibvorgang auf dem Datenträger auslöst, aktualisiert Linux sie meist nur, wenn sie älter ist als die Änderungszeit oder älter als ein Tag. Eine dritte Zeit, die Statusänderungszeit, rückt bei jeder Änderung an den Verwaltungsangaben vor, etwa an Rechten oder am Namen; sie lässt sich auch mit `touch` nicht zurückstellen. Viele Dateisysteme speichern zusätzlich die Entstehungszeit. Programme zum Sichern von Daten nutzen die Änderungszeit, um nur das zu kopieren, was sich seit dem letzten Mal geändert hat; mit `touch` kann man ihnen deshalb vortäuschen, eine Datei sei neu.
:::

### Der Texteditor nano

<span class="anker" id="stufe-5-3"></span>

Eine leere Datei ist erst der Anfang; jetzt soll Text hinein. Ein grafisches Programm wie den Editor von Windows gibt es im Terminal nicht, wohl aber Editoren, die im Terminalfenster selbst laufen.

:::definition Definition 5.3 (Texteditor, nano)
<span class="anker" id="satz-5-3"></span>

Ein __Texteditor__ ist ein Programm, mit dem man Textdateien anlegt und verändert; er speichert nur die Zeichen, keine Schriftart und keine Formatierung. __nano__ ist ein einfacher Texteditor, der im Terminal läuft und die wichtigsten Tastenkürzel ständig am unteren Rand anzeigt.
:::

Man startet ihn mit `nano datei`. Gibt es die Datei, zeigt er ihren Inhalt; gibt es sie nicht, beginnt er mit einer leeren Seite und legt die Datei erst beim Speichern an. Du tippst wie in jedem Editor; die Pfeiltasten bewegen den Cursor. Die Befehle laufen über Tastenkürzel, die nano unten auflistet: Das Zeichen `^` steht dort für die Strg-Taste, `M-` für die Alt-Taste. Unter Ubuntu 26.04 sind diese Zeilen englisch, solange das System auf Englisch eingestellt ist. Abbildung [19](#abb-19) zeigt den Aufbau des Fensters.

:::abbildung linux/k3nano 19
Das Fenster von nano im Schema: oben eine Titelzeile mit Programm und Dateiname (ein Stern heißt „ungespeichert“), in der Mitte der Text mit dem Cursor, unten eine Statuszeile für Meldungen und zwei Zeilen mit Tastenkürzeln. Nacheinander leuchten die Kürzel zum Speichern und zum Beenden auf.
:::

Diese Kürzel brauchst du ständig:

<ul>

<li>

⁠**Strg+O** speichert („Write Out“); nano fragt unten nach dem Dateinamen, die Eingabetaste bestätigt ihn.

</li>

<li>

⁠**Strg+X** beendet nano; ist der Text ungespeichert, fragt nano vorher, ob er speichern soll (`Y` für ja, `N` für nein).

</li>

<li>

⁠**Strg+K** schneidet die Zeile aus, in der der Cursor steht, **Strg+U** fügt sie wieder ein.

</li>

<li>

⁠**Strg+F** sucht nach einem Wort, **Strg+G** zeigt die Hilfe.

</li>

</ul>

::::beispiel Die Einkaufsliste schreiben
Tippe im Übungsverzeichnis `nano einkauf.txt`. Schreibe die vier Zeilen `Milch`, `Brot`, `Äpfel` und `Kaffee`, nach den ersten drei jeweils mit der Eingabetaste. Nach der letzten Zeile drückst du keine Eingabetaste; nano hängt das Zeilenende beim Speichern selbst an. So sieht das Fenster aus, wenn du fertig getippt hast, hier mit 72 Zeichen Breite und 16 Zeilen Höhe:

```text
  GNU nano 8.7.1                  einkauf.txt *
Milch
Brot
Äpfel
Kaffee
...
^G Help       ^O Write Out  ^F Where Is   ^K Cut        ^T Execute
^X Exit       ^R Read File  ^\ Replace    ^U Paste      ^J Justify
```

Strg+O fragt unten `Write to File: einkauf.txt`; nach der Eingabetaste meldet nano `[ Wrote 4 lines ]`, und der Stern in der Titelzeile verschwindet. Strg+X beendet nano. Zurück an der Eingabeaufforderung prüfst du das Ergebnis:

```console
$ cat einkauf.txt
Milch
Brot
Äpfel
Kaffee
$ wc einkauf.txt
 4  4 25 einkauf.txt
```

Vier Zeilen, vier Wörter, 25 Bytes. Zeichen sind es nur 24, denn das `Ä` belegt zwei Bytes (Unterabschnitt [4.1](dateien-ansehen.html#stufe-4-1)): `Milch` hat mit Zeilenende 6 Zeichen und 6 Bytes, `Brot` 5 und 5, `Kaffee` 7 und 7, `Äpfel` aber 6 Zeichen und 7 Bytes. Abbildung [20](#abb-20) zählt die Bytes zeilenweise zusammen: $6 + 5 + 7 + 7 = 25$.

:::abbildung linux/k3einkauf 20
Die Bytes der Einkaufsliste, Zeile für Zeile gezählt: `Milch` 6, `Brot` 5, `Äpfel` 7, `Kaffee` 7, jeweils mit Zeilenende. Die Summe ist 25, wie `wc` meldet.
:::

Lege auf dieselbe Weise drei Rezepte an, `rezepte/kuchen/apfelkuchen.txt`, `rezepte/kuchen/kaesekuchen.txt` und `rezepte/suppen/kuerbissuppe.txt`, mit ein paar Zeilen Zutaten. Den Pfad gibst du nano einfach als Argument mit.
::::

⁠**Kurz gesagt:** `nano datei` öffnet einen Texteditor im Terminal; Strg+O speichert, Strg+X beendet.

:::hintergrund Andere Editoren und warum man einen im Terminal braucht
Auf vielen Servern gibt es keine grafische Oberfläche, und über eine Netzverbindung kommt man oft nur mit einem Terminal an den Rechner. Ein Editor, der im Terminal läuft, funktioniert dort genauso wie am eigenen Schreibtisch. nano ist auf fast jedem Linux vorhanden und leicht zu bedienen. Viele Fachleute benutzen stattdessen vim, einen mächtigeren Editor mit eigener Bedienlogik: Man tippt dort zunächst Befehle statt Text. Wer sich in vim verirrt hat, verlässt ihn ohne zu speichern mit Esc, dann `:q!` und der Eingabetaste. Unter WSL 2 kann man Linux-Dateien auch mit Editoren unter Windows bearbeiten, etwa mit Visual Studio Code und seiner Erweiterung für WSL; der gewöhnliche Editor von Windows ist dafür weniger geeignet, weil er unter Umständen ein anderes Zeilenende schreibt.
:::

### Der Baum auf einen Blick: tree

<span class="anker" id="stufe-5-4"></span>

Nach einigen `mkdir` und `nano` verliert man leicht den Überblick, was wo liegt. `ls` zeigt immer nur eine Ebene; schöner wäre der ganze Baum.

:::definition Definition 5.4 (tree)
<span class="anker" id="satz-5-4"></span>

Der Befehl __tree__ zeichnet den Verzeichnisbaum ab dem genannten Verzeichnis, ohne Argument ab dem Arbeitsverzeichnis, mit Linien für die Ebenen und zählt am Ende Verzeichnisse und Dateien. Mit `-a` zeigt er auch versteckte Einträge.
:::

`tree` ist auf Ubuntu nicht vorinstalliert. Meldet die Shell `command not found`, tippst du einmal das folgende Rezept; es ist die einzige Ausnahme von der Regel in der Warnung oben:

```console
$ sudo apt install tree
```

`sudo` führt den Befehl mit den Rechten von `root` aus und fragt dazu nach dem Passwort, das du beim Einrichten deines Linux-Kontos gewählt hast ([Kapitel 1, Abschnitt 4.2](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/wsl-2-linux-neben-windows.html#stufe-4-2)); beim Tippen erscheinen keine Zeichen. `apt` ist die Paketverwaltung von Ubuntu ([Kapitel 1, Abschnitt 1.6](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/betriebssystem-kernel-und-distribution.html#stufe-1-6)) und installiert das Programm aus den Quellen der Distribution. Geht das nicht, etwa auf einem fremden Rechner, zeigt `ls -R` aus Unterabschnitt [3.6](den-inhalt-eines-verzeichnisses-anzeigen.html#stufe-3-6) dieselben Einträge, nur Verzeichnis für Verzeichnis statt als Baum.

::::beispiel Die Spielwiese
Lege zuerst ein paar leere Fotodateien und eine versteckte Einstellungsdatei an, dann zeigt `tree` alles:

```console
$ cd fotos/urlaub/2026
$ touch strand_1.jpg strand_2.jpg strand_10.jpg berg_1.jpg berg_2.jpg notiz.txt
$ ls
berg_1.jpg  notiz.txt     strand_10.jpg
berg_2.jpg  strand_1.jpg  strand_2.jpg
$ cd ~/linuxk3
$ touch .einstellungen
```

```console
$ tree
.
├── einkauf.txt
├── fotos
│   └── urlaub
│       └── 2026
│           ├── berg_1.jpg
│           ├── berg_2.jpg
│           ├── notiz.txt
│           ├── strand_1.jpg
│           ├── strand_10.jpg
│           └── strand_2.jpg
└── rezepte
    ├── kuchen
    │   ├── apfelkuchen.txt
    │   └── kaesekuchen.txt
    └── suppen
        └── kuerbissuppe.txt

7 directories, 10 files
```

Gezählt werden sieben Verzeichnisse, das Arbeitsverzeichnis `.` eingeschlossen, und zehn Dateien. `.einstellungen` fehlt, weil sie versteckt ist; `tree -a` zeigt sie mit. Auf dieser Spielwiese laufen die Beispiele der folgenden Abschnitte.
::::

⁠**Kurz gesagt:** `tree` zeigt einen Teilbaum mit allen Ebenen auf einmal.

### Aufgaben zu Abschnitt [5](#stufe-5)

<span class="anker" id="stufe-5-5"></span>

:::aufgabe Aufgabe 14 ★ Zwischenverzeichnisse
<span class="anker" id="aufg-14"></span>

Du tippst im Übungsverzeichnis `mkdir projekt/daten/roh`, ohne dass es `projekt` gibt. Was geschieht? Wie legst du alle drei Ebenen mit einem einzigen Befehl an? Was meldet derselbe Befehl, wenn du ihn ein zweites Mal tippst?

:::loesung
`mkdir projekt/daten/roh` scheitert, weil `projekt` und `daten` fehlen; Ubuntu 26.04 meldet nur `mkdir: No such file or directory`. `mkdir -p projekt/daten/roh` legt alle drei Ebenen an. Ein zweites `mkdir -p` mit demselben Pfad meldet nichts, denn `-p` akzeptiert vorhandene Verzeichnisse. Erst ohne `-p` gäbe es wieder eine Meldung:

```console
$ mkdir projekt/daten/roh
mkdir: No such file or directory
$ mkdir -p projekt/daten/roh
$ mkdir -p projekt/daten/roh
$ mkdir projekt/daten/roh
mkdir: projekt/daten/roh: File exists
```
:::
:::

:::aufgabe Aufgabe 15 ★★ Eine zweite Spielwiese
<span class="anker" id="aufg-15"></span>

Lege im Übungsverzeichnis für einen Sportverein das Verzeichnis `verein` mit den Unterverzeichnissen `mitglieder` und `termine` an, darin die leeren Dateien `mitglieder/liste.txt`, `termine/sommerfest.txt`, `beitraege.csv` und die versteckte Datei `.einstellungen`. Vergleiche dann in `verein` die Ausgaben von `ls`, `ls -a`, `ls -F` und `tree -a`. Was zeigt jede, was nicht?

:::loesung
```console
$ mkdir -p verein/mitglieder verein/termine
$ cd verein
$ touch mitglieder/liste.txt termine/sommerfest.txt beitraege.csv .einstellungen
$ ls
beitraege.csv  mitglieder  termine
$ ls -a
.  ..  .einstellungen  beitraege.csv  mitglieder  termine
$ ls -F
beitraege.csv  mitglieder/  termine/
$ tree -a
.
├── .einstellungen
├── beitraege.csv
├── mitglieder
│   └── liste.txt
└── termine
    └── sommerfest.txt

3 directories, 4 files
$ cd ..
```

`ls` zeigt nur die sichtbaren Einträge der obersten Ebene und verrät nicht, was Verzeichnisse sind. `ls -a` zeigt zusätzlich `.`, `..` und die versteckte Datei. `ls -F` markiert die beiden Verzeichnisse mit `/`. Nur `tree -a` zeigt alle Ebenen auf einmal, samt der versteckten Datei und der Dateien in den Unterverzeichnissen.
:::
:::

:::aufgabe Aufgabe 16 ★★ Die letzte Zeile in nano
<span class="anker" id="aufg-16"></span>

Schreibe mit nano eine Datei `drei.txt` mit den Zeilen `eins`, `zwei`, `drei`, ohne Eingabetaste nach `drei`, und eine Datei `vier.txt` mit denselben Zeilen, aber mit Eingabetaste nach `drei`. Sage voraus, was `wc -l drei.txt vier.txt` meldet, und prüfe es. Lösche beide Dateien danach mit `rm drei.txt vier.txt`; der Befehl `rm` entfernt die genannten Dateien.

:::loesung
Vorhersage: `drei.txt` hat drei Zeilenenden, also 3 Zeilen; nano hat das letzte selbst angehängt. In `vier.txt` steht nach `drei` das Zeilenende, das die Eingabetaste erzeugt hat, und danach eine leere Zeile, der nano beim Speichern ebenfalls ein Zeilenende anhängt: 4 Zeilen, die letzte leer.

```console
$ wc -l drei.txt vier.txt
 3 drei.txt
 4 vier.txt
 7 total
$ rm drei.txt vier.txt
```

`wc -l` zählt Zeilenenden, und die leere Zeile hat eines.
:::
:::

:::aufgabe Aufgabe 17 ★ touch auf eine vorhandene Datei
<span class="anker" id="aufg-17"></span>

Was ändert `touch einkauf.txt`, wenn die Einkaufsliste schon vier Zeilen enthält? Was bleibt gleich? Überlege zuerst, dann prüfe mit `ls -l` vorher und nachher und mit `cat`.

:::loesung
`touch` ändert bei einer vorhandenen Datei nur Zeitstempel: Änderungs- und Zugriffszeit springen auf jetzt, und mit ihnen die Statusänderungszeit. Gleich bleiben der Inhalt, die Größe, der Name, Besitzer und Zugriffsrechte. `ls -l` zeigt danach eine neue Uhrzeit bei unveränderter Größe; `cat` zeigt dieselben vier Zeilen wie vorher.
:::
:::

---
title: Wie die Shell Programme findet: PATH
pfad: Informatik / Linux und Kommandozeile / Wie die Shell eine Befehlszeile liest: Expansion, Quoting, Variablen, Umgebung
adresse: informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung
knoten: Kapitel 5: Wie die Shell eine Befehlszeile liest: Expansion, Quoting, Variablen, Umgebung
order: 6100600
summary: Kapitel 2 hat den Suchpfad eingeführt, die Liste der Verzeichnisse, in denen die Shell nach Programmen sucht.
tags: PATH
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
[Kapitel 2](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/die-shell-erste-befehle.html) hat den Suchpfad eingeführt, die Liste der Verzeichnisse, in denen die Shell nach Programmen sucht. Dieser Abschnitt zeigt, dass dahinter eine Umgebungsvariable steckt, nach welchen Regeln die Shell sucht, warum ein Programm im Arbeitsverzeichnis nicht ohne Weiteres startet und wie man den Suchpfad ändert.
:::

:::::vorwissen Was du dafür brauchst: Suchpfad und Befehlsarten

<span class="anker" id="stufe-5-1"></span>

<ul>

<li>

Der Suchpfad ist die Liste von Verzeichnissen, in denen die Shell nach einer Programmdatei mit dem Namen des Befehls sucht; sie startet die erste, die sie findet. Eingebaute Befehle und Aliase brauchen keine Suche. `type` zeigt, was hinter einem Namen steckt ([Kapitel 2, Abschnitte 3.2](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/arten-von-befehlen.html#stufe-3-2) bis 3.5).

</li>

<li>

`/bin` ist unter Ubuntu nur ein zweiter Name für `/usr/bin` ([Kapitel 3, Abschnitt 8.6](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/inode-und-links.html#stufe-8-6)). `tree` zeichnet einen Verzeichnisbaum ([Kapitel 3, Abschnitt 5.4](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-und-verzeichnisse-anlegen.html#stufe-5-4)). `ls -l` zeigt die Zugriffsrechte einer Datei als neun Zeichen ([Kapitel 3, Abschnitt 3.4](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/den-inhalt-eines-verzeichnisses-anzeigen.html#stufe-3-4)).

</li>

<li>

`tr` ersetzt Zeichen in seiner Standardeingabe ([Kapitel 4, Abschnitt 3.3](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/eingaben-umleiten.html#stufe-3-3)). Der Exit-Status 127 heißt „Befehl nicht gefunden“ ([Kapitel 4, Abschnitt 5.3](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/der-exit-status.html#stufe-5-3)).

</li>

</ul>

⁠**Kurz gesagt:** Du brauchst den Suchpfad, die Befehlsarten mit `type`, `tree`, `tr` und den Exit-Status 127.

:::::

### Die Variable PATH

<span class="anker" id="stufe-5-2"></span>

Woher weiß die Shell, welche Verzeichnisse zum Suchpfad gehören? Die Antwort ist eine Umgebungsvariable, die du lesen und ändern kannst wie jede andere. Abbildung [20](#abb-20) zeigt, wie aus ihrem Wert eine Liste wird.

:::abbildung linux/k5path 20
Der Wert von `PATH` ist ein einziger Text. Die Doppelpunkte darin trennen die Verzeichnisse; von links nach rechts gelesen ergeben sie die Reihenfolge, in der die Shell sucht.
:::

:::definition Definition 5.1 (PATH)
<span class="anker" id="satz-5-1"></span>

Die Umgebungsvariable __PATH__ enthält den Suchpfad als Text: die Verzeichnisse, durch Doppelpunkte getrennt, in der Reihenfolge, in der die Shell sie durchsucht. Ein leerer Eintrag, also zwei Doppelpunkte hintereinander oder ein Doppelpunkt am Anfang oder am Ende, steht für das Arbeitsverzeichnis.
:::

Den leeren Eintrag führt der Standard für Unix-Shells nur noch als Überbleibsel aus alter Zeit; wer das Arbeitsverzeichnis meint, soll `.` schreiben. Weil `PATH` eine Umgebungsvariable ist, bekommt jedes Kind den Suchpfad seines Elternprozesses mit.

::::beispiel Den Suchpfad lesen
Der Wert ist lang. Damit jedes Verzeichnis auf einer eigenen Zeile steht, ersetzt `tr` jeden Doppelpunkt durch ein Zeilenende; `head` zeigt die ersten neun:

```console
$ echo "$PATH" | tr ':' '\n' | head -n 9
/usr/local/sbin
/usr/local/bin
/usr/sbin
/usr/bin
/sbin
/bin
/usr/games
/usr/local/games
/usr/lib/wsl/lib
```

Die ersten acht Einträge stammen aus der Voreinstellung von Ubuntu; `/usr/lib/wsl/lib` und die vielen Verzeichnisse von Windows, die unter WSL 2 danach folgen, hängt WSL an. Weil `/bin` ein zweiter Name für `/usr/bin` ist, findet die Shell manche Programme doppelt:

```console
$ type -a ls
ls is aliased to `ls --color=auto'
ls is /usr/bin/ls
ls is /bin/ls
```

`type -a` nennt alle Treffer in der Reihenfolge der Suche. Gestartet wird der erste: Der Alias aus [Kapitel 2, Abschnitt 3.4](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/arten-von-befehlen.html#stufe-3-4) führt zu `ls`, und das findet die Shell in `/usr/bin`. Knapper antwortet der eingebaute Befehl `command -v`: Er schreibt für jeden Namen nur, was die Shell starten würde, bei einem Programm den Pfad, bei einem eingebauten Befehl den Namen.

```console
$ command -v tree cd
/usr/bin/tree
cd
```
::::

⁠**Kurz gesagt:** `PATH` ist der Suchpfad als Text, die Verzeichnisse durch Doppelpunkte getrennt und in der Reihenfolge der Suche.

### Die Befehlssuche

<span class="anker" id="stufe-5-3"></span>

Mit `PATH` lassen sich die Regeln der Suche vollständig angeben, auch für den Fall, dass der Name schon einen Pfad enthält.

:::satz Satz 5.2 (Befehlssuche)
<span class="anker" id="satz-5-2"></span>

Enthält der Befehlsname keinen Schrägstrich, prüft die Shell nach Alias, Schlüsselwort, Funktion und eingebautem Befehl ([Kapitel 2, Abschnitt 3.5](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/arten-von-befehlen.html#stufe-3-5)) die Verzeichnisse aus `PATH` von links nach rechts und startet die erste ausführbare Datei mit diesem Namen; den gefundenen Pfad merkt sie sich für später. Findet sie keine, meldet sie den Fehler und setzt den Exit-Status 127. Enthält der Befehlsname einen Schrägstrich, sucht die Shell gar nicht, sondern startet genau die Datei, die der Pfad bezeichnet.
:::

Abbildung [21](#abb-21) fasst den Weg vom Namen zum gestarteten Programm als Entscheidungsbaum zusammen.

:::abbildung linux/k5befehlssuche 21
Die Befehlssuche als Entscheidungsbaum. Erste Frage: Enthält der Name einen Schrägstrich? Ja: Die Shell startet genau diese Datei. Nein: Ist er ein Alias, ein Schlüsselwort, eine Funktion oder ein eingebauter Befehl? Dann erledigt die Shell ihn selbst. Sonst geht sie die Verzeichnisse aus `PATH` von links nach rechts durch: beim ersten Treffer Start und Merken des Pfads, ohne Treffer die Meldung „command not found“ und der Exit-Status 127.
:::

::::beispiel Mit Pfad gibt es keine Suche
```console
$ /usr/bin/echo Hallo
Hallo
```

`echo` allein wäre der eingebaute Befehl. Mit dem Pfad `/usr/bin/echo` startet die Shell stattdessen die gleichnamige Programmdatei, ohne zu suchen.
::::

⁠**Kurz gesagt:** Ohne Schrägstrich sucht die Shell in `PATH` und nimmt den ersten Treffer, mit Schrägstrich startet sie genau die genannte Datei.

:::hintergrund Die Shell merkt sich gefundene Programme
Damit sie nicht bei jedem Aufruf alle Verzeichnisse durchgehen muss, legt bash für jedes gefundene Programm einen Eintrag in einer Tabelle an. Der eingebaute Befehl `hash` zeigt diese Tabelle, `type` sagt bei einem gemerkten Programm „is hashed“. Verschiebt man ein Programm, nachdem die Shell es gemerkt hat, versucht sie es weiter am alten Ort und meldet, dass es die Datei dort nicht gibt; erst `hash -r` leert die Tabelle, und die Suche beginnt neu. Jede neue Zuweisung an `PATH` leert sie ebenfalls.
:::

### Ein Programm im Arbeitsverzeichnis: ./

<span class="anker" id="stufe-5-4"></span>

Legt man selbst ein Programm in ein Verzeichnis, das nicht im Suchpfad steht, findet die Shell es nicht, obwohl es direkt vor einem liegt. Für einen Versuch braucht man ein Programm. Bei den üblichen Voreinstellungen gibt `cp` der Kopie die Zugriffsrechte des Originals, darunter die Angabe, dass die Datei als Programm gestartet werden darf; eine Kopie von `tree` ist also wieder ein startbares Programm. Lege eine solche Kopie unter dem Namen `meinbaum` im Übungsverzeichnis an:

```console
$ cp /usr/bin/tree ./meinbaum
```

Abbildung [22](#abb-22) zeigt, was die Shell mit zwei Schreibweisen dieses Namens macht.

:::abbildung linux/k5punktslash 22
Oben `meinbaum`: kein Schrägstrich, also sucht die Shell in den Verzeichnissen aus `PATH`. Das Arbeitsverzeichnis `/home/student/linuxk5` gehört nicht dazu; die Suche endet ohne Treffer mit dem Exit-Status 127. Unten `./meinbaum`: Der Schrägstrich macht daraus einen Pfad, und die Shell startet die Datei im Arbeitsverzeichnis direkt.
:::

::::beispiel Mit und ohne ./
```console
$ meinbaum
meinbaum: command not found
$ echo $?
127
$ ./meinbaum urlaub
urlaub
├── 2025
│   ├── sommer
│   └── winter
└── 2026
    ├── sommer
    └── winter

7 directories, 0 files
```

Ohne Pfad findet die Shell `meinbaum` nicht. Mit `./` davor ist es ein relativer Pfad zum Arbeitsverzeichnis ([Kapitel 3, Abschnitt 2.5](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/das-arbeitsverzeichnis-und-pfade.html#stufe-2-5)), und das Programm zeichnet den Baum, den die Klammererweiterung in Unterabschnitt [1.6](expansion-muster-klammern-und-tilde.html#stufe-1-6) angelegt hat; `tree` zählt das Startverzeichnis mit.
::::

:::satz Satz 5.3 (Programm außerhalb des Suchpfads)
<span class="anker" id="satz-5-3"></span>

Ein Programm, das in keinem Verzeichnis aus `PATH` liegt, startet man mit einem Pfad, der einen Schrägstrich enthält: `./programm` im Arbeitsverzeichnis, sonst mit einem absoluten oder relativen Pfad.
:::

:::warnung Nicht jedes Programm verträgt einen neuen Namen
Stand der uutils-Fassung in Ubuntu 26.04: Die meisten Grundbefehle sind dort ein einziges Multicall-Programm, das am Aufrufnamen erkennt, welcher Befehl es sein soll ([Kapitel 2, Abschnitt 7.2](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/zwei-fassungen-der-grundbefehle-gnu-und-uutils.html#stufe-7-2)). Eine umbenannte Kopie davon weiß nicht mehr, was sie tun soll:

```console
$ cp /usr/bin/date ./meindatum
$ ./meindatum -d 2026-12-24 +%A
coreutils: unknown program 'meindatum'
$ cp /usr/bin/gnudate ./meindatum2
$ ./meindatum2 -d 2026-12-24 +%A
Thursday
```

Die GNU-Fassung `gnudate` ist ein eigenes Programm und funktioniert auch unter neuem Namen; auf Systemen mit GNU coreutils, etwa Debian, gilt das auch für `date` selbst. Für Versuche dieser Art nimmt man deshalb ein eigenständiges Programm wie `tree`.
:::

⁠**Kurz gesagt:** Das Arbeitsverzeichnis gehört nicht zum Suchpfad; ein Programm dort startet man mit `./`.

:::hintergrund Warum das Arbeitsverzeichnis nicht im Suchpfad steht
Früher war es anders. In der Anleitung zur Bourne-Shell von 1978 durchsucht die Shell ohne eigene Einstellung zuerst das aktuelle Verzeichnis, dann `/bin` und `/usr/bin`, und das Beispiel dort beginnt `PATH` mit einem Doppelpunkt, also mit dem Arbeitsverzeichnis. Heute fehlt es in den Voreinstellungen der Distributionen; auch die Programmbibliothek glibc, auf der fast alle Linux-Programme aufbauen, durchsucht beim Starten anderer Programme seit ihrer Version 2.24 von 2016 das Arbeitsverzeichnis nicht mehr, wenn `PATH` fehlt.

Die Handbücher nennen dafür kaum Gründe. Eine eigene Herleitung ergibt zwei. Erstens soll ein Befehl überall dasselbe Programm meinen: `ls` ist in jedem Verzeichnis `/usr/bin/ls`, egal wo du gerade stehst. Stünde das Arbeitsverzeichnis im Suchpfad, hinge die Bedeutung eines Befehls davon ab, welche Dateien zufällig dort liegen. Zweitens wäre es gefährlich. Legt jemand in ein Verzeichnis, das auch andere betreten, etwa `/tmp`, ein Programm namens `ls`, dann startete jeder, der dort `ls` tippt, dieses fremde Programm, und zwar mit seinen eigenen Rechten. Stünde das Arbeitsverzeichnis am Ende des Suchpfads, gewönne zwar das echte `ls`, doch ein Programm mit dem Namen eines Tippfehlers, etwa `sl`, liefe trotzdem. Die kleine Mühe, `./` zu tippen, ist der Preis für Befehle, die immer dasselbe bedeuten.
:::

### PATH ändern

<span class="anker" id="stufe-5-5"></span>

Für eigene Programme ist `./` auf Dauer lästig, und von einem anderen Verzeichnis aus müsste man den ganzen Pfad tippen. Bequemer ist es, das Verzeichnis mit den eigenen Programmen in den Suchpfad aufzunehmen. Weil `PATH` eine Variable ist, geht das mit einer Zuweisung.

::::beispiel Für einen Befehl und für die ganze Sitzung
Mit einer Zuweisung vor dem Befehl gilt der geänderte Suchpfad nur für diesen einen Befehl:

```console
$ PATH="$PWD:$PATH" meinbaum urlaub
urlaub
├── 2025
│   ├── sommer
│   └── winter
└── 2026
    ├── sommer
    └── winter

7 directories, 0 files
$ meinbaum
meinbaum: command not found
```

`$PWD` setzt das Arbeitsverzeichnis ein, `$PATH` den alten Suchpfad; dazwischen steht ein Doppelpunkt. Danach ist alles wie vorher. Für die ganze Sitzung legt man ein eigenes Verzeichnis für Programme an und setzt es vorn in den Suchpfad:

```console
$ mkdir bin
$ cp /usr/bin/tree bin/baum
$ PATH="$HOME/linuxk5/bin:$PATH"
$ baum urlaub
urlaub
├── 2025
│   ├── sommer
│   └── winter
└── 2026
    ├── sommer
    └── winter

7 directories, 0 files
$ type baum
baum is hashed (/home/student/linuxk5/bin/baum)
```

Ein `export` ist nicht nötig, weil `PATH` schon beim Start der Shell in ihrer Umgebung stand und deshalb markiert ist (Unterabschnitt [4.4](umgebung-und-vererbung.html#stufe-4-4)). `type` meldet, dass die Shell sich den Pfad gemerkt hat. Die Änderung gilt, bis die Shell endet.
::::

Die Zuweisung baut den neuen Wert aus dem alten: Die Parametererweiterung setzt für `$PATH` den bisherigen Text ein, davor stehen das neue Verzeichnis und ein Doppelpunkt. Abbildung [23](#abb-23) zeigt das, und daneben, was geschieht, wenn der alte Text fehlt. Die Stelle, an der man das Verzeichnis einfügt, entscheidet über den Vorrang. Steht es vorn, gewinnen seine Programme auch gegen gleichnamige Programme des Systems; steht es hinten, wie in `PATH="$PATH:$HOME/linuxk5/bin"`, gewinnen die Programme des Systems.

:::abbildung linux/k5pathneu 23
Wie eine Zuweisung den Suchpfad ändert. Oben `PATH="$HOME/linuxk5/bin:$PATH"`: Die Shell setzt für `$PATH` den alten Text ein und stellt das neue Verzeichnis mit einem Doppelpunkt davor; die alten Einträge bleiben und rücken eine Stelle nach hinten. Unten `PATH=/gibtsnicht`: Der alte Text kommt in der Zuweisung nicht vor, und die Liste besteht nur noch aus diesem einen Eintrag.
:::

:::warnung Den Suchpfad nicht beschädigen
Hänge neue Verzeichnisse immer an den alten Wert an, wie oben mit `$PATH`. Eine Zuweisung, die den alten Wert ersetzt, nimmt der Shell alle Programme:

```console
$ PATH=/gibtsnicht ls
Command 'ls' is available in the following places
 * /bin/ls
 * /usr/bin/ls
The command could not be located because '/usr/bin:/bin' is not included in the PATH environment variable.
ls: command not found
$ ls notiz.txt
notiz.txt
```

Hier galt der kaputte Suchpfad nur für einen Befehl, danach funktioniert `ls` wieder. Die ganze Meldung stammt von einem Hilfsprogramm, das Ubuntu für diesen Fall einrichtet: Findet die Shell einen Befehl nicht, ruft sie es auf, und es sucht nach Programmen dieses Namens. Ohne dieses Hilfsprogramm, etwa unter Debian, meldet bash selbst nur `bash: ls: command not found`. Ist der Suchpfad für die ganze Sitzung beschädigt, schließt du das Terminal und öffnest ein neues. Nimm außerdem nie `.` oder einen leeren Eintrag in den Suchpfad auf.
:::

⁠**Kurz gesagt:** Ein eigenes Verzeichnis kommt mit `PATH="verzeichnis:$PATH"` vorn in den Suchpfad; vorn heißt Vorrang, und der alte Wert muss erhalten bleiben.

### Aufgaben zu Abschnitt [5](#stufe-5)

<span class="anker" id="stufe-5-6"></span>

:::aufgabe Aufgabe 17 ★ Den eigenen Suchpfad erkunden
<span class="anker" id="aufg-17"></span>

(a) Wie viele Verzeichnisse stehen in deinem `PATH`? Zähle sie mit einer Pipeline. (b) Welches Verzeichnis durchsucht die Shell zuerst? (c) Wo liegen `tree` und `bash`? Nimm `type -a` und erkläre, warum jedes zweimal erscheint.

:::loesung
```console
$ echo "$PATH" | tr ':' '\n' | wc -l
53
$ echo "$PATH" | tr ':' '\n' | head -n 1
/usr/local/sbin
$ type -a tree bash
tree is /usr/bin/tree
tree is /bin/tree
bash is /usr/bin/bash
bash is /bin/bash
```

(a) `tr` macht aus jedem Doppelpunkt ein Zeilenende, `wc -l` zählt die Zeilen. Auf dem Testsystem sind es 53, weil WSL viele Verzeichnisse von Windows anhängt; auf einem Linux ohne WSL sind es meist acht bis zehn. (b) Das erste ist `/usr/local/sbin`. (c) Beide liegen in `/usr/bin`. Weil `/bin` ein zweiter Name für `/usr/bin` ist und beide im Suchpfad stehen, findet `type -a` jedes Programm zweimal; gestartet wird der erste Treffer.
:::
:::

:::aufgabe Aufgabe 18 ★★ Drei Wege zu einem Programm
<span class="anker" id="aufg-18"></span>

Kopiere `tree` als `meinbaum` in dein Übungsverzeichnis, falls es dort noch nicht liegt. Sage voraus, welche dieser Zeilen das Programm starten, und prüfe es mit dem Unterverzeichnis `urlaub/2025` als Argument: (a) `meinbaum` (b) `./meinbaum` (c) `PATH="$PWD:$PATH" meinbaum` (d) aus deinem Heimatverzeichnis heraus `linuxk5/meinbaum`. Welchen Exit-Status hinterlässt (a)? Warum funktioniert (d), obwohl der Pfad nicht mit `./` beginnt?

:::loesung
```console
$ cp /usr/bin/tree ./meinbaum
$ meinbaum
meinbaum: command not found
$ echo $?
127
$ ./meinbaum urlaub/2025
urlaub/2025
├── sommer
└── winter

3 directories, 0 files
$ PATH="$PWD:$PATH" meinbaum urlaub/2025
urlaub/2025
├── sommer
└── winter

3 directories, 0 files
$ cd ..
$ linuxk5/meinbaum linuxk5/urlaub/2025
linuxk5/urlaub/2025
├── sommer
└── winter

3 directories, 0 files
$ cd linuxk5
```

(a) Ohne Schrägstrich sucht die Shell nur in den Verzeichnissen aus `PATH`; das Übungsverzeichnis gehört nicht dazu. Exit-Status 127. (b) Der Schrägstrich macht aus dem Namen einen Pfad, die Shell startet die Datei direkt. (c) Für diesen einen Befehl steht das Arbeitsverzeichnis vorn im Suchpfad. (d) `linuxk5/meinbaum` enthält einen Schrägstrich, also sucht die Shell nicht, sondern nimmt den relativen Pfad vom Heimatverzeichnis aus. Auf `./` kommt es nicht an, nur auf den Schrägstrich.
:::
:::

:::aufgabe Aufgabe 19 ★★★ Ein falsches cat
<span class="anker" id="aufg-19"></span>

Lege im Übungsverzeichnis ein Verzeichnis `falle` an und kopiere `tree` hinein, diesmal unter dem Namen `cat`. Sage voraus, was `PATH="$PWD/falle:$PATH" cat einkauf.txt` ausgibt, und prüfe es. Was gibt danach `cat einkauf.txt` ohne Zuweisung aus? Erkläre mit dem Ergebnis, was geschähe, wenn das Arbeitsverzeichnis vorn im Suchpfad stünde und jemand eine Datei namens `cat` in ein Verzeichnis legte, das du betrittst.

:::loesung
```console
$ mkdir falle
$ cp /usr/bin/tree falle/cat
$ PATH="$PWD/falle:$PATH" cat einkauf.txt
einkauf.txt  [error opening dir]

0 directories, 1 file
$ cat einkauf.txt
Milch
Brot
Äpfel
Kaffee
```

Für den ersten Befehl steht `falle` vorn im Suchpfad. Die Shell findet dort zuerst eine Datei namens `cat` und startet sie; in Wahrheit ist es `tree`, das `einkauf.txt` als Verzeichnis öffnen will und scheitert. Ohne die Zuweisung gilt wieder der normale Suchpfad, und das echte `cat` zeigt die Liste. Stünde das Arbeitsverzeichnis vorn im Suchpfad, wäre jedes Verzeichnis, das du betrittst, eine solche Falle: Läge dort eine Datei `cat`, liefe sie statt des echten Programms, mit deinen Rechten. Hier war das Programm harmlos; ein fremdes Programm könnte unbemerkt Dateien verändern und danach das echte `cat` aufrufen, sodass du nichts bemerkst.
:::
:::

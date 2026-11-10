---
title: Prozesse und ihre drei Ströme
pfad: Informatik / Linux und Kommandozeile / Ströme, Umleitung, Pipes und Exit-Status
adresse: informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status
knoten: Kapitel 4: Ströme, Umleitung, Pipes und Exit-Status
order: 6090200
summary: Bevor man die Ausgabe eines Programms in eine Datei lenken oder zwei Programme verbinden kann, braucht man ein Bild davon, was ein laufendes Programm ist und auf welchen Wegen Daten hinein- und herauskommen.
tags: Prozess, Prozessnummer, Strom, Ende des Stroms, Standardeingabe, Standardausgabe, Standardfehlerausgabe, Dateideskriptor
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Bevor man die Ausgabe eines Programms in eine Datei lenken oder zwei Programme verbinden kann, braucht man ein Bild davon, was ein laufendes Programm ist und auf welchen Wegen Daten hinein- und herauskommen. Dieser Abschnitt führt den Prozess ein, den Strom, die drei Standardströme jedes Prozesses und die Nummern, unter denen ein Prozess seine Ströme kennt.
:::

### Was du dafür brauchst: Kernel, Shell und Dateien

<span class="anker" id="stufe-1-1"></span>

Dieses Kapitel setzt die [Kapitel 1](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/ein-linux-zum-ueben.html) bis 3 voraus. Daraus brauchst du vor allem diese Dinge.

<ul>

<li>

Der Kernel verwaltet die Hardware und alle Dateien. Ein Programm, das eine Datei öffnen, lesen oder beschreiben will, bittet ihn mit einem Systemaufruf darum ([Kapitel 1, Abschnitt 1.4](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/betriebssystem-kernel-und-distribution.html#stufe-1-4)).

</li>

<li>

Die Shell zerlegt eine Befehlszeile an Leerzeichen in Wörter. Das erste Wort ist der Befehl, die übrigen sind seine Argumente ([Kapitel 2, Abschnitt 2](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/der-aufbau-einer-befehlszeile.html#stufe-2)). Ist der Befehl eine Programmdatei, lässt die Shell das Programm ausführen und wartet, bis es fertig ist; einen eingebauten Befehl wie `cd` erledigt sie selbst ([Kapitel 2, Abschnitte 3.1](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/arten-von-befehlen.html#stufe-3-1) und [3.3](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/arten-von-befehlen.html#stufe-3-3)).

</li>

<li>

Strg+C bricht ein laufendes Programm ab. Strg+D am Anfang einer Zeile meldet einem Programm, das auf Tastatureingaben wartet, das Ende der Eingabe ([Kapitel 2, Abschnitte 5.4](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/schneller-arbeiten-vervollstandigung-verlauf-tastenkurzel.html#stufe-5-4) und [5.5](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/schneller-arbeiten-vervollstandigung-verlauf-tastenkurzel.html#stufe-5-5)).

</li>

<li>

Eine Datei ist eine Folge von Bytes unter einem Namen; eine Textdatei besteht aus Zeilen, und jede Zeile endet mit dem Byte 10, dem Zeilenende ([Kapitel 3, Abschnitte 1.2](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-verzeichnisse-und-der-verzeichnisbaum.html#stufe-1-2) und [4.1](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-ansehen.html#stufe-4-1)). `cat`, `head` und `wc` zeigen und zählen den Inhalt von Dateien ([Kapitel 3, Abschnitt 4](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-ansehen.html#stufe-4)).

</li>

<li>

In `/dev` stehen Gerätedateien, darunter `/dev/null`; in `/proc` erzeugt der Kernel für jedes laufende Programm ein Verzeichnis, dessen Name eine Zahl ist ([Kapitel 3, Abschnitte 7.7](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/die-verzeichnisstruktur-von-linux.html#stufe-7-7) und [7.8](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/die-verzeichnisstruktur-von-linux.html#stufe-7-8)). `mkdir`, `cp`, `mv` und `rm` legen an, kopieren, verschieben und löschen ([Kapitel 3, Abschnitte 5](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-und-verzeichnisse-anlegen.html#stufe-5) und [6](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/kopieren-verschieben-loschen.html#stufe-6)).

</li>

</ul>

::::beispiel Die Bytes einer kleinen Datei
[Kapitel 3](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-verzeichnisse-und-pfade.html) hat die Datei `/etc/hostname` Byte für Byte angesehen. `od -An -tu1` zeigt jedes Byte als Zahl:

```console
$ od -An -tu1 /etc/hostname
 108  97  98 111 114  10
```

Das sind die Buchstaben `l`, `a`, `b`, `o`, `r` und das Zeilenende, zusammen sechs Bytes. Diese sechs Zahlen tauchen in diesem Abschnitt noch einmal auf.
::::

⁠**Kurz gesagt:** Du brauchst den Kernel und seine Systemaufrufe, den Aufbau einer Befehlszeile, Strg+C und Strg+D, Dateien als Folgen von Bytes und die Verzeichnisse `/dev` und `/proc`.

### Der Prozess

<span class="anker" id="stufe-1-2"></span>

Bisher war in dieser Reihe vom „laufenden Programm“ die Rede. Das genügt nicht mehr, sobald dasselbe Programm mehrmals läuft: Öffnest du zwei Terminalfenster und startest in beiden den Editor `nano`, arbeiten zwei Exemplare desselben Programms nebeneinander, jedes mit seiner eigenen Datei und seiner eigenen Stelle im Text. Für ein solches einzelnes Exemplar braucht man ein eigenes Wort.

Als Bild zur Orientierung: Ein Rezept im Kochbuch entspricht dem Programm. Jedes Mal, wenn jemand nach dem Rezept kocht, entsteht ein Kochvorgang mit eigenen Töpfen, eigenen Zutaten und einem eigenen Stand, wie weit er schon ist; zwei Leute können gleichzeitig nach demselben Rezept kochen, ohne sich zu stören. Abbildung [1](#abb-1) zeigt dasselbe für ein Programm.

:::abbildung linux/k4prozess 1
Eine Programmdatei auf dem Datenträger und zwei Prozesse, die aus ihr gestartet wurden. Jeder Prozess hat seinen eigenen Speicher, seine eigenen geöffneten Dateien und sein eigenes Arbeitsverzeichnis. Endet ein Prozess, verschwindet nur er; die Programmdatei bleibt.
:::

:::definition Definition 1.1 (Prozess)
<span class="anker" id="satz-1-1"></span>

Ein __Prozess__ ist ein Programm, das gerade ausgeführt wird, zusammen mit allem, was zu genau dieser Ausführung gehört: seinem eigenen Bereich im Arbeitsspeicher, den Dateien, die es geöffnet hat, und seinem Arbeitsverzeichnis. Der Kernel hält jeden Prozess getrennt von allen anderen. Er gibt jedem Prozess eine Nummer, die __Prozessnummer__.
:::

Ein Programm ist also eine Datei, die auf dem Datenträger liegt; ein Prozess entsteht erst, wenn das Programm gestartet wird, und verschwindet, wenn es endet. Die Shell startet für jedes Programm, das sie ausführen soll, einen neuen Prozess und wartet, bis er endet. Einen eingebauten Befehl führt sie dagegen selbst aus, ohne neuen Prozess. Das erklärt auch, warum `cd` eingebaut sein muss ([Kapitel 2, Abschnitt 3.3](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/arten-von-befehlen.html#stufe-3-3)): Jeder Prozess hat sein eigenes Arbeitsverzeichnis, und ein neuer Prozess könnte nur sein eigenes wechseln, nicht das der Shell.

Die Verzeichnisse in `/proc`, deren Namen Zahlen sind, gehören zu den laufenden Prozessen; die Zahl ist die Prozessnummer. Daneben gibt es den Eintrag `/proc/self`. Er ist ein symbolischer Link ([Kapitel 3, Abschnitt 8.5](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/inode-und-links.html#stufe-8-5)), den der Kernel für jeden Prozess, der ihn liest, auf dessen eigenes Verzeichnis zeigen lässt.

::::beispiel Jeder Befehl ein neuer Prozess
Der Befehl `readlink` zeigt, wohin ein symbolischer Link zeigt. Zweimal hintereinander auf `/proc/self` angewandt:

```console
$ readlink /proc/self
443
$ readlink /proc/self
444
```

Jedes `readlink` hat eine andere Nummer gesehen, nämlich seine eigene: Die Shell hat für jeden Aufruf einen neuen Prozess gestartet. Auf deinem Rechner stehen andere Zahlen da. Der Eintrag `comm` in diesem Verzeichnis enthält den Namen des Programms, die erste Zeile von `status` ebenfalls:

```console
$ cat /proc/self/comm
cat
$ head -n 1 /proc/self/status
Name:   head
```

Wer liest, sieht sich selbst: `cat` findet dort `cat`, `head` findet `head`.
::::

⁠**Kurz gesagt:** Ein Programm ist eine Datei; ein Prozess ist eine laufende Ausführung davon, mit eigenem Speicher, eigenen geöffneten Dateien, eigenem Arbeitsverzeichnis und eigener Nummer.

### Der Strom

<span class="anker" id="stufe-1-3"></span>

Ein Programm wie `cat` soll Text aus einer Datei lesen können, von der Tastatur oder, wie sich zeigen wird, aus anderen Quellen. Es wäre mühsam, wenn es für jede Quelle eigene Befehle bräuchte. Einfacher ist es, wenn alle Quellen für das Programm gleich aussehen: als Bytes, die nacheinander ankommen.

Als Bild zur Orientierung dient ein Förderband. Die Bytes liegen hintereinander darauf und kommen eines nach dem anderen beim Empfänger an. Was vorbei ist, ist vorbei; der Empfänger kann das Band nicht zurückdrehen, und woher das Band kommt, sieht er nicht. Abbildung [2](#abb-2) zeigt das.

:::abbildung linux/k4strom 2
Ein Strom: Bytes laufen der Reihe nach vom schreibenden zum lesenden Prozess. Der Leser sieht nur die Bytes, nicht ihre Herkunft. Kommt nichts mehr, liefert die nächste Leseanfrage null Bytes, und der Leser weiß: Der Strom ist zu Ende.
:::

:::definition Definition 1.2 (Strom, Ende des Stroms)
<span class="anker" id="satz-1-2"></span>

Ein __Strom__ ist eine Folge von Bytes, die ein Prozess der Reihe nach liest oder schreibt. Der Prozess sieht dabei nur die Bytes selbst, nicht, woher sie kommen oder wohin sie gehen. Kommt beim Lesen nichts mehr und kann auch nichts mehr kommen, ist das __Ende des Stroms__ erreicht; der Kernel teilt es dem lesenden Prozess mit, indem eine Leseanfrage null Bytes liefert.
:::

Das Ende des Stroms ist also kein besonderes Zeichen, das im Strom steht, sondern die Antwort „nichts mehr“ auf eine Leseanfrage. [Kapitel 2, Abschnitt 5.5](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/schneller-arbeiten-vervollstandigung-verlauf-tastenkurzel.html#stufe-5-5) hat dasselbe beim Ende der Eingabe gesehen.

::::beispiel Der Strom aus /etc/hostname
`cat /etc/hostname` liest die Datei als Strom. Die erste Leseanfrage liefert die sechs Bytes 108, 97, 98, 111, 114 und 10 aus dem Beispiel in Unterabschnitt [1.1](#stufe-1-1); `cat` schreibt sie weiter, und im Terminal erscheint `labor`. Die zweite Leseanfrage liefert null Bytes. Daran erkennt `cat` das Ende des Stroms und hört auf. [Kapitel 1, Abschnitt 1.4](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/betriebssystem-kernel-und-distribution.html#stufe-1-4) hat genau diese beiden Leseanfragen mit dem Werkzeug `strace` sichtbar gemacht: Die erste lieferte sechs Bytes, die zweite null.
::::

⁠**Kurz gesagt:** Ein Strom ist eine Folge von Bytes, die ein Prozess der Reihe nach liest oder schreibt, ohne ihre Herkunft zu kennen; liefert eine Leseanfrage null Bytes, ist er zu Ende.

### Die Standardeingabe

<span class="anker" id="stufe-1-4"></span>

Viele Programme brauchen Daten. Bekommen sie einen Dateinamen als Argument, lesen sie die Datei. Bekommen sie keinen, müssen sie trotzdem irgendwo lesen. Dafür hat jeder Prozess von Anfang an einen festen Eingang.

:::definition Definition 1.3 (Standardeingabe)
<span class="anker" id="satz-1-3"></span>

Die __Standardeingabe__ (englisch *standard input*, kurz *stdin*) ist der Strom, aus dem ein Prozess liest, wenn ihm nichts anderes gesagt wird. Startet man ein Programm im Terminal, ist seine Standardeingabe das Terminal: Was man tippt, kommt nach der Eingabetaste als Zeile in diesem Strom an.
:::

`cat`, `wc`, `head` und viele andere Programme arbeiten nach derselben Regel: Mit Dateinamen lesen sie diese Dateien, ohne Dateinamen lesen sie ihre Standardeingabe. Startet man sie ohne Argument im Terminal, scheinen sie zu hängen. In Wahrheit warten sie auf Eingaben. Strg+D am Anfang einer Zeile beendet den Strom, und das Programm macht mit dem, was es bekommen hat, ordentlich weiter. Strg+C dagegen bricht das Programm ab; es gibt dann kein Ergebnis aus.

::::beispiel cat ohne Argument
Tippe `cat` und die Eingabetaste, danach `Hallo`, die Eingabetaste, `Welt`, die Eingabetaste und zum Schluss Strg+D:

```console
$ cat
Hallo
Hallo
Welt
Welt
```

Jede Zeile steht zweimal da. Die erste zeigt das Terminal beim Tippen an, die zweite hat `cat` geschrieben, nachdem es die Zeile aus seiner Standardeingabe gelesen hatte. Abbildung [3](#abb-3) verfolgt den Weg einer Zeile. Strg+D selbst erscheint nicht; danach endet `cat`, und die Eingabeaufforderung kommt zurück.

:::abbildung linux/k4cateingabe 3
Der Weg der getippten Zeile `Hallo`: Das Terminal zeigt sie beim Tippen an und schickt sie nach der Eingabetaste in die Standardeingabe von `cat`. `cat` schreibt sie in seine Standardausgabe, und das Terminal zeigt sie ein zweites Mal. Strg+D beendet den Strom, und `cat` endet.
:::
::::

::::beispiel [Zweites Beispiel] wc zählt getippte Zeilen
Tippe `wc -l`, dann die drei Zeilen `Milch`, `Brot`, `Kaffee` und Strg+D:

```console
$ wc -l
Milch
Brot
Kaffee
3
```

Die drei Zeilen hast du getippt. `wc` antwortet erst, wenn der Strom zu Ende ist, denn vorher weiß es nicht, ob noch Zeilen kommen; dann schreibt es die Zahl 3. Da es keinen Dateinamen hatte, steht hinter der Zahl auch keiner. Mit Strg+C statt Strg+D wäre `wc` ohne Ergebnis abgebrochen.
::::

⁠**Kurz gesagt:** Die Standardeingabe ist der Eingang eines Prozesses; im Terminal ist es die Tastatur, und Strg+D beendet den Strom.

### Die Standardausgabe

<span class="anker" id="stufe-1-5"></span>

Ein Programm muss seine Ergebnisse auch loswerden: die Namen, die `ls` findet, den Inhalt, den `cat` liest, die Zahlen, die `wc` zählt. Dafür gibt es einen festen Ausgang.

:::definition Definition 1.4 (Standardausgabe)
<span class="anker" id="satz-1-4"></span>

Die __Standardausgabe__ (englisch *standard output*, kurz *stdout*) ist der Strom, in den ein Prozess seine Ergebnisse schreibt. Startet man ein Programm im Terminal, ist seine Standardausgabe das Terminal, das alles anzeigt, was dort ankommt.
:::

Fast alles, was du in den [Kapiteln 2](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/die-shell-erste-befehle.html) und 3 als Antwort eines Befehls gesehen hast, kam über die Standardausgabe. Auch die zweite Zeile `Hallo` im Beispiel zur Standardeingabe hat `cat` in seine Standardausgabe geschrieben.

::::beispiel echo schreibt seine Argumente
Der eingebaute Befehl `echo` aus [Kapitel 2](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/die-shell-erste-befehle.html) schreibt seine Argumente, durch Leerzeichen getrennt, mit einem Zeilenende in die Standardausgabe:

```console
$ echo Hallo Linux
Hallo Linux
```

`echo` liest nichts; seine Standardeingabe benutzt es nicht, nur den Ausgang.
::::

⁠**Kurz gesagt:** Die Standardausgabe ist der Ausgang für die Ergebnisse eines Prozesses; im Terminal landet sie auf dem Bildschirm.

### Die Standardfehlerausgabe

<span class="anker" id="stufe-1-6"></span>

Nicht alles, was ein Programm schreibt, ist ein Ergebnis. Findet `ls` eine Datei nicht, meldet es das. Diese Meldung gehört nicht zu den Daten, nach denen man gefragt hat. Deshalb hat jeder Prozess einen zweiten Ausgang.

:::definition Definition 1.5 (Standardfehlerausgabe)
<span class="anker" id="satz-1-5"></span>

Die __Standardfehlerausgabe__ (englisch *standard error*, kurz *stderr*) ist ein zweiter Ausgabestrom, in den ein Prozess Fehlermeldungen, Warnungen und Hinweise schreibt. Startet man ein Programm im Terminal, geht auch dieser Strom an das Terminal.
:::

Im Terminal landen also beide Ausgänge auf demselben Bildschirm, und man sieht einer Zeile nicht an, durch welchen sie kam. Abbildung [4](#abb-4) zeigt einen Prozess mit seinen drei Standardströmen, als Bild zur Orientierung gezeichnet wie drei Rohre: eines führt hinein, zwei führen heraus.

:::abbildung linux/k4rohre 4
Ein Prozess mit seinen drei Standardströmen. Die Standardeingabe kommt von der Tastatur, Standardausgabe und Standardfehlerausgabe gehen beide an den Bildschirm. Bei `ls /etc/hostname /gibtsnicht` läuft das Ergebnis durch den einen, die Fehlermeldung durch den anderen Ausgang; am Bildschirm stehen beide Zeilen untereinander.
:::

::::beispiel Ein Ergebnis und eine Fehlermeldung
`ls` bekommt zwei Namen, von denen es nur den ersten gibt:

```console
$ ls /etc/hostname /gibtsnicht
ls: cannot access '/gibtsnicht': No such file or directory
/etc/hostname
```

Die erste Zeile ist eine Fehlermeldung und kam über die Standardfehlerausgabe; die zweite ist das Ergebnis und kam über die Standardausgabe. `ls` meldet Probleme mit den Argumenten zuerst. Am Bildschirm unterscheiden sich die Zeilen nicht; Abschnitt [2](ausgaben-umleiten.html#stufe-2) trennt sie.
::::

⁠**Kurz gesagt:** Die Standardfehlerausgabe ist ein eigener Ausgang für Meldungen; im Terminal mischt sie sich mit der Standardausgabe.

:::hintergrund Warum es einen eigenen Strom für Fehler gibt
In den ersten Jahren von Unix schrieben alle Programme ihre Meldungen in die Standardausgabe. Das war schon lästig, wenn man die Ausgabe in eine Datei schreiben ließ: Mitten zwischen den Daten standen dann Fehlermeldungen, und am Bildschirm sah man nichts davon. Unhaltbar wurde es, als man die Ausgabe eines Programms direkt einem anderen Programm zuführen konnte, denn dieses hielt die Meldung für Daten und verarbeitete sie weiter. Man lebte trotzdem noch einige Jahre damit. Kurz nach der sechsten Ausgabe von Unix, die 1975 erschien, führte Dennis Ritchie dann die Standardfehlerausgabe ein. Seitdem gilt die Arbeitsteilung: Daten in die Standardausgabe, Fehlermeldungen und Hinweise für den Menschen am Terminal in die Standardfehlerausgabe. So bleiben die Daten sauber, und die Meldungen erreichen den Menschen auch dann, wenn die Daten woanders hingehen.
:::

### Der Dateideskriptor

<span class="anker" id="stufe-1-7"></span>

Ein Prozess hat oft mehr als drei Ströme offen: Ein Kopierprogramm liest aus einer Datei und schreibt in eine andere, und daneben hat es noch die drei Standardströme. Bittet es den Kernel, zu lesen oder zu schreiben, muss es angeben, welche seiner offenen Dateien gemeint ist. Dateinamen wären dafür umständlich, denn manche Ströme haben gar keinen Namen.

Als Bild zur Orientierung dient eine Garderobe. Wer seinen Mantel abgibt, bekommt eine Marke mit einer Nummer; später genügt die Nummer, um genau diesen Mantel zu bekommen. Ebenso führt der Kernel für jeden Prozess eine Liste seiner geöffneten Dateien, und der Prozess nennt nur noch die Nummer des Eintrags. Abbildung [5](#abb-5) zeigt eine solche Liste.

:::abbildung linux/k4deskriptoren 5
Die Liste der Deskriptoren eines Prozesses. Die Nummern 0, 1 und 2 führen zum Terminal, die Nummer 3 zu einer Datei, die der Prozess selbst geöffnet hat. Der Prozess nennt dem Kernel beim Lesen und Schreiben nur die Nummer; was dahintersteht, weiß der Kernel.
:::

:::definition Definition 1.6 (Dateideskriptor)
<span class="anker" id="satz-1-6"></span>

Ein __Dateideskriptor__, kurz Deskriptor, ist eine kleine ganze Zahl, unter der der Kernel für einen Prozess eine geöffnete Datei führt. Die drei Standardströme haben feste Nummern: 0 ist die Standardeingabe, 1 die Standardausgabe, 2 die Standardfehlerausgabe. Jede weitere Datei, die der Prozess öffnet, bekommt die kleinste Nummer, die gerade frei ist, also zuerst die 3.
:::

Ein Programm schreibt sein Ergebnis also nicht „auf den Bildschirm“, sondern bittet den Kernel: „Schreibe diese Bytes in Deskriptor 1.“ In [Kapitel 1, Abschnitt 1.4](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/betriebssystem-kernel-und-distribution.html#stufe-1-4) stand genau das in der Ausgabe von `strace`: Die GNU-Fassung von `cat` öffnete `/etc/hostname` und bekam die Nummer 3, las aus Deskriptor 3 und schrieb mit `write(1, …)` in Deskriptor 1.

Woher kommen 0, 1 und 2, wenn ein Programm sie nie selbst geöffnet hat? Ein neuer Prozess übernimmt die geöffneten Deskriptoren des Prozesses, der ihn startet. Bei der Shell im Terminalfenster führen 0, 1 und 2 zum Terminal; jedes Programm, das sie startet, findet diese drei Deskriptoren deshalb schon vor. Im Verzeichnis `fd` unter `/proc/self` steht für jeden Deskriptor ein symbolischer Link mit der Nummer als Namen; er zeigt, wohin der Deskriptor führt.

::::beispiel Die Deskriptoren von ls
```console
$ ls -l /proc/self/fd
total 0
lrwx------ 1 student student 64 Nov 10 05:14 0 -> /dev/pts/2
lrwx------ 1 student student 64 Nov 10 05:14 1 -> /dev/pts/2
lrwx------ 1 student student 64 Nov 10 05:14 2 -> /dev/pts/2
lr-x------ 1 student student 64 Nov 10 05:14 3 -> /proc/454/fd
```

Die Deskriptoren 0, 1 und 2 führen alle zu `/dev/pts/2`. Das ist die Gerätedatei des Terminalfensters, in dem die Shell läuft; auf deinem Rechner steht vielleicht eine andere Zahl am Ende. Deskriptor 3 hat `ls` selbst geöffnet: Es ist das Verzeichnis, dessen Inhalt es gerade auflistet, nämlich `/proc/454/fd`, sein eigenes. Die 3 war die kleinste freie Nummer.
::::

⁠**Kurz gesagt:** Ein Deskriptor ist die Nummer, unter der ein Prozess eine geöffnete Datei beim Kernel anspricht; 0, 1 und 2 sind die drei Standardströme.

:::hintergrund Alles ist eine Datei
Im Beispiel führen die Deskriptoren 0, 1 und 2 zu einer Gerätedatei, Deskriptor 3 zu einem Verzeichnis. Für das Programm macht das keinen Unterschied: Es liest und schreibt immer mit denselben Systemaufrufen und nennt nur die Nummer. Das ist eine Folge des Grundgedankens von Unix, dass fast alles, womit ein Programm arbeitet, als Datei erscheint ([Kapitel 3, Abschnitt 7.7](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/die-verzeichnisstruktur-von-linux.html#stufe-7-7)). Der Kernel sorgt dafür, dass ein Schreibauftrag an ein Terminal, an eine Datei auf der Festplatte oder an `/dev/null` jeweils das Richtige bewirkt. Ein Programm wie `cat` enthält deshalb keine einzige Zeile, die sich um Terminals kümmert; es schreibt in Deskriptor 1, und was dahintersteht, entscheidet jemand anderes.
:::

### Aufgaben zu Abschnitt [1](#stufe-1)

<span class="anker" id="stufe-1-8"></span>

:::aufgabe Aufgabe 1 ★ Programm oder Prozess?
<span class="anker" id="aufg-1"></span>

(a) Auf deinem Rechner liegt die Datei `/usr/bin/nano`. Ist sie ein Programm oder ein Prozess? (b) Du startest `nano` in drei Terminalfenstern. Wie viele Programme und wie viele Prozesse sind beteiligt? (c) Du beendest zwei der drei. Was ist dann noch da? (d) Startet die Shell einen neuen Prozess, wenn du `cd /etc` tippst? Begründe.

:::loesung
(a) Ein Programm: `/usr/bin/nano` ist eine Datei auf dem Datenträger. Solange niemand sie startet, läuft nichts.

(b) Ein Programm und drei Prozesse. Jeder Start erzeugt einen eigenen Prozess mit eigener Nummer, eigenem Speicher und eigener geöffneter Datei; alle drei führen denselben Programmcode aus.

(c) Die Programmdatei und ein Prozess. Die beiden beendeten Prozesse sind verschwunden, die Datei `/usr/bin/nano` bleibt unverändert liegen.

(d) Nein. `cd` ist ein eingebauter Befehl, den die Shell selbst ausführt. Das muss so sein: Jeder Prozess hat sein eigenes Arbeitsverzeichnis, und ein neuer Prozess könnte nur seines wechseln, nicht das der Shell.
:::
:::

:::aufgabe Aufgabe 2 ★★ Lesen bis zum Ende
<span class="anker" id="aufg-2"></span>

(a) Starte `wc -w` ohne Argument, tippe die Zeile `Heute gibt es Kuchen` und dann Strg+D. Was erscheint, und warum erst nach Strg+D? (b) Wiederhole es, beende diesmal aber mit Strg+C. Was ist anders, und warum? (c) Warum hat das Terminal im Beispiel mit `cat` jede Zeile doppelt gezeigt, bei `wc -l` aber nur einmal?

:::loesung
(a) Nach Strg+D erscheint die Zahl 4:

```console
$ wc -w
Heute gibt es Kuchen
4
```

Die Zeile hast du getippt. `wc` zählt die Wörter seines ganzen Stroms und kann das Ergebnis erst schreiben, wenn es weiß, dass nichts mehr kommt, also nach dem Ende des Stroms. Vorher könnten noch weitere Zeilen folgen.

(b) Mit Strg+C erscheint keine Zahl:

```console
$ wc -w
Heute gibt es Kuchen
^C
```

Strg+C beendet den Strom nicht, sondern bricht `wc` ab. Ein abgebrochenes Programm schreibt kein Ergebnis mehr.

(c) `cat` liest jede Zeile und schreibt sie sofort wieder in seine Standardausgabe, also ans Terminal; dort stand sie schon einmal, weil das Terminal Getipptes anzeigt. `wc -l` schreibt die Zeilen nicht zurück, sondern nur am Ende die Zahl.
:::
:::

:::aufgabe Aufgabe 3 ★★ Welche Zeile durch welchen Ausgang?
<span class="anker" id="aufg-3"></span>

Sage für `cat /etc/hostname /gibtsnicht /etc/timezone` voraus, welche Zeilen erscheinen und durch welchen der beiden Ausgänge jede kommt. Prüfe die Zeilen am Rechner. Woran kannst du am Bildschirm allein nicht erkennen, ob deine Zuordnung stimmt?

:::loesung
Vorhersage: `labor` durch die Standardausgabe, dann die Meldung über `/gibtsnicht` durch die Standardfehlerausgabe, dann `Europe/Berlin` durch die Standardausgabe. Am Rechner:

```console
$ cat /etc/hostname /gibtsnicht /etc/timezone
labor
Europe/Berlin
cat: /gibtsnicht: No such file or directory
$ gnucat /etc/hostname /gibtsnicht /etc/timezone
labor
gnucat: /gibtsnicht: No such file or directory
Europe/Berlin
```

Die Zuordnung zu den Ausgängen stimmt, die Reihenfolge am Bildschirm aber nicht bei jeder Fassung. Stand der uutils-Fassung in Ubuntu 26.04: Ihr `cat` sammelt die Meldungen und schreibt sie erst am Ende; die GNU-Fassung, unter Ubuntu 26.04 als `gnucat` aufrufbar, meldet den Fehler an der Stelle, an der er auftritt. Am Bildschirm allein kannst du nicht erkennen, durch welchen Ausgang eine Zeile kam, denn beide führen zum selben Terminal und sehen gleich aus. Beweisen lässt es sich erst mit einer Umleitung, wie in Unterabschnitt [2.3](ausgaben-umleiten.html#stufe-2-3): `cat /etc/hostname /gibtsnicht /etc/timezone 2> /dev/null` zeigt nur noch die beiden Zeilen der Standardausgabe.
:::
:::

:::aufgabe Aufgabe 4 ★★★ Die Deskriptoren nachzählen
<span class="anker" id="aufg-4"></span>

Führe `ls -l /proc/self/fd` zweimal hintereinander aus. (a) Welche Teile der Ausgabe ändern sich, welche bleiben gleich, und warum? (b) Warum hat das Verzeichnis, das `ls` auflistet, die Nummer 3 und nicht etwa 7? (c) Führe danach `cat /proc/self/comm /proc/self/comm` aus und erkläre, warum zweimal derselbe Name erscheint.

:::loesung
(a) Gleich bleiben die Nummern 0 bis 3 und die Ziele der Deskriptoren 0, 1 und 2, nämlich das Terminal. Es ist dasselbe Terminal, weil beide `ls` von derselben Shell gestartet wurden und deren Deskriptoren übernommen haben. Anders sind die Uhrzeit, falls inzwischen eine Minute vergangen ist, und die Zahl im Ziel von Deskriptor 3, etwa `/proc/454/fd` und beim nächsten Mal eine höhere: Jedes `ls` ist ein neuer Prozess mit eigener Nummer und listet sein eigenes Verzeichnis auf.

(b) Ein neuer Prozess bekommt beim Öffnen die kleinste freie Nummer. 0, 1 und 2 sind schon belegt, die 3 ist die kleinste freie. Eine 7 käme nur vor, wenn 3 bis 6 schon belegt wären.

(c)

```console
$ cat /proc/self/comm /proc/self/comm
cat
cat
```

Beide Argumente liest derselbe Prozess, nämlich dieses eine `cat`. `/proc/self` zeigt deshalb beide Male auf dasselbe Verzeichnis, und dort steht der Name `cat`.
:::
:::

---
title: Datenträger und Einhängen
pfad: Informatik / Linux und Kommandozeile / Dateien, Verzeichnisse und Pfade
adresse: informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade
knoten: Kapitel 3: Dateien, Verzeichnisse und Pfade
order: 6081000
summary: Der eine Verzeichnisbaum aus Abschnitt 1 setzt sich aus mehreren Dateisystemen zusammen, die an Verzeichnissen eingehängt sind.
tags: lsblk, findmnt, df, /mnt/c
lang: de
---

<span class="anker" id="stufe-9"></span>

:::zweck
Der eine Verzeichnisbaum aus Abschnitt [1](dateien-verzeichnisse-und-der-verzeichnisbaum.html#stufe-1) setzt sich aus mehreren Dateisystemen zusammen, die an Verzeichnissen eingehängt sind. Dieser Abschnitt zeigt, wie man sieht, welche Datenträger es gibt, welches Dateisystem wo hängt und wie voll es ist, und was das für WSL 2 und das Windows-Laufwerk bedeutet. Alle Befehle hier lesen nur.
:::

:::::vorwissen Was du dafür brauchst: Datenträger, Dateisystem und Einhängen

<span class="anker" id="stufe-9-1"></span>

[Kapitel 1](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/ein-linux-zum-ueben.html) hat die Begriffe eingeführt, die dieser Abschnitt braucht. Ein Datenträger ist ein Gerät, das Daten dauerhaft speichert, etwa eine SSD oder ein USB-Stick, und er ist in Sektoren zu meist 512 Byte eingeteilt ([Kapitel 1, Abschnitt 5.1](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/datentrager-abbild-und-prufsumme.html#stufe-5-1)). Eine Partition ist ein zusammenhängender Bereich eines Datenträgers, der wie ein eigener Datenträger behandelt wird ([Kapitel 1, Abschnitt 5.2](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/datentrager-abbild-und-prufsumme.html#stufe-5-2)). Ein Dateisystem ist die Ordnung, nach der Dateien, Verzeichnisse und ihre Verwaltung auf einem Datenträger oder einer Partition abgelegt sind, unter Linux meist ext4 ([Kapitel 1, Abschnitt 5.3](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/datentrager-abbild-und-prufsumme.html#stufe-5-3)). Einhängen schließlich heißt, ein Dateisystem an ein vorhandenes Verzeichnis des Baums anzuhängen; dieses Verzeichnis heißt Einhängepunkt, und unter ihm erscheint der Inhalt des Dateisystems ([Kapitel 1, Abschnitt 8.1](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/das-live-system.html#stufe-8-1)).

::::beispiel Ein USB-Stick im Baum
Ein USB-Stick mit einem Dateisystem darauf erscheint zunächst als Gerätedatei, etwa `/dev/sdb1` für seine erste Partition. Seine Dateien sieht man erst, wenn das Dateisystem eingehängt ist, auf einem Ubuntu mit grafischer Oberfläche zum Beispiel unter `/media/student/STICK`. Eine Datei `urlaub.jpg` auf dem Stick hat dann den Pfad `/media/student/STICK/urlaub.jpg`. Abbildung [34](#abb-34) zeigt den Vorgang.

:::abbildung linux/k3einhaengen 34
Einhängen eines USB-Sticks. Links der Baum vorher, mit dem leeren Verzeichnis `/media/student/STICK`; rechts daneben das Dateisystem des Sticks mit eigener Wurzel. Beim Einhängen wird die Wurzel des Sticks an das Verzeichnis gesetzt, und seine Dateien erscheinen darunter. Nach dem Aushängen ist das Verzeichnis wieder leer.
:::
::::

⁠**Kurz gesagt:** Datenträger tragen Dateisysteme, und eingehängte Dateisysteme bilden zusammen den einen Baum.

:::::

### Die Datenträger anzeigen: lsblk

<span class="anker" id="stufe-9-2"></span>

Bevor man fragt, wo ein Dateisystem hängt, will man wissen, welche Datenträger überhaupt angeschlossen sind. [Kapitel 1, Abschnitte 8.1](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/das-live-system.html#stufe-8-1) und [9.7](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/der-live-usb-stick-vorbereiten-schreiben-starten.html#stufe-9-7), hat dafür einen Befehl als Rezept benutzt; jetzt lässt sich seine Ausgabe vollständig lesen.

:::definition Definition 9.1 (lsblk)
<span class="anker" id="satz-9-1"></span>

Der Befehl __lsblk__ (kurz für „list block devices“) listet die Datenträger und ihre Partitionen, also die Gerätedateien der Art `b`, mit Größe, Art und den Verzeichnissen, an denen ihre Dateisysteme eingehängt sind.
:::

Die Spalten bedeuten: `NAME` der Name der Gerätedatei in `/dev`; `MAJ:MIN` die beiden Gerätenummern, die auch `ls -l` zeigt; `RM` eine 1 für wechselbare Datenträger wie USB-Sticks; `SIZE` die Größe mit Einheiten zu 1024; `RO` eine 1 für nur lesbare Datenträger; `TYPE` `disk` für einen ganzen Datenträger, `part` für eine Partition; `MOUNTPOINTS` die Einhängepunkte.

::::beispiel Die Datenträger von WSL 2
```console
$ lsblk
NAME MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
sda    8:0    0 388.6M  1 disk
sdb    8:16   0   186M  1 disk
sdc    8:32   0     8G  0 disk [SWAP]
sdd    8:48   0     1T  0 disk /mnt/wslg/distro
                               /
```

`sda` und `sdb` sind kleine, nur lesbare Abbilder, die WSL selbst mitbringt. `sdc` ist der Auslagerungsspeicher, in den Linux Teile des Arbeitsspeichers schreibt, wenn er knapp wird; er ist nicht eingehängt, sondern als `[SWAP]` in Gebrauch. `sdd` ist dein Ubuntu: 1 TiB groß, wie `/sys/block/sdd/size` in Unterabschnitt [7.8](die-verzeichnisstruktur-von-linux.html#stufe-7-8) ergab, eingehängt unter `/` und ein zweites Mal, nur lesbar, für die grafischen Programme von WSL. Partitionen gibt es hier nicht; WSL legt das Dateisystem direkt auf den ganzen virtuellen Datenträger. Auf einem gewöhnlichen PC sähe man zum Beispiel `nvme0n1` mit Partitionen `nvme0n1p1`, `nvme0n1p2` und so weiter.
::::

⁠**Kurz gesagt:** `lsblk` zeigt Datenträger und Partitionen mit Größe und Einhängepunkt.

### Was wo eingehängt ist: findmnt

<span class="anker" id="stufe-9-3"></span>

`lsblk` zeigt nur Datenträger. Zum Baum gehören aber auch Dateisysteme ohne Datenträger, etwa `/proc` oder `/tmp`. Um für einen beliebigen Pfad zu erfahren, in welchem Dateisystem er liegt, braucht man ein anderes Werkzeug.

:::definition Definition 9.2 (findmnt)
<span class="anker" id="satz-9-2"></span>

Der Befehl __findmnt__ listet die eingehängten Dateisysteme mit Einhängepunkt (`TARGET`), Quelle (`SOURCE`), Art (`FSTYPE`) und Einstellungen (`OPTIONS`). Mit `-T pfad` nennt er nur das Dateisystem, in dem der Pfad liegt, mit `-t art` nur Dateisysteme einer Art, und mit `-o` wählt man die Spalten.
:::

Ohne Argumente zeigt `findmnt` alle eingehängten Dateisysteme als Baum; unter WSL 2 sind das mehrere Dutzend. Der ältere Befehl `mount` ohne Argumente gibt dieselbe Liste in je einer langen Zeile aus.

::::beispiel Drei Pfade, drei Dateisysteme
```console
$ findmnt -T ~ -o TARGET,SOURCE,FSTYPE
TARGET SOURCE   FSTYPE
/      /dev/sdd ext4
$ findmnt -T /mnt/c -o TARGET,SOURCE,FSTYPE
TARGET SOURCE FSTYPE
/mnt/c C:\    9p
$ findmnt -T /tmp -o TARGET,SOURCE,FSTYPE
TARGET SOURCE FSTYPE
/tmp   tmpfs  tmpfs
```

Dein Heimatverzeichnis liegt im ext4-Dateisystem auf `/dev/sdd`, das an der Wurzel hängt. `/mnt/c` ist das Laufwerk C: von Windows, eingehängt mit der Art 9p. `/tmp` ist ein tmpfs im Arbeitsspeicher, ohne Datenträger dahinter.
::::

::::beispiel [Zweites Beispiel] Alle Dateisysteme auf Datenträgern
```console
$ findmnt -t ext4,9p -o TARGET,SOURCE,FSTYPE
TARGET                 SOURCE   FSTYPE
/                      /dev/sdd ext4
├─/usr/lib/wsl/drivers drivers  9p
├─/mnt/wslg/distro     /dev/sdd ext4
└─/mnt/c               C:\      9p
```

Die Linien zeigen, unter welchem Einhängepunkt ein anderer liegt: Alle drei hängen unterhalb der Wurzel. `/usr/lib/wsl/drivers` reicht Treiber von Windows nach Linux durch.
::::

⁠**Kurz gesagt:** `findmnt` zeigt, welches Dateisystem an welchem Verzeichnis hängt; `findmnt -T pfad` beantwortet die Frage für einen einzelnen Pfad.

:::hintergrund Was mit dem Inhalt des Einhängepunkts geschieht
Ein Einhängepunkt ist ein gewöhnliches Verzeichnis und kann vorher Dateien enthalten. Beim Einhängen werden sie nicht gelöscht, sondern verdeckt: Solange das fremde Dateisystem eingehängt ist, führt der Pfad des Verzeichnisses zu dessen Wurzel, und die alten Einträge sind unerreichbar. Nach dem Aushängen sind sie wieder da. Der Kernel erreicht das bei der Auflösung eines Pfads (Unterabschnitt [8.2](inode-und-links.html#stufe-8-2)): Er führt eine Tabelle der Einhängepunkte, und trifft er auf einen davon, springt er zur Wurzel des eingehängten Dateisystems, statt in der Tabelle des Verzeichnisses weiterzulesen. Deshalb nimmt man als Einhängepunkt meist ein leeres Verzeichnis.
:::

:::hintergrund Wie ein USB-Stick in den Baum kommt
Auf einem Linux mit grafischer Oberfläche hängt ein Hilfsprogramm einen eingesteckten Stick von selbst ein, meist unter `/media/<benutzer>/<name des Sticks>`. Von Hand braucht man dazu Verwalterrechte: `sudo mount /dev/sdb1 /mnt` hängt die erste Partition des Sticks unter `/mnt` ein, `sudo umount /mnt` hängt sie wieder aus. Das Aushängen vor dem Abziehen ist wichtig: Linux schreibt Änderungen oft erst mit etwas Verzögerung auf den Datenträger, und erst beim Aushängen ist sicher, dass alles angekommen ist. Unter WSL 2 erscheinen USB-Sticks nicht als Datenträger in Linux ([Kapitel 1, Abschnitt 4.8](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/wsl-2-linux-neben-windows.html#stufe-4-8)); ihre Dateien bearbeitet man dort am einfachsten von Windows aus.
:::

### Wie voll ein Dateisystem ist: df mit Pfaden

<span class="anker" id="stufe-9-4"></span>

[Kapitel 2, Abschnitt 6.5](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/das-system-erkunden.html#stufe-6-5) hat mit `df -h /` gezeigt, wie viel Platz auf dem Datenträger des Systems frei ist. Mit dem Wissen über eingehängte Dateisysteme kann man dieselbe Frage für jeden Ort im Baum stellen. Abbildung [35](#abb-35) zeigt, aus welchen Dateisystemen der Baum unter WSL 2 besteht.

:::abbildung linux/k3wslbaum 35
Der Baum von WSL 2 aus drei Dateisystemen zusammengesetzt: das ext4-Dateisystem auf `/dev/sdd` als Grundstock, das tmpfs unter `/tmp` im Arbeitsspeicher und das Laufwerk C: unter `/mnt/c`. Jeder Teilbaum ist in der Farbe seines Dateisystems hinterlegt.
:::

:::definition Definition 9.3 (df mit Pfaden)
<span class="anker" id="satz-9-3"></span>

Bekommt __df__ Pfade als Argumente, zeigt es für jeden Pfad das Dateisystem, in dem er liegt, mit Größe, belegtem und freiem Platz. Die Option `-T` fügt die Art des Dateisystems hinzu.
:::

Für einen Pfad zählt also nicht, wo er im Baum steht, sondern auf welchem Dateisystem er liegt. Zwei Verzeichnisse direkt nebeneinander können auf verschiedenen Datenträgern liegen und verschieden viel Platz haben.

::::beispiel Platz an drei Orten
```console
$ df -hT ~ /tmp /mnt/c
Filesystem     Type   Size  Used Avail Use% Mounted on
/dev/sdd       ext4  1007G  4.2G  952G   1% /
tmpfs          tmpfs   16G     0   16G   0% /tmp
C:\            9p     475G  319G  156G  68% /mnt/c
```

Das Heimatverzeichnis hat 952 GiB frei, `/tmp` nur 16 GiB, denn es lebt im Arbeitsspeicher und darf höchstens die Hälfte davon belegen. Für `/mnt/c` meldet `df` die Belegung des Windows-Laufwerks. Dass das Dateisystem auf `/dev/sdd` nur 1007 GiB statt 1024 groß ist, liegt an seiner eigenen Verwaltung, die einen Teil des Datenträgers belegt; die Reserve für `root` aus [Kapitel 2, Abschnitt 6.5](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/das-system-erkunden.html#stufe-6-5) kommt beim freien Platz noch hinzu.
::::

⁠**Kurz gesagt:** `df -hT pfad` zeigt Art, Größe und freien Platz des Dateisystems, in dem ein Pfad liegt.

### Das Windows-Laufwerk unter WSL 2: /mnt/c

<span class="anker" id="stufe-9-5"></span>

Unter WSL 2 gehört zum Baum ein Dateisystem, das gar nicht in Linux liegt: das Laufwerk C: von Windows. Es verhält sich in mehreren Punkten anders als der Rest des Baums.

:::abbildung linux/k3grenze 36
Grenzen zwischen Dateisystemen. Ein harter Link von `/home/student` nach `/tmp` oder `/mnt/c` prallt an der Grenze ab; ein symbolischer Link überquert sie, weil er nur einen Pfad enthält; `mv` über die Grenze wird zu Kopieren und Löschen.
:::

:::definition Definition 9.4 (/mnt/c unter WSL 2)
<span class="anker" id="satz-9-4"></span>

Unter WSL 2 hängt das Laufwerk C: von Windows unter __/mnt/c__, als Dateisystem der Art 9p. Jeder Zugriff darauf wird als Anfrage an einen Dateiserver in Windows weitergereicht, der die Datei auf dem Windows-Laufwerk liest oder schreibt.
:::

Daraus folgen die Eigenheiten, die [Kapitel 1, Abschnitte 4.5](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/wsl-2-linux-neben-windows.html#stufe-4-5) und [4.7](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/wsl-2-linux-neben-windows.html#stufe-4-7) schon genannt hat. Zugriffe sind langsamer, besonders bei vielen kleinen Dateien, weil jede Anfrage den Weg zwischen Linux und Windows nimmt. Es gelten die Regeln von Windows für Namen, und Groß- und Kleinschreibung werden nicht unterschieden. Und weil `/mnt/c` ein eigenes Dateisystem ist, gelten die Grenzen aus diesem Kapitel: Ein harter Link von deinem Heimatverzeichnis dorthin ist unmöglich, und `mv` zwischen beiden kopiert und löscht, statt nur einen Eintrag umzuhängen. Abbildung [36](#abb-36) fasst die Grenzen zusammen.

::::beispiel Woran man die Grenze erkennt
Ob zwei Pfade im selben Dateisystem liegen, verrät `findmnt -T` oder `df`: Steht in der Spalte `TARGET` beziehungsweise `Mounted on` ein anderer Einhängepunkt, liegt eine Grenze dazwischen. Für `~` und `/mnt/c` zeigte das Beispiel in Unterabschnitt [9.4](#stufe-9-4) die Einhängepunkte `/` und `/mnt/c`. Ein harter Link von `~/linuxk3/einkauf.txt` nach `/mnt/c` muss deshalb aus demselben Grund scheitern wie der nach `/tmp` in Unterabschnitt [8.7](inode-und-links.html#stufe-8-7).
::::

⁠**Kurz gesagt:** `/mnt/c` ist unter WSL 2 ein eigenes Dateisystem mit den Regeln von Windows; für Linux-Arbeit gehört alles ins Heimatverzeichnis.

### Aufgaben zu Abschnitt [9](#stufe-9)

<span class="anker" id="stufe-9-6"></span>

:::aufgabe Aufgabe 31 ★ Eine Ausgabe von lsblk lesen
<span class="anker" id="aufg-31"></span>

Ein Notebook zeigt unter `lsblk` unter anderem die Zeilen `nvme0n1 259:0 0 476.9G 0 disk`, darunter `nvme0n1p1 259:1 0 260M 0 part /boot/efi` und `nvme0n1p2 259:2 0 476.6G 0 part /`, außerdem `sda 8:0 1 7.5G 0 disk` mit `sda1 8:1 1 7.5G 0 part /media/mira/STICK`. Wie viele Datenträger und wie viele Partitionen sind es? Welcher Datenträger ist wechselbar? Wo erscheinen die Dateien des Sticks im Baum?

:::loesung
Es sind zwei Datenträger mit `TYPE disk`: `nvme0n1` mit 476,9 GiB und `sda` mit 7,5 GiB. Dazu kommen drei Partitionen: `nvme0n1p1`, `nvme0n1p2` und `sda1`. Wechselbar ist `sda`, erkennbar an der 1 in der Spalte `RM`; es ist ein USB-Stick. Seine einzige Partition ist unter `/media/mira/STICK` eingehängt, also liegen seine Dateien dort, etwa `/media/mira/STICK/urlaub.jpg`. Die große Partition `nvme0n1p2` hängt an der Wurzel und trägt das System.
:::
:::

:::aufgabe Aufgabe 32 ★★ Welches Dateisystem?
<span class="anker" id="aufg-32"></span>

Bestimme mit `findmnt -T pfad -o TARGET,SOURCE,FSTYPE` für `/proc`, `/home/student/linuxk3`, `/tmp` und `/usr/bin`, in welchem Dateisystem sie liegen. Welche davon liegen auf einem Datenträger, welche nicht? Zwischen welchen der vier Orte ist ein harter Link möglich?

:::loesung
`/home/student/linuxk3` und `/usr/bin` liegen beide im ext4-Dateisystem auf `/dev/sdd`, das an `/` hängt (Beispiel in Unterabschnitt [9.3](#stufe-9-3)). `/tmp` ist ein tmpfs im Arbeitsspeicher, `/proc` ein virtuelles Dateisystem ohne Datenträger:

```console
$ findmnt -T /proc -o TARGET,SOURCE,FSTYPE
TARGET SOURCE FSTYPE
/proc  proc   proc
```

Auf einem Datenträger liegen also nur die ersten beiden. Ein harter Link ist nur zwischen `/home/student/linuxk3` und `/usr/bin` technisch möglich, weil nur sie im selben Dateisystem liegen. Anlegen kannst du ihn trotzdem nicht: In `/usr/bin` darf ein gewöhnlicher Benutzer keine Einträge anlegen, und Ubuntu verbietet in seiner Voreinstellung außerdem harte Links auf Dateien, die einem anderen Benutzer gehören und die man nicht zugleich lesen und beschreiben darf.
:::
:::

:::aufgabe Aufgabe 33 ★★ Hart nein, symbolisch ja
<span class="anker" id="aufg-33"></span>

`ln einkauf.txt /tmp/einkauf.txt` scheiterte in Unterabschnitt [8.7](inode-und-links.html#stufe-8-7). Würde `ln -s ~/linuxk3/einkauf.txt /tmp/einkauf.txt` funktionieren? Begründe mit dem, was in der neuen Datei stünde. Was wäre auf dem Testsystem nach einem Neustart mit dem Link geschehen, und was mit der Einkaufsliste?

:::loesung
Ja. Der symbolische Link wäre eine neue kleine Datei in `/tmp`, deren Inhalt der Text `/home/student/linuxk3/einkauf.txt` ist; die Shell hat die Tilde vorher ersetzt. Ein Pfad darf über jede Grenze zwischen Dateisystemen führen, denn er wird erst beim Zugriff aufgelöst. Auf dem Testsystem liegt `/tmp` im Arbeitsspeicher; nach einem Neustart wäre der Link deshalb verschwunden, die Einkaufsliste aber unberührt, denn ein symbolischer Link ist keine Verbindung, die sein Ziel kennt. Das Kapitel hat diesen Link nicht angelegt, um außerhalb des Übungsverzeichnisses nichts zu verändern.
:::
:::

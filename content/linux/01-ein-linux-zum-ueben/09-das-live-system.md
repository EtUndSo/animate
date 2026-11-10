---
title: Das Live-System
pfad: Informatik / Linux und Kommandozeile / Ein Linux zum Üben: WSL, virtuelle Maschine, Live-USB-Stick
adresse: informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick
knoten: Kapitel 1: Ein Linux zum Üben: WSL, virtuelle Maschine, Live-USB-Stick
order: 6060900
summary: Ein Linux, das vom USB-Stick startet, benutzt die eingebaute SSD nicht, und trotzdem kann man darin Dateien anlegen und Programme ausprobieren.
tags: Einhängen, Einhängepunkt, Live-System, squashfs, tmpfs, Overlay, Persistenz
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Ein Linux, das vom USB-Stick startet, benutzt die eingebaute SSD nicht, und trotzdem kann man darin Dateien anlegen und Programme ausprobieren. Dieser Abschnitt erklärt, wie das geht: Das System liegt in einem schreibgeschützten Abbild, und alles, was sich ändert, landet in einer Schicht im Arbeitsspeicher. Daraus folgt auch, warum nach dem Ausschalten alles weg ist.
:::

### Was du dafür brauchst: das Einhängen

<span class="anker" id="stufe-8-1"></span>

Unterabschnitt [4.5](wsl-2-linux-neben-windows.html#stufe-4-5) hat gezeigt, dass Linux alle Dateien in einem einzigen Baum mit der Wurzel `/` anordnet und das Laufwerk C: von Windows unter `/mnt/c` zeigt. Wie kommt der Inhalt eines Datenträgers an eine Stelle in diesem Baum?

:::definition Definition 8.1 (Einhängen, Einhängepunkt)
<span class="anker" id="satz-8-1"></span>

__Einhängen__ heißt, ein Dateisystem an einer Stelle im Verzeichnisbaum sichtbar zu machen: Ab dann zeigt der Ordner an dieser Stelle den Inhalt des Dateisystems. Der Ordner heißt __Einhängepunkt__. Ein Dateisystem, das nirgends eingehängt ist, benutzen die Programme nicht; sie lesen und schreiben dort keine Dateien.
:::

::::beispiel Die Datenträger in WSL 2
Der Befehl `lsblk` listet die Datenträger, die der Kernel sieht, mit ihrer Größe und ihrem Einhängepunkt:

```console Linux (WSL 2)
$ lsblk -o NAME,SIZE,TYPE,MOUNTPOINTS
NAME   SIZE TYPE MOUNTPOINTS
sda  388.6M disk
sdb    186M disk
sdc      8G disk [SWAP]
sdd      1T disk /mnt/wslg/distro
                 /
```

Linux nennt Datenträger `sda`, `sdb` und so weiter. Alle vier sind virtuelle Festplatten der VM von WSL 2. Das Dateisystem auf `sdd`, die ext4-Datei aus Unterabschnitt [4.6](wsl-2-linux-neben-windows.html#stufe-4-6), ist an der Wurzel `/` eingehängt und zusätzlich an einer zweiten Stelle; es enthält das ganze Ubuntu. `sda` und `sdb` haben in Ubuntu keinen Einhängepunkt; WSL braucht sie für eigene Zwecke außerhalb der Distribution. `sdc` enthält kein Dateisystem: `[SWAP]` steht für einen Bereich, in den der Kernel Teile des Arbeitsspeichers auslagern kann, und den benutzt er ohne Einhängen. Laufwerk C: steht nicht in der Liste, denn es ist kein Datenträger der VM; es kommt über den Dateiserver aus Abbildung [8](wsl-2-linux-neben-windows.html#abb-8) von der Windows-Seite und ist unter `/mnt/c` eingehängt.
::::

⁠**Kurz gesagt:** Ein Dateisystem wird an einem Ordner eingehängt; was nirgends eingehängt ist, benutzt kein Programm.

### Das Live-System

<span class="anker" id="stufe-8-2"></span>

Ein Linux soll vom Stick starten, vollständig benutzbar sein und die interne SSD nicht anrühren. Dateien anlegen soll man trotzdem können, und das System soll sich nach jedem Start wieder frisch zeigen.

Abbildung [11](#abb-11) zeigt, wie ein Live-System das erreicht: mit zwei Schichten, die das System übereinanderlegt.

:::abbildung linux/k1live 11
Die Schichten eines Live-Systems. Unten liegt das System als komprimiertes, schreibgeschütztes Abbild vom Stick, darüber eine beschreibbare Schicht im Arbeitsspeicher. Beide zusammen ergeben den Verzeichnisbaum, den die Programme sehen. Die interne SSD ist nicht eingehängt.
:::

:::definition Definition 8.2 (Live-System)
<span class="anker" id="satz-8-2"></span>

Ein __Live-System__ ist ein Betriebssystem, das vollständig von einem Wechseldatenträger startet und läuft, ohne die eingebauten Datenträger des Rechners einzuhängen. Sein System liegt schreibgeschützt auf dem Wechseldatenträger; alle Änderungen während der Sitzung landen im Arbeitsspeicher.
:::

::::beispiel Ubuntu ausprobieren
Startet man einen Ubuntu-Stick und wählt im Installationsprogramm „Ubuntu ausprobieren“, läuft Ubuntu als Live-System. Man kann im Browser surfen, Dateien anlegen und das Terminal benutzen. Die SSD mit Windows bleibt dabei unberührt, und nach dem Neustart ohne Stick startet Windows wie vorher.
::::

⁠**Kurz gesagt:** Ein Live-System läuft vom Stick und aus dem Arbeitsspeicher und lässt die interne SSD in Ruhe.

### Das komprimierte Abbild: squashfs

<span class="anker" id="stufe-8-3"></span>

Ein vollständiges Ubuntu mit Browser, Büroprogrammen und Treibern belegt viele Gigabyte. Damit es auf einen Stick passt und schnell gelesen wird, legt man es zusammengepresst in einer Datei ab.

:::definition Definition 8.3 (squashfs)
<span class="anker" id="satz-8-3"></span>

__squashfs__ ist ein Dateisystem, das seinen ganzen Inhalt in einer einzigen Datei komprimiert ablegt und sich nur lesen, nicht beschreiben lässt. Es wird einmal beim Bau des Abbilds erzeugt.
:::

::::beispiel squashfs auf dem Ubuntu-Stick
Im Abbild von Ubuntu liegt im Ordner `casper` das System in squashfs-Dateien. Beim Start hängt das Live-System sie ein, und von da an liest es jedes Programm, das man startet, aus dem komprimierten Abbild, entpackt Stück für Stück im Arbeitsspeicher. Ändern lässt sich darin nichts.
::::

⁠**Kurz gesagt:** squashfs ist ein komprimiertes Dateisystem, das man nur lesen kann.

:::hintergrund Warum ein komprimiertes Dateisystem schreibgeschützt ist
Der Grund steckt im Aufbau. squashfs komprimiert die Dateien in Blöcken, standardmäßig zu je 128 KiB, und legt die komprimierten Blöcke lückenlos hintereinander ab. Wie viel Platz ein Block danach braucht, hängt von seinem Inhalt ab. Ändert man in einer Datei ein paar Byte, wird ihr komprimierter Block fast immer länger oder kürzer. Dann passt er nicht mehr an seine alte Stelle, und alle folgenden Blöcke samt den Verweisen auf sie müssten verschoben werden. Ein Dateisystem, das nie geändert wird, kann sich dagegen die dichteste Anordnung leisten, und genau das braucht man für ein System, das auf einen Stick passen und unverändert bleiben soll. Beschreibbare Dateisysteme mit Kompression gibt es auch; sie lassen dafür Platz zwischen den Blöcken frei oder schreiben geänderte Blöcke an eine neue Stelle und verwalten den Platz entsprechend aufwendiger.
:::

### Ein Dateisystem im Arbeitsspeicher: tmpfs

<span class="anker" id="stufe-8-4"></span>

Wenn das System selbst nicht beschreibbar ist und die SSD tabu, braucht ein Live-System einen anderen Ort für alles, was sich ändert: neue Dateien, geänderte Einstellungen, Protokolle.

:::definition Definition 8.4 (tmpfs)
<span class="anker" id="satz-8-4"></span>

__tmpfs__ ist ein Dateisystem, dessen Dateien im Arbeitsspeicher liegen. Es lässt sich lesen und beschreiben wie jedes andere Dateisystem. Sein Inhalt verschwindet, sobald es ausgehängt oder der Rechner ausgeschaltet wird.
:::

::::beispiel tmpfs in WSL
Auch ein gewöhnliches Linux benutzt tmpfs, etwa für Dateien, die nur bis zum nächsten Neustart gebraucht werden. In WSL 2 ist zum Beispiel der Ordner `/run` ein tmpfs. Wie viel Arbeitsspeicher ein tmpfs höchstens belegen darf, legt man beim Einhängen fest; es belegt aber nur so viel, wie seine Dateien tatsächlich brauchen.
::::

⁠**Kurz gesagt:** tmpfs ist ein Dateisystem im Arbeitsspeicher, beschreibbar und flüchtig.

### Zwei Schichten übereinander: das Overlay

<span class="anker" id="stufe-8-5"></span>

Jetzt hat das Live-System zwei Dateisysteme: das System im squashfs, das man nur lesen kann, und ein leeres tmpfs, in das man schreiben kann. Die Programme sollen aber einen einzigen Verzeichnisbaum sehen, in dem das System steht und in dem man trotzdem alles ändern kann.

:::definition Definition 8.5 (Overlay)
<span class="anker" id="satz-8-5"></span>

Ein __Overlay__ legt zwei Dateisysteme übereinander und zeigt sie als eines: eine untere, nur lesbare Schicht und eine obere, beschreibbare Schicht. Beim Lesen einer Datei schaut es zuerst in der oberen Schicht nach und, wenn die Datei dort fehlt, in der unteren. Soll eine Datei der unteren Schicht geändert werden, kopiert es sie zuerst in die obere und ändert dort die Kopie. Wird eine Datei der unteren Schicht gelöscht, trägt es in der oberen Schicht eine Markierung ein, die die Datei verdeckt. Die untere Schicht bleibt in jedem Fall unverändert.
:::

::::beispiel Drei Dateien im Live-System
Die untere Schicht ist das squashfs des Systems, die obere ein tmpfs. (1) Du legst die neue Datei `notiz.txt` an: Sie entsteht nur in der oberen Schicht. (2) Du änderst eine Einstellungsdatei des Systems: Das Overlay kopiert sie aus dem squashfs in das tmpfs und ändert die Kopie; ab jetzt sehen alle Programme die geänderte Fassung, denn die obere Schicht hat Vorrang. (3) Du löschst eine Datei des Systems: In der oberen Schicht entsteht eine Markierung, und die Datei ist nicht mehr zu sehen, obwohl sie im squashfs weiter vorhanden ist. Nach einem Neustart ist das tmpfs leer, und alle drei Änderungen sind verschwunden.
::::

⁠**Kurz gesagt:** Das Overlay zeigt eine nur lesbare und eine beschreibbare Schicht als einen Baum; alle Änderungen landen oben.

:::hintergrund Wer die Schichten beim Start zusammensetzt
Wenn der Bootloader den Kernel startet, lädt er zusätzlich ein kleines Dateisystem in den Arbeitsspeicher, das *initramfs*. Darin läuft ein Programm, das die Schichten aufbaut, bevor das eigentliche System startet; bei Ubuntu heißt es `casper`. Es sucht den Datenträger, auf dem das Live-System liegt, hängt dessen squashfs-Dateien ein, legt ein tmpfs an und verbindet beides zu einem Overlay. Dieses Overlay macht es zur Wurzel `/` des Systems und übergibt an das erste Programm des eigentlichen Systems. Für alle Programme, die danach starten, sieht das Live-System aus wie ein gewöhnlich installiertes Linux.
:::

### Was beim Ausschalten geschieht

<span class="anker" id="stufe-8-6"></span>

Aus den Schichten folgt das Verhalten eines Live-Systems beim Ausschalten unmittelbar. Die obere Schicht liegt im Arbeitsspeicher, und der Arbeitsspeicher verliert ohne Strom seinen Inhalt. Die untere Schicht wurde nie verändert. Beim nächsten Start ist das System also genau so, wie es auf dem Stick steht.

::::beispiel Eine Datei, die den Neustart nicht übersteht
Für dieses Kapitel wurde ein sehr kleines Live-System, Alpine Linux in der Version 3.24, in einer Test-VM vom Abbild gestartet. Die Liste der eingehängten Dateisysteme zeigt die Schichten: das Startmedium mit seinem ISO-Dateisystem nur lesbar (`ro`), die Wurzel `/` als tmpfs, und ein Teil des Systems als squashfs, ebenfalls nur lesbar:

```console Alpine Linux, Live-System in einer Test-VM
# mount | grep -E ' on / |/media/|modloop'
/dev/sda on /media/sda type iso9660 (ro,relatime,nojoliet,check=s,map=n,blocksize=2048,iocharset=utf8)
tmpfs on / type tmpfs (rw,relatime,mode=755,inode64)
/dev/loop0 on /.modloop type squashfs (ro,relatime,errors=continue)
# echo 'Notiz aus der Live-Sitzung' > /root/notiz.txt
# cat /root/notiz.txt
Notiz aus der Live-Sitzung
```

Das Zeichen `#` am Zeilenanfang ist hier die Eingabeaufforderung, denn in dieser Test-VM arbeitet man als Administrator. In derselben Sitzung wurde außerdem das Programm `lsblk` aus dem Internet nachinstalliert. Nach einem Neustart der VM ist beides verschwunden:

```console Alpine Linux, nach dem Neustart
# cat /root/notiz.txt
cat: can't open '/root/notiz.txt': No such file or directory
# lsblk
-sh: lsblk: not found
```
::::

Alpine legt das ganze System beim Start in ein tmpfs und hängt nur einen Teil als squashfs ein; Ubuntu legt dagegen, wie in Unterabschnitt [8.5](#stufe-8-5) beschrieben, ein tmpfs als Overlay über seine squashfs-Dateien. Das Ergebnis ist dasselbe: Alles, was sich während der Sitzung ändert, steht im Arbeitsspeicher. Dasselbe gilt für Programme, die man im Live-System nachträglich installiert: Auch sie landen im Arbeitsspeicher und sind nach dem Neustart verschwunden.

⁠**Kurz gesagt:** Nach dem Ausschalten ist alles weg, was man im Live-System geändert hat, und jeder Start ist wieder frisch.

### Persistenz

<span class="anker" id="stufe-8-7"></span>

Dass ein Live-System alles vergisst, ist meist ein Vorteil. Wer aber regelmäßig mit demselben Stick arbeitet, möchte manchmal seine Dateien und Einstellungen behalten.

:::definition Definition 8.6 (Persistenz)
<span class="anker" id="satz-8-6"></span>

__Persistenz__ heißt bei einem Live-System, dass es Änderungen nicht im Arbeitsspeicher, sondern in einem zusätzlichen Speicherbereich auf dem Stick ablegt, sodass sie den Neustart überstehen. Bei Ubuntu ist das eine Partition oder Datei mit der Bezeichnung `casper-rw`, die das Live-System beim Start mit der Startoption `persistent` als obere Schicht benutzt.
:::

::::beispiel Persistenz mit Rufus
Das Windows-Programm Rufus, mit dem man Abbilder auf USB-Sticks schreibt, bietet beim Schreiben eines Ubuntu-Sticks einen Regler für die Größe einer solchen Persistenz-Partition. Die Anleitungen von Ubuntu beschreiben das nicht; Rufus selbst hat die Funktion für einzelne Ubuntu-Versionen mehrfach nachbessern müssen. Ob sie mit Ubuntu 26.04 zuverlässig funktioniert, ist nicht gesichert.
::::

⁠**Kurz gesagt:** Persistenz macht den Stick zu einem System mit Gedächtnis, ist bei Ubuntu aber eine wenig gepflegte Zusatzfunktion.

:::hintergrund Warum für dauerhaftes Arbeiten eine VM besser ist
Mit Persistenz verliert der Stick genau die Eigenschaften, die ein Live-System auszeichnen: Er ist nicht mehr bei jedem Start frisch, und ein Fehler bleibt bestehen. Dazu liegen alle Dateien unverschlüsselt auf dem Stick, und wer ihn verliert, gibt sie jedem preis, der ihn findet. Ein USB-Stick ist außerdem für viele kleine Schreibzugriffe weder schnell noch dauerhaft. Wer ein Linux zum dauerhaften Arbeiten braucht, ist mit WSL 2 oder einer VM besser bedient; der Live-Stick ist zum Ausprobieren und für einen sauberen Neustart da.
:::

### Aufgaben zu Abschnitt [8](#stufe-8)

<span class="anker" id="stufe-8-8"></span>

:::aufgabe Aufgabe 23 ★ Was übersteht den Neustart?
<span class="anker" id="aufg-23"></span>

Du arbeitest im Ubuntu-Live-System ohne Persistenz. Was davon ist nach dem nächsten Start vom selben Stick noch da? (a) Ein Lesezeichen im Browser, (b) eine Datei, die du im persönlichen Ordner gespeichert hast, (c) eine Datei, die du auf einen zweiten USB-Stick gespeichert hast, (d) eine Datei, die du in deinen Cloud-Speicher hochgeladen hast, (e) ein Programm, das du nachinstalliert hast. Begründe jeweils mit den Schichten.

:::loesung
(a) Weg. Das Lesezeichen steht in einer Datei im persönlichen Ordner, also in der oberen Schicht im Arbeitsspeicher. (b) Weg, aus demselben Grund. (c) Noch da. Der zweite Stick ist ein eigener Datenträger, den du eingehängt und direkt beschrieben hast; er gehört nicht zum Overlay. (d) Noch da. Die Datei liegt auf einem Server im Internet. (e) Weg. Die Dateien des Programms wurden in die obere Schicht geschrieben; das squashfs auf dem Stick ist unverändert.
:::
:::

:::aufgabe Aufgabe 24 ★★ Das Overlay nachvollziehen
<span class="anker" id="aufg-24"></span>

In der unteren Schicht eines Overlays liegen die Dateien `a`, `b` und `c`, die obere Schicht ist leer. Nacheinander geschieht: `a` wird geändert, `b` wird gelöscht, `d` wird neu angelegt, `d` wird geändert. Was steht danach in der oberen Schicht, was in der unteren, und welche Dateien sehen die Programme? Was sehen sie nach einem Neustart?

:::loesung
Nacheinander:

<ul>

<li>

`a` ändern: Das Overlay kopiert `a` in die obere Schicht und ändert dort die Kopie.

</li>

<li>

`b` löschen: In der oberen Schicht entsteht eine Markierung, die `b` verdeckt.

</li>

<li>

`d` anlegen: `d` entsteht nur in der oberen Schicht.

</li>

<li>

`d` ändern: Die Datei liegt schon oben und wird dort geändert, eine Kopie ist nicht nötig.

</li>

</ul>

Danach enthält die obere Schicht die geänderte Kopie von `a`, die Markierung für `b` und die geänderte Datei `d`. Die untere Schicht enthält unverändert `a`, `b` und `c`. Die Programme sehen `a` in der geänderten Fassung, `c` und `d`; `b` sehen sie nicht. Nach einem Neustart ist die obere Schicht leer: Die Programme sehen wieder `a` in der ursprünglichen Fassung, `b` und `c`, und `d` gibt es nicht.
:::
:::

:::aufgabe Aufgabe 25 ★ Wenn der Arbeitsspeicher voll wird
<span class="anker" id="aufg-25"></span>

Ein Rechner mit 8 GB Arbeitsspeicher läuft im Live-System. Du lädst eine 5 GB große Datei in deinen persönlichen Ordner herunter. Warum kann das Live-System dabei in Schwierigkeiten geraten, obwohl der USB-Stick noch Platz hat und die interne SSD 300 GB frei hat?

:::loesung
Der persönliche Ordner liegt im Overlay, und alles, was man dort speichert, landet in der oberen Schicht, also im tmpfs im Arbeitsspeicher. Die 5 GB der heruntergeladenen Datei belegen damit 5 GB Arbeitsspeicher, zusätzlich zu dem, was das laufende System, der Browser und das Herunterladen selbst brauchen. Bei 8 GB wird der Arbeitsspeicher knapp oder läuft voll, oder das tmpfs erreicht die Höchstgröße, die beim Einhängen festgelegt wurde. Dann bricht das Herunterladen mit einem Fehler ab, oder das ganze System wird zäh.

Der freie Platz auf dem Stick hilft nicht, weil das Live-System dort ohne Persistenz nichts schreibt; die untere Schicht ist nur lesbar. Der freie Platz auf der SSD hilft nicht, weil sie nicht eingehängt ist. Große Dateien speichert man im Live-System deshalb auf einem zweiten USB-Stick oder lädt sie gleich in einen Cloud-Speicher.
:::
:::

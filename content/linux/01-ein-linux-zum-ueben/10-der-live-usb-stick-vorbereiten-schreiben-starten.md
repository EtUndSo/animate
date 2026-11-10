---
title: Der Live-USB-Stick: vorbereiten, schreiben, starten
pfad: Informatik / Linux und Kommandozeile / Ein Linux zum Üben: WSL, virtuelle Maschine, Live-USB-Stick
adresse: informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick
knoten: Kapitel 1: Ein Linux zum Üben: WSL, virtuelle Maschine, Live-USB-Stick
order: 6061000
summary: Dieser Abschnitt richtet den dritten Weg ein: Ubuntu 26.04 als Live-System auf einem USB-Stick.
tags: Schnellstart, Schreibwerkzeug
lang: de
---

<span class="anker" id="stufe-9"></span>

:::zweck
Dieser Abschnitt richtet den dritten Weg ein: Ubuntu 26.04 als Live-System auf einem USB-Stick. Hier beschreibt man einen Datenträger und startet den Rechner auf ungewohnte Weise, deshalb stehen die Risiken und ihre Absicherung am Anfang. Er setzt die Abschnitte [5](datentrager-abbild-und-prufsumme.html#stufe-5), [6](wie-ein-pc-startet.html#stufe-6) und [8](das-live-system.html#stufe-8) voraus.
:::

### Die Risiken im Überblick

<span class="anker" id="stufe-9-1"></span>

Fast alles, was beim Live-Stick schiefgehen kann, hat eine von zwei Ursachen: Man beschreibt einen falschen Datenträger, oder man verändert etwas an der Startkette. Tabelle [4](#tab-4) nennt die einzelnen Gefahren mit ihrer Absicherung; die folgenden Unterabschnitte erklären sie.

<span class="anker" id="tab-4"></span>

**Tabelle 4:** Die Gefahren beim Live-USB-Stick und ihre Absicherung.

| Gefahr | Ursache | Absicherung |
|---|---|---|
| falscher Datenträger überschrieben | das Schreibwerkzeug ersetzt den ganzen gewählten Datenträger | andere USB-Speicher abziehen, Stick an der Größe erkennen (Unterabschnitt [9.2](#stufe-9-2)) |
| Abfrage des Wiederherstellungsschlüssels | Änderung an der Startkette | Schlüssel vorher sichern, nur das Bootmenü benutzen, Secure Boot an (Unterabschnitt [6.5](wie-ein-pc-startet.html#stufe-6-5)) |
| Windows-Daten beschädigt | Windows ruht nach „Herunterfahren“ mit Schnellstart | „Neu starten“ statt „Herunterfahren“, Windows-Partitionen nicht anfassen (Unterabschnitt [9.3](#stufe-9-3)) |
| Ubuntu versehentlich installiert | „Ubuntu installieren“ statt „ausprobieren“ gewählt | nur „Ubuntu ausprobieren“ (Unterabschnitt [9.6](#stufe-9-6)) |
| Stick formatiert | Windows bietet nach dem Schreiben an, den Stick zu formatieren | die Meldung mit „Abbrechen“ schließen (Unterabschnitt [9.5](#stufe-9-5)) |
| Ärger mit fremden Geräten | Rechner von Hochschule oder Arbeitgeber | nur eigene Rechner vom Stick starten |

⁠**Kurz gesagt:** Wer den richtigen Datenträger beschreibt und die Startkette nicht verändert, geht mit dem Live-Stick kaum ein Risiko ein.

### Den richtigen Datenträger erkennen

<span class="anker" id="stufe-9-2"></span>

Das Schreibwerkzeug überschreibt den Datenträger, den man ihm nennt, vollständig, von der Partitionstabelle bis zum letzten Sektor. Ist das versehentlich die interne SSD oder eine externe Festplatte mit der Datensicherung, sind deren Daten verloren. Das ist das größte Risiko des ganzen Wegs.

Windows zeigt alle Datenträger im Programm „Datenträgerverwaltung“; du öffnest es, indem du mit der rechten Maustaste auf das Startmenü klickst und „Datenträgerverwaltung“ wählst. Abbildung [12](#abb-12) zeigt schematisch, was du dort siehst, wenn ein 8-GB-Stick steckt.

:::abbildung linux/k1datentraeger 12
Die Datenträgerverwaltung von Windows, schematisch. Datenträger 0 ist die interne SSD mit EFI-Systempartition, Laufwerk C: und Wiederherstellungspartition; Datenträger 1 ist der Stick, ein Wechselmedium mit 7,45 GB. Nur Datenträger 1 darf das Ziel des Schreibwerkzeugs sein.
:::

:::warnung Den Stick sicher erkennen, bevor geschrieben wird
<ol>

<li>

Ziehe alle anderen USB-Speicher ab: externe Festplatten, Speicherkarten, weitere Sticks. Dann kann das Schreibwerkzeug sie nicht treffen.

</li>

<li>

Nimm einen Stick mit mindestens 8 GB, dessen Inhalt gelöscht werden darf. Sichere vorher alles, was du von ihm behalten willst.

</li>

<li>

Stecke den Stick ein und sieh in der Datenträgerverwaltung nach: Der Stick ist als Wechselmedium bezeichnet und hat die Größe, die du nach Unterabschnitt [5.1](datentrager-abbild-und-prufsumme.html#stufe-5-1) erwartest, bei 8 GB also etwa 7,45 GB. Der Datenträger mit Laufwerk C:, der EFI-Systempartition und der Wiederherstellungspartition ist die interne SSD; ihre Partitionen dürfen nie verändert werden.

</li>

<li>

Merke dir den Laufwerksbuchstaben und die Größe des Sticks und vergleiche beides im Schreibwerkzeug, bevor du startest.

</li>

</ol>
:::

⁠**Kurz gesagt:** Andere Speicher abziehen und den Stick an „Wechselmedium“ und seiner Größe erkennen, dann erst schreiben.

### Der Schnellstart von Windows

<span class="anker" id="stufe-9-3"></span>

„Herunterfahren“ beendet Windows auf den meisten Rechnern nicht vollständig. Das ist für den Start vom Stick wichtig, aus zwei Gründen.

:::definition Definition 9.1 (Schnellstart)
<span class="anker" id="satz-9-1"></span>

Der __Schnellstart__ ist eine Funktion von Windows, die beim Herunterfahren die Programme beendet, den Zustand des Windows-Kernels und seiner Treiber aber in eine Datei auf Laufwerk C: schreibt und beim nächsten Einschalten von dort fortsetzt, statt neu zu starten. Er ist in Windows standardmäßig eingeschaltet und wirkt nur beim Herunterfahren, nicht bei „Neu starten“.
:::

**Warum „Neu starten“ der richtige Weg zum Stick ist.** Nach „Herunterfahren“ mit Schnellstart überspringt die Firmware beim nächsten Einschalten oft so schnell den Moment, in dem sie auf die Taste für das Bootmenü reagiert, dass man ihn verpasst. Und Laufwerk C: bleibt in einem halb benutzten Zustand stehen, den Windows beim Fortsetzen genau so wieder erwartet. Würde ein anderes System dort etwas ändern, passten der gespeicherte Zustand und die Platte nicht mehr zusammen, und Windows könnte Dateien beschädigen. Linux hängt eine so ruhende Windows-Partition deshalb höchstens schreibgeschützt ein. „Neu starten“ beendet Windows dagegen vollständig und führt sofort durch die Firmware, wo die Taste für das Bootmenü sicher wirkt.

⁠**Kurz gesagt:** Zum Stick über „Neu starten“, nicht über „Herunterfahren“, und die Windows-Partitionen im Live-System nicht anfassen.

### Das Abbild laden und prüfen

<span class="anker" id="stufe-9-4"></span>

Für den Stick brauchst du dasselbe Abbild wie für die VM.

**Schritte.** So lädst und prüfst du das Abbild:

<ol>

<li>

Lade auf [https://ubuntu.com/download/desktop](https://ubuntu.com/download/desktop) die Datei `ubuntu-26.04.1-desktop-amd64.iso` herunter, 6,48 GB.

</li>

<li>

Lade von [https://releases.ubuntu.com/26.04/](https://releases.ubuntu.com/26.04/) die Datei `SHA256SUMS` in denselben Ordner, meist „Downloads“.

</li>

<li>

Öffne in diesem Ordner eine PowerShell; im Explorer geht das mit der rechten Maustaste in einen freien Bereich des Ordners und „Im Terminal öffnen“. Vergleiche dann mit dem Wert aus der vierten Zeile von `SHA256SUMS`:

```console Windows (PowerShell)
PS> (Get-FileHash .\ubuntu-26.04.1-desktop-amd64.iso).Hash -eq "601e30fbf5d97759367c632e2c33630665039b7e2158fd068403da3ccf1bda1f"
```

Die Antwort muss `True` lauten. Das Berechnen dauert für 6,5 GB eine Weile.

</li>

<li>

Steht `False` da, lade das Abbild noch einmal herunter und benutze es auf keinen Fall.

</li>

</ol>

⁠**Kurz gesagt:** Abbild und `SHA256SUMS` von Ubuntu laden, Prüfsumme vergleichen, nur bei `True` weitermachen.

### Das Schreibwerkzeug

<span class="anker" id="stufe-9-5"></span>

Ein Abbild wird nicht kopiert, sondern geschrieben (Unterabschnitt [5.4](datentrager-abbild-und-prufsumme.html#stufe-5-4)). Dafür gibt es eigene Programme.

:::definition Definition 9.2 (Schreibwerkzeug)
<span class="anker" id="satz-9-2"></span>

Ein __Schreibwerkzeug__ ist ein Programm, das ein Abbild Sektor für Sektor auf einen ganzen Datenträger schreibt. Dabei ersetzt es die Partitionstabelle und alle Daten des Datenträgers; was vorher darauf war, ist danach verloren.
:::

Abbildung [13](#abb-13) zeigt einen Stick vor und nach dem Schreiben.

:::abbildung linux/k1stick 13
Ein 8-GB-Stick vor und nach dem Schreiben des Ubuntu-Abbilds, schematisch und nicht maßstäblich. Vorher: eine Partitionstabelle und eine FAT32-Partition mit Dateien. Nachher: eine neue Partitionstabelle aus dem Abbild, das ISO-Dateisystem mit dem System und eine kleine EFI-Systempartition; der Rest des Sticks bleibt ungenutzt. Die alten Dateien sind nicht mehr auffindbar.
:::

::::beispiel [Beispiele] Zwei Schreibwerkzeuge
⁠**balenaEtcher** ([https://etcher.balena.io](https://etcher.balena.io)) ist das einfachste Werkzeug und läuft unter Windows, macOS und Linux. Es zeigt Systemlaufwerke standardmäßig gar nicht erst an und prüft nach dem Schreiben, ob jedes Byte richtig angekommen ist. Die Bedienung hat drei Schritte: „Flash from file“ und das Abbild wählen, „Select target“ und den Stick wählen, „Flash!“ und die Rückfrage von Windows bestätigen.

⁠**Rufus** ([https://rufus.ie](https://rufus.ie)) läuft nur unter Windows und hat mehr Einstellungen. Es stellt seine Oberfläche auf die Sprache von Windows ein; die Felder stehen dann deutsch beschriftet an denselben Stellen, hier sind die englischen Namen genannt. Nach dem Start prüfst du im Feld „Device“ (Laufwerk), dass dort der Stick mit seinem Buchstaben und seiner Größe steht. Mit „SELECT“ wählst du das Abbild, die übrigen Einstellungen lässt du, wie sie sind, und klickst auf „START“. Rufus fragt dann, ob es fehlende Startdateien herunterladen darf (Ja), und in welcher Art es das Abbild schreiben soll; behalte „Write in ISO Image mode“. Zuletzt warnt es, dass alle Daten auf dem Laufwerk zerstört werden. Prüfe in diesem Moment noch einmal das Laufwerk, dann bestätige. Nach etwa zehn Minuten steht „READY“ da.
::::

:::warnung Nach dem Schreiben: „Datenträger formatieren?“ abbrechen
Nach dem Schreiben meldet Windows oft, ein Laufwerk müsse formatiert werden, bevor man es benutzen kann. Der Grund ist harmlos: Windows kann die Partitionen aus dem Linux-Abbild nicht lesen. Klicke auf „Abbrechen“, niemals auf „Datenträger formatieren“, sonst ist der frisch geschriebene Stick wieder leer.
:::

⁠**Kurz gesagt:** Ein Schreibwerkzeug wie balenaEtcher oder Rufus macht den Stick zur Kopie des Abbilds; alles, was vorher darauf war, ist weg.

:::hintergrund Ein Stick vor und nach dem Schreiben, nachgemessen
Für dieses Kapitel wurde das Schreiben an einer Abbilddatei in der Größe eines 8-GB-Sticks nachgestellt, mit dem kleinen Abbild von Alpine Linux aus Unterabschnitt [8.6](das-live-system.html#stufe-8-6). Vorher enthielt die Partitionstabelle eine einzige FAT32-Partition über den ganzen Stick. Nachher stand dort die Tabelle aus dem Abbild:

```text
Device     Boot Start    End Sectors  Size Id Type
stick.img1 *        0 137215  137216   67M  0 Empty
stick.img2        220   3099    2880  1.4M ef EFI (FAT-12/16/32)
```

Partition 1 umfasst das ganze Abbild mit dem ISO-Dateisystem, Partition 2 liegt mitten darin und enthält die Startdateien für UEFI. Die übrigen 7,4 GiB des Sticks gehören zu keiner Partition mehr. Die alte FAT32-Partition ist nicht mehr eingetragen; ihre Dateien sind, soweit sie hinter dem Abbild lagen, zwar noch nicht überschrieben, aber ohne ihr Dateisystem nicht mehr aufzufinden. Bei Ubuntu ist die Aufteilung etwas anders, das Prinzip dasselbe.
:::

:::hintergrund Warum dieses Kapitel Ventoy nicht empfiehlt
Ein drittes Werkzeug, Ventoy, richtet den Stick einmal ein, danach kopiert man beliebig viele Abbilder einfach als Dateien darauf. Das ist bequem, aber Ventoy umgeht in der Voreinstellung die Prüfung von Secure Boot, und mit seinem eigenen Schlüssel erlaubt man dem Rechner dauerhaft, über Ventoy beliebige Startprogramme zu starten. Für erfahrene Nutzer kann das sinnvoll sein; für einen ersten Live-Stick reichen balenaEtcher und Rufus.
:::

### Vom Stick starten: „Ubuntu ausprobieren“

<span class="anker" id="stufe-9-6"></span>

Jetzt startest du den Rechner vom Stick. Prüfe vorher die Warnung in Unterabschnitt [6.5](wie-ein-pc-startet.html#stufe-6-5): Ist dein Laufwerk verschlüsselt, muss der Wiederherstellungsschlüssel gesichert sein.

:::warnung Nicht installieren
Das Installationsprogramm auf dem Stick kann Ubuntu auf die interne SSD installieren und dabei Windows mit allen Daten löschen. Wähle deshalb immer „Ubuntu ausprobieren“ und nie „Ubuntu installieren“. Auch im laufenden Live-System bleibt ein Symbol zum Installieren sichtbar, je nach Version im Dock am Bildschirmrand oder auf dem Schreibtisch; klicke es nicht an.
:::

**Schritte.** So startest du Ubuntu vom Stick:

<ol>

<li>

Speichere alle offenen Dateien unter Windows. Stecke den Stick ein.

</li>

<li>

Wähle im Startmenü „Neu starten“, nicht „Herunterfahren“ (Unterabschnitt [9.3](#stufe-9-3)).

</li>

<li>

Drücke sofort nach dem Neustart mehrmals die Taste für das Bootmenü (Unterabschnitt [6.2](wie-ein-pc-startet.html#stufe-6-2)) oder benutze den Weg über den erweiterten Start.

</li>

<li>

Wähle im Bootmenü den Eintrag mit dem Namen des Sticks. Gibt es ihn zweimal, nimm den, der mit „UEFI“ beginnt; der andere startet in der alten BIOS-Betriebsart.

</li>

<li>

GRUB zeigt sein Menü; der erste Eintrag startet Ubuntu. Nach einer Weile erscheint das Installationsprogramm.

</li>

<li>

Wähle Sprache, Barrierefreiheit, Tastaturbelegung und, wenn du willst, ein WLAN. Auf der Seite „Ubuntu ausprobieren oder installieren“ klickst du auf „Ubuntu ausprobieren“.

</li>

</ol>

Danach erscheint der Schreibtisch von Ubuntu. Läuft Linux jetzt mit Grafik, WLAN und Ton, kommt dein Rechner auch mit einem installierten Ubuntu zurecht. Für das Ausprobieren benutzt Ubuntu nur Treiber, die als freie Software vorliegen; manche Grafikkarten laufen deshalb langsamer als später in einer Installation.

⁠**Kurz gesagt:** „Neu starten“, Bootmenü, Eintrag „UEFI“ mit dem Stick, „Ubuntu ausprobieren“, nie „installieren“.

### Im Live-System: Terminal und Datenträger

<span class="anker" id="stufe-9-7"></span>

Das Terminal öffnest du im Live-System wie in der VM mit Strg+Alt+T. `cat /etc/os-release` zeigt dieselben Zeilen wie in Unterabschnitt [2.3](drei-wege-zu-einem-eigenen-linux.html#stufe-2-3), `uname -r` den Kernel von Ubuntu. Interessanter ist hier der Blick auf die Datenträger, denn jetzt sieht Linux die echte Hardware.

::::beispiel Die interne SSD bleibt unberührt
Der Befehl `lsblk` mit einer Auswahl von Spalten zeigt jeden Datenträger mit Größe, Art, Anschluss (`TRAN`, etwa `usb` oder `nvme`), der Angabe, ob er herausnehmbar ist (`RM`, 1 heißt ja), und seinem Einhängepunkt. Die folgende Ausgabe stammt aus der Test-VM aus Unterabschnitt [8.6](das-live-system.html#stufe-8-6): Das Alpine-Abbild steckte dort als virtueller USB-Stick, und eine leere virtuelle SSD war wie die SSD eines Windows-Rechners eingeteilt.

```console Alpine Linux, Live-System in einer Test-VM
# lsblk -o NAME,SIZE,TYPE,TRAN,RM,MOUNTPOINTS
NAME          SIZE TYPE TRAN   RM MOUNTPOINTS
fd0             0B disk         1
loop0        21.9M loop         0 /.modloop
sda           7.5G disk usb     1 /media/sda
├─sda1         67M part         1
└─sda2        1.4M part         1
sr0          1024M rom  ata     1
nvme0n1     476.9G disk nvme    0
├─nvme0n1p1   260M part nvme    0
├─nvme0n1p2    16M part nvme    0
├─nvme0n1p3   474G part nvme    0
└─nvme0n1p4   2.7G part nvme    0
```

Der Stick ist `sda`: angeschlossen über USB, herausnehmbar, 7,5 GiB groß und unter `/media/sda` eingehängt, denn von ihm liest das Live-System. Seine beiden Partitionen stammen aus dem Abbild. `loop0` ist das squashfs aus Unterabschnitt [8.6](das-live-system.html#stufe-8-6): Eine Datei vom Stick, die Linux wie einen Datenträger behandelt, heißt ein Datenträger vom Typ `loop`. `fd0` und `sr0` sind ein Disketten- und ein CD-Laufwerk, die die Test-VM von sich aus nachbildet. Die SSD heißt bei Linux `nvme0n1`, ihre Partitionen `nvme0n1p1` bis `nvme0n1p4`. Keine davon hat einen Einhängepunkt: Das Live-System benutzt die SSD nicht. Auf einem echten Rechner mit Ubuntu sieht die Liste ähnlich aus; dort stehen meist mehrere Einträge vom Typ `loop`, einer für jede squashfs-Datei.
::::

:::warnung Die Windows-Partitionen im Live-System nicht einhängen
Ubuntu zeigt die Partitionen der internen SSD auch in seinem Dateimanager an und hängt sie ein, wenn man darauf klickt. Lass sie in Ruhe: Ruht Windows mit Schnellstart, könntest du Laufwerk C: beschädigen, und ist es verschlüsselt, kommst du ohne den Wiederherstellungsschlüssel ohnehin nicht an die Dateien. Für diese Reihe brauchst du von der internen SSD nichts.
:::

⁠**Kurz gesagt:** Im Live-System zeigt `lsblk` die interne SSD ohne Einhängepunkt, also unbenutzt.

### Beenden und den Stick zurückverwandeln

<span class="anker" id="stufe-9-8"></span>

Zum Beenden wählst du oben rechts im Menü von Ubuntu „Ausschalten“ oder „Neu starten“. Ubuntu fordert dich auf, den Stick zu entfernen, und du bestätigst mit der Eingabetaste. Ohne Stick startet der Rechner wieder Windows, genau wie vorher. Alles, was du im Live-System angelegt hast, ist weg (Unterabschnitt [8.6](das-live-system.html#stufe-8-6)).

Den Stick kannst du für weitere Starts behalten. Brauchst du ihn wieder als gewöhnlichen Stick, schreibst du ihn mit einem Schreibwerkzeug neu oder lässt Rufus oder die Datenträgerverwaltung von Windows eine neue Partition mit FAT32 oder exFAT anlegen. Für beides gilt dieselbe Sorgfalt wie beim Schreiben: Ziel ist der Stick, an der Größe erkannt, und sonst nichts.

⁠**Kurz gesagt:** Ausschalten, Stick abziehen, Windows startet wie vorher; zurückverwandeln mit derselben Sorgfalt wie beim Schreiben.

### Aufgaben zu Abschnitt [9](#stufe-9)

<span class="anker" id="stufe-9-9"></span>

:::aufgabe Aufgabe 26 ★★★ Ein Live-USB-Stick mit Ubuntu
<span class="anker" id="aufg-26"></span>

Richte den dritten Weg vollständig ein. Halte bei jedem Schritt fest, woran du erkannt hast, dass er gelungen ist.

<ol class="al">

<li>

Vorbereitung: Prüfe, ob dein Laufwerk verschlüsselt ist, und sichere gegebenenfalls den Wiederherstellungsschlüssel. Lege einen Stick mit mindestens 8 GB bereit, dessen Inhalt du nicht mehr brauchst, und ziehe alle anderen USB-Speicher ab.

</li>

<li>

Lade das Abbild und `SHA256SUMS` herunter und prüfe die Prüfsumme.

</li>

<li>

Schreibe den Stick mit balenaEtcher oder Rufus. Erkenne den Stick vorher in der Datenträgerverwaltung.

</li>

<li>

Starte über „Neu starten“ und das Bootmenü vom Stick und wähle „Ubuntu ausprobieren“. Öffne das Terminal und führe `cat /etc/os-release` aus.

</li>

</ol>

Prüfpunkte am Ende: Der Wiederherstellungsschlüssel lag vor Schritt (c) bereit; die Prüfsumme stimmte; Secure Boot blieb eingeschaltet; nach dem Ausschalten startet Windows wie vorher.

:::loesung
Die einzelnen Schritte sind gelungen, wenn du Folgendes beobachtet hast:

<ol class="al">

<li>

Die Einstellungsseite zeigt, ob die Geräteverschlüsselung bzw. BitLocker eingeschaltet ist. Wenn ja, steht unter [https://aka.ms/myrecoverykey](https://aka.ms/myrecoverykey) ein Schlüssel für deinen Rechner, und du hast ihn auf Papier oder auf einem anderen Gerät. Nur der Stick für Ubuntu steckt noch am Rechner.

</li>

<li>

`(Get-FileHash .\ubuntu-26.04.1-desktop-amd64.iso).Hash -eq "601e..."` mit dem vollständigen Wert aus der vierten Zeile von `SHA256SUMS` antwortet `True`.

</li>

<li>

In der Datenträgerverwaltung war der Stick ein Wechselmedium mit etwa 7,45 GB (bei 8 GB). balenaEtcher meldet am Ende, dass das Schreiben und die anschließende Prüfung gelungen sind; Rufus zeigt „READY“. Eine Frage von Windows, den Stick zu formatieren, hast du mit „Abbrechen“ beantwortet.

</li>

<li>

Im Bootmenü hast du den Eintrag „UEFI:“ mit dem Namen des Sticks gewählt und im Installationsprogramm „Ubuntu ausprobieren“. Im Terminal zeigt `cat /etc/os-release` die Zeile `PRETTY_NAME="Ubuntu 26.04.1 LTS"`.

</li>

</ol>

Secure Boot war dabei eingeschaltet, denn du hast in der Firmware nichts verändert, und nach dem Ausschalten und Abziehen des Sticks startet Windows ohne Rückfrage.
:::
:::

:::aufgabe Aufgabe 27 ★ Die SSD im Live-System beobachten
<span class="anker" id="aufg-27"></span>

Führe im Live-System `lsblk -o NAME,SIZE,TYPE,TRAN,RM,MOUNTPOINTS` aus. Woran erkennst du (a) den Stick, (b) die interne SSD, (c) dass das Live-System die SSD nicht benutzt? Wie viele Partitionen hat deine SSD, und passen sie zu dem, was die Datenträgerverwaltung unter Windows zeigt?

:::loesung
So liest du die Ausgabe:

<ol class="al">

<li>

Den Stick erkennst du an `TRAN usb`, an `RM 1` (herausnehmbar) und an seiner Größe, bei einem 8-GB-Stick etwa `7.5G`. Der Stick selbst oder eine seiner Partitionen hat einen Einhängepunkt, denn von dort liest das Live-System sein System.

</li>

<li>

Die interne SSD heißt bei einer NVMe-SSD `nvme0n1`, bei einer über SATA angeschlossenen SSD oder Festplatte `sda` oder `sdb`. Sie hat `RM 0` und die Größe, die du nach Unterabschnitt [5.1](datentrager-abbild-und-prufsumme.html#stufe-5-1) erwartest, bei 512 GB also etwa `476.9G`.

</li>

<li>

Keine Partition der SSD hat einen Einhängepunkt. Das System liest und schreibt dort also nichts.

</li>

</ol>

Ein typischer Windows-Rechner zeigt vier Partitionen: die EFI-Systempartition, eine kleine reservierte Partition, Laufwerk C: und die Wiederherstellungspartition. Die Datenträgerverwaltung von Windows zeigt nur drei davon; die kleine reservierte Partition blendet sie aus.
:::
:::

:::aufgabe Aufgabe 28 ★★ Fehlersuche beim Start
<span class="anker" id="aufg-28"></span>

Was ist jeweils vermutlich passiert, und was tust du? (a) Nach „Herunterfahren“ und Einschalten startet sofort Windows, obwohl du die Taste für das Bootmenü gedrückt hast. (b) Im Bootmenü steht der Stick zweimal, einmal mit „UEFI:“ davor; du hast den anderen Eintrag gewählt, und es erscheint nur ein schwarzer Bildschirm. (c) Die Firmware meldet „Secure Boot Violation“. (d) Windows fragt nach dem Schreiben, ob es den Stick formatieren soll. (e) Nach dem Ausprobieren startet Windows und verlangt einen 48-stelligen Schlüssel.

:::loesung
(a) Nach „Herunterfahren“ hat Windows mit dem Schnellstart nur geruht, und die Firmware ist so schnell durchgelaufen, dass die Taste nicht mehr gewirkt hat. Abhilfe: Unter Windows „Neu starten“ wählen und die Taste sofort mehrmals drücken, oder über den erweiterten Start „Ein Gerät verwenden“.

(b) Der andere Eintrag startet den Stick in der alten BIOS-Betriebsart, die viele neue Rechner gar nicht mehr unterstützen oder die bei eingeschaltetem Secure Boot gesperrt ist. Abhilfe: Rechner ausschalten, erneut über das Bootmenü starten und den Eintrag mit „UEFI:“ wählen.

(c) Die Firmware hat ein Startprogramm auf dem Stick nicht akzeptiert: Sein Siegel passt nicht zu den Prüfschlüsseln der Firmware. Mögliche Ursachen sind ein beschädigter oder fremder Stick oder ein Zertifikat, das die Firmware nicht kennt (Hintergrund in Unterabschnitt [6.4](wie-ein-pc-startet.html#stufe-6-4)). Abhilfe: die Prüfsumme des Abbilds noch einmal kontrollieren und den Stick neu schreiben, dann alle Aktualisierungen von Windows und der Firmware einspielen. Secure Boot schaltest du für Ubuntu nicht aus.

(d) Windows kann die Partitionen aus dem Linux-Abbild nicht lesen und hält den Stick deshalb für unformatiert. Abhilfe: „Abbrechen“. Wer formatiert, macht den Stick wieder leer und muss ihn neu schreiben.

(e) Windows verlangt den Wiederherstellungsschlüssel, weil sich aus seiner Sicht die Startkette verändert hat, etwa weil doch eine Einstellung in der Firmware geändert wurde. Abhilfe: Den gesicherten Schlüssel von [https://aka.ms/myrecoverykey](https://aka.ms/myrecoverykey) eingeben; Windows startet dann und läuft normal weiter. Danach prüfst du, ob in der Firmware etwas verstellt ist, etwa Secure Boot oder die Bootreihenfolge, und stellst es zurück; dafür ist der Schlüssel unter Umständen ein weiteres Mal nötig.
:::
:::

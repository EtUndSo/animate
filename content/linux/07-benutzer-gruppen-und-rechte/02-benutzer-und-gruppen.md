---
title: Benutzer und Gruppen
pfad: Informatik / Linux und Kommandozeile / Benutzer, Gruppen und Rechte
adresse: informatik/linux-und-kommandozeile/benutzer-gruppen-und-rechte
knoten: Kapitel 7: Benutzer, Gruppen und Rechte
order: 6120200
summary: Bevor Linux entscheiden kann, wer eine Datei lesen darf, muss es Menschen und Programme unterscheiden.
tags: Benutzer, Benutzernummer, Gruppe, Gruppennummer, Benutzerliste, Hauptgruppe, Systemkonten, Zusatzgruppe
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Bevor Linux entscheiden kann, wer eine Datei lesen darf, muss es Menschen und Programme unterscheiden. Dieser Abschnitt zeigt, wie es das tut: mit Benutzern und Gruppen, die für den Kernel nur Nummern sind, mit zwei Textdateien, in denen die Namen zu diesen Nummern stehen, und mit einem Benutzer, für den fast keine Grenze gilt.
:::

:::::vorwissen Was du dafür brauchst: Prozess, Systemaufruf und Datei

<span class="anker" id="stufe-1-1"></span>

Dieses Kapitel setzt die [Kapitel 1](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/ein-linux-zum-ueben.html) bis 6 voraus. Daraus brauchst du vor allem diese Dinge.

<ul>

<li>

Der Kernel ist der Teil des Betriebssystems, der alles darf. Ein Programm kommt an Dateien nur, indem es den Kernel mit einem Systemaufruf darum bittet; der Kernel prüft die Anfrage und erledigt sie oder lehnt sie ab ([Kapitel 1, Abschnitt 1.4](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/betriebssystem-kernel-und-distribution.html#stufe-1-4)).

</li>

<li>

Ein Prozess ist ein Programm in Ausführung; der Kernel hält Prozesse voneinander getrennt ([Kapitel 4, Abschnitt 1.2](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/prozesse-und-ihre-drei-strome.html#stufe-1-2)). Eine geöffnete Datei führt der Kernel für einen Prozess unter einer kleinen Zahl, dem Dateideskriptor ([Kapitel 4, Abschnitt 1.7](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/prozesse-und-ihre-drei-strome.html#stufe-1-7)). Ein Kindprozess bekommt beim Start eine Kopie dessen, was sein Elternprozess mitgibt, und kann es nicht zurückgeben ([Kapitel 5, Abschnitt 4.5](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/umgebung-und-vererbung.html#stufe-4-5)).

</li>

<li>

`ls -l` zeigt für jede Datei zehn Zeichen am Anfang, den Besitzer und eine Gruppe; was die neun Zeichen nach dem ersten bedeuten, blieb bisher offen ([Kapitel 3, Abschnitt 3.4](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/den-inhalt-eines-verzeichnisses-anzeigen.html#stufe-3-4)). Zu jeder Datei gehört eine Inode mit allen Angaben außer dem Namen; ein Verzeichnis ist eine Tabelle, die Namen auf Inode-Nummern abbildet, und Löschen entfernt einen Namen aus dieser Tabelle ([Kapitel 3, Abschnitte 8.1](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/inode-und-links.html#stufe-8-1), 8.2 und 8.4).

</li>

<li>

`whoami` nennt deinen Benutzernamen, `id` zusätzlich eine Benutzernummer und Gruppen ([Kapitel 2, Abschnitt 6.2](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/das-system-erkunden.html#stufe-6-2)). Die Benutzerliste `/etc/passwd` ist eine Textdatei mit Datensätzen, deren Felder ein Doppelpunkt trennt; `grep`, `cut` und `awk` holen Zeilen und Felder heraus ([Kapitel 6, Abschnitte 1.2](/wissen/informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke/textdaten-datensatze-felder-und-zeilenenden.html#stufe-1-2), 2.1 und 9.2).

</li>

<li>

Die Shell öffnet die Datei einer Umleitung `>` selbst, bevor das Programm startet ([Kapitel 4, Abschnitte 2.1](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/ausgaben-umleiten.html#stufe-2-1) und [2.7](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/ausgaben-umleiten.html#stufe-2-7)). Ein Programm, das nicht im Suchpfad liegt, startet man mit `./programm` ([Kapitel 5, Abschnitt 5.4](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/wie-die-shell-programme-findet-path.html#stufe-5-4)).

</li>

</ul>

⁠**Kurz gesagt:** Du brauchst den Kernel als prüfende Stelle, Prozesse mit ihren Deskriptoren, die Inode und das Verzeichnis als Namenstabelle, `ls -l`, `id` und die Textwerkzeuge für Dateien mit Feldern.

:::warnung Nur im eigenen Übungsverzeichnis
Einige Befehle dieses Kapitels legen Dateien an, ändern ihre Rechte oder löschen sie. Lege dir deshalb ein eigenes Übungsverzeichnis an und arbeite dort:

```console
$ mkdir ~/linuxk7
$ cd ~/linuxk7
```

Alle Dateinamen in den Beispielen beziehen sich auf dieses Verzeichnis. Rechte von Dateien außerhalb davon änderst du nie, auch dann nicht, wenn ein Befehl es erlauben würde.
:::

:::::

### Der Benutzer und seine Nummer

<span class="anker" id="stufe-1-2"></span>

Auf einem Rechner arbeiten oft mehrere Menschen, und auch Programme, die im Hintergrund Dienste erbringen, sollen nicht alles dürfen. Bei jedem Zugriff muss Linux deshalb wissen, für wen er geschieht. Dafür bekommt jeder, der etwas tun darf, ein eigenes Konto.

Im Alltag kennt man das von Kundennummern: Der Mensch sagt seinen Namen, der Computer der Bank rechnet mit der Nummer. Zwei Kunden können denselben Namen tragen, aber nie dieselbe Nummer. Unter Linux ist es genauso, nur strenger: Der Kernel arbeitet ausschließlich mit der Nummer.

:::definition Definition 1.1 (Benutzer, Benutzernummer)
<span class="anker" id="satz-1-1"></span>

Ein __Benutzer__ (genauer Benutzerkonto) ist ein Eintrag, unter dem Prozesse laufen und dem Dateien gehören. Er hat einen Namen und eine ganze Zahl, die __Benutzernummer__, kurz UID (englisch „user identifier“). Der Kernel kennt nur die Benutzernummer; der Name ist eine Übersetzung für Menschen.
:::

`whoami` zeigt den Namen, `id -u` die Nummer desselben Benutzers:

```console
$ whoami
student
$ id -u
1000
```

Auf dem Testsystem heißt der Benutzer `student` und hat die Nummer 1000. Auf deinem Rechner steht dort dein eigener Name, im Live-System `ubuntu`, und die Nummer ist sehr wahrscheinlich ebenfalls 1000: Ubuntu und Debian geben dem ersten Menschen, der ein Konto bekommt, diese Nummer.

::::beispiel Name und Nummer in beide Richtungen
`id` übersetzt in beide Richtungen. Mit der Option `-n` zeigt es statt der Nummer den Namen, und hinter den Optionen darf ein Benutzer stehen, als Name oder als Nummer:

```console
$ id -un 1000
student
$ id -u student
1000
```

Die Nummer 1000 und der Name `student` bezeichnen dasselbe Konto.
::::

⁠**Kurz gesagt:** Ein Benutzer hat einen Namen für Menschen und eine Benutzernummer (UID) für den Kernel; der Kernel rechnet nur mit der Nummer.

### Die Gruppe und ihre Nummer

<span class="anker" id="stufe-1-3"></span>

Oft sollen mehrere Benutzer dieselben Rechte bekommen: alle in einer Wohngemeinschaft dürfen die Einkaufsliste ändern, alle, die den Rechner verwalten, dürfen Programme einrichten. Jedem einzeln Rechte zu geben, wäre mühsam und fehleranfällig. Deshalb fasst Linux Benutzer zu Gruppen zusammen, ähnlich wie ein Verein seine Mitglieder in Abteilungen.

:::definition Definition 1.2 (Gruppe, Gruppennummer)
<span class="anker" id="satz-1-2"></span>

Eine __Gruppe__ ist eine benannte Menge von Benutzern. Wie ein Benutzer hat sie einen Namen und eine ganze Zahl, die __Gruppennummer__, kurz GID (englisch „group identifier“). Ein Benutzer kann zu mehreren Gruppen gehören. Auch hier kennt der Kernel nur die Nummer.
:::

Die Gruppen stehen in der Textdatei `/etc/group`, eine Gruppe je Zeile. Vier Felder, getrennt durch Doppelpunkte, beschreiben sie: der Name, ein `x`, die Gruppennummer und eine Liste von Benutzern, die zur Gruppe gehören, getrennt durch Kommas. Das `x` ist ein Platzhalter: Früher konnte hier ein Passwort für die Gruppe stehen; heute stünde es in der eigenen Datei `/etc/gshadow`, und kaum jemand benutzt so etwas noch. Drei Zeilen der Datei holst du mit `grep` und einem Ausdruck mit Alternativen aus [Kapitel 6, Abschnitt 7.4](/wissen/informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke/regulare-ausdrucke-wiederholungen-gruppen-und-alternativen.html#stufe-7-4):

```console
$ grep -E '^(sudo|users|student):' /etc/group
sudo:x:27:student
users:x:100:
student:x:1000:
```

Die Gruppe `sudo` hat die Nummer 27, und `student` ist eingetragen. Wer zu dieser Gruppe gehört, darf unter Ubuntu Befehle mit den Rechten des Verwalters ausführen, wie [Kapitel 2, Abschnitt 6.2](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/das-system-erkunden.html#stufe-6-2) schon erwähnt hat. Die Gruppe `users` mit der Nummer 100 hat noch keine eingetragenen Mitglieder. Und die Gruppe `student` trägt denselben Namen wie der Benutzer und dieselbe Nummer 1000, hat aber ebenfalls niemanden in ihrer Liste. Warum `student` trotzdem dazugehört, klärt sich mit der Benutzerliste.

⁠**Kurz gesagt:** Eine Gruppe fasst Benutzer zusammen und hat einen Namen und eine Gruppennummer (GID); die Gruppen stehen in `/etc/group`.

### Die Benutzerliste: /etc/passwd

<span class="anker" id="stufe-1-4"></span>

`id` muss irgendwo nachschlagen, welcher Name zur Nummer 1000 gehört. Auch beim Anmelden muss das System zum eingegebenen Namen die Nummer finden. Die Antwort steht in einer gewöhnlichen Textdatei, die du aus [Kapitel 3, Abschnitt 7.3](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/die-verzeichnisstruktur-von-linux.html#stufe-7-3) und [Kapitel 6, Abschnitt 1.2](/wissen/informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke/textdaten-datensatze-felder-und-zeilenenden.html#stufe-1-2) schon kennst.

:::definition Definition 1.3 (Benutzerliste, Hauptgruppe)
<span class="anker" id="satz-1-3"></span>

Die __Benutzerliste__ `/etc/passwd` enthält für jedes Benutzerkonto einen Datensatz mit sieben Feldern, getrennt durch Doppelpunkte:

<ol>

<li>

der Benutzername;

</li>

<li>

ein `x`: Hier stand früher ein Wert zur Prüfung des Passworts, heute liegt er in einer eigenen Datei;

</li>

<li>

die Benutzernummer;

</li>

<li>

die Nummer einer Gruppe, der __Hauptgruppe__ des Benutzers;

</li>

<li>

ein Kommentar, meist der volle Name;

</li>

<li>

das Heimatverzeichnis;

</li>

<li>

das Programm, das nach der Anmeldung startet, meist eine Shell.

</li>

</ol>
:::

Abbildung [1](#abb-1) zerlegt den Datensatz des Testbenutzers.

:::abbildung linux/k7passwd 1
Die Zeile `student:x:1000:1000::/home/student:/bin/bash` aus `/etc/passwd`. Die sechs Doppelpunkte leuchten auf und teilen sie in sieben Felder; darunter erscheinen nacheinander die Bedeutungen: Name, Platzhalter für den Passwort-Prüfwert, Benutzernummer, Nummer der Hauptgruppe, Kommentar (hier leer), Heimatverzeichnis, Programm nach der Anmeldung. Zum Schluss verbindet ein Pfeil die Hauptgruppe 1000 mit der Zeile `student:x:1000:` aus `/etc/group`.
:::

```console
$ grep student /etc/passwd
student:x:1000:1000::/home/student:/bin/bash
$ head -n 3 /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
```

Der Benutzer `student` hat die Nummer 1000, die Hauptgruppe 1000, keinen Kommentar, das Heimatverzeichnis `/home/student` und `/bin/bash` als Shell. Jetzt ist auch klar, warum `student` zur Gruppe `student` gehört, obwohl die Mitgliederliste in `/etc/group` leer ist: Sie ist seine Hauptgruppe, und die steht in `/etc/passwd`. Ubuntu legt für jeden neuen Benutzer eine eigene Gruppe mit demselben Namen an und macht sie zu seiner Hauptgruppe.

Die ersten Zeilen der Datei gehören keinem Menschen. Konten wie `daemon` und `bin` heißen __Systemkonten__: Unter ihnen laufen Dienste des Systems, die nur wenige Rechte bekommen sollen. Ihr letztes Feld ist `/usr/sbin/nologin`, ein kleines Programm, das jede Anmeldung höflich ablehnt; so kann sich niemand als `daemon` anmelden.

::::beispiel Wer ist ein Mensch?
Unter Ubuntu und Debian haben Systemkonten Nummern unter 1000, Konten von Menschen beginnen bei 1000. Mit `awk` aus [Kapitel 6, Abschnitt 9.3](/wissen/informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke/rechnen-mit-spalten-awk.html#stufe-9-3) suchst du die Datensätze, deren drittes Feld mindestens 1000 ist:

```console
$ wc -l /etc/passwd
28 /etc/passwd
$ awk -F: '$3 >= 1000' /etc/passwd
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
student:x:1000:1000::/home/student:/bin/bash
```

Von 28 Konten des Testsystems gehört nur eines einem Menschen. Die Ausnahme `nobody` mit der höchsten Nummer 65534 ist ein Systemkonto mit Absicht: „niemand“, ein Benutzer, dem nichts gehört und unter dem Programme laufen können, die nichts dürfen sollen. Andere Systeme ziehen die Grenze anders; ältere Fedora-Fassungen begannen bei 500.
::::

⁠**Kurz gesagt:** `/etc/passwd` ordnet jedem Benutzernamen in sieben Feldern seine Nummer, seine Hauptgruppe, sein Heimatverzeichnis und sein Startprogramm zu.

### Hauptgruppe und Zusatzgruppen

<span class="anker" id="stufe-1-5"></span>

Ein Benutzer gehört also auf zwei Wegen zu Gruppen: über das vierte Feld in `/etc/passwd` und über die Mitgliederlisten in `/etc/group`. Für die Rechte zählen beide, aber sie spielen verschiedene Rollen. Abbildung [2](#abb-2) stellt sie nebeneinander.

:::abbildung linux/k7gruppen 2
Links der Datensatz von `student` aus `/etc/passwd`, rechts drei Zeilen aus `/etc/group`. Zuerst führt ein Pfeil vom vierten Feld (1000) zur Gruppe `student`: die Hauptgruppe. Dann führt ein zweiter Pfeil vom Namen `student` in der Mitgliederliste von `sudo` zurück zum Benutzer: eine Zusatzgruppe. Die Gruppe `users` bleibt grau. Unten erscheint die Zeile von `id`, in der beide Gruppen stehen.
:::

:::definition Definition 1.4 (Zusatzgruppe)
<span class="anker" id="satz-1-4"></span>

Eine __Zusatzgruppe__ eines Benutzers ist jede Gruppe, in deren Mitgliederliste in `/etc/group` er steht. Ein Benutzer hat genau eine Hauptgruppe und beliebig viele Zusatzgruppen. Für Rechte zählen alle seine Gruppen gleich.
:::

`id` zeigt alle Nummern zusammen, `groups` nur die Namen der Gruppen:

```console
$ id
uid=1000(student) gid=1000(student) groups=1000(student),27(sudo)
$ groups
student sudo
```

`uid` ist die Benutzernummer, `gid` die Hauptgruppe, und hinter `groups` stehen alle Gruppen, die Hauptgruppe eingeschlossen. In Klammern stehen jeweils die Namen, die `id` in den beiden Dateien nachgeschlagen hat. Auf deinem Rechner stehen dort oft weitere Gruppen, etwa `adm` oder `plugdev`: Ubuntu nimmt den ersten Benutzer bei der Einrichtung in mehrere Gruppen auf.

::::beispiel Die Zeile von root
`id` mit einem Namen zeigt die Gruppen eines anderen Benutzers:

```console
$ id root
uid=0(root) gid=0(root) groups=0(root)
```

Der Benutzer `root` hat die Nummer 0, seine Hauptgruppe heißt ebenfalls `root` und hat die Nummer 0, und Zusatzgruppen hat er keine.
::::

⁠**Kurz gesagt:** Jeder Benutzer hat eine Hauptgruppe (Feld 4 in `/etc/passwd`) und Zusatzgruppen (Mitgliederlisten in `/etc/group`); `id` zeigt alle.

### Der Benutzer eines Prozesses

<span class="anker" id="stufe-1-6"></span>

Nicht du öffnest Dateien, sondern ein Prozess, etwa `cat` oder die Shell. Damit der Kernel prüfen kann, ob der Zugriff erlaubt ist, muss er wissen, für welchen Benutzer dieser Prozess arbeitet. Deshalb trägt jeder Prozess die Nummern seines Benutzers bei sich, so wie man bei einer Veranstaltung ein Band am Handgelenk trägt, das am Eingang geprüft wird.

:::definition Definition 1.5 (Benutzer eines Prozesses)
<span class="anker" id="satz-1-5"></span>

Jeder Prozess trägt eine Benutzernummer, die Nummer einer Hauptgruppe und eine Liste von Zusatzgruppen. Der Kernel prüft jeden Zugriff mit diesen Nummern des Prozesses. Ein neuer Prozess erbt sie als Kopie von dem Prozess, der ihn startet. Das Programm, das eine Anmeldung durchführt, setzt sie einmal am Anfang einer Sitzung aus `/etc/passwd` und `/etc/group`.
:::

`id` ohne Namen fragt den Kernel nach den Nummern des eigenen Prozesses. Startest du `id` in einer neuen bash, die du mit `bash -c` aus [Kapitel 4](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/stroeme-umleitung-pipes-und-exit-status.html) aufrufst, zeigt es dieselben Nummern:

```console
$ bash -c id
uid=1000(student) gid=1000(student) groups=1000(student),27(sudo)
```

Die Shell hat ihre Nummern an die neue bash weitergegeben, diese an `id`. Abbildung [3](#abb-3) zeigt die Kette von der Anmeldung bis zu einem Programm. Weil jeder Prozess seine Kopie schon bei sich trägt, erreicht eine Änderung an `/etc/group` nach der Anmeldung die laufenden Prozesse nicht.

:::abbildung linux/k7prozess 3
Eine Kette von Prozessen von oben nach unten: das Anmeldeprogramm, darunter die Shell, darunter `bash -c`, darunter `id`. Zuerst liest das Anmeldeprogramm in `/etc/passwd` und `/etc/group` nach und klebt der Shell ein Etikett mit `uid=1000, gid=1000, Gruppen 1000, 27` auf. Dann geht eine Kopie des Etiketts in einem Schritt an die beiden neuen Prozesse. Die beiden Dateien bleiben danach grau: Die laufenden Prozesse schauen nicht mehr hinein.
:::

⁠**Kurz gesagt:** Jeder Prozess trägt die Benutzer- und Gruppennummern, für die er arbeitet; er erbt sie beim Start, und der Kernel prüft mit ihnen.

### Der Verwalter: root

<span class="anker" id="stufe-1-7"></span>

Irgendjemand muss das System pflegen dürfen: Programme einrichten, Einstellungen in `/etc` ändern, Konten anlegen. Unix löst das mit einem einzigen Benutzer, für den die Regeln dieses Kapitels fast nicht gelten.

:::definition Definition 1.6 (root)
<span class="anker" id="satz-1-6"></span>

__root__ ist der Benutzer mit der Benutzernummer 0. Für einen Prozess mit der Benutzernummer 0 überspringt der Kernel die Prüfung der Rechte an Dateien fast vollständig.
:::

Das „fast“ betrifft vor allem das Starten von Programmen. Den Namen `root` kennst du schon: Das Heimatverzeichnis von root ist `/root` ([Kapitel 3, Abschnitt 7.4](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/die-verzeichnisstruktur-von-linux.html#stufe-7-4)), und eine Shell, die als root läuft, zeigt am Ende der Eingabeaufforderung ein `#` statt eines `$` ([Kapitel 2, Abschnitt 1.4](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/terminal-und-shell.html#stufe-1-4)).

```console
$ ls -ld /root
drwx------ 4 root root 4096 Nov  4 15:32 /root
$ ls /root
ls: cannot open directory '/root': Permission denied
```

Das Verzeichnis `/root` gehört root, und `student` darf nicht hineinschauen.

⁠**Kurz gesagt:** root ist der Benutzer mit der Nummer 0; für ihn prüft der Kernel die Rechte an Dateien fast nicht.

:::hintergrund Warum es einen Verwalter gibt und warum man nicht als root arbeitet
Unix entstand auf großen Rechnern, an denen viele Menschen gleichzeitig über Terminals arbeiteten. Die Benutzer mussten voreinander geschützt werden: Keiner sollte die Dateien eines anderen lesen oder das System für alle lahmlegen können. Das gelingt nur, wenn die gewöhnlichen Konten wenig dürfen und ein besonderes Konto die Pflege übernimmt. Dieselbe Trennung schützt heute auch einen Rechner, an dem nur ein Mensch arbeitet: Ein Programm, das du startest, läuft mit deinen Rechten. Enthält es einen Fehler oder Schadcode, kann es deine Dateien beschädigen, aber nicht das System. Arbeitete man ständig als root, hätte jedes Programm alle Rechte, und diese Schutzschicht fiele weg.
:::

### Der Passwort-Prüfwert: /etc/shadow

<span class="anker" id="stufe-1-8"></span>

Beim Anmelden muss das System prüfen, ob das eingegebene Passwort stimmt. Es braucht dafür irgendetwas, mit dem es vergleichen kann. Das Passwort selbst zu speichern, wäre gefährlich: Wer die Datei liest, kennt alle Passwörter. Linux speichert deshalb etwas anderes.

:::definition Definition 1.7 (Passwort-Prüfwert, Schattendatei)
<span class="anker" id="satz-1-7"></span>

Der __Passwort-Prüfwert__ eines Benutzers ist ein Wert, der aus seinem Passwort berechnet wird, aus dem sich das Passwort aber nicht zurückrechnen lässt. Beim Anmelden berechnet das System den Wert aus dem eingegebenen Passwort neu und vergleicht. Die Prüfwerte stehen in der __Schattendatei__ `/etc/shadow`, einem Datensatz je Benutzer; das erste Feld ist der Name, das zweite der Prüfwert.
:::

Abbildung [4](#abb-4) zeigt die beiden Wege, die das System mit einem Passwort geht.

:::abbildung linux/k7pruefwert 4
Oben, beim Festlegen des Passworts: Das Passwort geht durch einen Kasten „Rechenweg“ und wird zum Prüfwert, einer langen, unleserlichen Zeichenfolge, die in die Zeile des Benutzers in `/etc/shadow` wandert. Ein Pfeil vom Prüfwert zurück zum Passwort wird rot durchgestrichen: Diesen Weg gibt es nicht. Unten, bei einer Anmeldung: Das eingegebene Passwort geht durch denselben Rechenweg; das Ergebnis wird mit dem gespeicherten Prüfwert verglichen, Gleichheit leuchtet grün.
:::

Ein Vergleich der beiden Dateien zeigt den entscheidenden Unterschied:

```console
$ ls -l /etc/passwd /etc/shadow
-rw-r--r-- 1 root root   1439 Nov 10 12:21 /etc/passwd
-rw-r----- 1 root shadow  731 Nov 10 12:21 /etc/shadow
$ cat /etc/shadow
cat: /etc/shadow: Permission denied
```

Die Benutzerliste darf jeder lesen, die Schattendatei nicht. Das ist Absicht. `/etc/passwd` muss für alle lesbar sein, denn viele Programme übersetzen mit ihr Nummern in Namen, `ls -l` zum Beispiel bei jeder Datei, die es zeigt. Die Prüfwerte dagegen sollen nur die Programme sehen, die eine Anmeldung prüfen. Deshalb steht im zweiten Feld von `/etc/passwd` nur ein `x`, und die Prüfwerte liegen in einer Datei, die root gehört und nur von root und der Gruppe `shadow` gelesen werden kann. Ein gültiger Prüfwert beginnt mit einem Kürzel für das Rechenverfahren, unter Ubuntu 26.04 mit `$y$` für das Verfahren yescrypt. Ein Eintrag, der mit `!` oder `*` beginnt, passt zu keinem Passwort; das Konto lässt sich dann nicht mit einem Passwort anmelden.

⁠**Kurz gesagt:** `/etc/shadow` enthält nicht die Passwörter, sondern Prüfwerte, aus denen sie sich nicht zurückrechnen lassen, und nur root darf die Datei lesen.

:::hintergrund Warum es zwei Dateien gibt
In den ersten Unix-Systemen standen die Prüfwerte im zweiten Feld von `/etc/passwd`, lesbar für alle. Damals schien das sicher: Ein Prüfwert verrät das Passwort nicht, und die Rechner waren zu langsam, um für ein gut gewähltes Passwort alle Möglichkeiten durchzuprobieren. Mit schnelleren Rechnern änderte sich das. Wer die Prüfwerte kopieren konnte, probierte zu Hause in Ruhe Wörter aus einem Wörterbuch durch, berechnete für jedes den Prüfwert und verglich. Die Prüfwerte wanderten deshalb in eine eigene Datei, die gewöhnliche Benutzer nicht lesen können. Wie ein Prüfwert berechnet wird und warum er das Raten bremst, ist ein Thema der Reihe Cybersecurity.
:::

### Aufgaben zu Abschnitt [1](#stufe-1)

<span class="anker" id="stufe-1-9"></span>

:::aufgabe Aufgabe 1 ★ Die Konten deines Systems
<span class="anker" id="aufg-1"></span>

(a) Wie viele Konten stehen in `/etc/passwd` deines Systems, und wie viele davon gehören Menschen? (b) Welche Konten haben `/bin/bash` als Programm nach der Anmeldung? Antworte mit `awk` oder `grep`. (c) Was geschieht, wenn jemand versucht, sich als `daemon` anzumelden, und warum ist das gewollt?

:::loesung
```console
$ wc -l /etc/passwd
28 /etc/passwd
$ awk -F: '$3 >= 1000 && $3 != 65534' /etc/passwd | wc -l
1
$ awk -F: '$7 == "/bin/bash" {print $1}' /etc/passwd
root
student
$ /usr/sbin/nologin
This account is currently not available.
$ echo $?
1
```

(a) Das Testsystem hat 28 Konten. Menschen haben Nummern ab 1000; `nobody` mit 65534 liegt zwar darüber, ist aber ein Systemkonto und wird deshalb mit `$3 != 65534` ausgeschlossen. Es bleibt ein Mensch, `student`. Auf deinem System können beide Zahlen anders sein. (b) Das siebte Feld vergleicht `awk` als Text mit `/bin/bash`; das trifft auf `root` und `student` zu. (c) Bei einer Anmeldung als `daemon` startet statt einer Shell das Programm `/usr/sbin/nologin`. Es schreibt „This account is currently not available.“ und endet mit dem Exit-Status 1, die Sitzung ist damit vorbei. Das ist gewollt: Unter `daemon` sollen nur Dienste laufen, kein Mensch soll sich so anmelden und mit dessen Rechten arbeiten können.
:::
:::

:::aufgabe Aufgabe 2 ★ Eine Zeile von id deuten
<span class="anker" id="aufg-2"></span>

Auf einem anderen Rechner zeigt `id` die Zeile `uid=1001(lea) gid=1001(lea) groups=1001(lea),27(sudo),100(users)`. (a) Wie lauten Benutzernummer und Hauptgruppe? (b) Welche Zusatzgruppen hat `lea`? (c) In welchen Zeilen von `/etc/group` steht `lea` in der Mitgliederliste, in welcher nicht, und warum?

:::loesung
(a) Die Benutzernummer ist 1001 (`uid=1001`), die Hauptgruppe ist `lea` mit der Nummer 1001 (`gid=1001`). (b) Die Zusatzgruppen sind alle Gruppen hinter `groups` außer der Hauptgruppe: `sudo` (27) und `users` (100). (c) `lea` steht in den Mitgliederlisten der Zeilen `sudo:x:27:…` und `users:x:100:…` von `/etc/group`. In der Zeile ihrer eigenen Gruppe `lea:x:1001:` steht sie nicht: Diese Gruppe ist ihre Hauptgruppe, und die Hauptgruppe steht im vierten Feld von `/etc/passwd`, nicht in der Mitgliederliste.
:::
:::

:::aufgabe Aufgabe 3 ★★ Zwei Dateien, zwei Rechte
<span class="anker" id="aufg-3"></span>

(a) Warum darf jeder `/etc/passwd` lesen? Nenne ein Programm aus diesem Kapitel, das sonst nicht wie gewohnt arbeiten könnte. (b) Was stünde im zweiten Feld von `/etc/passwd`, wenn die Prüfwerte noch dort lägen, und welche Gefahr entstünde daraus? (c) Ein Prüfwert beginnt mit `*`. Was bedeutet das für das Konto?

:::loesung
(a) Viele Programme übersetzen Nummern in Namen und schlagen dafür in `/etc/passwd` nach. `ls -l` zeigt bei jeder Datei den Namen des Besitzers, `id` die Namen hinter den Nummern; ohne Leserecht sähe man nur Zahlen, wie bei `ls -n`. (b) Im zweiten Feld stünde der Passwort-Prüfwert jedes Benutzers. Jeder könnte die Prüfwerte kopieren und in Ruhe Passwörter durchprobieren, indem er für jedes geratene Wort den Prüfwert berechnet und vergleicht. (c) Ein Prüfwert, der mit `*` beginnt, passt zu keinem Passwort. Das Konto lässt sich nicht mit einem Passwort anmelden; so ist root unter Ubuntu abgesichert.
:::
:::

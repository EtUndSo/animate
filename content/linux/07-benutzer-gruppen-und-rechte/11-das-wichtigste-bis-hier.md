---
title: Das Wichtigste bis hier
pfad: Informatik / Linux und Kommandozeile / Benutzer, Gruppen und Rechte
adresse: informatik/linux-und-kommandozeile/benutzer-gruppen-und-rechte
knoten: Kapitel 7: Benutzer, Gruppen und Rechte
order: 6121100
summary: Wer eine Datei lesen, ändern oder starten darf, wie Linux das bei jedem Zugriff entscheidet und wie man mit den Rechten des Administrators sicher arbeitet
tags: 
lang: de
---

:::kern Das Wichtigste bis hier
<ul>

<li>

Benutzer und Gruppen haben Namen für Menschen und Nummern (UID, GID) für den Kernel; die Zuordnung steht in `/etc/passwd` und `/etc/group`, die Passwort-Prüfwerte in der nur für root lesbaren `/etc/shadow`. root hat die Nummer 0.

</li>

<li>

Jeder Benutzer hat eine Hauptgruppe und Zusatzgruppen. Jeder Prozess trägt die Nummern seines Benutzers als Kopie; sie stammen von der Anmeldung, deshalb wirken neue Gruppen erst nach einer neuen Anmeldung.

</li>

<li>

Jede Datei hat einen Besitzer, eine Gruppe und neun Rechte `rwx` für die Klassen Besitzer, Gruppe und andere. `chmod` ändert sie symbolisch (`u+x`, `go=r`) oder oktal ($r = 4$, $w = 2$, $x = 1$, etwa 750); das darf nur der Besitzer oder root.

</li>

<li>

Bei Verzeichnissen heißt `r` Namen lesen, `x` hindurchgehen, `w` mit `x` Einträge anlegen, löschen und umbenennen. Löschen ändert das Verzeichnis, nicht die Datei.

</li>

<li>

Der Kernel prüft beim Öffnen: jedes Verzeichnis auf dem Pfad braucht `x`; dann gilt root, sonst die erste passende Klasse aus Besitzer, Gruppe, andere. Ein offener Deskriptor behält seinen Zugriff.

</li>

<li>

`sudo befehl` führt einen Befehl als root aus, erlaubt durch `/etc/sudoers`, mit dem eigenen Passwort, protokolliert in `/var/log/auth.log`. Umleitungen öffnet die Shell ohne `sudo`; als root schreibt man mit `| sudo tee`.

</li>

<li>

`adduser`, `addgroup`, `usermod -aG` und `deluser` verwalten Konten; `chown` (nur root) und `chgrp` ändern Besitzer und Gruppe. Die umask nimmt neuen Dateien Bits weg (verlangt UND NICHT umask).

</li>

<li>

SUID (4000) leiht einem Programm die effektive Benutzernummer seines Besitzers, bei Skripten nicht; SGID (2000) leiht die Gruppe oder vererbt sie in einem Verzeichnis; Sticky (1000) lässt in einem Verzeichnis nur eigene Dateien löschen.

</li>

</ul>
:::

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Linux entscheidet jeden Zugriff im Kernel beim Öffnen, indem es die Nummern des Prozesses mit Besitzer, Gruppe und den neun Rechten der Datei und jedes Verzeichnisses auf dem Weg vergleicht und die erste passende Klasse nimmt.

</li>

<li>

Eine Datei löschen kann, wer ihr Verzeichnis schreiben darf, weil Löschen nur einen Namen aus der Tabelle des Verzeichnisses streicht, außer das Sticky-Bit verbietet es.

</li>

<li>

Arbeiten mit den Rechten des Verwalters erledigt man mit `sudo` für einzelne Befehle, das selbst über das SUID-Bit root wird, protokolliert und auf erlaubte Benutzer beschränkt ist.

</li>

</ol>
:::

**Ein Prinzip hinter allen Ergebnissen.** Fast alles in diesem Kapitel folgt aus zwei Gedanken. Erstens: Der Kernel vergleicht Nummern, die ein Prozess bei sich trägt, mit Nummern und Bits, die an einem Objekt hängen, und zwar an genau dem Objekt, das verändert wird: am Inhalt einer Datei beim Lesen und Schreiben, an der Tabelle eines Verzeichnisses beim Anlegen und Löschen. Zweitens: Diese Nummern erbt ein Prozess bei seinem Start und behält sie; nur wenige, sorgfältig gebaute Programme dürfen sie ändern.

| Ergebnis | Woher es kommt |
|---|---|
| `ls -l` zeigt Namen, `ls -n` Zahlen | in der Inode stehen nur Nummern (Abschnitte [1](benutzer-und-gruppen.html#stufe-1) und [2](die-rechte-einer-datei.html#stufe-2)) |
| `cat /etc/shadow` meldet Permission denied | nur root und die Gruppe `shadow` dürfen lesen (Abschnitt [1](benutzer-und-gruppen.html#stufe-1)) |
| `ls fach` klappt, `cat fach/brief.txt` nicht | `r` ohne `x` am Verzeichnis (Abschnitt [4](rechte-bei-verzeichnissen.html#stufe-4)) |
| ein schreibgeschützter Brief lässt sich löschen | Löschen ändert das Verzeichnis (Abschnitt [4](rechte-bei-verzeichnissen.html#stufe-4)) |
| `cat weg/innen/zettel.txt` scheitert trotz `rw-r--r--` | `weg` fehlt das `x` (Abschnitt [5](wie-der-kernel-rechte-pruft.html#stufe-5)) |
| der Besitzer kann `----r--r--` nicht lesen | die erste passende Klasse gilt (Abschnitt [5](wie-der-kernel-rechte-pruft.html#stufe-5)) |
| `tail -f` liest weiter, `cat` nicht | geprüft wird beim Öffnen (Abschnitt [5](wie-der-kernel-rechte-pruft.html#stufe-5)) |
| `sudo cat` liest eine Datei mit 000 | für die Nummer 0 entfällt die Prüfung (Abschnitt [6](kurzzeitig-root-sudo-und-su.html#stufe-6)) |
| `sudo echo … > datei` meldet `bash: … Permission denied` | die Shell öffnet die Datei vor `sudo` (Abschnitt [6](kurzzeitig-root-sudo-und-su.html#stufe-6)) |
| `id` kennt die neue Gruppe nicht, `id "$USER"` schon | die Shell trägt ihre Kopie von der Anmeldung (Abschnitt [7](benutzer-und-gruppen-anlegen.html#stufe-7)) |
| `anna` darf einen Aushang mit 604 nicht lesen | sie passt auf die Klasse Gruppe (Abschnitt [7](benutzer-und-gruppen-anlegen.html#stufe-7)) |
| `chown` ohne `sudo` scheitert auch bei eigenen Dateien | nur root darf den Besitzer ändern (Abschnitt [8](besitz-und-voreinstellungen-chown-chgrp-und-umask.html#stufe-8)) |
| `umask 033` ergibt 644, nicht 633 | Bits werden weggenommen, nicht abgezogen (Abschnitt [8](besitz-und-voreinstellungen-chown-chgrp-und-umask.html#stufe-8)) |
| `./meinid` meldet `euid=0` | das SUID-Bit leiht die Nummer des Besitzers (Abschnitt [9](programme-ausfuhren-und-besondere-rechte.html#stufe-9)) |
| ein SUID-Skript läuft ohne `euid=0` | Linux ignoriert SUID bei Skripten (Abschnitt [9](programme-ausfuhren-und-besondere-rechte.html#stufe-9)) |
| `anna` kann in `ablage` nur eigene Dateien löschen | das Sticky-Bit (Abschnitt [9](programme-ausfuhren-und-besondere-rechte.html#stufe-9)) |
| nach `deluser` zeigt `ls` die Zahl 1001 | für den Kernel ist ein Benutzer eine Zahl (Abschnitt [9](programme-ausfuhren-und-besondere-rechte.html#stufe-9)) |

---
title: Das Wichtigste bis hier
pfad: Informatik / Linux und Kommandozeile / Software installieren: Paketverwaltung
adresse: informatik/linux-und-kommandozeile/software-installieren-paketverwaltung
knoten: Kapitel 9: Software installieren: Paketverwaltung
order: 6141200
summary: Woraus ein Paket besteht, woher es kommt, wie man Software installiert, aktualisiert und spurlos entfernt, und warum man den Paketen aus dem Netz trauen kann
tags: 
lang: de
---

:::kern Das Wichtigste bis hier
<ul>

<li>

Ein Paket ist eine Archivdatei mit den Dateien einer Software samt Zielort, einer Beschreibung (Name, Version, Architektur, Beziehungen) und Wartungsskripten, die als `root` laufen. Die Version lautet `[Epoche:]Programmversion-Revision`.

</li>

<li>

Pakete hängen voneinander ab (`Depends`, `Pre-Depends`), empfehlen (`Recommends`, voreingestellt mitinstalliert) und schlagen vor (`Suggests`), schließen einander aus (`Conflicts`) und erfüllen virtuelle Namen (`Provides`).

</li>

<li>

`dpkg` installiert einzelne Paketdateien und führt die Paketdatenbank unter `/var/lib/dpkg`; `dpkg -l`, `-L`, `-S` und `-s` fragen sie ab. `apt` löst Abhängigkeiten auf, lädt, prüft und lässt `dpkg` installieren.

</li>

<li>

Die Quellenliste `ubuntu.sources` in `/etc/apt/sources.list.d` nennt Server, Ausgaben (`resolute`, `-updates`, `-security`, `-backports`) und Bereiche (`main`, `restricted`, `universe`, `multiverse`); `sudo apt update` holt die Paketlisten und installiert nichts.

</li>

<li>

`apt search`, `show`, `list`, `policy` und `apt-cache depends` beantworten Fragen ohne `root`; die Kandidatenversion hat die höchste Priorität, dann die höchste Version.

</li>

<li>

`apt -s` simuliert. `sudo apt install`, `remove` (Konfigurationsdateien bleiben), `purge`, `autoremove` und `upgrade` verändern das System; eine Sperrdatei lässt nur einen Vorgang zur Zeit zu.

</li>

<li>

Eine signierte Release-Datei enthält die Prüfsummen der Paketlisten, diese die Prüfsummen der Paketdateien; `Signed-By` legt den Schlüsselbund fest. Spiegelserver und `http` müssen deshalb nicht vertrauenswürdig sein.

</li>

<li>

Sicherheitsupdates kommen über `resolute-security` und täglich von selbst über `unattended-upgrades`; laufende Programme benutzen bis zum Neustart die alte Fassung.

</li>

<li>

Das Alternativsystem wählt per Link in `/etc/alternatives` zwischen Programmen gleicher Aufgabe (`awk`, `sudo`); die Grundbefehle wählt das Paket `coreutils-from-uutils` bzw. `-gnu`.

</li>

<li>

Zusätzliche Quellen, einzelne `.deb`-Dateien und `curl … | bash` umgehen Teile der Prüfungen; Snaps bündeln ihre Bibliotheken.

</li>

</ul>
:::

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Unter Linux installiert man Software als Pakete aus den Paketquellen der Distribution: `apt` löst die Abhängigkeiten auf, lädt die Paketdateien und lässt `dpkg` sie auspacken und einrichten, nach `apt update` und mit `apt upgrade` auch neue Versionen.

</li>

<li>

Vollständig entfernen lässt sich ein Paket, weil `dpkg` beim Installieren jede seiner Dateien in die Paketdatenbank einträgt und beim Entfernen genau diese Liste abarbeitet, mit `purge` samt Konfigurationsdateien und mit `autoremove` samt überflüssig gewordenen Abhängigkeiten.

</li>

<li>

Einer heruntergeladenen Paketdatei kann der Rechner trauen, weil Ubuntu die Release-Datei mit seinem geheimen Archivschlüssel signiert, diese die Prüfsummen der Paketlisten und jene die Prüfsummen jeder Paketdatei enthalten, sodass `apt` mit dem öffentlichen Schlüssel jede Veränderung erkennt, gleichgültig über welchen Server die Dateien kamen.

</li>

</ol>
:::

**Ein Prinzip hinter allen Ergebnissen.** Fast alles in diesem Kapitel folgt aus zwei Gedanken. Erstens: Die Paketverwaltung führt Buch über jedes Paket und jede seiner Dateien und ändert das System nur über diese Buchführung; deshalb kann sie sauber entfernen, aktualisieren und Konflikte erkennen. Zweitens: Vertraut wird nur einer einzigen signierten Liste je Ausgabe, und alles Weitere ist über Prüfsummen an sie gekettet; deshalb darf der Weg, auf dem die Dateien kommen, unsicher sein.

| Ergebnis | Woher es kommt |
|---|---|
| `jq` bringt nur drei neue Pakete mit | `libc6` ist schon installiert, jedes Paket kommt nur einmal (Abschnitt [1](pakete-und-ihre-beziehungen.html#stufe-1)) |
| `fortune-mod` bringt `fortunes-min` mit | Empfehlungen installiert Ubuntu in der Voreinstellung mit (Abschnitt [1](pakete-und-ihre-beziehungen.html#stufe-1)) |
| `dpkg -S /usr/bin/ls` nennt `coreutils-from-uutils` | die Paketdatenbank kennt zu jeder Datei ihr Paket (Abschnitt [2](die-paketverwaltung-und-ihre-datenbank.html#stufe-2)) |
| `dpkg -S /etc/hostname` findet nichts | die Datei hat kein Paket angelegt (Abschnitt [2](die-paketverwaltung-und-ihre-datenbank.html#stufe-2)) |
| `apt update` installiert nichts | es ersetzt nur die Paketlisten (Abschnitt [3](paketquellen-und-paketlisten.html#stufe-3)) |
| Kandidat von `rust-coreutils` ist 0.10.0 | gleiche Priorität 500, dann höchste Version (Abschnitt [4](pakete-suchen-und-ansehen.html#stufe-4)) |
| ausgepacktes `hello` läuft, `dpkg -l` kennt es nicht | Installieren ist Auspacken plus Buchführung (Abschnitt [5](ein-paket-von-innen.html#stufe-5)) |
| ausgepacktes `sl` startet nicht | seine Abhängigkeit `libncurses6` fehlt (Abschnitt [5](ein-paket-von-innen.html#stufe-5)) |
| `apt install` ohne `sudo`: `Permission denied` | die Sperrdatei gehört `root` (Abschnitt [6](installieren-entfernen-aktualisieren.html#stufe-6)) |
| `apt -s` braucht kein `root` | eine Simulation ändert nichts und sperrt nichts (Abschnitt [6](installieren-entfernen-aktualisieren.html#stufe-6)) |
| `remove cron` lässt `/etc` stehen, `purge` nicht | Konfigurationsdateien sind in `cron.conffiles` vermerkt (Abschnitt [6](installieren-entfernen-aktualisieren.html#stufe-6)) |
| ein geändertes Byte, eine völlig andere Prüfsumme | SHA-256 (Abschnitt [7](warum-man-den-paketen-trauen-kann.html#stufe-7)) |
| `gpgv`: `Good signature` | nur der Besitzer des geheimen Archivschlüssels kann signieren (Abschnitt [7](warum-man-den-paketen-trauen-kann.html#stufe-7)) |
| `http` genügt | die Kette aus Signatur und Prüfsummen prüft jede Datei selbst (Abschnitt [7](warum-man-den-paketen-trauen-kann.html#stufe-7)) |
| `(deleted)` hinter der Programmdatei | der laufende Prozess behält die alte Datei, der Name gehört der neuen (Abschnitt [8](aktualisieren-als-schutz.html#stufe-8)) |
| `dpkg -S /usr/bin/sudo` findet nichts | den Link hat das Alternativsystem angelegt, kein Paket (Abschnitt [9](alternativen-ein-befehl-mehrere-pakete.html#stufe-9)) |
| der Wechsel auf GNU nähme `build-essential` mit | es hängt von `coreutils-from-uutils` ab (Abschnitt [9](alternativen-ein-befehl-mehrere-pakete.html#stufe-9)) |
| `apt` warnt vor dem Entfernen von `grep` | `Essential: yes` (Abschnitt [9](alternativen-ein-befehl-mehrere-pakete.html#stufe-9)) |

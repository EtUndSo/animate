---
title: Protokolle: das Journal
pfad: Informatik / Linux und Kommandozeile / Prozesse, Signale und Dienste
adresse: informatik/linux-und-kommandozeile/prozesse-signale-und-dienste
knoten: Kapitel 8: Prozesse, Signale und Dienste
order: 6130900
summary: Dienste haben kein Terminal, in das sie Meldungen schreiben könnten.
tags: Journal
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Dienste haben kein Terminal, in das sie Meldungen schreiben könnten. Trotzdem will man wissen, was sie tun und warum einer abgestürzt ist. Dieser Abschnitt zeigt, wo Linux die Meldungen aller Dienste sammelt, wie man sie gezielt liest und wer welche Meldungen lesen darf.
:::

### Das Journal

<span class="anker" id="stufe-8-1"></span>

[Kapitel 3, Abschnitt 7.5](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/die-verzeichnisstruktur-von-linux.html#stufe-7-5) hat Protokolldateien unter `/var/log` gezeigt. Neben ihnen gibt es auf Systemen mit `systemd` eine zentrale Sammelstelle für Meldungen.

:::definition Definition 8.1 (Journal, journalctl)
<span class="anker" id="satz-8-1"></span>

Das __Journal__ ist die Sammlung von Meldungen, die der Dienst `systemd-journald` führt. Er nimmt die Meldungen des Kernels, die Ausgaben aller Dienste, die `systemd` startet, und die Meldungen von `systemd` selbst entgegen und speichert jede mit Zeit, Rechner, Programm, PID und Unit. Gelesen wird das Journal mit `journalctl`.
:::

```console
$ ls /var/log
README            chrony        dmesg.3.gz      landscape
alternatives.log  dist-upgrade  dmesg.4.gz      lastlog
apt               dmesg         dpkg.log        private
auth.log          dmesg.0       fontconfig.log  syslog
bootstrap.log     dmesg.1.gz    journal         unattended-upgrades
btmp              dmesg.2.gz    kern.log        wtmp
$ ls -l /var/log/journal
total 12
drwxr-sr-x+2 root systemd-journal 12288 Nov 10 15:24 7466df72a38b4c519913497933f0e613
```

Das Journal liegt in `/var/log/journal` in einem Verzeichnis, das nach einer Kennung des Rechners benannt ist; dort übersteht es jeden Neustart. Ubuntu legt das Verzeichnis bei der Installation an. Fehlt es auf einem System, hält `systemd-journald` die Meldungen nur im Arbeitsspeicher, unter `/run/log/journal`, und sie gehen beim Herunterfahren verloren. Die Dateien des Journals sind keine Textdateien; man liest sie nicht mit `less`, sondern mit `journalctl`, das nach Unit, Zeit und Wichtigkeit filtern kann. Die Textdateien daneben, etwa `syslog` und `auth.log`, schreibt der Dienst `rsyslogd`, der eine Kopie der Meldungen bekommt. Abbildung [30](#abb-30) zeigt, woher die Meldungen kommen.

:::abbildung linux/k8journal 30
Links die Quellen: Kernel, die Dienste cron und k8eieruhr (ihre Ausgabe), systemd selbst. Pfeile führen zu `systemd-journald` in der Mitte; jede Meldung bekommt dort einen Zettel mit Zeit, Rechner, Programm[PID] und Unit. Rechts zwei Ablagen: das Journal des Systems und das Journal des Benutzers 1000. Ganz rechts `journalctl` mit drei Filtern (`-u`, `-b`, `-n`), durch die nur passende Zettel fallen. Ein Seitenpfeil von journald zu `rsyslogd` und weiter zu den Textdateien `/var/log/syslog` und `auth.log`.
:::

⁠**Kurz gesagt:** `systemd-journald` sammelt die Meldungen von Kernel, Diensten und `systemd` im Journal; `journalctl` liest und filtert es.

### Die Meldungen einer Unit: journalctl -u

<span class="anker" id="stufe-8-2"></span>

Das ganze Journal ist lang. Meist interessiert nur, was ein bestimmter Dienst gemeldet hat.

:::definition Definition 8.2 (journalctl -u, -n, `--user`)
<span class="anker" id="satz-8-2"></span>

`journalctl -u unit` zeigt nur die Meldungen dieser Unit, auch die, die `systemd` über sie schreibt. `-n zahl` zeigt nur die letzten so vielen Meldungen. Für Benutzerdienste schreibt man `--user` dazu.
:::

```console
$ systemctl --user start k8eieruhr
$ journalctl --user -u k8eieruhr -n 7
Nov 10 15:29:09 labor systemd[383]: Stopped k8eieruhr.service - Eieruhr zum Üben.
Nov 10 15:29:09 labor systemd[383]: Started k8eieruhr.service - Eieruhr zum Üben.
Nov 10 15:29:10 labor systemd[383]: k8eieruhr.service: Main process exited, code=killed, status=9/KILL
Nov 10 15:29:10 labor systemd[383]: k8eieruhr.service: Failed with result 'signal'.
Nov 10 15:29:11 labor systemd[383]: k8eieruhr.service: Scheduled restart job, restart counter is at 1.
Nov 10 15:29:11 labor systemd[383]: Started k8eieruhr.service - Eieruhr zum Üben.
Nov 10 15:29:19 labor systemd[383]: Started k8eieruhr.service - Eieruhr zum Üben.
```

Jede Zeile beginnt mit Datum und Uhrzeit, dem Namen des Rechners und dem Programm, das die Meldung geschrieben hat, mit seiner PID in eckigen Klammern; hier ist das immer die Benutzerinstanz von `systemd`, PID 383. Die Zeilen erzählen die Geschichte der Eieruhr aus Abschnitt [7](dienste-und-systemd.html#stufe-7): gestoppt, gestartet, durch SIGKILL beendet, neu gestartet und zuletzt wieder gestartet. Das Journal bewahrt die Meldungen auch über einen Neustart hinweg auf; wer die Versuche mehrmals macht, sieht deshalb auch ältere Zeilen.

⁠**Kurz gesagt:** `journalctl -u unit -n zahl` zeigt die letzten Meldungen einer Unit, mit `--user` die eines Benutzerdienstes.

### Mitlesen: journalctl -f

<span class="anker" id="stufe-8-3"></span>

Bei einem Fehler will man oft zusehen, was ein Dienst meldet, während man ihn neu startet. Wie `tail -f` bei einer Textdatei ([Kapitel 6, Abschnitt 1.6](/wissen/informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke/textdaten-datensatze-felder-und-zeilenenden.html#stufe-1-6)) kann `journalctl` neuen Meldungen folgen.

:::definition Definition 8.3 (journalctl -f)
<span class="anker" id="satz-8-3"></span>

`journalctl -f` zeigt die letzten Meldungen und wartet dann auf neue, die es sofort ausgibt, bis man Strg+C drückt. Mit `-u` und `-n` lässt es sich kombinieren.
:::

Öffne wieder ein zweites Terminal. Im ersten folgst du den Meldungen der laufenden Eieruhr; während `journalctl` wartet, startest du den Dienst im zweiten Terminal neu. Im ersten Terminal:

```console
$ journalctl --user -u k8eieruhr -f -n 1
Nov 10 15:29:19 labor systemd[383]: Started k8eieruhr.service - Eieruhr zum Üben.
Nov 10 15:29:25 labor systemd[383]: Stopping k8eieruhr.service - Eieruhr zum Üben...
Nov 10 15:29:25 labor systemd[383]: Stopped k8eieruhr.service - Eieruhr zum Üben.
Nov 10 15:29:25 labor systemd[383]: Started k8eieruhr.service - Eieruhr zum Üben.
^C
$ systemctl --user stop k8eieruhr
```

Im zweiten Terminal:

```console
$ systemctl --user restart k8eieruhr
```

Die erste Zeile ist die letzte alte Meldung (`-n 1`); die drei Zeilen darauf erschienen in dem Augenblick, in dem `restart` den Dienst stoppte und wieder startete. Abbildung [31](#abb-31) zeigt das Zusammenspiel der beiden Fenster.

:::abbildung linux/k8journalfolgen 31
Die beiden Terminals aus den Blöcken oben untereinander, jede Zeile im vollen Wortlaut. Oben läuft `journalctl --user -u k8eieruhr -f -n 1`, zeigt die letzte alte Meldung und wartet (das Warten kennt man von `tail -f`, es bleibt ruhig im Hintergrund). Unten wird `systemctl --user restart k8eieruhr` getippt. Betont wird der Weg der Meldungen: Der Befehl geht an `systemd --user`, das den Dienst stoppt und startet und dabei drei Meldungen an `systemd-journald` schickt; von dort erscheinen sie oben nacheinander als „Stopping …“, „Stopped …“, „Started …“, jede mit derselben Uhrzeit. Zuletzt beendet Strg+C das Mitlesen.
:::

Zum Schluss stoppst du die Eieruhr. Ohne `-f` und mit langer Ausgabe zeigt `journalctl` wie `systemctl` den Seitenanzeiger `less`; `q` beendet ihn, `--no-pager` schaltet ihn ab.

⁠**Kurz gesagt:** `journalctl -f` zeigt neue Meldungen, sobald sie entstehen, bis Strg+C.

### Seit dem Start: journalctl -b und `--since`

<span class="anker" id="stufe-8-4"></span>

Nach einem Neustart interessieren meist nur die Meldungen seit dem Hochfahren, bei einer Fehlersuche nur die der letzten Minuten. Das Journal merkt sich deshalb zu jeder Meldung, zu welchem Start des Systems sie gehört.

:::definition Definition 8.4 (journalctl -b, `--list-boots`, `--since`)
<span class="anker" id="satz-8-4"></span>

`journalctl -b` zeigt nur die Meldungen seit dem letzten Start, `-b -1` die des vorletzten. `journalctl --list-boots` listet die Starts, die das Journal kennt. `--since zeit` zeigt die Meldungen ab einem Zeitpunkt, etwa `--since today` oder `--since "10 minutes ago"`.
:::

```console
$ journalctl --list-boots
Hint: You are currently not seeing messages from other users and the system.
      Users in groups 'adm', 'systemd-journal' can see all messages.
      Pass -q to turn off this notice.
IDX BOOT ID                          FIRST ENTRY                 LAST ENTRY
...
 -1 e231b94455e94213baf36827f998a5d0 Tue 2026-11-10 14:59:00 CET Tue 2026-11-10 15:23:24 CET
  0 7452da1fadaf4375aefc3312166f38d2 Tue 2026-11-10 15:24:43 CET Tue 2026-11-10 15:29:31 CET
$ sudo journalctl -b -u cron --no-pager | head -n 3
Nov 10 15:24:41 labor systemd[1]: Started cron.service - Regular background program processing daemon.
Nov 10 15:24:41 labor (cron)[160]: cron.service: Referenced but unset environment variable evaluates to an empty string: EXTRA_OPTS
Nov 10 15:24:41 labor cron[160]: (CRON) INFO (pidfile fd = 3)
$ journalctl --user -u k8eieruhr --since "10 minutes ago" -n 2
Nov 10 15:29:31 labor systemd[383]: Stopping k8eieruhr.service - Eieruhr zum Üben...
Nov 10 15:29:31 labor systemd[383]: Stopped k8eieruhr.service - Eieruhr zum Üben.
```

Die Starts sind von 0 (der laufende) rückwärts nummeriert; jeder hat eine lange Kennung und die Zeiten seiner ersten und letzten Meldung. Die älteren Starts sind im Kapitel weggelassen. Auf dem Testsystem kennt das Journal an diesem Tag über zwanzig Starts: Unter WSL zählt jedes Hochfahren der WSL-Umgebung als Start, und Windows fährt sie herunter, wenn eine Weile kein Linux-Programm läuft. Auf einem gewöhnlichen Linux ist ein Start ein Hochfahren des Rechners. Die drei Meldungen von `cron` seit dem Start beginnen mit der von `systemd` (PID 1), dass es den Dienst gestartet hat. Ganz oben steht ein Hinweis: `student` sieht nicht alle Meldungen.

⁠**Kurz gesagt:** `journalctl -b` zeigt die Meldungen seit dem letzten Start, `--since` die seit einem Zeitpunkt.

### Wer welche Meldungen lesen darf

<span class="anker" id="stufe-8-5"></span>

Meldungen verraten viel: wer sich wann angemeldet hat, welche Befehle mit `sudo` liefen, welche Fehler ein Dienst hatte. Deshalb darf nicht jeder alles lesen.

:::satz Satz 8.5 (Rechte am Journal)
<span class="anker" id="satz-8-5"></span>

Liegt das Journal auf dem Datenträger unter `/var/log/journal`, darf jeder Benutzer die Meldungen seiner eigenen Prozesse und Benutzerdienste lesen. Die Meldungen des Systems und anderer Benutzer dürfen nur root und die Mitglieder der Gruppen `adm` und `systemd-journal` lesen.
:::

```console
$ journalctl -u cron -n 3
Hint: You are currently not seeing messages from other users and the system.
      Users in groups 'adm', 'systemd-journal' can see all messages.
      Pass -q to turn off this notice.
-- No entries --
$ getent group adm systemd-journal
adm:x:4:syslog
systemd-journal:x:999:
```

`student` gehört auf dem Testsystem zu keiner der beiden Gruppen und sieht deshalb keine Meldung von `cron`; mit `sudo` gelang es oben. Abbildung [32](#abb-32) zeigt, wer welchen Teil lesen darf.

:::abbildung linux/k8journalrechte 32
Zwei Ablagen des Journals: „System“ (Kernel, cron, sudo, systemd) und „Benutzer 1000“ (k8eieruhr). Davor nacheinander drei Leser. `student` kommt an die eigene Ablage (grün), an die des Systems nicht (rotes Schloss, der Hinweis „not seeing messages“ erscheint). Ein Mitglied der Gruppe `adm` kommt an beide. Root (über `sudo`) kommt an beide. Zum Schluss leuchtet die Zeile `adm:x:4:syslog` aus `/etc/group` auf: student fehlt in der Liste; daneben klein dieselbe Zeile mit dem ersten Benutzer einer gewöhnlichen Installation darin.
:::

`getent group` zeigt die Zeilen der Gruppen aus `/etc/group` ([Kapitel 7, Abschnitt 1.3](/wissen/informatik/linux-und-kommandozeile/benutzer-gruppen-und-rechte/benutzer-und-gruppen.html#stufe-1-3)). Dass `student` in keiner der beiden Gruppen ist, erklärt auch, warum `systemctl status cron` in Unterabschnitt [7.4](dienste-und-systemd.html#stufe-7-4) keine Meldungen zeigte. Eine gewöhnliche Ubuntu-Installation, am Desktop wie unter WSL, nimmt den ersten Benutzer dagegen in die Gruppe `adm` auf. Steht dein Name in der Zeile von `adm`, siehst du alle Meldungen ohne `sudo` und ohne den Hinweis. Wie man in Protokollen gezielt nach Spuren von Angriffen sucht, behandelt die Reihe Cybersecurity.

⁠**Kurz gesagt:** Eigene Meldungen darf jeder lesen, die des Systems nur root und die Gruppen `adm` und `systemd-journal`.

### Aufräumen

<span class="anker" id="stufe-8-6"></span>

Zum Schluss entfernst du den Übungsdienst, prüfst, dass keine Versuchsprogramme mehr laufen, und löschst das Übungsverzeichnis samt `nohup.out`. Die Eieruhr ist schon gestoppt und nicht mehr eingeschaltet; es bleibt die Unit-Datei. Ein zweites Terminal, das noch offen ist, schließt du vorher.

```console
$ rm ~/.config/systemd/user/k8eieruhr.service
$ systemctl --user daemon-reload
$ systemctl --user status k8eieruhr
Unit k8eieruhr.service could not be found.
$ pgrep -a -x sleep
$ cd
$ rm -r ~/linuxk8
```

Nach `daemon-reload` kennt `systemd` die Eieruhr nicht mehr. `pgrep` findet kein `sleep` mehr. `cd` ohne Argument führt ins Heimatverzeichnis, damit die Shell nicht im gelöschten Verzeichnis steht; `rm -r` löscht dann das Übungsverzeichnis mit allem darin ([Kapitel 3, Abschnitt 6.5](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/kopieren-verschieben-loschen.html#stufe-6-5)). Die Verzeichnisse unter `~/.config/systemd` lässt du stehen, denn darin können auch andere Einstellungen liegen. Die Meldungen der Eieruhr bleiben im Journal; `systemd-journald` löscht ältere Meldungen nach und nach von selbst, sobald das Journal eine Größengrenze erreicht. Selbst löschen solltest du darin nichts.

⁠**Kurz gesagt:** Eine eigene Unit entfernt man mit Stoppen, `disable`, Löschen der Datei und `daemon-reload`.

**Zum Weiterüben.** Die frei zugängliche Übungsplattform pwn.college bietet unter dem Namen „Linux Luminarium“ kleine Aufgaben im Browser an; das Modul „Processes and Jobs“ passt zu diesem Kapitel. Es läuft auf einem fremden Rechner, nicht auf deinem eigenen.

### Aufgaben zu Abschnitt [8](#stufe-8)

<span class="anker" id="stufe-8-7"></span>

:::aufgabe Aufgabe 25 ★★ Meldungen ohne Zeitstempel
<span class="anker" id="aufg-25"></span>

`journalctl` kennt die Option `-o`, die das Format der Ausgabe wählt. (a) Finde in `man journalctl` heraus, was `-o cat` tut. (b) Lege die Eieruhr an, starte und stoppe sie und zeige ihre letzten drei Meldungen mit `-o cat`. (c) Wozu ist das Format praktisch?

:::loesung
(a) `man journalctl` beschreibt unter der Option `-o` das Format `cat`: Es zeigt nur den Text jeder Meldung, ohne Zeit, Rechner und Programm. (b) Nach dem Starten und Stoppen der Eieruhr, etwa im Versuch der Lösung zu Aufgabe [23](dienste-und-systemd.html#aufg-23):

```console
$ journalctl --user -u k8eieruhr -o cat -n 3
Started k8eieruhr.service - Eieruhr zum Üben.
Stopping k8eieruhr.service - Eieruhr zum Üben...
Stopped k8eieruhr.service - Eieruhr zum Üben.
```

Danach löschst du die Unit-Datei wieder und liest mit `daemon-reload` neu ein, wie in Unterabschnitt [8.6](#stufe-8-6). (c) Ohne die vorangestellten Angaben lassen sich die Meldungen leichter mit den Textwerkzeugen aus [Kapitel 6](/wissen/informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke/textwerkzeuge-und-regulaere-ausdruecke.html) weiterverarbeiten, etwa zählen, sortieren oder zwischen zwei Tagen vergleichen.
:::
:::

:::aufgabe Aufgabe 26 ★ Wer liest mit?
<span class="anker" id="aufg-26"></span>

(a) Warum zeigt `journalctl -u cron` auf dem Testsystem keine Meldung, `journalctl --user -u k8eieruhr` aber schon? (b) Welche zwei Wege gibt es, damit `student` die Meldungen des Systems lesen kann? (c) Warum ist es sinnvoll, dass nicht jeder Benutzer alle Meldungen lesen darf? Nenne ein Beispiel aus diesem Kapitel für eine Meldung, die etwas über einen anderen Benutzer verrät.

:::loesung
(a) Die Meldungen von `cron` gehören zum Journal des Systems; das dürfen nur root und die Gruppen `adm` und `systemd-journal` lesen. Die Meldungen der Eieruhr stehen im Journal von `student`, das er selbst lesen darf. (b) `journalctl` mit `sudo` aufrufen oder `student` in die Gruppe `adm` oder `systemd-journal` aufnehmen ([Kapitel 7, Abschnitt 7.2](/wissen/informatik/linux-und-kommandozeile/benutzer-gruppen-und-rechte/benutzer-und-gruppen-anlegen.html#stufe-7-2)); die neue Gruppe wirkt erst nach einer neuen Anmeldung. (c) Meldungen verraten etwas über andere: Das Protokoll von `sudo` enthält zum Beispiel für jeden Aufruf den Benutzer, sein Arbeitsverzeichnis und den vollständigen Befehl ([Kapitel 7, Abschnitt 6.5](/wissen/informatik/linux-und-kommandozeile/benutzer-gruppen-und-rechte/kurzzeitig-root-sudo-und-su.html#stufe-6-5)). Wer alle Meldungen lesen darf, sieht also, wer wann was als root getan hat.
:::
:::

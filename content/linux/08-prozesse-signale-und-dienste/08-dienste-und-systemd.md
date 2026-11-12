---
title: Dienste und systemd
pfad: Informatik / Linux und Kommandozeile / Prozesse, Signale und Dienste
adresse: informatik/linux-und-kommandozeile/prozesse-signale-und-dienste
knoten: Kapitel 8: Prozesse, Signale und Dienste
order: 6130800
summary: Viele Prozesse im Baum aus Unterabschnitt 1.7 hat niemand von Hand gestartet, und sie haben kein Terminal.
tags: Dienst, Dienstverwalter, Unit, Unit-Datei, Benutzerdienst
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Viele Prozesse im Baum aus Unterabschnitt [1.7](prozesse-und-ihre-verwandtschaft.html#stufe-1-7) hat niemand von Hand gestartet, und sie haben kein Terminal. Dieser Abschnitt erklärt solche Dienste, das Programm `systemd`, das sie startet und überwacht, und wie man sie mit `systemctl` ansieht und steuert. Zum Üben legst du einen eigenen kleinen Dienst an.
:::

### Der Dienst

<span class="anker" id="stufe-7-1"></span>

Manche Arbeiten soll ein Rechner erledigen, ohne dass jemand angemeldet ist: zu festen Zeiten Aufgaben starten, die Uhr stellen, Meldungen sammeln, Anfragen aus dem Netz beantworten. Programme dafür laufen dauerhaft im Hintergrund.

:::definition Definition 7.1 (Dienst, Daemon)
<span class="anker" id="satz-7-1"></span>

Ein __Dienst__ (englisch „service“, unter Unix auch „daemon“) ist ein Programm, das im Hintergrund dauerhaft läuft und anderen Programmen oder dem System eine Leistung anbietet. Ein Dienst hat kein steuerndes Terminal, wird nicht von einer Shell gestartet und läuft oft unter einem eigenen Benutzer.
:::

Ein paar Dienste des Testsystems, mit Benutzer, PPID und Terminal:

```console
$ ps -o user:16,pid,ppid,tty,comm -C cron,chronyd,systemd-resolve,rsyslogd,dbus-daemon
USER                 PID    PPID TT       COMMAND
systemd-resolve       83       1 ?        systemd-resolve
root                 160       1 ?        cron
messagebus           161       1 ?        dbus-daemon
syslog               186       1 ?        rsyslogd
_chrony              232     159 ?        chronyd
_chrony              235     232 ?        chronyd
```

`user:16` macht die Spalte 16 Zeichen breit, damit lange Namen nicht abgeschnitten werden. Kein Dienst hat ein Terminal (`?`), die meisten sind Kinder von `systemd`, und viele gehören nicht root. `cron` startet Aufgaben zu festen Zeiten, `chronyd` stellt die Uhr, `rsyslogd` schreibt Meldungen in Dateien unter `/var/log`, `systemd-resolved` übersetzt Rechnernamen in Adressen, und `dbus-daemon` vermittelt Nachrichten zwischen Programmen. Abbildung [25](#abb-25) vergleicht einen Dienst mit einem Programm, das du im Terminal startest.

:::abbildung linux/k8dienst 25
Zwei Prozesse nebeneinander. Links `sleep 600` aus einem Terminal: Elternprozess bash, steuerndes Terminal pts/3, Besitzer student, Tastatur und Bildschirm sind angeschlossen. Rechts `cron`: Elternprozess systemd(1), Terminal „?“, Besitzer root; seine Standardeingabe kommt aus `/dev/null`, seine Ausgabe geht in ein Protokoll. Darunter `systemd-resolved` mit eigenem Benutzer `systemd-resolve`. Die Unterschiede leuchten nacheinander auf: Elternprozess, Terminal, Besitzer, Ein- und Ausgabe.
:::

⁠**Kurz gesagt:** Ein Dienst ist ein Programm ohne Terminal, das dauerhaft im Hintergrund für das System arbeitet, oft unter eigenem Benutzer.

### systemd: der Prozess mit der Nummer 1

<span class="anker" id="stufe-7-2"></span>

Jemand muss die Dienste beim Hochfahren starten, in der richtigen Reihenfolge, sie neu starten, wenn sie abstürzen, und beim Herunterfahren beenden. Unter Ubuntu erledigt das der Prozess, der ohnehin an der Wurzel des Baums steht.

:::definition Definition 7.2 (systemd als Dienstverwalter)
<span class="anker" id="satz-7-2"></span>

`systemd` ist als Prozess 1 der __Dienstverwalter__ des Systems: Er startet beim Hochfahren die Dienste, überwacht sie, startet sie bei Bedarf neu und beendet sie beim Herunterfahren. Für jeden angemeldeten Benutzer läuft zusätzlich eine eigene Instanz `systemd --user`, die die Dienste dieses Benutzers verwaltet. Gesteuert wird `systemd` mit dem Befehl `systemctl`.
:::

```console
$ ps -o pid,ppid,user,cmd -C systemd
    PID    PPID USER     CMD
      1       0 root     /sbin/init
    383       1 student  /usr/lib/systemd/systemd --user
$ ls -l /sbin/init
lrwxrwxrwx 1 root root 22 Jul 27 22:44 /sbin/init -> ../lib/systemd/systemd
$ systemctl is-system-running
running
```

`/sbin/init` ist nur ein symbolischer Link auf `systemd`. Die Instanz des Benutzers `student` hat die Nummer 383 und ist ein Kind des Prozesses 1. `systemctl is-system-running` meldet, dass der Start abgeschlossen ist und alles läuft. Die Benutzerinstanz beginnt mit der ersten Anmeldung des Benutzers und endet mit seiner letzten Sitzung, samt den Diensten, die sie verwaltet. Nur wenn der Verwalter für den Benutzer das Weiterlaufen ohne Anmeldung eingeschaltet hat (englisch „linger“), bleibt sie bestehen.

Unter WSL läuft `systemd` nur, wenn es in der Datei `/etc/wsl.conf` unter `[boot]` mit der Zeile `systemd=true` eingeschaltet ist. Bei einer Installation wie in [Kapitel 1, Abschnitt 4.2](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/wsl-2-linux-neben-windows.html#stufe-4-2) bringt Ubuntu diese Zeile selbst mit; auf dem Testsystem ist sie gesetzt. Meldet `systemctl` bei dir „System has not been booted with systemd as init system (PID 1)“, fehlt sie: Trag sie mit `sudo nano /etc/wsl.conf` ein und starte WSL neu, indem du in PowerShell `wsl --shutdown` eingibst und das Terminal wieder öffnest.

⁠**Kurz gesagt:** `systemd` startet, überwacht und beendet als Prozess 1 die Dienste des Systems, eine eigene Instanz die jedes Benutzers; gesteuert wird es mit `systemctl`.

### Die Unit

<span class="anker" id="stufe-7-3"></span>

`systemd` verwaltet nicht nur Dienste, sondern auch Zeitpläne, eingehängte Dateisysteme und Gruppen von Diensten. Für all das braucht es einen gemeinsamen Begriff.

:::definition Definition 7.3 (Unit)
<span class="anker" id="satz-7-3"></span>

Eine __Unit__ ist ein Ding, das `systemd` verwaltet. Ihr Name endet mit ihrer Art, etwa `.service` für einen Dienst, `.timer` für einen Zeitplan, `.mount` für ein eingehängtes Dateisystem oder `.target` für eine Gruppe von Units, die zusammen einen Zustand des Systems bilden.
:::

`systemctl list-units` zeigt die Units, die `systemd` gerade geladen hat; `--type` und `--state` schränken die Liste ein:

```console
$ systemctl list-units --type=service --state=running
  UNIT                    LOAD   ACTIVE SUB     DESCRIPTION
  chrony.service          loaded active running chrony, an NTP client/s…
  console-getty.service   loaded active running Console Getty
  cron.service            loaded active running Regular background prog…
  dbus.service            loaded active running D-Bus System Message Bus
  getty@tty1.service      loaded active running Getty on tty1
  networkd-dispatcher.se… loaded active running Dispatcher daemon for s…
  rsyslog.service         loaded active running System Logging Service
  systemd-journald.servi… loaded active running Journal Service
  systemd-logind.service  loaded active running User Login Management
  systemd-resolved.servi… loaded active running Network Name Resolution
  systemd-udevd.service   loaded active running Rule-based Manager for …
  unattended-upgrades.se… loaded active running Unattended Upgrades Shu…
  user@1000.service       loaded active running User Manager for UID 10…
  wsl-pro.service         loaded active running Bridge to Ubuntu Pro ag…

Legend: LOAD   → Reflects whether the unit definition was properly loaded.
        ACTIVE → The high-level unit activation state, i.e. generalization of SUB.
        SUB    → The low-level unit activation state, values depend on unit type.

14 loaded units listed.
```

`LOAD` sagt, ob `systemd` die Beschreibung der Unit lesen konnte, `ACTIVE` den groben Zustand (`active`, `inactive`, `failed`), `SUB` den genauen (`running` für einen laufenden Dienst); zu lange Namen kürzt `systemctl` mit „…“ auf die Breite des Terminals. `user@1000.service` ist die Benutzerinstanz von `student`, `wsl-pro.service` ein Dienst, den es nur unter WSL gibt. Passt eine Ausgabe von `systemctl` nicht auf den Bildschirm, zeigt es sie im Seitenanzeiger `less` ([Kapitel 2, Abschnitt 4.4](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/hilfe-finden.html#stufe-4-4)); `q` beendet ihn, und mit `--no-pager` schreibt `systemctl` direkt ins Terminal.

⁠**Kurz gesagt:** Eine Unit ist alles, was `systemd` verwaltet, ein Dienst ist eine Unit mit der Endung `.service`; `systemctl list-units` zeigt sie.

### Den Zustand ansehen: systemctl status

<span class="anker" id="stufe-7-4"></span>

Für einen einzelnen Dienst will man meist auf einen Blick wissen: Läuft er, seit wann, unter welcher PID, und startet er beim Hochfahren?

:::definition Definition 7.4 (systemctl status, is-active, is-enabled)
<span class="anker" id="satz-7-4"></span>

`systemctl status unit` zeigt für eine Unit, woher ihre Beschreibung stammt und ob sie beim Start mitgestartet wird (`Loaded`), ihren Zustand seit wann (`Active`), die PID ihres Hauptprozesses (`Main PID`), ihren Verbrauch, ihre Prozesse (`CGroup`) und ihre letzten Meldungen. `systemctl is-active unit` und `systemctl is-enabled unit` antworten nur mit einem Wort.
:::

Ansehen darf jeder Benutzer, auch die Dienste des Systems:

```console
$ systemctl status cron
● cron.service - Regular background program processing daemon
     Loaded: loaded (/usr/lib/systemd/system/cron.service; enabled; preset: enabled)
     Active: active (running) since Tue 2026-11-10 15:24:41 CET; 4min 23s ago
 Invocation: 5bebfba81d7240c09d04b95ea11dc2b4
       Docs: man:cron(8)
   Main PID: 160 (cron)
      Tasks: 1 (limit: 38204)
     Memory: 508K (peak: 2M)
        CPU: 15ms
     CGroup: /system.slice/cron.service
             └─160 /usr/sbin/cron -f -P
```

```console
$ systemctl is-active cron
active
$ systemctl is-enabled cron
enabled
```

Die erste Zeile nennt den Namen und die Beschreibung der Unit. Der Punkt davor fasst den Zustand zusammen, im Terminal auch mit einer Farbe: $\bullet$ (grün) für „aktiv“, $\circ$ für „inaktiv“ und $\times$ (rot) für „fehlgeschlagen“. `Loaded` nennt die Datei mit der Beschreibung und `enabled`: `cron` startet beim Hochfahren. `Active` sagt, dass der Dienst seit gut vier Minuten läuft, also seit dem letzten Start von WSL. `Main PID` ist die 160 aus Unterabschnitt [2.4](prozesse-beobachten.html#stufe-2-4). `CGroup` ist die Gruppe von Prozessen, in die `systemd` jeden Dienst steckt; so findet es auch alle Kinder eines Dienstes wieder. Die letzten Meldungen des Dienstes, die `status` sonst darunter zeigt, fehlen hier, weil `student` sie auf dem Testsystem nicht lesen darf; manchmal steht dort stattdessen die Warnung `some journal files were not opened due to insufficient permissions`. Bei dir stehen sie vielleicht da: Der erste Benutzer einer gewöhnlichen Ubuntu-Installation, am Desktop wie unter WSL, darf sie meist lesen. Abbildung [26](#abb-26) zeigt die Ausgabe so, wie sie in einem kleinen Terminalfenster erscheint, und geht ihre Teile der Reihe nach durch.

:::abbildung linux/k8statusbild 26
Die Ausgabe aus dem Block oben als Bildschirm, in einem Terminal, das für sie nur zehn Zeilen frei hat. Weil sie dort nicht ganz Platz findet, zeigt `systemctl` sie im Seitenanzeiger; darunter steht invers die Statuszeile `lines 1-10/11`. Der Punkt, `enabled` und `active (running)` sind grün. Zuerst blättert die Ansicht eine Zeile weiter (`lines 2-11/11 (END)`), sodass der Prozessbaum der letzten Zeile erscheint, und wieder zurück. Dann werden nacheinander hervorgehoben und links nummeriert: Name und Beschreibung der Unit (1), die Zeile `Loaded` mit der Datei, `enabled` und `preset` (2), die Zeile `Active` mit Zustand und Startzeit (3), der Hauptprozess `Main PID` (4) und die Zeile `CGroup` mit der Gruppe der Prozesse (5). Meldungen des Journals stehen nicht darunter, weil `student` sie auf dem Testsystem nicht lesen darf.
:::

⁠**Kurz gesagt:** `systemctl status` zeigt Zustand, Hauptprozess und letzte Meldungen einer Unit; `is-active` und `is-enabled` antworten mit einem Wort.

### Die Unit-Datei

<span class="anker" id="stufe-7-5"></span>

Woher weiß `systemd`, welches Programm zu `cron.service` gehört, und dass es beim Hochfahren starten soll? Das steht in einer Textdatei.

:::definition Definition 7.5 (Unit-Datei)
<span class="anker" id="satz-7-5"></span>

Eine __Unit-Datei__ beschreibt eine Unit in Abschnitten, deren Name in eckigen Klammern steht, und Zeilen der Form `Name=Wert`. `[Unit]` enthält allgemeine Angaben wie `Description=` und die Reihenfolge zu anderen Units (`After=`), `[Service]` bei einem Dienst das Programm (`ExecStart=`) und wie es zu betreuen ist, und `[Install]`, wann die Unit beim Start mitgestartet wird (`WantedBy=`). Die Unit-Dateien des Systems liegen unter `/usr/lib/systemd/system`, eigene Änderungen des Verwalters unter `/etc/systemd/system`.
:::

`systemctl cat unit` zeigt die Datei einer Unit:

```console
$ systemctl cat cron
```

```text
# /usr/lib/systemd/system/cron.service
[Unit]
Description=Regular background program processing daemon
Documentation=man:cron(8)
After=remote-fs.target nss-user-lookup.target

[Service]
EnvironmentFile=-/etc/default/cron
ExecStart=/usr/sbin/cron -f -P $EXTRA_OPTS
IgnoreSIGPIPE=false
KillMode=process
Restart=on-failure
SyslogFacility=cron

[Install]
WantedBy=multi-user.target
```

Die erste Zeile nennt den Ort der Datei. `ExecStart=` ist das Programm samt Argumenten; `-f` sagt `cron`, dass es im Vordergrund bleiben soll, statt sich selbst vom Terminal zu lösen, denn darum kümmert sich `systemd`. `Restart=on-failure` lässt `systemd` den Dienst neu starten, wenn er unerwartet endet. `WantedBy=multi-user.target` bedeutet: Der Dienst gehört zum gewöhnlichen Betrieb des Systems und startet mit ihm. Abbildung [27](#abb-27) ordnet die Zeilen.

:::abbildung linux/k8unitdatei 27
Die Unit-Datei von cron als drei Blöcke. Nacheinander leuchtet jeder Abschnitt auf, und daneben erscheint seine Rolle: [Unit] „was ist das, und nach wem starte ich“, [Service] „welches Programm, und was tun, wenn es endet“, [Install] „zu welchem Zustand des Systems gehöre ich“. Pfeile verbinden `ExecStart=` mit dem Prozess `/usr/sbin/cron -f -P` (PID 160) und `WantedBy=` mit einem Kasten `multi-user.target`.
:::

⁠**Kurz gesagt:** Eine Unit-Datei beschreibt eine Unit in den Abschnitten `[Unit]`, `[Service]` und `[Install]`; `systemctl cat` zeigt sie.

### Ein eigener Dienst: starten und stoppen

<span class="anker" id="stufe-7-6"></span>

Dienste des Systems startet und stoppt nur root, und ein Fehler dabei kann das System stören. Zum Üben eignet sich deshalb ein eigener Dienst, den deine Benutzerinstanz von `systemd` verwaltet. Er braucht kein `sudo` und berührt nichts außerhalb deines Heimatverzeichnisses.

:::definition Definition 7.6 (Benutzerdienst, start, stop)
<span class="anker" id="satz-7-6"></span>

Ein __Benutzerdienst__ ist ein Dienst, den die Instanz `systemd --user` eines Benutzers verwaltet; er läuft mit den Rechten dieses Benutzers. Seine Unit-Datei liegt unter `~/.config/systemd/user`, und `systemctl --user` richtet jeden Befehl an diese Instanz. Nach dem Anlegen oder Ändern einer Unit-Datei liest `systemctl --user daemon-reload` die Dateien neu ein. `systemctl start unit` startet eine Unit, `systemctl stop unit` beendet sie.
:::

:::warnung Nur der eigene Übungsdienst
Starte, stoppe oder ändere in diesem Kapitel nur den eigenen Benutzerdienst `k8eieruhr`. Dienste des Systems siehst du nur an; `sudo systemctl stop` an einem fremden Dienst kann das Netz, die Anmeldung oder die Protokolle lahmlegen. Der Übungsdienst selbst wartet nur; er lässt sich jederzeit mit `systemctl --user stop k8eieruhr` beenden und durch Löschen seiner Datei entfernen.
:::

Der Übungsdienst ist eine Eieruhr: Er wartet zehn Minuten. Die Unit-Datei schreibst du mit einem Here-Document ([Kapitel 4, Abschnitt 3.2](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/eingaben-umleiten.html#stufe-3-2)):

```console
$ mkdir -p ~/.config/systemd/user
$ cat > ~/.config/systemd/user/k8eieruhr.service <<ENDE
> [Unit]
> Description=Eieruhr zum Üben
>
> [Service]
> ExecStart=/usr/bin/sleep 600
> Restart=on-failure
>
> [Install]
> WantedBy=default.target
> ENDE
$ systemctl --user daemon-reload
$ systemctl --user status k8eieruhr
○ k8eieruhr.service - Eieruhr zum Üben
     Loaded: loaded (/home/student/.config/systemd/user/k8eieruhr.service; disabled; preset: enabled)
     Active: inactive (dead)
```

`default.target` ist bei einem Benutzerdienst der Zustand „Benutzer angemeldet“. Den Teil `.service` darf man bei `systemctl` weglassen. `systemd` kennt die Unit jetzt, sie ist aber nicht aktiv (`inactive`) und startet nicht von selbst (`disabled`).

```console
$ systemctl --user start k8eieruhr
$ systemctl --user status k8eieruhr
● k8eieruhr.service - Eieruhr zum Üben
     Loaded: loaded (/home/student/.config/systemd/user/k8eieruhr.service; disabled; preset: enabled)
     Active: active (running) since Tue 2026-11-10 15:29:07 CET; 418ms ago
 Invocation: 1e38067901944c18bc32b96d106e8f58
   Main PID: 820 (sleep)
      Tasks: 1 (limit: 38204)
     Memory: 1.3M (peak: 1.7M)
        CPU: 13ms
     CGroup: /user.slice/user-1000.slice/user@1000.service/app.slice/k8eieruhr.service
             └─820 /usr/bin/sleep 600
...
```

Der Dienst läuft, sein Hauptprozess ist ein `sleep 600` mit der PID 820, und dessen Elternprozess ist die Benutzerinstanz von `systemd`, nicht deine Shell. Unter der Zeile `CGroup` zeigt `status` noch die letzten Meldungen des Dienstes, hier die über seinen Start; sie sind im Kapitel weggelassen.

```console
$ systemctl --user is-active k8eieruhr
active
```

```console
$ systemctl --user stop k8eieruhr
$ systemctl --user is-active k8eieruhr
inactive
```

`stop` schickt den Prozessen des Dienstes SIGTERM und wartet, bis sie enden; wer nach einer Frist noch läuft, bekommt SIGKILL. `systemctl restart` stoppt und startet in einem Schritt. Für die Dienste des Systems lauten die Befehle genauso, nur ohne `--user` und mit `sudo` davor.

⁠**Kurz gesagt:** Ein Benutzerdienst wird mit einer Unit-Datei unter `~/.config/systemd/user` angelegt und mit `systemctl --user start` und `stop` gesteuert; nach jeder Änderung der Datei folgt `daemon-reload`.

### systemd wacht: Neustart nach einem Absturz

<span class="anker" id="stufe-7-7"></span>

Ein Dienst, der abstürzt, soll nicht stundenlang ausfallen, bis es jemand bemerkt. Weil `systemd` der Elternprozess jedes Dienstes ist, erfährt es sofort, wenn einer endet, und kann darauf reagieren.

:::definition Definition 7.7 (Restart=)
<span class="anker" id="satz-7-7"></span>

Die Zeile `Restart=` im Abschnitt `[Service]` legt fest, wann `systemd` einen beendeten Dienst neu startet: `no` nie (Standard), `on-failure` nur nach einem Fehler, `always` immer. Als Fehler gilt ein Exit-Status ungleich 0 und ein Ende durch ein Signal, außer durch SIGHUP, SIGINT, SIGTERM und SIGPIPE. Nach `systemctl stop` startet `systemd` nie neu. Wie lange es vor einem Neustart wartet, legt `RestartSec=` fest; ohne die Zeile sind es 100 Millisekunden.
:::

`systemctl show -p MainPID` nennt nur die PID des Hauptprozesses, und `journalctl --user -u k8eieruhr -n 4` zeigt die letzten vier Meldungen, die über die Eieruhr gesammelt wurden. Die Eieruhr hat `Restart=on-failure`:

```console
$ systemctl --user start k8eieruhr
$ systemctl --user show -p MainPID k8eieruhr
MainPID=829
$ kill -9 829
$ systemctl --user show -p MainPID k8eieruhr
MainPID=833
$ journalctl --user -u k8eieruhr -n 4
Nov 10 15:29:10 labor systemd[383]: k8eieruhr.service: Main process exited, code=killed, status=9/KILL
Nov 10 15:29:10 labor systemd[383]: k8eieruhr.service: Failed with result 'signal'.
Nov 10 15:29:11 labor systemd[383]: k8eieruhr.service: Scheduled restart job, restart counter is at 1.
Nov 10 15:29:11 labor systemd[383]: Started k8eieruhr.service - Eieruhr zum Üben.
$ kill 833
$ systemctl --user is-active k8eieruhr
inactive
```

Nach SIGKILL läuft der Dienst kurz darauf wieder, mit dem neuen Hauptprozess 833. `journalctl` zeigt die Meldungen von `systemd` dazu: Der Hauptprozess wurde durch SIGKILL beendet, das gilt als Fehler, ein Neustart ist geplant und ausgeführt. Nach SIGTERM dagegen bleibt der Dienst aus, denn ein Ende durch SIGTERM gilt als gewolltes Ende. Abbildung [28](#abb-28) zeigt den Ablauf.

:::abbildung linux/k8neustart 28
Oben `systemd --user` (PID 383), darunter der Dienst k8eieruhr mit dem Hauptprozess `sleep 600` (PID 829). Ein Signal SIGKILL trifft 829, der Prozess verschwindet. Ein Pfeil „Kind beendet: SIGKILL“ läuft zu systemd hinauf; dort leuchtet die Regel `Restart=on-failure` auf, ein Zähler „Neustarts“ springt auf 1, und ein neuer Prozess 833 erscheint. Zweiter Durchgang: SIGTERM trifft 833, der Pfeil meldet „SIGTERM: gewolltes Ende“, die Regel greift nicht, der Dienst bleibt aus.
:::

⁠**Kurz gesagt:** Mit `Restart=on-failure` startet `systemd` einen Dienst neu, der mit einem Fehler oder durch ein Signal wie SIGKILL endet, nicht aber nach SIGTERM oder `stop`.

### Beim Start mitstarten: enable

<span class="anker" id="stufe-7-8"></span>

`start` startet einen Dienst jetzt. Ob er auch nach dem nächsten Hochfahren läuft, ist eine getrennte Frage, und dafür gibt es einen eigenen Befehl.

:::definition Definition 7.8 (enable, disable)
<span class="anker" id="satz-7-8"></span>

`systemctl enable unit` legt fest, dass die Unit künftig mitgestartet wird, wenn das Ziel aus ihrer Zeile `WantedBy=` erreicht wird. Dazu legt es einen symbolischen Link im Verzeichnis `<ziel>.wants` an; es startet die Unit nicht. `systemctl disable unit` entfernt den Link wieder. Wer beides auf einmal will, schreibt `enable --now`.
:::

```console
$ systemctl --user enable k8eieruhr
Created symlink '/home/student/.config/systemd/user/default.target.wants/k8eieruhr.service' → '/home/student/.config/systemd/user/k8eieruhr.service'.
$ systemctl --user is-enabled k8eieruhr
enabled
$ ls -l ~/.config/systemd/user/default.target.wants
total 0
lrwxrwxrwx 1 student student 52 Nov 10 15:29 k8eieruhr.service -> /home/student/.config/systemd/user/k8eieruhr.service
$ systemctl --user is-active k8eieruhr
inactive
$ systemctl --user disable k8eieruhr
Removed '/home/student/.config/systemd/user/default.target.wants/k8eieruhr.service'.
$ systemctl --user is-enabled k8eieruhr
disabled
```

Nach `enable` steht im Verzeichnis `default.target.wants` ein symbolischer Link auf die Unit-Datei ([Kapitel 3, Abschnitt 8.5](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/inode-und-links.html#stufe-8-5)); trotzdem läuft die Eieruhr nicht, denn `enable` startet nichts. Beim nächsten Erreichen von `default.target`, also bei der nächsten Anmeldung, würde `systemd` den Link finden und die Eieruhr starten. `disable` entfernt den Link. Abbildung [29](#abb-29) stellt `start` und `enable` gegenüber.

:::abbildung linux/k8enable 29
Zwei Schalter nebeneinander: „jetzt“ (start/stop) und „beim nächsten Start“ (enable/disable). Unter „beim nächsten Start“ das Verzeichnis `default.target.wants`; bei enable erscheint darin ein Link auf `k8eieruhr.service`, der Dienst selbst bleibt aus. Dann ein Zeitsprung „nächste Anmeldung“: systemd erreicht `default.target`, folgt dem Link und startet den Dienst. Zuletzt disable: der Link verschwindet.
:::

⁠**Kurz gesagt:** `enable` sorgt über einen symbolischen Link dafür, dass eine Unit beim nächsten Start mitstartet, `start` startet sie jetzt; beides ist unabhängig voneinander.

### Dienste unter eigenen Benutzern

<span class="anker" id="stufe-7-9"></span>

Unterabschnitt [7.1](#stufe-7-1) hat gezeigt, dass viele Dienste nicht root gehören. Das ist kein Zufall, sondern steht in ihrer Unit-Datei.

:::definition Definition 7.9 (User=)
<span class="anker" id="satz-7-9"></span>

Die Zeile `User=` im Abschnitt `[Service]` nennt den Benutzer, unter dem `systemd` das Programm des Dienstes startet. Fehlt sie, läuft ein Dienst des Systems als root. Bei einem Benutzerdienst ist die Zeile überflüssig, denn er läuft immer unter dem Benutzer seiner Instanz.
:::

```console
$ grep -E '^(User|ExecStart)=' /usr/lib/systemd/system/systemd-resolved.service
ExecStart=/usr/lib/systemd/systemd-resolved
User=systemd-resolve
$ systemctl show -p User cron systemd-resolved
User=

User=systemd-resolve
```

`systemd-resolved` läuft als Systemkonto `systemd-resolve` ([Kapitel 7, Abschnitt 1.4](/wissen/informatik/linux-und-kommandozeile/benutzer-gruppen-und-rechte/benutzer-und-gruppen.html#stufe-1-4)), `cron` hat keine Zeile `User=` und läuft als root: Es muss die geplanten Aufgaben jedes Benutzers unter dessen Namen starten können, und das darf nur root.

⁠**Kurz gesagt:** Mit `User=` läuft ein Dienst unter einem eigenen Benutzer statt als root.

:::hintergrund Warum Dienste unter eigenen Benutzern laufen
Ein Dienst wie `systemd-resolved` beantwortet Anfragen anderer Programme und verarbeitet dabei Daten von außen, etwa aus dem Netz. Steckt in ihm ein Fehler, den jemand ausnutzt, kann der Angreifer genau das tun, was der Prozess darf. Läuft der Dienst als root, ist das alles. Läuft er unter einem Systemkonto, das nur seine eigenen Dateien schreiben darf, bleibt der Schaden auf diesen kleinen Bereich begrenzt. Das ist der Grundsatz der minimalen Rechte ([Cybersecurity, Kapitel 1, Abschnitt 5.2](/wissen/informatik/cybersecurity/sicherheit-schutzziele-und-spielregeln/sicherheitsprinzipien-rechte-vergeben-und-prufen.html#stufe-5-2)), angewandt auf Prozesse: Jedes Programm bekommt genau die Rechte, die es für seine Aufgabe braucht. Weil ein Kindprozess die Benutzernummern erbt (Unterabschnitt [1.8](prozesse-und-ihre-verwandtschaft.html#stufe-1-8)), gilt die Grenze auch für alles, was der Dienst selbst startet. Dass ein Konto wie `systemd-resolve` sich nicht anmelden kann, verhindert zusätzlich, dass jemand mit seinen Rechten eine Shell öffnet.
:::

### Aufgaben zu Abschnitt [7](#stufe-7)

<span class="anker" id="stufe-7-10"></span>

:::aufgabe Aufgabe 22 ★★ Den Dienst cron untersuchen
<span class="anker" id="aufg-22"></span>

(a) Läuft `cron` auf deinem System, und seit wann? Startet es beim Hochfahren? Antworte mit `systemctl status cron` und `systemctl is-enabled cron`. (b) Versuche `journalctl -u cron -n 5`. Was meldet es, und warum? (c) Zeige mit `sudo journalctl -b -u cron --no-pager` die ersten drei Meldungen von `cron` seit dem Start.

:::loesung
```console
$ systemctl status cron
● cron.service - Regular background program processing daemon
     Loaded: loaded (/usr/lib/systemd/system/cron.service; enabled; preset: enabled)
     Active: active (running) since Tue 2026-11-10 15:40:19 CET; 2min 19s ago
 Invocation: 8ad439bc7e01410994e559b266263e47
       Docs: man:cron(8)
   Main PID: 156 (cron)
      Tasks: 1 (limit: 38204)
     Memory: 512K (peak: 2M)
        CPU: 19ms
     CGroup: /system.slice/cron.service
             └─156 /usr/sbin/cron -f -P
```

```console
$ systemctl is-enabled cron
enabled
$ journalctl -u cron -n 5
Hint: You are currently not seeing messages from other users and the system.
      Users in groups 'adm', 'systemd-journal' can see all messages.
      Pass -q to turn off this notice.
-- No entries --
$ sudo journalctl -b -u cron --no-pager | head -n 3
Nov 10 15:40:19 labor systemd[1]: Started cron.service - Regular background program processing daemon.
Nov 10 15:40:19 labor (cron)[156]: cron.service: Referenced but unset environment variable evaluates to an empty string: EXTRA_OPTS
Nov 10 15:40:19 labor cron[156]: (CRON) INFO (pidfile fd = 3)
```

(a) `cron` läuft (`active (running)`), seit dem letzten Start von WSL vor gut zwei Minuten, mit der PID 156, und es ist `enabled`, startet also beim Hochfahren. (b) `journalctl` findet keine Meldung und erklärt im Hinweis, warum: `student` ist in keiner der Gruppen `adm` und `systemd-journal` und darf die Meldungen des Systems nicht lesen. Gehört dein Benutzer zur Gruppe `adm`, siehst du dagegen fünf Meldungen und keinen Hinweis. (c) Mit `sudo` sind sie lesbar: `systemd` startet den Dienst, `cron` bemerkt eine leere Variable aus seiner Unit-Datei (`$EXTRA_OPTS`) und meldet seinen Start.
:::
:::

:::aufgabe Aufgabe 23 ★★★ Neustart oder nicht
<span class="anker" id="aufg-23"></span>

Lege die Eieruhr erneut an, diesmal ohne Abschnitt `[Install]` und mit `Restart=on-failure`. (a) Starte sie, beende ihren Hauptprozess mit `kill` (SIGTERM) und prüfe mit `is-active`. (b) Ersetze mit `sed -i` ([Kapitel 6, Abschnitt 8.6](/wissen/informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke/umformen-im-strom-sed.html#stufe-8-6)) `on-failure` durch `always`, lies die Datei neu ein und wiederhole (a). Was ändert sich, und warum? (c) Wie hältst du einen Dienst mit `Restart=always` trotzdem an?

:::loesung
```console
$ mkdir -p ~/.config/systemd/user
$ printf '[Unit]\nDescription=Eieruhr zum Üben\n\n[Service]\nExecStart=/usr/bin/sleep 600\nRestart=on-failure\n' > ~/.config/systemd/user/k8eieruhr.service
$ systemctl --user daemon-reload
$ systemctl --user start k8eieruhr
$ kill 678
$ systemctl --user is-active k8eieruhr
inactive
$ sed -i 's/on-failure/always/' ~/.config/systemd/user/k8eieruhr.service
$ systemctl --user daemon-reload
$ systemctl --user start k8eieruhr
$ systemctl --user show -p MainPID k8eieruhr
MainPID=692
$ kill 692
$ systemctl --user is-active k8eieruhr
active
$ systemctl --user show -p MainPID k8eieruhr
MainPID=696
$ systemctl --user stop k8eieruhr
$ systemctl --user is-active k8eieruhr
inactive
```

Statt mit einem Here-Document ist die Datei hier mit `printf` geschrieben; `\n` steht für ein Zeilenende ([Kapitel 5, Abschnitt 3.1](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/worttrennung-und-quoting.html#stufe-3-1)). Die PID 678 des Hauptprozesses liefert `systemctl --user show -p MainPID k8eieruhr` oder `pgrep -f 'sleep 600'`. (a) Nach SIGTERM bleibt die Eieruhr aus: Bei `on-failure` gilt ein Ende durch SIGTERM als gewollt. (b) Mit `always` startet `systemd` den Dienst nach jedem Ende neu; nach `kill` ist er wieder aktiv, mit dem neuen Hauptprozess 696. (c) Mit `systemctl --user stop k8eieruhr`: Nach einem `stop` startet `systemd` nie neu, denn es weiß, dass das Ende gewollt ist. Zum Aufräumen löschst du danach die Unit-Datei mit `rm` und liest mit `systemctl --user daemon-reload` neu ein.
:::
:::

:::aufgabe Aufgabe 24 ★ start oder enable?
<span class="anker" id="aufg-24"></span>

Welchen Befehl brauchst du jeweils: (a) Ein Dienst soll ab sofort laufen, aber nach dem nächsten Hochfahren nicht mehr. (b) Ein Dienst soll ab dem nächsten Hochfahren laufen, jetzt aber nicht. (c) Beides. (d) Nach `systemctl enable` läuft ein Dienst nicht. Ist das ein Fehler?

:::loesung
(a) `systemctl start dienst`: läuft jetzt, `enable` unterbleibt. (b) `systemctl enable dienst`: legt nur den Link an. (c) `systemctl enable --now dienst` oder `enable` und `start` nacheinander. (d) Kein Fehler: `enable` legt nur den Link für den nächsten Start an. Ob der Dienst jetzt läuft, entscheidet allein `start`.
:::
:::

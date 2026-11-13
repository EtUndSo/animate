---
title: Entfernte Anmeldung: Client, Server und ein Übungsserver
pfad: Informatik / Linux und Kommandozeile / Auf entfernten Rechnern arbeiten: SSH, Dateien übertragen, tmux
adresse: informatik/linux-und-kommandozeile/auf-entfernten-rechnern-arbeiten-ssh-dateien-ubertragen-tmux
knoten: Kapitel 11: Auf entfernten Rechnern arbeiten: SSH, Dateien übertragen, tmux
order: 6160200
summary: Dieser Abschnitt erklärt, was es heißt, sich an einem anderen Rechner anzumelden, welche zwei Programme dabei zusammenarbeiten und wie du auf deinem eigenen Rechner einen Übungsserver einrichtest, der nur für dich selbst erreichbar ist.
tags: entfernten Anmeldung, Server, Client, SSH, Socket-Aktivierung
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Dieser Abschnitt erklärt, was es heißt, sich an einem anderen Rechner anzumelden, welche zwei Programme dabei zusammenarbeiten und wie du auf deinem eigenen Rechner einen Übungsserver einrichtest, der nur für dich selbst erreichbar ist.
:::

:::::vorwissen Was du dafür brauchst: Rechnername, Adresse und Port

<span class="anker" id="stufe-1-1"></span>

Dieses Kapitel setzt die [Kapitel 7](/wissen/informatik/linux-und-kommandozeile/benutzer-gruppen-und-rechte/benutzer-gruppen-und-rechte.html), 8 und 10 voraus. Für den Anfang brauchst du daraus vor allem diese Dinge.

<ul>

<li>

Ein Dienst ist ein Programm, das ohne Terminal im Hintergrund läuft und auf Arbeit wartet. Unter Ubuntu startet und überwacht der Dienstverwalter systemd die Dienste; jeder Dienst ist eine Unit, deren Zustand `systemctl status name` zeigt ([Kapitel 8, Abschnitte 7.1](/wissen/informatik/linux-und-kommandozeile/prozesse-signale-und-dienste/dienste-und-systemd.html#stufe-7-1) bis 7.4).

</li>

<li>

Software installiert man mit `sudo apt install paket` ([Kapitel 9, Abschnitt 6.3](/wissen/informatik/linux-und-kommandozeile/software-installieren-paketverwaltung/installieren-entfernen-aktualisieren.html#stufe-6-3)). Eine Datei, die nur root schreiben darf, füllt man mit `befehl | sudo tee datei`, weil eine Umleitung mit `>` die Rechte der eigenen Shell hätte ([Kapitel 7, Abschnitt 6.6](/wissen/informatik/linux-und-kommandozeile/benutzer-gruppen-und-rechte/kurzzeitig-root-sudo-und-su.html#stufe-6-6)). Mehrere Zeilen gibt man einem Befehl mit einem Here-Document mit ([Kapitel 4, Abschnitt 3.2](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/eingaben-umleiten.html#stufe-3-2)).

</li>

<li>

Jede Datei hat Rechte für Besitzer, Gruppe und andere, oktal geschrieben etwa 600 oder 644 ([Kapitel 7, Abschnitte 2](/wissen/informatik/linux-und-kommandozeile/benutzer-gruppen-und-rechte/die-rechte-einer-datei.html#stufe-2) und [3](/wissen/informatik/linux-und-kommandozeile/benutzer-gruppen-und-rechte/rechte-andern-chmod.html#stufe-3)).

</li>

</ul>

Neu sind drei Wörter aus der Welt der Netze. Sie werden hier nur so weit erklärt, wie dieses Kapitel sie braucht; wie Netze im Einzelnen funktionieren, erklärt die Reihe Cybersecurity.

Jeder Rechner hat einen *Rechnernamen*, den der Befehl `hostname` anzeigt. Damit andere Rechner ihn im Netz erreichen, hat er außerdem eine *Adresse*, eine Nummer im Netz ([Kapitel 1, Abschnitt 3.6](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/virtuelle-maschinen-der-rechner-im-rechner.html#stufe-3-6)). Eine Adresse ist besonders: `127.0.0.1` bezeichnet immer den Rechner selbst, auf dem das Programm gerade läuft. Ihr Name ist `localhost`. In der neueren, längeren Schreibweise von Adressen heißt dieselbe Stelle `::1`. Welche Namen zu welchen Adressen gehören, steht für den eigenen Rechner in der Datei `/etc/hosts`:

```console
$ hostname
labor
$ grep -w localhost /etc/hosts
127.0.0.1       localhost
```

Auf einem Rechner laufen oft viele Dienste gleichzeitig. Damit eine ankommende Verbindung den richtigen erreicht, trägt sie neben der Adresse eine zweite Nummer, den *Port*, eine Zahl von 0 bis 65 535. Ein Bild zur Orientierung: Die Adresse ist die Hausanschrift, der Port die Nummer der Wohnung. Ein Dienst, der an einem Port auf Verbindungen wartet, *lauscht* an diesem Port. Für jede Art von Dienst gibt es einen üblichen Port; der Dienst, um den es in diesem Kapitel geht, lauscht normalerweise am Port 22. Abbildung [1](#abb-1) zeigt das Bild mit Anschrift und Wohnungen.

:::abbildung linux/k11port 1
Adresse und Port. Ein Haus mit der Anschrift `127.0.0.1` (Schild darunter: „localhost, auch `::1`: immer der eigene Rechner“). Im Haus mehrere Wohnungstüren mit Nummern: `22` (darin ein Dienst „SSH-Server“, Ohr-Symbol „lauscht“), `443` (Webserver, gestrichelt, „nicht installiert“) und weitere Türen ohne Schild. Ein Brief mit der Aufschrift `127.0.0.1 : 22` kommt an und wird zur Tür 22 gebracht. Unten: „Adresse wählt den Rechner, Port wählt den Dienst“.
:::

⁠**Kurz gesagt:** Ein Rechner hat einen Namen und eine Adresse; `localhost` mit der Adresse `127.0.0.1` ist der eigene Rechner, und der Port wählt auf einem Rechner den Dienst aus, der eine Verbindung bekommt.

:::warnung Nur dort anmelden, wo du darfst
Melde dich nur an Rechnern an, für die dir jemand ein Konto gegeben hat: an deinen eigenen, mit deinem Zugang bei Hochschule oder Arbeitgeber und auf Übungsplattformen nach deren Regeln. Sich unbefugt Zugang zu Daten zu verschaffen, die nicht für einen bestimmt und gegen unberechtigten Zugang besonders gesichert sind, ist in Deutschland nach § 202a des Strafgesetzbuchs strafbar, wenn dabei die Zugangssicherung überwunden wird. Dieses Kapitel ist keine Rechtsberatung. Alle Übungen dieses Kapitels bleiben auf deinem eigenen Rechner. Lege dafür ein Übungsverzeichnis mit einer kleinen Einkaufsliste an:

```console
$ mkdir ~/linuxk11
$ cd ~/linuxk11
$ printf '%s\n' Milch Brot Äpfel Kaffee > einkauf.txt
```
:::

:::::

### Die entfernte Anmeldung

<span class="anker" id="stufe-1-2"></span>

Ein Server im Rechenzentrum hat keinen Bildschirm und keine Tastatur, und selbst wenn er welche hätte, säße man nicht davor. Trotzdem will man dort Befehle eingeben, Dateien ansehen und Programme starten, genau so, wie man es aus den bisherigen Kapiteln kennt.

Ein Bild zur Orientierung: ein Telefonat mit jemandem, der vor dem anderen Rechner sitzt, genau das tippt, was du ihm sagst, und dir vorliest, was auf seinem Bildschirm erscheint. Bei der entfernten Anmeldung fällt der Mensch in der Mitte weg; seine Arbeit übernehmen zwei Programme. Das Bild hat eine Grenze: Ein Mensch würde merken, wenn du dich verhörst oder jemand mithört. Die Programme müssen das selbst sicherstellen.

:::definition Definition 1.1 (Entfernte Anmeldung)
<span class="anker" id="satz-1-1"></span>

Bei einer __entfernten Anmeldung__ meldet man sich über eine Netzverbindung an einem anderen Rechner an. Dort startet eine Shell unter dem Benutzerkonto, das man auf diesem Rechner hat. Was man tippt, geht über die Verbindung zu dieser Shell, und was die Shell und ihre Programme ausgeben, kommt über die Verbindung zurück in das eigene Terminal.
:::

Wichtig ist, wo was geschieht. Das Terminalfenster gehört zum eigenen Rechner ([Kapitel 2, Abschnitt 1.2](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/terminal-und-shell.html#stufe-1-2)). Die Shell, jeder Befehl und jede Datei, die man in dieser Shell anfasst, gehören zum anderen Rechner: Ein `ls` zeigt die Dateien dort, ein `rm` löscht dort, und ein Programm rechnet mit dem Prozessor und dem Speicher des anderen Rechners.

::::beispiel Woran man erkennt, wo man ist
Die Eingabeaufforderung zeigt Benutzer und Rechnernamen ([Kapitel 2, Abschnitt 1.4](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/terminal-und-shell.html#stufe-1-4)). Meldet sich die Benutzerin `anna` von ihrem Rechner `laptop` an einem Server namens `rechner1` an, wechselt die Aufforderung von `anna@laptop:~$` zu `anna@rechner1:~$`. Bis sie die Verbindung mit `exit` beendet, laufen alle Befehle auf `rechner1`, auch wenn das Fenster dasselbe bleibt.
::::

:::hintergrund Warum man früher mitlesen konnte
Entfernte Anmeldungen gibt es seit den Anfängen der Netze. Die alten Programme dafür, `telnet` und `rlogin`, schickten alles, was man tippte, unverändert über die Leitung, auch das Passwort bei der Anmeldung. Jeder Rechner, über den die Verbindung lief, konnte es mitlesen. Genau das geschah 1995 im Netz der Technischen Universität Helsinki: Unbekannte zeichneten dort mit einem Programm, das auf der Leitung mitlas, die Passwörter vieler Benutzer auf. Der Forscher Tatu Ylönen schrieb daraufhin ein Programm, das die Verbindung verschlüsselt und prüft, mit wem man spricht. Daraus entstand das Verfahren, mit dem man sich heute fast überall entfernt anmeldet; seit 1999 gibt es davon eine freie Fassung, die auf nahezu jedem Linux läuft.
:::

⁠**Kurz gesagt:** Bei einer entfernten Anmeldung läuft die Shell auf dem anderen Rechner; das eigene Terminal ist nur das Fenster, durch das man mit ihr spricht.

### Client und Server

<span class="anker" id="stufe-1-3"></span>

An einer entfernten Anmeldung sind zwei Programme auf zwei Rechnern beteiligt. Sie haben verschiedene Aufgaben: Eines wartet, das andere ruft an.

:::definition Definition 1.2 (Server und Client)
<span class="anker" id="satz-1-2"></span>

Ein __Server__ ist ein Programm, das an einem Port lauscht und Verbindungen annimmt, um für andere Programme etwas zu erledigen. Ein __Client__ ist ein Programm, das von sich aus eine Verbindung zu einem Server aufbaut und dessen Dienste nutzt.
:::

Das Wort „Server“ bezeichnet auch den Rechner, auf dem ein solches Programm läuft; meist ergibt sich aus dem Satz, was gemeint ist. Ein Server ist fast immer ein Dienst im Sinn von [Kapitel 8](/wissen/informatik/linux-und-kommandozeile/prozesse-signale-und-dienste/prozesse-signale-und-dienste.html), denn er muss auch dann laufen, wenn niemand angemeldet ist.

::::beispiel Browser und Webserver
Wenn du eine Webseite aufrufst, ist dein Browser der Client: Er baut die Verbindung auf und fragt nach der Seite. Auf der anderen Seite lauscht ein Webserver, normalerweise am Port 443, und schickt die Seite zurück. Dieselbe Rollenverteilung gilt für jede entfernte Anmeldung: Der Client läuft bei dir, der Server auf dem Rechner, an dem du dich anmeldest.
::::

:::abbildung linux/k11clientserver 2
Client und Server. Zwei Zeilen untereinander. Oben: links „Browser (Client)“ auf einem Laptop, rechts „Webserver“ auf einem Rechner mit Tür 443; ein Pfeil „Verbindung aufbauen“ geht von links nach rechts, die Antwort „Seite“ kommt zurück. Unten dasselbe Muster mit „`ssh` (Client)“ und „`sshd` (Server)“ an Tür 22. Der Server ist jeweils mit einem Uhrsymbol „wartet immer“ markiert, der Client mit „ruft an, wenn er etwas braucht“.
:::

⁠**Kurz gesagt:** Der Server wartet an einem Port auf Verbindungen, der Client baut sie auf.

### SSH

<span class="anker" id="stufe-1-4"></span>

Damit Client und Server sich verstehen, müssen sie sich an dieselben Regeln halten: wer zuerst spricht, wie eine Nachricht aufgebaut ist, was auf welche Nachricht folgt. Solche Regeln heißen *Protokoll*. Für entfernte Anmeldungen gibt es ein Protokoll, das zugleich drei Sicherheitsfragen beantwortet.

:::definition Definition 1.3 (SSH)
<span class="anker" id="satz-1-3"></span>

__SSH__ (Secure Shell, „sichere Shell“) ist ein Protokoll für entfernte Anmeldungen und andere Arbeiten auf einem entfernten Rechner. Der SSH-Server heißt `sshd` und lauscht normalerweise am Port 22; der SSH-Client ist der Befehl `ssh`. Eine SSH-Verbindung leistet dreierlei:

<ol>

<li>

Der Server beweist dem Client, dass er der Rechner ist, für den er sich ausgibt.

</li>

<li>

Alles, was über die Verbindung geht, ist verschlüsselt; wer unterwegs mitliest, sieht nur unlesbare Daten.

</li>

<li>

Der Benutzer beweist dem Server, dass er das Konto benutzen darf, mit einem Passwort oder mit einem Schlüssel.

</li>

</ol>
:::

Unter Linux ist SSH fast immer die Fassung OpenSSH. Ubuntu bringt den Client im Paket `openssh-client` von Anfang an mit, den Server im Paket `openssh-server` dagegen nicht: Ein Rechner, an dem sich niemand von außen anmelden soll, braucht ihn nicht. Wie die Verschlüsselung im Innern funktioniert, ist Stoff der Reihe Cybersecurity; für die Bedienung genügt es zu wissen, dass sie stattfindet. Abbildung [3](#abb-3) zeigt die beteiligten Programme.

```console
$ ssh -V
OpenSSH_10.2p1 Ubuntu-2ubuntu3.8, OpenSSL 3.5.5 27 Jan 2026
```

`-V` gibt die Version aus, hier OpenSSH 10.2 in der Fassung von Ubuntu; die letzte Stelle hängt davon ab, welche Updates dein System schon hat.

:::abbildung linux/k11anmeldung 3
Eine entfernte Anmeldung mit SSH. Links der eigene Rechner mit dem Terminalfenster und dem Client `ssh`, rechts der Server mit dem Dienst `sshd`, der am Port 22 lauscht. Nacheinander erscheinen: die Verbindung als Rohr zwischen beiden Rechnern mit einem Schloss darauf (verschlüsselt); auf dem Server eine Shell, die `sshd` für den angemeldeten Benutzer startet; ein getippter Befehl `ls`, der als Paket durch das Rohr nach rechts wandert; die Ausgabe, die nach links zurückkommt und im Terminal erscheint. Etiketten: „Client“, „Server“, „Shell läuft hier“, „Fenster ist hier“.
:::

⁠**Kurz gesagt:** SSH ist das Protokoll für entfernte Anmeldungen: Der Client `ssh` verbindet sich mit dem Server `sshd`, der Server weist sich aus, die Verbindung ist verschlüsselt, und der Benutzer weist sich aus.

### Ein Übungsserver auf dem eigenen Rechner

<span class="anker" id="stufe-1-5"></span>

Zum Üben brauchst du einen SSH-Server, an dem du dich anmelden darfst. Den einfachsten hast du schon: deinen eigenen Rechner. Du installierst dort den Server und meldest dich über `localhost` bei dir selbst an. Für SSH macht es keinen Unterschied, ob der Server auf demselben Rechner läuft oder auf einem anderen Kontinent; alles, was in diesem Kapitel geschieht, funktioniert bei einem echten Server genauso. Wer eine virtuelle Maschine aus [Kapitel 1, Abschnitt 7](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/eine-virtuelle-maschine-mit-virtualbox.html#stufe-7) hat, kann den Server ebenso gut dort einrichten.

Die Einstellungen des Servers stehen in der Datei `/etc/ssh/sshd_config`. Unter Ubuntu liest sie gleich am Anfang alle Dateien mit der Endung `.conf` aus dem Verzeichnis `/etc/ssh/sshd_config.d` ein. Eigene Einstellungen schreibt man deshalb in eine eigene Datei dort, statt die mitgelieferte zu ändern. Für den Übungsserver sind das fünf Zeilen:

<ul>

<li>

`ListenAddress 127.0.0.1` und `ListenAddress ::1`: Der Server lauscht nur an den beiden Adressen des eigenen Rechners. Von einem anderen Rechner aus ist er damit nicht erreichbar.

</li>

<li>

`PasswordAuthentication no` und `KbdInteractiveAuthentication no`: Anmelden mit Passwort ist ausgeschaltet. Es bleibt nur die Anmeldung mit einem Schlüssel.

</li>

<li>

`PermitRootLogin no`: Als root darf sich niemand anmelden.

</li>

</ul>

Abbildung [4](#abb-4) zeigt, wie die eigene Datei in die Einstellungen des Servers gelangt.

:::abbildung linux/k11dropin 4
Dateiansicht (hell), zwei Dateien übereinander. Oben `/etc/ssh/sshd_config`, hervorgehoben `Include /etc/ssh/sshd_config.d/*.conf`, die übrigen Zeilen als …; darunter `/etc/ssh/sshd_config.d/10-linuxk11.conf` mit den fünf Zeilen aus dem Text, daneben Randetiketten: „nur über localhost erreichbar“ (beide `ListenAddress`), „keine Passwörter“ (zwei Zeilen), „kein root“. Ein Pfeil führt von der `Include`-Zeile zur unteren Datei, und deren Zeilen wandern an diese Stelle der oberen („an dieser Stelle eingelesen“).
:::

:::warnung Was der Übungsserver an deinem System ändert
Die folgenden Befehle installieren mit root-Rechten ein Paket und legen eine Datei in `/etc` an. Lege die Datei mit den fünf Zeilen *vor* der Installation an: Der Server startet sofort nach dem Installieren und soll von Anfang an nur über `localhost` erreichbar sein. Wie du ihn wieder vollständig entfernst, wenn du ihn nicht mehr brauchst, steht im letzten Unterabschnitt des Kapitels. Auf einem Rechner, der in einem fremden Netz hängt, etwa im WLAN eines Cafés, ist ein Server, der nur an `localhost` lauscht, von dort aus nicht zu erreichen; ohne die Zeilen `ListenAddress` wäre er es unter Umständen.

Richte den Übungsserver nur auf einem Rechner ein, auf dem noch kein SSH-Server installiert ist. Prüfe das vorher mit `dpkg -s openssh-server` ([Kapitel 9, Abschnitt 2.6](/wissen/informatik/linux-und-kommandozeile/software-installieren-paketverwaltung/die-paketverwaltung-und-ihre-datenbank.html#stufe-2-6)): Die Meldung `package 'openssh-server' is not installed` heißt, dass der Weg frei ist. Steht dort dagegen `Status: install ok installed`, etwa auf einem Server im Netz oder einer virtuellen Maschine, an der du dich selbst per SSH anmeldest, lass diesen Unterabschnitt aus: Die eigene Datei würde den Server nur noch über `localhost` erreichbar machen, und der Rückbau am Ende des Kapitels würde ihn entfernen. Du könntest dich dann selbst aussperren.
:::

Zuerst legst du das Verzeichnis und darin die Datei `10-linuxk11.conf` an. Das Here-Document liefert die fünf Zeilen, `sudo tee` schreibt sie mit root-Rechten in die Datei, und `> /dev/null` verwirft die Kopie, die `tee` zusätzlich auf den Bildschirm schreiben würde:

```console
$ sudo mkdir -p /etc/ssh/sshd_config.d
$ sudo tee /etc/ssh/sshd_config.d/10-linuxk11.conf > /dev/null <<'ENDE'
> ListenAddress 127.0.0.1
> ListenAddress ::1
> PasswordAuthentication no
> KbdInteractiveAuthentication no
> PermitRootLogin no
> ENDE
$ cat /etc/ssh/sshd_config.d/10-linuxk11.conf
ListenAddress 127.0.0.1
ListenAddress ::1
PasswordAuthentication no
KbdInteractiveAuthentication no
PermitRootLogin no
```

Dann installierst du den Server:

```console
$ sudo apt install openssh-server
Upgrading:
  openssh-client

Installing:
  openssh-server

Installing dependencies:
  libwrap0  ncurses-term  openssh-sftp-server  ssh-import-id
...
Continue? [Y/n] Y
...
Creating config file /etc/ssh/sshd_config with new version
Creating SSH2 RSA key; this may take some time ...
3072 SHA256:thkYzoobvxKHDY9kDns2MuqB1KOmZOdJ3d9c5f/KTD0 root@labor (RSA)
Creating SSH2 ECDSA key; this may take some time ...
256 SHA256:RClt9obROtQy/l0z77CeHnNCom2A5tzJTEIpgT0Lt+0 root@labor (ECDSA)
Creating SSH2 ED25519 key; this may take some time ...
256 SHA256:wNZ8yXKbBf8Si12Ie8pjqJdgbEqnuvLvD4qb6M7qYnw root@labor (ED25519)
Creating user 'sshd' (sshd user) with UID 985 and GID 65534.
Created symlink '/etc/systemd/system/sockets.target.wants/ssh.socket' → '/usr/lib/systemd/system/ssh.socket'.
...
```

Drei Dinge fallen auf. Erstens bringt apt auf dem Testsystem den Client `openssh-client` auf eine neuere Version: Das Paket des Servers verlangt in seiner Beschreibung genau dieselbe Version des Clients ([Kapitel 9, Abschnitt 1.5](/wissen/informatik/linux-und-kommandozeile/software-installieren-paketverwaltung/pakete-und-ihre-beziehungen.html#stufe-1-5)), und der Client war noch nicht auf dem neuesten Stand. Ist dein System aktuell, fällt diese Zeile weg. Zweitens erzeugt die Installation drei Schlüssel; die langen Zeichenketten hinter `SHA256:` sind ihre Kennzeichen. Drittens legt sie ein Systemkonto `sshd` an ([Kapitel 7, Abschnitt 1.4](/wissen/informatik/linux-und-kommandozeile/benutzer-gruppen-und-rechte/benutzer-und-gruppen.html#stufe-1-4)). Unter diesem Konto ohne Rechte arbeitet der Server alles ab, was ein Fremder vor der Anmeldung schicken kann; so richtet ein Fehler in diesem Teil möglichst wenig Schaden an ([Kapitel 8, Abschnitt 7.9](/wissen/informatik/linux-und-kommandozeile/prozesse-signale-und-dienste/dienste-und-systemd.html#stufe-7-9)).

:::hintergrund Warum die eigene Datei Vorrang hat
Liest der Server eine Einstellung mehrmals, gilt bei den meisten Einstellungen der erste Wert, den er findet. Weil `/etc/ssh/sshd_config` die Dateien aus `sshd_config.d` gleich in ihrer ersten wirksamen Zeile einliest, stehen deren Werte vor allen Werten der Hauptdatei und gewinnen. Unter mehreren eigenen Dateien gewinnt die, deren Name im Alphabet früher kommt; deshalb beginnen solche Dateinamen oft mit einer Zahl wie `10-`. Ausnahmen sind Einstellungen, die mehrere Werte sammeln, wie `ListenAddress`: Dort werden alle gefundenen Werte zusammengezählt. Der Vorteil eigener Dateien zeigt sich bei Updates. Die Hauptdatei gehört dem Paket; hat man sie selbst verändert, muss apt beim nächsten Update nachfragen, welche Fassung gelten soll. Eine eigene Datei im Verzeichnis `sshd_config.d` fasst das Paket nie an.
:::

⁠**Kurz gesagt:** Mit einer eigenen Einstellungsdatei, die den Server nur an `localhost` lauschen lässt und Passwörter verbietet, wird der eigene Rechner zu einem Übungsserver, an dem nur du selbst dich anmelden kannst.

### Die Socket-Aktivierung

<span class="anker" id="stufe-1-6"></span>

Nach der Installation sollte der Dienst `sshd` laufen und am Port 22 lauschen. Fragt man systemd nach dem Zustand, ergibt sich ein überraschendes Bild:

```console
$ systemctl status ssh.socket --no-pager
● ssh.socket - OpenBSD Secure Shell server socket
     Loaded: loaded (/usr/lib/systemd/system/ssh.socket; enabled; preset: enabled)
    Drop-In: /run/systemd/generator/ssh.socket.d
             └─addresses.conf
     Active: active (listening) since Fri 2026-11-13 03:06:11 CET; 4s ago
 Invocation: ba81c513bfbb4341b3422bbb75a1bb61
   Triggers: ● ssh.service
     Listen: [::1]:22 (Stream)
             127.0.0.1:22 (Stream)
      Tasks: 0 (limit: 38204)
     Memory: 12K (peak: 264K)
        CPU: 1ms
     CGroup: /system.slice/ssh.socket
$ systemctl status ssh.service --no-pager
○ ssh.service - OpenBSD Secure Shell server
     Loaded: loaded (/usr/lib/systemd/system/ssh.service; disabled; preset: enabled)
     Active: inactive (dead)
TriggeredBy: ● ssh.socket
       Docs: man:sshd(8)
             man:sshd_config(5)
```

Der eigentliche Dienst `ssh.service`, also das Programm `sshd`, läuft nicht ($\circ$, `inactive`). Aktiv ist eine andere Unit, `ssh.socket`, und sie lauscht genau an den beiden Adressen aus der Einstellungsdatei (`Listen:`). Die Stelle, an der ein Programm auf Verbindungen wartet oder über die es eine Verbindung benutzt, heißt *Socket*, englisch für Steckdose.

:::definition Definition 1.4 (Socket-Aktivierung)
<span class="anker" id="satz-1-4"></span>

Bei der __Socket-Aktivierung__ öffnet systemd selbst den Socket eines Dienstes und lauscht an dessen Port. Den Dienst startet systemd erst, wenn die erste Verbindung ankommt, und übergibt ihm dann den Socket mitsamt der wartenden Verbindung.
:::

Unter Ubuntu ist der SSH-Server seit der Version 22.10 so eingerichtet. Die Unit `ssh.socket` ist eingeschaltet, `ssh.service` selbst nicht; systemd startet sie bei Bedarf (`Triggers`, „löst aus“):

```console
$ systemctl is-enabled ssh.socket ssh.service
enabled
disabled
```

Solange niemand eine Verbindung aufgebaut hat, bleibt es dabei:

```console
$ systemctl is-active ssh.socket ssh.service
active
inactive
```

Für dich als Benutzer ändert das nichts: Der Client verbindet sich mit Port 22, und ob dort zuerst systemd oder gleich `sshd` antwortet, merkt er nicht. Abbildung [5](#abb-5) zeigt den Ablauf.

:::abbildung linux/k11socket 5
Socket-Aktivierung. Oben ein Kasten „systemd“ mit einer Steckdose am Port 22, beschriftet `ssh.socket, lauscht an 127.0.0.1:22 und [::1]:22`; darunter ein grauer, gestrichelter Kasten `ssh.service (sshd), inactive`. Eine Verbindung (Pfeil von „Client `ssh`“) kommt an der Steckdose an; systemd startet daraufhin `sshd` (der Kasten wird farbig, aus `inactive` wird `active`) und reicht die Steckdose samt wartender Verbindung hinüber. Unten der Satz: „Der Dienst startet erst, wenn jemand anruft.“
:::

:::hintergrund Warum Ubuntu den Server erst bei Bedarf startet
Die meisten Rechner mit SSH-Server bekommen nur selten eine Verbindung, viele virtuelle Maschinen und Container nie. Ein dauerhaft laufender `sshd` belegt trotzdem Arbeitsspeicher, nach Angaben der Ubuntu-Entwickler mindestens 3 MiB je Maschine. Auf einem Wirt mit Hunderten virtueller Maschinen summiert sich das. Mit der Socket-Aktivierung kostet ein unbenutzter Server nur den Socket in systemd. Einen Haken hat die Sache: Die Adressen und den Port, an denen gelauscht wird, legt jetzt die Unit `ssh.socket` fest, nicht mehr `sshd`. Damit die Einstellungen `ListenAddress` und `Port` trotzdem wirken, liest unter Ubuntu 24.04 und neuer ein kleines Programm von Ubuntu, der Generator `sshd-socket-generator`, sie beim Laden der Units aus den Einstellungsdateien und schreibt daraus die Ergänzung `addresses.conf`, die in der Statusausgabe unter `Drop-In` steht. Ändert man später eine dieser Einstellungen, muss man deshalb systemd die Units neu laden lassen und den Socket neu starten: `sudo systemctl daemon-reload`, dann `sudo systemctl restart ssh.socket`. Ein Neustart von `ssh.service` allein genügt nicht; die Kommentare in `/etc/ssh/sshd_config` weisen darauf hin. Wer alle Units mit `ssh` im Namen auflistet, findet daneben noch `sshd-unix-local.socket`. Diese Unit legt systemd seit seiner Version 256 selbst an, sobald ein SSH-Server installiert ist (Ubuntu 26.04 hat Version 259). Sie lauscht an keinem Port im Netz, sondern an der Socket-Datei `/run/ssh-unix-local/socket`, über die Programme desselben Rechners eine SSH-Verbindung ganz ohne Netz aufbauen können; von einem anderen Rechner aus ist sie nicht zu erreichen. Auf dem Testsystem war sie nach der Installation nur geladen, nicht aktiv.
:::

⁠**Kurz gesagt:** Unter Ubuntu lauscht systemd mit `ssh.socket` am Port 22 und startet `sshd` erst bei der ersten Verbindung.

:::aufgabe Aufgabe 1 ★ Rollen zuordnen
<span class="anker" id="aufg-1"></span>

Ordne zu, was auf welchem Rechner läuft, wenn sich `anna` von ihrem Laptop per SSH an `rechner1` anmeldet und dort `ls` eingibt: das Terminalfenster, der Client `ssh`, der Server `sshd`, die Shell, der Befehl `ls`, die Dateien, die `ls` anzeigt. An welchem Port lauscht der Server normalerweise, und wer baut die Verbindung auf?

:::loesung
Auf Annas Laptop laufen das Terminalfenster und der Client `ssh`. Auf `rechner1` laufen der Server `sshd` (genauer: für die Sitzung ein `sshd-session`), die Shell, in die Anna tippt, und der Befehl `ls`; die Dateien, die `ls` anzeigt, liegen ebenfalls auf `rechner1`. Der Server lauscht normalerweise am Port 22. Die Verbindung baut der Client auf, also Annas Laptop: Ein Server wartet, ein Client ruft an.
:::
:::

:::aufgabe Aufgabe 2 ★★ Den Übungsserver untersuchen
<span class="anker" id="aufg-2"></span>

Richte den Übungsserver wie in Abschnitt [1.5](#stufe-1-5) ein, falls noch nicht geschehen. Lies mit `systemctl status ssh.socket --no-pager` ab, an welchen Adressen und welchem Port der Server lauscht, und erkläre, woher systemd diese Angaben hat. Prüfe mit `systemctl is-active`, ob `ssh.service` läuft, und begründe das Ergebnis.

:::loesung
Die Statusausgabe zeigt unter `Listen:` die Zeilen `[::1]:22 (Stream)` und `127.0.0.1:22 (Stream)`: Der Server lauscht nur an den beiden Adressen des eigenen Rechners, und zwar am Port 22 (Abschnitt [1.6](#stufe-1-6)). Die Angaben stammen aus der Ergänzung `addresses.conf`, die unter `Drop-In` genannt ist. Diese Datei schreibt der Generator `sshd-socket-generator` beim Laden der Units; er liest dafür die Zeilen `ListenAddress` aus `/etc/ssh/sshd_config.d/10-linuxk11.conf`. Ob `ssh.service` läuft, hängt davon ab, ob seit dem letzten Start des Systems schon eine Verbindung kam:

```console
$ systemctl is-active ssh.service
active
```

Hier lief die Prüfung nach den Übungen der vorigen Abschnitte; die erste Verbindung hatte `sshd` gestartet, und er läuft seitdem. Direkt nach der Installation oder nach einem Neustart des Systems lautet die Antwort `inactive`, weil systemd den Dienst erst bei der ersten Verbindung startet. Unter WSL gilt ein Neustart von WSL als Neustart des Systems.
:::
:::

:::aufgabe Aufgabe 3 ★★ Warum fünf Zeilen
<span class="anker" id="aufg-3"></span>

Erkläre für jede der fünf Zeilen in `10-linuxk11.conf`, welche Gefahr sie verhindert. Was wäre anders, wenn du die Datei erst *nach* der Installation anlegst?

:::loesung
<ul>

<li>

Die beiden Zeilen `ListenAddress` verhindern, dass der Server von anderen Rechnern aus erreichbar ist. Ohne sie lauscht er an allen Adressen des Rechners, also auch an der Adresse im WLAN oder im Netz der Hochschule.

</li>

<li>

`PasswordAuthentication no` und `KbdInteractiveAuthentication no` verhindern, dass jemand Passwörter durchprobiert. Die zweite Zeile ist nötig, weil der Server Passwörter auch über ein zweites, allgemeineres Frageverfahren abfragen kann; erst beide zusammen schließen Passwörter ganz aus. Ubuntu setzt die zweite schon in `sshd_config`, die eigene Datei macht es unabhängig davon sicher.

</li>

<li>

`PermitRootLogin no` verhindert die Anmeldung als root, dem Konto, das alles darf und dessen Name überall gleich ist.

</li>

</ul>

Legt man die Datei erst nach der Installation an, läuft der Server zunächst mit den Voreinstellungen: Er lauscht an allen Adressen, und die Anmeldung mit Passwort ist erlaubt. Je nach Netz ist der eigene Rechner dann für einige Minuten von außen erreichbar. Außerdem wirkt eine nachträglich angelegte Datei mit `ListenAddress` erst nach `sudo systemctl daemon-reload` und `sudo systemctl restart ssh.socket` (Hintergrund in Abschnitt [1.6](#stufe-1-6)).
:::
:::

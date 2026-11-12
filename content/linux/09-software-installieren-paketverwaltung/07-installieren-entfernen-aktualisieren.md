---
title: Installieren, entfernen, aktualisieren
pfad: Informatik / Linux und Kommandozeile / Software installieren: Paketverwaltung
adresse: informatik/linux-und-kommandozeile/software-installieren-paketverwaltung
knoten: Kapitel 9: Software installieren: Paketverwaltung
order: 6140700
summary: Jetzt verändert apt das System.
tags: Sperrdatei, Trigger, manuell installiert, automatisch installiert, Konfigurationsdatei
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Jetzt verändert `apt` das System. Dieser Abschnitt zeigt, warum dafür `root` nötig ist, wie man vorher gefahrlos ausprobiert, was passieren würde, und was beim Installieren, Entfernen und Aktualisieren genau geschieht.
:::

### Die Sperre: warum Installieren root braucht

<span class="anker" id="stufe-6-1"></span>

Probiert man das Installieren ohne `sudo`, scheitert `apt` sofort, und die Meldung spricht nicht von Rechten an `/usr`, sondern von einer Datei namens `lock-frontend`.

```console
$ apt install hello
Error: Could not open lock file /var/lib/dpkg/lock-frontend - open (13: Permission denied)
Error: Unable to acquire the dpkg frontend lock (/var/lib/dpkg/lock-frontend), are you root?
$ echo $?
100
$ ls -l /var/lib/dpkg/lock-frontend /var/lib/dpkg/lock
-rw-r----- 1 root root 0 Nov  9 16:35 /var/lib/dpkg/lock
-rw-r----- 1 root root 0 Aug 27 16:11 /var/lib/dpkg/lock-frontend
```

Die Dateien sind leer und gehören `root`, und nur `root` darf sie öffnen. Was haben leere Dateien mit dem Installieren zu tun?

Ein Bild zur Orientierung: das Schild „Besetzt“ an einer Tür. Wer hineinwill, dreht am Riegel; ist schon jemand drin, wartet er. Das Schild schützt nicht vor Dieben, sondern davor, dass zwei Menschen gleichzeitig denselben Raum benutzen.

:::definition Definition 6.1 (Sperrdatei)
<span class="anker" id="satz-6-1"></span>

Eine __Sperrdatei__ ist eine Datei, die ein Programm öffnet und beim Kernel als gesperrt anmeldet, solange es arbeitet. Ein zweites Programm, das dieselbe Datei sperren will, bekommt die Sperre erst, wenn das erste fertig ist. Die Paketverwaltung benutzt `/var/lib/dpkg/lock-frontend` und `/var/lib/dpkg/lock`, damit nie zwei Vorgänge gleichzeitig Pakete installieren oder entfernen.
:::

Der Inhalt der Datei spielt keine Rolle; es kommt nur darauf an, ob gerade ein Prozess die Sperre hält. Endet dieser Prozess, gibt der Kernel die Sperre von selbst frei, auch wenn das Programm abstürzt. Exit-Status 100 ist bei `apt` ein allgemeiner Fehler. Abbildung [25](#abb-25) zeigt zwei Vorgänge, die sich um die Sperre bewerben.

:::abbildung linux/k9sperre 25
Die Datei `/var/lib/dpkg/lock-frontend` als Tür mit Riegel, darüber der Kernel als Verwalter der Riegel. Ein Prozess `unattended-upgrade` (root) dreht den Riegel, Schild „gesperrt“. Ein zweiter Prozess `sudo apt install` (root) kommt dazu und wartet mit einer Sanduhr. Der erste endet und steht grau daneben („beendet: der Kernel gibt die Sperre frei“), der Riegel öffnet sich von selbst, der zweite tritt ein, und der Riegel schließt wieder. Unten ein dritter Versuch `apt install hello` ohne `sudo` als `student`: Er scheitert schon vor der Tür am Schloss `rw-r-----` (`Permission denied`).
:::

⁠**Kurz gesagt:** Installieren braucht `root`, weil es Systemdateien schreibt; `apt` prüft das gleich am Anfang, wenn es die Sperrdatei öffnet, die nur ein Vorgang zur Zeit halten darf.

:::hintergrund Warum eine Sperre und warum root
Die Paketverwaltung ändert in einem Vorgang Hunderte Dateien unter `/usr` und `/etc` und dazu ihre Datenbank. Liefen zwei Vorgänge gleichzeitig, könnten sie dieselbe Datei abwechselnd überschreiben, und in der Datenbank stünde am Ende weder der eine noch der andere Stand. Deshalb sperrt jeder Vorgang zuerst. Das kommt im Alltag tatsächlich vor: Ubuntu installiert Sicherheitsupdates im Hintergrund selbst, und tippst du in diesem Augenblick `sudo apt install`, wartet `apt` und meldet, dass ein anderer Prozess die Sperre hält. Dass die Sperre vom Kernel kommt und nicht vom bloßen Vorhandensein einer Datei, hat einen praktischen Grund: Eine Datei bliebe nach einem Absturz liegen und blockierte alles; eine Sperre des Kernels verschwindet mit dem Prozess. `root` braucht man aus dem Grund, den [Kapitel 7, Abschnitt 4.3](/wissen/informatik/linux-und-kommandozeile/benutzer-gruppen-und-rechte/rechte-bei-verzeichnissen.html#stufe-4-3) erklärt: Die Verzeichnisse `/usr`, `/etc` und `/var/lib/dpkg` gehören `root` und haben für alle anderen kein Schreibrecht. Ein Programm, das dort Dateien anlegt, muss mit der Benutzernummer 0 laufen. Dass `apt` schon an der Sperrdatei scheitert, ist nur der erste Ort, an dem das auffällt.
:::

### Die Simulation

<span class="anker" id="stufe-6-2"></span>

Bevor man ein Paket installiert oder entfernt, will man wissen, was alles mitkommt oder mitgeht. Ein Befehl, der zwanzig Pakete entfernt, obwohl man eines wollte, sollte nicht erst nach dem Drücken der Eingabetaste auffallen.

:::definition Definition 6.2 (Simulation)
<span class="anker" id="satz-6-2"></span>

Mit der Option `-s` (lang `--simulate`) führt `apt` alle Schritte bis auf das Ändern aus: Es löst die Abhängigkeiten auf und zeigt, was es installieren, aktualisieren und entfernen würde, verändert aber nichts. Eine Simulation braucht weder `root` noch die Sperre. Am Ende steht je Vorgang eine Zeile: `Inst` (auspacken), `Conf` (einrichten), `Remv` (entfernen) oder `Purg` (vollständig entfernen).
:::

::::beispiel Was jq mitbringen würde
```console
$ apt -s install jq
NOTE: This is only a simulation!
      apt needs root privileges for real execution.
      Keep also in mind that locking is deactivated,
      so don't depend on the relevance to the real current situation!

Installing:
  jq

Installing dependencies:
  libjq1  libonig5

Summary:
  Upgrading: 0, Installing: 3, Removing: 0, Not Upgrading: 126
Inst libonig5 (6.9.10-1build1 Ubuntu:26.04/resolute [amd64])
Inst libjq1 (1.8.1-4ubuntu2 Ubuntu:26.04/resolute-updates, Ubuntu:26.04/resolute-security [amd64])
Inst jq (1.8.1-4ubuntu2 Ubuntu:26.04/resolute-updates, Ubuntu:26.04/resolute-security [amd64])
Conf libonig5 (6.9.10-1build1 Ubuntu:26.04/resolute [amd64])
Conf libjq1 (1.8.1-4ubuntu2 Ubuntu:26.04/resolute-updates, Ubuntu:26.04/resolute-security [amd64])
Conf jq (1.8.1-4ubuntu2 Ubuntu:26.04/resolute-updates, Ubuntu:26.04/resolute-security [amd64])
```

Die Simulation bestätigt den Graphen aus Abbildung [3](pakete-und-ihre-beziehungen.html#abb-3): drei neue Pakete, `libc6` ist schon da. Der Hinweis am Anfang erinnert daran, dass ohne Sperre ein anderer Vorgang gleichzeitig etwas ändern könnte. Die Reihenfolge ist kein Zufall: `apt` packt zuerst `libonig5` aus, weil beide anderen davon abhängen, und richtet am Schluss alle drei in derselben Reihenfolge ein. `Not Upgrading: 126` sind die installierten Pakete, für die es neuere Versionen gibt; `apt install` rührt sie nicht an.
::::

:::abbildung linux/k9simulation 26
Terminalbild mit `$ apt -s install jq`; die langen Zeilen brechen um wie im Terminal. Die Abschnitte der Ausgabe werden nacheinander gerahmt und nummeriert, die Liste darunter erklärt sie: 1 der Hinweis „nur Simulation: ohne root, ohne Sperre“, 2 `Installing` (verlangt), 3 `Installing dependencies` (mitgebracht), 4 `Summary` mit den Zahlen. Zum Schluss werden die Zeilen `Inst` (5, orange) und `Conf` (6, grün) hinterlegt und den zwei Arbeitsschritten von `dpkg` zugeordnet, „auspacken“ und „einrichten“. Die letzte Zeile erklärt die Reihenfolge `libonig5`, `libjq1`, `jq`: zuerst, wovon die anderen abhängen.
:::

Abbildung [26](#abb-26) beschriftet die Teile der Simulation.

⁠**Kurz gesagt:** `apt -s` zeigt ohne `root` und ohne Folgen, welche Pakete ein Befehl installieren, einrichten oder entfernen würde.

:::hintergrund Dieselbe Simulation mit apt-get
`apt-get -s install jq` simuliert dasselbe, schreibt aber in der älteren, für Skripte gedachten Form:

```console
$ apt-get -s install jq
NOTE: This is only a simulation!
      apt-get needs root privileges for real execution.
      Keep also in mind that locking is deactivated,
      so don't depend on the relevance to the real current situation!
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Solving dependencies... Done
The following additional packages will be installed:
  libjq1 libonig5
The following NEW packages will be installed:
  jq libjq1 libonig5
0 upgraded, 3 newly installed, 0 to remove and 126 not upgraded.
...
```

Die Zeilen `Inst` und `Conf` sind dieselben. In dieser Form begegnet dir die Ausgabe in vielen Anleitungen im Netz, die vor `apt` 3 entstanden sind.
:::

### Installieren: apt install

<span class="anker" id="stufe-6-3"></span>

Jetzt der eigentliche Vorgang. Hinter dem kurzen Befehl stecken alle Begriffe der bisherigen Abschnitte.

:::definition Definition 6.3 (apt install)
<span class="anker" id="satz-6-3"></span>

`sudo apt install paket …` installiert die genannten Pakete in der Kandidatenversion samt allen fehlenden Abhängigkeiten und Empfehlungen. Dazu

<ol>

<li>

löst `apt` die Abhängigkeiten auf und zeigt, was es tun wird;

</li>

<li>

lädt es die Paketdateien in den Paketzwischenspeicher `/var/cache/apt/archives` und prüft jede gegen die Prüfsumme aus der Paketliste;

</li>

<li>

ruft es `dpkg` auf, das je Paket das Skript `preinst` ausführt, den Datenteil auspackt und die Dateien in die Paketdatenbank einträgt;

</li>

<li>

richtet `dpkg` danach jedes Paket ein, indem es `postinst` ausführt.

</li>

</ol>
:::

Werden mehr Pakete installiert, als man genannt hat, oder müssen Pakete weichen, fragt `apt` vorher mit `Continue? [Y/n]` nach; die Eingabetaste oder `Y` setzt fort, ein `n` bricht ab, ohne etwas zu verändern. Ältere Fassungen von `apt` fragen mit `Do you want to continue? [Y/n]`. Kommt genau das genannte Paket dazu, legt `apt` ohne Rückfrage los. Abbildung [27](#abb-27) zeigt den Ablauf.

:::abbildung linux/k9installieren 27
Der Ablauf von `sudo apt install jq` als Fließband mit vier Stationen. 1 „Auflösen“: aus `jq` werden drei Kärtchen (`jq`, `libjq1`, `libonig5`). 2 „Laden und prüfen“: drei Paketdateien kommen vom Server in `/var/cache/apt/archives`, jede bekommt einen grünen Haken „Prüfsumme stimmt“. 3 „Auspacken“ (`dpkg`, Zeilen `Inst`): `preinst`, dann wandern die Dateien in den Verzeichnisbaum und die Dateilisten in die Paketdatenbank. 4 „Einrichten“ (Zeilen `Conf`): `postinst` läuft, das Paket ist „installiert“. `preinst` und `postinst` sind gestrichelt: Sie laufen nur, wenn ein Paket sie mitbringt. Über allen Stationen hängt das Schild „gesperrt“ der Sperrdatei; am Ende wird es abgenommen.
:::

:::warnung Installieren nur mit Bedacht
Ein installiertes Paket führt seine Wartungsskripte mit den Rechten von `root` aus und legt Dateien im ganzen System ab. Installiere deshalb nur Pakete aus den Paketquellen deiner Distribution, lies vorher die Simulation und installiere auf einem Rechner, der dir nicht gehört, nur mit Erlaubnis. Für die Übung in diesem Kapitel genügt das winzige Paket `hello`, das keine Abhängigkeit mitbringt, die nicht schon installiert ist, und keine Wartungsskripte hat.
:::

::::beispiel hello installieren
Die Simulation zeigt, dass nur `hello` selbst dazukommt:

```console
$ apt -s install hello
NOTE: This is only a simulation!
      apt needs root privileges for real execution.
      Keep also in mind that locking is deactivated,
      so don't depend on the relevance to the real current situation!

Installing:
  hello

Summary:
  Upgrading: 0, Installing: 1, Removing: 0, Not Upgrading: 126
Inst hello (2.10-5build1 Ubuntu:26.04/resolute [amd64])
Conf hello (2.10-5build1 Ubuntu:26.04/resolute [amd64])
```

Auf dem Testsystem sah die echte Installation so aus. `apt` fragt dabei nicht nach, weil genau das genannte Paket dazukommt:

```console
$ sudo apt install hello
Installing:
  hello

Summary:
  Upgrading: 0, Installing: 1, Removing: 0, Not Upgrading: 126
  Download size: 26.1 kB
  Space needed: 106 kB / 1022 GB available

Get:1 http://archive.ubuntu.com/ubuntu resolute/main amd64 hello amd64 2.10-5build1 [26.1 kB]
Fetched 26.1 kB in 0s (191 kB/s)

Selecting previously unselected package hello.
(Reading database ... 44601 files and directories currently installed.)
Preparing to unpack .../hello_2.10-5build1_amd64.deb ...
Unpacking hello (2.10-5build1) ...
Setting up hello (2.10-5build1) ...
Processing triggers for man-db (2.13.1-1build1) ...
Processing triggers for install-info (7.2-5ubuntu2) ...
$ type hello
hello is /usr/bin/hello
$ hello
Hello, world!
$ dpkg -l hello | tail -n 1
ii  hello          2.10-5build1 amd64        example package based on GNU hello
```

Die Zeilen folgen den Schritten der Definition. `Get` lädt die Paketdatei, `Preparing to unpack` holt sie aus dem Paketzwischenspeicher; die drei Punkte kürzen dort den Pfad `/var/cache/apt/archives` ab. `Unpacking` entspricht der Zeile `Inst` der Simulation, `Setting up` der Zeile `Conf`. Danach findet die Shell den Befehl `hello` im Suchpfad ([Kapitel 5, Abschnitt 5.3](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/wie-die-shell-programme-findet-path.html#stufe-5-3)), und `dpkg -l hello` zeigt `ii`.

Die beiden Zeilen `Processing triggers` gehören nicht zu `hello`. Die Pakete `man-db` und `install-info` haben bei `dpkg` angemeldet, dass sie benachrichtigt werden wollen, sobald ein Paket Dateien in `/usr/share/man` oder `/usr/share/info` ablegt. Eine solche Anmeldung heißt __Trigger__. `man-db` bringt daraufhin zum Beispiel die Datenbank auf den neuesten Stand, die `apropos` durchsucht ([Kapitel 2, Abschnitt 4.6](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/hilfe-finden.html#stufe-4-6)).
::::

⁠**Kurz gesagt:** `sudo apt install` löst auf, lädt und prüft die Paketdateien und lässt `dpkg` sie auspacken, eintragen und mit ihren Skripten einrichten.

### Manuell und automatisch installiert

<span class="anker" id="stufe-6-4"></span>

Installiert man `jq`, kommen `libjq1` und `libonig5` mit. Entfernt man `jq` später, braucht niemand mehr die beiden Bibliotheken. Woher soll `apt` wissen, dass sie nur wegen `jq` da waren?

:::definition Definition 6.4 (Manuell und automatisch installiert)
<span class="anker" id="satz-6-4"></span>

Ein Paket ist __manuell installiert__, wenn ein Benutzer es ausdrücklich verlangt hat. Es ist __automatisch installiert__, wenn `apt` es nur als Abhängigkeit oder Empfehlung eines anderen Pakets mitgebracht hat. `apt` merkt sich diese Markierung in der Datei `/var/lib/apt/extended_states`. `apt-mark showmanual` und `apt-mark showauto` listen die Pakete jeder Art.
:::

Mit `sudo apt-mark manual paket` und `sudo apt-mark auto paket` ändert man die Markierung, zum Beispiel wenn man eine Bibliothek, die als Abhängigkeit kam, selbst weiterbenutzen will.

::::beispiel Die Markierungen auf dem Testsystem
Auf dem Testsystem ist `hello` aus Unterabschnitt [6.3](#stufe-6-3) jetzt installiert:

```console
$ dpkg -l | grep -c '^ii'
630
$ apt-mark showmanual | head -n 5
acl
bash
bind9-dnsutils
binutils
build-essential
$ apt-mark showmanual | wc -l
43
$ apt-mark showauto | wc -l
587
$ apt-mark showmanual | grep hello
hello
```

Von 630 Paketen sind nur 43 ausdrücklich gewünscht, darunter `hello`, denn es wurde mit seinem Namen verlangt; 587 sind deren Abhängigkeiten. Das ist typisch: Wenige Pakete, die man wirklich will, ziehen viele nach sich.
::::

⁠**Kurz gesagt:** `apt` merkt sich, welche Pakete du verlangt hast und welche nur als Abhängigkeit kamen; daran erkennt es später, was überflüssig geworden ist.

### Entfernen: remove, purge und autoremove

<span class="anker" id="stufe-6-5"></span>

Beim Entfernen stellt sich eine Frage, die man sich beim Installieren nicht stellt: Was ist mit Einstellungen, die der Verwalter in der Zwischenzeit angepasst hat? Wer ein Programm nur vorübergehend entfernt, will sie behalten; wer es loswerden will, nicht.

:::definition Definition 6.5 (Konfigurationsdatei eines Pakets)
<span class="anker" id="satz-6-5"></span>

Eine __Konfigurationsdatei__ eines Pakets ist eine Datei, meist unter `/etc`, die das Paket als veränderbar kennzeichnet; sie steht in der Datei `paket.conffiles` der Paketdatenbank. `dpkg` überschreibt eine solche Datei nie still: Hat der Verwalter sie geändert und bringt eine neue Version eine andere mit, fragt `dpkg` beim Aktualisieren nach.
:::

Für das Entfernen gibt es drei Befehle:

<ul>

<li>

`sudo apt remove paket` entfernt das Paket, lässt aber seine Konfigurationsdateien stehen. `dpkg -l` zeigt danach `rc`: gewünscht „entfernen“, vorhanden „nur Konfigurationsdateien“.

</li>

<li>

`sudo apt purge paket` entfernt das Paket samt seinen Konfigurationsdateien. Dateien in den Heimatverzeichnissen der Benutzer bleiben in jedem Fall.

</li>

<li>

`sudo apt autoremove` entfernt alle automatisch installierten Pakete, die kein manuell installiertes Paket mehr braucht.

</li>

</ul>

::::beispiel cron entfernen, nur simuliert
```console
$ apt -s remove cron
NOTE: This is only a simulation!
      apt needs root privileges for real execution.
      Keep also in mind that locking is deactivated,
      so don't depend on the relevance to the real current situation!

The following package was automatically installed and is no longer required:
  cron-daemon-common
Use 'apt autoremove' to remove it.

REMOVING:
  cron

Summary:
  Upgrading: 0, Installing: 0, Removing: 1, Not Upgrading: 126
Remv cron [3.0pl1-200ubuntu1]
```

In eckigen Klammern steht die Version, die entfernt würde. Ohne `cron` braucht niemand mehr das automatisch installierte `cron-daemon-common`; `apt` entfernt es nicht von selbst, sondern weist auf `apt autoremove` hin. Dieselbe Simulation mit `purge`:

```console
$ apt -s purge cron
...
REMOVING:
  cron*

Summary:
  Upgrading: 0, Installing: 0, Removing: 1, Not Upgrading: 126
Purg cron [3.0pl1-200ubuntu1]
```

Der Stern hinter dem Namen und die Zeile `Purg` kennzeichnen das vollständige Entfernen: Auch die fünf Konfigurationsdateien aus Unterabschnitt [2.7](die-paketverwaltung-und-ihre-datenbank.html#stufe-2-7) würden gelöscht.
::::

::::beispiel hello wieder entfernen
Echt entfernt wird auf dem Testsystem nur `hello` aus Unterabschnitt [6.3](#stufe-6-3). Diesmal fragt `apt` nach, denn ein Paket verschwindet:

```console
$ sudo apt purge hello
REMOVING:
  hello*

Summary:
  Upgrading: 0, Installing: 0, Removing: 1, Not Upgrading: 126
  Freed space: 106 kB

Continue? [Y/n] Y
(Reading database ... 44606 files and directories currently installed.)
Removing hello (2.10-5build1) ...
Processing triggers for install-info (7.2-5ubuntu2) ...
Processing triggers for man-db (2.13.1-1build1) ...
$ sudo apt autoremove
Summary:
  Upgrading: 0, Installing: 0, Removing: 0, Not Upgrading: 126
$ dpkg -l hello
dpkg-query: no packages found matching hello
$ ls /usr/share/doc/hello
ls: cannot access '/usr/share/doc/hello': No such file or directory
```

Nach dem `Y` löscht `dpkg` die Dateien aus `hello.list`, und die Trigger von `man-db` und `install-info` laufen noch einmal. `apt autoremove` findet nichts, denn `hello` hatte keine Abhängigkeit mitgebracht. Die Paketdatenbank kennt `hello` danach nicht mehr, und das Verzeichnis mit Lizenz und Änderungslisten ist verschwunden. Das Testsystem hat wieder 629 Pakete, 42 davon manuell installiert.
::::

:::abbildung linux/k9entfernen 28
Drei Spalten für `remove`, `purge` und `autoremove`; die Zeilen sind Programmdateien unter `/usr`, Konfigurationsdateien unter `/etc`, eine automatisch installierte Bibliothek und Dateien im Heimatverzeichnis. `remove` und `purge` beginnen mit allen vier. Bei `remove` verschwinden die Programmdateien, `/etc` bleibt, `dpkg -l` zeigt `rc`, und die Bibliothek ist jetzt verwaist (orange). Bei `purge` verschwinden zusätzlich die Dateien unter `/etc`. `autoremove` kommt danach, beginnt also mit dem Stand nach `remove`, und entfernt die verwaiste Bibliothek. Das Heimatverzeichnis bleibt in allen drei Spalten unberührt (grüne Haken).
:::

⁠**Kurz gesagt:** `remove` lässt die Konfigurationsdateien stehen, `purge` löscht auch sie, `autoremove` räumt überflüssig gewordene Abhängigkeiten ab; Dateien im Heimatverzeichnis bleiben immer.

### Aktualisieren: upgrade und full-upgrade

<span class="anker" id="stufe-6-6"></span>

Nach `apt update` kennt `apt` für 126 installierte Pakete neuere Versionen. Sie zu installieren ist eine eigene Aufgabe, denn `apt install` lässt alle Pakete, die man nicht nennt, in Ruhe.

:::definition Definition 6.6 (apt upgrade, apt full-upgrade)
<span class="anker" id="satz-6-6"></span>

`sudo apt upgrade` bringt alle installierten Pakete auf ihre Kandidatenversion. Braucht eine neue Version eine zusätzliche Abhängigkeit, installiert es sie mit; ein Paket entfernt es nie. Lässt sich ein Paket nur aktualisieren, wenn ein anderes weicht, bleibt es auf der alten Version. `sudo apt full-upgrade` darf dagegen auch Pakete entfernen, wenn das nötig ist, um alles zu aktualisieren.
:::

Welche Pakete betroffen wären, zeigt `apt list --upgradable`:

```console
$ apt list --upgradable 2>/dev/null | head -n 4
Listing...
apt/resolute-updates,resolute-security 3.2.1ubuntu0.1 amd64 [upgradable from: 3.2.0]
base-files/resolute-updates 14ubuntu6.3 amd64 [upgradable from: 14ubuntu6.2]
bsdextrautils/resolute-updates,resolute-security 2.41.3-3ubuntu2.2 amd64 [upgradable from: 2.41.3-3ubuntu2]
$ apt list --upgradable 2>/dev/null | grep -c upgradable
126
```

`2>/dev/null` verwirft die Warnung von `apt` ([Kapitel 4, Abschnitt 2.4](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/ausgaben-umleiten.html#stufe-2-4)). Sogar `apt` selbst hat eine neue Version.

::::beispiel Was upgrade tun würde
```console
$ apt -s upgrade | grep -A 3 '^Summary'

WARNING: apt does not have a stable CLI interface. Use with caution in scripts.

Summary:
  Upgrading: 121, Installing: 0, Removing: 0, Not Upgrading: 5
Inst motd-news-config [14ubuntu6.2] (14ubuntu6.3 Ubuntu:26.04/resolute-updates [all])
Inst base-files [14ubuntu6.2] (14ubuntu6.3 Ubuntu:26.04/resolute-updates [amd64])
```

Beim Aktualisieren steht in der Zeile `Inst` die alte Version in eckigen Klammern, die neue in runden. 121 der 126 Pakete würden aktualisiert, fünf nicht. Warum, sagt eine weitere Zeile der Ausgabe:

```console
$ apt -s upgrade | grep -A 3 'phasing'

WARNING: apt does not have a stable CLI interface. Use with caution in scripts.

Not upgrading yet due to phasing:
  distro-info                  snapd
  python3-distro-info          software-properties-common
  python3-software-properties
```

Der folgende Hintergrund erklärt die gestaffelte Verteilung, auf Englisch „phasing“.
::::

:::abbildung linux/k9upgrade 29
Zwei Reihen mit denselben vier Paketen A bis D, jedes mit einem Schild für die installierte Version; über A, B und C wartet die Kandidatenversion („neu“). Oben `apt upgrade`: A und B bekommen ihren Kandidaten, C bleibt stehen („kept back“), weil seine neue Version mit D in Konflikt steht und D dafür verdrängen müsste. Unten `apt full-upgrade`: Auch C wird aktualisiert, dafür weicht D (rot durchgestrichen, „entfernt“). Darunter ein Balken für das Testsystem mit 126 aktualisierbaren Paketen: 121 grün „jetzt“, 5 grau „gestaffelt, später“.
:::

Abbildung [29](#abb-29) stellt beide Befehle nebeneinander.

⁠**Kurz gesagt:** `apt upgrade` aktualisiert alle installierten Pakete, ohne eines zu entfernen; `apt full-upgrade` darf dafür auch entfernen. Vorher holt `apt update` die Listen, sonst gibt es nichts Neues zu installieren.

:::hintergrund Gestaffelte Updates: warum nicht jeder Rechner alles sofort bekommt
Ein fehlerhaftes Update, das auf einen Schlag Millionen Rechner erreicht, richtet großen Schaden an. Ubuntu verteilt deshalb Updates aus `resolute-updates` schrittweise. In der Paketliste steht dazu ein Feld `Phased-Update-Percentage` mit einem Prozentwert. Jeder Rechner bildet aus dem Namen des Pakets, der Version und seiner eigenen Kennung in `/etc/machine-id` eine Zahl zwischen 0 und 100, die zufällig aussieht, aber für diesen Rechner und diese Version immer gleich ist. Liegt sie über dem Prozentwert, wartet der Rechner noch. Steigen keine Fehlermeldungen an, erhöht Ubuntu den Wert, bis alle Rechner das Update bekommen. Sicherheitsupdates werden nie gestaffelt, denn bei ihnen wiegt der Schaden durch Warten schwerer.
:::

### Aufgaben zu Abschnitt [6](#stufe-6)

<span class="anker" id="stufe-6-7"></span>

:::aufgabe Aufgabe 17 ★ Die Meldung ohne sudo
<span class="anker" id="aufg-17"></span>

Erkläre jedes Teil der Meldung `Could not open lock file /var/lib/dpkg/lock-frontend - open (13: Permission denied)`: Welche Datei, welcher Systemaufruf, welcher Fehler, und warum genau dieser? Benutze die Ausgabe von `ls -l` aus Unterabschnitt [6.1](#stufe-6-1).

:::loesung
`/var/lib/dpkg/lock-frontend` ist die Sperrdatei, die `apt` zuerst öffnet. `open` ist der Systemaufruf, mit dem ein Programm eine Datei öffnet ([Kapitel 1, Abschnitt 1.4](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/betriebssystem-kernel-und-distribution.html#stufe-1-4)). Der Fehler 13 heißt `Permission denied`: Der Kernel verweigert das Öffnen. Die Datei hat die Rechte `rw-r-----` mit Besitzer und Gruppe `root`. Für `student` gilt die Klasse „andere“ mit `---`, also kein Recht ([Kapitel 7, Abschnitt 5.2](/wissen/informatik/linux-und-kommandozeile/benutzer-gruppen-und-rechte/wie-der-kernel-rechte-pruft.html#stufe-5-2)). `apt` deutet das richtig und fragt `are you root?`.
:::
:::

:::aufgabe Aufgabe 18 ★★ Simulieren mit und ohne Empfehlungen
<span class="anker" id="aufg-18"></span>

(a) Simuliere `apt -s install fortune-mod` und zähle die Pakete. (b) Simuliere dasselbe mit der Option `--no-install-recommends`. Welches Paket fehlt, und warum? (c) Mit welchem Befehl prüfst du, dass Ubuntu Empfehlungen in der Voreinstellung mitinstalliert? Tipp: `apt-config dump` zeigt alle Einstellungen von `apt`.

:::loesung
```console
$ apt-config dump | grep -E 'Install-(Recommends|Suggests)'
APT::Install-Recommends "1";
APT::Install-Suggests "0";
$ apt -s install fortune-mod | grep -E '^(Inst|  Upgrading)'

WARNING: apt does not have a stable CLI interface. Use with caution in scripts.

Installing:
Installing dependencies:
  Upgrading: 0, Installing: 3, Removing: 0, Not Upgrading: 126
Inst librecode3 (3.7.15-3 Ubuntu:26.04/resolute [amd64])
Inst fortune-mod (1:1.99.1-9.2 Ubuntu:26.04/resolute [amd64])
Inst fortunes-min (1:1.99.1-9.2 Ubuntu:26.04/resolute [all])
$ apt -s install --no-install-recommends fortune-mod | grep -E '^(Inst|  Upgrading)'

WARNING: apt does not have a stable CLI interface. Use with caution in scripts.

Installing:
Installing dependencies:
  Upgrading: 0, Installing: 2, Removing: 0, Not Upgrading: 126
Inst librecode3 (3.7.15-3 Ubuntu:26.04/resolute [amd64])
Inst fortune-mod (1:1.99.1-9.2 Ubuntu:26.04/resolute [amd64])
```

(a) Drei Pakete. Der Ausdruck `^(Inst| Upgrading)` erfasst auch die Überschriften `Installing:`, weil sie mit `Inst` beginnen; gezählt werden die Zeilen `Inst` mit Klammer. (b) Zwei Pakete; es fehlt `fortunes-min`, die Empfehlung. Ohne sie fände `fortune` keine Sprüche. (c) `apt-config dump` zeigt `APT::Install-Recommends "1"`: Empfehlungen werden mitinstalliert; Vorschläge (`Install-Suggests "0"`) nicht.
:::
:::

:::aufgabe Aufgabe 19 ★★★ hello installieren und spurlos entfernen
<span class="anker" id="aufg-19"></span>

Nur auf deinem eigenen Linux, nach dem Kasten „Installieren nur mit Bedacht“: (a) Hole mit `sudo apt update` aktuelle Listen und simuliere `apt -s install hello`. (b) Installiere `hello`. Wo liegt das Programm, und welche Zeile zeigt jetzt `dpkg -l hello`? (c) Ist `hello` manuell oder automatisch installiert? (d) Entferne es mit `sudo apt purge hello`. Prüfe mit `dpkg -l hello`, `ls /usr/share/doc/hello` und `type hello`, dass nichts zurückgeblieben ist. (e) Warum hätte hier auch `remove` genügt?

:::loesung
Auf dem Testsystem lief der ganze Weg einmal echt; die Ausgaben zu (b) stehen in Unterabschnitt [6.3](#stufe-6-3), die zum Entfernen in Unterabschnitt [6.5](#stufe-6-5).

<ol class="al">

<li>

`sudo apt update` holt die Listen; `apt -s install hello` zeigt wie in Unterabschnitt [6.3](#stufe-6-3) genau ein neues Paket.

</li>

<li>

`sudo apt install hello` lädt die Paketdatei, prüft sie und lässt `dpkg` sie auspacken und einrichten, ohne nachzufragen, weil genau das genannte Paket dazukommt. Das Programm liegt in `/usr/bin/hello`: `type hello` meldet `hello is /usr/bin/hello`, `hello` gibt `Hello, world!` aus, und die Zeile von `dpkg -l hello` beginnt mit `ii`.

</li>

<li>

Manuell, denn du hast es mit seinem Namen verlangt: `apt-mark showmanual | grep hello` findet es (Unterabschnitt [6.4](#stufe-6-4)).

</li>

<li>

`sudo apt purge hello` fragt mit `Continue? [Y/n]` nach und entfernt nach `Y` die sechs Dateien; `dpkg` streicht den Eintrag. Danach meldet `dpkg -l hello` `no packages found matching hello`, und `ls /usr/share/doc/hello` meldet `No such file or directory`. Bei `type hello` gibt es eine Überraschung, wenn du `hello` vorher in derselben Shell aufgerufen hast; der Versuch steht unter dieser Liste.

</li>

<li>

`hello` hat keine Konfigurationsdateien (Unterabschnitt [5.3](ein-paket-von-innen.html#stufe-5-3)); `remove` hätte deshalb schon alles entfernt, `purge` ändert nichts mehr.

</li>

</ol>

Der Versuch zu (d), in derselben Shell wie die Installation, also nach dem Aufruf von `hello`:

```console
$ type hello
hello is hashed (/usr/bin/hello)
$ hello
bash: /usr/bin/hello: No such file or directory
$ hash -r
$ type hello
bash: type: hello: not found
$ apt-mark showmanual | wc -l
42
$ dpkg -l | grep -c '^ii'
629
```

Die bash hat sich beim ersten Aufruf gemerkt, wo `hello` liegt ([Kapitel 5, Abschnitt 5.3](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/wie-die-shell-programme-findet-path.html#stufe-5-3)), und versucht es weiter an diesem Ort, obwohl die Datei fehlt. `hash -r` leert diese Merkliste; danach findet auch `type` den Befehl nicht mehr. Eine neue Shell hätte dasselbe bewirkt. Die beiden Zahlen am Schluss sind wieder dieselben wie vor der Installation.
:::
:::

:::aufgabe Aufgabe 20 ★★ Wer räumt die Bibliotheken weg?
<span class="anker" id="aufg-20"></span>

Jemand installiert `jq` und entfernt es später mit `sudo apt remove jq`. (a) Was ist danach mit `libjq1` und `libonig5`? (b) Was meldet `apt` dazu, und was tut `sudo apt autoremove`? (c) Warum entfernt `apt remove` die Bibliotheken nicht gleich mit?

:::loesung
(a) Beide Bibliotheken bleiben installiert; sie sind als automatisch installiert markiert, aber kein manuell installiertes Paket braucht sie mehr. (b) `apt` meldet nach dem Entfernen, wie bei `cron-daemon-common` in Unterabschnitt [6.5](#stufe-6-5), dass die beiden Pakete automatisch installiert wurden und nicht mehr gebraucht werden, und weist auf `apt autoremove` hin. `sudo apt autoremove` entfernt sie dann. (c) `apt` geht vorsichtig vor: Du könntest die Bibliotheken inzwischen selbst benutzen, etwa für ein Programm, das du selbst übersetzt hast und das die Paketverwaltung nicht kennt. Das Abräumen ist deshalb ein eigener Schritt, dessen Liste man vorher liest; wer eine Bibliothek behalten will, markiert sie mit `sudo apt-mark manual`.
:::
:::

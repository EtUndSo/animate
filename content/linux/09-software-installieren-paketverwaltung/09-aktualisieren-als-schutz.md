---
title: Aktualisieren als Schutz
pfad: Informatik / Linux und Kommandozeile / Software installieren: Paketverwaltung
adresse: informatik/linux-und-kommandozeile/software-installieren-paketverwaltung
knoten: Kapitel 9: Software installieren: Paketverwaltung
order: 6140900
summary: Ein aktuelles System ist eines der wirksamsten Mittel gegen Angriffe, die ein einzelner Benutzer selbst in der Hand hat.
tags: Sicherheitsupdate, Zeitfenster, unattended-upgrades
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Ein aktuelles System ist eines der wirksamsten Mittel gegen Angriffe, die ein einzelner Benutzer selbst in der Hand hat. Dieser Abschnitt zeigt, wie Ubuntu Sicherheitslücken behebt, warum ein laufendes Programm nach einem Update noch die alte Fassung benutzt und wie Ubuntu Sicherheitsupdates selbst einspielt.
:::

### Das Sicherheitsupdate

<span class="anker" id="stufe-8-1"></span>

Programme enthalten Fehler, und manche davon kann ein Angreifer ausnutzen, um mehr zu tun, als er darf. Ein solcher Fehler heißt Schwachstelle oder Sicherheitslücke (ausführlich: [Cybersecurity, Kapitel 1, Abschnitt 2.1](/wissen/informatik/cybersecurity/sicherheit-schutzziele-und-spielregeln/von-der-schwachstelle-zum-schaden.html#stufe-2-1)). Wird eine bekannt, muss die Korrektur schnell auf alle Rechner.

:::definition Definition 8.1 (Sicherheitsupdate)
<span class="anker" id="satz-8-1"></span>

Ein __Sicherheitsupdate__ ist eine neue Version eines Pakets, die eine Sicherheitslücke behebt. Ubuntu stellt es in der Ausgabe `resolute-security` bereit, meist zugleich in `resolute-updates`. In einer LTS-Version ([Kapitel 1, Abschnitt 1.7](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/betriebssystem-kernel-und-distribution.html#stufe-1-7)) wechselt Ubuntu dafür in der Regel nicht zu einer neuen Programmversion, sondern baut die Korrektur in die vorhandene ein; die Revision steigt.
:::

::::beispiel Ein Sicherheitsupdate für sudo-rs
```console
$ apt policy sudo-rs
sudo-rs:
  Installed: 0.2.13-0ubuntu1
  Candidate: 0.2.13-0ubuntu1.2
  Version table:
     0.2.13-0ubuntu1.2 500
        500 http://archive.ubuntu.com/ubuntu resolute-updates/main amd64 Packages
        500 http://security.ubuntu.com/ubuntu resolute-security/main amd64 Packages
 *** 0.2.13-0ubuntu1 500
        500 http://archive.ubuntu.com/ubuntu resolute/main amd64 Packages
        100 /var/lib/dpkg/status
```

Die Programmversion bleibt 0.2.13; nur die Revision steigt von `0ubuntu1` auf `0ubuntu1.2`. Die Korrektur steckt im Paket, das Verhalten des Programms bleibt sonst gleich.
::::

:::abbildung linux/k9revision 35
Zwei Wege, eine Lücke zu schließen. Oben: Das Projekt veröffentlicht eine neue Programmversion mit der Korrektur und vielen weiteren Änderungen (neue Funktionen, geänderte Optionen als bunte Kärtchen). Unten der Weg von Ubuntu: Aus dieser neuen Version wird nur das Kärtchen „Korrektur“ herausgenommen und in die vorhandene Version 0.2.13 von `sudo-rs` eingesetzt; das Versionsschild ändert sich nur hinten von `0ubuntu1` zu `0ubuntu1.2`: Die Programmversion bleibt, die Revision steigt. Das Paket erscheint in `resolute-security` und `resolute-updates`.
:::

Abbildung [35](#abb-35) zeigt, wie Ubuntu eine Korrektur in die vorhandene Version einbaut.

⁠**Kurz gesagt:** Ein Sicherheitsupdate behebt eine Lücke; Ubuntu liefert es über `resolute-security` und erhöht meist nur die Revision, nicht die Programmversion.

:::hintergrund Warum LTS-Versionen keine neuen Programmversionen bekommen
Eine neue Programmversion bringt neben der Korrektur auch neue Funktionen, geänderte Optionen und neue Fehler mit. Auf einem Server, der seit Jahren läuft, kann das Skripte und Einstellungen brechen. Ubuntu verspricht in einer LTS-Version deshalb, dass sich das Verhalten der Pakete während der ganzen Pflegezeit möglichst nicht ändert, und nimmt aus der neuen Programmversion nur die Korrektur selbst heraus. Das kostet Arbeit, die Ubuntu für `main` selbst leistet; für `universe` hängt es an Freiwilligen oder an einem Abonnement von Ubuntu Pro (Tabelle [1](paketquellen-und-paketlisten.html#tab-1)). Größere Sprünge wie bei `rust-coreutils` von 0.8.0 auf 0.10.0 sind die Ausnahme.
:::

### Das Zeitfenster nach der Veröffentlichung

<span class="anker" id="stufe-8-2"></span>

Warum ist es so wichtig, Updates bald einzuspielen? Die Antwort liegt im Lebenslauf einer Schwachstelle.

:::definition Definition 8.2 (Zeitfenster einer bekannten Schwachstelle)
<span class="anker" id="satz-8-2"></span>

Spätestens mit dem Sicherheitsupdate wird eine Schwachstelle öffentlich: Die Korrektur verrät, wo der Fehler lag, und Hersteller veröffentlichen Beschreibungen dazu. Ab diesem Augenblick kennen sie auch Angreifer. Das __Zeitfenster__ eines Rechners ist die Zeit zwischen der Veröffentlichung und dem Augenblick, in dem dieser Rechner das Update installiert hat. In dieser Zeit ist er mit einer Lücke angreifbar, die allen bekannt ist.
:::

Für Angreifer sind bekannte, aber auf vielen Rechnern noch offene Lücken besonders bequem: Sie müssen nichts Neues finden, sondern nur Rechner suchen, die noch nicht aktualisiert sind, und das lässt sich automatisieren. Wer regelmäßig aktualisiert, macht sein Zeitfenster kurz. Abbildung [36](#abb-36) zeigt es für drei Rechner.

:::abbildung linux/k9zeitfenster 36
Eine Zeitachse, nicht maßstäblich, mit zwei Marken, „Fehler entsteht“ und „Update veröffentlicht“; ab der zweiten steigt eine rote Kurve „Angriffsversuche“. Darunter drei Rechner als Balken: Rechner A spielt das Update am selben Tag ein (kurzes rotes Stück), Rechner B nach einer Woche, Rechner C erst nach drei Monaten (langes rotes Stück unter dem höchsten Teil der Kurve). Die roten Stücke sind die Zeitfenster; sie beginnen alle bei der Veröffentlichung. Danach ist jeder Rechner geschützt (grün).
:::

::::beispiel Wie viel gerade offen ist
Auf dem Testsystem lagen die Paketlisten acht Tage zurück. Nach `sudo apt update` waren 126 Pakete aktualisierbar; 86 davon stammen auch aus der Sicherheitsausgabe, wie Aufgabe [14](pakete-suchen-und-ansehen.html#aufg-14) nachzählt. Das sind 86 Pakete mit Korrekturen für Lücken, die jeder kennen kann.
::::

⁠**Kurz gesagt:** Mit dem Update wird eine Lücke öffentlich; bis zum Installieren ist der Rechner mit einer allgemein bekannten Lücke angreifbar.

:::hintergrund Warum Aktualisieren zu den wirksamsten einfachen Schutzmaßnahmen gehört
Die Cybersecurity-Reihe zeigt den Lebenszyklus einer Schwachstelle: entstehen, entdeckt, gemeldet, behoben, eingespielt ([Cybersecurity, Kapitel 1, Abschnitt 7.5](/wissen/informatik/cybersecurity/sicherheit-schutzziele-und-spielregeln/schwachstellen-benennen-und-bewerten.html#stufe-7-5)). Eine Untersuchung von Angriffen aus den Jahren 2008 bis 2011 fand, dass Angriffe auf eine Lücke nach ihrer Veröffentlichung um bis zu fünf Größenordnungen zunahmen. Der Mechanismus dahinter: Vor der Veröffentlichung kennen nur wenige die Lücke; danach kann jeder Angreifer sie benutzen, und Programme, die das Netz nach verwundbaren Rechnern absuchen, lassen sich schnell um die neue Lücke ergänzen. Die US-Behörde für Cybersicherheit CISA führt deshalb einen Katalog von Schwachstellen, die nachweislich ausgenutzt werden, und verlangt von Bundesbehörden, sie binnen fester Fristen zu schließen. Gegen eine Lücke, die außer dem Angreifer noch niemand kennt, hilft das Aktualisieren nicht ([Cybersecurity, Kapitel 1, Abschnitt 7.6](/wissen/informatik/cybersecurity/sicherheit-schutzziele-und-spielregeln/schwachstellen-benennen-und-bewerten.html#stufe-7-6)); dagegen helfen die Sicherheitsprinzipien aus der Cybersecurity-Reihe. Gegen eine bekannte Lücke, für die es schon eine Korrektur gibt, hilft es, und es kostet nur einen Befehl.
:::

### Nach dem Update: laufende Programme

<span class="anker" id="stufe-8-3"></span>

Hat `apt upgrade` eine korrigierte Bibliothek installiert, ist dann jedes Programm geschützt? Nicht unbedingt: Ein Programm, das schon lief, kann noch die alte Fassung benutzen.

:::definition Definition 8.3 (Austausch einer Datei durch dpkg)
<span class="anker" id="satz-8-3"></span>

`dpkg` ersetzt eine Datei, indem es die neue Fassung zuerst unter dem Namen `datei.dpkg-new` auspackt und sie dann in einem Schritt auf den alten Namen umbenennt. Der Name zeigt danach auf die neue Datei. Die alte Datei verschwindet erst, wenn kein Prozess sie mehr geöffnet hat ([Kapitel 3, Abschnitt 8.4](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/inode-und-links.html#stufe-8-4)).
:::

Ein laufendes Programm hat seine Programmdatei und seine Bibliotheken geöffnet. Es arbeitet nach dem Update mit der alten Fassung weiter, bis es neu startet.

::::beispiel Eine Programmdatei unter einem laufenden Prozess austauschen
Der Versuch spielt den Austausch mit einer Kopie von `gnusleep` nach, der GNU-Fassung von `sleep`, die eine Zeit lang wartet. Eine umbenannte Kopie des uutils-Programms kennt ihren neuen Namen nicht und bricht ab ([Kapitel 5, Abschnitt 5.4](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/wie-die-shell-programme-findet-path.html#stufe-5-4)); auf einer Distribution ohne uutils nimmt man einfach `/usr/bin/sleep`. `$!` ist die PID des zuletzt im Hintergrund gestarteten Prozesses ([Kapitel 8, Abschnitt 3.2](/wissen/informatik/linux-und-kommandozeile/prozesse-signale-und-dienste/vordergrund-hintergrund-und-jobs.html#stufe-3-2)):

```console
$ cp /usr/bin/gnusleep schlaf
$ ./schlaf 600 &
[1] 777
$ ls -l /proc/$!/exe
lrwxrwxrwx 1 student student 0 Nov 12 00:23 /proc/777/exe -> /home/student/linuxk9/schlaf
$ cp /usr/bin/gnusleep schlaf.neu
$ mv schlaf.neu schlaf
$ ls -l /proc/$!/exe
lrwxrwxrwx 1 student student 0 Nov 12 00:23 /proc/777/exe -> '/home/student/linuxk9/schlaf (deleted)'
$ kill %1
$ rm schlaf
[1]+  Terminated                 ./schlaf 600
```

`/proc/<PID>/exe` zeigt die Programmdatei eines Prozesses ([Kapitel 8, Abschnitt 2.8](/wissen/informatik/linux-und-kommandozeile/prozesse-signale-und-dienste/prozesse-beobachten.html#stufe-2-8)). Nach dem Umbenennen gehört der Name `schlaf` der neuen Datei; der laufende Prozess benutzt weiter die alte, die keinen Namen mehr hat, und der Kernel kennzeichnet sie mit `(deleted)`. Genau so steht es nach einem Update um jedes Programm, das schon lief.
::::

Nach einem Update muss man deshalb die betroffenen Programme neu starten, bei Diensten mit `sudo systemctl restart dienst` ([Kapitel 8, Abschnitt 7.6](/wissen/informatik/linux-und-kommandozeile/prozesse-signale-und-dienste/dienste-und-systemd.html#stufe-7-6)). Nach einem Update des Kernels oder der C-Bibliothek `libc6`, die fast jedes Programm benutzt, startet man am einfachsten den ganzen Rechner neu. Unter WSL schließt man dazu alle Terminals und gibt in Windows `wsl --shutdown` ein; der Kernel von WSL selbst kommt nicht über `apt`, sondern mit den Aktualisierungen von Windows ([Kapitel 1, Abschnitt 4.8](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/wsl-2-linux-neben-windows.html#stufe-4-8)).

:::abbildung linux/k9neustart 37
Links ein laufender Prozess „Dienst“ mit einer Linie zu einer Bibliothek `libbeispiel` (Inode 1, orange, „alte Fassung mit Lücke“). Das Update legt `libbeispiel.dpkg-new` (Inode 2, grün) daneben und benennt sie um: Der Name wandert von Inode 1 zu Inode 2. Die Linie des laufenden Prozesses hängt weiter an Inode 1, die jetzt die Aufschrift „(deleted)“ trägt. Zum Schluss `systemctl restart`: Der alte Prozess endet („beendet“), Inode 1 wird freigegeben und verblasst, und der neu gestartete Dienst hängt an Inode 2.
:::

⁠**Kurz gesagt:** Ein Update tauscht die Datei unter dem Namen aus, nicht im laufenden Programm; geschützt ist ein Programm erst nach seinem Neustart.

### Automatische Sicherheitsupdates

<span class="anker" id="stufe-8-4"></span>

Wer jeden Tag daran denken muss, `apt update` und `apt upgrade` zu tippen, vergisst es irgendwann. Ubuntu nimmt einem diese Arbeit für Sicherheitsupdates ab.

:::definition Definition 8.4 (unattended-upgrades)
<span class="anker" id="satz-8-4"></span>

Das Paket __unattended-upgrades__ installiert Updates ohne Zutun des Benutzers. Unter Ubuntu ist es vorinstalliert und so eingestellt, dass es einmal am Tag die Paketlisten holt und Updates aus der Ausgabe vom Erscheinungstag und aus `resolute-security` einspielt. Die Ausgabe vom Erscheinungstag ändert sich nicht mehr; praktisch spielt es also die Sicherheitsupdates ein. Gestartet wird es von zwei Timer-Units.
:::

Eine Timer-Unit ist eine Unit, die `systemd` zu festen Zeiten eine andere Unit starten lässt ([Kapitel 8, Abschnitt 7.3](/wissen/informatik/linux-und-kommandozeile/prozesse-signale-und-dienste/dienste-und-systemd.html#stufe-7-3)).

::::beispiel Die Einstellungen auf dem Testsystem
```console
$ dpkg -l unattended-upgrades | tail -n 1
ii  unattended-upgrades 2.12ubuntu9  all          automatic installation of security upgrades
$ cat /etc/apt/apt.conf.d/20auto-upgrades
APT::Periodic::Update-Package-Lists "1";
APT::Periodic::Unattended-Upgrade "1";
$ grep -A 3 'Allowed-Origins {' /etc/apt/apt.conf.d/50unattended-upgrades
Unattended-Upgrade::Allowed-Origins {
        "${distro_id}:${distro_codename}";
        "${distro_id}:${distro_codename}-security";
        // Extended Security Maintenance; doesn't necessarily exist for
```

Die erste Datei schaltet das tägliche Holen der Listen und das Einspielen ein, der Wert `1` steht für einen Tag. Die zweite nennt die erlaubten Ausgaben; `${distro_codename}` steht für `resolute`. `resolute-updates` ist nicht dabei: Gewöhnliche Fehlerkorrekturen spielt Ubuntu nicht ungefragt ein. Wann das geschieht, steht in den Timer-Units:

```console
$ cd /usr/lib/systemd/system
$ grep -E '^(Description|OnCalendar|RandomizedDelaySec|Persistent)=' apt-daily.timer apt-daily-upgrade.timer
apt-daily.timer:Description=Daily apt download activities
apt-daily.timer:OnCalendar=*-*-* 6,18:00
apt-daily.timer:RandomizedDelaySec=12h
apt-daily.timer:Persistent=true
apt-daily-upgrade.timer:Description=Daily apt upgrade and clean activities
apt-daily-upgrade.timer:OnCalendar=*-*-* 6:00
apt-daily-upgrade.timer:RandomizedDelaySec=60m
apt-daily-upgrade.timer:Persistent=true
$ cd ~/linuxk9
```

`apt-daily` lädt um 6 und um 18 Uhr, jeweils um bis zu zwölf Stunden zufällig verschoben; `apt-daily-upgrade` spielt um 6 Uhr ein, um bis zu 60 Minuten verschoben. Die zufällige Verschiebung verteilt die Last: Sonst fragten Millionen Rechner in derselben Minute bei den Servern an. `Persistent=true` holt einen Lauf nach, den der Rechner verpasst hat, weil er ausgeschaltet war. Unter WSL ist das der Normalfall, denn die Distribution läuft nur, solange ein Terminal offen ist.
::::

:::abbildung linux/k9timer 38
Ein Zifferblatt über 24 Stunden. `apt-daily` hat zwei Startmarken um 6 und um 18 Uhr, an jede schließt sich ein hellblauer Bogen von zwölf Stunden an (der zweite weiter außen), in dem der Start zufällig fällt; ein Punkt springt an eine zufällige Stelle. `apt-daily-upgrade` hat eine Marke um 6 Uhr mit einem kurzen Bogen bis 7 Uhr. Darunter der Tagesstreifen eines Laptops, der nachts bis 8 Uhr aus ist (grau): Der Lauf um 6 Uhr wird verpasst, ein Pfeil zum Einschalten zeigt „verpasst, wird beim Einschalten nachgeholt“ (`Persistent=true`).
:::

Abbildung [38](#abb-38) zeigt die Zeiten der beiden Timer-Units.

⁠**Kurz gesagt:** `unattended-upgrades` spielt Sicherheitsupdates täglich von selbst ein; zwei Timer-Units von `systemd` bestimmen, wann.

:::warnung Automatik ersetzt nicht das eigene Aktualisieren
`unattended-upgrades` spielt nur Sicherheitsupdates ein, startet keine Dienste neu, die eine geänderte Bibliothek benutzen, und läuft nur, wenn der Rechner läuft. Gewöhne dir trotzdem an, regelmäßig selbst `sudo apt update && sudo apt upgrade` zu tippen ([Kapitel 4, Abschnitt 6.2](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/befehle-verketten.html#stufe-6-2)), vorher die Liste mit `apt list --upgradable` anzusehen und nach Updates von Kernel und `libc6` neu zu starten.
:::

### Der Pflegezeitraum

<span class="anker" id="stufe-8-5"></span>

Sicherheitsupdates gibt es nicht ewig. [Kapitel 1, Abschnitt 1.7](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/betriebssystem-kernel-und-distribution.html#stufe-1-7) hat die Pflegezeiten der Ubuntu-Versionen genannt; für die Paketverwaltung haben sie eine harte Folge.

:::definition Definition 8.5 (Ende der Pflege)
<span class="anker" id="satz-8-5"></span>

Endet der Pflegezeitraum einer Version, kommen in ihre Ausgabe `-security` keine neuen Pakete mehr, auch wenn neue Lücken bekannt werden. Einige Zeit danach verschwinden ihre Paketquellen vom gewöhnlichen Server, und `apt update` meldet nur noch Fehler. Für Ubuntu 26.04 LTS endet die Pflege für `main` im April 2031; für `universe` gibt es Sicherheitspflege nur mit Ubuntu Pro.
:::

Vor dem Ende wechselt man auf die nächste Version; bei Ubuntu erledigt das der Befehl `do-release-upgrade`. Das ist ein großer Schritt, der viele Pakete austauscht; man macht ihn mit einer Sicherung und nicht nebenbei. Abbildung [39](#abb-39) zeigt den Pflegezeitraum von Ubuntu 26.04.

:::abbildung linux/k9pflege 39
Eine Zeitachse von 2026 bis 2032. Ein grüner Balken „`main`: Sicherheitsupdates“ vom 23. April 2026 bis April 2031; ein gestrichelter Balken „`universe`: Sicherheitsupdates nur mit Ubuntu Pro“ darunter. Kleine Punkte auf dem grünen Balken stehen für einzelne Sicherheitsupdates. Ab April 2031 keine Punkte mehr („keine Updates mehr“); ein Pfeil „rechtzeitig wechseln“ zeigt einige Zeit davor nach oben auf einen neuen Balken „nächste LTS-Version“.
:::

⁠**Kurz gesagt:** Ein System ist nur geschützt, solange seine Version gepflegt wird; danach bleibt nur der Wechsel auf eine neuere.

### Aufgaben zu Abschnitt [8](#stufe-8)

<span class="anker" id="stufe-8-6"></span>

:::aufgabe Aufgabe 24 ★★ Die alte Bibliothek im Speicher
<span class="anker" id="aufg-24"></span>

Ein Webserver läuft seit drei Wochen. Gestern hat `unattended-upgrades` ein Sicherheitsupdate für eine Bibliothek eingespielt, die er benutzt. (a) Ist der Webserver jetzt geschützt? Begründe mit dem Versuch aus Unterabschnitt [8.3](#stufe-8-3). (b) Was müsste der Verwalter tun? (c) Woran könnte er einen betroffenen Prozess in `/proc` erkennen?

:::loesung
(a) Nein. Der Webserver hat die Bibliothek beim Start geöffnet und benutzt weiter die alte Fassung mit der Lücke; das Update hat nur den Namen auf die neue Datei umgebogen, wie im Versuch mit `schlaf`.

(b) Den Dienst neu starten, etwa mit `sudo systemctl restart` und dem Namen seiner Unit, oder den Rechner neu starten.

(c) Unter `/proc/<PID>/maps` führt der Kernel die Dateien auf, die ein Prozess in seinen Speicher eingeblendet hat, darunter die Programmdatei und alle Bibliotheken. Eine ersetzte Datei steht dort mit dem Zusatz `(deleted)`. Im Versuch mit `schlaf` findet `grep` fünf solche Zeilen:

```console
$ cp /usr/bin/gnusleep schlaf
$ ./schlaf 600 &
[1] 714
$ cp /usr/bin/gnusleep schlaf.neu
$ mv schlaf.neu schlaf
$ grep -c 'schlaf (deleted)' /proc/$!/maps
5
$ kill %1
$ rm schlaf
[1]+  Terminated                 ./schlaf 600
```

Für eine Bibliothek sucht man genauso nach ihrem Namen mit `(deleted)`.
:::
:::

:::aufgabe Aufgabe 25 ★ Wann die Automatik läuft
<span class="anker" id="aufg-25"></span>

Lies die Timer-Units aus Unterabschnitt [8.4](#stufe-8-4). (a) In welchem Zeitraum eines Tages spielt `apt-daily-upgrade` Updates ein, wenn der Rechner durchläuft? (b) Ein Laptop ist von Freitagabend bis Montag um 9 Uhr ausgeschaltet. Was passiert beim Einschalten, und warum? (c) Warum gibt es zwei Timer statt einem?

:::loesung
(a) Zwischen 6:00 und 7:00 Uhr: `OnCalendar=*-*-* 6:00` plus eine zufällige Verschiebung von bis zu 60 Minuten.

(b) Wegen `Persistent=true` merkt `systemd` beim Start, dass Läufe verpasst wurden, und holt sie kurz nach dem Einschalten nach, für beide Timer.

(c) Die Arbeit ist geteilt: `apt-daily` holt die Listen und lädt die Pakete im Hintergrund vor, zu einer über den Tag verteilten Zeit, damit nicht alle Rechner gleichzeitig die Server belasten; `apt-daily-upgrade` installiert dann, was schon da ist, zu einer festen Zeit am frühen Morgen, wenn der Rechner meist wenig zu tun hat.
:::
:::

:::aufgabe Aufgabe 26 ★★ Warum nicht alles automatisch?
<span class="anker" id="aufg-26"></span>

`unattended-upgrades` spielt Pakete aus `resolute-security` von selbst ein, aus `resolute-updates` nicht. Nenne einen Grund für jede der beiden Entscheidungen. Was spricht auf einem Rechner, den niemand beaufsichtigt, dafür, Sicherheitsupdates automatisch zu installieren, obwohl jedes Update etwas kaputtmachen kann?

:::loesung
Für `resolute-security`: Eine bekannte Lücke ist ab der Veröffentlichung ein offenes Zeitfenster für Angreifer, und Sicherheitsupdates ändern so wenig wie möglich; das Risiko, dass sie etwas kaputtmachen, ist klein im Vergleich zum Risiko des Wartens. Gegen `resolute-updates`: Gewöhnliche Fehlerkorrekturen sind nicht eilig und können Verhalten ändern, auf das sich jemand verlässt; der Verwalter soll sie bewusst einspielen. Auf einem unbeaufsichtigten Rechner spricht für die Automatik, dass sonst niemand die Updates einspielt: Eine offene, allen bekannte Lücke über Wochen ist sehr viel wahrscheinlicher ein Problem als ein seltenes fehlerhaftes Sicherheitsupdate.
:::
:::

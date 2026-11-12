---
title: Die Paketverwaltung und ihre Datenbank
pfad: Informatik / Linux und Kommandozeile / Software installieren: Paketverwaltung
adresse: informatik/linux-und-kommandozeile/software-installieren-paketverwaltung
knoten: Kapitel 9: Software installieren: Paketverwaltung
order: 6140300
summary: Die Paketverwaltung installiert nicht nur, sie führt auch Buch über jede Datei, die sie installiert hat.
tags: Paketverwaltung, Paketdatenbank, dpkg, apt, unverzichtbares Paket, Wartungsskripte
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Die Paketverwaltung installiert nicht nur, sie führt auch Buch über jede Datei, die sie installiert hat. Dieser Abschnitt zeigt, wie die zwei Werkzeuge `dpkg` und `apt` zusammenarbeiten, und befragt die Buchführung: Welche Pakete sind installiert, welche Dateien gehören zu einem Paket, zu welchem Paket gehört eine Datei? Alle Befehle dieses Abschnitts lesen nur und brauchen weder Netz noch `root`.
:::

### Die Paketverwaltung

<span class="anker" id="stufe-2-1"></span>

Abschnitt [1](pakete-und-ihre-beziehungen.html#stufe-1) hat gezeigt, was in einem Paket steckt. Jemand muss die Pakete nun auspacken, ihre Abhängigkeiten auflösen und sich merken, was er wohin gelegt hat, damit er es später wieder findet.

Ein Bild zur Orientierung: ein Lager mit Inventarliste. Für jede Lieferung steht in der Liste, welche Teile dazugehören und in welchem Regal jedes Teil liegt. Ohne Liste müsste man jedes Regal absuchen, um alle Teile einer Lieferung wieder herauszuholen.

:::definition Definition 2.1 (Paketverwaltung, Paketdatenbank)
<span class="anker" id="satz-2-1"></span>

Die __Paketverwaltung__ ist die Gruppe von Programmen, die Pakete installiert, aktualisiert und entfernt und dabei die Abhängigkeiten auflöst. Sie führt eine __Paketdatenbank__: Darin steht für jedes installierte Paket seine Beschreibung, sein Zustand und die vollständige Liste der Dateien, die es installiert hat.
:::

Aus der Liste der Dateien folgt die wichtigste Fähigkeit der Paketverwaltung: Sie kann ein Paket vollständig wieder entfernen, weil sie weiß, welche Dateien dazugehören. Und sie verhindert, dass zwei Pakete still dieselbe Datei überschreiben, denn sie bemerkt, dass die Datei schon einem anderen Paket gehört. Abbildung [6](#abb-6) zeigt die Buchführung.

:::abbildung linux/k9datenbank 6
Links der Verzeichnisbaum, rechts die Paketdatenbank als Tabelle mit den Spalten „Dateien“ und „Paket“: `bash` mit `/usr/bin/bash`, `grep` mit `/usr/bin/grep`, `/usr/share/man/man1/grep.1.gz` und weiteren, `tree` mit `/usr/bin/tree`. Jede Datei im Baum ist durch eine dünne Linie mit ihrer Zeile verbunden. Eine Datei `/etc/hostname` ohne Linie bleibt grau: Sie gehört keinem Paket. Zum Schluss wird die Zeile `tree` markiert, und die mit ihr verbundene Datei im Baum leuchtet: Das ist es, was beim Entfernen verschwindet.
:::

⁠**Kurz gesagt:** Die Paketverwaltung installiert und entfernt Pakete samt Abhängigkeiten und führt in ihrer Datenbank Buch über jedes installierte Paket und jede seiner Dateien.

:::hintergrund Warum Buchführung sauberes Entfernen erst möglich macht
Ein Installationsprogramm unter Windows kopiert Dateien an verschiedene Stellen und trägt Einstellungen ein. Ob es beim Deinstallieren alles wieder findet, hängt davon ab, wie sorgfältig sein Hersteller ein eigenes Deinstallationsprogramm geschrieben hat. Dasselbe Problem hat unter Linux, wer ein Programm selbst aus dem Quelltext übersetzt und mit `make install` verteilt: Danach weiß niemand mehr, welche Dateien dazugehörten. Die Paketverwaltung löst das an einer Stelle für alle Pakete gleich. Sie schreibt beim Installieren jede Datei in ihre Liste, bevor das Paket als installiert gilt, und beim Entfernen arbeitet sie genau diese Liste ab. Deshalb kann sie auch beim Aktualisieren Dateien entfernen, die die neue Version nicht mehr mitbringt. Für Software, die nicht aus Paketen stammt, sind `/usr/local` und `/opt` gedacht ([Kapitel 3, Abschnitt 7.2](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/die-verzeichnisstruktur-von-linux.html#stufe-7-2)): Dort liegt, was die Paketverwaltung nicht kennt, getrennt von dem, was sie verwaltet.
:::

### Zwei Ebenen: dpkg und apt

<span class="anker" id="stufe-2-2"></span>

Die Paketverwaltung von Debian und Ubuntu besteht aus zwei Werkzeugen, die verschiedene Aufgaben haben. Wer sie auseinanderhalten kann, versteht viele Meldungen besser.

:::definition Definition 2.2 (dpkg und apt)
<span class="anker" id="satz-2-2"></span>

__dpkg__ ist die untere Ebene der Paketverwaltung. Es installiert eine einzelne Paketdatei, die schon auf der Platte liegt, entfernt Pakete und führt die Paketdatenbank. Abhängigkeiten prüft es nur: Fehlt eine, bricht es ab, statt sie zu besorgen. __apt__ ist die obere Ebene. Es kennt die Pakete auf den Servern der Distribution, löst Abhängigkeiten auf, lädt die nötigen Paketdateien herunter, prüft sie und ruft dann `dpkg` auf, um sie zu installieren.
:::

Der Name `dpkg` steht für „Debian package“, `apt` für „Advanced Package Tool“. Neben dem Befehl `apt` gibt es die älteren `apt-get` und `apt-cache` mit fast denselben Aufgaben. Abbildung [7](#abb-7) zeigt die Arbeitsteilung.

:::abbildung linux/k9ebenen 7
Zwei Stockwerke. Oben `apt` mit drei Aufgaben „Pakete im Netz finden“, „Abhängigkeiten auflösen“, „herunterladen und prüfen“; ein Pfeil zum Server der Distribution. Unten `dpkg` mit „Paketdatei auspacken“, „Skripte ausführen“, „Buch führen“; ein Pfeil zur Paketdatenbank und zum Verzeichnisbaum. Ein Auftrag „installiere jq“ geht oben hinein, wird zu drei Paketdateien, die nach unten an `dpkg` gereicht werden.
:::

⁠**Kurz gesagt:** `dpkg` installiert einzelne Paketdateien und führt die Datenbank, `apt` besorgt die Pakete samt Abhängigkeiten aus dem Netz und lässt `dpkg` sie installieren.

### Die Liste der installierten Pakete: dpkg -l

<span class="anker" id="stufe-2-3"></span>

Die erste Frage an die Paketdatenbank lautet: Welche Pakete sind überhaupt installiert, und in welcher Version?

:::definition Definition 2.3 (dpkg -l)
<span class="anker" id="satz-2-3"></span>

`dpkg -l` listet die Pakete der Paketdatenbank als Tabelle mit Zustand, Name, Version, Architektur und Kurzbeschreibung. Ohne Argument zeigt es alle Pakete, mit Paketnamen als Argumenten nur diese; Muster wie `'coreutils-*'` sind erlaubt.
:::

Die ersten beiden Spalten jeder Zeile sind zwei Buchstaben für den Zustand. Der erste sagt, was der Verwalter *will*: `i` installieren, `r` entfernen, `p` vollständig entfernen, `h` festhalten, `u` unbekannt. Der zweite sagt, was tatsächlich *ist*: `i` installiert, `n` nicht installiert, `c` nur noch Konfigurationsdateien vorhanden, dazu einige Zwischenzustände für abgebrochene Vorgänge. Ein drittes Zeichen erscheint nur bei einem Fehler. Die drei Kopfzeilen der Ausgabe erklären diese Buchstaben in Kurzform.

::::beispiel Drei Pakete und ein fehlendes
```console
$ dpkg -l bash grep tree
+-- Desired=Unknown/Install/Remove/Purge/Hold
|+- Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
||+ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||| Name           Version      Architecture Description
+++-==============-============-============-=============================================
ii  bash           5.3-2ubuntu1 amd64        GNU Bourne Again SHell
ii  grep           3.12-1       amd64        GNU grep, egrep and fgrep
ii  tree           2.3.1-1      amd64        displays an indented directory tree, in color
```

`ii` heißt: Der Verwalter will das Paket installiert haben, und es ist installiert. Das ist der Normalfall. Nach einem Paket, das es nicht gibt, fragt man vergeblich:

```console
$ dpkg -l hello
dpkg-query: no packages found matching hello
$ echo $?
1
```

Die Meldung stammt von `dpkg-query`, dem Teil von `dpkg`, der Fragen an die Datenbank beantwortet; der Exit-Status 1 heißt hier „nichts gefunden“ ([Kapitel 4, Abschnitt 5.2](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/der-exit-status.html#stufe-5-2)).
::::

:::abbildung linux/k9dpkgl 8
Die Ausgabe von `dpkg -l` mit der Zeile `ii grep 3.12-1 amd64 …`. Die drei Kopfzeilen werden nacheinander farbig mit den ersten drei Spalten verbunden: `Install` mit dem ersten `i` („gewünscht: installieren“), `Inst` mit dem zweiten („Zustand: installiert“), `(none)` mit dem leeren dritten Feld („Fehler: keiner“). Darunter Klammern mit Nummern für Name, Programmversion 3.12, Revision 1, Architektur und Kurzbeschreibung; die Liste daneben erklärt sie.
:::

Wie viele Pakete installiert sind, zählt eine Pipe: Jede Zeile eines installierten Pakets beginnt mit `ii`.

```console
$ dpkg -l | grep -c '^ii'
629
```

Ein ganzes Ubuntu besteht also aus Hunderten Paketen; auf dem Testsystem sind einige davon für die Übungen dieser Reihe nachinstalliert, etwa `tree` aus [Kapitel 3](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-verzeichnisse-und-pfade.html).

⁠**Kurz gesagt:** `dpkg -l` zeigt installierte Pakete mit zwei Zustandsbuchstaben, `ii` heißt gewünscht und installiert.

### Die Dateien eines Pakets: dpkg -L

<span class="anker" id="stufe-2-4"></span>

Die zweite Frage: Welche Dateien hat ein bestimmtes Paket installiert? Das braucht man, wenn man das Programm, die Handbuchseite oder die Beispiele eines Pakets sucht.

:::definition Definition 2.4 (dpkg -L)
<span class="anker" id="satz-2-4"></span>

`dpkg -L paket` gibt die Liste aller Dateien und Verzeichnisse aus, die das installierte Paket `paket` angelegt hat, so wie sie in der Paketdatenbank steht.
:::

::::beispiel Was grep mitgebracht hat
```console
$ dpkg -L grep
/.
/usr
/usr/bin
/usr/bin/egrep
/usr/bin/fgrep
/usr/bin/grep
/usr/bin/rgrep
/usr/share
/usr/share/doc
/usr/share/doc/grep
/usr/share/doc/grep/AUTHORS
/usr/share/doc/grep/NEWS.Debian.gz
/usr/share/doc/grep/NEWS.gz
/usr/share/doc/grep/README
/usr/share/doc/grep/THANKS.gz
/usr/share/doc/grep/TODO.gz
/usr/share/doc/grep/changelog.Debian.gz
/usr/share/doc/grep/copyright
/usr/share/info
/usr/share/info/grep.info.gz
/usr/share/man
/usr/share/man/man1
/usr/share/man/man1/grep.1.gz
/usr/share/man/man1/egrep.1.gz
/usr/share/man/man1/fgrep.1.gz
/usr/share/man/man1/rgrep.1.gz
```

Neben `/usr/bin/grep` hat das Paket drei weitere Befehle mitgebracht, `egrep`, `fgrep` und `rgrep`, dazu je eine Handbuchseite. Die Liste enthält auch Verzeichnisse wie `/usr/bin`, die viele Pakete gemeinsam benutzen. Beim Entfernen löscht `dpkg` ein solches Verzeichnis nur, wenn es danach leer ist.
::::

⁠**Kurz gesagt:** `dpkg -L paket` zeigt alle Dateien, die ein installiertes Paket angelegt hat.

### Zu welchem Paket gehört eine Datei: dpkg -S

<span class="anker" id="stufe-2-5"></span>

Die dritte Frage geht in die umgekehrte Richtung: Zu welchem Paket gehört diese Datei? Man stellt sie, wenn man wissen will, woher ein Befehl kommt, oder bevor man eine fremde Datei unter `/usr` anfasst.

:::definition Definition 2.5 (dpkg -S)
<span class="anker" id="satz-2-5"></span>

`dpkg -S pfad` durchsucht die Dateilisten aller installierten Pakete und gibt jedes Paket aus, zu dem `pfad` gehört, in der Form `paket: pfad`. Gehört der Pfad zu keinem Paket, meldet es `no path found` und endet mit dem Exit-Status 1.
:::

::::beispiel Woher grep, bash und ls kommen
```console
$ dpkg -S /usr/bin/grep /usr/bin/bash /usr/bin/ls
grep: /usr/bin/grep
bash: /usr/bin/bash
coreutils-from-uutils: /usr/bin/ls
```

`grep` und `bash` stammen aus gleichnamigen Paketen. `ls` gehört zum Paket `coreutils-from-uutils`: Auf Ubuntu 26.04 ist `ls` die Rust-Fassung aus dem Projekt uutils ([Kapitel 2, Abschnitt 7.2](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/zwei-fassungen-der-grundbefehle-gnu-und-uutils.html#stufe-7-2)), und dieses Paket legt die Namen der Grundbefehle an.
::::

Nicht jede Datei unter `/etc` stammt aus einem Paket:

```console
$ dpkg -S /etc/hostname
dpkg-query: no path found matching pattern /etc/hostname
$ echo $?
1
```

`/etc/hostname` enthält den Namen genau dieses Rechners; die Installation hat sie für ihn angelegt. Eine Datei, die in keiner Dateiliste steht, löscht `dpkg` auch beim Entfernen eines Pakets nicht.

Abbildung [9](#abb-9) zeigt, dass `dpkg -L` und `dpkg -S` dieselbe Buchführung in zwei Richtungen lesen.

:::abbildung linux/k9zweirichtungen 9
Dieselbe Tabelle „Dateien – Paket“ zweimal benutzt. Oben fragt `dpkg -L grep` von der Spalte „Paket“ aus: Die Zeile `grep` leuchtet, alle ihre Dateien werden aufgezählt. Unten fragt `dpkg -S /usr/bin/ls` von der Spalte „Dateien“ aus: Die Suche läuft durch alle Zeilen, bleibt bei `coreutils-from-uutils` stehen und gibt den Paketnamen aus. Eine dritte Anfrage `/etc/hostname` läuft durch alle Zeilen und endet bei „nicht gefunden“.
:::

⁠**Kurz gesagt:** `dpkg -S pfad` sagt, zu welchem installierten Paket eine Datei gehört; Dateien wie `/etc/hostname`, die in keiner Dateiliste stehen, kennt die Buchführung nicht.

### Der Zustand eines Pakets: dpkg -s

<span class="anker" id="stufe-2-6"></span>

Die vierte Frage: Was steht in der Datenbank über ein bestimmtes installiertes Paket? Das ist die Paketbeschreibung aus Unterabschnitt [1.3](pakete-und-ihre-beziehungen.html#stufe-1-3), ergänzt um den Zustand.

:::definition Definition 2.6 (dpkg -s)
<span class="anker" id="satz-2-6"></span>

`dpkg -s paket` gibt den Eintrag eines Pakets aus der Paketdatenbank aus: die Paketbeschreibung und die Zeile `Status`. Diese nennt mit drei Wörtern, was gewünscht ist, ob ein Fehler vorliegt und welchen Zustand das Paket hat.
:::

Einige Pakete tragen das Feld `Essential: yes`. Ein solches __unverzichtbares Paket__ gehört zu jedem lauffähigen System; andere Pakete dürfen es benutzen, ohne es als Abhängigkeit zu nennen. Die Paketverwaltung entfernt es nur, wenn man es ihr ausdrücklich befiehlt.

::::beispiel Der Eintrag von grep
```console
$ dpkg -s grep
Package: grep
Essential: yes
Status: install ok installed
Priority: required
Section: utils
Installed-Size: 364
Maintainer: Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>
Architecture: amd64
Multi-Arch: foreign
Version: 3.12-1
Provides: rgrep
Pre-Depends: libc6 (>= 2.38), libpcre2-8-0 (>= 10.32)
Conflicts: rgrep
...
```

`install ok installed` heißt: gewünscht ist „installieren“, kein Fehler, Zustand „installiert“. `grep` ist unverzichtbar, denn unzählige Skripte des Systems rufen es auf. Seine Priorität ist `required`, die höchste. `Provides: rgrep` und `Conflicts: rgrep` sind das Muster aus Unterabschnitt [1.8](pakete-und-ihre-beziehungen.html#stufe-1-8): Früher gab es ein eigenes Paket `rgrep`; heute bringt `grep` den Befehl `rgrep` selbst mit und erfüllt den alten Namen.
::::

⁠**Kurz gesagt:** `dpkg -s paket` zeigt Beschreibung und Zustand eines installierten Pakets; `Essential: yes` kennzeichnet unverzichtbare Pakete.

### Wo die Paketdatenbank liegt

<span class="anker" id="stufe-2-7"></span>

Die Datenbank ist kein geheimnisvoller Speicher, sondern eine Sammlung gewöhnlicher Textdateien. Wer weiß, wo sie liegen, versteht, wie `dpkg` arbeitet.

:::definition Definition 2.7 (Ablage der Paketdatenbank)
<span class="anker" id="satz-2-7"></span>

`dpkg` legt seine Datenbank im Verzeichnis `/var/lib/dpkg` ab. Die Datei `status` enthält die Einträge aller Pakete, so wie `dpkg -s` sie zeigt. Im Unterverzeichnis `info` liegt zu jedem Paket eine Datei `paket.list` mit seinen Dateien und eine Datei `paket.md5sums` mit Prüfsummen dieser Dateien; dazu, wenn das Paket welche hat, seine Konfigurationsdateien in `paket.conffiles` und seine Skripte.
:::

Die Skripte eines Pakets heißen __Wartungsskripte__. Es gibt bis zu vier: `preinst` läuft vor dem Auspacken, `postinst` nach dem Auspacken, `prerm` vor dem Entfernen und `postrm` danach. `dpkg` führt sie mit den Rechten von `root` aus. Abbildung [10](#abb-10) zeigt, wann welches läuft.

:::abbildung linux/k9skripte 10
Zwei Zeitleisten. Oben „Installieren“: `preinst` (Skript-Symbol, Schild „root“), dann „Dateien auspacken und in `paket.list` eintragen“, dann `postinst` („einrichten“, etwa einen Dienst anmelden). Unten „Entfernen“: `prerm` (etwa den Dienst anhalten), dann „Dateien aus `paket.list` löschen, Konfigurationsdateien bleiben“, dann `postrm`. Die sechs Schritte sind nummeriert; rechts daneben die Dateien des Pakets `cron` in `/var/lib/dpkg/info` mit der Nummer ihres Schritts, die beim jeweiligen Schritt aufleuchten.
:::

::::beispiel grep und cron in der Datenbank
```console
$ ls /var/lib/dpkg/info/grep.*
/var/lib/dpkg/info/grep.list  /var/lib/dpkg/info/grep.md5sums
$ head -n 5 /var/lib/dpkg/info/grep.list
/.
/usr
/usr/bin
/usr/bin/egrep
/usr/bin/fgrep
$ ls /var/lib/dpkg/info/cron.*
/var/lib/dpkg/info/cron.conffiles  /var/lib/dpkg/info/cron.postrm
/var/lib/dpkg/info/cron.list       /var/lib/dpkg/info/cron.preinst
/var/lib/dpkg/info/cron.md5sums    /var/lib/dpkg/info/cron.prerm
/var/lib/dpkg/info/cron.postinst
$ cat /var/lib/dpkg/info/cron.conffiles
/etc/default/cron
/etc/init.d/cron
/etc/pam.d/cron
/etc/supercat/spcrc-crontab
/etc/supercat/spcrc-crontab-light
```

`grep.list` ist genau die Liste, die `dpkg -L grep` ausgibt. `grep` braucht keine Wartungsskripte. Der Zeitplandienst `cron` aus [Kapitel 8, Abschnitt 7](/wissen/informatik/linux-und-kommandozeile/prozesse-signale-und-dienste/dienste-und-systemd.html#stufe-7) dagegen hat alle vier, denn er muss beim Installieren als Dienst eingerichtet und beim Entfernen wieder abgemeldet werden. Seine Konfigurationsdateien unter `/etc` sind eigens vermerkt, denn der Verwalter darf sie ändern, und solche Änderungen soll die Paketverwaltung nicht einfach überschreiben.
::::

Was `dpkg` tut, schreibt es zusätzlich in die Protokolldatei `/var/log/dpkg.log` ([Kapitel 3, Abschnitt 7.5](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/die-verzeichnisstruktur-von-linux.html#stufe-7-5)). Die letzten drei Installationen auf dem Testsystem:

```console
$ grep ' install ' /var/log/dpkg.log | tail -n 3
2026-11-09 15:57:44 install seabios:all <none> 1.17.0-1ubuntu1
2026-11-09 15:57:44 install qemu-system-x86:amd64 <none> 1:10.2.1+ds-1ubuntu3.3
2026-11-09 15:57:44 install qemu-utils:amd64 <none> 1:10.2.1+ds-1ubuntu3.3
```

Jede Zeile nennt Zeitpunkt, Vorgang, Paket mit Architektur, alte Version (`<none>`: vorher nicht installiert) und neue Version.

:::warnung Die Paketdatenbank nie von Hand ändern
Die Dateien unter `/var/lib/dpkg` gehören `root`, und das hat seinen Grund. Löscht oder ändert man dort etwas, stimmt die Buchführung nicht mehr mit dem System überein: Die Paketverwaltung hält Pakete für installiert, die fehlen, oder überschreibt Dateien, die sie für frei hält. Lesen ist ungefährlich; geändert wird die Datenbank nur über `dpkg` und `apt`.
:::

⁠**Kurz gesagt:** Die Paketdatenbank besteht aus Textdateien unter `/var/lib/dpkg`: `status` für alle Einträge, `info/paket.list` für die Dateien eines Pakets, dazu Prüfsummen, Konfigurationsdateien und die Wartungsskripte, die als `root` laufen.

### Aufgaben zu Abschnitt [2](#stufe-2)

<span class="anker" id="stufe-2-8"></span>

:::aufgabe Aufgabe 5 ★ Woher kommen deine Befehle?
<span class="anker" id="aufg-5"></span>

Finde mit `dpkg -S` heraus, zu welchem Paket `/usr/bin/tree`, `/usr/bin/gnuls` und `/usr/bin/find` gehören. Was sagen dir die Paketnamen bei `gnuls` und `find` ([Kapitel 2, Abschnitt 7](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/zwei-fassungen-der-grundbefehle-gnu-und-uutils.html#stufe-7))?

:::loesung
```console
$ dpkg -S /usr/bin/tree /usr/bin/gnuls /usr/bin/find
tree: /usr/bin/tree
gnu-coreutils: /usr/bin/gnuls
findutils: /usr/bin/find
```

`gnuls` gehört zu `gnu-coreutils`, der GNU-Fassung der Grundbefehle, die Ubuntu 26.04 unter den Namen mit der Vorsilbe `gnu` mitliefert ([Kapitel 2, Abschnitt 7.3](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/zwei-fassungen-der-grundbefehle-gnu-und-uutils.html#stufe-7-3)). `find` gehört zu `findutils`, also zu GNU; die Rust-Fassung ersetzt in Ubuntu 26.04 nur die Grundbefehle der coreutils, nicht `find`.
:::
:::

:::aufgabe Aufgabe 6 ★★ Die Handbuchseite von ls
<span class="anker" id="aufg-6"></span>

(a) Zu welchem Paket gehört `/usr/share/man/man1/ls.1.gz`? (b) Wie viele Einträge hat die Dateiliste des Pakets `coreutils-from-uutils`? Benutze eine Pipe. (c) Sieh dir mit `ls -l` an, was `/usr/bin/ls` und `/usr/bin/cp` sind. Was folgt daraus über die Dateien in der Liste von `coreutils-from-uutils`?

:::loesung
```console
$ dpkg -S /usr/share/man/man1/ls.1.gz
coreutils-from-uutils: /usr/share/man/man1/ls.1.gz
$ dpkg -L coreutils-from-uutils | wc -l
223
$ ls -l /usr/bin/ls /usr/bin/cp
lrwxrwxrwx 1 root root  5 Mar 30  2026 /usr/bin/cp -> gnucp
lrwxrwxrwx 1 root root 29 Mar 30  2026 /usr/bin/ls -> ../lib/cargo/bin/coreutils/ls
```

(a) Die Handbuchseite gehört zu `coreutils-from-uutils`, damit `man ls` immer die Seite der Fassung zeigt, die `ls` tatsächlich ist.

(b) 223 Einträge, Verzeichnisse mitgezählt.

(c) Beide Namen sind symbolische Links, `ls` auf das Multicall-Programm von uutils, `cp` auf `gnucp`. Das Paket `coreutils-from-uutils` enthält also fast nur Links und Handbuchseiten, keine eigenen Programme; die Programme selbst stehen in `rust-coreutils` und `gnu-coreutils`.
:::
:::

:::aufgabe Aufgabe 7 ★ Zustände lesen
<span class="anker" id="aufg-7"></span>

Was bedeuten diese Zeilenanfänge in `dpkg -l`? (a) `ii`, (b) `rc`, (c) `un`, (d) `hi`. Welcher Zustand bleibt nach dem Entfernen eines Pakets mit Konfigurationsdateien zurück?

:::loesung
(a) `ii`: gewünscht installieren, installiert. (b) `rc`: gewünscht entfernen, vorhanden sind nur noch die Konfigurationsdateien. (c) `un`: unbekannt gewünscht, nicht installiert; `dpkg` kennt den Namen, etwa aus einem früheren Vorgang. (d) `hi`: festgehalten (englisch „hold“) und installiert; `apt upgrade` lässt ein solches Paket auf seiner Version. Nach dem Entfernen eines Pakets mit Konfigurationsdateien bleibt `rc` zurück, bis man es mit `purge` vollständig entfernt.
:::
:::

:::aufgabe Aufgabe 8 ★★ Wer lässt Skripte laufen?
<span class="anker" id="aufg-8"></span>

(a) Zähle mit einer Pipe, wie viele Pakete auf deinem System ein `postinst`-Skript haben. (b) Warum ist es für die Sicherheit wichtig, dass diese Skripte nur aus vertrauenswürdigen Paketen stammen? Denke daran, mit welchen Rechten `dpkg` sie ausführt.

:::loesung
(a) Jedes Skript liegt als `paket.postinst` in `/var/lib/dpkg/info`; ein Muster findet sie alle, `wc -l` zählt sie:

```console
$ ls /var/lib/dpkg/info/*.postinst | wc -l
223
```

(b) `dpkg` führt diese Skripte mit der Benutzernummer 0 aus. Ein Skript kann damit jede Datei lesen und ändern, Benutzer anlegen und Dienste einrichten ([Kapitel 7, Abschnitt 1.7](/wissen/informatik/linux-und-kommandozeile/benutzer-gruppen-und-rechte/benutzer-und-gruppen.html#stufe-1-7)). Wer ein Paket installiert, lässt also den Paketbetreuer mit vollen Rechten auf seinen Rechner. Bei den Paketen der Distribution ist das vertretbar, weil die Distribution sie baut und die Kette aus Signatur und Prüfsummen belegt, dass sie unverändert ankommen.
:::
:::

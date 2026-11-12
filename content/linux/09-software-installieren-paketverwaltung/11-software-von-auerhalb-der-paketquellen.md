---
title: Software von außerhalb der Paketquellen
pfad: Informatik / Linux und Kommandozeile / Software installieren: Paketverwaltung
adresse: informatik/linux-und-kommandozeile/software-installieren-paketverwaltung
knoten: Kapitel 9: Software installieren: Paketverwaltung
order: 6141100
summary: Nicht jede Software steht in den Paketquellen der Distribution.
tags: zusätzliche Paketquelle, Snap, Flatpak
lang: de
---

<span class="anker" id="stufe-10"></span>

:::zweck
Nicht jede Software steht in den Paketquellen der Distribution. Dieser Abschnitt zeigt die üblichen anderen Wege, eigene Paketquellen von Herstellern, einzelne Paketdateien, Installationsskripte und Pakete im Format Snap, und was bei jedem Weg von den Prüfungen der vorigen Abschnitte übrig bleibt.
:::

### Eine zusätzliche Paketquelle

<span class="anker" id="stufe-10-1"></span>

Manche Hersteller bieten ihre Programme für Ubuntu in einer eigenen Paketquelle an, damit Updates auf demselben Weg kommen wie alle anderen. Dazu kommen persönliche Paketquellen auf der Plattform Launchpad, kurz PPA („personal package archive“), in denen einzelne Entwickler neuere Versionen anbieten.

:::definition Definition 10.1 (Zusätzliche Paketquelle)
<span class="anker" id="satz-10-1"></span>

Eine __zusätzliche Paketquelle__ ist ein weiterer Eintrag in der Quellenliste, meist als eigene Datei `/etc/apt/sources.list.d/name.sources`, zusammen mit dem öffentlichen Schlüssel ihres Betreibers, meist unter `/etc/apt/keyrings`. Danach behandelt `apt` ihre Pakete wie die von Ubuntu: Sie erscheinen bei `apt search`, werden installiert und mit `apt upgrade` aktualisiert.
:::

Ein solcher Eintrag sieht aus wie die Einträge in `ubuntu.sources`; die Adresse ist hier erfunden:

```text /etc/apt/sources.list.d/beispiel.sources
Types: deb
URIs: https://pakete.example.org/ubuntu/
Suites: resolute
Components: main
Signed-By: /etc/apt/keyrings/beispiel.gpg
```

⁠**Kurz gesagt:** Eine zusätzliche Paketquelle ist ein weiterer Eintrag in der Quellenliste mit eigenem Schlüssel; ihre Pakete behandelt `apt` wie die der Distribution.

:::hintergrund Was man einer zusätzlichen Quelle anvertraut
Mit einer zusätzlichen Quelle vertraut man ihrem Betreiber mehr an, als es scheint. Erstens laufen die Wartungsskripte seiner Pakete als `root`; er kann also alles auf dem Rechner tun. Zweitens kann seine Quelle jedes beliebige Paket anbieten, nicht nur sein eigenes Programm. Bietet sie eine höhere Version eines Systempakets an, etwa von `sudo-rs`, wird diese bei gleicher Priorität zur Kandidatenversion (Unterabschnitt [4.4](pakete-suchen-und-ansehen.html#stufe-4-4)) und beim nächsten `apt upgrade` installiert. `Signed-By` verhindert nur, dass der Schlüssel dieser Quelle die Listen von Ubuntu unterschreibt; welche Pakete in ihrer eigenen Liste stehen, begrenzt es nicht. Drittens hängt die Sicherheit dieser Pakete davon ab, wie sorgfältig der Betreiber seinen geheimen Schlüssel hütet. Deshalb gilt: nur Quellen bekannter Hersteller, nur für das, was man wirklich braucht, und wieder entfernen, was man nicht mehr braucht.
:::

:::abbildung linux/k9fremdquelle 44
Die Versionstabelle von `sudo-rs` wie bei `apt policy`, mit zwei Quellen: Ubuntu (`resolute-updates` und `resolute-security`, je Priorität 500, Version `0.2.13-0ubuntu1.2`) und eine zusätzliche Quelle (`pakete.example.org`, Priorität 500, Version `0.3.0-1`). Erst wird die Priorität verglichen (Gleichstand), dann die Version. Bei gleicher Priorität gewinnt die höhere Version; das Schild „Candidate“ wandert zur zusätzlichen Quelle. `Signed-By` der zusätzlichen Quelle ist als Schloss an ihrer Liste zu sehen: Es prüft, wer die Liste unterschrieben hat, nicht, welche Pakete darin stehen.
:::

Abbildung [44](#abb-44) zeigt, wie eine zusätzliche Quelle ein Systempaket übernehmen könnte; die Version `0.3.0-1` ist erfunden.

### Eine einzelne Paketdatei

<span class="anker" id="stufe-10-2"></span>

Manche Hersteller bieten auf ihrer Webseite nur eine `.deb`-Datei zum Herunterladen an. Abschnitt [5](ein-paket-von-innen.html#stufe-5) hat gezeigt, was darin steckt; jetzt geht es ums Installieren.

:::definition Definition 10.2 (Eine Paketdatei installieren)
<span class="anker" id="satz-10-2"></span>

`sudo dpkg -i datei.deb` installiert eine Paketdatei auf der unteren Ebene: ohne Abhängigkeiten aufzulösen; fehlt eine, bleibt das Paket ausgepackt, aber nicht eingerichtet. `sudo apt install ./datei.deb` installiert dieselbe Datei und holt fehlende Abhängigkeiten aus den Paketquellen. Der Pfad muss einen Schrägstrich enthalten, sonst sucht `apt` ein Paket dieses Namens in den Listen.
:::

Beide Wege prüfen weder Signatur noch Prüfsumme der Datei: Für eine Datei von einer Webseite gibt es keine Release-Datei und keine Paketliste. Und es kommen keine Updates, außer der Hersteller richtet dabei eine Paketquelle ein. Abbildung [45](#abb-45) stellt die beiden Befehle gegenüber.

:::abbildung linux/k9einzeldatei 45
Eine Paketdatei `werkzeug_1.4_amd64.deb` mit dem Etikett „braucht: libonig5“. Links `dpkg -i`: Das Paket wird ausgepackt, die Abhängigkeit fehlt, es bleibt im Zustand „ausgepackt, nicht eingerichtet“ (Warnzeichen, `dpkg -l` zeigt `iU`). Rechts `apt install ./werkzeug_1.4_amd64.deb`: `apt` holt `libonig5` aus den Paketquellen (mit Prüfung, grüner Haken) und lässt dann beide einrichten (`ii`). Neben der Paketdatei selbst nur ein leerer, gestrichelter Kreis: Der grüne Haken der Kette fehlt, denn sie kam nicht aus einer Paketliste.
:::

:::warnung Eine fremde Paketdatei ist ein Programm mit root-Rechten
Wer eine Paketdatei installiert, lässt ihre Wartungsskripte als `root` laufen, noch bevor er das Programm zum ersten Mal startet. Lade `.deb`-Dateien nur von der Webseite des Herstellers selbst, prüfe die Prüfsumme, wenn er eine veröffentlicht, und sieh dir vorher mit `dpkg-deb -I` und `dpkg-deb -c` an, was das Paket mitbringt und ob es Skripte enthält.
:::

⁠**Kurz gesagt:** Eine einzelne Paketdatei installiert `apt install ./datei.deb` samt Abhängigkeiten; geprüft wird sie dabei nicht, und Updates kommen nicht von selbst.

### Installationsskripte aus dem Netz

<span class="anker" id="stufe-10-3"></span>

Viele Projekte empfehlen auf ihrer Webseite eine einzige Zeile, die ein Skript herunterlädt und gleich ausführt. Das ist bequem, und es ist der unsicherste der hier gezeigten Wege.

:::definition Definition 10.3 (Installation per curl | bash)
<span class="anker" id="satz-10-3"></span>

`curl -fsSL https://adresse/install.sh | bash` lädt mit dem Programm `curl` eine Datei aus dem Netz und gibt sie über eine Pipe an `bash` weiter ([Kapitel 4, Abschnitt 4.1](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/pipes-und-filter.html#stufe-4-1)). `bash` führt den Text als Befehle aus, Zeile für Zeile, während er ankommt.
:::

Die Optionen von `curl` bedeuten: `-f` bei einem Fehler des Servers nichts ausgeben, `-s` keine Fortschrittsanzeige, `-S` Fehler trotzdem melden, `-L` Weiterleitungen folgen. Das Skript läuft mit deinen Rechten, und viele solche Skripte rufen darin `sudo` auf. Man sieht nicht, was ausgeführt wird; man prüft weder eine Signatur noch eine Prüfsumme; und die Paketverwaltung erfährt nichts davon, sodass es kein sauberes Entfernen gibt. Abbildung [46](#abb-46) zeigt den Ablauf.

:::abbildung linux/k9curlbash 46
Oben das Terminal: Nach dem Befehl `curl … | bash` sieht man nur eine leere Zeile. Darunter, was dabei geschieht: Vom Server laufen die Zeilen des Skripts über `curl` und eine Pipe zu `bash`, das jede sofort ausführt, eine nach der anderen; unter `bash` sammeln sich die ausgeführten Zeilen. Die Zeile mit `sudo` ist rot („jetzt mit root“). Dann bricht die Verbindung mitten in einer Zeile ab, und `bash` führt die halbe Zeile aus. Ganz unten der sicherere Weg in drei Kästchen: in eine Datei laden, mit `less` lesen, dann `bash datei`.
:::

:::warnung Nie ungelesen ausführen
Die folgende Form wird hier nur gezeigt, damit du sie erkennst; führe sie nicht aus:

```console
$ curl -fsSL https://example.org/install.sh | bash
```

Wenn du einem Projekt vertraust und kein Paket gibt, lade das Skript zuerst in eine Datei, lies es mit `less` und führe es erst dann mit `bash datei` aus. Bricht die Verbindung mitten im Herunterladen ab, führt `bash` bei der Pipe das bis dahin Angekommene aus, womöglich eine halbe Zeile; bei einer heruntergeladenen Datei merkst du den Abbruch vorher.
:::

⁠**Kurz gesagt:** `curl … | bash` führt fremden Code ungesehen mit deinen Rechten aus, ohne Prüfung und ohne Buchführung; besser erst herunterladen, lesen, dann ausführen.

### Snap und Flatpak

<span class="anker" id="stufe-10-4"></span>

Pakete einer Distribution teilen sich Bibliotheken; deshalb muss ein Hersteller sein Programm für jede Distribution und jede Version eigens bauen. Einige Formate gehen den umgekehrten Weg.

:::definition Definition 10.4 (Snap, Flatpak)
<span class="anker" id="satz-10-4"></span>

Ein __Snap__ ist ein Paket in Ubuntus zweitem Paketformat, das ein Programm zusammen mit allen Bibliotheken bündelt, die es braucht. Es ist ein schreibgeschütztes Abbild im Format squashfs ([Kapitel 1, Abschnitt 8.3](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/das-live-system.html#stufe-8-3)), das das Programm `snapd` einhängt und abgeschottet vom übrigen System startet. `snapd` aktualisiert Snaps von selbst aus einem zentralen Angebot von Canonical. __Flatpak__ verfolgt dieselbe Idee und ist bei anderen Distributionen verbreitet.
:::

::::beispiel Snap auf dem Testsystem
```console
$ snap --version
snap          2.76.3
snapd         2.76.3
series        16
ubuntu        26.04
kernel        6.6.87.2-microsoft-standard-WSL2
architecture  amd64
$ snap list
No snaps are installed yet. Try 'snap install hello-world'.
```

Unter WSL ist kein Snap installiert. Auf einem Ubuntu-Desktop ist das anders; dort kommt zum Beispiel der Browser Firefox als Snap, und das gleichnamige Debian-Paket `firefox` installiert nur noch den Snap, wie seine Beschreibung sagt. Die Befehle von Snaps liegen in `/snap/bin`, das deshalb im Suchpfad steht ([Kapitel 2, Abschnitt 3.2](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/arten-von-befehlen.html#stufe-3-2)).
::::

⁠**Kurz gesagt:** Snaps und Flatpaks bringen ihre Bibliotheken selbst mit, laufen abgeschottet und aktualisieren sich selbst; Ubuntu benutzt Snap für einige große Programme.

:::hintergrund Vor- und Nachteile gebündelter Pakete
Für den Hersteller ist ein Snap bequem: Er baut sein Programm einmal und erreicht alle Ubuntu-Versionen. Die Abschottung begrenzt außerdem, was ein Programm auf dem System darf. Der Preis folgt aus dem Hintergrund zu Unterabschnitt [1.5](pakete-und-ihre-beziehungen.html#stufe-1-5): Jeder Snap bringt seine eigenen Kopien der Bibliotheken mit. Das kostet Platz und beim Start Zeit. Und wird in einer Bibliothek eine Lücke gefunden, genügt kein einzelnes Update mehr; jeder Snap, der sie enthält, muss von seinem Hersteller neu gebaut werden. Die Verantwortung für Sicherheitsupdates wandert so von der Distribution zu vielen einzelnen Herstellern.
:::

:::abbildung linux/k9snap 47
Zwei Hälften. Links „Pakete der Distribution“: drei Programme zeigen mit Pfeilen auf eine gemeinsame Bibliothek `libbeispiel`. Rechts „Snaps“: drei Programme, jedes in einer eigenen Kapsel mit einer eigenen Kopie von `libbeispiel`. Eine Lücke wird gefunden (rotes Zeichen an allen Kopien): Links genügt ein Update der einen Bibliothek, alle drei Pfeile werden grün; rechts muss jede Kapsel einzeln vom jeweiligen Hersteller erneuert werden, und die Kapseln werden nacheinander und unterschiedlich schnell grün.
:::

Abbildung [47](#abb-47) stellt beide Arten gegenüber.

:::hintergrund Paketverwaltungen von Programmiersprachen
Viele Programmiersprachen haben eine eigene Paketverwaltung, etwa `pip` für Python, `npm` für JavaScript und `cargo` für Rust. Installiert man damit Pakete für das ganze System, geraten sie leicht mit den Paketen der Distribution in Konflikt: Ein Programm des Systems bekommt dann eine andere Fassung einer Bibliothek, als die Distribution mit ihm geprüft hat, und `dpkg` weiß davon nichts. Ubuntu verhindert das für Python mit einer Datei, die das System-Python als „extern verwaltet“ kennzeichnet:

```console
$ head -n 4 /usr/lib/python3.14/EXTERNALLY-MANAGED
[externally-managed]
Error=To install Python packages system-wide, try apt install
 python3-xyz, where xyz is the package you are trying to
 install.
```

`pip` verweigert dann das Installieren in das System und zeigt diesen Text. Für eigene Projekte installiert man Python-Pakete in eine abgetrennte Umgebung im eigenen Heimatverzeichnis, die die Paketverwaltung des Systems nicht berührt.
:::

### Aufräumen

<span class="anker" id="stufe-10-5"></span>

Das Übungsverzeichnis enthält nur noch die heruntergeladene Paketdatei und den ausgepackten Baum. Beides kann weg; installiert war nichts davon:

```console
$ cd
$ rm -r ~/linuxk9
```

Hast du `hello` installiert, etwa in Aufgabe [19](installieren-entfernen-aktualisieren.html#aufg-19), und mit `purge` wieder entfernt, ist auch davon nichts übrig. Die Paketlisten in `/var/lib/apt/lists` bleiben, wie sie sind; Ubuntu frischt sie ohnehin regelmäßig auf.

### Aufgaben zu Abschnitt [10](#stufe-10)

<span class="anker" id="stufe-10-6"></span>

:::aufgabe Aufgabe 30 ★★ Vier Wege im Vergleich
<span class="anker" id="aufg-30"></span>

Vergleiche vier Wege, ein Programm zu installieren: (1) aus den Paketquellen von Ubuntu, (2) aus einer zusätzlichen Paketquelle des Herstellers, (3) als `.deb`-Datei von der Webseite des Herstellers, (4) per `curl … | bash`. Lege eine Tabelle an mit den Spalten: Wer prüft Herkunft und Unversehrtheit? Kommen Updates von selbst? Lässt es sich sauber entfernen? Mit welchen Rechten läuft fremder Code beim Installieren? Prüfe zum Schluss mit `apt-cache show firefox`, was das Paket `firefox` auf Ubuntu 26.04 installiert.

:::loesung
| Weg | Herkunft und Unversehrtheit | Updates | Entfernen | Code beim Installieren |
|---|---|---|---|---|
| (1) Ubuntu-Quellen | Signatur von Ubuntu und Prüfsummen | ja, über `apt upgrade`, Sicherheitsupdates automatisch | sauber über die Paketdatenbank | Wartungsskripte der Distribution, als `root` |
| (2) Quelle des Herstellers | Signatur des Herstellers und Prüfsummen | ja, über `apt upgrade` | sauber | Wartungsskripte des Herstellers, als `root` |
| (3) `.deb` von der Webseite | niemand, außer man vergleicht selbst eine veröffentlichte Prüfsumme | nein | sauber | Wartungsskripte des Herstellers, als `root` |
| (4) `curl \| bash` | niemand | nur, wenn das Skript selbst etwas einrichtet | nicht über die Paketverwaltung | beliebiger Code, mit deinen Rechten und oft mit `sudo` |

```console
$ apt-cache show firefox | grep -E '^(Version|Description)'
Version: 1:1snap1-0ubuntu9.1
Description-en: Installs Firefox snap and provides some system integration
...
```

Das Paket `firefox` hat die Version `1:1snap1-0ubuntu9.1` und installiert laut Beschreibung den Snap; der Browser selbst kommt also über Snap, nicht als Debian-Paket. Die Zeile `Version` erscheint zweimal, weil zwei Versionen in den Paketlisten stehen.
:::
:::

:::aufgabe Aufgabe 31 ★ dpkg -i oder apt install?
<span class="anker" id="aufg-31"></span>

Ein Hersteller bietet `werkzeug_1.4_amd64.deb` an, das von `libonig5` abhängt; auf deinem System ist `libonig5` nicht installiert. (a) Was passiert bei `sudo dpkg -i werkzeug_1.4_amd64.deb`? (b) Was bei `sudo apt install ./werkzeug_1.4_amd64.deb`? (c) Was bei `sudo apt install werkzeug_1.4_amd64.deb` ohne `./`?

:::loesung
(a) `dpkg` packt das Paket aus, bemerkt die fehlende Abhängigkeit und richtet es nicht ein: Es meldet ein Abhängigkeitsproblem und lässt das Paket im Zustand „ausgepackt“ (`iU` in `dpkg -l`). Reparieren lässt sich das mit `sudo apt --fix-broken install`, das `libonig5` nachinstalliert oder das Paket wieder entfernt.

(b) `apt` erkennt am Schrägstrich, dass eine Datei gemeint ist, liest ihre Beschreibung, holt `libonig5` aus den Paketquellen und installiert beides. Die Simulation mit `hello` zeigt, wie `apt` eine solche Datei kennzeichnet:

```console
$ apt -s install ./hello_2.10-5build1_amd64.deb | grep -E '^(Inst|Conf)'

WARNING: apt does not have a stable CLI interface. Use with caution in scripts.

Installing:
Inst hello (2.10-5build1 Ubuntu:26.04/resolute, local-deb [amd64])
Conf hello (2.10-5build1 Ubuntu:26.04/resolute, local-deb [amd64])
```

(c) Ohne Schrägstrich sucht `apt` ein Paket dieses Namens in den Listen und findet keins:

```console
$ apt -s install hello_2.10-5build1_amd64.deb | tail -n 3

WARNING: apt does not have a stable CLI interface. Use with caution in scripts.

Error: Unable to locate package hello_2.10-5build1_amd64.deb
Reading package lists...
Building dependency tree...
Reading state information...
```

Die Fehlermeldung steht vor den Fortschrittszeilen, weil sie auf der Standardfehlerausgabe sofort im Terminal erscheint, während `tail` die Standardausgabe erst am Ende ausgibt.
:::
:::

:::aufgabe Aufgabe 32 ★★ Eine Lücke in einer Bibliothek
<span class="anker" id="aufg-32"></span>

In einer weit verbreiteten Bibliothek wird eine Lücke bekannt. Auf einem Rechner benutzen sie zwei Programme aus den Paketquellen von Ubuntu und zwei Programme, die als Snap installiert sind. (a) Wie viele Updates braucht es, bis alle vier geschützt sind, und von wem müssen sie kommen? (b) Was muss nach den Updates noch geschehen, damit die laufenden Programme geschützt sind?

:::loesung
(a) Drei Updates. Ein einziges Update des Bibliothekspakets von Ubuntu schützt beide Programme aus den Paketquellen, weil sie dieselbe Bibliothek teilen. Jeder der beiden Snaps enthält eine eigene Kopie der Bibliothek und braucht ein eigenes Update von seinem Hersteller. Wie schnell die kommen, hängt an den Herstellern, nicht an Ubuntu.

(b) Die Programme, die schon liefen, müssen neu gestartet werden, sonst benutzen sie weiter die alte Fassung (Unterabschnitt [8.3](aktualisieren-als-schutz.html#stufe-8-3)).
:::
:::

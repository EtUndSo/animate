---
title: Pakete und ihre Beziehungen
pfad: Informatik / Linux und Kommandozeile / Software installieren: Paketverwaltung
adresse: informatik/linux-und-kommandozeile/software-installieren-paketverwaltung
knoten: Kapitel 9: Software installieren: Paketverwaltung
order: 6140200
summary: Unter Linux kommt Software in Paketen.
tags: Archivdatei, Paket, Paketbetreuer, Paketbeschreibung, Paketversion, Architektur, hängt, ab
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Unter Linux kommt Software in Paketen. Dieser Abschnitt erklärt, was in einem Paket steckt, wie man seine Version liest und wie Pakete voneinander abhängen, einander empfehlen oder einander ausschließen. Noch tippst du dabei keinen neuen Befehl.
:::

:::::vorwissen Was du dafür brauchst: Distribution, Verzeichnisse, Bibliotheken und root

<span class="anker" id="stufe-1-1"></span>

Dieses Kapitel setzt die [Kapitel 1](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/ein-linux-zum-ueben.html) bis 8 voraus. Daraus brauchst du vor allem diese Dinge.

<ul>

<li>

Eine Distribution ist ein vollständiges Betriebssystem aus Kernel, Werkzeugen, Programmen und Voreinstellungen, das ein Hersteller oder eine Gemeinschaft als Ganzes pflegt. Zu jeder Distribution gehört eine Paketverwaltung; [Kapitel 1](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/ein-linux-zum-ueben.html) hat sie nur beim Namen genannt ([Kapitel 1, Abschnitt 1.6](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/betriebssystem-kernel-und-distribution.html#stufe-1-6)).

</li>

<li>

Programme liegen in `/usr/bin`, Bibliotheken in `/usr/lib`, Handbuchseiten und Anleitungen in `/usr/share`, Einstellungen in `/etc` und veränderliche Daten wie Protokolle in `/var`. Eine Bibliothek ist eine Datei mit Programmteilen, die viele Programme gemeinsam benutzen ([Kapitel 3, Abschnitte 7.2](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/die-verzeichnisstruktur-von-linux.html#stufe-7-2), 7.3 und 7.5).

</li>

<li>

Ein symbolischer Link ist eine kleine Datei, die nur einen Pfad enthält; wer ihn öffnet, landet bei der Datei, auf die er zeigt ([Kapitel 3, Abschnitt 8.5](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/inode-und-links.html#stufe-8-5)).

</li>

<li>

Die Verzeichnisse unter `/usr` und `/etc` gehören `root` und dürfen nur von `root` verändert werden. `sudo befehl` führt einen einzelnen Befehl als `root` aus ([Kapitel 7, Abschnitte 1.7](/wissen/informatik/linux-und-kommandozeile/benutzer-gruppen-und-rechte/benutzer-und-gruppen.html#stufe-1-7) und [6.1](/wissen/informatik/linux-und-kommandozeile/benutzer-gruppen-und-rechte/kurzzeitig-root-sudo-und-su.html#stufe-6-1)).

</li>

<li>

Mit Pipes, `grep`, `head` und `wc -l` filterst und zählst du die Ausgaben langer Befehle ([Kapitel 4, Abschnitt 4.1](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/pipes-und-filter.html#stufe-4-1); [Kapitel 6, Abschnitte 1.5](/wissen/informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke/textdaten-datensatze-felder-und-zeilenenden.html#stufe-1-5) und [5.2](/wissen/informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke/suchen-mit-grep.html#stufe-5-2)).

</li>

</ul>

Neu ist ein Wort, das du von Windows kennst. Viele Dateien lassen sich zu einer einzigen Datei zusammenpacken, die ihre Namen und Verzeichnisse mitführt und aus der man sie später wieder auspacken kann. Eine solche Datei heißt __Archivdatei__; eine ZIP-Datei ist ein Beispiel dafür.

⁠**Kurz gesagt:** Du brauchst die Verzeichnisse `/usr`, `/etc` und `/var`, den Begriff Bibliothek, `sudo` und das Filtern mit Pipes; eine Archivdatei verpackt viele Dateien in eine.

:::warnung Was dieses Kapitel an deinem System verändert
Die meisten Befehle in diesem Kapitel lesen nur. Wo ein Befehl Software installieren oder entfernen würde, zeigt das Kapitel zuerst eine Simulation, die nichts verändert. Echt verändert werden nur drei Dinge, und jedes Mal steht vorher ein Kasten wie dieser: die Paketlisten deines Systems, das kleine Übungspaket `hello`, das du einmal installierst und wieder vollständig entfernst, und Dateien in einem eigenen Übungsverzeichnis, das du jetzt anlegst:

```console
$ mkdir ~/linuxk9
$ cd ~/linuxk9
```

Befehle mit `--allow-remove-essential`, `--force` oder dem Wort `purge` vor einem Paket, das du nicht selbst installiert hast, tippst du nie ab.
:::

:::::

### Das Paket

<span class="anker" id="stufe-1-2"></span>

Ein Programm ist selten eine einzige Datei. Schon das kleine Übungsprogramm `hello`, das nur einen Gruß ausgibt, besteht aus sechs Dateien in vier Verzeichnissen: dem Programm selbst, einer Handbuchseite, einer Anleitung und drei Textdateien mit Lizenz und Änderungsliste. Große Programme bringen Hunderte Dateien mit, dazu Einstellungen unter `/etc`. Wer installiert sie an die richtige Stelle, und wer weiß später noch, welche Datei zu welchem Programm gehört?

Ein Bild zur Orientierung: ein Möbelstück zum Selbstaufbauen. Im Karton liegen die Teile, außen klebt ein Etikett mit Name, Ausführung und dem Hinweis, was man zusätzlich braucht, und innen liegt eine Aufbauanleitung. Das Bild hat eine Grenze: Beim Paket arbeitet nicht ein Mensch die Anleitung ab, sondern der Rechner, und zwar mit den Rechten von `root`.

:::definition Definition 1.1 (Paket)
<span class="anker" id="satz-1-1"></span>

Ein __Paket__ ist eine Archivdatei mit den Dateien eines Programms, einer Bibliothek oder einer Sammlung von Daten, jede mit ihrem Platz im Verzeichnisbaum. Dazu enthält es eine Beschreibung seiner selbst und, wenn nötig, kleine Programme, die beim Installieren und Entfernen laufen. Unter Debian und Ubuntu endet die Datei eines Pakets auf `.deb`.
:::

Man unterscheidet den *Namen* eines Pakets, etwa `hello`, von der *Paketdatei*, etwa `hello_2.10-5build1_amd64.deb`. Den Namen benutzt man in fast allen Befehlen; die Datei liegt auf einem Server oder nach dem Herunterladen auf der Platte. Abbildung [1](#abb-1) zeigt die drei Bestandteile.

:::abbildung linux/k9paket 1
Ein Paket als Karton mit drei Fächern. Links die Dateien mit ihren Zielorten (`usr/bin/hello`, `usr/share/man/man1/hello.1.gz` und weitere), in der Mitte das Etikett mit Name, Version, Architektur und „braucht: libc6“, rechts das Fach für Skripte, das bei `hello` leer ist. Darunter der Verzeichnisbaum des Systems; beim Installieren wandern die Dateien an ihre Plätze, das Etikett wandert in eine Liste „installierte Pakete“.
:::

::::beispiel Was im Paket hello steckt
Das Paket `hello` enthält diese sechs Dateien:

<ul>

<li>

`/usr/bin/hello`, das Programm (26 936 Byte);

</li>

<li>

`/usr/share/man/man1/hello.1.gz`, die Handbuchseite;

</li>

<li>

`/usr/share/info/hello.info.gz`, eine längere Anleitung;

</li>

<li>

`/usr/share/doc/hello/copyright`, `NEWS.gz` und `changelog.Debian.gz`, Lizenz und Änderungslisten.

</li>

</ul>

Die Paketdatei selbst ist mit 26 068 Byte kleiner als das Programm allein, weil die Archivdatei ihren Inhalt komprimiert speichert.
::::

⁠**Kurz gesagt:** Ein Paket ist eine Archivdatei mit allen Dateien einer Software samt Zielort, einer Beschreibung und gegebenenfalls Skripten für das Installieren und Entfernen.

:::hintergrund Wer die Pakete baut
Die meisten Programme schreibt nicht die Distribution selbst, sondern ein eigenständiges Projekt, etwa das GNU-Projekt bei `hello` und `grep`. Ein __Paketbetreuer__ der Distribution holt sich den Quelltext, übersetzt ihn, legt fest, welche Datei wohin gehört, schreibt die Beschreibung und die Skripte und passt das Programm wenn nötig an die Distribution an. Ubuntu übernimmt die meisten Pakete von Debian und baut sie neu; in der Beschreibung steht dann neben dem Betreuer bei Ubuntu ein Feld `Original-Maintainer` mit dem Betreuer bei Debian. Erst dieser Zwischenschritt macht aus vielen einzelnen Programmen ein Betriebssystem, dessen Teile zueinander passen.
:::

:::hintergrund Pakete anderer Distributionen
Das Format `.deb` stammt von Debian und gilt für alle Distributionen, die von Debian abstammen, etwa Ubuntu, Linux Mint, Raspberry Pi OS und Kali. Die zweite große Familie benutzt Pakete mit der Endung `.rpm`, ursprünglich von Red Hat: Fedora, Red Hat Enterprise Linux und openSUSE. Daneben gibt es eigene Formate, etwa bei Arch Linux. Ein Paket der einen Familie lässt sich nicht einfach in der anderen installieren, denn Beschreibung, Skripte und Ablageorte folgen anderen Regeln. Die Ideen dieses Kapitels gelten aber für alle; nur die Befehle heißen anders.
:::

### Die Paketbeschreibung

<span class="anker" id="stufe-1-3"></span>

Bevor der Rechner ein Paket installiert, muss er wissen, wie es heißt, welche Version es ist, für welche Art von Prozessor es gebaut wurde und was es außer sich selbst braucht. Diese Angaben stehen nicht in den Dateien des Programms, sondern in einem eigenen Teil des Pakets.

:::definition Definition 1.2 (Paketbeschreibung)
<span class="anker" id="satz-1-2"></span>

Die __Paketbeschreibung__ ist eine kleine Textdatei im Paket mit Zeilen der Form `Feld: Wert`. Pflichtfelder sind unter anderem der Name (`Package`), die Version (`Version`), die Architektur (`Architecture`), der Betreuer (`Maintainer`) und ein Beschreibungstext (`Description`). Weitere Felder nennen den Platzbedarf, die Beziehungen zu anderen Paketen und eine Webseite.
:::

Angaben über Daten nennt man allgemein Metadaten; die Paketbeschreibung enthält die Metadaten eines Pakets.

::::beispiel Die Beschreibung des Pakets hello
So sieht die Beschreibung von `hello` aus:

```text
Package: hello
Version: 2.10-5build1
Architecture: amd64
Maintainer: Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>
Original-Maintainer: Santiago Vila <sanvila@debian.org>
Installed-Size: 104
Depends: libc6 (>= 2.38)
Conflicts: hello-traditional
Breaks: hello-debhelper (<< 2.9)
Replaces: hello-debhelper (<< 2.9), hello-traditional
Section: devel
Priority: optional
Homepage: https://www.gnu.org/software/hello/
Description: example package based on GNU hello
 The GNU hello program produces a familiar, friendly greeting.  It
 allows non-programmers to use a classic computer science tool which
 would otherwise be unavailable to them.
 .
 Seriously, though: this is an example of how to do a Debian package.
 It is the Debian version of the GNU Project's `hello world' program
 (which is itself an example for the GNU Project).
```

`Installed-Size` ist der Platz, den das Paket nach dem Installieren belegt, in KiB: $104 \cdot 1024 = 106\,496$ Byte. `Section` ordnet das Paket einem Sachgebiet zu, `Priority` sagt, wie wichtig es für ein lauffähiges System ist; `optional` heißt: entbehrlich. Die erste Zeile von `Description` ist eine Kurzbeschreibung, die eingerückten Zeilen danach sind der lange Text; eine Zeile mit einem einzelnen Punkt steht dort für eine Leerzeile. Die Felder `Depends`, `Conflicts`, `Breaks` und `Replaces` beschreiben Beziehungen zu anderen Paketen; sie sind das Thema der folgenden Unterabschnitte.
::::

⁠**Kurz gesagt:** Die Paketbeschreibung ist eine Textdatei im Paket mit Zeilen `Feld: Wert`, unter anderem Name, Version, Architektur, Platzbedarf, Beziehungen zu anderen Paketen und ein Beschreibungstext.

### Version und Architektur

<span class="anker" id="stufe-1-4"></span>

Von einem Paket gibt es im Lauf der Zeit viele Fassungen. Die Paketverwaltung muss entscheiden können, welche neuer ist, und sie muss wissen, ob ein Paket überhaupt auf diesem Rechner läuft. Beides steht im Namen der Paketdatei und in der Beschreibung.

:::definition Definition 1.3 (Paketversion)
<span class="anker" id="satz-1-3"></span>

Die __Paketversion__ hat die Form `[Epoche:]Programmversion[-Revision]`. Die *Programmversion* ist die Versionsnummer, die das Projekt seinem Programm gibt. Die *Revision* zählt, wie oft die Distribution dieses Programm in dieser Version neu verpackt hat. Die *Epoche* ist eine kleine ganze Zahl mit Doppelpunkt; sie fehlt meist und wird nur gesetzt, wenn sich die Zählweise der Programmversion geändert hat.
:::

In der Revision steckt bei Ubuntu oft mehr als eine Zahl. `ubuntu3` heißt: Ubuntu hat das Debian-Paket dreimal selbst verändert. `build1` heißt: Ubuntu hat es unverändert neu übersetzt. Eine Tilde `~` kennzeichnet eine Fassung, die als etwas *älter* gelten soll als dieselbe Nummer ohne Tilde; Ubuntu benutzt das für Pakete, die es nachträglich für eine schon erschienene Version bereitstellt. Abbildung [2](#abb-2) zerlegt eine Version in ihre Teile.

:::abbildung linux/k9version 2
Die Version `1:2.41.3-3ubuntu2.2` groß geschrieben und in drei farbige Abschnitte zerlegt: Epoche `1` („Zählweise geändert“), Programmversion `2.41.3` („vom Projekt“), Revision `3ubuntu2.2` („von der Distribution“). Die Revision klappt weiter auf: `3` von Debian, `ubuntu2` zwei Änderungen durch Ubuntu, `.2` zwei spätere Korrekturen. Darunter ein Zahlenstrahl der Reihenfolge: `0.10.0-1ubuntu2~26.04.1` steht knapp links von `0.10.0-1ubuntu2`, die Tilde als kleiner Pfeil nach links.
:::

Die __Architektur__ eines Pakets gibt an, für welche Art von Prozessor es gebaut ist. `amd64` steht für die üblichen 64-Bit-Prozessoren von PCs, `arm64` für 64-Bit-ARM-Prozessoren, etwa im Raspberry Pi. Pakete mit der Architektur `all` enthalten nur Skripte, Texte oder Daten und laufen überall.

::::beispiel [Beispiele] Versionen lesen
Die folgenden Versionen kommen in diesem Kapitel vor:

<ul>

<li>

`hello 2.10-5build1`: Programmversion 2.10 von GNU hello, fünfte Debian-Revision, von Ubuntu einmal unverändert neu übersetzt.

</li>

<li>

`sudo 1.9.17p2-1ubuntu3`: Programmversion 1.9.17p2, erste Debian-Revision, dreimal von Ubuntu verändert.

</li>

<li>

`fortune-mod 1:1.99.1-9.2`: Epoche 1, Programmversion 1.99.1, Revision 9.2.

</li>

<li>

`rust-coreutils 0.10.0-1ubuntu2~26.04.1`: Programmversion 0.10.0, eine für Ubuntu 26.04 nachgereichte Fassung; sie gilt als etwas älter als `0.10.0-1ubuntu2` ohne Tilde.

</li>

</ul>

Die Paketdatei heißt `Name_Version_Architektur.deb`, also `hello_2.10-5build1_amd64.deb`.
::::

⁠**Kurz gesagt:** Eine Paketversion besteht aus Epoche, Programmversion und Revision der Distribution; die Architektur sagt, auf welchem Prozessor das Paket läuft, `all` heißt überall.

:::hintergrund Wie die Paketverwaltung zwei Versionen vergleicht
Versionen werden nicht wie Text verglichen. Zuerst entscheidet die Epoche: Jede Version mit Epoche 1 ist neuer als jede ohne, deshalb ist `1:1.99.1` neuer als `2.0`. Danach werden Programmversion und Revision von links nach rechts in Stücke zerlegt, abwechselnd Ziffernfolgen und andere Zeichen. Ziffernfolgen vergleicht die Paketverwaltung als Zahlen: `2.10` ist neuer als `2.9`, weil 10 größer ist als 9, obwohl das Zeichen `1` vor dem Zeichen `9` käme. Bei den übrigen Zeichen kommen Buchstaben vor Satzzeichen, und die Tilde kommt vor allem anderen, sogar vor dem Ende der Version. Deshalb ist `0.10.0-1ubuntu2~26.04.1` älter als `0.10.0-1ubuntu2`. Die Epoche gibt es, weil manche Projekte ihre Zählung umstellen, etwa von Datumsversionen wie `2023.11` auf `1.0`; ohne Epoche hielte die Paketverwaltung die neue Fassung für älter und würde sie nie installieren.
:::

### Die Abhängigkeit

<span class="anker" id="stufe-1-5"></span>

Kaum ein Programm arbeitet allein. Fast alle benutzen Bibliotheken, die andere Pakete bereitstellen, und viele rufen andere Programme auf. Ein Paket muss also sagen können: Ohne dieses andere Paket funktioniere ich nicht.

Das Bild vom Möbelkarton hilft wieder: Auf dem Etikett steht „Sie benötigen zusätzlich: einen Akkuschrauber“. Hat man schon einen, kauft man keinen zweiten.

:::definition Definition 1.4 (Abhängigkeit)
<span class="anker" id="satz-1-4"></span>

Ein Paket A __hängt__ von einem Paket B __ab__, wenn A ohne B nicht funktioniert. A nennt B in seiner Beschreibung im Feld `Depends`, wenn nötig mit einer Bedingung an die Version, etwa `libc6 (>= 2.38)`: Version 2.38 oder neuer. Die Paketverwaltung installiert ein Paket nur zusammen mit allen Paketen, von denen es abhängt, und mit deren Abhängigkeiten, soweit sie noch fehlen. Diesen Schritt nennt man *Auflösen* der Abhängigkeiten.
:::

Die Zeichen in einer Bedingung lauten `>=` (mindestens), `<=` (höchstens), `=` (genau), `>>` (echt neuer) und `<<` (echt älter).

::::beispiel Die Abhängigkeiten von jq
Das Programm `jq` durchsucht und formt Daten im Textformat JSON, in dem viele Webdienste ihre Antworten liefern. Seine Beschreibung enthält die Zeile

```text
Depends: libjq1 (= 1.8.1-4ubuntu2), libc6 (>= 2.38), libonig5 (>= 6.8.1)
```

`libjq1` ist die Bibliothek, die die eigentliche Arbeit macht, und muss genau dieselbe Version haben. `libonig5` ist eine Bibliothek für Suchmuster, `libc6` die C-Bibliothek, die fast jedes Programm unter Linux braucht. `libjq1` hängt ihrerseits von `libc6` und `libonig5` ab, `libonig5` von `libc6`. Auf dem Testsystem ist `libc6` schon installiert. Wer `jq` installieren will, bekommt also drei neue Pakete: `jq`, `libjq1` und `libonig5`. Abbildung [3](#abb-3) zeigt den Graphen; `libonig5` kommt darin auf zwei Wegen vor, wird aber nur einmal installiert.
::::

:::abbildung linux/k9abhaengigkeit 3
Abhängigkeitsgraph von `jq`. Oben `jq`, darunter `libjq1` und `libonig5`, ganz unten `libc6`; Pfeile von `jq` zu allen drei, von `libjq1` zu `libonig5` und `libc6`, von `libonig5` zu `libc6`. Unter `libc6` hängen grau `libgcc-s1` (mit `gcc-16-base` darunter) und `libc-gconv-modules-extra`. Bereits installierte Pakete sind grün umrandet, die drei neuen orange; ein Zähler „neu zu installieren: 3“.
:::

⁠**Kurz gesagt:** Eine Abhängigkeit sagt, welche anderen Pakete ein Paket braucht; die Paketverwaltung installiert alle fehlenden mit, auch die Abhängigkeiten der Abhängigkeiten, aber jedes nur einmal.

:::hintergrund Warum Programme ihre Bibliotheken teilen
Man könnte jedem Programm alle Bibliotheken fest einbauen; dann bräuchte es keine Abhängigkeiten. Linux-Distributionen teilen die Bibliotheken aus zwei Gründen. Erstens liegt eine Bibliothek, die Hunderte Programme benutzen, nur einmal auf der Platte und, wenn sie läuft, oft nur einmal im Arbeitsspeicher. Zweitens, und das ist der wichtigere Grund: Findet jemand einen Fehler in der Bibliothek, etwa eine Sicherheitslücke, genügt es, dieses eine Paket zu aktualisieren, und alle Programme, die es benutzen, sind auf einen Schlag repariert. Auf dem Testsystem hängen 422 installierte Pakete von `libc6` ab. Der Preis dafür sind die Abhängigkeiten, die jemand verwalten muss. Bevor es Paketverwaltungen gab, suchte man fehlende Bibliotheken von Hand zusammen und stieß oft auf zwei Programme, die verschiedene, unverträgliche Fassungen derselben Bibliothek verlangten. Das nannte man scherzhaft die Abhängigkeitshölle.
:::

### Empfehlung und Vorschlag

<span class="anker" id="stufe-1-6"></span>

Nicht jede Beziehung ist so streng wie eine Abhängigkeit. Ein Programm kann ohne ein anderes Paket laufen, aber kaum sinnvoll sein; oder es kann ein Zusatzpaket gut gebrauchen, das aber nicht jeder will.

:::definition Definition 1.5 (Empfehlung, Vorschlag)
<span class="anker" id="satz-1-5"></span>

Eine __Empfehlung__ (Feld `Recommends`) nennt ein Paket, das fast alle Benutzer zusammen mit diesem Paket haben wollen. Ubuntu installiert Empfehlungen in der Voreinstellung mit. Ein __Vorschlag__ (Feld `Suggests`) nennt ein Paket, das nützlich sein kann; die Paketverwaltung zeigt Vorschläge nur an und installiert sie nicht.
:::

Daneben gibt es eine strengere Form der Abhängigkeit, `Pre-Depends`. Ein Paket mit diesem Feld darf erst ausgepackt werden, wenn das andere Paket schon vollständig installiert und eingerichtet ist. `grep` hat zum Beispiel ein `Pre-Depends` auf `libc6`: Die Skripte vieler anderer Pakete rufen `grep` auf, auch mitten in einer Installation, und `grep` muss deshalb in jedem Augenblick laufen können.

::::beispiel fortune und seine Sprüche
Das Programm `fortune` aus dem Paket `fortune-mod` gibt einen zufälligen Spruch aus. Es hängt von `libc6` und der Bibliothek `librecode3` ab. Die Sprüche selbst stehen in einem eigenen Paket: `fortune-mod` empfiehlt `fortunes-min`, eine kleine Sammlung, und schlägt `fortunes` vor, eine große. Ohne irgendeine Sammlung hätte `fortune` nichts zu sagen; deshalb ist `fortunes-min` eine Empfehlung und kein bloßer Vorschlag. Eine Abhängigkeit ist es auch nicht, denn statt der kleinen Sammlung genügt ebenso jede andere. Wer `fortune-mod` installiert, bekommt deshalb drei neue Pakete: `fortune-mod`, `librecode3` und `fortunes-min`.
::::

:::abbildung linux/k9beziehungen 4
Die Beziehungen von `fortune-mod` als Graph mit drei Pfeilarten. Durchgezogen (`Depends`) zu `libc6` und `librecode3`, gestrichelt (`Recommends`) zu `fortunes-min`, gepunktet (`Suggests`) zu `fortunes`, `x11-utils` und `bsdextrautils`. Ein Schalter „Empfehlungen mitinstallieren: an“; die installierten Pakete werden grün (`fortune-mod`, `librecode3`, `fortunes-min`, `libc6` war schon da), die Vorschläge bleiben grau. Der Schalter springt auf „aus“, `fortunes-min` wird grau, und der Zähler der neu installierten Pakete fällt von 3 auf 2.
:::

Abbildung [4](#abb-4) zeigt die drei Arten von Pfeilen im Graphen von `fortune-mod`.

⁠**Kurz gesagt:** Empfehlungen installiert Ubuntu mit, Vorschläge nur auf Wunsch; `Pre-Depends` verlangt, dass das andere Paket schon vor dem Auspacken fertig eingerichtet ist.

### Der Konflikt

<span class="anker" id="stufe-1-7"></span>

Manche Pakete vertragen sich nicht. Zwei Pakete, die beide eine Datei `/usr/bin/hello` mitbringen, können nicht gleichzeitig installiert sein, denn ein Pfad kann nur zu einer Datei führen. Ein Paket muss also auch sagen können: Mit diesem anderen Paket zusammen funktioniere ich nicht.

:::definition Definition 1.6 (Konflikt)
<span class="anker" id="satz-1-6"></span>

Ein __Konflikt__ (Feld `Conflicts`) nennt Pakete, die nicht gleichzeitig mit diesem Paket installiert sein dürfen. Will man das eine installieren, muss die Paketverwaltung das andere vorher entfernen.
:::

Zwei verwandte Felder sind schwächer. `Breaks` sagt: Das andere Paket funktioniert in den genannten Versionen nicht mehr, wenn dieses Paket installiert ist; es muss aktualisiert oder entfernt werden. `Replaces` erlaubt diesem Paket, Dateien des anderen zu überschreiben, etwa weil eine Datei von einem Paket in ein anderes umgezogen ist. Ohne diese Erlaubnis bricht die Paketverwaltung ab, sobald zwei Pakete dieselbe Datei beanspruchen.

::::beispiel hello und hello-traditional
In der Beschreibung von `hello` stehen die Zeilen `Conflicts: hello-traditional` und `Replaces: hello-debhelper (<< 2.9), hello-traditional`. Früher gab es eine zweite Fassung des Programms im Paket `hello-traditional`, die ebenfalls `/usr/bin/hello` mitbrachte. Beide zusammen gehen nicht; installiert man `hello`, muss `hello-traditional` weichen, und `hello` darf dessen Dateien übernehmen.
::::

⁠**Kurz gesagt:** Ein Konflikt schließt zwei Pakete gegenseitig aus; `Breaks` betrifft nur bestimmte Versionen, `Replaces` erlaubt das Überschreiben fremder Dateien.

### Das virtuelle Paket

<span class="anker" id="stufe-1-8"></span>

Für manche Aufgaben gibt es mehrere gleichwertige Programme. Ein Paket, das irgendein Programm der Sprache `awk` braucht ([Kapitel 6, Abschnitt 9](/wissen/informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke/rechnen-mit-spalten-awk.html#stufe-9)), ist mit `gawk` genauso zufrieden wie mit `mawk`. Es soll deshalb nicht ein bestimmtes Paket verlangen, sondern eine Fähigkeit.

:::definition Definition 1.7 (Virtuelles Paket)
<span class="anker" id="satz-1-7"></span>

Ein __virtuelles Paket__ ist ein Paketname, zu dem es keine eigene Paketdatei gibt. Echte Pakete erklären mit dem Feld `Provides`, dass sie diesen Namen erfüllen. Eine Abhängigkeit von einem virtuellen Paket ist erfüllt, sobald irgendein Paket installiert ist, das ihn erfüllt.
:::

Zusammen mit einem Konflikt bekommt das virtuelle Paket eine zweite Aufgabe: Erfüllen mehrere Pakete denselben Namen und steht er zugleich in ihrem `Conflicts`, dann kann immer nur eines von ihnen installiert sein. Ein Beispiel sind Mailserver, also Programme, die E-Mails von anderen Rechnern annehmen und weiterleiten. Die beiden Mailserver `postfix` und `exim4-daemon-light` erfüllen den Namen `mail-transport-agent` und stehen beide mit ihm in Konflikt. Auf einem Rechner ist deshalb immer höchstens einer von ihnen installiert; zwei würden sich um dieselbe Aufgabe streiten, die ankommenden E-Mails anzunehmen.

::::beispiel Wer awk sein darf
Die Pakete `gawk` und `mawk` enthalten beide die Zeile `Provides: awk`. Ein Paket mit `Depends: awk` ist zufrieden, wenn eines von beiden installiert ist; welches, entscheidet der Verwalter des Rechners. Auf dem Testsystem sind sogar beide installiert, denn sie schließen einander nicht aus.
::::

:::abbildung linux/k9virtuell 5
Links der virtuelle Name `awk` als gestrichelter Rahmen ohne eigene Datei; `gawk` und `mawk`, beide installiert, stecken mit Pfeilen „Provides: awk“ darin. Ein Paket mit `Depends: awk` zeigt auf den Rahmen und ist zufrieden, sobald eines der beiden grün ist. Rechts ein zweiter Rahmen `mail-transport-agent` mit dem Schild „Conflicts“: Er hat nur Platz für ein Paket; `postfix` steckt darin, `exim4-daemon-light` wartet davor; ein Versuch hineinzukommen scheitert am Schild (rotes Kreuz), solange `postfix` darin steckt.
:::

Abbildung [5](#abb-5) stellt beide Fälle gegenüber: einen virtuellen Namen, den mehrere Pakete zugleich erfüllen dürfen, und einen mit Konflikt, der nur eines zulässt.

⁠**Kurz gesagt:** Ein virtuelles Paket ist ein Name für eine Fähigkeit, den echte Pakete mit `Provides` erfüllen; mit einem Konflikt auf diesen Namen ist immer nur eines von ihnen installiert.

### Aufgaben zu Abschnitt [1](#stufe-1)

<span class="anker" id="stufe-1-9"></span>

:::aufgabe Aufgabe 1 ★ Einen Dateinamen lesen
<span class="anker" id="aufg-1"></span>

Im Zwischenspeicher der Paketverwaltung liegt die Datei `bsdutils_1%3a2.41.3-3ubuntu2.2_amd64.deb`. Die Zeichenfolge `%3a` steht in Dateinamen für einen Doppelpunkt. (a) Wie heißt das Paket, und welche Architektur hat es? (b) Zerlege die Version in Epoche, Programmversion und Revision. (c) Was sagt die Revision über die Arbeit von Debian und Ubuntu an diesem Paket?

:::loesung
(a) Der Name steht vor dem ersten Unterstrich, die Architektur vor `.deb`: Paket `bsdutils`, Architektur `amd64`.

(b) Zwischen den beiden Unterstrichen steht die Version `1:2.41.3-3ubuntu2.2`, nachdem man `%3a` durch einen Doppelpunkt ersetzt hat. Vor dem Doppelpunkt steht die Epoche 1. Die Programmversion reicht bis zum letzten Bindestrich: `2.41.3`. Danach kommt die Revision `3ubuntu2.2`.

(c) Debian hat das Programm in dieser Version dreimal verpackt (`3`), Ubuntu hat dieses Paket zweimal selbst verändert (`ubuntu2`), und danach kamen zwei weitere Korrekturen dazu (`.2`). Solche angehängten Nummern sind typisch für Updates nach dem Erscheinen einer Version. Die Epoche zeigt, dass Debian die Zählweise der Versionen dieses Pakets irgendwann umgestellt hat.
:::
:::

:::aufgabe Aufgabe 2 ★★ Welche Version ist neuer?
<span class="anker" id="aufg-2"></span>

Entscheide mit den Regeln aus dem Hintergrund in Unterabschnitt [1.4](#stufe-1-4) und begründe: (a) `2.10-1` oder `2.9-7`; (b) `0.2.13-0ubuntu1` oder `0.2.13-0ubuntu1.2`; (c) `9.7-3ubuntu2` oder `9.7-3ubuntu2~26.04.1`; (d) `1:1.0` oder `2026.11`.

:::loesung
(a) `2.10-1` ist neuer. Die Programmversionen werden in Stücke zerlegt: `2`, `.`, `10` gegen `2`, `.`, `9`. Ziffernfolgen werden als Zahlen verglichen, und 10 ist größer als 9. Die Revision zählt erst, wenn die Programmversionen gleich sind.

(b) `0.2.13-0ubuntu1.2` ist neuer. Bis `0ubuntu1` sind beide gleich; dann endet die eine Version, während die andere mit `.2` weitergeht. Jedes Zeichen außer der Tilde ist größer als das Ende.

(c) `9.7-3ubuntu2` ist neuer. Bis `3ubuntu2` sind beide gleich; dann kommt bei der zweiten eine Tilde, die vor allem anderen kommt, sogar vor dem Ende.

(d) `1:1.0` ist neuer, denn es hat die Epoche 1 und `2026.11` die Epoche 0. Die Epoche entscheidet vor allem anderen.

Nachprüfen lässt sich das mit `dpkg --compare-versions`, das mit dem Exit-Status 0 antwortet, wenn der Vergleich stimmt; `&&` gibt dann das Wort aus ([Kapitel 4, Abschnitt 6.2](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/befehle-verketten.html#stufe-6-2)):

```console
$ dpkg --compare-versions 2.10-1 gt 2.9-7 && echo neuer
neuer
$ dpkg --compare-versions 0.2.13-0ubuntu1.2 gt 0.2.13-0ubuntu1 && echo neuer
neuer
$ dpkg --compare-versions 9.7-3ubuntu2~26.04.1 lt 9.7-3ubuntu2 && echo aelter
aelter
$ dpkg --compare-versions 1:1.0 gt 2026.11 && echo neuer
neuer
```

`gt` heißt „größer als“, also neuer, `lt` „kleiner als“, also älter.
:::
:::

:::aufgabe Aufgabe 3 ★★ Abhängigkeiten auflösen
<span class="anker" id="aufg-3"></span>

Ein Paket `zeichner` hat `Depends: libbild, libtext`. `libbild` hat `Depends: libfarbe, libc6`, `libtext` hat `Depends: libc6` und `Recommends: schriften`, `libfarbe` hat `Depends: libc6` und `Suggests: farbtabellen`. Installiert ist nur `libc6`. (a) Zeichne den Abhängigkeitsgraphen. (b) Welche Pakete installiert die Paketverwaltung mit den Voreinstellungen von Ubuntu, wenn du `zeichner` installierst? (c) Was ändert sich, wenn Empfehlungen abgeschaltet sind?

:::loesung
(a) Pfeile für `Depends`: `zeichner` $\to$ `libbild`, `zeichner` $\to$ `libtext`, `libbild` $\to$ `libfarbe`, `libbild` $\to$ `libc6`, `libtext` $\to$ `libc6`, `libfarbe` $\to$ `libc6`. Dazu gestrichelt `libtext` $\to$ `schriften` (Empfehlung) und gepunktet `libfarbe` $\to$ `farbtabellen` (Vorschlag).

(b) `libc6` ist schon da. Neu sind `zeichner`, `libbild`, `libtext`, `libfarbe` und, weil Ubuntu Empfehlungen mitinstalliert, `schriften`: fünf Pakete. `farbtabellen` ist nur ein Vorschlag und bleibt weg.

(c) Ohne Empfehlungen fehlt `schriften`; es kommen vier Pakete. Die Abhängigkeiten selbst lassen sich nicht abschalten, denn ohne sie liefe `zeichner` nicht.
:::
:::

:::aufgabe Aufgabe 4 ★ Beziehungen zuordnen
<span class="anker" id="aufg-4"></span>

Welches Feld (`Depends`, `Pre-Depends`, `Recommends`, `Suggests`, `Conflicts`, `Provides`) passt? (a) Ein Textprogramm bringt eine eigene Rechtschreibprüfung mit und möchte, dass meist auch ein Wörterbuch installiert wird. (b) Zwei Uhrzeitdienste stellen beide die Uhr des Rechners und dürfen nicht gleichzeitig laufen. (c) Ein Mailprogramm erfüllt den allgemeinen Namen `mail-reader`. (d) Ein Bildbetrachter kann zusätzlich Fotos drucken, wenn ein Druckpaket vorhanden ist.

:::loesung
(a) `Recommends`: Fast alle wollen das Wörterbuch, aber das Programm läuft auch ohne. (b) `Conflicts`: Beide dürfen nie gleichzeitig installiert sein. (c) `Provides: mail-reader`: Das Mailprogramm erfüllt einen virtuellen Namen. (d) `Suggests`: Drucken ist ein nützlicher Zusatz für wenige.
:::
:::

---
title: Pakete suchen und ansehen
pfad: Informatik / Linux und Kommandozeile / Software installieren: Paketverwaltung
adresse: informatik/linux-und-kommandozeile/software-installieren-paketverwaltung
knoten: Kapitel 9: Software installieren: Paketverwaltung
order: 6140500
summary: Mit aktuellen Paketlisten kann apt Fragen beantworten, ohne etwas zu verändern: Gibt es ein Paket für eine bestimmte Aufgabe?
tags: Kandidatenversion
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Mit aktuellen Paketlisten kann `apt` Fragen beantworten, ohne etwas zu verändern: Gibt es ein Paket für eine bestimmte Aufgabe? Was steht in seiner Beschreibung? Welche Version würde installiert, und was hängt davon ab? Keiner der Befehle dieses Abschnitts braucht `root`.
:::

### Suchen: apt search

<span class="anker" id="stufe-4-1"></span>

Oft weiß man, was ein Programm tun soll, aber nicht, wie das Paket heißt. Die Paketlisten enthalten Namen und Beschreibungen aller Pakete; also kann man darin suchen.

:::definition Definition 4.1 (apt search)
<span class="anker" id="satz-4-1"></span>

`apt search ausdruck` durchsucht Namen und Beschreibungen aller Pakete der Paketlisten nach einem regulären Ausdruck ([Kapitel 6, Abschnitt 6.1](/wissen/informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke/regulare-ausdrucke-zeichen-klassen-und-anker.html#stufe-6-1)) und gibt jeden Treffer mit Name, Ausgabe, Version, Architektur und Kurzbeschreibung aus. Mit der Option `--names-only` sucht es nur in den Namen.
:::

::::beispiel Ein Paket nach Name und nach Aufgabe suchen
```console
$ apt search --names-only '^hello'
hello/resolute 2.10-5build1 amd64
  example package based on GNU hello
```

Gesucht wurden Namen, die mit `hello` beginnen; es gibt genau einen. Kennt man nur die Aufgabe, sucht man in den Beschreibungen, die auf Englisch sind:

```console
$ apt search 'json processor'
jq/resolute-updates,resolute-security 1.8.1-4ubuntu2 amd64
  lightweight and flexible command-line JSON processor

libjackson-json-java/resolute 1.9.13-2 all
  streaming fast powerful standard conformant json processor in java
...
python3-jq/resolute 1.11.0-1build1 amd64
  lightweight and flexible JSON processor (Python3 version)
```

Die Suche unterscheidet nicht zwischen Groß- und Kleinschreibung. Hinter dem Namen steht, aus welchen Ausgaben die Version kommt: `jq` gibt es in einer korrigierten Fassung aus `resolute-updates` und `resolute-security`.
::::

:::abbildung linux/k9suche 16
Terminalbild mit `$ apt search 'json processor'` und den ersten zwei Treffern. Die Zeile `jq/resolute-updates,resolute-security 1.8.1-4ubuntu2 amd64` wird gerahmt, erscheint darunter vergrößert und wird nacheinander in ihre Teile zerlegt und beschriftet: Paketname, Ausgaben, aus denen die Version stammt, Version, Architektur; darunter die eingerückte Kurzbeschreibung, in der die gefundenen Wörter „JSON processor“ markiert werden, obwohl sie groß geschrieben sind.
:::

Abbildung [16](#abb-16) zerlegt eine Trefferzeile.

⁠**Kurz gesagt:** `apt search` sucht in Namen und Beschreibungen aller bekannten Pakete, `--names-only` nur in den Namen.

### Ansehen: apt show

<span class="anker" id="stufe-4-2"></span>

Hat man ein Paket gefunden, will man vor dem Installieren wissen, was es tut, wie groß es ist und was es mitbringt.

:::definition Definition 4.2 (apt show)
<span class="anker" id="satz-4-2"></span>

`apt show paket` zeigt die Beschreibung eines Pakets aus den Paketlisten, ergänzt um Angaben von `apt`: `Download-Size` (Größe der Paketdatei), `APT-Sources` (aus welcher Liste es stammt) und bei installierten Paketen `APT-Manual-Installed`.
:::

Größen gibt `apt show` in kB zu 1000 Byte an, die Paketbeschreibung in KiB zu 1024 Byte.

::::beispiel Die Angaben zu hello
```console
$ apt show hello
Package: hello
Version: 2.10-5build1
Priority: optional
Section: devel
Origin: Ubuntu
Maintainer: Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>
Original-Maintainer: Santiago Vila <sanvila@debian.org>
Bugs: https://bugs.launchpad.net/ubuntu/+filebug
Installed-Size: 106 kB
Depends: libc6 (>= 2.38)
Conflicts: hello-traditional
Breaks: hello-debhelper (<< 2.9)
Replaces: hello-debhelper (<< 2.9), hello-traditional
Homepage: https://www.gnu.org/software/hello/
Download-Size: 26.1 kB
APT-Sources: http://archive.ubuntu.com/ubuntu resolute/main amd64 Packages
Description: example package based on GNU hello
...
```

Die `104` KiB aus der Paketbeschreibung sind $104 \cdot 1024 = 106\,496$ Byte, also rund 106 kB. Die Paketdatei ist 26 068 Byte groß, rund 26,1 kB. `APT-Sources` sagt: Diese Version steht in der Paketliste von `resolute`, Bereich `main`.
::::

:::abbildung linux/k9show 17
Terminalbild mit `$ apt show hello`. Drei Felder werden nacheinander gerahmt und links nummeriert; die Liste darunter erklärt sie: `Installed-Size: 106 kB` („so viel Platz nach dem Installieren, 104 KiB“), `Download-Size: 26.1 kB` („so groß ist die Paketdatei“) und `APT-Sources` („aus dieser Paketliste: resolute/main“). Zuletzt die Zeile `Depends: libc6 (>= 2.38)` mit einem kleinen grünen Haken „schon installiert“, im Terminal und in der Liste.
:::

Abbildung [17](#abb-17) hebt die Felder hervor, die `apt` selbst ergänzt.

::::beispiel Was apt in einer Pipe anders macht
Bei langen Ausgaben öffnet `apt show` den Seitenanzeiger `less` ([Kapitel 2, Abschnitt 4.4](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/hilfe-finden.html#stufe-4-4)). Schickt man die Ausgabe stattdessen in eine Pipe, warnt `apt` zuerst:

```console
$ apt show grep | head -n 18

WARNING: apt does not have a stable CLI interface. Use with caution in scripts.

Package: grep
Version: 3.12-1
Priority: required
Essential: yes
...
APT-Manual-Installed: yes
APT-Sources: http://archive.ubuntu.com/ubuntu resolute/main amd64 Packages
```

Die Warnung geht auf die Standardfehlerausgabe, deshalb erscheint sie im Terminal, obwohl die Standardausgabe in die Pipe läuft ([Kapitel 4, Abschnitt 1.6](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/prozesse-und-ihre-drei-strome.html#stufe-1-6)). Sie erinnert daran, dass sich die Ausgabe von `apt` ändern darf. `APT-Manual-Installed: yes` heißt, dass `grep` ausdrücklich installiert wurde und nicht nur als Abhängigkeit eines anderen Pakets.
::::

⁠**Kurz gesagt:** `apt show` zeigt Beschreibung, Größe und Herkunft eines Pakets; in einer Pipe warnt `apt` auf der Standardfehlerausgabe, dass seine Ausgabe nicht für Skripte gedacht ist.

### Auflisten: apt list

<span class="anker" id="stufe-4-3"></span>

Manchmal will man nicht ein Paket genau ansehen, sondern viele auf einen Blick: Welche davon sind installiert, welche nicht?

:::definition Definition 4.3 (apt list)
<span class="anker" id="satz-4-3"></span>

`apt list muster` gibt für jedes passende Paket eine Zeile mit Name, Ausgabe, Version und Architektur aus. Ist das Paket installiert, steht am Ende `[installed]`; `now` in der Liste der Ausgaben bedeutet „auf diesem Rechner installiert“. Die Option `--installed` zeigt alle installierten Pakete, `--upgradable` alle, für die es eine neuere Version gibt.
:::

::::beispiel Drei Pakete auf einen Blick
```console
$ apt list hello grep jq
grep/resolute,now 3.12-1 amd64 [installed]
hello/resolute 2.10-5build1 amd64
jq/resolute-updates,resolute-security 1.8.1-4ubuntu2 amd64
```

Zählt man alle installierten Pakete mit einer Pipe, erscheint wieder die Warnung, und die Zahl ist um eins größer als in Unterabschnitt [2.3](die-paketverwaltung-und-ihre-datenbank.html#stufe-2-3):

```console
$ apt list --installed | wc -l

WARNING: apt does not have a stable CLI interface. Use with caution in scripts.

630
```

In einer Pipe schreibt `apt list` vor die Liste die Zeile `Listing...`; die zählt `wc -l` mit. Für solche Zählungen ist `dpkg -l | grep -c '^ii'` der verlässlichere Weg.
::::

:::abbildung linux/k9liste 18
Terminalbild mit `$ apt list hello grep jq`; darunter zwei der Zeilen vergrößert: `grep/resolute,now 3.12-1 amd64 [installed]` und `hello/resolute 2.10-5build1 amd64`. Die Teile werden beschriftet: Name, Ausgaben (`now` = „auf diesem Rechner“), Version, Architektur, Zustand. Bei `grep` leuchten `now` und `[installed]` gemeinsam auf, bei `hello` bleibt die Stelle leer. Darunter die Zählung: 629 Zeilen `ii` von `dpkg -l` gegen 630 Zeilen von `apt list --installed | wc -l`, die zusätzliche Zeile `Listing...` rot markiert.
:::

Abbildung [18](#abb-18) zerlegt die Zeilen und zeigt, woher die zusätzliche Zeile kommt.

⁠**Kurz gesagt:** `apt list` zeigt Pakete zeilenweise mit Version und Zustand; `--installed` und `--upgradable` wählen die installierten bzw. aktualisierbaren aus.

### Die Kandidatenversion: apt policy

<span class="anker" id="stufe-4-4"></span>

Von einem Paket stehen oft mehrere Versionen in den Paketlisten, etwa die vom Erscheinungstag und eine korrigierte aus `resolute-updates`. Welche davon würde `apt` installieren?

:::definition Definition 4.4 (Kandidatenversion, apt policy)
<span class="anker" id="satz-4-4"></span>

Die __Kandidatenversion__ eines Pakets ist die Version, die `apt` installieren würde. `apt` gibt jeder Quelle eine Priorität, gewöhnliche Paketquellen haben 500, die installierte Version 100. Kandidat ist die Version aus der Quelle mit der höchsten Priorität, bei gleicher Priorität die höchste Version; eine Version, die älter ist als die installierte, wird bei diesen Prioritäten nie Kandidat. `apt policy paket` zeigt die installierte Version (`Installed`), den Kandidaten (`Candidate`) und eine Tabelle aller bekannten Versionen mit ihren Quellen; drei Sterne markieren die installierte.
:::

Eine Ausnahme unter Ubuntus Ausgaben ist `resolute-backports`: Ubuntu kennzeichnet sie so, dass `apt` ihr nur die Priorität 100 gibt. Ihre neueren Programmversionen installiert `apt` deshalb nicht von selbst, sondern nur, wenn man sie ausdrücklich verlangt, etwa mit `sudo apt install paket/resolute-backports`.

::::beispiel Kein Unterschied, ein Unterschied
```console
$ apt policy hello grep
hello:
  Installed: (none)
  Candidate: 2.10-5build1
  Version table:
     2.10-5build1 500
        500 http://archive.ubuntu.com/ubuntu resolute/main amd64 Packages
grep:
  Installed: 3.12-1
  Candidate: 3.12-1
  Version table:
 *** 3.12-1 500
        500 http://archive.ubuntu.com/ubuntu resolute/main amd64 Packages
        100 /var/lib/dpkg/status
```

`hello` ist nicht installiert, Kandidat ist die einzige Version. Bei `grep` sind installierte Version und Kandidat gleich; die Zeile mit `/var/lib/dpkg/status` ist die Paketdatenbank aus Unterabschnitt [2.7](die-paketverwaltung-und-ihre-datenbank.html#stufe-2-7). Anders bei den Grundbefehlen in Rust:

```console
$ apt policy rust-coreutils
rust-coreutils:
  Installed: 0.8.0-0ubuntu3
  Candidate: 0.10.0-1ubuntu2~26.04.1
  Version table:
     0.10.0-1ubuntu2~26.04.1 500
        500 http://archive.ubuntu.com/ubuntu resolute-updates/main amd64 Packages
        500 http://security.ubuntu.com/ubuntu resolute-security/main amd64 Packages
 *** 0.8.0-0ubuntu3 500
        500 http://archive.ubuntu.com/ubuntu resolute/main amd64 Packages
        100 /var/lib/dpkg/status
```

Installiert ist die Fassung 0.8.0 vom Erscheinungstag. In `resolute-updates` und `resolute-security` steht 0.10.0; sie ist neuer und deshalb der Kandidat. Dass sie auch in der Sicherheitsausgabe steht, heißt: Sie behebt Sicherheitslücken.
::::

:::abbildung linux/k9policy 19
Die Versionstabelle von `rust-coreutils` als Siegertreppchen. Zwei Versionen treten an: 0.10.0-1ubuntu2~ 26.04.1 mit zwei Quellen (`resolute-updates`, `resolute-security`, je Priorität 500) und 0.8.0-0ubuntu3 mit `resolute` (500) und `/var/lib/dpkg/status` (100, „installiert“). Erst wird die höchste Priorität verglichen (beide 500, Gleichstand), dann die Version; 0.10.0 steigt aufs Treppchen und bekommt das Schild „Candidate“, 0.8.0 behält das Schild „Installed“ und die drei Sterne.
:::

⁠**Kurz gesagt:** Die Kandidatenversion ist die Version, die `apt` installieren würde: höchste Priorität, dann höchste Version; `apt policy` zeigt sie neben der installierten.

### Abhängigkeiten anzeigen: apt-cache depends

<span class="anker" id="stufe-4-5"></span>

Abschnitt [1](pakete-und-ihre-beziehungen.html#stufe-1) hat Abhängigkeiten aus den Beschreibungen abgelesen. Für ein bestimmtes Paket zeigt sie ein eigener Befehl übersichtlicher, und er beantwortet auch die umgekehrte Frage: Wer hängt von diesem Paket ab?

:::definition Definition 4.5 (apt-cache depends, apt-cache rdepends)
<span class="anker" id="satz-4-5"></span>

`apt-cache depends paket` listet die Beziehungen eines Pakets aus den Paketlisten auf, eine je Zeile, mit der Art der Beziehung davor. Namen in spitzen Klammern sind virtuelle Pakete oder Namen, zu denen es in den Paketlisten kein Paket gibt; darunter stehen eingerückt die Pakete, die sie erfüllen. `apt-cache rdepends paket` listet umgekehrt die Pakete, die `paket` in ihren Beziehungen nennen; mit `--installed` nur die installierten.
:::

::::beispiel Der Graph von jq, aus den Listen gelesen
```console
$ apt-cache depends jq
jq
  Depends: libjq1
  Depends: libc6
  Depends: libonig5
$ apt-cache depends libjq1 libonig5
libjq1
  Depends: libc6
  Depends: libonig5
libonig5
  Depends: libc6
```

Das ist der Graph aus Abbildung [3](pakete-und-ihre-beziehungen.html#abb-3). Umgekehrt: Wer braucht die Bibliothek `libonig5`?

```console
$ apt-cache rdepends libonig5 | head -n 8
libonig5
Reverse Depends:
  libevhtp0t64
  php8.5-mbstring
  libjq1
  jq
  xh
  rust-findutils
$ apt-cache rdepends --installed libc6 | wc -l
622
$ apt-cache rdepends --installed libc6 | tail -n +3 | sort -u | wc -l
422
```

`libonig5` nutzen außer `jq` noch etliche andere Pakete. Bei `libc6` zählt die erste Pipe 622 Zeilen, aber das sind nicht 622 Pakete: Zwei Zeilen sind der Name und die Überschrift `Reverse Depends:`, und `apt-cache` geht jede Version eines Pakets einzeln durch, die in den Paketlisten steht, sodass manche Namen mehrfach erscheinen. Die zweite Pipe überspringt die zwei Kopfzeilen ([Kapitel 6, Abschnitt 1.5](/wissen/informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke/textdaten-datensatze-felder-und-zeilenenden.html#stufe-1-5)) und zählt jeden Namen einmal ([Kapitel 6, Abschnitt 3.6](/wissen/informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke/sortieren-und-zahlen-sort-und-uniq.html#stufe-3-6)): Von der C-Bibliothek hängen 422 installierte Pakete ab.
::::

:::abbildung linux/k9rdepends 20
Derselbe Graph in zwei Richtungen. Links `apt-cache depends jq`: Pfeile gehen von `jq` nach unten zu `libjq1`, `libonig5` und `libc6`. Rechts `apt-cache rdepends libonig5`: Der Blick dreht sich um, Pfeile kommen von oben in `libonig5` hinein, von `jq`, `libjq1`, `php8.5-mbstring`, `rust-findutils` und weiteren. Zum Schluss ein großer Fächer von Pfeilen, die in `libc6` münden, mit der Zahl 422.
:::

Abbildung [20](#abb-20) zeigt beide Blickrichtungen auf denselben Graphen.

::::beispiel Empfehlungen und spitze Klammern
```console
$ apt-cache depends fortune-mod | head -n 8
fortune-mod
  Depends: libc6
  Depends: librecode3
  Conflicts: <fortune>
 |Recommends: fortunes-min
  Recommends: <fortune-cookie-db>
    fortunes
    fortunes-bg
```

Ein senkrechter Strich vor einer Zeile heißt „oder die nächste“: `fortune-mod` empfiehlt `fortunes-min` oder irgendein Paket, das den virtuellen Namen `fortune-cookie-db` erfüllt. Darunter stehen die Spruchsammlungen, die das tun, in vielen Sprachen. `<fortune>` ist ein Name, unter dem es in den Paketlisten kein Paket gibt; mit dem Konflikt schließt `fortune-mod` jedes Paket aus, das so heißt oder diesen Namen erfüllt.
::::

⁠**Kurz gesagt:** `apt-cache depends` zeigt die Beziehungen eines Pakets, `apt-cache rdepends` die Pakete, die es brauchen; spitze Klammern kennzeichnen virtuelle Namen.

### Aufgaben zu Abschnitt [4](#stufe-4)

<span class="anker" id="stufe-4-6"></span>

:::aufgabe Aufgabe 12 ★ Ein Paket für eine Aufgabe finden
<span class="anker" id="aufg-12"></span>

Du willst im Terminal sehen, welche Verzeichnisse auf der Platte am meisten Platz belegen, mit einer bedienbaren Liste statt der Ausgabe von `du` ([Kapitel 3, Abschnitt 10.7](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-finden-und-platz-messen.html#stufe-10-7)). Suche mit `apt search` nach `'disk usage'` und wähle ein Paket. Prüfe mit `apt policy`, ob es installiert ist und welche Version installiert würde.

:::loesung
```console
$ apt search 'disk usage' | grep -A 1 '^ncdu'

WARNING: apt does not have a stable CLI interface. Use with caution in scripts.

ncdu/resolute 1.22-1build1 amd64
  ncurses disk usage viewer
$ apt policy ncdu
ncdu:
  Installed: (none)
  Candidate: 1.22-1build1
  Version table:
     1.22-1build1 500
        500 http://archive.ubuntu.com/ubuntu resolute/universe amd64 Packages
```

Die Suche liefert mehrere Treffer; `ncdu` ist ein Programm, das den Platzbedarf von Verzeichnissen als bedienbare Liste im Terminal zeigt. Ohne `grep` siehst du alle Treffer. `ncdu` ist nicht installiert; installiert würde die Version `1.22-1build1` aus `universe`.
:::
:::

:::aufgabe Aufgabe 13 ★★ cowsay ansehen
<span class="anker" id="aufg-13"></span>

(a) Zeige mit `apt show cowsay` Version, Bereich, Download- und Installationsgröße des Pakets `cowsay`. Was sagt der Bereich über die Pflege des Pakets? (b) Welche Beziehungen nennt `apt-cache depends cowsay`? Welche davon würde Ubuntu mitinstallieren? (c) Warum hat `cowsay` die Architektur `all`?

:::loesung
```console
$ apt show cowsay | grep -E '^(Version|Section|Installed-Size|Download-Size|APT-Sources)'

WARNING: apt does not have a stable CLI interface. Use with caution in scripts.

Version: 3.03+dfsg2-8build1
Section: universe/games
Installed-Size: 89.1 kB
Download-Size: 18.1 kB
APT-Sources: http://archive.ubuntu.com/ubuntu resolute/universe amd64 Packages
$ apt-cache depends cowsay
cowsay
  Depends: libtext-charwidth-perl
  Depends: <perl:any>
    perl
  Suggests: filters
  Suggests: cowsay-off
```

(a) Version `3.03+dfsg2-8build1`, Bereich `universe`, 89,1 kB installiert, 18,1 kB herunterzuladen. `universe` heißt: Freiwillige pflegen das Paket, Ubuntu selbst gibt keine Zusage für Sicherheitsupdates (ohne Ubuntu Pro). Der Zusatz `+dfsg2` in der Version sagt, dass Debian die Quelltexte neu gepackt hat, um Teile zu entfernen, die nicht seinen Regeln für freie Software entsprechen.

(b) `cowsay` hängt von `libtext-charwidth-perl` und von `perl` ab; `<perl:any>` ist ein Name, den das Paket `perl` erfüllt. `filters` und `cowsay-off` sind Vorschläge und werden nicht installiert. Auf dem Testsystem sind beide Abhängigkeiten schon da, deshalb käme nur `cowsay` selbst dazu.

(c) `cowsay` ist ein Skript in der Sprache Perl, kein übersetztes Programm. Es läuft auf jedem Prozessor, für den es `perl` gibt; deshalb hat es die Architektur `all`.
:::
:::

:::aufgabe Aufgabe 14 ★★ Was gerade aktualisierbar ist
<span class="anker" id="aufg-14"></span>

(a) Wie viele Pakete deines Systems lassen sich aktualisieren? Benutze `apt list --upgradable` mit einer Pipe und unterdrücke die Warnung von `apt`. (b) Wie viele davon kommen (auch) aus der Sicherheitsausgabe? (c) Warum zeigt `apt policy sudo-rs` bei dir womöglich etwas anderes als im Kapitel?

:::loesung
```console
$ apt list --upgradable 2>/dev/null | grep -c upgradable
126
$ apt list --upgradable 2>/dev/null | grep -c security
86
```

(a) 126 Pakete; `2>/dev/null` verwirft die Warnung, und `grep -c upgradable` zählt nur die Zeilen der Pakete, nicht die Zeile `Listing...`. (b) 86 Zeilen nennen eine Ausgabe mit `security`. (c) Die Zahlen hängen davon ab, wann deine Paketlisten zuletzt geholt wurden und welche Updates du schon installiert hast; beides ist bei dir anders als auf dem Testsystem am 12. November 2026.
:::
:::

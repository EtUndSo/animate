---
title: Alternativen: ein Befehl, mehrere Pakete
pfad: Informatik / Linux und Kommandozeile / Software installieren: Paketverwaltung
adresse: informatik/linux-und-kommandozeile/software-installieren-paketverwaltung
knoten: Kapitel 9: Software installieren: Paketverwaltung
order: 6141000
summary: Für manche Befehle gibt es mehrere Programme, die dieselbe Aufgabe erfüllen.
tags: Alternativsystem, geschützt
lang: de
---

<span class="anker" id="stufe-9"></span>

:::zweck
Für manche Befehle gibt es mehrere Programme, die dieselbe Aufgabe erfüllen. Ubuntu 26.04 ist dafür ein besonders gutes Beispiel: Es liefert `sudo` und die Grundbefehle in zwei Fassungen. Dieser Abschnitt zeigt, wie das System entscheidet, welche Fassung ein Befehl startet, und wie man das herausfindet, ohne etwas zu verändern.
:::

### Das Alternativsystem

<span class="anker" id="stufe-9-1"></span>

Auf dem Testsystem sind die beiden `awk`-Programme `gawk` und `mawk` installiert, die beide den virtuellen Namen `awk` erfüllen (Unterabschnitt [1.8](pakete-und-ihre-beziehungen.html#stufe-1-8)). Wer `awk` tippt, bekommt aber nur eines. Wer entscheidet, welches?

:::definition Definition 9.1 (Alternativsystem)
<span class="anker" id="satz-9-1"></span>

Das __Alternativsystem__ von Debian und Ubuntu verwaltet Gruppen von Programmen, die dieselbe Aufgabe erfüllen. Für jede Gruppe gibt es einen allgemeinen Namen, etwa `/usr/bin/awk`. Er ist ein symbolischer Link auf `/etc/alternatives/awk`, und dieser zweite Link zeigt auf das gewählte Programm. Jede Alternative hat eine Priorität. Im *automatischen Modus* zeigt der Link auf die Alternative mit der höchsten Priorität; im *manuellen Modus* bleibt er bei der Wahl des Verwalters. Verwaltet wird das mit dem Befehl `update-alternatives`.
:::

::::beispiel Welches awk startet
```console
$ ls -l /usr/bin/awk /etc/alternatives/awk
lrwxrwxrwx 1 root root 13 Aug 27 16:12 /etc/alternatives/awk -> /usr/bin/gawk
lrwxrwxrwx 1 root root 21 Feb  3  2026 /usr/bin/awk -> /etc/alternatives/awk
$ update-alternatives --display awk
awk - auto mode
  link best version is /usr/bin/gawk
  link currently points to /usr/bin/gawk
  link awk is /usr/bin/awk
  slave awk.1.gz is /usr/share/man/man1/awk.1.gz
  slave nawk is /usr/bin/nawk
  slave nawk.1.gz is /usr/share/man/man1/nawk.1.gz
/usr/bin/gawk - priority 10
  slave awk.1.gz: /usr/share/man/man1/gawk.1.gz
  slave nawk: /usr/bin/gawk
  slave nawk.1.gz: /usr/share/man/man1/gawk.1.gz
/usr/bin/mawk - priority 5
  slave awk.1.gz: /usr/share/man/man1/mawk.1.gz
  slave nawk: /usr/bin/mawk
  slave nawk.1.gz: /usr/share/man/man1/mawk.1.gz
```

Die Gruppe steht im automatischen Modus, `gawk` hat mit 10 die höhere Priorität und gewinnt. Mit dem Programm wechseln weitere Links mit, die das Werkzeug *slave* nennt: Die Handbuchseite `awk.1.gz` zeigt immer auf die Seite des gewählten Programms, damit `man awk` zum Programm passt.
::::

:::abbildung linux/k9alternativen 40
Oben `/usr/bin/awk` (allgemeiner Name) $\to$ `/etc/alternatives/awk`; von dort zeigt ein Pfeil auf einen der Kandidaten der Gruppe „awk“, die auf Sockeln stehen: `/usr/bin/gawk` (Priorität 10, höherer Sockel) und `/usr/bin/mawk` (Priorität 5). Ein Schalter „automatisch“ lässt den Pfeil auf den höheren Sockel zeigen. Unten der Folgelink (slave): `awk.1.gz` zeigt auf die passende Handbuchseite `gawk.1.gz`. Zum Schluss springt der Schalter auf „manuell“, der Pfeil schwenkt auf `mawk`, der Folgelink wechselt mit auf `mawk.1.gz`, und die Prioritäten verblassen: Sie zählen dann nicht mehr.
:::

⁠**Kurz gesagt:** Das Alternativsystem führt einen allgemeinen Namen über einen Link in `/etc/alternatives` zum gewählten Programm; automatisch gewinnt die höchste Priorität.

:::hintergrund Warum zwei Links statt einem
Ein einziger Link `/usr/bin/awk` $\to$ `/usr/bin/gawk` würde genügen, um das Programm zu wählen. Der Umweg über `/etc/alternatives` trennt aber zwei Zuständigkeiten. Unter `/usr` liegt, was die Pakete mitbringen und beim Aktualisieren ersetzen; unter `/etc` liegen die Entscheidungen des Verwalters ([Kapitel 3, Abschnitt 7.3](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/die-verzeichnisstruktur-von-linux.html#stufe-7-3)). Die Wahl, welches Programm `awk` sein soll, ist eine solche Entscheidung. Sie steht deshalb in `/etc`, wo man Einstellungen sucht und sichert, und kein Update unter `/usr` rührt sie an. Das Werkzeug merkt sich die Gruppen zusätzlich unter `/var/lib/dpkg/alternatives`.
:::

### sudo und sudo-rs

<span class="anker" id="stufe-9-2"></span>

[Kapitel 7, Abschnitt 6](/wissen/informatik/linux-und-kommandozeile/benutzer-gruppen-und-rechte/kurzzeitig-root-sudo-und-su.html#stufe-6) hat gezeigt, dass `sudo` unter Ubuntu 26.04 die Rust-Fassung sudo-rs ist. Fragt man die Paketdatenbank, wem `/usr/bin/sudo` gehört, bekommt man aber keine Antwort.

```console
$ dpkg -S /usr/bin/sudo
dpkg-query: no path found matching pattern /usr/bin/sudo
$ ls -l /usr/bin/sudo
lrwxrwxrwx 1 root root 22 Mar 13  2026 /usr/bin/sudo -> /etc/alternatives/sudo
$ readlink -f /usr/bin/sudo
/usr/lib/cargo/bin/sudo
$ update-alternatives --display sudo | grep -E 'mode|points|priority'
sudo - auto mode
  link currently points to /usr/lib/cargo/bin/sudo
/usr/bin/sudo.ws - priority 40
/usr/lib/cargo/bin/sudo - priority 50
```

`/usr/bin/sudo` gehört zu keinem Paket, weil kein Paket ihn mitbringt: `update-alternatives` hat den Link angelegt, als die Wartungsskripte der beiden Pakete `sudo-rs` und `sudo` ihre Programme anmeldeten. `readlink -f` folgt allen Links bis zum Ende. Die Rust-Fassung hat Priorität 50, das klassische `sudo` unter dem Namen `sudo.ws` Priorität 40. Abbildung [41](#abb-41) zeigt die Kette der Links. Beide Fassungen sind installiert:

```console
$ sudo --version | head -n 1
sudo-rs 0.2.13-0ubuntu1
$ sudo.ws --version | head -n 1
Sudo version 1.9.17p2
```

:::abbildung linux/k9sudo 41
Die Kette `/usr/bin/sudo` $\to$ `/etc/alternatives/sudo` $\to$ `/usr/lib/cargo/bin/sudo`. Eine Klammer über den ersten beiden Gliedern sagt „angelegt von update-alternatives, in keinem Paket“; das letzte steht auf dem Sockel „Paket `sudo-rs`, Priorität 50“, daneben `/usr/bin/sudo.ws` auf dem Sockel „Paket `sudo`, Priorität 40“. Der automatische Modus zeigt auf die 50. Unten die Folgelinks, die mit dem Hauptlink mitgehen: `sudo.8.gz` auf `sudo-rs.8.gz`, `visudo` auf die Rust-Fassung. `dpkg -S` fragt beim ersten Glied an und bekommt „no path found“.
:::

:::definition Definition 9.2 (Eine Alternative wählen)
<span class="anker" id="satz-9-2"></span>

`sudo update-alternatives --config name` zeigt die Alternativen einer Gruppe mit Nummern und fragt, welche gelten soll; `sudo update-alternatives --set name pfad` wählt eine ohne Rückfrage. Beides schaltet die Gruppe in den manuellen Modus. `sudo update-alternatives --auto name` schaltet zurück in den automatischen Modus.
:::

:::warnung Alternativen nicht zum Ausprobieren umstellen
Eine Umstellung wirkt sofort für alle Benutzer und alle Skripte des Systems. Stellt man `sudo` um und die neue Fassung verhält sich anders, kann man sich im schlimmsten Fall selbst die Verwalterrechte nehmen. `--display` und `--query` lesen nur; `--config`, `--set` und `--auto` gehören auf ein Testsystem, das man notfalls neu aufsetzt.
:::

⁠**Kurz gesagt:** `/usr/bin/sudo` ist ein Link des Alternativsystems; deshalb findet `dpkg -S` ihn nicht, und `update-alternatives --display sudo` zeigt, welche Fassung gilt.

### Die Grundbefehle: coreutils-from-uutils

<span class="anker" id="stufe-9-3"></span>

Auch die Grundbefehle wie `ls` und `cp` gibt es in zwei Fassungen, GNU und uutils ([Kapitel 2, Abschnitt 7](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/zwei-fassungen-der-grundbefehle-gnu-und-uutils.html#stufe-7)). Hier benutzt Ubuntu aber nicht das Alternativsystem, sondern Pakete, die einander ausschließen.

:::definition Definition 9.3 (coreutils-from-uutils, coreutils-from-gnu)
<span class="anker" id="satz-9-3"></span>

Unter Ubuntu 26.04 liegen die Programme beider Fassungen in eigenen Paketen: `rust-coreutils` (uutils) und `gnu-coreutils` (GNU, mit den Namen `gnuls` und so weiter). Welche Fassung die gewöhnlichen Namen wie `/usr/bin/ls` bekommt, entscheidet ein drittes, kleines Paket, das nur die Links enthält: `coreutils-from-uutils` oder `coreutils-from-gnu`. Beide erfüllen den virtuellen Namen `coreutils-from` und stehen mit ihm in Konflikt, sodass immer nur eines installiert sein kann.
:::

::::beispiel Wem die Namen gehören
```console
$ dpkg -S /usr/bin/ls /usr/bin/cp /usr/bin/gnuls
coreutils-from-uutils: /usr/bin/ls
coreutils-from-uutils: /usr/bin/cp
gnu-coreutils: /usr/bin/gnuls
$ ls -l /usr/bin/ls /usr/bin/cp
lrwxrwxrwx 1 root root  5 Mar 30  2026 /usr/bin/cp -> gnucp
lrwxrwxrwx 1 root root 29 Mar 30  2026 /usr/bin/ls -> ../lib/cargo/bin/coreutils/ls
```

Beide Namen gehören `coreutils-from-uutils`. Der Link `ls` führt zum Multicall-Programm von uutils ([Kapitel 2, Abschnitt 7.2](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/zwei-fassungen-der-grundbefehle-gnu-und-uutils.html#stufe-7-2)), der Link `cp` dagegen zu `gnucp`: In Ubuntu 26.04 stammen `cp`, `mv`, `rm`, `df` und `true` noch von GNU, und das Paket legt die Links entsprechend an. Die Beziehungen:

```console
$ apt-cache depends coreutils-from-uutils
coreutils-from-uutils
  PreDepends: rust-coreutils
  PreDepends: gnu-coreutils
  Conflicts: <coreutils-from>
    coreutils-from-gnu
    coreutils-from-busybox
    coreutils-from-toybox
  Breaks: coreutils
  Breaks: libdigest-sha3-perl
  Replaces: coreutils
  Replaces: <coreutils-from>
    coreutils-from-gnu
    coreutils-from-busybox
    coreutils-from-toybox
    coreutils-from-uutils
  Replaces: libdigest-sha3-perl
```

Das Paket braucht beide Programmpakete schon vor dem Auspacken (`PreDepends`), denn seine Links zeigen in beide. Der Konflikt mit dem virtuellen Namen `coreutils-from` schließt alle anderen Anbieter aus; außer GNU gäbe es noch Pakete für BusyBox und Toybox, zwei schlanke Sammlungen von Grundbefehlen. Der Stand auf dem Testsystem:

```console
$ dpkg -l 'coreutils-from-*' rust-coreutils gnu-coreutils
+-- Desired=Unknown/Install/Remove/Purge/Hold
|+- Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
||+ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||| Name                  Version        Architecture Description
+++-=====================-==============-============-==========================================
un  coreutils-from-gnu    <none>         <none>       (no description available)
ii  coreutils-from-uutils 0.0.0~ubuntu25 all          coreutils from the uutils project
ii  gnu-coreutils         9.7-3ubuntu2   amd64        GNU core utilities
ii  rust-coreutils        0.8.0-0ubuntu3 amd64        Universal coreutils utils, written in Rust
```

`un` heißt: `dpkg` kennt den Namen, gewünscht ist nichts Bestimmtes, installiert ist es nicht.
::::

:::abbildung linux/k9coreutils 42
Oben der virtuelle Name `coreutils-from` als gestrichelter Rahmen mit Platz für genau ein Paket; darin steckt `coreutils-from-uutils`, daneben warten grau und ausgeschlossen (`Conflicts`) `coreutils-from-gnu`, `-busybox`, `-toybox`. Von `coreutils-from-uutils` gehen Links nach unten: `ls`, `cat`, `date` zu `rust-coreutils` (Multicall-Programm), `cp`, `mv`, `rm`, `df`, `true` zu `gnu-coreutils` (`gnucp` …). Ein gestrichelter Pfeil deutet den Tausch an: `coreutils-from-gnu` würde in den Rahmen rücken, und alle Links zeigten dann auf `gnu-coreutils`; die beiden Programmpakete selbst blieben installiert.
:::

⁠**Kurz gesagt:** Welche Fassung die Grundbefehle stellt, entscheidet das installierte Paket `coreutils-from-uutils` oder `coreutils-from-gnu`; ein Konflikt auf den virtuellen Namen `coreutils-from` lässt nur eines zu.

:::hintergrund Warum nicht das Alternativsystem?
Die Links des Alternativsystems legen erst die Wartungsskripte an, also am Ende einer Installation. Grundbefehle wie `ls`, `cp` und `rm` benutzen aber die Wartungsskripte aller anderen Pakete, auch mitten in einer Installation oder einem großen Update. Sie müssen deshalb in jedem Augenblick da sein, auch wenn ein Paket nur ausgepackt und noch nicht eingerichtet ist. Ein gewöhnliches Paket, das die Links als Dateien in seinem Datenteil mitbringt, erfüllt das: `dpkg` ersetzt sie beim Auspacken in einem Schritt. Ubuntus Dokumentation rät auch ausdrücklich davon ab, die Grundbefehle über `update-alternatives` umzustellen.
:::

### Unverzichtbare und geschützte Pakete

<span class="anker" id="stufe-9-4"></span>

Was passiert, wenn man ein Paket entfernen will, ohne das das System nicht läuft? Die Paketverwaltung kennt dafür zwei Kennzeichen.

:::definition Definition 9.4 (Unverzichtbar, geschützt)
<span class="anker" id="satz-9-4"></span>

Ein Paket mit `Essential: yes` ist unverzichtbar (Unterabschnitt [2.6](die-paketverwaltung-und-ihre-datenbank.html#stufe-2-6)). Ein Paket mit `Protected: yes` ist __geschützt__: Die Paketverwaltung entfernt es nicht ohne ausdrückliche Erlaubnis, meist weil das System ohne es nicht starten oder nicht verwaltet werden kann. Anders als bei `Essential` dürfen andere Pakete aber nicht einfach annehmen, dass es installiert ist. Beide entfernt `apt` nur, wenn man es mit der Option `--allow-remove-essential` ausdrücklich erlaubt und eine zusätzliche Bestätigung gibt; vorher warnt es deutlich.
:::

::::beispiel grep und coreutils-from-uutils entfernen, nur simuliert
```console
$ dpkg -s coreutils-from-uutils | grep -E '^(Protected|Priority|Essential):'
Protected: yes
Priority: required
$ dpkg -s grep | grep -E '^(Protected|Priority|Essential):'
Essential: yes
Priority: required
$ apt -s remove grep
NOTE: This is only a simulation!
      apt needs root privileges for real execution.
      Keep also in mind that locking is deactivated,
      so don't depend on the relevance to the real current situation!

REMOVING:
  grep

WARNING: The following essential packages will be removed.
This should NOT be done unless you know exactly what you are doing!
  grep
...
```

Der Wechsel der Grundbefehle auf GNU, den Ubuntus Dokumentation für Ubuntu 26.04 beschreibt, entfernt ein geschütztes Paket. Die Simulation zeigt, was das alles nach sich zöge:

```console
$ apt -s install coreutils-from-gnu coreutils-from-uutils- --allow-remove-essential
...
The following packages were automatically installed and are no longer required:
  g++     g++-15-x86-64-linux-gnu  libcrypt-dev
  g++-15  g++-x86-64-linux-gnu     libstdc++-15-dev
Use 'apt autoremove' to remove them.

Installing:
  coreutils-from-gnu

REMOVING:
  build-essential  coreutils-from-uutils

WARNING: The following essential packages will be removed.
This should NOT be done unless you know exactly what you are doing!
  coreutils-from-uutils

Summary:
  Upgrading: 0, Installing: 1, Removing: 2, Not Upgrading: 126
Remv build-essential [12.12ubuntu2.26.04.2]
Remv coreutils-from-uutils [0.0.0~ubuntu25] [coreutils:amd64 ]
Inst coreutils-from-gnu (0.0.0~ubuntu25 Ubuntu:26.04/resolute [all])
Conf coreutils-from-gnu (0.0.0~ubuntu25 Ubuntu:26.04/resolute [all])
```

Ein Minuszeichen hinter einem Paketnamen heißt in `apt install`: dieses Paket entfernen. Überraschend ist die zweite Zeile unter `REMOVING`: Das Paket `build-essential`, das die Werkzeuge zum Übersetzen von C-Programmen zusammenfasst, hängt auf Ubuntu 26.04 ausdrücklich von `coreutils-from-uutils` ab und müsste mitgehen. Danach gälten auch die C++-Werkzeuge als überflüssig. Genau für solche Überraschungen gibt es die Simulation.
::::

:::abbildung linux/k9geschuetzt 43
Eine Kettenreaktion als Graph. Der Befehl „`coreutils-from-gnu` rein, `coreutils-from-uutils` raus“ stößt den ersten Stein an: `coreutils-from-uutils` (Schild „Protected: yes“) wird rot. Ein Pfeil `Depends` von `build-essential` zeigt auf ihn; damit wird auch `build-essential` rot. `build-essential` selbst zeigte mit einem Pfeil auf die Pakete, die es mitgebracht hat: `g++`, `g++-15`, `g++-x86-64-linux-gnu`, `g++-15-x86-64-linux-gnu`, `libstdc++-15-dev` und `libcrypt-dev`; mit `build-essential` verschwindet dieser Pfeil, und die Pakete werden orange „automatisch installiert, nicht mehr gebraucht“. `coreutils-from-gnu` wird grün. Über allem ein Warnschild mit dem Text der Warnung von `apt`.
:::

Abbildung [43](#abb-43) zeigt die Kettenreaktion, die die Simulation aufdeckt.

⁠**Kurz gesagt:** Unverzichtbare und geschützte Pakete entfernt `apt` nur auf ausdrücklichen Befehl und mit Warnung; die Simulation zeigt vorher, was alles mitginge.

### Aufgaben zu Abschnitt [9](#stufe-9)

<span class="anker" id="stufe-9-5"></span>

:::aufgabe Aufgabe 27 ★ Welcher Editor?
<span class="anker" id="aufg-27"></span>

Viele Programme starten einen Texteditor über den allgemeinen Namen `editor`. (a) Welche Alternativen gibt es auf deinem System, mit welchen Prioritäten, und welche gilt? Benutze `update-alternatives --display editor` mit `grep`. (b) Warum hat `ed` eine negative Priorität? (c) Mit welchem Befehl würdest du `vim` fest einstellen, und in welchem Modus stünde die Gruppe danach? Führe ihn nicht aus.

:::loesung
```console
$ update-alternatives --display editor | grep -E 'mode|points|priority'
editor - auto mode
  link currently points to /bin/nano
/bin/ed - priority -100
/bin/nano - priority 40
/usr/bin/vim.basic - priority 30
/usr/bin/vim.tiny - priority 15
```

(a) Vier Alternativen: `ed` mit $-100$, `nano` mit 40, `vim.basic` mit 30 und `vim.tiny` mit 15. Im automatischen Modus gilt `nano`, die höchste Priorität.

(b) `ed` ist ein sehr alter Editor ohne Bildschirmanzeige, der nur Befehle Zeile für Zeile annimmt. Mit der negativen Priorität wird er nur gewählt, wenn sonst kein Editor installiert ist; so gibt es immer irgendeinen.

(c) `sudo update-alternatives --set editor /usr/bin/vim.basic`. Danach steht die Gruppe im manuellen Modus und bleibt bei `vim`, auch wenn später ein Editor mit höherer Priorität dazukommt.
:::
:::

:::aufgabe Aufgabe 28 ★★ Das Rätsel um /usr/bin/awk
<span class="anker" id="aufg-28"></span>

(a) Was antwortet `dpkg -S /usr/bin/awk`, und was `dpkg -S /usr/bin/gawk /usr/bin/mawk`? (b) Erkläre den Unterschied. (c) Wo merkt sich `update-alternatives` die Gruppe `awk`? Sieh dir die Datei mit `cat` an und deute ihre Zeilen.

:::loesung
```console
$ dpkg -S /usr/bin/awk
dpkg-query: no path found matching pattern /usr/bin/awk
$ dpkg -S /usr/bin/gawk /usr/bin/mawk
gawk: /usr/bin/gawk
mawk: /usr/bin/mawk
$ cat /var/lib/dpkg/alternatives/awk
auto
/usr/bin/awk
awk.1.gz
/usr/share/man/man1/awk.1.gz
nawk
/usr/bin/nawk
nawk.1.gz
/usr/share/man/man1/nawk.1.gz

/usr/bin/gawk
10
/usr/share/man/man1/gawk.1.gz
/usr/bin/gawk
/usr/share/man/man1/gawk.1.gz
/usr/bin/mawk
5
/usr/share/man/man1/mawk.1.gz
/usr/bin/mawk
/usr/share/man/man1/mawk.1.gz
```

(a), (b) `/usr/bin/awk` gehört keinem Paket, denn `update-alternatives` hat den Link angelegt; die beiden Programme `gawk` und `mawk` dagegen sind gewöhnliche Dateien ihrer Pakete.

(c) In `/var/lib/dpkg/alternatives/awk`. Die erste Zeile ist der Modus, die zweite der allgemeine Name. Dann folgen die mitwechselnden Links, je ein Name und ein Pfad, bis zur Leerzeile. Danach steht jede Alternative mit ihrem Programm, ihrer Priorität und den Zielen der mitwechselnden Links in derselben Reihenfolge: für `gawk` die Handbuchseite `gawk.1.gz`, als `nawk` wieder `gawk` und dessen Handbuchseite.
:::
:::

:::aufgabe Aufgabe 29 ★★★ Warum build-essential mitginge
<span class="anker" id="aufg-29"></span>

(a) Zeige mit `apt-cache show build-essential` und `grep`, wovon `build-essential` abhängt. (b) Welche installierten Pakete hängen von `coreutils-from-uutils` ab? Benutze `apt-cache rdepends --installed`. (c) Erkläre damit die Simulation aus Unterabschnitt [9.4](#stufe-9-4). Was müsste ein Verwalter nach dem Wechsel tun, wenn er weiter C-Programme übersetzen will?

:::loesung
```console
$ apt-cache show build-essential | grep -m 1 '^Depends'
Depends: libc6-dev | libc-dev, gcc (>= 4:14.2), g++ (>= 4:14.2), make, dpkg-dev (>= 1.22.11), libcrypt-dev, coreutils-from-uutils
$ apt-cache rdepends --installed coreutils-from-uutils
coreutils-from-uutils
Reverse Depends:
  rust-coreutils
  build-essential
  build-essential
 |coreutils
```

(a) `build-essential` fasst Compiler und Werkzeuge zusammen, enthält selbst kaum Dateien und hängt am Ende ausdrücklich von `coreutils-from-uutils` ab. `grep -m 1` nimmt nur den ersten Treffer.

(b) `rust-coreutils`, `build-essential` (zweimal, für zwei Versionen in den Listen) und `coreutils`; der senkrechte Strich bei `coreutils` heißt, dass es eine Oder-Beziehung ist, die auch ein anderes Paket erfüllen kann.

(c) Beim Wechsel geht `coreutils-from-uutils`. Damit wäre die Abhängigkeit von `build-essential` verletzt, also muss es mitgehen. Dann hängt kein manuell installiertes Paket mehr von `g++` und einigen Bibliotheken ab; die Simulation meldet sie deshalb als überflüssig. `gcc` und `make` fehlen in dieser Liste: Auf dem Testsystem braucht oder empfiehlt sie noch ein anderes installiertes Paket. Wer weiter übersetzen will, markiert die Werkzeuge vor dem Wechsel als manuell installiert, etwa `sudo apt-mark manual gcc g++ make`, damit `autoremove` sie nicht abräumt; `build-essential` selbst lässt sich neben `coreutils-from-gnu` nicht installieren.
:::
:::

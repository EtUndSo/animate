---
title: Ein Paket von innen
pfad: Informatik / Linux und Kommandozeile / Software installieren: Paketverwaltung
adresse: informatik/linux-und-kommandozeile/software-installieren-paketverwaltung
knoten: Kapitel 9: Software installieren: Paketverwaltung
order: 6140600
summary: Ein Paket ist keine geheimnisvolle Software-Kapsel, sondern eine Archivdatei, die man herunterladen, öffnen und ansehen kann, ohne etwas zu installieren.
tags: Paketzwischenspeicher, Steuerteil, Datenteil
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Ein Paket ist keine geheimnisvolle Software-Kapsel, sondern eine Archivdatei, die man herunterladen, öffnen und ansehen kann, ohne etwas zu installieren. Dieser Abschnitt nimmt das Paket `hello` auseinander und zeigt, was die Paketverwaltung beim Installieren eigentlich auspackt.
:::

### Eine Paketdatei herunterladen: apt download

<span class="anker" id="stufe-5-1"></span>

Um ein Paket zu untersuchen, braucht man seine Datei. `apt` kennt aus der Paketliste ihren Ort und kann sie holen, ohne sie zu installieren.

:::definition Definition 5.1 (apt download)
<span class="anker" id="satz-5-1"></span>

`apt download paket` lädt die Paketdatei der Kandidatenversion in das Arbeitsverzeichnis. Es installiert nichts, löst keine Abhängigkeiten auf und braucht kein `root`.
:::

::::beispiel hello holen
```console
$ apt download hello
Get:1 http://archive.ubuntu.com/ubuntu resolute/main amd64 hello amd64 2.10-5build1 [26.1 kB]
Fetched 26.1 kB in 0s (282 kB/s)
$ ls -l
total 28
-rw-r--r-- 1 student student 26068 Feb  2  2026 hello_2.10-5build1_amd64.deb
```

Die Datei hat genau die 26 068 Byte, die in der Paketliste unter `Size` stehen. Ihr Änderungsdatum übernimmt `apt` vom Server; es ist der Tag, an dem Ubuntu das Paket gebaut und dort abgelegt hat.
::::

Beim Installieren lädt `apt` die Paketdateien nicht ins Arbeitsverzeichnis, sondern in seinen eigenen __Paketzwischenspeicher__ `/var/cache/apt/archives`. Der Befehl `apt` löscht sie dort nach einer erfolgreichen Installation wieder; das ältere `apt-get` lässt sie liegen, bis man sie mit `sudo apt clean` löscht. Auf dem Testsystem liegen dort Dateien früherer Vorgänge. Den Doppelpunkt einer Epoche schreibt `apt` in diesen Dateinamen als `%3a`, so wie in Webadressen:

```console
$ ls /var/cache/apt/archives | head -n 3
acl_2.3.2-2_amd64.deb
bind9-dnsutils_1%3a9.20.24-1ubuntu0.5_amd64.deb
bind9-host_1%3a9.20.24-1ubuntu0.5_amd64.deb
```

:::abbildung linux/k9download 21
Zwei Wege einer Paketdatei vom Server. Oben `apt download hello`: Die Datei landet im Arbeitsverzeichnis `~/linuxk9`, Schild „nur geladen, nichts installiert, kein root“. Unten `sudo apt install`: Die Datei landet in `/var/cache/apt/archives`, wandert von dort weiter zu `dpkg` und wird nach dem Installieren wieder gelöscht. Am Rand die Größe 26 068 Byte, die mit dem Feld `Size` der Paketliste übereinstimmt (grünes Gleichheitszeichen).
:::

Abbildung [21](#abb-21) stellt beide Ablageorte nebeneinander.

⁠**Kurz gesagt:** `apt download` holt nur die Paketdatei ins Arbeitsverzeichnis; beim Installieren landen die Dateien im Paketzwischenspeicher `/var/cache/apt/archives`.

### Der Aufbau einer Paketdatei

<span class="anker" id="stufe-5-2"></span>

Was steckt in den 26 068 Byte? Der Befehl `file` erkennt Dateien an ihren ersten Bytes ([Kapitel 3, Abschnitt 4.6](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-ansehen.html#stufe-4-6)), und er kennt auch Pakete.

:::definition Definition 5.2 (Aufbau einer .deb-Datei)
<span class="anker" id="satz-5-2"></span>

Eine Paketdatei im Format `.deb` ist ein Archiv im einfachen Unix-Format `ar` mit genau drei Teilen in fester Reihenfolge:

<ul>

<li>

`debian-binary`: eine Textdatei mit der Formatversion `2.0`;

</li>

<li>

`control.tar`: der __Steuerteil__, ein komprimiertes Archiv mit der Paketbeschreibung, den Prüfsummen der Dateien und den Wartungsskripten;

</li>

<li>

`data.tar`: der __Datenteil__, ein komprimiertes Archiv mit den Dateien, die installiert werden, mit Pfaden relativ zur Wurzel `/`.

</li>

</ul>
:::

Die Endung hinter `.tar` nennt das Verfahren, mit dem komprimiert wurde; Ubuntu benutzt `.zst` für Zstandard. `ar t` zeigt die Teile eines `ar`-Archivs.

::::beispiel hello zerlegt
```console
$ file hello_2.10-5build1_amd64.deb
hello_2.10-5build1_amd64.deb: Debian binary package (format 2.0), with control.tar.zst, data compression zst
$ ar t hello_2.10-5build1_amd64.deb
debian-binary
control.tar.zst
data.tar.zst
```
::::

:::abbildung linux/k9deb 22
Die Paketdatei `hello_2.10-5build1_amd64.deb` als Streifen von 26 068 Byte (nicht maßstäblich), der sich in drei Abschnitte teilt: ein schmaler Kopf `debian-binary` („2.0“), ein kleiner Block `control.tar.zst` (856 Byte) und ein großer `data.tar.zst` (25 019 Byte); dazu kommen $8 + 3 \cdot 60$ Byte Verwaltungsangaben des Archivs und 1 Füllbyte. Der Steuerteil klappt auf zu `control` und `md5sums`, der Datenteil zu einem Baum `usr/bin/hello`, `usr/share/doc/hello/…`, `usr/share/info/…`, `usr/share/man/man1/hello.1.gz`.
:::

⁠**Kurz gesagt:** Eine `.deb`-Datei ist ein `ar`-Archiv aus Formatkennung, Steuerteil (Beschreibung, Prüfsummen, Skripte) und Datenteil (die Dateien samt Pfaden).

:::hintergrund Warum ein so einfaches Format
`ar` ist eines der ältesten Archivformate von Unix; Werkzeuge zum Entpacken gibt es auf jedem System. Die Formatkennung steht als erster Teil vorn, damit ein Programm schon nach wenigen Byte weiß, ob es die Datei versteht. Dass Steuerteil und Datenteil getrennt sind, hat einen praktischen Grund: Um Beschreibung und Abhängigkeiten zu lesen, muss man nur den kleinen Steuerteil auspacken, nicht die oft großen Programmdateien. Mit gewöhnlichen Werkzeugen wie `ar` und `tar` kann man ein Paket deshalb auch auf einem Rechner ohne `dpkg` untersuchen.
:::

### Der Steuerteil: dpkg-deb -I

<span class="anker" id="stufe-5-3"></span>

Bevor man ein Paket installiert, das nicht aus den Paketquellen stammt, will man wissen, was es verlangt und ob es Skripte mitbringt. Das steht im Steuerteil.

:::definition Definition 5.3 (dpkg-deb -I)
<span class="anker" id="satz-5-3"></span>

`dpkg-deb` ist das Werkzeug von `dpkg` für einzelne Paketdateien. `dpkg-deb -I datei.deb` zeigt den Inhalt des Steuerteils: Größe und Zeilenzahl jeder Datei darin, dann die Paketbeschreibung.
:::

::::beispiel Der Steuerteil von hello
```console
$ dpkg-deb -I hello_2.10-5build1_amd64.deb
 new Debian package, version 2.0.
 size 26068 bytes: control archive=856 bytes.
     842 bytes,    21 lines      control
     375 bytes,     6 lines      md5sums
 Package: hello
 Version: 2.10-5build1
 Architecture: amd64
...
```

Der Steuerteil von `hello` enthält nur zwei Dateien: die Paketbeschreibung `control` aus Unterabschnitt [1.3](pakete-und-ihre-beziehungen.html#stufe-1-3) und `md5sums` mit einer Prüfsumme je Datei des Datenteils, sechs Zeilen für sechs Dateien. Wartungsskripte hat `hello` nicht; hätte es welche, stünden sie hier als `preinst`, `postinst`, `prerm` oder `postrm` in der Liste.
::::

:::abbildung linux/k9steuerteil 23
Terminalbild mit den ersten Zeilen von `$ dpkg-deb -I hello_2.10-5build1_amd64.deb`. Die beiden Zeilen `control` und `md5sums` werden hervorgehoben; Pfeile führen zu zwei aufgeklappten Zetteln: `control` mit den Feldern der Paketbeschreibung, `md5sums` mit sechs Zeilen „Prüfsumme – Pfad“. Daneben vier leere, gestrichelte Plätze `preinst`, `postinst`, `prerm`, `postrm` mit dem Hinweis „bei hello keine Skripte“.
:::

Abbildung [23](#abb-23) zeigt, was im Steuerteil steckt und was fehlt.

⁠**Kurz gesagt:** `dpkg-deb -I` zeigt den Steuerteil einer Paketdatei: Beschreibung, Prüfsummen der Dateien und gegebenenfalls Wartungsskripte.

### Der Datenteil: dpkg-deb -c und -x

<span class="anker" id="stufe-5-4"></span>

Was würde das Paket wohin schreiben? Das verrät der Datenteil, und man kann ihn auch an einem harmlosen Ort auspacken.

:::definition Definition 5.4 (dpkg-deb -c, dpkg-deb -x)
<span class="anker" id="satz-5-4"></span>

`dpkg-deb -c datei.deb` listet den Datenteil wie `ls -l`: Rechte, Besitzer, Größe, Datum und Pfad jeder Datei. `dpkg-deb -x datei.deb verzeichnis` packt den Datenteil in das angegebene Verzeichnis aus, ohne Skripte auszuführen und ohne die Paketdatenbank zu verändern.
:::

::::beispiel Wohin hello seine Dateien legen würde
```console
$ dpkg-deb -c hello_2.10-5build1_amd64.deb
drwxr-xr-x root/root         0 2026-02-02 21:44 ./
drwxr-xr-x root/root         0 2026-02-02 21:44 ./usr/
drwxr-xr-x root/root         0 2026-02-02 21:44 ./usr/bin/
-rwxr-xr-x root/root     26936 2026-02-02 21:44 ./usr/bin/hello
...
-rw-r--r-- root/root       790 2026-02-02 21:44 ./usr/share/man/man1/hello.1.gz
```

Alle Dateien gehören `root`; das Programm hat die Rechte `rwxr-xr-x` ([Kapitel 7, Abschnitt 2.4](/wissen/informatik/linux-und-kommandozeile/benutzer-gruppen-und-rechte/die-rechte-einer-datei.html#stufe-2-4)). Die Pfade beginnen mit `./`: Sie werden relativ zur Wurzel `/` angelegt. Packt man den Datenteil in ein Unterverzeichnis aus, entsteht dort derselbe Baum:

```console
$ dpkg-deb -x hello_2.10-5build1_amd64.deb auspacken
$ tree auspacken
auspacken
└── usr
    ├── bin
    │   └── hello
    └── share
        ├── doc
        │   └── hello
        │       ├── NEWS.gz
        │       ├── changelog.Debian.gz
        │       └── copyright
        ├── info
        │   └── hello.info.gz
        └── man
            └── man1
                └── hello.1.gz

9 directories, 6 files
```

Das Programm läuft sogar von dort aus:

```console
$ ./auspacken/usr/bin/hello
Hello, world!
$ ./auspacken/usr/bin/hello -g 'Guten Tag'
Guten Tag
$ dpkg -l hello
dpkg-query: no packages found matching hello
```

Die Paketdatenbank weiß von all dem nichts: `hello` ist nicht installiert, obwohl es auf der Platte liegt und läuft. Die Dateien gehören dir, nicht `root`, denn `dpkg-deb -x` übernimmt die Besitzer nur, wenn `root` es aufruft.
::::

:::abbildung linux/k9auspacken 24
Zwei Spalten mit derselben Paketdatei oben. Links „`dpkg-deb -x`“: Die Dateien landen in `~/linuxk9/auspacken/usr/…`, Besitzer `student`; das Programm läuft („Hello, world!“); die Paketdatenbank bleibt leer („no packages found“). Rechts „Installieren“: Die Dateien landen unter `/usr`, Besitzer `root`, das Programm läuft ebenso; zusätzlich laufen die Abhängigkeitsprüfung und, falls vorhanden, die Wartungsskripte (`hello` hat keine), und in der Paketdatenbank erscheint ein Eintrag `ii hello`. Die drei Zusatzschritte der rechten Spalte leuchten nacheinander auf.
:::

Abbildung [24](#abb-24) vergleicht Auspacken und Installieren.

⁠**Kurz gesagt:** Der Datenteil enthält die Dateien mit ihren Zielpfaden; `dpkg-deb -x` packt ihn irgendwohin aus, ohne zu installieren.

:::hintergrund Installieren ist mehr als Auspacken
Das Experiment zeigt, was Installieren ausmacht. Die Dateien an ihren Ort zu bringen ist nur ein Teil davon. Dazu kommen drei Dinge, die `dpkg-deb -x` nicht tut: `dpkg` trägt jede Datei in die Paketdatenbank ein, es führt die Wartungsskripte aus, und es prüft vorher Abhängigkeiten und Konflikte. Erst diese Buchführung macht das Paket später sauber entfernbar und aktualisierbar. Wer Dateien von Hand nach `/usr` kopiert, bekommt ein laufendes Programm, aber eines, das die Paketverwaltung nicht kennt und beim nächsten Aktualisieren ohne Warnung überschreiben könnte.
:::

### Aufgaben zu Abschnitt [5](#stufe-5)

<span class="anker" id="stufe-5-5"></span>

:::aufgabe Aufgabe 15 ★★ Die Dampflok untersuchen
<span class="anker" id="aufg-15"></span>

Das Paket `sl` zeigt eine Dampflok, die durchs Terminal fährt, wenn man sich bei `ls` vertippt. Lade es mit `apt download` in dein Übungsverzeichnis. (a) Wie heißt die Paketdatei, und wie groß ist sie? (b) Welche Abhängigkeiten nennt der Steuerteil? (c) Wohin würde das Programm installiert? (d) Packe den Datenteil in ein Verzeichnis `sl-aus` aus und starte das Programm von dort. Was passiert, und welche Zahl steht danach in `$?`? Erkläre es mit `dpkg -l` für die Bibliotheken aus (b).

:::loesung
```console
$ apt download sl
Get:1 http://archive.ubuntu.com/ubuntu resolute/universe amd64 sl amd64 5.02-1build1 [12.9 kB]
...
$ ls -l sl_*.deb
-rw-r--r-- 1 student student 12902 Nov 24  2025 sl_5.02-1build1_amd64.deb
$ dpkg-deb -f sl_*.deb Depends
libc6 (>= 2.34), libncurses6 (>= 6), libtinfo6 (>= 6)
$ dpkg-deb -c sl_*.deb | grep games/
drwxr-xr-x root/root         0 2025-11-24 19:28 ./usr/games/
-rwxr-xr-x root/root     26800 2025-11-24 19:28 ./usr/games/sl
$ dpkg-deb -x sl_*.deb sl-aus
$ ./sl-aus/usr/games/sl
./sl-aus/usr/games/sl: error while loading shared libraries: libncurses.so.6: cannot open shared object file: No such file or directory
$ echo $?
127
$ dpkg -l libncurses6 libtinfo6
...
ii  libtinfo6:amd64 6.6+20251231-1 amd64        shared low-level terminfo library for terminal handling
dpkg-query: no packages found matching libncurses6
```

(a) `sl_5.02-1build1_amd64.deb`, 12 902 Byte. `dpkg-deb -f datei feld` gibt ein einzelnes Feld der Beschreibung aus.

(b) `libc6`, `libncurses6` und `libtinfo6`, jeweils mit einer Mindestversion.

(c) Nach `/usr/games/sl`; Spiele liegen bei Debian und Ubuntu in `/usr/games`, das ebenfalls im Suchpfad steht ([Kapitel 2, Abschnitt 3.2](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/arten-von-befehlen.html#stufe-3-2)).

(d) Das Programm startet nicht. Bevor es läuft, lädt ein Teil des Systems die Bibliotheken, die es braucht, und `libncurses.so.6` aus dem Paket `libncurses6` fehlt; `libtinfo6` ist installiert. Der Status 127 kommt hier von diesem Lader, nicht von der Shell. Genau das verhindert die Abhängigkeit: Bei `apt install sl` hätte `apt` `libncurses6` mitinstalliert. Ein ausgepacktes Paket bekommt keine Abhängigkeiten.
:::
:::

:::aufgabe Aufgabe 16 ★ Prüfsummen im Steuerteil
<span class="anker" id="aufg-16"></span>

Packe den Steuerteil von `hello` mit `dpkg-deb -e hello_2.10-5build1_amd64.deb steuer` in ein Verzeichnis `steuer` aus. (a) Welche Dateien entstehen? (b) Vergleiche die Prüfsumme für `usr/bin/hello` in `steuer/md5sums` mit `md5sum auspacken/usr/bin/hello`. (c) Wozu könnte die Paketverwaltung diese Prüfsummen nach dem Installieren brauchen?

:::loesung
```console
$ dpkg-deb -x hello_2.10-5build1_amd64.deb auspacken
$ dpkg-deb -e hello_2.10-5build1_amd64.deb steuer
$ ls steuer
control  md5sums
$ grep usr/bin/hello steuer/md5sums
744cd4018e23f9e830ffd19d602311cd  usr/bin/hello
$ md5sum auspacken/usr/bin/hello
744cd4018e23f9e830ffd19d602311cd  auspacken/usr/bin/hello
```

(a) `control` und `md5sums`; Wartungsskripte hat `hello` nicht.

(b) Die Werte stimmen überein: Die ausgepackte Datei ist genau die, die der Paketbetreuer eingepackt hat.

(c) Nach dem Installieren legt `dpkg` die Datei als `/var/lib/dpkg/info/hello.md5sums` ab. Mit `dpkg --verify paket` vergleicht es später die installierten Dateien mit diesen Prüfsummen und meldet jede, die sich verändert hat, etwa durch einen Fehler auf der Platte oder eine Änderung von Hand. Gegen einen Angreifer mit `root`-Rechten hilft das wenig, denn er kann auch die Prüfsummen in der Paketdatenbank ändern.
:::
:::

---
title: Aufräumen: temporäre Dateien und `trap`
pfad: Informatik / Linux und Kommandozeile / Shell-Skripte
adresse: informatik/linux-und-kommandozeile/shell-skripte
knoten: Kapitel 10: Shell-Skripte
order: 6151000
summary: Viele Skripte brauchen Zwischendateien.
tags: mktemp, trap 'befehle' EXIT
lang: de
---

<span class="anker" id="stufe-9"></span>

:::zweck
Viele Skripte brauchen Zwischendateien. Dieser Abschnitt zeigt, wie man sie sicher anlegt, wie ein Skript sie auch dann wegräumt, wenn es abgebrochen wird, und wie ein vollständiges, robustes Skript aufgebaut ist.
:::

:::::vorwissen Was du dafür brauchst: Archive mit `tar` und das Datum

<span class="anker" id="stufe-9-1"></span>

Das Beispiel dieses Abschnitts packt ein Verzeichnis in eine Archivdatei ([Kapitel 9, Abschnitt 1.1](/wissen/informatik/linux-und-kommandozeile/software-installieren-paketverwaltung/pakete-und-ihre-beziehungen.html#stufe-1-1)). Unter Linux erledigt das der Befehl `tar`. Seine Optionen schreibt man meist als Buchstaben hintereinander:

<ul>

<li>

`-c` legt ein neues Archiv an, `-t` listet den Inhalt eines Archivs auf;

</li>

<li>

`-z` komprimiert das Archiv beim Schreiben mit `gzip` und entpackt es beim Lesen; solche Archive enden üblicherweise auf `.tar.gz`;

</li>

<li>

`-f datei` nennt die Archivdatei;

</li>

<li>

`-C verzeichnis` wechselt vor dem Einpacken in dieses Verzeichnis, damit die Pfade im Archiv dort beginnen.

</li>

</ul>

```console
$ tar -czf fotos.tar.gz -C fotos .
$ tar -tzf fotos.tar.gz
./
./strand 2.jpg
./berg.png
./2026/
./strand 1.jpg
./2027/
$ rm fotos.tar.gz
```

Die Reihenfolge der Einträge ist die, in der das Dateisystem sie liefert, nicht alphabetisch. Abbildung [38](#abb-38) zeigt, was die Optionen bewirken.

:::abbildung linux/k10tar 38
Links das Verzeichnis `fotos` mit `strand 1.jpg`, `strand 2.jpg`, `berg.png` und den Unterverzeichnissen `2026`, `2027`. `-C fotos` stellt einen Wegweiser „erst hineinwechseln“ auf, `.` nimmt alles darin mit. Die Einträge wandern in einen Karton (`-c`), der Karton wird zusammengepresst (`-z`) und bekommt das Etikett `fotos.tar.gz` (`-f`). Unten öffnet `tar -tzf` den Karton nur zum Hineinschauen: Die Namen erscheinen mit `./` davor, die Dateien bleiben drin.
:::

Das heutige Datum im Format Jahr-Monat-Tag liefert `date +%F` ([Kapitel 2, Abschnitt 6.3](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/das-system-erkunden.html#stufe-6-3)); in Dateinamen sortieren sich solche Daten von selbst richtig:

```console
$ date +%F
2026-11-12
```

⁠**Kurz gesagt:** `tar -czf archiv.tar.gz -C ordner .` packt ein Verzeichnis, `tar -tzf` zeigt den Inhalt, `date +%F` liefert das Datum für Dateinamen.

:::::

### Die temporäre Datei: `mktemp`

<span class="anker" id="stufe-9-2"></span>

Eine Zwischendatei mit einem festen Namen wie `/tmp/zwischen.txt` hat zwei Probleme. Laufen zwei Kopien des Skripts gleichzeitig, schreiben beide in dieselbe Datei. Und `/tmp` teilen sich alle Benutzer des Rechners ([Kapitel 3, Abschnitt 7.6](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/die-verzeichnisstruktur-von-linux.html#stufe-7-6)); unter einem Namen, den jeder vorhersehen kann, könnte schon etwas liegen, das ein anderer angelegt hat.

:::definition Definition 9.1 (`mktemp`)
<span class="anker" id="satz-9-1"></span>

Der Befehl __`mktemp`__ legt eine neue, leere Datei mit einem zufälligen Namen an, die nur der Besitzer lesen und schreiben darf (Rechte 600), und gibt ihren Namen aus. Ohne Argument bekommt sie einen Namen der Form `tmp.XXXXXXXXXX`, wobei die `X` durch zufällige Zeichen ersetzt werden, und entsteht in `/tmp`, oder in dem Verzeichnis, das die Umgebungsvariable `TMPDIR` nennt, falls sie gesetzt ist. `mktemp -d` legt ein Verzeichnis an (Rechte 700), `mktemp -p verzeichnis vorlage` eine Datei nach der eigenen Vorlage in einem anderen Verzeichnis.
:::

Den Namen fängt man mit der Befehlsersetzung ein:

```console
$ zwischen=$(mktemp)
$ echo "$zwischen"
/tmp/tmp.JopPYFgzyA
$ ls -l "$zwischen"
-rw------- 1 student student 0 Nov 12 23:46 /tmp/tmp.JopPYFgzyA
$ rm "$zwischen"
$ mktemp -p . notiz.XXXX
./notiz.8QcI
```

```console
$ ordner=$(mktemp -d)
$ ls -ld "$ordner"
drwx------ 2 student student 40 Nov 12 23:46 /tmp/tmp.A0M1Sy6jhB
$ rmdir "$ordner"
```

`mktemp` legt die Datei selbst an, bevor es den Namen ausgibt; gibt es den Namen schon, wählt es einen anderen. Wer die Datei bekommt, ist sicher, dass sie neu und leer ist und nur ihm gehört. Abbildung [39](#abb-39) zeigt den Vorgang.

:::abbildung linux/k10mktemp 39
Die Vorlage `tmp.XXXXXXXXXX` als Schild mit zehn leeren Würfelfeldern. Zehn Würfel rollen hinein und zeigen zufällige Zeichen, daraus wird `tmp.JopPYFgzyA`. Ein Stempel „neu angelegt, leer, `rw-------`“ prägt die Datei im Verzeichnis `/tmp`, in dem schon andere Dateien anderer Benutzer stehen. Ein zweiter Lauf daneben erzeugt einen anderen Namen; die beiden Dateien kommen sich nicht in die Quere.
:::

⁠**Kurz gesagt:** `mktemp` legt eine Datei mit unvorhersehbarem Namen und den Rechten 600 an und gibt den Namen aus.

### Aufräumen beim Beenden: `trap … EXIT`

<span class="anker" id="stufe-9-3"></span>

Eine Zwischendatei soll verschwinden, wenn das Skript endet, egal wie: nach getaner Arbeit, nach `exit 1` mitten im Skript oder weil jemand Strg+C drückt. An jedes `exit` ein `rm` zu schreiben ist mühsam und hilft bei Strg+C nicht.

[Kapitel 8, Abschnitt 5.2](/wissen/informatik/linux-und-kommandozeile/prozesse-signale-und-dienste/mit-signalen-arbeiten.html#stufe-5-2) hat `trap` eingeführt: `trap 'befehle' SIGNAL` legt fest, was die Shell tut, wenn ein Signal eintrifft. Für Skripte ist ein besonderer Name wichtig, der kein Signal ist.

:::definition Definition 9.2 (`trap … EXIT`)
<span class="anker" id="satz-9-2"></span>

Mit __`trap 'befehle' EXIT`__ führt die bash die Befehle aus, unmittelbar bevor sie sich beendet: wenn das Skript am Ende ankommt, bei `exit` und auch, wenn sie durch ein Signal wie SIGINT, SIGTERM oder SIGHUP beendet wird. Nicht ausgeführt werden sie, wenn der Prozess mit SIGKILL beendet wird.
:::

Die Befehle stehen in einfachen Anführungszeichen, damit `$tmp` erst beim Ausführen eingesetzt wird. Das Skript `zwischendatei.sh` legt eine Zwischendatei an, richtet das Aufräumen ein und tut dann so, als arbeite es lange; `sleep 600` wartet zehn Minuten:

```bash zwischendatei.sh
#!/bin/bash
# zwischendatei.sh: legt eine Zwischendatei an und räumt sie immer weg
tmp=$(mktemp)
trap 'rm -f "$tmp"; echo "Zwischendatei gelöscht"' EXIT
echo "Zwischendatei: $tmp"
echo "Ich arbeite ..."
sleep 600
echo "Fertig."
```

Nach einer Sekunde wird es mit Strg+C abgebrochen:

```console
$ chmod +x zwischendatei.sh
$ ./zwischendatei.sh
Zwischendatei: /tmp/tmp.ULJNwITrfq
Ich arbeite ...
^C
Zwischendatei gelöscht
$ echo $?
130
```

Der Status 130 ist 128 + 2, das Zeichen für einen Abbruch durch SIGINT ([Kapitel 8, Abschnitt 4.7](/wissen/informatik/linux-und-kommandozeile/prozesse-signale-und-dienste/signale.html#stufe-4-7)). Mit SIGTERM aus `kill` geht es ebenso. Damit die Ausgabe des Skripts im Hintergrund nicht zwischen die Eingabeaufforderungen gerät, schreibt sie diesmal in eine Datei; `wait` wartet, bis der Job beendet ist ([Kapitel 8, Abschnitte 3.2](/wissen/informatik/linux-und-kommandozeile/prozesse-signale-und-dienste/vordergrund-hintergrund-und-jobs.html#stufe-3-2) und [3.6](/wissen/informatik/linux-und-kommandozeile/prozesse-signale-und-dienste/vordergrund-hintergrund-und-jobs.html#stufe-3-6)):

```console
$ ./zwischendatei.sh > protokoll.txt &
[1] 684
$ kill %1
$ wait
$ cat protokoll.txt
Zwischendatei: /tmp/tmp.kMFXehOtyo
Ich arbeite ...
Zwischendatei gelöscht
```

Gegen SIGKILL hilft nichts, denn dieses Signal kann kein Prozess abfangen ([Kapitel 8, Abschnitt 4.5](/wissen/informatik/linux-und-kommandozeile/prozesse-signale-und-dienste/signale.html#stufe-4-5)). Damit die liegengebliebene Datei leicht zu finden ist, setzt die Zuweisung `TMPDIR=$PWD` vor dem Befehl ([Kapitel 5, Abschnitt 4.6](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/umgebung-und-vererbung.html#stufe-4-6)) das Verzeichnis für `mktemp` für diesen einen Lauf auf das Übungsverzeichnis:

```console
$ TMPDIR=$PWD ./zwischendatei.sh > protokoll.txt &
[1] 689
$ kill -9 %1
$ wait
$ cat protokoll.txt
Zwischendatei: /home/student/linuxk10/tmp.occObehWXm
Ich arbeite ...
$ ls tmp.*
tmp.occObehWXm
$ rm tmp.*
```

Abbildung [40](#abb-40) fasst zusammen, wann das Aufräumen läuft.

:::abbildung linux/k10trap 40
Eine Zeitleiste des Skripts: Start, `mktemp` legt eine Datei an, `trap ... EXIT` hängt ein Schild „vor dem Ende: `rm`“ an den Ausgang, dann der lange Arbeitsteil. Vier Enden zweigen ab: „läuft durch“, „`exit 1`“, „Strg+C (SIGINT)“, „`kill` (SIGTERM)“; alle vier führen durch den Ausgang mit dem Schild, die Datei verschwindet. Ein fünftes Ende „`kill -9` (SIGKILL)“ führt unter dem Ausgang vorbei direkt ins Aus; die Datei bleibt rot markiert liegen.
:::

:::hintergrund Warum Strg+C auch `sleep` trifft
Strg+C schickt SIGINT nicht nur an das Skript, sondern an alle Prozesse des Vordergrund-Jobs, also auch an `sleep`, das das Skript gestartet hat; ebenso schickt `kill %1` das Signal an alle Prozesse des Jobs. `sleep` endet sofort, die bash des Skripts beendet sich ebenfalls und führt vorher die `EXIT`-Befehle aus. Schickt man SIGTERM dagegen mit `kill` und der Prozessnummer nur an die bash, endet zwar die bash sofort und führt ihre `EXIT`-Befehle aus, aber `sleep` bekommt nichts davon mit und läuft weiter, bis seine zehn Minuten um sind. Hätte das Skript für SIGTERM einen eigenen `trap`, würde die bash sogar erst das Ende von `sleep` abwarten ([Kapitel 8, Abschnitt 5.2](/wissen/informatik/linux-und-kommandozeile/prozesse-signale-und-dienste/mit-signalen-arbeiten.html#stufe-5-2)). Das Signal an den ganzen Job erreicht dagegen alle Beteiligten auf einmal.
:::

⁠**Kurz gesagt:** `trap 'rm -f "$tmp"' EXIT` räumt beim Ende des Skripts auf, auch bei `exit`, Strg+C und `kill`, aber nicht bei `kill -9`.

### Das Skriptgerüst

<span class="anker" id="stufe-9-4"></span>

Die bisherigen Unterabschnitte haben einzelne Bausteine gezeigt. Zusammen ergeben sie eine feste Ordnung, nach der man robuste Skripte aufbaut. Wer ein fremdes Skript in dieser Ordnung öffnet, findet sich sofort zurecht.

:::satz Satz 9.3 (Das Skriptgerüst)
<span class="anker" id="satz-9-3"></span>

Ein robustes Skript besteht der Reihe nach aus:

<ol>

<li>

der Shebang-Zeile;

</li>

<li>

einem Kommentar mit Zweck, Aufruf und Bedeutung der Exit-Status;

</li>

<li>

den Einstellungen, etwa `set -u` und `set -o pipefail`;

</li>

<li>

festen Werten und den Funktionen, etwa einer Funktion für Fehlermeldungen;

</li>

<li>

der Prüfung der Argumente mit einem Aufrufhinweis und `exit 2`;

</li>

<li>

dem Anlegen von Zwischendateien mit `mktemp` und gleich danach `trap … EXIT`;

</li>

<li>

dem Hauptteil, in dem jeder kritische Schritt geprüft wird;

</li>

<li>

einem ausdrücklichen `exit 0` am Ende.

</li>

</ol>
:::

Das Skript `sicherung.sh` folgt diesem Gerüst. Es packt ein Verzeichnis in ein Archiv, das das Datum im Namen trägt:

```bash sicherung.sh
#!/bin/bash
# sicherung.sh: packt ein Verzeichnis in ein Archiv mit dem Datum im Namen
#   Aufruf:      sicherung.sh QUELLE ZIEL
#   Beispiel:    sicherung.sh fotos sicherungen
#   Exit-Status: 0 Sicherung angelegt, 1 Fehler, 2 falscher Aufruf

# --- Einstellungen ---
set -u
set -o pipefail

programm=$(basename "$0")

# --- Funktionen ---
fehler() {
    echo "$programm: $1" >&2
    exit 1
}

# --- Argumente prüfen ---
if [ $# -ne 2 ]; then
    echo "Aufruf: $programm QUELLE ZIEL" >&2
    exit 2
fi
quelle=$1
ziel=$2
[ -d "$quelle" ] || fehler "$quelle ist kein Verzeichnis"
[ -d "$ziel" ] || fehler "$ziel ist kein Verzeichnis"
archiv="$ziel/sicherung_$(date +%F).tar.gz"
if [ -e "$archiv" ]; then
    fehler "$archiv gibt es schon"
fi

# --- Aufräumen vorbereiten ---
tmp=$(mktemp -p "$ziel" .sicherung.XXXXXX) || fehler "keine Zwischendatei in $ziel"
trap 'rm -f "$tmp"' EXIT

# --- Hauptteil ---
tar -czf "$tmp" -C "$quelle" . || fehler "tar ist gescheitert"
mv "$tmp" "$archiv" || fehler "kann $archiv nicht anlegen"
echo "Gesichert: $archiv"
exit 0
```

Die Funktion `fehler` beendet mit ihrem `exit 1` das ganze Skript, nicht nur sich selbst, denn sie läuft in derselben Shell. Abbildung [41](#abb-41) ordnet die Zeilen den Teilen des Gerüsts zu.

:::abbildung linux/k10geruest 41
Das Skript `sicherung.sh` als helle Dateiansicht; lange Zeilen sind wie in den Code-Kästen umbrochen. Am Rand färben sich nacheinander Klammern mit den Namen der Teile: „Shebang“ (Zeile 1), „Kommentar: Zweck, Aufruf, Exit-Status“, „Einstellungen“, „feste Werte und Funktionen“, „Argumente prüfen“, „Aufräumen vorbereiten“, „Hauptteil“, „Ende: exit 0“. Zum Schluss leuchten in allen Teilen die Stellen auf, an denen das Skript ausdrücklich prüft (`|| fehler`, `if`, `exit 2`).
:::

Bevor es etwas anlegt, prüft das Skript, ob es beide Verzeichnisse gibt und ob das Archiv für heute schon existiert. Dann packt `tar` nicht gleich in das endgültige Archiv, sondern in eine versteckte Zwischendatei im Zielverzeichnis, und erst wenn `tar` Erfolg hatte, benennt `mv` sie um. Bricht der Lauf mittendrin ab, entfernt `trap` die halbfertige Zwischendatei, und unter dem richtigen Namen liegt nie ein unvollständiges Archiv. Weil Zwischendatei und Archiv im selben Dateisystem liegen, ist das Umbenennen ein einziger Schritt des Kernels ([Kapitel 3, Abschnitt 6.3](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/kopieren-verschieben-loschen.html#stufe-6-3)): Das Archiv erscheint ganz oder gar nicht. Da `mktemp` die Zwischendatei mit den Rechten 600 anlegt, darf auch das fertige Archiv nur sein Besitzer lesen; für eine Sicherung ist das erwünscht.

```console
$ mkdir sicherungen
$ chmod +x sicherung.sh
$ ./sicherung.sh fotos sicherungen
Gesichert: sicherungen/sicherung_2026-11-12.tar.gz
$ ls -A sicherungen
sicherung_2026-11-12.tar.gz
```

`ls -A` zeigt auch versteckte Dateien ([Kapitel 3, Abschnitt 3.2](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/den-inhalt-eines-verzeichnisses-anzeigen.html#stufe-3-2)); keine Zwischendatei ist übrig. Der Inhalt:

```console
$ tar -tzf sicherungen/sicherung_*.tar.gz
./
./strand 2.jpg
./berg.png
./2026/
./strand 1.jpg
./2027/
```

Ein zweiter Lauf am selben Tag, ein fehlendes Argument und eine falsche Quelle enden mit den versprochenen Exit-Status:

```console
$ ./sicherung.sh fotos sicherungen
sicherung.sh: sicherungen/sicherung_2026-11-12.tar.gz gibt es schon
$ echo $?
1
$ ./sicherung.sh fotos
Aufruf: sicherung.sh QUELLE ZIEL
$ echo $?
2
$ ./sicherung.sh gibtsnicht sicherungen
sicherung.sh: gibtsnicht ist kein Verzeichnis
$ echo $?
1
```

Abbildung [42](#abb-42) zeigt den Weg vom Verzeichnis zum Archiv.

:::abbildung linux/k10sicherung 42
Links das Verzeichnis `fotos`, rechts das Verzeichnis `sicherungen`. (1) `mktemp` legt in `sicherungen` eine graue, versteckte Datei `.sicherung.XXXXXX` an. (2) `tar` füllt sie mit dem gepackten Inhalt von `fotos`, ein Fortschrittsbalken läuft. (3) Ein Haken „tar: 0“, dann ein einziger Sprung: Die graue Datei bekommt den Namen `sicherung_2026-11-12.tar.gz` und wird farbig. Darunter ein zweiter Durchgang, der bei Schritt 2 mit einem Blitz abbricht: `trap` fegt die graue Datei weg, unter dem richtigen Namen erscheint nichts.
:::

:::hintergrund Skripte zu festen Zeiten starten
Eine Sicherung nützt am meisten, wenn sie von selbst läuft. Unter Linux gibt es dafür zwei Wege. Der ältere ist der Dienst `cron`. Jeder Benutzer hat eine Tabelle, die er mit `crontab -e` bearbeitet und mit `crontab -l` anzeigt. Eine Zeile wie `30 2 * * * /home/student/bin/sicherung.sh /home/student/fotos /home/student/sicherungen` bedeutet: Minute 30, Stunde 2, an jedem Tag des Monats, in jedem Monat, an jedem Wochentag, also täglich um 2:30 Uhr. Der neuere Weg sind Timer-Units von systemd, die [Kapitel 9, Abschnitt 8.4](/wissen/informatik/linux-und-kommandozeile/software-installieren-paketverwaltung/aktualisieren-als-schutz.html#stufe-8-4) bei den automatischen Updates gezeigt hat: Eine Datei `name.timer` legt mit `OnCalendar=` fest, wann die gleichnamige `name.service` startet, und mit `Persistent=true` holt systemd einen Lauf nach, den der Rechner im ausgeschalteten Zustand verpasst hat.

Beide starten das Skript ohne Terminal und nicht aus einer Anmelde-Shell. `cron` benutzt `/bin/sh` und eine sehr knappe Umgebung; die Startdatei `~/.bashrc` wird nicht gelesen, Aliase und eigene Einträge im Suchpfad fehlen. Ausgaben schickt `cron` als E-Mail an den Besitzer der Tabelle, sofern auf dem Rechner E-Mail eingerichtet ist, sonst gehen sie verloren. Ein Skript für den Zeitplan braucht deshalb eine Shebang-Zeile, absolute Pfade, eine Umleitung seiner Ausgaben in eine Protokolldatei und vor allem verlässliche Exit-Status, denn niemand sieht ihm zu. Genau dafür ist das Gerüst dieses Unterabschnitts gemacht.
:::

⁠**Kurz gesagt:** Shebang, Kommentar, Einstellungen, Funktionen, Argumentprüfung, `mktemp` mit `trap`, geprüfter Hauptteil und `exit 0` ergeben ein Skript, das man auch unbeaufsichtigt laufen lassen kann.

:::aufgabe Aufgabe 32 ★ Zwei Läufe gleichzeitig
<span class="anker" id="aufg-32"></span>

Zwei Kopien eines Skripts laufen gleichzeitig. Beide schreiben Zwischenergebnisse nach `/tmp/zwischen.txt`. Was kann schiefgehen? Warum passiert das mit `mktemp` nicht, und welche Rechte hat die Datei, die `mktemp` anlegt?

:::loesung
Beide Kopien lesen und schreiben dieselbe Datei; was die eine schreibt, überschreibt die andere oder mischt sich hinein, und jede liest am Ende womöglich die Zwischenergebnisse der anderen. Räumt eine Kopie die Datei weg, verschwindet sie auch für die andere. `mktemp` gibt jedem Lauf eine eigene, neu angelegte Datei mit einem zufälligen Namen; zwei Läufe kommen sich nicht in die Quere. Die Datei hat die Rechte `rw-------` (600): Nur ihr Besitzer kann sie lesen und schreiben, auch wenn sie im gemeinsamen Verzeichnis `/tmp` liegt.
:::
:::

:::aufgabe Aufgabe 33 ★★ Die Sicherung prüfen
<span class="anker" id="aufg-33"></span>

Erweitere `sicherung.sh`: Bevor `mv` die Zwischendatei umbenennt, soll `tar -tzf` sie einmal lesen; scheitert das, endet das Skript über `fehler`. Gib nach dem Umbenennen zusätzlich die Größe des Archivs mit `du -h` aus. Teste das Skript mit einem neuen Zielverzeichnis.

:::loesung
Zwei Zeilen ändern sich im Hauptteil. `tar -tzf` liest das ganze Archiv; seine Ausgabe interessiert nicht und geht nach `/dev/null`, nur der Exit-Status zählt. `du -h` gibt die Größe vor einem Tabulator aus, und `cut -f 1` schneidet sie ab ([Kapitel 6, Abschnitt 2.1](/wissen/informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke/spalten-ausschneiden-und-zeichen-ersetzen-cut-tr-und-paste.html#stufe-2-1)):

```bash sicherung.sh
#!/bin/bash
# sicherung.sh: packt ein Verzeichnis in ein Archiv mit dem Datum im Namen
#   Aufruf:      sicherung.sh QUELLE ZIEL
#   Beispiel:    sicherung.sh fotos sicherungen
#   Exit-Status: 0 Sicherung angelegt, 1 Fehler, 2 falscher Aufruf

# --- Einstellungen ---
set -u
set -o pipefail

programm=$(basename "$0")

# --- Funktionen ---
fehler() {
    echo "$programm: $1" >&2
    exit 1
}

# --- Argumente prüfen ---
if [ $# -ne 2 ]; then
    echo "Aufruf: $programm QUELLE ZIEL" >&2
    exit 2
fi
quelle=$1
ziel=$2
[ -d "$quelle" ] || fehler "$quelle ist kein Verzeichnis"
[ -d "$ziel" ] || fehler "$ziel ist kein Verzeichnis"
archiv="$ziel/sicherung_$(date +%F).tar.gz"
if [ -e "$archiv" ]; then
    fehler "$archiv gibt es schon"
fi

# --- Aufräumen vorbereiten ---
tmp=$(mktemp -p "$ziel" .sicherung.XXXXXX) || fehler "keine Zwischendatei in $ziel"
trap 'rm -f "$tmp"' EXIT

# --- Hauptteil ---
tar -czf "$tmp" -C "$quelle" . || fehler "tar ist gescheitert"
tar -tzf "$tmp" > /dev/null || fehler "das Archiv lässt sich nicht lesen"
mv "$tmp" "$archiv" || fehler "kann $archiv nicht anlegen"
echo "Gesichert: $archiv ($(du -h "$archiv" | cut -f 1))"
exit 0
```

```console
$ chmod +x sicherung.sh
$ mkdir sicherungen2
$ ./sicherung.sh fotos sicherungen2
Gesichert: sicherungen2/sicherung_2026-11-13.tar.gz (4.0K)
$ ls -A sicherungen2
sicherung_2026-11-13.tar.gz
```

Der Test lief einen Tag nach dem Kapitel, daher das andere Datum. `du` zählt belegte Blöcke zu 4 KiB, das Archiv selbst ist kleiner ([Kapitel 3, Abschnitt 10.7](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-finden-und-platz-messen.html#stufe-10-7)).
:::
:::

:::aufgabe Aufgabe 34 ★★★ Wenn `kill -9` zuschlägt
<span class="anker" id="aufg-34"></span>

Angenommen, `sicherung.sh` wird mit `kill -9` beendet, während `tar` läuft. Was bleibt im Zielverzeichnis zurück, was nicht? Warum entsteht nie ein unvollständiges Archiv unter dem Namen `sicherung_….tar.gz`? Was würde passieren, wenn das Skript `tar` direkt in `$archiv` schreiben ließe?

:::loesung
`kill -9` beendet die bash sofort; `trap` läuft nicht mehr ([Kapitel 8, Abschnitt 4.5](/wissen/informatik/linux-und-kommandozeile/prozesse-signale-und-dienste/signale.html#stufe-4-5)). Im Zielverzeichnis bleibt die versteckte Zwischendatei `.sicherung.XXXXXX` liegen. Trifft das Signal nur die bash, etwa `kill -9` mit ihrer Prozessnummer, schreibt `tar` die Datei noch zu Ende; trifft es mit `kill -9 %1` alle Prozesse des Jobs, bricht auch `tar` ab, und die Datei enthält ein halbes Archiv. Ein Archiv unter dem Namen `sicherung_….tar.gz` entsteht aber nicht, denn diesen Namen bekommt die Datei erst durch `mv`, und das läuft nur nach einem erfolgreichen `tar`. Schriebe `tar` direkt nach `$archiv`, läge nach dem Abbruch unter dem richtigen Namen ein unvollständiges Archiv. Ein späterer Lauf am selben Tag würde es mit „gibt es schon“ verweigern, und wer es öffnet, hielte es für eine gültige Sicherung. Die liegengebliebene Zwischendatei findet man mit `ls -A` und löscht sie von Hand.
:::
:::

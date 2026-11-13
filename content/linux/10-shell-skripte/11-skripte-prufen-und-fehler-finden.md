---
title: Skripte prüfen und Fehler finden
pfad: Informatik / Linux und Kommandozeile / Shell-Skripte
adresse: informatik/linux-und-kommandozeile/shell-skripte
knoten: Kapitel 10: Shell-Skripte
order: 6151100
summary: Ein Skript kann an seiner Schreibweise scheitern, an einem falschen Ablauf oder an einer Falle, die erst bei einem bestimmten Dateinamen zuschnappt.
tags: bash -n skript, bash -x skript, ShellCheck, Probelauf, Testfall
lang: de
---

<span class="anker" id="stufe-10"></span>

:::zweck
Ein Skript kann an seiner Schreibweise scheitern, an einem falschen Ablauf oder an einer Falle, die erst bei einem bestimmten Dateinamen zuschnappt. Dieser Abschnitt zeigt vier Werkzeuge dagegen: die Syntaxprüfung der bash, die Ablaufverfolgung, das Prüfprogramm ShellCheck und Probeläufe mit festen Testfällen.
:::

### Die Syntax prüfen: `bash -n`

<span class="anker" id="stufe-10-1"></span>

Ein vergessenes `fi` oder ein fehlendes Anführungszeichen fällt oft erst auf, wenn das Skript schon halb gelaufen ist. Man kann die bash ein Skript lesen lassen, ohne dass sie etwas ausführt.

:::definition Definition 10.1 (`bash -n`)
<span class="anker" id="satz-10-1"></span>

__`bash -n skript`__ liest das Skript vollständig und prüft, ob es den Regeln der Shell-Sprache entspricht, führt aber keinen Befehl aus. Bei einem Syntaxfehler meldet es die Zeile, an der es den Fehler bemerkt hat, und endet mit dem Status 2; sonst mit 0.
:::

```bash kaputt.sh
#!/bin/bash
# kaputt.sh: ein Skript mit einem Syntaxfehler
for datei in "$@"; do
    if [ -f "$datei" ]; then
        echo "$datei: eine Datei"
done
```

```console
$ bash -n kaputt.sh
kaputt.sh: line 6: syntax error near unexpected token `done'
kaputt.sh: line 6: `done'
$ echo $?
2
$ bash -n zaehle.sh
$ echo $?
0
```

Der Fehler ist das fehlende `fi` nach Zeile 5, gemeldet wird Zeile 6: Erst bei `done` merkt die bash, dass ein `if` noch offen ist, denn bis dahin hätte noch ein `fi` kommen können. Eine Fehlermeldung zeigt also, wo die Shell aufgeben musste, nicht unbedingt, wo der Fehler sitzt; die Ursache steht oft weiter oben. Abbildung [43](#abb-43) zeigt die Meldung im Terminal.

:::abbildung linux/k10bashn 43
Oben das dunkle Terminal mit `bash -n kaputt.sh` und den beiden Meldezeilen. Darunter die helle Dateiansicht von `kaputt.sh`: Ein Pfeil führt von der Meldung zu `done` in Zeile 6, eine gestrichelte rote Linie markiert die Lücke nach Zeile 5, wo das `fi` fehlt; links die Klammern von `for` und `if`, die von `if` bleibt offen.
:::

⁠**Kurz gesagt:** `bash -n skript` prüft die Schreibweise, ohne etwas auszuführen; die gemeldete Zeile ist die, an der die Shell aufgeben musste.

### Den Ablauf verfolgen: `bash -x`

<span class="anker" id="stufe-10-2"></span>

Ist die Schreibweise in Ordnung, tut das Skript aber etwas anderes als gedacht, will man sehen, welche Befehle wirklich laufen und welche Werte die Variablen dabei haben.

:::definition Definition 10.2 (`bash -x` und `set -x`)
<span class="anker" id="satz-10-2"></span>

__`bash -x skript`__ führt das Skript aus und schreibt vor jedem Befehl eine Zeile auf die Fehlerausgabe, die den Befehl nach der Expansion zeigt, mit einem `+` davor. `set -x` schaltet diese Ablaufverfolgung innerhalb eines Skripts oder der Befehlszeile ein, `set +x` wieder aus.
:::

```console
$ bash -x bewertung.sh 80
+ punkte=80
+ ist_zahl 80
+ [[ 80 =~ ^[0-9]+$ ]]
+ ((  punkte > 100  ))
+ ((  punkte >= 90  ))
+ ((  punkte >= 75  ))
+ echo gut
gut
```

Man sieht den Weg durch die Verzweigung: Die Prüfungen auf 100 und 90 scheitern, die auf 75 trifft. In der Befehlszeile:

```console
$ set -x
$ echo "Hallo, $USER"
+ echo 'Hallo, student'
Hallo, student
$ set +x
+ set +x
```

Die Zeile nach dem `+` zeigt die Wörter so, wie das Programm sie bekommt: `$USER` ist eingesetzt, und einfache Anführungszeichen markieren, was ein einzelnes Argument ist. Damit sieht man genau die Wörter, um die es in [Kapitel 5](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/expansion-quoting-variablen-und-umgebung.html) ging. Das Zeichen `+` steht in der Variablen `PS4`; mit `PS4='+ Zeile $LINENO: '` zeigt jede Zeile zusätzlich ihre Zeilennummer im Skript. Abbildung [44](#abb-44) ordnet die Spur dem Skript zu.

:::abbildung linux/k10bashx 44
Oben die helle Dateiansicht von `bewertung.sh`, darunter das dunkle Terminal mit `bash -x bewertung.sh 80`. Zu jeder Spurzeile unten (`+ punkte=80`, `+ ist_zahl 80`, …, `+ echo gut`) leuchtet oben die Zeile auf, aus der sie stammt; Nummern 1 bis 7 ordnen Spurzeilen und Zeilen einander zu. Zum Schluss werden die übersprungenen Zweige (`exit 2`, `sehr gut`, `bestanden`, `nicht bestanden`) grau.
:::

⁠**Kurz gesagt:** `bash -x` zeigt jeden ausgeführten Befehl mit den Wörtern, die er nach der Expansion bekommt.

### Typische Fehler finden: ShellCheck

<span class="anker" id="stufe-10-3"></span>

Viele Fehler dieses Kapitels fallen erst bei bestimmten Daten auf, etwa bei einem Dateinamen mit Leerzeichen. Ein Skript kann hundertmal fehlerfrei laufen und beim nächsten Mal Unsinn machen. Lege zwei Textdateien an, eine mit Leerzeichen im Namen:

```console
$ mkdir texte
$ echo "Hallo Welt" > texte/gruss.txt
$ echo "Liebe Oma, danke für das Paket." > "texte/mein brief.txt"
```

Das folgende Skript soll die Wörter aller Textdateien eines Verzeichnisses zählen. Es enthält gleich mehrere Fehler:

```bash fehlerhaft.sh
#!/bin/bash
# fehlerhaft.sh: zählt die Wörter aller Textdateien in einem Verzeichnis
cd $1
for datei in $(ls *.txt); do
    woerter=$(wc -w < $datei)
    echo "$datei: $woerter Wörter"
    gesamt=$(( gesamt + woerter ))
done
echo "Zusammen: $gesamt Wörter in $verzeichnis"
```

```console
$ bash fehlerhaft.sh texte
gruss.txt: 2 Wörter
fehlerhaft.sh: line 5: mein: No such file or directory
mein:  Wörter
fehlerhaft.sh: line 5: brief.txt: No such file or directory
brief.txt:  Wörter
Zusammen: 2 Wörter in
```

:::definition Definition 10.3 (ShellCheck)
<span class="anker" id="satz-10-3"></span>

__ShellCheck__ ist ein Programm, das ein Shell-Skript liest, ohne es auszuführen, und es mit einer Sammlung bekannter Fehlermuster vergleicht. Jede Meldung zeigt die Stelle, eine Nummer der Form `SC2086`, eine Einstufung (`error`, `warning`, `info` oder `style`) und einen kurzen Text; zu jeder Nummer gibt es eine Seite mit Erklärung und Abhilfe. Findet es etwas, endet es mit dem Status 1.
:::

Ein Programm, das Quelltext untersucht, ohne ihn laufen zu lassen, nennt man ein Werkzeug zur statischen Analyse. Welche Shell-Sprache gemeint ist, liest ShellCheck aus der Shebang-Zeile.

```console
$ shellcheck fehlerhaft.sh

In fehlerhaft.sh line 3:
cd $1
^---^ SC2164 (warning): Use 'cd ... || exit' or 'cd ... || return' in case cd fails.
   ^-- SC2086 (info): Double quote to prevent globbing and word splitting.

Did you mean:
cd "$1" || exit


In fehlerhaft.sh line 4:
for datei in $(ls *.txt); do
             ^---------^ SC2045 (error): Iterating over ls output is fragile. Use globs.
                  ^-- SC2035 (info): Use ./*glob* or -- *glob* so names with dashes won't become options.


In fehlerhaft.sh line 5:
    woerter=$(wc -w < $datei)
                      ^----^ SC2086 (info): Double quote to prevent globbing and word splitting.

Did you mean:
    woerter=$(wc -w < "$datei")


In fehlerhaft.sh line 9:
echo "Zusammen: $gesamt Wörter in $verzeichnis"
                                  ^----------^ SC2154 (warning): verzeichnis is referenced but not assigned.

For more information:
  https://www.shellcheck.net/wiki/SC2045 -- Iterating over ls output is fragi...
  https://www.shellcheck.net/wiki/SC2154 -- verzeichnis is referenced but not...
  https://www.shellcheck.net/wiki/SC2164 -- Use 'cd ... || exit' or 'cd ... |...
$ echo $?
1
```

Jede Meldung entspricht einer Regel dieses Kapitels: `cd` ohne Prüfung (Abschnitt [8.3](fehler-erkennen-und-melden.html#stufe-8-3)), Variablen ohne Anführungszeichen (Abschnitt [3.5](verzweigen-if-und-test.html#stufe-3-5)), eine Schleife über die Ausgabe von `ls` (Abschnitt [5.2](schleifen-for-und-while.html#stufe-5-2)), ein Muster, dessen Treffer mit einem Strich beginnen und dann als Option gelten könnten, und eine Variable, die nie belegt wird, hier ein vergessenes `verzeichnis=$1`. Auch die Pipe-Falle kennt ShellCheck: Für die fehlerhafte `minuten.sh` aus Abschnitt [6.4](zeilen-lesen-und-listen-speichern.html#stufe-6-4) meldet es, dass `summe` nur im Kindprozess der Pipeline verändert wird (SC2030 und SC2031). Die verbesserte Fassung:

```bash woerter.sh
#!/bin/bash
# woerter.sh: zählt die Wörter aller Textdateien in einem Verzeichnis
verzeichnis=$1
cd "$verzeichnis" || exit 1
gesamt=0
for datei in ./*.txt; do
    [ -f "$datei" ] || continue
    woerter=$(wc -w < "$datei")
    echo "$datei: $woerter Wörter"
    gesamt=$(( gesamt + woerter ))
done
echo "Zusammen: $gesamt Wörter in $verzeichnis"
```

```console
$ shellcheck woerter.sh
$ echo $?
0
$ bash woerter.sh texte
./gruss.txt: 2 Wörter
./mein brief.txt: 6 Wörter
Zusammen: 8 Wörter in texte
```

`[ -f "$datei" ] `| continue| fängt den Fall ab, dass das Muster nichts findet und als Text stehen bleibt. ShellCheck ist auf dem Testsystem schon installiert; sonst installiert man es mit `sudo apt install shellcheck` ([Kapitel 9, Abschnitt 6.3](/wissen/informatik/linux-und-kommandozeile/software-installieren-paketverwaltung/installieren-entfernen-aktualisieren.html#stufe-6-3)), und unter [https://www.shellcheck.net](https://www.shellcheck.net) gibt es dieselbe Prüfung im Browser. Abbildung [45](#abb-45) hebt die Meldungen hervor.

:::abbildung linux/k10shellcheck 45
Das dunkle Terminal mit dem Anfang der Ausgabe von `shellcheck fehlerhaft.sh`. Nacheinander leuchten die Meldungen auf; zu jeder erscheint am Rand ein kleines Etikett mit der passenden Regel aus dem Kapitel: SC2164 „`cd` prüfen“, SC2086 „Anführungszeichen“, SC2045 „keine Schleife über `ls`“, SC2035 „`./*` vor Mustern“, SC2154 „Variable nie belegt“. Die Einstufungen `error`, `warning` und `info` sind farbig unterschieden.
:::

:::hintergrund Wenn ShellCheck sich irrt
ShellCheck kennt die Absicht nicht. In `alle.sh` aus Abschnitt [2.4](argumente-ubergeben-positionsparameter.html#stufe-2-4) steht `$*` absichtlich ohne Anführungszeichen, um den Fehler vorzuführen, und ShellCheck meldet ihn trotzdem. Will man eine Meldung an einer Stelle bewusst hinnehmen, schreibt man direkt darüber einen Kommentar der Form `# shellcheck disable=SC2048`; ShellCheck schweigt dann für den folgenden Befehl. Mit `shellcheck -S warning skript` zeigt es nur Meldungen ab der Einstufung `warning`. Eine Meldung abzuschalten, statt den Fehler zu verstehen, ist allerdings selten die richtige Wahl.
:::

⁠**Kurz gesagt:** `shellcheck skript` findet typische Fehler wie fehlende Anführungszeichen, ungeprüftes `cd` und Schleifen über `ls`, bevor sie bei bestimmten Daten zuschlagen.

### Der Probelauf mit `echo`

<span class="anker" id="stufe-10-4"></span>

Ein Skript, das löscht, verschiebt oder überschreibt, testet man ungern echt. Man möchte erst sehen, welche Befehle es ausführen würde.

:::definition Definition 10.4 (Probelauf)
<span class="anker" id="satz-10-4"></span>

Ein __Probelauf__ ist ein Lauf, in dem vor jedem verändernden Befehl `echo` steht. Das Skript gibt den Befehl dann mit allen eingesetzten Wörtern aus, statt ihn auszuführen.
:::

In `loesche.sh` wird dafür nur eine Zeile geändert; ein Kommentar markiert sie, damit man sie nach dem Test wiederfindet:

```bash loesche.sh
#!/bin/bash
# loesche.sh: Probelauf, zeigt den Löschbefehl nur an
if ! cd "$1"; then
    echo "loesche.sh: kann nicht nach '$1' wechseln, lösche nichts" >&2
    exit 1
fi
echo rm -f -- *.tmp    # PROBELAUF: echo vor rm
echo "Aufgeräumt in $PWD"
```

```console
$ touch alt/c.tmp alt/d.tmp
$ ./loesche.sh alt
rm -f -- c.tmp d.tmp
Aufgeräumt in /home/student/linuxk10/alt
$ ls alt
c.tmp  d.tmp
```

Die Ausgabe zeigt den fertigen Befehl, nachdem die Pfadnamen-Erweiterung `*.tmp` ersetzt hat; die Dateien sind noch da. Danach entfernt man das `echo` wieder. Abbildung [46](#abb-46) vergleicht beide Läufe.

:::abbildung linux/k10probelauf 46
Zwei Durchgänge durch dieselbe Zeile. Oben „Probelauf“: Die Zeile `echo rm -f -- *.tmp` wird zu `echo rm -f -- c.tmp d.tmp` expandiert; `echo` hält den fertigen Befehl wie ein Plakat hoch, die Dateien `c.tmp` und `d.tmp` im Verzeichnis `alt` bleiben stehen. Unten „echter Lauf“ ohne `echo`: Derselbe expandierte Befehl geht an `rm`, die beiden Dateien verschwinden.
:::

⁠**Kurz gesagt:** Ein `echo` vor einem gefährlichen Befehl zeigt ihn mit allen eingesetzten Wörtern, ohne ihn auszuführen.

### Testfälle

<span class="anker" id="stufe-10-5"></span>

Probieren von Hand prüft meist nur die Fälle, an die man ohnehin gedacht hat. Systematisch wird es, wenn man vorher aufschreibt, was bei welcher Eingabe herauskommen muss, und das automatisch vergleicht.

:::definition Definition 10.5 (Testfall)
<span class="anker" id="satz-10-5"></span>

Ein __Testfall__ ist eine Eingabe zusammen mit dem Ergebnis, das ein Programm bei dieser Eingabe liefern muss. Gute Testfälle decken gewöhnliche Eingaben ab, die Grenzen zwischen zwei Ergebnissen und ungültige Eingaben.
:::

Für `bewertung.sh` liegen die Grenzen bei 90, 75 und 50: 90 muss „sehr gut“ sein, 89 schon „gut“, und genauso gehört an die beiden anderen Grenzen je ein Wert darauf und einer knapp darunter. Ungültig sind etwa 101, `abc` und eine leere Eingabe; dort soll das Skript nichts auf die Standardausgabe schreiben. Ein kleines Testskript ruft das zu prüfende Skript mit jedem Fall auf und vergleicht; mit einem Argument prüft es ein anderes Skript als `./bewertung.sh`:

```bash teste_bewertung.sh
#!/bin/bash
# teste_bewertung.sh: prüft bewertung.sh mit festen Testfällen
#   Aufruf: teste_bewertung.sh [SKRIPT]   (ohne Argument: ./bewertung.sh)
skript=./bewertung.sh
if [ $# -gt 0 ]; then
    skript=$1
fi
fehler=0

pruefe() {
    local erwartet=$1 eingabe=$2 ergebnis
    ergebnis=$("$skript" "$eingabe" 2> /dev/null)
    if [ "$ergebnis" = "$erwartet" ]; then
        echo "ok      $eingabe -> $ergebnis"
    else
        echo "FEHLER  $eingabe -> '$ergebnis', erwartet '$erwartet'"
        fehler=$(( fehler + 1 ))
    fi
}

pruefe "sehr gut" 100
pruefe "sehr gut" 90
pruefe "gut" 89
pruefe "gut" 75
pruefe "bestanden" 74
pruefe "bestanden" 50
pruefe "nicht bestanden" 49
pruefe "nicht bestanden" 0
pruefe "" 101
pruefe "" abc
pruefe "" ""
echo "$fehler Fehler"
[ "$fehler" -eq 0 ]
```

Die letzte Zeile macht aus dem Ergebnis den Exit-Status des Testskripts. Mit der alten Fassung aus Abschnitt [4.3](bequemer-prufen-und-case.html#stufe-4-3), die Abschnitt [7.4](funktionen.html#stufe-7-4) als `bewertung_alt.sh` aufgehoben hat, und mit der neuen:

```console
$ chmod +x teste_bewertung.sh
$ ./teste_bewertung.sh ./bewertung_alt.sh
ok      100 -> sehr gut
ok      90 -> sehr gut
ok      89 -> gut
ok      75 -> gut
ok      74 -> bestanden
ok      50 -> bestanden
ok      49 -> nicht bestanden
ok      0 -> nicht bestanden
FEHLER  101 -> 'sehr gut', erwartet ''
FEHLER  abc -> 'nicht bestanden', erwartet ''
FEHLER   -> 'nicht bestanden', erwartet ''
3 Fehler
$ echo $?
1
$ ./teste_bewertung.sh
ok      100 -> sehr gut
ok      90 -> sehr gut
ok      89 -> gut
ok      75 -> gut
ok      74 -> bestanden
ok      50 -> bestanden
ok      49 -> nicht bestanden
ok      0 -> nicht bestanden
ok      101 ->
ok      abc ->
ok       ->
0 Fehler
$ echo $?
0
```

Die alte Fassung rechnet mit allen gültigen Punkten richtig und fällt nur bei den ungültigen durch, genau die Fälle, die man beim Ausprobieren gern vergisst. Nach jeder Änderung an `bewertung.sh` genügt ein Aufruf des Testskripts, um zu sehen, ob noch alles stimmt. Abbildung [47](#abb-47) zeigt die Tabelle der Fälle.

:::abbildung linux/k10testfaelle 47
Eine Tabelle mit elf Zeilen „Eingabe – erwartet“: 100, 90, 89, 75, 74, 50, 49, 0, 101, `abc`, leer. Auf einem Zahlenstrahl von 0 bis 100 sind die Grenzen 50, 75, 90 markiert; die Testwerte 89/90, 74/75 und 49/50 sitzen genau beiderseits der Grenzen, 101 und `abc` außerhalb. Zwei Spalten mit Ergebnissen füllen sich nacheinander: für `bewertung_alt.sh` acht grüne Haken und drei rote Kreuze, für `bewertung.sh` elf grüne Haken.
:::

:::hintergrund Eine Lücke, die auch diese Testfälle übersehen
Auch die neue Fassung hat noch eine Lücke, und keiner der elf Fälle trifft sie: Zahlen mit einer führenden Null. `ist_zahl` lässt `0100` durch, denn es besteht nur aus Ziffern. Die Arithmetik der bash liest eine Zahl, die mit `0` beginnt, aber in der Oktalschreibweise ([Kapitel 7, Abschnitt 3.3](/wissen/informatik/linux-und-kommandozeile/benutzer-gruppen-und-rechte/rechte-andern-chmod.html#stufe-3-3)), und dort ist `0100` gleich 64:

```console
$ echo $(( 0100 ))
64
$ ./bewertung.sh 0100
bestanden
$ ./bewertung.sh 08 2> /dev/null
nicht bestanden
```

Bei `08` meldet die bash zusätzlich viermal den Fehler `value too great for base` auf der Fehlerausgabe, denn 8 ist keine Ziffer der Oktalschreibweise; das Skript endet trotzdem mit „nicht bestanden“ und dem Status 0. Abhilfe schafft ein strengerer Ausdruck in `ist_zahl`, `^(0|[1-9][0-9]*)$`, der eine führende Null nur für die Zahl 0 selbst erlaubt ([Kapitel 6, Abschnitt 7.4](/wissen/informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke/regulare-ausdrucke-wiederholungen-gruppen-und-alternativen.html#stufe-7-4)). Oder man schreibt in der Arithmetik `10#$punkte`; die Vorsilbe `10#` liest die Ziffern ausdrücklich im Dezimalsystem. Ob `0100` abgelehnt oder als 100 gelesen werden soll, muss man vorher festlegen, und genau dazu zwingt ein weiterer Testfall wie `pruefe "" 0100`.
:::

⁠**Kurz gesagt:** Testfälle halten vorher fest, was bei gewöhnlichen, grenznahen und ungültigen Eingaben herauskommen muss; ein Testskript vergleicht das nach jeder Änderung.

### Aufräumen

<span class="anker" id="stufe-10-6"></span>

Alle Übungen dieses Kapitels liefen im Übungsverzeichnis. Wenn du die Aufgaben erledigt hast, entfernst du es samt Inhalt; `cd` ohne Argument wechselt vorher ins Heimatverzeichnis, damit du nicht im zu löschenden Verzeichnis stehst:

```console
$ cd
$ rm -r ~/linuxk10
```

Skripte, die du behalten willst, kopierst du vorher nach `~/.local/bin` (Abschnitt [1.8](vom-befehl-zum-skript.html#stufe-1-8)). Die Änderung an `PATH` aus diesem Kapitel galt nur für die damalige Shell und ist mit ihr verschwunden.

:::aufgabe Aufgabe 35 ★★ ShellCheck auf eigene Skripte
<span class="anker" id="aufg-35"></span>

Lass ShellCheck über `alle.sh`, `sparen.sh` und die erste Fassung von `zaehle.sh` mit `$*` laufen. Welche Meldungen kommen, und welche davon zeigen einen echten Fehler? Verbessere `sparen.sh`, falls ShellCheck etwas findet.

:::loesung
```console
$ shellcheck alle.sh

In alle.sh line 6:
printf '  [%s]\n' $*
                  ^-- SC2048 (warning): Use "$@" (with quotes) to prevent whitespace problems.
                  ^-- SC2086 (info): Double quote to prevent globbing and word splitting.

Did you mean:
printf '  [%s]\n' "$*"

For more information:
  https://www.shellcheck.net/wiki/SC2048 -- Use "$@" (with quotes) to prevent...
  https://www.shellcheck.net/wiki/SC2086 -- Double quote to prevent globbing ...
$ shellcheck sparen.sh
$ shellcheck zaehle_alt.sh

In zaehle_alt.sh line 3:
wc -l $*
      ^-- SC2048 (warning): Use "$@" (with quotes) to prevent whitespace problems.
      ^-- SC2086 (info): Double quote to prevent globbing and word splitting.

Did you mean:
wc -l "$*"

For more information:
  https://www.shellcheck.net/wiki/SC2048 -- Use "$@" (with quotes) to prevent...
  https://www.shellcheck.net/wiki/SC2086 -- Double quote to prevent globbing ...
```

Hier liegt die erste Fassung mit `$*` als `zaehle_alt.sh`. Bei `alle.sh` ist die Meldung gewollt, das Skript führt den Fehler absichtlich vor; ein Kommentar `# shellcheck disable=SC2048,SC2086` über der Zeile würde sie abstellen. Bei `zaehle_alt.sh` ist es ein echter Fehler, Abschnitt [2.4](argumente-ubergeben-positionsparameter.html#stufe-2-4) hat ihn gezeigt. Achtung: Der Vorschlag „Did you mean“ schlägt `"$*"` vor, richtig ist hier aber `"$@"`, wie der Text von SC2048 sagt; `"$*"` würde alle Namen zu einem einzigen Argument verkleben. `sparen.sh` ist ohne Befund.
:::
:::

:::aufgabe Aufgabe 36 ★★ Einen Fehler mit `bash -x` finden
<span class="anker" id="aufg-36"></span>

Das folgende Skript soll den Durchschnitt seiner Argumente ausgeben, liefert für `2 4 6` aber 3 statt 4. Finde den Fehler mit `bash -x` und verbessere ihn.

```bash durchschnitt.sh
#!/bin/bash
# durchschnitt.sh: Durchschnitt ganzer Zahlen (fehlerhaft)
summe=0
anzahl=1
for zahl in "$@"; do
    summe=$(( summe + zahl ))
    anzahl=$(( anzahl + 1 ))
done
echo $(( summe / anzahl ))
```

:::loesung
```console
$ bash durchschnitt.sh 2 4 6
3
$ bash -x durchschnitt.sh 2 4 6
+ summe=0
+ anzahl=1
+ for zahl in "$@"
+ summe=2
+ anzahl=2
+ for zahl in "$@"
+ summe=6
+ anzahl=3
+ for zahl in "$@"
+ summe=12
+ anzahl=4
+ echo 3
3
```

Die Spur zeigt: Nach drei Zahlen steht `anzahl` auf 4, weil sie bei 1 statt bei 0 beginnt; $12/4=3$. Die Verbesserung setzt `anzahl=0` und fängt den Aufruf ohne Zahlen ab, der sonst durch null teilen würde:

```bash durchschnitt.sh
#!/bin/bash
# durchschnitt.sh: Durchschnitt ganzer Zahlen
if [ $# -eq 0 ]; then
    echo "Aufruf: durchschnitt.sh ZAHL..." >&2
    exit 2
fi
summe=0
anzahl=0
for zahl in "$@"; do
    summe=$(( summe + zahl ))
    anzahl=$(( anzahl + 1 ))
done
echo $(( summe / anzahl ))
```

```console
$ bash durchschnitt.sh 2 4 6
4
$ bash durchschnitt.sh 7 8
7
```

Bei `7 8` wäre der Durchschnitt 7,5; die ganzzahlige Teilung schneidet ab. Mit der Variablen `PS4` zeigt die Spur zusätzlich die Zeilennummern im Skript:

```console
$ PS4='+ Zeile $LINENO: ' bash -x durchschnitt.sh 7 8
+ Zeile 3: '[' 2 -eq 0 ']'
+ Zeile 7: summe=0
+ Zeile 8: anzahl=0
+ Zeile 9: for zahl in "$@"
+ Zeile 10: summe=7
+ Zeile 11: anzahl=1
+ Zeile 9: for zahl in "$@"
+ Zeile 10: summe=15
+ Zeile 11: anzahl=2
+ Zeile 13: echo 7
7
```
:::
:::

:::aufgabe Aufgabe 37 ★★★ Testfälle für zaehle.sh
<span class="anker" id="aufg-37"></span>

Schreibe ein Testskript `teste_zaehle.sh`, das die fertige `zaehle.sh` mit vier Fällen aufruft und jeweils nur den Exit-Status mit dem erwarteten vergleicht: keine Argumente (2), eine vorhandene Datei (0), eine fehlende Datei (1), eine vorhandene und eine fehlende (1). Die Ausgaben von `zaehle.sh` sollen dabei nicht erscheinen.

:::loesung
Die Funktion `erwarte` bekommt den erwarteten Status und danach die Argumente für `zaehle.sh`. `shift` entfernt den erwarteten Status, so dass `"$@"` nur noch die Argumente enthält. Beide Ausgaben von `zaehle.sh` gehen nach `/dev/null`, und `$?` wird sofort in `ist` gesichert:

```bash teste_zaehle.sh
#!/bin/bash
# teste_zaehle.sh: prüft die Exit-Status von zaehle.sh
fehler=0

erwarte() {
    local soll=$1 ist
    shift
    ./zaehle.sh "$@" > /dev/null 2>&1
    ist=$?
    if [ "$ist" -eq "$soll" ]; then
        echo "ok      zaehle.sh $* -> $ist"
    else
        echo "FEHLER  zaehle.sh $* -> $ist, erwartet $soll"
        fehler=$(( fehler + 1 ))
    fi
}

erwarte 2
erwarte 0 einkauf.txt
erwarte 1 gibtsnicht.txt
erwarte 1 einkauf.txt gibtsnicht.txt
echo "$fehler Fehler"
[ "$fehler" -eq 0 ]
```

```console
$ chmod +x teste_zaehle.sh
$ ./teste_zaehle.sh
ok      zaehle.sh  -> 2
ok      zaehle.sh einkauf.txt -> 0
ok      zaehle.sh gibtsnicht.txt -> 1
ok      zaehle.sh einkauf.txt gibtsnicht.txt -> 1
0 Fehler
$ echo $?
0
```

In der Meldung steht `$*`, denn dort sollen die Argumente bewusst zu einem Text verbunden werden (Abschnitt [2.5](argumente-ubergeben-positionsparameter.html#stufe-2-5)). Hier passt auch die Vorlage aus `teste_bewertung.sh` nicht ganz, denn dort wurde die Ausgabe verglichen, hier der Status; beide Testskripte enden selbst mit 0 nur dann, wenn kein Fall gescheitert ist.
:::
:::

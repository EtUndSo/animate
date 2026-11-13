---
title: Bequemer prüfen: `[[ ]]`, `(( ))` und `case`
pfad: Informatik / Linux und Kommandozeile / Shell-Skripte
adresse: informatik/linux-und-kommandozeile/shell-skripte
knoten: Kapitel 10: Shell-Skripte
order: 6150500
summary: Die eckige Klammer hat Fallen: Variablen ohne Anführungszeichen, Umleitungszeichen, getrennte Operatoren für Zahlen.
tags: [[ ausdruck ]], (( ausdruck )), Fallunterscheidung
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Die eckige Klammer hat Fallen: Variablen ohne Anführungszeichen, Umleitungszeichen, getrennte Operatoren für Zahlen. Die bash bietet zwei bequemere Formen, eine für Texte und Dateien, eine für Zahlen, dazu eine Verzweigung, die einen Text mit mehreren Mustern vergleicht.
:::

### Die doppelte eckige Klammer: `[[ ]]`

<span class="anker" id="stufe-4-1"></span>

Die Fehler mit `[ $leer = Anna ]` entstehen, weil `[` ein gewöhnlicher Befehl ist: Die Shell zerlegt seine Argumente in Wörter, bevor er sie sieht. Eine Prüfung, die die Shell selbst auswertet, kann diese Zerlegung auslassen.

:::definition Definition 4.1 (`[[ ]]`)
<span class="anker" id="satz-4-1"></span>

__`[[ ausdruck ]]`__ ist eine Prüfung, die die bash selbst als Teil ihrer Sprache auswertet. Sie kennt alle Prüfungen von `test`. Die Wörter zwischen den Klammern durchlaufen keine Worttrennung und keine Pfadnamen-Erweiterung; eine Variable bleibt also ein Wort, auch wenn sie leer ist oder Leerzeichen enthält. `<` und `>` sind darin Textvergleiche, keine Umleitungen.
:::

```console
$ [[ $leer = Anna ]]
$ echo $?
1
$ [[ -f $datei ]]
$ echo $?
0
```

Dazu kommt eine neue Möglichkeit: Steht rechts von `==` (oder `=`) ein Muster ohne Anführungszeichen, vergleicht `[[ ]]` den Text mit dem Muster, so wie die Pfadnamen-Erweiterung Dateinamen mit Mustern vergleicht ([Kapitel 5, Abschnitt 1.3](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/expansion-muster-klammern-und-tilde.html#stufe-1-3)), nur ohne Dateien. In Anführungszeichen ist das Muster gewöhnlicher Text:

```console
$ [[ $datei == *.txt ]]
$ echo $?
0
$ [[ $datei == "*.txt" ]]
$ echo $?
1
$ [[ 10 < 9 ]]
$ echo $?
0
```

`[[ 10 < 9 ]]` ist wahr: `<` vergleicht Texte, auch hier. Für Zahlen bleiben in `[[ ]]` `-lt` und die übrigen Buchstaben-Operatoren. Abbildung [14](#abb-14) zeigt, wo der Unterschied entsteht.

:::abbildung linux/k10doppelklammer 14
Zwei Wege nebeneinander. Links `[ $leer = Anna ]`: Die Zeile läuft zuerst durch die Station „Worttrennung“ der Shell, das leere Kärtchen fällt heraus, erst dann kommt der Rest beim Befehl `[` an; rotes Schild `2`. Rechts `[[ $leer = Anna ]]`: Die Zeile geht an der Station vorbei direkt in die bash, die die Prüfung selbst macht; das leere Kärtchen bleibt als ein Wort erhalten, Schild `1`. Darunter ein dritter Durchgang `[[ $datei == *.txt ]]`: Das Muster `*.txt` legt sich über `mein einkauf.txt` und passt, Schild `0`.
:::

::::beispiel [Gegenbeispiel] Nur in der bash
`[[ ]]` gehört zur bash und zu einigen anderen Shells, nicht zum Standard für Unix-Shells. `sh` ist unter Ubuntu die kleinere Shell `dash`, und die kennt es nicht:

```console
$ sh -c '[[ -f einkauf.txt ]] && echo ja'
sh: 1: [[: not found
```

Wer `[[ ]]` benutzt, schreibt deshalb `#!/bin/bash` in die Shebang-Zeile, nicht `#!/bin/sh`.
::::

:::hintergrund Woher die doppelte Klammer kommt
`[[ ]]` stammt aus der KornShell, die David Korn Anfang der 1980er-Jahre bei den Bell Labs entwickelte; die Fassung von 1988 enthielt die doppelte Klammer, und die bash hat sie übernommen. Der Grund ist derselbe, der in diesem Unterabschnitt zu sehen war: Weil `[[` ein Schlüsselwort ist, sieht die Shell schon beim Lesen, dass eine Prüfung folgt, und kann die Teile darin anders behandeln als die Argumente eines Befehls. Ein Befehl wie `[` bekommt dagegen nur fertige Wörter und kann nicht mehr erkennen, ob ein Wort aus einer leeren Variable entstanden ist.
:::

⁠**Kurz gesagt:** `[[ ]]` prüft wie `test`, aber ohne Worttrennung und Musterersetzung; mit `==` vergleicht es Text mit einem Muster.

### Eingaben prüfen mit regulären Ausdrücken: `=~`

<span class="anker" id="stufe-4-2"></span>

Ein Skript, das Punkte, Monate oder Beträge als Argument erwartet, soll erkennen, ob wirklich eine Zahl angekommen ist. Muster für Dateinamen sind dafür zu grob; reguläre Ausdrücke aus [Kapitel 6](/wissen/informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke/textwerkzeuge-und-regulaere-ausdruecke.html) beschreiben die Form genau.

:::definition Definition 4.2 (`=~`)
<span class="anker" id="satz-4-2"></span>

In `[[ text =~ ausdruck ]]` ist der Ausdruck rechts ein regulärer Ausdruck in der erweiterten Form ([Kapitel 6, Abschnitt 7.2](/wissen/informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke/regulare-ausdrucke-wiederholungen-gruppen-und-alternativen.html#stufe-7-2)). Die Prüfung ist wahr, wenn der Ausdruck irgendwo im Text einen Treffer hat. Der Ausdruck steht ohne Anführungszeichen; Teile in Anführungszeichen gelten als gewöhnliche Zeichen.
:::

Soll der ganze Text passen, verankert man den Ausdruck mit `^` und `$` ([Kapitel 6, Abschnitt 6.6](/wissen/informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke/regulare-ausdrucke-zeichen-klassen-und-anker.html#stufe-6-6)). `^[0-9]+$` heißt: von Anfang bis Ende eine oder mehrere Ziffern.

```console
$ eingabe=42
$ [[ $eingabe =~ ^[0-9]+$ ]]
$ echo $?
0
$ eingabe=4x2
$ [[ $eingabe =~ ^[0-9]+$ ]]
$ echo $?
1
$ eingabe=
$ [[ $eingabe =~ ^[0-9]+$ ]]
$ echo $?
1
```

Der leere Text fällt durch, weil `+` mindestens eine Ziffer verlangt ([Kapitel 6, Abschnitt 7.3](/wissen/informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke/regulare-ausdrucke-wiederholungen-gruppen-und-alternativen.html#stufe-7-3)). Wie in [Kapitel 6, Abschnitt 7.7](/wissen/informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke/regulare-ausdrucke-wiederholungen-gruppen-und-alternativen.html#stufe-7-7) prüft der Ausdruck nur die Form: `999` ist für ihn so gut wie `42`. Ob die Zahl in einem erlaubten Bereich liegt, prüft man danach mit einem Zahlenvergleich. Abbildung [15](#abb-15) vergleicht die drei Eingaben.

:::abbildung linux/k10regex 15
Der Ausdruck `^[0-9]+$` als Schablone mit drei Teilen: „Anfang“, „eine oder mehr Ziffern“, „Ende“. Drei Eingaben werden nacheinander daruntergeschoben: `42` füllt die Schablone von Anfang bis Ende, grünes `0`; bei `4x2` bleibt die Schablone am `x` hängen, rotes `1`; die leere Eingabe füllt den Teil „eine oder mehr“ nicht, rotes `1`.
:::

⁠**Kurz gesagt:** `[[ $text =~ ^[0-9]+$ ]]` prüft mit einem regulären Ausdruck, ob ein Text die erwartete Form hat.

### Rechnen als Bedingung: `(( ))`

<span class="anker" id="stufe-4-3"></span>

Zahlen mit `-lt` und `-ge` zu vergleichen ist umständlich. Die Arithmetik aus [Kapitel 5, Abschnitt 2.4](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/variablen-befehlsersetzung-und-arithmetik.html#stufe-2-4) kennt die üblichen Zeichen `<` und `>=`; es fehlt nur ein Weg, ihr Ergebnis als Exit-Status zu bekommen.

:::definition Definition 4.3 (`(( ))`)
<span class="anker" id="satz-4-3"></span>

__`(( ausdruck ))`__ wertet einen arithmetischen Ausdruck aus wie `$(( ))` und endet mit dem Exit-Status 0, wenn sein Wert nicht 0 ist, und mit 1, wenn sein Wert 0 ist. Vergleiche wie `<`, `<=`, `==`, `!=`, `>=`, `>` haben den Wert 1, wenn sie stimmen, sonst 0. Variablen schreibt man darin ohne `$`.
:::

Die Umkehrung ist kein Versehen: In der Arithmetik heißt 0 „falsch“, beim Exit-Status heißt 0 „Erfolg“. `(( ))` übersetzt das eine ins andere, damit `if` damit arbeiten kann.

```console
$ (( 10 < 9 ))
$ echo $?
1
$ (( 3 + 4 ))
$ echo $?
0
$ (( 0 ))
$ echo $?
1
$ n=5
$ (( n > 3 && n < 10 ))
$ echo $?
0
```

`&&` und `||` verknüpfen in der Arithmetik zwei Vergleiche zu „beide“ und „mindestens einer“. Wie `$(( ))` rechnet `(( ))` nur mit ganzen Zahlen. Abbildung [16](#abb-16) zeigt die Übersetzung.

:::abbildung linux/k10doppelrund 16
Ein Übersetzer zwischen zwei Welten. Links „Arithmetik“ mit drei Ausdrücken und ihren Werten: `10 < 9` ergibt `0`, `3 + 4` ergibt `7`, `n > 3 && n < 10` mit `n=5` ergibt `1`. Ein Pfeil durch das Tor `(( ))` nach rechts „Exit-Status“: Wert `0` wird zu Status `1` (rot, „falsch“), jeder andere Wert zu Status `0` (grün, „wahr“).
:::

::::beispiel Punkte bewerten
Das Skript `bewertung.sh` macht aus einer Punktzahl von 0 bis 100 eine Bewertung. Es prüft die Grenzen von oben nach unten; der erste Zweig, der passt, gewinnt:

```bash bewertung.sh
#!/bin/bash
# bewertung.sh: macht aus Punkten (0 bis 100) eine Bewertung
punkte=$1
if (( punkte >= 90 )); then
    echo "sehr gut"
elif (( punkte >= 75 )); then
    echo "gut"
elif (( punkte >= 50 )); then
    echo "bestanden"
else
    echo "nicht bestanden"
fi
```

```console
$ chmod +x bewertung.sh
$ ./bewertung.sh 93
sehr gut
$ ./bewertung.sh 75
gut
$ ./bewertung.sh 12
nicht bestanden
```

Bei 75 ist `punkte >= 90` falsch und `punkte >= 75` wahr; die Grenze 75 selbst gehört also zu „gut“.
::::

⁠**Kurz gesagt:** `(( ))` rechnet mit ganzen Zahlen und meldet „Wert ungleich 0“ als Erfolg; damit vergleicht man Zahlen mit `<`, `>=` und `==`.

### Bedingungen verknüpfen

<span class="anker" id="stufe-4-4"></span>

Oft hängt eine Entscheidung an mehr als einer Frage: „Es ist eine Datei und sie ist nicht leer“ oder „die Zahl ist kleiner als 0 oder größer als 100“. Manchmal braucht man auch nur das Gegenteil einer Frage.

:::definition Definition 4.4 (Verknüpfte Bedingungen)
<span class="anker" id="satz-4-4"></span>

<ul>

<li>

`!` vor einem Befehl kehrt seinen Exit-Status um: aus 0 wird 1, aus jedem anderen Wert 0.

</li>

<li>

Prüfungen verknüpft man mit `&&` und `||` zwischen Befehlen ([Kapitel 4, Abschnitte 6.2](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/befehle-verketten.html#stufe-6-2) und [6.3](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/befehle-verketten.html#stufe-6-3)), etwa `[ -f d ] && [ -s d ]`.

</li>

<li>

Innerhalb von `[[ ]]` und `(( ))` dürfen `&&`, `||` und `!` auch direkt zwischen den Teilen stehen.

</li>

</ul>
:::

```console
$ if ! grep -q Butter einkauf.txt; then echo "Butter fehlt"; fi
Butter fehlt
$ [ -f einkauf.txt ] && [ -s einkauf.txt ]
$ echo $?
0
$ [[ -f einkauf.txt && -s leer.txt ]]
$ echo $?
1
$ n=120
$ if (( n < 0 || n > 100 )); then echo "$n liegt außerhalb"; fi
120 liegt außerhalb
```

Hinter `!` steht ein Leerzeichen, sonst liest die interaktive Shell `!grep` als Rückgriff auf den Befehlsverlauf ([Kapitel 2, Abschnitt 5.2](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/schneller-arbeiten-vervollstandigung-verlauf-tastenkurzel.html#stufe-5-2)). Ältere Skripte verknüpfen innerhalb einer einzigen eckigen Klammer mit `-a` und `-o`; der Standard für Unix-Shells empfiehlt stattdessen getrennte Prüfungen mit `&&` und `||`, weil Ausdrücke mit `-a` und `-o` mehrdeutig sein können. Abbildung [17](#abb-17) zeigt die drei Formen.

:::abbildung linux/k10verknuepfen 17
Drei Reihen. Oben `! grep -q Butter einkauf.txt`: `grep` hält `1` hoch, das `!` dreht das Schild um zu `0`. Mitte `[ -f einkauf.txt ] && [ -s einkauf.txt ]`: zwei Prüf-Kästen hintereinander, der zweite wird nur betreten, weil der erste `0` meldet; Ergebnis `0`. Unten `[[ -f einkauf.txt && -s leer.txt ]]`: beide Teile in einem Kasten, der zweite liefert „leer“, Ergebnis `1`.
:::

⁠**Kurz gesagt:** `!` kehrt einen Exit-Status um; `&&` und `||` verknüpfen Prüfungen zwischen Befehlen oder innerhalb von `[[ ]]` und `(( ))`.

### Die Fallunterscheidung: `case`

<span class="anker" id="stufe-4-5"></span>

Ein Skript soll Dateien nach ihrer Endung einordnen: Bilder, Texte, Tabellen. Mit `if` und `elif` wäre das eine lange Kette von `[[ $1 == *.jpg ]]`. Für „ein Text, viele mögliche Muster“ gibt es eine eigene Form.

Ein Bild zur Orientierung: eine Sortieranlage für Briefe. Jeder Brief läuft an einer Reihe von Fächern vorbei und fällt in das erste, dessen Aufschrift passt.

:::definition Definition 4.5 (`case`)
<span class="anker" id="satz-4-5"></span>

Die __Fallunterscheidung__ `case wort in muster) befehle ;; ... esac` vergleicht das Wort der Reihe nach mit den Mustern und führt die Befehle des ersten passenden Musters aus, bis zum `;;`. Danach geht es hinter `esac` weiter. Die Muster sind Muster wie für Dateinamen (`*`, `?`, `[…]`); mehrere Muster für denselben Fall trennt `|`. Das Muster `*` passt auf alles und steht deshalb als Auffangfall am Ende. Passt kein Muster, geschieht nichts.
:::

```bash art.sh
#!/bin/bash
# art.sh: ordnet eine Datei nach der Endung ihres Namens ein
case "$1" in
    *.jpg | *.jpeg | *.png)
        echo "$1: ein Bild"
        ;;
    *.txt)
        echo "$1: ein Text"
        ;;
    *.csv)
        echo "$1: eine Tabelle"
        ;;
    *)
        echo "$1: unbekannte Art"
        ;;
esac
```

```console
$ chmod +x art.sh
$ ./art.sh "strand 1.jpg"
strand 1.jpg: ein Bild
$ ./art.sh einkauf.txt
einkauf.txt: ein Text
$ ./art.sh notiz.TXT
notiz.TXT: unbekannte Art
```

Muster unterscheiden Groß- und Kleinschreibung; `notiz.TXT` fällt deshalb in den Auffangfall. Das Skript prüft nur den Namen, nicht den Inhalt; was wirklich in einer Datei steckt, sagt `file` ([Kapitel 3, Abschnitt 4.6](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-ansehen.html#stufe-4-6)). Abbildung [18](#abb-18) zeigt die Sortieranlage.

:::abbildung linux/k10case 18
Eine Sortieranlage mit vier Fächern untereinander, beschriftet `*.jpg | *.jpeg | *.png`, `*.txt`, `*.csv` und `*`. Drei Namen laufen nacheinander von oben ein: `strand 1.jpg` fällt ins erste Fach („ein Bild“), `einkauf.txt` rollt am ersten vorbei und fällt ins zweite, `notiz.TXT` rollt an allen vorbei und landet im Auffangfach `*`. Ein Stopper hinter jedem Fach zeigt: Nach dem ersten Treffer werden keine weiteren Fächer geprüft.
:::

:::hintergrund Weiterprüfen statt aufhören
Mit `;;` endet ein Fall, und die übrigen Muster werden nicht mehr geprüft. Die bash kennt zwei weitere Abschlüsse: `;&` führt ohne Prüfung auch die Befehle des nächsten Falls aus, `;;&` prüft die folgenden Muster weiter und führt jeden weiteren passenden Fall aus. Das braucht man selten, etwa wenn ein Name wie `urlaub_2026.jpg` auf zwei Muster passt, `*.jpg` und `urlaub*`, und beides gemeldet werden soll: „ein Bild“ und „aus dem Urlaub“.
:::

⁠**Kurz gesagt:** `case` vergleicht ein Wort mit Mustern von oben nach unten und führt nur den ersten passenden Fall aus; `*` fängt den Rest.

:::aufgabe Aufgabe 12 ★ Einfache oder doppelte Klammer
<span class="anker" id="aufg-12"></span>

Es gelte `x="a b"` und `y=`. Sage voraus, was jede Zeile ausgibt, und prüfe: (a) `[ $x = "a b" ] && echo gleich`, (b) `[[ $x = "a b" ]] && echo gleich`, (c) `[[ -z $y ]] && echo leer`, (d) `[[ $x == a* ]] && echo passt`, (e) `[[ $x == "a*" ]] && echo passt`.

:::loesung
```console
$ x="a b"
$ y=
$ [ $x = "a b" ] && echo gleich
bash: [: too many arguments
$ [[ $x = "a b" ]] && echo gleich
gleich
$ [[ -z $y ]] && echo leer
leer
$ [[ $x == a* ]] && echo passt
passt
$ [[ $x == "a*" ]] && echo passt
```

(a) `$x` zerfällt in `a` und `b`, `test` bekommt zu viele Wörter. (b), (c) In `[[ ]]` gibt es keine Worttrennung, die Variablen bleiben je ein Wort. (d) `a*` ohne Anführungszeichen ist ein Muster, `a b` beginnt mit `a`. (e) In Anführungszeichen ist `a*` gewöhnlicher Text, und `a b` ist nicht dieser Text.
:::
:::

:::aufgabe Aufgabe 13 ★★ art.sh für große Endungen
<span class="anker" id="aufg-13"></span>

Erweitere `art.sh` so, dass auch `.JPG`, `.PNG` und `.TXT` erkannt werden und dass `.pdf` als „ein Dokument“ gilt. Benutze Klammerausdrücke in den Mustern, etwa `[jJ]`.

:::loesung
Ein Klammerausdruck wie `[jJ]` passt auf genau ein Zeichen aus der Menge ([Kapitel 3, Abschnitt 6.6](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/kopieren-verschieben-loschen.html#stufe-6-6)). Für jede Endung schreibt man jeden Buchstaben so:

```bash art.sh
#!/bin/bash
# art.sh: ordnet eine Datei nach der Endung ihres Namens ein, auch in Großbuchstaben
case "$1" in
    *.[jJ][pP][gG] | *.[jJ][pP][eE][gG] | *.[pP][nN][gG])
        echo "$1: ein Bild"
        ;;
    *.[tT][xX][tT])
        echo "$1: ein Text"
        ;;
    *.[cC][sS][vV])
        echo "$1: eine Tabelle"
        ;;
    *.[pP][dD][fF])
        echo "$1: ein Dokument"
        ;;
    *)
        echo "$1: unbekannte Art"
        ;;
esac
```

```console
$ ./art.sh notiz.TXT
notiz.TXT: ein Text
$ ./art.sh URLAUB.JPG
URLAUB.JPG: ein Bild
$ ./art.sh rechnung.pdf
rechnung.pdf: ein Dokument
$ ./art.sh laeufe.CSV
laeufe.CSV: eine Tabelle
$ ./art.sh liste.doc
liste.doc: unbekannte Art
```
:::
:::

:::aufgabe Aufgabe 14 ★★ Jahreszeiten
<span class="anker" id="aufg-14"></span>

Schreibe ein Skript `jahreszeit.sh MONAT`, das zu einer Monatszahl von 1 bis 12 die meteorologische Jahreszeit ausgibt (Dezember bis Februar Winter, März bis Mai Frühling usw.). Benutze `case` mit `|`. Alles andere soll die Meldung `kein Monat` ergeben.

:::loesung
```bash jahreszeit.sh
#!/bin/bash
# jahreszeit.sh: meteorologische Jahreszeit zu einer Monatszahl
case "$1" in
    12 | 1 | 2)
        echo "Winter"
        ;;
    3 | 4 | 5)
        echo "Frühling"
        ;;
    6 | 7 | 8)
        echo "Sommer"
        ;;
    9 | 10 | 11)
        echo "Herbst"
        ;;
    *)
        echo "kein Monat"
        ;;
esac
```

Eine Schleife prüft mehrere Monate auf einmal; `printf '%s: '` schreibt die Monatszahl ohne Zeilenende davor:

```console
$ chmod +x jahreszeit.sh
$ for m in 1 4 7 10 12 13 abc; do printf '%s: ' "$m"; ./jahreszeit.sh "$m"; done
1: Winter
4: Frühling
7: Sommer
10: Herbst
12: Winter
13: kein Monat
abc: kein Monat
```

Die Muster vergleichen Text, nicht Zahlen: `01` wäre „kein Monat“. Wer das will, ergänzt `01` bis `09` als weitere Muster.
:::
:::

:::aufgabe Aufgabe 15 ★★ Wahr ist 0
<span class="anker" id="aufg-15"></span>

Sage den Exit-Status voraus: (a) `(( 5 - 5 ))`, (b) `(( -1 ))`, (c) `(( 2 > 1 ))`. Danach: `n=0`, `(( n++ ))`, `echo $? $n`. Warum ist der Status hier 1, obwohl die Zeile tadellos funktioniert hat?

:::loesung
```console
$ (( 5 - 5 )); echo $?
1
$ (( -1 )); echo $?
0
$ (( 2 > 1 )); echo $?
0
$ n=0
$ (( n++ )); echo $? $n
1 1
```

`(( ))` fragt nur, ob der Wert 0 ist: $5-5=0$ ergibt 1, $-1$ ist nicht 0 und ergibt 0, der Vergleich hat den Wert 1 und ergibt 0. `n++` erhöht `n` auf 1, hat als Ausdruck aber den alten Wert 0, und daraus wird der Status 1. Die Zeile hat getan, was sie sollte; nur ihr Exit-Status sagt „falsch“. Das spielt eine Rolle, sobald etwas den Status auswertet, etwa `set -e` in Abschnitt [8.5](fehler-erkennen-und-melden.html#stufe-8-5).
:::
:::

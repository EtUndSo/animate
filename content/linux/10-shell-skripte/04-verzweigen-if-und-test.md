---
title: Verzweigen: `if` und `test`
pfad: Informatik / Linux und Kommandozeile / Shell-Skripte
adresse: informatik/linux-und-kommandozeile/shell-skripte
knoten: Kapitel 10: Shell-Skripte
order: 6150400
summary: Ein Skript soll je nach Lage verschieden handeln: eine Datei zählen, wenn es sie gibt, und sonst eine Meldung ausgeben.
tags: Verzweigung, test
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Ein Skript soll je nach Lage verschieden handeln: eine Datei zählen, wenn es sie gibt, und sonst eine Meldung ausgeben. Dieser Abschnitt zeigt, wie die Shell entscheidet, nämlich anhand des Exit-Status eines Befehls, und welcher Befehl Dateien, Texte und Zahlen prüft.
:::

### Die Verzweigung: `if`

<span class="anker" id="stufe-3-1"></span>

In vielen Programmiersprachen prüft eine Verzweigung eine Bedingung wie „$x > 3$“. Die Shell geht einen eigenen Weg: Sie führt einen Befehl aus und schaut, ob er Erfolg hatte. Das passt zu allem, was die [Kapitel 4](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/stroeme-umleitung-pipes-und-exit-status.html) und 6 über den Exit-Status gezeigt haben, etwa dass `grep -q` mit 0 meldet, dass es einen Treffer gab.

Ein Bild zur Orientierung: eine Weiche, die von einer Rückmeldung gestellt wird. Ein Befehl läuft, meldet „geklappt“ oder „nicht geklappt“, und danach fährt der Zug auf das eine oder andere Gleis.

:::definition Definition 3.1 (`if`)
<span class="anker" id="satz-3-1"></span>

Die __Verzweigung__ `if befehle; then befehle; fi` führt zuerst die Befehle zwischen `if` und `then` aus. Ist der Exit-Status des letzten davon 0, führt sie die Befehle zwischen `then` und `fi` aus, sonst überspringt sie sie. `if`, `then` und `fi` sind Schlüsselwörter der Shell; vor `then` und `fi` steht ein Semikolon oder ein Zeilenende.
:::

```console
$ if grep -q Kaffee einkauf.txt; then echo "Kaffee steht drauf"; fi
Kaffee steht drauf
$ if grep -q Butter einkauf.txt; then echo "Butter steht drauf"; fi
```

In Skripten schreibt man jeden Teil auf eine eigene Zeile und rückt den Inhalt ein; das ist leichter zu lesen und bedeutet dasselbe. Tippt man das in der Befehlszeile, zeigt die Shell vor jeder Folgezeile `>`, bis `fi` den Befehl abschließt:

```console
$ if grep -q Kaffee einkauf.txt
> then
>     echo "Kaffee steht drauf"
> fi
Kaffee steht drauf
```

Abbildung [9](#abb-9) zeigt den Ablauf als Weiche.

:::abbildung linux/k10if 9
Eine Weiche. Oben läuft der Befehl `grep -q Kaffee einkauf.txt` und hält ein Schild mit seinem Exit-Status hoch. Bei `0` stellt sich die Weiche auf das Gleis `then`: `echo "Kaffee steht drauf"`, danach geht es hinter `fi` weiter. Zweiter Durchgang mit `Butter`: Schild `1`, die Weiche führt am `then`-Gleis vorbei direkt hinter `fi`.
:::

:::hintergrund Warum `fi` und nicht `end`
Stephen Bourne schrieb die Bourne-Shell, aus der die bash hervorgegangen ist, Ende der 1970er-Jahre bei den Bell Labs. Er war mit der Programmiersprache ALGOL 68 vertraut, in der ein Abschnitt mit seinem rückwärts geschriebenen Schlüsselwort endet: `if` mit `fi`, `case` mit `esac`. Bourne übernahm diese Schreibweise. Sie hat einen praktischen Vorteil: Man sieht an jedem Ende, welcher Abschnitt dort schließt, was eine bloße schließende Klammer nicht verrät. Schleifen enden in der Shell allerdings mit `done`, nicht mit dem rückwärts geschriebenen `od`.
:::

⁠**Kurz gesagt:** `if` führt einen Befehl aus und nimmt den `then`-Zweig genau dann, wenn dieser Befehl mit dem Exit-Status 0 endet.

### Die Alternativen: `else` und `elif`

<span class="anker" id="stufe-3-2"></span>

Meist soll im anderen Fall etwas anderes geschehen, und manchmal gibt es mehr als zwei Fälle.

:::definition Definition 3.2 (`else` und `elif`)
<span class="anker" id="satz-3-2"></span>

Vor `fi` darf ein Zweig `else befehle` stehen; seine Befehle laufen, wenn die Bedingung nicht den Status 0 hatte. Dazwischen dürfen beliebig viele Zweige `elif befehle; then befehle` stehen (kurz für „else if“). Die Shell prüft die Bedingungen von oben nach unten und führt genau den Zweig der ersten aus, die mit 0 endet; endet keine mit 0, den `else`-Zweig, falls es ihn gibt.
:::

```console
$ if grep -q Butter einkauf.txt; then echo "Butter ist da"; else echo "Butter fehlt"; fi
Butter fehlt
```

::::beispiel Drei Fälle
Mit `elif` lassen sich drei Fälle unterscheiden. Die erste Bedingung endet hier mit 1, die zweite mit 0; also läuft der zweite Zweig, und der `else`-Zweig läuft nicht mehr:

```console
$ if grep -q Butter einkauf.txt; then echo "Butter"; elif grep -q Kaffee einkauf.txt; then echo "Kaffee, aber keine Butter"; else echo "weder noch"; fi
Kaffee, aber keine Butter
```
::::

⁠**Kurz gesagt:** `elif` prüft weitere Bedingungen der Reihe nach, `else` fängt alle übrigen Fälle; ausgeführt wird höchstens ein Zweig.

### Der Befehl `test` und die eckige Klammer

<span class="anker" id="stufe-3-3"></span>

`if` braucht einen Befehl, dessen Exit-Status die Frage beantwortet. Für Fragen wie „Gibt es diese Datei?“ oder „Ist diese Zahl kleiner als 10?“ gibt es einen eigenen Befehl, der nichts anderes tut, als zu prüfen und mit 0 oder 1 zu antworten.

:::definition Definition 3.3 (`test` und `[`)
<span class="anker" id="satz-3-3"></span>

Der Befehl __`test`__ wertet den Ausdruck aus, den seine Argumente bilden, und endet mit dem Status 0, wenn er wahr ist, mit 1, wenn er falsch ist, und mit 2 bei einem Fehler im Ausdruck. Er hat einen zweiten Namen, `[`; unter diesem Namen verlangt er als letztes Argument eine schließende Klammer `]`. `[ -f einkauf.txt ]` bedeutet also dasselbe wie `test -f einkauf.txt`.
:::

```console
$ test -f einkauf.txt
$ echo $?
0
$ [ -f einkauf.txt ]
$ echo $?
0
$ [ -d einkauf.txt ]
$ echo $?
1
$ type test [
test is a shell builtin
[ is a shell builtin
```

`-f` fragt, ob es eine gewöhnliche Datei ist, `-d`, ob es ein Verzeichnis ist. Wichtig ist hier die Form: `[` ist ein Befehl wie jeder andere, kein Satzzeichen. Deshalb müssen um die Klammer und um jeden Teil des Ausdrucks Leerzeichen stehen, damit es getrennte Wörter werden, und die schließende Klammer muss das letzte Wort sein. Fehlt etwas davon, gibt es Fehler:

```console
$ [ -f einkauf.txt
bash: [: missing `]'
$ [-f einkauf.txt ]
[-f: command not found
```

Im zweiten Fall sucht die Shell einen Befehl namens `[-f`, weil das erste Wort der Zeile so heißt. Abbildung [10](#abb-10) zerlegt eine Prüfung in ihre Wörter.

:::abbildung linux/k10klammer 10
Die Zeile `[ -f einkauf.txt ]` in vier Wort-Kärtchen zerlegt: `[` als „Befehl“, `-f` als „Frage“, `einkauf.txt` als „Gegenstand“, `]` als „Schlusszeichen, muss das letzte Argument sein“. Der Befehl `[` hält ein Schild mit seinem Exit-Status `0` hoch. Darunter die fehlerhafte Zeile `[-f einkauf.txt ]`: Das erste Kärtchen heißt `[-f`, ein rotes Fragezeichen „Befehl gibt es nicht“.
:::

:::hintergrund Warum die Klammer ein Befehl ist
Anfangs war `test` ein eigenes Programm, das ein Skript wie jedes andere Programm aufrief. Mit Unix System III (1981) wurde es in die Shell eingebaut, was den Start eines eigenen Programms für jede kleine Prüfung erspart, und bekam zugleich den zweiten Namen `[`, unter dem es prüft, ob als letztes Argument `]` folgt. So sieht eine Bedingung aus wie ein Ausdruck in Klammern, bleibt aber ein Befehl: Für die Shell ist `[` bis heute ein gewöhnlicher Befehlsname, und die Klammer `]` ist nur ein Argument. Neben dem eingebauten Befehl gibt es auch heute noch Programmdateien `/usr/bin/test` und `/usr/bin/[` für Programme, die keine Shell sind.
:::

⁠**Kurz gesagt:** `[ ausdruck ]` ist der Befehl `test` unter anderem Namen; er antwortet nur mit seinem Exit-Status und braucht Leerzeichen um jedes Wort.

### Dateien prüfen

<span class="anker" id="stufe-3-4"></span>

Bevor ein Skript eine Datei bearbeitet, sollte es fragen, ob es sie gibt und ob es die richtige Art von Eintrag ist. Sonst laufen Befehle mit Namen, die nichts bezeichnen, ins Leere.

:::definition Definition 3.4 (Dateiprüfungen)
<span class="anker" id="satz-3-4"></span>

Mit einem Namen als zweitem Wort prüft `test`:

<ul>

<li>

`-e name`: Der Eintrag existiert, gleich welcher Art.

</li>

<li>

`-f name`: Er ist eine gewöhnliche Datei.

</li>

<li>

`-d name`: Er ist ein Verzeichnis.

</li>

<li>

`-s name`: Er existiert und ist größer als 0 Byte.

</li>

<li>

`-r`, `-w`, `-x name`: Der Prozess darf ihn lesen, schreiben beziehungsweise ausführen.

</li>

<li>

`-L name`: Er ist ein symbolischer Link.

</li>

</ul>

Alle Prüfungen außer `-L` folgen symbolischen Links und prüfen das Ziel.
:::

Die Rechte prüft `test` mit den Nummern des Prozesses, so wie der Kernel beim Öffnen prüfen würde ([Kapitel 7, Abschnitt 5.2](/wissen/informatik/linux-und-kommandozeile/benutzer-gruppen-und-rechte/wie-der-kernel-rechte-pruft.html#stufe-5-2)). Das Skript `dateiinfo.sh` benutzt vier dieser Prüfungen in einer Kette aus `if`, `elif` und `else`; in einem Zweig steht eine weitere Verzweigung:

```bash dateiinfo.sh
#!/bin/bash
# dateiinfo.sh: sagt, was hinter einem Namen steckt
name=$1
if [ -d "$name" ]; then
    echo "$name: ein Verzeichnis"
elif [ -f "$name" ]; then
    if [ -s "$name" ]; then
        echo "$name: eine Datei mit Inhalt"
    else
        echo "$name: eine leere Datei"
    fi
elif [ -e "$name" ]; then
    echo "$name: weder Datei noch Verzeichnis"
else
    echo "$name: gibt es nicht"
fi
```

Für die Probe legst du ein Verzeichnis `fotos` und eine leere Datei an:

```console
$ mkdir fotos
$ touch leer.txt
```

```console
$ chmod +x dateiinfo.sh
$ ./dateiinfo.sh einkauf.txt
einkauf.txt: eine Datei mit Inhalt
$ ./dateiinfo.sh leer.txt
leer.txt: eine leere Datei
$ ./dateiinfo.sh fotos
fotos: ein Verzeichnis
$ ./dateiinfo.sh /dev/null
/dev/null: weder Datei noch Verzeichnis
$ ./dateiinfo.sh gibtsnicht.txt
gibtsnicht.txt: gibt es nicht
```

`/dev/null` ist eine Gerätedatei ([Kapitel 3, Abschnitt 7.7](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/die-verzeichnisstruktur-von-linux.html#stufe-7-7)): Es gibt sie, aber sie ist weder eine gewöhnliche Datei noch ein Verzeichnis. Abbildung [11](#abb-11) zeigt den Weg durch die Kette.

:::abbildung linux/k10dateiinfo 11
Die Kette aus `dateiinfo.sh` als Folge von vier Toren: `-d?`, `-f?`, `-e?`, dann `else`. Fünf Namen laufen nacheinander hinein: `fotos` biegt am ersten Tor ab („ein Verzeichnis“), `einkauf.txt` und `leer.txt` am zweiten, wo ein inneres Tor `-s?` sie in „mit Inhalt“ und „leer“ trennt, `/dev/null` am dritten, `gibtsnicht.txt` landet bei `else`. Jeder Name nimmt genau einen Weg.
:::

⁠**Kurz gesagt:** `-e`, `-f`, `-d`, `-s`, `-r`, `-w`, `-x` fragen nach Dasein, Art, Inhalt und Rechten eines Eintrags.

### Text vergleichen

<span class="anker" id="stufe-3-5"></span>

Skripte vergleichen oft Texte: Hat der Benutzer `ja` geantwortet? Ist ein Argument leer?

:::definition Definition 3.5 (Textvergleiche)
<span class="anker" id="satz-3-5"></span>

`test` vergleicht Texte mit `a = b` (gleich) und `a != b` (verschieden). `-z text` ist wahr, wenn der Text leer ist, `-n text`, wenn er nicht leer ist. Zeichen werden genau verglichen, Groß- und Kleinschreibung zählen.
:::

```console
$ name=Anna
$ [ "$name" = Anna ]
$ echo $?
0
$ [ "$name" != Anna ]
$ echo $?
1
$ [ -n "$name" ]
$ echo $?
0
$ leer=
$ [ -z "$leer" ]
$ echo $?
0
```

Die doppelten Anführungszeichen um `$name` sind kein Schmuck. `test` bekommt seinen Ausdruck als einzelne Wörter, und eine Variable ohne Anführungszeichen kann zu keinem oder zu mehreren Wörtern werden ([Kapitel 5, Abschnitt 3.2](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/worttrennung-und-quoting.html#stufe-3-2)). Dann sieht `test` einen Ausdruck mit fehlenden oder überzähligen Teilen:

```console
$ [ $leer = Anna ]
bash: [: =: unary operator expected
$ echo $?
2
$ [ "$leer" = Anna ]
$ echo $?
1
$ datei="mein einkauf.txt"
$ [ -f $datei ]
bash: [: mein: binary operator expected
$ echo $?
2
$ [ -f "$datei" ]
$ echo $?
0
```

Bei `[ $leer = Anna ]` verschwindet die leere Variable, und `test` sieht nur `= Anna ]`. Ein Ausdruck mit zwei Wörtern muss eine Frage mit einem Gegenstand sein, etwa `-z text`; also meldet `test`, `=` sei kein solcher Operator, und endet mit 2. In einem `if` zählt das wie „falsch“, das Skript nimmt still den falschen Zweig. Abbildung [12](#abb-12) zeigt, was ankommt.

:::abbildung linux/k10leerfalle 12
Zwei Zeilen untereinander, je oben getippt und unten als Wörter, die bei `[` ankommen. Links `[ $leer = Anna ]`: Das Kärtchen für `$leer` löst sich in Luft auf, es bleiben `=`, `Anna`, `]`; `[` hält ein rotes Schild `2` und „unary operator expected“. Rechts `[ "$leer" = Anna ]`: Ein leeres, aber vorhandenes Kärtchen `""` bleibt stehen, vier Wörter kommen an, Schild `1`, „falsch“. Darunter dasselbe für `mein einkauf.txt`: ohne Anführungszeichen zwei Kärtchen, mit Anführungszeichen eines.
:::

⁠**Kurz gesagt:** `=`, `!=`, `-z` und `-n` vergleichen Texte; jede Variable in `[ ]` gehört in doppelte Anführungszeichen.

### Zahlen vergleichen

<span class="anker" id="stufe-3-6"></span>

Ist eine Datei länger als 100 Zeilen? Hat ein Skript zu wenige Argumente? Solche Fragen vergleichen Zahlen, und dafür hat `test` eigene Operatoren.

:::definition Definition 3.6 (Zahlenvergleiche)
<span class="anker" id="satz-3-6"></span>

`test` vergleicht ganze Zahlen mit `-eq` (gleich), `-ne` (ungleich), `-lt` (kleiner), `-le` (kleiner oder gleich), `-gt` (größer) und `-ge` (größer oder gleich). Ist eines der Wörter keine ganze Zahl, meldet es einen Fehler und endet mit 2.
:::

Die Namen kommen aus dem Englischen: „equal“, „not equal“, „less than“, „less or equal“, „greater than“, „greater or equal“.

```console
$ [ 10 -lt 9 ]
$ echo $?
1
$ [ 10 -gt 9 ]
$ echo $?
0
$ [ 007 -eq 7 ]
$ echo $?
0
$ [ 007 = 7 ]
$ echo $?
1
$ [ zehn -gt 5 ]
bash: [: zehn: integer expected
$ echo $?
2
```

Als Zahlen sind `007` und `7` gleich, als Texte verschieden. Welcher Vergleich gemeint ist, entscheidet allein der Operator. Die Zeichen `<` und `>` vergleichen in `test` Texte nach ihrer Zeichenordnung ([Kapitel 6, Abschnitt 3.1](/wissen/informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke/sortieren-und-zahlen-sort-und-uniq.html#stufe-3-1)), und zwar nur, wenn man sie mit `\` vor der Shell schützt. Als Texte ist `10` kleiner als `9`, weil das Zeichen `1` vor dem Zeichen `9` kommt:

```console
$ [ 10 \< 9 ]
$ echo $?
0
```

Abbildung [13](#abb-13) stellt beide Vergleiche gegenüber.

:::abbildung linux/k10zahltext 13
Links „als Zahlen“ ein Zahlenstrahl von 0 bis 12; die Marken 9 und 10 liegen in der richtigen Reihenfolge, `-lt` fragt „liegt 10 links von 9?“, Antwort nein, Status `1`. Rechts „als Texte“ eine Liste in Wörterbuch-Reihenfolge mit den Zeichenketten `007`, `10`, `7`, `9` in Zeichenordnung; `10` steht vor `9`, weil das erste Zeichen `1` vor `9` kommt; `\<` antwortet ja, Status `0`.
:::

:::warnung `<` und `>` in `[ ]` sind Umleitungen
Ohne `\` sind `<` und `>` auch zwischen eckigen Klammern Umleitungszeichen ([Kapitel 4, Abschnitt 2.1](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/ausgaben-umleiten.html#stufe-2-1)). `[ 10 > 9 ]` prüft deshalb nicht, ob 10 größer ist, sondern legt eine leere Datei namens `9` an und fragt nur, ob `10` ein nicht leerer Text ist. Das ist immer wahr, gleich welche Zahlen dastehen:

```console
$ [ 10 > 9 ]
$ echo $?
0
$ ls -l 9
-rw-r--r-- 1 student student 0 Nov 12 23:45 9
$ rm 9
```

Stünde dort der Name einer vorhandenen Datei, würde sie geleert ([Kapitel 4, Abschnitt 2.1](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/ausgaben-umleiten.html#stufe-2-1)). Für Zahlen in `[ ]` gelten deshalb nur `-lt`, `-gt` und die übrigen Buchstaben-Operatoren.
:::

⁠**Kurz gesagt:** Zahlen vergleicht `test` mit `-eq`, `-ne`, `-lt`, `-le`, `-gt`, `-ge`; `<` und `>` vergleichen Texte oder leiten um.

:::aufgabe Aufgabe 8 ★ Exit-Status vorhersagen
<span class="anker" id="aufg-8"></span>

Sage den Exit-Status jeder Prüfung voraus und kontrolliere ihn mit `echo $?`: (a) `[ -d /etc ]`, (b) `[ -f /etc ]`, (c) `[ 5 -lt 10 ]`, (d) `[ 5 \< 10 ]`, (e) `[ Anna = anna ]`, (f) `[ -n "" ]`, (g) `[ -z ]`. Begründe besonders (d) und (g).

:::loesung
```console
$ [ -d /etc ]; echo $?
0
$ [ -f /etc ]; echo $?
1
$ [ 5 -lt 10 ]; echo $?
0
$ [ 5 \< 10 ]; echo $?
1
$ [ Anna = anna ]; echo $?
1
$ [ -n "" ]; echo $?
1
$ [ -z ]; echo $?
0
```

(d) `\<` vergleicht Texte Zeichen für Zeichen: `5` kommt nach `1`, also ist `5` als Text nicht kleiner als `10`. (e) Groß- und Kleinschreibung zählen. (g) Ohne Gegenstand hat `test` nur ein einziges Wort vor der Klammer, `-z`. Mit einem einzigen Wort prüft `test` nur, ob dieses Wort nicht leer ist, und `-z` ist ein nicht leerer Text. Genau diese Verwechslung macht `[ -z $leer ]` ohne Anführungszeichen tückisch: Es liefert zufällig das richtige Ergebnis, aber `[ -n $leer ]` ist dann ebenfalls wahr.
:::
:::

:::aufgabe Aufgabe 9 ★★ dateiinfo.sh erweitern
<span class="anker" id="aufg-9"></span>

Erweitere `dateiinfo.sh` so, dass es bei einer Datei zusätzlich meldet, ob du sie lesen und ob du sie ausführen darfst. Teste es mit `einkauf.txt`, `zeige.sh` und `/etc/shadow`.

:::loesung
Im Zweig für gewöhnliche Dateien kommen zwei weitere Verzweigungen dazu:

```bash dateiinfo.sh
#!/bin/bash
# dateiinfo.sh: sagt, was hinter einem Namen steckt, bei Dateien auch die Rechte
name=$1
if [ -d "$name" ]; then
    echo "$name: ein Verzeichnis"
elif [ -f "$name" ]; then
    if [ -s "$name" ]; then
        echo "$name: eine Datei mit Inhalt"
    else
        echo "$name: eine leere Datei"
    fi
    if [ -r "$name" ]; then
        echo "  lesen: ja"
    else
        echo "  lesen: nein"
    fi
    if [ -x "$name" ]; then
        echo "  ausführen: ja"
    else
        echo "  ausführen: nein"
    fi
elif [ -e "$name" ]; then
    echo "$name: weder Datei noch Verzeichnis"
else
    echo "$name: gibt es nicht"
fi
```

```console
$ ./dateiinfo.sh einkauf.txt
einkauf.txt: eine Datei mit Inhalt
  lesen: ja
  ausführen: nein
$ ./dateiinfo.sh zeige.sh
zeige.sh: eine Datei mit Inhalt
  lesen: ja
  ausführen: ja
$ ./dateiinfo.sh /etc/shadow
/etc/shadow: eine Datei mit Inhalt
  lesen: nein
  ausführen: nein
```

Über `/etc/shadow` darf jeder erfahren, dass es sie gibt und wie groß sie ist, denn das steht in ihrer Inode und im lesbaren Verzeichnis `/etc`; lesen darf sie nur `root` und die Gruppe `shadow` ([Kapitel 7, Abschnitt 1.8](/wissen/informatik/linux-und-kommandozeile/benutzer-gruppen-und-rechte/benutzer-und-gruppen.html#stufe-1-8)).
:::
:::

:::aufgabe Aufgabe 10 ★★ Drei Fehler
<span class="anker" id="aufg-10"></span>

Jede dieser Zeilen aus einem Skript enthält einen Fehler. Erkläre, was jeweils geschieht, und verbessere sie: (a) `if [$# -eq 0]; then`, (b) `if [ $antwort = ja ]; then` bei einer leeren Antwort, (c) `if [ $alter > 17 ]; then`.

:::loesung
```console
$ if [$# -eq 0]; then echo "keine Argumente"; fi
[0: command not found
$ antwort=
$ if [ $antwort = ja ]; then echo "Antwort ja"; fi
bash: [: =: unary operator expected
$ alter=15
$ if [ $alter > 17 ]; then echo "volljährig"; fi
volljährig
$ ls 17
17
$ rm 17
```

(a) Ohne Leerzeichen entsteht das Wort `[0` (in der Befehlszeile ist `$#` gleich 0), und einen Befehl dieses Namens gibt es nicht. Richtig: `if [ $# -eq 0 ]; then`. (b) Die leere Variable verschwindet, `test` sieht `= ja` und meldet einen Fehler mit Status 2; `if` nimmt still den anderen Weg. Richtig: `[ "$antwort" = ja ]`. (c) `>` leitet um: Es entsteht eine Datei `17`, und `test` prüft nur, ob `15` nicht leer ist, also immer wahr. Richtig: `[ "$alter" -gt 17 ]`.
:::
:::

:::aufgabe Aufgabe 11 ★★★ Groß oder klein?
<span class="anker" id="aufg-11"></span>

Schreibe ein Skript `gross.sh DATEI GRENZE`, das meldet, ob die Datei mehr als `GRENZE` Byte hat. Die Größe liefert `wc -c < datei` ([Kapitel 3, Abschnitt 4.5](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-ansehen.html#stufe-4-5)). Prüfe vorher, ob es die Datei gibt. Teste es mit `einkauf.txt` und den Grenzen 10 und 100.

:::loesung
```bash gross.sh
#!/bin/bash
# gross.sh: meldet, ob eine Datei mehr als GRENZE Byte hat
#   Aufruf: gross.sh DATEI GRENZE
datei=$1
grenze=$2
if [ -f "$datei" ]; then
    groesse=$(wc -c < "$datei")
    if [ "$groesse" -gt "$grenze" ]; then
        echo "$datei: $groesse Byte, mehr als $grenze"
    else
        echo "$datei: $groesse Byte, nicht mehr als $grenze"
    fi
else
    echo "$datei: keine Datei" >&2
    exit 1
fi
```

```console
$ chmod +x gross.sh
$ ./gross.sh einkauf.txt 10
einkauf.txt: 25 Byte, mehr als 10
$ ./gross.sh einkauf.txt 100
einkauf.txt: 25 Byte, nicht mehr als 100
$ ./gross.sh gibtsnicht.txt 10
gibtsnicht.txt: keine Datei
$ echo $?
1
```

`einkauf.txt` hat 25 Byte: je Zeile die Buchstaben und ein Zeilenende, `Ä` zählt in UTF-8 doppelt ($6+5+7+7=25$, [Kapitel 3, Abschnitt 4.1](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-ansehen.html#stufe-4-1)). Der Vergleich benutzt `-gt`, weil es um Zahlen geht.
:::
:::

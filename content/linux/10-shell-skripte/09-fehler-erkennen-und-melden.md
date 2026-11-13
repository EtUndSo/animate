---
title: Fehler erkennen und melden
pfad: Informatik / Linux und Kommandozeile / Shell-Skripte
adresse: informatik/linux-und-kommandozeile/shell-skripte
knoten: Kapitel 10: Shell-Skripte
order: 6150900
summary: Ein Skript, das bei einem Fehler still weitermacht, kann großen Schaden anrichten, etwa Dateien im falschen Verzeichnis löschen.
tags: exit n, set -u, set -e, set -o pipefail
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Ein Skript, das bei einem Fehler still weitermacht, kann großen Schaden anrichten, etwa Dateien im falschen Verzeichnis löschen. Dieser Abschnitt zeigt, wie ein Skript Erfolg und Misserfolg nach außen meldet, wohin seine Meldungen gehören, wie es jeden kritischen Schritt prüft und was die Hilfen `set -u`, `set -e` und `pipefail` leisten und was nicht.
:::

### Der Exit-Status eines Skripts: `exit`

<span class="anker" id="stufe-8-1"></span>

Wer ein Skript aufruft, ob ein Mensch, ein anderes Skript oder `if`, erfährt nur über den Exit-Status, ob es geklappt hat. Die Fassung von `zaehle.sh` aus Abschnitt [5.2](schleifen-for-und-while.html#stufe-5-2) meldet immer Erfolg, auch wenn nichts zu zählen war:

```console
$ ./zaehle.sh gibtsnicht.txt
gibtsnicht.txt: keine Datei
$ echo $?
0
$ ./zaehle.sh
$ echo $?
0
```

:::definition Definition 8.1 (Exit-Status eines Skripts)
<span class="anker" id="satz-8-1"></span>

Ein Skript endet mit dem Exit-Status seines zuletzt ausgeführten Befehls. Der eingebaute Befehl __`exit n`__ beendet das Skript sofort, wo immer er steht, mit dem Status `n`; ohne Zahl mit dem Status des zuletzt ausgeführten Befehls.
:::

Welche Zahl man wählt, folgt der Gewohnheit der Werkzeuge aus [Kapitel 4, Abschnitt 5.2](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/der-exit-status.html#stufe-5-2): 0 für Erfolg, 1 für einen gewöhnlichen Fehler, etwa eine fehlende Datei, 2 für einen falschen Aufruf, etwa fehlende Argumente. Die Zahlen 126, 127 und ab 128 sind für die Shell reserviert ([Kapitel 4, Abschnitt 5.3](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/der-exit-status.html#stufe-5-3)). Was die Zahlen bedeuten, gehört in den Kommentar am Anfang des Skripts, so wie Handbuchseiten einen Abschnitt `EXIT STATUS` haben. Abbildung [34](#abb-34) zeigt die Entscheidungen der fertigen `zaehle.sh`.

:::abbildung linux/k10exit 34
Der Weg durch die fertige `zaehle.sh` als Flussbild. Erste Frage „Argumente da?“: nein führt zu `Aufruf: zaehle.sh DATEI...` auf der Fehlerausgabe und dem Ausgang `exit 2`. Ja führt in eine Schleife über die Dateien; bei einer fehlenden Datei merkt sich das Skript `status=1` und geht mit `continue` weiter. Nach der Schleife der Ausgang `exit "$status"` mit zwei Schildern: `0` „alles gezählt“, `1` „mindestens eine fehlte“.
:::

⁠**Kurz gesagt:** Ein Skript meldet seinen Erfolg über den Exit-Status: `exit 0` bei Erfolg, 1 bei einem Fehler, 2 bei einem falschen Aufruf.

### Meldungen auf die Fehlerausgabe

<span class="anker" id="stufe-8-2"></span>

Meldungen wie „Datei fehlt“ sind keine Ergebnisse. Leitet jemand die Ausgabe des Skripts in eine Datei oder eine Pipe, sollen dort nur Ergebnisse ankommen, und die Meldung soll trotzdem im Terminal erscheinen.

:::satz Satz 8.2 (Wohin Meldungen gehören)
<span class="anker" id="satz-8-2"></span>

Ein Skript schreibt Ergebnisse auf die Standardausgabe und Fehlermeldungen, Warnungen und Aufrufhinweise mit `>&2` auf die Fehlerausgabe ([Kapitel 4, Abschnitte 1.6](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/prozesse-und-ihre-drei-strome.html#stufe-1-6) und [2.5](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/ausgaben-umleiten.html#stufe-2-5)). Eine Meldung beginnt mit dem Namen des Skripts, damit man ihre Herkunft auch in einer längeren Pipeline erkennt.
:::

Die fertige Fassung von `zaehle.sh` verbindet die beiden letzten Unterabschnitte. Sie prüft die Zahl der Argumente, meldet fehlende oder unlesbare Dateien auf der Fehlerausgabe, merkt sich in `status`, dass etwas fehlte, und zählt die übrigen Dateien trotzdem:

```bash zaehle.sh
#!/bin/bash
# zaehle.sh: zählt die Zeilen jeder angegebenen Datei
#   Aufruf:      zaehle.sh DATEI...
#   Exit-Status: 0 alles gezählt, 1 mindestens eine Datei fehlte,
#                2 falscher Aufruf

programm=$(basename "$0")

if [ $# -eq 0 ]; then
    echo "Aufruf: $programm DATEI..." >&2
    exit 2
fi

status=0
for datei in "$@"; do
    if [ ! -f "$datei" ] || [ ! -r "$datei" ]; then
        echo "$programm: $datei: keine lesbare Datei" >&2
        status=1
        continue
    fi
    zeilen=$(wc -l < "$datei")
    echo "$datei: $zeilen Zeilen"
done
exit "$status"
```

```console
$ ./zaehle.sh
Aufruf: zaehle.sh DATEI...
$ echo $?
2
$ ./zaehle.sh einkauf.txt gibtsnicht.txt "mein einkauf.txt"
einkauf.txt: 4 Zeilen
zaehle.sh: gibtsnicht.txt: keine lesbare Datei
mein einkauf.txt: 3 Zeilen
$ echo $?
1
$ ./zaehle.sh einkauf.txt "mein einkauf.txt"
einkauf.txt: 4 Zeilen
mein einkauf.txt: 3 Zeilen
$ echo $?
0
```

Leitet man die Standardausgabe in eine Datei um, landen nur die Ergebnisse dort; die Meldung erscheint weiter im Terminal. Umgekehrt verwirft `2> /dev/null` die Meldungen ([Kapitel 4, Abschnitt 2.4](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/ausgaben-umleiten.html#stufe-2-4)):

```console
$ ./zaehle.sh einkauf.txt gibtsnicht.txt > ergebnis.txt
zaehle.sh: gibtsnicht.txt: keine lesbare Datei
$ cat ergebnis.txt
einkauf.txt: 4 Zeilen
$ ./zaehle.sh einkauf.txt gibtsnicht.txt 2> /dev/null
einkauf.txt: 4 Zeilen
```

Standardausgabe und Fehlerausgabe sind dieselben Rohre, die [Kapitel 4, Abschnitt 1.6](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/prozesse-und-ihre-drei-strome.html#stufe-1-6) für jedes Programm gezeigt hat; ein Skript ist darin ein Programm wie jedes andere.

⁠**Kurz gesagt:** Ergebnisse auf die Standardausgabe, Meldungen mit `>&2` und dem Namen des Skripts auf die Fehlerausgabe.

### Jeden kritischen Schritt prüfen

<span class="anker" id="stufe-8-3"></span>

Eine Shell macht nach einem gescheiterten Befehl einfach mit dem nächsten weiter. Meist ist das harmlos, manchmal verheerend. Das folgende Skript soll in einem angegebenen Verzeichnis alle `.tmp`-Dateien löschen; `--` schützt vor Namen, die mit einem Strich beginnen ([Kapitel 2, Abschnitt 2.7](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/der-aufbau-einer-befehlszeile.html#stufe-2-7)):

```bash loesche.sh
#!/bin/bash
# loesche.sh: löscht alle .tmp-Dateien im angegebenen Verzeichnis (gefährlich)
cd "$1"
rm -f -- *.tmp
echo "Aufgeräumt in $PWD"
```

:::warnung Das Skript löscht im falschen Verzeichnis
Führe die folgenden Zeilen nur im Übungsverzeichnis aus. Das Skript löscht die Testdatei `wichtig.tmp`, die nur dafür angelegt wird.
:::

```console
$ mkdir alt
$ touch alt/a.tmp alt/b.tmp wichtig.tmp
$ chmod +x loesche.sh
$ ./loesche.sh alt
Aufgeräumt in /home/student/linuxk10/alt
$ ls alt
$ ./loesche.sh gibtsnicht
./loesche.sh: line 3: cd: gibtsnicht: No such file or directory
Aufgeräumt in /home/student/linuxk10
$ ls wichtig.tmp
ls: cannot access 'wichtig.tmp': No such file or directory
```

`cd` ist gescheitert, das Skript hat trotzdem gelöscht, und zwar im Arbeitsverzeichnis des Aufrufers.

:::satz Satz 8.3 (Kritische Schritte prüfen)
<span class="anker" id="satz-8-3"></span>

Hängt ein Befehl davon ab, dass ein früherer Befehl Erfolg hatte, prüft das Skript den Exit-Status des früheren ausdrücklich und bricht bei einem Fehler ab: `befehl || exit 1` oder `if ! befehl; then …; exit 1; fi`.
:::

```bash loesche.sh
#!/bin/bash
# loesche.sh: löscht alle .tmp-Dateien im angegebenen Verzeichnis
if ! cd "$1"; then
    echo "loesche.sh: kann nicht nach '$1' wechseln, lösche nichts" >&2
    exit 1
fi
rm -f -- *.tmp
echo "Aufgeräumt in $PWD"
```

```console
$ touch wichtig.tmp
$ ./loesche.sh gibtsnicht
./loesche.sh: line 3: cd: gibtsnicht: No such file or directory
loesche.sh: kann nicht nach 'gibtsnicht' wechseln, lösche nichts
$ echo $?
1
$ ls wichtig.tmp
wichtig.tmp
```

Kritisch sind vor allem Verzeichniswechsel, das Anlegen von Dateien und Verzeichnissen und jeder Befehl, dessen Ergebnis ein späterer löschend oder überschreibend weiterverwendet. Abbildung [35](#abb-35) stellt die beiden Fassungen nebeneinander.

:::abbildung linux/k10cdfalle 35
Zwei Läufe von `loesche.sh gibtsnicht` nebeneinander, der Arbeitsordner `~/linuxk10` mit der Datei `wichtig.tmp` als Kasten. Links ohne Prüfung: `cd` prallt ab (rotes Kreuz), der Ablauf geht trotzdem weiter zu `rm -f -- *.tmp`, das im Arbeitsordner zuschlägt; `wichtig.tmp` verschwindet. Rechts mit Prüfung: `cd` prallt ab, der Pfeil biegt sofort zu `exit 1` ab, `rm` bleibt grau, `wichtig.tmp` bleibt stehen.
:::

:::hintergrund Den Befehl prüfen, nicht `$?`
Man könnte auch `cd "$1"` schreiben und in der nächsten Zeile `if [ $? -ne 0 ]` prüfen. Das ist fehleranfällig: Schiebt jemand später eine Zeile dazwischen, etwa ein `echo`, prüft `$?` den Status des `echo`. Und `[ $? -ne 0 ]` setzt selbst einen neuen Status. Den Befehl direkt in `if` oder vor `||` zu schreiben, verbindet Prüfung und Befehl untrennbar.
:::

⁠**Kurz gesagt:** Jeder Schritt, auf den sich spätere Schritte verlassen, wird mit `|| exit 1` oder `if !` geprüft, bevor es weitergeht.

### Unbelegte Variablen melden: `set -u`

<span class="anker" id="stufe-8-4"></span>

Ein Tippfehler im Namen einer Variablen fällt der Shell nicht auf: Eine unbekannte Variable ist einfach leer ([Kapitel 5, Abschnitt 2.2](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/variablen-befehlsersetzung-und-arithmetik.html#stufe-2-2)).

```bash tippfehler.sh
#!/bin/bash
# tippfehler.sh: ein Tippfehler im Namen einer Variablen
ordner=fotos
echo "Ich sichere $odrner"
echo "Fertig."
```

```console
$ bash tippfehler.sh
Ich sichere
Fertig.
$ echo $?
0
```

:::definition Definition 8.4 (`set -u`)
<span class="anker" id="satz-8-4"></span>

Nach dem eingebauten Befehl __`set -u`__ ist es ein Fehler, eine Variable einzusetzen, der nie ein Wert zugewiesen wurde. Die Shell meldet ihn mit `unbound variable`, und ein Skript endet dann mit dem Status 1. Ausgenommen sind `$@` und `$*`. `set +u` schaltet die Prüfung wieder ab.
:::

Mit der Zeile `set -u` unter dem Kommentar meldet das Skript den Fehler, statt still weiterzumachen:

```console
$ bash tippfehler.sh
tippfehler.sh: line 5: odrner: unbound variable
$ echo $?
1
```

Auch ein fehlendes Argument zählt als unbelegt: Mit `set -u` bricht ein Skript bei `$1` ab, wenn kein Argument übergeben wurde. Wer prüfen will, ob ein Argument da ist, fragt deshalb `$#` ab, nicht `$1`. Eine leere Zuweisung wie `leer=` ist eine Belegung und löst keinen Fehler aus. Abbildung [36](#abb-36) zeigt den Unterschied.

:::abbildung linux/k10setu 36
Zwei Läufe von `tippfehler.sh`. Oben ohne `set -u`: Die Zeile `echo "Ich sichere $odrner"` greift in eine Schublade `odrner`, die es nicht gibt, und bekommt Luft; die Ausgabe `Ich sichere` endet im Leeren, das Skript läuft weiter bis `Fertig.`, Status `0`. Unten mit `set -u`: Derselbe Griff löst ein rotes Signal `unbound variable` aus, das Skript hält an dieser Zeile, Status `1`. Daneben die Schublade `ordner = fotos`, auf die der Tippfehler hätte zeigen sollen.
:::

⁠**Kurz gesagt:** `set -u` macht aus einer unbelegten Variablen einen Fehler, der das Skript anhält, statt still einen leeren Text einzusetzen.

### Abbrechen bei Fehlern: `set -e` und seine Grenzen

<span class="anker" id="stufe-8-5"></span>

Jeden Befehl einzeln zu prüfen ist mühsam. Die Shell bietet eine Einstellung, die ein Skript bei jedem gescheiterten Befehl beenden soll. Sie hat allerdings so viele Ausnahmen, dass man sie kennen muss, bevor man sich auf sie verlässt.

:::definition Definition 8.5 (`set -e`)
<span class="anker" id="satz-8-5"></span>

Nach dem eingebauten Befehl __`set -e`__ beendet sich die Shell, sobald ein Befehl mit einem Exit-Status ungleich 0 endet, mit diesem Status. Ausgenommen sind Befehle, deren Status gerade geprüft wird: die Bedingung von `if`, `elif`, `while` und `until`, jeder Befehl einer Kette mit `&&` oder `||` außer dem letzten, jeder Befehl einer Pipeline außer dem letzten und jeder Befehl hinter `!`. Wird eine Funktion in einer solchen Lage aufgerufen, gilt die Ausnahme für alle Befehle in ihr.
:::

Die letzte Regel ist die tückischste. Das Skript `abbruch.sh` ruft dieselbe Funktion dreimal auf; in ihr scheitert `false`:

```bash abbruch.sh
#!/bin/bash
# abbruch.sh: wo set -e greift und wo nicht
set -e

pruefen() {
    false
    echo "  in pruefen nach false weiter"
}

pruefen || echo "  pruefen meldet einen Fehler"
echo "1: nach 'pruefen || ...'"
if pruefen; then
    echo "2: im if-Zweig"
fi
pruefen
echo "3: diese Zeile erscheint nie"
```

```console
$ bash abbruch.sh
  in pruefen nach false weiter
1: nach 'pruefen || ...'
  in pruefen nach false weiter
2: im if-Zweig
$ echo $?
1
```

In den ersten beiden Aufrufen wird der Status von `pruefen` geprüft, also wirkt `set -e` in der ganzen Funktion nicht: `false` scheitert, die Funktion läuft weiter und endet mit dem Status des `echo`, also 0. Erst der dritte, ungeprüfte Aufruf beendet das Skript. Ein zweites Beispiel zeigt die umgekehrte Überraschung: Ein harmloser Befehl beendet das Skript.

```bash zaehler.sh
#!/bin/bash
# zaehler.sh: set -e und ein harmloser Befehl mit Status 1
set -e
anzahl=0
(( anzahl++ ))
echo "anzahl ist jetzt $anzahl"
```

```console
$ bash zaehler.sh
$ echo $?
1
```

`anzahl++` erhöht die Variable, hat aber als Ausdruck den alten Wert 0, und `(( ))` macht daraus den Status 1 (Abschnitt [4.3](bequemer-prufen-und-case.html#stufe-4-3)). Für `set -e` ist das ein Fehler, und das Skript endet ohne jede Meldung. `anzahl=$(( anzahl + 1 ))` hätte den Status 0. Abbildung [37](#abb-37) zeigt, wo `set -e` wirkt.

:::abbildung linux/k10sete 37
Das Skript `abbruch.sh` als helle Dateiansicht, die Zeile `set -e` am Eingang als Wächter. Drei Aufrufe von `pruefen`: Hinter `||` und in der Bedingung von `if` steht daneben „Status geprüft: Wächter schaut weg“, `false` darin scheitert ohne Folgen; beim dritten, ungeprüften Aufruf greift er zu, das Skript endet mit `1`, die letzte Zeile bleibt grau. Darunter die Ausgabe des Laufs und eine Liste der Stellen, an denen der Wächter wegschaut: Bedingung von `if`/`while`/`until`, links von `&&`/`||`, vorn in einer Pipeline, hinter `!`.
:::

:::hintergrund Warum `set -e` so viele Ausnahmen hat
Der Exit-Status hat in der Shell zwei Aufgaben. Er beantwortet Fragen: `grep -q Butter einkauf.txt` mit dem Status 1 heißt „Butter steht nicht drauf“, nicht „grep ist kaputt“. Und er meldet Fehler. Die Shell kann beides nicht unterscheiden. `set -e` behandelt deshalb jeden Status ungleich 0 als Fehler, außer an den Stellen, an denen offensichtlich eine Frage gestellt wird; sonst könnte man in einem solchen Skript kein `if` mehr schreiben. Diese Stellen sind aber nur dort erkennbar, wo die Frage gestellt wird, nicht tiefer in einer Funktion. Der Standard für Unix-Shells rät deshalb ausdrücklich davon ab, sich in Funktionen auf `set -e` zu verlassen, und viele erfahrene Skriptautoren benutzen es gar nicht. Die Regel dieses Kapitels: Kritische Schritte prüft das Skript selbst (Abschnitt [8.3](#stufe-8-3)); wer `set -e` zusätzlich einschaltet, sollte seine Grenzen kennen.
:::

⁠**Kurz gesagt:** `set -e` bricht bei ungeprüften Fehlern ab, wirkt aber nicht in Bedingungen, in Ketten und in Funktionen, deren Status geprüft wird; ausdrückliche Prüfungen ersetzt es nicht.

### Fehler in Pipelines: `pipefail`

<span class="anker" id="stufe-8-6"></span>

[Kapitel 4, Abschnitt 6.5](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/befehle-verketten.html#stufe-6-5) hat gezeigt: Der Exit-Status einer Pipeline ist der ihres letzten Befehls. Scheitert ein Befehl weiter vorn, merkt ein Skript davon nichts.

:::definition Definition 8.6 (`pipefail`)
<span class="anker" id="satz-8-6"></span>

Nach __`set -o pipefail`__ ist der Exit-Status einer Pipeline der des letzten Befehls, der mit einem Status ungleich 0 geendet hat, und 0 nur, wenn alle Befehle Erfolg hatten. `set +o pipefail` schaltet die Einstellung ab.
:::

```console
$ grep Butter einkauf.txt | sort > butter.txt
$ echo $?
0
$ set -o pipefail
$ grep Butter einkauf.txt | sort > butter.txt
$ echo $?
1
$ set +o pipefail
```

Ohne `pipefail` meldet die Pipeline Erfolg, weil `sort` eine leere Eingabe tadellos sortiert hat; dass `grep` nichts gefunden hat, geht verloren. In Skripten setzt man `set -o pipefail` meist gleich oben, zusammen mit `set -u`. Es ändert nichts daran, dass man den Status der Pipeline dann auch prüfen muss.

⁠**Kurz gesagt:** Mit `set -o pipefail` meldet eine Pipeline einen Fehler, sobald irgendeiner ihrer Befehle scheitert, nicht nur der letzte.

:::aufgabe Aufgabe 28 ★ Exit-Status vorhersagen
<span class="anker" id="aufg-28"></span>

Sage für die fertige `zaehle.sh` Ausgabe und Exit-Status voraus: (a) `./zaehle.sh fotos`, (b) `./zaehle.sh "" einkauf.txt`, (c) `./zaehle.sh einkauf.txt einkauf.txt`, (d) `./zaehle.sh /etc/shadow`. Prüfe deine Vorhersagen.

:::loesung
```console
$ ./zaehle.sh fotos; echo $?
zaehle.sh: fotos: keine lesbare Datei
1
$ ./zaehle.sh "" einkauf.txt; echo $?
zaehle.sh: : keine lesbare Datei
einkauf.txt: 4 Zeilen
1
$ ./zaehle.sh einkauf.txt einkauf.txt; echo $?
einkauf.txt: 4 Zeilen
einkauf.txt: 4 Zeilen
0
$ ./zaehle.sh /etc/shadow; echo $?
zaehle.sh: /etc/shadow: keine lesbare Datei
1
```

(a) Ein Verzeichnis ist keine gewöhnliche Datei. (b) Das leere Argument zählt als Argument (also kein Status 2), ist aber keine Datei; die Meldung enthält deshalb den leeren Namen zwischen zwei Doppelpunkten. (c) Doppelte Namen zählt das Skript einfach zweimal. (d) `/etc/shadow` ist eine Datei, aber nicht lesbar; dafür steht die zweite Prüfung `[ ! -r "$datei" ]`.
:::
:::

:::aufgabe Aufgabe 29 ★★ Ein robustes Skript für Dateigrößen
<span class="anker" id="aufg-29"></span>

Schreibe nach dem Vorbild von `zaehle.sh` ein Skript `groesse.sh`, das für jede Datei die Größe in Byte ausgibt (`wc -c < datei`). Es soll einen Aufrufhinweis haben, Meldungen auf die Fehlerausgabe schreiben und die Exit-Status 0, 1 und 2 so verwenden wie `zaehle.sh`.

:::loesung
```bash groesse.sh
#!/bin/bash
# groesse.sh: gibt die Größe jeder angegebenen Datei in Byte aus
#   Aufruf:      groesse.sh DATEI...
#   Exit-Status: 0 alles gemessen, 1 mindestens eine Datei fehlte,
#                2 falscher Aufruf

programm=$(basename "$0")

if [ $# -eq 0 ]; then
    echo "Aufruf: $programm DATEI..." >&2
    exit 2
fi

status=0
for datei in "$@"; do
    if [ ! -f "$datei" ] || [ ! -r "$datei" ]; then
        echo "$programm: $datei: keine lesbare Datei" >&2
        status=1
        continue
    fi
    echo "$datei: $(wc -c < "$datei") Byte"
done
exit "$status"
```

```console
$ chmod +x groesse.sh
$ ./groesse.sh einkauf.txt "mein einkauf.txt" gibtsnicht.txt
einkauf.txt: 25 Byte
mein einkauf.txt: 25 Byte
groesse.sh: gibtsnicht.txt: keine lesbare Datei
$ echo $?
1
$ ./groesse.sh
Aufruf: groesse.sh DATEI...
$ echo $?
2
```

Beide Listen sind zufällig 25 Byte lang: $8+7+10=25$ für Tomaten, Nudeln und Basilikum.
:::
:::

:::aufgabe Aufgabe 30 ★★ Warum hält es nicht an?
<span class="anker" id="aufg-30"></span>

Ein Skript beginnt mit `set -e` und enthält `mkdir ablage && cp einkauf.txt ablage/`. Das Verzeichnis `ablage` gibt es schon, `mkdir` scheitert also. Läuft das Skript weiter? Warum? Und warum beendet sich ein anderes Skript mit `set -e` an der Zeile `(( fehler++ ))`, wenn `fehler` vorher 0 war? Wie schreibt man beide Stellen besser?

:::loesung
Das Skript `ablage.sh` enthält beide Stellen; das Verzeichnis `ablage` gibt es vor dem Lauf schon:

```bash ablage.sh
#!/bin/bash
# ablage.sh: set -e und eine Kette mit &&
set -e
mkdir ablage && cp einkauf.txt ablage/
echo "weiter nach mkdir && cp"
fehler=0
(( fehler++ ))
echo "diese Zeile erscheint nie"
```

```console
$ bash ablage.sh
mkdir: ablage: File exists
weiter nach mkdir && cp
$ echo $?
1
$ ls ablage
```

`mkdir` steht links von `&&`; dort ist sein Status eine Frage, und `set -e` greift nicht. Das Skript läuft weiter, aber `cp` ist nie gelaufen, das Verzeichnis bleibt leer. `(( fehler++ ))` hat den Wert 0 und damit den Status 1, und weil dieser Status nicht geprüft wird, beendet `set -e` das Skript ohne Meldung. Besser: `mkdir -p ablage`, das ein vorhandenes Verzeichnis nicht als Fehler zählt, dann `cp einkauf.txt ablage/ || exit 1`, und `fehler=$(( fehler + 1 ))`. Die Meldung `mkdir: ablage: File exists` ist die der uutils-Fassung in Ubuntu 26.04; GNU `mkdir` schreibt `cannot create directory 'ablage': File exists`.
:::
:::

:::aufgabe Aufgabe 31 ★★ `pipefail` mit `ls`
<span class="anker" id="aufg-31"></span>

Sage voraus, welchen Exit-Status `ls gibtsnicht | wc -l` ohne und mit `pipefail` hat, und prüfe beides jeweils direkt danach mit `echo $? "${PIPESTATUS[@]}"`. Warum muss `$?` in derselben Zeile stehen wie `PIPESTATUS`?

:::loesung
```console
$ ls gibtsnicht | wc -l
ls: cannot access 'gibtsnicht': No such file or directory
0
$ echo $? "${PIPESTATUS[@]}"
0 2 0
$ set -o pipefail
$ ls gibtsnicht | wc -l
ls: cannot access 'gibtsnicht': No such file or directory
0
$ echo $? "${PIPESTATUS[@]}"
2 2 0
$ set +o pipefail
```

Ohne `pipefail` gilt der Status von `wc`, also 0; mit `pipefail` der von `ls`, also 2 ([Kapitel 4, Abschnitt 5.2](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/der-exit-status.html#stufe-5-2)). `PIPESTATUS` zeigt beide Male `2 0`. Beide Werte gehören zur letzten Pipeline, und jeder neue Befehl, auch ein `echo`, überschreibt sie; deshalb liest man beide in derselben Zeile aus. Stünde `echo $?` in einer eigenen Zeile davor, zeigte `PIPESTATUS` danach nur noch den Status dieses `echo`.
:::
:::

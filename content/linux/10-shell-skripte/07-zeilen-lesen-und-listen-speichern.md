---
title: Zeilen lesen und Listen speichern
pfad: Informatik / Linux und Kommandozeile / Shell-Skripte
adresse: informatik/linux-und-kommandozeile/shell-skripte
knoten: Kapitel 10: Shell-Skripte
order: 6150700
summary: Viele Daten stehen zeilenweise in Dateien: Einkaufslisten, Protokolle, Tabellen.
tags: read -r name …, IFS, Array
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Viele Daten stehen zeilenweise in Dateien: Einkaufslisten, Protokolle, Tabellen. Dieser Abschnitt zeigt, wie ein Skript Zeilen liest und in Felder zerlegt, warum eine Schleife hinter einer Pipe ihre Ergebnisse verliert und wie man mehrere Werte in einer einzigen Variablen aufbewahrt.
:::

### Der Befehl `read`

<span class="anker" id="stufe-6-1"></span>

Ein Skript soll eine Antwort von der Tastatur entgegennehmen oder eine Zeile aus einer Datei in Variablen ablegen. Dafür gibt es einen eingebauten Befehl, der genau eine Zeile von der Standardeingabe liest.

:::definition Definition 6.1 (`read`)
<span class="anker" id="satz-6-1"></span>

Der eingebaute Befehl __`read -r name …`__ liest eine Zeile von der Standardeingabe, zerlegt sie an Leerzeichen und Tabulatoren in Wörter und weist das erste Wort der ersten Variablen zu, das zweite der zweiten und so weiter; die letzte Variable bekommt den ganzen Rest der Zeile. Fehlen Wörter, bleiben die übrigen Variablen leer. `read` endet mit dem Status 0, wenn es eine Zeile gelesen hat, und mit 1, wenn der Strom zu Ende ist. Die Option `-p text` gibt vorher eine Eingabeaufforderung aus.
:::

```console
$ read -r -p "Wie heißt du? " name
Wie heißt du? Anna
$ echo "Hallo, $name!"
Hallo, Anna!
```

Hinter dem Fragezeichen wartet `read`, bis du `Anna` tippst und die Eingabetaste drückst. Mit mehreren Variablen und einem Here-String als Eingabe ([Kapitel 4, Abschnitt 3.3](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/eingaben-umleiten.html#stufe-3-3)):

```console
$ read -r vorname rest <<< "Anna Maria Berg"
$ echo "Vorname: $vorname, Rest: $rest"
Vorname: Anna, Rest: Maria Berg
```

Die Option `-r` („raw“, roh) sorgt dafür, dass `read` einen umgekehrten Schrägstrich als gewöhnliches Zeichen behandelt. Ohne sie entfernt es ihn und nimmt das folgende Zeichen als gewöhnliches Zeichen:

```console
$ read -r pfad <<< 'C:\Fotos\neu'
$ echo "$pfad"
C:\Fotos\neu
$ read pfad <<< 'C:\Fotos\neu'
$ echo "$pfad"
C:Fotosneu
```

Deshalb schreibt man `read` praktisch immer mit `-r`. Abbildung [24](#abb-24) zeigt die Verteilung auf die Variablen.

:::abbildung linux/k10read 24
Eine Zeile `Anna Maria Berg` läuft auf ein Förderband und wird an den Leerzeichen in drei Wörter geschnitten. Darunter zwei Schubladen `vorname` und `rest`: `Anna` fällt in die erste; weil es keine weitere Schublade gibt, fallen `Maria` und `Berg` samt dem Leerzeichen dazwischen zusammen in die letzte. Am Ende hält `read` das Schild `0`.
:::

⁠**Kurz gesagt:** `read -r a b` liest eine Zeile, legt das erste Wort in `a` und den Rest in `b`; am Ende des Stroms endet es mit 1.

### Eine Datei Zeile für Zeile lesen

<span class="anker" id="stufe-6-2"></span>

`read` liest eine Zeile und meldet am Ende des Stroms den Status 1. Genau so etwas braucht die `while`-Schleife als Bedingung: Sie soll laufen, solange es noch eine Zeile gibt.

:::satz Satz 6.2 (Zeilen lesen mit `while read`)
<span class="anker" id="satz-6-2"></span>

Die Schleife `while read -r zeile; do befehle; done < datei` leitet die Datei in die Standardeingabe der ganzen Schleife um. Jeder Aufruf von `read` liest die nächste Zeile in die Variable; nach der letzten Zeile liefert `read` den Status 1, und die Schleife endet.
:::

Die Umleitung steht hinter `done`, damit sie für die ganze Schleife gilt; die Datei wird einmal geöffnet, und jedes `read` liest dort weiter, wo das vorige aufgehört hat.

```console
$ while read -r zeile; do echo "- $zeile"; done < einkauf.txt
- Milch
- Brot
- Äpfel
- Kaffee
```

Abbildung [25](#abb-25) zeigt das Zusammenspiel. Eine Falle betrifft die letzte Zeile: Fehlt ihr das Zeilenende, liest `read` sie zwar in die Variable, meldet aber trotzdem den Status 1, weil der Strom zu Ende ist; die Schleife bearbeitet sie nicht mehr. Abhilfe schafft eine zweite Bedingung, die nachsieht, ob noch etwas in der Variablen steht:

```console
$ printf 'Milch\nBrot' > ohne_ende.txt
$ while read -r zeile; do echo "- $zeile"; done < ohne_ende.txt
- Milch
$ while read -r zeile || [ -n "$zeile" ]; do echo "- $zeile"; done < ohne_ende.txt
- Milch
- Brot
```

Textdateien, die unter Linux entstehen, enden fast immer mit einem Zeilenende; Dateien aus anderen Quellen nicht immer.

:::abbildung linux/k10whileread 25
Links die Datei `einkauf.txt` mit vier Zeilen und einem Lesezeichen. Ein Rohr `< einkauf.txt` führt in die Schleife. Bei jedem Durchgang holt `read` die Zeile am Lesezeichen in die Schublade `zeile`, das Lesezeichen rückt eine Zeile weiter, rechts erscheint `- Milch`, `- Brot` und so weiter. Nach `Kaffee` greift `read` ins Leere, hält `1` hoch, und die Schleife endet. Unten ein zweiter Durchgang mit `ohne_ende.txt`: `Brot` ohne Zeilenende landet in der Schublade, aber `read` hält trotzdem `1` hoch.
:::

⁠**Kurz gesagt:** `while read -r zeile; do …; done < datei` bearbeitet eine Datei Zeile für Zeile, bis `read` das Ende meldet.

### Felder trennen: `IFS`

<span class="anker" id="stufe-6-3"></span>

Eine CSV-Datei trennt ihre Felder mit Kommas ([Kapitel 6, Abschnitt 1.3](/wissen/informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke/textdaten-datensatze-felder-und-zeilenenden.html#stufe-1-3)). `read` trennt aber an Leerzeichen. Lege für die folgenden Beispiele das Lauftagebuch aus [Kapitel 6](/wissen/informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke/textwerkzeuge-und-regulaere-ausdruecke.html) mit einem Here-Document an ([Kapitel 4, Abschnitt 3.2](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/eingaben-umleiten.html#stufe-3-2)):

```console
$ cat > laeufe.csv << 'ENDE'
> datum,name,km,minuten
> 2026-11-02,Anna,5.0,28
> 2026-11-02,Ben,10.5,62
> 2026-11-03,Clara,7.2,41
> 2026-11-04,Anna,6.4,35
> 2026-11-05,Ben,5.0,31
> 2026-11-06,Anna,12.0,70
> 2026-11-07,Clara,8.0,44
> 2026-11-08,Ben,21.1,128
> 2026-11-09,Anna,5.0,27
> ENDE
```

:::definition Definition 6.3 (`IFS`)
<span class="anker" id="satz-6-3"></span>

Die Shell-Variable __`IFS`__ enthält die Zeichen, an denen die Shell Wörter trennt, beim Zerlegen von Ersetzungen ebenso wie in `read`. Voreingestellt sind Leerzeichen, Tabulator und Zeilenende. `IFS=, read -r a b c` setzt sie nur für diesen einen `read`-Befehl auf das Komma.
:::

Der Name steht für „internal field separator“, internes Feldtrennzeichen. Die Form `IFS=, read` ist eine Zuweisung vor einem Befehl ([Kapitel 5, Abschnitt 4.6](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/umgebung-und-vererbung.html#stufe-4-6)): Die übrige Shell trennt danach wieder wie gewohnt. Genau genommen verbindet auch `"$*"` aus Abschnitt [2.5](argumente-ubergeben-positionsparameter.html#stufe-2-5) die Argumente mit dem ersten Zeichen von `IFS`; voreingestellt ist das das Leerzeichen.

```console
$ IFS=, read -r datum name km minuten <<< "2026-11-02,Anna,5.0,28"
$ echo "$name: $km km"
Anna: 5.0 km
```

In einer Schleife wird daraus ein kleiner Bericht. `tail -n +2` lässt die Kopfzeile weg ([Kapitel 6, Abschnitt 1.5](/wissen/informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke/textdaten-datensatze-felder-und-zeilenenden.html#stufe-1-5)), und eine Pipe führt die übrigen Zeilen in die Schleife:

```bash laeufe.sh
#!/bin/bash
# laeufe.sh: schreibt jeden Lauf aus laeufe.csv als Satz
tail -n +2 laeufe.csv | while IFS=, read -r datum name km minuten; do
    echo "$datum: $name lief $km km in $minuten Minuten."
done
```

```console
$ chmod +x laeufe.sh
$ ./laeufe.sh
2026-11-02: Anna lief 5.0 km in 28 Minuten.
2026-11-02: Ben lief 10.5 km in 62 Minuten.
2026-11-03: Clara lief 7.2 km in 41 Minuten.
2026-11-04: Anna lief 6.4 km in 35 Minuten.
2026-11-05: Ben lief 5.0 km in 31 Minuten.
2026-11-06: Anna lief 12.0 km in 70 Minuten.
2026-11-07: Clara lief 8.0 km in 44 Minuten.
2026-11-08: Ben lief 21.1 km in 128 Minuten.
2026-11-09: Anna lief 5.0 km in 27 Minuten.
```

Abbildung [26](#abb-26) zeigt das Zerlegen einer Zeile.

:::abbildung linux/k10ifs 26
Die Zeile `2026-11-02,Anna,5.0,28` auf einem Förderband. Ein Schild `IFS=,` hängt über einer Schere, die nur an Kommas schneidet. Die vier Stücke fallen in die Schubladen `datum`, `name`, `km`, `minuten`. Darunter zum Vergleich dieselbe Zeile mit der Voreinstellung: Die Schere findet kein Leerzeichen, die ganze Zeile fällt in die erste Schublade.
:::

:::hintergrund Leerzeichen am Rand einer Zeile
Auch mit nur einer Variablen entfernt `read` Leerzeichen und Tabulatoren am Anfang und Ende der Zeile, weil sie zu `IFS` gehören. Für eingerückte Texte, etwa Programmzeilen, ist das falsch. Mit `IFS= read -r zeile`, also einem leeren `IFS` nur für diesen Befehl, bleibt die Zeile Zeichen für Zeichen erhalten. Die vollständige Form einer Leseschleife, die nichts verändert, ist deshalb `while IFS= read -r zeile || [ -n "$zeile" ]; do`.
:::

⁠**Kurz gesagt:** `IFS` legt fest, wo Wörter enden; `IFS=, read -r a b c` zerlegt eine Zeile an Kommas.

### Die Pipe-Falle

<span class="anker" id="stufe-6-4"></span>

Jetzt sollen die Minuten aller Läufe zusammengezählt werden. Das Skript sieht aus wie `laeufe.sh`, nur addiert es im Schleifenkörper, statt auszugeben. Es braucht nur das vierte Feld; die drei übrigen liest es in eine Variable mit dem Namen `_` (Unterstrich). Das ist ein üblicher Platzhalter, der zeigt, dass ein Feld absichtlich übergangen wird:

```bash minuten.sh
#!/bin/bash
# minuten.sh: zählt die Minuten aller Läufe zusammen (fehlerhaft)
summe=0
tail -n +2 laeufe.csv | while IFS=, read -r _ _ _ minuten; do
    summe=$(( summe + minuten ))
done
echo "Zusammen: $summe Minuten"
```

```console
$ chmod +x minuten.sh
$ ./minuten.sh
Zusammen: 0 Minuten
```

In [Kapitel 6, Abschnitt 2.3](/wissen/informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke/spalten-ausschneiden-und-zeichen-ersetzen-cut-tr-und-paste.html#stufe-2-3) kam für dieselben Läufe 466 heraus. Die Schleife hat richtig gerechnet, aber an der falschen Stelle.

:::satz Satz 6.4 (Die Pipe-Falle)
<span class="anker" id="satz-6-4"></span>

Jeder Befehl einer Pipeline mit mehr als einem Befehl läuft in einem eigenen Kindprozess der Shell, auch eine Schleife. Variablen, die eine Schleife hinter `|` setzt, gehören zu diesem Kindprozess und sind verloren, wenn er endet; die Shell, die nach der Pipeline weiterarbeitet, sieht ihre alten Werte.
:::

Das ist die Regel aus Abschnitt [1.5](vom-befehl-zum-skript.html#stufe-1-5), angewandt auf die Teile einer Pipeline: Der Kindprozess hat eine Kopie von `summe` hochgezählt, das Original blieb 0. Abbildung [27](#abb-27) zeigt die beiden Prozesse. Die Abhilfe: Die Schleife darf nicht hinter einer Pipe stehen. Leitet man die Datei mit `<` direkt in die Schleife um, läuft sie in der Shell des Skripts selbst; die Kopfzeile erkennt das Skript am ersten Feld und überspringt sie mit `continue`:

```bash minuten.sh
#!/bin/bash
# minuten.sh: zählt die Minuten aller Läufe zusammen
summe=0
while IFS=, read -r datum _ _ minuten; do
    if [ "$datum" = datum ]; then
        continue    # die Kopfzeile überspringen
    fi
    summe=$(( summe + minuten ))
done < laeufe.csv
echo "Zusammen: $summe Minuten"
```

```console
$ ./minuten.sh
Zusammen: 466 Minuten
```

Soll die Eingabe trotzdem von einem Befehl kommen, hilft die Prozesssubstitution `<(befehl)` aus [Kapitel 4, Abschnitt 7.5](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/aus-einer-ausgabe-argumente-machen.html#stufe-7-5): Die Shell startet den Befehl und setzt an seiner Stelle den Namen einer Datei ein, aus der man seine Ausgabe lesen kann. Mit `done < <(befehl)` liest die Schleife diese Datei, wieder ohne Pipe:

```console
$ n=0
$ while read -r zeile; do n=$(( n + 1 )); done < <(tail -n +2 laeufe.csv)
$ echo "$n Läufe"
9 Läufe
```

Zwischen den beiden `<` steht ein Leerzeichen: Das erste ist die Umleitung, das zweite gehört zu `<(…)`.

:::abbildung linux/k10pipefalle 27
Oben das Skript als Kasten „Shell des Skripts“ mit einer Schublade `summe = 0`. Bei der Pipeline wachsen zwei Kindprozesse heraus: `tail` links, die `while`-Schleife rechts, verbunden durch ein Rohr. Der rechte Kindprozess bekommt eine Kopie der Schublade und zählt sie hoch: 28, 90, 131, …, 466. Dann verschwinden beide Kindprozesse samt Kopie; `echo` in der Shell liest die Original-Schublade: `0`. Unten der richtige Weg: `done < laeufe.csv`, die Schleife läuft im Kasten der Shell selbst, die Schublade zeigt am Ende `466`.
:::

:::hintergrund Warum eine Pipe Kindprozesse braucht
Die Befehle einer Pipeline laufen gleichzeitig: Der erste schreibt, während der zweite schon liest ([Kapitel 4, Abschnitt 4.1](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/pipes-und-filter.html#stufe-4-1)). Die Shell selbst arbeitet ihre Befehle aber nacheinander ab; sie kann nicht zugleich den ersten Befehl ausführen und in einer Schleife die Ausgabe lesen. Also startet die Shell für jeden Befehl der Pipeline einen eigenen Prozess, auch für eingebaute Befehle und Schleifen, die sie sonst selbst ausführen würde. Der Standard für Unix-Shells lässt offen, ob der letzte Befehl stattdessen in der Shell selbst laufen darf. Die KornShell und die zsh tun das, dort stimmt `summe` nach der Schleife; die bash startet auch für den letzten Befehl einen Kindprozess. In Skripten kann man das mit `shopt -s lastpipe` ändern; das wirkt aber nur, wenn die Shell keine Jobs verwaltet ([Kapitel 8, Abschnitt 3.3](/wissen/informatik/linux-und-kommandozeile/prozesse-signale-und-dienste/vordergrund-hintergrund-und-jobs.html#stufe-3-3)), also in Skripten, nicht in der interaktiven Shell. Verlässlicher ist es, die Schleife gar nicht erst hinter eine Pipe zu stellen.
:::

⁠**Kurz gesagt:** Eine Schleife hinter `|` läuft in einem Kindprozess und verliert ihre Variablen; `done < datei` oder `done < <(befehl)` hält sie in der eigenen Shell.

### Das Array

<span class="anker" id="stufe-6-5"></span>

Ein Skript will sich eine Liste von Dateinamen merken, um sie später zu zählen oder an einen Befehl weiterzugeben. In einer gewöhnlichen Variablen ginge das nur als Text mit Leerzeichen dazwischen, und dann zerbrechen Namen wie `strand 1.jpg`. Die bash hat dafür eine eigene Art Variable.

Ein Bild zur Orientierung: ein Regal mit nummerierten Fächern unter einem gemeinsamen Namen. Jedes Fach enthält einen eigenen Text, und die Grenzen zwischen den Fächern bleiben erhalten.

:::definition Definition 6.5 (Array)
<span class="anker" id="satz-6-5"></span>

Ein __Array__ ist eine Variable, die mehrere Texte unter fortlaufenden Nummern ab 0 enthält, den Elementen. `name=(a b c)` legt es an, `${name[0]}` ist das erste Element, `"${name[@]}"` sind alle Elemente als eigene Wörter, `${#name[@]}` ist ihre Anzahl, und `name+=(d)` hängt ein Element an.
:::

Die geschweiften Klammern sind nötig; `$name[0]` wäre der Inhalt von `$name` gefolgt vom Text `[0]`. `"${name[@]}"` verhält sich wie `"$@"`: Jedes Element wird ein eigenes, unverändertes Wort.

```console
$ fotos=("strand 1.jpg" "strand 2.jpg" berg.png)
$ echo "${#fotos[@]}"
3
$ echo "${fotos[0]}"
strand 1.jpg
$ echo "${fotos[2]}"
berg.png
$ for f in "${fotos[@]}"; do echo "[$f]"; done
[strand 1.jpg]
[strand 2.jpg]
[berg.png]
$ fotos+=(neu.jpg)
$ echo "${#fotos[@]}"
4
```

Besonders nützlich ist ein Array zusammen mit der Pfadnamen-Erweiterung: `bilder=(fotos/*.jpg)` legt jeden passenden Namen in ein eigenes Element.

```console
$ bilder=(fotos/*.jpg)
$ echo "${#bilder[@]} Bilder"
2 Bilder
$ printf '%s\n' "${bilder[@]}"
fotos/strand 1.jpg
fotos/strand 2.jpg
```

Ein Array der Shell selbst ist schon in [Kapitel 4, Abschnitt 6.5](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/befehle-verketten.html#stufe-6-5) vorgekommen: `PIPESTATUS` enthält den Exit-Status jedes Befehls der letzten Pipeline, von links nach rechts.

```console
$ grep Butter einkauf.txt | sort
$ echo "${PIPESTATUS[@]}"
1 0
```

Abbildung [28](#abb-28) zeigt das Regal.

:::abbildung linux/k10array 28
Ein Regal `fotos` mit Fächern, die unten die Nummern 0, 1, 2 tragen; darin `strand 1.jpg`, `strand 2.jpg`, `berg.png`. Ein Zeiger auf Fach 0 erklärt `${fotos[0]}`, ein Zähler daneben `${#fotos[@]} = 3`. Bei `fotos+=(neu.jpg)` kommt Fach 3 mit `neu.jpg` dazu, der Zähler springt auf 4. Zum Schluss fließen alle Fächer über `"${fotos[@]}"` als vier getrennte Kärtchen in eine Schleife.
:::

:::hintergrund Arrays mit Namen statt Nummern
Die bash kennt auch Arrays, deren Fächer Namen statt Nummern tragen, so wie die assoziativen Arrays von `awk` ([Kapitel 6, Abschnitt 9.5](/wissen/informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke/rechnen-mit-spalten-awk.html#stufe-9-5)). Man legt sie mit `declare -A name` an und schreibt dann etwa `minuten[Anna]=160`. Die ursprüngliche Bourne-Shell und der Standard für Unix-Shells kennen gar keine Arrays; deshalb kommen sie in älteren Skripten selten vor.
:::

⁠**Kurz gesagt:** Ein Array hält mehrere Texte unter Nummern ab 0; `"${name[@]}"` liefert sie als getrennte Wörter, `${#name[@]}` ihre Anzahl.

:::aufgabe Aufgabe 19 ★ Eine kleine Umfrage
<span class="anker" id="aufg-19"></span>

Schreibe ein Skript `frage.sh`, das mit `read -r -p` nach dem Namen und nach dem Lieblingsobst fragt und dann einen Satz wie `Anna isst gern Kiwi.` ausgibt. Was geschieht, wenn du beim Namen `Anna Berg` eingibst, und was, wenn `read` zwei Variablen `vorname nachname` bekommt?

:::loesung
```bash frage.sh
#!/bin/bash
# frage.sh: fragt nach Name und Lieblingsobst
read -r -p "Wie heißt du? " name
read -r -p "Welches Obst isst du am liebsten? " obst
echo "$name isst gern $obst."
```

```console
$ chmod +x frage.sh
$ ./frage.sh
Wie heißt du? Anna Berg
Welches Obst isst du am liebsten? Kiwi
Anna Berg isst gern Kiwi.
$ read -r vorname nachname <<< "Anna Maria Berg"
$ echo "[$vorname] [$nachname]"
[Anna] [Maria Berg]
```

Mit einer einzigen Variablen bekommt diese die ganze Zeile, also `Anna Berg`. Mit zwei Variablen landet das erste Wort in der ersten, der ganze Rest in der letzten; bei drei Namen gehören zwei zum Nachnamen.
:::
:::

:::aufgabe Aufgabe 20 ★★ Annas Läufe
<span class="anker" id="aufg-20"></span>

Schreibe ein Skript, das `laeufe.csv` mit einer `while-read`-Schleife liest und am Ende ausgibt, wie viele Läufe Anna gemacht hat und wie viele Minuten sie zusammen gelaufen ist. Benutze nur die Shell, kein `awk`.

:::loesung
Die Schleife liest die Datei direkt, ohne Pipe, damit die Zähler nach der Schleife erhalten bleiben. Die Kopfzeile stört nicht, denn ihr Feld `name` ist nicht `Anna`:

```bash anna.sh
#!/bin/bash
# anna.sh: Läufe und Minuten von Anna aus laeufe.csv
laeufe=0
summe=0
while IFS=, read -r _ name _ minuten; do
    if [ "$name" = Anna ]; then
        laeufe=$(( laeufe + 1 ))
        summe=$(( summe + minuten ))
    fi
done < laeufe.csv
echo "Anna: $laeufe Läufe, $summe Minuten"
```

```console
$ chmod +x anna.sh
$ ./anna.sh
Anna: 4 Läufe, 160 Minuten
```

Probe: $28+35+70+27=160$, dieselbe Zahl wie in [Kapitel 6, Abschnitt 9.5](/wissen/informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke/rechnen-mit-spalten-awk.html#stufe-9-5). Datum und Kilometer werden nicht gebraucht und landen im Platzhalter `_`; er muss trotzdem dastehen, damit `minuten` das vierte Feld bekommt.
:::
:::

:::aufgabe Aufgabe 21 ★★ Ein Bericht über mehrere Tabellen
<span class="anker" id="aufg-21"></span>

Lege mit einem Here-Document eine zweite Datei `dezember.csv` im Format von `laeufe.csv` mit drei Läufen an. Schreibe ein Skript `bericht.sh`, das für jede Datei mit der Endung `.csv` im Arbeitsverzeichnis eine Zeile mit dem Dateinamen, der Zahl der Läufe und den gesamten Kilometern ausgibt. Rechne die Kilometer mit `awk` ([Kapitel 6, Abschnitt 9.4](/wissen/informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke/rechnen-mit-spalten-awk.html#stufe-9-4)), denn die Shell rechnet nur mit ganzen Zahlen.

:::loesung
```console
$ cat > dezember.csv << 'ENDE'
> datum,name,km,minuten
> 2026-12-01,Anna,5.0,29
> 2026-12-03,Ben,8.4,49
> 2026-12-05,Clara,6.0,34
> ENDE
```

Die Zahl der Läufe ist die Zahl der Zeilen minus der Kopfzeile. Die Kilometer haben Nachkommastellen, deshalb summiert sie `awk`; `printf "%.1f"` gibt eine Nachkommastelle aus ([Kapitel 6, Abschnitt 9.4](/wissen/informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke/rechnen-mit-spalten-awk.html#stufe-9-4)):

```bash bericht.sh
#!/bin/bash
# bericht.sh: Zahl der Läufe und Kilometer für jede CSV-Datei
for datei in *.csv; do
    [ -f "$datei" ] || continue
    laeufe=$(( $(wc -l < "$datei") - 1 ))
    km=$(awk -F, 'NR > 1 { s += $3 } END { printf "%.1f", s }' "$datei")
    echo "$datei: $laeufe Läufe, $km km"
done
```

```console
$ chmod +x bericht.sh
$ ./bericht.sh
dezember.csv: 3 Läufe, 19.4 km
laeufe.csv: 9 Läufe, 80.2 km
```

Probe: $5{,}0+8{,}4+6{,}0=19{,}4$; die 80,2 km von `laeufe.csv` kennt man aus [Kapitel 6](/wissen/informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke/textwerkzeuge-und-regulaere-ausdruecke.html). Die Shell arbeitet die Dateien ab, `awk` rechnet; jedes Werkzeug tut, was es kann.
:::
:::

:::aufgabe Aufgabe 22 ★★ Die Pipe-Falle vorhersagen
<span class="anker" id="aufg-22"></span>

Sage für jede der drei Zeilen (a) bis (c) voraus, was sie ausgibt, und prüfe es:

```console
$ echo Brot | read -r brot; echo "[$brot]"
$ read -r brot <<< Brot; echo "[$brot]"
$ n=0; printf 'a\nb\n' | while read -r z; do n=$((n+1)); echo "innen $n"; done; echo "außen $n"
```

:::loesung
```console
$ echo Brot | read -r brot; echo "[$brot]"
[]
$ read -r brot <<< Brot; echo "[$brot]"
[Brot]
$ n=0; printf 'a\nb\n' | while read -r z; do n=$((n+1)); echo "innen $n"; done; echo "außen $n"
innen 1
innen 2
außen 0
```

(a) `read` steht hinter einer Pipe und läuft in einem Kindprozess; die Variable verschwindet mit ihm, in der Shell bleibt `brot` leer. (b) Der Here-String braucht keine Pipe, `read` läuft in der eigenen Shell. (c) Innerhalb der Schleife zählt die Kopie richtig, außerhalb sieht man den alten Wert.
:::
:::

:::aufgabe Aufgabe 23 ★ Ein Array von Skripten
<span class="anker" id="aufg-23"></span>

Lege alle Dateien mit der Endung `.sh` im Übungsverzeichnis in einem Array ab. Gib aus, wie viele es sind, welches das erste und welches das letzte ist. Das letzte Element hat die Nummer „Anzahl minus eins“; rechne sie mit `$(( ))` aus.

:::loesung
```console
$ skripte=(*.sh)
$ echo "${#skripte[@]}"
25
$ echo "${skripte[0]}"
alle.sh
$ letzte=$(( ${#skripte[@]} - 1 ))
$ echo "${skripte[$letzte]}"
zeige.sh
```

Die Zahl hängt davon ab, welche Skripte du angelegt hast; im Testsystem waren es 25. Die Pfadnamen-Erweiterung sortiert die Namen, deshalb ist `alle.sh` vorn und `zeige.sh` hinten. Die Nummern beginnen bei 0, daher ist die letzte „Anzahl minus eins“.
:::
:::

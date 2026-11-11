---
title: Suchen mit grep
pfad: Informatik / Linux und Kommandozeile / Textwerkzeuge und reguläre Ausdrücke
adresse: informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke
knoten: Kapitel 6: Textwerkzeuge und reguläre Ausdrücke
order: 6110600
summary: grep hat in Kapitel 4 Zeilen mit einem Wort herausgesucht.
tags: grep
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
`grep` hat in [Kapitel 4](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/stroeme-umleitung-pipes-und-exit-status.html) Zeilen mit einem Wort herausgesucht. Dieser Abschnitt zeigt, was `grep` genau tut und wie seine wichtigsten Optionen eine Suche umkehren, zählen, nummerieren, auf die Treffer beschränken und auf ganze Verzeichnisse ausdehnen.
:::

### Zeilen mit einem Suchtext: grep

<span class="anker" id="stufe-5-1"></span>

Aus einer langen Datei will man oft nur die Zeilen, die etwas Bestimmtes enthalten: alle Läufe von Clara, alle Meldungen eines Programms an einem bestimmten Tag.

:::definition Definition 5.1 (grep)
<span class="anker" id="satz-5-1"></span>

Der Befehl __grep__ bekommt nach den Optionen als erstes Argument einen Suchtext und danach Dateien. Er schreibt jede Zeile dieser Dateien aus, in der der Suchtext irgendwo vorkommt, und lässt die übrigen weg. Ohne Dateien liest er seine Standardeingabe. Sein Exit-Status ist 0, wenn mindestens eine Zeile passte, 1, wenn keine passte, und 2 bei einem Fehler.
:::

Groß- und Kleinschreibung zählen: `clara` ist ein anderer Suchtext als `Clara`. Wie man den Exit-Status mit `grep -q` ohne Ausgabe für Entscheidungen nutzt, hat [Kapitel 4, Abschnitt 5.2](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/der-exit-status.html#stufe-5-2) gezeigt.

::::beispiel Claras Läufe
```console
$ grep Clara laeufe.csv
2026-11-03,Clara,7.2,41
2026-11-07,Clara,8.0,44
$ grep clara laeufe.csv
$ echo $?
1
```

Mit kleinem c findet `grep` nichts, schreibt nichts und meldet den Exit-Status 1.
::::

⁠**Kurz gesagt:** `grep suchtext datei` schreibt die Zeilen, die den Suchtext enthalten; der Exit-Status sagt, ob es welche gab.

:::hintergrund Woher der Name grep kommt
Der Name stammt aus dem Texteditor `ed`, mit dem man in den Anfangsjahren von Unix Dateien bearbeitete. Dort hieß der Befehl, der alle Zeilen mit einem bestimmten Inhalt ausgibt, `g/re/p`: `g` für „global“, alle Zeilen, `re` für den Suchausdruck und `p` für „print“, ausgeben. Ken Thompson machte aus diesem einen Befehl um 1973 ein eigenes kleines Programm, das man mit jeder Datei und hinter jeder Pipe benutzen kann, ganz im Sinn der Unix-Philosophie aus [Kapitel 4, Abschnitt 4.5](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/pipes-und-filter.html#stufe-4-5).
:::

### Umkehren, zählen, nummerieren: -i, -v, -c und -n

<span class="anker" id="stufe-5-2"></span>

Oft ist die Frage etwas anders gestellt als „welche Zeilen enthalten das Wort“: Welche enthalten es nicht? Wie viele sind es? Wo in der Datei stehen sie? Abbildung [15](#abb-15) zeigt, wie vier Optionen dieselbe Suche verändern.

:::abbildung linux/k6grep 15
Das Lauftagebuch mit seinen zehn Zeilen und dem Suchtext `Anna`. Ohne Option leuchten die vier Zeilen mit Anna auf. `-v` kehrt um: Jetzt leuchten die sechs anderen. `-c` ersetzt die Zeilen durch ihre Anzahl, 4. `-n` setzt vor jede Trefferzeile ihre Nummer, 2, 5, 7 und 10.
:::

:::definition Definition 5.2 (Optionen von grep)
<span class="anker" id="satz-5-2"></span>

`-i` lässt Groß- und Kleinschreibung beim Vergleich außer Acht. `-v` kehrt die Auswahl um und schreibt die Zeilen, in denen der Suchtext nicht vorkommt. `-c` schreibt statt der Zeilen nur ihre Anzahl. `-n` setzt vor jede ausgegebene Zeile ihre Nummer in der Datei und einen Doppelpunkt.
:::

::::beispiel Vier Fragen an das Lauftagebuch
```console
$ grep -i clara laeufe.csv
2026-11-03,Clara,7.2,41
2026-11-07,Clara,8.0,44
$ grep -v Anna laeufe.csv
datum,name,km,minuten
2026-11-02,Ben,10.5,62
2026-11-03,Clara,7.2,41
2026-11-05,Ben,5.0,31
2026-11-07,Clara,8.0,44
2026-11-08,Ben,21.1,128
$ grep -n Ben laeufe.csv
3:2026-11-02,Ben,10.5,62
6:2026-11-05,Ben,5.0,31
9:2026-11-08,Ben,21.1,128
$ grep -c Anna laeufe.csv
4
```

`-v` liefert auch die Kopfzeile, denn auch in ihr kommt `Anna` nicht vor. Die Nummern bei `-n` zählen die Kopfzeile als Zeile 1 mit.
::::

::::beispiel [Zweites Beispiel] grep als erste Stufe
Als Filter passt `grep` an den Anfang einer Pipeline. Welche Strecken ist Anna gelaufen?

```console
$ grep Anna laeufe.csv | cut -d, -f3 | paste -s -d' '
5.0 6.4 12.0 5.0
```
::::

⁠**Kurz gesagt:** `-i` ohne Rücksicht auf Groß und klein, `-v` die anderen Zeilen, `-c` ihre Anzahl, `-n` mit Zeilennummer.

### Nur den Treffer ausgeben: -o

<span class="anker" id="stufe-5-3"></span>

`grep` schreibt normalerweise die ganze Zeile. Manchmal interessiert aber nur das Stück, das gepasst hat, etwa um zu zählen, wie oft etwas vorkommt, und nicht, in wie vielen Zeilen. Abbildung [16](#abb-16) zeigt den Unterschied.

:::abbildung linux/k6grepo 16
Die Zeile `Anna und Anna` mit zwei Treffern für `Anna`. `grep -c` zählt Zeilen und meldet 1. `grep -o` hebt die beiden Treffer heraus und schreibt jeden auf eine eigene Zeile; `wc -l` zählt diese Zeilen und meldet 2.
:::

:::definition Definition 5.3 (grep -o)
<span class="anker" id="satz-5-3"></span>

Mit der Option `-o` schreibt `grep` statt der ganzen Zeile nur die Stücke, die zum Suchtext passen, jedes auf eine eigene Zeile. Kommt der Suchtext in einer Zeile mehrmals vor, entstehen mehrere Ausgabezeilen.
:::

::::beispiel Zeilen zählen oder Treffer zählen
```console
$ echo 'Anna und Anna' | grep -c Anna
1
$ echo 'Anna und Anna' | grep -o Anna
Anna
Anna
$ echo 'Anna und Anna' | grep -o Anna | wc -l
2
```

Eine Zeile, zwei Treffer. Bei einem festen Suchtext sieht jeder Treffer gleich aus; `-o` dient dann vor allem zum Zählen.
::::

⁠**Kurz gesagt:** `grep -o` schreibt nur die passenden Stücke, eines je Zeile; mit `wc -l` zählt man so Treffer statt Zeilen.

### In vielen Dateien suchen: -r und -l

<span class="anker" id="stufe-5-4"></span>

Wo stand noch einmal der Lauf von Clara, in welcher Datei? Bei mehreren Dateien oder einem ganzen Verzeichnisbaum muss `grep` zusätzlich sagen, woher eine Zeile stammt. Abbildung [17](#abb-17) zeigt, wie es dabei vorgeht.

:::abbildung linux/k6grepr 17
Ein kleiner Verzeichnisbaum: das Übungsverzeichnis mit einigen Dateien und dem Unterverzeichnis `archiv` mit `november.csv`. `grep -r Clara` besucht jede Datei, auch die im Unterverzeichnis; jede Trefferzeile erscheint rechts mit dem Pfad der Datei und einem Doppelpunkt davor. Mit `-l` schrumpft die Ausgabe auf eine Zeile je Datei mit Treffer.
:::

:::definition Definition 5.4 (grep mit mehreren Dateien, -r, -l)
<span class="anker" id="satz-5-4"></span>

Bekommt `grep` mehr als eine Datei, setzt es vor jede ausgegebene Zeile den Dateinamen und einen Doppelpunkt. Mit `-r` durchsucht es alle Dateien in den genannten Verzeichnissen und deren Unterverzeichnissen. Mit `-l` schreibt es statt der Zeilen nur die Namen der Dateien, in denen es etwas gefunden hat, jeden einmal.
:::

::::beispiel Clara in mehreren Dateien
```console
$ grep Clara laeufe.csv neu.csv
laeufe.csv:2026-11-03,Clara,7.2,41
laeufe.csv:2026-11-07,Clara,8.0,44
neu.csv:2026-11-03,Clara,7.2,41
neu.csv:2026-11-07,Clara,8.0,44
neu.csv:2026-11-10,Clara,6.0,33
$ grep -c Clara laeufe.csv neu.csv
laeufe.csv:2
neu.csv:3
```

`-c` zählt bei mehreren Dateien für jede einzeln. Für `-r` legst du ein Unterverzeichnis mit einer Kopie an:

```console
$ mkdir archiv
$ cp laeufe.csv archiv/november.csv
$ grep -r Clara archiv
archiv/november.csv:2026-11-03,Clara,7.2,41
archiv/november.csv:2026-11-07,Clara,8.0,44
$ grep -rl Clara . | sort
./archiv/november.csv
./klein.csv
./kurz.csv
./laeufe.csv
./namen.txt
./neu.csv
```

`.` ist das Arbeitsverzeichnis; `-rl` nennt alle Dateien darunter, in denen Clara vorkommt, auch die Namensliste aus Unterabschnitt [2.3](spalten-ausschneiden-und-zeichen-ersetzen-cut-tr-und-paste.html#stufe-2-3). `grep -r` geht die Dateien in der Reihenfolge durch, in der sie im Verzeichnis stehen, ungeordnet wie `find` in [Kapitel 3, Abschnitt 10.1](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-finden-und-platz-messen.html#stufe-10-1); das `sort` dahinter macht die Liste übersichtlich. Hast du die Aufgaben im Übungsverzeichnis gelöst, nennt die Liste auch deren Dateien, etwa `probe.csv`.
::::

⁠**Kurz gesagt:** Bei mehreren Dateien nennt `grep` die Herkunft jeder Zeile; `-r` durchsucht ganze Verzeichnisbäume, `-l` nennt nur die Dateinamen.

### Aufgaben zu Abschnitt [5](#stufe-5)

<span class="anker" id="stufe-5-5"></span>

:::aufgabe Aufgabe 13 ★ grep im Lauftagebuch
<span class="anker" id="aufg-13"></span>

(a) Wie viele Läufe hatte Ben? (b) Gib alle Läufe aus, die nicht von Anna sind, ohne die Kopfzeile. (c) In welcher Zeile steht der Lauf vom 7. November?

:::loesung
```console
$ grep -c Ben laeufe.csv
3
$ grep -v Anna laeufe.csv | grep -v datum
2026-11-02,Ben,10.5,62
2026-11-03,Clara,7.2,41
2026-11-05,Ben,5.0,31
2026-11-07,Clara,8.0,44
2026-11-08,Ben,21.1,128
$ grep -n 2026-11-07 laeufe.csv
8:2026-11-07,Clara,8.0,44
```

(a) Drei Zeilen mit Ben. (b) `grep -v Anna` lässt auch die Kopfzeile durch; ein zweites `grep -v` mit einem Wort aus der Kopfzeile entfernt sie. Ebenso ginge `tail -n +2` davor. (c) Zeile 8, die Kopfzeile mitgezählt.
:::
:::

:::aufgabe Aufgabe 14 ★★ Zeilen oder Treffer?
<span class="anker" id="aufg-14"></span>

Sage voraus, welche der beiden Zahlen größer ist, `grep -c 0 laeufe.csv` oder die Zahl, die `grep -o 0 laeufe.csv | wc -l` liefert, und begründe es. Prüfe am Rechner und erkläre die beiden Werte.

:::loesung
```console
$ grep -c 0 laeufe.csv
9
$ grep -o 0 laeufe.csv | wc -l
25
```

`grep -c` zählt Zeilen, in denen mindestens eine 0 vorkommt; das sind alle neun Läufe, denn jedes Datum enthält eine, die Kopfzeile keine. `grep -o` schreibt jede einzelne 0 auf eine eigene Zeile. In jedem Datum stecken zwei, in `2026` und im Tag `0x`; dazu kommen die Nullen in `5.0` (dreimal), `10.5`, `12.0`, `70` und `8.0`. Zusammen $9 \cdot 2 + 3 + 1 + 2 + 1 = 25$. Die zweite Zahl ist mindestens so groß wie die erste, weil jede gezählte Zeile mindestens einen Treffer hat.
:::
:::

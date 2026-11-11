---
title: Reguläre Ausdrücke: Zeichen, Klassen und Anker
pfad: Informatik / Linux und Kommandozeile / Textwerkzeuge und reguläre Ausdrücke
adresse: informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke
knoten: Kapitel 6: Textwerkzeuge und reguläre Ausdrücke
order: 6110700
summary: Bisher hat grep nach festen Wörtern gesucht.
tags: Zeichenkette, regulärer Ausdruck, Treffer, Punkt, Klammerausdruck, Zeichenklasse, Anker
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Bisher hat `grep` nach festen Wörtern gesucht. Viele Fragen betreffen aber eine Form: ein Datum aus einer bestimmten Woche, eine Dauer unter 30 Minuten, eine Zahl mit Dezimalpunkt. Dieser Abschnitt führt die Schreibweise ein, mit der man solche Formen beschreibt, und ihre ersten Bausteine: ein beliebiges Zeichen, eine Auswahl von Zeichen und die Stellen am Anfang und am Ende einer Zeile.
:::

### Der reguläre Ausdruck

<span class="anker" id="stufe-6-1"></span>

Wie findet man alle Läufe, die länger als 99 Minuten dauerten? Einen festen Suchtext gibt es dafür nicht; `128` ist nur eine von 900 dreistelligen Zahlen. Gebraucht wird eine Beschreibung wie „ein Komma, dann drei Ziffern, dann das Zeilenende“, und ein Werkzeug, das jede Zeile mit dieser Beschreibung vergleicht. Eine __Zeichenkette__ ist dabei einfach eine Folge von Zeichen, etwa ein Wort, eine Zahl oder eine ganze Zeile.

:::definition Definition 6.1 (Regulärer Ausdruck, Treffer)
<span class="anker" id="satz-6-1"></span>

Ein __regulärer Ausdruck__ ist ein Text, der eine Menge von Zeichenketten beschreibt. Er besteht aus gewöhnlichen Zeichen, die für sich selbst stehen, und aus Sonderzeichen mit eigener Bedeutung. Eine Zeile passt zu einem regulären Ausdruck, wenn ein zusammenhängendes Stück von ihr zu dieser Menge gehört; dieses Stück heißt __Treffer__.
:::

Der Suchtext von `grep` ist immer ein regulärer Ausdruck gewesen; er bestand bisher nur aus gewöhnlichen Zeichen. Der englische Name „regular expression“ wird oft zu „Regex“ abgekürzt.

::::beispiel Ein Ausdruck ohne Sonderzeichen
Der Ausdruck `Clara` enthält nur gewöhnliche Zeichen. Er beschreibt eine Menge mit genau einer Zeichenkette, `Clara`. Die Zeile `2026-11-03,Clara,7.2,41` passt, denn ihr Stück von Stelle 12 bis 16 ist genau diese Zeichenkette; das ist der Treffer. Genau so hat `grep Clara laeufe.csv` in Unterabschnitt [5.1](suchen-mit-grep.html#stufe-5-1) gearbeitet.
::::

Viele Sonderzeichen regulärer Ausdrücke bedeuten auch der Shell etwas: `*`, `?`, `[`, `$`, `\`, `|`, Klammern. Die Shell soll den Ausdruck aber unverändert an das Programm weitergeben. Nach der Regel aus [Kapitel 5, Abschnitt 3.8](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/worttrennung-und-quoting.html#stufe-3-8) gehört Text, den ein Programm unverändert bekommen soll, in einfache Anführungszeichen. Ab jetzt steht deshalb jeder reguläre Ausdruck mit Sonderzeichen in diesem Kapitel zwischen `'` und `'`; bei einem einfachen Wort wie `Clara` ist das nicht nötig, schadet aber nicht.

⁠**Kurz gesagt:** Ein regulärer Ausdruck beschreibt eine Menge von Zeichenketten; eine Zeile passt, wenn ein Stück von ihr dazugehört, und auf der Befehlszeile steht er in einfachen Anführungszeichen.

### Der Punkt: ein beliebiges Zeichen

<span class="anker" id="stufe-6-2"></span>

Das einfachste Sonderzeichen lässt eine Stelle offen: „hier irgendein Zeichen“. Abbildung [18](#abb-18) zeigt, welche Menge dadurch entsteht und welche Zeilen passen.

:::abbildung linux/k6menge 18
Links der Ausdruck `5.0`, rechts die Menge, die er beschreibt: alle Zeichenketten aus drei Zeichen, die mit 5 beginnen und mit 0 enden, darunter `5.0`, `5x0`, `520` und `5,0`. Darunter vier Zeilen. Bei `5.0`, `5x0` und `520` leuchtet ein Stück auf, das zur Menge gehört; `50` hat kein solches Stück und bleibt grau.
:::

:::definition Definition 6.2 (Punkt)
<span class="anker" id="satz-6-2"></span>

Der __Punkt__ `.` in einem regulären Ausdruck passt auf genau ein beliebiges Zeichen.
:::

Der Punkt steht also immer für genau eine Stelle, nicht für keine und nicht für mehrere.

::::beispiel Der Punkt in einer Zahl
```console
$ printf '%s\n' 5.0 5x0 520 50 | grep '5.0'
5.0
5x0
520
```

Gemeint war vielleicht die Zahl 5,0, gefunden werden auch `5x0` und `520`: Der Punkt passt auf jedes Zeichen zwischen 5 und 0. `50` passt nicht, denn zwischen 5 und 0 fehlt ein Zeichen.
::::

⁠**Kurz gesagt:** Ein Punkt passt auf genau ein beliebiges Zeichen.

### Sonderzeichen wörtlich nehmen: der umgekehrte Schrägstrich und grep -F

<span class="anker" id="stufe-6-3"></span>

Im Lauftagebuch stehen Kommazahlen mit Punkt. Wer nach `5.0` sucht, will meist wirklich einen Punkt und nicht irgendein Zeichen. Es braucht also einen Weg, einem Sonderzeichen seine Bedeutung zu nehmen.

:::definition Definition 6.3 (Umgekehrter Schrägstrich im Ausdruck, grep -F)
<span class="anker" id="satz-6-3"></span>

Ein umgekehrter Schrägstrich `\` vor einem Sonderzeichen macht es in einem regulären Ausdruck zu einem gewöhnlichen Zeichen: `\.` passt nur auf einen Punkt. Mit der Option `-F` nimmt `grep` den ganzen Suchtext als feste Zeichenkette, in der kein Zeichen eine Sonderbedeutung hat.
:::

Zwischen einfachen Anführungszeichen lässt die Shell den umgekehrten Schrägstrich stehen ([Kapitel 5, Abschnitt 3.4](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/worttrennung-und-quoting.html#stufe-3-4)); er kommt also bei `grep` an.

::::beispiel Nur der echte Punkt
```console
$ printf '%s\n' 5.0 5x0 520 50 | grep '5\.0'
5.0
$ printf '%s\n' 5.0 5x0 520 50 | grep -F '5.0'
5.0
```

Beide Wege finden nur noch die Zeile mit dem Punkt.
::::

⁠**Kurz gesagt:** `\` vor einem Sonderzeichen macht es gewöhnlich; `grep -F` nimmt den ganzen Suchtext wörtlich.

:::hintergrund Warum ein vergessener Schrägstrich selten auffällt
Ein Punkt ohne Schrägstrich passt auch auf einen Punkt. Alle Zeilen, die man finden wollte, werden deshalb weiterhin gefunden, und der Fehler zeigt sich nur in zusätzlichen Treffern, die man leicht übersieht: Eine Suche nach `bericht.txt` findet auch `berichtXtxt`. Das ist eine Folge davon, dass ein Ausdruck eine Menge beschreibt: Ohne Schrägstrich ist die Menge größer, enthält aber die gemeinte Zeichenkette noch. Wer einen festen Text sucht, in dem Punkte oder andere Sonderzeichen vorkommen, etwa einen Dateinamen, nimmt deshalb am besten gleich `grep -F`.
:::

### Eine Auswahl von Zeichen: der Klammerausdruck

<span class="anker" id="stufe-6-4"></span>

Der Punkt lässt jedes Zeichen zu. Oft soll an einer Stelle aber nur eine bestimmte Auswahl stehen dürfen, etwa nur die Tage 2, 3 oder 4. Abbildung [19](#abb-19) zeigt, wie eine eckige Klammer eine solche Auswahl für eine einzige Stelle beschreibt.

:::abbildung linux/k6klammer 19
Der Ausdruck `2026-11-0[2-4]` über dem Datum `2026-11-03`. Alle Zeichen bis zur letzten Stelle müssen genau übereinstimmen; die letzte Stelle ist ein Kästchen mit den erlaubten Zeichen 2, 3 und 4. Die 3 passt hinein und leuchtet auf. Beim Datum `2026-11-07` passt die 7 nicht ins Kästchen.
:::

:::definition Definition 6.4 (Klammerausdruck)
<span class="anker" id="satz-6-4"></span>

Ein __Klammerausdruck__ ist eine Liste von Zeichen in eckigen Klammern; er passt auf genau ein Zeichen, das in der Liste steht. Zwei Zeichen mit einem Bindestrich dazwischen stehen für alle Zeichen von einem bis zum anderen, etwa `[0-9]` für eine Ziffer. Steht direkt nach der öffnenden Klammer ein `^`, passt er auf genau ein Zeichen, das nicht in der Liste steht.
:::

Innerhalb der Klammern sind Punkt, Stern, Dollarzeichen und der umgekehrte Schrägstrich gewöhnliche Zeichen; `[.]` passt nur auf einen Punkt. Ein Bindestrich gilt als gewöhnliches Zeichen, wenn er als erstes oder letztes in der Liste steht, eine schließende eckige Klammer, wenn sie als erstes steht: `[]-]` passt auf `]` oder `-`. Die Muster für Dateinamen aus [Kapitel 3, Abschnitt 6.6](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/kopieren-verschieben-loschen.html#stufe-6-6) kennen dieselben Klammern; verneint wird dort aber mit `!`, hier mit `^`.

::::beispiel Drei Tage, zwei Personen, kein Punkt
```console
$ grep '2026-11-0[2-4]' laeufe.csv
2026-11-02,Anna,5.0,28
2026-11-02,Ben,10.5,62
2026-11-03,Clara,7.2,41
2026-11-04,Anna,6.4,35
$ grep -c ',[AB]' laeufe.csv
7
$ printf '%s\n' 5.0 5x0 520 | grep '5[^.]0'
5x0
520
```

Die Läufe vom 2. bis 4. November; sieben Zeilen, in denen auf ein Komma ein A oder ein B folgt, also die Läufe von Anna und Ben; und alle Zeilen, in denen zwischen 5 und 0 etwas anderes als ein Punkt steht.
::::

⁠**Kurz gesagt:** `[…]` passt auf genau ein Zeichen aus der Liste, `[^…]` auf genau eines, das nicht darin steht; `a-z` in der Liste ist ein Bereich.

:::hintergrund Warum Bereiche mit Vorsicht zu genießen sind
Was „alle Zeichen von a bis z“ sind, hängt von der Ordnung der Zeichen ab, also von der Spracheinstellung aus Unterabschnitt [3.4](sortieren-und-zahlen-sort-und-uniq.html#stufe-3-4). In `C` und `C.UTF-8` ist die Ordnung die der Zeichennummern, und `[a-z]` meint genau die 26 Kleinbuchstaben ohne Umlaute. Der Standard für Unix-Shells und ihre Werkzeuge legt Bereiche nur für die Spracheinstellung `C` fest und lässt ihre Bedeutung in allen anderen offen. Auf älteren Systemen mit Wörterbuchordnung lagen Groß- und Kleinbuchstaben abwechselnd, a, A, b, B, und `[A-Z]` umfasste dann auch fast alle Kleinbuchstaben. Bei Ziffern ist ein Bereich unbedenklich; für Buchstaben gibt es eine sicherere Schreibweise mit Namen statt Bereichen.
:::

### Zeichenklassen: [[:digit:]] und ihre Verwandten

<span class="anker" id="stufe-6-5"></span>

„Irgendein Buchstabe“ ist mehr als a bis z: Es gibt Großbuchstaben, Umlaute und Buchstaben anderer Sprachen. Statt sie aufzuzählen, gibt man der Auswahl einen Namen. Abbildung [20](#abb-20) legt drei solche Namen an eine Zeile.

:::abbildung linux/k6klassen 20
Die Zeile `2026-11-03,Clara,7.2,41` Zeichen für Zeichen. Nacheinander leuchten die Zeichen auf, die zu `[[:digit:]]` gehören (alle Ziffern), zu `[[:alpha:]]` (die Buchstaben von `Clara`) und zu `[[:punct:]]` (Bindestriche, Kommas und der Punkt). Jedes Zeichen gehört zu genau einer der drei Klassen.
:::

:::definition Definition 6.5 (Zeichenklasse)
<span class="anker" id="satz-6-5"></span>

Eine __Zeichenklasse__ ist eine benannte Gruppe von Zeichen, die man innerhalb eines Klammerausdrucks als `[:name:]` schreibt. Wichtige Namen sind `digit` für Ziffern, `alpha` für Buchstaben, `upper` und `lower` für Groß- und Kleinbuchstaben, `alnum` für Buchstaben und Ziffern, `space` für Leerzeichen und verwandte Zeichen wie Tabulator, Zeilenende und Wagenrücklauf, `blank` nur für Leerzeichen und Tabulator und `punct` für Satzzeichen. Welche Zeichen zu einer Klasse gehören, legt die Spracheinstellung fest.
:::

Die inneren Klammern gehören zum Namen, die äußeren zum Klammerausdruck. Eine einzelne Ziffer schreibt man deshalb `[[:digit:]]` mit doppelten Klammern; in `[[:digit:].]` passt der Ausdruck auf eine Ziffer oder einen Punkt.

::::beispiel Zeilen mit und ohne Ziffern
```console
$ grep -c '[[:digit:]]' laeufe.csv
9
$ grep -v '[[:digit:]]' laeufe.csv
datum,name,km,minuten
```

Neun Zeilen enthalten eine Ziffer, die Kopfzeile keine.
::::

::::beispiel [Zweites Beispiel] Ist ä ein Buchstabe?
```console
$ echo 'ä' | grep -c '[[:alpha:]]'
1
$ echo 'ä' | LC_ALL=C grep -c '[[:alpha:]]'
0
```

Unter `C.UTF-8` sind die beiden Bytes des ä ein Zeichen und ein Buchstabe. Unter `C` ist jedes Byte ein eigenes Zeichen, und keines der beiden ist ein Buchstabe. Hier zeigt sich, dass die Spracheinstellung sogar festlegt, was ein Zeichen ist.
::::

⁠**Kurz gesagt:** `[[:digit:]]`, `[[:alpha:]]` und ihre Verwandten wählen Zeichen nach Art; was dazugehört, bestimmt die Spracheinstellung.

### Anfang und Ende der Zeile: die Anker

<span class="anker" id="stufe-6-6"></span>

`grep ',2[0-9]'` soll die Läufe unter 30 Minuten finden, also die mit einer Dauer zwischen 20 und 29. Das Stück `,2` und eine Ziffer kommt aber auch in `,21.1` vor, der Strecke von Bens Halbmarathon. Gemeint ist „am Ende der Zeile“. Abbildung [21](#abb-21) zeigt, wie ein Ausdruck eine Stelle in der Zeile verlangen kann.

:::abbildung linux/k6anker 21
Die Zeile `2026-11-08,Ben,21.1,128` als Folge von Zeichen. Zwischen den Zeichen liegen Stellen, als senkrechte Striche gezeichnet. Der Strich vor dem ersten Zeichen ist die Stelle von `^`, der nach dem letzten die von `$`. Der Ausdruck `,2[0-9]` findet einen Treffer bei `,21`; mit `$` dahinter müsste der Treffer direkt vor dem letzten Strich enden, und das tut er nicht.
:::

:::definition Definition 6.6 (Anker)
<span class="anker" id="satz-6-6"></span>

Ein __Anker__ passt nicht auf ein Zeichen, sondern auf eine Stelle in der Zeile. `^` am Anfang eines Ausdrucks passt auf die Stelle vor dem ersten Zeichen der Zeile, `$` am Ende eines Ausdrucks auf die Stelle nach dem letzten Zeichen, direkt vor dem Zeilenende.
:::

`^d` passt also nur auf Zeilen, die mit d beginnen, `,28$` nur auf Zeilen, die mit `,28` enden, und `^$` nur auf leere Zeilen. Das Wort kommt vom Bild eines Ankers, der den Ausdruck an einem Ende der Zeile festmacht.

::::beispiel Kopfzeile, kurze Läufe, leere Zeilen
```console
$ grep '^d' laeufe.csv
datum,name,km,minuten
$ grep ',2[0-9]' laeufe.csv
2026-11-02,Anna,5.0,28
2026-11-08,Ben,21.1,128
2026-11-09,Anna,5.0,27
$ grep ',2[0-9]$' laeufe.csv
2026-11-02,Anna,5.0,28
2026-11-09,Anna,5.0,27
$ grep -c '^$' laeufe.csv
0
```

Ohne `$` rutscht Bens Halbmarathon durch, mit `$` bleiben die beiden Läufe unter 30 Minuten. Leere Zeilen hat die Datei keine.
::::

::::beispiel [Zweites Beispiel] Der Anker und das Windows-Zeilenende
```console
$ grep -c ',28$' laeufe.csv windows.csv
laeufe.csv:1
windows.csv:0
```

Beide Dateien enthalten die Zeile mit `,28`. In `windows.csv` steht zwischen `28` und dem Zeilenende aber noch der Wagenrücklauf aus Unterabschnitt [1.4](textdaten-datensatze-felder-und-zeilenenden.html#stufe-1-4). Das letzte Zeichen der Zeile ist deshalb kein `8`, und `$` findet keinen passenden Treffer. Nach `tr -d '\r'` aus Unterabschnitt [2.2](spalten-ausschneiden-und-zeichen-ersetzen-cut-tr-und-paste.html#stufe-2-2) wäre er gefunden worden.
::::

⁠**Kurz gesagt:** `^` verankert einen Ausdruck am Zeilenanfang, `$` am Zeilenende; beide passen auf Stellen, nicht auf Zeichen.

### Aufgaben zu Abschnitt [6](#stufe-6)

<span class="anker" id="stufe-6-7"></span>

:::aufgabe Aufgabe 15 ★ Ein Zeitraum, eine Dauer
<span class="anker" id="aufg-15"></span>

(a) Gib alle Läufe vom 5. bis 9. November aus. (b) Gib alle Läufe aus, die zwischen 40 und 49 Minuten dauerten.

:::loesung
```console
$ grep '^2026-11-0[5-9]' laeufe.csv
2026-11-05,Ben,5.0,31
2026-11-06,Anna,12.0,70
2026-11-07,Clara,8.0,44
2026-11-08,Ben,21.1,128
2026-11-09,Anna,5.0,27
$ grep ',4[0-9]$' laeufe.csv
2026-11-03,Clara,7.2,41
2026-11-07,Clara,8.0,44
```

(a) Der Klammerausdruck `[5-9]` lässt für die letzte Stelle des Tags die Ziffern 5 bis 9 zu; der Anker sorgt dafür, dass das Datum am Zeilenanfang steht. (b) Ein Komma, eine 4, irgendeine Ziffer und dann das Zeilenende: die Dauer im letzten Feld liegt zwischen 40 und 49. Ohne `$` passte auch eine Strecke wie `,42.0`, wenn es sie gäbe.
:::
:::

:::aufgabe Aufgabe 16 ★★ Der Punkt
<span class="anker" id="aufg-16"></span>

Du suchst Läufe über genau 1.0 km. (a) Sage voraus, was `grep -c '1.0' laeufe.csv` meldet, und erkläre das Ergebnis. (b) Schreibe zwei Befehle, die richtig suchen, einen mit regulärem Ausdruck und einen mit `-F`.

:::loesung
```console
$ grep -c '1.0' laeufe.csv
9
$ grep '1.0' laeufe.csv | head -n 1
2026-11-02,Anna,5.0,28
$ grep -c ',1\.0,' laeufe.csv
0
$ grep -cF ',1.0,' laeufe.csv
0
```

(a) Alle neun Läufe passen, obwohl keiner 1.0 km lang war. Der Punkt passt auf jedes Zeichen, und im Datum steht `11-0`: eine 1, ein Bindestrich, eine 0. (b) Mit `\.` meint der Ausdruck nur den Punkt, mit `-F` ist der ganze Suchtext wörtlich. Die Kommas davor und dahinter sorgen dafür, dass genau das Feld gemeint ist; ohne sie passte etwa auch eine Strecke wie `11.0`. Ergebnis in beiden Fällen: kein Lauf über genau 1.0 km.
:::
:::

:::aufgabe Aufgabe 17 ★★ Anker und Windows-Datei
<span class="anker" id="aufg-17"></span>

(a) Zähle mit `grep -c ',62$'` die Treffer in `laeufe.csv` und in `windows.csv` mit einem einzigen Befehl. (b) Erkläre den Unterschied. (c) Zähle richtig in `windows.csv`, ohne eine neue Datei anzulegen.

:::loesung
```console
$ grep -c ',62$' laeufe.csv windows.csv
laeufe.csv:1
windows.csv:0
$ tr -d '\r' < windows.csv | grep -c ',62$'
1
```

(a) Mit zwei Dateien zählt `grep -c` für jede einzeln. (b) In `windows.csv` steht zwischen `62` und dem Zeilenende der Wagenrücklauf; das letzte Zeichen der Zeile ist kein `2`, und `$` passt erst hinter dem Wagenrücklauf. (c) `tr` entfernt die Wagenrückläufe im Strom, und `grep` bekommt ohne Dateinamen die bereinigten Zeilen über die Pipe; eine neue Datei entsteht nicht.
:::
:::

---
title: Sortieren und Zählen: sort und uniq
pfad: Informatik / Linux und Kommandozeile / Textwerkzeuge und reguläre Ausdrücke
adresse: informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke
knoten: Kapitel 6: Textwerkzeuge und reguläre Ausdrücke
order: 6110400
summary: Wer ist am häufigsten gelaufen, welcher Lauf war der längste?
tags: sort, Sortierschlüssel, Spracheinstellung, uniq
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Wer ist am häufigsten gelaufen, welcher Lauf war der längste? Für solche Fragen ordnet man die Zeilen und zählt gleiche. Dieser Abschnitt zeigt, wie `sort` Zeilen vergleicht, wie es Zahlen und einzelne Spalten sortiert, warum die Reihenfolge von der Spracheinstellung abhängt und wie man mit `uniq` gleiche Zeilen zählt.
:::

### Wie sort vergleicht: die Zeichenordnung

<span class="anker" id="stufe-3-1"></span>

`sort` hat in [Kapitel 4, Abschnitt 4.2](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/pipes-und-filter.html#stufe-4-2) die Zeilen einer Liste geordnet. Bei Wörtern sieht das Ergebnis aus wie im Wörterbuch, bei Zahlen manchmal nicht. Um das vorherzusagen, muss man wissen, wie `sort` zwei Zeilen vergleicht.

:::definition Definition 3.1 (sort)
<span class="anker" id="satz-3-1"></span>

Der Befehl __sort__ liest alle Zeilen seiner Eingabe und schreibt sie geordnet aus. Zwei Zeilen vergleicht er Zeichen für Zeichen von links; das erste Zeichen, in dem sie sich unterscheiden, entscheidet nach der Ordnung der Zeichen. Ist eine Zeile der Anfang der anderen, kommt die kürzere zuerst. Mit `-r` kehrt `sort` die Reihenfolge um.
:::

Unter der Spracheinstellung des Testsystems, die [Kapitel 5, Abschnitt 1.3](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/expansion-muster-klammern-und-tilde.html#stufe-1-3) bei der Reihenfolge der Dateinamen erwähnt hat, ist die Ordnung der Zeichen die Reihenfolge ihrer Nummern. Darin stehen unter anderem die Ziffern vor den Großbuchstaben, diese vor den Kleinbuchstaben und die Umlaute dahinter. So vergleicht auch Python Zeichenketten ([Python, Kapitel 3, Abschnitt 1.3](/wissen/informatik/programmieren/python/entscheidungen-und-schleifen/bedingungen-vergleiche-und-logische-operatoren.html#stufe-1-3)).

::::beispiel Zahlen als Text, Datum vor Kopfzeile
```console
$ printf '%s\n' 10 9 100 | sort
10
100
9
$ sort laeufe.csv
2026-11-02,Anna,5.0,28
2026-11-02,Ben,10.5,62
2026-11-03,Clara,7.2,41
2026-11-04,Anna,6.4,35
2026-11-05,Ben,5.0,31
2026-11-06,Anna,12.0,70
2026-11-07,Clara,8.0,44
2026-11-08,Ben,21.1,128
2026-11-09,Anna,5.0,27
datum,name,km,minuten
```

`10` und `100` beginnen mit `1`, `9` mit `9`; die 1 kommt vor der 9, also stehen beide vor der 9. `10` ist der Anfang von `100` und kommt zuerst. Im Lauftagebuch beginnt jeder Datensatz mit einer Ziffer, die Kopfzeile mit dem Buchstaben `d`; Ziffern kommen vor Buchstaben, deshalb landet die Kopfzeile am Ende. Die Läufe selbst stehen in der Reihenfolge des Datums, denn ein Datum der Form Jahr-Monat-Tag ordnet sich Zeichen für Zeichen richtig.
::::

```console
$ printf '%s\n' 10 9 100 | sort -r
9
100
10
```

`-r` dreht dieselbe Ordnung einfach um.

⁠**Kurz gesagt:** `sort` vergleicht Zeilen Zeichen für Zeichen von links nach der Ordnung der Zeichen; deshalb steht `10` vor `9`.

### Numerisch sortieren: sort -n

<span class="anker" id="stufe-3-2"></span>

Für Strecken und Minuten ist die Zeichenordnung falsch: Ein Lauf über 10,5 km ist länger als einer über 5 km, auch wenn `1` vor `5` kommt. Abbildung [9](#abb-9) stellt die beiden Arten zu vergleichen nebeneinander.

:::abbildung linux/k6lexnum 9
Oben vergleicht `sort` die Texte `10.5` und `5.0` Zeichen für Zeichen: Schon das erste Zeichen entscheidet, `1` ist kleiner als `5`, also kommt `10.5` zuerst. Unten liest `sort -n` am Anfang jeder Zeile eine Zahl und vergleicht die Werte: 5,0 ist kleiner als 10,5, also kommt `5.0` zuerst.
:::

:::definition Definition 3.2 (sort -n)
<span class="anker" id="satz-3-2"></span>

Mit der Option `-n` liest `sort` am Anfang jeder Zeile eine Zahl, mit einem möglichen Minuszeichen und einem möglichen Dezimalpunkt, und vergleicht die Zeilen nach dem Wert dieser Zahl. Eine Zeile, die nicht mit einer Zahl beginnt, zählt wie die Zahl 0. Bei gleichem Wert entscheidet die Zeichenordnung der ganzen Zeile.
:::

::::beispiel Zahlen nach ihrem Wert
```console
$ printf '%s\n' 10 9 100 | sort -n
9
10
100
$ printf '%s\n' 2.5 -3 10 abc | sort -n
-3
abc
2.5
10
```

`abc` hat keine Zahl am Anfang, zählt als 0 und landet zwischen $-3$ und $2{,}5$. Bei der Spalte der Strecken zeigt sich der Unterschied besonders deutlich; `paste -s -d' '` legt das Ergebnis platzsparend in eine Zeile:

```console
$ cut -d, -f3 laeufe.csv | sort | paste -s -d' '
10.5 12.0 21.1 5.0 5.0 5.0 6.4 7.2 8.0 km
$ cut -d, -f3 laeufe.csv | sort -n | paste -s -d' '
km 5.0 5.0 5.0 6.4 7.2 8.0 10.5 12.0 21.1
```

Ohne `-n` stehen die zweistelligen Strecken vorn und `km` aus der Kopfzeile hinten, mit `-n` ist es umgekehrt: `km` zählt als 0, die Strecken stehen nach ihrem Wert.
::::

⁠**Kurz gesagt:** `sort -n` vergleicht die Zahl am Zeilenanfang nach ihrem Wert; Zeilen ohne Zahl zählen als 0.

### Nach einer Spalte sortieren: -t und -k

<span class="anker" id="stufe-3-3"></span>

Im Lauftagebuch steht die Strecke nicht am Anfang, sondern in Feld 3. Mit `cut` könnte man sie herausschneiden, dann wären aber Datum und Name verloren. Gesucht ist eine Sortierung der ganzen Datensätze nach einem einzigen Feld. Abbildung [10](#abb-10) zeigt die Idee.

:::abbildung linux/k6schluessel 10
Die Datensätze des Lauftagebuchs untereinander; in jeder Zeile ist Feld 3, die Strecke, farbig hinterlegt: der Schlüssel. `sort -t, -k3,3n` vergleicht nur diese hinterlegten Stücke als Zahlen. Die ganzen Zeilen wandern an ihre neuen Plätze, bis die Strecken von oben nach unten wachsen; bei den drei Läufen über 5.0 km entscheidet die ganze Zeile.
:::

:::definition Definition 3.3 (Sortierschlüssel)
<span class="anker" id="satz-3-3"></span>

`-t` und ein Zeichen legen das Trennzeichen fest, an dem `sort` die Zeilen in Felder zerlegt. `-k A,B` macht die Felder von Nummer $A$ bis Nummer $B$ zum __Sortierschlüssel__: `sort` vergleicht nur dieses Stück der Zeile. Buchstaben wie `n` oder `r` direkt hinter der Angabe, etwa `-k3,3n`, gelten nur für diesen Schlüssel. Fehlt `,B`, reicht der Schlüssel bis zum Ende der Zeile. Mehrere `-k` werden der Reihe nach verglichen; sind alle Schlüssel gleich, entscheidet die ganze Zeile.
:::

`-k3,3` heißt also „von Feld 3 bis Feld 3“, nur dieses eine Feld. Ohne `-t` beginnt ein neues Feld dort, wo auf ein anderes Zeichen Leerzeichen oder Tabulatoren folgen; diese Leerzeichen zählen dabei zum neuen Feld.

::::beispiel Nach Strecke, kurz und lang
```console
$ sort -t, -k3,3n laeufe.csv
datum,name,km,minuten
2026-11-02,Anna,5.0,28
2026-11-05,Ben,5.0,31
2026-11-09,Anna,5.0,27
2026-11-04,Anna,6.4,35
2026-11-03,Clara,7.2,41
2026-11-07,Clara,8.0,44
2026-11-02,Ben,10.5,62
2026-11-06,Anna,12.0,70
2026-11-08,Ben,21.1,128
```

Die Kopfzeile hat in Feld 3 den Text `km`, zählt als 0 und steht vorn. Die drei Läufe über 5.0 km haben denselben Schlüssel; zwischen ihnen entscheidet die ganze Zeile, also das Datum. Absteigend und auf drei Zeilen gekürzt ergibt sich die Bestenliste:

```console
$ sort -t, -k3,3nr laeufe.csv | head -n 3
2026-11-08,Ben,21.1,128
2026-11-06,Anna,12.0,70
2026-11-02,Ben,10.5,62
```

Der längste Lauf war Bens Halbmarathon über 21,1 km.
::::

::::beispiel Zwei Schlüssel
Nach Namen geordnet und bei jedem Namen die längsten Läufe zuerst; `tail -n +2` nimmt vorher die Kopfzeile heraus:

```console
$ tail -n +2 laeufe.csv | sort -t, -k2,2 -k3,3nr
2026-11-06,Anna,12.0,70
2026-11-04,Anna,6.4,35
2026-11-02,Anna,5.0,28
2026-11-09,Anna,5.0,27
2026-11-08,Ben,21.1,128
2026-11-02,Ben,10.5,62
2026-11-05,Ben,5.0,31
2026-11-07,Clara,8.0,44
2026-11-03,Clara,7.2,41
```

Der erste Schlüssel ordnet nach Namen, der zweite nur innerhalb gleicher Namen nach der Strecke, absteigend.
::::

⁠**Kurz gesagt:** `sort -t, -k3,3n` sortiert ganze Zeilen nach dem Wert von Feld 3; weitere `-k` entscheiden bei Gleichstand.

:::hintergrund Warum -k2 und -k2,2 verschieden sortieren
Ohne Ende reicht ein Schlüssel bis zum Ende der Zeile. Das fällt erst auf, wenn die Werte des Felds gleich sind:

```console
$ tail -n +2 laeufe.csv | sort -t, -k2 | head -n 2
2026-11-06,Anna,12.0,70
2026-11-09,Anna,5.0,27
$ tail -n +2 laeufe.csv | sort -t, -k2,2 | head -n 2
2026-11-02,Anna,5.0,28
2026-11-04,Anna,6.4,35
```

Mit `-k2` vergleicht `sort` Stücke wie `Anna,12.0,70` und `Anna,5.0,27`; nach `Anna,` entscheidet die `1` gegen die `5`, ein Textvergleich der Strecke. Mit `-k2,2` sind alle vier Schlüssel `Anna` gleich, und die ganze Zeile, also das Datum, entscheidet. Bei Zahlen ist das besonders tückisch: `-k2n` statt `-k2,2n` macht alles ab Feld 2 bis zum Zeilenende zum Schlüssel für den Zahlenvergleich, und das Handbuch der GNU-Fassung warnt ausdrücklich, dass das selten tut, was man erwartet. Wer ein einzelnes Feld meint, schreibt `-k2,2`. Die Option `--debug` unterstreicht in jeder Zeile das Stück, das `sort` als Schlüssel benutzt.
:::

### Die Spracheinstellung

<span class="anker" id="stufe-3-4"></span>

Dieselbe Datei kann auf zwei Rechnern verschieden sortiert herauskommen. Das liegt nicht an `sort`, sondern an der Spracheinstellung, die bisher nur nebenbei vorkam. Sie legt fest, nach welchen Regeln einer Sprache Text behandelt wird.

:::definition Definition 3.4 (Spracheinstellung)
<span class="anker" id="satz-3-4"></span>

Die __Spracheinstellung__, englisch „locale“, ist ein Satz von Regeln für eine Sprache und ein Land. Sie legt unter anderem fest, welche Bytes zusammen ein Zeichen bilden, welche Zeichen Buchstaben sind, in welcher Reihenfolge Zeichen sortiert werden und welches Zeichen das Dezimalzeichen ist. Ein Programm erfährt sie aus Umgebungsvariablen, vor allem aus `LANG` und `LC_ALL`; ist `LC_ALL` gesetzt, hat es Vorrang.
:::

Eine Spracheinstellung hat einen Namen wie `de_DE.UTF-8` für Deutsch in Deutschland mit UTF-8. Zwei besondere heißen `C` und `C.UTF-8`: Sie sortieren nach den Nummern der Zeichen und sind überall gleich. Benutzen kann man nur Spracheinstellungen, die auf dem System eingerichtet sind; `locale -a` zeigt sie.

::::beispiel Die Spracheinstellung des Testsystems
```console
$ echo $LANG
C.UTF-8
$ locale -a
C
C.utf8
POSIX
```

WSL startet Ubuntu mit `C.UTF-8`, und mehr ist auf dem Testsystem nicht eingerichtet; `POSIX` ist ein zweiter Name für `C`. Mit dieser Einstellung sortiert `sort` Großbuchstaben vor Kleinbuchstaben und den Umlaut ans Ende. `-f` behandelt Klein- wie Großbuchstaben; `LC_ALL=C` vor dem Befehl erzwingt die Einstellung `C` für diesen einen Aufruf:

```console
$ printf '%s\n' b ä B a A Z | sort | paste -s -d' '
A B Z a b ä
$ printf '%s\n' b ä B a A Z | sort -f | paste -s -d' '
A a B b Z ä
$ printf '%s\n' b ä B a A Z | LC_ALL=C sort | paste -s -d' '
A B Z a b ä
```

`C` und `C.UTF-8` ordnen beide nach den Nummern der Zeichen; deshalb sind die erste und die letzte Zeile gleich.
::::

Auf einem Rechner mit deutscher Oberfläche ist meist `de_DE.UTF-8` eingestellt. Laut der Dokumentation der GNU-Werkzeuge sortiert `sort` dort wie ein Wörterbuch, Groß- und Kleinschreibung und Umlaute zählen erst bei sonst gleichen Buchstaben, und die Liste käme als a, A, ä, b, B, Z heraus; hier ist das nicht nachgeprüft, weil diese Spracheinstellung auf dem Testsystem fehlt.

⁠**Kurz gesagt:** Die Spracheinstellung bestimmt, wie `sort` ordnet; `C` und `C.UTF-8` ordnen nach Zeichennummern, `LC_ALL=C sort` macht ein Ergebnis auf jedem Rechner gleich.

:::hintergrund Das Dezimalzeichen und sort -n
Die Spracheinstellung legt auch fest, welches Zeichen `sort -n` als Dezimalzeichen liest; so beschreibt es das Handbuch der GNU-Fassung. Unter `de_DE.UTF-8` ist das ein Komma, und der Punkt trennt dort Tausender ab wie in `1.050`. Eine Strecke wie `10.5` liest die GNU-Fassung von `sort -n` dann als 105; auf dem Testsystem lässt sich das mangels dieser Spracheinstellung nicht zeigen. Wer Dateien mit Dezimalpunkt sortiert, schreibt deshalb `LC_ALL=C sort -n`. Dasselbe empfiehlt sich in allem, was auf verschiedenen Rechnern dasselbe Ergebnis liefern soll. Die Option `--debug` nennt die Regeln, nach denen `sort` gerade vergleicht:

```console
$ printf '%s\n' b a | sort --debug
sort: text ordering performed using simple byte comparison
a
_
b
_
$ printf '%s\n' b a | gnusort --debug
gnusort: text ordering performed using ‘C.UTF-8’ sorting rules
a
_
b
_
```

Stand der uutils-Fassung in Ubuntu 26.04: Sie meldet unter `C.UTF-8` einen einfachen Vergleich der Bytes, die GNU-Fassung die Regeln von `C.UTF-8`. Beides ergibt dieselbe Ordnung, denn in UTF-8 folgen die Bytes der Zeichen derselben Reihenfolge wie ihre Nummern. Die Striche unter jeder Zeile sind die Unterstreichung des Schlüssels, hier die ganze Zeile.
:::

### Gleiche Nachbarzeilen: uniq

<span class="anker" id="stufe-3-5"></span>

[Kapitel 4, Abschnitte 4.2](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/pipes-und-filter.html#stufe-4-2) und [4.3](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/pipes-und-filter.html#stufe-4-3) haben gezeigt, dass `uniq` nur dann Wiederholungen streicht, wenn `sort` gleiche Zeilen vorher zusammengebracht hat. Mit einer Option wird aus dem Streichen ein Zählen. Abbildung [11](#abb-11) zeigt, wie `uniq` arbeitet und warum es auf Nachbarn angewiesen ist.

:::abbildung linux/k6uniq 11
`uniq -c` liest einen Strom von Namen, Zeile für Zeile von oben. Neben dem Strom steht ein einziger Merkzettel mit der vorigen Zeile und einem Zähler. Ist die neue Zeile gleich, wächst der Zähler; ist sie anders, schreibt `uniq` Zähler und Merkzettel aus und beginnt neu. Bei der ungeordneten Folge Anna, Ben, Clara, Anna kommt so jede Zeile mit 1 heraus, bei der geordneten Folge Anna, Anna, Anna, Anna, Ben … entstehen 4, 3 und 2.
:::

:::definition Definition 3.5 (uniq)
<span class="anker" id="satz-3-5"></span>

Der Befehl __uniq__ vergleicht jede Zeile seiner Eingabe mit der Zeile direkt davor und schreibt von mehreren gleichen Zeilen hintereinander nur eine aus. Mit `-c` setzt er vor jede ausgegebene Zeile, wie oft sie hintereinander vorkam. `-d` gibt nur Zeilen aus, die mehrfach hintereinander vorkamen, `-u` nur die, die einzeln standen.
:::

::::beispiel Zählen mit und ohne sort
```console
$ cut -d, -f2 laeufe.csv | uniq -c
      1 name
      1 Anna
      1 Ben
      1 Clara
      1 Anna
      1 Ben
      1 Anna
      1 Clara
      1 Ben
      1 Anna
$ cut -d, -f2 laeufe.csv | sort | uniq -c
      4 Anna
      3 Ben
      2 Clara
      1 name
```

Im Lauftagebuch stehen nirgends zwei gleiche Namen untereinander, also zählt `uniq` jede Zeile einzeln. Nach `sort` stehen die gleichen Namen beisammen, und die Zähler stimmen: Anna lief viermal, Ben dreimal, Clara zweimal.
::::

::::beispiel [Zweites Beispiel] Doppelte und einzelne Strecken
```console
$ cut -d, -f3 laeufe.csv | sort | uniq -d
5.0
$ cut -d, -f3 laeufe.csv | sort | uniq -u | paste -s -d' '
10.5 12.0 21.1 6.4 7.2 8.0 km
```

Nur die Strecke 5.0 kommt mehrfach vor. Alle übrigen Werte stehen einzeln da, auch `km` aus der Kopfzeile.
::::

⁠**Kurz gesagt:** `uniq` fasst gleiche Zeilen zusammen, die direkt untereinander stehen; `-c` zählt sie, `-d` und `-u` wählen mehrfache oder einzelne.

:::hintergrund Warum uniq nur Nachbarn vergleicht
`uniq` liest seinen Strom genau einmal von vorn nach hinten und merkt sich dabei nur eine Zeile, die vorige. Mehr braucht es nicht, um gleiche Nachbarn zu erkennen, und deshalb hängt sein Speicherbedarf nur von der Länge einer Zeile ab, nicht von der Zahl der Zeilen. Es kann jede Zeile ausgeben, sobald die nächste anders ist, und arbeitet sogar hinter `tail -f` mit einem Strom, der nie endet. Gleiche Zeilen an beliebigen Stellen zu finden, hieße dagegen, sich alle bisherigen Zeilen zu merken. Diese Arbeit überlässt man `sort`, das ohnehin alles lesen muss: Die kleinste Zeile kann ja ganz am Ende stehen, also kann `sort` keine Zeile ausgeben, bevor es die letzte gesehen hat. Für große Eingaben sortiert die GNU-Fassung Stücke im Speicher, legt sie in vorübergehenden Dateien ab und fügt sie danach zusammen. Weder der Standard für Unix-Shells und ihre Werkzeuge noch die Handbücher begründen die Beschränkung auf Nachbarn ausdrücklich; die Begründung oben ist eine eigene Herleitung aus dem, wie die beiden Werkzeuge arbeiten.
:::

### Häufigkeiten zählen: sort, uniq -c, sort -rn

<span class="anker" id="stufe-3-6"></span>

Die Frage „Was kommt wie oft vor, und was am häufigsten?“ stellt sich so oft, dass sich für sie eine feste Folge von Werkzeugen eingebürgert hat. Abbildung [12](#abb-12) zeigt, was die drei Schritte mit der Spalte der Strecken machen.

:::abbildung linux/k6haeufigkeit 12
Die neun Strecken des Lauftagebuchs ungeordnet. `sort` ordnet sie und schiebt die drei Werte `5.0` zu einem Block zusammen; die übrigen sechs Werte stehen einzeln. `uniq -c` macht aus jedem Block eine Zeile mit seiner Länge davor: einmal `3 5.0`, sechsmal eine 1. `sort -rn` ordnet diese Zeilen nach der Zahl, und `3 5.0` rückt aus der Mitte an die Spitze.
:::

:::satz Satz 3.6 (Häufigkeitstabelle)
<span class="anker" id="satz-3-6"></span>

Die Pipeline `sort | uniq -c | sort -rn` macht aus einer Liste von Werten, einer je Zeile, eine Tabelle der verschiedenen Werte mit ihrer Häufigkeit, den häufigsten zuerst. Das erste `sort` bringt gleiche Werte zusammen, `uniq -c` zählt sie, `sort -rn` ordnet nach der Anzahl absteigend.
:::

Das zweite `sort` braucht `-n`, weil die Zeilen jetzt mit einer Zahl beginnen; `uniq -c` rückt sie nach rechts ein, und führende Leerzeichen überliest `sort -n`.

::::beispiel Wer läuft am häufigsten?
```console
$ tail -n +2 laeufe.csv | cut -d, -f2 | sort | uniq -c | sort -rn
      4 Anna
      3 Ben
      2 Clara
```

Erst die Kopfzeile weg, dann die Namen ausschneiden, dann die Häufigkeitstabelle. Mit Feld 3 statt Feld 2 und `head -n 1` am Ende fragt dieselbe Pipeline nach der häufigsten Strecke:

```console
$ tail -n +2 laeufe.csv | cut -d, -f3 | sort | uniq -c | sort -rn | head -n 1
      3 5.0
```
::::

Wer nur die verschiedenen Werte ohne Anzahl braucht, kann `sort | uniq` kürzer schreiben: `sort -u` schreibt von gleichen Zeilen nur eine aus.

```console
$ tail -n +2 laeufe.csv | cut -d, -f2 | sort -u
Anna
Ben
Clara
```

⁠**Kurz gesagt:** `sort | uniq -c | sort -rn` zählt, wie oft jeder Wert vorkommt, und stellt den häufigsten nach oben; `sort -u` liefert nur die verschiedenen Werte.

### Aufgaben zu Abschnitt [3](#stufe-3)

<span class="anker" id="stufe-3-7"></span>

:::aufgabe Aufgabe 7 ★ Zahlen sortieren
<span class="anker" id="aufg-7"></span>

(a) Sage voraus, in welcher Reihenfolge `sort` und `sort -n` die Zeilen `8`, `75`, `120` und `7.5` ausgeben, und prüfe es. (b) Gib den längsten Lauf aus. (c) Gib den kürzesten Lauf aus, ohne dass die Kopfzeile dazwischenkommt. Warum ist es gerade dieser der drei Läufe über 5.0 km?

:::loesung
```console
$ printf '%s\n' 8 75 120 7.5 | sort | paste -s -d' '
120 7.5 75 8
$ printf '%s\n' 8 75 120 7.5 | sort -n | paste -s -d' '
7.5 8 75 120
$ sort -t, -k3,3nr laeufe.csv | head -n 1
2026-11-08,Ben,21.1,128
$ tail -n +2 laeufe.csv | sort -t, -k3,3n | head -n 1
2026-11-02,Anna,5.0,28
```

(a) Ohne `-n` vergleicht `sort` Zeichen für Zeichen: `120` beginnt mit der kleinsten Ziffer und steht vorn, `8` mit der größten und steht hinten. `7.5` und `75` beginnen beide mit 7; an der zweiten Stelle entscheidet der Punkt, der in der Ordnung der Zeichen vor den Ziffern steht. Mit `-n` zählt der Wert. (b) Feld 3 nach Wert absteigend, die erste Zeile ist der Halbmarathon. (c) Aufsteigend kämen die Kopfzeile, deren `km` als 0 zählt, und dann die drei Läufe über 5.0 km. Ohne Kopfzeile bleiben diese drei vorn; ihr Schlüssel ist gleich, und die ganze Zeile entscheidet. `2026-11-02,Anna` ist in der Zeichenordnung kleiner als `2026-11-05,Ben` und `2026-11-09,Anna`, also kommt der Lauf vom 2. November zuerst.
:::
:::

:::aufgabe Aufgabe 8 ★★ Wie oft?
<span class="anker" id="aufg-8"></span>

(a) Wie oft kommt jede Strecke vor? (b) Wie viele verschiedene Personen sind gelaufen? (c) An wie vielen verschiedenen Tagen wurde gelaufen? Antworte jeweils mit einer Pipeline.

:::loesung
```console
$ tail -n +2 laeufe.csv | cut -d, -f3 | sort | uniq -c | sort -rn
      3 5.0
      1 8.0
      1 7.2
      1 6.4
      1 21.1
      1 12.0
      1 10.5
$ tail -n +2 laeufe.csv | cut -d, -f2 | sort -u | wc -l
3
$ tail -n +2 laeufe.csv | cut -d, -f1 | sort -u | wc -l
8
```

(a) Die Häufigkeitstabelle aus Unterabschnitt [3.6](#stufe-3-6) über Feld 3: 5.0 km dreimal, jede andere Strecke einmal. Die Einsen stehen in umgekehrter Zeichenordnung, denn bei gleicher Zahl entscheidet die ganze Zeile, und `-r` kehrt auch diesen Vergleich um. (b) `sort -u` lässt jeden Namen einmal übrig, `wc -l` zählt sie: drei Personen. (c) Dasselbe mit dem Datum: neun Läufe an acht Tagen, weil am 2. November zwei Personen liefen.
:::
:::

:::aufgabe Aufgabe 9 ★★ Nachbarn
<span class="anker" id="aufg-9"></span>

(a) Sage voraus, was `printf '%s\n' Anna Anna Ben Anna | uniq -c` ausgibt. (b) `tail -n +2 laeufe.csv | cut -d, -f1 | uniq -c` zählt die Läufe je Tag richtig, obwohl kein `sort` davorsteht. Warum?

:::loesung
```console
$ printf '%s\n' Anna Anna Ben Anna | uniq -c
      2 Anna
      1 Ben
      1 Anna
$ tail -n +2 laeufe.csv | cut -d, -f1 | uniq -c | head -n 3
      2 2026-11-02
      1 2026-11-03
      1 2026-11-04
```

(a) Die ersten beiden Zeilen sind gleiche Nachbarn und werden zu `2 Anna`. Dann kommt Ben, dann wieder Anna; diese Anna hat einen anderen Vorgänger und wird neu gezählt. (b) Das Lauftagebuch ist nach dem Datum geordnet, gleiche Tage stehen also schon nebeneinander. `uniq` braucht kein `sort`, wenn die Eingabe die gleichen Werte bereits zusammen enthält; `sort` sorgt nur dafür, dass das sicher so ist.
:::
:::

:::aufgabe Aufgabe 10 ★★★ Zwei Schlüssel
<span class="anker" id="aufg-10"></span>

(a) Sortiere die Läufe ohne Kopfzeile nach dem Namen und bei gleichem Namen nach der Dauer, die längste zuerst. (b) Im Beispiel „Zwei Schlüssel“ in Unterabschnitt [3.3](#stufe-3-3) stehen Annas zwei Läufe über 5.0 km in der Reihenfolge 28 vor 27 Minuten. Welche Regel legt das fest?

:::loesung
```console
$ tail -n +2 laeufe.csv | sort -t, -k2,2 -k4,4nr
2026-11-06,Anna,12.0,70
2026-11-04,Anna,6.4,35
2026-11-02,Anna,5.0,28
2026-11-09,Anna,5.0,27
2026-11-08,Ben,21.1,128
2026-11-02,Ben,10.5,62
2026-11-05,Ben,5.0,31
2026-11-07,Clara,8.0,44
2026-11-03,Clara,7.2,41
```

(a) Erster Schlüssel ist Feld 2 allein, zweiter Feld 4 als Zahl und absteigend. (b) Mit `-k2,2 -k3,3nr` sind bei Annas Läufen über 5.0 km beide Schlüssel gleich: derselbe Name, dieselbe Strecke. Dann vergleicht `sort` als letztes Mittel die ganzen Zeilen, und zwar aufsteigend, denn das `r` gehört nur zum zweiten Schlüssel. `2026-11-02` ist kleiner als `2026-11-09`, also steht der Lauf mit 28 Minuten vorn. In Teil (a) stehen die beiden ebenfalls so, dort aber aus einem anderen Grund: Der zweite Schlüssel ist die Dauer, und 28 ist größer als 27.
:::
:::

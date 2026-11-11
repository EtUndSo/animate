---
title: Reguläre Ausdrücke: Wiederholungen, Gruppen und Alternativen
pfad: Informatik / Linux und Kommandozeile / Textwerkzeuge und reguläre Ausdrücke
adresse: informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke
knoten: Kapitel 6: Textwerkzeuge und reguläre Ausdrücke
order: 6110800
summary: Ein Zeichen, eine Auswahl, eine Stelle: Damit lassen sich Ausdrücke fester Länge schreiben.
tags: Stern, Grundform, erweiterten Form, Quantor, Gruppe, Alternative
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Ein Zeichen, eine Auswahl, eine Stelle: Damit lassen sich Ausdrücke fester Länge schreiben. Dieser Abschnitt ergänzt Wiederholungen, Gruppen und Alternativen, zeigt die zwei Schreibweisen, in denen es sie gibt, und erklärt drei Eigenheiten: welcher Treffer gewinnt, warum ein Ausdruck nur die Form prüft und wie sich reguläre Ausdrücke von den Mustern für Dateinamen unterscheiden.
:::

### Beliebig oft: der Stern

<span class="anker" id="stufe-7-1"></span>

Zahlen haben verschieden viele Stellen, Namen verschieden viele Buchstaben. Ein Ausdruck braucht deshalb eine Möglichkeit zu sagen: „davon beliebig viele“.

:::definition Definition 7.1 (Stern)
<span class="anker" id="satz-7-1"></span>

Ein __Stern__ `*` hinter einem gewöhnlichen Zeichen, einem Punkt oder einem Klammerausdruck passt auf beliebig viele Wiederholungen davon hintereinander, auch auf keine einzige.
:::

`a*` passt also auf die leere Zeichenkette, auf `a`, `aa`, `aaa` und so weiter. `.*` passt auf jede beliebige Folge von Zeichen; es ist die übliche Art, „und dazwischen irgendetwas“ zu schreiben.

::::beispiel Wiederholte Zeichen und beliebiges Dazwischen
```console
$ printf '%s\n' b ab aab ac | grep '^a*b$'
b
ab
aab
$ grep 'Anna.*5\.0' laeufe.csv
2026-11-02,Anna,5.0,28
2026-11-09,Anna,5.0,27
```

Der erste Ausdruck verlangt vom Anfang bis zum Ende beliebig viele a und ein b; `b` allein passt mit null a. Der zweite sucht Zeilen, in denen nach `Anna` irgendwo `5.0` folgt.
::::

::::beispiel [Gegenbeispiel] Ein Stern ohne Halt
```console
$ printf '%s\n' b ab aab ac | grep -c 'a*'
4
```

`a*` passt in jeder Zeile, auch in `b`, denn jede Zeile enthält die leere Zeichenkette, also null a. Ein Ausdruck, der nur aus einem Element mit Stern besteht, sucht deshalb nichts; erst Anker oder feste Zeichen daneben geben ihm Halt.
::::

⁠**Kurz gesagt:** `x*` heißt „beliebig viele x, auch keines“; `.*` passt auf jede Zeichenfolge.

### Die erweiterte Form: grep -E

<span class="anker" id="stufe-7-2"></span>

Für „mindestens eine Ziffer“ oder „genau drei Ziffern“ gibt es eigene Sonderzeichen. Ein Versuch ohne Vorbereitung geht allerdings schief:

```console
$ grep ',[0-9]{3}$' laeufe.csv
$ echo $?
1
$ grep -E ',[0-9]{3}$' laeufe.csv
2026-11-08,Ben,21.1,128
```

Ohne Option findet `grep` nichts, mit `-E` den Lauf über 128 Minuten. Es gibt zwei Schreibweisen für reguläre Ausdrücke; Abbildung [22](#abb-22) zeigt, wie sie denselben Text verschieden lesen.

:::abbildung linux/k6grundform 22
Der Ausdruck `,[0-9]{3}$` zweimal. Oben, ohne Option, sind `{`, `3` und `}` drei gewöhnliche Zeichen, die in der Zeile stehen müssten; der Vergleich mit `,128` scheitert an der geschweiften Klammer. Unten, mit `-E`, wird `{3}` zu einer Anweisung: die Ziffer davor dreimal. Die drei Ziffern `128` leuchten auf.
:::

:::definition Definition 7.2 (Grundform, erweiterte Form)
<span class="anker" id="satz-7-2"></span>

Die __Grundform__ regulärer Ausdrücke ist die Schreibweise, die `grep` ohne Option benutzt; englisch heißt sie „basic regular expressions“, kurz BRE. Darin sind die Zeichen `+ ? { } ( ) |` gewöhnliche Zeichen. In der __erweiterten Form__, englisch „extended regular expressions“, kurz ERE, sind sie zusätzlich Sonderzeichen; `grep -E` schaltet sie ein.
:::

In der Grundform hat `grep` also nach dem Text `{3}` gesucht, der im Lauftagebuch nicht vorkommt. Alles aus Abschnitt [6](regulare-ausdrucke-zeichen-klassen-und-anker.html#stufe-6) und der Stern gelten in beiden Formen gleich.

⁠**Kurz gesagt:** `grep -E` schaltet die erweiterte Form ein, in der `+ ? { } ( ) |` Sonderzeichen sind; ohne `-E` sind sie gewöhnliche Zeichen.

### Wiederholungen zählen: +, ? und {n,m}

<span class="anker" id="stufe-7-3"></span>

Der Stern lässt jede Anzahl zu, auch null. Oft ist aber „mindestens eins“, „vielleicht eins“ oder „genau drei“ gemeint. Abbildung [23](#abb-23) legt die vier Möglichkeiten an dieselben Zeichenketten.

:::abbildung linux/k6quantor 23
Vier Ausdrücke, jeder gegen die Zeichenketten `b`, `ab`, `aab` und `aaab` gelegt, mit Anker an beiden Enden: `a*b` passt auf alle vier, `a+b` auf alle außer `b`, `a?b` nur auf `b` und `ab`, `a{2,3}b` nur auf `aab` und `aaab`. Passende Zeichenketten leuchten auf, die übrigen bleiben grau.
:::

:::definition Definition 7.3 (Quantor)
<span class="anker" id="satz-7-3"></span>

Ein __Quantor__ steht hinter einem Element eines Ausdrucks und legt fest, wie oft es hintereinander vorkommen darf. In der erweiterten Form gibt es außer dem Stern: `+` für mindestens einmal, `?` für keinmal oder einmal, `{n}` für genau $n$-mal, `{n,m}` für $n$- bis $m$-mal und `{n,}` für mindestens $n$-mal.
:::

::::beispiel Kommazahlen, zweistellige Strecken, ein Plural
```console
$ grep -Eo '[0-9]+\.[0-9]+' laeufe.csv | paste -s -d' '
5.0 10.5 7.2 6.4 5.0 12.0 8.0 21.1 5.0
$ grep -E ',[0-9]{2}\.' laeufe.csv
2026-11-02,Ben,10.5,62
2026-11-06,Anna,12.0,70
2026-11-08,Ben,21.1,128
$ printf '%s\n' Minute Minuten Minutenzeiger | grep -E '^Minuten?$'
Minute
Minuten
```

`[0-9]+\.[0-9]+` beschreibt Ziffern, einen Punkt und wieder Ziffern; mit `-o` schneidet `grep` aus jeder Zeile genau die Strecke aus, denn sonst steht nirgends ein Punkt zwischen Ziffern. `,[0-9]{2}\.` findet Strecken mit zwei Stellen vor dem Punkt. `n?` lässt das n offen; die Anker schließen das längere Wort aus.
::::

⁠**Kurz gesagt:** `+` mindestens einmal, `?` höchstens einmal, `{n,m}` zwischen $n$- und $m$-mal; dazu der Stern für beliebig oft.

### Gruppe und Alternative

<span class="anker" id="stufe-7-4"></span>

Ein Quantor wirkt nur auf das Element direkt davor. Soll ein ganzes Wortstück wiederholt oder offengelassen werden, oder soll an einer Stelle das eine oder das andere stehen dürfen, braucht man Klammern und einen senkrechten Strich.

:::definition Definition 7.4 (Gruppe, Alternative)
<span class="anker" id="satz-7-4"></span>

Runde Klammern fassen einen Teil eines Ausdrucks zu einer __Gruppe__ zusammen; ein Quantor hinter der Gruppe wirkt auf sie als Ganzes. Der senkrechte Strich bildet eine __Alternative__: `a|b` passt, wo `a` passt oder wo `b` passt. Der Strich trennt dabei schwächer als alles andere, er teilt den ganzen Ausdruck oder die Gruppe, in der er steht.
:::

`^Anna|Ben` heißt deshalb „Anna am Zeilenanfang oder Ben irgendwo“; „Anna oder Ben am Zeilenanfang“ schreibt man `^(Anna|Ben)`.

::::beispiel Zwei Personen, zwei Tage, zwei Schreibweisen
```console
$ grep -E 'Anna|Clara' laeufe.csv | wc -l
6
$ grep -E '^2026-11-0(2|9),' laeufe.csv
2026-11-02,Anna,5.0,28
2026-11-02,Ben,10.5,62
2026-11-09,Anna,5.0,27
$ echo 'Kilometer km' | grep -oE 'k(ilo)?m(eter)?'
km
```

Sechs Läufe von Anna oder Clara; die Läufe vom 2. und vom 9. November. Im dritten Beispiel machen die Gruppen `ilo` und `eter` als Ganzes optional; der Ausdruck passt auf `km` und auf `Kilometer` mit kleinem k. Weil das Wort im Text mit großem K beginnt, schneidet `-o` nur `km` aus.
::::

⁠**Kurz gesagt:** `(…)` macht aus einem Teil eine Einheit für Quantoren, `a|b` lässt die Wahl; der Strich trennt am schwächsten.

### Grundform und erweiterte Form im Vergleich

<span class="anker" id="stufe-7-5"></span>

Manche Werkzeuge kennen nur eine der beiden Formen, und in Anleitungen begegnet man beiden. Deshalb lohnt ein genauer Blick, wie man dasselbe in der Grundform schreibt.

:::satz Satz 7.5 (Grundform und erweiterte Form)
<span class="anker" id="satz-7-5"></span>

Was die erweiterte Form mit `{ }` und `( )` ausdrückt, schreibt die Grundform mit einem umgekehrten Schrägstrich davor: `\{n,m\}` und `\(…\)`. Ob `\+`, `\?` und `\|` in der Grundform Sonderzeichen sind, überlässt der Standard für Unix-Shells und ihre Werkzeuge jedem Werkzeug selbst; die GNU-Werkzeuge verstehen sie so. Umgekehrt ist in der erweiterten Form ein Zeichen wie `+` mit Schrägstrich davor gewöhnlich.
:::

Tabelle [1](#tab-1) stellt die Schreibweisen gegenüber. `grep` benutzt ohne Option die Grundform.

<span class="anker" id="tab-1"></span>

**Tabelle 1:** Dieselben Ausdrücke in der erweiterten Form und in der Grundform. Punkt, Klammerausdrücke, Zeichenklassen, Anker und der Stern sind in beiden gleich. Die mit (GNU) markierten Formen verstehen die GNU-Werkzeuge; andere Werkzeuge müssen sie nicht kennen.

| Bedeutung | erweiterte Form (`grep -E`) | Grundform (`grep`) |
|---|---|---|
| beliebig oft | `x*` | `x*` |
| mindestens einmal | `x+` | `x\+` (GNU) |
| keinmal oder einmal | `x?` | `x\?` (GNU) |
| $n$- bis $m$-mal | `x{n,m}` | `x\{n,m\}` |
| Gruppe | `(ab)` | `\(ab\)` |
| Alternative | `a\|b` | `a\\|b` (GNU) |
| das Zeichen `+` selbst | `\+` | `+` |

::::beispiel Dieselbe Suche in der Grundform
```console
$ grep ',[0-9]\{3\}$' laeufe.csv
2026-11-08,Ben,21.1,128
$ grep 'Clara\|Ben' laeufe.csv | wc -l
5
```

Mit Schrägstrichen vor den geschweiften Klammern findet die Grundform den Lauf über 128 Minuten, und GNU `grep` versteht auch `\|`: fünf Läufe von Clara oder Ben.
::::

⁠**Kurz gesagt:** In der Grundform bekommen `{ }` und `( )` einen Schrägstrich davor, `\+ \? \|` sind dort eine Zugabe der GNU-Werkzeuge; im Zweifel schreibt man `-E`.

:::hintergrund Warum es zwei Formen gibt
Die Grundform ist die ältere. Sie stammt aus dem Editor `ed` und dem ersten `grep`, die `+`, `?` und `|` noch nicht als Sonderzeichen kannten. Als ein zweites Programm namens `egrep` diese Zeichen hinzunahm, hätten alte Suchtexte mit einem gewöhnlichen `+` plötzlich etwas anderes bedeutet. Also blieb die Grundform, wie sie war, und die erweiterte kam als zweite Schreibweise dazu. Die Handbuchseite `regex` im Abschnitt 7 des Handbuchs ([Kapitel 2, Abschnitt 4.5](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/hilfe-finden.html#stufe-4-5)) nennt die zwei Arten von Ausdrücken offen einen Fehlgriff; loswerden kann man ihn aber nicht mehr. Bei GNU `grep` können beide Formen dasselbe, sie unterscheiden sich nur in der Schreibweise. `egrep` gilt heute als veraltet; GNU `grep` gibt seit Version 3.8 eine Warnung aus und empfiehlt `grep -E`.
:::

### Der längste Treffer

<span class="anker" id="stufe-7-6"></span>

Passt ein Ausdruck an mehreren Stellen einer Zeile oder unterschiedlich weit, muss das Werkzeug sich für einen Treffer entscheiden. Bei `grep` ohne `-o` merkt man davon nichts, denn es schreibt ohnehin die ganze Zeile. Bei `grep -o` und beim Ersetzen kommt es darauf an. Abbildung [24](#abb-24) zeigt die Regel an einem Satz.

:::abbildung linux/k6gierig 24
Der Satz `Anna lief 5 km, Ben lief 10 km` und der Ausdruck `A.*km`. Der Treffer beginnt beim A ganz links. Ein erster Bogen reicht bis zum ersten `km`, ein zweiter, längerer bis zum letzten; der längere gewinnt und leuchtet auf. Darunter `A[^,]*km`: Das Komma darf nicht vorkommen, der Bogen endet beim ersten `km`.
:::

:::satz Satz 7.6 (Längster Treffer)
<span class="anker" id="satz-7-6"></span>

Unter allen Treffern eines Ausdrucks in einer Zeile gilt der, der am weitesten links beginnt. Gibt es ab dieser Stelle mehrere, gilt der längste.
:::

::::beispiel Bis zum letzten km
```console
$ echo 'Anna lief 5 km, Ben lief 10 km' | grep -o 'A.*km'
Anna lief 5 km, Ben lief 10 km
$ echo 'Anna lief 5 km, Ben lief 10 km' | grep -o 'A[^,]*km'
Anna lief 5 km
```

`.*` nimmt so viel, wie es kann, und der Treffer reicht bis zum letzten `km`. Wer nur bis zum ersten will, verbietet in der Wiederholung das Zeichen, an dem sie aufhören soll: `[^,]*` läuft nicht über das Komma hinweg.
::::

⁠**Kurz gesagt:** Es gewinnt der Treffer, der am weitesten links beginnt, und von dort der längste; begrenzen kann man ihn mit einem verneinten Klammerausdruck.

:::hintergrund Gierige und kürzeste Treffer in Programmiersprachen
Viele Programmiersprachen, etwa Python, suchen anders: Sie probieren die Möglichkeiten eines Ausdrucks der Reihe nach und nehmen die erste, die passt; jeder Quantor nimmt dabei so viel, wie er kann, und heißt deshalb gierig. Meist ergibt das denselben Treffer, bei einer Alternative aber nicht: In der Zeile `ab` findet Python mit `a|ab` nur `a`, `grep` den längsten Treffer:

```console
$ echo ab | grep -oE 'a|ab'
ab
```

Diese Sprachen kennen außerdem eine Schreibweise mit einem Fragezeichen hinter dem Quantor, etwa `.*?`, die so wenig nimmt wie möglich. Der Standard für Unix-Shells und ihre Werkzeuge hat sie 2024 für die erweiterte Form aufgenommen, dort als kürzester Treffer. GNU `grep` 3.12 auf dem Testsystem behandelt sie noch wie den gewöhnlichen Stern:

```console
$ echo 'Anna lief 5 km, Ben lief 10 km' | grep -oE 'A.*?km'
Anna lief 5 km, Ben lief 10 km
```

Der verneinte Klammerausdruck ist deshalb der Weg, der überall funktioniert.
:::

### Form statt Bedeutung

<span class="anker" id="stufe-7-7"></span>

Ein Ausdruck für ein Datum scheint leicht: vier Ziffern, Bindestrich, zwei Ziffern, Bindestrich, zwei Ziffern. Ob er auch nur echte Daten findet, zeigt ein Versuch:

```console
$ printf '%s\n' 2026-11-09 2026-13-45 9.11.2026 | grep -E '^[0-9]{4}-[0-9]{2}-[0-9]{2}$'
2026-11-09
2026-13-45
```

Den 45. Tag des 13. Monats gibt es nicht, und doch passt er. Die deutsche Schreibweise `9.11.2026` passt nicht, obwohl sie ein echtes Datum ist.

:::satz Satz 7.7 (Form statt Bedeutung)
<span class="anker" id="satz-7-7"></span>

Ein regulärer Ausdruck prüft nur, welche Zeichen in welcher Reihenfolge stehen. Was diese Zeichen bedeuten, ob eine Zahl groß oder klein ist, ob ein Datum existiert, weiß er nicht. Jede Regel über die Bedeutung muss man, wenn es überhaupt geht, in Regeln über Zeichen übersetzen.
:::

::::beispiel Den Monat genauer fassen
Monate gehen von 01 bis 12. Als Regel über Zeichen heißt das: eine 0 und eine Ziffer von 1 bis 9 oder eine 1 und eine Ziffer von 0 bis 2.

```console
$ printf '%s\n' 2026-11-09 2026-13-45 2026-00-10 | grep -E '^[0-9]{4}-(0[1-9]|1[0-2])-[0-9]{2}$'
2026-11-09
```

Monat 13 und Monat 00 fallen jetzt heraus. Für die Tage ginge es ebenso, doch dass der Februar nur 28 Tage hat, in Schaltjahren 29, macht den Ausdruck schnell unlesbar. Wer die Bedeutung prüfen will, vergleicht besser Zahlen mit einem Werkzeug, das rechnen kann.
::::

Warum ein Ausdruck nur Formen sieht, wird klar, wenn man betrachtet, wie ein Werkzeug ihn prüft. Abbildung [25](#abb-25) zeigt das für den Ausdruck `[0-9]+\.[0-9]+` für Kommazahlen aus Unterabschnitt [7.3](#stufe-7-3): Ein Werkzeug wie `grep` kann die Zeile Zeichen für Zeichen von links lesen und sich dabei nur merken, an welcher Stelle des Ausdrucks es gerade steht. Ob es „zwölf“ oder „zwanzig“ gelesen hat, merkt es sich nicht, nur „ich bin in der Zahl vor dem Punkt“.

:::abbildung linux/k6automat 25
Der Ausdruck `[0-9]+\.[0-9]+` als kleine Maschine mit vier Kreisen, den Zuständen „Start“, „in der Zahl“, „nach dem Punkt“ und „Ziel“. Pfeile tragen die Zeichen, die von einem Kreis zum nächsten führen: eine Ziffer vom Start in die Zahl, weitere Ziffern im Kreis zurück, ein Punkt weiter, eine Ziffer ins Ziel, weitere Ziffern im Ziel im Kreis zurück. Die Zeichenkette `10.5` wandert Zeichen für Zeichen hindurch; bei der 5 ist das Ziel erreicht. Die Maschine merkt sich nur den Kreis, in dem sie steht.
:::

⁠**Kurz gesagt:** Ein regulärer Ausdruck prüft die Form einer Zeichenkette, nicht ihre Bedeutung; `2026-13-45` hat die Form eines Datums.

:::hintergrund Reguläre Ausdrücke und endliche Automaten
Die Maschine aus Abbildung [25](#abb-25) heißt in der Informatik ein endlicher Automat: eine feste, endliche Zahl von Zuständen, und ein Eingabezeichen nach dem anderen bestimmt den nächsten Zustand. Der Mathematiker Stephen Kleene zeigte Anfang der 1950er-Jahre, dass reguläre Ausdrücke im mathematischen Sinn, gebaut nur aus einzelnen Zeichen, Aneinanderreihung, Alternative und Stern, genau die Mengen von Zeichenketten beschreiben, die ein endlicher Automat erkennen kann; der Satz trägt heute seinen Namen. Von ihm stammt auch das Wort „regulär“. Ken Thompson veröffentlichte 1968 ein Verfahren, das einen Ausdruck in so einen Automaten übersetzt und den Text dabei nur einmal von links nach rechts liest, alle Möglichkeiten zugleich verfolgend. Automaten dieser Art sind bis heute die Grundlage schneller Suchwerkzeuge wie `grep`. Daraus folgt eine Grenze: Ein endlicher Automat hat endlich viele Zustände und kann deshalb nicht beliebig weit zählen. Die Menge aller Zeichenketten aus einer Anzahl öffnender Klammern, gefolgt von genauso vielen schließenden, beschreibt kein regulärer Ausdruck. Manche Erweiterungen der Werkzeuge gehen über diese Grenze hinaus, etwa die Forderung, dass ein früher gefundenes Stück noch einmal vorkommt; dann versagen die schnellen Verfahren, und die Suche kann sehr viel langsamer werden.
:::

### Muster für Dateinamen und reguläre Ausdrücke

<span class="anker" id="stufe-7-8"></span>

`*`, `?` und eckige Klammern kennst du aus den Mustern für Dateinamen ([Kapitel 3, Abschnitt 6.6](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/kopieren-verschieben-loschen.html#stufe-6-6) und [Kapitel 5, Abschnitt 1.3](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/expansion-muster-klammern-und-tilde.html#stufe-1-3)). In regulären Ausdrücken kommen dieselben Zeichen vor, mit anderer Bedeutung. Wer beide verwechselt, sucht nach etwas anderem, als er meint.

:::satz Satz 7.8 (Muster und regulärer Ausdruck)
<span class="anker" id="satz-7-8"></span>

Ein Muster für Dateinamen wertet die Shell aus, bevor ein Befehl startet; ein regulärer Ausdruck wird vom Programm ausgewertet, etwa von `grep`. Im Muster steht `*` für eine beliebige Zeichenfolge und `?` für ein beliebiges Zeichen; im regulären Ausdruck wiederholt `*` das Element davor, `.` ist das beliebige Zeichen, und `?` macht in der erweiterten Form das Element davor optional. Ein Muster passt nur auf den ganzen Namen, ein Ausdruck ohne Anker schon auf ein Stück der Zeile.
:::

Tabelle [2](#tab-2) übersetzt die wichtigsten Muster in reguläre Ausdrücke. Die Anker sind nötig, weil ein Muster immer den ganzen Namen meint.

<span class="anker" id="tab-2"></span>

**Tabelle 2:** Muster für Dateinamen und die gleichwertigen regulären Ausdrücke. Ein Punkt ist im Muster ein gewöhnliches Zeichen, im Ausdruck braucht er einen Schrägstrich.

| Bedeutung | Muster für Dateinamen | regulärer Ausdruck |
|---|---|---|
| beliebige Zeichenfolge | `*` | `.*` |
| genau ein beliebiges Zeichen | `?` | `.` |
| ein Zeichen aus einer Liste | `[abc]` | `[abc]` |
| ein Zeichen nicht aus der Liste | `[!abc]` | `[^abc]` |
| alle Namen auf `.csv` | `*.csv` | `^.*\.csv$` |
| `foto` und ein Zeichen, dann `.jpg` | `foto?.jpg` | `^foto.\.jpg$` |

::::beispiel Derselbe Name, zwei Lesarten
```console
$ ls *.csv
drei.csv   kurz.csv    linux.csv  windows.csv
klein.csv  laeufe.csv  neu.csv
$ printf '%s\n' laeufe.csv laeufeXcsv | grep '^laeufe.csv$'
laeufe.csv
laeufeXcsv
$ printf '%s\n' laeufe.csv laeufeXcsv | grep '^laeufe\.csv$'
laeufe.csv
```

Im Muster `*.csv` ist der Punkt ein Punkt. Im Ausdruck passt er auf jedes Zeichen, auch auf das X; erst `\.` meint den Punkt. Hast du die Aufgaben im Übungsverzeichnis gelöst, nennt `ls` weitere Dateien.
::::

::::beispiel [Gegenbeispiel] Ein Ausdruck ohne Anführungszeichen
Hier zeigt sich, warum reguläre Ausdrücke in einfache Anführungszeichen gehören. Im Übungsverzeichnis liegt kurz eine Datei `Anna.txt`:

```console
$ touch Anna.txt
$ echo grep -c Ann* laeufe.csv
grep -c Anna.txt laeufe.csv
$ grep -c Ann* laeufe.csv
0
$ grep -c 'Ann*' laeufe.csv
4
$ rm Anna.txt
```

Ohne Anführungszeichen hält die Shell `Ann*` für ein Muster und ersetzt es durch den passenden Dateinamen, wie `echo` zeigt. `grep` sucht dann nach `Anna.txt` und findet nichts. Mit Anführungszeichen kommt der Ausdruck an: `An` und beliebig viele `n`, in vier Zeilen. Gäbe es keine passende Datei, bliebe das Muster stehen ([Kapitel 5, Abschnitt 1.5](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/expansion-muster-klammern-und-tilde.html#stufe-1-5)), und der Fehler fiele gar nicht auf, bis eines Tages eine passende Datei im Verzeichnis liegt.
::::

⁠**Kurz gesagt:** Muster wertet die Shell an Dateinamen aus, reguläre Ausdrücke das Programm an Zeilen; `*`, `?` und der Punkt bedeuten in beiden Verschiedenes.

### Aufgaben zu Abschnitt [7](#stufe-7)

<span class="anker" id="stufe-7-9"></span>

:::aufgabe Aufgabe 18 ★★ Lange Läufe, große Zahlen
<span class="anker" id="aufg-18"></span>

(a) Gib mit einem Quantor alle Läufe aus, die mindestens 100 Minuten dauerten. (b) Gib alle Strecken aus, die vor dem Punkt zwei Ziffern haben, ohne die übrigen Felder der Zeile.

:::loesung
```console
$ grep -E ',[0-9]{3,}$' laeufe.csv
2026-11-08,Ben,21.1,128
$ cut -d, -f3 laeufe.csv | grep -E '^[0-9]{2}\.'
10.5
12.0
21.1
```

(a) Mindestens drei Ziffern zwischen dem letzten Komma und dem Zeilenende, also mindestens 100 Minuten. (b) `cut` liefert nur die Strecken, eine je Zeile; der Ausdruck verlangt am Zeilenanfang genau zwei Ziffern und dann einen Punkt. Weil `grep` ganze Zeilen ausgibt und jede Zeile nur noch eine Strecke ist, braucht es kein `-o`.
:::
:::

:::aufgabe Aufgabe 19 ★★ Form statt Bedeutung bei Adressen
<span class="anker" id="aufg-19"></span>

Die Adressen von Geräten in einem Netz aus [Kapitel 1, Abschnitt 3.6](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/virtuelle-maschinen-der-rechner-im-rechner.html#stufe-3-6) schreibt man als vier Zahlen mit Punkten dazwischen, etwa `192.168.178.1`; jede der vier Zahlen liegt zwischen 0 und 255. Lege eine Datei `adressen.txt` mit den Zeilen `192.168.178.1`, `10.0.2.15`, `999.1.1.1`, `1.2.3` und `256.0.0.1` an. (a) Welche Zeilen findet `grep -E '^([0-9]{1,3}\.){3}[0-9]{1,3}$'`? Erkläre den Ausdruck Stück für Stück. (b) Welche gefundenen Zeilen sind keine gültigen Adressen, und warum findet der Ausdruck sie trotzdem? (c) ★★★ Schreibe einen Ausdruck, der für jede der vier Zahlen nur 0 bis 255 zulässt.

:::loesung
```console
$ printf '%s\n' 192.168.178.1 10.0.2.15 999.1.1.1 1.2.3 256.0.0.1 > adressen.txt
$ grep -E '^([0-9]{1,3}\.){3}[0-9]{1,3}$' adressen.txt
192.168.178.1
10.0.2.15
999.1.1.1
256.0.0.1
$ grep -E '^((25[0-5]|2[0-4][0-9]|1?[0-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1?[0-9]?[0-9])$' adressen.txt
192.168.178.1
10.0.2.15
```

(a) Der Ausdruck liest sich von links: Zeilenanfang; dann dreimal die Gruppe aus einer bis drei Ziffern und einem Punkt; dann noch einmal eine bis drei Ziffern; dann das Zeilenende. Gefunden werden alle Zeilen außer `1.2.3`, der eine Zahl fehlt. (b) `999.1.1.1` und `256.0.0.1` haben die Form einer Adresse, aber Zahlen über 255. Der Ausdruck prüft nur „bis zu drei Ziffern“ und weiß nichts von Zahlenwerten: Form statt Bedeutung. (c) Die Regel „0 bis 255“ muss man in Regeln über Ziffern übersetzen: `25` und eine Ziffer von 0 bis 5, oder `2`, eine Ziffer von 0 bis 4 und eine beliebige, oder eine höchstens dreistellige Zahl, deren erste Stelle, wenn es drei sind, eine 1 ist; das schreibt `1?[0-9]?[0-9]`. Diese Gruppe steht viermal da, dreimal mit Punkt. Der Ausdruck ist richtig, aber kaum noch lesbar; für solche Prüfungen nimmt man besser ein Werkzeug, das mit Zahlen rechnet.
:::
:::

:::aufgabe Aufgabe 20 ★★★ Der längste Treffer
<span class="anker" id="aufg-20"></span>

Sage voraus, was `grep -o` bei diesen Eingaben ausgibt, und prüfe es: (a) `'a.*a'` auf die Zeile `Anna lief mit Clara`; (b) `'n*'` auf dieselbe Zeile; (c) `grep -oE '[0-9]+'` auf die Zeile `2026-11-02,Anna,5.0,28`.

:::loesung
```console
$ echo 'Anna lief mit Clara' | grep -o 'a.*a'
a lief mit Clara
$ echo 'Anna lief mit Clara' | grep -o 'n*'
nn
$ echo '2026-11-02,Anna,5.0,28' | grep -oE '[0-9]+' | paste -s -d' '
2026 11 02 5 0 28
```

(a) Das erste kleine a steht am Ende von `Anna`, denn das große A passt nicht. Von dort gewinnt der längste Treffer, bis zum letzten a in `Clara`. (b) `n*` passt an jeder Stelle, notfalls auf null n. `grep -o` schreibt aber nur Treffer, die nicht leer sind; der einzige ist `nn` in `Anna`, wo der längste Treffer beide n umfasst. (c) `grep -o` sucht nach jedem Treffer hinter ihm weiter. Jeder Treffer ist eine längste Folge von Ziffern; Bindestriche, Kommas und der Punkt beenden ihn. So zerfällt die Zeile in sechs Zahlen.
:::
:::

:::aufgabe Aufgabe 21 ★★ Übersetzen
<span class="anker" id="aufg-21"></span>

(a) Übersetze die Muster `foto?.jpg`, `*.csv` und `[!0-9]*` in reguläre Ausdrücke für `grep` und prüfe sie an einer Datei mit den Zeilen `foto1.jpg`, `foto10.jpg`, `foto2.png`, `bericht.csv` und `3plan.txt`. (b) Schreibe `grep -E '(Anna|Ben),[0-9]{2}\.'` in der Grundform.

:::loesung
```console
$ printf '%s\n' foto1.jpg foto10.jpg foto2.png bericht.csv 3plan.txt > namensliste.txt
$ grep '^foto.\.jpg$' namensliste.txt
foto1.jpg
$ grep '\.csv$' namensliste.txt
bericht.csv
$ grep '^[^0-9]' namensliste.txt
foto1.jpg
foto10.jpg
foto2.png
bericht.csv
$ grep -E '(Anna|Ben),[0-9]{2}\.' laeufe.csv
2026-11-02,Ben,10.5,62
2026-11-06,Anna,12.0,70
2026-11-08,Ben,21.1,128
$ grep '\(Anna\|Ben\),[0-9]\{2\}\.' laeufe.csv
2026-11-02,Ben,10.5,62
2026-11-06,Anna,12.0,70
2026-11-08,Ben,21.1,128
```

(a) `foto?.jpg` wird `^foto.\.jpg$`: das Fragezeichen wird zum Punkt, der Punkt der Endung braucht einen Schrägstrich, und die Anker verlangen den ganzen Namen; `foto10.jpg` hat zwei Zeichen nach `foto` und fällt heraus. `*.csv` wird `^.*\.csv$`; weil `^.*` auf jeden Anfang passt, genügt `\.csv$`. `[!0-9]*` wird `^[^0-9]`: ein erstes Zeichen, das keine Ziffer ist, der Rest ist beliebig und braucht keinen Ausdruck. (b) In der Grundform bekommen Klammern, senkrechter Strich und geschweifte Klammern einen Schrägstrich; `\|` ist eine Zugabe der GNU-Werkzeuge. Beide Formen finden dieselben drei Läufe über mindestens 10 km von Anna oder Ben.
:::
:::

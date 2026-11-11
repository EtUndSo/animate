---
title: Variablen, Befehlsersetzung und Arithmetik
pfad: Informatik / Linux und Kommandozeile / Wie die Shell eine Befehlszeile liest: Expansion, Quoting, Variablen, Umgebung
adresse: informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung
knoten: Kapitel 5: Wie die Shell eine Befehlszeile liest: Expansion, Quoting, Variablen, Umgebung
order: 6100300
summary: Die Erweiterungen aus Abschnitt 1 ersetzen Text nach festen Regeln.
tags: Shell-Variable, Zuweisung, Parametererweiterung, Parameter, Befehlsersetzung, Arithmetik
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Die Erweiterungen aus Abschnitt [1](expansion-muster-klammern-und-tilde.html#stufe-1) ersetzen Text nach festen Regeln. Dieser Abschnitt führt Erweiterungen ein, die Werte einsetzen: den Wert einer Variablen, die Ausgabe eines Befehls und das Ergebnis einer Rechnung.
:::

### Die Shell-Variable

<span class="anker" id="stufe-2-1"></span>

Manche Angaben braucht man in mehreren Befehlen hintereinander: einen langen Pfad, einen Namen, ein Ergebnis. Statt sie jedes Mal neu zu tippen, möchte man sie sich unter einem kurzen Namen merken.

Als Bild zur Orientierung: eine Schublade mit einem Etikett. Auf dem Etikett steht der Name, in der Schublade liegt ein Zettel mit Text. Man kann den Zettel jederzeit austauschen, und wer den Namen nennt, bekommt den Text, der gerade darin liegt. Abbildung [6](#abb-6) zeigt eine solche Schublade.

:::abbildung linux/k5variable 6
Eine Shell-Variable als Schublade. Die Zuweisung `wohnort=Hamburg` legt den Text `Hamburg` in die Schublade mit dem Etikett `wohnort`. In `echo Ich wohne in $wohnort` ersetzt die Shell `$wohnort` durch den Inhalt der Schublade, bevor `echo` startet.
:::

:::definition Definition 2.1 (Shell-Variable, Zuweisung)
<span class="anker" id="satz-2-1"></span>

Eine __Shell-Variable__ ist ein Name, unter dem die laufende Shell einen Text speichert, den *Wert* der Variablen. Man legt eine Variable mit einer __Zuweisung__ der Form `NAME=wert` an oder ändert ihren Wert; vor und nach dem Gleichheitszeichen steht kein Leerzeichen. Der Name besteht aus Buchstaben ohne Umlaute, Ziffern und dem Unterstrich und beginnt nicht mit einer Ziffer; Groß- und Kleinbuchstaben sind verschieden.
:::

Steht in einer Befehlszeile `$NAME`, setzt die Shell dort den Wert ein. Der Wert ist immer Text, auch wenn er wie eine Zahl aussieht. Enthält er Leerzeichen, braucht er Anführungszeichen, damit er ein einziges Wort bleibt, wie ein Dateiname mit Leerzeichen.

::::beispiel Wohnort, Gruß und Pfad
```console
$ wohnort=Hamburg
$ echo Ich wohne in $wohnort
Ich wohne in Hamburg
$ gruss="Guten Morgen"
$ echo $gruss
Guten Morgen
$ ordner=~/linuxk5
$ echo $ordner
/home/student/linuxk5
```

Eine Zuweisung gibt nichts aus. In der letzten Zuweisung hat die Shell die Tilde direkt nach dem Gleichheitszeichen ersetzt; in der Variablen steht der volle Pfad. Das ist die Ausnahme von der Regel aus Unterabschnitt [1.7](expansion-muster-klammern-und-tilde.html#stufe-1-7): In einer Zuweisung ersetzt die Shell eine Tilde auch direkt nach dem Gleichheitszeichen und nach jedem Doppelpunkt, und bash tut das sogar bei einem Argument, das wie eine Zuweisung aussieht, etwa `echo x=~`.
::::

Das Leerzeichen um das Gleichheitszeichen ist der häufigste Fehler mit Variablen. Abbildung [7](#abb-7) zeigt, was die Shell aus der Zeile macht.

:::abbildung linux/k5zuweisung 7
Oben `wohnort=Hamburg`: ein einziges Wort mit Gleichheitszeichen, also eine Zuweisung. Unten `wohnort = Hamburg`: Die Shell zerlegt die Zeile an den Leerzeichen in drei Wörter; das erste ist der Befehl `wohnort`, die anderen beiden seine Argumente.
:::

::::beispiel Ein Leerzeichen zu viel
```console
$ wohnort = Hamburg
wohnort: command not found
$ echo $?
127
```

Die Shell sucht ein Programm namens `wohnort`, findet keines und meldet das mit dem Exit-Status 127.
::::

⁠**Kurz gesagt:** Eine Shell-Variable speichert unter einem Namen einen Text; `NAME=wert` ohne Leerzeichen legt ihn ab.

:::hintergrund Variablen in der Shell und in Python
Wer Variablen aus Python kennt ([Python, Kapitel 2, Abschnitt 6.2](/wissen/informatik/programmieren/python/werte-typen-und-variablen/variablen-namen-fur-objekte.html#stufe-6-2)), erkennt die Idee wieder: ein Name für einen Wert. Zwei Unterschiede sind wichtig. Erstens kennt die Shell keine Typen: Jeder Wert ist Text, und erst ein Befehl entscheidet, ob er ihn als Zahl deutet. Zweitens ist das Leerzeichen in der Shell kein Schmuck, sondern trennt Wörter; `x = 5` ist in Python eine Zuweisung, in der Shell der Aufruf eines Befehls `x`.
:::

### Die Parametererweiterung: `$NAME` und `${NAME}`

<span class="anker" id="stufe-2-2"></span>

Steht hinter dem Namen einer Variablen direkt weiterer Text, etwa eine Ziffer oder eine Endung, muss die Shell entscheiden, wo der Name aufhört. Und was geschieht, wenn eine Variable gar nicht existiert?

:::definition Definition 2.2 (Parametererweiterung)
<span class="anker" id="satz-2-2"></span>

Die __Parametererweiterung__ ersetzt `$NAME` oder `${NAME}` durch den Wert der Variablen. Ohne geschweifte Klammern nimmt die Shell als Namen so viele Zeichen, wie ein Name haben kann; mit Klammern endet der Name an der schließenden Klammer. Hat die Variable keinen Wert, setzt die Shell leeren Text ein, ohne Fehlermeldung.
:::

Allgemein heißt alles, was einen Wert speichert, den die Shell mit einem vorangestellten Dollarzeichen einsetzt, ein __Parameter__. Variablen sind Parameter mit einem Namen; andere Parameter tragen statt eines Namens eine Zahl oder ein Sonderzeichen. `$?` aus [Kapitel 4](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/stroeme-umleitung-pipes-und-exit-status.html) ist ein besonderer Parameter, den die Shell selbst setzt; er wird auf dieselbe Weise eingesetzt. Der eingebaute Befehl `unset` löscht eine Variable.

::::beispiel Wo der Name endet
```console
$ echo Wert: $gibtsnicht Ende
Wert: Ende
$ datei=foto
$ echo $datei1.jpg
.jpg
$ echo ${datei}1.jpg
foto1.jpg
$ unset wohnort
$ echo Wohnort: $wohnort Ende
Wohnort: Ende
```

In `$datei1.jpg` gehört die `1` noch zum Namen, denn Ziffern dürfen in Namen vorkommen. Die Shell sucht also eine Variable `datei1`, findet keine und setzt leeren Text ein; übrig bleibt `.jpg`. Die Klammern in `${datei}1.jpg` beenden den Namen vor der `1`. Nach `unset` ist `wohnort` leer, und auch hier gibt es keine Fehlermeldung.
::::

⁠**Kurz gesagt:** `$NAME` setzt den Wert einer Variablen ein, `${NAME}` grenzt den Namen ab; eine unbekannte Variable ergibt leeren Text.

:::hintergrund Vorgabewerte und Längen
Die geschweiften Klammern können mehr als nur den Namen abgrenzen. `${NAME:-vorgabe}` setzt den Wert ein oder, wenn die Variable leer ist oder fehlt, den Text `vorgabe`. `${#NAME}` setzt die Zahl der Zeichen des Werts ein:

```console
$ echo ${wohnort:-unbekannt}
unbekannt
$ wohnort=Hamburg
$ echo ${wohnort:-unbekannt} ${#wohnort}
Hamburg 7
```

Es gibt noch viele weitere Formen, etwa zum Abschneiden von Endungen; das Handbuch der bash beschreibt sie im Teil „Parameter Expansion“ (`man bash`).
:::

### Die Befehlsersetzung

<span class="anker" id="stufe-2-3"></span>

Manchmal kennt man einen Wert nicht im Voraus, aber ein Befehl kann ihn ausgeben: wie viele Dateien im Verzeichnis liegen, wer angemeldet ist, auf welchen Wochentag ein Datum fällt. Diese Ausgabe möchte man direkt in eine andere Befehlszeile einsetzen. Abbildung [8](#abb-8) zeigt, wie die Shell das macht.

:::abbildung linux/k5befehlsersetzung 8
Die Befehlsersetzung in `echo Angemeldet ist $(whoami)`: Zuerst lässt die Shell `whoami` in einem eigenen Prozess laufen und fängt seine Standardausgabe `student` samt Zeilenende auf. Das Zeilenende am Schluss fällt weg, der Rest ersetzt `$(whoami)`. Erst dann startet `echo`.
:::

:::definition Definition 2.3 (Befehlsersetzung)
<span class="anker" id="satz-2-3"></span>

Die __Befehlsersetzung__ `$(befehl)` führt den Befehl in den Klammern in einem eigenen Prozess aus und ersetzt sich selbst durch dessen Standardausgabe. Zeilenenden am Ende der Ausgabe entfernt die Shell dabei.
:::

::::beispiel Benutzer, Rechner, Einträge und ein Wochentag
```console
$ echo Angemeldet ist $(whoami) auf $(hostname)
Angemeldet ist student auf labor
$ anzahl=$(ls | wc -l)
$ echo Im Verzeichnis liegen $anzahl Einträge
Im Verzeichnis liegen 6 Einträge
$ echo Heiligabend 2026 ist ein $(date -d 2026-12-24 +%A)
Heiligabend 2026 ist ein Thursday
```

`whoami` nennt den Benutzer, `hostname` den Namen des Rechners. In der zweiten Befehlszeile läuft innerhalb der Befehlsersetzung sogar eine ganze Pipeline; ihr Ergebnis landet in einer Variablen. Gezählt werden sechs Einträge: fünf Dateien und das Verzeichnis `urlaub`; die versteckte Datei zeigt `ls` nicht. `date -d` rechnet mit dem angegebenen Datum statt mit dem heutigen, und `+%A` verlangt den Namen des Wochentags; weil das Testsystem auf Englisch eingestellt ist, heißt er `Thursday`.
::::

⁠**Kurz gesagt:** `$(befehl)` setzt die Ausgabe eines Befehls in die Befehlszeile ein, ohne die Zeilenenden am Schluss.

:::hintergrund Die alte Schreibweise mit Gravis
Ältere Anleitungen schreiben die Befehlsersetzung mit zwei Gravis-Zeichen, dem nach links geneigten Akzent: `` `befehl` ``.

```console
$ echo `whoami`
student
```

Die Form funktioniert noch, gilt aber als veraltet. Sie ist schwer vom Apostroph zu unterscheiden, und ineinander geschachtelte Befehlsersetzungen brauchen damit zusätzliche umgekehrte Schrägstriche; mit `$(…)` schachtelt man einfach Klammern.
:::

### Die Arithmetik

<span class="anker" id="stufe-2-4"></span>

Für eine schnelle Rechnung muss man kein eigenes Programm starten: Die Shell kann selbst mit ganzen Zahlen rechnen. Auch das ist eine Erweiterung: Die Shell setzt das Ergebnis der Rechnung in die Zeile ein.

:::definition Definition 2.4 (Arithmetik)
<span class="anker" id="satz-2-4"></span>

Die __Arithmetik__ `$((ausdruck))` rechnet den Ausdruck in den doppelten Klammern mit ganzen Zahlen aus und setzt das Ergebnis als Text ein. Erlaubt sind unter anderem `+`, `-`, `*` (mal), `/` (geteilt), `%` (Rest der Division), `**` (hoch) und runde Klammern; Punktrechnung geht vor Strichrechnung. `/` schneidet den Rest ab. Variablen nennt man im Ausdruck mit ihrem Namen, ein `$` ist dort nicht nötig.
:::

Ein `*` innerhalb von `$((…))` ist kein Muster, sondern das Malzeichen. Leerzeichen im Ausdruck sind erlaubt.

::::beispiel Ein Einkauf in Cent
Drei Brötchen zu je 45 Cent und zwei Liter Milch zu je 119 Cent: Wie viel kostet das in Euro und Cent? Weil die Shell nur ganze Zahlen kennt, rechnet man in Cent:

```console
$ echo $((3 * 45))
135
$ summe=$((3*45 + 2*119))
$ echo $summe
373
$ echo $((summe / 100)) Euro und $((summe % 100)) Cent
3 Euro und 73 Cent
```

Abbildung [9](#abb-9) rechnet Schritt für Schritt nach. In `summe / 100` steht kein `$` vor dem Namen; die Shell schlägt ihn im Ausdruck selbst nach.

:::abbildung linux/k5rechnung 9
Die Rechnung des Einkaufs: $3 \cdot 45 + 2 \cdot 119 = 135 + 238 = 373$ Cent. Die ganzzahlige Division durch 100 ergibt 3 Euro, der Rest 73 Cent; zur Probe $3 \cdot 100 + 73 = 373$.
:::
::::

::::beispiel [Zweites Beispiel] Teilen ohne Komma
```console
$ echo $((7 / 2)) $((7 % 2)) $((-7 / 2))
3 1 -3
$ echo $((2 ** 10))
1024
$ echo $(( (3 + 4) * 2 )) $(( 3 + 4 * 2 ))
14 11
```

$7/2$ wäre 3,5; die Shell schneidet die Stellen nach dem Komma ab und liefert 3, der Rest ist 1. Bei $-7/2$ schneidet sie ebenfalls ab, es ergibt sich $-3$, nicht $-4$. Die Klammern ändern die Reihenfolge der Rechnung wie in der Schule.
::::

⁠**Kurz gesagt:** `$((…))` rechnet mit ganzen Zahlen und setzt das Ergebnis ein; `/` schneidet den Rest ab, `%` liefert ihn.

:::hintergrund Warum nur ganze Zahlen und wie groß?
Die Shell rechnet mit ganzen Zahlen fester Größe, wie sie der Prozessor direkt verarbeitet; der Standard für Unix-Shells verlangt dafür ganze Zahlen mit Vorzeichen. Kommazahlen kennt sie nicht, eine Division durch null meldet sie als Fehler, und die Zahlen haben auf dem Testsystem 64 Bit. Die größte ist $2^{63} - 1$; eine Stelle darüber springt das Ergebnis ohne Warnung ins Negative:

```console
$ echo $((7 / 2.5))
bash: 7 / 2.5: arithmetic syntax error: invalid arithmetic operator (error token is ".5")
$ echo $((1 / 0))
bash: 1 / 0: division by 0 (error token is "0")
$ echo $((2 ** 63 - 1)) $((2 ** 63))
9223372036854775807 -9223372036854775808
```

Für Kommazahlen nimmt man ein anderes Werkzeug, etwa Python ([Python, Kapitel 2](/wissen/informatik/programmieren/python/werte-typen-und-variablen/werte-typen-und-variablen.html)). Für die Shell selbst genügen ganze Zahlen meist: Sie zählt Dateien, Zeilen und Wiederholungen.
:::

### Aufgaben zu Abschnitt [2](#stufe-2)

<span class="anker" id="stufe-2-5"></span>

:::aufgabe Aufgabe 5 ★ Ein Name mit Endung
<span class="anker" id="aufg-5"></span>

(a) Lege die Variablen `vorname` mit dem Wert `Lea` und `nachname` mit dem Wert `Berg` an und lass `echo` den Satz `Hallo, Lea Berg` schreiben. (b) Sage voraus, was `echo $vorname_notizen.txt` ausgibt, und erkläre es. (c) Lege mit `touch` eine leere Datei an, deren Name aus dem Vornamen und der Endung `_notizen.txt` besteht, also `Lea_notizen.txt`, ohne den Vornamen dabei auszuschreiben.

:::loesung
```console
$ vorname=Lea
$ nachname=Berg
$ echo Hallo, $vorname $nachname
Hallo, Lea Berg
$ echo $vorname_notizen.txt
.txt
$ touch ${vorname}_notizen.txt
$ ls *notizen*
Lea_notizen.txt
```

(a) Zwei Zuweisungen ohne Leerzeichen um das Gleichheitszeichen, dann setzt die Shell die beiden Werte für `echo` ein. (b) Der Unterstrich darf in Namen vorkommen, also sucht die Shell eine Variable `vorname_notizen`. Die gibt es nicht; sie wird zu leerem Text, und übrig bleibt `.txt`. (c) Die geschweiften Klammern beenden den Namen vor dem Unterstrich: `${vorname}_notizen.txt` ergibt `Lea_notizen.txt`.
:::
:::

:::aufgabe Aufgabe 6 ★ Drei falsche Zuweisungen
<span class="anker" id="aufg-6"></span>

Die Variable `wohnort` hat den Wert `Hamburg`. Jemand will ihn in `Köln` ändern und probiert drei Zeilen: (a) `wohnort = Köln` (b) `Wohnort=Köln` (c) `$wohnort=Köln`. Sage für jede voraus, ob die Shell ein Programm sucht und unter welchem Namen, und prüfe es. Welchen Wert hat `wohnort` danach?

:::loesung
```console
$ wohnort=Hamburg
$ wohnort = Köln
wohnort: command not found
$ Wohnort=Köln
$ $wohnort=Köln
Hamburg=Köln: command not found
$ echo $wohnort $Wohnort
Hamburg Köln
```

(a) Drei Wörter; das erste, `wohnort`, ist der Befehl. (b) Ein einziges Wort mit Gleichheitszeichen und einem gültigen Namen davor, also eine Zuweisung; die Shell sucht kein Programm und meldet nichts. Weil Groß- und Kleinbuchstaben verschieden sind, entsteht aber eine neue Variable `Wohnort`, und `wohnort` bleibt unberührt. (c) `$wohnort` wird zuerst durch `Hamburg` ersetzt. Das Wort `Hamburg=Köln` ist danach keine Zuweisung, denn ob ein Wort eine Zuweisung ist, entscheidet die Shell schon beim Zerlegen, als dort noch `$wohnort=Köln` stand; ein Name beginnt aber nicht mit `$`. Also ist es ein Befehlsname. In allen drei Fällen bleibt `wohnort` bei `Hamburg`; die letzte Zeile zeigt beide Variablen. Richtig wäre `wohnort=Köln`.
:::
:::

:::aufgabe Aufgabe 7 ★★ Rechnen mit ganzen Zahlen
<span class="anker" id="aufg-7"></span>

(a) Eine Fahrt dauert 437 Minuten. Lass die Shell ausgeben, wie viele Stunden und Minuten das sind. (b) Drei Noten lauten 2, 3 und 2. Was liefert `echo $(( (2 + 3 + 2) / 3 ))`, und wie weit liegt das vom wahren Durchschnitt entfernt? (c) Warum ergibt `$((10 / 3 * 3))` nicht dasselbe wie `$((10 * 3 / 3))`?

:::loesung
```console
$ echo $((437 / 60)) Stunden und $((437 % 60)) Minuten
7 Stunden und 17 Minuten
$ echo $(( (2 + 3 + 2) / 3 ))
2
$ echo $((10 / 3 * 3)) $((10 * 3 / 3))
9 10
```

(a) Eine Stunde hat 60 Minuten. Die ganzzahlige Division $437 / 60$ liefert die vollen Stunden, 7; der Rest $437 - 7 \cdot 60 = 17$ sind die Minuten. (b) Die Summe ist 7, und $7/3 = 2{,}33\ldots$; die Shell schneidet ab und liefert 2. Der Fehler beträgt ein Drittel. Wer genauer rechnen will, rechnet in kleineren Einheiten, etwa in Hundertsteln: `$(( (2 + 3 + 2) * 100 / 3 ))` ergibt 233, also 2,33. (c) Gleichrangige Rechenzeichen rechnet die Shell von links nach rechts. Links wird zuerst geteilt: $10/3 = 3$, der Rest geht verloren, und $3 \cdot 3 = 9$. Rechts wird zuerst malgenommen: $10 \cdot 3 = 30$ und $30/3 = 10$. Bei ganzen Zahlen teilt man deshalb möglichst spät.
:::
:::

:::aufgabe Aufgabe 8 ★★ Werte aus Befehlen
<span class="anker" id="aufg-8"></span>

(a) Speichere die Zahl der Dateien mit der Endung `.jpg` in deinem Übungsverzeichnis in einer Variablen `anzahl` und lass einen Satz wie `Es gibt 3 Fotos` ausgeben. (b) Lass die Shell mit einer einzigen Zeile ausgeben, auf welchen Wochentag der 17. Mai 2027 fällt.

:::loesung
```console
$ anzahl=$(ls *.jpg | wc -l)
$ echo Es gibt $anzahl Fotos
Es gibt 3 Fotos
$ echo Der 17. Mai 2027 ist ein $(date -d 2027-05-17 +%A)
Der 17. Mai 2027 ist ein Monday
```

(a) Die Pfadnamen-Erweiterung gibt `ls` die drei Fotos; `ls` schreibt sie in die Pipe je eine pro Zeile, `wc -l` zählt drei Zeilen, und die Befehlsersetzung legt die Zahl in der Variablen ab. (b) `date -d` rechnet mit dem genannten Tag, `+%A` verlangt den Wochentag. Auf einem deutsch eingestellten System hieße er `Montag`.
:::
:::

---
title: Entscheidungen: if, elif und else
pfad: Informatik / Programmieren / Python / Entscheidungen und Schleifen
adresse: informatik/programmieren/python/entscheidungen-und-schleifen
knoten: Kapitel 3: Entscheidungen und Schleifen
order: 6040300
summary: Mit einer Bedingung allein passiert noch nichts; ein Skript läuft weiterhin Zeile für Zeile von oben nach unten (Kapitel 1, Abschnitt 5.2).
tags: bedingte Anweisung, Kopfzeile, Block
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Mit einer Bedingung allein passiert noch nichts; ein Skript läuft weiterhin Zeile für Zeile von oben nach unten ([Kapitel 1, Abschnitt 5.2](/wissen/informatik/programmieren/python/programme-und-der-python-interpreter/skripte-schreiben-und-ausfuhren.html#stufe-5-2)). Dieser Abschnitt zeigt, wie ein Skript Zeilen nur ausführt, wenn eine Bedingung erfüllt ist, wie Python erkennt, welche Zeilen dazugehören, und wie man zwischen mehreren Fällen wählt.
:::

### Die bedingte Anweisung `if`

<span class="anker" id="stufe-2-1"></span>

Ein Skript liest die Temperatur in einem Zimmer ein. Eine Warnung soll es nur ausgeben, wenn es dort wärmer als 23 °C ist.

**Eine Weiche im Ablauf.** Ein Flussdiagramm zeichnet den Ablauf eines Programms: Ein Kasten steht für eine Anweisung, eine Raute für eine Frage, und die Pfeile zeigen, was als Nächstes kommt. Aus der Raute führen zwei Pfeile, einer für ja und einer für nein (Abb. [1](#abb-1), links). Auf dem Nein-Weg wird der Kasten mit der Warnung einfach umgangen.

:::abbildung prog/k3if 1
Flussdiagramme einer Entscheidung. Links `if`: Ist die Bedingung erfüllt, läuft der Kasten unter der Raute, sonst wird er umgangen. Rechts `if` mit `else`: Genau einer der beiden Kästen läuft. In beiden Fällen geht es danach an derselben Stelle weiter.
:::

:::definition Definition 2.1 (Bedingte Anweisung)
<span class="anker" id="satz-2-1"></span>

Eine __bedingte Anweisung__ hat die Form

`if Bedingung:` ` Anweisungen`

Die erste Zeile heißt __Kopfzeile__; sie beginnt mit `if` und endet mit einem Doppelpunkt. Darunter stehen eine oder mehrere Anweisungen, weiter eingerückt als die Kopfzeile. Python wertet die Bedingung aus und bestimmt ihren Wahrheitswert (Unterabschnitt [1.9](bedingungen-vergleiche-und-logische-operatoren.html#stufe-1-9)). Ist er `True`, führt Python die eingerückten Anweisungen aus, sonst überspringt es sie. In beiden Fällen geht es danach mit der nächsten Zeile weiter, die wieder so weit links steht wie die Kopfzeile.
:::

::::beispiel
Das Skript fragt die Temperatur ab und prüft sie:

```python temperatur_if.py
# Zimmertemperatur prüfen: gewünscht sind höchstens 23 Grad
temp = float(input("Temperatur in Grad: "))
if temp > 23:
    print("Achtung: zu warm")
print("fertig")
```

Zweimal gestartet, einmal mit 24,5 °C und einmal mit 22 °C:

```console Linux
$ python3 temperatur_if.py
Temperatur in Grad: 24.5
Achtung: zu warm
fertig
$ python3 temperatur_if.py
Temperatur in Grad: 22
fertig
```

```console Windows (PowerShell)
PS> py temperatur_if.py
Temperatur in Grad: 24.5
Achtung: zu warm
fertig
```

Die letzte Zeile des Skripts läuft in beiden Fällen, denn sie gehört nicht mehr zur Bedingung.
::::

⁠**Kurz gesagt:** `if Bedingung:` führt die eingerückten Zeilen darunter nur aus, wenn die Bedingung wahr ist.

### Der Block und die Einrückung

<span class="anker" id="stufe-2-2"></span>

Oft hängen mehrere Anweisungen an derselben Bedingung. Python muss dann erkennen, wo sie aufhören und wo das Skript für alle Fälle weitergeht.

**Wie eine Gliederung.** In einer Gliederung rücken Unterpunkte ein; was weiter links steht, gehört nicht mehr dazu. Python liest die Einrückung genauso (Abb. [2](#abb-2)).

:::abbildung prog/k3block 2
Ein Block ist an seiner Einrückung zu erkennen. Die zwei eingerückten Zeilen (blau hinterlegt) gehören zur Kopfzeile darüber; die letzte Zeile steht wieder so weit links wie die Kopfzeile und läuft immer.
:::

:::definition Definition 2.2 (Block)
<span class="anker" id="satz-2-2"></span>

Ein __Block__ ist eine Folge von Anweisungen, die alle gleich weit eingerückt sind und auf eine Kopfzeile folgen, also auf eine Zeile mit einem Doppelpunkt am Ende. Er endet vor der ersten Zeile, die weniger weit eingerückt ist. Ein Block darf selbst Kopfzeilen mit eigenen, noch weiter eingerückten Blöcken enthalten. Üblich sind vier Leerzeichen je Ebene; so empfiehlt es der Stilleitfaden für Python, PEP 8.
:::

::::beispiel
Zwei Anweisungen im Block:

```python temperatur_block.py
# Zwei Anweisungen hängen an derselben Bedingung
temp = float(input("Temperatur in Grad: "))
if temp > 23:
    zuviel = temp - 23
    print(f"Achtung: um {zuviel:.1f} Grad zu warm")
print("fertig")
```

```console Linux
$ python3 temperatur_block.py
Temperatur in Grad: 24.5
Achtung: um 1.5 Grad zu warm
fertig
```
::::

**Blöcke im interaktiven Modus.** Auch dort kann man einen Block eingeben. Nach der Kopfzeile zeigt Python statt `>>>` die Fortsetzung `...` ([Kapitel 1, Abschnitt 4.1](/wissen/informatik/programmieren/python/programme-und-der-python-interpreter/der-interaktive-modus.html#stufe-4-1)). Ab Python 3.13 rückt der interaktive Modus die nächste Zeile von selbst um vier Leerzeichen ein; du tippst nur noch die Anweisung. Eine leere Zeile beendet die Eingabe, erst dann läuft der Block. Hier enthält der Block eine zweite Kopfzeile mit einem eigenen, tiefer eingerückten Block:

```console
>>> temp = 24.5
>>> if temp > 20:
...     print("nicht zu kalt")
...     if temp > 23:
...         print("aber zu warm")
...
nicht zu kalt
aber zu warm
```

**Fehler in der Einrückung.** Ist eine Einrückung falsch, weist Python das ganze Skript schon beim Übersetzen zurück, wie bei jedem Syntaxfehler ([Kapitel 1, Abschnitt 6.1](/wissen/informatik/programmieren/python/programme-und-der-python-interpreter/fehler-lesen-und-verstehen.html#stufe-6-1)). Fehlt der Block nach einer Kopfzeile, lautet die Meldung:

```python einrueckung_fehlt.py
temp = 24.5
if temp > 23:
print("Achtung: zu warm")
```

```console Linux
$ python3 einrueckung_fehlt.py
  File "/home/student/python-kurs/einrueckung_fehlt.py", line 3
    print("Achtung: zu warm")
    ^^^^^
IndentationError: expected an indented block after 'if' statement on line 2
```

Rückt eine Zeile auf eine Tiefe zurück, die es vorher nicht gab, findet Python keinen Block, zu dem sie gehört:

```python einrueckung_uneben.py
temp = 24.5
if temp > 23:
    print("Achtung: zu warm")
  print("Bitte lüften")
```

```console Linux
$ python3 einrueckung_uneben.py
  File "/home/student/python-kurs/einrueckung_uneben.py", line 4
    print("Bitte lüften")
                         ^
IndentationError: unindent does not match any outer indentation level
```

Eine dritte Meldung, `TabError: inconsistent use of tabs and spaces in indentation`, erscheint, wenn eine Datei Tabulatoren und Leerzeichen so mischt, dass die Bedeutung von der Breite eines Tabulators abhinge. Gute Editoren setzen beim Druck auf die Tabulatortaste vier Leerzeichen; dann kann das nicht passieren.

⁠**Kurz gesagt:** Die Einrückung bestimmt, welche Zeilen zu einer Kopfzeile gehören; ein Block endet dort, wo eine Zeile wieder weiter links beginnt.

:::hintergrund Warum Python Blöcke durch Einrückung bildet
Viele Sprachen fassen einen Block mit Klammern zusammen, C zum Beispiel mit `{` und `}`. Ohne Klammern gehört in C nur die erste Anweisung zur Bedingung, gleich wie die Zeilen eingerückt sind. In

```c
if (temp > 23)
    fenster_auf = 1;
    heizung_aus();
```

läuft `heizung_aus();` deshalb immer, obwohl die Einrückung das Gegenteil behauptet. Wer den Code liest, sieht eine Gruppierung, der Compiler eine andere, und solche Fehler sind schwer zu finden. In Python kann das nicht passieren: Es gibt keine Klammern für Blöcke, also können Leser und Übersetzer die Gruppierung nicht verschieden sehen. Die Einrückung, die ein guter Programmierer ohnehin schreiben würde, ist selbst die Regel. Nebenbei entfällt der Streit darüber, wo die Klammern hingehören, und Programme werden kürzer.
:::

:::hintergrund Was der Übersetzer aus der Einrückung macht
Beim Zerlegen einer Datei in ihre Bestandteile verwandelt CPython die Einrückung in zwei unsichtbare Bestandteile, „Einrücken“ und „Ausrücken“, die genau die Rolle der Klammern in C spielen. Dafür führt es einen Stapel von Einrücktiefen, auf dem anfangs nur die 0 liegt. Ist eine neue Zeile tiefer eingerückt als die oberste Zahl auf dem Stapel, legt es ihre Tiefe obendrauf und erzeugt ein „Einrücken“. Ist sie weniger tief, nimmt es so lange Zahlen herunter und erzeugt je ein „Ausrücken“, bis die oberste Zahl gleich der neuen Tiefe ist. Gibt es diese Tiefe auf dem Stapel nicht, ist das genau der Fehler „unindent does not match any outer indentation level“. Ein Tabulator zählt beim Messen der Tiefe bis zum nächsten Vielfachen von 8. Weil andere Programme einen Tabulator oft vier Zeichen breit zeigen, lehnt Python Dateien ab, deren Bedeutung von dieser Breite abhinge; daher kommt der `TabError`.
:::

### Die Alternative `else`

<span class="anker" id="stufe-2-3"></span>

Das Skript soll nicht nur warnen, sondern im anderen Fall bestätigen, dass die Temperatur stimmt. Es gibt also zwei Wege, und genau einer davon soll laufen.

**Zwei Wege aus der Raute.** Im rechten Flussdiagramm von Abb. [1](#abb-1) führt jeder der beiden Pfeile zu einem eigenen Kasten, danach treffen sich die Wege wieder.

:::definition Definition 2.3 (`else`)
<span class="anker" id="satz-2-3"></span>

Auf den Block einer bedingten Anweisung darf eine Zeile `else:` folgen, genau so weit eingerückt wie das zugehörige `if`, und danach ein eigener Block. Er läuft genau dann, wenn die Bedingung falsch ist. Von den beiden Blöcken läuft also immer genau einer.
:::

::::beispiel
Das Skript aus Unterabschnitt [2.1](#stufe-2-1) mit einem zweiten Weg:

```python temperatur_else.py
# Temperatur prüfen: Warnung oder Bestätigung, genau eins von beiden
temp = float(input("Temperatur in Grad: "))
if temp > 23:
    print("Achtung: zu warm")
else:
    print("Temperatur in Ordnung")
print("fertig")
```

```console Windows (PowerShell)
PS> py temperatur_else.py
Temperatur in Grad: 22
Temperatur in Ordnung
fertig
```

`else` hat keine Bedingung, denn es ist genau der Fall, in dem die Bedingung des `if` nicht gilt.
::::

⁠**Kurz gesagt:** `else` gibt den Block an, der läuft, wenn die Bedingung falsch ist.

### Mehrere Fälle: `elif`

<span class="anker" id="stufe-2-4"></span>

Im Zimmer kann es zu kalt, in Ordnung oder zu warm sein. Für drei und mehr Fälle reicht ein einzelnes `else` nicht.

**Fragen nacheinander.** Man stellt die Fragen der Reihe nach, und die erste, die mit ja beantwortet wird, entscheidet (Abb. [3](#abb-3)). Was nach ihr kommt, wird gar nicht mehr gefragt.

:::abbildung prog/k3elif 3
Flussdiagramm von `if`, `elif` und `else`. Die Fragen werden von oben nach unten gestellt; die erste mit der Antwort ja wählt ihren Kasten, alle übrigen werden übersprungen. Ist keine Antwort ja, läuft der `else`-Kasten. Danach geht es an einer gemeinsamen Stelle weiter.
:::

:::definition Definition 2.4 (`elif`)
<span class="anker" id="satz-2-4"></span>

Zwischen dem Block eines `if` und einem möglichen `else` dürfen beliebig viele Zeilen `elif Bedingung:` mit je einem Block stehen, alle so weit eingerückt wie das `if`. `elif` ist eine Abkürzung von „else if“. Python prüft die Bedingungen von oben nach unten. Den Block der ersten Bedingung, die wahr ist, führt es aus und überspringt alle übrigen. Ist keine wahr, läuft der Block nach `else`, falls es eines gibt.
:::

::::beispiel
Die drei Fälle der Zimmertemperatur:

```python temperatur_elif.py
# Zimmertemperatur einordnen: gewünscht sind 20 bis 23 Grad
temp = float(input("Temperatur in Grad: "))
if temp < 20:
    print("zu kalt")
elif temp <= 23:
    print("in Ordnung")
else:
    print("zu warm")
```

```console Linux
$ python3 temperatur_elif.py
Temperatur in Grad: 18.5
zu kalt
$ python3 temperatur_elif.py
Temperatur in Grad: 21.5
in Ordnung
$ python3 temperatur_elif.py
Temperatur in Grad: 24.5
zu warm
```

Die zweite Bedingung prüft nur die obere Grenze. Das genügt, weil Python sie nur erreicht, wenn die erste falsch war, also wenn `temp` mindestens 20 ist. Die Reihenfolge der Fälle ist deshalb wichtig: Wer sie vertauscht, bekommt ein anderes Programm.
::::

Zwei Schreibfehler sind häufig. `else if` statt `elif` ergibt `SyntaxError: expected ':'`. Ein `elif` nach dem `else` ist ebenfalls ein Syntaxfehler; Python 3.14 sagt dazu ausdrücklich `'elif' block follows an 'else' block`, Python 3.13 nur `invalid syntax`.

⁠**Kurz gesagt:** Bei `if`, `elif` und `else` läuft genau der Block der ersten wahren Bedingung, sonst der `else`-Block.

:::hintergrund Eine Mehrfachauswahl nach festen Werten: `match`
Seit Python 3.10 gibt es eine weitere Schreibweise für den häufigen Fall, dass ein Wert mit einer Reihe fester Werte verglichen wird. Hinter `match` steht der Wert, hinter jedem `case` ein möglicher Wert; der Unterstrich `_` passt auf alles und übernimmt die Rolle von `else`:

```python einheit.py
# Einheitenzeichen erklären: Mehrfachauswahl mit match (seit Python 3.10)
zeichen = input("Einheitenzeichen: ")
match zeichen:
    case "m":
        print("Meter, die Einheit der Länge")
    case "s":
        print("Sekunde, die Einheit der Zeit")
    case "kg":
        print("Kilogramm, die Einheit der Masse")
    case _:
        print("unbekannt")
```

```console Linux
$ python3 einheit.py
Einheitenzeichen: s
Sekunde, die Einheit der Zeit
$ python3 einheit.py
Einheitenzeichen: x
unbekannt
```

Dasselbe leistet eine Kette `if zeichen == "m": … elif zeichen == "s": …`. Python prüft auch die `case`-Zeilen von oben nach unten, und es läuft nur der Block der ersten passenden. `match` kann noch viel mehr, etwa Werte auseinandernehmen; für Vergleiche mit Bereichen wie bei der Temperatur bleibt `elif` die übliche Form.
:::

### Typische Fehler in Bedingungen

<span class="anker" id="stufe-2-5"></span>

Die meisten Fehler in Entscheidungen haben eine der folgenden Ursachen.

<ul>

<li>

⁠**`=` statt `==`.** `if temp = 20:` ist eine Zuweisung an der Stelle einer Bedingung. Python meldet `SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?`.

</li>

<li>

⁠**Der Doppelpunkt fehlt.** `if temp > 23` ohne Doppelpunkt ergibt `SyntaxError: expected ':'`.

</li>

<li>

⁠**`or` mit einem einzelnen Wert.** `if einheit == "m" or "s":` fragt nicht, ob `einheit` einer der beiden Werte ist. Python liest `(einheit == "m") or "s"`, und `"s"` ist wahr:

```console
>>> einheit = "kg"
>>> einheit == "m" or "s"
's'
>>> einheit == "m" or einheit == "s"
False
```

</li>

<li>

⁠**Gleitkommazahlen mit `==`.** `if 0.1 + 0.2 == 0.3:` ist nie erfüllt; Gleitkommazahlen vergleicht man mit Toleranz ([Kapitel 2, Abschnitt 7.4](/wissen/informatik/programmieren/python/werte-typen-und-variablen/wahrheitswerte-und-vergleiche.html#stufe-7-4)).

</li>

<li>

⁠**Text statt Zahl.** Ohne Typumwandlung vergleicht `if eingabe < "9":` Text (Unterabschnitt [1.3](bedingungen-vergleiche-und-logische-operatoren.html#stufe-1-3)), und `if eingabe < 9:` bricht mit `TypeError` ab.

</li>

</ul>

⁠**Kurz gesagt:** `==` statt `=`, Doppelpunkt am Ende, jede Teilbedingung vollständig ausschreiben, Gleitkommazahlen mit Toleranz, Eingaben erst umwandeln.

### Anwendung: eine Waage mit Unter- und Überlauf

<span class="anker" id="stufe-2-6"></span>

Eine digitale Küchenwaage speichert jedes Gewicht als ganze Zahl, wie in der Aufgabe zur Küchenwaage in [Kapitel 2, Abschnitt 3](/wissen/informatik/programmieren/python/werte-typen-und-variablen/zahlen-im-binarsystem.html#stufe-3). Diese Zahl heißt hier der Rohwert. Eine Waage mit 12 Bit und dem Bereich 0 kg bis 5 kg teilt den Bereich in $2^{12}=4096$ gleiche Stufen von je $5\,\mathrm{kg}/4096=1{,}220703125$ g. Der Rohwert eines Gewichts $m$ ist die Zahl der vollen Stufen unter ihm, $\lfloor m/(1{,}220703125\,\mathrm{g})\rfloor$; der größte Rohwert ist 4095. Gewichte außerhalb des Bereichs kann die Waage nicht darstellen. Sie meldet einen Unterlauf, etwa wenn man sie mit einer Schüssel darauf auf null gestellt hat und die Schüssel dann abnimmt, oder einen Überlauf.

Die drei Fälle sind ein Fall für `if`, `elif` und `else`. Die Ganzzahlumwandlung `int` schneidet die Nachkommastellen ab ([Kapitel 2, Abschnitt 10.4](/wissen/informatik/programmieren/python/werte-typen-und-variablen/zeichenketten-eingabe-und-ausgabe.html#stufe-10-4)), das ist für positive Zahlen genau das Abrunden.

```python waage.py
# Küchenwaage mit 12 Bit und dem Bereich 0 kg bis 5 kg
gewicht = float(input("Gewicht in kg: "))
stufe = 5.0 / 4096                   # Gewicht je Stufe in kg
if gewicht < 0:
    print("Unterlauf: Rohwert 0")
elif gewicht >= 5.0:
    print("Überlauf: Rohwert 4095")
else:
    rohwert = int(gewicht / stufe)
    print(f"Rohwert {rohwert}, hexadezimal {rohwert:03x}")
```

```console Linux
$ python3 waage.py
Gewicht in kg: 2.5
Rohwert 2048, hexadezimal 800
$ python3 waage.py
Gewicht in kg: 1.0
Rohwert 819, hexadezimal 333
$ python3 waage.py
Gewicht in kg: 5.2
Überlauf: Rohwert 4095
$ python3 waage.py
Gewicht in kg: -0.1
Unterlauf: Rohwert 0
```

Das halbe Höchstgewicht 2,5 kg ergibt genau $2048=2^{11}$, hexadezimal `800`: Das oberste der 12 Bit ist gesetzt, alle anderen sind null. 1 kg entspricht $819{,}2$ Stufen, also dem Rohwert 819.

⁠**Kurz gesagt:** Drei sich ausschließende Bereiche einer Größe sind ein Fall für `if`, `elif` und `else`.

### Aufgaben zu Abschnitt [2](#stufe-2)

<span class="anker" id="stufe-2-7"></span>

:::aufgabe Aufgabe 6 ★ Ausgabe vorhersagen
<span class="anker" id="aufg-6"></span>

Ein Skript enthält diese Entscheidung:

```python
if temp > 20:
    print("in Ordnung")
elif temp > 23:
    print("zu warm")
else:
    print("zu kalt")
```

Was gibt es für `temp = 18.5`, `temp = 22.0` und `temp = 24.5` aus? Welcher Fall kann nie eintreten, und warum? Ändere die Reihenfolge so, dass alle drei Fälle richtig erkannt werden.

:::loesung
Für `temp = 18.5` ist die erste Bedingung falsch, die zweite auch, also läuft `else`: „zu kalt“. Für `temp = 22.0` ist die erste Bedingung wahr: „in Ordnung“. Für `temp = 24.5` ist die erste Bedingung ebenfalls wahr, denn $24{,}5>20$: „in Ordnung“, und das ist falsch. Der Fall „zu warm“ kann nie eintreten: Jede Temperatur über 23 ist auch über 20 und wird schon vom ersten Fall genommen; `elif` wird dann gar nicht mehr geprüft.

Richtig wird es, wenn die engere Bedingung zuerst kommt:

```python
if temp > 23:
    print("zu warm")
elif temp > 20:
    print("in Ordnung")
else:
    print("zu kalt")
```

Jetzt erreicht der zweite Fall nur noch Temperaturen bis 23 °C. Ebenso richtig ist die Reihenfolge von unten nach oben wie in `temperatur_elif.py`, mit `temp < 20` zuerst. Die beiden Fassungen unterscheiden sich nur an der Grenze 20: Hier gilt genau 20 °C als „zu kalt“, in `temperatur_elif.py` als „in Ordnung“.
:::
:::

:::aufgabe Aufgabe 7 ★★ Fehler suchen
<span class="anker" id="aufg-7"></span>

Das Skript `fehler_if.py` enthält drei Fehler:

```python fehler_if.py
temp = float(input("Temperatur in Grad: "))
if temp = 20.0
    print("genau 20 Grad")
else if temp > 20.0:
    print("mehr als 20 Grad")
```

Welchen Fehler meldet Python zuerst, und warum nur diesen einen? Behebe die Fehler einen nach dem anderen und notiere jedes Mal die nächste Meldung. Warum ist `temp == 20.0` für eine gemessene Temperatur trotzdem keine gute Bedingung?

:::loesung
Python übersetzt die ganze Datei, bevor es eine Zeile ausführt, und hört beim ersten Syntaxfehler auf ([Kapitel 1, Abschnitt 6.1](/wissen/informatik/programmieren/python/programme-und-der-python-interpreter/fehler-lesen-und-verstehen.html#stufe-6-1)). Deshalb erscheint immer nur eine Meldung, und es läuft keine Zeile, auch nicht das `input` in Zeile 1:

```console Linux
$ python3 fehler_if.py
  File "/home/student/python-kurs/fehler_if.py", line 2
    if temp = 20.0
       ^^^^^^^^^^^
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
```

Mit `if temp == 20.0` (Datei `fehler_if2.py`) kommt der nächste Fehler, der fehlende Doppelpunkt:

```console Linux
$ python3 fehler_if2.py
  File "/home/student/python-kurs/fehler_if2.py", line 2
    if temp == 20.0
                   ^
SyntaxError: expected ':'
```

Mit Doppelpunkt (`fehler_if3.py`) bleibt `else if`. Python liest `else` und erwartet danach sofort den Doppelpunkt:

```console Linux
$ python3 fehler_if3.py
  File "/home/student/python-kurs/fehler_if3.py", line 4
    else if temp > 20.0:
         ^^
SyntaxError: expected ':'
```

Mit `elif` läuft das Skript:

```python fehler_if_ok.py
temp = float(input("Temperatur in Grad: "))
if temp == 20.0:
    print("genau 20 Grad")
elif temp > 20.0:
    print("mehr als 20 Grad")
```

```console Linux
$ python3 fehler_if_ok.py
Temperatur in Grad: 20.0
genau 20 Grad
$ python3 fehler_if_ok.py
Temperatur in Grad: 20.000001
mehr als 20 Grad
```

Für eine Messung ist `temp == 20.0` trotzdem keine gute Bedingung. Ein Thermometer liefert fast nie genau 20,000000, und ein Ergebnis, das gerechnet wurde, trägt Rundungsfehler ([Kapitel 2, Abschnitt 7.3](/wissen/informatik/programmieren/python/werte-typen-und-variablen/wahrheitswerte-und-vergleiche.html#stufe-7-3)). Sinnvoll ist ein Vergleich mit Toleranz, etwa `abs(temp - 20.0) <= 0.1` oder `math.isclose(temp, 20.0, abs_tol=0.1)`. Für 20,000001 zeigt die zweite Ausgabe, wie knapp eine Messung an der Gleichheit vorbeigehen kann.
:::
:::

:::aufgabe Aufgabe 8 ★★ Das Ergebnis einer Klausur
<span class="anker" id="aufg-8"></span>

Schreibe ein Skript `klausur.py`, das die Punktzahl einer Klausur mit höchstens 100 Punkten abfragt und ausgibt: unter 50 Punkten „nicht bestanden“, unter 85 „bestanden“, bis einschließlich 100 „mit Auszeichnung“, darüber „ungültig“. Teste es mit 49,5, 50, 70 und 101 Punkten.

:::loesung
Die Fälle werden von unten nach oben abgegrenzt; jede Bedingung braucht nur die obere Grenze, weil Python sie nur erreicht, wenn die vorige falsch war.

```python klausur.py
# Ergebnis einer Klausur aus der Punktzahl (0 bis 100)
punkte = float(input("Punkte: "))
if punkte < 50:
    print("nicht bestanden")
elif punkte < 85:
    print("bestanden")
elif punkte <= 100:
    print("mit Auszeichnung")
else:
    print("ungültig")
```

```console Linux
$ python3 klausur.py
Punkte: 49.5
nicht bestanden
$ python3 klausur.py
Punkte: 50
bestanden
$ python3 klausur.py
Punkte: 70
bestanden
$ python3 klausur.py
Punkte: 101
ungültig
```

Der Test mit genau 50 Punkten prüft die Grenze: „unter 50“ ist dort falsch, also gilt „bestanden“.
:::
:::

:::aufgabe Aufgabe 9 ★★ Schaltjahre
<span class="anker" id="aufg-9"></span>

Ein Jahr ist ein Schaltjahr, wenn es durch 4 teilbar ist, außer es ist durch 100 teilbar; durch 400 teilbare Jahre sind aber wieder Schaltjahre.

<ol class="al">

<li>

Schreibe die Regel als einen einzigen Ausdruck mit `%`, `and` und `or` und prüfe ihn für 2024, 2026, 1900 und 2000.

</li>

<li>

Schreibe ein Skript `schaltjahr.py`, das dieselbe Entscheidung mit `if`, `elif` und `else` trifft, eine Bedingung je Zeile.

</li>

</ol>

:::loesung
(a) Die Regel lautet „durch 4 teilbar und nicht durch 100, oder durch 400“. Weil `and` stärker bindet als `or`, braucht der Ausdruck keine Klammern:

```console
>>> jahr = 2024
>>> jahr % 4 == 0 and jahr % 100 != 0 or jahr % 400 == 0
True
>>> jahr = 2026
>>> jahr % 4 == 0 and jahr % 100 != 0 or jahr % 400 == 0
False
>>> jahr = 1900
>>> jahr % 4 == 0 and jahr % 100 != 0 or jahr % 400 == 0
False
>>> jahr = 2000
>>> jahr % 4 == 0 and jahr % 100 != 0 or jahr % 400 == 0
True
```

(b) Mit `elif` prüft man die stärkste Regel zuerst, dann die Ausnahme, dann die Grundregel:

```python schaltjahr.py
# Schaltjahr nach dem gregorianischen Kalender, eine Bedingung je Zeile
jahr = int(input("Jahr: "))
if jahr % 400 == 0:
    print(jahr, "ist ein Schaltjahr")
elif jahr % 100 == 0:
    print(jahr, "ist kein Schaltjahr")
elif jahr % 4 == 0:
    print(jahr, "ist ein Schaltjahr")
else:
    print(jahr, "ist kein Schaltjahr")
```

```console Linux
$ python3 schaltjahr.py
Jahr: 1900
1900 ist kein Schaltjahr
$ python3 schaltjahr.py
Jahr: 2000
2000 ist ein Schaltjahr
```

Die Reihenfolge ist entscheidend: Käme `jahr % 4 == 0` zuerst, wäre 1900 ein Schaltjahr.
:::
:::

---
title: Entscheidungen: if, elif und else
pfad: Informatik / Programmieren / Python / Entscheidungen und Schleifen
knoten: Python 3: Entscheidungen und Schleifen
order: 6040300
summary: Mit einer Bedingung allein passiert noch nichts; ein Skript läuft weiterhin Zeile für Zeile von oben nach unten (Programmieren, Python 1, Abschnitt 5.2).
tags: bedingte Anweisung, Kopfzeile, Block
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Mit einer Bedingung allein passiert noch nichts; ein Skript läuft weiterhin Zeile für Zeile von oben nach unten ([Programmieren, Python 1, Abschnitt 5.2](/wissen/informatik/programmieren/python/programme-und-der-python-interpreter/skripte-schreiben-und-ausfuhren.html#stufe-5-2)). Dieser Abschnitt zeigt, wie ein Skript Zeilen nur ausführt, wenn eine Bedingung erfüllt ist, wie Python erkennt, welche Zeilen dazugehören, und wie man zwischen mehreren Fällen wählt.
:::

### Die bedingte Anweisung `if`

<span class="anker" id="stufe-2-1"></span>

Ein Skript misst die Spannung an einem USB-Anschluss. Eine Warnung soll es nur ausgeben, wenn die Spannung über 5,25 V liegt.

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

**Beispiel.** Das Skript fragt die Spannung ab und prüft sie:

```python usb_if.py
# Spannung an einem USB-Anschluss prüfen: erlaubt sind höchstens 5,25 V
u = float(input("Spannung in V: "))
if u > 5.25:
    print("Achtung: Spannung zu hoch")
print("Messung beendet")
```

Zweimal gestartet, einmal mit 5,4 V und einmal mit 5,0 V:

```console Linux
$ python3 usb_if.py
Spannung in V: 5.4
Achtung: Spannung zu hoch
Messung beendet
$ python3 usb_if.py
Spannung in V: 5.0
Messung beendet
```

```console Windows (PowerShell)
PS> py usb_if.py
Spannung in V: 5.4
Achtung: Spannung zu hoch
Messung beendet
```

Die letzte Zeile des Skripts läuft in beiden Fällen, denn sie gehört nicht mehr zur Bedingung.

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

**Beispiel.** Zwei Anweisungen im Block:

```python usb_block.py
# Zwei Anweisungen hängen an derselben Bedingung
u = float(input("Spannung in V: "))
if u > 5.25:
    zuviel = u - 5.25
    print(f"Achtung: Spannung um {zuviel:.2f} V zu hoch")
print("Messung beendet")
```

```console Linux
$ python3 usb_block.py
Spannung in V: 5.4
Achtung: Spannung um 0.15 V zu hoch
Messung beendet
```

**Blöcke im interaktiven Modus.** Auch dort kann man einen Block eingeben. Nach der Kopfzeile zeigt Python statt `>>>` die Fortsetzung `...` ([Programmieren, Python 1, Abschnitt 4.1](/wissen/informatik/programmieren/python/programme-und-der-python-interpreter/der-interaktive-modus.html#stufe-4-1)). Ab Python 3.13 rückt der interaktive Modus die nächste Zeile von selbst um vier Leerzeichen ein; du tippst nur noch die Anweisung. Eine leere Zeile beendet die Eingabe, erst dann läuft der Block. Hier enthält der Block eine zweite Kopfzeile mit einem eigenen, tiefer eingerückten Block:

```console
>>> u = 5.4
>>> if u > 4.75:
...     print("Spannung vorhanden")
...     if u > 5.25:
...         print("aber zu hoch")
...
Spannung vorhanden
aber zu hoch
```

**Fehler in der Einrückung.** Ist eine Einrückung falsch, weist Python das ganze Skript schon beim Übersetzen zurück, wie bei jedem Syntaxfehler ([Programmieren, Python 1, Abschnitt 6.1](/wissen/informatik/programmieren/python/programme-und-der-python-interpreter/fehler-lesen-und-verstehen.html#stufe-6-1)). Fehlt der Block nach einer Kopfzeile, lautet die Meldung:

```python einrueckung_fehlt.py
u = 5.4
if u > 5.25:
print("Achtung: Spannung zu hoch")
```

```console Linux
$ python3 einrueckung_fehlt.py
  File "/home/student/python-kurs/einrueckung_fehlt.py", line 3
    print("Achtung: Spannung zu hoch")
    ^^^^^
IndentationError: expected an indented block after 'if' statement on line 2
```

Rückt eine Zeile auf eine Tiefe zurück, die es vorher nicht gab, findet Python keinen Block, zu dem sie gehört:

```python einrueckung_uneben.py
u = 5.4
if u > 5.25:
    print("Achtung: Spannung zu hoch")
  print("Bitte das Netzteil prüfen")
```

```console Linux
$ python3 einrueckung_uneben.py
  File "/home/student/python-kurs/einrueckung_uneben.py", line 4
    print("Bitte das Netzteil prüfen")
                                      ^
IndentationError: unindent does not match any outer indentation level
```

Eine dritte Meldung, `TabError: inconsistent use of tabs and spaces in indentation`, erscheint, wenn eine Datei Tabulatoren und Leerzeichen so mischt, dass die Bedeutung von der Breite eines Tabulators abhinge. Gute Editoren setzen beim Druck auf die Tabulatortaste vier Leerzeichen; dann kann das nicht passieren.

⁠**Kurz gesagt:** Die Einrückung bestimmt, welche Zeilen zu einer Kopfzeile gehören; ein Block endet dort, wo eine Zeile wieder weiter links beginnt.

:::hintergrund Warum Python Blöcke durch Einrückung bildet
Viele Sprachen fassen einen Block mit Klammern zusammen, C zum Beispiel mit `{` und `}`. Ohne Klammern gehört in C nur die erste Anweisung zur Bedingung, gleich wie die Zeilen eingerückt sind. In

```c
if (u > 5.25)
    led_rot = 1;
    abschalten();
```

läuft `abschalten();` deshalb immer, obwohl die Einrückung das Gegenteil behauptet. Wer den Code liest, sieht eine Gruppierung, der Compiler eine andere, und solche Fehler sind schwer zu finden. In Python kann das nicht passieren: Es gibt keine Klammern für Blöcke, also können Leser und Übersetzer die Gruppierung nicht verschieden sehen. Die Einrückung, die ein guter Programmierer ohnehin schreiben würde, ist selbst die Regel. Nebenbei entfällt der Streit darüber, wo die Klammern hingehören, und Programme werden kürzer.
:::

:::hintergrund Was der Übersetzer aus der Einrückung macht
Beim Zerlegen einer Datei in ihre Bestandteile verwandelt CPython die Einrückung in zwei unsichtbare Bestandteile, „Einrücken“ und „Ausrücken“, die genau die Rolle der Klammern in C spielen. Dafür führt es einen Stapel von Einrücktiefen, auf dem anfangs nur die 0 liegt. Ist eine neue Zeile tiefer eingerückt als die oberste Zahl auf dem Stapel, legt es ihre Tiefe obendrauf und erzeugt ein „Einrücken“. Ist sie weniger tief, nimmt es so lange Zahlen herunter und erzeugt je ein „Ausrücken“, bis die oberste Zahl gleich der neuen Tiefe ist. Gibt es diese Tiefe auf dem Stapel nicht, ist das genau der Fehler „unindent does not match any outer indentation level“. Ein Tabulator zählt beim Messen der Tiefe bis zum nächsten Vielfachen von 8. Weil andere Programme einen Tabulator oft vier Zeichen breit zeigen, lehnt Python Dateien ab, deren Bedeutung von dieser Breite abhinge; daher kommt der `TabError`.
:::

### Die Alternative `else`

<span class="anker" id="stufe-2-3"></span>

Das Skript soll nicht nur warnen, sondern im anderen Fall bestätigen, dass die Spannung stimmt. Es gibt also zwei Wege, und genau einer davon soll laufen.

**Zwei Wege aus der Raute.** Im rechten Flussdiagramm von Abb. [1](#abb-1) führt jeder der beiden Pfeile zu einem eigenen Kasten, danach treffen sich die Wege wieder.

:::definition Definition 2.3 (`else`)
<span class="anker" id="satz-2-3"></span>

Auf den Block einer bedingten Anweisung darf eine Zeile `else:` folgen, genau so weit eingerückt wie das zugehörige `if`, und danach ein eigener Block. Er läuft genau dann, wenn die Bedingung falsch ist. Von den beiden Blöcken läuft also immer genau einer.
:::

**Beispiel.** Das Skript aus Unterabschnitt [2.1](#stufe-2-1) mit einem zweiten Weg:

```python usb_else.py
# Spannung prüfen: Warnung oder Bestätigung, genau eins von beiden
u = float(input("Spannung in V: "))
if u > 5.25:
    print("Achtung: Spannung zu hoch")
else:
    print("Spannung in Ordnung")
print("Messung beendet")
```

```console Windows (PowerShell)
PS> py usb_else.py
Spannung in V: 5.0
Spannung in Ordnung
Messung beendet
```

`else` hat keine Bedingung, denn es ist genau der Fall, in dem die Bedingung des `if` nicht gilt.

⁠**Kurz gesagt:** `else` gibt den Block an, der läuft, wenn die Bedingung falsch ist.

### Mehrere Fälle: `elif`

<span class="anker" id="stufe-2-4"></span>

Eine Spannung kann zu niedrig, in Ordnung oder zu hoch sein. Für drei und mehr Fälle reicht ein einzelnes `else` nicht.

**Fragen nacheinander.** Man stellt die Fragen der Reihe nach, und die erste, die mit ja beantwortet wird, entscheidet (Abb. [3](#abb-3)). Was nach ihr kommt, wird gar nicht mehr gefragt.

:::abbildung prog/k3elif 3
Flussdiagramm von `if`, `elif` und `else`. Die Fragen werden von oben nach unten gestellt; die erste mit der Antwort ja wählt ihren Kasten, alle übrigen werden übersprungen. Ist keine Antwort ja, läuft der `else`-Kasten. Danach geht es an einer gemeinsamen Stelle weiter.
:::

:::definition Definition 2.4 (`elif`)
<span class="anker" id="satz-2-4"></span>

Zwischen dem Block eines `if` und einem möglichen `else` dürfen beliebig viele Zeilen `elif Bedingung:` mit je einem Block stehen, alle so weit eingerückt wie das `if`. `elif` ist eine Abkürzung von „else if“. Python prüft die Bedingungen von oben nach unten. Den Block der ersten Bedingung, die wahr ist, führt es aus und überspringt alle übrigen. Ist keine wahr, läuft der Block nach `else`, falls es eines gibt.
:::

**Beispiel.** Die drei Fälle der USB-Spannung:

```python usb_elif.py
# Spannung eines USB-Anschlusses einordnen: erlaubt sind 4,75 V bis 5,25 V
u = float(input("Spannung in V: "))
if u < 4.75:
    print("zu niedrig")
elif u <= 5.25:
    print("in Ordnung")
else:
    print("zu hoch")
```

```console Linux
$ python3 usb_elif.py
Spannung in V: 4.5
zu niedrig
$ python3 usb_elif.py
Spannung in V: 5.1
in Ordnung
$ python3 usb_elif.py
Spannung in V: 5.4
zu hoch
```

Die zweite Bedingung prüft nur die obere Grenze. Das genügt, weil Python sie nur erreicht, wenn die erste falsch war, also wenn `u` mindestens 4,75 ist. Die Reihenfolge der Fälle ist deshalb wichtig: Wer sie vertauscht, bekommt ein anderes Programm.

Zwei Schreibfehler sind häufig. `else if` statt `elif` ergibt `SyntaxError: expected ':'`. Ein `elif` nach dem `else` ist ebenfalls ein Syntaxfehler; Python 3.14 sagt dazu ausdrücklich `'elif' block follows an 'else' block`, Python 3.13 nur `invalid syntax`.

⁠**Kurz gesagt:** Bei `if`, `elif` und `else` läuft genau der Block der ersten wahren Bedingung, sonst der `else`-Block.

:::hintergrund Eine Mehrfachauswahl nach festen Werten: `match`
Seit Python 3.10 gibt es eine weitere Schreibweise für den häufigen Fall, dass ein Wert mit einer Reihe fester Werte verglichen wird. Hinter `match` steht der Wert, hinter jedem `case` ein möglicher Wert; der Unterstrich `_` passt auf alles und übernimmt die Rolle von `else`:

```python einheit.py
# Einheitenzeichen erklären: Mehrfachauswahl mit match (seit Python 3.10)
zeichen = input("Einheitenzeichen: ")
match zeichen:
    case "V":
        print("Volt, die Einheit der Spannung")
    case "A":
        print("Ampere, die Einheit der Stromstärke")
    case "Ohm":
        print("Ohm, die Einheit des Widerstands")
    case _:
        print("unbekannt")
```

```console Linux
$ python3 einheit.py
Einheitenzeichen: A
Ampere, die Einheit der Stromstärke
$ python3 einheit.py
Einheitenzeichen: W
unbekannt
```

Dasselbe leistet eine Kette `if zeichen == "V": … elif zeichen == "A": …`. Python prüft auch die `case`-Zeilen von oben nach unten, und es läuft nur der Block der ersten passenden. `match` kann noch viel mehr, etwa Werte auseinandernehmen; für Vergleiche mit Bereichen wie bei der Spannung bleibt `elif` die übliche Form.
:::

### Typische Fehler in Bedingungen

<span class="anker" id="stufe-2-5"></span>

Die meisten Fehler in Entscheidungen haben eine der folgenden Ursachen.

<ul>

<li>

⁠**`=` statt `==`.** `if u = 5:` ist eine Zuweisung an der Stelle einer Bedingung. Python meldet `SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?`.

</li>

<li>

⁠**Der Doppelpunkt fehlt.** `if u > 5.25` ohne Doppelpunkt ergibt `SyntaxError: expected ':'`.

</li>

<li>

⁠**`or` mit einem einzelnen Wert.** `if einheit == "V" or "A":` fragt nicht, ob `einheit` einer der beiden Werte ist. Python liest `(einheit == "V") or "A"`, und `"A"` ist wahr:

```console
>>> einheit = "Ohm"
>>> einheit == "V" or "A"
'A'
>>> einheit == "V" or einheit == "A"
False
```

</li>

<li>

⁠**Gleitkommazahlen mit `==`.** `if 0.1 + 0.2 == 0.3:` ist nie erfüllt; Gleitkommazahlen vergleicht man mit Toleranz ([Programmieren, Python 2, Abschnitt 7.4](/wissen/informatik/programmieren/python/werte-typen-und-variablen/wahrheitswerte-und-vergleiche.html#stufe-7-4)).

</li>

<li>

⁠**Text statt Zahl.** Ohne Typumwandlung vergleicht `if eingabe < "9":` Text (Unterabschnitt [1.3](bedingungen-vergleiche-und-logische-operatoren.html#stufe-1-3)), und `if eingabe < 9:` bricht mit `TypeError` ab.

</li>

</ul>

⁠**Kurz gesagt:** `==` statt `=`, Doppelpunkt am Ende, jede Teilbedingung vollständig ausschreiben, Gleitkommazahlen mit Toleranz, Eingaben erst umwandeln.

### Anwendung: ein Messbereich mit Unter- und Überlauf

<span class="anker" id="stufe-2-6"></span>

Ein Analog-Digital-Umsetzer (ADU) wandelt eine Spannung in eine ganze Zahl. Diese Zahl heißt der Code. Ein ADU mit 12 Bit und dem Messbereich 0 V bis 5 V teilt den Bereich in $2^{12}=4096$ gleiche Stufen von je $5\,\mathrm V/4096=1{,}220703125$ mV. Der Code einer Spannung $U$ ist die Zahl der vollen Stufen unter ihr, $\lfloor U/(1{,}220703125\,\mathrm{mV})\rfloor$; der größte Code ist 4095. Spannungen außerhalb des Bereichs kann der Umsetzer nicht darstellen: Er meldet einen Unterlauf oder einen Überlauf.

Die drei Fälle sind ein Fall für `if`, `elif` und `else`. Die Ganzzahlumwandlung `int` schneidet die Nachkommastellen ab ([Programmieren, Python 2, Abschnitt 10.4](/wissen/informatik/programmieren/python/werte-typen-und-variablen/zeichenketten-eingabe-und-ausgabe.html#stufe-10-4)), das ist für positive Zahlen genau das Abrunden.

```python adu.py
# 12-Bit-Analog-Digital-Umsetzer mit dem Messbereich 0 V bis 5 V
u = float(input("Spannung in V: "))
stufe = 5.0 / 4096                   # Spannung je Stufe in V
if u < 0:
    print("Unterlauf: Code 0")
elif u >= 5.0:
    print("Überlauf: Code 4095")
else:
    code = int(u / stufe)
    print(f"Code {code}, hexadezimal {code:03x}")
```

```console Linux
$ python3 adu.py
Spannung in V: 2.5
Code 2048, hexadezimal 800
$ python3 adu.py
Spannung in V: 1.0
Code 819, hexadezimal 333
$ python3 adu.py
Spannung in V: 5.2
Überlauf: Code 4095
$ python3 adu.py
Spannung in V: -0.1
Unterlauf: Code 0
```

Die halbe Vollaussteuerung 2,5 V ergibt genau $2048=2^{11}$, hexadezimal `800`: Das oberste der 12 Bit ist gesetzt, alle anderen sind null. 1 V entspricht $819{,}2$ Stufen, also dem Code 819.

⁠**Kurz gesagt:** Drei sich ausschließende Bereiche einer Messgröße sind ein Fall für `if`, `elif` und `else`.

### Aufgaben zu Abschnitt [2](#stufe-2)

<span class="anker" id="stufe-2-7"></span>

:::aufgabe Aufgabe 6 ★ Ausgabe vorhersagen
<span class="anker" id="aufg-6"></span>

Ein Skript enthält diese Entscheidung:

```python
if u > 4.75:
    print("in Ordnung")
elif u > 5.25:
    print("zu hoch")
else:
    print("zu niedrig")
```

Was gibt es für $u=4{,}5$, $u=5{,}0$ und $u=5{,}4$ aus? Welcher Fall kann nie eintreten, und warum? Ändere die Reihenfolge so, dass alle drei Fälle richtig erkannt werden.

:::loesung
Für $u=4{,}5$ ist die erste Bedingung falsch, die zweite auch, also läuft `else`: „zu niedrig“. Für $u=5{,}0$ ist die erste Bedingung wahr: „in Ordnung“. Für $u=5{,}4$ ist die erste Bedingung ebenfalls wahr, denn $5{,}4>4{,}75$: „in Ordnung“, und das ist falsch. Der Fall „zu hoch“ kann nie eintreten: Jede Spannung über 5,25 ist auch über 4,75 und wird schon vom ersten Fall genommen; `elif` wird dann gar nicht mehr geprüft.

Richtig wird es, wenn die engere Bedingung zuerst kommt:

```python
if u > 5.25:
    print("zu hoch")
elif u > 4.75:
    print("in Ordnung")
else:
    print("zu niedrig")
```

Jetzt erreicht der zweite Fall nur noch Spannungen bis 5,25 V. Ebenso richtig ist die Reihenfolge von unten nach oben wie in `usb_elif.py`, mit `u < 4.75` zuerst.
:::
:::

:::aufgabe Aufgabe 7 ★★ Fehler suchen
<span class="anker" id="aufg-7"></span>

Das Skript `fehler_if.py` enthält drei Fehler:

```python fehler_if.py
u = float(input("Spannung in V: "))
if u = 5.0
    print("genau 5 V")
else if u > 5.0:
    print("mehr als 5 V")
```

Welchen Fehler meldet Python zuerst, und warum nur diesen einen? Behebe die Fehler einen nach dem anderen und notiere jedes Mal die nächste Meldung. Warum ist `u == 5.0` für eine gemessene Spannung trotzdem keine gute Bedingung?

:::loesung
Python übersetzt die ganze Datei, bevor es eine Zeile ausführt, und hört beim ersten Syntaxfehler auf ([Programmieren, Python 1, Abschnitt 6.1](/wissen/informatik/programmieren/python/programme-und-der-python-interpreter/fehler-lesen-und-verstehen.html#stufe-6-1)). Deshalb erscheint immer nur eine Meldung, und es läuft keine Zeile, auch nicht das `input` in Zeile 1:

```console Linux
$ python3 fehler_if.py
  File "/home/student/python-kurs/fehler_if.py", line 2
    if u = 5.0
       ^^^^^^^
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
```

Mit `if u == 5.0` (Datei `fehler_if2.py`) kommt der nächste Fehler, der fehlende Doppelpunkt:

```console Linux
$ python3 fehler_if2.py
  File "/home/student/python-kurs/fehler_if2.py", line 2
    if u == 5.0
               ^
SyntaxError: expected ':'
```

Mit Doppelpunkt (`fehler_if3.py`) bleibt `else if`. Python liest `else` und erwartet danach sofort den Doppelpunkt:

```console Linux
$ python3 fehler_if3.py
  File "/home/student/python-kurs/fehler_if3.py", line 4
    else if u > 5.0:
         ^^
SyntaxError: expected ':'
```

Mit `elif` läuft das Skript:

```python fehler_if_ok.py
u = float(input("Spannung in V: "))
if u == 5.0:
    print("genau 5 V")
elif u > 5.0:
    print("mehr als 5 V")
```

```console Linux
$ python3 fehler_if_ok.py
Spannung in V: 5.0
genau 5 V
$ python3 fehler_if_ok.py
Spannung in V: 5.000001
mehr als 5 V
```

Für eine Messung ist `u == 5.0` trotzdem keine gute Bedingung. Ein Messgerät liefert fast nie genau 5,000000, und ein Ergebnis, das gerechnet wurde, trägt Rundungsfehler ([Programmieren, Python 2, Abschnitt 7.3](/wissen/informatik/programmieren/python/werte-typen-und-variablen/wahrheitswerte-und-vergleiche.html#stufe-7-3)). Sinnvoll ist ein Vergleich mit Toleranz, etwa `abs(u - 5.0) <= 0.01` oder `math.isclose(u, 5.0, abs_tol=0.01)`. Für 5,000001 zeigt die zweite Ausgabe, wie knapp eine Messung an der Gleichheit vorbeigehen kann.
:::
:::

:::aufgabe Aufgabe 8 ★★ Ladezustand einer Akkuzelle
<span class="anker" id="aufg-8"></span>

Schreibe ein Skript `akku.py`, das die Spannung einer Lithium-Ionen-Zelle abfragt und ausgibt: unter 3,0 V „leer“, unter 3,6 V „schwach“, bis einschließlich 4,2 V „gut“, darüber „überladen“. Teste es mit 2,9 V, 3,0 V, 3,7 V und 4,3 V.

:::loesung
Die Fälle werden von unten nach oben abgegrenzt; jede Bedingung braucht nur die obere Grenze, weil Python sie nur erreicht, wenn die vorige falsch war.

```python akku.py
# Ladezustand einer Lithium-Ionen-Zelle aus ihrer Spannung
u = float(input("Zellspannung in V: "))
if u < 3.0:
    print("leer")
elif u < 3.6:
    print("schwach")
elif u <= 4.2:
    print("gut")
else:
    print("überladen")
```

```console Linux
$ python3 akku.py
Zellspannung in V: 2.9
leer
$ python3 akku.py
Zellspannung in V: 3.0
schwach
$ python3 akku.py
Zellspannung in V: 3.7
gut
$ python3 akku.py
Zellspannung in V: 4.3
überladen
```

Der Test mit genau 3,0 V prüft die Grenze: „unter 3,0 V“ ist dort falsch, also gilt „schwach“.
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

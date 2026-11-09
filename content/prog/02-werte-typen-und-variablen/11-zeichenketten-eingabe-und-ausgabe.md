---
title: Zeichenketten, Eingabe und Ausgabe
pfad: Informatik / Programmieren / Python / Werte, Typen und Variablen
knoten: Python 2: Werte, Typen und Variablen
order: 6031100
summary: Ein Programm soll nach Werten fragen und Ergebnisse ordentlich formatiert ausgeben.
tags: Verketten, f-String, Typumwandlung
lang: de
---

<span class="anker" id="stufe-10"></span>

:::zweck
Ein Programm soll nach Werten fragen und Ergebnisse ordentlich formatiert ausgeben. Dieser Abschnitt zeigt, wie man mit Zeichenketten rechnet, Zahlen formatiert in Text einsetzt, Eingaben liest, Text und Zahlen ineinander umwandelt und rundet. Zum Schluss entsteht ein kleiner Einheitenrechner.
:::

### Zeichenketten verketten und vervielfachen

<span class="anker" id="stufe-10-1"></span>

Python 1 hat die Zeichenkette als Wert aus Text eingeführt ([Programmieren, Python 1, Abschnitt 4.6](/wissen/informatik/programmieren/python/programme-und-der-python-interpreter/der-interaktive-modus.html#stufe-4-6)); ihr Typ heißt `str`. Auch mit Text kann man einiges rechnen: Teile zusammensetzen, Linien aus Strichen bauen, die Länge bestimmen.

:::definition Definition 10.1 (Operatoren und Länge von Zeichenketten)
<span class="anker" id="satz-10-1"></span>

Für Zeichenketten bedeutet `+` Aneinanderhängen, das __Verketten__: `"Ohm" + "meter"` ist `"Ohmmeter"`. `*` mit einem `int` wiederholt die Zeichenkette. Die eingebaute Funktion `len` liefert die Zahl der Zeichen.
:::

::::beispiel
Verketten, wiederholen, zählen:

```console
>>> "Ohm" + "meter"
'Ohmmeter'
>>> "Ohm" * 3
'OhmOhmOhm'
>>> "-" * 20
'--------------------'
>>> len("Ohm")
3
>>> len("Größe")
5
>>> len("")
0
>>> "4" + "2"
'42'
```

`""` ist die leere Zeichenkette, mit null Zeichen. `"4" + "2"` ergibt den Text `'42'`, nicht die Zahl 6: Für `str` bedeutet `+` Verketten, egal, was in der Zeichenkette steht.
::::

⁠**Kurz gesagt:** Bei Zeichenketten verkettet `+`, `*` wiederholt, und `len` zählt die Zeichen.

### Der f-String

<span class="anker" id="stufe-10-2"></span>

`print("Strom in mA:", strom * 1000)` druckt 17 Stellen, wo zwei genügen. Für eine ordentliche Ausgabe will man Zahlen mitten in einen Text setzen und dabei bestimmen, wie viele Stellen erscheinen.

**Ein Formular mit Lücken.** Man schreibt den Text einmal hin und lässt Lücken; in jede Lücke kommt ein ausgerechneter Wert, in der gewünschten Form.

:::definition Definition 10.2 (f-String)
<span class="anker" id="satz-10-2"></span>

Ein __f-String__ ist eine Zeichenkette mit einem `f` vor dem ersten Anführungszeichen. Jeder Ausdruck in geschweiften Klammern `{...}` wird ausgewertet, und sein Wert wird als Text an diese Stelle gesetzt.
:::

Hinter dem Ausdruck kann, durch einen Doppelpunkt getrennt, eine Formatangabe stehen. Sie legt fest, wie der Wert als Text erscheint:

| Formatangabe | Bedeutung | Beispiel und Ergebnis |
|---|---|---|
| `.2f` | 2 Nachkommastellen | `f"{3.14159:.2f}"` ergibt `3.14` |
| `.3e` | wissenschaftlich | `f"{0.0125:.3e}"` ergibt `1.250e-02` |
| `8.3f` | mindestens 8 Zeichen breit | `f"{3.14159:8.3f}"` ergibt ` 3.142` |
| `5d` | ganze Zahl, 5 Zeichen breit | `f"{42:5d}"` ergibt ` 42` |
| `,.2f` | mit Tausendertrennung | `f"{1234567.891:,.2f}"` ergibt `1,234,567.89` |
| `.1%` | als Prozent | `f"{0.256:.1%}"` ergibt `25.6%` |
| `08b` | binär mit 8 Stellen | `f"{19:08b}"` ergibt `00010011` |
| `x` | hexadezimal | `f"{255:x}"` ergibt `ff` |

Steht hinter dem Ausdruck ein Gleichheitszeichen, `f"{U=}"`, setzt Python den Ausdruck selbst, ein `=` und den Wert ein; das ist praktisch zum Nachsehen von Zwischenwerten. Die Formatangaben sind dieselben wie bei der Funktion `format` aus Unterabschnitt [3.4](zahlen-im-binarsystem.html#stufe-3-4). Wie in allen Python-Ausgaben steht der Dezimalpunkt als Punkt und die Tausendertrennung als Komma.

::::beispiel
Eine Messzeile mit Spannung, Strom, Widerstand und Leistung:

```console
>>> U = 3.3
>>> I = 0.0125
>>> f"U = {U} V, I = {I * 1000:.1f} mA"
'U = 3.3 V, I = 12.5 mA'
>>> f"R = {U / I:.1f} Ohm, P = {U * I:.3e} W"
'R = 264.0 Ohm, P = 4.125e-02 W'
>>> f"{U=}"
'U=3.3'
>>> print(f"Strom: {I * 1000:.2f} mA")
Strom: 12.50 mA
```

Der interaktive Modus zeigt einen f-String als Zeichenkette mit Apostrophen; erst `print` gibt den reinen Text aus.
::::

**Den gespeicherten Wert von `0.1`, fertig.** In Unterabschnitt [4.6](gleitkommazahlen-der-typ-float.html#stufe-4-6) hat die Rechnung mit $5^{55}$ von Hand die 55 Nachkommastellen des gespeicherten Werts von `0.1` geliefert. Mit einer Formatangabe geht es direkt:

```console
>>> f"{0.1:.20f}"
'0.10000000000000000555'
>>> f"{0.1:.55f}"
'0.1000000000000000055511151231257827021181583404541015625'
```

Dieselben Stellen wie von Hand. Eine Formatangabe rundet nur die Anzeige; der Wert des Objekts bleibt, wie er ist.

⁠**Kurz gesagt:** Ein f-String setzt Werte in `{...}` in einen Text ein; hinter dem Doppelpunkt legt eine Formatangabe Stellen und Form fest.

### Die Eingabe mit `input`

<span class="anker" id="stufe-10-3"></span>

Bisher stehen alle Werte im Quelltext. Ein Einheitenrechner soll aber die Zahlen erfragen, mit denen er rechnet.

:::definition Definition 10.3 (`input`)
<span class="anker" id="satz-10-3"></span>

Die eingebaute Funktion `input` schreibt den Text in ihren Klammern als Frage ins Terminal, wartet, bis der Benutzer eine Zeile eintippt und Enter drückt, und liefert diese Zeile als Zeichenkette, ohne das Enter.
:::

::::beispiel
Im interaktiven Modus erscheint die Frage, und dahinter tippt man die Antwort, hier `5`:

```console
>>> spannung = input("Spannung in V: ")
Spannung in V: 5
>>> spannung
'5'
>>> type(spannung)
<class 'str'>
>>> spannung * 2
'55'
```

`input` liefert *immer* eine Zeichenkette, auch wenn man eine Zahl eintippt. `spannung * 2` wiederholt deshalb den Text, statt zu rechnen. Mit einer Eingabe zu rechnen, verlangt einen weiteren Schritt.
::::

⁠**Kurz gesagt:** `input` fragt nach einer Zeile und liefert sie als `str`.

### Die Typumwandlung

<span class="anker" id="stufe-10-4"></span>

Der Text `'5'` soll zur Zahl 5 werden, die Zahl 42 zum Text `'42'`. Python wandelt nie von selbst um (Unterabschnitt [1.2](objekte-und-typen.html#stufe-1-2)); man muss es ausdrücklich verlangen.

:::definition Definition 10.4 (Typumwandlung)
<span class="anker" id="satz-10-4"></span>

Die Funktionen `int`, `float` und `str` erzeugen aus einem Wert ein neues Objekt mit dem Typ ihres Namens. Das heißt __Typumwandlung__.

<ul>

<li>

`int(text)` und `float(text)` lesen eine Zahl aus einer Zeichenkette; Leerzeichen am Rand sind erlaubt. Passt der Text nicht, melden sie einen `ValueError`.

</li>

<li>

`int(x)` macht aus einem `float` eine ganze Zahl, indem es die Nachkommastellen abschneidet, also in Richtung null rundet.

</li>

<li>

`str(x)` liefert den Text, den `print` für $x$ ausgeben würde.

</li>

</ul>
:::

::::beispiel
Umwandlungen, die gelingen, und zwei, die scheitern:

```console
>>> int("42")
42
>>> int(" 42 ")
42
>>> float("4.2")
4.2
>>> float("1e3")
1000.0
>>> int("4.2")
Traceback (most recent call last):
  File "<python-input-4>", line 1, in <module>
    int("4.2")
    ~~~^^^^^^^
ValueError: invalid literal for int() with base 10: '4.2'
>>> float("2,5")
Traceback (most recent call last):
  File "<python-input-5>", line 1, in <module>
    float("2,5")
    ~~~~~^^^^^^^
ValueError: could not convert string to float: '2,5'
>>> str(42) + "1"
'421'
>>> int(3.99)
3
>>> int(-3.99)
-3
```

`int("4.2")` scheitert, weil `4.2` keine ganze Zahl ist; `int(float("4.2"))` ginge. `float("2,5")` scheitert am Komma: Python erwartet den Dezimalpunkt, auch bei Eingaben. Für Zahlen aus `input` ist das typische Muster deshalb `float(input("..."))`.
::::

⁠**Kurz gesagt:** `int`, `float` und `str` wandeln ausdrücklich um; `int` schneidet Nachkommastellen ab.

:::hintergrund Warum Python Text und Zahl nicht von selbst umwandelt
Was sollte `"2" + 3` ergeben, den Text `'23'` oder die Zahl 5? Manche Sprachen entscheiden sich still für eine der beiden Möglichkeiten, JavaScript etwa für `'23'`. Dann rechnet ein Programm mit eingelesenen Messwerten falsch, ohne dass es jemand merkt. Python folgt dem Grundsatz, bei Mehrdeutigkeit nicht zu raten: Es meldet einen `TypeError` und zwingt dazu, mit `int`, `float` oder `str` zu sagen, was gemeint ist. Zwischen Zahlentypen wandelt Python dagegen sehr wohl von selbst um (Unterabschnitt [2.2](ganze-zahlen-und-rechenoperatoren.html#stufe-2-2)), denn dort ist die Bedeutung eindeutig: $2+3{,}0$ ist $5{,}0$.
:::

### Runden: erst von Hand, dann fertig

<span class="anker" id="stufe-10-5"></span>

`2200 * 1.5e-3` ergibt `3.3000000000000003`, die Spannung an $2{,}2\,\mathrm{k\Omega}$ bei $1{,}5\,\mathrm{mA}$ mit einem Rundungsrest. Ein solches Ergebnis will man auf eine ganze Zahl oder auf wenige Stellen runden, und zwar nicht nur in der Anzeige, sondern als Wert, mit dem man weiterrechnet.

**Von Hand.** `int` schneidet ab. Addiert man vorher $0{,}5$, wird aus dem Abschneiden ein Runden: $2{,}7+0{,}5=3{,}2$ wird zu 3, $2{,}2+0{,}5=2{,}7$ zu 2. Das ist die Schulregel „ab 5 aufrunden“:

```console
>>> int(2.7 + 0.5)
3
>>> int(2.5 + 0.5)
3
>>> int(3.5 + 0.5)
4
>>> int(-2.7 + 0.5)
-2
```

Die letzte Zeile ist falsch: $-2{,}7$ liegt näher an $-3$. Weil `int` Richtung null abschneidet, funktioniert der Trick nur für positive Zahlen.

**Fertig.** Die eingebaute Funktion `round` rundet richtig, auch bei negativen Zahlen.

:::definition Definition 10.5 (`round`)
<span class="anker" id="satz-10-5"></span>

`round(x)` liefert die ganze Zahl, die $x$ am nächsten liegt. Liegt $x$ genau in der Mitte zwischen zwei ganzen Zahlen, liefert `round` die gerade von beiden. `round(x, n)` rundet auf $n$ Nachkommastellen und liefert einen `float`.
:::

```console
>>> round(2.7)
3
>>> round(-2.7)
-3
>>> round(2.5)
2
>>> round(3.5)
4
>>> round(-2.5)
-2
>>> round(3.14159, 2)
3.14
>>> round(2.675, 2)
2.67
>>> f"{2.675:.20f}"
'2.67499999999999982236'
```

`round(2.675, 2)` ergibt $2{,}67$ und nicht $2{,}68$, und das ist kein Fehler: Der gespeicherte Wert von `2.675` liegt knapp unter $2{,}675$, wie die letzte Zeile zeigt, also ist $2{,}67$ die nächste Zahl mit zwei Nachkommastellen. Wer abrunden oder aufrunden will, nimmt `math.floor` oder `math.ceil`.

**Vergleich.**

| $x$ | `int(x + 0.5)` | `round(x)` |
|---|---|---|
| $2{,}7$ | 3 | 3 |
| $2{,}5$ | 3 | 2 |
| $3{,}5$ | 4 | 4 |
| $-2{,}5$ | $-2$ | $-2$ |
| $-2{,}7$ | $-2$ | $-3$ |

Die beiden Wege unterscheiden sich an zwei Stellen: bei genauen Hälften wie $2{,}5$, wo `round` zur geraden Zahl geht, und bei negativen Zahlen, wo der Weg von Hand falsch ist. Der fertige Weg ist für alle Zahlen richtig und folgt derselben Regel wie die Rundung der `float` in Unterabschnitt [4.6](gleitkommazahlen-der-typ-float.html#stufe-4-6).

⁠**Kurz gesagt:** `round` rundet zur nächsten Zahl und bei genauen Hälften zur geraden; `int(x + 0.5)` klappt nur für positive Zahlen und rundet Hälften immer auf.

:::hintergrund Warum zur geraden Zahl gerundet wird
Die Schulregel rundet jede genaue Hälfte auf. Bei vielen gerundeten Werten summiert sich das zu einem Fehler, der immer in dieselbe Richtung zeigt. Ein Beispiel: $0{,}5+1{,}5+2{,}5+3{,}5=8$. Nach der Schulregel gerundet ergibt die Summe $1+2+3+4=10$. Zur geraden Zahl gerundet ergibt sie $0+2+2+4=8$: Die Hälfte der Fälle geht nach oben, die andere nach unten, und im Mittel heben sich die Fehler auf. Deshalb rundet IEEE 754 in der Grundeinstellung jede Rechnung mit `float` zur geraden Mantisse, und Python übernimmt dieselbe Regel für `round`. Es verhindert außerdem, dass ein Wert, den man immer wieder abzieht und hinzuzählt, langsam in eine Richtung wandert.
:::

### Anwendung: ein Einheitenrechner

<span class="anker" id="stufe-10-6"></span>

Mit `input`, `float` und einem f-String lässt sich ein kleines Werkzeug für den Messplatz schreiben: Es fragt nach Spannung und Widerstand und gibt Strom und Leistung in passenden Einheiten aus. Rechnet man mit Kiloohm, kommt der Strom direkt in Milliampere heraus, denn $1\,\mathrm V/1\,\mathrm{k\Omega}=1\,\mathrm{mA}$, und die Leistung in Milliwatt.

```python einheiten.py
# Einheitenrechner: Strom und Leistung an einem Widerstand
spannung = float(input("Spannung in V: "))
widerstand_k = float(input("Widerstand in kOhm: "))

strom_ma = spannung / widerstand_k      # V / kOhm ergibt mA
leistung_mw = spannung * strom_ma       # V * mA ergibt mW

print(f"Strom: {strom_ma:.2f} mA")
print(f"Leistung: {leistung_mw:.2f} mW")
```

Beim Start fragt das Skript nacheinander die beiden Werte ab; eingetippt sind hier 5 und 2.2:

```console Windows (PowerShell)
PS> py einheiten.py
Spannung in V: 5
Widerstand in kOhm: 2.2
Strom: 2.27 mA
Leistung: 11.36 mW
```

```console Linux
$ python3 einheiten.py
Spannung in V: 5
Widerstand in kOhm: 2.2
Strom: 2.27 mA
Leistung: 11.36 mW
```

Tippt man `2,2` mit Komma, bricht das Skript mit dem `ValueError` aus Unterabschnitt [10.4](#stufe-10-4) ab. Wie man solche Eingaben abfängt und erneut fragt, ist eine eigene Fähigkeit, die dieses Kapitel nicht braucht.

⁠**Kurz gesagt:** `float(input(...))` liest eine Zahl, ein f-String gibt das Ergebnis mit passend vielen Stellen aus.

### Aufgaben zu Abschnitt [10](#stufe-10)

<span class="anker" id="stufe-10-7"></span>

:::aufgabe Aufgabe 37 ★ Text und Zahl
<span class="anker" id="aufg-37"></span>

Sage vorher und prüfe: (a) `"ab" * 3`, (b) `"Ohm" + str(470)`, (c) `len("kOhm") * 2`, (d) `int("7") + int("3")`, (e) `"7" + "3"`, (f) `str(1 / 4)`.

:::loesung
```console
>>> "ab" * 3
'ababab'
>>> "Ohm" + str(470)
'Ohm470'
>>> len("kOhm") * 2
8
>>> int("7") + int("3")
10
>>> "7" + "3"
'73'
>>> str(1 / 4)
'0.25'
```

(b) `str` macht aus der Zahl Text, erst dann geht `+`. (c) `len` liefert 4, ein `int`, und $4\cdot2=8$ ist eine Rechnung, keine Wiederholung. (d) und (e) zeigen den Unterschied: Nach der Umwandlung in Zahlen rechnet `+`, bei Text verkettet es.
:::
:::

:::aufgabe Aufgabe 38 ★★ Formatieren
<span class="anker" id="aufg-38"></span>

Schreibe für jede Zeile einen f-String, der mit den gegebenen Variablen genau diesen Text erzeugt.

<ol class="al">

<li>

`r = 4700` $\to$ `R = 4.70 kOhm`

</li>

<li>

`c = 1e-7` $\to$ `C = 1.00e-07 F`

</li>

<li>

`anteil = 0.125` $\to$ `Anteil: 12.5%`

</li>

<li>

`c_feld = 1019` $\to$ `0x3fb` und `01111111011`

</li>

</ol>

:::loesung
```console
>>> r = 4700
>>> f"R = {r / 1000:.2f} kOhm"
'R = 4.70 kOhm'
>>> c = 1e-7
>>> f"C = {c:.2e} F"
'C = 1.00e-07 F'
>>> anteil = 0.125
>>> f"Anteil: {anteil:.1%}"
'Anteil: 12.5%'
>>> c_feld = 1019
>>> f"{c_feld:#x}"
'0x3fb'
>>> f"{c_feld:011b}"
'01111111011'
```

(a) In den geschweiften Klammern darf ein ganzer Ausdruck stehen, hier die Umrechnung in Kiloohm. (c) Die Angabe `%` multipliziert mit 100 und hängt das Prozentzeichen an. (d) `#x` schreibt das Präfix `0x` dazu; `011b` füllt auf 11 Stellen mit Nullen auf, wie im Exponentenfeld von $0{,}1$ in Abb. [7](gleitkommazahlen-der-typ-float.html#abb-7).
:::
:::

:::aufgabe Aufgabe 39 ★★ Runden von Hand und fertig
<span class="anker" id="aufg-39"></span>

Fülle die Tabelle für $x=0{,}5$; $1{,}5$; $-0{,}5$; $-1{,}5$; $4{,}49$ aus: `int(x + 0.5)`, `round(x)`, `math.floor(x)`, `int(x)`. Erst vorhersagen, dann prüfen. Bei welchen Werten liefern alle vier Spalten dasselbe?

:::loesung
```console
>>> import math
>>> int(0.5 + 0.5), round(0.5), math.floor(0.5), int(0.5)
(1, 0, 0, 0)
>>> int(1.5 + 0.5), round(1.5), math.floor(1.5), int(1.5)
(2, 2, 1, 1)
>>> int(-0.5 + 0.5), round(-0.5), math.floor(-0.5), int(-0.5)
(0, 0, -1, 0)
>>> int(-1.5 + 0.5), round(-1.5), math.floor(-1.5), int(-1.5)
(-1, -2, -2, -1)
>>> int(4.49 + 0.5), round(4.49), math.floor(4.49), int(4.49)
(4, 4, 4, 4)
```

| $x$ | `int(x + 0.5)` | `round(x)` | `math.floor(x)` | `int(x)` |
|---|---|---|---|---|
| $0{,}5$ | 1 | 0 | 0 | 0 |
| $1{,}5$ | 2 | 2 | 1 | 1 |
| $-0{,}5$ | 0 | 0 | $-1$ | 0 |
| $-1{,}5$ | $-1$ | $-2$ | $-2$ | $-1$ |
| $4{,}49$ | 4 | 4 | 4 | 4 |

Nur bei $4{,}49$ stimmen alle vier überein: Die Zahl ist positiv, keine genaue Hälfte, und ihr Nachkommaanteil ist kleiner als $0{,}5$. `round` geht bei Hälften zur geraden Zahl ($0{,}5\to0$, $1{,}5\to2$, $-1{,}5\to-2$). Der Weg von Hand rundet Hälften immer auf und wird bei $-1{,}5$ zu $-1$, weil `int` Richtung null abschneidet. `math.floor` rundet nach unten, `int` Richtung null; beide unterscheiden sich nur bei negativen Zahlen.
:::
:::

:::aufgabe Aufgabe 40 ★★ Ein Pegelrechner
<span class="anker" id="aufg-40"></span>

Schreibe ein Skript `pegel.py`, das nach der Eingangsspannung und der Ausgangsspannung in Volt fragt und die Spannungsverstärkung als Faktor mit zwei Nachkommastellen und in Dezibel mit einer Nachkommastelle ausgibt, $20\log_{10}(U_\mathrm{aus}/U_\mathrm{ein})$. Teste es mit $0{,}02\,\mathrm V$ und $1{,}2\,\mathrm V$.

:::loesung
```python pegel.py
# Pegelrechner: Spannungsverstärkung als Faktor und in Dezibel
import math

u_ein = float(input("Eingangsspannung in V: "))
u_aus = float(input("Ausgangsspannung in V: "))

faktor = u_aus / u_ein
pegel_db = 20 * math.log10(faktor)    # Spannungspegel in dB

print(f"Faktor: {faktor:.2f}")
print(f"Pegel: {pegel_db:.1f} dB")
```

```console Windows (PowerShell)
PS> py pegel.py
Eingangsspannung in V: 0.02
Ausgangsspannung in V: 1.2
Faktor: 60.00
Pegel: 35.6 dB
```

Unter Linux mit `python3 pegel.py` gleich. Das Ergebnis passt zu Aufgabe [30](module-math-und-sys.html#aufg-30): Faktor 60, also $35{,}6\,\mathrm{dB}$.
:::
:::

:::aufgabe Aufgabe 41 ★ Ein Fehler beim Einlesen
<span class="anker" id="aufg-41"></span>

Ein Skript enthält die Zeilen `u = input("U in V: ")` und `print("Doppelte Spannung:", u * 2)`. Für die Eingabe 5 gibt es `55` aus. Erkläre das Verhalten und behebe den Fehler. Was gibt dein verbessertes Skript für die Eingabe `2.5` aus?

:::loesung
`input` liefert immer einen `str` (Unterabschnitt [10.3](#stufe-10-3)). `u * 2` wiederholt deshalb den Text `'5'`, statt zu rechnen. Abhilfe: die Eingabe mit `float` umwandeln.

```python einlesen.py
# Eine Spannung einlesen und verdoppeln, mit Typumwandlung
u = float(input("U in V: "))
print("Doppelte Spannung:", u * 2)
```

```console Linux
$ python3 einlesen.py
U in V: 2.5
Doppelte Spannung: 5.0
```

Mit `int` statt `float` wäre die Eingabe `2.5` mit einem `ValueError` gescheitert, deshalb ist `float` die richtige Wahl für Messwerte.
:::
:::

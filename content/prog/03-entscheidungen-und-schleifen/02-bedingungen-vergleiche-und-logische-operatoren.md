---
title: Bedingungen: Vergleiche und logische Operatoren
pfad: Informatik / Programmieren / Python / Entscheidungen und Schleifen
knoten: Python 3: Entscheidungen und Schleifen
order: 6040200
summary: Ein Programm, das entscheiden soll, braucht eine Frage, auf die es nur ja oder nein gibt: Liegt die Spannung im erlaubten Bereich?
tags: verketteter Vergleich, Kurzschlussauswertung, Wahrheitswert
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Ein Programm, das entscheiden soll, braucht eine Frage, auf die es nur ja oder nein gibt: Liegt die Spannung im erlaubten Bereich? Ist der Strom kleiner als die Grenze? Dieser Abschnitt zeigt, wie man solche Fragen in Python schreibt, wie man mehrere davon verknüpft und welche Werte Python als ja und welche als nein ansieht.
:::

### Rückblick: Wahrheitswerte und Vergleiche

<span class="anker" id="stufe-1-1"></span>

Python 2 hat die Bausteine schon bereitgestellt. Der Typ `bool` hat genau zwei Werte, `True` und `False`. Die sechs Vergleichsoperatoren liefern einen solchen Wert:

| Operator | Bedeutung | Operator | Bedeutung |
|---|---|---|---|
| `==` | gleich | `!=` | ungleich |
| `<` | kleiner | `<=` | kleiner oder gleich |
| `>` | größer | `>=` | größer oder gleich |

Vergleiche haben einen niedrigeren Rang als alle Rechenoperatoren: In `u * 2 > 10` rechnet Python zuerst `u * 2`. Gleitkommazahlen prüft man nicht mit `==` auf Gleichheit, sondern mit einer Toleranz, fertig mit `math.isclose`. Ob ein Name an `None` gebunden ist, prüft man mit `is`. Ausführlich: [Programmieren, Python 2, Abschnitt 7](/wissen/informatik/programmieren/python/werte-typen-und-variablen/wahrheitswerte-und-vergleiche.html#stufe-7).

```console
>>> u = 5.1
>>> u > 5
True
>>> type(u > 5)
<class 'bool'>
>>> 0.1 + 0.2 == 0.3
False
```

⁠**Kurz gesagt:** Ein Vergleich ist ein Ausdruck, dessen Wert `True` oder `False` ist.

### Verkettete Vergleiche

<span class="anker" id="stufe-1-2"></span>

Ein USB-Anschluss soll 5 V liefern, erlaubt sind 4,75 V bis 5,25 V. Ob eine gemessene Spannung $U$ in diesem Bereich liegt, schreibt man in der Mathematik als $4{,}75\,\mathrm V\le U\le5{,}25\,\mathrm V$.

**Zwei Marken auf dem Zahlenstrahl.** Die Kette $4{,}75\le U\le5{,}25$ enthält zwei Vergleiche, die beide stimmen müssen: $U$ liegt rechts von der unteren Marke und links von der oberen. Python erlaubt genau diese Schreibweise.

:::definition Definition 1.1 (Verketteter Vergleich)
<span class="anker" id="satz-1-1"></span>

Stehen mehrere Vergleichsoperatoren hintereinander, etwa `a < b <= c`, so heißt der Ausdruck ein __verketteter Vergleich__. Er ergibt `True` genau dann, wenn jeder der einzelnen Vergleiche `a < b` und `b <= c` `True` ergibt. Den mittleren Ausdruck `b` wertet Python dabei nur einmal aus, und ergibt schon ein früherer Vergleich `False`, wertet es die weiteren nicht mehr aus.
:::

::::beispiel
Eine Spannung im Bereich und eine darüber:

```console
>>> u = 5.1
>>> 4.75 <= u <= 5.25
True
>>> u = 5.4
>>> 4.75 <= u <= 5.25
False
>>> 1 < 3 > 2
True
```

Die letzte Zeile ist erlaubt, denn `1 < 3` und `3 > 2` stimmen beide. Sie liest sich aber schlecht, weil sie keinen Bereich beschreibt. Verkettete Vergleiche benutzt man am besten nur in der Form `untere <= wert <= obere`.
::::

⁠**Kurz gesagt:** `a <= x <= b` prüft wie in der Mathematik, ob `x` zwischen `a` und `b` liegt.

:::hintergrund Warum dieselbe Zeile in C immer wahr ist
In C, der Sprache, in der CPython selbst geschrieben ist, liefert ein Vergleich keinen eigenen Wahrheitswert, sondern die ganze Zahl 1 für wahr und 0 für falsch. Mehrere Vergleiche hintereinander wertet C von links nach rechts aus, einen nach dem anderen. Aus `4.75 <= u <= 5.25` wird dort `(4.75 <= u) <= 5.25`: Zuerst entsteht 0 oder 1, und beides ist kleiner als 5,25. Die Bedingung ist also immer erfüllt, auch für $u=100$. Der Compiler gcc warnt deshalb mit der Option `-Wall` vor solchen Ketten. Python hat sich für die Bedeutung aus der Mathematik entschieden, weil sie das ist, was man beim Lesen erwartet.
:::

### Zeichenketten vergleichen

<span class="anker" id="stufe-1-3"></span>

Auch Text muss man vergleichen, etwa wenn ein Programm prüft, ob jemand `ja` eingetippt hat, oder Namen alphabetisch ordnen soll.

**Wie im Wörterbuch.** Im Wörterbuch steht „Ohm“ vor „Volt“, weil schon der erste Buchstabe entscheidet. Sind die ersten Buchstaben gleich, entscheidet der zweite, und so weiter. Ein Wort, das der Anfang eines längeren ist, steht vor diesem: „Volt“ vor „Voltmeter“.

:::definition Definition 1.2 (Vergleich von Zeichenketten)
<span class="anker" id="satz-1-2"></span>

Zwei Zeichenketten sind gleich (`==`), wenn sie aus denselben Zeichen in derselben Reihenfolge bestehen; Groß- und Kleinbuchstaben sind verschiedene Zeichen. Für `<` und die übrigen Größenvergleiche geht Python die beiden Ketten Zeichen für Zeichen von links durch. Am ersten Zeichen, in dem sie sich unterscheiden, entscheidet die Nummer des Zeichens: Die Kette mit der kleineren Nummer ist die kleinere. Ist eine Kette der Anfang der anderen, ist sie die kleinere.
:::

Die Nummer eines Zeichens ist die weltweit festgelegte Nummer aus [Programmieren, Python 1, Abschnitt 6.1](/wissen/informatik/programmieren/python/programme-und-der-python-interpreter/fehler-lesen-und-verstehen.html#stufe-6-1), zum Beispiel U+201E für das untere Anführungszeichen. Für die Reihenfolge reicht es, drei Bereiche zu kennen: Die Ziffern `0` bis `9` haben die Nummern U+0030 bis U+0039, die Großbuchstaben `A` bis `Z` U+0041 bis U+005A und die Kleinbuchstaben `a` bis `z` U+0061 bis U+007A. Ziffern kommen also vor Großbuchstaben, Großbuchstaben vor Kleinbuchstaben.

::::beispiel
Fünf Vergleiche von Zeichenketten:

```console
>>> "Ohm" == "ohm"
False
>>> "Ohm" < "Volt"
True
>>> "Z" < "a"
True
>>> "Volt" < "Voltmeter"
True
>>> "10" < "9"
True
```

Die letzte Zeile verdient einen zweiten Blick. `"10"` und `"9"` sind Text, keine Zahlen. Python vergleicht das erste Zeichen `1` (U+0031) mit `9` (U+0039), und `1` hat die kleinere Nummer. Das wird zur Falle, wenn ein Programm Eingaben vergleicht, denn `input` liefert immer eine Zeichenkette ([Programmieren, Python 2, Abschnitt 10.3](/wissen/informatik/programmieren/python/werte-typen-und-variablen/zeichenketten-eingabe-und-ausgabe.html#stufe-10-3)). Erst nach der Typumwandlung vergleicht Python Zahlen:

```console
>>> eingabe = "10"
>>> eingabe < "9"
True
>>> float(eingabe) < 9
False
>>> eingabe == 10
False
>>> eingabe < 9
Traceback (most recent call last):
  File "<python-input-4>", line 1, in <module>
    eingabe < 9
TypeError: '<' not supported between instances of 'str' and 'int'
```

Gleichheit zwischen Text und Zahl ist einfach falsch, denn ein Text ist nie gleich einer Zahl. Einen Größenvergleich zwischen beiden lehnt Python dagegen ab, weil es keine sinnvolle Antwort gibt.
::::

⁠**Kurz gesagt:** Zeichenketten vergleicht Python Zeichen für Zeichen nach ihren Nummern; `"10" < "9"` ist wahr, deshalb Eingaben erst umwandeln, dann vergleichen.

### Der Operator `not`

<span class="anker" id="stufe-1-4"></span>

Manchmal ist die Gegenfrage die interessante: nicht „liegt die Spannung im Bereich?“, sondern „liegt sie nicht im Bereich?“.

**Ein Inverter.** In der Digitaltechnik kehrt ein Inverter ein Signal um: Aus 1 wird 0, aus 0 wird 1. Der Operator `not` tut dasselbe mit Wahrheitswerten.

:::definition Definition 1.3 (`not`)
<span class="anker" id="satz-1-3"></span>

`not` ist ein einstelliger Operator. `not x` ergibt `True`, wenn `x` den Wert `False` hat, und `False`, wenn `x` den Wert `True` hat.
:::

| `x` | `not x` |
|---|---|
| `False` | `True` |
| `True` | `False` |

`not` hat einen niedrigeren Rang als die Vergleiche: `not u > 5.25` heißt `not (u > 5.25)`.

::::beispiel
Eine Spannung von 5,4 V liegt nicht im Bereich:

```console
>>> u = 5.4
>>> not 4.75 <= u <= 5.25
True
>>> not True
False
```
::::

⁠**Kurz gesagt:** `not` kehrt einen Wahrheitswert um.

### Der Operator `and`

<span class="anker" id="stufe-1-5"></span>

Ein Netzteil arbeitet nur dann richtig, wenn zwei Dinge gleichzeitig stimmen: Die Spannung liegt im Bereich, und der Strom überschreitet die Grenze nicht.

**Zwei Schalter in Reihe.** Eine Lampe hinter zwei Schaltern in Reihe leuchtet nur, wenn beide Schalter geschlossen sind. Ist einer offen, bleibt sie dunkel.

:::definition Definition 1.4 (`and`)
<span class="anker" id="satz-1-4"></span>

`and` ist ein zweistelliger Operator. `a and b` ergibt `True` genau dann, wenn `a` und `b` beide `True` sind.
:::

| `a` | `b` | `a and b` |
|---|---|---|
| `False` | `False` | `False` |
| `False` | `True` | `False` |
| `True` | `False` | `False` |
| `True` | `True` | `True` |

Ein verketteter Vergleich ist eine Kurzschreibweise für `and`: `a < b < c` hat denselben Wert wie `a < b and b < c`, nur dass `b` einmal ausgewertet wird (Unterabschnitt [1.2](#stufe-1-2)).

::::beispiel
Die Spannung stimmt, der Strom ist mit 0,62 A aber höher als die erlaubten 0,5 A:

```console
>>> u = 5.1
>>> i = 0.62
>>> 4.75 <= u <= 5.25 and i <= 0.5
False
```
::::

⁠**Kurz gesagt:** `a and b` ist nur wahr, wenn beide wahr sind.

### Der Operator `or`

<span class="anker" id="stufe-1-6"></span>

Ein Alarm soll anspringen, wenn die Spannung zu niedrig ist oder wenn sie zu hoch ist; eins von beiden genügt.

**Zwei Schalter parallel.** Eine Lampe hinter zwei parallelen Schaltern leuchtet, sobald mindestens einer geschlossen ist.

:::definition Definition 1.5 (`or`)
<span class="anker" id="satz-1-5"></span>

`or` ist ein zweistelliger Operator. `a or b` ergibt `True` genau dann, wenn mindestens einer der beiden Operanden `True` ist.
:::

| `a` | `b` | `a or b` |
|---|---|---|
| `False` | `False` | `False` |
| `False` | `True` | `True` |
| `True` | `False` | `True` |
| `True` | `True` | `True` |

::::beispiel
Der Alarm aus der Einleitung, einmal mit `or` und einmal als Umkehrung des Bereichs:

```console
>>> u = 5.4
>>> u < 4.75 or u > 5.25
True
>>> not 4.75 <= u <= 5.25
True
```

Beide Zeilen fragen dasselbe: Eine Spannung liegt genau dann außerhalb des Bereichs, wenn sie unter der unteren oder über der oberen Grenze liegt.
::::

⁠**Kurz gesagt:** `a or b` ist wahr, sobald einer der beiden wahr ist.

### Die Rangfolge der logischen Operatoren

<span class="anker" id="stufe-1-7"></span>

Was bedeutet `a or b and c`: `(a or b) and c` oder `a or (b and c)`? Wie bei Punkt- und Strichrechnung legt eine Rangfolge fest, was zuerst gilt.

:::definition Definition 1.6 (Rangfolge)
<span class="anker" id="satz-1-6"></span>

Von fester zu loser bindend: Rechenoperatoren, dann Vergleiche, dann `not`, dann `and`, zuletzt `or`. `and` bindet also stärker als `or`, so wie Mal stärker bindet als Plus.
:::

::::beispiel
Ohne Klammern rechnet Python zuerst `False and False`:

```console
>>> True or False and False
True
>>> (True or False) and False
False
```

Wer eine Bedingung aus `and` und `or` zusammensetzt, setzt am besten Klammern, auch wo sie nicht nötig sind. Sie kosten nichts und ersparen dem Leser das Nachschlagen.
::::

⁠**Kurz gesagt:** `not` vor `and` vor `or`, alle nach den Vergleichen; im Zweifel Klammern.

### Die Kurzschlussauswertung

<span class="anker" id="stufe-1-8"></span>

Manche Bedingung hat eine zweite Hälfte, die nur dann sinnvoll ist, wenn die erste stimmt. In `n != 0 and 10 / n > 1` darf die Division nur stattfinden, wenn `n` nicht null ist.

**Wer die Antwort kennt, liest nicht weiter.** Ist in „A und B“ schon A falsch, ist das Ganze falsch, was immer B ist. Ist in „A oder B“ schon A wahr, ist das Ganze wahr. In beiden Fällen braucht man B nicht mehr anzusehen.

:::definition Definition 1.7 (Kurzschlussauswertung)
<span class="anker" id="satz-1-7"></span>

Python wertet `a and b` und `a or b` von links aus und hört auf, sobald das Ergebnis feststeht. Bei `a and b` wird `b` nur ausgewertet, wenn `a` wahr ist; bei `a or b` nur, wenn `a` falsch ist. Diese Regel heißt __Kurzschlussauswertung__.
:::

::::beispiel
Der Ausdruck `1 / 0` löst eine Ausnahme aus, sobald Python ihn auswertet. Mit ihm sieht man, ob die rechte Seite ausgewertet wird:

```console
>>> False and 1 / 0
False
>>> True or 1 / 0
True
>>> True and 1 / 0
Traceback (most recent call last):
  File "<python-input-2>", line 1, in <module>
    True and 1 / 0
             ~~^~~
ZeroDivisionError: division by zero
```

In den ersten beiden Zeilen steht das Ergebnis nach dem linken Operanden fest, und `1 / 0` wird nie gerechnet. Genau das macht die Bedingung vom Anfang sicher. Die Reihenfolge der beiden Hälften ist dabei nicht gleichgültig:

```console
>>> n = 0
>>> n != 0 and 10 / n > 1
False
>>> 10 / n > 1 and n != 0
Traceback (most recent call last):
  File "<python-input-2>", line 1, in <module>
    10 / n > 1 and n != 0
    ~~~^~~
ZeroDivisionError: division by zero
```

Die Prüfung, die eine Rechnung erst erlaubt, muss links stehen.
::::

⁠**Kurz gesagt:** `and` und `or` werten den rechten Operanden nur aus, wenn er das Ergebnis noch ändern kann; die schützende Bedingung gehört deshalb nach links.

:::hintergrund Warum `and` und `or` keine Funktionen sein können
Bei einem Funktionsaufruf wie `print(a, b)` rechnet Python zuerst alle Werte in den Klammern aus und übergibt sie dann. Eine Funktion „und“ bekäme also immer beide Werte, auch den, der eine Ausnahme auslöst. Deshalb sind `and` und `or` Teil der Sprache selbst. Beim Übersetzen in Bytecode ([Programmieren, Python 1, Abschnitt 2.4](/wissen/informatik/programmieren/python/programme-und-der-python-interpreter/vom-quelltext-zur-ausfuhrung-compiler-und-interpreter.html#stufe-2-4)) wird aus `a and b` ein Sprung: Python berechnet `a`, prüft dessen Wahrheitswert und springt, wenn `a` falsch ist, an den Befehlen für `b` vorbei. Die Befehle für `b` stehen zwar im Bytecode, werden aber übersprungen.
:::

### Der Wahrheitswert von Objekten

<span class="anker" id="stufe-1-9"></span>

Die Operatoren `not`, `and` und `or` nehmen nicht nur `True` und `False` an, sondern jeden Wert. Python muss also wissen, ob etwa die Zahl 0 oder die Zeichenkette `""` als ja oder als nein gilt. Python 2 hat diese Frage offengelassen.

**Ist da etwas?** Die Regel folgt einer einfachen Frage: Ist in dem Wert etwas enthalten? Eine Null und eine leere Zeichenkette enthalten nichts und gelten als nein; jede andere Zahl und jeder Text mit mindestens einem Zeichen gelten als ja.

:::definition Definition 1.8 (Wahrheitswert)
<span class="anker" id="satz-1-8"></span>

Jedes Objekt hat einen __Wahrheitswert__, `True` oder `False`; die Typumwandlung `bool(x)` zeigt ihn an. Von den bisher bekannten Werten haben genau diese den Wahrheitswert `False`: `False`, `None`, die Null jedes Zahlentyps (`0`, `0.0`, `-0.0`, `0j`) und die leere Zeichenkette `""`. Alle anderen haben den Wahrheitswert `True`. Wo Python eine Bedingung erwartet, etwa bei `not`, benutzt es den Wahrheitswert des Objekts.
:::

::::beispiel
`bool` zeigt den Wahrheitswert verschiedener Werte:

```console
>>> bool(0)
False
>>> bool(0.0)
False
>>> bool("")
False
>>> bool(None)
False
>>> bool("0")
True
>>> bool(" ")
True
>>> bool("False")
True
>>> bool(-1)
True
>>> bool(1e-300)
True
>>> bool(0.1 + 0.2 - 0.3)
True
>>> not ""
True
```

`"0"`, `" "` und `"False"` sind Zeichenketten mit mindestens einem Zeichen, also wahr; was die Zeichen bedeuten, spielt keine Rolle. `0.1 + 0.2 - 0.3` ist nicht null, sondern etwa $5{,}55\cdot10^{-17}$, weil jede Rechnung gerundet wird ([Programmieren, Python 2, Abschnitt 5.1](/wissen/informatik/programmieren/python/werte-typen-und-variablen/rechnen-mit-gleitkommazahlen.html#stufe-5-1)), und gilt deshalb als wahr.
::::

⁠**Kurz gesagt:** Von den bisher bekannten Werten gelten Null, `None`, `False` und die leere Zeichenkette als falsch, alle anderen als wahr.

:::hintergrund Wer festlegt, was als falsch gilt
Den Wahrheitswert legt der Typ eines Objekts fest, so wie er auch festlegt, was `+` bedeutet ([Programmieren, Python 2, Abschnitt 1.2](/wissen/informatik/programmieren/python/werte-typen-und-variablen/objekte-und-typen.html#stufe-1-2)). Für die Zahlentypen ist es die Null, für `str` die leere Kette. Die Regel stammt aus älteren Sprachen: In C gilt in einer Bedingung die Zahl 0 als falsch und jede andere als wahr. Python überträgt diese Idee von „null“ auf „leer“. So kann man fragen, ob ein Text etwas enthält, ohne seine Länge auszurechnen.
:::

### Was `and` und `or` als Ergebnis liefern

<span class="anker" id="stufe-1-10"></span>

Ein Programm fragt nach dem Namen eines Messplatzes. Bleibt die Eingabe leer, soll ein Standardname gelten. Dafür gibt es eine kurze Schreibweise, die eine Eigenschaft von `and` und `or` nutzt.

:::definition Definition 1.9 (Ergebnis von `and` und `or`)
<span class="anker" id="satz-1-9"></span>

`a and b` ergibt `a` selbst, wenn `a` falsch ist, und sonst `b`. `a or b` ergibt `a` selbst, wenn `a` wahr ist, und sonst `b`. Das Ergebnis ist also immer einer der beiden Operanden, unverändert. `not x` ergibt dagegen immer `True` oder `False`.
:::

Sind beide Operanden vom Typ `bool`, kommen genau die Tafeln aus den Unterabschnitten [1.5](#stufe-1-5) und [1.6](#stufe-1-6) heraus.

::::beispiel
Mit Zahlen und Zeichenketten als Operanden:

```console
>>> 3 and 4
4
>>> 0 and 4
0
>>> 0 or "leer"
'leer'
>>> "" or "Standard"
'Standard'
>>> "Messplatz 2" or "Standard"
'Messplatz 2'
>>> None or 0
0
>>> not "Ohm"
False
```

Mit `name = eingabe or "Standard"` bekommt `name` den eingetippten Text, wenn er nicht leer ist, und sonst `"Standard"`.
::::

**Die Falle mit der Null.** Bei Zahlen ist dieselbe Schreibweise gefährlich. Die Zeile `strom = messwert or 0.02` soll einen fehlenden Messwert durch 20 mA ersetzen. Eine echte Messung von `0.0` hat aber ebenfalls den Wahrheitswert `False` und wird stillschweigend durch `0.02` ersetzt. Ob ein Wert fehlt, prüft man deshalb mit `messwert is None` und nicht über seinen Wahrheitswert.

⁠**Kurz gesagt:** `and` und `or` liefern einen ihrer Operanden; `wert or ersatz` ersetzt jeden falschen Wert, auch eine echte Null.

:::hintergrund Warum `and` und `or` einen Operanden liefern
Wegen der Kurzschlussauswertung steht bei `a and b` und `a or b` am Ende ein Operand fest, der das Ergebnis entschieden hat: Ist `a` bei `and` falsch, entscheidet `a`; sonst entscheidet `b`, denn das Ganze ist genau dann wahr, wenn `b` wahr ist. Dieser entscheidende Operand hat denselben Wahrheitswert wie das Ergebnis. Python gibt ihn deshalb unverändert zurück, statt ihn in `True` oder `False` umzuwandeln: Als Bedingung benutzt, verhält er sich genau wie der umgewandelte Wert, und er verliert dabei keine Information, die man wie beim Standardnamen noch brauchen kann. Bei `not` gibt es keinen solchen Operanden, denn keiner der Werte steht für das Gegenteil. Deshalb muss `not` einen neuen Wert erzeugen, und der ist immer ein `bool`.
:::

### Aufgaben zu Abschnitt [1](#stufe-1)

<span class="anker" id="stufe-1-11"></span>

:::aufgabe Aufgabe 1 ★ Wahrheitswerte vorhersagen
<span class="anker" id="aufg-1"></span>

Sage für jeden Ausdruck vorher, was der interaktive Modus anzeigt, und prüfe dann am Rechner: (a) `bool("0")`, (b) `bool("")`, (c) `0 or "x"`, (d) `3 and 4`, (e) `1 < 5 < 3`, (f) `"10" < "9"`, (g) `not 0.0`, (h) `None or 0`, (i) `"Ohm" == "ohm" or 2 > 1`.

:::loesung
```console
>>> bool("0")
True
>>> bool("")
False
>>> 0 or "x"
'x'
>>> 3 and 4
4
>>> 1 < 5 < 3
False
>>> "10" < "9"
True
>>> not 0.0
True
>>> None or 0
0
>>> "Ohm" == "ohm" or 2 > 1
True
```

(a) `"0"` ist eine Zeichenkette mit einem Zeichen, also wahr; was das Zeichen bedeutet, spielt keine Rolle. (b) Die leere Zeichenkette ist falsch. (c) `0` ist falsch, also liefert `or` den rechten Operanden. (d) `3` ist wahr, also liefert `and` den rechten Operanden. (e) `1 < 5` stimmt, `5 < 3` nicht; ein verketteter Vergleich ist nur wahr, wenn alle Teile stimmen. (f) Text wird Zeichen für Zeichen verglichen, und `1` hat eine kleinere Nummer als `9`. (g) `0.0` ist falsch, `not` macht daraus `True`. (h) `None` ist falsch, also kommt der rechte Operand `0` heraus, obwohl auch er falsch ist. (i) Der Vergleich links ist `False` (Groß- und Kleinschreibung), der rechte `True`; `or` liefert ihn.
:::
:::

:::aufgabe Aufgabe 2 ★★ Bedingungen für einen Akku
<span class="anker" id="aufg-2"></span>

Eine Lithium-Ionen-Zelle darf zwischen 3,0 V und 4,2 V betrieben werden, bei Temperaturen zwischen $-20$ °C und $60$ °C und mit höchstens 2 A Ladestrom.

<ol class="al">

<li>

Schreibe einen Ausdruck, der für die Namen `u`, `temp` und `i` genau dann `True` ergibt, wenn alle drei Werte erlaubt sind.

</li>

<li>

Schreibe einen Ausdruck für „mindestens ein Wert ist nicht erlaubt“, ohne `not` zu benutzen.

</li>

<li>

Prüfe beide für $u=3{,}7$ V, $\vartheta=25$ °C, $I=2{,}5$ A.

</li>

</ol>

:::loesung
(a) Drei Bereiche, verknüpft mit `and`:

```python
3.0 <= u <= 4.2 and -20 <= temp <= 60 and i <= 2
```

(b) „Mindestens ein Wert ist nicht erlaubt“ heißt: Eine der Grenzen ist überschritten. Ohne `not` schreibt man jede Verletzung einzeln und verknüpft sie mit `or`:

```python
u < 3.0 or u > 4.2 or temp < -20 or temp > 60 or i > 2
```

(c)

```console
>>> u = 3.7
>>> temp = 25
>>> i = 2.5
>>> 3.0 <= u <= 4.2 and -20 <= temp <= 60 and i <= 2
False
>>> u < 3.0 or u > 4.2 or temp < -20 or temp > 60 or i > 2
True
```

Spannung und Temperatur sind erlaubt, der Strom nicht. Deshalb ist (a) falsch und (b) wahr. Die beiden Ausdrücke liefern immer entgegengesetzte Werte, weil (b) genau das Gegenteil von (a) beschreibt.
:::
:::

:::aufgabe Aufgabe 3 ★★ Die Regeln von De Morgan
<span class="anker" id="aufg-3"></span>

Prüfe im interaktiven Modus für alle vier Kombinationen von `a` und `b` aus `True` und `False`, dass `not (a and b)` denselben Wert hat wie `not a or not b`, und dass `not (a or b)` denselben Wert hat wie `not a and not b`. Erkläre die erste Regel mit den zwei Schaltern in Reihe.

:::loesung
Für jede der vier Kombinationen ergeben beide Vergleiche `True`, hier die erste und die letzte:

```console
>>> a = False
>>> b = False
>>> (not (a and b)) == (not a or not b)
True
>>> (not (a or b)) == (not a and not b)
True
>>> a = True
>>> b = True
>>> (not (a and b)) == (not a or not b)
True
>>> (not (a or b)) == (not a and not b)
True
```

Mit `a = False, b = True` und `a = True, b = False` kommt ebenfalls zweimal `True` heraus. Die Klammern um `not (a and b)` sind nötig, weil `==` stärker bindet als `not`.

Mit den zwei Schaltern in Reihe: `a and b` heißt „die Lampe leuchtet“, also beide Schalter geschlossen. `not (a and b)` heißt „die Lampe ist dunkel“, und das ist genau dann der Fall, wenn mindestens einer der Schalter offen ist, also `not a or not b`. Die zweite Regel ist dasselbe für die Parallelschaltung: Die Lampe ist genau dann dunkel, wenn beide Schalter offen sind.
:::
:::

:::aufgabe Aufgabe 4 ★★ Schutz durch die Reihenfolge
<span class="anker" id="aufg-4"></span>

Welche der folgenden Ausdrücke lösen für `n = 0` eine Ausnahme aus, welche nicht? Begründe, dann prüfe. (a) `n != 0 and 1 / n < 0.5`, (b) `1 / n < 0.5 and n != 0`, (c) `n == 0 or 1 / n < 0.5`, (d) `n == 0 and 1 / n < 0.5`. (e) Nach `import math` und `x = -1`: Was ergibt `x >= 0 and math.sqrt(x) < 3`?

:::loesung
(a) `n != 0` ist falsch, also wertet `and` die Division nicht aus: `False`, keine Ausnahme. (b) Die Division steht links und wird zuerst ausgewertet: `ZeroDivisionError`. (c) `n == 0` ist wahr, also wertet `or` den Rest nicht aus: `True`. (d) `n == 0` ist wahr, und `and` muss deshalb den rechten Teil auswerten: `ZeroDivisionError`. (e) `x >= 0` ist falsch, `math.sqrt(-1)` wird nie aufgerufen: `False`.

```console
>>> n = 0
>>> n != 0 and 1 / n < 0.5
False
>>> n == 0 or 1 / n < 0.5
True
>>> n == 0 and 1 / n < 0.5
Traceback (most recent call last):
  File "<python-input-3>", line 1, in <module>
    n == 0 and 1 / n < 0.5
               ~~^~~
ZeroDivisionError: division by zero
>>> import math
>>> x = -1
>>> x >= 0 and math.sqrt(x) < 3
False
```

Schützen kann eine Bedingung nur, wenn sie links steht und so gebaut ist, dass sie im gefährlichen Fall das Ergebnis schon festlegt: bei `and` durch „falsch“, bei `or` durch „wahr“.
:::
:::

:::aufgabe Aufgabe 5 ★★ Zwei Fallen mit `or`
<span class="anker" id="aufg-5"></span>

<ol class="al">

<li>

`strom = messwert or 0.02` soll fehlende Messwerte ersetzen. Was ergibt die Zeile für `messwert = 0.005`, für `messwert = None` und für `messwert = 0.0`? Welches Ergebnis ist falsch, und warum?

</li>

<li>

Für `einheit = "Ohm"` ergibt `einheit == "V" or "A"` nicht `False`. Was ergibt es, und wie lautet der Ausdruck, der wirklich fragt, ob `einheit` gleich `"V"` oder gleich `"A"` ist?

</li>

</ol>

:::loesung
(a)

```console
>>> messwert = 0.005
>>> messwert or 0.02
0.005
>>> messwert = None
>>> messwert or 0.02
0.02
>>> messwert = 0.0
>>> messwert or 0.02
0.02
```

Das dritte Ergebnis ist falsch: Eine gemessene Null ist ein gültiger Messwert, aber `0.0` hat den Wahrheitswert `False`, und `or` ersetzt ihn. Gemeint war „fehlt der Wert?“, und das prüft `messwert is None`. Mit den Mitteln aus Abschnitt [2](entscheidungen-if-elif-und-else.html#stufe-2) schreibt man:

```python
if messwert is None:
    strom = 0.02
else:
    strom = messwert
```

(b)

```console
>>> einheit = "Ohm"
>>> einheit == "V" or "A"
'A'
>>> einheit == "V" or einheit == "A"
False
```

`==` bindet stärker als `or`. Python liest `(einheit == "V") or "A"`; der linke Teil ist `False`, also liefert `or` den rechten Operanden `"A"`, und der ist als nicht leere Zeichenkette wahr. Jeder Vergleich muss vollständig dastehen.
:::
:::

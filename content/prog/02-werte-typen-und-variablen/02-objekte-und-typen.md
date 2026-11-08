---
title: Objekte und Typen
pfad: Informatik / Programmieren / Python / Werte, Typen und Variablen
knoten: Python 2: Werte, Typen und Variablen
order: 6030200
summary: Alles, womit Python rechnet, liegt als Objekt im Arbeitsspeicher.
tags: Objekt, Typ, Identität, Methode
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Alles, womit Python rechnet, liegt als Objekt im Arbeitsspeicher. Dieser Abschnitt klärt, was ein Objekt ist, woran Python erkennt, was man mit einem Objekt tun darf, und wie man zwei Objekte voneinander unterscheidet.
:::

### Das Objekt

<span class="anker" id="stufe-1-1"></span>

Python 1 hat Zahlen wie 42 und Texte wie `"Hallo"` Werte genannt ([Programmieren, Python 1, Abschnitt 4.2](/wissen/informatik/programmieren/python/programme-und-der-python-interpreter/der-interaktive-modus.html#stufe-4-2)). Während Python mit einem Wert arbeitet, muss dieser Wert irgendwo stehen. Und Python muss wissen, was für ein Wert es ist: Mit der Zahl 42 kann man rechnen, mit dem Text aus den Zeichen 4 und 2 nicht.

**Ein beschrifteter Kasten.** Man kann sich den Arbeitsspeicher als lange Reihe von Fächern vorstellen. Python legt jeden Wert in einen eigenen Kasten. Auf den Kasten schreibt es, welche Art von Wert darin liegt, und jeder Kasten steht an einem festen Platz mit einer Platznummer (Abb. [1](#abb-1)). Das ist ein Bild zur Orientierung: Wie der Speicher technisch aufgebaut ist, spielt für das Folgende keine Rolle.

:::abbildung prog/k2objekt 1
Drei Objekte im Arbeitsspeicher, als Kästen gezeichnet. Jeder Kasten trägt eine Aufschrift, welche Art von Wert er enthält, und steht an einem festen Platz. Auf dem Bildschirm sehen die erste und die dritte Zahl gleich aus, für Python sind es verschiedene Dinge. Die Platznummern sind erfunden.
:::

:::definition Definition 1.1 (Objekt)
<span class="anker" id="satz-1-1"></span>

Ein __Objekt__ ist ein Stück des Arbeitsspeichers, in dem Python einen Wert ablegt, zusammen mit der Angabe, welche Art von Wert dort liegt.
:::

Jeder Wert, mit dem Python arbeitet, steckt in einem Objekt: jede Zahl, jede Zeichenkette, auch jedes Zwischenergebnis einer Rechnung.

**Beispiel.** Tippt man im interaktiven Modus nacheinander `42`, `4.0` und `"42"` ein, rechnet Python mit drei Objekten wie in Abb. [1](#abb-1):

```console
>>> 42
42
>>> 4.0
4.0
>>> "42"
'42'
```

Das erste enthält die ganze Zahl 42, das zweite eine Zahl mit Nachkommastellen, das dritte den Text aus den Zeichen 4 und 2. Der interaktive Modus zeigt die Art schon in der Schreibweise: ohne Punkt, mit Punkt, mit Apostrophen.

⁠**Kurz gesagt:** Ein Objekt ist ein Wert im Arbeitsspeicher, der die Angabe seiner Art mit sich trägt.

### Der Typ

<span class="anker" id="stufe-1-2"></span>

Bevor Python zwei Werte verknüpft, muss es wissen, was mit ihnen erlaubt ist. Das Pluszeichen bedeutet für zwei Zahlen etwas anderes als für zwei Texte, und für eine Zahl und einen Text bedeutet es gar nichts.

**Die Aufschrift auf dem Kasten.** In Abb. [1](#abb-1) steht auf jedem Kasten, welche Art von Wert er enthält. Diese Aufschrift hat in Python einen eigenen Namen.

:::definition Definition 1.2 (Typ)
<span class="anker" id="satz-1-2"></span>

Der __Typ__ eines Objekts ist die Art seines Werts. Er legt fest, welche Werte das Objekt haben kann und was man mit ihm tun kann. Die Funktion `type` liefert den Typ eines Objekts.
:::

**Beispiel.** Die drei Objekte aus Abb. [1](#abb-1) haben drei verschiedene Typen:

```console
>>> type(42)
<class 'int'>
>>> type(4.0)
<class 'float'>
>>> type("42")
<class 'str'>
```

`<class 'int'>` ist Pythons Schreibweise für „der Typ `int`“; das Wort `class` steht hier für einen Typ. Die drei Namen sind englische Abkürzungen:

| Typ | englisch | Bedeutung | Beispiele |
|---|---|---|---|
| `int` | integer | ganze Zahl | `42`, `-7`, `0` |
| `float` | floating point number | Gleitkommazahl | `4.0`, `0.5`, `2.5e-3` |
| `str` | string | Zeichenkette | `"42"`, `'Ohm'` |

Welchen Typ eine Zahl bekommt, entscheidet allein ihre Schreibweise: Ohne Punkt und ohne `e` ist sie ein `int`, mit Punkt oder mit `e` ein `float`. Deshalb ist auch `4e3` ein `float`, obwohl der Wert 4000 eine ganze Zahl ist:

```console
>>> 4e3
4000.0
>>> type(4e3)
<class 'float'>
```

Was der Typ bewirkt, zeigt das Pluszeichen. Für zwei Objekte vom Typ `int` addiert es, für zwei Objekte vom Typ `str` hängt es die Texte aneinander, und für einen `str` und einen `int` kennt Python keine Regel:

```console
>>> 2 + 3
5
>>> "2" + "3"
'23'
>>> "2" + 3
Traceback (most recent call last):
  File "<python-input-2>", line 1, in <module>
    "2" + 3
    ~~~~^~~
TypeError: can only concatenate str (not "int") to str
```

Die Ausnahme ([Programmieren, Python 1, Abschnitt 6.3](/wissen/informatik/programmieren/python/programme-und-der-python-interpreter/fehler-lesen-und-verstehen.html#stufe-6-3)) hat die Art `TypeError`, auf Deutsch etwa „Typfehler“. Die Beschreibung sagt: An einen `str` kann man nur einen `str` anhängen, keinen `int`. Python wandelt die Zahl 3 also nicht von sich aus in den Text `"3"` um.

⁠**Kurz gesagt:** Der Typ sagt, was für ein Wert in einem Objekt steckt und was man mit ihm tun kann; `type` zeigt ihn an.

:::hintergrund Woher Python beim Ausführen weiß, was das Pluszeichen tun soll
Im Arbeitsspeicher stehen nur Zahlenmuster. Dasselbe Muster kann eine Zahl bedeuten oder eine Folge von Buchstaben, je nachdem, wie man es liest. Deshalb trägt in CPython jedes Objekt einen Verweis auf seinen Typ bei sich, gleich am Anfang seines Speicherbereichs. Trifft die Interpreterschleife ([Programmieren, Python 1, Abschnitt 2.4](/wissen/informatik/programmieren/python/programme-und-der-python-interpreter/vom-quelltext-zur-ausfuhrung-compiler-und-interpreter.html#stufe-2-4)) auf ein Pluszeichen, schaut sie bei beiden Werten nach dem Typ und führt die Additionsregel aus, die zu diesen Typen gehört. Gibt es keine passende Regel, löst sie einen `TypeError` aus.

In der Sprache C ist das anders: Dort schreibt man im Quelltext zu jedem Speicherplatz dazu, welchen Typ er hat, und der Compiler wählt schon beim Übersetzen den passenden Maschinenbefehl. Im fertigen Programm steht der Typ nirgends mehr. Das macht C schneller, weil nichts nachgesehen werden muss. Python bezahlt die Nachfrage bei jeder Rechnung mit Zeit und gewinnt dafür Beweglichkeit: Dieselbe Zeile Quelltext kann einmal mit ganzen Zahlen, einmal mit Gleitkommazahlen und einmal mit Text arbeiten.
:::

### Die Identität

<span class="anker" id="stufe-1-3"></span>

Zwei Objekte können denselben Typ und denselben Wert haben und trotzdem zwei verschiedene Kästen sein. Um sie auseinanderzuhalten, braucht jedes Objekt ein Kennzeichen, das nur es selbst hat.

**Die Platznummer.** In Abb. [1](#abb-1) steht jeder Kasten an einem eigenen Platz. Zwei Kästen mit gleicher Aufschrift und gleichem Inhalt erkennt man an ihren verschiedenen Platznummern.

:::definition Definition 1.3 (Identität)
<span class="anker" id="satz-1-3"></span>

Die __Identität__ eines Objekts ist eine ganze Zahl, die das Objekt von allen anderen Objekten unterscheidet, die zur selben Zeit bestehen. Sie ändert sich nicht, solange das Objekt besteht. Die Funktion `id` liefert sie.
:::

**Beispiel.** Die Identität ist eine lange, zufällig wirkende Zahl:

```console
>>> id(42)
11371408
>>> id("Ohm")
140493353858800
```

Auf deinem Rechner erscheinen andere Zahlen, und beim nächsten Start von Python wieder andere. Das macht nichts: Es kommt nie auf den Zahlenwert an, nur darauf, ob zwei Objekte dieselbe Identität haben.

Bei Zahlen und Zeichenketten bleibt außerdem der Wert eines Objekts für immer derselbe. Eine Rechnung verändert kein vorhandenes Objekt. Sie liefert ein neues Objekt, in dem das Ergebnis steht: `2 + 3` lässt die Objekte 2 und 3 unberührt und liefert ein Objekt mit dem Wert 5.

⁠**Kurz gesagt:** Die Identität ist die feste Nummer eines Objekts; `id` zeigt sie an.

:::hintergrund Was die Nummer in CPython bedeutet
In CPython ist die Identität die Adresse, an der das Objekt im Arbeitsspeicher beginnt. Daher die großen Zahlen. Andere Programme, die Python ausführen, dürfen andere Nummern vergeben; die Sprache verlangt nur, dass die Nummer eindeutig ist und sich nicht ändert.

Eindeutig heißt: eindeutig unter den Objekten, die gleichzeitig bestehen. Ein Objekt, das kein Teil des Programms mehr braucht, gibt CPython wieder frei, und sein Platz kann für ein neues Objekt benutzt werden. Zwei Objekte, die nacheinander bestehen, können deshalb dieselbe Nummer bekommen. Wer Identitäten vergleicht, muss also dafür sorgen, dass beide Objekte noch da sind.
:::

### Die Methode

<span class="anker" id="stufe-1-4"></span>

Manche Fähigkeiten eines Typs passen auf kein Rechenzeichen: einen Text in Großbuchstaben umwandeln oder eine Zahl als Bruch schreiben. Dafür bringt jeder Typ eigene Funktionen mit.

**Funktionen, die zum Kasten gehören.** Eine Funktion ist ein fertiges Teilprogramm mit einem Namen ([Programmieren, Python 1, Abschnitt 4.7](/wissen/informatik/programmieren/python/programme-und-der-python-interpreter/der-interaktive-modus.html#stufe-4-7)). Manche Funktionen hängen an einem Typ wie Knöpfe an einem Gerät: Man drückt sie bei einem bestimmten Objekt, und sie arbeiten mit genau diesem Objekt.

:::definition Definition 1.4 (Methode)
<span class="anker" id="satz-1-4"></span>

Eine __Methode__ ist eine Funktion, die zu einem Typ gehört. Man ruft sie für ein Objekt auf, indem man hinter das Objekt einen Punkt, den Namen der Methode und runde Klammern schreibt.
:::

**Beispiel.** Der Typ `str` hat eine Methode `upper`, die den Text in Großbuchstaben liefert. Der Typ `float` hat eine Methode `as_integer_ratio`, die die Zahl als Bruch aus Zähler und Nenner schreibt:

```console
>>> "Ohm".upper()
'OHM'
>>> (2.5).as_integer_ratio()
(5, 2)
>>> (2.5).upper()
Traceback (most recent call last):
  File "<python-input-2>", line 1, in <module>
    (2.5).upper()
    ^^^^^^^^^^^
AttributeError: 'float' object has no attribute 'upper'
```

Die Antwort `(5, 2)` besteht aus zwei Werten in Klammern: dem Zähler 5 und dem Nenner 2, denn $2{,}5=5/2$. Die letzte Eingabe zeigt, dass jede Methode zu ihrem Typ gehört: Ein `float` hat keine Methode `upper`. Python meldet das als `AttributeError`, auf Deutsch etwa „Merkmalsfehler“: Am Objekt hängt nichts mit dem Namen `upper`. Die Klammern um `2.5` sorgen dafür, dass Python den Punkt vor dem Methodennamen nicht für einen Dezimalpunkt hält. Bei einer ganzen Zahl braucht man sie: Ohne Klammern läse Python `19.` als Anfang der Zahl $19{,}0$.

⁠**Kurz gesagt:** Eine Methode ist eine Funktion eines Typs; man ruft sie mit `objekt.name()` auf.

### Aufgaben zu Abschnitt [1](#stufe-1)

<span class="anker" id="stufe-1-5"></span>

:::aufgabe Aufgabe 1 ★ Typen vorhersagen
<span class="anker" id="aufg-1"></span>

Welchen Typ haben diese Werte? Schreibe zuerst deine Vorhersage auf und prüfe sie dann mit `type`.

(a) `7` (b) `7.0` (c) `"7"` (d) `7e0` (e) `70e-1` (f) `"7.0"` (g) `-0`

:::loesung
Den Typ entscheidet allein die Schreibweise (Unterabschnitt [1.2](#stufe-1-2)):

```console
>>> type(7)
<class 'int'>
>>> type(7.0)
<class 'float'>
>>> type("7")
<class 'str'>
>>> type(7e0)
<class 'float'>
>>> type(70e-1)
<class 'float'>
>>> type("7.0")
<class 'str'>
>>> type(-0)
<class 'int'>
```

(a) Ziffern ohne Punkt: `int`. (b) Punkt: `float`. (c) und (f) In Anführungszeichen steht Text, gleich, wie er aussieht: `str`. (d) und (e) Ein `e` macht die Zahl zum `float`, auch wenn ihr Wert ganz ist: `7e0` und `70e-1` sind beide `7.0`. (g) `-0` ist das einstellige Minus vor der ganzen Zahl 0, also ein `int` mit dem Wert 0.
:::
:::

:::aufgabe Aufgabe 2 ★ Was erlaubt der Typ?
<span class="anker" id="aufg-2"></span>

Sage vorher, was der interaktive Modus anzeigt, und prüfe am Rechner. Erkläre jede Fehlermeldung mit dem Begriff Typ.

<ol class="al">

<li>

`"Ohm" + "meter"`

</li>

<li>

`"Ohm" + 1`

</li>

<li>

`"kilo".upper()`

</li>

<li>

`(0.75).as_integer_ratio()`

</li>

<li>

`(4.0).upper()`

</li>

</ol>

:::loesung
```console
>>> "Ohm" + "meter"
'Ohmmeter'
>>> "Ohm" + 1
Traceback (most recent call last):
  File "<python-input-1>", line 1, in <module>
    "Ohm" + 1
    ~~~~~~^~~
TypeError: can only concatenate str (not "int") to str
>>> "kilo".upper()
'KILO'
>>> (0.75).as_integer_ratio()
(3, 4)
>>> (4.0).upper()
Traceback (most recent call last):
  File "<python-input-4>", line 1, in <module>
    (4.0).upper()
    ^^^^^^^^^^^
AttributeError: 'float' object has no attribute 'upper'
```

(a) Zwei `str`: Für diesen Typ heißt `+` Aneinanderhängen. (b) Für einen `str` und einen `int` hat das Pluszeichen keine Regel; der Typ des rechten Operanden passt nicht, deshalb `TypeError`. (c) `upper` ist eine Methode des Typs `str`. (d) $0{,}75=\frac34$; `as_integer_ratio` ist eine Methode des Typs `float`. (e) Der Typ `float` hat keine Methode `upper`, deshalb `AttributeError`: Welche Methoden es gibt, legt der Typ fest.
:::
:::

:::aufgabe Aufgabe 3 ★★ Wert, Typ, Identität
<span class="anker" id="aufg-3"></span>

Zwei Objekte haben beide den Typ `float` und den Wert $0{,}5$. Erkläre mit dem Bild der Kästen, woran Python sie trotzdem unterscheiden kann. Warum genügt der Wert allein dafür nicht, und warum genügen Wert und Typ zusammen auch nicht?

:::loesung
Im Bild stehen zwei Kästen mit der Aufschrift `float` und dem Inhalt $0{,}5$ an zwei verschiedenen Plätzen. Python unterscheidet sie an ihrer Identität, der Platznummer, die `id` anzeigt. Der Wert allein genügt nicht, weil beide denselben Wert haben; Wert und Typ zusammen genügen auch nicht, weil auch die Typen gleich sind. Nur die Identität ist für jedes Objekt verschieden, solange beide gleichzeitig bestehen. Ob zwei solche Objekte überhaupt getrennt bestehen oder ob Python ein einziges benutzt, entscheidet Python selbst; die Frage nach dem Unterschied stellt sich aber, sobald es zwei sind.
:::
:::

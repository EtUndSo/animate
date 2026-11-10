---
title: Das Newton-Verfahren
pfad: Informatik / Programmieren / Python / Entscheidungen und Schleifen
adresse: informatik/programmieren/python/entscheidungen-und-schleifen
knoten: Kapitel 3: Entscheidungen und Schleifen
order: 6040900
summary: Die Bisektion fragt in jedem Schritt nur nach dem Vorzeichen von f und gewinnt damit ein Bit.
tags: Tangente, Newton-Verfahren, quadratische Konvergenz
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Die Bisektion fragt in jedem Schritt nur nach dem Vorzeichen von $f$ und gewinnt damit ein Bit. Dieser Abschnitt zeigt ein Verfahren, das zusätzlich die Steigung von $f$ benutzt und dadurch die Zahl der gültigen Stellen in jedem Schritt etwa verdoppelt. Es ist das Heron-Verfahren aus [Kapitel 1](/wissen/informatik/programmieren/python/programme-und-der-python-interpreter/programme-und-der-python-interpreter.html), jetzt mit Begründung, warum es so schnell ist und wann es versagt.
:::

:::::vorwissen Was du dafür brauchst: Ableitung und Tangente

<span class="anker" id="stufe-8-1"></span>

Die Ableitung $f'(g)$ einer Funktion an der Stelle $g$ ist die Steigung ihres Graphen dort. Die __Tangente__ an der Stelle $g$ ist die Gerade durch den Punkt $(g, f(g))$ mit dieser Steigung:

$$t(x)=f(g)+f'(g)\,(x-g).$$

In der Nähe von $g$ unterscheidet sich der Graph kaum von seiner Tangente. Für die Wurzel braucht man nur eine Ableitung aus der Schule: Für $f(x)=x^2-a$ mit fester Zahl $a$ ist $f'(x)=2x$.

::::beispiel
Für $f(x)=x^2-2$ an der Stelle $g=2$ ist $f(2)=2$ und $f'(2)=4$, die Tangente also $t(x)=2+4(x-2)$. Sie schneidet die $x$-Achse dort, wo $t(x)=0$ ist: $x=2-2/4=1{,}5$.
::::

⁠**Kurz gesagt:** Die Tangente ist die Gerade, die sich an einer Stelle an den Graphen anschmiegt; ihre Steigung ist die Ableitung.

:::::

### Das Newton-Verfahren

<span class="anker" id="stufe-8-2"></span>

Die Nullstelle einer Kurve ist schwer zu finden, die Nullstelle einer Geraden dagegen leicht. Das Newton-Verfahren ersetzt die Kurve deshalb in jedem Schritt durch ihre Tangente.

**Der Tangente folgen.** Man steht auf dem Graphen über einer Schätzung $g$, legt die Tangente an und folgt ihr bis zur $x$-Achse. Der Schnittpunkt ist die neue Schätzung. Liegt die Schätzung schon nahe der Nullstelle, schmiegt sich die Tangente auf dem ganzen Weg dorthin eng an die Kurve, und man landet sehr nahe an der echten Nullstelle (Abb. [9](#abb-9)).

:::abbildung prog/k3newton 9
Zwei Schritte des Newton-Verfahrens für $f(x)=x^2-2$. Die Tangente bei $g_0=2$ (orange) schneidet die Achse bei $g_1=1{,}5$, die Tangente bei $g_1$ (grün) bei $g_2=1{,}41\overline{6}$. Der rote Punkt ist $\sqrt2\approx1{,}41421$; $g_2$ liegt schon so nahe daran, dass man die beiden Punkte in dieser Darstellung kaum trennen kann.
:::

:::definition Definition 8.1 (Newton-Verfahren)
<span class="anker" id="satz-8-1"></span>

Das __Newton-Verfahren__ für eine Nullstelle einer differenzierbaren Funktion $f$ beginnt mit einem Startwert $g_0$ und berechnet daraus nacheinander

$$g_{n+1}=g_n-\frac{f(g_n)}{f'(g_n)},$$

solange $|f(g_n)|$ größer als eine Toleranz $\varepsilon$ ist. $g_{n+1}$ ist die Nullstelle der Tangente an der Stelle $g_n$; dazu muss $f'(g_n)\ne0$ sein.
:::

Die Formel folgt direkt aus der Tangente: $t(x)=f(g_n)+f'(g_n)(x-g_n)=0$ ergibt $x=g_n-f(g_n)/f'(g_n)$.

::::beispiel
Für $f(x)=x^2-2$ mit $g_0=2$ ist $g_1=1{,}5$ wie in Unterabschnitt [8.1](#stufe-8-1). Im nächsten Schritt ist $f(1{,}5)=0{,}25$ und $f'(1{,}5)=3$, also $g_2=1{,}5-0{,}25/3=1{,}41\overline6$.
::::

⁠**Kurz gesagt:** Das Newton-Verfahren springt in jedem Schritt zur Nullstelle der Tangente.

### Die Wurzel durch Newton

<span class="anker" id="stufe-8-3"></span>

Für $f(g)=g^2-a$ ist $f'(g)=2g$, und der Newton-Schritt lautet

$$g_{n+1}=g_n-\frac{g_n^2-a}{2g_n}=\frac{2g_n^2-g_n^2+a}{2g_n}=\frac12\Bigl(g_n+\frac{a}{g_n}\Bigr).$$

Das ist genau das Heron-Verfahren aus [Kapitel 1, Abschnitte 1.1](/wissen/informatik/programmieren/python/programme-und-der-python-interpreter/programme-und-programmiersprachen.html#stufe-1-1) und [4.5](/wissen/informatik/programmieren/python/programme-und-der-python-interpreter/der-interaktive-modus.html#stufe-4-5): Das alte Rezept für die Wurzel ist das Newton-Verfahren für $x^2-a$. Als Skript mit einer Schleife, die stoppt, sobald $|g^2-a|\le10^{-12}$ ist:

```python wurzel_newton.py
# Quadratwurzel mit dem Newton-Verfahren: g -> g - f(g)/f'(g) mit f(g) = g*g - a und f'(g) = 2*g
a = float(input("a = "))
eps = 1e-12                               # Toleranz für |g*g - a|
g = max(1.0, a)                           # Startwert
schritte = 0
while abs(g * g - a) > eps:
    g = g - (g * g - a) / (2 * g)
    schritte = schritte + 1
    print(f"Schritt {schritte}: g = {g}")
print("Näherung:", g, "nach", schritte, "Schritten")
```

```console Linux
$ python3 wurzel_newton.py
a = 2
Schritt 1: g = 1.5
Schritt 2: g = 1.4166666666666667
Schritt 3: g = 1.4142156862745099
Schritt 4: g = 1.4142135623746899
Schritt 5: g = 1.4142135623730951
Näherung: 1.4142135623730951 nach 5 Schritten
```

Fünf Schritte statt 41. Die richtigen Stellen wachsen sichtbar: eine nach Schritt 1 (`1.5`), drei nach Schritt 2 (`1.416`), sechs nach Schritt 3, zwölf nach Schritt 4, und Schritt 5 trifft den `float`, der $\sqrt2$ am nächsten liegt. Den Startwert $\max(1,a)$ übernimmt das Skript von der Bisektion; er liegt sicher nicht unter der Wurzel.

⁠**Kurz gesagt:** Für die Wurzel ist der Newton-Schritt das Heron-Rezept $\frac12(g+a/g)$, und es braucht für $\sqrt2$ fünf Schritte.

:::hintergrund Warum das Heron-Rezept aus Kapitel 1 eine Stufe daneben landete
In [Kapitel 1, Abschnitt 4.5](/wissen/informatik/programmieren/python/programme-und-der-python-interpreter/der-interaktive-modus.html#stufe-4-5) endete das Rezept in der Form `(g + 2/g) / 2` bei `1.414213562373095`, eine kleinste Stufe neben `2 ** 0.5`. Das Skript hier rechnet mit der Form `g - (g*g - 2)/(2*g)` und hört nach Schritt 5 bei `1.4142135623730951` auf. Beide Formen sind mathematisch gleich, aber sie runden verschieden, so wie zehnmal `+ 0.1` und `* 10` in [Kapitel 2, Abschnitt 5.1](/wissen/informatik/programmieren/python/werte-typen-und-variablen/rechnen-mit-gleitkommazahlen.html#stufe-5-1). Ganz nahe am Ziel kommt bei der zweiten Form etwas hinzu: In `g*g - 2` werden zwei fast gleiche Zahlen voneinander abgezogen, und das Ergebnis besteht fast nur noch aus Rundungsfehlern, wie bei der Auslöschung in [Kapitel 2, Abschnitt 5.4](/wissen/informatik/programmieren/python/werte-typen-und-variablen/rechnen-mit-gleitkommazahlen.html#stufe-5-4). Ließe man diese Form weiterlaufen, spränge $g$ deshalb ohne Ende zwischen `1.4142135623730951` und `1.414213562373095` hin und her; das Skript hat beim Abbruch zufällig den besseren der beiden erwischt. Die Heron-Form bleibt dagegen auf `1.414213562373095` stehen. Bei $\sqrt3$ treffen beide Formen mit dem Abbruch des Skripts den besten Wert. In einem Versuch mit 100 000 Zahlen zwischen 0,01 und 1000 lagen beide Formen nach vielen Schritten nie mehr als eine Stufe neben dem besten `float`; die Newton-Form pendelte in gut einem Viertel der Fälle zwischen zwei Nachbarn. Mehr kann ein Verfahren, das selbst mit gerundeten Zahlen rechnet, kaum versprechen, und Toleranzen wie $10^{-12}$ sind ohnehin viel gröber als eine Stufe.
:::

### Die Konvergenzgeschwindigkeit

<span class="anker" id="stufe-8-4"></span>

Dass sich die Zahl der richtigen Stellen in jedem Schritt etwa verdoppelt, ist kein Zufall der Zahl 2. Man kann es für die Wurzel exakt ausrechnen.

:::satz Satz 8.2 (Fehler des Newton-Schritts für die Wurzel)
<span class="anker" id="satz-8-2"></span>

Sei $a>0$, $g_n>0$ und $g_{n+1}=\frac12(g_n+a/g_n)$. Für die Fehler $d_n=g_n-\sqrt a$ gilt

$$d_{n+1}=\frac{d_n^2}{2g_n}.$$
:::

:::beweis Ausrechnen
$d_{n+1}=\dfrac{g_n^2+a}{2g_n}-\sqrt a=\dfrac{g_n^2-2\sqrt a\,g_n+a}{2g_n}=\dfrac{(g_n-\sqrt a)^2}{2g_n}=\dfrac{d_n^2}{2g_n}$.
:::

Zwei Folgerungen. Erstens ist $d_{n+1}\ge0$: Nach dem ersten Schritt liegt jede Schätzung über $\sqrt a$ oder auf ihr. Zweitens wird der Fehler in jedem Schritt quadriert, bis auf den Faktor $1/(2g_n)$, der nahe der Lösung etwa $1/(2\sqrt a)$ ist. Für den relativen Fehler $\delta_n=d_n/\sqrt a$ folgt daraus mit $g_n\ge\sqrt a$ die Abschätzung $\delta_{n+1}=\delta_n^2\sqrt a/(2g_n)\le\delta_n^2/2$. Ist $\delta_n$ etwa $10^{-p}$, hat $g_n$ also etwa $p$ gültige Dezimalstellen, dann ist $\delta_{n+1}$ höchstens etwa $10^{-2p}/2$: Aus $p$ gültigen Stellen werden etwa $2p$. Diese Eigenschaft heißt __quadratische Konvergenz__.

::::beispiel
Die Fehler des Skripts für $\sqrt2$ mit $g_0=2$, nachgerechnet mit dem Satz:

| $n$ | $d_n=g_n-\sqrt2$ | $d_n^2/(2g_n)$ |
|---|---|---|
| 0 | $0{,}586$ | $0{,}0858$ |
| 1 | $0{,}0858$ | $0{,}00245$ |
| 2 | $0{,}00245$ | $2{,}12\cdot10^{-6}$ |
| 3 | $2{,}12\cdot10^{-6}$ | $1{,}59\cdot10^{-12}$ |
| 4 | $1{,}59\cdot10^{-12}$ | $9\cdot10^{-25}$, kleiner als der Abstand der `float` |

Jede Zeile sagt den Fehler der nächsten richtig voraus. Abb. [10](#abb-10) stellt die drei Verfahren nebeneinander.

:::abbildung prog/k3fehler 10
Fehler über der Zahl der Schritte für $\sqrt2$, logarithmisch aufgetragen. Das Schrittverfahren mit der Schrittweite 0,01 ist nach 42 Schritten kaum näher gekommen. Die Bisektion (Fehler der Mitte nach $n$ Schritten) folgt im Mittel der gestrichelten Geraden: Halbieren ist auf der logarithmischen Achse eine Gerade. Newton fällt immer steiler ab, denn jeder Schritt quadriert den Fehler; nach Schritt 4 lässt sich der Fehler nicht mehr auftragen, weil er null ist.
:::
::::

⁠**Kurz gesagt:** Beim Newton-Verfahren wird der Fehler in jedem Schritt quadriert, die Zahl der gültigen Stellen verdoppelt sich.

:::hintergrund Warum Newton die Stellen verdoppelt
Der Satz gilt nicht nur für die Wurzel. Die Taylorformel mit Restglied, angewandt auf eine zweimal differenzierbare Funktion $f$ an der Stelle $g$, liefert für eine Nullstelle $x^*$

$$0=f(x^*)=f(g)+f'(g)\,(x^*-g)+\tfrac12f''(\xi)\,(x^*-g)^2$$

mit einer Zahl $\xi$ zwischen $g$ und $x^*$. Die Tangente lässt den letzten Summanden weg; ihr Fehler ist also quadratisch im Abstand. Teilt man durch $f'(g)$ und setzt den Newton-Schritt $g'=g-f(g)/f'(g)$ ein, bleibt

$$g'-x^*=\frac{f''(\xi)}{2f'(g)}\,(g-x^*)^2 .$$

Für $f(x)=x^2-a$ ist $f''=2$ und $f'(g)=2g$, und man erhält genau Satz [8.2](#satz-8-2). Der Mechanismus: Das Verfahren ersetzt die Funktion durch eine Gerade, und eine glatte Funktion unterscheidet sich von ihrer Tangente nur um einen Fehler, der mit dem Quadrat des Abstands wächst. Die Bisektion benutzt von $f$ nur das Vorzeichen, ein Bit je Schritt. Newton benutzt den Wert und die Steigung, also viel mehr Information über die Lage der Nullstelle, und gewinnt deshalb mehr. Das gilt, solange $f'(x^*)\ne0$ ist und man nahe genug an der Nullstelle beginnt; was sonst passiert, zeigt der nächste Unterabschnitt.
:::

### Die Grenzen des Newton-Verfahrens

<span class="anker" id="stufe-8-5"></span>

Die Bisektion findet bei einem Vorzeichenwechsel immer eine Nullstelle. Das Newton-Verfahren ist viel schneller, aber es hat keine solche Garantie.

**Die Steigung ist null.** Ist $f'(g)=0$, ist die Tangente waagerecht und schneidet die Achse nicht. Für die Wurzel passiert das beim Startwert $g=0$:

```console
>>> g = 0.0
>>> g - (g * g - 2) / (2 * g)
Traceback (most recent call last):
  File "<python-input-1>", line 1, in <module>
    g - (g * g - 2) / (2 * g)
        ~~~~~~~~~~~~^~~~~~~~~
ZeroDivisionError: division by zero
```

Python 3.13 meldet hier `float division by zero`.

**Ein Kreislauf.** Bei manchen Funktionen und Startwerten springen die Schätzungen hin und her, ohne sich der Nullstelle zu nähern. Für $f(x)=x^3-2x+2$ mit $f'(x)=3x^2-2$ und dem Startwert 0 kehrt das Verfahren nach zwei Schritten zum Start zurück. Die einzige reelle Nullstelle liegt bei etwa $-1{,}77$, weit weg von beiden Werten:

```python newton_zyklus.py
# Newton für f(x) = x**3 - 2*x + 2 mit dem Startwert 0: sechs Schritte
x = 0.0
for schritt in range(1, 7):
    x = x - (x ** 3 - 2 * x + 2) / (3 * x ** 2 - 2)
    print(f"Schritt {schritt}: x = {x}")
```

```console Linux
$ python3 newton_zyklus.py
Schritt 1: x = 1.0
Schritt 2: x = 0.0
Schritt 3: x = 1.0
Schritt 4: x = 0.0
Schritt 5: x = 1.0
Schritt 6: x = 0.0
```

Mit einer `while`-Schleife und der Bedingung $|f(x)|>\varepsilon$ wäre das eine Endlosschleife.

**Eine Toleranz, die nie erreicht wird.** Die Bedingung `abs(g * g - a) > 1e-12` vergleicht mit einer festen Zahl. Für große $a$ sind aber schon die Abstände benachbarter `float` bei $g^2$ größer als $10^{-12}$. Für $a=123456789$ kommt das Verfahren auf einem Wert zur Ruhe, bei dem $g^2-a$ etwa $-1{,}5\cdot10^{-8}$ ist, und der nächste Schritt ändert $g$ nicht mehr:

```console
>>> a = 123456789.0
>>> g = 11111.111060555555
>>> g * g - a
-1.4901161193847656e-08
>>> g - (g * g - a) / (2 * g)
11111.111060555555
```

`wurzel_newton.py` würde für dieses $a$ nie aufhören. Abhilfe ist wie bei der Bisektion eine relative Toleranz, `abs(g * g - a) > 1e-12 * a` ([Kapitel 2, Abschnitt 7.4](/wissen/informatik/programmieren/python/werte-typen-und-variablen/wahrheitswerte-und-vergleiche.html#stufe-7-4)).

**Weit weg ist es langsam.** Quadratische Konvergenz gilt erst nahe der Nullstelle. Für $\sqrt{25}$ mit dem Startwert 25 schrumpft der Fehler in den ersten Schritten nur um einen kleinen Faktor, von 20 auf 8 und dann auf etwa 2,5, bevor die Stellen sich zu verdoppeln beginnen:

```console Linux
$ python3 wurzel_newton.py
a = 25
Schritt 1: g = 13.0
Schritt 2: g = 7.461538461538462
Schritt 3: g = 5.406026962727994
Schritt 4: g = 5.015247601944898
Schritt 5: g = 5.000023178253949
Schritt 6: g = 5.000000000053723
Schritt 7: g = 5.0
Näherung: 5.0 nach 7 Schritten
```

Für $g_n\gg\sqrt a$ ist $\frac12(g_n+a/g_n)\approx g_n/2$: Weit oberhalb der Wurzel halbiert jeder Schritt nur die Schätzung und damit ungefähr auch den Fehler, der dort fast so groß ist wie die Schätzung selbst.

⁠**Kurz gesagt:** Newton braucht eine Ableitung ungleich null, einen Startwert nahe der Lösung und eine passende Toleranz; dann ist es sehr schnell, sonst kann es kreisen, kriechen oder endlos laufen.

### Der fertige Weg: `math.sqrt`

<span class="anker" id="stufe-8-6"></span>

Für die Wurzel selbst schreibt man in der Praxis keine Schleife, sondern ruft `math.sqrt` auf ([Kapitel 2, Abschnitt 8.2](/wissen/informatik/programmieren/python/werte-typen-und-variablen/module-math-und-sys.html#stufe-8-2)). Das folgende Skript stellt die Wege von Hand und den fertigen Weg mit derselben Toleranz nebeneinander:

```python wurzel_vergleich.py
# Wurzel aus 2 von Hand (Bisektion, Newton) und fertig (math.sqrt), mit derselben Toleranz 1e-12
import math
a = 2.0
eps = 1e-12

lo = 0.0                                  # Bisektion
hi = max(1.0, a)
schritte_b = 0
while hi - lo > eps:
    mitte = (lo + hi) / 2
    if mitte * mitte < a:
        lo = mitte
    else:
        hi = mitte
    schritte_b = schritte_b + 1
bisektion = (lo + hi) / 2

g = max(1.0, a)                           # Newton
schritte_n = 0
while abs(g * g - a) > eps:
    g = g - (g * g - a) / (2 * g)
    schritte_n = schritte_n + 1

fertig = math.sqrt(a)                     # fertiger Weg
print(f"Bisektion:  {bisektion}  nach {schritte_b} Schritten, Abstand zu math.sqrt {abs(bisektion - fertig):.1e}")
print(f"Newton:     {g}  nach {schritte_n} Schritten, Abstand zu math.sqrt {abs(g - fertig):.1e}")
print(f"math.sqrt:  {fertig}")
print("Newton == math.sqrt:", g == fertig)
```

```console Linux
$ python3 wurzel_vergleich.py
Bisektion:  1.414213562372879  nach 41 Schritten, Abstand zu math.sqrt 2.2e-13
Newton:     1.4142135623730951  nach 5 Schritten, Abstand zu math.sqrt 0.0e+00
math.sqrt:  1.4142135623730951
Newton == math.sqrt: True
```

Damit ist der Weg „erst von Hand, dann fertig“ für die Wurzel vollständig:

| Verfahren | Aufwand | Ergebnis |
|---|---|---|
| Raten und Prüfen | etwa $\sqrt a$ Schritte | nur ganzzahlige Wurzeln (Unterabschnitt [6.1](losungen-durch-probieren-raten-und-prufen-naherung-mit-toleranz.html#stufe-6-1)) |
| Schrittverfahren | etwa $a/\varepsilon$ Schritte | $\sqrt{25}$: 49 990 Schritte für $\varepsilon=0{,}01$; $\sqrt2$ auf zwölf Stellen: über zwei Tage (Unterabschnitt [6.3](losungen-durch-probieren-raten-und-prufen-naherung-mit-toleranz.html#stufe-6-3)) |
| Bisektion | $\lceil\log_2(L/\varepsilon)\rceil$ Schritte | $\sqrt2$: 41 Schritte, Abweichung $2{,}2\cdot10^{-13}$ (Abschnitt [7](die-bisektion.html#stufe-7)) |
| Newton | wenige Schritte nahe der Lösung | $\sqrt2$: 5 Schritte, genau der `float` von `math.sqrt` (Unterabschnitt [8.3](#stufe-8-3)) |
| `math.sqrt` | ein Aufruf | der `float`, der $\sqrt a$ am nächsten liegt |

Was `math.sqrt` zusätzlich leistet: Es ist für jede Zahl schnell und genau, ohne dass man Startwert, Toleranz oder eine Notbremse wählen muss, und es meldet für negative Zahlen einen Fehler, statt eine Schleife endlos laufen zu lassen.

⁠**Kurz gesagt:** `math.sqrt` liefert in einem Aufruf das Ergebnis, das die Verfahren von Hand nur näherungsweise und mit sorgfältig gewählter Toleranz erreichen.

:::hintergrund Was `math.sqrt` im Prozessor tut
Das Modul `math` reicht die meisten Funktionen an die Mathematikbibliothek der Sprache C weiter. Für die Quadratwurzel haben übliche PC-Prozessoren (x86-64) einen eigenen Befehl, und die C-Bibliothek benutzt ihn. Die Norm IEEE 754 verlangt für die Wurzel dasselbe wie für die vier Grundrechenarten: Das Ergebnis ist der exakte Wert, gerundet auf den nächsten `float` ([Kapitel 2, Abschnitt 5.1](/wissen/informatik/programmieren/python/werte-typen-und-variablen/rechnen-mit-gleitkommazahlen.html#stufe-5-1)). Für $\sqrt2$ lässt sich das nachprüfen: `1.4142135623730951` liegt $9{,}7\cdot10^{-17}$ über $\sqrt2$, der Nachbar `1.414213562373095` $1{,}25\cdot10^{-16}$ darunter. Wie der Befehl intern rechnet, ist Sache des Prozessors. Je nach Bauart bestimmt er die Wurzel Ziffer für Ziffer, ähnlich einer schriftlichen Rechnung, oder mit einer Newton-artigen Iteration, in beiden Fällen mit genug zusätzlichen Stellen, um richtig runden zu können.
:::

### Aufgaben zu Abschnitt [8](#stufe-8)

<span class="anker" id="stufe-8-7"></span>

:::aufgabe Aufgabe 31 ★ Newton von Hand
<span class="anker" id="aufg-31"></span>

Rechne drei Newton-Schritte für $\sqrt3$ mit dem Startwert $g_0=2$ von Hand, als Bruch und als Dezimalzahl. Berechne die Fehler $d_0$ bis $d_3$ und prüfe Satz [8.2](#satz-8-2) für $d_1$ und $d_2$. Wie viele Schritte bräuchte die Bisektion auf $[1,2]$ für dieselbe Genauigkeit wie $g_3$?

:::loesung
Mit $g_{n+1}=\frac12(g_n+3/g_n)$:

$$\begin{aligned} g_1&=\tfrac12\bigl(2+\tfrac32\bigr)=\tfrac74=1{,}75,\\ g_2&=\tfrac12\bigl(\tfrac74+\tfrac{12}7\bigr)=\tfrac{97}{56}\approx1{,}7321429,\\ g_3&=\tfrac12\bigl(\tfrac{97}{56}+\tfrac{168}{97}\bigr)=\tfrac{18817}{10864}\approx1{,}7320508100 . \end{aligned}$$

Mit $\sqrt3=1{,}7320508075\ldots$ sind die Fehler $d_0=0{,}26795$, $d_1=0{,}017949$, $d_2=9{,}205\cdot10^{-5}$ und $d_3=2{,}446\cdot10^{-9}$. Satz [8.2](#satz-8-2): $d_0^2/(2g_0)=0{,}26795^2/4=0{,}017949=d_1$ und $d_1^2/(2g_1)=0{,}017949^2/3{,}5=9{,}205\cdot10^{-5}=d_2$. Die richtigen Stellen wachsen von 0 über 2 und 4 auf 8: `2`, `1.7`, `1.732`, `1.7320508`.

Die Bisektion auf $[1,2]$ liefert eine Mitte mit dem Fehler höchstens $\varepsilon/2$. Für $d_3=2{,}4\cdot10^{-9}$ braucht sie $\varepsilon\le4{,}9\cdot10^{-9}$, also $\lceil\log_2(1/(4{,}9\cdot10^{-9}))\rceil=\lceil27{,}6\rceil=28$ Schritte statt drei.
:::
:::

:::aufgabe Aufgabe 32 ★★ Die Kubikwurzel mit Newton
<span class="anker" id="aufg-32"></span>

Die Kubikwurzel $\sqrt[3]{10}$ ist die Nullstelle von $f(g)=g^3-10$. Leite den Newton-Schritt her, schreibe ein Skript mit dem Startwert 10 und der Abbruchbedingung $|g^3-10|\le10^{-12}\cdot10$, das jeden Schritt ausgibt, und vergleiche mit `10 ** (1/3)`. Ab welchem Schritt verdoppeln sich die Stellen?

:::loesung
Mit $f(g)=g^3-10$ und $f'(g)=3g^2$ ist $g_{n+1}=g_n-\dfrac{g_n^3-10}{3g_n^2}=\dfrac13\Bigl(2g_n+\dfrac{10}{g_n^2}\Bigr)$.

```python kubik_newton.py
# Kubikwurzel aus 10 mit Newton: f(g) = g**3 - a, f'(g) = 3*g**2
a = 10.0
g = a                                     # Startwert
schritte = 0
while abs(g ** 3 - a) > 1e-12 * a:
    g = g - (g ** 3 - a) / (3 * g ** 2)
    schritte = schritte + 1
    print(f"Schritt {schritte}: g = {g}")
print("Vergleich 10 ** (1/3):", a ** (1 / 3))
```

```console Linux
$ python3 kubik_newton.py
Schritt 1: g = 6.7
Schritt 2: g = 4.540922254399644
Schritt 3: g = 3.188937050342083
Schritt 4: g = 2.453741355711228
Schritt 5: g = 2.189459564816151
Schritt 6: g = 2.154991996711556
Schritt 7: g = 2.154434834145626
Schritt 8: g = 2.154434690031893
Vergleich 10 ** (1/3): 2.154434690031884
```

Weit oberhalb der Wurzel nimmt $g$ in jedem Schritt nur um etwa ein Drittel ab, denn für große $g$ ist $\frac13(2g+10/g^2)\approx\frac23g$. Ab Schritt 5 verdoppeln sich die Stellen: Der Fehler sinkt von $3{,}5\cdot10^{-2}$ über $5{,}6\cdot10^{-4}$ und $1{,}4\cdot10^{-7}$ auf etwa $10^{-14}$. Die letzten Stellen unterscheiden sich von `10 ** (1/3)`, weil die Toleranz $|g^3-10|\le10^{-11}$ einen Fehler von etwa $10^{-12}$ in $g$ zulässt; das Ergebnis erfüllt die verlangte Genauigkeit.
:::
:::

:::aufgabe Aufgabe 33 ★★ Newton mit relativer Toleranz
<span class="anker" id="aufg-33"></span>

Ändere `wurzel_newton.py` so, dass die Bedingung `abs(g * g - a) > 1e-12 * a` lautet und nur das Endergebnis ausgegeben wird. Teste mit $a=2$, $a=25$, $a=123456789$ und $a=0{,}0001$. Wie viele Schritte braucht es jeweils? Warum braucht $a=0{,}0001$ trotz kleiner Zahl einige Schritte mehr?

:::loesung
```python newton_relativ.py
# Newton für die Wurzel mit relativer Toleranz: endet auch für große und kleine a
a = float(input("a = "))
g = max(1.0, a)
schritte = 0
while abs(g * g - a) > 1e-12 * a:
    g = g - (g * g - a) / (2 * g)
    schritte = schritte + 1
print("Näherung:", g, "nach", schritte, "Schritten")
```

```console Linux
$ python3 newton_relativ.py
a = 2
Näherung: 1.4142135623730951 nach 5 Schritten
$ python3 newton_relativ.py
a = 25
Näherung: 5.0 nach 7 Schritten
$ python3 newton_relativ.py
a = 123456789
Näherung: 11111.111060555555 nach 18 Schritten
$ python3 newton_relativ.py
a = 0.0001
Näherung: 0.01 nach 11 Schritten
```

Für $a=123456789$ endet die Schleife jetzt: Die erlaubte Abweichung ist $10^{-12}\cdot a\approx1{,}2\cdot10^{-4}$, viel mehr als die $1{,}5\cdot10^{-8}$, die übrig bleiben. Die 18 Schritte kommen vom Startwert $a$, der weit über der Wurzel liegt; die ersten Schritte halbieren nur. Für $a=0{,}0001$ ist der Startwert 1 hundertmal so groß wie die Wurzel 0,01. Auch hier halbieren die ersten Schritte nur, etwa $\log_2 100\approx7$-mal, bevor die quadratische Konvergenz einsetzt.
:::
:::

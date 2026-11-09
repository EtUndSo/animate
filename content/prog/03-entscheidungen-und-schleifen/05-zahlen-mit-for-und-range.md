---
title: Zählen mit for und range
pfad: Informatik / Programmieren / Python / Entscheidungen und Schleifen
knoten: Python 3: Entscheidungen und Schleifen
order: 6040500
summary: Oft steht schon vor der ersten Wiederholung fest, wie viele es werden: für jeden von acht Messkanälen, für jeden Widerstand einer Reihe.
tags: for-Schleife, Schleifenvariable
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Oft steht schon vor der ersten Wiederholung fest, wie viele es werden: für jeden von acht Messkanälen, für jeden Widerstand einer Reihe. Mit `while` braucht man dafür einen Zähler, eine Bedingung und eine Zeile, die den Zähler erhöht, und vergisst man die letzte, läuft die Schleife endlos. Dieser Abschnitt führt eine Schleife ein, die das Zählen selbst übernimmt, und die Zahlenfolgen, die sie durchläuft.
:::

### Die `for`-Schleife

<span class="anker" id="stufe-4-1"></span>

Eine Schleife, die eine feste Folge von Werten abarbeitet, braucht keine eigene Bedingung: Sie endet, wenn die Folge zu Ende ist.

**Ein Stufenschalter.** Man kann sich einen Stufenschalter vorstellen, der Stellung für Stellung weiterdreht: Bei jeder Stellung passiert dasselbe, und nach der letzten Stellung ist Schluss. Ein Name zeigt jeweils die aktuelle Stellung an.

:::definition Definition 4.1 (`for`-Schleife)
<span class="anker" id="satz-4-1"></span>

Eine __`for`-Schleife__ hat die Form

`for name in range(n):` ` Block`

Dabei liefert `range(n)` für eine ganze Zahl $n$ die ganzen Zahlen $0, 1, \ldots, n-1$ der Reihe nach. Die Schleife bindet `name` nacheinander an jede dieser Zahlen und führt jedes Mal den Block aus; nach der letzten Zahl geht es nach dem Block weiter. Der Name heißt die __Schleifenvariable__. Allgemein steht nach `in` ein Objekt, das der Reihe nach Werte liefert; in diesem Abschnitt ist es immer ein `range`.
:::

**Beispiel.** Die ersten Zweierpotenzen:

```python zweierpotenzen.py
# Zweierpotenzen mit einer for-Schleife
for k in range(5):
    print(k, 2 ** k)
print("fertig")
```

```console Linux
$ python3 zweierpotenzen.py
0 1
1 2
2 4
3 8
4 16
fertig
```

Mit `while` braucht dieselbe Schleife drei Zeilen mehr: `k = 0` vor der Schleife, die Bedingung `k < 5` und `k = k + 1` am Ende des Blocks. Die `for`-Schleife erledigt alle drei.

⁠**Kurz gesagt:** `for k in range(n):` führt den Block für $k=0,1,\ldots,n-1$ aus.

### Die Zahlenfolge `range`

<span class="anker" id="stufe-4-2"></span>

Nicht jede Folge beginnt bei 0 und geht in Einerschritten: Widerstände von 100 $\Omega$ bis 500 $\Omega$ in Schritten von 100 $\Omega$, ein Countdown von 10 abwärts.

**Marken auf dem Zahlenstrahl.** Man setzt auf dem Zahlenstrahl eine erste Marke beim Start und dann weitere im festen Abstand, bis man die Stopp-Marke erreicht oder überschreitet. Die Stopp-Marke selbst gehört nicht dazu (Abb. [5](#abb-5)).

:::abbildung prog/k3range 5
Die Folge `range(2, 11, 3)`: Sie beginnt beim Start 2, geht in Schritten von 3 weiter und hört vor dem Stopp 11 auf. Die nächste Marke wäre 11 selbst; der Stopp gehört nie zur Folge.
:::

:::definition Definition 4.2 (`range`)
<span class="anker" id="satz-4-2"></span>

`range` gibt es mit einem, zwei oder drei ganzzahligen Argumenten: `range(stop)`, `range(start, stop)` und `range(start, stop, schritt)`. Fehlt `start`, ist er 0; fehlt `schritt`, ist er 1. Die Folge besteht aus den Zahlen $\mathtt{start}$, $\mathtt{start}+\mathtt{schritt}$, $\mathtt{start}+2\cdot\mathtt{schritt}$, …, solange sie bei positivem Schritt kleiner als `stop` und bei negativem Schritt größer als `stop` sind. `stop` selbst gehört nie dazu. Ist schon `start` nicht mehr vor `stop`, ist die Folge leer. `len` liefert die Zahl der Elemente, für positiven Schritt

$$\mathtt{len}=\max\Bigl(0,\Bigl\lceil\frac{\mathtt{stop}-\mathtt{start}}{\mathtt{schritt}}\Bigr\rceil\Bigr).$$
:::

**Beispiel.** Der Zusatz `end=" "` in `print`, mit Namen übergeben, schreibt am Ende ein Leerzeichen statt eines Zeilenwechsels. So steht jede Folge in einer Zeile, und `print()` ohne Werte beendet die Zeile:

```python range_folgen.py
# Welche Zahlen liefert range? Jede Zeile zeigt eine Folge, end=" " hält sie in einer Zeile.
for i in range(5):
    print(i, end=" ")
print()
for i in range(2, 6):
    print(i, end=" ")
print()
for i in range(2, 10, 3):
    print(i, end=" ")
print()
for i in range(10, 0, -3):
    print(i, end=" ")
print()
for i in range(5, 5):
    print(i, end=" ")
print("(leer)")
```

```console Linux
$ python3 range_folgen.py
0 1 2 3 4
2 3 4 5
2 5 8
10 7 4 1
(leer)
```

Im interaktiven Modus zeigt Python ein `range` nur mit seinen Grenzen an, die Zahl der Elemente liefert `len`. Nur ganze Zahlen sind erlaubt, und der Schritt darf nicht 0 sein:

```console
>>> range(5)
range(0, 5)
>>> len(range(2, 10, 3))
3
>>> len(range(0, 100, 7))
15
>>> range(0.5)
Traceback (most recent call last):
  File "<python-input-3>", line 1, in <module>
    range(0.5)
    ~~~~~^^^^^
TypeError: 'float' object cannot be interpreted as an integer
>>> range(1, 10, 0)
Traceback (most recent call last):
  File "<python-input-4>", line 1, in <module>
    range(1, 10, 0)
    ~~~~~^^^^^^^^^^
ValueError: range() arg 3 must not be zero
```

`len(range(0, 100, 7))` ist $\lceil100/7\rceil=\lceil14{,}29\rceil=15$: die Zahlen 0, 7, 14, …, 98.

Eine Tabelle von Strömen für Widerstände von 100 $\Omega$ bis 500 $\Omega$ braucht als Stopp 501, damit 500 noch dazugehört:

```python strom_tabelle.py
# Strom durch verschiedene Widerstände an 5 V
u = 5.0
for r in range(100, 501, 100):
    print(f"R = {r} Ohm   I = {u / r * 1000:4.1f} mA")
```

```console Linux
$ python3 strom_tabelle.py
R = 100 Ohm   I = 50.0 mA
R = 200 Ohm   I = 25.0 mA
R = 300 Ohm   I = 16.7 mA
R = 400 Ohm   I = 12.5 mA
R = 500 Ohm   I = 10.0 mA
```

Der häufigste Fehler mit `range` ist genau dieser: `range(1, 10)` liefert 1 bis 9, nicht 1 bis 10.

⁠**Kurz gesagt:** `range(start, stop, schritt)` zählt von `start` in Schritten bis vor `stop`; der Stopp gehört nie dazu.

:::hintergrund Warum der Stopp nicht zur Folge gehört
Ein Bereich, der die untere Grenze einschließt und die obere ausschließt, hat zwei angenehme Eigenschaften. Erstens ist seine Länge die Differenz der Grenzen: `range(a, b)` hat genau $b-a$ Elemente, und `range(n)` hat genau $n$. Zweitens schließen zwei solche Bereiche lückenlos und ohne Überschneidung aneinander an: `range(0, 5)` und `range(5, 10)` ergeben zusammen genau `range(0, 10)`, und die gemeinsame Grenze 5 kommt genau einmal vor. Der Informatiker Edsger Dijkstra hat 1982 begründet, warum man Folgen deshalb am besten bei 0 beginnen und mit $0\le i<n$ beschreiben sollte: Schlösse man die untere Grenze aus, müsste ein Bereich, der bei der kleinsten natürlichen Zahl 0 beginnt, mit der Grenze $-1$ geschrieben werden, also mit einer Zahl außerhalb der natürlichen Zahlen. Python folgt dieser Wahl bei `range` und überall, wo Bereiche vorkommen.
:::

:::hintergrund Was ein `range` im Speicher ablegt
Ein `range` legt seine Zahlen nicht ab. Es speichert nur drei Zahlen, Start, Stopp und Schritt, und rechnet jedes Element erst aus, wenn die Schleife es braucht, als $\mathtt{start}+k\cdot\mathtt{schritt}$. Deshalb braucht `range(10 ** 15)` nicht mehr Speicher als `range(5)`, und `len` rechnet die Zahl der Elemente mit der Formel aus, statt zu zählen:

```console
>>> len(range(10 ** 15))
1000000000000000
```
:::

### Gleitkomma-Schritte über einen ganzzahligen Zähler

<span class="anker" id="stufe-4-3"></span>

Eine Zeitachse soll die Zeitpunkte 0 ms, 0,1 ms, …, 1 ms durchlaufen. `range` nimmt aber nur ganze Zahlen an.

Die Lösung ist dieselbe wie bei der Gleitkomma-Falle in Unterabschnitt [3.3](wiederholen-mit-while.html#stufe-3-3): Die Schleife zählt mit einer ganzen Zahl $k$, und den Zeitpunkt berechnet man in jedem Durchlauf neu als $t_k=k\cdot\Delta t$, hier als `k / 10`. Das folgende Skript stellt beide Wege nebeneinander, das fortgesetzte Addieren und die Rechnung aus dem Zähler:

```python zeitachse.py
# Zeitpunkte 0 ms, 0.1 ms, ..., 1 ms: einmal aufaddiert, einmal aus dem ganzzahligen Zähler
t = 0.0
for k in range(11):
    print(k, t, k / 10)
    t = t + 0.1
```

```console Linux
$ python3 zeitachse.py
0 0.0 0.0
1 0.1 0.1
2 0.2 0.2
3 0.30000000000000004 0.3
4 0.4 0.4
5 0.5 0.5
6 0.6 0.6
7 0.7 0.7
8 0.7999999999999999 0.8
9 0.8999999999999999 0.9
10 0.9999999999999999 1.0
```

Die mittlere Spalte sammelt die Rundungsfehler auf, die rechte trifft jeden Zeitpunkt so genau, wie ein `float` ihn überhaupt darstellen kann. [Programmieren, Python 2, Abschnitt 5](/wissen/informatik/programmieren/python/werte-typen-und-variablen/rechnen-mit-gleitkommazahlen.html#stufe-5) hat in einer Aufgabe dieselbe Beobachtung mit dem interaktiven Modus gemacht; mit der Schleife sieht man alle Zeitpunkte auf einmal.

⁠**Kurz gesagt:** Für Schritte mit Gleitkommazahlen zählt `range` ganzzahlig, und den Wert berechnet man aus dem Zähler.

### `for` oder `while`?

<span class="anker" id="stufe-4-4"></span>

Beide Schleifen wiederholen einen Block. Welche man nimmt, hängt davon ab, was man vor dem ersten Durchlauf weiß.

|  | `for k in range(…)` | `while Bedingung` |
|---|---|---|
| wann geeignet | Zahl der Durchläufe steht vorher fest | Ziel steht fest, Zahl der Durchläufe nicht |
| wie sie endet | nach dem letzten Wert der Folge | wenn die Bedingung falsch ist |
| Gefahr | keine Endlosschleife möglich | endlos, wenn der Block die Bedingung nicht ändert |
| Beispiel | Tabelle für 5 Widerstände | Kondensator bis 1 % entladen |

Ein Unterschied überrascht oft: Bindet man in einer `for`-Schleife die Schleifenvariable an einen anderen Wert, hat das auf den nächsten Durchlauf keine Wirkung, denn die Schleife bindet den Namen jedes Mal neu an den nächsten Wert aus dem `range`.

```python schleifenvariable.py
# Wer in der Schleife die Schleifenvariable ändert, ändert nicht die Folge
for i in range(3):
    print("Anfang des Durchlaufs:", i)
    i = 100
    print("nach i = 100:", i)
```

```console Linux
$ python3 schleifenvariable.py
Anfang des Durchlaufs: 0
nach i = 100: 100
Anfang des Durchlaufs: 1
nach i = 100: 100
Anfang des Durchlaufs: 2
nach i = 100: 100
```

Die Zuweisung `i = 100` ändert nur, woran der Name im laufenden Durchlauf gebunden ist; das `range` liefert trotzdem 1 und dann 2.

⁠**Kurz gesagt:** `for`, wenn die Folge der Werte vorher feststeht; `while`, wenn nur das Ziel feststeht.

### Aufgaben zu Abschnitt [4](#stufe-4)

<span class="anker" id="stufe-4-5"></span>

:::aufgabe Aufgabe 15 ★ Folgen vorhersagen
<span class="anker" id="aufg-15"></span>

Schreibe für jedes `range` die Zahlen auf, die es liefert, und ihre Anzahl. Prüfe die Anzahl mit `len` und die Zahlen mit einer Schleife wie in `range_folgen.py`. (a) `range(4)`, (b) `range(1, 4)`, (c) `range(0, 10, 2)`, (d) `range(10, 0, -2)`, (e) `range(3, 3)`, (f) `range(0, 1, 5)`, (g) `range(-3, 3)`.

:::loesung
(a) 0, 1, 2, 3: vier Zahlen. (b) 1, 2, 3: drei. (c) 0, 2, 4, 6, 8: fünf. (d) 10, 8, 6, 4, 2: fünf, die 0 gehört als Stopp nicht dazu. (e) leer. (f) nur die 0: eine Zahl, denn $0+5$ liegt schon über dem Stopp. (g) $-3$ bis 2: sechs Zahlen.

```console
>>> len(range(4))
4
>>> len(range(1, 4))
3
>>> len(range(0, 10, 2))
5
>>> len(range(10, 0, -2))
5
>>> len(range(3, 3))
0
>>> len(range(0, 1, 5))
1
>>> len(range(-3, 3))
6
```

Für positive Schritte bestätigt die Formel aus Unterabschnitt [4.2](#stufe-4-2) jede Zahl, etwa (f): $\lceil(1-0)/5\rceil=\lceil0{,}2\rceil=1$.
:::
:::

:::aufgabe Aufgabe 16 ★★ Eine Leistungstabelle
<span class="anker" id="aufg-16"></span>

Schreibe ein Skript, das für $U=12$ V und die Widerstände 100 $\Omega$, 200 $\Omega$, …, 1000 $\Omega$ die Leistung $P=U^2/R$ in Watt mit zwei Nachkommastellen ausgibt, eine Zeile je Widerstand. Welche Argumente braucht `range`?

:::loesung
Der Stopp muss über 1000 liegen, damit 1000 noch dazugehört: `range(100, 1001, 100)`.

```python leistung_tabelle.py
# Leistung P = U*U/R an 12 V für R = 100 Ohm bis 1000 Ohm
u = 12.0
for r in range(100, 1001, 100):
    print(f"R = {r:4d} Ohm   P = {u * u / r:.2f} W")
```

```console Linux
$ python3 leistung_tabelle.py
R =  100 Ohm   P = 1.44 W
R =  200 Ohm   P = 0.72 W
R =  300 Ohm   P = 0.48 W
R =  400 Ohm   P = 0.36 W
R =  500 Ohm   P = 0.29 W
R =  600 Ohm   P = 0.24 W
R =  700 Ohm   P = 0.21 W
R =  800 Ohm   P = 0.18 W
R =  900 Ohm   P = 0.16 W
R = 1000 Ohm   P = 0.14 W
```

Die Formatangabe `4d` hält die Widerstände rechtsbündig in vier Stellen, sodass die Spalten untereinanderstehen ([Programmieren, Python 2, Abschnitt 10.2](/wissen/informatik/programmieren/python/werte-typen-und-variablen/zeichenketten-eingabe-und-ausgabe.html#stufe-10-2)).
:::
:::

:::aufgabe Aufgabe 17 ★★ Eine Sekunde Audio
<span class="anker" id="aufg-17"></span>

Ein Audiosignal wird mit 48 kHz abgetastet, die Abtastzeitpunkte sind $t_k=k/48000$ s. Berechne $t_{48000}$, das genau 1 s sein sollte, auf drei Wegen: (a) mit einer Schleife, die 48 000-mal `1 / 48000` zu `t` addiert, (b) als `48000 * (1 / 48000)`, (c) als `48000 / 48000`. Welche Wege treffen 1,0 genau? Erkläre den Unterschied mit der Zahl der Rundungen.

:::loesung
```python audio.py
# Eine Sekunde bei 48 kHz: den letzten Abtastzeitpunkt auf drei Wegen berechnen
t = 0.0
for k in range(48000):
    t = t + 1 / 48000
print("aufaddiert:   ", t)
print("48000 * (1/48000):", 48000 * (1 / 48000))
print("48000 / 48000:", 48000 / 48000)
```

```console Linux
$ python3 audio.py
aufaddiert:    1.000000000000893
48000 * (1/48000): 1.0
48000 / 48000: 1.0
```

(a) trifft 1 nicht: In jeder der 48 000 Additionen wird gerundet, und die Fehler häufen sich auf etwa $9\cdot10^{-13}$. (b) enthält zwei Rundungen, eine beim Bilden von `1 / 48000` und eine beim Multiplizieren. Hier gleichen sie sich so aus, dass genau 1,0 herauskommt; garantiert ist das nicht, `49 * (1 / 49)` ergibt zum Beispiel `0.9999999999999999`. (c) ist eine einzige, exakte Rechnung. Am sichersten berechnet man jeden Zeitpunkt deshalb als `k / 48000`: eine Rundung je Wert, nie aufgehäuft.
:::
:::

:::aufgabe Aufgabe 18 ★★ Schleifen umschreiben
<span class="anker" id="aufg-18"></span>

<ol class="al">

<li>

Schreibe `zaehlen.py` aus Unterabschnitt [3.1](wiederholen-mit-while.html#stufe-3-1) mit einer `for`-Schleife. Was gibt deine Fassung als letzten Wert des Zählers aus, und warum unterscheidet er sich von der `while`-Fassung?

</li>

<li>

Schreibe die Schleife `for i in range(10, 0, -3):` mit `print(i)` im Block als `while`-Schleife.

</li>

</ol>

:::loesung
(a)

```python zaehlen_for.py
# zaehlen.py mit einer for-Schleife
for zaehler in range(1, 4):
    print("Durchlauf", zaehler)
print("fertig, zaehler =", zaehler)
```

```console Linux
$ python3 zaehlen_for.py
Durchlauf 1
Durchlauf 2
Durchlauf 3
fertig, zaehler = 3
```

Die `for`-Schleife bindet `zaehler` zuletzt an 3, den letzten Wert aus dem `range`, und erhöht ihn nicht weiter. Die `while`-Fassung erhöht den Zähler am Ende jedes Durchlaufs, auch des letzten, und endet erst, wenn die Prüfung mit dem Wert 4 fehlschlägt.

(b) Start vor der Schleife, Bedingung „noch über dem Stopp“, Schritt am Ende des Blocks:

```python countdown_while.py
# for i in range(10, 0, -3): print(i)  als while-Schleife
i = 10
while i > 0:
    print(i)
    i = i - 3
```

```console Linux
$ python3 countdown_while.py
10
7
4
1
```

Bei negativem Schritt heißt die Bedingung `i > 0`, nicht `i < 0`: Die Folge läuft, solange sie über dem Stopp liegt.
:::
:::

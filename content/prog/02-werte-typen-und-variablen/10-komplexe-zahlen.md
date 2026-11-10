---
title: Komplexe Zahlen
pfad: Informatik / Programmieren / Python / Werte, Typen und Variablen
adresse: informatik/programmieren/python/werte-typen-und-variablen
knoten: Kapitel 2: Werte, Typen und Variablen
order: 6031000
summary: Mit komplexen Zahlen haben auch negative Zahlen eine Wurzel, und jeder Punkt der Ebene wird zu einer einzigen Zahl, mit der man rechnen kann.
tags: Attribut
lang: de
---

<span class="anker" id="stufe-9"></span>

:::zweck
Mit komplexen Zahlen haben auch negative Zahlen eine Wurzel, und jeder Punkt der Ebene wird zu einer einzigen Zahl, mit der man rechnen kann. Dieser Abschnitt zeigt, wie Python komplexe Zahlen speichert, wie man Betrag und Phase von Hand und fertig bestimmt, und dreht zum Schluss einen Punkt in der Ebene mit einer einzigen Multiplikation.
:::

:::::vorwissen Was du dafür brauchst: komplexe Zahlen

<span class="anker" id="stufe-9-1"></span>

Dieser Unterabschnitt stellt zusammen, was das Kapitel aus der Mathematik der komplexen Zahlen benutzt; ausführlich steht es in [HöMa1, Kapitel 2](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/komplexe-zahlen/komplexe-zahlen.html).

**Real- und Imaginärteil.** Eine komplexe Zahl $z=x+\mathrm jy$ besteht aus dem Realteil $x=\operatorname{Re}z$ und dem Imaginärteil $y=\operatorname{Im}z$, beides reelle Zahlen. Für die imaginäre Einheit gilt $\mathrm j^2=-1$. Die Mathematik schreibt sie meist $i$; das Kapitel schreibt $\mathrm j$, weil Python es so schreibt.

**Die komplexe Ebene.** Man trägt $x$ nach rechts und $y$ nach oben auf. Dann ist $z$ ein Punkt der Ebene, oder ein Pfeil vom Nullpunkt zu diesem Punkt. Die zu $z$ *konjugiert komplexe* Zahl $z^*=x-\mathrm jy$ ist ihr Spiegelbild an der waagerechten Achse.

**Betrag und Phase.** Der Betrag $|z|=\sqrt{x^2+y^2}$ ist die Länge des Pfeils. Die Phase $\varphi$, auch Argument genannt, ist der Winkel des Pfeils gegen die positive reelle Achse, gegen den Uhrzeigersinn positiv, mit $-\pi<\varphi\le\pi$. Es gilt $\tan\varphi=y/x$, aber $\arctan(y/x)$ liefert nur Winkel zwischen $-\frac\pi2$ und $\frac\pi2$; liegt $z$ links der senkrechten Achse, muss man $\pi$ addieren oder abziehen.

**Polarform.** Mit der Eulerschen Formel $\mathrm{e}^{\mathrm j\varphi}=\cos\varphi+\mathrm j\sin\varphi$ ist $z=|z|\,\mathrm{e}^{\mathrm j\varphi}$. Beim Multiplizieren multiplizieren sich die Beträge, und die Phasen addieren sich; beim Dividieren teilen sich die Beträge, und die Phasen subtrahieren sich.

::::beispiel
$z=3+4\mathrm j$ hat $|z|=\sqrt{9+16}=5$ und $\varphi=\arctan\frac43\approx0{,}9273\approx53{,}13^\circ$. Es ist $z^*=3-4\mathrm j$ und $z\cdot z^*=9+16=25=|z|^2$.
::::

⁠**Kurz gesagt:** $z=x+\mathrm jy=|z|\,\mathrm{e}^{\mathrm j\varphi}$ mit $|z|=\sqrt{x^2+y^2}$ und der Phase $\varphi$ als Winkel des Pfeils.

:::::

### Der Typ `complex`

<span class="anker" id="stufe-9-2"></span>

Ein Punkt der Ebene hat zwei Koordinaten, eine komplexe Zahl zwei Teile. Python braucht einen Typ, der beide zusammen als eine Zahl speichert und mit ihr nach den Regeln der komplexen Rechnung rechnet.

**Ein Paar von Gleitkommazahlen.** Python speichert eine komplexe Zahl als zwei `float` nebeneinander, den Realteil und den Imaginärteil, und schreibt die imaginäre Einheit als `j`.

:::definition Definition 9.1 (Der Typ `complex`)
<span class="anker" id="satz-9-1"></span>

Ein Objekt vom Typ `complex` speichert eine komplexe Zahl als Paar zweier `float`, Realteil und Imaginärteil. Eine Zahl mit einem angehängten `j` ist imaginär: `4j` bedeutet $4\mathrm j$. Die Funktion `complex(x, y)` erzeugt $x+\mathrm jy$.
:::

::::beispiel
`3 + 4j` ist eine Rechnung: `int` plus imaginäre Zahl ergibt `complex`. Python zeigt komplexe Zahlen in Klammern:

```console
>>> z = 3 + 4j
>>> z
(3+4j)
>>> type(z)
<class 'complex'>
>>> complex(3, 4)
(3+4j)
>>> 1j * 1j
(-1+0j)
>>> (1 + 2j) * (3 - 4j)
(11+2j)
>>> (1 + 2j) / (3 - 4j)
(-0.2+0.4j)
>>> j
Traceback (most recent call last):
  File "<python-input-7>", line 1, in <module>
    j
NameError: name 'j' is not defined
```

Die letzte Eingabe zeigt eine Falle: `j` allein ist für Python ein Name, keine Zahl. Die imaginäre Einheit schreibt man `1j`. Die Grundrechenarten und `**` funktionieren mit `complex`; Ganzzahldivision, Rest und die Vergleiche `<` und `>` gibt es nicht, weil komplexe Zahlen keine Reihenfolge haben.
::::

⁠**Kurz gesagt:** `complex` speichert Real- und Imaginärteil als zwei `float`; die imaginäre Einheit heißt `1j`.

:::hintergrund Warum Python `j` schreibt und nicht `i`
Die Mathematik schreibt meist $i$, die Ingenieurwissenschaften und Teile der Physik schreiben $\mathrm j$, weil dort $i$ schon für eine andere Größe vergeben ist. Python folgt diesen Fächern; Entwickler der Sprache begründeten das in der Diskussion über einen Änderungswunsch damit, dass diese Schreibweise dort seit Langem üblich ist und eine Umstellung bestehende Programme brechen würde. Statt `j` darf man auch `J` schreiben, `i` dagegen nicht.
:::

### Das Attribut: Real- und Imaginärteil

<span class="anker" id="stufe-9-3"></span>

Aus einer komplexen Zahl will man oft den Real- oder den Imaginärteil allein haben, etwa die waagerechte Koordinate eines Punkts. Dafür braucht man keine Rechnung: Beide Teile stehen fertig im Objekt.

**Was am Objekt hängt.** Eine Methode hängt an einem Objekt und wird mit Punkt und Klammern aufgerufen (Unterabschnitt [1.4](objekte-und-typen.html#stufe-1-4)). Es können aber auch einfache Werte am Objekt hängen, die man ohne Klammern abliest.

:::definition Definition 9.2 (Attribut)
<span class="anker" id="satz-9-2"></span>

Ein __Attribut__ ist ein Name, der an einem Objekt hängt und mit einem Punkt abgerufen wird: *objekt*`.`*name*. Methoden sind Attribute, die man aufruft; andere Attribute sind einfach Werte.
:::

Daher kommt der Name der Ausnahme `AttributeError` aus Unterabschnitt [1.4](objekte-und-typen.html#stufe-1-4): Am Objekt hing kein Attribut mit dem gesuchten Namen.

::::beispiel
`real` und `imag` sind Attribute mit den beiden Teilen als `float`; `conjugate` ist eine Methode und liefert die konjugiert komplexe Zahl:

```console
>>> z.real
3.0
>>> z.imag
4.0
>>> z.conjugate()
(3-4j)
>>> z * z.conjugate()
(25+0j)
>>> z.real = 5
Traceback (most recent call last):
  File "<python-input-12>", line 1, in <module>
    z.real = 5
    ^^^^^^
AttributeError: readonly attribute
```

Die letzte Zeile zeigt: Die Attribute lassen sich nur lesen. Ein `complex` ändert seinen Wert nie, so wie jede Zahl (Unterabschnitt [1.3](objekte-und-typen.html#stufe-1-3)).
::::

⁠**Kurz gesagt:** Ein Attribut ist ein Name am Objekt; `z.real` und `z.imag` liefern Real- und Imaginärteil.

### Das Modul `cmath`

<span class="anker" id="stufe-9-4"></span>

Die Funktionen aus `math` arbeiten nur mit reellen Zahlen. `math.sqrt(-1)` ist deshalb ein Fehler, obwohl $\sqrt{-1}=\mathrm j$ eine vernünftige Antwort wäre.

**Ein zweiter Werkzeugkasten.** Für komplexe Zahlen gibt es ein eigenes Modul mit denselben Funktionsnamen. Weil jedes Modul seine eigenen Namen hat, können `math.sqrt` und `cmath.sqrt` nebeneinander bestehen.

:::definition Definition 9.3 (Das Modul `cmath`)
<span class="anker" id="satz-9-3"></span>

Das Modul `cmath` enthält mathematische Funktionen für komplexe Zahlen, darunter `sqrt`, `exp`, `log`, `sin`, `cos` sowie `phase`, `polar` und `rect` für die Polarform. Die Rechenfunktionen liefern ein `complex`; `phase` liefert einen `float` und `polar` zwei `float`.
:::

::::beispiel
Mit `math` scheitert die Wurzel aus $-1$:

```console
>>> import math
>>> math.sqrt(-1)
Traceback (most recent call last):
  File "<python-input-1>", line 1, in <module>
    math.sqrt(-1)
    ~~~~~~~~~^^^^
ValueError: expected a nonnegative input, got -1.0
```

Unter Python 3.13 lautet die Beschreibung kürzer `math domain error`. Mit `cmath` gelingt sie, ebenso die Eulersche Formel für $\varphi=\pi$. Die Sitzung mit `z` geht dabei weiter:

```console
>>> import math
>>> import cmath
>>> cmath.sqrt(-1)
1j
>>> cmath.exp(1j * math.pi)
(-1+1.2246467991473532e-16j)
>>> (-1) ** 0.5
(6.123233995736766e-17+1j)
```

$\mathrm{e}^{\mathrm j\pi}$ ist $-1$; der Imaginärteil $1{,}22\cdot10^{-16}$ ist der Rundungsrest von `math.pi`, derselbe wie bei `math.sin(math.pi)` in Unterabschnitt [8.2](module-math-und-sys.html#stufe-8-2). Die letzte Zeile ist eine Falle: Eine negative Zahl hoch einen nicht ganzzahligen Exponenten liefert ohne Warnung ein `complex`, und auch dieses trägt einen Rundungsrest im Realteil.
::::

⁠**Kurz gesagt:** `cmath` ist `math` für komplexe Zahlen; dort hat auch $\sqrt{-1}$ ein Ergebnis.

### Betrag und Phase: erst von Hand, dann fertig

<span class="anker" id="stufe-9-5"></span>

Für einen Punkt der Ebene sagen Betrag und Phase oft mehr als Real- und Imaginärteil: Der Betrag ist sein Abstand vom Nullpunkt, die Phase die Richtung, in der er liegt. So beschreibt man auch einen Ort mit „5 km in Richtung Nordosten“.

**Der Pfeil.** Abb. [10](#abb-10) zeigt $z=3+4\mathrm j$ als Pfeil. Der Betrag ist seine Länge, die Phase sein Winkel gegen die reelle Achse. Real- und Imaginärteil sind die beiden Katheten eines rechtwinkligen Dreiecks, der Betrag die Hypotenuse.

:::abbildung prog/k2zeiger 10
Die komplexe Zahl $z=3+4\mathrm j$ als Pfeil in der komplexen Ebene, gestrichelt die konjugiert komplexe Zahl $z^*$. Rechts, mit welchem Python-Ausdruck man jede Größe erhält.
:::

**Von Hand.** Den Betrag liefert der Satz des Pythagoras. Für die Phase gibt es in `math` die Funktion `math.atan2(y, x)`: Sie bekommt Imaginär- und Realteil getrennt, in dieser Reihenfolge, und kann deshalb den richtigen Quadranten bestimmen. `math.atan(y / x)` sieht nur den Quotienten und liefert für $-3-4\mathrm j$ denselben Winkel wie für $3+4\mathrm j$:

```console
>>> (z.real ** 2 + z.imag ** 2) ** 0.5
5.0
>>> math.atan2(z.imag, z.real)
0.9272952180016122
>>> math.degrees(math.atan2(z.imag, z.real))
53.13010235415598
>>> w = -3 - 4j
>>> math.atan(w.imag / w.real)
0.9272952180016122
>>> math.atan2(w.imag, w.real)
-2.214297435588181
```

$-2{,}2143$ ist $-126{,}87^\circ$: Der Pfeil von $w$ zeigt nach links unten, und das ist richtig.

**Fertig.** Die eingebaute Funktion `abs` liefert bei einem `complex` den Betrag, `cmath.phase` die Phase, und `cmath.polar` beides auf einmal. `cmath.rect` macht aus Betrag und Phase wieder Real- und Imaginärteil:

```console
>>> abs(z)
5.0
>>> cmath.phase(z)
0.9272952180016122
>>> cmath.phase(w)
-2.214297435588181
>>> cmath.polar(z)
(5.0, 0.9272952180016122)
>>> cmath.rect(5, 0.9272952180016122)
(3.0000000000000004+3.9999999999999996j)
```

**Vergleich.** Von Hand und fertig liefern dieselben `float`: $5{,}0$ für den Betrag, $0{,}9272952180016122$ und $-2{,}214297435588181$ für die Phasen. `cmath.phase` wählt den Quadranten selbst und liefert immer einen Winkel von $-\pi$ bis $\pi$. Der Rückweg mit `rect` trifft $3+4\mathrm j$ bis auf Rundungsreste in der letzten Stelle, weil Kosinus und Sinus der gerundeten Phase wieder gerundet werden.

⁠**Kurz gesagt:** Betrag von Hand mit Pythagoras, Phase mit `math.atan2(y, x)`; fertig mit `abs`, `cmath.phase` und `cmath.polar`.

### Anwendung: einen Punkt in der Ebene drehen

<span class="anker" id="stufe-9-6"></span>

Mit Variablen, `math` und `complex` lässt sich jetzt eine Aufgabe aus der Geometrie vollständig in Python lösen. Spiele, Landkarten und Zeichenprogramme drehen ständig Punkte um einen Mittelpunkt. Mit komplexen Zahlen ist jede solche Drehung eine einzige Multiplikation.

**Die Idee.** Der Mittelpunkt liegt im Nullpunkt, der Punkt bei $z$. Die Zahl $\mathrm{e}^{\mathrm j\alpha}$ hat den Betrag 1 und die Phase $\alpha$. Beim Multiplizieren multiplizieren sich die Beträge, und die Phasen addieren sich (Unterabschnitt [9.1](#stufe-9-1)). Deshalb hat

$$z_{\mathrm{neu}}=z\cdot\mathrm{e}^{\mathrm j\alpha}$$

denselben Betrag wie $z$, und seine Phase ist um $\alpha$ größer: Der Punkt hat sich um den Winkel $\alpha$ um den Nullpunkt gedreht, für $\alpha>0$ gegen den Uhrzeigersinn, für $\alpha<0$ im Uhrzeigersinn. In Python liefert `cmath.rect(1, alpha)` die Zahl $\mathrm{e}^{\mathrm j\alpha}$, mit $\alpha$ im Bogenmaß.

**Die Uhr.** Eine Uhr-App zeichnet den Minutenzeiger als Pfeil vom Mittelpunkt der Uhr zur Zeigerspitze. Der Zeiger ist 10 cm lang und zeigt um 12:00 senkrecht nach oben; seine Spitze liegt dann bei $z=10\mathrm j$. In jeder Minute dreht er sich um $6^\circ$ im Uhrzeigersinn, nach $m$ Minuten also um $\alpha=-6^\circ\cdot m$. Wo liegt die Spitze um 12:20?

```console
>>> spitze = 10j
>>> m = 20
>>> drehung = cmath.rect(1, math.radians(-6 * m))
>>> drehung
(-0.4999999999999998-0.8660254037844387j)
>>> spitze_neu = spitze * drehung
>>> spitze_neu
(8.660254037844387-4.999999999999998j)
>>> abs(spitze_neu)
10.0
>>> math.degrees(cmath.phase(spitze_neu))
-29.999999999999993
>>> math.degrees(cmath.phase(spitze_neu / spitze))
-119.99999999999999
```

Um 12:20 liegt die Spitze $8{,}66$ cm rechts und 5 cm unterhalb des Mittelpunkts, dort, wo auf dem Zifferblatt die 4 steht (Abb. [11](#abb-11)). Ihr Abstand vom Mittelpunkt ist weiter 10 cm, und ihre Phase ist $-30^\circ$: $90^\circ$ am Anfang, um $120^\circ$ zurückgedreht. Teilt man die neue Lage durch die alte, subtrahieren sich die Phasen, und übrig bleibt der Drehwinkel $-120^\circ$. Die Reste in den letzten Stellen stammen von `math.pi` in `math.radians` und von Kosinus und Sinus, die `cmath.rect` ausrechnet.

:::abbildung prog/k2drehen 11
Der Minutenzeiger als Pfeil in der komplexen Ebene, der Mittelpunkt der Uhr im Nullpunkt; die Striche markieren die zwölf Stunden. Um 12:00 liegt die Spitze bei $z=10\mathrm j$, um 12:20 bei $8{,}66-5\mathrm j$. Die Multiplikation mit $\mathrm{e}^{\mathrm j\alpha}$, $\alpha=-120^\circ$, dreht den Pfeil im Uhrzeigersinn und lässt seine Länge gleich.
:::

Als Skript mit Kommentaren und Einheiten:

```python drehen.py
# Minutenzeiger einer Uhr: Lage der Spitze m Minuten nach 12:00
import cmath
import math

laenge = 10.0    # Länge des Zeigers in cm
m = 20           # Minuten nach 12:00

spitze = laenge * 1j                 # um 12:00 zeigt er nach oben
alpha = math.radians(-6 * m)         # Minus: im Uhrzeigersinn
spitze_neu = spitze * cmath.rect(1, alpha)   # drehen = multiplizieren

print("Spitze in cm:", spitze_neu)
print("Abstand vom Mittelpunkt in cm:", abs(spitze_neu))
print("Phase in Grad:", math.degrees(cmath.phase(spitze_neu)))
```

```console Linux
$ python3 drehen.py
Spitze in cm: (8.660254037844387-4.999999999999998j)
Abstand vom Mittelpunkt in cm: 10.0
Phase in Grad: -29.999999999999993
```

Für eine andere Uhrzeit ändert man nur die Zeile mit `m`. Unter Windows (`py drehen.py`) erscheint dieselbe Ausgabe. Selbstverständlich ist das nicht: Kosinus und Sinus in `cmath.rect` und den Betrag in `abs` berechnet Python mit Funktionen der Systembibliothek, und die runden nicht auf jedem System gleich. Bei anderen Zahlen unterscheidet sich deshalb die letzte Stelle zwischen Windows und Linux; Aufgabe [35](#aufg-35) zeigt ein Beispiel.

⁠**Kurz gesagt:** `z * cmath.rect(1, alpha)` dreht den Punkt $z$ um den Winkel $\alpha$ um den Nullpunkt; `abs` und `cmath.phase` zeigen Abstand und Richtung.

### Aufgaben zu Abschnitt [9](#stufe-9)

<span class="anker" id="stufe-9-7"></span>

:::aufgabe Aufgabe 33 ★ Rechnen mit `complex`
<span class="anker" id="aufg-33"></span>

Sage vorher und prüfe: (a) `(2 + 3j) + (1 - 1j)`, (b) `(2 + 3j) * 1j`, (c) `(1 + 1j) ** 2`, (d) `abs(-5j)`, (e) `(3 + 4j).conjugate().imag`. Deute (b) am Pfeil: Was macht die Multiplikation mit $\mathrm j$?

:::loesung
```console
>>> (2 + 3j) + (1 - 1j)
(3+2j)
>>> (2 + 3j) * 1j
(-3+2j)
>>> (1 + 1j) ** 2
2j
>>> abs(-5j)
5.0
>>> (3 + 4j).conjugate().imag
-4.0
```

(a) Real- und Imaginärteile addieren sich. (b) $(2+3\mathrm j)\mathrm j=2\mathrm j+3\mathrm j^2=-3+2\mathrm j$. Am Pfeil: $\mathrm j=\mathrm{e}^{\mathrm j\pi/2}$ hat den Betrag 1 und die Phase $90^\circ$; die Multiplikation dreht den Pfeil um $90^\circ$ gegen den Uhrzeigersinn und lässt seine Länge gleich. (c) $(1+\mathrm j)^2=1+2\mathrm j+\mathrm j^2=2\mathrm j$; Python zeigt eine rein imaginäre Zahl ohne Realteil an. (d) Der Betrag von $-5\mathrm j$ ist 5. (e) Konjugieren dreht das Vorzeichen des Imaginärteils um.
:::
:::

:::aufgabe Aufgabe 34 ★★ Der richtige Quadrant
<span class="anker" id="aufg-34"></span>

Bestimme die Phase von $1+\mathrm j$, $-1+\mathrm j$, $-1-\mathrm j$ und $1-\mathrm j$ in Grad, einmal mit `math.atan` von $y/x$ und einmal mit `cmath.phase`. Für welche Zahlen weichen die Ergebnisse ab, und um wie viel?

:::loesung
```console
>>> import math
>>> import cmath
>>> math.degrees(math.atan(1 / 1)), math.degrees(cmath.phase(1 + 1j))
(45.0, 45.0)
>>> math.degrees(math.atan(1 / -1)), math.degrees(cmath.phase(-1 + 1j))
(-45.0, 135.0)
>>> math.degrees(math.atan(-1 / -1)), math.degrees(cmath.phase(-1 - 1j))
(45.0, -135.0)
>>> math.degrees(math.atan(-1 / 1)), math.degrees(cmath.phase(1 - 1j))
(-45.0, -45.0)
```

Mit einem Komma zwischen zwei Ausdrücken zeigt der interaktive Modus beide Werte nebeneinander. Für $1+\mathrm j$ und $1-\mathrm j$ rechts der senkrechten Achse stimmen beide Wege überein. Für $-1+\mathrm j$ und $-1-\mathrm j$ weicht `atan` um $180^\circ$ ab: Der Quotient $y/x$ ist derselbe wie bei der gegenüberliegenden Zahl, der Pfeil zeigt aber in die entgegengesetzte Richtung. `cmath.phase` und `math.atan2` sehen beide Teile getrennt und wählen den richtigen Quadranten.
:::
:::

:::aufgabe Aufgabe 35 ★★ Weitere Zeigerstellungen
<span class="anker" id="aufg-35"></span>

<ol class="al">

<li>

Der Stundenzeiger derselben Uhr ist 6 cm lang und zeigt um 3:00 waagerecht nach rechts; seine Spitze liegt dann bei $z=6$. In jeder Stunde dreht er sich um $30^\circ$ im Uhrzeigersinn. Berechne die Lage seiner Spitze um 5:00, ihren Abstand vom Mittelpunkt und ihre Phase in Grad.

</li>

<li>

Nach wie vielen Minuten zeigt der Minutenzeiger aus Unterabschnitt [9.6](#stufe-9-6) zum ersten Mal genau schräg nach rechts oben, sodass Real- und Imaginärteil seiner Spitze gleich sind? Welche Phase hat die Spitze dann? Prüfe mit Python, mit einem geeigneten Vergleich.

</li>

</ol>

:::loesung
(a) Um 5:00 hat sich der Stundenzeiger seit 3:00 um zwei Stunden gedreht, also um $\alpha=-2\cdot30^\circ=-60^\circ$:

```console
>>> import math
>>> import cmath
>>> stunde = 6
>>> stunde_neu = stunde * cmath.rect(1, math.radians(-30 * 2))
>>> stunde_neu
(3.000000000000001-5.196152422706632j)
>>> abs(stunde_neu)
6.000000000000001
>>> math.degrees(cmath.phase(stunde_neu))
-59.99999999999999
```

Die Spitze liegt bei $(3-5{,}196\,\mathrm j)$ cm, also 3 cm rechts und $5{,}2$ cm unterhalb des Mittelpunkts, dort, wo die 5 steht. Ihr Abstand vom Mittelpunkt ist 6 cm und ihre Phase $-60^\circ$, beides bis auf Rundungsreste in der letzten Stelle.

(b) Real- und Imaginärteil sind gleich und positiv, wenn die Phase $45^\circ$ ist. Die Spitze beginnt bei $90^\circ$ und verliert $6^\circ$ pro Minute; $45^\circ$ erreicht sie also nach $45/6=7{,}5$ Minuten, um 12:07:30. Weil Real- und Imaginärteil gerundete Werte sind, prüft man ihre Gleichheit mit Toleranz:

```console
>>> spitze_neu = 10j * cmath.rect(1, math.radians(-6 * 7.5))
>>> math.isclose(spitze_neu.real, spitze_neu.imag)
True
```

Die beiden Teile selbst zeigt Python je nach System verschieden an, unter Windows so:

```console
>>> spitze_neu
(7.0710678118654755+7.0710678118654755j)
>>> math.degrees(cmath.phase(spitze_neu))
45.0
```

Unter Linux so:

```console
>>> spitze_neu
(7.071067811865475+7.0710678118654755j)
>>> math.degrees(cmath.phase(spitze_neu))
45.00000000000001
```

Mathematisch sind beide Teile $10\cdot\frac{\sqrt2}2\approx7{,}07$, und die Phase ist $45^\circ$. Kosinus und Sinus rechnet `cmath.rect` aber mit der Systembibliothek (Unterabschnitt [9.6](#stufe-9-6)), und unter Linux fällt der Realteil in der letzten Stelle etwas kleiner aus. Ein Vergleich mit `==` hätte deshalb unter Windows `True` und unter Linux `False` geliefert; der Vergleich mit Toleranz liefert überall `True`.
:::
:::

:::aufgabe Aufgabe 36 ★★★ Eine quadratische Gleichung ohne reelle Lösung
<span class="anker" id="aufg-36"></span>

Die Gleichung $x^2+x+1=0$ hat keine reelle Lösung: In der Lösungsformel $x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$ steht unter der Wurzel $1-4=-3$. Berechne beide komplexen Lösungen mit `cmath.sqrt`, dazu ihren Betrag und ihre Phase in Grad. Setze sie in die Gleichung ein und prüfe, dass sie die Gleichung erfüllen, und zwar mit einem geeigneten Vergleich.

:::loesung
Mit $a=b=c=1$ steht unter der Wurzel $b^2-4ac=-3$, und `cmath.sqrt` liefert $\sqrt3\,\mathrm j$:

```console
>>> import math
>>> import cmath
>>> a = 1
>>> b = 1
>>> c = 1
>>> w = cmath.sqrt(b ** 2 - 4 * a * c)
>>> w
1.7320508075688772j
>>> x1 = (-b + w) / (2 * a)
>>> x2 = (-b - w) / (2 * a)
>>> x1
(-0.5+0.8660254037844386j)
>>> x2
(-0.5-0.8660254037844386j)
>>> math.degrees(cmath.phase(x1))
120.00000000000001
>>> math.degrees(cmath.phase(x2))
-120.00000000000001
>>> rest = a * x1 ** 2 + b * x1 + c
>>> rest
(1.1102230246251565e-16+0j)
>>> rest == 0
False
>>> abs(rest) <= 1e-12
True
>>> abs(a * x2 ** 2 + b * x2 + c) <= 1e-12
True
```

Die Lösungen sind $x_{1,2}=-\frac12\pm\frac{\sqrt3}2\,\mathrm j$ mit den Phasen $\pm120^\circ$. Die Phasen passen zum Satz von Vieta, nach dem $x_1x_2=\frac ca=1$ ist: Die Phasen addieren sich beim Multiplizieren, und $120^\circ+(-120^\circ)=0^\circ$ ist die Phase der Zahl 1. Beim Einsetzen bleibt ein Rest von $1{,}1\cdot10^{-16}$: Rundungsreste aus mehreren Rechenschritten, denn $\frac{\sqrt3}2$ ist als `float` nicht exakt. `==` liefert deshalb `False`. Verglichen wird mit 0, also versagt auch der relative Vergleich (Unterabschnitt [7.4](wahrheitswerte-und-vergleiche.html#stufe-7-4)). Der geeignete Vergleich ist der mit absoluter Toleranz, für komplexe Zahlen mit dem Betrag. $10^{-12}$ liegt weit über den Rundungsresten von Zahlen der Größe 1 und weit unter allem, was als echte Abweichung zählen würde.

Der Betrag beider Lösungen ist genau 1, denn $\frac14+\frac34=1$. Python zeigt ihn je nach System verschieden an, unter Windows so:

```console
>>> abs(x1)
0.9999999999999999
```

Unter Linux so:

```console
>>> abs(x1)
1.0
```

Den Betrag einer komplexen Zahl berechnet Python mit einer Funktion der Systembibliothek, und die rundet nicht auf jedem System gleich (Unterabschnitt [9.6](#stufe-9-6)).
:::
:::

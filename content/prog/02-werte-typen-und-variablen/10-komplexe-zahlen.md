---
title: Komplexe Zahlen
pfad: Informatik / Programmieren / Python / Werte, Typen und Variablen
knoten: Python 2: Werte, Typen und Variablen
order: 6031000
summary: In der Wechselstromtechnik rechnet man mit komplexen Spannungen, Strömen und Impedanzen.
tags: Attribut
lang: de
---

<span class="anker" id="stufe-9"></span>

:::zweck
In der Wechselstromtechnik rechnet man mit komplexen Spannungen, Strömen und Impedanzen. Dieser Abschnitt zeigt, wie Python komplexe Zahlen speichert, wie man Betrag und Phase von Hand und fertig bestimmt, und rechnet zum Schluss die Impedanz eines RC-Glieds aus.
:::

### Was du dafür brauchst: komplexe Zahlen

<span class="anker" id="stufe-9-1"></span>

Dieser Unterabschnitt stellt zusammen, was das Kapitel aus der Mathematik der komplexen Zahlen benutzt; ausführlich steht es in Höhere Mathematik 1, [Teil 2](/wissen/informatik/programmieren/python/werte-typen-und-variablen/werte-typen-und-variablen.html).

**Real- und Imaginärteil.** Eine komplexe Zahl $z=x+\mathrm jy$ besteht aus dem Realteil $x=\operatorname{Re}z$ und dem Imaginärteil $y=\operatorname{Im}z$, beides reelle Zahlen. Für die imaginäre Einheit gilt $\mathrm j^2=-1$. Die Elektrotechnik schreibt $\mathrm j$ statt $i$, weil $i$ für den Strom vergeben ist.

**Die komplexe Ebene.** Man trägt $x$ nach rechts und $y$ nach oben auf. Dann ist $z$ ein Punkt der Ebene, oder ein Pfeil vom Nullpunkt zu diesem Punkt; in der Elektrotechnik heißt dieser Pfeil Zeiger. Die zu $z$ *konjugiert komplexe* Zahl $z^*=x-\mathrm jy$ ist ihr Spiegelbild an der waagerechten Achse.

**Betrag und Phase.** Der Betrag $|z|=\sqrt{x^2+y^2}$ ist die Länge des Zeigers. Die Phase $\varphi$, auch Argument genannt, ist der Winkel des Zeigers gegen die positive reelle Achse, gegen den Uhrzeigersinn positiv, mit $-\pi<\varphi\le\pi$. Es gilt $\tan\varphi=y/x$, aber $\arctan(y/x)$ liefert nur Winkel zwischen $-\frac\pi2$ und $\frac\pi2$; liegt $z$ links der senkrechten Achse, muss man $\pi$ addieren oder abziehen.

**Polarform.** Mit der Eulerschen Formel $\mathrm{e}^{\mathrm j\varphi}=\cos\varphi+\mathrm j\sin\varphi$ ist $z=|z|\,\mathrm{e}^{\mathrm j\varphi}$. Beim Multiplizieren multiplizieren sich die Beträge, und die Phasen addieren sich; beim Dividieren teilen sich die Beträge, und die Phasen subtrahieren sich.

⁠**Beispiel:** $z=3+4\mathrm j$ hat $|z|=\sqrt{9+16}=5$ und $\varphi=\arctan\frac43\approx0{,}9273\approx53{,}13^\circ$. Es ist $z^*=3-4\mathrm j$ und $z\cdot z^*=9+16=25=|z|^2$.

⁠**Kurz gesagt:** $z=x+\mathrm jy=|z|\,\mathrm{e}^{\mathrm j\varphi}$ mit $|z|=\sqrt{x^2+y^2}$ und der Phase $\varphi$ als Winkel des Zeigers.

### Der Typ `complex`

<span class="anker" id="stufe-9-2"></span>

Eine Impedanz hat zwei Anteile, Wirk- und Blindwiderstand. Python braucht einen Typ, der beide zusammen als eine Zahl speichert und mit ihr nach den Regeln der komplexen Rechnung rechnet.

**Ein Paar von Gleitkommazahlen.** Python speichert eine komplexe Zahl als zwei `float` nebeneinander, den Realteil und den Imaginärteil, und schreibt die imaginäre Einheit wie die Elektrotechnik als `j`.

:::definition Definition 9.1 (Der Typ `complex`)
<span class="anker" id="satz-9-1"></span>

Ein Objekt vom Typ `complex` speichert eine komplexe Zahl als Paar zweier `float`, Realteil und Imaginärteil. Eine Zahl mit einem angehängten `j` ist imaginär: `4j` bedeutet $4\mathrm j$. Die Funktion `complex(x, y)` erzeugt $x+\mathrm jy$.
:::

**Beispiel.** `3 + 4j` ist eine Rechnung: `int` plus imaginäre Zahl ergibt `complex`. Python zeigt komplexe Zahlen in Klammern:

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

⁠**Kurz gesagt:** `complex` speichert Real- und Imaginärteil als zwei `float`; die imaginäre Einheit heißt `1j`.

:::hintergrund Warum Python `j` schreibt und nicht `i`
Die Mathematik schreibt meist $i$, die Elektrotechnik $\mathrm j$. Python folgt der Elektrotechnik und der Physik; ein Entwickler der Sprache begründete das in der Diskussion über einen Änderungswunsch damit, dass diese Schreibweise dort seit Langem üblich ist und eine Umstellung bestehende Programme brechen würde. Statt `j` darf man auch `J` schreiben, `i` dagegen nicht.
:::

### Das Attribut: Real- und Imaginärteil

<span class="anker" id="stufe-9-3"></span>

Aus einer komplexen Zahl will man oft den Real- oder den Imaginärteil allein haben, etwa den Wirkwiderstand einer Impedanz. Dafür braucht man keine Rechnung: Beide Teile stehen fertig im Objekt.

**Was am Objekt hängt.** Eine Methode hängt an einem Objekt und wird mit Punkt und Klammern aufgerufen (Unterabschnitt [1.4](objekte-und-typen.html#stufe-1-4)). Es können aber auch einfache Werte am Objekt hängen, die man ohne Klammern abliest.

:::definition Definition 9.2 (Attribut)
<span class="anker" id="satz-9-2"></span>

Ein __Attribut__ ist ein Name, der an einem Objekt hängt und mit einem Punkt abgerufen wird: *objekt*`.`*name*. Methoden sind Attribute, die man aufruft; andere Attribute sind einfach Werte.
:::

Daher kommt der Name der Ausnahme `AttributeError` aus Unterabschnitt [1.4](objekte-und-typen.html#stufe-1-4): Am Objekt hing kein Attribut mit dem gesuchten Namen.

**Beispiel.** `real` und `imag` sind Attribute mit den beiden Teilen als `float`; `conjugate` ist eine Methode und liefert die konjugiert komplexe Zahl:

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

⁠**Kurz gesagt:** Ein Attribut ist ein Name am Objekt; `z.real` und `z.imag` liefern Real- und Imaginärteil.

### Das Modul `cmath`

<span class="anker" id="stufe-9-4"></span>

Die Funktionen aus `math` arbeiten nur mit reellen Zahlen. `math.sqrt(-1)` ist deshalb ein Fehler, obwohl $\sqrt{-1}=\mathrm j$ eine vernünftige Antwort wäre.

**Ein zweiter Werkzeugkasten.** Für komplexe Zahlen gibt es ein eigenes Modul mit denselben Funktionsnamen. Weil jedes Modul seine eigenen Namen hat, können `math.sqrt` und `cmath.sqrt` nebeneinander bestehen.

:::definition Definition 9.3 (Das Modul `cmath`)
<span class="anker" id="satz-9-3"></span>

Das Modul `cmath` enthält mathematische Funktionen für komplexe Zahlen, darunter `sqrt`, `exp`, `log`, `sin`, `cos` sowie `phase`, `polar` und `rect` für die Polarform. Die Rechenfunktionen liefern ein `complex`; `phase` liefert einen `float` und `polar` zwei `float`.
:::

**Beispiel.** Mit `math` scheitert die Wurzel aus $-1$:

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

⁠**Kurz gesagt:** `cmath` ist `math` für komplexe Zahlen; dort hat auch $\sqrt{-1}$ ein Ergebnis.

### Betrag und Phase: erst von Hand, dann fertig

<span class="anker" id="stufe-9-5"></span>

Für eine Impedanz sind Betrag und Phase oft wichtiger als Real- und Imaginärteil: Der Betrag bestimmt die Stromstärke, die Phase die Verschiebung zwischen Spannung und Strom.

**Der Zeiger.** Abb. [10](#abb-10) zeigt $z=3+4\mathrm j$ als Zeiger. Der Betrag ist seine Länge, die Phase sein Winkel gegen die reelle Achse. Real- und Imaginärteil sind die beiden Katheten eines rechtwinkligen Dreiecks, der Betrag die Hypotenuse.

:::abbildung prog/k2zeiger 10
Die komplexe Zahl $z=3+4\mathrm j$ als Zeiger in der komplexen Ebene, gestrichelt die konjugiert komplexe Zahl $z^*$. Rechts, mit welchem Python-Ausdruck man jede Größe erhält.
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

$-2{,}2143$ ist $-126{,}87^\circ$: Der Zeiger von $w$ zeigt nach links unten, und das ist richtig.

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

### Anwendung: die Impedanz eines RC-Glieds

<span class="anker" id="stufe-9-6"></span>

Mit Variablen, `math` und `complex` lässt sich jetzt eine Wechselstromrechnung vollständig in Python führen.

**Die Schaltung.** Ein Widerstand $R=1\,\mathrm{k\Omega}$ und ein Kondensator $C=100\,\mathrm{nF}$ liegen in Reihe an einer Sinusspannung mit $f=1\,\mathrm{kHz}$ und dem Scheitelwert $\hat U=5\,\mathrm V$, Phase 0. Mit der Kreisfrequenz $\omega=2\pi f$ ist die Impedanz

$$Z=R+\frac{1}{\mathrm j\omega C}=R-\mathrm j\,\frac{1}{\omega C},$$

und der Strom ist $I=\hat U/Z$. Dabei ist die übliche Zeitabhängigkeit $\mathrm{e}^{\mathrm j\omega t}$ angenommen.

**Die Rechnung.** Die Namen folgen den Formelzeichen. Großbuchstaben wie `R` und `C` sind hier sinnvoll, weil sie die Formel lesbar machen:

```console
>>> R = 1000
>>> C = 100e-9
>>> f = 1000
>>> Z = R + 1 / (1j * 2 * math.pi * f * C)
>>> Z
(1000-1591.5494309189537j)
>>> abs(Z)
1879.6354942005232
>>> math.degrees(cmath.phase(Z))
-57.85809236465795
>>> I = 5 / Z
>>> I
(0.0014152159983755108+0.0022523862168419427j)
>>> math.degrees(cmath.phase(I))
57.85809236465795
```

Die Impedanz hat den Betrag $1879{,}6\,\Omega$ und die Phase $-57{,}86^\circ$ (Abb. [11](#abb-11)). Der Strom hat den Scheitelwert $5\,\mathrm V/1879{,}6\,\Omega\approx2{,}66\,\mathrm{mA}$ und eilt der Spannung um $57{,}86^\circ$ voraus, wie es sich für eine Schaltung mit kapazitivem Verhalten gehört.

:::abbildung prog/k2rc 11
Zeigerdiagramm der Impedanz des RC-Glieds bei $f=1\,\mathrm{kHz}$: Der Widerstand liefert den Realteil, der Kondensator einen negativen Imaginärteil. Zusammen ergeben sie den Zeiger $Z$ mit $|Z|=1879{,}6\,\Omega$ und der Phase $\varphi=-57{,}86^\circ$.
:::

Als Skript mit Kommentaren und Einheiten:

```python rc_impedanz.py
# Impedanz einer Reihenschaltung aus R und C bei einer Frequenz
import cmath
import math

R = 1000.0       # Widerstand in Ohm
C = 100e-9       # Kapazität in F
f = 1000.0       # Frequenz in Hz
U = 5.0          # Spannung der Quelle in V, Phase 0

omega = 2 * math.pi * f            # Kreisfrequenz in 1/s
Z = R + 1 / (1j * omega * C)       # Impedanz in Ohm
I = U / Z                          # Strom in A, komplex

print("Z in Ohm:", Z)
print("|Z| in Ohm:", abs(Z))
print("Phase von Z in Grad:", math.degrees(cmath.phase(Z)))
print("|I| in mA:", U / abs(Z) * 1000)    # |I| = U / |Z|
print("Phase von I in Grad:", math.degrees(cmath.phase(I)))
```

```console Linux
$ python3 rc_impedanz.py
Z in Ohm: (1000-1591.5494309189537j)
|Z| in Ohm: 1879.6354942005232
Phase von Z in Grad: -57.85809236465795
|I| in mA: 2.66009022250704
Phase von I in Grad: 57.85809236465795
```

Unter Windows (`py rc_impedanz.py`) erscheint dieselbe Ausgabe. Den Betrag des Stroms rechnet das Skript als $\hat U/|Z|$ aus. `abs(I) * 1000` ergibt mathematisch dasselbe, unter Windows und Linux aber eine verschiedene letzte Stelle: Den Betrag einer komplexen Zahl berechnet Python mit einer Funktion der Systembibliothek, und die rundet nicht auf jedem System gleich.

⁠**Kurz gesagt:** Mit `1j`, `math.pi`, `abs` und `cmath.phase` rechnet Python Impedanzen und Ströme wie in der Wechselstromtechnik.

### Aufgaben zu Abschnitt [9](#stufe-9)

<span class="anker" id="stufe-9-7"></span>

:::aufgabe Aufgabe 33 ★ Rechnen mit `complex`
<span class="anker" id="aufg-33"></span>

Sage vorher und prüfe: (a) `(2 + 3j) + (1 - 1j)`, (b) `(2 + 3j) * 1j`, (c) `(1 + 1j) ** 2`, (d) `abs(-5j)`, (e) `(3 + 4j).conjugate().imag`. Deute (b) am Zeiger: Was macht die Multiplikation mit $\mathrm j$?

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

(a) Real- und Imaginärteile addieren sich. (b) $(2+3\mathrm j)\mathrm j=2\mathrm j+3\mathrm j^2=-3+2\mathrm j$. Am Zeiger: $\mathrm j=\mathrm{e}^{\mathrm j\pi/2}$ hat den Betrag 1 und die Phase $90^\circ$; die Multiplikation dreht den Zeiger um $90^\circ$ gegen den Uhrzeigersinn und lässt seine Länge gleich. (c) $(1+\mathrm j)^2=1+2\mathrm j+\mathrm j^2=2\mathrm j$; Python zeigt eine rein imaginäre Zahl ohne Realteil an. (d) Der Betrag von $-5\mathrm j$ ist 5. (e) Konjugieren dreht das Vorzeichen des Imaginärteils um.
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

Mit einem Komma zwischen zwei Ausdrücken zeigt der interaktive Modus beide Werte nebeneinander. Für $1+\mathrm j$ und $1-\mathrm j$ rechts der senkrechten Achse stimmen beide Wege überein. Für $-1+\mathrm j$ und $-1-\mathrm j$ weicht `atan` um $180^\circ$ ab: Der Quotient $y/x$ ist derselbe wie bei der gegenüberliegenden Zahl, der Zeiger zeigt aber in die entgegengesetzte Richtung. `cmath.phase` und `math.atan2` sehen beide Teile getrennt und wählen den richtigen Quadranten.
:::
:::

:::aufgabe Aufgabe 35 ★★ Ein zweites RC-Glied
<span class="anker" id="aufg-35"></span>

$R=2{,}2\,\mathrm{k\Omega}$, $C=47\,\mathrm{nF}$, $f=2\,\mathrm{kHz}$, $\hat U=10\,\mathrm V$.

<ol class="al">

<li>

Berechne $Z$, $|Z|$ in $\Omega$, die Phase von $Z$ in Grad und den Scheitelwert des Stroms in mA.

</li>

<li>

Bei welcher Frequenz sind Real- und Imaginärteil von $Z$ betragsgleich? Welche Phase hat $Z$ dann? Prüfe mit Python.

</li>

</ol>

:::loesung
(a)

```console
>>> import math
>>> import cmath
>>> R = 2200
>>> C = 47e-9
>>> f = 2000
>>> Z = R + 1 / (1j * 2 * math.pi * f * C)
>>> Z
(2200-1693.1376924669719j)
>>> abs(Z)
2776.097124679247
>>> math.degrees(cmath.phase(Z))
-37.582169952663065
>>> 10 / abs(Z) * 1000
3.6021794450564872
```

$Z=(2200-1693{,}1\,\mathrm j)\,\Omega$, $|Z|=2776{,}1\,\Omega$, Phase $-37{,}58^\circ$, Scheitelwert des Stroms $3{,}60\,\mathrm{mA}$.

(b) Betragsgleich heißt $R=\frac1{\omega C}$, also $f=\frac{1}{2\pi RC}$. Dann ist die Phase $-45^\circ$:

```console
>>> f = 1 / (2 * math.pi * R * C)
>>> f
1539.2160840608833
>>> Z = R + 1 / (1j * 2 * math.pi * f * C)
>>> Z
(2200-2200.0000000000005j)
>>> math.degrees(cmath.phase(Z))
-45.00000000000001
```

Bei $f\approx1539\,\mathrm{Hz}$ sind beide Teile $2200\,\Omega$, bis auf einen Rundungsrest in der letzten Stelle; die Phase ist $-45^\circ$. Das ist die Grenzfrequenz des RC-Glieds.
:::
:::

:::aufgabe Aufgabe 36 ★★★ Spannungsteiler mit Kondensator
<span class="anker" id="aufg-36"></span>

Am Kondensator des RC-Glieds aus Unterabschnitt [9.6](#stufe-9-6) liegt die Spannung $U_C=\hat U\cdot\frac{Z_C}{Z}$ mit $Z_C=\frac{1}{\mathrm j\omega C}$. Berechne $U_C$, ihren Betrag und ihre Phase. Prüfe, dass $U_C$ und die Spannung am Widerstand $U_R=R\cdot I$ zusammen $\hat U$ ergeben, und zwar mit einem geeigneten Vergleich.

:::loesung
```console
>>> import math
>>> import cmath
>>> R = 1000
>>> C = 100e-9
>>> f = 1000
>>> Z_C = 1 / (1j * 2 * math.pi * f * C)
>>> Z = R + Z_C
>>> U_C = 5 * Z_C / Z
>>> U_C
(3.584784001624489-2.252386216841943j)
>>> abs(U_C)
4.233665079824152
>>> math.degrees(cmath.phase(U_C))
-32.14190763534206
>>> U_R = R * (5 / Z)
>>> U_R + U_C
(5-4.440892098500626e-16j)
>>> abs((U_R + U_C) - 5) <= 1e-9 * 5
True
```

$U_C\approx(3{,}585-2{,}252\,\mathrm j)\,\mathrm V$ mit dem Betrag $4{,}23\,\mathrm V$ und der Phase $-32{,}14^\circ$. Die Phase passt zur Rechnung mit der Polarform: $Z_C$ hat die Phase $-90^\circ$, $Z$ die Phase $-57{,}86^\circ$, der Quotient also $-90^\circ+57{,}86^\circ=-32{,}14^\circ$. Die Summe $U_R+U_C$ ist nicht genau 5, sondern hat einen Imaginärteil von $4\cdot10^{-16}$: Rundungsreste aus mehreren Rechenschritten. `==` würde deshalb `False` liefern. Der geeignete Vergleich ist der mit relativer Toleranz; für komplexe Zahlen nimmt man den Betrag der Differenz.
:::
:::

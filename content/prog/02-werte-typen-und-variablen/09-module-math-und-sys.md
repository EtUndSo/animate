---
title: Module: `math` und `sys`
pfad: Informatik / Programmieren / Python / Werte, Typen und Variablen
knoten: Python 2: Werte, Typen und Variablen
order: 6030900
summary: Quadratwurzel, Sinus, Logarithmus, die Grenzen des Typs float : Python bringt dafür fertige Funktionen und Werte mit, sortiert in Module.
tags: Modul
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Quadratwurzel, Sinus, Logarithmus, die Grenzen des Typs `float`: Python bringt dafür fertige Funktionen und Werte mit, sortiert in Module. Dieser Abschnitt zeigt, wie man ein Modul lädt, und nutzt die Module `math` und `sys`, um die Ergebnisse der letzten Abschnitte auf dem fertigen Weg zu bestätigen.
:::

### Das Modul und `import`

<span class="anker" id="stufe-8-1"></span>

Python kennt Tausende fertiger Funktionen. Wären alle ihre Namen ständig da, gäbe es ein Gedränge: Zwei Funktionen mit demselben Namen könnten sich gegenseitig verdrängen, und Python müsste beim Start alles laden.

**Ein Werkzeugkasten, den man erst holt.** Die Funktionen liegen deshalb in beschrifteten Werkzeugkästen. Man holt einen Kasten, wenn man ihn braucht, und greift dann mit seinem Namen hinein: „aus dem Kasten `math` die Wurzel“.

:::definition Definition 8.1 (Modul)
<span class="anker" id="satz-8-1"></span>

Ein __Modul__ ist eine Datei mit fertigen Python-Definitionen, etwa Funktionen und Werten. Die Anweisung `import math` lädt das Modul `math` und bindet den Namen `math` an das Modulobjekt. Auf seinen Inhalt greift man mit einem Punkt zu: `math.sqrt` ist die Funktion `sqrt` aus dem Modul `math`.
:::

Der Punkt hat dieselbe Bedeutung wie bei einer Methode (Unterabschnitt [1.4](objekte-und-typen.html#stufe-1-4)): „das, was an diesem Objekt hängt“. Das Modulobjekt ist ein Objekt wie jedes andere, mit dem Typ `module`.

**Beispiel.** Vor dem `import` kennt Python den Namen nicht; danach ist nur `math` neu, nicht die Namen darin:

```console
>>> math.sqrt(2)
Traceback (most recent call last):
  File "<python-input-0>", line 1, in <module>
    math.sqrt(2)
    ^^^^
NameError: name 'math' is not defined. Did you forget to import 'math'?
>>> import math
>>> math.sqrt(2)
1.4142135623730951
>>> type(math)
<class 'module'>
>>> sqrt(2)
Traceback (most recent call last):
  File "<python-input-4>", line 1, in <module>
    sqrt(2)
    ^^^^
NameError: name 'sqrt' is not defined
```

`math.sqrt(2)` liefert denselben `float` wie `2 ** 0.5` in Python 1 ([Programmieren, Python 1, Abschnitt 4.5](/wissen/informatik/programmieren/python/programme-und-der-python-interpreter/der-interaktive-modus.html#stufe-4-5)). Ein `import` gilt bis zum Ende der Sitzung oder des Skripts; im Skript steht er üblicherweise ganz oben.

⁠**Kurz gesagt:** `import modul` lädt ein Modul und bindet seinen Namen; `modul.name` greift auf seinen Inhalt zu.

### Das Modul `math`

<span class="anker" id="stufe-8-2"></span>

Für technische Rechnungen braucht man die Funktionen vom Taschenrechner: Wurzel, Exponentialfunktion, Logarithmen, Winkelfunktionen. Das Modul `math` enthält sie für `float`.

| Name | Bedeutung |
|---|---|
| `math.pi`, `math.e` | die Zahlen $\pi$ und $\mathrm{e}$ als `float` |
| `math.inf`, `math.nan` | die besonderen Werte `inf` und `nan` |
| `math.sqrt(x)` | Quadratwurzel $\sqrt x$ |
| `math.exp(x)` | $\mathrm{e}^x$ |
| `math.log(x)`, `math.log10(x)` | natürlicher Logarithmus, Zehnerlogarithmus |
| `math.sin(x)`, `math.cos(x)`, `math.tan(x)` | Winkelfunktionen, $x$ im Bogenmaß |
| `math.degrees(x)`, `math.radians(x)` | Bogenmaß in Grad und zurück |
| `math.hypot(x, y)` | $\sqrt{x^2+y^2}$ |
| `math.floor(x)`, `math.ceil(x)` | nach unten, nach oben zur ganzen Zahl |

**Beispiel.** Ein Zehnerlogarithmus, eine Entladekurve nach einer Zeitkonstante und ein Sinus:

```console
>>> math.log10(1000)
3.0
>>> math.exp(-1)
0.36787944117144233
>>> math.sin(math.radians(30))
0.49999999999999994
>>> math.sin(math.pi)
1.2246467991473532e-16
```

Ein Kondensator ist nach einer Zeitkonstante auf $\mathrm{e}^{-1}\approx36{,}8\,\%$ seiner Anfangsspannung entladen. Die letzten beiden Zeilen zeigen wieder Rundungsfehler: $\sin30^\circ$ ist $0{,}5$, und $\sin\pi$ ist 0. Aber weder $30^\circ$ im Bogenmaß noch $\pi$ selbst ist als `float` exakt; `math.pi` ist nur der `float`, der $\pi$ am nächsten liegt.

⁠**Kurz gesagt:** `math` enthält die Funktionen des Taschenrechners für `float`; Winkel stehen im Bogenmaß.

:::hintergrund Warum $\sin\pi$ ausgerechnet $1{,}22\cdot10^{-16}$ ergibt
`math.pi` ist ein wenig kleiner als $\pi$: $\texttt{math.pi}=\pi-\delta$ mit $\delta\approx1{,}2246\cdot10^{-16}$. Für kleine $\delta$ ist $\sin(\pi-\delta)=\sin\delta\approx\delta$. Die Funktion `math.sin` rechnet also nicht falsch, im Gegenteil: Sie liefert den Sinus der Zahl, die sie bekommen hat, bis auf die letzte Stelle genau. Das Ergebnis verrät sogar den Darstellungsfehler von `math.pi`. Der Fehler steckt in der Eingabe, nicht in der Funktion.
:::

### Der Toleranzvergleich, fertig: `math.isclose`

<span class="anker" id="stufe-8-3"></span>

Den Vergleich mit Toleranz aus Unterabschnitt [7.4](wahrheitswerte-und-vergleiche.html#stufe-7-4) braucht man so oft, dass `math` ihn fertig mitbringt.

**Fertig.** `math.isclose(a, b)` prüft $|a-b|\le\max\bigl(r\cdot\max(|a|,|b|),\ t_{\mathrm{abs}}\bigr)$ mit der relativen Toleranz $r=10^{-9}$ und der absoluten Toleranz $t_{\mathrm{abs}}=0$. Andere Toleranzen übergibt man mit ihrem Namen in den Klammern, als `rel_tol=` und `abs_tol=`:

```console
>>> math.isclose(0.1 + 0.2, 0.3)
True
>>> math.isclose(1e-20, 0.0)
False
>>> math.isclose(1e-20, 0.0, abs_tol=1e-12)
True
>>> math.isclose(4520, 4700, rel_tol=0.05)
True
>>> math.isclose(math.nan, math.nan)
False
>>> math.isclose(math.inf, math.inf)
True
```

**Vergleich.** Der Ausdruck von Hand aus Unterabschnitt [7.4](wahrheitswerte-und-vergleiche.html#stufe-7-4) und `math.isclose` liefern für $0{,}1+0{,}2$ und $0{,}3$ beide `True`, und an der Null scheitern beide ohne absolute Toleranz. Der fertige Weg ist kürzer, prüft die Toleranzen auf sinnvolle Werte und behandelt `inf` und `nan` nach festen Regeln: `nan` ist zu nichts nah, `inf` nur zu sich selbst.

⁠**Kurz gesagt:** `math.isclose` ist der fertige Toleranzvergleich mit $r=10^{-9}$ und ohne absolute Toleranz.

:::hintergrund Warum gerade $10^{-9}$, und warum keine absolute Toleranz voreingestellt ist
Die Voreinstellung $10^{-9}$ verlangt etwa neun gleiche Dezimalstellen, rund die Hälfte der knapp 16, die ein `float` hat. Damit bleibt Platz für die Rundungsfehler vieler Rechenschritte, und echte Unterschiede fallen trotzdem auf. Eine absolute Toleranz lässt sich dagegen nicht für alle Fälle sinnvoll voreinstellen, weil sie eine Einheit hat: $10^{-9}$ wäre für Spannungen in Volt winzig, für Kapazitäten in Farad aber größer als jeder übliche Kondensator. Deshalb ist sie 0, und wer mit 0 vergleicht, muss sich selbst überlegen, welche Größenordnung „praktisch null“ ist.
:::

### Die Grenzen des Typs `float`, fertig: `sys.float_info`

<span class="anker" id="stufe-8-4"></span>

Abschnitt [5](rechnen-mit-gleitkommazahlen.html#stufe-5) hat die Maschinengenauigkeit und den größten `float` von Hand bestimmt. Python hält diese Zahlen auch fertig bereit.

**Fertig.** Das Modul `sys` enthält Angaben über das laufende Python. Darin beschreibt `sys.float_info` den Typ `float`. Das Modul `math` hat dazu Funktionen für die Abstände benachbarter `float`: `math.ulp(x)` ist der Abstand von $x$ zum nächsten `float` mit größerem Betrag (*unit in the last place*), `math.nextafter(x, y)` der nächste `float` von $x$ in Richtung $y$:

```console
>>> import sys
>>> sys.float_info.epsilon
2.220446049250313e-16
>>> sys.float_info.max
1.7976931348623157e+308
>>> sys.float_info.min
2.2250738585072014e-308
>>> sys.float_info.mant_dig
53
>>> sys.float_info.dig
15
>>> math.ulp(1.0)
2.220446049250313e-16
>>> math.ulp(1e16)
2.0
>>> math.nextafter(0.1, 1)
0.10000000000000002
```

**Vergleich.** Alle Werte stimmen mit den Ergebnissen von Hand überein:

| Größe | von Hand | fertig |
|---|---|---|
| Maschinengenauigkeit $\varepsilon_{\mathrm M}$ | `2 ** -52` (Unterabschnitt [5.2](rechnen-mit-gleitkommazahlen.html#stufe-5-2)) | `sys.float_info.epsilon` |
| Abstand bei $10^{16}$ | $2^{-52}\cdot2^{53}=2$ (Unterabschnitt [5.2](rechnen-mit-gleitkommazahlen.html#stufe-5-2)) | `math.ulp(1e16)` |
| größter `float` | $(2-2^{-52})\cdot2^{1023}$ (Unterabschnitt [5.5](rechnen-mit-gleitkommazahlen.html#stufe-5-5)) | `sys.float_info.max` |
| kleinster gewöhnlicher `float` | $2^{-1022}$ | `sys.float_info.min` |
| Stellen der Mantisse | $p=53$ (Unterabschnitt [4.2](gleitkommazahlen-der-typ-float.html#stufe-4-2)) | `sys.float_info.mant_dig` |

Der fertige Weg sagt, was auf dem laufenden Rechner tatsächlich gilt. Der Weg von Hand erklärt, woher die Zahlen kommen.

⁠**Kurz gesagt:** `sys.float_info` beschreibt den Typ `float`, `math.ulp` den Abstand benachbarter `float`; beides bestätigt die Rechnungen von Hand.

:::hintergrund Wenn es exakt sein muss: die Module `fractions` und `decimal`
Für Rechnungen, die keinen Rundungsfehler vertragen, gibt es zwei weitere Module mit eigenen Zahltypen. `fractions` rechnet mit Brüchen aus zwei `int`, also exakt. `decimal` rechnet im Dezimalsystem, so wie man es auf Papier tut; dort ist $0{,}1$ exakt, und man kann die Zahl der Stellen einstellen. Den Wert übergibt man als Zeichenkette, denn ein `float` wie `0.1` trägt seinen Darstellungsfehler schon in sich. Gibt man ihn trotzdem als `float` hinein, zeigt `decimal` genau den gespeicherten Wert, dieselben Stellen, die in Unterabschnitt [4.6](gleitkommazahlen-der-typ-float.html#stufe-4-6) die Rechnung mit $5^{55}$ geliefert hat:

```console
>>> import fractions
>>> fractions.Fraction(1, 10) + fractions.Fraction(2, 10)
Fraction(3, 10)
>>> import decimal
>>> decimal.Decimal("0.1") + decimal.Decimal("0.2")
Decimal('0.3')
>>> decimal.Decimal(0.1)
Decimal('0.1000000000000000055511151231257827021181583404541015625')
```

Beide Typen sind deutlich langsamer als `float`, weil der Prozessor sie nicht direkt kann. Für Messwerte, die ohnehin nur wenige gültige Stellen haben, ist `float` die richtige Wahl; exakte Typen braucht man etwa für Geldbeträge.
:::

### Aufgaben zu Abschnitt [8](#stufe-8)

<span class="anker" id="stufe-8-5"></span>

:::aufgabe Aufgabe 29 ★ Drei Wege zur Hypotenuse
<span class="anker" id="aufg-29"></span>

Berechne $\sqrt{3^2+4^2}$ mit `math.sqrt`, mit `** 0.5` und mit `math.hypot`. Berechne ebenso $\sqrt{x^2+x^2}$ für den `float` `x = 1e200` auf allen drei Wegen. Was geht schief, und warum hilft `math.hypot`?

:::loesung
```console
>>> import math
>>> math.sqrt(3 ** 2 + 4 ** 2)
5.0
>>> (3 ** 2 + 4 ** 2) ** 0.5
5.0
>>> math.hypot(3, 4)
5.0
>>> x = 1e200
>>> math.sqrt(x * x + x * x)
inf
>>> math.hypot(x, x)
1.414213562373095e+200
```

Bei $x=10^{200}$ ist schon $x^2=10^{400}$ größer als der größte `float`: `x * x` ergibt `inf`, und $\sqrt\infty=\infty$. Mit `x ** 2` bricht die Rechnung sogar mit einem `OverflowError` ab (Unterabschnitt [5.5](rechnen-mit-gleitkommazahlen.html#stufe-5-5)). Das Ergebnis $\sqrt2\cdot10^{200}$ selbst ist aber harmlos. `math.hypot` rechnet so, dass kein Zwischenergebnis überläuft. Die Idee zeigt die Umformung $\sqrt{x^2+y^2}=|x|\sqrt{1+(y/x)^2}$ für $|x|\ge|y|$: Unter der Wurzel stehen nur noch Zahlen zwischen 1 und 2.
:::
:::

:::aufgabe Aufgabe 30 ★★ Pegel in Dezibel
<span class="anker" id="aufg-30"></span>

Ein Verstärker macht aus $20\,\mathrm{mV}$ am Eingang $1{,}2\,\mathrm V$ am Ausgang. Die Spannungsverstärkung in Dezibel ist $20\log_{10}(U_\mathrm{aus}/U_\mathrm{ein})$.

<ol class="al">

<li>

Berechne sie mit Variablen und `math.log10`.

</li>

<li>

Ein Tiefpass schwächt eine Spannung um $3\,\mathrm{dB}$. Um welchen Faktor? Löse $20\log_{10}x=-3$ nach $x$ auf und rechne mit `10 ** (...)`. Vergleiche mit $1/\sqrt2$.

</li>

</ol>

:::loesung
(a)

```console
>>> import math
>>> u_ein = 0.02
>>> u_aus = 1.2
>>> 20 * math.log10(u_aus / u_ein)
35.56302500767287
```

Die Verstärkung ist 60, das sind $35{,}6\,\mathrm{dB}$.

(b) $20\log_{10}x=-3$ ergibt $x=10^{-3/20}$:

```console
>>> 10 ** (-3 / 20)
0.7079457843841379
>>> 1 / math.sqrt(2)
0.7071067811865475
```

$-3\,\mathrm{dB}$ ist ein Faktor $0{,}708$, fast genau $1/\sqrt2\approx0{,}707$. Deshalb heißt die Grenzfrequenz eines Tiefpasses, bei der die Spannung auf $1/\sqrt2$ gefallen ist, auch 3-dB-Grenzfrequenz; genau sind es $20\log_{10}(1/\sqrt2)\approx-3{,}01\,\mathrm{dB}$.
:::
:::

:::aufgabe Aufgabe 31 ★★★ Der Darstellungsfehler von $\pi$
<span class="anker" id="aufg-31"></span>

<ol class="al">

<li>

Zeige mit der Näherung $\sin(\pi-\delta)\approx\delta$, dass `math.sin(math.pi)` ungefähr den Abstand $\delta=\pi-\texttt{math.pi}$ liefert.

</li>

<li>

Die Dezimalstellen von $\pi$ beginnen mit $3{,}1415926535897932384626433832795028841971$. Bestimme $\delta$ mit `decimal`: Schreibe diese Stellen als Zeichenkette in `decimal.Decimal`, ziehe `decimal.Decimal(math.pi)` davon ab und vergleiche mit (a).

</li>

<li>

Liegt `math.pi` über oder unter $\pi$? Was verrät das Vorzeichen von `math.sin(math.pi)`?

</li>

</ol>

:::loesung
(a) `math.pi` ist der `float` neben $\pi$, also $\texttt{math.pi}=\pi-\delta$ mit einem kleinen $\delta$. Mit $\sin(\pi-\delta)=\sin\delta$ und $\sin\delta\approx\delta$ für kleine $\delta$ liefert `math.sin(math.pi)` den Wert $\delta$ bis auf einen Fehler der Größe $\delta^3/6\approx3\cdot10^{-49}$, der weit unter jeder Rundung liegt.

(b)

```console
>>> import math
>>> import decimal
>>> decimal.Decimal("3.1415926535897932384626433832795028841971") - decimal.Decimal(math.pi)
Decimal('1.224646799147353177226065238E-16')
>>> math.sin(math.pi)
1.2246467991473532e-16
```

Beide stimmen in allen 17 angezeigten Stellen überein. `decimal` rechnet in der Grundeinstellung mit 28 gültigen Stellen; deshalb endet das Ergebnis dort.

(c) $\delta$ ist positiv, also liegt `math.pi` *unter* $\pi$. Das Vorzeichen von `math.sin(math.pi)` verrät es: Der Sinus ist links von $\pi$ positiv.
:::
:::

:::aufgabe Aufgabe 32 ★ Von Hand oder fertig?
<span class="anker" id="aufg-32"></span>

Bestätige mit `sys.float_info` und `math.ulp` drei Aussagen: (a) $\varepsilon_{\mathrm M}=2^{-52}$, (b) der Abstand benachbarter `float` bei $2^{53}$ ist 2, (c) bei $0{,}1$ ist er $2^{-56}$. Begründe (b) und (c) zuerst mit dem Exponenten der Zahl, wie in Unterabschnitt [5.2](rechnen-mit-gleitkommazahlen.html#stufe-5-2). Rechne jeweils den Wert von Hand mit `**` aus und vergleiche mit `==`. Warum ist `==` hier ausnahmsweise der richtige Vergleich?

:::loesung
```console
>>> import sys
>>> import math
>>> sys.float_info.epsilon == 2 ** -52
True
>>> math.ulp(2.0 ** 53) == 2
True
>>> math.ulp(0.1) == 2 ** -56
True
```

(b) Bei $2^{53}$ ist der Exponent 53, der Abstand $2^{-52}\cdot2^{53}=2$. (c) $0{,}1$ liegt zwischen $2^{-4}$ und $2^{-3}$, der Abstand ist $2^{-52}\cdot2^{-4}=2^{-56}$. Hier ist `==` der richtige Vergleich, weil keine Seite einen Rundungsfehler trägt: Alle Werte sind Zweierpotenzen, also exakt darstellbar, und `2 ** -52` wird exakt berechnet. Gefragt ist ausdrücklich, ob die Werte bis auf das letzte Bit übereinstimmen.
:::
:::

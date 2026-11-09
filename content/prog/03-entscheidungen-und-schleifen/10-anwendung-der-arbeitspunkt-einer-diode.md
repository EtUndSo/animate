---
title: Anwendung: der Arbeitspunkt einer Diode
pfad: Informatik / Programmieren / Python / Entscheidungen und Schleifen
knoten: Python 3: Entscheidungen und Schleifen
order: 6041000
summary: Bisektion und Newton sind nicht für Wurzeln gemacht, sondern für Gleichungen, die man nicht nach der Unbekannten auflösen kann.
tags: Arbeitspunkt
lang: de
---

<span class="anker" id="stufe-9"></span>

:::zweck
Bisektion und Newton sind nicht für Wurzeln gemacht, sondern für Gleichungen, die man nicht nach der Unbekannten auflösen kann. Dieser Abschnitt löst eine solche Gleichung aus der Elektrotechnik: den Strom durch eine Diode mit Vorwiderstand.
:::

### Was du dafür brauchst: Diodenkennlinie und Vorwiderstand

<span class="anker" id="stufe-9-1"></span>

Durch eine Siliziumdiode fließt in Durchlassrichtung der Strom

$$I_\mathrm D=I_\mathrm S\bigl(\mathrm{e}^{U/U_\mathrm T}-1\bigr).$$

Dabei ist $U$ die Spannung an der Diode, $I_\mathrm S$ der Sättigungsstrom, eine Eigenschaft der Diode, hier $10^{-12}$ A, und $U_\mathrm T=k_\mathrm BT/e_0$ die Temperaturspannung, mit der Boltzmann-Konstanten $k_\mathrm B$, der absoluten Temperatur $T$ und der Elementarladung $e_0$; bei $T=300$ K ist $U_\mathrm T\approx25{,}85$ mV. Die Kennlinie steigt wegen der Exponentialfunktion sehr steil an: Je 59,5 mV mehr Spannung verzehnfacht sich der Strom, denn $\mathrm{e}^{0{,}0595/0{,}02585}\approx10$.

Liegt die Diode in Reihe mit einem Widerstand $R$ an einer Spannungsquelle $U_0$, fällt am Widerstand die Spannung $U_0-U$ ab, und durch ihn fließt $I_R=(U_0-U)/R$. Weil es nur einen Weg für den Strom gibt, ist $I_R=I_\mathrm D$. Der Strom und die Spannung, die beide Gleichungen zugleich erfüllen, heißen der __Arbeitspunkt__. Ausführlich stehen Kennlinie und Arbeitspunkt in Grundlagen der Elektrotechnik, Teil 9.

⁠**Beispiel:** Mit $U_0=5$ V und $R=1$ $\mathrm{k\Omega}$ fließt bei $U=0{,}6$ V durch den Widerstand $4{,}4$ mA, durch die Diode aber nach der Kennlinie $10^{-12}\,\mathrm A\cdot(\mathrm{e}^{0{,}6/0{,}02585}-1)\approx12$ mA. Die Spannung $U=0{,}6$ V ist also zu hoch für den Arbeitspunkt.

⁠**Kurz gesagt:** Im Arbeitspunkt fließt durch Widerstand und Diode derselbe Strom.

### Der Arbeitspunkt als Nullstelle

<span class="anker" id="stufe-9-2"></span>

Zeichnet man den Strom durch den Widerstand und den Strom durch die Diode über $U$ auf, schneiden sich die beiden Kurven im Arbeitspunkt (Abb. [11](#abb-11)). Die Gerade heißt Arbeitsgerade.

:::abbildung prog/k3diode 11
Diodenkennlinie ($I_\mathrm S=10^{-12}$ A, $U_\mathrm T=25{,}85$ mV) und Arbeitsgerade für $U_0=5$ V und $R=1$ $\mathrm{k\Omega}$. Die Gerade fällt in diesem Ausschnitt kaum, weil fast die ganzen 5 V am Widerstand liegen. Ihr Schnittpunkt mit der Kennlinie ist der Arbeitspunkt.
:::

Den Schnittpunkt kann man als Nullstelle schreiben. Die Funktion

$$f(U)=\frac{U_0-U}{R}-I_\mathrm S\bigl(\mathrm{e}^{U/U_\mathrm T}-1\bigr)$$

ist der Überschuss des Widerstandsstroms über den Diodenstrom, und im Arbeitspunkt ist $f(U)=0$. Bei $U=0$ ist $f(0)=U_0/R=5$ mA $>0$, bei $U=U_0$ ist $f(U_0)=-I_\mathrm S(\mathrm{e}^{U_0/U_\mathrm T}-1)<0$. $f$ ist stetig, also liegt nach dem Zwischenwertsatz eine Nullstelle zwischen 0 und $U_0$. Es ist auch nur eine, denn beide Teile von $f$ fallen mit wachsendem $U$, $f$ ist also streng fallend. Nach $U$ auflösen lässt sich die Gleichung mit den üblichen Funktionen nicht, weil $U$ einmal frei und einmal im Exponenten steht.

⁠**Kurz gesagt:** Der Arbeitspunkt ist die einzige Nullstelle von $f(U)$ zwischen 0 und $U_0$.

:::hintergrund Gibt es doch eine Formel?
Es gibt eine, aber nur mit einer besonderen Funktion, der Lambertschen W-Funktion. Sie ist dadurch erklärt, dass $w=W(z)$ die Gleichung $w\,\mathrm{e}^w=z$ löst. Mit ihr ist

$$I=\frac{U_\mathrm T}{R}\,W\!\Bigl(\frac{I_\mathrm SR}{U_\mathrm T}\,\mathrm{e}^{(U_0+I_\mathrm SR)/U_\mathrm T}\Bigr)-I_\mathrm S .$$

Für die Zahlen dieses Abschnitts ist das Argument von $W$ etwa $3{,}9\cdot10^{76}$ und $W\approx171{,}2$, und es kommt derselbe Strom heraus wie mit den Verfahren unten. Die Standardbibliothek von Python kennt diese Funktion nicht, und um sie auszurechnen, braucht man selbst wieder ein Näherungsverfahren. Die Formel verschiebt die Schleife also nur an eine andere Stelle.
:::

### Der Arbeitspunkt durch Bisektion

<span class="anker" id="stufe-9-3"></span>

Die Bisektion braucht nur das Vorzeichen von $f$ und das Startintervall $[0,U_0]$. Hier ist $f(\mathit{lo})>0$, die Fälle in der Schleife sind also gegenüber der Wurzel vertauscht: Liegt der Widerstandsstrom in der Mitte noch über dem Diodenstrom, liegt der Arbeitspunkt rechts davon.

```python diode_bisektion.py
# Arbeitspunkt einer Diode mit Vorwiderstand: Nullstelle von f(U) durch Bisektion
import math
u0 = 5.0              # Quellenspannung in V
r = 1000.0            # Vorwiderstand in Ohm
i_s = 1e-12           # Sättigungsstrom der Diode in A
u_t = 0.02585         # Temperaturspannung in V, bei 300 K
eps = 1e-12           # Breite des Intervalls in V

lo = 0.0              # f(0) = u0/r > 0
hi = u0               # f(u0) < 0
schritte = 0
while hi - lo > eps:
    mitte = (lo + hi) / 2
    f = (u0 - mitte) / r - i_s * (math.exp(mitte / u_t) - 1)
    if f > 0:         # der Widerstand liefert mehr Strom, als die Diode bei mitte führt: U liegt höher
        lo = mitte
    else:
        hi = mitte
    schritte = schritte + 1
u = (lo + hi) / 2
print(f"U = {u:.6f} V, I = {(u0 - u) / r * 1000:.4f} mA nach {schritte} Schritten")
```

```console Linux
$ python3 diode_bisektion.py
U = 0.574147 V, I = 4.4259 mA nach 43 Schritten
```

Satz [7.3](die-bisektion.html#satz-7-3) sagt die Schrittzahl voraus: $\lceil\log_2(5\,\mathrm V/10^{-12}\,\mathrm V)\rceil=\lceil42{,}2\rceil=43$. Die Bisektion braucht dafür weder die Ableitung noch einen guten Startwert, nur den Vorzeichenwechsel.

⁠**Kurz gesagt:** Die Bisektion findet den Arbeitspunkt $U=0{,}5741$ V, $I=4{,}426$ mA sicher in 43 Schritten.

### Der Arbeitspunkt durch Newton

<span class="anker" id="stufe-9-4"></span>

Für das Newton-Verfahren braucht man die Ableitung

$$f'(U)=-\frac1R-\frac{I_\mathrm S}{U_\mathrm T}\,\mathrm{e}^{U/U_\mathrm T}.$$

Das Skript stoppt, sobald ein Newton-Schritt die Spannung um weniger als $10^{-12}$ V ändert, und hat eine Notbremse nach 1000 Schritten. Den Startwert fragt es ab:

```python diode_newton.py
# Arbeitspunkt einer Diode mit Vorwiderstand: Nullstelle von f(U) mit dem Newton-Verfahren
import math
u0 = 5.0              # Quellenspannung in V
r = 1000.0            # Vorwiderstand in Ohm
i_s = 1e-12           # Sättigungsstrom der Diode in A
u_t = 0.02585         # Temperaturspannung in V, bei 300 K

u = float(input("Startwert in V: "))
schritt = 1.0         # Länge des letzten Newton-Schritts in V, zu Beginn beliebig groß
schritte = 0
while abs(schritt) > 1e-12 and schritte < 1000:
    f = (u0 - u) / r - i_s * (math.exp(u / u_t) - 1)
    f_strich = -1 / r - i_s / u_t * math.exp(u / u_t)
    schritt = -f / f_strich
    u = u + schritt
    schritte = schritte + 1
print(f"U = {u:.6f} V nach {schritte} Schritten")
```

```console Linux
$ python3 diode_newton.py
Startwert in V: 0.7
U = 0.574147 V nach 10 Schritten
$ python3 diode_newton.py
Startwert in V: 5
U = 0.574147 V nach 177 Schritten
$ python3 diode_newton.py
Startwert in V: 0
U = 0.574147 V nach 178 Schritten
```

Mit einem Startwert in der Nähe, 0,7 V, braucht Newton 10 Schritte. Von $U_0=5$ V aus sind es 177, viermal so viele wie bei der Bisektion. Der Grund ist die Exponentialfunktion: Weit oberhalb des Arbeitspunkts ist der Diodenstrom riesig, und $f$ und $f'$ bestehen fast nur aus ihm. Dann ist $f(U)/f'(U)\approx U_\mathrm T$, und jeder Newton-Schritt senkt die Spannung nur um etwa 25,85 mV. Von 5 V bis 0,57 V sind das $(5-0{,}57)/0{,}02585\approx171$ Schritte, bevor die schnelle Phase beginnt. Vom Startwert 0 aus springt der erste Schritt fast genau auf 5 V, weil die Diode bei 0 V kaum Strom führt und die Tangente fast nur die flache Arbeitsgerade sieht; danach geht es wie vom Startwert 5 V weiter.

Daraus folgt die übliche Arbeitsteilung: Man grenzt die Lösung mit einer sicheren Methode oder mit Vorwissen ein, für Siliziumdioden etwa 0,5 V bis 0,8 V, und lässt dann Newton die letzten Stellen holen.

⁠**Kurz gesagt:** Nahe am Arbeitspunkt gestartet, braucht Newton 10 Schritte; weit weg kriecht es in Schritten von $U_\mathrm T$ und ist langsamer als die Bisektion.

:::hintergrund Wie Schaltungssimulatoren das Problem lösen
Schaltungssimulatoren wie SPICE stellen für eine Schaltung die Gleichungen aller Knoten auf und lösen sie mit dem Newton-Verfahren, für viele Unbekannte zugleich. Dioden und Transistoren machen dabei genau die Schwierigkeiten dieses Abschnitts: Ein zu großer Spannungsschritt lässt $\mathrm{e}^{U/U_\mathrm T}$ riesig werden oder sogar über den größten `float` hinauswachsen, und die Iteration kriecht oder springt. Die Simulatoren begrenzen deshalb, wie weit sich die Spannung an einem pn-Übergang in einem Schritt erhöhen darf. Schlägt Newton oberhalb einer kritischen Spannung einen großen Schritt $\Delta U$ nach oben vor, wird er auf etwa $U_\mathrm T\ln(1+\Delta U/U_\mathrm T)$ verkürzt. Der Diodenstrom wächst dann in einem Schritt nur so stark, als wäre die Kennlinie dort eine Gerade, und das Verfahren bleibt in der Nähe des Bereichs, in dem es schnell ist. Wie leicht die Exponentialfunktion überläuft, zeigt schon $U_0=20$ V:

```console
>>> import math
>>> math.exp(20 / 0.02585)
Traceback (most recent call last):
  File "<python-input-1>", line 1, in <module>
    math.exp(20 / 0.02585)
    ~~~~~~~~^^^^^^^^^^^^^^
OverflowError: math range error
```
:::

### Aufgaben zu Abschnitt [9](#stufe-9)

<span class="anker" id="stufe-9-5"></span>

:::aufgabe Aufgabe 34 ★★★ Ein anderer Arbeitspunkt
<span class="anker" id="aufg-34"></span>

Dieselbe Diode liegt mit $R=2{,}2$ $\mathrm{k\Omega}$ an $U_0=12$ V.

<ol class="al">

<li>

Sage mit Satz [7.3](die-bisektion.html#satz-7-3) voraus, wie viele Schritte die Bisektion mit $\varepsilon=10^{-9}$ V braucht. Bestimme dann $U$ und $I$ mit der Bisektion.

</li>

<li>

Bestimme den Arbeitspunkt mit Newton, einmal vom Startwert 0,6 V und einmal von 12 V. Schätze die zweite Schrittzahl vorher ab.

</li>

<li>

Der Strom ist etwa 17 % größer als im Beispiel mit 5 V. Um wie viel ändert sich die Diodenspannung? Erkläre das Ergebnis mit der Kennlinie.

</li>

</ol>

:::loesung
(a) $\lceil\log_2(12\,\mathrm V/10^{-9}\,\mathrm V)\rceil=\lceil33{,}5\rceil=34$. Das Skript ist `diode_bisektion.py` mit den neuen Werten und `eps = 1e-9`:

```console Linux
$ python3 diode12_bisektion.py
U = 0.578273 V, I = 5.1917 mA nach 34 Schritten
```

(b) Vom Startwert 12 V aus geht Newton in Schritten von etwa $U_\mathrm T$ abwärts, das sind etwa $(12-0{,}58)/0{,}02585\approx442$ Schritte und einige für die letzten Stellen. Das Skript `diode12_newton.py` ist `diode_newton.py` mit den neuen Werten:

```console Linux
$ python3 diode12_newton.py
Startwert in V: 0.6
U = 0.578273 V nach 6 Schritten
$ python3 diode12_newton.py
Startwert in V: 12
U = 0.578273 V nach 447 Schritten
```

(c) Die Diodenspannung steigt nur um $0{,}578273-0{,}574147=0{,}0041$ V, also 4,1 mV, obwohl der Strom von 4,426 mA auf 5,192 mA steigt. Im Durchlassbereich ist $I\approx I_\mathrm S\mathrm{e}^{U/U_\mathrm T}$, also $U\approx U_\mathrm T\ln(I/I_\mathrm S)$: Die Spannung hängt nur logarithmisch vom Strom ab. Ein Stromverhältnis von $5{,}192/4{,}426=1{,}173$ ergibt $U_\mathrm T\ln1{,}173=25{,}85\,\mathrm{mV}\cdot0{,}160=4{,}1$ mV. Deshalb rechnet man in Überschlägen oft mit einer festen Diodenspannung.
:::
:::

:::aufgabe Aufgabe 35 ★★ Wenn die Exponentialfunktion überläuft
<span class="anker" id="aufg-35"></span>

Setze in `diode_newton.py` $U_0=20$ V und starte mit dem Startwert 20. Was passiert, und warum? Läuft `diode_bisektion.py` mit $U_0=20$ V? Begründe mit der Mitte des ersten Intervalls und rechne nach.

:::loesung
Mit dem Startwert 20 V muss Python im ersten Schritt $\mathrm{e}^{20/0{,}02585}=\mathrm{e}^{773{,}7}$ ausrechnen, und das liegt weit über dem größten `float` von etwa $1{,}8\cdot10^{308}=\mathrm{e}^{709{,}8}$ ([Programmieren, Python 2, Abschnitt 5.5](/wissen/informatik/programmieren/python/werte-typen-und-variablen/rechnen-mit-gleitkommazahlen.html#stufe-5-5)). `math.exp` meldet den Überlauf mit einer Ausnahme:

```console Linux
$ python3 diode20_newton.py
Startwert in V: 20
Traceback (most recent call last):
  File "/home/student/python-kurs/diode20_newton.py", line 11, in <module>
    f = (u0 - u) / r - i_s * (math.exp(u / u_t) - 1)
                              ~~~~~~~~^^^^^^^^^
OverflowError: math range error
```

Die Bisektion läuft dagegen. Sie berechnet $f$ nie am Rand `hi`, sondern nur in den Mitten, und schon die erste Mitte, 10 V, ergibt $\mathrm{e}^{386{,}8}\approx10^{168}$, das ist darstellbar. Danach liegen alle Mitten unter 10 V:

```console Linux
$ python3 diode20_bisektion.py
U = 0.612332 V, I = 19.3877 mA nach 45 Schritten
```

Die Schrittzahl ist $\lceil\log_2(20/10^{-12})\rceil=\lceil44{,}2\rceil=45$. Newton mit einem vernünftigen Startwert kommt zum selben Ergebnis:

```console Linux
$ python3 diode20_newton.py
Startwert in V: 0.7
U = 0.612332 V nach 9 Schritten
```
:::
:::

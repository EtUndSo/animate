---
title: Die Bisektion
pfad: Informatik / Programmieren / Python / Entscheidungen und Schleifen
knoten: Python 3: Entscheidungen und Schleifen
order: 6040800
summary: Das Schrittverfahren tastet sich mit festen Schritten an die Lösung heran und ist deshalb langsam.
tags: stetig, Bisektion, Schleifeninvariante
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Das Schrittverfahren tastet sich mit festen Schritten an die Lösung heran und ist deshalb langsam. Dieser Abschnitt zeigt ein Verfahren, das den Bereich, in dem die Lösung liegen muss, in jedem Schritt halbiert, und bestimmt, wie viele Schritte es braucht.
:::

### Was du dafür brauchst: der Zwischenwertsatz

<span class="anker" id="stufe-7-1"></span>

Die Wurzel $\sqrt a$ ist die positive Nullstelle der Funktion $f(x)=x^2-a$, denn $f(\sqrt a)=0$. Statt nach einer Wurzel kann man also nach einer Nullstelle suchen. Woran erkennt man, dass in einem Intervall eine Nullstelle liegt?

Eine Funktion heißt __stetig__ auf einem Intervall $[x_1,x_2]$, wenn ihr Graph dort ohne Sprung verläuft, wenn man ihn also zeichnen kann, ohne den Stift abzusetzen. Für solche Funktionen gilt:

:::satz Satz 7.1 (Zwischenwertsatz, Fassung für Nullstellen)
<span class="anker" id="satz-7-1"></span>

Ist $f$ stetig auf $[x_1,x_2]$ und haben $f(x_1)$ und $f(x_2)$ verschiedene Vorzeichen, dann gibt es mindestens eine Zahl $x^*$ mit $x_1<x^*<x_2$ und $f(x^*)=0$.
:::

Anschaulich: Wer ohne abzusetzen von unterhalb der $x$-Achse nach oberhalb zeichnet, muss sie irgendwo kreuzen. Ausführlich steht der Satz in Höhere Mathematik 1, Teil 5, Abschnitt 8.

⁠**Beispiel:** $f(x)=x^2-2$ ist stetig, und es ist $f(0)=-2<0$ und $f(2)=2>0$. Also hat $f$ zwischen 0 und 2 eine Nullstelle, nämlich $\sqrt2$.

⁠**Kurz gesagt:** Wechselt eine stetige Funktion zwischen zwei Stellen das Vorzeichen, liegt dazwischen eine Nullstelle.

### Das Bisektionsverfahren

<span class="anker" id="stufe-7-2"></span>

Der Zwischenwertsatz sagt, dass eine Nullstelle im Intervall liegt, aber nicht, wo. Die Bisektion findet sie, indem sie das Intervall immer wieder teilt.

**Zahlenraten mit „größer oder kleiner“.** Jemand denkt sich eine Zahl zwischen 1 und 100 und antwortet nur mit „größer“ oder „kleiner“. Wer immer die Mitte des noch möglichen Bereichs rät, halbiert ihn mit jeder Antwort und hat die Zahl nach höchstens 7 Fragen, denn $2^7=128\ge100$. Die Bisektion rät auf dieselbe Weise; die Antwort gibt ihr das Vorzeichen von $f$ in der Mitte (Abb. [8](#abb-8)).

:::abbildung prog/k3bisektion 8
Bisektion für $\sqrt2$ als Intervallschachtelung. Jede Zeile zeigt das Intervall vor einem Schritt (blau) und seine Mitte (schwarzer Strich). Ist das Quadrat der Mitte kleiner als 2, wird die Mitte zur neuen linken Grenze, sonst zur neuen rechten. Jedes Intervall ist halb so breit wie das vorige und enthält immer $\sqrt2$ (rot gestrichelt).
:::

:::definition Definition 7.2 (Bisektion)
<span class="anker" id="satz-7-2"></span>

Gegeben sind eine stetige Funktion $f$, zwei Zahlen $\mathit{lo}<\mathit{hi}$ mit $f(\mathit{lo})<0\le f(\mathit{hi})$ und eine Toleranz $\varepsilon>0$. Die __Bisektion__ wiederholt, solange $\mathit{hi}-\mathit{lo}>\varepsilon$ ist:

<ol>

<li>

Berechne die Mitte $m=(\mathit{lo}+\mathit{hi})/2$.

</li>

<li>

Ist $f(m)<0$, setze $\mathit{lo}=m$, sonst $\mathit{hi}=m$.

</li>

</ol>

Das Ergebnis ist die Mitte des letzten Intervalls. Ist das Vorzeichen andersherum, $f(\mathit{lo})>0\ge f(\mathit{hi})$, vertauscht man in Schritt 2 die beiden Fälle.
:::

Nach jedem Schritt gilt wieder $f(\mathit{lo})<0\le f(\mathit{hi})$: Die Grenze, die durch die Mitte ersetzt wird, ist immer die mit demselben Vorzeichen wie $f(m)$. Nach dem Zwischenwertsatz enthält das Intervall deshalb stets eine Nullstelle, oder seine rechte Grenze ist selbst eine.

**Beispiel.** Die ersten sechs Schritte für $f(x)=x^2-2$ mit $\mathit{lo}=0$ und $\mathit{hi}=2$:

| Schritt | $\mathit{lo}$ | $\mathit{hi}$ | $m$ | $m^2$ | neues Intervall |
|---|---|---|---|---|---|
| 1 | 0 | 2 | 1 | 1 | $[1;\,2]$ |
| 2 | 1 | 2 | 1,5 | 2,25 | $[1;\,1{,}5]$ |
| 3 | 1 | 1,5 | 1,25 | 1,5625 | $[1{,}25;\,1{,}5]$ |
| 4 | 1,25 | 1,5 | 1,375 | 1,890625 | $[1{,}375;\,1{,}5]$ |
| 5 | 1,375 | 1,5 | 1,4375 | 2,06640625 | $[1{,}375;\,1{,}4375]$ |
| 6 | 1,375 | 1,4375 | 1,40625 | 1,9775390625 | $[1{,}40625;\,1{,}4375]$ |

Nach sechs Schritten ist das Intervall $2/2^6=0{,}03125$ breit, und $\sqrt2\approx1{,}4142$ liegt darin.

⁠**Kurz gesagt:** Die Bisektion ersetzt in jedem Schritt die Intervallgrenze, die auf derselben Seite der Nullstelle liegt wie die Mitte, durch die Mitte.

:::hintergrund Warum die Bisektion nicht danebenliegen kann: die Schleifeninvariante
Um zu zeigen, dass eine Schleife das Richtige berechnet, sucht man eine Aussage, die vor dem ersten Durchlauf gilt und die jeder Durchlauf erhält. Eine solche Aussage heißt __Schleifeninvariante__. Bei der Bisektion ist es „$f(\mathit{lo})<0\le f(\mathit{hi})$“. Sie gilt am Anfang nach Voraussetzung, und jeder Durchlauf erhält sie, wie oben gezeigt. Also gilt sie auch nach dem letzten Durchlauf. Dann gilt zusätzlich die Abbruchbedingung, $\mathit{hi}-\mathit{lo}\le\varepsilon$. Beides zusammen heißt: Im Intervall $(\mathit{lo},\mathit{hi}]$ der Breite höchstens $\varepsilon$ liegt eine Nullstelle, und die Mitte ist höchstens $\varepsilon/2$ von ihr entfernt. Dass die Schleife überhaupt endet, folgt aus einer zweiten Beobachtung: Die Breite halbiert sich in jedem Durchlauf und wird deshalb irgendwann kleiner als jedes positive $\varepsilon$. Dieses Vorgehen, Invariante plus eine Größe, die sicher abnimmt, ist die übliche Art, Schleifen zu begründen, nicht nur bei der Bisektion.
:::

### Die Wurzel durch Bisektion

<span class="anker" id="stufe-7-3"></span>

Als Skript braucht die Bisektion für $\sqrt a$ ein Startintervall mit Vorzeichenwechsel. Links passt immer $\mathit{lo}=0$, denn $f(0)=-a<0$. Rechts passt $\mathit{hi}=\max(1,a)$: Für $a\ge1$ ist $a^2\ge a$, also $f(a)\ge0$; für $a<1$ ist $f(1)=1-a>0$.

```python wurzel_bisektion.py
# Quadratwurzel durch Bisektion: Nullstelle von f(x) = x*x - a im Intervall [lo, hi]
a = float(input("a = "))
eps = float(input("Toleranz eps = "))     # gewünschte Breite des Intervalls
lo = 0.0                                  # f(lo) < 0
hi = max(1.0, a)                          # f(hi) >= 0, denn die Wurzel liegt nie über max(1, a)
schritte = 0
while hi - lo > eps:
    mitte = (lo + hi) / 2
    if mitte * mitte < a:                 # f(mitte) < 0: die Nullstelle liegt rechts von mitte
        lo = mitte
    else:                                 # sonst liegt sie links von mitte oder genau dort
        hi = mitte
    schritte = schritte + 1
print("Näherung:", (lo + hi) / 2, "nach", schritte, "Schritten")
print("Intervall:", lo, "bis", hi)
```

```console Linux
$ python3 wurzel_bisektion.py
a = 2
Toleranz eps = 1e-12
Näherung: 1.414213562372879 nach 41 Schritten
Intervall: 1.4142135623724243 bis 1.4142135623733338
$ python3 wurzel_bisektion.py
a = 25
Toleranz eps = 0.01
Näherung: 5.0018310546875 nach 12 Schritten
Intervall: 4.998779296875 bis 5.0048828125
```

Für $\sqrt2$ genügen 41 Schritte, und das Ergebnis weicht nur um $2{,}2\cdot10^{-13}$ von $\sqrt2$ ab. Für $\sqrt{25}$ mit der Toleranz 0,01 sind es 12 Schritte statt der 49 990 des Schrittverfahrens. Die Toleranz bedeutet hier etwas anderes als dort: Sie begrenzt die Breite des Intervalls für $g$, nicht den Abstand von $g^2$ zu $a$.

⁠**Kurz gesagt:** Mit dem Startintervall $[0,\max(1,a)]$ findet die Bisektion $\sqrt2$ in 41 Schritten auf zwölf Stellen.

### Die Schrittzahl der Bisektion

<span class="anker" id="stufe-7-4"></span>

41 und 12: Diese Zahlen lassen sich vor dem Start ausrechnen.

:::satz Satz 7.3 (Schrittzahl der Bisektion)
<span class="anker" id="satz-7-3"></span>

Beginnt die Bisektion mit einem Intervall der Breite $L=\mathit{hi}-\mathit{lo}$, so ist das Intervall nach $n$ Schritten $L/2^n$ breit. Ist $L>\varepsilon$, endet sie nach

$$n=\Bigl\lceil\log_2\frac{L}{\varepsilon}\Bigr\rceil$$

Schritten, und die zurückgegebene Mitte ist höchstens $\varepsilon/2$ von einer Nullstelle entfernt.
:::

:::beweis Halbieren
Jeder Schritt ersetzt eine Grenze durch die Mitte, das Intervall wird also genau halb so breit. Nach $n$ Schritten ist es $L/2^n$ breit. Die Schleife läuft, solange die Breite größer als $\varepsilon$ ist, und endet nach dem ersten $n$ mit $L/2^n\le\varepsilon$, also mit $2^n\ge L/\varepsilon$ oder $n\ge\log_2(L/\varepsilon)$. Das kleinste solche $n$ ist die aufgerundete Zahl $\lceil\log_2(L/\varepsilon)\rceil$. Nach der Schleifeninvariante liegt im letzten Intervall eine Nullstelle, und die Mitte ist von jedem Punkt des Intervalls höchstens die halbe Breite, also höchstens $\varepsilon/2$, entfernt.
:::

Der Beweis rechnet mit exakten Mitten. In allen Beispielen dieses Kapitels sind die Mitten als `float` exakt darstellbar, denn sie sind Brüche mit Zweierpotenzen im Nenner und haben weniger als 53 Binärstellen.

**Beispiel.** Für $\sqrt2$ mit $[0,2]$ und $\varepsilon=10^{-12}$ ist $L/\varepsilon=2\cdot10^{12}$ und $\log_2(2\cdot10^{12})=40{,}86$, aufgerundet 41. Für $\sqrt{25}$ mit $[0,25]$ und $\varepsilon=0{,}01$ ist $\log_2 2500=11{,}29$, aufgerundet 12. Beides sind genau die Schrittzahlen der Skripte.

⁠**Kurz gesagt:** Die Bisektion braucht $\lceil\log_2(L/\varepsilon)\rceil$ Schritte; jede Verzehnfachung der Genauigkeit kostet nur etwa 3,3 Schritte mehr.

:::hintergrund Warum Halbieren so viel schneller ist als Abtasten
Das Schrittverfahren aus Abschnitt [6](losungen-durch-probieren-raten-und-prufen-naherung-mit-toleranz.html#stufe-6) verkleinert den Bereich, in dem die Lösung noch liegen kann, in jedem Schritt um ein festes Stück $h$; die Zahl der Schritte wächst deshalb wie $L/h$. Die Bisektion halbiert den Bereich. Mit $n$ Schritten unterscheidet sie $2^n$ gleich breite Teilintervalle, und welches davon die Lösung enthält, legen die $n$ Ja-Nein-Antworten fest. Zehn Schritte unterscheiden schon $2^{10}=1024$, also etwa $10^3$ Teilintervalle, das sind drei Dezimalstellen. Für zwölf Stellen braucht man etwa $4\cdot10=40$ Schritte, statt $2\cdot10^{12}$ beim Abtasten mit der Schrittweite $\varepsilon$.

Was diese Antworten sind, sieht man an der Tabelle in Unterabschnitt [7.2](#stufe-7-2). Schreibt man für „die Mitte wird linke Grenze“ eine 1 und für „die Mitte wird rechte Grenze“ eine 0, ergeben die ersten zwölf Schritte für $\sqrt2$ die Folge `1 0 1 1 0 1 0 1 0 0 0 0`. Das sind genau die ersten zwölf Binärziffern von $\sqrt2=1{,}01101010000\ldots_2$ ([Programmieren, Python 2, Abschnitt 3.6](/wissen/informatik/programmieren/python/werte-typen-und-variablen/zahlen-im-binarsystem.html#stufe-3-6)). Jeder Schritt der Bisektion bestimmt also ein weiteres Bit der Lösung, nicht mehr und nicht weniger.
:::

:::hintergrund Wie klein die Toleranz sein darf
Die Breite des Intervalls kann nicht unter den Abstand benachbarter `float` sinken. Bei $\sqrt2$ ist dieser Abstand $\varepsilon_{\mathrm M}=2{,}2\cdot10^{-16}$. Verlangt man $\varepsilon=10^{-17}$, sind $\mathit{lo}$ und $\mathit{hi}$ nach 53 Schritten Nachbarn, `1.414213562373095` und `1.4142135623730951`. Ihre gerundete Mitte ist wieder einer der beiden, das Intervall wird nicht mehr kleiner, und die Bedingung `hi - lo > eps` bleibt für immer wahr: eine Endlosschleife. Abhilfe schaffen eine Toleranz, die zur Größe der Lösung passt, etwa `hi - lo > 1e-15 * hi` wie beim Vergleich mit relativer Toleranz in [Programmieren, Python 2, Abschnitt 7.4](/wissen/informatik/programmieren/python/werte-typen-und-variablen/wahrheitswerte-und-vergleiche.html#stufe-7-4), oder eine Höchstzahl von Schritten als Notbremse.
:::

### Aufgaben zu Abschnitt [7](#stufe-7)

<span class="anker" id="stufe-7-5"></span>

:::aufgabe Aufgabe 27 ★ Bisektion von Hand
<span class="anker" id="aufg-27"></span>

Führe vier Schritte der Bisektion für $\sqrt3$ von Hand aus, mit $f(x)=x^2-3$ und dem Startintervall $[1,2]$. Lege eine Tabelle an wie in Unterabschnitt [7.2](#stufe-7-2). Wie breit ist das letzte Intervall, und welche Näherung liefert seine Mitte?

:::loesung
| Schritt | $\mathit{lo}$ | $\mathit{hi}$ | $m$ | $m^2$ | neues Intervall |
|---|---|---|---|---|---|
| 1 | 1 | 2 | 1,5 | 2,25 | $[1{,}5;\,2]$ |
| 2 | 1,5 | 2 | 1,75 | 3,0625 | $[1{,}5;\,1{,}75]$ |
| 3 | 1,5 | 1,75 | 1,625 | 2,640625 | $[1{,}625;\,1{,}75]$ |
| 4 | 1,625 | 1,75 | 1,6875 | 2,84765625 | $[1{,}6875;\,1{,}75]$ |

Das letzte Intervall ist $1/2^4=0{,}0625$ breit. Seine Mitte 1,71875 weicht um 0,013 von $\sqrt3\approx1{,}73205$ ab, weniger als die halbe Breite 0,03125, wie Satz [7.3](#satz-7-3) verspricht.
:::
:::

:::aufgabe Aufgabe 28 ★★ Schrittzahlen vorhersagen
<span class="anker" id="aufg-28"></span>

Berechne mit Satz [7.3](#satz-7-3), wie viele Schritte `wurzel_bisektion.py` braucht, und prüfe dann am Rechner: (a) $a=10$, $\varepsilon=10^{-6}$; (b) $a=1000$, $\varepsilon=10^{-9}$; (c) $a=2$, $\varepsilon=5\cdot10^{-13}$; (d) $a=2$, $\varepsilon=10^{-13}$. Wie viele Schritte kostet jede Halbierung von $\varepsilon$, wie viele jede Verzehntelung?

:::loesung
Mit $L=\max(1,a)$: (a) $\lceil\log_2(10/10^{-6})\rceil=\lceil23{,}25\rceil=24$; (b) $\lceil\log_2(1000/10^{-9})\rceil=\lceil39{,}86\rceil=40$; (c) $\lceil\log_2(2/(5\cdot10^{-13}))\rceil=\lceil41{,}86\rceil=42$; (d) $\lceil\log_2(2/10^{-13})\rceil=\lceil44{,}19\rceil=45$.

```console Linux
$ python3 wurzel_bisektion.py
a = 10
Toleranz eps = 1e-6
Näherung: 3.162277638912201 nach 24 Schritten
Intervall: 3.162277340888977 bis 3.162277936935425
$ python3 wurzel_bisektion.py
a = 1000
Toleranz eps = 1e-9
Näherung: 31.62277660203472 nach 40 Schritten
Intervall: 31.62277660157997 bis 31.622776602489466
$ python3 wurzel_bisektion.py
a = 2
Toleranz eps = 5e-13
Näherung: 1.4142135623731065 nach 42 Schritten
Intervall: 1.414213562372879 bis 1.4142135623733338
$ python3 wurzel_bisektion.py
a = 2
Toleranz eps = 1e-13
Näherung: 1.414213562373078 nach 45 Schritten
Intervall: 1.4142135623730496 bis 1.4142135623731065
```

Jede Halbierung von $\varepsilon$ kostet genau einen Schritt (von 41 auf 42), denn $\log_2(2x)=\log_2x+1$. Jede Verzehntelung kostet $\log_2 10\approx3{,}32$ Schritte, also drei oder vier (von 42 bei $5\cdot10^{-13}$ zu 45 bei $10^{-13}$ sind es drei, weil der Faktor dort nur 5 ist; von 41 bei $10^{-12}$ zu 45 bei $10^{-13}$ sind es vier).
:::
:::

:::aufgabe Aufgabe 29 ★★ Nullstellen ohne Wurzel
<span class="anker" id="aufg-29"></span>

Die Bisektion funktioniert für jede stetige Funktion mit Vorzeichenwechsel.

<ol class="al">

<li>

Finde mit der Bisektion die Zahl $x$ mit $\cos x=x$ im Intervall $[0,1]$, also die Nullstelle von $f(x)=\cos x-x$, mit $\varepsilon=10^{-12}$. Prüfe zuerst den Vorzeichenwechsel. Achtung: Hier ist $f(\mathit{lo})>0$.

</li>

<li>

Ebenso die Nullstelle von $x^3-x-1$ in $[1,2]$.

</li>

</ol>

:::loesung
(a) $f(0)=\cos0-0=1>0$ und $f(1)=\cos1-1\approx-0{,}46<0$: Es gibt einen Vorzeichenwechsel. Weil $f(\mathit{lo})>0$ ist, wird `lo` ersetzt, wenn $f$ in der Mitte noch positiv ist:

```python bisektion_cos.py
# Bisektion für cos(x) = x, also die Nullstelle von f(x) = cos(x) - x in [0, 1]; hier ist f(lo) > 0
import math
lo = 0.0                                  # f(0) = 1 > 0
hi = 1.0                                  # f(1) = cos(1) - 1 < 0
eps = 1e-12
schritte = 0
while hi - lo > eps:
    mitte = (lo + hi) / 2
    if math.cos(mitte) - mitte > 0:       # f(mitte) > 0: die Nullstelle liegt rechts von mitte
        lo = mitte
    else:
        hi = mitte
    schritte = schritte + 1
x = (lo + hi) / 2
print("x =", x, "nach", schritte, "Schritten, cos(x) - x =", math.cos(x) - x)
```

```console Linux
$ python3 bisektion_cos.py
x = 0.7390851332152124 nach 40 Schritten, cos(x) - x = -8.659739592076221e-14
```

Die Schrittzahl ist $\lceil\log_2(1/10^{-12})\rceil=\lceil39{,}86\rceil=40$.

(b) $f(1)=-1<0$, $f(2)=5>0$, wie bei der Wurzel:

```python bisektion_kubisch.py
# Bisektion für die Nullstelle von f(x) = x**3 - x - 1 in [1, 2]
lo = 1.0                                  # f(1) = -1 < 0
hi = 2.0                                  # f(2) = 5 > 0
eps = 1e-12
schritte = 0
while hi - lo > eps:
    mitte = (lo + hi) / 2
    if mitte ** 3 - mitte - 1 < 0:
        lo = mitte
    else:
        hi = mitte
    schritte = schritte + 1
x = (lo + hi) / 2
print("x =", x, "nach", schritte, "Schritten")
```

```console Linux
$ python3 bisektion_kubisch.py
x = 1.3247179572449568 nach 40 Schritten
```

Auch hier 40 Schritte, denn das Intervall ist wieder 1 breit. Die Bisektion braucht von der Funktion nur das Vorzeichen; ob es eine Wurzel, ein Kosinus oder ein Polynom ist, spielt keine Rolle.
:::
:::

:::aufgabe Aufgabe 30 ★★★ Eine zu kleine Toleranz
<span class="anker" id="aufg-30"></span>

Starte die Bisektion für $\sqrt2$ mit $\varepsilon=10^{-17}$ und einer Notbremse nach 200 Schritten. Gib nach der Schleife `lo`, `hi`, `hi - lo` und die Zahl der Schritte aus. Erkläre das Ergebnis. Ersetze dann die Bedingung durch `hi - lo > 1e-15 * hi` und bestimme die Schrittzahl, auch mit Satz [7.3](#satz-7-3).

:::loesung
```python bisektion_eps.py
# Bisektion für die Wurzel aus 2 mit zu kleiner Toleranz, mit einer Notbremse nach 200 Schritten
lo = 0.0
hi = 2.0
eps = 1e-17
schritte = 0
while hi - lo > eps and schritte < 200:
    mitte = (lo + hi) / 2
    if mitte * mitte < 2:
        lo = mitte
    else:
        hi = mitte
    schritte = schritte + 1
print("lo =", lo, " hi =", hi)
print("hi - lo =", hi - lo, " Schritte:", schritte)

lo = 0.0                                  # dasselbe mit relativer Toleranz
hi = 2.0
schritte = 0
while hi - lo > 1e-15 * hi:
    mitte = (lo + hi) / 2
    if mitte * mitte < 2:
        lo = mitte
    else:
        hi = mitte
    schritte = schritte + 1
print("relativ: Näherung", (lo + hi) / 2, "nach", schritte, "Schritten")
```

```console Linux
$ python3 bisektion_eps.py
lo = 1.414213562373095  hi = 1.4142135623730951
hi - lo = 2.220446049250313e-16  Schritte: 200
relativ: Näherung 1.4142135623730954 nach 51 Schritten
```

Mit $\varepsilon=10^{-17}$ endet die Schleife nur durch die Notbremse. `lo` und `hi` sind benachbarte `float` mit dem Abstand $\varepsilon_{\mathrm M}=2{,}2\cdot10^{-16}$; ihre Mitte ist nicht darstellbar und wird auf einen der beiden gerundet, sodass sich nichts mehr ändert. Mit der relativen Toleranz endet die Schleife, sobald die Breite höchstens $10^{-15}\cdot\mathit{hi}\approx1{,}41\cdot10^{-15}$ ist. Nach Satz [7.3](#satz-7-3) mit diesem $\varepsilon$: $\lceil\log_2(2/(1{,}41\cdot10^{-15}))\rceil=\lceil50{,}3\rceil=51$. Die Näherung `1.4142135623730954` ist der Nachbar oberhalb von `math.sqrt(2)`, also eine Stufe neben dem besten Wert und gut innerhalb der verlangten Genauigkeit.
:::
:::

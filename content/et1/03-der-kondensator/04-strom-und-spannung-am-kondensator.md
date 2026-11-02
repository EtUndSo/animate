---
title: Stufe 3: Strom und Spannung am Kondensator
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Der Kondensator
order: 1130400
summary: Am Widerstand legt die Spannung den Strom im selben Moment fest.
tags: Stromquelle
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Am Widerstand legt die Spannung den Strom im selben Moment fest. Am Kondensator ist das anders: Hier hängt der Strom daran, wie schnell die Spannung sich ändert. Diese Stufe stellt das Gesetz auf.
:::

**Die Idee.** Die Spannung zeigt an, wie viel Ladung bisher hineingeflossen ist. Strom ändert diese Ladung. Fließt viel Strom, steigt die Spannung schnell. Fließt keiner, bleibt sie stehen, auch wenn sie hoch ist. Der Strom folgt also nicht aus dem Wert der Spannung, sondern aus ihrer Änderung.

:::satz Satz 3.1 (Strom und Spannung am Kondensator)
<span class="anker" id="satz-3-1"></span>

Mit Strom- und Spannungszählpfeil in gleicher Richtung ([Teil 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)) gilt für zeitabhängige Größen

<span class="anker" id="gl-3-1"></span>
<span class="anker" id="gl-3-2"></span>
$$\begin{aligned} i(t)&=\frac{\mathrm{d} q}{\mathrm{d} t}=C\,\frac{\mathrm{d} u(t)}{\mathrm{d} t},\\ u(t)&=\frac{q(t)}{C}=u(t_0)+\frac1C\int_{t_0}^{t}i(t')\,\mathrm{d} t'. \end{aligned} \tag{3.1|3.2}$$
:::

:::herleitung Strom und Spannung
Strom ist Ladung je Zeit, $i=\mathrm{d} q/\mathrm{d} t$ ([Teil 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)). Einsetzen von $q=C\,u$ und Herausziehen der konstanten Zahl $C$ ergibt [(3.1)](#gl-3-1). Umgekehrt ist die Ladung die Fläche unter der Stromkurve, wie der Weg die Fläche unter der Geschwindigkeit ist ([Teil 1](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)): $q(t)=q(t_0)+\int_{t_0}^{t}i\,\mathrm{d} t'$. Teilen durch $C$ ergibt [(3.2)](#gl-3-2).
:::

⁠**So liest man das:** Kleinbuchstaben stehen für zeitabhängige Größen, $t'$ ist die Integrationsvariable, $u(t_0)$ die Spannung zur Startzeit. $i$ in A, $C$ in F, $\mathrm{d} u/\mathrm{d} t$ in V/s. 1 mA an 100 µF lässt die Spannung um 10 V/s steigen. **Vorzeichen:** $q$ ist die Ladung der Platte, in die der Strompfeil hineinzeigt. Bei $i>0$ wächst sie und $u$ steigt, bei $i<0$ sinkt $u$. **Gültigkeit:** $C$ muss konstant sein.

**Zwei Folgerungen.** Erstens: **Die Spannung springt nicht.** Ein Sprung um $\Delta U$ in der Zeit $\Delta t$ verlangt $i=C\,\Delta U/\Delta t$. Für $\Delta t\to0$ wüchse der Strom unbegrenzt, denn die Ladung $C\,\Delta U$ müsste in null Zeit ankommen. 9 V in 1 µs an 100 µF verlangen schon 900 A. Der Strom darf dagegen springen, denn er ist nicht an eine gespeicherte Größe gebunden. Zweitens: **Bei konstanter Spannung fließt kein Strom.** Mit $\mathrm{d} u/\mathrm{d} t=0$ ist $i=0$, der Kondensator sperrt Gleichstrom.

**Beispiel.** Eine __Stromquelle__, ein Bauteil, das seinen Strom unabhängig von der Spannung festhält, speist über den Schalter S einen Widerstand und einen ungeladenen Kondensator in Reihe (Abb. [3](#abb-3)). Sie liefert $I=0{,}9$ mA, $R$ und $C$ sind die Werte des RC-Kreises. Mit dem Schließen von S bei $t=0$ springt $u_R$ auf den festen Wert $R\,I=9$ V. Am Kondensator liefert [(3.2)](#gl-3-2) mit $u_C(0)=0$

<span class="anker" id="gl-3-3"></span>
$$u_C(t)=\frac{Q(t)}{C}=\frac{I\,t}{C}=9\,\mathrm{V/s}\cdot t. \tag{3.3}$$

Die Spannung wächst gerade an. Sie startet stetig bei null, obwohl der Strom springt. Eine ideale Stromquelle lädt ohne Ende weiter, bis das Dielektrikum durchschlägt. Bei 1 s sind beide Spannungen gleich.

:::abbildung et1/k3rampe 3
Eine Stromquelle lädt einen Kondensator über $R=10\,\mathrm{k\Omega}$. Mit dem Schließen von S springt $u_R$ auf 9 V und bleibt dort. $u_C$ startet bei null und steigt mit 9 V/s, weil je Sekunde dieselbe Ladung ankommt.
:::

⁠**Grenzfall:** Für $C\to\infty$ wird die Steigung null, die Spannung rührt sich nicht. Ein sehr großer Kondensator hält deshalb eine Spannung fest.

:::frage An einem leeren Kondensator liegt 0 V. Muss der Strom dann nicht null sein?
Das gilt für einen Widerstand. Am Kondensator sagt $u=0$ nichts über $i$, denn $i$ hängt an der Steigung von $u$, nicht am Wert. In Abb. [3](#abb-3) ist bei $t=0$ die Spannung null, der Strom aber 0,9 mA.
:::

:::aufgabe Aufgabe 3 ★★ Vom Strom zur Spannung und zurück
<span class="anker" id="aufg-3"></span>

Ein Kondensator mit 100 µF ist bei $t=0$ leer. Der Strom beträgt $+0{,}5$ mA von 0 bis 2 s, null von 2 s bis 3 s und $-1$ mA von 3 s bis 4 s.

<ol class="al">

<li>

Skizziere $u(t)$ und gib die Werte bei 2 s, 3 s und 4 s an.

</li>

<li>

Welche Ladung trägt er bei 3 s?

</li>

<li>

An einem anderen Kondensator mit 10 µF steigt die Spannung in 5 ms gleichmäßig von 2 V auf 7 V. Welcher Strom fließt?

</li>

<li>

Warum darf $i(t)$ eine senkrechte Kante haben, $u(t)$ aber nicht?

</li>

</ol>

:::loesung
(a) Bei konstantem Strom ist $u$ eine Gerade mit der Steigung $i/C$. Von 0 bis 2 s: $0{,}5\,\mathrm{mA}/100\,\mu\text{F}=5$ V/s, also $u(2\,\mathrm{s})=10$ V. Von 2 s bis 3 s: $i=0$, die Spannung bleibt 10 V. Von 3 s bis 4 s: $-10$ V/s, also $u(4\,\mathrm{s})=0$. Die Kurve ist ein Trapez.

(b) $Q=C\,u=100\,\mu\text{F}\cdot10\,\mathrm{V}=1$ mC. Das ist auch die Fläche unter $i(t)$ bis 3 s: $0{,}5\,\mathrm{mA}\cdot2\,\mathrm{s}$.

(c) $i=C\,\Delta u/\Delta t=10\,\mu\text{F}\cdot5\,\mathrm{V}/5\,\mathrm{ms}=10$ mA.

(d) $u$ folgt aus der Fläche unter $i$. Eine Fläche wächst immer stetig, auch wenn $i$ eine Kante hat. Eine Kante in $u$ verlangte dagegen unbegrenzten Strom.
:::
:::

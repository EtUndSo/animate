---
title: Stufe 3: Strom und Spannung am Kondensator
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Der Kondensator
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator
knoten: Kapitel 3: Der Kondensator
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

Mit Strom- und Spannungszählpfeil in gleicher Richtung ([Kapitel 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)) gilt für zeitabhängige Größen

<span class="anker" id="gl-3-1"></span>
<span class="anker" id="gl-3-2"></span>
$$\begin{aligned} i(t)&=\frac{\mathrm{d} q}{\mathrm{d} t}=C\,\frac{\mathrm{d} u(t)}{\mathrm{d} t},\\ u(t)&=\frac{q(t)}{C}=u(t_0)+\frac1C\int_{t_0}^{t}i(t')\,\mathrm{d} t'. \end{aligned} \tag{3.1|3.2}$$
:::

:::herleitung Strom und Spannung
Strom ist Ladung je Zeit, $i=\mathrm{d} q/\mathrm{d} t$ ([Kapitel 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)). Einsetzen von $q=C\,u$ und Herausziehen der konstanten Zahl $C$ ergibt [(3.1)](#gl-3-1). Umgekehrt ist die Ladung die Fläche unter der Stromkurve, wie der Weg die Fläche unter der Geschwindigkeit ist ([Kapitel 1](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)): $q(t)=q(t_0)+\int_{t_0}^{t}i\,\mathrm{d} t'$. Teilen durch $C$ ergibt [(3.2)](#gl-3-2).
:::

⁠**So liest man das:** Kleinbuchstaben stehen für zeitabhängige Größen, $t'$ ist die Integrationsvariable, $u(t_0)$ die Spannung zur Startzeit. $i$ in A, $C$ in F, $\mathrm{d} u/\mathrm{d} t$ in V/s. 1 mA an 100 µF lässt die Spannung um 10 V/s steigen. **Vorzeichen:** $q$ ist die Ladung der Platte, in die der Strompfeil hineinzeigt. Bei $i>0$ wächst sie und $u$ steigt, bei $i<0$ sinkt $u$. **Gültigkeit:** $C$ muss konstant sein.

**Zwei Folgerungen.** Erstens: **Die Spannung springt nicht.** Ein Sprung um $\Delta U$ in der Zeit $\Delta t$ verlangt $i=C\,\Delta U/\Delta t$. Für $\Delta t\to0$ wüchse der Strom unbegrenzt, denn die Ladung $C\,\Delta U$ müsste in null Zeit ankommen. 9 V in 1 µs an 100 µF verlangen schon 900 A. Der Strom darf dagegen springen, denn er ist nicht an eine gespeicherte Größe gebunden. Zweitens: **Bei konstanter Spannung fließt kein Strom.** Mit $\mathrm{d} u/\mathrm{d} t=0$ ist $i=0$, der Kondensator sperrt Gleichstrom.

::::beispiel
Eine __Stromquelle__, ein Bauteil, das seinen Strom unabhängig von der Spannung festhält, speist über den Schalter S einen Widerstand und einen ungeladenen Kondensator in Reihe (Abb. [3](#abb-3)). Sie liefert $I=0{,}9$ mA, $R$ und $C$ sind die Werte des RC-Kreises. Mit dem Schließen von S bei $t=0$ springt $u_R$ auf den festen Wert $R\,I=9$ V. Am Kondensator liefert [(3.2)](#gl-3-2) mit $u_C(0)=0$

<span class="anker" id="gl-3-3"></span>
$$u_C(t)=\frac{Q(t)}{C}=\frac{I\,t}{C}=9\,\mathrm{V/s}\cdot t. \tag{3.3}$$

Die Spannung wächst gerade an. Sie startet stetig bei null, obwohl der Strom springt. Eine ideale Stromquelle lädt ohne Ende weiter, bis das Dielektrikum durchschlägt. Bei 1 s sind beide Spannungen gleich.

:::abbildung et1/k3rampe 3
Eine Stromquelle lädt einen Kondensator über $R=10\,\mathrm{k\Omega}$. Mit dem Schließen von S springt $u_R$ auf 9 V und bleibt dort. $u_C$ startet bei null und steigt mit 9 V/s, weil je Sekunde dieselbe Ladung ankommt.
:::
::::

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

::::formelsammlung
**Strom am Kondensator**

$$i(t)=\frac{\mathrm{d} q}{\mathrm{d} t}=C\,\frac{\mathrm{d} u(t)}{\mathrm{d} t}$$

Strom- und Spannungszählpfeil gleichsinnig, $C$ konstant; $\mathrm{d} u/\mathrm{d} t$ in V/s. Der Strom folgt aus der Änderung der Spannung, nicht aus ihrem Wert: Bei konstanter Spannung ist $i=0$, der Kondensator sperrt Gleichstrom. Bei $i>0$ wächst die Ladung der Platte, in die der Strompfeil zeigt.

**Spannung aus dem Strom**

$$u(t)=\frac{q(t)}{C}=u(t_0)+\frac1C\int_{t_0}^{t}i(t')\,\mathrm{d} t'$$

$u(t_0)$ Spannung zur Startzeit, $t'$ Integrationsvariable: Die Ladung ist die Fläche unter der Stromkurve.

**Die Spannung springt nicht**

$$i=C\,\Delta U/\Delta t$$

Ein Sprung um $\Delta U$ in der Zeit $\Delta t\to0$ verlangte unbegrenzten Strom, denn die Ladung $C\,\Delta U$ müsste in null Zeit ankommen. Der Strom darf springen, er ist an keine gespeicherte Größe gebunden. Für $C\to\infty$ rührt sich die Spannung nicht.

**Laden mit einer Stromquelle**

$$u_C(t)=\frac{Q(t)}{C}=\frac{I\,t}{C}$$

Eine Stromquelle hält ihren Strom $I$ unabhängig von der Spannung fest. Ab $u_C(0)=0$ steigt die Spannung gerade an, weil je Sekunde dieselbe Ladung ankommt; eine ideale Stromquelle lädt weiter, bis das Dielektrikum durchschlägt.
::::

::::lernkarten
:::karte formel Strom am Kondensator
Wie hängt der Strom $i(t)$ durch einen Kondensator von seiner Spannung $u(t)$ ab, und was setzt die Formel voraus?
---
$i(t)=\frac{\mathrm{d} q}{\mathrm{d} t}=C\,\frac{\mathrm{d} u(t)}{\mathrm{d} t}$: Der Strom folgt aus der Änderung der Spannung, nicht aus ihrem Wert. Strom- und Spannungszählpfeil zeigen in dieselbe Richtung, $C$ ist konstant.
--- falsch
$i(t)=C\,u(t)$: Der Strom ist die Kapazität mal dem Wert der Spannung. Bei hoher Spannung fließt deshalb immer ein großer Strom, auch wenn sie sich gar nicht ändert.
--- falsch
$i(t)=\frac1C\,\frac{\mathrm{d} u(t)}{\mathrm{d} t}$: Der Strom ist die Änderung der Spannung, geteilt durch die Kapazität. Ein großer Kondensator braucht deshalb für dieselbe Änderung wenig Strom.
--- falsch
$i(t)=C\,\frac{\mathrm{d} u(t)}{\mathrm{d} t}$: Der Strom folgt aus der Änderung der Spannung. Das gilt für jede Wahl der Zählpfeile und auch dann, wenn sich $C$ mit der Spannung ändert.
:::
:::karte formel Spannung aus dem Strom
Wie berechnet man die Spannung $u(t)$ eines Kondensators aus dem Strom, der seit der Startzeit $t_0$ geflossen ist?
---
$u(t)=\frac{q(t)}{C}=u(t_0)+\frac1C\int_{t_0}^{t}i(t')\,\mathrm{d} t'$: Startspannung plus die Fläche unter der Stromkurve, geteilt durch $C$; $t'$ ist die Integrationsvariable.
--- falsch
$u(t)=\frac1C\int_{t_0}^{t}i(t')\,\mathrm{d} t'$: die Fläche unter der Stromkurve, geteilt durch $C$. Die Startspannung zählt nicht, weil jeder Kondensator bei null beginnt.
--- falsch
$u(t)=u(t_0)+C\int_{t_0}^{t}i(t')\,\mathrm{d} t'$: Startspannung plus die Fläche unter der Stromkurve, multipliziert mit $C$; $t'$ ist die Integrationsvariable.
--- falsch
$u(t)=u(t_0)+\frac{i(t)}{C}\,(t-t_0)$: Startspannung plus der jetzige Strom mal der vergangenen Zeit, geteilt durch $C$, für jeden beliebigen Stromverlauf.
:::
:::karte herleitung Strom und Spannung
Leite aus $i=\mathrm{d} q/\mathrm{d} t$ und $q=C\,u$ die beiden Beziehungen $i=C\,\mathrm{d} u/\mathrm{d} t$ und $u(t)=u(t_0)+\frac1C\int_{t_0}^{t}i\,\mathrm{d} t'$ her.
---
Strom ist Ladung je Zeit, $i=\mathrm{d} q/\mathrm{d} t$, weil er zählt, wie viel Ladung je Zeit auf die Platte fließt.
---
Einsetzen von $q=C\,u$ und Herausziehen von $C$ ergibt $i=C\,\mathrm{d} u/\mathrm{d} t$, weil $C$ eine konstante Zahl ist.
---
Umgekehrt ist die Ladung die Fläche unter der Stromkurve, $q(t)=q(t_0)+\int_{t_0}^{t}i\,\mathrm{d} t'$, weil sie sich aus allen kleinen Portionen des Stroms aufsummiert, so wie der Weg aus der Geschwindigkeit.
---
Teilen durch $C$ ergibt $u(t)=u(t_0)+\frac1C\int_{t_0}^{t}i\,\mathrm{d} t'$, weil zu jeder Zeit $u=q/C$ gilt.
:::
:::karte zusammenhang Die Spannung springt nicht
Warum kann die Spannung an einem Kondensator nicht springen, der Strom aber schon?
---
Ein Sprung um $\Delta U$ in der Zeit $\Delta t$ verlangt $i=C\,\Delta U/\Delta t$, für $\Delta t\to0$ also unbegrenzten Strom, denn die Ladung $C\,\Delta U$ müsste in null Zeit ankommen. Der Strom ist an keine gespeicherte Größe gebunden.
--- falsch
Weil das Dielektrikum eine schnelle Änderung des Felds zwischen den Platten bremst wie eine Trägheit; der Strom fließt dagegen nur in den Drähten, wo nichts bremst, und kann deshalb springen.
--- falsch
Umgekehrt: Die Spannung kann springen, der Strom nicht. Strom ist bewegte Ladung, und bewegte Ladung kann ihre Geschwindigkeit ohne unbegrenzte Kraft nicht sprunghaft ändern.
--- falsch
Weil reale Batterien ihre Spannung nur langsam aufbauen und den Anstieg begrenzen; an einer idealen Quelle würde auch die Spannung am Kondensator beim Einschalten sofort springen.
:::
:::karte zusammenhang Kondensator bei konstanter Spannung
Was geschieht mit dem Strom durch einen Kondensator, solange seine Spannung konstant bleibt?
---
Er ist null: Mit $\mathrm{d} u/\mathrm{d} t=0$ ist $i=0$, auch wenn die Spannung hoch ist. Der Kondensator sperrt Gleichstrom.
--- falsch
Er ist konstant und proportional zur Spannung wie bei einem Widerstand; eine hohe Spannung treibt einen großen Gleichstrom hindurch.
--- falsch
Er ist nur dann null, wenn die Spannung null ist; bei jeder anderen konstanten Spannung fließt ein kleiner Gleichstrom.
--- falsch
Er wächst langsam an, weil sich bei konstanter Spannung immer weiter Ladung auf den beiden Platten sammelt.
:::
:::karte zusammenhang Strom am leeren Kondensator
Muss der Strom durch einen leeren Kondensator null sein, weil an ihm 0 V liegen?
---
Nein: Der Strom hängt nicht am Wert der Spannung, sondern an ihrer Steigung, $u=0$ sagt nichts über $i$. Eine Stromquelle treibt bei 0 V ihren vollen Strom hinein.
--- falsch
Ja: Ohne Spannung fließt kein Strom, das gilt für jeden Zweipol, auch für den Kondensator. Strom fließt erst, wenn sich auf den Platten eine Spannung gebildet hat.
--- falsch
Nein, aber nur, weil das Dielektrikum bei 0 V noch leitet. Mit der ersten getrennten Ladung wird es zum Isolator, und der Strom endet.
--- falsch
Ja, solange er leer ist: Eine Stromquelle muss ihn erst vorladen, bevor sie Strom hineintreiben kann; danach fließt ihr voller Strom.
:::
:::karte begriff Stromquelle
Was zeichnet eine Stromquelle aus, und wie verläuft die Spannung an einem leeren Kondensator, den sie lädt?
---
Eine Stromquelle hält ihren Strom $I$ unabhängig von der Spannung fest. Am Kondensator steigt die Spannung deshalb gerade an, $u_C(t)=\frac{Q(t)}{C}=\frac{I\,t}{C}$, weil je Sekunde dieselbe Ladung ankommt.
--- falsch
Eine Stromquelle hält ihre Spannung unabhängig vom Strom fest. Am Kondensator steigt deshalb der Strom gerade an, bis der Kondensator voll ist und die Quelle dann von selbst abschaltet.
--- falsch
Eine Stromquelle hält ihren Strom fest, aber nur, bis der Kondensator ihre Spannung erreicht hat; dann endet der Strom, und die Spannung am Kondensator bleibt stehen.
--- falsch
Eine Stromquelle gibt eine feste Ladung ab und hört dann auf. Am Kondensator springt die Spannung deshalb sofort auf ihren Endwert $Q/C$ und bleibt dort stehen.
:::
:::karte zusammenhang Sehr großer Kondensator
Wie verhält sich die Spannung an einem sehr großen Kondensator, wenn ein endlicher Strom fließt?
---
Sie rührt sich kaum: Die Steigung ist $i/C$, für $C\to\infty$ wird sie null. Ein sehr großer Kondensator hält deshalb eine Spannung fest.
--- falsch
Sie folgt dem Strom besonders schnell, weil ein großer Kondensator mehr Ladung auf einmal bewegt und deshalb schneller reagiert.
--- falsch
Sie steigt besonders stark, weil sich auf großen Platten mehr Ladung sammelt und mehr Ladung immer mehr Spannung bedeutet.
--- falsch
Sie schwankt stark, weil ein großer Kondensator jeden kleinen Strom verstärkt und in große Änderungen der Spannung umsetzt.
:::
:::karte zusammenhang Vorzeichen des Stroms
Was bedeutet ein negativer Strom $i<0$ an einem Kondensator, wenn Strom- und Spannungspfeil in dieselbe Richtung zeigen?
---
Die Ladung der Platte, in die der Strompfeil hineinzeigt, sinkt, also sinkt $u$. Bei $i>0$ wächst sie, und $u$ steigt.
--- falsch
Der Kondensator ist verpolt: Seine Spannung ist negativ, solange $i<0$ ist, und wird sofort positiv, wenn der Strom das Vorzeichen wechselt.
--- falsch
Die Ladung der Platte, in die der Strompfeil hineinzeigt, wächst trotzdem, nur langsamer als bei $i>0$; $u$ steigt also weiter an.
--- falsch
Der Strom fließt durch das Dielektrikum zurück; die Ladung auf den Platten bleibt dabei gleich, nur $u$ kehrt ihr Vorzeichen um.
:::
::::

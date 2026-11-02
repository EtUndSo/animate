---
title: Stufe 2: Warum der Widerstand warm wird
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Leistung, Anpassung und Wirkungsgrad
order: 1170300
summary: Im Widerstand verlässt die Energie den Stromkreis.
tags: Nennbelastbarkeit, Hyperbel
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Im Widerstand verlässt die Energie den Stromkreis. Diese Stufe zeigt den Mechanismus und die Grenze, die daraus folgt.
:::

**Die Idee.** Liegt an einem Widerstand eine Spannung, herrscht in ihm ein Feld. Es beschleunigt jedes freie Elektron. Nach der Flugzeit $T$ stößt das Elektron und verliert die gerichtete Geschwindigkeit wieder ([Teil 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)). Dabei geht seine Bewegungsenergie an das Kristallgitter, die Atome schwingen stärker, und diese Schwingung ist Wärme (Abb. [2](#abb-2)). Das Elektron ist nur der Überbringer: Hinter dem Widerstand hat es dieselbe Drift wie davor, denn Strom und Querschnitt sind gleich. Es hat Potenzial verloren, ohne schneller zu werden. Also steckt die ganze Energie im Gitter. Die Drift selbst fällt nicht ins Gewicht: Bei 0,44 µ m/s ([Teil 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)) trägt ein Elektron $8{,}8\cdot10^{-44}$ J, an 9 V gibt es $1{,}44\cdot10^{-18}$ J ab, das $1{,}6\cdot10^{25}$-Fache.

:::abbildung et1/k7stoss 2
Stoßmodell für ein Elektron. Im Flug wächst die Arbeit des Felds (blau) und steckt als Bewegungsenergie im Elektron. Beim Stoß springt die Wärme im Gitter um $W_1$ (rot). Nach jedem Stoß sind beide Kurven gleich hoch: Alles geht ans Gitter.
:::

:::satz Satz 2.1 (Stromwärme und Belastbarkeit)
<span class="anker" id="satz-2-1"></span>

In einem Widerstand wird die gesamte elektrische Leistung zu Wärme:

<span class="anker" id="gl-2-1"></span>
$$P=U\,I=R\,I^2=\frac{U^2}{R}. \tag{2.1}$$

Ein Bauteil verträgt das nur bis zu seiner __Nennbelastbarkeit__ $P_\mathrm{max}$:

<span class="anker" id="gl-2-2"></span>
$$P\le P_\mathrm{max}. \tag{2.2}$$
:::

⁠**So liest man das:** Ein kleiner Schichtwiderstand hat $P_\mathrm{max}=250$ mW, ein Heizlüfter wandelt 2 kW. Quadratisch ist die Formel, weil der Strom zweimal zählt: Doppelter Strom heißt doppelt so viele Coulomb je Sekunde, und wegen $U=R\,I$ gibt jedes doppelt so viel ab. Bei gleichem Strom (Reihe) wächst die Wärme mit $R$, bei gleicher Spannung (parallel) fällt sie mit $R$. **Gültigkeit:** $P=U\,I$ gilt immer, die beiden anderen Formen nur für den ohmschen Widerstand ($R$ unabhängig vom Strom), und $U$ und $I$ müssen zu diesem Widerstand gehören.

:::herleitung Von den Stößen zu $U^2/R$
Im Modell aus [Teil 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html) wird ein Elektron mit $a=e\,E/m_\mathrm e$ beschleunigt und erreicht $v_\mathrm{max}=a\,T$ auf der Strecke $s=\frac12a\,T^2$. Das Feld verrichtet die Arbeit $e\,E\,s=m_\mathrm e\,a\,s=\frac12m_\mathrm e(a\,T)^2=W_1$, genau die Bewegungsenergie beim Stoß. Im Volumen $A\,L$ sitzen $n\,A\,L$ freie Elektronen, jedes stößt $1/T$-mal je Sekunde:

$$P=n\,A\,L\,\frac{W_1}{T}=n\,A\,L\,\frac{e^2E^2\,T}{2\,m_\mathrm e}=\sigma\,E^2\,A\,L.$$

Dabei ist $\sigma=n\,e\,\mu$ und $\mu=e\,T/(2\,m_\mathrm e)$ ([Teil 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)). Mit $U=E\,L$ und $R=L/(\sigma A)$ wird daraus $P=U^2/R$.
:::

**Belastbarkeit.** Die Temperatur steigt, bis das Bauteil je Sekunde so viel Wärme an die Umgebung abgibt, wie im Inneren entsteht. Mehr Leistung heißt also höhere Temperatur, und zu hohe Temperatur zerstört es. Im Diagramm aus Abb. [3](#abb-3) ist die Grenze die __Hyperbel__ $I=P_\mathrm{max}/U$, jeder Widerstand eine Gerade durch den Ursprung. Ihr Schnittpunkt liegt bei $U_\mathrm{max}=\sqrt{P_\mathrm{max}\,R}$ und $I_\mathrm{max}=\sqrt{P_\mathrm{max}/R}$.

:::abbildung et1/k7grenze 3
Grenze eines Widerstands mit 250 mW. Jeder Widerstandswert darf nur bis zur Hyperbel betrieben werden: 25 $\Omega$ bis 100 mA, 100 $\Omega$ bis 50 mA, 400 $\Omega$ bis 25 mA.
:::

**Beispiel.** Mit 100 $\Omega$ und 250 mW sind $U_\mathrm{max}=5$ V und $I_\mathrm{max}=50$ mA zulässig. An idealen 9 V entstünden 810 mW, das 3,24-Fache. Nötig wäre $R\ge(9\,\mathrm{V})^2/250\,\mathrm{mW}=324\,\Omega$. **Grenzfälle:** $R\to\infty$ ergibt $P\to0$. $R\to0$ ergibt an fester Spannung $P\to\infty$. Das verhindert nur der Innenwiderstand der Quelle (Stufe [5](wohin-die-leistung-einer-quelle-geht.html#stufe-5)).

:::frage Heizdraht und Zuleitung führen denselben Strom. Warum glüht nur der Heizdraht?
Bei gleichem Strom ist die Wärme proportional zu $R$. Eine Zuleitung mit 10 m$\Omega$ setzt bei 0,5 A nur 2,5 mW um, die Last mit 16 $\Omega$ dagegen 4 W, das 1600-Fache. In Haartrockner und Lötkolben ist die Wärme der Zweck, in der Leitung ist sie Verlust (Stufe [4](leitungsverluste.html#stufe-4)).
:::

:::aufgabe Aufgabe 2 ★★ Welcher wird heißer?
<span class="anker" id="aufg-2"></span>

Zwei Widerstände mit 100 $\Omega$ und 300 $\Omega$, beide für 250 mW ausgelegt, liegen an 12 V. Sage zuerst voraus, welcher jeweils heißer wird. (a) Sie liegen in Reihe. (b) Sie liegen parallel. Berechne alle Leistungen. (c) Wo wird die Nennbelastbarkeit überschritten?

:::loesung
(a) Reihe: $I=12\,\mathrm{V}/400\,\Omega=30$ mA, $P=R\,I^2$ ergibt 90 mW und 270 mW. Der größere Widerstand wird heißer: gleich viele Coulomb, jedes gibt dort dreimal so viel ab. (b) Parallel: $P=U^2/R$ ergibt 1,44 W und 0,48 W. Der kleinere wird heißer: gleiche Energie je Coulomb, aber dreimal so viele Coulomb. (c) In Reihe ist der 300-$\Omega$-Widerstand mit 270 mW überlastet, parallel sind es beide.
:::
:::

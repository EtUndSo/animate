---
title: Stufe 2: Kreisring und Kugelschale
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Zustandsdichte und Fermi-Verteilung
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/zustandsdichte-und-fermi-verteilung
knoten: Kapitel 10: Zustandsdichte und Fermi-Verteilung
order: 4200400
summary: In der Kette gibt es zu jeder Energie nur zwei Wellenvektoren.
tags: 
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
In der Kette gibt es zu jeder Energie nur zwei Wellenvektoren. In der Ebene und im Raum sind es viele. Diese Stufe zählt sie.
:::

**Die Idee.** Die erlaubten $\boldsymbol k$ bilden im $k$-Raum ein Raster. Jeder Punkt beansprucht eine Zelle mit der Kante $2\pi/L$, also die Fläche $(2\pi/L)^2$ oder das Volumen $(2\pi/L)^3$. Bei der Parabel hängt $E$ nur vom Betrag $k$ ab. Alle Zustände einer Energie liegen deshalb auf einem Kreis oder einer Kugel, und das Fenster von $E$ bis $E+\mathrm{d} E$ ist ein Kreisring oder eine Kugelschale (Abb. [2](#abb-2)). Zählen heißt: Größe der Schale durch Größe einer Zelle. Mit steigender Energie wird die Schale größer und zugleich dünner, weil die Parabel steiler wird. In der Ebene heben sich beide Einflüsse genau auf, im Raum gewinnt die Größe.

:::abbildung gemb1/k10kugel 2
Oben die Zustände einer Energie im $k$-Raum: zwei Punkte, ein Kreis, eine Kugel, rot das Fenster $\mathrm{d} k$. Unten die Folge für $D(E)$. Die Zahl der Plätze wächst mit der Größe des Rings, die Umrechnung von $\mathrm{d} k$ auf $\mathrm{d} E$ ist in allen drei Fällen dieselbe.
:::

:::satz Satz 2.1 (Zustandsdichten ohne äußeres Potential)
<span class="anker" id="satz-2-1"></span>

Mit $E=\hbar^2k^2/(2m^*)$ und $D(E)=(2/L^d)\,\mathrm{d} Z/\mathrm{d} E$ gilt:

| $d$ | $D(E)$ | Verlauf |
|---|---|---|
| 1 | $\dfrac2h\sqrt{\dfrac{2m^*}{E}}=\dfrac1{\pi\hbar}\sqrt{\dfrac{2m^*}{E}}$ | $\propto E^{-1/2}$ |
| [2.2ex] 2 | $\dfrac{4\pi m^*}{h^2}=\dfrac{m^*}{\pi\hbar^2}$ | $\propto E^0$ |
| [2.2ex] 3 | $\dfrac{2\sqrt2\cdot4\pi}{h^3}\,m^{*3/2}\sqrt E=\dfrac{m^*}{\pi^2\hbar^3}\sqrt{2m^*E}=\dfrac{4\pi(2m^*)^{3/2}}{h^3}\sqrt E$ | $\propto E^{1/2}$ |

Die Einheiten sind $1/(\mathrm{eV\,cm})$, $1/(\mathrm{eV\,cm^2})$ und $1/(\mathrm{eV\,cm^3})$.
:::

:::herleitung Ring und Schale
⁠**Ebene.** Ring: $\pi(k+\mathrm{d} k)^2-\pi k^2\approx2\pi k\,\mathrm{d} k$, der Term $(\mathrm{d} k)^2$ entfällt. Also $\mathrm{d} Z=2\pi k\,\mathrm{d} k/(2\pi/L)^2=L^2k\,\mathrm{d} k/(2\pi)$. Aus $E=\hbar^2k^2/(2m^*)$ folgt $\mathrm{d} E=\hbar^2k\,\mathrm{d} k/m^*$, das heißt $k\,\mathrm{d} k=m^*\mathrm{d} E/\hbar^2$. Das ergibt $D=(2/L^2)\,\mathrm{d} Z/\mathrm{d} E=m^*/(\pi\hbar^2)$. Das $k$ kürzt sich: Darum ist $D$ konstant.

⁠**Raum.** Schale: $\frac43\pi(k+\mathrm{d} k)^3-\frac43\pi k^3=\frac43\pi\bigl(3k^2\mathrm{d} k+3k(\mathrm{d} k)^2+(\mathrm{d} k)^3\bigr)\approx4\pi k^2\mathrm{d} k$. Also $\mathrm{d} Z=4\pi k^2\mathrm{d} k/(2\pi/L)^3=L^3k^2\mathrm{d} k/(2\pi^2)$, je Volumen mit Spin $D(k)\,\mathrm{d} k=(k^2/\pi^2)\,\mathrm{d} k$. Mit $k\,\mathrm{d} k=m^*\mathrm{d} E/\hbar^2$ und $k=\sqrt{2m^*E}/\hbar$ folgt $D(E)=m^*\sqrt{2m^*E}/(\pi^2\hbar^3)$.
:::

⁠**Warum die Exponenten?** Stets ist $D\propto k^{d-1}\,\mathrm{d} k/\mathrm{d} E$. Der Faktor $k^{d-1}$ ist die Größe der Fläche gleicher Energie: zwei Punkte, Kreisumfang, Kugeloberfläche. Der Faktor $\mathrm{d} k/\mathrm{d} E\propto E^{-1/2}$ kommt von der Parabel und hängt nicht von $d$ ab. Mit $k\propto E^{1/2}$ bleibt $D\propto E^{(d-2)/2}$. Die Summe [(1.1)](warum-man-zustande-zahlt.html#gl-1-1) wird in drei Dimensionen entsprechend zu

<span class="anker" id="gl-2-1"></span>
$$n=\frac2{L^3}\sum_{k_x,k_y,k_z}f\bigl(E(\boldsymbol k)\bigr)=\frac2{(2\pi)^3}\int\mathrm{d} k_x\,\mathrm{d} k_y\,\mathrm{d} k_z\,f\bigl(E(\boldsymbol k)\bigr)=\int\mathrm{d} E\,D(E)\,f(E), \tag{2.1}$$

denn jeder Rasterpunkt steht für $\Delta k_x\,\Delta k_y\,\Delta k_z/(2\pi/L)^3=1$, und aus jedem $\Delta k_i$ wird für $L\to\infty$ ein $\mathrm{d} k_i$. Das $L^3$ kürzt sich.

::::beispiel
Ein Film mit $L=200$ nm und $m^*=m_0$, Fenster 50 bis 55 meV: Die Formel gibt $\mathrm{d} Z=417{,}7$, das Auszählen des Rasters 408, also 2 % weniger. Ein Würfel mit $L=100$ nm enthält unter 0,1 eV nach der Kugel 71 807 Zustände, gezählt sind es 71 711. Der Fehler sitzt am Rand und verliert mit wachsender Größe an Gewicht. Bei $m^*=m_0$ ist in 2D $D=4{,}18\cdot10^{14}\,\mathrm{eV^{-1}\,cm^{-2}}$ und in 3D $D(1\,\mathrm{eV})=6{,}81\cdot10^{21}\,\mathrm{eV^{-1}\,cm^{-3}}$.
::::

⁠**Grenzfall:** Für $E\to0$ schrumpft die Kugel auf einen Punkt, also $D\to0$. Der Kreis schrumpft auch, aber im selben Maß wird der Ring dicker, und $D$ bleibt.

**Mehrere Bänder.** Jedes Band zählt für sich, die Zustandsdichten addieren sich. Ein zweites Band setzt ab seiner Unterkante einen eigenen Beitrag auf den ersten: in 2D eine Stufe der Höhe $m^*/(\pi\hbar^2)$, in 1D eine neue Spitze. Ein Band mit größerer Masse ist flacher und liefert mehr Plätze, die Stufe ist dort höher.

:::frage In Teil 2 war es ein Viertelkreis, hier ist es ein ganzer Kreis. Was stimmt?
Beides. In der Box zählen nur positive Quantenzahlen, das Raster ist aber mit $\pi/L$ doppelt so fein: $\frac14\pi k^2/(\pi/L)^2=k^2L^2/(4\pi)$. Mit periodischen Rändern zählen beide Vorzeichen bei einem Raster von $2\pi/L$: $\pi k^2/(2\pi/L)^2=k^2L^2/(4\pi)$. Die Zustandsdichte hängt nicht von der Art des Rands ab, solange der Kristall groß ist.
:::

:::aufgabe Aufgabe 2 ★★ Film, Würfel und zweites Band
<span class="anker" id="aufg-2"></span>

Es gelte $m^*=0{,}2\,m_0$.

<ol class="al">

<li>

Berechne $D$ in einem Film. Wie viele Plätze liegen in einem Quadrat mit $L=150$ nm im Fenster 2 meV?

</li>

<li>

Berechne $D(0{,}1\,\mathrm{eV})$ für ein dreidimensionales Stück.

</li>

<li>

Vorhersage: Ab $E_2$ kommt im Film ein Band mit $0{,}4\,m_0$ hinzu. Skizziere $D(E)$. Um welchen Faktor springt $D$ bei $E_2$?

</li>

</ol>

:::loesung
(a) $D=m^*/(\pi\hbar^2)=8{,}36\cdot10^{13}\,\mathrm{eV^{-1}\,cm^{-2}}=0{,}836\,\mathrm{eV^{-1}\,nm^{-2}}$. Plätze: $D\,L^2\,\Delta E=37{,}6$. (b) $D(0{,}1\,\mathrm{eV})=1{,}93\cdot10^{20}\,\mathrm{eV^{-1}\,cm^{-3}}$. (c) Eine Treppe. Bei $E_2$ springt $D$ von $0{,}2$ auf $0{,}6$ in Einheiten von $m_0/(\pi\hbar^2)$, also um den Faktor 3.
:::
:::

:::aufgabe Aufgabe 3 ★★★ Keine Parabel
<span class="anker" id="aufg-3"></span>

In einer Ebene gelte $E=\hbar v_\mathrm{Dirac}|\boldsymbol k|$ mit $v_\mathrm{Dirac}=10^6$ m/s, wie an den Dirac-Punkten von Graphen ([Teil 9](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/bandstrukturen-lesen/bandstrukturen-lesen.html)).

<ol class="al">

<li>

Leite $D(E)$ her. Zähle nur einen solchen Punkt.

</li>

<li>

Berechne $D(0{,}1\,\mathrm{eV})$.

</li>

<li>

Welche Potenz von $E$ ergäbe dieselbe Beziehung in einer und in drei Dimensionen?

</li>

</ol>

:::loesung
(a) Ring wie in Stufe [2](#stufe-2): $\mathrm{d} Z=L^2k\,\mathrm{d} k/(2\pi)$. Mit $v=v_\mathrm{Dirac}$, $k=E/(\hbar v)$ und $\mathrm{d} k=\mathrm{d} E/(\hbar v)$ folgt $\mathrm{d} Z=L^2E\,\mathrm{d} E/(2\pi\hbar^2v^2)$ und $D=(2/L^2)\,\mathrm{d} Z/\mathrm{d} E=E/(\pi\hbar^2v^2)$. (b) $\hbar v=0{,}658$ eV nm, $D=7{,}35\cdot10^{12}\,\mathrm{eV^{-1}\,cm^{-2}}$. (c) $\mathrm{d} k/\mathrm{d} E$ ist konstant, also $D\propto k^{d-1}\propto E^{d-1}$: in 1D $E^0$, in 3D $E^2$.
:::
:::

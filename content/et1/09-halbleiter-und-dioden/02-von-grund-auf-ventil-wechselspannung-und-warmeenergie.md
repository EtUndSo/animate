---
title: Von Grund auf: Ventil, Wechselspannung und Wärmeenergie
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Halbleiter und Dioden
order: 1190200
summary: Wie aus Silizium ein Ventil für Strom wird und wie man mit ihm rechnet
tags: Wechselspannung, Scheitelwert, Frequenz, Einweggleichrichter, Elektronenvolt, Wärmeenergie, Boltzmann-Konstanten, Boltzmann-Verteilung
lang: de
---

Eine __Wechselspannung__ wechselt periodisch ihr Vorzeichen. Hier ist sie sinusförmig, $u_\mathrm e(t)=\hat u\sin(2\pi ft)$, mit dem __Scheitelwert__ $\hat u$ (größter Betrag) und der __Frequenz__ $f$ (Schwingungen je Sekunde, Einheit Hz). Eine Schwingung dauert $T=1/f$, bei 50 Hz also 20 ms. Kleine Buchstaben stehen für zeitabhängige Größen.

:::abbildung et1/k9einweg 1
Links: Diode mit den Anschlüssen Anode (A) und Kathode (K) in Reihe mit einem Widerstand an einer Wechselspannung. Rechts oben: Am Widerstand erscheint nur die positive Halbwelle, um 0,7 V verkleinert. Rechts unten: Die Diode hält im Leiten 0,7 V und übernimmt im Sperren die ganze negative Spannung. $\hat u=12$ V, 50 Hz.
:::

Abb. [1](#abb-1) zeigt die Wirkung einer Diode. Die Masche ergibt $u_\mathrm e=u_\mathrm D+u_\mathrm a$. Ist $u_\mathrm e$ positiv, leitet die Diode, an ihr bleiben rund 0,7 V, der Rest liegt am Widerstand. Ist $u_\mathrm e$ negativ, fließt kein Strom. Dann ist $u_\mathrm a=0$, und die Diode trägt die ganze Spannung. Aus der Wechselspannung wird eine Spannung mit nur einem Vorzeichen. Diese Schaltung heißt __Einweggleichrichter__. Ihr Scheitel ist $12\,\mathrm{V}-0{,}7\,\mathrm{V}=11{,}3$ V.

Für das Warum braucht das Kapitel zwei Energiegrößen. Das __Elektronenvolt__ (eV) ist die Energie, die ein Elektron beim Durchlaufen von 1 V gewinnt ([Teil 1](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)): $1\,\mathrm{eV}=e\cdot1\,\mathrm{V}=1{,}602\cdot10^{-19}$ J. Die __Wärmeenergie__ entsteht, weil Atome und Elektronen sich bei jeder Temperatur ungeordnet bewegen. Ihr Maß ist $k_\mathrm BT$ mit der absoluten Temperatur $T$ in K und der __Boltzmann-Konstanten__ $k_\mathrm B$. Bei 300 K ist $k_\mathrm BT=4{,}14\cdot10^{-21}\,\mathrm{J}=25{,}85$ meV. Die Stöße verteilen diese Energie ungleich: Wenige Teilchen haben viel, viele wenig. Im Gleichgewicht gilt die __Boltzmann-Verteilung__:

<span class="anker" id="gl-0-1"></span>
$$\text{Anteil der Teilchen mit mindestens der Energie }W=\mathrm{e}^{-W/(k_\mathrm BT)}. \tag{0.1}$$

Je $k_\mathrm BT$ mehr Energie sinkt der Anteil um den Faktor 2,718, bei $10\,k_\mathrm BT$ ist er $4{,}5\cdot10^{-5}$. Dasselbe Gesetz beschreibt, wie die Luft mit der Höhe dünner wird.

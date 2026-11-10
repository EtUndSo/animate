---
title: Stufe 1: Strom ist bewegte Ladung
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Strom, Widerstand und Kirchhoff
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff
knoten: Kapitel 2: Strom, Widerstand und Kirchhoff
order: 1120200
summary: Kapitel 1 hat Ladungen betrachtet, die ruhen oder einzeln fliegen.
tags: Ladungsdichte, Stromstärke, Stromkreis, stationär
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
[Kapitel 1](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html) hat Ladungen betrachtet, die ruhen oder einzeln fliegen. In einem Draht bewegen sich unzählige Ladungen gemeinsam. Diese Stufe gibt dieser Bewegung zwei Maße.
:::

**Die Idee.** Man stellt sich an eine Stelle des Leiters und misst, wie viel Ladung je Sekunde vorbeikommt. Das hängt von drei Dingen ab: wie dicht die Ladung sitzt, wie schnell sie läuft und wie groß der Querschnitt ist. In der Zeit $\Delta t$ kommt genau die Ladung durch die Fläche, die vorher höchstens den Weg $v\,\Delta t$ entfernt war (Abb. [1](#abb-1)).

:::abbildung et1/k2strom 1
Ladungsträger mit der Geschwindigkeit $v$ in einem Leiter. Alle Ladung im getönten Stück läuft in der Zeit $\Delta t$ durch die Fläche $A$. Das Stück hat das Volumen $A\,v\,\Delta t$.
:::

:::definition Definition 1.1 (Strom und Stromdichte)
<span class="anker" id="satz-1-1"></span>

Die __Ladungsdichte__ $q=\Delta Q/\Delta V$ ist die Ladung je Volumen. Die __Stromstärke__ (kurz Strom) ist die Ladung, die je Zeit durch eine Fläche läuft. Die Stromdichte ist der Strom je Fläche:

<span class="anker" id="gl-1-1"></span>
<span class="anker" id="gl-1-2"></span>
$$\begin{aligned} i&=\lim_{\Delta t\to0}\frac{\Delta Q}{\Delta t}=\frac{\mathrm{d} Q}{\mathrm{d} t},\qquad I=q\,v\,A,\qquad [I]=\mathrm{C/s}=\mathrm A,\\ j&=\frac IA=q\,v,\qquad\vec j=q\,\vec v. \end{aligned} \tag{1.1|1.2}$$
:::

⁠**So liest man das:** $i$ ist der zeitabhängige Strom, $I$ der zeitlich konstante, in Ampere: 3 mA im Rechenmodell, 20 mA in einer Leuchtdiode, 16 A in einer Hausleitung. $q$ hat die Einheit $\mathrm{C/m^3}$. Für die freien Elektronen im Kupfer ist $q=-n\,e=-1{,}36\cdot10^{10}\,\mathrm{C/m^3}$. $j$ hat die Einheit $\mathrm{A/m^2}$, Hausleitungen führen rund $10\,\mathrm{A/mm^2}$. Der Vektor $\vec j$ zeigt für $q>0$ in Richtung von $\vec v$, für $q<0$ entgegengesetzt. **Gültigkeit:** $I=q\,v\,A$ setzt voraus, dass $q$ und $v$ über $A$ gleich sind und $v$ senkrecht auf $A$ steht.

:::herleitung Strom aus Dichte und Geschwindigkeit
Die Fläche sei $A=\Delta x\,\Delta y$. Das getönte Stück hat das Volumen $\Delta V=\Delta x\,\Delta y\,\Delta z$ mit $\Delta z=v\,\Delta t$. Es enthält die Ladung $\Delta Q=q\,\Delta V=q\,A\,v\,\Delta t$, die in der Zeit $\Delta t$ durch $A$ läuft. Also ist $\Delta Q/\Delta t=q\,v\,A$.
:::

**Wann fließt dauerhaft Strom?** Zwei Bedingungen müssen erfüllt sein. Erstens braucht der Kreis eine Quelle, etwa eine Batterie oder ein Netzteil. Sie liefert Energie, keine Ladung: Die Ladungsträger sitzen schon im Leiter, die Quelle treibt sie nur im Kreis herum. Zweitens muss der __Stromkreis__ geschlossen sein, also ein Weg, der in sich zurückläuft. An einer Unterbrechung staut sich sonst Ladung, ihr Feld hebt das antreibende Feld auf, und der Strom endet. Ein zeitlich konstanter Strom im geschlossenen Kreis heißt __stationär__.

::::beispiel
Im Rechenmodell laufen 3 mC je Sekunde durch den Draht, das sind $3\,\mathrm{mC}/e=1{,}87\cdot10^{16}$ Elektronen. Die Stromdichte ist $j=3\,\mathrm{mA}/0{,}5\,\mathrm{mm^2}=6\,\mathrm{mA/mm^2}$. Ein Meter Draht enthält die freie Ladung $n\,e\,A=6800$ C. Die gesamte Ladung, die eine Blockbatterie in ihrem Leben umsetzt (rund 1800 C), steckt also schon in 26 cm dieses Drahts. **Kontrolle:** Für $v=0$ ist $I=0$, gleichgültig wie viel Ladung im Draht sitzt. Doppelte Fläche bei gleichem $v$ ergibt doppelten Strom, denn es sind zwei Drähte nebeneinander.
::::

:::frage Werden die Elektronen im Verbraucher verbraucht?
Nein. Ladung bleibt erhalten, aus einem Bauteil kommen je Sekunde so viele Elektronen heraus, wie hineinlaufen. Verbraucht wird Energie: Jedes Coulomb gibt seine Energie je Ladung, die Spannung, an das Bauteil ab und läuft auf niedrigerem Potenzial weiter.
:::

:::aufgabe Aufgabe 1 ★ Strom, Ladung, Stromdichte
<span class="anker" id="aufg-1"></span>

<ol class="al">

<li>

Eine Leuchtdiode führt 5 min lang 20 mA. Wie viel Ladung läuft durch sie, wie viele Elektronen sind das?

</li>

<li>

Ein Kabel mit $1{,}5\,\mathrm{mm^2}$ Querschnitt führt 16 A. Wie groß ist $j$ in $\mathrm{A/mm^2}$?

</li>

<li>

In welche Richtung zeigt $\vec j$ in einem Draht, in dem Elektronen nach rechts laufen?

</li>

</ol>

:::loesung
(a) $Q=I\,t=20\,\mathrm{mA}\cdot300\,\mathrm{s}=6$ C, das sind $6\,\mathrm{C}/e=3{,}7\cdot10^{19}$ Elektronen. (b) $j=16\,\mathrm{A}/1{,}5\,\mathrm{mm^2}=10{,}7\,\mathrm{A/mm^2}$. (c) Nach links: Für Elektronen ist $q<0$, also zeigt $\vec j=q\,\vec v$ gegen $\vec v$.
:::
:::

---
title: Stufe 1: Energie je Ladung mal Ladung je Zeit
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Leistung, Anpassung und Wirkungsgrad
order: 1170200
summary: Spannung sagt, wie viel Energie eine Ladung abgibt, Strom, wie viel Ladung vorbeikommt.
tags: 
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Spannung sagt, wie viel Energie eine Ladung abgibt, Strom, wie viel Ladung vorbeikommt. Diese Stufe verbindet beides zur Energie je Zeit.
:::

**Die Idee.** Zwischen den Anschlüssen eines Bauteils liegt die Spannung $U$. Nach [Teil 1](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html) gibt jedes Coulomb, das vom höheren zum niedrigeren Potenzial gelangt, die Energie $U$ in Joule ab. Der Strom $I$ zählt, wie viele Coulomb je Sekunde durchlaufen. Je Sekunde werden also $U\cdot I$ Joule umgesetzt (Abb. [1](#abb-1)). Beide Faktoren sind nötig: Spannung ohne Strom setzt nichts um, weil keine Ladung läuft. Strom ohne Spannung setzt nichts um, weil keine Ladung etwas abgibt.

:::abbildung et1/k7ladung 1
Last mit 8 V und 0,5 A. Unten der Potenzialverlauf: Jedes Coulomb verliert 8 J. Gezeichnet sind positive Ladungen in Stromrichtung. Elektronen laufen umgekehrt, das Ergebnis ist dasselbe.
:::

:::definition Definition 1.1 (Energie und Leistung)
<span class="anker" id="satz-1-1"></span>

Läuft die Ladung $\mathrm{d} Q$ durch die Spannung $u$, gibt sie die Energie $\mathrm{d} W=u\,\mathrm{d} Q$ ab. Mit dem Strom $i=\mathrm{d} Q/\mathrm{d} t$ folgen

<span class="anker" id="gl-1-1"></span>
$$p(t)=\frac{\mathrm{d} W}{\mathrm{d} t}=u(t)\,i(t),\qquad W=\int u\,\mathrm{d} Q=\int_{t_1}^{t_2}u(t)\,i(t)\,\mathrm{d} t. \tag{1.1}$$

Für Gleichgrößen, also wenn $U$ und $I$ nicht von der Zeit abhängen, ist

<span class="anker" id="gl-1-2"></span>
$$W=U\,I\,\Delta t,\qquad P=\frac{W}{\Delta t}=U\,I. \tag{1.2}$$
:::

⁠**So liest man das:** $u$ in V, $i$ in A, $p$ in Watt: $[P]=\mathrm{V\,A}=\mathrm{J/s}=\mathrm W$. Eine Anzeige-LED setzt 20 mW um, ein Wasserkocher 2 kW, ein Kraftwerksblock 1 GW. Der Ausdruck $W/\Delta t$ ist allgemein der Mittelwert der Leistung über die Zeit $\Delta t$, $p(t)$ ihr Momentanwert. Geräte laufen oft dauerhaft, deshalb kennzeichnet man sie durch die Leistung und nicht durch die Energie. Für die Energie gilt $1\,\mathrm{W\,s}=1\,\mathrm{V\,A\,s}=1\,\mathrm{J}=1\,\mathrm{N\,m}$. Die Elektrotechnik rechnet meist in Wattsekunden oder Kilowattstunden, $1\,\mathrm{kWh}=3{,}6\,\mathrm{MJ}$. Joule ist bei Verbrennungsvorgängen üblich, Newtonmeter für mechanische Arbeit.

⁠**Vorzeichen:** Mit Verbraucher-Zählpfeilen ([Teil 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)) heißt $p>0$: Das Bauteil nimmt Energie auf, $p<0$: Es gibt Energie ab. Mit Erzeuger-Zählpfeilen ist es umgekehrt. **Gültigkeit:** $p=u\,i$ gilt für jedes Eintor, wenn $u$ und $i$ am selben Anschlusspaar gezählt werden. Über das Innere des Bauteils wird nichts vorausgesetzt.

:::herleitung Warum nur Spannung und Strom zählen
In der Zeit $\mathrm{d} t$ tritt am Anschluss 1 die Ladung $\mathrm{d} Q=i\,\mathrm{d} t$ ein und am Anschluss 2 dieselbe Ladung aus (Knotenregel, [Teil 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)). Das Innere bleibt unverändert. Für die Bilanz ist es so, als wäre $\mathrm{d} Q$ unmittelbar von $\varphi_1$ nach $\varphi_2$ gelangt. Nach [Teil 1](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html) ist die abgegebene Energie $\mathrm{d} W=(\varphi_1-\varphi_2)\,\mathrm{d} Q=u\,i\,\mathrm{d} t$. Division durch $\mathrm{d} t$ ergibt [(1.1)](#gl-1-1). Elektronen laufen umgekehrt und tragen negative Ladung. Beide Vorzeichen zusammen ergeben dasselbe Produkt.
:::

::::beispiel
An $R_\mathrm{L}=16\,\Omega$ liegen 8 V, es fließen 0,5 A ([Teil 5](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)). Jedes Coulomb gibt 8 J ab, je Sekunde kommen 0,5 C: $P=4$ W. In einer Stunde sind das $W=4\,\mathrm{W}\cdot3600\,\mathrm{s}=14{,}4\,\mathrm{kJ}=4\,\mathrm{Wh}$. Einzeln gezählt laufen je Sekunde $I/e=3{,}12\cdot10^{18}$ Elektronen durch, jedes gibt $e\cdot8\,\mathrm{V}=1{,}28\cdot10^{-18}$ J ab. Das Produkt sind wieder 4 W.
::::

⁠**Grenzfälle:** An offenen Klemmen sind es 9 V und 0 A, also $P=0$. Ein idealer Draht hat $U=0$, also $P=0$ bei jedem Strom.

:::frage Wird im Bauteil Strom verbraucht?
Nein. Vor und hinter dem Bauteil fließt derselbe Strom, die Ladung kommt vollständig wieder heraus. Verbraucht wird Energie: Die Ladung läuft auf niedrigerem Potenzial weiter. Auf der Rechnung für den „Stromverbrauch“ stehen deshalb Kilowattstunden.
:::

:::aufgabe Aufgabe 1 ★ Energie und Vorzeichen
<span class="anker" id="aufg-1"></span>

(a) Ein Akku mit 3,7 V speichert die Ladung 2 Ah (2 A eine Stunde lang). Wie viel Energie ist das in Wh und in kJ? Wie lange versorgt er ein Gerät mit 0,74 W? (b) Ein Wasserkocher mit 2 kW läuft 3 Minuten. Wie viele kWh sind das, und was kosten sie bei 30 ct/kWh? (c) An einem Eintor misst man mit Verbraucher-Zählpfeilen $U=12$ V und $I=-3$ A. Nimmt es Leistung auf, oder gibt es welche ab?

:::loesung
(a) $Q=2\,\mathrm{A}\cdot3600\,\mathrm{s}=7200$ C, also $W=3{,}7\,\mathrm{V}\cdot7200\,\mathrm{C}=26{,}64$ kJ $=7{,}4$ Wh. Bei 0,74 W reicht das 10 h. (b) $W=2\,\mathrm{kW}\cdot0{,}05\,\mathrm{h}=0{,}1$ kWh, das kostet 3 ct. (c) $P=12\,\mathrm{V}\cdot(-3\,\mathrm{A})=-36$ W. Das Eintor gibt 36 W ab.
:::
:::

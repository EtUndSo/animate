---
title: Stufe 1: Drei Schichten, zwei Spannungen
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Der Bipolartransistor
order: 1200300
summary: Eine Diode hat zwei Anschlüsse und eine Kennlinie.
tags: npn-Transistor, BE-Diode, CB-Diode, pnp-Transistor, Schaltzeichen, Kollektorstrom, Basisstrom, Emitterstrom
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Eine Diode hat zwei Anschlüsse und eine Kennlinie. Der Transistor hat drei Anschlüsse. Diese Stufe klärt seinen Aufbau und zählt, wie viele Größen frei sind.
:::

**Die Idee.** Ein __npn-Transistor__ besteht aus drei Gebieten desselben Halbleiters: n-dotierter Emitter, p-dotierte Basis, n-dotierter Kollektor (Abb. [1](#abb-1)). Der Emitter ist am stärksten dotiert, damit er viele Elektronen abgeben kann. Der Kollektor ist am schwächsten dotiert, damit seine Raumladungszone breit wird und hohe Spannungen aushält. Die Basis liegt dazwischen und ist sehr schmal, rund 1 µ m. So entstehen zwei pn-Übergänge, die sich die Basis teilen: die __BE-Diode__ und die __CB-Diode__. Im Normalbetrieb leitet die BE-Diode, die CB-Diode sperrt. Vertauscht man n und p, entsteht der __pnp-Transistor__ (Stufe [4](drei-bereiche-drei-ersatzschaltbilder.html#stufe-4)). Im __Schaltzeichen__, dem Symbol im Schaltplan, ist der Emitter der Anschluss mit dem Pfeil. Er zeigt die Richtung des technischen Stroms.

:::abbildung et1/k10aufbau 1
Links: npn-Transistor als Schichtfolge und als Schaltzeichen mit allen Zählpfeilen. Rechts: pnp-Transistor mit umgekehrter Schichtfolge. Der Emitterpfeil zeigt dort in das Bauteil hinein, alle Ströme und Spannungen kehren sich um.
:::

:::definition Definition 1.1 (Ströme und Spannungen am npn-Transistor)
<span class="anker" id="satz-1-1"></span>

$I_\mathrm{B}$ und $I_\mathrm{C}$ zählen in das Bauteil hinein, $I_\mathrm{E}$ heraus. Spannungen sind Potenzialdifferenzen, der erste Index ist der Pluspol: $U_\mathrm{BE}=\varphi_\mathrm{B}-\varphi_\mathrm{E}$, $U_\mathrm{CE}=\varphi_\mathrm{C}-\varphi_\mathrm{E}$, $U_\mathrm{CB}=\varphi_\mathrm{C}-\varphi_\mathrm{B}$. Immer gilt

<span class="anker" id="gl-1-1"></span>
$$I_\mathrm{E}=I_\mathrm{B}+I_\mathrm{C},\qquad U_\mathrm{CE}=U_\mathrm{CB}+U_\mathrm{BE}. \tag{1.1}$$
:::

⁠**So liest man das:** $I_\mathrm{C}$ ist der __Kollektorstrom__, je nach Typ von Mikroampere bis Ampere. $I_\mathrm{B}$ ist der viel kleinere __Basisstrom__, $I_\mathrm{E}$ der __Emitterstrom__. $U_\mathrm{BE}$ liegt an der BE-Diode, um 0,6 V. $U_\mathrm{CE}$ reicht von rund 0,2 V bis zu einigen 10 V. $U_\mathrm{CB}$ ist die Sperrspannung der CB-Diode. **Gültigkeit:** Knoten- und Maschenregel gelten in jedem Betriebszustand.

:::herleitung Wie viele Größen frei sind
Ein Bauteil mit $n$ Anschlüssen hat $n$ Ströme. Es speichert keine Ladung, also nimmt die Knotenregel ([Teil 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)) einen Strom weg. Es hat $n$ Potenziale, aber nur Differenzen zählen, also bleiben $n-1$ Spannungen. Die Diode ($n=2$) hat eine Spannung, einen Strom und eine Kurve. Der Transistor ($n=3$) hat zwei Spannungen und zwei Ströme. Sein Inneres verknüpft sie durch zwei Gleichungen,

$$I_\mathrm{B}=f(U_\mathrm{BE},U_\mathrm{CE}),\qquad I_\mathrm{C}=g(U_\mathrm{BE},U_\mathrm{CE}).$$

Er ist also ein Zweitor ([Teil 6](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore/zweitore.html)), dessen beide Tore sich den Emitter teilen.
:::

**Beispiel.** Im Rechenmodell sind $\varphi_\mathrm{E}=0$, $\varphi_\mathrm{B}=0{,}6$ V, $\varphi_\mathrm{C}=6$ V. Damit ist $U_\mathrm{BE}=0{,}6$ V, $U_\mathrm{CE}=6$ V und $U_\mathrm{CB}=5{,}4$ V. Die BE-Diode leitet, denn ihre p-Seite liegt höher. Die CB-Diode sperrt, denn ihre n-Seite liegt 5,4 V höher. Aus $I_\mathrm{C}=2$ mA und $I_\mathrm{B}=10$ µ A folgt $I_\mathrm{E}=2{,}01$ mA. **Grenzfall:** Für $U_\mathrm{CB}=0$ ist $U_\mathrm{CE}=U_\mathrm{BE}$. Dort endet der Normalbetrieb.

:::frage Kann ich einen Transistor aus zwei Dioden zusammenlöten?
Nein. Das Ersatzbild aus zwei Dioden zeigt nur die Polung der Grenzen. In zwei getrennten Dioden rekombiniert jedes Elektron, lange bevor es die zweite Sperrschicht erreicht, und die gesperrte Diode bleibt gesperrt. Der Transistoreffekt entsteht erst dadurch, dass beide Grenzen enger beieinanderliegen, als ein Elektron im p-Gebiet überlebt.
:::

:::aufgabe Aufgabe 1 ★ Vom Potenzial zur Spannung
<span class="anker" id="aufg-1"></span>

Gegen Masse werden $\varphi_\mathrm{E}=1{,}2$ V, $\varphi_\mathrm{B}=1{,}85$ V und $\varphi_\mathrm{C}=7$ V gemessen, dazu $I_\mathrm{B}=15$ µ A und $I_\mathrm{C}=3$ mA. (a) Bestimme $U_\mathrm{BE}$, $U_\mathrm{CE}$, $U_\mathrm{CB}$ und prüfe [(1.1)](#gl-1-1). (b) Wie groß ist $I_\mathrm{E}$? (c) Auf welchen Wert muss $\varphi_\mathrm{C}$ fallen, damit $U_\mathrm{CB}=0$ wird?

:::loesung
(a) $U_\mathrm{BE}=0{,}65$ V, $U_\mathrm{CE}=5{,}8$ V, $U_\mathrm{CB}=5{,}15$ V. Probe: $5{,}15\,\mathrm{V}+0{,}65\,\mathrm{V}=5{,}8$ V. (b) $I_\mathrm{E}=3{,}015$ mA. (c) $U_\mathrm{CB}=0$ heißt $\varphi_\mathrm{C}=\varphi_\mathrm{B}=1{,}85$ V.
:::
:::

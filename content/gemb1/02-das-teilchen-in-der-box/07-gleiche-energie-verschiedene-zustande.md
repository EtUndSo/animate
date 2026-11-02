---
title: Stufe 5: Gleiche Energie, verschiedene Zustände
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Das Teilchen in der Box
order: 4120700
summary: Im Quadrat treffen sich manche Energien.
tags: entartet, Entartungsgrad, Niveau, zufällige Entartung
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Im Quadrat treffen sich manche Energien. Diese Stufe erklärt, woher das kommt, und zeigt, wie man Zustände und Niveaus richtig zählt.
:::

**Die Idee.** Im Quadrat sind $x$ und $y$ gleichwertig: Um 90° gedreht sieht die Box gleich aus. Bei dieser Drehung wird aus dem Muster $(2,1)$ das Muster $(1,2)$. Es sind verschiedene Funktionen, aber ihre Krümmung ist dieselbe, also auch ihre Energie. Streckt man die Box in einer Richtung, hebt das die Gleichheit auf (Abb. [5](#abb-5)).

:::definition Definition 5.1 (Entartung)
<span class="anker" id="satz-5-1"></span>

Gehören zu einem Energiewert mehrere verschiedene Zustände, heißt er __entartet__. Die Zahl $g$ dieser linear unabhängigen Zustände ist der __Entartungsgrad__. Ein __Niveau__ ist ein Energiewert, ein Zustand eine Wellenfunktion: Ein Niveau mit Grad $g$ enthält $g$ Zustände.
:::

:::satz Satz 5.2 (Quadratische Box)
<span class="anker" id="satz-5-2"></span>

Für $L_x=L_y=L$ und $m_x=m_y=m$ gilt

<span class="anker" id="gl-5-1"></span>
$$E_{n_x,n_y}=E_0\,(n_x^2+n_y^2)+V_0,\qquad E_0=\frac{\hbar^2\pi^2}{2mL^2}. \tag{5.1}$$

Für $n_x\neq n_y$ ist $E_{n_x,n_y}=E_{n_y,n_x}$, also $g\ge2$. Für $n_x=n_y$ hat ein Zustand keinen Partner dieser Art.
:::

⁠**So liest man das:** $E_0$ ist die Nullpunktsenergie einer Box der Breite $L$, für $m=m_0$ also $E_0=0{,}376\,\mathrm{eV\,nm^2}/L^2$. Die Vertauschung ist eine Symmetrie der Box, und Symmetrie ist die Ursache dieser Entartung. Es gibt daneben __zufällige Entartung__: Zwei Summen von Quadraten können ohne jede Symmetrie gleich sein. So ist $1^2+7^2=5^2+5^2=50$, das Niveau $50\,E_0$ hat die Zustände $(1,7)$, $(7,1)$ und $(5,5)$, also $g=3$. Deshalb steht im Satz $g\ge2$ und nicht $g=2$. Sicher ist nur das Verfahren: alle Kombinationen ausrechnen und sortieren.

**Beispiel.** Für $L=2$ nm ist $E_0=94$ meV:

| Zustände | $(1,1)$ | $(1,2)$, $(2,1)$ | $(2,2)$ | $(1,3)$, $(3,1)$ | $(2,3)$, $(3,2)$ |
|---|---|---|---|---|---|
| $E/E_0$ | 2 | 5 | 8 | 10 | 13 |
| $g$ | 1 | 2 | 1 | 2 | 2 |
| $E$ in meV | 188 | 470 | 752 | 940 | 1222 |

:::abbildung gemb1/k2entartung 5
Niveaus in Einheiten von $E_0$. Links die quadratische Box, doppelte Linien sind zweifach entartet. Rechts die um 10 % in $x$ gestreckte Box: Jedes Paar spaltet auf. Die Stufe in der längeren Richtung kostet weniger, deshalb liegt $(2,1)$ unter $(1,2)$.
:::

**Symmetrie brechen.** Mit $L_x=1{,}1\,L_y$ ist $E=E_0(n_x^2/1{,}21+n_y^2)$, wobei $E_0$ mit $L_y$ gebildet ist. Aus dem Paar bei $5\,E_0$ werden $E_{2,1}=4{,}31\,E_0$ und $E_{1,2}=4{,}83\,E_0$, im Modell 49 meV Abstand. Die Entartung ist aufgehoben, weil die Vertauschung die Box nicht mehr in sich selbst überführt. Ungleiche Massen wirken genauso. **Grenzfall:** Für $L_x\to L_y$ schließt sich die Lücke stetig.

:::frage Sind entartete Zustände nicht in Wahrheit derselbe Zustand?
Nein. $\psi_{2,1}$ hat eine Knotenlinie quer zur $x$-Achse, $\psi_{1,2}$ eine quer zur $y$-Achse. An der Stelle $(L/2,\,L/4)$ ist das eine null, das andere nicht. Nur die Energie ist gleich, die Aufenthaltsorte sind es nicht.
:::

:::aufgabe Aufgabe 7 ★★★ Symmetrie oder Zufall?
<span class="anker" id="aufg-7"></span>

<ol class="al">

<li>

Finde in der quadratischen Box alle Zustände mit $n_x^2+n_y^2=25$, $50$ und $85$. Wie groß ist jeweils $g$?

</li>

<li>

Die Box wird auf $L_x=1{,}1\,L_y$ gestreckt. Berechne die Energien der drei Zustände mit der Summe 50 in Einheiten von $E_0$. Bleibt etwas entartet?

</li>

<li>

In Aufgabe [6](die-box-in-der-ebene.html#aufg-6) haben $(2,2)$ und $(4,1)$ dieselbe Energie, obwohl das Rechteck keine Vertauschungssymmetrie hat. Woher kommt das?

</li>

</ol>

:::loesung
(a) Summe 25: $(3,4)$, $(4,3)$, $g=2$. Summe 50: $(1,7)$, $(7,1)$, $(5,5)$, $g=3$. Summe 85: $(2,9)$, $(9,2)$, $(6,7)$, $(7,6)$, $g=4$. (b) $(5,5)$: $25/1{,}21+25=45{,}7$. $(1,7)$: $1/1{,}21+49=49{,}8$. $(7,1)$: $49/1{,}21+1=41{,}5$, jeweils in $E_0$. Nichts bleibt entartet. (c) Das ist Zufall: Eine Drehung um 90° führt das Rechteck nicht in sich über, aber wegen $L_x=2L_y$ ist $2^2+4\cdot2^2=4^2+4\cdot1^2$. Schon eine kleine Änderung von $L_x$ hebt die Gleichheit auf.
:::
:::

---
title: Stufe 7: Metallische Bindung
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Chemische Bindung
order: 4150900
summary: Ein Lithiumatom hat ein Valenzelektron, aber viele Nachbarn.
tags: Elektronengas
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Ein Lithiumatom hat ein Valenzelektron, aber viele Nachbarn. Für Elektronenpaare zu allen reicht das nicht, und einen Partner, der das Elektron nimmt, gibt es unter Lithiumatomen auch nicht. Diese Stufe zeigt die dritte Lösung.
:::

**Die Idee.** Das äußerste Elektron ist nur schwach gebunden. Die näher am Kern liegenden, gefüllten Orbitale schirmen das Coulomb-Potential ab ([Teil 4](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/atome-und-orbitale/atome-und-orbitale.html)), und auf gleicher Tiefe ist der abgeschirmte Trichter schmaler (Abb. [7](#abb-7)). Wie in einer kürzeren Box liegt das Niveau dadurch höher, und das Atom ist leichter zu ionisieren. Geben alle Atome eines Verbunds Elektronen ab, nimmt sie niemand auf. Sie bleiben zwischen den Atomen, gehören allen zugleich und sind frei beweglich. Sie bilden ein __Elektronengas__. Zurück bleiben positive Atomrümpfe, meist mit Edelgaskonfiguration, und das negative Gas hält sie zusammen wie ein elektrostatischer Kleister. Das ist die metallische Bindung.

:::abbildung gemb1/k5metall 7
Links: Potentielle Energie $V(r)$ des 2s-Elektrons im Lithium ohne und mit den abschirmenden 1s-Elektronen (Modellkurven) und die zugehörigen Niveaus. Rechts: Atomrümpfe im Elektronengas.
:::

:::satz Satz 7.1 (Einsperrenergie im Elektronengas)
<span class="anker" id="satz-7-1"></span>

$N$ Atome im Abstand $a$ auf einer Kette geben je ein Elektron in eine Box der Länge $L=Na$. Für große $N$ ist die mittlere Bewegungsenergie

<span class="anker" id="gl-7-1"></span>
$$\bar E_\mathrm{kin}=\frac1{12}\,\frac{h^2}{8m_0a^2}. \tag{7.1}$$
:::

⁠**So liest man das:** Der Bruch rechts ist die Grundzustandsenergie einer Box der Breite $a$, also eines Elektrons auf dem Platz eines Atoms. Das gemeinsame Gas senkt die Bewegungsenergie auf ein Zwölftel, obwohl das Pauli-Prinzip die Elektronen in höhere Niveaus zwingt. Hinzu kommt die Anziehung: Jeder Rumpf sitzt mitten in negativer Ladung. **Gültigkeit:** Modell in einer Dimension ohne Abstoßung der Elektronen. Es erklärt das Vorzeichen, nicht die genaue Zahl.

:::herleitung Niveaus zählen
Die Niveaus sind $E_n=n^2h^2/(8m_0L^2)$ ([Teil 2](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/das-teilchen-in-der-box/das-teilchen-in-der-box.html)) mit je zwei Elektronen, $N$ Elektronen füllen $n=1$ bis $N/2$. Mit $\sum_{n=1}^{N/2}n^2\approx(N/2)^3/3$ ist die Gesamtenergie $2\cdot\frac{N^3}{24}\cdot\frac{h^2}{8m_0N^2a^2}$. Geteilt durch $N$ kürzt sich jedes $N$ heraus.
:::

::::beispiel
Ohne Abschirmung läge das 2s-Elektron des Lithiums bei $-13{,}6\,\mathrm{eV}\cdot9/4=-30{,}6$ eV, gemessen ist $-5{,}39$ eV. Bei $a=0{,}30$ nm ist die Boxenergie 4,18 eV, ihr Zwölftel 0,35 eV. Im Modell spart jedes Elektron 3,8 eV Bewegungsenergie.
::::

⁠**Grenzfall:** Für $N=2$ ist $\bar E_\mathrm{kin}$ ein Viertel der Boxenergie. Schon zwei Atome gewinnen den Großteil, das ist das Bild der längeren Box aus Stufe [3](zwei-atome-teilen-elektronen.html#stufe-3).

**Eigenschaften.** Die frei beweglichen Elektronen erklären die hohe Leitfähigkeit von Gold, Aluminium, Kupfer oder Silber. Zwischen verschiedenen Elementen gibt es keinen Grund für feste Zahlenverhältnisse, Legierungen (Metallmischungen) entstehen in vielen Verhältnissen. Die Bindung ist nicht gerichtet: Die Atome ordnen sich möglichst dicht an, wie Kugeln in einer Kiste, und können aneinander vorbeigleiten. Darum lässt sich Kupfer zu Draht ziehen. Die Bindungsenergie ist meist kleiner als bei ionischen und kovalenten Bindungen, von 1 eV (Na) bis 3 eV (Al) je Atom. Übergangsmetalle erreichen mehr, zum Beispiel 8,6 eV bei Wolfram, weil die Elektronen der nicht aufgefüllten Schalen zusätzlich kovalent binden.

:::frage Wird das Atom beim Abschirmen kleiner? Die kürzere Box klingt danach.
Nein, das Bild endet hier. Die kürzere Box vergleicht die Trichter auf gleicher Tiefe. Das Niveau liegt dadurch höher, und dort ist der Trichter weit: Der Umkehrradius ist $1{,}44\,\mathrm{eV\,nm}/5{,}39\,\mathrm{eV}=0{,}27$ nm, fast der Abstand zum Nachbarn. Darum reicht das Elektron bis zu den nächsten Atomen.
:::

:::aufgabe Aufgabe 9 ★★ Das Gas nachzählen
<span class="anker" id="aufg-9"></span>

<ol class="al">

<li>

Berechne $\bar E_\mathrm{kin}$ mit $\sum_{n=1}^Mn^2=M(M+1)(2M+1)/6$ exakt für $N=2$, 4, 10, 100 und vergleiche mit [(7.1)](#gl-7-1).

</li>

<li>

Natrium schmilzt bei 371 K, Aluminium bei 933 K, Wolfram bei 3695 K. Berechne das Verhältnis von Bindungsenergie zu $k_\mathrm BT$ am Schmelzpunkt.

</li>

</ol>

:::loesung
(a) In Einheiten von $h^2/(8m_0a^2)$: 0,250 für $N=2$, 0,156 für $N=4$, 0,110 für $N=10$, 0,0858 für $N=100$, Grenzwert $1/12=0{,}0833$. (b) $k_\mathrm BT$ am Schmelzpunkt ist 32, 80 und 318 meV, das Verhältnis 31, 37 und 27. Ein Metall schmilzt weit unterhalb von $k_\mathrm BT=E_\mathrm B$.
:::
:::

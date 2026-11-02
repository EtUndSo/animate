---
title: Stufe 4: Richtung und Vorzeichen der Orbitale
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Chemische Bindung
order: 4150600
summary: s-Orbitale sind rund.
tags: \pi-Orbital, lokalisiert
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
s-Orbitale sind rund. p-Orbitale haben eine Richtung und zwei Keulen mit verschiedenem Vorzeichen. Diese Stufe klärt, welche Orbitale überhaupt koppeln und wie stark.
:::

**Die Idee.** Das Integral $H_\mathrm{AB}$ summiert das Produkt beider Wellen über den Raum. Wo Keulen gleichen Vorzeichens überlappen, trägt es zur Bindung bei, wo verschiedene überlappen, dagegen. Trifft ein Orbital mit gleich viel Plus und Minus auf das andere, ist die Summe null: Die beiden koppeln nicht, wie nah sie auch kommen. Es zählt also nicht, ob sich Orbitale berühren, sondern ob die Symmetrie eine Kopplung zulässt.

:::abbildung gemb1/k5ueberlapp 4
Kopplung $H_\mathrm{AB}$ zwischen Orbitalen zweier Atome, die Kernachse ist $z$. Blau: positives Vorzeichen, rot: negatives. Gezeichnet ist die Lage, in der gleiche Vorzeichen überlappen. Unten Mitte und rechts heben sich Plus und Minus auf.
:::

:::definition Definition 4.1 (Kopplung und Typen der Bindung)
<span class="anker" id="satz-4-1"></span>

Die Kopplung zweier Orbitale ist $H_\mathrm{AB}=\int\phi_\mathrm A\hat H\phi_\mathrm B\,\mathrm{d} V$, ihre Beträge heißen $V_\mathrm{ss}$, $V_{\mathrm{sp}\sigma}$, $V_{\mathrm{pp}\sigma}$, $V_{\mathrm{pp}\pi}$. Überlappen gleiche Vorzeichen, ist $H_\mathrm{AB}$ negativ, überlappen verschiedene, positiv. Hebt die Symmetrie alles auf, ist $H_\mathrm{AB}=0$. Ein $\sigma$-Orbital entsteht bei Überlapp entlang der Kernachse. Ein __$\pi$-Orbital__ entsteht aus p-Orbitalen quer zur Achse: Die Achse liegt in seiner Knotenebene, die Dichte sitzt darüber und darunter.
:::

⁠**So liest man das:** Der Index sagt, welche Orbitale koppeln und wie sie liegen. $V_{\mathrm{pp}\sigma}$ ist größer als $V_{\mathrm{pp}\pi}$, denn frontal überlappen Keulen stärker als seitlich. Die Bindung C–C bringt als $\sigma$-Bindung 3,6 eV, die $\pi$-Bindung der Doppelbindung 2,8 eV. **Gültigkeit:** Orbitale benachbarter Atome. Am selben Atom koppeln verschiedene Orbitale nicht, denn sie sind orthogonal.

**Beispiel.** Ein Stickstoffatom hat drei einfach besetzte p-Orbitale. In N$_2$ überlappen die $\mathrm p_z$ frontal zu einem $\sigma$-Orbital, die $\mathrm p_x$ und die $\mathrm p_y$ seitlich zu zwei $\pi$-Orbitalen. Das sind drei Elektronenpaare, eine Dreifachbindung mit 9,8 eV. **Grenzfall:** Vertauscht man bei einem Orbital Plus und Minus, ändert sich nur das Vorzeichen von $H_\mathrm{AB}$, die Energien bleiben.

**Eigenschaften.** Das Elektronenpaar sitzt zwischen zwei Atomen, es ist __lokalisiert__, und beide ziehen ähnlich stark daran. Die Bindungsenergie liegt bei etwa 4 bis 12 eV. Anders als bei Ionen geben die Orbitale die Richtungen vor. Das bestimmt die Gestalt von Molekülen und den meist locker gepackten Aufbau kovalenter Festkörper. Die Zahlenverhältnisse sind stöchiometrisch. Bei Elementen höherer Perioden können auch d-Orbitale beteiligt sein. Kovalente Festkörper wie Silizium oder Diamant sind Halbleiter oder Isolatoren, weil ihre Elektronen in den Bindungen festsitzen.

:::frage Zwei $\mathrm p_z$-Orbitale mit derselben Ausrichtung sind doch gleichphasig. Warum ist $\phi_\mathrm A+\phi_\mathrm B$ hier antibindend?
Weil sich die Pluskeule des linken und die Minuskeule des rechten Atoms treffen. Die Summe erzeugt dort einen Knoten, bindend ist $\phi_\mathrm A-\phi_\mathrm B$. „Gleichphasig“ meint gleiche Vorzeichen im Überlappgebiet, nicht gleiche Koeffizienten.
:::

:::aufgabe Aufgabe 5 ★★★ Vier Orbitale an zwei Atomen
<span class="anker" id="aufg-5"></span>

Atom A liegt links, Atom B rechts auf der $z$-Achse. Jedes trägt ein s-Orbital und ein $\mathrm p_z$-Orbital, dessen Pluskeule nach $+z$ zeigt. Nur Orbitale verschiedener Atome koppeln.

<ol class="al">

<li>

Bestimme aus den Vorzeichen, die sich treffen, $H_{\mathrm{ss}}$, $H_{\mathrm s_\mathrm A\mathrm p_\mathrm B}$, $H_{\mathrm p_\mathrm A\mathrm s_\mathrm B}$ und $H_{\mathrm{pp}}$ in den Beträgen $V_\mathrm{ss}$, $V_{\mathrm{sp}\sigma}$, $V_{\mathrm{pp}\sigma}$.

</li>

<li>

Stelle die $4\times4$-Matrix für $\psi=c_1\phi_{\mathrm s\mathrm A}+c_2\phi_{\mathrm s\mathrm B}+c_3\phi_{\mathrm p\mathrm A}+c_4\phi_{\mathrm p\mathrm B}$ auf. Die Diagonale sei $E_\mathrm s,E_\mathrm s,E_\mathrm p,E_\mathrm p$.

</li>

<li>

Setze $V_{\mathrm{sp}\sigma}=0$. Zeige, dass die Matrix in zwei $2\times2$-Blöcke zerfällt, und berechne die Energien für $E_\mathrm s=-12$ eV, $E_\mathrm p=-6$ eV, $V_\mathrm{ss}=1{,}5$ eV, $V_{\mathrm{pp}\sigma}=2{,}5$ eV. Welche Kombination der p-Orbitale ist bindend?

</li>

<li>

Vorhersage: Rücken die Niveaus zusammen oder auseinander, wenn $V_{\mathrm{sp}\sigma}=1{,}5$ eV hinzukommt? Prüfe mit einem Rechner.

</li>

</ol>

:::loesung
(a) $\mathrm s_\mathrm A$ und $\mathrm s_\mathrm B$: Plus auf Plus, $H_{\mathrm{ss}}=-V_\mathrm{ss}$. $\mathrm s_\mathrm A$ trifft die Minuskeule von $\mathrm p_\mathrm B$: $+V_{\mathrm{sp}\sigma}$. Die Pluskeule von $\mathrm p_\mathrm A$ trifft $\mathrm s_\mathrm B$: $-V_{\mathrm{sp}\sigma}$. Plus von $\mathrm p_\mathrm A$ trifft Minus von $\mathrm p_\mathrm B$: $+V_{\mathrm{pp}\sigma}$. (b) Die Zeilen sind $(E_\mathrm s,-V_\mathrm{ss},0,V_{\mathrm{sp}\sigma})$, $(-V_\mathrm{ss},E_\mathrm s,-V_{\mathrm{sp}\sigma},0)$, $(0,-V_{\mathrm{sp}\sigma},E_\mathrm p,V_{\mathrm{pp}\sigma})$, $(V_{\mathrm{sp}\sigma},0,V_{\mathrm{pp}\sigma},E_\mathrm p)$. (c) Ohne $V_{\mathrm{sp}\sigma}$ bleiben die Blöcke s und p: $E=E_\mathrm s\mp V_\mathrm{ss}=-13{,}5$ eV und $-10{,}5$ eV, $E=E_\mathrm p\mp V_{\mathrm{pp}\sigma}=-8{,}5$ eV und $-3{,}5$ eV. Bindend ist $\phi_{\mathrm p\mathrm A}-\phi_{\mathrm p\mathrm B}$ bei $-8{,}5$ eV, denn so treffen sich gleiche Vorzeichen. (d) Auseinander: $-13{,}92$; $-10{,}81$; $-8{,}09$; $-3{,}19$ eV. Gekoppelte Niveaus stoßen sich ab, die Summe bleibt $-36$ eV, die Spur der Matrix.
:::
:::

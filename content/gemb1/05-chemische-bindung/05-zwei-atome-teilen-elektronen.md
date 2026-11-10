---
title: Stufe 3: Zwei Atome teilen Elektronen
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Chemische Bindung
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/chemische-bindung
knoten: Kapitel 5: Chemische Bindung
order: 4150500
summary: Zwei Wasserstoffatome haben dieselbe Elektronegativität.
tags: bindendes Molekülorbital, antibindendes Molekülorbital, \sigma-Orbital, Kopplungsenergie
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Zwei Wasserstoffatome haben dieselbe Elektronegativität. Keines gibt sein Elektron ab, und doch gewinnen sie 4,75 eV. Diese Stufe zeigt, woher diese Energie kommt.
:::

**Die Idee.** Atome mit ähnlicher, mittlerer bis hoher Elektronegativität binden sich, indem ihre einfach besetzten Atomorbitale überlappen. Zwei Wellen können sich auf zwei Arten überlagern. Gleichphasig addieren sie sich zwischen den Kernen: Die Welle wird breiter und weniger gekrümmt, und ihre Dichte rückt zwischen die Kerne, wo beide sie anziehen. Die Energie sinkt. Gegenphasig löschen sie sich in der Mitte aus: Ein Knoten entsteht, die Krümmung wächst, die Dichte fehlt zwischen den Kernen. Die Energie steigt. Aus zwei Atomorbitalen werden zwei Molekülorbitale. Beide Elektronen passen mit entgegengesetztem Spin ins untere, und jedes Atom sieht zwei Elektronen um sich, wie Helium. So helfen sich die Atome gegenseitig zur Edelgaskonfiguration.

:::abbildung gemb1/k5molekuel 3
Links: Das Niveau 1s spaltet in H$_2$ auf, beide Elektronen besetzen das untere Orbital (nicht maßstäblich). Rechts: Dichte eines Elektrons auf der Kernachse bei $r_0=1{,}4\,r_1$ mit dem Bohr-Radius $r_1$. Punkte: Kerne, gestrichelt: Mittel der Dichten beider Atome.
:::

:::definition Definition 3.1 (Molekülorbital)
<span class="anker" id="satz-3-1"></span>

Ein Molekülorbital ist ein Zustand eines Elektrons im Feld mehrerer Kerne, näherungsweise eine Summe von Atomorbitalen. Ein __bindendes Molekülorbital__ liegt energetisch unter den Atomorbitalen, ein __antibindendes Molekülorbital__ darüber. Ein __$\sigma$-Orbital__ ist rund um die Kernachse symmetrisch, sein antibindendes Gegenstück heißt $\sigma^*$.
:::

:::satz Satz 3.2 (Zwei gekoppelte Orbitale)
<span class="anker" id="satz-3-2"></span>

Mit $\psi=c_\mathrm A\phi_\mathrm A+c_\mathrm B\phi_\mathrm B$ wird die Schrödinger-Gleichung zu

<span class="anker" id="gl-3-1"></span>
$$\begin{pmatrix}E_\mathrm{AO}&-V_\mathrm{ss}\\-V_\mathrm{ss}&E_\mathrm{AO}\end{pmatrix}\begin{pmatrix}c_\mathrm A\\c_\mathrm B\end{pmatrix}=E\begin{pmatrix}c_\mathrm A\\c_\mathrm B\end{pmatrix} \quad\Rightarrow\quad \begin{aligned} E_\sigma&=E_\mathrm{AO}-V_\mathrm{ss},&c_\mathrm A&=c_\mathrm B,\\ E_{\sigma^*}&=E_\mathrm{AO}+V_\mathrm{ss},&c_\mathrm A&=-c_\mathrm B. \end{aligned} \tag{3.1}$$

Zwei Elektronen im bindenden Orbital gewinnen $E_\mathrm B=2(E_\mathrm{AO}-E_\sigma)=2V_\mathrm{ss}$.
:::

⁠**So liest man das:** $\phi_\mathrm A,\phi_\mathrm B$ sind die Atomorbitale, $E_\mathrm{AO}$ ihre Energie, in H$_2$ also 1s mit $-13{,}6$ eV. Die __Kopplungsenergie__ $V_\mathrm{ss}>0$ spielt dieselbe Rolle wie der Hüpfparameter $t_0$ in [Kapitel 2](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/das-teilchen-in-der-box/das-teilchen-in-der-box.html): [(3.1)](#gl-3-1) ist die Hamilton-Matrix zweier gekoppelter Plätze. Sie fällt mit dem Abstand wie die Ausläufer der Orbitale ([Kapitel 3](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/stufe-barriere-und-tunneleffekt/stufe-barriere-und-tunneleffekt.html)), bei Wasserstoff ungefähr wie $\mathrm{e}^{-r/r_1}$. **Gültigkeit:** zwei gleiche Atome, $\int\phi_\mathrm A\phi_\mathrm B\,\mathrm{d} V$ vernachlässigt. Das ist grob, denn dieses Überlappintegral ist in H$_2$ 0,75. Mit ihm steigt $\sigma^*$ stärker, als $\sigma$ sinkt. Die Elektronen stoßen sich außerdem ab, $V_\mathrm{ss}$ ist ein effektiver Wert.

:::herleitung Von der Überlagerung zur Matrix
Einsetzen in $\hat H\psi=E\psi$, Multiplizieren mit $\phi_\mathrm A$ und Integrieren ergibt $c_\mathrm AE_\mathrm{AO}+c_\mathrm BH_\mathrm{AB}=E\,c_\mathrm A$ mit $H_\mathrm{AB}=\int\phi_\mathrm A\hat H\phi_\mathrm B\,\mathrm{d} V=-V_\mathrm{ss}$. Mit $\phi_\mathrm B$ folgt die zweite Zeile. Das Minuszeichen stammt daher, dass $\hat H$ im Überlappgebiet vor allem die negative Energie im Feld der Kerne enthält. Die Bedingung $\det=0$ lautet $(E_\mathrm{AO}-E)^2=V_\mathrm{ss}^2$.
:::

:::analogie
Zwei gleiche LC-Schwingkreise mit $\omega_0=1/\sqrt{L_\mathrm SC}$ und der Gegeninduktivität $M$ schwingen gemeinsam auf zwei Arten: gleichphasig mit $\omega_0/\sqrt{1+k_\mathrm M}$, gegenphasig mit $\omega_0/\sqrt{1-k_\mathrm M}$, wobei $k_\mathrm M=M/L_\mathrm S$. Die tiefere, gleichphasige Frequenz entspricht $\sigma$, die höhere $\sigma^*$. Das Bild endet an zwei Stellen: Die Frequenzen liegen nicht genau symmetrisch, und Schwingkreise kennen kein Pauli-Prinzip.
:::

::::beispiel
Aus $E_\mathrm B=4{,}75$ eV folgt $V_\mathrm{ss}=2{,}37$ eV, also $E_\sigma=-15{,}97$ eV und $E_{\sigma^*}=-11{,}22$ eV. Zwischen den Kernen ist die Dichte im bindenden Orbital 14 % höher als im Mittel der Atome, auf den abgewandten Seiten kleiner. Im antibindenden Orbital ist sie in der Mitte null, das wirkt abstoßend. Beim weiteren Annähern stoßen sich die Kerne ab, innere Schalen hat H$_2$ nicht.
::::

⁠**Grenzfälle:** Für $r\to\infty$ geht $V_\mathrm{ss}\to0$, beide Niveaus enden bei $E_\mathrm{AO}$. Zwei Heliumatome (1s$^2$) müssen beide Orbitale doppelt besetzen. Gewinn $-2V_\mathrm{ss}$ und Verlust $+2V_\mathrm{ss}$ heben sich auf, mit Überlappintegral überwiegt der Verlust. Darum bleibt Helium einatomig, und das ist der Mechanismus der Abstoßung voller Hüllen aus Stufe [1](die-energiekurve-der-bindung.html#stufe-1).

:::frage Sinkt die Energie, weil das Elektron mehr Platz hat, oder weil es zwischen den Kernen sitzt?
Beides gehört zusammen. Mehr Platz senkt die Krümmungsenergie wie in der längeren Box aus [Kapitel 2](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/das-teilchen-in-der-box/das-teilchen-in-der-box.html). Im fertigen Molekül lässt sich die Kraft auf jeden Kern elektrostatisch verstehen: Die Ladung zwischen den Kernen zieht beide nach innen und hält ihrer Abstoßung die Waage.
:::

:::aufgabe Aufgabe 4 ★★ Orbitale füllen
<span class="anker" id="aufg-4"></span>

<ol class="al">

<li>

Verteile die Elektronen von H$_2^+$, H$_2$, H$_2^-$, He$_2^+$ und He$_2$ auf $\sigma$ und $\sigma^*$. Gib den Gewinn in Vielfachen von $V_\mathrm{ss}$ an. Welche sind gebunden?

</li>

<li>

H$_2^+$ gewinnt 2,79 eV, H$_2$ nur 4,75 eV statt des Doppelten. Nenne einen Grund.

</li>

<li>

Vorhersage: Zwei Wasserstoffatome treffen sich mit parallelem Spin. Was geschieht?

</li>

</ol>

:::loesung
(a) H$_2^+$: $\sigma^1$, Gewinn $V_\mathrm{ss}$. H$_2$: $\sigma^2$, $2V_\mathrm{ss}$. H$_2^-$ und He$_2^+$: $\sigma^2\sigma^{*1}$, $V_\mathrm{ss}$. He$_2$: $\sigma^2\sigma^{*2}$, null. Gebunden sind alle außer He$_2$. (b) Die beiden Elektronen in H$_2$ stoßen sich ab. (c) Nach Pauli muss ein Elektron nach $\sigma^*$, der Gewinn verschwindet, die Atome stoßen sich ab.
:::
:::

---
title: Stufe 5: Hybridisierung im Tetraeder
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Chemische Bindung
order: 4150700
summary: Kohlenstoff, 1mathrm s 2\,2mathrm s 2\,2mathrm p 2 , hat zwei einfach besetzte p-Orbitale, das 2s-Paar kann keine Bindung mehr eingehen.
tags: Tetraeders, Hybridorbitale, freie Elektronenpaar, Lewis-Schreibweise
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Kohlenstoff, $1\mathrm s^2\,2\mathrm s^2\,2\mathrm p^2$, hat zwei einfach besetzte p-Orbitale, das 2s-Paar kann keine Bindung mehr eingehen. Danach sollte CH$_2$ entstehen. Stabil ist aber CH$_4$ mit vier gleichen Bindungen. Diese Stufe löst den Widerspruch.
:::

**Die Idee.** Zwei Schritte führen zur Lösung (Abb. [5](#abb-5)). Erstens: Hebt man ein 2s-Elektron nach 2p, gibt es vier einfach besetzte Orbitale und damit vier statt zwei Bindungen. Das kostet Energie, die zwei zusätzlichen Bindungen bringen mehr. Zweitens: Eine Summe von Lösungen ähnlicher Energie ist näherungsweise wieder eine Lösung ([Teil 4](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/atome-und-orbitale/atome-und-orbitale.html)). Überlagert man s und p, verstärken sie sich auf einer Seite und löschen sich auf der anderen aus. Es entsteht eine einseitige Keule, die stärker überlappen kann als s oder p allein. Die vier Keulen stoßen sich ab und weichen einander aus: Sie zeigen in die Ecken eines __Tetraeders__, einer Pyramide aus vier gleichseitigen Dreiecken.

:::abbildung gemb1/k5hybrid 5
Oben: Besetzung von Kohlenstoff bis zu vier gleichen Orbitalen, daneben die Überlagerung von s und p (Winkelanteil, gleicher Maßstab). Unten: Tetraederrichtungen in CH$_4$, NH$_3$ und H$_2$O. Blau: Bindungen, orange: freie Elektronenpaare, rot: gemessener Winkel H–X–H.
:::

:::definition Definition 5.1 (sp$^3$-Hybridorbitale)
<span class="anker" id="satz-5-1"></span>

Aus $\phi_\mathrm s$ (2s) und $\phi_x,\phi_y,\phi_z$ (2p) entstehen durch Linearkombination vier __Hybridorbitale__

<span class="anker" id="gl-5-1"></span>
$$\begin{aligned} \phi_\mathrm{h1}&=\tfrac12(\phi_\mathrm s+\phi_x+\phi_y+\phi_z),&\phi_\mathrm{h2}&=\tfrac12(\phi_\mathrm s+\phi_x-\phi_y-\phi_z),\\ \phi_\mathrm{h3}&=\tfrac12(\phi_\mathrm s-\phi_x+\phi_y-\phi_z),&\phi_\mathrm{h4}&=\tfrac12(\phi_\mathrm s-\phi_x-\phi_y+\phi_z). \end{aligned} \tag{5.1}$$
:::

:::satz Satz 5.2 (Winkel aus dem Mischverhältnis)
<span class="anker" id="satz-5-2"></span>

Ein Hybrid mit dem Gewicht $w$ auf einem p-Orbital in Richtung $\boldsymbol d$ ist $\phi_\mathrm h=(\phi_\mathrm s+w\,\phi_{\boldsymbol d})/\sqrt{1+w^2}$. Für zwei orthogonale gleichartige Hybride gilt

<span class="anker" id="gl-5-2"></span>
$$\cos\beta=-\frac1{w^2},\qquad\text{bei sp}^3\text{ mit }w^2=3:\quad\beta=109{,}47^\circ. \tag{5.2}$$

Die Summe der Dichten aller vier Hybride ist gleich der Summe der Dichten von 2s, 2p$_x$, 2p$_y$, 2p$_z$.
:::

⁠**So liest man das:** $\beta$ ist der Winkel zwischen zwei Keulen, $\phi_{\boldsymbol d}=d_x\phi_x+d_y\phi_y+d_z\phi_z$ ein p-Orbital in Richtung des Einheitsvektors $\boldsymbol d$. Der s-Anteil ist $1/(1+w^2)$, bei sp$^3$ also 25 %. Die Keule ist doppelt so hoch wie s und 1,15-mal so hoch wie p. **Gültigkeit:** alle Hybride gleichartig. Das Anheben und Mischen ist ein Rechenweg, kein Ablauf in der Zeit.

:::herleitung Winkel und Dichte
Die Orbitale sind orthonormal, daher ist

$$\int\phi_\mathrm{h1}\phi_\mathrm{h2}\,\mathrm{d} V=\frac{1+w^2\,\boldsymbol d_1\cdot\boldsymbol d_2}{1+w^2}=0\quad\Rightarrow\quad\cos\beta=\boldsymbol d_1\cdot\boldsymbol d_2=-\frac1{w^2}.$$

Orthogonal müssen sie sein, damit verschiedene Zustände entstehen. In [(5.1)](#gl-5-1) ist $w^2=3$ mit den Richtungen $\frac1{\sqrt3}(1,1,1)$, $\frac1{\sqrt3}(1,-1,-1)$ usw. Beim Quadrieren und Summieren von [(5.1)](#gl-5-1) tritt jeder gemischte Term zweimal mit Plus und zweimal mit Minus auf, es bleibt $\sum_i\phi_{\mathrm hi}^2=\phi_\mathrm s^2+\phi_x^2+\phi_y^2+\phi_z^2$.
:::

::::beispiel
Das Anheben kostet in Kohlenstoff 4,2 eV, eine C–H-Bindung bringt im Mittel 4,3 eV, die zwei zusätzlichen also 8,6 eV. Die vier Außenelektronen verteilen sich nach der Hundschen Regel einzeln auf die Hybride, jedes bildet mit einem H-Atom eine $\sigma$-Bindung. In Diamant, Silizium und Germanium verbinden sich die Atome untereinander: Jedes ist tetraedrisch von vier Nachbarn umgeben und hat so acht Elektronen um sich.
::::

⁠**Grenzfall:** Ohne s-Anteil, $w\to\infty$, wird $\beta\to90^\circ$: Reine p-Orbitale stehen rechtwinklig.

**Stickstoff und Sauerstoff.** Stickstoff hat fünf Außenelektronen. Ein Hybrid trägt ein Paar, das __freie Elektronenpaar__, das keine weitere Bindung eingeht, drei bilden $\sigma$-Bindungen. NH$_3$ ist eine Pyramide mit dreieckiger Grundfläche, das freie Paar zeigt in die vierte Ecke. In der __Lewis-Schreibweise__ steht ein Strich für ein Elektronenpaar, ein Punkt für ein Einzelelektron. Formal gilt $|\dot{\mathrm N}\!\cdot+\,3\,\mathrm H\!\cdot\;\to\;|\mathrm{NH}_3$. So läuft die Bildung aber nicht ab, denn freie Atome gibt es nur unter hohem Energieaufwand, etwa in einem Plasma (ionisiertes Gas). Sauerstoff hat sechs Außenelektronen, also zwei freie Paare und zwei $\sigma$-Bindungen. Freie Paare beanspruchen mehr Raum als Bindungen, darum sinkt der Winkel auf $107^\circ$ in NH$_3$ und $104{,}5^\circ$ in H$_2$O. Ohne Hybridisierung erwartete man $90^\circ$.

:::frage Gibt es im freien Kohlenstoffatom vier Keulen, oder sind sie erfunden?
Das freie Atom hat im Grundzustand 2s$^2$ 2p$^2$. Die Hybride beschreiben das gebundene Atom. [(5.1)](#gl-5-1) ist eine Drehung im Raum der vier Orbitale, bei gleicher Besetzung ändert sich die Gesamtdichte nicht. Die Tetraederform von CH$_4$ ist dagegen gemessen.
:::

:::aufgabe Aufgabe 6 ★★ Der Tetraeder nachgerechnet
<span class="anker" id="aufg-6"></span>

<ol class="al">

<li>

Berechne den Winkel zwischen $(1,1,1)$ und $(1,-1,-1)$. Zeige, dass sich alle vier Richtungen zu null summieren.

</li>

<li>

An einem Punkt sei $\phi_\mathrm s=0{,}5$, $\phi_x=0{,}2$, $\phi_y=0{,}1$, $\phi_z=0{,}4$. Berechne die vier Hybride und prüfe die Summenregel.

</li>

<li>

In H$_2$O ist $\beta=104{,}5^\circ$. Welches $w^2$ und welcher s-Anteil gehört zu den O–H-Bindungen? Wo steckt der Rest des s-Orbitals?

</li>

</ol>

:::loesung
(a) $\cos\beta=(1-1-1)/3=-\frac13$, also $\beta=109{,}47^\circ$. Die Summe ist $(0,0,0)$. (b) Die Hybride sind 0,6, 0,1, 0 und 0,3. Die Quadrate summieren sich zu $0{,}36+0{,}01+0+0{,}09=0{,}46$, ebenso $0{,}25+0{,}04+0{,}01+0{,}16=0{,}46$. (c) $w^2=-1/\cos\beta=3{,}99$, s-Anteil $1/(1+w^2)=20$ %. Der Rest des s-Orbitals sitzt in den freien Paaren. Dort lohnt die tiefe Energie von s, denn diese Elektronen binden nichts.
:::
:::

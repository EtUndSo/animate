---
title: Stufe 5: Inversion
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Die MOS-Kapazität
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/die-mos-kapazitat
knoten: Kapitel 15: Die MOS-Kapazität
order: 4250700
summary: Die Verarmungszone kann nicht beliebig wachsen, denn die Bänder biegen immer weiter.
tags: schwache Inversion, starker Inversion
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Die Verarmungszone kann nicht beliebig wachsen, denn die Bänder biegen immer weiter. Diese Stufe zeigt, was geschieht, wenn $E_\mathrm{Fi}$ an der Grenzfläche unter $E_\mathrm F$ sinkt.
:::

**Die Idee.** Mit steigendem $\varphi_\mathrm s$ rückt $E_\mathrm F$ an der Grenzfläche zum Leitungsband. Nach [(2.3)](wie-sich-die-gatespannung-aufteilt.html#gl-2-3) wächst $n(0)$ exponentiell, $p(0)$ fällt ebenso. Erreicht $E_\mathrm F$ dort die Bandmitte, sind beide Dichten gleich $n_\mathrm i$. Darüber überwiegen Elektronen: Die Oberfläche ist lokal n-leitend, obwohl das Substrat p-dotiert ist. Die Ladungsverhältnisse haben sich umgekehrt, daher der Name. Zunächst sind es wenige Elektronen, das ist __schwache Inversion__. Erreicht ihre Dichte an der Grenzfläche die Dichte der Löcher im Substrat, spricht man von __starker Inversion__.

Die Elektronen kommen weder aus dem Gate noch aus dem Substrat. Sie entstehen langsam durch thermische Paarbildung in der Raumladungszone: Das Feld zieht das Elektron zur Grenzfläche und schiebt das Loch ins Substrat. Viel schneller geht es, wenn ein benachbartes n-Gebiet sie seitlich nachliefert.

:::satz Satz 5.1 (Einsatz der Inversion)
<span class="anker" id="satz-5-1"></span>

Für ein p-Substrat beginnt schwache Inversion bei $n(0)=p(0)=n_\mathrm i$, starke Inversion bei $n(0)=N_\mathrm A$:

<span class="anker" id="gl-5-1"></span>
$$\varphi_\mathrm{s,WI}=V_\mathrm T\ln\frac{N_\mathrm A}{n_\mathrm i}=\frac{E_\mathrm{Fi,\infty}-E_\mathrm F}{e},\qquad\varphi_\mathrm{s,SI}=2V_\mathrm T\ln\frac{N_\mathrm A}{n_\mathrm i}=2\varphi_\mathrm{s,WI}. \tag{5.1}$$

Für ein n-Substrat gilt $\varphi_\mathrm{s,WI}=-V_\mathrm T\ln(N_\mathrm D/n_\mathrm i)$ und $\varphi_\mathrm{s,SI}=2\varphi_\mathrm{s,WI}$, starke Inversion beginnt bei $p(0)=N_\mathrm D$.
:::

:::herleitung Aus den Randdichten
$p(0)=n_\mathrm i$ in [(2.3)](wie-sich-die-gatespannung-aufteilt.html#gl-2-3) gibt $\varphi_\mathrm{s,WI}=V_\mathrm T\ln(N_\mathrm A/n_\mathrm i)$. Mit [(0.2)](von-grund-auf-was-aus-fruheren-teilen-gebraucht-wird.html#gl-0-2) ist das der Abstand von $E_\mathrm{Fi}$ und $E_\mathrm F$ im Substrat: So weit muss $E_\mathrm{Fi}$ sinken, um $E_\mathrm F$ zu erreichen. $n(0)=N_\mathrm A$ ergibt $\varphi_\mathrm s=V_\mathrm T\ln(N_\mathrm A^2/n_\mathrm i^2)$, das Doppelte. Anschaulich: $E_\mathrm{Fi}$ muss noch einmal denselben Abstand sinken, damit an der Grenzfläche $E_\mathrm F$ so hoch über $E_\mathrm{Fi}$ liegt wie im Substrat darunter.
:::

:::abbildung gemb1/k15bereiche 5
Exakt gerechnete Bandkanten des Rechenmodells bei $\varphi_\mathrm s=-0{,}15$, 0,25, 0,58 und 0,86 V, Grenzfläche bei $x=0$. Alle Teilbilder haben dieselben Achsen. Orange die Verarmungszone. Rot Löcher, blau Elektronen, nur angedeutet und in Wirklichkeit dichter an der Grenzfläche.
:::

Die Tabelle fasst die vier Bereiche und ihre drei Übergänge für das p-Substrat zusammen, $E_\mathrm{Fi}$ meint den Wert an der Grenzfläche. Beim n-Substrat gilt dieselbe Tabelle, wenn man $\varphi_\mathrm s$ und $V_\mathrm G$ das Vorzeichen gibt, $n$ und $p$ tauscht, $N_\mathrm A$ durch $N_\mathrm D$ ersetzt und die Relationen von $E_\mathrm{Fi}$ und $E_\mathrm F$ umkehrt.

| Bereich | $\varphi_\mathrm s$ | Dichten an der Grenzfläche | $E_\mathrm{Fi}$ | Bänder |
|---|---|---|---|---|
| Akkumulation | $\varphi_\mathrm s<0$ | $p(0)>N_\mathrm A$ | $>E_\mathrm F$ | nach oben |
| Flachband | $\varphi_\mathrm s=0$ | $p(0)=N_\mathrm A$ | $>E_\mathrm F$ | flach |
| Verarmung | $0<\varphi_\mathrm s<\varphi_\mathrm{s,WI}$ | $n_\mathrm i<p(0)<N_\mathrm A$ | $>E_\mathrm F$ | nach unten |
| Beginn schwache Inversion | $\varphi_\mathrm s=\varphi_\mathrm{s,WI}$ | $n(0)=p(0)=n_\mathrm i$ | $=E_\mathrm F$ | nach unten |
| schwache Inversion | $\varphi_\mathrm{s,WI}<\varphi_\mathrm s<\varphi_\mathrm{s,SI}$ | $n_\mathrm i<n(0)<N_\mathrm A$ | $<E_\mathrm F$ | nach unten |
| Beginn starke Inversion | $\varphi_\mathrm s=\varphi_\mathrm{s,SI}$ | $n(0)=N_\mathrm A$ | $<E_\mathrm F$ | nach unten |
| starke Inversion | $\varphi_\mathrm s>\varphi_\mathrm{s,SI}$ | $n(0)>N_\mathrm A$ | $<E_\mathrm F$ | nach unten |

Oberhalb von $\varphi_\mathrm{s,SI}$ ändert sich die Lage grundlegend. Schon 60 mV mehr verzehnfachen $n(0)$, die Elektronen liefern nun die Ladung, und die Verarmungszone wächst kaum noch. Ihre größte Weite ist

<span class="anker" id="gl-5-2"></span>
$$L_\mathrm{depl,max}=\sqrt{\frac{2\varepsilon\,\varphi_\mathrm{s,SI}}{eN_\mathrm A}}=\sqrt{\frac{4\varepsilon V_\mathrm T\ln(N_\mathrm A/n_\mathrm i)}{eN_\mathrm A}}. \tag{5.2}$$

::::beispiel
Im Rechenmodell ist $\varphi_\mathrm{s,WI}=0{,}389$ V, $\varphi_\mathrm{s,SI}=0{,}777$ V und $L_\mathrm{depl,max}=183$ nm. Dabei wächst $n(0)$ von $2{,}6\cdot10^{3}$ auf $3\cdot10^{16}\,\mathrm{cm^{-3}}$, um den Faktor $10^{13}$. Bei $\varphi_\mathrm{s,SI}$ liegt $E_\mathrm C$ noch 0,17 eV über $E_\mathrm F$. Bei rund 0,95 V schneidet $E_\mathrm C$ das Fermi-Niveau, und die Schicht verhält sich metallähnlich.
::::

⁠**Grenzfälle:** Für $N_\mathrm A=10^{14}$, $10^{16}$ und $10^{18}\,\mathrm{cm^{-3}}$ ist $\varphi_\mathrm{s,SI}=0{,}48$, 0,72 und 0,96 V und $L_\mathrm{depl,max}=2{,}5$ µ m, 305 nm und 35 nm. Stärkere Dotierung braucht etwas mehr Bandverbiegung, die Zone wird aber viel schmaler.

:::frage Warum spricht man erst bei $E_\mathrm{Fi}=E_\mathrm F$ von Inversion, wenn die Elektronen doch von Anfang an zunehmen?
Sie sind zunächst viel seltener als Löcher: Bei $\varphi_\mathrm s=0{,}2$ V stehen $6\cdot10^{6}$ Elektronen $1{,}3\cdot10^{13}$ Löchern gegenüber. $E_\mathrm{Fi}=E_\mathrm F$ ist genau der Ort, an dem beide Dichten gleich sind.
:::

:::aufgabe Aufgabe 5 ★★ Inversion im n-Substrat
<span class="anker" id="aufg-5"></span>

Ein n-Substrat hat $N_\mathrm D=2\cdot10^{16}\,\mathrm{cm^{-3}}$.

<ol class="al">

<li>

Berechne $\varphi_\mathrm{s,WI}$, $\varphi_\mathrm{s,SI}$ und $L_\mathrm{depl,max}$. Welche Vorzeichen haben sie, und warum?

</li>

<li>

Welche Ladungsträger bilden die Inversionsschicht? Welches Vorzeichen hat $V_\mathrm G$?

</li>

<li>

Vorhersage: Wird $|\varphi_\mathrm{s,SI}|$ bei 350 K größer oder kleiner? Prüfe mit $n_\mathrm i(350\,\mathrm{K})=2{,}5\cdot10^{11}\,\mathrm{cm^{-3}}$.

</li>

</ol>

:::loesung
(a) $\varphi_\mathrm{s,WI}=-0{,}378$ V, $\varphi_\mathrm{s,SI}=-0{,}756$ V, $L_\mathrm{depl,max}=221$ nm. Die Potentiale sind negativ, weil die Bänder beim n-Substrat nach oben biegen müssen, damit $E_\mathrm F$ an der Grenzfläche zum Valenzband rückt. (b) Löcher, und $V_\mathrm G<0$. (c) Kleiner. $n_\mathrm i$ wächst stärker als $T$: $|\varphi_\mathrm{s,SI}|=2k_\mathrm B\cdot350\,\mathrm{K}/e\cdot\ln(2\cdot10^{16}/2{,}5\cdot10^{11})=0{,}68$ V.
:::
:::

:::aufgabe Aufgabe 6 ★ Bereiche zuordnen
<span class="anker" id="aufg-6"></span>

<ol class="al">

<li>

Ein p-Substrat hat $N_\mathrm A=10^{16}\,\mathrm{cm^{-3}}$. Ordne $\varphi_\mathrm s=-0{,}05$, 0,10, 0,50 und 0,80 V je einem Bereich zu und gib $n(0)$ und $p(0)$ an.

</li>

<li>

Skizziere für ein n-Substrat die Bänder in starker Inversion. Trage $E_\mathrm C$, $E_\mathrm{Fi}$, $E_\mathrm F$ und $E_\mathrm V$ ein und markiere die Bandverbiegung und die Lage der Löcher.

</li>

</ol>

:::loesung
(a) $\varphi_\mathrm{s,WI}=0{,}360$ V, $\varphi_\mathrm{s,SI}=0{,}720$ V. $-0{,}05$ V ist Akkumulation mit $p(0)=6{,}9\cdot10^{16}$ und $n(0)=1{,}1\cdot10^{3}\,\mathrm{cm^{-3}}$. 0,10 V ist Verarmung mit $2{,}1\cdot10^{14}$ und $3{,}8\cdot10^{5}\,\mathrm{cm^{-3}}$. 0,50 V ist schwache Inversion mit $4{,}0\cdot10^{7}$ und $2{,}0\cdot10^{12}\,\mathrm{cm^{-3}}$. 0,80 V ist starke Inversion mit $3{,}6\cdot10^{2}$ und $2{,}2\cdot10^{17}\,\mathrm{cm^{-3}}$. (b) Im Substrat liegt $E_\mathrm F$ über $E_\mathrm{Fi}$. Zur Grenzfläche biegen alle Bänder nach oben, $E_\mathrm{Fi}$ schneidet $E_\mathrm F$ und liegt an der Grenzfläche mindestens so weit darüber wie im Substrat darunter. Die Bandverbiegung $|e\varphi_\mathrm s|$ misst man zwischen Substrat und Grenzfläche. $E_\mathrm V$ kommt $E_\mathrm F$ nahe, die Löcher sitzen im Valenzband direkt an der Grenzfläche.
:::
:::

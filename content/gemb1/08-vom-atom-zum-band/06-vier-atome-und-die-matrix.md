---
title: Stufe 4: Vier Atome und die Matrix
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Vom Atom zum Band
order: 4180600
summary: Zwei Atome ergaben eine Matrix mit vier Einträgen.
tags: Nächste-Nachbar-Näherung, Säkulargleichung
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Zwei Atome ergaben eine Matrix mit vier Einträgen. Diese Stufe zeigt an vier Atomen, wie jeder Eintrag entsteht und welche man streichen darf. Das Verfahren gilt dann für beliebig viele Atome.
:::

**Die Idee.** Auf dem Gitter aus [Teil 2](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/das-teilchen-in-der-box/das-teilchen-in-der-box.html) ist ein Orbital eine Liste von Zahlen, also ein Vektor, und ein Integral wird bis auf den Faktor $\Delta x$ zum Skalarprodukt: $\int\phi_{\ell'}^*\phi_\ell\,\mathrm{d} x\approx\sum_i\phi_{\ell'}^*(x_i)\,\phi_\ell(x_i)\,\Delta x$. Die Orbitale sind Basisvektoren, die $c_\ell$ die Koordinaten von $\psi$, und Projizieren heißt, Koordinaten abzulesen. So wird die Differentialgleichung eine Matrix mit so vielen Zeilen, wie es Orbitale gibt.

**Der Ansatz.** Vier Atome im Abstand $a$, je ein s-Orbital, $n$ zählt die Lösungen:

<span class="anker" id="gl-4-1"></span>
$$\hat H=-\frac{\hbar^2}{2m}\frac{\mathrm{d}^2}{\mathrm{d} x^2}+V_1+V_2+V_3+V_4,\qquad\psi_n(x)=\sum_{\ell=1}^4c_\ell^{(n)}\,\phi_\ell(x). \tag{4.1}$$

Einsetzen, Multiplikation mit $\phi_{\ell'}^*$ und Integration ergeben für jedes $\ell'=1,\dots,4$ eine Zeile von $\boldsymbol H\boldsymbol c=E\boldsymbol S\boldsymbol c$:

<span class="anker" id="gl-4-2"></span>
$$\sum_\ell c_\ell\,\langle\ell'|\hat H|\ell\rangle=E\sum_\ell c_\ell\,\langle\ell'|\ell\rangle. \tag{4.2}$$

**Welche Einträge bleiben.** Die Orbitale klingen exponentiell ab, das entscheidet alles.

<ul>

<li>

⁠**Hauptdiagonalelemente:** $\langle\ell|\hat H|\ell\rangle\approx E_\mathrm s$. Die anderen Trichter wirken kaum, denn dort ist $\phi_\ell$ klein.

</li>

<li>

⁠**Nebendiagonalelemente:** $\langle\ell|\hat H|\ell\pm1\rangle=-V_\mathrm{ss}$. Alle Nachbarpaare haben denselben Abstand.

</li>

<li>

⁠**Weiter entfernte Paare:** $\langle1|\hat H|3\rangle=\langle2|\hat H|4\rangle\approx0$ und $\langle1|\hat H|4\rangle\approx0$. Liegt $E_\mathrm s$ um 5 eV unter dem Potential zwischen den Atomen, ist $\kappa=11{,}5\,\mathrm{nm^{-1}}$. Ein Atomabstand mehr schwächt um $\mathrm{e}^{-\kappa a}=0{,}057$. Diese Einschränkung heißt __Nächste-Nachbar-Näherung__.

</li>

<li>

⁠**Überlappmatrix:** $\langle\ell|\ell\rangle=\int|\phi_\ell|^2\,\mathrm{d} x=1$ und $\langle\ell'|\ell\rangle=0$ für $\ell'\neq\ell$. Damit ist $\boldsymbol S$ die Einheitsmatrix $\mathbf1$.

</li>

</ul>

:::satz Satz 4.1 (Reguläres Eigenwertproblem)
<span class="anker" id="satz-4-1"></span>

Für vier Atome gilt

<span class="anker" id="gl-4-3"></span>
$$\boldsymbol H\boldsymbol c^{(n)}=E_n\boldsymbol c^{(n)},\qquad \boldsymbol H=\begin{pmatrix}E_\mathrm s&-V_\mathrm{ss}&0&0\\-V_\mathrm{ss}&E_\mathrm s&-V_\mathrm{ss}&0\\0&-V_\mathrm{ss}&E_\mathrm s&-V_\mathrm{ss}\\0&0&-V_\mathrm{ss}&E_\mathrm s\end{pmatrix}. \tag{4.3}$$

Die Energien folgen aus der __Säkulargleichung__ $\det|\boldsymbol H-E\mathbf1|=0$: Das charakteristische Polynom ist null.
:::

⁠**So liest man das:** „Regulär“ heißt, dass rechts nur $E$ mal Einheitsmatrix steht. Die Hauptdiagonale ist die Energie am Atom, die Nebendiagonale die Kopplung zum Nachbarn. Vier Atome mit je einem s-Orbital ergeben vier Zustände, zu jedem $n$ gehört ein Eigenvektor $(c_1^{(n)},\dots,c_4^{(n)})$.

**Die Lösung.** Mit $\xi=(E-E_\mathrm s)/V_\mathrm{ss}$ lautet das Polynom $\xi^4-3\xi^2+1=0$, also $\xi^2=(3\pm\sqrt5)/2$ und $\xi=\pm1{,}618$, $\pm0{,}618$. Dieselbe Matrix hat [Teil 2](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/das-teilchen-in-der-box/das-teilchen-in-der-box.html) für die Box auf dem Gitter gelöst, dort mit $2t_0+V_0$ und $-t_0$. Für $N$ Atome gilt also

<span class="anker" id="gl-4-4"></span>
$$E_n=E_\mathrm s-2V_\mathrm{ss}\cos\frac{n\pi}{N+1},\qquad c_\ell^{(n)}=\sqrt{\frac2{N+1}}\,\sin\frac{n\pi\ell}{N+1},\qquad n=1,\dots,N. \tag{4.4}$$

Die Koeffizienten bilden die stehende Welle einer Box der Länge $L=(N+1)a$ mit $k_n=n\pi/L$, denn das Elektron kann die Kette nicht verlassen: $c_0=c_{N+1}=0$. Die Energien liegen auf einem Kosinus (Abb. [4](#abb-4)).

:::abbildung gemb1/k8vier 4
Vier Atome mit $E_\mathrm s=-5$ eV und $V_\mathrm{ss}=0{,}5$ eV. Links: Koeffizienten $c_\ell^{(n)}$ der vier Zustände, orange die Einhüllende $\sin(n\pi\ell/5)$. Rechts: Die vier Energien liegen auf einem Kosinus bei $k=n\pi/(5a)$.
:::

**Beispiel.** Mit $E_\mathrm s=-5$ eV und $V_\mathrm{ss}=0{,}5$ eV sind die Energien $-5{,}809$, $-5{,}309$, $-4{,}691$ und $-4{,}191$ eV. Ihre Summe ist $4E_\mathrm s$, die Niveaus spalten um die Mitte auf. Gleiches Vorzeichen bei Nachbarn senkt die Energie, jeder Vorzeichenwechsel hebt sie: $n=1$ hat keinen Wechsel, $n=4$ an jedem Paar. **Kontrolle:** Vier Töpfe mit $b=0{,}4$ nm ergeben ohne Näherung 166,9, 180,2, 198,3 und 214,6 meV, [(4.4)](#gl-4-4) mit den Werten aus Stufe [3](zwei-atome.html#stufe-3) ergibt 166,4, 181,1, 199,4 und 214,2 meV. **Grenzfall:** $N=2$ ergibt mit $\cos(\pi/3)=\frac12$ wieder [(3.2)](zwei-atome.html#gl-3-2).

:::aufgabe Aufgabe 4 ★★ Drei Atome
<span class="anker" id="aufg-4"></span>

Eine Kette aus drei Atomen hat $E_\mathrm s=-5$ eV und $V_\mathrm{ss}=0{,}5$ eV.

<ol class="al">

<li>

Stelle $\boldsymbol H$ auf und berechne die Eigenwerte aus der Säkulargleichung, ohne [(4.4)](#gl-4-4) zu benutzen.

</li>

<li>

Bestimme die normierten Eigenvektoren. Welcher Zustand ist am mittleren Atom null, und warum liegt er genau bei $E_\mathrm s$?

</li>

<li>

Prüfe das Ergebnis mit [(4.4)](#gl-4-4) und mit der Summe der Eigenwerte.

</li>

</ol>

:::loesung
(a) Mit $\xi=(E-E_\mathrm s)/V_\mathrm{ss}$ ist die Determinante $-\xi(\xi^2-2)=0$, also $\xi=0,\pm\sqrt2$ und $E=-5{,}707$, $-5{,}000$, $-4{,}293$ eV. (b) $\boldsymbol c=\frac12(1,\sqrt2,1)$, $\frac1{\sqrt2}(1,0,-1)$, $\frac12(1,-\sqrt2,1)$. Der mittlere Zustand ist am mittleren Atom null. Die äußeren Atome koppeln nicht direkt, es bleibt $E_\mathrm s$. (c) $2\cos(n\pi/4)=\sqrt2$, 0, $-\sqrt2$ passt, die Summe ist $-15$ eV $=3E_\mathrm s$.
:::
:::

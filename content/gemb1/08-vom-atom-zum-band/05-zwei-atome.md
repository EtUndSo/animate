---
title: Stufe 3: Zwei Atome
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Vom Atom zum Band
order: 4180500
summary: Stufe 2 zeigte Bänder aus einer numerischen Lösung, aber kein Verfahren für Atome.
tags: LCAO
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Stufe 2 zeigte Bänder aus einer numerischen Lösung, aber kein Verfahren für Atome. Diese Stufe rechnet den kleinsten Fall aus [Teil 5](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/chemische-bindung/chemische-bindung.html) so, dass er sich auf viele Atome übertragen lässt.
:::

**Die Idee.** Das kleinste Molekül ist H$_2^+$: zwei Protonen, ein Elektron. Weit getrennt hat das Elektron bei Atom 1 und bei Atom 2 dieselbe Energie. Rücken die Atome zusammen, wird die Wand zwischen den Trichtern dünn, die Orbitale überlappen, das Elektron tunnelt hin und her. Ein Zustand fester Energie gehört dann beiden Atomen gleich. Dafür gibt es zwei Möglichkeiten: Summe und Differenz der Orbitale. Die Differenz hat in der Mitte einen Knoten, ist stärker gekrümmt und liegt höher. Die Summe ist weniger gekrümmt und hält das Elektron dort, wo beide Kerne ziehen. Aus einem Niveau werden zwei.

**Der Ansatz.** $\phi_\ell$ ist die Lösung des „Atoms“ am Platz $\ell$, also des einzelnen Coulomb-Potentials $V_\ell$, hier ein s-Orbital mit der Energie $E_\mathrm s$ (in [Teil 5](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/chemische-bindung/chemische-bindung.html) $E_\mathrm{AO}$):

<span class="anker" id="gl-3-1"></span>
$$\Bigl[-\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2}+V_\ell\Bigr]\phi_\ell=E_\mathrm s\,\phi_\ell,\qquad\ell=1,2. \tag{3.1}$$

Das Molekül hat $\hat H=-\frac{\hbar^2}{2m}\frac{\mathrm{d}^2}{\mathrm{d} x^2}+V_1+V_2$. Die beiden Orbitale fasst man als Basis eines zweidimensionalen Vektorraums auf und setzt an: $\psi=c_1\phi_1+c_2\phi_2$. Das heißt __LCAO__ (englisch linear combination of atomic orbitals).

:::satz Satz 3.1 (Aufspaltung)
<span class="anker" id="satz-3-1"></span>

Aus dem Niveau $E_\mathrm s$ werden zwei Niveaus:

<span class="anker" id="gl-3-2"></span>
$$E_\sigma=E_\mathrm s-V_\mathrm{ss},\quad\psi_\sigma=\tfrac1{\sqrt2}(\phi_1+\phi_2)\qquad\text{und}\qquad E_{\sigma^*}=E_\mathrm s+V_\mathrm{ss},\quad\psi_{\sigma^*}=\tfrac1{\sqrt2}(\phi_1-\phi_2). \tag{3.2}$$

Dabei ist $-V_\mathrm{ss}=\langle1|\hat H|2\rangle=\int\phi_1^*\,\hat H\,\phi_2\,\mathrm{d} x$ mit $V_\mathrm{ss}>0$.
:::

:::herleitung Projektion auf die Basis
Abkürzungen: $\langle\ell'|\hat H|\ell\rangle=\int\phi_{\ell'}^*\hat H\phi_\ell\,\mathrm{d} x$ und $\langle\ell'|\ell\rangle=\int\phi_{\ell'}^*\phi_\ell\,\mathrm{d} x$ (Bra-Ket-Notation, $|\ell\rangle$ steht für $\phi_\ell$). Man setzt $\psi$ in $\hat H\psi=E\psi$ ein, multipliziert mit $\phi_1^*$ und integriert, dann dasselbe mit $\phi_2^*$:

$$c_1\langle1|\hat H|1\rangle+c_2\langle1|\hat H|2\rangle=E(c_1\langle1|1\rangle+c_2\langle1|2\rangle),\quad c_1\langle2|\hat H|1\rangle+c_2\langle2|\hat H|2\rangle=E(c_1\langle2|1\rangle+c_2\langle2|2\rangle).$$

Es ist $\langle1|1\rangle=\langle2|2\rangle=1$. Näherungen: $\langle1|2\rangle\approx0$ und $\langle1|\hat H|1\rangle=\langle2|\hat H|2\rangle\approx E_\mathrm s$. Das ergibt

$$\begin{pmatrix}E_\mathrm s&-V_\mathrm{ss}\\-V_\mathrm{ss}&E_\mathrm s\end{pmatrix}\begin{pmatrix}c_1\\c_2\end{pmatrix}=E\begin{pmatrix}c_1\\c_2\end{pmatrix}.$$

Eine Lösung mit $c_1,c_2\neq0$ verlangt $(E_\mathrm s-E)^2-V_\mathrm{ss}^2=0$, also $E=E_\mathrm s\mp V_\mathrm{ss}$ mit $c_2=\pm c_1$.
:::

:::abbildung gemb1/k8doppel 3
Zwei Töpfe des Kammpotentials mit $b=0{,}4$ nm, gerechnet ohne Näherung (grau: klassisch verbotenes Gebiet). Der bindende Zustand hat in der Barriere Dichte, der antibindende dort einen Knoten. Rechts: Das Niveau bei 190,8 meV spaltet in zwei.
:::

⁠**So liest man das:** $V_\mathrm{ss}$ ist die Kopplungsenergie aus [Teil 5](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/chemische-bindung/chemische-bindung.html), eine Energie von wenigen meV bis zu einigen eV. Der Index ss sagt: s-Orbital koppelt an s-Orbital. Oft heißt auch $\langle1|\hat H|2\rangle$ selbst Überlappintegral, in dieser Reihe heißt so nur $\langle1|2\rangle$. Warum das Element negativ ist, zeigt [(3.1)](#gl-3-1): Aus $\hat H\phi_2=(E_\mathrm s+V_1)\phi_2$ folgt

<span class="anker" id="gl-3-3"></span>
$$\langle1|\hat H|2\rangle=E_\mathrm s\langle1|2\rangle+\int\phi_1^*V_1\phi_2\,\mathrm{d} x. \tag{3.3}$$

$V_1$ ist negativ, und $\phi_1\phi_2>0$. Der Mechanismus ist die Anziehung des Kerns, gewichtet mit der gemeinsamen Fläche der Orbitale. In der Mitte ist $|\psi_\sigma|^2=2\phi^2$ und $|\psi_{\sigma^*}|^2=0$. **Gültigkeit:** zwei gleiche Atome, $\langle1|2\rangle$ klein, ein Orbital je Atom.

::::beispiel
Zwei Töpfe mit $b=0{,}4$ nm haben $E_\sigma=175{,}5$ meV und $E_{\sigma^*}=205{,}0$ meV, also $V_\mathrm{ss}=14{,}8$ meV. Die Mitte 190,3 meV stimmt fast mit dem Einzeltopf überein. Das zweite Niveau spaltet in 654,1 und 774,9 meV, viermal so stark: Höhere Zustände reichen weiter in die Barriere.
::::

⁠**Grenzfall:** Für großen Abstand geht $V_\mathrm{ss}\to0$, beide Niveaus fallen auf $E_\mathrm s$ zusammen.

:::frage Warum setzt man $\langle1|2\rangle\approx0$, aber nicht $\langle1|\hat H|2\rangle\approx0$? Beide messen doch den Überlapp.
In [(3.3)](#gl-3-3) wird der Überlapp mit dem tiefen Potential $V_1$ gewichtet, und ohne Kopplung gäbe es keine Aufspaltung. $S=\langle1|2\rangle$ ändert die Zahlen nur leicht: Mit $S$ wird $E_\sigma=(E_\mathrm s-V_\mathrm{ss})/(1+S)$ und $E_{\sigma^*}=(E_\mathrm s+V_\mathrm{ss})/(1-S)$, das antibindende Niveau steigt also etwas stärker, als das bindende sinkt. Streng richtig wird $S=0$ mit leicht veränderten, orthogonalen Basisfunktionen. $V_\mathrm{ss}$ passt man dann an Messung oder genaue Rechnung an.
:::

:::aufgabe Aufgabe 3 ★ Aufspaltung ausmessen
<span class="anker" id="aufg-3"></span>

Ein Molekül aus zwei gleichen Atomen hat die Niveaus $E_\sigma=-7{,}3$ eV und $E_{\sigma^*}=-6{,}1$ eV.

<ol class="al">

<li>

Bestimme $E_\mathrm s$ und $V_\mathrm{ss}$.

</li>

<li>

Das Molekül enthält zwei Elektronen. Welche Energie gewinnt es gegenüber zwei getrennten Atomen? Was ändert sich mit vier Elektronen?

</li>

<li>

Die Kopplung fällt wie $\mathrm{e}^{-\kappa r}$ mit $\kappa=10\,\mathrm{nm^{-1}}$. Wie groß ist die Aufspaltung, wenn der Abstand um 0,1 nm wächst?

</li>

</ol>

:::loesung
(a) $E_\mathrm s=\frac12(E_{\sigma^*}+E_\sigma)=-6{,}7$ eV, $V_\mathrm{ss}=\frac12(E_{\sigma^*}-E_\sigma)=0{,}6$ eV. (b) Zwei Elektronen: $-14{,}6$ eV statt $-13{,}4$ eV, Gewinn $2V_\mathrm{ss}=1{,}2$ eV. Mit vier ist $2E_\sigma+2E_{\sigma^*}=4E_\mathrm s$: kein Gewinn. (c) Faktor $\mathrm{e}^{-1}$: $V_\mathrm{ss}=0{,}221$ eV, Aufspaltung $E_{\sigma^*}-E_\sigma=0{,}441$ eV statt 1,2 eV.
:::
:::

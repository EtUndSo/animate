---
title: Das Wichtigste
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Differentialrechnung für Vektorfelder
order: 3111000
summary: Was Ableiten heißt, wenn Eingang und Ausgang Vektoren sind
tags: 
lang: de
---

:::kern Das Wichtigste
<ul>

<li>

Jacobi-Matrix $D\boldsymbol f=(\partial f_j/\partial x_k)_{jk}$, Gradient $\nabla f=(Df)^T$. Differenzierbar heißt: $\boldsymbol f(\boldsymbol{x})-\boldsymbol f(\boldsymbol{x}_0)-D\boldsymbol f(\boldsymbol{x}_0)(\boldsymbol{x}-\boldsymbol{x}_0)$ verschwindet schneller als $|\boldsymbol{x}-\boldsymbol{x}_0|$. Stetige partielle Ableitungen reichen dafür, ihre bloße Existenz nicht.

</li>

<li>

Kettenregel: $D(\boldsymbol f\circ\boldsymbol{g})=D\boldsymbol f(\boldsymbol{g})\,D\boldsymbol{g}$. Längs einer Kurve: $\frac{\mathrm{d}}{\mathrm{d} t}u(\gamma)=\nabla u(\gamma)\cdot\dot\gamma$. Der Gradient zeigt bergauf und steht senkrecht auf den Höhenlinien.

</li>

<li>

Radial: $\nabla r=\hat{\boldsymbol{e}}_r$, $\nabla f(r)=f'(r)\,\hat{\boldsymbol{e}}_r$, $\operatorname{div}(f(r)\,\hat{\boldsymbol{e}}_r)=f'+(n-1)f/r$. Ein stetiges Zentralfeld auf $\mathbb{R}^n\setminus\{0\}$, $n\ge2$, ist genau dann ein Gradientenfeld, wenn es radialsymmetrisch ist.

</li>

<li>

$\operatorname{div}\boldsymbol{E}=\sum_j\partial E_j/\partial x_j$ misst Quellen, $\operatorname{rot}\boldsymbol{E}=\nabla\times\boldsymbol{E}$ misst Wirbel, $\Delta=\nabla\cdot\nabla$. In 2D ist $\operatorname{rot}\boldsymbol{E}=\partial_{x_1}E_2-\partial_{x_2}E_1$, und $\operatorname{div}\boldsymbol{F}=\operatorname{rot}\boldsymbol{F}^\perp$.

</li>

<li>

Integrabilität: $\boldsymbol{F}=\nabla\varphi$ erzwingt $\partial F_k/\partial x_j=\partial F_j/\partial x_k$, also $\operatorname{rot}\boldsymbol{F}=0$. Das ist notwendig, aber nicht auf jedem Gebiet hinreichend.

</li>

<li>

Produktregeln: $\operatorname{div}(\varphi\boldsymbol{E})=\nabla\varphi\cdot\boldsymbol{E}+\varphi\operatorname{div}\boldsymbol{E}$, $\operatorname{rot}(\varphi\boldsymbol{E})=\nabla\varphi\times\boldsymbol{E}+\varphi\operatorname{rot}\boldsymbol{E}$.

</li>

<li>

$\operatorname{rot}\nabla\varphi=0$, $\operatorname{div}\operatorname{rot}\boldsymbol{E}=0$, $\operatorname{rot}\operatorname{rot}\boldsymbol{E}=\nabla\operatorname{div}\boldsymbol{E}-\Delta\boldsymbol{E}$.

</li>

<li>

Potentiale sind nicht eindeutig: $\varphi+\text{konst}$, $\boldsymbol{A}+\nabla\psi$. Coulomb-Eichung: $\operatorname{div}\boldsymbol{A}=0$.

</li>

</ul>
:::

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Die Ableitung einer Abbildung ist die Matrix ihrer besten linearen Näherung, und das Hintereinanderschalten von Abbildungen wird zum Matrixprodukt.

</li>

<li>

Aus dieser Matrix liest man ab, was ein Feld tut: Ihre Diagonale ergibt die Divergenz, also die Quellen, ihr schiefsymmetrischer Anteil die Rotation, also die Wirbel.

</li>

<li>

Gradienten sind wirbelfrei und Rotationen quellenfrei, weil man zweite Ableitungen vertauschen darf. Die Umkehrungen hängen vom Gebiet ab.

</li>

</ol>
:::

**Ein Prinzip hinter allen Ergebnissen.** Fast alles in diesem Kapitel folgt aus zwei Tatsachen: Nahe einem Punkt ist eine Abbildung linear, und zweite Ableitungen lassen sich vertauschen.

| Ergebnis | Woher es kommt |
|---|---|
| $A=D\boldsymbol f$ | Schritte längs der Achsen lesen die Spalten ab (Stufe [2](differenzierbar-heit-linear-genahert.html#stufe-2)) |
| Kettenregel | Lineare Abbildungen verketten sich als Matrixprodukt (Stufe [3](die-kettenregel.html#stufe-3)) |
| Gradient zeigt bergauf | Skalarprodukt $\nabla u\cdot\boldsymbol v$ der linearen Näherung (Stufe [3](die-kettenregel.html#stufe-3)) |
| $\nabla f(r)=f'(r)\,\hat{\boldsymbol{e}}_r$ | Kettenregel mit $\nabla r=\hat{\boldsymbol{e}}_r$ (Stufe [4](radiale-funktionen-und-felder.html#stufe-4)) |
| $(n-1)f/r$ in der Divergenz | Produktregel mit $\operatorname{div}\boldsymbol{x}=n$ (Stufe [5](divergenz-und-laplace-operator.html#stufe-5)) |
| $\operatorname{div}\boldsymbol{F}=\operatorname{rot}\boldsymbol{F}^\perp$ | Drehung vertauscht die Einträge der Jacobi-Matrix (Stufe [6](rotation.html#stufe-6)) |
| $\operatorname{rot}\nabla\varphi=0$ | Lemma von Schwarz (Stufe [7](integrabilitatsbedingungen.html#stufe-7)) |
| $\operatorname{div}\operatorname{rot}\boldsymbol{E}=0$ | $\varepsilon_{ijk}$ schief, zweite Ableitung symmetrisch (Stufe [8](rechenregeln-und-vektorpotential.html#stufe-8)) |
| $\operatorname{rot}\operatorname{rot}\boldsymbol{E}=\nabla\operatorname{div}\boldsymbol{E}-\Delta\boldsymbol{E}$ | Graßmann mit dem Feld an letzter Stelle (Stufe [8](rechenregeln-und-vektorpotential.html#stufe-8)) |

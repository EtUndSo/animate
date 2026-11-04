---
title: Das Wichtigste bis hier
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Differentialrechnung für Vektorfelder
order: 3110600
summary: Was Ableiten heißt, wenn Eingang und Ausgang Vektoren sind
tags: 
lang: de
---

:::kern Das Wichtigste bis hier
<ul>

<li>

Die Jacobi-Matrix $D\boldsymbol f=(\partial f_j/\partial x_k)_{jk}$ sammelt alle ersten partiellen Ableitungen; Zeilen sind Ausgänge, Spalten Eingänge. Für eine skalare Funktion ist $\nabla f=(Df)^T$ der Gradient.

</li>

<li>

Differenzierbar heißt: $\boldsymbol f(\boldsymbol{x}_0+\boldsymbol s)=\boldsymbol f(\boldsymbol{x}_0)+D\boldsymbol f(\boldsymbol{x}_0)\,\boldsymbol s$ plus ein Fehler, der schneller verschwindet als $|\boldsymbol s|$. Stetige partielle Ableitungen reichen dafür, ihre bloße Existenz nicht. Für $C^2$-Funktionen darf man zweite Ableitungen vertauschen (Lemma von Schwarz).

</li>

<li>

Kettenregel: $D(\boldsymbol f\circ\boldsymbol{g})=D\boldsymbol f(\boldsymbol{g})\,D\boldsymbol{g}$. Längs einer Kurve: $\frac{\mathrm{d}}{\mathrm{d} t}h(\gamma)=\nabla h(\gamma)\cdot\dot\gamma$. Der Gradient zeigt in Richtung des steilsten Anstiegs und steht senkrecht auf den Höhenlinien.

</li>

<li>

Gradientenfeld: $\boldsymbol{E}=\nabla\varphi$; in der Physik $\boldsymbol{E}=-\nabla u$. Seine Jacobi-Matrix ist symmetrisch.

</li>

<li>

Radial: $\nabla r=\hat{\boldsymbol{e}}_r$, $\nabla f(r)=f'(r)\,\hat{\boldsymbol{e}}_r$, $\operatorname{div}\bigl(f(r)\,\hat{\boldsymbol{e}}_r\bigr)=f'(r)+(n-1)f(r)/r$. Ein stetiges Zentralfeld auf $\mathbb{R}^n\setminus\{0\}$, $n\ge2$, ist genau dann ein Gradientenfeld, wenn es radialsymmetrisch ist; ein Potential ist eine Stammfunktion des Profils.

</li>

<li>

$\operatorname{div}\boldsymbol{E}=\sum_j\partial E_j/\partial x_j$ misst, wie stark ein Feld an einer Stelle auseinanderströmt, $\operatorname{rot}\boldsymbol{E}=\nabla\times\boldsymbol{E}$, wie stark es dort kreist; $\Delta=\operatorname{div}\nabla$. In der Ebene ist $\operatorname{rot}\boldsymbol{E}=\partial_{x_1}E_2-\partial_{x_2}E_1$ und $\operatorname{div}\boldsymbol{F}=\operatorname{rot}\boldsymbol{F}^\perp$.

</li>

<li>

Integrabilitätsbedingungen: $\boldsymbol{F}=\nabla\varphi$ erzwingt $\partial F_k/\partial x_j=\partial F_j/\partial x_k$, in Ebene und Raum $\operatorname{rot}\boldsymbol{F}=0$. Das ist notwendig, aber nicht auf jeder Menge hinreichend.

</li>

<li>

Produktregeln: $\operatorname{div}(\varphi\boldsymbol{E})=\nabla\varphi\cdot\boldsymbol{E}+\varphi\operatorname{div}\boldsymbol{E}$, $\operatorname{rot}(\varphi\boldsymbol{E})=\nabla\varphi\times\boldsymbol{E}+\varphi\operatorname{rot}\boldsymbol{E}$, dazu die Regeln für $\boldsymbol{E}\times\boldsymbol B$.

</li>

<li>

$\operatorname{rot}\nabla\varphi=0$, $\operatorname{div}\operatorname{rot}\boldsymbol{E}=0$, $\operatorname{rot}\operatorname{rot}\boldsymbol{E}=\nabla\operatorname{div}\boldsymbol{E}-\Delta\boldsymbol{E}$.

</li>

<li>

Potentiale sind nicht eindeutig: $\varphi+\text{konst}$, $\boldsymbol{A}+\nabla\psi$. Coulomb-Eichung: $\operatorname{div}\boldsymbol{A}=0$, dann $\operatorname{rot}\boldsymbol B=-\Delta\boldsymbol{A}$.

</li>

</ul>
:::

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Die Ableitung einer Abbildung ist die Matrix ihrer besten linearen Näherung, und das Hintereinanderausführen von Abbildungen wird zum Produkt dieser Matrizen.

</li>

<li>

Aus dieser Matrix liest man ab, was ein Feld tut: Ihre Diagonale ergibt die Divergenz, also die Quellen, ihr schiefsymmetrischer Anteil die Rotation, also die Wirbel.

</li>

<li>

Gradienten sind wirbelfrei und Rotationen quellenfrei, weil man zweite Ableitungen vertauschen darf; ob die Umkehrungen gelten, hängt von der Menge ab, auf der das Feld erklärt ist.

</li>

</ol>
:::

**Ein Prinzip hinter allen Ergebnissen.** Fast alles in diesem Kapitel folgt aus zwei Tatsachen: Nahe einem Punkt verhält sich eine differenzierbare Abbildung wie ihre Jacobi-Matrix, und zweite Ableitungen lassen sich vertauschen.

| Ergebnis | Woher es kommt |
|---|---|
| $A=D\boldsymbol f$ | Schritte längs der Achsen lesen die Spalten der Näherung ab (Unterabschnitt [1.17](differenzierbarkeit-und-kettenregel-fur-abbildungen.html#stufe-1-17)) |
| Kettenregel | Lineare Näherungen hintereinander ergeben das Matrixprodukt (Unterabschnitt [1.25](differenzierbarkeit-und-kettenregel-fur-abbildungen.html#stufe-1-25)) |
| Gradient zeigt bergauf | Richtungsableitung $\nabla h\cdot\boldsymbol v=\vert \nabla h\vert \cos\alpha$ (Unterabschnitt [1.29](differenzierbarkeit-und-kettenregel-fur-abbildungen.html#stufe-1-29)) |
| $D\boldsymbol{E}$ symmetrisch für $\boldsymbol{E}=\nabla\varphi$ | Lemma von Schwarz (Unterabschnitt [1.24](differenzierbarkeit-und-kettenregel-fur-abbildungen.html#stufe-1-24)) |
| $\nabla f(r)=f'(r)\,\hat{\boldsymbol{e}}_r$ | Kettenregel mit $\nabla r=\hat{\boldsymbol{e}}_r$ (Unterabschnitt [2.5](radialsymmetrische-funktionen-und-felder.html#stufe-2-5)) |
| $(n-1)f/r$ in der Divergenz | Produktregel mit $\operatorname{div}\boldsymbol{x}=n$ (Unterabschnitt [3.10](divergenz-rotation-und-laplace-operator.html#stufe-3-10)) |
| $\operatorname{div}\boldsymbol{F}=\operatorname{rot}\boldsymbol{F}^\perp$ | Drehung vertauscht die Einträge der Jacobi-Matrix (Unterabschnitt [3.16](divergenz-rotation-und-laplace-operator.html#stufe-3-16)) |
| $\operatorname{rot}\nabla\varphi=0$ | Lemma von Schwarz (Unterabschnitt [3.18](divergenz-rotation-und-laplace-operator.html#stufe-3-18)) |
| $\operatorname{div}\operatorname{rot}\boldsymbol{E}=0$ | $\varepsilon_{ijk}$ schiefsymmetrisch, zweite Ableitung symmetrisch (Unterabschnitt [4.9](rechenregeln-und-identitaten-fur-divergenz-und-rotation.html#stufe-4-9)) |
| $\operatorname{rot}\operatorname{rot}\boldsymbol{E}=\nabla\operatorname{div}\boldsymbol{E}-\Delta\boldsymbol{E}$ | Graßmann-Identität, das Feld an letzter Stelle (Unterabschnitt [4.10](rechenregeln-und-identitaten-fur-divergenz-und-rotation.html#stufe-4-10)) |

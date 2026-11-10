---
title: Das Wichtigste
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Vektorprodukt und Basen
adresse: elektrotechnik/1-semester/hohere-mathematik-1/vektorprodukt-und-basen
knoten: Kapitel 9: Vektorprodukt und Basen
order: 1291100
summary: Warum jeder Vektor in einem Koordinatensystem genau eine Darstellung hat und wie man ein rechtwinkliges baut
tags: 
lang: de
---

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Eine Basis ist ein Koordinatensystem: Jeder Vektor hat darin genau eine Darstellung, und alle Basen eines Vektorraums sind gleich lang.

</li>

<li>

In einer Orthonormalbasis liest man die Koordinaten über das Skalarprodukt ab: $\vec x=\sum_i\langle\vec x,\vec v_i\rangle\vec v_i$. Gram-Schmidt baut sie, indem es von jedem Vektor die Projektionen auf die fertigen Richtungen abzieht.

</li>

<li>

Im $\mathbb{R}^3$ liefert $\vec u\times\vec v$ die dritte Richtung: Der Vektor steht senkrecht auf $\vec u$ und $\vec v$, sein Betrag ist die Fläche des Parallelogramms.

</li>

</ol>
:::

:::kern Das Wichtigste
<ul>

<li>

$\vec u\times\vec v=(u_2v_3-u_3v_2,\ u_3v_1-u_1v_3,\ u_1v_2-u_2v_1)$. Bilinear, $\vec u\times\vec v=-\vec v\times\vec u$, senkrecht auf $\vec u,\vec v$, $\|\vec u\times\vec v\|=\|\vec u\|\|\vec v\|\sin\alpha$, Rechtssystem. Null genau bei Abhängigkeit. Lagrange: $\|\vec u\times\vec v\|^2+\langle\vec u,\vec v\rangle^2=\|\vec u\|^2\|\vec v\|^2$. Graßmann: $\vec u\times(\vec v\times\vec w)=\langle\vec u,\vec w\rangle\vec v-\langle\vec u,\vec v\rangle\vec w$.

</li>

<li>

$\operatorname{spat}(\vec a,\vec b,\vec c)=\langle\vec a,\vec b\times\vec c\rangle$, $\operatorname{Vol}(P)=|\operatorname{spat}|$. Zyklisch vertauschbar, $>0$ bei Rechtssystem, $\ne0$ genau bei Unabhängigkeit.

</li>

<li>

ONS: $\langle\vec v_i,\vec v_j\rangle=\delta_{ij}$. $\operatorname{Proj}_U(\vec p)=\sum_i\langle\vec p,\vec v_i\rangle\vec v_i$ ist der nächste Punkt, der Rest steht senkrecht auf $U$.

</li>

<li>

Basis: jedes $\vec a$ hat genau eine Darstellung $\sum_i\alpha_i\vec b_i$. Gleichbedeutend: erzeugend und linear unabhängig. Mehr als $n$ Vektoren sind abhängig, alle Basen haben dieselbe Länge $\dim V$. Basisergänzung, Basisauswahl.

</li>

<li>

ONB: $\vec x=\sum_i\langle\vec x,\vec v_i\rangle\vec v_i$. Gram-Schmidt: $\vec d_k=\vec b_k-\sum_{i<k}\langle\vec b_k,\vec c_i\rangle\vec c_i$, $\vec c_k=\vec d_k/\|\vec d_k\|$.

</li>

<li>

Skalarproduktraum: (S1) linear im ersten Eingang, (S2) symmetrisch oder hermitesch, (S3) positiv. Polynome: $\int_{-1}^1pq\,\mathrm{d} x$. $\mathbb{C}^n$: $\sum_iu_i\overline{v_i}$.

</li>

</ul>
:::

**Ein Prinzip hinter allen Ergebnissen.** Jedes Ergebnis zerlegt einen Vektor in Anteile längs fester Richtungen. Stehen die Richtungen senkrecht, stören sie einander nicht: Das Skalarprodukt mit einer Richtung blendet alle anderen aus.

| Ergebnis | Woher es kommt |
|---|---|
| Formel für $\vec u\times\vec v$ | Ausmultiplizieren, die Einheitsvektoren geben die Tafel vor (Stufe [1](das-vektorprodukt.html#stufe-1)) |
| Betrag gleich Fläche | Die Höhe ist der Rest der Projektion, Pythagoras gibt den Rest (Stufe [1](das-vektorprodukt.html#stufe-1)) |
| Normalenvektor, Schnittgerade | Beide stehen senkrecht auf zwei bekannten Richtungen (Stufe [2](rechenregeln-und-geometrie-im-raum.html#stufe-2)) |
| Spatprodukt gleich Volumen | Die Höhe ist die Projektion auf $\vec b\times\vec c$ (Stufe [3](spatprodukt-und-volumen.html#stufe-3)) |
| Nächster Punkt eines Unterraums | Senkrechte Richtungen entkoppeln, jede Koordinate wird einzeln optimiert (Stufe [4](orthonormalsysteme-und-projektion.html#stufe-4)) |
| Eindeutige Koordinaten | Die Differenz zweier Darstellungen ist eine Nullkombination (Stufe [5](die-basis.html#stufe-5)) |
| Alle Basen gleich lang | Eine Richtung wegrechnen: ein Vektor weniger, eine Achse weniger (Stufe [6](die-dimension.html#stufe-6)) |
| Koordinaten als Skalarprodukt, Gram-Schmidt | Das Skalarprodukt blendet aus, der Rest der Projektion steht senkrecht (Stufe [7](orthonormalbasis-und-gram-schmidt.html#stufe-7)) |
| Polynome, $\mathbb{C}^n$ | Die Beweise benutzen nur die Regeln des Skalarprodukts (Stufe [8](skalarproduktraume.html#stufe-8)) |

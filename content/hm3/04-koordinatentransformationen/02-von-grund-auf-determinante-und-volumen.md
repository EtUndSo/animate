---
title: Von Grund auf: Determinante und Volumen
pfad: Elektrotechnik / 3. Semester / HöMa3 – Höhere Mathematik 3 / Koordinatentransformationen
adresse: elektrotechnik/3-semester/hohere-mathematik-3/koordinatentransformationen
knoten: Kapitel 4: Koordinatentransformationen
order: 3140200
summary: Beim Wechsel der Koordinaten taucht eine Determinante auf.
tags: Parallelotop, orientiertes Volumen
lang: de
---

:::zweck
Beim Wechsel der Koordinaten taucht eine Determinante auf. Hier steht, was sie geometrisch misst.
:::

Die Matrix $A=\begin{pmatrix}a&b\\c&d\end{pmatrix}$ bildet die Einheitsvektoren auf ihre Spalten $(a,c)$ und $(b,d)$ ab. Das Einheitsquadrat wird also zum Parallelogramm, das diese Spalten aufspannen. Dessen Fläche ist der Betrag des Kreuzprodukts $(a,c,0)\times(b,d,0)=(0,0,ad-bc)$, also $|\det A|$.

Das gilt in jeder Dimension. Das von den Spalten einer Matrix $A\in\mathbb{R}^{n\times n}$ aufgespannte schiefe Gebilde heißt __Parallelotop__: für $n=2$ ein Parallelogramm, für $n=3$ ein Spat. Die Determinante ist sein __orientiertes Volumen__: Ihr Betrag ist das Volumen, ihr Vorzeichen sagt, ob $A$ den Drehsinn erhält ($+$) oder spiegelt ($-$). Wegen $\det A=\det A^T$ gilt dasselbe für die Zeilen.

Ein Quader $Z$ ist ein gestreckter und verschobener Einheitswürfel. Weil $A$ linear ist, folgt für alle Quader

<span class="anker" id="gl-0-1"></span>
$$\operatorname{vol}(AZ)=|\det A|\,\operatorname{vol}(Z). \tag{0.1}$$

⁠**So liest man das:** Der Faktor hängt nur von $A$ ab, nicht von Lage oder Größe des Quaders. Für $A=\begin{pmatrix}2&1\\1&-1\end{pmatrix}$ ist $\det A=-3$: Jede Fläche wird dreimal so groß, und das Bild ist gespiegelt.

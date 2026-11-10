---
title: Das Wichtigste
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Matrizen und lineare Gleichungssysteme
adresse: elektrotechnik/1-semester/hohere-mathematik-1/matrizen-und-lineare-gleichungssysteme
knoten: Kapitel 10: Matrizen und lineare Gleichungssysteme
order: 1301100
summary: Eine Matrix ist eine lineare Abbildung in Zahlen, ein Gleichungssystem fragt rückwärts nach ihr
tags: 
lang: de
---

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Eine Matrix ist eine lineare Abbildung in Zahlen: Ihre $j$-te Spalte ist das Bild des $j$-ten Basisvektors, und diese Bilder legen die Abbildung überall fest.

</li>

<li>

Das Matrizenprodukt ist genau das Hintereinanderausführen. Daher kommen die Regel „Zeile mal Spalte“ und die Abhängigkeit von der Reihenfolge.

</li>

<li>

Ein Gleichungssystem $Ax=b$ fragt, welcher Vektor auf $b$ abgebildet wird. Keine Lösung gibt es, wenn $b$ nicht im Bild liegt. Liegt $b$ im Bild, gibt es genau eine Lösung, falls nur der Nullvektor im Kern liegt, und sonst unendlich viele.

</li>

</ol>
:::

:::kern Das Wichtigste
<ul>

<li>

Linear: $L(\alpha v_1+v_2)=\alpha L(v_1)+L(v_2)$. Daraus folgen $L(0)=0$ und $L(\sum_jx_jv_j)=\sum_jx_jL(v_j)$.

</li>

<li>

Die $j$-te Spalte einer Matrix ist das Bild des $j$-ten Basisvektors. In beliebigen Basen ist es sein Koordinatenvektor, und die Matrix hängt von den Basen ab.

</li>

<li>

$Ax$ ist „Zeile mal $x$“ und zugleich $\sum_jx_jA_{\bullet j}$. Produkt: $c_{kj}=\sum_ib_{ki}a_{ij}$, Format $(\ell\times m)(m\times n)=\ell\times n$, rechts steht die zuerst ausgeführte Abbildung.

</li>

<li>

$L$ injektiv $\iff\ker L=\{0\}$. Dimensionssatz: $\dim V=\dim\ker L+\dim\operatorname{im}L$.

</li>

<li>

$\mathbb K^{n\times n}$ ist nicht kommutativ, hat Nullteiler und nicht zu jedem $A\ne0$ eine Inverse.

</li>

<li>

$Ax=b$ ist lösbar $\iff b\in\operatorname{im}A\iff\operatorname{rg}(A)=\operatorname{rg}(A\,|\,b)$. Die Lösungsmenge ist $x_{\mathrm{part}}+\ker A$.

</li>

<li>

Gauß: Zeilenumformungen sind umkehrbar, also bleibt die Lösungsmenge. Die Zahl der Stufen ist $\operatorname{rg}(A)=\operatorname{Zrg}(A)=\operatorname{Srg}(A)$, die Zahl der freien Variablen ist $n-r$.

</li>

<li>

Inverse: $(A\,|\,E_n)\iff(E_n\,|\,A^{-1})$, möglich genau für $\operatorname{rg}(A)=n$.

</li>

</ul>
:::

**Ein Prinzip hinter allen Ergebnissen.** Fast alles folgt aus einer Zeile: Für eine lineare Abbildung ist $L(\sum_jx_jv_j)=\sum_jx_jL(v_j)$. Man zerlegt den Vektor nach einer Basis, und $L$ wirkt nur noch auf die Basisvektoren.

| Ergebnis | Woher es kommt |
|---|---|
| $L(0)=0$, abhängige Bilder | (L1) und (L2) reichen Linearkombinationen durch (Stufe [1](lineare-abbildungen.html#stufe-1)) |
| Matrix, Produkt mit Vektor | Zerlegen nach $e_1,\dots,e_n$, nur deren Bilder zählen (Stufe [2](die-spalten-sind-die-bilder.html#stufe-2)) |
| Dimensionssatz | Jeder Basisvektor verschwindet oder trägt zum Bild bei (Stufe [3](kern-bild-und-die-bilanz-der-dimensionen.html#stufe-3)) |
| Darstellungsmatrix | Jede Basis macht aus dem Raum einen Zahlenraum (Stufe [4](koordinaten-und-darstellungsmatrix.html#stufe-4)) |
| Matrizenprodukt | Zweimal zerlegen, einmal für jede Abbildung (Stufe [5](hintereinanderausfuhren-ist-multiplizieren.html#stufe-5)) |
| Lösungsmenge $=x_{\mathrm{part}}+\ker A$ | Zwei Lösungen unterscheiden sich um einen Kernvektor (Stufe [6](gleichungssysteme-fragen-ruckwarts.html#stufe-6)) |
| Gauß-Algorithmus | Zeilenumformungen lassen sich rückgängig machen (Stufe [7](der-gau-algorithmus.html#stufe-7)) |
| Rang, Inverse | Die Treppe zählt unabhängige Zeilen und Spalten zugleich (Stufe [8](rang-und-inverse.html#stufe-8)) |

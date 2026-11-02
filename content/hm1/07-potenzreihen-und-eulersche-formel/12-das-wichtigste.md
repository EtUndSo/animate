---
title: Das Wichtigste
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Potenzreihen und Eulersche Formel
order: 1271200
summary: Wie eine einzige Reihe Exponentialfunktion, Sinus und Cosinus enthält und warum Multiplizieren komplexer Zahlen Drehen und Strecken ist
tags: Potenzreihe, Konvergenzradius, Exponentialreihe, Cauchy-Produkt, Funktionalgleichung, Eulersche Formel, Additionstheorem, Polardarstellung
lang: de
---

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Eine __Potenzreihe__ $\sum_{n=0}^\infty a_nx^n$ (ein Polynom, das nie endet) konvergiert im Inneren eines Kreises um 0 absolut und divergiert außerhalb. Sein Radius ist der __Konvergenzradius__ $R$.

</li>

<li>

Die __Exponentialreihe__ $\exp(z)=\sum z^n/n!$ erfüllt über das __Cauchy-Produkt__ (die Multiplikationsregel für Reihen) die __Funktionalgleichung__ $\exp(z+w)=\exp(z)\exp(w)$ (Summe im Argument wird Produkt). Für $z=\mathrm{i}\varphi$ zerfällt sie in die __Eulersche Formel__ $\mathrm{e}^{\mathrm{i}\varphi}=\cos\varphi+\mathrm{i}\sin\varphi$, aus der jedes __Additionstheorem__ folgt (die Formeln für $\sin(x+y)$ und $\cos(x+y)$).

</li>

<li>

Jedes $z\ne0$ hat die __Polardarstellung__ $z=|z|\,\mathrm{e}^{\mathrm{i}\varphi}$ (Länge mal Richtung). Beim Multiplizieren multiplizieren sich die Längen, die Winkel addieren sich. Deshalb bilden die Lösungen von $z^n=a$, die __komplexen Wurzeln__, ein regelmäßiges $n$-Eck.

</li>

</ol>
:::

:::kern Das Wichtigste
<ul>

<li>

Jede Potenzreihe hat einen Radius $R$: innen absolut konvergent, außen divergent, auf dem Rand ist alles möglich. $R=1/A=1/B$, allgemein $B=\limsup\sqrt[n]{|a_n|}$. Innen ist sie stetig.

</li>

<li>

$\sin x$ und $\cos x$ sind Reihen mit $R=\infty$. Cauchy-Produkt: $c_k=\sum_{\ell=0}^ka_\ell b_{k-\ell}$, die Summe über eine Diagonale.

</li>

<li>

$\exp(z)=\sum z^n/n!$ für alle $z\in\mathbb{C}$, $\exp(z+w)=\exp(z)\exp(w)$, $|\mathrm{e}^{\mathrm{i}\varphi}|=1$, $|\mathrm{e}^z|=\mathrm{e}^{\operatorname{Re} z}$.

</li>

<li>

Euler: $\mathrm{e}^{\mathrm{i}x}=\cos x+\mathrm{i}\sin x$, daraus $\sin^2x+\cos^2x=1$ und die Additionstheoreme. $\pi/2$ ist die erste Nullstelle des Cosinus: $\mathrm{e}^{\mathrm{i}\pi/2}=\mathrm{i}$, $\mathrm{e}^{\mathrm{i}\pi}=-1$, $\mathrm{e}^{2\pi\mathrm{i}}=1$.

</li>

<li>

Polarform $z=|z|\,\mathrm{e}^{\mathrm{i}\varphi}$ mit $\cos\varphi=x/|z|$, $\sin\varphi=y/|z|$. Multiplizieren heißt: Beträge multiplizieren, Winkel addieren.

</li>

<li>

$z^n=a$ hat $n$ Lösungen $|a|^{1/n}\,\mathrm{e}^{\mathrm{i}(\alpha+2\pi k)/n}$, die Ecken eines regelmäßigen $n$-Ecks.

</li>

</ul>
:::

**Ein Prinzip hinter allen Ergebnissen.** Eine einzige Reihe enthält alles. Aus $\exp(z)=\sum z^n/n!$ kommen Sinus, Cosinus und die Zahl $\pi$, aus $\exp(z+w)=\exp(z)\exp(w)$ alle Rechenregeln.

| Ergebnis | Woher es kommt |
|---|---|
| Konvergenzkreis | Konvergenz bei $y$ gibt für kleinere $\vert x\vert $ eine geometrische Majorante (Stufe [1](der-konvergenzkreis.html#stufe-1)) |
| $R=1/A$ und $R=1/B$ | Die Glieder wachsen je Schritt um den Faktor $A\vert x\vert $ (Stufe [2](den-radius-ausrechnen.html#stufe-2)) |
| Sinus und Cosinus | Ungerade und gerade Potenzen mit wechselndem Vorzeichen (Stufe [3](sinus-und-cosinus-als-reihen.html#stufe-3)) |
| Funktionalgleichung | Cauchy-Produkt plus binomische Formel (Stufen [4](reihen-multiplizieren.html#stufe-4) und [5](die-exponentialreihe-reell-und-komplex.html#stufe-5)) |
| Eulersche Formel | Die Potenzen von $\mathrm{i}$ wiederholen sich mit Periode 4 (Stufe [6](die-eulersche-formel.html#stufe-6)) |
| Additionstheoreme | Funktionalgleichung, nach Real- und Imaginärteil sortiert (Stufe [6](die-eulersche-formel.html#stufe-6)) |
| $\pi$ und Periodizität | Erste Nullstelle des Cosinus, $\mathrm{e}^{\mathrm{i}\pi/2}=\mathrm{i}$ (Stufe [7](die-zahl-und-die-wertetabelle.html#stufe-7)) |
| Drehen und Strecken | $\mathrm{e}^{\mathrm{i}\varphi}\mathrm{e}^{\mathrm{i}\psi}=\mathrm{e}^{\mathrm{i}(\varphi+\psi)}$ (Stufe [8](polardarstellung-drehen-und-strecken.html#stufe-8)) |
| Regelmäßiges $n$-Eck | $\exp$ hat die Periode $2\pi\mathrm{i}$ (Stufe [9](die-ten-wurzeln.html#stufe-9)) |

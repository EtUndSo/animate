---
title: Das Wichtigste
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Vektoren und Skalarprodukt
order: 1281100
summary: Warum Pfeile, Zahlenspalten und Polynome denselben Regeln folgen und wie Länge und Winkel dazukommen
tags: 
lang: de
---

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Ein Vektorraum ist eine Menge mit Addition und Streckung, die wenige Axiome erfüllen. Jede Folgerung aus den Axiomen gilt deshalb für Pfeile, Zahlenspalten und Polynome zugleich.

</li>

<li>

Vektoren sind linear unabhängig, wenn sich keiner aus den anderen bauen lässt. Gleichbedeutend: Nur die Linearkombination mit lauter Nullen ergibt den Nullvektor.

</li>

<li>

Das Skalarprodukt $\langle\vec x,\vec y\rangle=\sum_ix_iy_i$ bringt Länge, Winkel und „senkrecht“. Zerlegt man einen Vektor in einen parallelen Teil und einen senkrechten Rest, liefert der Rest den kürzesten Abstand, und aus $\|\text{Rest}\|^2\ge0$ folgt die Cauchy-Schwarz-Ungleichung.

</li>

</ol>
:::

:::kern Das Wichtigste
<ul>

<li>

Vektorraum: kommutative Gruppe $(V,+)$ mit Streckung, (V2) bis (V4). Beispiele: $\mathbb{R}^n$, $\mathbb{C}^n$, Funktionen, Polynome.

</li>

<li>

Gerade $\vec p+t\vec v$, Strecke $\vec p+t(\vec q-\vec p)$ mit $t\in[0,1]$, Ebene $\vec p+s\vec u+t\vec v$. Unterraum: enthält $\vec0$, abgeschlossen unter $+$ und $\alpha\cdot$. $\operatorname{span}$ ist immer einer.

</li>

<li>

Linear unabhängig: $\sum_i\alpha_i\vec a_i=\vec0\Rightarrow$ alle $\alpha_i=0$. Gleichbedeutend: Keiner ist Linearkombination der übrigen.

</li>

<li>

$\langle\vec x,\vec y\rangle=\sum_ix_iy_i$, $\|\vec x\|=\sqrt{\langle\vec x,\vec x\rangle}$, $d(\vec x,\vec y)=\|\vec x-\vec y\|$, $\|\vec x\pm\vec z\|^2=\|\vec x\|^2\pm2\langle\vec x,\vec z\rangle+\|\vec z\|^2$.

</li>

<li>

$\operatorname{Proj}_{\vec v}(\vec q)=\frac{\langle\vec q,\vec v\rangle}{\|\vec v\|^2}\vec v$, der Rest steht senkrecht auf $\vec v$. Der Abstand zur Geraden ist die Länge des Rests.

</li>

<li>

$|\langle\vec x,\vec y\rangle|\le\|\vec x\|\,\|\vec y\|$, Gleichheit genau bei linearer Abhängigkeit. Winkel: $\cos\phi=\frac{\langle\vec x,\vec y\rangle}{\|\vec x\|\,\|\vec y\|}$. Parallelogramm: $\|\vec x+\vec y\|^2+\|\vec x-\vec y\|^2=2\|\vec x\|^2+2\|\vec y\|^2$.

</li>

<li>

Hessesche Normalform $\langle\vec u,\vec n\rangle=\beta$ mit $\|\vec n\|=1$, $\beta\ge0$. Lotfußpunkt $\vec q=\vec p+(\beta-\langle\vec p,\vec n\rangle)\vec n$, Abstand $|\beta-\langle\vec p,\vec n\rangle|$, Winkel zur Geraden $\sin\gamma=\frac{|\langle\vec n,\vec v\rangle|}{\|\vec n\|\,\|\vec v\|}$.

</li>

</ul>
:::

**Ein Prinzip hinter allen Ergebnissen.** Die ersten vier Stufen benutzen nur zwei Dinge: addieren und strecken. Die letzten vier benutzen zusätzlich nur, dass $\langle\cdot,\cdot\rangle$ in jedem Eingang linear ist und dass Quadrate nicht negativ sind.

| Ergebnis | Woher es kommt |
|---|---|
| $\vec a+\vec b$, $\alpha\vec a$, Gerade | Beides wirkt Stelle für Stelle (Stufe [1](pfeile-addieren-und-strecken.html#stufe-1)) |
| $0\cdot\vec u=\vec0$, Regeln für Polynome | Allein die Axiome, keine Koordinaten (Stufe [2](der-vektorraum.html#stufe-2)) |
| Unterraum, Aufspann | Addieren und Strecken führen nicht heraus (Stufe [3](unterraum-und-linearkombination.html#stufe-3)) |
| Lineare Unabhängigkeit, Ebene | Nullkombination nach einem Vektor auflösen (Stufe [4](lineare-unabhangigkeit.html#stufe-4)) |
| Norm, Abstand, Pythagoras | Ausmultiplizieren von $\langle\vec x+\vec y,\vec x+\vec y\rangle$ (Stufe [5](skalarprodukt-norm-abstand.html#stufe-5)) |
| Projektion, Abstand Punkt zu Gerade | Der Rest soll senkrecht stehen (Stufe [6](projektion-und-abstand-zur-geraden.html#stufe-6)) |
| Cauchy-Schwarz, Winkel, Parallelogramm | Die Länge des Rests ist nicht negativ (Stufe [7](winkel-cauchy-schwarz-parallelogramm.html#stufe-7)) |
| Hyperebene, Lotfußpunkt | Senkrecht auf einer einzigen Richtung (Stufe [8](kugel-hyperebene-drei-geometrische-probleme.html#stufe-8)) |

---
title: Überblick: Vektorprodukt und Basen
kurz: Überblick
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Vektorprodukt und Basen
adresse: elektrotechnik/1-semester/hohere-mathematik-1/vektorprodukt-und-basen
knoten: Kapitel 9: Vektorprodukt und Basen
order: 1290100
summary: Warum jeder Vektor in einem Koordinatensystem genau eine Darstellung hat und wie man ein rechtwinkliges baut
tags: Vektorprodukt, Spatprodukt, Orthonormalsystem, Orthogonalprojektion, Basis, Dimension, Orthonormalbasis, Gram-Schmidt-Verfahren
lang: de
---

## Worum es geht

Der Punkt $(5,0)$ lässt sich in Kästchen abzählen. Mit den schiefen Richtungen $\vec a=(3,1)$ und $\vec b=(1,2)$ heißt derselbe Punkt $2\vec a-\vec b$. Die Frage lautet: *Was macht eine Liste von Vektoren zu einem Koordinatensystem, warum haben alle Koordinatensysteme eines Raums gleich viele Achsen, und wie baut man ein rechtwinkliges?*

Die Antwort führt über acht Begriffe. Das __Vektorprodukt__ macht aus zwei Vektoren des $\mathbb{R}^3$ einen dritten, der auf beiden senkrecht steht. Das __Spatprodukt__ misst damit das Volumen eines schiefen Quaders. Ein __Orthonormalsystem__ besteht aus Vektoren der Länge 1, die paarweise senkrecht stehen. Mit ihm liefert die __Orthogonalprojektion__ den nächsten Punkt eines Unterraums: Man fällt das Lot. Eine __Basis__ ist ein Koordinatensystem: eine geordnete Liste von Vektoren, aus denen sich jeder Vektor auf genau eine Weise bauen lässt. Die __Dimension__ ist ihre Länge. Eine __Orthonormalbasis__ ist eine Basis aus senkrechten Einheitsvektoren, und das __Gram-Schmidt-Verfahren__ baut sie aus einer beliebigen Basis.



**So arbeitest du mit diesem Kapitel.** Die Abschnitte bauen aufeinander auf, jeder neue Begriff hat einen eigenen Unterabschnitt mit Beispiel. Kästen zum Aufklappen enthalten Hintergrund (warum etwas so ist und woher es kommt), Herleitungen und Hinweise zur Simulation; zum Weiterlesen braucht man sie nicht. Versuche die Aufgaben (★ bis ★★★) zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf.

:::merke Das Rechenmodell für dieses Kapitel
<ul>

<li>

⁠**Zwei Vektoren im Raum ([Kapitel 8](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/vektoren-und-skalarprodukt/vektoren-und-skalarprodukt.html)):** $\vec u=(2,1,0)$, $\vec v=(0,1,2)$ mit $\vec u\times\vec v=(2,-4,2)$. Ihr Parallelogramm hat die Fläche $\sqrt{24}=4{,}899$. Die dritte Kante $\vec k=(1,0,2)$ ergibt einen schiefen Quader mit Volumen 6.

</li>

<li>

⁠**Eine rechtwinklige Basis:** $\vec f_1=\frac13(1,2,-2)$, $\vec f_2=\frac13(-2,2,1)$, $\vec f_3=\frac13(2,1,2)$. Der Vektor $\vec x=(5,1,-1)$ hat darin die Koordinaten $3,-3,3$.

</li>

<li>

⁠**Eine schiefe Basis der Ebene ([Kapitel 8](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/vektoren-und-skalarprodukt/vektoren-und-skalarprodukt.html)):** $\vec a=(3,1)$, $\vec b=(1,2)$. Der Vektor $(5,0)=2\vec a-\vec b$ hat darin die Koordinaten $2,-1$.

</li>

<li>

⁠**Polynome:** $1,x,x^2$ auf $[-1,1]$ mit $\langle p,q\rangle=\int_{-1}^1p(x)q(x)\,\mathrm{d} x$.

</li>

</ul>

Alle Zahlen rechnet `rechnung_kap9.py` nach.
:::

---
title: Überblick: Differentialrechnung für Vektorfelder
kurz: Überblick
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Differentialrechnung für Vektorfelder
order: 3110100
summary: Was Ableiten heißt, wenn Eingang und Ausgang Vektoren sind
tags: Vektorfeld, Jacobi-Matrix, Gradient, Skalarpotential, Divergenz, Rotation, Laplace-Operator, Vektorpotential
lang: de
---

## Worum es geht

Eine Funktion einer Variablen hat eine Ableitung, und das ist eine einzige Zahl: So stark ändert sich der Ausgang, wenn sich der Eingang ändert. Ein elektrisches Feld oder eine Luftströmung ordnet dagegen jedem Punkt des Raums einen Pfeil zu. Drei Zahlen gehen hinein, drei kommen heraus, und jede Ausgangszahl kann von jeder Eingangszahl abhängen. Die Frage dieses Kapitels lautet: *Was heißt Ableiten, wenn Eingang und Ausgang Vektoren sind, und was verrät die Ableitung über ein Feld?* Der Nutzen: Man sieht einem Feld an, ob es aus einer Quelle strömt, ob es wirbelt und ob es aus einem Potential stammt. Alle Feldgleichungen der Elektrotechnik sind in dieser Sprache geschrieben.

Der Weg führt über acht Begriffe. Ein __Vektorfeld__ ordnet jedem Punkt einen Vektor zu. Die __Jacobi-Matrix__ sammelt alle ersten Ableitungen einer Abbildung. Der __Gradient__ ist der Vektor der ersten Ableitungen einer Zahlenfunktion. Das __Skalarpotential__ eines Felds ist eine Zahlenfunktion, deren Gradient dieses Feld ist. Die __Divergenz__ misst, wie stark ein Feld an einer Stelle auseinanderströmt, die __Rotation__, wie stark es dort wirbelt. Der __Laplace-Operator__ ist eine Summe zweiter Ableitungen. Das __Vektorpotential__ eines Felds ist ein Vektorfeld, dessen Rotation dieses Feld ist.

**So arbeitest du mit diesem Kapitel.** Jede Stufe ist ein eigener kurzer Artikel mit der Idee, typischen Fragen zum Aufklappen und Aufgaben (★ bis ★★★). Versuche die Aufgaben zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf. Schließe eine Stufe ab, bevor du zur nächsten gehst.

:::merke Die Rechenmodelle für dieses Kapitel
<ul>

<li>

⁠**Abbildung** $\boldsymbol f(x,y)=(x^2-y^2,\;2xy)$ von $\mathbb{R}^2$ nach $\mathbb{R}^2$, betrachtet im Punkt $(1,\tfrac12)$.

</li>

<li>

⁠**Schale** $\varphi(x,y)=x^2+2y^2$: eine Zahl je Punkt. Die Höhenlinien sind Ellipsen um den Nullpunkt.

</li>

<li>

⁠**Drehfeld** $(x,y)\mapsto(-y,\,x)$: Die Pfeile kreisen gegen den Uhrzeigersinn um den Nullpunkt.

</li>

<li>

⁠**Strahlfeld** $\boldsymbol{x}\mapsto\boldsymbol{x}$: Die Pfeile zeigen vom Nullpunkt weg.

</li>

</ul>

Vorausgesetzt werden partielle Ableitungen, Grenzwerte in mehreren Variablen, Matrizen, Determinanten, Skalar- und Kreuzprodukt. Vektoren sind fett gesetzt, $|\boldsymbol{x}|$ ist die euklidische Länge. In $\mathbb{R}^2$ und $\mathbb{R}^3$ steht $(x,y)$ und $(x,y,z)$ für $(x_1,x_2)$ und $(x_1,x_2,x_3)$.
:::

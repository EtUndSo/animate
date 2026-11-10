---
title: Von Grund auf: Abstand, Schranken, zwei Ungleichungen
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Folgen und Grenzwerte
adresse: elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte
knoten: Kapitel 4: Folgen und Grenzwerte
order: 1240200
summary: Was „beliebig nah“ heißt und warum die reellen Zahlen keine Lücke haben dürfen
tags: Abstand, Abstandsregel, Supremum, Infimum, Vollständigkeitsaxiom
lang: de
---

Es gilt $\mathbb{N}=\{1,2,3,\dots\}$ und $\mathbb{N}_0=\mathbb{N}\cup\{0\}$. Das Zeichen $\forall$ heißt „für alle“, $\exists$ heißt „es gibt“ ([Kapitel 1](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html)). Aus [Kapitel 1](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html) werden vier Werkzeuge gebraucht.

⁠**Betrag als Abstand.** $|x|$ ist $x$ für $x\ge0$ und $-x$ für $x<0$. Die Zahl $|x-y|$ ist der __Abstand__ von $x$ und $y$ auf der Zahlengeraden. Addiert man $a$ zu $-\varepsilon<x-a<\varepsilon$, folgt die __Abstandsregel__

$$|x-a|<\varepsilon\quad\iff\quad a-\varepsilon<x<a+\varepsilon.$$

Die Zahl $x$ liegt dann im offenen Intervall $(a-\varepsilon,a+\varepsilon)$, zwischen den beiden Grenzen, aber nicht auf ihnen.

⁠**Dreiecksungleichung.** $|x+y|\le|x|+|y|$. Für Abstände heißt das: Ein Umweg über $z$ ist nie kürzer, $|x-y|\le|x-z|+|z-y|$. Die untere Form lautet $\bigl||x|-|y|\bigr|\le|x-y|$.

⁠**Schranken.** Das __Supremum__ $\sup M$ ist die kleinste obere Schranke einer Menge $M$, das __Infimum__ $\inf M$ die größte untere. Das __Vollständigkeitsaxiom__ fordert: Jede nach unten beschränkte, nicht leere Teilmenge von $\mathbb{R}$ hat ein Infimum in $\mathbb{R}$, entsprechend hat jede nach oben beschränkte ein Supremum. Ist $y<\sup M$, gibt es ein $x\in M$ mit $y<x\le\sup M$, sonst wäre $y$ eine kleinere obere Schranke.

⁠**Bernoulli-Ungleichung.** $(1+x)^n\ge1+nx$ für $x>-1$ und $n\in\mathbb{N}$; für $n\ge2$ und $x\ne0$ gilt sogar $>$.

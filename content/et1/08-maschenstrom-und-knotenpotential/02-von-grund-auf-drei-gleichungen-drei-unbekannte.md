---
title: Von Grund auf: Drei Gleichungen, drei Unbekannte
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Maschenstrom- und Knotenpotentialverfahren
order: 1180200
summary: Warum ein Netz mit wenigen Unbekannten auskommt
tags: symmetrisch, Leitwert
lang: de
---

Beide Verfahren enden bei einem linearen Gleichungssystem $\mathbf M\,\mathbf x=\mathbf b$, also einer Matrix mal einem Spaltenvektor ([Teil 6](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore/zweitore.html)). $\mathbf x$ enthält die Unbekannten, $\mathbf b$ die bekannte rechte Seite. Jede Zeile der Matrix ist eine Gleichung, jede Spalte gehört zu einer Unbekannten. Für zwei Unbekannte ist die Determinante $\det\mathbf M=a\,d-b\,c$ bekannt. Für drei Unbekannte geht man die erste Zeile durch. Jede Zahl wird mit der Determinante multipliziert, die nach Streichen ihrer Zeile und Spalte übrig bleibt, und die Vorzeichen wechseln ($+,-,+$):

<span class="anker" id="gl-0-1"></span>
$$\det\begin{pmatrix}a&b&c\\d&e&f\\p&q&r\end{pmatrix}=a\,(e\,r-f\,q)-b\,(d\,r-f\,p)+c\,(d\,q-e\,p). \tag{0.1}$$

:::satz Satz 0.1 (Cramersche Regel)
<span class="anker" id="satz-0-1"></span>

Ist $D=\det\mathbf M\neq0$, hat $\mathbf M\,\mathbf x=\mathbf b$ genau eine Lösung. Ihre $i$-te Komponente ist

<span class="anker" id="gl-0-2"></span>
$$x_i=\frac{D_i}{D}. \tag{0.2}$$

$D_i$ ist die Determinante der Matrix, in der die Spalte $i$ durch $\mathbf b$ ersetzt wurde.
:::

:::herleitung Cramer bei zwei Unbekannten
Aus $a\,x+b\,y=e$ und $c\,x+d\,y=f$ entsteht $y$-frei: $d$ mal die erste minus $b$ mal die zweite Gleichung ergibt $(a\,d-b\,c)\,x=e\,d-b\,f$. Links steht $D\,x$, rechts die Determinante mit $(e,f)$ in Spalte 1. Bei mehr Unbekannten läuft es gleich.
:::

Beispiel: $2x+y=5$ und $x+3y=5$ haben $D=5$, $D_1=10$, $D_2=5$, also $x=2$, $y=1$. Die Regel eignet sich für die Handrechnung bis etwa vier Unbekannte, besonders wenn die Matrix viele Nullen enthält. Eine Matrix heißt __symmetrisch__, wenn sie sich beim Spiegeln an der Hauptdiagonale (von links oben nach rechts unten) nicht ändert. Der __Leitwert__ $G=1/R$ ([Teil 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)) hat die Einheit Siemens: $1\,\mathrm{mS}=1/\mathrm{k\Omega}$.

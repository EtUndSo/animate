---
title: Stufe 1: Die Jacobi-Matrix
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Differentialrechnung für Vektorfelder
order: 3110200
summary: Eine Abbildung mit n Eingängen und m Ausgängen hat mcdot n erste partielle Ableitungen.
tags: offenen Menge, skalare Funktion, Vektorfeld, Jacobi-Matrix, Gradient, Nabla-Symbol, Differentialoperator, erster Ordnung
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Eine Abbildung mit $n$ Eingängen und $m$ Ausgängen hat $m\cdot n$ erste partielle Ableitungen. Diese Stufe ordnet sie in einer Matrix an und zeigt, was Zeilen und Spalten bedeuten.
:::

**Die Idee.** Bei einer Funktion einer Variablen ist die Ableitung ein Verstärkungsfaktor: Ein kleiner Schritt $s$ am Eingang ändert den Ausgang um etwa $f'(x)\,s$. Geht ein Vektor hinein und kommt ein Vektor heraus, reicht ein Faktor nicht mehr. Es braucht eine Matrix, denn sie macht aus einem Vektor einen Vektor. Ihre Einträge liegen fest: Ändert man nur $x_k$ um $s_k$, ändert sich der Ausgang $f_j$ um etwa $\frac{\partial f_j}{\partial x_k}s_k$. Spalte $k$ sagt also, was ein Schritt in Richtung $x_k$ bewirkt, Zeile $j$, wovon der Ausgang $f_j$ abhängt (Abb. [1](#abb-1)).

:::abbildung hm3/k1jacobi 1
Die Abbildung $\boldsymbol f(x,y)=(x^2-y^2,\,2xy)$ biegt ein kleines Quadrat um $(1,\tfrac12)$. Die Spalten der Jacobi-Matrix, mit der Schrittlänge multipliziert, sind die Pfeile rechts. Sie spannen das gestrichelte Parallelogramm auf, die lineare Näherung des Bilds.
:::

**Abbildungen und Felder.** Betrachtet werden Abbildungen $\boldsymbol f=(f_1,\dots,f_m):\mathcal U\to\mathbb{R}^m$ auf einer __offenen Menge__ $\mathcal U\subset\mathbb{R}^n$. Offen heißt: Um jeden Punkt von $\mathcal U$ liegt noch eine kleine Kugel ganz in $\mathcal U$. Man kann also von jedem Punkt aus in alle Richtungen ein Stück gehen, und das braucht man zum Ableiten. Für $m=1$ heißt $f$ eine __skalare Funktion__. Für $m=n$ heißt die Abbildung ein __Vektorfeld__, geschrieben $\boldsymbol{E}=(E_1,\dots,E_n)$: In jedem Punkt $\boldsymbol{x}$ ist der Pfeil $\boldsymbol{E}(\boldsymbol{x})$ angeheftet.

:::definition Definition 1.1 (Jacobi-Matrix und Gradient)
<span class="anker" id="satz-1-1"></span>

Für eine partiell differenzierbare Abbildung $\boldsymbol f$ heißt

<span class="anker" id="gl-1-1"></span>
$$D\boldsymbol f=\Bigl(\frac{\partial f_j}{\partial x_k}\Bigr)_{jk}=\begin{pmatrix}\frac{\partial f_1}{\partial x_1}&\cdots&\frac{\partial f_1}{\partial x_n}\\\vdots&\ddots&\vdots\\\frac{\partial f_m}{\partial x_1}&\cdots&\frac{\partial f_m}{\partial x_n}\end{pmatrix}\in\mathbb{R}^{m\times n} \tag{1.1}$$

die __Jacobi-Matrix__ von $\boldsymbol f$. Für eine skalare Funktion $f$ heißt der Spaltenvektor

<span class="anker" id="gl-1-2"></span>
$$\nabla f:=\operatorname{grad}f=\Bigl(\frac{\partial f}{\partial x_1},\dots,\frac{\partial f}{\partial x_n}\Bigr)^T\in\mathbb{R}^n \tag{1.2}$$

der __Gradient__ von $f$.
:::

⁠**So liest man das:** $j$ zählt die Ausgänge, also die Zeilen, $k$ die Eingänge, also die Spalten. Das Zeichen $\nabla=(\partial/\partial x_1,\dots,\partial/\partial x_n)^T$ heißt __Nabla-Symbol__. Es hat die Form eines Spaltenvektors, seine Einträge sind aber Ableitungsbefehle: Für sich allein hat es keinen Wert. Für eine skalare Funktion ist $Df$ ein Zeilenvektor aus $\mathbb{R}^{1\times n}$, und es gilt $\nabla f=(Df)^T$. Deshalb ist Zeile $j$ der Jacobi-Matrix der transponierte Gradient der Komponente $f_j$.

Eine Vorschrift, die aus einer Funktion durch Ableiten eine neue macht, heißt __Differentialoperator__. Der Gradient enthält nur erste Ableitungen, er ist ein Differentialoperator __erster Ordnung__. Er macht aus einer skalaren Funktion ein Vektorfeld.

**Beispiel.** Für die Abbildung aus dem Rechenmodell ist $\partial f_2/\partial x=2y$ der Eintrag in Zeile 2, Spalte 1:

$$D\boldsymbol f(x,y)=\begin{pmatrix}2x&-2y\\2y&2x\end{pmatrix},\qquad D\boldsymbol f(1,\tfrac12)=\begin{pmatrix}2&-1\\1&2\end{pmatrix}.$$

Der Schritt $\boldsymbol s=(\tfrac1{10},0)$ von $(1,\tfrac12)$ aus sollte den Ausgang um $D\boldsymbol f\,\boldsymbol s=(\tfrac15,\tfrac1{10})$ ändern. Exakt ist die Änderung $\boldsymbol f(\tfrac{11}{10},\tfrac12)-\boldsymbol f(1,\tfrac12)=(\tfrac{21}{100},\tfrac1{10})$. Für die Schale ist $\nabla\varphi(x,y)=(2x,\,4y)^T$. **Grenzfall:** Für $n=m=1$ ist $Df=(f')$ eine $1\times1$-Matrix, die gewöhnliche Ableitung.

:::frage Warum unterscheidet man Zeile und Spalte? Es sind doch dieselben Zahlen.
Sie haben verschiedene Aufgaben. Die Zeile $Df$ wirkt als Matrix: $Df\,\boldsymbol s$ ist die Änderung von $f$ beim Schritt $\boldsymbol s$, also eine Zahl. Die Spalte $\nabla f$ ist ein Vektor im Eingangsraum, den man als Pfeil zeichnen kann. Beides hängt über das Skalarprodukt zusammen: $Df\,\boldsymbol s=\nabla f\cdot\boldsymbol s$.
:::

:::aufgabe Aufgabe 1 ★ Matrix aufstellen
<span class="anker" id="aufg-1"></span>

Sei $\boldsymbol f(x,y,z)=(xy^2,\;x+\mathrm{e}^{z})$.

<ol class="al">

<li>

Welches Format hat $D\boldsymbol f$? Berechne $D\boldsymbol f(1,2,0)$ und den Gradienten der zweiten Komponente.

</li>

<li>

Sage mit der Matrix die Änderung von $\boldsymbol f$ beim Schritt $\boldsymbol s=(\tfrac1{10},0,-\tfrac1{10})$ voraus und vergleiche mit der exakten Änderung.

</li>

</ol>

:::loesung
(a) Das Format ist $2\times3$: zwei Ausgänge, drei Eingänge.

$$D\boldsymbol f=\begin{pmatrix}y^2&2xy&0\\1&0&\mathrm{e}^z\end{pmatrix},\qquad D\boldsymbol f(1,2,0)=\begin{pmatrix}4&4&0\\1&0&1\end{pmatrix},\qquad\nabla f_2=(1,0,\mathrm{e}^z)^T.$$

(b) $D\boldsymbol f\,\boldsymbol s=(\tfrac25,\;\tfrac1{10}-\tfrac1{10})=(\tfrac25,\,0)$. Exakt ist $\boldsymbol f(\tfrac{11}{10},2,-\tfrac1{10})-\boldsymbol f(1,2,0)=(\tfrac25,\;\tfrac1{10}+\mathrm{e}^{-1/10}-1)\approx(0{,}4;\;0{,}0048)$. Die zweite Komponente ist fast null, wie vorhergesagt.
:::
:::

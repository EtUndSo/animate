---
title: Stufe 6: Rotation
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Differentialrechnung für Vektorfelder
order: 3110700
summary: Die Divergenz benutzt nur die Diagonale der Jacobi-Matrix.
tags: Rotation, Wirbeldichte, Levi-Civita-Symbolen
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Die Divergenz benutzt nur die Diagonale der Jacobi-Matrix. Die Einträge daneben tragen eine andere Information: Sie sagen, ob ein Feld wirbelt.
:::

**Die Idee.** Sieh dir ein kleines Quadrat in der $x_1$-$x_2$-Ebene an. Ist $F_2$ an der rechten Kante größer als an der linken, zieht das Feld das Quadrat gegen den Uhrzeigersinn herum. Dasselbe bewirkt ein $F_1$, das an der oberen Kante kleiner ist als an der unteren. Die Drehneigung um die $x_3$-Achse ist also $\partial F_2/\partial x_1-\partial F_1/\partial x_2$. Für die anderen beiden Achsen gilt dasselbe.

:::definition Definition 6.1 (Rotation im Raum)
<span class="anker" id="satz-6-1"></span>

Sei $\mathcal U\subset\mathbb{R}^3$ offen und $\boldsymbol{E}=(E_1,E_2,E_3)$ ein differenzierbares Vektorfeld. Die __Rotation__ von $\boldsymbol{E}$, englisch curl, ist

<span class="anker" id="gl-6-1"></span>
$$\operatorname{rot}\boldsymbol{E}:=\nabla\times\boldsymbol{E}=\begin{pmatrix}\partial E_3/\partial x_2-\partial E_2/\partial x_3\\\partial E_1/\partial x_3-\partial E_3/\partial x_1\\\partial E_2/\partial x_1-\partial E_1/\partial x_2\end{pmatrix}. \tag{6.1}$$
:::

⁠**So liest man das:** Aus einem Vektorfeld wird wieder ein Vektorfeld. Die Komponenten sind ein Maß für die lokale __Wirbeldichte__ um die jeweilige Koordinatenachse. Als Merkregel dient die Determinante, formal nach der ersten Spalte entwickelt:

<span class="anker" id="gl-6-2"></span>
$$\operatorname{rot}\boldsymbol{F}=\det\begin{pmatrix}\hat{\boldsymbol{e}}_1&\partial/\partial x_1&F_1\\\hat{\boldsymbol{e}}_2&\partial/\partial x_2&F_2\\\hat{\boldsymbol{e}}_3&\partial/\partial x_3&F_3\end{pmatrix}. \tag{6.2}$$

**Levi-Civita-Symbole.** Kompakter geht es mit den __Levi-Civita-Symbolen__ $\varepsilon_{ijk}=\hat{\boldsymbol{e}}_i\cdot(\hat{\boldsymbol{e}}_j\times\hat{\boldsymbol{e}}_k)\in\{-1,0,1\}$, wobei $\hat{\boldsymbol{e}}_1,\hat{\boldsymbol{e}}_2,\hat{\boldsymbol{e}}_3$ die Einheitsvektoren der Achsen sind. Es ist $\varepsilon_{123}=1$, zyklisches Vertauschen ändert nichts, das Vertauschen zweier Indizes wechselt das Vorzeichen, ein doppelter Index gibt 0. Damit gilt

<span class="anker" id="gl-6-3"></span>
$$(\operatorname{rot}\boldsymbol{F})_i=\sum_{j,k=1}^3\varepsilon_{ijk}\,\frac{\partial F_k}{\partial x_j}. \tag{6.3}$$

Für $i=1$ bleiben nur $(j,k)=(2,3)$ mit $+1$ und $(3,2)$ mit $-1$. Das ist die erste Zeile von [(6.1)](#gl-6-1).

**Rotation in der Ebene.** Für ein Feld $\boldsymbol{E}=(E_1,E_2,0)$, das nicht von $x_3$ abhängt, bleibt von [(6.1)](#gl-6-1) nur die dritte Zeile: $\operatorname{rot}\boldsymbol{E}=(0,0,\,\partial E_2/\partial x_1-\partial E_1/\partial x_2)^T$. Das legt fest:

:::definition Definition 6.2 (Rotation in 2D)
<span class="anker" id="satz-6-2"></span>

Für ein differenzierbares Vektorfeld $\boldsymbol{E}=(E_1,E_2)$ auf $\mathcal U\subset\mathbb{R}^2$ ist

<span class="anker" id="gl-6-4"></span>
$$\operatorname{rot}\boldsymbol{E}=\frac{\partial E_2}{\partial x_1}-\frac{\partial E_1}{\partial x_2}. \tag{6.4}$$
:::

In der Ebene ist die Rotation also eine Zahl, denn alle Wirbel drehen um dieselbe Achse senkrecht zur Ebene. Divergenz und Rotation sind dort beide skalar und gehen durch eine Drehung ineinander über.

:::satz Satz 6.3 (Drehen um $\pi/2$)
<span class="anker" id="satz-6-3"></span>

Für ein differenzierbares Feld $\boldsymbol{F}=(F_1,F_2)$ sei $\boldsymbol{F}^\perp=(-F_2,F_1)$, das um $\pi/2$ gegen den Uhrzeigersinn gedrehte Feld. Dann gilt

<span class="anker" id="gl-6-5"></span>
$$\operatorname{div}\boldsymbol{F}=\operatorname{rot}\boldsymbol{F}^\perp,\qquad\operatorname{div}\boldsymbol{F}^\perp=-\operatorname{rot}\boldsymbol{F}. \tag{6.5}$$
:::

:::beweis Einsetzen
$\operatorname{rot}\boldsymbol{F}^\perp=\partial_{x_1}F_1-\partial_{x_2}(-F_2)=\operatorname{div}\boldsymbol{F}$ und $\operatorname{div}\boldsymbol{F}^\perp=\partial_{x_1}(-F_2)+\partial_{x_2}F_1=-\operatorname{rot}\boldsymbol{F}$.
:::

:::abbildung hm3/k1wirbel 6
Dreht man das Strahlfeld $\boldsymbol{F}=(x,y)$ um $\pi/2$, wird aus der Quelle ein Wirbel: $\boldsymbol{F}^\perp$ ist das Drehfeld. Rechts das Scherfeld $\boldsymbol G=(y,0)$: Alle Pfeile laufen parallel, trotzdem ist die Rotation nicht null, weil die obere Kante eines Quadrats nach rechts und die untere nach links gezogen wird.
:::

**Beispiele.** Für die starre Drehung $\boldsymbol{F}=\omega\,(-x_2,x_1,0)$ mit Winkelgeschwindigkeit $\omega$ ist $\operatorname{rot}\boldsymbol{F}=(0,0,2\omega)$: die Drehachse, mit dem doppelten $\omega$ als Länge. Das Drehfeld hat also $\operatorname{rot}(-y,x)=2$ (Abb. [6](#abb-6)). Für die Felder aus der Tabelle in Stufe [4](radiale-funktionen-und-felder.html#stufe-4) gibt [(6.4)](#gl-6-4) $\operatorname{rot}(x\,\hat{\boldsymbol{e}}_r)=y/r$ und $\operatorname{rot}(2x,4y)=0$. **Kontrolle** mit [(6.5)](#gl-6-5): Das Strahlfeld hat $\operatorname{div}=2$ und $\operatorname{rot}=0$, sein gedrehtes Feld, das Drehfeld, hat $\operatorname{rot}=2$ und $\operatorname{div}=0$.

:::analogie
Halte ein winziges Schaufelrad in die Strömung. Dreht es sich, wirbelt das Feld an dieser Stelle, und $\operatorname{rot}\boldsymbol{E}$ zeigt längs der Drehachse. Das Bild stimmt nur, solange das Rad klein ist, und es zeigt nichts über Quellen.
:::

:::frage Rotation heißt doch, dass die Feldlinien im Kreis laufen?
Nein, die Rotation ist eine lokale Größe. Das Scherfeld $(y,0)$ hat parallele Feldlinien und $\operatorname{rot}=-1$. Umgekehrt kann ein Feld im Kreis laufen und trotzdem $\operatorname{rot}=0$ haben, wenn es nach außen gerade richtig abfällt: $\boldsymbol{H}=(-y,x)/(x^2+y^2)$ auf $\mathbb{R}^2\setminus\{0\}$.
:::

:::frage Wie ist das Kreuzprodukt für mehr als drei Komponenten definiert, etwa bei einem Feld $\boldsymbol{E}(\boldsymbol{x},t)$?
Bei $\boldsymbol{E}(\boldsymbol{x},t)$ stellt sich die Frage gar nicht: Das Feld hat vier Eingänge, aber nur drei Ausgänge. Das Kreuzprodukt arbeitet nur mit den Ausgängen, für jeden Punkt und jede Zeit einzeln, und $\operatorname{rot}$ leitet nur nach $x_1,x_2,x_3$ ab, $t$ bleibt dabei fest. Für zwei Vektoren mit $n\ge4$ Komponenten gibt es das Kreuzprodukt in dieser Form nicht, denn senkrecht zu beiden steht dort mehr als eine Richtung. Was bleibt, sind die Zahlen $a_jb_k-a_kb_j$ für jedes Paar $j<k$, je eine pro Koordinatenebene, zusammen $n(n-1)/2$ Stück. Nur für $n=3$ sind das drei, deshalb passen sie dort in einen Vektor.
:::

:::aufgabe Aufgabe 8 ★ Divergenz und Rotation rechnen
<span class="anker" id="aufg-8"></span>

<ol class="al">

<li>

Berechne $\operatorname{div}\boldsymbol{F}$ und $\operatorname{rot}\boldsymbol{F}$ für $\boldsymbol{F}(x,y,z)=(x^2y,\;yz,\;xz^2)$ im Punkt $(1,2,-1)$.

</li>

<li>

Berechne für $\boldsymbol G(x,y)=(x^2y,\;xy^2)$ die Größen $\operatorname{div}\boldsymbol G$, $\operatorname{rot}\boldsymbol G$, $\operatorname{div}\boldsymbol G^\perp$, $\operatorname{rot}\boldsymbol G^\perp$ und prüfe [(6.5)](#gl-6-5).

</li>

<li>

Bestätige die Behauptung über $\boldsymbol{H}$ aus der letzten Frage: $\operatorname{rot}\boldsymbol{H}=0$.

</li>

</ol>

:::loesung
(a) $\operatorname{div}\boldsymbol{F}=2xy+z+2xz$, im Punkt $4-1-2=1$. $\operatorname{rot}\boldsymbol{F}=(0-y,\;0-z^2,\;0-x^2)=(-y,-z^2,-x^2)$, im Punkt $(-2,-1,-1)$. (b) $\operatorname{div}\boldsymbol G=2xy+2xy=4xy$ und $\operatorname{rot}\boldsymbol G=y^2-x^2$. Mit $\boldsymbol G^\perp=(-xy^2,\;x^2y)$ ist $\operatorname{div}\boldsymbol G^\perp=-y^2+x^2=-\operatorname{rot}\boldsymbol G$ und $\operatorname{rot}\boldsymbol G^\perp=2xy+2xy=4xy=\operatorname{div}\boldsymbol G$. (c) Mit $\rho^2=x^2+y^2$ ist $\partial_x(x/\rho^2)=(y^2-x^2)/\rho^4$ und $\partial_y(-y/\rho^2)=(y^2-x^2)/\rho^4$. Die Differenz ist null.
:::
:::

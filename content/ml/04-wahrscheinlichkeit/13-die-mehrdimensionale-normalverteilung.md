---
title: Die mehrdimensionale Normalverteilung
pfad: Informatik / Machine Learning / Mathematische Grundlagen / Wahrscheinlichkeit
knoten: Grundlagen 4: Wahrscheinlichkeit
nachschlagen: ja
order: 15241300
summary: Die Normalverteilung gibt es auch für Vektoren.
tags: normalverteilt, gemeinsam normalverteilt, Mahalanobis-Abstand
lang: de
---

<span class="anker" id="stufe-12"></span>

:::zweck
Die Normalverteilung gibt es auch für Vektoren. Sie wird durch einen Erwartungswertvektor und eine Kovarianzmatrix vollständig beschrieben, und ihre Höhenlinien sind Ellipsen. Dieser Abschnitt zeigt, warum: Im Eigensystem der Kovarianzmatrix zerfällt sie in unabhängige eindimensionale Normalverteilungen. Daraus folgen ihre wichtigsten Eigenschaften: Sie bleibt unter linearen Abbildungen normal, ihre Rand- und bedingten Verteilungen sind normal, und bei ihr ist unkorreliert dasselbe wie unabhängig.
:::

### Die Dichte

<span class="anker" id="stufe-12-1"></span>

In einer Dimension steht im Exponenten der Normalverteilung die quadrierte Abweichung, geteilt durch die Varianz: $(x-\mu)^2/\sigma^2=(x-\mu)\,(\sigma^2)^{-1}(x-\mu)$. In mehreren Dimensionen tritt an die Stelle der Abweichung der Vektor $\mathbf{x}-\boldsymbol{\mu}$ und an die Stelle der Varianz die Kovarianzmatrix.

:::definition Definition 12.1 (Mehrdimensionale Normalverteilung)
<span class="anker" id="satz-12-1"></span>

Ein Zufallsvektor $\mathbf{x}\in\mathbb{R}^d$ heißt __normalverteilt__ mit dem Erwartungswertvektor $\boldsymbol{\mu}$ und der symmetrischen, positiv definiten Kovarianzmatrix $\boldsymbol{\Sigma}$, kurz $\mathbf{x}\sim\mathcal N(\boldsymbol{\mu},\boldsymbol{\Sigma})$, wenn er die Dichte

<span class="anker" id="gl-12-1"></span>
$$p(\mathbf{x})=\frac1{(2\pi)^{d/2}\sqrt{\det\boldsymbol{\Sigma}}}\,\exp\Bigl(-\tfrac12\,(\mathbf{x}-\boldsymbol{\mu})^{\top}\boldsymbol{\Sigma}^{-1}(\mathbf{x}-\boldsymbol{\mu})\Bigr) \tag{12.1}$$

hat. Statt „normalverteilt“ sagt man auch __gemeinsam normalverteilt__.
:::

Für $d=1$ ist $\det\boldsymbol{\Sigma}=\sigma^2$, und es entsteht [(8.5)](wichtige-verteilungen.html#gl-8-5). Ist $\boldsymbol{\Sigma}=\operatorname{diag}(\sigma_1^2,\dots,\sigma_d^2)$ diagonal, so ist der Exponent $-\tfrac12\sum_j(x_j-\mu_j)^2/\sigma_j^2$ und $\det\boldsymbol{\Sigma}=\prod_j\sigma_j^2$. Die Dichte zerfällt dann in das Produkt der $d$ eindimensionalen Dichten $\mathcal N(\mu_j,\sigma_j^2)$, und die Komponenten sind unabhängig. Unterabschnitt [12.3](#stufe-12-3) zeigt, dass $\boldsymbol{\mu}$ und $\boldsymbol{\Sigma}$ tatsächlich Erwartungswertvektor und Kovarianzmatrix sind. Die Formel braucht $\boldsymbol{\Sigma}^{-1}$ und $\det\boldsymbol{\Sigma}>0$, also eine positiv definite Kovarianzmatrix. Ist $\boldsymbol{\Sigma}$ singulär, so liegt die Verteilung nach Unterabschnitt [11.6](zufallsvektoren-und-die-kovarianzmatrix.html#stufe-11-6) auf einer Ebene oder Geraden, die den Raum nicht ausfüllt, und hat keine Dichte; dieses Kapitel betrachtet nur positiv definite $\boldsymbol{\Sigma}$.

⁠**Rechenbeispiel:** Für $d=2$ mit $\boldsymbol{\mu}=(1,\,2)^{\top}$ und $\boldsymbol{\Sigma}=\bigl(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr)$ ist $\det\boldsymbol{\Sigma}=3$ und $\boldsymbol{\Sigma}^{-1}=\tfrac13\bigl(\begin{smallmatrix}2&-1\\-1&2\end{smallmatrix}\bigr)$ nach [Grundlagen 1, Abschnitt 11.3](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/einheitsmatrix-und-inverse.html#stufe-11-3). Die Dichte ist am höchsten bei $\mathbf{x}=\boldsymbol{\mu}$, mit dem Wert $1/(2\pi\sqrt3)\approx0{,}0919$. Der Korrelationskoeffizient der beiden Komponenten ist $1/\sqrt{2\cdot2}=0{,}5$.

⁠**Kurz gesagt:** Die mehrdimensionale Normalverteilung hat im Exponenten die quadratische Form $-\tfrac12(\mathbf{x}-\boldsymbol{\mu})^{\top}\boldsymbol{\Sigma}^{-1}(\mathbf{x}-\boldsymbol{\mu})$; bei diagonaler Kovarianzmatrix ist sie das Produkt unabhängiger eindimensionaler Normalverteilungen.

### Höhenlinien und der Mahalanobis-Abstand

<span class="anker" id="stufe-12-2"></span>

Die Dichte hängt von $\mathbf{x}$ nur über die Zahl im Exponenten ab. Punkte mit gleichem Wert dieser Zahl haben gleiche Dichte. Die Zahl ist eine quadratische Form in $\mathbf{x}-\boldsymbol{\mu}$, und wie [Grundlagen 2](/wissen/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/projektion-eigenwerte-und-zerlegungen.html) gezeigt hat, sind die Höhenlinien einer positiv definiten quadratischen Form Ellipsen.

:::definition Definition 12.2 (Mahalanobis-Abstand)
<span class="anker" id="satz-12-2"></span>

Für eine symmetrische, positiv definite Matrix $\boldsymbol{\Sigma}$ heißt

<span class="anker" id="gl-12-2"></span>
$$\Delta(\mathbf{x})=\sqrt{(\mathbf{x}-\boldsymbol{\mu})^{\top}\boldsymbol{\Sigma}^{-1}(\mathbf{x}-\boldsymbol{\mu})} \tag{12.2}$$

der __Mahalanobis-Abstand__ von $\mathbf{x}$ zu $\boldsymbol{\mu}$.
:::

Die Dichte [(12.1)](#gl-12-1) ist $p(\mathbf{x})=p(\boldsymbol{\mu})\,\mathrm{e}^{-\Delta^2/2}$. Die Höhenlinien der Dichte sind also die Mengen mit festem Mahalanobis-Abstand. Ihre Form folgt aus [Grundlagen 2, Abschnitt 7.7](/wissen/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/diagonalisierung-und-spektralsatz.html#stufe-7-7). $\boldsymbol{\Sigma}^{-1}$ hat dieselben Eigenvektoren $\mathbf{q}_i$ wie $\boldsymbol{\Sigma}$ und die Eigenwerte $1/\lambda_i$, denn aus $\boldsymbol{\Sigma}\mathbf{q}_i=\lambda_i\mathbf{q}_i$ folgt $\boldsymbol{\Sigma}^{-1}\mathbf{q}_i=\lambda_i^{-1}\mathbf{q}_i$. Die Ellipse $\Delta=1$ hat deshalb ihre Achsen in den Richtungen $\mathbf{q}_i$ und die Halbachsen $1/\sqrt{1/\lambda_i}=\sqrt{\lambda_i}$, also die Standardabweichungen in diesen Richtungen. Die Ellipse $\Delta=c$ ist um den Faktor $c$ größer. Der Mahalanobis-Abstand misst also den Abstand in Standardabweichungen, gezählt in der Richtung, in der man sich bewegt.

:::abbildung ml/k4ellipsen 17
Die Normalverteilung mit $\boldsymbol{\mu}=(1,2)^{\top}$ und $\boldsymbol{\Sigma}=\bigl(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr)$. (a) Die Höhenlinien $\Delta=1$ (durchgezogen) und $\Delta=2$ (gestrichelt) sind Ellipsen mit den Achsen in Richtung der Eigenvektoren $\mathbf{q}_1=(1,1)^{\top}/\sqrt2$ zum Eigenwert $3$ und $\mathbf{q}_2=(1,-1)^{\top}/\sqrt2$ zum Eigenwert $1$; die Halbachsen der inneren Ellipse sind $\sqrt3$ und $1$. Dazu $80$ Punkte, gezogen aus dieser Verteilung: $31$ liegen innerhalb von $\Delta=1$, $69$ innerhalb von $\Delta=2$. (b) Kennt man $x_2=4$, so ist $x_1$ normalverteilt mit dem Erwartungswert $2$ und der Standardabweichung $\sqrt{3/2}\approx1{,}22$ (orange: $\pm$ eine Standardabweichung). Die graue Gerade verbindet die bedingten Erwartungswerte für alle Werte von $x_2$; sie geht durch $\boldsymbol{\mu}$ und durch die Punkte, an denen die Ellipsen waagrechte Tangenten haben.
:::

⁠**Rechenbeispiel:** Für die Verteilung aus Unterabschnitt [12.1](#stufe-12-1) mit den Eigenwerten $3$ und $1$ vergleiche man die Punkte $\mathbf{x}_a=\boldsymbol{\mu}+(1{,}5;\ 1{,}5)^{\top}$ und $\mathbf{x}_b=\boldsymbol{\mu}+(1,\,-1)^{\top}$. Euklidisch ist $\mathbf{x}_a$ weiter von $\boldsymbol{\mu}$ entfernt, $\sqrt{4{,}5}\approx2{,}12$ gegen $\sqrt2\approx1{,}41$. In Eigenkoordinaten $y_i=\mathbf{q}_i^{\top}(\mathbf{x}-\boldsymbol{\mu})$ liegt $\mathbf{x}_a$ bei $y_1=1{,}5\sqrt2$, $y_2=0$ und $\mathbf{x}_b$ bei $y_1=0$, $y_2=\sqrt2$, und Abb. [18](#abb-18) ergibt $\Delta(\mathbf{x}_a)\approx1{,}22$ und $\Delta(\mathbf{x}_b)\approx1{,}41$. Der Punkt $\mathbf{x}_a$ liegt in der Richtung, in der die Verteilung weit streut, und ist deshalb weniger ungewöhnlich als $\mathbf{x}_b$, obwohl er weiter entfernt ist. Seine Dichte ist größer.

:::abbildung ml/k4rmahalanobis 18
Der Mahalanobis-Abstand zweier Punkte in Eigenkoordinaten: Jede Koordinate wird durch die Varianz in ihrer Richtung geteilt. Also ist $\Delta(\mathbf{x}_a)=\sqrt{1{,}5}\approx1{,}22$ und $\Delta(\mathbf{x}_b)=\sqrt2\approx1{,}41$.
:::

⁠**Kurz gesagt:** Die Höhenlinien der Normalverteilung sind Ellipsen konstanten Mahalanobis-Abstands, mit Achsen in Richtung der Eigenvektoren von $\boldsymbol{\Sigma}$ und Halbachsen $\Delta\sqrt{\lambda_i}$; der Mahalanobis-Abstand misst in Standardabweichungen der jeweiligen Richtung.

### Im Eigensystem zerfällt die Verteilung

<span class="anker" id="stufe-12-3"></span>

[Grundlagen 2](/wissen/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/projektion-eigenwerte-und-zerlegungen.html) hat gezeigt, dass eine symmetrische Matrix in ihrer Eigenbasis diagonal wird und gekoppelte Rechnungen in unabhängige eindimensionale zerfallen. Für die Normalverteilung heißt das: In den Koordinaten der Hauptachsen ist sie das Produkt unabhängiger eindimensionaler Normalverteilungen.

:::satz Satz 12.3 (Zerlegung im Eigensystem)
<span class="anker" id="satz-12-3"></span>

Es sei $\mathbf{x}\sim\mathcal N(\boldsymbol{\mu},\boldsymbol{\Sigma})$ und $\boldsymbol{\Sigma}=\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top}$ die Zerlegung aus dem Spektralsatz ([Grundlagen 2, Abschnitt 7.6](/wissen/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/diagonalisierung-und-spektralsatz.html#stufe-7-6)), mit orthonormalen Eigenvektoren $\mathbf{q}_i$ als Spalten von $\mathbf{Q}$ und den Eigenwerten $\lambda_i>0$. Dann sind die Koordinaten

<span class="anker" id="gl-12-3"></span>
$$\mathbf{y}=\mathbf{Q}^{\top}(\mathbf{x}-\boldsymbol{\mu}),\qquad y_i=\mathbf{q}_i^{\top}(\mathbf{x}-\boldsymbol{\mu}), \tag{12.3}$$

unabhängig, und $y_i\sim\mathcal N(0,\lambda_i)$. Insbesondere ist $\mathbb{E}[\mathbf{x}]=\boldsymbol{\mu}$ und $\operatorname{Cov}(\mathbf{x})=\boldsymbol{\Sigma}$.
:::

:::beweis Zerlegung im Eigensystem
Es ist $\boldsymbol{\Sigma}^{-1}=\mathbf{Q}\boldsymbol{\Lambda}^{-1}\mathbf{Q}^{\top}$, also $(\mathbf{x}-\boldsymbol{\mu})^{\top}\boldsymbol{\Sigma}^{-1}(\mathbf{x}-\boldsymbol{\mu})=\mathbf{y}^{\top}\boldsymbol{\Lambda}^{-1}\mathbf{y}=\sum_iy_i^2/\lambda_i$, und $\det\boldsymbol{\Sigma}=\prod_i\lambda_i$. Die Abbildung von $\mathbf{x}$ auf $\mathbf{y}$ verschiebt und dreht nur; ihre Jacobi-Matrix $\mathbf{Q}^{\top}$ hat den Betrag der Determinante $1$. Nach dem Flächenfaktor aus [Grundlagen 3, Abschnitt 5.4](/wissen/informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel/die-jacobi-matrix.html#stufe-5-4), ändert sie Flächen und Volumina nicht, und die Dichte von $\mathbf{y}$ ist an jeder Stelle dieselbe Zahl wie die von $\mathbf{x}$ an der zugehörigen Stelle (vergleiche den Variablenwechsel im Hintergrund-Kasten von Unterabschnitt [8.6](wichtige-verteilungen.html#stufe-8-6)). Also ist

$$p(\mathbf{y})=\frac1{(2\pi)^{d/2}\sqrt{\prod_i\lambda_i}}\,\exp\Bigl(-\tfrac12\sum_i\frac{y_i^2}{\lambda_i}\Bigr)=\prod_{i=1}^d\frac1{\sqrt{2\pi\lambda_i}}\,\mathrm{e}^{-y_i^2/(2\lambda_i)} ,$$

das Produkt der Dichten $\mathcal N(0,\lambda_i)$. Damit ist $\mathbb{E}[\mathbf{y}]=\mathbf{0}$ und $\operatorname{Cov}(\mathbf{y})=\boldsymbol{\Lambda}$. Wegen $\mathbf{x}=\mathbf{Q}\mathbf{y}+\boldsymbol{\mu}$ folgt mit [(11.1)](zufallsvektoren-und-die-kovarianzmatrix.html#gl-11-1) und [(11.4)](zufallsvektoren-und-die-kovarianzmatrix.html#gl-11-4) $\mathbb{E}[\mathbf{x}]=\boldsymbol{\mu}$ und $\operatorname{Cov}(\mathbf{x})=\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top}=\boldsymbol{\Sigma}$.
:::

Anschaulich ist eine mehrdimensionale Normalverteilung also eine Wolke aus unabhängigen Glocken entlang senkrechter Achsen, die gedreht und verschoben wurde. Die Drehung koppelt die Koordinaten $x_1,\dots,x_d$ und macht sie korreliert; in den Koordinaten der Hauptachsen ist die Kopplung verschwunden. Die Achsen sind die Richtungen extremer Streuung aus Unterabschnitt [11.6](zufallsvektoren-und-die-kovarianzmatrix.html#stufe-11-6).

⁠**Rechenbeispiel:** Für $\boldsymbol{\mu}=(1,\,2)^{\top}$ und $\boldsymbol{\Sigma}=\bigl(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr)$ ist $y_1=\tfrac1{\sqrt2}(x_1-1+x_2-2)$ normalverteilt mit Varianz $3$ und $y_2=\tfrac1{\sqrt2}(x_1-1-x_2+2)$ mit Varianz $1$, und beide sind unabhängig. Die Summe $x_1+x_2=\sqrt2\,y_1+3$ hat also die Varianz $2\cdot3=6$, wie auch $\mathbf{1}^{\top}\boldsymbol{\Sigma}\mathbf{1}=2+1+1+2=6$ ergibt.

⁠**Kurz gesagt:** In den Koordinaten der Eigenvektoren von $\boldsymbol{\Sigma}$ ist die Normalverteilung ein Produkt unabhängiger eindimensionaler Normalverteilungen mit den Eigenwerten als Varianzen.

:::hintergrund Wie viel Wahrscheinlichkeit in einer Ellipse liegt
In einer Dimension liegen $68{,}3\,\%$ innerhalb einer Standardabweichung. In zwei Dimensionen liegt innerhalb der Ellipse $\Delta=1$ deutlich weniger. Mit den Eigenkoordinaten, geteilt durch $\sqrt{\lambda_i}$, wird die Verteilung zu zwei unabhängigen Standardnormalverteilungen, und die Ellipse wird zum Kreis vom Radius $c$. Mit Polarkoordinaten wie in der Herleitung zu Unterabschnitt [8.5](wichtige-verteilungen.html#stufe-8-5) ist

$$P(\Delta\le c)=\int_0^{2\pi}\!\!\int_0^c\frac1{2\pi}\,\mathrm{e}^{-r^2/2}\,r\,\mathrm{d} r\,\mathrm{d}\varphi=1-\mathrm{e}^{-c^2/2} .$$

Das ergibt $39{,}3\,\%$ für $c=1$, $86{,}5\,\%$ für $c=2$ und $98{,}9\,\%$ für $c=3$. Von den $80$ Punkten in Abb. [17](#abb-17) (a) liegen $31$, also $38{,}8\,\%$, innerhalb von $\Delta=1$ und $69$, also $86{,}3\,\%$, innerhalb von $\Delta=2$. In höheren Dimensionen sinkt der Anteil weiter: Viele Komponenten, von denen jede ein wenig abweicht, ergeben zusammen fast sicher einen großen Abstand. Wer Ausreißer mit einer festen Schwelle für $\Delta$ sucht, muss die Schwelle deshalb nach der Dimension wählen.
:::

### Lineare Abbildungen und das Erzeugen normalverteilter Vektoren

<span class="anker" id="stufe-12-4"></span>

Bildet man aus normalverteilten Größen Summen, Differenzen oder andere Linearkombinationen, so bleibt die Glockenform erhalten. Das macht die Normalverteilung so bequem: Man muss nur Erwartungswertvektor und Kovarianzmatrix nachrechnen, und die bekommt man aus [(11.1)](zufallsvektoren-und-die-kovarianzmatrix.html#gl-11-1) und [(11.4)](zufallsvektoren-und-die-kovarianzmatrix.html#gl-11-4).

:::satz Satz 12.4 (Lineare Abbildungen normalverteilter Vektoren)
<span class="anker" id="satz-12-4"></span>

Ist $\mathbf{x}\sim\mathcal N(\boldsymbol{\mu},\boldsymbol{\Sigma})$, $\mathbf{A}\in\mathbb{R}^{m\times d}$ mit Rang $m$ und $\mathbf{b}\in\mathbb{R}^m$, so ist

<span class="anker" id="gl-12-4"></span>
$$\mathbf{A}\mathbf{x}+\mathbf{b}\sim\mathcal N\bigl(\mathbf{A}\boldsymbol{\mu}+\mathbf{b},\ \mathbf{A}\boldsymbol{\Sigma}\mathbf{A}^{\top}\bigr). \tag{12.4}$$

Insbesondere ist jede Komponente $x_j\sim\mathcal N(\mu_j,\Sigma_{jj})$, und jede Linearkombination $\mathbf{u}^{\top}\mathbf{x}$ mit $\mathbf{u}\ne\mathbf{0}$ ist normalverteilt mit der Varianz $\mathbf{u}^{\top}\boldsymbol{\Sigma}\mathbf{u}$.
:::

Für eine invertierbare Matrix $\mathbf{A}$ folgt der Satz aus dem Variablenwechsel: Der Exponent bleibt eine quadratische Form, und der Vorfaktor ändert sich um den Faktor $1/|\det\mathbf{A}|$. Für $m<d$ ergänzt man $\mathbf{A}$ zu einer invertierbaren Matrix und marginalisiert die zusätzlichen Komponenten heraus; die Rechnung ist länger und wird hier nicht ausgeführt.

Umgekehrt lässt sich jede Normalverteilung aus der einfachsten erzeugen. Hat $\mathbf{z}$ unabhängige standardnormalverteilte Komponenten, so ist $\mathbf{z}\sim\mathcal N(\mathbf{0},\mathbf{I})$. Mit der Cholesky-Zerlegung $\boldsymbol{\Sigma}=\mathbf{L}\mathbf{L}^{\top}$ aus [Grundlagen 2, Abschnitt 8.6](/wissen/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/positiv-definite-matrizen.html#stufe-8-6), ist dann nach [(12.4)](#gl-12-4)

<span class="anker" id="gl-12-5"></span>
$$\mathbf{x}=\boldsymbol{\mu}+\mathbf{L}\mathbf{z}\sim\mathcal N(\boldsymbol{\mu},\boldsymbol{\Sigma}). \tag{12.5}$$

So erzeugen Rechner normalverteilte Zufallsvektoren mit vorgegebener Kovarianzmatrix; die $80$ Punkte in Abb. [17](#abb-17) sind so entstanden.

⁠**Rechenbeispiel:** Für $\boldsymbol{\Sigma}=\bigl(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr)$ ist $\mathbf{L}=\bigl(\begin{smallmatrix}\sqrt2&0\\1/\sqrt2&\sqrt{3/2}\end{smallmatrix}\bigr)$, denn $\mathbf{L}\mathbf{L}^{\top}$ hat die Einträge $2$, $\sqrt2\cdot\tfrac1{\sqrt2}=1$ und $\tfrac12+\tfrac32=2$. Aus $\mathbf{z}=(1,\,-1)^{\top}$ wird $\mathbf{x}=(1,\,2)^{\top}+\bigl(\sqrt2;\ \tfrac1{\sqrt2}-\sqrt{3/2}\bigr)^{\top}\approx(2{,}414;\ 1{,}482)^{\top}$. Die erste Komponente $x_1$ allein ist $\mathcal N(1,2)$-verteilt.

⁠**Kurz gesagt:** Lineare Abbildungen normalverteilter Vektoren sind wieder normalverteilt, mit $\mathbf{A}\boldsymbol{\mu}+\mathbf{b}$ und $\mathbf{A}\boldsymbol{\Sigma}\mathbf{A}^{\top}$; aus unabhängigen Standardnormalverteilten erzeugt $\boldsymbol{\mu}+\mathbf{L}\mathbf{z}$ jede Normalverteilung.

### Bedingte Verteilungen

<span class="anker" id="stufe-12-5"></span>

Zwei gemeinsam normalverteilte Messgrößen seien korreliert. Misst man die eine, so weiß man mehr über die andere: Ihr Erwartungswert verschiebt sich, und ihre Unsicherheit wird kleiner. Bei der Normalverteilung lässt sich beides genau ausrechnen, und die bedingte Verteilung ist wieder eine Normalverteilung.

:::satz Satz 12.5 (Bedingte Normalverteilung)
<span class="anker" id="satz-12-5"></span>

Es sei $(x_1,x_2)^{\top}\sim\mathcal N(\boldsymbol{\mu},\boldsymbol{\Sigma})$ mit $\boldsymbol{\mu}=(\mu_1,\mu_2)^{\top}$ und $\boldsymbol{\Sigma}=\bigl(\begin{smallmatrix}\Sigma_{11}&\Sigma_{12}\\\Sigma_{12}&\Sigma_{22}\end{smallmatrix}\bigr)$. Gegeben $x_2$ ist $x_1$ normalverteilt mit

<span class="anker" id="gl-12-6"></span>
$$\mu_{1|2}=\mu_1+\frac{\Sigma_{12}}{\Sigma_{22}}\,(x_2-\mu_2),\qquad \sigma^2_{1|2}=\Sigma_{11}-\frac{\Sigma_{12}^2}{\Sigma_{22}}=\Sigma_{11}\,(1-\rho^2). \tag{12.6}$$

Für Vektoren $\mathbf{x}_a$, $\mathbf{x}_b$ mit den Blöcken $\boldsymbol{\Sigma}_{aa}$, $\boldsymbol{\Sigma}_{ab}$, $\boldsymbol{\Sigma}_{bb}$ gilt entsprechend $\boldsymbol{\mu}_{a|b}=\boldsymbol{\mu}_a+\boldsymbol{\Sigma}_{ab}\boldsymbol{\Sigma}_{bb}^{-1}(\mathbf{x}_b-\boldsymbol{\mu}_b)$ und $\boldsymbol{\Sigma}_{a|b}=\boldsymbol{\Sigma}_{aa}-\boldsymbol{\Sigma}_{ab}\boldsymbol{\Sigma}_{bb}^{-1}\boldsymbol{\Sigma}_{ab}^{\top}$.
:::

:::herleitung Bedingte Normalverteilung durch quadratisches Ergänzen
Nach Unterabschnitt [9.4](mehrere-zufallsvariablen.html#stufe-9-4) ist $p(x_1\mid x_2)=p(x_1,x_2)/p(x_2)$ mit der Randdichte $p(x_2)$; bei festem $x_2$ ist der Nenner eine Zahl. Als Funktion von $x_1$ ist die bedingte Dichte also proportional zu $\exp\bigl(-\tfrac12\,Q\bigr)$ mit der quadratischen Form $Q$ aus dem Exponenten. Mit $a_1=x_1-\mu_1$, $a_2=x_2-\mu_2$ und $D=\det\boldsymbol{\Sigma}$ ist nach [Grundlagen 1, Abschnitt 11.3](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/einheitsmatrix-und-inverse.html#stufe-11-3),

$$Q=\frac1D\bigl(\Sigma_{22}a_1^2-2\Sigma_{12}a_1a_2+\Sigma_{11}a_2^2\bigr).$$

Quadratisches Ergänzen in $a_1$ wie in [Grundlagen 2, Abschnitt 5.4](/wissen/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/quadratische-formen.html#stufe-5-4), ergibt

$$Q=\frac{\Sigma_{22}}D\Bigl(a_1-\frac{\Sigma_{12}}{\Sigma_{22}}a_2\Bigr)^2+\text{(ein Glied ohne }a_1).$$

Das Glied ohne $a_1$ wird bei festem $x_2$ zu einem konstanten Faktor. Was bleibt, ist der Exponent einer Normalverteilung in $x_1$ mit dem Erwartungswert $\mu_1+\frac{\Sigma_{12}}{\Sigma_{22}}a_2$ und der Varianz $D/\Sigma_{22}=\Sigma_{11}-\Sigma_{12}^2/\Sigma_{22}$. Mit $\rho=\Sigma_{12}/\sqrt{\Sigma_{11}\Sigma_{22}}$ ist das $\Sigma_{11}(1-\rho^2)$.
:::

Drei Dinge fallen auf. Der bedingte Erwartungswert hängt linear von $x_2$ ab; er liegt auf einer Geraden durch $\boldsymbol{\mu}$ (Abb. [17](#abb-17) (b)). Die bedingte Varianz ist nie größer als die Randvarianz $\Sigma_{11}$, und sie hängt nicht vom beobachteten Wert $x_2$ ab, nur von der Stärke der Korrelation. Und für $\rho=0$ ändert die Beobachtung gar nichts.

⁠**Rechenbeispiel:** Für $\boldsymbol{\mu}=(1,\,2)^{\top}$ und $\boldsymbol{\Sigma}=\bigl(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr)$ werde $x_2=4$ beobachtet. Dann ist $\mu_{1|2}=1+\tfrac12\,(4-2)=2$ und $\sigma^2_{1|2}=2-\tfrac12=1{,}5$. Ohne die Beobachtung ist $x_1\sim\mathcal N(1,2)$. Die Messung von $x_2$ hat den Erwartungswert von $x_1$ verschoben und seine Varianz um ein Viertel verringert, um den Anteil $\rho^2=0{,}25$.

⁠**Kurz gesagt:** Bei der Normalverteilung ist die bedingte Verteilung wieder normal; ihr Erwartungswert liegt auf einer Geraden in der beobachteten Größe, ihre Varianz $\Sigma_{11}(1-\rho^2)$ hängt nicht vom beobachteten Wert ab.

:::hintergrund Der Kalman-Filter: Bedingen, immer wieder
Ein Navigationsgerät bestimmt Ort und Geschwindigkeit eines Fahrzeugs aus verrauschten Satellitenmessungen. Der Kalman-Filter, der dafür in der Regelungs- und Nachrichtentechnik verwendet wird, beschreibt den Zustand als normalverteilten Vektor. Bei jeder neuen Messung bildet er die bedingte Verteilung des Zustands gegeben die Messung, genau mit den Formeln [(12.6)](#gl-12-6) in Vektorform; zwischen den Messungen schreibt er die Verteilung mit der Bewegungsgleichung fort, einer linearen Abbildung, unter der sie nach [(12.4)](#gl-12-4) normal bleibt. Weil die bedingte Varianz nicht von den Messwerten abhängt, kann man sogar vor der ersten Messung ausrechnen, wie genau das Ergebnis werden wird.
:::

### Unkorreliert und unabhängig

<span class="anker" id="stufe-12-6"></span>

Nach Unterabschnitt [10.5](kovarianz-und-korrelation.html#stufe-10-5) folgt aus unkorreliert im Allgemeinen nicht unabhängig. Bei gemeinsam normalverteilten Größen ist das anders.

:::satz Satz 12.6 (Unkorreliert heißt bei der Normalverteilung unabhängig)
<span class="anker" id="satz-12-6"></span>

Sind $x_1,\dots,x_d$ gemeinsam normalverteilt und paarweise unkorreliert, so sind sie unabhängig.
:::

Denn dann ist $\boldsymbol{\Sigma}$ diagonal, und nach Unterabschnitt [12.1](#stufe-12-1) zerfällt die Dichte in das Produkt der Randdichten. Für die Normalverteilung ist die Kovarianzmatrix also die vollständige Beschreibung aller Zusammenhänge zwischen den Komponenten.

:::warnung Einzeln normalverteilt genügt nicht
Die Voraussetzung ist, dass der Vektor gemeinsam normalverteilt ist, nicht nur jede Komponente für sich. Im Rechenbeispiel 2 aus Unterabschnitt [10.5](kovarianz-und-korrelation.html#stufe-10-5) sind $X$ und $Y=VX$ beide standardnormalverteilt und unkorreliert, aber abhängig. Der Vektor $(X,Y)^{\top}$ ist nicht gemeinsam normalverteilt: Sonst wäre nach [(12.4)](#gl-12-4) auch $X+Y$ normalverteilt, aber $X+Y$ ist mit der Wahrscheinlichkeit $\tfrac12$ genau $0$. Seine Punkte liegen auf zwei Geraden (Abb. [13](kovarianz-und-korrelation.html#abb-13) (f)), nicht in einer elliptischen Wolke.
:::

⁠**Rechenbeispiel:** In Unterabschnitt [11.4](zufallsvektoren-und-die-kovarianzmatrix.html#stufe-11-4) waren Summe und Differenz der beiden Merkmale unkorreliert. Ist $\mathbf{x}\sim\mathcal N(\boldsymbol{\mu},\boldsymbol{\Sigma})$ mit $\boldsymbol{\Sigma}=\bigl(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr)$, so ist $(x_1+x_2,\ x_1-x_2)^{\top}$ nach [(12.4)](#gl-12-4) gemeinsam normalverteilt mit der Kovarianzmatrix $\operatorname{diag}(6;\,2)$. Die beiden Größen sind deshalb nicht nur unkorreliert, sondern unabhängig: Wer die Summe kennt, weiß nichts über die Differenz.

⁠**Kurz gesagt:** Bei gemeinsam normalverteilten Größen folgt aus unkorreliert die Unabhängigkeit; einzeln normalverteilte Größen genügen dafür nicht.

:::hintergrund Warum die Normalverteilung diese Sonderstellung hat
Die Dichte [(12.1)](#gl-12-1) hängt nur über eine quadratische Form vom Ort ab. Eine quadratische Form enthält genau die Produkte je zweier Komponenten, und deren Gewichte sind durch die Kovarianzmatrix festgelegt. Mehr als paarweise, lineare Zusammenhänge kann die Verteilung deshalb gar nicht ausdrücken. Ist die Kovarianzmatrix diagonal, fehlen die gemischten Glieder, der Exponent wird eine Summe, und die Exponentialfunktion macht aus der Summe ein Produkt. Bei anderen Verteilungen können Zusammenhänge in Größen wie $\mathbb{E}[X^2Y]$ oder in der Form der Punktwolke stecken, die keine Kovarianz sieht, wie die Parabel und das Kreuz in Abb. [13](kovarianz-und-korrelation.html#abb-13). Deshalb darf man aus einer kleinen Korrelation nur dann auf Unabhängigkeit schließen, wenn man Grund hat, eine gemeinsame Normalverteilung anzunehmen.
:::

:::aufgabe Aufgabe 37 ★ Welcher Punkt ist ungewöhnlicher?
<span class="anker" id="aufg-37"></span>

Es sei $\mathbf{x}\sim\mathcal N\bigl(\mathbf{0},\operatorname{diag}(4;\,1)\bigr)$.

<ol class="al">

<li>

Berechne den euklidischen Abstand und den Mahalanobis-Abstand der Punkte $(2,0)$ und $(0,2)$ zum Nullpunkt.

</li>

<li>

Welcher Punkt hat die größere Dichte? Um welchen Faktor?

</li>

<li>

Skizziere die Höhenlinien $\Delta=1$ und $\Delta=2$.

</li>

</ol>

:::loesung
(a) Beide Punkte haben den euklidischen Abstand $2$. Mit $\boldsymbol{\Sigma}^{-1}=\operatorname{diag}(\tfrac14;\,1)$ ist $\Delta(2,0)=\sqrt{4/4}=1$ und $\Delta(0,2)=\sqrt{4/1}=2$.

(b) $(2,0)$ hat die größere Dichte, um den Faktor $\mathrm{e}^{-1/2}/\mathrm{e}^{-2}=\mathrm{e}^{1{,}5}\approx4{,}48$. In Richtung $x_1$ ist die Standardabweichung $2$, ein Abstand $2$ ist dort nur eine Standardabweichung; in Richtung $x_2$ sind es zwei.

(c) Ellipsen um den Nullpunkt mit den Halbachsen $2$ und $1$ ($\Delta=1$) bzw. $4$ und $2$ ($\Delta=2$) entlang der $x_1$- und $x_2$-Achse.
:::
:::

:::aufgabe Aufgabe 38 ★★ Eine Messung verbessert die andere
<span class="anker" id="aufg-38"></span>

Zwei Messgrößen seien gemeinsam normalverteilt mit $\boldsymbol{\mu}=\mathbf{0}$ und $\boldsymbol{\Sigma}=\bigl(\begin{smallmatrix}4&2\\2&3\end{smallmatrix}\bigr)$.

<ol class="al">

<li>

Gib die Randverteilung von $x_1$ an.

</li>

<li>

Berechne die bedingte Verteilung von $x_1$ gegeben $x_2=3$. Um wie viel Prozent sinkt die Varianz?

</li>

<li>

Wie groß müsste $|\rho|$ sein, damit die bedingte Standardabweichung höchstens halb so groß ist wie die Randstandardabweichung?

</li>

</ol>

:::loesung
(a) $x_1\sim\mathcal N(0,4)$.

(b) $\mu_{1|2}=0+\tfrac23\cdot3=2$ und $\sigma^2_{1|2}=4-\tfrac43=\tfrac83\approx2{,}67$. Die Varianz sinkt um $\tfrac13$, also um $33{,}3\,\%$; das ist $\rho^2=\tfrac{4}{12}$.

(c) $\sigma_{1|2}=\sigma_1\sqrt{1-\rho^2}\le\tfrac12\sigma_1$ verlangt $1-\rho^2\le\tfrac14$, also $|\rho|\ge\sqrt{3}/2\approx0{,}866$.
:::
:::

:::aufgabe Aufgabe 39 ★★ Erzeugen mit Cholesky
<span class="anker" id="aufg-39"></span>

<ol class="al">

<li>

Bestimme die Cholesky-Zerlegung $\boldsymbol{\Sigma}=\mathbf{L}\mathbf{L}^{\top}$ von $\boldsymbol{\Sigma}=\bigl(\begin{smallmatrix}4&2\\2&3\end{smallmatrix}\bigr)$.

</li>

<li>

Ein Rechner liefert die unabhängigen Standardnormal-Werte $z_1=0{,}5$ und $z_2=-1$. Welchen Punkt aus $\mathcal N\bigl((1,1)^{\top},\boldsymbol{\Sigma}\bigr)$ erzeugt [(12.5)](#gl-12-5)?

</li>

<li>

Zeige allgemein mit [(11.4)](zufallsvektoren-und-die-kovarianzmatrix.html#gl-11-4), dass $\boldsymbol{\mu}+\mathbf{L}\mathbf{z}$ die Kovarianzmatrix $\boldsymbol{\Sigma}$ hat.

</li>

</ol>

:::loesung
(a) $l_{11}=\sqrt4=2$, $l_{21}=2/2=1$, $l_{22}=\sqrt{3-1}=\sqrt2$, also $\mathbf{L}=\bigl(\begin{smallmatrix}2&0\\1&\sqrt2\end{smallmatrix}\bigr)$. Probe: $\mathbf{L}\mathbf{L}^{\top}=\bigl(\begin{smallmatrix}4&2\\2&1+2\end{smallmatrix}\bigr)$.

(b) $\mathbf{L}\mathbf{z}=(2\cdot0{,}5;\ 1\cdot0{,}5-\sqrt2)^{\top}\approx(1;\ -0{,}914)^{\top}$, also $\mathbf{x}\approx(2;\ 0{,}086)^{\top}$.

(c) $\operatorname{Cov}(\boldsymbol{\mu}+\mathbf{L}\mathbf{z})=\mathbf{L}\,\operatorname{Cov}(\mathbf{z})\,\mathbf{L}^{\top}=\mathbf{L}\mathbf{I}\mathbf{L}^{\top}=\boldsymbol{\Sigma}$; der feste Vektor $\boldsymbol{\mu}$ ändert die Kovarianz nicht.
:::
:::

:::aufgabe Aufgabe 40 ★★★ Die Ellipse mit $95\,\%$
<span class="anker" id="aufg-40"></span>

<ol class="al">

<li>

Bestimme für eine zweidimensionale Normalverteilung den Wert $c$, für den die Ellipse $\Delta=c$ genau $95\,\%$ der Wahrscheinlichkeit enthält. Vergleiche mit dem Wert $1{,}96$ in einer Dimension.

</li>

<li>

Gib für $\boldsymbol{\mu}=(1,2)^{\top}$ und $\boldsymbol{\Sigma}=\bigl(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr)$ die Richtungen und Längen der Halbachsen dieser Ellipse an.

</li>

</ol>

:::loesung
(a) $1-\mathrm{e}^{-c^2/2}=0{,}95$ ergibt $c^2=-2\ln0{,}05\approx5{,}99$ und $c\approx2{,}448$. In zwei Dimensionen muss man weiter hinausgehen als die $1{,}96$ Standardabweichungen in einer Dimension, weil zwei Koordinaten Gelegenheit zur Abweichung haben.

(b) In Richtung $\tfrac1{\sqrt2}(1,1)^{\top}$ die Halbachse $2{,}448\cdot\sqrt3\approx4{,}24$, in Richtung $\tfrac1{\sqrt2}(1,-1)^{\top}$ die Halbachse $2{,}448\cdot1\approx2{,}45$, um den Mittelpunkt $(1,2)$.
:::
:::

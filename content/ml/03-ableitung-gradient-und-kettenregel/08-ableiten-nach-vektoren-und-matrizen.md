---
title: Ableiten nach Vektoren und Matrizen
pfad: Informatik / Machine Learning / Mathematische Grundlagen / Ableitung, Gradient und Kettenregel
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Kapitel 3: Ableitung, Gradient und Kettenregel
nachschlagen: ja
order: 15230800
summary: Gradienten von Ausdrücken wie a top x , x top Ax oder lVerty-AxrVert 2 braucht man immer wieder.
tags: Layout-Konvention
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Gradienten von Ausdrücken wie $\mathbf{a}^{\top}\mathbf{x}$, $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}$ oder $\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert^2$ braucht man immer wieder. Dieser Abschnitt legt zuerst fest, welche Form jede Ableitung hat, und leitet dann die wichtigsten Formeln komponentenweise her. Am Ende stehen Ableitungen nach einer Matrix und die Regel, mit der man eine Empfindlichkeit rückwärts durch ein Matrixprodukt rechnet.
:::

### Die Layout-Konvention

<span class="anker" id="stufe-7-1"></span>

Bei Funktionen einer Variablen ist die Ableitung eine Zahl, und es gibt nichts anzuordnen. Bei Vektoren und Matrizen muss man festlegen, in welcher Form die vielen partiellen Ableitungen aufgeschrieben werden: als Spalte oder als Zeile, als $m\times n$- oder als $n\times m$-Matrix. Eine solche Festlegung heißt __Layout-Konvention__. Mathematisch ist jede Wahl gleich gut; man muss sie nur durchhalten, sonst erscheinen Formeln plötzlich transponiert.

:::definition Definition 7.1 (Layout-Konvention dieses Kapitels)
<span class="anker" id="satz-7-1"></span>

<ol class="rm">

<li>

Vektoren sind Spalten. Der Gradient einer Funktion $f:\mathbb{R}^n\to\mathbb{R}$ ist eine Spalte mit derselben Form wie $\mathbf{x}$.

</li>

<li>

Die Jacobi-Matrix einer Funktion $\mathbf{g}:\mathbb{R}^n\to\mathbb{R}^m$ ist eine $m\times n$-Matrix: eine Zeile je Ausgang, eine Spalte je Eingang.

</li>

<li>

Die Ableitung einer Funktion $f:\mathbb{R}^{m\times n}\to\mathbb{R}$ nach einer Matrix $\mathbf{A}$ ist eine $m\times n$-Matrix $\nabla_{\mathbf{A}}f$ mit dem Eintrag $\partial f/\partial a_{ij}$ an der Stelle $(i,j)$, also mit derselben Form wie $\mathbf{A}$.

</li>

</ol>
:::

Tabelle [2](#tab-2) fasst das zusammen. Zwei Folgerungen hat das Kapitel schon benutzt: Für eine Funktion mit einem Ausgang ist die Jacobi-Matrix der Gradient als Zeile, $\mathbf{J}_f=\nabla f^{\top}$. Und die Kettenregel für Gradienten braucht die Transponierte, $\nabla(f\circ\mathbf{g})=\mathbf{J}_{\mathbf{g}}^{\top}\nabla f$. Regel (iii) wird in Abschnitt [7.5](#stufe-7-5) gebraucht: Wer eine Matrix um eine kleine Matrix $\mathbf E$ verändert, will $\nabla_{\mathbf{A}}f$ und $\mathbf E$ Eintrag für Eintrag vergleichen können.

<span class="anker" id="tab-2"></span>

**Tabelle 2:** Die Form der Ableitung je nach Art der Funktion, in der Konvention dieses Kapitels.

| Funktion | Ableitung | Form |
|---|---|---|
| $f:\mathbb{R}\to\mathbb{R}$ | $f'(x)$ | Zahl |
| $f:\mathbb{R}^n\to\mathbb{R}$ | $\nabla f(\mathbf{x})$ | Spalte, $n\times1$ (wie $\mathbf{x}$) |
| $\mathbf{g}:\mathbb{R}^n\to\mathbb{R}^m$ | $\mathbf{J}_{\mathbf{g}}(\mathbf{x})$ | $m\times n$ (Zeile $i$ ist $\nabla g_i^{\top}$) |
| $f:\mathbb{R}^{m\times n}\to\mathbb{R}$ | $\nabla_{\mathbf{A}}f(\mathbf{A})$ | $m\times n$ (wie $\mathbf{A}$) |

::::beispiel [Rechenbeispiel]
Für $f(\mathbf{x})=x_1^2x_2+x_2^2$ an der Stelle $(1,\,2)$ ist der Gradient die Spalte $\nabla f=(4,\,5)^{\top}$ und die Jacobi-Matrix die Zeile $\mathbf{J}_f=(4\ \ 5)$. Für $\mathbf{g}$ aus [(5.1)](die-jacobi-matrix.html#gl-5-1) ist $\mathbf{J}_{\mathbf{g}}$ eine $2\times2$-Matrix, deren erste Zeile $(2\ \ 1)$ der Gradient von $g_1=x_1x_2$ als Zeile ist.
::::

⁠**Kurz gesagt:** Im Kapitel hat ein Gradient die Form seiner Variablen, und eine Jacobi-Matrix hat eine Zeile je Ausgang; daraus folgen $\mathbf{J}_f=\nabla f^{\top}$ und die Transponierte in der Kettenregel für Gradienten.

:::hintergrund Andere Konventionen in der Literatur
Viele Bücher schreiben den Gradienten als Zeile. Dann ist er dasselbe wie die Jacobi-Matrix einer Funktion mit einem Ausgang, und die Kettenregel kommt ganz ohne Transponieren aus, denn $\nabla(f\circ\mathbf{g})=\nabla f\,\mathbf{J}_{\mathbf{g}}$ ist dann ein Produkt aus Zeile und Matrix. Der Preis ist, dass der Gradient nicht mehr die Form von $\mathbf{x}$ hat; die Gerade $\mathbf{x}+t\,\nabla f$ in Richtung des steilsten Anstiegs braucht dann ein Transponieren. Man unterscheidet zwei Anordnungen: Im Zähler-Layout richten sich die Zeilen nach den Komponenten der Funktion, wie bei der Jacobi-Matrix dieses Kapitels. Im Nenner-Layout richten sie sich nach den Komponenten der Variablen; dann ist die Ableitung einer vektorwertigen Funktion die Transponierte der Jacobi-Matrix. Dieses Kapitel benutzt eine verbreitete Mischform, Gradient als Spalte und Jacobi-Matrix im Zähler-Layout. Formeln aus verschiedenen Quellen darf man deshalb nicht ungeprüft kombinieren. Eine schnelle Probe ist die Form: Ein Gradient nach $\mathbf{x}\in\mathbb{R}^n$ muss $n$ Einträge in einer Spalte haben. Eine zuverlässigere Probe ist ein kleines Zahlenbeispiel.
:::

### Lineare Funktionen

<span class="anker" id="stufe-7-2"></span>

Die einfachste Funktion vieler Variablen ist die gewichtete Summe. Ihr Gradient ist so einfach, dass man ihn sofort hinschreiben kann; die Herleitung zeigt das Muster, nach dem alle weiteren Formeln dieses Abschnitts entstehen.

:::satz Satz 7.2 (Gradienten linearer Funktionen)
<span class="anker" id="satz-7-2"></span>

Für feste Vektoren $\mathbf{a},\mathbf{y}$ und eine feste Matrix $\mathbf{A}$ passender Form gilt

<span class="anker" id="gl-7-1"></span>
$$\nabla_{\mathbf{x}}(\mathbf{a}^{\top}\mathbf{x})=\nabla_{\mathbf{x}}(\mathbf{x}^{\top}\mathbf{a})=\mathbf{a},\qquad \nabla_{\mathbf{x}}(\mathbf{y}^{\top}\mathbf{A}\mathbf{x})=\mathbf{A}^{\top}\mathbf{y} . \tag{7.1}$$
:::

:::beweis Gradienten linearer Funktionen
Es ist $\mathbf{a}^{\top}\mathbf{x}=\sum_ja_jx_j$. Nach $x_k$ abgeleitet bleibt nur der Summand mit $j=k$, also $a_k$. Wegen $\mathbf{x}^{\top}\mathbf{a}=\mathbf{a}^{\top}\mathbf{x}$ gilt dasselbe für $\mathbf{x}^{\top}\mathbf{a}$. Für den zweiten Teil setzt man $\mathbf{a}=\mathbf{A}^{\top}\mathbf{y}$, denn $\mathbf{y}^{\top}\mathbf{A}\mathbf{x}=(\mathbf{A}^{\top}\mathbf{y})^{\top}\mathbf{x}$.
:::

::::beispiel [Rechenbeispiel]
In [Kapitel 1, Abschnitt 2.2](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-skalarprodukt.html#stufe-2-2), war für Wohnung 1 mit $\mathbf{x}_1=(60,\,2,\,3)^{\top}$ und den Gewichten $\mathbf{w}=(3,\,10,\,-4)^{\top}$ die Vorhersage $\hat y_1=\mathbf{w}^{\top}\mathbf{x}_1=188$. Als Funktion der Gewichte hat sie den Gradienten $\nabla_{\mathbf{w}}\hat y_1=\mathbf{x}_1=(60,\,2,\,3)^{\top}$. Erhöht man $w_1$ um $0{,}1$, so steigt die Vorhersage um $60\cdot0{,}1=6$ auf $194$; tatsächlich ist $3{,}1\cdot60+10\cdot2-4\cdot3=194$. Der Grund ist einfach: Jedes Gewicht wird mit seinem Merkmal multipliziert, und deshalb ist die Empfindlichkeit nach einem Gewicht genau das zugehörige Merkmal.
::::

⁠**Kurz gesagt:** Der Gradient von $\mathbf{a}^{\top}\mathbf{x}$ nach $\mathbf{x}$ ist $\mathbf{a}$, der von $\mathbf{y}^{\top}\mathbf{A}\mathbf{x}$ ist $\mathbf{A}^{\top}\mathbf{y}$.

### Quadratische Formen

<span class="anker" id="stufe-7-3"></span>

Quadratische Formen $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}$ aus [Kapitel 2, Abschnitt 5](/wissen/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/quadratische-formen.html#stufe-5), kommen überall vor, wo Quadrate summiert werden. Beim Ableiten taucht $\mathbf{x}$ an zwei Stellen auf, und beide tragen bei, wie die beiden Wege in Abschnitt [6.2](die-kettenregel-fur-mehrere-variablen.html#stufe-6-2).

:::satz Satz 7.3 (Gradient einer quadratischen Form)
<span class="anker" id="satz-7-3"></span>

Für eine Matrix $\mathbf{A}\in\mathbb{R}^{n\times n}$ gilt

<span class="anker" id="gl-7-2"></span>
$$\nabla_{\mathbf{x}}(\mathbf{x}^{\top}\mathbf{A}\mathbf{x})=(\mathbf{A}+\mathbf{A}^{\top})\,\mathbf{x} . \tag{7.2}$$

Ist $\mathbf{A}$ symmetrisch, so ist das $2\mathbf{A}\mathbf{x}$. Insbesondere ist $\nabla\lVert\mathbf{x}\rVert^2=\nabla(\mathbf{x}^{\top}\mathbf{x})=2\mathbf{x}$.
:::

:::beweis Gradient einer quadratischen Form
Es ist $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=\sum_{i=1}^n\sum_{j=1}^nx_i\,a_{ij}\,x_j$. Leitet man nach $x_k$ ab, tragen zwei Gruppen von Summanden bei: die mit $i=k$, deren Ableitung $\sum_ja_{kj}x_j=(\mathbf{A}\mathbf{x})_k$ ist, und die mit $j=k$, deren Ableitung $\sum_ix_ia_{ik}=(\mathbf{A}^{\top}\mathbf{x})_k$ ist. Der Summand mit $i=j=k$ ist $a_{kk}x_k^2$ und hat die Ableitung $2a_{kk}x_k$; er ist in beiden Gruppen je einmal mit $a_{kk}x_k$ enthalten. Also ist die Komponente $k$ des Gradienten $(\mathbf{A}\mathbf{x})_k+(\mathbf{A}^{\top}\mathbf{x})_k$.
:::

Nach [Kapitel 2, Abschnitt 5.2](/wissen/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/quadratische-formen.html#stufe-5-2), hängt die quadratische Form nur vom symmetrischen Anteil $\mathbf{S}=\tfrac12(\mathbf{A}+\mathbf{A}^{\top})$ ab. Die Formel passt dazu: $(\mathbf{A}+\mathbf{A}^{\top})\mathbf{x}=2\mathbf{S}\mathbf{x}$.

::::beispiel [Rechenbeispiel]
Für $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\0&3\end{smallmatrix}\bigr)$ ist $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=x_1^2+2x_1x_2+3x_2^2$, an der Stelle $\mathbf{x}=(1,\,1)^{\top}$ also $6$. Nach [(7.2)](#gl-7-2) ist

$$\nabla f(1,1)=(\mathbf{A}+\mathbf{A}^{\top})\mathbf{x}=\begin{pmatrix}2&2\\2&6\end{pmatrix}\begin{pmatrix}1\\1\end{pmatrix}=\begin{pmatrix}2+2\\2+6\end{pmatrix}=\begin{pmatrix}4\\8\end{pmatrix}.$$

Probe mit den partiellen Ableitungen $2x_1+2x_2=4$ und $2x_1+6x_2=8$. Die Formel $2\mathbf{A}\mathbf{x}=(6,\,6)^{\top}$, die nur für symmetrische Matrizen gilt, wäre hier falsch.
::::

⁠**Kurz gesagt:** Der Gradient von $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}$ ist $(\mathbf{A}+\mathbf{A}^{\top})\mathbf{x}$, für symmetrisches $\mathbf{A}$ also $2\mathbf{A}\mathbf{x}$, und der von $\lVert\mathbf{x}\rVert^2$ ist $2\mathbf{x}$.

### Die Quadratsumme eines Residuums

<span class="anker" id="stufe-7-4"></span>

In [Kapitel 2, Abschnitt 3](/wissen/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/die-beste-naherungslosung.html#stufe-3), war das Residuum $\mathbf{r}=\mathbf{y}-\mathbf{A}\mathbf{x}$ der Fehlervektor eines Gleichungssystems $\mathbf{A}\mathbf{x}=\mathbf{y}$, das keine Lösung hat, und gesucht war das $\mathbf{x}$ mit dem kürzesten Residuum. Die Quadratsumme $\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert^2$ ist eine Funktion von $\mathbf{x}$, und ihr Gradient sagt, wie sie auf eine Änderung von $\mathbf{x}$ reagiert.

:::satz Satz 7.4 (Gradient der Quadratsumme)
<span class="anker" id="satz-7-4"></span>

Für $f(\mathbf{x})=\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert^2$ mit $\mathbf{A}\in\mathbb{R}^{m\times n}$ und $\mathbf{y}\in\mathbb{R}^m$ gilt

<span class="anker" id="gl-7-3"></span>
$$\nabla f(\mathbf{x})=-2\mathbf{A}^{\top}(\mathbf{y}-\mathbf{A}\mathbf{x})=2\mathbf{A}^{\top}(\mathbf{A}\mathbf{x}-\mathbf{y}). \tag{7.3}$$
:::

:::beweis Gradient der Quadratsumme
Die Funktion ist eine Verkettung: Zuerst bildet die affine Abbildung $\mathbf{r}(\mathbf{x})=\mathbf{y}-\mathbf{A}\mathbf{x}$ das Residuum, dann bildet $\mathbf{r}\mapsto\lVert\mathbf{r}\rVert^2$ seine Quadratsumme. Nach Abschnitt [5.4](die-jacobi-matrix.html#stufe-5-4) ist $\mathbf{J}_{\mathbf{r}}=-\mathbf{A}$, nach [(7.2)](#gl-7-2) ist $\nabla_{\mathbf{r}}\lVert\mathbf{r}\rVert^2=2\mathbf{r}$. Die Kettenregel [(6.3)](die-kettenregel-fur-mehrere-variablen.html#gl-6-3) ergibt $\nabla f=(-\mathbf{A})^{\top}\,2\mathbf{r}=-2\mathbf{A}^{\top}\mathbf{r}$.
:::

::::beispiel [Rechenbeispiel]
Es sei $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\0&1\end{smallmatrix}\bigr)$, $\mathbf{y}=(1,\,0)^{\top}$ und $\mathbf{x}=(2,\,1)^{\top}$. Dann ist $\mathbf{A}\mathbf{x}=(4,\,1)^{\top}$, das Residuum $\mathbf{r}=(-3,\,-1)^{\top}$ und $f(\mathbf{x})=9+1=10$. Mit $\mathbf{A}^{\top}\mathbf{r}=(-3,\,-7)^{\top}$ ist

$$\nabla f(\mathbf{x})=-2\mathbf{A}^{\top}\mathbf{r}=-2\begin{pmatrix}-3\\-7\end{pmatrix}=\begin{pmatrix}6\\14\end{pmatrix}$$

(Abb. [13](#abb-13)). Probe: Ausgeschrieben ist $f(\mathbf{x})=(1-x_1-2x_2)^2+x_2^2$ mit den partiellen Ableitungen $-2\,(1-x_1-2x_2)=6$ und $-4\,(1-x_1-2x_2)+2x_2=12+2=14$.

:::abbildung ml/k3rresiduum 13
Der Gradient der Quadratsumme $\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert^2$: Jede Komponente von $\mathbf{A}^{\top}\mathbf{r}$ ist das Skalarprodukt einer Spalte von $\mathbf{A}$ mit dem Residuum.
:::
::::

Die Formel verbindet sich mit [Kapitel 2](/wissen/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/projektion-eigenwerte-und-zerlegungen.html). Dort stand das Residuum der besten Näherungslösung $\hat{\mathbf{x}}$ senkrecht auf allen Spalten von $\mathbf{A}$, also $\mathbf{A}^{\top}\hat{\mathbf{r}}=\mathbf{0}$, und daraus folgten die Normalgleichungen $\mathbf{A}^{\top}\mathbf{A}\hat{\mathbf{x}}=\mathbf{A}^{\top}\mathbf{y}$. Nach [(7.3)](#gl-7-3) heißt das: An der Stelle $\hat{\mathbf{x}}$ ist der Gradient der Quadratsumme null, sie steigt und fällt dort in keiner Richtung, bis auf Glieder zweiter Ordnung. Für das Beispiel aus [Kapitel 2, Abschnitt 3.3](/wissen/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/die-beste-naherungslosung.html#stufe-3-3), mit der Matrix $\mathbf{A}=\Bigl(\begin{smallmatrix}1&0\\0&1\\1&1\end{smallmatrix}\Bigr)$, $\mathbf{y}=(1,\,1,\,1)^{\top}$ und $\hat{\mathbf{x}}=(\tfrac23,\,\tfrac23)^{\top}$ ist $\hat{\mathbf{r}}=(\tfrac13,\,\tfrac13,\,-\tfrac13)^{\top}$ und $\mathbf{A}^{\top}\hat{\mathbf{r}}=(\tfrac13-\tfrac13,\ \tfrac13-\tfrac13)^{\top}=\mathbf{0}$.

⁠**Kurz gesagt:** Der Gradient von $\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert^2$ ist $-2\mathbf{A}^{\top}(\mathbf{y}-\mathbf{A}\mathbf{x})$; er verschwindet genau dort, wo das Residuum senkrecht auf den Spalten von $\mathbf{A}$ steht.

### Ableiten nach einer Matrix

<span class="anker" id="stufe-7-5"></span>

Manchmal ist nicht ein Vektor die Variable, sondern eine ganze Matrix: Wie ändert sich eine Zahl, wenn man einen Eintrag einer Matrix verändert? Nach Regel (iii) der Konvention ordnet man die $m\cdot n$ partiellen Ableitungen in der Form der Matrix an. Dann gilt die lineare Näherung wie gewohnt, nur dass das Skalarprodukt über alle Einträge läuft:

<span class="anker" id="gl-7-4"></span>
$$f(\mathbf{A}+\mathbf E)\approx f(\mathbf{A})+\sum_{i=1}^m\sum_{j=1}^n\bigl(\nabla_{\mathbf{A}}f\bigr)_{ij}\,e_{ij} \tag{7.4}$$

für eine kleine Matrix $\mathbf E$ mit den Einträgen $e_{ij}$. Die Doppelsumme ist dasselbe wie $\operatorname{spur}\bigl((\nabla_{\mathbf{A}}f)^{\top}\mathbf E\bigr)$ mit der Spur aus [Kapitel 2, Abschnitt 6.5](/wissen/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/eigenwerte-und-eigenvektoren.html#stufe-6-5).

:::satz Satz 7.5 (Zwei Ableitungen nach einer Matrix)
<span class="anker" id="satz-7-5"></span>

Für feste Vektoren $\mathbf{u}\in\mathbb{R}^m$, $\mathbf{v}\in\mathbb{R}^n$ und eine Matrix $\mathbf{A}\in\mathbb{R}^{m\times n}$ gilt

<span class="anker" id="gl-7-5"></span>
$$\nabla_{\mathbf{A}}(\mathbf{u}^{\top}\mathbf{A}\mathbf{v})=\mathbf{u}\mathbf{v}^{\top},\qquad \nabla_{\mathbf{A}}\lVert\mathbf{A}\rVert_F^2=2\mathbf{A} . \tag{7.5}$$

Dabei ist $\lVert\mathbf{A}\rVert_F$ die Frobeniusnorm aus [Kapitel 2, Abschnitt 10.1](/wissen/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/naherung-durch-matrizen-von-kleinem-rang.html#stufe-10-1).
:::

:::beweis Zwei Ableitungen nach einer Matrix
Es ist $\mathbf{u}^{\top}\mathbf{A}\mathbf{v}=\sum_i\sum_ju_i\,a_{ij}\,v_j$. Der Eintrag $a_{ij}$ kommt in genau einem Summanden vor, mit dem Faktor $u_iv_j$. Also ist $\partial(\mathbf{u}^{\top}\mathbf{A}\mathbf{v})/\partial a_{ij}=u_iv_j$, und das ist der Eintrag $(i,j)$ des äußeren Produkts $\mathbf{u}\mathbf{v}^{\top}$ aus [Kapitel 1, Abschnitt 9.5](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrixprodukt.html#stufe-9-5). Ebenso ist $\lVert\mathbf{A}\rVert_F^2=\sum_{i,j}a_{ij}^2$ und $\partial/\partial a_{ij}$ davon $2a_{ij}$.
:::

::::beispiel [Rechenbeispiel]
Für $\mathbf{u}=(1,\,2)^{\top}$ und $\mathbf{v}=(3,\,-1)^{\top}$ ist

$$\nabla_{\mathbf{A}}(\mathbf{u}^{\top}\mathbf{A}\mathbf{v})=\mathbf{u}\mathbf{v}^{\top}=\begin{pmatrix}3&-1\\6&-2\end{pmatrix},$$

an jeder Stelle $\mathbf{A}$, denn die Funktion ist linear in $\mathbf{A}$. Für $\mathbf{A}=\mathbf{I}$ ist $\mathbf{u}^{\top}\mathbf{A}\mathbf{v}=\mathbf{u}^{\top}\mathbf{v}=3-2=1$. Vergrößert man den Eintrag $a_{21}$ um $0{,}1$, so sagt der Gradient eine Änderung um $6\cdot0{,}1=0{,}6$ voraus. Tatsächlich kommt $a_{21}$ nur im Summanden $u_2\,a_{21}\,v_1=2\cdot a_{21}\cdot3$ vor, und der wächst um $0{,}6$.
::::

⁠**Kurz gesagt:** Die Ableitung einer Zahl nach einer Matrix hat die Form der Matrix; für $\mathbf{u}^{\top}\mathbf{A}\mathbf{v}$ ist sie das äußere Produkt $\mathbf{u}\mathbf{v}^{\top}$, für $\lVert\mathbf{A}\rVert_F^2$ ist sie $2\mathbf{A}$.

### Rückwärts durch ein Matrixprodukt

<span class="anker" id="stufe-7-6"></span>

Oft ist ein Matrix-Vektor-Produkt $\mathbf{y}=\mathbf{A}\mathbf{x}$ nur ein Zwischenschritt einer längeren Rechnung, an deren Ende eine Zahl $f(\mathbf{y})$ steht. Kennt man schon, wie diese Zahl auf $\mathbf{y}$ reagiert, also $\nabla f(\mathbf{y})$, so will man daraus ablesen, wie sie auf $\mathbf{A}$ und auf $\mathbf{x}$ reagiert. Diese Rechnung rückwärts durch einen Baustein ist das Muster für den Rückwärtsmodus in Abschnitt [10](automatische-differentiation.html#stufe-10).

:::satz Satz 7.6 (Rückwärtsregel des Matrixprodukts)
<span class="anker" id="satz-7-6"></span>

Es sei $f:\mathbb{R}^m\to\mathbb{R}$ differenzierbar, $\mathbf{y}=\mathbf{A}\mathbf{x}$ mit $\mathbf{A}\in\mathbb{R}^{m\times n}$ und $F(\mathbf{A},\mathbf{x})=f(\mathbf{A}\mathbf{x})$. Dann gilt

<span class="anker" id="gl-7-6"></span>
$$\nabla_{\mathbf{A}}F=\nabla f(\mathbf{y})\,\mathbf{x}^{\top},\qquad \nabla_{\mathbf{x}}F=\mathbf{A}^{\top}\,\nabla f(\mathbf{y}). \tag{7.6}$$

Allgemeiner gilt für $\mathbf{C}=\mathbf{A}\mathbf{B}$ und $F(\mathbf{A},\mathbf{B})=f(\mathbf{C})$: $\nabla_{\mathbf{A}}F=(\nabla_{\mathbf{C}}f)\,\mathbf{B}^{\top}$ und $\nabla_{\mathbf{B}}F=\mathbf{A}^{\top}\,(\nabla_{\mathbf{C}}f)$.
:::

:::beweis Rückwärtsregel des Matrixprodukts
Es ist $y_i=\sum_ka_{ik}x_k$. Der Eintrag $a_{ij}$ beeinflusst nur $y_i$, und zwar mit dem Faktor $\partial y_i/\partial a_{ij}=x_j$. Es gibt also nur einen Weg von $a_{ij}$ zu $f$, und $\partial F/\partial a_{ij}=\frac{\partial f}{\partial y_i}\,x_j$; das ist der Eintrag $(i,j)$ von $\nabla f(\mathbf{y})\,\mathbf{x}^{\top}$. Die Variable $x_j$ dagegen beeinflusst jedes $y_i$, mit dem Faktor $a_{ij}$; über alle Wege summiert ist $\partial F/\partial x_j=\sum_i\frac{\partial f}{\partial y_i}\,a_{ij}$, die Komponente $j$ von $\mathbf{A}^{\top}\nabla f(\mathbf{y})$. Die zweite Aussage folgt ebenso, weil $\mathbf{C}=\mathbf{A}\mathbf{B}$ Spalte für Spalte ein Matrix-Vektor-Produkt ist.
:::

::::beispiel [Rechenbeispiel]
In [Kapitel 1, Abschnitt 7.1](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrix-vektor-produkt.html#stufe-7-1), war $\mathbf{A}=\Bigl(\begin{smallmatrix}1&2\\0&-1\\3&1\end{smallmatrix}\Bigr)$ und $\mathbf{x}=(2,\,1)^{\top}$, also $\mathbf{y}=\mathbf{A}\mathbf{x}=(4,\,-1,\,7)^{\top}$. Es sei $f(\mathbf{y})=y_1-y_3=-3$, also $\nabla f(\mathbf{y})=(1,\,0,\,-1)^{\top}$. Nach [(7.6)](#gl-7-6) ist

$$\nabla_{\mathbf{A}}F=\begin{pmatrix}1\\0\\-1\end{pmatrix}\begin{pmatrix}2&1\end{pmatrix}=\begin{pmatrix}2&1\\0&0\\-2&-1\end{pmatrix},\qquad \nabla_{\mathbf{x}}F=\mathbf{A}^{\top}\begin{pmatrix}1\\0\\-1\end{pmatrix}=\begin{pmatrix}-2\\1\end{pmatrix}$$

(Abb. [14](#abb-14)). Probe: Ausgeschrieben ist $F=(x_1+2x_2)-(3x_1+x_2)=-2x_1+x_2$ mit dem Gradienten $(-2,\,1)^{\top}$. Die zweite Zeile von $\nabla_{\mathbf{A}}F$ ist null, weil $y_2$ in $f$ nicht vorkommt; die Einträge der zweiten Zeile von $\mathbf{A}$ wirken nur auf $y_2$.

:::abbildung ml/k3rrueck 14
Der Gradient nach dem Eingang eines Matrix-Vektor-Produkts: Jede Komponente sammelt über alle drei Ausgänge $y_i$, wie stark $f$ auf $y_i$ reagiert, gewichtet mit dem Faktor $a_{ij}$, mit dem $x_j$ auf $y_i$ wirkt.
:::
::::

:::warnung Die Formprobe ist eine Merkhilfe, kein Beweis
Die Formen legen [(7.6)](#gl-7-6) fast fest: $\nabla_{\mathbf{A}}F$ muss die Form $m\times n$ haben, und aus der Spalte $\nabla f(\mathbf{y})$ mit $m$ Einträgen und der Spalte $\mathbf{x}$ mit $n$ Einträgen ergibt nur $\nabla f(\mathbf{y})\,\mathbf{x}^{\top}$ diese Form. Man kann sich die Regel so merken. Die Formprobe erkennt aber weder ein falsches Vorzeichen noch einen fehlenden Faktor noch eine vertauschte Reihenfolge bei quadratischen Matrizen. Begründet ist die Regel erst durch die Rechnung mit den Komponenten.
:::

⁠**Kurz gesagt:** Rückwärts durch $\mathbf{y}=\mathbf{A}\mathbf{x}$: Der Gradient nach $\mathbf{A}$ ist $\nabla f(\mathbf{y})\,\mathbf{x}^{\top}$, der nach $\mathbf{x}$ ist $\mathbf{A}^{\top}\nabla f(\mathbf{y})$.

:::aufgabe Aufgabe 24 ★ Gradienten in Matrixschreibweise
<span class="anker" id="aufg-24"></span>

Berechne mit den Formeln dieses Abschnitts und mache jeweils die Probe mit den partiellen Ableitungen.

<ol class="al">

<li>

$f(\mathbf{x})=\mathbf{b}^{\top}\mathbf{x}+5$ mit $\mathbf{b}=(2,\,-1,\,4)^{\top}$;

</li>

<li>

$f(\mathbf{x})=\lVert\mathbf{x}\rVert^2$ an der Stelle $(1,\,-1,\,2)$;

</li>

<li>

$f(\mathbf{x})=\mathbf{x}^{\top}\mathbf{A}\mathbf{x}$ mit $\mathbf{A}=\bigl(\begin{smallmatrix}2&1\\3&4\end{smallmatrix}\bigr)$ an der Stelle $(1,\,-1)$.

</li>

</ol>

:::loesung
(a) Nach [(7.1)](#gl-7-1) ist $\nabla f=\mathbf{b}=(2,\,-1,\,4)^{\top}$. Probe: $f=2x_1-x_2+4x_3+5$.

(b) Nach [(7.2)](#gl-7-2) mit $\mathbf{A}=\mathbf{I}$ ist $\nabla f=2\mathbf{x}=(2,\,-2,\,4)^{\top}$. Probe: $\partial_jf=2x_j$.

(c) $\mathbf{A}+\mathbf{A}^{\top}=\bigl(\begin{smallmatrix}4&4\\4&8\end{smallmatrix}\bigr)$, also $\nabla f(1,-1)=(4-4,\ 4-8)^{\top}=(0,\,-4)^{\top}$. Probe: $f=2x_1^2+4x_1x_2+4x_2^2$ hat die partiellen Ableitungen $4x_1+4x_2=0$ und $4x_1+8x_2=-4$.
:::
:::

:::aufgabe Aufgabe 25 ★★ Die Ausgleichsgerade aus Kapitel 2
<span class="anker" id="aufg-25"></span>

In [Kapitel 2, Abschnitt 3.6](/wissen/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/die-beste-naherungslosung.html#stufe-3-6), wurde eine Gerade durch die Punkte $(0,\,1)$, $(1,\,2)$ und $(2,\,4)$ gelegt, mit $\mathbf{A}=\Bigl(\begin{smallmatrix}1&0\\1&1\\1&2\end{smallmatrix}\Bigr)$ und $\mathbf{y}=(1,\,2,\,4)^{\top}$.

<ol class="al">

<li>

Berechne $f(\mathbf{x})=\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert^2$ und $\nabla f(\mathbf{x})$ an der Stelle $\mathbf{x}=(1,\,1)^{\top}$.

</li>

<li>

In welche Richtung sollte man $\mathbf{x}$ von $(1,\,1)$ aus ein kleines Stück verschieben, damit $f$ am schnellsten kleiner wird?

</li>

<li>

Zeige, dass der Gradient an der Stelle $\hat{\mathbf{x}}=(\tfrac56,\,\tfrac32)^{\top}$ aus [Kapitel 2](/wissen/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/projektion-eigenwerte-und-zerlegungen.html) null ist.

</li>

</ol>

:::loesung
(a) $\mathbf{A}\mathbf{x}=(1,\,2,\,3)^{\top}$, $\mathbf{r}=\mathbf{y}-\mathbf{A}\mathbf{x}=(0,\,0,\,1)^{\top}$ und $f=1$. Mit $\mathbf{A}^{\top}\mathbf{r}=(0+0+1,\ 0+0+2)^{\top}=(1,\,2)^{\top}$ ist $\nabla f=-2\mathbf{A}^{\top}\mathbf{r}=(-2,\,-4)^{\top}$.

(b) Am schnellsten fällt $f$ in Richtung $-\nabla f/\lVert\nabla f\rVert=(2,\,4)^{\top}/\sqrt{20}=(1,\,2)^{\top}/\sqrt5\approx(0{,}447;\ 0{,}894)^{\top}$: Der Achsenabschnitt soll etwas, die Steigung doppelt so stark wachsen. Das passt dazu, dass die Gerade $1+t$ den dritten Punkt $(2,\,4)$ um $1$ verfehlt.

(c) $\mathbf{A}\hat{\mathbf{x}}=(\tfrac56,\ \tfrac73,\ \tfrac{23}6)^{\top}$, also $\hat{\mathbf{r}}=(\tfrac16,\ -\tfrac13,\ \tfrac16)^{\top}$ und

$$\mathbf{A}^{\top}\hat{\mathbf{r}}=\begin{pmatrix}\tfrac16-\tfrac13+\tfrac16\\0-\tfrac13+\tfrac26\end{pmatrix}=\begin{pmatrix}0\\0\end{pmatrix}.$$

Der Gradient ist null: An der besten Näherungslösung ändert keine kleine Verschiebung die Quadratsumme in erster Ordnung.
:::
:::

:::aufgabe Aufgabe 26 ★★ Ableitungen nach einer Matrix
<span class="anker" id="aufg-26"></span>

<ol class="al">

<li>

Zeige $\nabla_{\mathbf{A}}\operatorname{spur}\mathbf{A}=\mathbf{I}$ für quadratisches $\mathbf{A}$.

</li>

<li>

Zeige mit [(7.6)](#gl-7-6) und $\nabla\lVert\mathbf{y}\rVert^2=2\mathbf{y}$, dass $\nabla_{\mathbf{A}}\lVert\mathbf{A}\mathbf{x}\rVert^2=2\,(\mathbf{A}\mathbf{x})\,\mathbf{x}^{\top}$ ist, und berechne das für $\mathbf{A}=\mathbf{I}\in\mathbb{R}^{2\times2}$ und $\mathbf{x}=(1,\,2)^{\top}$.

</li>

<li>

Prüfe (b) mit der linearen Näherung [(7.4)](#gl-7-4): Um wie viel ändert sich $\lVert\mathbf{A}\mathbf{x}\rVert^2$ ungefähr, wenn man $a_{12}$ von $0$ auf $0{,}01$ erhöht? Rechne nach.

</li>

</ol>

:::loesung
(a) $\operatorname{spur}\mathbf{A}=\sum_ia_{ii}$. Die Ableitung nach $a_{ij}$ ist $1$ für $i=j$ und $0$ sonst; in der Form von $\mathbf{A}$ angeordnet ist das $\mathbf{I}$.

(b) Es ist $\lVert\mathbf{A}\mathbf{x}\rVert^2=f(\mathbf{y})$ mit $\mathbf{y}=\mathbf{A}\mathbf{x}$ und $\nabla f(\mathbf{y})=2\mathbf{y}$. Nach [(7.6)](#gl-7-6) ist $\nabla_{\mathbf{A}}\lVert\mathbf{A}\mathbf{x}\rVert^2=2\mathbf{y}\,\mathbf{x}^{\top}=2\,(\mathbf{A}\mathbf{x})\,\mathbf{x}^{\top}$. Für $\mathbf{A}=\mathbf{I}$ und $\mathbf{x}=(1,\,2)^{\top}$:

$$\nabla_{\mathbf{A}}\lVert\mathbf{A}\mathbf{x}\rVert^2=2\begin{pmatrix}1\\2\end{pmatrix}\begin{pmatrix}1&2\end{pmatrix}=\begin{pmatrix}2&4\\4&8\end{pmatrix}.$$

(c) Der Eintrag $(1,2)$ des Gradienten ist $4$, also sagt [(7.4)](#gl-7-4) eine Änderung um etwa $4\cdot0{,}01=0{,}04$ voraus. Genau: Mit $a_{12}=0{,}01$ ist $\mathbf{A}\mathbf{x}=(1{,}02;\ 2)^{\top}$ und $\lVert\mathbf{A}\mathbf{x}\rVert^2=1{,}0404+4=5{,}0404$, also eine Änderung um $0{,}0404$ gegenüber $5$.
:::
:::

:::aufgabe Aufgabe 27 ★★★ Die Rückwärtsregel für ein Produkt zweier Matrizen
<span class="anker" id="aufg-27"></span>

Es sei $\mathbf{C}=\mathbf{A}\mathbf{B}$ und $F(\mathbf{A},\mathbf{B})=f(\mathbf{C})$ mit $\mathbf G=\nabla_{\mathbf{C}}f$.

<ol class="al">

<li>

Zeige komponentenweise $\nabla_{\mathbf{A}}F=\mathbf G\mathbf{B}^{\top}$ und $\nabla_{\mathbf{B}}F=\mathbf{A}^{\top}\mathbf G$.

</li>

<li>

Prüfe beide Formeln für $\mathbf{A}=(1\ \ 2)$, $\mathbf{B}=\bigl(\begin{smallmatrix}3\\4\end{smallmatrix}\bigr)$ und $f(\mathbf{C})=c_{11}^2$, indem du $F$ ausschreibst.

</li>

</ol>

:::loesung
(a) Es ist $c_{ik}=\sum_ja_{ij}b_{jk}$. Der Eintrag $a_{ij}$ wirkt auf alle $c_{ik}$ der Zeile $i$, mit dem Faktor $b_{jk}$; über diese Wege summiert ist $\partial F/\partial a_{ij}=\sum_kg_{ik}b_{jk}=(\mathbf G\mathbf{B}^{\top})_{ij}$. Der Eintrag $b_{jk}$ wirkt auf alle $c_{ik}$ der Spalte $k$, mit dem Faktor $a_{ij}$; also ist $\partial F/\partial b_{jk}=\sum_ia_{ij}g_{ik}=(\mathbf{A}^{\top}\mathbf G)_{jk}$.

(b) $\mathbf{C}=1\cdot3+2\cdot4=11$, $F=121$ und $\mathbf G=2c_{11}=22$. Die Formeln ergeben $\nabla_{\mathbf{A}}F=22\,(3\ \ 4)=(66\ \ 88)$ und $\nabla_{\mathbf{B}}F=(1,\,2)^{\top}\cdot22=(22,\,44)^{\top}$. Ausgeschrieben ist $F=(3a_{11}+4a_{12})^2$ mit den Ableitungen $2\cdot11\cdot3=66$ und $2\cdot11\cdot4=88$, und $F=(b_{11}+2b_{21})^2$ mit den Ableitungen $22$ und $44$.
:::
:::

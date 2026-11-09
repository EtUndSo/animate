---
title: Die Singulärwertzerlegung
pfad: Informatik / Machine Learning / Mathematische Grundlagen / Projektion, Eigenwerte und Zerlegungen
knoten: Grundlagen 2: Projektion, Eigenwerte und Zerlegungen
nachschlagen: ja
order: 15221000
summary: Eigenvektoren gibt es nur bei quadratischen Matrizen, und senkrecht aufeinander stehen sie nur bei symmetrischen.
tags: Singulärwerte, rechte Singulärvektoren, linke Singulärvektor, Spektralnorm
lang: de
---

<span class="anker" id="stufe-9"></span>

:::zweck
Eigenvektoren gibt es nur bei quadratischen Matrizen, und senkrecht aufeinander stehen sie nur bei symmetrischen. Dieser Abschnitt zeigt, dass jede Matrix, auch eine rechteckige, ein Paar von rechtwinkligen Achsenkreuzen hat: eines im Raum der Eingänge und eines im Raum der Ausgänge. Die Matrix bildet jede Achse des einen auf ein Vielfaches einer Achse des anderen ab. Daraus wird eine Zerlegung jeder Matrix in Drehung, Streckung und Drehung.
:::

### Senkrechte Richtungen, die senkrecht bleiben

<span class="anker" id="stufe-9-1"></span>

Die Matrix $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ hat als Dreiecksmatrix den doppelten Eigenwert $2$, aber nur eine Eigenrichtung: $(\mathbf{A}-2\mathbf{I})\mathbf{v}=\mathbf{0}$ heißt $3v_2=0$, also kommen nur Vielfache von $\mathbf{e}_1$ in Frage (Aufgabe [19](eigenwerte-und-eigenvektoren.html#aufg-19)). Nach Abschnitt [7.2](diagonalisierung-und-spektralsatz.html#stufe-7-2) ist sie nicht diagonalisierbar. Trotzdem macht sie aus dem Einheitskreis eine Ellipse (Abb. [23](#abb-23)), und eine Ellipse hat zwei senkrechte Achsen. Welche Pfeile des Kreises landen auf diesen Achsen?

Gesucht ist weniger als ein Eigenvektor: Ein Pfeil darf seine Richtung ändern. Gesucht sind zwei senkrechte Einheitsvektoren $\mathbf{v}_1$, $\mathbf{v}_2$, deren Bilder $\mathbf{A}\mathbf{v}_1$ und $\mathbf{A}\mathbf{v}_2$ wieder senkrecht aufeinander stehen. Ob zwei Bilder senkrecht stehen, sagt ihr Skalarprodukt:

$$(\mathbf{A}\mathbf{v}_1)^{\top}(\mathbf{A}\mathbf{v}_2)=\mathbf{v}_1^{\top}\,\mathbf{A}^{\top}\mathbf{A}\,\mathbf{v}_2 .$$

Hier taucht die Gram-Matrix $\mathbf{A}^{\top}\mathbf{A}$ auf. Sie ist symmetrisch, auch wenn $\mathbf{A}$ es nicht ist, und hat nach dem Spektralsatz eine Orthonormalbasis aus Eigenvektoren. Ist $\mathbf{v}_2$ ein Eigenvektor von $\mathbf{A}^{\top}\mathbf{A}$ zum Eigenwert $\lambda_2$ und steht $\mathbf{v}_1$ senkrecht auf $\mathbf{v}_2$, so ist das Skalarprodukt $\lambda_2\,\mathbf{v}_1^{\top}\mathbf{v}_2=0$. Die Eigenvektoren von $\mathbf{A}^{\top}\mathbf{A}$ leisten also das Gewünschte. Dieselbe Rechnung mit $\mathbf{v}_1=\mathbf{v}_2$ liefert die Längen der Bilder: $\lVert\mathbf{A}\mathbf{v}_i\rVert^2=\mathbf{v}_i^{\top}\mathbf{A}^{\top}\mathbf{A}\mathbf{v}_i=\lambda_i$.

::::beispiel [Rechenbeispiel]
Für $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ ist $\mathbf{A}^{\top}\mathbf{A}=\bigl(\begin{smallmatrix}4&6\\6&13\end{smallmatrix}\bigr)$ mit der Spur $17$ und der Determinante $52-36=16$. Das charakteristische Polynom $\lambda^2-17\lambda+16=(\lambda-16)(\lambda-1)$ hat die Nullstellen $16$ und $1$. Normierte Eigenvektoren sind $\mathbf{v}_1=(1,\,2)^{\top}/\sqrt5$ zu $16$ und $\mathbf{v}_2=(-2,\,1)^{\top}/\sqrt5$ zu $1$. Ihre Bilder

$$\mathbf{A}\mathbf{v}_1=\frac1{\sqrt5}\begin{pmatrix}8\\4\end{pmatrix},\qquad \mathbf{A}\mathbf{v}_2=\frac1{\sqrt5}\begin{pmatrix}-1\\2\end{pmatrix}$$

haben das Skalarprodukt $\tfrac15(-8+8)=0$ und die Längen $\sqrt{80/5}=4=\sqrt{16}$ und $1=\sqrt1$ (Abb. [22](#abb-22)).

:::abbildung ml/k2rsvdidee 22
Die Bilder $\mathbf{A}\mathbf{v}_1=(8,4)^{\top}/\sqrt5$ und $\mathbf{A}\mathbf{v}_2=(-1,2)^{\top}/\sqrt5$ stehen senkrecht aufeinander und haben die Längenquadrate $16$ und $1$, die Eigenwerte von $\mathbf{A}^{\top}\mathbf{A}$.
:::
::::

⁠**Kurz gesagt:** Die Eigenvektoren der symmetrischen Matrix $\mathbf{A}^{\top}\mathbf{A}$ sind senkrechte Richtungen, deren Bilder unter $\mathbf{A}$ wieder senkrecht aufeinander stehen; die Bilder haben die Längen $\sqrt{\lambda_i}$.

### Singulärwerte

<span class="anker" id="stufe-9-2"></span>

Die Längen der Bilder sind die wichtigsten Kennzahlen einer Matrix: Sie sagen, wie stark die Matrix in ihren Hauptrichtungen streckt. Nach Abschnitt [8.4](positiv-definite-matrizen.html#stufe-8-4) ist $\mathbf{A}^{\top}\mathbf{A}$ positiv semidefinit, ihre Eigenwerte sind also nicht negativ, und man darf die Wurzel ziehen.

:::definition Definition 9.1 (Singulärwerte)
<span class="anker" id="satz-9-1"></span>

Es sei $\mathbf{A}\in\mathbb{R}^{m\times n}$, und $\lambda_1\ge\lambda_2\ge\dots\ge\lambda_n\ge0$ seien die Eigenwerte von $\mathbf{A}^{\top}\mathbf{A}$, absteigend sortiert und mehrfache mehrfach gezählt. Die Zahlen

<span class="anker" id="gl-9-1"></span>
$$d_j=\sqrt{\lambda_j},\qquad d_1\ge d_2\ge\dots\ge d_n\ge0 , \tag{9.1}$$

heißen die __Singulärwerte__ von $\mathbf{A}$.
:::

Viele Bücher schreiben $\sigma_j$ statt $d_j$. Die Singulärwerte tragen hier immer einen Index; das $d$ ohne Index aus [Grundlagen 1](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/vektoren-und-matrizen.html), die Zahl der Merkmale, ist etwas anderes.

:::satz Satz 9.2 (Singulärwerte und Rang)
<span class="anker" id="satz-9-2"></span>

Die Zahl der Singulärwerte, die nicht null sind, ist der Rang von $\mathbf{A}$.
:::

:::beweis Singulärwerte und Rang
Es seien $\mathbf{v}_1,\dots,\mathbf{v}_n$ orthonormale Eigenvektoren von $\mathbf{A}^{\top}\mathbf{A}$ zu $\lambda_1,\dots,\lambda_n$. Jeder Vektor ist $\mathbf{x}=\sum_jc_j\mathbf{v}_j$, also ist $\mathbf{A}\mathbf{x}=\sum_jc_j\,\mathbf{A}\mathbf{v}_j$: Der Spaltenraum wird von den Bildern $\mathbf{A}\mathbf{v}_1,\dots,\mathbf{A}\mathbf{v}_n$ aufgespannt. Diese stehen nach dem vorigen Unterabschnitt paarweise senkrecht und haben die Längen $d_j$. Die Bilder mit $d_j=0$ sind der Nullvektor und tragen nichts bei. Die übrigen stehen senkrecht aufeinander und sind nicht null; durch ihre Längen geteilt, sind sie orthonormal und nach dem Satz in Abschnitt [1.1](orthonormalbasen-und-orthogonale-matrizen.html#stufe-1-1) linear unabhängig. Sie bilden eine Basis des Spaltenraums, und ihre Zahl ist der Rang.
:::

Den Rang einer Matrix bezeichnet man im Folgenden mit $r$. Es ist $d_1\ge\dots\ge d_r>0$ und $d_{r+1}=\dots=d_n=0$.

::::beispiel [Rechenbeispiel]
$\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ hat die Singulärwerte $d_1=4$ und $d_2=1$ und den Rang $2$. Die Eigenwerte sind $2$ und $2$: Singulärwerte und Eigenwerte sind im Allgemeinen verschiedene Zahlen. Die Matrix $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ hat $\mathbf{A}^{\top}\mathbf{A}=\bigl(\begin{smallmatrix}5&10\\10&20\end{smallmatrix}\bigr)$ mit den Eigenwerten $25$ und $0$, also die Singulärwerte $5$ und $0$ und den Rang $1$.
::::

⁠**Kurz gesagt:** Die Singulärwerte $d_j$ sind die Wurzeln der Eigenwerte von $\mathbf{A}^{\top}\mathbf{A}$; sie messen, wie stark $\mathbf{A}$ in ihren Hauptrichtungen streckt, und die Zahl der positiven ist der Rang.

### Singulärvektoren

<span class="anker" id="stufe-9-3"></span>

Zu jedem positiven Singulärwert gehören zwei Richtungen: eine Eingangsrichtung $\mathbf{v}_j$ und die Richtung ihres Bildes.

:::definition Definition 9.3 (Singulärvektoren)
<span class="anker" id="satz-9-3"></span>

Orthonormale Eigenvektoren $\mathbf{v}_1,\dots,\mathbf{v}_n$ von $\mathbf{A}^{\top}\mathbf{A}$ zu den Eigenwerten $d_1^2,\dots,d_n^2$ heißen __rechte Singulärvektoren__ von $\mathbf{A}$. Für $d_j>0$ heißt

<span class="anker" id="gl-9-2"></span>
$$\mathbf{u}_j=\frac{\mathbf{A}\mathbf{v}_j}{d_j},\qquad\text{also}\qquad \mathbf{A}\mathbf{v}_j=d_j\mathbf{u}_j , \tag{9.2}$$

der zugehörige __linke Singulärvektor__.
:::

Die Namen kommen von der Stelle, an der die Vektoren in der Zerlegung des nächsten Unterabschnitts stehen. Die linken Singulärvektoren sind wieder orthonormal, denn

$$\mathbf{u}_i^{\top}\mathbf{u}_j=\frac{\mathbf{v}_i^{\top}\mathbf{A}^{\top}\mathbf{A}\mathbf{v}_j}{d_id_j}=\frac{d_j^2\,\mathbf{v}_i^{\top}\mathbf{v}_j}{d_id_j},$$

und das ist $1$ für $i=j$ und $0$ sonst. Sie sind die Eigenvektoren von $\mathbf{A}\mathbf{A}^{\top}$, und es gilt die Gleichung in der Gegenrichtung:

$$\mathbf{A}^{\top}\mathbf{u}_j=\frac{\mathbf{A}^{\top}\mathbf{A}\mathbf{v}_j}{d_j}=d_j\mathbf{v}_j,\qquad \mathbf{A}\mathbf{A}^{\top}\mathbf{u}_j=d_j\,\mathbf{A}\mathbf{v}_j=d_j^2\,\mathbf{u}_j .$$

$\mathbf{A}$ bildet $\mathbf{v}_j$ auf $d_j\mathbf{u}_j$ ab, und $\mathbf{A}^{\top}$ bildet $\mathbf{u}_j$ auf $d_j\mathbf{v}_j$ ab.

:::warnung Die Vorzeichen gehören zusammen
Ein Eigenvektor ist nur bis auf das Vorzeichen bestimmt. Berechnet man die $\mathbf{v}_j$ als Eigenvektoren von $\mathbf{A}^{\top}\mathbf{A}$ und getrennt davon die $\mathbf{u}_j$ als Eigenvektoren von $\mathbf{A}\mathbf{A}^{\top}$, so kann ein $\mathbf{u}_j$ das falsche Vorzeichen bekommen, und dann ist $\mathbf{A}\mathbf{v}_j=-d_j\mathbf{u}_j$. Sicher ist der Weg über [(9.2)](#gl-9-2): zuerst $\mathbf{v}_j$ wählen, dann $\mathbf{u}_j=\mathbf{A}\mathbf{v}_j/d_j$ berechnen. Dreht man $\mathbf{v}_j$ und $\mathbf{u}_j$ gemeinsam um, bleibt alles richtig.
:::

::::beispiel [Rechenbeispiel]
Für $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ ist $\mathbf{u}_1=\mathbf{A}\mathbf{v}_1/4=(2,\,1)^{\top}/\sqrt5$ und $\mathbf{u}_2=\mathbf{A}\mathbf{v}_2/1=(-1,\,2)^{\top}/\sqrt5$. Zur Kontrolle: $\mathbf{A}\mathbf{A}^{\top}=\bigl(\begin{smallmatrix}13&6\\6&4\end{smallmatrix}\bigr)$ bildet $(2,\,1)^{\top}$ auf $(32,\,16)^{\top}=16\,(2,\,1)^{\top}$ ab. Der Vektor $(-2,\,-1)^{\top}/\sqrt5$ wäre ebenfalls ein normierter Eigenvektor von $\mathbf{A}\mathbf{A}^{\top}$ zu $16$, aber mit ihm wäre $\mathbf{A}\mathbf{v}_1=-4\,\mathbf{u}_1$.
::::

⁠**Kurz gesagt:** Die rechten Singulärvektoren $\mathbf{v}_j$ sind Eigenvektoren von $\mathbf{A}^{\top}\mathbf{A}$, die linken sind $\mathbf{u}_j=\mathbf{A}\mathbf{v}_j/d_j$; beide Familien sind orthonormal, und $\mathbf{A}\mathbf{v}_j=d_j\mathbf{u}_j$.

### Die Zerlegung

<span class="anker" id="stufe-9-4"></span>

Schreibt man die Gleichungen $\mathbf{A}\mathbf{v}_j=d_j\mathbf{u}_j$ für alle $j$ nebeneinander, entsteht eine Zerlegung der ganzen Matrix.

:::satz Satz 9.4 (Singulärwertzerlegung)
<span class="anker" id="satz-9-4"></span>

Jede Matrix $\mathbf{A}\in\mathbb{R}^{m\times n}$ vom Rang $r$ lässt sich schreiben als

<span class="anker" id="gl-9-3"></span>
$$\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top} \tag{9.3}$$

mit orthogonalen Matrizen $\mathbf{U}\in\mathbb{R}^{m\times m}$ und $\mathbf{V}\in\mathbb{R}^{n\times n}$ und einer Matrix $\mathbf{D}\in\mathbb{R}^{m\times n}$, die auf der Diagonale die Singulärwerte $d_1\ge\dots\ge d_r>0$ trägt und sonst nur Nullen. Die Spalten von $\mathbf{V}$ sind rechte Singulärvektoren, die ersten $r$ Spalten von $\mathbf{U}$ die zugehörigen linken. Gleichwertig ist die kompakte Form

<span class="anker" id="gl-9-4"></span>
$$\mathbf{A}=\sum_{j=1}^rd_j\,\mathbf{u}_j\mathbf{v}_j^{\top} . \tag{9.4}$$
:::

:::beweis Singulärwertzerlegung
Für $j\le r$ ist $\mathbf{A}\mathbf{v}_j=d_j\mathbf{u}_j$. Für $j>r$ ist $d_j=0$, also $\lVert\mathbf{A}\mathbf{v}_j\rVert=0$ und $\mathbf{A}\mathbf{v}_j=\mathbf{0}$. Ist $r<m$, ergänzt man $\mathbf{u}_1,\dots,\mathbf{u}_r$ zu einer Orthonormalbasis des $\mathbb{R}^m$, etwa mit dem Gram-Schmidt-Verfahren wie im Beweis des Spektralsatzes. Nach [Grundlagen 1, Abschnitt 9.2](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrixprodukt.html#stufe-9-2), ist Spalte $j$ von $\mathbf{A}\mathbf{V}$ der Vektor $\mathbf{A}\mathbf{v}_j$, und Spalte $j$ von $\mathbf{U}\mathbf{D}$ ist $d_j\mathbf{u}_j$ für $j\le r$ und sonst der Nullvektor. Also ist $\mathbf{A}\mathbf{V}=\mathbf{U}\mathbf{D}$. Weil $\mathbf{V}$ orthogonal ist, ist $\mathbf{V}\mathbf{V}^{\top}=\mathbf{I}$, und Multiplikation mit $\mathbf{V}^{\top}$ von rechts ergibt $\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$. Die kompakte Form folgt aus [Grundlagen 1, Abschnitt 9.5](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrixprodukt.html#stufe-9-5): Spalte $j$ von $\mathbf{U}\mathbf{D}$ mal Zeile $j$ von $\mathbf{V}^{\top}$, summiert über $j$; nur die Summanden mit $j\le r$ sind nicht null.
:::

Die Form von $\mathbf{D}$ richtet sich nach der Form von $\mathbf{A}$. Für $m=3$ und $n=2$ ist zum Beispiel $\mathbf{D}=\Bigl(\begin{smallmatrix}d_1&0\\0&d_2\\0&0\end{smallmatrix}\Bigr)$. Die übliche Abkürzung ist SVD, nach dem englischen Namen *singular value decomposition*.

::::beispiel [Rechenbeispiel]
Für $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ ist

$$\mathbf{A}=\underbrace{\frac1{\sqrt5}\begin{pmatrix}2&-1\\1&2\end{pmatrix}}_{\mathbf{U}}\underbrace{\begin{pmatrix}4&0\\0&1\end{pmatrix}}_{\mathbf{D}}\underbrace{\frac1{\sqrt5}\begin{pmatrix}1&2\\-2&1\end{pmatrix}}_{\mathbf{V}^{\top}},$$

denn $\mathbf{U}\mathbf{D}=\tfrac1{\sqrt5}\bigl(\begin{smallmatrix}8&-1\\4&2\end{smallmatrix}\bigr)$ und $\mathbf{U}\mathbf{D}\mathbf{V}^{\top}=\tfrac15\bigl(\begin{smallmatrix}8+2&16-1\\4-4&8+2\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$. In kompakter Form:

$$4\cdot\frac15\begin{pmatrix}2&4\\1&2\end{pmatrix}+1\cdot\frac15\begin{pmatrix}2&-1\\-4&2\end{pmatrix}=\begin{pmatrix}1{,}6&3{,}2\\0{,}8&1{,}6\end{pmatrix}+\begin{pmatrix}0{,}4&-0{,}2\\-0{,}8&0{,}4\end{pmatrix}=\begin{pmatrix}2&3\\0&2\end{pmatrix}.$$
::::

⁠**Kurz gesagt:** Jede Matrix ist $\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$ mit zwei orthogonalen Matrizen und den Singulärwerten auf der Diagonale von $\mathbf{D}$, oder gleichwertig eine Summe $\sum_jd_j\mathbf{u}_j\mathbf{v}_j^{\top}$.

:::hintergrund Warum es die Zerlegung für jede Matrix gibt
Eigenvektoren hat nicht jede Matrix, und ihre Eigenvektoren stehen nicht immer senkrecht. Die Singulärwertzerlegung umgeht beide Hindernisse mit einem Trick: Sie benutzt nicht die Eigenvektoren von $\mathbf{A}$, sondern die von $\mathbf{A}^{\top}\mathbf{A}$. Diese Matrix ist für jedes $\mathbf{A}$ symmetrisch und positiv semidefinit, und für sie garantiert der Spektralsatz eine Orthonormalbasis aus Eigenvektoren mit Eigenwerten $\ge0$. Der Preis: Man braucht zwei Basen statt einer, eine für die Eingänge und eine für die Ausgänge.

Man kann die Singulärvektoren auch ohne $\mathbf{A}^{\top}\mathbf{A}$ beschreiben. Nach [(8.2)](positiv-definite-matrizen.html#gl-8-2), angewandt auf $\mathbf{A}^{\top}\mathbf{A}$, ist für Einheitsvektoren $\lVert\mathbf{A}\mathbf{v}\rVert^2=\mathbf{v}^{\top}\mathbf{A}^{\top}\mathbf{A}\mathbf{v}\le\lambda_1=d_1^2$, mit Gleichheit bei $\mathbf{v}_1$. Also ist $\mathbf{v}_1$ die Richtung, die $\mathbf{A}$ am stärksten streckt, und $d_1$ ist diese größte Streckung. Unter allen Einheitsvektoren, die senkrecht auf $\mathbf{v}_1$ stehen, wird $\mathbf{v}_2$ am stärksten gestreckt, und so weiter; das zeigt dieselbe Mittelwert-Rechnung wie im Beweis von [(8.2)](positiv-definite-matrizen.html#gl-8-2), mit $c_1=0$. Die Zerlegung zählt also die Richtungen der Reihe nach auf, von der stärksten zur schwächsten Streckung.

Eindeutig sind die Singulärwerte. Sind alle $d_j$ verschieden und positiv, so ist jedes Paar $\mathbf{v}_j,\mathbf{u}_j$ bis auf ein gemeinsames Vorzeichen festgelegt. Bei gleichen Singulärwerten gibt es mehr Freiheit: Eine orthogonale Matrix $\mathbf{Q}$ hat lauter Singulärwerte $1$, und für jede orthogonale Matrix $\mathbf{V}$ ist $\mathbf{Q}=(\mathbf{Q}\mathbf{V})\,\mathbf{I}\,\mathbf{V}^{\top}$ eine Singulärwertzerlegung.
:::

### Drehung, Streckung, Drehung

<span class="anker" id="stufe-9-5"></span>

Liest man $\mathbf{A}\mathbf{x}=\mathbf{U}\bigl(\mathbf{D}(\mathbf{V}^{\top}\mathbf{x})\bigr)$ von rechts nach links, so wirkt jede Matrix in drei Schritten (Abb. [23](#abb-23)):

<ol>

<li>

$\mathbf{V}^{\top}\mathbf{x}$ berechnet nach [(1.2)](orthonormalbasen-und-orthogonale-matrizen.html#gl-1-2) die Koordinaten $c_j=\mathbf{v}_j^{\top}\mathbf{x}$ von $\mathbf{x}$ in der Basis der $\mathbf{v}_j$. Geometrisch ist das eine Drehung oder Spiegelung, die $\mathbf{v}_j$ auf $\mathbf{e}_j$ legt.

</li>

<li>

$\mathbf{D}$ multipliziert jede Koordinate $c_j$ mit $d_j$. Ist $m>n$, hängt $\mathbf{D}$ Nullen an, ist $m<n$, lässt $\mathbf{D}$ die letzten Koordinaten weg. Aus dem Einheitskreis wird eine Ellipse, deren Achsen auf den Koordinatenachsen liegen.

</li>

<li>

$\mathbf{U}$ legt $\mathbf{e}_j$ auf $\mathbf{u}_j$, wieder eine Drehung oder Spiegelung.

</li>

</ol>

Jede lineare Abbildung ist also, bis auf Spiegelungen, eine Drehung, eine Streckung längs der Achsen und noch eine Drehung. Sie macht aus dem Einheitskreis eine Ellipse, aus der Einheitskugel ein Ellipsoid, mit den Halbachsen $d_j\mathbf{u}_j$. Ist $\det\mathbf{A}<0$, so ist mindestens eine Spiegelung dabei, denn nach [Grundlagen 1, Abschnitt 14.5](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/die-determinante.html#stufe-14-5), ist $\det\mathbf{A}=\det\mathbf{U}\cdot\det\mathbf{D}\cdot\det\mathbf{V}^{\top}$, und $\det\mathbf{D}\ge0$.

:::abbildung ml/k2svd 23
Die Matrix $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ als Drehung, Streckung, Drehung. Links oben der Einheitskreis mit $\mathbf{v}_1=(1,2)^{\top}/\sqrt5$ (rot) und $\mathbf{v}_2=(-2,1)^{\top}/\sqrt5$ (grün). $\mathbf{V}^{\top}$ dreht um $-63{,}4^\circ$ und legt $\mathbf{v}_1$ auf $\mathbf{e}_1$ und $\mathbf{v}_2$ auf $\mathbf{e}_2$ (links unten). $\mathbf{D}$ streckt die erste Achse um $d_1=4$ und die zweite um $d_2=1$ (rechts unten). $\mathbf{U}$ dreht um $26{,}6^\circ$ und legt die Achsen auf $\mathbf{u}_1=(2,1)^{\top}/\sqrt5$ und $\mathbf{u}_2=(-1,2)^{\top}/\sqrt5$ (rechts oben). Der schwarze Punkt $\mathbf{x}=\mathbf{e}_2$ landet auf allen Wegen bei $\mathbf{A}\mathbf{x}=(3,2)^{\top}$. Der direkte Weg oben ist $\mathbf{A}$ selbst: Der Einheitskreis wird zur Ellipse mit den Halbachsen $4\,\mathbf{u}_1$ und $1\cdot\mathbf{u}_2$.
:::

::::beispiel [Rechenbeispiel]
Für $\mathbf{x}=\mathbf{e}_2$ und $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ sind die Koordinaten $\mathbf{V}^{\top}\mathbf{x}=(2,\,1)^{\top}/\sqrt5$. Gestreckt ergibt das $\mathbf{D}\mathbf{V}^{\top}\mathbf{x}=(8,\,1)^{\top}/\sqrt5$, und gedreht

$$\mathbf{U}\mathbf{D}\mathbf{V}^{\top}\mathbf{x}=\frac15\begin{pmatrix}2&-1\\1&2\end{pmatrix}\begin{pmatrix}8\\1\end{pmatrix}=\frac15\begin{pmatrix}15\\10\end{pmatrix}=\begin{pmatrix}3\\2\end{pmatrix}=\mathbf{A}\mathbf{e}_2 .$$

$\mathbf{V}$ hat die Spalten $(\cos\theta,\,\sin\theta)^{\top}$ und $(-\sin\theta,\,\cos\theta)^{\top}$ mit $\cos\theta=1/\sqrt5$, ist also die Drehung um $\theta\approx63{,}4^\circ$, und $\mathbf{V}^{\top}$ dreht um $-63{,}4^\circ$ zurück. $\mathbf{U}$ ist die Drehung um $26{,}6^\circ$, denn $\cos26{,}6^\circ\approx2/\sqrt5$.
::::

⁠**Kurz gesagt:** Jede Matrix dreht, streckt längs der Achsen und dreht wieder, bis auf Spiegelungen; aus dem Einheitskreis wird eine Ellipse mit den Halbachsen $d_j\mathbf{u}_j$.

### Bausteine vom Rang 1 und die Räume einer Matrix

<span class="anker" id="stufe-9-6"></span>

Jeder Summand $d_j\mathbf{u}_j\mathbf{v}_j^{\top}$ der kompakten Form [(9.4)](#gl-9-4) hat den Rang $1$, denn alle seine Spalten sind Vielfache von $\mathbf{u}_j$. Er wirkt auf einen Vektor so:

$$d_j\mathbf{u}_j\mathbf{v}_j^{\top}\mathbf{x}=d_j\,(\mathbf{v}_j^{\top}\mathbf{x})\,\mathbf{u}_j .$$

Er liest die Koordinate von $\mathbf{x}$ längs $\mathbf{v}_j$ ab, multipliziert sie mit $d_j$ und gibt das Ergebnis in Richtung $\mathbf{u}_j$ aus. Die Matrix ist die Summe von $r$ solchen Bausteinen, nach ihrer Größe $d_j$ geordnet. Nebenbei liefert die Zerlegung Orthonormalbasen für die Unterräume, die zu einer Matrix gehören.

:::satz Satz 9.5 (Was die Singulärvektoren aufspannen)
<span class="anker" id="satz-9-5"></span>

Es sei $\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$ mit dem Rang $r$. Dann gilt:

<ol class="rm">

<li>

$\mathbf{u}_1,\dots,\mathbf{u}_r$ ist eine Orthonormalbasis des Spaltenraums von $\mathbf{A}$, und $\mathbf{u}_{r+1},\dots,\mathbf{u}_m$ ist eine Orthonormalbasis seines orthogonalen Komplements;

</li>

<li>

$\mathbf{v}_{r+1},\dots,\mathbf{v}_n$ ist eine Orthonormalbasis des Kerns von $\mathbf{A}$, und $\mathbf{v}_1,\dots,\mathbf{v}_r$ ist eine Orthonormalbasis des Spaltenraums von $\mathbf{A}^{\top}$.

</li>

</ol>
:::

:::beweis Räume
(i) Jedes $\mathbf{A}\mathbf{x}=\sum_{j\le r}d_j(\mathbf{v}_j^{\top}\mathbf{x})\mathbf{u}_j$ liegt im Spann von $\mathbf{u}_1,\dots,\mathbf{u}_r$, und umgekehrt ist $\mathbf{u}_j=\mathbf{A}(\mathbf{v}_j/d_j)$ ein Bild. Die übrigen Spalten von $\mathbf{U}$ stehen senkrecht auf diesen, spannen also nach Abschnitt [4.4](projektion-auf-einen-unterraum.html#stufe-4-4) das orthogonale Komplement auf. (ii) Weil die $\mathbf{u}_j$ unabhängig und die $d_j$ positiv sind, ist $\mathbf{A}\mathbf{x}=\mathbf{0}$ genau dann, wenn $\mathbf{v}_j^{\top}\mathbf{x}=0$ für alle $j\le r$ ist, wenn also $\mathbf{x}$ nur Koordinaten längs $\mathbf{v}_{r+1},\dots,\mathbf{v}_n$ hat. Schließlich ist $\mathbf{A}^{\top}=\mathbf{V}\mathbf{D}^{\top}\mathbf{U}^{\top}$ eine Singulärwertzerlegung von $\mathbf{A}^{\top}$, in der $\mathbf{U}$ und $\mathbf{V}$ die Rollen tauschen; (i) für $\mathbf{A}^{\top}$ ergibt den Rest.
:::

Die Zahlen passen zum Rangsatz aus [Grundlagen 1, Abschnitt 13.5](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/unabhangigkeit-basis-und-rang.html#stufe-13-5): Der Kern hat die Dimension $n-r$.

::::beispiel [Rechenbeispiel]
Die Matrix $\mathbf{H}$ mit den Spalten $(1,\,0,\,1)^{\top}$ und $(0,\,1,\,1)^{\top}$ aus Abschnitt [3.2](die-beste-naherungslosung.html#stufe-3-2) hat $\mathbf{H}^{\top}\mathbf{H}=\bigl(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr)$ mit den Eigenwerten $3$ und $1$, also die Singulärwerte $d_1=\sqrt3$ und $d_2=1$, und die rechten Singulärvektoren $\mathbf{v}_1=(1,\,1)^{\top}/\sqrt2$, $\mathbf{v}_2=(1,\,-1)^{\top}/\sqrt2$. Die linken sind

$$\mathbf{u}_1=\frac{\mathbf{H}\mathbf{v}_1}{\sqrt3}=\frac1{\sqrt6}\begin{pmatrix}1\\1\\2\end{pmatrix},\qquad \mathbf{u}_2=\frac{\mathbf{H}\mathbf{v}_2}{1}=\frac1{\sqrt2}\begin{pmatrix}1\\-1\\0\end{pmatrix}.$$

Sie bilden eine Orthonormalbasis der Ebene $x_3=x_1+x_2$, eine andere als in Abschnitt [4.3](projektion-auf-einen-unterraum.html#stufe-4-3). Ergänzt wird sie durch $\mathbf{u}_3=(1,\,1,\,-1)^{\top}/\sqrt3$, den normierten Normalenvektor aus Abschnitt [4.4](projektion-auf-einen-unterraum.html#stufe-4-4). In der vollen Zerlegung ist $\mathbf{D}=\Bigl(\begin{smallmatrix}\sqrt3&0\\0&1\\0&0\end{smallmatrix}\Bigr)$. Der Kern besteht nur aus dem Nullvektor, denn $r=n=2$.
::::

⁠**Kurz gesagt:** Eine Matrix ist die Summe von $r$ Bausteinen $d_j\mathbf{u}_j\mathbf{v}_j^{\top}$ vom Rang $1$; die $\mathbf{u}_j$ mit $d_j>0$ spannen den Spaltenraum auf, die $\mathbf{v}_j$ mit $d_j=0$ den Kern.

### Symmetrische Matrizen

<span class="anker" id="stufe-9-7"></span>

Bei einer symmetrischen Matrix gibt es schon eine Zerlegung mit einer Orthonormalbasis, $\mathbf{A}=\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top}$. Wie hängt sie mit der Singulärwertzerlegung zusammen?

:::satz Satz 9.6 (Singulärwerte symmetrischer Matrizen)
<span class="anker" id="satz-9-6"></span>

Die Singulärwerte einer symmetrischen Matrix sind die Beträge $|\lambda_i|$ ihrer Eigenwerte. Ist $\mathbf{q}_i$ ein normierter Eigenvektor zu $\lambda_i\ne0$, so ist $\mathbf{v}=\mathbf{q}_i$ ein rechter und $\mathbf{u}=\operatorname{sign}(\lambda_i)\,\mathbf{q}_i$ der zugehörige linke Singulärvektor.
:::

:::beweis Symmetrische Matrizen
Es ist $\mathbf{A}^{\top}\mathbf{A}=\mathbf{A}^2=\mathbf{Q}\boldsymbol{\Lambda}^2\mathbf{Q}^{\top}$, also hat $\mathbf{A}^{\top}\mathbf{A}$ die Eigenvektoren $\mathbf{q}_i$ mit den Eigenwerten $\lambda_i^2$, und die Singulärwerte sind $\sqrt{\lambda_i^2}=|\lambda_i|$. Nach [(9.2)](#gl-9-2) ist $\mathbf{u}=\mathbf{A}\mathbf{q}_i/|\lambda_i|=(\lambda_i/|\lambda_i|)\,\mathbf{q}_i$.
:::

Ist $\mathbf{A}$ positiv semidefinit, so sind Spektralzerlegung und Singulärwertzerlegung dieselbe Zerlegung, mit $\mathbf{U}=\mathbf{V}=\mathbf{Q}$. Bei negativen Eigenwerten wandert das Vorzeichen in $\mathbf{U}$. Bei nicht symmetrischen Matrizen haben Eigenwerte und Singulärwerte im Allgemeinen nichts miteinander zu tun, wie $\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ mit den Eigenwerten $2,2$ und den Singulärwerten $4,1$ zeigt. Einen Zusammenhang gibt es aber immer: Jeder Eigenwert ist im Betrag höchstens $d_1$; das folgt aus dem nächsten Unterabschnitt.

::::beispiel [Rechenbeispiel]
$\mathbf{A}=\bigl(\begin{smallmatrix}1&3\\3&1\end{smallmatrix}\bigr)$ hat die Eigenwerte $4$ mit $\mathbf{q}_1=(1,\,1)^{\top}/\sqrt2$ und $-2$ mit $\mathbf{q}_2=(1,\,-1)^{\top}/\sqrt2$. Die Singulärwerte sind $4$ und $2$. Mit $\mathbf{v}_2=\mathbf{q}_2$ ist $\mathbf{A}\mathbf{v}_2=(-2,\,2)^{\top}/\sqrt2=2\cdot(-1,\,1)^{\top}/\sqrt2$, also $\mathbf{u}_2=-\mathbf{q}_2$.
::::

⁠**Kurz gesagt:** Bei symmetrischen Matrizen sind die Singulärwerte die Beträge der Eigenwerte, und bei positiv semidefiniten ist die Singulärwertzerlegung die Spektralzerlegung.

### Die Spektralnorm

<span class="anker" id="stufe-9-8"></span>

Wie stark kann eine Matrix einen Vektor höchstens verlängern? Für Vektoren misst die Norm die Größe. Für eine Matrix ist eine natürliche Größe ihr stärkster Verlängerungsfaktor.

:::definition Definition 9.7 (Spektralnorm)
<span class="anker" id="satz-9-7"></span>

Die __Spektralnorm__ einer Matrix $\mathbf{A}$ ist

$$\lVert\mathbf{A}\rVert_2=\max_{\mathbf{x}\ne\mathbf{0}}\frac{\lVert\mathbf{A}\mathbf{x}\rVert}{\lVert\mathbf{x}\rVert} .$$
:::

:::satz Satz 9.8 (Größte und kleinste Streckung)
<span class="anker" id="satz-9-8"></span>

Für jedes $\mathbf{A}\in\mathbb{R}^{m\times n}$ mit den Singulärwerten $d_1\ge\dots\ge d_n$ und jedes $\mathbf{x}\in\mathbb{R}^n$ gilt

<span class="anker" id="gl-9-5"></span>
$$d_n\,\lVert\mathbf{x}\rVert\le\lVert\mathbf{A}\mathbf{x}\rVert\le d_1\,\lVert\mathbf{x}\rVert . \tag{9.5}$$

Die Grenzen werden bei $\mathbf{x}=\mathbf{v}_1$ und $\mathbf{x}=\mathbf{v}_n$ erreicht. Insbesondere ist $\lVert\mathbf{A}\rVert_2=d_1$.
:::

:::beweis Größte und kleinste Streckung
Mit $\mathbf{c}=\mathbf{V}^{\top}\mathbf{x}$ ist $\lVert\mathbf{c}\rVert=\lVert\mathbf{x}\rVert$ und $\lVert\mathbf{A}\mathbf{x}\rVert^2=\mathbf{x}^{\top}\mathbf{A}^{\top}\mathbf{A}\mathbf{x}=\sum_jd_j^2c_j^2$. Das liegt zwischen $d_n^2\sum_jc_j^2$ und $d_1^2\sum_jc_j^2$. Es ist der Rayleigh-Quotient [(8.2)](positiv-definite-matrizen.html#gl-8-2) von $\mathbf{A}^{\top}\mathbf{A}$, mit $\lVert\mathbf{x}\rVert^2$ multipliziert.
:::

Zwei Folgerungen. Erstens ist $\lVert\mathbf{A}\mathbf{x}\rVert\le\lVert\mathbf{A}\rVert_2\lVert\mathbf{x}\rVert$ und daher $\lVert\mathbf{A}\mathbf{B}\mathbf{x}\rVert\le\lVert\mathbf{A}\rVert_2\lVert\mathbf{B}\rVert_2\lVert\mathbf{x}\rVert$, also $\lVert\mathbf{A}\mathbf{B}\rVert_2\le\lVert\mathbf{A}\rVert_2\lVert\mathbf{B}\rVert_2$: Hintereinander ausgeführt, multiplizieren sich die größten Streckfaktoren höchstens. Zweitens ist für einen Eigenvektor $\lVert\mathbf{A}\mathbf{v}\rVert=|\lambda|\,\lVert\mathbf{v}\rVert$, also $|\lambda|\le d_1$ für jeden Eigenwert einer quadratischen Matrix. Für einen komplexen Eigenvektor $\mathbf{v}=\mathbf{a}+\mathrm j\mathbf{b}$ mit reellen $\mathbf{a},\mathbf{b}$ gilt dasselbe, wenn man $\lVert\mathbf{v}\rVert^2=(\mathbf{v}^*)^{\top}\mathbf{v}=\lVert\mathbf{a}\rVert^2+\lVert\mathbf{b}\rVert^2$ setzt, denn $\lVert\mathbf{A}\mathbf{v}\rVert^2=\lVert\mathbf{A}\mathbf{a}\rVert^2+\lVert\mathbf{A}\mathbf{b}\rVert^2$ liegt nach [(9.5)](#gl-9-5) zwischen $d_n^2\lVert\mathbf{v}\rVert^2$ und $d_1^2\lVert\mathbf{v}\rVert^2$; für quadratisches $\mathbf{A}$ ist also auch $|\lambda|\ge d_n$.

::::beispiel [Rechenbeispiel]
Für $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ ist $\lVert\mathbf{A}\rVert_2=4$. Die Einheitsvektoren werden weniger gestreckt: $\lVert\mathbf{A}\mathbf{e}_1\rVert=\lVert(2,\,0)^{\top}\rVert=2$ und $\lVert\mathbf{A}\mathbf{e}_2\rVert=\lVert(3,\,2)^{\top}\rVert=\sqrt{13}\approx3{,}61$. Den Faktor $4$ erreicht man nur bei $\mathbf{v}_1=(1,\,2)^{\top}/\sqrt5$, den kleinsten Faktor $1$ bei $\mathbf{v}_2$. Der Eigenwert $2$ liegt zwischen $1$ und $4$.
::::

⁠**Kurz gesagt:** Die Spektralnorm $\lVert\mathbf{A}\rVert_2=d_1$ ist der größte Faktor, um den $\mathbf{A}$ einen Vektor verlängert; der kleinste ist $d_n$.

:::hintergrund Mehrere Antennen: parallele Kanäle aus der Singulärwertzerlegung
Ein Funksystem mit mehreren Sende- und Empfangsantennen heißt MIMO-System. Jede Empfangsantenne empfängt eine Mischung aller Sendesignale. In einem einfachen Modell ist der empfangene Vektor $\mathbf{y}=\mathbf{K}\mathbf{x}+\boldsymbol\nu$: $\mathbf{x}$ enthält die Sendesignale der Antennen, die Kanalmatrix $\mathbf{K}$ beschreibt, wie stark jede Sendeantenne bei jeder Empfangsantenne ankommt, und $\boldsymbol\nu$ ist das Rauschen.

Kennen Sender und Empfänger die Zerlegung $\mathbf{K}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$, so sendet der Sender $\mathbf{x}=\mathbf{V}\tilde{\mathbf{x}}$, und der Empfänger berechnet $\tilde{\mathbf{y}}=\mathbf{U}^{\top}\mathbf{y}$. Dann ist

$$\tilde{\mathbf{y}}=\mathbf{U}^{\top}\mathbf{U}\mathbf{D}\mathbf{V}^{\top}\mathbf{V}\tilde{\mathbf{x}}+\mathbf{U}^{\top}\boldsymbol\nu=\mathbf{D}\tilde{\mathbf{x}}+\tilde{\boldsymbol\nu} .$$

Aus dem gemischten Kanal sind $r$ getrennte Kanäle geworden: $\tilde y_j=d_j\tilde x_j+\tilde\nu_j$. Jeder überträgt einen eigenen Datenstrom, mit dem Verstärkungsfaktor $d_j$. Das Rauschen wird dabei nur gedreht, seine Länge bleibt gleich, denn $\mathbf{U}^{\top}$ ist orthogonal. Die Zahl der nutzbaren parallelen Kanäle ist der Rang der Kanalmatrix, und wie gut jeder Kanal ist, sagt sein Singulärwert. Das ist Drehung, Streckung, Drehung in der Praxis: Der Sender dreht vor, der Kanal streckt, der Empfänger dreht zurück.
:::

:::aufgabe Aufgabe 27 ★★ Eine Zerlegung von Hand
<span class="anker" id="aufg-27"></span>

Es sei $\mathbf{A}=\bigl(\begin{smallmatrix}3&0\\4&5\end{smallmatrix}\bigr)$.

<ol class="al">

<li>

Berechne $\mathbf{A}^{\top}\mathbf{A}$, ihre Eigenwerte und die Singulärwerte von $\mathbf{A}$.

</li>

<li>

Bestimme $\mathbf{v}_1,\mathbf{v}_2$ und daraus $\mathbf{u}_1,\mathbf{u}_2$ mit [(9.2)](#gl-9-2). Prüfe $\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$.

</li>

<li>

Vergleiche die Singulärwerte mit den Eigenwerten von $\mathbf{A}$. Was stimmt überein, was nicht?

</li>

</ol>

:::loesung
(a) $\mathbf{A}^{\top}\mathbf{A}=\bigl(\begin{smallmatrix}9+16&20\\20&25\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}25&20\\20&25\end{smallmatrix}\bigr)$ mit Spur $50$ und Determinante $625-400=225$, also $\lambda^2-50\lambda+225=(\lambda-45)(\lambda-5)$. Die Singulärwerte sind $d_1=\sqrt{45}=3\sqrt5\approx6{,}708$ und $d_2=\sqrt5\approx2{,}236$.

(b) Eigenvektoren von $\mathbf{A}^{\top}\mathbf{A}$: $\mathbf{v}_1=(1,\,1)^{\top}/\sqrt2$ zu $45$ und $\mathbf{v}_2=(-1,\,1)^{\top}/\sqrt2$ zu $5$. Dann

$$\mathbf{u}_1=\frac{\mathbf{A}\mathbf{v}_1}{d_1}=\frac{(3,\,9)^{\top}}{\sqrt2\cdot3\sqrt5}=\frac{(1,\,3)^{\top}}{\sqrt{10}},\qquad \mathbf{u}_2=\frac{\mathbf{A}\mathbf{v}_2}{d_2}=\frac{(-3,\,1)^{\top}}{\sqrt2\cdot\sqrt5}=\frac{(-3,\,1)^{\top}}{\sqrt{10}} .$$

Probe: $\mathbf{U}\mathbf{D}=\tfrac1{\sqrt{10}}\bigl(\begin{smallmatrix}3\sqrt5&-3\sqrt5\\9\sqrt5&\sqrt5\end{smallmatrix}\bigr)=\tfrac1{\sqrt2}\bigl(\begin{smallmatrix}3&-3\\9&1\end{smallmatrix}\bigr)$ und

$$\mathbf{U}\mathbf{D}\mathbf{V}^{\top}=\frac1{\sqrt2}\begin{pmatrix}3&-3\\9&1\end{pmatrix}\frac1{\sqrt2}\begin{pmatrix}1&1\\-1&1\end{pmatrix}=\frac12\begin{pmatrix}6&0\\8&10\end{pmatrix}=\begin{pmatrix}3&0\\4&5\end{pmatrix}.$$

(c) Die Eigenwerte der Dreiecksmatrix sind $3$ und $5$. Das Produkt stimmt überein: $3\cdot5=15=3\sqrt5\cdot\sqrt5=|\det\mathbf{A}|$. Die Summen nicht: $8$ gegen $4\sqrt5\approx8{,}94$. Die Eigenwerte liegen im Betrag zwischen $d_2$ und $d_1$: $2{,}236\le3$ und $5\le6{,}708$.
:::
:::

:::aufgabe Aufgabe 28 ★★ Eine rechteckige Matrix
<span class="anker" id="aufg-28"></span>

Es sei $\mathbf{A}=\Bigl(\begin{smallmatrix}1&1\\1&1\\1&-1\end{smallmatrix}\Bigr)$.

<ol class="al">

<li>

Bestimme die Singulärwerte und die Singulärvektoren $\mathbf{v}_1,\mathbf{v}_2,\mathbf{u}_1,\mathbf{u}_2$.

</li>

<li>

Ergänze $\mathbf{u}_3$ und schreibe die volle Zerlegung $\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$ hin.

</li>

<li>

Gib Orthonormalbasen des Spaltenraums und seines orthogonalen Komplements an.

</li>

</ol>

:::loesung
(a) $\mathbf{A}^{\top}\mathbf{A}=\bigl(\begin{smallmatrix}3&1\\1&3\end{smallmatrix}\bigr)$ hat die Eigenwerte $4$ mit $\mathbf{v}_1=(1,\,1)^{\top}/\sqrt2$ und $2$ mit $\mathbf{v}_2=(1,\,-1)^{\top}/\sqrt2$. Also $d_1=2$, $d_2=\sqrt2$, und

$$\mathbf{u}_1=\frac{\mathbf{A}\mathbf{v}_1}2=\frac{(2,\,2,\,0)^{\top}}{2\sqrt2}=\frac{(1,\,1,\,0)^{\top}}{\sqrt2},\qquad \mathbf{u}_2=\frac{\mathbf{A}\mathbf{v}_2}{\sqrt2}=\frac{(0,\,0,\,2)^{\top}}{\sqrt2\cdot\sqrt2}=(0,\,0,\,1)^{\top} .$$

(b) $\mathbf{u}_3$ steht senkrecht auf beiden: $\mathbf{u}_3=(1,\,-1,\,0)^{\top}/\sqrt2$. Die volle Zerlegung ist

$$\mathbf{A}=\begin{pmatrix}1/\sqrt2&0&1/\sqrt2\\1/\sqrt2&0&-1/\sqrt2\\0&1&0\end{pmatrix}\begin{pmatrix}2&0\\0&\sqrt2\\0&0\end{pmatrix}\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}.$$

(c) Nach dem Satz in Abschnitt [9.6](#stufe-9-6) ist $\mathbf{u}_1,\mathbf{u}_2$ eine Orthonormalbasis des Spaltenraums und $\mathbf{u}_3$ eine des orthogonalen Komplements. Zur Kontrolle: Die Spalten $(1,\,1,\,1)^{\top}=\sqrt2\,\mathbf{u}_1+\mathbf{u}_2$ und $(1,\,1,\,-1)^{\top}=\sqrt2\,\mathbf{u}_1-\mathbf{u}_2$ liegen im Spann von $\mathbf{u}_1,\mathbf{u}_2$, und beide stehen senkrecht auf $\mathbf{u}_3$.
:::
:::

:::aufgabe Aufgabe 29 ★★★ Eigenschaften der Singulärwerte
<span class="anker" id="aufg-29"></span>

<ol class="al">

<li>

Zeige: Für eine quadratische Matrix ist $|\det\mathbf{A}|=d_1d_2\cdots d_n$.

</li>

<li>

Zeige: $\mathbf{A}$ und $\mathbf{A}^{\top}$ haben dieselben positiven Singulärwerte.

</li>

<li>

Zeige: Für $\mathbf{u}\ne\mathbf{0}$ und $\mathbf{v}\ne\mathbf{0}$ hat das äußere Produkt $\mathbf{u}\mathbf{v}^{\top}$ genau einen positiven Singulärwert, nämlich $\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert$.

</li>

<li>

Zeige: Ist $\mathbf{Q}$ orthogonal, so haben $\mathbf{Q}\mathbf{A}$ und $\mathbf{A}$ dieselben Singulärwerte.

</li>

</ol>

:::loesung
(a) Nach [Grundlagen 1, Abschnitt 14.5](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/die-determinante.html#stufe-14-5), ist $\det\mathbf{A}=\det\mathbf{U}\cdot\det\mathbf{D}\cdot\det\mathbf{V}^{\top}$. Die beiden orthogonalen Matrizen haben die Determinante $\pm1$, und $\mathbf{D}$ ist eine Diagonalmatrix mit der Determinante $d_1\cdots d_n$. Also ist $|\det\mathbf{A}|=d_1\cdots d_n$.

(b) Aus $\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$ folgt $\mathbf{A}^{\top}\mathbf{A}=\mathbf{V}\mathbf{D}^{\top}\mathbf{D}\mathbf{V}^{\top}$ und $\mathbf{A}\mathbf{A}^{\top}=\mathbf{U}\mathbf{D}\mathbf{D}^{\top}\mathbf{U}^{\top}$. Die Diagonalmatrizen $\mathbf{D}^{\top}\mathbf{D}$ und $\mathbf{D}\mathbf{D}^{\top}$ haben dieselben Einträge $d_j^2>0$ auf der Diagonale, nur verschieden viele Nullen. Die Singulärwerte von $\mathbf{A}^{\top}$ sind die Wurzeln der Eigenwerte von $(\mathbf{A}^{\top})^{\top}\mathbf{A}^{\top}=\mathbf{A}\mathbf{A}^{\top}$, also wieder die $d_j$, ergänzt um Nullen.

(c) $(\mathbf{u}\mathbf{v}^{\top})^{\top}(\mathbf{u}\mathbf{v}^{\top})=\mathbf{v}\,\mathbf{u}^{\top}\mathbf{u}\,\mathbf{v}^{\top}=\lVert\mathbf{u}\rVert^2\,\mathbf{v}\mathbf{v}^{\top}$. Diese Matrix bildet $\mathbf{v}$ auf $\lVert\mathbf{u}\rVert^2\lVert\mathbf{v}\rVert^2\,\mathbf{v}$ ab und jeden Vektor senkrecht zu $\mathbf{v}$ auf null. Ihre Eigenwerte sind also $\lVert\mathbf{u}\rVert^2\lVert\mathbf{v}\rVert^2$ und sonst $0$, und der einzige positive Singulärwert ist $\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert$.

(d) $(\mathbf{Q}\mathbf{A})^{\top}(\mathbf{Q}\mathbf{A})=\mathbf{A}^{\top}\mathbf{Q}^{\top}\mathbf{Q}\mathbf{A}=\mathbf{A}^{\top}\mathbf{A}$. Beide Matrizen haben dieselbe Gram-Matrix und damit dieselben Singulärwerte. Anschaulich: Eine Drehung oder Spiegelung nach $\mathbf{A}$ ändert die Form der Ellipse nicht, nur ihre Lage.
:::
:::

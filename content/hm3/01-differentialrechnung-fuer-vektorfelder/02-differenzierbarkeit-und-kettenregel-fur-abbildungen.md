---
title: Differenzierbarkeit und Kettenregel für Abbildungen
pfad: Elektrotechnik / 3. Semester / HöMa3 – Höhere Mathematik 3 / Differentialrechnung für Vektorfelder
adresse: elektrotechnik/3-semester/hohere-mathematik-3/differentialrechnung-fur-vektorfelder
knoten: Kapitel 1: Differentialrechnung für Vektorfelder
order: 3110200
summary: Eine Funktion einer Variablen hat eine Ableitung, die angibt, wie schnell sich ihr Wert ändert.
tags: Komponente, Vektor, Einheitsvektor, Länge, euklidische Norm, Abstand, Skalarprodukt, Matrix
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Eine Funktion einer Variablen hat eine Ableitung, die angibt, wie schnell sich ihr Wert ändert. Dieser Abschnitt überträgt das auf Abbildungen, in die mehrere Zahlen hineingehen und aus denen mehrere herauskommen. Er klärt, wann eine solche Abbildung differenzierbar ist und wie man zwei hintereinander ausgeführte Abbildungen ableitet.
:::

### Was du dafür brauchst: Vektoren im $\mathbb{R}^n$

<span class="anker" id="stufe-1-1"></span>

Ein Punkt der Ebene wird durch zwei Zahlen beschrieben, ein Punkt des Raums durch drei. In diesem Kapitel braucht man Listen aus beliebig vielen Zahlen und ein Maß für ihre Länge.

**Der Raum $\mathbb{R}^n$.** Für eine natürliche Zahl $n$ ist $\mathbb{R}^n$ die Menge aller Listen $\boldsymbol{x}=(x_1,\dots,x_n)$ aus $n$ reellen Zahlen. Die Zahl $x_j$ heißt die $j$-te __Komponente__ von $\boldsymbol{x}$. Der $\mathbb{R}^2$ ist die Ebene, der $\mathbb{R}^3$ der Raum. Dort schreibt man oft $(x,y)$ statt $(x_1,x_2)$ und $(x,y,z)$ statt $(x_1,x_2,x_3)$.

**Vektoren.** Man kann $\boldsymbol{x}$ als Punkt lesen oder als Pfeil vom Nullpunkt zu diesem Punkt. Als Pfeil gelesen heißt $\boldsymbol{x}$ ein __Vektor__. Vektoren werden fett gesetzt, Zahlen nicht. Man addiert Vektoren und multipliziert sie mit einer Zahl $c$ Komponente für Komponente:

$$\boldsymbol{x}+\boldsymbol{y}=(x_1+y_1,\dots,x_n+y_n),\qquad c\,\boldsymbol{x}=(c\,x_1,\dots,c\,x_n).$$

Der Pfeil $\boldsymbol{y}-\boldsymbol{x}$ führt vom Punkt $\boldsymbol{x}$ zum Punkt $\boldsymbol{y}$. Den Vektor, dessen Komponenten alle null sind, schreibt man kurz $0$.

**Einheitsvektoren der Achsen.** Der Vektor $\hat{\boldsymbol{e}}_j$ hat an der Stelle $j$ eine $1$ und sonst lauter Nullen. Er zeigt in Richtung der $x_j$-Achse und heißt der $j$-te __Einheitsvektor__. Jeder Vektor ist eine Summe von Vielfachen dieser Vektoren: $\boldsymbol{x}=x_1\hat{\boldsymbol{e}}_1+\dots+x_n\hat{\boldsymbol{e}}_n$.

**Länge und Abstand.** Die __Länge__ des Vektors $\boldsymbol{x}$ ist

$$|\boldsymbol{x}|=\sqrt{x_1^2+\dots+x_n^2}.$$

In der Ebene ist das der Satz des Pythagoras. Man nennt $|\boldsymbol{x}|$ auch die __euklidische Norm__ von $\boldsymbol{x}$. Der __Abstand__ zweier Punkte $\boldsymbol{x}$ und $\boldsymbol{y}$ ist die Länge des Pfeils zwischen ihnen, also $|\boldsymbol{y}-\boldsymbol{x}|$.

::::beispiel
Für $\boldsymbol{x}=(3,4)$ ist $|\boldsymbol{x}|=\sqrt{9+16}=5$. Die Punkte $(1,2)$ und $(4,6)$ haben den Abstand $|(3,4)|=5$. Im Raum ist $|(1,2,2)|=\sqrt{1+4+4}=3$.
::::

⁠**Kurz gesagt:** Ein Vektor im $\mathbb{R}^n$ ist eine Liste von $n$ Zahlen, die man als Pfeil zeichnet. Seine Länge ist die Wurzel aus der Summe der Quadrate seiner Komponenten.

### Was du dafür brauchst: das Skalarprodukt

<span class="anker" id="stufe-1-2"></span>

Ob zwei Pfeile in ähnliche Richtungen zeigen, senkrecht aufeinander stehen oder gegeneinander zeigen, misst eine einzige Zahl.

Das __Skalarprodukt__ zweier Vektoren $\boldsymbol a,\boldsymbol b\in\mathbb{R}^n$ ist die Zahl

$$\boldsymbol a\cdot\boldsymbol b=a_1b_1+\dots+a_nb_n=\sum_{j=1}^n a_jb_j .$$

Für $\boldsymbol a=\boldsymbol b$ ergibt sich die Summe der Quadrate: $\boldsymbol a\cdot\boldsymbol a=|\boldsymbol a|^2$. Geometrisch gilt

$$\boldsymbol a\cdot\boldsymbol b=|\boldsymbol a|\,|\boldsymbol b|\cos\alpha ,$$

wobei $\alpha$ der Winkel zwischen den beiden Pfeilen ist. Daran liest man ab: Für Vektoren, die nicht null sind, ist das Skalarprodukt positiv, wenn der Winkel kleiner als $90^\circ$ ist, null, wenn sie senkrecht aufeinander stehen, und negativ, wenn der Winkel größer als $90^\circ$ ist. Mit einem Einheitsvektor liefert das Skalarprodukt eine Komponente: $\hat{\boldsymbol{e}}_j\cdot\boldsymbol{x}=x_j$.

::::beispiel
$(1,2,2)\cdot(2,0,-1)=2+0-2=0$, die beiden Vektoren stehen senkrecht aufeinander. Für $(1,1)$ und $(1,0)$ ist das Skalarprodukt $1$. Zur Kontrolle mit dem Winkel: $|(1,1)|\,|(1,0)|\cos45^\circ=\sqrt2\cdot1\cdot\tfrac1{\sqrt2}=1$.
::::

⁠**Kurz gesagt:** Das Skalarprodukt multipliziert Komponente mit Komponente und addiert. Es ist genau dann null, wenn zwei Vektoren, die nicht null sind, senkrecht aufeinander stehen.

### Was du dafür brauchst: Matrizen und Matrixprodukt

<span class="anker" id="stufe-1-3"></span>

Eine Matrix macht aus einem Vektor einen anderen Vektor. Das ist die einfachste Art, aus mehreren Zahlen mehrere andere Zahlen zu berechnen.

**Matrix.** Eine __Matrix__ $M\in\mathbb{R}^{m\times n}$ ist eine rechteckige Zahlentabelle mit $m$ Zeilen und $n$ Spalten. Den Eintrag in Zeile $j$ und Spalte $k$ schreibt man $M_{jk}$. Für die ganze Matrix schreibt man kurz $M=(M_{jk})_{jk}$. Das Paar $m\times n$ heißt das __Format__ der Matrix. Eine Matrix mit gleich vielen Zeilen und Spalten heißt __quadratisch__. Die Einträge $M_{11},M_{22},\dots$ einer quadratischen Matrix bilden ihre __Diagonale__.

**Matrix mal Vektor.** Für $M\in\mathbb{R}^{m\times n}$ und einen Vektor $\boldsymbol s\in\mathbb{R}^n$ ist $M\boldsymbol s\in\mathbb{R}^m$ der Vektor mit den Komponenten

$$(M\boldsymbol s)_j=\sum_{k=1}^n M_{jk}\,s_k,\qquad j=1,\dots,m.$$

Komponente $j$ entsteht also aus Zeile $j$ von $M$: Eintrag für Eintrag mit $\boldsymbol s$ multiplizieren und aufsummieren. Für $\boldsymbol s=\hat{\boldsymbol{e}}_k$ bleibt nur der Summand mit $s_k=1$ übrig. Deshalb ist $M\hat{\boldsymbol{e}}_k$ die Spalte $k$ von $M$.

**Matrixprodukt.** Für $M\in\mathbb{R}^{m\times n}$ und $L\in\mathbb{R}^{n\times p}$ ist das __Matrixprodukt__ $ML\in\mathbb{R}^{m\times p}$ die Matrix mit den Einträgen

$$(ML)_{ik}=\sum_{j=1}^n M_{ij}\,L_{jk}.$$

Eintrag $(i,k)$ ist Zeile $i$ von $M$ mal Spalte $k$ von $L$. Das geht nur, wenn $M$ so viele Spalten hat wie $L$ Zeilen, und das Ergebnis hat so viele Zeilen wie $M$ und so viele Spalten wie $L$. Es gilt $(ML)\boldsymbol s=M(L\boldsymbol s)$: Das Produkt wirkt wie die beiden Matrizen nacheinander, zuerst $L$, dann $M$.

::::beispiel
$$\begin{pmatrix}1&2\\3&4\end{pmatrix}\begin{pmatrix}1\\1\end{pmatrix}=\begin{pmatrix}3\\7\end{pmatrix},\qquad \begin{pmatrix}1&2\\3&4\end{pmatrix}\begin{pmatrix}0&1\\1&0\end{pmatrix}=\begin{pmatrix}2&1\\4&3\end{pmatrix}.$$

Die Matrix $\bigl(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr)$ macht aus $\hat{\boldsymbol{e}}_2=(0,1)$ ihre zweite Spalte $(2,4)$. Eine $2\times3$-Matrix mal eine $3\times1$-Matrix ergibt eine $2\times1$-Matrix.
::::

⁠**Kurz gesagt:** Matrix mal Vektor ergibt einen Vektor. Das Matrixprodukt ist die Matrix, die dasselbe bewirkt wie zwei Matrizen nacheinander.

### Was du dafür brauchst: Transponieren und symmetrische Matrizen

<span class="anker" id="stufe-1-4"></span>

Dieselben Zahlen lassen sich als Zeile oder als Spalte anordnen. Für die Rechnung macht das einen Unterschied.

**Transponieren.** Die __Transponierte__ $M^T$ einer Matrix $M\in\mathbb{R}^{m\times n}$ entsteht, wenn man Zeilen und Spalten vertauscht. Es ist $M^T\in\mathbb{R}^{n\times m}$ und $(M^T)_{jk}=M_{kj}$. Zweimal transponieren gibt die ursprüngliche Matrix zurück.

**Zeile und Spalte.** Ein Vektor mit $n$ Komponenten lässt sich als Spalte schreiben, also als $n\times1$-Matrix, oder als Zeile, also als $1\times n$-Matrix. In Rechnungen mit Matrizen ist ein Vektor immer eine Spalte. Im Fließtext schreibt man ihn aus Platzgründen meist als Zeile $(x_1,\dots,x_n)$; gemeint ist dann dieselbe Spalte. Wo es auf die Form ankommt, macht das Zeichen $T$ sie deutlich: $(x_1,\dots,x_n)^T$ ist ausdrücklich die Spalte. Zeile mal Spalte ist das Skalarprodukt: $\boldsymbol a^T\boldsymbol b=\boldsymbol a\cdot\boldsymbol b$.

**Symmetrische Matrizen.** Eine quadratische Matrix heißt __symmetrisch__, wenn $M^T=M$ gilt, also $M_{jk}=M_{kj}$ für alle $j,k$. Ihre Einträge sind an der Diagonalen gespiegelt.

::::beispiel
$$\begin{pmatrix}1&2&3\\4&5&6\end{pmatrix}^T=\begin{pmatrix}1&4\\2&5\\3&6\end{pmatrix},\qquad (1\;\;2\;\;3)\begin{pmatrix}4\\5\\6\end{pmatrix}=4+10+18=32 .$$

Die Matrix $\bigl(\begin{smallmatrix}1&2\\2&5\end{smallmatrix}\bigr)$ ist symmetrisch. Die Matrix $\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)$ ist es nicht, denn rechts oben steht $-1$ und links unten $1$.
::::

⁠**Kurz gesagt:** Transponieren vertauscht Zeilen und Spalten. Eine symmetrische Matrix bleibt dabei gleich.

### Was du dafür brauchst: Funktionen mehrerer Variablen

<span class="anker" id="stufe-1-5"></span>

Die Temperatur in einem Raum oder die Höhe eines Geländes ordnet jedem Punkt eine Zahl zu. Eine Wanderkarte zeigt die Höhe, ohne das Gelände räumlich zu zeichnen: Linien verbinden die Punkte gleicher Höhe (Abb. [1](#abb-1)).

:::abbildung hm3/k1hoehen 1
Die Schale $\varphi(x,y)=x^2+2y^2$ als Landkarte. Die blauen Linien sind die Höhenlinien $\varphi=1$, $\varphi=3$ und $\varphi=6$, Ellipsen um den Nullpunkt. An vier Punkten steht der Funktionswert in Schwarz: $\varphi(0,0)=0$, $\varphi(2,0)=4$ und $\varphi(1,1)=\varphi(-1,-1)=3$.
:::

**Skalare Funktionen.** Eine Funktion $f$ von $n$ Variablen ordnet jedem Punkt $\boldsymbol{x}=(x_1,\dots,x_n)$ eines Bereichs des $\mathbb{R}^n$ eine reelle Zahl $f(\boldsymbol{x})=f(x_1,\dots,x_n)$ zu. Eine einzelne reelle Zahl nennt man in diesem Zusammenhang einen __Skalar__, um sie von einem Vektor zu unterscheiden. Eine Funktion, deren Werte Skalare sind, heißt deshalb eine __skalare Funktion__.

**Graph.** Bei zwei Variablen kann man über jedem Punkt $(x,y)$ der Ebene die Höhe $z=f(x,y)$ auftragen. So entsteht eine Fläche im Raum, der __Graph__ von $f$.

**Höhenlinien.** Für eine Zahl $c$ heißt die Menge aller Punkte $(x,y)$ mit $f(x,y)=c$ die __Höhenlinie__ von $f$ zum Wert $c$. Sie ist die Schnittlinie des Graphen mit der waagerechten Ebene in der Höhe $c$, von oben gesehen. Bei drei Variablen ist die Menge aller Punkte mit $f(x,y,z)=c$ meist eine Fläche. Sie heißt __Niveaufläche__.

::::beispiel
Die Funktion $\varphi(x,y)=x^2+2y^2$ heißt in diesem Kapitel die *Schale*, weil ihr Graph wie eine Schale aussieht. Es ist $\varphi(0,0)=0$, $\varphi(2,0)=4$, $\varphi(0,1)=2$ und $\varphi(1,1)=3$. Die Höhenlinie zum Wert $3$ besteht aus den Punkten mit $x^2+2y^2=3$. Das ist eine Ellipse um den Nullpunkt, die die $x$-Achse bei $\pm\sqrt3$ und die $y$-Achse bei $\pm\sqrt{3/2}$ schneidet und durch $(1,1)$ läuft.
::::

⁠**Kurz gesagt:** Eine skalare Funktion ordnet jedem Punkt eine Zahl zu. Man zeichnet sie als Landkarte mit Höhenlinien.

### Was du dafür brauchst: Grenzwert und Stetigkeit in mehreren Variablen

<span class="anker" id="stufe-1-6"></span>

Ableitungen sind Grenzwerte. Bei mehreren Variablen kann man sich einem Punkt auf unendlich vielen Wegen nähern, und ein Grenzwert soll auf jedem dieser Wege derselbe sein.

**Folgen von Punkten.** Eine Folge von Punkten $\boldsymbol{x}_\nu\in\mathbb{R}^n$, $\nu=1,2,3,\dots$, __konvergiert__ gegen $\boldsymbol{x}_0$, wenn ihr Abstand $|\boldsymbol{x}_\nu-\boldsymbol{x}_0|$ zu $\boldsymbol{x}_0$ gegen null geht. Man schreibt $\boldsymbol{x}_\nu\to\boldsymbol{x}_0$.

**Grenzwert.** Sei $f$ eine skalare Funktion, die in allen Punkten nahe $\boldsymbol{x}_0$ erklärt ist, außer vielleicht in $\boldsymbol{x}_0$ selbst. Man schreibt

$$\lim_{\boldsymbol{x}\to\boldsymbol{x}_0}f(\boldsymbol{x})=c$$

und nennt die Zahl $c$ den __Grenzwert__ von $f$ in $\boldsymbol{x}_0$, wenn für jede Folge $\boldsymbol{x}_\nu\to\boldsymbol{x}_0$ mit $\boldsymbol{x}_\nu\neq\boldsymbol{x}_0$ die Zahlen $f(\boldsymbol{x}_\nu)$ gegen $c$ gehen. Gibt es zwei Folgen, längs derer $f$ verschiedenen Zahlen zustrebt, gibt es keinen Grenzwert.

**Stetigkeit.** Die Funktion $f$ heißt __stetig__ in $\boldsymbol{x}_0$, wenn sie dort erklärt ist und $\lim_{\boldsymbol{x}\to\boldsymbol{x}_0}f(\boldsymbol{x})=f(\boldsymbol{x}_0)$ gilt. Sie heißt stetig, wenn sie in jedem Punkt ihres Bereichs stetig ist. Summen, Produkte und Verkettungen stetiger Funktionen sind stetig, Quotienten überall dort, wo der Nenner nicht null ist. Deshalb sind zum Beispiel alle Polynome in $x_1,\dots,x_n$ stetig.

::::beispiel
Die Schale $\varphi(x,y)=x^2+2y^2$ ist ein Polynom und damit stetig. Anders die Funktion $q(x,y)=\dfrac{x^2-y^2}{x^2+y^2}$ für $(x,y)\neq(0,0)$, ergänzt durch $q(0,0)=0$. Längs der Folge $(1/\nu,\,0)$ ist $q=1$, längs der Folge $(0,\,1/\nu)$ ist $q=-1$. Beide Folgen gehen gegen den Nullpunkt, aber die Funktionswerte streben verschiedenen Zahlen zu. Also hat $q$ im Nullpunkt keinen Grenzwert und ist dort nicht stetig.
::::

⁠**Kurz gesagt:** Ein Grenzwert in mehreren Variablen existiert nur, wenn jede Annäherung an den Punkt denselben Wert liefert. Stetig heißt: Der Grenzwert ist der Funktionswert.

### Was du dafür brauchst: Partielle Ableitungen

<span class="anker" id="stufe-1-7"></span>

Wie stark ändert sich $f(x,y)$, wenn man nur $x$ ändert und $y$ festhält? Hält man $y$ fest, bleibt eine Funktion der einen Variablen $x$ übrig, und deren Ableitung kennt man.

Im Bild der Landkarte läuft man auf einer waagerechten Geraden $y=\text{konst}$ und beobachtet, wie die Höhe steigt oder fällt (Abb. [2](#abb-2)). Die Steigung an der Stelle, an der man gerade steht, ist die partielle Ableitung nach $x$.

:::abbildung hm3/k1partiell 2
Links: Auf der roten Geraden $y=1$ ändert sich nur $x$; blau die Höhenlinien der Schale. Rechts: Längs dieser Geraden ist $\varphi(x,1)=x^2+2$ eine Funktion der einen Variablen $x$. Ihre Steigung bei $x=1$ (gestrichelt die Tangente) ist die partielle Ableitung $\frac{\partial\varphi}{\partial x}(1,1)=2$.
:::

:::definition Definition 1.1 (Partielle Ableitung)
<span class="anker" id="satz-1-1"></span>

Sei $f$ eine skalare Funktion von $n$ Variablen, die in allen Punkten nahe $\boldsymbol{x}$ erklärt ist. Die __partielle Ableitung__ von $f$ nach $x_k$ im Punkt $\boldsymbol{x}$ ist

<span class="anker" id="gl-1-1"></span>
$$\frac{\partial f}{\partial x_k}(\boldsymbol{x})=\lim_{t\to0}\frac{f(\boldsymbol{x}+t\,\hat{\boldsymbol{e}}_k)-f(\boldsymbol{x})}{t}, \tag{1.1}$$

falls dieser Grenzwert existiert. Existieren in jedem Punkt alle partiellen Ableitungen, heißt $f$ __partiell differenzierbar__.
:::

⁠**So liest man das:** Der Punkt $\boldsymbol{x}+t\,\hat{\boldsymbol{e}}_k$ unterscheidet sich von $\boldsymbol{x}$ nur in der Komponente $k$, und zwar um $t$. Der Bruch ist also der gewöhnliche Differenzenquotient in Richtung der $x_k$-Achse. Beim Rechnen leitet man nach $x_k$ ab und behandelt alle anderen Variablen wie Konstanten. Statt $\frac{\partial f}{\partial x_k}$ schreibt man auch kurz $\partial_{x_k}f$.

::::beispiel
Für die Schale $\varphi(x,y)=x^2+2y^2$ ist

$$\frac{\partial\varphi}{\partial x}=2x,\qquad \frac{\partial\varphi}{\partial y}=4y,\qquad\text{also}\qquad \frac{\partial\varphi}{\partial x}(1,1)=2,\quad\frac{\partial\varphi}{\partial y}(1,1)=4.$$

Zur Kontrolle der Differenzenquotient mit $t=\frac1{10}$: $\bigl(\varphi(1{,}1;\,1)-\varphi(1,1)\bigr)/0{,}1=(3{,}21-3)/0{,}1=2{,}1$, nahe bei $2$. Mit drei Variablen: Für $f(x,y,z)=xy^2z^3$ ist $\partial f/\partial y=2xyz^3$.
::::

⁠**Kurz gesagt:** Die partielle Ableitung nach $x_k$ ist die Steigung in Richtung der $x_k$-Achse. Man berechnet sie, indem man alle anderen Variablen festhält.

### Was du dafür brauchst: Höhere partielle Ableitungen

<span class="anker" id="stufe-1-8"></span>

Die partiellen Ableitungen einer Funktion sind selbst wieder Funktionen. Oft lassen sie sich erneut ableiten.

Leitet man $\partial f/\partial x_k$ nach $x_j$ ab, entsteht die __zweite partielle Ableitung__

$$\frac{\partial^2 f}{\partial x_j\,\partial x_k}=\frac{\partial}{\partial x_j}\Bigl(\frac{\partial f}{\partial x_k}\Bigr).$$

Gelesen wird von rechts nach links: zuerst nach $x_k$, dann nach $x_j$. Bei zwei gleichen Variablen schreibt man $\partial^2f/\partial x_k^2$. Für $j\neq k$ nennt man sie eine __gemischte__ partielle Ableitung. Ebenso gibt es dritte und höhere partielle Ableitungen. Wie oft insgesamt abgeleitet wird, heißt die __Ordnung__ der Ableitung.

::::beispiel
Für $f(x,y)=x^2y^3$ ist $\partial f/\partial x=2xy^3$ und $\partial f/\partial y=3x^2y^2$. Daraus folgen die vier zweiten partiellen Ableitungen

$$\frac{\partial^2 f}{\partial x^2}=2y^3,\qquad \frac{\partial^2 f}{\partial y\,\partial x}=6xy^2,\qquad \frac{\partial^2 f}{\partial x\,\partial y}=6xy^2,\qquad \frac{\partial^2 f}{\partial y^2}=6x^2y .$$

Die beiden gemischten Ableitungen stimmen hier überein, obwohl sie auf verschiedenen Wegen entstanden sind.
::::

⁠**Kurz gesagt:** Höhere partielle Ableitungen entstehen durch wiederholtes Ableiten. Die Ordnung zählt, wie oft abgeleitet wurde.

### Was du dafür brauchst: Offene Mengen

<span class="anker" id="stufe-1-9"></span>

Um in einem Punkt abzuleiten, muss man von ihm aus ein kleines Stück in jede Richtung gehen können, ohne den Bereich zu verlassen, in dem die Funktion erklärt ist. Am Rand eines Bereichs ist das nicht möglich (Abb. [3](#abb-3)).

:::abbildung hm3/k1offen 3
Links: Die Kreisscheibe ohne ihren Rand (gestrichelt) ist offen. Um jeden ihrer Punkte passt eine kleine Kreisscheibe, die ganz in ihr liegt; je näher der Punkt am Rand liegt, desto kleiner muss sie sein. Rechts: Gehört der Rand dazu, ist die Menge nicht offen. Um einen Randpunkt ragt jede noch so kleine Kreisscheibe nach außen.
:::

Die __Kugel__ um $\boldsymbol{x}_0$ mit dem Radius $\rho>0$ ist die Menge aller Punkte, deren Abstand zu $\boldsymbol{x}_0$ kleiner als $\rho$ ist:

$$\{\boldsymbol{x}\in\mathbb{R}^n:\ |\boldsymbol{x}-\boldsymbol{x}_0|<\rho\}.$$

In der Ebene ist das eine Kreisscheibe ohne ihren Randkreis.

:::definition Definition 1.2 (Offene Menge)
<span class="anker" id="satz-1-2"></span>

Eine Menge $\mathcal U\subset\mathbb{R}^n$ heißt __offen__, wenn um jeden Punkt von $\mathcal U$ eine Kugel liegt, die ganz in $\mathcal U$ enthalten ist.
:::

::::beispiel
Die Kreisscheibe $\{|\boldsymbol{x}|<1\}$ in der Ebene ist offen: Um einen Punkt $\boldsymbol{x}_0$ mit $|\boldsymbol{x}_0|<1$ liegt die Kugel mit dem Radius $\rho=1-|\boldsymbol{x}_0|$ ganz in ihr. Ebenso offen sind der ganze $\mathbb{R}^n$, der $\mathbb{R}^n$ ohne den Nullpunkt, geschrieben $\mathbb{R}^n\setminus\{0\}$ (Radius $\rho=|\boldsymbol{x}_0|$), und die Halbebene $\{(x,y):x+y>0\}$. Die Kreisscheibe mit Rand, $\{|\boldsymbol{x}|\le1\}$, ist nicht offen: Jede Kugel um den Randpunkt $(1,0)$ enthält Punkte mit $|\boldsymbol{x}|>1$.
::::

⁠**Kurz gesagt:** Von jedem Punkt einer offenen Menge aus kann man ein Stück in jede Richtung gehen, ohne die Menge zu verlassen.

### Abbildungen mit mehreren Ausgängen

<span class="anker" id="stufe-1-10"></span>

Viele Größen bestehen aus mehreren Zahlen, die alle vom Ort abhängen, zum Beispiel die drei Komponenten einer Kraft. Eine skalare Funktion liefert nur eine Zahl. Man braucht also Funktionen, die einen Vektor liefern.

Man kann sich eine solche Funktion als Gerät mit $n$ Eingängen und $m$ Ausgängen vorstellen. An jedem Ausgang erscheint eine Zahl, und jede dieser Zahlen darf von allen Eingängen abhängen.

:::definition Definition 1.3 (Abbildung und Komponentenfunktionen)
<span class="anker" id="satz-1-3"></span>

Sei $\mathcal U\subset\mathbb{R}^n$ offen. Eine __Abbildung__ $\boldsymbol f\colon\mathcal U\to\mathbb{R}^m$ ordnet jedem Punkt $\boldsymbol{x}\in\mathcal U$ einen Vektor

$$\boldsymbol f(\boldsymbol{x})=\bigl(f_1(\boldsymbol{x}),\dots,f_m(\boldsymbol{x})\bigr)\in\mathbb{R}^m$$

zu. Die skalaren Funktionen $f_1,\dots,f_m$ heißen die __Komponentenfunktionen__ von $\boldsymbol f$.
:::

Für $m=1$ ist eine Abbildung eine skalare Funktion; man setzt sie dann nicht fett. Eine Abbildung heißt stetig oder partiell differenzierbar, wenn alle ihre Komponentenfunktionen stetig oder partiell differenzierbar sind.

::::beispiel
Die Abbildung $\boldsymbol f\colon\mathbb{R}^2\to\mathbb{R}^2$,

$$\boldsymbol f(x,y)=\bigl(x^2-y^2,\;2xy\bigr),$$

hat die Komponentenfunktionen $f_1(x,y)=x^2-y^2$ und $f_2(x,y)=2xy$. Im Punkt $(1,\frac12)$ liefert sie $\boldsymbol f(1,\tfrac12)=(1-\tfrac14,\;1)=(\tfrac34,\,1)$. Ein Beispiel mit verschieden vielen Ein- und Ausgängen ist $\boldsymbol g\colon\mathbb{R}^3\to\mathbb{R}^2$, $\boldsymbol g(x,y,z)=(xyz,\;x+y)$.
::::

⁠**Kurz gesagt:** Eine Abbildung von $\mathbb{R}^n$ nach $\mathbb{R}^m$ besteht aus $m$ skalaren Funktionen von $n$ Variablen.

### Vektorfelder

<span class="anker" id="stufe-1-11"></span>

Ein elektrisches Feld oder die Geschwindigkeit einer Strömung ordnet jedem Punkt des Raums einen Pfeil zu. Der Pfeil gehört zu diesem Punkt: Man zeichnet ihn so, dass er dort beginnt (Abb. [4](#abb-4)).

:::abbildung hm3/k1feld 4
Das Drehfeld $\boldsymbol{E}(x,y)=(-y,x)$. An jedem Gitterpunkt beginnt der Pfeil $\boldsymbol{E}(x,y)$, auf $0{,}3$ seiner Länge verkleinert, damit sich die Pfeile nicht überdecken. Rot der Pfeil $\boldsymbol{E}(1,0)=(0,1)$. Die Pfeile laufen gegen den Uhrzeigersinn um den Nullpunkt und werden nach außen länger.
:::

:::definition Definition 1.4 (Vektorfeld)
<span class="anker" id="satz-1-4"></span>

Sei $\mathcal U\subset\mathbb{R}^n$ offen. Eine Abbildung $\boldsymbol{E}\colon\mathcal U\to\mathbb{R}^n$, die jedem Punkt einen Vektor mit ebenso vielen Komponenten zuordnet, heißt __Vektorfeld__ auf $\mathcal U$. Man schreibt $\boldsymbol{E}=(E_1,\dots,E_n)$.
:::

Rechnerisch ist ein Vektorfeld eine Abbildung mit $m=n$. Der Unterschied liegt in der Deutung: Eingang und Ausgang leben im selben Raum, und der Wert $\boldsymbol{E}(\boldsymbol{x})$ wird als Pfeil gezeichnet, der im Punkt $\boldsymbol{x}$ beginnt.

::::beispiel [Beispiel 1] das Drehfeld
$\boldsymbol{E}(x,y)=(-y,\,x)$ auf $\mathbb{R}^2$. Im Punkt $(1,0)$ ist $\boldsymbol{E}=(0,1)$, der Pfeil zeigt nach oben. Im Punkt $(0,1)$ ist $\boldsymbol{E}=(-1,0)$, er zeigt nach links, im Punkt $(-1,0)$ ist $\boldsymbol{E}=(0,-1)$, er zeigt nach unten. Die Länge $|\boldsymbol{E}(x,y)|=\sqrt{y^2+x^2}$ ist der Abstand des Punkts vom Nullpunkt. In diesem Kapitel heißt dieses Feld das *Drehfeld*.
::::

::::beispiel [Beispiel 2] das Strahlfeld
$\boldsymbol{E}(\boldsymbol{x})=\boldsymbol{x}$ auf $\mathbb{R}^n$. Der Pfeil im Punkt $\boldsymbol{x}$ zeigt vom Nullpunkt weg und ist so lang wie der Abstand zum Nullpunkt. In diesem Kapitel heißt es das *Strahlfeld*.
::::

⁠**Kurz gesagt:** Ein Vektorfeld heftet an jeden Punkt einen Pfeil derselben Dimension.

### Die Jacobi-Matrix

<span class="anker" id="stufe-1-12"></span>

Eine Abbildung mit $n$ Eingängen und $m$ Ausgängen hat $m\cdot n$ erste partielle Ableitungen, denn jede der $m$ Komponentenfunktionen lässt sich nach jeder der $n$ Variablen ableiten. Man braucht eine übersichtliche Anordnung für sie.

Man stellt sich eine Tabelle vor. Jede Zeile gehört zu einem Ausgang $f_j$, jede Spalte zu einem Eingang $x_k$. Im Feld in Zeile $j$ und Spalte $k$ steht, wie stark der Ausgang $f_j$ auf den Eingang $x_k$ reagiert:

$$\begin{array}{c|ccc} & x_1 & \cdots & x_n\\\hline f_1 & \partial f_1/\partial x_1 & \cdots & \partial f_1/\partial x_n\\ \vdots & \vdots & & \vdots\\ f_m & \partial f_m/\partial x_1 & \cdots & \partial f_m/\partial x_n \end{array}$$

:::definition Definition 1.5 (Jacobi-Matrix)
<span class="anker" id="satz-1-5"></span>

Sei $\mathcal U\subset\mathbb{R}^n$ offen und $\boldsymbol f=(f_1,\dots,f_m)\colon\mathcal U\to\mathbb{R}^m$ partiell differenzierbar. Die Matrix

<span class="anker" id="gl-1-2"></span>
$$D\boldsymbol f=\Bigl(\frac{\partial f_j}{\partial x_k}\Bigr)_{jk}=\begin{pmatrix}\frac{\partial f_1}{\partial x_1}&\cdots&\frac{\partial f_1}{\partial x_n}\\\vdots&\ddots&\vdots\\\frac{\partial f_m}{\partial x_1}&\cdots&\frac{\partial f_m}{\partial x_n}\end{pmatrix}\in\mathbb{R}^{m\times n} \tag{1.2}$$

heißt __Jacobi-Matrix__ von $\boldsymbol f$. Ihren Wert im Punkt $\boldsymbol{x}$ schreibt man $D\boldsymbol f(\boldsymbol{x})$.
:::

⁠**So liest man das:** Der Index $j$ zählt die Zeilen, also die Ausgänge. Der Index $k$ zählt die Spalten, also die Eingänge. Zeile $j$ enthält alle Ableitungen der einen Komponentenfunktion $f_j$. Spalte $k$ enthält die Ableitungen aller Komponentenfunktionen nach der einen Variablen $x_k$. Die Jacobi-Matrix ist an jedem Punkt eine andere Matrix, sie hängt also selbst von $\boldsymbol{x}$ ab.

::::beispiel [Beispiel 1]
Für $\boldsymbol f(x,y)=(x^2-y^2,\;2xy)$ ist zum Beispiel $\partial f_2/\partial x=2y$ der Eintrag in Zeile $2$, Spalte $1$. Insgesamt

$$D\boldsymbol f(x,y)=\begin{pmatrix}2x&-2y\\2y&2x\end{pmatrix},\qquad D\boldsymbol f(1,\tfrac12)=\begin{pmatrix}2&-1\\1&2\end{pmatrix}.$$
::::

::::beispiel [Beispiel 2]
Das Drehfeld $\boldsymbol{E}(x,y)=(-y,x)$ hat an jedem Punkt dieselbe Jacobi-Matrix $D\boldsymbol{E}=\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)$, denn $E_1=-y$ hängt nur von $y$ ab und $E_2=x$ nur von $x$.
::::

⁠**Grenzfall:** Für $n=m=1$ ist $Df=(f')$ eine $1\times1$-Matrix, die gewöhnliche Ableitung.

⁠**Kurz gesagt:** Die Jacobi-Matrix ist die Tabelle aller ersten partiellen Ableitungen einer Abbildung: Zeilen gehören zu den Ausgängen, Spalten zu den Eingängen.

### Der Gradient

<span class="anker" id="stufe-1-13"></span>

Bei einer skalaren Funktion besteht die Jacobi-Matrix aus einer einzigen Zeile: den Steigungen in Richtung der Achsen. Schreibt man diese Zahlen untereinander, bilden sie einen Vektor, und den kann man als Pfeil in die Landkarte zeichnen.

Im Punkt $(1,1)$ steigt die Schale $\varphi=x^2+2y^2$ in $x$-Richtung mit der Steigung $2$ und in $y$-Richtung mit der Steigung $4$. Aus diesen beiden Zahlen setzt man den Pfeil $(2,4)$ zusammen (Abb. [5](#abb-5)).

:::abbildung hm3/k1gradpfeil 5
Der Gradient der Schale $\varphi(x,y)=x^2+2y^2$ im Punkt $(1,1)$. Die partiellen Ableitungen $2$ und $4$ sind die Steigungen in $x$- und $y$-Richtung. Als Komponenten eines Vektors ergeben sie den schwarzen Pfeil $(2,4)^T$, hier auf ein Viertel verkleinert. Blau die Höhenlinien.
:::

:::definition Definition 1.6 (Gradient)
<span class="anker" id="satz-1-6"></span>

Sei $\mathcal U\subset\mathbb{R}^n$ offen und $f\colon\mathcal U\to\mathbb{R}$ eine partiell differenzierbare skalare Funktion. Der Spaltenvektor

<span class="anker" id="gl-1-3"></span>
$$\operatorname{grad}f=\begin{pmatrix}\partial f/\partial x_1\\\vdots\\\partial f/\partial x_n\end{pmatrix}=\Bigl(\frac{\partial f}{\partial x_1},\dots,\frac{\partial f}{\partial x_n}\Bigr)^T\in\mathbb{R}^n \tag{1.3}$$

heißt __Gradient__ von $f$. Man schreibt dafür auch $\nabla f$, gelesen „Nabla $f$“.
:::

Ordnet man jedem Punkt $\boldsymbol{x}\in\mathcal U$ den Vektor $\nabla f(\boldsymbol{x})$ zu, entsteht ein Vektorfeld auf $\mathcal U$. Der Gradient macht also aus einer skalaren Funktion ein Vektorfeld.

::::beispiel
Für die Schale ist $\nabla\varphi(x,y)=(2x,\,4y)^T$. Im Punkt $(1,1)$ ist $\nabla\varphi=(2,4)^T$, im Nullpunkt ist $\nabla\varphi=(0,0)^T$: Am Boden der Schale steigt sie in keiner Achsenrichtung. Mit drei Variablen: Für $f(x,y,z)=xy^2z^3$ ist $\nabla f=(y^2z^3,\;2xyz^3,\;3xy^2z^2)^T$.
::::

⁠**Kurz gesagt:** Der Gradient ist der Vektor der partiellen Ableitungen einer skalaren Funktion. Er heftet an jeden Punkt einen Pfeil.

### Das Nabla-Symbol

<span class="anker" id="stufe-1-14"></span>

Den Gradienten erhält man, indem man auf $f$ nacheinander die Ableitungen nach $x_1,\dots,x_n$ anwendet und die Ergebnisse untereinander schreibt. Diese Liste von Ableitungsbefehlen bekommt ein eigenes Zeichen.

Man kann sie sich wie einen Vektor vorstellen, dessen Einträge keine Zahlen sind, sondern Anweisungen: „leite nach $x_1$ ab“, „leite nach $x_2$ ab“ und so weiter. Schreibt man eine Funktion rechts daneben, wird jede Anweisung auf sie angewendet.

:::definition Definition 1.7 (Nabla-Symbol)
<span class="anker" id="satz-1-7"></span>

Das __Nabla-Symbol__ ist der Spaltenvektor aus Ableitungsbefehlen

<span class="anker" id="gl-1-4"></span>
$$\nabla=\Bigl(\frac{\partial}{\partial x_1},\dots,\frac{\partial}{\partial x_n}\Bigr)^T. \tag{1.4}$$
:::

Steht rechts daneben eine skalare Funktion $f$, wird jeder Eintrag auf $f$ angewendet, und es entsteht der Gradient: $\nabla f=(\partial f/\partial x_1,\dots,\partial f/\partial x_n)^T=\operatorname{grad}f$. So wie $\frac{\mathrm{d}}{\mathrm{d} x}$ ohne Funktion dahinter keine Zahl ist, hat $\nabla$ für sich allein keinen Wert. Es hat nur die Form eines Spaltenvektors.

::::beispiel
Für $f(x,y)=x^2y$ in der Ebene ist $\nabla=(\partial/\partial x,\,\partial/\partial y)^T$ und

$$\nabla f=\begin{pmatrix}\partial(x^2y)/\partial x\\\partial(x^2y)/\partial y\end{pmatrix}=\begin{pmatrix}2xy\\x^2\end{pmatrix}.$$
::::

⁠**Kurz gesagt:** $\nabla$ ist ein Spaltenvektor aus Ableitungsbefehlen. Erst mit einer Funktion dahinter ergibt es etwas, nämlich den Gradienten.

### Gradient und Jacobi-Matrix: Spalte und Zeile

<span class="anker" id="stufe-1-15"></span>

Gradient und Jacobi-Matrix einer skalaren Funktion enthalten dieselben Zahlen. Sie sind trotzdem verschiedene Objekte, und man muss sie auseinanderhalten.

Für eine skalare Funktion $f$, also $m=1$, hat die Jacobi-Matrix eine einzige Zeile: $Df\in\mathbb{R}^{1\times n}$ ist ein Zeilenvektor. Der Gradient ist ein Spaltenvektor. Es gilt

<span class="anker" id="gl-1-5"></span>
$$\nabla f=(Df)^T . \tag{1.5}$$

Für eine Abbildung $\boldsymbol f=(f_1,\dots,f_m)$ ist Zeile $j$ der Jacobi-Matrix die Jacobi-Matrix der Komponentenfunktion $f_j$. Die Zeilen der Jacobi-Matrix sind also die transponierten Gradienten der Komponentenfunktionen: Zeile $j$ von $D\boldsymbol f$ ist $(\nabla f_j)^T$.

Multipliziert man die Zeile $Df(\boldsymbol{x})$ mit einem Spaltenvektor $\boldsymbol s\in\mathbb{R}^n$, ergibt Zeile mal Spalte das Skalarprodukt: $Df(\boldsymbol{x})\,\boldsymbol s=\nabla f(\boldsymbol{x})\cdot\boldsymbol s$.

::::beispiel
Für $\boldsymbol f(x,y)=(x^2-y^2,\;2xy)$ ist $\nabla f_1=(2x,\,-2y)^T$ und $\nabla f_2=(2y,\,2x)^T$. Transponiert und untereinander geschrieben, ergeben sie die Jacobi-Matrix $\bigl(\begin{smallmatrix}2x&-2y\\2y&2x\end{smallmatrix}\bigr)$ aus Unterabschnitt [1.12](#stufe-1-12).
::::

⁠**Kurz gesagt:** Der Gradient ist eine Spalte, die Jacobi-Matrix einer skalaren Funktion eine Zeile mit denselben Einträgen. Die Zeilen der Jacobi-Matrix einer Abbildung sind die transponierten Gradienten ihrer Komponentenfunktionen.

:::hintergrund Warum man Zeile und Spalte unterscheidet, obwohl es dieselben Zahlen sind
Die beiden Schreibweisen haben verschiedene Aufgaben. Die Spalte $\nabla f(\boldsymbol{x})$ ist ein Vektor im Raum der Eingänge. Man zeichnet sie als Pfeil, der im Punkt $\boldsymbol{x}$ beginnt, wie in Abb. [5](#abb-5). Die Zeile $Df(\boldsymbol{x})$ ist eine Matrix. Man multipliziert sie mit einem Vektor und erhält eine Zahl. Bei einer Abbildung mit mehreren Ausgängen gibt es nur noch die Matrix $D\boldsymbol f$. Sie hat mehrere Zeilen, und keine davon ist allein „der Gradient von $\boldsymbol f$“.
:::

### Differentialoperatoren

<span class="anker" id="stufe-1-16"></span>

Der Gradient ist eine Vorschrift, die aus einer Funktion durch Ableiten eine neue Funktion macht. Solche Vorschriften kommen in diesem Kapitel mehrfach vor, deshalb bekommen sie einen Namen.

Man kann sich eine Maschine vorstellen: Oben steckt man eine Funktion hinein, die Maschine leitet sie auf eine festgelegte Weise ab, und unten kommt eine neue Funktion heraus.

:::definition Definition 1.8 (Differentialoperator)
<span class="anker" id="satz-1-8"></span>

Eine Vorschrift, die einer Funktion mit Hilfe ihrer partiellen Ableitungen eine neue Funktion zuordnet, heißt __Differentialoperator__. Die höchste Ordnung der Ableitungen, die er benutzt, heißt seine Ordnung.
:::

::::beispiel
$f\mapsto f'$ ist ein Differentialoperator erster Ordnung für Funktionen einer Variablen, $f\mapsto f''$ einer zweiter Ordnung. Für Funktionen von zwei Variablen ist $f\mapsto\partial^2f/\partial x^2+\partial f/\partial y$ ein Differentialoperator zweiter Ordnung; für $f=x^2y$ liefert er $2y+x^2$. Der Gradient $f\mapsto\nabla f$ braucht nur erste partielle Ableitungen. Er ist ein Differentialoperator erster Ordnung, der aus einer skalaren Funktion ein Vektorfeld macht.
::::

⁠**Kurz gesagt:** Ein Differentialoperator macht durch Ableiten aus einer Funktion eine neue. Der Gradient ist einer erster Ordnung.

### Totale Differenzierbarkeit

<span class="anker" id="stufe-1-17"></span>

Partielle Ableitungen schauen nur entlang der Achsen. Eine Ableitung soll aber beschreiben, wie sich die Abbildung bei *jedem* kleinen Schritt ändert, in welche Richtung er auch geht. Dieser Unterabschnitt sagt, wann die Jacobi-Matrix das leistet.

**Die Idee aus einer Variablen.** Bei einer Funktion einer Variablen gilt nahe $x_0$

$$f(x_0+s)\approx f(x_0)+f'(x_0)\,s .$$

Der Fehler dieser Näherung wird für kleine $s$ nicht nur klein, er wird schneller klein als der Schritt $s$ selbst:

$$\frac{f(x_0+s)-f(x_0)-f'(x_0)\,s}{s}=\frac{f(x_0+s)-f(x_0)}{s}-f'(x_0)\;\longrightarrow\;0\qquad(s\to0).$$

Das ist nur eine Umformung der Definition der Ableitung. Die Näherung ersetzt die Funktion nahe $x_0$ durch eine Gerade, die __lineare Näherung__.

**Mehrere Variablen.** Bei einer Abbildung $\boldsymbol f\colon\mathcal U\to\mathbb{R}^m$ mit $\mathcal U\subset\mathbb{R}^n$ ist der Schritt $\boldsymbol s$ ein Vektor im $\mathbb{R}^n$ und die Änderung des Werts ein Vektor im $\mathbb{R}^m$. Statt mit einer Zahl muss man den Schritt also mit einer Matrix $A\in\mathbb{R}^{m\times n}$ multiplizieren:

$$\boldsymbol f(\boldsymbol{x}_0+\boldsymbol s)\approx\boldsymbol f(\boldsymbol{x}_0)+A\,\boldsymbol s .$$

Abb. [6](#abb-6) zeigt, was das bedeutet. Die Abbildung biegt ein kleines Quadrat zu einem krummen Viereck. Die Näherung ersetzt das krumme Viereck durch ein Parallelogramm, und je kleiner das Quadrat, desto besser passt es.

:::abbildung hm3/k1jacobi 6
Die Abbildung $\boldsymbol f(x,y)=(x^2-y^2,\,2xy)$ biegt ein kleines Quadrat um $(1,\tfrac12)$ zu einem krummen Viereck (rechts, blau). Die Spalten der Jacobi-Matrix $D\boldsymbol f(1,\tfrac12)$, mit der halben Seitenlänge $0{,}3$ des Quadrats multipliziert, sind die beiden Pfeile rechts. Sie spannen das gestrichelte Parallelogramm auf: die lineare Näherung des Bilds.
:::

:::definition Definition 1.9 (Totale Differenzierbarkeit)
<span class="anker" id="satz-1-9"></span>

Sei $\mathcal U\subset\mathbb{R}^n$ offen. Eine Abbildung $\boldsymbol f\colon\mathcal U\to\mathbb{R}^m$ heißt im Punkt $\boldsymbol{x}_0\in\mathcal U$ __total differenzierbar__, wenn es eine Matrix $A\in\mathbb{R}^{m\times n}$ gibt mit

<span class="anker" id="gl-1-6"></span>
$$\lim_{\boldsymbol{x}\to\boldsymbol{x}_0}\frac{|\boldsymbol f(\boldsymbol{x})-\boldsymbol f(\boldsymbol{x}_0)-A(\boldsymbol{x}-\boldsymbol{x}_0)|}{|\boldsymbol{x}-\boldsymbol{x}_0|}=0. \tag{1.6}$$

Statt total differenzierbar sagt man auch kurz __differenzierbar__. Die Abbildung heißt differenzierbar auf $\mathcal U$, wenn sie in jedem Punkt von $\mathcal U$ differenzierbar ist.
:::

⁠**So liest man das:** Mit dem Schritt $\boldsymbol s=\boldsymbol{x}-\boldsymbol{x}_0$ ist der Zähler die Länge des Fehlers der Näherung $\boldsymbol f(\boldsymbol{x}_0)+A\boldsymbol s$, der Nenner die Länge des Schritts. Der Bruch ist eine skalare Funktion von $\boldsymbol{x}$, und ihr Grenzwert ist null. Das heißt: Der Fehler verschwindet schneller als der Schritt, und zwar gleichgültig, auf welchem Weg $\boldsymbol{x}$ sich $\boldsymbol{x}_0$ nähert. Für $m=n=1$ steht dort die Bedingung aus einer Variablen von oben.

Welche Matrix kommt als $A$ in Frage? Geht man nur in Achsenrichtung, misst man partielle Ableitungen. Daraus folgt:

:::satz Satz 1.10 (Die Näherung ist die Jacobi-Matrix)
<span class="anker" id="satz-1-10"></span>

Ist $\boldsymbol f$ in $\boldsymbol{x}_0$ differenzierbar, dann existieren dort alle partiellen Ableitungen, und die Matrix in [(1.6)](#gl-1-6) ist die Jacobi-Matrix: $A=D\boldsymbol f(\boldsymbol{x}_0)$.
:::

:::beweis Die Spalten von $A$
Nähere dich $\boldsymbol{x}_0$ längs der $x_k$-Achse: $\boldsymbol{x}=\boldsymbol{x}_0+t\,\hat{\boldsymbol{e}}_k$ mit $t\to0$. Dann ist $|\boldsymbol{x}-\boldsymbol{x}_0|=|t|$, und [(1.6)](#gl-1-6) sagt

$$\Bigl|\frac{\boldsymbol f(\boldsymbol{x}_0+t\,\hat{\boldsymbol{e}}_k)-\boldsymbol f(\boldsymbol{x}_0)}{t}-A\,\hat{\boldsymbol{e}}_k\Bigr|\longrightarrow0 .$$

Komponente $j$ des Bruchs ist der Differenzenquotient von $f_j$ in Richtung $x_k$. Er geht also gegen die Komponente $j$ von $A\,\hat{\boldsymbol{e}}_k$, und das ist der Eintrag $A_{jk}$. Damit existiert die partielle Ableitung $\partial f_j/\partial x_k(\boldsymbol{x}_0)$, und sie ist gleich $A_{jk}$.
:::

Für eine differenzierbare Abbildung gilt also für kleine Schritte $\boldsymbol s$

<span class="anker" id="gl-1-7"></span>
$$\boldsymbol f(\boldsymbol{x}_0+\boldsymbol s)\approx\boldsymbol f(\boldsymbol{x}_0)+D\boldsymbol f(\boldsymbol{x}_0)\,\boldsymbol s , \tag{1.7}$$

in Worten: Änderung ist ungefähr Jacobi-Matrix mal Schritt. Jetzt erhalten Zeilen und Spalten der Jacobi-Matrix eine anschauliche Bedeutung. Ein Schritt um $s_k$ in Richtung $x_k$ ändert den Ausgang um etwa $s_k$ mal Spalte $k$. Spalte $k$ sagt also, was ein Schritt in Richtung $x_k$ bewirkt. Zeile $j$ sagt, wie der Ausgang $f_j$ auf Schritte in alle Richtungen reagiert.

:::hintergrund Warum der Fehler schneller verschwinden muss als der Schritt
Man könnte fordern, dass der Fehler $\boldsymbol f(\boldsymbol{x}_0+\boldsymbol s)-\boldsymbol f(\boldsymbol{x}_0)-A\boldsymbol s$ nur gegen null geht. Das sagt aber nichts: Ist $\boldsymbol f$ stetig, gehen $\boldsymbol f(\boldsymbol{x}_0+\boldsymbol s)-\boldsymbol f(\boldsymbol{x}_0)$ und $A\boldsymbol s$ beide gegen null, für *jede* Matrix $A$. Erst die Forderung, dass der Fehler schneller verschwindet als $|\boldsymbol s|$, legt die Matrix fest. Erfüllen zwei Matrizen $A$ und $A'$ die Bedingung [(1.6)](#gl-1-6), dann geht auch die Differenz der beiden Fehler, geteilt durch $|\boldsymbol s|$, gegen null, also $(A-A')\boldsymbol s/|\boldsymbol s|\to0$. Mit $\boldsymbol s=t\,\hat{\boldsymbol{e}}_k$ ist dieser Bruch für jedes $t>0$ derselbe Vektor $(A-A')\hat{\boldsymbol{e}}_k$, also ist er null. Damit stimmen alle Spalten überein, und $A=A'$. Unter allen Matrizen gibt es also höchstens eine, deren Näherung im Kleinen besser wird als jede andere. Deshalb heißt $D\boldsymbol f(\boldsymbol{x}_0)$ die beste lineare Näherung.
:::

:::hintergrund Die Abbildung unter der Lupe
Was die Jacobi-Matrix beschreibt, sieht man, wenn man in den Punkt $\boldsymbol{x}_0$ hineinzoomt. Man nimmt einen festen Schritt $\boldsymbol s$, verkleinert ihn auf $\eta\,\boldsymbol s$ mit einer kleinen Zahl $\eta>0$ und vergrößert die Änderung, die er bewirkt, wieder um den Faktor $1/\eta$. Aus [(1.6)](#gl-1-6) folgt

$$\frac{\boldsymbol f(\boldsymbol{x}_0+\eta\,\boldsymbol s)-\boldsymbol f(\boldsymbol{x}_0)}{\eta}\;\longrightarrow\;D\boldsymbol f(\boldsymbol{x}_0)\,\boldsymbol s\qquad(\eta\to0).$$

Unter immer stärkerer Vergrößerung sieht die Abbildung also aus wie die Matrix $D\boldsymbol f(\boldsymbol{x}_0)$: Geraden werden zu Geraden, Quadrate zu Parallelogrammen, wie in Abb. [6](#abb-6). Das ist der Mechanismus hinter der Differentialrechnung in mehreren Variablen: Krumme Abbildungen werden im Kleinen durch Matrizen ersetzt, und mit Matrizen kann man rechnen. Dass die Einträge gerade die partiellen Ableitungen sind, liegt daran, dass eine Matrix durch ihre Spalten $A\hat{\boldsymbol{e}}_k$ festgelegt ist, und die misst man mit Schritten längs der Achsen, wie im Beweis von Satz [1.10](#satz-1-10).
:::

::::beispiel [Beispiel 1]
Für die Schale gilt um den Punkt $(1,1)$ exakt

$$\varphi(1+s_1,\,1+s_2)=3+2s_1+4s_2+s_1^2+2s_2^2 .$$

Mit $A=D\varphi(1,1)=(2\;\;4)$ ist der Fehler $s_1^2+2s_2^2\le2|\boldsymbol s|^2$. Der Bruch in [(1.6)](#gl-1-6) ist also höchstens $2|\boldsymbol s|$ und geht gegen null: Die Schale ist in $(1,1)$ differenzierbar.
::::

::::beispiel [Beispiel 2]
Für $\boldsymbol f(x,y)=(x^2-y^2,\,2xy)$ und den Schritt $\boldsymbol s=(\tfrac1{10},0)$ von $(1,\tfrac12)$ aus sagt [(1.7)](#gl-1-7) die Änderung

$$D\boldsymbol f(1,\tfrac12)\,\boldsymbol s=\begin{pmatrix}2&-1\\1&2\end{pmatrix}\begin{pmatrix}1/10\\0\end{pmatrix}=\begin{pmatrix}1/5\\1/10\end{pmatrix}$$

voraus. Das ist $\frac1{10}$ mal die erste Spalte. Exakt ist $\boldsymbol f(\tfrac{11}{10},\tfrac12)-\boldsymbol f(1,\tfrac12)=(\tfrac{21}{100},\,\tfrac1{10})$. Die Abweichung $\frac1{100}$ ist klein gegen die Schrittlänge $\frac1{10}$.
::::

⁠**Kurz gesagt:** Differenzierbar heißt: Nahe dem Punkt ist die Änderung bis auf einen Fehler, der schneller verschwindet als der Schritt, gleich Jacobi-Matrix mal Schritt.

### Die Tangentialebene

<span class="anker" id="stufe-1-18"></span>

Bei einer skalaren Funktion von zwei Variablen kann man die lineare Näherung zeichnen. Sie ist eine Ebene, an die sich der Graph anschmiegt, so wie sich der Graph einer Funktion einer Variablen an seine Tangente anschmiegt.

Für $m=1$ ist $Df(\boldsymbol{x}_0)\,\boldsymbol s=\nabla f(\boldsymbol{x}_0)\cdot\boldsymbol s$ (Unterabschnitt [1.15](#stufe-1-15)). Für eine differenzierbare skalare Funktion $f$ von zwei Variablen heißt die Ebene

$$z=f(\boldsymbol{x}_0)+\nabla f(\boldsymbol{x}_0)\cdot(\boldsymbol{x}-\boldsymbol{x}_0)$$

die __Tangentialebene__ an den Graphen von $f$ über dem Punkt $\boldsymbol{x}_0$. Nahe $\boldsymbol{x}_0$ unterscheidet sich der Graph von ihr um weniger als jedes feste Vielfache des Abstands $|\boldsymbol{x}-\boldsymbol{x}_0|$.

::::beispiel
Für die Schale ist $\varphi(1,1)=3$ und $\nabla\varphi(1,1)=(2,4)^T$. Die Tangentialebene über $(1,1)$ ist

$$z=3+2(x-1)+4(y-1)=2x+4y-3 .$$

Im Punkt $(1{,}1;\,1)$ liefert sie $3{,}2$, die Schale hat dort den Wert $3{,}21$.
::::

⁠**Kurz gesagt:** Die Tangentialebene ist die lineare Näherung einer Funktion von zwei Variablen, als Ebene über der Landkarte gezeichnet.

### Partielle Ableitungen allein reichen nicht

<span class="anker" id="stufe-1-19"></span>

Sobald alle partiellen Ableitungen existieren, kann man die Jacobi-Matrix aufschreiben. Ob sie die Abbildung auch bei Schritten in schräger Richtung beschreibt, verraten die partiellen Ableitungen aber nicht. Ein Beispiel zeigt, dass das schiefgehen kann.

Sei

$$f(x,y)=\frac{xy}{x^2+y^2}\quad\text{für }(x,y)\neq(0,0),\qquad f(0,0)=0 .$$

Auf beiden Achsen ist $f=0$. Deshalb existieren beide partiellen Ableitungen im Nullpunkt, und beide sind null. Als Matrix in [(1.6)](#gl-1-6) käme nach Satz [1.10](#satz-1-10) nur $A=(0\;\;0)$ in Frage. Auf der Diagonale ist aber $f(t,t)=\frac{t^2}{2t^2}=\frac12$ für jedes $t\neq0$, so nah man dem Nullpunkt auch kommt (Abb. [7](#abb-7)). Längs der Diagonale ist der Bruch in [(1.6)](#gl-1-6)

$$\frac{|f(t,t)-0-0|}{|(t,t)|}=\frac{1/2}{\sqrt2\,|t|}\longrightarrow\infty\qquad(t\to0).$$

Also ist $f$ im Nullpunkt nicht differenzierbar. Die Funktion ist dort nicht einmal stetig. Die partiellen Ableitungen bemerken das nicht, weil der Sprung neben den Achsen liegt.

:::abbildung hm3/k1schraeg 7
Links: $f=xy/(x^2+y^2)$ ist auf jedem Strahl durch den Nullpunkt konstant, die Zahlen sind die Werte auf den Strahlen. Rechts: Längs der Achse ist $f=0$, längs der Diagonale springt $f$ im Nullpunkt von $\frac12$ auf $0$.
:::

Die Umkehrung von Satz [1.10](#satz-1-10) ist also falsch: Aus der Existenz aller partiellen Ableitungen folgt im Allgemeinen nicht die Differenzierbarkeit.

⁠**Kurz gesagt:** Partielle Ableitungen sehen nur die Achsen. Eine Funktion kann alle partiellen Ableitungen haben und trotzdem nicht differenzierbar sein.

### Stetig differenzierbar

<span class="anker" id="stufe-1-20"></span>

Den Grenzwert [(1.6)](#gl-1-6) für jede Funktion auszurechnen, wäre mühsam. Eine Bedingung, die man den partiellen Ableitungen direkt ansieht, macht das in fast allen Fällen überflüssig.

Im Gegenbeispiel des letzten Unterabschnitts springen die Werte der Funktion nahe dem Nullpunkt, und mit ihnen ihre partiellen Ableitungen. Verändern sich die partiellen Ableitungen dagegen nur allmählich, gilt die Steigung, die man längs der Achsen misst, auch in allen Richtungen dazwischen.

:::satz Satz 1.11 (Hinreichende Bedingung)
<span class="anker" id="satz-1-11"></span>

Sei $\mathcal U\subset\mathbb{R}^n$ offen. Sind alle partiellen Ableitungen von $\boldsymbol f\colon\mathcal U\to\mathbb{R}^m$ auf $\mathcal U$ stetig, dann ist $\boldsymbol f$ auf $\mathcal U$ differenzierbar.
:::

Eine Abbildung, deren partielle Ableitungen alle existieren und stetig sind, heißt __stetig differenzierbar__.

:::hintergrund Warum stetige partielle Ableitungen genügen
Man geht von $\boldsymbol{x}_0$ nach $\boldsymbol{x}_0+\boldsymbol s$ nicht schräg, sondern in $n$ Teilschritten parallel zu den Achsen: zuerst um $s_1$ in Richtung $x_1$, dann um $s_2$ in Richtung $x_2$ und so weiter. Auf jedem Teilschritt ändert sich nur eine Variable, jede Komponentenfunktion ist dort eine Funktion einer Variablen. Für sie gilt der Mittelwertsatz: Die Änderung ist die Ableitung an einer Zwischenstelle mal die Länge des Teilschritts. Hier ist das die partielle Ableitung an einem Zwischenpunkt mal $s_k$. Weil die partiellen Ableitungen stetig sind, unterscheiden sie sich an den Zwischenpunkten nur wenig von ihren Werten in $\boldsymbol{x}_0$, und dieser Unterschied geht mit $\boldsymbol s\to0$ gegen null. Summiert man die Teilschritte, ist die Änderung also $D\boldsymbol f(\boldsymbol{x}_0)\,\boldsymbol s$ plus ein Fehler, der schneller verschwindet als $|\boldsymbol s|$. Die Stetigkeit verbindet so die Achsenrichtungen mit allen übrigen Richtungen.
:::

::::beispiel
Die Komponentenfunktionen von $\boldsymbol f(x,y)=(x^2-y^2,\,2xy)$ sind Polynome. Ihre partiellen Ableitungen $2x$, $-2y$, $2y$, $2x$ sind wieder Polynome und damit stetig. Also ist $\boldsymbol f$ auf ganz $\mathbb{R}^2$ stetig differenzierbar und damit differenzierbar. Dasselbe gilt für jede Abbildung, die aus Polynomen, $\mathrm{e}$-Funktion, Sinus, Kosinus und ähnlichen Bausteinen zusammengesetzt ist, überall dort, wo kein Nenner null wird.
::::

Damit gilt die Kette

$$\text{stetig differenzierbar}\;\Longrightarrow\;\text{differenzierbar}\;\Longrightarrow\;\text{alle partiellen Ableitungen existieren}.$$

Der zweite Pfeil lässt sich nach Unterabschnitt [1.19](#stufe-1-19) nicht umkehren. Auch der erste lässt sich nicht umkehren: Es gibt differenzierbare Funktionen, deren partielle Ableitungen nicht stetig sind.

:::hintergrund Eine differenzierbare Funktion mit unstetiger Ableitung
Schon in einer Variablen gibt es das. Sei $f(x)=x^2\sin(1/x)$ für $x\neq0$ und $f(0)=0$. Im Nullpunkt ist der Differenzenquotient $\frac{f(t)-f(0)}{t}=t\sin(1/t)$, und wegen $|\sin|\le1$ geht er gegen $0$. Also ist $f'(0)=0$. Für $x\neq0$ ist $f'(x)=2x\sin(1/x)-\cos(1/x)$. Der erste Summand geht für $x\to0$ gegen null, der zweite schwankt beliebig nahe am Nullpunkt zwischen $-1$ und $1$. Die Ableitung existiert also überall, ist aber im Nullpunkt nicht stetig. Die Funktion schwingt nahe dem Nullpunkt immer schneller, aber mit immer kleinerem Ausschlag.
:::

:::hintergrund Muss man immer den Grenzwert der Definition ausrechnen?
Nein. Besteht eine Abbildung aus Polynomen, $\mathrm{e}$-Funktion, Sinus und ähnlichen Bausteinen, sind ihre partiellen Ableitungen stetig, und Satz [1.11](#satz-1-11) erledigt alles. Den Grenzwert [(1.6)](#gl-1-6) braucht man nur an Sonderstellen: dort, wo die Abbildung stückweise erklärt ist, wo ein Nenner null wird oder wo eine Wurzel oder ein Betrag nicht ableitbar ist.
:::

⁠**Kurz gesagt:** Stetige partielle Ableitungen garantieren die Differenzierbarkeit. Dann ist die Jacobi-Matrix wirklich die Ableitung.

### Mehrfach stetig differenzierbar

<span class="anker" id="stufe-1-21"></span>

Oft braucht man nicht nur stetige erste, sondern auch stetige zweite oder höhere partielle Ableitungen. Dafür gibt es eine kurze Schreibweise.

:::definition Definition 1.12 ($k$-mal stetig differenzierbar)
<span class="anker" id="satz-1-12"></span>

Sei $\mathcal U\subset\mathbb{R}^n$ offen und $k$ eine natürliche Zahl. Eine Abbildung $\boldsymbol f\colon\mathcal U\to\mathbb{R}^m$ heißt __$k$-mal stetig differenzierbar__, wenn alle ihre partiellen Ableitungen der Ordnung kleiner oder gleich $k$ existieren und stetig sind. Die Menge dieser Abbildungen heißt $C^k(\mathcal U;\mathbb{R}^m)$, bei skalaren Funktionen kurz $C^k(\mathcal U)$.
:::

⁠**So liest man das:** „Kleiner oder gleich $k$“ schließt die Ordnung $0$ ein, also die Abbildung selbst. Gemeint sind alle Ableitungen von der Ordnung $0$ bis einschließlich $k$, nicht nur die der Ordnung $k$. $C^1$ ist dasselbe wie stetig differenzierbar. Man schreibt kurz $\boldsymbol f\in C^k$.

::::beispiel
Die Schale $\varphi=x^2+2y^2$ ist ein Polynom. Alle ihre partiellen Ableitungen jeder Ordnung sind Polynome, also ist $\varphi\in C^k$ für jedes $k$. Die Funktion $f(x,y)=x|x|$ ist in $C^1$, aber nicht in $C^2$: Es ist $\partial f/\partial x=2|x|$ und $\partial f/\partial y=0$, beides stetig. Die zweite Ableitung $\partial^2f/\partial x^2$ ist $2$ für $x>0$ und $-2$ für $x<0$ und existiert auf der $y$-Achse nicht.
::::

⁠**Kurz gesagt:** $C^k$ heißt: alle partiellen Ableitungen bis zur Ordnung $k$ existieren und sind stetig.

### Das Lemma von Schwarz

<span class="anker" id="stufe-1-22"></span>

Im Beispiel zu den höheren partiellen Ableitungen stimmten die beiden gemischten Ableitungen überein. Das ist kein Zufall, sondern gilt immer, wenn die Ableitungen stetig sind.

:::satz Satz 1.13 (Lemma von Schwarz)
<span class="anker" id="satz-1-13"></span>

Sei $k\ge2$ und $\boldsymbol f\in C^k(\mathcal U;\mathbb{R}^m)$. Dann darf man bei allen partiellen Ableitungen der Ordnung kleiner oder gleich $k$ die Reihenfolge der Ableitungen beliebig vertauschen. Insbesondere gilt für jede skalare Funktion $f\in C^2(\mathcal U)$

$$\frac{\partial^2f}{\partial x_j\,\partial x_k}=\frac{\partial^2f}{\partial x_k\,\partial x_j}\qquad\text{für alle }j,k .$$
:::

::::beispiel
Für $f(x,y)=x^2y^3$ ergaben beide Reihenfolgen $6xy^2$ (Unterabschnitt [1.8](#stufe-1-8)). Das Polynom ist in $C^2$, also musste es so sein.
::::

::::beispiel [Gegenbeispiel]
Ohne Stetigkeit kann die Reihenfolge eine Rolle spielen. Sei $f(x,y)=\dfrac{xy(x^2-y^2)}{x^2+y^2}$ für $(x,y)\neq(0,0)$ und $f(0,0)=0$. Aus der Definition [(1.1)](#gl-1-1) folgt $\frac{\partial f}{\partial x}(0,y)=-y$ und $\frac{\partial f}{\partial y}(x,0)=x$. Damit ist

$$\frac{\partial^2f}{\partial y\,\partial x}(0,0)=\frac{\mathrm{d}}{\mathrm{d} y}(-y)=-1,\qquad\frac{\partial^2f}{\partial x\,\partial y}(0,0)=\frac{\mathrm{d}}{\mathrm{d} x}\,x=1 .$$

Die gemischten Ableitungen dieser Funktion sind im Nullpunkt nicht stetig, deshalb greift der Satz nicht.
::::

:::hintergrund Warum man die Reihenfolge vertauschen darf
Beide gemischten Ableitungen im Punkt $(x,y)$ entstehen aus derselben Zahl, dem doppelten Differenzenquotienten

$$\frac{f(x+a,y+b)-f(x+a,y)-f(x,y+b)+f(x,y)}{a\,b}$$

mit kleinen Schritten $a$ und $b$. Lässt man zuerst $a\to0$ gehen und dann $b\to0$, erhält man die eine gemischte Ableitung, in der anderen Reihenfolge die andere. Sind die zweiten Ableitungen stetig, liefert der Mittelwertsatz, angewendet in jeder der beiden Variablen, für den Bruch den Wert einer gemischten Ableitung an einem Zwischenpunkt im Rechteck mit den Seiten $a$ und $b$. Mit $a,b\to0$ rückt dieser Punkt nach $(x,y)$, und wegen der Stetigkeit kommt in beiden Reihenfolgen dasselbe heraus.
:::

⁠**Kurz gesagt:** Bei Funktionen mit stetigen zweiten Ableitungen ist es egal, in welcher Reihenfolge man ableitet.

### Gradientenfelder und Skalarpotentiale

<span class="anker" id="stufe-1-23"></span>

Manche Vektorfelder sind der Gradient einer skalaren Funktion. Dann steckt die ganze Information der $n$ Komponenten in einer einzigen Funktion, und man muss nur diese kennen.

Man kann sich ein Gelände vorstellen, dessen Höhe die Funktion ist. Das Feld besteht dann an jedem Punkt aus dem Pfeil, den man in Abb. [5](#abb-5) aus den Steigungen zusammengesetzt hat.

:::definition Definition 1.14 (Gradientenfeld und Skalarpotential)
<span class="anker" id="satz-1-14"></span>

Sei $\mathcal U\subset\mathbb{R}^n$ offen und $\boldsymbol{E}\colon\mathcal U\to\mathbb{R}^n$ ein Vektorfeld. Gibt es eine differenzierbare Funktion $\varphi\colon\mathcal U\to\mathbb{R}$ mit

$$\boldsymbol{E}=\nabla\varphi\quad\text{auf }\mathcal U,$$

dann heißt $\boldsymbol{E}$ ein __Gradientenfeld__ auf $\mathcal U$. Jede solche Funktion $\varphi$ heißt ein __Skalarpotential__ von $\boldsymbol{E}$.
:::

Man sagt „ein“ Skalarpotential, weil es nicht das einzige ist: Mit $\varphi$ hat auch $\varphi+1$ den Gradienten $\boldsymbol{E}$, denn die Ableitung einer Konstanten ist null.

::::beispiel [Beispiel 1]
Das Feld $\boldsymbol{E}(x,y)=(2x,\,4y)$ ist ein Gradientenfeld auf $\mathbb{R}^2$. Ein Skalarpotential ist die Schale $\varphi=x^2+2y^2$, denn $\nabla\varphi=(2x,4y)^T$.
::::

::::beispiel [Beispiel 2]
Das Strahlfeld $\boldsymbol{E}(\boldsymbol{x})=\boldsymbol{x}$ ist ein Gradientenfeld auf $\mathbb{R}^n$ mit dem Skalarpotential $\varphi(\boldsymbol{x})=\frac12|\boldsymbol{x}|^2=\frac12(x_1^2+\dots+x_n^2)$. Denn $\partial\varphi/\partial x_j=x_j$, also $\nabla\varphi=\boldsymbol{x}$.
::::

⁠**Kurz gesagt:** Ein Gradientenfeld ist der Gradient einer skalaren Funktion, seines Skalarpotentials.

### Die Jacobi-Matrix eines Gradientenfelds ist symmetrisch

<span class="anker" id="stufe-1-24"></span>

Wie erkennt man an einem Feld, dass es kein Gradientenfeld ist, ohne vergeblich nach einem Skalarpotential zu suchen? Die Jacobi-Matrix verrät es.

Bei einem Gradientenfeld $\boldsymbol{E}=\nabla\varphi$ sind die Komponenten erste partielle Ableitungen von $\varphi$. Die Einträge der Jacobi-Matrix $D\boldsymbol{E}$ sind deshalb zweite partielle Ableitungen von $\varphi$. Nach dem Lemma von Schwarz kommt es dabei nicht auf die Reihenfolge an, und das spiegelt die Matrix an ihrer Diagonalen.

:::satz Satz 1.15 (Symmetrie der Jacobi-Matrix)
<span class="anker" id="satz-1-15"></span>

Ist $\boldsymbol{E}=\nabla\varphi$ ein Gradientenfeld mit einem zweimal stetig differenzierbaren Skalarpotential $\varphi$, dann ist die Jacobi-Matrix $D\boldsymbol{E}$ symmetrisch: $D\boldsymbol{E}=(D\boldsymbol{E})^T$.
:::

:::beweis Symmetrie
Die Komponente $j$ von $\boldsymbol{E}$ ist $E_j=\partial\varphi/\partial x_j$. Mit dem Lemma von Schwarz folgt

$$(D\boldsymbol{E})_{jk}=\frac{\partial E_j}{\partial x_k}=\frac{\partial}{\partial x_k}\Bigl(\frac{\partial\varphi}{\partial x_j}\Bigr)=\frac{\partial^2\varphi}{\partial x_k\,\partial x_j}=\frac{\partial^2\varphi}{\partial x_j\,\partial x_k}=\frac{\partial E_k}{\partial x_j}=(D\boldsymbol{E})_{kj}.$$
:::

Ist das Feld $\boldsymbol{E}$ selbst stetig differenzierbar, ist die Voraussetzung an $\varphi$ immer erfüllt: Die ersten partiellen Ableitungen von $\varphi$ sind die Komponenten von $\boldsymbol{E}$, ihre partiellen Ableitungen also die von $\boldsymbol{E}$, und die sind stetig. Für ein stetig differenzierbares Feld heißt das: Ist $D\boldsymbol{E}$ an einem Punkt nicht symmetrisch, dann hat $\boldsymbol{E}$ kein Skalarpotential. Ob umgekehrt jedes Feld mit symmetrischer Jacobi-Matrix ein Skalarpotential hat, sagt der Satz nicht.

::::beispiel [Beispiel 1]
Für $\boldsymbol{E}=(2x,4y)$ ist $D\boldsymbol{E}=\bigl(\begin{smallmatrix}2&0\\0&4\end{smallmatrix}\bigr)$ symmetrisch, passend zum Skalarpotential $x^2+2y^2$.
::::

::::beispiel [Beispiel 2]
Das Drehfeld $(-y,x)$ ist stetig differenzierbar und hat $D\boldsymbol{E}=\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)$. Rechts oben steht $-1$, links unten $1$. Die Matrix ist nicht symmetrisch, also ist das Drehfeld kein Gradientenfeld.
::::

⁠**Kurz gesagt:** Gradientenfelder haben eine symmetrische Jacobi-Matrix, weil man zweite Ableitungen vertauschen darf. Ein Feld mit unsymmetrischer Jacobi-Matrix hat kein Skalarpotential.

### Die Kettenregel

<span class="anker" id="stufe-1-25"></span>

Oft setzt man eine Abbildung in eine andere ein. Ein Beispiel: Die Temperatur hängt vom Ort ab, und der Ort eines Messfühlers hängt von seiner Einstellung ab. Wie hängt die Ableitung des Ergebnisses von den Ableitungen der beiden Teile ab?

Sei $\boldsymbol{g}=(g_1,\dots,g_m)$ eine Abbildung der Variablen $\boldsymbol{x}=(x_1,\dots,x_n)$ und $f$ eine skalare Funktion der Variablen $\boldsymbol{y}=(y_1,\dots,y_m)$. Die Abbildung $\boldsymbol{x}\mapsto f(\boldsymbol{g}(\boldsymbol{x}))$ heißt die __Verkettung__ von $f$ und $\boldsymbol{g}$ und wird $f\circ\boldsymbol{g}$ geschrieben. Sie ist erklärt, wenn jeder Wert $\boldsymbol{g}(\boldsymbol{x})$ dort liegt, wo $f$ erklärt ist.

Ändert man $x_k$ ein wenig, ändern sich alle Zwischengrößen $y_j=g_j(\boldsymbol{x})$, jede ungefähr um $\partial g_j/\partial x_k$ mal den Schritt. Jede Zwischengröße wirkt ihrerseits mit dem Faktor $\partial f/\partial y_j$ auf $f$. Die Wirkungen addieren sich über alle Wege $x_k\to y_j\to f$ (Abb. [8](#abb-8)).

:::abbildung hm3/k1kette 8
Die Wege, auf denen eine Änderung von $x_k$ die Verkettung $f\circ\boldsymbol{g}$ erreicht. Blau: wie stark sich jede Zwischengröße $y_j=g_j(\boldsymbol{x})$ ändert. Rot: wie stark $f$ auf $y_j$ reagiert. Jeder Weg trägt das Produkt seiner beiden Faktoren bei, die Kettenregel summiert über alle Wege.
:::

:::satz Satz 1.16 (Kettenregel)
<span class="anker" id="satz-1-16"></span>

Sei $f=f(y_1,\dots,y_m)$ eine differenzierbare Funktion und $\boldsymbol{g}=(g_1,\dots,g_m)$ eine differenzierbare Abbildung in $\boldsymbol{x}=(x_1,\dots,x_n)$. Dann ist die Verkettung $(f\circ\boldsymbol{g})(\boldsymbol{x})=f(\boldsymbol{g}(\boldsymbol{x}))$, falls sie erklärt ist, eine differenzierbare Funktion von $\boldsymbol{x}$ mit

<span class="anker" id="gl-1-8"></span>
$$\frac{\partial(f\circ\boldsymbol{g})}{\partial x_k}(\boldsymbol{x})=\sum_{j=1}^m\frac{\partial f}{\partial y_j}\bigl(\boldsymbol{g}(\boldsymbol{x})\bigr)\,\frac{\partial g_j}{\partial x_k}(\boldsymbol{x}),\qquad k=1,\dots,n. \tag{1.8}$$

Für Abbildungen $\boldsymbol f=(f_1,\dots,f_N)$ gilt entsprechend

$$\frac{\partial(\boldsymbol f\circ\boldsymbol{g})_i}{\partial x_k}(\boldsymbol{x})=\sum_{j=1}^m\frac{\partial f_i}{\partial y_j}\bigl(\boldsymbol{g}(\boldsymbol{x})\bigr)\,\frac{\partial g_j}{\partial x_k}(\boldsymbol{x}),$$

geschrieben als Matrixprodukt

<span class="anker" id="gl-1-9"></span>
$$D(\boldsymbol f\circ\boldsymbol{g})(\boldsymbol{x})=D\boldsymbol f\bigl(\boldsymbol{g}(\boldsymbol{x})\bigr)\,D\boldsymbol{g}(\boldsymbol{x}). \tag{1.9}$$
:::

⁠**So liest man das:** Die Summe in [(1.8)](#gl-1-8) läuft über alle Wege $x_k\to y_j\to f$ aus Abb. [8](#abb-8). Sie ist genau Zeile mal Spalte: Zeile $i$ von $D\boldsymbol f$ mal Spalte $k$ von $D\boldsymbol{g}$. Die Formate passen zusammen: $N\times m$ mal $m\times n$ ergibt $N\times n$. Wichtig: Die äußere Jacobi-Matrix $D\boldsymbol f$ wird an der Stelle $\boldsymbol{g}(\boldsymbol{x})$ ausgewertet, nicht an der Stelle $\boldsymbol{x}$.

:::herleitung Fehler durch Fehler
Setze $\boldsymbol{y}=\boldsymbol{g}(\boldsymbol{x})$. Nach [(1.6)](#gl-1-6) gilt für einen Schritt $\boldsymbol s$ im $\mathbb{R}^n$ und einen Schritt $\boldsymbol w$ im $\mathbb{R}^m$

$$\boldsymbol{g}(\boldsymbol{x}+\boldsymbol s)-\boldsymbol{y}=D\boldsymbol{g}(\boldsymbol{x})\,\boldsymbol s+\boldsymbol r_1,\qquad\boldsymbol f(\boldsymbol{y}+\boldsymbol w)-\boldsymbol f(\boldsymbol{y})=D\boldsymbol f(\boldsymbol{y})\,\boldsymbol w+\boldsymbol r_2 .$$

Dabei verschwinden die Fehler $\boldsymbol r_1$ und $\boldsymbol r_2$ schneller als $|\boldsymbol s|$ beziehungsweise $|\boldsymbol w|$. Setzt man $\boldsymbol w=\boldsymbol{g}(\boldsymbol{x}+\boldsymbol s)-\boldsymbol{y}$ ein, folgt

$$\boldsymbol f\bigl(\boldsymbol{g}(\boldsymbol{x}+\boldsymbol s)\bigr)-\boldsymbol f(\boldsymbol{y})=D\boldsymbol f(\boldsymbol{y})\,D\boldsymbol{g}(\boldsymbol{x})\,\boldsymbol s+D\boldsymbol f(\boldsymbol{y})\,\boldsymbol r_1+\boldsymbol r_2 .$$

Beide Fehlerterme verschwinden schneller als $|\boldsymbol s|$, weil $|\boldsymbol w|$ für kleine $\boldsymbol s$ höchstens ein festes Vielfaches von $|\boldsymbol s|$ ist. Also ist $\boldsymbol f\circ\boldsymbol{g}$ in $\boldsymbol{x}$ differenzierbar, und nach Satz [1.10](#satz-1-10) ist die Matrix vor $\boldsymbol s$ ihre Jacobi-Matrix.
:::

::::beispiel
Sei $f(y_1,y_2)=y_1^2+y_2$ und $\boldsymbol{g}(x_1,x_2)=(x_1x_2,\;x_1+x_2)$, betrachtet im Punkt $\boldsymbol{x}=(1,2)$. Dort ist $\boldsymbol{g}(1,2)=(2,3)$. Die beiden Jacobi-Matrizen sind

$$Df(\boldsymbol{y})=(2y_1\;\;\;1),\quad Df(2,3)=(4\;\;\;1),\qquad D\boldsymbol{g}(\boldsymbol{x})=\begin{pmatrix}x_2&x_1\\1&1\end{pmatrix},\quad D\boldsymbol{g}(1,2)=\begin{pmatrix}2&1\\1&1\end{pmatrix}.$$

Nach [(1.9)](#gl-1-9) ist $D(f\circ\boldsymbol{g})(1,2)=(4\;\;1)\bigl(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\bigr)=(9\;\;5)$. Zur Kontrolle direkt: $(f\circ\boldsymbol{g})(\boldsymbol{x})=x_1^2x_2^2+x_1+x_2$ hat die partiellen Ableitungen $2x_1x_2^2+1$ und $2x_1^2x_2+1$, im Punkt $(1,2)$ also $9$ und $5$.
::::

⁠**Grenzfall:** Für $n=m=N=1$ steht dort die bekannte Kettenregel $(f\circ g)'(x)=f'(g(x))\,g'(x)$.

:::hintergrund Warum die Ableitung einer Verkettung ein Matrixprodukt ist
Im Kleinen wirkt jede differenzierbare Abbildung wie ihre Jacobi-Matrix (Hintergrund „Die Abbildung unter der Lupe“). Ein kleiner Schritt $\boldsymbol s$ am Eingang wird von $\boldsymbol{g}$ zu ungefähr $D\boldsymbol{g}(\boldsymbol{x})\,\boldsymbol s$. Dieser Schritt kommt bei $\boldsymbol f$ an der Stelle $\boldsymbol{g}(\boldsymbol{x})$ an und wird dort zu ungefähr $D\boldsymbol f(\boldsymbol{g}(\boldsymbol{x}))\bigl(D\boldsymbol{g}(\boldsymbol{x})\,\boldsymbol s\bigr)$. Zwei Matrizen nacheinander wirken wie ihr Produkt (Unterabschnitt [1.3](#stufe-1-3)). Die Kettenregel sagt also nur: Die beste lineare Näherung einer Verkettung ist die Verkettung der besten linearen Näherungen. Die Herleitung zeigt, dass die Fehler dabei schneller verschwinden als der Schritt. Deshalb muss die äußere Matrix am Bildpunkt $\boldsymbol{g}(\boldsymbol{x})$ genommen werden: Dort kommt der Schritt an.
:::

⁠**Kurz gesagt:** Die Jacobi-Matrix einer Verkettung ist das Produkt der Jacobi-Matrizen, die äußere ausgewertet am Bildpunkt.

### Kurven

<span class="anker" id="stufe-1-26"></span>

Ein Teilchen, das sich durch den Raum bewegt, ist zu jeder Zeit $t$ an einem Punkt. Das beschreibt eine Abbildung mit einem einzigen Eingang, der Zeit, und $n$ Ausgängen, den Koordinaten.

:::abbildung hm3/k1kurve 9
Die Kurve $\gamma(t)=(\cos t,\sin t)$ läuft gegen den Uhrzeigersinn auf dem Kreis mit Radius $1$. Im Punkt $\gamma(\pi/4)$ ist der Tangentenvektor $\dot\gamma(\pi/4)=\bigl(-\tfrac1{\sqrt2},\tfrac1{\sqrt2}\bigr)$ eingezeichnet. Er berührt den Kreis und zeigt in die Richtung, in die die Kurve läuft.
:::

:::definition Definition 1.17 (Kurve und Tangentenvektor)
<span class="anker" id="satz-1-17"></span>

Sei $I\subset\mathbb{R}$ ein Intervall. Eine Abbildung $\gamma\colon I\to\mathbb{R}^n$, $t\mapsto\gamma(t)=\bigl(\gamma_1(t),\dots,\gamma_n(t)\bigr)$, heißt __Kurve__. Sie heißt differenzierbar, wenn alle Komponentenfunktionen $\gamma_j$ differenzierbar sind. Dann heißt

$$\dot\gamma(t)=\bigl(\dot\gamma_1(t),\dots,\dot\gamma_n(t)\bigr)$$

der __Tangentenvektor__ von $\gamma$ an der Stelle $t$. Der Punkt über einem Zeichen bezeichnet die Ableitung nach $t$.
:::

Der Tangentenvektor ist die Jacobi-Matrix von $\gamma$, eine Spalte mit $n$ Einträgen. Nach [(1.7)](#gl-1-7) ist $\gamma(t+\tau)\approx\gamma(t)+\tau\,\dot\gamma(t)$ für kleine Zahlen $\tau$. Er zeigt also in die Richtung, in die die Kurve läuft, und seine Länge gibt an, wie schnell sie durchlaufen wird. Beschreibt $\gamma(t)$ den Ort eines Teilchens zur Zeit $t$, ist $\dot\gamma(t)$ seine Geschwindigkeit.

::::beispiel
$\gamma(t)=(\cos t,\,\sin t)$ für $t\in[0,2\pi]$ läuft einmal gegen den Uhrzeigersinn um den Kreis mit Radius $1$ (Abb. [9](#abb-9)). Der Tangentenvektor ist $\dot\gamma(t)=(-\sin t,\,\cos t)$ und hat immer die Länge $1$. Bei $t=\pi/4$ ist $\gamma=(\tfrac1{\sqrt2},\tfrac1{\sqrt2})$ und $\dot\gamma=(-\tfrac1{\sqrt2},\tfrac1{\sqrt2})$. Das Skalarprodukt der beiden ist $-\tfrac12+\tfrac12=0$: Der Tangentenvektor steht senkrecht auf dem Pfeil vom Mittelpunkt zum Kurvenpunkt.
::::

⁠**Kurz gesagt:** Eine Kurve ist eine Abbildung von einem Intervall in den $\mathbb{R}^n$. Ihr Tangentenvektor ist die Ableitung jeder Komponente nach $t$ und zeigt in Laufrichtung.

### Die Ableitung längs einer Kurve

<span class="anker" id="stufe-1-27"></span>

Ein Teilchen läuft durch einen Raum, in dem die Temperatur von Ort zu Ort verschieden ist. Wie schnell ändert sich die Temperatur, die es auf seinem Weg misst? Das ist die Kettenregel für den Fall, dass die innere Abbildung eine Kurve ist.

:::satz Satz 1.18 (Ableitung längs einer Kurve)
<span class="anker" id="satz-1-18"></span>

Sei $\mathcal U\subset\mathbb{R}^n$ offen, $h\colon\mathcal U\to\mathbb{R}$ differenzierbar und $\gamma\colon I\to\mathcal U$ eine differenzierbare Kurve. Dann gilt

<span class="anker" id="gl-1-10"></span>
$$\frac{\mathrm{d}}{\mathrm{d} t}\,h\bigl(\gamma(t)\bigr)=\nabla h\bigl(\gamma(t)\bigr)\cdot\dot\gamma(t). \tag{1.10}$$
:::

:::beweis Kettenregel mit einem Eingang
Setze in Satz [1.16](#satz-1-16) $f=h$ und $\boldsymbol{g}=\gamma$. Die innere Abbildung hat nur den Eingang $t$, ihre Jacobi-Matrix ist die Spalte $\dot\gamma(t)$. Die äußere Jacobi-Matrix $Dh(\gamma(t))$ ist eine Zeile. Zeile mal Spalte ist das Skalarprodukt:

$$\frac{\mathrm{d}}{\mathrm{d} t}\,h\bigl(\gamma(t)\bigr)=Dh\bigl(\gamma(t)\bigr)\,\dot\gamma(t)=\sum_{j=1}^n\frac{\partial h}{\partial x_j}\bigl(\gamma(t)\bigr)\,\dot\gamma_j(t)=\nabla h\bigl(\gamma(t)\bigr)\cdot\dot\gamma(t).$$
:::

::::beispiel
Die Schale $\varphi=x^2+2y^2$ längs des Kreises $\gamma(t)=(\cos t,\sin t)$. Es ist $\nabla\varphi(\gamma(t))=(2\cos t,\;4\sin t)$ und $\dot\gamma(t)=(-\sin t,\;\cos t)$, also

$$\frac{\mathrm{d}}{\mathrm{d} t}\,\varphi\bigl(\gamma(t)\bigr)=-2\cos t\sin t+4\sin t\cos t=2\sin t\cos t .$$

Zur Kontrolle direkt: $\varphi(\gamma(t))=\cos^2t+2\sin^2t=1+\sin^2t$ hat die Ableitung $2\sin t\cos t$.
::::

⁠**Grenzfall:** Für $n=1$ und $\gamma(t)=t$ steht dort $\frac{\mathrm{d}}{\mathrm{d} t}h(t)=h'(t)$.

:::hintergrund Warum $h$ differenzierbar sein muss und nicht nur partiell differenzierbar
Die Formel benutzt die Kettenregel, und die braucht die Differenzierbarkeit. Ein Beispiel zeigt, dass partielle Ableitungen nicht reichen. Sei $w(x,y)=\dfrac{x^2y}{x^2+y^2}$ für $(x,y)\neq(0,0)$ und $w(0,0)=0$. Auf beiden Achsen ist $w=0$, also sind beide partiellen Ableitungen im Nullpunkt null und $\nabla w(0,0)=(0,0)^T$. Längs der Kurve $\gamma(t)=(t,t)$ ist aber $w(\gamma(t))=\frac{t^3}{2t^2}=\frac t2$, mit der Ableitung $\frac12$ bei $t=0$. Die rechte Seite von [(1.10)](#gl-1-10) wäre dort $\nabla w(0,0)\cdot(1,1)=0$. Die Formel gilt hier nicht, weil $w$ im Nullpunkt nicht differenzierbar ist.
:::

⁠**Kurz gesagt:** Die Änderung einer Funktion längs einer Kurve ist das Skalarprodukt aus Gradient und Tangentenvektor.

### Die Richtungsableitung

<span class="anker" id="stufe-1-28"></span>

Wie steil ist ein Gelände, wenn man in eine Richtung losgeht, die keine Achsenrichtung ist? Die partiellen Ableitungen beantworten das nur für die Achsen.

Man geht vom Punkt $\boldsymbol{x}$ aus auf einer Geraden in die gewünschte Richtung und misst, wie schnell sich die Funktion dabei ändert. Damit die Antwort nur von der Richtung abhängt und nicht vom Tempo, nimmt man einen Richtungsvektor der Länge $1$.

:::definition Definition 1.19 (Richtungsableitung)
<span class="anker" id="satz-1-19"></span>

Sei $h$ differenzierbar und $\boldsymbol v\in\mathbb{R}^n$ ein Vektor der Länge $|\boldsymbol v|=1$. Die __Richtungsableitung__ von $h$ im Punkt $\boldsymbol{x}$ in Richtung $\boldsymbol v$ ist die Ableitung längs der Geraden $\gamma(t)=\boldsymbol{x}+t\,\boldsymbol v$ an der Stelle $t=0$.
:::

Die Gerade hat den Tangentenvektor $\dot\gamma=\boldsymbol v$. Nach [(1.10)](#gl-1-10) ist die Richtungsableitung deshalb

<span class="anker" id="gl-1-11"></span>
$$\frac{\mathrm{d}}{\mathrm{d} t}\,h(\boldsymbol{x}+t\,\boldsymbol v)\Big|_{t=0}=\nabla h(\boldsymbol{x})\cdot\boldsymbol v . \tag{1.11}$$

Für $\boldsymbol v=\hat{\boldsymbol{e}}_k$ ist das die partielle Ableitung nach $x_k$.

::::beispiel
Die Schale im Punkt $(1,1)$ in Richtung $\boldsymbol v=\frac15(3,4)$. Es ist $|\boldsymbol v|=\frac15\sqrt{9+16}=1$ und

$$\nabla\varphi(1,1)\cdot\boldsymbol v=(2,4)\cdot\tfrac15(3,4)=\tfrac15(6+16)=\tfrac{22}5=4{,}4 .$$
::::

⁠**Kurz gesagt:** Die Richtungsableitung ist die Steigung in einer beliebigen Richtung $\boldsymbol v$ der Länge $1$, und sie ist $\nabla h\cdot\boldsymbol v$.

### Wohin der Gradient zeigt

<span class="anker" id="stufe-1-29"></span>

In welche Richtung steigt eine Funktion am stärksten, und in welche Richtung bleibt sie gleich? Beides liest man am Gradienten ab.

Nach [(1.11)](#gl-1-11) und der geometrischen Form des Skalarprodukts ist die Richtungsableitung

$$\nabla h(\boldsymbol{x})\cdot\boldsymbol v=|\nabla h(\boldsymbol{x})|\,|\boldsymbol v|\cos\alpha=|\nabla h(\boldsymbol{x})|\cos\alpha ,$$

wobei $\alpha$ der Winkel zwischen $\nabla h(\boldsymbol{x})$ und $\boldsymbol v$ ist. Der Kosinus ist am größten, nämlich $1$, für $\alpha=0$.

:::satz Satz 1.20 (Richtung des steilsten Anstiegs)
<span class="anker" id="satz-1-20"></span>

Sei $h$ differenzierbar und $\nabla h(\boldsymbol{x})\neq0$.

<ol class="rm">

<li>

Die Richtungsableitung in $\boldsymbol{x}$ ist am größten in Richtung $\boldsymbol v=\nabla h(\boldsymbol{x})/|\nabla h(\boldsymbol{x})|$. Dort hat sie den Wert $|\nabla h(\boldsymbol{x})|$. Der Gradient zeigt also in die Richtung des steilsten Anstiegs, und seine Länge ist diese Steigung.

</li>

<li>

Der Gradient steht senkrecht auf den Höhenlinien: Ist $\gamma$ eine differenzierbare Kurve, auf der $h$ konstant ist, dann gilt $\nabla h(\gamma(t))\cdot\dot\gamma(t)=0$.

</li>

</ol>
:::

:::beweis Steilster Anstieg und Höhenlinien
(i) folgt aus der Rechnung davor, denn $\cos\alpha\le1$ mit Gleichheit genau für $\alpha=0$. (ii) Auf der Kurve ist $h(\gamma(t))=c$ für eine feste Zahl $c$. Die Ableitung nach $t$ ist null, und nach [(1.10)](#gl-1-10) ist sie $\nabla h(\gamma(t))\cdot\dot\gamma(t)$.
:::

:::abbildung hm3/k1gradient 10
Höhenlinien der Schale $\varphi=x^2+2y^2$ mit Gradientenpfeilen auf der Linie $\varphi=3$. Im Punkt $(1,1)$ ist $\nabla\varphi=(2,4)^T$, gezeichnet in verkleinertem Maßstab. Die grüne Kurve $\gamma$ schneidet die Höhenlinien, und [(1.10)](#gl-1-10) sagt, wie schnell $\varphi$ dabei wächst.
:::

::::beispiel
Für die Schale im Punkt $(1,1)$ ist $\nabla\varphi=(2,4)^T$ und $|\nabla\varphi|=\sqrt{20}=2\sqrt5\approx4{,}47$. Am steilsten steigt sie in Richtung $(2,4)/(2\sqrt5)=(1,2)/\sqrt5$, mit der Steigung $4{,}47$. Die Richtung $\frac15(3,4)$ aus dem letzten Unterabschnitt liefert nur $4{,}4$. Senkrecht zum Gradienten, in Richtung $\pm(-2,1)/\sqrt5$, ändert sich $\varphi$ in erster Näherung nicht: Das ist die Richtung der Höhenlinie durch $(1,1)$ (Abb. [10](#abb-10)).
::::

:::hintergrund Der Graph ist eine Fläche im Raum. Warum zeigt der Gradient dann in der Ebene?
Der Gradient von $h(x,y)$ hat zwei Komponenten. Er ist ein Vektor im Raum der Eingänge, also in der $x$-$y$-Ebene. Er gibt die Richtung an, in die man auf der Landkarte gehen muss, um am steilsten bergauf zu kommen. Er ist kein Pfeil, der auf dem Hang liegt. Deshalb steht er in der Karte senkrecht auf den Höhenlinien.
:::

⁠**Kurz gesagt:** Der Gradient zeigt in die Richtung des steilsten Anstiegs, seine Länge ist diese Steigung, und er steht senkrecht auf den Höhenlinien.

### Feldlinien

<span class="anker" id="stufe-1-30"></span>

Man möchte einem Vektorfeld folgen: an jedem Punkt genau in die Richtung weiterlaufen, in die der Pfeil dort zeigt. Ein Blatt, das auf einer Strömung treibt, tut genau das.

:::definition Definition 1.21 (Feldlinie)
<span class="anker" id="satz-1-21"></span>

Sei $\boldsymbol{E}$ ein Vektorfeld auf der offenen Menge $\mathcal U$. Eine differenzierbare Kurve $\gamma\colon I\to\mathcal U$ heißt __Feldlinie__ von $\boldsymbol{E}$, wenn ihr Tangentenvektor in jedem Punkt der Pfeil des Felds ist:

$$\dot\gamma(t)=\boldsymbol{E}\bigl(\gamma(t)\bigr)\qquad\text{für alle }t\in I .$$
:::

In Zeichnungen zeigt man meist nur die Bahn einer Feldlinie. Sie verläuft überall in Richtung der Pfeile.

::::beispiel [Beispiel 1]
Für das Drehfeld $\boldsymbol{E}(x,y)=(-y,x)$ ist der Kreis $\gamma(t)=(\cos t,\sin t)$ eine Feldlinie: $\dot\gamma(t)=(-\sin t,\cos t)$ und $\boldsymbol{E}(\gamma(t))=(-\sin t,\cos t)$ stimmen überein. Die Feldlinien des Drehfelds sind Kreise um den Nullpunkt (vergleiche Abb. [4](#abb-4)).
::::

::::beispiel [Beispiel 2]
Für das Strahlfeld $\boldsymbol{E}(\boldsymbol{x})=\boldsymbol{x}$ in der Ebene ist $\gamma(t)=(\mathrm{e}^t,0)$ eine Feldlinie, denn $\dot\gamma(t)=(\mathrm{e}^t,0)=\gamma(t)=\boldsymbol{E}(\gamma(t))$. Sie läuft auf der $x$-Achse vom Nullpunkt weg.
::::

⁠**Kurz gesagt:** Eine Feldlinie ist eine Kurve, die an jedem Punkt dem Pfeil des Felds folgt.

### Potentialfelder in der Physik

<span class="anker" id="stufe-1-31"></span>

In der Physik soll ein Teilchen, das dem Feld folgt, potentielle Energie verlieren, so wie ein Ball beim Bergabrollen Höhe verliert. Mit $\boldsymbol{E}=\nabla\varphi$ wäre es umgekehrt, denn der Gradient zeigt bergauf. Deshalb wählt man dort das andere Vorzeichen.

:::definition Definition 1.22 (Potential im Sinn der Physik)
<span class="anker" id="satz-1-22"></span>

Sei $\boldsymbol{E}$ ein Vektorfeld auf der offenen Menge $\mathcal U$. In der Physik heißt eine differenzierbare Funktion $u$ mit

$$\boldsymbol{E}=-\nabla u$$

ein __Potential__ von $\boldsymbol{E}$. Das Feld $\boldsymbol{E}=-\nabla u$ heißt dann das zugehörige __Potentialfeld__.
:::

Längs einer Feldlinie $\gamma$ nimmt das Potential ab, wo das Feld nicht null ist. Nach [(1.10)](#gl-1-10) und mit $\dot\gamma=\boldsymbol{E}(\gamma)$ ist

$$\frac{\mathrm{d}}{\mathrm{d} t}\,u\bigl(\gamma(t)\bigr)=\nabla u\bigl(\gamma(t)\bigr)\cdot\dot\gamma(t)=-\boldsymbol{E}\bigl(\gamma(t)\bigr)\cdot\dot\gamma(t)=-\bigl|\boldsymbol{E}\bigl(\gamma(t)\bigr)\bigr|^2<0 .$$

Für den Begriff Gradientenfeld spielt das Vorzeichen keine Rolle: Aus $\boldsymbol{E}=-\nabla u$ folgt $\boldsymbol{E}=\nabla(-u)$. Ein Potentialfeld ist also ein Gradientenfeld mit dem Skalarpotential $-u$.

::::beispiel
Sei $u(x,y,z)=-3x$ im ganzen Raum. Dann ist $\boldsymbol{E}=-\nabla u=(3,0,0)$, ein Feld, das überall gleich stark in $x$-Richtung zeigt. Die Kurve $\gamma(t)=(3t,0,0)$ ist eine Feldlinie, denn $\dot\gamma=(3,0,0)=\boldsymbol{E}$. Längs ihr ist $u(\gamma(t))=-9t$, das Potential fällt mit der Rate $9=|\boldsymbol{E}|^2$.
::::

⁠**Kurz gesagt:** In der Physik ist das Feld der negative Gradient des Potentials. Dann fällt das Potential längs jeder Feldlinie.

### Aufgaben

<span class="anker" id="stufe-1-32"></span>

:::aufgabe Aufgabe 1 ★ Jacobi-Matrix aufstellen
<span class="anker" id="aufg-1"></span>

Sei $\boldsymbol f(x,y,z)=(xy^2,\;x+\mathrm{e}^{z})$.

<ol class="al">

<li>

Welches Format hat $D\boldsymbol f$? Berechne $D\boldsymbol f(1,2,0)$ und den Gradienten der zweiten Komponentenfunktion.

</li>

<li>

Sage mit [(1.7)](#gl-1-7) die Änderung von $\boldsymbol f$ beim Schritt $\boldsymbol s=(\tfrac1{10},0,-\tfrac1{10})$ von $(1,2,0)$ aus voraus und vergleiche mit der exakten Änderung.

</li>

</ol>

:::loesung
(a) $\boldsymbol f$ hat zwei Ausgänge und drei Eingänge, also hat $D\boldsymbol f$ das Format $2\times3$. Zeile 1 enthält die Ableitungen von $f_1=xy^2$, Zeile 2 die von $f_2=x+\mathrm{e}^z$:

$$D\boldsymbol f=\begin{pmatrix}y^2&2xy&0\\1&0&\mathrm{e}^z\end{pmatrix},\qquad D\boldsymbol f(1,2,0)=\begin{pmatrix}4&4&0\\1&0&1\end{pmatrix},\qquad\nabla f_2=(1,\,0,\,\mathrm{e}^z)^T .$$

Der Gradient von $f_2$ ist die transponierte zweite Zeile.

(b) Vorhersage nach [(1.7)](#gl-1-7):

$$D\boldsymbol f(1,2,0)\,\boldsymbol s=\begin{pmatrix}4&4&0\\1&0&1\end{pmatrix}\begin{pmatrix}1/10\\0\\-1/10\end{pmatrix}=\begin{pmatrix}2/5\\0\end{pmatrix}.$$

Exakt ist $\boldsymbol f(\tfrac{11}{10},2,-\tfrac1{10})-\boldsymbol f(1,2,0)=\bigl(\tfrac{11}{10}\cdot4-4,\;\tfrac{11}{10}+\mathrm{e}^{-1/10}-2\bigr)=\bigl(\tfrac25,\;\tfrac1{10}+\mathrm{e}^{-1/10}-1\bigr)\approx(0{,}4;\;0{,}0048)$. Die erste Komponente stimmt exakt, weil $f_1$ in $x$ linear ist. Die zweite ist fast null, wie vorhergesagt; die Abweichung $0{,}0048$ ist klein gegen die Schrittlänge $|\boldsymbol s|\approx0{,}14$.
:::
:::

:::aufgabe Aufgabe 2 ★ Gradientenfeld oder nicht?
<span class="anker" id="aufg-2"></span>

<ol class="al">

<li>

Zeige, dass $\boldsymbol{E}(x,y)=(2xy,\;x^2+1)$ ein Gradientenfeld auf $\mathbb{R}^2$ ist, indem du nachrechnest, dass $\varphi(x,y)=x^2y+y$ ein Skalarpotential ist. Prüfe außerdem, dass $D\boldsymbol{E}$ symmetrisch ist.

</li>

<li>

Zeige mit Satz [1.15](#satz-1-15), dass $\boldsymbol{F}(x,y)=(y,\,-x)$ kein Gradientenfeld auf $\mathbb{R}^2$ ist. In welche Richtung laufen seine Pfeile um den Nullpunkt?

</li>

</ol>

:::loesung
(a) $\nabla\varphi=\bigl(\partial(x^2y+y)/\partial x,\;\partial(x^2y+y)/\partial y\bigr)^T=(2xy,\;x^2+1)^T=\boldsymbol{E}$. Also ist $\boldsymbol{E}$ ein Gradientenfeld mit dem Skalarpotential $\varphi$. Die Jacobi-Matrix

$$D\boldsymbol{E}=\begin{pmatrix}\partial E_1/\partial x&\partial E_1/\partial y\\\partial E_2/\partial x&\partial E_2/\partial y\end{pmatrix}=\begin{pmatrix}2y&2x\\2x&0\end{pmatrix}$$

ist symmetrisch, wie Satz [1.15](#satz-1-15) verlangt.

(b) $D\boldsymbol{F}=\bigl(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\bigr)$. Rechts oben steht $\partial F_1/\partial y=1$, links unten $\partial F_2/\partial x=-1$; die Matrix ist an keinem Punkt symmetrisch. $\boldsymbol{F}$ ist stetig differenzierbar, also wäre jedes Skalarpotential zweimal stetig differenzierbar, und Satz [1.15](#satz-1-15) schließt es aus. Im Punkt $(1,0)$ ist $\boldsymbol{F}=(0,-1)$, der Pfeil zeigt nach unten; im Punkt $(0,1)$ ist $\boldsymbol{F}=(1,0)$, er zeigt nach rechts. Die Pfeile laufen also im Uhrzeigersinn um den Nullpunkt, $\boldsymbol{F}$ ist das gespiegelte Drehfeld.
:::
:::

:::aufgabe Aufgabe 3 ★★ Differenzierbar nach Definition
<span class="anker" id="aufg-3"></span>

Sei $f(x,y)=5+3x-2y+|\boldsymbol{x}|^2\cos\bigl(1/|\boldsymbol{x}|^2\bigr)$ mit $|\boldsymbol{x}|^2=x^2+y^2$ für $(x,y)\neq(0,0)$ und $f(0,0)=5$.

<ol class="al">

<li>

Zeige mit [(1.6)](#gl-1-6), dass $f$ im Nullpunkt differenzierbar ist, und gib $A$ an.

</li>

<li>

Zeige, dass $\partial f/\partial x$ im Nullpunkt nicht stetig ist. Betrachte dazu die Punkte $(x,0)$ mit $x>0$ und $1/x^2=2\pi\mu+\frac\pi2$ für $\mu\in\mathbb{N}$. Warum hilft Satz [1.11](#satz-1-11) hier nicht?

</li>

</ol>

:::loesung
(a) Kandidat ist die lineare Näherung aus dem glatten Teil, $A=(3\;\;{-2})$. Dann ist $f(x,y)-5-(3x-2y)=|\boldsymbol{x}|^2\cos(1/|\boldsymbol{x}|^2)$ für $\boldsymbol{x}\neq0$. Wegen $|\cos|\le1$ ist der Bruch aus [(1.6)](#gl-1-6) höchstens $|\boldsymbol{x}|^2/|\boldsymbol{x}|=|\boldsymbol{x}|$ und geht gegen null. Also ist $f$ im Nullpunkt differenzierbar mit $A=(3\;\;{-2})$; insbesondere ist $\partial f/\partial x(0,0)=3$.

(b) Für $\boldsymbol{x}\neq0$ ist nach Ketten- und Produktregel

$$\frac{\partial f}{\partial x}=3+2x\cos\frac1{|\boldsymbol{x}|^2}+\frac{2x}{|\boldsymbol{x}|^2}\sin\frac1{|\boldsymbol{x}|^2}.$$

In den Punkten $(x,0)$ mit $x>0$ und $1/x^2=2\pi\mu+\frac\pi2$ ist $\cos(1/x^2)=0$ und $\sin(1/x^2)=1$, also $\partial f/\partial x=3+2/x$. Für $\mu\to\infty$ gehen diese Punkte gegen den Nullpunkt, aber $3+2/x$ wächst über alle Grenzen und strebt nicht gegen $\partial f/\partial x(0,0)=3$. Die partielle Ableitung ist im Nullpunkt also nicht stetig. Satz [1.11](#satz-1-11) gibt nur eine hinreichende Bedingung: Seine Voraussetzung fehlt hier, seine Aussage gilt trotzdem.
:::
:::

:::aufgabe Aufgabe 4 ★★ Stetig, aber nicht differenzierbar
<span class="anker" id="aufg-4"></span>

Sei $w(x,y)=x^2y/(x^2+y^2)$ für $(x,y)\neq(0,0)$ und $w(0,0)=0$, die Funktion aus dem Hintergrund-Kasten zu Satz [1.18](#satz-1-18). Zeige: $w$ ist im Nullpunkt stetig, beide partiellen Ableitungen existieren dort, aber $w$ ist dort nicht differenzierbar. Tipp: Welche Matrix käme als $A$ in Frage? Prüfe den Bruch aus [(1.6)](#gl-1-6) längs $(t,t)$.

:::loesung
⁠*Stetig:* Wegen $x^2\le x^2+y^2$ ist $|w(x,y)|\le|y|\le|\boldsymbol{x}|$, und das geht für $\boldsymbol{x}\to0$ gegen $0=w(0,0)$.

⁠*Partielle Ableitungen:* $w(x,0)=0$ und $w(0,y)=0$ für alle $x,y$. Die Differenzenquotienten [(1.1)](#gl-1-1) längs der Achsen sind also null, beide partiellen Ableitungen existieren und sind null.

⁠*Nicht differenzierbar:* Nach Satz [1.10](#satz-1-10) käme nur $A=(0\;\;0)$ in Frage. Längs $(t,t)$ mit $t>0$ ist $w(t,t)=t^3/(2t^2)=t/2$ und $|(t,t)|=\sqrt2\,t$. Der Bruch aus [(1.6)](#gl-1-6) ist $\frac{t/2}{\sqrt2\,t}=\frac1{2\sqrt2}\approx0{,}354$ für jedes $t$ und geht nicht gegen null.
:::
:::

:::aufgabe Aufgabe 5 ★ Richtung, Kurve, Ebene
<span class="anker" id="aufg-5"></span>

Sei $h(x,y)=x^2y-y^2$.

<ol class="al">

<li>

Berechne die Richtungsableitung in $(2,1)$ in Richtung $\boldsymbol v=\frac15(3,4)$. In welche Richtung steigt $h$ dort am stärksten, wie groß ist diese Steigung, und in welche Richtungen bleibt $h$ in erster Näherung gleich?

</li>

<li>

Berechne $\frac{\mathrm{d}}{\mathrm{d} t}h(\gamma(t))$ für $\gamma(t)=(t^2,t)$ mit [(1.10)](#gl-1-10) und zur Kontrolle durch Einsetzen.

</li>

<li>

Gib die Tangentialebene an den Graphen von $h$ über dem Punkt $(2,1)$ an.

</li>

</ol>

:::loesung
(a) $\nabla h=(2xy,\;x^2-2y)^T$, also $\nabla h(2,1)=(4,2)^T$. Die Richtungsableitung ist $(4,2)\cdot\frac15(3,4)=\frac15(12+8)=4$. Am stärksten steigt $h$ in Richtung $(4,2)/|(4,2)|=(2,1)/\sqrt5$, mit der Steigung $|(4,2)|=\sqrt{20}=2\sqrt5\approx4{,}47$. In erster Näherung gleich bleibt $h$ senkrecht dazu, in den Richtungen $\pm(-1,2)/\sqrt5$, denn $(4,2)\cdot(-1,2)=0$.

(b) $\nabla h(\gamma(t))=(2t^3,\;t^4-2t)$ und $\dot\gamma(t)=(2t,\,1)$. Nach [(1.10)](#gl-1-10) ist $\frac{\mathrm{d}}{\mathrm{d} t}h(\gamma(t))=4t^4+t^4-2t=5t^4-2t$. Einsetzen: $h(\gamma(t))=t^4\cdot t-t^2=t^5-t^2$ hat die Ableitung $5t^4-2t$.

(c) $h(2,1)=4-1=3$, also $z=3+4(x-2)+2(y-1)=4x+2y-7$.
:::
:::

:::aufgabe Aufgabe 6 ★★ Kettenregel als Matrixprodukt
<span class="anker" id="aufg-6"></span>

Sei $\boldsymbol{g}(s,t)=(s+t,\;st)$ und $\boldsymbol f(y_1,y_2)=(y_1y_2,\;y_1^2)$. Berechne $D(\boldsymbol f\circ\boldsymbol{g})(1,1)$ mit [(1.9)](#gl-1-9) und zur Kontrolle direkt.

:::loesung
$\boldsymbol{g}(1,1)=(2,1)$. Es ist $D\boldsymbol f(\boldsymbol{y})=\bigl(\begin{smallmatrix}y_2&y_1\\2y_1&0\end{smallmatrix}\bigr)$ und $D\boldsymbol{g}(s,t)=\bigl(\begin{smallmatrix}1&1\\t&s\end{smallmatrix}\bigr)$, also

$$D(\boldsymbol f\circ\boldsymbol{g})(1,1)=D\boldsymbol f(2,1)\,D\boldsymbol{g}(1,1)=\begin{pmatrix}1&2\\4&0\end{pmatrix}\begin{pmatrix}1&1\\1&1\end{pmatrix}=\begin{pmatrix}3&3\\4&4\end{pmatrix}.$$

Die äußere Matrix wird am Bildpunkt $(2,1)$ ausgewertet, nicht bei $(1,1)$. Direkt: $\boldsymbol f\circ\boldsymbol{g}=\bigl((s+t)st,\;(s+t)^2\bigr)=(s^2t+st^2,\;(s+t)^2)$ hat die Ableitungen $(2st+t^2,\;s^2+2st)$ und $(2(s+t),\;2(s+t))$, bei $(1,1)$ also dieselbe Matrix.
:::
:::

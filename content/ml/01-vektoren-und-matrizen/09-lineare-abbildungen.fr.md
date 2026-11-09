---
title: Applications linéaires
pfad: Informatique / Apprentissage automatique / Fondements mathématiques / Vecteurs et matrices
knoten: Fondements 1 : Vecteurs et matrices
nachschlagen: ja
order: 15210900
summary: Une matrice n’est pas seulement un tableau, mais aussi une règle de calcul qui transforme un vecteur en un autre.
tags: application, linéaire, rotation, étirement, cisaillement, affine, ordonnée à l’origine
lang: fr
---

<span class="anker" id="stufe-8"></span>

:::zweck
Une matrice n’est pas seulement un tableau, mais aussi une règle de calcul qui transforme un vecteur en un autre. Cette section montre quelles règles peuvent s’écrire ainsi, à savoir exactement les règles linéaires, et ce qu’une matrice fait géométriquement de l’espace.
:::

### Applications linéaires

<span class="anker" id="stufe-8-1"></span>

De nombreux calculs transforment une liste de nombres en une autre liste. À partir des caractéristiques d’un appartement, on estime son prix d’achat et son loyer ; à partir des échantillons d’un signal, on obtient un signal filtré. Une telle règle s’appelle une __application__ $f\colon\mathbb{R}^n\to\mathbb{R}^m$ : elle associe à chaque vecteur $\mathbf{x}\in\mathbb{R}^n$ un vecteur $f(\mathbf{x})\in\mathbb{R}^m$.

Le produit matrice-vecteur possède deux propriétés particulières (sous-section [7.1](das-matrix-vektor-produkt.html#stufe-7-1)) : $\mathbf{A}(\mathbf{u}+\mathbf{v})=\mathbf{A}\mathbf{u}+\mathbf{A}\mathbf{v}$ et $\mathbf{A}(c\,\mathbf{x})=c\,\mathbf{A}\mathbf{x}$. Il est indifférent d’additionner d’abord ou d’appliquer d’abord la matrice, et de même de multiplier d’abord par un nombre ou d’appliquer d’abord la matrice. Dans le plan, on voit ces propriétés sur un quadrillage : une telle application transforme des droites en droites ou en points isolés, laisse l’origine à sa place et transforme des lignes de quadrillage parallèles et équidistantes en lignes parallèles et équidistantes ou en points.

:::definition Définition 8.1 (Application linéaire)
<span class="anker" id="satz-8-1"></span>

Une application $f\colon\mathbb{R}^n\to\mathbb{R}^m$ est dite __linéaire__ si, pour tous $\mathbf{u},\mathbf{v}\in\mathbb{R}^n$ et tous les scalaires $c$, on a :

<span class="anker" id="gl-8-1"></span>
$$f(\mathbf{u}+\mathbf{v})=f(\mathbf{u})+f(\mathbf{v})\qquad\text{et}\qquad f(c\,\mathbf{u})=c\,f(\mathbf{u}) . \tag{8.1}$$
:::

Ensemble, les deux conditions signifient : $f$ conserve les combinaisons linéaires, $f(c_1\mathbf{u}+c_2\mathbf{v})=c_1f(\mathbf{u})+c_2f(\mathbf{v})$. Toute application linéaire envoie le vecteur nul sur le vecteur nul, car $f(\mathbf{0})=f(0\cdot\mathbf{u})=0\cdot f(\mathbf{u})=\mathbf{0}$.

::::beispiel [Exemple de calcul]
L’application $f(\mathbf{x})=(x_1+x_2,\ 2x_1)^{\top}$ de $\mathbb{R}^2$ dans $\mathbb{R}^2$ est linéaire. Ses deux composantes sont des sommes de multiples des $x_j$, et de telles sommes vérifient les conditions [(8.1)](#gl-8-1) ; par exemple, $f(\mathbf{u}+\mathbf{v})=(u_1+v_1+u_2+v_2,\ 2u_1+2v_1)^{\top}=f(\mathbf{u})+f(\mathbf{v})$. L’application $g(\mathbf{x})=x_1x_2$ n’est pas linéaire, car $g(2\mathbf{x})=4x_1x_2\ne2\,g(\mathbf{x})$ dès que $x_1x_2\ne0$. L’application $h(\mathbf{x})=\mathbf{x}+\mathbf 1$ n’est pas linéaire non plus, car $h(\mathbf{0})=\mathbf 1\ne\mathbf{0}$.
::::

⁠**En bref :** Une application est linéaire si elle conserve les sommes et les multiples ; elle envoie alors des combinaisons linéaires sur des combinaisons linéaires.

:::hintergrund La même linéarité que pour les systèmes LTI
En théorie des signaux et des systèmes, on connaît le principe de superposition : un système linéaire répond à la somme de deux signaux d’entrée par la somme des deux réponses, et à un signal amplifié par la réponse amplifiée dans la même proportion. Ce sont exactement les conditions [(8.1)](#gl-8-1), simplement pour des signaux au lieu de listes de nombres. Un signal échantillonné de longueur finie est un vecteur (sous-section [1.3](vektoren-daten-als-zahlenlisten.html#stufe-1-3)), et un système linéaire qui traite de tels signaux est une application linéaire.
:::

### Toute application linéaire est une matrice

<span class="anker" id="stufe-8-2"></span>

Toute matrice fournit une application linéaire $\mathbf{x}\mapsto\mathbf{A}\mathbf{x}$. La réciproque est-elle vraie ? Oui, et la raison est simple : tout vecteur est une combinaison linéaire des vecteurs unitaires, et une application linéaire conserve les combinaisons linéaires. Qui sait où vont les $n$ vecteurs unitaires sait donc où va chaque vecteur.

:::satz Théorème 8.2 (Matrice d’une application linéaire)
<span class="anker" id="satz-8-2"></span>

Pour toute application linéaire $f\colon\mathbb{R}^n\to\mathbb{R}^m$, il existe exactement une matrice $\mathbf{A}\in\mathbb{R}^{m\times n}$ telle que $f(\mathbf{x})=\mathbf{A}\mathbf{x}$ pour tout $\mathbf{x}\in\mathbb{R}^n$. Ses colonnes sont les images des vecteurs unitaires :

<span class="anker" id="gl-8-2"></span>
$$\mathbf{a}_j=f(\mathbf{e}_j),\qquad j=1,\dots,n . \tag{8.2}$$
:::

:::beweis Matrice d’une application linéaire
D’après [(1.6)](vektoren-daten-als-zahlenlisten.html#gl-1-6), on a $\mathbf{x}=\sum_jx_j\mathbf{e}_j$. Comme $f$ est linéaire, il s’ensuit

$$f(\mathbf{x})=f\Bigl(\sum_{j=1}^nx_j\mathbf{e}_j\Bigr)=\sum_{j=1}^nx_j\,f(\mathbf{e}_j)=\sum_{j=1}^nx_j\,\mathbf{a}_j=\mathbf{A}\mathbf{x} ,$$

la dernière égalité découlant de la vue par colonnes [(7.3)](das-matrix-vektor-produkt.html#gl-7-3). S’il existait une seconde matrice $\mathbf{B}$ telle que $\mathbf{B}\mathbf{x}=f(\mathbf{x})$ pour tout $\mathbf{x}$, alors, avec $\mathbf{x}=\mathbf{e}_j$, la colonne $j$ de $\mathbf{B}$ serait égale à $f(\mathbf{e}_j)=\mathbf{a}_j$, et ce pour chaque $j$. Donc $\mathbf{B}=\mathbf{A}$.
:::

::::beispiel [Exemple de calcul]
Pour $f(\mathbf{x})=(x_1+x_2,\ 2x_1)^{\top}$, on a $f(\mathbf{e}_1)=(1,\,2)^{\top}$ et $f(\mathbf{e}_2)=(1,\,0)^{\top}$. Donc

$$\mathbf{A}=\begin{pmatrix}1&1\\2&0\end{pmatrix},\qquad\text{et pour vérifier}\qquad \mathbf{A}\begin{pmatrix}3\\-1\end{pmatrix}=\begin{pmatrix}2\\6\end{pmatrix}=f\bigl((3,\,-1)^{\top}\bigr).$$
::::

⁠**En bref :** Applications linéaires et matrices sont une seule et même chose ; la colonne $j$ de la matrice est l’image du vecteur unitaire $\mathbf{e}_j$.

:::hintergrund Un filtre comme matrice : les colonnes sont les réponses impulsionnelles décalées
Soit un filtre à temps discret qui calcule $y[n]=x[n]+0{,}5\,x[n-1]$ et qui traite des signaux de trois échantillons, aucun signal n’étant présent avant le premier échantillon. Le filtre est linéaire, il a donc une matrice. D’après [(8.2)](#gl-8-2), sa colonne $j$ est la réponse au vecteur unitaire $\mathbf{e}_j$, c’est-à-dire à une seule impulsion unité à la position $j$. Cette réponse est la réponse impulsionnelle $(1;\,0{,}5)$, décalée de $j-1$ pas :

$$\mathbf{A}=\begin{pmatrix}1&0&0\\0{,}5&1&0\\0&0{,}5&1\end{pmatrix}.$$

La troisième colonne ne contient plus que le $1$, parce que le signal s’arrête après trois échantillons. Pour $\mathbf{x}=(2,\,4,\,6)^{\top}$, la matrice fournit $(2,\,5,\,8)^{\top}$, comme la formule du filtre. Toute convolution d’un signal fini est de cette manière un produit matrice-vecteur, et le théorème ci-dessus explique pourquoi : si l’on connaît la réponse à chaque impulsion isolée, on connaît tout le système.
:::

:::hintergrund Données ou application ? Deux rôles du même tableau
Une matrice peut être une collection de données, comme la matrice de données $\mathbf{X}$, ou une application, comme la matrice d’un filtre. Formellement, c’est la même chose, et parfois la même matrice joue les deux rôles à la fois : la matrice de données est aussi l’application $\mathbf{w}\mapsto\mathbf{X}\mathbf{w}$, qui transforme des poids en prédictions. Elle envoie l’espace $\mathbb{R}^d$ des poids dans l’espace $\mathbb{R}^N$ des listes de prédictions. En lisant une formule, il vaut donc la peine de se demander dans quel rôle une matrice apparaît à ce moment-là.
:::

### Applications linéaires du plan

<span class="anker" id="stufe-8-3"></span>

Dans le plan, on peut voir ce que fait une matrice. On dessine le carré unité de sommets $\mathbf{0}$, $\mathbf{e}_1$, $\mathbf{e}_1+\mathbf{e}_2$ et $\mathbf{e}_2$, ainsi que son image. Comme l’application conserve les combinaisons linéaires, le carré devient le parallélogramme de sommets $\mathbf{0}$, $\mathbf{a}_1$, $\mathbf{a}_1+\mathbf{a}_2$ et $\mathbf{a}_2$. Ses deux côtés issus de l’origine sont les colonnes de la matrice (Fig. [32](#abb-32)). Tout le quadrillage du plan est déformé de la même façon : chaque case devient une copie translatée de ce parallélogramme.

:::abbildung ml/k1ebene 32
Quatre applications linéaires du plan. En gris pointillé, le carré unité ; en bleu, son image. La flèche rouge est l’image $\mathbf{a}_1$ de $\mathbf{e}_1$, la verte l’image $\mathbf{a}_2$ de $\mathbf{e}_2$ ; ce sont les deux colonnes de la matrice. Pour l’aplatissement, $\mathbf{a}_2=\mathbf{0}$, et le carré devient le segment allant de $\mathbf{0}$ à $\mathbf{e}_1$.
:::

<ul>

<li>

La __rotation__ de $90^\circ$ dans le sens inverse des aiguilles d’une montre envoie $\mathbf{e}_1$ sur $(0,\,1)^{\top}$ et $\mathbf{e}_2$ sur $(-1,\,0)^{\top}$ ; ce sont ses colonnes.

</li>

<li>

L’__étirement__ $\operatorname{diag}(2;\,0{,}5)$ allonge le plan au double dans le sens horizontal et le comprime de moitié dans le sens vertical.

</li>

<li>

Le __cisaillement__ $\bigl(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\bigr)$ laisse $\mathbf{e}_1$ à sa place et pousse $\mathbf{e}_2$ vers la droite : chaque point est décalé vers la droite d’une distance égale à sa hauteur.

</li>

<li>

La matrice $\operatorname{diag}(1;\,0)$ conserve la première composante et met la deuxième à zéro. Elle aplatit tout le plan sur l’axe des $x_1$.

</li>

</ul>

::::beispiel [Exemple de calcul] la rotation d’un angle quelconque
Si l’on tourne de l’angle $\alpha$ dans le sens inverse des aiguilles d’une montre, $\mathbf{e}_1$ arrive au point $(\cos\alpha,\,\sin\alpha)^{\top}$ du cercle unité, et $\mathbf{e}_2$, situé $90^\circ$ plus loin, au point $(-\sin\alpha,\,\cos\alpha)^{\top}$. D’après [(8.2)](#gl-8-2), la matrice de rotation est donc

<span class="anker" id="gl-8-3"></span>
$$\mathbf R_\alpha=\begin{pmatrix}\cos\alpha&-\sin\alpha\\\sin\alpha&\cos\alpha\end{pmatrix}. \tag{8.3}$$

Pour $\alpha=90^\circ$, on retrouve la matrice de la Fig. [32](#abb-32). Elle fait tourner le point $(1,\,1)^{\top}$ en $(-1,\,1)^{\top}$ ; l’étirement l’envoie sur $(2;\ 0{,}5)^{\top}$, le cisaillement sur $(2,\,1)^{\top}$ et l’aplatissement sur $(1,\,0)^{\top}$.
::::

⁠**En bref :** Une matrice $2\times2$ déforme le quadrillage du plan ; le carré unité devient le parallélogramme construit sur ses deux colonnes.

### Fonctions linéaires à une seule sortie

<span class="anker" id="stufe-8-4"></span>

Un modèle qui tire un seul nombre des caractéristiques d’un exemple est une application de $\mathbb{R}^d$ dans $\mathbb{R}$. Si elle est linéaire, sa matrice est, d’après le théorème de la sous-section [8.2](#stufe-8-2), une seule ligne de $d$ coefficients.

:::satz Théorème 8.3 (Les fonctions linéaires sont des sommes pondérées)
<span class="anker" id="satz-8-3"></span>

Toute application linéaire $f\colon\mathbb{R}^d\to\mathbb{R}$ est de la forme $f(\mathbf{x})=\mathbf{w}^{\top}\mathbf{x}$, avec les poids $w_j=f(\mathbf{e}_j)$.
:::

C’est le théorème de la sous-section [8.2](#stufe-8-2) pour $m=1$ : la matrice $1\times d$ est la ligne $\mathbf{w}^{\top}$, et son produit avec $\mathbf{x}$ est le produit scalaire. La somme pondérée de la sous-section [2.2](das-skalarprodukt.html#stufe-2-2) n’est donc pas un exemple parmi d’autres, mais la règle linéaire la plus générale à une seule sortie.

::::beispiel [Exemple de calcul]
La règle de l’agente immobilière est $f(\mathbf{x})=3x_1+10x_2-4x_3$. On a $f(\mathbf{e}_1)=3$, $f(\mathbf{e}_2)=10$, $f(\mathbf{e}_3)=-4$, donc $\mathbf{w}=(3,\,10,\,-4)^{\top}$. Le poids $w_j=f(\mathbf{e}_j)$ est la valeur de la règle pour un exemple imaginaire qui ne possède qu’une unité de la caractéristique $j$ et rien d’autre : il indique combien une unité de cette caractéristique apporte.
::::

⁠**En bref :** Toute application linéaire à une seule sortie est une somme pondérée $\mathbf{w}^{\top}\mathbf{x}$, et le poids $w_j$ est sa valeur en $\mathbf{e}_j$.

### Applications affines

<span class="anker" id="stufe-8-5"></span>

L’agente immobilière remarque que ses estimations sont systématiquement trop basses. Elle ajoute donc à chaque somme pondérée un montant de base de $20$ mille euros. Cette nouvelle règle n’est plus linéaire : à un appartement imaginaire $\mathbf{x}=\mathbf{0}$, elle associe $20$ et non $0$. C’est une application linéaire suivie d’une translation.

:::definition Définition 8.4 (Application affine)
<span class="anker" id="satz-8-4"></span>

Une application $f\colon\mathbb{R}^n\to\mathbb{R}^m$ de la forme

<span class="anker" id="gl-8-4"></span>
$$f(\mathbf{x})=\mathbf{A}\mathbf{x}+\mathbf{b} \tag{8.4}$$

avec une matrice $\mathbf{A}\in\mathbb{R}^{m\times n}$ et un vecteur fixe $\mathbf{b}\in\mathbb{R}^m$ est dite __affine__. Pour une seule sortie ($m=1$), on écrit $f(\mathbf{x})=\mathbf{w}^{\top}\mathbf{x}+b$, et l’on appelle le nombre $b$ l’__ordonnée à l’origine__.
:::

Pour $\mathbf{b}\ne\mathbf{0}$, une application affine n’est pas linéaire, car $f(\mathbf{0})=\mathbf{b}\ne\mathbf{0}$. Dans l’image du quadrillage, le plan est d’abord déformé, puis translaté en bloc de $\mathbf{b}$ ; l’origine arrive en $\mathbf{b}$. Dans le langage courant, on qualifie souvent aussi de « linéaires » des règles affines. Dans cette série, seule une application avec $\mathbf{b}=\mathbf{0}$ est dite linéaire.

Pour tous les exemples à la fois, on écrit la prédiction affine à l’aide du vecteur de uns $\mathbf 1\in\mathbb{R}^N$ :

<span class="anker" id="gl-8-5"></span>
$$\hat{\mathbf{y}}=\mathbf{X}\mathbf{w}+b\,\mathbf 1 . \tag{8.5}$$

Le terme $b\,\mathbf 1$ ajoute à chaque prédiction le même montant $b$.

::::beispiel [Exemple de calcul]
Avec $\mathbf{w}=(3,\,10,\,-4)^{\top}$ et $b=20$, les prédictions $(188,\,126,\,286,\,232)^{\top}$ deviennent

$$\hat{\mathbf{y}}=\mathbf{X}\mathbf{w}+20\cdot\mathbf 1=(208,\,146,\,306,\,252)^{\top}\ \text{milliers d’euros}.$$
::::

⁠**En bref :** Une application affine est une application linéaire plus une translation fixe, $\mathbf{A}\mathbf{x}+\mathbf{b}$ ; pour une seule sortie, la translation s’appelle l’ordonnée à l’origine.

:::hintergrund L’astuce de la composante égale à un
Une fonction affine peut s’écrire comme une fonction linéaire si l’on ajoute à chaque exemple une composante de valeur fixe $1$ :

$$\mathbf{w}^{\top}\mathbf{x}+b=\begin{pmatrix}w_1&\cdots&w_d&b\end{pmatrix}\begin{pmatrix}x_1\\\vdots\\x_d\\1\end{pmatrix}.$$

L’ordonnée à l’origine devient ainsi le poids d’une caractéristique qui vaut toujours $1$. Pour l’ensemble du jeu de données, on ajoute à la matrice de données une colonne de uns : $\begin{pmatrix}\mathbf{X}&\mathbf 1\end{pmatrix}\begin{pmatrix}\mathbf{w}\\b\end{pmatrix}=\mathbf{X}\mathbf{w}+b\,\mathbf 1$. Pour les appartements, la matrice de données augmentée a pour lignes $(60,2,3,1)$, $(40,1,1,1)$, $(90,4,6,1)$, $(70,3,2,1)$, et avec le vecteur $(3,\,10,\,-4,\,20)^{\top}$, on retrouve $(208,\,146,\,306,\,252)^{\top}$. Grâce à cette astuce, les règles affines n’ont pas besoin d’une théorie propre : tout ce qui vaut pour les applications linéaires vaut aussi pour elles, dans l’espace qui a une dimension de plus.
:::

:::aufgabe Exercice 18 ★ Linéaire ou non ?
<span class="anker" id="aufg-18"></span>

Vérifiez lesquelles des applications suivantes sont linéaires et donnez la matrice de celles qui le sont :

$$\begin{gathered} f_1(\mathbf{x})=(2x_1,\ x_1-x_2)^{\top},\qquad f_2(\mathbf{x})=x_1^2,\qquad f_3(\mathbf{x})=(x_2,\ x_1)^{\top},\\ f_4(x)=2x+3,\qquad f_5(\mathbf{x})=(0,\ 0)^{\top} \end{gathered}$$

pour $\mathbf{x}\in\mathbb{R}^2$, ou $x\in\mathbb{R}$ dans le cas de $f_4$.

:::loesung
<ul>

<li>

$f_1$ est linéaire ; ses deux composantes sont des sommes de multiples des $x_j$. Les colonnes sont $f_1(\mathbf{e}_1)=(2,\,1)^{\top}$ et $f_1(\mathbf{e}_2)=(0,\,-1)^{\top}$, donc $\bigl(\begin{smallmatrix}2&0\\1&-1\end{smallmatrix}\bigr)$.

</li>

<li>

$f_2$ n’est pas linéaire : $f_2(2\mathbf{x})=4x_1^2\ne2f_2(\mathbf{x})$ dès que $x_1\ne0$.

</li>

<li>

$f_3$ est linéaire, de matrice $\bigl(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr)$ ; elle échange les composantes.

</li>

<li>

$f_4$ n’est pas linéaire, car $f_4(0)=3\ne0$. Elle est affine, d’ordonnée à l’origine $3$.

</li>

<li>

$f_5$ est linéaire, et sa matrice est la matrice nulle ; les deux conditions sont vérifiées, car $\mathbf{0}+\mathbf{0}=\mathbf{0}$ et $c\,\mathbf{0}=\mathbf{0}$.

</li>

</ul>
:::
:::

:::aufgabe Exercice 19 ★★ Des matrices à partir des images des vecteurs unitaires
<span class="anker" id="aufg-19"></span>

<ol class="al">

<li>

Donnez la matrice de la rotation de $30^\circ$ et calculez l’image de $(2,\,0)^{\top}$.

</li>

<li>

La réflexion par rapport à la première bissectrice $x_1=x_2$ échange les deux composantes. Donnez sa matrice et l’image de $(3,\,1)^{\top}$.

</li>

<li>

Une application linéaire vérifie $f\bigl((1,\,1)^{\top}\bigr)=(1,\,4)^{\top}$ et $f\bigl((2,\,-1)^{\top}\bigr)=(5,\,-1)^{\top}$. Déterminez sa matrice. Indication : écrivez les deux conditions à l’aide des colonnes $\mathbf{a}_1,\mathbf{a}_2$.

</li>

</ol>

:::loesung
(a) D’après [(8.3)](#gl-8-3), avec $\cos30^\circ=\sqrt3/2\approx0{,}866$ et $\sin30^\circ=\tfrac12$ :

$$\mathbf R_{30^\circ}=\begin{pmatrix}0{,}866&-0{,}5\\0{,}5&0{,}866\end{pmatrix},\qquad \mathbf R_{30^\circ}\begin{pmatrix}2\\0\end{pmatrix}=\begin{pmatrix}\sqrt3\\1\end{pmatrix}\approx\begin{pmatrix}1{,}732\\1\end{pmatrix}.$$

L’image est le double de la première colonne, une flèche de longueur $2$ inclinée de $30^\circ$.

(b) $\mathbf{e}_1$ est envoyé sur $\mathbf{e}_2$ et $\mathbf{e}_2$ sur $\mathbf{e}_1$ ; la matrice est donc $\bigl(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr)$, et $(3,\,1)^{\top}$ est envoyé sur $(1,\,3)^{\top}$.

(c) Par linéarité, $f\bigl((1,1)^{\top}\bigr)=\mathbf{a}_1+\mathbf{a}_2=(1,\,4)^{\top}$ et $f\bigl((2,-1)^{\top}\bigr)=2\mathbf{a}_1-\mathbf{a}_2=(5,\,-1)^{\top}$. En additionnant les deux équations, on obtient $3\mathbf{a}_1=(6,\,3)^{\top}$, donc $\mathbf{a}_1=(2,\,1)^{\top}$ et $\mathbf{a}_2=(1,4)^{\top}-(2,1)^{\top}=(-1,\,3)^{\top}$. La matrice est $\bigl(\begin{smallmatrix}2&-1\\1&3\end{smallmatrix}\bigr)$. Vérification : $\bigl(\begin{smallmatrix}2&-1\\1&3\end{smallmatrix}\bigr)(2,\,-1)^{\top}=(5,\,-1)^{\top}$.
:::
:::

:::aufgabe Exercice 20 ★★ Un différentiateur comme matrice
<span class="anker" id="aufg-20"></span>

Un filtre calcule, à partir d’un signal de quatre échantillons, les différences $y[n]=x[n]-x[n-1]$, en supposant $x[0]=0$ avant le premier échantillon, $n=1,\dots,4$.

<ol class="al">

<li>

Pourquoi le filtre est-il linéaire ? Établissez sa matrice $4\times4$ en calculant les réponses aux quatre impulsions unité.

</li>

<li>

Calculez la réponse à $\mathbf{x}=(1,\,2,\,4,\,7)^{\top}$ avec la matrice et avec la formule.

</li>

</ol>

:::loesung
(a) Chaque composante de sortie $y[n]=x[n]-x[n-1]$ est une somme fixe de multiples des composantes d’entrée ; le filtre est donc linéaire. La réponse à l’impulsion en position $1$, $\mathbf{x}=\mathbf{e}_1=(1,0,0,0)^{\top}$, est $(1,\,-1,\,0,\,0)^{\top}$ : le signal saute d’abord à $1$, puis revient à $0$. De même, le filtre répond à $\mathbf{e}_2$ par $(0,\,1,\,-1,\,0)^{\top}$, à $\mathbf{e}_3$ par $(0,\,0,\,1,\,-1)^{\top}$ et à $\mathbf{e}_4$ par $(0,\,0,\,0,\,1)^{\top}$ ; pour cette dernière impulsion, le signal s’arrête avant qu’elle ne retombe. Ces réponses sont les colonnes :

$$\mathbf{A}=\begin{pmatrix}1&0&0&0\\-1&1&0&0\\0&-1&1&0\\0&0&-1&1\end{pmatrix}.$$

(b) Avec la matrice : $\mathbf{A}\,(1,2,4,7)^{\top}=(1,\ -1+2,\ -2+4,\ -4+7)^{\top}=(1,\,1,\,2,\,3)^{\top}$. Avec la formule : $y[1]=1-0=1$, $y[2]=2-1=1$, $y[3]=4-2=2$, $y[4]=7-4=3$.
:::
:::

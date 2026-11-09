---
title: Les matrices et la matrice de données
pfad: Informatique / Apprentissage automatique / Fondements mathématiques / Vecteurs et matrices
knoten: Fondements 1 : Vecteurs et matrices
nachschlagen: ja
order: 15210700
summary: Un jeu de données se compose de nombreux vecteurs de même longueur.
tags: matrice, coefficient, taille, carrée, diagonale, matrice diagonale, matrice nulle, matrice de données
lang: fr
---

<span class="anker" id="stufe-6"></span>

:::zweck
Un jeu de données se compose de nombreux vecteurs de même longueur. Cette section les réunit en un seul tableau de nombres, une matrice, et fixe la façon d’écrire les matrices et de calculer avec elles.
:::

### Matrices

<span class="anker" id="stufe-6-1"></span>

Le tableau des appartements est plus que quatre vecteurs isolés : c’est un objet avec lequel on veut calculer comme un tout. Une image en niveaux de gris est elle aussi un tableau, à savoir un tableau de luminosités, disposées en lignes et en colonnes. Un tel schéma rectangulaire de nombres s’appelle une matrice.

:::definition Définition 6.1 (Matrice)
<span class="anker" id="satz-6-1"></span>

Une __matrice__ $\mathbf{A}\in\mathbb{R}^{m\times n}$ est une disposition rectangulaire de $m\cdot n$ nombres réels en $m$ lignes et $n$ colonnes :

$$\mathbf{A}=\begin{pmatrix}a_{11}&a_{12}&\cdots&a_{1n}\\a_{21}&a_{22}&\cdots&a_{2n}\\\vdots&\vdots&&\vdots\\a_{m1}&a_{m2}&\cdots&a_{mn}\end{pmatrix}.$$

Le nombre $a_{ij}$ situé à la ligne $i$ et à la colonne $j$ s’appelle __coefficient__ de la matrice. Le couple $m\times n$ s’appelle la __taille__ de la matrice.
:::

Les matrices s’écrivent en majuscules grasses, leurs coefficients avec la lettre minuscule et deux indices : d’abord la ligne, puis la colonne. La $j$-ième colonne de $\mathbf{A}$ est un vecteur à $m$ composantes ; on la note $\mathbf{a}_j$. On écrit alors aussi la matrice comme la suite de ses colonnes, $\mathbf{A}=\begin{pmatrix}\mathbf{a}_1&\cdots&\mathbf{a}_n\end{pmatrix}$. Un vecteur à $d$ composantes est une matrice de taille $d\times1$, une ligne de $d$ nombres une matrice de taille $1\times d$.

Deux matrices sont égales si elles ont la même taille et le même coefficient à chaque position. On additionne des matrices de même taille et on les multiplie par un nombre coefficient par coefficient, exactement comme les vecteurs : $(\mathbf{A}+\mathbf{B})_{ij}=a_{ij}+b_{ij}$ et $(c\,\mathbf{A})_{ij}=c\,a_{ij}$.

⁠**Exemple de calcul :** La matrice

$$\mathbf{A}=\begin{pmatrix}1&2&3\\4&5&6\end{pmatrix}\in\mathbb{R}^{2\times3}$$

est de taille $2\times3$, a pour coefficients $a_{12}=2$ et $a_{21}=4$, et pour deuxième colonne $\mathbf{a}_2=(2,\,5)^{\top}$. Une image en niveaux de gris de $3\times3$ pixels qui montre une croix claire sur fond sombre est la matrice de lignes $(0,1,0)$, $(1,1,1)$ et $(0,1,0)$. De plus,

$$\begin{pmatrix}1&2\\3&4\end{pmatrix}+\begin{pmatrix}0&1\\1&0\end{pmatrix}=\begin{pmatrix}1&3\\4&4\end{pmatrix},\qquad 2\begin{pmatrix}1&2\\3&4\end{pmatrix}=\begin{pmatrix}2&4\\6&8\end{pmatrix}.$$

⁠**En bref :** Une matrice est un tableau rectangulaire de nombres à $m$ lignes et $n$ colonnes ; le coefficient $a_{ij}$ se trouve à la ligne $i$ et à la colonne $j$.

:::hintergrund Une image comme matrice et comme vecteur
Si l’on lit une image ligne par ligne et que l’on met les lignes bout à bout, la matrice devient un long vecteur : la croix $3\times3$ donne le vecteur $(0,1,0,1,1,1,0,1,0)^{\top}\in\mathbb{R}^9$, une image $28\times28$ un vecteur de $\mathbb{R}^{784}$. Les nombres restent les mêmes, mais une information se perd dans l’écriture : quels pixels sont voisins. Le pixel situé juste sous un autre se trouve, dans le long vecteur, $28$ positions plus loin. Pour les calculs qui pondèrent chaque caractéristique séparément, cela ne joue aucun rôle. Pour les calculs qui veulent exploiter les voisinages, la forme matricielle est la plus naturelle.
:::

### Matrices carrées et matrices diagonales

<span class="anker" id="stufe-6-2"></span>

Certaines matrices reviennent si souvent qu’elles portent un nom particulier. Pour ces trois types, la forme du tableau est particulièrement simple.

Une matrice qui a autant de lignes que de colonnes est dite __carrée__. Les coefficients $a_{11},a_{22},\dots,a_{nn}$ d’une matrice carrée forment sa __diagonale__, qui va du coin supérieur gauche au coin inférieur droit.

:::definition Définition 6.2 (Matrice diagonale, matrice nulle)
<span class="anker" id="satz-6-2"></span>

Une matrice carrée dont les coefficients hors de la diagonale sont tous nuls s’appelle une __matrice diagonale__. Pour un vecteur $\mathbf{v}\in\mathbb{R}^n$, $\operatorname{diag}(\mathbf{v})$ est la matrice diagonale de coefficients diagonaux $v_1,\dots,v_n$.

La matrice dont tous les coefficients sont nuls s’appelle la __matrice nulle__ et se note $\mathbf 0$.
:::

⁠**Exemple de calcul :**

$$\operatorname{diag}\bigl((2;\ 0{,}5)^{\top}\bigr)=\begin{pmatrix}2&0\\0&0{,}5\end{pmatrix},\qquad \operatorname{diag}\bigl((1,\,0,\,3)^{\top}\bigr)=\begin{pmatrix}1&0&0\\0&0&0\\0&0&3\end{pmatrix}.$$

La seconde matrice a un coefficient diagonal nul et est pourtant une matrice diagonale ; on exige seulement que des zéros figurent hors de la diagonale. Au lieu de $\operatorname{diag}\bigl((2;\ 0{,}5)^{\top}\bigr)$, on écrit plus brièvement $\operatorname{diag}(2;\,0{,}5)$.

⁠**En bref :** Une matrice carrée a autant de lignes que de colonnes ; une matrice diagonale n’a de coefficients non nuls que sur sa diagonale.

### La matrice de données

<span class="anker" id="stufe-6-3"></span>

Le tableau des appartements de la sous-section [1.2](vektoren-daten-als-zahlenlisten.html#stufe-1-2) est une matrice : quatre lignes, une par appartement, et trois colonnes, une par caractéristique. Cette disposition, un exemple par ligne, est la forme standard d’un jeu de données (Fig. [27](#abb-27)).

:::abbildung ml/k1datenmatrix 27
La matrice de données $\mathbf{X}$ du jeu de données des appartements. Chaque ligne est un exemple, sous la forme du vecteur écrit en ligne $\mathbf{x}_i^{\top}$ (en bleu : l’appartement 2). Chaque colonne est la colonne d’une caractéristique sur l’ensemble des exemples (en orange : les surfaces). Le coefficient $x_{21}=40$ figure dans les deux.
:::

:::definition Définition 6.3 (Matrice de données)
<span class="anker" id="satz-6-3"></span>

Pour un jeu de données d’exemples $\mathbf{x}_1,\dots,\mathbf{x}_N\in\mathbb{R}^d$, la __matrice de données__ est la matrice $\mathbf{X}\in\mathbb{R}^{N\times d}$ dont la ligne $i$ est l’exemple $\mathbf{x}_i$, écrit en ligne :

<span class="anker" id="gl-6-1"></span>
$$\mathbf{X}=\begin{pmatrix}\mathbf{x}_1^{\top}\\\mathbf{x}_2^{\top}\\\vdots\\\mathbf{x}_N^{\top}\end{pmatrix}=\begin{pmatrix}x_{11}&\cdots&x_{1d}\\\vdots&&\vdots\\x_{N1}&\cdots&x_{Nd}\end{pmatrix}. \tag{6.1}$$
:::

Le coefficient $x_{ij}$ est la valeur de la caractéristique $j$ pour l’exemple $i$, exactement comme convenu dans la sous-section [1.3](vektoren-daten-als-zahlenlisten.html#stufe-1-3). La colonne $j$ de $\mathbf{X}$ est la colonne de la caractéristique $j$ de la sous-section [4.3](abstande-und-einheiten.html#stufe-4-3) : toutes les valeurs de cette caractéristique sur l’ensemble des exemples. Les lignes correspondent donc aux exemples, les colonnes aux caractéristiques. La moyenne des exemples $\bar{\mathbf{x}}$ a pour composante $j$ la moyenne de la colonne $j$.

⁠**Exemple de calcul :** Pour le jeu de données des appartements, on a

$$\mathbf{X}=\begin{pmatrix}60&2&3\\40&1&1\\90&4&6\\70&3&2\end{pmatrix}\in\mathbb{R}^{4\times3}.$$

Le coefficient $x_{32}=4$ est le nombre de pièces de l’appartement 3, la première colonne $(60,\,40,\,90,\,70)^{\top}$ contient toutes les surfaces, et sa moyenne $65$ est la première composante de $\bar{\mathbf{x}}=(65;\ 2{,}5;\ 3)^{\top}$.

⁠**En bref :** La matrice de données $\mathbf{X}\in\mathbb{R}^{N\times d}$ contient un exemple par ligne et une caractéristique par colonne.

:::hintergrund Les exemples en lignes ou en colonnes ?
Cette série écrit les exemples en lignes, comme dans un tableur et dans la plupart des manuels et des bibliothèques logicielles actuels. Certains textes font l’inverse et placent les exemples en colonnes, côte à côte ; leur matrice de données est alors de taille $d\times N$. Les lettres varient aussi : souvent, le nombre d’exemples s’appelle $m$ et le nombre de caractéristiques $n$, et l’exemple numéro $i$ s’écrit $\mathbf{x}^{(i)}$, avec l’indice en haut entre parenthèses. Sur le fond, rien ne change. Qui lit un texte qu’il ne connaît pas vérifie donc d’abord ce qui y est ligne et ce qui y est colonne.
:::

:::aufgabe Exercice 15 ★ Lire et construire des matrices
<span class="anker" id="aufg-15"></span>

<ol class="al">

<li>

Quelle est la taille de $\mathbf{B}=\bigl(\begin{smallmatrix}1&0&2\\2&1&0\end{smallmatrix}\bigr)$ ? Donnez $b_{13}$, $b_{21}$ et la troisième colonne de $\mathbf{B}$.

</li>

<li>

Écrivez la matrice de données des trois textes de la sous-section [5.4](winkel-und-ahnlichkeit.html#stufe-5-4). Que signifient $N$, $d$ et le coefficient $x_{23}$ ?

</li>

<li>

Une image en niveaux de gris de $4\times4$ pixels montre un « L » clair : la première colonne et la ligne du bas sont claires ($1$), tout le reste est sombre ($0$). Écrivez la matrice et lisez-la ligne par ligne pour en faire un vecteur. Combien de composantes a-t-il ?

</li>

</ol>

:::loesung
(a) $\mathbf{B}$ est de taille $2\times3$. On a $b_{13}=2$ (ligne 1, colonne 3) et $b_{21}=2$ (ligne 2, colonne 1) ; la troisième colonne est $(2,\,0)^{\top}$.

(b) $\mathbf{X}=\Bigl(\begin{smallmatrix}3&2&0\\6&4&0\\0&1&3\end{smallmatrix}\Bigr)$, avec $N=3$ textes et $d=3$ mots. Le coefficient $x_{23}=0$ signifie : le troisième mot, « élection », n’apparaît pas dans le deuxième texte.

(c) La matrice a pour lignes $(1,0,0,0)$, $(1,0,0,0)$, $(1,0,0,0)$ et $(1,1,1,1)$. Lue ligne par ligne, elle donne le vecteur

$$(1,0,0,0,\ 1,0,0,0,\ 1,0,0,0,\ 1,1,1,1)^{\top}\in\mathbb{R}^{16}$$

à $4\cdot4=16$ composantes.
:::
:::

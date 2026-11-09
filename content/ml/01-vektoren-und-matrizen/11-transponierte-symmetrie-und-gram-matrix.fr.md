---
title: Transposée, symétrie et matrice de Gram
pfad: Informatique / Apprentissage automatique / Fondements mathématiques / Vecteurs et matrices
knoten: Fondements 1 : Vecteurs et matrices
nachschlagen: ja
order: 15211100
summary: Si l’on échange les lignes et les colonnes d’une matrice, on obtient sa transposée.
tags: transposée, symétrique, matrice de Gram
lang: fr
---

<span class="anker" id="stufe-10"></span>

:::zweck
Si l’on échange les lignes et les colonnes d’une matrice, on obtient sa transposée. Elle permet de rassembler tous les produits scalaires d’un jeu de données dans une seule matrice : les ressemblances de tous les exemples entre eux et les liens de toutes les caractéristiques entre elles.
:::

### La transposée

<span class="anker" id="stufe-10-1"></span>

Le signe $^{\top}$ est connu depuis la sous-section [1.3](vektoren-daten-als-zahlenlisten.html#stufe-1-3) : il transforme une colonne en ligne. Pour les matrices, il signifie la même chose, appliquée à chaque colonne : la colonne $j$ devient la ligne $j$. La matrice subit ainsi une symétrie par rapport à sa diagonale.

:::definition Définition 10.1 (Transposée)
<span class="anker" id="satz-10-1"></span>

La __transposée__ d’une matrice $\mathbf{A}\in\mathbb{R}^{m\times n}$ est la matrice $\mathbf{A}^{\top}\in\mathbb{R}^{n\times m}$ telle que

<span class="anker" id="gl-10-1"></span>
$$(\mathbf{A}^{\top})_{ij}=a_{ji} . \tag{10.1}$$
:::

Un vecteur $\mathbf{x}\in\mathbb{R}^d$ est une matrice $d\times1$, sa transposée $\mathbf{x}^{\top}$ la matrice $1\times d$ ayant les mêmes coefficients. L’écriture $\mathbf{u}^{\top}\mathbf{v}$ de la sous-section [2.1](das-skalarprodukt.html#stufe-2-1) est donc désormais, au sens littéral, un produit matriciel : une matrice $1\times d$ fois une matrice $d\times1$, dont le résultat est une matrice $1\times1$, c’est-à-dire un nombre.

:::satz Théorème 10.2 (Règles de calcul de la transposée)
<span class="anker" id="satz-10-2"></span>

Pour des matrices de tailles compatibles et des scalaires $c$, on a

$$(\mathbf{A}^{\top})^{\top}=\mathbf{A},\qquad(\mathbf{A}+\mathbf{B})^{\top}=\mathbf{A}^{\top}+\mathbf{B}^{\top},\qquad(c\,\mathbf{A})^{\top}=c\,\mathbf{A}^{\top},\qquad(\mathbf{A}\mathbf{B})^{\top}=\mathbf{B}^{\top}\mathbf{A}^{\top} .$$
:::

:::herleitung La transposée d’un produit
Pour $\mathbf{A}\in\mathbb{R}^{m\times n}$ et $\mathbf{B}\in\mathbb{R}^{n\times k}$, on a, d’après [(10.1)](#gl-10-1) et [(9.1)](das-matrixprodukt.html#gl-9-1),

$$\bigl((\mathbf{A}\mathbf{B})^{\top}\bigr)_{li}=(\mathbf{A}\mathbf{B})_{il}=\sum_{j=1}^na_{ij}\,b_{jl}=\sum_{j=1}^n(\mathbf{B}^{\top})_{lj}\,(\mathbf{A}^{\top})_{ji}=(\mathbf{B}^{\top}\mathbf{A}^{\top})_{li} .$$

Les trois premières règles découlent directement de la définition.
:::

::::beispiel [Exemple de calcul]
$$\begin{pmatrix}1&2&3\\4&5&6\end{pmatrix}^{\top}=\begin{pmatrix}1&4\\2&5\\3&6\end{pmatrix}.$$

Pour $\mathbf{C}=\bigl(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr)$ et $\mathbf{D}=\bigl(\begin{smallmatrix}0&1\\1&1\end{smallmatrix}\bigr)$, on a $\mathbf{C}\mathbf{D}=\bigl(\begin{smallmatrix}2&3\\4&7\end{smallmatrix}\bigr)$, donc $(\mathbf{C}\mathbf{D})^{\top}=\bigl(\begin{smallmatrix}2&4\\3&7\end{smallmatrix}\bigr)$. On obtient la même chose avec $\mathbf{D}^{\top}\mathbf{C}^{\top}=\bigl(\begin{smallmatrix}0&1\\1&1\end{smallmatrix}\bigr)\bigl(\begin{smallmatrix}1&3\\2&4\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}2&4\\3&7\end{smallmatrix}\bigr)$, tandis que $\mathbf{C}^{\top}\mathbf{D}^{\top}=\bigl(\begin{smallmatrix}3&4\\4&6\end{smallmatrix}\bigr)$ est autre chose.
::::

⁠**En bref :** Transposer échange lignes et colonnes ; pour un produit, l’ordre s’inverse, $(\mathbf{A}\mathbf{B})^{\top}=\mathbf{B}^{\top}\mathbf{A}^{\top}$.

:::hintergrund Pourquoi l’ordre s’inverse quand on transpose un produit
Dans le produit $\mathbf{A}\mathbf{B}$, les lignes de $\mathbf{A}$ rencontrent les colonnes de $\mathbf{B}$. Après transposition, les lignes de $\mathbf{A}$ sont les colonnes de $\mathbf{A}^{\top}$, et les colonnes de $\mathbf{B}$ sont les lignes de $\mathbf{B}^{\top}$. Pour que des lignes rencontrent de nouveau des colonnes, $\mathbf{B}^{\top}$ doit se trouver à gauche. Les tailles le montrent aussi : $(\mathbf{A}\mathbf{B})^{\top}$ est de taille $k\times m$, et $\mathbf{B}^{\top}\mathbf{A}^{\top}$ est $(k\times n)\cdot(n\times m)$, donc compatible. L’expression $\mathbf{A}^{\top}\mathbf{B}^{\top}$ serait $(n\times m)\cdot(k\times n)$ et n’est définie que si, par hasard, $m=k$. Un cas particulier de la règle est $\mathbf{u}^{\top}\mathbf{v}=\mathbf{v}^{\top}\mathbf{u}$ : un nombre est sa propre transposée, donc $\mathbf{u}^{\top}\mathbf{v}=(\mathbf{u}^{\top}\mathbf{v})^{\top}=\mathbf{v}^{\top}\mathbf{u}$.
:::

### Matrices symétriques

<span class="anker" id="stufe-10-2"></span>

Certains tableaux restent identiques lorsqu’on les réfléchit par rapport à leur diagonale. Un tableau des distances entre villes en est un : le trajet de Munich à Cologne est aussi long que celui de Cologne à Munich.

:::definition Définition 10.3 (Matrice symétrique)
<span class="anker" id="satz-10-3"></span>

Une matrice carrée $\mathbf{A}$ est dite __symétrique__ si $\mathbf{A}^{\top}=\mathbf{A}$, c’est-à-dire $a_{ij}=a_{ji}$ pour tous $i,j$.
:::

Toute matrice diagonale est symétrique. Une source importante de matrices symétriques est le produit d’une matrice par sa propre transposée : pour toute matrice $\mathbf{A}$, on a

<span class="anker" id="gl-10-2"></span>
$$(\mathbf{A}^{\top}\mathbf{A})^{\top}=\mathbf{A}^{\top}(\mathbf{A}^{\top})^{\top}=\mathbf{A}^{\top}\mathbf{A} , \tag{10.2}$$

donc $\mathbf{A}^{\top}\mathbf{A}$ est symétrique, de même que $\mathbf{A}\mathbf{A}^{\top}$.

::::beispiel [Exemple de calcul]
$\bigl(\begin{smallmatrix}2&1\\1&3\end{smallmatrix}\bigr)$ est symétrique, la rotation $\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)$ ne l’est pas. Pour $\mathbf{C}=\bigl(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr)$, on a

$$\mathbf{C}^{\top}\mathbf{C}=\begin{pmatrix}1&3\\2&4\end{pmatrix}\begin{pmatrix}1&2\\3&4\end{pmatrix}=\begin{pmatrix}10&14\\14&20\end{pmatrix},$$

qui est bien symétrique, comme l’exige [(10.2)](#gl-10-2).
::::

⁠**En bref :** Une matrice symétrique est égale à sa transposée ; $\mathbf{A}^{\top}\mathbf{A}$ et $\mathbf{A}\mathbf{A}^{\top}$ sont toujours symétriques.

:::hintergrund Produits scalaires pondérés
Dans le produit scalaire $\mathbf{u}^{\top}\mathbf{v}=\sum_ju_jv_j$, chaque position compte autant. Si l’on veut compter les positions avec des poids différents, on prend des poids positifs $d_1,\dots,d_n$ et l’on forme $\sum_jd_j\,u_jv_j$. Avec la matrice diagonale $\mathbf{D}=\operatorname{diag}(d_1,\dots,d_n)$, cela s’écrit $\mathbf{u}^{\top}\mathbf{D}\mathbf{v}$, car $\mathbf{D}\mathbf{v}=(d_1v_1,\dots,d_nv_n)^{\top}$.

Ce nombre obéit aux mêmes règles de calcul que le produit scalaire ordinaire. Il est linéaire par rapport à chacun des deux vecteurs, et $\mathbf{u}^{\top}\mathbf{D}\mathbf{u}=\sum_jd_ju_j^2$ est positif pour tout $\mathbf{u}\ne\mathbf{0}$. Il est symétrique parce que $\mathbf{D}$ est symétrique : un nombre est sa propre transposée, et avec la règle de la transposée d’un produit, appliquée deux fois, on a $\mathbf{u}^{\top}\mathbf{D}\mathbf{v}=(\mathbf{u}^{\top}\mathbf{D}\mathbf{v})^{\top}=\mathbf{v}^{\top}\mathbf{D}^{\top}\mathbf{u}=\mathbf{v}^{\top}\mathbf{D}\mathbf{u}$. Comme la preuve de l’inégalité de Cauchy-Schwarz n’a utilisé que ces règles, on peut tout aussi bien mesurer avec $\mathbf{u}^{\top}\mathbf{D}\mathbf{v}$ des longueurs, des distances et des angles. Ils ont simplement d’autres valeurs. Par exemple, $(1,\,1)^{\top}$ et $(-1,\,1)^{\top}$ sont orthogonaux au sens ordinaire, mais pas avec $\mathbf{D}=\operatorname{diag}(2,\,1)$ : $(1,\,1)\,\mathbf{D}\,(-1,\,1)^{\top}=2\cdot1\cdot(-1)+1\cdot1\cdot1=-1$.

La standardisation de la sous-section [4.5](abstande-und-einheiten.html#stufe-4-5) est exactement une telle pondération. La distance entre deux exemples standardisés est $\sqrt{(\mathbf{x}_a-\mathbf{x}_b)^{\top}\mathbf{D}\,(\mathbf{x}_a-\mathbf{x}_b)}$ avec $\mathbf{D}=\operatorname{diag}(1/s_1^2,\dots,1/s_d^2)$. Inversement, toute pondération de ce type agit comme un changement d’unités : si l’on multiplie la caractéristique $j$ par $\sqrt{d_j}$, le produit scalaire ordinaire des vecteurs convertis vaut $\sum_j(\sqrt{d_j}\,u_j)(\sqrt{d_j}\,v_j)=\mathbf{u}^{\top}\mathbf{D}\mathbf{v}$. Le choix des unités et le choix des poids dans $\mathbf{D}$ sont donc une seule et même décision.
:::

### La matrice de Gram des exemples

<span class="anker" id="stufe-10-3"></span>

À quel point chaque exemple d’un jeu de données ressemble-t-il à chacun des autres ? On peut écrire tous les produits scalaires deux à deux dans un tableau : la ligne $i$, colonne $k$ contient $\mathbf{x}_i^{\top}\mathbf{x}_k$. Ce tableau est un seul produit matriciel.

:::definition Définition 10.4 (Matrice de Gram)
<span class="anker" id="satz-10-4"></span>

La __matrice de Gram__ d’une liste de vecteurs $\mathbf{v}_1,\dots,\mathbf{v}_k$ est la matrice $k\times k$ des produits scalaires deux à deux, avec le coefficient $\mathbf{v}_i^{\top}\mathbf{v}_l$ à la ligne $i$ et à la colonne $l$.
:::

Pour les exemples d’un jeu de données, c’est la matrice $\mathbf{X}\mathbf{X}^{\top}\in\mathbb{R}^{N\times N}$. En effet, son coefficient $(i,k)$ est la ligne $i$ de $\mathbf{X}$ fois la colonne $k$ de $\mathbf{X}^{\top}$, c’est-à-dire $\mathbf{x}_i^{\top}\mathbf{x}_k$ :

<span class="anker" id="gl-10-3"></span>
$$(\mathbf{X}\mathbf{X}^{\top})_{ik}=\mathbf{x}_i^{\top}\mathbf{x}_k . \tag{10.3}$$

Elle est symétrique, sa diagonale contient les carrés des longueurs $\lVert\mathbf{x}_i\rVert^2$, et, d’après [(4.1)](abstande-und-einheiten.html#gl-4-1), on peut y lire toutes les distances :

<span class="anker" id="gl-10-4"></span>
$$\lVert\mathbf{x}_i-\mathbf{x}_k\rVert^2=(\mathbf{X}\mathbf{X}^{\top})_{ii}+(\mathbf{X}\mathbf{X}^{\top})_{kk}-2\,(\mathbf{X}\mathbf{X}^{\top})_{ik} . \tag{10.4}$$

Si l’on divise le coefficient $(i,k)$ par $\sqrt{(\mathbf{X}\mathbf{X}^{\top})_{ii}\,(\mathbf{X}\mathbf{X}^{\top})_{kk}}$, on obtient la similarité cosinus de $\mathbf{x}_i$ et $\mathbf{x}_k$.

::::beispiel [Exemple de calcul]
Pour les trois textes de la sous-section [5.4](winkel-und-ahnlichkeit.html#stufe-5-4), on a

$$\mathbf{X}=\begin{pmatrix}3&2&0\\6&4&0\\0&1&3\end{pmatrix},\qquad \mathbf{X}\mathbf{X}^{\top}=\begin{pmatrix}13&26&2\\26&52&4\\2&4&10\end{pmatrix}.$$

D’après [(10.4)](#gl-10-4), la distance entre le texte 1 et le texte 3 vaut $\sqrt{13+10-2\cdot2}=\sqrt{19}$, comme calculé précédemment. La similarité cosinus du texte 1 et du texte 2 vaut $26/\sqrt{13\cdot52}=1$.
::::

⁠**En bref :** La matrice de Gram $\mathbf{X}\mathbf{X}^{\top}$ est le tableau de tous les produits scalaires deux à deux des exemples ; on en déduit toutes les longueurs, distances et angles.

:::hintergrund La matrice de Gram contient toute la géométrie du jeu de données
Les longueurs, les distances et les angles entre les exemples ne dépendent que des produits scalaires, et non des coordonnées individuelles. Si l’on fait tourner tout le jeu de données autour de l’origine, par exemple, toutes les coordonnées changent, mais aucun produit scalaire, et la matrice de Gram reste la même. Deux jeux de données ayant la même matrice de Gram ont donc géométriquement le même aspect. Qui veut seulement savoir quels exemples se ressemblent n’a donc pas besoin de la matrice de données elle-même, mais seulement de sa matrice de Gram.
:::

### La matrice de Gram des caractéristiques

<span class="anker" id="stufe-10-4"></span>

Si l’on inverse les rôles, on obtient un tableau portant sur les caractéristiques : à quel point deux caractéristiques vont-elles de pair sur l’ensemble des exemples ? Les colonnes de ces caractéristiques sont des vecteurs de $\mathbb{R}^N$, et leur produit scalaire le mesure. Cette matrice de Gram des colonnes est $\mathbf{X}^{\top}\mathbf{X}\in\mathbb{R}^{d\times d}$ :

<span class="anker" id="gl-10-5"></span>
$$(\mathbf{X}^{\top}\mathbf{X})_{jl}=\sum_{i=1}^Nx_{ij}\,x_{il} . \tag{10.5}$$

Le coefficient $(j,l)$ est le produit scalaire des colonnes des caractéristiques $j$ et $l$ ; la diagonale contient la somme des carrés de chaque caractéristique.

:::satz Théorème 10.5 (La matrice de Gram comme somme sur les exemples)
<span class="anker" id="satz-10-5"></span>

<span class="anker" id="gl-10-6"></span>
$$\mathbf{X}^{\top}\mathbf{X}=\sum_{i=1}^N\mathbf{x}_i\,\mathbf{x}_i^{\top} . \tag{10.6}$$

Chaque exemple apporte son propre produit extérieur.
:::

Le coefficient $(j,l)$ du membre de droite est $\sum_ix_{ij}\,x_{il}$, le même que dans [(10.5)](#gl-10-5). Si un nouvel exemple s’ajoute, $\mathbf{X}^{\top}\mathbf{X}$ ne change donc que d’une couche supplémentaire $\mathbf{x}_{N+1}\mathbf{x}_{N+1}^{\top}$ ; il n’est pas nécessaire de tout recalculer.

::::beispiel [Exemple de calcul]
Pour les textes, on a

$$\mathbf{X}^{\top}\mathbf{X}=\begin{pmatrix}45&30&0\\30&21&3\\0&3&9\end{pmatrix}.$$

Les coefficients de la première ligne sont les produits scalaires de la colonne « but » avec les trois colonnes des caractéristiques (Fig. [37](#abb-37)).

:::abbildung ml/k1rgrammerk 37
La première ligne de la matrice de Gram des caractéristiques : la colonne « but » $(3,\,6,\,0)^{\top}$ fois elle-même, fois la colonne « ballon » $(2,\,4,\,1)^{\top}$ et fois la colonne « élection » $(0,\,0,\,3)^{\top}$.
:::

Le $0$ à la position $(1,3)$ indique que les mots « but » et « élection » n’apparaissent ensemble dans aucun texte. Comme somme des trois produits extérieurs :

$$\begin{pmatrix}9&6&0\\6&4&0\\0&0&0\end{pmatrix}+\begin{pmatrix}36&24&0\\24&16&0\\0&0&0\end{pmatrix}+\begin{pmatrix}0&0&0\\0&1&3\\0&3&9\end{pmatrix}=\begin{pmatrix}45&30&0\\30&21&3\\0&3&9\end{pmatrix}.$$
::::

⁠**En bref :** $\mathbf{X}^{\top}\mathbf{X}$ est la matrice de Gram des colonnes des caractéristiques ; c’est la somme des produits extérieurs $\mathbf{x}_i\mathbf{x}_i^{\top}$ de tous les exemples.

:::aufgabe Exercice 24 ★ Transposer
<span class="anker" id="aufg-24"></span>

<ol class="al">

<li>

Donnez $\mathbf{B}^{\top}$ pour $\mathbf{B}=\bigl(\begin{smallmatrix}1&0&2\\2&1&0\end{smallmatrix}\bigr)$ et calculez $\mathbf{B}^{\top}\mathbf{B}$ et $\mathbf{B}\mathbf{B}^{\top}$. Quelles sont leurs tailles, et sont-elles symétriques ?

</li>

<li>

Montrez à l’aide des règles de calcul que $(\mathbf{A}\mathbf{B}\mathbf{C})^{\top}=\mathbf{C}^{\top}\mathbf{B}^{\top}\mathbf{A}^{\top}$.

</li>

</ol>

:::loesung
(a) $\mathbf{B}^{\top}=\Bigl(\begin{smallmatrix}1&2\\0&1\\2&0\end{smallmatrix}\Bigr)$. On a alors

$$\mathbf{B}^{\top}\mathbf{B}=\begin{pmatrix}5&2&2\\2&1&0\\2&0&4\end{pmatrix}\in\mathbb{R}^{3\times3},\qquad \mathbf{B}\mathbf{B}^{\top}=\begin{pmatrix}5&2\\2&5\end{pmatrix}\in\mathbb{R}^{2\times2}.$$

Les deux sont symétriques, comme l’exige [(10.2)](#gl-10-2). Le coefficient $(1,1)$ de $\mathbf{B}^{\top}\mathbf{B}$ vaut $1^2+2^2=5$, la somme des carrés de la première colonne ; le coefficient $(1,2)$ de $\mathbf{B}\mathbf{B}^{\top}$ vaut $1\cdot2+0\cdot1+2\cdot0=2$, le produit scalaire des deux lignes.

(b) En appliquant deux fois la règle de la transposée d’un produit : $(\mathbf{A}\mathbf{B}\mathbf{C})^{\top}=\bigl((\mathbf{A}\mathbf{B})\mathbf{C}\bigr)^{\top}=\mathbf{C}^{\top}(\mathbf{A}\mathbf{B})^{\top}=\mathbf{C}^{\top}\mathbf{B}^{\top}\mathbf{A}^{\top}$.
:::
:::

:::aufgabe Exercice 25 ★★ Matrices de Gram d’un petit jeu de données
<span class="anker" id="aufg-25"></span>

Un jeu de données comporte trois exemples à deux caractéristiques : $\mathbf{x}_1=(1,\,0)^{\top}$, $\mathbf{x}_2=(2,\,1)^{\top}$, $\mathbf{x}_3=(0,\,3)^{\top}$.

<ol class="al">

<li>

Écrivez $\mathbf{X}$ et calculez $\mathbf{X}\mathbf{X}^{\top}$ et $\mathbf{X}^{\top}\mathbf{X}$.

</li>

<li>

Lisez dans $\mathbf{X}\mathbf{X}^{\top}$ la distance entre $\mathbf{x}_2$ et $\mathbf{x}_3$ et vérifiez-la directement.

</li>

<li>

Confirmez [(10.6)](#gl-10-6) en additionnant les trois produits extérieurs $\mathbf{x}_i\mathbf{x}_i^{\top}$.

</li>

</ol>

:::loesung
(a) $\mathbf{X}=\Bigl(\begin{smallmatrix}1&0\\2&1\\0&3\end{smallmatrix}\Bigr)$,

$$\mathbf{X}\mathbf{X}^{\top}=\begin{pmatrix}1&2&0\\2&5&3\\0&3&9\end{pmatrix},\qquad \mathbf{X}^{\top}\mathbf{X}=\begin{pmatrix}5&2\\2&10\end{pmatrix}.$$

(b) D’après [(10.4)](#gl-10-4), $\lVert\mathbf{x}_2-\mathbf{x}_3\rVert^2=5+9-2\cdot3=8$, donc la distance vaut $\sqrt8\approx2{,}83$. Directement : $\mathbf{x}_2-\mathbf{x}_3=(2,\,-2)^{\top}$, dont le carré de la longueur vaut $4+4=8$.

(c) $\mathbf{x}_1\mathbf{x}_1^{\top}=\bigl(\begin{smallmatrix}1&0\\0&0\end{smallmatrix}\bigr)$, $\mathbf{x}_2\mathbf{x}_2^{\top}=\bigl(\begin{smallmatrix}4&2\\2&1\end{smallmatrix}\bigr)$, $\mathbf{x}_3\mathbf{x}_3^{\top}=\bigl(\begin{smallmatrix}0&0\\0&9\end{smallmatrix}\bigr)$ ; la somme est $\bigl(\begin{smallmatrix}5&2\\2&10\end{smallmatrix}\bigr)=\mathbf{X}^{\top}\mathbf{X}$.
:::
:::

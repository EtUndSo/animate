---
title: Calcul terme à terme et tenseurs
pfad: Informatique / Apprentissage automatique / Fondements mathématiques / Vecteurs et matrices
knoten: Fondements 1 : Vecteurs et matrices
nachschlagen: ja
order: 15211600
summary: Tout calcul avec des vecteurs et des matrices n’est pas un produit matriciel.
tags: produit de Hadamard, terme à terme, tenseur, axe, forme
lang: fr
---

<span class="anker" id="stufe-15"></span>

:::zweck
Tout calcul avec des vecteurs et des matrices n’est pas un produit matriciel. Cette section présente les calculs qui opèrent coefficient par coefficient et étend les vecteurs et les matrices à des tableaux de nombres à plus de deux indices, tels qu’on en a besoin pour les images.
:::

### Le produit de Hadamard

<span class="anker" id="stufe-15-1"></span>

Un commerçant dispose de la liste des quantités vendues et de la liste des prix unitaires. Pour chaque article, il veut le chiffre d’affaires, c’est-à-dire la quantité fois le prix, mais pas encore la somme. C’est un produit coefficient par coefficient.

:::definition Définition 15.1 (Produit de Hadamard)
<span class="anker" id="satz-15-1"></span>

Pour deux vecteurs ou deux matrices de même taille, le __produit de Hadamard__ $\mathbf{A}\odot\mathbf{B}$ est le produit coefficient par coefficient :

<span class="anker" id="gl-15-1"></span>
$$(\mathbf{A}\odot\mathbf{B})_{ij}=a_{ij}\,b_{ij} . \tag{15.1}$$
:::

Le produit de Hadamard n’est *pas* le produit matriciel. Le produit matriciel forme des produits scalaires de lignes et de colonnes ; le produit de Hadamard ne multiplie que des coefficients situés à la même position. Deux liens avec ce que l’on connaît déjà : si l’on additionne les composantes du produit de Hadamard de deux vecteurs, on obtient leur produit scalaire, $\mathbf 1^{\top}(\mathbf{u}\odot\mathbf{v})=\mathbf{u}^{\top}\mathbf{v}$. Et le produit de Hadamard par un vecteur fixe est la multiplication par une matrice diagonale : $\mathbf{v}\odot\mathbf{x}=\operatorname{diag}(\mathbf{v})\,\mathbf{x}$.

::::beispiel [Exemple de calcul]
$(1,\,2,\,3)^{\top}\odot(4,\,5,\,6)^{\top}=(4,\,10,\,18)^{\top}$, et $4+10+18=32$ est le produit scalaire. Pour les matrices, on a

$$\begin{pmatrix}1&2\\3&4\end{pmatrix}\odot\begin{pmatrix}0&1\\1&0\end{pmatrix}=\begin{pmatrix}0&2\\3&0\end{pmatrix},\qquad\text{mais}\qquad \begin{pmatrix}1&2\\3&4\end{pmatrix}\begin{pmatrix}0&1\\1&0\end{pmatrix}=\begin{pmatrix}2&1\\4&3\end{pmatrix}.$$

Avec un vecteur de zéros et de uns, on peut masquer des caractéristiques : $(1,\,0,\,1)^{\top}\odot\mathbf{x}_1=(60,\,0,\,3)^{\top}$ supprime le nombre de pièces de l’appartement 1.
::::

⁠**En bref :** Le produit de Hadamard $\odot$ multiplie coefficient par coefficient ; ce n’est pas le produit matriciel.

### Fonctions terme à terme

<span class="anker" id="stufe-15-2"></span>

Souvent, on applique la même fonction à chaque coefficient d’un vecteur : on élève toutes les erreurs au carré, on prend la valeur absolue de chacune ou l’on arrondit toutes les valeurs.

:::definition Définition 15.2 (Fonction terme à terme)
<span class="anker" id="satz-15-2"></span>

Pour une fonction $f\colon\mathbb{R}\to\mathbb{R}$ et un vecteur $\mathbf{x}\in\mathbb{R}^d$, $f$ appliquée __terme à terme__ est le vecteur $\bigl(f(x_1),\dots,f(x_d)\bigr)^{\top}$. Pour les matrices, il en va de même, coefficient par coefficient.
:::

De nombreuses normes peuvent s’écrire ainsi : la norme 1 est la somme des valeurs absolues prises terme à terme, $\lVert\mathbf{x}\rVert_1=\mathbf 1^{\top}|\mathbf{x}|$, et le carré de la norme euclidienne la somme des carrés pris terme à terme. Une fonction appliquée terme à terme n’est en général pas linéaire : l’élévation au carré terme à terme transforme $2\mathbf{x}$ en le vecteur de coefficients $4x_j^2$, et non $2x_j^2$.

::::beispiel [Exemple de calcul]
Le vecteur d’erreur de l’agente immobilière était $(-12,\,-4,\,-4,\,-8)^{\top}$. Les valeurs absolues terme à terme donnent $(12,\,4,\,4,\,8)^{\top}$, de somme $28$, la norme 1. Pour l’expert A de la sous-section [3.5](normen-die-groe-eines-vektors.html#stufe-3-5), les carrés terme à terme donnent $(100,\,100,\,100,\,100)^{\top}$, de somme $400=20^2$.
::::

⁠**En bref :** Une fonction appliquée terme à terme agit sur chaque coefficient séparément ; elle n’est en général pas linéaire.

### Ajouter un vecteur à chaque ligne

<span class="anker" id="stufe-15-3"></span>

Pour centrer un jeu de données entier, on soustrait de chaque ligne de la matrice de données le même vecteur, la moyenne des exemples. De même, la prédiction affine ajoute à chaque composante la même ordonnée à l’origine. Pour de tels calculs, il faut une notation.

La moyenne des exemples est fournie par un produit matrice-vecteur : $\bar{\mathbf{x}}=\frac1N\mathbf{X}^{\top}\mathbf 1$, car sa composante $j$ est $\frac1N\sum_ix_{ij}$, la moyenne de la colonne $j$. La matrice dont toutes les lignes sont égales à $\bar{\mathbf{x}}^{\top}$ est le produit extérieur $\mathbf 1\,\bar{\mathbf{x}}^{\top}$. La matrice de données centrée s’écrit donc

<span class="anker" id="gl-15-2"></span>
$$\tilde{\mathbf{X}}=\mathbf{X}-\mathbf 1\,\bar{\mathbf{x}}^{\top} , \tag{15.2}$$

et sa ligne $i$ est le vecteur $(\mathbf{x}_i-\bar{\mathbf{x}})^{\top}$. Beaucoup de textes écrivent pour cela, en abrégé, $\mathbf{X}-\bar{\mathbf{x}}^{\top}$, et entendent par là : soustraire le vecteur ligne de chaque ligne. À strictement parler, la différence d’une matrice $N\times d$ et d’une matrice $1\times d$ n’est pas définie ; l’écriture abrégée désigne toujours [(15.2)](#gl-15-2).

::::beispiel [Exemple de calcul]
Pour les appartements, $\bar{\mathbf{x}}=\tfrac14\mathbf{X}^{\top}\mathbf 1=(65;\ 2{,}5;\ 3)^{\top}$ et

$$\tilde{\mathbf{X}}=\begin{pmatrix}60&2&3\\40&1&1\\90&4&6\\70&3&2\end{pmatrix}-\begin{pmatrix}65&2{,}5&3\\65&2{,}5&3\\65&2{,}5&3\\65&2{,}5&3\end{pmatrix}=\begin{pmatrix}-5&-0{,}5&0\\-25&-1{,}5&-2\\25&1{,}5&3\\5&0{,}5&-1\end{pmatrix}.$$

Chaque colonne est la colonne de la caractéristique correspondante, centrée comme dans la sous-section [4.3](abstande-und-einheiten.html#stufe-4-3), et sa somme est nulle.
::::

⁠**En bref :** Ajouter un vecteur $\mathbf{q}$ à chaque ligne d’une matrice $\mathbf{A}$ s’écrit $\mathbf{A}+\mathbf 1\,\mathbf{q}^{\top}$ ; l’abréviation répandue $\mathbf{A}+\mathbf{q}^{\top}$ signifie exactement cela.

### Tenseurs

<span class="anker" id="stufe-15-4"></span>

Un scalaire est un nombre isolé, un vecteur une liste à un indice, une matrice un tableau à deux indices. Une image couleur en demande trois : ligne, colonne et canal de couleur. Une pile d’images couleur en demande quatre. On réunit tous ces tableaux de nombres sous un même nom.

:::definition Définition 15.3 (Tenseur, forme)
<span class="anker" id="satz-15-3"></span>

En apprentissage automatique, un __tenseur__ est un tableau de nombres dont les coefficients sont numérotés par $k$ indices. Chaque indice court le long d’un __axe__. La liste des longueurs des axes s’appelle la __forme__ du tenseur.
:::

Un scalaire est un tenseur à $0$ axe, un vecteur de $\mathbb{R}^d$ un tenseur à un axe de longueur $d$, une matrice de $\mathbb{R}^{m\times n}$ un tenseur de forme $m\times n$. Un tenseur de forme $n_1\times n_2\times\dots\times n_k$ a $n_1\cdot n_2\cdots n_k$ coefficients. La figure [42](#abb-42) montre les premiers niveaux.

:::abbildung ml/k1tensor 42
Tenseurs de $0$ à $4$ axes : un scalaire, un vecteur à $4$ coefficients, une matrice $4\times4$ (par exemple une image en niveaux de gris), une image couleur formée de trois canaux $4\times4$ pour le rouge, le vert et le bleu, et une pile de $N$ telles images couleur (suggérée par trois images).
:::

::::beispiel [Exemple de calcul]
Une image couleur de $4\times4$ pixels à trois canaux de couleur est un tenseur de forme $3\times4\times4$ à $48$ coefficients. Le coefficient d’indices $(1,2,3)$ est la luminosité du premier canal, donc du rouge, au pixel situé à la ligne $2$ et à la colonne $3$.
::::

⁠**En bref :** Un tenseur est un tableau de nombres à un nombre quelconque d’axes ; scalaire, vecteur et matrice sont les cas à $0$, $1$ et $2$ axes.

:::hintergrund Le tenseur de la physique est autre chose
En physique et en électrotechnique, un tenseur est plus qu’un tableau de nombres ; c’est le cas, par exemple, du tenseur des contraintes d’un matériau ou du tenseur de permittivité d’un cristal. Là, un tenseur s’accompagne d’une règle indiquant comment ses coefficients changent lorsqu’on fait tourner le système de coordonnées ; les coefficients seuls ne le définissent pas. En apprentissage automatique, cette règle est absente : un tenseur n’y est qu’un tableau multidimensionnel de nombres. Le mot est le même, la notion est différente.
:::

### Les images comme tenseurs

<span class="anker" id="stufe-15-5"></span>

Les données d’images sont l’exemple le plus important de tenseurs à plus de deux axes. Leur forme montre immédiatement combien de nombres un jeu de données contient.

Une image en niveaux de gris de $28\times28$ pixels est une matrice, donc un tenseur de forme $28\times28$ à $784$ coefficients. Une image couleur de $32\times32$ pixels a trois canaux et la forme $3\times32\times32$, soit $3072$ coefficients. Une pile de $100$ telles images couleur a la forme $100\times3\times32\times32$ et $307\,200$ coefficients. Le premier axe compte alors les exemples, exactement comme les lignes de la matrice de données : la matrice de données est le cas particulier d’une pile de vecteurs, de forme $N\times d$.

L’ordre des axes est une convention. Certains programmes placent le canal de couleur au début ($3\times32\times32$), d’autres à la fin ($32\times32\times3$). Les nombres sont les mêmes, seule leur disposition diffère, et avant tout calcul, il doit être clair quel axe signifie quoi.

::::beispiel [Exemple de calcul]
Un jeu de données de $60\,000$ images en niveaux de gris de $28\times28$ pixels est un tenseur de forme $60\,000\times28\times28$ à $47\,040\,000$ coefficients. Si l’on transforme chaque image en un vecteur de $\mathbb{R}^{784}$, on obtient une matrice de données de $\mathbb{R}^{60\,000\times784}$, avec les mêmes coefficients.
::::

⁠**En bref :** Une image est un tenseur à deux ou trois axes, une pile d’images un tenseur avec un axe de plus ; le premier axe compte les exemples.

:::aufgabe Exercice 36 ★ Terme à terme ou non ?
<span class="anker" id="aufg-36"></span>

<ol class="al">

<li>

Calculez $\mathbf{u}\odot\mathbf{v}$ et $\mathbf{u}^{\top}\mathbf{v}$ pour $\mathbf{u}=(2,\,-1,\,3)^{\top}$ et $\mathbf{v}=(1,\,4,\,2)^{\top}$.

</li>

<li>

Calculez $\bigl(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr)\odot\bigl(\begin{smallmatrix}2&0\\1&3\end{smallmatrix}\bigr)$ et le produit matriciel des mêmes matrices.

</li>

<li>

Quelle est la forme d’une pile de $64$ images couleur de $224\times224$ pixels, avec le canal de couleur en tête, et combien de coefficients a-t-elle ?

</li>

</ol>

:::loesung
(a) $\mathbf{u}\odot\mathbf{v}=(2,\,-4,\,6)^{\top}$ et $\mathbf{u}^{\top}\mathbf{v}=2-4+6=4$, la somme des coefficients du produit de Hadamard.

(b) Produit de Hadamard : $\bigl(\begin{smallmatrix}1\cdot2&2\cdot0\\3\cdot1&4\cdot3\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}2&0\\3&12\end{smallmatrix}\bigr)$. Produit matriciel : $\bigl(\begin{smallmatrix}2+2&0+6\\6+4&0+12\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}4&6\\10&12\end{smallmatrix}\bigr)$. Seul le coefficient en bas à droite coïncide, par hasard.

(c) La forme est $64\times3\times224\times224$, avec $64\cdot3\cdot224\cdot224=9\,633\,792$ coefficients.
:::
:::

:::aufgabe Exercice 37 ★★ Centrer un jeu de données
<span class="anker" id="aufg-37"></span>

<ol class="al">

<li>

Montrez que les colonnes de la matrice de données centrée [(15.2)](#gl-15-2) ont pour somme zéro, c’est-à-dire que $\mathbf 1^{\top}\tilde{\mathbf{X}}=\mathbf{0}^{\top}$. Utilisez $\mathbf 1^{\top}\mathbf 1=N$.

</li>

<li>

Centrez la matrice de données des trois textes de la sous-section [5.4](winkel-und-ahnlichkeit.html#stufe-5-4).

</li>

</ol>

:::loesung
(a) On a $\bar{\mathbf{x}}^{\top}=\frac1N\mathbf 1^{\top}\mathbf{X}$, la transposée de $\bar{\mathbf{x}}=\frac1N\mathbf{X}^{\top}\mathbf 1$. Par conséquent,

$$\mathbf 1^{\top}\tilde{\mathbf{X}}=\mathbf 1^{\top}\mathbf{X}-(\mathbf 1^{\top}\mathbf 1)\,\bar{\mathbf{x}}^{\top}=\mathbf 1^{\top}\mathbf{X}-N\cdot\tfrac1N\,\mathbf 1^{\top}\mathbf{X}=\mathbf{0}^{\top} .$$

Chaque colonne est un vecteur centré, dont les composantes ont pour somme zéro, comme dans la sous-section [4.3](abstande-und-einheiten.html#stufe-4-3).

(b) La moyenne des textes est $\bar{\mathbf{x}}=\tfrac13\bigl((3,2,0)^{\top}+(6,4,0)^{\top}+(0,1,3)^{\top}\bigr)=(3,\,\tfrac73,\,1)^{\top}$. Matrice centrée :

$$\tilde{\mathbf{X}}=\begin{pmatrix}0&-\frac13&-1\\3&\frac53&-1\\-3&-\frac43&2\end{pmatrix}.$$

La somme de chaque colonne est nulle : $0+3-3=0$, $-\tfrac13+\tfrac53-\tfrac43=0$, $-1-1+2=0$.
:::
:::

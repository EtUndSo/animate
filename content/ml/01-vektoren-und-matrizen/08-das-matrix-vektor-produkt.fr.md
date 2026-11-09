---
title: Le produit matrice-vecteur
pfad: Informatique / Apprentissage automatique / Fondements mathématiques / Vecteurs et matrices
knoten: Fondements 1 : Vecteurs et matrices
nachschlagen: ja
order: 15210800
summary: La même somme pondérée doit être calculée pour tous les exemples d’un jeu de données.
tags: produit matrice-vecteur, espace des colonnes
lang: fr
---

<span class="anker" id="stufe-7"></span>

:::zweck
La même somme pondérée doit être calculée pour tous les exemples d’un jeu de données. Cette section introduit pour cela le produit d’une matrice et d’un vecteur et montre les deux façons de le lire : ligne par ligne ou colonne par colonne.
:::

### Matrice fois vecteur

<span class="anker" id="stufe-7-1"></span>

L’agente immobilière de la sous-section [2.2](das-skalarprodukt.html#stufe-2-2) estime chaque appartement avec la même somme pondérée. Pour quatre appartements, elle calcule quatre fois $\mathbf{w}^{\top}\mathbf{x}_i$. Si l’on écrit les appartements comme les lignes d’une matrice, on peut exprimer les quatre calculs en une seule étape : chaque ligne de la matrice est multipliée par le même vecteur.

:::definition Définition 7.1 (Produit matrice-vecteur)
<span class="anker" id="satz-7-1"></span>

Pour $\mathbf{A}\in\mathbb{R}^{m\times n}$ et $\mathbf{x}\in\mathbb{R}^n$, le __produit matrice-vecteur__ $\mathbf{A}\mathbf{x}$ est le vecteur de $\mathbb{R}^m$ de composantes

<span class="anker" id="gl-7-1"></span>
$$(\mathbf{A}\mathbf{x})_i=\sum_{j=1}^{n}a_{ij}\,x_j=a_{i1}x_1+a_{i2}x_2+\dots+a_{in}x_n ,\qquad i=1,\dots,m . \tag{7.1}$$
:::

Le produit n’existe que si $\mathbf{x}$ a autant de composantes que $\mathbf{A}$ a de colonnes. Le résultat a autant de composantes que $\mathbf{A}$ a de lignes. Des règles de calcul des sommes, il découle que $\mathbf{A}(\mathbf{u}+\mathbf{v})=\mathbf{A}\mathbf{u}+\mathbf{A}\mathbf{v}$ et $\mathbf{A}(c\,\mathbf{x})=c\,\mathbf{A}\mathbf{x}$.

⁠**Exemple de calcul :** Pour

$$\mathbf{A}=\begin{pmatrix}1&2\\0&-1\\3&1\end{pmatrix}\quad\text{et}\quad \mathbf{x}=\begin{pmatrix}2\\1\end{pmatrix}\qquad\text{on a}\qquad \mathbf{A}\mathbf{x}=\begin{pmatrix}4\\-1\\7\end{pmatrix}.$$

Chaque composante est une somme selon [(7.1)](#gl-7-1) (Fig. [28](#abb-28)). Une matrice $3\times2$ multipliée par un vecteur à $2$ composantes donne un vecteur à $3$ composantes.

:::abbildung ml/k1rmv 28
Le produit matrice-vecteur composante par composante : pour chaque ligne $i$, les coefficients $a_{ij}$ sont multipliés par les $x_j$ correspondants, puis additionnés.
:::

⁠**En bref :** $\mathbf{A}\mathbf{x}$ est le vecteur dont la composante $i$ est la somme $\sum_ja_{ij}x_j$ ; une matrice $m\times n$ transforme un vecteur de $\mathbb{R}^n$ en un vecteur de $\mathbb{R}^m$.

### La vue par lignes : de nombreux produits scalaires

<span class="anker" id="stufe-7-2"></span>

La formule [(7.1)](#gl-7-1) dit, pour chaque composante : la ligne $i$ de la matrice, multipliée coefficient par coefficient par $\mathbf{x}$, puis sommée. C’est le produit scalaire de la ligne $i$ avec $\mathbf{x}$ (Fig. [30](#abb-30), à gauche).

:::satz Théorème 7.2 (Vue par lignes)
<span class="anker" id="satz-7-2"></span>

La composante $i$ de $\mathbf{A}\mathbf{x}$ est le produit scalaire de la $i$-ième ligne de $\mathbf{A}$ avec $\mathbf{x}$. Pour une matrice de données $\mathbf{X}$ de lignes $\mathbf{x}_i^{\top}$ et un vecteur de poids $\mathbf{w}$, cela signifie

<span class="anker" id="gl-7-2"></span>
$$\mathbf{X}\mathbf{w}=\begin{pmatrix}\mathbf{x}_1^{\top}\mathbf{w}\\\vdots\\\mathbf{x}_N^{\top}\mathbf{w}\end{pmatrix}. \tag{7.2}$$
:::

Le produit matrice-vecteur applique donc la somme pondérée de poids $\mathbf{w}$ à tous les exemples à la fois et fournit le vecteur de toutes les prédictions. Dans l’image de la comparaison avec un motif : chaque exemple est comparé au même motif $\mathbf{w}$.

⁠**Exemple de calcul :** Pour le jeu de données des appartements et $\mathbf{w}=(3,\,10,\,-4)^{\top}$, on a

$$\hat{\mathbf{y}}=\mathbf{X}\mathbf{w}=\begin{pmatrix}60&2&3\\40&1&1\\90&4&6\\70&3&2\end{pmatrix}\begin{pmatrix}3\\10\\-4\end{pmatrix}=\begin{pmatrix}188\\126\\286\\232\end{pmatrix},$$

les quatre prédictions de l’agente immobilière en milliers d’euros. Chaque composante est le produit scalaire d’une ligne avec $\mathbf{w}$ (Fig. [29](#abb-29)).

:::abbildung ml/k1rzeilen 29
La vue par lignes pour l’agente immobilière : chaque appartement, c’est-à-dire chaque ligne de $\mathbf{X}$, fois les poids $\mathbf{w}$.
:::

⁠**En bref :** Dans la vue par lignes, $\mathbf{A}\mathbf{x}$ est une liste de produits scalaires, un par ligne ; $\mathbf{X}\mathbf{w}$ donne les prédictions pour tous les exemples.

:::hintergrund Combien de travail de calcul coûte un produit matrice-vecteur
Chacune des $m$ composantes demande $n$ multiplications et $n-1$ additions. Au total, cela fait $m(2n-1)$, soit environ $2mn$ opérations élémentaires. Pour les quatre appartements à trois caractéristiques, il y en a $4\cdot5=20$. Pour un jeu de données d’un million d’exemples à cent caractéristiques, il y en a environ $2\cdot10^8$. Un processeur actuel exécute plusieurs milliards de ces opérations par seconde ; un seul produit matrice-vecteur de cette taille est donc vite effectué. De tels décomptes ne donnent cependant que l’ordre de grandeur du temps de calcul, car la vitesse réelle d’un ordinateur dépend aussi de la vitesse à laquelle il peut aller chercher les nombres en mémoire.
:::

### La vue par colonnes : une combinaison linéaire des colonnes

<span class="anker" id="stufe-7-3"></span>

On peut aussi ordonner autrement la même somme. Au lieu de procéder ligne par ligne, on rassemble toutes les contributions qui appartiennent à $x_1$, puis toutes celles qui appartiennent à $x_2$, et ainsi de suite. Les contributions de $x_j$ se trouvent toutes dans la colonne $j$ de la matrice. Le produit devient alors une combinaison linéaire des colonnes (Fig. [30](#abb-30), à droite).

:::abbildung ml/k1zeilenspalten 30
Deux façons de lire $\mathbf{A}\mathbf{x}$ pour $\mathbf{A}=\bigl(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\bigr)$ et $\mathbf{x}=(2,\,1)^{\top}$. À gauche, la vue par lignes : la composante $1$ du résultat est le produit scalaire de la première ligne avec $\mathbf{x}$. À droite, la vue par colonnes : $\mathbf{A}\mathbf{x}$ vaut $2$ fois la première colonne $\mathbf{a}_1=(2,1)^{\top}$ plus $1$ fois la deuxième colonne $\mathbf{a}_2=(1,1)^{\top}$.
:::

:::satz Théorème 7.3 (Vue par colonnes)
<span class="anker" id="satz-7-3"></span>

Si $\mathbf{a}_1,\dots,\mathbf{a}_n$ sont les colonnes de $\mathbf{A}\in\mathbb{R}^{m\times n}$, alors

<span class="anker" id="gl-7-3"></span>
$$\mathbf{A}\mathbf{x}=x_1\mathbf{a}_1+x_2\mathbf{a}_2+\dots+x_n\mathbf{a}_n=\sum_{j=1}^nx_j\,\mathbf{a}_j . \tag{7.3}$$

Le produit matrice-vecteur est la combinaison linéaire des colonnes de $\mathbf{A}$ ayant pour coefficients les composantes de $\mathbf{x}$.
:::

:::beweis Vue par colonnes
La composante $i$ du membre de droite est $\sum_jx_j\,(\mathbf{a}_j)_i=\sum_jx_j\,a_{ij}$, car la $i$-ième composante de la colonne $\mathbf{a}_j$ est le coefficient $a_{ij}$. C’est exactement la composante $i$ de $\mathbf{A}\mathbf{x}$ d’après [(7.1)](#gl-7-1).
:::

⁠**Exemple de calcul 1 :** Pour le produit $\mathbf{A}\mathbf{x}$ de la sous-section [7.1](#stufe-7-1), on a

$$\begin{pmatrix}1&2\\0&-1\\3&1\end{pmatrix}\begin{pmatrix}2\\1\end{pmatrix}=2\begin{pmatrix}1\\0\\3\end{pmatrix}+1\begin{pmatrix}2\\-1\\1\end{pmatrix}=\begin{pmatrix}4\\-1\\7\end{pmatrix}.$$

⁠**Exemple de calcul 2 :** Les prédictions de l’agente immobilière valent $3$ fois la colonne des surfaces plus $10$ fois la colonne des pièces plus $(-4)$ fois la colonne des distances (Fig. [31](#abb-31)). Les colonnes de $\mathbf{X}$ se notent ici, comme dans la sous-section [6.1](matrizen-und-die-datenmatrix.html#stufe-6-1), $\mathbf{a}_1$, $\mathbf{a}_2$, $\mathbf{a}_3$. Sous cette forme, on voit quelle part de chaque prédiction provient de quelle caractéristique : le premier terme contient les contributions de la surface, le deuxième celles des pièces, le troisième celles de la distance.

:::abbildung ml/k1rspalten 31
La vue par colonnes pour l’agente immobilière : chaque colonne $\mathbf{a}_j$ de $\mathbf{X}$ est multipliée par son poids $w_j$, puis les trois vecteurs sont additionnés.
:::

⁠**En bref :** Dans la vue par colonnes, $\mathbf{A}\mathbf{x}$ est une combinaison linéaire des colonnes de $\mathbf{A}$ ; les composantes de $\mathbf{x}$ indiquent combien l’on prend de chaque colonne.

:::hintergrund Pourquoi il y a deux vues sur le même calcul
Les deux vues calculent les mêmes $m\cdot n$ produits $a_{ij}x_j$ et les additionnent. La vue par lignes les regroupe d’abord ligne par ligne, la vue par colonnes d’abord colonne par colonne ; avec un nombre fini de termes, l’ordre est indifférent, comme pour la somme double de la sous-section [1.1](vektoren-daten-als-zahlenlisten.html#stufe-1-1). Mais chaque vue répond à une autre question. La vue par lignes demande : qu’obtient-on dans la composante $i$ ? La vue par colonnes demande : quels résultats la matrice peut-elle fournir, si l’on choisit $\mathbf{x}$ librement ? La seconde question mène directement à la notion suivante.
:::

### L’espace des colonnes

<span class="anker" id="stufe-7-4"></span>

Si l’on fait parcourir à $\mathbf{x}$ tous les vecteurs de $\mathbb{R}^n$, $\mathbf{A}\mathbf{x}$ parcourt, d’après la vue par colonnes, toutes les combinaisons linéaires des colonnes. En général, on n’obtient pas ainsi tous les vecteurs de $\mathbb{R}^m$.

:::definition Définition 7.4 (Espace des colonnes)
<span class="anker" id="satz-7-4"></span>

L’__espace des colonnes__ d’une matrice $\mathbf{A}\in\mathbb{R}^{m\times n}$ est l’ensemble de tous les vecteurs $\mathbf{A}\mathbf{x}$ avec $\mathbf{x}\in\mathbb{R}^n$, c’est-à-dire l’ensemble de toutes les combinaisons linéaires des colonnes de $\mathbf{A}$.
:::

⁠**Exemple de calcul 1 :** La matrice $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ a pour colonnes $(1,\,2)^{\top}$ et $(2,\,4)^{\top}=2\,(1,\,2)^{\top}$. Toute combinaison linéaire est un multiple de $(1,\,2)^{\top}$. L’espace des colonnes n’est donc que la droite passant par l’origine et dirigée par $(1,\,2)^{\top}$, bien que les résultats aient deux composantes. Le vecteur $(3,\,6)^{\top}$ en fait partie, le vecteur $(1,\,1)^{\top}$ non.

⁠**Exemple de calcul 2 :** La matrice $\mathbf{H}=\Bigl(\begin{smallmatrix}1&0\\0&1\\1&1\end{smallmatrix}\Bigr)$ donne $\mathbf{H}\mathbf{x}=(x_1,\,x_2,\,x_1+x_2)^{\top}$. Son espace des colonnes se compose des vecteurs de $\mathbb{R}^3$ dont la troisième composante est la somme des deux premières ; c’est un plan de l’espace. Le vecteur $(1,\,2,\,3)^{\top}=\mathbf{H}\,(1,\,2)^{\top}$ en fait partie, $(1,\,1,\,1)^{\top}$ non, car $1+1\ne1$.

Pour une matrice de données, cela signifie : les prédictions $\mathbf{X}\mathbf{w}$ se trouvent toujours dans l’espace des colonnes de $\mathbf{X}$, quels que soient les poids choisis. Avec ces caractéristiques, on ne peut produire que des listes de prédictions bien déterminées.

⁠**En bref :** L’espace des colonnes d’une matrice est l’ensemble de tous les vecteurs $\mathbf{A}\mathbf{x}$, c’est-à-dire tout ce que l’on peut obtenir par combinaison linéaire de ses colonnes.

:::aufgabe Exercice 16 ★ Deux vues sur un produit
<span class="anker" id="aufg-16"></span>

<ol class="al">

<li>

Calculez $\mathbf{B}\mathbf{x}$ pour $\mathbf{B}=\bigl(\begin{smallmatrix}1&0&2\\2&1&0\end{smallmatrix}\bigr)$ et $\mathbf{x}=(1,\,3,\,-1)^{\top}$, une fois dans la vue par lignes et une fois dans la vue par colonnes.

</li>

<li>

$\mathbf{B}\,(1,\,2)^{\top}$ est-il défini ? Et $\mathbf{B}\,(1,\,2,\,3)^{\top}$ ? Justifiez à l’aide des tailles et indiquez combien de composantes a le résultat lorsqu’il est défini.

</li>

<li>

$(2,\,0,\,2)^{\top}$ appartient-il à l’espace des colonnes de la matrice $\mathbf{H}$ de la sous-section [7.4](#stufe-7-4) ? Et $(2,\,1,\,2)^{\top}$ ?

</li>

</ol>

:::loesung
(a) Vue par lignes : $(1\cdot1+0\cdot3+2\cdot(-1),\ 2\cdot1+1\cdot3+0\cdot(-1))^{\top}=(-1,\,5)^{\top}$. Vue par colonnes : $1\,(1,\,2)^{\top}+3\,(0,\,1)^{\top}-1\,(2,\,0)^{\top}=(1+0-2,\ 2+3-0)^{\top}=(-1,\,5)^{\top}$.

(b) $\mathbf{B}$ a trois colonnes. $\mathbf{B}\,(1,\,2)^{\top}$ n’est pas défini, parce que le vecteur n’a que deux composantes. $\mathbf{B}\,(1,\,2,\,3)^{\top}$ est défini et a autant de composantes que $\mathbf{B}$ a de lignes, à savoir deux : $(1+0+6,\ 2+2+0)^{\top}=(7,\,4)^{\top}$.

(c) L’espace des colonnes de $\mathbf{H}$ se compose des vecteurs dont la troisième composante est la somme des deux premières. Pour $(2,\,0,\,2)^{\top}$, on a $2+0=2$ : oui, c’est $\mathbf{H}\,(2,\,0)^{\top}$. Pour $(2,\,1,\,2)^{\top}$, on a $2+1=3\ne2$ : non.
:::
:::

:::aufgabe Exercice 17 ★★ Le loyer mensuel
<span class="anker" id="aufg-17"></span>

Une grille de référence des loyers estime le loyer mensuel d’un appartement avec les poids $\mathbf{w}_{\mathrm M}=(12,\,30,\,-8)^{\top}$ en euros par mètre carré, par pièce et par kilomètre.

<ol class="al">

<li>

Calculez les loyers estimés des quatre appartements sous la forme $\mathbf{X}\mathbf{w}_{\mathrm M}$, une fois dans la vue par lignes et une fois dans la vue par colonnes.

</li>

<li>

De combien de multiplications et d’additions avez-vous eu besoin ? Combien en faudrait-il pour $10\,000$ appartements à $20$ caractéristiques ?

</li>

</ol>

:::loesung
(a) Vue par lignes, pour l’appartement 1 : $12\cdot60+30\cdot2-8\cdot3=720+60-24=756$, et de même $502$, $1152$ et $914$ euros. Vue par colonnes :

$$12\begin{pmatrix}60\\40\\90\\70\end{pmatrix}+30\begin{pmatrix}2\\1\\4\\3\end{pmatrix}-8\begin{pmatrix}3\\1\\6\\2\end{pmatrix}=\begin{pmatrix}720\\480\\1080\\840\end{pmatrix}+\begin{pmatrix}60\\30\\120\\90\end{pmatrix}-\begin{pmatrix}24\\8\\48\\16\end{pmatrix}=\begin{pmatrix}756\\502\\1152\\914\end{pmatrix}.$$

(b) Chacune des quatre composantes demande $3$ multiplications et $2$ additions, soit au total $12+8=20$. Pour $10\,000$ appartements à $20$ caractéristiques, il faut $10\,000\cdot20=200\,000$ multiplications et $10\,000\cdot19=190\,000$ additions, soit au total $390\,000\approx2mn$ avec $m=10\,000$, $n=20$.
:::
:::

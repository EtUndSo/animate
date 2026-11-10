---
title: Dériver par rapport à des vecteurs et des matrices
pfad: Informatique / Apprentissage automatique / Fondements mathématiques / Dérivée, gradient et règle de dérivation en chaîne
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Chapitre 3 : Dérivée, gradient et règle de dérivation en chaîne
nachschlagen: ja
order: 15230800
summary: On a sans cesse besoin des gradients d’expressions comme a top x , x top Ax ou lVerty-AxrVert 2 .
tags: convention de disposition
lang: fr
---

<span class="anker" id="stufe-7"></span>

:::zweck
On a sans cesse besoin des gradients d’expressions comme $\mathbf{a}^{\top}\mathbf{x}$, $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}$ ou $\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert^2$. Cette section fixe d’abord la forme de chaque dérivée, puis établit les formules les plus importantes composante par composante. Elle se termine par les dérivées par rapport à une matrice et par la règle qui permet de calculer une sensibilité à rebours à travers un produit matriciel.
:::

### La convention de disposition

<span class="anker" id="stufe-7-1"></span>

Pour les fonctions d’une variable, la dérivée est un nombre, et il n’y a rien à ranger. Pour les vecteurs et les matrices, il faut fixer sous quelle forme on écrit les nombreuses dérivées partielles : en colonne ou en ligne, en matrice $m\times n$ ou $n\times m$. Un tel choix s’appelle une __convention de disposition__. Mathématiquement, tous les choix se valent ; il faut seulement s’y tenir, sinon des formules apparaissent soudain transposées.

:::definition Définition 7.1 (Convention de disposition de ce chapitre)
<span class="anker" id="satz-7-1"></span>

<ol class="rm">

<li>

Les vecteurs sont des colonnes. Le gradient d’une fonction $f:\mathbb{R}^n\to\mathbb{R}$ est une colonne de même forme que $\mathbf{x}$.

</li>

<li>

La matrice jacobienne d’une fonction $\mathbf{g}:\mathbb{R}^n\to\mathbb{R}^m$ est une matrice $m\times n$ : une ligne par sortie, une colonne par entrée.

</li>

<li>

La dérivée d’une fonction $f:\mathbb{R}^{m\times n}\to\mathbb{R}$ par rapport à une matrice $\mathbf{A}$ est une matrice $\nabla_{\mathbf{A}}f$ de taille $m\times n$ dont le coefficient en position $(i,j)$ est $\partial f/\partial a_{ij}$ ; elle a donc la même forme que $\mathbf{A}$.

</li>

</ol>
:::

Le tableau [2](#tab-2) résume cela. Le chapitre a déjà utilisé deux conséquences : pour une fonction à une seule sortie, la matrice jacobienne est le gradient écrit en ligne, $\mathbf{J}_f=\nabla f^{\top}$. Et la règle de dérivation en chaîne pour les gradients a besoin de la transposée, $\nabla(f\circ\mathbf{g})=\mathbf{J}_{\mathbf{g}}^{\top}\nabla f$. La règle (iii) servira dans la section [7.5](#stufe-7-5) : qui modifie une matrice d’une petite matrice $\mathbf E$ veut pouvoir comparer $\nabla_{\mathbf{A}}f$ et $\mathbf E$ coefficient par coefficient.

<span class="anker" id="tab-2"></span>

**Tableau 2 :** La forme de la dérivée selon le type de fonction, dans la convention de ce chapitre.

| Fonction | Dérivée | Forme |
|---|---|---|
| $f:\mathbb{R}\to\mathbb{R}$ | $f'(x)$ | nombre |
| $f:\mathbb{R}^n\to\mathbb{R}$ | $\nabla f(\mathbf{x})$ | colonne, $n\times1$ (comme $\mathbf{x}$) |
| $\mathbf{g}:\mathbb{R}^n\to\mathbb{R}^m$ | $\mathbf{J}_{\mathbf{g}}(\mathbf{x})$ | $m\times n$ (la ligne $i$ est $\nabla g_i^{\top}$) |
| $f:\mathbb{R}^{m\times n}\to\mathbb{R}$ | $\nabla_{\mathbf{A}}f(\mathbf{A})$ | $m\times n$ (comme $\mathbf{A}$) |

::::beispiel [Exemple de calcul]
Pour $f(\mathbf{x})=x_1^2x_2+x_2^2$ au point $(1,\,2)$, le gradient est la colonne $\nabla f=(4,\,5)^{\top}$ et la matrice jacobienne la ligne $\mathbf{J}_f=(4\ \ 5)$. Pour $\mathbf{g}$ de [(5.1)](die-jacobi-matrix.html#gl-5-1), $\mathbf{J}_{\mathbf{g}}$ est une matrice $2\times2$ dont la première ligne $(2\ \ 1)$ est le gradient de $g_1=x_1x_2$ écrit en ligne.
::::

⁠**En bref :** Dans ce chapitre, un gradient a la forme de sa variable, et une matrice jacobienne a une ligne par sortie ; il en découle $\mathbf{J}_f=\nabla f^{\top}$ et la transposée dans la règle de dérivation en chaîne pour les gradients.

:::hintergrund D’autres conventions dans la littérature
Beaucoup de livres écrivent le gradient en ligne. Il est alors identique à la matrice jacobienne d’une fonction à une seule sortie, et la règle de dérivation en chaîne se passe entièrement de transposition, car $\nabla(f\circ\mathbf{g})=\nabla f\,\mathbf{J}_{\mathbf{g}}$ est alors le produit d’une ligne par une matrice. Le prix à payer est que le gradient n’a plus la forme de $\mathbf{x}$ ; la droite $\mathbf{x}+t\,\nabla f$ dans la direction de plus forte montée demande alors une transposition. On distingue deux dispositions : dans la disposition numérateur, les lignes correspondent aux composantes de la fonction, comme pour la matrice jacobienne de ce chapitre. Dans la disposition dénominateur, elles correspondent aux composantes de la variable ; la dérivée d’une fonction à valeurs vectorielles est alors la transposée de la matrice jacobienne. Ce chapitre utilise une forme mixte répandue : gradient en colonne et matrice jacobienne en disposition numérateur. On ne doit donc pas combiner sans vérification des formules provenant de sources différentes. Une vérification rapide porte sur la forme : un gradient par rapport à $\mathbf{x}\in\mathbb{R}^n$ doit avoir $n$ coefficients dans une colonne. Une vérification plus fiable est un petit exemple numérique.
:::

### Fonctions linéaires

<span class="anker" id="stufe-7-2"></span>

La fonction de plusieurs variables la plus simple est la somme pondérée. Son gradient est si simple qu’on peut l’écrire immédiatement ; la preuve montre le schéma selon lequel sont obtenues toutes les autres formules de cette section.

:::satz Théorème 7.2 (Gradients de fonctions linéaires)
<span class="anker" id="satz-7-2"></span>

Pour des vecteurs fixes $\mathbf{a},\mathbf{y}$ et une matrice fixe $\mathbf{A}$ de forme adaptée, on a

<span class="anker" id="gl-7-1"></span>
$$\nabla_{\mathbf{x}}(\mathbf{a}^{\top}\mathbf{x})=\nabla_{\mathbf{x}}(\mathbf{x}^{\top}\mathbf{a})=\mathbf{a},\qquad \nabla_{\mathbf{x}}(\mathbf{y}^{\top}\mathbf{A}\mathbf{x})=\mathbf{A}^{\top}\mathbf{y} . \tag{7.1}$$
:::

:::beweis Gradients de fonctions linéaires
On a $\mathbf{a}^{\top}\mathbf{x}=\sum_ja_jx_j$. En dérivant par rapport à $x_k$, seul reste le terme $j=k$, donc $a_k$. Comme $\mathbf{x}^{\top}\mathbf{a}=\mathbf{a}^{\top}\mathbf{x}$, il en va de même pour $\mathbf{x}^{\top}\mathbf{a}$. Pour la seconde partie, on pose $\mathbf{a}=\mathbf{A}^{\top}\mathbf{y}$, car $\mathbf{y}^{\top}\mathbf{A}\mathbf{x}=(\mathbf{A}^{\top}\mathbf{y})^{\top}\mathbf{x}$.
:::

::::beispiel [Exemple de calcul]
Dans le [chapitre 1, section 2.2](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-skalarprodukt.html#stufe-2-2), la prédiction pour l’appartement 1, avec $\mathbf{x}_1=(60,\,2,\,3)^{\top}$ et les poids $\mathbf{w}=(3,\,10,\,-4)^{\top}$, était $\hat y_1=\mathbf{w}^{\top}\mathbf{x}_1=188$. En tant que fonction des poids, elle a pour gradient $\nabla_{\mathbf{w}}\hat y_1=\mathbf{x}_1=(60,\,2,\,3)^{\top}$. Si l’on augmente $w_1$ de $0{,}1$, la prédiction augmente de $60\cdot0{,}1=6$ et passe à $194$ ; effectivement, $3{,}1\cdot60+10\cdot2-4\cdot3=194$. La raison est simple : chaque poids est multiplié par sa caractéristique, et c’est pourquoi la sensibilité par rapport à un poids est exactement la caractéristique correspondante.
::::

⁠**En bref :** Le gradient de $\mathbf{a}^{\top}\mathbf{x}$ par rapport à $\mathbf{x}$ est $\mathbf{a}$, celui de $\mathbf{y}^{\top}\mathbf{A}\mathbf{x}$ est $\mathbf{A}^{\top}\mathbf{y}$.

### Formes quadratiques

<span class="anker" id="stufe-7-3"></span>

Les formes quadratiques $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}$ du [chapitre 2, section 5](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/quadratische-formen.html#stufe-5), apparaissent partout où l’on additionne des carrés. Lors de la dérivation, $\mathbf{x}$ apparaît à deux endroits, et les deux contribuent, comme les deux chemins de la section [6.2](die-kettenregel-fur-mehrere-variablen.html#stufe-6-2).

:::satz Théorème 7.3 (Gradient d’une forme quadratique)
<span class="anker" id="satz-7-3"></span>

Pour une matrice $\mathbf{A}\in\mathbb{R}^{n\times n}$, on a

<span class="anker" id="gl-7-2"></span>
$$\nabla_{\mathbf{x}}(\mathbf{x}^{\top}\mathbf{A}\mathbf{x})=(\mathbf{A}+\mathbf{A}^{\top})\,\mathbf{x} . \tag{7.2}$$

Si $\mathbf{A}$ est symétrique, cela donne $2\mathbf{A}\mathbf{x}$. En particulier, $\nabla\lVert\mathbf{x}\rVert^2=\nabla(\mathbf{x}^{\top}\mathbf{x})=2\mathbf{x}$.
:::

:::beweis Gradient d’une forme quadratique
On a $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=\sum_{i=1}^n\sum_{j=1}^nx_i\,a_{ij}\,x_j$. Si l’on dérive par rapport à $x_k$, deux groupes de termes contribuent : ceux avec $i=k$, dont la dérivée est $\sum_ja_{kj}x_j=(\mathbf{A}\mathbf{x})_k$, et ceux avec $j=k$, dont la dérivée est $\sum_ix_ia_{ik}=(\mathbf{A}^{\top}\mathbf{x})_k$. Le terme $i=j=k$ vaut $a_{kk}x_k^2$ et a pour dérivée $2a_{kk}x_k$ ; il figure une fois dans chacun des deux groupes, avec $a_{kk}x_k$. La composante $k$ du gradient est donc $(\mathbf{A}\mathbf{x})_k+(\mathbf{A}^{\top}\mathbf{x})_k$.
:::

D’après le [chapitre 2, section 5.2](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/quadratische-formen.html#stufe-5-2), la forme quadratique ne dépend que de la partie symétrique $\mathbf{S}=\tfrac12(\mathbf{A}+\mathbf{A}^{\top})$. La formule est cohérente avec cela : $(\mathbf{A}+\mathbf{A}^{\top})\mathbf{x}=2\mathbf{S}\mathbf{x}$.

::::beispiel [Exemple de calcul]
Pour $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\0&3\end{smallmatrix}\bigr)$, on a $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=x_1^2+2x_1x_2+3x_2^2$, donc $6$ au point $\mathbf{x}=(1,\,1)^{\top}$. D’après [(7.2)](#gl-7-2), on a

$$\nabla f(1,1)=(\mathbf{A}+\mathbf{A}^{\top})\mathbf{x}=\begin{pmatrix}2&2\\2&6\end{pmatrix}\begin{pmatrix}1\\1\end{pmatrix}=\begin{pmatrix}2+2\\2+6\end{pmatrix}=\begin{pmatrix}4\\8\end{pmatrix}.$$

Vérification avec les dérivées partielles $2x_1+2x_2=4$ et $2x_1+6x_2=8$. La formule $2\mathbf{A}\mathbf{x}=(6,\,6)^{\top}$, qui ne vaut que pour les matrices symétriques, serait fausse ici.
::::

⁠**En bref :** Le gradient de $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}$ est $(\mathbf{A}+\mathbf{A}^{\top})\mathbf{x}$, donc $2\mathbf{A}\mathbf{x}$ pour $\mathbf{A}$ symétrique, et celui de $\lVert\mathbf{x}\rVert^2$ est $2\mathbf{x}$.

### La somme des carrés d’un résidu

<span class="anker" id="stufe-7-4"></span>

Dans le [chapitre 2, section 3](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/die-beste-naherungslosung.html#stufe-3), le résidu $\mathbf{r}=\mathbf{y}-\mathbf{A}\mathbf{x}$ était le vecteur d’erreur d’un système d’équations $\mathbf{A}\mathbf{x}=\mathbf{y}$ sans solution, et l’on cherchait le $\mathbf{x}$ dont le résidu est le plus court. La somme des carrés $\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert^2$ est une fonction de $\mathbf{x}$, et son gradient dit comment elle réagit à une modification de $\mathbf{x}$.

:::satz Théorème 7.4 (Gradient de la somme des carrés)
<span class="anker" id="satz-7-4"></span>

Pour $f(\mathbf{x})=\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert^2$ avec $\mathbf{A}\in\mathbb{R}^{m\times n}$ et $\mathbf{y}\in\mathbb{R}^m$, on a

<span class="anker" id="gl-7-3"></span>
$$\nabla f(\mathbf{x})=-2\mathbf{A}^{\top}(\mathbf{y}-\mathbf{A}\mathbf{x})=2\mathbf{A}^{\top}(\mathbf{A}\mathbf{x}-\mathbf{y}). \tag{7.3}$$
:::

:::beweis Gradient de la somme des carrés
La fonction est une composée : d’abord l’application affine $\mathbf{r}(\mathbf{x})=\mathbf{y}-\mathbf{A}\mathbf{x}$ forme le résidu, puis $\mathbf{r}\mapsto\lVert\mathbf{r}\rVert^2$ forme sa somme des carrés. D’après la section [5.4](die-jacobi-matrix.html#stufe-5-4), $\mathbf{J}_{\mathbf{r}}=-\mathbf{A}$ ; d’après [(7.2)](#gl-7-2), $\nabla_{\mathbf{r}}\lVert\mathbf{r}\rVert^2=2\mathbf{r}$. La règle de dérivation en chaîne [(6.3)](die-kettenregel-fur-mehrere-variablen.html#gl-6-3) donne $\nabla f=(-\mathbf{A})^{\top}\,2\mathbf{r}=-2\mathbf{A}^{\top}\mathbf{r}$.
:::

::::beispiel [Exemple de calcul]
Soit $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\0&1\end{smallmatrix}\bigr)$, $\mathbf{y}=(1,\,0)^{\top}$ et $\mathbf{x}=(2,\,1)^{\top}$. Alors $\mathbf{A}\mathbf{x}=(4,\,1)^{\top}$, le résidu est $\mathbf{r}=(-3,\,-1)^{\top}$ et $f(\mathbf{x})=9+1=10$. Avec $\mathbf{A}^{\top}\mathbf{r}=(-3,\,-7)^{\top}$, on a

$$\nabla f(\mathbf{x})=-2\mathbf{A}^{\top}\mathbf{r}=-2\begin{pmatrix}-3\\-7\end{pmatrix}=\begin{pmatrix}6\\14\end{pmatrix}$$

(Fig. [13](#abb-13)). Vérification : écrite explicitement, $f(\mathbf{x})=(1-x_1-2x_2)^2+x_2^2$, de dérivées partielles $-2\,(1-x_1-2x_2)=6$ et $-4\,(1-x_1-2x_2)+2x_2=12+2=14$.

:::abbildung ml/k3rresiduum 13
Le gradient de la somme des carrés $\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert^2$ : chaque composante de $\mathbf{A}^{\top}\mathbf{r}$ est le produit scalaire d’une colonne de $\mathbf{A}$ et du résidu.
:::
::::

La formule rejoint le [chapitre 2](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/projektion-eigenwerte-und-zerlegungen.html). Le résidu de la meilleure solution approchée $\hat{\mathbf{x}}$ y était perpendiculaire à toutes les colonnes de $\mathbf{A}$, donc $\mathbf{A}^{\top}\hat{\mathbf{r}}=\mathbf{0}$, et il en découlait les équations normales $\mathbf{A}^{\top}\mathbf{A}\hat{\mathbf{x}}=\mathbf{A}^{\top}\mathbf{y}$. D’après [(7.3)](#gl-7-3), cela signifie : au point $\hat{\mathbf{x}}$, le gradient de la somme des carrés est nul ; elle n’y monte ni ne descend dans aucune direction, aux termes d’ordre deux près. Pour l’exemple du [chapitre 2, section 3.3](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/die-beste-naherungslosung.html#stufe-3-3), avec la matrice $\mathbf{A}=\Bigl(\begin{smallmatrix}1&0\\0&1\\1&1\end{smallmatrix}\Bigr)$, $\mathbf{y}=(1,\,1,\,1)^{\top}$ et $\hat{\mathbf{x}}=(\tfrac23,\,\tfrac23)^{\top}$, on a $\hat{\mathbf{r}}=(\tfrac13,\,\tfrac13,\,-\tfrac13)^{\top}$ et $\mathbf{A}^{\top}\hat{\mathbf{r}}=(\tfrac13-\tfrac13,\ \tfrac13-\tfrac13)^{\top}=\mathbf{0}$.

⁠**En bref :** Le gradient de $\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert^2$ est $-2\mathbf{A}^{\top}(\mathbf{y}-\mathbf{A}\mathbf{x})$ ; il s’annule exactement là où le résidu est perpendiculaire aux colonnes de $\mathbf{A}$.

### Dériver par rapport à une matrice

<span class="anker" id="stufe-7-5"></span>

Parfois, la variable n’est pas un vecteur, mais toute une matrice : comment un nombre change-t-il lorsqu’on modifie un coefficient d’une matrice ? D’après la règle (iii) de la convention, on range les $m\cdot n$ dérivées partielles sous la forme de la matrice. L’approximation linéaire vaut alors comme d’habitude, à ceci près que le produit scalaire porte sur tous les coefficients :

<span class="anker" id="gl-7-4"></span>
$$f(\mathbf{A}+\mathbf E)\approx f(\mathbf{A})+\sum_{i=1}^m\sum_{j=1}^n\bigl(\nabla_{\mathbf{A}}f\bigr)_{ij}\,e_{ij} \tag{7.4}$$

pour une petite matrice $\mathbf E$ de coefficients $e_{ij}$. La somme double est la même chose que $\operatorname{tr}\bigl((\nabla_{\mathbf{A}}f)^{\top}\mathbf E\bigr)$, avec la trace du [chapitre 2, section 6.5](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/eigenwerte-und-eigenvektoren.html#stufe-6-5).

:::satz Théorème 7.5 (Deux dérivées par rapport à une matrice)
<span class="anker" id="satz-7-5"></span>

Pour des vecteurs fixes $\mathbf{u}\in\mathbb{R}^m$, $\mathbf{v}\in\mathbb{R}^n$ et une matrice $\mathbf{A}\in\mathbb{R}^{m\times n}$, on a

<span class="anker" id="gl-7-5"></span>
$$\nabla_{\mathbf{A}}(\mathbf{u}^{\top}\mathbf{A}\mathbf{v})=\mathbf{u}\mathbf{v}^{\top},\qquad \nabla_{\mathbf{A}}\lVert\mathbf{A}\rVert_F^2=2\mathbf{A} . \tag{7.5}$$

Ici, $\lVert\mathbf{A}\rVert_F$ est la norme de Frobenius du [chapitre 2, section 10.1](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/naherung-durch-matrizen-von-kleinem-rang.html#stufe-10-1).
:::

:::beweis Deux dérivées par rapport à une matrice
On a $\mathbf{u}^{\top}\mathbf{A}\mathbf{v}=\sum_i\sum_ju_i\,a_{ij}\,v_j$. Le coefficient $a_{ij}$ apparaît dans un seul terme, avec le facteur $u_iv_j$. Donc $\partial(\mathbf{u}^{\top}\mathbf{A}\mathbf{v})/\partial a_{ij}=u_iv_j$, et c’est le coefficient $(i,j)$ du produit extérieur $\mathbf{u}\mathbf{v}^{\top}$ du [chapitre 1, section 9.5](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrixprodukt.html#stufe-9-5). De même, $\lVert\mathbf{A}\rVert_F^2=\sum_{i,j}a_{ij}^2$, et sa dérivée $\partial/\partial a_{ij}$ vaut $2a_{ij}$.
:::

::::beispiel [Exemple de calcul]
Pour $\mathbf{u}=(1,\,2)^{\top}$ et $\mathbf{v}=(3,\,-1)^{\top}$, on a

$$\nabla_{\mathbf{A}}(\mathbf{u}^{\top}\mathbf{A}\mathbf{v})=\mathbf{u}\mathbf{v}^{\top}=\begin{pmatrix}3&-1\\6&-2\end{pmatrix},$$

en tout point $\mathbf{A}$, car la fonction est linéaire en $\mathbf{A}$. Pour $\mathbf{A}=\mathbf{I}$, on a $\mathbf{u}^{\top}\mathbf{A}\mathbf{v}=\mathbf{u}^{\top}\mathbf{v}=3-2=1$. Si l’on augmente le coefficient $a_{21}$ de $0{,}1$, le gradient prévoit une variation de $6\cdot0{,}1=0{,}6$. En effet, $a_{21}$ n’apparaît que dans le terme $u_2\,a_{21}\,v_1=2\cdot a_{21}\cdot3$, et celui-ci augmente de $0{,}6$.
::::

⁠**En bref :** La dérivée d’un nombre par rapport à une matrice a la forme de la matrice ; pour $\mathbf{u}^{\top}\mathbf{A}\mathbf{v}$, c’est le produit extérieur $\mathbf{u}\mathbf{v}^{\top}$, pour $\lVert\mathbf{A}\rVert_F^2$, c’est $2\mathbf{A}$.

### À rebours à travers un produit matriciel

<span class="anker" id="stufe-7-6"></span>

Souvent, un produit matrice-vecteur $\mathbf{y}=\mathbf{A}\mathbf{x}$ n’est qu’une étape intermédiaire d’un calcul plus long, au bout duquel se trouve un nombre $f(\mathbf{y})$. Si l’on sait déjà comment ce nombre réagit à $\mathbf{y}$, c’est-à-dire $\nabla f(\mathbf{y})$, on veut en déduire comment il réagit à $\mathbf{A}$ et à $\mathbf{x}$. Ce calcul à rebours à travers une brique sert de modèle au mode inverse de la section [10](automatische-differentiation.html#stufe-10).

:::satz Théorème 7.6 (Règle arrière du produit matriciel)
<span class="anker" id="satz-7-6"></span>

Soit $f:\mathbb{R}^m\to\mathbb{R}$ différentiable, $\mathbf{y}=\mathbf{A}\mathbf{x}$ avec $\mathbf{A}\in\mathbb{R}^{m\times n}$ et $F(\mathbf{A},\mathbf{x})=f(\mathbf{A}\mathbf{x})$. Alors

<span class="anker" id="gl-7-6"></span>
$$\nabla_{\mathbf{A}}F=\nabla f(\mathbf{y})\,\mathbf{x}^{\top},\qquad \nabla_{\mathbf{x}}F=\mathbf{A}^{\top}\,\nabla f(\mathbf{y}). \tag{7.6}$$

Plus généralement, pour $\mathbf{C}=\mathbf{A}\mathbf{B}$ et $F(\mathbf{A},\mathbf{B})=f(\mathbf{C})$, on a $\nabla_{\mathbf{A}}F=(\nabla_{\mathbf{C}}f)\,\mathbf{B}^{\top}$ et $\nabla_{\mathbf{B}}F=\mathbf{A}^{\top}\,(\nabla_{\mathbf{C}}f)$.
:::

:::beweis Règle arrière du produit matriciel
On a $y_i=\sum_ka_{ik}x_k$. Le coefficient $a_{ij}$ n’influence que $y_i$, avec le facteur $\partial y_i/\partial a_{ij}=x_j$. Il n’y a donc qu’un seul chemin de $a_{ij}$ à $f$, et $\partial F/\partial a_{ij}=\frac{\partial f}{\partial y_i}\,x_j$ ; c’est le coefficient $(i,j)$ de $\nabla f(\mathbf{y})\,\mathbf{x}^{\top}$. La variable $x_j$, elle, influence chaque $y_i$, avec le facteur $a_{ij}$ ; en sommant sur tous les chemins, on obtient $\partial F/\partial x_j=\sum_i\frac{\partial f}{\partial y_i}\,a_{ij}$, la composante $j$ de $\mathbf{A}^{\top}\nabla f(\mathbf{y})$. Le second énoncé s’obtient de la même manière, car $\mathbf{C}=\mathbf{A}\mathbf{B}$ est, colonne par colonne, un produit matrice-vecteur.
:::

::::beispiel [Exemple de calcul]
Dans le [chapitre 1, section 7.1](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrix-vektor-produkt.html#stufe-7-1), on avait $\mathbf{A}=\Bigl(\begin{smallmatrix}1&2\\0&-1\\3&1\end{smallmatrix}\Bigr)$ et $\mathbf{x}=(2,\,1)^{\top}$, donc $\mathbf{y}=\mathbf{A}\mathbf{x}=(4,\,-1,\,7)^{\top}$. Soit $f(\mathbf{y})=y_1-y_3=-3$, donc $\nabla f(\mathbf{y})=(1,\,0,\,-1)^{\top}$. D’après [(7.6)](#gl-7-6), on a

$$\nabla_{\mathbf{A}}F=\begin{pmatrix}1\\0\\-1\end{pmatrix}\begin{pmatrix}2&1\end{pmatrix}=\begin{pmatrix}2&1\\0&0\\-2&-1\end{pmatrix},\qquad \nabla_{\mathbf{x}}F=\mathbf{A}^{\top}\begin{pmatrix}1\\0\\-1\end{pmatrix}=\begin{pmatrix}-2\\1\end{pmatrix}$$

(Fig. [14](#abb-14)). Vérification : écrite explicitement, $F=(x_1+2x_2)-(3x_1+x_2)=-2x_1+x_2$, de gradient $(-2,\,1)^{\top}$. La deuxième ligne de $\nabla_{\mathbf{A}}F$ est nulle parce que $y_2$ n’apparaît pas dans $f$ ; les coefficients de la deuxième ligne de $\mathbf{A}$ n’agissent que sur $y_2$.

:::abbildung ml/k3rrueck 14
Le gradient par rapport à l’entrée d’un produit matrice-vecteur : chaque composante rassemble, sur les trois sorties $y_i$, la force avec laquelle $f$ réagit à $y_i$, pondérée par le facteur $a_{ij}$ avec lequel $x_j$ agit sur $y_i$.
:::
::::

:::warnung La vérification des formes est un moyen mnémotechnique, pas une preuve
Les formes déterminent presque entièrement [(7.6)](#gl-7-6) : $\nabla_{\mathbf{A}}F$ doit être de forme $m\times n$, et, à partir de la colonne $\nabla f(\mathbf{y})$ à $m$ coefficients et de la colonne $\mathbf{x}$ à $n$ coefficients, seul $\nabla f(\mathbf{y})\,\mathbf{x}^{\top}$ donne cette forme. On peut retenir la règle de cette façon. Mais la vérification des formes ne détecte ni un signe faux, ni un facteur manquant, ni un ordre inversé lorsque les matrices sont carrées. Seul le calcul composante par composante justifie la règle.
:::

⁠**En bref :** À rebours à travers $\mathbf{y}=\mathbf{A}\mathbf{x}$ : le gradient par rapport à $\mathbf{A}$ est $\nabla f(\mathbf{y})\,\mathbf{x}^{\top}$, celui par rapport à $\mathbf{x}$ est $\mathbf{A}^{\top}\nabla f(\mathbf{y})$.

:::aufgabe Exercice 24 ★ Gradients en notation matricielle
<span class="anker" id="aufg-24"></span>

Calculez à l’aide des formules de cette section et vérifiez chaque fois avec les dérivées partielles.

<ol class="al">

<li>

$f(\mathbf{x})=\mathbf{b}^{\top}\mathbf{x}+5$ avec $\mathbf{b}=(2,\,-1,\,4)^{\top}$ ;

</li>

<li>

$f(\mathbf{x})=\lVert\mathbf{x}\rVert^2$ au point $(1,\,-1,\,2)$ ;

</li>

<li>

$f(\mathbf{x})=\mathbf{x}^{\top}\mathbf{A}\mathbf{x}$ avec $\mathbf{A}=\bigl(\begin{smallmatrix}2&1\\3&4\end{smallmatrix}\bigr)$ au point $(1,\,-1)$.

</li>

</ol>

:::loesung
(a) D’après [(7.1)](#gl-7-1), on a $\nabla f=\mathbf{b}=(2,\,-1,\,4)^{\top}$. Vérification : $f=2x_1-x_2+4x_3+5$.

(b) D’après [(7.2)](#gl-7-2) avec $\mathbf{A}=\mathbf{I}$, on a $\nabla f=2\mathbf{x}=(2,\,-2,\,4)^{\top}$. Vérification : $\partial_jf=2x_j$.

(c) $\mathbf{A}+\mathbf{A}^{\top}=\bigl(\begin{smallmatrix}4&4\\4&8\end{smallmatrix}\bigr)$, donc $\nabla f(1,-1)=(4-4,\ 4-8)^{\top}=(0,\,-4)^{\top}$. Vérification : $f=2x_1^2+4x_1x_2+4x_2^2$ a pour dérivées partielles $4x_1+4x_2=0$ et $4x_1+8x_2=-4$.
:::
:::

:::aufgabe Exercice 25 ★★ La droite des moindres carrés du chapitre 2
<span class="anker" id="aufg-25"></span>

Dans le [chapitre 2, section 3.6](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/die-beste-naherungslosung.html#stufe-3-6), on a ajusté une droite aux points $(0,\,1)$, $(1,\,2)$ et $(2,\,4)$, avec $\mathbf{A}=\Bigl(\begin{smallmatrix}1&0\\1&1\\1&2\end{smallmatrix}\Bigr)$ et $\mathbf{y}=(1,\,2,\,4)^{\top}$.

<ol class="al">

<li>

Calculez $f(\mathbf{x})=\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert^2$ et $\nabla f(\mathbf{x})$ au point $\mathbf{x}=(1,\,1)^{\top}$.

</li>

<li>

Dans quelle direction faut-il déplacer $\mathbf{x}$ d’un petit pas à partir de $(1,\,1)$ pour que $f$ diminue le plus vite ?

</li>

<li>

Montrez que le gradient est nul au point $\hat{\mathbf{x}}=(\tfrac56,\,\tfrac32)^{\top}$ du [chapitre 2](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/projektion-eigenwerte-und-zerlegungen.html).

</li>

</ol>

:::loesung
(a) $\mathbf{A}\mathbf{x}=(1,\,2,\,3)^{\top}$, $\mathbf{r}=\mathbf{y}-\mathbf{A}\mathbf{x}=(0,\,0,\,1)^{\top}$ et $f=1$. Avec $\mathbf{A}^{\top}\mathbf{r}=(0+0+1,\ 0+0+2)^{\top}=(1,\,2)^{\top}$, on a $\nabla f=-2\mathbf{A}^{\top}\mathbf{r}=(-2,\,-4)^{\top}$.

(b) C’est dans la direction $-\nabla f/\lVert\nabla f\rVert=(2,\,4)^{\top}/\sqrt{20}=(1,\,2)^{\top}/\sqrt5\approx(0{,}447;\ 0{,}894)^{\top}$ que $f$ diminue le plus vite : l’ordonnée à l’origine doit augmenter un peu, la pente deux fois plus. Cela concorde avec le fait que la droite $1+t$ manque le troisième point $(2,\,4)$ de $1$.

(c) $\mathbf{A}\hat{\mathbf{x}}=(\tfrac56,\ \tfrac73,\ \tfrac{23}6)^{\top}$, donc $\hat{\mathbf{r}}=(\tfrac16,\ -\tfrac13,\ \tfrac16)^{\top}$ et

$$\mathbf{A}^{\top}\hat{\mathbf{r}}=\begin{pmatrix}\tfrac16-\tfrac13+\tfrac16\\0-\tfrac13+\tfrac26\end{pmatrix}=\begin{pmatrix}0\\0\end{pmatrix}.$$

Le gradient est nul : à la meilleure solution approchée, aucun petit déplacement ne modifie la somme des carrés au premier ordre.
:::
:::

:::aufgabe Exercice 26 ★★ Dérivées par rapport à une matrice
<span class="anker" id="aufg-26"></span>

<ol class="al">

<li>

Montrez que $\nabla_{\mathbf{A}}\operatorname{tr}\mathbf{A}=\mathbf{I}$ pour $\mathbf{A}$ carrée.

</li>

<li>

Montrez à l’aide de [(7.6)](#gl-7-6) et de $\nabla\lVert\mathbf{y}\rVert^2=2\mathbf{y}$ que $\nabla_{\mathbf{A}}\lVert\mathbf{A}\mathbf{x}\rVert^2=2\,(\mathbf{A}\mathbf{x})\,\mathbf{x}^{\top}$, et calculez ce gradient pour $\mathbf{A}=\mathbf{I}\in\mathbb{R}^{2\times2}$ et $\mathbf{x}=(1,\,2)^{\top}$.

</li>

<li>

Vérifiez (b) avec l’approximation linéaire [(7.4)](#gl-7-4) : de combien $\lVert\mathbf{A}\mathbf{x}\rVert^2$ change-t-il environ si l’on augmente $a_{12}$ de $0$ à $0{,}01$ ? Faites le calcul exact.

</li>

</ol>

:::loesung
(a) $\operatorname{tr}\mathbf{A}=\sum_ia_{ii}$. La dérivée par rapport à $a_{ij}$ vaut $1$ pour $i=j$ et $0$ sinon ; disposée sous la forme de $\mathbf{A}$, c’est $\mathbf{I}$.

(b) On a $\lVert\mathbf{A}\mathbf{x}\rVert^2=f(\mathbf{y})$ avec $\mathbf{y}=\mathbf{A}\mathbf{x}$ et $\nabla f(\mathbf{y})=2\mathbf{y}$. D’après [(7.6)](#gl-7-6), $\nabla_{\mathbf{A}}\lVert\mathbf{A}\mathbf{x}\rVert^2=2\mathbf{y}\,\mathbf{x}^{\top}=2\,(\mathbf{A}\mathbf{x})\,\mathbf{x}^{\top}$. Pour $\mathbf{A}=\mathbf{I}$ et $\mathbf{x}=(1,\,2)^{\top}$ :

$$\nabla_{\mathbf{A}}\lVert\mathbf{A}\mathbf{x}\rVert^2=2\begin{pmatrix}1\\2\end{pmatrix}\begin{pmatrix}1&2\end{pmatrix}=\begin{pmatrix}2&4\\4&8\end{pmatrix}.$$

(c) Le coefficient $(1,2)$ du gradient vaut $4$, donc [(7.4)](#gl-7-4) prédit une variation d’environ $4\cdot0{,}01=0{,}04$. Calcul exact : avec $a_{12}=0{,}01$, on a $\mathbf{A}\mathbf{x}=(1{,}02;\ 2)^{\top}$ et $\lVert\mathbf{A}\mathbf{x}\rVert^2=1{,}0404+4=5{,}0404$, soit une variation de $0{,}0404$ par rapport à $5$.
:::
:::

:::aufgabe Exercice 27 ★★★ La règle arrière pour un produit de deux matrices
<span class="anker" id="aufg-27"></span>

Soit $\mathbf{C}=\mathbf{A}\mathbf{B}$ et $F(\mathbf{A},\mathbf{B})=f(\mathbf{C})$ avec $\mathbf G=\nabla_{\mathbf{C}}f$.

<ol class="al">

<li>

Montrez composante par composante que $\nabla_{\mathbf{A}}F=\mathbf G\mathbf{B}^{\top}$ et $\nabla_{\mathbf{B}}F=\mathbf{A}^{\top}\mathbf G$.

</li>

<li>

Vérifiez les deux formules pour $\mathbf{A}=(1\ \ 2)$, $\mathbf{B}=\bigl(\begin{smallmatrix}3\\4\end{smallmatrix}\bigr)$ et $f(\mathbf{C})=c_{11}^2$ en écrivant $F$ explicitement.

</li>

</ol>

:::loesung
(a) On a $c_{ik}=\sum_ja_{ij}b_{jk}$. Le coefficient $a_{ij}$ agit sur tous les $c_{ik}$ de la ligne $i$, avec le facteur $b_{jk}$ ; en sommant sur ces chemins, on obtient $\partial F/\partial a_{ij}=\sum_kg_{ik}b_{jk}=(\mathbf G\mathbf{B}^{\top})_{ij}$. Le coefficient $b_{jk}$ agit sur tous les $c_{ik}$ de la colonne $k$, avec le facteur $a_{ij}$ ; donc $\partial F/\partial b_{jk}=\sum_ia_{ij}g_{ik}=(\mathbf{A}^{\top}\mathbf G)_{jk}$.

(b) $\mathbf{C}=1\cdot3+2\cdot4=11$, $F=121$ et $\mathbf G=2c_{11}=22$. Les formules donnent $\nabla_{\mathbf{A}}F=22\,(3\ \ 4)=(66\ \ 88)$ et $\nabla_{\mathbf{B}}F=(1,\,2)^{\top}\cdot22=(22,\,44)^{\top}$. Écrite explicitement, $F=(3a_{11}+4a_{12})^2$, de dérivées $2\cdot11\cdot3=66$ et $2\cdot11\cdot4=88$, et $F=(b_{11}+2b_{21})^2$, de dérivées $22$ et $44$.
:::
:::

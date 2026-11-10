---
title: Projection sur un sous-espace
pfad: Informatique / Apprentissage automatique / Fondements mathématiques / Projection, valeurs propres et décompositions
adresse: informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen
knoten: Chapitre 2 : Projection, valeurs propres et décompositions
nachschlagen: ja
order: 15220500
summary: La section précédente a trouvé le point le plus proche d’un espace des colonnes.
tags: sous-espace, matrice de projection, supplémentaire orthogonal, procédé de Gram-Schmidt, décomposition QR
lang: fr
---

<span class="anker" id="stufe-4"></span>

:::zweck
La section précédente a trouvé le point le plus proche d’un espace des colonnes. Cette section exprime ce résultat sous forme de matrice, montre que tout devient particulièrement simple lorsque les colonnes sont orthonormées, et présente un procédé qui transforme des colonnes indépendantes quelconques en colonnes orthonormées. On peut ainsi calculer la meilleure solution approchée sans former $\mathbf{A}^{\top}\mathbf{A}$.
:::

### Sous-espaces

<span class="anker" id="stufe-4-1"></span>

Les droites et les plans passant par l’origine, les espaces des colonnes et les noyaux ont une propriété commune : lorsqu’ils contiennent deux vecteurs, ils contiennent aussi toute combinaison linéaire de ces deux vecteurs. On n’en sort jamais en additionnant ou en multipliant par des nombres. Ces ensembles portent un nom particulier.

:::definition Définition 4.1 (Sous-espace)
<span class="anker" id="satz-4-1"></span>

Un ensemble $\mathcal U\subseteq\mathbb{R}^n$ est appelé __sous-espace__ de $\mathbb{R}^n$ s’il est engendré par un nombre fini de vecteurs.
:::

De façon équivalente : $\mathcal U$ contient le vecteur nul, et lorsque $\mathcal U$ contient deux vecteurs $\mathbf{u},\mathbf{v}$, il contient aussi $\mathbf{u}+\mathbf{v}$ et tout multiple $c\,\mathbf{u}$. Tout sous-espace a une base et donc, d’après le [chapitre 1, section 13.3](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/unabhangigkeit-basis-und-rang.html#stufe-13-3), une dimension.

::::beispiel [Exemple de calcul]
Dans $\mathbb{R}^3$, sont des sous-espaces : l’origine seule, de dimension $0$ ; toute droite passant par l’origine, de dimension $1$ ; tout plan passant par l’origine, comme l’espace des colonnes de $\mathbf{H}$ de la section précédente, de dimension $2$ ; et $\mathbb{R}^3$ tout entier. Le noyau d’une matrice est un sous-espace, son espace des colonnes aussi. Une droite qui ne passe pas par l’origine n’est pas un sous-espace, car elle ne contient pas le vecteur nul.
::::

⁠**En bref :** Un sous-espace est l’ensemble engendré par des vecteurs ; on n’en sort pas en additionnant ou en multipliant par des nombres.

### La matrice de projection d’un espace des colonnes

<span class="anker" id="stufe-4-2"></span>

Pour des colonnes linéairement indépendantes, [(3.5)](die-beste-naherungslosung.html#gl-3-5) donne le point le plus proche $\hat{\mathbf{y}}=\mathbf{A}\hat{\mathbf{x}}=\mathbf{A}(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}\mathbf{y}$. La matrice placée devant $\mathbf{y}$ ne dépend que de $\mathbf{A}$. Elle fait pour l’espace des colonnes ce que $\mathbf{a}\mathbf{a}^{\top}/(\mathbf{a}^{\top}\mathbf{a})$ faisait pour une droite.

:::definition Définition 4.2 (Matrice de projection d’un espace des colonnes)
<span class="anker" id="satz-4-2"></span>

Si $\mathbf{A}$ a des colonnes linéairement indépendantes, on appelle

<span class="anker" id="gl-4-1"></span>
$$\mathbf{P}=\mathbf{A}(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top} \tag{4.1}$$

la __matrice de projection__ sur l’espace des colonnes de $\mathbf{A}$.
:::

:::satz Théorème 4.3 (Propriétés)
<span class="anker" id="satz-4-3"></span>

On a $\mathbf{P}\mathbf{y}=\hat{\mathbf{y}}$, $\mathbf{P}^{\top}=\mathbf{P}$, $\mathbf{P}^2=\mathbf{P}$ et $\mathbf{P}\mathbf{A}=\mathbf{A}$. Donc $\mathbf{P}$ est la projection orthogonale sur l’espace des colonnes.
:::

:::beweis Propriétés
La première égalité est le calcul ci-dessus. Avec les règles de calcul du [chapitre 1, sections 10.1](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/transponierte-symmetrie-und-gram-matrix.html#stufe-10-1) et [11.4](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/einheitsmatrix-und-inverse.html#stufe-11-4), on a $\mathbf{P}^{\top}=\mathbf{A}\bigl((\mathbf{A}^{\top}\mathbf{A})^{-1}\bigr)^{\top}\mathbf{A}^{\top}=\mathbf{A}(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}=\mathbf{P}$, car $\mathbf{A}^{\top}\mathbf{A}$ est symétrique, et donc son inverse aussi. De plus, $\mathbf{P}\mathbf{A}=\mathbf{A}(\mathbf{A}^{\top}\mathbf{A})^{-1}(\mathbf{A}^{\top}\mathbf{A})=\mathbf{A}$, d’où $\mathbf{P}^2=\mathbf{P}\mathbf{A}(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}=\mathbf{A}(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}=\mathbf{P}$. D’après le théorème de la section [2.4](projektion-auf-eine-gerade.html#stufe-2-4), une projection symétrique est orthogonale.
:::

L’égalité $\mathbf{P}\mathbf{A}=\mathbf{A}$ dit : chaque colonne, et donc chaque vecteur de l’espace des colonnes, reste en place lors de la projection.

::::beispiel [Exemple de calcul]
Pour $\mathbf{H}$, on a

$$\mathbf{P}=\mathbf{H}\cdot\frac13\begin{pmatrix}2&-1\\-1&2\end{pmatrix}\mathbf{H}^{\top}=\frac13\begin{pmatrix}2&-1&1\\-1&2&1\\1&1&2\end{pmatrix}.$$

Vérification : $\mathbf{P}(1,\,1,\,1)^{\top}=\tfrac13(2,\,2,\,4)^{\top}=(\tfrac23,\,\tfrac23,\,\tfrac43)^{\top}=\hat{\mathbf{y}}$, et $\mathbf{P}\mathbf{a}_1=\tfrac13(2+1,\ -1+1,\ 1+2)^{\top}=(1,\,0,\,1)^{\top}=\mathbf{a}_1$.
::::

⁠**En bref :** La matrice de projection $\mathbf{P}=\mathbf{A}(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}$ envoie chaque vecteur sur le point le plus proche de l’espace des colonnes ; elle est symétrique et vérifie $\mathbf{P}^2=\mathbf{P}$.

### Colonnes orthonormées

<span class="anker" id="stufe-4-3"></span>

La formule [(4.1)](#gl-4-1) contient une inverse. Celle-ci disparaît lorsque les colonnes sont orthonormées, car alors $\mathbf{A}^{\top}\mathbf{A}=\mathbf{I}$. Pour une matrice $\mathbf{Q}$ à colonnes orthonormées, la meilleure solution approchée est donc simplement $\hat{\mathbf{x}}=\mathbf{Q}^{\top}\mathbf{y}$ : ses composantes sont les longueurs des ombres $\mathbf{q}_i^{\top}\mathbf{y}$.

:::satz Théorème 4.4 (Projection dans le cas de colonnes orthonormées)
<span class="anker" id="satz-4-4"></span>

Si $\mathbf{Q}\in\mathbb{R}^{n\times k}$ a des colonnes orthonormées $\mathbf{q}_1,\dots,\mathbf{q}_k$, la matrice de projection sur son espace des colonnes est

<span class="anker" id="gl-4-2"></span>
$$\mathbf{P}=\mathbf{Q}\mathbf{Q}^{\top}=\sum_{i=1}^k\mathbf{q}_i\mathbf{q}_i^{\top} . \tag{4.2}$$
:::

La forme en somme découle du [chapitre 1, section 9.5](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrixprodukt.html#stufe-9-5) : un produit matriciel est la somme des produits extérieurs des colonnes et des lignes. Chaque terme $\mathbf{q}_i\mathbf{q}_i^{\top}$ est la matrice de projection sur la droite de direction $\mathbf{q}_i$. Pour des colonnes orthonormées, la projection sur l’espace des colonnes est donc la somme des projections sur les différents axes. Cela explique après coup la dernière sous-section de la section [1](orthonormalbasen-und-orthogonale-matrizen.html#stufe-1) : $\mathbf{Q}\mathbf{Q}^{\top}$ n’est pas la matrice identité, mais la projection sur l’espace des colonnes de $\mathbf{Q}$. Ce qui est perpendiculaire à cet espace, elle le jette.

::::beispiel [Exemple de calcul]
Les vecteurs $\mathbf{q}_1=\tfrac1{\sqrt2}(1,\,0,\,1)^{\top}$ et $\mathbf{q}_2=\tfrac1{\sqrt6}(-1,\,2,\,1)^{\top}$ sont orthonormés : $\lVert\mathbf{q}_1\rVert^2=\tfrac22$, $\lVert\mathbf{q}_2\rVert^2=\tfrac66$, $\mathbf{q}_1^{\top}\mathbf{q}_2=\tfrac{-1+0+1}{\sqrt{12}}=0$. Pour les deux, la troisième composante est la somme des deux premières ; ils forment une base orthonormée du plan de $\mathbf{H}$. On a

$$\mathbf{q}_1\mathbf{q}_1^{\top}+\mathbf{q}_2\mathbf{q}_2^{\top}=\frac12\begin{pmatrix}1&0&1\\0&0&0\\1&0&1\end{pmatrix}+\frac16\begin{pmatrix}1&-2&-1\\-2&4&2\\-1&2&1\end{pmatrix}=\frac13\begin{pmatrix}2&-1&1\\-1&2&1\\1&1&2\end{pmatrix},$$

la même matrice que dans la sous-section précédente, cette fois sans inverse.
::::

⁠**En bref :** Pour des colonnes orthonormées, $\hat{\mathbf{x}}=\mathbf{Q}^{\top}\mathbf{y}$ et $\mathbf{P}=\mathbf{Q}\mathbf{Q}^{\top}$, la somme des projections sur les différentes colonnes.

### Le supplémentaire orthogonal

<span class="anker" id="stufe-4-4"></span>

Si l’on projette $\mathbf{y}$ sur un sous-espace, il reste le résidu $\mathbf{y}-\mathbf{P}\mathbf{y}$. Il est perpendiculaire à tout le sous-espace. Tous les vecteurs ayant cette propriété forment eux-mêmes un sous-espace, et $\mathbf{y}$ se décompose en une partie dans l’un et une partie dans l’autre.

:::definition Définition 4.5 (Supplémentaire orthogonal)
<span class="anker" id="satz-4-5"></span>

Le __supplémentaire orthogonal__ d’un sous-espace $\mathcal U\subseteq\mathbb{R}^n$ est l’ensemble

<span class="anker" id="gl-4-3"></span>
$$\mathcal U^\perp=\{\mathbf{z}\in\mathbb{R}^n:\ \mathbf{z}^{\top}\mathbf{u}=0\ \text{pour tout}\ \mathbf{u}\in\mathcal U\} . \tag{4.3}$$
:::

On lit $\mathcal U^\perp$ « $\mathcal U$ orthogonal ». Si $\mathcal U$ est l’espace des colonnes de $\mathbf{A}$, $\mathbf{z}$ est perpendiculaire à $\mathcal U$ si et seulement si $\mathbf{A}^{\top}\mathbf{z}=\mathbf{0}$ ; le supplémentaire orthogonal est donc le noyau de $\mathbf{A}^{\top}$.

:::satz Théorème 4.6 (Décomposition en deux parties perpendiculaires)
<span class="anker" id="satz-4-6"></span>

Si $\mathbf{P}$ est la projection orthogonale sur un sous-espace $\mathcal U$ de $\mathbb{R}^n$, alors :

<ol class="rm">

<li>

Tout vecteur $\mathbf{y}$ s’écrit d’une seule façon comme somme $\mathbf{y}=\mathbf{u}+\mathbf{z}$ avec $\mathbf{u}\in\mathcal U$ et $\mathbf{z}\in\mathcal U^\perp$, à savoir $\mathbf{u}=\mathbf{P}\mathbf{y}$ et $\mathbf{z}=(\mathbf{I}-\mathbf{P})\mathbf{y}$.

</li>

<li>

$\mathbf{I}-\mathbf{P}$ est la projection orthogonale sur $\mathcal U^\perp$.

</li>

<li>

$\dim\mathcal U^\perp=n-\dim\mathcal U$.

</li>

</ol>
:::

:::beweis Décomposition
(i) Que $\mathbf{P}\mathbf{y}$ soit dans $\mathcal U$ et que $\mathbf{y}-\mathbf{P}\mathbf{y}$ soit perpendiculaire à $\mathcal U$, c’est la définition de la projection orthogonale. S’il existait une seconde décomposition $\mathbf{y}=\mathbf{u}'+\mathbf{z}'$, alors $\mathbf{u}-\mathbf{u}'=\mathbf{z}'-\mathbf{z}$ serait un vecteur appartenant à $\mathcal U$ et en même temps perpendiculaire à $\mathcal U$, donc perpendiculaire à lui-même. Le carré de sa longueur serait alors nul ; ce serait donc le vecteur nul. (ii) $\mathbf{I}-\mathbf{P}$ est symétrique, et $(\mathbf{I}-\mathbf{P})^2=\mathbf{I}-2\mathbf{P}+\mathbf{P}^2=\mathbf{I}-\mathbf{P}$. D’après (i), son image est contenue dans $\mathcal U^\perp$. Tout $\mathbf{z}\in\mathcal U^\perp$ reste fixe : $\mathbf{P}\mathbf{z}$ est dans $\mathcal U$ et est en même temps la différence $\mathbf{z}-(\mathbf{z}-\mathbf{P}\mathbf{z})$ de deux vecteurs perpendiculaires à $\mathcal U$ ; donc $\mathbf{P}\mathbf{z}$ est perpendiculaire à lui-même et vaut $\mathbf{0}$. (iii) Si l’on choisit une base de $\mathcal U$ comme colonnes d’une matrice $\mathbf{A}$, alors $\mathcal U^\perp$ est le noyau de $\mathbf{A}^{\top}$. D’après le théorème du rang du [chapitre 1, section 13.5](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/unabhangigkeit-basis-und-rang.html#stufe-13-5), ce noyau est de dimension $n-\operatorname{rg}\mathbf{A}^{\top}=n-\operatorname{rg}\mathbf{A}=n-\dim\mathcal U$.
:::

::::beispiel [Exemple de calcul]
Le plan de $\mathbf{H}$ est de dimension $2$ ; son supplémentaire orthogonal dans $\mathbb{R}^3$ est donc de dimension $1$ : c’est la droite dirigée par le vecteur normal $\mathbf{k}=(1,\,1,\,-1)^{\top}$. Effectivement, $\mathbf{H}^{\top}\mathbf{k}=(1-1,\ 1-1)^{\top}=\mathbf{0}$. On a

$$\mathbf{I}-\mathbf{P}=\frac13\begin{pmatrix}1&1&-1\\1&1&-1\\-1&-1&1\end{pmatrix}=\frac{\mathbf{k}\mathbf{k}^{\top}}{\mathbf{k}^{\top}\mathbf{k}},$$

la projection sur cette droite. Pour $\mathbf{y}=(1,\,1,\,1)^{\top}$, on a $(\mathbf{I}-\mathbf{P})\mathbf{y}=(\tfrac13,\,\tfrac13,\,-\tfrac13)^{\top}$, le résidu de la section précédente.
::::

⁠**En bref :** Le supplémentaire orthogonal $\mathcal U^\perp$ contient tous les vecteurs perpendiculaires à $\mathcal U$ ; tout vecteur se décompose de façon unique en une partie dans $\mathcal U$ et une partie dans $\mathcal U^\perp$, et la somme des deux dimensions vaut $n$.

### Le procédé de Gram-Schmidt

<span class="anker" id="stufe-4-5"></span>

Des colonnes orthonormées simplifient tout, mais on dispose en général de colonnes quelconques. Le procédé de Gram-Schmidt construit, à partir de vecteurs linéairement indépendants $\mathbf{a}_1,\dots,\mathbf{a}_k$, des vecteurs orthonormés $\mathbf{q}_1,\dots,\mathbf{q}_k$ qui engendrent le même sous-espace.

La Fig. [11](#abb-11) montre l’idée pour deux vecteurs. On normalise le premier. Du second, on retranche son ombre sur le premier, c’est-à-dire sa projection. Ce qui reste est perpendiculaire au premier, et on le normalise. Pour le troisième vecteur, on retranche les ombres sur les deux vecteurs déjà trouvés, et ainsi de suite.

:::abbildung ml/k2gramschmidt 11
Le procédé de Gram-Schmidt pour $\mathbf{a}_1=(2,1)^{\top}$ et $\mathbf{a}_2=(1,2)^{\top}$. On normalise d’abord $\mathbf{a}_1$ : $\mathbf{q}_1=\mathbf{a}_1/\sqrt5$. Du second vecteur, on retranche son ombre $(\mathbf{q}_1^{\top}\mathbf{a}_2)\,\mathbf{q}_1=(1{,}6;\,0{,}8)^{\top}$ (en bleu). Le reste $\tilde{\mathbf{q}}_2=(-0{,}6;\,1{,}2)^{\top}$ (en orange, parallèle à la perpendiculaire en tirets) est perpendiculaire à $\mathbf{q}_1$ ; normalisé, il donne $\mathbf{q}_2=(-1,2)^{\top}/\sqrt5$.
:::

:::definition Définition 4.7 (Procédé de Gram-Schmidt)
<span class="anker" id="satz-4-7"></span>

On donne des vecteurs linéairement indépendants $\mathbf{a}_1,\dots,\mathbf{a}_k\in\mathbb{R}^n$. Le __procédé de Gram-Schmidt__ calcule successivement, pour $i=1,\dots,k$,

<span class="anker" id="gl-4-4"></span>
$$\tilde{\mathbf{q}}_i=\mathbf{a}_i-\sum_{l=1}^{i-1}(\mathbf{q}_l^{\top}\mathbf{a}_i)\,\mathbf{q}_l,\qquad \mathbf{q}_i=\frac{\tilde{\mathbf{q}}_i}{\lVert\tilde{\mathbf{q}}_i\rVert} . \tag{4.4}$$
:::

Pour $i=1$, la somme est vide, donc $\tilde{\mathbf{q}}_1=\mathbf{a}_1$. D’après [(4.2)](#gl-4-2), la somme est la projection de $\mathbf{a}_i$ sur le sous-espace engendré par les vecteurs déjà trouvés ; $\tilde{\mathbf{q}}_i$ est le résidu de cette projection.

:::satz Théorème 4.8 (Ce que fournit Gram-Schmidt)
<span class="anker" id="satz-4-8"></span>

Les vecteurs $\mathbf{q}_1,\dots,\mathbf{q}_k$ sont orthonormés, et pour tout $i$, les vecteurs $\mathbf{q}_1,\dots,\mathbf{q}_i$ engendrent le même sous-espace que $\mathbf{a}_1,\dots,\mathbf{a}_i$.
:::

:::beweis Gram-Schmidt
On procède pas à pas. Supposons que $\mathbf{q}_1,\dots,\mathbf{q}_{i-1}$ soient déjà orthonormés et engendrent le même sous-espace que $\mathbf{a}_1,\dots,\mathbf{a}_{i-1}$. Alors $\tilde{\mathbf{q}}_i$ est le résidu de la projection de $\mathbf{a}_i$ sur ce sous-espace et est donc perpendiculaire à $\mathbf{q}_1,\dots,\mathbf{q}_{i-1}$ ; par un calcul direct, $\mathbf{q}_l^{\top}\tilde{\mathbf{q}}_i=\mathbf{q}_l^{\top}\mathbf{a}_i-\mathbf{q}_l^{\top}\mathbf{a}_i=0$. On a $\tilde{\mathbf{q}}_i\ne\mathbf{0}$, car sinon $\mathbf{a}_i$ serait une combinaison linéaire de $\mathbf{q}_1,\dots,\mathbf{q}_{i-1}$, et donc de $\mathbf{a}_1,\dots,\mathbf{a}_{i-1}$, ce qui contredirait l’indépendance. On peut donc normaliser. Enfin, $\mathbf{a}_i=\tilde{\mathbf{q}}_i+\sum_l(\mathbf{q}_l^{\top}\mathbf{a}_i)\mathbf{q}_l$ est une combinaison linéaire de $\mathbf{q}_1,\dots,\mathbf{q}_i$, et inversement $\mathbf{q}_i$ est une combinaison linéaire de $\mathbf{a}_i$ et de $\mathbf{q}_1,\dots,\mathbf{q}_{i-1}$. Les deux listes engendrent donc le même sous-espace.
:::

Si les vecteurs donnés sont malgré tout dépendants, le procédé s’en aperçoit de lui-même : à un moment donné, $\tilde{\mathbf{q}}_i=\mathbf{0}$, et l’on ne peut pas normaliser.

::::beispiel [Exemple de calcul]
Pour les colonnes de $\mathbf{H}$, $\mathbf{a}_1=(1,\,0,\,1)^{\top}$ et $\mathbf{a}_2=(0,\,1,\,1)^{\top}$, on a $\mathbf{q}_1=\mathbf{a}_1/\sqrt2$. Ensuite, $\mathbf{q}_1^{\top}\mathbf{a}_2=1/\sqrt2$ et

$$\tilde{\mathbf{q}}_2=\mathbf{a}_2-\frac1{\sqrt2}\,\mathbf{q}_1=(0,\,1,\,1)^{\top}-\tfrac12(1,\,0,\,1)^{\top}=\bigl(-\tfrac12,\,1,\,\tfrac12\bigr)^{\top},\qquad \lVert\tilde{\mathbf{q}}_2\rVert=\sqrt{\tfrac14+1+\tfrac14}=\sqrt{\tfrac32} .$$

Une fois normalisé, $\mathbf{q}_2=\tfrac1{\sqrt6}(-1,\,2,\,1)^{\top}$, exactement la base orthonormée de l’exemple de calcul associé à [(4.2)](#gl-4-2). La Fig. [12](#abb-12) montre les deux sommes de cet exemple de calcul.

:::abbildung ml/k2rgs 12
Gram-Schmidt pour les colonnes de $\mathbf{H}$ : le produit scalaire $\mathbf{q}_1^{\top}\mathbf{a}_2$ avec $\mathbf{q}_1=(1,0,1)^{\top}/\sqrt2$ et $\mathbf{a}_2=(0,1,1)^{\top}$, qui donne la longueur de l’ombre, et le carré de la longueur du reste $\tilde{\mathbf{q}}_2=(-\tfrac12,1,\tfrac12)^{\top}$.
:::
::::

⁠**En bref :** Gram-Schmidt retranche de chaque vecteur sa projection sur les vecteurs déjà trouvés et normalise le reste ; on obtient ainsi une base orthonormée du même sous-espace.

:::hintergrund Coût et erreurs d’arrondi
Pour $k$ vecteurs de $n$ composantes chacun, le procédé nécessite environ $2nk^2$ opérations arithmétiques : à l’étape $i$, il faut calculer $i-1$ produits scalaires et retrancher autant de multiples, chaque opération coûte environ $2n$, et la somme sur $i$ croît comme $k^2$. Avec des nombres arrondis, la version [(4.4)](#gl-4-4) est sensible : si deux des vecteurs donnés sont presque parallèles, $\tilde{\mathbf{q}}_i$ est une petite différence de grands nombres, et les $\mathbf{q}_i$ calculés ne sont alors plus exactement orthogonaux. Un ordre légèrement modifié des étapes de calcul, le procédé de Gram-Schmidt modifié, retranche les ombres une à une du reste déjà réduit au lieu de les retrancher toutes du $\mathbf{a}_i$ initial. Avec des nombres exacts, il donne le même résultat ; avec des nombres arrondis, il est nettement plus précis. Les bibliothèques logicielles utilisent le plus souvent encore d’autres méthodes, qui travaillent avec des réflexions, c’est-à-dire avec des matrices orthogonales.
:::

### La décomposition QR

<span class="anker" id="stufe-4-6"></span>

Le procédé de Gram-Schmidt peut s’écrire comme une décomposition de matrice. D’après la preuve ci-dessus, chaque vecteur $\mathbf{a}_i$ est une combinaison linéaire de $\mathbf{q}_1,\dots,\mathbf{q}_i$, à savoir

$$\mathbf{a}_i=\sum_{l=1}^{i-1}(\mathbf{q}_l^{\top}\mathbf{a}_i)\,\mathbf{q}_l+\lVert\tilde{\mathbf{q}}_i\rVert\,\mathbf{q}_i .$$

Seuls les $i$ premiers vecteurs $\mathbf{q}_l$ y figurent, pas les suivants. Si l’on écrit les coefficients en colonnes d’une matrice, on obtient donc une matrice triangulaire.

:::definition Définition 4.9 (Décomposition QR)
<span class="anker" id="satz-4-9"></span>

Si $\mathbf{A}\in\mathbb{R}^{m\times n}$ a des colonnes linéairement indépendantes, la __décomposition QR__ est l’écriture

<span class="anker" id="gl-4-5"></span>
$$\mathbf{A}=\mathbf{Q}\mathbf{R} \tag{4.5}$$

avec une matrice $\mathbf{Q}\in\mathbb{R}^{m\times n}$ à colonnes orthonormées et une matrice triangulaire supérieure $\mathbf{R}\in\mathbb{R}^{n\times n}$ à coefficients diagonaux positifs. On a $r_{li}=\mathbf{q}_l^{\top}\mathbf{a}_i$ pour $l<i$ et $r_{ii}=\lVert\tilde{\mathbf{q}}_i\rVert$.
:::

Une matrice triangulaire supérieure n’a que des zéros sous la diagonale. D’après la vue par colonnes, la colonne $i$ de $\mathbf{Q}\mathbf{R}$ est $\sum_lr_{li}\mathbf{q}_l$, c’est-à-dire exactement l’écriture de $\mathbf{a}_i$ ci-dessus. Les colonnes de $\mathbf{Q}$ sont fournies par le procédé de Gram-Schmidt, les coefficients de $\mathbf{R}$ s’obtiennent au passage. Comme $\mathbf{Q}$ a des colonnes orthonormées, on a de plus $\mathbf{R}=\mathbf{Q}^{\top}\mathbf{A}$.

::::beispiel [Exemple de calcul]
Pour $\mathbf{H}$, on a

$$\mathbf{Q}=\begin{pmatrix}\tfrac1{\sqrt2}&-\tfrac1{\sqrt6}\\0&\tfrac2{\sqrt6}\\\tfrac1{\sqrt2}&\tfrac1{\sqrt6}\end{pmatrix},\qquad \mathbf{R}=\begin{pmatrix}\sqrt2&\tfrac1{\sqrt2}\\0&\sqrt{\tfrac32}\end{pmatrix}\approx\begin{pmatrix}1{,}414&0{,}707\\0&1{,}225\end{pmatrix}.$$

Vérification de la deuxième colonne : $\tfrac1{\sqrt2}\cdot\tfrac1{\sqrt2}(1,\,0,\,1)^{\top}+\sqrt{\tfrac32}\cdot\tfrac1{\sqrt6}(-1,\,2,\,1)^{\top}=\tfrac12(1,\,0,\,1)^{\top}+\tfrac12(-1,\,2,\,1)^{\top}=(0,\,1,\,1)^{\top}=\mathbf{a}_2$.
::::

⁠**En bref :** La décomposition QR $\mathbf{A}=\mathbf{Q}\mathbf{R}$ écrit le procédé de Gram-Schmidt comme un produit matriciel : $\mathbf{Q}$ a des colonnes orthonormées, $\mathbf{R}$ est une matrice triangulaire supérieure.

### La meilleure solution approchée avec QR

<span class="anker" id="stufe-4-7"></span>

Avec la décomposition QR, on peut résoudre les équations normales sans calculer $\mathbf{A}^{\top}\mathbf{A}$. On substitue $\mathbf{A}=\mathbf{Q}\mathbf{R}$ et on utilise $\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}$.

:::satz Théorème 4.10 (Meilleure solution approchée avec QR)
<span class="anker" id="satz-4-10"></span>

Si $\mathbf{A}=\mathbf{Q}\mathbf{R}$ est la décomposition QR, la meilleure solution approchée de $\mathbf{A}\mathbf{x}=\mathbf{y}$ est la solution de

<span class="anker" id="gl-4-6"></span>
$$\mathbf{R}\hat{\mathbf{x}}=\mathbf{Q}^{\top}\mathbf{y} . \tag{4.6}$$
:::

:::beweis Résolution avec QR
On a $\mathbf{A}^{\top}\mathbf{A}=\mathbf{R}^{\top}\mathbf{Q}^{\top}\mathbf{Q}\mathbf{R}=\mathbf{R}^{\top}\mathbf{R}$ et $\mathbf{A}^{\top}\mathbf{y}=\mathbf{R}^{\top}\mathbf{Q}^{\top}\mathbf{y}$. Les équations normales s’écrivent donc $\mathbf{R}^{\top}\mathbf{R}\hat{\mathbf{x}}=\mathbf{R}^{\top}\mathbf{Q}^{\top}\mathbf{y}$. La matrice triangulaire $\mathbf{R}$ a des coefficients diagonaux positifs ; d’après le [chapitre 1, section 14.4](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/die-determinante.html#stufe-14-4), son déterminant est donc non nul, et elle est inversible ; il en va de même pour $\mathbf{R}^{\top}$. En multipliant à gauche par $(\mathbf{R}^{\top})^{-1}$, il reste [(4.6)](#gl-4-6).
:::

Le système [(4.6)](#gl-4-6) est triangulaire et se résout de bas en haut, comme la remontée à la fin de la méthode du pivot de Gauss du [chapitre 1, section 12.3](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/lineare-gleichungssysteme.html#stufe-12-3). Pour une matrice $m\times n$, l’ensemble du calcul coûte environ $2mn^2$ opérations arithmétiques, presque toutes pour la décomposition QR.

::::beispiel [Exemple de calcul]
Pour $\mathbf{H}$ et $\mathbf{y}=(1,\,1,\,1)^{\top}$, on a $\mathbf{Q}^{\top}\mathbf{y}=\bigl(\tfrac2{\sqrt2},\ \tfrac{-1+2+1}{\sqrt6}\bigr)^{\top}=\bigl(\sqrt2,\ \tfrac2{\sqrt6}\bigr)^{\top}$. La ligne du bas de [(4.6)](#gl-4-6) s’écrit $\sqrt{\tfrac32}\,\hat x_2=\tfrac2{\sqrt6}$, d’où $\hat x_2=\tfrac2{\sqrt6}\cdot\sqrt{\tfrac23}=\tfrac23$. La ligne du haut s’écrit $\sqrt2\,\hat x_1+\tfrac1{\sqrt2}\cdot\tfrac23=\sqrt2$, d’où $\hat x_1=1-\tfrac13=\tfrac23$. C’est la même solution qu’avec les équations normales. Les composantes de $\mathbf{Q}^{\top}\mathbf{y}$ sont les produits scalaires de la Fig. [13](#abb-13).

:::abbildung ml/k2rqr 13
Le second membre $\mathbf{Q}^{\top}\mathbf{y}$ du système triangulaire pour $\mathbf{y}=(1,1,1)^{\top}$, avec $\mathbf{q}_1=(1,0,1)^{\top}/\sqrt2$ et $\mathbf{q}_2=(-1,2,1)^{\top}/\sqrt6$.
:::
::::

⁠**En bref :** Avec $\mathbf{A}=\mathbf{Q}\mathbf{R}$, les équations normales deviennent le système triangulaire $\mathbf{R}\hat{\mathbf{x}}=\mathbf{Q}^{\top}\mathbf{y}$ ; la matrice $\mathbf{A}^{\top}\mathbf{A}$ n’est jamais formée.

:::aufgabe Exercice 11 ★ Gram-Schmidt et projection
<span class="anker" id="aufg-11"></span>

On donne $\mathbf{a}_1=(1,\,1,\,0)^{\top}$ et $\mathbf{a}_2=(1,\,0,\,1)^{\top}$.

<ol class="al">

<li>

Appliquez le procédé de Gram-Schmidt et vérifiez que $\mathbf{q}_1,\mathbf{q}_2$ sont orthonormés.

</li>

<li>

Calculez la matrice de projection $\mathbf{P}=\mathbf{q}_1\mathbf{q}_1^{\top}+\mathbf{q}_2\mathbf{q}_2^{\top}$ sur le plan engendré par $\mathbf{a}_1$ et $\mathbf{a}_2$, et projetez $\mathbf{y}=(1,\,2,\,3)^{\top}$.

</li>

<li>

Déterminez un vecteur qui engendre le supplémentaire orthogonal du plan, et vérifiez $\mathbf{I}-\mathbf{P}=\mathbf{k}\mathbf{k}^{\top}/(\mathbf{k}^{\top}\mathbf{k})$.

</li>

</ol>

:::loesung
(a) $\mathbf{q}_1=\mathbf{a}_1/\sqrt2=(1,\,1,\,0)^{\top}/\sqrt2$. On a ensuite $\mathbf{q}_1^{\top}\mathbf{a}_2=1/\sqrt2$ et

$$\tilde{\mathbf{q}}_2=\mathbf{a}_2-\tfrac1{\sqrt2}\,\mathbf{q}_1=(1,\,0,\,1)^{\top}-\tfrac12(1,\,1,\,0)^{\top}=\bigl(\tfrac12,\,-\tfrac12,\,1\bigr)^{\top},\qquad \lVert\tilde{\mathbf{q}}_2\rVert^2=\tfrac14+\tfrac14+1=\tfrac32 ,$$

donc $\mathbf{q}_2=\tilde{\mathbf{q}}_2/\sqrt{3/2}=(1,\,-1,\,2)^{\top}/\sqrt6$. Vérification : $\mathbf{q}_1^{\top}\mathbf{q}_2=(1-1+0)/\sqrt{12}=0$, $\lVert\mathbf{q}_2\rVert^2=\tfrac{1+1+4}6=1$.

(b)

$$\mathbf{P}=\frac12\begin{pmatrix}1&1&0\\1&1&0\\0&0&0\end{pmatrix}+\frac16\begin{pmatrix}1&-1&2\\-1&1&-2\\2&-2&4\end{pmatrix}=\frac13\begin{pmatrix}2&1&1\\1&2&-1\\1&-1&2\end{pmatrix},$$

$$\mathbf{P}\mathbf{y}=\frac13\begin{pmatrix}2+2+3\\1+4-3\\1-2+6\end{pmatrix}=\begin{pmatrix}7/3\\2/3\\5/3\end{pmatrix}.$$

(c) On cherche $\mathbf{k}$ tel que $\mathbf{a}_1^{\top}\mathbf{k}=k_1+k_2=0$ et $\mathbf{a}_2^{\top}\mathbf{k}=k_1+k_3=0$, donc $\mathbf{k}=(1,\,-1,\,-1)^{\top}$ ou un multiple. On a $\mathbf{k}^{\top}\mathbf{k}=3$ et

$$\mathbf{I}-\mathbf{P}=\frac13\begin{pmatrix}1&-1&-1\\-1&1&1\\-1&1&1\end{pmatrix}=\frac{\mathbf{k}\mathbf{k}^{\top}}{\mathbf{k}^{\top}\mathbf{k}} .$$

Le supplémentaire orthogonal du plan est la droite de direction $\mathbf{k}$, de dimension $3-2=1$. Pour contrôle : $\mathbf{y}-\mathbf{P}\mathbf{y}=(-\tfrac43,\,\tfrac43,\,\tfrac43)^{\top}=-\tfrac43\mathbf{k}$ appartient à cette droite.
:::
:::

:::aufgabe Exercice 12 ★★ Résoudre avec QR
<span class="anker" id="aufg-12"></span>

Utilisez la matrice $\mathbf{A}$ de colonnes $\mathbf{a}_1$ et $\mathbf{a}_2$ de l’exercice [11](#aufg-11).

<ol class="al">

<li>

Donnez la décomposition QR et vérifiez $\mathbf{Q}\mathbf{R}=\mathbf{A}$.

</li>

<li>

Résolvez $\mathbf{A}\mathbf{x}=(1,\,2,\,3)^{\top}$ au sens des moindres carrés avec [(4.6)](#gl-4-6) et, pour contrôle, avec les équations normales.

</li>

</ol>

:::loesung
(a) D’après l’exercice [11](#aufg-11) : $\mathbf{q}_1=(1,\,1,\,0)^{\top}/\sqrt2$, $\mathbf{q}_2=(1,\,-1,\,2)^{\top}/\sqrt6$, $r_{11}=\lVert\mathbf{a}_1\rVert=\sqrt2$, $r_{12}=\mathbf{q}_1^{\top}\mathbf{a}_2=1/\sqrt2$, $r_{22}=\lVert\tilde{\mathbf{q}}_2\rVert=\sqrt{3/2}$ :

$$\mathbf{Q}=\begin{pmatrix}1/\sqrt2&1/\sqrt6\\1/\sqrt2&-1/\sqrt6\\0&2/\sqrt6\end{pmatrix},\qquad \mathbf{R}=\begin{pmatrix}\sqrt2&1/\sqrt2\\0&\sqrt{3/2}\end{pmatrix}.$$

Vérification : la colonne 1 de $\mathbf{Q}\mathbf{R}$ est $\sqrt2\,\mathbf{q}_1=\mathbf{a}_1$ ; la colonne 2 est $\tfrac1{\sqrt2}\mathbf{q}_1+\sqrt{\tfrac32}\,\mathbf{q}_2=\tfrac12(1,\,1,\,0)^{\top}+\tfrac12(1,\,-1,\,2)^{\top}=(1,\,0,\,1)^{\top}=\mathbf{a}_2$, car $\sqrt{3/2}/\sqrt6=\tfrac12$.

(b) $\mathbf{Q}^{\top}\mathbf{y}=\bigl(\tfrac3{\sqrt2},\ \tfrac{1-2+6}{\sqrt6}\bigr)^{\top}=\bigl(\tfrac3{\sqrt2},\ \tfrac5{\sqrt6}\bigr)^{\top}$. La ligne du bas de $\mathbf{R}\hat{\mathbf{x}}=\mathbf{Q}^{\top}\mathbf{y}$ donne $\hat x_2=\tfrac5{\sqrt6}\cdot\sqrt{\tfrac23}=\tfrac53$, celle du haut $\sqrt2\,\hat x_1+\tfrac1{\sqrt2}\cdot\tfrac53=\tfrac3{\sqrt2}$, soit, après multiplication par $\sqrt2$, $2\hat x_1+\tfrac53=3$, donc $\hat x_1=\tfrac23$. Contrôle avec les équations normales : $\mathbf{A}^{\top}\mathbf{A}=\bigl(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr)$, $\mathbf{A}^{\top}\mathbf{y}=(3,\,4)^{\top}$, $\hat{\mathbf{x}}=\tfrac13\bigl(\begin{smallmatrix}2&-1\\-1&2\end{smallmatrix}\bigr)(3,\,4)^{\top}=(\tfrac23,\,\tfrac53)^{\top}$. De plus, $\mathbf{A}\hat{\mathbf{x}}=(\tfrac73,\,\tfrac23,\,\tfrac53)^{\top}=\mathbf{P}\mathbf{y}$, le résultat de l’exercice [11](#aufg-11).
:::
:::

:::aufgabe Exercice 13 ★★ Supplémentaires orthogonaux
<span class="anker" id="aufg-13"></span>

<ol class="al">

<li>

Quelle est la dimension du supplémentaire orthogonal d’une droite passant par l’origine dans $\mathbb{R}^3$ ? Et celle du supplémentaire d’une droite dans $\mathbb{R}^5$ ?

</li>

<li>

Montrez que $(\mathcal U^\perp)^\perp=\mathcal U$. Indication : montrez d’abord que tout vecteur de $\mathcal U$ appartient à $(\mathcal U^\perp)^\perp$. Décomposez ensuite un vecteur $\mathbf{y}\in(\mathcal U^\perp)^\perp$ comme dans le théorème de la section [4.4](#stufe-4-4), et formez le produit scalaire avec sa partie dans $\mathcal U^\perp$.

</li>

</ol>

:::loesung
(a) D’après le théorème de la section [4.4](#stufe-4-4), $\dim\mathcal U^\perp=n-\dim\mathcal U$ : dans $\mathbb{R}^3$, on obtient donc $3-1=2$, un plan ; dans $\mathbb{R}^5$, $5-1=4$.

(b) Première partie : si $\mathbf{u}\in\mathcal U$, alors $\mathbf{u}^{\top}\mathbf{z}=0$ pour tout $\mathbf{z}\in\mathcal U^\perp$, d’après la définition de $\mathcal U^\perp$. Donc $\mathbf{u}$ est perpendiculaire à $\mathcal U^\perp$ tout entier et appartient à $(\mathcal U^\perp)^\perp$. Seconde partie : soit $\mathbf{y}\in(\mathcal U^\perp)^\perp$. D’après le théorème, on décompose $\mathbf{y}=\mathbf{u}+\mathbf{z}$ avec $\mathbf{u}\in\mathcal U$ et $\mathbf{z}\in\mathcal U^\perp$. Alors $\mathbf{z}^{\top}\mathbf{y}=0$, car $\mathbf{y}$ est perpendiculaire à $\mathcal U^\perp$, et $\mathbf{z}^{\top}\mathbf{u}=0$, car $\mathbf{z}$ est perpendiculaire à $\mathcal U$. Donc $\mathbf{z}^{\top}\mathbf{z}=\mathbf{z}^{\top}\mathbf{y}-\mathbf{z}^{\top}\mathbf{u}=0$, et $\mathbf{z}=\mathbf{0}$. Ainsi, $\mathbf{y}=\mathbf{u}\in\mathcal U$. Chacun des deux ensembles contient l’autre ; ils sont égaux.
:::
:::

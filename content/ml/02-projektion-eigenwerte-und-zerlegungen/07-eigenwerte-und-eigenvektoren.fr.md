---
title: Valeurs propres et vecteurs propres
pfad: Informatique / Apprentissage automatique / Fondements mathématiques / Projection, valeurs propres et décompositions
knoten: Fondements 2 : Projection, valeurs propres et décompositions
nachschlagen: ja
order: 15220700
summary: Une matrice fait à la fois tourner et étire la plupart des vecteurs.
tags: conjugué, vecteur propre, valeur propre, polynôme caractéristique, sous-espace propre, trace, multiplicité algébrique, multiplicité géométrique
lang: fr
---

<span class="anker" id="stufe-6"></span>

:::zweck
Une matrice fait à la fois tourner et étire la plupart des vecteurs. Mais il existe des directions qu’elle ne fait pas tourner : une flèche dans une telle direction est seulement allongée, raccourcie ou retournée. Cette section trouve ces directions et les facteurs d’étirement qui leur correspondent. Ce sont les axes naturels d’une matrice.
:::

### Ce dont vous avez besoin : nombres complexes

<span class="anker" id="stufe-6-1"></span>

La recherche des facteurs d’étirement mène à des équations polynomiales, et toutes n’ont pas de solutions réelles. Cette sous-section rassemble ce que ce chapitre utilise sur les nombres complexes.

**Nombres complexes.** Un nombre complexe $z=x+\mathrm j\,y$ se compose de la partie réelle $x$ et de la partie imaginaire $y$, deux nombres réels. L’unité imaginaire vérifie $\mathrm j^2=-1$. L’électrotechnique écrit $\mathrm j$ au lieu de $i$, car $i$ est déjà réservé au courant.

**Conjugué et module.** Le __conjugué__ de $z$ est le nombre $z^*=x-\mathrm j\,y$. On a $z\,z^*=x^2+y^2=|z|^2$, le carré du module, un nombre réel qui n’est nul que pour $z=0$. Un nombre est réel si et seulement si $z=z^*$. La conjugaison est compatible avec la somme et le produit : $(z+w)^*=z^*+w^*$ et $(zw)^*=z^*w^*$. Pour un vecteur $\mathbf{v}$ à composantes complexes, $\mathbf{v}^*$ désigne dans ce chapitre le vecteur des composantes conjuguées, non transposé. On a alors

$$(\mathbf{v}^*)^{\top}\mathbf{v}=\sum_i|v_i|^2>0\qquad\text{pour }\mathbf{v}\ne\mathbf{0} .$$

**La formule d’Euler.** Pour tout nombre réel $\alpha$, $\mathrm e^{\mathrm j\alpha}=\cos\alpha+\mathrm j\sin\alpha$ ; c’est un point du cercle unité du plan complexe, de module $1$.

**Racines des polynômes.** Tout polynôme de degré $n\ge1$ à coefficients réels ou complexes a exactement $n$ racines complexes, si l’on compte les racines multiples avec leur multiplicité, et se décompose en $n$ facteurs linéaires. Si le polynôme est à coefficients réels et si $z$ est une racine, alors $z^*$ en est une aussi : les racines non réelles vont par paires.

⁠**Exemple de calcul :** D’après la formule de résolution de l’équation du second degré, $\lambda^2-1{,}2\lambda+1=0$ a pour racines $\lambda=0{,}6\pm\sqrt{0{,}36-1}=0{,}6\pm\mathrm j\,0{,}8$, une paire de nombres conjugués de module $\sqrt{0{,}36+0{,}64}=1$. Pour $\mathbf{v}=(1,\,-\mathrm j)^{\top}$, on a $\mathbf{v}^*=(1,\,\mathrm j)^{\top}$ et $(\mathbf{v}^*)^{\top}\mathbf{v}=1\cdot1+\mathrm j\cdot(-\mathrm j)=1+1=2$ (Fig. [16](#abb-16)).

:::abbildung ml/k2rkomplex 16
Le produit scalaire $(\mathbf{v}^*)^{\top}\mathbf{v}$ pour $\mathbf{v}=(1,-\mathrm j)^{\top}$ : chaque terme vaut $v_i^*v_i=|v_i|^2$, car $\mathrm j\cdot(-\mathrm j)=-\mathrm j^2=1$.
:::

⁠**En bref :** Les nombres complexes $x+\mathrm jy$ avec $\mathrm j^2=-1$ résolvent toute équation polynomiale ; la conjugaison change le signe de la partie imaginaire, et $zz^*=|z|^2$ est réel.

### Vecteurs propres et valeurs propres

<span class="anker" id="stufe-6-2"></span>

Dans Fondements 1, section 8.3, des matrices faisaient tourner, étiraient et cisaillaient la grille du plan. Ce faisant, la plupart des flèches changent de direction. Mais pour certaines matrices, il existe des directions dans lesquelles une flèche reste sur sa droite passant par l’origine : elle est seulement étirée, comprimée ou retournée (Fig. [17](#abb-17)).

:::abbildung ml/k2eigen 17
La matrice $\mathbf{A}=\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$ envoie le cercle unité (en gris) sur une ellipse (en bleu). La flèche $\mathbf{v}_1=(1,1)^{\top}/\sqrt2$ (en rouge) reste sur sa droite et est étirée d’un facteur cinq, la flèche $\mathbf{v}_2=(1,-2)^{\top}/\sqrt5$ (en vert) d’un facteur deux ; leurs images sont dessinées en clair. Les droites grises sont les deux directions propres. Le vecteur unitaire $\mathbf{e}_1$, en revanche, est envoyé sur $(4,2)^{\top}$ (en tirets) et change de direction.
:::

:::definition Définition 6.1 (Vecteur propre, valeur propre)
<span class="anker" id="satz-6-1"></span>

Soit $\mathbf{A}\in\mathbb{R}^{n\times n}$. Un vecteur $\mathbf{v}\ne\mathbf{0}$ est appelé __vecteur propre__ de $\mathbf{A}$ s’il existe un nombre $\lambda$ tel que

<span class="anker" id="gl-6-1"></span>
$$\mathbf{A}\mathbf{v}=\lambda\,\mathbf{v} . \tag{6.1}$$

Le nombre $\lambda$ est appelé la __valeur propre__ associée.
:::

Le vecteur nul est exclu, car $\mathbf{A}\mathbf{0}=\lambda\mathbf{0}$ vaut pour tout nombre $\lambda$ et ne révèle rien. La valeur propre, en revanche, peut être nulle : le vecteur propre est alors envoyé sur $\mathbf{0}$. Une valeur propre négative retourne la flèche. Dans ce chapitre, les valeurs propres sont notées $\lambda$ ou $\lambda_i$. Le mot vient de l’allemand (*eigen* signifie « propre »), et l’anglais l’emploie aussi : *eigenvalue*, *eigenvector*.

⁠**Exemple de calcul :** Pour $\mathbf{A}=\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$, on a

$$\mathbf{A}\begin{pmatrix}1\\1\end{pmatrix}=\begin{pmatrix}5\\5\end{pmatrix}=5\begin{pmatrix}1\\1\end{pmatrix},\qquad \mathbf{A}\begin{pmatrix}1\\-2\end{pmatrix}=\begin{pmatrix}2\\-4\end{pmatrix}=2\begin{pmatrix}1\\-2\end{pmatrix},\qquad \mathbf{A}\begin{pmatrix}1\\0\end{pmatrix}=\begin{pmatrix}4\\2\end{pmatrix}.$$

Donc $(1,\,1)^{\top}$ est un vecteur propre associé à la valeur propre $5$, et $(1,\,-2)^{\top}$ un vecteur propre associé à la valeur propre $2$. Le vecteur $(1,\,0)^{\top}$ n’en est pas un, car $(4,\,2)^{\top}$ n’est pas un multiple de lui.

⁠**En bref :** Un vecteur propre n’est pas tourné par la matrice, mais seulement multiplié par un nombre ; ce nombre est la valeur propre.

:::hintergrund Les fonctions propres, vous les connaissez déjà
En signaux et systèmes, on rencontre la même idée pour des fonctions au lieu de vecteurs. Un système LTI de réponse impulsionnelle $h(t)$ répond à la fonction exponentielle $\mathrm e^{pt}$ de fréquence complexe $p$, notée $s$ dans beaucoup d’ouvrages, par

$$\int_{-\infty}^{\infty}h(\tau)\,\mathrm e^{p(t-\tau)}\,\mathrm{d}\tau=H(p)\,\mathrm e^{pt},\qquad H(p)=\int_{-\infty}^{\infty}h(\tau)\,\mathrm e^{-p\tau}\,\mathrm{d}\tau ,$$

pour tous les $p$ pour lesquels l’intégrale existe. La forme de l’entrée est conservée, seul un facteur numérique s’y ajoute : $\mathrm e^{pt}$ est une fonction propre du système, et la valeur propre est la valeur $H(p)$ de la fonction de transfert. L’équation [(6.1)](#gl-6-1) dit la même chose pour une matrice. Un système LTI est une application linéaire de signaux vers des signaux, une matrice une application linéaire de vecteurs vers des vecteurs ; dans les deux cas, il existe des entrées qui sont seulement multipliées par un nombre.
:::

### Le polynôme caractéristique

<span class="anker" id="stufe-6-3"></span>

Comment trouver des valeurs propres sans les deviner ? On réécrit [(6.1)](#gl-6-1) de façon que tout soit du même côté : $\mathbf{A}\mathbf{v}-\lambda\mathbf{v}=\mathbf{0}$, c’est-à-dire $(\mathbf{A}-\lambda\mathbf{I})\mathbf{v}=\mathbf{0}$. On cherche un $\lambda$ pour lequel ce système homogène a une solution $\mathbf{v}\ne\mathbf{0}$. D’après Fondements 1, section 11.5, cela signifie que la matrice $\mathbf{A}-\lambda\mathbf{I}$ n’est pas inversible. D’après Fondements 1, section 14.6, c’est le cas si et seulement si son déterminant est nul.

:::definition Définition 6.2 (Polynôme caractéristique)
<span class="anker" id="satz-6-2"></span>

Pour $\mathbf{A}\in\mathbb{R}^{n\times n}$, on appelle

<span class="anker" id="gl-6-2"></span>
$$p(\lambda)=\det(\mathbf{A}-\lambda\mathbf{I}) \tag{6.2}$$

le __polynôme caractéristique__ de $\mathbf{A}$.
:::

:::satz Théorème 6.3 (Les valeurs propres sont les racines)
<span class="anker" id="satz-6-3"></span>

Un nombre $\lambda$ est une valeur propre de $\mathbf{A}$ si et seulement si $p(\lambda)=0$.
:::

Le polynôme caractéristique est de degré $n$. Pour une matrice $2\times2$, il vaut

<span class="anker" id="gl-6-3"></span>
$$\det\begin{pmatrix}a-\lambda&b\\c&d-\lambda\end{pmatrix}=(a-\lambda)(d-\lambda)-bc=\lambda^2-(a+d)\,\lambda+(ad-bc) . \tag{6.3}$$

D’après la sous-section sur les nombres complexes, il a exactement $n$ racines complexes, comptées avec leur multiplicité. Une matrice $n\times n$ a donc $n$ valeurs propres, si l’on admet les valeurs complexes et que l’on compte les valeurs multiples avec leur multiplicité.

⁠**Exemple de calcul :** Pour $\mathbf{A}=\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$, on a $p(\lambda)=\lambda^2-7\lambda+(12-2)=\lambda^2-7\lambda+10=(\lambda-5)(\lambda-2)$. Les valeurs propres sont $5$ et $2$, comme dans la sous-section précédente. Pour la matrice diagonale $\operatorname{diag}(3;\,-1)$, on a $p(\lambda)=(3-\lambda)(-1-\lambda)$, de racines $3$ et $-1$ : les valeurs propres d’une matrice diagonale sont sur sa diagonale, les vecteurs propres sont les vecteurs unitaires.

⁠**En bref :** Les valeurs propres sont les racines du polynôme caractéristique $\det(\mathbf{A}-\lambda\mathbf{I})$ ; une matrice $n\times n$ a $n$ valeurs propres, comptées avec leur multiplicité et dans les complexes.

### Calculer les vecteurs propres

<span class="anker" id="stufe-6-4"></span>

Lorsqu’une valeur propre $\lambda$ est connue, les vecteurs propres associés sont les solutions $\mathbf{v}\ne\mathbf{0}$ du système homogène $(\mathbf{A}-\lambda\mathbf{I})\mathbf{v}=\mathbf{0}$. On les trouve avec la méthode du pivot de Gauss. Avec $\mathbf{v}$, tout multiple $c\,\mathbf{v}$ avec $c\ne0$ est aussi un vecteur propre, car $\mathbf{A}(c\mathbf{v})=c\lambda\mathbf{v}=\lambda(c\mathbf{v})$. Un vecteur propre n’est donc jamais unique ; seule sa direction l’est, et parfois même pas elle.

:::definition Définition 6.4 (Sous-espace propre)
<span class="anker" id="satz-6-4"></span>

Le noyau de $\mathbf{A}-\lambda\mathbf{I}$ est appelé le __sous-espace propre__ de $\mathbf{A}$ associé à la valeur propre $\lambda$.
:::

Il contient tous les vecteurs propres associés à $\lambda$ ainsi que le vecteur nul. En tant que noyau, c’est un sous-espace au sens de la section [4.1](projektion-auf-einen-unterraum.html#stufe-4-1).

⁠**Exemple de calcul :** Pour $\mathbf{A}=\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$ et $\lambda=5$, on a

$$\mathbf{A}-5\mathbf{I}=\begin{pmatrix}-1&1\\2&-2\end{pmatrix}.$$

Les deux lignes exigent la même chose : $-v_1+v_2=0$. Le sous-espace propre est la droite de tous les multiples de $(1,\,1)^{\top}$. Pour $\lambda=2$, on a $\mathbf{A}-2\mathbf{I}=\bigl(\begin{smallmatrix}2&1\\2&1\end{smallmatrix}\bigr)$ avec la condition $2v_1+v_2=0$ ; le sous-espace propre est la droite de direction $(1,\,-2)^{\top}$. Normalisés, les vecteurs propres sont $\mathbf{v}_1=(1,\,1)^{\top}/\sqrt2$ et $\mathbf{v}_2=(1,\,-2)^{\top}/\sqrt5$, comme dans la Fig. [17](#abb-17). Ils ne sont pas perpendiculaires : $(1,\,1)(1,\,-2)^{\top}=-1\ne0$.

⁠**En bref :** Les vecteurs propres associés à $\lambda$ sont les solutions $\mathbf{v}\ne\mathbf{0}$ de $(\mathbf{A}-\lambda\mathbf{I})\mathbf{v}=\mathbf{0}$ ; avec le vecteur nul, ils forment le sous-espace propre.

### Trace et déterminant

<span class="anker" id="stufe-6-5"></span>

Dans [(6.3)](#gl-6-3) figurent deux nombres que l’on lit directement sur la matrice : $ad-bc$ est le déterminant, et $a+d$ est la somme des coefficients diagonaux. Cette somme porte un nom à elle. Les deux nombres sont liés de façon simple aux valeurs propres et servent donc de vérification.

:::definition Définition 6.5 (Trace)
<span class="anker" id="satz-6-5"></span>

La __trace__ d’une matrice carrée $\mathbf{A}\in\mathbb{R}^{n\times n}$ est la somme de ses coefficients diagonaux :

<span class="anker" id="gl-6-4"></span>
$$\operatorname{tr}\mathbf{A}=a_{11}+a_{22}+\dots+a_{nn}=\sum_{i=1}^na_{ii} . \tag{6.4}$$
:::

:::satz Théorème 6.6 (Trace et déterminant à partir des valeurs propres)
<span class="anker" id="satz-6-6"></span>

Si $\lambda_1,\dots,\lambda_n$ sont les valeurs propres de $\mathbf{A}$, comptées avec leur multiplicité et dans les complexes, alors

<span class="anker" id="gl-6-5"></span>
$$\operatorname{tr}\mathbf{A}=\lambda_1+\lambda_2+\dots+\lambda_n,\qquad \det\mathbf{A}=\lambda_1\cdot\lambda_2\cdots\lambda_n . \tag{6.5}$$

De plus, $\operatorname{tr}(\mathbf{A}\mathbf{B})=\operatorname{tr}(\mathbf{B}\mathbf{A})$ pour $\mathbf{A}\in\mathbb{R}^{m\times n}$ et $\mathbf{B}\in\mathbb{R}^{n\times m}$.
:::

:::herleitung Trace et déterminant
Pour $n=2$ : le polynôme $\lambda^2-(a+d)\lambda+(ad-bc)$ se factorise en $(\lambda-\lambda_1)(\lambda-\lambda_2)=\lambda^2-(\lambda_1+\lambda_2)\lambda+\lambda_1\lambda_2$. En comparant les coefficients, on obtient $a+d=\lambda_1+\lambda_2$ et $ad-bc=\lambda_1\lambda_2$.

Pour $n$ quelconque, $p(\lambda)$ se factorise de même en $(\lambda_1-\lambda)(\lambda_2-\lambda)\cdots(\lambda_n-\lambda)$ ; le signe est correct, car le terme $(-\lambda)^n$ apparaît dans $\det(\mathbf{A}-\lambda\mathbf{I})$. Pour $\lambda=0$, on obtient à gauche $\det\mathbf{A}$ et à droite $\lambda_1\cdots\lambda_n$. Pour la trace, on compare les coefficients de $\lambda^{n-1}$. À droite, ils valent $(-1)^{n-1}(\lambda_1+\dots+\lambda_n)$. À gauche, dans le développement de Laplace, seul le produit des coefficients diagonaux $(a_{11}-\lambda)\cdots(a_{nn}-\lambda)$ fournit une puissance de $\lambda$ aussi élevée, avec le coefficient $(-1)^{n-1}(a_{11}+\dots+a_{nn})$.

Pour le dernier énoncé : $\operatorname{tr}(\mathbf{A}\mathbf{B})=\sum_i(\mathbf{A}\mathbf{B})_{ii}=\sum_i\sum_la_{il}b_{li}$ et $\operatorname{tr}(\mathbf{B}\mathbf{A})=\sum_l\sum_ib_{li}a_{il}$. C’est la même double somme, simplement ordonnée autrement.
:::

⁠**Exemple de calcul :** Pour $\mathbf{A}=\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$, on a $\operatorname{tr}\mathbf{A}=7=5+2$ (Fig. [18](#abb-18)) et $\det\mathbf{A}=10=5\cdot2$. Pour $\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$, on a $\operatorname{tr}=7$ et $\det=6$ ; les valeurs propres sont donc les solutions de $\lambda^2-7\lambda+6=0$, à savoir $6$ et $1$. Pour $\mathbf{A}\in\mathbb{R}^{2\times3}$ de lignes $(1,0,2)$, $(0,1,1)$ et $\mathbf{B}=\mathbf{A}^{\top}$, la matrice $\mathbf{A}\mathbf{B}=\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ a pour trace $7$, et $\mathbf{B}\mathbf{A}$ est une matrice $3\times3$ de coefficients diagonaux $1$, $1$ et $5$, elle aussi de trace $7$.

:::abbildung ml/k2rspur 18
La trace de $\mathbf{A}=\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$ comme somme des coefficients diagonaux ; elle est égale à la somme des valeurs propres $5$ et $2$.
:::

⁠**En bref :** La trace est la somme des coefficients diagonaux et la somme des valeurs propres ; le déterminant est le produit des valeurs propres.

### Valeurs propres complexes

<span class="anker" id="stufe-6-6"></span>

Une rotation de $90^\circ$ ne laisse aucune flèche sur sa droite : chacune est tournée d’un angle droit. Elle ne peut donc pas avoir de vecteur propre réel. Le polynôme caractéristique montre ce qui se passe à la place.

⁠**Exemple de calcul 1 :** Pour la rotation $\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)$, on a $p(\lambda)=\lambda^2+1$, de racines $\lambda=\mathrm j$ et $\lambda=-\mathrm j$. Les valeurs propres sont imaginaires pures. À $\lambda=\mathrm j$ est associé le vecteur propre complexe $(1,\,-\mathrm j)^{\top}$, car $\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)(1,\,-\mathrm j)^{\top}=(\mathrm j,\,1)^{\top}=\mathrm j\,(1,\,-\mathrm j)^{\top}$.

⁠**Exemple de calcul 2 :** La rotation $\mathbf{Q}=\bigl(\begin{smallmatrix}0{,}6&-0{,}8\\0{,}8&0{,}6\end{smallmatrix}\bigr)$ de la section [1.4](orthonormalbasen-und-orthogonale-matrizen.html#stufe-1-4) a $p(\lambda)=\lambda^2-1{,}2\lambda+1$ et, d’après l’exemple de calcul sur les nombres complexes, les valeurs propres $0{,}6\pm\mathrm j\,0{,}8=\cos\alpha\pm\mathrm j\sin\alpha=\mathrm e^{\pm\mathrm j\alpha}$ avec $\alpha\approx53{,}13^\circ$. En général, la rotation d’angle $\alpha$ a pour valeurs propres $\mathrm e^{\pm\mathrm j\alpha}$.

Une matrice réelle peut donc avoir des valeurs propres complexes. Comme son polynôme caractéristique est à coefficients réels, elles apparaissent par paires de nombres conjugués. Un vecteur propre réel ne peut être associé qu’à une valeur propre réelle : si $\mathbf{v}$ était réel et $\mathbf{A}\mathbf{v}=\lambda\mathbf{v}$, alors $\lambda\mathbf{v}$, image d’un vecteur réel, serait réel, et donc $\lambda$ aussi. Des valeurs propres complexes indiquent que la matrice fait tourner dans un plan.

⁠**En bref :** Une matrice réelle peut avoir des valeurs propres complexes, toujours par paires de nombres conjugués ; une rotation d’angle $\alpha$ a pour valeurs propres $\mathrm e^{\pm\mathrm j\alpha}$.

:::hintergrund Tourner, c’est multiplier par $\mathrm e^{\mathrm j\alpha}$
Pour les électrotechniciens, ce résultat est familier. On identifie la flèche $(x_1,\,x_2)^{\top}$ au nombre complexe $z=x_1+\mathrm jx_2$, comme pour un phaseur. Une rotation d’angle $\alpha$ est alors la multiplication par $\mathrm e^{\mathrm j\alpha}$ : $\mathrm e^{\mathrm j\alpha}z=(x_1\cos\alpha-x_2\sin\alpha)+\mathrm j\,(x_1\sin\alpha+x_2\cos\alpha)$, et ce sont exactement les deux composantes de $\mathbf{Q}\mathbf{x}$ pour la matrice de rotation de Fondements 1, section 8.3. En notation complexe, la rotation est donc une multiplication par un nombre, et ce nombre est une valeur propre. La seconde valeur propre $\mathrm e^{-\mathrm j\alpha}$ correspond à l’écriture conjuguée $z^*$, qui tourne dans le sens contraire.
:::

### Valeurs propres multiples

<span class="anker" id="stufe-6-7"></span>

Le polynôme caractéristique peut avoir une racine double. Deux des $n$ valeurs propres coïncident alors. Le nombre de fois où une valeur propre apparaît est une grandeur à part entière.

:::definition Définition 6.7 (Multiplicité algébrique)
<span class="anker" id="satz-6-7"></span>

La __multiplicité algébrique__ d’une valeur propre $\lambda$ est la multiplicité de $\lambda$ comme racine du polynôme caractéristique.
:::

⁠**Exemple de calcul :** La matrice $2\mathbf{I}=\operatorname{diag}(2;\,2)$ a $p(\lambda)=(2-\lambda)^2$ : la valeur propre $2$ est de multiplicité algébrique $2$. Le cisaillement $\bigl(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\bigr)$ de Fondements 1, section 8.3, a $p(\lambda)=(1-\lambda)^2$ : la valeur propre $1$ est elle aussi de multiplicité algébrique $2$. La matrice $\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$ a deux valeurs propres distinctes, chacune de multiplicité algébrique $1$.

⁠**En bref :** La multiplicité algébrique compte combien de fois une valeur propre apparaît comme racine du polynôme caractéristique.

### Combien il y a de vecteurs propres

<span class="anker" id="stufe-6-8"></span>

Les deux exemples avec une valeur propre double se comportent de façon très différente. La matrice $2\mathbf{I}$ étire chaque flèche d’un facteur deux ; tout vecteur $\ne\mathbf{0}$ est un vecteur propre, et le sous-espace propre est le plan tout entier. Le cisaillement décale chaque point vers la droite d’une quantité égale à sa hauteur ; seules les flèches situées sur l’axe des $x_1$ restent sur leur droite. Son sous-espace propre est $\ker\bigl(\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\bigr)$, la droite de direction $(1,\,0)^{\top}$. La différence tient à la dimension du sous-espace propre.

:::definition Définition 6.8 (Multiplicité géométrique)
<span class="anker" id="satz-6-8"></span>

La __multiplicité géométrique__ d’une valeur propre est la dimension de son sous-espace propre.
:::

Elle vaut au moins $1$, car à chaque valeur propre correspond un vecteur propre, et au plus la multiplicité algébrique ; ce chapitre ne démontre pas cette seconde partie. Pour $2\mathbf{I}$, les deux multiplicités valent $2$ ; pour le cisaillement, la multiplicité algébrique vaut $2$ et la géométrique $1$ : il lui manque un vecteur propre.

:::satz Théorème 6.9 (Valeurs propres distinctes, vecteurs propres indépendants)
<span class="anker" id="satz-6-9"></span>

Des vecteurs propres $\mathbf{v}_1,\dots,\mathbf{v}_k$ associés à des valeurs propres $\lambda_1,\dots,\lambda_k$ deux à deux distinctes sont linéairement indépendants. Si une matrice $n\times n$ a $n$ valeurs propres distinctes, ses vecteurs propres forment une base.
:::

:::beweis Vecteurs propres indépendants
Pour deux vecteurs propres : supposons $c_1\mathbf{v}_1+c_2\mathbf{v}_2=\mathbf{0}$. En appliquant $\mathbf{A}$, on obtient $c_1\lambda_1\mathbf{v}_1+c_2\lambda_2\mathbf{v}_2=\mathbf{0}$. Si l’on en retranche $\lambda_2$ fois la première équation, il reste $c_1(\lambda_1-\lambda_2)\mathbf{v}_1=\mathbf{0}$. Comme $\lambda_1\ne\lambda_2$ et $\mathbf{v}_1\ne\mathbf{0}$, on a $c_1=0$, et alors aussi $c_2=0$. Pour davantage de vecteurs propres, on procède de même : s’il existait une relation de dépendance, on en prendrait une ayant le moins possible de coefficients non nuls. Appliquer $\mathbf{A}$ puis retrancher cette relation multipliée par l’une des valeurs propres $\lambda$ concernées donnerait une relation de dépendance avec encore moins de coefficients non nuls, ce qui est une contradiction.
:::

⁠**Exemple de calcul :** Les vecteurs propres $(1,\,1)^{\top}$ et $(1,\,-2)^{\top}$ de $\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$ sont associés aux valeurs propres distinctes $5$ et $2$ ; ils sont linéairement indépendants, car $\det\bigl(\begin{smallmatrix}1&1\\1&-2\end{smallmatrix}\bigr)=-3\ne0$. Le cisaillement, en revanche, n’a que la direction propre $(1,\,0)^{\top}$ ; il n’existe pas deux vecteurs propres indépendants.

⁠**En bref :** La multiplicité géométrique compte les vecteurs propres indépendants associés à une valeur propre ; elle peut être inférieure à la multiplicité algébrique, mais des valeurs propres distinctes ont toujours des vecteurs propres indépendants.

### Règles de calcul pour les valeurs propres

<span class="anker" id="stufe-6-9"></span>

Qui connaît les vecteurs propres d’une matrice les connaît aussi pour de nombreuses matrices construites à partir d’elle. Les règles découlent toutes directement de [(6.1)](#gl-6-1).

:::satz Théorème 6.10 (Règles de calcul)
<span class="anker" id="satz-6-10"></span>

Soit $\mathbf{A}\mathbf{v}=\lambda\mathbf{v}$ avec $\mathbf{v}\ne\mathbf{0}$. Alors :

<ol class="rm">

<li>

$\mathbf{A}^k\mathbf{v}=\lambda^k\mathbf{v}$ pour tout entier naturel $k$ ;

</li>

<li>

$(\mathbf{A}+\beta\mathbf{I})\mathbf{v}=(\lambda+\beta)\mathbf{v}$ pour tout nombre $\beta$ ;

</li>

<li>

$\mathbf{A}$ est inversible si et seulement si aucune valeur propre n’est nulle, et alors $\mathbf{A}^{-1}\mathbf{v}=\frac1\lambda\mathbf{v}$ ;

</li>

<li>

$\mathbf{A}^{\top}$ a les mêmes valeurs propres que $\mathbf{A}$, mais en général d’autres vecteurs propres.

</li>

</ol>
:::

:::beweis Règles de calcul
(i) $\mathbf{A}^2\mathbf{v}=\mathbf{A}(\lambda\mathbf{v})=\lambda\mathbf{A}\mathbf{v}=\lambda^2\mathbf{v}$, et ainsi de suite. (ii) $(\mathbf{A}+\beta\mathbf{I})\mathbf{v}=\lambda\mathbf{v}+\beta\mathbf{v}$. (iii) D’après [(6.5)](#gl-6-5), $\det\mathbf{A}$ est le produit des valeurs propres ; il est donc non nul si et seulement si aucune valeur propre n’est nulle. En multipliant $\mathbf{A}\mathbf{v}=\lambda\mathbf{v}$ par $\mathbf{A}^{-1}$, on obtient $\mathbf{v}=\lambda\mathbf{A}^{-1}\mathbf{v}$. (iv) D’après Fondements 1, section 14.5, $\det(\mathbf{A}^{\top}-\lambda\mathbf{I})=\det\bigl((\mathbf{A}-\lambda\mathbf{I})^{\top}\bigr)=\det(\mathbf{A}-\lambda\mathbf{I})$ ; les deux matrices ont le même polynôme caractéristique.
:::

⁠**Exemple de calcul :** Pour $\mathbf{A}=\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$, la matrice $\mathbf{A}^2=\bigl(\begin{smallmatrix}18&7\\14&11\end{smallmatrix}\bigr)$ a pour valeurs propres $25$ et $4$ : $\mathbf{A}^2(1,\,1)^{\top}=(25,\,25)^{\top}$. La matrice $\mathbf{A}-5\mathbf{I}$ a pour valeurs propres $0$ et $-3$ et n’est pas inversible. L’inverse $\mathbf{A}^{-1}=\tfrac1{10}\bigl(\begin{smallmatrix}3&-1\\-2&4\end{smallmatrix}\bigr)$ a pour valeurs propres $\tfrac15$ et $\tfrac12$ : $\mathbf{A}^{-1}(1,\,-2)^{\top}=\tfrac1{10}(5,\,-10)^{\top}=\tfrac12(1,\,-2)^{\top}$. La transposée $\mathbf{A}^{\top}=\bigl(\begin{smallmatrix}4&2\\1&3\end{smallmatrix}\bigr)$ a elle aussi les valeurs propres $5$ et $2$, mais $\mathbf{A}^{\top}(1,\,1)^{\top}=(6,\,4)^{\top}$ : ses vecteurs propres sont $(2,\,1)^{\top}$ et $(1,\,-1)^{\top}$.

⁠**En bref :** Les puissances, les décalages de $\beta\mathbf{I}$ et l’inverse conservent les vecteurs propres et transforment les valeurs propres de la même façon ; la transposée ne conserve que les valeurs propres.

:::aufgabe Exercice 17 ★ Valeurs propres et vecteurs propres
<span class="anker" id="aufg-17"></span>

Déterminez les valeurs propres et les sous-espaces propres de

$$\mathbf{A}_1=\begin{pmatrix}2&2\\1&3\end{pmatrix},\qquad \mathbf{A}_2=\begin{pmatrix}3&0\\0&3\end{pmatrix},\qquad \mathbf{A}_3=\begin{pmatrix}1&3\\3&1\end{pmatrix}.$$

Vérifiez chaque fois la trace et le déterminant. Pour quelle matrice les vecteurs propres sont-ils perpendiculaires ?

:::loesung
$\mathbf{A}_1$ : trace $5$, déterminant $6-2=4$, donc $\lambda^2-5\lambda+4=(\lambda-4)(\lambda-1)$. Pour $\lambda=4$ : $\mathbf{A}_1-4\mathbf{I}=\bigl(\begin{smallmatrix}-2&2\\1&-1\end{smallmatrix}\bigr)$, sous-espace propre de direction $(1,\,1)^{\top}$. Pour $\lambda=1$ : $\mathbf{A}_1-\mathbf{I}=\bigl(\begin{smallmatrix}1&2\\1&2\end{smallmatrix}\bigr)$, sous-espace propre de direction $(2,\,-1)^{\top}$. Vérification : $4+1=5$, $4\cdot1=4$. Les vecteurs propres ne sont pas perpendiculaires : $(1,\,1)(2,\,-1)^{\top}=1$.

$\mathbf{A}_2=3\mathbf{I}$ : $p(\lambda)=(3-\lambda)^2$, la valeur propre $3$ est double ; le sous-espace propre est le plan tout entier. Vérification : $3+3=6$, $3\cdot3=9$. On peut choisir deux vecteurs propres perpendiculaires, par exemple $\mathbf{e}_1$ et $\mathbf{e}_2$, mais aussi deux vecteurs obliques l’un par rapport à l’autre.

$\mathbf{A}_3$ : trace $2$, déterminant $1-9=-8$, donc $\lambda^2-2\lambda-8=(\lambda-4)(\lambda+2)$. Vecteurs propres : $(1,\,1)^{\top}$, associé à $4$, et $(1,\,-1)^{\top}$, associé à $-2$. Vérification : $4-2=2$, $4\cdot(-2)=-8$. Ils sont perpendiculaires ; $\mathbf{A}_3$ est symétrique, et la section [7.5](diagonalisierung-und-spektralsatz.html#stufe-7-5) montre que ce n’est pas un hasard.
:::
:::

:::aufgabe Exercice 18 ★ Matrices triangulaires
<span class="anker" id="aufg-18"></span>

Montrez que les valeurs propres d’une matrice triangulaire supérieure sont ses coefficients diagonaux. Déterminez les valeurs propres et les vecteurs propres de $\Bigl(\begin{smallmatrix}2&1&0\\0&3&1\\0&0&5\end{smallmatrix}\Bigr)$.

:::loesung
Pour une matrice triangulaire supérieure, $\mathbf{A}-\lambda\mathbf{I}$ est encore une matrice triangulaire supérieure, de coefficients diagonaux $a_{ii}-\lambda$. D’après Fondements 1, section 14.4, son déterminant est le produit des coefficients diagonaux : $p(\lambda)=(a_{11}-\lambda)\cdots(a_{nn}-\lambda)$. Les racines sont les coefficients diagonaux.

Pour la matrice donnée, les valeurs propres sont donc $2$, $3$ et $5$. Pour $2$ : $\mathbf{A}-2\mathbf{I}=\Bigl(\begin{smallmatrix}0&1&0\\0&1&1\\0&0&3\end{smallmatrix}\Bigr)$ exige $v_3=0$ et $v_2=0$, vecteur propre $(1,\,0,\,0)^{\top}$. Pour $3$ : $\Bigl(\begin{smallmatrix}-1&1&0\\0&0&1\\0&0&2\end{smallmatrix}\Bigr)$ exige $v_3=0$ et $v_2=v_1$, vecteur propre $(1,\,1,\,0)^{\top}$. Pour $5$ : $\Bigl(\begin{smallmatrix}-3&1&0\\0&-2&1\\0&0&0\end{smallmatrix}\Bigr)$ exige $v_2=3v_1$ et $v_3=2v_2$, vecteur propre $(1,\,3,\,6)^{\top}$. Vérification : $\mathbf{A}(1,\,3,\,6)^{\top}=(2+3,\ 9+6,\ 30)^{\top}=5\,(1,\,3,\,6)^{\top}$.
:::
:::

:::aufgabe Exercice 19 ★★ Multiplicités
<span class="anker" id="aufg-19"></span>

Pour $\mathbf{B}_1=\bigl(\begin{smallmatrix}2&0\\0&2\end{smallmatrix}\bigr)$, $\mathbf{B}_2=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ et $\mathbf{B}_3=\Bigl(\begin{smallmatrix}1&0&0\\0&1&1\\0&0&1\end{smallmatrix}\Bigr)$, déterminez toutes les valeurs propres avec leurs multiplicités algébrique et géométrique.

:::loesung
$\mathbf{B}_1=2\mathbf{I}$ : valeur propre $2$, multiplicité algébrique $2$ ; le sous-espace propre est le plan tout entier, multiplicité géométrique $2$.

$\mathbf{B}_2$ : matrice triangulaire, valeur propre $2$ de multiplicité algébrique $2$. $\mathbf{B}_2-2\mathbf{I}=\bigl(\begin{smallmatrix}0&3\\0&0\end{smallmatrix}\bigr)$ exige $v_2=0$ ; le sous-espace propre est l’axe des $x_1$, multiplicité géométrique $1$. Comme au cisaillement, il manque un vecteur propre à $\mathbf{B}_2$.

$\mathbf{B}_3$ : matrice triangulaire, valeur propre $1$ de multiplicité algébrique $3$. $\mathbf{B}_3-\mathbf{I}=\Bigl(\begin{smallmatrix}0&0&0\\0&0&1\\0&0&0\end{smallmatrix}\Bigr)$ exige seulement $v_3=0$ ; le sous-espace propre est $\operatorname{span}\{\mathbf{e}_1,\mathbf{e}_2\}$, multiplicité géométrique $2$. Ici, la multiplicité géométrique se situe entre $1$ et la multiplicité algébrique.
:::
:::

:::aufgabe Exercice 20 ★★ Une rotation et une réflexion
<span class="anker" id="aufg-20"></span>

<ol class="al">

<li>

Calculez les valeurs propres de la rotation d’angle $30^\circ$ et écrivez-les sous la forme $\mathrm e^{\pm\mathrm j\alpha}$.

</li>

<li>

La réflexion $\bigl(\begin{smallmatrix}0{,}6&0{,}8\\0{,}8&-0{,}6\end{smallmatrix}\bigr)$ de la section [1.5](orthonormalbasen-und-orthogonale-matrizen.html#stufe-1-5) est elle aussi orthogonale. Déterminez ses valeurs propres et ses vecteurs propres, et interprétez-les géométriquement.

</li>

<li>

Montrez que toute valeur propre réelle d’une matrice orthogonale vaut $1$ ou $-1$.

</li>

</ol>

:::loesung
(a) La rotation d’angle $30^\circ$ est $\bigl(\begin{smallmatrix}\sqrt3/2&-1/2\\1/2&\sqrt3/2\end{smallmatrix}\bigr)$, de trace $\sqrt3$ et de déterminant $1$. Donc $p(\lambda)=\lambda^2-\sqrt3\,\lambda+1$ et

$$\lambda=\frac{\sqrt3\pm\sqrt{3-4}}2=\frac{\sqrt3}2\pm\mathrm j\,\frac12=\cos30^\circ\pm\mathrm j\sin30^\circ=\mathrm e^{\pm\mathrm j\,30^\circ} .$$

(b) Trace $0$, déterminant $-0{,}36-0{,}64=-1$, donc $p(\lambda)=\lambda^2-1$, de valeurs propres $1$ et $-1$. Pour $1$ : $\bigl(\begin{smallmatrix}-0{,}4&0{,}8\\0{,}8&-1{,}6\end{smallmatrix}\bigr)$, vecteur propre $(2,\,1)^{\top}$. Pour $-1$ : $\bigl(\begin{smallmatrix}1{,}6&0{,}8\\0{,}8&0{,}4\end{smallmatrix}\bigr)$, vecteur propre $(1,\,-2)^{\top}$. Géométriquement : les points de l’axe de symétrie, de direction $(2,\,1)^{\top}$, restent fixes, la valeur propre est $1$ ; la direction perpendiculaire est retournée, la valeur propre est $-1$. Les deux vecteurs propres sont perpendiculaires, car la matrice est symétrique.

(c) Soit $\mathbf{Q}\mathbf{v}=\lambda\mathbf{v}$ avec $\lambda$ réel et $\mathbf{v}\ne\mathbf{0}$ réel. D’après [(1.3)](orthonormalbasen-und-orthogonale-matrizen.html#gl-1-3), $\lVert\mathbf{v}\rVert=\lVert\mathbf{Q}\mathbf{v}\rVert=|\lambda|\,\lVert\mathbf{v}\rVert$, donc $|\lambda|=1$ et $\lambda=\pm1$. Un mouvement rigide ne peut que laisser une flèche telle quelle sur sa droite ou la retourner ; il ne peut pas l’étirer.
:::
:::

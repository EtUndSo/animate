---
title: Diagonalisation et théorème spectral
pfad: Informatique / Apprentissage automatique / Fondements mathématiques / Projection, valeurs propres et décompositions
knoten: Fondements 2 : Projection, valeurs propres et décompositions
nachschlagen: ja
order: 15220800
summary: Si l’on décrit une matrice dans une base formée de ses vecteurs propres, elle devient diagonale : chaque coordonnée est seulement multipliée par sa valeur propre, et des calculs couplés se décomposent en calculs séparés.
tags: changement de base, diagonalisable, axes principaux
lang: fr
---

<span class="anker" id="stufe-7"></span>

:::zweck
Si l’on décrit une matrice dans une base formée de ses vecteurs propres, elle devient diagonale : chaque coordonnée est seulement multipliée par sa valeur propre, et des calculs couplés se décomposent en calculs séparés. Cette section montre quand c’est possible et démontre que c’est toujours possible pour les matrices symétriques, et même avec une base orthonormée.
:::

### Changement de base

<span class="anker" id="stufe-7-1"></span>

La même flèche a des coordonnées différentes dans des bases différentes. De même, la même application linéaire a des matrices différentes dans des coordonnées différentes. Certaines bases rendent la matrice particulièrement simple.

Soit $\mathbf s_1,\dots,\mathbf s_n$ une base de $\mathbb{R}^n$, et $\mathbf{S}$ la matrice ayant ces vecteurs pour colonnes. D’après Fondements 1, section 13.5, elle est inversible. Si $\mathbf{x}$ a les coordonnées $\mathbf{c}$ dans cette base, alors $\mathbf{x}=\sum_ic_i\mathbf s_i=\mathbf{S}\mathbf{c}$, et inversement $\mathbf{c}=\mathbf{S}^{-1}\mathbf{x}$. Si l’on applique $\mathbf{A}$ à $\mathbf{x}$, l’image $\mathbf{A}\mathbf{x}$ a les coordonnées $\mathbf{S}^{-1}\mathbf{A}\mathbf{x}=\mathbf{S}^{-1}\mathbf{A}\mathbf{S}\,\mathbf{c}$. Dans les nouvelles coordonnées, l’application agit donc par la matrice $\mathbf{S}^{-1}\mathbf{A}\mathbf{S}$ : on convertit d’abord dans les anciennes coordonnées, on applique ensuite l’application, puis on reconvertit.

:::definition Définition 7.1 (Changement de base)
<span class="anker" id="satz-7-1"></span>

Si $\mathbf{S}$ est inversible, $\mathbf{B}=\mathbf{S}^{-1}\mathbf{A}\mathbf{S}$ est appelée la matrice de $\mathbf{A}$ dans la base des colonnes de $\mathbf{S}$. Le passage de $\mathbf{A}$ à $\mathbf{B}$ est appelé __changement de base__.
:::

Deux matrices liées de cette façon sont dites semblables. Elles décrivent la même application, simplement dans des coordonnées différentes.

:::satz Théorème 7.2 (Ce qu’un changement de base ne modifie pas)
<span class="anker" id="satz-7-2"></span>

$\mathbf{A}$ et $\mathbf{S}^{-1}\mathbf{A}\mathbf{S}$ ont le même polynôme caractéristique, donc les mêmes valeurs propres, la même trace et le même déterminant.
:::

:::beweis Changement de base
On a $\mathbf{S}^{-1}\mathbf{A}\mathbf{S}-\lambda\mathbf{I}=\mathbf{S}^{-1}(\mathbf{A}-\lambda\mathbf{I})\mathbf{S}$. D’après les règles de calcul de Fondements 1, section 14.5, son déterminant vaut $\det\mathbf{S}^{-1}\cdot\det(\mathbf{A}-\lambda\mathbf{I})\cdot\det\mathbf{S}=\det(\mathbf{A}-\lambda\mathbf{I})$. D’après [(6.5)](eigenwerte-und-eigenvektoren.html#gl-6-5), la trace et le déterminant se déduisent des valeurs propres.
:::

⁠**Exemple de calcul :** Pour $\mathbf{A}=\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$ et la base $(1,\,0)^{\top}$, $(1,\,1)^{\top}$ de Fondements 1, section 13.3, on a $\mathbf{S}=\bigl(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\bigr)$ et $\mathbf{S}^{-1}=\bigl(\begin{smallmatrix}1&-1\\0&1\end{smallmatrix}\bigr)$. Alors

$$\mathbf{S}^{-1}\mathbf{A}\mathbf{S}=\begin{pmatrix}1&-1\\0&1\end{pmatrix}\begin{pmatrix}4&5\\2&5\end{pmatrix}=\begin{pmatrix}2&0\\2&5\end{pmatrix}.$$

La trace vaut de nouveau $7$, le déterminant de nouveau $10$, et les valeurs propres figurent maintenant sur la diagonale d’une matrice triangulaire : $2$ et $5$.

⁠**En bref :** Dans la base des colonnes de $\mathbf{S}$, l’application $\mathbf{A}$ a pour matrice $\mathbf{S}^{-1}\mathbf{A}\mathbf{S}$ ; les valeurs propres, la trace et le déterminant restent inchangés.

### Diagonalisation

<span class="anker" id="stufe-7-2"></span>

La matrice la plus simple possible est une matrice diagonale : elle multiplie chaque coordonnée par un nombre qui lui est propre, sans mélanger les coordonnées. Si l’on prend pour base les vecteurs propres, chaque vecteur de base est seulement multiplié par sa valeur propre. Dans cette base, la matrice est donc diagonale.

:::satz Théorème 7.3 (Diagonalisation)
<span class="anker" id="satz-7-3"></span>

Si $\mathbf{A}\in\mathbb{R}^{n\times n}$ a $n$ vecteurs propres linéairement indépendants $\mathbf s_1,\dots,\mathbf s_n$ associés aux valeurs propres $\lambda_1,\dots,\lambda_n$, et si $\mathbf{S}$ est la matrice ayant ces vecteurs pour colonnes, alors

<span class="anker" id="gl-7-1"></span>
$$\mathbf{S}^{-1}\mathbf{A}\mathbf{S}=\boldsymbol{\Lambda}=\operatorname{diag}(\lambda_1,\dots,\lambda_n),\qquad\text{donc}\qquad \mathbf{A}=\mathbf{S}\boldsymbol{\Lambda}\mathbf{S}^{-1} . \tag{7.1}$$

Réciproquement, si $\mathbf{A}$ peut s’écrire ainsi, les colonnes de $\mathbf{S}$ sont des vecteurs propres.
:::

:::beweis Diagonalisation
D’après Fondements 1, section 9.2, la colonne $i$ de $\mathbf{A}\mathbf{S}$ est le produit $\mathbf{A}\mathbf s_i=\lambda_i\mathbf s_i$, et la colonne $i$ de $\mathbf{S}\boldsymbol{\Lambda}$ vaut elle aussi $\lambda_i\mathbf s_i$. Donc $\mathbf{A}\mathbf{S}=\mathbf{S}\boldsymbol{\Lambda}$. Les colonnes de $\mathbf{S}$ sont indépendantes, donc $\mathbf{S}$ est inversible, et la multiplication à gauche par $\mathbf{S}^{-1}$ donne [(7.1)](#gl-7-1). En lisant la même égalité $\mathbf{A}\mathbf{S}=\mathbf{S}\boldsymbol{\Lambda}$ dans l’autre sens, on obtient la réciproque.
:::

Une matrice qui peut s’écrire ainsi est dite __diagonalisable__. D’après le théorème de la section [6.8](eigenwerte-und-eigenvektoren.html#stufe-6-8), c’est par exemple toujours le cas lorsque les $n$ valeurs propres sont toutes distinctes. Le cisaillement n’est pas diagonalisable, car il lui manque un vecteur propre. La rotation de $90^\circ$ n’est pas non plus diagonalisable avec des nombres réels, seulement avec des nombres complexes. Ces deux matrices sont pourtant inversibles : inversible et diagonalisable sont deux propriétés différentes.

⁠**Exemple de calcul :** Pour $\mathbf{A}=\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$, de vecteurs propres $(1,\,1)^{\top}$ et $(1,\,-2)^{\top}$, on a

$$\mathbf{S}=\begin{pmatrix}1&1\\1&-2\end{pmatrix},\qquad \mathbf{S}^{-1}=\frac13\begin{pmatrix}2&1\\1&-1\end{pmatrix},\qquad \mathbf{S}^{-1}\mathbf{A}\mathbf{S}=\frac13\begin{pmatrix}2&1\\1&-1\end{pmatrix}\begin{pmatrix}5&2\\5&-4\end{pmatrix}=\begin{pmatrix}5&0\\0&2\end{pmatrix}.$$

⁠**En bref :** Une matrice qui possède $n$ vecteurs propres indépendants est diagonale dans la base formée par ceux-ci : $\mathbf{A}=\mathbf{S}\boldsymbol{\Lambda}\mathbf{S}^{-1}$.

### Découpler : puissances et suites

<span class="anker" id="stufe-7-3"></span>

Une matrice que l’on applique encore et encore montre à quoi cela sert. Deux localités A et B échangent chaque année des habitants : $20\,\%$ des habitants de A déménagent vers B, $30\,\%$ des habitants de B déménagent vers A, tous les autres restent. Si $\mathbf{x}_k$ désigne les nombres d’habitants l’année $k$, alors

$$\mathbf{x}_{k+1}=\mathbf M\mathbf{x}_k\qquad\text{avec}\qquad \mathbf M=\begin{pmatrix}0{,}8&0{,}3\\0{,}2&0{,}7\end{pmatrix}.$$

Les deux nombres d’habitants sont couplés : chaque nouveau nombre dépend des deux anciens. Après $k$ années, $\mathbf{x}_k=\mathbf M^k\mathbf{x}_0$. Calculer directement la puissance $\mathbf M^k$ est laborieux et ne montre pas ce qui se passe à long terme. Dans la base propre, c’est simple.

:::satz Théorème 7.4 (Puissances et suites dans la base propre)
<span class="anker" id="satz-7-4"></span>

Si $\mathbf{A}=\mathbf{S}\boldsymbol{\Lambda}\mathbf{S}^{-1}$, alors $\mathbf{A}^k=\mathbf{S}\boldsymbol{\Lambda}^k\mathbf{S}^{-1}$ avec $\boldsymbol{\Lambda}^k=\operatorname{diag}(\lambda_1^k,\dots,\lambda_n^k)$. Pour la suite $\mathbf{x}_{k+1}=\mathbf{A}\mathbf{x}_k$, on a

<span class="anker" id="gl-7-2"></span>
$$\mathbf{x}_k=\sum_{i=1}^nc_i\,\lambda_i^k\,\mathbf s_i\qquad\text{avec}\qquad \mathbf{c}=\mathbf{S}^{-1}\mathbf{x}_0 . \tag{7.2}$$
:::

:::beweis Puissances
$\mathbf{A}^2=\mathbf{S}\boldsymbol{\Lambda}\mathbf{S}^{-1}\mathbf{S}\boldsymbol{\Lambda}\mathbf{S}^{-1}=\mathbf{S}\boldsymbol{\Lambda}^2\mathbf{S}^{-1}$, car $\mathbf{S}^{-1}\mathbf{S}=\mathbf{I}$ disparaît au milieu ; il en va de même pour toute puissance. Si l’on décompose $\mathbf{x}_0=\sum_ic_i\mathbf s_i$ en vecteurs propres, chaque application de $\mathbf{A}$ multiplie chaque part seulement par sa valeur propre.
:::

Dans les coordonnées $\mathbf{c}$ de la base propre, chaque étape consiste à multiplier chaque coordonnée par son propre nombre : $c_i\mapsto\lambda_ic_i$. Un calcul couplé à $n$ inconnues devient $n$ calculs séparés à une inconnue chacun. Ces coordonnées sont découplées. À long terme, la part associée à la valeur propre de plus grand module l’emporte.

⁠**Exemple de calcul :** $\mathbf M$ a pour trace $1{,}5$ et pour déterminant $0{,}56-0{,}06=0{,}5$, donc pour valeurs propres $1$ et $0{,}5$. Des vecteurs propres sont $\mathbf s_1=(3,\,2)^{\top}$ pour la valeur propre $1$, car $\mathbf M\mathbf s_1=(2{,}4+0{,}6;\ 0{,}6+1{,}4)^{\top}=\mathbf s_1$, et $\mathbf s_2=(1,\,-1)^{\top}$ pour la valeur propre $0{,}5$. Si, au départ, $1000$ personnes habitent à A et personne à B, alors $\mathbf{x}_0=(1000,\,0)^{\top}=200\,\mathbf s_1+400\,\mathbf s_2$ et, d’après [(7.2)](#gl-7-2),

$$\mathbf{x}_k=200\begin{pmatrix}3\\2\end{pmatrix}+400\cdot0{,}5^k\begin{pmatrix}1\\-1\end{pmatrix}=\begin{pmatrix}600+400\cdot0{,}5^k\\400-400\cdot0{,}5^k\end{pmatrix}.$$

Après un an, on obtient $(800,\,200)^{\top}$, après deux ans $(700,\,300)^{\top}$, et à long terme la répartition tend vers $(600,\,400)^{\top}$. La part associée à la valeur propre $0{,}5$ diminue de moitié chaque année, la part associée à la valeur propre $1$ reste.

⁠**En bref :** Dans la base propre, toute puissance de la matrice se ramène à des puissances des valeurs propres ; des suites couplées se décomposent en suites séparées, une par vecteur propre.

:::hintergrund Le même principe que pour les systèmes LTI et la transformée de Fourier
Dans le domaine temporel, un système LTI est une convolution : chaque valeur de sortie dépend de toutes les valeurs d’entrée, tout est couplé. Si l’on décompose le signal d’entrée en fonctions exponentielles $\mathrm e^{pt}$, chacune est seulement multipliée par sa valeur propre $H(p)$, et le couplage a disparu. Les transformées de Laplace et de Fourier font pour les signaux ce que le changement de base $\mathbf{S}^{-1}$ fait pour les vecteurs : elles convertissent dans les coordonnées des fonctions propres.

Pour les signaux échantillonnés, la correspondance est même, au sens littéral, une diagonalisation. Une convolution circulaire $y_k=\sum_lh_{(k-l)\bmod n}\,x_l$ est une matrice dont la première colonne est la réponse impulsionnelle $(h_0,\dots,h_{n-1})^{\top}$ et dont les autres colonnes en sont les décalages circulaires. Ses vecteurs propres sont les oscillations complexes échantillonnées $\mathbf f_m=\bigl(1,\ \mathrm e^{\mathrm j2\pi m/n},\ \mathrm e^{\mathrm j2\pi\cdot2m/n},\dots\bigr)^{\top}$, et la valeur propre associée à $\mathbf f_m$ est la valeur $H[m]=\sum_qh_q\,\mathrm e^{-\mathrm j2\pi mq/n}$ de la transformée de Fourier discrète de la réponse impulsionnelle. La matrice de la transformée de Fourier discrète est donc, au facteur $1/n$ près, le $\mathbf{S}^{-1}$ qui diagonalise toute convolution circulaire, et ce pour toutes les réponses impulsionnelles à la fois. Exemple avec $n=3$ et $h=(1;\,0{,}5;\,0)$ : la matrice $\Bigl(\begin{smallmatrix}1&0&0{,}5\\0{,}5&1&0\\0&0{,}5&1\end{smallmatrix}\Bigr)$ envoie $\mathbf f_0=(1,1,1)^{\top}$ sur $1{,}5\,\mathbf f_0$, et $1{,}5=H[0]=h_0+h_1+h_2$.
:::

### Les matrices symétriques ont des valeurs propres réelles

<span class="anker" id="stufe-7-4"></span>

Pour les matrices symétriques, beaucoup de choses sont particulièrement simples. Première propriété : leurs valeurs propres sont toujours réelles. Une matrice symétrique ne fait donc tourner aucun plan sur lui-même, contrairement aux rotations de la section [6.6](eigenwerte-und-eigenvektoren.html#stufe-6-6).

:::satz Théorème 7.5 (Valeurs propres réelles)
<span class="anker" id="satz-7-5"></span>

Toute valeur propre d’une matrice symétrique réelle est réelle.
:::

:::beweis Valeurs propres réelles
Soit $\mathbf{A}\mathbf{v}=\lambda\mathbf{v}$ avec $\mathbf{v}\ne\mathbf{0}$, où $\lambda$ et $\mathbf{v}$ peuvent a priori être complexes. Si l’on conjugue les deux membres, $\mathbf{A}$ reste inchangée, car elle est réelle : $\mathbf{A}\mathbf{v}^*=\lambda^*\mathbf{v}^*$. On calcule le nombre $(\mathbf{v}^*)^{\top}\mathbf{A}\mathbf{v}$ de deux façons. D’une part, avec $\mathbf{A}\mathbf{v}=\lambda\mathbf{v}$ :

$$(\mathbf{v}^*)^{\top}\mathbf{A}\mathbf{v}=\lambda\,(\mathbf{v}^*)^{\top}\mathbf{v} .$$

D’autre part, avec $\mathbf{A}=\mathbf{A}^{\top}$ et $\mathbf{A}\mathbf{v}^*=\lambda^*\mathbf{v}^*$ :

$$(\mathbf{v}^*)^{\top}\mathbf{A}\mathbf{v}=(\mathbf{A}^{\top}\mathbf{v}^*)^{\top}\mathbf{v}=(\mathbf{A}\mathbf{v}^*)^{\top}\mathbf{v}=\lambda^*\,(\mathbf{v}^*)^{\top}\mathbf{v} .$$

Donc $(\lambda-\lambda^*)\,(\mathbf{v}^*)^{\top}\mathbf{v}=0$. D’après la section [6.1](eigenwerte-und-eigenvektoren.html#stufe-6-1), $(\mathbf{v}^*)^{\top}\mathbf{v}=\sum_i|v_i|^2>0$, donc $\lambda=\lambda^*$, et $\lambda$ est réel.
:::

À une valeur propre réelle correspondent alors aussi des vecteurs propres réels, car $(\mathbf{A}-\lambda\mathbf{I})\mathbf{v}=\mathbf{0}$ est un système d’équations réel.

⁠**Exemple de calcul :** $\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ a pour polynôme caractéristique $\lambda^2-7\lambda+6$, de discriminant $49-24=25>0$, et pour valeurs propres réelles $6$ et $1$. Pour une matrice symétrique $2\times2$ quelconque $\bigl(\begin{smallmatrix}a&b\\b&c\end{smallmatrix}\bigr)$, le discriminant vaut $(a+c)^2-4(ac-b^2)=(a-c)^2+4b^2\ge0$ ; les valeurs propres sont donc toujours réelles, comme l’affirme le théorème.

⁠**En bref :** Une matrice symétrique n’a que des valeurs propres réelles et des vecteurs propres réels.

### Les vecteurs propres des matrices symétriques sont perpendiculaires

<span class="anker" id="stufe-7-5"></span>

Les vecteurs propres de $\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$ étaient obliques l’un par rapport à l’autre. Pour les matrices symétriques, cela ne peut pas arriver.

:::satz Théorème 7.6 (Vecteurs propres orthogonaux)
<span class="anker" id="satz-7-6"></span>

Des vecteurs propres d’une matrice symétrique associés à des valeurs propres distinctes sont perpendiculaires.
:::

:::beweis Vecteurs propres orthogonaux
Soit $\mathbf{A}\mathbf{v}_1=\lambda_1\mathbf{v}_1$ et $\mathbf{A}\mathbf{v}_2=\lambda_2\mathbf{v}_2$ avec $\lambda_1\ne\lambda_2$. On calcule $\mathbf{v}_1^{\top}\mathbf{A}\mathbf{v}_2$ de deux façons : comme $\mathbf{v}_1^{\top}(\lambda_2\mathbf{v}_2)=\lambda_2\,\mathbf{v}_1^{\top}\mathbf{v}_2$, et, avec $\mathbf{A}^{\top}=\mathbf{A}$, comme $(\mathbf{A}\mathbf{v}_1)^{\top}\mathbf{v}_2=\lambda_1\,\mathbf{v}_1^{\top}\mathbf{v}_2$. Donc $(\lambda_1-\lambda_2)\,\mathbf{v}_1^{\top}\mathbf{v}_2=0$, et comme $\lambda_1\ne\lambda_2$, on a $\mathbf{v}_1^{\top}\mathbf{v}_2=0$.
:::

⁠**Exemple de calcul :** $\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ admet le vecteur propre $(2,\,1)^{\top}$ associé à la valeur propre $6$, car $(10+2,\ 4+2)^{\top}=6\,(2,\,1)^{\top}$, et le vecteur propre $(1,\,-2)^{\top}$ associé à la valeur propre $1$, car $(5-4,\ 2-4)^{\top}=(1,\,-2)^{\top}$. Leur produit scalaire vaut $2-2=0$ (Fig. [19](#abb-19)).

:::abbildung ml/k2rsenkrecht 19
Le produit scalaire des vecteurs propres $(2,1)^{\top}$, associé à la valeur propre $6$, et $(1,-2)^{\top}$, associé à la valeur propre $1$, de la matrice symétrique $\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ : ils sont perpendiculaires.
:::

⁠**En bref :** Pour une matrice symétrique, des vecteurs propres associés à des valeurs propres distinctes sont perpendiculaires.

:::hintergrund Pourquoi c’est justement la symétrie qui rend les directions propres perpendiculaires
La preuve utilise la symétrie à un seul endroit : $(\mathbf{A}\mathbf{v}_1)^{\top}\mathbf{v}_2=\mathbf{v}_1^{\top}(\mathbf{A}\mathbf{v}_2)$. Pour une matrice symétrique, cette égalité vaut pour tous les vecteurs ; on peut faire passer $\mathbf{A}$ d’un côté à l’autre du produit scalaire. Le produit scalaire mesure quelle part de $\mathbf{v}_2$ pointe dans la direction de $\mathbf{v}_1$. Si $\mathbf{A}$ étire une direction d’un facteur $\lambda_1$ et l’autre d’un facteur $\lambda_2$, cette part est multipliée par $\lambda_1$ à gauche et par $\lambda_2$ à droite. Les deux membres ne peuvent être égaux que s’il n’y a rien à multiplier, c’est-à-dire si cette part est nulle. Pour une matrice non symétrique, cette règle de passage ne vaut pas, et des directions propres obliques sont possibles.

Il en découle une deuxième propriété importante. Si $\mathbf{q}$ est un vecteur propre et si $\mathbf{z}$ est perpendiculaire à $\mathbf{q}$, alors $\mathbf{A}\mathbf{z}$ est lui aussi perpendiculaire à $\mathbf{q}$ : $(\mathbf{A}\mathbf{z})^{\top}\mathbf{q}=\mathbf{z}^{\top}\mathbf{A}\mathbf{q}=\lambda\,\mathbf{z}^{\top}\mathbf{q}=0$. Une matrice symétrique envoie donc le supplémentaire orthogonal d’un vecteur propre dans lui-même. On peut y chercher le vecteur propre suivant, et ainsi de suite. C’est exactement ainsi que fonctionne la preuve de la sous-section suivante.
:::

### Le théorème spectral

<span class="anker" id="stufe-7-6"></span>

Les deux théorèmes précédents laissent supposer que toute matrice symétrique est diagonale dans une base orthonormée de vecteurs propres. C’est vrai même lorsque des valeurs propres sont multiples. L’ensemble des valeurs propres d’une matrice est appelé son spectre, d’où le nom du théorème.

:::satz Théorème 7.7 (Théorème spectral)
<span class="anker" id="satz-7-7"></span>

Pour toute matrice symétrique $\mathbf{A}\in\mathbb{R}^{n\times n}$, il existe une base orthonormée $\mathbf{q}_1,\dots,\mathbf{q}_n$ formée de vecteurs propres, de valeurs propres réelles $\lambda_1,\dots,\lambda_n$. Avec la matrice orthogonale $\mathbf{Q}=\begin{pmatrix}\mathbf{q}_1&\cdots&\mathbf{q}_n\end{pmatrix}$ et $\boldsymbol{\Lambda}=\operatorname{diag}(\lambda_1,\dots,\lambda_n)$, on a

<span class="anker" id="gl-7-3"></span>
$$\mathbf{A}=\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top}=\sum_{i=1}^n\lambda_i\,\mathbf{q}_i\mathbf{q}_i^{\top} . \tag{7.3}$$
:::

:::beweis Théorème spectral
On procède pas à pas. D’après la section [6.3](eigenwerte-und-eigenvektoren.html#stufe-6-3), $\mathbf{A}$ a au moins une valeur propre $\lambda_1$ ; d’après la section [7.4](#stufe-7-4), elle est réelle et possède un vecteur propre réel, que l’on normalise en $\mathbf{q}_1$. On complète $\mathbf{q}_1$ en une base orthonormée de $\mathbb{R}^n$, par exemple avec le procédé de Gram-Schmidt appliqué à $\mathbf{q}_1,\mathbf{e}_1,\dots,\mathbf{e}_n$, en sautant les vecteurs pour lesquels $\tilde{\mathbf{q}}=\mathbf{0}$. Les autres vecteurs de base forment les colonnes d’une matrice $\mathbf{W}\in\mathbb{R}^{n\times(n-1)}$, et $\mathbf{Q}_1=\begin{pmatrix}\mathbf{q}_1&\mathbf{W}\end{pmatrix}$ est orthogonale. Alors

$$\mathbf{Q}_1^{\top}\mathbf{A}\mathbf{Q}_1=\begin{pmatrix}\mathbf{q}_1^{\top}\mathbf{A}\mathbf{q}_1&\mathbf{q}_1^{\top}\mathbf{A}\mathbf{W}\\\mathbf{W}^{\top}\mathbf{A}\mathbf{q}_1&\mathbf{W}^{\top}\mathbf{A}\mathbf{W}\end{pmatrix}=\begin{pmatrix}\lambda_1&\mathbf{0}^{\top}\\\mathbf{0}&\mathbf{B}\end{pmatrix}$$

avec la matrice symétrique $\mathbf{B}=\mathbf{W}^{\top}\mathbf{A}\mathbf{W}$, de taille $(n-1)\times(n-1)$. Les zéros en bas à gauche apparaissent parce que $\mathbf{A}\mathbf{q}_1=\lambda_1\mathbf{q}_1$ est perpendiculaire aux colonnes de $\mathbf{W}$, et ceux en haut à droite également, parce que $\mathbf{A}$ est symétrique. Pour $\mathbf{B}$, on répète la même opération jusqu’à ce qu’il ne reste qu’une matrice $1\times1$. Si l’on a ainsi trouvé pour $\mathbf{B}$ une matrice orthogonale $\mathbf{Q}_B$ telle que $\mathbf{Q}_B^{\top}\mathbf{B}\mathbf{Q}_B$ soit diagonale, alors $\mathbf{Q}=\mathbf{Q}_1\bigl(\begin{smallmatrix}1&\mathbf{0}^{\top}\\\mathbf{0}&\mathbf{Q}_B\end{smallmatrix}\bigr)$ est orthogonale en tant que produit de matrices orthogonales, et $\mathbf{Q}^{\top}\mathbf{A}\mathbf{Q}=\bigl(\begin{smallmatrix}\lambda_1&\mathbf{0}^{\top}\\\mathbf{0}&\mathbf{Q}_B^{\top}\mathbf{B}\mathbf{Q}_B\end{smallmatrix}\bigr)=\boldsymbol{\Lambda}$ est diagonale. Comme $\mathbf{Q}^{-1}=\mathbf{Q}^{\top}$, il s’ensuit que $\mathbf{A}=\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top}$. La forme en somme découle de Fondements 1, section 9.5, car $\mathbf{Q}\boldsymbol{\Lambda}$ a pour colonnes $\lambda_i\mathbf{q}_i$.
:::

D’après la section [2.3](projektion-auf-eine-gerade.html#stufe-2-3), chaque terme $\mathbf{q}_i\mathbf{q}_i^{\top}$ est la projection sur la droite de direction $\mathbf{q}_i$. Une matrice symétrique est donc une somme de projections sur des axes perpendiculaires, chacune pondérée par sa valeur propre. Pour une valeur propre multiple, le choix des $\mathbf{q}_i$ dans son sous-espace propre est libre : toute base orthonormée du sous-espace propre convient. Le signe de chaque $\mathbf{q}_i$ est lui aussi libre. Certains ouvrages classent les valeurs propres par ordre décroissant, d’autres non.

⁠**Exemple de calcul :** Pour $\mathbf{A}=\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$, $\mathbf{q}_1=(2,\,1)^{\top}/\sqrt5$ et $\mathbf{q}_2=(1,\,-2)^{\top}/\sqrt5$ sont les vecteurs propres normés associés à $6$ et à $1$. Alors

$$6\cdot\frac15\begin{pmatrix}4&2\\2&1\end{pmatrix}+1\cdot\frac15\begin{pmatrix}1&-2\\-2&4\end{pmatrix}=\frac15\begin{pmatrix}25&10\\10&10\end{pmatrix}=\begin{pmatrix}5&2\\2&2\end{pmatrix}.$$

⁠**En bref :** Toute matrice symétrique s’écrit $\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top}$ : elle est diagonale dans un repère convenablement tourné, et c’est une somme pondérée de projections sur des axes perpendiculaires.

:::hintergrund D’où viennent les matrices symétriques
Des matrices symétriques apparaissent partout où une matrice décrit des relations deux à deux qui ne dépendent pas de l’ordre. Les matrices de Gram $\mathbf{X}^{\top}\mathbf{X}$ et $\mathbf{X}\mathbf{X}^{\top}$ de Fondements 1, section 10, contiennent des produits scalaires, et $\mathbf{u}^{\top}\mathbf{v}=\mathbf{v}^{\top}\mathbf{u}$. D’après la section [5.2](quadratische-formen.html#stufe-5-2), on peut toujours choisir symétrique la matrice d’une forme quadratique. La matrice d’inductance de bobines couplées est symétrique, car l’inductance mutuelle de la bobine 1 sur la bobine 2 est la même que dans l’autre sens. Pour toutes ces matrices, le théorème spectral garantit des valeurs propres réelles et des directions propres perpendiculaires.
:::

### Axes principaux

<span class="anker" id="stufe-7-7"></span>

Dans la section [5.3](quadratische-formen.html#stufe-5-3), l’allure d’une forme quadratique se reconnaissait facilement tant que sa matrice était diagonale. Le théorème spectral rend toute matrice symétrique diagonale si l’on fait tourner convenablement les coordonnées. Les termes croisés disparaissent alors.

:::satz Théorème 7.8 (Axes principaux d’une forme quadratique)
<span class="anker" id="satz-7-8"></span>

Si $\mathbf{A}=\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top}$ et si $c_i=\mathbf{q}_i^{\top}\mathbf{x}$ sont les coordonnées de $\mathbf{x}$ dans la base propre, alors

<span class="anker" id="gl-7-4"></span>
$$\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=\lambda_1c_1^2+\lambda_2c_2^2+\dots+\lambda_nc_n^2 . \tag{7.4}$$
:::

:::beweis Axes principaux
Avec $\mathbf{c}=\mathbf{Q}^{\top}\mathbf{x}$, on a $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=\mathbf{x}^{\top}\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top}\mathbf{x}=\mathbf{c}^{\top}\boldsymbol{\Lambda}\mathbf{c}=\sum_i\lambda_ic_i^2$.
:::

C’est pourquoi les directions des vecteurs propres sont appelées les __axes principaux__ de la forme quadratique. Si toutes les valeurs propres sont positives, la ligne de niveau $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=1$ est une ellipse, et dans $\mathbb{R}^3$ un ellipsoïde. Ses axes sont dans les directions $\mathbf{q}_i$, et le demi-axe dans la direction $\mathbf{q}_i$ a pour longueur $1/\sqrt{\lambda_i}$, car pour $\mathbf{x}=t\,\mathbf{q}_i$, on a $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=\lambda_it^2=1$ exactement en $t=\pm1/\sqrt{\lambda_i}$. Une grande valeur propre correspond à une direction de forte pente et à un demi-axe court.

:::abbildung ml/k2ellipse 20
Les lignes de niveau $5x_1^2+4x_1x_2+2x_2^2=1$ (en bleu) et $=\tfrac14$ (en bleu clair) sont des ellipses. Leurs axes (en gris) sont dans les directions des vecteurs propres $\mathbf{q}_1=(2,1)^{\top}/\sqrt5$, associé à la valeur propre $6$, et $\mathbf{q}_2=(1,-2)^{\top}/\sqrt5$, associé à la valeur propre $1$. Les demi-axes de l’ellipse extérieure valent $1/\sqrt6\approx0{,}41$ (en rouge) et $1/\sqrt1=1$ (en vert) : c’est dans la direction de la grande valeur propre que la forme croît le plus vite, et l’ellipse y est la plus étroite.
:::

⁠**Exemple de calcul :** Pour $f(\mathbf{x})=5x_1^2+4x_1x_2+2x_2^2$, les coordonnées dans la base propre sont $c_1=(2x_1+x_2)/\sqrt5$ et $c_2=(x_1-2x_2)/\sqrt5$, et

$$5x_1^2+4x_1x_2+2x_2^2=6\,c_1^2+c_2^2=\tfrac65(2x_1+x_2)^2+\tfrac15(x_1-2x_2)^2 .$$

En développant, le membre de droite donne $\tfrac15\bigl(24x_1^2+24x_1x_2+6x_2^2+x_1^2-4x_1x_2+4x_2^2\bigr)=5x_1^2+4x_1x_2+2x_2^2$. La ligne de niveau $f=1$ est l’ellipse de la Fig. [20](#abb-20), de demi-axes $1/\sqrt6\approx0{,}408$ et $1$.

⁠**En bref :** Dans la base propre, toute forme quadratique devient la somme $\sum_i\lambda_ic_i^2$, sans termes croisés ; les vecteurs propres sont les axes principaux de ses ellipses, et les demi-axes valent $1/\sqrt{\lambda_i}$.

:::hintergrund Deux façons de compléter les carrés
Dans la section [5.4](quadratische-formen.html#stufe-5-4), la même forme pouvait aussi s’écrire $5(x_1+0{,}4x_2)^2+1{,}2x_2^2$. Les facteurs $5$ et $1{,}2$ de cette écriture sont d’autres nombres que les valeurs propres $6$ et $1$ obtenues ici. Les deux décompositions sont justes, mais les nouvelles coordonnées sont différentes : lorsqu’on complète le carré, $x_1+0{,}4x_2$ et $x_2$ sont des coordonnées obliques ; avec le théorème spectral, $c_1,c_2$ sont des coordonnées dans un repère orthogonal tourné. Seule la seconde décomposition montre les axes de l’ellipse. Les deux ont en commun autre chose : le nombre de facteurs positifs, négatifs et nuls est le même. Cela vaut pour toute décomposition d’une forme quadratique en une somme de carrés de coordonnées indépendantes ; ce théorème s’appelle la loi d’inertie de Sylvester. C’est pourquoi compléter le carré et calculer les valeurs propres mènent toujours au même verdict : cuvette, gouttière ou selle.
:::

:::aufgabe Exercice 21 ★ Diagonaliser
<span class="anker" id="aufg-21"></span>

Soit $\mathbf{A}=\bigl(\begin{smallmatrix}2&2\\1&3\end{smallmatrix}\bigr)$ la matrice de l’exercice [17](eigenwerte-und-eigenvektoren.html#aufg-17).

<ol class="al">

<li>

Donnez $\mathbf{S}$ et $\boldsymbol{\Lambda}$ telles que $\mathbf{A}=\mathbf{S}\boldsymbol{\Lambda}\mathbf{S}^{-1}$ et vérifiez l’égalité.

</li>

<li>

Calculez $\mathbf{A}^3$ une fois directement et une fois comme $\mathbf{S}\boldsymbol{\Lambda}^3\mathbf{S}^{-1}$.

</li>

</ol>

:::loesung
(a) D’après l’exercice [17](eigenwerte-und-eigenvektoren.html#aufg-17) : valeurs propres $4$ et $1$, de vecteurs propres $(1,\,1)^{\top}$ et $(2,\,-1)^{\top}$. Donc

$$\mathbf{S}=\begin{pmatrix}1&2\\1&-1\end{pmatrix},\qquad \boldsymbol{\Lambda}=\begin{pmatrix}4&0\\0&1\end{pmatrix},\qquad \mathbf{S}^{-1}=\frac13\begin{pmatrix}1&2\\1&-1\end{pmatrix},$$

car $\det\mathbf{S}=-3$. Vérification : $\mathbf{S}\boldsymbol{\Lambda}\mathbf{S}^{-1}=\bigl(\begin{smallmatrix}4&2\\4&-1\end{smallmatrix}\bigr)\cdot\tfrac13\bigl(\begin{smallmatrix}1&2\\1&-1\end{smallmatrix}\bigr)=\tfrac13\bigl(\begin{smallmatrix}6&6\\3&9\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}2&2\\1&3\end{smallmatrix}\bigr)$.

(b) Directement : $\mathbf{A}^2=\bigl(\begin{smallmatrix}6&10\\5&11\end{smallmatrix}\bigr)$ et $\mathbf{A}^3=\mathbf{A}^2\mathbf{A}=\bigl(\begin{smallmatrix}12+10&12+30\\10+11&10+33\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}22&42\\21&43\end{smallmatrix}\bigr)$. Par la base propre : $\boldsymbol{\Lambda}^3=\operatorname{diag}(64;\,1)$, $\mathbf{S}\boldsymbol{\Lambda}^3=\bigl(\begin{smallmatrix}64&2\\64&-1\end{smallmatrix}\bigr)$ et

$$\mathbf{S}\boldsymbol{\Lambda}^3\mathbf{S}^{-1}=\frac13\begin{pmatrix}64+2&128-2\\64-1&128+1\end{pmatrix}=\begin{pmatrix}22&42\\21&43\end{pmatrix}.$$

Pour de grandes puissances, la seconde voie est beaucoup plus courte : seules les valeurs propres sont élevées à la puissance.
:::
:::

:::aufgabe Exercice 22 ★★ Découpler une suite
<span class="anker" id="aufg-22"></span>

Les nombres de Fibonacci $0,1,1,2,3,5,\dots$ vérifient $F_{k+2}=F_{k+1}+F_k$. Avec $\mathbf{x}_k=(F_{k+1},\,F_k)^{\top}$, on a $\mathbf{x}_{k+1}=\bigl(\begin{smallmatrix}1&1\\1&0\end{smallmatrix}\bigr)\mathbf{x}_k$.

<ol class="al">

<li>

Déterminez les valeurs propres et les vecteurs propres de la matrice.

</li>

<li>

À l’aide de [(7.2)](#gl-7-2), établissez une formule pour $F_k$ et vérifiez-la pour $k=5$.

</li>

<li>

Comment se comporte $F_{k+1}/F_k$ pour $k$ grand, et pourquoi ?

</li>

</ol>

:::loesung
(a) $p(\lambda)=\lambda^2-\lambda-1$, de racines $\varphi=\tfrac{1+\sqrt5}2\approx1{,}618$ et $\psi=\tfrac{1-\sqrt5}2\approx-0{,}618$. La première ligne de $(\mathbf{A}-\lambda\mathbf{I})\mathbf{v}=\mathbf{0}$ s’écrit $(1-\lambda)v_1+v_2=0$ ; la seconde, $v_1-\lambda v_2=0$, lui est équivalente, car $p(\lambda)=0$. Des vecteurs propres sont $\mathbf s_1=(\varphi,\,1)^{\top}$ et $\mathbf s_2=(\psi,\,1)^{\top}$.

(b) $\mathbf{x}_0=(F_1,\,F_0)^{\top}=(1,\,0)^{\top}=c_1\mathbf s_1+c_2\mathbf s_2$ exige $c_1+c_2=0$ et $c_1\varphi+c_2\psi=1$, donc $c_1=1/(\varphi-\psi)=1/\sqrt5$ et $c_2=-1/\sqrt5$. D’après [(7.2)](#gl-7-2), $\mathbf{x}_k=\tfrac1{\sqrt5}(\varphi^k\mathbf s_1-\psi^k\mathbf s_2)$ ; la seconde composante est

$$F_k=\frac{\varphi^k-\psi^k}{\sqrt5} .$$

Pour $k=5$ : $\varphi^5=\tfrac{11+5\sqrt5}2$ et $\psi^5=\tfrac{11-5\sqrt5}2$, donc $F_5=\tfrac{5\sqrt5}{\sqrt5}=5$. Numériquement : $\varphi^5\approx11{,}090$, $\psi^5\approx-0{,}090$, $(11{,}090+0{,}090)/2{,}236\approx5{,}000$.

(c) Comme $|\psi|<1$, $\psi^k$ tend vers zéro, et $F_{k+1}/F_k$ tend vers $\varphi\approx1{,}618$, le nombre d’or. La part associée à la valeur propre de plus grand module l’emporte, comme dans la section [7.3](#stufe-7-3) ; chaque pas supplémentaire la multiplie par $\varphi$.
:::
:::

:::aufgabe Exercice 23 ★★ Décomposition spectrale
<span class="anker" id="aufg-23"></span>

<ol class="al">

<li>

Écrivez $\mathbf{A}=\bigl(\begin{smallmatrix}3&4\\4&-3\end{smallmatrix}\bigr)$ sous la forme $\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top}$ et comme somme $\lambda_1\mathbf{q}_1\mathbf{q}_1^{\top}+\lambda_2\mathbf{q}_2\mathbf{q}_2^{\top}$.

</li>

<li>

Déterminez les axes principaux de la forme $3x_1^2+8x_1x_2-3x_2^2$ et écrivez-la sous la forme $\lambda_1c_1^2+\lambda_2c_2^2$. De quelle forme de base de la section [5.3](quadratische-formen.html#stufe-5-3) s’agit-il ?

</li>

<li>

La matrice $\Bigl(\begin{smallmatrix}2&0&0\\0&3&1\\0&1&3\end{smallmatrix}\Bigr)$ admet $2$ comme valeur propre double. Donnez une base orthonormée de vecteurs propres. Est-elle unique ?

</li>

</ol>

:::loesung
(a) Trace $0$, déterminant $-9-16=-25$, donc $\lambda^2-25=0$ et $\lambda=\pm5$. Pour $5$ : $\bigl(\begin{smallmatrix}-2&4\\4&-8\end{smallmatrix}\bigr)$, $\mathbf{q}_1=(2,\,1)^{\top}/\sqrt5$. Pour $-5$ : $\bigl(\begin{smallmatrix}8&4\\4&2\end{smallmatrix}\bigr)$, $\mathbf{q}_2=(1,\,-2)^{\top}/\sqrt5$. Avec $\mathbf{Q}=\tfrac1{\sqrt5}\bigl(\begin{smallmatrix}2&1\\1&-2\end{smallmatrix}\bigr)$ et $\boldsymbol{\Lambda}=\operatorname{diag}(5;\,-5)$, on a $\mathbf{A}=\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top}$, et

$$5\cdot\frac15\begin{pmatrix}4&2\\2&1\end{pmatrix}-5\cdot\frac15\begin{pmatrix}1&-2\\-2&4\end{pmatrix}=\begin{pmatrix}3&4\\4&-3\end{pmatrix}.$$

(b) La forme a exactement cette matrice. Avec $c_1=(2x_1+x_2)/\sqrt5$ et $c_2=(x_1-2x_2)/\sqrt5$, on a

$$3x_1^2+8x_1x_2-3x_2^2=5c_1^2-5c_2^2=(2x_1+x_2)^2-(x_1-2x_2)^2 ,$$

soit, après développement, $4x_1^2+4x_1x_2+x_2^2-x_1^2+4x_1x_2-4x_2^2$. Les axes principaux sont dirigés selon $(2,\,1)^{\top}$ et $(1,\,-2)^{\top}$. Une valeur propre est positive, l’autre négative : c’est une selle dont les axes sont tournés par rapport aux axes de coordonnées.

(c) $\mathbf{e}_1$ est un vecteur propre associé à $2$. Le bloc inférieur $\bigl(\begin{smallmatrix}3&1\\1&3\end{smallmatrix}\bigr)$ a les valeurs propres $4$, avec $(1,\,1)^{\top}$, et $2$, avec $(1,\,-1)^{\top}$. Une base orthonormée de vecteurs propres est donc

$$\mathbf{e}_1,\qquad \tfrac1{\sqrt2}(0,\,1,\,-1)^{\top}\quad\text{associé à }2,\qquad \tfrac1{\sqrt2}(0,\,1,\,1)^{\top}\quad\text{associé à }4 .$$

Elle n’est pas unique. Le sous-espace propre associé à $2$ est le plan engendré par $\mathbf{e}_1$ et $(0,\,1,\,-1)^{\top}$, et toute base orthonormée de ce plan convient, par exemple $\tfrac1{\sqrt2}\bigl(\mathbf{e}_1+\tfrac1{\sqrt2}(0,1,-1)^{\top}\bigr)$ et $\tfrac1{\sqrt2}\bigl(\mathbf{e}_1-\tfrac1{\sqrt2}(0,1,-1)^{\top}\bigr)$. Seul le vecteur propre associé à la valeur propre simple $4$ est unique, au signe près.
:::
:::

---
title: La pseudo-inverse
pfad: Informatique / Apprentissage automatique / Fondements mathématiques / Projection, valeurs propres et décompositions
knoten: Fondements 2 : Projection, valeurs propres et décompositions
nachschlagen: ja
order: 15221200
summary: Dans Fondements 1, seule une matrice carrée à colonnes indépendantes avait une inverse.
tags: inverse à gauche, inverse à droite, pseudo-inverse
lang: fr
---

<span class="anker" id="stufe-11"></span>

:::zweck
Dans [Fondements 1](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/vektoren-und-matrizen.html), seule une matrice carrée à colonnes indépendantes avait une inverse. Cette section donne à toute matrice une sorte d’inverse : une qui inverse à gauche lorsqu’il y a plus d’équations que d’inconnues, une qui inverse à droite lorsqu’il y en a moins, et une pour tous les cas, la pseudo-inverse. Celle-ci fournit toujours une meilleure solution approchée et, s’il y en a plusieurs, la plus courte.
:::

### Inverses à gauche

<span class="anker" id="stufe-11-1"></span>

Une matrice haute $\mathbf{A}\in\mathbb{R}^{m\times n}$ avec $m>n$ n’a pas d’inverse ; elle n’est même pas carrée. Elle peut cependant posséder une moitié de la propriété d’une inverse.

:::definition Définition 11.1 (Inverse à gauche)
<span class="anker" id="satz-11-1"></span>

Une matrice $\mathbf F\in\mathbb{R}^{n\times m}$ telle que $\mathbf F\mathbf{A}=\mathbf{I}_n$ est appelée __inverse à gauche__ de $\mathbf{A}\in\mathbb{R}^{m\times n}$.
:::

:::satz Théorème 11.2 (Inverse à gauche)
<span class="anker" id="satz-11-2"></span>

$\mathbf{A}$ a une inverse à gauche si et seulement si ses colonnes sont linéairement indépendantes. Dans ce cas,

<span class="anker" id="gl-11-1"></span>
$$\mathbf F=(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top} \tag{11.1}$$

est une inverse à gauche, et $\mathbf F\mathbf{y}$ est la meilleure solution approchée de $\mathbf{A}\mathbf{x}=\mathbf{y}$.
:::

:::beweis Inverse à gauche
Si les colonnes sont indépendantes, $\mathbf{A}^{\top}\mathbf{A}$ est inversible d’après la section [3.5](die-beste-naherungslosung.html#stufe-3-5), et $(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}\mathbf{A}=\mathbf{I}$. D’après [(3.5)](die-beste-naherungslosung.html#gl-3-5), $\mathbf F\mathbf{y}=\hat{\mathbf{x}}$. Inversement, si $\mathbf{A}$ a une inverse à gauche et si $\mathbf{A}\mathbf{x}=\mathbf{0}$, alors $\mathbf{x}=\mathbf F\mathbf{A}\mathbf{x}=\mathbf F\mathbf{0}=\mathbf{0}$ ; le noyau est donc $\{\mathbf{0}\}$, et les colonnes sont indépendantes.
:::

$\mathbf F$ n’inverse pas à droite. D’après [(4.1)](projektion-auf-einen-unterraum.html#gl-4-1), le produit $\mathbf{A}\mathbf F=\mathbf{A}(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}$ est la projection sur l’espace des colonnes, et pour $m>n$, ce n’est pas $\mathbf{I}_m$. Une matrice haute a en outre beaucoup d’inverses à gauche ; [(11.1)](#gl-11-1) est celle qui correspond à la projection orthogonale.

::::beispiel [Exemple de calcul]
Pour $\mathbf{H}$, de colonnes $(1,\,0,\,1)^{\top}$ et $(0,\,1,\,1)^{\top}$, on a $(\mathbf{H}^{\top}\mathbf{H})^{-1}=\tfrac13\bigl(\begin{smallmatrix}2&-1\\-1&2\end{smallmatrix}\bigr)$ et

$$\mathbf F=\frac13\begin{pmatrix}2&-1\\-1&2\end{pmatrix}\begin{pmatrix}1&0&1\\0&1&1\end{pmatrix}=\frac13\begin{pmatrix}2&-1&1\\-1&2&1\end{pmatrix}.$$

On a $\mathbf F\mathbf{H}=\tfrac13\bigl(\begin{smallmatrix}2+1&-1+1\\-1+1&2+1\end{smallmatrix}\bigr)=\mathbf{I}_2$, et $\mathbf F(1,\,1,\,1)^{\top}=(\tfrac23,\,\tfrac23)^{\top}$ est la meilleure solution approchée de la section [3.3](die-beste-naherungslosung.html#stufe-3-3). $\mathbf{H}\mathbf F$ est la matrice de projection $\tfrac13\Bigl(\begin{smallmatrix}2&-1&1\\-1&2&1\\1&1&2\end{smallmatrix}\Bigr)$ de la section [4.2](projektion-auf-einen-unterraum.html#stufe-4-2). Une autre inverse à gauche est $\bigl(\begin{smallmatrix}1&0&0\\0&1&0\end{smallmatrix}\bigr)$, car les deux premières lignes de $\mathbf{H}$ forment la matrice identité ; mais pour $(1,\,1,\,1)^{\top}$, elle ne fournit pas la meilleure solution approchée : elle donne $(1,\,1)^{\top}$.
::::

⁠**En bref :** Une matrice à colonnes indépendantes a pour inverse à gauche $(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}$ ; celle-ci envoie $\mathbf{y}$ sur la meilleure solution approchée.

### Inverses à droite

<span class="anker" id="stufe-11-2"></span>

Pour une matrice large avec $m<n$, il y a moins d’équations que d’inconnues. Si le système est résoluble, il a une infinité de solutions. Une inverse à droite en choisit une, et une solution bien particulière.

:::definition Définition 11.3 (Inverse à droite)
<span class="anker" id="satz-11-3"></span>

Une matrice $\mathbf G\in\mathbb{R}^{n\times m}$ telle que $\mathbf{A}\mathbf G=\mathbf{I}_m$ est appelée __inverse à droite__ de $\mathbf{A}\in\mathbb{R}^{m\times n}$.
:::

:::satz Théorème 11.4 (Inverse à droite et solution la plus courte)
<span class="anker" id="satz-11-4"></span>

Si les lignes de $\mathbf{A}$ sont linéairement indépendantes,

<span class="anker" id="gl-11-2"></span>
$$\mathbf G=\mathbf{A}^{\top}(\mathbf{A}\mathbf{A}^{\top})^{-1} \tag{11.2}$$

est une inverse à droite. $\mathbf{x}=\mathbf G\mathbf{y}$ résout $\mathbf{A}\mathbf{x}=\mathbf{y}$ pour tout $\mathbf{y}$, et c’est, parmi toutes les solutions, celle de plus petite longueur.
:::

:::beweis Inverse à droite
Les lignes de $\mathbf{A}$ sont les colonnes de $\mathbf{A}^{\top}$ ; d’après la section [3.5](die-beste-naherungslosung.html#stufe-3-5), appliquée à $\mathbf{A}^{\top}$, $\mathbf{A}\mathbf{A}^{\top}$ est inversible. Alors $\mathbf{A}\mathbf G=\mathbf{A}\mathbf{A}^{\top}(\mathbf{A}\mathbf{A}^{\top})^{-1}=\mathbf{I}$ et $\mathbf{A}\mathbf G\mathbf{y}=\mathbf{y}$. Si $\mathbf{x}$ est une solution quelconque, alors $\mathbf{A}(\mathbf{x}-\mathbf G\mathbf{y})=\mathbf{0}$ ; $\mathbf{z}=\mathbf{x}-\mathbf G\mathbf{y}$ appartient donc au noyau. Le vecteur $\mathbf G\mathbf{y}=\mathbf{A}^{\top}\mathbf{w}$, avec $\mathbf{w}=(\mathbf{A}\mathbf{A}^{\top})^{-1}\mathbf{y}$, est perpendiculaire à tout vecteur du noyau, car $(\mathbf{A}^{\top}\mathbf{w})^{\top}\mathbf{z}=\mathbf{w}^{\top}\mathbf{A}\mathbf{z}=0$. D’après le théorème de Pythagore,

$$\lVert\mathbf{x}\rVert^2=\lVert\mathbf G\mathbf{y}+\mathbf{z}\rVert^2=\lVert\mathbf G\mathbf{y}\rVert^2+\lVert\mathbf{z}\rVert^2\ge\lVert\mathbf G\mathbf{y}\rVert^2 ,$$

avec égalité seulement pour $\mathbf{z}=\mathbf{0}$.
:::

Géométriquement, l’ensemble des solutions est une droite ou un plan qui ne passe pas par l’origine, et $\mathbf G\mathbf{y}$ en est le point le plus proche de l’origine : le pied de la perpendiculaire abaissée de l’origine.

::::beispiel [Exemple de calcul]
L’équation unique $x_1+2x_2=5$ a $\mathbf{A}=(1\ \ 2)$ et $\mathbf{A}\mathbf{A}^{\top}=5$. Donc $\mathbf G=\tfrac15(1,\,2)^{\top}$ et $\mathbf G\cdot5=(1,\,2)^{\top}$. Toutes les solutions s’écrivent $(1,\,2)^{\top}+t\,(2,\,-1)^{\top}$, de carré de longueur $(1+2t)^2+(2-t)^2=5+5t^2$ ; la solution la plus courte est obtenue pour $t=0$. Le vecteur $(1,\,2)^{\top}$ est perpendiculaire à la droite des solutions, dont la direction est $(2,\,-1)^{\top}$.
::::

⁠**En bref :** Une matrice à lignes indépendantes a pour inverse à droite $\mathbf{A}^{\top}(\mathbf{A}\mathbf{A}^{\top})^{-1}$ ; celle-ci fournit la solution la plus courte.

### La pseudo-inverse

<span class="anker" id="stufe-11-3"></span>

Si $\mathbf{A}$ n’a ni colonnes indépendantes ni lignes indépendantes, les deux formules échouent. Un exemple est $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ de la section [3.5](die-beste-naherungslosung.html#stufe-3-5) : pour $\mathbf{y}=(1,\,1)^{\top}$, chaque point de la droite $x_1+2x_2=\tfrac35$ est une meilleure solution approchée. La décomposition en valeurs singulières fournit une formule pour toute matrice.

:::definition Définition 11.5 (Pseudo-inverse)
<span class="anker" id="satz-11-5"></span>

Soit $\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$ de rang $r$. La matrice $\mathbf{D}^+\in\mathbb{R}^{n\times m}$ s’obtient à partir de $\mathbf{D}^{\top}$ en remplaçant chaque $d_j>0$ par $1/d_j$ ; les zéros restent. La __pseudo-inverse__ de $\mathbf{A}$ est

<span class="anker" id="gl-11-3"></span>
$$\mathbf{A}^+=\mathbf{V}\mathbf{D}^+\mathbf{U}^{\top}=\sum_{j=1}^r\frac1{d_j}\,\mathbf{v}_j\mathbf{u}_j^{\top} . \tag{11.3}$$
:::

Chaque brique inverse une brique de $\mathbf{A}$ : $\mathbf{A}$ envoie $\mathbf{v}_j$ sur $d_j\mathbf{u}_j$, $\mathbf{A}^+$ envoie $\mathbf{u}_j$ sur $\mathbf{v}_j/d_j$. Les directions $\mathbf{u}_j$ avec $j>r$, que $\mathbf{A}$ n’atteint pas, $\mathbf{A}^+$ les envoie sur zéro au lieu de diviser par zéro. Si $\mathbf{A}$ est inversible, alors $\mathbf{A}^+=\mathbf{A}^{-1}$, car dans ce cas $\mathbf{A}^{-1}=(\mathbf{V}^{\top})^{-1}\mathbf{D}^{-1}\mathbf{U}^{-1}=\mathbf{V}\mathbf{D}^{-1}\mathbf{U}^{\top}$.

::::beispiel [Exemple de calcul]
$\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ est symétrique et semi-définie positive, de valeur propre $5$ associée à $\mathbf{q}=(1,\,2)^{\top}/\sqrt5$ et de valeur propre $0$. D’après la section [9.7](die-singularwertzerlegung.html#stufe-9-7), $\mathbf{A}=5\,\mathbf{q}\mathbf{q}^{\top}$ est sa décomposition compacte, avec $d_1=5$ et $\mathbf{u}_1=\mathbf{v}_1=\mathbf{q}$. Donc

$$\mathbf{A}^+=\frac15\,\mathbf{q}\mathbf{q}^{\top}=\frac1{25}\begin{pmatrix}1&2\\2&4\end{pmatrix}.$$
::::

⁠**En bref :** La pseudo-inverse $\mathbf{A}^+=\mathbf{V}\mathbf{D}^+\mathbf{U}^{\top}$ inverse chaque brique $d_j\mathbf{u}_j\mathbf{v}_j^{\top}$ avec $d_j>0$ et envoie sur zéro les directions associées à la valeur singulière $0$.

### La meilleure solution approchée la plus courte

<span class="anker" id="stufe-11-4"></span>

Que fournit $\mathbf{A}^+\mathbf{y}$ ? Ce vecteur réunit les deux sous-sections précédentes.

:::satz Théorème 11.6 (Pseudo-inverse et moindres carrés)
<span class="anker" id="satz-11-6"></span>

Pour toute matrice $\mathbf{A}$ et tout vecteur $\mathbf{y}$, $\mathbf{x}^+=\mathbf{A}^+\mathbf{y}$ est une meilleure solution approchée de $\mathbf{A}\mathbf{x}=\mathbf{y}$, et c’est, parmi toutes les meilleures solutions approchées, celle de plus petite longueur. En particulier,

$$\begin{gathered} \mathbf{A}^+=(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}\quad\text{si les colonnes sont indépendantes},\\ \mathbf{A}^+=\mathbf{A}^{\top}(\mathbf{A}\mathbf{A}^{\top})^{-1}\quad\text{si les lignes sont indépendantes}. \end{gathered}$$
:::

:::beweis Pseudo-inverse
On calcule dans les coordonnées des vecteurs singuliers : $\mathbf{c}=\mathbf{V}^{\top}\mathbf{x}$ et $\boldsymbol\beta=\mathbf{U}^{\top}\mathbf{y}$. Comme $\mathbf{U}^{\top}$ conserve les longueurs,

$$\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert^2=\lVert\mathbf{U}^{\top}\mathbf{y}-\mathbf{D}\mathbf{V}^{\top}\mathbf{x}\rVert^2=\lVert\boldsymbol\beta-\mathbf{D}\mathbf{c}\rVert^2=\sum_{j=1}^r(\beta_j-d_jc_j)^2+\sum_{j=r+1}^m\beta_j^2 .$$

La seconde somme ne dépend pas de $\mathbf{x}$. La première est nulle, donc aussi petite que possible, si et seulement si $c_j=\beta_j/d_j$ pour tout $j\le r$ ; les $c_j$ avec $j>r$ n’y apparaissent pas du tout. Les meilleures solutions approchées sont donc exactement les $\mathbf{x}=\mathbf{V}\mathbf{c}$ avec $c_j=\beta_j/d_j$ pour $j\le r$ et $c_{r+1},\dots,c_n$ quelconques. Leur longueur vérifie $\lVert\mathbf{x}\rVert^2=\lVert\mathbf{c}\rVert^2=\sum_{j\le r}(\beta_j/d_j)^2+\sum_{j>r}c_j^2$ ; elle est minimale pour $c_j=0$ lorsque $j>r$. Ce $\mathbf{c}$ est $\mathbf{D}^+\boldsymbol\beta$, donc $\mathbf{x}=\mathbf{V}\mathbf{D}^+\mathbf{U}^{\top}\mathbf{y}=\mathbf{A}^+\mathbf{y}$.

Si les colonnes sont indépendantes, il n’y a, d’après la section [3.5](die-beste-naherungslosung.html#stufe-3-5), qu’une seule meilleure solution approchée, $(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}\mathbf{y}$ ; elle doit coïncider avec $\mathbf{A}^+\mathbf{y}$, et ce pour tout $\mathbf{y}$. Si les lignes sont indépendantes, le rang vaut $m$ d’après [Fondements 1, section 13.4](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/unabhangigkeit-basis-und-rang.html#stufe-13-4) ; l’espace des colonnes est donc $\mathbb{R}^m$ tout entier, et le système est résoluble pour tout $\mathbf{y}$ ; les meilleures solutions approchées sont les solutions, et la plus courte est $\mathbf G\mathbf{y}$ d’après la section [11.2](#stufe-11-2).
:::

::::beispiel [Exemple de calcul 1]
Pour $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ et $\mathbf{y}=(1,\,1)^{\top}$, on a $\mathbf{x}^+=\tfrac1{25}(1+2,\ 2+4)^{\top}=(0{,}12;\ 0{,}24)^{\top}$. Ce vecteur est sur la droite des meilleures solutions approchées, car $0{,}12+2\cdot0{,}24=0{,}6=\tfrac35$, et il pointe dans la direction $(1,\,2)^{\top}$, perpendiculaire à cette droite : c’est son point le plus proche de l’origine.
::::

::::beispiel [Exemple de calcul 2]
Une même grandeur est mesurée trois fois, avec les résultats $4$, $5$ et $9$. Le système « $x=4$, $x=5$, $x=9$ » a pour matrice $\mathbf{1}\in\mathbb{R}^{3\times1}$, une colonne de uns. Elle a une colonne indépendante, donc $\mathbf{1}^+=(\mathbf{1}^{\top}\mathbf{1})^{-1}\mathbf{1}^{\top}=\tfrac13(1,\,1,\,1)$ et

$$x^+=\tfrac13\,\mathbf{1}^{\top}\mathbf{y}=\tfrac13\,(4+5+9)=6 ,$$

la moyenne (Fig. [27](#abb-27)). La moyenne de plusieurs mesures est la meilleure solution approchée du système qui tient chaque mesure pour exacte.

:::abbildung ml/k2rmittel 27
La pseudo-inverse de la colonne de uns appliquée aux valeurs mesurées $\mathbf{y}=(4,5,9)^{\top}$ : le produit scalaire avec $\mathbf{1}$ est la somme des valeurs mesurées ; divisée par $\mathbf{1}^{\top}\mathbf{1}=3$, elle donne la moyenne.
:::
::::

⁠**En bref :** Pour toute matrice, $\mathbf{A}^+\mathbf{y}$ est une meilleure solution approchée, et la plus courte s’il y en a plusieurs ; si les colonnes ou les lignes sont indépendantes, $\mathbf{A}^+$ est l’inverse à gauche ou à droite.

:::hintergrund Pourquoi la pseudo-inverse ne divise pas par zéro
La pseudo-inverse remplace $1/d_j$ par $0$ là où $d_j=0$. Cela semble arbitraire, mais découle d’un passage à la limite. La matrice $\mathbf{A}^{\top}\mathbf{A}+\delta^2\mathbf{I}$ est inversible pour tout $\delta\ne0$, car ses valeurs propres sont $d_j^2+\delta^2>0$. Dans les coordonnées des vecteurs singuliers, $(\mathbf{A}^{\top}\mathbf{A}+\delta^2\mathbf{I})^{-1}\mathbf{A}^{\top}$ multiplie la $j$-ième coordonnée par

$$\frac{d_j}{d_j^2+\delta^2}\ \xrightarrow{\ \delta\to0\ }\ \begin{cases}1/d_j&\text{pour }d_j>0,\\0&\text{pour }d_j=0.\end{cases}$$

Donc $\mathbf{A}^+=\lim_{\delta\to0}(\mathbf{A}^{\top}\mathbf{A}+\delta^2\mathbf{I})^{-1}\mathbf{A}^{\top}$ pour toute matrice. Ce passage à la limite révèle aussi un danger : la pseudo-inverse ne dépend pas continûment de la matrice. Pour $\operatorname{diag}(1;\,\varepsilon)$ avec $\varepsilon>0$ petit, la pseudo-inverse est $\operatorname{diag}(1;\,1/\varepsilon)$, énorme ; pour $\varepsilon=0$, elle vaut $\operatorname{diag}(1;\,0)$. Une valeur singulière minuscule, qui n’est non nulle qu’à cause d’erreurs de mesure ou d’arrondi, est énormément amplifiée par $\mathbf{A}^+$. C’est pourquoi les logiciels de calcul traitent comme nulles les valeurs singulières inférieures à un petit seuil. La section suivante mesure à quel point de petites valeurs singulières amplifient les erreurs.
:::

:::aufgabe Exercice 33 ★ Une inverse à gauche
<span class="anker" id="aufg-33"></span>

La droite des moindres carrés de la section [3.6](die-beste-naherungslosung.html#stufe-3-6) correspond à $\mathbf{A}=\Bigl(\begin{smallmatrix}1&0\\1&1\\1&2\end{smallmatrix}\Bigr)$.

<ol class="al">

<li>

Calculez l’inverse à gauche $\mathbf F=(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}$ et vérifiez $\mathbf F\mathbf{A}=\mathbf{I}$.

</li>

<li>

Appliquez $\mathbf F$ à $\mathbf{y}=(1,\,2,\,4)^{\top}$ et comparez avec la section [3.6](die-beste-naherungslosung.html#stufe-3-6).

</li>

<li>

Lisez sur les lignes de $\mathbf F$ comment l’ordonnée à l’origine et la pente de la droite des moindres carrés s’obtiennent pour des valeurs mesurées $y_1,y_2,y_3$ quelconques.

</li>

</ol>

:::loesung
(a) $\mathbf{A}^{\top}\mathbf{A}=\bigl(\begin{smallmatrix}3&3\\3&5\end{smallmatrix}\bigr)$, d’inverse $\tfrac16\bigl(\begin{smallmatrix}5&-3\\-3&3\end{smallmatrix}\bigr)$, donc

$$\mathbf F=\frac16\begin{pmatrix}5&-3\\-3&3\end{pmatrix}\begin{pmatrix}1&1&1\\0&1&2\end{pmatrix}=\frac16\begin{pmatrix}5&2&-1\\-3&0&3\end{pmatrix},\qquad \mathbf F\mathbf{A}=\frac16\begin{pmatrix}5+2-1&2-2\\-3+3&6\end{pmatrix}=\mathbf{I} .$$

(b) $\mathbf F(1,\,2,\,4)^{\top}=\tfrac16(5+4-4,\ -3+12)^{\top}=(\tfrac56,\,\tfrac32)^{\top}$, la droite des moindres carrés de la section [3.6](die-beste-naherungslosung.html#stufe-3-6).

(c) Pour des valeurs mesurées quelconques, l’ordonnée à l’origine vaut $\hat x_1=\tfrac16(5y_1+2y_2-y_3)$ et la pente $\hat x_2=\tfrac12(y_3-y_1)$. La somme des poids de l’ordonnée à l’origine vaut $1$ : si toutes les valeurs mesurées sont égales, l’ordonnée à l’origine est cette valeur. Pour trois abscisses de mesure équidistantes, la pente ne dépend que des deux points extrêmes ; le point du milieu n’influe que sur la hauteur de la droite.
:::
:::

:::aufgabe Exercice 34 ★★ Solutions les plus courtes
<span class="anker" id="aufg-34"></span>

<ol class="al">

<li>

Déterminez la pseudo-inverse de $\mathbf{A}=\bigl(\begin{smallmatrix}1&1\\1&1\end{smallmatrix}\bigr)$ et $\mathbf{x}^+$ pour $\mathbf{y}=(1,\,3)^{\top}$. Vérifiez que $\mathbf{x}^+$ est une meilleure solution approchée et qu’il n’en existe pas de plus courte.

</li>

<li>

Déterminez la solution la plus courte de $x_1+2x_2+2x_3=9$. Comparez sa longueur avec celle de la solution $(9,\,0,\,0)^{\top}$.

</li>

</ol>

:::loesung
(a) $\mathbf{A}=2\,\mathbf{q}\mathbf{q}^{\top}$ avec $\mathbf{q}=(1,\,1)^{\top}/\sqrt2$ ; comme la matrice est symétrique et semi-définie positive, c’est sa décomposition compacte, avec $d_1=2$ et $\mathbf{u}_1=\mathbf{v}_1=\mathbf{q}$. On en déduit $\mathbf{A}^+=\tfrac12\mathbf{q}\mathbf{q}^{\top}=\tfrac14\bigl(\begin{smallmatrix}1&1\\1&1\end{smallmatrix}\bigr)$ et $\mathbf{x}^+=\tfrac14(4,\,4)^{\top}=(1,\,1)^{\top}$. On a $\mathbf{A}\mathbf{x}^+=(2,\,2)^{\top}$, la projection de $(1,\,3)^{\top}$ sur la droite de direction $(1,\,1)^{\top}$, car $\tfrac{1+3}2(1,\,1)^{\top}=(2,\,2)^{\top}$. Les meilleures solutions approchées sont tous les $\mathbf{x}$ tels que $x_1+x_2=2$, c’est-à-dire $(1+s,\ 1-s)^{\top}$, de carré de longueur $2+2s^2$. La plus courte est celle obtenue pour $s=0$, et c’est $\mathbf{x}^+$.

(b) $\mathbf{A}=(1\ \ 2\ \ 2)$ a $\mathbf{A}\mathbf{A}^{\top}=9$ ; donc $\mathbf G=\tfrac19(1,\,2,\,2)^{\top}$, et la solution la plus courte est $\mathbf G\cdot9=(1,\,2,\,2)^{\top}$, de longueur $3$. La solution $(9,\,0,\,0)^{\top}$ a pour longueur $9$. La solution la plus courte pointe dans la direction du vecteur normal $(1,\,2,\,2)^{\top}$ du plan des solutions.
:::
:::

:::aufgabe Exercice 35 ★★★ Ce que projette la pseudo-inverse
<span class="anker" id="aufg-35"></span>

Soit $\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$ de rang $r$, et soient $\mathbf{U}_r$, $\mathbf{V}_r$ les matrices formées des $r$ premières colonnes de $\mathbf{U}$ et de $\mathbf{V}$.

<ol class="al">

<li>

Montrez que $\mathbf{A}\mathbf{A}^+=\mathbf{U}_r\mathbf{U}_r^{\top}$ et $\mathbf{A}^+\mathbf{A}=\mathbf{V}_r\mathbf{V}_r^{\top}$. Sur quels espaces ces matrices projettent-elles ?

</li>

<li>

Déduisez-en $\mathbf{A}\mathbf{A}^+\mathbf{A}=\mathbf{A}$ et $\mathbf{A}^+\mathbf{A}\mathbf{A}^+=\mathbf{A}^+$.

</li>

</ol>

:::loesung
(a) $\mathbf{A}\mathbf{A}^+=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}\mathbf{V}\mathbf{D}^+\mathbf{U}^{\top}=\mathbf{U}\mathbf{D}\mathbf{D}^+\mathbf{U}^{\top}$. La matrice $\mathbf{D}\mathbf{D}^+$, de taille $m\times m$, porte $d_j\cdot\tfrac1{d_j}=1$ aux $r$ premières places de la diagonale et des zéros partout ailleurs. Donc $\mathbf{A}\mathbf{A}^+=\sum_{j\le r}\mathbf{u}_j\mathbf{u}_j^{\top}=\mathbf{U}_r\mathbf{U}_r^{\top}$, c’est-à-dire, d’après [(4.2)](projektion-auf-einen-unterraum.html#gl-4-2), la projection orthogonale sur le sous-espace engendré par $\mathbf{u}_1,\dots,\mathbf{u}_r$, l’espace des colonnes de $\mathbf{A}$. De même, $\mathbf{A}^+\mathbf{A}=\mathbf{V}\mathbf{D}^+\mathbf{D}\mathbf{V}^{\top}=\mathbf{V}_r\mathbf{V}_r^{\top}$ est la projection sur le sous-espace engendré par $\mathbf{v}_1,\dots,\mathbf{v}_r$, l’espace des colonnes de $\mathbf{A}^{\top}$ ; c’est le supplémentaire orthogonal du noyau.

(b) Chaque colonne de $\mathbf{A}$ appartient à l’espace des colonnes, et la projection sur celui-ci la laisse fixe : $\mathbf{A}\mathbf{A}^+\mathbf{A}=(\mathbf{U}_r\mathbf{U}_r^{\top})\mathbf{A}=\mathbf{A}$. De même, chaque colonne de $\mathbf{A}^+=\sum_{j\le r}\tfrac1{d_j}\mathbf{v}_j\mathbf{u}_j^{\top}$ appartient au sous-espace engendré par $\mathbf{v}_1,\dots,\mathbf{v}_r$, donc $\mathbf{A}^+\mathbf{A}\mathbf{A}^+=(\mathbf{V}_r\mathbf{V}_r^{\top})\mathbf{A}^+=\mathbf{A}^+$.
:::
:::

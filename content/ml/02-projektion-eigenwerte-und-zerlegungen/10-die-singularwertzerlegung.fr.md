---
title: La décomposition en valeurs singulières
pfad: Informatique / Apprentissage automatique / Fondements mathématiques / Projection, valeurs propres et décompositions
knoten: Fondements 2 : Projection, valeurs propres et décompositions
nachschlagen: ja
order: 15221000
summary: Les vecteurs propres n’existent que pour les matrices carrées, et ils ne sont perpendiculaires que pour les matrices symétriques.
tags: valeurs singulières, vecteurs singuliers à droite, vecteur singulier à gauche, norme spectrale
lang: fr
---

<span class="anker" id="stufe-9"></span>

:::zweck
Les vecteurs propres n’existent que pour les matrices carrées, et ils ne sont perpendiculaires que pour les matrices symétriques. Cette section montre que toute matrice, même rectangulaire, possède une paire de repères orthogonaux : l’un dans l’espace des entrées et l’autre dans l’espace des sorties. La matrice envoie chaque axe de l’un sur un multiple d’un axe de l’autre. Il en résulte une décomposition de toute matrice en rotation, étirement et rotation.
:::

### Des directions perpendiculaires qui restent perpendiculaires

<span class="anker" id="stufe-9-1"></span>

La matrice $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$, étant triangulaire, a la valeur propre double $2$, mais une seule direction propre : $(\mathbf{A}-2\mathbf{I})\mathbf{v}=\mathbf{0}$ signifie $3v_2=0$, donc seuls les multiples de $\mathbf{e}_1$ conviennent (exercice [19](eigenwerte-und-eigenvektoren.html#aufg-19)). D’après la section [7.2](diagonalisierung-und-spektralsatz.html#stufe-7-2), elle n’est pas diagonalisable. Elle transforme pourtant le cercle unité en une ellipse (Fig. [23](#abb-23)), et une ellipse a deux axes perpendiculaires. Quelles flèches du cercle aboutissent sur ces axes ?

On cherche moins qu’un vecteur propre : une flèche a le droit de changer de direction. On cherche deux vecteurs unitaires perpendiculaires $\mathbf{v}_1$, $\mathbf{v}_2$ dont les images $\mathbf{A}\mathbf{v}_1$ et $\mathbf{A}\mathbf{v}_2$ sont de nouveau perpendiculaires. Que deux images soient perpendiculaires, c’est leur produit scalaire qui le dit :

$$(\mathbf{A}\mathbf{v}_1)^{\top}(\mathbf{A}\mathbf{v}_2)=\mathbf{v}_1^{\top}\,\mathbf{A}^{\top}\mathbf{A}\,\mathbf{v}_2 .$$

Ici apparaît la matrice de Gram $\mathbf{A}^{\top}\mathbf{A}$. Elle est symétrique, même si $\mathbf{A}$ ne l’est pas, et d’après le théorème spectral, elle possède une base orthonormée de vecteurs propres. Si $\mathbf{v}_2$ est un vecteur propre de $\mathbf{A}^{\top}\mathbf{A}$ associé à la valeur propre $\lambda_2$ et si $\mathbf{v}_1$ est perpendiculaire à $\mathbf{v}_2$, alors le produit scalaire vaut $\lambda_2\,\mathbf{v}_1^{\top}\mathbf{v}_2=0$. Les vecteurs propres de $\mathbf{A}^{\top}\mathbf{A}$ font donc ce que l’on souhaite. Le même calcul avec $\mathbf{v}_1=\mathbf{v}_2$ fournit les longueurs des images : $\lVert\mathbf{A}\mathbf{v}_i\rVert^2=\mathbf{v}_i^{\top}\mathbf{A}^{\top}\mathbf{A}\mathbf{v}_i=\lambda_i$.

⁠**Exemple de calcul :** Pour $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$, on a $\mathbf{A}^{\top}\mathbf{A}=\bigl(\begin{smallmatrix}4&6\\6&13\end{smallmatrix}\bigr)$, de trace $17$ et de déterminant $52-36=16$. Le polynôme caractéristique $\lambda^2-17\lambda+16=(\lambda-16)(\lambda-1)$ a pour racines $16$ et $1$. Des vecteurs propres normés sont $\mathbf{v}_1=(1,\,2)^{\top}/\sqrt5$ pour $16$ et $\mathbf{v}_2=(-2,\,1)^{\top}/\sqrt5$ pour $1$. Leurs images

$$\mathbf{A}\mathbf{v}_1=\frac1{\sqrt5}\begin{pmatrix}8\\4\end{pmatrix},\qquad \mathbf{A}\mathbf{v}_2=\frac1{\sqrt5}\begin{pmatrix}-1\\2\end{pmatrix}$$

ont pour produit scalaire $\tfrac15(-8+8)=0$ et pour longueurs $\sqrt{80/5}=4=\sqrt{16}$ et $1=\sqrt1$ (Fig. [22](#abb-22)).

:::abbildung ml/k2rsvdidee 22
Les images $\mathbf{A}\mathbf{v}_1=(8,4)^{\top}/\sqrt5$ et $\mathbf{A}\mathbf{v}_2=(-1,2)^{\top}/\sqrt5$ sont perpendiculaires et ont pour carrés de longueur $16$ et $1$, les valeurs propres de $\mathbf{A}^{\top}\mathbf{A}$.
:::

⁠**En bref :** Les vecteurs propres de la matrice symétrique $\mathbf{A}^{\top}\mathbf{A}$ sont des directions perpendiculaires dont les images par $\mathbf{A}$ sont de nouveau perpendiculaires ; les images ont pour longueurs $\sqrt{\lambda_i}$.

### Valeurs singulières

<span class="anker" id="stufe-9-2"></span>

Les longueurs des images sont les grandeurs caractéristiques les plus importantes d’une matrice : elles indiquent de combien la matrice étire dans ses directions principales. D’après la section [8.4](positiv-definite-matrizen.html#stufe-8-4), $\mathbf{A}^{\top}\mathbf{A}$ est semi-définie positive ; ses valeurs propres ne sont donc pas négatives, et l’on peut en prendre la racine.

:::definition Définition 9.1 (Valeurs singulières)
<span class="anker" id="satz-9-1"></span>

Soit $\mathbf{A}\in\mathbb{R}^{m\times n}$, et soient $\lambda_1\ge\lambda_2\ge\dots\ge\lambda_n\ge0$ les valeurs propres de $\mathbf{A}^{\top}\mathbf{A}$, classées par ordre décroissant, les valeurs multiples étant comptées avec leur multiplicité. Les nombres

<span class="anker" id="gl-9-1"></span>
$$d_j=\sqrt{\lambda_j},\qquad d_1\ge d_2\ge\dots\ge d_n\ge0 , \tag{9.1}$$

sont appelés les __valeurs singulières__ de $\mathbf{A}$.
:::

Beaucoup d’ouvrages écrivent $\sigma_j$ au lieu de $d_j$. Ici, les valeurs singulières portent toujours un indice ; le $d$ sans indice de Fondements 1, le nombre de caractéristiques, est autre chose.

:::satz Théorème 9.2 (Valeurs singulières et rang)
<span class="anker" id="satz-9-2"></span>

Le nombre de valeurs singulières non nulles est le rang de $\mathbf{A}$.
:::

:::beweis Valeurs singulières et rang
Soient $\mathbf{v}_1,\dots,\mathbf{v}_n$ des vecteurs propres orthonormés de $\mathbf{A}^{\top}\mathbf{A}$ associés à $\lambda_1,\dots,\lambda_n$. Tout vecteur s’écrit $\mathbf{x}=\sum_jc_j\mathbf{v}_j$, donc $\mathbf{A}\mathbf{x}=\sum_jc_j\,\mathbf{A}\mathbf{v}_j$ : l’espace des colonnes est engendré par les images $\mathbf{A}\mathbf{v}_1,\dots,\mathbf{A}\mathbf{v}_n$. D’après la sous-section précédente, celles-ci sont perpendiculaires deux à deux et ont pour longueurs $d_j$. Les images avec $d_j=0$ sont le vecteur nul et n’apportent rien. Les autres sont perpendiculaires entre elles et non nulles ; divisées par leurs longueurs, elles sont orthonormées et, d’après le théorème de la section [1.1](orthonormalbasen-und-orthogonale-matrizen.html#stufe-1-1), linéairement indépendantes. Elles forment une base de l’espace des colonnes, et leur nombre est le rang.
:::

Dans la suite, on note $r$ le rang d’une matrice. On a $d_1\ge\dots\ge d_r>0$ et $d_{r+1}=\dots=d_n=0$.

⁠**Exemple de calcul :** $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ a les valeurs singulières $d_1=4$ et $d_2=1$ et le rang $2$. Ses valeurs propres sont $2$ et $2$ : valeurs singulières et valeurs propres sont en général des nombres différents. La matrice $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ a $\mathbf{A}^{\top}\mathbf{A}=\bigl(\begin{smallmatrix}5&10\\10&20\end{smallmatrix}\bigr)$, de valeurs propres $25$ et $0$, donc les valeurs singulières $5$ et $0$ et le rang $1$.

⁠**En bref :** Les valeurs singulières $d_j$ sont les racines des valeurs propres de $\mathbf{A}^{\top}\mathbf{A}$ ; elles mesurent de combien $\mathbf{A}$ étire dans ses directions principales, et le nombre de valeurs singulières positives est le rang.

### Vecteurs singuliers

<span class="anker" id="stufe-9-3"></span>

À chaque valeur singulière positive correspondent deux directions : une direction d’entrée $\mathbf{v}_j$ et la direction de son image.

:::definition Définition 9.3 (Vecteurs singuliers)
<span class="anker" id="satz-9-3"></span>

Des vecteurs propres orthonormés $\mathbf{v}_1,\dots,\mathbf{v}_n$ de $\mathbf{A}^{\top}\mathbf{A}$ associés aux valeurs propres $d_1^2,\dots,d_n^2$ sont appelés __vecteurs singuliers à droite__ de $\mathbf{A}$. Pour $d_j>0$, on appelle

<span class="anker" id="gl-9-2"></span>
$$\mathbf{u}_j=\frac{\mathbf{A}\mathbf{v}_j}{d_j},\qquad\text{donc}\qquad \mathbf{A}\mathbf{v}_j=d_j\mathbf{u}_j , \tag{9.2}$$

le __vecteur singulier à gauche__ associé.
:::

Les noms viennent de la place qu’occupent ces vecteurs dans la décomposition de la sous-section suivante. Les vecteurs singuliers à gauche sont eux aussi orthonormés, car

$$\mathbf{u}_i^{\top}\mathbf{u}_j=\frac{\mathbf{v}_i^{\top}\mathbf{A}^{\top}\mathbf{A}\mathbf{v}_j}{d_id_j}=\frac{d_j^2\,\mathbf{v}_i^{\top}\mathbf{v}_j}{d_id_j},$$

et cela vaut $1$ pour $i=j$ et $0$ sinon. Ce sont les vecteurs propres de $\mathbf{A}\mathbf{A}^{\top}$, et l’on a l’égalité dans le sens inverse :

$$\mathbf{A}^{\top}\mathbf{u}_j=\frac{\mathbf{A}^{\top}\mathbf{A}\mathbf{v}_j}{d_j}=d_j\mathbf{v}_j,\qquad \mathbf{A}\mathbf{A}^{\top}\mathbf{u}_j=d_j\,\mathbf{A}\mathbf{v}_j=d_j^2\,\mathbf{u}_j .$$

$\mathbf{A}$ envoie $\mathbf{v}_j$ sur $d_j\mathbf{u}_j$, et $\mathbf{A}^{\top}$ envoie $\mathbf{u}_j$ sur $d_j\mathbf{v}_j$.

:::warnung Les signes vont de pair
Un vecteur propre n’est déterminé qu’au signe près. Si l’on calcule les $\mathbf{v}_j$ comme vecteurs propres de $\mathbf{A}^{\top}\mathbf{A}$ et, séparément, les $\mathbf{u}_j$ comme vecteurs propres de $\mathbf{A}\mathbf{A}^{\top}$, un $\mathbf{u}_j$ peut recevoir le mauvais signe, et alors $\mathbf{A}\mathbf{v}_j=-d_j\mathbf{u}_j$. La voie sûre passe par [(9.2)](#gl-9-2) : choisir d’abord $\mathbf{v}_j$, puis calculer $\mathbf{u}_j=\mathbf{A}\mathbf{v}_j/d_j$. Si l’on change à la fois le signe de $\mathbf{v}_j$ et celui de $\mathbf{u}_j$, tout reste correct.
:::

⁠**Exemple de calcul :** Pour $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$, on a $\mathbf{u}_1=\mathbf{A}\mathbf{v}_1/4=(2,\,1)^{\top}/\sqrt5$ et $\mathbf{u}_2=\mathbf{A}\mathbf{v}_2/1=(-1,\,2)^{\top}/\sqrt5$. Pour contrôle : $\mathbf{A}\mathbf{A}^{\top}=\bigl(\begin{smallmatrix}13&6\\6&4\end{smallmatrix}\bigr)$ envoie $(2,\,1)^{\top}$ sur $(32,\,16)^{\top}=16\,(2,\,1)^{\top}$. Le vecteur $(-2,\,-1)^{\top}/\sqrt5$ serait lui aussi un vecteur propre normé de $\mathbf{A}\mathbf{A}^{\top}$ associé à $16$, mais avec lui, on aurait $\mathbf{A}\mathbf{v}_1=-4\,\mathbf{u}_1$.

⁠**En bref :** Les vecteurs singuliers à droite $\mathbf{v}_j$ sont des vecteurs propres de $\mathbf{A}^{\top}\mathbf{A}$, ceux à gauche sont $\mathbf{u}_j=\mathbf{A}\mathbf{v}_j/d_j$ ; les deux familles sont orthonormées, et $\mathbf{A}\mathbf{v}_j=d_j\mathbf{u}_j$.

### La décomposition

<span class="anker" id="stufe-9-4"></span>

Si l’on écrit côte à côte les égalités $\mathbf{A}\mathbf{v}_j=d_j\mathbf{u}_j$ pour tous les $j$, on obtient une décomposition de la matrice entière.

:::satz Théorème 9.4 (Décomposition en valeurs singulières)
<span class="anker" id="satz-9-4"></span>

Toute matrice $\mathbf{A}\in\mathbb{R}^{m\times n}$ de rang $r$ peut s’écrire

<span class="anker" id="gl-9-3"></span>
$$\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top} \tag{9.3}$$

avec des matrices orthogonales $\mathbf{U}\in\mathbb{R}^{m\times m}$ et $\mathbf{V}\in\mathbb{R}^{n\times n}$ et une matrice $\mathbf{D}\in\mathbb{R}^{m\times n}$ qui porte sur sa diagonale les valeurs singulières $d_1\ge\dots\ge d_r>0$ et ne contient sinon que des zéros. Les colonnes de $\mathbf{V}$ sont des vecteurs singuliers à droite, les $r$ premières colonnes de $\mathbf{U}$ les vecteurs singuliers à gauche associés. Une formulation équivalente est la forme compacte

<span class="anker" id="gl-9-4"></span>
$$\mathbf{A}=\sum_{j=1}^rd_j\,\mathbf{u}_j\mathbf{v}_j^{\top} . \tag{9.4}$$
:::

:::beweis Décomposition en valeurs singulières
Pour $j\le r$, on a $\mathbf{A}\mathbf{v}_j=d_j\mathbf{u}_j$. Pour $j>r$, on a $d_j=0$, donc $\lVert\mathbf{A}\mathbf{v}_j\rVert=0$ et $\mathbf{A}\mathbf{v}_j=\mathbf{0}$. Si $r<m$, on complète $\mathbf{u}_1,\dots,\mathbf{u}_r$ en une base orthonormée de $\mathbb{R}^m$, par exemple avec le procédé de Gram-Schmidt, comme dans la preuve du théorème spectral. D’après Fondements 1, section 9.2, la colonne $j$ de $\mathbf{A}\mathbf{V}$ est le vecteur $\mathbf{A}\mathbf{v}_j$, et la colonne $j$ de $\mathbf{U}\mathbf{D}$ vaut $d_j\mathbf{u}_j$ pour $j\le r$ et sinon le vecteur nul. Donc $\mathbf{A}\mathbf{V}=\mathbf{U}\mathbf{D}$. Comme $\mathbf{V}$ est orthogonale, $\mathbf{V}\mathbf{V}^{\top}=\mathbf{I}$, et la multiplication à droite par $\mathbf{V}^{\top}$ donne $\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$. La forme compacte découle de Fondements 1, section 9.5 : colonne $j$ de $\mathbf{U}\mathbf{D}$ fois ligne $j$ de $\mathbf{V}^{\top}$, sommé sur $j$ ; seuls les termes avec $j\le r$ sont non nuls.
:::

Le format de $\mathbf{D}$ suit celui de $\mathbf{A}$. Pour $m=3$ et $n=2$, par exemple, $\mathbf{D}=\Bigl(\begin{smallmatrix}d_1&0\\0&d_2\\0&0\end{smallmatrix}\Bigr)$. L’abréviation usuelle est SVD, d’après le nom anglais *singular value decomposition*.

⁠**Exemple de calcul :** Pour $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$, on a

$$\mathbf{A}=\underbrace{\frac1{\sqrt5}\begin{pmatrix}2&-1\\1&2\end{pmatrix}}_{\mathbf{U}}\underbrace{\begin{pmatrix}4&0\\0&1\end{pmatrix}}_{\mathbf{D}}\underbrace{\frac1{\sqrt5}\begin{pmatrix}1&2\\-2&1\end{pmatrix}}_{\mathbf{V}^{\top}},$$

car $\mathbf{U}\mathbf{D}=\tfrac1{\sqrt5}\bigl(\begin{smallmatrix}8&-1\\4&2\end{smallmatrix}\bigr)$ et $\mathbf{U}\mathbf{D}\mathbf{V}^{\top}=\tfrac15\bigl(\begin{smallmatrix}8+2&16-1\\4-4&8+2\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$. Sous forme compacte :

$$4\cdot\frac15\begin{pmatrix}2&4\\1&2\end{pmatrix}+1\cdot\frac15\begin{pmatrix}2&-1\\-4&2\end{pmatrix}=\begin{pmatrix}1{,}6&3{,}2\\0{,}8&1{,}6\end{pmatrix}+\begin{pmatrix}0{,}4&-0{,}2\\-0{,}8&0{,}4\end{pmatrix}=\begin{pmatrix}2&3\\0&2\end{pmatrix}.$$

⁠**En bref :** Toute matrice s’écrit $\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$, avec deux matrices orthogonales et les valeurs singulières sur la diagonale de $\mathbf{D}$, ou, de façon équivalente, comme une somme $\sum_jd_j\mathbf{u}_j\mathbf{v}_j^{\top}$.

:::hintergrund Pourquoi la décomposition existe pour toute matrice
Toutes les matrices n’ont pas de vecteurs propres, et leurs vecteurs propres ne sont pas toujours perpendiculaires. La décomposition en valeurs singulières contourne ces deux obstacles grâce à une astuce : elle n’utilise pas les vecteurs propres de $\mathbf{A}$, mais ceux de $\mathbf{A}^{\top}\mathbf{A}$. Cette matrice est symétrique et semi-définie positive pour tout $\mathbf{A}$, et pour elle, le théorème spectral garantit une base orthonormée de vecteurs propres, de valeurs propres $\ge0$. Le prix à payer : il faut deux bases au lieu d’une, l’une pour les entrées et l’autre pour les sorties.

On peut aussi décrire les vecteurs singuliers sans $\mathbf{A}^{\top}\mathbf{A}$. D’après [(8.2)](positiv-definite-matrizen.html#gl-8-2), appliqué à $\mathbf{A}^{\top}\mathbf{A}$, on a pour des vecteurs unitaires $\lVert\mathbf{A}\mathbf{v}\rVert^2=\mathbf{v}^{\top}\mathbf{A}^{\top}\mathbf{A}\mathbf{v}\le\lambda_1=d_1^2$, avec égalité en $\mathbf{v}_1$. Ainsi, $\mathbf{v}_1$ est la direction que $\mathbf{A}$ étire le plus, et $d_1$ est cet étirement maximal. Parmi tous les vecteurs unitaires perpendiculaires à $\mathbf{v}_1$, c’est $\mathbf{v}_2$ qui est le plus étiré, et ainsi de suite ; c’est ce que montre le même calcul de moyenne que dans la preuve de [(8.2)](positiv-definite-matrizen.html#gl-8-2), avec $c_1=0$. La décomposition énumère donc les directions dans l’ordre, de l’étirement le plus fort au plus faible.

Les valeurs singulières sont uniques. Si tous les $d_j$ sont distincts et positifs, chaque paire $\mathbf{v}_j,\mathbf{u}_j$ est déterminée à un signe commun près. Si des valeurs singulières sont égales, il y a davantage de liberté : une matrice orthogonale $\mathbf{Q}$ n’a que des valeurs singulières égales à $1$, et pour toute matrice orthogonale $\mathbf{V}$, $\mathbf{Q}=(\mathbf{Q}\mathbf{V})\,\mathbf{I}\,\mathbf{V}^{\top}$ est une décomposition en valeurs singulières.
:::

### Rotation, étirement, rotation

<span class="anker" id="stufe-9-5"></span>

Si l’on lit $\mathbf{A}\mathbf{x}=\mathbf{U}\bigl(\mathbf{D}(\mathbf{V}^{\top}\mathbf{x})\bigr)$ de droite à gauche, toute matrice agit en trois étapes (Fig. [23](#abb-23)) :

<ol>

<li>

$\mathbf{V}^{\top}\mathbf{x}$ calcule, d’après [(1.2)](orthonormalbasen-und-orthogonale-matrizen.html#gl-1-2), les coordonnées $c_j=\mathbf{v}_j^{\top}\mathbf{x}$ de $\mathbf{x}$ dans la base des $\mathbf{v}_j$. Géométriquement, c’est une rotation ou une réflexion qui amène $\mathbf{v}_j$ sur $\mathbf{e}_j$.

</li>

<li>

$\mathbf{D}$ multiplie chaque coordonnée $c_j$ par $d_j$. Si $m>n$, $\mathbf{D}$ ajoute des zéros ; si $m<n$, $\mathbf{D}$ supprime les dernières coordonnées. Le cercle unité devient une ellipse dont les axes sont portés par les axes de coordonnées.

</li>

<li>

$\mathbf{U}$ amène $\mathbf{e}_j$ sur $\mathbf{u}_j$, de nouveau par une rotation ou une réflexion.

</li>

</ol>

Toute application linéaire est donc, aux réflexions près, une rotation, un étirement le long des axes et encore une rotation. Elle transforme le cercle unité en une ellipse et la sphère unité en un ellipsoïde, de demi-axes $d_j\mathbf{u}_j$. Si $\det\mathbf{A}<0$, il y a au moins une réflexion, car d’après Fondements 1, section 14.5, $\det\mathbf{A}=\det\mathbf{U}\cdot\det\mathbf{D}\cdot\det\mathbf{V}^{\top}$, et $\det\mathbf{D}\ge0$.

:::abbildung ml/k2svd 23
La matrice $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ comme rotation, étirement, rotation. En haut à gauche, le cercle unité avec $\mathbf{v}_1=(1,2)^{\top}/\sqrt5$ (en rouge) et $\mathbf{v}_2=(-2,1)^{\top}/\sqrt5$ (en vert). $\mathbf{V}^{\top}$ fait tourner de $-63{,}4^\circ$ et amène $\mathbf{v}_1$ sur $\mathbf{e}_1$ et $\mathbf{v}_2$ sur $\mathbf{e}_2$ (en bas à gauche). $\mathbf{D}$ étire le premier axe d’un facteur $d_1=4$ et le second d’un facteur $d_2=1$ (en bas à droite). $\mathbf{U}$ fait tourner de $26{,}6^\circ$ et amène les axes sur $\mathbf{u}_1=(2,1)^{\top}/\sqrt5$ et $\mathbf{u}_2=(-1,2)^{\top}/\sqrt5$ (en haut à droite). Le point noir $\mathbf{x}=\mathbf{e}_2$ aboutit, quel que soit le chemin, en $\mathbf{A}\mathbf{x}=(3,2)^{\top}$. Le chemin direct, en haut, est $\mathbf{A}$ elle-même : le cercle unité devient l’ellipse de demi-axes $4\,\mathbf{u}_1$ et $1\cdot\mathbf{u}_2$.
:::

⁠**Exemple de calcul :** Pour $\mathbf{x}=\mathbf{e}_2$ et $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$, les coordonnées sont $\mathbf{V}^{\top}\mathbf{x}=(2,\,1)^{\top}/\sqrt5$. Après étirement, on obtient $\mathbf{D}\mathbf{V}^{\top}\mathbf{x}=(8,\,1)^{\top}/\sqrt5$, et après rotation

$$\mathbf{U}\mathbf{D}\mathbf{V}^{\top}\mathbf{x}=\frac15\begin{pmatrix}2&-1\\1&2\end{pmatrix}\begin{pmatrix}8\\1\end{pmatrix}=\frac15\begin{pmatrix}15\\10\end{pmatrix}=\begin{pmatrix}3\\2\end{pmatrix}=\mathbf{A}\mathbf{e}_2 .$$

$\mathbf{V}$ a pour colonnes $(\cos\theta,\,\sin\theta)^{\top}$ et $(-\sin\theta,\,\cos\theta)^{\top}$ avec $\cos\theta=1/\sqrt5$ ; c’est donc la rotation d’angle $\theta\approx63{,}4^\circ$, et $\mathbf{V}^{\top}$ annule cette rotation en tournant de $-63{,}4^\circ$. $\mathbf{U}$ est la rotation d’angle $26{,}6^\circ$, car $\cos26{,}6^\circ\approx2/\sqrt5$.

⁠**En bref :** Toute matrice fait tourner, étire le long des axes et fait de nouveau tourner, aux réflexions près ; le cercle unité devient une ellipse de demi-axes $d_j\mathbf{u}_j$.

### Briques de rang 1 et espaces d’une matrice

<span class="anker" id="stufe-9-6"></span>

Chaque terme $d_j\mathbf{u}_j\mathbf{v}_j^{\top}$ de la forme compacte [(9.4)](#gl-9-4) est de rang $1$, car toutes ses colonnes sont des multiples de $\mathbf{u}_j$. Il agit ainsi sur un vecteur :

$$d_j\mathbf{u}_j\mathbf{v}_j^{\top}\mathbf{x}=d_j\,(\mathbf{v}_j^{\top}\mathbf{x})\,\mathbf{u}_j .$$

Il lit la coordonnée de $\mathbf{x}$ le long de $\mathbf{v}_j$, la multiplie par $d_j$ et renvoie le résultat dans la direction $\mathbf{u}_j$. La matrice est la somme de $r$ telles briques, classées selon leur taille $d_j$. Au passage, la décomposition fournit des bases orthonormées des sous-espaces associés à une matrice.

:::satz Théorème 9.5 (Ce qu’engendrent les vecteurs singuliers)
<span class="anker" id="satz-9-5"></span>

Soit $\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$ de rang $r$. Alors :

<ol class="rm">

<li>

$\mathbf{u}_1,\dots,\mathbf{u}_r$ est une base orthonormée de l’espace des colonnes de $\mathbf{A}$, et $\mathbf{u}_{r+1},\dots,\mathbf{u}_m$ une base orthonormée de son supplémentaire orthogonal ;

</li>

<li>

$\mathbf{v}_{r+1},\dots,\mathbf{v}_n$ est une base orthonormée du noyau de $\mathbf{A}$, et $\mathbf{v}_1,\dots,\mathbf{v}_r$ une base orthonormée de l’espace des colonnes de $\mathbf{A}^{\top}$.

</li>

</ol>
:::

:::beweis Espaces
(i) Tout $\mathbf{A}\mathbf{x}=\sum_{j\le r}d_j(\mathbf{v}_j^{\top}\mathbf{x})\mathbf{u}_j$ appartient au sous-espace engendré par $\mathbf{u}_1,\dots,\mathbf{u}_r$, et inversement $\mathbf{u}_j=\mathbf{A}(\mathbf{v}_j/d_j)$ est une image. Les autres colonnes de $\mathbf{U}$ sont perpendiculaires à celles-ci et engendrent donc, d’après la section [4.4](projektion-auf-einen-unterraum.html#stufe-4-4), le supplémentaire orthogonal. (ii) Comme les $\mathbf{u}_j$ sont indépendants et les $d_j$ positifs, on a $\mathbf{A}\mathbf{x}=\mathbf{0}$ si et seulement si $\mathbf{v}_j^{\top}\mathbf{x}=0$ pour tout $j\le r$, c’est-à-dire si $\mathbf{x}$ n’a de coordonnées que le long de $\mathbf{v}_{r+1},\dots,\mathbf{v}_n$. Enfin, $\mathbf{A}^{\top}=\mathbf{V}\mathbf{D}^{\top}\mathbf{U}^{\top}$ est une décomposition en valeurs singulières de $\mathbf{A}^{\top}$, dans laquelle $\mathbf{U}$ et $\mathbf{V}$ échangent leurs rôles ; (i) appliqué à $\mathbf{A}^{\top}$ donne le reste.
:::

Les nombres concordent avec le théorème du rang de Fondements 1, section 13.5 : le noyau est de dimension $n-r$.

⁠**Exemple de calcul :** La matrice $\mathbf{H}$ de colonnes $(1,\,0,\,1)^{\top}$ et $(0,\,1,\,1)^{\top}$ de la section [3.2](die-beste-naherungslosung.html#stufe-3-2) a $\mathbf{H}^{\top}\mathbf{H}=\bigl(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr)$, de valeurs propres $3$ et $1$, donc les valeurs singulières $d_1=\sqrt3$ et $d_2=1$, et les vecteurs singuliers à droite $\mathbf{v}_1=(1,\,1)^{\top}/\sqrt2$, $\mathbf{v}_2=(1,\,-1)^{\top}/\sqrt2$. Ceux à gauche sont

$$\mathbf{u}_1=\frac{\mathbf{H}\mathbf{v}_1}{\sqrt3}=\frac1{\sqrt6}\begin{pmatrix}1\\1\\2\end{pmatrix},\qquad \mathbf{u}_2=\frac{\mathbf{H}\mathbf{v}_2}{1}=\frac1{\sqrt2}\begin{pmatrix}1\\-1\\0\end{pmatrix}.$$

Ils forment une base orthonormée du plan $x_3=x_1+x_2$, différente de celle de la section [4.3](projektion-auf-einen-unterraum.html#stufe-4-3). Elle est complétée par $\mathbf{u}_3=(1,\,1,\,-1)^{\top}/\sqrt3$, le vecteur normal normé de la section [4.4](projektion-auf-einen-unterraum.html#stufe-4-4). Dans la décomposition complète, $\mathbf{D}=\Bigl(\begin{smallmatrix}\sqrt3&0\\0&1\\0&0\end{smallmatrix}\Bigr)$. Le noyau ne contient que le vecteur nul, car $r=n=2$.

⁠**En bref :** Une matrice est la somme de $r$ briques $d_j\mathbf{u}_j\mathbf{v}_j^{\top}$ de rang $1$ ; les $\mathbf{u}_j$ avec $d_j>0$ engendrent l’espace des colonnes, les $\mathbf{v}_j$ avec $d_j=0$ le noyau.

### Matrices symétriques

<span class="anker" id="stufe-9-7"></span>

Pour une matrice symétrique, il existe déjà une décomposition avec une base orthonormée, $\mathbf{A}=\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top}$. Quel est son lien avec la décomposition en valeurs singulières ?

:::satz Théorème 9.6 (Valeurs singulières des matrices symétriques)
<span class="anker" id="satz-9-6"></span>

Les valeurs singulières d’une matrice symétrique sont les valeurs absolues $|\lambda_i|$ de ses valeurs propres. Si $\mathbf{q}_i$ est un vecteur propre normé associé à $\lambda_i\ne0$, alors $\mathbf{v}=\mathbf{q}_i$ est un vecteur singulier à droite et $\mathbf{u}=\operatorname{sign}(\lambda_i)\,\mathbf{q}_i$ le vecteur singulier à gauche associé.
:::

:::beweis Matrices symétriques
On a $\mathbf{A}^{\top}\mathbf{A}=\mathbf{A}^2=\mathbf{Q}\boldsymbol{\Lambda}^2\mathbf{Q}^{\top}$ ; $\mathbf{A}^{\top}\mathbf{A}$ a donc les vecteurs propres $\mathbf{q}_i$, de valeurs propres $\lambda_i^2$, et les valeurs singulières valent $\sqrt{\lambda_i^2}=|\lambda_i|$. D’après [(9.2)](#gl-9-2), $\mathbf{u}=\mathbf{A}\mathbf{q}_i/|\lambda_i|=(\lambda_i/|\lambda_i|)\,\mathbf{q}_i$.
:::

Si $\mathbf{A}$ est semi-définie positive, la décomposition spectrale et la décomposition en valeurs singulières sont une seule et même décomposition, avec $\mathbf{U}=\mathbf{V}=\mathbf{Q}$. En cas de valeurs propres négatives, le signe passe dans $\mathbf{U}$. Pour les matrices non symétriques, valeurs propres et valeurs singulières n’ont en général rien à voir entre elles, comme le montre $\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$, de valeurs propres $2,2$ et de valeurs singulières $4,1$. Il existe cependant toujours un lien : toute valeur propre est, en module, au plus égale à $d_1$ ; cela découle de la sous-section suivante.

⁠**Exemple de calcul :** $\mathbf{A}=\bigl(\begin{smallmatrix}1&3\\3&1\end{smallmatrix}\bigr)$ a la valeur propre $4$, avec $\mathbf{q}_1=(1,\,1)^{\top}/\sqrt2$, et la valeur propre $-2$, avec $\mathbf{q}_2=(1,\,-1)^{\top}/\sqrt2$. Les valeurs singulières sont $4$ et $2$. Avec $\mathbf{v}_2=\mathbf{q}_2$, on a $\mathbf{A}\mathbf{v}_2=(-2,\,2)^{\top}/\sqrt2=2\cdot(-1,\,1)^{\top}/\sqrt2$, donc $\mathbf{u}_2=-\mathbf{q}_2$.

⁠**En bref :** Pour les matrices symétriques, les valeurs singulières sont les valeurs absolues des valeurs propres, et pour les matrices semi-définies positives, la décomposition en valeurs singulières est la décomposition spectrale.

### La norme spectrale

<span class="anker" id="stufe-9-8"></span>

De combien une matrice peut-elle au plus allonger un vecteur ? Pour les vecteurs, la norme mesure la taille. Pour une matrice, une mesure naturelle de la taille est son plus fort facteur d’allongement.

:::definition Définition 9.7 (Norme spectrale)
<span class="anker" id="satz-9-7"></span>

La __norme spectrale__ d’une matrice $\mathbf{A}$ est

$$\lVert\mathbf{A}\rVert_2=\max_{\mathbf{x}\ne\mathbf{0}}\frac{\lVert\mathbf{A}\mathbf{x}\rVert}{\lVert\mathbf{x}\rVert} .$$
:::

:::satz Théorème 9.8 (Étirement maximal et minimal)
<span class="anker" id="satz-9-8"></span>

Pour tout $\mathbf{A}\in\mathbb{R}^{m\times n}$ de valeurs singulières $d_1\ge\dots\ge d_n$ et tout $\mathbf{x}\in\mathbb{R}^n$,

<span class="anker" id="gl-9-5"></span>
$$d_n\,\lVert\mathbf{x}\rVert\le\lVert\mathbf{A}\mathbf{x}\rVert\le d_1\,\lVert\mathbf{x}\rVert . \tag{9.5}$$

Les bornes sont atteintes pour $\mathbf{x}=\mathbf{v}_1$ et $\mathbf{x}=\mathbf{v}_n$. En particulier, $\lVert\mathbf{A}\rVert_2=d_1$.
:::

:::beweis Étirement maximal et minimal
Avec $\mathbf{c}=\mathbf{V}^{\top}\mathbf{x}$, on a $\lVert\mathbf{c}\rVert=\lVert\mathbf{x}\rVert$ et $\lVert\mathbf{A}\mathbf{x}\rVert^2=\mathbf{x}^{\top}\mathbf{A}^{\top}\mathbf{A}\mathbf{x}=\sum_jd_j^2c_j^2$. Cette quantité est comprise entre $d_n^2\sum_jc_j^2$ et $d_1^2\sum_jc_j^2$. C’est le quotient de Rayleigh [(8.2)](positiv-definite-matrizen.html#gl-8-2) de $\mathbf{A}^{\top}\mathbf{A}$, multiplié par $\lVert\mathbf{x}\rVert^2$.
:::

Deux conséquences. Premièrement, $\lVert\mathbf{A}\mathbf{x}\rVert\le\lVert\mathbf{A}\rVert_2\lVert\mathbf{x}\rVert$, et donc $\lVert\mathbf{A}\mathbf{B}\mathbf{x}\rVert\le\lVert\mathbf{A}\rVert_2\lVert\mathbf{B}\rVert_2\lVert\mathbf{x}\rVert$, d’où $\lVert\mathbf{A}\mathbf{B}\rVert_2\le\lVert\mathbf{A}\rVert_2\lVert\mathbf{B}\rVert_2$ : appliqués l’un après l’autre, les plus grands facteurs d’étirement se multiplient au plus. Deuxièmement, pour un vecteur propre, $\lVert\mathbf{A}\mathbf{v}\rVert=|\lambda|\,\lVert\mathbf{v}\rVert$, donc $|\lambda|\le d_1$ pour toute valeur propre d’une matrice carrée. Pour un vecteur propre complexe $\mathbf{v}=\mathbf{a}+\mathrm j\mathbf{b}$, avec $\mathbf{a},\mathbf{b}$ réels, il en va de même si l’on pose $\lVert\mathbf{v}\rVert^2=(\mathbf{v}^*)^{\top}\mathbf{v}=\lVert\mathbf{a}\rVert^2+\lVert\mathbf{b}\rVert^2$, car $\lVert\mathbf{A}\mathbf{v}\rVert^2=\lVert\mathbf{A}\mathbf{a}\rVert^2+\lVert\mathbf{A}\mathbf{b}\rVert^2$ est compris, d’après [(9.5)](#gl-9-5), entre $d_n^2\lVert\mathbf{v}\rVert^2$ et $d_1^2\lVert\mathbf{v}\rVert^2$ ; pour $\mathbf{A}$ carrée, on a donc aussi $|\lambda|\ge d_n$.

⁠**Exemple de calcul :** Pour $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$, on a $\lVert\mathbf{A}\rVert_2=4$. Les vecteurs unitaires de la base sont moins étirés : $\lVert\mathbf{A}\mathbf{e}_1\rVert=\lVert(2,\,0)^{\top}\rVert=2$ et $\lVert\mathbf{A}\mathbf{e}_2\rVert=\lVert(3,\,2)^{\top}\rVert=\sqrt{13}\approx3{,}61$. On n’atteint le facteur $4$ qu’en $\mathbf{v}_1=(1,\,2)^{\top}/\sqrt5$, et le plus petit facteur, $1$, en $\mathbf{v}_2$. La valeur propre $2$ est comprise entre $1$ et $4$.

⁠**En bref :** La norme spectrale $\lVert\mathbf{A}\rVert_2=d_1$ est le plus grand facteur dont $\mathbf{A}$ allonge un vecteur ; le plus petit est $d_n$.

:::hintergrund Plusieurs antennes : des canaux parallèles grâce à la décomposition en valeurs singulières
Un système radio comportant plusieurs antennes d’émission et de réception est appelé système MIMO. Chaque antenne de réception reçoit un mélange de tous les signaux émis. Dans un modèle simple, le vecteur reçu est $\mathbf{y}=\mathbf{K}\mathbf{x}+\boldsymbol\nu$ : $\mathbf{x}$ contient les signaux émis par les antennes, la matrice de canal $\mathbf{K}$ décrit avec quelle intensité chaque antenne d’émission parvient à chaque antenne de réception, et $\boldsymbol\nu$ est le bruit.

Si l’émetteur et le récepteur connaissent la décomposition $\mathbf{K}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$, l’émetteur envoie $\mathbf{x}=\mathbf{V}\tilde{\mathbf{x}}$, et le récepteur calcule $\tilde{\mathbf{y}}=\mathbf{U}^{\top}\mathbf{y}$. Alors

$$\tilde{\mathbf{y}}=\mathbf{U}^{\top}\mathbf{U}\mathbf{D}\mathbf{V}^{\top}\mathbf{V}\tilde{\mathbf{x}}+\mathbf{U}^{\top}\boldsymbol\nu=\mathbf{D}\tilde{\mathbf{x}}+\tilde{\boldsymbol\nu} .$$

Le canal mélangé est devenu $r$ canaux séparés : $\tilde y_j=d_j\tilde x_j+\tilde\nu_j$. Chacun transmet son propre flux de données, avec le gain $d_j$. Le bruit n’est que tourné, sa longueur reste la même, car $\mathbf{U}^{\top}$ est orthogonale. Le nombre de canaux parallèles utilisables est le rang de la matrice de canal, et la qualité de chaque canal est donnée par sa valeur singulière. C’est le schéma rotation, étirement, rotation mis en pratique : l’émetteur fait tourner au préalable, le canal étire, le récepteur fait tourner en sens inverse.
:::

:::aufgabe Exercice 27 ★★ Une décomposition à la main
<span class="anker" id="aufg-27"></span>

Soit $\mathbf{A}=\bigl(\begin{smallmatrix}3&0\\4&5\end{smallmatrix}\bigr)$.

<ol class="al">

<li>

Calculez $\mathbf{A}^{\top}\mathbf{A}$, ses valeurs propres et les valeurs singulières de $\mathbf{A}$.

</li>

<li>

Déterminez $\mathbf{v}_1,\mathbf{v}_2$ et, à partir de là, $\mathbf{u}_1,\mathbf{u}_2$ à l’aide de [(9.2)](#gl-9-2). Vérifiez $\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$.

</li>

<li>

Comparez les valeurs singulières avec les valeurs propres de $\mathbf{A}$. Qu’est-ce qui coïncide, qu’est-ce qui ne coïncide pas ?

</li>

</ol>

:::loesung
(a) $\mathbf{A}^{\top}\mathbf{A}=\bigl(\begin{smallmatrix}9+16&20\\20&25\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}25&20\\20&25\end{smallmatrix}\bigr)$, de trace $50$ et de déterminant $625-400=225$, donc $\lambda^2-50\lambda+225=(\lambda-45)(\lambda-5)$. Les valeurs singulières sont $d_1=\sqrt{45}=3\sqrt5\approx6{,}708$ et $d_2=\sqrt5\approx2{,}236$.

(b) Vecteurs propres de $\mathbf{A}^{\top}\mathbf{A}$ : $\mathbf{v}_1=(1,\,1)^{\top}/\sqrt2$, associé à $45$, et $\mathbf{v}_2=(-1,\,1)^{\top}/\sqrt2$, associé à $5$. On en déduit

$$\mathbf{u}_1=\frac{\mathbf{A}\mathbf{v}_1}{d_1}=\frac{(3,\,9)^{\top}}{\sqrt2\cdot3\sqrt5}=\frac{(1,\,3)^{\top}}{\sqrt{10}},\qquad \mathbf{u}_2=\frac{\mathbf{A}\mathbf{v}_2}{d_2}=\frac{(-3,\,1)^{\top}}{\sqrt2\cdot\sqrt5}=\frac{(-3,\,1)^{\top}}{\sqrt{10}} .$$

Vérification : $\mathbf{U}\mathbf{D}=\tfrac1{\sqrt{10}}\bigl(\begin{smallmatrix}3\sqrt5&-3\sqrt5\\9\sqrt5&\sqrt5\end{smallmatrix}\bigr)=\tfrac1{\sqrt2}\bigl(\begin{smallmatrix}3&-3\\9&1\end{smallmatrix}\bigr)$ et

$$\mathbf{U}\mathbf{D}\mathbf{V}^{\top}=\frac1{\sqrt2}\begin{pmatrix}3&-3\\9&1\end{pmatrix}\frac1{\sqrt2}\begin{pmatrix}1&1\\-1&1\end{pmatrix}=\frac12\begin{pmatrix}6&0\\8&10\end{pmatrix}=\begin{pmatrix}3&0\\4&5\end{pmatrix}.$$

(c) Les valeurs propres de la matrice triangulaire sont $3$ et $5$. Les produits coïncident : $3\cdot5=15=3\sqrt5\cdot\sqrt5=|\det\mathbf{A}|$. Les sommes, non : $8$ contre $4\sqrt5\approx8{,}94$. Les valeurs propres sont, en valeur absolue, comprises entre $d_2$ et $d_1$ : $2{,}236\le3$ et $5\le6{,}708$.
:::
:::

:::aufgabe Exercice 28 ★★ Une matrice rectangulaire
<span class="anker" id="aufg-28"></span>

Soit $\mathbf{A}=\Bigl(\begin{smallmatrix}1&1\\1&1\\1&-1\end{smallmatrix}\Bigr)$.

<ol class="al">

<li>

Déterminez les valeurs singulières et les vecteurs singuliers $\mathbf{v}_1,\mathbf{v}_2,\mathbf{u}_1,\mathbf{u}_2$.

</li>

<li>

Complétez avec $\mathbf{u}_3$ et écrivez la décomposition complète $\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$.

</li>

<li>

Donnez des bases orthonormées de l’espace des colonnes et de son supplémentaire orthogonal.

</li>

</ol>

:::loesung
(a) $\mathbf{A}^{\top}\mathbf{A}=\bigl(\begin{smallmatrix}3&1\\1&3\end{smallmatrix}\bigr)$ a les valeurs propres $4$, avec $\mathbf{v}_1=(1,\,1)^{\top}/\sqrt2$, et $2$, avec $\mathbf{v}_2=(1,\,-1)^{\top}/\sqrt2$. Donc $d_1=2$, $d_2=\sqrt2$, et

$$\mathbf{u}_1=\frac{\mathbf{A}\mathbf{v}_1}2=\frac{(2,\,2,\,0)^{\top}}{2\sqrt2}=\frac{(1,\,1,\,0)^{\top}}{\sqrt2},\qquad \mathbf{u}_2=\frac{\mathbf{A}\mathbf{v}_2}{\sqrt2}=\frac{(0,\,0,\,2)^{\top}}{\sqrt2\cdot\sqrt2}=(0,\,0,\,1)^{\top} .$$

(b) $\mathbf{u}_3$ est perpendiculaire aux deux : $\mathbf{u}_3=(1,\,-1,\,0)^{\top}/\sqrt2$. La décomposition complète est

$$\mathbf{A}=\begin{pmatrix}1/\sqrt2&0&1/\sqrt2\\1/\sqrt2&0&-1/\sqrt2\\0&1&0\end{pmatrix}\begin{pmatrix}2&0\\0&\sqrt2\\0&0\end{pmatrix}\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}.$$

(c) D’après le théorème de la section [9.6](#stufe-9-6), $\mathbf{u}_1,\mathbf{u}_2$ est une base orthonormée de l’espace des colonnes, et $\mathbf{u}_3$ une base orthonormée de son supplémentaire orthogonal. Pour contrôle : les colonnes $(1,\,1,\,1)^{\top}=\sqrt2\,\mathbf{u}_1+\mathbf{u}_2$ et $(1,\,1,\,-1)^{\top}=\sqrt2\,\mathbf{u}_1-\mathbf{u}_2$ appartiennent au sous-espace engendré par $\mathbf{u}_1,\mathbf{u}_2$, et toutes deux sont perpendiculaires à $\mathbf{u}_3$.
:::
:::

:::aufgabe Exercice 29 ★★★ Propriétés des valeurs singulières
<span class="anker" id="aufg-29"></span>

<ol class="al">

<li>

Montrez que, pour une matrice carrée, $|\det\mathbf{A}|=d_1d_2\cdots d_n$.

</li>

<li>

Montrez que $\mathbf{A}$ et $\mathbf{A}^{\top}$ ont les mêmes valeurs singulières positives.

</li>

<li>

Montrez que, pour $\mathbf{u}\ne\mathbf{0}$ et $\mathbf{v}\ne\mathbf{0}$, le produit extérieur $\mathbf{u}\mathbf{v}^{\top}$ a exactement une valeur singulière positive, à savoir $\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert$.

</li>

<li>

Montrez que, si $\mathbf{Q}$ est orthogonale, $\mathbf{Q}\mathbf{A}$ et $\mathbf{A}$ ont les mêmes valeurs singulières.

</li>

</ol>

:::loesung
(a) D’après Fondements 1, section 14.5, $\det\mathbf{A}=\det\mathbf{U}\cdot\det\mathbf{D}\cdot\det\mathbf{V}^{\top}$. Les deux matrices orthogonales ont pour déterminant $\pm1$, et $\mathbf{D}$ est une matrice diagonale de déterminant $d_1\cdots d_n$. Donc $|\det\mathbf{A}|=d_1\cdots d_n$.

(b) De $\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$, on déduit $\mathbf{A}^{\top}\mathbf{A}=\mathbf{V}\mathbf{D}^{\top}\mathbf{D}\mathbf{V}^{\top}$ et $\mathbf{A}\mathbf{A}^{\top}=\mathbf{U}\mathbf{D}\mathbf{D}^{\top}\mathbf{U}^{\top}$. Les matrices diagonales $\mathbf{D}^{\top}\mathbf{D}$ et $\mathbf{D}\mathbf{D}^{\top}$ portent sur leur diagonale les mêmes coefficients $d_j^2>0$ ; seul le nombre de zéros diffère. Les valeurs singulières de $\mathbf{A}^{\top}$ sont les racines carrées des valeurs propres de $(\mathbf{A}^{\top})^{\top}\mathbf{A}^{\top}=\mathbf{A}\mathbf{A}^{\top}$, c’est-à-dire de nouveau les $d_j$, complétés par des zéros.

(c) $(\mathbf{u}\mathbf{v}^{\top})^{\top}(\mathbf{u}\mathbf{v}^{\top})=\mathbf{v}\,\mathbf{u}^{\top}\mathbf{u}\,\mathbf{v}^{\top}=\lVert\mathbf{u}\rVert^2\,\mathbf{v}\mathbf{v}^{\top}$. Cette matrice envoie $\mathbf{v}$ sur $\lVert\mathbf{u}\rVert^2\lVert\mathbf{v}\rVert^2\,\mathbf{v}$ et tout vecteur perpendiculaire à $\mathbf{v}$ sur zéro. Ses valeurs propres sont donc $\lVert\mathbf{u}\rVert^2\lVert\mathbf{v}\rVert^2$ et, pour le reste, $0$, et l’unique valeur singulière positive est $\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert$.

(d) $(\mathbf{Q}\mathbf{A})^{\top}(\mathbf{Q}\mathbf{A})=\mathbf{A}^{\top}\mathbf{Q}^{\top}\mathbf{Q}\mathbf{A}=\mathbf{A}^{\top}\mathbf{A}$. Les deux matrices ont la même matrice de Gram, et donc les mêmes valeurs singulières. Intuitivement : une rotation ou une réflexion appliquée après $\mathbf{A}$ ne change pas la forme de l’ellipse, seulement sa position.
:::
:::

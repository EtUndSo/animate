---
title: Bases orthonormées et matrices orthogonales
pfad: Informatique / Apprentissage automatique / Fondements mathématiques / Projection, valeurs propres et décompositions
adresse: informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen
knoten: Chapitre 2 : Projection, valeurs propres et décompositions
nachschlagen: ja
order: 15220200
summary: Certains repères sont particulièrement commodes : leurs axes sont perpendiculaires entre eux, et l’unité a la même longueur sur chaque axe.
tags: orthonormés, base orthonormée, matrice orthogonale
lang: fr
---

<span class="anker" id="stufe-1"></span>

:::zweck
Certains repères sont particulièrement commodes : leurs axes sont perpendiculaires entre eux, et l’unité a la même longueur sur chaque axe. Dans un tel repère, il n’est pas nécessaire de résoudre un système d’équations pour trouver les coordonnées d’un point, et l’on calcule les longueurs avec le théorème de Pythagore. Cette section introduit ces repères et les matrices qui leur correspondent.
:::

### Vecteurs orthonormés

<span class="anker" id="stufe-1-1"></span>

Dans le [chapitre 1, section 5.3](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/winkel-und-ahnlichkeit.html#stufe-5-3), deux vecteurs étaient dits orthogonaux lorsque leur produit scalaire est nul. Le motif constant $(1,1,1,1)^{\top}$ et le motif alterné $(1,-1,1,-1)^{\top}$ en étaient un exemple : la comparaison d’une série temporelle avec l’un des motifs n’était pas perturbée par l’autre. Elle donnait toutefois la part multipliée par $4$, parce que les deux motifs ont la longueur $2$. Si des vecteurs orthogonaux ont en plus la longueur $1$, ce facteur disparaît lui aussi.

Imaginez les deux axes $\mathbf{e}_1$ et $\mathbf{e}_2$ du plan, tournés d’un bloc d’un certain angle. Les deux flèches ont toujours la longueur $1$ et restent perpendiculaires l’une à l’autre ; elles pointent simplement dans d’autres directions.

:::definition Définition 1.1 (Orthonormés)
<span class="anker" id="satz-1-1"></span>

Des vecteurs $\mathbf{q}_1,\dots,\mathbf{q}_k\in\mathbb{R}^n$ sont dits __orthonormés__ si chacun d’eux a la longueur $1$ et s’ils sont orthogonaux deux à deux :

<span class="anker" id="gl-1-1"></span>
$$\mathbf{q}_i^{\top}\mathbf{q}_l=\begin{cases}1, & i=l,\\ 0, & i\ne l.\end{cases} \tag{1.1}$$
:::

Le mot réunit « orthogonal » et « normé ». Les vecteurs unitaires $\mathbf{e}_1,\dots,\mathbf{e}_n$ en sont l’exemple le plus simple.

:::satz Théorème 1.2 (Des vecteurs orthonormés sont linéairement indépendants)
<span class="anker" id="satz-1-2"></span>

Si $\mathbf{q}_1,\dots,\mathbf{q}_k$ sont orthonormés, ils sont linéairement indépendants.
:::

:::beweis Indépendance linéaire
Supposons $c_1\mathbf{q}_1+\dots+c_k\mathbf{q}_k=\mathbf{0}$. On forme le produit scalaire des deux membres avec $\mathbf{q}_l$. D’après [(1.1)](#gl-1-1), il ne reste à gauche que le terme $c_l\,\mathbf{q}_l^{\top}\mathbf{q}_l=c_l$, et à droite on a $\mathbf{q}_l^{\top}\mathbf{0}=0$. Donc $c_l=0$, et ce pour tout $l$. D’après la définition du [chapitre 1, section 13.2](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/unabhangigkeit-basis-und-rang.html#stufe-13-2), les vecteurs sont donc linéairement indépendants.
:::

::::beispiel [Exemple de calcul]
Pour $\mathbf{q}_1=(0{,}6;\ 0{,}8)^{\top}$ et $\mathbf{q}_2=(-0{,}8;\ 0{,}6)^{\top}$, on a

$$\mathbf{q}_1^{\top}\mathbf{q}_1=0{,}36+0{,}64=1,\qquad \mathbf{q}_2^{\top}\mathbf{q}_2=0{,}64+0{,}36=1,\qquad \mathbf{q}_1^{\top}\mathbf{q}_2=-0{,}48+0{,}48=0 .$$

Les deux vecteurs sont orthonormés ; la Fig. [1](#abb-1) montre le dernier produit scalaire pas à pas. Le motif constant et le motif alterné deviennent orthonormés si on les divise par leur longueur $2$ : $\tfrac12(1,1,1,1)^{\top}$ et $\tfrac12(1,-1,1,-1)^{\top}$.

:::abbildung ml/k2rorth 1
Le produit scalaire $\mathbf{q}_1^{\top}\mathbf{q}_2$ pas à pas, avec $0{,}6=\tfrac35$ et $0{,}8=\tfrac45$ : produit composante par composante, puis la somme.
:::
::::

⁠**En bref :** Des vecteurs orthonormés ont la longueur $1$ et sont perpendiculaires deux à deux ; ils sont toujours linéairement indépendants.

### Bases orthonormées

<span class="anker" id="stufe-1-2"></span>

D’après le [chapitre 1, section 13.3](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/unabhangigkeit-basis-und-rang.html#stufe-13-3), une base est un système de coordonnées : tout vecteur y a exactement une représentation. Les plus commodes sont les bases dont les vecteurs sont orthonormés. Elles sont comme le repère habituel, simplement tourné.

:::definition Définition 1.3 (Base orthonormée)
<span class="anker" id="satz-1-3"></span>

Une base formée de vecteurs orthonormés est appelée __base orthonormée__.
:::

Pour l’espace $\mathbb{R}^n$ tout entier, il suffit de trouver $n$ vecteurs orthonormés. D’après le théorème de la sous-section précédente, ils sont linéairement indépendants. Si on les écrit en colonnes dans une matrice $n\times n$, celle-ci est de rang $n$, et son espace des colonnes est, d’après le [chapitre 1, section 13.5](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/unabhangigkeit-basis-und-rang.html#stufe-13-5), l’espace $\mathbb{R}^n$ tout entier. Les $n$ vecteurs engendrent donc $\mathbb{R}^n$ et forment une base. De même, on peut chercher une base orthonormée d’un sous-espace engendré, par exemple d’un plan de $\mathbb{R}^3$ : des vecteurs orthonormés qui engendrent exactement ce sous-espace.

::::beispiel [Exemple de calcul]
Les vecteurs $\mathbf{q}_1=(0{,}6;\ 0{,}8)^{\top}$ et $\mathbf{q}_2=(-0{,}8;\ 0{,}6)^{\top}$ sont deux vecteurs orthonormés de $\mathbb{R}^2$, donc une base orthonormée de $\mathbb{R}^2$. Les vecteurs unitaires $\mathbf{e}_1,\mathbf{e}_2,\mathbf{e}_3$ forment la base orthonormée de $\mathbb{R}^3$ que l’on appelle base canonique. Le plan $\operatorname{span}\{\mathbf{e}_1,\mathbf{e}_2\}$ de $\mathbb{R}^3$ a pour base orthonormée $\mathbf{e}_1,\mathbf{e}_2$.
::::

⁠**En bref :** Une base orthonormée est un repère tourné : $n$ vecteurs orthonormés de $\mathbb{R}^n$ forment toujours une base.

### Coordonnées dans une base orthonormée

<span class="anker" id="stufe-1-3"></span>

Dans une base quelconque, il faut résoudre un système d’équations pour trouver les coordonnées d’un vecteur. Dans le [chapitre 1, section 13.3](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/unabhangigkeit-basis-und-rang.html#stufe-13-3), le vecteur $(3,\,2)^{\top}$ avait, dans la base $(1,\,0)^{\top}$, $(1,\,1)^{\top}$, les coordonnées $1$ et $2$. Les produits scalaires $(1,0)(3,2)^{\top}=3$ et $(1,1)(3,2)^{\top}=5$ sont tout autre chose. Dans une base orthonormée, en revanche, les coordonnées sont exactement les produits scalaires.

L’image de la longueur de l’ombre, vue dans le [chapitre 1, section 5.5](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/winkel-und-ahnlichkeit.html#stufe-5-5), en donne la raison. Pour un vecteur normé $\mathbf{q}$, $\mathbf{q}^{\top}\mathbf{x}$ est la longueur de l’ombre de $\mathbf{x}$ sur la droite de direction $\mathbf{q}$. Dans une base orthonormée, chaque coordonnée est l’ombre sur son propre axe (Fig. [2](#abb-2)).

:::abbildung ml/k2onb 2
Coordonnées dans la base orthonormée $\mathbf{q}_1=(0{,}6;\,0{,}8)^{\top}$, $\mathbf{q}_2=(-0{,}8;\,0{,}6)^{\top}$ (en vert). La flèche $\mathbf{x}=(3,1)^{\top}$ projette une ombre sur chacun des deux axes tournés (en gris), la lumière tombant chaque fois perpendiculairement (en tirets). Les longueurs des ombres $\mathbf{q}_1^{\top}\mathbf{x}=2{,}6$ (en bleu) et $\mathbf{q}_2^{\top}\mathbf{x}=-1{,}8$ (en orange) sont les coordonnées : $\mathbf{x}=2{,}6\,\mathbf{q}_1-1{,}8\,\mathbf{q}_2$.
:::

:::satz Théorème 1.4 (Coordonnées dans une base orthonormée)
<span class="anker" id="satz-1-4"></span>

Si $\mathbf{q}_1,\dots,\mathbf{q}_n$ est une base orthonormée de $\mathbb{R}^n$, alors pour tout vecteur $\mathbf{x}\in\mathbb{R}^n$

<span class="anker" id="gl-1-2"></span>
$$\mathbf{x}=\sum_{i=1}^n(\mathbf{q}_i^{\top}\mathbf{x})\,\mathbf{q}_i\qquad\text{et}\qquad \lVert\mathbf{x}\rVert^2=\sum_{i=1}^n(\mathbf{q}_i^{\top}\mathbf{x})^2 . \tag{1.2}$$
:::

:::beweis Coordonnées dans une base orthonormée
Comme les vecteurs forment une base, il existe des nombres $c_1,\dots,c_n$ tels que $\mathbf{x}=\sum_ic_i\mathbf{q}_i$. Le produit scalaire avec $\mathbf{q}_l$ donne, d’après [(1.1)](#gl-1-1),

$$\mathbf{q}_l^{\top}\mathbf{x}=\sum_{i=1}^nc_i\,\mathbf{q}_l^{\top}\mathbf{q}_i=c_l ,$$

car seul le terme d’indice $i=l$ n’est pas nul. Pour la longueur, on développe :

$$\lVert\mathbf{x}\rVert^2=\mathbf{x}^{\top}\mathbf{x}=\sum_{i=1}^n\sum_{l=1}^nc_i\,c_l\,\mathbf{q}_i^{\top}\mathbf{q}_l=\sum_{i=1}^nc_i^2 ,$$

là encore parce que seuls les termes avec $i=l$ subsistent.
:::

La seconde formule est le théorème de Pythagore dans $\mathbb{R}^n$ : la longueur d’une flèche se calcule de la même façon à partir de ses coordonnées dans n’importe quel repère orthogonal, pourvu que l’unité ait la longueur $1$ sur tous les axes.

::::beispiel [Exemple de calcul]
Pour $\mathbf{x}=(3,\,1)^{\top}$ et la base de la sous-section précédente, on a

$$c_1=\mathbf{q}_1^{\top}\mathbf{x}=1{,}8+0{,}8=2{,}6,\qquad c_2=\mathbf{q}_2^{\top}\mathbf{x}=-2{,}4+0{,}6=-1{,}8 .$$

Vérification : $2{,}6\,(0{,}6;\ 0{,}8)^{\top}-1{,}8\,(-0{,}8;\ 0{,}6)^{\top}=(1{,}56+1{,}44;\ 2{,}08-1{,}08)^{\top}=(3,\,1)^{\top}$. Et $c_1^2+c_2^2=6{,}76+3{,}24=10=\lVert\mathbf{x}\rVert^2$. La Fig. [3](#abb-3) montre les trois sommes avec des fractions.

:::abbildung ml/k2rkoord 3
Les coordonnées $c_1=\tfrac{13}5=2{,}6$ et $c_2=-\tfrac95=-1{,}8$ de $\mathbf{x}$ comme produits scalaires, et la somme de leurs carrés, le carré de la longueur de $\mathbf{x}$.
:::
::::

⁠**En bref :** Dans une base orthonormée, chaque coordonnée est un produit scalaire, $c_i=\mathbf{q}_i^{\top}\mathbf{x}$, et la somme des carrés des coordonnées est le carré de la longueur.

:::hintergrund Les oscillations comme base orthonormée, et le théorème de Parseval
Les quatre vecteurs

$$\begin{gathered} \mathbf{q}_1=\tfrac12(1,\,1,\,1,\,1)^{\top},\qquad \mathbf{q}_2=\tfrac1{\sqrt2}(1,\,0,\,-1,\,0)^{\top},\\ \mathbf{q}_3=\tfrac1{\sqrt2}(0,\,1,\,0,\,-1)^{\top},\qquad \mathbf{q}_4=\tfrac12(1,\,-1,\,1,\,-1)^{\top} \end{gathered}$$

sont les valeurs d’une constante, d’une oscillation en cosinus et d’une oscillation en sinus de période égale à quatre pas, et d’une oscillation qui change de signe à chaque pas, chaque vecteur étant normé. On vérifie facilement qu’ils sont orthonormés. Ils forment donc une base orthonormée de $\mathbb{R}^4$. Toute série temporelle de quatre valeurs, par exemple la température à quatre moments de la journée, est une somme de ces quatre oscillations, et les parts sont, d’après [(1.2)](#gl-1-2), de simples produits scalaires. Pour la série temporelle $\mathbf{x}=(4,\,2,\,0,\,2)^{\top}$, on a $\mathbf{q}_1^{\top}\mathbf{x}=4$, $\mathbf{q}_2^{\top}\mathbf{x}=4/\sqrt2=2\sqrt2$, $\mathbf{q}_3^{\top}\mathbf{x}=0$ et $\mathbf{q}_4^{\top}\mathbf{x}=0$ : la série temporelle ne se compose que d’une constante et d’un cosinus.

La seconde formule de [(1.2)](#gl-1-2) dit que la somme des carrés $\lVert\mathbf{x}\rVert^2=24$ de la série temporelle est égale à la somme des carrés des parts, $16+8+0+0=24$. En mathématiques, cet énoncé s’appelle le théorème de Parseval. La transformée de Fourier discrète est la même décomposition avec des oscillations complexes ; c’est avec elle, par exemple, qu’un logiciel de musique décompose un son en ses notes. Sa matrice pour $N$ valeurs conserve les longueurs si et seulement si on la normalise par $1/\sqrt N$ ; sans ce facteur, le théorème de Parseval comporte en plus le facteur $N$.
:::

### Matrices orthogonales

<span class="anker" id="stufe-1-4"></span>

Si l’on écrit les vecteurs d’une base orthonormée en colonnes dans une matrice $\mathbf{Q}=\begin{pmatrix}\mathbf{q}_1&\cdots&\mathbf{q}_n\end{pmatrix}$, les deux formules [(1.2)](#gl-1-2) s’écrivent comme des produits matriciels. D’après la vue par lignes du [chapitre 1, section 7.2](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrix-vektor-produkt.html#stufe-7-2), toutes les coordonnées à la fois forment le vecteur $\mathbf{c}=\mathbf{Q}^{\top}\mathbf{x}$, car les lignes de $\mathbf{Q}^{\top}$ sont les vecteurs $\mathbf{q}_i^{\top}$. Inversement, d’après la vue par colonnes, $\mathbf{x}=\sum_ic_i\mathbf{q}_i=\mathbf{Q}\mathbf{c}$. La matrice $\mathbf{Q}^{\top}$ défait donc ce que fait $\mathbf{Q}$.

:::definition Définition 1.5 (Matrice orthogonale)
<span class="anker" id="satz-1-5"></span>

Une matrice carrée $\mathbf{Q}\in\mathbb{R}^{n\times n}$ dont les colonnes sont orthonormées est appelée __matrice orthogonale__. De façon équivalente : $\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}$.
:::

Les deux formulations sont équivalentes, car le coefficient $(i,l)$ de $\mathbf{Q}^{\top}\mathbf{Q}$ est le produit scalaire $\mathbf{q}_i^{\top}\mathbf{q}_l$ des colonnes $i$ et $l$. La condition $\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}$ est donc exactement [(1.1)](#gl-1-1).

:::satz Théorème 1.6 (L’inverse d’une matrice orthogonale)
<span class="anker" id="satz-1-6"></span>

Si $\mathbf{Q}$ est orthogonale, alors $\mathbf{Q}$ est inversible et $\mathbf{Q}^{-1}=\mathbf{Q}^{\top}$. De plus, $\mathbf{Q}\mathbf{Q}^{\top}=\mathbf{I}$ ; les lignes de $\mathbf{Q}$ sont donc elles aussi orthonormées, et $\mathbf{Q}^{\top}$ est également orthogonale.
:::

:::beweis Inverse d’une matrice orthogonale
Les colonnes sont orthonormées, donc linéairement indépendantes d’après la première sous-section. D’après le théorème du [chapitre 1, section 13.5](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/unabhangigkeit-basis-und-rang.html#stufe-13-5), $\mathbf{Q}$ est donc inversible. En multipliant $\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}$ à droite par $\mathbf{Q}^{-1}$, on obtient $\mathbf{Q}^{\top}=\mathbf{Q}^{-1}$, et par conséquent aussi $\mathbf{Q}\mathbf{Q}^{\top}=\mathbf{Q}\mathbf{Q}^{-1}=\mathbf{I}$.
:::

Un mot sur le nom. Une matrice orthogonale a des colonnes orthonormées, et pas seulement orthogonales ; le nom est un héritage de l’histoire. Les matrices dont les colonnes sont seulement orthogonales, mais pas normées, n’ont pas de nom particulier. Pour elles, $\mathbf{Q}^{\top}\mathbf{Q}$ est une matrice diagonale portant sur sa diagonale les carrés des longueurs des colonnes, mais ce n’est pas $\mathbf{I}$.

::::beispiel [Exemple de calcul]
Avec les vecteurs de la première sous-section comme colonnes, on a

$$\mathbf{Q}=\begin{pmatrix}0{,}6&-0{,}8\\0{,}8&0{,}6\end{pmatrix},\qquad \mathbf{Q}^{\top}\mathbf{Q}=\begin{pmatrix}0{,}36+0{,}64&-0{,}48+0{,}48\\-0{,}48+0{,}48&0{,}64+0{,}36\end{pmatrix}=\mathbf{I} .$$

Les coefficients de $\mathbf{Q}^{\top}\mathbf{Q}$ sont les produits scalaires des colonnes de la première sous-section ; la Fig. [1](#abb-1) montre le coefficient hors diagonale. Donc $\mathbf{Q}^{-1}=\mathbf{Q}^{\top}$, sans calcul. Cette matrice est la matrice de rotation du [chapitre 1, section 8.3](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/lineare-abbildungen.html#stufe-8-3), avec $\cos\alpha=0{,}6$ et $\sin\alpha=0{,}8$, donc une rotation d’angle $\alpha\approx53{,}13^\circ$ dans le sens inverse des aiguilles d’une montre. L’inverse $\mathbf{Q}^{\top}$ fait tourner du même angle en sens contraire.
::::

⁠**En bref :** Une matrice orthogonale est une matrice carrée à colonnes orthonormées ; son inverse est simplement sa transposée.

### Les longueurs et les angles sont conservés

<span class="anker" id="stufe-1-5"></span>

Une rotation ne change ni la longueur d’une flèche ni l’angle entre deux flèches. Toutes les matrices orthogonales ont cette propriété, et c’est la raison pour laquelle on aime tant calculer avec elles.

:::satz Théorème 1.7 (Les matrices orthogonales conservent les produits scalaires)
<span class="anker" id="satz-1-7"></span>

Si $\mathbf{Q}$ est orthogonale, alors pour tous $\mathbf{x},\mathbf{y}\in\mathbb{R}^n$

<span class="anker" id="gl-1-3"></span>
$$(\mathbf{Q}\mathbf{x})^{\top}(\mathbf{Q}\mathbf{y})=\mathbf{x}^{\top}\mathbf{y},\qquad \lVert\mathbf{Q}\mathbf{x}\rVert=\lVert\mathbf{x}\rVert , \tag{1.3}$$

et l’angle entre $\mathbf{Q}\mathbf{x}$ et $\mathbf{Q}\mathbf{y}$ est le même que celui entre $\mathbf{x}$ et $\mathbf{y}$. Le déterminant vaut $\det\mathbf{Q}=1$ ou $\det\mathbf{Q}=-1$.
:::

:::beweis Conservation des produits scalaires
D’après la règle $(\mathbf{A}\mathbf{B})^{\top}=\mathbf{B}^{\top}\mathbf{A}^{\top}$ du [chapitre 1, section 10.1](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/transponierte-symmetrie-und-gram-matrix.html#stufe-10-1), on a $(\mathbf{Q}\mathbf{x})^{\top}(\mathbf{Q}\mathbf{y})=\mathbf{x}^{\top}\mathbf{Q}^{\top}\mathbf{Q}\mathbf{y}=\mathbf{x}^{\top}\mathbf{I}\mathbf{y}=\mathbf{x}^{\top}\mathbf{y}$. Avec $\mathbf{y}=\mathbf{x}$, on obtient l’énoncé sur la longueur, et comme l’angle se calcule uniquement à partir de produits scalaires et de longueurs, il reste lui aussi inchangé. Pour le déterminant, on utilise les règles de calcul du [chapitre 1, section 14.5](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/die-determinante.html#stufe-14-5) : $1=\det\mathbf{I}=\det(\mathbf{Q}^{\top}\mathbf{Q})=\det\mathbf{Q}^{\top}\cdot\det\mathbf{Q}=(\det\mathbf{Q})^2$.
:::

Une matrice orthogonale déplace donc l’espace de façon rigide, sans le déformer. Si $\det\mathbf{Q}=1$, c’est une rotation. Si $\det\mathbf{Q}=-1$, elle contient une réflexion, car d’après le [chapitre 1, section 14.2](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/die-determinante.html#stufe-14-2), un déterminant négatif inverse l’orientation.

::::beispiel [Exemple de calcul]
La rotation de la sous-section précédente envoie $\mathbf{x}=(3,\,1)^{\top}$ sur $\mathbf{Q}\mathbf{x}=(1{,}8-0{,}8;\ 2{,}4+0{,}6)^{\top}=(1,\,3)^{\top}$. Les deux vecteurs ont le même carré de longueur, $10$. Le déterminant de la rotation vaut $0{,}36+0{,}64=1$. La matrice $\bigl(\begin{smallmatrix}0{,}6&0{,}8\\0{,}8&-0{,}6\end{smallmatrix}\bigr)$ a elle aussi des colonnes orthonormées, mais son déterminant vaut $-0{,}36-0{,}64=-1$ : c’est la réflexion par rapport à la droite de direction $(2,\,1)^{\top}$, car elle envoie $(2,\,1)^{\top}$ sur lui-même et $(-1,\,2)^{\top}$ sur $(1,\,-2)^{\top}$.
::::

⁠**En bref :** Les matrices orthogonales conservent les produits scalaires, les longueurs et les angles ; ce sont des rotations ou des réflexions, et leur déterminant vaut $\pm1$.

:::hintergrund Pourquoi le calcul numérique apprécie les matrices orthogonales
Un ordinateur calcule avec des nombres arrondis ; chaque résultat intermédiaire porte une petite erreur $\boldsymbol{\delta}$. Si l’on multiplie un tel résultat intermédiaire par une matrice, l’erreur est elle aussi multipliée par cette matrice. Une matrice quelconque peut l’amplifier ; une matrice orthogonale ne le peut pas, car d’après [(1.3)](#gl-1-3), $\lVert\mathbf{Q}\boldsymbol{\delta}\rVert=\lVert\boldsymbol{\delta}\rVert$. Les méthodes de calcul qui ne consistent qu’en multiplications par des matrices orthogonales ne font donc pas croître les erreurs d’arrondi. Pour la même raison, l’inverse ne pose aucun problème : inutile de la calculer, la transposée suffit, et elle est exacte.
:::

### Matrices à colonnes orthonormées

<span class="anker" id="stufe-1-6"></span>

Souvent, on dispose de moins de vecteurs orthonormés que l’espace n’a de dimensions. Un plan de $\mathbb{R}^3$ a une base orthonormée de deux vecteurs. Si on les écrit en colonnes dans une matrice, celle-ci n’est pas carrée : elle a trois lignes et deux colonnes. Une partie des règles de calcul reste valable, une autre non, et la différence est importante.

:::satz Théorème 1.8 (Matrices rectangulaires à colonnes orthonormées)
<span class="anker" id="satz-1-8"></span>

Si $\mathbf{Q}\in\mathbb{R}^{n\times k}$ a des colonnes orthonormées et si $k<n$, alors $\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}_k$ et $\lVert\mathbf{Q}\mathbf{c}\rVert=\lVert\mathbf{c}\rVert$ pour tout $\mathbf{c}\in\mathbb{R}^k$. La matrice $\mathbf{Q}\mathbf{Q}^{\top}\in\mathbb{R}^{n\times n}$, en revanche, n’est pas la matrice identité.
:::

:::beweis Matrices rectangulaires
Les deux premiers énoncés découlent de [(1.1)](#gl-1-1) exactement comme pour les matrices carrées. Pour le troisième : la matrice $\mathbf{Q}^{\top}$ a $k$ lignes et $n$ colonnes. D’après le théorème du rang du [chapitre 1, section 13.5](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/unabhangigkeit-basis-und-rang.html#stufe-13-5), son noyau est de dimension $n-\operatorname{rg}\mathbf{Q}^{\top}\ge n-k\ge1$. Il existe donc un vecteur $\mathbf{z}\ne\mathbf{0}$ tel que $\mathbf{Q}^{\top}\mathbf{z}=\mathbf{0}$, et pour lui $\mathbf{Q}\mathbf{Q}^{\top}\mathbf{z}=\mathbf{0}\ne\mathbf{z}$. Donc $\mathbf{Q}\mathbf{Q}^{\top}\ne\mathbf{I}$.
:::

::::beispiel [Exemple de calcul 1]
La matrice dont l’unique colonne est $\mathbf{q}=(0{,}6;\ 0{,}8)^{\top}$ vérifie $\mathbf{q}^{\top}\mathbf{q}=1$, mais

$$\mathbf{q}\mathbf{q}^{\top}=\begin{pmatrix}0{,}36&0{,}48\\0{,}48&0{,}64\end{pmatrix}\ne\mathbf{I} .$$

Celle-ci envoie $(-0{,}8;\ 0{,}6)^{\top}$ sur $\mathbf{0}$. Elle envoie le vecteur $\mathbf{x}=(3,\,1)^{\top}$ sur $(1{,}08+0{,}48;\ 1{,}44+0{,}64)^{\top}=(1{,}56;\ 2{,}08)^{\top}$. C’est exactement l’extrémité de l’ombre de $\mathbf{x}$ du [chapitre 1, section 5.5](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/winkel-und-ahnlichkeit.html#stufe-5-5), car $\mathbf{q}\mathbf{q}^{\top}\mathbf{x}=\mathbf{q}\,(\mathbf{q}^{\top}\mathbf{x})=2{,}6\,\mathbf{q}$.
::::

::::beispiel [Exemple de calcul 2]
Les colonnes de $\mathbf{Q}=\Bigl(\begin{smallmatrix}1&0\\0&1\\0&0\end{smallmatrix}\Bigr)$ sont $\mathbf{e}_1$ et $\mathbf{e}_2$ dans $\mathbb{R}^3$. On a $\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}_2$, mais $\mathbf{Q}\mathbf{Q}^{\top}=\operatorname{diag}(1;\,1;\,0)$. Cette matrice conserve les deux premières composantes et met la troisième à zéro.
::::

⁠**En bref :** Pour une matrice rectangulaire à colonnes orthonormées, $\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}$, mais $\mathbf{Q}\mathbf{Q}^{\top}\ne\mathbf{I}$ : le produit dans cet ordre jette une partie du vecteur.

:::aufgabe Exercice 1 ★ Orthonormalité et coordonnées
<span class="anker" id="aufg-1"></span>

On donne $\mathbf{q}_1=\tfrac13(1,\,2,\,2)^{\top}$, $\mathbf{q}_2=\tfrac13(2,\,1,\,-2)^{\top}$ et $\mathbf{q}_3=\tfrac13(2,\,-2,\,1)^{\top}$.

<ol class="al">

<li>

Vérifiez que les trois vecteurs sont orthonormés.

</li>

<li>

Calculez les coordonnées de $\mathbf{x}=(3,\,0,\,3)^{\top}$ dans cette base orthonormée et faites la vérification. Vérifiez la formule pour $\lVert\mathbf{x}\rVert^2$.

</li>

</ol>

:::loesung
(a) On forme les six produits scalaires ; le facteur commun $\tfrac13\cdot\tfrac13=\tfrac19$ est placé devant :

$$\mathbf{q}_1^{\top}\mathbf{q}_1=\tfrac19(1+4+4)=1,\quad \mathbf{q}_2^{\top}\mathbf{q}_2=\tfrac19(4+1+4)=1,\quad \mathbf{q}_3^{\top}\mathbf{q}_3=\tfrac19(4+4+1)=1,$$

$$\mathbf{q}_1^{\top}\mathbf{q}_2=\tfrac19(2+2-4)=0,\quad \mathbf{q}_1^{\top}\mathbf{q}_3=\tfrac19(2-4+2)=0,\quad \mathbf{q}_2^{\top}\mathbf{q}_3=\tfrac19(4-2-2)=0 .$$

Les trois vecteurs ont la longueur $1$ et sont deux à deux perpendiculaires : ils sont orthonormés et forment donc, d’après la section [1.2](#stufe-1-2), une base orthonormée de $\mathbb{R}^3$.

(b) D’après [(1.2)](#gl-1-2), les coordonnées sont des produits scalaires, sans système d’équations à résoudre :

$$c_1=\mathbf{q}_1^{\top}\mathbf{x}=\tfrac13(3+0+6)=3,\qquad c_2=\mathbf{q}_2^{\top}\mathbf{x}=\tfrac13(6+0-6)=0,\qquad c_3=\mathbf{q}_3^{\top}\mathbf{x}=\tfrac13(6+0+3)=3 .$$

Vérification : $3\mathbf{q}_1+0\cdot\mathbf{q}_2+3\mathbf{q}_3=(1,\,2,\,2)^{\top}+(2,\,-2,\,1)^{\top}=(3,\,0,\,3)^{\top}=\mathbf{x}$. Formule de la longueur : $c_1^2+c_2^2+c_3^2=9+0+9=18$ et $\lVert\mathbf{x}\rVert^2=9+0+9=18$.
:::
:::

:::aufgabe Exercice 2 ★ Une matrice orthogonale
<span class="anker" id="aufg-2"></span>

Soit $\mathbf{Q}$ la matrice de colonnes $\mathbf{q}_1,\mathbf{q}_2,\mathbf{q}_3$ de l’exercice [1](#aufg-1).

<ol class="al">

<li>

Donnez $\mathbf{Q}^{-1}$ sans calcul. Vérifiez $\mathbf{Q}\mathbf{Q}^{\top}=\mathbf{I}$ sur un coefficient hors diagonale de votre choix.

</li>

<li>

Calculez $\mathbf{Q}\,(1,\,1,\,1)^{\top}$ et comparez les longueurs. Calculez $\det\mathbf{Q}$. La matrice $\mathbf{Q}$ est-elle une rotation ou une réflexion ?

</li>

</ol>

:::loesung
(a) Les colonnes sont orthonormées, donc $\mathbf{Q}$ est orthogonale et $\mathbf{Q}^{-1}=\mathbf{Q}^{\top}$, sans calcul. Ici,

$$\mathbf{Q}=\frac13\begin{pmatrix}1&2&2\\2&1&-2\\2&-2&1\end{pmatrix}$$

est même symétrique, donc $\mathbf{Q}^{-1}=\mathbf{Q}^{\top}=\mathbf{Q}$. Le coefficient $(1,2)$ de $\mathbf{Q}\mathbf{Q}^{\top}$ est le produit scalaire de la première et de la deuxième ligne : $\tfrac19(1\cdot2+2\cdot1+2\cdot(-2))=0$.

(b) $\mathbf{Q}\,(1,\,1,\,1)^{\top}=\tfrac13(5,\,1,\,1)^{\top}$, de carré de longueur $\tfrac19(25+1+1)=3$, soit exactement le carré de la longueur de $(1,\,1,\,1)^{\top}$, comme l’exige [(1.3)](#gl-1-3). Le déterminant vaut

$$\det\mathbf{Q}=\tfrac1{27}\bigl(1\cdot(1-4)-2\cdot(2+4)+2\cdot(-4-2)\bigr)=\tfrac1{27}(-3-12-12)=-1 .$$

$\mathbf{Q}$ est donc une réflexion. Plus précisément : comme $\mathbf{Q}=\mathbf{Q}^{\top}=\mathbf{Q}^{-1}$, on a $\mathbf{Q}^2=\mathbf{I}$ ; appliquée deux fois, elle ramène tout à sa place. Le vecteur $\mathbf{k}=(1,\,-1,\,-1)^{\top}$ est retourné, $\mathbf{Q}\mathbf{k}=\tfrac13(1-2-2,\ 2-1+2,\ 2+2-1)^{\top}=(-1,\,1,\,1)^{\top}=-\mathbf{k}$, et les vecteurs perpendiculaires à $\mathbf{k}$ restent fixes. $\mathbf{Q}$ est la réflexion par rapport au plan $x_1-x_2-x_3=0$.
:::
:::

:::aufgabe Exercice 3 ★★ Calculer avec des matrices orthogonales
<span class="anker" id="aufg-3"></span>

<ol class="al">

<li>

Montrez que si $\mathbf{Q}_1$ et $\mathbf{Q}_2$ sont orthogonales, alors $\mathbf{Q}_1\mathbf{Q}_2$ est elle aussi orthogonale.

</li>

<li>

La somme de deux matrices orthogonales est-elle encore orthogonale ? Justifiez ou donnez un contre-exemple.

</li>

<li>

Montrez qu’une matrice diagonale est orthogonale si et seulement si chacun de ses coefficients diagonaux vaut $1$ ou $-1$. Que fait une telle matrice géométriquement ?

</li>

</ol>

:::loesung
(a) Avec $(\mathbf{A}\mathbf{B})^{\top}=\mathbf{B}^{\top}\mathbf{A}^{\top}$, on a $(\mathbf{Q}_1\mathbf{Q}_2)^{\top}(\mathbf{Q}_1\mathbf{Q}_2)=\mathbf{Q}_2^{\top}\mathbf{Q}_1^{\top}\mathbf{Q}_1\mathbf{Q}_2=\mathbf{Q}_2^{\top}\mathbf{I}\mathbf{Q}_2=\mathbf{I}$. Intuitivement : deux mouvements rigides successifs forment encore un mouvement rigide.

(b) Non. Contre-exemple : $\mathbf{I}+\mathbf{I}=2\mathbf{I}$, et $(2\mathbf{I})^{\top}(2\mathbf{I})=4\mathbf{I}\ne\mathbf{I}$ ; la somme double toutes les longueurs. De même, $\mathbf{I}+(-\mathbf{I})$ est la matrice nulle.

(c) Pour $\mathbf{D}=\operatorname{diag}(d_1,\dots,d_n)$, on a $\mathbf{D}^{\top}\mathbf{D}=\operatorname{diag}(d_1^2,\dots,d_n^2)$. C’est $\mathbf{I}$ si et seulement si chaque $d_i^2=1$, c’est-à-dire $d_i=1$ ou $d_i=-1$. Une telle matrice inverse le sens des axes pour lesquels $d_i=-1$ et laisse les autres en place : elle effectue des réflexions par rapport aux plans de coordonnées. Par exemple, $\operatorname{diag}(1;\,-1)$ est la réflexion par rapport à l’axe des $x_1$, et $\operatorname{diag}(-1;\,-1)$ est la rotation d’angle $180^\circ$.
:::
:::

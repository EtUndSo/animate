---
title: Matrices définies positives
pfad: Informatique / Apprentissage automatique / Fondements mathématiques / Projection, valeurs propres et décompositions
knoten: Fondements 2 : Projection, valeurs propres et décompositions
nachschlagen: ja
order: 15220900
summary: Une forme quadratique est une cuvette si elle est positive partout sauf à l’origine.
tags: définie positive, semi-définie positive, indéfinie, quotient de Rayleigh
lang: fr
---

<span class="anker" id="stufe-8"></span>

:::zweck
Une forme quadratique est une cuvette si elle est positive partout sauf à l’origine. Cette section donne un nom à cette propriété et présente des critères pour la vérifier : par les valeurs propres, par les pivots et par des déterminants. S’y ajoutent deux conséquences : la plus grande et la plus petite valeur d’une forme sur le cercle unité, et une décomposition que seules les cuvettes possèdent.
:::

### Définie positive et semi-définie positive

<span class="anker" id="stufe-8-1"></span>

La cuvette et la gouttière de la section [5.3](quadratische-formen.html#stufe-5-3) diffèrent en un point : hors de l’origine, la cuvette est partout positive, la gouttière seulement non négative. Ces deux propriétés portent des noms consacrés.

:::definition Définition 8.1 (Définie positive, semi-définie positive)
<span class="anker" id="satz-8-1"></span>

Une matrice symétrique $\mathbf{A}\in\mathbb{R}^{n\times n}$ est dite __définie positive__ si

<span class="anker" id="gl-8-1"></span>
$$\mathbf{x}^{\top}\mathbf{A}\mathbf{x}>0\qquad\text{pour tout}\ \mathbf{x}\ne\mathbf{0} , \tag{8.1}$$

et __semi-définie positive__ si $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}\ge0$ pour tout $\mathbf{x}$.
:::

La symétrie fait partie de la définition. Pour la forme quadratique, ce n’est pas une restriction : d’après la section [5.2](quadratische-formen.html#stufe-5-2), seule la partie symétrique compte de toute façon. Elle est cependant nécessaire pour que les critères de la sous-section suivante soient valables. Toute matrice définie positive est aussi semi-définie positive.

⁠**Exemple de calcul :** $\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ est définie positive, car d’après la section [5.4](quadratische-formen.html#stufe-5-4), $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=5(x_1+0{,}4x_2)^2+1{,}2x_2^2$, et cette expression n’est nulle que si $x_2=0$, et alors aussi $x_1=0$. La matrice $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ a pour forme $x_1^2+4x_1x_2+4x_2^2=(x_1+2x_2)^2\ge0$ ; elle est semi-définie positive, mais pas définie positive, car pour $\mathbf{x}=(2,\,-1)^{\top}$ la forme est nulle. Son graphe est une gouttière dont le fond de vallée est dans la direction $(2,\,-1)^{\top}$.

⁠**En bref :** Définie positive signifie : la forme quadratique est positive hors de l’origine, c’est une cuvette ; semi-définie positive signifie : elle n’est négative nulle part.

### Le critère des valeurs propres

<span class="anker" id="stufe-8-2"></span>

La forme en axes principaux [(7.4)](diagonalisierung-und-spektralsatz.html#gl-7-4) répond immédiatement à la question : une somme $\sum_i\lambda_ic_i^2$ est positive pour tout choix des coordonnées si tous les $\lambda_i$ sont positifs, et pas sinon.

:::satz Théorème 8.2 (Critère des valeurs propres)
<span class="anker" id="satz-8-2"></span>

Une matrice symétrique est définie positive si et seulement si toutes ses valeurs propres sont positives, et semi-définie positive si et seulement si aucune n’est négative.
:::

:::beweis Critère des valeurs propres
Si tous les $\lambda_i>0$ et si $\mathbf{x}\ne\mathbf{0}$, alors $\mathbf{c}=\mathbf{Q}^{\top}\mathbf{x}\ne\mathbf{0}$ aussi, car $\mathbf{Q}$ est inversible ; d’après [(7.4)](diagonalisierung-und-spektralsatz.html#gl-7-4), on a alors $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=\sum_i\lambda_ic_i^2>0$. Inversement, si une valeur propre vérifie $\lambda_i\le0$, alors pour le vecteur propre $\mathbf{x}=\mathbf{q}_i$, la forme vaut $\mathbf{q}_i^{\top}\mathbf{A}\mathbf{q}_i=\lambda_i\le0$, et $\mathbf{A}$ n’est pas définie positive. Pour le cas semi-défini, on procède de même, avec $\ge$ au lieu de $>$.
:::

Si une matrice symétrique a des valeurs propres positives et négatives, sa forme est positive dans certaines directions et négative dans d’autres : c’est une selle. Une telle matrice est dite __indéfinie__. De même, une matrice dont toutes les valeurs propres sont négatives est dite définie négative ; sa forme est un dôme.

⁠**Exemple de calcul :** $\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ a les valeurs propres $6$ et $1$ : définie positive. $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ a les valeurs propres $5$ et $0$ : semi-définie positive. $\bigl(\begin{smallmatrix}1&3\\3&1\end{smallmatrix}\bigr)$ n’a que des coefficients positifs, mais les valeurs propres $4$ et $-2$ : indéfinie, car pour $\mathbf{x}=(1,\,-1)^{\top}$, la forme vaut $1-6+1=-4$. Des coefficients positifs ne disent donc rien du caractère défini.

⁠**En bref :** Une matrice symétrique est définie positive si et seulement si toutes ses valeurs propres sont positives ; des valeurs propres positives et négatives à la fois donnent une selle.

:::hintergrund Pourquoi la symétrie fait partie de la définition
Certains ouvrages définissent les matrices définies positives par la forme quadratique, d’autres par les valeurs propres. Pour les matrices symétriques, c’est la même chose d’après le théorème ; pour les matrices non symétriques, non. La matrice $\bigl(\begin{smallmatrix}2&-5\\0&2\end{smallmatrix}\bigr)$, étant triangulaire, a les valeurs propres $2$ et $2$, toutes deux positives. Sa forme quadratique est pourtant $2x_1^2-5x_1x_2+2x_2^2$, et pour $\mathbf{x}=(1,\,1)^{\top}$ elle vaut $2-5+2=-1$. La raison : la forme ne voit que la partie symétrique $\bigl(\begin{smallmatrix}2&-2{,}5\\-2{,}5&2\end{smallmatrix}\bigr)$, de valeurs propres $4{,}5$ et $-0{,}5$, alors que les valeurs propres appartiennent à la matrice entière. Quiconque emploie la notion sans symétrie doit donc toujours préciser de quelle définition il s’agit.
:::

### Critères sans valeurs propres

<span class="anker" id="stufe-8-3"></span>

Pour de grandes matrices, calculer les valeurs propres est coûteux. La complétion du carré de la section [5.4](quadratische-formen.html#stufe-5-4) fournit un critère sans valeurs propres, et il en découle un second, avec des déterminants.

:::satz Théorème 8.3 (Critères pour les matrices définies positives)
<span class="anker" id="satz-8-3"></span>

Pour une matrice symétrique $\mathbf{A}\in\mathbb{R}^{n\times n}$, les propriétés suivantes sont équivalentes :

<ol class="rm">

<li>

$\mathbf{A}$ est définie positive ;

</li>

<li>

la méthode du pivot de Gauss sans échange de lignes fournit $n$ pivots positifs ;

</li>

<li>

tous les mineurs principaux dominants sont positifs : les déterminants des sous-matrices $k\times k$ situées en haut à gauche sont strictement positifs pour $k=1,\dots,n$.

</li>

</ol>

Pour $n=2$ et $\mathbf{A}=\bigl(\begin{smallmatrix}a&b\\b&c\end{smallmatrix}\bigr)$, cela signifie : $a>0$ et $ac-b^2>0$.
:::

Pour $n=2$, c’est [(5.3)](quadratische-formen.html#gl-5-3) : les pivots sont $a$ et $c-b^2/a$, la forme est une cuvette si et seulement si les deux sont positifs, et, pour $a>0$, $c-b^2/a>0$ équivaut à $ac-b^2>0$. Pour $n$ plus grand, chaque étape d’élimination complète une variable en un carré, comme dans l’encadré « Contexte » de la section [5.4](quadratische-formen.html#stufe-5-4). Le déterminant de la sous-matrice $k\times k$ en haut à gauche est le produit des $k$ premiers pivots ; c’est pourquoi les pivots sont tous positifs si et seulement si les mineurs principaux dominants le sont. Le critère des déterminants est aussi appelé critère de Sylvester.

Deux mises en garde. Premièrement, $\det\mathbf{A}>0$ seul ne suffit pas : $\operatorname{diag}(-1;\,-3)$ a pour déterminant $3$, mais elle est définie négative. Deuxièmement, le critère ne se transpose pas simplement au cas semi-défini : $\operatorname{diag}(0;\,-1)$ a pour mineurs principaux dominants $0$ et $0$, tous deux non négatifs, et n’est pourtant pas semi-définie positive.

⁠**Exemple de calcul :** Pour

$$\mathbf{A}=\begin{pmatrix}2&1&0\\1&2&1\\0&1&2\end{pmatrix}$$

les mineurs principaux dominants valent $2$, $\det\bigl(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr)=3$ et $\det\mathbf{A}=2\cdot3-1\cdot2=4$, tous positifs : $\mathbf{A}$ est définie positive. Les pivots sont $2$, $\tfrac32$ et $\tfrac43$, les quotients de mineurs consécutifs. Pour contrôle : les valeurs propres sont $2-\sqrt2$, $2$ et $2+\sqrt2$, toutes positives, et leur produit vaut $(4-2)\cdot2=4$.

⁠**En bref :** Une matrice symétrique est définie positive si et seulement si tous les pivots, ou tous les mineurs principaux dominants, sont positifs ; pour une matrice $2\times2$, cela signifie $a>0$ et $ac-b^2>0$.

### Les matrices de Gram sont semi-définies positives

<span class="anker" id="stufe-8-4"></span>

Dans Fondements 1, section 10, sont apparues les matrices de Gram $\mathbf{X}^{\top}\mathbf{X}$ et $\mathbf{X}\mathbf{X}^{\top}$, et dans ce chapitre, $\mathbf{A}^{\top}\mathbf{A}$ dans les équations normales. Elles sont toujours semi-définies positives, et la raison en est simple : leur forme quadratique est un carré de longueur.

:::satz Théorème 8.4 (Matrices de Gram)
<span class="anker" id="satz-8-4"></span>

Pour toute matrice $\mathbf{A}\in\mathbb{R}^{m\times n}$, $\mathbf{A}^{\top}\mathbf{A}$ est semi-définie positive. Elle est définie positive si et seulement si les colonnes de $\mathbf{A}$ sont linéairement indépendantes.
:::

:::beweis Matrices de Gram
$\mathbf{A}^{\top}\mathbf{A}$ est symétrique, et $\mathbf{x}^{\top}\mathbf{A}^{\top}\mathbf{A}\mathbf{x}=(\mathbf{A}\mathbf{x})^{\top}(\mathbf{A}\mathbf{x})=\lVert\mathbf{A}\mathbf{x}\rVert^2\ge0$. Cette quantité est nulle si et seulement si $\mathbf{A}\mathbf{x}=\mathbf{0}$. Si les colonnes sont indépendantes, cela n’arrive que pour $\mathbf{x}=\mathbf{0}$.
:::

Il en va de même pour $\mathbf{A}\mathbf{A}^{\top}$, avec les lignes au lieu des colonnes. Le théorème explique après coup la section [3.5](die-beste-naherungslosung.html#stufe-3-5) : si les colonnes sont indépendantes, $\mathbf{A}^{\top}\mathbf{A}$ est définie positive, n’a donc que des valeurs propres positives et est inversible.

⁠**Exemple de calcul :** $\mathbf{H}^{\top}\mathbf{H}=\bigl(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr)$ a les valeurs propres $3$ et $1$ : définie positive, ce qui concorde avec les colonnes indépendantes de $\mathbf{H}$. Pour $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$, on a $\mathbf{A}^{\top}\mathbf{A}=\bigl(\begin{smallmatrix}5&10\\10&20\end{smallmatrix}\bigr)$, de déterminant $0$ et de valeurs propres $25$ et $0$ : semi-définie positive, mais pas définie positive.

⁠**En bref :** $\mathbf{A}^{\top}\mathbf{A}$ est toujours semi-définie positive, car $\mathbf{x}^{\top}\mathbf{A}^{\top}\mathbf{A}\mathbf{x}=\lVert\mathbf{A}\mathbf{x}\rVert^2$ ; si les colonnes sont indépendantes, elle est définie positive.

### Plus grande et plus petite valeur sur le cercle unité

<span class="anker" id="stufe-8-5"></span>

Une forme quadratique croît comme le carré de la longueur de $\mathbf{x}$. Pour voir à quel point elle croît dans les différentes directions, on ne l’évalue qu’en des vecteurs de longueur $1$. Dans quelle direction est-elle la plus grande ?

:::satz Théorème 8.5 (Valeurs extrêmes d’une forme quadratique)
<span class="anker" id="satz-8-5"></span>

Soit $\mathbf{A}$ symétrique, de plus petite valeur propre $\lambda_{\min}$ et de plus grande valeur propre $\lambda_{\max}$. Pour tout vecteur $\mathbf{x}\ne\mathbf{0}$,

<span class="anker" id="gl-8-2"></span>
$$\lambda_{\min}\le\frac{\mathbf{x}^{\top}\mathbf{A}\mathbf{x}}{\mathbf{x}^{\top}\mathbf{x}}\le\lambda_{\max} . \tag{8.2}$$

La plus grande valeur est atteinte en un vecteur propre associé à $\lambda_{\max}$, la plus petite en un vecteur propre associé à $\lambda_{\min}$.
:::

:::beweis Valeurs extrêmes
Avec $\mathbf{c}=\mathbf{Q}^{\top}\mathbf{x}$, on a $\mathbf{x}^{\top}\mathbf{x}=\mathbf{c}^{\top}\mathbf{c}=\sum_ic_i^2$, car $\mathbf{Q}$ conserve les longueurs, et $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=\sum_i\lambda_ic_i^2$. Le quotient vaut donc

$$\frac{\sum_i\lambda_ic_i^2}{\sum_ic_i^2}=\sum_i\lambda_i\,g_i\qquad\text{avec}\qquad g_i=\frac{c_i^2}{\sum_lc_l^2}\ge0,\quad \sum_ig_i=1 .$$

C’est une moyenne pondérée des valeurs propres, et une moyenne est toujours comprise entre la plus petite et la plus grande des valeurs moyennées. Pour $\mathbf{x}=\mathbf{q}_i$, seul le poids $g_i=1$ est non nul, et le quotient vaut $\lambda_i$.
:::

Le quotient de [(8.2)](#gl-8-2) est appelé __quotient de Rayleigh__. Pour $\lVert\mathbf{x}\rVert=1$, c’est la forme quadratique elle-même : sur le cercle unité, la forme est comprise entre la plus petite et la plus grande valeur propre.

⁠**Exemple de calcul :** Pour $\mathbf{A}=\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$, le quotient de Rayleigh vaut $5$ en $\mathbf{e}_1$, $2$ en $\mathbf{e}_2$, $\tfrac{5+4+2}2=5{,}5$ en $(1,\,1)^{\top}/\sqrt2$ et $\tfrac{5-4+2}2=1{,}5$ en $(1,\,-1)^{\top}/\sqrt2$. Toutes ces valeurs sont comprises entre $1$ et $6$. Il atteint la valeur $6$ en $\mathbf{q}_1=(2,\,1)^{\top}/\sqrt5$ : $\tfrac15(20+8+2)=6$. Le quotient ne dépend pas de la longueur de $\mathbf{x}$ ; la Fig. [21](#abb-21) le calcule pour $\mathbf{x}=(1,\,1)^{\top}$, sans racines.

:::abbildung ml/k2rrayleigh 21
Le quotient de Rayleigh de $\mathbf{A}=\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ au point $\mathbf{x}=(1,1)^{\top}$ : numérateur et dénominateur comme sommes ; le quotient $\tfrac{11}2=5{,}5$ est compris entre les valeurs propres $1$ et $6$.
:::

⁠**En bref :** Sur le cercle unité, une forme quadratique est comprise entre la plus petite et la plus grande valeur propre, et ces valeurs extrêmes sont atteintes dans les directions propres.

### La décomposition de Cholesky

<span class="anker" id="stufe-8-6"></span>

Compléter le carré écrit une forme définie positive comme une somme de carrés. Si l’on regroupe en un vecteur les expressions à l’intérieur des carrés, la forme est le carré de la longueur de ce vecteur. Il en résulte une décomposition de la matrice.

:::satz Théorème 8.6 (Décomposition de Cholesky)
<span class="anker" id="satz-8-6"></span>

Une matrice symétrique $\mathbf{A}$ est définie positive si et seulement s’il existe une matrice triangulaire inférieure $\mathbf L$ à coefficients diagonaux positifs telle que

<span class="anker" id="gl-8-3"></span>
$$\mathbf{A}=\mathbf L\mathbf L^{\top} . \tag{8.3}$$

Cette matrice $\mathbf L$ est unique et est appelée le facteur de Cholesky de $\mathbf{A}$.
:::

Si $\mathbf{A}=\mathbf L\mathbf L^{\top}$, alors $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=\lVert\mathbf L^{\top}\mathbf{x}\rVert^2$, une somme de carrés, et comme $\mathbf L$ est inversible, elle n’est nulle que pour $\mathbf{x}=\mathbf{0}$. C’est l’un des deux sens. L’autre sens, à savoir que toute matrice définie positive possède un tel facteur, c’est la complétion du carré : pour $n=2$, on le lit sur [(5.3)](quadratische-formen.html#gl-5-3),

$$\mathbf L=\begin{pmatrix}\sqrt a&0\\b/\sqrt a&\sqrt{c-b^2/a}\end{pmatrix},$$

et pour $n$ plus grand, on poursuit la complétion variable par variable. D’après Fondements 1, section 14.5, $\det\mathbf{A}=\det\mathbf L\cdot\det\mathbf L^{\top}=(l_{11}\cdots l_{nn})^2$.

⁠**Exemple de calcul :** Pour $\mathbf{A}=\bigl(\begin{smallmatrix}4&2\\2&5\end{smallmatrix}\bigr)$, on a $a=4$, $b=2$, $c=5$, donc $l_{11}=2$, $l_{21}=1$ et $l_{22}=\sqrt{5-1}=2$ :

$$\mathbf L=\begin{pmatrix}2&0\\1&2\end{pmatrix},\qquad \mathbf L\mathbf L^{\top}=\begin{pmatrix}4&2\\2&1+4\end{pmatrix}=\mathbf{A} .$$

La forme est $4x_1^2+4x_1x_2+5x_2^2=(2x_1+x_2)^2+(2x_2)^2$ ; les deux expressions à l’intérieur des carrés sont les composantes de $\mathbf L^{\top}\mathbf{x}$. Le déterminant vaut $20-4=16=(2\cdot2)^2$.

⁠**En bref :** Toute matrice définie positive s’écrit $\mathbf L\mathbf L^{\top}$ avec une matrice triangulaire inférieure $\mathbf L$ ; cette décomposition est la complétion du carré sous forme matricielle.

:::aufgabe Exercice 24 ★ Déterminer le caractère défini
<span class="anker" id="aufg-24"></span>

À l’aide de deux critères différents, déterminez si les matrices suivantes sont définies positives, semi-définies positives, définies négatives ou indéfinies :

$$\mathbf{A}_1=\begin{pmatrix}3&1\\1&2\end{pmatrix},\qquad \mathbf{A}_2=\begin{pmatrix}2&6\\6&18\end{pmatrix},\qquad \mathbf{A}_3=\begin{pmatrix}1&3\\3&2\end{pmatrix},\qquad \mathbf{A}_4=\begin{pmatrix}-2&1\\1&-1\end{pmatrix}.$$

:::loesung
<ul>

<li>

$\mathbf{A}_1$ : $a=3>0$ et $ac-b^2=6-1=5>0$ : définie positive. Valeurs propres : trace $5$, déterminant $5$, $\lambda=\tfrac{5\pm\sqrt5}2\approx3{,}62$ et $1{,}38$, toutes deux positives.

</li>

<li>

$\mathbf{A}_2$ : $a=2>0$, mais $ac-b^2=36-36=0$. Valeurs propres $20$ et $0$ : semi-définie positive, mais pas définie. Après complétion du carré : $2(x_1+3x_2)^2$, une gouttière.

</li>

<li>

$\mathbf{A}_3$ : $ac-b^2=2-9=-7<0$ ; le produit des valeurs propres vaut $-7$, elles sont donc de signes contraires : indéfinie. Elles valent $\tfrac{3\pm\sqrt{37}}2\approx4{,}54$ et $-1{,}54$.

</li>

<li>

$\mathbf{A}_4$ : $a=-2<0$, donc pas définie positive. Pour $-\mathbf{A}_4=\bigl(\begin{smallmatrix}2&-1\\-1&1\end{smallmatrix}\bigr)$, on a $a=2>0$ et $ac-b^2=1>0$ ; $-\mathbf{A}_4$ est donc définie positive, et $\mathbf{A}_4$ définie négative. Valeurs propres de $\mathbf{A}_4$ : trace $-3$, déterminant $1$, $\lambda=\tfrac{-3\pm\sqrt5}2\approx-0{,}38$ et $-2{,}62$, toutes deux négatives : un dôme.

</li>

</ul>
:::
:::

:::aufgabe Exercice 25 ★★ Un piège
<span class="anker" id="aufg-25"></span>

<ol class="al">

<li>

La matrice $\bigl(\begin{smallmatrix}1&-4\\0&1\end{smallmatrix}\bigr)$ n’a que des valeurs propres positives. Sa forme quadratique est-elle positive ? Trouvez un vecteur qui montre le contraire, et expliquez la contradiction.

</li>

<li>

Pour quels nombres $t$ la matrice $\bigl(\begin{smallmatrix}1&t\\t&4\end{smallmatrix}\bigr)$ est-elle définie positive ? Pour lesquels est-elle semi-définie positive ?

</li>

</ol>

:::loesung
(a) Les valeurs propres sont $1$ et $1$, mais la forme $x_1^2-4x_1x_2+x_2^2$ vaut $1-4+1=-2<0$ en $\mathbf{x}=(1,\,1)^{\top}$. Il n’y a pas de contradiction : le critère des valeurs propres ne vaut que pour les matrices symétriques. La forme ne voit que la partie symétrique $\bigl(\begin{smallmatrix}1&-2\\-2&1\end{smallmatrix}\bigr)$, et celle-ci a les valeurs propres $3$ et $-1$ ; la forme est indéfinie.

(b) Avec le critère $2\times2$ : $a=1>0$, et $ac-b^2=4-t^2>0$ exactement pour $|t|<2$. Pour que la matrice soit semi-définie positive, il faut des valeurs propres $\ge0$. Leur somme est la trace $5>0$, leur produit le déterminant $4-t^2$ ; toutes deux sont $\ge0$ si et seulement si $4-t^2\ge0$, c’est-à-dire pour $|t|\le2$. Pour $t=\pm2$, la matrice est semi-définie positive, mais pas définie, de valeurs propres $5$ et $0$ ; pour $|t|>2$, elle est indéfinie.
:::
:::

:::aufgabe Exercice 26 ★★ Quotient de Rayleigh et Cholesky
<span class="anker" id="aufg-26"></span>

Soit $\mathbf{A}=\bigl(\begin{smallmatrix}4&2\\2&5\end{smallmatrix}\bigr)$.

<ol class="al">

<li>

Calculez les valeurs propres et le quotient de Rayleigh aux points $\mathbf{e}_1$, $\mathbf{e}_2$ et $(1,\,1)^{\top}$. Vérifiez [(8.2)](#gl-8-2).

</li>

<li>

Résolvez $\mathbf{A}\mathbf{x}=(2,\,9)^{\top}$ à l’aide du facteur de Cholesky : d’abord $\mathbf L\mathbf{z}=(2,\,9)^{\top}$ de haut en bas, puis $\mathbf L^{\top}\mathbf{x}=\mathbf{z}$ de bas en haut.

</li>

</ol>

:::loesung
(a) Trace $9$, déterminant $16$ : $\lambda=\tfrac{9\pm\sqrt{81-64}}2=\tfrac{9\pm\sqrt{17}}2\approx6{,}56$ et $2{,}44$. Le quotient de Rayleigh vaut $4$ en $\mathbf{e}_1$, $5$ en $\mathbf{e}_2$ et $\tfrac{4+2+2+5}2=\tfrac{13}2=6{,}5$ en $(1,\,1)^{\top}$. Ces trois valeurs sont comprises entre $2{,}44$ et $6{,}56$ ; la troisième est proche du maximum, car $(1,\,1)^{\top}$ pointe presque dans la direction du vecteur propre associé à la plus grande valeur propre.

(b) D’après la section [8.6](#stufe-8-6) : $\mathbf L=\bigl(\begin{smallmatrix}2&0\\1&2\end{smallmatrix}\bigr)$. De haut en bas : $2z_1=2$, donc $z_1=1$ ; $z_1+2z_2=9$, donc $z_2=4$. Puis $\mathbf L^{\top}\mathbf{x}=\mathbf{z}$ de bas en haut : $2x_2=4$, donc $x_2=2$ ; $2x_1+x_2=1$, donc $x_1=-\tfrac12$. Vérification : $\mathbf{A}(-\tfrac12,\,2)^{\top}=(-2+4,\ -1+10)^{\top}=(2,\,9)^{\top}$. Deux systèmes triangulaires remplacent un système d’équations quelconque.
:::
:::

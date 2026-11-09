---
title: Formes quadratiques
pfad: Informatique / Apprentissage automatique / Fondements mathématiques / Projection, valeurs propres et décompositions
knoten: Fondements 2 : Projection, valeurs propres et décompositions
nachschlagen: ja
order: 15220600
summary: Après les fonctions linéaires, les fonctions quadratiques sont les fonctions de plusieurs variables les plus simples.
tags: forme quadratique
lang: fr
---

<span class="anker" id="stufe-5"></span>

:::zweck
Après les fonctions linéaires, les fonctions quadratiques sont les fonctions de plusieurs variables les plus simples. Elles décrivent des énergies, des carrés d’erreurs et des surfaces courbes. Cette section les écrit à l’aide d’une matrice, présente les trois formes de base, cuvette, gouttière et selle, et montre comment reconnaître sur la matrice de quelle forme il s’agit, tant qu’il n’y a pas de termes croisés.
:::

### Formes quadratiques

<span class="anker" id="stufe-5-1"></span>

Dans [Fondements 1, section 8.4](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/lineare-abbildungen.html#stufe-8-4), toute fonction linéaire à une sortie était une somme pondérée $\mathbf{w}^{\top}\mathbf{x}$ des composantes. Le type de fonction suivant par ordre de simplicité additionne des produits de deux composantes : des carrés comme $x_1^2$ et des termes croisés comme $x_1x_2$. Un exemple tiré de l’électrotechnique est l’énergie magnétique de deux bobines couplées d’inductances $L_1$, $L_2$ et d’inductance mutuelle $M$, parcourues par les courants $i_1$ et $i_2$ :

$$W=\tfrac12L_1i_1^2+M\,i_1i_2+\tfrac12L_2i_2^2 .$$

De telles sommes peuvent s’écrire avec une matrice au milieu.

:::definition Définition 5.1 (Forme quadratique)
<span class="anker" id="satz-5-1"></span>

Pour une matrice carrée $\mathbf{A}\in\mathbb{R}^{n\times n}$, la fonction

<span class="anker" id="gl-5-1"></span>
$$f(\mathbf{x})=\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=\sum_{i=1}^n\sum_{l=1}^na_{il}\,x_ix_l \tag{5.1}$$

est appelée la __forme quadratique__ de $\mathbf{A}$.
:::

Le résultat est un nombre : $\mathbf{A}\mathbf{x}$ est un vecteur, et $\mathbf{x}^{\top}(\mathbf{A}\mathbf{x})$ est le produit scalaire de $\mathbf{x}$ avec ce vecteur. Pour $n=2$, on obtient en détaillant

$$\mathbf{x}^{\top}\begin{pmatrix}a_{11}&a_{12}\\a_{21}&a_{22}\end{pmatrix}\mathbf{x}=a_{11}x_1^2+(a_{12}+a_{21})\,x_1x_2+a_{22}x_2^2 .$$

Si l’on double $\mathbf{x}$, $f$ est multiplié par quatre : $f(c\,\mathbf{x})=c^2f(\mathbf{x})$. D’où le nom.

::::beispiel [Exemple de calcul]
Pour $\mathbf{A}=\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$, on a $f(\mathbf{x})=5x_1^2+4x_1x_2+2x_2^2$. Au point $\mathbf{x}=(1,\,-1)^{\top}$, on a $f=5-4+2=3$ ; pour contrôle, $\mathbf{A}\mathbf{x}=(3,\,0)^{\top}$ et $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=3$. La Fig. [14](#abb-14) calcule la double somme [(5.1)](#gl-5-1) en ce point, terme par terme. Au point $(1,\,1)^{\top}$, on a $f=11$ ; à l’origine, $f=0$. L’énergie des deux bobines vaut $W=\tfrac12\,\mathbf i^{\top}\bigl(\begin{smallmatrix}L_1&M\\M&L_2\end{smallmatrix}\bigr)\,\mathbf i$ avec le vecteur des courants $\mathbf i=(i_1,\,i_2)^{\top}$ ; la matrice est appelée matrice d’inductance.

:::abbildung ml/k2rqf 14
La forme quadratique de $\mathbf{A}=\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ au point $\mathbf{x}=(1,-1)^{\top}$ comme double somme : quatre termes, un pour chaque coefficient de $\mathbf{A}$.
:::
::::

⁠**En bref :** Une forme quadratique $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}$ est une somme de carrés et de produits croisés des composantes, avec les coefficients de $\mathbf{A}$ comme poids.

### Seule la partie symétrique compte

<span class="anker" id="stufe-5-2"></span>

Dans l’expression pour $n=2$, $a_{12}$ et $a_{21}$ n’interviennent que par leur somme. Les matrices $\bigl(\begin{smallmatrix}5&4\\0&2\end{smallmatrix}\bigr)$ et $\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ ont donc la même forme quadratique. On peut toujours choisir la matrice symétrique.

:::satz Théorème 5.2 (La partie symétrique)
<span class="anker" id="satz-5-2"></span>

Pour toute matrice carrée $\mathbf{A}$ et tout $\mathbf{x}$,

<span class="anker" id="gl-5-2"></span>
$$\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=\mathbf{x}^{\top}\Bigl(\frac{\mathbf{A}+\mathbf{A}^{\top}}2\Bigr)\mathbf{x} . \tag{5.2}$$
:::

:::beweis La partie symétrique
Le nombre $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}$ est égal à sa propre transposée, donc $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=(\mathbf{x}^{\top}\mathbf{A}\mathbf{x})^{\top}=\mathbf{x}^{\top}\mathbf{A}^{\top}\mathbf{x}$. La moyenne des deux expressions est $\mathbf{x}^{\top}\frac{\mathbf{A}+\mathbf{A}^{\top}}2\mathbf{x}$.
:::

La matrice $\frac12(\mathbf{A}+\mathbf{A}^{\top})$ est symétrique. Dans ce chapitre, une forme quadratique a donc toujours une matrice symétrique. On la lit ainsi : sur la diagonale figurent les coefficients des carrés, et hors de la diagonale, à chaque fois la moitié du coefficient du terme croisé.

::::beispiel [Exemple de calcul]
La forme $3x_1^2-6x_1x_2+x_2^2$ a pour matrice symétrique $\bigl(\begin{smallmatrix}3&-3\\-3&1\end{smallmatrix}\bigr)$. La forme $x_1^2+2x_2^2+4x_3^2+2x_1x_3$ de $\mathbb{R}^3$ a pour matrice $\Bigl(\begin{smallmatrix}1&0&1\\0&2&0\\1&0&4\end{smallmatrix}\Bigr)$ ; le terme croisé $2x_1x_3$ se répartit sur les coefficients $(1,3)$ et $(3,1)$.
::::

⁠**En bref :** Une forme quadratique ne voit que la partie symétrique de sa matrice ; on l’écrit donc toujours avec une matrice symétrique.

### Cuvette, gouttière et selle

<span class="anker" id="stufe-5-3"></span>

Pour deux variables, on peut dessiner la forme quadratique comme une surface au-dessus du plan, avec $f(\mathbf{x})$ comme altitude, et, comme sur une carte, ses lignes de niveau, les lignes d’égale altitude. C’est le plus simple lorsque la matrice est diagonale. Il n’y a alors pas de termes croisés, et $f(\mathbf{x})=a_{11}x_1^2+a_{22}x_2^2$. Selon les signes des deux coefficients, on obtient trois formes de base (Fig. [15](#abb-15)).

:::abbildung ml/k2formen 15
En haut, les graphes des formes quadratiques $x_1^2+2x_2^2$ (cuvette), $x_1^2$ (gouttière) et $x_1^2-x_2^2$ (selle) au-dessus du carré $|x_1|,|x_2|\le1$ ; en bas, leurs lignes de niveau. Pour la cuvette, ce sont des ellipses ($f=\tfrac14,\tfrac12,1$) ; pour la gouttière, des paires de droites parallèles, avec en tirets la droite $x_1=0$, sur laquelle la gouttière est à l’altitude zéro. Pour la selle, ce sont des hyperboles, en trait fort pour $f=\tfrac14,\tfrac12$, en trait pâle pour $f=-\tfrac14,-\tfrac12$ ; en tirets, les deux droites où $f=0$.
:::

<ul>

<li>

⁠**Cuvette :** les deux coefficients diagonaux sont positifs, par exemple $f=x_1^2+2x_2^2$. Alors $f(\mathbf{x})>0$ pour tout $\mathbf{x}\ne\mathbf{0}$, et $f=0$ seulement à l’origine. Les lignes de niveau sont des ellipses centrées à l’origine, dont les demi-axes sont portés par les axes de coordonnées.

</li>

<li>

⁠**Gouttière :** un coefficient est positif, l’autre nul, par exemple $f=x_1^2$. Alors $f\ge0$, mais $f=0$ sur toute la droite $x_1=0$ : la surface y présente un fond de vallée rectiligne. Les lignes de niveau sont des paires de droites parallèles.

</li>

<li>

⁠**Selle :** les coefficients sont de signes contraires, par exemple $f=x_1^2-x_2^2$. Le long de l’axe des $x_1$, la surface monte des deux côtés ; le long de l’axe des $x_2$, elle descend des deux côtés. Les lignes de niveau sont des hyperboles.

</li>

</ul>

Si les deux coefficients sont négatifs, la cuvette est à l’envers ; c’est un dôme. Un coefficient négatif et un coefficient nul donnent une gouttière retournée, une crête. Avec plus de deux variables, il en va de même : les signes des coefficients diagonaux décident de la forme.

::::beispiel [Exemple de calcul]
Pour la cuvette $f=x_1^2+2x_2^2$, la ligne de niveau $f=1$ est l’ellipse de demi-axes $1$ sur l’axe des $x_1$ et $1/\sqrt2\approx0{,}707$ sur l’axe des $x_2$ : en $(1,\,0)^{\top}$ et en $(0,\,1/\sqrt2)^{\top}$, on a $f=1$. Pour la selle $f=x_1^2-x_2^2$, on a $f(1,\,0)=1$, $f(0,\,1)=-1$ et $f(1,\,1)=0$.
::::

⁠**En bref :** Sans termes croisés, on lit la forme sur les signes de la diagonale : tous positifs, une cuvette ; positif et nul, une gouttière ; signes contraires, une selle.

### Compléter le carré

<span class="anker" id="stufe-5-4"></span>

Avec des termes croisés, on ne voit plus la forme immédiatement. La forme $5x_1^2+4x_1x_2+2x_2^2$ est-elle une cuvette ? Le terme croisé peut devenir négatif. On connaît depuis le lycée un outil qui élimine les termes croisés : compléter le carré. Cette technique écrit la forme comme une somme de carrés, et l’on lit la forme sur les coefficients des carrés, comme dans la sous-section précédente.

:::herleitung Compléter le carré pour deux variables
Soit $a\ne0$. On met $a$ en facteur dans les termes contenant $x_1$ et l’on complète pour obtenir un carré :

$$ax_1^2+2bx_1x_2+cx_2^2=a\Bigl(x_1^2+\frac{2b}ax_1x_2\Bigr)+cx_2^2=a\Bigl(x_1+\frac bax_2\Bigr)^2-\frac{b^2}ax_2^2+cx_2^2 .$$

On a donc

<span class="anker" id="gl-5-3"></span>
$$ax_1^2+2bx_1x_2+cx_2^2=a\Bigl(x_1+\frac bax_2\Bigr)^2+\Bigl(c-\frac{b^2}a\Bigr)x_2^2 . \tag{5.3}$$
:::

Le membre de droite est une somme de deux carrés. Les nouvelles variables $z_1=x_1+\frac bax_2$ et $z_2=x_2$ prennent tous les couples de valeurs possibles lorsque $\mathbf{x}$ parcourt le plan. La forme dans les variables $z_1,z_2$ n’a donc plus de terme croisé, et les signes de $a$ et de $c-b^2/a$ décident s’il s’agit d’une cuvette, d’une gouttière ou d’une selle.

::::beispiel [Exemple de calcul 1]
Pour $5x_1^2+4x_1x_2+2x_2^2$, on a $a=5$, $b=2$, $c=2$ :

$$5x_1^2+4x_1x_2+2x_2^2=5\,(x_1+0{,}4\,x_2)^2+1{,}2\,x_2^2 .$$

Les deux coefficients sont positifs : la forme est une cuvette. Vérification en $\mathbf{x}=(1,\,-1)^{\top}$ : $5\cdot0{,}36+1{,}2=3$.
::::

::::beispiel [Exemple de calcul 2]
On a $x_1^2+6x_1x_2+x_2^2=(x_1+3x_2)^2-8x_2^2$. Les coefficients sont de signes contraires : c’est une selle. Effectivement, $f(1,\,0)=1>0$ et $f(1,\,-1)=1-6+1=-4<0$.
::::

⁠**En bref :** Compléter le carré écrit une forme quadratique comme une somme de carrés ; les signes des coefficients des carrés montrent s’il s’agit d’une cuvette, d’une gouttière ou d’une selle.

:::hintergrund Compléter le carré, c’est la méthode du pivot de Gauss
Les nombres de [(5.3)](#gl-5-3) sont les mêmes que dans la méthode du pivot de Gauss de [Fondements 1, section 12.3](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/lineare-gleichungssysteme.html#stufe-12-3), appliquée à la matrice symétrique $\bigl(\begin{smallmatrix}a&b\\b&c\end{smallmatrix}\bigr)$. Pour créer un zéro sous la diagonale, on retranche de la deuxième ligne $\frac ba$ fois la première et l’on obtient $\bigl(\begin{smallmatrix}a&b\\0&c-b^2/a\end{smallmatrix}\bigr)$. Les coefficients diagonaux de cette forme échelonnée, ce qu’on appelle les pivots, sont exactement les coefficients des carrés, et le facteur d’élimination $\frac ba$ figure dans la première parenthèse. Pour la matrice $\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ : facteur $0{,}4$, pivots $5$ et $1{,}2$. Avec $n$ variables, on poursuit de la même façon : chaque étape d’élimination complète une variable en un carré. La forme est une cuvette si et seulement si tous les pivots sont positifs. D’après les règles de calcul de [Fondements 1, section 14.5](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/die-determinante.html#stufe-14-5), le produit des pivots est le déterminant, ici $5\cdot1{,}2=6=5\cdot2-2\cdot2$.
:::

:::aufgabe Exercice 14 ★ Formes et matrices
<span class="anker" id="aufg-14"></span>

<ol class="al">

<li>

Donnez la matrice symétrique des formes $2x_1^2-2x_1x_2+3x_2^2$ et $x_1x_2$.

</li>

<li>

Calculez la forme de $\bigl(\begin{smallmatrix}1&3\\-1&2\end{smallmatrix}\bigr)$ et sa matrice symétrique.

</li>

<li>

Déterminez sans calcul si $3x_1^2+x_2^2$, $-x_1^2$ et $2x_1^2-x_2^2+x_3^2$ sont une cuvette, une gouttière, une selle ou autre chose.

</li>

</ol>

:::loesung
(a) Sur la diagonale, les coefficients des carrés ; hors de la diagonale, la moitié du coefficient du terme croisé : $2x_1^2-2x_1x_2+3x_2^2$ a pour matrice $\bigl(\begin{smallmatrix}2&-1\\-1&3\end{smallmatrix}\bigr)$, et $x_1x_2$ a pour matrice $\bigl(\begin{smallmatrix}0&1/2\\1/2&0\end{smallmatrix}\bigr)$.

(b) $\mathbf{x}^{\top}\bigl(\begin{smallmatrix}1&3\\-1&2\end{smallmatrix}\bigr)\mathbf{x}=x_1^2+(3-1)\,x_1x_2+2x_2^2=x_1^2+2x_1x_2+2x_2^2$. La matrice symétrique est $\tfrac12(\mathbf{A}+\mathbf{A}^{\top})=\bigl(\begin{smallmatrix}1&1\\1&2\end{smallmatrix}\bigr)$.

(c) $3x_1^2+x_2^2$ : les deux coefficients sont positifs, c’est une cuvette. $-x_1^2$ : un coefficient négatif et un coefficient nul, donc une gouttière retournée, une crête le long de l’axe des $x_2$. $2x_1^2-x_2^2+x_3^2$ : des signes différents, donc une selle ; le long des axes des $x_1$ et des $x_3$, la forme monte ; le long de l’axe des $x_2$, elle descend.
:::
:::

:::aufgabe Exercice 15 ★★ Compléter le carré
<span class="anker" id="aufg-15"></span>

Complétez le carré et déterminez la forme :

$$f_1=2x_1^2+8x_1x_2+11x_2^2,\qquad f_2=x_1^2+4x_1x_2+4x_2^2,\qquad f_3=x_1^2+4x_1x_2+x_2^2 .$$

Pour la gouttière, donnez la droite sur laquelle $f=0$, et pour la selle, un point où $f<0$.

:::loesung
Avec [(5.3)](#gl-5-3) :

<ul>

<li>

$f_1$ : $a=2$, $b=4$, $c=11$, donc $f_1=2(x_1+2x_2)^2+(11-8)\,x_2^2=2(x_1+2x_2)^2+3x_2^2$. Les deux coefficients sont positifs : une cuvette.

</li>

<li>

$f_2=(x_1+2x_2)^2+0\cdot x_2^2$ : une gouttière. Elle est nulle sur la droite $x_1+2x_2=0$, c’est-à-dire la droite de direction $(2,\,-1)^{\top}$.

</li>

<li>

$f_3=(x_1+2x_2)^2-3x_2^2$ : des signes différents, une selle. Si l’on choisit $x_2=1$ et $x_1=-2$, le premier carré s’annule : $f_3(-2,\,1)=4-8+1=-3<0$.

</li>

</ul>
:::
:::

:::aufgabe Exercice 16 ★★ Bobines couplées
<span class="anker" id="aufg-16"></span>

Deux bobines couplées ont $L_1=4\,\mathrm{mH}$ et $L_2=1\,\mathrm{mH}$.

<ol class="al">

<li>

Complétez le carré dans l’énergie $W=\tfrac12L_1i_1^2+M\,i_1i_2+\tfrac12L_2i_2^2$.

</li>

<li>

Pour quelles valeurs de $M$ a-t-on $W>0$ pour tous les courants $(i_1,\,i_2)\ne(0,\,0)$ ? Qu’en déduit-on pour le coefficient de couplage $k=M/\sqrt{L_1L_2}$ ?

</li>

</ol>

:::loesung
(a) Dans [(5.3)](#gl-5-3), on a $a=\tfrac12L_1$, $2b=M$ et $c=\tfrac12L_2$, donc $b/a=M/L_1$ et $b^2/a=M^2/(2L_1)$ :

$$W=\tfrac12L_1\Bigl(i_1+\frac M{L_1}\,i_2\Bigr)^2+\tfrac12\Bigl(L_2-\frac{M^2}{L_1}\Bigr)i_2^2=2\,\mathrm{mH}\,\Bigl(i_1+\frac M{4\,\mathrm{mH}}\,i_2\Bigr)^2+\Bigl(\frac12\,\mathrm{mH}-\frac{M^2}{8\,\mathrm{mH}}\Bigr)i_2^2 .$$

(b) Le premier coefficient est positif. On a $W>0$ pour tous les courants $\ne(0,\,0)$ si et seulement si le second l’est aussi : $L_2-M^2/L_1>0$, donc $M^2<L_1L_2=4\,(\mathrm{mH})^2$ et $|M|<2\,\mathrm{mH}$. Pour le coefficient de couplage, cela signifie $|k|=|M|/\sqrt{L_1L_2}<1$. Pour $|k|=1$, le couplage parfait, la forme ne serait qu’une gouttière : pour le rapport de courants adéquat $i_1=-\tfrac M{L_1}\,i_2$, l’énergie stockée serait nulle. Le fait que l’énergie d’un champ magnétique ne soit jamais négative impose donc $|k|\le1$.
:::
:::

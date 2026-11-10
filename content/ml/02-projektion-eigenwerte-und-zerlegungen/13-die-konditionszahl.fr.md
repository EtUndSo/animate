---
title: Le conditionnement
pfad: Informatique / Apprentissage automatique / Fondements mathématiques / Projection, valeurs propres et décompositions
adresse: informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen
knoten: Chapitre 2 : Projection, valeurs propres et décompositions
nachschlagen: ja
order: 15221300
summary: Les données de mesure ne sont jamais exactes, et un ordinateur arrondit à chaque étape.
tags: conditionnement
lang: fr
---

<span class="anker" id="stufe-12"></span>

:::zweck
Les données de mesure ne sont jamais exactes, et un ordinateur arrondit à chaque étape. De combien la solution d’un système d’équations change-t-elle lorsque le second membre est un peu faux ? Cette section montre qu’un seul nombre, tiré des valeurs singulières, donne la réponse, et ce qu’il signifie pour les équations normales.
:::

### Un système d’équations sensible

<span class="anker" id="stufe-12-1"></span>

Le système d’équations

$$x_1+x_2=2,\qquad x_1+1{,}01\,x_2=2{,}01$$

a pour solution $\mathbf{x}=(1,\,1)^{\top}$. Si l’on modifie de $0{,}01$ le second membre de la deuxième équation, pour le porter à $2{,}02$, la différence des équations donne $0{,}01\,x_2=0{,}02$, donc $x_2=2$ et $x_1=0$. Une modification des données au troisième chiffre déplace la solution d’une quantité égale à sa propre taille.

Géométriquement, les deux équations sont deux droites qui se coupent au point solution. Ici, elles sont presque parallèles ; elles se coupent sous un angle d’environ $0{,}29^\circ$ seulement. Si l’on déplace un peu l’une d’elles, le point d’intersection se déplace loin le long de l’autre (Fig. [28](#abb-28)). Si les droites sont au contraire perpendiculaires, il ne se déplace que d’autant que l’on déplace la droite.

:::abbildung ml/k2kondition 28
Le même déplacement de la droite rouge, d’une distance $0{,}2$ (en tirets), deux fois. À gauche, elle coupe la droite bleue à angle droit, et le point d’intersection se déplace de $0{,}2$. À droite, les droites se coupent sous un angle de $8^\circ$, et le point d’intersection se déplace de $0{,}2/\sin8^\circ\approx1{,}44$. Plus l’angle d’intersection est faible, plus la solution réagit fortement aux modifications des données.
:::

Quelle est l’ampleur de l’effet, rapportée aux grandeurs elles-mêmes ? Le second membre $\mathbf{y}=(2;\ 2{,}01)^{\top}$ a pour longueur $\sqrt{4+4{,}0401}\approx2{,}8355$ (Fig. [29](#abb-29)), la modification $\Delta\mathbf{y}=(0;\ 0{,}01)^{\top}$ a pour longueur $0{,}01$. Le second membre change donc, en valeur relative, de $0{,}01/2{,}8355\approx0{,}35\,\%$. La solution change de $\Delta\mathbf{x}=(-1,\,1)^{\top}$, soit, en valeur relative, de $\lVert\Delta\mathbf{x}\rVert/\lVert\mathbf{x}\rVert=\sqrt2/\sqrt2=100\,\%$. L’erreur relative est amplifiée environ $284$ fois.

:::abbildung ml/k2rnormy 29
Le carré de la longueur du second membre comme produit scalaire $\mathbf{y}^{\top}\mathbf{y}$ ; la longueur vaut $\sqrt{8{,}0401}\approx2{,}8355$.
:::

⁠**En bref :** Si les droites d’un système d’équations se coupent en étant presque parallèles, de petites modifications des données déplacent fortement la solution.

### Le conditionnement

<span class="anker" id="stufe-12-2"></span>

D’où vient ce facteur ? Avec la décomposition en valeurs singulières, on peut estimer précisément l’amplification.

:::definition Définition 12.1 (Conditionnement)
<span class="anker" id="satz-12-1"></span>

Soit $\mathbf{A}\in\mathbb{R}^{m\times n}$ à colonnes linéairement indépendantes, donc $d_n>0$. Le __conditionnement__ (ou nombre de conditionnement) de $\mathbf{A}$ est

<span class="anker" id="gl-12-1"></span>
$$\kappa(\mathbf{A})=\frac{d_1}{d_n}, \tag{12.1}$$

le rapport de l’étirement maximal à l’étirement minimal.
:::

On a toujours $\kappa(\mathbf{A})\ge1$. Une matrice orthogonale a $\kappa=1$, car toutes ses valeurs singulières valent $1$. Une matrice de grand conditionnement est dite mal conditionnée.

:::satz Théorème 12.2 (Amplification des erreurs)
<span class="anker" id="satz-12-2"></span>

Soit $\mathbf{A}\in\mathbb{R}^{n\times n}$ inversible, $\mathbf{A}\mathbf{x}=\mathbf{y}$ avec $\mathbf{y}\ne\mathbf{0}$ et $\mathbf{A}(\mathbf{x}+\Delta\mathbf{x})=\mathbf{y}+\Delta\mathbf{y}$. Alors

<span class="anker" id="gl-12-2"></span>
$$\frac{\lVert\Delta\mathbf{x}\rVert}{\lVert\mathbf{x}\rVert}\le\kappa(\mathbf{A})\,\frac{\lVert\Delta\mathbf{y}\rVert}{\lVert\mathbf{y}\rVert} . \tag{12.2}$$

Il y a égalité lorsque $\mathbf{y}$ pointe dans la direction de $\mathbf{u}_1$ et $\Delta\mathbf{y}$ dans la direction de $\mathbf{u}_n$.
:::

:::beweis Amplification des erreurs
Des deux équations, on déduit $\mathbf{A}\Delta\mathbf{x}=\Delta\mathbf{y}$. D’après [(9.5)](die-singularwertzerlegung.html#gl-9-5), $\lVert\mathbf{y}\rVert=\lVert\mathbf{A}\mathbf{x}\rVert\le d_1\lVert\mathbf{x}\rVert$, donc $1/\lVert\mathbf{x}\rVert\le d_1/\lVert\mathbf{y}\rVert$, et $\lVert\Delta\mathbf{y}\rVert=\lVert\mathbf{A}\Delta\mathbf{x}\rVert\ge d_n\lVert\Delta\mathbf{x}\rVert$, donc $\lVert\Delta\mathbf{x}\rVert\le\lVert\Delta\mathbf{y}\rVert/d_n$. En multipliant, on obtient [(12.2)](#gl-12-2). Si $\mathbf{y}$ pointe dans la direction de $\mathbf{u}_1$, $\mathbf{x}$ est un multiple de $\mathbf{v}_1$ et la première inégalité est une égalité ; si $\Delta\mathbf{y}$ pointe dans la direction de $\mathbf{u}_n$, $\Delta\mathbf{x}$ est un multiple de $\mathbf{v}_n$ et la seconde est une égalité.
:::

Le pire cas est donc le suivant : la solution est dans la direction que $\mathbf{A}$ étire le plus, de sorte que $\mathbf{y}$ est grand par rapport à $\mathbf{x}$, et l’erreur est dans la direction que $\mathbf{A}$ étire le moins, de sorte que le calcul en retour l’agrandit d’un facteur $1/d_n$.

::::beispiel [Exemple de calcul]
$\mathbf{A}=\bigl(\begin{smallmatrix}1&1\\1&1{,}01\end{smallmatrix}\bigr)$ est symétrique, de trace $2{,}01$ et de déterminant $0{,}01$. Ses valeurs propres sont

$$\lambda_{1,2}=\frac{2{,}01\pm\sqrt{2{,}01^2-0{,}04}}2=\frac{2{,}01\pm\sqrt{4{,}0001}}2\approx\frac{2{,}01\pm2{,}000025}2,$$

donc $\lambda_1\approx2{,}005012$ et $\lambda_2\approx0{,}004988$, toutes deux positives. D’après la section [9.7](die-singularwertzerlegung.html#stufe-9-7), ce sont aussi les valeurs singulières, et $\kappa(\mathbf{A})\approx402$. L’amplification observée, $284$, est inférieure. Elle n’atteint pas tout à fait la borne, car $\Delta\mathbf{y}=(0;\ 0{,}01)^{\top}$ ne pointe pas exactement dans la direction de $\mathbf{u}_2\approx(1,\,-1)^{\top}/\sqrt2$. Pour $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$, on a $\kappa=4/1=4$ : les erreurs relatives sont au plus multipliées par quatre.
::::

⁠**En bref :** Le conditionnement $\kappa(\mathbf{A})=d_1/d_n$ est le plus grand facteur par lequel $\mathbf{A}^{-1}$ peut agrandir, dans la solution, une erreur relative des données.

### Conditionnement et déterminant

<span class="anker" id="stufe-12-3"></span>

Dans l’encadré « Contexte » du [chapitre 1, section 14.6](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/die-determinante.html#stufe-14-6), figurait une mise en garde : un petit déterminant ne signifie pas qu’une matrice est presque singulière. Le conditionnement mesure ce que l’on voulait dire là-bas.

:::satz Théorème 12.3 (Distance à la matrice singulière la plus proche)
<span class="anker" id="satz-12-3"></span>

Pour une matrice inversible $\mathbf{A}\in\mathbb{R}^{n\times n}$, la plus petite distance $\lVert\mathbf{A}-\mathbf{B}\rVert_2$ à une matrice singulière $\mathbf{B}$ vaut $d_n$. Rapportée à la taille $\lVert\mathbf{A}\rVert_2=d_1$, elle vaut

<span class="anker" id="gl-12-3"></span>
$$\min_{\mathbf{B}\ \text{singulière}}\frac{\lVert\mathbf{A}-\mathbf{B}\rVert_2}{\lVert\mathbf{A}\rVert_2}=\frac1{\kappa(\mathbf{A})} . \tag{12.3}$$
:::

:::beweis Distance
Une matrice singulière est de rang au plus $n-1$. D’après le théorème d’Eckart-Young avec $k=n-1$, on a $\lVert\mathbf{A}-\mathbf{B}\rVert_2\ge d_n$, et la matrice singulière $\mathbf{A}_{n-1}$ est exactement à la distance $d_n$.
:::

Un grand conditionnement signifie donc qu’une modification relativement petite rend la matrice singulière. Le déterminant mesure autre chose. D’après l’exercice [29](die-singularwertzerlegung.html#aufg-29), $|\det\mathbf{A}|=d_1\cdots d_n$, le produit de tous les étirements ; il dépend de la taille de la matrice. Le conditionnement est un rapport et ne change pas lorsqu’on multiplie $\mathbf{A}$ par un nombre : $\kappa(c\mathbf{A})=\kappa(\mathbf{A})$ pour $c\ne0$. Il mesure seulement à quel point est aplatie l’ellipse en laquelle $\mathbf{A}$ transforme le cercle unité.

::::beispiel [Exemple de calcul]
Les deux matrices du [chapitre 1, section 14.6](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/die-determinante.html#stufe-14-6) : $0{,}1\cdot\mathbf{I}_{10}$ a pour déterminant $10^{-10}$, mais toutes ses valeurs singulières valent $0{,}1$, et $\kappa=1$ ; elle est aussi bien conditionnée que possible. $\operatorname{diag}(1000;\ 0{,}001)$ a pour déterminant $1$, mais $\kappa=1000/0{,}001=10^6$. Pour $\mathbf{A}=\bigl(\begin{smallmatrix}1&1\\1&1{,}01\end{smallmatrix}\bigr)$, la distance à la matrice singulière la plus proche vaut $d_2\approx0{,}005$ : si l’on modifie des coefficients de quelques millièmes, elle devient singulière. La matrice singulière $\bigl(\begin{smallmatrix}1&1\\1&1\end{smallmatrix}\bigr)$ est à la distance $\lVert\bigl(\begin{smallmatrix}0&0\\0&0{,}01\end{smallmatrix}\bigr)\rVert_2=0{,}01$, un peu plus que le minimum.
::::

⁠**En bref :** $1/\kappa(\mathbf{A})$ est la distance relative à la matrice singulière la plus proche ; le déterminant n’en dit rien, car il dépend de la taille de la matrice.

### Les équations normales élèvent le conditionnement au carré

<span class="anker" id="stufe-12-4"></span>

On peut calculer la meilleure solution approchée par les équations normales $\mathbf{A}^{\top}\mathbf{A}\hat{\mathbf{x}}=\mathbf{A}^{\top}\mathbf{y}$ ou par la décomposition QR, $\mathbf{R}\hat{\mathbf{x}}=\mathbf{Q}^{\top}\mathbf{y}$. Mathématiquement, les deux donnent le même résultat. Avec des nombres arrondis, non, et la raison en est le conditionnement.

:::satz Théorème 12.4 (Conditionnement de la matrice de Gram)
<span class="anker" id="satz-12-4"></span>

Si $\mathbf{A}$ a des colonnes linéairement indépendantes,

<span class="anker" id="gl-12-4"></span>
$$\kappa(\mathbf{A}^{\top}\mathbf{A})=\kappa(\mathbf{A})^2 . \tag{12.4}$$

Pour la décomposition QR $\mathbf{A}=\mathbf{Q}\mathbf{R}$, en revanche, $\kappa(\mathbf{R})=\kappa(\mathbf{A})$.
:::

:::beweis Matrice de Gram
$\mathbf{A}^{\top}\mathbf{A}$ est symétrique et définie positive, de valeurs propres $d_j^2$ ; d’après la section [9.7](die-singularwertzerlegung.html#stufe-9-7), ce sont aussi ses valeurs singulières, et leur rapport vaut $d_1^2/d_n^2$. Comme $\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}$, on a $\mathbf{R}^{\top}\mathbf{R}=\mathbf{R}^{\top}\mathbf{Q}^{\top}\mathbf{Q}\mathbf{R}=\mathbf{A}^{\top}\mathbf{A}$ ; $\mathbf{R}$ a donc les mêmes valeurs singulières que $\mathbf{A}$.
:::

::::beispiel [Exemple de calcul]
La matrice des appartements de la section [3.7](die-beste-naherungslosung.html#stufe-3-7), surface et nombre de pièces, a les valeurs singulières $d_1\approx135{,}02$ et $d_2\approx0{,}848$, donc $\kappa(\mathbf{A})\approx159{,}3$ et $\kappa(\mathbf{A}^{\top}\mathbf{A})\approx25\,367$. Deux causes rendent $\kappa(\mathbf{A})$ grand. Premièrement, les unités : les surfaces sont des nombres autour de $65$, les nombres de pièces autour de $2{,}5$. Si l’on mesure la surface en unités de $10\,\mathrm m^2$, le conditionnement descend à environ $18{,}5$. Deuxièmement, les deux colonnes pointent presque dans la même direction : elles ne forment qu’un angle d’environ $8{,}9^\circ$. C’est pourquoi, même si l’on ramène les deux colonnes à la longueur $1$, il reste $\kappa\approx12{,}8$. Le changement d’unités ne modifie pas les valeurs ajustées $\hat{\mathbf{y}}$ : si l’on divise une colonne par $10$, le poids correspondant devient $10$ fois plus grand, et les produits restent les mêmes.
::::

⁠**En bref :** Les équations normales travaillent avec $\kappa(\mathbf{A})^2$, la décomposition QR avec $\kappa(\mathbf{A})$ ; des unités bien choisies abaissent le conditionnement.

:::hintergrund Ce que l’ordinateur fait du conditionnement
Un ordinateur stocke habituellement les nombres avec environ $16$ chiffres décimaux significatifs et arrondit après chaque opération. Une bonne méthode fournit la solution exacte d’un problème dont les données ne sont modifiées que de l’ordre de grandeur de cet arrondi ; de telles méthodes sont dites stables au sens rétrograde (*backward stable*). D’après [(12.2)](#gl-12-2), le résultat a alors une erreur relative d’au plus environ $\kappa\cdot10^{-16}$ : on perd à peu près $\log_{10}\kappa$ des $16$ chiffres.

La voie de la décomposition QR (et celle de la décomposition en valeurs singulières) est stable au sens rétrograde ; lorsque le résidu est petit, son erreur croît à peu près comme $\kappa(\mathbf{A})$. La voie des équations normales ne l’est pas : elle travaille avec la matrice $\mathbf{A}^{\top}\mathbf{A}$, et son erreur croît toujours comme $\kappa(\mathbf{A})^2$, même lorsque le résidu est petit. Pour $\kappa(\mathbf{A})=10^6$, on perd par cette voie environ $12$ des $16$ chiffres, avec QR environ $6$. Pour les appartements, avec $\kappa(\mathbf{A})^2\approx2{,}5\cdot10^4$, c’est encore anodin ; pour de grands jeux de données aux caractéristiques presque dépendantes, non. C’est pourquoi les bons programmes calculent la meilleure solution approchée par QR ou par la décomposition en valeurs singulières, et non par les équations normales, bien que celles-ci décrivent la théorie de la façon la plus concise.
:::

:::aufgabe Exercice 36 ★ Lire des conditionnements
<span class="anker" id="aufg-36"></span>

Déterminez le conditionnement

<ol class="al">

<li>

de $\operatorname{diag}(2;\ 0{,}5)$ et de $\operatorname{diag}(-3;\ 3)$ ;

</li>

<li>

de la matrice de rotation d’angle $30^\circ$ ;

</li>

<li>

de $5\mathbf{A}$ pour $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$. Comparez les déterminants de $\mathbf{A}$ et de $5\mathbf{A}$.

</li>

</ol>

:::loesung
(a) $\operatorname{diag}(2;\,0{,}5)$ a les valeurs singulières $2$ et $0{,}5$, donc $\kappa=4$. D’après la section [9.7](die-singularwertzerlegung.html#stufe-9-7), $\operatorname{diag}(-3;\,3)$ a les valeurs singulières $3$ et $3$, donc $\kappa=1$, bien que les valeurs propres soient de signes contraires.

(b) Une matrice de rotation est orthogonale ; toutes ses valeurs singulières valent $1$ : $\kappa=1$.

(c) $5\mathbf{A}$ a les valeurs singulières $20$ et $5$, donc de nouveau $\kappa=4$. Le déterminant, en revanche, passe de $4$ à $\det(5\mathbf{A})=25\cdot4=100$.
:::
:::

:::aufgabe Exercice 37 ★★ Déterminant 1, et pourtant mal conditionnée
<span class="anker" id="aufg-37"></span>

Soit $\mathbf{A}=\bigl(\begin{smallmatrix}10&7\\7&5\end{smallmatrix}\bigr)$.

<ol class="al">

<li>

Calculez $\det\mathbf{A}$ et $\mathbf{A}^{-1}$. Résolvez $\mathbf{A}\mathbf{x}=(17,\,12)^{\top}$ et $\mathbf{A}\mathbf{x}=(17;\ 12{,}1)^{\top}$.

</li>

<li>

Calculez les variations relatives de $\mathbf{y}$ et de $\mathbf{x}$ ainsi que leur rapport.

</li>

<li>

Calculez $\kappa(\mathbf{A})$ et vérifiez [(12.2)](#gl-12-2). À quelle distance $\mathbf{A}$ se trouve-t-elle de la matrice singulière la plus proche ?

</li>

</ol>

:::loesung
(a) $\det\mathbf{A}=50-49=1$ et $\mathbf{A}^{-1}=\bigl(\begin{smallmatrix}5&-7\\-7&10\end{smallmatrix}\bigr)$. On a donc $\mathbf{A}^{-1}(17,\,12)^{\top}=(85-84,\ -119+120)^{\top}=(1,\,1)^{\top}$ et $\mathbf{A}^{-1}(17;\ 12{,}1)^{\top}=(85-84{,}7;\ -119+121)^{\top}=(0{,}3;\ 2)^{\top}$.

(b) $\lVert\Delta\mathbf{y}\rVert/\lVert\mathbf{y}\rVert=0{,}1/\sqrt{433}\approx0{,}1/20{,}809\approx0{,}48\,\%$. $\Delta\mathbf{x}=(-0{,}7;\ 1)^{\top}$, donc $\lVert\Delta\mathbf{x}\rVert/\lVert\mathbf{x}\rVert=\sqrt{1{,}49}/\sqrt2\approx1{,}2207/1{,}4142\approx86{,}3\,\%$. Le rapport vaut environ $180$.

(c) $\mathbf{A}$ est symétrique, de trace $15$ et de déterminant $1$, donc $\lambda=\tfrac{15\pm\sqrt{221}}2\approx14{,}933$ et $0{,}0670$, toutes deux positives. D’après la section [9.7](die-singularwertzerlegung.html#stufe-9-7), ce sont les valeurs singulières, et $\kappa(\mathbf{A})\approx14{,}933/0{,}0670\approx223$. La borne [(12.2)](#gl-12-2) est respectée : $86{,}3\,\%\le223\cdot0{,}48\,\%\approx107\,\%$. La distance à la matrice singulière la plus proche vaut $d_2\approx0{,}067$, soit $1/223$ en valeur relative. Le déterminant $1$ n’en révèle rien.
:::
:::

:::aufgabe Exercice 38 ★★★ Règles de calcul pour le conditionnement
<span class="anker" id="aufg-38"></span>

Soit $\mathbf{A}\in\mathbb{R}^{n\times n}$ inversible et $\mathbf{Q}$ orthogonale. Montrez que :

<ol class="al">

<li>

$\kappa(\mathbf{Q}\mathbf{A})=\kappa(\mathbf{A})$ et $\kappa(\mathbf{A}^{-1})=\kappa(\mathbf{A})$ ;

</li>

<li>

pour toutes les valeurs propres $\lambda$ et $\mu$ de $\mathbf{A}$, on a $|\lambda|/|\mu|\le\kappa(\mathbf{A})$ ;

</li>

<li>

pour $\mathbf{A}$ symétrique, $\kappa(\mathbf{A})=|\lambda|_{\max}/|\lambda|_{\min}$, le rapport de la valeur propre de plus grande valeur absolue à celle de plus petite valeur absolue.

</li>

</ol>

:::loesung
(a) D’après l’exercice [29](die-singularwertzerlegung.html#aufg-29), $\mathbf{Q}\mathbf{A}$ a les mêmes valeurs singulières que $\mathbf{A}$, donc le même conditionnement. De $\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$, on déduit $\mathbf{A}^{-1}=\mathbf{V}\mathbf{D}^{-1}\mathbf{U}^{\top}$, une décomposition en valeurs singulières dont les valeurs singulières sont les $1/d_j$. La plus grande est $1/d_n$, la plus petite $1/d_1$, donc $\kappa(\mathbf{A}^{-1})=\tfrac{1/d_n}{1/d_1}=\tfrac{d_1}{d_n}=\kappa(\mathbf{A})$.

(b) Pour un vecteur propre $\mathbf{v}$ associé à $\lambda$, [(9.5)](die-singularwertzerlegung.html#gl-9-5) donne $d_n\lVert\mathbf{v}\rVert\le\lVert\mathbf{A}\mathbf{v}\rVert=|\lambda|\,\lVert\mathbf{v}\rVert\le d_1\lVert\mathbf{v}\rVert$, donc $d_n\le|\lambda|\le d_1$ ; cela vaut aussi pour les vecteurs propres complexes, comme l’a montré la section [9.8](die-singularwertzerlegung.html#stufe-9-8). Il en va de même pour $\mu$. Donc $|\lambda|/|\mu|\le d_1/d_n$.

(c) Pour $\mathbf{A}$ symétrique, les valeurs singulières sont, d’après la section [9.7](die-singularwertzerlegung.html#stufe-9-7), les valeurs absolues $|\lambda_i|$. La plus grande valeur singulière est donc $|\lambda|_{\max}$, la plus petite $|\lambda|_{\min}$.
:::
:::

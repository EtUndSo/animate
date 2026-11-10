---
title: La matrice jacobienne
pfad: Informatique / Apprentissage automatique / Fondements mathématiques / Dérivée, gradient et règle de dérivation en chaîne
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Chapitre 3 : Dérivée, gradient et règle de dérivation en chaîne
nachschlagen: ja
order: 15230600
summary: Beaucoup d’opérations de calcul ne fournissent pas un nombre, mais plusieurs : un produit matrice-vecteur transforme un vecteur en un autre.
tags: à valeurs vectorielles, matrice jacobienne
lang: fr
---

<span class="anker" id="stufe-5"></span>

:::zweck
Beaucoup d’opérations de calcul ne fournissent pas un nombre, mais plusieurs : un produit matrice-vecteur transforme un vecteur en un autre. Pour de telles fonctions, la matrice jacobienne rassemble les dérivées partielles de toutes les sorties par rapport à toutes les entrées. C’est la matrice de l’approximation linéaire, et pour les deux briques les plus fréquentes, les applications linéaires et les fonctions appliquées terme à terme, elle a une forme particulièrement simple.
:::

### Fonctions à plusieurs sorties

<span class="anker" id="stufe-5-1"></span>

Dans le [chapitre 1, section 8](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/lineare-abbildungen.html#stufe-8), une application linéaire $\mathbf{x}\mapsto\mathbf{A}\mathbf{x}$ envoyait des vecteurs de $\mathbb{R}^n$ sur des vecteurs de $\mathbb{R}^m$, et dans le [chapitre 1, section 15.2](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/elementweise-rechnen-und-tensoren.html#stufe-15-2), une fonction était appliquée séparément à chaque composante d’un vecteur. Dans les deux cas, un vecteur produit plusieurs nombres. Chacun d’eux est à lui seul une fonction de plusieurs variables.

:::definition Définition 5.1 (Fonction à valeurs vectorielles)
<span class="anker" id="satz-5-1"></span>

Une fonction $\mathbf{g}:\mathbb{R}^n\to\mathbb{R}^m$ qui associe à chaque $\mathbf{x}\in\mathbb{R}^n$ un vecteur

$$\mathbf{g}(\mathbf{x})=\begin{pmatrix}g_1(\mathbf{x})\\ \vdots\\ g_m(\mathbf{x})\end{pmatrix}\in\mathbb{R}^m$$

est dite __à valeurs vectorielles__. Les fonctions $g_1,\dots,g_m:\mathbb{R}^n\to\mathbb{R}$ s’appellent ses composantes.
:::

Dans ce chapitre, les fonctions à valeurs vectorielles s’écrivent en gras, comme les vecteurs ; les fonctions dont la valeur est un nombre s’écrivent en maigre.

::::beispiel [Exemple de calcul]
Tout au long des sections [5](#stufe-5) et [6](die-kettenregel-fur-mehrere-variablen.html#stufe-6), nous utiliserons la fonction $\mathbf{g}:\mathbb{R}^2\to\mathbb{R}^2$ définie par

<span class="anker" id="gl-5-1"></span>
$$\mathbf{g}(\mathbf{x})=\begin{pmatrix}x_1x_2\\ 2x_1+x_2^2\end{pmatrix},\qquad \mathbf{g}(1,2)=\begin{pmatrix}2\\6\end{pmatrix}. \tag{5.1}$$

Ses composantes sont $g_1(\mathbf{x})=x_1x_2$ et $g_2(\mathbf{x})=2x_1+x_2^2$.
::::

⁠**En bref :** Une fonction à valeurs vectorielles $\mathbf{g}:\mathbb{R}^n\to\mathbb{R}^m$ se compose de $m$ fonctions de $n$ variables, une pour chaque sortie.

### La matrice jacobienne

<span class="anker" id="stufe-5-2"></span>

Chaque composante $g_i$ a $n$ dérivées partielles, une par rapport à chaque entrée. Cela fait en tout $m\cdot n$ nombres. On les range dans un tableau avec une ligne par sortie et une colonne par entrée.

:::definition Définition 5.2 (Matrice jacobienne)
<span class="anker" id="satz-5-2"></span>

Si toutes les dérivées partielles des composantes de $\mathbf{g}:\mathbb{R}^n\to\mathbb{R}^m$ existent au point $\mathbf{x}$, la matrice de taille $m\times n$

<span class="anker" id="gl-5-2"></span>
$$\mathbf{J}_{\mathbf{g}}(\mathbf{x})=\begin{pmatrix}\dfrac{\partial g_1}{\partial x_1}&\cdots&\dfrac{\partial g_1}{\partial x_n}\\ \vdots&&\vdots\\ \dfrac{\partial g_m}{\partial x_1}&\cdots&\dfrac{\partial g_m}{\partial x_n}\end{pmatrix},\qquad \bigl(\mathbf{J}_{\mathbf{g}}(\mathbf{x})\bigr)_{ij}=\frac{\partial g_i}{\partial x_j}(\mathbf{x}), \tag{5.2}$$

s’appelle la __matrice jacobienne__ de $\mathbf{g}$ au point $\mathbf{x}$.
:::

La ligne $i$ correspond à la sortie $g_i$ ; c’est son gradient, écrit en ligne : $\nabla g_i(\mathbf{x})^{\top}$. La colonne $j$ correspond à l’entrée $x_j$ ; elle indique comment toutes les sorties réagissent à la fois lorsqu’on ne modifie que $x_j$. Pour une fonction $f:\mathbb{R}^n\to\mathbb{R}$ à une seule sortie, la matrice jacobienne est une matrice de taille $1\times n$, à savoir le gradient écrit en ligne : $\mathbf{J}_f(\mathbf{x})=\nabla f(\mathbf{x})^{\top}$. La matrice porte le nom du mathématicien Carl Gustav Jacob Jacobi.

::::beispiel [Exemple de calcul]
Pour $\mathbf{g}$ de [(5.1)](#gl-5-1), on a

$$\mathbf{J}_{\mathbf{g}}(\mathbf{x})=\begin{pmatrix}x_2&x_1\\2&2x_2\end{pmatrix},\qquad \mathbf{J}_{\mathbf{g}}(1,2)=\begin{pmatrix}2&1\\2&4\end{pmatrix}.$$

La première colonne $(2,\,2)^{\top}$ dit : si $x_1$ augmente d’un petit $h$, les deux sorties augmentent d’environ $2h$. La deuxième colonne $(1,\,4)^{\top}$ dit : si $x_2$ augmente, la deuxième sortie réagit quatre fois plus fortement que la première.
::::

⁠**En bref :** La matrice jacobienne a une ligne par sortie et une colonne par entrée ; son coefficient $(i,j)$ est $\partial g_i/\partial x_j$.

### L’approximation linéaire avec la matrice jacobienne

<span class="anker" id="stufe-5-3"></span>

Chaque composante a son approximation linéaire [(3.4)](partielle-ableitungen-und-der-gradient.html#gl-3-4). Si l’on écrit les $m$ approximations les unes sous les autres, on trouve à gauche les composantes de $\mathbf{g}(\mathbf{x}+\mathbf{h})$ et à droite les lignes de la matrice jacobienne multipliées par $\mathbf{h}$. D’après la vue par lignes du [chapitre 1, section 7.2](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrix-vektor-produkt.html#stufe-7-2), c’est un produit matrice-vecteur.

:::satz Théorème 5.3 (Approximation linéaire d’une fonction à valeurs vectorielles)
<span class="anker" id="satz-5-3"></span>

Si chaque composante de $\mathbf{g}$ est différentiable au point $\mathbf{x}$, alors

<span class="anker" id="gl-5-3"></span>
$$\mathbf{g}(\mathbf{x}+\mathbf{h})=\mathbf{g}(\mathbf{x})+\mathbf{J}_{\mathbf{g}}(\mathbf{x})\,\mathbf{h}+\mathbf{r}(\mathbf{h})\qquad\text{avec}\qquad\lim_{\mathbf{h}\to\mathbf{0}}\frac{\lVert\mathbf{r}(\mathbf{h})\rVert}{\lVert\mathbf{h}\rVert}=0 . \tag{5.3}$$
:::

:::beweis Approximation linéaire d’une fonction à valeurs vectorielles
La composante $i$ de $\mathbf{J}_{\mathbf{g}}(\mathbf{x})\,\mathbf{h}$ est $\nabla g_i(\mathbf{x})^{\top}\mathbf{h}$. D’après la définition de la différentiabilité [(3.5)](partielle-ableitungen-und-der-gradient.html#gl-3-5), le quotient $r_i(\mathbf{h})/\lVert\mathbf{h}\rVert$ tend vers $0$ pour tout $i$. Comme $\lVert\mathbf{r}\rVert\le|r_1|+\dots+|r_m|$, le quotient $\lVert\mathbf{r}(\mathbf{h})\rVert/\lVert\mathbf{h}\rVert$ tend lui aussi vers $0$.
:::

Au voisinage de $\mathbf{x}$, $\mathbf{g}$ agit donc comme l’application linéaire $\mathbf{h}\mapsto\mathbf{J}_{\mathbf{g}}(\mathbf{x})\,\mathbf{h}$, et d’après le [chapitre 1, section 8.2](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/lineare-abbildungen.html#stufe-8-2), à toute application linéaire correspond exactement une matrice. La matrice jacobienne est cette matrice. Sous la loupe, $\mathbf{g}$ déforme un petit quadrillage autour de $\mathbf{x}$ de la même façon que la matrice $\mathbf{J}_{\mathbf{g}}(\mathbf{x})$ déforme le quadrillage unité : il est tourné, étiré ou cisaillé, mais les lignes droites restent presque droites.

::::beispiel [Exemple de calcul]
Pour $\mathbf{g}$ de [(5.1)](#gl-5-1) au point $(1,\,2)$ et $\mathbf{h}=(0{,}1;\ -0{,}1)^{\top}$, on a

$$\mathbf{J}_{\mathbf{g}}(1,2)\,\mathbf{h}=\begin{pmatrix}2\cdot0{,}1+1\cdot(-0{,}1)\\2\cdot0{,}1+4\cdot(-0{,}1)\end{pmatrix}=\begin{pmatrix}0{,}1\\-0{,}2\end{pmatrix}, \qquad \mathbf{g}(1{,}1;\ 1{,}9)\approx\begin{pmatrix}2{,}1\\5{,}8\end{pmatrix}.$$

La valeur exacte est $\mathbf{g}(1{,}1;\ 1{,}9)=(2{,}09;\ 5{,}81)^{\top}$. La Fig. [10](#abb-10) montre le produit ligne par ligne.

:::abbildung ml/k3rjacobi 10
La variation de l’approximation linéaire de $\mathbf{g}$ au point $\mathbf{x}=(1,\,2)^{\top}$ comme produit matrice-vecteur : chaque ligne est le produit scalaire du gradient d’une sortie et du déplacement.
:::
::::

⁠**En bref :** Près de $\mathbf{x}$, on a $\mathbf{g}(\mathbf{x}+\mathbf{h})\approx\mathbf{g}(\mathbf{x})+\mathbf{J}_{\mathbf{g}}(\mathbf{x})\,\mathbf{h}$ ; la matrice jacobienne est la matrice de l’application linéaire à laquelle $\mathbf{g}$ se ramène à petite échelle.

### Deux matrices jacobiennes importantes

<span class="anker" id="stufe-5-4"></span>

Deux briques reviennent sans cesse dans les calculs sur des données : le produit matrice-vecteur et les fonctions que l’on applique séparément à chaque composante. On a besoin de leurs matrices jacobiennes encore et encore, et toutes deux s’écrivent sans calcul.

:::satz Théorème 5.4 (Matrices jacobiennes des briques)
<span class="anker" id="satz-5-4"></span>

<ol class="al">

<li>

Pour $\mathbf{g}(\mathbf{x})=\mathbf{A}\mathbf{x}+\mathbf{b}$ avec $\mathbf{A}\in\mathbb{R}^{m\times n}$ et $\mathbf{b}\in\mathbb{R}^m$, on a $\mathbf{J}_{\mathbf{g}}(\mathbf{x})=\mathbf{A}$ en tout point.

</li>

<li>

Si $\mathbf{g}:\mathbb{R}^n\to\mathbb{R}^n$ applique une fonction dérivable $\varphi$ d’une variable à chaque composante, $g_i(\mathbf{x})=\varphi(x_i)$, alors

<span class="anker" id="gl-5-4"></span>
$$\mathbf{J}_{\mathbf{g}}(\mathbf{x})=\operatorname{diag}\bigl(\varphi'(x_1),\,\dots,\,\varphi'(x_n)\bigr). \tag{5.4}$$

</li>

</ol>
:::

:::beweis Matrices jacobiennes des briques
(a) La composante $i$ est $g_i(\mathbf{x})=\sum_ka_{ik}x_k+b_i$. Quand on dérive par rapport à $x_j$, il ne reste que le terme avec $k=j$, donc $\partial g_i/\partial x_j=a_{ij}$. (b) La composante $g_i=\varphi(x_i)$ ne dépend que de $x_i$. Sa dérivée par rapport à $x_j$ est donc $0$ pour $j\ne i$ et $\varphi'(x_i)$ pour $j=i$.
:::

Les deux résultats ont une raison simple. Une application affine est déjà linéaire, à la translation $\mathbf{b}$ près ; sa meilleure approximation linéaire est elle-même, sans $\mathbf{b}$. Pour une fonction appliquée terme à terme, chaque entrée n’agit que sur sa propre sortie ; tous les coefficients hors de la diagonale sont nuls, parce qu’il n’y a pas de liaison entre des composantes différentes.

::::beispiel [Exemple de calcul]
Pour $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\0&-1\\3&1\end{smallmatrix}\bigr)$, la matrice jacobienne de $\mathbf{x}\mapsto\mathbf{A}\mathbf{x}$ est partout $\mathbf{A}$ elle-même. Si l’on élève chaque composante au carré, $\varphi(t)=t^2$, la matrice jacobienne au point $\mathbf{x}=(1,\,-2,\,3)^{\top}$ est $\operatorname{diag}(2;\,-4;\,6)$. Si l’on applique la fonction logistique à chaque composante de $\mathbf{x}=(0,\,2)^{\top}$, la matrice jacobienne vaut, d’après [(2.4)](die-kettenregel.html#gl-2-4), $\operatorname{diag}\bigl(\sigma'(0);\,\sigma'(2)\bigr)\approx\operatorname{diag}(0{,}25;\ 0{,}105)$.
::::

⁠**En bref :** La matrice jacobienne de $\mathbf{x}\mapsto\mathbf{A}\mathbf{x}+\mathbf{b}$ est $\mathbf{A}$ ; celle d’une fonction appliquée terme à terme est la matrice diagonale des dérivées individuelles.

:::hintergrund Le déterminant de la matrice jacobienne comme facteur d’aire
D’après le [chapitre 1, section 14.3](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/die-determinante.html#stufe-14-3), une application linéaire multiplie l’aire de toute figure par le même facteur $|\det\mathbf{A}|$. Comme $\mathbf{g}$ agit à petite échelle comme $\mathbf{J}_{\mathbf{g}}(\mathbf{x})$, cela vaut approximativement aussi pour $\mathbf{g}$ : un petit carré autour de $\mathbf{x}$, d’aire $F$, se transforme en une figure qui est presque un parallélogramme d’aire $|\det\mathbf{J}_{\mathbf{g}}(\mathbf{x})|\cdot F$. Pour $\mathbf{g}$ de [(5.1)](#gl-5-1), on a $\det\mathbf{J}_{\mathbf{g}}(1,2)=2\cdot4-1\cdot2=6$ : au voisinage de $(1,\,2)$, $\mathbf{g}$ multiplie les aires par six environ. Un exemple connu est celui des coordonnées polaires, $\mathbf{g}(r,\varphi)=(r\cos\varphi,\ r\sin\varphi)^{\top}$. Leur matrice jacobienne a pour colonnes $(\cos\varphi,\,\sin\varphi)^{\top}$ et $(-r\sin\varphi,\,r\cos\varphi)^{\top}$ et pour déterminant $r\cos^2\varphi+r\sin^2\varphi=r$. Un petit rectangle de côtés $\Delta r$ et $\Delta\varphi$ devient un morceau de couronne d’aire environ $r\,\Delta r\,\Delta\varphi$, car l’arc d’angle $\Delta\varphi$ à la distance $r$ a pour longueur $r\,\Delta\varphi$.
:::

:::aufgabe Exercice 17 ★ Calculer des matrices jacobiennes
<span class="anker" id="aufg-17"></span>

Calculez la matrice jacobienne au point indiqué.

<ol class="al">

<li>

$\mathbf{g}(\mathbf{x})=(x_1+x_2,\ x_1-x_2,\ x_1x_2)^{\top}$ au point $(3,\,1)$ ;

</li>

<li>

$\mathbf{g}(\mathbf{x})=(\mathrm{e}^{x_1},\,\mathrm{e}^{x_2},\,\mathrm{e}^{x_3})^{\top}$ au point $(0,\,1,\,-1)$ ;

</li>

<li>

$f(\mathbf{x})=x_1^2x_2+x_2^2$ de [(3.1)](partielle-ableitungen-und-der-gradient.html#gl-3-1) au point $(1,\,2)$. Quelle forme a la matrice, et à quoi correspond-elle ?

</li>

</ol>

:::loesung
(a) La matrice jacobienne a trois lignes et deux colonnes :

$$\mathbf{J}_{\mathbf{g}}(\mathbf{x})=\begin{pmatrix}1&1\\1&-1\\x_2&x_1\end{pmatrix},\qquad \mathbf{J}_{\mathbf{g}}(3,1)=\begin{pmatrix}1&1\\1&-1\\1&3\end{pmatrix}.$$

(b) La fonction agit terme à terme ; d’après [(5.4)](#gl-5-4), $\mathbf{J}=\operatorname{diag}(\mathrm{e}^0;\,\mathrm{e}^1;\,\mathrm{e}^{-1})\approx\operatorname{diag}(1;\ 2{,}718;\ 0{,}368)$.

(c) Une fonction à une seule sortie a une matrice jacobienne $1\times2$, le gradient sous forme de ligne : $\mathbf{J}_f(1,2)=(4\ \ 5)=\nabla f(1,2)^{\top}$.
:::
:::

:::aufgabe Exercice 18 ★★ Approximation linéaire d’une application du plan
<span class="anker" id="aufg-18"></span>

Soit $\mathbf{g}(\mathbf{x})=(x_1^2-x_2,\ x_1x_2)^{\top}$.

<ol class="al">

<li>

Calculez $\mathbf{J}_{\mathbf{g}}(2,1)$ et, à l’aide de celle-ci, une valeur approchée de $\mathbf{g}(2{,}05;\ 0{,}9)$. Comparez avec la valeur exacte.

</li>

<li>

Comment faut-il déplacer les entrées pour que la première sortie change, mais que la seconde, en approximation linéaire, ne change pas du tout ? Donnez un tel déplacement $\mathbf{h}$.

</li>

</ol>

:::loesung
(a) $\mathbf{J}_{\mathbf{g}}(\mathbf{x})=\bigl(\begin{smallmatrix}2x_1&-1\\x_2&x_1\end{smallmatrix}\bigr)$, donc $\mathbf{J}_{\mathbf{g}}(2,1)=\bigl(\begin{smallmatrix}4&-1\\1&2\end{smallmatrix}\bigr)$, et $\mathbf{g}(2,1)=(3,\,2)^{\top}$. Avec $\mathbf{h}=(0{,}05;\ -0{,}1)^{\top}$, on a

$$\mathbf{J}_{\mathbf{g}}\mathbf{h}=\begin{pmatrix}0{,}2+0{,}1\\0{,}05-0{,}2\end{pmatrix}=\begin{pmatrix}0{,}3\\-0{,}15\end{pmatrix},\qquad \mathbf{g}(2{,}05;\ 0{,}9)\approx\begin{pmatrix}3{,}3\\1{,}85\end{pmatrix}.$$

La valeur exacte est $\mathbf{g}(2{,}05;\ 0{,}9)=(4{,}2025-0{,}9;\ 1{,}845)^{\top}=(3{,}3025;\ 1{,}845)^{\top}$.

(b) En approximation linéaire, la seconde sortie varie de $h_1+2h_2$ ; c’est nul pour $\mathbf{h}$ dans la direction $(2,\,-1)^{\top}$. Pour un pas égal exactement à ce vecteur, la première sortie varie alors de $4\cdot2-1\cdot(-1)=9$. Les deux entrées doivent donc changer : $x_1$ augmente, $x_2$ diminue deux fois moins, par exemple $\mathbf{h}=(0{,}02;\ -0{,}01)^{\top}$, avec l’effet $(0{,}09;\ 0)^{\top}$.
:::
:::

:::aufgabe Exercice 19 ★★★ De combien $\mathbf{g}$ agrandit les aires
<span class="anker" id="aufg-19"></span>

Soit $\mathbf{g}$ comme dans [(5.1)](#gl-5-1).

<ol class="al">

<li>

Calculez les images des quatre sommets du carré de sommets $(1,\,2)$, $(1{,}1;\ 2)$, $(1{,}1;\ 2{,}1)$ et $(1;\ 2{,}1)$.

</li>

<li>

Les images forment presque un parallélogramme. Estimez son aire à l’aide des images des deux côtés qui partent de $\mathbf{g}(1,2)$, et comparez avec $|\det\mathbf{J}_{\mathbf{g}}(1,2)|\cdot0{,}01$.

</li>

</ol>

:::loesung
(a) Avec $\mathbf{g}(\mathbf{x})=(x_1x_2,\ 2x_1+x_2^2)^{\top}$ :

$$\mathbf{g}(1,2)=\begin{pmatrix}2\\6\end{pmatrix},\quad \mathbf{g}(1{,}1;\,2)=\begin{pmatrix}2{,}2\\6{,}2\end{pmatrix},\quad \mathbf{g}(1{,}1;\,2{,}1)=\begin{pmatrix}2{,}31\\6{,}61\end{pmatrix},\quad \mathbf{g}(1;\,2{,}1)=\begin{pmatrix}2{,}1\\6{,}41\end{pmatrix}.$$

(b) Les images des deux côtés qui partent de $\mathbf{g}(1,2)$ sont $(0{,}2;\ 0{,}2)^{\top}$ et $(0{,}1;\ 0{,}41)^{\top}$. D’après le [chapitre 1, section 14.1](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/die-determinante.html#stufe-14-1), le parallélogramme qu’elles engendrent a pour aire $|0{,}2\cdot0{,}41-0{,}1\cdot0{,}2|=0{,}062$. La matrice jacobienne prédit $|\det\mathbf{J}_{\mathbf{g}}(1,2)|\cdot0{,}01=6\cdot0{,}01=0{,}06$. L’écart vient de ce que le carré n’est pas arbitrairement petit ; le quatrième sommet, en $(2{,}31;\ 6{,}61)$, ne se trouve d’ailleurs que presque là où un vrai parallélogramme l’aurait, en $(2{,}3;\ 6{,}61)$.
:::
:::

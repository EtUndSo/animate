---
title: Systèmes d’équations linéaires
pfad: Informatique / Apprentissage automatique / Fondements mathématiques / Vecteurs et matrices
adresse: informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen
knoten: Chapitre 1 : Vecteurs et matrices
nachschlagen: ja
order: 15211300
summary: Jusqu’ici, l’entrée x était donnée et la sortie Ax était cherchée.
tags: système d’équations linéaires, matrice des coefficients, second membre, solution, matrice augmentée, méthode du pivot de Gauss, forme échelonnée, homogène
lang: fr
---

<span class="anker" id="stufe-12"></span>

:::zweck
Jusqu’ici, l’entrée $\mathbf{x}$ était donnée et la sortie $\mathbf{A}\mathbf{x}$ était cherchée. Cette section pose la question inverse : quelle entrée fournit une sortie donnée ? C’est un système d’équations linéaires. Elle montre comment le résoudre et quand il n’a aucune solution, exactement une ou une infinité.
:::

### Les systèmes d’équations sous forme matricielle

<span class="anker" id="stufe-12-1"></span>

On connaît depuis l’école des problèmes comme celui-ci : deux nombres $x_1$ et $x_2$ vérifient $2x_1+x_2=5$ et $x_1+x_2=3$ ; quels sont-ils ? Les membres de gauche sont les composantes d’un produit matrice-vecteur. Le problème demande donc : quel vecteur $\mathbf{x}$ la matrice $\bigl(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\bigr)$ envoie-t-elle sur $(5,\,3)^{\top}$ ?

:::definition Définition 12.1 (Système d’équations linéaires)
<span class="anker" id="satz-12-1"></span>

Pour une matrice $\mathbf{A}\in\mathbb{R}^{m\times n}$ et un vecteur $\mathbf{y}\in\mathbb{R}^m$,

<span class="anker" id="gl-12-1"></span>
$$\mathbf{A}\mathbf{x}=\mathbf{y} \tag{12.1}$$

s’appelle un __système d’équations linéaires__ à $m$ équations et aux $n$ inconnues $x_1,\dots,x_n$. La matrice $\mathbf{A}$ s’appelle la __matrice des coefficients__, le vecteur $\mathbf{y}$ le __second membre__. Tout vecteur $\mathbf{x}\in\mathbb{R}^n$ qui vérifie [(12.1)](#gl-12-1) s’appelle une __solution__.
:::

Écrite en détail, la ligne $i$ contient l’équation $a_{i1}x_1+\dots+a_{in}x_n=y_i$.

::::beispiel [Exemple de calcul]
Le système

$$\begin{pmatrix}2&1\\1&1\end{pmatrix}\begin{pmatrix}x_1\\x_2\end{pmatrix}=\begin{pmatrix}5\\3\end{pmatrix}$$

a pour solution $\mathbf{x}=(2,\,1)^{\top}$ : $2\cdot2+1=5$ et $2+1=3$. La matrice des coefficients est connue depuis la sous-section [11.2](einheitsmatrix-und-inverse.html#stufe-11-2), avec l’inverse $\bigl(\begin{smallmatrix}1&-1\\-1&2\end{smallmatrix}\bigr)$. Si l’on multiplie le système à gauche par celle-ci, la solution apparaît immédiatement : $\mathbf{x}=\mathbf{A}^{-1}\mathbf{y}=(5-3,\ -5+6)^{\top}=(2,\,1)^{\top}$.
::::

⁠**En bref :** Un système d’équations linéaires $\mathbf{A}\mathbf{x}=\mathbf{y}$ demande quelle entrée $\mathbf{x}$ fournit la sortie $\mathbf{y}$.

### Image en lignes et image en colonnes

<span class="anker" id="stufe-12-2"></span>

Comme pour le produit matrice-vecteur, il existe deux façons de lire un système d’équations.

**Image en lignes.** Chaque équation, prise isolément, décrit un ensemble de points. Avec deux inconnues, $2x_1+x_2=5$ est une droite du plan, de même que $x_1+x_2=3$. Une solution doit vérifier les deux équations, donc se trouver sur les deux droites : c’est leur point d’intersection (Fig. [38](#abb-38), à gauche). Avec trois inconnues, chaque équation est un plan de l’espace.

**Image en colonnes.** D’après la vue par colonnes [(7.3)](das-matrix-vektor-produkt.html#gl-7-3), on a $\mathbf{A}\mathbf{x}=x_1\mathbf{a}_1+\dots+x_n\mathbf{a}_n$. L’équation demande donc : avec quels coefficients la combinaison linéaire des colonnes donne-t-elle le second membre ? Dans l’exemple : $x_1\,(2,\,1)^{\top}+x_2\,(1,\,1)^{\top}=(5,\,3)^{\top}$, résolu par $x_1=2$ et $x_2=1$. C’est exactement la partie droite de la Fig. [30](das-matrix-vektor-produkt.html#abb-30).

:::abbildung ml/k1lgs 38
L’image en lignes de trois systèmes d’équations à deux inconnues. Chaque équation est une droite, une solution se trouve sur toutes les droites. (a) Les droites se coupent en un point. (b) Les droites sont parallèles et n’ont aucun point commun. (c) Les deux équations décrivent la même droite, et chacun de ses points est une solution.
:::

L’image en colonnes indique immédiatement quand il existe une solution. Les vecteurs $\mathbf{A}\mathbf{x}$ forment l’espace des colonnes (sous-section [7.4](das-matrix-vektor-produkt.html#stufe-7-4)).

:::satz Théorème 12.2 (Existence de solutions)
<span class="anker" id="satz-12-2"></span>

Le système $\mathbf{A}\mathbf{x}=\mathbf{y}$ a une solution si et seulement si $\mathbf{y}$ appartient à l’espace des colonnes de $\mathbf{A}$.
:::

::::beispiel [Exemple de calcul]
Le système $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)\mathbf{x}=\mathbf{y}$ a une solution pour $\mathbf{y}=(3,\,6)^{\top}$, par exemple $\mathbf{x}=(1,\,1)^{\top}$, mais pas pour $\mathbf{y}=(1,\,1)^{\top}$ : d’après la sous-section [7.4](das-matrix-vektor-produkt.html#stufe-7-4), l’espace des colonnes n’est que la droite dirigée par $(1,\,2)^{\top}$.
::::

⁠**En bref :** Dans l’image en lignes, une solution est un point commun à toutes les équations ; dans l’image en colonnes, c’est le choix des coefficients avec lequel les colonnes donnent le second membre.

### La méthode du pivot de Gauss

<span class="anker" id="stufe-12-3"></span>

Avec deux inconnues, on trouve la solution à vue d’œil. Avec trois ou plus, il faut une méthode qui fonctionne toujours. L’idée est la même qu’à l’école : on soustrait un multiple d’une équation d’une autre, de sorte qu’une inconnue disparaisse. On répète cela jusqu’à ce que la dernière équation ne contienne plus qu’une inconnue.

Pour cela, on n’écrit que les nombres : la matrice des coefficients et, séparé par un trait, le second membre. Ce tableau s’appelle la __matrice augmentée__ $(\mathbf{A}\,|\,\mathbf{y})$.

:::definition Définition 12.3 (Méthode du pivot de Gauss)
<span class="anker" id="satz-12-3"></span>

La __méthode du pivot de Gauss__ transforme la matrice augmentée à l’aide de trois opérations sur les lignes :

<ol>

<li>

ajouter à une ligne un multiple d’une autre ligne ;

</li>

<li>

échanger deux lignes ;

</li>

<li>

multiplier une ligne par un nombre non nul.

</li>

</ol>

Le but est la __forme échelonnée__ : dans chaque ligne, le premier coefficient non nul est précédé d’au moins un zéro de plus que dans la ligne du dessus. On détermine ensuite les inconnues de bas en haut (remontée).
:::

:::satz Théorème 12.4 (Les opérations sur les lignes ne changent pas les solutions)
<span class="anker" id="satz-12-4"></span>

Un système et le système obtenu à partir de lui par des opérations sur les lignes ont les mêmes solutions.
:::

:::beweis Opérations sur les lignes
Toute solution de l’ancien système vérifie aussi les nouvelles équations, car celles-ci sont des sommes et des multiples des anciennes. Mais chacune des trois opérations peut aussi être annulée : retrancher de nouveau le multiple, rééchanger les lignes, diviser par le nombre. Donc, inversement, toute solution du nouveau système vérifie aussi l’ancien.
:::

::::beispiel [Exemple de calcul]
Le système

$$\begin{aligned} x_1+2x_2+x_3&=8\\ 2x_1+x_2+x_3&=7\\ x_1+x_2+2x_3&=9 \end{aligned} \qquad\text{a pour matrice augmentée}\qquad \left(\begin{array}{ccc|c}1&2&1&8\\2&1&1&7\\1&1&2&9\end{array}\right).$$

Si l’on soustrait deux fois la première ligne de la deuxième et une fois de la troisième, $x_1$ disparaît des deux. Si l’on échange ensuite les nouvelles deuxième et troisième lignes et que l’on soustrait trois fois la nouvelle deuxième de la troisième, $x_2$ disparaît aussi de la dernière ligne :

$$\left(\begin{array}{ccc|c}1&2&1&8\\0&-3&-1&-9\\0&-1&1&1\end{array}\right) \;\longrightarrow\; \left(\begin{array}{ccc|c}1&2&1&8\\0&-1&1&1\\0&-3&-1&-9\end{array}\right) \;\longrightarrow\; \left(\begin{array}{ccc|c}1&2&1&8\\0&-1&1&1\\0&0&-4&-12\end{array}\right).$$

De bas en haut : $-4x_3=-12$, donc $x_3=3$ ; puis $-x_2+3=1$, donc $x_2=2$ ; puis $x_1+4+3=8$, donc $x_1=1$. La solution est $\mathbf{x}=(1,\,2,\,3)^{\top}$, et la substitution dans les trois équations la confirme.
::::

⁠**En bref :** La méthode du pivot de Gauss élimine les inconnues pas à pas par des opérations sur les lignes, qui ne changent pas les solutions, puis substitue de bas en haut.

:::hintergrund Pourquoi on ne calcule pas d’inverse pour résoudre un système
Si $\mathbf{A}$ est inversible, la solution est $\mathbf{x}=\mathbf{A}^{-1}\mathbf{y}$. C’est utile pour raisonner, mais peu commode comme méthode de calcul. La méthode du pivot de Gauss demande, pour un système de $n$ équations à $n$ inconnues, environ $\tfrac23n^3$ opérations élémentaires ; calculer l’inverse coûte environ $2n^3$, trois fois plus, et il faut encore y ajouter le produit $\mathbf{A}^{-1}\mathbf{y}$. De plus, un ordinateur calcule avec un nombre fini de chiffres. L’inverse ne peut alors être représentée qu’arrondie, et l’élimination directe fournit en général des résultats plus précis. L’inverse est donc avant tout un outil pour réfléchir et démontrer, pas pour calculer.
:::

### Aucune, une ou une infinité de solutions

<span class="anker" id="stufe-12-4"></span>

Deux droites du plan se coupent en un point, sont parallèles ou sont confondues (Fig. [38](#abb-38)). Elles ne peuvent pas avoir exactement deux points d’intersection. Il en va de même pour tout système d’équations linéaires, quelle que soit sa taille.

:::satz Théorème 12.5 (Nombre de solutions)
<span class="anker" id="satz-12-5"></span>

Un système d’équations linéaires n’a aucune solution, ou exactement une solution, ou une infinité de solutions.
:::

:::beweis Nombre de solutions
Il suffit de montrer que si le système a deux solutions distinctes $\mathbf{x}\ne\mathbf{x}'$, il en a une infinité. Pour tout nombre $t$, on a

$$\mathbf{A}\bigl(\mathbf{x}+t\,(\mathbf{x}'-\mathbf{x})\bigr)=\mathbf{A}\mathbf{x}+t\,(\mathbf{A}\mathbf{x}'-\mathbf{A}\mathbf{x})=\mathbf{y}+t\,(\mathbf{y}-\mathbf{y})=\mathbf{y} ,$$

donc chaque point $\mathbf{x}+t\,(\mathbf{x}'-\mathbf{x})$ de la droite passant par $\mathbf{x}$ et $\mathbf{x}'$ est une solution, et des valeurs différentes de $t$ donnent des points différents.
:::

Le système $\mathbf{A}\mathbf{x}=\mathbf{0}$, de second membre nul, est dit __homogène__. Il a toujours la solution $\mathbf{x}=\mathbf{0}$. Si l’on connaît une seule solution $\mathbf{x}_{\mathrm s}$ du système $\mathbf{A}\mathbf{x}=\mathbf{y}$, on obtient toutes les autres en lui ajoutant les solutions du système homogène : $\mathbf{A}\mathbf{x}=\mathbf{y}$ est vérifié si et seulement si $\mathbf{A}(\mathbf{x}-\mathbf{x}_{\mathrm s})=\mathbf{y}-\mathbf{y}=\mathbf{0}$.

::::beispiel [Exemple de calcul]
Les trois systèmes de la Fig. [38](#abb-38) :

<ol class="al">

<li>

$2x_1+x_2=5$, $x_1+x_2=3$ : exactement une solution, $(2,\,1)^{\top}$.

</li>

<li>

$x_1+x_2=3$, $x_1+x_2=1$ : aucune solution, car la même somme ne peut pas valoir à la fois $3$ et $1$.

</li>

<li>

$x_1+x_2=3$, $2x_1+2x_2=6$ : la deuxième équation est le double de la première. Une solution est $\mathbf{x}_{\mathrm s}=(3,\,0)^{\top}$, et le système homogène $x_1+x_2=0$ est résolu par tous les multiples de $(-1,\,1)^{\top}$. Toutes les solutions sont donc $\mathbf{x}=(3,\,0)^{\top}+t\,(-1,\,1)^{\top}$, avec $t$ quelconque.

</li>

</ol>
::::

⁠**En bref :** Un système d’équations linéaires n’a aucune solution, exactement une ou une infinité ; toutes les solutions sont une solution plus les solutions du système homogène.

### Plus d’équations que d’inconnues

<span class="anker" id="stufe-12-5"></span>

Avec des données, la situation est souvent déséquilibrée. Supposons que l’on cherche des poids $w_1$ pour la surface et $w_2$ pour les pièces, de sorte que la somme pondérée donne exactement le prix réel de trois appartements. Cela fait trois équations pour deux inconnues.

:::definition Définition 12.6 (Surdéterminé, sous-déterminé)
<span class="anker" id="satz-12-6"></span>

Un système d’équations linéaires qui a plus d’équations que d’inconnues ($m>n$) est dit __surdéterminé__, un système qui a moins d’équations que d’inconnues ($m<n$) __sous-déterminé__.
:::

Un système surdéterminé n’a le plus souvent aucune solution : deux équations fixent déjà deux inconnues, et la troisième équation devrait, par hasard, être vérifiée elle aussi. Dans l’image en colonnes : pour $n<m$, l’espace des colonnes de $n$ colonnes dans $\mathbb{R}^m$ n’est qu’une petite partie de $\mathbb{R}^m$, et le second membre ne s’y trouve presque jamais. Un système sous-déterminé, en revanche, a une infinité de solutions s’il en a au moins une : dans la forme échelonnée, au moins une inconnue reste sans pivot propre, et elle peut être choisie librement.

::::beispiel [Exemple de calcul]
Pour les appartements 1 à 3, dont les prix sont $200$, $130$ et $290$ mille euros, le système s’écrit

$$60\,w_1+2\,w_2=200,\qquad 40\,w_1+w_2=130,\qquad 90\,w_1+4\,w_2=290 .$$

Des deux premières équations, on tire $w_1=3$ et $w_2=10$ : si l’on soustrait deux fois la deuxième de la première, il reste $-20\,w_1=-60$. Substitué dans la troisième, cela donne toutefois $270+40=310\ne290$. Le système n’a pas de solution. Aucune paire de poids ne donne exactement les trois prix. Ce que l’on cherche à la place dans un tel cas est une question à part.
::::

⁠**En bref :** Un système surdéterminé a plus d’équations que d’inconnues et n’a le plus souvent aucune solution ; un système sous-déterminé en a moins et, s’il a une solution, il en a une infinité.

:::aufgabe Exercice 28 ★★ La méthode du pivot de Gauss
<span class="anker" id="aufg-28"></span>

Résolvez par la méthode du pivot de Gauss et faites la vérification :

$$x_1+x_2+x_3=6,\qquad 2x_1+3x_2+x_3=11,\qquad x_1-x_2+2x_3=5 .$$

:::loesung
La matrice augmentée est $\Bigl(\begin{smallmatrix}1&1&1&|&6\\2&3&1&|&11\\1&-1&2&|&5\end{smallmatrix}\Bigr)$. Si l’on soustrait deux fois la première ligne de la deuxième et une fois de la troisième, on obtient les lignes $(0,\,1,\,-1\,|\,-1)$ et $(0,\,-2,\,1\,|\,-1)$. Si l’on ajoute ensuite deux fois la nouvelle deuxième ligne à la troisième, celle-ci devient $(0,\,0,\,-1\,|\,-3)$. La forme échelonnée s’écrit

$$x_1+x_2+x_3=6,\qquad x_2-x_3=-1,\qquad -x_3=-3 .$$

De bas en haut : $x_3=3$, $x_2=-1+3=2$, $x_1=6-2-3=1$. Vérification : $1+2+3=6$, $2+6+3=11$, $1-2+6=5$. La solution est $\mathbf{x}=(1,\,2,\,3)^{\top}$.
:::
:::

:::aufgabe Exercice 29 ★★ Combien de solutions ?
<span class="anker" id="aufg-29"></span>

Déterminez pour chaque système l’ensemble des solutions et dessinez l’image en lignes :

<ol class="al">

<li>

$x_1+2x_2=3$, $2x_1+4x_2=6$ ;

</li>

<li>

$x_1+2x_2=3$, $2x_1+4x_2=5$ ;

</li>

<li>

$x_1+2x_2=3$, $x_1-x_2=0$.

</li>

</ol>

:::loesung
(a) La deuxième équation est le double de la première ; toutes deux décrivent la même droite. Une infinité de solutions : avec $x_2=t$, on a $x_1=3-2t$, donc $\mathbf{x}=(3,\,0)^{\top}+t\,(-2,\,1)^{\top}$.

(b) En doublant la première équation, on obtient $2x_1+4x_2=6$, ce qui contredit $2x_1+4x_2=5$. Les droites sont parallèles ; il n’y a aucune solution.

(c) D’après la deuxième équation, $x_1=x_2$ ; en substituant dans la première, on obtient $3x_2=3$. Exactement une solution : $\mathbf{x}=(1,\,1)^{\top}$, le point d’intersection de deux droites non parallèles.
:::
:::

:::aufgabe Exercice 30 ★★ Des poids qui conviennent
<span class="anker" id="aufg-30"></span>

Ajoutez au système surdéterminé de la sous-section [12.5](#stufe-12-5) l’appartement 4, dont le prix est de $240$ mille euros.

<ol class="al">

<li>

Pour lesquels des quatre appartements le prix est-il atteint exactement avec $w_1=3$, $w_2=10$ ?

</li>

<li>

Écrivez le système à quatre équations sous la forme $\mathbf{A}\mathbf{w}=\mathbf{y}$. Quelles sont les tailles de $\mathbf{A}$, $\mathbf{w}$ et $\mathbf{y}$ ? Que signifie « aucune solution » dans l’image en colonnes ?

</li>

</ol>

:::loesung
(a) Avec $w_1=3$, $w_2=10$ : appartement 1 : $180+20=200$ (atteint), appartement 2 : $120+10=130$ (atteint), appartement 3 : $270+40=310$ au lieu de $290$ (non atteint), appartement 4 : $210+30=240$ (atteint). Trois des quatre prix sont justes, mais pas tous.

(b) $\mathbf{A}=\Biggl(\begin{smallmatrix}60&2\\40&1\\90&4\\70&3\end{smallmatrix}\Biggr)\in\mathbb{R}^{4\times2}$, $\mathbf{w}\in\mathbb{R}^2$, $\mathbf{y}=(200,\,130,\,290,\,240)^{\top}\in\mathbb{R}^4$. L’espace des colonnes de $\mathbf{A}$ se compose de toutes les combinaisons $w_1\mathbf{a}_1+w_2\mathbf{a}_2$ de la colonne des surfaces et de la colonne des pièces ; c’est un plan passant par l’origine dans $\mathbb{R}^4$. « Aucune solution » signifie : le vecteur des prix $\mathbf{y}$ ne se trouve pas dans ce plan. Aucun choix des deux poids ne produit exactement ces quatre prix.
:::
:::

---
title: Le déterminant
pfad: Informatique / Apprentissage automatique / Fondements mathématiques / Vecteurs et matrices
knoten: Fondements 1 : Vecteurs et matrices
nachschlagen: ja
order: 15211500
summary: Une application linéaire déforme le quadrillage du plan, et les aires s’agrandissent ou rétrécissent.
tags: déterminant, orientation, développement de Laplace
lang: fr
---

<span class="anker" id="stufe-14"></span>

:::zweck
Une application linéaire déforme le quadrillage du plan, et les aires s’agrandissent ou rétrécissent. Cette section détermine le facteur dont elles changent. Ce facteur est un seul nombre, le déterminant, et il permet aussi de reconnaître si une matrice est inversible.
:::

### Le déterminant d’une matrice $2\times2$

<span class="anker" id="stufe-14-1"></span>

Le carré unité a pour aire $1$. Une matrice $\mathbf{A}$ l’envoie sur le parallélogramme construit sur ses deux colonnes (sous-section [8.3](lineare-abbildungen.html#stufe-8-3)). Quelle est l’aire de ce parallélogramme ? La figure [40](#abb-40) la montre pour $\mathbf{A}=\bigl(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\bigr)$.

:::abbildung ml/k1det 40
À gauche, le carré unité d’aire $1$ ; à droite, son image par $\mathbf{A}=\bigl(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\bigr)$ : le parallélogramme construit sur les colonnes $\mathbf{a}_1$ et $\mathbf{a}_2$. Il a pour aire $5=3\cdot2-1\cdot1$. En pointillé, le rectangle qui l’entoure et à partir duquel on peut calculer l’aire.
:::

:::herleitung L’aire du parallélogramme
Soient $\mathbf{a}_1=(a,\,c)^{\top}$ et $\mathbf{a}_2=(b,\,d)^{\top}$ les colonnes, avec des nombres tous positifs, et supposons que $\mathbf{a}_2$ se trouve en haut à gauche de $\mathbf{a}_1$, comme dans la Fig. [40](#abb-40). Le parallélogramme de sommets $\mathbf{0}$, $\mathbf{a}_1$, $\mathbf{a}_1+\mathbf{a}_2$, $\mathbf{a}_2$ tient dans le rectangle de côtés $a+b$ et $c+d$. Pour ne garder que lui, on découpe dans le rectangle deux triangles rectangles de côtés de l’angle droit $a$ et $c$, deux triangles rectangles de côtés de l’angle droit $b$ et $d$ et deux rectangles de côtés $b$ et $c$ :

$$(a+b)(c+d)-2\cdot\tfrac12ac-2\cdot\tfrac12bd-2\,bc=ac+ad+bc+bd-ac-bd-2bc=ad-bc .$$

Pour $\mathbf{A}=\bigl(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\bigr)$ : $4\cdot3-3-2-2=5$.
:::

:::definition Définition 14.1 (Déterminant d’une matrice $2\times2$)
<span class="anker" id="satz-14-1"></span>

Le __déterminant__ de la matrice $\mathbf{A}=\bigl(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\bigr)$ est le nombre

<span class="anker" id="gl-14-1"></span>
$$\det\mathbf{A}=ad-bc . \tag{14.1}$$
:::

Sa valeur absolue est l’aire du parallélogramme construit sur les colonnes, c’est-à-dire le facteur dont $\mathbf{A}$ change l’aire du carré unité. C’est le même nombre que celui qui figure au dénominateur de l’inverse [(11.2)](einheitsmatrix-und-inverse.html#gl-11-2).

⁠**Exemple de calcul :** $\det\bigl(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\bigr)=6-1=5$, $\det\bigl(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\bigr)=2-1=1$, $\det\operatorname{diag}(2;\,0{,}5)=1$ et $\det\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)=0$. L’étirement change la forme du carré, mais pas son aire : ce qu’il gagne en largeur, il le perd en hauteur.

⁠**En bref :** Le déterminant $ad-bc$ d’une matrice $2\times2$ est, en valeur absolue, le facteur dont l’application change l’aire du carré unité.

### Le signe du déterminant

<span class="anker" id="stufe-14-2"></span>

Une aire n’est jamais négative, le déterminant peut l’être. Son signe porte une information supplémentaire : il indique si l’application retourne le plan, comme un miroir.

Dans le carré unité, $\mathbf{e}_2$ se trouve, vu de $\mathbf{e}_1$, dans le sens inverse des aiguilles d’une montre. Si cela reste ainsi pour les images, c’est-à-dire si $\mathbf{a}_2$ se trouve lui aussi, vu de $\mathbf{a}_1$, dans le sens inverse des aiguilles d’une montre, alors $\det\mathbf{A}>0$. Si $\mathbf{a}_2$ se trouve dans le sens des aiguilles d’une montre par rapport à $\mathbf{a}_1$, le plan a été retourné, et $\det\mathbf{A}<0$. Cette propriété s’appelle l’__orientation__ : un déterminant positif conserve l’orientation, un déterminant négatif l’inverse.

⁠**Exemple de calcul :** La réflexion par rapport à l’axe des $x_1$, $\operatorname{diag}(1;\,-1)$, a pour déterminant $-1$ : l’aire reste la même, l’orientation s’inverse. Si l’on échange les colonnes d’une matrice, le déterminant change de signe : $\det\bigl(\begin{smallmatrix}1&3\\2&1\end{smallmatrix}\bigr)=1-6=-5$. La rotation de $90^\circ$ a $\det=0\cdot0-(-1)\cdot1=1$, le cisaillement $\det=1\cdot1-1\cdot0=1$, l’aplatissement $\operatorname{diag}(1;\,0)$ le déterminant $0$.

⁠**En bref :** La valeur absolue du déterminant est le facteur d’aire, son signe indique si l’application retourne le plan.

### Le facteur d’aire vaut pour toute figure

<span class="anker" id="stufe-14-3"></span>

Jusqu’ici, il s’agissait du carré unité. Mais une application linéaire traite chaque endroit du plan de la même façon, et c’est pourquoi elle change l’aire de toute figure du même facteur.

:::satz Théorème 14.2 (Facteur d’aire)
<span class="anker" id="satz-14-2"></span>

Si $\mathbf{A}\in\mathbb{R}^{2\times2}$ transforme une figure d’aire $F$, l’image a pour aire $|\det\mathbf{A}|\cdot F$.
:::

:::herleitung Facteur d’aire
On pose sur la figure un quadrillage fin de petits carrés de côté $h$. Un carré de coin $\mathbf{q}$ a pour sommets $\mathbf{q}$, $\mathbf{q}+h\mathbf{e}_1$, $\mathbf{q}+h\mathbf{e}_1+h\mathbf{e}_2$ et $\mathbf{q}+h\mathbf{e}_2$. Son image a pour sommets $\mathbf{A}\mathbf{q}$, $\mathbf{A}\mathbf{q}+h\mathbf{a}_1$, $\mathbf{A}\mathbf{q}+h\mathbf{a}_1+h\mathbf{a}_2$ et $\mathbf{A}\mathbf{q}+h\mathbf{a}_2$ : c’est le parallélogramme construit sur $h\mathbf{a}_1$ et $h\mathbf{a}_2$, translaté en $\mathbf{A}\mathbf{q}$. Son aire est $h^2\,|\det\mathbf{A}|$, quel que soit l’endroit où se trouvait le carré. Chaque petit carré est donc agrandi ou réduit du même facteur $|\det\mathbf{A}|$. La figure se compose approximativement de tels carrés, et ce d’autant plus exactement que le quadrillage est fin. C’est pourquoi le facteur vaut pour la figure entière.
:::

⁠**Exemple de calcul :** Le disque de rayon $1$ a pour aire $\pi$. L’étirement $\operatorname{diag}(3;\,2)$ en fait une ellipse de demi-axes $3$ et $2$. Son aire est $\pi\cdot3\cdot2=6\pi$, soit exactement $|\det\mathbf{A}|=6$ fois l’aire du disque. Le triangle de sommets $\mathbf{0}$, $\mathbf{e}_1$, $\mathbf{e}_2$ a pour aire $\tfrac12$ ; par $\bigl(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\bigr)$, il devient le triangle de sommets $\mathbf{0}$, $(3,1)^{\top}$, $(1,2)^{\top}$, d’aire $\tfrac52$.

⁠**En bref :** Une application linéaire change l’aire de toute figure du même facteur $|\det\mathbf{A}|$, parce qu’elle traite de la même façon chaque petite case du quadrillage.

### Déterminants de matrices plus grandes

<span class="anker" id="stufe-14-4"></span>

Dans l’espace, le cube unité devient le parallélépipède construit sur les trois colonnes de la matrice, un pavé droit déformé en biais. Son volume est le facteur dont l’application change les volumes. Pour des matrices plus grandes aussi, il existe un tel nombre. On le calcule en le ramenant à des déterminants de matrices plus petites.

:::definition Définition 14.3 (Déterminant)
<span class="anker" id="satz-14-3"></span>

Pour $\mathbf{A}\in\mathbb{R}^{1\times1}$, on pose $\det\mathbf{A}=a_{11}$. Pour $\mathbf{A}\in\mathbb{R}^{n\times n}$ avec $n\ge2$, on pose

<span class="anker" id="gl-14-2"></span>
$$\det\mathbf{A}=\sum_{j=1}^n(-1)^{1+j}\,a_{1j}\,\det\mathbf{A}_{1j} , \tag{14.2}$$

où $\mathbf{A}_{1j}$ est la matrice $(n-1)\times(n-1)$ obtenue à partir de $\mathbf{A}$ en supprimant la première ligne et la colonne $j$. Cette règle de calcul s’appelle le __développement de Laplace__ selon la première ligne.
:::

Pour $n=2$, [(14.2)](#gl-14-2) redonne $a_{11}a_{22}-a_{12}a_{21}$. On peut tout aussi bien développer selon n’importe quelle autre ligne ou colonne, avec le signe $(-1)^{i+j}$ pour le coefficient $a_{ij}$ ; le résultat est toujours le même. Pour $n=3$, $|\det\mathbf{A}|$ est le volume du parallélépipède construit sur les trois colonnes, et le signe indique si les colonnes sont disposées dans le même sens de rotation que $\mathbf{e}_1,\mathbf{e}_2,\mathbf{e}_3$ (règle de la main droite) ou en miroir.

⁠**Exemple de calcul :** Pour la matrice des coefficients de la sous-section [12.3](lineare-gleichungssysteme.html#stufe-12-3),

$$\mathbf{A}=\begin{pmatrix}1&2&1\\2&1&1\\1&1&2\end{pmatrix},$$

le développement de Laplace selon la première ligne donne $\det\mathbf{A}=-4$ (Fig. [41](#abb-41)).

:::abbildung ml/k1rlaplace 41
Le développement de Laplace selon la première ligne : chaque coefficient de la première ligne fois le déterminant de la matrice restante, sans sa ligne ni sa colonne, avec des signes alternés.
:::

Pour une matrice triangulaire supérieure, sous la diagonale de laquelle ne figurent que des zéros, on développe à chaque fois selon la première colonne et l’on obtient le produit des coefficients diagonaux, par exemple $\det\Bigl(\begin{smallmatrix}2&1&3\\0&3&1\\0&0&4\end{smallmatrix}\Bigr)=2\cdot3\cdot4=24$.

⁠**En bref :** Le développement de Laplace ramène le déterminant d’une matrice $n\times n$ à des déterminants plus petits ; sa valeur absolue est le facteur dont l’application change les volumes.

### Règles de calcul pour les déterminants

<span class="anker" id="stufe-14-5"></span>

La règle la plus importante découle directement de l’intuition. Si l’on effectue deux applications l’une après l’autre, la première change le volume de son facteur, et la seconde change encore le résultat du sien. Les facteurs se multiplient.

:::satz Théorème 14.4 (Règles de calcul du déterminant)
<span class="anker" id="satz-14-4"></span>

Pour $\mathbf{A},\mathbf{B}\in\mathbb{R}^{n\times n}$ et un nombre $c$, on a :

<ol class="rm">

<li>

$\det(\mathbf{A}\mathbf{B})=\det\mathbf{A}\cdot\det\mathbf{B}$ ;

</li>

<li>

$\det\mathbf{A}^{\top}=\det\mathbf{A}$ ;

</li>

<li>

$\det\mathbf{A}^{-1}=1/\det\mathbf{A}$, si $\mathbf{A}$ est inversible ;

</li>

<li>

$\det(c\,\mathbf{A})=c^n\det\mathbf{A}$ ;

</li>

<li>

si l’on ajoute à une ligne un multiple d’une autre, le déterminant ne change pas ; si l’on échange deux lignes, il change de signe ; si l’on multiplie une ligne par $c$, il est multiplié par $c$.

</li>

</ol>
:::

La règle (iii) découle de (i) avec $\mathbf{A}\mathbf{A}^{-1}=\mathbf{I}$ et $\det\mathbf{I}=1$. La règle (iv) dit : si l’on étire les $n$ arêtes du cube unité d’un facteur $c$, son volume est multiplié par $c^n$. La règle (v) fait de la méthode du pivot de Gauss la voie pratique pour calculer des déterminants : on met la matrice sous forme échelonnée, on retient le nombre d’échanges et l’on multiplie les coefficients diagonaux.

⁠**Exemple de calcul 1 :** Avec $\det\bigl(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\bigr)=1$ et $\det\bigl(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\bigr)=5$, le produit $\bigl(\begin{smallmatrix}7&4\\4&3\end{smallmatrix}\bigr)$ doit avoir pour déterminant $5$ : $21-16=5$.

⁠**Exemple de calcul 2 :** Dans la méthode du pivot de Gauss de la sous-section [12.3](lineare-gleichungssysteme.html#stufe-12-3), la matrice des coefficients a été mise, par des additions de multiples et un échange, sous la forme échelonnée de diagonale $1$, $-1$, $-4$. Son déterminant vaut donc $(-1)\cdot\bigl(1\cdot(-1)\cdot(-4)\bigr)=-4$, comme avec le développement de Laplace.

⁠**En bref :** Le déterminant d’un produit est le produit des déterminants, parce que les facteurs de volume se multiplient lors de la composition ; en pratique, on le calcule avec la méthode du pivot de Gauss.

:::hintergrund Pourquoi les opérations sur les lignes changent le déterminant précisément ainsi
D’après la règle (ii), on peut tout aussi bien transformer les colonnes au lieu des lignes, et c’est sur les colonnes que sont construits le parallélogramme ou le parallélépipède. Si l’on ajoute à une colonne un multiple d’une autre, par exemple $\mathbf{a}_2\to\mathbf{a}_2+t\,\mathbf{a}_1$, le côté opposé à $\mathbf{a}_1$ glisse parallèlement à $\mathbf{a}_1$. Le parallélogramme est cisaillé comme un paquet de cartes que l’on pousse sur le côté. La base et la hauteur restent les mêmes, donc l’aire aussi. Dans l’espace, il en va de même pour le parallélépipède : chaque section parallèle à la base n’est que déplacée, pas modifiée, et des solides dont les sections ont la même aire à chaque hauteur ont le même volume (principe de Cavalieri). Si l’on échange deux colonnes, l’aire reste la même, mais le sens de rotation de la première vers la deuxième colonne s’inverse, et avec lui le signe. Si l’on multiplie une colonne par $c$, une arête devient $c$ fois plus longue et le volume $c$ fois plus grand. Pour les matrices $2\times2$, la formule $ad-bc$ le confirme directement, par exemple pour le cisaillement : $a\,(d+t\,c)-(b+t\,a)\,c=ad-bc$.

Inversement, trois propriétés suffisent déjà à déterminer entièrement le déterminant : $\det\mathbf{I}=1$ ; si l’on échange deux lignes, le signe change ; et si l’on fixe toutes les lignes sauf une, le déterminant est linéaire par rapport à cette ligne. Toute fonction de la matrice possédant ces trois propriétés est le déterminant. La raison en est la méthode du pivot de Gauss : elle ramène toute matrice carrée, par des opérations sur les lignes, à $\mathbf{I}$ ou à une matrice ayant une ligne nulle, et l’effet de chaque opération est fixé par les trois propriétés. C’est pourquoi de nombreux manuels définissent le déterminant par ces propriétés et en déduisent le développement de Laplace.
:::

:::hintergrund Pourquoi on ne calcule pas les déterminants par le développement de Laplace
Le développement de Laplace d’une matrice $n\times n$ fait appel à $n$ déterminants de taille $n-1$, chacun d’eux à $n-1$ déterminants de taille $n-2$, et ainsi de suite. Écrit en entier, cela donne $n!$ produits. Pour $n=20$, cela fait plus de $2\cdot10^{18}$, hors de portée d’un ordinateur. La méthode du pivot de Gauss, en revanche, ne demande qu’environ $\tfrac23n^3$ opérations élémentaires, soit, pour $n=20$, quelques milliers. Le développement de Laplace est donc une définition et un outil pour les petites matrices et les démonstrations, pas une méthode de calcul.
:::

### Déterminant et inversibilité

<span class="anker" id="stufe-14-6"></span>

Si le déterminant est nul, le carré unité devient une figure d’aire nulle, c’est-à-dire un segment ou un point. L’application aplatit le plan, et ce qui est aplati ne peut pas être reconstitué.

:::satz Théorème 14.5 (Déterminant et inversibilité)
<span class="anker" id="satz-14-5"></span>

Une matrice carrée $\mathbf{A}$ est inversible si et seulement si $\det\mathbf{A}\ne0$.
:::

:::beweis Déterminant et inversibilité
Si $\mathbf{A}$ est inversible, alors, d’après la règle (i), $\det\mathbf{A}\cdot\det\mathbf{A}^{-1}=\det\mathbf{I}=1$, donc $\det\mathbf{A}\ne0$. Si, inversement, $\det\mathbf{A}\ne0$, on met $\mathbf{A}$ sous forme échelonnée par la méthode du pivot de Gauss. D’après la règle (v), le déterminant n’est alors modifié que par des facteurs non nuls ; le déterminant de la forme échelonnée n’est donc pas nul non plus. C’est le produit de ses coefficients diagonaux, donc aucun d’eux n’est nul, et il y a $n$ pivots. Ainsi $\operatorname{rg}\mathbf{A}=n$, et d’après le théorème de la sous-section [13.5](unabhangigkeit-basis-und-rang.html#stufe-13-5), $\mathbf{A}$ est inversible.
:::

Avec le théorème de la sous-section [13.5](unabhangigkeit-basis-und-rang.html#stufe-13-5), les énoncés suivants sont donc équivalents pour une matrice carrée : $\det\mathbf{A}\ne0$, $\mathbf{A}$ inversible, $\operatorname{rg}\mathbf{A}=n$, $\ker\mathbf{A}=\{\mathbf{0}\}$, colonnes linéairement indépendantes.

⁠**Exemple de calcul :** La matrice $\mathbf K$ de la sous-section [13.4](unabhangigkeit-basis-und-rang.html#stufe-13-4) a pour déterminant $\det\mathbf K=1\cdot(2-1)-0+1\cdot(0-1)=0$, en accord avec $\operatorname{rg}\mathbf K=2$. La matrice des coefficients de l’exemple traité par la méthode du pivot de Gauss a $\det=-4\ne0$ et est inversible ; c’est pourquoi le système avait exactement une solution.

⁠**En bref :** Une matrice carrée est inversible si et seulement si son déterminant n’est pas nul, c’est-à-dire si elle n’aplatit pas l’espace.

:::hintergrund Un petit déterminant ne signifie pas « presque non inversible »
On pourrait penser qu’une matrice de très petit déterminant est presque singulière. C’est faux. La matrice $0{,}1\,\mathbf{I}_{10}$ a pour déterminant $0{,}1^{10}=10^{-10}$, mais elle est parfaitement inversible : son inverse est $10\,\mathbf{I}_{10}$, et elle ne fait rien d’autre que raccourcir toutes les longueurs à un dixième. Le déterminant minuscule vient seulement de ce que le facteur $0{,}1$ se multiplie dans dix directions. Inversement, $\operatorname{diag}(1000;\,0{,}001)$ a pour déterminant $1$, bien qu’elle aplatisse presque le plan dans une direction. Le déterminant mesure le volume, et le volume dépend de l’échelle. Il ne permet pas de voir de façon fiable si une matrice détruit « presque » de l’information.
:::

:::aufgabe Exercice 34 ★ Calculer des déterminants
<span class="anker" id="aufg-34"></span>

<ol class="al">

<li>

Calculez les déterminants de $\bigl(\begin{smallmatrix}2&4\\1&2\end{smallmatrix}\bigr)$ et de $\Bigl(\begin{smallmatrix}1&2&0\\3&1&2\\0&1&1\end{smallmatrix}\Bigr)$. Laquelle des deux matrices est inversible ?

</li>

<li>

Quelle est l’aire du triangle de sommets $(0,\,0)$, $(3,\,1)$ et $(1,\,2)$ ?

</li>

<li>

Quel est le volume du parallélépipède construit sur les vecteurs $(1,\,0,\,0)^{\top}$, $(1,\,2,\,0)^{\top}$ et $(0,\,1,\,3)^{\top}$ ?

</li>

</ol>

:::loesung
(a) $\det\bigl(\begin{smallmatrix}2&4\\1&2\end{smallmatrix}\bigr)=4-4=0$ : non inversible, la deuxième colonne est le double de la première. Pour la matrice $3\times3$, en développant selon la première ligne :

$$1\cdot\det\begin{pmatrix}1&2\\1&1\end{pmatrix}-2\cdot\det\begin{pmatrix}3&2\\0&1\end{pmatrix}+0=1\cdot(1-2)-2\cdot3=-7 .$$

Elle est inversible.

(b) Le triangle est la moitié du parallélogramme construit sur $(3,1)^{\top}$ et $(1,2)^{\top}$, d’aire $|\det\bigl(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\bigr)|=5$ ; il a donc pour aire $2{,}5$. Cela découle aussi du facteur d’aire : le triangle de sommets $\mathbf{0}$, $\mathbf{e}_1$, $\mathbf{e}_2$, d’aire $\tfrac12$, est envoyé sur ce triangle.

(c) Les vecteurs pris comme colonnes donnent $\Bigl(\begin{smallmatrix}1&1&0\\0&2&1\\0&0&3\end{smallmatrix}\Bigr)$, une matrice triangulaire supérieure de déterminant $1\cdot2\cdot3=6$. Le volume vaut $6$.
:::
:::

:::aufgabe Exercice 35 ★★ Vérifier les règles de calcul
<span class="anker" id="aufg-35"></span>

<ol class="al">

<li>

Vérifiez $\det(\mathbf{C}\mathbf{D})=\det\mathbf{C}\cdot\det\mathbf{D}$ pour $\mathbf{C}=\bigl(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr)$ et $\mathbf{D}=\bigl(\begin{smallmatrix}0&1\\1&1\end{smallmatrix}\bigr)$, et calculez $\det(3\,\mathbf{C})$.

</li>

<li>

Montrez que toute matrice de rotation $\mathbf R_\alpha$ a pour déterminant $1$. Qu’est-ce que cela signifie géométriquement ?

</li>

<li>

Justifiez sans calcul pourquoi une matrice ayant deux colonnes égales a pour déterminant $0$.

</li>

</ol>

:::loesung
(a) $\det\mathbf{C}=4-6=-2$, $\det\mathbf{D}=0-1=-1$ et $\mathbf{C}\mathbf{D}=\bigl(\begin{smallmatrix}2&3\\4&7\end{smallmatrix}\bigr)$, avec $\det=14-12=2=(-2)\cdot(-1)$. De plus, $3\mathbf{C}=\bigl(\begin{smallmatrix}3&6\\9&12\end{smallmatrix}\bigr)$, avec $\det=36-54=-18=3^2\cdot(-2)$, comme l’indique la règle (iv) avec $n=2$.

(b) $\det\mathbf R_\alpha=\cos\alpha\cdot\cos\alpha-(-\sin\alpha)\cdot\sin\alpha=\cos^2\alpha+\sin^2\alpha=1$. Une rotation ne change aucune aire et ne retourne pas le plan.

(c) Deux colonnes égales sont linéairement dépendantes. Le parallélogramme ou le parallélépipède construit sur les colonnes est aplati, d’aire ou de volume nul. La même chose découle de la règle (v), appliquée aux colonnes grâce à $\det\mathbf{A}^{\top}=\det\mathbf{A}$ : si l’on échange les deux colonnes égales, la matrice reste la même, mais le déterminant devrait changer de signe. Donc $\det\mathbf{A}=-\det\mathbf{A}$, et par conséquent $\det\mathbf{A}=0$.
:::
:::

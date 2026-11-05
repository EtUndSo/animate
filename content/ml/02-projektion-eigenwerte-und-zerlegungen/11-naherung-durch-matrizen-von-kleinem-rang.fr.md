---
title: Approximation par des matrices de petit rang
pfad: Informatique / Apprentissage automatique / Projection, valeurs propres et décompositions
order: 6221100
summary: La décomposition en valeurs singulières classe les briques d’une matrice selon leur taille.
tags: norme de Frobenius, décomposition en valeurs singulières tronquée
lang: fr
---

<span class="anker" id="stufe-10"></span>

:::zweck
La décomposition en valeurs singulières classe les briques d’une matrice selon leur taille. Si l’on omet les petites, il reste une matrice de rang plus petit, que l’on peut stocker avec beaucoup moins de nombres. Cette section mesure à quelle distance cette approximation se trouve de la matrice d’origine et démontre qu’aucune autre matrice de même rang n’est plus proche.
:::

### La norme de Frobenius

<span class="anker" id="stufe-10-1"></span>

Pour dire à quel point deux matrices sont proches l’une de l’autre, il faut une mesure de la taille de leur différence. La norme spectrale en est une ; elle mesure l’allongement maximal. Une seconde est encore plus immédiate : on lit la matrice ligne par ligne, comme une image dans la Partie 1, section 6.1, pour en faire un long vecteur, et l’on prend sa norme euclidienne.

:::definition Définition 10.1 (Norme de Frobenius)
<span class="anker" id="satz-10-1"></span>

La __norme de Frobenius__ de $\mathbf{A}\in\mathbb{R}^{m\times n}$ est

$$\lVert\mathbf{A}\rVert_F=\sqrt{\sum_{i=1}^m\sum_{j=1}^na_{ij}^2} .$$
:::

:::satz Théorème 10.2 (Norme de Frobenius et valeurs singulières)
<span class="anker" id="satz-10-2"></span>

Pour toute matrice $\mathbf{A}$ de rang $r$,

<span class="anker" id="gl-10-1"></span>
$$\lVert\mathbf{A}\rVert_F^2=\operatorname{tr}(\mathbf{A}^{\top}\mathbf{A})=d_1^2+d_2^2+\dots+d_r^2 . \tag{10.1}$$
:::

:::beweis Norme de Frobenius
Le coefficient diagonal $j$ de $\mathbf{A}^{\top}\mathbf{A}$ est $\mathbf{a}_j^{\top}\mathbf{a}_j=\sum_ia_{ij}^2$, le carré de la longueur de la colonne $j$. La trace, somme de ces coefficients, est donc la somme des carrés de tous les coefficients de $\mathbf{A}$. D’après [(6.5)](eigenwerte-und-eigenvektoren.html#gl-6-5), la trace est aussi la somme des valeurs propres de $\mathbf{A}^{\top}\mathbf{A}$, et ce sont les $d_j^2$.
:::

Deux conséquences. Comme $d_1^2\le\sum_jd_j^2$, on a $\lVert\mathbf{A}\rVert_2\le\lVert\mathbf{A}\rVert_F$. Et une matrice orthogonale ne modifie pas la norme de Frobenius : $(\mathbf{Q}\mathbf{A})^{\top}(\mathbf{Q}\mathbf{A})=\mathbf{A}^{\top}\mathbf{Q}^{\top}\mathbf{Q}\mathbf{A}=\mathbf{A}^{\top}\mathbf{A}$, donc $\mathbf{Q}\mathbf{A}$ et $\mathbf{A}$ ont les mêmes valeurs singulières.

⁠**Exemple de calcul :** Pour $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$, on a $\lVert\mathbf{A}\rVert_F^2=4+9+0+4=17=4^2+1^2$ (Fig. [24](#abb-24)), donc $\lVert\mathbf{A}\rVert_F=\sqrt{17}\approx4{,}12$, un peu plus que $\lVert\mathbf{A}\rVert_2=4$.

:::abbildung ml/k2rfrobenius 24
Le carré de la norme de Frobenius de $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ : la somme des carrés de tous les coefficients, égale à la somme des carrés des valeurs singulières.
:::

⁠**En bref :** La norme de Frobenius est la norme euclidienne de l’ensemble des coefficients ; son carré est la somme des carrés des valeurs singulières.

### La décomposition tronquée

<span class="anker" id="stufe-10-2"></span>

Si l’on arrête la somme [(9.4)](die-singularwertzerlegung.html#gl-9-4) après les $k$ plus grandes briques, on obtient une approximation.

:::definition Définition 10.3 (Décomposition en valeurs singulières tronquée)
<span class="anker" id="satz-10-3"></span>

Pour $k<r$, on appelle

<span class="anker" id="gl-10-2"></span>
$$\mathbf{A}_k=\sum_{j=1}^kd_j\,\mathbf{u}_j\mathbf{v}_j^{\top} \tag{10.2}$$

la __décomposition en valeurs singulières tronquée__ de $\mathbf{A}$ à $k$ briques.
:::

$\mathbf{A}_k$ est de rang $k$, car $\mathbf{A}_k\mathbf{v}_j=d_j\mathbf{u}_j$ pour $j\le k$ et $\mathbf{A}_k\mathbf{v}_j=\mathbf{0}$ pour $j>k$ ; les images engendrent donc un espace de dimension $k$. L’erreur est le reste de la somme :

$$\mathbf{A}-\mathbf{A}_k=\sum_{j=k+1}^rd_j\,\mathbf{u}_j\mathbf{v}_j^{\top} .$$

Sa matrice de Gram est $\sum_{j>k}d_j^2\mathbf{v}_j\mathbf{v}_j^{\top}$, car les termes croisés disparaissent puisque $\mathbf{u}_i^{\top}\mathbf{u}_j=0$. Elle a les valeurs propres $d_{k+1}^2,\dots,d_r^2$ et, pour le reste, zéro. L’erreur a donc les valeurs singulières $d_{k+1},\dots,d_r$, et d’après [(9.5)](die-singularwertzerlegung.html#gl-9-5) et [(10.1)](#gl-10-1),

<span class="anker" id="gl-10-3"></span>
$$\lVert\mathbf{A}-\mathbf{A}_k\rVert_2=d_{k+1},\qquad \lVert\mathbf{A}-\mathbf{A}_k\rVert_F=\sqrt{d_{k+1}^2+\dots+d_r^2} . \tag{10.3}$$

Pour être stockée, $\mathbf{A}_k$ n’a besoin que des $k$ vecteurs $\mathbf{u}_j$ à $m$ composantes chacun, des $k$ vecteurs $\mathbf{v}_j$ à $n$ composantes chacun et des $k$ nombres $d_j$, soit au total $k(m+n+1)$ nombres au lieu de $mn$.

⁠**Exemple de calcul :** Pour $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ et $k=1$, on a

$$\mathbf{A}_1=4\,\mathbf{u}_1\mathbf{v}_1^{\top}=\begin{pmatrix}1{,}6&3{,}2\\0{,}8&1{,}6\end{pmatrix},\qquad \mathbf{A}-\mathbf{A}_1=\mathbf{u}_2\mathbf{v}_2^{\top}=\begin{pmatrix}0{,}4&-0{,}2\\-0{,}8&0{,}4\end{pmatrix}.$$

La norme de Frobenius de l’erreur vaut $\sqrt{0{,}16+0{,}04+0{,}64+0{,}16}=1=d_2$ (Fig. [25](#abb-25)), de même que sa norme spectrale.

:::abbildung ml/k2rfehler 25
L’erreur de la meilleure approximation de rang $1$ en norme de Frobenius, avec $0{,}4=\tfrac25$, $0{,}2=\tfrac15$ et $0{,}8=\tfrac45$ : son carré vaut $d_2^2=1$.
:::

⁠**En bref :** $\mathbf{A}_k$ conserve les $k$ plus grandes briques ; l’erreur a les valeurs singulières restantes, et sa norme spectrale vaut $d_{k+1}$.

### La meilleure approximation

<span class="anker" id="stufe-10-3"></span>

Il existe beaucoup de matrices de rang $k$. La décomposition tronquée est-elle la meilleure d’entre elles ? Oui, dans les deux normes.

:::satz Théorème 10.4 (Théorème d’Eckart-Young)
<span class="anker" id="satz-10-4"></span>

Soit $\mathbf{A}$ de rang $r$ et $k<r$. Pour toute matrice $\mathbf{B}$ de même format telle que $\operatorname{rg}\mathbf{B}\le k$,

<span class="anker" id="gl-10-4"></span>
$$\lVert\mathbf{A}-\mathbf{B}\rVert_2\ge d_{k+1}=\lVert\mathbf{A}-\mathbf{A}_k\rVert_2,\qquad \lVert\mathbf{A}-\mathbf{B}\rVert_F\ge\sqrt{d_{k+1}^2+\dots+d_r^2}=\lVert\mathbf{A}-\mathbf{A}_k\rVert_F . \tag{10.4}$$

Parmi toutes les matrices de rang au plus $k$, c’est donc $\mathbf{A}_k$ qui est la plus proche de $\mathbf{A}$.
:::

:::beweis Norme spectrale
D’après le théorème du rang, le noyau de $\mathbf{B}$ est de dimension $n-\operatorname{rg}\mathbf{B}\ge n-k$. On choisit $n-k$ vecteurs linéairement indépendants $\mathbf{b}_1,\dots,\mathbf{b}_{n-k}$ dans le noyau et l’on y ajoute $\mathbf{v}_1,\dots,\mathbf{v}_{k+1}$. Cela fait $n+1$ vecteurs de $\mathbb{R}^n$, et d’après la Partie 1, section 13.4, ils sont linéairement dépendants, car une matrice à $n$ lignes est de rang au plus $n$. Il existe donc des nombres non tous nuls tels que $\sum_l\alpha_l\mathbf{b}_l=\sum_j\beta_j\mathbf{v}_j$. Ce vecteur $\mathbf{z}$ n’est pas nul, car sinon, en raison de l’indépendance des deux listes, tous les nombres seraient nuls. Il appartient au noyau de $\mathbf{B}$ et au sous-espace engendré par $\mathbf{v}_1,\dots,\mathbf{v}_{k+1}$. On le normalise à la longueur $1$. Alors $(\mathbf{A}-\mathbf{B})\mathbf{z}=\mathbf{A}\mathbf{z}$, et avec $\mathbf{z}=\sum_{j\le k+1}c_j\mathbf{v}_j$, $\sum_jc_j^2=1$ :

$$\lVert(\mathbf{A}-\mathbf{B})\mathbf{z}\rVert^2=\lVert\mathbf{A}\mathbf{z}\rVert^2=\sum_{j=1}^{k+1}d_j^2c_j^2\ge d_{k+1}^2\sum_{j=1}^{k+1}c_j^2=d_{k+1}^2 .$$

Ainsi, $\mathbf{A}-\mathbf{B}$ allonge le vecteur unitaire $\mathbf{z}$ d’un facteur au moins égal à $d_{k+1}$, et $\lVert\mathbf{A}-\mathbf{B}\rVert_2\ge d_{k+1}$.
:::

La preuve en montre la raison : une matrice de rang $k$ doit envoyer sur zéro tout un ensemble de directions, à savoir son noyau. Ce noyau rencontre forcément l’espace des $k+1$ directions que $\mathbf{A}$ étire le plus, et là, $\mathbf{B}$ commet une erreur d’au moins $d_{k+1}$.

⁠**Exemple de calcul :** Pour $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$, $\mathbf{A}_1$ est la meilleure matrice de rang $1$, avec l’erreur $1$ dans les deux normes. Une autre matrice de rang $1$, par exemple $\mathbf{B}=\bigl(\begin{smallmatrix}2&3\\0&0\end{smallmatrix}\bigr)$, qui annule simplement la deuxième ligne, a pour erreur $\mathbf{A}-\mathbf{B}=\bigl(\begin{smallmatrix}0&0\\0&2\end{smallmatrix}\bigr)$, de norme $2$.

⁠**En bref :** La décomposition tronquée $\mathbf{A}_k$ est la meilleure approximation de rang $k$, en norme spectrale comme en norme de Frobenius.

:::hintergrund Pourquoi l’énoncé vaut aussi pour la norme de Frobenius
La preuve pour la norme de Frobenius considère les lignes $\mathbf{a}^{(1)\top},\dots,\mathbf{a}^{(m)\top}$ de $\mathbf{A}$ comme $m$ points de $\mathbb{R}^n$, à la manière des exemples d’une matrice de données. Si $\mathbf{B}$ est de rang au plus $k$, ses lignes appartiennent à un sous-espace $\mathcal S$ de dimension $k$ : l’espace des colonnes de $\mathbf{B}^{\top}$, complété jusqu’à la dimension $k$. Pour un sous-espace $\mathcal S$ fixé, de matrice de projection $\mathbf{P}$, la projection $\mathbf{P}\mathbf{a}^{(i)}$ de chaque ligne est, d’après la section [4](projektion-auf-einen-unterraum.html#stufe-4), le point de $\mathcal S$ le plus proche. Avec une base orthonormée $\mathbf{w}_1,\dots,\mathbf{w}_k$ de $\mathcal S$, le théorème de Pythagore donne

$$\lVert\mathbf{A}-\mathbf{B}\rVert_F^2\ge\sum_i\bigl\lVert\mathbf{a}^{(i)}-\mathbf{P}\mathbf{a}^{(i)}\bigr\rVert^2=\lVert\mathbf{A}\rVert_F^2-\sum_i\lVert\mathbf{P}\mathbf{a}^{(i)}\rVert^2=\lVert\mathbf{A}\rVert_F^2-\sum_{l=1}^k\lVert\mathbf{A}\mathbf{w}_l\rVert^2 ,$$

car $\lVert\mathbf{P}\mathbf{a}^{(i)}\rVert^2=\sum_l(\mathbf{w}_l^{\top}\mathbf{a}^{(i)})^2$, et $\mathbf{w}_l^{\top}\mathbf{a}^{(i)}$ est la composante $i$ de $\mathbf{A}\mathbf{w}_l$. Il reste à montrer que $\sum_l\lVert\mathbf{A}\mathbf{w}_l\rVert^2\le d_1^2+\dots+d_k^2$. Dans les coordonnées des $\mathbf{v}_j$, on a

$$\sum_{l=1}^k\lVert\mathbf{A}\mathbf{w}_l\rVert^2=\sum_{l=1}^k\sum_jd_j^2(\mathbf{v}_j^{\top}\mathbf{w}_l)^2=\sum_jd_j^2\,g_j\qquad\text{avec}\qquad g_j=\sum_{l=1}^k(\mathbf{v}_j^{\top}\mathbf{w}_l)^2 .$$

Chaque $g_j$ est le carré de la longueur de la projection de $\mathbf{v}_j$ sur $\mathcal S$, donc $0\le g_j\le1$, et la somme de tous les $g_j$ vaut $\sum_l\lVert\mathbf{w}_l\rVert^2=k$. Une somme $\sum_jd_j^2g_j$ avec de tels poids est maximale lorsque les $k$ plus grands $d_j^2$ reçoivent le poids plein $1$ ; elle vaut alors $d_1^2+\dots+d_k^2$. Avec [(10.1)](#gl-10-1), il s’ensuit que $\lVert\mathbf{A}-\mathbf{B}\rVert_F^2\ge d_{k+1}^2+\dots+d_r^2$. Le calcul montre au passage que le sous-espace dont les lignes de $\mathbf{A}$ sont le plus proches est le sous-espace engendré par $\mathbf{v}_1,\dots,\mathbf{v}_k$.
:::

### Une image avec peu de nombres

<span class="anker" id="stufe-10-4"></span>

Une image en niveaux de gris est une matrice. D’après le théorème d’Eckart-Young, $\mathbf{A}_k$ est la meilleure approximation à $k$ briques, et [(10.3)](#gl-10-3) indique ce que l’on perd. La proportion

$$\frac{d_1^2+\dots+d_k^2}{d_1^2+\dots+d_r^2}$$

indique quelle part de la somme des carrés de toutes les valeurs de luminosité est conservée.

⁠**Exemple de calcul :** La croix de la Partie 1, section 6.1, est

$$\mathbf{C}=\begin{pmatrix}0&1&0\\1&1&1\\0&1&0\end{pmatrix}.$$

Elle est symétrique. Son polynôme caractéristique est $-\lambda^3+\lambda^2+2\lambda=-\lambda(\lambda-2)(\lambda+1)$, ses valeurs propres sont $2$, $-1$ et $0$, de vecteurs propres $(1,\,2,\,1)^{\top}$, $(1,\,-1,\,1)^{\top}$ et $(1,\,0,\,-1)^{\top}$. D’après la section [9.7](die-singularwertzerlegung.html#stufe-9-7), les valeurs singulières sont $2$, $1$ et $0$ ; le rang est $2$. La meilleure approximation de rang $1$ est, avec $\mathbf{q}_1=(1,\,2,\,1)^{\top}/\sqrt6$,

$$\mathbf{C}_1=2\,\mathbf{q}_1\mathbf{q}_1^{\top}=\frac13\begin{pmatrix}1&2&1\\2&4&2\\1&2&1\end{pmatrix},\qquad \mathbf{C}-\mathbf{C}_1=\frac13\begin{pmatrix}-1&1&-1\\1&-1&1\\-1&1&-1\end{pmatrix}$$

(Fig. [26](#abb-26)). L’erreur a la taille $1$ dans les deux normes. $\mathbf{C}_1$ conserve $4/5=80\,\%$ de la somme $\lVert\mathbf{C}\rVert_F^2=5$. Chaque ligne de $\mathbf{C}_1$ est un multiple de la même ligne $(1,\,2,\,1)$ : une image de rang $1$ est un profil de luminosité des colonnes multiplié par un profil de luminosité des lignes, ici une tache floue dont le point le plus clair est au centre. Il faut stocker $1\cdot(3+3+1)=7$ nombres au lieu de $9$.

:::abbildung ml/k2bild 26
La croix $\mathbf{C}$ de $3\times3$ pixels (à gauche ; $0$ noir, $1$ blanc), sa meilleure approximation $\mathbf{C}_1$ de rang $1$ (au centre ; la valeur $\tfrac43$ est plus claire que le blanc et représentée en blanc) et l’erreur $\mathbf{C}-\mathbf{C}_1$ (à droite ; rouge positif, bleu négatif). L’erreur est elle-même une matrice de rang $1$, la brique associée à la valeur singulière $1$.
:::

Pour une croix de $3\times3$ pixels, l’économie est faible. Pour de grandes images, la différence est considérable : une image de $1000\times1000$ pixels a $10^6$ coefficients ; l’approximation à $k=50$ briques nécessite $50\cdot(1000+1000+1)=100\,050$ nombres, soit environ $10\,\%$. Que l’approximation ait un bel aspect dépend de la vitesse à laquelle les valeurs singulières décroissent. Dans beaucoup de photos, des lignes voisines se ressemblent fortement ; les lignes sont alors proches d’un sous-espace de petite dimension, et quelques grandes valeurs singulières portent presque toute la somme $\sum_jd_j^2$.

⁠**En bref :** Une image de rang $k$ nécessite $k(m+n+1)$ nombres ; la décomposition tronquée est la meilleure image de ce type, et $\sum_{j\le k}d_j^2/\sum_jd_j^2$ indique la part conservée.

:::aufgabe Exercice 30 ★ Normes d’une matrice
<span class="anker" id="aufg-30"></span>

<ol class="al">

<li>

Calculez $\lVert\mathbf{A}\rVert_F$ et $\lVert\mathbf{A}\rVert_2$ pour $\mathbf{A}=\bigl(\begin{smallmatrix}3&0\\4&5\end{smallmatrix}\bigr)$ de l’exercice [27](die-singularwertzerlegung.html#aufg-27) et vérifiez [(10.1)](#gl-10-1).

</li>

<li>

Quelle est la norme de Frobenius d’une matrice orthogonale $n\times n$ ?

</li>

<li>

Montrez que $\lVert\mathbf{A}\rVert_2\le\lVert\mathbf{A}\rVert_F\le\sqrt r\,\lVert\mathbf{A}\rVert_2$. Quand y a-t-il égalité à droite ?

</li>

</ol>

:::loesung
(a) $\lVert\mathbf{A}\rVert_F^2=9+0+16+25=50=45+5=d_1^2+d_2^2$, donc $\lVert\mathbf{A}\rVert_F=\sqrt{50}\approx7{,}07$, et $\lVert\mathbf{A}\rVert_2=d_1=3\sqrt5\approx6{,}71$.

(b) Toutes les valeurs singulières d’une matrice orthogonale valent $1$, donc $\lVert\mathbf{Q}\rVert_F^2=n$ et $\lVert\mathbf{Q}\rVert_F=\sqrt n$. On le voit aussi directement : chacune des $n$ colonnes a pour carré de longueur $1$.

(c) On a $\lVert\mathbf{A}\rVert_2^2=d_1^2\le d_1^2+\dots+d_r^2=\lVert\mathbf{A}\rVert_F^2$, et chacun des $r$ termes vaut au plus $d_1^2$, donc $\lVert\mathbf{A}\rVert_F^2\le r\,d_1^2$. En prenant les racines carrées, on obtient les deux inégalités. Il y a égalité à droite si et seulement si toutes les valeurs singulières positives sont égales à $d_1$, comme pour une matrice orthogonale.
:::
:::

:::aufgabe Exercice 31 ★★ La meilleure matrice de rang 1
<span class="anker" id="aufg-31"></span>

Soit $\mathbf{A}=\Bigl(\begin{smallmatrix}1&1\\1&1\\1&-1\end{smallmatrix}\Bigr)$ la matrice de l’exercice [28](die-singularwertzerlegung.html#aufg-28).

<ol class="al">

<li>

Calculez $\mathbf{A}_1$ et l’erreur $\mathbf{A}-\mathbf{A}_1$ dans les deux normes.

</li>

<li>

La matrice $\mathbf{B}$ dont tous les coefficients valent un est elle aussi de rang $1$. Calculez $\lVert\mathbf{A}-\mathbf{B}\rVert_F$ et $\lVert\mathbf{A}-\mathbf{B}\rVert_2$ et comparez avec (a).

</li>

<li>

Quelle part de la somme des carrés des coefficients est conservée dans $\mathbf{A}_1$ ?

</li>

</ol>

:::loesung
(a) D’après l’exercice [28](die-singularwertzerlegung.html#aufg-28) : $d_1=2$, $\mathbf{u}_1=(1,\,1,\,0)^{\top}/\sqrt2$, $\mathbf{v}_1=(1,\,1)^{\top}/\sqrt2$. Donc

$$\mathbf{A}_1=2\,\mathbf{u}_1\mathbf{v}_1^{\top}=\begin{pmatrix}1&1\\1&1\\0&0\end{pmatrix},\qquad \mathbf{A}-\mathbf{A}_1=\begin{pmatrix}0&0\\0&0\\1&-1\end{pmatrix}.$$

L’erreur a pour norme de Frobenius $\sqrt{1+1}=\sqrt2=d_2$. C’est le produit extérieur $\mathbf{e}_3\,(1,\,-1)$, dont l’unique valeur singulière est, d’après l’exercice [29](die-singularwertzerlegung.html#aufg-29), $1\cdot\sqrt2$ ; sa norme spectrale vaut elle aussi $\sqrt2$.

(b) $\mathbf{A}-\mathbf{B}=\Bigl(\begin{smallmatrix}0&0\\0&0\\0&-2\end{smallmatrix}\Bigr)$ a pour taille $2>\sqrt2$ dans les deux normes. Comme l’exige le théorème d’Eckart-Young, $\mathbf{B}$ est plus éloignée de $\mathbf{A}$ que $\mathbf{A}_1$.

(c) $\lVert\mathbf{A}\rVert_F^2=6=4+2$, et $\mathbf{A}_1$ conserve $d_1^2/(d_1^2+d_2^2)=\tfrac46=\tfrac23\approx67\,\%$.
:::
:::

:::aufgabe Exercice 32 ★ Encombrement mémoire
<span class="anker" id="aufg-32"></span>

Une image en niveaux de gris a $600\times800$ pixels.

<ol class="al">

<li>

Combien de nombres l’approximation à $k=40$ briques nécessite-t-elle ? Quelle part du nombre initial cela représente-t-il ?

</li>

<li>

À partir de quel $k$ l’approximation ne fait-elle plus économiser de mémoire ?

</li>

</ol>

:::loesung
(a) $40\cdot(600+800+1)=40\cdot1\,401=56\,040$ nombres au lieu de $600\cdot800=480\,000$, soit environ $11{,}7\,\%$.

(b) L’approximation fait économiser de la mémoire tant que $k\cdot1\,401<480\,000$, c’est-à-dire pour $k\le342$, car $342\cdot1\,401=479\,142$ et $343\cdot1\,401=480\,543$. À partir de $k=343$, l’approximation nécessite plus de nombres que l’image elle-même. Le rang vaut au plus $600$ ; il n’existe de toute façon pas plus de $600$ briques.
:::
:::

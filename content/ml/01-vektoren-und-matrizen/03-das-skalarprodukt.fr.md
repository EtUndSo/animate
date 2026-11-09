---
title: Le produit scalaire
pfad: Informatique / Apprentissage automatique / Fondements mathématiques / Vecteurs et matrices
knoten: Fondements 1 : Vecteurs et matrices
nachschlagen: ja
order: 15210300
summary: Deux vecteurs de même longueur donnent un seul nombre lorsqu’on multiplie leurs composantes correspondantes et qu’on additionne les produits.
tags: produit scalaire, poids, somme pondérée, modèle, prédiction, vecteur de uns, moyenne
lang: fr
---

<span class="anker" id="stufe-2"></span>

:::zweck
Deux vecteurs de même longueur donnent un seul nombre lorsqu’on multiplie leurs composantes correspondantes et qu’on additionne les produits. Ce calcul est le plus fréquent de tout l’apprentissage automatique : il transforme des valeurs mesurées en une estimation et compare des données à un motif.
:::

### Le produit scalaire de deux vecteurs

<span class="anker" id="stufe-2-1"></span>

Une facture d’achats se calcule ainsi : quantité fois prix pour chaque article, puis on additionne le tout. Le même calcul avec deux vecteurs quelconques s’appelle le produit scalaire.

On peut se le représenter comme la rencontre d’une ligne et d’une colonne. On écrit le premier vecteur en ligne, le second en colonne à côté. Puis on multiplie le premier élément de la ligne par le premier de la colonne, le deuxième par le deuxième, et ainsi de suite, et l’on additionne :

$$\begin{pmatrix}1&2&3\end{pmatrix}\begin{pmatrix}4\\-1\\2\end{pmatrix}=1\cdot4+2\cdot(-1)+3\cdot2=8 .$$

:::definition Définition 2.1 (Produit scalaire)
<span class="anker" id="satz-2-1"></span>

Le __produit scalaire__ de deux vecteurs $\mathbf{u},\mathbf{v}\in\mathbb{R}^d$ est le nombre

<span class="anker" id="gl-2-1"></span>
$$\mathbf{u}^{\top}\mathbf{v}=\sum_{j=1}^{d}u_j\,v_j=u_1v_1+u_2v_2+\dots+u_dv_d . \tag{2.1}$$
:::

La notation $\mathbf{u}^{\top}\mathbf{v}$ dit exactement ce qui se passe : $\mathbf{u}^{\top}$ est $\mathbf{u}$ écrit en ligne, et la ligne rencontre la colonne $\mathbf{v}$. Le résultat est un scalaire, d’où le nom.

:::satz Théorème 2.2 (Règles de calcul du produit scalaire)
<span class="anker" id="satz-2-2"></span>

Pour tous $\mathbf{u},\mathbf{v},\mathbf{q}\in\mathbb{R}^d$ et tout scalaire $c$, on a :

<ol class="rm">

<li>

$\mathbf{u}^{\top}\mathbf{v}=\mathbf{v}^{\top}\mathbf{u}$ (symétrie) ;

</li>

<li>

$(c\,\mathbf{u})^{\top}\mathbf{v}=c\,(\mathbf{u}^{\top}\mathbf{v})$ et $(\mathbf{u}+\mathbf{q})^{\top}\mathbf{v}=\mathbf{u}^{\top}\mathbf{v}+\mathbf{q}^{\top}\mathbf{v}$ (linéarité, de même par rapport au second vecteur) ;

</li>

<li>

$\mathbf{u}^{\top}\mathbf{u}=\sum_ju_j^2\ge0$, et $\mathbf{u}^{\top}\mathbf{u}=0$ seulement pour $\mathbf{u}=\mathbf{0}$.

</li>

</ol>
:::

:::beweis Règles de calcul du produit scalaire
(i) découle de $u_jv_j=v_ju_j$ pour chaque composante. (ii) est la règle des sommes [(1.2)](vektoren-daten-als-zahlenlisten.html#gl-1-2) : $\sum_j(c\,u_j)v_j=c\sum_ju_jv_j$ et $\sum_j(u_j+q_j)v_j=\sum_ju_jv_j+\sum_jq_jv_j$. (iii) Chaque terme $u_j^2$ est positif ou nul. La somme n’est nulle que si chaque terme est nul, c’est-à-dire si chaque $u_j=0$.
:::

⁠**Exemple de calcul :** Pour $\mathbf{u}=(1,\,2,\,3)^{\top}$ et $\mathbf{v}=(4,\,-1,\,2)^{\top}$, on a $\mathbf{u}^{\top}\mathbf{v}=8$ et $\mathbf{u}^{\top}\mathbf{u}=14$ (Fig. [6](#abb-6)). Dans l’ordre inverse, on obtient le même nombre, $\mathbf{v}^{\top}\mathbf{u}=4\cdot1+(-1)\cdot2+2\cdot3=8$, comme l’exige la symétrie.

:::abbildung ml/k1rskp 6
Deux produits scalaires pas à pas : composante fois composante, puis la somme des produits. Le produit scalaire d’un vecteur avec lui-même est la somme des carrés de ses composantes.
:::

⁠**En bref :** Le produit scalaire multiplie deux vecteurs composante par composante et additionne les produits ; c’est un nombre.

:::hintergrund D’autres notations pour la même chose
Dans de nombreux livres, on trouve $\mathbf{u}\cdot\mathbf{v}$ ou $\langle\mathbf{u},\mathbf{v}\rangle$ au lieu de $\mathbf{u}^{\top}\mathbf{v}$ ; en anglais, on parle de *dot product* ou d’*inner product*. Il s’agit du même nombre. Cette série écrit $\mathbf{u}^{\top}\mathbf{v}$, parce qu’on voit ainsi dans la notation même qu’une ligne rencontre une colonne. Cela s’avère payant dès que des tableaux de nombres entrent en jeu.
:::

### Poids et sommes pondérées

<span class="anker" id="stufe-2-2"></span>

Une agente immobilière estime de tête le prix d’un appartement à peu près ainsi : chaque mètre carré vaut environ $3$ mille euros, chaque pièce ajoute encore $10$ mille euros, et chaque kilomètre de distance au centre retranche $4$ mille euros. Elle prend donc chaque caractéristique avec son propre facteur et additionne le tout.

Le nombre avec lequel une caractéristique entre dans un tel calcul s’appelle son __poids__. Un grand poids positif signifie : chaque unité de cette caractéristique augmente fortement le résultat. Un poids négatif signifie : la caractéristique fait baisser le résultat.

:::definition Définition 2.3 (Somme pondérée)
<span class="anker" id="satz-2-3"></span>

Pour un vecteur de poids $\mathbf{w}=(w_1,\dots,w_d)^{\top}$ et un exemple $\mathbf{x}\in\mathbb{R}^d$, la __somme pondérée__ est

<span class="anker" id="gl-2-2"></span>
$$\hat y=\mathbf{w}^{\top}\mathbf{x}=\sum_{j=1}^{d}w_j\,x_j . \tag{2.2}$$
:::

Une règle de calcul fixe qui produit un nombre à partir des caractéristiques d’un exemple s’appelle un __modèle__. Le nombre que le modèle fournit pour un exemple s’appelle sa __prédiction__. Le chapeau sur le $y$ dans $\hat y$ indique qu’il s’agit d’une estimation calculée et non d’une valeur mesurée. Dans ce chapitre, les poids sont toujours donnés ; savoir d’où viennent de bons poids est une question à part.

⁠**Exemple de calcul :** L’agente immobilière utilise les poids $\mathbf{w}=(3,\,10,\,-4)^{\top}$ en milliers d’euros par mètre carré, par pièce et par kilomètre. Pour l’appartement 1, $\hat y_1=\mathbf{w}^{\top}\mathbf{x}_1=188$ (Fig. [7](#abb-7)), soit $188$ mille euros.

:::abbildung ml/k1rgewicht 7
L’estimation de l’agente immobilière pour l’appartement 1 : chaque caractéristique fois son poids, puis la somme. Les contributions des trois caractéristiques sont de $180$, $20$ et $-12$ mille euros.
:::

Pour les autres appartements, on obtient de même $\hat y_2=126$, $\hat y_3=286$ et $\hat y_4=232$. Chaque produit $w_jx_j$ s’exprime en milliers d’euros, parce que l’unité de la caractéristique se simplifie avec l’unité au dénominateur du poids. C’est la seule raison pour laquelle on peut additionner les trois produits.

⁠**En bref :** Une somme pondérée est le produit scalaire $\mathbf{w}^{\top}\mathbf{x}$ des poids et des caractéristiques ; c’est le modèle le plus simple qui transforme des caractéristiques en une prédiction.

:::hintergrund Un grand poids ne signifie pas que la caractéristique est importante
Chez l’agente immobilière, le poids des pièces, $10$, est plus de trois fois plus grand que celui de la surface, $3$. Pourtant, pour l’appartement 1, la surface apporte $180$ mille euros et le nombre de pièces seulement $20$. La raison : un poids s’applique par unité de la caractéristique, et la surface compte beaucoup d’unités. Si l’on mesure la surface en unités de $10\,\mathrm m^2$, l’appartement 1 ne mesure plus que $6$ unités, et le même modèle a besoin du poids $30$ mille euros par $10\,\mathrm m^2$. La prédiction reste la même, seul le poids est devenu dix fois plus grand. La valeur d’un poids dépend donc de l’unité choisie. Si l’on veut savoir combien une caractéristique contribue à la prédiction, il faut regarder le produit $w_jx_j$, et non le poids seul.
:::

### Somme et moyenne comme produit scalaire

<span class="anker" id="stufe-2-3"></span>

De nombreux calculs de tous les jours sont des produits scalaires avec un second vecteur particulièrement simple. Ceux dont on a le plus souvent besoin sont la somme et la moyenne de toutes les composantes.

Le __vecteur de uns__ $\mathbf 1\in\mathbb{R}^n$ n’a que des uns comme composantes. Le produit scalaire avec lui additionne simplement toutes les composantes : $\mathbf 1^{\top}\mathbf{v}=v_1+\dots+v_n$.

:::definition Définition 2.4 (Moyenne)
<span class="anker" id="satz-2-4"></span>

La __moyenne__ des composantes d’un vecteur $\mathbf{v}\in\mathbb{R}^n$ est

<span class="anker" id="gl-2-3"></span>
$$\bar v=\frac1n\sum_{i=1}^nv_i=\frac1n\,\mathbf 1^{\top}\mathbf{v} . \tag{2.3}$$
:::

Autres calculs de ce type : le produit scalaire avec un vecteur unitaire sélectionne une composante, $\mathbf{e}_j^{\top}\mathbf{v}=v_j$, car tous les autres produits contiennent un zéro. Le produit scalaire d’un vecteur avec lui-même est la somme des carrés, $\mathbf{v}^{\top}\mathbf{v}=\sum_iv_i^2$. Les quantités multipliées par les prix, puis additionnées, donnent le montant de la facture. Et évaluer un polynôme $p(t)=c_1+c_2t+\dots+c_nt^{n-1}$ en un point $t$ revient à former le produit scalaire $\mathbf{c}^{\top}\mathbf{z}$ de ses coefficients $\mathbf{c}=(c_1,\dots,c_n)^{\top}$ avec les puissances $\mathbf{z}=(1,\,t,\,t^2,\dots,t^{n-1})^{\top}$. Pour $p(t)=1+2t+3t^2$ au point $t=2$, cela donne $(1,\,2,\,3)\,(1,\,2,\,4)^{\top}=1+4+12=17$.

⁠**Exemple de calcul :** De janvier à mars, l’appartement 1 a consommé $\mathbf{u}=(200,\,250,\,300)^{\top}$ kWh d’électricité (sous-section [1.4](vektoren-daten-als-zahlenlisten.html#stufe-1-4)). Au total, cela fait $\mathbf 1^{\top}\mathbf{u}=750$ kWh, soit en moyenne $\bar u=250$ kWh par mois (Fig. [8](#abb-8)). La consommation de février est $\mathbf{e}_2^{\top}\mathbf{u}=250$ kWh.

:::abbildung ml/k1rmittel 8
Somme et moyenne de la consommation d’électricité comme produit scalaire avec le vecteur de uns, en kWh.
:::

Si le kilowattheure coûte $\mathbf{p}=(0{,}32;\ 0{,}34;\ 0{,}28)^{\top}$ euro au cours des trois mois, la facture d’électricité est le produit scalaire des prix et des quantités : $\mathbf{p}^{\top}\mathbf{u}=233$ euros (Fig. [9](#abb-9)). Chaque produit $p_ju_j$ est le montant d’un mois, en euros par kWh fois des kWh, donc en euros.

:::abbildung ml/k1rstrom 9
La facture d’électricité comme produit scalaire : prix fois quantité pour chaque mois, puis la somme, en euros.
:::

⁠**En bref :** La somme, la moyenne, la sélection d’une composante et la somme des carrés sont des produits scalaires avec $\mathbf 1$, $\tfrac1n\mathbf 1$, $\mathbf{e}_j$ et le vecteur lui-même.

### Le produit scalaire comme comparaison avec un motif

<span class="anker" id="stufe-2-4"></span>

Il s’agit de vérifier si un signal mesuré saute alternativement vers le haut et vers le bas d’un échantillon à l’autre. Pour cela, on écrit le motif recherché sous forme de vecteur, ici $\mathbf{w}=(1,\,-1,\,1,\,-1)^{\top}$, et l’on forme le produit scalaire avec le signal.

La Fig. [10](#abb-10) montre ce qui se passe alors. Chaque échantillon est multiplié par la valeur du motif à la même position. Si le signal a, en une position, le même signe que le motif, le produit est positif ; s’il a le signe opposé, le produit est négatif. Si le signal suit partout le motif, les contributions positives s’accumulent en une grande somme. Si le signal n’a rien à voir avec le motif, les contributions positives et négatives se compensent.

:::abbildung ml/k1muster 10
Comparaison avec un motif par le produit scalaire. En haut le motif $\mathbf{w}=(1,-1,1,-1)^{\top}$, au milieu deux signaux, en bas les produits $w_j\,x_j$ en chaque position $j$. À gauche, le signal $\mathbf{x}=(2,-1,3,-2)^{\top}$ saute au rythme du motif : tous les produits sont positifs, la somme vaut $8$. À droite, $\mathbf{x}'=(2,2,3,3)^{\top}$ croît régulièrement : les produits se compensent, la somme vaut $0$.
:::

Plus précisément : la contribution de la position $j$ au produit scalaire $\mathbf{w}^{\top}\mathbf{x}$ est $w_jx_j$. Elle est positive lorsque $w_j$ et $x_j$ ont le même signe, et négative lorsqu’ils sont de signes opposés. Plus les valeurs absolues sont grandes aux positions où les signes concordent, plus le produit scalaire est grand.

En traitement du signal, on connaît ce calcul sous le nom de corrélation. L’intercorrélation de deux suites réelles $x[n]$ et $y[n]$ pour un décalage nul vaut $\sum_nx[n]\,y[n]$. Si l’on écrit les échantillons de deux signaux de longueur finie sous forme de vecteurs $\mathbf{x}$ et $\mathbf{y}$, c’est exactement le produit scalaire $\mathbf{x}^{\top}\mathbf{y}$. L’énergie d’un signal, $\sum_nx[n]^2$, est de même $\mathbf{x}^{\top}\mathbf{x}$. La comparaison avec un motif n’est donc pas un nouvel outil, mais celui-là même avec lequel un corrélateur cherche un motif connu dans un signal.

⁠**Exemple de calcul :** Avec le motif alterné $\mathbf{w}=(1,\,-1,\,1,\,-1)^{\top}$, on a $\mathbf{w}^{\top}\mathbf{x}=8$ pour $\mathbf{x}=(2,\,-1,\,3,\,-2)^{\top}$ et $\mathbf{w}^{\top}\mathbf{x}'=0$ pour $\mathbf{x}'=(2,\,2,\,3,\,3)^{\top}$ (Fig. [11](#abb-11)). Avec le motif constant $\mathbf 1=(1,\,1,\,1,\,1)^{\top}$, c’est l’inverse : $\mathbf 1^{\top}\mathbf{x}=2$, mais $\mathbf 1^{\top}\mathbf{x}'=10$. Le signal $\mathbf{x}$ est donc surtout alterné, $\mathbf{x}'$ surtout constant.

:::abbildung ml/k1rmuster 11
Le motif alterné $\mathbf{w}$ avec deux signaux. En haut, $\mathbf{x}$ suit le motif : les quatre produits sont positifs. En bas, $\mathbf{x}'$ croît régulièrement : les produits se compensent deux à deux.
:::

La somme pondérée de l’agente immobilière est elle aussi une comparaison avec un motif. Son motif $\mathbf{w}=(3,\,10,\,-4)^{\top}$ décrit ce qui donne de la valeur à un appartement : beaucoup de surface, beaucoup de pièces, peu de distance. Plus un appartement correspond à ce motif, plus sa prédiction est élevée.

⁠**En bref :** Le produit scalaire $\mathbf{w}^{\top}\mathbf{x}$ est grand lorsque $\mathbf{x}$ a de grandes valeurs là où le motif $\mathbf{w}$ a de grandes valeurs de même signe ; c’est la corrélation pour un décalage nul.

:::hintergrund La fonction de corrélation n’est faite que de produits scalaires
L’intercorrélation ne compare pas un signal à un motif en une seule position, mais pour chaque décalage possible. Pour chaque décalage $k$, sa valeur est un produit scalaire : celui du signal avec le motif décalé de $k$ pas. Toute la fonction de corrélation est donc une suite de produits scalaires, un par décalage. Là où le motif se trouve dans le signal, les contributions positives s’accumulent, et la fonction de corrélation y atteint sa plus grande valeur. C’est ainsi qu’un récepteur radar trouve l’écho de sa propre impulsion et qu’un récepteur radio trouve le début d’une trame de données connue. En apprentissage automatique, le décalage reste le plus souvent fixé à zéro : on compare un exemple dans son ensemble à un motif.
:::

:::aufgabe Exercice 4 ★ Vérifier les règles de calcul
<span class="anker" id="aufg-4"></span>

Soient $\mathbf{u}=(1,\,0,\,2)^{\top}$, $\mathbf{v}=(3,\,-1,\,1)^{\top}$ et $\mathbf{q}=(0,\,2,\,1)^{\top}$. Calculez $\mathbf{u}^{\top}\mathbf{v}$, $\mathbf{v}^{\top}\mathbf{u}$, $\mathbf{u}^{\top}(\mathbf{v}+\mathbf{q})$, $\mathbf{u}^{\top}\mathbf{v}+\mathbf{u}^{\top}\mathbf{q}$, $(3\mathbf{u})^{\top}\mathbf{v}$ et $\mathbf{u}^{\top}\mathbf{u}$. Quelle règle de calcul chaque comparaison met-elle en évidence ?

:::loesung
On a $\mathbf{u}^{\top}\mathbf{v}=3+0+2=5$ et $\mathbf{v}^{\top}\mathbf{u}=3+0+2=5$ : le produit scalaire est symétrique, c’est la règle (i). Avec $\mathbf{v}+\mathbf{q}=(3,\,1,\,2)^{\top}$, on a $\mathbf{u}^{\top}(\mathbf{v}+\mathbf{q})=3+0+4=7$, et $\mathbf{u}^{\top}\mathbf{v}+\mathbf{u}^{\top}\mathbf{q}=5+(0+0+2)=7$ : c’est la linéarité par rapport au second vecteur, la règle (ii). De plus, $(3\mathbf{u})^{\top}\mathbf{v}=(3,0,6)\,(3,-1,1)^{\top}=9+0+6=15=3\cdot5$, là encore la règle (ii). Enfin, $\mathbf{u}^{\top}\mathbf{u}=1+0+4=5>0$, comme l’exige la règle (iii) pour $\mathbf{u}\ne\mathbf{0}$.
:::
:::

:::aufgabe Exercice 5 ★★ L’estimation de l’agente immobilière
<span class="anker" id="aufg-5"></span>

Utilisez les poids $\mathbf{w}=(3,\,10,\,-4)^{\top}$ de la sous-section [2.2](#stufe-2-2).

<ol class="al">

<li>

Calculez les prédictions pour les quatre appartements. Quelle est leur unité ?

</li>

<li>

Dans l’appartement 2, on monte une cloison ; il a ensuite deux pièces pour la même surface. Comment la prédiction change-t-elle, et pourquoi la variation ne dépend-elle pas de la surface ?

</li>

<li>

Un collègue affirme : « Chez l’agente immobilière, ce sont les pièces qui comptent le plus, elles ont le plus grand poids. » Vérifiez cette affirmation sur l’appartement 1 en comparant les trois contributions $w_jx_{1j}$.

</li>

</ol>

:::loesung
(a) Comme dans la sous-section [2.2](#stufe-2-2) : $188$, $126$, $286$ et $232$, chaque fois en milliers d’euros. L’unité est le millier d’euros, parce que chaque poids a pour unité « milliers d’euros par unité de la caractéristique » et que l’unité de la caractéristique se simplifie dans le produit.

(b) L’appartement 2 devient $(40,\,2,\,1)^{\top}$. La prédiction passe de $126$ à $120+20-4=136$, elle augmente donc de $10$. En général, lorsque la deuxième caractéristique varie de $\Delta x_2$, la somme pondérée varie de $w_2\,\Delta x_2$, car $\mathbf{w}^{\top}(\mathbf{x}+\Delta x_2\,\mathbf{e}_2)=\mathbf{w}^{\top}\mathbf{x}+\Delta x_2\,\mathbf{w}^{\top}\mathbf{e}_2=\mathbf{w}^{\top}\mathbf{x}+\Delta x_2\,w_2$. Les autres caractéristiques n’y jouent aucun rôle. C’est la linéarité du produit scalaire : chaque caractéristique contribue pour elle-même, sans interaction avec les autres.

(c) Pour l’appartement 1, les contributions sont $w_1x_{11}=180$, $w_2x_{12}=20$ et $w_3x_{13}=-12$. C’est de loin la surface qui apporte la plus grande contribution, bien que son poids soit le plus petit en valeur absolue. L’affirmation du collègue confond le poids par unité et la contribution à la prédiction ; la surface compte un très grand nombre d’unités.
:::
:::

:::aufgabe Exercice 6 ★★ Un motif pour les signaux croissants
<span class="anker" id="aufg-6"></span>

Il s’agit de vérifier si un signal de quatre échantillons est croissant. On propose comme motif $\mathbf{w}=(-3,\,-1,\,1,\,3)^{\top}$.

<ol class="al">

<li>

Calculez $\mathbf{w}^{\top}\mathbf{x}$ pour $\mathbf{x}=(1,2,3,4)^{\top}$, $(4,3,2,1)^{\top}$, $(5,5,5,5)^{\top}$ et $(1,3,2,4)^{\top}$, et interprétez les résultats.

</li>

<li>

Pourquoi tout signal constant $c\,\mathbf1$ donne-t-il exactement zéro ? Utilisez $\mathbf 1^{\top}\mathbf{w}$.

</li>

</ol>

:::loesung
(a) $\mathbf{w}^{\top}(1,2,3,4)^{\top}=-3-2+3+12=10$ : le signal croît, le résultat est nettement positif. $\mathbf{w}^{\top}(4,3,2,1)^{\top}=-12-3+2+3=-10$ : le signal décroît, le résultat est tout aussi nettement négatif. $\mathbf{w}^{\top}(5,5,5,5)^{\top}=-15-5+5+15=0$ : constant, pas de croissance. $\mathbf{w}^{\top}(1,3,2,4)^{\top}=-3-3+2+12=8$ : le signal croît dans l’ensemble, avec un retour en arrière au milieu, et le résultat est un peu plus petit que pour la croissance régulière. Le motif pondère négativement les premières valeurs et positivement les dernières ; il réagit donc selon que les dernières valeurs sont plus grandes que les premières ou non.

(b) $\mathbf 1^{\top}\mathbf{w}=-3-1+1+3=0$. Pour un signal constant, on a donc $\mathbf{w}^{\top}(c\,\mathbf 1)=c\,\mathbf{w}^{\top}\mathbf 1=c\cdot0=0$. Comme la somme des poids est nulle, le motif ignore complètement une composante continue commune : il ne mesure que des différences entre les échantillons.
:::
:::

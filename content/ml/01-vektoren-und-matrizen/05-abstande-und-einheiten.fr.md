---
title: Distances et unités
pfad: Informatique / Apprentissage automatique / Fondements mathématiques / Vecteurs et matrices
knoten: Fondements 1 : Vecteurs et matrices
nachschlagen: ja
order: 15210500
summary: Deux exemples se ressemblent lorsque leurs vecteurs sont proches l’un de l’autre.
tags: distance, colonne de la caractéristique, centré, écart type, standardise
lang: fr
---

<span class="anker" id="stufe-4"></span>

:::zweck
Deux exemples se ressemblent lorsque leurs vecteurs sont proches l’un de l’autre. Cette section mesure des distances, montre que le résultat dépend des unités choisies et présente une méthode qui rend les caractéristiques comparables.
:::

### La distance entre deux points de données

<span class="anker" id="stufe-4-1"></span>

Deux appartements se ressemblent s’ils ne diffèrent que peu pour toutes les caractéristiques. Les différences figurent dans le vecteur différence $\mathbf{u}-\mathbf{v}$, la flèche qui va d’un point à l’autre. La grandeur de cette flèche est donnée par une norme.

:::definition Définition 4.1 (Distance)
<span class="anker" id="satz-4-1"></span>

La __distance__ entre deux vecteurs $\mathbf{u},\mathbf{v}\in\mathbb{R}^d$ relativement à une norme est la norme de leur différence, $\lVert\mathbf{u}-\mathbf{v}\rVert$. Sans autre précision, il s’agit de la distance euclidienne.
:::

Des propriétés d’une norme découlent les propriétés que l’on attend d’une distance : elle n’est jamais négative et n’est nulle que pour des points égaux ; elle est aussi grande de $\mathbf{u}$ à $\mathbf{v}$ que de $\mathbf{v}$ à $\mathbf{u}$, parce que $\mathbf{v}-\mathbf{u}=-(\mathbf{u}-\mathbf{v})$ ; et le chemin passant par un troisième point $\mathbf{q}$ n’est jamais plus court, $\lVert\mathbf{u}-\mathbf{v}\rVert\le\lVert\mathbf{u}-\mathbf{q}\rVert+\lVert\mathbf{q}-\mathbf{v}\rVert$. C’est l’inégalité triangulaire (N3), appliquée à $\mathbf{u}-\mathbf{v}=(\mathbf{u}-\mathbf{q})+(\mathbf{q}-\mathbf{v})$.

**Distance et produit scalaire.** En développant le carré de la distance euclidienne avec les règles de calcul du produit scalaire, on obtient

<span class="anker" id="gl-4-1"></span>
$$\lVert\mathbf{u}-\mathbf{v}\rVert^2=(\mathbf{u}-\mathbf{v})^{\top}(\mathbf{u}-\mathbf{v})=\lVert\mathbf{u}\rVert^2+\lVert\mathbf{v}\rVert^2-2\,\mathbf{u}^{\top}\mathbf{v} . \tag{4.1}$$

À longueurs fixées, on a donc : plus le produit scalaire est grand, plus la distance est petite. Tous deux mesurent la ressemblance, mais en sens opposés.

⁠**Exemple de calcul :** Les appartements 1 et 2 diffèrent de $\mathbf{x}_1-\mathbf{x}_2=(20,\,1,\,2)^{\top}$. Leur distance euclidienne vaut $\sqrt{405}\approx20{,}12$ (Fig. [18](#abb-18)), leur distance en norme 1 vaut $20+1+2=23$, et en norme du maximum $20$.

:::abbildung ml/k1rabstand 18
La distance euclidienne entre les appartements 1 et 2 : d’abord la différence, puis sa longueur.
:::

Vérification de [(4.1)](#gl-4-1) avec $\mathbf{u}=(1,\,2,\,2)^{\top}$ et $\mathbf{v}=(2,\,0,\,1)^{\top}$ : à gauche $\lVert(-1,\,2,\,1)^{\top}\rVert^2=6$, à droite $9+5-2\cdot4=6$.

⁠**En bref :** La distance entre deux points de données est la norme de leur différence ; proches signifie semblables.

### Les distances dépendent des unités

<span class="anker" id="stufe-4-2"></span>

Dans l’exemple de calcul qui précède, la distance $20{,}12$ correspond presque exactement à la différence de surface de $20\,\mathrm m^2$. Sur les $405$ du carré de la distance, $400$ proviennent de la surface. La différence d’une pièce et de deux kilomètres ne joue pratiquement aucun rôle, et ce uniquement parce que les surfaces exprimées en mètres carrés sont de grands nombres.

Trois autres appartements montrent ce qui en découle. La question est de savoir lequel des appartements B et C ressemble le plus à l’appartement A :

$$\text{A}=(60,\,2)^{\top},\qquad \text{B}=(63,\,4)^{\top},\qquad \text{C}=(54,\,2)^{\top}\qquad(\text{surface en m}^2,\ \text{pièces}).$$

En mètres carrés, $\lVert\text{A}-\text{B}\rVert=\sqrt{9+4}\approx3{,}61$ et $\lVert\text{A}-\text{C}\rVert=\sqrt{36+0}=6$ : B est plus proche. Si l’on mesure la surface en unités de $10\,\mathrm m^2$, on a $\text{A}=(6,\,2)^{\top}$, $\text{B}=(6{,}3;\ 4)^{\top}$, $\text{C}=(5{,}4;\ 2)^{\top}$ et $\lVert\text{A}-\text{B}\rVert=\sqrt{0{,}09+4}\approx2{,}02$, $\lVert\text{A}-\text{C}\rVert=0{,}6$ : c’est maintenant C qui est plus proche. La figure [19](#abb-19) montre les deux images.

:::abbildung ml/k1einheiten 19
Les trois mêmes appartements, à gauche avec la surface en $\mathrm m^2$, à droite en unités de $10\,\mathrm m^2$. Les deux axes d’une même image ont la même échelle, de sorte que la longueur d’un segment est la distance euclidienne. À gauche, c’est B qui est le plus proche de A (en tirets, le cercle de centre A passant par B), à droite c’est C.
:::

Le mécanisme est simple. Le carré de la distance contient, pour chaque caractéristique, la différence élevée au carré. Si l’on mesure une caractéristique dans une autre unité, ses nombres sont multipliés par un facteur $c$, et sa contribution au carré de la distance par $c^2$. Les contributions des autres caractéristiques restent les mêmes. Une caractéristique aux grands nombres détermine presque à elle seule la distance, une caractéristique aux petits nombres est presque noyée.

⁠**En bref :** Les distances entre exemples dépendent des unités des caractéristiques ; l’exemple qui ressemble le plus à un autre peut changer avec un changement d’unité.

:::hintergrund Tout choix d’unités est une pondération
La distance euclidienne additionne des carrés de mètres carrés, de pièces et de kilomètres. Du point de vue du calcul, c’est possible, parce que l’ordinateur ne voit que des nombres. Physiquement, c’est une somme de grandeurs de natures différentes, et les unités décident du poids de chacune. Qui indique la surface en $\mathrm m^2$ a ainsi décidé, sans le vouloir, que $1\,\mathrm m^2$ de différence compte autant qu’une pièce de différence. Il n’existe pas de bon choix imposé par la nature. Il faut le faire consciemment, et la méthode qui suit est un tel choix conscient.
:::

### Les écarts à la moyenne

<span class="anker" id="stufe-4-3"></span>

Pour rendre les caractéristiques comparables, on considère chaque caractéristique séparément, sur l’ensemble des exemples. Dans le tableau [1](vektoren-daten-als-zahlenlisten.html#tab-1), ce sont les colonnes : les surfaces de tous les appartements forment le vecteur $\mathbf{v}=(60,\,40,\,90,\,70)^{\top}\in\mathbb{R}^4$. Un tel vecteur appartient à une caractéristique et a autant de composantes qu’il y a d’exemples. On l’appelle ici la __colonne de la caractéristique__.

Pour la comparaison, ce n’est pas la grandeur des surfaces qui compte, mais l’ampleur de leurs différences. On mesure donc chaque surface comme un écart à la moyenne. En électrotechnique, cette étape s’appelle : retirer la composante continue et ne garder que la composante alternative.

:::definition Définition 4.2 (Vecteur centré)
<span class="anker" id="satz-4-2"></span>

Pour $\mathbf{v}\in\mathbb{R}^N$ de moyenne $\bar v$, on appelle

<span class="anker" id="gl-4-2"></span>
$$\tilde{\mathbf{v}}=\mathbf{v}-\bar v\,\mathbf 1=(v_1-\bar v,\,\dots,\,v_N-\bar v)^{\top} \tag{4.2}$$

le vecteur __centré__. Ses composantes sont les écarts à la moyenne.
:::

Les écarts se compensent toujours : $\mathbf 1^{\top}\tilde{\mathbf{v}}=\mathbf 1^{\top}\mathbf{v}-\bar v\,\mathbf 1^{\top}\mathbf 1=N\bar v-\bar v\,N=0$. Le vecteur centré a donc une moyenne nulle.

⁠**Exemple de calcul :** Les surfaces $\mathbf{v}=(60,\,40,\,90,\,70)^{\top}$ ont pour moyenne $\bar v=65$. Le vecteur centré est $\tilde{\mathbf{v}}=(-5,\,-25,\,25,\,5)^{\top}$, et la somme des écarts est effectivement nulle (Fig. [20](#abb-20)). Les nombres de pièces $(2,\,1,\,4,\,3)^{\top}$ ont pour moyenne $2{,}5$ et, centrés, donnent $(-0{,}5;\ -1{,}5;\ 1{,}5;\ 0{,}5)^{\top}$ ; les distances $(3,\,1,\,6,\,2)^{\top}$ ont pour moyenne $3$ et, centrées, donnent $(0,\,-2,\,3,\,-1)^{\top}$.

:::abbildung ml/k1rzentriert 20
La moyenne des surfaces et la somme des écarts à la moyenne, en $\mathrm m^2$.
:::

⁠**En bref :** Centrer retranche la moyenne de chaque composante ; il reste les écarts, dont la somme est nulle.

### L’écart type

<span class="anker" id="stufe-4-4"></span>

L’ampleur des variations d’une caractéristique se voit à la grandeur de ses écarts. Une valeur absolue typique d’une composante est la valeur efficace de la sous-section [3.6](normen-die-groe-eines-vektors.html#stufe-3-6). Appliquée au vecteur centré, elle donne l’écart typique à la moyenne. Dans le langage de l’électrotechnique : la valeur efficace de la composante alternative.

:::definition Définition 4.3 (Écart type)
<span class="anker" id="satz-4-3"></span>

L’__écart type__ d’un vecteur $\mathbf{v}\in\mathbb{R}^N$ est la valeur efficace de son vecteur centré :

<span class="anker" id="gl-4-3"></span>
$$\operatorname{std}(\mathbf{v})=\operatorname{rms}(\tilde{\mathbf{v}})=\frac{\lVert\mathbf{v}-\bar v\,\mathbf 1\rVert}{\sqrt N}=\sqrt{\frac1N\sum_{i=1}^N(v_i-\bar v)^2} . \tag{4.3}$$
:::

L’écart type a la même unité que la caractéristique. Il est nul si et seulement si toutes les composantes sont égales. De nombreux textes divisent, dans [(4.3)](#gl-4-3), par $N-1$ au lieu de $N$. Avec beaucoup d’exemples, la différence est faible. Cette série divise par $N$ et le précise lorsqu’il doit en être autrement.

⁠**Exemple de calcul :** Les surfaces centrées $(-5,\,-25,\,25,\,5)^{\top}$ ont pour somme des carrés $1\,300$, donc $\operatorname{std}(\mathbf{v})=\sqrt{325}\approx18{,}03\,\mathrm m^2$ (Fig. [21](#abb-21)). De même, on obtient pour les pièces $\sqrt{5/4}\approx1{,}118$ et pour les distances $\sqrt{14/4}\approx1{,}871$ km.

:::abbildung ml/k1rstd 21
L’écart type des surfaces : élever les écarts au carré, en faire la moyenne, extraire la racine. Le résultat $\sqrt{325}\approx18{,}03$ s’exprime en $\mathrm m^2$.
:::

⁠**En bref :** L’écart type est la valeur efficace des écarts à la moyenne, la variation typique d’une caractéristique.

:::hintergrund La composante continue et la composante alternative se partagent la puissance
Un vecteur est la somme de sa composante continue $\bar v\,\mathbf 1$ et de sa composante alternative $\tilde{\mathbf{v}}$. Pour le carré de la longueur, les règles de calcul du produit scalaire donnent

$$\lVert\bar v\,\mathbf 1+\tilde{\mathbf{v}}\rVert^2=\bar v^2\,\mathbf 1^{\top}\mathbf 1+2\,\bar v\,\mathbf 1^{\top}\tilde{\mathbf{v}}+\lVert\tilde{\mathbf{v}}\rVert^2=N\bar v^2+0+\lVert\tilde{\mathbf{v}}\rVert^2 ,$$

parce que la somme des écarts est nulle. En divisant par $N$, on obtient $\operatorname{rms}(\mathbf{v})^2=\bar v^2+\operatorname{std}(\mathbf{v})^2$. C’est la même décomposition que pour un courant mixte, dont la puissance dans une résistance se compose de la puissance de la composante continue et de celle de la composante alternative. Pour les surfaces : $\operatorname{rms}^2=(3600+1600+8100+4900)/4=4550=65^2+325$.
:::

### Standardiser

<span class="anker" id="stufe-4-5"></span>

On peut maintenant mesurer chaque caractéristique à l’aune de sa propre variation typique. Au lieu de « $25\,\mathrm m^2$ au-dessus de la moyenne », on dit « $1{,}39$ écart type au-dessus de la moyenne ». Dans ce langage, toutes les caractéristiques ont le même ordre de grandeur, quelle que soit l’unité dans laquelle elles ont été mesurées à l’origine.

:::definition Définition 4.4 (Standardiser)
<span class="anker" id="satz-4-4"></span>

On __standardise__ (on centre et on réduit) une caractéristique $j$, dont la colonne a pour moyenne $\bar x_j$ et pour écart type $s_j>0$, en remplaçant chaque valeur par

<span class="anker" id="gl-4-4"></span>
$$z_{ij}=\frac{x_{ij}-\bar x_j}{s_j},\qquad i=1,\dots,N, \tag{4.4}$$

et l’on appelle les nombres $z_{ij}$ les valeurs standardisées.
:::

La colonne standardisée a pour moyenne $0$ et pour écart type $1$, car le centrage rend la moyenne nulle et la division par $s_j$ ramène l’écart typique à un. Les valeurs n’ont plus d’unité.

⁠**Exemple de calcul 1 : le jeu de données des appartements.** Avec les moyennes $65$, $2{,}5$, $3$ et les écarts types $18{,}03$, $1{,}118$, $1{,}871$, les quatre appartements deviennent

$$\begin{aligned} \mathbf{z}_1&\approx(-0{,}28;\ -0{,}45;\ 0)^{\top}, & \mathbf{z}_2&\approx(-1{,}39;\ -1{,}34;\ -1{,}07)^{\top},\\ \mathbf{z}_3&\approx(1{,}39;\ 1{,}34;\ 1{,}60)^{\top}, & \mathbf{z}_4&\approx(0{,}28;\ 0{,}45;\ -0{,}53)^{\top}. \end{aligned}$$

Les trois caractéristiques se situent maintenant dans la même plage de valeurs.

⁠**Exemple de calcul 2 : A, B et C.** Les trois appartements de la sous-section [4.2](#stufe-4-2) ont une surface moyenne de $59\,\mathrm m^2$, avec un écart type de $\sqrt{14}\approx3{,}74\,\mathrm m^2$, et en moyenne $8/3$ pièces, avec un écart type de $\sqrt{8/9}\approx0{,}943$. Après standardisation, $\lVert\text A-\text B\rVert\approx2{,}27$ et $\lVert\text A-\text C\rVert\approx1{,}60$. C’est donc à C que A ressemble le plus, et ce jugement ne dépend plus de l’unité de la surface.

Le fait que l’unité disparaisse est vrai en général :

:::satz Théorème 4.5 (Les valeurs standardisées ne dépendent pas de l’unité)
<span class="anker" id="satz-4-5"></span>

Si l’on convertit une caractéristique dans une autre unité, $v_i'=\alpha\,v_i+\beta$ pour tout $i$, avec des nombres $\alpha>0$ et $\beta$, ses valeurs standardisées restent les mêmes.
:::

:::beweis Indépendance vis-à-vis de l’unité
La moyenne devient $\bar v'=\frac1N\sum_i(\alpha\,v_i+\beta)=\alpha\,\bar v+\beta$, et les écarts $v_i'-\bar v'=\alpha\,(v_i-\bar v)$. D’après [(4.3)](#gl-4-3), on a alors $\operatorname{std}(\mathbf{v}')=|\alpha|\operatorname{std}(\mathbf{v})=\alpha\operatorname{std}(\mathbf{v})$. Dans le quotient [(4.4)](#gl-4-4), $\alpha$ se simplifie, et $\beta$ a déjà disparu lors du centrage.
:::

Le terme $\beta$ couvre aussi les conversions avec un zéro décalé, par exemple des degrés Celsius en degrés Fahrenheit.

⁠**En bref :** Standardiser mesure chaque caractéristique comme un écart à la moyenne, en multiples de son écart type ; ensuite, les distances ne dépendent plus des unités.

:::hintergrund Pourquoi justement l’écart type comme étalon ?
Il faut pour chaque caractéristique un étalon qui, lors d’un changement d’unité, change du même facteur que les différences entre les valeurs. Il se simplifie alors. Toute grandeur calculée à partir des différences entre les valeurs de la caractéristique et ayant l’unité de la caractéristique remplit ce rôle : l’écart type, mais aussi l’étendue, de la plus petite à la plus grande valeur. L’écart type est le choix habituel, parce qu’il tient compte de toutes les valeurs et pas seulement des deux extrêmes.

Ce que la standardisation fait d’une distance se voit lorsqu’on soustrait l’un de l’autre deux exemples standardisés $\mathbf{z}_a$ et $\mathbf{z}_b$. La moyenne disparaît, $z_{aj}-z_{bj}=(x_{aj}-x_{bj})/s_j$, et il reste

$$\lVert\mathbf{z}_a-\mathbf{z}_b\rVert^2=\sum_{j=1}^d\frac{(x_{aj}-x_{bj})^2}{s_j^2} .$$

La distance des valeurs standardisées est donc la distance ordinaire dans laquelle la différence au carré pour la caractéristique $j$ compte avec le poids $1/s_j^2$. Pour les appartements A et B, cela donne $3^2/14+2^2/(8/9)=9/14+9/2\approx5{,}14$, dont la racine vaut $2{,}27$, comme plus haut.

Mais la standardisation est elle-même une décision. Elle donne à chaque caractéristique le même poids dans la distance, même à une caractéristique qui ne joue aucun rôle pour la question posée. Et une caractéristique qui a la même valeur pour tous les exemples a un écart type nul et ne peut pas être standardisée ; mais elle ne distingue pas non plus les exemples et ne contribue à aucune distance.
:::

:::aufgabe Exercice 9 ★ Composante continue et composante alternative
<span class="anker" id="aufg-9"></span>

Un signal a pour échantillons $\mathbf{x}=(1,\,3,\,1,\,-1)^{\top}$. Calculez la moyenne, le vecteur centré, l’écart type et la valeur efficace. Vérifiez que $\operatorname{rms}(\mathbf{x})^2=\bar x^2+\operatorname{std}(\mathbf{x})^2$.

:::loesung
La moyenne vaut $\bar x=(1+3+1-1)/4=1$, le vecteur centré est $\tilde{\mathbf{x}}=(0,\,2,\,0,\,-2)^{\top}$. L’écart type vaut $\sqrt{(0+4+0+4)/4}=\sqrt2\approx1{,}414$, la valeur efficace $\sqrt{(1+9+1+1)/4}=\sqrt3\approx1{,}732$. Vérification : $\operatorname{rms}^2=3=1^2+(\sqrt2)^2=\bar x^2+\operatorname{std}^2$. La composante continue et la composante alternative se partagent la « puissance » $3$ dans le rapport $1:2$.
:::
:::

:::aufgabe Exercice 10 ★★ Quel appartement ressemble le plus à l’appartement 1 ?
<span class="anker" id="aufg-10"></span>

<ol class="al">

<li>

Calculez les distances euclidiennes de l’appartement 1 aux appartements 2, 3 et 4 avec les valeurs du tableau [1](vektoren-daten-als-zahlenlisten.html#tab-1). Quelle part du carré de la distance à l’appartement 2 provient de la surface ?

</li>

<li>

Calculez les mêmes distances avec les valeurs standardisées de la sous-section [4.5](#stufe-4-5). Quelle part du carré de la distance à l’appartement 2 provient maintenant de la surface ?

</li>

<li>

Quel appartement ressemble chaque fois le plus à l’appartement 1 ? Qu’est-ce que la standardisation a changé ici, si ce n’est pas la réponse ?

</li>

</ol>

:::loesung
(a) Avec les valeurs du tableau :

$$\begin{aligned} \lVert\mathbf{x}_1-\mathbf{x}_2\rVert&=\sqrt{20^2+1^2+2^2}=\sqrt{405}\approx20{,}12,\\ \lVert\mathbf{x}_1-\mathbf{x}_3\rVert&=\sqrt{30^2+2^2+3^2}=\sqrt{913}\approx30{,}22,\\ \lVert\mathbf{x}_1-\mathbf{x}_4\rVert&=\sqrt{10^2+1^2+1^2}=\sqrt{102}\approx10{,}10 . \end{aligned}$$

Sur les $405$ du carré de la distance à l’appartement 2, $400$ proviennent de la surface, soit $98{,}8$ %.

(b) Avec les vecteurs standardisés de la sous-section [4.5](#stufe-4-5), on a $\mathbf{z}_1-\mathbf{z}_2\approx(1{,}109;\ 0{,}894;\ 1{,}069)^{\top}$, de carrés $1{,}231$, $0{,}800$ et $1{,}143$. La distance vaut $\sqrt{3{,}174}\approx1{,}78$. On obtient de même $\lVert\mathbf{z}_1-\mathbf{z}_3\rVert\approx2{,}92$ et $\lVert\mathbf{z}_1-\mathbf{z}_4\rVert\approx1{,}18$. La part de la surface dans le carré de la distance à l’appartement 2 est maintenant de $1{,}231/3{,}174\approx38{,}8$ %.

(c) Dans les deux cas, l’appartement 4 est le plus semblable, suivi de l’appartement 2, puis de l’appartement 3. L’ordre ne change pas ici, parce que, dans ce petit jeu de données, les grands appartements ont aussi plus de pièces et sont plus éloignés du centre ; les trois caractéristiques racontent à peu près la même histoire. Ce qui a changé, c’est *pourquoi* l’appartement 4 est le plus semblable : avec les valeurs brutes, la surface décide presque à elle seule ; après standardisation, les trois caractéristiques contribuent à peu près autant. Que la réponse reste malgré tout la même est un hasard de ces données ; pour les appartements A, B et C de la sous-section [4.2](#stufe-4-2), elle a changé.
:::
:::

:::aufgabe Exercice 11 ★★ Celsius ou Fahrenheit
<span class="anker" id="aufg-11"></span>

Sur quatre jours, on a mesuré à midi $10$, $20$, $15$ et $25$ $^\circ$C.

<ol class="al">

<li>

Convertissez en degrés Fahrenheit ($F=1{,}8\,C+32$). Calculez dans les deux unités la moyenne et l’écart type.

</li>

<li>

Calculez les valeurs standardisées dans les deux unités et comparez.

</li>

<li>

Qu’advient-il des valeurs standardisées si l’on convertit une caractéristique avec un facteur négatif, par exemple $v_i'=-v_i$ ?

</li>

</ol>

:::loesung
(a) En degrés Fahrenheit, les valeurs sont $1{,}8\cdot10+32=50$, $68$, $59$ et $77$. En degrés Celsius, la moyenne vaut $17{,}5$ et l’écart type $\sqrt{(56{,}25+6{,}25+6{,}25+56{,}25)/4}=\sqrt{31{,}25}\approx5{,}590$ ; en degrés Fahrenheit, la moyenne vaut $63{,}5=1{,}8\cdot17{,}5+32$ et l’écart type $\approx10{,}062=1{,}8\cdot5{,}590$. Le terme additif $32$ ne fait que décaler la moyenne, le facteur $1{,}8$ étire aussi l’écart type.

(b) Dans les deux unités, les valeurs standardisées valent $\approx(-1{,}342;\ 0{,}447;\ -0{,}447;\ 1{,}342)$. C’est ce qu’exige le théorème de la sous-section [4.5](#stufe-4-5) : le terme additif disparaît lors du centrage, le facteur se simplifie avec l’écart type.

(c) Avec $v_i'=-v_i$, tous les écarts à la moyenne sont multipliés par $-1$, mais l’écart type par $|-1|=1$. Les valeurs standardisées changent donc de signe. Pour les distances entre exemples, cela n’a aucune importance, car $\lVert-\mathbf{u}\rVert=\lVert\mathbf{u}\rVert$ ; le jeu de données subit seulement une réflexion.
:::
:::

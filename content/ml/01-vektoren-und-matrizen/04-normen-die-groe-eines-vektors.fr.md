---
title: Normes : la grandeur d’un vecteur
pfad: Informatique / Apprentissage automatique / Fondements mathématiques / Vecteurs et matrices
knoten: Fondements 1 : Vecteurs et matrices
nachschlagen: ja
order: 15210400
summary: Quelle est la grandeur d’un vecteur ?
tags: norme euclidienne, longueur, normé, normer, norme 1, norme du maximum, norme, inégalité triangulaire
lang: fr
---

<span class="anker" id="stufe-3"></span>

:::zweck
Quelle est la grandeur d’un vecteur ? Il existe plusieurs réponses justes à cette question. Cette section présente les trois plus importantes, explique ce qu’elles ont en commun et montre à quoi elles servent : à mesurer la grandeur d’une erreur.
:::

### La norme euclidienne

<span class="anker" id="stufe-3-1"></span>

La grandeur la plus naturelle d’une flèche est sa longueur. Dans le plan, le théorème de Pythagore la fournit : la flèche $(3,\,-4)^{\top}$ est l’hypoténuse d’un triangle rectangle dont les côtés de l’angle droit mesurent $3$ et $4$ ; elle a donc pour longueur $\sqrt{3^2+4^2}=5$. Dans l’espace, on applique deux fois Pythagore et l’on obtient la racine de la somme des trois carrés. On utilise la même formule en toute dimension.

:::definition Définition 3.1 (Norme euclidienne)
<span class="anker" id="satz-3-1"></span>

La __norme euclidienne__ d’un vecteur $\mathbf{x}\in\mathbb{R}^d$ est

<span class="anker" id="gl-3-1"></span>
$$\lVert\mathbf{x}\rVert_2=\sqrt{\mathbf{x}^{\top}\mathbf{x}}=\sqrt{x_1^2+x_2^2+\dots+x_d^2} . \tag{3.1}$$

Sans indice, $\lVert\mathbf{x}\rVert$ désigne toujours, dans cette série, la norme euclidienne.
:::

On l’appelle aussi la __longueur__ du vecteur ou, à cause des carrés, la norme $L_2$. Un vecteur de longueur $1$ est dit __normé__. Si l’on divise un vecteur $\mathbf{x}\ne\mathbf{0}$ par sa longueur, $\mathbf{x}/\lVert\mathbf{x}\rVert$ est normé et pointe dans la même direction. Cette opération s’appelle __normer__.

⁠**Exemple de calcul :** Le vecteur $\mathbf{x}=(3,\,-4)^{\top}$ a pour longueur $\lVert\mathbf{x}\rVert_2=5$ (Fig. [12](#abb-12)). Normé, il devient $\mathbf{x}/5=(0{,}6;\ -0{,}8)^{\top}$. Dans l’espace, $\lVert(1,\,2,\,2)^{\top}\rVert=\sqrt{1+4+4}=3$.

:::abbildung ml/k1rl2 12
La norme euclidienne de $(3,\,-4)^{\top}$ : élever les composantes au carré, additionner, extraire la racine. Le signe moins disparaît lors de l’élévation au carré.
:::

⁠**En bref :** La norme euclidienne est la longueur de la flèche, la racine de la somme des carrés des composantes.

### La norme 1

<span class="anker" id="stufe-3-2"></span>

Dans une ville au réseau de rues à angles droits, un taxi ne peut pas traverser les pâtés de maisons en diagonale. Pour aller de l’origine au point $(3,\,-4)^{\top}$, il parcourt $3$ pâtés dans une direction et $4$ pâtés dans l’autre, soit $7$ pâtés au total. C’est cette longueur que mesure la norme 1.

:::definition Définition 3.2 (Norme 1)
<span class="anker" id="satz-3-2"></span>

La __norme 1__ d’un vecteur $\mathbf{x}\in\mathbb{R}^d$ est

<span class="anker" id="gl-3-2"></span>
$$\lVert\mathbf{x}\rVert_1=|x_1|+|x_2|+\dots+|x_d|=\sum_{j=1}^d|x_j| . \tag{3.2}$$
:::

On l’appelle aussi norme $L_1$ ou, d’après le réseau de rues de Manhattan, norme de Manhattan.

⁠**Exemple de calcul :** Pour $\mathbf{x}=(3,\,-4)^{\top}$, on a $\lVert\mathbf{x}\rVert_1=7$ (Fig. [13](#abb-13)), et $\lVert(1,\,2,\,2)^{\top}\rVert_1=1+2+2=5$.

:::abbildung ml/k1rl1 13
La norme 1 de $\mathbf{x}=(3,\,-4)^{\top}$ : additionner les valeurs absolues des composantes.
:::

Ici, la norme 1 est plus grande que la longueur euclidienne, parce que le détour par les rues est plus long que le trajet à vol d’oiseau.

⁠**En bref :** La norme 1 additionne les valeurs absolues des composantes ; c’est le trajet à travers un réseau de rues à angles droits.

### La norme du maximum

<span class="anker" id="stufe-3-3"></span>

Lors d’un contrôle qualité, c’est souvent le pire écart seul qui compte. Une pièce mécanique a trois cotes, et chacune peut s’écarter d’au plus $0{,}1$ mm de sa valeur nominale. Seul le plus grand des trois écarts décide si la pièce est conforme.

:::definition Définition 3.3 (Norme du maximum)
<span class="anker" id="satz-3-3"></span>

La __norme du maximum__ d’un vecteur $\mathbf{x}\in\mathbb{R}^d$ est la plus grande valeur absolue d’une composante :

<span class="anker" id="gl-3-3"></span>
$$\lVert\mathbf{x}\rVert_\infty=\max_{j=1,\dots,d}|x_j| . \tag{3.3}$$
:::

On l’appelle aussi norme $L_\infty$. La raison du symbole infini est donnée dans la sous-section suivante.

⁠**Exemple de calcul :** $\lVert(3,\,-4)^{\top}\rVert_\infty=4$ et $\lVert(1,\,2,\,2)^{\top}\rVert_\infty=2$. Si les écarts d’une pièce sont de $(0{,}05;\ -0{,}08;\ 0{,}02)$ mm, leur norme du maximum vaut $0{,}08$ mm, et la pièce est conforme.

⁠**En bref :** La norme du maximum est la plus grande valeur absolue d’une composante, le pire écart individuel.

### Ce qui fait une norme

<span class="anker" id="stufe-3-4"></span>

Les trois normes mesurent différemment, mais elles ont en commun trois propriétés que l’on attend de toute mesure de grandeur. Seul le vecteur nul a une grandeur nulle. Un vecteur deux fois plus long est deux fois plus grand. Et un détour n’est jamais plus court que le chemin direct.

:::definition Définition 3.4 (Norme)
<span class="anker" id="satz-3-4"></span>

Une __norme__ sur $\mathbb{R}^d$ associe à chaque vecteur $\mathbf{x}$ un nombre réel $\lVert\mathbf{x}\rVert$, de sorte que pour tous $\mathbf{u},\mathbf{v},\mathbf{x}\in\mathbb{R}^d$ et tous les scalaires $c$ :

<ol>

<li>

$\lVert\mathbf{x}\rVert\ge0$, et $\lVert\mathbf{x}\rVert=0$ seulement pour $\mathbf{x}=\mathbf{0}$ ;

</li>

<li>

$\lVert c\,\mathbf{x}\rVert=|c|\,\lVert\mathbf{x}\rVert$ ;

</li>

<li>

$\lVert\mathbf{u}+\mathbf{v}\rVert\le\lVert\mathbf{u}\rVert+\lVert\mathbf{v}\rVert$ (__inégalité triangulaire__).

</li>

</ol>
:::

L’inégalité triangulaire doit son nom au triangle formé par les flèches $\mathbf{u}$, $\mathbf{v}$ et $\mathbf{u}+\mathbf{v}$ : le côté $\mathbf{u}+\mathbf{v}$ n’est jamais plus long que les deux autres réunis.

**Les normes $p$.** La norme 1 et la norme euclidienne sont deux cas d’une famille entière. Pour tout nombre $p\ge1$, la __norme $p$__ est

<span class="anker" id="gl-3-4"></span>
$$\lVert\mathbf{x}\rVert_p=\Bigl(\sum_{j=1}^d|x_j|^p\Bigr)^{1/p} . \tag{3.4}$$

Pour $p=1$, c’est la norme 1, pour $p=2$ la norme euclidienne. Plus $p$ est grand, plus la plus grande composante prédomine dans la somme. Pour $p\to\infty$, il ne reste qu’elle ; c’est pourquoi la norme du maximum se note $\lVert\cdot\rVert_\infty$.

**La sphère unité.** On voit comment une norme mesure en regardant l’ensemble de tous les vecteurs de grandeur $1$. On l’appelle la __sphère unité__ de la norme, même si elle n’est pas forcément ronde (Fig. [14](#abb-14)). Pour la norme euclidienne, c’est, dans le plan, le cercle de rayon $1$. Pour la norme 1, c’est le losange $|x_1|+|x_2|=1$ : dans chaque quadrant, c’est un segment, par exemple $x_1+x_2=1$ pour $x_1,x_2\ge0$. Pour la norme du maximum, c’est le carré de sommets $(\pm1,\,\pm1)$, car en chacun de ses points la plus grande des deux composantes vaut exactement $1$ en valeur absolue.

:::abbildung ml/k1einheitskugeln 14
Les sphères unités de trois normes dans le plan : le losange de la norme 1 (à gauche, en orange), le cercle de la norme euclidienne (au milieu, en bleu) et le carré de la norme du maximum (à droite, en vert) ; en gris, à chaque fois, les deux autres pour comparaison. Toutes trois passent par les points $(\pm1,\,0)$ et $(0,\,\pm1)$.
:::

⁠**Exemple de calcul :** Pour $\mathbf{x}=(3,\,-4)^{\top}$, on a $\lVert\mathbf{x}\rVert_1=7$, $\lVert\mathbf{x}\rVert_2=5$, $\lVert\mathbf{x}\rVert_3=91^{1/3}\approx4{,}498$, $\lVert\mathbf{x}\rVert_{10}=1\,107\,625^{1/10}\approx4{,}022$ (Fig. [15](#abb-15)) et $\lVert\mathbf{x}\rVert_\infty=4$. Quand $p$ croît, la norme $p$ se rapproche de la plus grande valeur absolue d’une composante, ici $4$. La raison se lit déjà dans la somme : pour $p=10$, $4^{10}$ est presque dix-huit fois plus grand que $3^{10}$, et la racine de la somme est à peine plus grande que la racine de $4^{10}$ seul.

:::abbildung ml/k1rlp 15
Deux normes $p$ de $\mathbf{x}=(3,\,-4)^{\top}$, pour $p=3$ et $p=10$. Plus $p$ est grand, plus le terme de la plus grande composante prédomine.
:::

Que la norme 1 satisfasse les conditions (N1) à (N3) se vérifie directement : (N1) et (N2) sont vraies parce que $|x_j|\ge0$ et $|c\,x_j|=|c|\,|x_j|$. (N3) découle de l’inégalité triangulaire pour les nombres, $|u_j+v_j|\le|u_j|+|v_j|$, sommée sur tous les $j$. Pour la norme du maximum, on procède de même. Pour la norme euclidienne, l’inégalité triangulaire est intuitivement évidente, parce que le chemin direct entre deux points n’est jamais plus long qu’un détour par un troisième point.

⁠**En bref :** Une norme mesure la grandeur d’un vecteur de sorte que seul le vecteur nul ait une grandeur nulle, que les multiples croissent en proportion et que l’inégalité triangulaire soit vérifiée ; les normes $p$ forment une famille à laquelle appartiennent $L_1$, $L_2$ et $L_\infty$.

:::hintergrund Pourquoi il faut $p\ge1$ et pourquoi la « norme zéro » n’est pas une norme
Pour $p<1$, la formule [(3.4)](#gl-3-4) viole l’inégalité triangulaire. Avec $p=\tfrac12$, on a $\lVert(1,0)^{\top}\rVert_{1/2}=1$ et $\lVert(0,1)^{\top}\rVert_{1/2}=1$, mais $\lVert(1,1)^{\top}\rVert_{1/2}=(1+1)^2=4>1+1$. Sa « sphère unité » est creusée vers l’intérieur ; elle a la forme d’une étoile.

On rencontre souvent le terme de « norme $L_0$ » : le nombre de composantes non nulles. C’est une mesure utile du nombre de caractéristiques qu’un vecteur utilise réellement. Ce n’est pourtant pas une norme, car elle viole (N2) : le vecteur $2\mathbf{x}$ a exactement autant de composantes non nulles que $\mathbf{x}$, et non deux fois plus.
:::

:::hintergrund Les normes ne proviennent pas toutes d’un produit scalaire
La norme euclidienne est construite à partir du produit scalaire, $\lVert\mathbf{x}\rVert^2=\mathbf{x}^{\top}\mathbf{x}$. Il en découle une égalité appelée identité du parallélogramme. En développant avec les règles de calcul du produit scalaire, on obtient

$$\lVert\mathbf{u}+\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2+2\,\mathbf{u}^{\top}\mathbf{v}+\lVert\mathbf{v}\rVert^2 ,\qquad \lVert\mathbf{u}-\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2-2\,\mathbf{u}^{\top}\mathbf{v}+\lVert\mathbf{v}\rVert^2 ,$$

et la somme des deux lignes donne $\lVert\mathbf{u}+\mathbf{v}\rVert^2+\lVert\mathbf{u}-\mathbf{v}\rVert^2=2\lVert\mathbf{u}\rVert^2+2\lVert\mathbf{v}\rVert^2$ : dans un parallélogramme, la somme des carrés des deux diagonales est égale à la somme des carrés des quatre côtés. Toute norme issue d’un produit scalaire doit satisfaire cette égalité. La norme 1 ne la satisfait pas : avec $\mathbf{u}=\mathbf{e}_1$ et $\mathbf{v}=\mathbf{e}_2$, on a à gauche $\lVert(1,1)^{\top}\rVert_1^2+\lVert(1,-1)^{\top}\rVert_1^2=4+4=8$, mais à droite $2+2=4$. Il n’existe donc aucun produit scalaire dont la longueur associée soit la norme 1. C’est pourquoi on ne peut pas mesurer avec elle des angles comme ceux que fournit le produit scalaire.
:::

### Le vecteur d’erreur et sa grandeur

<span class="anker" id="stufe-3-5"></span>

Un modèle fournit des prédictions, et tôt ou tard on apprend les valeurs réelles. On veut alors savoir à quel point les prédictions étaient bonnes. Pour chaque exemple, il y a un écart, et ces écarts forment un vecteur. Sa norme est une mesure de la grandeur de l’erreur dans son ensemble.

:::definition Définition 3.5 (Vecteur d’erreur)
<span class="anker" id="satz-3-5"></span>

Si $\hat y_1,\dots,\hat y_N$ sont les prédictions d’un modèle pour $N$ exemples et $y_1,\dots,y_N$ les valeurs réelles, on appelle le vecteur

<span class="anker" id="gl-3-5"></span>
$$\hat{\mathbf{y}}-\mathbf{y}=(\hat y_1-y_1,\,\dots,\,\hat y_N-y_N)^{\top} \tag{3.5}$$

le __vecteur d’erreur__. Ici, $\hat{\mathbf{y}}=(\hat y_1,\dots,\hat y_N)^{\top}$ est le vecteur des prédictions et $\mathbf{y}=(y_1,\dots,y_N)^{\top}$ le vecteur des valeurs réelles.
:::

Choisir la norme que l’on applique au vecteur d’erreur, c’est décider quelles erreurs l’on redoute le plus. Le signe n’y joue aucun rôle, car toute norme donne à $\mathbf{y}-\hat{\mathbf{y}}$ la même grandeur qu’à $\hat{\mathbf{y}}-\mathbf{y}$.

⁠**Exemple de calcul :** Les quatre appartements ont été vendus ; les prix réels étaient $\mathbf{y}=(200,\,130,\,290,\,240)^{\top}$, en milliers d’euros. Deux experts A et B avaient auparavant fait les estimations suivantes :

$$\hat{\mathbf{y}}_{\mathrm A}=(210,\,120,\,300,\,230)^{\top},\qquad \hat{\mathbf{y}}_{\mathrm B}=(200,\,130,\,290,\,280)^{\top}.$$

Leurs vecteurs d’erreur sont $\hat{\mathbf{y}}_{\mathrm A}-\mathbf{y}=(10,\,-10,\,10,\,-10)^{\top}$ et $\hat{\mathbf{y}}_{\mathrm B}-\mathbf{y}=(0,\,0,\,0,\,40)^{\top}$. L’expert A se trompe toujours un peu, l’expert B tombe juste trois fois et se trompe lourdement une fois. Les trois normes jugent différemment (tableau [2](#tab-2)). Les normes euclidiennes sont calculées dans la Fig. [16](#abb-16).

:::abbildung ml/k1rfehler 16
Les normes euclidiennes des deux vecteurs d’erreur, en milliers d’euros. Avec $1\,600$, l’unique grosse erreur de B contribue quatre fois plus à la somme des carrés que les quatre petites erreurs de A réunies.
:::

<span class="anker" id="tab-2"></span>

**Tableau 2 :** Les normes des vecteurs d’erreur de deux experts, en milliers d’euros.

|  | $\lVert\cdot\rVert_1$ | $\lVert\cdot\rVert_2$ | $\lVert\cdot\rVert_\infty$ |
|---|---|---|---|
| Expert A, $\hat{\mathbf{y}}_{\mathrm A}-\mathbf{y}$ | $40$ | $\sqrt{4\cdot100}=20$ | $10$ |
| Expert B, $\hat{\mathbf{y}}_{\mathrm B}-\mathbf{y}$ | $40$ | $\sqrt{1600}=40$ | $40$ |

Selon la norme 1, les deux sont aussi bons l’un que l’autre : tous deux se trompent au total de $40$ mille euros. Selon la norme euclidienne, A est deux fois meilleur, selon la norme du maximum quatre fois meilleur. Qui juge chaque millier d’euros d’écart aussi grave, quel que soit l’appartement, mesure avec $L_1$. Qui juge une grosse valeur aberrante plus grave que de nombreuses petites erreurs mesure avec $L_2$. Qui ne craint que le pire des cas mesure avec $L_\infty$.

⁠**En bref :** Le vecteur d’erreur rassemble les écarts de toutes les prédictions ; sa norme mesure la grandeur de l’erreur, et le choix de la norme détermine quelles erreurs comptent particulièrement.

:::hintergrund Pourquoi la somme des carrés punit les grosses erreurs et ignore presque les petites
Dans la norme euclidienne, chaque écart intervient au carré. Un écart de $0{,}1$ contribue pour $0{,}01$, un écart de $10$ en revanche pour $100$. Le carré rend les petits nombres plus petits et les grands nombres plus grands. Une seule grosse erreur de $40$ contribue donc pour $1600$, quatre fois plus que quatre erreurs de $10$ réunies. La norme 1, en revanche, croît partout à la même vitesse : chaque unité d’écart coûte autant, qu’elle appartienne à une petite ou à une grande erreur. C’est pourquoi elle fait aussi une nette différence entre « exactement zéro » et « un peu à côté », alors que la somme des carrés ne fait guère de différence entre les deux. La propriété souhaitée dépend de la tâche, et c’est précisément pour cela qu’il existe plusieurs normes.
:::

### La valeur efficace

<span class="anker" id="stufe-3-6"></span>

La norme euclidienne croît avec le nombre de composantes. Si l’on évalue un expert sur quatre appartements et un autre sur quatre cents, le second a un vecteur d’erreur beaucoup plus long, même s’il estime aussi bien appartement par appartement. Si l’on veut comparer des erreurs ramenées à un seul exemple, il faut éliminer l’effet du nombre de composantes.

:::definition Définition 3.6 (Valeur efficace)
<span class="anker" id="satz-3-6"></span>

La __valeur efficace__ d’un vecteur $\mathbf{x}\in\mathbb{R}^n$ est

<span class="anker" id="gl-3-6"></span>
$$\operatorname{rms}(\mathbf{x})=\frac{\lVert\mathbf{x}\rVert}{\sqrt n}=\sqrt{\frac1n\sum_{i=1}^nx_i^2} . \tag{3.6}$$
:::

L’abréviation rms signifie *root mean square* : la racine de la moyenne des carrés. La valeur efficace est une valeur absolue typique d’une composante. Si toutes les composantes ont la même valeur absolue $a$, la valeur efficace vaut exactement $a$.

Le nom est connu en électrotechnique : la valeur efficace d’une tension alternative est la racine de la moyenne temporelle de son carré. Pour un signal échantillonné, [(3.6)](#gl-3-6) est le même calcul, avec des échantillons au lieu d’une intégrale. Si l’on échantillonne une sinusoïde sur exactement une période en $n\ge3$ points régulièrement répartis, on obtient même exactement la valeur efficace $1/\sqrt2$ de la sinusoïde.

⁠**Exemple de calcul :** Les vecteurs d’erreur des experts de la sous-section précédente ont pour valeurs efficaces $\operatorname{rms}(\hat{\mathbf{y}}_{\mathrm A}-\mathbf{y})=20/\sqrt4=10$ et $\operatorname{rms}(\hat{\mathbf{y}}_{\mathrm B}-\mathbf{y})=40/\sqrt4=20$ mille euros : A se trompe typiquement de $10$ mille euros. Une sinusoïde d’amplitude $1$, échantillonnée en quatre points régulièrement répartis sur une période, a pour échantillons $\mathbf{x}=(0,\,1,\,0,\,-1)^{\top}$ et pour valeur efficace $1/\sqrt2\approx0{,}707$ (Fig. [17](#abb-17)).

:::abbildung ml/k1rrms 17
La valeur efficace d’une sinusoïde échantillonnée : additionner les carrés, diviser par le nombre de composantes, extraire la racine.
:::

⁠**En bref :** La valeur efficace $\lVert\mathbf{x}\rVert/\sqrt n$ est la valeur absolue typique d’une composante et rend comparables des vecteurs de longueurs différentes.

:::hintergrund Combien de composantes peuvent être grandes ?
La valeur efficace limite le nombre de composantes qui peuvent avoir une grande valeur absolue. Si $k$ des $n$ composantes ont une valeur absolue d’au moins $a>0$, ces $k$ composantes contribuent à elles seules au moins pour $k\,a^2$ à la somme des carrés. La somme des carrés complète vaut $n\operatorname{rms}(\mathbf{x})^2$, donc $k\,a^2\le n\operatorname{rms}(\mathbf{x})^2$, soit

$$\frac kn\le\Bigl(\frac{\operatorname{rms}(\mathbf{x})}{a}\Bigr)^2 .$$

Une proportion d’au plus $(\operatorname{rms}/a)^2$ des composantes peut donc atteindre au moins $a$ en valeur absolue. Au plus un quart des composantes peut atteindre le double de la valeur efficace, au plus un pour cent dix fois la valeur efficace. Pour l’expert B, avec $\operatorname{rms}=20$, au plus $(20/30)^2=4/9\approx44$ % des erreurs peuvent valoir $30$ ou plus ; en réalité, c’est une sur quatre, soit $25$ %. Cette majoration s’appelle l’inégalité de Bienaymé-Tchebychev.
:::

:::aufgabe Exercice 7 ★ Calculer des normes
<span class="anker" id="aufg-7"></span>

Soit $\mathbf{x}=(2,\,-1,\,0,\,2)^{\top}$.

<ol class="al">

<li>

Calculez $\lVert\mathbf{x}\rVert_1$, $\lVert\mathbf{x}\rVert_2$, $\lVert\mathbf{x}\rVert_3$ et $\lVert\mathbf{x}\rVert_\infty$ ainsi que le vecteur normé $\mathbf{x}/\lVert\mathbf{x}\rVert$.

</li>

<li>

Vérifiez que $\lVert\mathbf{x}\rVert_\infty\le\lVert\mathbf{x}\rVert_2\le\lVert\mathbf{x}\rVert_1$. Expliquez pourquoi cet ordre est valable pour tout vecteur.

</li>

</ol>

:::loesung
(a) $\lVert\mathbf{x}\rVert_1=2+1+0+2=5$, $\lVert\mathbf{x}\rVert_2=\sqrt{4+1+0+4}=3$, $\lVert\mathbf{x}\rVert_3=(8+1+0+8)^{1/3}=17^{1/3}\approx2{,}571$ et $\lVert\mathbf{x}\rVert_\infty=2$. Le vecteur normé est $\mathbf{x}/3=(\tfrac23,\,-\tfrac13,\,0,\,\tfrac23)^{\top}$, de longueur $\sqrt{(4+1+4)/9}=1$.

(b) On a $2\le3\le5$, et $\lVert\mathbf{x}\rVert_3$, qui vaut $2{,}571$, se situe lui aussi entre les deux. En général : si $|x_k|$ est la plus grande valeur absolue d’une composante, alors $\lVert\mathbf{x}\rVert_\infty^2=x_k^2\le\sum_jx_j^2=\lVert\mathbf{x}\rVert_2^2$, car la somme contient $x_k^2$ et, en plus, uniquement des termes positifs ou nuls. Et $\lVert\mathbf{x}\rVert_1^2=\bigl(\sum_j|x_j|\bigr)^2=\sum_jx_j^2+\sum_{j\ne l}|x_j|\,|x_l|\ge\lVert\mathbf{x}\rVert_2^2$, parce que les termes croisés ne sont pas négatifs. Intuitivement : le trajet à vol d’oiseau n’est jamais plus long que le chemin à travers le réseau de rues, ni plus court que la plus longue des étapes prises isolément.
:::
:::

:::aufgabe Exercice 8 ★★ Quelle est la qualité des estimations de l’agente immobilière ?
<span class="anker" id="aufg-8"></span>

L’agente immobilière de la sous-section [2.2](das-skalarprodukt.html#stufe-2-2) avait fait les prédictions $\hat{\mathbf{y}}=(188,\,126,\,286,\,232)^{\top}$ ; les prix réels étaient $\mathbf{y}=(200,\,130,\,290,\,240)^{\top}$, en milliers d’euros.

<ol class="al">

<li>

Calculez le vecteur d’erreur, ses trois normes et sa valeur efficace. Pour quel appartement se trompe-t-elle le plus ?

</li>

<li>

Que remarquez-vous au sujet des signes ? Désormais, l’agente immobilière ajoute $7$ mille euros à chaque prédiction. Calculez le nouveau vecteur d’erreur et ses normes. S’est-elle améliorée selon les trois normes ?

</li>

</ol>

:::loesung
(a) Le vecteur d’erreur est $\hat{\mathbf{y}}-\mathbf{y}=(188-200,\ 126-130,\ 286-290,\ 232-240)^{\top}=(-12,\,-4,\,-4,\,-8)^{\top}$. Ses normes : $\lVert\cdot\rVert_1=28$, $\lVert\cdot\rVert_2=\sqrt{144+16+16+64}=\sqrt{240}\approx15{,}49$, $\lVert\cdot\rVert_\infty=12$, valeur efficace $\sqrt{240}/2\approx7{,}75$ mille euros. C’est pour l’appartement 1 qu’elle se trompe le plus, de $12$ mille euros.

(b) Toutes les erreurs sont négatives : l’agente immobilière estime systématiquement trop bas, son erreur a une composante continue. Avec un supplément de $7$ mille euros, le vecteur d’erreur devient $(-5,\,3,\,3,\,-1)^{\top}$, avec $\lVert\cdot\rVert_1=12$, $\lVert\cdot\rVert_2=\sqrt{25+9+9+1}=\sqrt{44}\approx6{,}63$, $\lVert\cdot\rVert_\infty=5$ et la valeur efficace $\sqrt{44}/2\approx3{,}32$. Elle s’est améliorée selon les trois normes. Le supplément $7$ est exactement la moyenne des valeurs absolues des erreurs, $(12+4+4+8)/4=7$ : il retire la composante continue de l’erreur et ne laisse que la composante alternative.
:::
:::

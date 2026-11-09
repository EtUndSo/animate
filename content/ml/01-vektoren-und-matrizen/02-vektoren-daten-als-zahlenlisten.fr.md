---
title: Vecteurs : les données comme listes de nombres
pfad: Informatique / Apprentissage automatique / Fondements mathématiques / Vecteurs et matrices
knoten: Fondements 1 : Vecteurs et matrices
nachschlagen: ja
order: 15210200
summary: Un ordinateur ne sait manipuler que des nombres.
tags: indice, symbole somme, indice de sommation, somme double, caractéristique, exemple, jeu de données, vecteur
lang: fr
---

<span class="anker" id="stufe-1"></span>

:::zweck
Un ordinateur ne sait manipuler que des nombres. Cette section explique comment décrire une chose du monde réel par une liste de nombres et quels calculs sont permis avec de telles listes.
:::

### Ce dont vous avez besoin : le symbole somme et les indices

<span class="anker" id="stufe-1-1"></span>

Dans ce chapitre, on additionne sans cesse de nombreux nombres. Pour ne pas avoir à écrire chaque fois « $a_1+a_2+\dots$ », il existe une notation abrégée.

**Les indices.** Lorsqu’on a plusieurs nombres de même nature, on les numérote : $a_1,a_2,\dots,a_n$. Le petit numéro placé en bas s’appelle l’__indice__. Il indique seulement de quel nombre de la liste il s’agit et n’a rien à voir avec la valeur de ce nombre.

**Le symbole somme.** Pour la somme de $a_1$ à $a_n$, on écrit

<span class="anker" id="gl-1-1"></span>
$$\sum_{i=1}^{n} a_i = a_1+a_2+\dots+a_n , \tag{1.1}$$

ce qui se lit « somme des $a_i$ pour $i$ allant de $1$ à $n$ ». Le grand sigma grec s’appelle le __symbole somme__. La lettre $i$ placée dessous est l’__indice de sommation__ : il prend successivement les valeurs $1,2,\dots,n$, et pour chaque valeur un terme s’ajoute. L’indice de sommation est un indice muet. Qu’on l’appelle $i$, $j$ ou $k$ ne change pas la somme : $\sum_{i=1}^n a_i=\sum_{j=1}^n a_j$.

**Deux règles de calcul.** Une somme écrite avec le symbole somme n’est qu’une somme ordinaire d’un nombre fini de nombres, écrite en abrégé. Les règles connues s’y appliquent donc : on peut factoriser par un facteur commun (distributivité) et réordonner et regrouper les termes à volonté (commutativité et associativité). Avec le symbole somme, cela s’écrit ainsi : un facteur commun peut passer devant la somme, et une somme de sommes peut être scindée :

<span class="anker" id="gl-1-2"></span>
$$\sum_{i=1}^n c\,a_i=c\sum_{i=1}^n a_i ,\qquad \sum_{i=1}^n (a_i+b_i)=\sum_{i=1}^n a_i+\sum_{i=1}^n b_i . \tag{1.2}$$

**Les sommes doubles.** Les nombres rangés dans un tableau reçoivent deux indices : $a_{ij}$ est le nombre situé à la ligne $i$ et à la colonne $j$. La somme de tous les coefficients d’un tableau à $m$ lignes et $n$ colonnes s’écrit sous la forme d’une __somme double__

$$\sum_{i=1}^{m}\sum_{j=1}^{n}a_{ij} .$$

On la lit de l’intérieur vers l’extérieur : pour chaque ligne $i$, la somme intérieure additionne les nombres de cette ligne, et la somme extérieure additionne les sommes des lignes. Comme l’ordre n’importe pas lorsque les termes sont en nombre fini, on peut échanger les deux symboles somme et additionner d’abord colonne par colonne.

⁠**Exemple de calcul 1 :** Pour $a_1=2$, $a_2=5$, $a_3=1$, on écrit d’abord chaque somme en entier, puis on y substitue les nombres et l’on additionne (Fig. [1](#abb-1)). Ainsi, $\sum_{i=1}^3 a_i=8$ et $\sum_{i=1}^3 a_i^2=30$. Dans la troisième somme, l’indice de sommation est lui-même le terme : $\sum_{j=1}^{3}j=6$.

:::abbildung ml/k1rsumme 1
Trois sommes pas à pas : écrire le symbole somme en entier, substituer les nombres, additionner.
:::

⁠**Exemple de calcul 2 :** Le tableau de lignes $(1,\,2)$ et $(3,\,4)$ a pour coefficients $a_{11}=1$, $a_{12}=2$, $a_{21}=3$, $a_{22}=4$. En additionnant ligne par ligne, la somme double donne $(1+2)+(3+4)=10$, et colonne par colonne $(1+3)+(2+4)=10$ (Fig. [2](#abb-2)).

:::abbildung ml/k1rdoppel 2
La somme double sur le tableau de lignes $(1,\,2)$ et $(3,\,4)$, en haut d’abord ligne par ligne, en bas d’abord colonne par colonne. Les deux ordres donnent la même somme.
:::

⁠**En bref :** $\sum_{i=1}^n a_i$ est la somme de $a_1$ à $a_n$ ; l’indice de sommation $i$ n’est qu’un indice muet.

### Exemples et caractéristiques

<span class="anker" id="stufe-1-2"></span>

Qui veut apprendre à partir de données a d’abord devant soi une collection de choses de même nature : des appartements, des patients, des lettres, des mesures effectuées sur une machine. On décrit chaque chose par les mêmes grandeurs mesurées. Les appartements, par exemple, par leur surface, leur nombre de pièces et leur distance au centre-ville. Si l’on note cela pour plusieurs appartements, on obtient un tableau (tableau [1](#tab-1)). Il accompagne tout le chapitre.

<span class="anker" id="tab-1"></span>

**Tableau 1 :** Le jeu de données des appartements de ce chapitre : quatre appartements, chacun décrit par trois caractéristiques. Les nombres sont inventés.

|  | Surface en $\mathrm{m}^2$ | Pièces | Distance au centre en km |
|---|---|---|---|
| Appartement 1 | 60 | 2 | 3 |
| Appartement 2 | 40 | 1 | 1 |
| Appartement 3 | 90 | 4 | 6 |
| Appartement 4 | 70 | 3 | 2 |

Chaque ligne du tableau correspond à une chose, chaque colonne à une grandeur mesurée. Pour les deux, il existe des mots consacrés.

:::definition Définition 1.1 (Caractéristique, exemple, jeu de données)
<span class="anker" id="satz-1-1"></span>

Une __caractéristique__ est une propriété que l’on peut indiquer par un nombre réel.

Un __exemple__ est une chose individuelle, décrite par les valeurs de $d$ caractéristiques.

Un __jeu de données__ est une collection de $N$ exemples, tous décrits par les mêmes $d$ caractéristiques.
:::

Dans toute la série, $N$ est le nombre d’exemples et $d$ le nombre de caractéristiques. Les exemples sont numérotés $i=1,\dots,N$, les caractéristiques $j=1,\dots,d$.

Deux remarques sur les mots. Dans les bases de données, une ligne d’un tableau s’appelle souvent « enregistrement » ; le jeu de données, lui, est ici la collection entière. Et le mot « exemple » désigne toujours, dans ce chapitre, une chose issue d’un jeu de données ; c’est pourquoi les exercices entièrement calculés s’appellent « exemple de calcul ».

⁠**Exemple de calcul :** Le jeu de données des appartements comporte $N=4$ exemples et $d=3$ caractéristiques. La caractéristique 2 est le nombre de pièces. Pour l’appartement 3, elle vaut $4$.

Une propriété n’est pas toujours, par nature, un nombre. Le quartier d’un appartement est un nom. De telles propriétés doivent d’abord être traduites en nombres avant que l’on puisse calculer avec elles. Dans ce chapitre, toutes les caractéristiques sont déjà des nombres.

⁠**En bref :** Un jeu de données se compose de $N$ exemples, et chaque exemple est décrit par les mêmes $d$ caractéristiques.

:::hintergrund Les mêmes choses sous d’autres noms
Dans les textes de langue anglaise, un exemple s’appelle *example*, *sample*, *instance* ou *data point*, une caractéristique *feature* ou *attribute*, et le jeu de données *dataset*. En français aussi, on rencontre souvent « échantillon », « individu », « observation » ou « point de données » pour un exemple. Il s’agit toujours de la même chose : une ligne du tableau.
:::

### Vecteurs

<span class="anker" id="stufe-1-3"></span>

Pour l’ordinateur, un appartement n’est rien d’autre que ses trois nombres. Pour pouvoir calculer avec ces trois nombres comme avec un seul objet, on les réunit en une liste. L’ordre y est fixé : d’abord la surface, puis les pièces, puis la distance.

On peut aussi dessiner une telle liste lorsqu’elle ne contient que deux nombres. Si l’on ne garde de l’appartement 4 que le nombre de pièces $3$ et la distance $2$, on obtient le point de coordonnées $(3,\,2)$ dans un plan dont l’axe horizontal compte les pièces et l’axe vertical les kilomètres. On peut aussi se représenter la même liste comme une flèche qui va de l’origine à ce point (Fig. [3](#abb-3)). Les deux images décrivent les deux mêmes nombres.

:::abbildung ml/k1punktpfeil 3
Le vecteur $\mathbf{x}=(3,\,2)^{\top}$, à gauche comme point, à droite comme flèche allant de l’origine à ce point. Ici, $x_1$ représente le nombre de pièces et $x_2$ la distance au centre en km de l’appartement 4.
:::

:::definition Définition 1.2 (Vecteur)
<span class="anker" id="satz-1-2"></span>

Un __vecteur__ $\mathbf{x}$ à $d$ composantes est une liste ordonnée de $d$ nombres réels $x_1,\dots,x_d$, écrits les uns sous les autres :

$$\mathbf{x}=\begin{pmatrix}x_1\\\vdots\\x_d\end{pmatrix}.$$

Le nombre $x_j$ s’appelle la $j$-ième __composante__ de $\mathbf{x}$. L’ensemble de tous les vecteurs à $d$ composantes se note $\mathbb{R}^d$. Deux vecteurs sont égaux s’ils ont le même nombre de composantes et si toutes leurs composantes de même position coïncident.
:::

Les vecteurs s’écrivent en minuscules grasses, leurs composantes en caractères maigres. Par opposition à un vecteur, on appelle un nombre réel isolé un __scalaire__.

**Colonne et ligne.** Dans cette série, un vecteur est toujours une colonne. Dans le texte courant, une colonne prend beaucoup de place. On écrit donc les nombres côte à côte et l’on place derrière un $\top$ en exposant : $(x_1,\dots,x_d)^{\top}$ désigne les mêmes nombres écrits en colonne. Le signe se lit __transposé__. Il transforme une ligne en colonne et une colonne en ligne. Inversement, $\mathbf{x}^{\top}=(x_1,\,\dots,\,x_d)$ est le vecteur $\mathbf{x}$ écrit en ligne. Lorsqu’un vecteur contient des nombres décimaux, on sépare les composantes par des points-virgules, afin de ne pas confondre la virgule décimale avec la virgule de séparation : $(0{,}2;\ 0{,}25;\ 0{,}3)^{\top}$ a trois composantes.

**Les exemples d’un jeu de données.** L’exemple numéro $i$ est le vecteur $\mathbf{x}_i\in\mathbb{R}^d$. On appelle aussi le vecteur d’un exemple son __vecteur de caractéristiques__. Ses composantes reçoivent deux indices : $x_{ij}$ est la valeur de la caractéristique $j$ pour l’exemple $i$. Une lettre grasse avec un indice est donc un vecteur entier tiré d’une liste de vecteurs, une lettre maigre avec deux indices un nombre isolé.

⁠**Exemple de calcul :** L’appartement 1 est le vecteur $\mathbf{x}_1=(60,\,2,\,3)^{\top}\in\mathbb{R}^3$. Sa deuxième composante est $x_{12}=2$. Le vecteur $(2,\,60,\,3)^{\top}$ contient les mêmes nombres, mais c’est un autre vecteur : en première position figure maintenant le nombre $2$, et on le lirait comme une surface.

⁠**En bref :** Un vecteur est une liste ordonnée de nombres, que l’on peut dessiner comme un point ou comme une flèche ; un exemple à $d$ caractéristiques est un vecteur de $\mathbb{R}^d$.

:::hintergrund Ce qu’est vraiment un vecteur
Une liste de nombres est le vecteur avec lequel on calcule. En mathématiques, la notion est plus large : un vecteur est tout ce que l’on peut additionner et multiplier par un nombre sans sortir du type d’objet considéré. Les flèches du plan en font partie, mais aussi les signaux. Un signal échantillonné $n$ fois est la liste de ses échantillons $x[0],\dots,x[n-1]$, donc un vecteur de $\mathbb{R}^n$. Additionner deux signaux, c’est les superposer, et multiplier un signal par un nombre, c’est l’amplifier ; les deux opérations donnent de nouveau un signal de même longueur.

Une image aussi est un vecteur. Une image en niveaux de gris de $28\times28$ pixels se compose de $784$ valeurs de luminosité. Si on les lit à la suite, ligne par ligne, l’image est un point de $\mathbb{R}^{784}$. Cette représentation ne se dessine plus, mais on calcule avec elle exactement comme avec deux ou trois composantes.
:::

### Addition et multiple

<span class="anker" id="stufe-1-4"></span>

On veut calculer avec des listes de valeurs mesurées : additionner la consommation d’électricité de deux appartements, convertir des kilowattheures en mégawattheures ou regarder de combien deux appartements diffèrent. Tout cela se fait composante par composante.

Dans l’image des flèches, additionner signifie : on accroche la deuxième flèche à la pointe de la première. La flèche qui va de l’origine à la nouvelle pointe est la somme (Fig. [4](#abb-4), à gauche). Multiplier par un nombre, c’est allonger ou raccourcir la flèche ; un facteur négatif la retourne en plus (Fig. [4](#abb-4), à droite).

:::abbildung ml/k1addition 4
À gauche : $\mathbf{u}=(3,\,1)^{\top}$ plus $\mathbf{v}=(1,\,2)^{\top}$. Si l’on accroche $\mathbf{v}$ à la pointe de $\mathbf{u}$ (ou $\mathbf{u}$ à la pointe de $\mathbf{v}$, en tirets), on arrive en $\mathbf{u}+\mathbf{v}=(4,\,3)^{\top}$. À droite : $\mathbf{u}=(2,\,1)^{\top}$, le double $2\mathbf{u}=(4,\,2)^{\top}$ (en gris) et $-\mathbf{u}=(-2,\,-1)^{\top}$.
:::

:::definition Définition 1.3 (Addition et multiple)
<span class="anker" id="satz-1-3"></span>

Pour deux vecteurs $\mathbf{u},\mathbf{v}\in\mathbb{R}^d$ et un scalaire $c$, la __somme__ $\mathbf{u}+\mathbf{v}$ et le __multiple__ $c\,\mathbf{u}$ sont les vecteurs de composantes

<span class="anker" id="gl-1-3"></span>
$$(\mathbf{u}+\mathbf{v})_j=u_j+v_j ,\qquad (c\,\mathbf{u})_j=c\,u_j ,\qquad j=1,\dots,d. \tag{1.3}$$

Le __vecteur nul__ $\mathbf{0}$ n’a que des zéros comme composantes. On écrit $-\mathbf{u}$ pour $(-1)\,\mathbf{u}$ et $\mathbf{u}-\mathbf{v}$ pour $\mathbf{u}+(-\mathbf{v})$.
:::

On ne peut additionner que des vecteurs ayant le même nombre de composantes. Et cela n’a de sens que si la même grandeur figure à la même position : des kilowattheures avec des kilowattheures, pas des mètres carrés avec des pièces.

Comme chaque composante est à elle seule un calcul ordinaire sur des nombres, les règles connues s’appliquent : $\mathbf{u}+\mathbf{v}=\mathbf{v}+\mathbf{u}$, $(\mathbf{u}+\mathbf{v})+\mathbf{q}=\mathbf{u}+(\mathbf{v}+\mathbf{q})$, $c\,(\mathbf{u}+\mathbf{v})=c\,\mathbf{u}+c\,\mathbf{v}$, $(c+c')\,\mathbf{u}=c\,\mathbf{u}+c'\,\mathbf{u}$ et $\mathbf{u}+\mathbf{0}=\mathbf{u}$ pour tous les vecteurs $\mathbf{u},\mathbf{v},\mathbf{q}\in\mathbb{R}^d$ et tous les scalaires $c,c'$.

La différence $\mathbf{u}-\mathbf{v}$ a sa propre interprétation géométrique. C’est la flèche qui va de la pointe de $\mathbf{v}$ à la pointe de $\mathbf{u}$, car $\mathbf{v}+(\mathbf{u}-\mathbf{v})=\mathbf{u}$. Pour deux exemples, elle indique de combien ils diffèrent pour chaque caractéristique.

⁠**Exemple de calcul :** De janvier à mars, l’appartement 1 a consommé $\mathbf{u}=(200,\,250,\,300)^{\top}$ kilowattheures d’électricité, et l’appartement 2, dans le même immeuble, $\mathbf{v}=(150,\,100,\,120)^{\top}$. Ensemble, ils consomment

$$\mathbf{u}+\mathbf{v}=(350,\,350,\,420)^{\top}\ \text{kWh}.$$

Le multiple $0{,}001\,\mathbf{u}=(0{,}2;\ 0{,}25;\ 0{,}3)^{\top}$ donne la consommation de l’appartement 1 en mégawattheures. La différence $\mathbf{u}-\mathbf{v}=(50,\,150,\,180)^{\top}$ indique combien de kilowattheures l’appartement 1 consomme chaque mois de plus que l’appartement 2. Dans le jeu de données des appartements, $\mathbf{x}_3-\mathbf{x}_1=(30,\,2,\,3)^{\top}$ : l’appartement 3 est plus grand de $30\,\mathrm m^2$, a deux pièces de plus et se trouve $3$ km plus loin du centre que l’appartement 1.

⁠**En bref :** On additionne des vecteurs et on les multiplie par un nombre en procédant composante par composante.

### Combinaisons linéaires

<span class="anker" id="stufe-1-5"></span>

Presque chaque calcul de ce chapitre prend plusieurs vecteurs, multiplie chacun par son propre nombre et additionne les résultats. Une moyenne est un tel calcul, un mélange aussi.

Dans l’image des flèches : on parcourt $c_1$ fois le trajet $\mathbf{v}_1$, puis $c_2$ fois le trajet $\mathbf{v}_2$, et ainsi de suite. Le point d’arrivée est le résultat.

:::definition Définition 1.4 (Combinaison linéaire)
<span class="anker" id="satz-1-4"></span>

Pour des vecteurs $\mathbf{v}_1,\dots,\mathbf{v}_k\in\mathbb{R}^d$ et des scalaires $c_1,\dots,c_k$, on appelle

<span class="anker" id="gl-1-4"></span>
$$c_1\mathbf{v}_1+c_2\mathbf{v}_2+\dots+c_k\mathbf{v}_k=\sum_{l=1}^{k}c_l\,\mathbf{v}_l \tag{1.4}$$

une __combinaison linéaire__ des vecteurs $\mathbf{v}_1,\dots,\mathbf{v}_k$. Les nombres $c_l$ s’appellent ses __coefficients__.
:::

Attention à la lecture : $\mathbf{v}_l$ est en gras, c’est donc le $l$-ième vecteur de la liste, et non la $l$-ième composante d’un vecteur.

⁠**Exemple de calcul 1 :** $(1,\,2)^{\top}+3\,(0,\,1)^{\top}=(1,\,2)^{\top}+(0,\,3)^{\top}=(1,\,5)^{\top}$.

⁠**Exemple de calcul 2 : le milieu.** La combinaison linéaire $\tfrac12\mathbf{x}_1+\tfrac12\mathbf{x}_2$ des appartements 1 et 2 vaut

$$\tfrac12\,(60,\,2,\,3)^{\top}+\tfrac12\,(40,\,1,\,1)^{\top}=(50;\ 1{,}5;\ 2)^{\top}.$$

C’est un appartement fictif qui se situe, pour chaque caractéristique, exactement entre les deux. Le point se trouve au milieu du segment qui les relie.

⁠**Exemple de calcul 3 : la moyenne des exemples.** Si l’on prend les $N$ exemples avec le coefficient $1/N$, on obtient la __moyenne des exemples__

<span class="anker" id="gl-1-5"></span>
$$\bar{\mathbf{x}}=\frac1N\sum_{i=1}^{N}\mathbf{x}_i . \tag{1.5}$$

Pour le jeu de données des appartements, $\bar{\mathbf{x}}=(65;\ 2{,}5;\ 3)^{\top}$ (Fig. [5](#abb-5)), l’« appartement moyen » : en moyenne $65\,\mathrm m^2$, $2{,}5$ pièces et $3$ km jusqu’au centre.

:::abbildung ml/k1rmittelvektor 5
La moyenne des quatre appartements : la somme des vecteurs est calculée composante par composante, puis divisée par $4$ ; $5/2=2{,}5$.
:::

⁠**En bref :** Une combinaison linéaire multiplie chaque vecteur par son propre nombre et additionne le tout.

:::hintergrund Où se trouvent les mélanges de deux points
Si, pour deux vecteurs $\mathbf{x}_1,\mathbf{x}_2$, on choisit les coefficients de sorte que leur somme vaille $1$, c’est-à-dire $(1-t)\,\mathbf{x}_1+t\,\mathbf{x}_2$ avec un nombre $t$, le résultat se trouve toujours sur la droite passant par les deux points. En effet, on peut le réécrire sous la forme

$$(1-t)\,\mathbf{x}_1+t\,\mathbf{x}_2=\mathbf{x}_1+t\,(\mathbf{x}_2-\mathbf{x}_1) .$$

Autrement dit : partir du point $\mathbf{x}_1$ et parcourir $t$ fois la flèche de liaison $\mathbf{x}_2-\mathbf{x}_1$. Pour $t=0$, on est en $\mathbf{x}_1$, pour $t=1$ en $\mathbf{x}_2$, pour $t=\tfrac12$ au milieu. Toutes les valeurs de $t$ comprises entre $0$ et $1$ donnent les points du segment qui les relie. On a besoin de tels mélanges chaque fois que l’on veut former des valeurs intermédiaires entre deux points de données.
:::

### Les vecteurs unitaires

<span class="anker" id="stufe-1-6"></span>

Les vecteurs les plus simples ont une seule composante égale à $1$ et des zéros partout ailleurs. Pour un exemple, cela signifierait : une seule caractéristique est « allumée », et ce avec la valeur $1$. Dans le plan, ce sont les deux flèches de longueur $1$ le long des axes.

:::definition Définition 1.5 (Vecteur unitaire)
<span class="anker" id="satz-1-5"></span>

Le $j$-ième __vecteur unitaire__ $\mathbf{e}_j\in\mathbb{R}^d$ a un $1$ en position $j$ et un $0$ à toutes les autres positions.
:::

Dans $\mathbb{R}^2$, on a $\mathbf{e}_1=(1,\,0)^{\top}$ et $\mathbf{e}_2=(0,\,1)^{\top}$. Tout vecteur est une combinaison linéaire des vecteurs unitaires, et les coefficients sont exactement ses composantes :

<span class="anker" id="gl-1-6"></span>
$$\mathbf{x}=x_1\mathbf{e}_1+x_2\mathbf{e}_2+\dots+x_d\mathbf{e}_d=\sum_{j=1}^d x_j\,\mathbf{e}_j . \tag{1.6}$$

On le voit en calculant le membre de droite composante par composante : en position $j$, seul le terme $x_j\mathbf{e}_j$ apporte une contribution, à savoir $x_j\cdot1$. D’autres coefficients sont impossibles, car ils donneraient un autre nombre en une position ou une autre.

⁠**Exemple de calcul :** $\mathbf{x}_1=(60,\,2,\,3)^{\top}=60\,\mathbf{e}_1+2\,\mathbf{e}_2+3\,\mathbf{e}_3$, soit $60$ fois « un mètre carré » plus $2$ fois « une pièce » plus $3$ fois « un kilomètre ».

⁠**En bref :** Le vecteur unitaire $\mathbf{e}_j$ vaut un en position $j$ et zéro partout ailleurs ; tout vecteur est la somme $\sum_jx_j\mathbf{e}_j$.

:::aufgabe Exercice 1 ★ Lire et écrire des sommes
<span class="anker" id="aufg-1"></span>

<ol class="al">

<li>

Calculez $\sum_{i=1}^{5}(2i-1)$ et $\sum_{i=1}^{2}\sum_{j=1}^{3}i\,j$.

</li>

<li>

Écrivez $3+6+9+12$ avec un symbole somme.

</li>

<li>

Soit $a_i$ la surface de l’appartement $i$ du tableau [1](#tab-1). Que signifient $\sum_{i=1}^4a_i$ et $\frac14\sum_{i=1}^4a_i$, et quels nombres obtient-on ?

</li>

</ol>

:::loesung
(a) L’indice de sommation $i$ prend les valeurs de $1$ à $5$, et les termes sont les nombres impairs $1,3,5,7,9$ :

$$\sum_{i=1}^{5}(2i-1)=1+3+5+7+9=25 .$$

Dans la somme double, pour chaque $i$ fixé, la somme intérieure vaut $\sum_{j=1}^3i\,j=i\,(1+2+3)=6i$ ; le facteur $i$ ne dépend pas de $j$ et peut, d’après [(1.2)](#gl-1-2), passer devant la somme intérieure. Ensuite, $\sum_{i=1}^2 6i=6+12=18$.

(b) Les termes sont les multiples de $3$ : $3+6+9+12=\sum_{i=1}^43i$. L’écriture $3\sum_{i=1}^4i$ est tout aussi juste, d’après la règle du facteur commun.

(c) $\sum_{i=1}^4a_i=60+40+90+70=260$ est la surface totale des quatre appartements en $\mathrm m^2$, et $\frac14\sum_{i=1}^4a_i=65$ est la surface moyenne d’un appartement.
:::
:::

:::aufgabe Exercice 2 ★ Calculer avec des vecteurs
<span class="anker" id="aufg-2"></span>

<ol class="al">

<li>

Calculez $2\mathbf{u}-3\mathbf{v}$ pour $\mathbf{u}=(1,\,-1,\,0)^{\top}$ et $\mathbf{v}=(0,\,1,\,2)^{\top}$.

</li>

<li>

Écrivez $(4,\,-1,\,2)^{\top}$ comme combinaison linéaire des vecteurs unitaires de $\mathbb{R}^3$.

</li>

<li>

Trouvez des nombres $c_1,c_2$ tels que $c_1(1,\,2)^{\top}+c_2(2,\,1)^{\top}=(3,\,3)^{\top}$. Dessinez la solution avec des flèches.

</li>

<li>

Calculez $\mathbf{x}_3-\mathbf{x}_2$ pour le jeu de données des appartements et décrivez en mots ce que ce vecteur exprime.

</li>

</ol>

:::loesung
(a) Composante par composante : $2\mathbf{u}=(2,\,-2,\,0)^{\top}$ et $3\mathbf{v}=(0,\,3,\,6)^{\top}$, donc $2\mathbf{u}-3\mathbf{v}=(2,\,-5,\,-6)^{\top}$.

(b) D’après [(1.6)](#gl-1-6), les coefficients sont les composantes : $(4,\,-1,\,2)^{\top}=4\,\mathbf{e}_1-\mathbf{e}_2+2\,\mathbf{e}_3$.

(c) Composante par composante, la condition s’écrit $c_1+2c_2=3$ et $2c_1+c_2=3$. Si l’on soustrait deux fois la première équation de la deuxième, il reste $-3c_2=-3$, donc $c_2=1$, puis $c_1=1$. Vérification : $(1,\,2)^{\top}+(2,\,1)^{\top}=(3,\,3)^{\top}$. Sur le dessin, on accroche la flèche $(2,\,1)^{\top}$ à la pointe de $(1,\,2)^{\top}$ et l’on arrive en $(3,\,3)^{\top}$.

(d) $\mathbf{x}_3-\mathbf{x}_2=(90-40,\ 4-1,\ 6-1)^{\top}=(50,\,3,\,5)^{\top}$ : l’appartement 3 est plus grand de $50\,\mathrm m^2$ que l’appartement 2, a trois pièces de plus et se trouve $5$ km plus loin du centre. Le vecteur est la flèche qui va du point $\mathbf{x}_2$ au point $\mathbf{x}_3$.
:::
:::

:::aufgabe Exercice 3 ★ Un jeu de données à vous
<span class="anker" id="aufg-3"></span>

Choisissez quatre choses de votre quotidien, par exemple des aliments, des vélos ou des chansons, et trois propriétés que vous pouvez indiquer par un nombre pour chacune d’elles. Mesurez ou recherchez les valeurs.

<ol class="al">

<li>

Dressez le tableau. Que valent $N$ et $d$ ? Écrivez le deuxième exemple sous forme de vecteur $\mathbf{x}_2$.

</li>

<li>

Quelle propriété, qui vous intéresserait aussi, n’est pas un nombre ? Comment pourrait-on la traduire en nombres ?

</li>

<li>

Calculez la moyenne des exemples $\bar{\mathbf{x}}$. Existe-t-il une chose qui lui ressemble exactement ?

</li>

</ol>

:::loesung
Une solution possible : quatre pommes, avec pour caractéristiques la masse en g, le diamètre en cm et le prix en centimes.

(a) Supposons que le tableau ait pour lignes $(180;\ 7{,}5;\ 45)$, $(150;\ 7{,}0;\ 40)$, $(210;\ 8{,}0;\ 55)$ et $(165;\ 7{,}2;\ 40)$. On a alors $N=4$ et $d=3$, et $\mathbf{x}_2=(150;\ 7{,}0;\ 40)^{\top}$. Seul compte le fait que chaque chose soit décrite par les trois mêmes caractéristiques, dans le même ordre.

(b) La variété est un nom, pas un nombre. On peut la traduire en introduisant pour chaque variété une caractéristique propre, qui vaut $1$ si la pomme appartient à cette variété et $0$ sinon. Numéroter simplement les variétés n’est en revanche le plus souvent pas une bonne idée : les numéros suggèrent un ordre et des distances qui n’existent pas entre des variétés.

(c) La moyenne des exemples se calcule composante par composante ; ici, $\bar{\mathbf{x}}=(176{,}25;\ 7{,}425;\ 45)^{\top}$. Aucune pomme du tableau n’a exactement ces valeurs. La moyenne est un exemple imaginaire et non un exemple mesuré ; pour une propriété comme le nombre de pièces, elle peut même prendre une valeur qu’aucune chose réelle ne peut avoir, par exemple $2{,}5$ pièces.
:::
:::

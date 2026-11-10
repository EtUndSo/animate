---
title: Graphes de calcul
pfad: Informatique / Apprentissage automatique / Fondements mathématiques / Dérivée, gradient et règle de dérivation en chaîne
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Chapitre 3 : Dérivée, gradient et règle de dérivation en chaîne
nachschlagen: ja
order: 15231000
summary: Un ordinateur évalue les longues formules pas à pas, et chaque pas est une opération simple dont la dérivée est connue.
tags: graphe de calcul, évaluation avant, dérivée locale
lang: fr
---

<span class="anker" id="stufe-9"></span>

:::zweck
Un ordinateur évalue les longues formules pas à pas, et chaque pas est une opération simple dont la dérivée est connue. Un graphe de calcul rend visibles ces pas et leurs dépendances. Cette section dessine un tel graphe, l’évalue vers l’avant sous forme de tableau et inscrit sur chaque arête sa dérivée locale. Tout est alors prêt pour calculer mécaniquement les dérivées du résultat par rapport à toutes les entrées.
:::

### Résultats intermédiaires

<span class="anker" id="stufe-9-1"></span>

Avec les règles de la section [1.4](die-ableitung.html#stufe-1-4), on peut dériver toute formule composée d’opérations élémentaires et de fonctions connues. Mais si l’on écrit le résultat sous forme de formule, il devient souvent bien plus long que la fonction elle-même. D’après la règle du produit, un produit de $n$ facteurs a une dérivée formée de $n$ termes de $n$ facteurs chacun ; la formule croît donc comme $n^2$, alors que la fonction n’a que $n$ facteurs. Avec des résultats intermédiaires, en revanche, le calcul reste petit. Après chaque pas, on retient la valeur et la dérivée obtenues jusque-là, et l’on poursuit le calcul avec des nombres, non avec des formules.

::::beispiel [Exemple de calcul]
Soit $p(x)=(x+1)(x+2)(x+3)(x+4)$ ; on cherche $p'(0)$. La règle du produit écrite explicitement donne quatre termes, dans chacun desquels un facteur est remplacé par sa dérivée $1$ :

$$p'(0)=2\cdot3\cdot4+1\cdot3\cdot4+1\cdot2\cdot4+1\cdot2\cdot3=24+12+8+6=50$$

(Fig. [17](#abb-17)). Pas à pas, avec les produits partiels $p_1=x+1$, $p_k=p_{k-1}\cdot(x+k)$ et la règle du produit $p_k'=p_{k-1}'\cdot(x+k)+p_{k-1}\cdot1$, on procède ainsi :

$$\begin{gathered} p_1=1,\quad p_1'=1;\qquad p_2=1\cdot2=2,\quad p_2'=1\cdot2+1\cdot1=3;\\ p_3=2\cdot3=6,\quad p_3'=3\cdot3+2\cdot1=11;\qquad p_4=6\cdot4=24,\quad p_4'=11\cdot4+6\cdot1=50 . \end{gathered}$$

Chaque pas coûte deux multiplications et une addition, quel que soit le nombre de facteurs déjà traités.

:::abbildung ml/k3rvierfaktoren 17
La règle du produit écrite explicitement pour $p(x)=(x+1)(x+2)(x+3)(x+4)$ en $0$ : dans le terme $k$, le facteur $x+k$ est remplacé par sa dérivée $1$.
:::
::::

⁠**En bref :** Les formules de dérivées écrites explicitement deviennent vite bien plus longues que la fonction ; avec des résultats intermédiaires stockés sous forme de nombres, le coût par pas reste faible.

### Le graphe de calcul

<span class="anker" id="stufe-9-2"></span>

Quels résultats intermédiaires un calcul comporte et de quoi chacun dépend, c’est une figure faite de nœuds et de flèches qui le montre le plus clairement. Une flèche d’un nœud $a$ vers un nœud $b$ signifie : on a besoin de $a$ pour calculer $b$.

:::definition Définition 9.1 (Graphe de calcul)
<span class="anker" id="satz-9-1"></span>

Un __graphe de calcul__ se compose de nœuds et d’arêtes orientées, c’est-à-dire de flèches entre les nœuds. Chaque nœud représente un nombre ou, dans des calculs plus grands, tout un vecteur ou une matrice. Les nœuds d’entrée sont les entrées du calcul ; tout autre nœud $v$ est obtenu par une opération de base à partir des nœuds d’où part une arête vers $v$. Ceux-ci s’appellent les prédécesseurs de $v$, et $v$ s’appelle leur successeur. En suivant les arêtes, on ne revient jamais à un nœud par lequel on est déjà passé ; un tel graphe est dit acyclique. Un nœud distingué est le résultat.
:::

Les opérations de base sont les opérations élémentaires et les fonctions d’une variable comme le carré, la fonction exponentielle ou la fonction logistique. Comme le graphe est acyclique, on peut toujours ranger les nœuds de sorte que chaque nœud vienne après ses prédécesseurs ; c’est dans cet ordre que l’on calcule. Un programme de calcul comportant des boucles et des branchements donne lui aussi un tel graphe pour des valeurs d’entrée données : une boucle parcourue trois fois fournit trois fois de suite les mêmes nœuds.

::::beispiel [Exemple de calcul]
L’exemple de cette section et de la suivante est

<span class="anker" id="gl-9-1"></span>
$$f(x_1,x_2,x_3)=(x_1+x_2)\,(x_2+x_3) \tag{9.1}$$

avec les résultats intermédiaires $v_1=x_1+x_2$ et $v_2=x_2+x_3$ et le résultat $f=v_1\cdot v_2$. Le graphe a trois nœuds d’entrée, deux nœuds d’addition et un nœud de multiplication, reliés par six arêtes (Fig. [18](#abb-18)). L’entrée $x_2$ a deux successeurs ; le graphe s’y ramifie.

:::abbildung ml/k3graph 18
Le graphe de calcul de $f=(x_1+x_2)\,(x_2+x_3)$. Les flèches pointent dans le sens du calcul, les cercles contiennent l’opération de base. En vert figurent les valeurs de l’évaluation avant au point $(1,\,2,\,3)$.
:::
::::

⁠**En bref :** Un graphe de calcul décompose un calcul en opérations de base ; ses arêtes montrent quelle valeur entre dans quelle autre, et comme il est acyclique, il existe toujours un ordre dans lequel on peut l’évaluer.

### L’évaluation avant

<span class="anker" id="stufe-9-3"></span>

Évaluer un graphe de calcul, c’est calculer les nœuds dans un ordre où chaque nœud vient après ses prédécesseurs. Si l’on écrit les pas les uns sous les autres, on obtient un tableau dont on a aussi besoin pour les dérivées : toutes les valeurs sont stockées, pas seulement le résultat.

:::definition Définition 9.2 (Évaluation avant)
<span class="anker" id="satz-9-2"></span>

L’__évaluation avant__ d’un graphe de calcul calcule tous les nœuds dans un ordre où chaque nœud vient après ses prédécesseurs, et stocke chaque valeur.
:::

::::beispiel [Exemple de calcul]
Pour [(9.1)](#gl-9-1) au point $(1,\,2,\,3)$, on obtient le tableau [3](#tab-3).

<span class="anker" id="tab-3"></span>

**Tableau 3 :** L’évaluation avant pour $f=(x_1+x_2)\,(x_2+x_3)$ au point $(1,\,2,\,3)$.

| Nœud | Calcul | Valeur |
|---|---|---|
| $x_1$ | entrée | $1$ |
| $x_2$ | entrée | $2$ |
| $x_3$ | entrée | $3$ |
| $v_1$ | $x_1+x_2$ | $3$ |
| $v_2$ | $x_2+x_3$ | $5$ |
| $f$ | $v_1\cdot v_2$ | $15$ |
::::

⁠**En bref :** L’évaluation avant évalue le graphe nœud par nœud et stocke chaque valeur intermédiaire.

### Dérivées locales

<span class="anker" id="stufe-9-4"></span>

Chaque arête relie un nœud à un successeur obtenu à partir de lui par une opération de base. La force avec laquelle le successeur réagit à une petite variation de ce seul prédécesseur est une dérivée partielle ordinaire de l’opération de base.

:::definition Définition 9.3 (Dérivée locale)
<span class="anker" id="satz-9-3"></span>

Pour une arête de $a$ vers $b$, la dérivée partielle $\partial b/\partial a$ de l’opération de base qui calcule $b$, par rapport à son entrée $a$, s’appelle la __dérivée locale__ de l’arête. Elle est évaluée avec les valeurs stockées de l’évaluation avant.
:::

Pour les opérations de base, les dérivées locales sont simples (tableau [4](#tab-4)). Il est remarquable qu’elles demandent si peu : pour la fonction exponentielle et la fonction logistique, la valeur stockée du successeur lui-même suffit. Le nœud maximum présente un point anguleux lorsque les deux entrées sont égales ; on y utilise l’une des deux valeurs unilatérales.

<span class="anker" id="tab-4"></span>

**Tableau 4 :** Dérivées locales des opérations de base, exprimées à l’aide des valeurs stockées.

| Opération | dérivées locales | valeurs nécessaires |
|---|---|---|
| $b=a_1+a_2$ | $\partial b/\partial a_1=1$, $\ \partial b/\partial a_2=1$ | aucune |
| $b=a_1\cdot a_2$ | $\partial b/\partial a_1=a_2$, $\ \partial b/\partial a_2=a_1$ | les entrées |
| $b=a^2$ | $\partial b/\partial a=2a$ | l’entrée |
| $b=\mathrm{e}^a$ | $\partial b/\partial a=\mathrm{e}^a=b$ | la sortie |
| $b=\sigma(a)$ | $\partial b/\partial a=b\,(1-b)$ | la sortie |
| $b=\max(a_1,a_2)$ | $1$ pour la plus grande entrée, $0$ pour l’autre | laquelle est la plus grande |

Avec les dérivées locales, la règle de dérivation en chaîne de la section [6.2](die-kettenregel-fur-mehrere-variablen.html#stufe-6-2) devient un simple exercice de dénombrement : la dérivée du résultat par rapport à une entrée est la somme sur tous les chemins allant de l’entrée au résultat, et le long de chaque chemin, on multiplie les dérivées locales de ses arêtes.

::::beispiel [Exemple de calcul]
Dans le graphe de la Fig. [18](#abb-18), les quatre arêtes allant des entrées aux nœuds d’addition ont la dérivée locale $1$. L’arête allant de $v_1$ au résultat a $\partial f/\partial v_1=v_2=5$, celle qui part de $v_2$ a $\partial f/\partial v_2=v_1=3$. De $x_1$, un chemin mène au résultat, de $x_3$ également, de $x_2$ deux. On a donc

$$\frac{\partial f}{\partial x_1}=1\cdot5=5,\qquad \frac{\partial f}{\partial x_2}=1\cdot5+1\cdot3=8,\qquad \frac{\partial f}{\partial x_3}=1\cdot3=3 .$$

Vérification : en développant, $f=x_1x_2+x_1x_3+x_2^2+x_2x_3$, de dérivées partielles $x_2+x_3=5$, $x_1+2x_2+x_3=8$ et $x_1+x_2=3$.
::::

⁠**En bref :** Chaque arête porte la dérivée locale de son opération de base, évaluée avec les valeurs stockées ; la dérivée du résultat est la somme, sur tous les chemins, des produits de ces nombres.

:::aufgabe Exercice 32 ★ Un graphe avec un carré
<span class="anker" id="aufg-32"></span>

Soit $f(x_1,x_2,x_3)=(x_1x_2+x_3)^2$.

<ol class="al">

<li>

Dessinez le graphe de calcul avec les résultats intermédiaires $v_1=x_1x_2$, $v_2=v_1+x_3$ et $f=v_2^2$.

</li>

<li>

Établissez le tableau de l’évaluation avant au point $(1,\,2,\,3)$ et inscrivez sur chaque arête sa dérivée locale.

</li>

<li>

Calculez les trois dérivées partielles comme sommes sur les chemins et faites la vérification.

</li>

</ol>

:::loesung
(a) Entrées $x_1,x_2,x_3$ ; un nœud de multiplication $v_1$ avec des arêtes venant de $x_1$ et de $x_2$ ; un nœud d’addition $v_2$ avec des arêtes venant de $v_1$ et de $x_3$ ; un nœud carré $f$ avec une arête venant de $v_2$.

(b) Évaluation avant : $x_1=1$, $x_2=2$, $x_3=3$, $v_1=2$, $v_2=5$, $f=25$. Dérivées locales : $\partial v_1/\partial x_1=x_2=2$, $\partial v_1/\partial x_2=x_1=1$, $\partial v_2/\partial v_1=1$, $\partial v_2/\partial x_3=1$, $\partial f/\partial v_2=2v_2=10$.

(c) De chaque entrée, exactement un chemin mène au résultat :

$$\frac{\partial f}{\partial x_1}=2\cdot1\cdot10=20,\qquad \frac{\partial f}{\partial x_2}=1\cdot1\cdot10=10,\qquad \frac{\partial f}{\partial x_3}=1\cdot10=10 .$$

Vérification : $\partial_1f=2\,(x_1x_2+x_3)\,x_2=20$, $\partial_2f=2\,(x_1x_2+x_3)\,x_1=10$, $\partial_3f=2\,(x_1x_2+x_3)=10$.
:::
:::

:::aufgabe Exercice 33 ★★ Cinq facteurs
<span class="anker" id="aufg-33"></span>

Soit $p(x)=(x+1)(x+2)(x+3)(x+4)(x+5)$.

<ol class="al">

<li>

Calculez $p'(1)$ pas à pas avec des produits partiels, comme dans l’exemple de calcul de la section [9.1](#stufe-9-1).

</li>

<li>

Combien de multiplications demande la règle du produit écrite explicitement, combien le calcul pas à pas ? Comment ces deux nombres croissent-ils avec le nombre $n$ de facteurs ?

</li>

</ol>

:::loesung
(a) En $1$, les facteurs sont $2,3,4,5,6$. Pas à pas :

$$\begin{aligned} p_1&=2, & p_1'&=1,\\ p_2&=2\cdot3=6, & p_2'&=1\cdot3+2\cdot1=5,\\ p_3&=6\cdot4=24, & p_3'&=5\cdot4+6\cdot1=26,\\ p_4&=24\cdot5=120, & p_4'&=26\cdot5+24\cdot1=154,\\ p_5&=120\cdot6=720, & p_5'&=154\cdot6+120\cdot1=1044 . \end{aligned}$$

Donc $p'(1)=1044$. Vérification : $p'(1)=p(1)\bigl(\tfrac12+\tfrac13+\tfrac14+\tfrac15+\tfrac16\bigr)=720\cdot\tfrac{87}{60}=1044$.

(b) Écrite explicitement, la règle du produit a $n$ termes de $n-1$ facteurs chacun, soit $n\,(n-2)$ multiplications ; pour $n=5$, cela fait $15$. Pas à pas, chacun des $n-1$ pas demande deux multiplications, soit $8$ pour $n=5$. La formule écrite explicitement croît comme $n^2$, le calcul pas à pas comme $n$.
:::
:::

:::aufgabe Exercice 34 ★★ Une boucle sous forme de graphe
<span class="anker" id="aufg-34"></span>

Un programme pose $y=x$, puis élève $y$ au carré trois fois de suite.

<ol class="al">

<li>

Dessinez le graphe de calcul et donnez la fonction $y(x)$.

</li>

<li>

Calculez en $x=2$ toutes les valeurs intermédiaires et les dérivées locales, et déduisez-en $y'(2)$. Comparez avec la dérivée de la formule de (a).

</li>

</ol>

:::loesung
(a) Le graphe est une chaîne $x\to y_1\to y_2\to y_3$ de trois nœuds carrés, $y_k=y_{k-1}^2$. On a $y=((x^2)^2)^2=x^8$.

(b) En $2$ : $y_1=4$, $y_2=16$, $y_3=256$. Les dérivées locales sont $2\cdot2=4$, $2\cdot4=8$ et $2\cdot16=32$, leur produit $4\cdot8\cdot32=1024$. La formule donne $8x^7=8\cdot128=1024$.
:::
:::

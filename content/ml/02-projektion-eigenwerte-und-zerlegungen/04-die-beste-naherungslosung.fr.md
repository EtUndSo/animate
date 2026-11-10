---
title: La meilleure solution approchée
pfad: Informatique / Apprentissage automatique / Fondements mathématiques / Projection, valeurs propres et décompositions
adresse: informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen
knoten: Chapitre 2 : Projection, valeurs propres et décompositions
nachschlagen: ja
order: 15220400
summary: Un système comportant plus d’équations que d’inconnues n’a en général pas de solution.
tags: résidu, meilleure solution approchée, équations normales, droite des moindres carrés
lang: fr
---

<span class="anker" id="stufe-3"></span>

:::zweck
Un système comportant plus d’équations que d’inconnues n’a en général pas de solution. Cette section cherche à la place les inconnues qui satisfont le système aussi bien que possible. Elles découlent d’un système d’équations plus petit, toujours résoluble, et la raison en est à nouveau un angle droit.
:::

### Rappel : plus d’équations que d’inconnues

<span class="anker" id="stufe-3-1"></span>

Dans le [chapitre 1, section 12.5](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/lineare-gleichungssysteme.html#stufe-12-5), deux poids, $w_1$ pour la surface et $w_2$ pour le nombre de pièces, devaient reproduire exactement les prix d’appartements. Avec les quatre appartements, c’est le système $\mathbf{A}\mathbf{w}=\mathbf{y}$ avec

$$\mathbf{A}=\begin{pmatrix}60&2\\40&1\\90&4\\70&3\end{pmatrix},\qquad \mathbf{y}=\begin{pmatrix}200\\130\\290\\240\end{pmatrix}\ \text{milliers d’euros}.$$

Il n’a pas de solution. Vu par colonnes, cela signifie : les colonnes de $\mathbf{A}$ engendrent dans $\mathbb{R}^4$ un plan, l’espace des colonnes, et le vecteur des prix $\mathbf{y}$ n’est pas dans ce plan. Quel que soit le choix de $\mathbf{w}$, il subsiste un reste.

:::definition Définition 3.1 (Résidu)
<span class="anker" id="satz-3-1"></span>

Pour un système d’équations $\mathbf{A}\mathbf{x}=\mathbf{y}$ et un vecteur quelconque $\mathbf{x}$, on appelle

<span class="anker" id="gl-3-1"></span>
$$\mathbf{r}=\mathbf{y}-\mathbf{A}\mathbf{x} \tag{3.1}$$

le __résidu__ associé à $\mathbf{x}$.
:::

Le mot vient du latin et signifie « reste ». Le résidu est nul si et seulement si $\mathbf{x}$ résout le système. C’est le vecteur d’erreur du [chapitre 1, section 3.5](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/normen-die-groe-eines-vektors.html#stufe-3-5), avec le signe opposé ; sa longueur est la même.

::::beispiel [Exemple de calcul]
Avec les poids $\mathbf{w}=(3,\,10)^{\top}$ du [chapitre 1](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/vektoren-und-matrizen.html), on obtient $\mathbf{A}\mathbf{w}=(200,\,130,\,310,\,240)^{\top}$ et le résidu $\mathbf{r}=\mathbf{y}-\mathbf{A}\mathbf{w}=(0,\,0,\,-20,\,0)^{\top}$, de longueur $20$. Trois prix sont reproduits exactement, un autre est manqué de $20$ mille euros.
::::

⁠**En bref :** Le résidu $\mathbf{r}=\mathbf{y}-\mathbf{A}\mathbf{x}$ est le reste qu’un vecteur $\mathbf{x}$ laisse lorsqu’on résout $\mathbf{A}\mathbf{x}=\mathbf{y}$.

### La meilleure solution approchée

<span class="anker" id="stufe-3-2"></span>

Si le résidu ne peut pas s’annuler, il doit au moins être aussi petit que possible. On le mesure par sa longueur euclidienne.

On peut se représenter le problème géométriquement. Quand $\mathbf{x}$ parcourt tous les vecteurs, $\mathbf{A}\mathbf{x}$ parcourt, d’après le [chapitre 1, section 7.4](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrix-vektor-produkt.html#stufe-7-4), l’espace des colonnes de $\mathbf{A}$. La distance $\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert$ est la distance du point $\mathbf{y}$ au point $\mathbf{A}\mathbf{x}$ de l’espace des colonnes. On cherche donc le point de l’espace des colonnes le plus proche de $\mathbf{y}$ (Fig. [6](#abb-6)). Dans la section précédente, l’espace des colonnes était une droite ; maintenant, ce peut être un plan ou un sous-espace engendré de dimension supérieure.

:::definition Définition 3.2 (Meilleure solution approchée)
<span class="anker" id="satz-3-2"></span>

Un vecteur $\hat{\mathbf{x}}$ est appelé __meilleure solution approchée__ du système $\mathbf{A}\mathbf{x}=\mathbf{y}$ si

<span class="anker" id="gl-3-2"></span>
$$\lVert\mathbf{y}-\mathbf{A}\hat{\mathbf{x}}\rVert\le\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert\qquad\text{pour tout }\mathbf{x} . \tag{3.2}$$
:::

La longueur est minimale là où son carré est minimal, et ce carré est la somme des carrés des composantes du résidu. C’est pourquoi on parle aussi de solution au sens de la *méthode des moindres carrés*. Si le système a une solution exacte, c’est aussi la meilleure solution approchée, car son résidu est de longueur nulle.

:::abbildung ml/k2ebene 6
Projection sur un plan de $\mathbb{R}^3$. Les colonnes $\mathbf{a}_1=(1,0,1)^{\top}$ et $\mathbf{a}_2=(0,1,1)^{\top}$ engendrent le plan $x_3=x_1+x_2$ (en bleu). Le point $\mathbf{y}=(1,1,1)^{\top}$ n’appartient pas à ce plan. Le point du plan le plus proche est $\hat{\mathbf{y}}=(\tfrac23,\tfrac23,\tfrac43)^{\top}$ ; le résidu $\mathbf{r}=\mathbf{y}-\hat{\mathbf{y}}=(\tfrac13,\tfrac13,-\tfrac13)^{\top}$ est perpendiculaire au plan.
:::

::::beispiel [Exemple de calcul]
La matrice $\mathbf{H}$ du [chapitre 1, section 7.4](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrix-vektor-produkt.html#stufe-7-4), a pour colonnes $\mathbf{a}_1=(1,\,0,\,1)^{\top}$ et $\mathbf{a}_2=(0,\,1,\,1)^{\top}$. Son espace des colonnes est le plan de tous les vecteurs dont la troisième composante est la somme des deux premières. Le vecteur $\mathbf{y}=(1,\,1,\,1)^{\top}$ n’en fait pas partie ; le système $\mathbf{H}\mathbf{x}=\mathbf{y}$ n’a donc pas de solution. Avec $\mathbf{x}=(1,\,0)^{\top}$, le résidu est $(0,\,1,\,0)^{\top}$, de longueur $1$ ; avec $\mathbf{x}=(1,\,1)^{\top}$, il vaut $(0,\,0,\,-1)^{\top}$, également de longueur $1$. La sous-section suivante dira si l’on peut faire mieux.
::::

⁠**En bref :** La meilleure solution approchée rend le résidu aussi court que possible ; géométriquement, elle cherche le point de l’espace des colonnes le plus proche de $\mathbf{y}$.

### Les équations normales

<span class="anker" id="stufe-3-3"></span>

Pour la droite, le point le plus proche était le pied de la perpendiculaire : le résidu était perpendiculaire à la droite. Pour un espace des colonnes, la même condition s’impose naturellement : le résidu doit être perpendiculaire à tout vecteur de l’espace des colonnes. Cela s’écrit comme un système d’équations.

:::herleitung Les équations normales
Tout vecteur de l’espace des colonnes est une combinaison linéaire $\sum_jz_j\mathbf{a}_j$ des colonnes. Si $\mathbf{r}$ est perpendiculaire à chaque colonne, il l’est aussi à toute combinaison linéaire de ce type, car $\bigl(\sum_jz_j\mathbf{a}_j\bigr)^{\top}\mathbf{r}=\sum_jz_j\,\mathbf{a}_j^{\top}\mathbf{r}$. Il suffit donc d’exiger pour chaque colonne :

$$\mathbf{a}_j^{\top}(\mathbf{y}-\mathbf{A}\hat{\mathbf{x}})=0\qquad\text{pour }j=1,\dots,n .$$

Les nombres $\mathbf{a}_j^{\top}(\mathbf{y}-\mathbf{A}\hat{\mathbf{x}})$ sont les composantes de $\mathbf{A}^{\top}(\mathbf{y}-\mathbf{A}\hat{\mathbf{x}})$, car les lignes de $\mathbf{A}^{\top}$ sont les colonnes de $\mathbf{A}$. Ensemble, les $n$ conditions s’écrivent donc $\mathbf{A}^{\top}(\mathbf{y}-\mathbf{A}\hat{\mathbf{x}})=\mathbf{0}$, soit, après développement, $\mathbf{A}^{\top}\mathbf{A}\,\hat{\mathbf{x}}=\mathbf{A}^{\top}\mathbf{y}$.
:::

:::definition Définition 3.3 (Équations normales)
<span class="anker" id="satz-3-3"></span>

Au système $\mathbf{A}\mathbf{x}=\mathbf{y}$ avec $\mathbf{A}\in\mathbb{R}^{m\times n}$ sont associées les __équations normales__

<span class="anker" id="gl-3-3"></span>
$$\mathbf{A}^{\top}\mathbf{A}\,\hat{\mathbf{x}}=\mathbf{A}^{\top}\mathbf{y} . \tag{3.3}$$
:::

Le mot « normal » signifie ici « perpendiculaire », comme pour le vecteur normal d’un plan : les équations exigent que le résidu soit perpendiculaire à l’espace des colonnes. La matrice $\mathbf{A}^{\top}\mathbf{A}$ est la matrice de Gram des colonnes du [chapitre 1, section 10.4](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/transponierte-symmetrie-und-gram-matrix.html#stufe-10-4) ; elle est carrée, avec autant de lignes qu’il y a d’inconnues. Un grand système insoluble de $m$ équations devient un petit système de $n$ équations. Pour une seule colonne $\mathbf{a}$, on obtient $\mathbf{a}^{\top}\mathbf{a}\,\hat x=\mathbf{a}^{\top}\mathbf{y}$, la formule de la section précédente.

::::beispiel [Exemple de calcul]
Pour $\mathbf{H}$ et $\mathbf{y}=(1,\,1,\,1)^{\top}$, on a

$$\mathbf{H}^{\top}\mathbf{H}=\begin{pmatrix}2&1\\1&2\end{pmatrix},\qquad \mathbf{H}^{\top}\mathbf{y}=\begin{pmatrix}2\\2\end{pmatrix}.$$

Chaque coefficient est le produit scalaire de deux colonnes ou d’une colonne avec $\mathbf{y}$ (Fig. [7](#abb-7)).

:::abbildung ml/k2rnormal 7
Deux coefficients des équations normales comme produits scalaires : le coefficient $(1,2)$ de $\mathbf{H}^{\top}\mathbf{H}$ est $\mathbf{a}_1^{\top}\mathbf{a}_2$, la première composante de $\mathbf{H}^{\top}\mathbf{y}$ est $\mathbf{a}_1^{\top}\mathbf{y}$.
:::

Les équations normales $2\hat x_1+\hat x_2=2$ et $\hat x_1+2\hat x_2=2$ ont pour solution $\hat{\mathbf{x}}=(\tfrac23,\,\tfrac23)^{\top}$. On a donc $\hat{\mathbf{y}}=\mathbf{H}\hat{\mathbf{x}}=(\tfrac23,\,\tfrac23,\,\tfrac43)^{\top}$ et le résidu $\mathbf{r}=(\tfrac13,\,\tfrac13,\,-\tfrac13)^{\top}$. Vérification : $\mathbf{a}_1^{\top}\mathbf{r}=\tfrac13-\tfrac13=0$ et $\mathbf{a}_2^{\top}\mathbf{r}=\tfrac13-\tfrac13=0$. La longueur du résidu est $\sqrt{3/9}\approx0{,}577$, plus courte que les deux essais de la sous-section précédente.
::::

⁠**En bref :** Les équations normales $\mathbf{A}^{\top}\mathbf{A}\hat{\mathbf{x}}=\mathbf{A}^{\top}\mathbf{y}$ exigent que le résidu soit perpendiculaire à toutes les colonnes.

### Pourquoi les équations normales donnent la meilleure solution

<span class="anker" id="stufe-3-4"></span>

Qu’un résidu perpendiculaire corresponde au point le plus proche, c’était, pour la droite, le théorème de Pythagore. Le même argument vaut ici : il décompose l’erreur en une partie que l’on peut influencer par le choix de $\mathbf{x}$ et une partie que l’on ne peut pas influencer.

:::satz Théorème 3.4 (Les équations normales donnent la meilleure solution approchée)
<span class="anker" id="satz-3-4"></span>

Si $\hat{\mathbf{x}}$ résout les équations normales, alors pour tout vecteur $\mathbf{x}$

<span class="anker" id="gl-3-4"></span>
$$\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert^2=\lVert\mathbf{y}-\mathbf{A}\hat{\mathbf{x}}\rVert^2+\lVert\mathbf{A}(\mathbf{x}-\hat{\mathbf{x}})\rVert^2 . \tag{3.4}$$

Donc $\hat{\mathbf{x}}$ est une meilleure solution approchée. Inversement, toute meilleure solution approchée résout les équations normales, et toutes les meilleures solutions approchées donnent le même point $\hat{\mathbf{y}}=\mathbf{A}\hat{\mathbf{x}}$.
:::

:::beweis Meilleure solution approchée
On décompose $\mathbf{y}-\mathbf{A}\mathbf{x}=(\mathbf{y}-\mathbf{A}\hat{\mathbf{x}})+\mathbf{A}(\hat{\mathbf{x}}-\mathbf{x})$. Le premier terme est le résidu $\mathbf{r}$ associé à $\hat{\mathbf{x}}$, le second est dans l’espace des colonnes. D’après les équations normales, $\mathbf{r}$ est perpendiculaire à l’espace des colonnes, et le théorème de Pythagore donne [(3.4)](#gl-3-4). Le second terme du membre de droite n’est jamais négatif ; donc $\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert\ge\lVert\mathbf{y}-\mathbf{A}\hat{\mathbf{x}}\rVert$ pour tout $\mathbf{x}$.

Si $\mathbf{x}$ est lui aussi une meilleure solution approchée, les deux longueurs sont égales, et [(3.4)](#gl-3-4) impose $\mathbf{A}(\mathbf{x}-\hat{\mathbf{x}})=\mathbf{0}$. Alors $\mathbf{A}\mathbf{x}=\mathbf{A}\hat{\mathbf{x}}$ : les deux vecteurs donnent le même point et le même résidu, et $\mathbf{x}$ vérifie lui aussi les équations normales.
:::

::::beispiel [Exemple de calcul]
Pour $\mathbf{H}$, $\mathbf{y}=(1,\,1,\,1)^{\top}$ et $\mathbf{x}=(1,\,0)^{\top}$, on a $\lVert\mathbf{y}-\mathbf{H}\mathbf{x}\rVert^2=1$. Le membre de droite de [(3.4)](#gl-3-4) vaut $\lVert\mathbf{r}\rVert^2=\tfrac13$ plus $\lVert\mathbf{H}(\tfrac13,\,-\tfrac23)^{\top}\rVert^2=\lVert(\tfrac13,\,-\tfrac23,\,-\tfrac13)^{\top}\rVert^2=\tfrac69$, soit au total $\tfrac13+\tfrac23=1$.
::::

⁠**En bref :** Pythagore décompose le carré de l’erreur en un résidu perpendiculaire, qu’aucun choix de $\mathbf{x}$ ne peut réduire, et en une partie dans l’espace des colonnes, qui s’annule en $\hat{\mathbf{x}}$.

:::hintergrund Ce que l’on peut influencer et ce que l’on ne peut pas
La formule [(3.4)](#gl-3-4) explique pourquoi c’est précisément la position perpendiculaire qui est la bonne condition. Tout candidat $\mathbf{A}\mathbf{x}$ est dans l’espace des colonnes. La distance à $\mathbf{y}$ se compose de deux morceaux perpendiculaires entre eux : un morceau dans l’espace des colonnes, de $\mathbf{A}\mathbf{x}$ à $\hat{\mathbf{y}}$, et le morceau $\mathbf{r}$ perpendiculaire à celui-ci, de $\hat{\mathbf{y}}$ à $\mathbf{y}$. Le premier morceau peut être modifié à volonté par le choix de $\mathbf{x}$ et, en particulier, ramené à zéro. Le second ne dépend pas du tout de $\mathbf{x}$ : c’est la partie de $\mathbf{y}$ qu’aucune combinaison linéaire des colonnes n’atteint. La meilleure solution approchée est exactement celle qui annule le morceau influençable. Que les deux morceaux s’additionnent selon Pythagore, sans pouvoir se compenser mutuellement, tient à leur angle droit.
:::

### Quand la meilleure solution approchée est unique

<span class="anker" id="stufe-3-5"></span>

Les équations normales forment un système carré. Qu’il ait exactement une solution dépend de l’inversibilité de $\mathbf{A}^{\top}\mathbf{A}$. Et ce sont les colonnes de $\mathbf{A}$ qui en décident.

:::satz Théorème 3.5 (Inversibilité de $\mathbf{A}^{\top}\mathbf{A}$)
<span class="anker" id="satz-3-5"></span>

La matrice $\mathbf{A}^{\top}\mathbf{A}$ est inversible si et seulement si les colonnes de $\mathbf{A}$ sont linéairement indépendantes. La meilleure solution approchée est alors unique :

<span class="anker" id="gl-3-5"></span>
$$\hat{\mathbf{x}}=(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}\mathbf{y} . \tag{3.5}$$
:::

:::beweis Inversibilité
D’après le [chapitre 1, section 13.5](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/unabhangigkeit-basis-und-rang.html#stufe-13-5), la matrice carrée $\mathbf{A}^{\top}\mathbf{A}$ est inversible si et seulement si son noyau ne contient que le vecteur nul. Supposons $\mathbf{A}^{\top}\mathbf{A}\mathbf{z}=\mathbf{0}$. Alors on a aussi $\mathbf{z}^{\top}\mathbf{A}^{\top}\mathbf{A}\mathbf{z}=0$, donc $\lVert\mathbf{A}\mathbf{z}\rVert^2=0$ et $\mathbf{A}\mathbf{z}=\mathbf{0}$. Inversement, $\mathbf{A}\mathbf{z}=\mathbf{0}$ entraîne immédiatement $\mathbf{A}^{\top}\mathbf{A}\mathbf{z}=\mathbf{0}$. Les deux noyaux sont donc égaux. Le noyau de $\mathbf{A}$ ne contient que le vecteur nul si et seulement si les colonnes de $\mathbf{A}$ sont linéairement indépendantes.
:::

Si les colonnes sont linéairement dépendantes, il existe une infinité de meilleures solutions approchées. On peut ajouter à l’une d’elles n’importe quel vecteur du noyau de $\mathbf{A}$ sans changer $\mathbf{A}\hat{\mathbf{x}}$. Le point le plus proche $\hat{\mathbf{y}}$ reste néanmoins unique, comme le montre le théorème de la sous-section précédente. Cela concorde avec le [chapitre 1, section 13.6](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/unabhangigkeit-basis-und-rang.html#stufe-13-6) : des caractéristiques dépendantes rendent les poids ambigus, mais pas les prédictions.

::::beispiel [Exemple de calcul 1]
Les colonnes de $\mathbf{H}$ sont linéairement indépendantes, et $\mathbf{H}^{\top}\mathbf{H}=\bigl(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr)$ a pour inverse $\tfrac13\bigl(\begin{smallmatrix}2&-1\\-1&2\end{smallmatrix}\bigr)$. Avec [(3.5)](#gl-3-5), on obtient $\hat{\mathbf{x}}=\tfrac13\bigl(\begin{smallmatrix}2&-1\\-1&2\end{smallmatrix}\bigr)(2,\,2)^{\top}=(\tfrac23,\,\tfrac23)^{\top}$, comme plus haut.
::::

::::beispiel [Exemple de calcul 2]
Pour $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ et $\mathbf{y}=(1,\,1)^{\top}$, les colonnes sont dépendantes. Les équations normales s’écrivent $\bigl(\begin{smallmatrix}5&10\\10&20\end{smallmatrix}\bigr)\hat{\mathbf{x}}=(3,\,6)^{\top}$, c’est-à-dire deux fois la même équation $\hat x_1+2\hat x_2=\tfrac35$. Tout point de cette droite est une meilleure solution approchée, par exemple $(\tfrac35,\,0)^{\top}$ ou $(0,\,\tfrac3{10})^{\top}$. Toutes donnent le même point $\hat{\mathbf{y}}=(\tfrac35,\,\tfrac65)^{\top}$, la projection de $\mathbf{y}$ sur la droite de direction $(1,\,2)^{\top}$.
::::

⁠**En bref :** Si les colonnes sont linéairement indépendantes, $\mathbf{A}^{\top}\mathbf{A}$ est inversible et la meilleure solution approchée $\hat{\mathbf{x}}=(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}\mathbf{y}$ est unique ; sinon, il y en a une infinité, qui donnent toutes le même point le plus proche.

### Une droite passant par trois points

<span class="anker" id="stufe-3-6"></span>

La théorie est maintenant complète, et elle s’applique à un problème de tous les jours. Trois points de mesure $(t,\,y)=(0,\,1)$, $(1,\,2)$ et $(2,\,4)$ doivent être décrits par une droite $y=x_1+x_2\,t$. Les trois points ne sont pas alignés. On cherche l’ordonnée à l’origine $x_1$ et la pente $x_2$ qui conviennent le mieux.

Chaque point de mesure fournit une équation $x_1+x_2\,t_i=y_i$. Avec la colonne de uns pour l’ordonnée à l’origine, comme dans le [chapitre 1, section 8.5](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/lineare-abbildungen.html#stufe-8-5), on obtient le système

$$\mathbf{A}\mathbf{x}=\mathbf{y}\qquad\text{avec}\qquad \mathbf{A}=\begin{pmatrix}1&0\\1&1\\1&2\end{pmatrix},\qquad \mathbf{y}=\begin{pmatrix}1\\2\\4\end{pmatrix}.$$

Les composantes du résidu sont les écarts verticaux des points de mesure à la droite, mesurés dans la direction $y$ (Fig. [8](#abb-8)). La meilleure solution approchée rend la somme de leurs carrés aussi petite que possible. Une telle droite est appelée __droite des moindres carrés__.

:::abbildung ml/k2ausgleich 8
La droite des moindres carrés pour les points de mesure $(0,1)$, $(1,2)$ et $(2,4)$. Les segments rouges sont les composantes du résidu, les écarts verticaux des points à la droite dans la direction $y$. La droite rend la somme de leurs carrés aussi petite que possible, ici $\tfrac1{36}+\tfrac19+\tfrac1{36}=\tfrac16$.
:::

::::beispiel [Exemple de calcul]
On a

$$\mathbf{A}^{\top}\mathbf{A}=\begin{pmatrix}3&3\\3&5\end{pmatrix},\qquad \mathbf{A}^{\top}\mathbf{y}=\begin{pmatrix}7\\10\end{pmatrix},\qquad (\mathbf{A}^{\top}\mathbf{A})^{-1}=\frac16\begin{pmatrix}5&-3\\-3&3\end{pmatrix},$$

donc $\hat{\mathbf{x}}=\tfrac16(35-30,\ -21+30)^{\top}=(\tfrac56,\,\tfrac32)^{\top}$. Les coefficients de $\mathbf{A}^{\top}\mathbf{A}$ et de $\mathbf{A}^{\top}\mathbf{y}$ sont des sommes sur les points de mesure ; la Fig. [9](#abb-9) en montre deux. La droite des moindres carrés est $y=\tfrac56+\tfrac32\,t$. Ses valeurs aux abscisses des mesures sont $\mathbf{A}\hat{\mathbf{x}}=(\tfrac56,\,\tfrac73,\,\tfrac{23}6)^{\top}$, le résidu est $\mathbf{r}=(\tfrac16,\,-\tfrac13,\,\tfrac16)^{\top}$, avec pour somme des carrés $\tfrac16$. Vérification : $\mathbf{A}^{\top}\mathbf{r}=(\tfrac16-\tfrac13+\tfrac16,\ 0-\tfrac13+\tfrac13)^{\top}=(0,\,0)^{\top}$.

La première composante de la vérification a une signification propre. La première colonne de $\mathbf{A}$ est la colonne de uns, et $\mathbf{1}^{\top}\mathbf{r}=0$ signifie : la somme des résidus est nulle. En moyenne, la droite n’est ni trop haute ni trop basse. De façon équivalente, elle passe par le barycentre des points de mesure, ici $(\bar t,\,\bar y)=(1,\,\tfrac73)$ : on a bien $\tfrac56+\tfrac32\cdot1=\tfrac73$.

:::abbildung ml/k2rausgleich 9
Deux coefficients des équations normales de la droite des moindres carrés comme sommes sur les trois points de mesure $(t_i,\,y_i)=(0,1)$, $(1,2)$, $(2,4)$.
:::
::::

⁠**En bref :** Une droite des moindres carrés est la meilleure solution approchée du système qui exige que tous les points de mesure soient sur la droite ; avec une colonne de uns, la somme de ses résidus est nulle.

:::hintergrund Reproduire au mieux une suite à partir d’une autre
Le même calcul construit des règles de prévision pour des suites de nombres. Une piscine en plein air veut reproduire au mieux ses ventes de glaces $d[n]$ du jour $n$ à partir du nombre $x[n]$ de ses visiteurs le jour $n$ et les jours précédents, avec la règle $\sum_kh_k\,x[n-k]$ et les poids $h_0,\dots,h_{K-1}$. Pour chaque jour $n$, c’est une équation pour les $K$ inconnues $h_k$ ; pour de nombreux jours, on obtient donc un système surdéterminé $\mathbf{X}\mathbf h=\mathbf d$. La ligne $n$ de $\mathbf{X}$ contient $x[n],x[n-1],\dots,x[n-K+1]$. Dans les équations normales $\mathbf{X}^{\top}\mathbf{X}\mathbf h=\mathbf{X}^{\top}\mathbf d$, le coefficient $(k,l)$ de $\mathbf{X}^{\top}\mathbf{X}$ est la somme $\sum_nx[n-k]\,x[n-l]$, c’est-à-dire, aux effets de bord près au début et à la fin de la suite, l’intercorrélation de $x$ avec elle-même pour le décalage $l-k$, l’autocorrélation. Dans $\mathbf{X}^{\top}\mathbf d$ figure l’intercorrélation de $d$ et de $x$. Ce sont exactement les produits scalaires de suites décalées du [chapitre 1, section 2.4](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-skalarprodukt.html#stufe-2-4). D’après [(3.3)](#gl-3-3), le résidu $d[n]-\sum_kh_k\,x[n-k]$ de la meilleure règle est perpendiculaire à chaque suite de visiteurs décalée : ce que la règle ne peut pas reproduire n’a rien en commun avec aucune des suites à partir desquelles elle compose sa prévision.
:::

### Les appartements : ce que le chapitre 1 avait laissé ouvert

<span class="anker" id="stufe-3-7"></span>

On peut maintenant répondre à la question du début de la section. On cherche les poids pour la surface et le nombre de pièces qui reproduisent les quatre prix le mieux possible.

::::beispiel [Exemple de calcul]
Pour le système $\mathbf{A}\mathbf{w}=\mathbf{y}$ de la première sous-section, on a

$$\mathbf{A}^{\top}\mathbf{A}=\begin{pmatrix}18\,200&730\\730&30\end{pmatrix},\qquad \mathbf{A}^{\top}\mathbf{y}=\begin{pmatrix}60\,100\\2\,410\end{pmatrix}.$$

La Fig. [10](#abb-10) détaille le calcul de deux des coefficients.

:::abbildung ml/k2rwohnungen 10
Deux coefficients des équations normales des appartements comme produits scalaires : $\mathbf{a}_1=(60,40,90,70)^{\top}$ est la colonne des surfaces, $\mathbf{a}_2=(2,1,4,3)^{\top}$ la colonne des pièces, $\mathbf{y}=(200,130,290,240)^{\top}$ le vecteur des prix.
:::

Les deux colonnes sont linéairement indépendantes ; le déterminant vaut $18\,200\cdot30-730^2=13\,100$. Avec l’inverse du [chapitre 1, section 11.3](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/einheitsmatrix-und-inverse.html#stufe-11-3), on a

$$\hat{\mathbf{w}}=\frac1{13\,100}\begin{pmatrix}30&-730\\-730&18\,200\end{pmatrix}\begin{pmatrix}60\,100\\2\,410\end{pmatrix}=\frac1{13\,100}\begin{pmatrix}43\,700\\-11\,000\end{pmatrix}=\begin{pmatrix}437/131\\-110/131\end{pmatrix}\approx\begin{pmatrix}3{,}336\\-0{,}840\end{pmatrix}.$$

Les prix estimés sont $\mathbf{A}\hat{\mathbf{w}}\approx(198{,}47;\ 132{,}60;\ 296{,}87;\ 230{,}99)^{\top}$, et le résidu est

$$\mathbf{r}=\mathbf{y}-\mathbf{A}\hat{\mathbf{w}}=\frac{20}{131}\,(10,\,-17,\,-45,\,59)^{\top}\approx(1{,}53;\ -2{,}60;\ -6{,}87;\ 9{,}01)^{\top}$$

de longueur $\lVert\mathbf{r}\rVert\approx11{,}72$. Les poids $(3,\,10)^{\top}$ du [chapitre 1](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/vektoren-und-matrizen.html) reproduisaient exactement trois prix, mais laissaient un résidu de longueur $20$. La meilleure solution approchée ne reproduit exactement aucun prix, mais s’écarte nettement moins dans l’ensemble. Vérification : $\mathbf{A}^{\top}\mathbf{r}=\frac{20}{131}(600-680-4050+4130,\ 20-17-180+177)^{\top}=\mathbf{0}$.
::::

⁠**En bref :** La meilleure solution approchée pour les appartements est formée des poids $\hat{\mathbf{w}}\approx(3{,}336;\ -0{,}840)^{\top}$ ; avec une longueur de $11{,}72$, son résidu est nettement plus court que tout résidu qui reproduit exactement trois prix.

:::hintergrund Pourquoi le poids des pièces est négatif
Un poids négatif pour le nombre de pièces semble d’abord faux : davantage de pièces ne devrait pas faire baisser le prix. Le calcul est pourtant juste, et la raison se trouve dans les données. Dans ces quatre appartements, la surface et le nombre de pièces augmentent ensemble : plus l’appartement est grand, plus il a de pièces. Les deux colonnes de $\mathbf{A}$ pointent donc presque dans la même direction ; d’après le [chapitre 1, section 5.2](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/winkel-und-ahnlichkeit.html#stufe-5-2), le cosinus de leur angle vaut $730/\sqrt{18\,200\cdot30}\approx0{,}988$, l’angle n’est donc que d’environ $8{,}9^\circ$. La meilleure combinaison prend beaucoup de la colonne des surfaces et retranche un peu de la colonne des pièces, afin de compenser les écarts des appartements par rapport à la proportion commune. À surface égale, plus de pièces signifie ici des pièces plus petites, ce qui peut effectivement faire baisser un prix ; mais quatre appartements ne suffisent pas à montrer si c’est vrai. Comme dans le [chapitre 1, section 13.6](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/unabhangigkeit-basis-und-rang.html#stufe-13-6) : lorsque des caractéristiques portent presque la même information, les poids pris isolément disent peu de chose, les prédictions en revanche beaucoup.
:::

:::aufgabe Exercice 7 ★ Équations normales à la main
<span class="anker" id="aufg-7"></span>

Le système $x_1=1$, $x_2=2$, $x_1+x_2=6$ n’a pas de solution.

<ol class="al">

<li>

Écrivez-le sous la forme $\mathbf{A}\mathbf{x}=\mathbf{y}$, établissez les équations normales et résolvez-les.

</li>

<li>

Calculez le résidu et vérifiez qu’il est perpendiculaire aux deux colonnes. De combien la meilleure solution approchée manque-t-elle chacune des trois équations ?

</li>

</ol>

:::loesung
(a) Avec $\mathbf{A}=\Bigl(\begin{smallmatrix}1&0\\0&1\\1&1\end{smallmatrix}\Bigr)$ et $\mathbf{y}=(1,\,2,\,6)^{\top}$, on a $\mathbf{A}^{\top}\mathbf{A}=\bigl(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr)$ et $\mathbf{A}^{\top}\mathbf{y}=(1+6,\ 2+6)^{\top}=(7,\,8)^{\top}$. Les équations normales $2\hat x_1+\hat x_2=7$, $\hat x_1+2\hat x_2=8$ ont pour solution

$$\hat{\mathbf{x}}=\frac13\begin{pmatrix}2&-1\\-1&2\end{pmatrix}\begin{pmatrix}7\\8\end{pmatrix}=\frac13\begin{pmatrix}6\\9\end{pmatrix}=\begin{pmatrix}2\\3\end{pmatrix}.$$

(b) $\mathbf{A}\hat{\mathbf{x}}=(2,\,3,\,5)^{\top}$ et $\mathbf{r}=\mathbf{y}-\mathbf{A}\hat{\mathbf{x}}=(-1,\,-1,\,1)^{\top}$. Vérification : $\mathbf{a}_1^{\top}\mathbf{r}=-1+0+1=0$ et $\mathbf{a}_2^{\top}\mathbf{r}=0-1+1=0$. Chacune des trois équations est manquée d’exactement $1$ : $\hat x_1=2$ au lieu de $1$, $\hat x_2=3$ au lieu de $2$, $\hat x_1+\hat x_2=5$ au lieu de $6$. La meilleure solution approchée répartit la contradiction de façon égale ; $\lVert\mathbf{r}\rVert^2=3$.
:::
:::

:::aufgabe Exercice 8 ★★ Une droite des moindres carrés
<span class="anker" id="aufg-8"></span>

Déterminez la droite des moindres carrés $y=x_1+x_2\,t$ pour les points $(1,\,2)$, $(2,\,3)$ et $(3,\,5)$. Calculez le résidu, vérifiez $\mathbf{A}^{\top}\mathbf{r}=\mathbf{0}$ et montrez que la droite passe par le barycentre des trois points.

:::loesung
Avec $\mathbf{A}=\Bigl(\begin{smallmatrix}1&1\\1&2\\1&3\end{smallmatrix}\Bigr)$ et $\mathbf{y}=(2,\,3,\,5)^{\top}$, on a

$$\mathbf{A}^{\top}\mathbf{A}=\begin{pmatrix}3&6\\6&14\end{pmatrix},\qquad \mathbf{A}^{\top}\mathbf{y}=\begin{pmatrix}10\\23\end{pmatrix},\qquad \hat{\mathbf{x}}=\frac16\begin{pmatrix}14&-6\\-6&3\end{pmatrix}\begin{pmatrix}10\\23\end{pmatrix}=\frac16\begin{pmatrix}2\\9\end{pmatrix}=\begin{pmatrix}1/3\\3/2\end{pmatrix}.$$

La droite des moindres carrés est $y=\tfrac13+\tfrac32\,t$, avec les valeurs $\tfrac{11}6$, $\tfrac{10}3$, $\tfrac{29}6$ aux abscisses des points de mesure. Le résidu est $\mathbf{r}=(\tfrac16,\,-\tfrac13,\,\tfrac16)^{\top}$, et $\mathbf{A}^{\top}\mathbf{r}=\bigl(\tfrac16-\tfrac13+\tfrac16,\ \tfrac16-\tfrac23+\tfrac12\bigr)^{\top}=(0,\,0)^{\top}$. Le barycentre est $(\bar t,\,\bar y)=(2,\,\tfrac{10}3)$, et $\tfrac13+\tfrac32\cdot2=\tfrac{10}3$ : la droite passe par ce point. Cela découle de la première composante de $\mathbf{A}^{\top}\mathbf{r}=\mathbf{0}$ : la somme des résidus est nulle, donc $\bar y=\hat x_1+\hat x_2\,\bar t$.
:::
:::

:::aufgabe Exercice 9 ★★ Prix de base et prix au mètre carré
<span class="anker" id="aufg-9"></span>

Les quatre appartements doivent être estimés uniquement d’après leur surface, avec un prix de base : $y\approx x_1+x_2\cdot\text{surface}$.

<ol class="al">

<li>

Écrivez $\mathbf{A}$ avec la colonne de uns et résolvez les équations normales.

</li>

<li>

Calculez le résidu et sa longueur. Comparez avec le résultat de la dernière sous-section.

</li>

</ol>

:::loesung
(a) La matrice comporte la colonne de uns et la colonne des surfaces :

$$\mathbf{A}=\begin{pmatrix}1&60\\1&40\\1&90\\1&70\end{pmatrix},\qquad \mathbf{A}^{\top}\mathbf{A}=\begin{pmatrix}4&260\\260&18\,200\end{pmatrix},\qquad \mathbf{A}^{\top}\mathbf{y}=\begin{pmatrix}860\\60\,100\end{pmatrix}.$$

Le déterminant vaut $4\cdot18\,200-260^2=72\,800-67\,600=5\,200$, et

$$\hat{\mathbf{x}}=\frac1{5\,200}\begin{pmatrix}18\,200&-260\\-260&4\end{pmatrix}\begin{pmatrix}860\\60\,100\end{pmatrix}=\frac1{5\,200}\begin{pmatrix}26\,000\\16\,800\end{pmatrix}=\begin{pmatrix}5\\42/13\end{pmatrix}\approx\begin{pmatrix}5\\3{,}231\end{pmatrix}.$$

Le prix de base est de $5$ milliers d’euros, auxquels s’ajoutent environ $3{,}23$ milliers d’euros par mètre carré.

(b) Les prix estimés sont $5+\tfrac{42}{13}\cdot\text{surface}$, et le résidu est

$$\mathbf{r}=\tfrac1{13}\,(15,\,-55,\,-75,\,115)^{\top}\approx(1{,}15;\ -4{,}23;\ -5{,}77;\ 8{,}85)^{\top},\qquad \lVert\mathbf{r}\rVert=\tfrac1{13}\sqrt{22\,100}\approx11{,}44 .$$

La somme des résidus est nulle, comme l’exige la colonne de uns. Avec la surface et le nombre de pièces, on avait $\lVert\mathbf{r}\rVert\approx11{,}72$ ; le prix de base et la surface, avec deux inconnues également, s’ajustent donc un peu mieux. Le choix des deux colonnes modifie l’espace des colonnes, et donc le point le plus proche.
:::
:::

:::aufgabe Exercice 10 ★★★ Résidus sans colonne de uns
<span class="anker" id="aufg-10"></span>

<ol class="al">

<li>

Montrez que si l’espace des colonnes de $\mathbf{A}$ contient le vecteur de uns $\mathbf{1}$, la somme des composantes du résidu de la meilleure solution approchée est nulle.

</li>

<li>

Vérifiez sur le résidu des appartements de la dernière sous-section que, sans colonne de uns, la somme des résidus n’est en général pas nulle.

</li>

</ol>

:::loesung
(a) Si $\mathbf{1}$ appartient à l’espace des colonnes, le résidu de la meilleure solution approchée est, d’après les équations normales, perpendiculaire à $\mathbf{1}$, car il est perpendiculaire à tout l’espace des colonnes. Donc $\mathbf{1}^{\top}\mathbf{r}=\sum_ir_i=0$.

(b) Le résidu des appartements est $\tfrac{20}{131}(10,\,-17,\,-45,\,59)^{\top}$, de somme $\tfrac{20}{131}(10-17-45+59)=\tfrac{140}{131}\approx1{,}07\ne0$. Sans colonne de uns, $\mathbf{1}$ n’appartient pas ici à l’espace des colonnes, et les résidus ne se compensent pas nécessairement.
:::
:::

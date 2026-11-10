---
title: Projection sur une droite
pfad: Informatique / Apprentissage automatique / Fondements mathématiques / Projection, valeurs propres et décompositions
adresse: informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen
knoten: Chapitre 2 : Projection, valeurs propres et décompositions
nachschlagen: ja
order: 15220300
summary: Un point se trouve à côté d’une droite.
tags: projection orthogonale, matrice de projection, projection
lang: fr
---

<span class="anker" id="stufe-2"></span>

:::zweck
Un point se trouve à côté d’une droite. Quel point de la droite est le plus proche de lui ? Cette section répond à la question pour les droites passant par l’origine, en toute dimension. La réponse est le pied de la perpendiculaire, et la raison en est le théorème de Pythagore.
:::

### Le pied de la perpendiculaire

<span class="anker" id="stufe-2-1"></span>

Une droite passant par l’origine est formée de tous les multiples $t\,\mathbf{a}$ d’un vecteur directeur $\mathbf{a}\ne\mathbf{0}$. On donne un point $\mathbf{y}$, qui n’est pas nécessairement sur elle. On cherche le point de la droite le plus proche de $\mathbf{y}$.

Dans le [chapitre 1, section 5.5](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/winkel-und-ahnlichkeit.html#stufe-5-5), une flèche éclairée perpendiculairement projetait une ombre sur une droite. L’extrémité de l’ombre est le point où la perpendiculaire abaissée de $\mathbf{y}$ rencontre la droite, le *pied de la perpendiculaire*. Le segment qui relie ce point à $\mathbf{y}$ est perpendiculaire à la droite (Fig. [4](#abb-4)). Que ce soit le point le plus proche, la sous-section suivante le montre. Ici, on commence par le calculer, y compris lorsque $\mathbf{a}$ n’est pas normé.

:::herleitung Le pied de la perpendiculaire
Le point cherché est sur la droite ; il s’écrit donc $\hat x\,\mathbf{a}$ avec un nombre $\hat x$ encore inconnu. Le vecteur de liaison $\mathbf{y}-\hat x\,\mathbf{a}$ doit être perpendiculaire à $\mathbf{a}$ :

$$\mathbf{a}^{\top}(\mathbf{y}-\hat x\,\mathbf{a})=0\qquad\Longleftrightarrow\qquad \mathbf{a}^{\top}\mathbf{y}-\hat x\,\mathbf{a}^{\top}\mathbf{a}=0\qquad\Longleftrightarrow\qquad \hat x=\frac{\mathbf{a}^{\top}\mathbf{y}}{\mathbf{a}^{\top}\mathbf{a}} .$$

Comme $\mathbf{a}\ne\mathbf{0}$, on a $\mathbf{a}^{\top}\mathbf{a}=\lVert\mathbf{a}\rVert^2>0$ ; la division est donc permise, et il existe exactement un tel $\hat x$.
:::

:::definition Définition 2.1 (Projection sur une droite)
<span class="anker" id="satz-2-1"></span>

Soit $\mathbf{a}\in\mathbb{R}^n$, $\mathbf{a}\ne\mathbf{0}$. La __projection orthogonale__ de $\mathbf{y}\in\mathbb{R}^n$ sur la droite passant par l’origine de direction $\mathbf{a}$ est le point

<span class="anker" id="gl-2-1"></span>
$$\hat{\mathbf{y}}=\hat x\,\mathbf{a}\qquad\text{avec}\qquad\hat x=\frac{\mathbf{a}^{\top}\mathbf{y}}{\mathbf{a}^{\top}\mathbf{a}} . \tag{2.1}$$
:::

Le point $\hat{\mathbf{y}}$ est un vecteur de $\mathbb{R}^n$ ; le nombre $\hat x$ est sa coordonnée le long de $\mathbf{a}$. Il ne faut pas confondre les deux. Si $\mathbf{a}$ est normé, alors $\mathbf{a}^{\top}\mathbf{a}=1$ et $\hat{\mathbf{y}}=(\mathbf{a}^{\top}\mathbf{y})\,\mathbf{a}$, exactement le point d’ombre du [chapitre 1](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/vektoren-und-matrizen.html).

:::abbildung ml/k2lot 4
La projection de $\mathbf{y}=(4,3)^{\top}$ sur la droite de direction $\mathbf{a}=(1,2)^{\top}$. Le pied de la perpendiculaire est $\hat{\mathbf{y}}=2\mathbf{a}=(2,4)^{\top}$ ; le vecteur de liaison $\mathbf{r}=(2,-1)^{\top}$ (en bleu) est perpendiculaire à la droite. Un autre point de la droite, par exemple $(1,2)^{\top}$, est plus éloigné de $\mathbf{y}$ (en tirets) : le triangle formé par $\mathbf{y}$, $\hat{\mathbf{y}}$ et $(1,2)^{\top}$ est rectangle en $\hat{\mathbf{y}}$, et le côté en tirets est son hypoténuse.
:::

::::beispiel [Exemple de calcul 1]
Pour $\mathbf{a}=(1,\,2)^{\top}$ et $\mathbf{y}=(4,\,3)^{\top}$, on a $\mathbf{a}^{\top}\mathbf{y}=4+6=10$ et $\mathbf{a}^{\top}\mathbf{a}=5$ (Fig. [5](#abb-5)), donc $\hat x=2$ et $\hat{\mathbf{y}}=(2,\,4)^{\top}$. Le vecteur de liaison $\mathbf{y}-\hat{\mathbf{y}}=(2,\,-1)^{\top}$ est perpendiculaire à $\mathbf{a}$ : $2-2=0$.

:::abbildung ml/k2rproj 5
Les deux produits scalaires de la projection pas à pas : $\mathbf{a}^{\top}\mathbf{y}=10$ au numérateur et $\mathbf{a}^{\top}\mathbf{a}=5$ au dénominateur de $\hat x$.
:::
::::

::::beispiel [Exemple de calcul 2]
Pour $\mathbf{a}=(3,\,4)^{\top}$ et $\mathbf{y}=(3,\,1)^{\top}$, on a $\hat x=(9+4)/25=0{,}52$ et $\hat{\mathbf{y}}=0{,}52\,(3,\,4)^{\top}=(1{,}56;\ 2{,}08)^{\top}$, le même point d’ombre que dans le [chapitre 1](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/vektoren-und-matrizen.html) avec le vecteur normé $(0{,}6;\ 0{,}8)^{\top}=\mathbf{a}/5$. La longueur du vecteur directeur ne joue aucun rôle : si l’on remplace $\mathbf{a}$ par $c\,\mathbf{a}$ avec $c\ne0$, $\hat x$ devient $\hat x/c$, et $\hat{\mathbf{y}}$ ne change pas. Si l’on double en revanche $\mathbf{y}$, $\hat{\mathbf{y}}$ double aussi.
::::

⁠**En bref :** La projection de $\mathbf{y}$ sur la droite de direction $\mathbf{a}$ est le pied de la perpendiculaire, $\hat{\mathbf{y}}=\frac{\mathbf{a}^{\top}\mathbf{y}}{\mathbf{a}^{\top}\mathbf{a}}\,\mathbf{a}$.

### Le pied de la perpendiculaire est le point le plus proche

<span class="anker" id="stufe-2-2"></span>

Jusqu’ici, on a seulement montré que le vecteur de liaison vers le pied est perpendiculaire. Que le pied soit aussi le point le plus proche découle du théorème de Pythagore : en s’éloignant du pied le long de la droite, on ajoute au segment perpendiculaire un morceau dans la direction de la droite, et cela ne peut qu’augmenter la distance.

:::satz Théorème 2.2 (Le pied de la perpendiculaire est le point le plus proche)
<span class="anker" id="satz-2-2"></span>

Soit $\hat{\mathbf{y}}=\hat x\,\mathbf{a}$ la projection de $\mathbf{y}$ sur la droite de direction $\mathbf{a}$. Pour tout nombre $t$,

<span class="anker" id="gl-2-2"></span>
$$\lVert\mathbf{y}-t\,\mathbf{a}\rVert^2=\lVert\mathbf{y}-\hat{\mathbf{y}}\rVert^2+(t-\hat x)^2\,\lVert\mathbf{a}\rVert^2 . \tag{2.2}$$

En particulier, $\hat{\mathbf{y}}$ est l’unique point de la droite situé à la plus petite distance de $\mathbf{y}$.
:::

:::beweis Le point le plus proche
On écrit le vecteur qui va de $t\,\mathbf{a}$ à $\mathbf{y}$ comme la somme de deux flèches :

$$\mathbf{y}-t\,\mathbf{a}=(\mathbf{y}-\hat{\mathbf{y}})+(\hat x-t)\,\mathbf{a} .$$

D’après la démonstration ci-dessus, le premier terme est perpendiculaire à $\mathbf{a}$, donc aussi au second. D’après le théorème de Pythagore du [chapitre 1, section 5.3](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/winkel-und-ahnlichkeit.html#stufe-5-3), le carré de la longueur de la somme est la somme des carrés des longueurs, et c’est [(2.2)](#gl-2-2). Le second terme du membre de droite n’est jamais négatif et ne s’annule que pour $t=\hat x$. La distance est donc minimale exactement pour $t=\hat x$.
:::

La longueur du pied vérifie $\lVert\hat{\mathbf{y}}\rVert=|\hat x|\,\lVert\mathbf{a}\rVert=|\mathbf{a}^{\top}\mathbf{y}|/\lVert\mathbf{a}\rVert=|\cos\varphi|\,\lVert\mathbf{y}\rVert$, où $\varphi$ est l’angle entre $\mathbf{a}$ et $\mathbf{y}$. C’est le côté adjacent dans le triangle rectangle d’hypoténuse $\mathbf{y}$.

::::beispiel [Exemple de calcul]
Dans le premier exemple de calcul de la sous-section précédente, $\lVert\mathbf{y}-\hat{\mathbf{y}}\rVert^2=\lVert(2,\,-1)^{\top}\rVert^2=5$. Pour le point $t=1$, c’est-à-dire $(1,\,2)^{\top}$, [(2.2)](#gl-2-2) prédit le carré de la distance $5+1\cdot5=10$, et effectivement $\lVert(3,\,1)^{\top}\rVert^2=10$. Pour $t=3$, c’est-à-dire $(3,\,6)^{\top}$, il vaut également $5+1\cdot5=10=\lVert(1,\,-3)^{\top}\rVert^2$. Les deux points sont à la même distance du pied, de part et d’autre.
::::

⁠**En bref :** Le point le plus proche d’une droite est le pied de la perpendiculaire, car d’après Pythagore, tout pas le long de la droite augmente le carré de la distance.

:::hintergrund Pourquoi il y a exactement un point le plus proche, et pourquoi cela tient à la norme euclidienne
La preuve utilise le théorème de Pythagore, et celui-ci ne vaut que pour les normes issues d’un produit scalaire. Dans le [chapitre 1, section 3.4](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/normen-die-groe-eines-vektors.html#stufe-3-4), il est apparu que la norme 1 n’est pas une telle norme. Avec elle, l’unicité est effectivement perdue. Exemple : la droite de direction $\mathbf{a}=(1,\,1)^{\top}$ et le point $\mathbf{y}=(1,\,0)^{\top}$. Pour $0\le t\le1$, on a

$$\lVert\mathbf{y}-t\,\mathbf{a}\rVert_1=|1-t|+|0-t|=(1-t)+t=1 ,$$

la distance est donc la même pour tous les points entre $\mathbf{0}$ et $\mathbf{a}$ ; en dehors de ce segment, elle est plus grande. Pour cette norme, il existe tout un segment de points les plus proches. Pour la norme euclidienne, il y en a exactement un : $\hat x=\tfrac12$, le point $(\tfrac12,\,\tfrac12)^{\top}$. Cette projection unique, calculable par une formule simple, est l’une des raisons pour lesquelles tant de méthodes utilisent la distance euclidienne.
:::

### La matrice de projection

<span class="anker" id="stufe-2-3"></span>

L’application $\mathbf{y}\mapsto\hat{\mathbf{y}}$ est linéaire : la somme de deux points est envoyée sur la somme de leurs projections, un multiple sur le multiple correspondant. D’après le [chapitre 1, section 8.2](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/lineare-abbildungen.html#stufe-8-2), elle a donc une matrice. On la lit directement en écrivant le nombre $\mathbf{a}^{\top}\mathbf{y}$ de l’autre côté de $\mathbf{a}$ et en regroupant autrement le produit matriciel :

$$\hat{\mathbf{y}}=\mathbf{a}\,\frac{\mathbf{a}^{\top}\mathbf{y}}{\mathbf{a}^{\top}\mathbf{a}}=\frac{\mathbf{a}\,\mathbf{a}^{\top}}{\mathbf{a}^{\top}\mathbf{a}}\,\mathbf{y} .$$

Au numérateur figure le produit extérieur du [chapitre 1, section 9.5](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrixprodukt.html#stufe-9-5).

:::definition Définition 2.3 (Matrice de projection d’une droite)
<span class="anker" id="satz-2-3"></span>

Pour $\mathbf{a}\ne\mathbf{0}$, on appelle

<span class="anker" id="gl-2-3"></span>
$$\mathbf{P}=\frac{\mathbf{a}\,\mathbf{a}^{\top}}{\mathbf{a}^{\top}\mathbf{a}} \tag{2.3}$$

la __matrice de projection__ sur la droite de direction $\mathbf{a}$. On a $\mathbf{P}\mathbf{y}=\hat{\mathbf{y}}$.
:::

:::satz Théorème 2.4 (Propriétés de la matrice de projection d’une droite)
<span class="anker" id="satz-2-4"></span>

On a $\mathbf{P}^{\top}=\mathbf{P}$ et $\mathbf{P}^2=\mathbf{P}$. Les points de la droite restent où ils sont : $\mathbf{P}\mathbf{a}=\mathbf{a}$. Les vecteurs perpendiculaires à $\mathbf{a}$ sont envoyés sur $\mathbf{0}$. Le rang de $\mathbf{P}$ est $1$.
:::

:::beweis Propriétés
On a $(\mathbf{a}\mathbf{a}^{\top})^{\top}=\mathbf{a}\mathbf{a}^{\top}$, donc $\mathbf{P}$ est symétrique. De plus, $\mathbf{P}^2=\mathbf{a}(\mathbf{a}^{\top}\mathbf{a})\mathbf{a}^{\top}/(\mathbf{a}^{\top}\mathbf{a})^2=\mathbf{a}\mathbf{a}^{\top}/(\mathbf{a}^{\top}\mathbf{a})=\mathbf{P}$, car $\mathbf{a}^{\top}\mathbf{a}$ est un nombre. $\mathbf{P}\mathbf{a}=\mathbf{a}\,(\mathbf{a}^{\top}\mathbf{a})/(\mathbf{a}^{\top}\mathbf{a})=\mathbf{a}$. Si $\mathbf{a}^{\top}\mathbf{z}=0$, alors $\mathbf{P}\mathbf{z}=\mathbf{a}\,(\mathbf{a}^{\top}\mathbf{z})/(\mathbf{a}^{\top}\mathbf{a})=\mathbf{0}$. Chaque colonne de $\mathbf{P}$ est un multiple de $\mathbf{a}$, donc le rang est $1$.
:::

L’équation $\mathbf{P}^2=\mathbf{P}$ a une signification simple : un point qui est déjà sur la droite ne bouge plus lors d’une seconde projection.

::::beispiel [Exemple de calcul]
Pour $\mathbf{a}=(1,\,2)^{\top}$, on a

$$\mathbf{P}=\frac15\begin{pmatrix}1&2\\2&4\end{pmatrix},\qquad \mathbf{P}\begin{pmatrix}4\\3\end{pmatrix}=\frac15\begin{pmatrix}4+6\\8+12\end{pmatrix}=\begin{pmatrix}2\\4\end{pmatrix}.$$

Vérification de $\mathbf{P}^2=\mathbf{P}$ : $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)^2=\bigl(\begin{smallmatrix}5&10\\10&20\end{smallmatrix}\bigr)=5\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$, donc $\mathbf{P}^2=\frac1{25}\cdot5\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)=\mathbf{P}$. La matrice $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ était, dans le [chapitre 1, section 11.5](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/einheitsmatrix-und-inverse.html#stufe-11-5), l’exemple d’une matrice sans inverse. On voit maintenant ce qu’elle fait : elle vaut cinq fois une projection et écrase le plan sur la droite de direction $(1,\,2)^{\top}$.
::::

⁠**En bref :** La projection sur une droite est le produit matrice-vecteur par $\mathbf{P}=\mathbf{a}\mathbf{a}^{\top}/(\mathbf{a}^{\top}\mathbf{a})$ ; cette matrice est symétrique et vérifie $\mathbf{P}^2=\mathbf{P}$.

### Projections en général

<span class="anker" id="stufe-2-4"></span>

Il y a aussi des ombres sous une lumière oblique. L’ombre d’un point sur une droite n’est alors plus le pied de la perpendiculaire, mais elle se trouve toujours sur la droite, et un point qui est déjà sur la droite est sa propre ombre. La propriété $\mathbf{P}^2=\mathbf{P}$ est donc conservée, la symétrie ne l’est pas.

:::definition Définition 2.5 (Projection)
<span class="anker" id="satz-2-5"></span>

Une matrice carrée $\mathbf{P}$ telle que $\mathbf{P}^2=\mathbf{P}$ est appelée __projection__. On parle de projection orthogonale si, de plus, pour tout $\mathbf{y}$, le vecteur de liaison $\mathbf{y}-\mathbf{P}\mathbf{y}$ est perpendiculaire à toutes les images $\mathbf{P}\mathbf{z}$.
:::

:::satz Théorème 2.6 (Orthogonale signifie symétrique)
<span class="anker" id="satz-2-6"></span>

Une projection $\mathbf{P}$ est une projection orthogonale si et seulement si $\mathbf{P}^{\top}=\mathbf{P}$.
:::

:::beweis Orthogonale signifie symétrique
Pour tous $\mathbf{y},\mathbf{z}$, on a $(\mathbf{y}-\mathbf{P}\mathbf{y})^{\top}\mathbf{P}\mathbf{z}=\mathbf{y}^{\top}(\mathbf{I}-\mathbf{P})^{\top}\mathbf{P}\mathbf{z}$. Si $\mathbf{P}^{\top}=\mathbf{P}$, alors $(\mathbf{I}-\mathbf{P})^{\top}\mathbf{P}=\mathbf{P}-\mathbf{P}^2=\mathbf 0$, et l’expression est nulle. Inversement, si l’expression est nulle pour tous $\mathbf{y},\mathbf{z}$, la matrice $(\mathbf{I}-\mathbf{P})^{\top}\mathbf{P}$ est la matrice nulle ; en effet, avec $\mathbf{y}=\mathbf{e}_i$ et $\mathbf{z}=\mathbf{e}_l$, l’expression sélectionne son coefficient $(i,l)$. Alors $\mathbf{P}=\mathbf{P}^{\top}\mathbf{P}$, et $\mathbf{P}^{\top}\mathbf{P}$ est symétrique d’après le [chapitre 1, section 10.2](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/transponierte-symmetrie-und-gram-matrix.html#stufe-10-2).
:::

::::beispiel [Exemple de calcul]
La matrice $\mathbf{P}=\bigl(\begin{smallmatrix}1&1\\0&0\end{smallmatrix}\bigr)$ envoie $(x_1,\,x_2)^{\top}$ sur $(x_1+x_2,\,0)^{\top}$. On a $\mathbf{P}^2=\bigl(\begin{smallmatrix}1&1\\0&0\end{smallmatrix}\bigr)\bigl(\begin{smallmatrix}1&1\\0&0\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}1&1\\0&0\end{smallmatrix}\bigr)$, donc $\mathbf{P}$ est une projection sur l’axe des $x_1$. Elle n’est pas symétrique, donc pas orthogonale : le point $(0,\,1)^{\top}$ est envoyé sur $(1,\,0)^{\top}$, et le vecteur de liaison $(-1,\,1)^{\top}$ est oblique par rapport à l’axe. La lumière arrive ici dans la direction $(1,\,-1)^{\top}$. Le point le plus proche sur l’axe des $x_1$, $(0,\,0)^{\top}$, n’est pas celui que fournit cette projection.
::::

⁠**En bref :** Une projection est une matrice telle que $\mathbf{P}^2=\mathbf{P}$ ; elle est orthogonale, c’est-à-dire qu’elle abaisse une perpendiculaire, si et seulement si elle est symétrique.

:::aufgabe Exercice 4 ★ Une projection à la main
<span class="anker" id="aufg-4"></span>

Projetez $\mathbf{y}=(3,\,3,\,0)^{\top}$ sur la droite de direction $\mathbf{a}=(2,\,1,\,2)^{\top}$.

<ol class="al">

<li>

Calculez $\hat x$, $\hat{\mathbf{y}}$ et le vecteur de liaison $\mathbf{r}=\mathbf{y}-\hat{\mathbf{y}}$. Vérifiez $\mathbf{a}^{\top}\mathbf{r}=0$. À quelle distance de la droite se trouve $\mathbf{y}$ ?

</li>

<li>

Écrivez la matrice de projection $\mathbf{P}$ et vérifiez $\mathbf{P}\mathbf{y}=\hat{\mathbf{y}}$ et $\mathbf{P}\mathbf{a}=\mathbf{a}$.

</li>

</ol>

:::loesung
(a) On a $\mathbf{a}^{\top}\mathbf{y}=6+3+0=9$ et $\mathbf{a}^{\top}\mathbf{a}=4+1+4=9$, donc $\hat x=1$ et $\hat{\mathbf{y}}=\mathbf{a}=(2,\,1,\,2)^{\top}$. Le vecteur de liaison est $\mathbf{r}=\mathbf{y}-\hat{\mathbf{y}}=(1,\,2,\,-2)^{\top}$, et $\mathbf{a}^{\top}\mathbf{r}=2+2-4=0$ : il est perpendiculaire à la droite. La distance de $\mathbf{y}$ à la droite vaut $\lVert\mathbf{r}\rVert=\sqrt{1+4+4}=3$ ; d’après le théorème de la section [2.2](#stufe-2-2), aucun point de la droite n’est plus proche.

(b)

$$\mathbf{P}=\frac{\mathbf{a}\mathbf{a}^{\top}}{\mathbf{a}^{\top}\mathbf{a}}=\frac19\begin{pmatrix}4&2&4\\2&1&2\\4&2&4\end{pmatrix},\qquad \mathbf{P}\mathbf{y}=\frac19\begin{pmatrix}12+6\\6+3\\12+6\end{pmatrix}=\begin{pmatrix}2\\1\\2\end{pmatrix},\qquad \mathbf{P}\mathbf{a}=\frac19\begin{pmatrix}8+2+8\\4+1+4\\8+2+8\end{pmatrix}=\mathbf{a} .$$
:::
:::

:::aufgabe Exercice 5 ★★ Pythagore sur la droite
<span class="anker" id="aufg-5"></span>

Soient $\mathbf{a}=(1,\,2)^{\top}$ et $\mathbf{y}=(4,\,3)^{\top}$ comme dans l’exemple de calcul.

<ol class="al">

<li>

Calculez $\lVert\mathbf{y}-t\,\mathbf{a}\rVert^2$ pour $t=0$, $1$, $2$, $3$ et $4$, directement et avec [(2.2)](#gl-2-2).

</li>

<li>

Calculez l’angle $\varphi$ entre $\mathbf{a}$ et $\mathbf{y}$ et vérifiez $\lVert\hat{\mathbf{y}}\rVert=|\cos\varphi|\,\lVert\mathbf{y}\rVert$.

</li>

</ol>

:::loesung
(a) Calcul direct : pour $t=0$, $\lVert(4,\,3)^{\top}\rVert^2=25$ ; pour $t=1$, $\lVert(3,\,1)^{\top}\rVert^2=10$ ; pour $t=2$, $\lVert(2,\,-1)^{\top}\rVert^2=5$ ; pour $t=3$, $\lVert(1,\,-3)^{\top}\rVert^2=10$ ; pour $t=4$, $\lVert(0,\,-5)^{\top}\rVert^2=25$. Avec [(2.2)](#gl-2-2), $\hat x=2$, $\lVert\mathbf{r}\rVert^2=5$ et $\lVert\mathbf{a}\rVert^2=5$ : $5+5(t-2)^2$ donne $25$, $10$, $5$, $10$, $25$. Les valeurs sont symétriques autour du pied $t=2$, car le carré de la distance croît avec le carré du déplacement le long de la droite.

(b) $\cos\varphi=\mathbf{a}^{\top}\mathbf{y}/(\lVert\mathbf{a}\rVert\,\lVert\mathbf{y}\rVert)=10/(\sqrt5\cdot5)=2/\sqrt5\approx0{,}894$, donc $\varphi\approx26{,}57^\circ$. On a $\lVert\hat{\mathbf{y}}\rVert=\lVert(2,\,4)^{\top}\rVert=\sqrt{20}=2\sqrt5$ et $|\cos\varphi|\,\lVert\mathbf{y}\rVert=\tfrac2{\sqrt5}\cdot5=2\sqrt5$.
:::
:::

:::aufgabe Exercice 6 ★★ Quelles matrices sont des projections ?
<span class="anker" id="aufg-6"></span>

Pour chaque matrice, déterminez si c’est une projection et si c’est une projection orthogonale. Pour les projections, décrivez sur quoi l’on projette.

$$\mathbf{P}_1=\begin{pmatrix}1&0\\0&0\end{pmatrix},\quad \mathbf{P}_2=\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix},\quad \mathbf{P}_3=\begin{pmatrix}1&0\\1&0\end{pmatrix},\quad \mathbf{P}_4=\begin{pmatrix}1&2\\0&1\end{pmatrix},\quad \mathbf{P}_5=\mathbf{I},\quad \mathbf{P}_6=\mathbf 0 .$$

:::loesung
Pour chaque matrice, on vérifie d’abord $\mathbf{P}^2=\mathbf{P}$, puis $\mathbf{P}^{\top}=\mathbf{P}$.

<ul>

<li>

$\mathbf{P}_1$ : $\mathbf{P}_1^2=\mathbf{P}_1$ et symétrique, donc la projection orthogonale sur l’axe des $x_1$.

</li>

<li>

$\mathbf{P}_2$ : $\mathbf{P}_2^2=\tfrac14\bigl(\begin{smallmatrix}2&2\\2&2\end{smallmatrix}\bigr)=\mathbf{P}_2$ et symétrique : la projection orthogonale sur la droite de direction $(1,\,1)^{\top}$ ; on a $\mathbf{P}_2=\mathbf{a}\mathbf{a}^{\top}/(\mathbf{a}^{\top}\mathbf{a})$ avec $\mathbf{a}=(1,\,1)^{\top}$.

</li>

<li>

$\mathbf{P}_3$ : $\mathbf{P}_3^2=\bigl(\begin{smallmatrix}1&0\\1&0\end{smallmatrix}\bigr)=\mathbf{P}_3$, mais elle n’est pas symétrique. C’est une projection oblique : elle envoie $(x_1,\,x_2)^{\top}$ sur $x_1\,(1,\,1)^{\top}$, donc sur la droite de direction $(1,\,1)^{\top}$, et le vecteur $(0,\,1)^{\top}$ sur zéro. La lumière arrive dans la direction $(0,\,1)^{\top}$, et non perpendiculairement à la droite.

</li>

<li>

$\mathbf{P}_4$ : $\mathbf{P}_4^2=\bigl(\begin{smallmatrix}1&4\\0&1\end{smallmatrix}\bigr)\ne\mathbf{P}_4$. Ce n’est pas une projection, mais un cisaillement ; appliqué deux fois, il cisaille deux fois plus fort.

</li>

<li>

$\mathbf{P}_5=\mathbf{I}$ : $\mathbf{I}^2=\mathbf{I}$, symétrique. C’est la projection orthogonale sur le plan tout entier ; elle laisse tout à sa place.

</li>

<li>

$\mathbf{P}_6=\mathbf 0$ : $\mathbf 0^2=\mathbf 0$, symétrique. C’est la projection orthogonale sur l’origine.

</li>

</ul>
:::
:::

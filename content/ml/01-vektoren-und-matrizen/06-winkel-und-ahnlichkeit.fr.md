---
title: Angles et similarité
pfad: Informatique / Apprentissage automatique / Fondements mathématiques / Vecteurs et matrices
adresse: informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen
knoten: Chapitre 1 : Vecteurs et matrices
nachschlagen: ja
order: 15210600
summary: Deux vecteurs peuvent pointer dans des directions semblables, même s’ils ont des longueurs différentes.
tags: angle, orthogonaux, similarité cosinus
lang: fr
---

<span class="anker" id="stufe-5"></span>

:::zweck
Deux vecteurs peuvent pointer dans des directions semblables, même s’ils ont des longueurs différentes. Cette section mesure l’angle qu’ils forment. Elle repose sur une inégalité qui indique en outre précisément quand une comparaison avec un motif réagit le plus fortement.
:::

### L’inégalité de Cauchy-Schwarz

<span class="anker" id="stufe-5-1"></span>

Jusqu’où le produit scalaire de deux vecteurs peut-il aller lorsque leurs longueurs sont fixées ? Un essai : $\mathbf{u}=(1,\,2,\,2)^{\top}$ a pour longueur $3$, $\mathbf{v}=(2,\,0,\,1)^{\top}$ a pour longueur $\sqrt5\approx2{,}24$. Leur produit scalaire vaut $2+0+2=4$, nettement moins que le produit des longueurs $3\cdot2{,}24\approx6{,}71$. Si l’on prend à la place $\mathbf{v}=2\mathbf{u}$, un vecteur de même direction et de longueur $6$, on a $\mathbf{u}^{\top}(2\mathbf{u})=2\cdot9=18=3\cdot6$ : exactement le produit des longueurs. On ne peut pas faire mieux.

:::satz Théorème 5.1 (Inégalité de Cauchy-Schwarz)
<span class="anker" id="satz-5-1"></span>

Pour tous $\mathbf{u},\mathbf{v}\in\mathbb{R}^d$, on a

<span class="anker" id="gl-5-1"></span>
$$|\mathbf{u}^{\top}\mathbf{v}|\le\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert . \tag{5.1}$$

L’égalité a lieu si et seulement si l’un des deux vecteurs est un multiple de l’autre.
:::

:::beweis Inégalité de Cauchy-Schwarz
Si $\mathbf{v}=\mathbf{0}$, les deux membres sont nuls. Sinon, on considère, pour un nombre $t$ quelconque, le vecteur $\mathbf{u}-t\,\mathbf{v}$. Le carré de sa longueur n’est jamais négatif, et d’après les règles de calcul du produit scalaire

$$0\le\lVert\mathbf{u}-t\,\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2-2t\,\mathbf{u}^{\top}\mathbf{v}+t^2\lVert\mathbf{v}\rVert^2 .$$

Cela vaut pour tout $t$, donc aussi pour $t=\mathbf{u}^{\top}\mathbf{v}/\lVert\mathbf{v}\rVert^2$, la valeur pour laquelle le membre de droite, vu comme une parabole en $t$, est minimal. En substituant :

$$0\le\lVert\mathbf{u}\rVert^2-2\,\frac{(\mathbf{u}^{\top}\mathbf{v})^2}{\lVert\mathbf{v}\rVert^2}+\frac{(\mathbf{u}^{\top}\mathbf{v})^2}{\lVert\mathbf{v}\rVert^2}=\lVert\mathbf{u}\rVert^2-\frac{(\mathbf{u}^{\top}\mathbf{v})^2}{\lVert\mathbf{v}\rVert^2}.$$

Après multiplication par $\lVert\mathbf{v}\rVert^2>0$, cela donne $(\mathbf{u}^{\top}\mathbf{v})^2\le\lVert\mathbf{u}\rVert^2\lVert\mathbf{v}\rVert^2$ ; en prenant la racine, on obtient [(5.1)](#gl-5-1).

L’égalité a lieu si et seulement si $\lVert\mathbf{u}-t\,\mathbf{v}\rVert=0$ pour ce $t$, c’est-à-dire si $\mathbf{u}=t\,\mathbf{v}$. Inversement, pour $\mathbf{u}=c\,\mathbf{v}$, on a effectivement $|\mathbf{u}^{\top}\mathbf{v}|=|c|\,\lVert\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert$.
:::

::::beispiel [Exemple de calcul]
Pour $\mathbf{u}=(1,\,2,\,2)^{\top}$ et $\mathbf{v}=(2,\,0,\,1)^{\top}$, on a $|\mathbf{u}^{\top}\mathbf{v}|=4\le3\cdot\sqrt5\approx6{,}71$. L’inégalité est stricte, parce que $\mathbf{v}$ n’est pas un multiple de $\mathbf{u}$.
::::

L’inégalité permet de rattraper ce qui, dans la sous-section [3.4](normen-die-groe-eines-vektors.html#stufe-3-4), n’était justifié que de manière intuitive : l’inégalité triangulaire de la norme euclidienne. On a

$$\lVert\mathbf{u}+\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2+2\,\mathbf{u}^{\top}\mathbf{v}+\lVert\mathbf{v}\rVert^2\le\lVert\mathbf{u}\rVert^2+2\,\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert+\lVert\mathbf{v}\rVert^2=\bigl(\lVert\mathbf{u}\rVert+\lVert\mathbf{v}\rVert\bigr)^2 ,$$

et en prenant la racine, on obtient (N3).

⁠**En bref :** En valeur absolue, le produit scalaire vaut au plus le produit des longueurs, et il lui est égal si et seulement si les vecteurs se trouvent sur une même droite passant par l’origine.

:::hintergrund Pourquoi le produit scalaire reconnaît les motifs : l’énoncé précis
Dans la sous-section [2.4](das-skalarprodukt.html#stufe-2-4), la comparaison avec un motif était une image intuitive : le produit scalaire $\mathbf{w}^{\top}\mathbf{x}$ est grand lorsque la série temporelle suit le motif. L’inégalité de Cauchy-Schwarz en fait un énoncé précis. Si l’on ne compare que des séries temporelles de même longueur $\lVert\mathbf{x}\rVert$, $\mathbf{w}^{\top}\mathbf{x}$ est toujours compris entre $-\lVert\mathbf{w}\rVert\,\lVert\mathbf{x}\rVert$ et $+\lVert\mathbf{w}\rVert\,\lVert\mathbf{x}\rVert$. La plus grande valeur est atteinte exactement par la série temporelle qui est un multiple positif du motif, la plus petite par le multiple négatif. Parmi toutes les séries temporelles de même longueur, la comparaison réagit donc le plus fortement au motif lui-même.

⁠**Exemple de calcul :** Le motif alterné $\mathbf{w}=(1,-1,1,-1)^{\top}$ a pour longueur $2$. Parmi toutes les séries temporelles de longueur $2$, $\mathbf{x}=\mathbf{w}$ donne la plus grande valeur, $4=2\cdot2$, la série temporelle $(2,0,0,0)^{\top}$ seulement $2$, et $\mathbf{x}=-\mathbf{w}$ la plus petite valeur, $-4$.

Toute recherche qui décrit des textes ou des images par des vecteurs exploite le même énoncé : parmi tous les vecteurs de même longueur, celui qui donne le plus grand produit scalaire avec la requête est celui qui est un multiple positif de la requête. Pour que la longueur ne fausse pas le résultat, on ramène au préalable tous les vecteurs à la même longueur.
:::

### L’angle entre deux vecteurs

<span class="anker" id="stufe-5-2"></span>

Deux flèches issues de l’origine forment un angle. Il indique à quel point leurs directions se ressemblent, indépendamment de leurs longueurs. Dans le plan, on peut le mesurer au rapporteur. Pour des vecteurs ayant de nombreuses composantes, il faut une formule, et c’est le produit scalaire qui la fournit.

:::herleitung Le produit scalaire dans le plan
Les flèches $\mathbf{u}$ et $\mathbf{v}$ et leur flèche de liaison $\mathbf{u}-\mathbf{v}$ forment un triangle. Si $\varphi$ est l’angle entre $\mathbf{u}$ et $\mathbf{v}$, la loi des cosinus (théorème d’Al-Kashi) de la géométrie scolaire donne

$$\lVert\mathbf{u}-\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2+\lVert\mathbf{v}\rVert^2-2\,\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert\cos\varphi .$$

D’après [(4.1)](abstande-und-einheiten.html#gl-4-1), ce même membre de gauche est égal à $\lVert\mathbf{u}\rVert^2+\lVert\mathbf{v}\rVert^2-2\,\mathbf{u}^{\top}\mathbf{v}$. En comparant les deux lignes, il reste

$$\mathbf{u}^{\top}\mathbf{v}=\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert\cos\varphi .$$

Dans le plan et dans l’espace, le produit scalaire est donc le produit des longueurs multiplié par le cosinus de l’angle que forment les deux vecteurs.
:::

En dimension supérieure, il n’existe pas de rapporteur. On inverse donc le raisonnement et l’on utilise la formule comme définition.

:::definition Définition 5.2 (Angle)
<span class="anker" id="satz-5-2"></span>

Pour $\mathbf{u},\mathbf{v}\in\mathbb{R}^d$, tous deux différents de $\mathbf{0}$, l’__angle__ $\varphi$ entre $\mathbf{u}$ et $\mathbf{v}$ est le nombre $\varphi\in[0^\circ,180^\circ]$ tel que

<span class="anker" id="gl-5-2"></span>
$$\cos\varphi=\frac{\mathbf{u}^{\top}\mathbf{v}}{\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert} . \tag{5.2}$$
:::

Cette définition n’est possible que parce que le membre de droite est toujours compris entre $-1$ et $1$ d’après l’inégalité de Cauchy-Schwarz. À chacun de ces nombres correspond exactement un angle entre $0^\circ$ et $180^\circ$. Le signe du produit scalaire indique si l’angle est aigu ($\mathbf{u}^{\top}\mathbf{v}>0$), droit ($\mathbf{u}^{\top}\mathbf{v}=0$) ou obtus ($\mathbf{u}^{\top}\mathbf{v}<0$).

::::beispiel [Exemple de calcul]
Pour $(1,\,0)^{\top}$ et $(1,\,1)^{\top}$, on a $\cos\varphi=1/\sqrt2$, donc $\varphi=45^\circ$. Pour $(1,\,0,\,1)^{\top}$ et $(1,\,1,\,0)^{\top}$, on a $\cos\varphi=\tfrac12$, donc $\varphi=60^\circ$ (Fig. [22](#abb-22)). Pour $\mathbf{u}=(1,\,2,\,2)^{\top}$ et $\mathbf{v}=(2,\,0,\,1)^{\top}$, on a $\cos\varphi=4/(3\sqrt5)\approx0{,}596$, donc $\varphi\approx53{,}4^\circ$.

:::abbildung ml/k1rwinkel 22
L’angle entre $(1,\,0,\,1)^{\top}$ et $(1,\,1,\,0)^{\top}$ : au numérateur le produit scalaire, au dénominateur les deux longueurs.
:::
::::

⁠**En bref :** Le cosinus de l’angle entre deux vecteurs est leur produit scalaire divisé par le produit de leurs longueurs.

### Vecteurs orthogonaux

<span class="anker" id="stufe-5-3"></span>

Lorsque le produit scalaire de deux vecteurs est nul, aucun des deux n’apporte de contribution dans la direction de l’autre. Dans le plan, les flèches sont alors perpendiculaires. Ce cas est si important qu’il porte un nom à part.

:::definition Définition 5.3 (Orthogonaux)
<span class="anker" id="satz-5-3"></span>

Deux vecteurs $\mathbf{u},\mathbf{v}\in\mathbb{R}^d$ sont dits __orthogonaux__ si $\mathbf{u}^{\top}\mathbf{v}=0$.
:::

Si les deux vecteurs sont différents de $\mathbf{0}$, leur angle vaut exactement $90^\circ$ d’après [(5.2)](#gl-5-2). Le vecteur nul est orthogonal à tout vecteur.

:::satz Théorème 5.4 (Théorème de Pythagore)
<span class="anker" id="satz-5-4"></span>

Si $\mathbf{u}$ et $\mathbf{v}$ sont orthogonaux, alors $\lVert\mathbf{u}+\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2+\lVert\mathbf{v}\rVert^2$.
:::

Cela découle immédiatement de $\lVert\mathbf{u}+\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2+2\,\mathbf{u}^{\top}\mathbf{v}+\lVert\mathbf{v}\rVert^2$, car le terme du milieu est nul.

::::beispiel [Exemple de calcul 1]
$(1,\,2,\,2)^{\top}$ et $(2,\,0,\,-1)^{\top}$ sont orthogonaux, car $2+0-2=0$. Leur somme $(3,\,2,\,1)^{\top}$ a pour carré de la longueur $14=9+5$.
::::

::::beispiel [Exemple de calcul 2] deux motifs qui ne se gênent pas
Le motif constant $\mathbf 1=(1,\,1,\,1,\,1)^{\top}$ et le motif alterné $\mathbf{w}=(1,\,-1,\,1,\,-1)^{\top}$ de la sous-section [2.4](das-skalarprodukt.html#stufe-2-4) sont orthogonaux, $\mathbf 1^{\top}\mathbf{w}=0$. Une série temporelle composée de $2$ fois le motif constant et de $1$ fois le motif alterné est $\mathbf{x}=2\cdot\mathbf 1+\mathbf{w}=(3,\,1,\,3,\,1)^{\top}$. La comparaison avec le motif constant donne $\mathbf 1^{\top}\mathbf{x}=8=2\cdot4$, la comparaison avec le motif alterné $\mathbf{w}^{\top}\mathbf{x}=4=1\cdot4$ (Fig. [23](#abb-23)). Chaque comparaison trouve exactement sa propre part, multipliée par $\lVert\mathbf 1\rVert^2=\lVert\mathbf{w}\rVert^2=4$ ; l’autre part ne la perturbe pas.

:::abbildung ml/k1rortho 23
Les deux motifs sont orthogonaux (en haut). La comparaison de la série temporelle $\mathbf{x}=2\cdot\mathbf 1+\mathbf{w}$ avec chaque motif fournit la part de ce motif, multipliée par $4$.
:::
::::

⁠**En bref :** Orthogonal signifie produit scalaire nul ; des flèches orthogonales sont perpendiculaires, et le théorème de Pythagore s’applique à elles.

:::hintergrund Pourquoi des motifs orthogonaux ne se gênent pas, et quel rapport avec les coefficients de Fourier
Si une série temporelle est une combinaison linéaire $\mathbf{x}=\alpha\,\mathbf 1+\beta\,\mathbf{w}$ de deux motifs orthogonaux, alors, d’après les règles de calcul,

$$\mathbf 1^{\top}\mathbf{x}=\alpha\,\mathbf 1^{\top}\mathbf 1+\beta\,\mathbf 1^{\top}\mathbf{w}=\alpha\,\lVert\mathbf 1\rVert^2+0 ,\qquad\text{donc}\qquad \alpha=\frac{\mathbf 1^{\top}\mathbf{x}}{\lVert\mathbf 1\rVert^2} .$$

La comparaison avec un motif ne mesure donc que la part de ce motif, parce que la contribution de l’autre motif disparaît avec le facteur $\mathbf 1^{\top}\mathbf{w}=0$. Si les motifs n’étaient pas orthogonaux, chaque comparaison compterait aussi un morceau de l’autre part.

C’est exactement ainsi que sont construits les coefficients d’une série de Fourier, qui décompose une courbe périodique, par exemple le son d’une note tenue, en oscillations cosinus et sinus. Pour une fonction $s(t)$ de période $T$ et $\omega_0=2\pi/T$, on a

$$a_k=\frac{2}{T}\int_0^Ts(t)\cos(k\omega_0t)\,\mathrm{d} t=\frac{\int_0^Ts(t)\cos(k\omega_0t)\,\mathrm{d} t}{\int_0^T\cos^2(k\omega_0t)\,\mathrm{d} t}\qquad(k\ge1),$$

car $\int_0^T\cos^2(k\omega_0t)\,\mathrm{d} t=T/2$. L’intégrale du produit de deux fonctions joue le rôle du produit scalaire, et les fonctions cosinus et sinus de fréquences différentes sont orthogonales en ce sens : l’intégrale de leur produit sur une période est nulle. C’est pourquoi on peut calculer chaque coefficient de Fourier séparément, sans connaître les autres.
:::

### La similarité cosinus

<span class="anker" id="stufe-5-4"></span>

Parfois, la longueur d’un vecteur est secondaire. Un texte peut être décrit par un vecteur dont la composante $j$ compte combien de fois le mot $j$ d’une liste de mots fixée apparaît dans le texte. Un compte rendu détaillé d’un match de football contient les mots « but » et « ballon » plus souvent qu’une brève dépêche sur le même match, mais dans la même proportion. Les deux vecteurs ont des longueurs différentes, mais pointent dans la même direction. Pour le contenu, c’est la direction qui compte.

:::definition Définition 5.5 (Similarité cosinus)
<span class="anker" id="satz-5-5"></span>

La __similarité cosinus__ de deux vecteurs $\mathbf{u},\mathbf{v}\ne\mathbf{0}$ est le nombre

<span class="anker" id="gl-5-3"></span>
$$\frac{\mathbf{u}^{\top}\mathbf{v}}{\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert}\in[-1,\,1] , \tag{5.3}$$

c’est-à-dire le cosinus de leur angle.
:::

Elle vaut $1$ lorsque les vecteurs pointent dans la même direction, $0$ lorsqu’ils sont orthogonaux, et $-1$ lorsqu’ils pointent en sens opposés. Si l’on multiplie l’un des vecteurs par un nombre positif, elle ne change pas, car ce nombre se simplifie.

::::beispiel [Exemple de calcul]
Trois textes et leurs décomptes des mots « but », « ballon » et « élection » :

$$\mathbf{x}_1=(3,\,2,\,0)^{\top},\qquad \mathbf{x}_2=(6,\,4,\,0)^{\top},\qquad \mathbf{x}_3=(0,\,1,\,3)^{\top} .$$

Le texte 2 est un compte rendu deux fois plus long du même match, le texte 3 traite surtout d’une élection. La similarité cosinus des textes 1 et 2 vaut $1$, celle des textes 1 et 3 vaut $2/\sqrt{130}\approx0{,}175$ (Fig. [24](#abb-24)). De même, celle des textes 2 et 3 vaut $4/(\sqrt{52}\,\sqrt{10})=4/\sqrt{520}\approx0{,}175$.

:::abbildung ml/k1rkosinus 24
Deux similarités cosinus des décomptes de mots : à chaque fois un produit scalaire au numérateur et deux longueurs au dénominateur.
:::

Les distances, en revanche, valent $\lVert\mathbf{x}_1-\mathbf{x}_2\rVert=\sqrt{13}\approx3{,}61$, $\lVert\mathbf{x}_1-\mathbf{x}_3\rVert=\sqrt{19}\approx4{,}36$ et $\lVert\mathbf{x}_2-\mathbf{x}_3\rVert=\sqrt{54}\approx7{,}35$. Selon la distance, le texte 1 n’est guère plus éloigné du texte 3 que du texte 2, bien que le texte 2 traite exactement du même sujet. La similarité cosinus le reconnaît immédiatement : elle vaut $1$, et l’angle avec le texte 3, d’environ $79{,}9^\circ$, est presque droit.
::::

⁠**En bref :** La similarité cosinus ne compare que les directions de deux vecteurs et ignore leurs longueurs.

:::hintergrund La similarité cosinus n’est pas la même chose que la corrélation
Si l’on centre au préalable deux vecteurs de même longueur (sous-section [4.3](abstande-und-einheiten.html#stufe-4-3)), le cosinus de leur angle mesure si les composantes se situent en même temps au-dessus ou au-dessous de leur moyenne respective. Ce nombre s’appelle coefficient de corrélation. Sans centrage, on obtient souvent tout autre chose. Exemple : $\mathbf{a}=(1,2,3)^{\top}$, $\mathbf{b}=(3,4,5)^{\top}$ et $\mathbf{c}=(3,2,1)^{\top}$. La similarité cosinus de $\mathbf{a}$ et $\mathbf{b}$ vaut environ $0{,}983$, celle de $\mathbf{a}$ et $\mathbf{c}$ tout de même $0{,}714$ ; toutes deux sont donc nettement positives. Une fois centrés, on a $\tilde{\mathbf{a}}=(-1,0,1)^{\top}$, $\tilde{\mathbf{b}}=(-1,0,1)^{\top}$ et $\tilde{\mathbf{c}}=(1,0,-1)^{\top}$ : le coefficient de corrélation de $\mathbf{a}$ et $\mathbf{b}$ vaut $1$, mais celui de $\mathbf{a}$ et $\mathbf{c}$ vaut $-1$, car $\mathbf{c}$ décroît exactement là où $\mathbf{a}$ croît. La similarité cosinus non centrée n’était positive que parce que tous les nombres sont positifs et que les trois vecteurs pointent donc à peu près dans la même direction.
:::

### Le produit scalaire comme longueur d’ombre

<span class="anker" id="stufe-5-5"></span>

Le produit scalaire avec un vecteur normé a une signification géométrique simple. Imaginez une droite passant par l’origine et dirigée par le vecteur normé $\mathbf{u}$, et faites tomber la lumière perpendiculairement sur cette droite. La flèche $\mathbf{x}$ projette alors une ombre sur la droite (Fig. [25](#abb-25)). Quelle est sa longueur ?

:::abbildung ml/k1schatten 25
L’ombre de la flèche $\mathbf{x}=(3,1)^{\top}$ sur la droite dirigée par le vecteur normé $\mathbf{u}=(0{,}6;\,0{,}8)^{\top}$. La lumière tombe perpendiculairement sur la droite (en tirets). L’ombre (en bleu clair) a pour longueur $\mathbf{u}^{\top}\mathbf{x}=\lVert\mathbf{x}\rVert\cos\varphi=2{,}6$ et se termine au point $(\mathbf{u}^{\top}\mathbf{x})\,\mathbf{u}=(1{,}56;\,2{,}08)^{\top}$.
:::

:::satz Théorème 5.6 (Longueur de l’ombre)
<span class="anker" id="satz-5-6"></span>

Soit $\mathbf{u}\in\mathbb{R}^d$ normé, c’est-à-dire $\lVert\mathbf{u}\rVert=1$. Alors $\mathbf{u}^{\top}\mathbf{x}$ est la longueur algébrique de l’ombre de $\mathbf{x}$ sur la droite de direction $\mathbf{u}$ : l’ombre se termine au point $(\mathbf{u}^{\top}\mathbf{x})\,\mathbf{u}$, et la flèche de liaison $\mathbf{x}-(\mathbf{u}^{\top}\mathbf{x})\,\mathbf{u}$ est orthogonale à $\mathbf{u}$.
:::

:::beweis Longueur de l’ombre
Avec $\mathbf{u}^{\top}\mathbf{u}=\lVert\mathbf{u}\rVert^2=1$, on a $\mathbf{u}^{\top}\bigl(\mathbf{x}-(\mathbf{u}^{\top}\mathbf{x})\,\mathbf{u}\bigr)=\mathbf{u}^{\top}\mathbf{x}-(\mathbf{u}^{\top}\mathbf{x})\,\mathbf{u}^{\top}\mathbf{u}=0$. La flèche de liaison est donc perpendiculaire à la droite ; c’est exactement la direction d’où vient la lumière. Le point d’ombre $(\mathbf{u}^{\top}\mathbf{x})\,\mathbf{u}$ se trouve à la distance $|\mathbf{u}^{\top}\mathbf{x}|$ de l’origine, parce que $\mathbf{u}$ a pour longueur $1$. Il se trouve dans la direction de $\mathbf{u}$ si $\mathbf{u}^{\top}\mathbf{x}>0$, et dans la direction opposée si $\mathbf{u}^{\top}\mathbf{x}<0$. Dans le triangle rectangle formé par $\mathbf{x}$, l’ombre et la flèche de liaison, $\mathbf{x}$ est l’hypoténuse ; c’est pourquoi la longueur de l’ombre vaut aussi $\lVert\mathbf{x}\rVert\cos\varphi$.
:::

Si $\mathbf{u}$ n’est pas normé, $\mathbf{u}^{\top}\mathbf{x}$ est la longueur de l’ombre de $\mathbf{x}$ dans la direction de $\mathbf{u}$, multipliée par $\lVert\mathbf{u}\rVert$.

::::beispiel [Exemple de calcul]
$\mathbf{u}=(0{,}6;\ 0{,}8)^{\top}$ est normé, car $0{,}36+0{,}64=1$. Pour $\mathbf{x}=(3,\,1)^{\top}$, la longueur de l’ombre vaut $\mathbf{u}^{\top}\mathbf{x}=2{,}6$ (Fig. [26](#abb-26)), le point d’ombre est $2{,}6\,\mathbf{u}=(1{,}56;\ 2{,}08)^{\top}$ et la flèche de liaison $\mathbf{x}-2{,}6\,\mathbf{u}=(1{,}44;\ -1{,}08)^{\top}$. Celle-ci est orthogonale à $\mathbf{u}$ : $0{,}6\cdot1{,}44-0{,}8\cdot1{,}08=0$. Avec $\lVert\mathbf{x}\rVert=\sqrt{10}\approx3{,}162$, on a $\cos\varphi=2{,}6/3{,}162\approx0{,}822$, donc $\varphi\approx34{,}7^\circ$.

:::abbildung ml/k1rschatten 26
La longueur de l’ombre de $\mathbf{x}$ dans la direction du vecteur normé $\mathbf{u}$, comme produit scalaire.
:::
::::

Pour une somme pondérée, cela signifie : si les poids sont normés, $\mathbf{w}^{\top}\mathbf{x}$ indique jusqu’où l’exemple $\mathbf{x}$ s’étend dans la direction de $\mathbf{w}$. Tous les points qui donnent la même valeur $\mathbf{w}^{\top}\mathbf{x}$ projettent la même ombre. Dans le plan, ils se trouvent donc sur une droite perpendiculaire à $\mathbf{w}$, dans l’espace sur un plan perpendiculaire à $\mathbf{w}$.

⁠**En bref :** Pour un vecteur normé $\mathbf{u}$, $\mathbf{u}^{\top}\mathbf{x}$ est la longueur de l’ombre que $\mathbf{x}$ projette sur la droite de direction $\mathbf{u}$.

:::aufgabe Exercice 12 ★ Angle et orthogonalité
<span class="anker" id="aufg-12"></span>

<ol class="al">

<li>

Calculez l’angle entre $(2,\,1,\,2)^{\top}$ et $(1,\,0,\,1)^{\top}$ et vérifiez l’inégalité de Cauchy-Schwarz.

</li>

<li>

$(1,\,1,\,0)^{\top}$ et $(1,\,-1,\,3)^{\top}$ sont-ils orthogonaux ?

</li>

<li>

Trouvez un vecteur $\mathbf{v}\ne\mathbf{0}$ orthogonal à $\mathbf{u}=(1,\,2)^{\top}$ et vérifiez le théorème de Pythagore pour $\mathbf{u}$ et $\mathbf{v}$.

</li>

</ol>

:::loesung
(a) Le produit scalaire vaut $2+0+2=4$, les longueurs sont $3$ et $\sqrt2$. Donc $\cos\varphi=4/(3\sqrt2)\approx0{,}943$ et $\varphi\approx19{,}5^\circ$. Cauchy-Schwarz : $4\le3\sqrt2\approx4{,}243$.

(b) $1\cdot1+1\cdot(-1)+0\cdot3=0$ : oui, ils sont orthogonaux.

(c) Pour $\mathbf{v}=(v_1,v_2)^{\top}$, la condition exige $v_1+2v_2=0$. Une solution est $\mathbf{v}=(2,\,-1)^{\top}$, de même que tout multiple non nul de ce vecteur. Vérification du théorème de Pythagore : $\mathbf{u}+\mathbf{v}=(3,\,1)^{\top}$ a pour carré de la longueur $10$, et $\lVert\mathbf{u}\rVert^2+\lVert\mathbf{v}\rVert^2=5+5=10$.
:::
:::

:::aufgabe Exercice 13 ★★ Quel texte est semblable ?
<span class="anker" id="aufg-13"></span>

Quatre textes, dans lesquels on a de nouveau compté les mots « but », « ballon » et « élection » : $\mathbf{x}_a=(2,\,0,\,1)^{\top}$, $\mathbf{x}_b=(0,\,3,\,0)^{\top}$, $\mathbf{x}_c=(4,\,0,\,2)^{\top}$ et $\mathbf{x}_d=(1,\,1,\,1)^{\top}$.

<ol class="al">

<li>

Calculez la similarité cosinus et la distance euclidienne du texte $a$ aux trois autres textes.

</li>

<li>

Quel texte ressemble le plus au texte $a$, selon la distance et selon la similarité cosinus ? Expliquez la différence.

</li>

</ol>

:::loesung
(a) Avec $\lVert\mathbf{x}_a\rVert=\sqrt5$, $\lVert\mathbf{x}_b\rVert=3$, $\lVert\mathbf{x}_c\rVert=\sqrt{20}$ et $\lVert\mathbf{x}_d\rVert=\sqrt3$ :

<ul>

<li>

par rapport au texte $b$ : $\mathbf{x}_a^{\top}\mathbf{x}_b=0$, similarité cosinus $0$ ; distance $\sqrt{4+9+1}=\sqrt{14}\approx3{,}74$ ;

</li>

<li>

par rapport au texte $c$ : $\mathbf{x}_a^{\top}\mathbf{x}_c=8+0+2=10$, similarité cosinus $10/(\sqrt5\sqrt{20})=1$ ; distance $\sqrt{4+0+1}=\sqrt5\approx2{,}24$ ;

</li>

<li>

par rapport au texte $d$ : $\mathbf{x}_a^{\top}\mathbf{x}_d=3$, similarité cosinus $3/(\sqrt5\sqrt3)\approx0{,}775$ ; distance $\sqrt{1+1+0}=\sqrt2\approx1{,}41$.

</li>

</ul>

(b) Selon la distance, c’est le texte $d$ qui est le plus proche, selon la similarité cosinus le texte $c$. Pour le texte $c$, $\mathbf{x}_c=2\mathbf{x}_a$ : même répartition des mots, simplement deux fois plus long, donc, sur le fond, le même sujet. La distance pénalise la plus grande longueur, la similarité cosinus ne voit que la direction. Le texte $d$ est court et se trouve donc près de tout texte court, même sans sujet commun. Pour comparer des contenus, la similarité cosinus est ici la mesure appropriée, et le texte $b$ n’a absolument rien en commun avec le texte $a$.
:::
:::

:::aufgabe Exercice 14 ★★★ Distance et angle de vecteurs normés
<span class="anker" id="aufg-14"></span>

<ol class="al">

<li>

Montrez que, pour des vecteurs normés $\mathbf{u},\mathbf{v}$ formant l’angle $\varphi$, on a $\lVert\mathbf{u}-\mathbf{v}\rVert^2=2-2\cos\varphi$. Qu’en découle-t-il pour les classements « semblable selon la distance » et « semblable selon la similarité cosinus », si l’on norme au préalable tous les exemples ?

</li>

<li>

Vérifiez la formule sur les textes normés $\mathbf{x}_1$ et $\mathbf{x}_3$ de la sous-section [5.4](#stufe-5-4).

</li>

<li>

Montrez que $\lVert\mathbf{u}+\mathbf{v}\rVert=\lVert\mathbf{u}\rVert+\lVert\mathbf{v}\rVert$ si et seulement si $\mathbf{u}^{\top}\mathbf{v}=\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert$. Quand est-ce le cas ?

</li>

</ol>

:::loesung
(a) D’après [(4.1)](abstande-und-einheiten.html#gl-4-1), on a $\lVert\mathbf{u}-\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2+\lVert\mathbf{v}\rVert^2-2\,\mathbf{u}^{\top}\mathbf{v}=1+1-2\cos\varphi$, car $\mathbf{u}^{\top}\mathbf{v}=\cos\varphi$ pour des vecteurs normés. La distance est donc une fonction décroissante de la similarité cosinus : plus le cosinus est grand, plus la distance est petite. Si l’on norme au préalable tous les exemples, la distance et la similarité cosinus classent donc les exemples exactement de la même façon.

(b) Les textes normés sont $\mathbf{x}_1/\sqrt{13}$ et $\mathbf{x}_3/\sqrt{10}$, de cosinus $0{,}1754$. La formule donne $2-2\cdot0{,}1754\approx1{,}649$. Directement : $\mathbf{x}_1/\sqrt{13}-\mathbf{x}_3/\sqrt{10}\approx(0{,}832;\ 0{,}238;\ -0{,}949)^{\top}$, dont le carré de la longueur vaut $0{,}692+0{,}057+0{,}900\approx1{,}649$.

(c) Les deux membres sont positifs ou nuls ; on peut donc comparer leurs carrés. On a $\lVert\mathbf{u}+\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2+2\,\mathbf{u}^{\top}\mathbf{v}+\lVert\mathbf{v}\rVert^2$ et $(\lVert\mathbf{u}\rVert+\lVert\mathbf{v}\rVert)^2=\lVert\mathbf{u}\rVert^2+2\,\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert+\lVert\mathbf{v}\rVert^2$. Les deux sont égaux si et seulement si $\mathbf{u}^{\top}\mathbf{v}=\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert$. D’après l’inégalité de Cauchy-Schwarz et son cas d’égalité, c’est le cas si et seulement si l’un des vecteurs est un multiple de l’autre, et ce avec un facteur $\ge0$, car sinon le produit scalaire serait négatif. Intuitivement : l’inégalité triangulaire ne devient une égalité que si le triangle est aplati et que les deux flèches pointent dans la même direction.
:::
:::

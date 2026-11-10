---
title: Dérivée directionnelle et plus forte montée
pfad: Informatique / Apprentissage automatique / Fondements mathématiques / Dérivée, gradient et règle de dérivation en chaîne
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Chapitre 3 : Dérivée, gradient et règle de dérivation en chaîne
nachschlagen: ja
order: 15230500
summary: Les dérivées partielles indiquent comment la fonction réagit lorsqu’on modifie une seule entrée.
tags: dérivée directionnelle
lang: fr
---

<span class="anker" id="stufe-4"></span>

:::zweck
Les dérivées partielles indiquent comment la fonction réagit lorsqu’on modifie une seule entrée. Si l’on déplace toutes les entrées à la fois dans une direction, la dérivée directionnelle mesure la pente. À l’aide de celle-ci, cette section montre que le gradient pointe dans la direction de la plus forte montée et qu’il est perpendiculaire aux lignes de niveau. Un exemple montre que le chemin de plus forte descente ne mène pourtant pas nécessairement au point le plus bas.
:::

### La dérivée directionnelle

<span class="anker" id="stufe-4-1"></span>

Sur le terrain, on va rarement exactement vers le nord ou exactement vers l’est. Qui se trouve au point $\mathbf{x}$ et part dans une direction quelconque ressent une pente qui dépend de la direction. On décrit une direction par un vecteur $\mathbf{u}$ de longueur $1$. La longueur doit être fixée : qui fait des pas deux fois plus grands monte deux fois plus à chaque pas, sans que le terrain soit plus raide.

:::definition Définition 4.1 (Dérivée directionnelle)
<span class="anker" id="satz-4-1"></span>

Pour un vecteur $\mathbf{u}$ tel que $\lVert\mathbf{u}\rVert=1$, on appelle

<span class="anker" id="gl-4-1"></span>
$$D_{\mathbf{u}}f(\mathbf{x})=\lim_{t\to0}\frac{f(\mathbf{x}+t\,\mathbf{u})-f(\mathbf{x})}{t} \tag{4.1}$$

la __dérivée directionnelle__ de $f$ au point $\mathbf{x}$ dans la direction $\mathbf{u}$, pour autant que la limite existe.
:::

Pour $\mathbf{u}=\mathbf{e}_j$, c’est la dérivée partielle par rapport à $x_j$. Dans l’image du paysage, on coupe le terrain le long de la droite passant par $\mathbf{x}$ de direction $\mathbf{u}$, et la dérivée directionnelle est la pente de cette courbe de coupe. Il n’est cependant pas nécessaire de la recalculer pour chaque direction.

:::satz Théorème 4.2 (Dérivée directionnelle et gradient)
<span class="anker" id="satz-4-2"></span>

Si $f$ est différentiable au point $\mathbf{x}$, on a pour tout vecteur $\mathbf{u}$ de longueur $1$

<span class="anker" id="gl-4-2"></span>
$$D_{\mathbf{u}}f(\mathbf{x})=\nabla f(\mathbf{x})^{\top}\mathbf{u} . \tag{4.2}$$
:::

:::beweis Dérivée directionnelle et gradient
On pose dans [(3.5)](partielle-ableitungen-und-der-gradient.html#gl-3-5) en particulier $\mathbf{h}=t\,\mathbf{u}$ avec $t\ne0$ ; alors $\lVert\mathbf{h}\rVert=|t|$. Le quotient $\frac{f(\mathbf{x}+t\mathbf{u})-f(\mathbf{x})-t\,\nabla f(\mathbf{x})^{\top}\mathbf{u}}{|t|}$ tend vers $0$, donc $\frac{f(\mathbf{x}+t\mathbf{u})-f(\mathbf{x})}{t}-\nabla f(\mathbf{x})^{\top}\mathbf{u}$ aussi.
:::

::::beispiel [Exemple de calcul]
Pour $f(\mathbf{x})=x_1^2x_2+x_2^2$ au point $(1,\,2)$, avec $\nabla f=(4,\,5)^{\top}$ et la direction $\mathbf{u}=(0{,}6;\ 0{,}8)^{\top}$, de longueur $\sqrt{0{,}36+0{,}64}=1$, on a

$$D_{\mathbf{u}}f(1,2)=4\cdot0{,}6+5\cdot0{,}8=2{,}4+4{,}0=6{,}4$$

(Fig. [8](#abb-8)). Dans la direction opposée $-\mathbf{u}$, la pente vaut $-6{,}4$, et dans la direction $(0{,}8;\ -0{,}6)^{\top}$, perpendiculaire à $\mathbf{u}$, elle vaut $3{,}2-3{,}0=0{,}2$.

:::abbildung ml/k3rrichtung 8
La dérivée directionnelle comme produit scalaire du gradient et de la direction, pour $f(\mathbf{x})=x_1^2x_2+x_2^2$ au point $\mathbf{x}=(1,\,2)^{\top}$.
:::
::::

⁠**En bref :** La pente dans la direction d’un vecteur unitaire $\mathbf{u}$ est le produit scalaire $\nabla f(\mathbf{x})^{\top}\mathbf{u}$.

### La direction de plus forte montée

<span class="anker" id="stufe-4-2"></span>

Dans quelle direction faut-il aller pour que la montée soit la plus raide ? D’après [(4.2)](#gl-4-2), on cherche le vecteur unitaire $\mathbf{u}$ pour lequel le produit scalaire $\nabla f(\mathbf{x})^{\top}\mathbf{u}$ est le plus grand. Le [chapitre 1](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/vektoren-und-matrizen.html) a fourni l’outil pour cela : l’inégalité de Cauchy-Schwarz.

:::satz Théorème 4.3 (Plus forte montée)
<span class="anker" id="satz-4-3"></span>

Soit $f$ différentiable au point $\mathbf{x}$ et $\nabla f(\mathbf{x})\ne\mathbf{0}$. Alors, pour tout vecteur $\mathbf{u}$ de longueur $1$,

<span class="anker" id="gl-4-3"></span>
$$-\lVert\nabla f(\mathbf{x})\rVert\le D_{\mathbf{u}}f(\mathbf{x})\le\lVert\nabla f(\mathbf{x})\rVert . \tag{4.3}$$

La borne supérieure n’est atteinte que pour $\mathbf{u}=\nabla f(\mathbf{x})/\lVert\nabla f(\mathbf{x})\rVert$, la borne inférieure que pour $\mathbf{u}=-\nabla f(\mathbf{x})/\lVert\nabla f(\mathbf{x})\rVert$. Le gradient pointe donc dans la direction de la plus forte montée, et sa longueur est la pente dans cette direction ; l’opposé du gradient pointe dans la direction de la plus forte descente.
:::

:::beweis Plus forte montée
D’après l’inégalité de Cauchy-Schwarz du [chapitre 1, section 5.1](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/winkel-und-ahnlichkeit.html#stufe-5-1), on a $|\nabla f(\mathbf{x})^{\top}\mathbf{u}|\le\lVert\nabla f(\mathbf{x})\rVert\,\lVert\mathbf{u}\rVert=\lVert\nabla f(\mathbf{x})\rVert$, et l’égalité a lieu si et seulement si $\mathbf{u}$ est un multiple de $\nabla f(\mathbf{x})$. Les multiples de longueur $1$ sont $\pm\nabla f(\mathbf{x})/\lVert\nabla f(\mathbf{x})\rVert$. En les substituant, on obtient $\pm\nabla f(\mathbf{x})^{\top}\nabla f(\mathbf{x})/\lVert\nabla f(\mathbf{x})\rVert=\pm\lVert\nabla f(\mathbf{x})\rVert$.
:::

Avec l’angle $\varphi$ entre $\nabla f(\mathbf{x})$ et $\mathbf{u}$ du [chapitre 1, section 5.2](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/winkel-und-ahnlichkeit.html#stufe-5-2), on a $D_{\mathbf{u}}f(\mathbf{x})=\lVert\nabla f(\mathbf{x})\rVert\cos\varphi$. Si l’on va dans la direction du gradient, $\varphi=0$ et $\cos\varphi=1$. Si l’on s’en écarte de $90^\circ$, la pente est nulle. Si l’on va en sens contraire, elle est la plus fortement négative. D’après le [chapitre 1, section 5.5](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/winkel-und-ahnlichkeit.html#stufe-5-5), $\nabla f(\mathbf{x})^{\top}\mathbf{u}$ est la longueur de l’ombre du gradient sur la droite de direction $\mathbf{u}$, et une ombre est la plus longue lorsque la droite pointe dans la direction de la flèche elle-même.

Le théorème repose sur trois hypothèses. Premièrement, il faut $\nabla f(\mathbf{x})\ne\mathbf{0}$ ; si le gradient est nul, la pente est nulle dans toutes les directions d’après [(4.2)](#gl-4-2), et aucune direction n’est plus raide qu’une autre. Deuxièmement, $f$ doit être différentiable, sinon [(4.2)](#gl-4-2) ne vaut pas. Troisièmement, le théorème compare des directions de même longueur euclidienne ; si l’on mesure les pas autrement, la direction de plus grande pente change (encadré « Contexte » ci-dessous).

::::beispiel [Exemple de calcul]
Pour $f(\mathbf{x})=x_1^2x_2+x_2^2$ au point $(1,\,2)$, on a $\lVert\nabla f\rVert=\sqrt{16+25}=\sqrt{41}\approx6{,}403$, et la direction de plus grande pente est $(4,\,5)^{\top}/\sqrt{41}\approx(0{,}625;\ 0{,}781)^{\top}$. Aucune direction n’a une pente plus grande. La direction $\mathbf{u}=(0{,}6;\ 0{,}8)^{\top}$ de la sous-section précédente ne s’en écarte que d’environ $1{,}8^\circ$ ; c’est pourquoi sa pente $6{,}4$ était déjà presque maximale. Dans la direction $(5,\,-4)^{\top}/\sqrt{41}$, perpendiculaire au gradient, la pente vaut $(20-20)/\sqrt{41}=0$.
::::

⁠**En bref :** Le gradient pointe dans la direction de la plus forte montée, et sa longueur est la pente dans cette direction ; à l’opposé du gradient, la descente est la plus raide.

:::hintergrund La direction de plus grande pente dépend de la façon dont on mesure les pas
Le théorème compare toutes les directions $\mathbf{u}$ telles que $\lVert\mathbf{u}\rVert=1$ dans la norme euclidienne. Le [chapitre 1, section 3](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/normen-die-groe-eines-vektors.html#stufe-3), présentait d’autres normes. Si l’on autorise tous les pas tels que $\lVert\mathbf{u}\rVert_\infty\le1$, si chaque composante peut donc prendre une valeur entre $-1$ et $1$, alors $\nabla f^{\top}\mathbf{u}=\sum_j\partial_jf\cdot u_j$ est maximal lorsque chaque composante $u_j$ vaut $+1$ ou $-1$ avec le signe de $\partial_jf$. La direction de plus grande pente est alors $\operatorname{sign}(\nabla f)$, composante par composante, et la pente vaut $\sum_j|\partial_jf|=\lVert\nabla f\rVert_1$. Si l’on autorise en revanche tous les pas tels que $\lVert\mathbf{u}\rVert_1\le1$, on met tout le budget dans la composante de plus grand $|\partial_jf|$ : la direction de plus grande pente est un axe de coordonnées, et la pente vaut $\lVert\nabla f\rVert_\infty$. Pour $\nabla f=(4,\,5)^{\top}$, cela donne les directions $(1,\,1)^{\top}$ de pente $9$ et $(0,\,1)^{\top}$ de pente $5$. « Le gradient est la direction de plus grande pente » est donc un énoncé qui porte sur la longueur euclidienne. Il dépend aussi des unités des variables : si l’on mesure $x_1$ dans d’autres unités, les longueurs des pas changent, et avec elles la direction de plus grande pente, exactement comme les distances dans le [chapitre 1, section 4.2](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/abstande-und-einheiten.html#stufe-4-2).
:::

### Le gradient est perpendiculaire aux lignes de niveau

<span class="anker" id="stufe-4-3"></span>

Qui marche le long d’une ligne de niveau ne monte ni ne descend. Dans la direction de la ligne de niveau, la pente est donc nulle, et d’après la sous-section précédente, la pente est nulle exactement dans les directions perpendiculaires au gradient. Le gradient est donc perpendiculaire à la ligne de niveau. Plus précisément :

:::satz Théorème 4.4 (Gradient et ligne de niveau)
<span class="anker" id="satz-4-4"></span>

Soit $f$ différentiable au point $\mathbf{x}$, $\nabla f(\mathbf{x})\ne\mathbf{0}$ et $c=f(\mathbf{x})$. L’ensemble de niveau de l’approximation linéaire passant par $\mathbf{x}$, c’est-à-dire l’ensemble des points $\mathbf{x}+\mathbf{h}$ tels que $\nabla f(\mathbf{x})^{\top}\mathbf{h}=0$, est, pour deux variables, la droite passant par $\mathbf{x}$ perpendiculaire au gradient. C’est la tangente à la ligne de niveau de $f$ pour la valeur $c$.
:::

Que la droite touche la ligne de niveau découle de la loupe : au voisinage de $\mathbf{x}$, $f$ et son approximation linéaire ne diffèrent que d’une erreur qui disparaît plus vite que $\lVert\mathbf{h}\rVert$, si bien que leurs lignes de niveau pour la valeur $c$ diffèrent elles aussi si peu qu’elles ont la même direction en $\mathbf{x}$. L’exercice [22](die-kettenregel-fur-mehrere-variablen.html#aufg-22) fournit une preuve à l’aide de la règle de dérivation en chaîne. Pour plus de deux variables, il en va de même pour l’ensemble de niveau, qui est alors une surface : le gradient lui est perpendiculaire.

::::beispiel [Exemple de calcul]
Pour la cuvette $f(\mathbf{x})=x_1^2+4x_2^2$, on a $\nabla f(\mathbf{x})=(2x_1,\,8x_2)^{\top}$, soit $(2,\,8)^{\top}$ au point $(1,\,1)$. La ligne de niveau passant par ce point est l’ellipse $x_1^2+4x_2^2=5$. La direction $\mathbf{t}=(4,\,-1)^{\top}$ est perpendiculaire au gradient, car $2\cdot4+8\cdot(-1)=0$. Si l’on part de $(1,\,1)$ et que l’on avance de $s$ dans cette direction, on a

$$f(1+4s,\ 1-s)=(1+4s)^2+4\,(1-s)^2=5+20s^2 .$$

La valeur ne change que de $20s^2$, quantité qui disparaît donc plus vite que $s$ : la droite touche la ligne de niveau et en est la tangente. La Fig. [9](#abb-9) montre les gradients en de nombreux points ; chacun est perpendiculaire à la ligne de niveau passant par son point de départ.

:::abbildung ml/k3hoehen 9
Gradients (rouge, dessinés raccourcis) sur des lignes de niveau (gris). (a) Pour la cuvette ronde, tous les gradients pointent exactement dans la direction opposée au centre. (b) Pour la cuvette allongée, ils sont eux aussi perpendiculaires aux lignes de niveau, mais ne pointent exactement dans la direction opposée au centre que sur les axes. Au point $(1,\,1)$ (noir), la direction de la plus forte descente est tracée en bleu. En (a), elle pointe vers le point le plus bas ; en (b), elle s’écarte d’environ $31^\circ$ de la direction du point le plus bas (en tirets).
:::
::::

⁠**En bref :** Le long d’une ligne de niveau, $f$ ne change pas ; c’est pourquoi le gradient lui est perpendiculaire.

### Plus forte descente et point le plus bas

<span class="anker" id="stufe-4-4"></span>

Pour une cuvette ronde, il va de soi que le chemin de plus forte descente mène au centre. Pour une cuvette allongée, c’est faux, et cette différence est importante, car on attend facilement du gradient plus qu’il ne sait.

Pour $f(\mathbf{x})=x_1^2+x_2^2$, on a $\nabla f(\mathbf{x})=2\mathbf{x}$. L’opposé du gradient, $-2\mathbf{x}$, pointe donc de chaque point exactement vers l’origine, le point le plus bas de la cuvette. Pour $f(\mathbf{x})=x_1^2+4x_2^2$, on a $-\nabla f(\mathbf{x})=(-2x_1,\,-8x_2)^{\top}$, et ce n’est un multiple de $-\mathbf{x}$ que si $x_1=0$ ou $x_2=0$, donc sur les axes. Partout ailleurs, la plus forte descente passe à côté du point le plus bas.

La raison tient à la forme des lignes de niveau. Le gradient ne sait que la façon dont le terrain est incliné en son point de départ ; il est perpendiculaire à la ligne de niveau en ce point. Pour des lignes de niveau allongées, la perpendiculaire est oblique par rapport à la direction du centre. Dans l’exemple, $f$ croît quatre fois plus vite dans la direction $x_2$ que dans la direction $x_1$ ; les parois de la cuvette sont plus raides dans la direction $x_2$, et la plus forte descente mène surtout en travers de celles-ci.

::::beispiel [Exemple de calcul]
Au point $(1,\,1)$, on a $-\nabla f=(-2,\,-8)^{\top}$, de longueur $\sqrt{68}\approx8{,}246$ ; la direction de la plus forte descente est donc $(-0{,}243;\ -0{,}970)^{\top}$. La direction du point le plus bas est $(-1,\,-1)^{\top}/\sqrt2\approx(-0{,}707;\ -0{,}707)^{\top}$. L’angle entre les deux a pour cosinus

$$\frac{(-2)\cdot(-1)+(-8)\cdot(-1)}{\sqrt{68}\cdot\sqrt2}=\frac{10}{\sqrt{136}}\approx0{,}857,$$

il vaut donc environ $31^\circ$. Dans la direction du point le plus bas, la pente n’est, d’après [(4.2)](#gl-4-2), que de $-10/\sqrt2\approx-7{,}07$, alors qu’elle vaut $-8{,}246$ dans la plus forte descente.
::::

⁠**En bref :** L’opposé du gradient indique la plus forte descente, mais il ne pointe vers le point le plus bas que pour des lignes de niveau rondes ; pour des lignes de niveau allongées, il passe à côté.

:::aufgabe Exercice 13 ★ Pentes dans de nombreuses directions
<span class="anker" id="aufg-13"></span>

Soit $f(\mathbf{x})=x_1^2+4x_2^2$ et $\mathbf{x}=(1,\,1)^{\top}$.

<ol class="al">

<li>

Calculez les dérivées directionnelles dans les directions $\mathbf{e}_1$, $\mathbf{e}_2$, $(1,\,1)^{\top}/\sqrt2$ et $(-1,\,1)^{\top}/\sqrt2$.

</li>

<li>

Comparez avec $\lVert\nabla f(\mathbf{x})\rVert$. Laquelle des quatre directions est la plus proche de la direction de plus grande pente ?

</li>

</ol>

:::loesung
(a) On a $\nabla f(1,1)=(2,\,8)^{\top}$. D’après [(4.2)](#gl-4-2) :

$$D_{\mathbf{e}_1}f=2,\qquad D_{\mathbf{e}_2}f=8,\qquad D_{(1,1)/\sqrt2}f=\frac{2+8}{\sqrt2}\approx7{,}071,\qquad D_{(-1,1)/\sqrt2}f=\frac{-2+8}{\sqrt2}\approx4{,}243 .$$

(b) $\lVert\nabla f\rVert=\sqrt{68}\approx8{,}246$ ; aucune des pentes n’est plus grande, comme l’exige [(4.3)](#gl-4-3). C’est $\mathbf{e}_2$, avec $8$, qui est la plus proche de la direction de plus grande pente. L’angle entre $\mathbf{e}_2$ et $\nabla f$ a pour cosinus $8/\sqrt{68}\approx0{,}970$, soit environ $14^\circ$ ; pour $(1,\,1)^{\top}/\sqrt2$, il est d’environ $31^\circ$.
:::
:::

:::aufgabe Exercice 14 ★★ Une hyperbole comme ligne de niveau
<span class="anker" id="aufg-14"></span>

Soit $f(\mathbf{x})=x_1x_2$ et $\mathbf{x}=(2,\,1)^{\top}$.

<ol class="al">

<li>

Calculez $\nabla f(\mathbf{x})$, la direction de plus grande pente et la pente dans cette direction.

</li>

<li>

La ligne de niveau passant par $\mathbf{x}$ est $x_2=2/x_1$. Calculez la pente de cette courbe en $x_1=2$, écrivez sa direction tangente sous forme de vecteur et vérifiez que celui-ci est perpendiculaire à $\nabla f(\mathbf{x})$.

</li>

</ol>

:::loesung
(a) $\nabla f(\mathbf{x})=(x_2,\,x_1)^{\top}$, donc $(1,\,2)^{\top}$ au point $(2,\,1)$. La direction de plus grande pente est $(1,\,2)^{\top}/\sqrt5\approx(0{,}447;\ 0{,}894)^{\top}$, la pente dans cette direction $\sqrt5\approx2{,}236$.

(b) La ligne de niveau $x_2=2/x_1$ a pour pente $-2/x_1^2$, soit $-\tfrac12$ en $x_1=2$. Une direction tangente est $(1,\,-\tfrac12)^{\top}$ ou, après multiplication par $2$, $(2,\,-1)^{\top}$. On a $(1,\,2)(2,\,-1)^{\top}=2-2=0$ : le gradient est perpendiculaire à la ligne de niveau.
:::
:::

:::aufgabe Exercice 15 ★★ Fonctions linéaires
<span class="anker" id="aufg-15"></span>

Soit $f(\mathbf{x})=\mathbf{a}^{\top}\mathbf{x}+b$ avec $\mathbf{a}\in\mathbb{R}^d$ fixé, $\mathbf{a}\ne\mathbf{0}$, et un nombre $b$.

<ol class="al">

<li>

Montrez que $\nabla f(\mathbf{x})=\mathbf{a}$ en tout point. Que sont les lignes de niveau pour $d=2$ ?

</li>

<li>

Pour les appartements du [chapitre 1](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/vektoren-und-matrizen.html), on a $\hat y=\mathbf{w}^{\top}\mathbf{x}+b$ avec $\mathbf{w}=(3,\,10,\,-4)^{\top}$, où $x_1$ est la surface en $\mathrm m^2$, $x_2$ le nombre de pièces et $x_3$ la distance au centre en km. Quelle variation $\mathbf{u}$ des caractéristiques telle que $\lVert\mathbf{u}\rVert=1$ augmente le plus la prédiction, et de combien ?

</li>

<li>

Si l’on indique la surface en $10\,\mathrm m^2$, le poids passe de $w_1=3$ à $30$. Quelle est maintenant la direction de plus grande pente ? Qu’en apprend-on sur le théorème de la plus forte montée ?

</li>

</ol>

:::loesung
(a) $\partial_k(\mathbf{a}^{\top}\mathbf{x}+b)=a_k$, donc $\nabla f=\mathbf{a}$ partout. Pour $d=2$, les lignes de niveau sont les droites $a_1x_1+a_2x_2+b=c$ ; elles sont parallèles entre elles et perpendiculaires à $\mathbf{a}$.

(b) Le gradient par rapport à $\mathbf{x}$ est $\mathbf{w}=(3,\,10,\,-4)^{\top}$, avec $\lVert\mathbf{w}\rVert=\sqrt{9+100+16}=\sqrt{125}\approx11{,}18$. La variation de longueur $1$ la plus raide est $\mathbf{u}=\mathbf{w}/\sqrt{125}\approx(0{,}268;\ 0{,}894;\ -0{,}358)^{\top}$, et elle augmente la prédiction d’environ $11{,}18$ milliers d’euros : un peu plus de surface, nettement plus de pièces et un peu plus près du centre.

(c) Dans les nouvelles unités, on a $\mathbf{w}'=(30,\,10,\,-4)^{\top}$, avec $\lVert\mathbf{w}'\rVert=\sqrt{1016}\approx31{,}87$, et la direction de plus grande pente est $\mathbf{w}'/\lVert\mathbf{w}'\rVert\approx(0{,}941;\ 0{,}314;\ -0{,}125)^{\top}$ : elle porte maintenant presque entièrement sur la surface. Le même appartement, les mêmes prix, mais une autre direction de plus grande pente. Le théorème de la plus forte montée compare des pas de même longueur euclidienne dans les coordonnées choisies, et ce que signifie « longueur $1$ » dépend des unités, exactement comme les distances dans le [chapitre 1, section 4.2](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/abstande-und-einheiten.html#stufe-4-2). Pour des caractéristiques exprimées dans des unités différentes, la direction de plus grande pente n’a de sens qu’après la standardisation du [chapitre 1, section 4.5](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/abstande-und-einheiten.html#stufe-4-5).
:::
:::

:::aufgabe Exercice 16 ★★★ Quand la plus forte descente pointe-t-elle vers le centre ?
<span class="anker" id="aufg-16"></span>

Soit $f(\mathbf{x})=a\,x_1^2+b\,x_2^2$ avec des nombres $a,b>0$.

<ol class="al">

<li>

Montrez que $-\nabla f(\mathbf{x})$ est un multiple positif de $-\mathbf{x}$ si et seulement si $a=b$ ou si $\mathbf{x}$ se trouve sur l’un des axes ($\mathbf{x}\ne\mathbf{0}$).

</li>

<li>

Pour $a=1$, $b=4$, calculez aux points $(1,\,1)$, $(2,\,1)$ et $(4,\,1)$ l’angle entre $-\nabla f$ et $-\mathbf{x}$. Comment évolue-t-il lorsqu’on s’éloigne vers l’extérieur sur la droite $x_2=1$ ?

</li>

</ol>

:::loesung
(a) On a $-\nabla f(\mathbf{x})=(-2ax_1,\,-2bx_2)^{\top}$. Ce vecteur est égal à $c\,(-x_1,\,-x_2)^{\top}$ avec un $c>0$ si et seulement si $2ax_1=c\,x_1$ et $2bx_2=c\,x_2$. Si les deux coordonnées sont non nulles, il s’ensuit que $2a=c=2b$, donc $a=b$. Si $x_1=0$, $c=2b$ suffit ; si $x_2=0$, $c=2a$ suffit. Pour une cuvette ronde, la plus forte descente pointe donc partout vers l’origine, pour une cuvette allongée seulement sur les axes.

(b) Pour $a=1$, $b=4$, on a $-\nabla f=(-2x_1,\,-8x_2)^{\top}$ :

$$\begin{aligned} (1,\,1)&:\ \cos\varphi=\frac{2+8}{\sqrt{68}\,\sqrt2}\approx0{,}857,\ \varphi\approx31{,}0^\circ;\\ (2,\,1)&:\ \cos\varphi=\frac{8+8}{\sqrt{80}\,\sqrt5}=0{,}8,\ \varphi\approx36{,}9^\circ;\\ (4,\,1)&:\ \cos\varphi=\frac{32+8}{\sqrt{128}\,\sqrt{17}}\approx0{,}857,\ \varphi\approx31{,}0^\circ . \end{aligned}$$

Sur la droite $x_2=1$, l’angle, qui vaut $0^\circ$ en $x_1=0$, commence par augmenter, puis diminue de nouveau ; loin vers l’extérieur, le point se trouve presque dans la direction de l’axe des $x_1$, et la plus forte descente y pointe de nouveau presque vers le centre.
:::
:::

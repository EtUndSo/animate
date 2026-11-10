---
title: Dérivées partielles et gradient
pfad: Informatique / Apprentissage automatique / Fondements mathématiques / Dérivée, gradient et règle de dérivation en chaîne
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Chapitre 3 : Dérivée, gradient et règle de dérivation en chaîne
nachschlagen: ja
order: 15230400
summary: Lorsqu’un nombre dépend de nombreuses entrées, on peut modifier un peu chaque entrée séparément en fixant les autres.
tags: fonction de d variables, ensemble de niveau, ligne de niveau, courbe de coupe, dérivée partielle, gradient, plan tangent, différentiable
lang: fr
---

<span class="anker" id="stufe-3"></span>

:::zweck
Lorsqu’un nombre dépend de nombreuses entrées, on peut modifier un peu chaque entrée séparément en fixant les autres. Les pentes que l’on trouve ainsi s’appellent dérivées partielles. Ensemble, elles forment un vecteur, le gradient, et avec lui l’approximation linéaire de la section [1](die-ableitung.html#stufe-1) devient une approximation par un plan. La section se termine en précisant quand cette approximation est vraiment valable.
:::

### Fonctions de plusieurs variables

<span class="anker" id="stufe-3-1"></span>

Dans le [chapitre 1, section 2.2](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-skalarprodukt.html#stufe-2-2), la prédiction pour un appartement était la somme pondérée $\hat y=\mathbf{w}^{\top}\mathbf{x}$ des caractéristiques. Si l’on fixe les caractéristiques et que l’on se demande comment la prédiction dépend des poids, $\hat y$ est un nombre qui dépend des $d$ nombres $w_1,\dots,w_d$. De même, la forme quadratique $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}$ du [chapitre 2, section 5.1](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/quadratische-formen.html#stufe-5-1), dépend de toutes les composantes de $\mathbf{x}$. Pour de telles correspondances, il faut une notion propre.

:::definition Définition 3.1 (Fonction de plusieurs variables, ligne de niveau)
<span class="anker" id="satz-3-1"></span>

Une fonction $f:\mathbb{R}^d\to\mathbb{R}$ associe à chaque vecteur $\mathbf{x}\in\mathbb{R}^d$ un nombre $f(\mathbf{x})=f(x_1,\dots,x_d)$ ; on l’appelle __fonction de $d$ variables__. Pour un nombre $c$, l’ensemble de tous les $\mathbf{x}$ tels que $f(\mathbf{x})=c$ s’appelle l’__ensemble de niveau__ de $f$ pour la valeur $c$. Pour $d=2$, c’est en général une courbe, que l’on appelle alors __ligne de niveau__.
:::

Pour deux variables, l’image d’un paysage aide. Le vecteur $\mathbf{x}=(x_1,\,x_2)^{\top}$ est un lieu sur une carte, $f(\mathbf{x})$ l’altitude du terrain au-dessus de ce lieu. Le graphe de $f$, l’ensemble des points $(x_1,\,x_2,\,f(x_1,x_2))$ de l’espace, est la surface du terrain. Les lignes de niveau relient, comme sur une carte de randonnée, tous les lieux de même altitude. Là où elles sont serrées, le terrain est raide ; là où elles sont espacées, il est plat. Au-delà de deux variables, l’image fait défaut, mais les calculs restent les mêmes.

::::beispiel [Exemple de calcul]
Tout au long des sections [3](#stufe-3) à [8](die-hesse-matrix-und-die-quadratische-naherung.html#stufe-8), nous utiliserons la fonction

<span class="anker" id="gl-3-1"></span>
$$f(\mathbf{x})=x_1^2\,x_2+x_2^2 . \tag{3.1}$$

Au point $\mathbf{x}=(1,\,2)^{\top}$, on a $f(1,2)=1\cdot2+4=6$. La ligne de niveau $f=6$ comprend tous les points tels que $x_1^2x_2+x_2^2=6$. Pour $x_1=0$, cela donne $x_2^2=6$, donc le point $(0;\ \sqrt6)^{\top}\approx(0;\ 2{,}449)^{\top}$ s’y trouve. De manière générale, pour tout $x_1$ fixé, l’équation est du second degré en $x_2$, et sa solution positive $x_2=\tfrac12\bigl(\sqrt{x_1^4+24}-x_1^2\bigr)$ décrit toute la ligne de niveau au-dessus de l’axe des $x_1$ ; pour $x_1=1$, elle donne $\tfrac12(5-1)=2$. La Fig. [6](#abb-6) montre quelques lignes de niveau.
::::

⁠**En bref :** Une fonction de $d$ variables associe un nombre à chaque vecteur ; avec deux variables, on se la représente comme un paysage dont les lignes de niveau relient les lieux de même altitude.

### Dérivées partielles

<span class="anker" id="stufe-3-2"></span>

Avec quelle force $f$ réagit-elle si l’on ne modifie qu’une seule entrée ? On fixe toutes les autres, et $f$ devient une fonction ordinaire d’une variable. Dans l’image du paysage, on coupe le terrain le long d’une droite parallèle à un axe. La surface de coupe présente comme bord une courbe, la __courbe de coupe__, et sa pente est la sensibilité cherchée.

:::definition Définition 3.2 (Dérivée partielle)
<span class="anker" id="satz-3-2"></span>

La __dérivée partielle__ de $f:\mathbb{R}^d\to\mathbb{R}$ par rapport à $x_j$ au point $\mathbf{x}$ est

<span class="anker" id="gl-3-2"></span>
$$\frac{\partial f}{\partial x_j}(\mathbf{x})=\lim_{h\to0}\frac{f(\mathbf{x}+h\,\mathbf{e}_j)-f(\mathbf{x})}{h}, \tag{3.2}$$

pour autant que la limite existe. Ici, $\mathbf{e}_j$ est le $j$-ième vecteur unitaire du [chapitre 1, section 1.6](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/vektoren-daten-als-zahlenlisten.html#stufe-1-6). On écrit aussi en abrégé $\partial_jf(\mathbf{x})$.
:::

Le vecteur $\mathbf{x}+h\,\mathbf{e}_j$ ne diffère de $\mathbf{x}$ que par sa $j$-ième composante, et ce de $h$. La définition est donc la dérivée ordinaire de la section [1.2](die-ableitung.html#stufe-1-2), appliquée à la fonction que l’on obtient en fixant toutes les variables sauf $x_j$. Il en découle la règle de calcul : on dérive par rapport à $x_j$ et on traite toutes les autres variables comme des constantes. Le symbole $\partial$ est un d rond et rappelle que seule une partie des variables bouge.

::::beispiel [Exemple de calcul]
Pour $f(\mathbf{x})=x_1^2x_2+x_2^2$, on traite $x_2$ comme une constante en dérivant par rapport à $x_1$, et inversement :

$$\frac{\partial f}{\partial x_1}=2x_1\,x_2,\qquad \frac{\partial f}{\partial x_2}=x_1^2+2x_2 .$$

Au point $(1,\,2)$, cela donne $4$ et $5$. Les courbes de coupe montrent la même chose (Fig. [6](#abb-6)) : si l’on fixe $x_2=2$, il reste $f(x_1,2)=2x_1^2+4$, de pente $4x_1=4$ en $x_1=1$. Si l’on fixe $x_1=1$, il reste $f(1,x_2)=x_2+x_2^2$, de pente $1+2x_2=5$ en $x_2=2$.

:::abbildung ml/k3schnitt 6
Les dérivées partielles comme pentes de courbes de coupe, pour $f(\mathbf{x})=x_1^2x_2+x_2^2$ au point $(1,\,2)$. (a) Lignes de niveau pour les valeurs $2$, $4$, $6$ (noir), $8$ et $10$, ainsi que les deux droites de coupe passant par $(1,\,2)$. (b) Le long de la droite bleue $x_2=2$, le terrain suit $2x_1^2+4$, de pente $4$ en $x_1=1$. (c) Le long de la droite rouge $x_1=1$, il suit $x_2+x_2^2$, de pente $5$ en $x_2=2$.
:::
::::

⁠**En bref :** La dérivée partielle $\partial f/\partial x_j$ est la pente dans la direction de l’axe des $x_j$ : on dérive par rapport à $x_j$ et on fixe toutes les autres variables.

### Le gradient

<span class="anker" id="stufe-3-3"></span>

Une fonction de $d$ variables a en chaque point $d$ dérivées partielles. On les réunit en un vecteur, afin de pouvoir calculer avec elles comme avec $\mathbf{x}$ lui-même.

:::definition Définition 3.3 (Gradient)
<span class="anker" id="satz-3-3"></span>

Si toutes les dérivées partielles de $f:\mathbb{R}^d\to\mathbb{R}$ existent au point $\mathbf{x}$, le vecteur colonne

<span class="anker" id="gl-3-3"></span>
$$\nabla f(\mathbf{x})=\begin{pmatrix}\partial_1f(\mathbf{x})\\ \vdots\\ \partial_df(\mathbf{x})\end{pmatrix}\in\mathbb{R}^d \tag{3.3}$$

s’appelle le __gradient__ de $f$ au point $\mathbf{x}$. Le symbole $\nabla$ se lit « nabla ».
:::

Le gradient a la même forme que $\mathbf{x}$ : un coefficient par variable, écrit en colonne. Cette convention vaut dans tout le chapitre ; la section [7](ableiten-nach-vektoren-und-matrizen.html#stufe-7) y revient, parce que tous les livres ne la choisissent pas. Si l’on associe à chaque point $\mathbf{x}$ son gradient, on obtient un champ de flèches, une en chaque lieu de la carte. La section [4](richtungsableitung-und-steilster-anstieg.html#stufe-4) précise dans quelle direction pointent ces flèches.

::::beispiel [Exemple de calcul]
Pour $f(\mathbf{x})=x_1^2x_2+x_2^2$, on a

$$\nabla f(\mathbf{x})=\begin{pmatrix}2x_1x_2\\ x_1^2+2x_2\end{pmatrix},\qquad \nabla f(1,2)=\begin{pmatrix}4\\5\end{pmatrix},\qquad \nabla f(0,1)=\begin{pmatrix}0\\2\end{pmatrix} .$$

Pour la somme de carrés $f(\mathbf{x})=x_1^2+x_2^2+x_3^2$, on a $\nabla f(\mathbf{x})=(2x_1,\,2x_2,\,2x_3)^{\top}=2\mathbf{x}$.
::::

⁠**En bref :** Le gradient est le vecteur colonne de toutes les dérivées partielles, de même forme que $\mathbf{x}$.

### L’approximation linéaire dans l’espace

<span class="anker" id="stufe-3-4"></span>

Pour une variable, la tangente remplace la fonction au voisinage d’un point. Avec deux variables, c’est un plan qui prend sa place. Sous la loupe, un terrain lisse ressemble, au voisinage d’un point, à une plaque inclinée : c’est le __plan tangent__. Un plan passant par le point $(\mathbf{x},\,f(\mathbf{x}))$ a la forme $f(\mathbf{x})+m_1h_1+m_2h_2$, où $\mathbf{h}=(h_1,\,h_2)^{\top}$ est le déplacement sur la carte et où $m_1$, $m_2$ sont les inclinaisons de la plaque dans la direction des deux axes. Pour qu’il épouse le terrain, ses inclinaisons le long des axes doivent coïncider avec les pentes des courbes de coupe, donc $m_j=\partial_jf(\mathbf{x})$.

On obtient ainsi l’approximation linéaire pour plusieurs variables :

<span class="anker" id="gl-3-4"></span>
$$f(\mathbf{x}+\mathbf{h})\approx f(\mathbf{x})+\nabla f(\mathbf{x})^{\top}\mathbf{h}=f(\mathbf{x})+\sum_{j=1}^d\partial_jf(\mathbf{x})\,h_j . \tag{3.4}$$

La formule dit quelque chose de remarquable : si l’on modifie plusieurs entrées à la fois de petites quantités, *leurs effets s’additionnent*. Chaque variable apporte $\partial_jf\cdot h_j$, comme si elle avait été modifiée seule. Pour de grandes variations, ce n’est plus vrai, car les variables influencent alors mutuellement leur effet, comme dans $x_1^2x_2$. Pour de petites variations, ces interactions sont des produits de petites grandeurs et disparaissent plus vite que les effets individuels, exactement comme le petit carré du coin dans la règle du produit.

::::beispiel [Exemple de calcul]
Pour $f(\mathbf{x})=x_1^2x_2+x_2^2$ au point $\mathbf{x}=(1,\,2)^{\top}$ et le déplacement $\mathbf{h}=(0{,}01;\ 0{,}02)^{\top}$, on a

$$f(\mathbf{x}+\mathbf{h})\approx f(\mathbf{x})+\nabla f(\mathbf{x})^{\top}\mathbf{h}=6+4\cdot0{,}01+5\cdot0{,}02=6+0{,}14=6{,}14 .$$

La valeur exacte est $f(1{,}01;\ 2{,}02)=1{,}0201\cdot2{,}02+2{,}02^2=2{,}060602+4{,}0804=6{,}141002$. L’erreur $0{,}001002$ est bien plus petite que la variation $0{,}14$ elle-même. La Fig. [7](#abb-7) montre le produit scalaire pas à pas.

:::abbildung ml/k3rlinear 7
La variation de l’approximation linéaire comme produit scalaire du gradient et du déplacement : chaque variable apporte sa dérivée partielle multipliée par sa propre variation.
:::
::::

⁠**En bref :** Près de $\mathbf{x}$, on a $f(\mathbf{x}+\mathbf{h})\approx f(\mathbf{x})+\nabla f(\mathbf{x})^{\top}\mathbf{h}$ : pour de petites variations, les effets des différentes variables s’additionnent.

### Différentiabilité

<span class="anker" id="stufe-3-5"></span>

Jusqu’ici, l’approximation [(3.4)](#gl-3-4) a seulement été rendue plausible. Pour une variable, elle découlait de l’existence de la dérivée. Avec plusieurs variables, l’existence des dérivées partielles ne suffit pas, comme le montre le contre-exemple ci-dessous. On exige donc l’approximation elle-même : son erreur doit disparaître plus vite que le déplacement, de même que dans [(1.4)](die-ableitung.html#gl-1-4) l’erreur $r(h)$ disparaissait plus vite que $h$. On ne peut pas diviser par un vecteur ; au lieu de diviser par $h$, on divise donc par la longueur $\lVert\mathbf{h}\rVert$ du [chapitre 1, section 3.1](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/normen-die-groe-eines-vektors.html#stufe-3-1).

:::definition Définition 3.4 (Différentiabilité)
<span class="anker" id="satz-3-4"></span>

Une fonction $f:\mathbb{R}^d\to\mathbb{R}$ est dite __différentiable__ au point $\mathbf{x}$ s’il existe un vecteur $\mathbf{g}\in\mathbb{R}^d$ tel que

<span class="anker" id="gl-3-5"></span>
$$\lim_{\mathbf{h}\to\mathbf{0}}\frac{f(\mathbf{x}+\mathbf{h})-f(\mathbf{x})-\mathbf{g}^{\top}\mathbf{h}}{\lVert\mathbf{h}\rVert}=0 . \tag{3.5}$$

La limite $\mathbf{h}\to\mathbf{0}$ signifie : le quotient est arbitrairement proche de $0$ dès que $\lVert\mathbf{h}\rVert$ est assez petit et que $\mathbf{h}\ne\mathbf{0}$, quelle que soit la direction d’où $\mathbf{h}$ s’approche.
:::

:::satz Théorème 3.5 (Différentiable signifie : gradient et approximation linéaire)
<span class="anker" id="satz-3-5"></span>

Si $f$ est différentiable au point $\mathbf{x}$, toutes les dérivées partielles y existent, et le vecteur de [(3.5)](#gl-3-5) est le gradient : $\mathbf{g}=\nabla f(\mathbf{x})$. Réciproquement, $f$ est différentiable au point $\mathbf{x}$ si toutes les dérivées partielles existent au voisinage de $\mathbf{x}$ et sont continues au point $\mathbf{x}$.
:::

:::beweis Le vecteur est le gradient
On choisit dans [(3.5)](#gl-3-5) en particulier $\mathbf{h}=t\,\mathbf{e}_j$ avec un nombre $t\ne0$ ; alors $\lVert\mathbf{h}\rVert=|t|$ et $\mathbf{g}^{\top}\mathbf{h}=t\,g_j$. Le quotient s’écrit $\frac{f(\mathbf{x}+t\mathbf{e}_j)-f(\mathbf{x})-t\,g_j}{|t|}$ et tend vers $0$. Alors $\frac{f(\mathbf{x}+t\mathbf{e}_j)-f(\mathbf{x})}{t}-g_j$ tend aussi vers $0$, car ce nombre a la même valeur absolue. La dérivée partielle par rapport à $x_j$ existe donc, et elle vaut $g_j$. Cela vaut pour tout $j$.
:::

Pour la pratique, c’est le second énoncé qui importe. Les polynômes, la fonction exponentielle, la fonction logistique et tout ce que l’on construit à partir d’eux par les opérations élémentaires et la composition ont des dérivées partielles continues partout où ils sont définis. De telles fonctions sont donc différentiables, et [(3.4)](#gl-3-4) vaut pour elles. Les exceptions dans ce chapitre sont les points anguleux, comme pour $|x|$ ou $\max(x,\,0)$.

:::warnung Les dérivées partielles seules ne suffisent pas
La fonction $f(x_1,x_2)=\dfrac{x_1x_2}{x_1^2+x_2^2}$ avec $f(0,0)=0$ est nulle sur les deux axes, car on y a $x_1x_2=0$. Ses courbes de coupe passant par l’origine le long des axes sont donc horizontales : $\partial_1f(0,0)=\partial_2f(0,0)=0$, le gradient à l’origine est $\mathbf{0}$. L’approximation linéaire prévoit donc que $f$ est presque $0$ au voisinage de l’origine. Sur la diagonale $x_1=x_2=t$ avec $t\ne0$, on a pourtant $f(t,t)=t^2/(2t^2)=\tfrac12$, aussi petit que soit $t$. La fonction fait un saut à l’origine, et aucun plan ne l’épouse. Elle n’y est pas différentiable, bien que les deux dérivées partielles existent. Qui déduit l’approximation linéaire de l’existence du gradient a donc besoin de la différentiabilité, garantie par exemple par des dérivées partielles continues.
:::

::::beispiel [Exemple de calcul]
Pour $f(\mathbf{x})=x_1^2x_2+x_2^2$, les dérivées partielles $2x_1x_2$ et $x_1^2+2x_2$ sont des polynômes, donc continues partout, et $f$ est différentiable partout. Dans l’exemple de calcul associé à [(3.4)](#gl-3-4), l’erreur valait $0{,}001002$ pour $\lVert\mathbf{h}\rVert=\sqrt{0{,}0001+0{,}0004}\approx0{,}0224$, le quotient de [(3.5)](#gl-3-5) valait donc environ $0{,}045$. Si l’on divise $\mathbf{h}$ par deux, ce qui donne $(0{,}005;\ 0{,}01)^{\top}$, l’erreur vaut $f(1{,}005;\ 2{,}01)-6-0{,}07=0{,}000250\ldots$ et le quotient environ $0{,}022$ : il est divisé par deux en même temps que $\mathbf{h}$ et tend vers $0$.
::::

⁠**En bref :** Être différentiable signifie que l’approximation linéaire par le gradient a une erreur qui disparaît plus vite que $\lVert\mathbf{h}\rVert$ ; des dérivées partielles continues le garantissent, leur simple existence non.

:::hintergrund Pourquoi des dérivées partielles continues suffisent
On ne va pas de $\mathbf{x}$ à $\mathbf{x}+\mathbf{h}$ en biais, mais en deux tronçons parallèles aux axes : d’abord de $h_1$ dans la direction $x_1$, puis de $h_2$ dans la direction $x_2$. Sur chaque tronçon, une seule variable change, et d’après le théorème des accroissements finis pour une variable, la variation vaut exactement $\partial_jf\cdot h_j$, évaluée en un point intermédiaire du tronçon. Si les dérivées partielles sont continues, leurs valeurs en ces points intermédiaires sont proches de leurs valeurs au point $\mathbf{x}$, et la somme des deux tronçons ne diffère de $\nabla f(\mathbf{x})^{\top}\mathbf{h}$ que d’une quantité qui disparaît plus vite que $\lVert\mathbf{h}\rVert$. Pour le contre-exemple, c’est précisément ce raisonnement qui s’effondre : ses dérivées partielles existent certes en dehors de l’origine, mais elles ne sont pas continues. Sur l’axe $x_1=0$, par exemple, $\partial_1f(0,x_2)=1/x_2$, et cela devient arbitrairement grand à mesure que l’on s’approche de l’origine, où la valeur est $0$.
:::

:::aufgabe Exercice 9 ★ Dérivées partielles et gradients
<span class="anker" id="aufg-9"></span>

Calculez les dérivées partielles et le gradient au point indiqué.

<ol class="al">

<li>

$f(\mathbf{x})=3x_1-2x_2+5$ au point $(4,\,-1)$ ;

</li>

<li>

$f(\mathbf{x})=x_1\,\mathrm{e}^{x_2}$ aux points $(2,\,0)$ et $(1,\,1)$ ;

</li>

<li>

$f(\mathbf{x})=x_1x_2+x_2x_3+x_3x_1$ au point $(1,\,2,\,3)$.

</li>

</ol>

:::loesung
(a) $\partial_1f=3$, $\partial_2f=-2$, donc $\nabla f=(3,\,-2)^{\top}$ en tout point.

(b) $\partial_1f=\mathrm{e}^{x_2}$ et $\partial_2f=x_1\mathrm{e}^{x_2}$. Au point $(2,\,0)$, on a $\nabla f=(1,\,2)^{\top}$, au point $(1,\,1)$, on a $\nabla f=(\mathrm{e},\,\mathrm{e})^{\top}\approx(2{,}718;\ 2{,}718)^{\top}$.

(c) $\partial_1f=x_2+x_3$, $\partial_2f=x_1+x_3$, $\partial_3f=x_1+x_2$ ; au point $(1,\,2,\,3)$, on a donc $\nabla f=(5,\,4,\,3)^{\top}$.
:::
:::

:::aufgabe Exercice 10 ★★ Approximation linéaire à deux variables
<span class="anker" id="aufg-10"></span>

Soit $f(\mathbf{x})=x_1\,\mathrm{e}^{x_2}$.

<ol class="al">

<li>

À l’aide de l’approximation linéaire au point $(2,\,0)$, calculez une valeur approchée de $f(2{,}1;\ -0{,}05)$ et comparez avec la valeur exacte.

</li>

<li>

Laquelle des deux variations contribue le plus à la variation de $f$ ? Pourquoi se compensent-elles exactement dans l’approximation linéaire, mais pas dans la valeur exacte ?

</li>

</ol>

:::loesung
(a) On a $f(2,0)=2$ et $\nabla f(2,0)=(1,\,2)^{\top}$ d’après l’exercice [9](#aufg-9). Avec $\mathbf{h}=(0{,}1;\ -0{,}05)^{\top}$ :

$$f(2{,}1;\ -0{,}05)\approx2+1\cdot0{,}1+2\cdot(-0{,}05)=2+0{,}1-0{,}1=2{,}0 .$$

La valeur exacte est $2{,}1\,\mathrm{e}^{-0{,}05}\approx2{,}1\cdot0{,}951229\approx1{,}99758$. L’erreur vaut environ $0{,}0024$.

(b) Les deux variations contribuent autant, $+0{,}1$ et $-0{,}1$, et se compensent dans l’approximation linéaire. Dans la valeur exacte, en revanche, les variables s’influencent mutuellement : si $x_1$ augmente, $f$ réagit plus fortement à $x_2$, car $\partial_2f=x_1\mathrm{e}^{x_2}$ croît avec $x_1$. La diminution de $x_2$ agit donc un peu plus fortement que ne le suppose l’approximation linéaire. De telles interactions sont des produits de deux variations, ici par exemple $0{,}1\cdot(-0{,}05)=-0{,}005$, et font partie des termes d’ordre deux que l’approximation linéaire laisse de côté. La section [8](die-hesse-matrix-und-die-quadratische-naherung.html#stufe-8) les calcule (exercice [29](die-hesse-matrix-und-die-quadratische-naherung.html#aufg-29)).
:::
:::

:::aufgabe Exercice 11 ★★ Lignes de niveau et courbes de coupe
<span class="anker" id="aufg-11"></span>

Soit $f(\mathbf{x})=x_1^2x_2+x_2^2$ comme dans [(3.1)](#gl-3-1).

<ol class="al">

<li>

Quelle valeur $f$ prend-elle au point $(2,\,1)$ ? Donnez un autre point de la même ligne de niveau avec $x_1=0$.

</li>

<li>

Calculez $\nabla f(2,1)$ et les équations des deux courbes de coupe passant par $(2,\,1)$. Vérifiez leurs pentes.

</li>

</ol>

:::loesung
(a) $f(2,1)=4\cdot1+1=5$. Avec $x_1=0$, la ligne de niveau exige $x_2^2=5$ ; le point $(0;\ \sqrt5)\approx(0;\ 2{,}236)$, par exemple, s’y trouve.

(b) $\nabla f(2,1)=(2\cdot2\cdot1,\ 4+2\cdot1)^{\top}=(4,\,6)^{\top}$. La courbe de coupe le long de $x_2=1$ est $f(x_1,1)=x_1^2+1$, de pente $2x_1=4$ en $x_1=2$. La courbe de coupe le long de $x_1=2$ est $f(2,x_2)=4x_2+x_2^2$, de pente $4+2x_2=6$ en $x_2=1$. Les deux pentes coïncident avec les composantes du gradient.
:::
:::

:::aufgabe Exercice 12 ★★★ Continue, mais pas différentiable
<span class="anker" id="aufg-12"></span>

Soit $f(x_1,x_2)=\sqrt{|x_1x_2|}$.

<ol class="al">

<li>

Montrez que les deux dérivées partielles existent à l’origine et valent $0$.

</li>

<li>

Montrez avec $\mathbf{h}=(t,\,t)^{\top}$ que le quotient de [(3.5)](#gl-3-5) avec $\mathbf{g}=\mathbf{0}$ ne tend pas vers $0$. Pourquoi en découle-t-il que $f$ n’est pas différentiable à l’origine, bien que $f$ y soit continue ?

</li>

</ol>

:::loesung
(a) Sur les deux axes, on a $x_1x_2=0$, donc $f=0$. Ainsi, $\frac{f(h,0)-f(0,0)}{h}=0$ pour tout $h\ne0$, et de même pour la seconde variable. Les deux dérivées partielles à l’origine valent $0$.

(b) Si $f$ était différentiable à l’origine, le vecteur de [(3.5)](#gl-3-5) devrait, d’après le théorème de la section [3.5](#stufe-3-5), être le gradient $\mathbf{0}$. Or, avec $\mathbf{h}=(t,\,t)^{\top}$, on a $f(\mathbf{h})=\sqrt{t^2}=|t|$ et $\lVert\mathbf{h}\rVert=\sqrt2\,|t|$, donc

$$\frac{f(\mathbf{h})-f(\mathbf{0})-\mathbf{0}^{\top}\mathbf{h}}{\lVert\mathbf{h}\rVert}=\frac{|t|}{\sqrt2\,|t|}=\frac1{\sqrt2}\approx0{,}707 ,$$

pour tout $t\ne0$, aussi petit soit-il. Le quotient ne tend pas vers $0$, donc $f$ n’est pas différentiable. Pourtant, $f$ est continue, car $|f(\mathbf{x})|=\sqrt{|x_1|\,|x_2|}\le\max(|x_1|,|x_2|)\le\lVert\mathbf{x}\rVert$ tend vers $0$ lorsque $\mathbf{x}$ tend vers $\mathbf{0}$. Le terrain ne présente pas de trou à l’origine, mais un pli le long de la diagonale, qu’aucun plan ne peut épouser.
:::
:::

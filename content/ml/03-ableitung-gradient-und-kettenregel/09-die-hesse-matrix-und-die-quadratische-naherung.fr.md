---
title: La matrice hessienne et l’approximation quadratique
pfad: Informatique / Apprentissage automatique / Fondements mathématiques / Dérivée, gradient et règle de dérivation en chaîne
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Chapitre 3 : Dérivée, gradient et règle de dérivation en chaîne
nachschlagen: ja
order: 15230900
summary: Le gradient décrit l’inclinaison du terrain, mais pas son bombement.
tags: dérivées partielles secondes, matrice hessienne, différence croisée, dérivée directionnelle seconde
lang: fr
---

<span class="anker" id="stufe-8"></span>

:::zweck
Le gradient décrit l’inclinaison du terrain, mais pas son bombement. Les dérivées partielles secondes sont rassemblées dans la matrice hessienne. Celle-ci est symétrique, et grâce à elle, l’approximation linéaire devient quadratique. Ses valeurs propres indiquent avec quelle force le terrain se courbe dans les différentes directions et relient cette section aux formes quadratiques du [chapitre 2](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/projektion-eigenwerte-und-zerlegungen.html).
:::

### Dérivées partielles secondes

<span class="anker" id="stufe-8-1"></span>

Les dérivées partielles $\partial_jf$ sont elles-mêmes des fonctions de $\mathbf{x}$. On peut les dériver partiellement une nouvelle fois, par rapport à la même variable ou à une autre. Cela décrit comment la pente dans la direction $x_j$ change lorsqu’on avance dans la direction $x_i$.

:::definition Définition 8.1 (Dérivées partielles secondes)
<span class="anker" id="satz-8-1"></span>

Les __dérivées partielles secondes__ de $f:\mathbb{R}^d\to\mathbb{R}$ sont

<span class="anker" id="gl-8-1"></span>
$$\frac{\partial^2f}{\partial x_i\,\partial x_j}=\frac{\partial}{\partial x_i}\Bigl(\frac{\partial f}{\partial x_j}\Bigr), \tag{8.1}$$

obtenues en dérivant d’abord par rapport à $x_j$, puis par rapport à $x_i$. Pour $i=j$, on écrit $\partial^2f/\partial x_i^2$. Pour $i\ne j$, on les appelle dérivées croisées.
:::

::::beispiel [Exemple de calcul]
Pour $f(\mathbf{x})=x_1^2x_2+x_2^2$, on a $\partial_1f=2x_1x_2$ et $\partial_2f=x_1^2+2x_2$, donc

$$\begin{gathered} \frac{\partial^2f}{\partial x_1^2}=\frac{\partial}{\partial x_1}(2x_1x_2)=2x_2,\qquad \frac{\partial^2f}{\partial x_2\,\partial x_1}=\frac{\partial}{\partial x_2}(2x_1x_2)=2x_1,\\ \frac{\partial^2f}{\partial x_1\,\partial x_2}=\frac{\partial}{\partial x_1}(x_1^2+2x_2)=2x_1,\qquad \frac{\partial^2f}{\partial x_2^2}=\frac{\partial}{\partial x_2}(x_1^2+2x_2)=2 . \end{gathered}$$

Au point $(1,\,2)$, cela donne $4$, $2$, $2$ et $2$. Les deux dérivées croisées sont égales, bien qu’elles aient été obtenues par des chemins différents.
::::

⁠**En bref :** Les dérivées partielles secondes dérivent une dérivée partielle une nouvelle fois partiellement ; les dérivées croisées décrivent comment la pente dans une direction change lorsqu’on se déplace dans une autre direction.

### La matrice hessienne

<span class="anker" id="stufe-8-2"></span>

Une fonction de $d$ variables a $d^2$ dérivées partielles secondes. Comme les dérivées premières dans le gradient, on les réunit dans un seul objet, ici une matrice carrée.

:::definition Définition 8.2 (Matrice hessienne)
<span class="anker" id="satz-8-2"></span>

La matrice $d\times d$

<span class="anker" id="gl-8-2"></span>
$$\mathbf{H}_f(\mathbf{x})=\begin{pmatrix}\dfrac{\partial^2f}{\partial x_1^2}&\cdots&\dfrac{\partial^2f}{\partial x_1\,\partial x_d}\\ \vdots&&\vdots\\ \dfrac{\partial^2f}{\partial x_d\,\partial x_1}&\cdots&\dfrac{\partial^2f}{\partial x_d^2}\end{pmatrix},\qquad \bigl(\mathbf{H}_f(\mathbf{x})\bigr)_{ij}=\frac{\partial^2f}{\partial x_i\,\partial x_j}(\mathbf{x}), \tag{8.2}$$

s’appelle la __matrice hessienne__ de $f$ au point $\mathbf{x}$.
:::

La matrice doit son nom au mathématicien Otto Hesse ; certains livres écrivent $\nabla^2f$. Sa colonne $j$ est le gradient de la fonction $\partial_jf$. Elle est donc étroitement liée à la matrice jacobienne du gradient, la fonction à valeurs vectorielles $\mathbf{x}\mapsto\nabla f(\mathbf{x})$ : le coefficient $(i,j)$ de celle-ci est $\partial(\partial_if)/\partial x_j$, la dérivée dans l’autre ordre. La sous-section suivante montre que les deux ordres donnent presque toujours le même résultat ; la matrice hessienne est alors la matrice jacobienne du gradient.

::::beispiel [Exemple de calcul]
Pour $f(\mathbf{x})=x_1^2x_2+x_2^2$, on a, d’après la sous-section précédente,

$$\mathbf{H}_f(\mathbf{x})=\begin{pmatrix}2x_2&2x_1\\2x_1&2\end{pmatrix},\qquad \mathbf{H}_f(1,2)=\begin{pmatrix}4&2\\2&2\end{pmatrix}.$$

Pour une fonction quadratique $f(\mathbf{x})=\tfrac12\mathbf{x}^{\top}\mathbf{A}\mathbf{x}+\mathbf{b}^{\top}\mathbf{x}+c$ avec $\mathbf{A}$ symétrique, on a d’après la section [7](ableiten-nach-vektoren-und-matrizen.html#stufe-7) $\nabla f(\mathbf{x})=\mathbf{A}\mathbf{x}+\mathbf{b}$, et donc $\mathbf{H}_f=\mathbf{A}$ en tout point. Pour la cuvette $x_1^2+4x_2^2$ de la section [4](richtungsableitung-und-steilster-anstieg.html#stufe-4), on a $\mathbf{A}=\operatorname{diag}(2;\,8)$.
::::

⁠**En bref :** La matrice hessienne rassemble toutes les dérivées partielles secondes ; pour une fonction quadratique $\tfrac12\mathbf{x}^{\top}\mathbf{A}\mathbf{x}+\mathbf{b}^{\top}\mathbf{x}+c$, elle vaut $\mathbf{A}$ partout.

### Le théorème de Schwarz

<span class="anker" id="stufe-8-3"></span>

Dans l’exemple de calcul, les deux dérivées croisées étaient égales. Ce n’est pas un hasard : cela vaut pour toutes les fonctions dont les dérivées secondes ne présentent pas de sauts.

:::satz Théorème 8.3 (Théorème de Schwarz)
<span class="anker" id="satz-8-3"></span>

Si toutes les dérivées partielles secondes de $f$ existent au voisinage de $\mathbf{x}$ et sont continues au point $\mathbf{x}$, alors on a en ce point

<span class="anker" id="gl-8-3"></span>
$$\frac{\partial^2f}{\partial x_i\,\partial x_j}=\frac{\partial^2f}{\partial x_j\,\partial x_i} \tag{8.3}$$

pour tous $i,j$. La matrice hessienne est alors symétrique.
:::

On voit la raison sur un calcul dans lequel l’ordre n’intervient pas du tout. On se déplace à partir de $\mathbf{x}$ de $h$ dans la direction $x_1$ et de $k$ dans la direction $x_2$, et l’on forme la __différence croisée__

$$\Delta(h,k)=f(x_1+h,\,x_2+k)-f(x_1+h,\,x_2)-f(x_1,\,x_2+k)+f(x_1,\,x_2).$$

Si l’on regroupe le premier terme avec le troisième et le deuxième avec le quatrième, $\Delta$ est la variation de la différence $f(x_1+h,\cdot)-f(x_1,\cdot)$ lors du pas $k$ dans la direction $x_2$ : comment la montée dans la direction $x_1$ change-t-elle lorsqu’on avance dans la direction $x_2$ ? Divisé par $hk$, ce nombre tend, pour $h$ et $k$ petits, vers la dérivée prise d’abord par rapport à $x_1$, puis par rapport à $x_2$. Si l’on regroupe plutôt les deux premiers termes et les deux derniers, on lit le même nombre comme la variation de la montée dans la direction $x_2$ lors du pas dans la direction $x_1$, et le quotient tend vers la dérivée dans l’autre ordre. Les deux limites appartiennent au même nombre $\Delta/(hk)$. La continuité garantit que l’ordre des deux passages à la limite n’a pas d’importance.

::::beispiel [Exemple de calcul]
Pour $f(\mathbf{x})=x_1^2x_2+x_2^2$ au point $(1,\,2)$ avec $h=k=0{,}1$, on a

$$\Delta=f(1{,}1;\ 2{,}1)-f(1{,}1;\ 2)-f(1;\ 2{,}1)+f(1,2)=6{,}951-6{,}42-6{,}51+6=0{,}021,$$

donc $\Delta/(hk)=2{,}1$, proche de la dérivée croisée $2x_1=2$. L’écart vient de ce que $2x_1$ n’est pas constant entre $x_1=1$ et $x_1=1{,}1$.
::::

⁠**En bref :** Lorsque les dérivées secondes sont continues, l’ordre de dérivation est indifférent, et la matrice hessienne est symétrique.

:::hintergrund Quand les dérivées secondes ne sont pas continues
Sans continuité, le théorème peut être faux. Le contre-exemple classique est $f(x_1,x_2)=x_1x_2\,\frac{x_1^2-x_2^2}{x_1^2+x_2^2}$ avec $f(0,0)=0$. Si l’on calcule les dérivées partielles premières sur les axes, on obtient $\partial_1f(0,x_2)=-x_2$ et $\partial_2f(x_1,0)=x_1$. En dérivant la première par rapport à $x_2$, on obtient $-1$ à l’origine ; en dérivant la seconde par rapport à $x_1$, on obtient $+1$. Les dérivées croisées à l’origine sont donc différentes, parce que les dérivées secondes y font un saut. Pour les fonctions de ce chapitre sans point anguleux, cela ne se produit pas ; elles sont construites à partir de polynômes, de fonctions exponentielles et des opérations élémentaires, et ont, partout où elles sont définies, des dérivées continues de tout ordre.
:::

### L’approximation quadratique

<span class="anker" id="stufe-8-4"></span>

Pour une variable, la tangente a été améliorée par une parabole dans la section [1.5](die-ableitung.html#stufe-1-5). Pour plusieurs variables, le plan tangent est remplacé par une surface bombée, dont le bombement est décrit par la matrice hessienne.

:::satz Théorème 8.4 (Approximation quadratique)
<span class="anker" id="satz-8-4"></span>

Si $f$ a des dérivées partielles secondes continues au voisinage de $\mathbf{x}$, alors

<span class="anker" id="gl-8-4"></span>
$$f(\mathbf{x}+\mathbf{h})=f(\mathbf{x})+\nabla f(\mathbf{x})^{\top}\mathbf{h}+\tfrac12\,\mathbf{h}^{\top}\mathbf{H}_f(\mathbf{x})\,\mathbf{h}+r_2(\mathbf{h})\qquad\text{avec}\qquad\lim_{\mathbf{h}\to\mathbf{0}}\frac{r_2(\mathbf{h})}{\lVert\mathbf{h}\rVert^2}=0 . \tag{8.4}$$
:::

:::herleitung L’approximation quadratique le long d’une droite
On restreint $f$ à la droite passant par $\mathbf{x}$ dans la direction $\mathbf{h}$ : $\phi(t)=f(\mathbf{x}+t\,\mathbf{h})$. C’est une fonction d’une variable. D’après [(6.4)](die-kettenregel-fur-mehrere-variablen.html#gl-6-4), on a $\phi'(t)=\nabla f(\mathbf{x}+t\mathbf{h})^{\top}\mathbf{h}=\sum_jh_j\,\partial_jf(\mathbf{x}+t\mathbf{h})$. On dérive chaque terme une nouvelle fois avec [(6.4)](die-kettenregel-fur-mehrere-variablen.html#gl-6-4), cette fois pour la fonction $\partial_jf$ :

$$\phi''(t)=\sum_{j=1}^dh_j\sum_{i=1}^d\frac{\partial^2f}{\partial x_i\,\partial x_j}(\mathbf{x}+t\mathbf{h})\,h_i=\mathbf{h}^{\top}\mathbf{H}_f(\mathbf{x}+t\mathbf{h})\,\mathbf{h} .$$

L’approximation quadratique [(1.6)](die-ableitung.html#gl-1-6) de $\phi$ en $0$, évaluée en $t=1$, s’écrit $\phi(1)\approx\phi(0)+\phi'(0)+\tfrac12\phi''(0)$, et c’est [(8.4)](#gl-8-4). Que l’erreur disparaisse plus vite que $\lVert\mathbf{h}\rVert^2$ découle de la continuité des dérivées secondes.
:::

Le nouveau terme $\tfrac12\mathbf{h}^{\top}\mathbf{H}_f\mathbf{h}$ est une forme quadratique au sens du [chapitre 2, section 5.1](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/quadratische-formen.html#stufe-5-1), avec la matrice hessienne pour matrice. Au voisinage de $\mathbf{x}$, la fonction ressemble donc à un plan plus une forme quadratique.

::::beispiel [Exemple de calcul]
Pour $f(\mathbf{x})=x_1^2x_2+x_2^2$ au point $(1,\,2)$ et $\mathbf{h}=(0{,}01;\ 0{,}02)^{\top}$ comme dans la section [3.4](partielle-ableitungen-und-der-gradient.html#stufe-3-4), on a

$$\tfrac12\,\mathbf{h}^{\top}\mathbf{H}_f\mathbf{h}=\tfrac12\bigl(4\cdot0{,}01^2+2\cdot2\cdot0{,}01\cdot0{,}02+2\cdot0{,}02^2\bigr)=\tfrac12\,(0{,}0004+0{,}0008+0{,}0008)=0{,}001$$

(Fig. [15](#abb-15)). L’approximation quadratique vaut $6+0{,}14+0{,}001=6{,}141$, la valeur exacte $6{,}141002$. L’erreur est passée de $0{,}001002$ à $0{,}000002$. Le reste est le terme d’ordre trois : $x_1^2x_2$ contient le terme $h_1^2h_2=0{,}0001\cdot0{,}02=0{,}000002$, qu’aucune approximation quadratique ne saisit.

:::abbildung ml/k3rtaylor2 15
Le terme de courbure de l’approximation quadratique comme somme double ; les deux termes croisés $h_1\cdot2\cdot h_2$ et $h_2\cdot2\cdot h_1$ sont réunis dans le terme du milieu.
:::
::::

⁠**En bref :** Près de $\mathbf{x}$, on a $f(\mathbf{x}+\mathbf{h})\approx f(\mathbf{x})+\nabla f(\mathbf{x})^{\top}\mathbf{h}+\tfrac12\mathbf{h}^{\top}\mathbf{H}_f(\mathbf{x})\mathbf{h}$ : un plan plus une forme quadratique.

### La courbure dans une direction

<span class="anker" id="stufe-8-5"></span>

Avec quelle force le terrain est-il bombé lorsqu’on part de $\mathbf{x}$ dans la direction $\mathbf{u}$ ? La démonstration de la sous-section précédente a déjà donné la réponse : la dérivée seconde de $\phi(t)=f(\mathbf{x}+t\mathbf{u})$ en $0$ vaut $\mathbf{u}^{\top}\mathbf{H}_f(\mathbf{x})\mathbf{u}$.

:::definition Définition 8.5 (Courbure dans une direction)
<span class="anker" id="satz-8-5"></span>

Pour un vecteur $\mathbf{u}$ de longueur $1$,

<span class="anker" id="gl-8-5"></span>
$$\frac{\mathrm{d}^2}{\mathrm{d} t^2}f(\mathbf{x}+t\,\mathbf{u})\Big|_{t=0}=\mathbf{u}^{\top}\mathbf{H}_f(\mathbf{x})\,\mathbf{u} \tag{8.5}$$

s’appelle la __dérivée directionnelle seconde__ de $f$ au point $\mathbf{x}$ dans la direction $\mathbf{u}$. Elle mesure la courbure de la courbe de coupe dans cette direction.
:::

Avec les résultats du [chapitre 2](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/projektion-eigenwerte-und-zerlegungen.html), on peut dire immédiatement quelles sont la plus grande et la plus petite valeur possible de cette courbure. La matrice hessienne est symétrique et a, d’après le théorème spectral du [chapitre 2, section 7.6](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/diagonalisierung-und-spektralsatz.html#stufe-7-6), des valeurs propres réelles et des vecteurs propres perpendiculaires entre eux.

:::satz Théorème 8.6 (Courbure et valeurs propres)
<span class="anker" id="satz-8-6"></span>

Soient $\lambda_{\min}$ et $\lambda_{\max}$ la plus petite et la plus grande valeur propre de la matrice hessienne symétrique $\mathbf{H}_f(\mathbf{x})$. Alors, pour toute direction $\mathbf{u}$ telle que $\lVert\mathbf{u}\rVert=1$,

<span class="anker" id="gl-8-6"></span>
$$\lambda_{\min}\le\mathbf{u}^{\top}\mathbf{H}_f(\mathbf{x})\,\mathbf{u}\le\lambda_{\max}. \tag{8.6}$$

Dans la direction d’un vecteur propre, la courbure est exactement la valeur propre associée. Si $\mathbf{H}_f(\mathbf{x})$ est définie positive, la courbure est positive dans toutes les directions ; si elle est indéfinie, le terrain se courbe vers le haut dans certaines directions et vers le bas dans d’autres.
:::

L’inégalité est l’énoncé du [chapitre 2, section 8.5](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/positiv-definite-matrizen.html#stufe-8-5), sur la plus grande et la plus petite valeur d’une forme quadratique sur le cercle unité. Pour un vecteur propre $\mathbf{u}$ de valeur propre $\lambda$, on a $\mathbf{u}^{\top}\mathbf{H}_f\mathbf{u}=\lambda\,\mathbf{u}^{\top}\mathbf{u}=\lambda$. Les notions de matrice définie positive et indéfinie viennent du [chapitre 2, section 8](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/positiv-definite-matrizen.html#stufe-8) ; on y lisait la forme d’une forme quadratique sur ses valeurs propres : cuvette, gouttière ou selle. Par l’approximation quadratique [(8.4)](#gl-8-4), cela se transpose au terrain au voisinage de $\mathbf{x}$ : pour une matrice hessienne définie positive, les lignes de niveau du terme de courbure sont des ellipses dont les axes principaux, d’après le [chapitre 2, section 7.7](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/diagonalisierung-und-spektralsatz.html#stufe-7-7), sont dirigés selon les vecteurs propres et sont courts dans la direction de forte courbure.

::::beispiel [Exemple de calcul 1]
Pour la cuvette $f(\mathbf{x})=x_1^2+4x_2^2$, on a $\mathbf{H}_f=\operatorname{diag}(2;\,8)$, de valeurs propres $2$ et $8$. Dans la direction $x_1$, la courbure vaut $2$, dans la direction $x_2$, elle vaut $8$, et dans la direction $\mathbf{u}=(1,\,1)^{\top}/\sqrt2$, elle vaut $\tfrac12(2+8)=5$. Cela explique les lignes de niveau allongées de la section [4.4](richtungsableitung-und-steilster-anstieg.html#stufe-4-4) : dans la direction $x_2$, la cuvette se courbe quatre fois plus fortement, ses parois y sont plus raides, et les ellipses sont étroites dans cette direction.
::::

::::beispiel [Exemple de calcul 2]
Pour $f(\mathbf{x})=x_1^2x_2+x_2^2$ au point $(1,\,2)$, on a $\mathbf{H}_f=\bigl(\begin{smallmatrix}4&2\\2&2\end{smallmatrix}\bigr)$. La trace $6$ et le déterminant $4$ donnent, d’après le [chapitre 2, section 6.5](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/eigenwerte-und-eigenvektoren.html#stufe-6-5), les valeurs propres $3\pm\sqrt5$, soit environ $5{,}236$ et $0{,}764$. Les deux sont positives, la matrice hessienne est définie positive : au voisinage de $(1,\,2)$, le terrain se courbe vers le haut dans toutes les directions. Dans la direction $\mathbf{u}=(1,\,1)^{\top}/\sqrt2$, la courbure vaut

$$\mathbf{u}^{\top}\mathbf{H}_f\mathbf{u}=\tfrac12\,(4+2+2+2)=5,$$

et elle est comprise entre $0{,}764$ et $5{,}236$ (Fig. [16](#abb-16)).

:::abbildung ml/k3rkruemmung 16
La courbure de $f(\mathbf{x})=x_1^2x_2+x_2^2$ au point $(1,\,2)$ dans la direction de la bissectrice ; le facteur $\tfrac12$ vient de $u_iu_j=\tfrac12$.
:::
::::

⁠**En bref :** La courbure dans la direction $\mathbf{u}$ est $\mathbf{u}^{\top}\mathbf{H}_f\mathbf{u}$ ; elle est comprise entre la plus petite et la plus grande valeur propre de la matrice hessienne, et les signes de celles-ci décident si le terrain se courbe comme une cuvette ou comme une selle.

:::hintergrund Matrice hessienne fois vecteur, sans la matrice hessienne
Lorsqu’il y a beaucoup de variables, la matrice hessienne est énorme : pour un million de variables, elle a $10^{12}$ coefficients. Mais souvent, on n’a besoin que de son produit par un vecteur $\mathbf{v}$. On l’obtient sans construire la matrice. Le nombre $\nabla f(\mathbf{x})^{\top}\mathbf{v}=\sum_jv_j\,\partial_jf(\mathbf{x})$ est une fonction de $\mathbf{x}$, et son gradient a pour composantes $\sum_jv_j\,\partial^2f/\partial x_i\partial x_j$ ; on a donc $\nabla_{\mathbf{x}}\bigl(\nabla f(\mathbf{x})^{\top}\mathbf{v}\bigr)=\mathbf{H}_f(\mathbf{x})\,\mathbf{v}$. Pour $f(\mathbf{x})=x_1^2x_2+x_2^2$ et $\mathbf{v}=(1,\,1)^{\top}$, on a $\nabla f^{\top}\mathbf{v}=2x_1x_2+x_1^2+2x_2$, de gradient $(2x_2+2x_1,\ 2x_1+2)^{\top}$, donc $(6,\,4)^{\top}$ au point $(1,\,2)$, et c’est bien $\mathbf{H}_f\mathbf{v}=(4+2,\ 2+2)^{\top}$. On calcule donc deux gradients au lieu d’une matrice à $d^2$ coefficients.
:::

:::aufgabe Exercice 28 ★ Matrices hessiennes
<span class="anker" id="aufg-28"></span>

Calculez la matrice hessienne au point indiqué et vérifiez la symétrie.

<ol class="al">

<li>

$f(\mathbf{x})=x_1^3+x_1x_2^2$ au point $(1,\,2)$ ;

</li>

<li>

$f(\mathbf{x})=\mathrm{e}^{x_1+2x_2}$ au point $(0,\,0)$. Quel est le rang de la matrice ?

</li>

<li>

$f(\mathbf{x})=x_1x_2x_3$ au point $(1,\,2,\,3)$.

</li>

</ol>

:::loesung
(a) $\partial_1f=3x_1^2+x_2^2$ et $\partial_2f=2x_1x_2$, donc

$$\mathbf{H}_f(\mathbf{x})=\begin{pmatrix}6x_1&2x_2\\2x_2&2x_1\end{pmatrix},\qquad \mathbf{H}_f(1,2)=\begin{pmatrix}6&4\\4&2\end{pmatrix};$$

les dérivées croisées $\partial_2(3x_1^2+x_2^2)=2x_2$ et $\partial_1(2x_1x_2)=2x_2$ sont égales.

(b) Avec $f=\mathrm{e}^{x_1+2x_2}$, on a $\partial_1f=f$ et $\partial_2f=2f$, donc $\mathbf{H}_f=f\cdot\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ et, à l’origine, $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$. La deuxième ligne est le double de la première ; le rang vaut $1$, les valeurs propres sont $5$ et $0$. C’est cohérent : $f$ ne dépend que de $x_1+2x_2$ et est constante dans la direction $(2,\,-1)^{\top}$ ; elle n’est donc pas courbée dans cette direction.

(c) $\partial_1f=x_2x_3$, $\partial_2f=x_1x_3$, $\partial_3f=x_1x_2$, donc

$$\mathbf{H}_f(\mathbf{x})=\begin{pmatrix}0&x_3&x_2\\x_3&0&x_1\\x_2&x_1&0\end{pmatrix},\qquad \mathbf{H}_f(1,2,3)=\begin{pmatrix}0&3&2\\3&0&1\\2&1&0\end{pmatrix}.$$
:::
:::

:::aufgabe Exercice 29 ★★ Approximation quadratique
<span class="anker" id="aufg-29"></span>

Soit $f(\mathbf{x})=x_1\,\mathrm{e}^{x_2}$ comme dans l’exercice [10](partielle-ableitungen-und-der-gradient.html#aufg-10).

<ol class="al">

<li>

Calculez $\mathbf{H}_f(2,0)$.

</li>

<li>

Calculez avec l’approximation quadratique au point $(2,\,0)$ une valeur approchée de $f(2{,}1;\ -0{,}05)$ et comparez-la avec l’approximation linéaire de l’exercice [10](partielle-ableitungen-und-der-gradient.html#aufg-10) et avec la valeur exacte.

</li>

</ol>

:::loesung
(a) $\partial_1^2f=0$, $\partial_1\partial_2f=\mathrm{e}^{x_2}$, $\partial_2^2f=x_1\mathrm{e}^{x_2}$, donc $\mathbf{H}_f(2,0)=\bigl(\begin{smallmatrix}0&1\\1&2\end{smallmatrix}\bigr)$.

(b) Avec $\mathbf{h}=(0{,}1;\ -0{,}05)^{\top}$, on a

$$\tfrac12\,\mathbf{h}^{\top}\mathbf{H}_f\mathbf{h}=\tfrac12\bigl(0+2\cdot1\cdot0{,}1\cdot(-0{,}05)+2\cdot0{,}05^2\bigr)=\tfrac12\,(-0{,}01+0{,}005)=-0{,}0025 .$$

L’approximation quadratique vaut $2+0-0{,}0025=1{,}9975$, l’approximation linéaire valait $2{,}0$, la valeur exacte est $1{,}997582$. L’erreur passe de $0{,}0024$ à $0{,}00008$. Le terme croisé $-0{,}005$ est l’interaction de l’exercice [10](partielle-ableitungen-und-der-gradient.html#aufg-10).
:::
:::

:::aufgabe Exercice 30 ★★ Courbures d’une cuvette oblique
<span class="anker" id="aufg-30"></span>

Soit $f(\mathbf{x})=x_1^2+4x_2^2+x_1x_2$.

<ol class="al">

<li>

Écrivez $f$ sous la forme $\tfrac12\mathbf{x}^{\top}\mathbf{H}\mathbf{x}$ et donnez $\mathbf{H}$.

</li>

<li>

Calculez les valeurs propres de $\mathbf{H}$ et les courbures dans les directions $\mathbf{e}_1$, $\mathbf{e}_2$ et $(1,\,-1)^{\top}/\sqrt2$. Vérifiez [(8.6)](#gl-8-6).

</li>

<li>

Dans quelle direction la courbure est-elle la plus grande ? Donnez un vecteur propre.

</li>

</ol>

:::loesung
(a) $\tfrac12\mathbf{x}^{\top}\mathbf{H}\mathbf{x}$ avec $\mathbf{H}=\bigl(\begin{smallmatrix}2&1\\1&8\end{smallmatrix}\bigr)$ donne $\tfrac12\,(2x_1^2+2x_1x_2+8x_2^2)=x_1^2+x_1x_2+4x_2^2$. C’est aussi la matrice hessienne de $f$.

(b) Trace $10$, déterminant $16-1=15$, donc $\lambda^2-10\lambda+15=0$ et $\lambda=5\pm\sqrt{10}$, soit environ $8{,}162$ et $1{,}838$. Les courbures sont $\mathbf{e}_1^{\top}\mathbf{H}\mathbf{e}_1=2$, $\mathbf{e}_2^{\top}\mathbf{H}\mathbf{e}_2=8$ et, pour $\mathbf{u}=(1,\,-1)^{\top}/\sqrt2$ : $\tfrac12\,(2-1-1+8)=4$. Toutes les trois se situent entre $1{,}838$ et $8{,}162$.

(c) La courbure est la plus grande dans la direction d’un vecteur propre associé à $\lambda=5+\sqrt{10}$. La première ligne de $(\mathbf{H}-\lambda\mathbf{I})\mathbf{v}=\mathbf{0}$ donne $(2-\lambda)v_1+v_2=0$, donc $\mathbf{v}=(1;\ 3+\sqrt{10})^{\top}\approx(1;\ 6{,}162)^{\top}$, soit, après normalisation, environ $(0{,}160;\ 0{,}987)^{\top}$. C’est presque la direction $x_2$, légèrement tournée par le terme croisé $x_1x_2$.
:::
:::

:::aufgabe Exercice 31 ★★★ Des dérivées croisées différentes
<span class="anker" id="aufg-31"></span>

Soit $f(x_1,x_2)=x_1x_2\,\dfrac{x_1^2-x_2^2}{x_1^2+x_2^2}$ pour $\mathbf{x}\ne\mathbf{0}$ et $f(0,0)=0$.

<ol class="al">

<li>

Montrez à l’aide du taux d’accroissement que $\partial_1f(0,x_2)=-x_2$ pour $x_2\ne0$ et que $\partial_1f(0,0)=0$. Calculez de même $\partial_2f(x_1,0)$.

</li>

<li>

Déduisez-en que les deux dérivées croisées à l’origine valent $-1$ et $+1$. Quelle hypothèse du théorème de Schwarz n’est pas satisfaite ?

</li>

</ol>

:::loesung
(a) Sur l’axe $x_1=0$, on a $f=0$. Pour $x_2\ne0$,

$$\partial_1f(0,x_2)=\lim_{h\to0}\frac{f(h,x_2)-0}{h}=\lim_{h\to0}x_2\,\frac{h^2-x_2^2}{h^2+x_2^2}=x_2\cdot\frac{-x_2^2}{x_2^2}=-x_2 .$$

À l’origine, $f(h,0)=0$, donc $\partial_1f(0,0)=0$ ; la formule $-x_2$ vaut donc aussi pour $x_2=0$. De même, $\partial_2f(x_1,0)=\lim_k x_1\frac{x_1^2-k^2}{x_1^2+k^2}=x_1$.

(b) D’abord par rapport à $x_1$, puis par rapport à $x_2$ : $\frac{\partial}{\partial x_2}(-x_2)=-1$. D’abord par rapport à $x_2$, puis par rapport à $x_1$ : $\frac{\partial}{\partial x_1}(x_1)=+1$. Les dérivées croisées à l’origine sont différentes. L’hypothèse non satisfaite est la continuité des dérivées secondes à l’origine : en dehors de l’origine, la dérivée croisée vaut $-1$ en tout point de l’axe des $x_2$ et $+1$ en tout point de l’axe des $x_1$. Elle fait donc un saut à l’origine, et les deux ordres de dérivation s’en approchent par des côtés différents.
:::
:::

---
title: Dérivation numérique et vérification du gradient
pfad: Informatique / Apprentissage automatique / Fondements mathématiques / Dérivée, gradient et règle de dérivation en chaîne
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Chapitre 3 : Dérivée, gradient et règle de dérivation en chaîne
nachschlagen: ja
order: 15231200
summary: On peut aussi estimer des dérivées sans formule : on évalue la fonction en deux points proches et l’on forme le taux d’accroissement.
tags: différence avant, erreur de troncature, différence centrée, nombres à virgule flottante, epsilon machine, annulation catastrophique, vérification du gradient, erreur relative
lang: fr
---

<span class="anker" id="stufe-11"></span>

:::zweck
On peut aussi estimer des dérivées sans formule : on évalue la fonction en deux points proches et l’on forme le taux d’accroissement. C’est trop lent pour calculer ainsi toutes les dérivées d’une fonction ayant beaucoup d’entrées, mais idéal pour vérifier une dérivée établie à la main ou programmée. Cette section montre quelle est la précision des deux taux usuels, pourquoi un pas trop petit est nuisible et comment effectuer et évaluer une vérification du gradient.
:::

### La différence avant

<span class="anker" id="stufe-11-1"></span>

D’après la définition [(1.3)](die-ableitung.html#gl-1-3), le taux d’accroissement tend vers la dérivée lorsque $h$ tend vers zéro. Si on le calcule avec un petit $h$ fixe, on obtient une approximation, et la question est de savoir quelle est sa qualité.

:::definition Définition 11.1 (Différence avant)
<span class="anker" id="satz-11-1"></span>

Pour un pas fixe $h>0$,

<span class="anker" id="gl-11-1"></span>
$$D_+f(x)=\frac{f(x+h)-f(x)}{h} \tag{11.1}$$

s’appelle la __différence avant__. Son écart à $f'(x)$, qui vient uniquement de ce que $h$ n’est pas nul, s’appelle l’__erreur de troncature__.
:::

L’approximation quadratique [(1.6)](die-ableitung.html#gl-1-6) fournit l’erreur de troncature : si l’on y substitue $f(x+h)\approx f(x)+f'(x)h+\tfrac12f''(x)h^2$, on obtient

<span class="anker" id="gl-11-2"></span>
$$D_+f(x)\approx f'(x)+\tfrac12f''(x)\,h . \tag{11.2}$$

L’erreur est donc à peu près proportionnelle à $h$ : un $h$ dix fois plus petit donne une erreur de troncature environ dix fois plus petite.

::::beispiel [Exemple de calcul]
Pour $f(x)=x^3$ en $2$ avec $h=10^{-3}$, on a $2{,}001^3=8{,}012006001$ et

$$D_+f(2)=\frac{8{,}012006001-8}{0{,}001}=12{,}006001 .$$

L’erreur $0{,}006001$ concorde avec $\tfrac12f''(2)\,h=\tfrac12\cdot12\cdot0{,}001=0{,}006$ ; le reste $0{,}000001=h^2$ est le terme suivant.
::::

⁠**En bref :** La différence avant a une erreur de troncature d’environ $\tfrac12f''(x)\,h$, proportionnelle au pas.

### La différence centrée

<span class="anker" id="stufe-11-2"></span>

La différence avant mesure la pente de la sécante entre $x$ et $x+h$, et pour une courbe incurvée, cette sécante est systématiquement plus raide ou moins raide que la tangente en $x$. Si l’on place la sécante symétriquement autour de $x$, de $x-h$ à $x+h$, cette erreur se compense.

:::definition Définition 11.2 (Différence centrée)
<span class="anker" id="satz-11-2"></span>

Pour un pas fixe $h>0$,

<span class="anker" id="gl-11-3"></span>
$$D_0f(x)=\frac{f(x+h)-f(x-h)}{2h} \tag{11.3}$$

s’appelle la __différence centrée__.
:::

:::satz Théorème 11.3 (Erreur de troncature de la différence centrée)
<span class="anker" id="satz-11-3"></span>

Si $f$ a une dérivée troisième continue, alors

<span class="anker" id="gl-11-4"></span>
$$D_0f(x)\approx f'(x)+\tfrac16f'''(x)\,h^2 . \tag{11.4}$$

L’erreur de troncature est donc à peu près proportionnelle à $h^2$.
:::

:::herleitung Pourquoi la courbure s’élimine
On prolonge d’un terme l’approximation quadratique de la section [1.5](die-ableitung.html#stufe-1-5). Si, comme on l’a fait là pour la parabole, on ajuste en plus la dérivée troisième, le terme $\tfrac16f'''(x)\,h^3$ s’ajoute ; le facteur $\tfrac16$ vient de ce que la dérivée troisième de $h^3$ vaut $6$. On a ainsi

$$f(x\pm h)\approx f(x)\pm f'(x)\,h+\tfrac12f''(x)\,h^2\pm\tfrac16f'''(x)\,h^3 .$$

Si l’on soustrait les deux équations l’une de l’autre, les termes en puissances paires de $h$ disparaissent, car ils ont le même signe des deux côtés : $f(x)$ et le terme de courbure $\tfrac12f''h^2$. Il reste $f(x+h)-f(x-h)\approx2f'(x)\,h+\tfrac13f'''(x)\,h^3$, et la division par $2h$ donne [(11.4)](#gl-11-4). Concrètement : la courbure rend la sécante de droite plus raide et celle de gauche moins raide, et la différence centrée est la moyenne des deux.
:::

Pour une fonction quadratique, $f'''=0$, et la différence centrée est exacte pour tout $h$. Elle demande deux nouvelles évaluations de $f$, la différence avant une seule lorsque $f(x)$ est déjà connu.

::::beispiel [Exemple de calcul]
Pour $f(x)=x^3$ en $2$ avec $h=10^{-3}$, on a $1{,}999^3=7{,}988005999$ et

$$D_0f(2)=\frac{8{,}012006001-7{,}988005999}{0{,}002}=\frac{0{,}024000002}{0{,}002}=12{,}000001 .$$

L’erreur vaut $0{,}000001=\tfrac16\cdot6\cdot h^2$, six mille fois moins que pour la différence avant.
::::

⁠**En bref :** La différence centrée a une erreur de troncature d’environ $\tfrac16f'''(x)\,h^2$, parce que le terme de courbure s’élimine.

### Ce dont vous avez besoin : nombres à virgule flottante

<span class="anker" id="stufe-11-3"></span>

D’après les deux formules de l’erreur de troncature, il suffirait de choisir $h$ assez petit. Avec la calculatrice et avec tout logiciel de calcul, cela tourne mal, et la raison en est la façon dont les ordinateurs stockent les nombres.

Les ordinateurs stockent les nombres à virgule comme __nombres à virgule flottante__ : comme un nombre ayant un nombre fixe de chiffres dans le système binaire, multiplié par une puissance de deux. L’usage est la double précision selon la norme IEEE 754, avec $53$ chiffres binaires, soit environ $16$ chiffres décimaux. Le résultat de chaque opération est arrondi au nombre représentable le plus proche. L’erreur relative de cet arrondi est au plus $2^{-53}\approx1{,}1\cdot10^{-16}$. L’écart entre $1$ et le nombre représentable immédiatement supérieur est deux fois plus grand,

$$\varepsilon_{\mathrm M}=2^{-52}\approx2{,}2\cdot10^{-16};$$

ce nombre s’appelle l’__epsilon machine__, et les logiciels de calcul l’affichent sous le nom eps. En simple précision, avec $24$ chiffres binaires, soit environ $7$ chiffres décimaux, on a $\varepsilon_{\mathrm M}=2^{-23}\approx1{,}2\cdot10^{-7}$.

L’arrondi devient dangereux lorsqu’on soustrait des nombres presque égaux. Les premiers chiffres s’annulent, les erreurs d’arrondi des derniers restent, et seuls quelques chiffres du résultat sont encore exacts. C’est ce qu’on appelle l’__annulation catastrophique__. Un taux d’accroissement soustrait précisément de tels nombres l’un de l’autre, et plus $h$ est petit, plus ils se ressemblent.

::::beispiel [Exemple de calcul]
Pour $f(x)=x^3$ en $2$ et $h=10^{-8}$, on a $f(2+h)=8{,}00000012\ldots$ Les deux valeurs de la fonction valent environ $8$ et portent chacune une erreur d’arrondi pouvant atteindre environ $8\cdot1{,}1\cdot10^{-16}\approx9\cdot10^{-16}$. Leur différence vaut environ $1{,}2\cdot10^{-7}$ ; une erreur de $10^{-15}$ sur celle-ci est une erreur relative de presque $10^{-8}$. Des $16$ chiffres, seuls environ $8$ sont donc encore exacts après la soustraction, et la division par $h$ n’y change rien.
::::

⁠**En bref :** Les ordinateurs arrondissent chaque résultat à environ $16$ chiffres, $\varepsilon_{\mathrm M}=2^{-52}$ ; lors de la soustraction de nombres presque égaux, il n’en reste que peu de chiffres exacts.

### La courbe d’erreur

<span class="anker" id="stufe-11-4"></span>

Dans un taux d’accroissement, deux erreurs agissent donc en sens contraire. L’erreur de troncature diminue quand $h$ diminue. L’erreur d’arrondi augmente quand $h$ diminue : l’erreur sur la différence au numérateur reste à peu près la même, mais elle est divisée par un $h$ de plus en plus petit.

:::satz Théorème 11.4 (Erreur totale des taux d’accroissement)
<span class="anker" id="satz-11-4"></span>

Si les valeurs de la fonction sont exactes à une erreur relative d’au plus $\tfrac12\varepsilon_{\mathrm M}$ près, l’erreur totale est approximativement au plus

<span class="anker" id="gl-11-5"></span>
$$E_+(h)=\tfrac12|f''(x)|\,h+\frac{\varepsilon_{\mathrm M}|f(x)|}{h}\qquad\text{et}\qquad E_0(h)=\tfrac16|f'''(x)|\,h^2+\frac{\varepsilon_{\mathrm M}|f(x)|}{2h} \tag{11.5}$$

pour la différence avant et la différence centrée respectivement. $E_+$ est minimale en $h_+=\sqrt{2\varepsilon_{\mathrm M}|f|/|f''|}$, où elle vaut $\sqrt{2\varepsilon_{\mathrm M}|f|\,|f''|}$ ; $E_0$ est minimale en $h_0=\bigl(\tfrac32\varepsilon_{\mathrm M}|f|/|f'''|\bigr)^{1/3}$.
:::

:::herleitung Le meilleur pas
Au numérateur figurent deux valeurs de la fonction, chacune avec une erreur d’arrondi pouvant atteindre $\tfrac12\varepsilon_{\mathrm M}|f|$, soit au total jusqu’à $\varepsilon_{\mathrm M}|f|$. Pour la différence avant, cette erreur est divisée par $h$, pour la différence centrée par $2h$. S’y ajoutent les erreurs de troncature [(11.2)](#gl-11-2) et [(11.4)](#gl-11-4). Une fonction de la forme $a\,h+b/h$ avec $a,b>0$ a pour dérivée $a-b/h^2$, qui s’annule en $h=\sqrt{b/a}$ ; la valeur y est $2\sqrt{ab}$. Avec $a=\tfrac12|f''|$ et $b=\varepsilon_{\mathrm M}|f|$, cela donne $h_+$. Pour $a\,h^2+b/h$, la dérivée est $2ah-b/h^2$, qui s’annule pour $h^3=b/(2a)$ ; avec $a=\tfrac16|f'''|$ et $b=\tfrac12\varepsilon_{\mathrm M}|f|$, cela donne $h_0$.
:::

Si l’on porte l’erreur en fonction de $h$ en échelle log-log, on obtient un V (Fig. [20](#abb-20)). À droite, la courbe monte avec la pente $1$ (avant) ou $2$ (centrée), parce que l’erreur de troncature y domine. À gauche, elle descend avec la pente $-1$, parce que l’erreur d’arrondi y domine. Les points mesurés à gauche sont dispersés, car les erreurs d’arrondi sont plus ou moins grandes selon le nombre ; [(11.5)](#gl-11-5) n’indique que leur ordre de grandeur. Comme règle empirique, on choisit $h\approx\sqrt{\varepsilon_{\mathrm M}}\approx10^{-8}$ pour la différence avant et $h\approx\varepsilon_{\mathrm M}^{1/3}\approx6\cdot10^{-6}$ pour la différence centrée, chaque fois multiplié par l’ordre de grandeur de $x$ si $|x|$ est supérieur à $1$.

:::abbildung ml/k3vkurve 20
L’erreur des deux taux d’accroissement pour $f(x)=x^3$ en $2$, calculée en double précision, en fonction du pas $h$ de $10^{-15}$ à $10^{-1}$, les deux axes étant logarithmiques. À droite domine l’erreur de troncature (pente $1$ ou $2$), à gauche l’erreur d’arrondi (pente $-1$). Les courbes en tirets sont les estimations [(11.5)](#gl-11-5) ; les points les plus bas se trouvent en $h\approx10^{-8}$ (différence avant) et en $h\approx3\cdot10^{-6}$ (différence centrée).
:::

::::beispiel [Exemple de calcul]
Pour $f(x)=x^3$ en $2$, on a $|f|=8$, $|f''|=12$ et $|f'''|=6$. Le meilleur pas de la différence avant est $h_+=\sqrt{2\cdot2{,}2\cdot10^{-16}\cdot8/12}\approx1{,}7\cdot10^{-8}$, avec une erreur d’environ $\sqrt{2\cdot2{,}2\cdot10^{-16}\cdot8\cdot12}\approx2{,}1\cdot10^{-7}$ ; rapportée à $f'(2)=12$, elle correspond à environ huit chiffres exacts. Le meilleur pas de la différence centrée est $h_0=(1{,}5\cdot2{,}2\cdot10^{-16}\cdot8/6)^{1/3}\approx7{,}6\cdot10^{-6}$, avec une erreur d’environ $(7{,}6\cdot10^{-6})^2+2{,}2\cdot10^{-16}\cdot8/(2\cdot7{,}6\cdot10^{-6})\approx1{,}7\cdot10^{-10}$, soit environ onze chiffres exacts. La Fig. [20](#abb-20) confirme les deux : on a mesuré $7{,}3\cdot10^{-8}$ pour $h=10^{-8}$ et $2{,}0\cdot10^{-11}$ pour $h\approx3{,}2\cdot10^{-6}$. Avec $h=10^{-14}$, en revanche, la première décimale est déjà fausse pour les deux taux.
::::

⁠**En bref :** Un $h$ trop grand donne des erreurs de troncature, un pas trop petit, des erreurs d’arrondi ; le mieux est $h\approx10^{-8}$ pour la différence avant et $h\approx10^{-5}$ à $10^{-6}$ pour la différence centrée, qui atteint alors environ onze chiffres exacts au lieu de huit.

### La vérification du gradient

<span class="anker" id="stufe-11-5"></span>

Qui établit un gradient à la main ou le programme sous forme de pas arrière commet facilement des erreurs : un chemin oublié, une transposition manquante, un facteur faux. Un taux d’accroissement n’a besoin d’aucune démonstration, il se contente d’évaluer la fonction. En comparant les deux, on trouve de telles erreurs de façon fiable.

:::definition Définition 11.5 (Vérification du gradient)
<span class="anker" id="satz-11-5"></span>

Lors de la __vérification du gradient__, on compare un gradient calculé $\mathbf{g}_{\mathrm a}$ en un point $\mathbf{x}$ au gradient numérique $\mathbf{g}_{\mathrm n}$, dont les composantes sont des différences centrées,

<span class="anker" id="gl-11-6"></span>
$$g_{\mathrm n,j}=\frac{f(\mathbf{x}+h\,\mathbf{e}_j)-f(\mathbf{x}-h\,\mathbf{e}_j)}{2h}. \tag{11.6}$$

Pour chaque composante, on calcule alors l’__erreur relative__

<span class="anker" id="gl-11-7"></span>
$$\rho_j=\frac{|g_{\mathrm a,j}-g_{\mathrm n,j}|}{\max\bigl(|g_{\mathrm a,j}|,\,|g_{\mathrm n,j}|\bigr)}, \tag{11.7}$$

où l’on pose $\rho_j=0$ si les deux valeurs sont nulles.
:::

On compare en relatif, parce qu’une erreur absolue de $10^{-6}$ est excellente pour une dérivée de $10^{6}$, mais constitue un échec complet pour une dérivée de $10^{-6}$. Pour un calcul en double précision et un $h$ de l’ordre de $10^{-5}$, les valeurs empiriques suivantes s’appliquent : une erreur relative supérieure à $10^{-2}$ signifie presque sûrement une erreur dans la formule. Entre $10^{-2}$ et $10^{-4}$, le résultat est suspect. En dessous de $10^{-4}$, il est le plus souvent correct pour des fonctions présentant des points anguleux, et $10^{-7}$ ou moins est un bon résultat. Une vérification coûte $2n$ évaluations de $f$ ; c’est pourquoi on ne vérifie qu’en quelques points ou seulement quelques composantes. Le mode inverse sert au calcul proprement dit, le taux d’accroissement à son contrôle.

::::beispiel [Exemple de calcul 1]
Supposons que, pour $f(\mathbf{x})=x_1^2x_2+x_2^2$, quelqu’un ait établi le gradient $(2x_1x_2,\ x_1^2+x_2)^{\top}$, en oubliant un facteur $2$. Au point $(1,\,2)$, cela donne $\mathbf{g}_{\mathrm a}=(4,\,3)^{\top}$. Avec $h=0{,}001$, on a

$$\begin{aligned} g_{\mathrm n,1}&=\frac{f(1{,}001;\ 2)-f(0{,}999;\ 2)}{0{,}002}=\frac{6{,}004002-5{,}996002}{0{,}002}=4,\\ g_{\mathrm n,2}&=\frac{f(1;\ 2{,}001)-f(1;\ 1{,}999)}{0{,}002}=\frac{6{,}005001-5{,}995001}{0{,}002}=5 . \end{aligned}$$

Les différences centrées sont ici exactes, car $f$ est au plus quadratique en chaque variable prise séparément. Les erreurs relatives sont $\rho_1=0$ et $\rho_2=|3-5|/5=0{,}4$ : la deuxième composante est fausse.
::::

::::beispiel [Exemple de calcul 2]
On vérifie la formule $\sigma'(x)=\sigma(x)(1-\sigma(x))$ en $1$. Avec dix décimales, $\sigma(1)\approx0{,}7310585786$, et la formule donne $0{,}7310585786\cdot0{,}2689414214\approx0{,}1966119332$. Avec $h=0{,}01$, on a $\sigma(1{,}01)\approx0{,}7330201492$ et $\sigma(0{,}99)\approx0{,}7290879223$, donc

$$g_{\mathrm n}=\frac{0{,}7330201492-0{,}7290879223}{0{,}02}=\frac{0{,}0039322269}{0{,}02}\approx0{,}196611345 .$$

L’erreur relative vaut $\rho\approx5{,}9\cdot10^{-7}/0{,}1966\approx3{,}0\cdot10^{-6}$. Elle provient de l’erreur de troncature due au pas relativement grand et se situe bien en dessous du seuil $10^{-2}$ ; la formule est juste. En double précision avec $h=10^{-5}$, elle tombe à environ $10^{-11}$.
::::

⁠**En bref :** La vérification du gradient compare un gradient calculé, composante par composante, avec des différences centrées ; des erreurs relatives supérieures à $10^{-2}$ signalent une erreur dans la formule, des erreurs inférieures à $10^{-7}$ une formule juste.

### Points anguleux et autres pièges

<span class="anker" id="stufe-11-6"></span>

Une vérification du gradient peut donner l’alarme alors que la formule est juste, ou rester muette alors qu’elle est fausse. Les causes les plus fréquentes sont prévisibles.

La première cause, ce sont les points anguleux. En un point anguleux, comme pour $|x|$ ou $\max(x,\,0)$ en $0$, il n’y a pas de dérivée. Si un point anguleux se trouve entre $x-h$ et $x+h$, la différence centrée mesure un mélange des deux pentes à gauche et à droite, alors que la dérivée calculée n’en connaît qu’une. La deuxième cause est une précision trop faible. En simple précision, $\varepsilon_{\mathrm M}\approx1{,}2\cdot10^{-7}$ ; d’après [(11.5)](#gl-11-5), le meilleur pas de la différence centrée se situe alors autour de $10^{-2}$, et des erreurs relatives de l’ordre de $10^{-5}$ à $10^{-3}$ sont normales même avec une formule juste. La troisième est un pas trop petit, qui fait grimper l’erreur d’arrondi. La quatrième, ce sont des gradients très petits : si les deux valeurs sont presque nulles, l’erreur relative n’est guère significative, et l’on regarde en plus l’erreur absolue. Enfin, il faut vérifier en un point aléatoire, et non en un point particulier : au point $\mathbf{x}=\mathbf{0}$, de nombreux termes d’une formule s’annulent, et avec eux les erreurs que ces termes contiennent.

:::warnung Seul ce que l’on vérifie est vérifié
Une vérification du gradient réussie en un point montre que la formule y est juste, pas qu’elle l’est partout. Un terme oublié qui est nul au point vérifié passe inaperçu. Vérifiez donc en plusieurs points avec des nombres irréguliers, et vérifiez toutes les composantes qui sont calculées de manière différente.
:::

::::beispiel [Exemple de calcul]
Pour $f(x)=|x|$ en $x=10^{-6}$, la dérivée vaut $1$. Avec $h=10^{-5}$, le point anguleux en $0$ se trouve entre $x-h$ et $x+h$, et

$$D_0f(10^{-6})=\frac{|1{,}1\cdot10^{-5}|-|-0{,}9\cdot10^{-5}|}{2\cdot10^{-5}}=\frac{0{,}2\cdot10^{-5}}{2\cdot10^{-5}}=0{,}1 .$$

L’erreur relative vaut $0{,}9$, bien que la formule $f'(x)=1$ pour $x>0$ soit juste. Avec $h=10^{-7}$, le point anguleux se trouve à l’extérieur, et la différence centrée vaut exactement $1$.
::::

⁠**En bref :** Les points anguleux, la simple précision, des pas trop petits et des gradients proches de zéro faussent la vérification ; on vérifie en plusieurs points irréguliers.

:::aufgabe Exercice 39 ★ Deux taux d’accroissement
<span class="anker" id="aufg-39"></span>

Soit $f(x)=\mathrm{e}^x$ et $x=0$, donc $f'(0)=1$.

<ol class="al">

<li>

Calculez avec la calculatrice $D_+f(0)$ et $D_0f(0)$ pour $h=0{,}1$ et $h=0{,}01$.

</li>

<li>

Comparez les erreurs avec les approximations $\tfrac12f''(0)\,h$ et $\tfrac16f'''(0)\,h^2$.

</li>

</ol>

:::loesung
(a) Avec $\mathrm{e}^{0{,}1}\approx1{,}105170918$, $\mathrm{e}^{-0{,}1}\approx0{,}904837418$, $\mathrm{e}^{0{,}01}\approx1{,}010050167$ et $\mathrm{e}^{-0{,}01}\approx0{,}990049834$ :

$$\begin{aligned} h=0{,}1:&\quad D_+=\frac{1{,}105170918-1}{0{,}1}\approx1{,}05171,\\ &\quad D_0=\frac{1{,}105170918-0{,}904837418}{0{,}2}\approx1{,}001668;\\ h=0{,}01:&\quad D_+=\frac{1{,}010050167-1}{0{,}01}\approx1{,}005017,\\ &\quad D_0=\frac{1{,}010050167-0{,}990049834}{0{,}02}\approx1{,}0000167 . \end{aligned}$$

(b) Les erreurs de la différence avant sont $0{,}0517$ et $0{,}0050$, l’approximation $\tfrac12h$ prédit $0{,}05$ et $0{,}005$. Les erreurs de la différence centrée sont $0{,}00167$ et $0{,}0000167$, l’approximation $\tfrac16h^2$ prédit $0{,}00167$ et $0{,}0000167$. Un $h$ dix fois plus petit rend l’une des erreurs dix fois plus petite, l’autre cent fois plus petite.
:::
:::

:::aufgabe Exercice 40 ★★ Une vérification du gradient
<span class="anker" id="aufg-40"></span>

Pour $f(\mathbf{x})=x_1\,\mathrm{e}^{x_2}$, quelqu’un affirme que $\nabla f(\mathbf{x})=(\mathrm{e}^{x_2},\ \mathrm{e}^{x_2})^{\top}$.

<ol class="al">

<li>

Calculez au point $(2,\,0)$ le gradient numérique avec $h=0{,}01$ et les erreurs relatives des deux composantes. Quelle composante est fausse ?

</li>

<li>

Pourquoi la vérification au point $(1,\,0)$ aurait-elle été inadaptée ?

</li>

</ol>

:::loesung
(a) Par rapport à $x_1$ : $\frac{f(2{,}01;\,0)-f(1{,}99;\,0)}{0{,}02}=\frac{2{,}01-1{,}99}{0{,}02}=1$, l’affirmation donne $\mathrm{e}^0=1$, donc $\rho_1=0$. Par rapport à $x_2$ :

$$g_{\mathrm n,2}=\frac{2\,\mathrm{e}^{0{,}01}-2\,\mathrm{e}^{-0{,}01}}{0{,}02}\approx\frac{2{,}0201003-1{,}9800997}{0{,}02}\approx2{,}0000333 .$$

L’affirmation donne $1$, donc $\rho_2=|1-2{,}0000333|/2{,}0000333\approx0{,}5$. La deuxième composante est fausse ; la valeur juste est $x_1\mathrm{e}^{x_2}=2$.

(b) Au point $(1,\,0)$, on a $x_1\mathrm{e}^{x_2}=1=\mathrm{e}^{x_2}$ : la formule fausse y coïncide par hasard avec la formule juste, et la vérification n’aurait donné qu’une erreur relative d’environ $2\cdot10^{-5}$, due à l’erreur de troncature. L’erreur serait passée inaperçue.
:::
:::

:::aufgabe Exercice 41 ★★ Le meilleur pas
<span class="anker" id="aufg-41"></span>

Soit $f(x)=\mathrm{e}^x$ en $1$, donc $f=f''=f'''=\mathrm{e}$.

<ol class="al">

<li>

Calculez $h_+$, $h_0$ et les plus petites erreurs correspondantes d’après [(11.5)](#gl-11-5) en double précision.

</li>

<li>

Refaites le calcul en simple précision. Combien de chiffres exacts peut-on alors espérer au plus ?

</li>

</ol>

:::loesung
(a) Avec $|f|=|f''|=|f'''|=\mathrm{e}$ et $\varepsilon_{\mathrm M}\approx2{,}22\cdot10^{-16}$ :

$$\begin{aligned} h_+&=\sqrt{2\varepsilon_{\mathrm M}}\approx2{,}1\cdot10^{-8}, & E_+(h_+)&=\mathrm{e}\sqrt{2\varepsilon_{\mathrm M}}\approx5{,}7\cdot10^{-8},\\ h_0&=(1{,}5\,\varepsilon_{\mathrm M})^{1/3}\approx6{,}9\cdot10^{-6}, & E_0(h_0)&=\tfrac{\mathrm{e}}6h_0^2+\frac{\varepsilon_{\mathrm M}\mathrm{e}}{2h_0}\approx6{,}5\cdot10^{-11}. \end{aligned}$$

Rapportées à $f'(1)=\mathrm{e}$, ce sont des erreurs relatives d’environ $2\cdot10^{-8}$ et $2\cdot10^{-11}$, soit un peu moins de huit et un peu moins de onze chiffres exacts.

(b) Avec $\varepsilon_{\mathrm M}\approx1{,}19\cdot10^{-7}$, on a $h_+\approx4{,}9\cdot10^{-4}$, avec $E_+\approx1{,}3\cdot10^{-3}$, et $h_0\approx5{,}6\cdot10^{-3}$, avec $E_0\approx4{,}3\cdot10^{-5}$. Rapporté à $\mathrm{e}$, cela fait environ $5\cdot10^{-4}$ et $1{,}6\cdot10^{-5}$ : on peut espérer au plus environ trois et cinq chiffres exacts respectivement. C’est pourquoi une vérification du gradient en simple précision fournit, même avec une formule juste, des erreurs relatives de l’ordre de $10^{-5}$ à $10^{-3}$.
:::
:::

:::aufgabe Exercice 42 ★★★ Point anguleux dans le graphe
<span class="anker" id="aufg-42"></span>

Soit $f(\mathbf{x})=\max(x_1,\,x_2)\cdot x_3$.

<ol class="al">

<li>

Calculez en mode inverse le gradient au point $(2;\ 2{,}000001;\ 3)$.

</li>

<li>

Calculez la différence centrée par rapport à $x_1$ avec $h=10^{-5}$ et l’erreur relative. La formule est-elle fausse ?

</li>

<li>

Que fournit le mode inverse au point $(2,\,2,\,3)$, et pourquoi n’y a-t-il pas de gradient en ce point ?

</li>

</ol>

:::loesung
(a) Au point $(2;\ 2{,}000001;\ 3)$, on a $v=\max(x_1,x_2)=x_2=2{,}000001$ et $f=6{,}000003$. À rebours : $\bar f=1$, $\bar v=x_3=3$, $\bar x_3=v=2{,}000001$ ; le maximum transmet $\bar v$ à la plus grande entrée, $x_2$, donc $\bar x_2=3$ et $\bar x_1=0$. Le gradient est $(0;\ 3;\ 2{,}000001)^{\top}$.

(b) $f(2{,}00001;\ 2{,}000001;\ 3)=3\cdot2{,}00001=6{,}00003$ et $f(1{,}99999;\ 2{,}000001;\ 3)=3\cdot2{,}000001=6{,}000003$, donc

$$g_{\mathrm n,1}=\frac{6{,}00003-6{,}000003}{0{,}00002}=\frac{0{,}000027}{0{,}00002}=1{,}35$$

et $\rho_1=|0-1{,}35|/1{,}35=1$. La formule est pourtant juste. Le point anguleux en $x_1=x_2$ se trouve entre $x_1-h$ et $x_1+h$ : à droite, $f$ croît avec la pente $3$ en $x_1$, à gauche pas du tout, et la différence centrée mélange les deux.

(c) Au point $(2,\,2,\,3)$, les deux entrées du maximum sont égales. Le mode inverse transmet $\bar v=3$ à l’une des deux, selon celle que le calcul traite comme la plus grande en cas d’égalité ; il fournit donc $(3,\,0,\,2)^{\top}$ ou $(0,\,3,\,2)^{\top}$. Il n’y a pas de gradient en ce point : si l’on augmente $x_1$, $f$ croît avec la pente $3$ ; si l’on diminue $x_1$, $f$ reste inchangée. Les pentes à gauche et à droite sont différentes, comme pour $|x|$ en $0$.
:::
:::

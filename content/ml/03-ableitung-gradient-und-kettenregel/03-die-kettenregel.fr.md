---
title: La règle de dérivation en chaîne
pfad: Informatique / Apprentissage automatique / Fondements mathématiques / Dérivée, gradient et règle de dérivation en chaîne
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Chapitre 3 : Dérivée, gradient et règle de dérivation en chaîne
nachschlagen: ja
order: 15230300
summary: Beaucoup de fonctions s’obtiennent en substituant une fonction dans une autre.
tags: composée, fonction logistique
lang: fr
---

<span class="anker" id="stufe-2"></span>

:::zweck
Beaucoup de fonctions s’obtiennent en substituant une fonction dans une autre. La règle de dérivation en chaîne indique comment la dérivée d’une telle composée s’obtient à partir des dérivées de ses parties : les facteurs des différents étages se multiplient. Cela vaut pour des chaînes d’un nombre quelconque de maillons. La section se termine par la fonction logistique, dont la dérivée s’exprime à l’aide de la fonction elle-même.
:::

### Composition

<span class="anker" id="stufe-2-1"></span>

La fonction $(3x+1)^2$ se calcule en deux temps : d’abord $u=3x+1$, puis $u^2$. Beaucoup de formules sont construites ainsi, comme composition d’opérations simples. Qui reconnaît cette construction peut assembler la dérivée à partir des dérivées des différentes opérations.

:::definition Définition 2.1 (Composition)
<span class="anker" id="satz-2-1"></span>

Si $g$ et $f$ sont des fonctions et si chaque valeur $g(x)$ se trouve là où $f$ est définie, la fonction

$$(f\circ g)(x)=f\bigl(g(x)\bigr)$$

s’appelle la __composée__ de $f$ et $g$, qui se lit « $f$ rond $g$ ». La fonction $g$, appliquée en premier, s’appelle fonction intérieure, $f$ s’appelle fonction extérieure.
:::

::::beispiel [Exemple de calcul]
Pour $F(x)=(3x+1)^2$, la fonction intérieure est $g(x)=3x+1$ et la fonction extérieure $f(u)=u^2$, donc $F=f\circ g$. En $1$, on a $g(1)=4$ et $F(1)=f(4)=16$. L’ordre compte : $(g\circ f)(x)=g(f(x))=3x^2+1$ est une autre fonction, qui vaut $4$ en $1$.
::::

⁠**En bref :** Une composée $f\circ g$ applique d’abord $g$, puis $f$ ; on ne peut pas intervertir l’ordre.

### La règle de dérivation en chaîne

<span class="anker" id="stufe-2-2"></span>

Comment $F=f\circ g$ réagit-elle à une petite variation de $x$ ? On suit la variation à travers les deux étages. D’après l’approximation linéaire, le premier étage transmet une petite variation $\Delta x$ à peu près sous la forme $\Delta u\approx g'(x)\,\Delta x$. Le second étage transmet cette variation sous la forme $\Delta y\approx f'(u)\,\Delta u$. Au total, $\Delta y\approx f'(u)\,g'(x)\,\Delta x$. Comme dans un train d’engrenages à deux étages, les facteurs des étages se multiplient (Fig. [4](#abb-4)).

:::abbildung ml/k3getriebe 4
La règle de dérivation en chaîne comme train d’engrenages pour $y=(3x+1)^2$ en $1$. Les trois droites graduées ont la même échelle. Le segment $\Delta x=0{,}01$ (bleu) est étiré d’un facteur trois par le premier étage, $\Delta u=0{,}03$ (orange), puis par le second étage d’un facteur huit environ, $\Delta y=0{,}2409\approx0{,}24$ (rouge).
:::

:::satz Théorème 2.2 (Règle de dérivation en chaîne)
<span class="anker" id="satz-2-2"></span>

Si $g$ est dérivable en $x$ et si $f$ est dérivable en $g(x)$, alors $f\circ g$ est dérivable en $x$, et

<span class="anker" id="gl-2-1"></span>
$$(f\circ g)'(x)=f'\bigl(g(x)\bigr)\cdot g'(x). \tag{2.1}$$
:::

Il est important de voir où les dérivées sont évaluées : $g'$ en $x$, mais $f'$ en $u=g(x)$, c’est-à-dire là où la fonction extérieure travaille effectivement. Avec $u=g(x)$ et $y=f(u)$, on écrit souvent la règle sous la forme $\frac{\mathrm{d} y}{\mathrm{d} x}=\frac{\mathrm{d} y}{\mathrm{d} u}\cdot\frac{\mathrm{d} u}{\mathrm{d} x}$. On dirait que $\mathrm{d} u$ se simplifie. Comme moyen mnémotechnique, c’est utile ; comme justification, non, car les symboles ne sont pas des fractions, mais des limites.

:::beweis Règle de dérivation en chaîne
Soit $u=g(x)$. D’après l’approximation linéaire [(1.4)](die-ableitung.html#gl-1-4), on a $g(x+h)=u+g'(x)\,h+r_g(h)$ avec $r_g(h)/h\to0$ et $f(u+k)=f(u)+f'(u)\,k+r_f(k)$ avec $r_f(k)/k\to0$ ; on convient ici que $r_f(0)=0$. On pose $k=g(x+h)-u=g'(x)\,h+r_g(h)$. Alors

$$f\bigl(g(x+h)\bigr)-f(u)=f'(u)\,k+r_f(k)=f'(u)\,g'(x)\,h+f'(u)\,r_g(h)+r_f(k).$$

Après division par $h$, le terme du milieu tend vers $0$. Pour le dernier, on écrit $r_f(k)/h=\bigl(r_f(k)/k\bigr)\cdot(k/h)$ tant que $k\ne0$ ; le premier facteur tend vers $0$, car $k$ tend vers $0$ en même temps que $h$, et le second tend vers $g'(x)$. Si $k=0$, le terme vaut de toute façon $0$. Il reste $f'(u)\,g'(x)$.
:::

::::beispiel [Exemple de calcul]
Pour $F(x)=(3x+1)^2$, on a $g'(x)=3$ et $f'(u)=2u$. En $1$, on a $u=g(1)=4$, donc

$$F'(1)=f'(4)\cdot g'(1)=8\cdot3=24 .$$

Vérification : en développant, $F(x)=9x^2+6x+1$, donc $F'(x)=18x+6$ et $F'(1)=24$. La Fig. [4](#abb-4) montre la même chose avec des nombres : $F(1{,}01)=4{,}03^2=16{,}2409$, et l’approximation linéaire prévoit $16+24\cdot0{,}01=16{,}24$.
::::

⁠**En bref :** Dans une composée, les dérivées des étages se multiplient, chacune évaluée au point où travaille son étage : $(f\circ g)'(x)=f'(g(x))\,g'(x)$.

### Chaînes à nombreux maillons

<span class="anker" id="stufe-2-3"></span>

La plupart des calculs comportent plus de deux opérations. La règle de dérivation en chaîne peut s’appliquer de manière répétée : avec trois étages, $f_3\circ f_2\circ f_1=f_3\circ(f_2\circ f_1)$, et appliquée deux fois, [(2.1)](#gl-2-1) donne un produit de trois facteurs. Il en va de même pour un nombre quelconque d’étages.

:::satz Théorème 2.3 (Règle de dérivation en chaîne pour de nombreux maillons)
<span class="anker" id="satz-2-3"></span>

Soit $u_0=x$ et $u_k=f_k(u_{k-1})$ pour $k=1,\dots,L$, et supposons chaque fonction $f_k$ dérivable en $u_{k-1}$. Alors

<span class="anker" id="gl-2-2"></span>
$$\frac{\mathrm{d} u_L}{\mathrm{d} x}=f_L'(u_{L-1})\cdot f_{L-1}'(u_{L-2})\cdots f_1'(u_0). \tag{2.2}$$
:::

Il en découle un ordre pour le calcul. Chaque facteur a besoin de la valeur à laquelle travaille son étage. On calcule donc d’abord les valeurs intermédiaires $u_1,u_2,\dots$, comme pour l’évaluation ordinaire, et ensuite seulement les facteurs. L’ordre dans lequel on multiplie ensuite les facteurs est indifférent lorsqu’il s’agit de nombres.

::::beispiel [Exemple de calcul]
Soit $y=\dfrac1{(x^2+1)^3}$ en $x=1$. La chaîne a trois maillons :

$$u_1=x^2+1=2,\qquad u_2=u_1^3=8,\qquad y=\frac1{u_2}=\frac18 .$$

Les facteurs sont $\frac{\mathrm{d} u_1}{\mathrm{d} x}=2x=2$, $\frac{\mathrm{d} u_2}{\mathrm{d} u_1}=3u_1^2=12$ et $\frac{\mathrm{d} y}{\mathrm{d} u_2}=-\frac1{u_2^2}=-\frac1{64}$, donc

$$\frac{\mathrm{d} y}{\mathrm{d} x}=2\cdot12\cdot\Bigl(-\frac1{64}\Bigr)=-\frac{24}{64}=-0{,}375 .$$

Vérification : d’après la règle des puissances et la règle de dérivation en chaîne, $y=(x^2+1)^{-3}$ a pour dérivée $-3\,(x^2+1)^{-4}\cdot2x$, soit en $1$ : $-6/16=-0{,}375$.
::::

⁠**En bref :** Dans une longue chaîne, la dérivée est le produit des dérivées de tous les maillons ; on calcule d’abord les valeurs intermédiaires, puis les facteurs.

### La fonction logistique

<span class="anker" id="stufe-2-4"></span>

Certaines grandeurs doivent varier de façon lisse entre deux bornes, par exemple une proportion entre $0$ et $1$. Une fonction qui envoie tout nombre réel dans cet intervalle, sans saut, sans point anguleux et en étant toujours croissante, est la fonction logistique. Elle décrit aussi une croissance avec saturation : une grandeur croît d’abord de façon presque exponentielle, puis s’approche d’un plafond. Sa dérivée est un bel exemple de règle de dérivation en chaîne et a une forme remarquable.

:::definition Définition 2.4 (Fonction logistique)
<span class="anker" id="satz-2-4"></span>

La fonction

<span class="anker" id="gl-2-3"></span>
$$\sigma(x)=\frac1{1+\mathrm{e}^{-x}} \tag{2.3}$$

s’appelle __fonction logistique__.
:::

Pour $x$ grand et positif, $\mathrm{e}^{-x}$ est presque $0$ et $\sigma(x)$ presque $1$. Pour $x$ négatif et grand en valeur absolue, $\mathrm{e}^{-x}$ est énorme et $\sigma(x)$ presque $0$. En $0$, on a $\sigma(0)=\tfrac12$. De plus, $\sigma(-x)=1-\sigma(x)$, car $\frac1{1+\mathrm{e}^{x}}=\frac{\mathrm{e}^{-x}}{\mathrm{e}^{-x}+1}=1-\frac1{1+\mathrm{e}^{-x}}$ ; le graphe est donc symétrique par rapport au point $(0,\,\tfrac12)$ (Fig. [5](#abb-5)).

:::satz Théorème 2.5 (Dérivée de la fonction logistique)
<span class="anker" id="satz-2-5"></span>

On a

<span class="anker" id="gl-2-4"></span>
$$\sigma'(x)=\sigma(x)\,\bigl(1-\sigma(x)\bigr). \tag{2.4}$$

La dérivée est partout positive et au plus égale à $\tfrac14$ ; elle atteint sa plus grande valeur $\tfrac14$ en $0$.
:::

:::herleitung La dérivée de la fonction logistique
La fonction est une chaîne de trois maillons : $u_1=-x$, $u_2=1+\mathrm{e}^{u_1}$, $\sigma=1/u_2$. Les facteurs sont $-1$, $\mathrm{e}^{u_1}=\mathrm{e}^{-x}$ et $-1/u_2^2$. D’après [(2.2)](#gl-2-2), on a

$$\sigma'(x)=-\frac1{(1+\mathrm{e}^{-x})^2}\cdot\mathrm{e}^{-x}\cdot(-1)=\frac{\mathrm{e}^{-x}}{(1+\mathrm{e}^{-x})^2}=\frac1{1+\mathrm{e}^{-x}}\cdot\frac{\mathrm{e}^{-x}}{1+\mathrm{e}^{-x}} .$$

Le premier facteur est $\sigma(x)$. Le second vaut $\frac{(1+\mathrm{e}^{-x})-1}{1+\mathrm{e}^{-x}}=1-\sigma(x)$. Comme $\sigma(x)$ est compris entre $0$ et $1$, les deux facteurs sont positifs. Pour un nombre $p$ compris entre $0$ et $1$, on a $p\,(1-p)=\tfrac14-(p-\tfrac12)^2\le\tfrac14$, avec égalité exactement pour $p=\tfrac12$, donc pour $x=0$.
:::

:::abbildung ml/k3logistisch 5
La fonction logistique $\sigma$ (bleu) monte de $0$ à $1$, avec la plus forte pente en $0$. Sa dérivée (rouge) y atteint sa plus grande valeur $\tfrac14$ et devient vite petite des deux côtés. Les valeurs en $0$ et en $2$ de l’exemple de calcul sont marquées.
:::

::::beispiel [Exemple de calcul]
En $2$, on a $\mathrm{e}^{-2}\approx0{,}1353$, donc $\sigma(2)\approx1/1{,}1353\approx0{,}8808$ et

$$\sigma'(2)=\sigma(2)\,\bigl(1-\sigma(2)\bigr)\approx0{,}8808\cdot0{,}1192\approx0{,}1050 .$$

Une fois $\sigma(2)$ calculé, la dérivée ne coûte plus qu’une soustraction et une multiplication, sans nouveau calcul d’exponentielle. En $10$, on a $\sigma(10)\approx0{,}99995$ et $\sigma'(10)\approx0{,}0000454$ : loin de l’origine, la fonction est presque horizontale, et les petites variations de l’entrée n’arrivent presque plus à la sortie.
::::

⁠**En bref :** La fonction logistique $\sigma(x)=1/(1+\mathrm{e}^{-x})$ envoie de façon lisse tout nombre dans l’intervalle entre $0$ et $1$ ; sa dérivée vaut $\sigma(1-\sigma)$, au plus $\tfrac14$, et se calcule à partir de la seule valeur de la fonction.

:::aufgabe Exercice 5 ★ Courbe en cloche
<span class="anker" id="aufg-5"></span>

Soit $f(x)=\mathrm{e}^{-x^2}$.

<ol class="al">

<li>

Déterminez la fonction intérieure et la fonction extérieure, et calculez $f'(x)$.

</li>

<li>

Calculez $f'(0)$, $f'(1)$ et $f'(-1)$, et interprétez les signes sur le graphe.

</li>

</ol>

:::loesung
(a) La fonction intérieure est $u=-x^2$, avec $u'=-2x$, la fonction extérieure est $\mathrm{e}^u$, de dérivée $\mathrm{e}^u$. D’après la règle de dérivation en chaîne, $f'(x)=\mathrm{e}^{-x^2}\cdot(-2x)=-2x\,\mathrm{e}^{-x^2}$.

(b) $f'(0)=0$ : le graphe a une tangente horizontale en $0$, il y atteint son sommet. $f'(1)=-2/\mathrm{e}\approx-0{,}7358$ : à droite du sommet, il descend. $f'(-1)=2/\mathrm{e}\approx0{,}7358$ : à gauche du sommet, il monte. Comme $f(-x)=f(x)$, les pentes en $\pm1$ sont opposées.
:::
:::

:::aufgabe Exercice 6 ★★ Une chaîne de trois maillons
<span class="anker" id="aufg-6"></span>

Soit $y=\sqrt{1+x^4}$.

<ol class="al">

<li>

Décomposez la fonction en trois maillons $u_1$, $u_2$, $y$ et calculez en $x=1$ d’abord toutes les valeurs intermédiaires, puis tous les facteurs.

</li>

<li>

Calculez $\frac{\mathrm{d} y}{\mathrm{d} x}$ en $1$ comme produit des facteurs, et vérifiez avec la règle de dérivation en chaîne appliquée en une seule fois.

</li>

</ol>

:::loesung
(a) Les maillons sont $u_1=x^4$, $u_2=1+u_1$ et $y=\sqrt{u_2}$. En $1$, les valeurs intermédiaires sont $u_1=1$, $u_2=2$ et $y=\sqrt2\approx1{,}4142$. Les facteurs sont $\frac{\mathrm{d} u_1}{\mathrm{d} x}=4x^3=4$, $\frac{\mathrm{d} u_2}{\mathrm{d} u_1}=1$ et $\frac{\mathrm{d} y}{\mathrm{d} u_2}=\frac1{2\sqrt{u_2}}=\frac1{2\sqrt2}\approx0{,}3536$.

(b) Le produit vaut $4\cdot1\cdot\frac1{2\sqrt2}=\frac2{\sqrt2}=\sqrt2\approx1{,}4142$. En une seule fois : $y'=\frac1{2\sqrt{1+x^4}}\cdot4x^3$, donc $\frac4{2\sqrt2}=\sqrt2$ en $1$.
:::
:::

:::aufgabe Exercice 7 ★★ Propriétés de la fonction logistique
<span class="anker" id="aufg-7"></span>

<ol class="al">

<li>

Montrez à l’aide de [(2.4)](#gl-2-4) et de $\sigma(-x)=1-\sigma(x)$ que $\sigma'(-x)=\sigma'(x)$. Qu’est-ce que cela signifie pour le graphe de $\sigma'$ ?

</li>

<li>

Calculez $\sigma(1)$ et $\sigma'(1)$ avec quatre décimales.

</li>

<li>

Calculez la dérivée seconde $\sigma''$, exprimée à l’aide de $\sigma$, et déterminez son signe pour $x>0$ et pour $x<0$. Qu’est-ce que cela dit de la courbure du graphe de $\sigma$ ?

</li>

</ol>

:::loesung
(a) Avec $\sigma(-x)=1-\sigma(x)$, on a $\sigma'(-x)=\sigma(-x)\,\bigl(1-\sigma(-x)\bigr)=\bigl(1-\sigma(x)\bigr)\,\sigma(x)=\sigma'(x)$. Le graphe de $\sigma'$ est symétrique par rapport à l’axe vertical, comme le montre la Fig. [5](#abb-5).

(b) $\mathrm{e}^{-1}\approx0{,}3679$, donc $\sigma(1)=1/1{,}3679\approx0{,}7311$ et $\sigma'(1)\approx0{,}7311\cdot0{,}2689\approx0{,}1966$.

(c) Avec la règle du produit et la règle de dérivation en chaîne : $\sigma''=(\sigma-\sigma^2)'=\sigma'-2\sigma\sigma'=\sigma'\,(1-2\sigma)=\sigma(1-\sigma)(1-2\sigma)$. Pour $x>0$, on a $\sigma>\tfrac12$, donc $1-2\sigma<0$ et $\sigma''<0$ : le graphe s’y incurve vers le bas. Pour $x<0$, on a $\sigma''>0$, et il s’incurve vers le haut. En $0$, la courbure change de signe ; c’est là que la pente est la plus grande.
:::
:::

:::aufgabe Exercice 8 ★★★ La dérivée d’une fonction réciproque
<span class="anker" id="aufg-8"></span>

Pour $x>0$, on a $\mathrm{e}^{\ln x}=x$.

<ol class="al">

<li>

Dérivez les deux membres par rapport à $x$ avec la règle de dérivation en chaîne et déduisez-en $(\ln x)'=1/x$, en supposant que $\ln$ est dérivable.

</li>

<li>

Procédez de même avec $(\sqrt x)^2=x$ et comparez avec la règle des puissances.

</li>

<li>

La fonction réciproque de la fonction logistique est $\ell(p)=\ln\frac{p}{1-p}$ pour $0<p<1$. Vérifiez $\ell(\sigma(x))=x$ et calculez $\ell'(p)$ une fois directement et une fois à l’aide de $\sigma'$.

</li>

</ol>

:::loesung
(a) Le membre de gauche est une composée, de fonction intérieure $\ln x$ et de fonction extérieure $\mathrm{e}^u$. D’après la règle de dérivation en chaîne, sa dérivée est $\mathrm{e}^{\ln x}\cdot(\ln x)'=x\cdot(\ln x)'$. Le membre de droite a pour dérivée $1$. Donc $x\,(\ln x)'=1$ et $(\ln x)'=1/x$.

(b) De $(\sqrt x)^2=x$, on tire $2\sqrt x\cdot(\sqrt x)'=1$, donc $(\sqrt x)'=\frac1{2\sqrt x}=\tfrac12x^{-1/2}$, exactement la règle des puissances avec $n=\tfrac12$.

(c) On a $1-\sigma(x)=\frac{\mathrm{e}^{-x}}{1+\mathrm{e}^{-x}}$, donc $\frac{\sigma(x)}{1-\sigma(x)}=\frac1{\mathrm{e}^{-x}}=\mathrm{e}^x$ et $\ell(\sigma(x))=\ln\mathrm{e}^x=x$. Directement, $\ell(p)=\ln p-\ln(1-p)$ et

$$\ell'(p)=\frac1p+\frac1{1-p}=\frac{1}{p\,(1-p)} .$$

À l’aide de $\sigma'$ : en dérivant $\ell(\sigma(x))=x$, on obtient $\ell'(\sigma(x))\cdot\sigma'(x)=1$, donc $\ell'(p)=\frac1{\sigma'(x)}=\frac1{p(1-p)}$ avec $p=\sigma(x)$. Là où $\sigma$ est plate, sa fonction réciproque est raide.
:::
:::

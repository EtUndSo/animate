---
title: La dérivée
pfad: Informatique / Apprentissage automatique / Fondements mathématiques / Dérivée, gradient et règle de dérivation en chaîne
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Chapitre 3 : Dérivée, gradient et règle de dérivation en chaîne
nachschlagen: ja
order: 15230200
summary: La dérivée mesure avec quelle force une fonction d’une variable réagit à une petite modification de son entrée.
tags: sécante, taux d’accroissement, limite, dérivable, dérivée, tangente, point anguleux, approximation linéaire
lang: fr
---

<span class="anker" id="stufe-1"></span>

:::zweck
La dérivée mesure avec quelle force une fonction d’une variable réagit à une petite modification de son entrée. Cette section l’introduit comme limite de pentes, l’interprète comme la pente de la droite qui épouse le mieux la courbe et fournit les règles de calcul qui permettent de calculer des dérivées sans passer chaque fois par une limite. Elle se termine par la dérivée seconde, qui décrit comment la pente elle-même varie.
:::

### Taux de variation et taux d’accroissement

<span class="anker" id="stufe-1-1"></span>

Une fonction $f$ associe à chaque nombre $x$ un nombre $f(x)$. Si l’on augmente $x$ d’un petit pas $h$, la valeur change en général elle aussi, à savoir de $f(x+h)-f(x)$. Seule la comparaison avec $h$ dit si c’est beaucoup ou peu : une variation de la valeur de $0{,}1$ est grande si $x$ n’a augmenté que de $0{,}001$, et petite si $x$ a augmenté de $100$. On divise donc l’une des deux variations par l’autre.

Sur le graphe, c’est une pente. On trace une droite passant par les deux points $(x,\,f(x))$ et $(x+h,\,f(x+h))$ du graphe. Une telle droite passant par deux points d’une courbe s’appelle une __sécante__. Sa pente est la différence de hauteur des deux points divisée par leur écart horizontal. Elle indique de combien le graphe monte en moyenne entre les deux points.

:::definition Définition 1.1 (Taux d’accroissement)
<span class="anker" id="satz-1-1"></span>

Pour une fonction $f$, un point $x$ et un nombre $h\ne0$, on appelle

<span class="anker" id="gl-1-1"></span>
$$\frac{f(x+h)-f(x)}{h} \tag{1.1}$$

le __taux d’accroissement__ de $f$ en $x$ pour le pas $h$. C’est la pente de la sécante passant par $(x,\,f(x))$ et $(x+h,\,f(x+h))$.
:::

Le pas $h$ peut aussi être négatif ; le second point se trouve alors à gauche de $x$. Pour $h=0$, le quotient n’est pas défini, car on ne peut pas diviser par zéro.

::::beispiel [Exemple de calcul]
Soit $f(x)=x^3$ et $x=2$, donc $f(2)=8$. Pour trois pas, on a

$$\frac{3^3-8}{1}=19,\qquad \frac{2{,}5^3-8}{0{,}5}=\frac{15{,}625-8}{0{,}5}=15{,}25,\qquad \frac{2{,}1^3-8}{0{,}1}=\frac{9{,}261-8}{0{,}1}=12{,}61 .$$

Les sécantes deviennent plus plates à mesure que le second point se rapproche de $(2,\,8)$ (Fig. [1](#abb-1)). Pour un $h$ quelconque, on calcule avec $(2+h)^3=8+12h+6h^2+h^3$ :

<span class="anker" id="gl-1-2"></span>
$$\frac{(2+h)^3-8}{h}=\frac{12h+6h^2+h^3}{h}=12+6h+h^2 . \tag{1.2}$$

Avec $h=1$, $h=0{,}5$ et $h=0{,}1$, cette formule redonne $19$, $15{,}25$ et $12{,}61$. Avec $h=0{,}01$, elle donne $12{,}0601$, avec $h=-0{,}1$, elle donne $12-0{,}6+0{,}01=11{,}41$.

:::abbildung ml/k3sekante 1
Sécantes du graphe de $f(x)=x^3$ passant par le point $(2,\,8)$, de pentes $19$ pour $h=1$ (rouge) et $15{,}25$ pour $h=0{,}5$ (orange). Lorsque le pas $h$ diminue, le second point se rapproche, la sécante devient plus plate, et sa pente $12+6h+h^2$ s’approche de la pente $12$ de la tangente (en tirets).
:::
::::

⁠**En bref :** Le taux d’accroissement est la variation de la valeur de la fonction divisée par la variation de l’entrée, la pente moyenne entre deux points du graphe.

### La dérivée

<span class="anker" id="stufe-1-2"></span>

Dans l’exemple de calcul, les pentes des sécantes sont d’autant plus proches de $12$ que $|h|$ est petit, et ce des deux côtés : $12{,}61$ pour $h=0{,}1$, $11{,}41$ pour $h=-0{,}1$. Elles n’atteignent la valeur $12$ elle-même pour aucun $h\ne0$, mais elles en deviennent arbitrairement proches. C’est pourquoi on appelle $12$ la limite des pentes des sécantes. De manière générale, une grandeur qui dépend de $h$ a pour __limite__ $c$ quand $h\to0$ si elle est arbitrairement proche de $c$ dès que $h$ est suffisamment proche de $0$ sans être égal à $0$. Les $h$ positifs et négatifs comptent alors de la même façon.

:::definition Définition 1.2 (Dérivée)
<span class="anker" id="satz-1-2"></span>

Une fonction $f$ est dite __dérivable__ en $x$ si le taux d’accroissement a une limite quand $h\to0$. Cette limite

<span class="anker" id="gl-1-3"></span>
$$f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h} \tag{1.3}$$

s’appelle la __dérivée__ de $f$ en $x$. On écrit aussi $\frac{\mathrm{d} f}{\mathrm{d} x}(x)$. La droite passant par $(x,\,f(x))$ de pente $f'(x)$ s’appelle la __tangente__ au graphe.
:::

Si $f$ est dérivable en tout point, $f'$ est à son tour une fonction : elle associe à chaque $x$ la pente du graphe en ce point. On l’appelle fonction dérivée, ou tout simplement dérivée elle aussi. La notation $\frac{\mathrm{d} f}{\mathrm{d} x}$ rappelle le quotient de [(1.1)](#gl-1-1), mais elle n’est pas elle-même une fraction : c’est le symbole de la limite.

::::beispiel [Exemple de calcul 1]
D’après [(1.2)](#gl-1-2), le taux d’accroissement de $f(x)=x^3$ en $2$ vaut $12+6h+h^2$. Quand $h\to0$, $6h$ et $h^2$ deviennent arbitrairement petits, donc $f'(2)=12$. Le même calcul en un point $x$ quelconque donne, avec $(x+h)^3=x^3+3x^2h+3xh^2+h^3$, le quotient $3x^2+3xh+h^2$ et donc $f'(x)=3x^2$.
::::

Toutes les fonctions ne sont pas dérivables partout. Une exception typique est un __point anguleux__ : un point où le graphe se poursuit sans saut, mais avec à sa gauche une autre pente qu’à sa droite. Les pentes des sécantes avec $h>0$ s’y approchent de la pente de droite, celles avec $h<0$ de la pente de gauche. Comme les deux sont différentes, il n’y a pas de limite commune, donc pas de dérivée ; aucune droite n’épouse les deux côtés à la fois. L’exemple le plus connu est la fonction valeur absolue $|x|$ en $0$.

::::beispiel [Exemple de calcul 2]
La fonction valeur absolue $f(x)=|x|$ n’a pas de dérivée en $0$. Son taux d’accroissement vaut $|h|/h$, soit $1$ pour tout $h>0$ et $-1$ pour tout $h<0$. Il n’existe aucun nombre dont il s’approche des deux côtés. Le graphe présente en $0$ un point anguleux : à gauche, sa pente vaut $-1$, à droite $+1$. En tout autre point, $|x|$ est dérivable, de dérivée $1$ pour $x>0$ et $-1$ pour $x<0$.
::::

⁠**En bref :** La dérivée $f'(x)$ est la limite des pentes des sécantes, c’est-à-dire la pente de la tangente ; en un point anguleux, elle n’existe pas.

### L’approximation linéaire

<span class="anker" id="stufe-1-3"></span>

À quoi sert la tangente ? Si l’on regarde un graphe lisse à travers une loupe de plus en plus forte, on y voit de moins en moins de courbure. Sous un fort grossissement, il ne reste de la courbe qu’un morceau droit, et ce morceau se trouve sur la tangente (Fig. [2](#abb-2)). Au voisinage du point $x$, on peut donc remplacer la fonction par sa tangente. Il est beaucoup plus facile de calculer avec une droite qu’avec la fonction elle-même.

:::abbildung ml/k3lupe 2
La loupe : le graphe de $f(x)=x^3$ (bleu) et sa tangente $8+12\,(x-2)$ en $2$ (en tirets rouges) dans trois fenêtres, chacune dix fois plus étroite que la précédente. Dans la dernière fenêtre, la courbe et la tangente ne se distinguent plus.
:::

:::satz Théorème 1.3 (Approximation linéaire)
<span class="anker" id="satz-1-3"></span>

Si $f$ est dérivable en $x$, alors

<span class="anker" id="gl-1-4"></span>
$$f(x+h)=f(x)+f'(x)\,h+r(h)\qquad\text{avec}\qquad \lim_{h\to0}\frac{r(h)}{h}=0 . \tag{1.4}$$

L’expression $f(x)+f'(x)\,h$ s’appelle l’__approximation linéaire__ de $f$ en $x$, et $r(h)$ est son erreur.
:::

:::beweis Approximation linéaire
On pose $r(h)=f(x+h)-f(x)-f'(x)\,h$ ; l’égalité de gauche est alors vérifiée par construction. Pour $h\ne0$, on a

$$\frac{r(h)}{h}=\frac{f(x+h)-f(x)}{h}-f'(x),$$

et d’après [(1.3)](#gl-1-3), le premier terme tend vers $f'(x)$, la différence tend donc vers $0$.
:::

La condition $r(h)/h\to0$ en dit plus que le simple fait que l’erreur devienne petite. Après tout, $h$ lui aussi devient petit ; l’essentiel est que l’erreur disparaisse plus vite que $h$. Si l’on divise $h$ par deux, la variation $f'(x)\,h$ est divisée par deux, mais l’erreur diminue nettement plus que de moitié. C’est le sens précis de la loupe.

L’égalité [(1.4)](#gl-1-4) fournit aussi l’interprétation la plus parlante de la dérivée. Une petite variation $h$ de l’entrée arrive à la sortie à peu près sous la forme $f'(x)\,h$. La dérivée est donc le *facteur* par lequel la fonction transmet les petites variations, sa sensibilité en $x$. Un grand $|f'(x)|$ signifie que de petites variations de l’entrée suffisent à modifier fortement la valeur ; un $f'(x)$ négatif signifie que la valeur diminue quand l’entrée augmente.

::::beispiel [Exemple de calcul]
Pour $f(x)=x^3$ en $2$ et $h=0{,}01$, l’approximation linéaire donne

$$f(2{,}01)\approx8+12\cdot0{,}01=8{,}12 .$$

La valeur exacte est $f(2{,}01)=2{,}01^3=8{,}120601$. L’erreur vaut $r(0{,}01)=0{,}000601$, et d’après le calcul associé à [(1.2)](#gl-1-2), on a en général $r(h)=6h^2+h^3$. Le quotient $r(h)/h=6h+h^2$ vaut $0{,}0601$ pour $h=0{,}01$ et $0{,}006001$ pour $h=0{,}001$ : il tend vers zéro, comme l’exige le théorème.
::::

⁠**En bref :** Près de $x$, on a $f(x+h)\approx f(x)+f'(x)\,h$ ; la dérivée est le facteur par lequel les petites variations sont transmises, et l’erreur disparaît plus vite que $h$.

:::hintergrund Pourquoi la tangente est justement la meilleure droite
Toute droite passant par le point $(x,\,f(x))$ fournit une approximation $f(x+h)\approx f(x)+m\,h$ avec une certaine pente $m$. Son erreur est $f(x+h)-f(x)-m\,h$. Si on la divise par $h$, on obtient le taux d’accroissement moins $m$, et cela tend vers $f'(x)-m$ quand $h\to0$. Cette limite n’est nulle que pour $m=f'(x)$. Pour toute autre pente, l’erreur reste durablement de l’ordre de $|f'(x)-m|\cdot|h|$ ; elle ne diminue donc qu’aussi vite que $h$ lui-même. La tangente est par conséquent la seule droite passant par le point dont l’erreur disparaît plus vite que $h$. En ce sens, elle est la meilleure approximation linéaire, et c’est exactement ainsi que l’on peut aussi définir la dérivée : comme l’unique nombre $m$ pour lequel $f(x+h)-f(x)-m\,h$ tend vers zéro plus vite que $h$. Cette forme de la définition a l’avantage de se transposer telle quelle aux fonctions à plusieurs entrées, où il n’y a plus de quotient, parce qu’on ne peut pas diviser par un vecteur. La section [3](partielle-ableitungen-und-der-gradient.html#stufe-3) en fait usage.
:::

### Règles de dérivation

<span class="anker" id="stufe-1-4"></span>

Calculer chaque dérivée par la limite est fastidieux. Heureusement, quelques dérivées usuelles et quatre règles suffisent pour dériver presque toute formule construite à partir des opérations élémentaires et de fonctions connues. Le tableau [1](#tab-1) rassemble les dérivées usuelles que ce chapitre utilise.

<span class="anker" id="tab-1"></span>

**Tableau 1 :** Dérivées usuelles. La règle des puissances vaut pour tout exposant réel $n$, pour $n$ non entier seulement si $x>0$. Les angles dans $\sin$ et $\cos$ sont mesurés en radians.

| Fonction $f(x)$ | Dérivée $f'(x)$ | Exemple |
|---|---|---|
| $c$ (constante) | $0$ | $f(x)=7$ : $f'(x)=0$ |
| $x^n$ | $n\,x^{n-1}$ | $x^3\mapsto3x^2$, $\ \tfrac1x=x^{-1}\mapsto-\tfrac1{x^2}$, $\ \sqrt x=x^{1/2}\mapsto\tfrac1{2\sqrt x}$ |
| $\mathrm{e}^x$ | $\mathrm{e}^x$ | en $0$ : pente $1$ |
| $\ln x$ ($x>0$) | $\tfrac1x$ | en $1$ : pente $1$ |
| $\sin x$ | $\cos x$ | en $0$ : pente $1$ |
| $\cos x$ | $-\sin x$ | en $0$ : pente $0$ |

:::satz Théorème 1.4 (Règles de dérivation)
<span class="anker" id="satz-1-4"></span>

Si $u$ et $v$ sont dérivables en $x$ et si $c$ est un nombre, on a en ce point :

<span class="anker" id="gl-1-5"></span>
$$\begin{aligned} (u+v)'&=u'+v' &&\text{(règle de la somme)}\\ (c\,u)'&=c\,u' &&\text{(règle du facteur constant)}\\ (u\,v)'&=u'\,v+u\,v' &&\text{(règle du produit)}\\ \Bigl(\frac uv\Bigr)'&=\frac{u'\,v-u\,v'}{v^2}\quad\text{si }v(x)\ne0 &&\text{(règle du quotient)} \end{aligned} \tag{1.5}$$
:::

Les deux premières règles découlent immédiatement de la définition, car les taux d’accroissement de sommes et de multiples se décomposent de la même manière. La règle du produit est moins évidente. Une image la rend claire : on se représente $u\,v$ comme l’aire d’un rectangle de côtés $u$ et $v$. Si les côtés augmentent de $\Delta u$ et $\Delta v$, trois bandes s’ajoutent : $u\,\Delta v$, $v\,\Delta u$ et le petit carré du coin $\Delta u\,\Delta v$. Pour de petites variations, le petit carré du coin est le produit de deux petites grandeurs et disparaît plus vite que les deux bandes. Il reste $\Delta(uv)\approx v\,\Delta u+u\,\Delta v$, et en divisant par $h$, on obtient la règle du produit.

:::beweis Règle du produit et règle des puissances
Avec $\Delta u=u(x+h)-u(x)$ et $\Delta v=v(x+h)-v(x)$, on a exactement

$$u(x+h)\,v(x+h)-u(x)\,v(x)=v(x)\,\Delta u+u(x)\,\Delta v+\Delta u\,\Delta v .$$

Si l’on divise par $h$, $\Delta u/h$ tend vers $u'(x)$ et $\Delta v/h$ vers $v'(x)$. Le dernier terme vaut $(\Delta u/h)\cdot\Delta v$ ; son premier facteur tend vers $u'(x)$, le second vers $0$, car une fonction dérivable ne varie que peu pour $h$ petit. Le quotient entier tend donc vers $u'(x)\,v(x)+u(x)\,v'(x)$.

Pour la règle des puissances avec un entier naturel $n$, on développe $(x+h)^n$. D’après la formule du binôme, on a

$$(x+h)^n=x^n+n\,x^{n-1}h+(\text{termes en }h^2,h^3,\dots,h^n),$$

donc le taux d’accroissement vaut $n\,x^{n-1}$ plus des termes qui contiennent encore au moins un facteur $h$. Quand $h\to0$, il reste $n\,x^{n-1}$. La règle du quotient découle de la règle du produit, appliquée à $u=(u/v)\cdot v$.
:::

::::beispiel [Exemple de calcul]
Soit $f(x)=(x^2+1)(x-3)$ ; on cherche $f'(2)$. Avec $u=x^2+1$, $u'=2x$, $v=x-3$, $v'=1$, la règle du produit donne

$$f'(x)=2x\,(x-3)+(x^2+1)\cdot1,\qquad f'(2)=4\cdot(-1)+5\cdot1=1 .$$

Vérification : en développant, $f(x)=x^3-3x^2+x-3$, donc $f'(x)=3x^2-6x+1$ et $f'(2)=12-12+1=1$.
::::

⁠**En bref :** Avec les dérivées usuelles du tableau et les règles pour la somme, le multiple, le produit et le quotient, on dérive des formules composées sans passer par une limite.

:::hintergrund Pourquoi la fonction exponentielle est sa propre dérivée
Pour toute base $a>0$, on a $a^{x+h}-a^x=a^x\,(a^h-1)$. Le taux d’accroissement de $a^x$ est donc $a^x$ fois le taux d’accroissement de $a^x$ en $0$, soit $a^x\cdot\frac{a^h-1}{h}$ : la pente en tout point est la valeur de la fonction multipliée par la pente en $0$. Pour $a=2$, cette pente en $0$ vaut environ $0{,}693$, pour $a=3$ environ $1{,}099$. Entre les deux, il existe exactement une base pour laquelle elle vaut $1$, et cette base est le nombre d’Euler $\mathrm{e}\approx2{,}718$. Pour elle, la pente est partout égale à la valeur de la fonction. La dérivée de $\ln x$ en découle, car le logarithme annule l’effet de la fonction exponentielle : si $y=\ln x$, alors $x=\mathrm{e}^y$, et une petite variation de $y$ entraîne une variation de $x$ multipliée par $\mathrm{e}^y=x$. Inversement, une petite variation de $x$ entraîne donc une variation de $y$ multipliée par $1/x$.
:::

### La dérivée seconde et l’approximation quadratique

<span class="anker" id="stufe-1-5"></span>

La tangente donne la direction du graphe, mais pas la façon dont il s’en écarte en s’incurvant. Que la courbe s’écarte de la tangente vers le haut ou vers le bas, et de combien, dépend de la façon dont la pente elle-même varie. On mesure cette variation, là encore, par une dérivée : la dérivée de la dérivée.

:::definition Définition 1.5 (Dérivées d’ordre supérieur)
<span class="anker" id="satz-1-5"></span>

Si la fonction dérivée $f'$ est dérivable en $x$, on appelle $f''(x)=(f')'(x)$ la __dérivée seconde__ de $f$ en $x$. De même, $f'''=(f'')'$ est la dérivée troisième, et de manière générale on écrit $f^{(k)}$ pour la dérivée $k$-ième.
:::

Si $f''(x)>0$, la pente augmente en $x$ ; le graphe s’incurve vers le haut en s’écartant de la tangente et se trouve au-dessus d’elle au voisinage de $x$. Si $f''(x)<0$, il s’incurve vers le bas. La dérivée seconde mesure donc la __courbure__ du graphe, plus précisément : la vitesse à laquelle sa pente varie.

Avec la dérivée seconde, l’approximation devient plus précise. On remplace la tangente par la parabole qui a, en $x$, la même valeur, la même pente et la même dérivée seconde que $f$. Une parabole $p(h)=a+b\,h+c\,h^2$ vérifie $p(0)=a$, $p'(0)=b$ et $p''(0)=2c$. Pour que ces trois nombres correspondent à $f(x)$, $f'(x)$ et $f''(x)$, il faut $a=f(x)$, $b=f'(x)$ et $c=\tfrac12f''(x)$. C’est de là que vient le facteur $\tfrac12$.

:::satz Théorème 1.6 (Approximation quadratique)
<span class="anker" id="satz-1-6"></span>

Si $f$ est deux fois dérivable au voisinage de $x$ et si $f''$ est continue en $x$, alors

<span class="anker" id="gl-1-6"></span>
$$f(x+h)=f(x)+f'(x)\,h+\tfrac12f''(x)\,h^2+r_2(h)\qquad\text{avec}\qquad\lim_{h\to0}\frac{r_2(h)}{h^2}=0 . \tag{1.6}$$
:::

Ici, « continue » signifie que $f''$ ne varie que peu, sans saut, lorsque le point varie peu. La preuve se mène comme pour l’approximation linéaire, avec un argument de plus ; l’énoncé s’appelle formule de Taylor. L’erreur $r_2(h)$ disparaît maintenant plus vite que $h^2$, donc, pour $h$ petit, encore beaucoup plus vite que l’erreur de l’approximation linéaire.

::::beispiel [Exemple de calcul]
Pour $f(x)=x^3$, on a $f'(x)=3x^2$, $f''(x)=6x$ et $f'''(x)=6$. En $2$, on a $f''(2)=12>0$ : le graphe s’incurve vers le haut en s’écartant de la tangente, comme le montre le panneau de gauche de la Fig. [2](#abb-2). L’approximation quadratique pour $h=0{,}01$ est

$$f(2{,}01)\approx8+12\cdot0{,}01+\tfrac12\cdot12\cdot0{,}01^2=8+0{,}12+0{,}0006=8{,}1206 .$$

La valeur exacte est $8{,}120601$, l’erreur n’est plus que $0{,}000001=h^3$. La Fig. [3](#abb-3) montre la somme des trois termes.

:::abbildung ml/k3rtaylor1 3
L’approximation quadratique de $f(x)=x^3$ en $2$ pour $h=0{,}01$, comme somme de la valeur, du terme de pente et du terme de courbure.
:::
::::

⁠**En bref :** La dérivée seconde mesure la vitesse à laquelle la pente varie, c’est-à-dire la courbure ; avec elle, l’approximation devient $f(x+h)\approx f(x)+f'(x)\,h+\tfrac12f''(x)\,h^2$.

:::hintergrund Polynômes de Taylor d’ordre supérieur
On peut aller plus loin et ajuster aussi la dérivée troisième et toutes les suivantes. Le polynôme

$$f(x)+f'(x)\,h+\frac{f''(x)}{2}\,h^2+\frac{f'''(x)}{6}\,h^3+\dots+\frac{f^{(k)}(x)}{k!}\,h^k$$

s’appelle polynôme de Taylor d’ordre $k$ ; ici, $k!=1\cdot2\cdots k$. Les dénominateurs $k!$ viennent, comme le facteur $\tfrac12$, de ce que la dérivée $k$-ième de $h^k$ vaut $k!$. Pour $f(x)=x^3$, le polynôme de Taylor d’ordre trois est déjà exact : $8+12h+6h^2+h^3$ est exactement $(2+h)^3$. Pour la plupart des fonctions, l’approximation s’améliore à chaque ordre, tant que $h$ est assez petit. Pour ce chapitre, les ordres un et deux suffisent.
:::

:::aufgabe Exercice 1 ★ Sécantes et tangente
<span class="anker" id="aufg-1"></span>

Soit $f(x)=x^2$.

<ol class="al">

<li>

Calculez le taux d’accroissement en $3$ pour $h=1$, $h=0{,}1$ et $h=-0{,}1$.

</li>

<li>

Montrez que le taux d’accroissement en $3$ vaut $6+h$, et déterminez $f'(3)$.

</li>

<li>

Donnez la tangente en $3$ et calculez avec elle une valeur approchée de $3{,}02^2$. Quelle est l’erreur ?

</li>

</ol>

:::loesung
(a) Avec $f(3)=9$, on a

$$\frac{4^2-9}{1}=7,\qquad \frac{3{,}1^2-9}{0{,}1}=\frac{9{,}61-9}{0{,}1}=6{,}1,\qquad \frac{2{,}9^2-9}{-0{,}1}=\frac{8{,}41-9}{-0{,}1}=5{,}9 .$$

La sécante vers la droite est plus raide que la tangente, celle vers la gauche moins raide, parce que le graphe de la parabole est incurvé vers le haut.

(b) $(3+h)^2=9+6h+h^2$, donc le taux d’accroissement vaut $\frac{6h+h^2}{h}=6+h$. Quand $h\to0$, il tend vers $6$ des deux côtés ; on a $f'(3)=6$, ce qui concorde avec la règle $(x^2)'=2x$.

(c) La tangente est $t(x)=9+6\,(x-3)$. Elle fournit $3{,}02^2\approx9+6\cdot0{,}02=9{,}12$. La valeur exacte est $3{,}02^2=9{,}1204$. L’erreur $0{,}0004=0{,}02^2$ vaut exactement $h^2$, car $f(3+h)-9-6h=h^2$. Elle disparaît plus vite que $h$, comme le promet l’approximation linéaire.
:::
:::

:::aufgabe Exercice 2 ★ Dériver avec les règles
<span class="anker" id="aufg-2"></span>

Dérivez et évaluez au point indiqué.

<ol class="al">

<li>

$f(x)=4x^3-2x+7$ en $1$ ;

</li>

<li>

$f(x)=x^2\,\mathrm{e}^x$ en $0$ et en $1$ ;

</li>

<li>

$f(x)=\dfrac{x}{1+x^2}$ en $0$ et en $1$. Que signifie le résultat en $1$ pour le graphe ?

</li>

</ol>

:::loesung
(a) Règle de la somme et règle du facteur constant avec la règle des puissances : $f'(x)=12x^2-2$, donc $f'(1)=10$.

(b) Règle du produit avec $u=x^2$, $v=\mathrm{e}^x$ : $f'(x)=2x\,\mathrm{e}^x+x^2\,\mathrm{e}^x=(2x+x^2)\,\mathrm{e}^x$. Donc $f'(0)=0$ et $f'(1)=3\mathrm{e}\approx8{,}155$.

(c) Règle du quotient avec $u=x$, $u'=1$, $v=1+x^2$, $v'=2x$ :

$$f'(x)=\frac{1\cdot(1+x^2)-x\cdot2x}{(1+x^2)^2}=\frac{1-x^2}{(1+x^2)^2},\qquad f'(0)=1,\qquad f'(1)=0 .$$

En $1$, le graphe a une tangente horizontale. C’est là que se trouve son point le plus haut : pour tout $x$, on a $\frac{x}{1+x^2}\le\frac12$, parce que $1+x^2-2x=(x-1)^2\ge0$, et $f(1)=\tfrac12$.
:::
:::

:::aufgabe Exercice 3 ★★ Des racines à la loupe
<span class="anker" id="aufg-3"></span>

Soit $f(x)=\sqrt x$.

<ol class="al">

<li>

Calculez $f'(x)$ et $f''(x)$ avec la règle des puissances.

</li>

<li>

À l’aide de l’approximation linéaire et de l’approximation quadratique en $4$, calculez une valeur approchée de $\sqrt{4{,}1}$. Comparez les deux avec la calculatrice.

</li>

<li>

La tangente se trouve-t-elle au-dessus ou au-dessous du graphe ? Justifiez avec le signe de $f''(4)$.

</li>

</ol>

:::loesung
(a) Avec $\sqrt x=x^{1/2}$, on a $f'(x)=\tfrac12x^{-1/2}=\frac1{2\sqrt x}$ et $f''(x)=-\tfrac14x^{-3/2}$.

(b) En $4$, on a $f(4)=2$, $f'(4)=\tfrac14$ et $f''(4)=-\tfrac14\cdot\tfrac18=-\tfrac1{32}$. Avec $h=0{,}1$ :

$$\text{linéaire : }2+\tfrac14\cdot0{,}1=2{,}025,\quad \text{quadratique : }2{,}025-\tfrac12\cdot\tfrac1{32}\cdot0{,}01=2{,}025-0{,}00015625=2{,}02484375 .$$

La calculatrice donne $\sqrt{4{,}1}\approx2{,}0248457$. L’erreur de l’approximation linéaire vaut environ $1{,}5\cdot10^{-4}$, celle de l’approximation quadratique seulement environ $1{,}9\cdot10^{-6}$.

(c) Comme $f''(4)<0$, le graphe s’incurve vers le bas en s’écartant de la tangente ; la tangente se trouve au-dessus du graphe. C’est pourquoi l’approximation linéaire $2{,}025$ est trop grande.
:::
:::

:::aufgabe Exercice 4 ★★ Point anguleux ou pas
<span class="anker" id="aufg-4"></span>

<ol class="al">

<li>

Montrez à l’aide du taux d’accroissement que $g(x)=x\,|x|$ est dérivable en $0$, et déterminez $g'(0)$.

</li>

<li>

Déterminez $g'(x)$ pour $x>0$ et pour $x<0$. La fonction $g'$ a-t-elle elle-même une dérivée en $0$ ?

</li>

<li>

La fonction $m(x)=\max(x,\,0)$ renvoie $x$ si $x$ est positif, et $0$ sinon. Où est-elle dérivable, et quelles valeurs y prend sa dérivée ?

</li>

</ol>

:::loesung
(a) On a $g(0)=0$ et $\frac{g(h)-g(0)}{h}=\frac{h\,|h|}{h}=|h|$. Cela tend vers $0$ des deux côtés, donc $g'(0)=0$. La valeur absolue seule présente un point anguleux, mais le facteur $x$ aplatit les deux branches à l’origine.

(b) Pour $x>0$, on a $g(x)=x^2$ et $g'(x)=2x$ ; pour $x<0$, on a $g(x)=-x^2$ et $g'(x)=-2x$. Avec (a), on obtient $g'(x)=2|x|$ pour tout $x$. Cette fonction présente un point anguleux en $0$, son taux d’accroissement $2|h|/h$ vaut $\pm2$. La fonction $g$ est donc dérivable une fois, mais pas deux fois.

(c) Pour $x>0$, on a $m(x)=x$ avec $m'(x)=1$ ; pour $x<0$, on a $m(x)=0$ avec $m'(x)=0$. En $0$, le taux d’accroissement vaut $1$ pour $h>0$ et $0$ pour $h<0$ ; il n’y a pas de dérivée en ce point. Le graphe présente un point anguleux en $0$.
:::
:::

---
title: La règle de dérivation en chaîne pour plusieurs variables
pfad: Informatique / Apprentissage automatique / Fondements mathématiques / Dérivée, gradient et règle de dérivation en chaîne
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Chapitre 3 : Dérivée, gradient et règle de dérivation en chaîne
nachschlagen: ja
order: 15230700
summary: Les calculs à plusieurs variables sont des chaînes de fonctions à nombreuses entrées et sorties.
tags: courbe, vecteur vitesse
lang: fr
---

<span class="anker" id="stufe-6"></span>

:::zweck
Les calculs à plusieurs variables sont des chaînes de fonctions à nombreuses entrées et sorties. La règle de dérivation en chaîne s’y transpose : les matrices jacobiennes des étages se multiplient. Composante par composante, cela signifie que l’on somme sur tous les chemins par lesquels une variation va d’une entrée à la sortie. Pour le gradient d’un nombre, c’est la transposée de la matrice jacobienne qui apparaît.
:::

### La règle de dérivation en chaîne comme produit matriciel

<span class="anker" id="stufe-6-1"></span>

Supposons deux étages montés en série : $\mathbf{g}:\mathbb{R}^n\to\mathbb{R}^m$ transforme $\mathbf{x}$ en le vecteur intermédiaire $\mathbf{u}=\mathbf{g}(\mathbf{x})$, et $\mathbf f:\mathbb{R}^m\to\mathbb{R}^p$ transforme celui-ci en $\mathbf{y}=\mathbf f(\mathbf{u})$. On suit une petite variation $\Delta\mathbf{x}$ comme dans la section [2.2](die-kettenregel.html#stufe-2-2). D’après [(5.3)](die-jacobi-matrix.html#gl-5-3), le premier étage la transmet sous la forme $\Delta\mathbf{u}\approx\mathbf{J}_{\mathbf{g}}\,\Delta\mathbf{x}$, le second sous la forme $\Delta\mathbf{y}\approx\mathbf{J}_{\mathbf f}\,\Delta\mathbf{u}\approx\mathbf{J}_{\mathbf f}\,\mathbf{J}_{\mathbf{g}}\,\Delta\mathbf{x}$. Le produit de deux nombres devient le produit de deux matrices. Cela concorde avec le [chapitre 1, section 9.4](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrixprodukt.html#stufe-9-4) : deux étages linéaires successifs forment un étage linéaire dont la matrice est le produit des deux matrices.

:::satz Théorème 6.1 (Règle de dérivation en chaîne pour plusieurs variables)
<span class="anker" id="satz-6-1"></span>

Si $\mathbf{g}$ est différentiable au point $\mathbf{x}$ et si $\mathbf f$ est différentiable au point $\mathbf{g}(\mathbf{x})$, alors $\mathbf f\circ\mathbf{g}$ est différentiable au point $\mathbf{x}$, et

<span class="anker" id="gl-6-1"></span>
$$\mathbf{J}_{\mathbf f\circ\mathbf{g}}(\mathbf{x})=\mathbf{J}_{\mathbf f}\bigl(\mathbf{g}(\mathbf{x})\bigr)\,\mathbf{J}_{\mathbf{g}}(\mathbf{x}). \tag{6.1}$$
:::

Les formes concordent : à gauche figure une matrice $p\times n$, à droite une matrice $p\times m$ multipliée par une matrice $m\times n$. Le nombre commun $m$ est le nombre de variables intermédiaires. Comme pour une variable, chaque matrice jacobienne est évaluée là où travaille son étage, $\mathbf{J}_{\mathbf f}$ donc en la valeur intermédiaire $\mathbf{u}=\mathbf{g}(\mathbf{x})$. Pour des chaînes plus longues $\mathbf f_L\circ\dots\circ\mathbf f_1$, la matrice jacobienne est le produit $\mathbf{J}_{\mathbf f_L}\cdots\mathbf{J}_{\mathbf f_1}$, l’étage appliqué en dernier se trouvant tout à gauche. Contrairement à ce qui se passe avec des nombres, on n’a pas le droit d’intervertir les facteurs.

:::beweis Règle de dérivation en chaîne pour plusieurs variables
La preuve se mène comme dans la section [2.2](die-kettenregel.html#stufe-2-2), avec des longueurs au lieu de valeurs absolues. Avec $\mathbf{u}=\mathbf{g}(\mathbf{x})$ et $\mathbf{k}=\mathbf{g}(\mathbf{x}+\mathbf{h})-\mathbf{u}=\mathbf{J}_{\mathbf{g}}\mathbf{h}+\mathbf{r}_{\mathbf{g}}(\mathbf{h})$, on a

$$\mathbf f\bigl(\mathbf{g}(\mathbf{x}+\mathbf{h})\bigr)-\mathbf f(\mathbf{u})=\mathbf{J}_{\mathbf f}\,\mathbf{k}+\mathbf{r}_{\mathbf f}(\mathbf{k})=\mathbf{J}_{\mathbf f}\mathbf{J}_{\mathbf{g}}\,\mathbf{h}+\mathbf{J}_{\mathbf f}\,\mathbf{r}_{\mathbf{g}}(\mathbf{h})+\mathbf{r}_{\mathbf f}(\mathbf{k}).$$

L’erreur du milieu disparaît plus vite que $\lVert\mathbf{h}\rVert$, parce que $\mathbf{r}_{\mathbf{g}}$ le fait et que la multiplication par une matrice fixe agrandit les longueurs au plus d’un facteur fixe. La dernière disparaît plus vite que $\lVert\mathbf{k}\rVert$, et $\lVert\mathbf{k}\rVert$ est au plus un multiple fixe de $\lVert\mathbf{h}\rVert$ dès que $\mathbf{h}$ est petit. Donc $\mathbf{J}_{\mathbf f}\mathbf{J}_{\mathbf{g}}$ est la matrice de l’approximation linéaire de $\mathbf f\circ\mathbf{g}$.
:::

::::beispiel [Exemple de calcul]
Soit $\mathbf{g}$ comme dans [(5.1)](die-jacobi-matrix.html#gl-5-1) et $f(\mathbf{u})=u_1^2+3u_2$, une fonction à une seule sortie ($p=1$). Leur composée est $F(\mathbf{x})=f(\mathbf{g}(\mathbf{x}))=x_1^2x_2^2+6x_1+3x_2^2$. Au point $\mathbf{x}=(1,\,2)^{\top}$, on a $\mathbf{u}=\mathbf{g}(\mathbf{x})=(2,\,6)^{\top}$ et $\mathbf{J}_f(\mathbf{u})=(2u_1\ \ 3)=(4\ \ 3)$. D’après [(6.1)](#gl-6-1), on a

$$\mathbf{J}_F(1,2)=\begin{pmatrix}4&3\end{pmatrix}\begin{pmatrix}2&1\\2&4\end{pmatrix}=\begin{pmatrix}4\cdot2+3\cdot2&\ 4\cdot1+3\cdot4\end{pmatrix}=\begin{pmatrix}14&16\end{pmatrix}.$$

Vérification avec la fonction écrite explicitement : $\partial_1F=2x_1x_2^2+6=8+6=14$ et $\partial_2F=2x_1^2x_2+6x_2=4+12=16$.
::::

⁠**En bref :** La matrice jacobienne d’une composée est le produit des matrices jacobiennes des étages, l’étage appliqué en dernier à gauche : $\mathbf{J}_{\mathbf f\circ\mathbf{g}}=\mathbf{J}_{\mathbf f}\,\mathbf{J}_{\mathbf{g}}$.

### Somme sur tous les chemins

<span class="anker" id="stufe-6-2"></span>

Si l’on écrit le produit matriciel [(6.1)](#gl-6-1) coefficient par coefficient, on obtient une somme sur les variables intermédiaires. Pour une fonction $F=f\circ\mathbf{g}$ à une seule sortie, on a

<span class="anker" id="gl-6-2"></span>
$$\frac{\partial F}{\partial x_j}(\mathbf{x})=\sum_{i=1}^m\frac{\partial f}{\partial u_i}(\mathbf{u})\,\frac{\partial u_i}{\partial x_j}(\mathbf{x}),\qquad \mathbf{u}=\mathbf{g}(\mathbf{x}). \tag{6.2}$$

Cette somme a une signification concrète. Une variation de $x_j$ n’atteint pas $F$ directement, mais en passant par les variables intermédiaires $u_1,\dots,u_m$. Chaque variable intermédiaire est un chemin : sur le chemin passant par $u_i$, la variation est d’abord multipliée par $\partial u_i/\partial x_j$, puis par $\partial f/\partial u_i$. À la sortie, les contributions de tous les chemins arrivent et s’additionnent (Fig. [11](#abb-11)). C’est pourquoi on résume souvent la règle de dérivation en chaîne ainsi : multiplier le long d’un chemin, sommer sur tous les chemins.

:::abbildung ml/k3wege 11
La règle de dérivation en chaîne comme réseau de chemins pour $F=f\circ\mathbf{g}$ au point $(1,\,2)$. Sur chaque arête figure la dérivée locale de la cible par rapport au point de départ de l’arête. De $x_1$, deux chemins mènent à $F$, l’un par $u_1$ (bleu), l’autre par $u_2$ (orange). Le long de chaque chemin, on multiplie les facteurs, puis on additionne les deux contributions. On peut se représenter un réseau de canalisations dans lequel chaque tuyau multiplie la quantité qui le traverse par son facteur et où les débits se rejoignent à l’arrivée.
:::

::::beispiel [Exemple de calcul 1]
Pour $F=f\circ\mathbf{g}$ de la sous-section précédente, les facteurs des arêtes au point $(1,\,2)$ sont

$$\frac{\partial u_1}{\partial x_1}=x_2=2,\quad \frac{\partial u_1}{\partial x_2}=x_1=1,\quad \frac{\partial u_2}{\partial x_1}=2,\quad \frac{\partial u_2}{\partial x_2}=2x_2=4,\quad \frac{\partial f}{\partial u_1}=2u_1=4,\quad \frac{\partial f}{\partial u_2}=3 .$$

La somme sur les deux chemins donne les coefficients $14$ et $16$, comme dans le produit matriciel (Fig. [12](#abb-12)).

:::abbildung ml/k3rwege 12
Les dérivées partielles de $F=f\circ\mathbf{g}$ au point $(1,\,2)$ comme sommes sur les deux chemins passant par $u_1$ et $u_2$.
:::
::::

::::beispiel [Exemple de calcul 2]
Une entrée, deux chemins. Soit $F(x)=g_1(x)\,g_2(x)$ avec $g_1(x)=x^2$ et $g_2(x)=3x$, donc $f(\mathbf{u})=u_1u_2$. Les chemins par $u_1$ et par $u_2$ donnent

$$\frac{\mathrm{d} F}{\mathrm{d} x}=\frac{\partial f}{\partial u_1}\,g_1'(x)+\frac{\partial f}{\partial u_2}\,g_2'(x)=u_2\cdot2x+u_1\cdot3=3x\cdot2x+x^2\cdot3=9x^2 .$$

Vérification : $F(x)=3x^3$ a pour dérivée $9x^2$. Qui oublie un chemin obtient $6x^2$ ou $3x^2$. Au passage, c’est exactement la règle du produit [(1.5)](die-ableitung.html#gl-1-5) : elle est la règle de dérivation en chaîne pour deux chemins.
::::

⁠**En bref :** Composante par composante, la règle de dérivation en chaîne est une somme sur tous les chemins de l’entrée à la sortie ; le long de chaque chemin, on multiplie les dérivées locales.

:::hintergrund Pourquoi on somme sur les chemins
La raison est l’observation de la section [3.4](partielle-ableitungen-und-der-gradient.html#stufe-3-4) : pour de petites variations, les effets s’additionnent. Si l’on modifie $x_j$ de $\Delta x_j$, toutes les variables intermédiaires changent à la fois, chacune d’environ $\frac{\partial u_i}{\partial x_j}\Delta x_j$. C’est l’approximation linéaire de $f$ dans les variables $u_1,\dots,u_m$ qui dit comment ces variations simultanées agissent sur $f$ : chacune apporte $\frac{\partial f}{\partial u_i}\Delta u_i$, et les contributions s’additionnent comme si chaque variable intermédiaire avait changé seule. La somme sur les chemins est donc la somme de ces contributions individuelles. Pour des chaînes plus longues, cela se poursuit : un chemin traverse alors plusieurs variables intermédiaires l’une après l’autre, on multiplie le long du chemin tous les facteurs des arêtes, et à la fin on somme sur tous les chemins de l’entrée à la sortie. Le nombre de chemins peut alors croître très vite ; la section [10](automatische-differentiation.html#stufe-10) montre comment les regrouper habilement.
:::

### Le gradient d’une composée

<span class="anker" id="stufe-6-3"></span>

Pour une fonction $F=f\circ\mathbf{g}$ à une seule sortie, la matrice jacobienne est le gradient écrit en ligne. Si l’on veut le gradient en colonne, comme ce chapitre l’a convenu, il faut transposer la règle de dérivation en chaîne.

:::satz Théorème 6.2 (Gradient d’une composée)
<span class="anker" id="satz-6-2"></span>

Si $\mathbf{g}:\mathbb{R}^n\to\mathbb{R}^m$ est différentiable au point $\mathbf{x}$ et si $f:\mathbb{R}^m\to\mathbb{R}$ est différentiable au point $\mathbf{u}=\mathbf{g}(\mathbf{x})$, alors

<span class="anker" id="gl-6-3"></span>
$$\nabla(f\circ\mathbf{g})(\mathbf{x})=\mathbf{J}_{\mathbf{g}}(\mathbf{x})^{\top}\,\nabla f(\mathbf{u}). \tag{6.3}$$
:::

:::beweis Gradient d’une composée
D’après [(6.1)](#gl-6-1), on a $\nabla(f\circ\mathbf{g})(\mathbf{x})^{\top}=\mathbf{J}_{f\circ\mathbf{g}}(\mathbf{x})=\mathbf{J}_f(\mathbf{u})\,\mathbf{J}_{\mathbf{g}}(\mathbf{x})=\nabla f(\mathbf{u})^{\top}\,\mathbf{J}_{\mathbf{g}}(\mathbf{x})$. En transposant les deux membres avec la règle $(\mathbf{A}\mathbf{B})^{\top}=\mathbf{B}^{\top}\mathbf{A}^{\top}$ du [chapitre 1, section 10.1](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/transponierte-symmetrie-und-gram-matrix.html#stufe-10-1), on obtient l’énoncé.
:::

La transposée n’est que de la comptabilité : elle apparaît parce que le gradient s’écrit en colonne, alors que les lignes de la matrice jacobienne correspondent aux sorties. Sur le fond, [(6.3)](#gl-6-3) dit la même chose que [(6.2)](#gl-6-2) : la composante $j$ de $\mathbf{J}_{\mathbf{g}}^{\top}\nabla f$ est la colonne $j$ de $\mathbf{J}_{\mathbf{g}}$ multipliée par $\nabla f$, donc la somme sur les chemins partant de $x_j$. Si la fonction intérieure est linéaire, $\mathbf{g}(\mathbf{x})=\mathbf{A}\mathbf{x}$, on obtient d’après la section [5.4](die-jacobi-matrix.html#stufe-5-4) la règle $\nabla_{\mathbf{x}}f(\mathbf{A}\mathbf{x})=\mathbf{A}^{\top}\,\nabla f(\mathbf{A}\mathbf{x})$. L’indice $\mathbf{x}$ sur le nabla indique par rapport à quelle variable le gradient est formé.

::::beispiel [Exemple de calcul]
Avec $\mathbf{J}_{\mathbf{g}}(1,2)$ et $\nabla f(\mathbf{u})=(4,\,3)^{\top}$ de l’exemple associé à [(6.1)](#gl-6-1), on a

$$\nabla F(1,2)=\begin{pmatrix}2&1\\2&4\end{pmatrix}^{\top}\begin{pmatrix}4\\3\end{pmatrix}=\begin{pmatrix}2&2\\1&4\end{pmatrix}\begin{pmatrix}4\\3\end{pmatrix}=\begin{pmatrix}8+6\\4+12\end{pmatrix}=\begin{pmatrix}14\\16\end{pmatrix}.$$

Sans transposer, on obtiendrait $\mathbf{J}_{\mathbf{g}}\,\nabla f=(8+3;\ 8+12)^{\top}=(11,\,20)^{\top}$, ce qui est faux.
::::

:::warnung Ne pas oublier la transposée
Si la matrice jacobienne de la fonction intérieure est symétrique, un oubli de la transposition passe inaperçu. Vérifiez donc une formule de gradient que vous avez établie vous-même sur un exemple dont la matrice jacobienne n’est pas symétrique. Si $\mathbf{J}_{\mathbf{g}}$ n’a pas autant de lignes que de colonnes, un coup d’œil sur les formes trahit l’erreur immédiatement : $\nabla f$ a $m$ coefficients, $\mathbf{J}_{\mathbf{g}}^{\top}$ a $m$ colonnes, et seul $\mathbf{J}_{\mathbf{g}}^{\top}\nabla f$ donne un vecteur à $n$ coefficients.
:::

⁠**En bref :** Le gradient d’une composée est la transposée de la matrice jacobienne de la fonction intérieure multipliée par le gradient de la fonction extérieure : $\nabla(f\circ\mathbf{g})=\mathbf{J}_{\mathbf{g}}^{\top}\nabla f$.

### Dérivée le long d’une courbe

<span class="anker" id="stufe-6-4"></span>

Une promenade sur la carte est une courbe : à chaque instant $t$, on se trouve en un lieu $\boldsymbol{\gamma}(t)\in\mathbb{R}^d$. À quelle vitesse l’altitude $f(\boldsymbol{\gamma}(t))$ change-t-elle en chemin ? C’est un cas particulier de la règle de dérivation en chaîne avec une seule variable d’entrée $t$.

:::definition Définition 6.3 (Courbe et vitesse)
<span class="anker" id="satz-6-3"></span>

Une __courbe__ est une fonction $\boldsymbol{\gamma}:\mathbb{R}\to\mathbb{R}^d$, $t\mapsto\boldsymbol{\gamma}(t)=(\gamma_1(t),\dots,\gamma_d(t))^{\top}$. Sa dérivée $\boldsymbol{\gamma}'(t)=(\gamma_1'(t),\dots,\gamma_d'(t))^{\top}$ s’appelle le __vecteur vitesse__.
:::

Le vecteur vitesse est la matrice jacobienne de $\boldsymbol{\gamma}$, une matrice $d\times1$. Il pointe dans la direction dans laquelle on se déplace à cet instant, et sa longueur est la vitesse. D’après [(6.1)](#gl-6-1) avec $n=1$, on a, pour $f$ différentiable,

<span class="anker" id="gl-6-4"></span>
$$\frac{\mathrm{d}}{\mathrm{d} t}f\bigl(\boldsymbol{\gamma}(t)\bigr)=\nabla f\bigl(\boldsymbol{\gamma}(t)\bigr)^{\top}\boldsymbol{\gamma}'(t). \tag{6.4}$$

Pour une droite $\boldsymbol{\gamma}(t)=\mathbf{x}+t\,\mathbf{h}$, on a $\boldsymbol{\gamma}'=\mathbf{h}$ et le taux de variation $\nabla f(\mathbf{x})^{\top}\mathbf{h}$ ; si $\mathbf{h}$ est de longueur $1$, c’est la dérivée directionnelle de la section [4.1](richtungsableitung-und-steilster-anstieg.html#stufe-4-1). Si une courbe reste entièrement dans une ligne de niveau, $f(\boldsymbol{\gamma}(t))$ est constant, le membre de gauche est donc nul : le gradient est perpendiculaire à tout vecteur vitesse dans la ligne de niveau. C’est le théorème de la section [4.3](richtungsableitung-und-steilster-anstieg.html#stufe-4-3), désormais justifié par la règle de dérivation en chaîne.

::::beispiel [Exemple de calcul]
Soit $f(\mathbf{x})=x_1^2x_2+x_2^2$ et $\boldsymbol{\gamma}(t)=(1+t,\ 2+2t)^{\top}$, une droite passant par $(1,\,2)$ avec $\boldsymbol{\gamma}'(t)=(1,\,2)^{\top}$. En $t=0$, on a

$$\frac{\mathrm{d}}{\mathrm{d} t}f\bigl(\boldsymbol{\gamma}(t)\bigr)\Big|_{t=0}=\begin{pmatrix}4&5\end{pmatrix}\begin{pmatrix}1\\2\end{pmatrix}=4+10=14 .$$

Vérification : $f(\boldsymbol{\gamma}(t))=(1+t)^2(2+2t)+(2+2t)^2=2\,(1+t)^3+4\,(1+t)^2$ a pour dérivée $6+8=14$ en $t=0$.
::::

⁠**En bref :** Le long d’une courbe, $f$ varie avec le taux $\nabla f^{\top}\boldsymbol{\gamma}'$ ; dans une ligne de niveau, ce taux est nul.

:::aufgabe Exercice 20 ★ Règle de dérivation en chaîne avec des matrices jacobiennes
<span class="anker" id="aufg-20"></span>

Soit $\mathbf{g}(\mathbf{x})=(x_1+x_2,\ x_1x_2)^{\top}$ et $f(\mathbf{u})=u_1^2-u_2$.

<ol class="al">

<li>

Calculez au point $\mathbf{x}=(1,\,3)^{\top}$ la valeur intermédiaire $\mathbf{u}$, la matrice jacobienne $\mathbf{J}_{\mathbf{g}}(\mathbf{x})$ et $\nabla f(\mathbf{u})$.

</li>

<li>

Calculez $\nabla(f\circ\mathbf{g})(\mathbf{x})$ avec [(6.3)](#gl-6-3) et vérifiez avec la fonction écrite explicitement. Qu’obtiendrait-on sans transposer ?

</li>

</ol>

:::loesung
(a) $\mathbf{u}=\mathbf{g}(1,3)=(4,\,3)^{\top}$. La matrice jacobienne est $\mathbf{J}_{\mathbf{g}}(\mathbf{x})=\bigl(\begin{smallmatrix}1&1\\x_2&x_1\end{smallmatrix}\bigr)$, donc $\bigl(\begin{smallmatrix}1&1\\3&1\end{smallmatrix}\bigr)$ au point $(1,\,3)$. Le gradient de la fonction extérieure est $\nabla f(\mathbf{u})=(2u_1,\,-1)^{\top}=(8,\,-1)^{\top}$.

(b) D’après [(6.3)](#gl-6-3) :

$$\nabla(f\circ\mathbf{g})(1,3)=\begin{pmatrix}1&3\\1&1\end{pmatrix}\begin{pmatrix}8\\-1\end{pmatrix}=\begin{pmatrix}8-3\\8-1\end{pmatrix}=\begin{pmatrix}5\\7\end{pmatrix}.$$

Vérification : $F(\mathbf{x})=(x_1+x_2)^2-x_1x_2=x_1^2+x_1x_2+x_2^2$ a pour dérivées partielles $2x_1+x_2=5$ et $x_1+2x_2=7$. Sans transposer, on obtiendrait $\mathbf{J}_{\mathbf{g}}\nabla f=(8-1;\ 24-1)^{\top}=(7,\,23)^{\top}$, c’est-à-dire un résultat faux.
:::
:::

:::aufgabe Exercice 21 ★★ Trois chemins
<span class="anker" id="aufg-21"></span>

Soit $F(x)=g_1(x)\,g_2(x)\,g_3(x)$ avec $g_1(x)=x$, $g_2(x)=x^2$ et $g_3(x)=x^3$.

<ol class="al">

<li>

Dessinez le réseau de chemins qui va de $x$ à $F=u_1u_2u_3$ en passant par $u_1,u_2,u_3$, et écrivez sur chaque arête son facteur.

</li>

<li>

Calculez $F'(x)$ comme somme sur les trois chemins et comparez avec la dérivée de $x^6$.

</li>

</ol>

:::loesung
(a) De $x$ partent trois arêtes vers $u_1$, $u_2$, $u_3$, avec les facteurs $1$, $2x$ et $3x^2$. De chaque $u_i$ part une arête vers $F=u_1u_2u_3$ ; son facteur est le produit des deux autres : $u_2u_3=x^5$, $u_1u_3=x^4$ et $u_1u_2=x^3$.

(b) En sommant sur les trois chemins :

$$F'(x)=x^5\cdot1+x^4\cdot2x+x^3\cdot3x^2=x^5+2x^5+3x^5=6x^5 .$$

C’est la dérivée de $F(x)=x^6$. Le chemin qui passe par $u_k$ apporte $k\,x^5$, parce que $g_k=x^k$ a pour dérivée $k\,x^{k-1}$ et que les deux autres facteurs donnent ensemble $x^{6-k}$. La règle du produit pour trois facteurs est donc la somme sur trois chemins.
:::
:::

:::aufgabe Exercice 22 ★★ Courbe dans la ligne de niveau
<span class="anker" id="aufg-22"></span>

Soit $f(\mathbf{x})=x_1^2+4x_2^2$ et $\boldsymbol{\gamma}(t)=\bigl(\sqrt5\cos t,\ \tfrac{\sqrt5}2\sin t\bigr)^{\top}$.

<ol class="al">

<li>

Montrez que $\boldsymbol{\gamma}$ reste entièrement dans la ligne de niveau $f=5$.

</li>

<li>

Déterminez $t$ tel que $\boldsymbol{\gamma}(t)=(1,\,1)^{\top}$, calculez-y $\boldsymbol{\gamma}'(t)$ et vérifiez que $\nabla f^{\top}\boldsymbol{\gamma}'=0$. Comparez la direction avec le vecteur $\mathbf{t}$ de la section [4.3](richtungsableitung-und-steilster-anstieg.html#stufe-4-3).

</li>

<li>

Justifiez de manière générale à l’aide de [(6.4)](#gl-6-4) : si une courbe dérivable reste dans un ensemble de niveau de $f$, alors $\nabla f$ est perpendiculaire à son vecteur vitesse.

</li>

</ol>

:::loesung
(a) $f(\boldsymbol{\gamma}(t))=5\cos^2t+4\cdot\tfrac54\sin^2t=5\,(\cos^2t+\sin^2t)=5$ pour tout $t$.

(b) De $\sqrt5\cos t=1$ et $\tfrac{\sqrt5}2\sin t=1$, on tire $\cos t=1/\sqrt5$ et $\sin t=2/\sqrt5$, donc $t\approx1{,}107$. En ce point,

$$\boldsymbol{\gamma}'(t)=\bigl(-\sqrt5\sin t,\ \tfrac{\sqrt5}2\cos t\bigr)^{\top}=\bigl(-2,\ \tfrac12\bigr)^{\top},\qquad \nabla f(1,1)^{\top}\boldsymbol{\gamma}'=2\cdot(-2)+8\cdot\tfrac12=0 .$$

Le vecteur vitesse est $-\tfrac12\,(4,\,-1)^{\top}$, donc parallèle au vecteur $\mathbf{t}$ de la section [4.3](richtungsableitung-und-steilster-anstieg.html#stufe-4-3).

(c) Si $\boldsymbol{\gamma}$ reste dans l’ensemble de niveau de valeur $c$, alors $f(\boldsymbol{\gamma}(t))=c$ pour tout $t$, et la dérivée par rapport à $t$ est nulle. D’après [(6.4)](#gl-6-4), cette dérivée vaut $\nabla f(\boldsymbol{\gamma}(t))^{\top}\boldsymbol{\gamma}'(t)$. Le gradient est donc perpendiculaire à tout vecteur vitesse d’une courbe située dans l’ensemble de niveau.
:::
:::

:::aufgabe Exercice 23 ★★★ Une chaîne de trois étages
<span class="anker" id="aufg-23"></span>

Soit $F(\mathbf{x})=\sum_{i=1}^2(\mathbf{A}\mathbf{x})_i^2$ avec $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\0&1\end{smallmatrix}\bigr)$. Le calcul se compose de trois étages : $\mathbf{u}=\mathbf{A}\mathbf{x}$, puis $v_i=u_i^2$ pour chaque composante, puis $F=v_1+v_2$.

<ol class="al">

<li>

Donnez les trois matrices jacobiennes au point $\mathbf{x}=(2,\,1)^{\top}$ et calculez $\mathbf{J}_F$ comme leur produit.

</li>

<li>

Montrez de manière générale que $\nabla F(\mathbf{x})=2\mathbf{A}^{\top}\mathbf{A}\mathbf{x}$ et vérifiez le résultat de (a).

</li>

<li>

Calculez le produit de (a) une fois en commençant par la gauche et une fois en commençant par la droite. Quel ordre demande le moins de multiplications lorsque $\mathbf{A}$ est une matrice $n\times n$ ?

</li>

</ol>

:::loesung
(a) Au point $(2,\,1)$, on a $\mathbf{u}=\mathbf{A}\mathbf{x}=(4,\,1)^{\top}$, $\mathbf{v}=(16,\,1)^{\top}$ et $F=17$. Les matrices jacobiennes sont $\mathbf{J}_1=\mathbf{A}$, $\mathbf{J}_2=\operatorname{diag}(2u_1;\,2u_2)=\operatorname{diag}(8;\,2)$ et $\mathbf{J}_3=(1\ \ 1)$. Leur produit vaut

$$\mathbf{J}_F=(1\ \ 1)\,\operatorname{diag}(8;\,2)\,\begin{pmatrix}1&2\\0&1\end{pmatrix}=(8\ \ 2)\begin{pmatrix}1&2\\0&1\end{pmatrix}=(8\ \ 18).$$

(b) Après transposition, $\nabla F=\mathbf{A}^{\top}\,\operatorname{diag}(2\mathbf{u})\,\mathbf{1}=\mathbf{A}^{\top}\,2\mathbf{u}=2\mathbf{A}^{\top}\mathbf{A}\mathbf{x}$. Avec $\mathbf{A}^{\top}\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\2&5\end{smallmatrix}\bigr)$, on a $2\mathbf{A}^{\top}\mathbf{A}\mathbf{x}=2\,(4,\,9)^{\top}=(8,\,18)^{\top}$, comme en (a). Vérification : $F=(x_1+2x_2)^2+x_2^2$ a pour dérivées partielles $2\cdot4=8$ et $4\cdot4+2=18$.

(c) En commençant par la gauche : $(1\ \ 1)\,\operatorname{diag}(8;2)$ est une ligne, qui demande $n$ multiplications, et la ligne fois $\mathbf{A}$ en demande $n^2$. En commençant par la droite : $\operatorname{diag}(8;2)\,\mathbf{A}$ demande $n^2$ multiplications, et la ligne fois le résultat encore $n^2$. Par la gauche, il en faut donc environ $n^2$, par la droite environ $2n^2$. Si la matrice du milieu n’était pas diagonale, mais pleine, le produit matriciel coûterait même environ $n^3$ en commençant par la droite. Par la gauche, en partant du résultat, on n’obtient jamais que des lignes.
:::
:::

---
title: Indépendance, base et rang
pfad: Informatique / Apprentissage automatique / Fondements mathématiques / Vecteurs et matrices
adresse: informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen
knoten: Chapitre 1 : Vecteurs et matrices
nachschlagen: ja
order: 15211400
summary: Certains vecteurs d’une liste n’apportent rien de nouveau, parce qu’on peut les composer à partir des autres.
tags: sous-espace engendré, linéairement indépendants, linéairement dépendants, base, dimension, base canonique, rang, rang maximal
lang: fr
---

<span class="anker" id="stufe-13"></span>

:::zweck
Certains vecteurs d’une liste n’apportent rien de nouveau, parce qu’on peut les composer à partir des autres. Cette section mesure combien de directions réellement différentes une matrice contient et montre ce que cela signifie pour les données lorsque des caractéristiques portent deux fois la même information.
:::

### Le sous-espace engendré

<span class="anker" id="stufe-13-1"></span>

L’espace des colonnes d’une matrice est l’ensemble de toutes les combinaisons linéaires de ses colonnes. La même construction donne un ensemble pour toute liste de vecteurs, et celui-ci reçoit un nom propre (Fig. [39](#abb-39)).

:::abbildung ml/k1spann 39
Le sous-espace engendré (en bleu) par trois listes de vecteurs du plan, à l’échelle $1:2$. (a) Un vecteur engendre une droite passant par l’origine. (b) Un deuxième vecteur sur la même droite ne change rien. (c) Deux vecteurs de directions différentes engendrent le plan tout entier.
:::

:::definition Définition 13.1 (Sous-espace engendré)
<span class="anker" id="satz-13-1"></span>

Le __sous-espace engendré__ par les vecteurs $\mathbf{v}_1,\dots,\mathbf{v}_k\in\mathbb{R}^d$ est l’ensemble de toutes leurs combinaisons linéaires :

<span class="anker" id="gl-13-1"></span>
$$\operatorname{span}\{\mathbf{v}_1,\dots,\mathbf{v}_k\}=\Bigl\{\sum_{l=1}^kc_l\,\mathbf{v}_l\ :\ c_1,\dots,c_k\in\mathbb{R}\Bigr\}. \tag{13.1}$$
:::

L’espace des colonnes d’une matrice est donc le sous-espace engendré par ses colonnes. Si deux vecteurs appartiennent au sous-espace engendré, toute combinaison linéaire de ceux-ci y appartient aussi ; on n’en sort jamais en additionnant et en multipliant par des nombres.

::::beispiel [Exemple de calcul]
$\operatorname{span}\{(1,\,2)^{\top}\}$ est la droite de tous les multiples $c\,(1,\,2)^{\top}$. Le sous-espace engendré par $(1,\,2)^{\top}$ et $(2,\,4)^{\top}$ est la même droite, car $(2,\,4)^{\top}=2\,(1,\,2)^{\top}$. Le sous-espace engendré par $(1,\,0)^{\top}$ et $(1,\,1)^{\top}$ est le plan tout entier : tout vecteur $(y_1,\,y_2)^{\top}$ vaut $(y_1-y_2)\,(1,\,0)^{\top}+y_2\,(1,\,1)^{\top}$. Dans $\mathbb{R}^3$, $\operatorname{span}\{\mathbf{e}_1,\mathbf{e}_2\}$ est le plan de tous les vecteurs tels que $x_3=0$.
::::

⁠**En bref :** Le sous-espace engendré par une liste de vecteurs est tout ce que l’on peut obtenir par combinaison linéaire de ces vecteurs.

### Indépendance linéaire

<span class="anker" id="stufe-13-2"></span>

Dans la Fig. [39](#abb-39) (b), le deuxième vecteur n’apporte rien de nouveau : il appartient déjà au sous-espace engendré par le premier. Un jeu de données peut présenter la même faiblesse. S’il contient le nombre de chambres, le nombre de salons et le nombre total de pièces, la troisième colonne est la somme des deux premières et ne porte aucune information propre. Il faut un mot pour dire que, dans une liste de vecteurs, rien n’est superflu.

:::definition Définition 13.2 (Indépendance linéaire)
<span class="anker" id="satz-13-2"></span>

Des vecteurs $\mathbf{v}_1,\dots,\mathbf{v}_k$ sont dits __linéairement indépendants__ si

<span class="anker" id="gl-13-2"></span>
$$c_1\mathbf{v}_1+c_2\mathbf{v}_2+\dots+c_k\mathbf{v}_k=\mathbf{0} \tag{13.2}$$

n’est vérifié que pour $c_1=c_2=\dots=c_k=0$. Sinon, ils sont dits __linéairement dépendants__.
:::

Linéairement dépendants signifie, de façon équivalente : au moins l’un des vecteurs est une combinaison linéaire des autres. En effet, si [(13.2)](#gl-13-2) est vérifié avec un coefficient $c_l\ne0$, on peut isoler $\mathbf{v}_l$ : $\mathbf{v}_l=-\sum_{l'\ne l}(c_{l'}/c_l)\,\mathbf{v}_{l'}$. Inversement, une telle écriture donne immédiatement une combinaison avec le coefficient $-1$ devant $\mathbf{v}_l$.

::::beispiel [Exemple de calcul]
$(1,\,2)^{\top}$ et $(2,\,4)^{\top}$ sont linéairement dépendants : $2\,(1,\,2)^{\top}-(2,\,4)^{\top}=\mathbf{0}$. Les vecteurs $(1,\,0)^{\top}$ et $(1,\,1)^{\top}$ sont linéairement indépendants : de $c_1(1,\,0)^{\top}+c_2(1,\,1)^{\top}=(c_1+c_2,\ c_2)^{\top}=\mathbf{0}$, on tire d’abord $c_2=0$, puis $c_1=0$. Les trois vecteurs $(1,\,0,\,1)^{\top}$, $(0,\,1,\,1)^{\top}$ et $(1,\,1,\,2)^{\top}$ sont linéairement dépendants, car le troisième est la somme des deux premiers.
::::

⁠**En bref :** Linéairement indépendants signifie qu’aucun des vecteurs ne peut être obtenu par combinaison des autres : il n’y a pas de redondance.

### Base et dimension

<span class="anker" id="stufe-13-3"></span>

Si l’on veut décrire un sous-espace engendré de la façon la plus concise possible, on prend aussi peu de vecteurs que nécessaire, mais assez pour tout atteindre. Une telle liste est comme un système de coordonnées : chaque vecteur du sous-espace engendré s’écrit alors d’une seule façon à l’aide de cette liste.

:::definition Définition 13.3 (Base, dimension)
<span class="anker" id="satz-13-3"></span>

Une liste de vecteurs linéairement indépendants dont le sous-espace engendré est un ensemble $\mathcal S$ s’appelle une __base__ de $\mathcal S$. Le nombre de vecteurs d’une base s’appelle la __dimension__ de $\mathcal S$, notée $\dim\mathcal S$.
:::

Un ensemble $\mathcal S$ a de nombreuses bases différentes, mais toutes se composent du même nombre de vecteurs ; c’est un théorème d’algèbre linéaire, sur lequel repose la définition de la dimension. Les vecteurs unitaires $\mathbf{e}_1,\dots,\mathbf{e}_d$ forment une base de $\mathbb{R}^d$, la __base canonique__ ; c’est pourquoi $\dim\mathbb{R}^d=d$.

:::satz Théorème 13.4 (Coordonnées uniques)
<span class="anker" id="satz-13-4"></span>

Si $\mathbf{v}_1,\dots,\mathbf{v}_k$ est une base de $\mathcal S$, tout vecteur $\mathbf{x}\in\mathcal S$ s’écrit d’une seule façon sous la forme $\mathbf{x}=\sum_lc_l\mathbf{v}_l$.
:::

:::beweis Coordonnées uniques
Il existe au moins une écriture, parce que la base engendre $\mathcal S$. S’il y en avait deux, $\sum_lc_l\mathbf{v}_l=\sum_lc_l'\mathbf{v}_l$, leur différence serait $\sum_l(c_l-c_l')\mathbf{v}_l=\mathbf{0}$. En raison de l’indépendance linéaire, toutes les différences vérifient alors $c_l-c_l'=0$.
:::

::::beispiel [Exemple de calcul]
$(1,\,0)^{\top}$ et $(1,\,1)^{\top}$ forment une base de $\mathbb{R}^2$ : ils sont linéairement indépendants et engendrent le plan. Dans cette base, le vecteur $(3,\,2)^{\top}$ a pour coordonnées $1$ et $2$, car $(3,\,2)^{\top}=1\cdot(1,\,0)^{\top}+2\cdot(1,\,1)^{\top}$. La droite $\operatorname{span}\{(0,\,1)^{\top}\}$ est de dimension $1$, bien que ses vecteurs aient deux composantes.
::::

⁠**En bref :** Une base est une liste de vecteurs indépendants qui engendre tout ; sa longueur est la dimension.

### Le rang d’une matrice

<span class="anker" id="stufe-13-4"></span>

Une matrice à $n$ colonnes peut contenir moins de $n$ directions réellement différentes. Le nombre de directions qui restent lorsqu’on supprime tout ce qui est superflu indique ce qu’une matrice accomplit réellement.

:::definition Définition 13.5 (Rang)
<span class="anker" id="satz-13-5"></span>

Le __rang__ $\operatorname{rg}\mathbf{A}$ d’une matrice $\mathbf{A}$ est le plus grand nombre de colonnes linéairement indépendantes de $\mathbf{A}$. Il est égal à la dimension de son espace des colonnes.
:::

:::satz Théorème 13.6 (Rang des colonnes égal au rang des lignes)
<span class="anker" id="satz-13-6"></span>

Le plus grand nombre de colonnes linéairement indépendantes d’une matrice est égal au plus grand nombre de lignes linéairement indépendantes. En particulier, $\operatorname{rg}\mathbf{A}=\operatorname{rg}\mathbf{A}^{\top}\le\min(m,n)$ pour $\mathbf{A}\in\mathbb{R}^{m\times n}$.
:::

Si $\operatorname{rg}\mathbf{A}=\min(m,n)$, on dit que $\mathbf{A}$ est de __rang maximal__. En pratique, on détermine le rang par la méthode du pivot de Gauss : les opérations sur les lignes ne le changent pas, et dans la forme échelonnée, il est égal au nombre de lignes qui ne sont pas entièrement nulles.

::::beispiel [Exemple de calcul]
$\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ est de rang $1$ : la deuxième colonne est le double de la première, et de même la deuxième ligne est le double de la première. Pour

$$\mathbf K=\begin{pmatrix}1&0&1\\0&1&1\\1&1&2\end{pmatrix}$$

on soustrait la première et la deuxième ligne de la troisième et l’on obtient les lignes $(1,0,1)$, $(0,1,1)$, $(0,0,0)$. Deux lignes ne sont pas nulles, donc $\operatorname{rg}\mathbf K=2$ ; effectivement, la troisième colonne est la somme des deux premières. La matrice de données des appartements est de rang maximal $3$.
::::

⁠**En bref :** Le rang compte combien de directions réellement différentes se trouvent dans les colonnes d’une matrice, et il y en a exactement autant que dans ses lignes.

:::hintergrund Pourquoi il y a autant de lignes indépendantes que de colonnes indépendantes
Cela ne va pas de soi : les lignes et les colonnes d’une matrice $3\times5$ vivent dans des espaces tout à fait différents. Voici un argument court. Supposons que $r$ colonnes de $\mathbf{A}$ soient linéairement indépendantes et que toute autre colonne soit une combinaison linéaire de celles-ci. Ces $r$ colonnes forment une matrice $\mathbf G\in\mathbb{R}^{m\times r}$. Chaque colonne $\mathbf{a}_j$ de $\mathbf{A}$ est alors $\mathbf G$ fois un vecteur de coefficients à $r$ composantes. Si l’on écrit ces vecteurs de coefficients comme colonnes d’une matrice $\mathbf F\in\mathbb{R}^{r\times n}$, on a, d’après [(9.2)](das-matrixprodukt.html#gl-9-2), $\mathbf{A}=\mathbf G\mathbf F$. Lisons maintenant le même produit ligne par ligne : la ligne $i$ de $\mathbf{A}$ est la ligne $i$ de $\mathbf G$ fois $\mathbf F$, donc une combinaison linéaire des $r$ lignes de $\mathbf F$. Toutes les lignes de $\mathbf{A}$ appartiennent donc au sous-espace engendré par les $r$ lignes de $\mathbf F$, un ensemble de dimension au plus $r$, et plus de $r$ d’entre elles ne peuvent donc pas être linéairement indépendantes. Les lignes ont donc au plus autant de directions indépendantes que les colonnes. Si l’on applique le même argument à $\mathbf{A}^{\top}$, dont les colonnes sont les lignes de $\mathbf{A}$, on obtient l’inégalité inverse. Les deux nombres sont donc égaux.
:::

### Le noyau et le théorème du rang

<span class="anker" id="stufe-13-5"></span>

Une matrice à $n$ colonnes reçoit des vecteurs provenant de $n$ directions. Une partie de ces directions arrive dans le résultat, le reste est envoyé sur le vecteur nul et se perd. Les directions perdues forment un ensemble à part.

:::definition Définition 13.7 (Noyau)
<span class="anker" id="satz-13-7"></span>

Le __noyau__ d’une matrice $\mathbf{A}\in\mathbb{R}^{m\times n}$ est l’ensemble de tous les vecteurs que $\mathbf{A}$ envoie sur le vecteur nul :

<span class="anker" id="gl-13-3"></span>
$$\ker\mathbf{A}=\{\mathbf{x}\in\mathbb{R}^n:\ \mathbf{A}\mathbf{x}=\mathbf{0}\} . \tag{13.3}$$
:::

Le noyau est l’ensemble des solutions du système homogène de la sous-section [12.4](lineare-gleichungssysteme.html#stufe-12-4). Il contient toujours le vecteur nul et, s’il contient deux vecteurs, il contient aussi toute combinaison linéaire de ceux-ci ; on peut donc parler de sa dimension.

:::satz Théorème 13.8 (Théorème du rang)
<span class="anker" id="satz-13-8"></span>

Pour toute matrice $\mathbf{A}\in\mathbb{R}^{m\times n}$, on a

<span class="anker" id="gl-13-4"></span>
$$\dim\ker\mathbf{A}+\operatorname{rg}\mathbf{A}=n . \tag{13.4}$$
:::

Les $n$ directions de l’entrée se répartissent : ce qui n’arrive pas dans le résultat atterrit dans le noyau. On le voit ainsi avec la méthode du pivot de Gauss : la forme échelonnée comporte $\operatorname{rg}\mathbf{A}$ pivots. Les $n-\operatorname{rg}\mathbf{A}$ inconnues restantes n’ont pas de pivot propre et peuvent être choisies librement dans le système homogène. Chacune d’elles fournit une direction du noyau.

:::satz Théorème 13.9 (Quand une matrice carrée est inversible)
<span class="anker" id="satz-13-9"></span>

Pour $\mathbf{A}\in\mathbb{R}^{n\times n}$, les énoncés suivants sont équivalents : (i) $\mathbf{A}$ est inversible ; (ii) $\ker\mathbf{A}=\{\mathbf{0}\}$ ; (iii) $\operatorname{rg}\mathbf{A}=n$ ; (iv) les colonnes de $\mathbf{A}$ sont linéairement indépendantes.
:::

:::beweis Inversibilité
(ii) découle de (i) d’après la sous-section [11.5](einheitsmatrix-und-inverse.html#stufe-11-5). (ii), (iii) et (iv) sont équivalents d’après le théorème du rang et la définition du rang. Il reste à montrer que (iii) et (ii) entraînent (i). Si $\operatorname{rg}\mathbf{A}=n$, l’espace des colonnes est un espace de dimension $n$ dans $\mathbb{R}^n$, donc $\mathbb{R}^n$ tout entier. Chaque système $\mathbf{A}\mathbf{c}_j=\mathbf{e}_j$ a donc une solution, et les solutions forment les colonnes d’une matrice $\mathbf{C}$ telle que $\mathbf{A}\mathbf{C}=\mathbf{I}$. De plus, $\mathbf{A}(\mathbf{C}\mathbf{A}-\mathbf{I})=\mathbf{A}\mathbf{C}\mathbf{A}-\mathbf{A}=\mathbf 0$. Chaque colonne de $\mathbf{C}\mathbf{A}-\mathbf{I}$ appartient donc au noyau, qui, d’après (ii), ne contient que le vecteur nul. Donc $\mathbf{C}\mathbf{A}=\mathbf{I}$ également, et $\mathbf{C}=\mathbf{A}^{-1}$.
:::

::::beispiel [Exemple de calcul]
$\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ a pour noyau $\operatorname{span}\{(2,\,-1)^{\top}\}$, de dimension $1$, et pour rang $1$ : $1+1=2$. La matrice $\mathbf K$ ci-dessus a pour noyau $\operatorname{span}\{(1,\,1,\,-1)^{\top}\}$, car sa troisième colonne est la somme des deux premières ; avec $\operatorname{rg}\mathbf K=2$, on a $1+2=3$.
::::

**Rang et existence de solutions.** Avec le rang et le noyau, les questions de la section [12](lineare-gleichungssysteme.html#stufe-12) se lisent sur des nombres, même pour des matrices qui ne sont pas carrées. Existe-t-il une solution ? Est-elle unique ? Existe-t-il une solution pour chaque second membre ?

:::satz Théorème 13.10 (Existence de solutions et rang)
<span class="anker" id="satz-13-10"></span>

Pour $\mathbf{A}\in\mathbb{R}^{m\times n}$ et $\mathbf{y}\in\mathbb{R}^m$, on a :

<ol class="rm">

<li>

$\mathbf{A}\mathbf{x}=\mathbf{y}$ a une solution si et seulement si $\operatorname{rg}(\mathbf{A}\,|\,\mathbf{y})=\operatorname{rg}\mathbf{A}$ ;

</li>

<li>

si le système a une solution, celle-ci est unique si et seulement si $\operatorname{rg}\mathbf{A}=n$ ;

</li>

<li>

$\mathbf{A}\mathbf{x}=\mathbf{y}$ a une solution pour tout $\mathbf{y}\in\mathbb{R}^m$ si et seulement si $\operatorname{rg}\mathbf{A}=m$.

</li>

</ol>
:::

:::beweis Existence de solutions et rang
(i) D’après la sous-section [12.2](lineare-gleichungssysteme.html#stufe-12-2), le système a une solution si et seulement si $\mathbf{y}$ appartient à l’espace des colonnes de $\mathbf{A}$. Si $\mathbf{y}$ y appartient, la colonne supplémentaire n’apporte aucune nouvelle direction : les colonnes de $(\mathbf{A}\,|\,\mathbf{y})$ engendrent le même espace que celles de $\mathbf{A}$, et les deux rangs sont égaux à la dimension de cet espace. Si $\mathbf{y}$ n’y appartient pas, on prend $r=\operatorname{rg}\mathbf{A}$ colonnes linéairement indépendantes $\mathbf g_1,\dots,\mathbf g_r$ de $\mathbf{A}$, et en plus $\mathbf{y}$. De $c_1\mathbf g_1+\dots+c_r\mathbf g_r+c\,\mathbf{y}=\mathbf{0}$, on tire $c=0$, car sinon $\mathbf{y}$ serait une combinaison linéaire des $\mathbf g_l$ et appartiendrait à l’espace des colonnes ; on a alors aussi $c_l=0$ pour tous les coefficients. Donc $(\mathbf{A}\,|\,\mathbf{y})$ a au moins $r+1$ colonnes linéairement indépendantes, et $\operatorname{rg}(\mathbf{A}\,|\,\mathbf{y})>\operatorname{rg}\mathbf{A}$.

(ii) D’après la sous-section [12.4](lineare-gleichungssysteme.html#stufe-12-4), toutes les solutions sont une solution plus les vecteurs du noyau. La solution est donc unique si et seulement si $\ker\mathbf{A}=\{\mathbf{0}\}$, ce qui, d’après le théorème du rang, signifie $\operatorname{rg}\mathbf{A}=n$.

(iii) Tout $\mathbf{y}$ appartient à l’espace des colonnes si et seulement si l’espace des colonnes est $\mathbb{R}^m$ tout entier. C’est le cas si et seulement s’il est de dimension $m$, c’est-à-dire si $\operatorname{rg}\mathbf{A}=m$.
:::

Pour une matrice carrée avec $\operatorname{rg}\mathbf{A}=n=m$, (ii) et (iii) se rejoignent : exactement une solution pour chaque second membre, en accord avec le théorème sur l’inversibilité.

::::beispiel [Exemple de calcul]
Pour $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$, on a $\operatorname{rg}\mathbf{A}=1$. Avec $\mathbf{y}=(1,\,1)^{\top}$, la matrice augmentée a pour lignes $(1,\,2\,|\,1)$ et $(2,\,4\,|\,1)$ ; si l’on soustrait deux fois la première de la deuxième, il reste $(0,\,0\,|\,-1)$, qui n’est pas une ligne nulle. Donc $\operatorname{rg}(\mathbf{A}\,|\,\mathbf{y})=2\ne1$, et le système n’a pas de solution, comme dans la sous-section [12.2](lineare-gleichungssysteme.html#stufe-12-2). Avec $\mathbf{y}=(3,\,6)^{\top}$, en revanche, il reste $(0,\,0\,|\,0)$, les rangs sont égaux, et le système a une solution. Comme $\operatorname{rg}\mathbf{A}=1<2=n$, la solution n’est pas unique : toutes les solutions sont $(1,\,1)^{\top}+t\,(2,\,-1)^{\top}$. Et comme $\operatorname{rg}\mathbf{A}=1<2=m$, il existe des seconds membres sans solution. Dans le système surdéterminé de la sous-section [12.5](lineare-gleichungssysteme.html#stufe-12-5), on a $\operatorname{rg}\mathbf{A}=2=n$ : s’il existait une solution, elle serait unique. Mais il n’y en a pas, donc, d’après (i), on a là $\operatorname{rg}(\mathbf{A}\,|\,\mathbf{y})=3$.
::::

⁠**En bref :** Le noyau rassemble les directions qu’une matrice envoie sur zéro ; le noyau et le rang se partagent les $n$ directions d’entrée. Un système $\mathbf{A}\mathbf{x}=\mathbf{y}$ a une solution si et seulement si le second membre n’augmente pas le rang, et la solution est unique si et seulement si le noyau ne contient que le vecteur nul.

### Caractéristiques dépendantes

<span class="anker" id="stufe-13-6"></span>

Dans des jeux de données réels, des caractéristiques portent parfois deux fois la même information. Un questionnaire relève le poids corporel en kilogrammes et, pour une autre exploitation, une seconde fois en livres. Une description de maison indique la surface du rez-de-chaussée, celle de l’étage et la surface totale. Pour la matrice de données, cela signifie : ses colonnes sont linéairement dépendantes, et son rang est inférieur au nombre de caractéristiques.

::::beispiel [Exemple de calcul] rez-de-chaussée, étage, surface totale
Quatre maisons :

$$\mathbf{X}=\begin{pmatrix}50&40&90\\60&0&60\\45&45&90\\70&30&100\end{pmatrix}\qquad(\text{surfaces en }\mathrm m^2).$$

La troisième colonne est la somme des deux premières. Donc $\operatorname{rg}\mathbf{X}=2<3$, et le noyau contient $\mathbf k=(1,\,1,\,-1)^{\top}$, car $\mathbf{X}\mathbf k=\mathbf{0}$. Il en découle deux choses.

<ul>

<li>

⁠**Les poids ne sont pas uniques.** Pour tout nombre $t$, $\mathbf{w}$ et $\mathbf{w}+t\,\mathbf k$ fournissent les mêmes prédictions, car $\mathbf{X}(\mathbf{w}+t\,\mathbf k)=\mathbf{X}\mathbf{w}+t\,\mathbf{X}\mathbf k=\mathbf{X}\mathbf{w}$. Les poids $(3,\,3,\,0)^{\top}$, « $3$ par mètre carré de rez-de-chaussée et d’étage », et $(0,\,0,\,3)^{\top}$, « $3$ par mètre carré de surface totale », donnent tous deux $(270,\,180,\,270,\,300)^{\top}$. À partir des seules prédictions, on ne peut pas savoir quels poids étaient visés, et cela n’a pas de sens d’interpréter un seul de ces poids.

</li>

<li>

⁠**La matrice de Gram des caractéristiques est singulière.** De $\mathbf{X}\mathbf k=\mathbf{0}$, on tire $\mathbf{X}^{\top}\mathbf{X}\mathbf k=\mathbf{X}^{\top}\mathbf{0}=\mathbf{0}$ avec $\mathbf k\ne\mathbf{0}$. D’après la sous-section [11.5](einheitsmatrix-und-inverse.html#stufe-11-5), $\mathbf{X}^{\top}\mathbf{X}$ n’a alors pas d’inverse.

</li>

</ul>
::::

::::beispiel [Exemple de calcul] kilogrammes et livres
Une livre vaut exactement $0{,}45359237$ kg, donc une masse en livres vaut $c=1/0{,}45359237\approx2{,}20462$ fois la même masse en kilogrammes. Trois personnes avec leur taille (cm), leur masse (kg) et leur masse (livres) :

$$\mathbf{X}=\begin{pmatrix}170&70&70\,c\\182&85&85\,c\\165&60&60\,c\end{pmatrix}\approx\begin{pmatrix}170&70&154{,}3\\182&85&187{,}4\\165&60&132{,}3\end{pmatrix}.$$

La troisième colonne vaut $c$ fois la deuxième, donc $\operatorname{rg}\mathbf{X}=2$, et $(0,\,c,\,-1)^{\top}$ appartient au noyau. La colonne en livres n’apporte aucune information nouvelle, elle ne fait que dupliquer une information existante.
::::

⁠**En bref :** Si des caractéristiques portent deux fois la même information, les colonnes de la matrice de données sont linéairement dépendantes ; le rang est alors inférieur à $d$, des poids différents fournissent les mêmes prédictions, et $\mathbf{X}^{\top}\mathbf{X}$ n’est pas inversible.

:::aufgabe Exercice 31 ★★ Rang et noyau
<span class="anker" id="aufg-31"></span>

Déterminez le rang et le noyau de

$$\mathbf{A}_1=\begin{pmatrix}1&2&3\\2&4&6\\1&0&1\end{pmatrix}\qquad\text{et}\qquad \mathbf{A}_2=\begin{pmatrix}1&1&0\\0&1&1\\1&0&1\end{pmatrix}$$

et vérifiez chaque fois le théorème du rang. Laquelle des deux matrices est inversible ?

:::loesung
$\mathbf{A}_1$ : la deuxième ligne est le double de la première. Si l’on soustrait de la deuxième ligne le double de la première, et de la troisième la première, il reste les lignes $(1,2,3)$, $(0,0,0)$, $(0,-2,-2)$ ; après échange des deux lignes du bas, c’est une forme échelonnée à deux pivots, donc $\operatorname{rg}\mathbf{A}_1=2$. Le noyau est donné par les équations $x_1+2x_2+3x_3=0$ et $-2x_2-2x_3=0$ : avec $x_3=t$, on a $x_2=-t$ et $x_1=-2(-t)-3t=-t$, donc $\ker\mathbf{A}_1=\operatorname{span}\{(1,\,1,\,-1)^{\top}\}$. Vérification : la somme des deux premières colonnes est $(3,\,6,\,1)^{\top}$, la troisième colonne est $(3,\,6,\,1)^{\top}$. Théorème du rang : $1+2=3$. $\mathbf{A}_1$ n’est pas inversible.

$\mathbf{A}_2$ : si l’on soustrait la première ligne de la troisième, on obtient $(0,\,-1,\,1)$ ; si l’on y ajoute la deuxième ligne, on obtient $(0,\,0,\,2)$. Trois pivots, donc $\operatorname{rg}\mathbf{A}_2=3$ et $\ker\mathbf{A}_2=\{\mathbf{0}\}$. Théorème du rang : $0+3=3$. $\mathbf{A}_2$ est inversible ; son déterminant vaut $1\cdot(1-0)-1\cdot(0-1)+0=2\ne0$.
:::
:::

:::aufgabe Exercice 32 ★★ Kilogrammes et livres
<span class="anker" id="aufg-32"></span>

Utilisez la matrice de données des personnes de la sous-section [13.6](#stufe-13-6).

<ol class="al">

<li>

Donnez deux vecteurs de poids différents qui fournissent les mêmes prédictions pour les trois personnes, de sorte que l’un n’utilise que la colonne des kilogrammes et l’autre que la colonne des livres.

</li>

<li>

Le tableau donne les valeurs en livres arrondies à une décimale. Les colonnes du tableau arrondi sont-elles encore exactement linéairement dépendantes ? Qu’est-ce que cela dit du rang que l’on calcule à partir de données arrondies ?

</li>

</ol>

:::loesung
(a) Les poids $(0,\,1,\,0)^{\top}$ prédisent pour chaque personne sa masse en kilogrammes, donc $(70,\,85,\,60)^{\top}$. Les poids $(0,\,0,\,1/c)^{\top}\approx(0;\ 0;\ 0{,}4536)^{\top}$, qui n’utilisent que la colonne des livres, fournissent les mêmes prédictions, car $\frac1c\cdot c\,x=x$. Les deux vecteurs de poids diffèrent de $\frac1c\,(0,\,c,\,-1)^{\top}$, un vecteur du noyau.

(b) Les rapports des valeurs arrondies en livres aux valeurs en kilogrammes sont $154{,}3/70\approx2{,}20429$, $187{,}4/85\approx2{,}20471$ et $132{,}3/60=2{,}205$ ; ils ne sont pas exactement égaux. Les colonnes arrondies ne sont donc plus exactement proportionnelles, et le tableau arrondi a, par le calcul, le rang maximal $3$. Sur le fond, rien n’a changé : la colonne des livres ne porte toujours presque que l’information de la colonne des kilogrammes. Le rang saute de $2$ à $3$ à cause d’arrondis minuscules. C’est pourquoi, pour des données mesurées ou arrondies, le rang seul ne dit pas si deux caractéristiques portent pratiquement la même information.
:::
:::

:::aufgabe Exercice 33 ★★ Un quartier sous forme de nombre
<span class="anker" id="aufg-33"></span>

Les appartements se trouvent soit au nord, soit au sud. On traduit cela en deux caractéristiques : « Nord » vaut $1$ pour les appartements du nord et $0$ sinon, « Sud » de même pour le sud. Pour un prix de base, on ajoute en outre une colonne de uns (sous-section [8.5](lineare-abbildungen.html#stufe-8-5)). Quatre appartements, alternativement au nord et au sud, donnent

$$\mathbf{X}=\begin{pmatrix}1&1&0\\1&0&1\\1&1&0\\1&0&1\end{pmatrix}\qquad(\text{colonnes : uns, Nord, Sud}).$$

<ol class="al">

<li>

Déterminez le rang de $\mathbf{X}$ et un vecteur $\mathbf k\ne\mathbf{0}$ du noyau. Quelle relation entre les colonnes se cache derrière ?

</li>

<li>

Montrez que les poids $(100,\,20,\,0)^{\top}$ et $(80,\,40,\,20)^{\top}$ fournissent les mêmes prédictions. Comment supprimer la dépendance sans perdre d’information ?

</li>

</ol>

:::loesung
(a) Chaque appartement se trouve soit au nord, soit au sud ; la colonne « Nord » plus la colonne « Sud » vaut donc $1$ dans chaque ligne, ce qui donne la colonne de uns. Les colonnes sont linéairement dépendantes, et $\mathbf k=(1,\,-1,\,-1)^{\top}$ appartient au noyau : $\mathbf{X}\mathbf k=\mathbf{0}$. La première et la deuxième colonne sont indépendantes, donc $\operatorname{rg}\mathbf{X}=2$.

(b) $\mathbf{X}\,(100,\,20,\,0)^{\top}=(120,\,100,\,120,\,100)^{\top}$ et $\mathbf{X}\,(80,\,40,\,20)^{\top}=(120,\,100,\,120,\,100)^{\top}$. Les deux vecteurs de poids diffèrent de $(20,\,-20,\,-20)^{\top}=20\,\mathbf k$. On supprime la dépendance en omettant l’une des deux colonnes « Nord » ou « Sud », par exemple « Sud ». Le prix de base est alors le prix au sud, et le poids de « Nord » est le supplément pour le nord. Aucune information n’est perdue, car « Sud » vaut toujours $1-\text{Nord}$ et peut être recalculé à tout moment.
:::
:::

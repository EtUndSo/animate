---
title: Le produit matriciel
pfad: Informatique / Apprentissage automatique / Fondements mathématiques / Vecteurs et matrices
adresse: informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen
knoten: Chapitre 1 : Vecteurs et matrices
nachschlagen: ja
order: 15211000
summary: Deux applications linéaires effectuées l’une après l’autre donnent de nouveau une application linéaire, donc une matrice.
tags: produit matriciel, produit extérieur
lang: fr
---

<span class="anker" id="stufe-9"></span>

:::zweck
Deux applications linéaires effectuées l’une après l’autre donnent de nouveau une application linéaire, donc une matrice. Cette section la détermine. Le résultat est le produit matriciel, et sa définition découle nécessairement de ce problème.
:::

### Le produit matriciel

<span class="anker" id="stufe-9-1"></span>

On applique d’abord à un vecteur $\mathbf{x}\in\mathbb{R}^k$ une matrice $\mathbf{B}\in\mathbb{R}^{n\times k}$, puis au résultat $\mathbf{B}\mathbf{x}\in\mathbb{R}^n$ une matrice $\mathbf{A}\in\mathbb{R}^{m\times n}$ (Fig. [33](#abb-33)). La composition $\mathbf{x}\mapsto\mathbf{A}(\mathbf{B}\mathbf{x})$ est linéaire, car chacun des deux étages conserve les sommes et les multiples. D’après le théorème de la sous-section [8.2](lineare-abbildungen.html#stufe-8-2), elle a donc une matrice. Sa colonne $l$ est l’image de $\mathbf{e}_l$ : le premier étage en fait la colonne $\mathbf{B}\mathbf{e}_l$ de $\mathbf{B}$, le second étage multiplie celle-ci par $\mathbf{A}$.

:::abbildung ml/k1hinter 33
En haut, deux applications linéaires l’une après l’autre : d’abord $\mathbf{B}$, puis $\mathbf{A}$. En bas, la même application en une seule étape, avec l’unique matrice $\mathbf{A}\mathbf{B}$. Le produit matriciel est défini précisément de sorte que les deux chemins donnent le même résultat.
:::

:::definition Définition 9.1 (Produit matriciel)
<span class="anker" id="satz-9-1"></span>

Pour $\mathbf{A}\in\mathbb{R}^{m\times n}$ et $\mathbf{B}\in\mathbb{R}^{n\times k}$, le __produit matriciel__ $\mathbf{A}\mathbf{B}\in\mathbb{R}^{m\times k}$ est la matrice de coefficients

<span class="anker" id="gl-9-1"></span>
$$(\mathbf{A}\mathbf{B})_{il}=\sum_{j=1}^{n}a_{ij}\,b_{jl},\qquad i=1,\dots,m,\quad l=1,\dots,k . \tag{9.1}$$
:::

Le coefficient $(i,l)$ est le produit scalaire de la ligne $i$ de $\mathbf{A}$ avec la colonne $l$ de $\mathbf{B}$. Le produit n’est défini que si $\mathbf{A}$ a autant de colonnes que $\mathbf{B}$ a de lignes : les tailles « intérieures » doivent coïncider, $(m\times n)\cdot(n\times k)$, et le résultat a les tailles « extérieures » $m\times k$.

:::satz Théorème 9.2 (Le produit est la composition)
<span class="anker" id="satz-9-2"></span>

Pour tout $\mathbf{x}\in\mathbb{R}^k$, on a $(\mathbf{A}\mathbf{B})\,\mathbf{x}=\mathbf{A}\,(\mathbf{B}\mathbf{x})$.
:::

:::herleitung Composition
D’après [(7.1)](das-matrix-vektor-produkt.html#gl-7-1) et [(9.1)](#gl-9-1), la composante $i$ du membre de gauche est

$$\sum_{l=1}^k(\mathbf{A}\mathbf{B})_{il}\,x_l=\sum_{l=1}^k\sum_{j=1}^na_{ij}\,b_{jl}\,x_l=\sum_{j=1}^na_{ij}\Bigl(\sum_{l=1}^kb_{jl}\,x_l\Bigr)=\sum_{j=1}^na_{ij}\,(\mathbf{B}\mathbf{x})_j ,$$

et c’est la composante $i$ de $\mathbf{A}(\mathbf{B}\mathbf{x})$. À l’étape du milieu, on a échangé les deux sommes et mis $a_{ij}$ en facteur devant la somme intérieure.
:::

::::beispiel [Exemple de calcul]
Pour $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\0&1\end{smallmatrix}\bigr)$ et $\mathbf{B}=\bigl(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr)$, on a

$$\mathbf{A}\mathbf{B}=\begin{pmatrix}2&1\\1&0\end{pmatrix}.$$

Chacun des quatre coefficients est une somme selon [(9.1)](#gl-9-1) (Fig. [34](#abb-34)).

:::abbildung ml/k1rprodukt 34
Le produit matriciel coefficient par coefficient : le coefficient $(i,l)$ est la ligne $i$ de $\mathbf{A}$ fois la colonne $l$ de $\mathbf{B}$.
:::

Vérification avec $\mathbf{x}=(1,\,2)^{\top}$ : $\mathbf{B}\mathbf{x}=(2,\,1)^{\top}$, puis $\mathbf{A}(\mathbf{B}\mathbf{x})=(4,\,1)^{\top}$ ; et directement $(\mathbf{A}\mathbf{B})\mathbf{x}=(2+2,\ 1+0)^{\top}=(4,\,1)^{\top}$.
::::

⁠**En bref :** Le produit matriciel $\mathbf{A}\mathbf{B}$ est la matrice de l’application « d’abord $\mathbf{B}$, puis $\mathbf{A}$ » ; son coefficient $(i,l)$ est la ligne $i$ de $\mathbf{A}$ fois la colonne $l$ de $\mathbf{B}$.

:::hintergrund Pourquoi le produit matriciel est défini précisément ainsi
La formule [(9.1)](#gl-9-1) semble arbitraire au premier abord. Il paraîtrait plus naturel de multiplier les matrices coefficient par coefficient. Mais le produit matriciel n’est pas une libre invention : il est fixé par une exigence, celle d’être la matrice de la composition. D’après le théorème de la sous-section [8.2](lineare-abbildungen.html#stufe-8-2), cette matrice est unique, et sa colonne $l$ doit être l’image de $\mathbf{e}_l$ par les deux applications, c’est-à-dire $\mathbf{A}$ fois la colonne $l$ de $\mathbf{B}$. Si on l’écrit composante par composante, on obtient exactement [(9.1)](#gl-9-1). Un produit coefficient par coefficient n’aurait pas une telle signification : il ne décrit pas la composition de deux applications.
:::

### De nombreux vecteurs à la fois

<span class="anker" id="stufe-9-2"></span>

Comme on l’a vu en établissant le produit, la colonne $l$ de $\mathbf{A}\mathbf{B}$ est le produit de $\mathbf{A}$ par la colonne $l$ de $\mathbf{B}$. On peut donc lire un produit matriciel comme plusieurs produits matrice-vecteur placés côte à côte :

<span class="anker" id="gl-9-2"></span>
$$\mathbf{A}\begin{pmatrix}\mathbf{B}\mathbf{e}_1&\cdots&\mathbf{B}\mathbf{e}_k\end{pmatrix}=\begin{pmatrix}\mathbf{A}\mathbf{B}\mathbf{e}_1&\cdots&\mathbf{A}\mathbf{B}\mathbf{e}_k\end{pmatrix}. \tag{9.2}$$

De même, la ligne $i$ de $\mathbf{A}\mathbf{B}$ est la ligne $i$ de $\mathbf{A}$, multipliée par $\mathbf{B}$.

Pour les données, cela signifie : si l’on veut appliquer plusieurs sommes pondérées à tous les exemples, on écrit les vecteurs de poids côte à côte comme colonnes d’une matrice $\mathbf{W}$. Le produit $\mathbf{X}\mathbf{W}$ contient alors dans la colonne $l$ les prédictions obtenues avec le $l$-ième vecteur de poids.

::::beispiel [Exemple de calcul]
Outre le prix d’achat avec $\mathbf{w}=(3,\,10,\,-4)^{\top}$ (milliers d’euros), on veut estimer le loyer mensuel avec les poids $\mathbf{w}_{\mathrm M}=(12,\,30,\,-8)^{\top}$ (euros). Avec $\mathbf{W}=\begin{pmatrix}\mathbf{w}&\mathbf{w}_{\mathrm M}\end{pmatrix}\in\mathbb{R}^{3\times2}$, on a

$$\mathbf{X}\mathbf{W}=\begin{pmatrix}60&2&3\\40&1&1\\90&4&6\\70&3&2\end{pmatrix}\begin{pmatrix}3&12\\10&30\\-4&-8\end{pmatrix}=\begin{pmatrix}188&756\\126&502\\286&1152\\232&914\end{pmatrix}.$$

La ligne $i$ contient les deux estimations pour l’appartement $i$, la colonne $1$ tous les prix d’achat, la colonne $2$ tous les loyers.
::::

⁠**En bref :** Les colonnes de $\mathbf{A}\mathbf{B}$ sont $\mathbf{A}$ fois les colonnes de $\mathbf{B}$ ; $\mathbf{X}\mathbf{W}$ applique plusieurs sommes pondérées à tous les exemples à la fois.

### Règles de calcul : l’ordre compte

<span class="anker" id="stufe-9-3"></span>

Pour les nombres, $2\cdot3=3\cdot2$. Pour les matrices, ce n’est pas le cas, et la raison est facile à voir : tourner d’abord puis étirer n’est pas la même chose qu’étirer d’abord puis tourner (Fig. [35](#abb-35)).

:::abbildung ml/k1reihenfolge 35
Le carré unité avec $\mathbf{e}_1$ (en rouge) et $\mathbf{e}_2$ (en vert), et à côté ses images par $\mathbf{S}\mathbf R$ et $\mathbf R\mathbf{S}$. Ici, $\mathbf R$ est la rotation de $90^\circ$ et $\mathbf{S}=\operatorname{diag}(2;\,0{,}5)$ l’étirement. L’ordre décide si le rectangle s’allonge horizontalement ou verticalement.
:::

:::satz Théorème 9.3 (Règles de calcul du produit matriciel)
<span class="anker" id="satz-9-3"></span>

Pour des matrices de tailles compatibles et des scalaires $c$, on a :

<ol class="rm">

<li>

$(\mathbf{A}\mathbf{B})\mathbf{C}=\mathbf{A}(\mathbf{B}\mathbf{C})$ (associativité) ;

</li>

<li>

$\mathbf{A}(\mathbf{B}+\mathbf{C})=\mathbf{A}\mathbf{B}+\mathbf{A}\mathbf{C}$ et $(\mathbf{A}+\mathbf{B})\mathbf{C}=\mathbf{A}\mathbf{C}+\mathbf{B}\mathbf{C}$ (distributivité) ;

</li>

<li>

$c\,(\mathbf{A}\mathbf{B})=(c\,\mathbf{A})\mathbf{B}=\mathbf{A}(c\,\mathbf{B})$.

</li>

</ol>

En général, cependant, $\mathbf{A}\mathbf{B}\ne\mathbf{B}\mathbf{A}$ : le produit matriciel n’est *pas* commutatif.
:::

La règle (i) découle de la signification : les deux membres sont la matrice de l’application « d’abord $\mathbf{C}$, puis $\mathbf{B}$, puis $\mathbf{A}$ », car $(\mathbf{A}\mathbf{B})(\mathbf{C}\mathbf{x})=\mathbf{A}(\mathbf{B}(\mathbf{C}\mathbf{x}))=\mathbf{A}((\mathbf{B}\mathbf{C})\mathbf{x})$ pour tout $\mathbf{x}$. Les règles (ii) et (iii) se vérifient coefficient par coefficient à l’aide de [(9.1)](#gl-9-1) et des règles de calcul des sommes.

::::beispiel [Exemple de calcul 1]
Avec la rotation $\mathbf R=\mathbf R_{90^\circ}=\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)$ et l’étirement $\mathbf{S}=\operatorname{diag}(2;\,0{,}5)$, on a

$$\mathbf{S}\mathbf R=\begin{pmatrix}0&-2\\0{,}5&0\end{pmatrix},\qquad \mathbf R\mathbf{S}=\begin{pmatrix}0&-0{,}5\\2&0\end{pmatrix}.$$

Tourner d’abord puis étirer envoie $\mathbf{e}_1$ sur $(0;\,0{,}5)^{\top}$, étirer d’abord puis tourner l’envoie sur $(0,\,2)^{\top}$.
::::

::::beispiel [Exemple de calcul 2]
D’après la sous-section [9.1](#stufe-9-1), $\mathbf{A}\mathbf{B}=\bigl(\begin{smallmatrix}2&1\\1&0\end{smallmatrix}\bigr)$, mais $\mathbf{B}\mathbf{A}=\bigl(\begin{smallmatrix}0&1\\1&2\end{smallmatrix}\bigr)$. Avec des tailles différentes, c’est encore plus net : pour $\mathbf{A}\in\mathbb{R}^{2\times3}$ et $\mathbf{B}\in\mathbb{R}^{3\times2}$, $\mathbf{A}\mathbf{B}$ est une matrice $2\times2$ et $\mathbf{B}\mathbf{A}$ une matrice $3\times3$.
::::

⁠**En bref :** Dans un produit matriciel, on peut déplacer les parenthèses et développer, mais pas échanger l’ordre des facteurs.

:::hintergrund Pourquoi le placement des parenthèses fait gagner du temps de calcul
D’après la règle (i), $(\mathbf{A}\mathbf{B})\mathbf{x}=\mathbf{A}(\mathbf{B}\mathbf{x})$. Le résultat est le même, le travail ne l’est pas. Pour deux matrices $n\times n$, le produit $\mathbf{A}\mathbf{B}$ demande, pour chacun des $n^2$ coefficients, $n$ multiplications et $n-1$ additions, soit au total environ $2n^3$ opérations élémentaires ; ensuite, $(\mathbf{A}\mathbf{B})\mathbf{x}$ coûte encore environ $2n^2$. La voie $\mathbf{A}(\mathbf{B}\mathbf{x})$ se compose de deux produits matrice-vecteur d’environ $2n^2$ opérations chacun. Pour $n=1000$, cela fait environ $2\cdot10^9$ contre $4\cdot10^6$ opérations élémentaires, une différence d’un facteur $500$. Qui applique une longue chaîne de matrices à un vecteur calcule donc de droite à gauche et ne forme jamais la matrice produit.
:::

### Deux étages linéaires n’en font qu’un

<span class="anker" id="stufe-9-4"></span>

Si l’on enchaîne plusieurs étages de calcul linéaires, on n’obtient pas de nouveau type d’application. D’après la sous-section [9.1](#stufe-9-1), c’est clair, mais cela mérite un théorème à part, car cela marque les limites des règles linéaires.

:::satz Théorème 9.4 (Applications linéaires en cascade)
<span class="anker" id="satz-9-4"></span>

Si $f(\mathbf{x})=\mathbf{B}\mathbf{x}$ et $g(\mathbf{u})=\mathbf{A}\mathbf{u}$ sont linéaires, la composition $\mathbf{x}\mapsto g(f(\mathbf{x}))$ est de nouveau linéaire, et ce avec l’unique matrice $\mathbf{A}\mathbf{B}$. Il en va de même pour toute chaîne finie d’étages linéaires.
:::

Quel que soit le nombre d’étages linéaires que l’on enchaîne, le résultat peut toujours se calculer en une seule étape avec une seule matrice. Ce que peut faire une chaîne d’étages linéaires, une seule matrice le peut donc déjà. À petite échelle, on le connaît des achats : si l’on convertit d’abord un prix d’euros en dollars, puis qu’on retire une remise de $10$ %, l’ensemble revient à un seul facteur de conversion.

::::beispiel [Exemple de calcul]
Un premier étage transforme trois nombres en deux, $\mathbf{B}=\bigl(\begin{smallmatrix}1&2&0\\0&1&-1\end{smallmatrix}\bigr)$, un second transforme deux nombres de nouveau en trois, $\mathbf{A}=\Bigl(\begin{smallmatrix}2&1\\1&-1\\0&3\end{smallmatrix}\Bigr)$. Ensemble, cela donne l’unique matrice

$$\mathbf{A}\mathbf{B}=\begin{pmatrix}2&5&-1\\1&1&1\\0&3&-3\end{pmatrix}.$$

Vérification avec $\mathbf{x}=(1,\,1,\,1)^{\top}$ : $\mathbf{B}\mathbf{x}=(3,\,0)^{\top}$ et $\mathbf{A}(3,\,0)^{\top}=(6,\,3,\,0)^{\top}$ ; de même, $(\mathbf{A}\mathbf{B})\mathbf{x}=(2+5-1,\ 1+1+1,\ 0+3-3)^{\top}=(6,\,3,\,0)^{\top}$.
::::

⁠**En bref :** Des étages linéaires enchaînés forment ensemble une seule application linéaire, dont la matrice est le produit des matrices de chaque étage.

### Le produit extérieur

<span class="anker" id="stufe-9-5"></span>

Le produit scalaire $\mathbf{u}^{\top}\mathbf{v}$ est « ligne fois colonne » et donne un nombre. Si l’on inverse l’ordre, « colonne fois ligne », on obtient d’après [(9.1)](#gl-9-1) une matrice entière : le tableau de tous les produits d’une composante de l’un des vecteurs par une composante de l’autre, comme une table de multiplication.

:::definition Définition 9.5 (Produit extérieur)
<span class="anker" id="satz-9-5"></span>

Pour $\mathbf{u}\in\mathbb{R}^m$ et $\mathbf{v}\in\mathbb{R}^n$, le __produit extérieur__ $\mathbf{u}\mathbf{v}^{\top}\in\mathbb{R}^{m\times n}$ est la matrice de coefficients

<span class="anker" id="gl-9-3"></span>
$$(\mathbf{u}\mathbf{v}^{\top})_{ij}=u_i\,v_j . \tag{9.3}$$
:::

C’est le produit matriciel d’une matrice $m\times1$ par une matrice $1\times n$. Chaque colonne est un multiple de $\mathbf{u}$, à savoir $v_j\,\mathbf{u}$, et chaque ligne un multiple de $\mathbf{v}^{\top}$.

::::beispiel [Exemple de calcul]
$$\begin{pmatrix}1\\2\\3\end{pmatrix}\begin{pmatrix}4&5\end{pmatrix}=\begin{pmatrix}4&5\\8&10\\12&15\end{pmatrix}.$$
::::

Avec le produit extérieur, tout produit matriciel peut s’écrire comme une somme : « colonne $j$ de $\mathbf{A}$ fois ligne $j$ de $\mathbf{B}$ », sommé sur $j$,

<span class="anker" id="gl-9-4"></span>
$$\mathbf{A}\mathbf{B}=\sum_{j=1}^n\mathbf{a}_j\,\bigl(\text{ligne $j$ de }\mathbf{B}\bigr) . \tag{9.4}$$

Le coefficient $(i,l)$ du membre de droite est $\sum_ja_{ij}\,b_{jl}$, exactement comme dans [(9.1)](#gl-9-1). Pour $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\0&1\end{smallmatrix}\bigr)$ et $\mathbf{B}=\bigl(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr)$ de la sous-section [9.1](#stufe-9-1), la somme de deux produits extérieurs redonne $\mathbf{A}\mathbf{B}$ (Fig. [36](#abb-36)).

:::abbildung ml/k1raeusser 36
Le produit matriciel comme somme de produits extérieurs : colonne $j$ de $\mathbf{A}$ fois ligne $j$ de $\mathbf{B}$, sommé sur $j=1,2$.
:::

⁠**En bref :** Le produit extérieur $\mathbf{u}\mathbf{v}^{\top}$ est le tableau de tous les produits $u_iv_j$ ; tout produit matriciel est une somme de tels tableaux.

:::aufgabe Exercice 21 ★ Produits et tailles
<span class="anker" id="aufg-21"></span>

<ol class="al">

<li>

Calculez $\mathbf{C}\mathbf{D}$ et $\mathbf{D}\mathbf{C}$ pour $\mathbf{C}=\bigl(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr)$ et $\mathbf{D}=\bigl(\begin{smallmatrix}0&1\\1&1\end{smallmatrix}\bigr)$.

</li>

<li>

Soient $\mathbf{A}\in\mathbb{R}^{2\times3}$, $\mathbf{B}\in\mathbb{R}^{3\times4}$ et $\mathbf{x}\in\mathbb{R}^4$. Lesquelles des expressions $\mathbf{A}\mathbf{B}$, $\mathbf{B}\mathbf{A}$, $\mathbf{A}\mathbf{B}\mathbf{x}$, $\mathbf{B}\mathbf{x}\mathbf{A}$ sont définies, et quelle est la taille du résultat ?

</li>

<li>

Calculez le produit extérieur $(1,\,-1)^{\top}(2,\,0,\,3)$ et vérifiez que chaque ligne est un multiple de $(2,\,0,\,3)$.

</li>

</ol>

:::loesung
(a) $\mathbf{C}\mathbf{D}=\bigl(\begin{smallmatrix}1\cdot0+2\cdot1&1\cdot1+2\cdot1\\3\cdot0+4\cdot1&3\cdot1+4\cdot1\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}2&3\\4&7\end{smallmatrix}\bigr)$ et $\mathbf{D}\mathbf{C}=\bigl(\begin{smallmatrix}0+3&0+4\\1+3&2+4\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}3&4\\4&6\end{smallmatrix}\bigr)$. Les deux produits sont différents.

(b) $\mathbf{A}\mathbf{B}$ : $(2\times3)\cdot(3\times4)$ convient, taille $2\times4$. $\mathbf{B}\mathbf{A}$ : $(3\times4)\cdot(2\times3)$, dimensions intérieures $4\ne2$, non défini. $\mathbf{A}\mathbf{B}\mathbf{x}$ : $(2\times4)\cdot(4\times1)$ convient, un vecteur de $\mathbb{R}^2$. $\mathbf{B}\mathbf{x}\mathbf{A}$ : $\mathbf{B}\mathbf{x}$ est de taille $3\times1$, et $(3\times1)\cdot(2\times3)$ ne convient pas, dimensions intérieures $1\ne2$ ; non défini.

(c) $(1,\,-1)^{\top}(2,\,0,\,3)=\bigl(\begin{smallmatrix}2&0&3\\-2&0&-3\end{smallmatrix}\bigr)$. La première ligne est $1\cdot(2,0,3)$, la deuxième $-1\cdot(2,0,3)$.
:::
:::

:::aufgabe Exercice 22 ★★ Deux rotations
<span class="anker" id="aufg-22"></span>

<ol class="al">

<li>

Calculez $\mathbf R_\alpha\mathbf R_\beta$ à l’aide de [(8.3)](lineare-abbildungen.html#gl-8-3). De quelle rotation s’agit-il ? Quelles deux formules de trigonométrie obtenez-vous au passage ?

</li>

<li>

Calculez $\mathbf R_{90^\circ}^2=\mathbf R_{90^\circ}\mathbf R_{90^\circ}$ et $\mathbf R_{90^\circ}^4$ et interprétez géométriquement les résultats.

</li>

<li>

A-t-on $\mathbf R_\alpha\mathbf R_\beta=\mathbf R_\beta\mathbf R_\alpha$ ? Pourquoi cela ne contredit-il pas la règle selon laquelle les matrices ne commutent pas ?

</li>

</ol>

:::loesung
(a) En développant, on obtient

$$\mathbf R_\alpha\mathbf R_\beta=\begin{pmatrix}\cos\alpha\cos\beta-\sin\alpha\sin\beta&-(\cos\alpha\sin\beta+\sin\alpha\cos\beta)\\\sin\alpha\cos\beta+\cos\alpha\sin\beta&\cos\alpha\cos\beta-\sin\alpha\sin\beta\end{pmatrix}.$$

Géométriquement, c’est « d’abord tourner de $\beta$, puis de $\alpha$ », donc la rotation d’angle $\alpha+\beta$, dont la matrice est $\mathbf R_{\alpha+\beta}$ d’après [(8.3)](lineare-abbildungen.html#gl-8-3). En comparant les coefficients, on obtient les formules d’addition $\cos(\alpha+\beta)=\cos\alpha\cos\beta-\sin\alpha\sin\beta$ et $\sin(\alpha+\beta)=\sin\alpha\cos\beta+\cos\alpha\sin\beta$. Le produit matriciel les fournit sans qu’il soit nécessaire de les connaître par cœur.

(b) $\mathbf R_{90^\circ}^2=\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}-1&0\\0&-1\end{smallmatrix}\bigr)=-\mathbf{I}$ : deux fois $90^\circ$ font un demi-tour, chaque point est envoyé sur son symétrique par rapport à l’origine. $\mathbf R_{90^\circ}^4=(-\mathbf{I})(-\mathbf{I})=\mathbf{I}$ : quatre quarts de tour font un tour complet.

(c) Oui : les deux produits valent $\mathbf R_{\alpha+\beta}=\mathbf R_{\beta+\alpha}$, car des rotations du plan autour d’un même point peuvent être effectuées dans n’importe quel ordre. « Non commutatif » signifie seulement que $\mathbf{A}\mathbf{B}=\mathbf{B}\mathbf{A}$ n’est *pas toujours* vrai. Pour certains couples, par exemple deux rotations du plan ou deux matrices diagonales, l’égalité peut néanmoins avoir lieu.
:::
:::

:::aufgabe Exercice 23 ★★ Les bonnes parenthèses
<span class="anker" id="aufg-23"></span>

Soient $\mathbf{A}\in\mathbb{R}^{100\times1000}$, $\mathbf{B}\in\mathbb{R}^{1000\times1000}$ et $\mathbf{x}\in\mathbb{R}^{1000}$. Estimez le nombre d’opérations élémentaires pour $(\mathbf{A}\mathbf{B})\mathbf{x}$ et pour $\mathbf{A}(\mathbf{B}\mathbf{x})$. Comptez pour cela environ $2mnk$ opérations pour le produit d’une matrice $m\times n$ par une matrice $n\times k$.

:::loesung
$(\mathbf{A}\mathbf{B})\mathbf{x}$ : le produit $\mathbf{A}\mathbf{B}$ d’une matrice $100\times1000$ par une matrice $1000\times1000$ coûte environ $2\cdot100\cdot1000\cdot1000=2\cdot10^8$, puis $(\mathbf{A}\mathbf{B})\mathbf{x}$ encore environ $2\cdot100\cdot1000=2\cdot10^5$ ; au total, environ $200{,}2$ millions. $\mathbf{A}(\mathbf{B}\mathbf{x})$ : $\mathbf{B}\mathbf{x}$ coûte environ $2\cdot1000\cdot1000=2\cdot10^6$, puis $\mathbf{A}(\mathbf{B}\mathbf{x})$ environ $2\cdot10^5$ ; au total, environ $2{,}2$ millions. La seconde voie est environ $91$ fois plus rapide, avec le même résultat.
:::
:::

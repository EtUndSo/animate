---
title: Matrice identité et inverse
pfad: Informatique / Apprentissage automatique / Fondements mathématiques / Vecteurs et matrices
knoten: Fondements 1 : Vecteurs et matrices
nachschlagen: ja
order: 15211200
summary: Certaines applications linéaires peuvent être annulées, d’autres non.
tags: matrice identité, inversible, inverse, singulière
lang: fr
---

<span class="anker" id="stufe-11"></span>

:::zweck
Certaines applications linéaires peuvent être annulées, d’autres non. Cette section introduit la matrice qui ne change rien et la matrice inverse, qui défait une application, et précise quand celle-ci existe.
:::

### La matrice identité

<span class="anker" id="stufe-11-1"></span>

Parmi toutes les applications linéaires, il en est une qui ne fait rien du tout : elle envoie chaque vecteur sur lui-même. D’après [(8.2)](lineare-abbildungen.html#gl-8-2), ses colonnes sont les images des vecteurs unitaires, c’est-à-dire les vecteurs unitaires eux-mêmes.

:::definition Définition 11.1 (Matrice identité)
<span class="anker" id="satz-11-1"></span>

La __matrice identité__ $\mathbf{I}_n\in\mathbb{R}^{n\times n}$ est la matrice diagonale dont tous les coefficients diagonaux valent un. Ses colonnes sont $\mathbf{e}_1,\dots,\mathbf{e}_n$.
:::

Lorsque la taille est claire, on écrit simplement $\mathbf{I}$. Pour tout vecteur $\mathbf{x}\in\mathbb{R}^n$, on a $\mathbf{I}\mathbf{x}=\mathbf{x}$, et pour toute matrice $\mathbf{A}\in\mathbb{R}^{m\times n}$, $\mathbf{A}\mathbf{I}_n=\mathbf{A}$ et $\mathbf{I}_m\mathbf{A}=\mathbf{A}$. Dans le produit matriciel, la matrice identité joue le rôle du nombre $1$.

⁠**Exemple de calcul :**

$$\mathbf{I}_3=\begin{pmatrix}1&0&0\\0&1&0\\0&0&1\end{pmatrix},\qquad \mathbf{I}_3\begin{pmatrix}60\\2\\3\end{pmatrix}=\begin{pmatrix}60\\2\\3\end{pmatrix}.$$

⁠**En bref :** La matrice identité a des uns sur la diagonale et des zéros ailleurs ; en tant qu’application, elle laisse chaque vecteur inchangé.

### La matrice inverse

<span class="anker" id="stufe-11-2"></span>

Une rotation de $90^\circ$ s’annule en tournant de $90^\circ$ en sens inverse. Un étirement au double s’annule en comprimant de moitié. Dans les deux cas, il existe une seconde application qui annule la première : effectuées l’une après l’autre, les deux ensemble ne font rien.

:::definition Définition 11.2 (Matrice inverse)
<span class="anker" id="satz-11-2"></span>

Une matrice carrée $\mathbf{A}\in\mathbb{R}^{n\times n}$ est dite __inversible__ s’il existe une matrice $\mathbf{A}^{-1}\in\mathbb{R}^{n\times n}$ telle que

<span class="anker" id="gl-11-1"></span>
$$\mathbf{A}\mathbf{A}^{-1}=\mathbf{A}^{-1}\mathbf{A}=\mathbf{I} . \tag{11.1}$$

La matrice $\mathbf{A}^{-1}$ s’appelle l’__inverse__ de $\mathbf{A}$.
:::

Il existe au plus une telle matrice. En effet, si $\mathbf{B}$ et $\mathbf{C}$ sont toutes deux inverses de $\mathbf{A}$, alors $\mathbf{B}=\mathbf{B}\mathbf{I}=\mathbf{B}(\mathbf{A}\mathbf{C})=(\mathbf{B}\mathbf{A})\mathbf{C}=\mathbf{I}\mathbf{C}=\mathbf{C}$. C’est pourquoi on peut parler de *l’*inverse. Si on la connaît, on peut retrouver l’entrée à partir de tout résultat $\mathbf{y}=\mathbf{A}\mathbf{x}$ : $\mathbf{A}^{-1}\mathbf{y}=\mathbf{A}^{-1}\mathbf{A}\mathbf{x}=\mathbf{x}$.

⁠**Exemple de calcul :**

$$\begin{pmatrix}2&1\\1&1\end{pmatrix}\begin{pmatrix}1&-1\\-1&2\end{pmatrix}=\begin{pmatrix}2-1&-2+2\\1-1&-1+2\end{pmatrix}=\begin{pmatrix}1&0\\0&1\end{pmatrix},$$

et de même dans l’autre ordre, donc $\bigl(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\bigr)^{-1}=\bigl(\begin{smallmatrix}1&-1\\-1&2\end{smallmatrix}\bigr)$. L’étirement a pour inverse $\operatorname{diag}(2;\,0{,}5)^{-1}=\operatorname{diag}(0{,}5;\,2)$, la rotation de $90^\circ$ la rotation de $-90^\circ$, $\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)^{-1}=\bigl(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\bigr)$.

⁠**En bref :** L’inverse $\mathbf{A}^{-1}$ annule l’application $\mathbf{A}$ : $\mathbf{A}^{-1}\mathbf{A}=\mathbf{A}\mathbf{A}^{-1}=\mathbf{I}$.

:::hintergrund L’inverse d’une matrice diagonale
Une matrice diagonale $\operatorname{diag}(\mathbf{v})$ multiplie chaque composante par son propre facteur $v_j$. On annule cela en divisant chaque composante par son facteur : $\operatorname{diag}(\mathbf{v})^{-1}=\operatorname{diag}(1/v_1,\dots,1/v_n)$. C’est possible exactement lorsqu’aucun facteur n’est nul. Un facteur $v_j=0$ efface la composante $j$, et ce qui est effacé, aucun calcul ne peut le récupérer.
:::

### L’inverse d’une matrice $2\times2$

<span class="anker" id="stufe-11-3"></span>

Pour les matrices $2\times2$, il existe une formule simple. On échange les deux coefficients diagonaux, on place un signe moins devant les deux autres et l’on divise par un nombre formé à partir des quatre coefficients.

:::satz Théorème 11.3 (Inverse d’une matrice $2\times2$)
<span class="anker" id="satz-11-3"></span>

La matrice $\mathbf{A}=\bigl(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\bigr)$ est inversible si et seulement si $ad-bc\ne0$, et alors

<span class="anker" id="gl-11-2"></span>
$$\mathbf{A}^{-1}=\frac{1}{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}. \tag{11.2}$$
:::

:::herleitung Inverse d’une matrice $2\times2$
En développant, on obtient

$$\begin{pmatrix}a&b\\c&d\end{pmatrix}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}=\begin{pmatrix}ad-bc&-ab+ba\\cd-dc&-cb+da\end{pmatrix}=(ad-bc)\,\mathbf{I} ,$$

et de même dans l’autre ordre. Si $ad-bc\ne0$, on divise par ce nombre et l’on obtient [(11.1)](#gl-11-1). Si $ad-bc=0$, $\mathbf{A}$ envoie le vecteur $(d,\,-c)^{\top}$ sur $(ad-bc,\ cd-dc)^{\top}=\mathbf{0}$, et de même $(b,\,-a)^{\top}$ sur $\mathbf{0}$. Au moins l’un des deux n’est pas le vecteur nul, sauf si les quatre coefficients sont nuls, et alors $\mathbf{A}$ est de toute façon la matrice nulle. Or une matrice qui envoie un vecteur $\mathbf{x}\ne\mathbf{0}$ sur $\mathbf{0}$ n’a pas d’inverse : s’il en existait une, on aurait $\mathbf{x}=\mathbf{A}^{-1}\mathbf{A}\mathbf{x}=\mathbf{A}^{-1}\mathbf{0}=\mathbf{0}$.
:::

⁠**Exemple de calcul :** Pour $\bigl(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\bigr)$, on a $ad-bc=2-1=1$, donc l’inverse est $\bigl(\begin{smallmatrix}1&-1\\-1&2\end{smallmatrix}\bigr)$, comme plus haut. Pour $\bigl(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\bigr)$, on a $ad-bc=5$, et l’inverse est $\tfrac15\bigl(\begin{smallmatrix}2&-1\\-1&3\end{smallmatrix}\bigr)$.

⁠**En bref :** Une matrice $2\times2$ est inversible si et seulement si $ad-bc\ne0$ ; l’inverse est $\frac{1}{ad-bc}\bigl(\begin{smallmatrix}d&-b\\-c&a\end{smallmatrix}\bigr)$.

### Règles de calcul pour les inverses

<span class="anker" id="stufe-11-4"></span>

Qui effectue deux applications l’une après l’autre et veut annuler le tout doit d’abord défaire la seconde. C’est pourquoi l’ordre s’inverse quand on inverse un produit.

:::satz Théorème 11.4 (Règles de calcul pour les inverses)
<span class="anker" id="satz-11-4"></span>

Si $\mathbf{A},\mathbf{B}\in\mathbb{R}^{n\times n}$ sont inversibles et si $c\ne0$, alors $\mathbf{A}\mathbf{B}$, $\mathbf{A}^{\top}$, $\mathbf{A}^{-1}$ et $c\,\mathbf{A}$ sont également inversibles, et l’on a

$$(\mathbf{A}\mathbf{B})^{-1}=\mathbf{B}^{-1}\mathbf{A}^{-1},\qquad(\mathbf{A}^{\top})^{-1}=(\mathbf{A}^{-1})^{\top},\qquad(\mathbf{A}^{-1})^{-1}=\mathbf{A},\qquad(c\,\mathbf{A})^{-1}=\tfrac1c\,\mathbf{A}^{-1}.$$
:::

:::herleitung Règles de calcul pour les inverses
On vérifie à chaque fois que le produit avec le candidat donne la matrice identité. Pour le produit : $(\mathbf{A}\mathbf{B})(\mathbf{B}^{-1}\mathbf{A}^{-1})=\mathbf{A}(\mathbf{B}\mathbf{B}^{-1})\mathbf{A}^{-1}=\mathbf{A}\mathbf{A}^{-1}=\mathbf{I}$, et de même $(\mathbf{B}^{-1}\mathbf{A}^{-1})(\mathbf{A}\mathbf{B})=\mathbf{I}$. Pour la transposée : $\mathbf{A}^{\top}(\mathbf{A}^{-1})^{\top}=(\mathbf{A}^{-1}\mathbf{A})^{\top}=\mathbf{I}^{\top}=\mathbf{I}$, et de même dans l’autre ordre. Les deux dernières règles découlent directement de [(11.1)](#gl-11-1).
:::

Une règle que l’on aimerait bien avoir n’est pas vraie : $(\mathbf{A}+\mathbf{B})^{-1}$ n’est en général pas $\mathbf{A}^{-1}+\mathbf{B}^{-1}$. Déjà pour les nombres, $\frac{1}{2+4}=\frac16$, mais $\frac12+\frac14=\frac34$.

⁠**Exemple de calcul :** Pour $\mathbf{A}=\bigl(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\bigr)$ et $\mathbf{B}=\bigl(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\bigr)$, on a $\mathbf{A}\mathbf{B}=\bigl(\begin{smallmatrix}7&4\\4&3\end{smallmatrix}\bigr)$ avec $ad-bc=21-16=5$, donc $(\mathbf{A}\mathbf{B})^{-1}=\tfrac15\bigl(\begin{smallmatrix}3&-4\\-4&7\end{smallmatrix}\bigr)$. On obtient la même chose avec

$$\mathbf{B}^{-1}\mathbf{A}^{-1}=\tfrac15\begin{pmatrix}2&-1\\-1&3\end{pmatrix}\begin{pmatrix}1&-1\\-1&2\end{pmatrix}=\tfrac15\begin{pmatrix}3&-4\\-4&7\end{pmatrix}.$$

⁠**En bref :** L’inverse d’un produit est le produit des inverses dans l’ordre inverse, $(\mathbf{A}\mathbf{B})^{-1}=\mathbf{B}^{-1}\mathbf{A}^{-1}$.

:::hintergrund Une image pour l’ordre inversé
Qui, le matin, enfile d’abord un pull, puis une veste, retire le soir d’abord la veste, puis le pull. L’annulation parcourt les étapes à rebours. L’application $\mathbf{A}\mathbf{B}$ est « d’abord $\mathbf{B}$, puis $\mathbf{A}$ » ; pour l’annuler, il faut d’abord défaire $\mathbf{A}$, puis $\mathbf{B}$, c’est-à-dire appliquer d’abord $\mathbf{A}^{-1}$, puis $\mathbf{B}^{-1}$. Écrit sous forme matricielle, avec l’application effectuée en premier à droite, cela donne $\mathbf{B}^{-1}\mathbf{A}^{-1}$. L’image ne vaut que pour ce qui concerne l’ordre ; elle n’explique pas pourquoi une inverse existe.
:::

### Quand il n’y a pas d’inverse

<span class="anker" id="stufe-11-5"></span>

La matrice $\operatorname{diag}(1;\,0)$ aplatit le plan sur l’axe des $x_1$ (Fig. [32](lineare-abbildungen.html#abb-32)). Les points $(1,\,5)^{\top}$ et $(1,\,-2)^{\top}$ arrivent tous deux en $(1,\,0)^{\top}$. Qui ne voit que le résultat $(1,\,0)^{\top}$ ne peut pas savoir de quel point il provient. La deuxième composante est perdue, et aucun calcul ne la rend.

:::satz Théorème 11.5 (Sans inverse)
<span class="anker" id="satz-11-5"></span>

S’il existe un vecteur $\mathbf{x}\ne\mathbf{0}$ tel que $\mathbf{A}\mathbf{x}=\mathbf{0}$, alors $\mathbf{A}$ n’est pas inversible.
:::

:::beweis Sans inverse
S’il existait une inverse, on aurait $\mathbf{x}=\mathbf{A}^{-1}\mathbf{A}\mathbf{x}=\mathbf{A}^{-1}\mathbf{0}=\mathbf{0}$, ce qui contredit $\mathbf{x}\ne\mathbf{0}$.
:::

Concrètement : avec $\mathbf{A}\mathbf{x}=\mathbf{0}$, pour tout $\mathbf{u}$, les deux vecteurs différents $\mathbf{u}$ et $\mathbf{u}+\mathbf{x}$ arrivent au même endroit, car $\mathbf{A}(\mathbf{u}+\mathbf{x})=\mathbf{A}\mathbf{u}+\mathbf{A}\mathbf{x}=\mathbf{A}\mathbf{u}$. Deux entrées ayant la même sortie ne peuvent pas être distinguées. Une matrice carrée qui n’est pas inversible est dite __singulière__.

⁠**Exemple de calcul :** Pour $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$, on a $ad-bc=4-4=0$. Effectivement, $\mathbf{x}=(2,\,-1)^{\top}$ est envoyé sur $(2-2,\ 4-4)^{\top}=\mathbf{0}$, et les vecteurs différents $(1,\,1)^{\top}$ et $(3,\,0)^{\top}$ arrivent tous deux en $(3,\,6)^{\top}$.

Pour les données, cela signifie : un calcul qui, par exemple, ne retient du nombre de chambres et du nombre de salons que le nombre total de pièces ne peut plus séparer les deux nombres. Pour les matrices $2\times2$, c’est exactement le cas $ad-bc=0$ de la sous-section [11.3](#stufe-11-3).

⁠**En bref :** Si une matrice envoie un vecteur $\mathbf{x}\ne\mathbf{0}$ sur $\mathbf{0}$, elle perd de l’information et n’a pas d’inverse ; on dit alors qu’elle est singulière.

:::aufgabe Exercice 26 ★ Calculer des inverses
<span class="anker" id="aufg-26"></span>

<ol class="al">

<li>

Calculez les inverses de $\bigl(\begin{smallmatrix}4&3\\1&1\end{smallmatrix}\bigr)$ et de $\bigl(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr)$, et faites chaque fois la vérification.

</li>

<li>

Pour quel nombre $t$ la matrice $\bigl(\begin{smallmatrix}2&t\\4&6\end{smallmatrix}\bigr)$ n’est-elle pas inversible ? Donnez, dans ce cas, un vecteur $\mathbf{x}\ne\mathbf{0}$ tel que $\mathbf{A}\mathbf{x}=\mathbf{0}$.

</li>

<li>

Donnez l’inverse de $\operatorname{diag}(4;\,-1;\,0{,}5)$.

</li>

</ol>

:::loesung
(a) Pour $\bigl(\begin{smallmatrix}4&3\\1&1\end{smallmatrix}\bigr)$, on a $ad-bc=4-3=1$, et l’inverse est $\bigl(\begin{smallmatrix}1&-3\\-1&4\end{smallmatrix}\bigr)$. Vérification : $\bigl(\begin{smallmatrix}4&3\\1&1\end{smallmatrix}\bigr)\bigl(\begin{smallmatrix}1&-3\\-1&4\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}4-3&-12+12\\1-1&-3+4\end{smallmatrix}\bigr)=\mathbf{I}$. Pour $\bigl(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr)$, on a $ad-bc=4-6=-2$, et l’inverse est $-\tfrac12\bigl(\begin{smallmatrix}4&-2\\-3&1\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}-2&1\\1{,}5&-0{,}5\end{smallmatrix}\bigr)$. Vérification : $\bigl(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr)\bigl(\begin{smallmatrix}-2&1\\1{,}5&-0{,}5\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}-2+3&1-1\\-6+6&3-2\end{smallmatrix}\bigr)=\mathbf{I}$.

(b) $ad-bc=12-4t=0$ pour $t=3$. La matrice est alors $\bigl(\begin{smallmatrix}2&3\\4&6\end{smallmatrix}\bigr)$ ; sa deuxième ligne est le double de la première. Le vecteur $(3,\,-2)^{\top}$ est envoyé sur $(6-6,\ 12-12)^{\top}=\mathbf{0}$.

(c) $\operatorname{diag}(4;\,-1;\,0{,}5)^{-1}=\operatorname{diag}(0{,}25;\,-1;\,2)$ : chaque coefficient diagonal est remplacé par son inverse.
:::
:::

:::aufgabe Exercice 27 ★★ Raisonner avec des inverses
<span class="anker" id="aufg-27"></span>

<ol class="al">

<li>

Vérifiez $(\mathbf{C}^{\top})^{-1}=(\mathbf{C}^{-1})^{\top}$ pour $\mathbf{C}=\bigl(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr)$.

</li>

<li>

Soit $\mathbf{A}$ inversible et $\mathbf{A}\mathbf{B}=\mathbf 0$. Montrez qu’alors $\mathbf{B}=\mathbf 0$.

</li>

<li>

Pour les nombres, $ab=0$ entraîne $a=0$ ou $b=0$. Montrez avec $\mathbf{A}=\mathbf{B}=\bigl(\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\bigr)$ que ce n’est pas vrai pour les matrices. Pourquoi cela ne contredit-il pas (b) ?

</li>

</ol>

:::loesung
(a) $\mathbf{C}^{-1}=\bigl(\begin{smallmatrix}-2&1\\1{,}5&-0{,}5\end{smallmatrix}\bigr)$ d’après l’exercice précédent, donc $(\mathbf{C}^{-1})^{\top}=\bigl(\begin{smallmatrix}-2&1{,}5\\1&-0{,}5\end{smallmatrix}\bigr)$. D’autre part, $\mathbf{C}^{\top}=\bigl(\begin{smallmatrix}1&3\\2&4\end{smallmatrix}\bigr)$, avec $ad-bc=-2$, donc $(\mathbf{C}^{\top})^{-1}=-\tfrac12\bigl(\begin{smallmatrix}4&-3\\-2&1\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}-2&1{,}5\\1&-0{,}5\end{smallmatrix}\bigr)$. Les deux coïncident.

(b) On multiplie $\mathbf{A}\mathbf{B}=\mathbf 0$ à gauche par $\mathbf{A}^{-1}$ : $\mathbf{B}=\mathbf{I}\mathbf{B}=\mathbf{A}^{-1}\mathbf{A}\mathbf{B}=\mathbf{A}^{-1}\mathbf 0=\mathbf 0$.

(c) $\mathbf{A}\mathbf{A}=\bigl(\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\bigr)\bigl(\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}0\cdot0+1\cdot0&0\cdot1+1\cdot0\\0&0\end{smallmatrix}\bigr)=\mathbf 0$, bien que $\mathbf{A}\ne\mathbf 0$. Géométriquement, $\mathbf{A}$ envoie le vecteur $\mathbf{e}_2$ sur $\mathbf{e}_1$ et $\mathbf{e}_1$ sur $\mathbf{0}$ ; appliquée deux fois, elle envoie tout sur le vecteur nul. Cela ne contredit pas (b), car $\mathbf{A}$ n’est pas inversible : $ad-bc=0$. La conclusion de (b) a besoin de l’inverse.
:::
:::

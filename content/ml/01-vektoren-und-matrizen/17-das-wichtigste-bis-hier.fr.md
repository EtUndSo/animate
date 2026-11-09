---
title: L’essentiel jusqu’ici
pfad: Informatique / Apprentissage automatique / Fondements mathématiques / Vecteurs et matrices
knoten: Fondements 1 : Vecteurs et matrices
nachschlagen: ja
order: 15211700
summary: Les données comme listes de nombres, les modèles comme applications linéaires
tags: 
lang: fr
---

:::kern L’essentiel jusqu’ici
<ul>

<li>

Un exemple à $d$ caractéristiques est un vecteur colonne $\mathbf{x}\in\mathbb{R}^d$ ; un jeu de données de $N$ exemples est la matrice de données $\mathbf{X}\in\mathbb{R}^{N\times d}$, avec un exemple par ligne.

</li>

<li>

Le produit scalaire $\mathbf{u}^{\top}\mathbf{v}=\sum_ju_jv_j$ est une somme pondérée et une comparaison avec un motif ; la somme pondérée $\mathbf{w}^{\top}\mathbf{x}$ est la règle linéaire la plus générale à une seule sortie.

</li>

<li>

Les normes mesurent la grandeur : $\lVert\mathbf{x}\rVert_2=\sqrt{\mathbf{x}^{\top}\mathbf{x}}$, $\lVert\mathbf{x}\rVert_1=\sum_j|x_j|$, $\lVert\mathbf{x}\rVert_\infty=\max_j|x_j|$ ; la valeur efficace est $\lVert\mathbf{x}\rVert/\sqrt n$. Les distances $\lVert\mathbf{u}-\mathbf{v}\rVert$ dépendent des unités ; la standardisation les en rend indépendantes.

</li>

<li>

$|\mathbf{u}^{\top}\mathbf{v}|\le\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert$ ; l’angle est donné par $\cos\varphi=\mathbf{u}^{\top}\mathbf{v}/(\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert)$, orthogonal signifie $\mathbf{u}^{\top}\mathbf{v}=0$.

</li>

<li>

$\mathbf{A}\mathbf{x}$ est une liste de produits scalaires (vue par lignes) et une combinaison linéaire des colonnes (vue par colonnes) ; $\mathbf{X}\mathbf{w}$ donne toutes les prédictions à la fois.

</li>

<li>

Toute application linéaire est une matrice, dont les colonnes sont les images des vecteurs unitaires ; affine signifie $\mathbf{A}\mathbf{x}+\mathbf{b}$.

</li>

<li>

$\mathbf{A}\mathbf{B}$ signifie « d’abord $\mathbf{B}$, puis $\mathbf{A}$ » ; le produit est associatif, non commutatif ; des étages linéaires enchaînés forment une seule matrice.

</li>

<li>

$(\mathbf{A}\mathbf{B})^{\top}=\mathbf{B}^{\top}\mathbf{A}^{\top}$ ; $\mathbf{X}\mathbf{X}^{\top}$ contient tous les produits scalaires des exemples, $\mathbf{X}^{\top}\mathbf{X}=\sum_i\mathbf{x}_i\mathbf{x}_i^{\top}$ ceux des caractéristiques.

</li>

<li>

$(\mathbf{A}\mathbf{B})^{-1}=\mathbf{B}^{-1}\mathbf{A}^{-1}$ ; $\mathbf{A}\mathbf{x}=\mathbf{y}$ n’a aucune solution, une seule ou une infinité, et a une solution si et seulement si $\mathbf{y}$ appartient à l’espace des colonnes.

</li>

<li>

$\dim\ker\mathbf{A}+\operatorname{rg}\mathbf{A}=n$ ; $\mathbf{A}\mathbf{x}=\mathbf{y}$ a une solution si et seulement si $\operatorname{rg}(\mathbf{A}\,|\,\mathbf{y})=\operatorname{rg}\mathbf{A}$, et celle-ci est alors unique si et seulement si $\operatorname{rg}\mathbf{A}=n$ ; des caractéristiques dépendantes abaissent le rang et rendent les poids ambigus.

</li>

<li>

$\det\mathbf{A}$ est le facteur de volume algébrique, $\det(\mathbf{A}\mathbf{B})=\det\mathbf{A}\det\mathbf{B}$, et $\mathbf{A}$ est inversible si et seulement si $\det\mathbf{A}\ne0$.

</li>

<li>

$\odot$ multiplie coefficient par coefficient ; les tenseurs sont des tableaux de nombres à un nombre quelconque d’axes.

</li>

</ul>
:::

:::merke La réponse en trois phrases
<ol>

<li>

Un jeu de données est une matrice dont les lignes contiennent les exemples sous forme de vecteurs, et la ressemblance, la distance et la grandeur sont des produits scalaires et des normes de ces vecteurs, qui dépendent des unités choisies.

</li>

<li>

Une règle linéaire est fixée par les images des vecteurs unitaires, c’est donc une matrice, et le produit matrice-vecteur l’applique à tous les exemples à la fois.

</li>

<li>

Composer des applications revient à multiplier leurs matrices, et ce sont le rang, le noyau et le déterminant qui décident si une application peut être inversée : ils montrent si des directions se perdent en chemin.

</li>

</ol>
:::

**Un principe derrière tous les résultats.** Presque tout dans ce chapitre découle de deux opérations : on additionne des vecteurs et on les multiplie par des nombres, et les applications linéaires conservent exactement ces deux opérations.

| Résultat | D’où il vient |
|---|---|
| Somme pondérée, comparaison avec un motif | produit scalaire : produits à la même position, additionnés (section [2](das-skalarprodukt.html#stufe-2)) |
| Longueur, distance, angle | tous issus du produit scalaire : $\lVert\mathbf{x}\rVert^2=\mathbf{x}^{\top}\mathbf{x}$, [(4.1)](abstande-und-einheiten.html#gl-4-1), Cauchy-Schwarz (sections [3](normen-die-groe-eines-vektors.html#stufe-3) à [5](winkel-und-ahnlichkeit.html#stufe-5)) |
| Les distances dépendent des unités | chaque caractéristique intervient avec sa valeur numérique au carré (section [4](abstande-und-einheiten.html#stufe-4)) |
| Vues par lignes et par colonnes | la même somme double, ordonnée différemment (section [7](das-matrix-vektor-produkt.html#stufe-7)) |
| Matrice d’une application linéaire | $\mathbf{x}=\sum_jx_j\mathbf{e}_j$, et l’application conserve les combinaisons linéaires (section [8](lineare-abbildungen.html#stufe-8)) |
| Produit matriciel, non commutatif | matrice de la composition (section [9](das-matrixprodukt.html#stufe-9)) |
| Matrice de Gram | tableau des produits scalaires, $\mathbf{X}\mathbf{X}^{\top}$ et $\mathbf{X}^{\top}\mathbf{X}$ (section [10](transponierte-symmetrie-und-gram-matrix.html#stufe-10)) |
| Pas d’inverse si $\mathbf{A}\mathbf{x}=\mathbf{0}$, $\mathbf{x}\ne\mathbf{0}$ | deux entrées, une sortie : information perdue (section [11](einheitsmatrix-und-inverse.html#stufe-11)) |
| Aucune, une, une infinité de solutions | avec deux solutions, toute la droite qui passe par elles est solution (section [12](lineare-gleichungssysteme.html#stufe-12)) |
| Poids ambigus | les vecteurs du noyau ne changent pas $\mathbf{X}\mathbf{w}$ (section [13](unabhangigkeit-basis-und-rang.html#stufe-13)) |
| $\det(\mathbf{A}\mathbf{B})=\det\mathbf{A}\det\mathbf{B}$ | les facteurs de volume se multiplient lors de la composition (section [14](die-determinante.html#stufe-14)) |

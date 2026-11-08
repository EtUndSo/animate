---
title: L’essentiel jusqu’ici
pfad: Informatique / Apprentissage automatique / Fondements mathématiques / Projection, valeurs propres et décompositions
knoten: Fondements 2 : Projection, valeurs propres et décompositions
nachschlagen: ja
order: 15221400
summary: Points les plus proches, directions naturelles et les briques d’une matrice
tags: 
lang: fr
---

:::kern L’essentiel jusqu’ici
<ul>

<li>

Vecteurs orthonormés : $\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}$ ; les coordonnées sont des produits scalaires $c_i=\mathbf{q}_i^{\top}\mathbf{x}$ ; les matrices orthogonales conservent les longueurs et les angles. Si $\mathbf{Q}$ n’est pas carrée, $\mathbf{Q}\mathbf{Q}^{\top}\ne\mathbf{I}$.

</li>

<li>

Projection sur une droite : $\hat{\mathbf{y}}=\frac{\mathbf{a}^{\top}\mathbf{y}}{\mathbf{a}^{\top}\mathbf{a}}\,\mathbf{a}$ ; le reste est perpendiculaire à $\mathbf{a}$, et $\hat{\mathbf{y}}$ est le point le plus proche. Les matrices de projection vérifient $\mathbf{P}^2=\mathbf{P}$, les matrices de projection orthogonale en outre $\mathbf{P}^{\top}=\mathbf{P}$.

</li>

<li>

Meilleure solution approchée : le résidu $\mathbf{r}=\mathbf{y}-\mathbf{A}\hat{\mathbf{x}}$ est perpendiculaire à l’espace des colonnes, donc $\mathbf{A}^{\top}\mathbf{A}\hat{\mathbf{x}}=\mathbf{A}^{\top}\mathbf{y}$ ; elle est unique exactement lorsque les colonnes sont indépendantes.

</li>

<li>

Projection sur un sous-espace : $\mathbf{P}=\mathbf{A}(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}=\mathbf{Q}\mathbf{Q}^{\top}$ ; Gram-Schmidt fournit $\mathbf{A}=\mathbf{Q}\mathbf{R}$, et $\mathbf{R}\hat{\mathbf{x}}=\mathbf{Q}^{\top}\mathbf{y}$.

</li>

<li>

Les formes quadratiques $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}$ ne dépendent que de la partie symétrique ; on reconnaît cuvette, gouttière et selle en complétant le carré.

</li>

<li>

Valeurs propres : $\mathbf{A}\mathbf{v}=\lambda\mathbf{v}$, $\det(\mathbf{A}-\lambda\mathbf{I})=0$ ; trace $=\sum\lambda_i$, $\det=\prod\lambda_i$ ; les rotations ont des valeurs propres complexes.

</li>

<li>

$\mathbf{A}=\mathbf{S}\boldsymbol{\Lambda}\mathbf{S}^{-1}$ découple, $\mathbf{A}^k=\mathbf{S}\boldsymbol{\Lambda}^k\mathbf{S}^{-1}$. Cas symétrique : $\mathbf{A}=\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top}$ avec des $\lambda_i$ réels et des axes principaux perpendiculaires, demi-axes $1/\sqrt{\lambda_i}$.

</li>

<li>

Définie positive $\Leftrightarrow$ toutes les valeurs propres $>0$ $\Leftrightarrow$ tous les pivots $>0$ $\Leftrightarrow$ tous les mineurs principaux dominants $>0$ ; $\mathbf{A}^{\top}\mathbf{A}$ est semi-définie positive ; décomposition de Cholesky $\mathbf{A}=\mathbf L\mathbf L^{\top}$.

</li>

<li>

Décomposition en valeurs singulières $\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}=\sum_jd_j\mathbf{u}_j\mathbf{v}_j^{\top}$ pour toute matrice : tourner, étirer, tourner ; les $d_j^2$ sont les valeurs propres de $\mathbf{A}^{\top}\mathbf{A}$, $\lVert\mathbf{A}\rVert_2=d_1$.

</li>

<li>

$\lVert\mathbf{A}\rVert_F^2=\sum_jd_j^2$ ; $\mathbf{A}_k$ est la meilleure approximation de rang $k$, avec l’erreur $d_{k+1}$ en norme spectrale.

</li>

<li>

$\mathbf{A}^+=\mathbf{V}\mathbf{D}^+\mathbf{U}^{\top}$ fournit la meilleure solution approchée la plus courte ; cas particuliers : $(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}$ et $\mathbf{A}^{\top}(\mathbf{A}\mathbf{A}^{\top})^{-1}$.

</li>

<li>

$\kappa(\mathbf{A})=d_1/d_n$ borne l’amplification des erreurs relatives ; $1/\kappa$ est la distance relative à la singularité ; $\kappa(\mathbf{A}^{\top}\mathbf{A})=\kappa(\mathbf{A})^2$.

</li>

</ul>
:::

:::merke La réponse en trois phrases
<ol>

<li>

Un système d’équations sans solution se résout au mieux en projetant perpendiculairement le second membre sur l’espace des colonnes : le résidu est alors perpendiculaire à toutes les colonnes, ce qui donne les équations normales, et d’après Pythagore, aucun autre point n’est plus proche.

</li>

<li>

Les vecteurs propres sont les directions qu’une matrice ne fait qu’étirer ; dans leur base, la matrice devient diagonale, et pour les matrices symétriques, ils forment un repère orthogonal sur lequel on lit l’allure de toute forme quadratique.

</li>

<li>

Toute matrice est une somme, ordonnée par taille, de briques $d_j\mathbf{u}_j\mathbf{v}_j^{\top}$ de rang $1$ : les $k$ premières donnent la meilleure approximation de rang $k$, et le rapport $d_1/d_n$ indique à quel point des erreurs dans les données peuvent fausser la solution.

</li>

</ol>
:::

**Un principe derrière tous les résultats.** Presque tout dans ce chapitre découle d’un seul principe : dans un repère orthogonal, un carré de longueur se décompose, d’après Pythagore, en parts indépendantes, et le plus court chemin vers une droite, un plan ou un sous-espace est le chemin perpendiculaire.

| Résultat | D’où il vient |
|---|---|
| Coordonnées comme produits scalaires, $\mathbf{Q}^{-1}=\mathbf{Q}^{\top}$ | axes perpendiculaires de longueur $1$ : les termes croisés disparaissent (section [1](orthonormalbasen-und-orthogonale-matrizen.html#stufe-1)) |
| Point le plus proche sur une droite et sur un sous-espace | Pythagore : reste perpendiculaire plus déplacement dans le sous-espace (sections [2](projektion-auf-eine-gerade.html#stufe-2) et [3](die-beste-naherungslosung.html#stufe-3)) |
| Équations normales | résidu perpendiculaire à chaque colonne : $\mathbf{A}^{\top}\mathbf{r}=\mathbf{0}$ (section [3](die-beste-naherungslosung.html#stufe-3)) |
| Gram-Schmidt et QR | retrancher l’ombre, normaliser le reste perpendiculaire (section [4](projektion-auf-einen-unterraum.html#stufe-4)) |
| Cuvette, gouttière, selle | signes des coefficients d’une somme de carrés (sections [5](quadratische-formen.html#stufe-5) et [8](positiv-definite-matrizen.html#stufe-8)) |
| Découplage par diagonalisation | dans la base propre, chaque coordonnée évolue séparément (section [7](diagonalisierung-und-spektralsatz.html#stufe-7)) |
| Théorème spectral | symétrie : $\mathbf{A}$ peut changer de côté dans le produit scalaire, le supplémentaire orthogonal d’un vecteur propre reste stable (section [7](diagonalisierung-und-spektralsatz.html#stufe-7)) |
| Décomposition en valeurs singulières de toute matrice | théorème spectral pour la matrice symétrique $\mathbf{A}^{\top}\mathbf{A}$ (section [9](die-singularwertzerlegung.html#stufe-9)) |
| Meilleure approximation de rang $k$ | le noyau d’une matrice de rang $k$ rencontre les $k+1$ directions les plus étirées (section [10](naherung-durch-matrizen-von-kleinem-rang.html#stufe-10)) |
| Meilleure solution approchée la plus courte | Pythagore dans les coordonnées des vecteurs singuliers : les parts dans le noyau ne font qu’allonger (section [11](die-pseudoinverse.html#stufe-11)) |
| Conditionnement | étirement maximal et minimal $d_1$ et $d_n$ (section [12](die-konditionszahl.html#stufe-12)) |

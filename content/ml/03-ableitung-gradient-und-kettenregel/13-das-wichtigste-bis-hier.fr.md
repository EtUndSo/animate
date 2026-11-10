---
title: L’essentiel jusqu’ici
pfad: Informatique / Apprentissage automatique / Fondements mathématiques / Dérivée, gradient et règle de dérivation en chaîne
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Chapitre 3 : Dérivée, gradient et règle de dérivation en chaîne
nachschlagen: ja
order: 15231300
summary: Comment un nombre réagit à ses entrées : de la tangente au mode inverse
tags: 
lang: fr
---

:::kern L’essentiel jusqu’ici
<ul>

<li>

Dérivée : $f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}$ ; près de $x$, $f(x+h)\approx f(x)+f'(x)h$, avec une erreur qui disparaît plus vite que $h$. Avec la dérivée seconde : $f(x+h)\approx f(x)+f'(x)h+\tfrac12f''(x)h^2$.

</li>

<li>

Règle de dérivation en chaîne : $(f\circ g)'(x)=f'(g(x))\,g'(x)$ ; pour de longues chaînes, le produit de tous les facteurs. Fonction logistique : $\sigma'=\sigma(1-\sigma)\le\tfrac14$.

</li>

<li>

Gradient $\nabla f\in\mathbb{R}^d$ en colonne ; $f(\mathbf{x}+\mathbf{h})\approx f(\mathbf{x})+\nabla f(\mathbf{x})^{\top}\mathbf{h}$ si $f$ est différentiable ; les dérivées partielles seules ne suffisent pas.

</li>

<li>

Dérivée directionnelle $D_{\mathbf{u}}f=\nabla f^{\top}\mathbf{u}$ ; plus forte montée dans la direction $\nabla f$, avec la pente $\lVert\nabla f\rVert$ (Cauchy-Schwarz) ; $\nabla f$ est perpendiculaire aux lignes de niveau ; $-\nabla f$ ne pointe vers le point le plus bas que pour des lignes de niveau rondes.

</li>

<li>

Matrice jacobienne $\mathbf{J}_{\mathbf{g}}\in\mathbb{R}^{m\times n}$, une ligne par sortie : $\mathbf{g}(\mathbf{x}+\mathbf{h})\approx\mathbf{g}(\mathbf{x})+\mathbf{J}_{\mathbf{g}}\mathbf{h}$ ; pour $\mathbf{A}\mathbf{x}+\mathbf{b}$, elle vaut $\mathbf{A}$, pour des fonctions appliquées terme à terme, elle est diagonale.

</li>

<li>

Règle de dérivation en chaîne : $\mathbf{J}_{\mathbf f\circ\mathbf{g}}=\mathbf{J}_{\mathbf f}\mathbf{J}_{\mathbf{g}}$, composante par composante une somme sur tous les chemins ; $\nabla(f\circ\mathbf{g})=\mathbf{J}_{\mathbf{g}}^{\top}\nabla f$.

</li>

<li>

$\nabla(\mathbf{a}^{\top}\mathbf{x})=\mathbf{a}$, $\nabla(\mathbf{x}^{\top}\mathbf{A}\mathbf{x})=(\mathbf{A}+\mathbf{A}^{\top})\mathbf{x}$, $\nabla\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert^2=-2\mathbf{A}^{\top}(\mathbf{y}-\mathbf{A}\mathbf{x})$, $\nabla_{\mathbf{A}}(\mathbf{u}^{\top}\mathbf{A}\mathbf{v})=\mathbf{u}\mathbf{v}^{\top}$ ; à rebours à travers $\mathbf{y}=\mathbf{A}\mathbf{x}$ avec $F=f(\mathbf{A}\mathbf{x})$ : $\nabla_{\mathbf{A}}F=\nabla f(\mathbf{y})\,\mathbf{x}^{\top}$, $\nabla_{\mathbf{x}}F=\mathbf{A}^{\top}\nabla f(\mathbf{y})$.

</li>

<li>

Matrice hessienne $\mathbf{H}_f$, symétrique d’après Schwarz ; $f(\mathbf{x}+\mathbf{h})\approx f+\nabla f^{\top}\mathbf{h}+\tfrac12\mathbf{h}^{\top}\mathbf{H}_f\mathbf{h}$ ; la courbure dans la direction $\mathbf{u}$ est $\mathbf{u}^{\top}\mathbf{H}_f\mathbf{u}$, comprise entre la plus petite et la plus grande valeur propre.

</li>

<li>

Graphe de calcul : opérations de base, évaluation avant avec valeurs stockées, dérivées locales sur les arêtes.

</li>

<li>

Mode direct : valeurs tangentes, une passe par direction ($\mathbf{J}\dot{\mathbf{x}}$). Mode inverse : adjoints $\bar a=\sum\bar b\,\partial b/\partial a$ à partir de $\bar f=1$, une passe pour le gradient complet, coût : un petit multiple d’une évaluation, prix : la mémoire.

</li>

<li>

Numérique : erreur de la différence avant $\approx\tfrac12f''h$, de la différence centrée $\approx\tfrac16f'''h^2$ ; l’arrondi croît comme $\varepsilon_{\mathrm M}/h$, d’où la courbe en V ; vérification du gradient avec l’erreur relative : au-dessus de $10^{-2}$ faux, en dessous de $10^{-7}$ bon.

</li>

</ul>
:::

:::merke La réponse en trois phrases
<ol>

<li>

C’est son approximation linéaire qui dit comment un nombre réagit à de petites modifications de ses entrées : chaque entrée apporte sa dérivée partielle multipliée par sa variation, et les contributions s’additionnent pour donner le produit scalaire avec le gradient.

</li>

<li>

D’après l’inégalité de Cauchy-Schwarz, ce produit scalaire est, pour des pas de longueur fixe, le plus grand dans la direction du gradient, qui pointe donc dans la direction de plus forte montée et est perpendiculaire aux lignes de niveau.

</li>

<li>

Si le nombre résulte d’une longue chaîne d’étapes de calcul, sa dérivée est un produit de matrices jacobiennes, donc une somme sur tous les chemins, et le mode inverse calcule ce produit en partant du nombre, avec des vecteurs lignes, de sorte qu’il fournit toutes les dérivées à la fois pour un petit multiple du coût d’une seule évaluation.

</li>

</ol>
:::

**Un principe derrière tous les résultats.** Presque tout dans ce chapitre découle d’un principe : suffisamment près d’un point, toute fonction différentiable est linéaire. Dérivée, gradient et matrice jacobienne sont cette approximation linéaire, la règle de dérivation en chaîne monte en série des approximations linéaires en multipliant leurs matrices, et le mode direct et le mode inverse sont deux façons de parenthéser ce produit.

| Résultat | D’où il vient |
|---|---|
| Dérivée et tangente | la seule droite dont l’erreur disparaît plus vite que $h$ (section [1](die-ableitung.html#stufe-1)) |
| Règle du produit | le petit carré du coin $\Delta u\,\Delta v$ est petit d’ordre deux (section [1.4](die-ableitung.html#stufe-1-4)) |
| Règle de dérivation en chaîne à une variable | chaque étage transmet les petites variations avec son facteur (section [2](die-kettenregel.html#stufe-2)) |
| Gradient et plan tangent | les effets de petites variations s’additionnent (section [3](partielle-ableitungen-und-der-gradient.html#stufe-3)) |
| Plus forte montée | Cauchy-Schwarz pour $\nabla f^{\top}\mathbf{u}$ (section [4](richtungsableitung-und-steilster-anstieg.html#stufe-4)) |
| Gradient perpendiculaire à la ligne de niveau | le long de la ligne de niveau, la pente est nulle (sections [4](richtungsableitung-und-steilster-anstieg.html#stufe-4) et [6](die-kettenregel-fur-mehrere-variablen.html#stufe-6)) |
| Matrice jacobienne | la matrice de l’approximation linéaire d’une fonction à valeurs vectorielles (section [5](die-jacobi-matrix.html#stufe-5)) |
| Règle de dérivation en chaîne comme produit matriciel, somme sur les chemins | approximations linéaires montées en série (section [6](die-kettenregel-fur-mehrere-variablen.html#stufe-6)) |
| Identités matricielles, règle arrière | règle de dérivation en chaîne composante par composante, dans une convention de disposition fixe (section [7](ableiten-nach-vektoren-und-matrizen.html#stufe-7)) |
| Matrice hessienne et courbure | dérivée seconde le long d’une droite, valeurs propres d’une forme quadratique (section [8](die-hesse-matrix-und-die-quadratische-naherung.html#stufe-8)) |
| Mode inverse | regrouper les chemins selon leur première arête, réutiliser les sommes partielles ; parenthésage par la gauche (sections [9](rechengraphen.html#stufe-9) et [10](automatische-differentiation.html#stufe-10)) |
| Différence centrée, courbe en V | les termes de Taylor pairs s’éliminent ; les erreurs d’arrondi croissent comme $1/h$ (section [11](numerische-ableitung-und-gradientenprufung.html#stufe-11)) |

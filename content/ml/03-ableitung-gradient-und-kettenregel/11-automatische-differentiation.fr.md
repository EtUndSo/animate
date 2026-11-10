---
title: Différentiation automatique
pfad: Informatique / Apprentissage automatique / Fondements mathématiques / Dérivée, gradient et règle de dérivation en chaîne
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Chapitre 3 : Dérivée, gradient et règle de dérivation en chaîne
nachschlagen: ja
order: 15231100
summary: Avec le graphe de calcul, on peut calculer des dérivées mécaniquement, sans transformer de formules, et exactement, aux arrondis des opérations de base près.
tags: différentiation automatique, mode direct, valeur tangente, adjoint, mode inverse
lang: fr
---

<span class="anker" id="stufe-10"></span>

:::zweck
Avec le graphe de calcul, on peut calculer des dérivées mécaniquement, sans transformer de formules, et exactement, aux arrondis des opérations de base près. C’est ce qu’on appelle la différentiation automatique. Il y a deux façons de combiner les dérivées locales : vers l’avant, au même rythme que le calcul, ou à rebours, du résultat vers les entrées. Le mode inverse fournit la dérivée d’un nombre par rapport à toutes ses entrées en une seule passe, et cette section montre pourquoi cela coûte si peu.
:::

### Ce qu’est la différentiation automatique

<span class="anker" id="stufe-10-1"></span>

Il y a trois façons d’obtenir la dérivée d’un calcul. On peut transformer la formule à l’aide des règles ; c’est la dérivation symbolique, et d’après la section [9.1](rechengraphen.html#stufe-9-1), les formules grossissent alors rapidement. On peut évaluer la fonction en deux points proches et former un taux d’accroissement ; c’est la dérivation numérique, elle n’est qu’approximativement juste, et la section [11](numerische-ableitung-und-gradientenprufung.html#stufe-11) étudie son erreur. La troisième façon réunit les avantages des deux autres.

:::definition Définition 10.1 (Différentiation automatique)
<span class="anker" id="satz-10-1"></span>

La __différentiation automatique__ calcule les dérivées d’un calcul en appliquant la règle de dérivation en chaîne à son graphe de calcul : elle évalue les dérivées locales avec les nombres du calcul et les combine selon la somme sur les chemins.
:::

La différentiation automatique calcule avec des nombres, non avec des formules, et c’est pourquoi aucune expression ne grossit. Elle n’approche rien : le résultat est la dérivée exacte, faussée seulement par l’arrondi des différentes étapes de calcul. Et elle fonctionne pour tout programme composé d’opérations de base, même avec des boucles et des branchements, car pour les entrées données, le programme fournit un graphe de calcul. Le calcul pas à pas de l’exemple de la section [9.1](rechengraphen.html#stufe-9-1) était déjà de la différentiation automatique.

::::beispiel [Exemple de calcul]
Pour [(9.1)](rechengraphen.html#gl-9-1), la section précédente a assemblé les dérivées $5$, $8$ et $3$ à partir des dérivées locales, sans développer ni dériver la formule de $f$. C’était de la différentiation automatique, même si ce n’était pas encore avec une méthode fixe pour l’ordre du calcul. Les deux sous-sections suivantes donnent cet ordre.
::::

⁠**En bref :** La différentiation automatique applique la règle de dérivation en chaîne au graphe de calcul, avec des nombres ; elle est exacte aux arrondis près et n’a besoin d’aucune formule.

### Le mode direct

<span class="anker" id="stufe-10-2"></span>

La première possibilité suit le calcul lui-même. On fixe dans quelle direction on modifie les entrées, et l’on transporte avec chaque nœud, à côté de sa valeur, la vitesse à laquelle il change lors de cette modification.

:::definition Définition 10.2 (Mode direct)
<span class="anker" id="satz-10-2"></span>

En __mode direct__, on choisit une direction $\dot{\mathbf{x}}\in\mathbb{R}^n$ pour les entrées et l’on calcule pour chaque nœud $b$, à côté de sa valeur, le nombre

<span class="anker" id="gl-10-1"></span>
$$\dot b=\sum_{a\text{ prédécesseur de }b}\frac{\partial b}{\partial a}\,\dot a , \tag{10.1}$$

dans le même ordre que les valeurs. Ce nombre s’appelle la __valeur tangente__ de $b$ ; les nœuds d’entrée reçoivent comme valeurs tangentes les composantes de $\dot{\mathbf{x}}$.
:::

Le nom rappelle la tangente de la section [1.2](die-ableitung.html#stufe-1-2), mais il s’agit d’un nombre : la valeur tangente $\dot b$ est le taux de variation du nœud $b$ lorsqu’on déplace les entrées le long de la droite $\mathbf{x}+t\,\dot{\mathbf{x}}$. La formule [(10.1)](#gl-10-1) est la règle de dérivation en chaîne le long de cette courbe, [(6.4)](die-kettenregel-fur-mehrere-variablen.html#gl-6-4), pour un seul nœud. Après une passe, on trouve au résultat $\dot f=\nabla f(\mathbf{x})^{\top}\dot{\mathbf{x}}$. Si le calcul a plusieurs sorties, on y trouve le produit $\mathbf{J}\,\dot{\mathbf{x}}$ de la matrice jacobienne par la direction. Avec $\dot{\mathbf{x}}=\mathbf{e}_j$, une passe fournit la dérivée partielle par rapport à $x_j$ et, s’il y a plusieurs sorties, la colonne $j$ de la matrice jacobienne. Pour le gradient complet d’une fonction de $n$ variables, le mode direct a donc besoin de $n$ passes.

::::beispiel [Exemple de calcul]
Pour [(9.1)](rechengraphen.html#gl-9-1) au point $(1,\,2,\,3)$ dans la direction $\dot{\mathbf{x}}=\mathbf{e}_2=(0,\,1,\,0)^{\top}$, on obtient le tableau [5](#tab-5). Au résultat, on trouve $\dot f=8=\partial f/\partial x_2$. Pour $\partial f/\partial x_1$ et $\partial f/\partial x_3$, il faut deux passes de plus, avec $\mathbf{e}_1$ et $\mathbf{e}_3$.

<span class="anker" id="tab-5"></span>

**Tableau 5 :** Le mode direct pour $f=(x_1+x_2)\,(x_2+x_3)$ au point $(1,\,2,\,3)$ dans la direction $\dot{\mathbf{x}}=\mathbf{e}_2$.

| Nœud | Calcul | Valeur | Valeur tangente |  |
|---|---|---|---|---|
| $x_1$ | entrée | $1$ | $\dot x_1$ | $0$ |
| $x_2$ | entrée | $2$ | $\dot x_2$ | $1$ |
| $x_3$ | entrée | $3$ | $\dot x_3$ | $0$ |
| $v_1$ | $x_1+x_2$ | $3$ | $\dot v_1=\dot x_1+\dot x_2$ | $1$ |
| $v_2$ | $x_2+x_3$ | $5$ | $\dot v_2=\dot x_2+\dot x_3$ | $1$ |
| $f$ | $v_1\cdot v_2$ | $15$ | $\dot f=v_2\,\dot v_1+v_1\,\dot v_2$ | $5+3=8$ |
::::

⁠**En bref :** Le mode direct transporte avec chaque valeur sa valeur tangente ; une passe fournit la dérivée dans une direction, donc une colonne de la matrice jacobienne.

:::hintergrund Le mode direct avec des nombres duaux
Le mode direct peut être vu comme un calcul avec des nombres étendus. On calcule avec des couples $a+\dot a\,\varepsilon$, où $\varepsilon$ est un nouveau symbole soumis à la seule règle $\varepsilon^2=0$ ; de tels nombres s’appellent des nombres duaux. L’addition et la multiplication se font comme d’habitude : $(a+\dot a\varepsilon)+(b+\dot b\varepsilon)=(a+b)+(\dot a+\dot b)\varepsilon$ et $(a+\dot a\varepsilon)(b+\dot b\varepsilon)=ab+(a\dot b+\dot ab)\varepsilon$, car le terme $\dot a\dot b\varepsilon^2$ disparaît. Le facteur devant $\varepsilon$ suit donc exactement la règle de la somme et la règle du produit. Pour [(9.1)](rechengraphen.html#gl-9-1), on pose $x_1=1$, $x_2=2+\varepsilon$, $x_3=3$ et l’on obtient $(3+\varepsilon)(5+\varepsilon)=15+8\varepsilon+\varepsilon^2=15+8\varepsilon$ : la valeur et la dérivée par rapport à $x_2$ en un seul calcul. Pour une fonction $\varphi$ d’une variable, on pose $\varphi(a+\dot a\varepsilon)=\varphi(a)+\varphi'(a)\,\dot a\,\varepsilon$, ce qui correspond à l’approximation linéaire, dans laquelle le carré du petit terme ne joue aucun rôle. Les nombres duaux ont été introduits par William Kingdon Clifford en 1873, bien avant tout ordinateur.
:::

### Le mode inverse

<span class="anker" id="stufe-10-3"></span>

Pour une entrée donnée, le mode direct demande dans quelle mesure chaque nœud en dépend. Le mode inverse pose la question inverse : dans quelle mesure le résultat dépend-il de chaque nœud ? On peut répondre à cette question à rebours, à partir du résultat, et à la fin on connaît la réponse pour toutes les entrées à la fois.

:::definition Définition 10.3 (Mode inverse)
<span class="anker" id="satz-10-3"></span>

L’__adjoint__ d’un nœud $a$ est $\bar a=\partial f/\partial a$, la dérivée du résultat par rapport à ce nœud, lorsqu’on le considère comme une entrée du reste du calcul. En __mode inverse__, on effectue d’abord l’évaluation avant et l’on stocke toutes les valeurs. Puis on pose $\bar f=1$ et l’on calcule pour les nœuds, dans l’ordre inverse,

<span class="anker" id="gl-10-2"></span>
$$\bar a=\sum_{b\text{ successeur de }a}\bar b\,\frac{\partial b}{\partial a}. \tag{10.2}$$

Les adjoints des nœuds d’entrée forment le gradient $\nabla f(\mathbf{x})$.
:::

L’ordre inverse est nécessaire, parce que chaque nœud a besoin des adjoints de ses successeurs, et ceux-ci viennent après lui dans le calcul. Chaque adjoint a la même forme que son nœud ; si un nœud est un vecteur ou une matrice, l’adjoint est lui aussi un vecteur ou une matrice, comme pour la règle arrière du produit matriciel de la section [7.6](ableiten-nach-vektoren-und-matrizen.html#stufe-7-6).

:::satz Théorème 10.4 (Le mode inverse fournit le gradient)
<span class="anker" id="satz-10-4"></span>

Pour tout nœud $a$, le nombre $\bar a$ calculé selon [(10.2)](#gl-10-2) est la somme, sur tous les chemins allant de $a$ au résultat, du produit des dérivées locales le long de chaque chemin. Pour les nœuds d’entrée, c’est, d’après la section [9.4](rechengraphen.html#stufe-9-4), la dérivée partielle de $f$.
:::

:::beweis Le mode inverse fournit le gradient
On classe tous les chemins allant de $a$ au résultat selon leur première arête. Chaque chemin commence par une arête vers un successeur $b$ et se poursuit ensuite comme chemin de $b$ au résultat. Les chemins qui passent par $b$ apportent donc ensemble $\frac{\partial b}{\partial a}$ fois la somme sur tous les chemins de $b$ au résultat. Si cette somme est déjà correctement calculée pour tous les successeurs, c’est-à-dire égale à $\bar b$, la somme pour $a$ est exactement [(10.2)](#gl-10-2). Pour le résultat lui-même, l’énoncé est vrai avec $\bar f=1$, le chemin vide. Comme on calcule à rebours, les successeurs passent toujours avant $a$, et l’énoncé se transmet nœud par nœud jusqu’aux entrées.
:::

::::beispiel [Exemple de calcul]
Pour [(9.1)](rechengraphen.html#gl-9-1) au point $(1,\,2,\,3)$, on obtient le tableau [6](#tab-6) et la Fig. [19](#abb-19). Une seule passe arrière fournit les trois dérivées partielles $(5,\,8,\,3)$, que le mode direct n’obtenait qu’avec trois passes.

<span class="anker" id="tab-6"></span>

**Tableau 6 :** Le mode inverse pour $f=(x_1+x_2)\,(x_2+x_3)$ au point $(1,\,2,\,3)$ ; les valeurs proviennent du tableau [3](rechengraphen.html#tab-3).

| Nœud | Calcul d’après [(10.2)](#gl-10-2) | Adjoint |
|---|---|---|
| $f$ | départ | $\bar f=1$ |
| $v_2$ | $\bar f\cdot\partial f/\partial v_2=1\cdot v_1$ | $\bar v_2=3$ |
| $v_1$ | $\bar f\cdot\partial f/\partial v_1=1\cdot v_2$ | $\bar v_1=5$ |
| $x_3$ | $\bar v_2\cdot1$ | $\bar x_3=3$ |
| $x_2$ | $\bar v_1\cdot1+\bar v_2\cdot1$ | $\bar x_2=5+3=8$ |
| $x_1$ | $\bar v_1\cdot1$ | $\bar x_1=5$ |

:::abbildung ml/k3rueckwaerts 19
Valeurs avant et arrière dans le graphe de calcul de $f=(x_1+x_2)\,(x_2+x_3)$ au point $(1,\,2,\,3)$ : en vert les valeurs de l’évaluation avant, en rouge les adjoints, en gris sur les arêtes les dérivées locales. Lors du calcul à rebours, chaque adjoint remonte les flèches en sens inverse et est multiplié par la dérivée locale de l’arête ; là où deux arêtes partent d’un même nœud, comme pour $x_2$, les contributions s’additionnent.
:::
::::

⁠**En bref :** Le mode inverse calcule d’abord vers l’avant en stockant toutes les valeurs, puis, à rebours, les adjoints $\bar a=\sum\bar b\,\partial b/\partial a$ ; une passe arrière fournit le gradient complet.

### Motifs dans le flux arrière

<span class="anker" id="stufe-10-4"></span>

D’après le tableau [4](rechengraphen.html#tab-4), les opérations de base se comportent, lors du calcul à rebours, de manière simple et récurrente. Qui connaît ces motifs peut écrire les adjoints presque sans calcul et repérer vite des erreurs dans des démonstrations.

:::satz Théorème 10.5 (Motifs des opérations de base)
<span class="anker" id="satz-10-5"></span>

<ol class="al">

<li>

Une *addition* transmet son adjoint tel quel à chaque entrée.

</li>

<li>

Une *multiplication* transmet à chaque entrée son adjoint multiplié par la valeur de l’*autre* entrée.

</li>

<li>

Un *maximum* transmet son adjoint en entier à la plus grande entrée ; la plus petite reçoit $0$.

</li>

<li>

Une fonction d’une variable multiplie l’adjoint par sa dérivée locale, donc par $b\,(1-b)$ pour la fonction logistique.

</li>

<li>

Si un nœud est utilisé plusieurs fois, les contributions de tous ses successeurs s’*additionnent*.

</li>

</ol>
:::

Chaque énoncé est [(10.2)](#gl-10-2) avec les dérivées locales du tableau [4](rechengraphen.html#tab-4). De (b) découle une observation utile : si un facteur est mille fois plus grand que l’autre, l’adjoint du plus petit facteur est mille fois plus grand que celui du plus grand. De grandes différences dans les ordres de grandeur des entrées entraînent donc des différences tout aussi grandes dans les dérivées partielles.

::::beispiel [Exemple de calcul]
Dans le tableau [6](#tab-6), la multiplication a interverti les valeurs : $v_1$ a reçu $v_2=5$, $v_2$ a reçu $v_1=3$. Les additions ont transmis ces valeurs telles quelles, et $x_2$, nœud à deux successeurs, a recueilli $5+3=8$. Un exemple avec maximum : pour $f=\max(x_1,x_2)\cdot x_3$ au point $(1,\,2,\,3)$, on a $v=\max(1,2)=2$ et $f=6$. À rebours, $\bar v=x_3=3$ et $\bar x_3=v=2$ ; le maximum transmet $\bar v$ à la plus grande entrée $x_2$, donc $\bar x_2=3$ et $\bar x_1=0$. En effet, une petite modification de $x_1$ ne change pas le résultat tant que $x_1<x_2$.
::::

⁠**En bref :** L’addition distribue, la multiplication intervertit, le maximum aiguille, et aux ramifications on additionne.

### Le coût

<span class="anker" id="stufe-10-5"></span>

Pourquoi le mode inverse est-il si important ? Parce qu’il fournit le gradient d’une fonction ayant un très grand nombre d’entrées pour un coût presque aussi faible que celui de la valeur de la fonction elle-même. La comparaison des méthodes le montre clairement.

Pour le gradient d’une fonction de $n$ variables, le mode direct a besoin de $n$ passes, une par direction d’entrée. Une passe coûte un petit multiple d’une évaluation de $f$, car à chaque opération de base s’ajoute sa valeur tangente. Les taux d’accroissement demandent même $n+1$ ou $2n$ évaluations. Le mode inverse, en revanche, n’a toujours besoin que d’exactement une évaluation avant et d’une passe arrière, quelle que soit la taille de $n$. Dans la passe arrière, chaque arête est utilisée exactement une fois, avec une multiplication et une addition. Elle ne coûte donc, elle aussi, qu’un petit multiple de l’évaluation avant.

:::satz Théorème 10.6 (Coût des modes direct et inverse)
<span class="anker" id="satz-10-6"></span>

Soit $\mathbf{g}:\mathbb{R}^n\to\mathbb{R}^m$ donnée par un graphe de calcul fait d’opérations de base, et supposons qu’une évaluation coûte le temps $T$. Alors la matrice jacobienne complète coûte environ $c\cdot n\cdot T$ en mode direct et environ $c\cdot m\cdot T$ en mode inverse. Le nombre $c$ ne dépend ni de $n$ ni de $m$. Si l’on compte chaque opération élémentaire comme un pas, on peut montrer que la valeur de la fonction et le gradient demandent ensemble au plus quatre fois plus de pas que la valeur de la fonction seule ; si l’on compte aussi les accès à la mémoire, $c$ reste inférieur à $6$, et en pratique il vaut souvent $2$ à $3$. Pour un nombre ($m=1$), le gradient complet ne coûte donc en mode inverse qu’un petit multiple fixe d’une évaluation.
:::

On démontre le théorème en comptant, pour chaque opération de base, combien de pas de calcul son pas arrière demande par rapport à elle-même. Il en découle une règle empirique : beaucoup d’entrées et une seule sortie, comme pour un nombre qui dépend de millions de boutons de réglage, appellent le mode inverse. Peu d’entrées et beaucoup de sorties appellent le mode direct. Pour la matrice jacobienne complète d’une fonction ayant beaucoup d’entrées et de sorties, il n’existe pas d’astuce de ce genre ; toute méthode y coûte de nombreuses passes.

Le mode inverse a un prix : la mémoire. La passe arrière a besoin de toutes les valeurs de l’évaluation avant, car les dérivées locales sont évaluées avec elles. Il faut donc conserver chaque valeur intermédiaire jusqu’à ce que la passe arrière l’ait dépassée. Pour de longs calculs, cette mémoire est souvent la véritable limite.

::::beispiel [Exemple de calcul]
Supposons qu’une fonction ait $n=10^6$ entrées et qu’une évaluation dure une seconde. Pour le gradient, le mode direct a besoin de $10^6$ passes, donc d’au moins $10^6$ secondes, soit un peu plus de $11$ jours. Les différences centrées demandent $2\cdot10^6$ évaluations, un peu plus de $23$ jours, et ne sont alors qu’approximativement justes. Le mode inverse a besoin d’une évaluation avant et d’une passe arrière, donc, avec $c\approx3$, de quelques secondes.
::::

⁠**En bref :** Le mode inverse fournit les $n$ dérivées partielles d’un nombre pour un petit multiple fixe d’une évaluation, indépendamment de $n$ ; il le paie par la mémoire nécessaire à toutes les valeurs intermédiaires.

:::hintergrund Pourquoi le mode inverse est si bon marché, et d’où il vient
La somme sur tous les chemins peut avoir énormément de termes. Si l’on enchaîne dix pas de calcul dont chacun utilise deux fois son prédécesseur, par exemple $v_{k+1}=v_k\cdot v_k$, il y a entre l’entrée et le résultat $2^{10}=1024$ chemins, et plus de $10^{15}$ pour $50$ pas. Le mode inverse ne compte jamais ces chemins un par un. Il regroupe tous les chemins qui passent par un même nœud dans l’adjoint de celui-ci et réutilise cette somme partielle pour tous les prédécesseurs. C’est la même idée que pour la règle du produit pas à pas de la section [9.1](rechengraphen.html#stufe-9-1) : un résultat intermédiaire est calculé une fois, puis utilisé souvent. Ainsi, chaque arête coûte une multiplication et une addition, et le coût croît avec le nombre d’arêtes, non avec le nombre de chemins. On peut réduire le besoin en mémoire en ne conservant que certaines valeurs intermédiaires et en recalculant les autres pendant la passe arrière ; avec une répartition habile, la mémoire et le facteur dont le temps de calcul dépasse celui d’une simple évaluation ne croissent plus alors que logarithmiquement avec la longueur du calcul.

Le mode direct a été décrit en 1964 sous forme de programme informatique. Le mode inverse a été développé par Seppo Linnainmaa en 1970 dans son mémoire de master à l’université d’Helsinki, pour estimer comment les erreurs d’arrondi de toutes les étapes de calcul se répercutent sur le résultat ; la sensibilité du résultat à chaque étape intermédiaire est exactement l’adjoint de celle-ci. Un programme générant automatiquement le mode inverse pour des calculs quelconques a suivi en 1980.
:::

### Parenthésage : vecteur fois matrice jacobienne

<span class="anker" id="stufe-10-6"></span>

La différence entre les deux modes peut aussi se décrire avec des matrices. Un calcul composé d’étages $\mathbf{g}_1,\dots,\mathbf{g}_L$ et qui se termine par un nombre a, d’après [(6.1)](die-kettenregel-fur-mehrere-variablen.html#gl-6-1), la matrice jacobienne

$$\mathbf{J}=\mathbf{J}_L\,\mathbf{J}_{L-1}\cdots\mathbf{J}_1 ,$$

où $\mathbf{J}_L$ est une ligne, parce que le dernier étage n’a qu’une sortie. Le produit est le même quel que soit le parenthésage ; d’après le [chapitre 1, section 9.3](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrixprodukt.html#stufe-9-3), le coût, lui, est très différent. Le mode inverse parenthèse par la gauche : $\bigl((\mathbf{J}_L\mathbf{J}_{L-1})\,\mathbf{J}_{L-2}\bigr)\cdots$. Chaque pas multiplie une ligne par une matrice et donne de nouveau une ligne, l’adjoint transposé de l’étage concerné. Le mode direct parenthèse par la droite : $\mathbf{J}_L\bigl(\cdots(\mathbf{J}_2\,(\mathbf{J}_1\dot{\mathbf{x}}))\bigr)$. Pour un vecteur $\dot{\mathbf{x}}$ isolé, c’est également bon marché ; mais pour le gradient complet, il lui faut $n$ tels vecteurs, et cela coûte autant que si l’on calculait entièrement les produits $\mathbf{J}_2\mathbf{J}_1$, $\mathbf{J}_3\mathbf{J}_2\mathbf{J}_1,\dots$.

S’y ajoute un second point : on ne forme jamais les matrices jacobiennes. Chaque pas arrière calcule directement le produit de l’adjoint par la matrice jacobienne, avec les règles des opérations de base. Pour un produit matrice-vecteur $\mathbf{y}=\mathbf{A}\mathbf{x}$, c’est, d’après [(7.6)](ableiten-nach-vektoren-und-matrizen.html#gl-7-6), $\bar{\mathbf{x}}=\mathbf{A}^{\top}\bar{\mathbf{y}}$, sans matrice supplémentaire ; pour une fonction appliquée terme à terme, c’est, d’après [(5.4)](die-jacobi-matrix.html#gl-5-4), le produit composante par composante avec les dérivées, sans construire de matrice diagonale. C’est d’ailleurs indispensable : si un étage a $10^5$ entrées et $10^5$ sorties, sa matrice jacobienne a $10^{10}$ coefficients, soit, à huit octets par nombre, $80$ gigaoctets.

::::beispiel [Exemple de calcul]
Supposons qu’un calcul se compose de trois étages $\mathbb{R}^{1000}\to\mathbb{R}^{1000}$ et d’un dernier étage $\mathbb{R}^{1000}\to\mathbb{R}$. D’après le [chapitre 1, section 9.3](/wissen/fr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrixprodukt.html#stufe-9-3), le produit d’une ligne par une matrice $1000\times1000$ coûte environ $2\cdot10^6$ opérations élémentaires, le produit de deux telles matrices environ $2\cdot10^9$. Avec un parenthésage par la gauche, il s’agit de trois produits ligne-matrice, soit environ $6\cdot10^6$ au total. Avec un parenthésage par la droite, il s’agit de deux produits matriciels et d’un produit ligne-matrice, soit environ $4\cdot10^9$ au total, environ $670$ fois plus.
::::

⁠**En bref :** Le mode inverse multiplie la chaîne des matrices jacobiennes par la gauche avec une ligne, le mode direct par la droite avec une colonne ; les matrices jacobiennes elles-mêmes ne sont jamais formées.

:::aufgabe Exercice 35 ★ À rebours à travers un carré
<span class="anker" id="aufg-35"></span>

Soit $f=(x_1x_2+x_3)^2$ comme dans l’exercice [32](rechengraphen.html#aufg-32).

<ol class="al">

<li>

Calculez au point $(1,\,2,\,3)$ tous les adjoints en mode inverse et présentez-les dans un tableau comme le tableau [6](#tab-6).

</li>

<li>

Combien de passes le mode direct demanderait-il pour le même gradient ? Effectuez la passe pour $\dot{\mathbf{x}}=\mathbf{e}_1$.

</li>

</ol>

:::loesung
(a) Avec les valeurs de l’exercice [32](rechengraphen.html#aufg-32) :

| Nœud | Calcul | Adjoint |
|---|---|---|
| $f$ | départ | $\bar f=1$ |
| $v_2$ | $\bar f\cdot2v_2$ | $\bar v_2=10$ |
| $v_1$ | $\bar v_2\cdot1$ | $\bar v_1=10$ |
| $x_3$ | $\bar v_2\cdot1$ | $\bar x_3=10$ |
| $x_2$ | $\bar v_1\cdot x_1$ | $\bar x_2=10$ |
| $x_1$ | $\bar v_1\cdot x_2$ | $\bar x_1=20$ |

(b) Trois passes, une par entrée. Avec $\dot{\mathbf{x}}=\mathbf{e}_1$ : $\dot v_1=x_2\dot x_1+x_1\dot x_2=2$, $\dot v_2=\dot v_1+\dot x_3=2$, $\dot f=2v_2\,\dot v_2=10\cdot2=20=\partial f/\partial x_1$.
:::
:::

:::aufgabe Exercice 36 ★★ La fonction logistique dans le graphe
<span class="anker" id="aufg-36"></span>

Soit $f(x_1,x_2)=\sigma(2x_1-x_2)$ avec la fonction logistique $\sigma$.

<ol class="al">

<li>

Dessinez le graphe avec $v_1=2x_1$, $v_2=v_1-x_2$, $f=\sigma(v_2)$ et effectuez l’évaluation avant au point $(1,\,1)$.

</li>

<li>

Calculez tous les adjoints. De quel nombre stocké le nœud $\sigma$ a-t-il besoin pour sa dérivée locale ?

</li>

<li>

Vérifiez par le calcul que $\nabla f(\mathbf{x})=\sigma'(2x_1-x_2)\,(2,\,-1)^{\top}$.

</li>

</ol>

:::loesung
(a) Le graphe a les arêtes $x_1\to v_1$, $v_1\to v_2$, $x_2\to v_2$ et $v_2\to f$. Évaluation avant au point $(1,\,1)$ : $v_1=2$, $v_2=1$, $f=\sigma(1)\approx0{,}7311$.

(b) $\bar f=1$ ; $\bar v_2=\bar f\cdot f\,(1-f)\approx0{,}7311\cdot0{,}2689\approx0{,}1966$ ; $\bar v_1=\bar v_2\cdot1\approx0{,}1966$ ; $\bar x_2=\bar v_2\cdot(-1)\approx-0{,}1966$ ; $\bar x_1=\bar v_1\cdot2\approx0{,}3932$. Pour sa dérivée locale, le nœud $\sigma$ n’a besoin que de sa propre sortie stockée $f$, d’après le tableau [4](rechengraphen.html#tab-4).

(c) D’après la règle de dérivation en chaîne, $\nabla f=\sigma'(2x_1-x_2)\,\nabla(2x_1-x_2)=\sigma'(2x_1-x_2)\,(2,\,-1)^{\top}$, donc $0{,}1966\cdot(2,\,-1)^{\top}=(0{,}3932;\ -0{,}1966)^{\top}$ au point $(1,\,1)$.
:::
:::

:::aufgabe Exercice 37 ★★ Nombres duaux
<span class="anker" id="aufg-37"></span>

<ol class="al">

<li>

Calculez $p(x)=(x+1)(x+2)(x+3)(x+4)$ avec le nombre dual $x=0+1\varepsilon$ et lisez $p(0)$ et $p'(0)$.

</li>

<li>

Calculez de même $(x^2+1)^3$ en $x=1+\varepsilon$ et comparez avec la règle de dérivation en chaîne.

</li>

</ol>

:::loesung
(a) Avec $x=\varepsilon$ :

$$(1+\varepsilon)(2+\varepsilon)=2+3\varepsilon,\quad (2+3\varepsilon)(3+\varepsilon)=6+11\varepsilon,\quad (6+11\varepsilon)(4+\varepsilon)=24+50\varepsilon .$$

Donc $p(0)=24$ et $p'(0)=50$ ; les coefficients de $\varepsilon$ sont exactement les $p_k'$ de l’exemple de calcul de la section [9.1](rechengraphen.html#stufe-9-1).

(b) $(1+\varepsilon)^2=1+2\varepsilon$, plus $1$ donne $2+2\varepsilon$ ; $(2+2\varepsilon)^2=4+8\varepsilon$ et $(4+8\varepsilon)(2+2\varepsilon)=8+24\varepsilon$. La règle de dérivation en chaîne donne $3\,(x^2+1)^2\cdot2x=3\cdot4\cdot2=24$ en $1$.
:::
:::

:::aufgabe Exercice 38 ★★★ Quel mode ?
<span class="anker" id="aufg-38"></span>

<ol class="al">

<li>

Un calcul a $3$ entrées et $1000$ sorties, un autre $1000$ entrées et $3$ sorties. Combien de passes le mode direct et le mode inverse demandent-ils dans chaque cas pour la matrice jacobienne complète ?

</li>

<li>

Soit $f(\mathbf{x})=\mathbf{c}^{\top}\mathbf{B}\mathbf{x}$ avec une matrice pleine $\mathbf{B}\in\mathbb{R}^{n\times n}$, la fonction étant calculée en deux étages $\mathbf{y}=\mathbf{B}\mathbf{x}$ et $f=\mathbf{c}^{\top}\mathbf{y}$. Une passe avant calcule $\mathbf{c}^{\top}(\mathbf{B}\dot{\mathbf{x}})$, une passe arrière $\bar{\mathbf{x}}=\mathbf{B}^{\top}\mathbf{c}$. Comptez, pour les deux façons de faire, les opérations élémentaires que coûte le gradient complet, si un produit matrice-vecteur coûte environ $2n^2$ et un produit scalaire environ $2n$.

</li>

<li>

Pourquoi le mode inverse a-t-il besoin de plus de mémoire que le mode direct ? Quelles valeurs le mode direct peut-il oublier immédiatement ?

</li>

</ol>

:::loesung
(a) Avec $3$ entrées et $1000$ sorties, le mode direct demande $3$ passes, le mode inverse $1000$ ; on choisit le mode direct. Avec $1000$ entrées et $3$ sorties, c’est l’inverse : $1000$ passes avant contre $3$ passes arrière.

(b) En mode direct, le gradient demande $n$ passes avec $\dot{\mathbf{x}}=\mathbf{e}_1,\dots,\mathbf{e}_n$, chacune avec un produit matrice-vecteur $\mathbf{B}\dot{\mathbf{x}}$ et un produit scalaire, soit en tout environ $n\,(2n^2+2n)\approx2n^3$ opérations élémentaires. En mode inverse, $\bar{\mathbf{y}}=\mathbf{c}$, et $\bar{\mathbf{x}}=\mathbf{B}^{\top}\mathbf{c}$ coûte un produit matrice-vecteur, environ $2n^2$ ; s’y ajoute l’évaluation avant, avec environ $2n^2+2n$. Le mode inverse est donc environ $n/2$ fois plus rapide.

(c) La passe arrière a besoin des valeurs de l’évaluation avant pour évaluer les dérivées locales, et elle ne vient qu’une fois l’évaluation avant terminée. Toutes les valeurs intermédiaires doivent donc être conservées jusque-là. En mode direct, la valeur et la valeur tangente avancent ensemble ; aucune des deux n’est plus nécessaire dès que tous les successeurs du nœud sont calculés, et elles peuvent alors être oubliées.
:::
:::

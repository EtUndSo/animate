---
title: Lo esencial hasta aquí
pfad: Informática / Aprendizaje automático / Fundamentos matemáticos / Proyección, valores propios y descomposiciones
knoten: Fundamentos 2: Proyección, valores propios y descomposiciones
nachschlagen: ja
order: 15221400
summary: Puntos más cercanos, direcciones naturales y los bloques de una matriz
tags: 
lang: es
---

:::kern Lo esencial hasta aquí
<ul>

<li>

Vectores ortonormales: $\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}$; las coordenadas son productos escalares $c_i=\mathbf{q}_i^{\top}\mathbf{x}$; las matrices ortogonales conservan longitudes y ángulos. Si $\mathbf{Q}$ no es cuadrada, $\mathbf{Q}\mathbf{Q}^{\top}\ne\mathbf{I}$.

</li>

<li>

Proyección sobre una recta: $\hat{\mathbf{y}}=\frac{\mathbf{a}^{\top}\mathbf{y}}{\mathbf{a}^{\top}\mathbf{a}}\,\mathbf{a}$; el resto es perpendicular a $\mathbf{a}$, y $\hat{\mathbf{y}}$ es el punto más cercano. Las matrices de proyección cumplen $\mathbf{P}^2=\mathbf{P}$; las ortogonales, además, $\mathbf{P}^{\top}=\mathbf{P}$.

</li>

<li>

Mejor solución aproximada: el residuo $\mathbf{r}=\mathbf{y}-\mathbf{A}\hat{\mathbf{x}}$ es perpendicular al espacio columna, es decir, $\mathbf{A}^{\top}\mathbf{A}\hat{\mathbf{x}}=\mathbf{A}^{\top}\mathbf{y}$; es única si y solo si las columnas son independientes.

</li>

<li>

Proyección sobre un subespacio: $\mathbf{P}=\mathbf{A}(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}=\mathbf{Q}\mathbf{Q}^{\top}$; Gram-Schmidt da $\mathbf{A}=\mathbf{Q}\mathbf{R}$, y $\mathbf{R}\hat{\mathbf{x}}=\mathbf{Q}^{\top}\mathbf{y}$.

</li>

<li>

Las formas cuadráticas $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}$ solo dependen de la parte simétrica; cuenco, canal y silla se reconocen completando cuadrados.

</li>

<li>

Valores propios: $\mathbf{A}\mathbf{v}=\lambda\mathbf{v}$, $\det(\mathbf{A}-\lambda\mathbf{I})=0$; traza $=\sum\lambda_i$, $\det=\prod\lambda_i$; las rotaciones tienen valores propios complejos.

</li>

<li>

$\mathbf{A}=\mathbf{S}\boldsymbol{\Lambda}\mathbf{S}^{-1}$ desacopla, $\mathbf{A}^k=\mathbf{S}\boldsymbol{\Lambda}^k\mathbf{S}^{-1}$. Simétrica: $\mathbf{A}=\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top}$, con $\lambda_i$ reales y ejes principales perpendiculares, semiejes $1/\sqrt{\lambda_i}$.

</li>

<li>

Definida positiva $\Leftrightarrow$ todos los valores propios $>0$ $\Leftrightarrow$ todos los pivotes $>0$ $\Leftrightarrow$ todos los menores principales dominantes $>0$; $\mathbf{A}^{\top}\mathbf{A}$ es semidefinida positiva; Cholesky: $\mathbf{A}=\mathbf L\mathbf L^{\top}$.

</li>

<li>

Descomposición en valores singulares $\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}=\sum_jd_j\mathbf{u}_j\mathbf{v}_j^{\top}$ para toda matriz: girar, estirar, girar; los $d_j^2$ son los valores propios de $\mathbf{A}^{\top}\mathbf{A}$, $\lVert\mathbf{A}\rVert_2=d_1$.

</li>

<li>

$\lVert\mathbf{A}\rVert_F^2=\sum_jd_j^2$; $\mathbf{A}_k$ es la mejor aproximación de rango $k$, con el error $d_{k+1}$ en la norma espectral.

</li>

<li>

$\mathbf{A}^+=\mathbf{V}\mathbf{D}^+\mathbf{U}^{\top}$ da la mejor solución aproximada más corta; casos particulares: $(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}$ y $\mathbf{A}^{\top}(\mathbf{A}\mathbf{A}^{\top})^{-1}$.

</li>

<li>

$\kappa(\mathbf{A})=d_1/d_n$ acota la amplificación de los errores relativos; $1/\kappa$ es la distancia relativa a la singularidad; $\kappa(\mathbf{A}^{\top}\mathbf{A})=\kappa(\mathbf{A})^2$.

</li>

</ul>
:::

:::merke La respuesta en tres frases
<ol>

<li>

Un sistema de ecuaciones sin solución se resuelve lo mejor posible proyectando el lado derecho perpendicularmente sobre el espacio columna: el residuo es entonces perpendicular a todas las columnas, de ahí se siguen las ecuaciones normales, y por Pitágoras ningún otro punto está más cerca.

</li>

<li>

Los vectores propios son las direcciones que una matriz solo estira; en su base, la matriz se vuelve diagonal, y en las matrices simétricas forman un sistema de ejes rectangular en el que se lee la forma de cualquier forma cuadrática.

</li>

<li>

Toda matriz es una suma, ordenada por tamaño, de bloques $d_j\mathbf{u}_j\mathbf{v}_j^{\top}$ de rango $1$: los $k$ primeros dan la mejor aproximación de rango $k$, y el cociente $d_1/d_n$ dice cuánto pueden falsear la solución los errores en los datos.

</li>

</ol>
:::

**Un principio detrás de todos los resultados.** Casi todo en este capítulo se deduce de un principio: en un sistema de ejes rectangular, el cuadrado de una longitud se descompone por Pitágoras en partes independientes, y el camino más corto a una recta, a un plano o a un subespacio es el perpendicular.

| Resultado | De dónde viene |
|---|---|
| Coordenadas como productos escalares, $\mathbf{Q}^{-1}=\mathbf{Q}^{\top}$ | ejes perpendiculares de longitud $1$: los términos cruzados desaparecen (sección [1](orthonormalbasen-und-orthogonale-matrizen.html#stufe-1)) |
| Punto más cercano sobre una recta y sobre un subespacio | Pitágoras: resto perpendicular más desplazamiento dentro del subespacio (secciones [2](projektion-auf-eine-gerade.html#stufe-2) y [3](die-beste-naherungslosung.html#stufe-3)) |
| Ecuaciones normales | residuo perpendicular a cada columna: $\mathbf{A}^{\top}\mathbf{r}=\mathbf{0}$ (sección [3](die-beste-naherungslosung.html#stufe-3)) |
| Gram-Schmidt y QR | restar la sombra, normalizar el resto perpendicular (sección [4](projektion-auf-einen-unterraum.html#stufe-4)) |
| Cuenco, canal, silla | signos de los factores de una suma de cuadrados (secciones [5](quadratische-formen.html#stufe-5) y [8](positiv-definite-matrizen.html#stufe-8)) |
| Desacoplar diagonalizando | en la base propia, cada coordenada actúa por separado (sección [7](diagonalisierung-und-spektralsatz.html#stufe-7)) |
| Teorema espectral | simetría: $\mathbf{A}$ puede cambiar de lado en el producto escalar, y el complemento de un vector propio se conserva (sección [7](diagonalisierung-und-spektralsatz.html#stufe-7)) |
| Descomposición en valores singulares de toda matriz | teorema espectral para la matriz simétrica $\mathbf{A}^{\top}\mathbf{A}$ (sección [9](die-singularwertzerlegung.html#stufe-9)) |
| Mejor aproximación de rango $k$ | el núcleo de una matriz de rango $k$ corta las $k+1$ direcciones más estiradas (sección [10](naherung-durch-matrizen-von-kleinem-rang.html#stufe-10)) |
| Mejor solución aproximada más corta | Pitágoras en las coordenadas de los vectores singulares: las partes en el núcleo solo alargan (sección [11](die-pseudoinverse.html#stufe-11)) |
| Número de condición | estiramiento máximo y mínimo, $d_1$ y $d_n$ (sección [12](die-konditionszahl.html#stufe-12)) |

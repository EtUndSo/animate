---
title: Lo esencial hasta aquí
pfad: Informática / Aprendizaje automático / Fundamentos matemáticos / Vectores y matrices
adresse: informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen
knoten: Capítulo 1: Vectores y matrices
nachschlagen: ja
order: 15211700
summary: Los datos como listas de números, los modelos como aplicaciones lineales
tags: 
lang: es
---

:::kern Lo esencial hasta aquí
<ul>

<li>

Un ejemplo con $d$ características es un vector columna $\mathbf{x}\in\mathbb{R}^d$; un conjunto de datos de $N$ ejemplos es la matriz de datos $\mathbf{X}\in\mathbb{R}^{N\times d}$, con un ejemplo por fila.

</li>

<li>

El producto escalar $\mathbf{u}^{\top}\mathbf{v}=\sum_ju_jv_j$ es una suma ponderada y una comparación con un patrón; la suma ponderada $\mathbf{w}^{\top}\mathbf{x}$ es la regla lineal más general con una salida.

</li>

<li>

Las normas miden el tamaño: $\lVert\mathbf{x}\rVert_2=\sqrt{\mathbf{x}^{\top}\mathbf{x}}$, $\lVert\mathbf{x}\rVert_1=\sum_j|x_j|$, $\lVert\mathbf{x}\rVert_\infty=\max_j|x_j|$; el valor cuadrático medio es $\lVert\mathbf{x}\rVert/\sqrt n$. Las distancias $\lVert\mathbf{u}-\mathbf{v}\rVert$ dependen de las unidades; estandarizar las hace independientes de ellas.

</li>

<li>

$|\mathbf{u}^{\top}\mathbf{v}|\le\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert$; el ángulo cumple $\cos\varphi=\mathbf{u}^{\top}\mathbf{v}/(\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert)$; ortogonal significa $\mathbf{u}^{\top}\mathbf{v}=0$.

</li>

<li>

$\mathbf{A}\mathbf{x}$ es una lista de productos escalares (visión por filas) y una combinación lineal de las columnas (visión por columnas); $\mathbf{X}\mathbf{w}$ son todas las predicciones a la vez.

</li>

<li>

Toda aplicación lineal es una matriz cuyas columnas son las imágenes de los vectores unitarios; afín significa $\mathbf{A}\mathbf{x}+\mathbf{b}$.

</li>

<li>

$\mathbf{A}\mathbf{B}$ es «primero $\mathbf{B}$, después $\mathbf{A}$»; es asociativo, no conmutativo; varias etapas lineales en serie son una sola matriz.

</li>

<li>

$(\mathbf{A}\mathbf{B})^{\top}=\mathbf{B}^{\top}\mathbf{A}^{\top}$; $\mathbf{X}\mathbf{X}^{\top}$ contiene todos los productos escalares de los ejemplos, y $\mathbf{X}^{\top}\mathbf{X}=\sum_i\mathbf{x}_i\mathbf{x}_i^{\top}$, los de las características.

</li>

<li>

$(\mathbf{A}\mathbf{B})^{-1}=\mathbf{B}^{-1}\mathbf{A}^{-1}$; $\mathbf{A}\mathbf{x}=\mathbf{y}$ no tiene ninguna solución, tiene una o tiene infinitas, y tiene solución si y solo si $\mathbf{y}$ está en el espacio columna.

</li>

<li>

$\dim\ker\mathbf{A}+\operatorname{rango}\mathbf{A}=n$; $\mathbf{A}\mathbf{x}=\mathbf{y}$ tiene solución si y solo si $\operatorname{rango}(\mathbf{A}\,|\,\mathbf{y})=\operatorname{rango}\mathbf{A}$, y entonces es única si y solo si $\operatorname{rango}\mathbf{A}=n$; las características dependientes reducen el rango y hacen ambiguos los pesos.

</li>

<li>

$\det\mathbf{A}$ es el factor de volumen con signo, $\det(\mathbf{A}\mathbf{B})=\det\mathbf{A}\det\mathbf{B}$, y $\mathbf{A}$ es invertible si y solo si $\det\mathbf{A}\ne0$.

</li>

<li>

$\odot$ multiplica entrada por entrada; los tensores son disposiciones de números con un número cualquiera de ejes.

</li>

</ul>
:::

:::merke La respuesta en tres frases
<ol>

<li>

Un conjunto de datos es una matriz cuyas filas contienen los ejemplos como vectores, y la similitud, la distancia y el tamaño son productos escalares y normas de estos vectores, que dependen de las unidades elegidas.

</li>

<li>

Una regla lineal queda fijada por las imágenes de los vectores unitarios, es decir, es una matriz, y el producto matriz-vector la aplica a todos los ejemplos a la vez.

</li>

<li>

Componer aplicaciones es multiplicar sus matrices, y si una aplicación puede invertirse lo deciden el rango, el núcleo y el determinante: muestran si en ella se pierden direcciones.

</li>

</ol>
:::

**Un principio detrás de todos los resultados.** Casi todo en este capítulo se deduce de dos operaciones: los vectores se suman y se multiplican por números, y las aplicaciones lineales conservan exactamente estas dos operaciones.

| Resultado | De dónde viene |
|---|---|
| Suma ponderada, comparación con un patrón | producto escalar: productos en la misma posición, sumados (sección [2](das-skalarprodukt.html#stufe-2)) |
| Longitud, distancia, ángulo | todos a partir del producto escalar: $\lVert\mathbf{x}\rVert^2=\mathbf{x}^{\top}\mathbf{x}$, [(4.1)](abstande-und-einheiten.html#gl-4-1), Cauchy-Schwarz (secciones [3](normen-die-groe-eines-vektors.html#stufe-3) a [5](winkel-und-ahnlichkeit.html#stufe-5)) |
| Las distancias dependen de las unidades | cada característica entra con el cuadrado de su valor numérico (sección [4](abstande-und-einheiten.html#stufe-4)) |
| Visión por filas y visión por columnas | la misma suma doble, ordenada de distinta manera (sección [7](das-matrix-vektor-produkt.html#stufe-7)) |
| Matriz de una aplicación lineal | $\mathbf{x}=\sum_jx_j\mathbf{e}_j$, y la aplicación conserva las combinaciones lineales (sección [8](lineare-abbildungen.html#stufe-8)) |
| Producto de matrices, no conmutativo | matriz de la composición (sección [9](das-matrixprodukt.html#stufe-9)) |
| Matriz de Gram | tabla de los productos escalares, $\mathbf{X}\mathbf{X}^{\top}$ y $\mathbf{X}^{\top}\mathbf{X}$ (sección [10](transponierte-symmetrie-und-gram-matrix.html#stufe-10)) |
| Sin inversa si $\mathbf{A}\mathbf{x}=\mathbf{0}$ con $\mathbf{x}\ne\mathbf{0}$ | dos entradas, una salida: información perdida (sección [11](einheitsmatrix-und-inverse.html#stufe-11)) |
| Ninguna, una o infinitas soluciones | con dos soluciones, toda la recta que pasa por ellas es solución (sección [12](lineare-gleichungssysteme.html#stufe-12)) |
| Pesos ambiguos | los vectores del núcleo no cambian $\mathbf{X}\mathbf{w}$ (sección [13](unabhangigkeit-basis-und-rang.html#stufe-13)) |
| $\det(\mathbf{A}\mathbf{B})=\det\mathbf{A}\det\mathbf{B}$ | los factores de volumen se multiplican al componer aplicaciones (sección [14](die-determinante.html#stufe-14)) |

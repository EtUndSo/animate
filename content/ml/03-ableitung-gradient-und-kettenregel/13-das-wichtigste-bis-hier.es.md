---
title: Lo esencial hasta aquí
pfad: Informática / Aprendizaje automático / Fundamentos matemáticos / Derivada, gradiente y regla de la cadena
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Capítulo 3: Derivada, gradiente y regla de la cadena
nachschlagen: ja
order: 15231300
summary: Cómo responde un número a sus entradas: de la recta tangente al modo inverso
tags: 
lang: es
---

:::kern Lo esencial hasta aquí
<ul>

<li>

Derivada: $f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}$; cerca de $x$, $f(x+h)\approx f(x)+f'(x)h$, con un error que desaparece más rápido que $h$. Con la segunda derivada: $f(x+h)\approx f(x)+f'(x)h+\tfrac12f''(x)h^2$.

</li>

<li>

Regla de la cadena: $(f\circ g)'(x)=f'(g(x))\,g'(x)$; en cadenas largas, el producto de todos los factores. Función logística: $\sigma'=\sigma(1-\sigma)\le\tfrac14$.

</li>

<li>

Gradiente $\nabla f\in\mathbb{R}^d$ como columna; $f(\mathbf{x}+\mathbf{h})\approx f(\mathbf{x})+\nabla f(\mathbf{x})^{\top}\mathbf{h}$ si $f$ es diferenciable; las derivadas parciales solas no bastan.

</li>

<li>

Derivada direccional $D_{\mathbf{u}}f=\nabla f^{\top}\mathbf{u}$; máximo ascenso en la dirección de $\nabla f$, con pendiente $\lVert\nabla f\rVert$ (Cauchy-Schwarz); $\nabla f$ es perpendicular a las curvas de nivel; $-\nabla f$ solo apunta al punto más bajo si las curvas de nivel son redondas.

</li>

<li>

Matriz jacobiana $\mathbf{J}_{\mathbf{g}}\in\mathbb{R}^{m\times n}$, una fila por salida: $\mathbf{g}(\mathbf{x}+\mathbf{h})\approx\mathbf{g}(\mathbf{x})+\mathbf{J}_{\mathbf{g}}\mathbf{h}$; para $\mathbf{A}\mathbf{x}+\mathbf{b}$ es $\mathbf{A}$; para funciones elemento a elemento, diagonal.

</li>

<li>

Regla de la cadena: $\mathbf{J}_{\mathbf f\circ\mathbf{g}}=\mathbf{J}_{\mathbf f}\mathbf{J}_{\mathbf{g}}$, componente a componente una suma sobre todos los caminos; $\nabla(f\circ\mathbf{g})=\mathbf{J}_{\mathbf{g}}^{\top}\nabla f$.

</li>

<li>

$\nabla(\mathbf{a}^{\top}\mathbf{x})=\mathbf{a}$, $\nabla(\mathbf{x}^{\top}\mathbf{A}\mathbf{x})=(\mathbf{A}+\mathbf{A}^{\top})\mathbf{x}$, $\nabla\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert^2=-2\mathbf{A}^{\top}(\mathbf{y}-\mathbf{A}\mathbf{x})$, $\nabla_{\mathbf{A}}(\mathbf{u}^{\top}\mathbf{A}\mathbf{v})=\mathbf{u}\mathbf{v}^{\top}$; hacia atrás a través de $\mathbf{y}=\mathbf{A}\mathbf{x}$ con $F=f(\mathbf{A}\mathbf{x})$: $\nabla_{\mathbf{A}}F=\nabla f(\mathbf{y})\,\mathbf{x}^{\top}$, $\nabla_{\mathbf{x}}F=\mathbf{A}^{\top}\nabla f(\mathbf{y})$.

</li>

<li>

Matriz hessiana $\mathbf{H}_f$, simétrica según Schwarz; $f(\mathbf{x}+\mathbf{h})\approx f+\nabla f^{\top}\mathbf{h}+\tfrac12\mathbf{h}^{\top}\mathbf{H}_f\mathbf{h}$; la curvatura en la dirección $\mathbf{u}$ es $\mathbf{u}^{\top}\mathbf{H}_f\mathbf{u}$, entre el menor y el mayor valor propio.

</li>

<li>

Grafo computacional: operaciones elementales, evaluación hacia adelante con valores guardados, derivadas locales en las aristas.

</li>

<li>

Modo directo: valores tangentes, una pasada por dirección ($\mathbf{J}\dot{\mathbf{x}}$). Modo inverso: adjuntos $\bar a=\sum\bar b\,\partial b/\partial a$ a partir de $\bar f=1$, una pasada para el gradiente completo, coste de un pequeño múltiplo de una evaluación; precio: memoria.

</li>

<li>

Numérica: error de la diferencia progresiva $\approx\tfrac12f''h$, de la diferencia central $\approx\tfrac16f'''h^2$; el redondeo crece como $\varepsilon_{\mathrm M}/h$, de ahí la curva en V; comprobación del gradiente con el error relativo: por encima de $10^{-2}$, incorrecto; por debajo de $10^{-7}$, bien.

</li>

</ul>
:::

:::merke La respuesta en tres frases
<ol>

<li>

Cómo reacciona un número a pequeñas variaciones de sus entradas lo dice su aproximación lineal: cada entrada aporta su derivada parcial por su variación, y las contribuciones se suman para dar el producto escalar con el gradiente.

</li>

<li>

Según la desigualdad de Cauchy-Schwarz, este producto escalar es máximo, para pasos de longitud fija, en la dirección del gradiente, que por eso apunta cuesta arriba de la forma más empinada y es perpendicular a las curvas de nivel.

</li>

<li>

Si el número surge de una larga cadena de pasos de cálculo, su derivada es un producto de matrices jacobianas, es decir, una suma sobre todos los caminos, y el modo inverso calcula este producto desde el número con vectores fila, de modo que da todas las derivadas a la vez por un pequeño múltiplo del coste de una sola evaluación.

</li>

</ol>
:::

**Un principio detrás de todos los resultados.** Casi todo en este capítulo se deduce de un principio: lo bastante cerca de un punto, toda función diferenciable es lineal. La derivada, el gradiente y la matriz jacobiana son esta aproximación lineal; la regla de la cadena conecta aproximaciones lineales una tras otra y multiplica al hacerlo sus matrices; y el modo directo y el modo inverso son dos maneras de asociar este producto.

| Resultado | De dónde viene |
|---|---|
| Derivada y recta tangente | la única recta cuyo error desaparece más rápido que $h$ (sección [1](die-ableitung.html#stufe-1)) |
| Regla del producto | la pieza de la esquina $\Delta u\,\Delta v$ es pequeña de segundo orden (sección [1.4](die-ableitung.html#stufe-1-4)) |
| Regla de la cadena de una variable | cada etapa transmite las pequeñas variaciones con su factor (sección [2](die-kettenregel.html#stufe-2)) |
| Gradiente y plano tangente | los efectos de las pequeñas variaciones se suman (sección [3](partielle-ableitungen-und-der-gradient.html#stufe-3)) |
| Máximo ascenso | Cauchy-Schwarz para $\nabla f^{\top}\mathbf{u}$ (sección [4](richtungsableitung-und-steilster-anstieg.html#stufe-4)) |
| Gradiente perpendicular a la curva de nivel | a lo largo de la curva de nivel, la pendiente es nula (secciones [4](richtungsableitung-und-steilster-anstieg.html#stufe-4) y [6](die-kettenregel-fur-mehrere-variablen.html#stufe-6)) |
| Matriz jacobiana | la matriz de la aproximación lineal de una función vectorial (sección [5](die-jacobi-matrix.html#stufe-5)) |
| Regla de la cadena como producto de matrices, suma sobre caminos | aproximaciones lineales conectadas una tras otra (sección [6](die-kettenregel-fur-mehrere-variablen.html#stufe-6)) |
| Identidades matriciales, regla hacia atrás | regla de la cadena componente a componente, con una convención de disposición fija (sección [7](ableiten-nach-vektoren-und-matrizen.html#stufe-7)) |
| Matriz hessiana y curvatura | segunda derivada a lo largo de una recta, valores propios de una forma cuadrática (sección [8](die-hesse-matrix-und-die-quadratische-naherung.html#stufe-8)) |
| Modo inverso | agrupar los caminos según su primera arista, reutilizar sumas parciales; asociación por la izquierda (secciones [9](rechengraphen.html#stufe-9) y [10](automatische-differentiation.html#stufe-10)) |
| Diferencia central, curva en V | los términos de Taylor pares se cancelan; los errores de redondeo crecen como $1/h$ (sección [11](numerische-ableitung-und-gradientenprufung.html#stufe-11)) |

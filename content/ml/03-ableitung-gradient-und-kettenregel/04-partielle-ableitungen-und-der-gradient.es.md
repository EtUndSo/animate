---
title: Derivadas parciales y el gradiente
pfad: Informática / Aprendizaje automático / Fundamentos matemáticos / Derivada, gradiente y regla de la cadena
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Capítulo 3: Derivada, gradiente y regla de la cadena
nachschlagen: ja
order: 15230400
summary: Si un número depende de muchas entradas, se puede modificar un poco cada entrada por separado y mantener fijas las demás.
tags: función de d variables, conjunto de nivel, curva de nivel, curva de corte, derivada parcial, gradiente, plano tangente, diferenciable
lang: es
---

<span class="anker" id="stufe-3"></span>

:::zweck
Si un número depende de muchas entradas, se puede modificar un poco cada entrada por separado y mantener fijas las demás. Las pendientes que se encuentran así se llaman derivadas parciales. Juntas forman un vector, el gradiente, y con él la aproximación lineal de la sección [1](die-ableitung.html#stufe-1) se convierte en una aproximación mediante un plano. Al final, la sección aclara cuándo es realmente válida esta aproximación.
:::

### Funciones de varias variables

<span class="anker" id="stufe-3-1"></span>

En el [capítulo 1, sección 2.2](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-skalarprodukt.html#stufe-2-2), la predicción para una vivienda era la suma ponderada $\hat y=\mathbf{w}^{\top}\mathbf{x}$ de las características. Si se mantienen fijas las características y se pregunta cómo depende la predicción de los pesos, $\hat y$ es un número que depende de los $d$ números $w_1,\dots,w_d$. Del mismo modo, la forma cuadrática $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}$ del [capítulo 2, sección 5.1](/wissen/es/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/quadratische-formen.html#stufe-5-1), depende de todas las componentes de $\mathbf{x}$. Para tales asignaciones hace falta un concepto propio.

:::definition Definición 3.1 (Función de varias variables, curva de nivel)
<span class="anker" id="satz-3-1"></span>

Una función $f:\mathbb{R}^d\to\mathbb{R}$ asigna a cada vector $\mathbf{x}\in\mathbb{R}^d$ un número $f(\mathbf{x})=f(x_1,\dots,x_d)$; se llama __función de $d$ variables__. Para un número $c$, el conjunto de todos los $\mathbf{x}$ con $f(\mathbf{x})=c$ se llama __conjunto de nivel__ de $f$ para el valor $c$. Para $d=2$ suele ser una curva y se llama entonces __curva de nivel__.
:::

Para dos variables ayuda la imagen de un paisaje. El vector $\mathbf{x}=(x_1,\,x_2)^{\top}$ es un lugar en un mapa, y $f(\mathbf{x})$, la altura del terreno sobre ese lugar. La gráfica de $f$, el conjunto de los puntos $(x_1,\,x_2,\,f(x_1,x_2))$ en el espacio, es la superficie del terreno. Las curvas de nivel unen, como en un mapa de senderismo, todos los lugares de la misma altura. Donde están juntas, el terreno es empinado; donde están muy separadas, es llano. Con más de dos variables falta la imagen, pero los cálculos siguen siendo los mismos.

::::beispiel [Ejemplo numérico]
A lo largo de las secciones [3](#stufe-3) a [8](die-hesse-matrix-und-die-quadratische-naherung.html#stufe-8) nos acompaña la función

<span class="anker" id="gl-3-1"></span>
$$f(\mathbf{x})=x_1^2\,x_2+x_2^2 . \tag{3.1}$$

En el punto $\mathbf{x}=(1,\,2)^{\top}$, $f(1,2)=1\cdot2+4=6$. A la curva de nivel $f=6$ pertenecen todos los puntos con $x_1^2x_2+x_2^2=6$. Para $x_1=0$ esto es $x_2^2=6$; así, el punto $(0;\ \sqrt6)^{\top}\approx(0;\ 2{,}449)^{\top}$ está en ella. En general, para cada $x_1$ fijo la ecuación es cuadrática en $x_2$, y su solución positiva $x_2=\tfrac12\bigl(\sqrt{x_1^4+24}-x_1^2\bigr)$ describe toda la curva de nivel por encima del eje $x_1$; para $x_1=1$ da $\tfrac12(5-1)=2$. La fig. [6](#abb-6) muestra algunas curvas de nivel.
::::

⁠**En resumen:** Una función de $d$ variables asigna a cada vector un número; con dos variables se la imagina como un paisaje cuyas curvas de nivel unen los lugares de la misma altura.

### Derivadas parciales

<span class="anker" id="stufe-3-2"></span>

¿Con qué intensidad reacciona $f$ si solo se modifica una entrada? Se mantienen fijas todas las demás, y $f$ se convierte en una función ordinaria de una variable. En la imagen del paisaje, se corta el terreno a lo largo de una recta paralela a un eje. La superficie del corte muestra como borde una curva, la __curva de corte__, y su pendiente es la sensibilidad buscada.

:::definition Definición 3.2 (Derivada parcial)
<span class="anker" id="satz-3-2"></span>

La __derivada parcial__ de $f:\mathbb{R}^d\to\mathbb{R}$ respecto de $x_j$ en el punto $\mathbf{x}$ es

<span class="anker" id="gl-3-2"></span>
$$\frac{\partial f}{\partial x_j}(\mathbf{x})=\lim_{h\to0}\frac{f(\mathbf{x}+h\,\mathbf{e}_j)-f(\mathbf{x})}{h}, \tag{3.2}$$

siempre que el límite exista. Aquí, $\mathbf{e}_j$ es el $j$-ésimo vector unitario del [capítulo 1, sección 1.6](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/vektoren-daten-als-zahlenlisten.html#stufe-1-6). Abreviadamente se escribe también $\partial_jf(\mathbf{x})$.
:::

El vector $\mathbf{x}+h\,\mathbf{e}_j$ se diferencia de $\mathbf{x}$ solo en la $j$-ésima componente, y en concreto en $h$. La definición es, pues, la derivada ordinaria de la sección [1.2](die-ableitung.html#stufe-1-2), aplicada a la función que se obtiene al mantener fijas todas las variables excepto $x_j$. De ello se sigue la regla de cálculo: se deriva respecto de $x_j$ y se tratan todas las demás variables como constantes. El símbolo $\partial$ es una d redondeada y recuerda que solo se mueve una parte de las variables.

::::beispiel [Ejemplo numérico]
Para $f(\mathbf{x})=x_1^2x_2+x_2^2$, al derivar respecto de $x_1$ se trata la variable $x_2$ como constante, y a la inversa:

$$\frac{\partial f}{\partial x_1}=2x_1\,x_2,\qquad \frac{\partial f}{\partial x_2}=x_1^2+2x_2 .$$

En el punto $(1,\,2)$ esto da $4$ y $5$. Con las curvas de corte se ve lo mismo (fig. [6](#abb-6)): si se mantiene fijo $x_2=2$, queda $f(x_1,2)=2x_1^2+4$, con pendiente $4x_1=4$ en el punto $x_1=1$. Si se mantiene fijo $x_1=1$, queda $f(1,x_2)=x_2+x_2^2$, con pendiente $1+2x_2=5$ en el punto $x_2=2$.

:::abbildung ml/k3schnitt 6
Derivadas parciales como pendientes de curvas de corte, para $f(\mathbf{x})=x_1^2x_2+x_2^2$ en el punto $(1,\,2)$. (a) Curvas de nivel para los valores $2$, $4$, $6$ (negro), $8$ y $10$, junto con las dos rectas de corte que pasan por $(1,\,2)$. (b) A lo largo de la recta azul $x_2=2$, el terreno tiene el perfil $2x_1^2+4$, con pendiente $4$ en $x_1=1$. (c) A lo largo de la recta roja $x_1=1$, tiene el perfil $x_2+x_2^2$, con pendiente $5$ en $x_2=2$.
:::
::::

⁠**En resumen:** La derivada parcial $\partial f/\partial x_j$ es la pendiente en la dirección del eje $x_j$: se deriva respecto de $x_j$ y se mantienen fijas todas las demás variables.

### El gradiente

<span class="anker" id="stufe-3-3"></span>

Una función de $d$ variables tiene en cada punto $d$ derivadas parciales. Se reúnen en un vector para poder calcular con ellas como con el propio $\mathbf{x}$.

:::definition Definición 3.3 (Gradiente)
<span class="anker" id="satz-3-3"></span>

Si en el punto $\mathbf{x}$ existen todas las derivadas parciales de $f:\mathbb{R}^d\to\mathbb{R}$, el vector columna

<span class="anker" id="gl-3-3"></span>
$$\nabla f(\mathbf{x})=\begin{pmatrix}\partial_1f(\mathbf{x})\\ \vdots\\ \partial_df(\mathbf{x})\end{pmatrix}\in\mathbb{R}^d \tag{3.3}$$

se llama __gradiente__ de $f$ en el punto $\mathbf{x}$. El símbolo $\nabla$ se lee «nabla».
:::

El gradiente tiene la misma forma que $\mathbf{x}$: una entrada por variable, escrita como columna. Esta convención vale en todo el capítulo; la sección [7](ableiten-nach-vektoren-und-matrizen.html#stufe-7) vuelve sobre ella, porque no todos los libros la adoptan. Si se asigna a cada punto $\mathbf{x}$ su gradiente, surge un campo de flechas, una en cada lugar del mapa. Hacia dónde apuntan estas flechas lo aclara la sección [4](richtungsableitung-und-steilster-anstieg.html#stufe-4).

::::beispiel [Ejemplo numérico]
Para $f(\mathbf{x})=x_1^2x_2+x_2^2$ se tiene

$$\nabla f(\mathbf{x})=\begin{pmatrix}2x_1x_2\\ x_1^2+2x_2\end{pmatrix},\qquad \nabla f(1,2)=\begin{pmatrix}4\\5\end{pmatrix},\qquad \nabla f(0,1)=\begin{pmatrix}0\\2\end{pmatrix} .$$

Para la suma de cuadrados $f(\mathbf{x})=x_1^2+x_2^2+x_3^2$, $\nabla f(\mathbf{x})=(2x_1,\,2x_2,\,2x_3)^{\top}=2\mathbf{x}$.
::::

⁠**En resumen:** El gradiente es el vector columna de todas las derivadas parciales, con la misma forma que $\mathbf{x}$.

### La aproximación lineal en el espacio

<span class="anker" id="stufe-3-4"></span>

Para una variable, la recta tangente sustituye a la función cerca de un punto. Con dos variables, su lugar lo ocupa un plano. Bajo la lupa, un terreno suave parece, cerca de un punto, una placa inclinada: es el __plano tangente__. Un plano que pasa por el punto $(\mathbf{x},\,f(\mathbf{x}))$ tiene la forma $f(\mathbf{x})+m_1h_1+m_2h_2$, donde $\mathbf{h}=(h_1,\,h_2)^{\top}$ es el desplazamiento en el mapa y $m_1$, $m_2$ son las inclinaciones de la placa en la dirección de los dos ejes. Para que se ajuste al terreno, sus inclinaciones a lo largo de los ejes deben coincidir con las pendientes de las curvas de corte, es decir, $m_j=\partial_jf(\mathbf{x})$.

De ahí resulta la aproximación lineal para muchas variables:

<span class="anker" id="gl-3-4"></span>
$$f(\mathbf{x}+\mathbf{h})\approx f(\mathbf{x})+\nabla f(\mathbf{x})^{\top}\mathbf{h}=f(\mathbf{x})+\sum_{j=1}^d\partial_jf(\mathbf{x})\,h_j . \tag{3.4}$$

La fórmula dice algo notable: si se modifican varias entradas a la vez en pequeñas cantidades, *sus efectos se suman*. Cada variable aporta $\partial_jf\cdot h_j$, como si se hubiera modificado sola. Con variaciones grandes esto ya no es cierto, porque entonces las variables influyen mutuamente en sus efectos, como en $x_1^2x_2$. Con variaciones pequeñas, estas interacciones son productos de magnitudes pequeñas y desaparecen más rápido que los efectos individuales, exactamente igual que la pieza de la esquina en la regla del producto.

::::beispiel [Ejemplo numérico]
Para $f(\mathbf{x})=x_1^2x_2+x_2^2$ en el punto $\mathbf{x}=(1,\,2)^{\top}$ y el desplazamiento $\mathbf{h}=(0{,}01;\ 0{,}02)^{\top}$ se tiene

$$f(\mathbf{x}+\mathbf{h})\approx f(\mathbf{x})+\nabla f(\mathbf{x})^{\top}\mathbf{h}=6+4\cdot0{,}01+5\cdot0{,}02=6+0{,}14=6{,}14 .$$

El valor exacto es $f(1{,}01;\ 2{,}02)=1{,}0201\cdot2{,}02+2{,}02^2=2{,}060602+4{,}0804=6{,}141002$. El error $0{,}001002$ es mucho menor que la propia variación $0{,}14$. La fig. [7](#abb-7) muestra el producto escalar paso a paso.

:::abbildung ml/k3rlinear 7
La variación de la aproximación lineal como producto escalar del gradiente y el desplazamiento: cada variable aporta su derivada parcial por su propia variación.
:::
::::

⁠**En resumen:** Cerca de $\mathbf{x}$, $f(\mathbf{x}+\mathbf{h})\approx f(\mathbf{x})+\nabla f(\mathbf{x})^{\top}\mathbf{h}$: con variaciones pequeñas, los efectos de las distintas variables se suman.

### Diferenciabilidad

<span class="anker" id="stufe-3-5"></span>

Hasta ahora, la aproximación [(3.4)](#gl-3-4) solo se ha hecho plausible. Para una variable, se seguía de la existencia de la derivada. Con varias variables, la existencia de las derivadas parciales no basta para ello, como muestra el contraejemplo de más abajo. Por eso se exige la propia aproximación: su error debe desaparecer más rápido que el desplazamiento, igual que en [(1.4)](die-ableitung.html#gl-1-4) el error $r(h)$ desaparecía más rápido que $h$. No se puede dividir entre un vector; por eso, en lugar de dividir entre $h$, se divide entre la longitud $\lVert\mathbf{h}\rVert$ del [capítulo 1, sección 3.1](/wissen/es/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/normen-die-groe-eines-vektors.html#stufe-3-1).

:::definition Definición 3.4 (Diferenciabilidad)
<span class="anker" id="satz-3-4"></span>

Una función $f:\mathbb{R}^d\to\mathbb{R}$ se llama __diferenciable__ en el punto $\mathbf{x}$ si existe un vector $\mathbf{g}\in\mathbb{R}^d$ con

<span class="anker" id="gl-3-5"></span>
$$\lim_{\mathbf{h}\to\mathbf{0}}\frac{f(\mathbf{x}+\mathbf{h})-f(\mathbf{x})-\mathbf{g}^{\top}\mathbf{h}}{\lVert\mathbf{h}\rVert}=0 . \tag{3.5}$$

El límite $\mathbf{h}\to\mathbf{0}$ significa: el cociente está arbitrariamente cerca de $0$ en cuanto $\lVert\mathbf{h}\rVert$ es lo bastante pequeño y $\mathbf{h}\ne\mathbf{0}$, sin importar desde qué dirección se acerque $\mathbf{h}$.
:::

:::satz Teorema 3.5 (Diferenciable significa: gradiente y aproximación lineal)
<span class="anker" id="satz-3-5"></span>

Si $f$ es diferenciable en el punto $\mathbf{x}$, allí existen todas las derivadas parciales, y el vector de [(3.5)](#gl-3-5) es el gradiente: $\mathbf{g}=\nabla f(\mathbf{x})$. A la inversa, $f$ es diferenciable en el punto $\mathbf{x}$ si todas las derivadas parciales existen cerca de $\mathbf{x}$ y son continuas en el punto $\mathbf{x}$.
:::

:::beweis El vector es el gradiente
Se elige en [(3.5)](#gl-3-5), en particular, $\mathbf{h}=t\,\mathbf{e}_j$ con un número $t\ne0$; entonces $\lVert\mathbf{h}\rVert=|t|$ y $\mathbf{g}^{\top}\mathbf{h}=t\,g_j$. El cociente es $\frac{f(\mathbf{x}+t\mathbf{e}_j)-f(\mathbf{x})-t\,g_j}{|t|}$ y tiende a $0$. Entonces también $\frac{f(\mathbf{x}+t\mathbf{e}_j)-f(\mathbf{x})}{t}-g_j$ tiende a $0$, pues este número tiene el mismo valor absoluto. Así pues, la derivada parcial respecto de $x_j$ existe y es $g_j$. Esto vale para cada $j$.
:::

Para la práctica es importante la segunda afirmación. Los polinomios, la función exponencial, la función logística y todo lo que se construye a partir de ellos mediante operaciones aritméticas básicas y composición tienen derivadas parciales continuas en todos los puntos donde están definidos. Tales funciones son, por tanto, diferenciables, y para ellas vale [(3.4)](#gl-3-4). Las excepciones en este capítulo son los puntos angulosos, como en $|x|$ o $\max(x,\,0)$.

:::warnung Las derivadas parciales por sí solas no bastan
La función $f(x_1,x_2)=\dfrac{x_1x_2}{x_1^2+x_2^2}$ con $f(0,0)=0$ es nula sobre ambos ejes, pues allí $x_1x_2=0$. Sus curvas de corte por el origen a lo largo de los ejes son, por tanto, horizontales: $\partial_1f(0,0)=\partial_2f(0,0)=0$, y el gradiente en el origen es $\mathbf{0}$. Por eso, la aproximación lineal predice que $f$ es casi $0$ cerca del origen. Pero sobre la diagonal $x_1=x_2=t$ con $t\ne0$ se tiene $f(t,t)=t^2/(2t^2)=\tfrac12$, por pequeño que sea $t$. La función salta en el origen, y ningún plano se ajusta a ella. Allí no es diferenciable, aunque existen ambas derivadas parciales. Quien deduce la aproximación lineal de la existencia del gradiente necesita, por tanto, la diferenciabilidad, por ejemplo a través de derivadas parciales continuas.
:::

::::beispiel [Ejemplo numérico]
Para $f(\mathbf{x})=x_1^2x_2+x_2^2$, las derivadas parciales $2x_1x_2$ y $x_1^2+2x_2$ son polinomios, por tanto continuas en todas partes, y $f$ es diferenciable en todas partes. En el ejemplo numérico de [(3.4)](#gl-3-4), el error era $0{,}001002$ con $\lVert\mathbf{h}\rVert=\sqrt{0{,}0001+0{,}0004}\approx0{,}0224$, de modo que el cociente de [(3.5)](#gl-3-5) era aproximadamente $0{,}045$. Si se reduce $\mathbf{h}$ a la mitad, a $(0{,}005;\ 0{,}01)^{\top}$, el error es $f(1{,}005;\ 2{,}01)-6-0{,}07=0{,}000250\ldots$ y el cociente es aproximadamente $0{,}022$: se reduce a la mitad con $\mathbf{h}$ y tiende a $0$.
::::

⁠**En resumen:** Diferenciable significa que la aproximación lineal con el gradiente tiene un error que desaparece más rápido que $\lVert\mathbf{h}\rVert$; las derivadas parciales continuas lo garantizan, su mera existencia no.

:::hintergrund Por qué bastan las derivadas parciales continuas
No se va de $\mathbf{x}$ a $\mathbf{x}+\mathbf{h}$ en diagonal, sino en dos tramos paralelos a los ejes: primero $h_1$ en la dirección $x_1$, después $h_2$ en la dirección $x_2$. En cada tramo cambia solo una variable y, según el teorema del valor medio para una variable, la variación es exactamente $\partial_jf\cdot h_j$, evaluada en un punto intermedio del tramo. Si las derivadas parciales son continuas, sus valores en los puntos intermedios están cerca de los valores en el punto $\mathbf{x}$, y la suma de los dos tramos se diferencia de $\nabla f(\mathbf{x})^{\top}\mathbf{h}$ solo en una cantidad que desaparece más rápido que $\lVert\mathbf{h}\rVert$. En el contraejemplo falla justamente este paso: sus derivadas parciales existen fuera del origen, pero no son continuas. Sobre el eje $x_1=0$, por ejemplo, $\partial_1f(0,x_2)=1/x_2$, y esto se hace arbitrariamente grande cuanto más se acerca uno al origen, donde el valor es $0$.
:::

:::aufgabe Ejercicio 9 ★ Derivadas parciales y gradientes
<span class="anker" id="aufg-9"></span>

Calcula las derivadas parciales y el gradiente en el punto indicado.

<ol class="al">

<li>

$f(\mathbf{x})=3x_1-2x_2+5$ en el punto $(4,\,-1)$;

</li>

<li>

$f(\mathbf{x})=x_1\,\mathrm{e}^{x_2}$ en los puntos $(2,\,0)$ y $(1,\,1)$;

</li>

<li>

$f(\mathbf{x})=x_1x_2+x_2x_3+x_3x_1$ en el punto $(1,\,2,\,3)$.

</li>

</ol>

:::loesung
(a) $\partial_1f=3$, $\partial_2f=-2$, así que $\nabla f=(3,\,-2)^{\top}$ en todos los puntos.

(b) $\partial_1f=\mathrm{e}^{x_2}$ y $\partial_2f=x_1\mathrm{e}^{x_2}$. En el punto $(2,\,0)$ se tiene $\nabla f=(1,\,2)^{\top}$; en el punto $(1,\,1)$, $\nabla f=(\mathrm{e},\,\mathrm{e})^{\top}\approx(2{,}718;\ 2{,}718)^{\top}$.

(c) $\partial_1f=x_2+x_3$, $\partial_2f=x_1+x_3$, $\partial_3f=x_1+x_2$; en el punto $(1,\,2,\,3)$, por tanto, $\nabla f=(5,\,4,\,3)^{\top}$.
:::
:::

:::aufgabe Ejercicio 10 ★★ Aproximación lineal con dos variables
<span class="anker" id="aufg-10"></span>

Sea $f(\mathbf{x})=x_1\,\mathrm{e}^{x_2}$.

<ol class="al">

<li>

Calcula con la aproximación lineal en el punto $(2,\,0)$ un valor aproximado de $f(2{,}1;\ -0{,}05)$ y compáralo con el valor exacto.

</li>

<li>

¿Cuál de las dos variaciones contribuye más a la variación de $f$? ¿Por qué se compensan exactamente en la aproximación lineal, pero no en el valor exacto?

</li>

</ol>

:::loesung
(a) Se tiene $f(2,0)=2$ y $\nabla f(2,0)=(1,\,2)^{\top}$ según el ejercicio [9](#aufg-9). Con $\mathbf{h}=(0{,}1;\ -0{,}05)^{\top}$:

$$f(2{,}1;\ -0{,}05)\approx2+1\cdot0{,}1+2\cdot(-0{,}05)=2+0{,}1-0{,}1=2{,}0 .$$

El valor exacto es $2{,}1\,\mathrm{e}^{-0{,}05}\approx2{,}1\cdot0{,}951229\approx1{,}99758$. El error es de unos $0{,}0024$.

(b) Ambas variaciones contribuyen lo mismo, $+0{,}1$ y $-0{,}1$, y se compensan en la aproximación lineal. En el valor exacto, sin embargo, las variables se influyen mutuamente: si $x_1$ aumenta, $f$ reacciona con más fuerza a $x_2$, pues $\partial_2f=x_1\mathrm{e}^{x_2}$ crece con $x_1$. Por eso, la disminución de $x_2$ actúa con algo más de fuerza de lo que supone la aproximación lineal. Estas interacciones son productos de dos variaciones, aquí por ejemplo $0{,}1\cdot(-0{,}05)=-0{,}005$, y pertenecen a los términos de segundo orden que la aproximación lineal omite. La sección [8](die-hesse-matrix-und-die-quadratische-naherung.html#stufe-8) los calcula (ejercicio [29](die-hesse-matrix-und-die-quadratische-naherung.html#aufg-29)).
:::
:::

:::aufgabe Ejercicio 11 ★★ Curvas de nivel y curvas de corte
<span class="anker" id="aufg-11"></span>

Sea $f(\mathbf{x})=x_1^2x_2+x_2^2$ como en [(3.1)](#gl-3-1).

<ol class="al">

<li>

¿Qué valor tiene $f$ en el punto $(2,\,1)$? Da otro punto de la misma curva de nivel con $x_1=0$.

</li>

<li>

Calcula $\nabla f(2,1)$ y las ecuaciones de las dos curvas de corte que pasan por $(2,\,1)$. Comprueba sus pendientes.

</li>

</ol>

:::loesung
(a) $f(2,1)=4\cdot1+1=5$. Con $x_1=0$, la curva de nivel exige $x_2^2=5$; por tanto, por ejemplo, $(0;\ \sqrt5)\approx(0;\ 2{,}236)$ está en ella.

(b) $\nabla f(2,1)=(2\cdot2\cdot1,\ 4+2\cdot1)^{\top}=(4,\,6)^{\top}$. La curva de corte a lo largo de $x_2=1$ es $f(x_1,1)=x_1^2+1$, con la pendiente $2x_1=4$ en $x_1=2$. La curva de corte a lo largo de $x_1=2$ es $f(2,x_2)=4x_2+x_2^2$, con la pendiente $4+2x_2=6$ en $x_2=1$. Ambas pendientes coinciden con las componentes del gradiente.
:::
:::

:::aufgabe Ejercicio 12 ★★★ Continua, pero no diferenciable
<span class="anker" id="aufg-12"></span>

Sea $f(x_1,x_2)=\sqrt{|x_1x_2|}$.

<ol class="al">

<li>

Demuestra que ambas derivadas parciales existen en el origen y valen $0$.

</li>

<li>

Demuestra con $\mathbf{h}=(t,\,t)^{\top}$ que el cociente de [(3.5)](#gl-3-5) con $\mathbf{g}=\mathbf{0}$ no tiende a $0$. ¿Por qué se sigue de ello que $f$ no es diferenciable en el origen, aunque $f$ sea continua allí?

</li>

</ol>

:::loesung
(a) Sobre ambos ejes se tiene $x_1x_2=0$, así que $f=0$. Por tanto, $\frac{f(h,0)-f(0,0)}{h}=0$ para todo $h\ne0$, y lo mismo ocurre con la segunda variable. Ambas derivadas parciales en el origen valen $0$.

(b) Si $f$ fuera diferenciable en el origen, el vector de [(3.5)](#gl-3-5) tendría que ser, según el teorema de la sección [3.5](#stufe-3-5), el gradiente $\mathbf{0}$. Pero con $\mathbf{h}=(t,\,t)^{\top}$ se tiene $f(\mathbf{h})=\sqrt{t^2}=|t|$ y $\lVert\mathbf{h}\rVert=\sqrt2\,|t|$, así que

$$\frac{f(\mathbf{h})-f(\mathbf{0})-\mathbf{0}^{\top}\mathbf{h}}{\lVert\mathbf{h}\rVert}=\frac{|t|}{\sqrt2\,|t|}=\frac1{\sqrt2}\approx0{,}707 ,$$

para todo $t\ne0$, por pequeño que sea. El cociente no tiende a $0$; por tanto, $f$ no es diferenciable. Aun así, $f$ es continua, pues $|f(\mathbf{x})|=\sqrt{|x_1|\,|x_2|}\le\max(|x_1|,|x_2|)\le\lVert\mathbf{x}\rVert$ tiende a $0$ cuando $\mathbf{x}$ tiende a $\mathbf{0}$. El terreno no tiene ningún hueco en el origen, pero sí un pliegue a lo largo de la diagonal, al que no se ajusta ningún plano.
:::
:::

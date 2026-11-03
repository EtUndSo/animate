---
title: El truco: amortiguar, descomponer, compensar
pfad: Ingeniería eléctrica / 3.er semestre / Señales y sistemas / Transformada de Laplace
order: 3220400
summary: Toda señal como superposición de $\mathrm{e}^{pt}$, y por qué un sistema LTI convierte esto en una multiplicación
tags: densidad
lang: es
---

<span class="anker" id="stufe-2-2"></span>

**La idea.** Primero se hace descomponible la señal y después se deshace el cambio:

<ol>

<li>

⁠**Amortiguar.** Se multiplica por $\mathrm{e}^{-\sigma t}$. Si una señal por la derecha crece como mucho como $\mathrm{e}^{\alpha t}$, $s(t)\,\mathrm{e}^{-\sigma t}$ decae para todo $\sigma>\alpha$ y es absolutamente integrable.

</li>

<li>

⁠**Descomponer.** La señal amortiguada es una superposición de oscilaciones puras. Su espectro de Fourier es exactamente la transformada de Laplace $S(p)=\int s(t)\,\mathrm{e}^{-pt}\mathrm{d} t$ sobre la recta $\operatorname{Re} p=\sigma$ (ejercicio [2](konvergenzbereich-welche-dampfungen-funktionieren.html#aufg-2)):

$$\mathcal{F}\bigl\{s(t)\,\mathrm{e}^{-\sigma t}\bigr\}(f)=S(\sigma+\mathrm{j}2\pi f).$$

</li>

<li>

⁠**Compensar.** Se multiplica la descomposición por $\mathrm{e}^{\sigma t}$. El factor no depende de $f$ y puede entrar en la integral. Allí convierte cada oscilación $\mathrm{e}^{\mathrm{j}2\pi ft}$ en el bloque elemental $\mathrm{e}^{(\sigma+\mathrm{j}2\pi f)t}=\mathrm{e}^{pt}$.

</li>

</ol>

El resultado es la superposición que se suponía.

:::satz Teorema 2.1 (Fórmula de inversión de la transformada de Laplace)
<span class="anker" id="satz-2-1"></span>

Si $\sigma$ está en la región de convergencia de $S(p)$, se cumple

<span class="anker" id="gl-2-1"></span>
$$s(t)=\frac{1}{2\pi\mathrm{j}}\int_{\sigma-\mathrm{j}\infty}^{\sigma+\mathrm{j}\infty}S(p)\,\mathrm{e}^{pt}\,\mathrm{d} p =\int_{-\infty}^{\infty}S(\sigma+\mathrm{j}2\pi f)\,\mathrm{e}^{(\sigma+\mathrm{j}2\pi f)t}\,\mathrm{d} f. \tag{2.1}$$
:::

⁠**Cómo leerlo:**

<ul>

<li>

El camino de integración es la recta vertical $\operatorname{Re} p=\sigma$ del plano $p$, recorrida de abajo arriba ($f$ de $-\infty$ a $+\infty$, fig. [2](#abb-2)).

</li>

<li>

$\mathrm{e}^{pt}$ es el bloque elemental, y $S(p)\,\mathrm{d} p/(2\pi\mathrm{j})=S(\sigma+\mathrm{j}2\pi f)\,\mathrm{d} f$, su peso complejo. $S(p)$ misma es una __densidad__: peso por intervalo de frecuencia. Si $s$ es una tensión en V, $S$ tiene la unidad V s.

</li>

<li>

La integral se entiende como el límite $\lim_{F\to\infty}\int_{-F}^{F}\dots\mathrm{d} f$. Da $s(t)$ en todo punto en que $s$ es continua y, en un punto de salto, la media de los límites por la izquierda y por la derecha.

</li>

</ul>

⁠**Caso límite $\sigma=0$:** si el eje imaginario está en la región de convergencia, puede elegirse $\sigma=0$. Entonces $p=\mathrm{j}2\pi f$, y [(2.1)](#gl-2-1) se convierte en la fórmula de inversión de Fourier. La transformada de Laplace contiene la transformada de Fourier como caso particular.

:::herleitung fórmula de inversión a partir de la de Fourier
Según el paso 2, $S(\sigma+\mathrm{j}2\pi f)$ es el espectro de Fourier de $s(t)\mathrm{e}^{-\sigma t}$. La fórmula de inversión de Fourier da

$$s(t)\,\mathrm{e}^{-\sigma t}=\int_{-\infty}^{\infty}S(\sigma+\mathrm{j}2\pi f)\,\mathrm{e}^{\mathrm{j}2\pi ft}\,\mathrm{d} f.$$

Multiplicación por $\mathrm{e}^{\sigma t}$, que no depende de $f$:

$$s(t)=\int_{-\infty}^{\infty}S(\sigma+\mathrm{j}2\pi f)\,\mathrm{e}^{(\sigma+\mathrm{j}2\pi f)t}\,\mathrm{d} f.$$

Cambio de variable $p=\sigma+\mathrm{j}2\pi f$ con $\sigma$ fijo: $\mathrm{d} p=\mathrm{j}2\pi\,\mathrm{d} f$, es decir, $\mathrm{d} f=\mathrm{d} p/(2\pi\mathrm{j})$. Los límites $f=\mp\infty$ pasan a ser $p=\sigma\mp\mathrm{j}\infty$:

$$s(t)=\frac{1}{2\pi\mathrm{j}}\int_{\sigma-\mathrm{j}\infty}^{\sigma+\mathrm{j}\infty}S(p)\,\mathrm{e}^{pt}\,\mathrm{d} p.$$
:::

**Ejemplo: el escalón a partir de bloques elementales.** Para $\varepsilon(t)$, $S(p)=1/p$ con $\operatorname{Re} p>0$. Se elige $\sigma=0{,}5/\mathrm s$ (fig. [2](#abb-2)). La figura [3](#abb-3) muestra lo que resulta si solo se superponen los bloques con $|f|\le F$. Ya con $F=0{,}25$ Hz se reconoce la forma del escalón. Al crecer $F$, el flanco se hace más abrupto; en $t=0$ la curva tiende al valor medio $\tfrac12$ (0,40; 0,47; 0,49), y en $t=-1$ s, a cero (0,053; 0,029; 0,008).

:::abbildung et3/k2linie 2
Plano $p$ para el escalón $\varepsilon(t)$, $S(p)=1/p$. La región de convergencia (fondo azul) está a la derecha del polo $p=0$. Cualquier recta vertical dentro de ella sirve como camino de integración; aquí, $\sigma=0{,}5/\mathrm s$. Cada punto de la recta es un bloque elemental $\mathrm{e}^{pt}$ con el peso $S(p)$.
:::

:::abbildung et3/k2sprung 3
El escalón, superpuesto a partir de los bloques elementales $\mathrm{e}^{pt}$ sobre la recta $\operatorname{Re} p=0{,}5/\mathrm s$, tomando solo los bloques con $|f|\le F$: $s_F(t)=\int_{-F}^{F}S(\sigma+\mathrm{j}2\pi f)\,\mathrm{e}^{(\sigma+\mathrm{j}2\pi f)t}\mathrm{d} f$ con $S(p)=1/p$. Cuantos más bloques, más exacto es el escalón; en $t=0$ la curva tiende a $\tfrac12$.
:::

:::frage Todos los bloques elementales son complejos. ¿Por qué sale una curva real?
Los bloques aparecen por parejas: a $f$ le corresponde $-f$, es decir, a $p$ el punto conjugado $p^*$. Para una señal real, el peso allí es el conjugado, $S(p^*)=S(p)^*$ (lo muestra el cálculo $S(p)=\int s(t)\mathrm{e}^{-pt}\mathrm{d} t$ con $s$ real). Cada pareja da $S\mathrm{e}^{pt}+(S\mathrm{e}^{pt})^*=2\operatorname{Re}\{S(p)\mathrm{e}^{pt}\}$, es decir, una oscilación real, amortiguada o creciente. Las partes imaginarias se cancelan por parejas.
:::

:::frage Entonces, ¿es una suma o una integral?
En general, una integral: sobre la recta hay un continuo de bloques elementales, cada uno con un peso infinitesimal $S\,\mathrm{d} f$.
:::

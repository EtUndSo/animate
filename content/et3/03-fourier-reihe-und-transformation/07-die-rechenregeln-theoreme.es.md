---
title: Etapa 6: Las reglas de cálculo (teoremas)
pfad: Ingeniería eléctrica / 3.er semestre / ET3 – Fundamentos de ingeniería eléctrica 3: señales y sistemas / Serie y transformada de Fourier
adresse: elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation
knoten: Capítulo 3: Serie y transformada de Fourier
order: 3230700
summary: En lugar de calcular cada integral de nuevo, se usan reglas: ¿qué le ocurre al espectro si se desplaza, se comprime, se deriva o se modula la señal?
tags: densidad de energía
lang: es
---

<span class="anker" id="stufe-6"></span>

:::zweck
En lugar de calcular cada integral de nuevo, se usan reglas: ¿qué le ocurre al espectro si se desplaza, se comprime, se deriva o se modula la señal? Cada regla se deduce de lo que la operación hace con una única oscilación.
:::

:::satz Teorema 6.1 (Teoremas de la transformada de Fourier)
<span class="anker" id="satz-6-1"></span>

<span class="anker" id="gl-6-1"></span>
<span class="anker" id="gl-6-2"></span>
<span class="anker" id="gl-6-3"></span>
<span class="anker" id="gl-6-4"></span>
<span class="anker" id="gl-6-5"></span>
<span class="anker" id="gl-6-6"></span>
<span class="anker" id="gl-6-7"></span>
<span class="anker" id="gl-6-8"></span>
<span class="anker" id="gl-6-9"></span>
<span class="anker" id="gl-6-10"></span>
<span class="anker" id="gl-6-11"></span>
$$\begin{aligned} &\text{Superposición:} && \textstyle\sum_ia_is_i(t)\;\circ\!\!-\!\!\bullet\;\sum_ia_iS_i(f)\\ &\text{Conjugación:} && s^*(t)\;\circ\!\!-\!\!\bullet\;S^*(-f)\\ &\text{Escalado (semejanza):} && s(bt)\;\circ\!\!-\!\!\bullet\;\frac{1}{|b|}S\Bigl(\frac fb\Bigr),\quad b\neq0;\qquad s(-t)\;\circ\!\!-\!\!\bullet\;S(-f)\\ &\text{Desplazamiento:} && s(t-t_0)\;\circ\!\!-\!\!\bullet\;S(f)\,\mathrm{e}^{-\mathrm{j}2\pi ft_0},\qquad\delta(t-t_0)\;\circ\!\!-\!\!\bullet\;\mathrm{e}^{-\mathrm{j}2\pi ft_0}\\ &\text{Derivación:} && \frac{\mathrm{d}^n}{\mathrm{d} t^n}s(t)\;\circ\!\!-\!\!\bullet\;(\mathrm{j}2\pi f)^nS(f)\\ &\text{Simetría (dualidad):} && S(t)\;\circ\!\!-\!\!\bullet\;s(-f)\\ &\text{Modulación:} && \mathrm{e}^{\mathrm{j}2\pi Ft}s(t)\;\circ\!\!-\!\!\bullet\;S(f-F)\\ &\text{Derivación en frecuencia:} && -\mathrm{j}2\pi t\,s(t)\;\circ\!\!-\!\!\bullet\;\frac{\mathrm{d}}{\mathrm{d} f}S(f)\\ &\text{Convolución, multiplicación:} && s_1*s_2\;\circ\!\!-\!\!\bullet\;S_1S_2,\qquad s_1s_2\;\circ\!\!-\!\!\bullet\;S_1*S_2\\ &\text{Áreas:} && \int s(t)\mathrm{d} t=S(0),\qquad\int S(f)\mathrm{d} f=s(0)\\ &\text{Parseval:} && \int|s(t)|^2\mathrm{d} t=\int|S(f)|^2\mathrm{d} f \end{aligned} \tag{6.1|6.2|6.3|6.4|6.5|6.6|6.7|6.8|6.9|6.10|6.11}$$
:::

⁠**Cómo leer los más importantes:**

<ul>

<li>

⁠**Escalado (semejanza):** una señal comprimida en el tiempo ($|b|>1$) tiene un espectro más ancho. Las señales cortas necesitan muchas frecuencias. La duración y el ancho de banda varían en sentido inverso.

</li>

<li>

⁠**Desplazamiento:** un retardo no cambia el módulo, solo la fase, y lo hace de forma lineal en $f$: cada oscilación se desplaza el mismo tiempo, lo que a mayor frecuencia supone un ángulo mayor.

</li>

<li>

⁠**Derivación:** $\frac{\mathrm{d}}{\mathrm{d} t}\mathrm{e}^{\mathrm{j}2\pi ft}=\mathrm{j}2\pi f\,\mathrm{e}^{\mathrm{j}2\pi ft}$. Derivar amplifica las frecuencias altas.

</li>

<li>

⁠**Simetría:** la transformada directa y la inversa solo se diferencian en el signo del exponente. Por eso cada par de transformadas da un segundo par con los papeles intercambiados.

</li>

<li>

⁠**Modulación:** multiplicar por $\mathrm{e}^{\mathrm{j}2\pi Ft}$ desplaza todo el espectro en $F$. Así funciona toda emisora de radio.

</li>

<li>

⁠**Multiplicación:** el producto de dos señales tiene como espectro la convolución de los espectros; es la contrapartida del teorema de convolución.

</li>

<li>

⁠**Parseval:** la energía es la misma en ambos dominios. $|S(f)|^2$ es la __densidad de energía__ en función de la frecuencia.

</li>

</ul>

:::herleitung Escalado, desplazamiento, derivación, simetría, modulación, multiplicación, Parseval
⁠**Escalado** ($b>0$, $\tau=bt$): $\int s(bt)\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t=\frac1b\int s(\tau)\mathrm{e}^{-\mathrm{j}2\pi(f/b)\tau}\mathrm{d}\tau=\frac1bS(f/b)$. Para $b<0$ se invierten los límites; de ahí $1/|b|$.

⁠**Desplazamiento** ($\tau=t-t_0$): $\int s(\tau)\mathrm{e}^{-\mathrm{j}2\pi f(\tau+t_0)}\mathrm{d}\tau=\mathrm{e}^{-\mathrm{j}2\pi ft_0}S(f)$. Con $s=\delta$ se obtiene el par para $\delta(t-t_0)$.

⁠**Derivación:** derivar la transformada inversa respecto a $t$, $\frac{\mathrm{d}}{\mathrm{d} t}\int S\mathrm{e}^{\mathrm{j}2\pi ft}\mathrm{d} f=\int\mathrm{j}2\pi f\,S\,\mathrm{e}^{\mathrm{j}2\pi ft}\mathrm{d} f$.

⁠**Simetría:** en la transformada inversa, sustituir $t$ por $-t$: $s(-t)=\int S(f)\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} f$. Ahora intercambiar los nombres de las variables $t$ y $f$: $s(-f)=\int S(t)\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t$, que es la transformada directa de $S(t)$.

⁠**Modulación:** $\int\mathrm{e}^{\mathrm{j}2\pi Ft}s(t)\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t=\int s(t)\mathrm{e}^{-\mathrm{j}2\pi(f-F)t}\mathrm{d} t=S(f-F)$. La derivación en el dominio de la frecuencia se obtiene igualmente derivando la transformada directa respecto a $f$.

⁠**Multiplicación:** teorema de convolución para las señales $s_1(t)$ y $s_2(t)$, es decir, $s_1*s_2\;\circ\!\!-\!\!\bullet\;S_1S_2$; después, aplicar la simetría a este par: $S_1(t)S_2(t)\;\circ\!\!-\!\!\bullet\;s_1(-f)*s_2(-f)$. Renombrando se obtiene [(6.9)](#gl-6-9).

⁠**Áreas:** sustituir $f=0$ en la transformada directa y $t=0$ en la inversa.

⁠**Parseval:** $\int|s|^2\mathrm{d} t=\int s\,s^*\mathrm{d} t$ es el producto $s(t)s^*(t)$ integrado; por tanto, según la multiplicación, la conjugación y el teorema del área, $\bigl[S(f)*S^*(-f)\bigr]_{f=0}=\int S(\nu)S^*(\nu)\mathrm{d}\nu$.
:::

:::frage ¿Por qué un retardo no cambia el módulo del espectro?
Porque un retardo no atenúa ni amplifica ninguna oscilación; solo desplaza cada una. Cada oscilación se desplaza el mismo tiempo $t_0$, lo que a la frecuencia $f$ corresponde al ángulo $2\pi ft_0$. Por eso la fase es una recta en $f$ con pendiente $-2\pi t_0$. Un sistema con $|H|=1$ y fase lineal retrasa una señal sin cambiar su forma.
:::

:::aufgabe Ejercicio 6 ★★ Aplicar los teoremas
<span class="anker" id="aufg-6"></span>

Usa $\operatorname{rect}(t)\;\circ\!\!-\!\!\bullet\;\operatorname{si}(\pi f)$ (directamente de la definición: $\int_{-1/2}^{1/2}\mathrm{e}^{-\mathrm{j}2\pi ft}\,\mathrm{d} t=\operatorname{si}(\pi f)$) y los teoremas.

<ol class="al">

<li>

Determina el espectro de un pulso rectangular de altura 1 desde $t=0$ hasta $t=2$ s. ¿Cuánto vale su módulo en $f=0$ y dónde está el primer cero?

</li>

<li>

Determina el espectro de $\cos(2\pi F_0t)\operatorname{rect}(t)$ con $F_0=5$ Hz y esbózalo.

</li>

</ol>

:::loesung
(a) El pulso es $\operatorname{rect}\bigl(\frac{t-1}{2}\bigr)$. Escalado ($T=2$) y desplazamiento ($t_0=1$ s): $2\operatorname{si}(2\pi f)\,\mathrm{e}^{-\mathrm{j}2\pi f}$. Módulo en $f=0$: 2 (el área). Primer cero en $f=0{,}5$ Hz. El desplazamiento solo cambia la fase.

(b) $\cos(2\pi F_0t)=\frac12\mathrm{e}^{\mathrm{j}2\pi F_0t}+\frac12\mathrm{e}^{-\mathrm{j}2\pi F_0t}$; modulación: $\frac12\operatorname{si}(\pi(f-5))+\frac12\operatorname{si}(\pi(f+5))$. Dos lóbulos principales si de altura $\frac12$ en $\pm5$ Hz, con los primeros ceros a 1 Hz a cada lado.
:::
:::

:::aufgabe Ejercicio 7 ★★ La simetría como herramienta
<span class="anker" id="aufg-7"></span>

Por el ejercicio [4](vom-periodischen-zum-einmaligen-signal.html#aufg-4) sabes que $\mathrm{e}^{-|t|}\;\circ\!\!-\!\!\bullet\;\frac{2}{1+(2\pi f)^2}$. Con ello, determina sin integrales el espectro de $\frac{1}{1+t^2}$.

:::loesung
Aplicar la simetría al par: $\frac{2}{1+(2\pi t)^2}\;\circ\!\!-\!\!\bullet\;\mathrm{e}^{-|f|}$. Ahora dilatar el tiempo. Con $x(t)=\frac{2}{1+(2\pi t)^2}$ se tiene $x\bigl(\frac{t}{2\pi}\bigr)=\frac{2}{1+t^2}$; por el teorema de escalado (semejanza) con $b=\frac1{2\pi}$, esto da $\circ\!\!-\!\!\bullet\;2\pi\,\mathrm{e}^{-2\pi|f|}$. Dividir entre dos:

$$\frac{1}{1+t^2}\;\circ\!\!-\!\!\bullet\;\pi\,\mathrm{e}^{-2\pi|f|}.$$

Comprobación con el teorema del área: $\int\frac{\mathrm{d} t}{1+t^2}=\pi=S(0)$.
:::
:::

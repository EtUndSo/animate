---
title: Etapa 2: Señales periódicas, la serie de Fourier
pfad: Ingeniería eléctrica / 3.er semestre / Señales y sistemas / Serie y transformada de Fourier
order: 3230300
summary: Una señal periódica se repite al cabo de T .
tags: frecuencia fundamental, armónicos, serie de Fourier, componente continua, ortogonales
lang: es
---

<span class="anker" id="stufe-2"></span>

:::zweck
Una señal periódica se repite al cabo de $T$. Se puede componer a partir de oscilaciones, pero solo de unas muy concretas. Esta etapa muestra de cuáles y cómo se hallan sus pesos.
:::

**La idea.** Una oscilación $\mathrm{e}^{\mathrm{j}2\pi ft}$ se repite al cabo de $T$ si y solo si $fT$ es un número entero. Por tanto, en una señal de periodo $T$ solo aparecen las frecuencias $f_k=kF$, con la __frecuencia fundamental__ $F=1/T$; son los __armónicos__:

<span class="anker" id="gl-2-1"></span>
$$s_p(t)=\sum_{k=-\infty}^{\infty}S_p(k)\,\mathrm{e}^{\mathrm{j}2\pi kFt}. \tag{2.1}$$

Esta es la __serie de Fourier__ (síntesis). $S_p(k)$ es el peso complejo del $k$-ésimo armónico.

**Señales reales.** Para una señal real, $s_p=s_p^*$. Al conjugar [(2.1)](#gl-2-1), $\mathrm{e}^{\mathrm{j}2\pi kFt}$ se convierte en la oscilación con $-k$. Comparando los coeficientes se obtiene

$$S_p(-k)=S_p^*(k).$$

Cada par $k,-k$ da entonces $2\operatorname{Re}\{S_p(k)\mathrm{e}^{\mathrm{j}2\pi kFt}\}$, una oscilación cosenoidal real. Con $S_p(k)=|S_p(k)|\,\mathrm{e}^{\mathrm{j}\varphi_p(k)}$:

<span class="anker" id="gl-2-2"></span>
<span class="anker" id="gl-2-3"></span>
$$\begin{aligned} s_p(t)&=S_p(0)+2\sum_{k=1}^{\infty}|S_p(k)|\cos\bigl(2\pi kFt+\varphi_p(k)\bigr)\\ &=S_p(0)+2\sum_{k=1}^{\infty}\Bigl[\operatorname{Re}\{S_p(k)\}\cos(2\pi kFt)-\operatorname{Im}\{S_p(k)\}\sin(2\pi kFt)\Bigr]. \end{aligned} \tag{2.2|2.3}$$

La fase $\varphi_p(k)$ se determina como en cualquier número complejo, con $\arctan$ y la corrección de cuadrante ($+\pi$ si la parte real es negativa). $S_p(0)$ es la __componente continua__, el valor medio de la señal.

**Hallar los pesos: ortogonalidad.** ¿Cómo se extrae un único $S_p(n)$ de la suma? Se multiplica por $\mathrm{e}^{-\mathrm{j}2\pi nFt}$ y se promedia sobre un periodo. Al hacerlo desaparecen todos los demás armónicos:

<span class="anker" id="gl-2-4"></span>
$$\frac1T\int_0^T\mathrm{e}^{\mathrm{j}2\pi(k-n)Ft}\,\mathrm{d} t=\begin{cases}1&k=n\\0&k\neq n\end{cases}. \tag{2.4}$$

Para $k\neq n$, el fasor $\mathrm{e}^{\mathrm{j}2\pi(k-n)Ft}$ da exactamente $|k-n|$ vueltas completas en el periodo, y su valor medio es cero. Para $k=n$ está quieto. Por eso, las oscilaciones de frecuencias distintas se llaman __ortogonales__. Queda:

:::satz Teorema 2.1 (Serie de Fourier)
<span class="anker" id="satz-2-1"></span>

Una señal de periodo $T=1/F$ y potencia finita tiene la representación [(2.1)](#gl-2-1) con

<span class="anker" id="gl-2-5"></span>
$$S_p(k)=\frac1T\int_{t_1}^{t_1+T}s_p(t)\,\mathrm{e}^{-\mathrm{j}2\pi kFt}\,\mathrm{d} t, \tag{2.5}$$

donde $t_1$ es arbitrario (análisis).
:::

⁠**Cómo leerlo:** $S_p(k)$ es el valor medio de la señal después de «girarla en sentido contrario» con el $k$-ésimo armónico. Si el armónico está en la señal, su fasor deja de girar y su contribución se conserva en el promedio. $S_p(0)$ es simplemente el valor medio.

:::herleitung Fórmula de análisis
Multiplicar [(2.1)](#gl-2-1) por $\mathrm{e}^{-\mathrm{j}2\pi nFt}$, integrar sobre un periodo e intercambiar suma e integral:

$$\int_0^Ts_p(t)\mathrm{e}^{-\mathrm{j}2\pi nFt}\mathrm{d} t=\sum_kS_p(k)\int_0^T\mathrm{e}^{\mathrm{j}2\pi(k-n)Ft}\mathrm{d} t=S_p(n)\,T.$$

Para $k\neq n$, la integral vale $\frac{\mathrm{e}^{\mathrm{j}2\pi(k-n)FT}-1}{\mathrm{j}2\pi(k-n)F}=0$, porque $\mathrm{e}^{\mathrm{j}2\pi(k-n)}=1$. Como el integrando tiene periodo $T$, se puede integrar sobre cualquier intervalo de longitud $T$.
:::

**Ejemplo: una serie finita.** $s_p(t)=1+2\cos(2\pi Ft)+\sin(4\pi Ft)$. Con las fórmulas de Euler, los coeficientes se leen directamente, sin integrar:

$$2\cos(2\pi Ft)=\mathrm{e}^{\mathrm{j}2\pi Ft}+\mathrm{e}^{-\mathrm{j}2\pi Ft},\qquad\sin(4\pi Ft)=\frac{1}{2\mathrm{j}}\mathrm{e}^{\mathrm{j}4\pi Ft}-\frac{1}{2\mathrm{j}}\mathrm{e}^{-\mathrm{j}4\pi Ft},$$

es decir, $S_p(0)=1$, $S_p(\pm1)=1$, $S_p(2)=-\tfrac{\mathrm{j}}{2}$, $S_p(-2)=\tfrac{\mathrm{j}}{2}$, todos los demás nulos. Comprobación: $S_p(-2)=S_p^*(2)$.

**Ejemplo: la onda cuadrada.** Para el modelo de referencia (1 para $|t|\le T_1/2$, con $T_1=T/2$):

<span class="anker" id="gl-2-6"></span>
$$S_p(0)=\frac{T_1}{T},\qquad S_p(k)=\frac1T\int_{-T_1/2}^{T_1/2}\mathrm{e}^{-\mathrm{j}2\pi kFt}\mathrm{d} t=\frac{\sin(\pi kT_1/T)}{\pi k}\quad(k\neq0). \tag{2.6}$$

Con $T_1=T/2$: $S_p(0)=0{,}5$, $S_p(\pm1)=1/\pi=0{,}318$, $S_p(\pm2)=0$, $S_p(\pm3)=-0{,}106$, $S_p(\pm5)=0{,}064$. Faltan los armónicos pares, porque $\sin(\pi k/2)=0$ para $k$ par. Todos los coeficientes son reales porque la señal es par (etapa [5](symmetrien-im-signal-und-im-spektrum.html#stufe-5)). La figura [1](#abb-1) los muestra para dos ciclos de trabajo: cuanto más estrecho es el pulso, más lentamente decrecen los coeficientes.

:::abbildung et3/k3koeff 1
Coeficientes de Fourier de la onda cuadrada (0/1) para dos anchuras de pulso. En trazo discontinuo, la envolvente $\frac{T_1}{T}\operatorname{si}(\pi kT_1/T)$. Con $T_1=T/2$ faltan los armónicos pares; con $T_1=T/4$, uno de cada cuatro.
:::

:::frage ¿Por qué en una señal periódica no aparecen frecuencias entre los armónicos?
Porque cada oscilación de la suma tiene que tener ella misma el periodo $T$; si no, la suma no sería periódica. Una oscilación con $f=1{,}5F$ solo ha dado vuelta y media al cabo de $T$ y está en una posición distinta de la inicial. Ningún peso, por bien elegido que esté, puede compensarlo, porque las frecuencias distintas son ortogonales y no pueden anularse entre sí.
:::

:::aufgabe Ejercicio 1 ★ Leer los coeficientes
<span class="anker" id="aufg-1"></span>

$s_p(t)=\frac12+\cos\bigl(2\pi Ft+\frac\pi3\bigr)+\frac12\sin(6\pi Ft)$.

<ol class="al">

<li>

Determina todos los $S_p(k)$ con las fórmulas de Euler. Comprueba que $S_p(-k)=S_p^*(k)$.

</li>

<li>

Indica $|S_p(1)|$ y $\varphi_p(1)$ y compáralos con [(2.2)](#gl-2-2).

</li>

</ol>

:::loesung
(a) $\cos(x+\frac\pi3)=\frac12\mathrm{e}^{\mathrm{j}\pi/3}\mathrm{e}^{\mathrm{j} x}+\frac12\mathrm{e}^{-\mathrm{j}\pi/3}\mathrm{e}^{-\mathrm{j} x}$ y $\frac12\sin(3x)=\frac{1}{4\mathrm{j}}\mathrm{e}^{\mathrm{j}3x}-\frac{1}{4\mathrm{j}}\mathrm{e}^{-\mathrm{j}3x}$, con $x=2\pi Ft$:

$$S_p(0)=\tfrac12,\quad S_p(\pm1)=\tfrac12\mathrm{e}^{\pm\mathrm{j}\pi/3}=0{,}25\pm0{,}433\mathrm{j},\quad S_p(3)=-\tfrac{\mathrm{j}}{4},\quad S_p(-3)=\tfrac{\mathrm{j}}{4},$$

todos los demás nulos. $S_p(-1)=S_p^*(1)$ y $S_p(-3)=S_p^*(3)$ se cumplen.

(b) $|S_p(1)|=\frac12$, $\varphi_p(1)=60^\circ$. En [(2.2)](#gl-2-2): $2\cdot\frac12\cos(2\pi Ft+60^\circ)$, exactamente el término coseno de la señal. (Potencia según Parseval: $\frac14+2\cdot\frac14+2\cdot\frac1{16}=0{,}875$.)
:::
:::

:::aufgabe Ejercicio 2 ★★ La onda cuadrada estrecha
<span class="anker" id="aufg-2"></span>

Onda cuadrada con $T_1=T/4$.

<ol class="al">

<li>

Calcula $S_p(0)$, $S_p(1)$, $S_p(2)$ y $S_p(4)$ a partir de [(2.6)](#gl-2-6).

</li>

<li>

¿Por qué $S_p(4)=0$? Interprétalo con la ortogonalidad: ¿cuántos periodos del cuarto armónico caben en el pulso?

</li>

</ol>

:::loesung
(a) $S_p(0)=\frac14$, $S_p(1)=\frac{\sin(\pi/4)}{\pi}=0{,}225$, $S_p(2)=\frac{\sin(\pi/2)}{2\pi}=0{,}159$, $S_p(4)=\frac{\sin\pi}{4\pi}=0$.

(b) El cuarto armónico tiene periodo $T/4$, exactamente la anchura del pulso. La fórmula de análisis integra $\mathrm{e}^{-\mathrm{j}2\pi4Ft}$ sobre el pulso, es decir, sobre exactamente una vuelta completa del fasor. El valor medio es cero. En general, $S_p(k)$ se anula cuando en el pulso cabe un número entero de periodos del $k$-ésimo armónico.
:::
:::

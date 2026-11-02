---
title: Etapa 5: Función de distribución y densidad de probabilidad
pfad: Ingeniería eléctrica / 3.er semestre / Señales y sistemas / Señales aleatorias
order: 3270600
summary: Los valores medios no lo dicen todo.
tags: función de distribución, densidad de probabilidad, cuantizador
lang: es
---

<span class="anker" id="stufe-5"></span>

:::zweck
Los valores medios no lo dicen todo. ¿Con qué frecuencia toma una señal cada valor? Eso lo describe la distribución.
:::

:::definition Definición 5.1 (Distribución)
<span class="anker" id="satz-5-1"></span>

<span class="anker" id="gl-5-1"></span>
$$P_s(x)=\mathrm{Prob}[s(t)\le x],\qquad p_s(x)=\frac{\mathrm{d} P_s(x)}{\mathrm{d} x},\qquad P_s(x)=\int_{-\infty}^xp_s(\xi)\,\mathrm{d}\xi. \tag{5.1}$$
:::

⁠**Cómo leerlo:** la __función de distribución__ $P_s(x)$ es la fracción del conjunto (en los procesos ergódicos, la fracción del tiempo) en la que la señal está por debajo del umbral $x$. Crece de forma monótona desde $P_s(-\infty)=0$ hasta $P_s(\infty)=1$. La __densidad de probabilidad__ $p_s(x)$ nunca es negativa, tiene área 1, y $p_s(x)\,\mathrm{d} x$ es la probabilidad de que la señal esté entre $x$ y $x+\mathrm{d} x$. De ahí se obtienen todos los valores medios de primer orden:

<span class="anker" id="gl-5-2"></span>
$$m_s=\int x\,p_s(x)\,\mathrm{d} x,\qquad L_s=\int x^2p_s(x)\,\mathrm{d} x,\qquad\mathrm E\{F[s]\}=\int F(x)\,p_s(x)\,\mathrm{d} x. \tag{5.2}$$

**Ejemplo: distribución uniforme.** Todos los valores de un intervalo de anchura $a$ en torno a $m_s$ son igual de probables: $p_s(x)=\frac1a\operatorname{rect}\bigl(\frac{x-m_s}{a}\bigr)$. Entonces

$$L_s=\frac1a\int_{m_s-a/2}^{m_s+a/2}x^2\mathrm{d} x=\frac{a^2}{12}+m_s^2,\qquad\sigma_s^2=\frac{a^2}{12}.$$

Los números aleatorios del modelo de referencia ($a=1$, $m_s=0$) tienen la varianza $\frac1{12}=0{,}0833$.

**Características.** Si una señal pasa por una característica $y=k(x)$ (amplificador con saturación, rectificador, cuantizador), su distribución cambia. Con una característica monótona, la probabilidad de cada intervalo se conserva:

<span class="anker" id="gl-5-3"></span>
$$p_g(y)\,|\mathrm{d} y|=p_s(x)\,|\mathrm{d} x|\qquad\Longrightarrow\qquad p_g(y)=\frac{p_s(x)}{|k'(x)|},\qquad P_g\bigl(k(x)\bigr)=P_s(x)\ \ (k\text{ creciente}). \tag{5.3}$$

Donde la característica es empinada, los valores se reparten sobre un rango amplio y la densidad disminuye. Con esta regla, cualquier distribución puede transformarse en otra deseada. Ejemplo: $k(x)=(2|x|-x^2)\operatorname{sgn}x$ convierte una distribución triangular en $[-1,1]$ en una distribución uniforme (ejercicio [4](#aufg-4)).

**Cuantización.** Un __cuantizador__ sustituye cada valor por el más cercano de $M$ niveles. Con niveles uniformes de anchura $\Delta$ y sin saturación, el error está distribuido de forma aproximadamente uniforme entre $-\frac\Delta2$ y $\frac\Delta2$; tiene, por tanto, la varianza $\frac{\Delta^2}{12}$. Para una señal con distribución uniforme sobre los $M$ niveles (varianza $\frac{(M\Delta)^2}{12}$), la relación señal-ruido es $M^2$, en decibelios $20\lg M\approx6\,\text{dB por bit}$: 48 dB con 8 bits, 96 dB con 16 bits.

:::aufgabe Ejercicio 3 ★ Distribución uniforme
<span class="anker" id="aufg-3"></span>

Una señal tiene distribución uniforme entre 1 V y 3 V. Calcula $m_s$, $L_s$, $\sigma_s^2$ y la probabilidad de que esté por encima de 2,5 V.

:::loesung
$a=2$ V, $m_s=2$ V. $\sigma_s^2=\frac{a^2}{12}=\frac13$ V$^2$, $L_s=\frac13+4=4{,}33$ V$^2$. Por encima de 2,5 V queda una cuarta parte del intervalo; por tanto, $\mathrm{Prob}=\frac{0{,}5}{2}=0{,}25$.
:::
:::

:::aufgabe Ejercicio 4 ★★ Transformar distribuciones
<span class="anker" id="aufg-4"></span>

Una señal tiene la densidad triangular $p_s(x)=\Lambda(x)$ en $[-1,1]$.

<ol class="al">

<li>

Determina $P_s(x)$ para $0\le x\le1$.

</li>

<li>

Demuestra con [(5.3)](#gl-5-3) que $k(x)=(2x-x^2)$ para $x\ge0$ (y prolongada de forma impar) genera una distribución uniforme en $[-1,1]$. Pista: para la distribución uniforme, $P_g(y)=\frac12+\frac y2$.

</li>

</ol>

:::loesung
(a) $P_s(x)=\frac12+\int_0^x(1-\xi)\,\mathrm{d}\xi=\frac12+x-\frac{x^2}{2}$ para $0\le x\le1$.

(b) Según [(5.3)](#gl-5-3), tiene que cumplirse $P_g(k(x))=P_s(x)$, es decir, $\frac12+\frac{k(x)}{2}=\frac12+x-\frac{x^2}{2}$. De ahí resulta $k(x)=2x-x^2$. La característica es empinada en $x=0$ (pendiente 2), donde la densidad triangular es máxima, y plana en el borde. Así, los valores frecuentes se separan y los poco frecuentes se juntan. Una simulación da un histograma plano de altura 0,5.
:::
:::

:::aufgabe Ejercicio 4a ★★★ (Para profundizar) El cuantizador óptimo
<span class="anker" id="aufg-4a"></span>

Un cuantizador con los umbrales $u_i$ y los valores de nivel $v_i$ (el nivel $i$ rige para $u_i<x\le u_{i+1}$) tiene el error cuadrático medio $N_q=\sum_i\int_{u_i}^{u_{i+1}}(v_i-x)^2p_s(x)\,\mathrm{d} x$.

<ol class="al">

<li>

Demuestra derivando respecto a $v_i$: en el óptimo, $v_i$ está en el centro de gravedad de la densidad sobre su intervalo.

</li>

<li>

Demuestra derivando respecto a $u_i$: en el óptimo, $u_i$ está justo en el punto medio entre $v_{i-1}$ y $v_i$.

</li>

<li>

¿Por qué, para una señal con distribución uniforme, el cuantizador uniforme es óptimo?

</li>

</ol>

:::loesung
(a) $\frac{\partial N_q}{\partial v_i}=\int_{u_i}^{u_{i+1}}2(v_i-x)p_s(x)\mathrm{d} x=0$; por tanto, $v_i=\dfrac{\int_{u_i}^{u_{i+1}}x\,p_s\,\mathrm{d} x}{\int_{u_i}^{u_{i+1}}p_s\,\mathrm{d} x}$, el centro de gravedad.

(b) $u_i$ aparece como límite superior del intervalo $i-1$ y como límite inferior del intervalo $i$: $\frac{\partial N_q}{\partial u_i}=(v_{i-1}-u_i)^2p_s(u_i)-(v_i-u_i)^2p_s(u_i)=0$; por tanto, $u_i=\frac12(v_{i-1}+v_i)$. Cada valor se asigna al nivel cuyo valor de nivel está más cerca.

(c) Con densidad constante, el centro de gravedad de cada intervalo es su punto medio. Intervalos de igual anchura con sus puntos medios como valores de nivel cumplen ambas condiciones, con la anchura de nivel $\Delta=a/M$.
:::
:::

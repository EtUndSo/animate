---
title: Etapa 2: Un primer sistema, el circuito RC
pfad: Ingeniería eléctrica / 3.er semestre / Señales y sistemas / Sistemas LTI y convolución
order: 3210300
summary: Con el paso bajo RC (fig.
tags: respuesta en frecuencia
lang: es
---

<span class="anker" id="stufe-2"></span>

:::zweck
Con el paso bajo RC (fig. [2](#abb-2)) se puede calcular cómo responde un sistema a dos entradas típicas: una exponencial compleja y un escalón.
:::

**La ecuación diferencial.** La corriente a través de $R$ es $(u_1-u_2)/R$. Fluye íntegramente hacia el condensador y lo carga, $C\,\dot u_2=(u_1-u_2)/R$. Reordenando:

<span class="anker" id="gl-2-1"></span>
$$RC\,\frac{\mathrm{d} u_2}{\mathrm{d} t}+u_2=u_1. \tag{2.1}$$

:::abbildung et3/k1rcschaltung 2
Paso bajo RC: entrada $u_1$, salida $u_2$ en el condensador. En el modelo de referencia, $RC=1$ s.
:::

**Entrada $\mathrm{e}^{\mathrm{j}2\pi Ft}$: la salida es un número por la entrada.** Si se aplica $u_1=\mathrm{e}^{\mathrm{j}2\pi Ft}$, la salida en régimen permanente tiene la misma forma, solo con otra amplitud y otra fase: $u_2=H(F)\,\mathrm{e}^{\mathrm{j}2\pi Ft}$. El número $H(F)$ depende de la frecuencia y por eso se llama __respuesta en frecuencia__. La razón es que derivar no cambia la forma, $\frac{\mathrm{d}}{\mathrm{d} t}\mathrm{e}^{\mathrm{j}2\pi Ft}=\mathrm{j}2\pi F\,\mathrm{e}^{\mathrm{j}2\pi Ft}$. Sustituyendo en [(2.1)](#gl-2-1):

$$H(F)\,\mathrm{e}^{\mathrm{j}2\pi Ft}\,(1+\mathrm{j}2\pi FRC)=\mathrm{e}^{\mathrm{j}2\pi Ft}\quad\Longrightarrow\quad H(F)=\frac{1}{1+\mathrm{j}2\pi FRC}.$$

Lo mismo da el cálculo de corriente alterna con fasores: el condensador tiene la impedancia $1/(\mathrm{j}2\pi FC)$, y el circuito es un divisor de tensión,

$$\underline U_2=\frac{1/(\mathrm{j}2\pi FC)}{R+1/(\mathrm{j}2\pi FC)}\,\underline U_1=\frac{1}{1+\mathrm{j}2\pi FRC}\,\underline U_1.$$

La tensión real correspondiente a un fasor es $u(t)=\operatorname{Re}\{\sqrt2\,|\underline U|\,\mathrm{e}^{\mathrm{j}(2\pi Ft+\varphi)}\}=\sqrt2\,|\underline U|\cos(2\pi Ft+\varphi)$ (fasor de valor eficaz).

:::satz Teorema 2.1 (Función de transferencia del paso bajo RC)
<span class="anker" id="satz-2-1"></span>

Con $x=2\pi FRC$:

<span class="anker" id="gl-2-2"></span>
<span class="anker" id="gl-2-3"></span>
$$\begin{aligned} \operatorname{Re}\{H\}&=\frac{1}{1+x^2},\qquad \operatorname{Im}\{H\}=\frac{-x}{1+x^2},\\ |H(F)|&=\sqrt{\operatorname{Re}\{H\}^2+\operatorname{Im}\{H\}^2}=\sqrt{H\,H^*}=\frac{1}{\sqrt{1+x^2}},\qquad \varphi(F)=-\arctan x. \end{aligned} \tag{2.2|2.3}$$
:::

⁠**Cómo leerlo:** $|H|$ indica en qué factor se reduce la amplitud; $\varphi$, en qué ángulo se retrasa la oscilación. Para $x=1$, es decir, $F=1/(2\pi RC)=0{,}16$ Hz en el modelo de referencia, $|H|=0{,}707$ y $\varphi=-45^\circ$. Para $x=10$, $|H|=0{,}0995$ y $\varphi=-84{,}3^\circ$ (fig. [3](#abb-3)). **Casos límite:** $F\to0$ da $H\to1$ (el condensador tiene tiempo de cargarse por completo); $F\to\infty$ da $H\to0$ con $\varphi\to-90^\circ$ (el condensador actúa como un cortocircuito).

:::abbildung et3/k1bode 3
Módulo y fase de la función de transferencia del paso bajo RC en función de $x=2\pi FRC$ (escala logarítmica). Las oscilaciones lentas pasan casi sin cambios; las rápidas se atenúan y se retrasan hasta $90^\circ$.
:::

**La fase en general.** Para un número complejo cualquiera $H=\operatorname{Re}\{H\}+\mathrm{j}\operatorname{Im}\{H\}$ se cumple

<span class="anker" id="gl-2-4"></span>
$$\varphi=\arctan\frac{\operatorname{Im}\{H\}}{\operatorname{Re}\{H\}}+\lambda\pi+l\cdot2\pi,\qquad \lambda=\begin{cases}0&\operatorname{Re}\{H\}\ge0\\1&\operatorname{Re}\{H\}<0\end{cases},\quad l\ \text{entero}, \tag{2.4}$$

donde $\arctan$ da el valor principal en $[-\pi/2,\pi/2]$.

:::frage ¿Por qué la fórmula de la fase necesita el término $\lambda\pi$?
$\arctan$ solo ve el cociente $\operatorname{Im}/\operatorname{Re}$. Los números $1+\mathrm{j}$ y $-1-\mathrm{j}$ tienen el mismo cociente, 1, pero están en cuadrantes opuestos. $\arctan1=45^\circ$ es correcto para $1+\mathrm{j}$. Para $-1-\mathrm{j}$, el ángulo verdadero es $45^\circ+180^\circ=225^\circ$, equivalente a $-135^\circ$ (con $l=-1$). Siempre que la parte real es negativa hay que sumar $\pi$.
:::

**Entrada escalón: la curva exponencial.** En $t=0$ se aplica $u_1=1$ V, con el condensador descargado. Para $t\ge0$, la ley de mallas con la corriente $i$ da

$$1=R\,i(t)+\frac1C\int_0^ti(\tau)\,\mathrm{d}\tau.$$

Derivando se obtiene $0=R\,\frac{\mathrm{d} i}{\mathrm{d} t}+\frac iC$, es decir, $\frac{\mathrm{d} i}{i}=-\frac{\mathrm{d} t}{RC}$, e integrando,

$$\ln|i|=-\frac{t}{RC}+K\quad\Longrightarrow\quad i(t)=A\,\mathrm{e}^{-t/RC},\qquad A=i(0)=\frac1R,$$

ya que en el primer instante toda la tensión cae en $R$. Con la ley de mallas $u_2=1-R\,i$ se obtiene

<span class="anker" id="gl-2-5"></span>
$$u_2(t)=1-\mathrm{e}^{-t/RC}\qquad(t\ge0). \tag{2.5}$$

El mecanismo: cuanto más cargado está el condensador, menos tensión queda para $R$, menor es la corriente de carga y más despacio sigue cargándose. Esta realimentación hace que la curva sea exponencial.

:::ltspice Paso bajo RC: respuesta al escalón y respuesta en frecuencia
⁠**Esquema:** fuente `voltage` en el nodo `in`, `res` con `1Meg` de `in` a `out`, `cap` con `1u` de `out` a masa; es decir, $RC=1$ s. Cuidado: SPICE lee `1M` como 1 mili; mega se escribe `Meg`.

⁠**Escalón:** fuente `PULSE(0 1 0 1u 1u 100)`, directiva `.tran 5`. Los valores exactos los da una medida como `.meas tran g1 FIND V(out) AT=1`; el resultado aparece en el SPICE Error Log (View, SPICE Error Log). Valores esperados: 0,393 en 0,5 s, 0,632 en 1 s y 0,950 en 3 s, es decir, $1-\mathrm{e}^{-t}$ como en [(2.5)](#gl-2-5).

⁠**Respuesta en frecuencia:** valor de fuente `AC 1` y, en lugar de `.tran`, la directiva `.ac dec 100 0.01 100`. LTspice dibuja el módulo en dB (trazo continuo) y la fase (trazo discontinuo). En 0,159 Hz ($x=1$) se leen $-3{,}0$ dB, es decir, $|H|=0{,}707$, y $-45^\circ$. Compara los valores en $x=10$ con tu resultado del ejercicio [2](#aufg-2)(a).
:::

:::aufgabe Ejercicio 2 ★★ Respuesta en frecuencia y fase
<span class="anker" id="aufg-2"></span>

<ol class="al">

<li>

Calcula $|H|$ y $\varphi$ del paso bajo RC para $x=0$, $1$ y $10$. ¿A qué frecuencia en Hz corresponde $x=10$ en el modelo de referencia?

</li>

<li>

Se aplica una señal $u_1(t)=\cos(2\pi Ft)$ con $x=1$. Escribe $u_2(t)$. ¿Cuántos segundos se retrasa $u_2$ si $RC=1$ s?

</li>

<li>

Determina con [(2.4)](#gl-2-4) las fases de $-1-\mathrm{j}$, $-\mathrm{j}$ y $-2$.

</li>

</ol>

:::loesung
(a) $x=0$: $|H|=1$, $\varphi=0$. $x=1$: $|H|=0{,}707$, $\varphi=-45^\circ$. $x=10$: $|H|=0{,}0995$, $\varphi=-84{,}3^\circ$. $x=10$ significa $F=10/(2\pi RC)=1{,}59$ Hz.

(b) $u_2(t)=0{,}707\cos(2\pi Ft-45^\circ)$ con $2\pi F=1/\mathrm s$, es decir, $F=0{,}159$ Hz. Retraso de $t_0=-\varphi/(2\pi F)=(\pi/4)/(1/\mathrm s)=0{,}785$ s.

(c) $-1-\mathrm{j}$: $\arctan1=45^\circ$, parte real negativa, por tanto $+180^\circ$: $225^\circ$, equivalente a $-135^\circ$. $-\mathrm{j}$: parte real nula, parte imaginaria negativa; $\arctan(\operatorname{Im}/\operatorname{Re})$ tiende a $-90^\circ$, la fase es $-90^\circ$. $-2$: $\arctan0=0$, parte real negativa, por tanto $180^\circ$.
:::
:::

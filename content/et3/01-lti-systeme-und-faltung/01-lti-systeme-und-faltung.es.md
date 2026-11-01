---
title: Señales, sistemas LTI y convolución
pfad: Ingeniería eléctrica / 3.er semestre / Señales y sistemas / Sistemas LTI y convolución
order: 3210100
summary: Por qué la respuesta a un único impulso describe todo el sistema
tags: señal, normalizadas, periodo, frecuencia, sistema, transformación, lineal, invariante en el tiempo
lang: es
---

## De qué trata

Un sistema recibe una señal y entrega otra: un circuito RC suaviza una tensión, la caja de un altavoz colorea un sonido, un amplificador de medida retrasa y amplifica. La pregunta de este artículo es: *¿Qué hay que saber de un sistema para poder calcular la salida para cualquier señal de entrada?*

Para la amplia clase de los sistemas lineales e invariantes en el tiempo (sistemas LTI), la respuesta es sorprendentemente breve: la respuesta a un único impulso infinitamente corto. La herramienta que obtiene de esta única respuesta todas las demás es la convolución.

:::merke La respuesta en tres frases (al final del artículo deberían resultar evidentes)
<ol>

<li>

Toda señal es una superposición de infinitos impulsos cortos: en cada instante $\tau$, un impulso de peso $s(\tau)\,\mathrm{d}\tau$.

</li>

<li>

Un sistema LTI responde a un impulso desplazado con la respuesta al impulso desplazada $h(t-\tau)$ (invariancia en el tiempo), y a una suma de impulsos con la suma de las respuestas (linealidad).

</li>

<li>

Por eso la salida es la convolución $g(t)=\int s(\tau)\,h(t-\tau)\,\mathrm{d}\tau$, y $h(t)$ describe el sistema por completo.

</li>

</ol>
:::

**Un principio detrás de todos los resultados.** La tabla asigna los resultados de este artículo al principio «descomponer, pasar un bloque por el sistema, recomponer».

| Resultado | De dónde viene |
|---|---|
| Integral de convolución | superponer impulsos, superponer respuestas al impulso desplazadas (etapa [4](#stufe-4)) |
| Reflejar al calcular | $h(t-\tau)$ es la respuesta a un impulso que llegó hace $t-\tau$ segundos (etapa [5](#stufe-5)) |
| $\delta$ es el elemento neutro | una señal hecha de impulsos, a través de un sistema que deja cada impulso sin cambios (etapa [6](#stufe-6)) |
| Leyes conmutativa, asociativa y distributiva | intercambiar los papeles, sistemas en cascada, sistemas en paralelo (etapa [6](#stufe-6)) |
| Propiedad de muestreo (de criba), escalado del impulso de Dirac | $\delta$ solo está definido a través de su área (etapa [7](#stufe-7)) |
| Respuesta al escalón = integral de la respuesta al impulso | un escalón es la suma de todos los impulsos hasta $t$ (etapa [8](#stufe-8)) |
| Causalidad, estabilidad | condiciones sobre $h(t)$: nula antes del impulso, área finita de $\vert h\vert $ (etapa [9](#stufe-9)) |
| Convolución sin sistema | la misma superposición, por ejemplo en la suma de los dados al tirar dos dados (etapa [10](#stufe-10)) |

**Cómo trabajar con este artículo.** Cada etapa tiene la idea, preguntas típicas con respuestas desplegables y ejercicios (de ★ a ★★★). Intenta resolverlos primero por tu cuenta; la solución se despliega justo debajo de cada ejercicio.

:::merke El modelo de referencia de este artículo
<ul>

<li>

⁠**Paso bajo RC** con $T=RC=1$ s (por ejemplo $R=1\,\mathrm{M\Omega}$, $C=1\,\mu\text{F}$). Tiempos en s, tensiones en V; es decir, se calcula sin dimensiones.

</li>

<li>

⁠**Pulso rectangular** de altura $a=1$ V y duración $T_0=1$ s, que empieza en $t=0$.

</li>

</ul>

El script `rechnung_kap1.py` recalcula los números y las curvas.
:::

## Etapa 1: Describir señales

<span class="anker" id="stufe-1"></span>

:::zweck
Antes de estudiar sistemas hace falta un lenguaje para las señales: algunas formas básicas y dos operaciones sobre el eje de tiempo, desplazar y escalar.
:::

Una __señal__ es la evolución de una magnitud física en el tiempo, escrita como función $s(t)$. En teoría de sistemas se suele calcular con magnitudes __normalizadas__: tiempos en múltiplos de 1 s, tensiones en múltiplos de 1 V. Así, las ecuaciones entre magnitudes se convierten en ecuaciones entre valores numéricos, y $\mathrm{e}^{-t}$ puede escribirse sin problemas de unidades.

**Señales elementales.** Algunas señales pueden describirse con una expresión sencilla y aparecen una y otra vez (fig. [1](#abb-1)):

$$\begin{gathered} \sin(2\pi t),\qquad \mathrm{e}^{-\pi t^2}\ \text{(gaussiana)},\qquad \varepsilon(t)=\begin{cases}0&t<0\\1&t\ge0\end{cases},\\ \operatorname{rect}(t)=\begin{cases}1&|t|\le\frac12\\0&|t|>\frac12\end{cases},\qquad \Lambda(t)=\begin{cases}1-|t|&|t|\le1\\0&|t|>1\end{cases}. \end{gathered}$$

El escalón $\varepsilon(t)$ y el rectángulo $\operatorname{rect}(t)$ presentan saltos. Qué valor rige exactamente en el punto del salto es cuestión de convenio. A menudo se elige ahí $\tfrac12$: así, rectángulos colocados uno a continuación de otro dan exactamente 1 en todas partes.

:::abbildung et3/k1elementar
Señales elementales. Abajo a la derecha, un rectángulo desplazado y escalado: centro en $t_0=2$, anchura $T=2$, altura $a=0{,}8$.
:::

**Desplazar y escalar.** De una señal se obtienen otras nuevas transformando el eje de tiempo:

<ul>

<li>

⁠**Desplazar:** $t\to t-t_0$. Para $t_0>0$, la señal se *retrasa* $t_0$, es decir, se desplaza hacia la derecha.

</li>

<li>

⁠**Escalar:** $t\to t/T$. Para $|T|>1$ la señal se ensancha, para $0<|T|<1$ se estrecha, y para $T<0$ además se refleja.

</li>

</ul>

Ambas operaciones juntas, más una amplitud $a$, dan por ejemplo el pulso rectangular

<span class="anker" id="gl-1-1"></span>
$$s(t)=a\operatorname{rect}\Bigl(\frac{t-t_0}{T}\Bigr)=\begin{cases}a & |t-t_0|\le |T|/2\\ 0 & \text{en otro caso}\end{cases} \tag{1.1}$$

con centro $t_0$, duración $|T|$ y altura $a$. Se comprueba sustituyendo el argumento $(t-t_0)/T$ en la definición de $\operatorname{rect}$. Del mismo modo, $\sin(2\pi t/T)=\sin(2\pi Ft)$ es el seno escalado con __periodo__ $T$ y __frecuencia__ $F=1/T$.

:::frage ¿Por qué $t-t_0$ desplaza la señal hacia la derecha, si se está restando algo?
La nueva señal muestra en el instante $t$ el valor que la antigua tenía en el instante $t-t_0$, es decir, *antes*. Todo lo que hacía la señal antigua, la nueva lo hace $t_0$ más tarde. Lo más sencillo es comprobarlo en un punto característico: el flanco de $\varepsilon(t-t_0)$ está donde el argumento se anula, en $t=t_0$.
:::

**La exponencial compleja.** Lo más importante para la teoría de sistemas es

$$\mathrm{e}^{\mathrm{j}2\pi Ft}=\cos(2\pi Ft)+\mathrm{j}\sin(2\pi Ft).$$

De un par complejo conjugado se obtienen, según Euler, las oscilaciones reales:

$$\cos(2\pi Ft)=\frac{\mathrm{e}^{\mathrm{j}2\pi Ft}+\mathrm{e}^{-\mathrm{j}2\pi Ft}}{2},\qquad \sin(2\pi Ft)=\frac{\mathrm{e}^{\mathrm{j}2\pi Ft}-\mathrm{e}^{-\mathrm{j}2\pi Ft}}{2\mathrm{j}}.$$

En una oscilación, un retardo $t_0$ aparece como un desfase:

<span class="anker" id="gl-1-2"></span>
$$\cos\bigl(2\pi F(t-t_0)\bigr)=\cos(2\pi Ft+\varphi)=\operatorname{Re}\bigl\{\mathrm{e}^{\mathrm{j}2\pi Ft}\,\mathrm{e}^{\mathrm{j}\varphi}\bigr\},\qquad\varphi=-2\pi Ft_0. \tag{1.2}$$

⁠**En resumen:** en una oscilación, retrasar es lo mismo que girar la fase, y en $\mathrm{e}^{\mathrm{j}2\pi Ft}$ es incluso lo mismo que multiplicar por el número $\mathrm{e}^{\mathrm{j}\varphi}$. En la [parte 2](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html), esta propiedad sostiene toda la transformada de Laplace.

:::aufgabe Ejercicio 1 ★ Desplazar, escalar, fase
<span class="anker" id="aufg-1"></span>

<ol class="al">

<li>

¿Dónde empieza y dónde termina $s(t)=2\operatorname{rect}\bigl(\frac{t-3}{4}\bigr)$, y qué altura tiene el pulso?

</li>

<li>

Escribe un pulso rectangular que tenga la altura 0,5 V desde $t=1$ s hasta $t=4$ s.

</li>

<li>

Esboza $s(-t)$ para $s(t)=\varepsilon(t-1)$. ¿Dónde está el flanco?

</li>

<li>

Un coseno con $F=50$ Hz se retrasa $t_0=5$ ms. ¿Qué fase $\varphi$ tiene después?

</li>

</ol>

:::loesung
(a) Centro $t_0=3$, duración $T=4$: de $t=1$ a $t=5$, altura 2.

(b) Centro 2,5 s, duración 3 s: $s(t)=0{,}5\operatorname{rect}\bigl(\frac{t-2{,}5}{3}\bigr)$.

(c) $s(-t)=\varepsilon(-t-1)$. El flanco está donde el argumento se anula: $-t-1=0$, es decir, $t=-1$. El valor es 1 donde el argumento es $\ge0$, es decir, para $t\le-1$. Un escalón reflejado: 1 a la izquierda de $-1$, 0 a la derecha.

(d) $\varphi=-2\pi Ft_0=-2\pi\cdot50\,\mathrm{Hz}\cdot5\,\mathrm{ms}=-\pi/2=-90^\circ$. Un retardo de un cuarto de periodo es un cuarto de vuelta.
:::
:::

## Etapa 2: Un primer sistema, el circuito RC

<span class="anker" id="stufe-2"></span>

:::zweck
En el paso bajo RC (fig. [2](#abb-2)) ya se ven a pequeña escala todas las ideas de este artículo: una exponencial compleja sale solo multiplicada por un número, y a un escalón el circuito responde con una curva exponencial.
:::

**La ecuación diferencial.** La corriente a través de $R$ es $(u_1-u_2)/R$. Fluye íntegramente hacia el condensador y lo carga, $C\,\dot u_2=(u_1-u_2)/R$. Reordenando:

<span class="anker" id="gl-2-1"></span>
$$RC\,\frac{\mathrm{d} u_2}{\mathrm{d} t}+u_2=u_1. \tag{2.1}$$

:::abbildung et3/k1rcschaltung
Paso bajo RC: entrada $u_1$, salida $u_2$ en el condensador. En el modelo de referencia, $RC=1$ s.
:::

**Entrada $\mathrm{e}^{\mathrm{j}2\pi Ft}$: la salida es un número por la entrada.** Si se aplica $u_1=\mathrm{e}^{\mathrm{j}2\pi Ft}$, la salida en régimen permanente tiene la misma forma, solo con otra amplitud y otra fase: $u_2=H(F)\,\mathrm{e}^{\mathrm{j}2\pi Ft}$. La razón es que derivar no cambia la forma, $\frac{\mathrm{d}}{\mathrm{d} t}\mathrm{e}^{\mathrm{j}2\pi Ft}=\mathrm{j}2\pi F\,\mathrm{e}^{\mathrm{j}2\pi Ft}$. Sustituyendo en [(2.1)](#gl-2-1):

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

:::abbildung et3/k1bode
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

## Etapa 3: Qué es un sistema LTI

<span class="anker" id="stufe-3"></span>

:::zweck
El circuito RC tiene dos propiedades en las que se basa todo lo demás: es lineal e invariante en el tiempo. Esta etapa define ambas y muestra lo que permiten.
:::

Un __sistema__ asigna a una señal de entrada una señal de salida:

$$g(t)=\operatorname{Tr}\{s(t)\}.$$

Una asignación así, de funciones a funciones, se llama __transformación__. No asigna un valor numérico a otro: la salida en el instante $t$ puede depender de toda la evolución anterior de la entrada. En el circuito RC, $u_2(t)$ depende de cuánta carga se ha acumulado hasta $t$.

:::definition Definición 3.1 (Sistema LTI)
<span class="anker" id="satz-3-1"></span>

Un sistema se llama

<ul>

<li>

__lineal__ si para constantes arbitrarias $a_i$ se cumple el principio de superposición:

<span class="anker" id="gl-3-1"></span>
$$\operatorname{Tr}\Bigl\{\sum_ia_is_i(t)\Bigr\}=\sum_ia_i\operatorname{Tr}\{s_i(t)\}=\sum_ia_ig_i(t); \tag{3.1}$$

</li>

<li>

__invariante en el tiempo__ si para todo desplazamiento $t_0$ se cumple:

<span class="anker" id="gl-3-2"></span>
$$\operatorname{Tr}\{s(t-t_0)\}=g(t-t_0). \tag{3.2}$$

</li>

</ul>

Un sistema lineal e invariante en el tiempo se llama, abreviadamente, __sistema LTI__ (del inglés linear time-invariant).
:::

En el circuito RC, la linealidad se debe a que en la ecuación diferencial [(2.1)](#gl-2-1) no aparecen productos ni cuadrados de $u_1$ y $u_2$. La invariancia en el tiempo se debe a que $R$ y $C$ no cambian con el tiempo. Todas las redes de $R$, $L$ y $C$ se describen mediante ecuaciones diferenciales lineales con coeficientes constantes. Sin embargo, esto no vale para todo sistema LTI: el elemento de retardo ideal de la etapa [7](#stufe-7), por ejemplo, no tiene tal ecuación.

**Lo que permiten las dos propiedades.** Si se conoce la respuesta $g_0$ a un pulso rectangular $s_0$, se conoce sin más cálculo la respuesta a cualquier suma de pulsos rectangulares desplazados y escalados. La figura [4](#abb-4) lo muestra para $s(t)=s_0(t)+0{,}5\,s_0(t-2)$: la salida es $g_0(t)+0{,}5\,g_0(t-2)$.

:::abbildung et3/k1doppel
Izquierda: rectángulo $s_0$ (altura 1 V, duración 1 s) y la respuesta $g_0$ del circuito RC. Derecha: un par de pulsos. La respuesta (rojo) es la suma de $g_0(t)$ y la copia desplazada y reducida a la mitad $0{,}5\,g_0(t-2)$ (discontinua).
:::

:::frage ¿Es lineal $g(t)=2s(t)+1$? Al fin y al cabo, la característica es una recta.
No. En un sistema lineal, la entrada cero tiene que dar la salida cero: si en [(3.1)](#gl-3-1) se toman todos los $a_i=0$, resulta $\operatorname{Tr}\{0\}=0$. Aquí $\operatorname{Tr}\{0\}=1$. También falla el principio de superposición: dos entradas aplicadas por separado dan en suma $2s_1+2s_2+2$, pero aplicadas juntas dan $2s_1+2s_2+1$. Una recta que no pasa por el origen se llama *afín*, no lineal.
:::

:::ltspice Comprobar la superposición: dos rectángulos
⁠**Esquema:** el circuito RC de la etapa [2](#stufe-2), pero con dos fuentes `voltage` en serie: `V1`, con el polo negativo a masa y el positivo en el nodo `a`, valor `PULSE(0 {a1} 0 1u 1u 1)`; encima, `V2` de `a` a `in`, valor `PULSE(0 {a2} 2 1u 1u 1)`. En serie, las tensiones se suman; al circuito RC le llega, por tanto, $a_1s_0(t)+a_2s_0(t-2)$.

⁠**Directivas:** `.param a1=1 a2=0.5`, `.step param a1 list 0 1`, `.step param a2 list 0 0.5`, `.tran 0 6 0 1m`. LTspice calcula las cuatro combinaciones y las dibuja superpuestas.

⁠**Lo que ves:** las curvas $0$, $g_0(t)$, $0{,}5\,g_0(t-2)$ y su suma, como en la fig. [4](#abb-4). En $t=2{,}5$ s, $0{,}141+0{,}197=0{,}338$. La suma de las entradas da la suma de las respuestas (linealidad), y la fuente desplazada 2 s da la curva desplazada 2 s (invariancia en el tiempo).
:::

:::aufgabe Ejercicio 3 ★ ¿LTI o no?
<span class="anker" id="aufg-3"></span>

Comprueba para cada sistema la linealidad y la invariancia en el tiempo: (a) $g(t)=3\,s(t-2)$, (b) $g(t)=s(t)^2$, (c) $g(t)=s(t)+1$, (d) $g(t)=t\,s(t)$, (e) $g(t)=s(2t)$, (f) $g(t)=\int_{-\infty}^ts(\tau)\,\mathrm{d}\tau$.

:::loesung
(a) Lineal e invariante en el tiempo (ganancia 3, retardo 2): LTI. (b) No lineal: $\operatorname{Tr}\{2s\}=4s^2\neq2s^2$. Invariante en el tiempo. (c) No lineal (afín, $\operatorname{Tr}\{0\}=1$). Invariante en el tiempo. (d) Lineal. No invariante en el tiempo: $\operatorname{Tr}\{s(t-t_0)\}=t\,s(t-t_0)$, pero $g(t-t_0)=(t-t_0)\,s(t-t_0)$. El factor $t$ es un componente que cambia con el tiempo. (e) Lineal. No invariante en el tiempo: $\operatorname{Tr}\{s(t-t_0)\}=s(2t-t_0)$, pero $g(t-t_0)=s(2t-2t_0)$. Comprimir el tiempo comprime también cualquier desplazamiento. (f) LTI. Lineal, porque la integral es lineal. Invariante en el tiempo: $\int_{-\infty}^ts(\tau-t_0)\mathrm{d}\tau=\int_{-\infty}^{t-t_0}s(\vartheta)\mathrm{d}\vartheta=g(t-t_0)$. Su respuesta al impulso es $\varepsilon(t)$ (etapa [8](#stufe-8)).
:::
:::

## Etapa 4: La integral de convolución

<span class="anker" id="stufe-4"></span>

:::zweck
Con la linealidad y la invariancia en el tiempo, la respuesta a *cualquier* señal puede calcularse a partir de la respuesta a un único pulso corto. El resultado es la integral de convolución.
:::

**La idea en cuatro pasos.**

<ol>

<li>

⁠**Descomponer.** Se aproxima la señal de entrada por una escalera de rectángulos estrechos de anchura $T_0$. Como bloque elemental sirve un rectángulo $s_0(t)$ de duración $T_0$ y altura $1/T_0$, es decir, de área 1. El peldaño en $nT_0$ es este bloque, desplazado $nT_0$ y ponderado con $s(nT_0)\,T_0$, el área de la franja:

$$s(t)\approx s_a(t)=\sum_{n=-\infty}^{\infty}s(nT_0)\,s_0(t-nT_0)\,T_0.$$

</li>

<li>

⁠**Un bloque a través del sistema.** A $s_0$ el sistema responde con $g_0(t)$. Esto hay que conocerlo una vez.

</li>

<li>

⁠**Recomponer.** Invariancia en el tiempo: el bloque desplazado produce la respuesta desplazada. Linealidad: los pesos y la suma pasan a través del sistema. Por tanto,

$$g_a(t)=\sum_{n=-\infty}^{\infty}s(nT_0)\,g_0(t-nT_0)\,T_0\approx g(t).$$

</li>

<li>

⁠**Paso al límite $T_0\to0$.** La escalera se convierte en la señal. El rectángulo de área 1 se convierte en el __impulso de Dirac__ (delta de Dirac) $\delta(t)$, un impulso infinitamente corto de área 1 (etapa [7](#stufe-7)). Su respuesta se llama __respuesta al impulso__ $h(t)$. De $nT_0$ resulta la variable continua $\tau$; de $T_0$, el diferencial $\mathrm{d}\tau$; de las sumas, integrales.

</li>

</ol>

:::abbildung et3/k1treppe
Arriba: un pulso triangular $s(t)=\Lambda(t-1)$ y su aproximación escalonada con $T_0=0{,}5$ s. Abajo: la respuesta exacta del circuito RC y la suma de las respuestas a los rectángulos desplazados. La desviación máxima baja de 0,17 ($T_0=0{,}5$ s) a 0,08 ($0{,}25$ s) y a 0,03 ($0{,}1$ s).
:::

:::satz Teorema 4.1 (Integral de convolución)
<span class="anker" id="satz-4-1"></span>

Para toda señal $s(t)$ se cumple

<span class="anker" id="gl-4-1"></span>
$$s(t)=\int_{-\infty}^{\infty}s(\tau)\,\delta(t-\tau)\,\mathrm{d}\tau, \tag{4.1}$$

y un sistema LTI con respuesta al impulso $h(t)$ responde a ella con

<span class="anker" id="gl-4-2"></span>
$$g(t)=\int_{-\infty}^{\infty}s(\tau)\,h(t-\tau)\,\mathrm{d}\tau. \tag{4.2}$$
:::

⁠**Cómo leerlo:** $\tau$ es el instante de un impulso de entrada, y $s(\tau)\,\mathrm{d}\tau$, su peso (el área de la franja). $h(t-\tau)$ es la respuesta del sistema en el instante $t$ a un impulso que llegó en el instante $\tau$, es decir, hace $t-\tau$ segundos. La salida reúne todos los impulsos del pasado, cada uno ponderado según cuánto lo «recuerda» todavía el sistema al cabo de ese tiempo. La ecuación es exacta y vale para todo sistema LTI.

⁠**En resumen:** la salida de un sistema LTI es la superposición de sus respuestas al impulso, desplazadas a cada instante de la entrada y ponderadas con el valor de la entrada en ese instante.

:::frage ¿Por qué los bloques rectangulares tienen que tener área 1?
Para que la respuesta al bloque conserve una forma fija en el paso al límite. Un rectángulo de altura fija 1 tendría área cero para $T_0\to0$, y su respuesta desaparecería. Con la altura $1/T_0$, el área sigue siendo 1, y la respuesta tiende a $h(t)$. En el circuito RC, el pico de la respuesta es $(1-\mathrm{e}^{-T_0})/T_0$: 0,632 para $T_0=1$ s, 0,787 para 0,5 s, 0,952 para 0,1 s, y para $T_0\to0$ pasa a ser $1=h(0^+)$. El área de la respuesta sigue siendo siempre 1.
:::

:::frage ¿Existe en la realidad el impulso $\delta(t)$? ¿Cómo se mide entonces $h(t)$?
Un impulso infinitamente corto no existe. Pero basta cualquier pulso mucho más corto que las constantes de tiempo del sistema. Entonces el sistema solo ve su área, y la respuesta es prácticamente $(\text{área})\cdot h(t)$. En el circuito RC con $RC=1$ s, el pico de la respuesta a un pulso de 1 ms se desvía solo un 0,05 % de $h(0^+)$. Así se miden también las respuestas al impulso: se da una palmada en una sala y se graba la reverberación.
:::

:::ltspice Aproximar la respuesta al impulso con un rectángulo corto
⁠**Esquema:** el circuito RC de la etapa [2](#stufe-2) con la fuente `PULSE(0 {1/T0} 0 1n 1n {T0})`: un rectángulo de anchura $T_0$ y altura $1/T_0$, es decir, de área 1.

⁠**Directivas:** `.param T0=1`, `.step param T0 list 1 0.5 0.1 1m`, `.tran 0 10 0 1m`, `.meas tran spitze MAX V(out)`, `.meas tran flaeche INTEG V(out)`.

⁠**Lo que ves:** los picos valen 0,632; 0,787; 0,952 y 0,9995, como $(1-\mathrm{e}^{-T_0})/T_0$. Con el pulso de 1 ms, la respuesta ya es prácticamente $h(t)=\mathrm{e}^{-t}$. El área vale 1,000 en las cuatro simulaciones: un pulso mucho más corto que $RC$ solo actúa a través de su área.
:::

:::aufgabe Ejercicio 4 ★★ La escalera, más de cerca
<span class="anker" id="aufg-4"></span>

<ol class="al">

<li>

Calcula la respuesta $g_0(t)$ del circuito RC ($RC=1$ s) al rectángulo de altura $1/T_0$ de $0$ a $T_0$. Usa para ello [(2.5)](#gl-2-5) y escribe el rectángulo como diferencia de dos escalones.

</li>

<li>

Demuestra que $g_0(T_0)=(1-\mathrm{e}^{-T_0})/T_0$ y que tiende a 1 para $T_0\to0$.

</li>

<li>

¿Por qué la aproximación $g_a$ de la fig. [5](#abb-5) va retrasada? (Pista: ¿dónde está el peldaño respecto al triángulo en el flanco ascendente y en el descendente?)

</li>

</ol>

:::loesung
(a) El rectángulo es $\frac{1}{T_0}[\varepsilon(t)-\varepsilon(t-T_0)]$. Linealidad e invariancia en el tiempo con la respuesta al escalón [(2.5)](#gl-2-5):

$$g_0(t)=\frac{1}{T_0}\Bigl[\bigl(1-\mathrm{e}^{-t}\bigr)\varepsilon(t)-\bigl(1-\mathrm{e}^{-(t-T_0)}\bigr)\varepsilon(t-T_0)\Bigr].$$

(b) En $t=T_0$ el segundo sumando es nulo: $g_0(T_0)=(1-\mathrm{e}^{-T_0})/T_0$. Con $\mathrm{e}^{-T_0}\approx1-T_0+T_0^2/2$ para $T_0$ pequeño, esto es $\approx1-T_0/2\to1=h(0^+)$. Valores numéricos: 0,632; 0,787; 0,952 para $T_0=1$; 0,5; 0,1 s.

(c) Cada peldaño mantiene el valor $s(nT_0)$ desde el *comienzo* del intervalo hasta su final. Por eso, en el flanco ascendente la escalera queda por debajo del triángulo, y en el descendente, por encima: en promedio está retrasada $T_0/2$. La salida hereda este retraso; en el lado descendente, $g_a$ queda por encima de $g$ ($g_a(2)=0{,}508$ en lugar de $0{,}400$ para $T_0=0{,}5$ s). Con un $T_0$ menor se reduce el retraso y, con él, el error.
:::
:::

## Etapa 5: Calcular la convolución

<span class="anker" id="stufe-5"></span>

:::zweck
La integral [(4.2)](#gl-4-2) hay que evaluarla para señales concretas. La clave es dibujar ambos factores en función de la variable de integración $\tau$.
:::

**La receta.** Para un instante fijo $t$:

<ol>

<li>

Dibujar $s(\tau)$ en función de $\tau$.

</li>

<li>

Dibujar $h(-\tau)$: *reflejar* $h$ respecto al eje vertical.

</li>

<li>

$h(t-\tau)$: *desplazar* la $h$ reflejada una distancia $t$ hacia la derecha.

</li>

<li>

⁠*Multiplicar* ambas e *integrar* respecto a $\tau$: eso es $g(t)$.

</li>

</ol>

Si se deja crecer $t$, la $h$ reflejada se desliza de izquierda a derecha sobre $s$. Donde las dos no se solapan, $g(t)=0$.

¿Por qué reflejada? Como función de $\tau$, el argumento $t-\tau$ disminuye cuando $\tau$ crece. El comienzo de $h$ (edad cero) está en $\tau=t$; los impulsos más antiguos quedan más a la izquierda. En el circuito RC, $h$ es máxima al principio: el sistema «recuerda» con más fuerza el pasado más reciente.

**Ejemplo: circuito RC y pulso rectangular.** La respuesta al impulso del circuito RC con la constante de tiempo $T=RC$ es un pulso exponencial decreciente de área 1 (la etapa [8](#stufe-8) lo deduce):

<span class="anker" id="gl-5-1"></span>
$$h(t)=\frac1T\,\varepsilon(t)\,\mathrm{e}^{-t/T}. \tag{5.1}$$

Entrada: rectángulo de altura $a$ de $0$ a $T_0$. La figura [6](#abb-6) muestra la posición de los dos factores para dos instantes. Hay tres tramos:

<span class="anker" id="gl-5-2"></span>
$$g(t)=\begin{cases}0 & t<0,\\[2pt] a\bigl(1-\mathrm{e}^{-t/T}\bigr) & 0\le t\le T_0,\\[2pt] a\bigl(\mathrm{e}^{T_0/T}-1\bigr)\mathrm{e}^{-t/T} & t>T_0.\end{cases} \tag{5.2}$$

:::herleitung Respuesta al pulso rectangular
⁠**$t<0$:** La $h(t-\tau)$ desplazada solo es distinta de cero para $\tau\le t<0$; $s(\tau)$, solo para $\tau\ge0$. No hay solapamiento, $g=0$.

⁠**$0\le t\le T_0$:** Solapamiento para $0<\tau<t$:

$$g(t)=\int_0^ta\,\frac1T\,\mathrm{e}^{-(t-\tau)/T}\,\mathrm{d}\tau=\frac aT\,\mathrm{e}^{-t/T}\int_0^t\mathrm{e}^{\tau/T}\mathrm{d}\tau=\frac aT\,\mathrm{e}^{-t/T}\cdot T\bigl(\mathrm{e}^{t/T}-1\bigr)=a\bigl(1-\mathrm{e}^{-t/T}\bigr).$$

⁠**$t>T_0$:** Solapamiento ya solo para $0<\tau<T_0$:

$$g(t)=\frac aT\,\mathrm{e}^{-t/T}\int_0^{T_0}\mathrm{e}^{\tau/T}\mathrm{d}\tau=a\bigl(\mathrm{e}^{T_0/T}-1\bigr)\mathrm{e}^{-t/T}.$$
:::

En el modelo de referencia ($a=1$, $T_0=T=1$ s): $g(0{,}5)=0{,}3935$, $g(1)=0{,}6321$, $g(2)=0{,}2325$, $g(3)=0{,}0855$. Es la misma curva que $g_0$ en la fig. [4](#abb-4).

:::abbildung et3/k1schieben
Convolución gráfica, $a=1$, $T_0=T=1$ s. Azul: $s(\tau)$. Rojo: $h(t-\tau)$, reflejada y desplazada una distancia $t$. El área naranja es $g(t)$: 0,3935 en $t=0{,}5$ s (solapamiento parcial), 0,2325 en $t=2$ s (todo el rectángulo cae en la parte ya amortiguada de $h$). A la derecha, la respuesta completa con ambos puntos.
:::

:::frage ¿Por qué se refleja $h$ y no $s$?
También se puede reflejar $s$, porque la convolución es conmutativa (etapa [6](#stufe-6)). Se refleja la función con la que el desplazamiento resulta más claro, normalmente la de forma más sencilla.
:::

:::ltspice Respuesta al pulso rectangular
⁠**Esquema:** el circuito RC de la etapa [2](#stufe-2) con la fuente `PULSE(0 1 0 1u 1u 1)`: altura 1 V, duración 1 s.

⁠**Directivas:** `.tran 0 20 0 1m`; para cada instante, una medida como `.meas tran g2 FIND V(out) AT=2`, y además `.meas tran gmax MAX V(out)` y `.meas tran flaeche INTEG V(out)`.

⁠**Lo que ves:** $g(0{,}5)=0{,}3935$, $g(1)=0{,}6321$, $g(2)=0{,}2325$ y $g(3)=0{,}0855$, exactamente como predice [(5.2)](#gl-5-2). Compara `gmax` y `flaeche` con tu resultado del ejercicio [6](#aufg-6).
:::

:::aufgabe Ejercicio 5 ★★ Rectángulo con rectángulo
<span class="anker" id="aufg-5"></span>

Calcula $\operatorname{rect}(t)*\operatorname{rect}(t)$ con la receta. Distingue $|t|>1$, $-1\le t\le0$ y $0\le t\le1$. ¿Qué señal elemental resulta?

:::loesung
El rectángulo reflejado vuelve a ser $\operatorname{rect}$ (es simétrico); desplazado, ocupa $[t-\frac12,t+\frac12]$. La integral es la longitud del solapamiento con $[-\frac12,\frac12]$:

<ul>

<li>

$|t|>1$: sin solapamiento, 0.

</li>

<li>

$-1\le t\le0$: solapamiento de $-\frac12$ a $t+\frac12$, longitud $1+t$.

</li>

<li>

$0\le t\le1$: solapamiento de $t-\frac12$ a $\frac12$, longitud $1-t$.

</li>

</ul>

En conjunto, $1-|t|$ para $|t|\le1$: $\operatorname{rect}*\operatorname{rect}=\Lambda$. Numéricamente: 1,000; 0,500; 0,200 en $t=0$; 0,5; 0,8.
:::
:::

:::aufgabe Ejercicio 6 ★★ Comprobar la respuesta al rectángulo
<span class="anker" id="aufg-6"></span>

<ol class="al">

<li>

Demuestra que [(5.2)](#gl-5-2) es continua en $t=T_0$. ¿Por qué tiene que ser continua?

</li>

<li>

¿Dónde tiene $g(t)$ su máximo y cuánto vale en el modelo de referencia?

</li>

<li>

Demuestra que el área bajo $g(t)$ es igual a $aT_0$, y justifícalo sin calcular, a partir de $\int h\,\mathrm{d} t=1$.

</li>

</ol>

:::loesung
(a) En $t=T_0$: $a(1-\mathrm{e}^{-T_0/T})$ y $a(\mathrm{e}^{T_0/T}-1)\mathrm{e}^{-T_0/T}=a(1-\mathrm{e}^{-T_0/T})$, iguales. Físicamente: la tensión del condensador no puede saltar; para ello haría falta una corriente infinita. Matemáticamente: la convolución de una señal acotada con una $h$ integrable es continua.

(b) Durante el pulso, $g$ crece; después, decrece. El máximo está en $t=T_0$: $g(1\,\mathrm{s})=1-\mathrm{e}^{-1}=0{,}632$.

(c) Cálculo:

$$\int g\,\mathrm{d} t=a\Bigl[T_0-T\bigl(1-\mathrm{e}^{-T_0/T}\bigr)\Bigr]+a\bigl(\mathrm{e}^{T_0/T}-1\bigr)T\mathrm{e}^{-T_0/T}=aT_0.$$

Sin cálculo: el área de una convolución es el producto de las áreas, $\int g\,\mathrm{d} t=\int\!\!\int s(\tau)h(t-\tau)\,\mathrm{d}\tau\,\mathrm{d} t=\int s\,\mathrm{d}\tau\cdot\int h\,\mathrm{d} t=aT_0\cdot1$. Numéricamente: 1,000.
:::
:::

## Etapa 6: Reglas de cálculo de la convolución

<span class="anker" id="stufe-6"></span>

:::zweck
La convolución se comporta en muchos aspectos como una multiplicación. Cada regla de cálculo tiene un significado para los sistemas.
:::

La integral de convolución se escribe abreviadamente como __producto de convolución__ $g(t)=s(t)*h(t)$. La ecuación [(4.1)](#gl-4-1) queda entonces $s(t)=s(t)*\delta(t)$.

<ol class="al">

<li>

⁠**Elemento neutro.** $s*\delta=s$: el impulso de Dirac desempeña el papel del uno. Un sistema con $h(t)=\delta(t)$ transmite cualquier señal sin cambios; se dice que es __idealmente libre de distorsión__.

</li>

<li>

⁠**Ley conmutativa.** $s*h=h*s$. Significado: la entrada y la respuesta al impulso pueden intercambiar sus papeles. El sistema con la respuesta al impulso $s$ responde a la entrada $h$ igual que el sistema $h$ a la entrada $s$.

</li>

<li>

⁠**Ley asociativa.** $(f*s)*h=f*(s*h)$. Significado: dos sistemas en cascada actúan como un único sistema cuya respuesta al impulso es la convolución de las dos respuestas al impulso.

</li>

<li>

⁠**Ley distributiva.** $f*(s+h)=f*s+f*h$. Significado: dos sistemas conectados en paralelo cuyas salidas se suman actúan como un sistema con la suma de las respuestas al impulso.

</li>

<li>

⁠**Señales complejas.** Como la convolución es lineal, se descompone en partes reales e imaginarias:

<span class="anker" id="gl-6-1"></span>
$$s*h=\bigl[\operatorname{Re} s*\operatorname{Re} h-\operatorname{Im} s*\operatorname{Im} h\bigr]+\mathrm{j}\bigl[\operatorname{Re} s*\operatorname{Im} h+\operatorname{Im} s*\operatorname{Re} h\bigr]. \tag{6.1}$$

</li>

</ol>

:::herleitung Ley conmutativa
Sustitución $\tau'=t-\tau$, es decir, $\tau=t-\tau'$ y $\mathrm{d}\tau=-\mathrm{d}\tau'$. Los límites $\tau=\mp\infty$ pasan a ser $\tau'=\pm\infty$; al intercambiarlos se anula el signo menos:

$$s*h=\int_{-\infty}^{\infty}s(\tau)\,h(t-\tau)\,\mathrm{d}\tau=\int_{-\infty}^{\infty}s(t-\tau')\,h(\tau')\,\mathrm{d}\tau'=h*s.$$
:::

:::abbildung et3/k1bloecke
Arriba: conexión en cascada, respuesta al impulso $h_1*h_2$ (ley asociativa). Abajo: conexión en paralelo con suma, respuesta al impulso $h_1+h_2$ (ley distributiva).
:::

:::aufgabe Ejercicio 7 ★★ Dos circuitos RC en cascada
<span class="anker" id="aufg-7"></span>

Se conectan uno tras otro dos circuitos RC con $RC=1$ s. El segundo no carga al primero (por ejemplo, gracias a un seguidor de tensión entre ambos).

<ol class="al">

<li>

Calcula la respuesta al impulso de la cascada, $h*h$ con $h(t)=\mathrm{e}^{-t}\varepsilon(t)$.

</li>

<li>

¿Cuándo es máxima y cuánto vale su área?

</li>

<li>

¿Por qué hace falta la condición «no carga»?

</li>

</ol>

:::loesung
(a) Para $t\ge0$:

$$(h*h)(t)=\int_0^t\mathrm{e}^{-\tau}\mathrm{e}^{-(t-\tau)}\mathrm{d}\tau=\mathrm{e}^{-t}\int_0^t\mathrm{d}\tau=t\,\mathrm{e}^{-t}.$$

Por tanto, $h_{\text{cascada}}(t)=t\,\mathrm{e}^{-t}\varepsilon(t)$.

(b) Derivada $(1-t)\mathrm{e}^{-t}=0$ en $t=1$ s, máximo $\mathrm{e}^{-1}=0{,}368$. Área $\int_0^\infty t\mathrm{e}^{-t}\mathrm{d} t=1=1\cdot1$ (producto de las áreas).

(c) Sin desacoplo, el segundo circuito RC extrae corriente del primer condensador. Entonces la tensión en el primer condensador ya no es la de un circuito RC sin carga, y la cascada no tiene $h*h$ como respuesta al impulso. Sigue siendo un sistema LTI, pero con otra respuesta al impulso. La convolución de las respuestas individuales presupone que ningún sistema influye de vuelta sobre su entrada.
:::
:::

## Etapa 7: El impulso de Dirac

<span class="anker" id="stufe-7"></span>

:::zweck
El impulso de Dirac es el objeto límite de la etapa [4](#stufe-4). No es una función ordinaria. Todas sus propiedades se deducen de que solo actúa a través de su área.
:::

**Qué es $\delta$ y qué no es.** Los rectángulos $\frac{1}{T_0}\operatorname{rect}(t/T_0)$ se hacen cada vez más estrechos y altos para $T_0\to0$, y su área sigue siendo 1 (fig. [8](#abb-8)). No existe un límite en el sentido de las funciones ordinarias: una función que es nula en todas partes salvo en un punto tiene área cero, sea cual sea su valor en ese punto. Por eso $\delta(t)$ es una __distribución__: un objeto que solo queda determinado por su efecto bajo una integral, concretamente por [(4.1)](#gl-4-1). Se dibuja como una flecha cuya altura indica el peso (el área).

:::abbildung et3/k1dirac
Izquierda: rectángulos de área 1, cada vez más estrechos y altos. Derecha: el símbolo del objeto límite. La altura de la flecha es el peso, no el valor de la función.
:::

:::satz Teorema 7.1 (Propiedades del impulso de Dirac)
<span class="anker" id="satz-7-1"></span>

<span class="anker" id="gl-7-1"></span>
<span class="anker" id="gl-7-2"></span>
<span class="anker" id="gl-7-3"></span>
<span class="anker" id="gl-7-4"></span>
<span class="anker" id="gl-7-5"></span>
<span class="anker" id="gl-7-6"></span>
$$\begin{aligned} &\text{Peso:} && [a\,\delta(t)]*s(t)=a\,s(t),\qquad a_1\delta(t)+a_2\delta(t)=(a_1+a_2)\,\delta(t),\\ &\text{Muestreo:} && \int_{-\infty}^{\infty}\delta(\tau)\,s(-\tau)\,\mathrm{d}\tau=s(0),\qquad s(t)\,\delta(t-T)=s(T)\,\delta(t-T),\\ &\text{Área:} && \int_{-\infty}^{\infty}a\,\delta(t)\,\mathrm{d} t=a,\\ &\text{Escalado:} && \delta(bt)=\frac{1}{|b|}\,\delta(t),\qquad \delta(-t)=\delta(t),\\ &\text{Desplazamiento:} && \delta(t-t_0)*s(t)=s(t-t_0),\\ &\text{Integral:} && \varepsilon(t)=\int_{-\infty}^t\delta(\tau)\,\mathrm{d}\tau,\qquad \frac{\mathrm{d}}{\mathrm{d} t}\varepsilon(t)=\delta(t). \end{aligned} \tag{7.1|7.2|7.3|7.4|7.5|7.6}$$
:::

⁠**Cómo leerlo:** el producto $s(t)\,\delta(t-T)$ solo puede tener efecto en el punto $T$, así que solo cuenta $s(T)$. Un impulso comprimido $\delta(bt)$ es igual de «infinitamente alto», pero ya solo tiene área $1/|b|$. Un sistema con $h(t)=\delta(t-t_0)$ retrasa $t_0$ cualquier señal; se llama __elemento de retardo ideal__. Y como el escalón es la integral acumulada del impulso, se pueden derivar funciones con saltos: un salto de altura $A$ se convierte en $A\,\delta$. Esto se llama __derivación generalizada__. Cuidado: muchas operaciones, por ejemplo elevar al cuadrado, $\delta^2$, no están definidas para impulsos de Dirac.

:::herleitung Escalado y producto de muestreo
⁠**Escalado.** Para $b>0$, con $\vartheta=b\tau$:

$$\delta(bt)*s(t)=\int\delta(b\tau)\,s(t-\tau)\,\mathrm{d}\tau=\frac1b\int\delta(\vartheta)\,s\Bigl(t-\frac\vartheta b\Bigr)\mathrm{d}\vartheta=\frac1b\,s(t).$$

Para $b<0$, la sustitución invierte el sentido de integración y resulta $-\frac1b=\frac{1}{|b|}$. Por tanto, $\delta(bt)$ actúa como $\frac1{|b|}\delta(t)$. Con $b=-1$ se obtiene la simetría $\delta(-t)=\delta(t)$.

⁠**Producto de muestreo.** Si se convoluciona $s(t)\delta(t)$ con una $g(t)$ cualquiera, la propiedad de muestreo da

$$[s(t)\delta(t)]*g(t)=\int s(\tau)\delta(\tau)\,g(t-\tau)\,\mathrm{d}\tau=s(0)\,g(t)=[s(0)\delta(t)]*g(t).$$

Ambos actúan igual sobre cualquier $g$; por tanto, $s(t)\delta(t)=s(0)\delta(t)$. Con un desplazamiento se obtiene $s(t)\delta(t-T)=s(T)\delta(t-T)$.

⁠**Integral.** $\varepsilon(t)=\delta(t)*\varepsilon(t)=\int\delta(\tau)\,\varepsilon(t-\tau)\,\mathrm{d}\tau$, y $\varepsilon(t-\tau)=1$ exactamente para $\tau\le t$.
:::

:::frage Pero $\delta(0)$ es infinito. Entonces $\delta(2t)$ es lo mismo que $\delta(t)$, ¿no?
No. «Infinitamente alto» no describe $\delta$, porque todos los valores de la función salvo en $0$ son iguales, y el valor en $0$ no es un número. Lo que caracteriza a $\delta$ es su área. Si se comprime el rectángulo de área 1 a la mitad de su anchura y se deja igual la altura, el área se reduce a la mitad. Por eso $\delta(2t)=\frac12\delta(t)$.
:::

:::aufgabe Ejercicio 8 ★ Calcular con $\delta$
<span class="anker" id="aufg-8"></span>

Calcula: (a) $\int_{-\infty}^\infty\delta(t-2)\,\mathrm{e}^{-t}\mathrm{d} t$, (b) $\mathrm{e}^{-t}\,\delta(t-1)$, (c) $\int_{-\infty}^\infty\delta(2t)\,\mathrm{d} t$, (d) $\delta(t)*\delta(t-3)$, (e) $\operatorname{rect}(t)*\delta(t-1)$, (f) $\frac{\mathrm{d}}{\mathrm{d} t}\bigl[3\,\varepsilon(t-1)\bigr]$.

:::loesung
(a) $\mathrm{e}^{-2}=0{,}135$. (b) $\mathrm{e}^{-1}\,\delta(t-1)$. (c) $\tfrac12$. (d) $\delta(t-3)$. (e) $\operatorname{rect}(t-1)$. (f) $3\,\delta(t-1)$.
:::
:::

## Etapa 8: Integrar y derivar

<span class="anker" id="stufe-8"></span>

:::zweck
El integrador y el derivador son sistemas LTI. A través de ellos se relacionan la respuesta al escalón y la respuesta al impulso, y se puede obtener la respuesta al impulso del circuito RC a partir de su respuesta al escalón.
:::

**El integrador.** Si en [(7.6)](#gl-7-6) se sustituye $\delta$ por una $s$ cualquiera, el mismo cálculo da:

<span class="anker" id="gl-8-1"></span>
$$s(t)*\varepsilon(t)=\int_{-\infty}^ts(\tau)\,\mathrm{d}\tau. \tag{8.1}$$

Un sistema con la respuesta al impulso $\varepsilon(t)$ forma la integral acumulada de su entrada; se llama __integrador__. Si se lee [(8.1)](#gl-8-1) con los papeles intercambiados ($\varepsilon*s$), dice: **la respuesta al escalón de un sistema es la integral acumulada de su respuesta al impulso.** Comprobación en el circuito RC: $\int_0^t\mathrm{e}^{-\tau}\mathrm{d}\tau=1-\mathrm{e}^{-t}$, exactamente [(2.5)](#gl-2-5). Dos caminos independientes, la ecuación diferencial y la convolución, dan lo mismo.

**El derivador.** Un integrador y un __derivador__ uno tras otro dejan cualquier señal sin cambios; la cascada es idealmente libre de distorsión. Por eso la respuesta al impulso del derivador es la distribución $\delta'(t)$ (__doblete__), definida por

<span class="anker" id="gl-8-2"></span>
$$\delta'(t)*s(t)=\frac{\mathrm{d}}{\mathrm{d} t}s(t). \tag{8.2}$$

De forma aproximada, $\delta'$ es un pulso rectangular doble y estrecho: primero un rectángulo de altura $+1/T_0^2$, luego otro de altura $-1/T_0^2$, cada uno de anchura $T_0$. Se dibuja como un par de flechas, una hacia arriba y otra hacia abajo.

**Respuesta al impulso = derivada de la respuesta al escalón.** Como $\delta=\frac{\mathrm{d}}{\mathrm{d} t}\varepsilon$ y el sistema es lineal e invariante en el tiempo, se cumple $h=\frac{\mathrm{d}}{\mathrm{d} t}(\text{respuesta al escalón})$. Para el circuito RC, con la regla del producto:

<span class="anker" id="gl-8-3"></span>
$$h(t)=\frac{\mathrm{d}}{\mathrm{d} t}\Bigl[\bigl(1-\mathrm{e}^{-t/RC}\bigr)\varepsilon(t)\Bigr]=\frac{1}{RC}\mathrm{e}^{-t/RC}\varepsilon(t)+\bigl(1-\mathrm{e}^{-t/RC}\bigr)\delta(t)=\frac{1}{RC}\mathrm{e}^{-t/RC}\varepsilon(t). \tag{8.3}$$

El segundo sumando desaparece por [(7.2)](#gl-7-2): $(1-\mathrm{e}^{0})\,\delta(t)=0$. El mecanismo detrás: la respuesta al escalón del circuito RC no salta; el condensador necesita tiempo para cargarse. Solo una respuesta al escalón con salto produce un impulso de Dirac en $h$ (ejercicio [9](#aufg-9)).

:::aufgabe Ejercicio 9 ★★ Paso alto: un impulso de Dirac en la respuesta al impulso
<span class="anker" id="aufg-9"></span>

Si se intercambian $R$ y $C$, la tensión se toma en $R$ (paso alto CR, $RC=1$ s). Su respuesta al escalón es $\mathrm{e}^{-t}\varepsilon(t)$.

<ol class="al">

<li>

Justifica la respuesta al escalón con el mecanismo: ¿qué tensión hay en $R$ en el primer instante y cuál al cabo de mucho tiempo?

</li>

<li>

Determina la respuesta al impulso derivando. ¿Qué significa físicamente la componente de Dirac?

</li>

<li>

Comprueba: integrar la respuesta al impulso tiene que devolver la respuesta al escalón.

</li>

</ol>

:::loesung
(a) En el primer instante el condensador está descargado y no hay tensión en él. El 1 V completo cae en $R$. Después, la corriente carga el condensador, su tensión crece como $1-\mathrm{e}^{-t}$ y en $R$ queda $\mathrm{e}^{-t}$. Al cabo de mucho tiempo, el condensador está cargado, no circula corriente y en $R$ ya no hay tensión.

(b) Regla del producto:

$$h(t)=\frac{\mathrm{d}}{\mathrm{d} t}\bigl[\mathrm{e}^{-t}\varepsilon(t)\bigr]=-\mathrm{e}^{-t}\varepsilon(t)+\mathrm{e}^{0}\,\delta(t)=\delta(t)-\mathrm{e}^{-t}\varepsilon(t).$$

Aquí la respuesta al escalón salta en $t=0$ de 0 a 1; por eso se conserva la componente de Dirac. Físicamente: un impulso infinitamente corto pasa por completo, porque el condensador no puede crear tensión en un tiempo nulo. La carga que el impulso ha llevado al condensador se descarga después a través de $R$, en sentido contrario: $-\mathrm{e}^{-t}$.

(c) $\int_{-\infty}^t\bigl[\delta(\tau)-\mathrm{e}^{-\tau}\varepsilon(\tau)\bigr]\mathrm{d}\tau=\varepsilon(t)-\bigl(1-\mathrm{e}^{-t}\bigr)\varepsilon(t)=\mathrm{e}^{-t}\varepsilon(t)$.
:::
:::

## Etapa 9: Causal y estable

<span class="anker" id="stufe-9"></span>

:::zweck
Dos propiedades que todo sistema real debe tener pueden leerse directamente en $h(t)$.
:::

:::definition Definición 9.1 (Causal, estable)
<span class="anker" id="satz-9-1"></span>

Un sistema se llama __causal__ si la salida no empieza antes que la entrada. Para un sistema LTI, esto significa

<span class="anker" id="gl-9-1"></span>
$$h(t)=0\quad\text{para }t<0. \tag{9.1}$$

Un sistema se llama __estable__ (más exactamente, estable BIBO, *bounded input, bounded output*) si responde a toda entrada acotada $|s(t)|\le A<\infty$ con una salida acotada.
:::

Causal: un impulso en el instante 0 no puede tener efecto antes. En la convolución solo contribuyen entonces los impulsos del pasado, $g(t)=\int_{-\infty}^ts(\tau)h(t-\tau)\mathrm{d}\tau$.

:::satz Teorema 9.2 (Condición de estabilidad)
<span class="anker" id="satz-9-2"></span>

Un sistema LTI es estable si y solo si su respuesta al impulso es absolutamente integrable:

<span class="anker" id="gl-9-2"></span>
$$\int_{-\infty}^{\infty}|h(\tau)|\,\mathrm{d}\tau<\infty. \tag{9.2}$$
:::

:::herleitung Condición de estabilidad
⁠**Suficiente.** Con la desigualdad triangular para integrales y $|s|\le A$:

$$|g(t)|=\Bigl|\int h(\tau)\,s(t-\tau)\,\mathrm{d}\tau\Bigr|\le\int|h(\tau)|\,|s(t-\tau)|\,\mathrm{d}\tau\le A\int|h(\tau)|\,\mathrm{d}\tau.$$

Si la integral es finita, $g$ está acotada.

⁠**Necesaria.** Si $\int|h|=\infty$, se elige la entrada acotada más desfavorable: $s(t_1-\tau)=\operatorname{sign}h(\tau)$, es decir, siempre $\pm1$ con el signo de $h$. Entonces $g(t_1)=\int|h(\tau)|\,\mathrm{d}\tau=\infty$, aunque $|s|\le1$.
:::

Ejemplos: el circuito RC tiene $\int|h|=1$ y es estable. El elemento de retardo ideal ($\int|\delta(t-t_0)|\mathrm{d} t=1$) es estable. El integrador tiene $\int_0^\infty\varepsilon\,\mathrm{d} t=\infty$ y es inestable: al escalón acotado responde con la rampa no acotada $t\,\varepsilon(t)$.

:::aufgabe Ejercicio 10 ★★ ¿Causal? ¿Estable?
<span class="anker" id="aufg-10"></span>

Estudia (a) $h(t)=\mathrm{e}^{-2t}\varepsilon(t)$, (b) $h(t)=\mathrm{e}^{t}\varepsilon(t)$, (c) $h(t)=\varepsilon(t)-\varepsilon(t-1)$, (d) $h(t)=\mathrm{e}^{-|t|}$, (e) $h(t)=\delta(t+1)$. Para cada sistema inestable, indica una entrada acotada que produzca una salida no acotada.

:::loesung
(a) Causal, $\int|h|=\tfrac12$: estable.

(b) Causal, $\int_0^\infty\mathrm{e}^t\mathrm{d} t=\infty$: inestable. El escalón $\varepsilon(t)$ produce $\int_0^t\mathrm{e}^\tau\mathrm{d}\tau=\mathrm{e}^t-1$, no acotada.

(c) Causal, $\int|h|=1$: estable. El sistema forma la integral de la entrada sobre el último segundo (ventana deslizante).

(d) No causal, porque $h(t)\neq0$ para $t<0$. $\int\mathrm{e}^{-|t|}\mathrm{d} t=2$: estable.

(e) $\delta(t+1)$ actúa en $t=-1<0$: $g(t)=s(t+1)$; el sistema «ve» la entrada con un segundo de antelación. No causal, pero estable ($\int|h|=1$).
:::
:::

## Etapa 10: Convolución sin ningún sistema

<span class="anker" id="stufe-10"></span>

:::frage La convolución tiene sentido cuando una señal pasa de verdad por un sistema. ¿Qué significa cuando no hay ningún sistema en juego?
La convolución es una operación de cálculo con un significado propio y general: *para cada forma de repartir un resultado en dos partes, se multiplican los pesos de ambas partes y se suma sobre todos los repartos.* El sistema es una interpretación de esto (primera parte: cuándo llegó el impulso; segunda parte: qué edad tiene), no la única.

⁠**Ejemplo sin sistema y sin tiempo: dos dados.** ¿Con qué probabilidad la suma de los dados es $k$? Cada reparto $k=i+(k-i)$ contribuye con la probabilidad $P_1(i)\,P_2(k-i)$:

$$P(k)=\sum_iP_1(i)\,P_2(k-i).$$

Esto es una convolución, con exactamente la misma estructura que $g(t)=\int s(\tau)h(t-\tau)\mathrm{d}\tau$: $\tau$ corresponde a los puntos del primer dado, $t$ a la suma y $t-\tau$ a los puntos del segundo. Dos dados con distribución uniforme («rectángulos») dan una distribución triangular, exactamente como $\operatorname{rect}*\operatorname{rect}=\Lambda$ en el ejercicio [5](#aufg-5). El 7 es el resultado más frecuente porque tiene más repartos (fig. [9](#abb-9)).

Otros ejemplos: una media móvil sobre valores medidos es una convolución con un rectángulo. Una foto desenfocada es la imagen nítida convolucionada con la mancha de luz que la óptica forma a partir de un punto. Y quien multiplica dos polinomios convoluciona sus coeficientes (ejercicio [11](#aufg-11)).
:::

:::abbildung et3/k1wuerfel
Probabilidades de la suma de los dados. Cada distribución es la convolución de la anterior con la de un solo dado. El rectángulo se convierte en un triángulo ($P(7)=6/36$), y este, en una curva acampanada ($P(10)=P(11)=27/216$).
:::

:::zusatz Por qué aparecen convoluciones tan a menudo
Si se convolucionan cada vez más distribuciones iguales, el resultado se aproxima a una curva de Gauss, casi con independencia de la forma de partida (teorema central del límite). Por eso el ruido, la suma de muchas influencias pequeñas e independientes, sigue tan a menudo una distribución gaussiana. Y que la convolución de los coeficientes corresponda a un producto de polinomios es el núcleo de todas las transformadas que convierten convoluciones en productos: la [parte 2](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html) hace lo mismo con los bloques $\mathrm{e}^{pt}$ en lugar de las potencias $x^n$.
:::

:::aufgabe Ejercicio 11 ★ Convolución con dados y polinomios
<span class="anker" id="aufg-11"></span>

<ol class="al">

<li>

Calcula $P(7)$ y $P(4)$ para dos dados a partir de la suma de convolución. ¿Qué repartos contribuyen en cada caso?

</li>

<li>

Calcula $P(10)$ para tres dados convolucionando la distribución de dos con la de uno.

</li>

<li>

Desarrolla $(1+2x)(3+x)$. Demuestra que la sucesión de coeficientes del resultado es la convolución de las sucesiones $(1,2)$ y $(3,1)$.

</li>

</ol>

:::loesung
(a) $P(7)$: repartos $1+6,\,2+5,\dots,6+1$, seis en total, cada uno con $\frac16\cdot\frac16$: $P(7)=\frac{6}{36}=\frac16$. $P(4)$: $1+3,\,2+2,\,3+1$: $\frac{3}{36}=\frac{1}{12}$.

(b) $P_3(10)=\sum_{j=1}^6P_2(10-j)\cdot\frac16=\frac16\bigl[P_2(9)+P_2(8)+P_2(7)+P_2(6)+P_2(5)+P_2(4)\bigr]=\frac16\cdot\frac{4+5+6+5+4+3}{36}=\frac{27}{216}=\frac18$.

(c) $(1+2x)(3+x)=3+x+6x+2x^2=3+7x+2x^2$. El coeficiente de $x^k$ reúne todos los pares de potencias con $i+j=k$: $c_0=1\cdot3=3$, $c_1=1\cdot1+2\cdot3=7$, $c_2=2\cdot1=2$. Esta es la suma de convolución $c_k=\sum_ia_ib_{k-i}$, la misma estructura que en los dados.
:::
:::

:::kern Lo esencial
<ul>

<li>

Desplazar $t\to t-t_0$ retrasa, escalar $t\to t/T$ ensancha; $a\operatorname{rect}\bigl(\frac{t-t_0}{T}\bigr)$: centro $t_0$, duración $|T|$, altura $a$.

</li>

<li>

Paso bajo RC: $H(F)=\dfrac{1}{1+\mathrm{j}2\pi FRC}$, $|H|=\dfrac{1}{\sqrt{1+(2\pi FRC)^2}}$, $\varphi=-\arctan(2\pi FRC)$; respuesta al escalón $1-\mathrm{e}^{-t/RC}$.

</li>

<li>

LTI: principio de superposición y $\operatorname{Tr}\{s(t-t_0)\}=g(t-t_0)$.

</li>

<li>

$s(t)=\int s(\tau)\delta(t-\tau)\mathrm{d}\tau$ y $g(t)=\int s(\tau)h(t-\tau)\mathrm{d}\tau=s*h$.

</li>

<li>

Calcular: reflejar, desplazar, multiplicar, integrar.

</li>

<li>

$s*\delta=s$; conmutativa, asociativa (cascada: $h_1*h_2$), distributiva (paralelo: $h_1+h_2$).

</li>

<li>

$s(t)\delta(t-T)=s(T)\delta(t-T)$; $\delta(bt)=\delta(t)/|b|$; $\delta(t-t_0)*s=s(t-t_0)$; $\frac{\mathrm{d}}{\mathrm{d} t}\varepsilon=\delta$.

</li>

<li>

Respuesta al escalón $=\int h$, respuesta al impulso $=\frac{\mathrm{d}}{\mathrm{d} t}$(respuesta al escalón).

</li>

<li>

Causal: $h(t)=0$ para $t<0$. Estable: $\int|h|\mathrm{d} t<\infty$.

</li>

</ul>
:::

**Mirada a la [parte 2](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html).** Este artículo descompone las señales en impulsos $\delta(t-\tau)$. El sistema responde a cada uno con una copia desplazada de $h$, y hay que sumar todas las copias: la convolución. La [parte 2](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html) descompone las señales en bloques $\mathrm{e}^{pt}$. A cada uno de ellos el sistema responde solo con un número $H(p)$, y la convolución se convierte en una multiplicación.

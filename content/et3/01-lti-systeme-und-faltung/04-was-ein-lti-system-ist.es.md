---
title: Etapa 3: Qué es un sistema LTI
pfad: Ingeniería eléctrica / 3.er semestre / Señales y sistemas / Sistemas LTI y convolución
order: 3210400
summary: El circuito RC tiene dos propiedades en las que se basa todo lo demás: es lineal e invariante en el tiempo.
tags: sistema, transformación, lineal, invariante en el tiempo, sistema LTI
lang: es
---

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

En el circuito RC, la linealidad se debe a que en la ecuación diferencial [(2.1)](ein-erstes-system-das-rc-glied.html#gl-2-1) no aparecen productos ni cuadrados de $u_1$ y $u_2$. La invariancia en el tiempo se debe a que $R$ y $C$ no cambian con el tiempo. Todas las redes de $R$, $L$ y $C$ se describen mediante ecuaciones diferenciales lineales con coeficientes constantes. Sin embargo, esto no vale para todo sistema LTI: un elemento de retardo ideal, por ejemplo, que solo retrasa su entrada un tiempo fijo, no tiene tal ecuación.

**Lo que permiten las dos propiedades.** Si se conoce la respuesta $g_0$ a un pulso rectangular $s_0$, se conoce sin más cálculo la respuesta a cualquier suma de pulsos rectangulares desplazados y escalados. La figura [4](#abb-4) lo muestra para $s(t)=s_0(t)+0{,}5\,s_0(t-2)$: la salida es $g_0(t)+0{,}5\,g_0(t-2)$.

:::abbildung et3/k1doppel 4
Izquierda: rectángulo $s_0$ (altura 1 V, duración 1 s) y la respuesta $g_0$ del circuito RC. Derecha: un par de pulsos. La respuesta (rojo) es la suma de $g_0(t)$ y la copia desplazada y reducida a la mitad $0{,}5\,g_0(t-2)$ (discontinua).
:::

:::frage ¿Es lineal $g(t)=2s(t)+1$? Al fin y al cabo, la característica es una recta.
No. En un sistema lineal, la entrada cero tiene que dar la salida cero: si en [(3.1)](#gl-3-1) se toman todos los $a_i=0$, resulta $\operatorname{Tr}\{0\}=0$. Aquí $\operatorname{Tr}\{0\}=1$. También falla el principio de superposición: dos entradas aplicadas por separado dan en suma $2s_1+2s_2+2$, pero aplicadas juntas dan $2s_1+2s_2+1$. Una recta que no pasa por el origen se llama *afín*, no lineal.
:::

:::ltspice Comprobar la superposición: dos rectángulos
⁠**Esquema:** el circuito RC de la etapa [2](ein-erstes-system-das-rc-glied.html#stufe-2), pero con dos fuentes `voltage` en serie: `V1`, con el polo negativo a masa y el positivo en el nodo `a`, valor `PULSE(0 {a1} 0 1u 1u 1)`; encima, `V2` de `a` a `in`, valor `PULSE(0 {a2} 2 1u 1u 1)`. En serie, las tensiones se suman; al circuito RC le llega, por tanto, $a_1s_0(t)+a_2s_0(t-2)$.

⁠**Directivas:** `.param a1=1 a2=0.5`, `.step param a1 list 0 1`, `.step param a2 list 0 0.5`, `.tran 0 6 0 1m`. LTspice calcula las cuatro combinaciones y las dibuja superpuestas.

⁠**Lo que ves:** las curvas $0$, $g_0(t)$, $0{,}5\,g_0(t-2)$ y su suma, como en la fig. [4](#abb-4). En $t=2{,}5$ s, $0{,}141+0{,}197=0{,}338$. La suma de las entradas da la suma de las respuestas (linealidad), y la fuente desplazada 2 s da la curva desplazada 2 s (invariancia en el tiempo).
:::

:::aufgabe Ejercicio 3 ★ ¿LTI o no?
<span class="anker" id="aufg-3"></span>

Comprueba para cada sistema la linealidad y la invariancia en el tiempo: (a) $g(t)=3\,s(t-2)$, (b) $g(t)=s(t)^2$, (c) $g(t)=s(t)+1$, (d) $g(t)=t\,s(t)$, (e) $g(t)=s(2t)$, (f) $g(t)=\int_{-\infty}^ts(\tau)\,\mathrm{d}\tau$.

:::loesung
(a) Lineal e invariante en el tiempo (ganancia 3, retardo 2): LTI. (b) No lineal: $\operatorname{Tr}\{2s\}=4s^2\neq2s^2$. Invariante en el tiempo. (c) No lineal (afín, $\operatorname{Tr}\{0\}=1$). Invariante en el tiempo. (d) Lineal. No invariante en el tiempo: $\operatorname{Tr}\{s(t-t_0)\}=t\,s(t-t_0)$, pero $g(t-t_0)=(t-t_0)\,s(t-t_0)$. El factor $t$ es un componente que cambia con el tiempo. (e) Lineal. No invariante en el tiempo: $\operatorname{Tr}\{s(t-t_0)\}=s(2t-t_0)$, pero $g(t-t_0)=s(2t-2t_0)$. Comprimir el tiempo comprime también cualquier desplazamiento. (f) LTI. Lineal, porque la integral es lineal. Invariante en el tiempo: $\int_{-\infty}^ts(\tau-t_0)\mathrm{d}\tau=\int_{-\infty}^{t-t_0}s(\vartheta)\mathrm{d}\vartheta=g(t-t_0)$. Su respuesta al impulso es $\varepsilon(t)$ (etapa [8](integrieren-und-differenzieren.html#stufe-8)).
:::
:::

---
title: Etapa 3: Función de correlación y producto de correlación
pfad: Ingeniería eléctrica / 3.er semestre / Señales y sistemas / Funciones de correlación
order: 3260400
summary: Un eco se parece al pulso emitido, pero está desplazado.
tags: función de autocorrelación, función de correlación cruzada, producto de correlación
lang: es
---

<span class="anker" id="stufe-3"></span>

:::zweck
Un eco se parece al pulso emitido, pero está desplazado. Por eso se compara para cada desplazamiento $\tau$.
:::

:::definition Definición 3.1 (Función de correlación para señales de energía)
<span class="anker" id="satz-3-1"></span>

<span class="anker" id="gl-3-1"></span>
$$\varphi^E_{sg}(\tau)=\int_{-\infty}^{\infty}s^*(t)\,g(t+\tau)\,\mathrm{d} t=s^*(-\tau)*g(\tau). \tag{3.1}$$

Para $g=s$ se llama __función de autocorrelación__ (FAC) $\varphi^E_{ss}(\tau)$; en otro caso, __función de correlación cruzada__ (FCC). Dividida por $\sqrt{E_sE_g}$, se llama normalizada.
:::

⁠**Cómo leerlo:** se desplaza $g$ una distancia $\tau$ hacia la izquierda y se calcula la integral del producto. El segundo signo igual es la clave: la correlación es una convolución con la señal reflejada y conjugada. Por eso se llama también __producto de correlación__. A diferencia de la convolución, aquí no se refleja nada: ambas señales avanzan en el mismo sentido.

:::herleitung correlación como convolución
En [(3.1)](#gl-3-1), sustituir $t=-\vartheta$: $\int s^*(-\vartheta)\,g(\tau-\vartheta)\,\mathrm{d}\vartheta$. Esta es la integral de convolución de $s^*(-\tau)$ con $g(\tau)$.
:::

:::satz Teorema 3.2 (Propiedades de las funciones de correlación)
<span class="anker" id="satz-3-2"></span>

<span class="anker" id="gl-3-2"></span>
<span class="anker" id="gl-3-3"></span>
$$\begin{aligned} &\varphi^E_{gs}(\tau)=\varphi^{E*}_{sg}(-\tau),\qquad\varphi^E_{ss}(\tau)=\varphi^{E*}_{ss}(-\tau)\ \ (\text{par para }s\text{ real}),\\ &|\varphi^E_{ss}(\tau)|\le\varphi^E_{ss}(0)=E_s. \end{aligned} \tag{3.2|3.3}$$

Una señal de duración limitada tiene una FAC de duración doble.
:::

⁠**Cómo leerlo:** a lo que más se parece una señal es a sí misma sin desplazar, y ahí la FAC es su energía. La FAC de un rectángulo es el triángulo: $\varphi^E_{ss}=\operatorname{rect}(-\tau)*\operatorname{rect}(\tau)=\Lambda(\tau)$, el doble de ancho que el rectángulo (fig. [1](#abb-1), izquierda).

::::beispiel encontrar un eco
Se emite $s=\operatorname{rect}(t)$ y se recibe el eco atenuado y retrasado $g=0{,}5\operatorname{rect}(t-3)$. La FCC es $\varphi^E_{sg}(\tau)=0{,}5\,\Lambda(\tau-3)$: su máximo está en $\tau=3$, el retardo, y su altura $0{,}5=0{,}5\cdot E_s$ indica la atenuación (fig. [1](#abb-1), derecha). Así mide un radar la distancia.

:::abbildung et3/k6korr 1
Izquierda: la FAC del rectángulo es el triángulo, con máximo $=E_s=1$ en $\tau=0$ y el doble de anchura. Derecha: la FCC entre el pulso emitido y el eco $0{,}5\operatorname{rect}(t-3)$ tiene su máximo en el retardo $\tau=3$.
:::
::::

:::frage La convolución y la correlación parecen casi iguales. ¿Dónde está la diferencia?
En la convolución, $\int s(\tau)h(t-\tau)\mathrm{d}\tau$, la segunda señal avanza hacia atrás ($-\tau$): el sistema «recuerda» el pasado. En la correlación, $\int s^*(t)g(t+\tau)\mathrm{d} t$, ambas avanzan hacia delante: se colocan dos formas una exactamente sobre la otra y se mide su coincidencia. En el cálculo, la diferencia es precisamente la reflexión; por eso la correlación es una convolución con la señal reflejada.
:::

:::ltspice Encontrar un eco con un integrador deslizante
Un filtro que en cada instante integra sobre el último segundo forma $y(t)=\int_{t-1}^{t}g(u)\,\mathrm{d} u$. Con $s=\operatorname{rect}(t)$, esto es exactamente la FCC [(3.1)](#gl-3-1), retrasada 0,5 s: $y(t)=\varphi^E_{sg}(t-0{,}5)$. El filtro la calcula para todos los $\tau$ mientras llega la señal.

⁠**Esquema:** fuente `voltage` en el nodo `g` con `PULSE(0 0.5 2.5 1u 1u 1)`, el eco $0{,}5\operatorname{rect}(t-3)$. Dos fuentes de comportamiento `bv`: en el nodo `int`, con `V=idt(V(g))` (integral acumulada), y en el nodo `y`, con `V=V(int)-delay(V(int),1)` (integral sobre el último segundo).

⁠**Directivas:** `.tran 0 6 0 1m`, `.meas tran ymax MAX V(y)`.

⁠**Lo que ves:** `V(y)` es el triángulo $0{,}5\,\Lambda(t-3{,}5)$, con el máximo 0,5 en $t=3{,}5$ s: el retardo de 3 s más 0,5 s, porque el filtro no termina de integrar hasta el final del eco. La altura 0,5 es la atenuación del eco.

⁠**Para el ejercicio [3](#aufg-3):** entrada `PULSE(0 1 0 1u 1u 1 2 2)`, el doble rectángulo, ambos rectángulos 0,5 s más tarde que en el texto. Para `y` tomas

`V=V(int)-delay(V(int),1)+delay(V(int),2)-delay(V(int),3)`.

Este filtro integra sobre dos ventanas que encajan con el doble rectángulo, y `V(y)` es su FAC, desplazada 3 s. Compara con tu resultado del ejercicio [3](#aufg-3)(a).
:::

:::aufgabe Ejercicio 3 ★★ Eco y repetición
<span class="anker" id="aufg-3"></span>

<ol class="al">

<li>

Una señal consta de dos rectángulos: $s(t)=\operatorname{rect}(t)+\operatorname{rect}(t-2)$. Determina su FAC. ¿En qué se ve la repetición?

</li>

<li>

Comprueba [(3.3)](#gl-3-3) para esta señal.

</li>

</ol>

:::loesung
(a) Con $\operatorname{rect}(-\tau)=\operatorname{rect}(\tau)$ y $\operatorname{rect}*\operatorname{rect}=\Lambda$, los cuatro productos parciales dan

$$\varphi^E_{ss}(\tau)=2\Lambda(\tau)+\Lambda(\tau-2)+\Lambda(\tau+2).$$

Los picos secundarios en $\tau=\pm2$ muestran la separación de la repetición. Allí, uno de los dos rectángulos queda sobre el otro. En $\tau=0$ quedan ambos superpuestos, lo que da la altura doble.

(b) $\varphi^E_{ss}(0)=2=E_s=1+1$, y los picos secundarios solo valen 1.
:::
:::

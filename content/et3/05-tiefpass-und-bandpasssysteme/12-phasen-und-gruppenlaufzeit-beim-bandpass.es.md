---
title: Etapa 11: Retardo de fase y de grupo en el paso banda
pfad: Ingeniería eléctrica / 3.er semestre / ET3 – Fundamentos de ingeniería eléctrica 3: señales y sistemas / Sistemas paso bajo y paso banda
adresse: elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme
knoten: Capítulo 5: Sistemas paso bajo y paso banda
order: 3251200
summary: ¿Por qué hay dos retardos?
tags: distorsión de retardo
lang: es
---

<span class="anker" id="stufe-11"></span>

:::zweck
¿Por qué hay dos retardos? Porque la portadora y la envolvente pueden retrasarse de forma distinta.
:::

**La idea.** Supongamos que un paso banda tiene en la banda de paso un módulo constante y una fase ligeramente curvada. En torno a $f_0$, esta se aproxima por su tangente:

$$\varphi(f)\approx\varphi(f_0)+(f-f_0)\frac{\mathrm{d}\varphi}{\mathrm{d} f}\Big|_{f_0}=-2\pi f_0t_\mathrm p-2\pi(f-f_0)t_\mathrm g$$

con $t_\mathrm p=t_\mathrm p(f_0)$ y $t_\mathrm g=t_\mathrm g(f_0)$ de [(1.4)](das-verzerrungsfreie-system.html#gl-1-4) y [(1.5)](das-verzerrungsfreie-system.html#gl-1-5). En el dominio paso bajo ($f-f_0\to f$), esto es $H_T(f)=2\operatorname{rect}(f/\Delta f)\,\mathrm{e}^{-\mathrm{j}2\pi f_0t_\mathrm p}\,\mathrm{e}^{-\mathrm{j}2\pi ft_\mathrm g}$: una fase constante y un retardo.

:::satz Teorema 11.1 (Retardos en el paso banda)
<span class="anker" id="satz-11-1"></span>

<span class="anker" id="gl-11-1"></span>
$$g_T(t)=s_T(t-t_\mathrm g)\,\mathrm{e}^{-\mathrm{j}2\pi f_0t_\mathrm p},\qquad g(t)=\operatorname{Re}\bigl\{s_T(t-t_\mathrm g)\,\mathrm{e}^{\mathrm{j}2\pi f_0(t-t_\mathrm p)}\bigr\}. \tag{11.1}$$
:::

⁠**Cómo leerlo:** la envolvente, que transporta la información, sufre el *retardo de grupo*. La portadora sufre el *retardo de fase*. La transmisión solo está libre de distorsión en sentido estricto si ambos son iguales. Es decir, la recta de fase pasa por el origen (o por un múltiplo de $2\pi$ en $f=0$). Para la información suele bastar ya con un retardo de grupo constante: si $t_\mathrm g$ no es constante, las distintas componentes de frecuencia de la envolvente llegan en instantes distintos y los pulsos se ensanchan (__distorsión de retardo__).

:::ltspice La envolvente y la portadora llegan en instantes distintos
⁠**Esquema:** el circuito resonante del recuadro LTspice de la etapa [9](bandpasssignal-durch-bandpasssystem.html#stufe-9) ($f_0=10$ Hz, $\Delta f=2$ Hz). En el análisis `.ac`, su fase en 10 Hz es $0^\circ$; por tanto, $t_\mathrm p(f_0)=0$. Si cambias el eje de fase a «Group Delay», muestra en 10 Hz $t_\mathrm g(f_0)=0{,}16$ s.

⁠**Experimento:** como entrada, una fuente de comportamiento `bv`, una portadora con una envolvente que varía lentamente:

`V=(1+0.5*cos(2*pi*0.2*time))*cos(2*pi*10*time)`

Directivas `.tran 0 20 0 0.2m` y `.options plotwinsize=0`.

⁠**Lo que ves:** dibuja `V(in)` y `V(out)` superpuestas y amplía el tramo de 14,5 s a 15,5 s. El máximo de la envolvente llega a la salida unos 0,16 s más tarde, pero los pasos por cero de la portadora están en los mismos sitios que en la entrada. Es exactamente lo que dice [(11.1)](#gl-11-1): la envolvente se retrasa $t_\mathrm g$, y la portadora, $t_\mathrm p$.
:::

:::aufgabe Ejercicio 10 ★★ Leer los retardos
<span class="anker" id="aufg-10"></span>

En $f_0=1$ MHz, un paso banda tiene la fase $\varphi(f_0)=-\pi/2$ y la pendiente $\frac{\mathrm{d}\varphi}{\mathrm{d} f}=-2\pi\cdot2\,\mu\text{s}$.

<ol class="al">

<li>

Calcula $t_\mathrm p$ y $t_\mathrm g$.

</li>

<li>

¿Cuánto se retrasa la envolvente de un pulso a la salida? ¿Está después la portadora todavía en la misma posición respecto a la envolvente?

</li>

</ol>

:::loesung
(a) $t_\mathrm p=-\frac{\varphi(f_0)}{2\pi f_0}=\frac{\pi/2}{2\pi\cdot10^6\,\mathrm{Hz}}=0{,}25$ µ s. $t_\mathrm g=2$ µ s.

(b) La envolvente llega 2 µ s más tarde. La portadora solo está desplazada 0,25 µ s. Respecto a la envolvente, está por tanto girada $2\pi f_0(t_\mathrm g-t_\mathrm p)=3{,}5\pi$, que módulo $2\pi$ es igual a $1{,}5\pi$, es decir, $-\pi/2$: un cuarto de periodo. La información de la envolvente se conserva sin distorsión mientras $t_\mathrm g$ sea constante en toda la banda.
:::
:::

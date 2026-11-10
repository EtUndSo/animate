---
title: Etapa 5: Correlación y sistemas LTI
pfad: Ingeniería eléctrica / 3.er semestre / ET3 – Fundamentos de ingeniería eléctrica 3: señales y sistemas / Funciones de correlación
adresse: elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen
knoten: Capítulo 6: Funciones de correlación
order: 3260600
summary: ¿Qué le hace un sistema LTI a la FAC y a la densidad espectral de energía?
tags: 
lang: es
---

<span class="anker" id="stufe-5"></span>

:::zweck
¿Qué le hace un sistema LTI a la FAC y a la densidad espectral de energía? ¿Y cómo se mide un sistema con la correlación cruzada?
:::

:::satz Teorema 5.1 (Wiener-Lee)
<span class="anker" id="satz-5-1"></span>

Para $g=s*h$:

<span class="anker" id="gl-5-1"></span>
$$\varphi^E_{gg}(\tau)=\varphi^E_{ss}(\tau)*\varphi^E_{hh}(\tau)\;\circ\!\!-\!\!\bullet\;|G(f)|^2=|S(f)|^2\,|H(f)|^2, \tag{5.1}$$

<span class="anker" id="gl-5-2"></span>
$$\varphi^E_{sg}(\tau)=\varphi^E_{ss}(\tau)*h(\tau)\;\circ\!\!-\!\!\bullet\;|S(f)|^2\,H(f). \tag{5.2}$$
:::

:::herleitung Wiener-Lee
$\varphi^E_{gg}=g^*(-\tau)*g(\tau)=[s^*(-\tau)*h^*(-\tau)]*[s(\tau)*h(\tau)]$. Reordenar según las leyes conmutativa y asociativa: $[s^*(-\tau)*s(\tau)]*[h^*(-\tau)*h(\tau)]=\varphi^E_{ss}*\varphi^E_{hh}$. Del mismo modo, $\varphi^E_{sg}=s^*(-\tau)*s(\tau)*h(\tau)$.
:::

⁠**Cómo leerlo:** el sistema multiplica la energía en cada frecuencia por $|H|^2$. La fase del sistema no influye en la energía. La ecuación [(5.2)](#gl-5-2) es un método de medida: si la entrada tiene una FAC que es casi un impulso de Dirac ponderado $c\,\delta(\tau)$ (por ejemplo, un pulso muy corto), la correlación cruzada entre la entrada y la salida es casi $c\,h(\tau)$, es decir, la respuesta al impulso salvo el factor $c$. A diferencia de $|H|^2$, contiene también la fase.

:::ltspice Energía antes y después del circuito RC
⁠**Esquema:** fuente de comportamiento `bv` en el nodo `s` con `V=exp(-time)*(time>0)`, el pulso exponencial $\varepsilon(t)\mathrm{e}^{-t}$. El factor `(time>0)` hace que LTspice calcule el estado inicial en $t=0$ con 0 V y que el condensador empiece descargado. Detrás, el circuito RC (`res` con `1Meg`, `cap` con `1u`) con la salida en el nodo `g`.

⁠**Directivas:** `.tran 0 30 0 1m`, `.meas tran Es INTEG V(s)*V(s)` y `.meas tran Eg INTEG V(g)*V(g)`, las energías según [(1.1)](energie-und-leistung.html#gl-1-1).

⁠**Lo que ves:** `Es` $=0{,}500$, como $E_s=\varphi^E_{ss}(0)=\frac12$ en la etapa [4](energiedichtespektrum.html#stufe-4). Compara `Eg` con tu resultado del ejercicio [5](#aufg-5). La energía de salida es menor porque el circuito RC multiplica la energía en cada frecuencia por $|H|^2\le1$.
:::

:::aufgabe Ejercicio 5 ★★ Energía a la salida
<span class="anker" id="aufg-5"></span>

El pulso exponencial $\varepsilon(t)\mathrm{e}^{-t}$ pasa por un circuito RC con $RC=1$ s.

<ol class="al">

<li>

Determina $|G(f)|^2$ y, a partir de ahí, la energía de salida. Pista: $\int_{-\infty}^\infty\frac{\mathrm{d} x}{(1+x^2)^2}=\frac\pi2$.

</li>

<li>

Compruébalo en el dominio del tiempo con $g(t)=t\,\mathrm{e}^{-t}\varepsilon(t)$ ([capítulo 1](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html), dos circuitos RC en cascada).

</li>

</ol>

:::loesung
(a) $|G|^2=|S|^2|H|^2=\frac{1}{(1+(2\pi f)^2)^2}$. Con $x=2\pi f$: $E_g=\frac{1}{2\pi}\int\frac{\mathrm{d} x}{(1+x^2)^2}=\frac{1}{2\pi}\cdot\frac\pi2=\frac14$.

(b) $\int_0^\infty t^2\mathrm{e}^{-2t}\mathrm{d} t=\frac{2}{2^3}=\frac14$. Ambos caminos coinciden. La energía baja de $\frac12$ a $\frac14$ porque el segundo circuito RC atenúa aún más las frecuencias altas.
:::
:::

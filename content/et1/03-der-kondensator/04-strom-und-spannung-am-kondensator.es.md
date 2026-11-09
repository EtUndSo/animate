---
title: Etapa 3: Corriente y tensión en el condensador
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / El condensador
order: 1130400
summary: En una resistencia, la tensión fija la corriente en el mismo instante.
tags: fuente de corriente
lang: es
---

<span class="anker" id="stufe-3"></span>

:::zweck
En una resistencia, la tensión fija la corriente en el mismo instante. En un condensador es distinto: aquí la corriente depende de lo rápido que cambie la tensión. Esta etapa establece la ley.
:::

**La idea.** La tensión indica cuánta carga ha entrado hasta ese momento. La corriente cambia esa carga. Si circula mucha corriente, la tensión sube deprisa. Si no circula ninguna, se queda como está, aunque sea alta. Por tanto, la corriente no se deduce del valor de la tensión, sino de su variación.

:::satz Teorema 3.1 (Corriente y tensión en el condensador)
<span class="anker" id="satz-3-1"></span>

Con las flechas de referencia de corriente y tensión en el mismo sentido ([Parte 2](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)), para magnitudes dependientes del tiempo se cumple

<span class="anker" id="gl-3-1"></span>
<span class="anker" id="gl-3-2"></span>
$$\begin{aligned} i(t)&=\frac{\mathrm{d} q}{\mathrm{d} t}=C\,\frac{\mathrm{d} u(t)}{\mathrm{d} t},\\ u(t)&=\frac{q(t)}{C}=u(t_0)+\frac1C\int_{t_0}^{t}i(t')\,\mathrm{d} t'. \end{aligned} \tag{3.1|3.2}$$
:::

:::herleitung Corriente y tensión
La corriente es carga por unidad de tiempo, $i=\mathrm{d} q/\mathrm{d} t$ ([Parte 2](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)). Sustituyendo $q=C\,u$ y sacando fuera el número constante $C$ se obtiene [(3.1)](#gl-3-1). A la inversa, la carga es el área bajo la curva de corriente, igual que el camino es el área bajo la velocidad ([Parte 1](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)): $q(t)=q(t_0)+\int_{t_0}^{t}i\,\mathrm{d} t'$. Dividiendo por $C$ se obtiene [(3.2)](#gl-3-2).
:::

⁠**Cómo leerlo:** Las minúsculas indican magnitudes dependientes del tiempo, $t'$ es la variable de integración, $u(t_0)$ la tensión en el instante inicial. $i$ en A, $C$ en F, $\mathrm{d} u/\mathrm{d} t$ en V/s. 1 mA en 100 µF hace subir la tensión a razón de 10 V/s. **Signo:** $q$ es la carga de la placa hacia la que apunta la flecha de corriente. Con $i>0$ crece y $u$ sube; con $i<0$, $u$ baja. **Validez:** $C$ debe ser constante.

**Dos consecuencias.** Primera: **La tensión no salta.** Un salto de $\Delta U$ en el tiempo $\Delta t$ exige $i=C\,\Delta U/\Delta t$. Para $\Delta t\to0$, la corriente crecería sin límite, porque la carga $C\,\Delta U$ tendría que llegar en un tiempo nulo. 9 V en 1 µs en 100 µF exigen ya 900 A. La corriente, en cambio, sí puede saltar, porque no está ligada a una magnitud almacenada. Segunda: **Con tensión constante no circula corriente.** Con $\mathrm{d} u/\mathrm{d} t=0$ es $i=0$: el condensador bloquea la corriente continua.

::::beispiel
Una __fuente de corriente__, un componente que mantiene fija su corriente con independencia de la tensión, alimenta a través del interruptor S una resistencia y un condensador sin carga en serie (fig. [3](#abb-3)). Entrega $I=0{,}9$ mA; $R$ y $C$ son los valores del circuito RC. Al cerrar S en $t=0$, $u_R$ salta al valor fijo $R\,I=9$ V. En el condensador, [(3.2)](#gl-3-2) con $u_C(0)=0$ da

<span class="anker" id="gl-3-3"></span>
$$u_C(t)=\frac{Q(t)}{C}=\frac{I\,t}{C}=9\,\mathrm{V/s}\cdot t. \tag{3.3}$$

La tensión crece en línea recta. Parte de cero de forma continua, aunque la corriente salte. Una fuente de corriente ideal sigue cargando sin fin, hasta que se produce la ruptura del dieléctrico. En 1 s, ambas tensiones son iguales.

:::abbildung et1/k3rampe 3
Una fuente de corriente carga un condensador a través de $R=10\,\mathrm{k\Omega}$. Al cerrar S, $u_R$ salta a 9 V y se queda ahí. $u_C$ parte de cero y sube a razón de 9 V/s, porque cada segundo llega la misma carga.
:::
::::

⁠**Caso límite:** Para $C\to\infty$, la pendiente se hace cero y la tensión no se mueve. Por eso, un condensador muy grande mantiene fija una tensión.

:::frage En un condensador vacío hay 0 V. ¿No tiene que ser entonces cero la corriente?
Eso vale para una resistencia. En un condensador, $u=0$ no dice nada sobre $i$, porque $i$ depende de la pendiente de $u$, no de su valor. En la fig. [3](#abb-3), en $t=0$ la tensión es cero, pero la corriente es de 0,9 mA.
:::

:::aufgabe Ejercicio 3 ★★ De la corriente a la tensión y de vuelta
<span class="anker" id="aufg-3"></span>

Un condensador de 100 µF está vacío en $t=0$. La corriente es de $+0{,}5$ mA de 0 a 2 s, nula de 2 s a 3 s y de $-1$ mA de 3 s a 4 s.

<ol class="al">

<li>

Dibuja $u(t)$ e indica los valores en 2 s, 3 s y 4 s.

</li>

<li>

¿Qué carga lleva en 3 s?

</li>

<li>

En otro condensador de 10 µF, la tensión sube uniformemente de 2 V a 7 V en 5 ms. ¿Qué corriente circula?

</li>

<li>

¿Por qué $i(t)$ puede tener un escalón vertical, pero $u(t)$ no?

</li>

</ol>

:::loesung
(a) Con corriente constante, $u$ es una recta de pendiente $i/C$. De 0 a 2 s: $0{,}5\,\mathrm{mA}/100\,\mu\text{F}=5$ V/s, es decir, $u(2\,\mathrm{s})=10$ V. De 2 s a 3 s: $i=0$, la tensión se mantiene en 10 V. De 3 s a 4 s: $-10$ V/s, es decir, $u(4\,\mathrm{s})=0$. La curva es un trapecio.

(b) $Q=C\,u=100\,\mu\text{F}\cdot10\,\mathrm{V}=1$ mC. Esa es también el área bajo $i(t)$ hasta 3 s: $0{,}5\,\mathrm{mA}\cdot2\,\mathrm{s}$.

(c) $i=C\,\Delta u/\Delta t=10\,\mu\text{F}\cdot5\,\mathrm{V}/5\,\mathrm{ms}=10$ mA.

(d) $u$ se obtiene del área bajo $i$. Un área siempre crece de forma continua, aunque $i$ tenga un escalón. Un escalón en $u$, en cambio, exigiría una corriente ilimitada.
:::
:::

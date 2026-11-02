---
title: Etapa 9: Carga a través de una resistencia
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / El condensador
order: 1131000
summary: En una fuente de tensión, la corriente de carga depende de la tensión del condensador, y esta depende de la corriente de carga.
tags: cortocircuito, circuito abierto, ecuación diferencial
lang: es
---

<span class="anker" id="stufe-9"></span>

:::zweck
En una fuente de tensión, la corriente de carga depende de la tensión del condensador, y esta depende de la corriente de carga. Esta etapa plantea la ecuación de esta realimentación y la resuelve desde cero.
:::

**La idea.** En el circuito RC (fig. [9](#abb-9)), el interruptor S pasa en $t=0$ de la posición 2 a la 1, y el condensador está vacío. La tensión no puede saltar (etapa [3](strom-und-spannung-am-kondensator.html#stufe-3)), así que $u_C(0)=0$. Toda la tensión de la batería está en $R$, y circula $i(0)=U_0/R=0{,}9$ mA. En ese instante, el condensador se comporta como un cable, de ahí el término __cortocircuito__: circula corriente, la tensión es cero. El motivo: aún no hay carga separada, así que no hay campo que se oponga a la corriente.

La corriente lleva carga, y $u_C$ sube. Por la ley de mallas queda menos para $R$, la corriente baja y $u_C$ sube más despacio. Esta realimentación da forma a toda la curva. Al final, $u_C=U_0$. En $R$ no queda nada, $i=0$: el condensador se comporta como un __circuito abierto__, los terminales actúan como si estuvieran sueltos. El motivo: el campo de la carga separada eleva la placa al potencial del polo, y a lo largo de $R$ no queda ninguna caída.

:::abbildung et1/k3rckreis 9
Izquierda, el circuito RC con flechas de referencia, ley de mallas $U_0=u_R+u_C$. La posición 1 carga, la posición 2 descarga. Derecha, los dos circuitos equivalentes: en $t=0$, el condensador vacío actúa como un cable; tras mucho tiempo, el lleno actúa como unos terminales abiertos.
:::

**La ecuación.** La ley de mallas ([Parte 2](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)) dice $U_0=u_R+u_C$. Con la ley de Ohm $u_R=R\,i$ y con $i=C\,\mathrm{d} u_C/\mathrm{d} t$ de [(3.1)](strom-und-spannung-am-kondensator.html#gl-3-1) resulta

<span class="anker" id="gl-9-1"></span>
$$U_0=R\,C\,\frac{\mathrm{d} u_C}{\mathrm{d} t}+u_C. \tag{9.1}$$

Es una __ecuación diferencial__: una ecuación en la que la magnitud buscada aparece junto con su derivada. Lo que se busca no es un número, sino toda una función $u_C(t)$. Reordenada con $\tau=RC$, dice

<span class="anker" id="gl-9-2"></span>
$$\frac{\mathrm{d} u_C}{\mathrm{d} t}=\frac{U_0-u_C}{\tau}. \tag{9.2}$$

En palabras: la pendiente de la curva es la distancia al valor final, dividida por $\tau$. Así, a cada punto $(t,u_C)$ le corresponde una pendiente (fig. [10](#abb-10)). Quien empieza en el valor inicial y sigue en todas partes esta pendiente dibuja la solución. Por eso, a cada valor inicial le corresponde exactamente una curva.

:::abbildung et1/k3richtung 10
La ecuación [(9.2)](#gl-9-2) en imagen: cada trazo gris muestra la pendiente en ese lugar, para $U_0=9$ V y $\tau=1$ s. Muy por debajo de 9 V es grande, en 9 V es cero y por encima es negativa. Las curvas siguen los trazos desde los valores iniciales 0 V, 3 V y 12 V y se acercan todas al mismo valor final.
:::

:::satz Teorema 9.1 (Carga)
<span class="anker" id="satz-9-1"></span>

Para $u_C(0)=0$ y $t\ge0$ se cumple

<span class="anker" id="gl-9-3"></span>
$$u_C(t)=U_0\bigl(1-\mathrm{e}^{-t/\tau}\bigr),\qquad i(t)=\frac{U_0}{R}\,\mathrm{e}^{-t/\tau},\qquad u_R(t)=U_0\,\mathrm{e}^{-t/\tau},\qquad\tau=R\,C. \tag{9.3}$$
:::

⁠**Cómo leerlo:** $\mathrm{e}=2{,}718$ es el número de Euler. $\tau$ es la constante de tiempo en s: $\mathrm{\Omega\cdot F}=\frac{\mathrm V}{\mathrm A}\cdot\frac{\mathrm{A\,s}}{\mathrm V}=\mathrm s$. El factor $\mathrm{e}^{-t/\tau}$ empieza en 1 y cae en cada tiempo $\tau$ a $1/\mathrm{e}$ de su valor, es decir, al 36,8 %. **Validez:** componentes ideales, fuente constante, $t=0$ es el instante de la conmutación.

:::herleitung Resolver la ecuación desde cero
⁠**Paso 1: Solo cuenta la distancia al final.** Sea $x(t)=U_0-u_C(t)$. Como $U_0$ es constante, $\mathrm{d} x/\mathrm{d} t=-\mathrm{d} u_C/\mathrm{d} t$, y [(9.2)](#gl-9-2) se convierte en

$$\frac{\mathrm{d} x}{\mathrm{d} t}=-\frac{x}{\tau},\qquad x(0)=U_0.$$

La variación de $x$ es proporcional a la propia $x$: cuanto mayor es el resto, más deprisa se reduce.

⁠**Paso 2: Dividir por $x$.** Para $x>0$ es $\frac1x\,\frac{\mathrm{d} x}{\mathrm{d} t}=-\frac1\tau$. Por la regla de la cadena, el miembro izquierdo es la derivada de $\ln x(t)$, porque $\frac{\mathrm{d}}{\mathrm{d} t}\ln x(t)=\frac1x\,\frac{\mathrm{d} x}{\mathrm{d} t}$.

⁠**Paso 3: Integrar.** Así, $\ln x(t)$ tiene la pendiente constante $-1/\tau$ y es una recta: $\ln x(t)=-t/\tau+K$ con una constante $K$.

⁠**Paso 4: Deshacer el logaritmo.** Aplicando la función exponencial a ambos miembros se obtiene $x(t)=\mathrm{e}^{K}\,\mathrm{e}^{-t/\tau}$. Para $t=0$ queda $x(0)=\mathrm{e}^{K}$, es decir, $\mathrm{e}^{K}=U_0$. Así, $x(t)=U_0\,\mathrm{e}^{-t/\tau}$.

⁠**Paso 5: Volver a la variable original.** $u_C=U_0-x=U_0(1-\mathrm{e}^{-t/\tau})$. Derivando: $i=C\,\mathrm{d} u_C/\mathrm{d} t=\frac{C\,U_0}{\tau}\mathrm{e}^{-t/\tau}=\frac{U_0}{R}\mathrm{e}^{-t/\tau}$, y $u_R=R\,i$.

⁠**Verificación:** Sustituyendo en [(9.1)](#gl-9-1) se obtiene $R\,C\cdot\frac{U_0}{\tau}\mathrm{e}^{-t/\tau}+U_0-U_0\mathrm{e}^{-t/\tau}=U_0$. Es correcto.

⁠**El mismo camino a través de la corriente:** De $U_0=R\,i+\frac1C\int_0^ti\,\mathrm{d} t'$, derivando, resulta $0=R\,\frac{\mathrm{d} i}{\mathrm{d} t}+\frac iC$. Escrito de forma breve, es $\frac{\mathrm{d} i}{i}=-\frac{\mathrm{d} t}{RC}$, y los pasos 2 a 4 dan $\ln i=-\frac{t}{RC}+\ln\frac{U_0}{R}$, es decir, de nuevo $i=\frac{U_0}{R}\mathrm{e}^{-t/RC}$.
:::

**Ejemplo.** En el modelo de referencia, tras $t=1$ s es $u_C=9\,\mathrm{V}\cdot(1-\mathrm{e}^{-1})=5{,}69$ V, $u_R=3{,}31$ V e $i=0{,}331$ mA (fig. [11](#abb-11)). Las dos tensiones suman 9 V en todo momento. La tangente en el inicio sube a razón de $U_0/\tau=9$ V/s y alcanza 9 V exactamente en $t=\tau$: si la corriente inicial se mantuviera constante como en la etapa [3](strom-und-spannung-am-kondensator.html#stufe-3), el condensador estaría lleno tras $\tau$. **En resumen:** $\tau$ es la carga final dividida por la corriente inicial, $C\,U_0/(U_0/R)=RC$.

:::abbildung et1/k3laden 11
Carga con $U_0=9$ V, $R=10\,\mathrm{k\Omega}$ y $C=100\,\mu\text{F}$. Izquierda, las tensiones; derecha, la corriente. La corriente salta de cero a 0,9 mA en $t=0$ y se extingue. Las tangentes en el inicio alcanzan el valor final en $t=\tau=1$ s. Los puntos corresponden a $t=\tau$.
:::

⁠**Casos límite:** Para $t\to0$, $\mathrm{e}^{-t/\tau}\to1$: $u_C=0$, $i=U_0/R$; es el cortocircuito. Para $t\to\infty$, $\mathrm{e}^{-t/\tau}\to0$: $u_C=U_0$, $i=0$; es el circuito abierto. Para $R\to0$, $\tau\to0$ e $i(0)\to\infty$. Con una resistencia real de cableado de 0,1 $\Omega$ serían 90 A durante 10 µs.

:::frage ¿Llega el condensador alguna vez a estar del todo lleno?
Matemáticamente nunca, porque $\mathrm{e}^{-t/\tau}$ no llega a cero. En la práctica, tras unos pocos $\tau$: tras $5\tau$ falta el 0,7 %, en el modelo de referencia 61 mV. La corriente de carga es entonces de solo 6 µA y está en el orden de magnitud de la corriente de fuga de la etapa [5](bauformen-und-selbstentladung.html#stufe-5).
:::

:::aufgabe Ejercicio 10 ★★ Otro circuito RC
<span class="anker" id="aufg-10"></span>

Una fuente de 12 V carga a través de 4,7 k$\Omega$ un condensador vacío de 220 µF.

<ol class="al">

<li>

Calcula $\tau$ e $i(0)$.

</li>

<li>

¿Cuánto vale $u_C$ tras 1 s?

</li>

<li>

¿Cuándo alcanza $u_C$ la mitad de 12 V y cuándo el 99 %?

</li>

<li>

Predice: ¿qué cambia en $\tau$ y en $i(0)$ si $R$ se duplica, y qué en la tensión final?

</li>

</ol>

:::loesung
(a) $\tau=4{,}7\,\mathrm{k\Omega}\cdot220\,\mu\text{F}=1{,}034$ s, $i(0)=12\,\mathrm{V}/4{,}7\,\mathrm{k\Omega}=2{,}55$ mA.

(b) $u_C=12\,\mathrm{V}\cdot(1-\mathrm{e}^{-1/1{,}034})=7{,}44$ V.

(c) $\mathrm{e}^{-t/\tau}=\frac12$ da $t=\tau\ln2=0{,}717$ s. Para el 99 %, $\mathrm{e}^{-t/\tau}=0{,}01$, es decir, $t=\tau\ln100=4{,}76$ s.

(d) $\tau$ se duplica, $i(0)$ se reduce a la mitad, la tensión final sigue siendo 12 V, porque al final ya no circula corriente por $R$.
:::
:::

:::aufgabe Ejercicio 11 ★★★ El balance energético de la carga
<span class="anker" id="aufg-11"></span>

El condensador del circuito RC se carga de 0 a $U_0$.

<ol class="al">

<li>

Demuestra con $W_\mathrm{B}=\int_0^\infty U_0\,i\,\mathrm{d} t$ que la batería cede $C\,U_0^2$.

</li>

<li>

Demuestra con $W_R=\int_0^\infty R\,i^2\,\mathrm{d} t$ que en la resistencia $\frac12CU_0^2$ se convierte en calor. Da los números del modelo de referencia.

</li>

<li>

¿Por qué $R$ no aparece en el resultado, aunque toda la pérdida se produce en $R$?

</li>

</ol>

:::loesung
(a) $W_\mathrm{B}=U_0\int_0^\infty i\,\mathrm{d} t=U_0\,Q=C\,U_0^2$, porque la integral de la corriente es la carga. Cálculo: $\int_0^\infty\frac{U_0}{R}\mathrm{e}^{-t/\tau}\mathrm{d} t=\frac{U_0}{R}\tau=C\,U_0$.

(b) $W_R=\int_0^\infty R\,\frac{U_0^2}{R^2}\mathrm{e}^{-2t/\tau}\mathrm{d} t=\frac{U_0^2}{R}\cdot\frac\tau2=\frac12CU_0^2$. Modelo de referencia: la batería entrega 8,10 mJ; 4,05 mJ van al condensador y otros 4,05 mJ a la resistencia.

(c) Una $R$ menor aumenta la corriente, pero acorta el tiempo. Por eso, en $W_R=\frac{U_0^2}{R}\cdot\frac{\tau}{2}=\frac{U_0^2}{R}\cdot\frac{RC}{2}$, $R$ se simplifica exactamente. El rendimiento de la carga desde una tensión fija es siempre del 50 %, siempre que el condensador parta de cero. El mismo cálculo está detrás de la pérdida [(8.3)](ladungserhaltung-beim-umschalten.html#gl-8-3).
:::
:::

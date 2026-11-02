---
title: Etapa 9: Rectificadores y bomba de carga
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / Semiconductores y diodos
order: 1191100
summary: El rectificador de media onda desperdicia una de cada dos semiondas.
tags: rectificador en puente, filtrado
lang: es
---

<span class="anker" id="stufe-9"></span>

:::zweck
El rectificador de media onda desperdicia una de cada dos semiondas. Esta etapa aprovecha ambas y muestra cómo elevar una tensión por encima de la tensión de la fuente con diodos y condensadores.
:::

**La idea.** El __rectificador en puente__ (circuito de Graetz) consta de cuatro diodos en rombo (fig. [11](#abb-11)). Conmutan la carga en cada semionda de modo que la corriente siempre la recorre de arriba abajo. Con tensión positiva a la izquierda, pasa por D$_1$, la carga y D$_3$. Mientras tanto, D$_2$ tiene el cátodo arriba, en el potencial alto, y el ánodo en la entrada baja, así que bloquea, y lo mismo D$_4$. En la otra semionda las parejas se intercambian.

:::abbildung et1/k9graetz 11
Arriba: puente en ambas semiondas, diodos que conducen en color, bloqueados en gris; el signo más marca la entrada más alta. La corriente por la carga $R$ tiene siempre el mismo sentido. Abajo: entrada $u_\mathrm e$ (gris) y salida $u_\mathrm a$ (azul) para $\hat u=12$ V, $U_\mathrm F=0{,}7$ V.
:::

:::satz Teorema 9.1 (Rectificador en puente)
<span class="anker" id="satz-9-1"></span>

En el modelo con tensión directa, como la corriente siempre recorre dos diodos en serie, se cumple

<span class="anker" id="gl-9-1"></span>
$$u_\mathrm a=\begin{cases}|u_\mathrm e|-2U_\mathrm F&|u_\mathrm e|>2U_\mathrm F\\0&\text{en otro caso.}\end{cases} \tag{9.1}$$

Un diodo bloqueado soporta como máximo $\hat u-U_\mathrm F$.
:::

⁠**Cómo leerlo:** Para $|u_\mathrm e|<2U_\mathrm F$ no conduce ninguna pareja, y $u_\mathrm a$ se queda en cero. En el pico reducido se lee el doble de la tensión directa. **Validez:** carga óhmica. La entrada y la salida no tienen un punto de referencia común.

**Ejemplo.** El pico es $12\,\mathrm{V}-1{,}4\,\mathrm{V}=10{,}6$ V; en el rectificador de media onda, 11,3 V. La pausa dura 0,74 ms por semionda, es decir, el 7,4 % del tiempo. El valor medio es 6,29 V; en el rectificador de media onda, solo 3,48 V. **Casos límite:** Para $U_\mathrm F\to0$, $u_\mathrm a=|u_\mathrm e|$. Para $\hat u<1{,}4$ V la salida se queda en cero.

:::ltspice Rectificador en puente
⁠**Esquema:** fuente con `SINE(0 12 50)` entre `a` y `b`. Diodos DM de `a` a `p`, de `b` a `p`, de masa a `a` y de masa a `b`. `res` 1k de `p` a masa.

⁠**Directiva:** `.tran 40m`

⁠**Lo que ves:** `V(p)` como en la fig. [11](#abb-11), pico 10,57 V, valor medio 6,29 V. La tensión $V(p,a)$ en el diodo bloqueado alcanza 11,28 V. El cálculo da 10,6 V, 6,29 V y 11,3 V. Para el ejercicio [11](#aufg-11), pon 24 en lugar de 12.
:::

:::frage Esto todavía pulsa mucho. ¿Es ya tensión continua?
Todavía no. Un condensador en paralelo con la carga (__filtrado__) se carga hasta el pico y alimenta la carga durante la pausa. En 10 ms pierde $\Delta U=I\,\Delta t/C$ ([Parte 3](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator/der-kondensator.html)). Con $I=10{,}6$ mA y $C=470$ µ F son 0,23 V. Los diodos conducen entonces solo brevemente en el pico.
:::

**Bomba de carga.** Genera a partir de una tensión continua $U_\mathrm e$ otra más alta, sin bobina. Aquí los diodos se consideran ideales (fig. [12](#abb-12)). *Paso 1:* El conmutador conecta la placa inferior de $C_1$ a masa. $C_1$ se carga a través de D$_1$ hasta $U_\mathrm e$. *Paso 2:* El conmutador conecta la placa inferior a $U_\mathrm e$. La tensión en $C_1$ no puede saltar ([Parte 3](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator/der-kondensator.html)), así que la placa superior salta a $2U_\mathrm e$. D$_1$ bloquea porque ahora su cátodo está más alto, D$_2$ conduce y $C_1$ cede carga al condensador de salida $C_2$. Tras unos pocos ciclos, $U_\mathrm a\approx2U_\mathrm e$. En la práctica, pequeñas resistencias limitan los picos de corriente. Con más etapas de bombeo según el mismo esquema, la tensión sigue subiendo.

:::abbildung et1/k9pumpe 12
Bomba de carga; los caminos de corriente de los dos pasos están en color. Izquierda: $U_\mathrm e$ carga el condensador $C_1$. Derecha: $U_\mathrm e$ y la tensión en $C_1$ están en serie y alimentan $C_2$.
:::

:::herleitung Tensión tras $k$ ciclos para $C_1=C_2$
En el primer paso, también $C_2$ se carga a $U_\mathrm e$ a través de los dos diodos. En el paso de bombeo se conectan $C_1$ con $2U_\mathrm e$ y $C_2$ con $U_\mathrm a$. La carga se conserva, y condensadores iguales terminan en el valor medio: $U_\mathrm a'=(2U_\mathrm e+U_\mathrm a)/2$. La distancia al valor final $2U_\mathrm e$ se reduce a la mitad en cada ciclo: $U_\mathrm a(k)=2U_\mathrm e-U_\mathrm e\,2^{-k}$.
:::

Con $U_\mathrm e=5$ V esto da 7,5 V, 8,75 V, 9,38 V, y así hasta 10 V. Con diodos reales se pierde dos veces $U_\mathrm F$: el valor final es $2U_\mathrm e-2U_\mathrm F=8{,}6$ V. **Caso límite:** Si circula corriente en la salida, falta carga en cada ciclo y $U_\mathrm a$ se queda por debajo del valor final.

:::aufgabe Ejercicio 11 ★★ Fuente de alimentación
<span class="anker" id="aufg-11"></span>

Un puente está conectado a $\hat u=24$ V, $U_\mathrm F=0{,}7$ V.

<ol class="al">

<li>

¿Cuánto vale el pico de $u_\mathrm a$? ¿Qué tensión inversa debe soportar cada diodo?

</li>

<li>

¿Durante qué fracción del tiempo es $u_\mathrm a=0$?

</li>

<li>

La carga consume 100 mA. ¿Qué $C$ limita la fluctuación a 1 V? ¿Cuánto debería valer en el rectificador de media onda, y por qué?

</li>

</ol>

:::loesung
(a) $24\,\mathrm{V}-1{,}4\,\mathrm{V}=22{,}6$ V, tensión inversa $24\,\mathrm{V}-0{,}7\,\mathrm{V}=23{,}3$ V. (b) $u_\mathrm a=0$ para $|\sin|<1{,}4/24$, es decir, 3,34° alrededor de cada paso por cero, que son $2\cdot3{,}34^\circ/180^\circ=3{,}7$ % del tiempo. (c) $C=I\,\Delta t/\Delta U=100\,\mathrm{mA}\cdot10\,\mathrm{ms}/1\,\mathrm{V}=1000$ µ F. En el rectificador de media onda, la reposición llega solo cada 20 ms, así que 2000 µ F.
:::
:::

:::aufgabe Ejercicio 12 ★★ Contar bombeos
<span class="anker" id="aufg-12"></span>

$U_\mathrm e=3$ V, $C_1=C_2$, diodos ideales.

<ol class="al">

<li>

¿Cuánto vale $U_\mathrm a$ tras 1, 2 y 3 ciclos?

</li>

<li>

¿Tras cuántos ciclos se alcanza el 99 % del valor final?

</li>

<li>

¿Qué valor final dan diodos reales con 0,7 V? ¿Qué queda con $U_\mathrm e=1{,}5$ V, y qué se deduce de ello para los circuitos de baja tensión?

</li>

</ol>

:::loesung
(a) $U_\mathrm a(k)=6\,\mathrm{V}-3\,\mathrm{V}\cdot2^{-k}$: 4,5 V, 5,25 V, 5,63 V. (b) $3\,\mathrm{V}\cdot2^{-k}\le0{,}06\,\mathrm{V}$ exige $2^k\ge50$, así que $k=6$. (c) $6\,\mathrm{V}-1{,}4\,\mathrm{V}=4{,}6$ V. Con 1,5 V quedan $3\,\mathrm{V}-1{,}4\,\mathrm{V}=1{,}6$ V, apenas más que la entrada. Por eso, con tensiones bajas los diodos se sustituyen por interruptores.
:::
:::

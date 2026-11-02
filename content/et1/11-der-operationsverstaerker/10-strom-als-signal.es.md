---
title: Etapa 8: La corriente como señal
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / El amplificador operacional
order: 1211000
summary: Hasta ahora, la señal era la tensión.
tags: amplificador de transimpedancia, resistencia diferencial, convertidor de impedancia negativa
lang: es
---

<span class="anker" id="stufe-8"></span>

:::zweck
Hasta ahora, la señal era la tensión. Pero muchas fuentes entregan una corriente. Esta etapa convierte corriente en tensión y muestra que el AO puede imitar una resistencia negativa.
:::

**Corriente en tensión.** Un fotodiodo entrega una corriente que apenas depende de su tensión. En el __amplificador de transimpedancia__ circula directamente hacia la masa virtual y tiene que pasar por $R$ (fig. [10](#abb-10), izquierda):

<span class="anker" id="gl-8-1"></span>
$$U_\mathrm{A}=-R\,I_\mathrm{E},\qquad r_\mathrm{ent}=\frac{\Delta U_-}{\Delta I_\mathrm{E}}=\frac{R}{1+A}. \tag{8.1}$$

Con $R=1$ M$\Omega$, 2 µ A se convierten en $-2$ V. El nudo se mueve solo $2\,\mathrm{V}/A=20$ µ V. Esa es la pequeña resistencia de entrada de 10 $\Omega$, un valor para cambios (__resistencia diferencial__). La fuente ve casi un cortocircuito, y su resistencia interna no importa.

**Una resistencia negativa.** Con tensión positiva, una resistencia toma corriente en el sentido de la flecha de referencia (convenio receptor, [Parte 2](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)). El __convertidor de impedancia negativa__ (NIC) empuja en cambio corriente hacia fuera (fig. [10](#abb-10), derecha). El terminal 1 está en la entrada positiva, y desde allí una $R$ lleva a la salida. Desde la salida, una $R$ igual lleva a la entrada negativa, y desde allí $R_2$ a masa. De $\varphi_+=\varphi_-$ se sigue $U_1=U_2$.

:::satz Teorema 8.1 (NIC)
<span class="anker" id="satz-8-1"></span>

<span class="anker" id="gl-8-2"></span>
$$R_\mathrm{ent}=\frac{U_1}{I_1}=-R_2. \tag{8.2}$$

La regla solo vale mientras la resistencia $R_\mathrm{i}$ que actúa en el terminal 1 respecto a masa sea menor que $R_2$.
:::

⁠**Cómo leerlo:** $I_1$ se cuenta hacia el terminal 1; $U_1$, respecto a masa. $U_2$ e $I_2$ pertenecen a $R_2$. $R_\mathrm{i}$ es todo lo que está conectado por fuera al terminal 1, por ejemplo fuente y carga en paralelo. **Validez:** $U_\mathrm{A}=U_1(1+R/R_2)$ debe estar dentro de los límites.

:::herleitung Por qué cambia el signo y cuándo vale la regla
Por $R_2$ circula $I_2=U_2/R_2$, y no entra corriente en la entrada, así que también circula por la $R$ inferior: la salida está en $U_\mathrm{A}=U_2+R\,I_2$. La $R$ superior tiene la misma tensión y conduce la misma corriente, de la salida al terminal 1. Por tanto, $I_1=-I_2$ y $R_\mathrm{ent}=U_1/I_1=-R_2$.

Aquí hay dos realimentaciones: la $R$ inferior da realimentación negativa; la izquierda, positiva. Si cambia $U_\mathrm{A}$, $\varphi_-$ cambia en la fracción $\beta_-=R_2/(R_2+R)$ y $\varphi_+$ en $\beta_+=R_\mathrm{i}/(R_\mathrm{i}+R)$. Solo para $\beta_->\beta_+$ predomina la realimentación negativa, es decir, para $R_\mathrm{i}<R_2$.
:::

:::abbildung et1/k11nic 10
A la izquierda, el amplificador de transimpedancia con una fuente de corriente como entrada. A la derecha, el NIC con $R=10$ k$\Omega$ y $R_2=5$ k$\Omega$ con 1 V en el terminal 1: la salida está en 3 V y empuja 0,2 mA hacia fuera del terminal.
:::

**Ejemplo.** Con $R=10$ k$\Omega$, $R_2=5$ k$\Omega$ y $U_1=1$ V son $I_2=0{,}2$ mA, $U_\mathrm{A}=3$ V, $I_1=-0{,}2$ mA, es decir, $R_\mathrm{ent}=-5$ k$\Omega$. La energía viene de la alimentación del AO. *Aplicación:* Una fuente de corriente de 1 mA con resistencia interna $R_\mathrm{q}=10$ k$\Omega$ entrega a 1 k$\Omega$ solo 0,909 mA, porque una parte pasa por $R_\mathrm{q}$. En paralelo, un NIC con $R_2=R_\mathrm{q}$: la conductancia $1/R_\mathrm{q}-1/R_2$ se anula, y la carga recibe 1 mA. La fuente real actúa como una ideal. El NIC entrega exactamente los 0,1 mA que deriva $R_\mathrm{q}$. **Caso límite:** Sin carga, $R_\mathrm{i}=R_\mathrm{q}=R_2$, ambas realimentaciones son igual de fuertes, la ganancia de lazo es cero y la regla deja de valer.

:::aufgabe Ejercicio 9 ★★★ Compensar una fuente de corriente
<span class="anker" id="aufg-9"></span>

Un NIC con $R=10$ k$\Omega$ y $R_2=4{,}7$ k$\Omega$ está en paralelo con una fuente de 2 mA y $R_\mathrm{q}=4{,}7$ k$\Omega$. La carga es de 1 k$\Omega$. (a) ¿Qué corriente recibe la carga sin NIC y cuál con NIC? (b) ¿Dónde está la salida del AO? (c) ¿Hasta qué resistencia de carga bastan los 11 V de la salida? (d) ¿Por qué el circuito es estable con carga, pero no sin ella?

:::loesung
(a) Sin NIC, $2\,\mathrm{mA}\cdot4{,}7/5{,}7=1{,}65$ mA; con NIC, 2 mA. (b) $U_1=2$ V, $I_2=0{,}426$ mA, $U_\mathrm{A}=2\,\mathrm{V}+10\,\mathrm{k\Omega}\cdot0{,}426\,\mathrm{mA}=6{,}26$ V. (c) $U_\mathrm{A}=U_1(1+R/R_2)=3{,}13\,U_1\le11$ V da $U_1\le3{,}52$ V, es decir, $R_\mathrm{L}\le1{,}76$ k$\Omega$. (d) Con carga, $R_\mathrm{i}=R_\mathrm{q}\parallel1\,\mathrm{k\Omega}=825\,\Omega<R_2$, y predomina la realimentación negativa. Sin carga, $R_\mathrm{i}=R_2$, y las dos realimentaciones se anulan.
:::
:::

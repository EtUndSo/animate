---
title: Visión general: El amplificador operacional
kurz: Visión general
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / El amplificador operacional
order: 1210100
summary: Cómo un factor enorme e impreciso se convierte en un componente cuyo comportamiento solo depende de las resistencias
tags: amplificador operacional, ganancia en lazo abierto, realimentación negativa
lang: es
---

## De qué trata

Un __amplificador operacional__, abreviado AO, es un amplificador integrado formado por unas cuantas decenas de transistores. Amplifica la tensión entre sus dos entradas unas 100000 veces. Este factor se llama __ganancia en lazo abierto__. Varía en un factor de cuatro de un ejemplar a otro y cambia con la temperatura. Aun así, con este componente se construyen amplificadores que solo notan un 0,01 % de esa variación, además de sumadores e integradores. La pregunta es: *¿Cómo un factor enorme e impreciso se convierte en un componente cuyo comportamiento solo depende de las resistencias?* La respuesta es la __realimentación negativa__: una parte de la tensión de salida se devuelve a la entrada de modo que actúa contra su propia causa.



**Cómo trabajar con este capítulo.** Cada etapa es un artículo breve con la idea, preguntas típicas desplegables y ejercicios (de ★ a ★★★). Intenta resolverlos primero por tu cuenta; la solución se despliega justo debajo de cada ejercicio. Termina una etapa antes de pasar a la siguiente.

:::merke El modelo de referencia de este capítulo
<ul>

<li>

⁠**AO V:** Ganancia en lazo abierto $A=100000$ (ejemplares de 50000 a 200000), resistencia de entrada $r_\mathrm{e}=1$ M$\Omega$, resistencia de salida $r_\mathrm{a}=75\,\Omega$. Alimentación $\pm12$ V; la salida alcanza $\pm11$ V y como máximo 20 mA. Para la etapa [10](wo-die-regeln-enden.html#stufe-10): frecuencia de transición $f_\mathrm{T}=1$ MHz (allí $A$ ha caído a 1), offset $U_\mathrm{off}=1$ mV (diferencia residual de las entradas), corriente de polarización de entrada $I_\mathrm{B}=50$ nA (corriente de base de los transistores de entrada), rechazo de modo común 90 dB (atenuación de perturbaciones comunes).

</li>

<li>

⁠**Circuito externo:** $R_1=10$ k$\Omega$, $R_2=40$ k$\Omega$, $U_\mathrm{E}=1$ V.

</li>

<li>

⁠**Etapa diferencial:** transistores T de la [Parte 10](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor/der-bipolartransistor.html) ($B=200$, $U_T=26$ mV), $I_0=2$ mA, $R_\mathrm{C}=3$ k$\Omega$.

</li>

<li>

⁠**Sensor:** 1 mV eficaz, resistencia interna 10 k$\Omega$, ancho de banda (el rango de frecuencias que deja pasar) 20 kHz, temperatura 300 K.

</li>

</ul>

El script `rechnung_kap11.py` comprueba todos los números.
:::

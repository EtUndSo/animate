---
title: Visión general: Semiconductores y diodos
kurz: Visión general
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / Semiconductores y diodos
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden
knoten: Capítulo 9: Semiconductores y diodos
order: 1190100
summary: Cómo el silicio se convierte en una válvula para la corriente y cómo se calcula con ella
tags: diodo, semiconductor, Dopado, portadores de carga, unión pn, zona de carga espacial, curva característica, punto de trabajo
lang: es
---

## De qué trata

Un cargador convierte la tensión alterna de la toma de corriente en la tensión continua para la batería recargable. El componente que lo hace se llama __diodo__: deja pasar la corriente en un sentido (sentido directo) y la bloquea en el otro (sentido inverso). Consiste en un __semiconductor__, un material cuya conductividad está entre la de un metal y la de un aislante y se puede ajustar a voluntad. La pregunta de este capítulo es: *¿Cómo se convierte un trozo de silicio en una válvula para la corriente, y cómo se calcula con un componente que no obedece la ley de Ohm?*

La respuesta pasa por seis conceptos. __Dopado__ significa introducir unos pocos átomos de impureza y fijar así cuántos __portadores de carga__ (cargas móviles) tiene el cristal. En el límite entre dos regiones dopadas de forma distinta, la __unión pn__, se forma por sí sola la __zona de carga espacial__, una capa delgada sin cargas móviles que actúa como barrera de energía. La __curva característica__ es la gráfica de la corriente frente a la tensión, y el __punto de trabajo__ es el par de tensión y corriente que se establece en un circuito.



**Cómo trabajar con este capítulo.** Las secciones se apoyan unas en otras y cada término nuevo tiene su propia subsección con un ejemplo. Los recuadros desplegables contienen el contexto (por qué algo es así y de dónde viene), deducciones e indicaciones para la simulación; no hacen falta para seguir leyendo. Intenta primero los ejercicios (de ★ a ★★★) por tu cuenta; la solución se despliega justo debajo de cada ejercicio.

:::merke El modelo de referencia de este capítulo
<ul>

<li>

⁠**Diodo:** silicio, corriente inversa de saturación $I_\mathrm S=10^{-14}$ A (la pequeña corriente en sentido inverso), tensión térmica $U_T=25{,}85$ mV (energía térmica por carga) a $T=300$ K (27 °C). En el modelo de interruptor rige la tensión directa $U_\mathrm F=0{,}7$ V (tensión en el diodo en conducción).

</li>

<li>

⁠**Unión pn:** $10^{16}$ átomos de impureza por cm$^3$ en cada lado, $n_\mathrm i=10^{10}\,\mathrm{cm^{-3}}$ electrones libres en silicio puro, permitividad relativa $\varepsilon_\mathrm r=11{,}7$.

</li>

<li>

⁠**Circuito:** fuente $U_0=5$ V, resistencia $R=1\,\mathrm{k\Omega}$, diodo en serie.

</li>

<li>

⁠**Rectificador:** tensión senoidal con valor de pico de 12 V y 50 Hz, carga 1 k$\Omega$.

</li>

<li>

⁠**Constantes:** $e=1{,}602\cdot10^{-19}$ C, $k_\mathrm B=1{,}3806\cdot10^{-23}$ J/K. El script `rechnung_kap9.py` comprueba todos los números.

</li>

</ul>
:::

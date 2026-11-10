---
title: Visión general: Carga, campo y potencial
kurz: Visión general
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / Carga, campo y potencial
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial
knoten: Capítulo 1: Carga, campo y potencial
order: 1110100
summary: Por qué la tensión es una diferencia y qué hace con una carga
tags: tensión, carga, campo eléctrico, potencial, punto de referencia, resistencia
lang: es
---

## De qué trata

En una batería rectangular pone 9 V. Este dato es una __tensión__. No dice cuánta energía contiene la batería, sino cuánta energía cede cada unidad de __carga__ que pasa de un terminal al otro: 9 julios por culombio. La carga es la propiedad de ciertas partículas de ejercer y sentir fuerzas eléctricas. El julio es la unidad de energía; el culombio, la unidad de carga. La pregunta de este capítulo es: *¿Por qué la tensión es siempre una diferencia entre dos puntos, y qué hace con una carga?*

La respuesta pasa por dos conceptos. Un __campo eléctrico__ determina para cada lugar qué fuerza actúa allí sobre una carga. El __potencial__ determina para cada lugar cuánta energía por culombio tiene allí una carga respecto a un cero elegido libremente, el __punto de referencia__.



**Cómo trabajar con este capítulo.** Las secciones se apoyan unas en otras y cada término nuevo tiene su propia subsección con un ejemplo. Los recuadros desplegables contienen el contexto (por qué algo es así y de dónde viene), deducciones e indicaciones para la simulación; no hacen falta para seguir leyendo. Intenta primero los ejercicios (de ★ a ★★★) por tu cuenta; la solución se despliega justo debajo de cada ejercicio.

:::merke El modelo de referencia de este capítulo
<ul>

<li>

⁠**Par de placas:** dos placas metálicas planas A y B en el vacío (espacio sin aire), separadas $d=3$ mm, distancia pequeña frente a la anchura de las placas. Una batería de 9 V está conectada con el polo positivo a A y con el polo negativo a B. El eje $x$ va de A ($x=0$) a B. Entre las placas hay el campo uniforme $E=3$ kV/m (etapas [5](feldlinien-und-leiter.html#stufe-5) y [8](spannung-und-masse.html#stufe-8)).

</li>

<li>

⁠**Dos esferas:** esferas pequeñas con $Q_\mathrm{A}=+10$ nC y $Q_\mathrm{B}=-20$ nC a la distancia $r=3$ cm. La esfera A tiene una masa de 1 g.

</li>

<li>

⁠**Circuito:** la misma batería conectada a dos resistencias en serie, 6 V en la primera y 3 V en la segunda. Una __resistencia__ es un componente en el que la carga que lo atraviesa cede energía en forma de calor ([capítulo 2](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)).

</li>

<li>

⁠**Constantes:** $e=1{,}602\cdot10^{-19}$ C, $m_\mathrm{e}=9{,}109\cdot10^{-31}$ kg, $k=8{,}99\cdot10^{9}\,\mathrm{N\,m^2/C^2}$, $g=9{,}81\,\mathrm{m/s^2}$; las etapas las explican. El script `rechnung_kap1.py` comprueba todos los números.

</li>

</ul>
:::

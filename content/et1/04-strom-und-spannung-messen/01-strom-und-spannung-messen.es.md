---
title: Visión general: Medir corriente y tensión
kurz: Visión general
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / Medir corriente y tensión
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-und-spannung-messen
knoten: Capítulo 4: Medir corriente y tensión
order: 1140100
summary: Por qué todo instrumento modifica el circuito y cómo medir con exactitud a pesar de ello
tags: resistencia interna, mecanismo de medida, rango de medida
lang: es
---

## De qué trata

En un divisor de tensión debería haber 3 V, y el instrumento muestra 2,73 V. El divisor está bien y la lectura es correcta: muestra la tensión presente desde que se conectó el instrumento. Y es que un instrumento de medida es un componente con una __resistencia interna__, la resistencia entre sus terminales. La pregunta es: *¿Por qué todo instrumento modifica el circuito que mide, qué tamaño tiene el error y por qué un puente mide con más exactitud que un instrumento por sí solo?*



**Cómo trabajar con este capítulo.** Las secciones se apoyan unas en otras y cada término nuevo tiene su propia subsección con un ejemplo. Los recuadros desplegables contienen el contexto (por qué algo es así y de dónde viene), deducciones e indicaciones para la simulación; no hacen falta para seguir leyendo. Intenta primero los ejercicios (de ★ a ★★★) por tu cuenta; la solución se despliega justo debajo de cada ejercicio.

:::merke El modelo de referencia de este capítulo
<ul>

<li>

⁠**Instrumento:** un __mecanismo de medida__ (la parte del aparato que convierte la corriente en una desviación de la aguja) con desviación a fondo de escala para $I_\mathrm M=50$ µ A y resistencia propia $R_\mathrm M=2$ k$\Omega$. Como amperímetro en el __rango de medida__ (intervalo de valores que puede mostrar) hasta 10 mA tiene $R_\mathrm{iA}=10\,\Omega$; como voltímetro en el rango hasta 10 V tiene $R_\mathrm{iV}=200$ k$\Omega$ (etapa [2](den-messbereich-erweitern.html#stufe-2)). Su lectura se desvía como máximo un 1 % del valor de fondo de escala.

</li>

<li>

⁠**Objeto medido:** $R=1{,}8$ k$\Omega$ conectada a una fuente de tensión ideal $U=9$ V (mantiene 9 V con cualquier corriente). Sin instrumento circulan 5 mA.

</li>

<li>

⁠**Divisor:** $R_1=60$ k$\Omega$ y $R_2=30$ k$\Omega$ en serie a 9 V; en $R_2$ hay 3 V.

</li>

<li>

⁠**Puente:** $R_1=1$ k$\Omega$, $R_2=1{,}8$ k$\Omega$, $R_3=1$ k$\Omega$ a 9 V; se busca $R_4$. Para cambios pequeños, cuatro resistencias de 350 $\Omega$ cada una a 9 V.

</li>

</ul>

El script `rechnung_kap4.py` recalcula todos los números.
:::

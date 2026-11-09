---
title: Visión general: Fuentes y fuentes equivalentes
kurz: Visión general
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / Fuentes y fuentes equivalentes
order: 1150100
summary: Por qué dos números sustituyen a toda una red
tags: 
lang: es
---

## De qué trata

Un sensor cuelga de dos cables, y detrás hay un circuito con decenas de componentes. Solo percibe la tensión y la corriente en sus terminales. La pregunta de este capítulo es: *¿Cuántos números hacen falta para describir toda una red en dos terminales?* La respuesta es dos, siempre que la red sea lineal: contiene solo resistencias y fuentes fijas, y el doble de causa da el doble de efecto.

El camino tiene tres partes. Las etapas [1](widerstande-zusammenfassen.html#stufe-1) a [3](stern-und-dreieck.html#stufe-3) reducen redes sin fuente. Las etapas [4](ideale-quellen.html#stufe-4) a [7](quellen-zusammenschalten.html#stufe-7) introducen las fuentes y muestran que también ellas son rectas. Las etapas [8](uberlagerung.html#stufe-8) y [9](thevenin-und-norton.html#stufe-9) demuestran que esto vale para toda red lineal, y la etapa [10](der-r-2r-wandler.html#stufe-10) lo aprovecha en un convertidor.



**Cómo trabajar con este capítulo.** Las secciones se apoyan unas en otras y cada término nuevo tiene su propia subsección con un ejemplo. Los recuadros desplegables contienen el contexto (por qué algo es así y de dónde viene), deducciones e indicaciones para la simulación; no hacen falta para seguir leyendo. Intenta primero los ejercicios (de ★ a ★★★) por tu cuenta; la solución se despliega justo debajo de cada ejercicio.

:::merke El modelo de referencia de este capítulo
<ul>

<li>

⁠**Batería:** la batería de 9 V de la [Parte 1](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html). Su tensión de fuente (la tensión que aporta la química) es $U_\mathrm{q}=9$ V; su resistencia interna, $R_\mathrm{q}=2\,\Omega$.

</li>

<li>

⁠**Carga:** el aparato conectado, con la resistencia $R_\mathrm{L}=16\,\Omega$. Las etapas [1](widerstande-zusammenfassen.html#stufe-1) a [3](stern-und-dreieck.html#stufe-3) construyen redes de carga con muchas resistencias, todas las cuales dan exactamente 16 $\Omega$.

</li>

<li>

⁠**Red N:** dos fuentes y dos resistencias (fig. [9](uberlagerung.html#abb-9)): $U_\mathrm{q1}=18$ V, $R_1=6\,\Omega$, $R_2=3\,\Omega$, $I_\mathrm{q2}=1{,}5$ A. La etapa [9](thevenin-und-norton.html#stufe-9) muestra que desde fuera N no se distingue de la batería.

</li>

</ul>

El script `rechnung_kap5.py` comprueba todos los números.
:::

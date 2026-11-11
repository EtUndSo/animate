---
title: Visión general: Sistemas paso bajo y paso banda
kurz: Visión general
pfad: Ingeniería eléctrica / 3.er semestre / ET3 – Fundamentos de ingeniería eléctrica 3: señales y sistemas / Sistemas paso bajo y paso banda
adresse: elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme
knoten: Capítulo 5: Sistemas paso bajo y paso banda
order: 3250100
summary: Transmisión sin distorsión, paso bajo ideal, envolvente compleja y retardo de grupo
tags: 
lang: es
---

## De qué trata

Casi toda transmisión debe hacer llegar una señal lo más inalterada posible, pero solo en un determinado rango de frecuencias: un paso bajo deja pasar las frecuencias bajas; un paso banda, una banda en torno a una frecuencia portadora. Este capítulo se pregunta: *¿qué significa exactamente «inalterada», qué precio tiene una banda limitada de forma abrupta y cómo se calcula con señales que van montadas sobre una portadora de alta frecuencia?*

**Cómo trabajar con este capítulo.** Las secciones se apoyan unas en otras y cada término nuevo tiene su propia subsección con un ejemplo. Los recuadros desplegables contienen el contexto (por qué algo es así y de dónde viene), deducciones e indicaciones para la simulación; no hacen falta para seguir leyendo. Intenta primero los ejercicios (de ★ a ★★★) por tu cuenta; la solución se despliega justo debajo de cada ejercicio.

:::merke El modelo de referencia de este capítulo
<ul>

<li>

⁠**Paso bajo RC** con $RC=1$ s, como en los [capítulos 1](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html) a 3.

</li>

<li>

⁠**Paso bajo ideal** con $f_\mathrm g=1$ Hz (para comparar, también 2 Hz).

</li>

<li>

⁠**Paso banda ideal** con la frecuencia central $f_0=10$ Hz y el ancho de banda $\Delta f=2$ Hz.

</li>

<li>

⁠**Paso bajo en tiempo discreto** con $f_\mathrm g=0{,}2$ (normalizada a la frecuencia de muestreo) y 21 coeficientes.

</li>

</ul>

$\operatorname{si}(x)=\sin(x)/x$, como en el [capítulo 3](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html).
:::

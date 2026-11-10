---
title: Visión general: Muestreo y sistemas en tiempo discreto
kurz: Visión general
pfad: Ingeniería eléctrica / 3.er semestre / ET3 – Fundamentos de ingeniería eléctrica 3: señales y sistemas / Muestreo y sistemas en tiempo discreto
adresse: elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme
knoten: Capítulo 4: Muestreo y sistemas en tiempo discreto
order: 3240100
summary: De la señal continua a la secuencia de números: teorema de muestreo, convolución discreta, DFT, FFT y transformada z
tags: muestras
lang: es
---

## De qué trata

Un ordenador no puede almacenar una función $s(t)$, solo una secuencia de números. Por eso se mide la señal con un periodo de muestreo fijo $T$ y se trabaja con las __muestras__ $s(nT)$. Dos preguntas guían este capítulo: *¿Se pierde información en el proceso?* Y: *¿cómo se calcula con secuencias de números del mismo modo en que los [capítulos 1](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html) a 3 calculaban con funciones?*



**Cómo trabajar con este capítulo.** Las secciones se apoyan unas en otras y cada término nuevo tiene su propia subsección con un ejemplo. Los recuadros desplegables contienen el contexto (por qué algo es así y de dónde viene), deducciones e indicaciones para la simulación; no hacen falta para seguir leyendo. Intenta primero los ejercicios (de ★ a ★★★) por tu cuenta; la solución se despliega justo debajo de cada ejercicio.

:::merke El modelo de referencia de este capítulo
<ul>

<li>

⁠**Frecuencia de muestreo** $f_\mathrm A=1/T=1$ kHz ($T=1$ ms). Señales de prueba: oscilaciones cosenoidales de 300 Hz y de 700 Hz.

</li>

<li>

En las secuencias, la frecuencia se normaliza a la frecuencia de muestreo: $f=1$ corresponde a $f_\mathrm A$. Con $f_\mathrm A=1$ kHz, $f=0{,}3$ significa, por tanto, 300 Hz.

</li>

<li>

⁠**Sistema recursivo** $g(n)=s(n)+0{,}6\,g(n-1)$.

</li>

<li>

⁠**Ejemplo de DFT** $s_d=(1,\,2,\,0,\,-1)$.

</li>

</ul>

El script `rechnung_kap4.py` recalcula los números y las curvas.
:::

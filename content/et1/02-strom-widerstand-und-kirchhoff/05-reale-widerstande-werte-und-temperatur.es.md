---
title: Etapa 4: Resistencias reales: valores y temperatura
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / Corriente, resistencia y leyes de Kirchhoff
order: 1120500
summary: Hasta ahora, R era un número dado por el material y la forma.
tags: resistencias de película metálica o de carbón, resistencias bobinadas, SMD, serie E, coeficiente de temperatura, PTC, conductor en frío, NTC
lang: es
---

<span class="anker" id="stufe-4"></span>

:::zweck
Hasta ahora, $R$ era un número dado por el material y la forma. Un componente comprado tiene un valor normalizado y una tolerancia, y su resistencia cambia con la temperatura.
:::

**La idea.** La fabricación se dispersa en un porcentaje. Por eso, los valores ofrecidos están escalonados de modo que valores consecutivos tengan la misma separación *porcentual*. En cuanto a la temperatura, decide $\sigma=n\,e\,\mu$: el calor cambia o bien la movilidad $\mu$ o bien la densidad de portadores de carga $n$.

**Tipos constructivos.** Las __resistencias de película metálica o de carbón__ llevan una capa fina sobre un cuerpo cerámico; es la forma habitual para 0,1 a 2 W, y el valor figura en ellas como código de colores. Las __resistencias bobinadas__ soportan mucha potencia y temperatura y son adecuadas para valores pequeños. Las resistencias __SMD__ (Surface Mounted Device) se sueldan directamente sobre la placa de circuito impreso. Son muy pequeñas, permiten una alta densidad de montaje, toleran poca potencia y, al no tener hilos de conexión, son adecuadas para altas frecuencias.

:::definition Definición 4.1 (Serie E)
<span class="anker" id="satz-4-1"></span>

Una __serie E__ E$N$ contiene $N$ valores por década; según DIN IEC 60063 existen E3, E6, E12, E24, E48, E96 y E192:

<span class="anker" id="gl-4-1"></span>
$$w=\bigl(\sqrt[N]{10}\,\bigr)^{i}=\sqrt[N]{10^{i}},\qquad i=0,1,\dots,N-1. \tag{4.1}$$
:::

⁠**Cómo leerlo:** $w$ es el factor; la década (potencia de diez) se elige libremente. El paso es un factor fijo; en E12, $\sqrt[12]{10}=1{,}21$. Los valores normalizados están redondeados: 1,0; 1,2; 1,5; 1,8; 2,2; 2,7; 3,3; 3,9; 4,7; 5,6; 6,8; 8,2. Algunos se desvían un poco de [(4.1)](#gl-4-1) por razones históricas, por ejemplo 2,7 en lugar de 2,61. ¿Por qué este factor? E12 corresponde a la tolerancia $\pm10\,\%$: los intervalos de valores vecinos se unen entonces sin huecos, y cada pieza fabricada corresponde a un valor normalizado. Del mismo modo, E6 corresponde a $\pm20\,\%$ y E24 a $\pm5\,\%$.

**Código de colores.** Las resistencias con hilos de conexión suelen llevar cuatro anillos: dos cifras, el multiplicador $10^x$ y la tolerancia. Las cifras son negro 0, marrón 1, rojo 2, naranja 3, amarillo 4, verde 5, azul 6, violeta 7, gris 8, blanco 9. Como multiplicador se añaden oro $10^{-1}$ y plata $10^{-2}$. La tolerancia es marrón 1 %, rojo 2 %, verde 0,5 %, azul 0,25 %, violeta 0,1 %, oro 5 %, plata 10 %. Amarillo, violeta, rojo, oro significa $47\cdot10^2\,\Omega=4{,}7\,\mathrm{k\Omega}$ con $\pm5\,\%$, es decir, de 4,47 a 4,94 k$\Omega$. $R_1$ de la cadena lleva rojo, negro, rojo, oro.

:::satz Teorema 4.2 (Dependencia de la temperatura)
<span class="anker" id="satz-4-2"></span>

Cerca de una temperatura de referencia $\vartheta_0$ se cumple

<span class="anker" id="gl-4-2"></span>
$$R(\vartheta)=R(\vartheta_0)\,\bigl(1+\alpha_{\vartheta_0}\,(\vartheta-\vartheta_0)\bigr). \tag{4.2}$$
:::

⁠**Cómo leerlo:** $\vartheta$ es la temperatura en °C, en las hojas de datos normalmente $\vartheta_0=20$ °C. El __coeficiente de temperatura__ $\alpha$ tiene la unidad 1/K: cobre $3{,}9\cdot10^{-3}$, wolframio $4{,}5\cdot10^{-3}$, carbón $-0{,}5\cdot10^{-3}$, constantán unos $10^{-5}$. Para $\alpha>0$, el material se llama __PTC__ (positive temperature coefficient) o __conductor en frío__: conduce mejor en frío. Para $\alpha<0$, se llama __NTC__ (negative temperature coefficient) o __conductor en caliente__. **Validez:** [(4.2)](#gl-4-2) es la tangente a la curva real. En los metales abarca mucho, en los semiconductores solo unos pocos kelvin (fig. [5](#abb-5), izquierda).

:::abbildung et1/k2temperatur 5
Izquierda: $R/R_{20}$ frente a la temperatura para el cobre ($\alpha=3{,}9\cdot10^{-3}$ /K), la aleación compensada constantán y un conductor en caliente semiconductor (unos $-4\,\%$/K a 20 °C). Derecha: curva característica modelo de una lámpara incandescente de 9 V. En frío tiene $1{,}5\,\Omega$; en funcionamiento, con 0,5 A, tiene $18\,\Omega$. La curva pasa de una a otra de las dos rectas discontinuas.
:::

**Mecanismo.** Metales (cobre, plata, platino, wolframio): $n$ es fijo, una red cristalina más caliente vibra con más fuerza, el tiempo de vuelo $T$ baja, $\mu$ baja, $R$ sube. Semiconductores (silicio, germanio): a temperatura ambiente solo unos pocos electrones están libres. El calor libera más ([Parte 9](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden/halbleiter-und-dioden.html)), $n$ crece mucho más deprisa de lo que cae $\mu$, $R$ baja. __Aleaciones compensadas__ como el constantán: predominan las colisiones con los átomos extraños incorporados irregularmente, que apenas dependen de la temperatura. Como alternativa se conectan en serie una PTC y una NTC, de modo que el aumento de una compense la disminución de la otra ($R_1\alpha_1+R_2\alpha_2=0$).

::::beispiel
El hilo se calienta de 20 °C a 70 °C. De [(4.2)](#gl-4-2) se obtiene el factor $1+3{,}9\cdot10^{-3}\cdot50=1{,}195$, es decir, 40,6 m$\Omega$ en lugar de 34 m$\Omega$. Un caso extremo es el filamento de wolframio de la lámpara: el factor 12 de $1{,}5\,\Omega$ a $18\,\Omega$ corresponde según [(4.2)](#gl-4-2) a unos 2460 °C, como aproximación burda en este amplio intervalo.
::::

⁠**Casos límite:** $\vartheta=\vartheta_0$ da $R(\vartheta_0)$; $\alpha=0$ da un valor constante.

:::frage ¿Por qué las lámparas incandescentes suelen fundirse al encenderlas?
En frío, el filamento solo tiene $1{,}5\,\Omega$; con 9 V circulan en el primer momento 6 A en lugar de 0,5 A. Este impulso calienta el filamento en fracciones de segundo. Su resistencia sube, lo que reduce la corriente, hasta llegar a $18\,\Omega$. En los puntos delgados el calentamiento es mayor, y allí se rompe el filamento.
:::

:::aufgabe Ejercicio 4 ★★ Valores normalizados y temperatura
<span class="anker" id="aufg-4"></span>

<ol class="al">

<li>

Una resistencia lleva azul, gris, rojo, oro. ¿Cuáles son su valor y su intervalo?

</li>

<li>

Calcula el factor de paso de E24. ¿Qué tolerancia hace que los intervalos vecinos justo se toquen?

</li>

<li>

Una bobina de cobre tiene exactamente $10\,\Omega$ a 20 °C y $12\,\Omega$ en caliente. ¿A qué temperatura está?

</li>

<li>

Una resistencia de cobre de $100\,\Omega$ debe hacerse independiente de la temperatura con carbón en serie. ¿Qué valor necesita el carbón?

</li>

</ol>

:::loesung
(a) Azul 6, gris 8, rojo $10^2$, oro $\pm5\,\%$: $6{,}8\,\mathrm{k\Omega}$, intervalo de 6,46 a 7,14 k$\Omega$.

(b) $\sqrt[24]{10}=1{,}10$. De $(1+t)/(1-t)=1{,}10$ se obtiene $t=4{,}8\,\%$, redondeado $\pm5\,\%$.

(c) $\vartheta=20\text{\,°C}+(12/10-1)/(3{,}9\cdot10^{-3}\,\mathrm{K^{-1}})=71$ °C.

(d) $R_\mathrm{Cu}\,\alpha_\mathrm{Cu}+R_\mathrm C\,\alpha_\mathrm C=0$: $R_\mathrm C=100\,\Omega\cdot3{,}9/0{,}5=780\,\Omega$.
:::
:::

---
title: Etapa 1: Por qué entra corriente en un aislante
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / El condensador
order: 1130200
summary: Las placas no se tocan.
tags: 
lang: es
---

<span class="anker" id="stufe-1"></span>

:::zweck
Las placas no se tocan. Aun así, un instrumento de medida en el cable de conexión indica corriente. Esta etapa aclara qué carga se mueve y hacia dónde.
:::

**La idea.** El par de placas sin carga se conecta a la batería con cables (fig. [1](#abb-1)). En el primer instante, ambas placas están al mismo potencial, pero los polos de la batería distan 9 V entre sí. La caída de potencial está, por tanto, a lo largo de los cables. Allí hay un campo, y este empuja a los electrones libres del metal. En el cable de la placa A corren alejándose de la placa hacia el polo positivo; en el cable de la placa B, del polo negativo hacia la placa. A pierde electrones y se vuelve positiva; B gana electrones y se vuelve negativa. Ningún electrón cruza el hueco: cada electrón que llega a B procede del cable que la precede, no de A.

Con cada carga desplazada crece el campo entre las placas y, con él, la tensión. Las placas se acercan al potencial de sus polos, la caída a lo largo de los cables se reduce y la corriente disminuye. Con 9 V entre las placas, cada placa está al potencial de su polo. A lo largo de los cables no queda ninguna caída, sobre los electrones ya no actúa ninguna fuerza y la corriente termina.

:::abbildung et1/k3aufbau 1
Izquierda: el par de placas durante la carga. Los electrones corren de la placa A al polo positivo, y otros tantos del polo negativo a la placa B. La corriente $i$ se cuenta en el sentido de la carga positiva, es decir, contra los electrones, y es igual en ambos cables de conexión. Por el aislante no pasa carga; allí está el campo $E$. Derecha: el símbolo con flechas de referencia.
:::

:::definition Definición 1.1 (Condensador)
<span class="anker" id="satz-1-1"></span>

Un condensador consta de dos electrodos separados por un dieléctrico. Su carga $Q$ es la carga del electrodo positivo; el otro lleva $-Q$. Corriente a través del condensador significa: por un terminal entra una corriente y, en el mismo instante, por el otro sale la misma corriente.
:::

⁠**Cómo leerlo:** Cargado significa: la carga está separada, no añadida. La carga total sigue siendo cero. Cada línea de campo que empieza en A termina en B ([Parte 1](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)). Lo habitual son cargas de nanoculombios a miliculombios. **Validez:** El dieléctrico se considera un aislante ideal; la etapa [5](bauformen-und-selbstentladung.html#stufe-5) indica la desviación.

:::herleitung Por qué circula la misma corriente en ambos terminales
Supongamos que entra más de lo que sale. Entonces se acumula en el componente una carga neta $Q_\mathrm{n}$, y todo el componente sube de potencial respecto a su entorno. Cuánto lo muestra una esfera del tamaño de una carcasa, $r=1$ cm: según la [Parte 1](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html) tiene el potencial $\varphi=k\,Q_\mathrm{n}/r$, y ya 1 µC daría 900 kV. El campo de esta carga frena la entrada mucho antes de que surja una diferencia medible. Así, $Q_\mathrm{n}$ se mantiene prácticamente en cero, y la ley de nudos de la [Parte 2](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html) se cumple para el componente en su conjunto.
:::

:::analogie
En la tubería de un circuito de agua hay una membrana de goma atravesada. La bomba empuja agua contra ella, y la membrana se estira. A ambos lados se mueve agua, pero nada atraviesa la membrana. Su contrapresión crece con el estiramiento, y cuando alcanza la presión de la bomba, el agua se detiene. La imagen termina en la energía: la membrana la almacena en la goma; el condensador, en el campo entre las placas (etapa [6](die-gespeicherte-energie.html#stufe-6)).
:::

**Ejemplo.** Un instrumento de medida en el cable de A indica durante 0,1 s una corriente constante de 0,9 mA. Se han desplazado entonces $Q=I\,t=90\,\mu\text{C}$, es decir, $5{,}6\cdot10^{14}$ electrones. Han abandonado A, y otros tantos han llegado a B. Un instrumento en el cable de B indica los mismos 0,9 mA.

⁠**Caso límite:** Si las placas ya están a los potenciales de los polos, la caída a lo largo de los cables es cero, y también la corriente. Un condensador cargado a 9 V no toma corriente de una batería de 9 V.

:::frage Entonces, ¿la corriente pasa por el condensador o no?
Por los cables de conexión sí; por el hueco, no. Desde fuera solo se ven los terminales: por uno entra corriente y por el otro sale la misma. Para el circuito esto parece una corriente continuada, de ahí la forma breve de hablar. Pero solo dura mientras la carga cambia.
:::

:::frage ¿Por qué la carga se queda donde está al desconectar la batería?
Los electrones de B son atraídos por A, pero el aislante no los deja pasar, y los extremos de los cables están abiertos. Un camino solo surge cuando un conductor une los terminales (etapa [10](entladen-und-zeitkonstante.html#stufe-10)).
:::

:::aufgabe Ejercicio 1 ★ Lo que indican los instrumentos
<span class="anker" id="aufg-1"></span>

En el cable de conexión de la placa A de un condensador, un instrumento de medida indica durante 2 s una corriente constante de 0,45 mA.

<ol class="al">

<li>

¿Cuánta carga se ha desplazado y cuántos electrones son?

</li>

<li>

¿Qué indica un instrumento en el cable de la placa B? ¿Cuál es después la carga total del condensador?

</li>

<li>

¿Cuántos electrones han atravesado el aislante?

</li>

</ol>

:::loesung
(a) $Q=I\,t=0{,}45\,\mathrm{mA}\cdot2\,\mathrm{s}=900\,\mu\text{C}$, es decir, $N=Q/e=5{,}6\cdot10^{15}$ electrones.

(b) También 0,45 mA: lo que entra por A sale por B. La carga total sigue siendo cero; A lleva $+900\,\mu\text{C}$ y B lleva $-900\,\mu\text{C}$.

(c) Ninguno. Los electrones de B proceden del cable; los electrones de A se han ido por el cable.
:::
:::

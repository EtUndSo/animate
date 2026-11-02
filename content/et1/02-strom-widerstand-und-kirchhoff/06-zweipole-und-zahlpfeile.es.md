---
title: Etapa 5: Dipolos y flechas de referencia
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / Corriente, resistencia y leyes de Kirchhoff
order: 1120600
summary: A partir de ahora no importa lo que ocurre dentro del componente, sino lo que se puede medir en sus terminales.
tags: dipolo, curva característica, caja negra, red, dipolo lineal, dipolo no lineal, convenio receptor, convenio generador
lang: es
---

<span class="anker" id="stufe-5"></span>

:::zweck
A partir de ahora no importa lo que ocurre dentro del componente, sino lo que se puede medir en sus terminales. Para ello hace falta un concepto para el componente y un convenio sobre los signos.
:::

**La idea.** Para calcular basta saber cómo responde un componente con corriente a una tensión. El interior puede ser desconocido. Los signos se fijan de antemano con flechas, porque antes del cálculo a menudo no se conocen los sentidos reales. El resultado dice después si la realidad sigue la flecha.

:::definition Definición 5.1 (Dipolo, caja negra, red)
<span class="anker" id="satz-5-1"></span>

Un __dipolo__ es un componente que se puede describir por completo mediante la corriente y la tensión entre sus dos terminales. En régimen estacionario (independiente del tiempo), eso es su __curva característica__ $I=f(U)$. Una __caja negra__ es un sistema cuyo comportamiento hacia fuera se conoce, pero cuya estructura es desconocida o no importa. Una __red__ es una interconexión de dipolos. Si la curva característica es una recta que pasa por el origen, se cumple

<span class="anker" id="gl-5-1"></span>
$$G=\frac IU=\text{const}\quad\text{o bien}\quad R=\frac UI=\text{const}. \tag{5.1}$$
:::

⁠**Cómo leerlo:** Un __dipolo lineal__ así es la resistencia óhmica (fig. [4](das-ohmsche-gesetz-aus-feld-und-stoen.html#abb-4), derecha, cada recta un valor). También las baterías y las fuentes de tensión forman parte de las redes lineales, pero su curva característica no pasa por el origen ([Parte 5](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)). En un __dipolo no lineal__ como la lámpara incandescente (fig. [5](reale-widerstande-werte-und-temperatur.html#abb-5), derecha), $U/I$ depende del punto de trabajo, y allí no se cumple [(5.1)](#gl-5-1).

:::definition Definición 5.2 (Convenios de signos)
<span class="anker" id="satz-5-2"></span>

La flecha de tensión apunta de 1 a 2 y significa $U_{12}=\varphi_1-\varphi_2$ ([Parte 1](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)). La flecha de corriente cuenta la carga positiva en el sentido de la flecha. En el __convenio receptor__ (CR), las flechas de tensión y de corriente de un dipolo apuntan en el mismo sentido; en el __convenio generador__ (CG), en sentidos opuestos. Para una resistencia se cumple

<span class="anker" id="gl-5-2"></span>
$$U=R\,I\quad\text{(CR)},\qquad U=-R\,I\quad\text{(CG)}. \tag{5.2}$$
:::

⁠**Cómo leerlo:** Ambos convenios son solo acuerdos. El sentido de ambas flechas se elige libremente; eso cambia signos, nunca la física. Lo habitual es el CR en el receptor y el CG en la fuente, porque entonces en funcionamiento normal todos los números son positivos (fig. [6](#abb-6), izquierda). **Por qué encaja:** En el receptor, la carga positiva va del potencial alto al bajo y cede energía; corriente y tensión tienen el mismo sentido. En la fuente se eleva del potencial bajo al alto; corriente y tensión tienen sentidos opuestos. En el CR, $U\,I>0$ significa por tanto absorción de energía; en el CG, entrega.

El __sentido convencional de la corriente__ es el sentido en el que se movería la carga positiva: fuera de la fuente, de positivo a negativo. Corresponde a la flecha de corriente en el receptor en el CR. Los electrones se mueven en sentido contrario.

:::abbildung et1/k2zaehlpfeil 6
Izquierda: cadena de fuente y $3\,\mathrm{k\Omega}$ con las flechas habituales. En la fuente, sentidos opuestos (CG); en la resistencia, el mismo sentido (CR); todos los valores son positivos. Los electrones se mueven contra la flecha de corriente. Derecha: la misma resistencia, una vez con la flecha de tensión invertida. Solo cambia el signo.
:::

**Ejemplo.** 9 V en $3\,\mathrm{k\Omega}$ dan $I=3$ mA. Si la flecha de tensión apunta de abajo arriba, $U=\varphi_\text{abajo}-\varphi_\text{arriba}=-9$ V, y [(5.2)](#gl-5-2) queda $-9\,\mathrm{V}=-3\,\mathrm{k\Omega}\cdot3\,\mathrm{mA}$. **Comprobación:** Si se invierten ambas flechas, $U=R\,I$ se convierte en $-U=R\,(-I)$, es decir, de nuevo la misma ecuación.

:::frage Los electrones van de negativo a positivo. ¿Por qué se calcula al revés?
El sentido se fijó antes de conocer los electrones, y no perjudica: en $\vec j=q\,\vec v$, para los electrones ambos factores cambian de signo. Electrones hacia la izquierda dan la misma densidad de corriente que carga positiva hacia la derecha. La caída de tensión, el calor y el campo magnético solo dependen de $\vec j$.
:::

:::aufgabe Ejercicio 5 ★ Interpretar los signos
<span class="anker" id="aufg-5"></span>

<ol class="al">

<li>

Una caja negra en el CR muestra $U=5$ V e $I=-2$ mA. ¿Absorbe o entrega energía, y cuánta por segundo?

</li>

<li>

Una batería de coche en el CG muestra $U=14$ V e $I=-10$ A. ¿Qué le ocurre?

</li>

<li>

En un hilo, los electrones avanzan hacia la derecha; el módulo de la corriente es 2 mA. La flecha de corriente apunta hacia la derecha. ¿Cuánto vale $I$?

</li>

</ol>

:::loesung
(a) $U\,I=-10$ mW en el CR: la caja entrega 10 mW; funciona como fuente. (b) $U\,I=-140$ W en el CG: no entrega, sino que absorbe 140 W. Se está cargando. (c) La corriente en el sentido de la carga positiva va hacia la izquierda, así que $I=-2$ mA.
:::
:::

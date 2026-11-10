---
title: Etapa 9: Realimentación positiva y el disparador de Schmitt
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / El amplificador operacional
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-operationsverstarker
knoten: Capítulo 11: El amplificador operacional
order: 1211100
summary: Si en el amplificador no inversor se intercambian las entradas, las mismas ecuaciones dan el mismo número.
tags: histéresis, disparador de Schmitt, inestable
lang: es
---

<span class="anker" id="stufe-9"></span>

:::zweck
Si en el amplificador no inversor se intercambian las entradas, las mismas ecuaciones dan el mismo número. Pero el circuito hace algo completamente distinto. Esta etapa aclara por qué falla aquí la regla y qué ocurre en su lugar.
:::

**La idea.** Ahora $U_\mathrm{E}$ está en la entrada negativa, y el divisor lleva a la entrada positiva (fig. [11](#abb-11)). El cálculo $U_\mathrm{D}=\beta\,U_\mathrm{A}-U_\mathrm{E}$ y $U_\mathrm{A}=A\,U_\mathrm{D}$ tiene, con $U_\mathrm{E}=1$ V, la solución $U_\mathrm{A}=5{,}00025$ V. Es un equilibrio, pero inestable, como una bola sobre una cima. Una perturbación de 1 µ V hacia arriba eleva la entrada positiva, luego crece $U_\mathrm{D}$, luego la salida sigue subiendo. El efecto refuerza su causa. La salida va hasta el tope y se queda allí. Allí la regla no vale: $U_\mathrm{D}\ne0$.

En el tope, el circuito recuerda su estado. Si la salida está en $+11$ V, la entrada positiva está en $+2{,}2$ V. Mientras $U_\mathrm{E}$ se quede por debajo, $U_\mathrm{D}>0$ y nada cambia. Si $U_\mathrm{E}$ supera los 2,2 V, la salida bascula, y la entrada positiva salta a $-2{,}2$ V. Esto refuerza el basculamiento. Para volver a bascular, $U_\mathrm{E}$ tiene que bajar de $-2{,}2$ V. La salida depende de la historia previa; esto se llama __histéresis__. El circuito se llama __disparador de Schmitt__ inversor.

:::satz Teorema 9.1 (Disparador de Schmitt)
<span class="anker" id="satz-9-1"></span>

Con $\beta=R_1/(R_1+R_2)$, la salida bascula

<span class="anker" id="gl-9-1"></span>
$$\text{hacia abajo en }U_\mathrm{E}=\beta\,U_\mathrm{A,max},\qquad\text{hacia arriba en }U_\mathrm{E}=\beta\,U_\mathrm{A,min}. \tag{9.1}$$

La anchura de la histéresis es $\beta\,(U_\mathrm{A,max}-U_\mathrm{A,min})$. Entre los umbrales son posibles ambos estados.
:::

⁠**Cómo leerlo:** La salida cambia en cuanto $U_\mathrm{D}$ cambia de signo. **Validez:** $A\beta>1$; si no, la realimentación positiva no basta para bascular.

:::herleitung La misma ecuación, otro signo
Con la inercia de la etapa [4](gegenkopplung.html#stufe-4) se cumple ahora $\tau\,\mathrm{d} U_\mathrm{A}/\mathrm{d} t=A(\beta\,U_\mathrm{A}-U_\mathrm{E})-U_\mathrm{A}=(A\beta-1)\,U_\mathrm{A}-A\,U_\mathrm{E}$. El factor delante de $U_\mathrm{A}$ es ahora positivo. Una desviación del equilibrio crece como $\mathrm{e}^{+t/\tau_\mathrm{M}}$ con $\tau_\mathrm{M}=\tau/(A\beta-1)=0{,}80$ µ s, del mismo tamaño que en la etapa [4](gegenkopplung.html#stufe-4). Así, 1 µ V de perturbación se convierte en los 11 V en 13 µ s. Una alimentación ilimitada daría una subida ilimitada; el circuito sería __inestable__. Solo la saturación la detiene.
:::

:::abbildung et1/k11schmitt 11
A la izquierda, el disparador de Schmitt inversor. A la derecha, el ciclo de histéresis en el modelo de referencia, $\beta=0{,}2$: viniendo de la izquierda bascula en $+2{,}2$ V; viniendo de la derecha, en $-2{,}2$ V. Las flechas indican el sentido de recorrido.
:::

::::beispiel
Los umbrales son $\pm0{,}2\cdot11\,\mathrm{V}=\pm2{,}2$ V, y la histéresis tiene 4,4 V de ancho. Poco después de bascular con $U_\mathrm{E}=2{,}2$ V es $U_\mathrm{D}=-2{,}2\,\mathrm{V}-2{,}2\,\mathrm{V}=-4{,}4$ V, muy lejos de la ventana. Utilidad: una señal ruidosa que cruza lentamente un umbral hace conmutar un comparador muchas veces de un lado a otro. En el disparador de Schmitt, el umbral salta 4,4 V tras el primer basculamiento, y un ruido menor que esa anchura no provoca un segundo basculamiento.
::::

⁠**Casos límite:** $\beta\to0$ da el comparador de la etapa [3](der-opv-ohne-ruckfuhrung.html#stufe-3). $U_\mathrm{E}=0$ admite ambos estados, según la historia previa.

:::frage LTspice mostró en `.op`, con las entradas intercambiadas, 5,00025 V. ¿Está mal la simulación?
No, responde a otra pregunta. `.op` resuelve la ecuación de equilibrio, y esta solución existe. Si un equilibrio se mantiene lo decide solo la evolución temporal. En el componente siempre hay algo de ruido; por eso la salida se escapa. El recuadro de LTspice de la etapa [10](wo-die-regeln-enden.html#stufe-10) lo muestra en `.tran`.
:::

:::aufgabe Ejercicio 10 ★★ Disparador de Schmitt
<span class="anker" id="aufg-10"></span>

(a) Con $R_1=10$ k$\Omega$, $R_2=90$ k$\Omega$: ¿dónde están los umbrales y qué anchura tiene la histéresis? (b) Elige $R_2$ para los umbrales $\pm1$ V con $R_1=10$ k$\Omega$. (c) Con (a), $U_\mathrm{E}$ va de $-5$ V a $+5$ V y vuelve. Esboza $U_\mathrm{A}(U_\mathrm{E})$. (d) Una alimentación de 0 a 5 V da una salida de 0,5 V a 4,5 V, $\beta=0{,}2$. ¿Dónde están los umbrales?

:::loesung
(a) $\beta=0{,}1$: umbrales $\pm1{,}1$ V, anchura 2,2 V. (b) $\beta=1/11$, así que $R_2=100$ k$\Omega$. (c) Con $-5$ V, la salida está en $+11$ V. Se queda allí hasta $U_\mathrm{E}=+1{,}1$ V, salta a $-11$ V y se queda allí hasta $5$ V. A la vuelta no salta de nuevo hasta $-1{,}1$ V. (d) $0{,}2\cdot4{,}5\,\mathrm{V}=0{,}9$ V y $0{,}2\cdot0{,}5\,\mathrm{V}=0{,}1$ V.
:::
:::

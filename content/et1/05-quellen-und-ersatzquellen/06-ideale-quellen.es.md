---
title: Etapa 4: Fuentes ideales
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / Fuentes y fuentes equivalentes
order: 1150600
summary: Hasta ahora falta lo que impulsa la corriente.
tags: fuente de tensión ideal, fuente de corriente ideal, tensión de fuente, corriente de fuente
lang: es
---

<span class="anker" id="stufe-4"></span>

:::zweck
Hasta ahora falta lo que impulsa la corriente. Esta etapa introduce los dos componentes básicos que aportan energía a una red.
:::

**La idea.** Una fuente mantiene fija una sola magnitud. La otra la determina la red conectada. Una __fuente de tensión ideal__ mantiene la diferencia de potencial entre sus terminales. Qué corriente circula lo decide la carga. Una __fuente de corriente ideal__ mantiene la corriente en su rama. Qué tensión se establece lo decide también la carga. Ambas son modelos. No se pueden construir, pero una fuente de alimentación regulada o un circuito con transistores ([Parte 10](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor/der-bipolartransistor.html)) se les acercan en un rango limitado.

:::abbildung et1/k5ideal 5
A la izquierda, la fuente de tensión ideal: en el diagrama, una horizontal; la tensión no depende de la corriente. A la derecha, la fuente de corriente ideal: una vertical; la corriente no depende de la tensión. El trazo en el símbolo muestra el comportamiento con el valor cero: trazado a lo largo, la línea está cerrada; trazado en transversal, la línea está interrumpida.
:::

:::definition Definición 4.1 (Fuentes ideales)
<span class="anker" id="satz-4-1"></span>

Para la fuente de tensión ideal y la fuente de corriente ideal se cumple

<span class="anker" id="gl-4-1"></span>
$$U_\mathrm{AB}=U_\mathrm{q}\quad\text{para toda corriente},\qquad\qquad I_\mathrm{A}=I_\mathrm{q}\quad\text{para toda tensión}. \tag{4.1}$$
:::

⁠**Cómo leerlo:** $U_\mathrm{q}$ es la __tensión de fuente__ en V, de milivoltios a kilovoltios, aquí 9 V. $I_\mathrm{q}$ es la __corriente de fuente__ en A, de microamperios a amperios. En la fig. [5](#abb-5), la pendiente de la curva característica es la resistencia interna con signo negativo: cero en la fuente de tensión, infinita en la fuente de corriente. Al calcular, una fuente de tensión sustituye la diferencia de dos potenciales de nudo por un valor conocido; una fuente de corriente fija la corriente de una rama.

⁠**Validez:** Dos conexiones contradicen el modelo. Una fuente de tensión cortocircuitada debería cumplir a la vez $U_\mathrm{AB}=U_\mathrm{q}$ y $U_\mathrm{AB}=0$. Una fuente de corriente abierta debería cumplir a la vez $I_\mathrm{A}=I_\mathrm{q}$ e $I_\mathrm{A}=0$, porque una corriente necesita un camino cerrado.

**Ejemplo.** La fuente de 9 V entrega 0,5625 A en 16 $\Omega$, 9 A en 1 $\Omega$, y en 1 m$\Omega$ serían 9000 A. Una fuente de 0,5 A produce 8 V en 16 $\Omega$, 500 V en 1 k$\Omega$, y en 1 M$\Omega$ serían 500 kV. **Caso límite:** Cuanto más extrema es la carga, más se aleja el modelo de cualquier aparato real. Ese es el motivo de la siguiente etapa.

:::frage ¿Puede la corriente circular también al revés por una fuente?
Sí. Una fuente ideal solo fija su única magnitud. Si la corriente entra por el polo positivo de una fuente de tensión, es $I_\mathrm{A}<0$, y la fuente absorbe potencia. Así se carga una batería recargable.
:::

:::aufgabe Ejercicio 5 ★ ¿Qué cambia?
<span class="anker" id="aufg-5"></span>

Una fuente de corriente ideal de 2 mA alimenta 1 k$\Omega$. (a) ¿Cuánto vale la tensión, y cuánto con 4,7 k$\Omega$? (b) En serie con la fuente se añade una segunda resistencia de 1 k$\Omega$. ¿Qué cambia en la primera y qué en la fuente? (c) En paralelo con una fuente ideal de 5 V que alimenta 1 k$\Omega$ se añaden 10 $\Omega$. ¿Qué cambia en la carga y qué en la fuente?

:::loesung
(a) $2\,\mathrm{mA}\cdot1\,\mathrm{k\Omega}=2$ V, con 4,7 k$\Omega$ son 9,4 V. La corriente no cambia.

(b) En la primera resistencia no cambia nada: la corriente es fija y la tensión sigue siendo 2 V. La fuente debe aportar 4 V. En serie con una fuente de corriente ideal, una resistencia es invisible desde fuera.

(c) En la carga no cambia nada, sigue en 5 V y 5 mA. La fuente entrega 505 mA en lugar de 5 mA. En paralelo con una fuente de tensión ideal, una resistencia es invisible desde fuera.
:::
:::

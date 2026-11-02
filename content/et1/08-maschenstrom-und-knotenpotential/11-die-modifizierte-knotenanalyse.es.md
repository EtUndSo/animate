---
title: Etapa 9: El análisis por nudos modificado
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / Análisis por mallas y por nudos
order: 1181100
summary: Una fuente de tensión ideal no tiene conductancia ni forma de fuente de corriente (Parte 5).
tags: ganancia de corriente, frecuencia de transición
lang: es
---

<span class="anker" id="stufe-9"></span>

:::zweck
Una fuente de tensión ideal no tiene conductancia ni forma de fuente de corriente ([Parte 5](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)). Esta etapa elimina la última restricción. Así calcula SPICE cualquier circuito.
:::

**La idea.** Una fuente de tensión fija la tensión entre dos nudos. Su corriente solo se establece a través de la red, así que es desconocida. Se toma como incógnita adicional. Una incógnita adicional exige una ecuación adicional, y la propia fuente la aporta: la diferencia de potencial es $U_\mathrm q$. Así vuelve por cada fuente de tensión exactamente una ecuación de malla; todo lo demás sigue siendo análisis por nudos (fig. [9](#abb-9)).

:::abbildung et1/k8mna 9
Análisis por nudos modificado. La fuente entre $i$ y $k$ recibe una columna nueva para su corriente $I_V$ (verde) y una fila nueva para su tensión (rojo). $\mathbf Y$ se queda como está.
:::

:::satz Teorema 9.1 (Análisis por nudos modificado, MNA)
<span class="anker" id="satz-9-1"></span>

Una red con $n$ nudos además del nudo de referencia y una fuente de tensión ideal entre $i$ y $k$ cumple

<span class="anker" id="gl-9-1"></span>
$$\begin{pmatrix}\mathbf Y&\mathbf C\\\mathbf B&0\end{pmatrix}\begin{pmatrix}\mathbf U\\I_V\end{pmatrix}=\begin{pmatrix}\mathbf I_\mathrm q\\U_\mathrm q\end{pmatrix}. \tag{9.1}$$

$\mathbf C$ es la columna nueva con $+1$ en la fila $i$ y $-1$ en la fila $k$. $\mathbf B$ es la fila nueva con $+1$ en la columna $i$ y $-1$ en la columna $k$. $I_V$ se cuenta de $i$ a través de la fuente hacia $k$. La fila nueva dice

<span class="anker" id="gl-9-2"></span>
$$U_i-U_k=U_\mathrm q. \tag{9.2}$$

Por cada fuente de tensión adicional se añaden una fila y una columna.
:::

⁠**Cómo leerlo:** $I_V$ sale en $i$ y llega en $k$; por eso está en la fila $i$ con $+1$ y en la fila $k$ con $-1$, como las corrientes salientes de una conductancia. Si la fuente entrega potencia, su corriente la atraviesa de negativo a positivo, e $I_V$ es negativa. Eso es justo lo que SPICE muestra como `I(V1)`. Los unos no tienen unidad; la fila nueva calcula en voltios, la columna nueva en amperios. **Validez:** En la diagonal hay ahora un cero, pero el sistema sigue siendo resoluble mientras la red sea unívoca. Dos fuentes ideales en paralelo no lo son. **En resumen:** Cada elemento de la red tiene su propia estampa, y todas se pueden escribir independientemente unas de otras.

**Ejemplo: la red modelo tal como la ve SPICE.** SPICE no convierte nada. La batería es una fuente ideal $U_\mathrm q$ entre el nuevo nudo 3 y masa; detrás está $R_1$ de 3 a 1. La fuente de corriente y $R_5$ se quedan como están. Las incógnitas son $U_1$, $U_2$, $U_3$ e $I_V$:

$$\begin{pmatrix}1{,}75&-0{,}5&-1&0\\-0{,}5&0{,}8&0&0\\-1&0&1&1\\0&0&1&0\end{pmatrix} \begin{pmatrix}U_1\\U_2\\U_3\\I_V\end{pmatrix}=\begin{pmatrix}0\\4\\0\\9\end{pmatrix}.$$

La última fila da $U_3=9$ V, con lo que las dos primeras filas se convierten en el sistema de la etapa [5](das-knotenpotentialverfahren.html#stufe-5): $U_1=8$ V, $U_2=10$ V. La tercera fila da $I_V=G_1\,(U_1-U_3)=-1$ mA. Son los resultados de ambos métodos, sin ninguna conversión. **Caso límite:** Para $R_1\to0$, el nudo 3 pasa a ser el nudo 1. El análisis por nudos falla ahí, el MNA no (ejercicio [11](#aufg-11)).

:::ltspice La red modelo tal como la resuelve SPICE
⁠**Esquema:** `voltage` con `9` de `3` a masa, `R1 1k` de `3` a `1`, `R2 4k` de `1` a masa, `R3 2k` de `1` a `2`, `R4 10k` y `R5 5k` de `2` a masa, `current` con `4m` de masa a `2`.

⁠**Directivas:** `.op`, `.meas op u1 FIND V(1)`, `.meas op u2 FIND V(2)`, `.meas op u3 FIND V(3)`, `.meas op iv FIND I(V1)`.

⁠**Lo que ves:** $\mathtt{u1}=8$ V, $\mathtt{u2}=10$ V, $\mathtt{u3}=9$ V, $\mathtt{iv}=-1$ mA. Son exactamente las cuatro incógnitas de la matriz de arriba. `I(V1)` cuenta del terminal positivo al negativo a través de la fuente, como $I_V$. Después sustituye la batería como en el ejercicio [11](#aufg-11).
:::

**Una fuente de 0 V es un amperímetro.** Una fuente de tensión ideal con $U_\mathrm q=0$ actúa como un hilo, pero el MNA da su corriente. Esto se aprovecha para medir la __ganancia de corriente__. En el amplificador, $I_\mathrm{ent}$ alimenta el nudo 1 con $G_\mathrm i$, y la salida 2 está unida a masa por la fuente de 0 V. Con $I_\mathrm{sal}$ del nudo 2 a través de la fuente hacia masa se tiene

<span class="anker" id="gl-9-3"></span>
$$\begin{pmatrix}G_\mathrm i&0&0\\g&G_\mathrm o&1\\0&1&0\end{pmatrix}\begin{pmatrix}U_1\\U_2\\I_\mathrm{sal}\end{pmatrix}=\begin{pmatrix}I_\mathrm{ent}\\0\\0\end{pmatrix},\qquad \frac{I_\mathrm{sal}}{I_\mathrm{ent}}=\frac{1}{I_\mathrm{ent}}\cdot\frac{g\,I_\mathrm{ent}}{-G_\mathrm i}=-\frac{g}{G_\mathrm i}. \tag{9.3}$$

En el modelo esto da $-100$. Como $U_2=0$, por $G_\mathrm o$ no circula nada, y toda la corriente controlada pasa por el amperímetro. A frecuencias altas este módulo baja. La frecuencia a la que cae a 1 se llama __frecuencia de transición__ e indica lo rápido que es un transistor.

**El amplificador con una fuente ideal.** Si en la entrada hay la tensión ideal $U_\mathrm q$, el cálculo es más corto que en [(8.2)](gesteuerte-quellen-und-verstarker.html#gl-8-2). Con $I_V$ del nudo 1 a través de la fuente hacia masa y $G=G_\mathrm o+G_\mathrm L$ se cumple

<span class="anker" id="gl-9-4"></span>
$$\begin{pmatrix}G_\mathrm i&0&1\\g&G&0\\1&0&0\end{pmatrix}\begin{pmatrix}U_\mathrm i\\U_\mathrm o\\I_V\end{pmatrix}=\begin{pmatrix}0\\0\\U_\mathrm q\end{pmatrix},\qquad A_u=\frac{U_\mathrm o}{U_\mathrm q}=\frac{1}{U_\mathrm q}\cdot\frac{g\,U_\mathrm q}{-G}=-\frac gG=-g\,R, \tag{9.4}$$

con $R=1/G$. Es una estructura básica que reaparece en casi todos los amplificadores:

<span class="anker" id="gl-9-5"></span>
$$\text{ganancia de tensión}=-\text{transconductancia}\cdot\text{resistencia de carga}. \tag{9.5}$$

La resistencia de carga es la conexión en paralelo de todas las resistencias del nudo de salida, en el modelo $20\,\mathrm{k\Omega}\parallel5\,\mathrm{k\Omega}=4\,\mathrm{k\Omega}$, es decir, $A_u=-50\,\mathrm{mS}\cdot4\,\mathrm{k\Omega}=-200$. Si varias fuentes con la misma tensión de control alimentan la salida, sus transconductancias se suman. La regla sirve para estimar y para comprobar un cálculo. **Caso límite:** Sin carga y con $G_\mathrm o\to0$, $A_u$ crece sin límite; en realidad lo limita entonces la tensión de alimentación.

:::frage ¿Por qué SPICE no calcula con mallas, si de todos modos necesita fuentes de tensión?
Porque el MNA solo añade una fila por cada fuente de tensión, mientras que las mallas habría que buscarlas primero. Una red suele tener pocas fuentes de tensión y muchísimos componentes. Además, con esa ampliación la matriz apenas crece y sigue siendo dispersa.
:::

:::aufgabe Ejercicio 11 ★★★ Sustituir sin cambios
<span class="anker" id="aufg-11"></span>

Sustituye en la red modelo la batería y $R_1$ por una fuente ideal de 8 V del nudo 1 a masa.

<ol class="al">

<li>

Plantea el sistema MNA para $U_1$, $U_2$, $I_V$ y resuélvelo con la regla de Cramer.

</li>

<li>

¿Por qué no cambia nada respecto a la red original fuera de la rama sustituida?

</li>

<li>

Ahora la fuente ideal da 9 V. ¿Cuánto valen $U_2$ e $I_V$?

</li>

</ol>

:::loesung
(a) Incógnitas $U_1$, $U_2$, $I_V$. Quedan $G_2$, $G_3$, $G_4$, $G_5$ y la fuente de corriente:

$$\begin{pmatrix}0{,}75&-0{,}5&1\\-0{,}5&0{,}8&0\\1&0&0\end{pmatrix}\begin{pmatrix}U_1\\U_2\\I_V\end{pmatrix}=\begin{pmatrix}0\\4\\8\end{pmatrix}.$$

$D=-0{,}8$, $D_1=-6{,}4$, $D_2=-8$, $D_3=0{,}8$. Por tanto, $U_1=8$ V, $U_2=10$ V, $I_V=-1$ mA.

(b) En el nudo 1 ya había 8 V, y la rama llevaba 1 mA hacia el nudo. Una fuente ideal con exactamente esa tensión impone el mismo estado. El resto de la red solo percibe la tensión y la corriente en ese nudo.

(c) $U_1=9$ V. Fila 2: $U_2=(4+0{,}5\cdot9)/0{,}8=10{,}6$ V. Fila 1: $I_V=-0{,}75\cdot9+0{,}5\cdot10{,}625=-1{,}44$ mA.
:::
:::

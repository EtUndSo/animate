---
title: Etapa 6: El punto de trabajo
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / Semiconductores y diodos
order: 1190800
summary: En una resistencia, U=R\,I da el resultado de inmediato.
tags: recta de carga, punto de trabajo, Análisis del punto de trabajo, Síntesis del punto de trabajo, sin carga, cortocircuito, histéresis, iteración
lang: es
---

<span class="anker" id="stufe-6"></span>

:::zweck
En una resistencia, $U=R\,I$ da el resultado de inmediato. El diodo sigue otra curva. Esta etapa halla la tensión y la corriente del diodo en un circuito.
:::

**La idea.** Deben cumplirse dos condiciones a la vez. El diodo solo admite puntos de su curva característica. El resto del circuito, fuente y resistencia, solo admite puntos de la __recta de carga__ ([Parte 5](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)). El circuito encuentra la intersección por sí mismo: si $U_\mathrm D$ es demasiado pequeña, la resistencia entrega más corriente de la que deja pasar el diodo. La carga se acumula en el nudo entre ambos y eleva su potencial hasta que las dos corrientes son iguales.

:::abbildung et1/k9arbeitsgerade 8
Circuito del modelo de referencia y solución gráfica. En rojo, la recta de carga por los puntos sin carga y cortocircuito. En azul, la curva característica del diodo, intersección en 0,69 V y 4,31 mA. En verde, la curva característica de una resistencia de 250 $\Omega$ en lugar del diodo, intersección en 1 V y 4 mA.
:::

:::definition Definición 6.1 (Punto de trabajo)
<span class="anker" id="satz-6-1"></span>

El __punto de trabajo__ (PT) es el punto de la curva característica que fijan la corriente por el componente y la tensión en él. __Análisis del punto de trabajo__ significa determinarlo a partir del circuito dado. __Síntesis del punto de trabajo__ significa elegir los componentes de modo que resulte un PT deseado.
:::

**El caso lineal.** Si se sustituye el diodo por una resistencia $R_1$, rigen la ecuación del componente, la ley de las mallas y, de ellas, la recta de carga:

<span class="anker" id="gl-6-1"></span>
$$I=\frac{U_{R1}}{R_1},\qquad U_0=U_R+U_{R1}=R\,I+U_{R1},\qquad I=\frac{U_0-U_{R1}}{R}. \tag{6.1}$$

Dos ecuaciones lineales se pueden resolver; con $R_1=250\,\Omega$ resulta $I=U_0/(R+R_1)=4$ mA y $U_{R1}=1$ V. Resolver el sistema de ecuaciones significa intersecar las dos rectas.

:::satz Teorema 6.2 (Punto de trabajo del diodo)
<span class="anker" id="satz-6-2"></span>

Para el circuito en serie se cumplen a la vez

<span class="anker" id="gl-6-2"></span>
$$I=\frac{U_0-U_\mathrm D}{R}\qquad\text{y}\qquad I=I_\mathrm S\bigl(\mathrm{e}^{U_\mathrm D/U_T}-1\bigr). \tag{6.2}$$

La curva característica sube en todas partes, la recta baja en todas partes; por tanto hay exactamente una intersección.
:::

⁠**Cómo leerlo:** $U_\mathrm D$ es la tensión $U$ de [(4.1)](warum-der-strom-exponentiell-wachst.html#gl-4-1). La recta de carga se traza por dos puntos, sin tener en cuenta el diodo: __sin carga__ ($I=0$, $U_\mathrm D=U_0$) y __cortocircuito__ ($U_\mathrm D=0$, $I=U_0/R$). La curva característica viene de la ecuación o de una hoja de datos. **Validez:** Los componentes cuya curva característica retrocede o cuyo estado depende de su historia (__histéresis__) pueden tener varias intersecciones. Varios componentes no lineales se resuelven numéricamente o con circuitos equivalentes (etapa [7](lineare-ersatzschaltungen.html#stufe-7)).

[(6.2)](#gl-6-2) no se puede despejar para $U_\mathrm D$, porque $U_\mathrm D$ está en el exponente y fuera de él. Se resuelve gráficamente o por __iteración__, es decir, por sustitución repetida: estima $U_\mathrm D$, calcula $I=(U_0-U_\mathrm D)/R$, luego $U_\mathrm D=U_T\ln(I/I_\mathrm S+1)$, y repite.

**Ejemplo.** Inicio con $U_\mathrm D=0{,}7$ V. Paso 1: $I=4{,}300$ mA, $U_\mathrm D=0{,}69245$ V. Paso 2: $I=4{,}3076$ mA, $U_\mathrm D=0{,}69249$ V. Así, el PT es (0,692 V | 4,31 mA), y en la resistencia hay 4,31 V. Si se duplica $U_0$ a 10 V, la corriente casi se duplica, a 9,29 mA, y $U_\mathrm D$ sube solo 20 mV, a 0,712 V. **Casos límite:** Con $U_0=0{,}5$ V, $I=2{,}3$ µ A, y casi toda la tensión de la fuente queda en el diodo. Con $U_0$ negativa, $I=-I_\mathrm S$, y la fuente queda por completo en el diodo.

:::frage ¿Por qué no se calcula al revés: estimar $U_\mathrm D$, obtener $I$ de la función exponencial y luego $U_\mathrm D=U_0-R\,I$?
Porque ese camino diverge. Un error de 1 mV cambia la corriente del diodo un 3,9 %, es decir, 0,17 mA, y eso da en la resistencia un error de 167 mV. En el primer método el error se reduce en cada paso en ese mismo factor, $r/R=0{,}006$ (etapa [8](kleine-anderungen-um-den-arbeitspunkt.html#stufe-8)). El logaritmo plano amortigua, la exponencial empinada amplifica.
:::

:::aufgabe Ejercicio 7 ★★ Hallar y ajustar el punto de trabajo
<span class="anker" id="aufg-7"></span>

El diodo del modelo de referencia está en serie con $R=470\,\Omega$ conectado a $U_0=3$ V.

<ol class="al">

<li>

Determina los puntos sin carga y cortocircuito de la recta de carga.

</li>

<li>

Itera desde 0,7 V hasta que tres cifras ya no cambien.

</li>

<li>

Síntesis del punto de trabajo: ¿qué $R$ da la corriente de 2 mA con $U_0=5$ V? ¿Qué corriente circula con el valor normalizado 2,2 k$\Omega$?

</li>

<li>

Se invierte el diodo. ¿Qué se mide en el diodo y en la resistencia?

</li>

</ol>

:::loesung
(a) Sin carga $U_\mathrm D=3$ V, cortocircuito $I=3\,\mathrm{V}/470\,\Omega=6{,}38$ mA. (b) $U_\mathrm D=0{,}7$ V da $I=4{,}894$ mA, esto da $U_\mathrm D=0{,}6958$ V, luego $I=4{,}903$ mA y de nuevo $U_\mathrm D=0{,}6958$ V. PT: (0,696 V | 4,90 mA). (c) A 2 mA, $U_\mathrm D=0{,}673$ V, así que $R=(5\,\mathrm{V}-0{,}673\,\mathrm{V})/2\,\mathrm{mA}=2{,}16\,\mathrm{k\Omega}$. Con 2,2 k$\Omega$ circulan 1,97 mA. (d) El diodo bloquea: $I=-10^{-14}$ A, en la resistencia 4,7 pV, en el diodo $-3$ V.
:::
:::

---
title: Etapa 8: Conservación de la carga al conmutar
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / El condensador
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator
knoten: Capítulo 3: El condensador
order: 1130900
summary: Si se conmutan condensadores cargados, la nueva tensión puede hallarse sin ningún cálculo de corriente.
tags: 
lang: es
---

<span class="anker" id="stufe-8"></span>

:::zweck
Si se conmutan condensadores cargados, la nueva tensión puede hallarse sin ningún cálculo de corriente. Basta con contar carga.
:::

**La idea.** En un sistema cerrado, la suma de las cargas se mantiene constante ([capítulo 1](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)). En los circuitos, un sistema así surge cuando todo camino de un nudo a masa pasa por un condensador. Es la isla de la etapa [7](parallel-und-reihenschaltung.html#stufe-7): los dieléctricos bloquean todos los caminos. La carga puede redistribuirse dentro de la isla, pero no abandonarla. Si se compara el antes y el después, no hace falta saber cómo transcurrió la igualación.

:::satz Teorema 8.1 (Conservación de la carga en una isla)
<span class="anker" id="satz-8-1"></span>

Si todo camino de un nudo a masa pasa por una capacidad, la suma de las cargas de las placas conectadas se mantiene constante:

<span class="anker" id="gl-8-1"></span>
$$Q_\mathrm{tot}=\sum_iC_iU_i=\text{const}. \tag{8.1}$$
:::

⁠**Cómo leerlo:** $U_i$ es la tensión del nudo a la placa opuesta, de modo que $C_iU_i$ es la carga de la placa en el nudo, con signo. La comparación vale entre dos estados de reposo; $Q=C\,U$ proporciona las tensiones. **Validez:** Del nudo no debe colgar ninguna resistencia ni fuente hacia el exterior, y la igualación debe ser rápida frente a la autodescarga.

:::abbildung et1/k3umladen 8
Posición 1: $C_1$ se carga a 9 V, $C_2$ está vacío. Posición 2: la isla discontinua contiene las placas superiores de ambos condensadores. Los 900 µC se reparten hasta que ambas tensiones son iguales.
:::

::::beispiel
En la fig. [8](#abb-8), $C_1$ lleva en la posición 1 la carga $C_1U_0=900\,\mu\text{C}$, y $C_2$ está vacío. El interruptor pasa a la posición 2. Ambas placas superiores cuelgan ahora de un cable, de modo que tras la igualación rige la misma tensión $U$. De [(8.1)](#gl-8-1) resulta

<span class="anker" id="gl-8-2"></span>
$$C_1U+C_2U=C_1U_0\quad\Longrightarrow\quad U=U_0\,\frac{C_1}{C_1+C_2}=9\,\mathrm{V}\cdot\frac{100}{150}=6\,\mathrm{V}. \tag{8.2}$$

Después, $C_1$ aún lleva 600 µC, y $C_2$ ha recibido 300 µC.
::::

**La energía no se conserva.** Antes hay almacenados $\frac12C_1U_0^2=4{,}05$ mJ; después, $\frac12(C_1+C_2)U^2=2{,}70$ mJ. Faltan 1,35 mJ, un tercio. La corriente de igualación calienta los cables y el interruptor. La pérdida no depende de su resistencia: una resistencia menor da una corriente mayor durante menos tiempo, y ambos efectos se compensan exactamente. En general, en la igualación de dos tensiones $U_1$ y $U_2$ se pierde:

<span class="anker" id="gl-8-3"></span>
$$W_\mathrm{V}=\frac12\,\frac{C_1C_2}{C_1+C_2}\,(U_1-U_2)^2. \tag{8.3}$$

:::herleitung La pérdida en la igualación
Con $U=\frac{C_1U_1+C_2U_2}{C_1+C_2}$ de [(8.1)](#gl-8-1) es

$$W_\mathrm{V}=\tfrac12C_1U_1^2+\tfrac12C_2U_2^2-\tfrac12\,\frac{(C_1U_1+C_2U_2)^2}{C_1+C_2}.$$

Con el denominador común $2(C_1+C_2)$ se anulan $C_1^2U_1^2$ y $C_2^2U_2^2$. En el numerador queda $C_1C_2(U_1^2-2U_1U_2+U_2^2)$, que es [(8.3)](#gl-8-3).
:::

⁠**Casos límite:** Para $C_2\to0$, $U=U_0$ se mantiene y no se pierde nada. Para $C_2\gg C_1$, $U\to0$: la carga no desaparece, pero se reparte en un condensador tan grande que apenas queda tensión.

:::frage Al cargar en la posición 1, la carga también cambia. ¿Por qué no rige allí la conservación?
Porque allí no hay isla. El nudo cuelga directamente de masa a través de la batería, y ese es un camino sin capacidad. Por él entra la carga. La conservación siempre vale para el conjunto, pero [(8.1)](#gl-8-1) necesita un nudo del que todos los caminos salgan por dieléctricos.
:::

:::ltspice Redistribución de carga a través de una resistencia
⁠**Esquema:** `cap` con `100u` de `a` a masa, valor inicial `IC=9`. `cap` con `50u` de `b` a masa, valor inicial `IC=0`. `res` con `{Rv}` de `a` a `b`. Esta resistencia representa los cables y el interruptor.

⁠**Directivas:** `.param Rv=10`, `.step param Rv list 1 10 100`, `.tran 0 100m 0 1u uic`, además de `.meas tran ua FIND V(a) AT=100m` y `.meas tran wr INTEG V(a,b)*I(R1)`. El resultado aparece en el SPICE Error Log.

⁠**Lo que ves:** Para las tres resistencias, `ua` $=6$ V y `wr` $=1{,}35$ mJ, como en [(8.2)](#gl-8-2) y [(8.3)](#gl-8-3). Solo cambia el tiempo de la igualación. Pon `IC=3` en $C_2$ y compara con el ejercicio [9](#aufg-9)(a).
:::

:::aufgabe Ejercicio 9 ★★ Redistribución de carga con precarga
<span class="anker" id="aufg-9"></span>

$C_1=100\,\mu\text{F}$ lleva 9 V. Entonces se conecta $C_2=50\,\mu\text{F}$, que ya está cargado.

<ol class="al">

<li>

$C_2$ lleva $+3$ V, en el mismo sentido que $C_1$. ¿Cuál es la tensión final? ¿Cuánta energía se pierde?

</li>

<li>

$C_2$ lleva $-3$ V, es decir, con la polaridad invertida. ¿Cuáles son ahora la tensión final y la pérdida?

</li>

<li>

Caso límite: ¿Qué resulta para $U_2=9$ V, y por qué no circula corriente de igualación?

</li>

</ol>

:::loesung
(a) $Q=100\,\mu\text{F}\cdot9\,\mathrm{V}+50\,\mu\text{F}\cdot3\,\mathrm{V}=1050\,\mu\text{C}$, $U=1050\,\mu\text{C}/150\,\mu\text{F}=7$ V. Pérdida según [(8.3)](#gl-8-3): $\frac12\cdot33{,}3\,\mu\text{F}\cdot(9\,\mathrm{V}-3\,\mathrm{V})^2=0{,}60$ mJ. Comprobación: antes 4,275 mJ, después 3,675 mJ.

(b) $Q=900\,\mu\text{C}-150\,\mu\text{C}=750\,\mu\text{C}$, $U=5$ V. Pérdida: $\frac12\cdot33{,}3\,\mu\text{F}\cdot(12\,\mathrm{V})^2=2{,}40$ mJ. La diferencia de tensiones es de 12 V, no de 6 V.

(c) $U=9$ V, $W_\mathrm{V}=0$. Ambos nudos están ya al mismo potencial, así que nada impulsa una corriente.
:::
:::

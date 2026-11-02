---
title: Etapa 8: Superposición
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / Fuentes y fuentes equivalentes
order: 1151000
summary: Cuando hay varias fuentes en distintos lugares de la red, los grupos por sí solos no ayudan.
tags: método de superposición, independiente, sensibilidad
lang: es
---

<span class="anker" id="stufe-8"></span>

:::zweck
Cuando hay varias fuentes en distintos lugares de la red, los grupos por sí solos no ayudan. El __método de superposición__ descompone el problema en un cálculo por fuente.
:::

**La idea.** Una red queda determinada por tres tipos de ecuaciones: ley de los nudos, ley de las mallas, ley de Ohm. En ninguna de ellas aparece un producto o un cuadrado de corrientes y tensiones, mientras $R$ sea fija. Tales ecuaciones son lineales. Si un sistema así tiene la solución $x'$ para una fuente y la solución $x''$ para otra, entonces $x'+x''$ es la solución cuando ambas fuentes actúan a la vez. Sustituir lo demuestra: cada ecuación se suma término a término. Así pues, cada fuente impulsa su propia corriente por la red como si la otra no estuviera, y las corrientes se suman en cada rama.

:::satz Teorema 8.1 (Superposición)
<span class="anker" id="satz-8-1"></span>

En una red lineal con $n$ fuentes de tensión independientes y $m$ fuentes de corriente independientes, para toda tensión de rama y toda corriente de rama se cumple

<span class="anker" id="gl-8-1"></span>
<span class="anker" id="gl-8-2"></span>
$$\begin{aligned} U_\mathrm{AB}&=a_1U_\mathrm{q1}+\dots+a_nU_{\mathrm{q}n}+Z_1I_\mathrm{q1}+\dots+Z_mI_{\mathrm{q}m},\\ I_\mathrm{CD}&=Y_1U_\mathrm{q1}+\dots+Y_nU_{\mathrm{q}n}+b_1I_\mathrm{q1}+\dots+b_mI_{\mathrm{q}m}. \end{aligned} \tag{8.1|8.2}$$

Los coeficientes solo dependen de las resistencias, no de las fuentes.
:::

⁠**Cómo leerlo:** Una fuente es __independiente__ si su valor no depende de ninguna magnitud de la red. $a_k$ es la ganancia de tensión de la fuente $k$ a la tensión $U_\mathrm{AB}$, sin unidad: es cuántos voltios cambia $U_\mathrm{AB}$ por cada voltio de la fuente. También se llama __sensibilidad__. $Z_k$ en $\Omega$ es la resistencia de transferencia (la transimpedancia) de una fuente de corriente a esta tensión. De forma análoga, $Y_k$ en S y la ganancia de corriente $b_k$ describen la corriente entre dos nudos C y D. $U_\mathrm{AB}$ e $I_\mathrm{CD}$ representan cualquier tensión y cualquier corriente de la red. **Validez:** solo para redes lineales y solo para tensiones y corrientes.

**El procedimiento.**

<ol>

<li>

Desactivar todas las fuentes menos una. Una fuente de tensión ideal con valor cero impone potenciales iguales en sus terminales, y eso lo hace un cable: se convierte en un **cortocircuito**. Una fuente de corriente ideal con valor cero impone corriente cero, y eso lo hace un hueco: se convierte en **terminales abiertos**. Las resistencias internas de las fuentes reales permanecen en la red.

</li>

<li>

Calcular el efecto parcial de esa única fuente. Normalmente solo queda un divisor de tensión o de corriente.

</li>

<li>

Repetir para cada fuente y sumar todos los efectos parciales con su signo correcto.

</li>

</ol>

:::abbildung et1/k5ueberlagerung 9
La red N y sus dos circuitos parciales. Centro: la fuente de corriente está abierta y queda un divisor de tensión. Derecha: la fuente de tensión es un cable, y la fuente de corriente alimenta $R_1$ y $R_2$ en paralelo. Los terminales A y B están abiertos.
:::

**Ejemplo.** Se busca $U_\mathrm{AB}$ en N con los terminales abiertos (fig. [9](#abb-9)). Circuito parcial 1: divisor de tensión, $U'=\frac{R_2}{R_1+R_2}\,U_\mathrm{q1}=\frac13\cdot18\,\mathrm{V}=6$ V. Circuito parcial 2: $U''=(R_1\parallel R_2)\,I_\mathrm{q2}=2\,\Omega\cdot1{,}5\,\mathrm{A}=3$ V. Suma: $U_\mathrm{AB}=9$ V. Los coeficientes son, por tanto, $a=\frac13$ para $U_\mathrm{q1}$ y $Z=2\,\Omega$ para $I_\mathrm{q2}$. **Comprobación** con la ley de los nudos en A: por $R_1$ llegan $(18-9)\,\mathrm{V}/6\,\Omega=1{,}5$ A, más 1,5 A de la fuente de corriente, y por $R_2$ salen $9\,\mathrm{V}/3\,\Omega=3$ A. También las corrientes de rama se superponen: en $R_1$ circulan $2$ A del circuito parcial 1 y $-0{,}5$ A del circuito parcial 2. **Caso límite:** Si se duplican ambas fuentes, $U_\mathrm{AB}$ se duplica a 18 V, porque los coeficientes no cambian.

:::herleitung Los coeficientes de N
Con los terminales abiertos, la ley de los nudos en A dice $(U_\mathrm{q1}-U_\mathrm{AB})/R_1+I_\mathrm{q2}=U_\mathrm{AB}/R_2$. Despejando la tensión buscada:

$$U_\mathrm{AB}=\frac{R_2}{R_1+R_2}\,U_\mathrm{q1}+\frac{R_1R_2}{R_1+R_2}\,I_\mathrm{q2}.$$

Esta es la forma [(8.1)](#gl-8-1): cada sumando pertenece a una fuente, y los coeficientes solo contienen resistencias.
:::

**El límite: la potencia.** La potencia en una resistencia es cuadrática en la tensión, $P=UI=U^2/R$ ([Parte 7](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/leistung-anpassung-und-wirkungsgrad/leistung-und-anpassung.html)). En $R_2$, sumar daría $(6\,\mathrm{V})^2/3\,\Omega+(3\,\mathrm{V})^2/3\,\Omega=15$ W. Lo cierto son $(9\,\mathrm{V})^2/3\,\Omega=27$ W. Falta el término cruzado $2U'U''/R_2=12$ W. Las potencias no se pueden superponer; las tensiones y las corrientes, sí. Más adelante llega una excepción: con magnitudes alternas de distinta frecuencia, el término cruzado desaparece en la media temporal. Tampoco vale la superposición en cuanto hay un diodo en la red ([Parte 9](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden/halbleiter-und-dioden.html)).

:::frage ¿Por qué no puedo sacar de la red una fuente de tensión desactivada?
Porque cero voltios no se convierten en «nada». La fuente sigue siendo parte de la línea; solo que ya no mantiene ninguna tensión. Si se saca, se interrumpe el camino de la corriente a través de ella. Ese sería el caso de la fuente de corriente, no el de la fuente de tensión.
:::

:::aufgabe Ejercicio 9 ★★ Dos fuentes, un consumidor
<span class="anker" id="aufg-9"></span>

Del nudo C salen tres ramas hacia la masa común: $R_3=4\,\Omega$ directamente, $R_\mathrm{s}=2\,\Omega$ en serie con $U_\mathrm{s}=12$ V y $R_\mathrm{t}=4\,\Omega$ en serie con $U_\mathrm{t}=6$ V (ambos polos positivos apuntan hacia C). (a) Calcula la tensión $U_3$ en $R_3$ por superposición y en general como fórmula. Comprueba con la ley de los nudos. (b) Compara la potencia real en $R_3$ con la suma de las potencias parciales. (c) ¿Cuánto vale la sensibilidad de $U_3$ respecto a $U_\mathrm{t}$? ¿Qué resulta con ella para $U_\mathrm{t}=8$ V, sin recalcularlo todo?

:::loesung
(a) $U_\mathrm{t}$ desactivada: $R_\mathrm{t}\parallel R_3=2\,\Omega$, divisor $U_3'=\frac{2}{2+2}\cdot12\,\mathrm{V}=6$ V. $U_\mathrm{s}$ desactivada: $R_\mathrm{s}\parallel R_3=\frac43\,\Omega$, divisor $U_3''=\frac{4/3}{4+4/3}\cdot6\,\mathrm{V}=1{,}5$ V. Por tanto, $U_3=7{,}5$ V. En general:

$$U_3=\frac{R_\mathrm{t}R_3}{R_\mathrm{s}R_\mathrm{t}+R_3(R_\mathrm{s}+R_\mathrm{t})}\,U_\mathrm{s}+\frac{R_\mathrm{s}R_3}{R_\mathrm{s}R_\mathrm{t}+R_3(R_\mathrm{s}+R_\mathrm{t})}\,U_\mathrm{t}.$$

Ley de los nudos: $\frac{12-7{,}5}{2}\,\mathrm{A}+\frac{6-7{,}5}{4}\,\mathrm{A}=2{,}25\,\mathrm{A}-0{,}375\,\mathrm{A}=1{,}875$ A, y $7{,}5\,\mathrm{V}/4\,\Omega=1{,}875$ A. La fuente de 6 V absorbe corriente.

(b) Potencias parciales: 9 W y 0,5625 W, suma 9,56 W. Real: $(7{,}5\,\mathrm{V})^2/4\,\Omega=14{,}06$ W.

(c) $a_\mathrm{t}=\frac{1{,}5\,\mathrm{V}}{6\,\mathrm{V}}=\frac14$. Para 8 V: $U_3=6\,\mathrm{V}+\frac14\cdot8\,\mathrm{V}=8$ V.
:::
:::

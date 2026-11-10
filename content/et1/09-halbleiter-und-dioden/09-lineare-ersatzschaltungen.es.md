---
title: Etapa 7: Circuitos equivalentes lineales
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / Semiconductores y diodos
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden
knoten: Capítulo 9: Semiconductores y diodos
order: 1190900
summary: Con varios diodos se acoplan varias ecuaciones exponenciales, y a mano ya no es posible.
tags: Diodo ideal, Diodo con tensión directa, tensión directa
lang: es
---

<span class="anker" id="stufe-7"></span>

:::zweck
Con varios diodos se acoplan varias ecuaciones exponenciales, y a mano ya no es posible. Esta etapa sustituye el diodo por partes lineales y da un procedimiento que siempre funciona.
:::

**La idea.** A lo largo de tres décadas de corriente, $U_\mathrm D$ cambia solo 180 mV. Así que la curva característica es casi un ángulo recto, y el componente casi un interruptor. El precio del modelo: hay que conocer el estado de conmutación de cada diodo. Se supone y se comprueba después.

:::abbildung et1/k9ersatz 9
Arriba a la izquierda: curva característica real (azul), diodo ideal (verde) y modelo con $U_\mathrm F=0{,}7$ V (rojo). Arriba a la derecha: los circuitos equivalentes de ambos modelos en estado de conducción y de bloqueo. Abajo: ejemplo con dos diodos y su resultado.
:::

:::definition Definición 7.1 (Dos modelos de diodo)
<span class="anker" id="satz-7-1"></span>

__Diodo ideal__: en conducción, un cortocircuito; en bloqueo, un circuito abierto.

<span class="anker" id="gl-7-1"></span>
$$I_\mathrm D>0\ \Rightarrow\ U_\mathrm D=0,\qquad U_\mathrm D<0\ \Rightarrow\ I_\mathrm D=0. \tag{7.1}$$

__Diodo con tensión directa__: en conducción, una fuente de tensión $U_\mathrm F$; en bloqueo, un circuito abierto.

<span class="anker" id="gl-7-2"></span>
$$I_\mathrm D>0\ \Rightarrow\ U_\mathrm D=U_\mathrm F,\qquad U_\mathrm D<U_\mathrm F\ \Rightarrow\ I_\mathrm D=0. \tag{7.2}$$
:::

⁠**Cómo leerlo:** $U_\mathrm F$ se llama __tensión directa__, también caída directa. No es un valor del material como $U_\mathrm{D0}$ ni un umbral, sino un valor del modelo: se elige la tensión a la corriente esperada. Lo habitual es 0,6 V o 0,7 V. El diodo del modelo tiene 0,6 V a 0,12 mA y 0,7 V a 5,8 mA. **Validez:** En el modelo de referencia, exactamente $I=4{,}31$ mA. El diodo ideal da 5,00 mA (16 % de más), $U_\mathrm F=0{,}7$ V da 4,30 mA ($-0{,}2$ %), $U_\mathrm F=0{,}6$ V da 4,40 mA (2 % de más). El diodo ideal solo basta cuando las tensiones del circuito son grandes frente a 0,7 V.

**El procedimiento.**

<ol>

<li>

Elige un circuito equivalente para los diodos.

</li>

<li>

Supón de forma plausible qué diodo conduce y cuál bloquea.

</li>

<li>

Sustituye los diodos y calcula todas las corrientes y tensiones.

</li>

<li>

Comprueba: los diodos que conducen necesitan $I_\mathrm D>0$, los que bloquean $U_\mathrm D<U_\mathrm F$. Si hay una contradicción, elige una nueva suposición.

</li>

</ol>

$n$ diodos tienen $2^n$ combinaciones, así que compensa una buena primera suposición. Ayuda echar un vistazo a los potenciales.

::::beispiel
Fig. [9](#abb-9) abajo: 5 V y 2 V alimentan el nudo X, cada una a través de 1 k$\Omega$ y un diodo; de allí $R_3=2\,\mathrm{k\Omega}$ va a masa. $U_\mathrm F=0{,}7$ V.

⁠*Suposición 1: ambos conducen.* La ley de los nudos ([capítulo 2](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)) en X es $(4{,}3\,\mathrm{V}-\varphi_\mathrm X)/R_1+(1{,}3\,\mathrm{V}-\varphi_\mathrm X)/R_2=\varphi_\mathrm X/R_3$. De ello resulta $\varphi_\mathrm X=2{,}24$ V, $I_\mathrm{D1}=2{,}06$ mA e $I_\mathrm{D2}=-0{,}94$ mA. La corriente negativa es una contradicción.

⁠*Suposición 2: D$_1$ conduce, D$_2$ bloquea.* Entonces $I=(5\,\mathrm{V}-0{,}7\,\mathrm{V})/3\,\mathrm{k\Omega}=1{,}43$ mA y $\varphi_\mathrm X=2{,}87$ V. En D$_2$ hay $U_\mathrm{D2}=2\,\mathrm{V}-2{,}87\,\mathrm{V}=-0{,}87$ V. Eso es menor que $U_\mathrm F$, sin contradicción. Los PT son D$_1$ (0,7 V | 1,43 mA) y D$_2$ ($-0{,}87$ V | 0). La simulación completa da 2,89 V y 1,45 mA.

⁠*Vista de los potenciales:* D$_2$ solo conduce si $\varphi_\mathrm X<2\,\mathrm{V}-0{,}7\,\mathrm{V}=1{,}3$ V. La fuente de 5 V por sí sola ya eleva X a 2,87 V, así que el cátodo de D$_2$ está por encima del ánodo. La tensión más alta se impone. La suposición 3 (solo conduce D$_2$) daría $U_\mathrm{D1}=4{,}13$ V, la suposición 4 (ambos bloquean) $U_\mathrm{D1}=5$ V, ambas mayores que $U_\mathrm F$ y, por tanto, contradicciones.
::::

⁠**Caso límite:** Con $U_2=5$ V, las dos ramas son iguales y cada diodo lleva la mitad.

:::frage ¿Por qué es una contradicción una corriente negativa? Una fuente de tensión sí puede absorber corriente.
La fuente equivalente sí, el diodo no: en sentido inverso solo circula $I_\mathrm S$. El modelo solo vale para $I_\mathrm D>0$. Un resultado negativo muestra que el cálculo ha usado el diodo fuera de este rango.
:::

:::aufgabe Ejercicio 8 ★★ ¿Quién gana?
<span class="anker" id="aufg-8"></span>

En el ejemplo, la fuente de 2 V pasa a ser la fuente $U_2$.

<ol class="al">

<li>

Sea $U_2=4{,}5$ V. ¿Qué diodos conducen? Calcula $\varphi_\mathrm X$ y todas las corrientes de los diodos.

</li>

<li>

¿A partir de qué $U_2$ empieza a conducir D$_2$?

</li>

</ol>

:::loesung
(a) Suposición: ambos conducen. $(4{,}3\,\mathrm{V}-\varphi_\mathrm X)/R_1+(3{,}8\,\mathrm{V}-\varphi_\mathrm X)/R_2=\varphi_\mathrm X/R_3$ da $\varphi_\mathrm X=3{,}24$ V, $I_\mathrm{D1}=1{,}06$ mA, $I_\mathrm{D2}=0{,}56$ mA. Ambas positivas, sin contradicción. Comprobación: $1{,}62\,\mathrm{mA}\cdot2\,\mathrm{k\Omega}=3{,}24$ V. (b) Mientras D$_2$ bloquea, $\varphi_\mathrm X=2{,}87$ V. D$_2$ empieza a conducir cuando $U_2-0{,}7\,\mathrm{V}=2{,}87$ V, es decir, con $U_2=3{,}57$ V.
:::
:::

:::aufgabe Ejercicio 9 ★★★ Diodos de protección
<span class="anker" id="aufg-9"></span>

La entrada de un chip es el nudo X. Una tensión $U_\mathrm e$ lo alimenta a través de $R=1\,\mathrm{k\Omega}$. D$_1$ va de X (ánodo) a la alimentación $+5$ V. D$_2$ va de masa (ánodo) a X. $U_\mathrm F=0{,}7$ V.

<ol class="al">

<li>

Determina para $U_\mathrm e=3$ V, $12$ V y $-3$ V qué diodo conduce, así como $\varphi_\mathrm X$ y la corriente por $R$.

</li>

<li>

Dibuja $\varphi_\mathrm X$ frente a $U_\mathrm e$.

</li>

<li>

¿Por qué se descarta una de las cuatro combinaciones sin calcular?

</li>

</ol>

:::loesung
(a) $U_\mathrm e=3$ V: no conduce ningún diodo, $I=0$, $\varphi_\mathrm X=3$ V. Comprobación: $U_\mathrm{D1}=-2$ V, $U_\mathrm{D2}=-3$ V. $U_\mathrm e=12$ V: D$_1$ conduce, $\varphi_\mathrm X=5{,}7$ V, $I=6{,}3$ mA fluye hacia la alimentación. $U_\mathrm e=-3$ V: D$_2$ conduce, $\varphi_\mathrm X=-0{,}7$ V, $I=-2{,}3$ mA, la corriente viene de masa. (b) Una rampa $\varphi_\mathrm X=U_\mathrm e$ entre $-0{,}7$ V y 5,7 V, horizontal fuera de ese intervalo: la entrada queda protegida. (c) Si ambos condujeran, $\varphi_\mathrm X$ tendría que ser 5,7 V y $-0{,}7$ V a la vez.
:::
:::

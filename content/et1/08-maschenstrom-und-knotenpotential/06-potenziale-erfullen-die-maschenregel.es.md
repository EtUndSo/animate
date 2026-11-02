---
title: Etapa 4: Los potenciales cumplen la ley de las mallas
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / Análisis por mallas y por nudos
order: 1180600
summary: De z tensiones solo k-1 son libres.
tags: 
lang: es
---

<span class="anker" id="stufe-4"></span>

:::zweck
De $z$ tensiones solo $k-1$ son libres. Esta etapa muestra por qué los potenciales de los nudos asumen ese papel y por qué la ley de las mallas se cumple entonces por sí sola.
:::

**La idea.** Cada nudo tiene un potencial ([Parte 1](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)), como cada punto de un paisaje tiene una altura. La tensión de una rama es la diferencia de altura entre sus extremos. Quien camina en círculo vuelve a la altura de partida, sean cuales sean las alturas asignadas a los nudos (fig. [4](#abb-4)). Así, la ley de las mallas no se puede violar. Como solo cuentan las diferencias, una altura se puede fijar libremente. Eso ahorra una incógnita, y quedan $k-1$.

:::abbildung et1/k8hoehen 4
Los nudos de la red modelo como alturas. La vuelta de 0 por 1 y 2 de regreso a 0 sube 8 V y 2 V y baja 10 V. La suma es cero, y seguiría siendo cero si las alturas 1 y 2 se desplazaran arbitrariamente.
:::

:::definition Definición 4.1 (Nudo de referencia y potencial de nudo)
<span class="anker" id="satz-4-1"></span>

Un nudo 0 elegido libremente es el *nudo de referencia*; su potencial es $\varphi_0=0$. El *potencial de nudo* de otro nudo $\mu$ es su tensión respecto al nudo de referencia:

<span class="anker" id="gl-4-1"></span>
$$U_\mu=\varphi_\mu-\varphi_0. \tag{4.1}$$

La tensión de una rama entre los nudos $\mu$ y $\nu$ es $U_{\mu\nu}=U_\mu-U_\nu$; hacia el nudo de referencia, $U_{\mu0}=U_\mu$.
:::

:::satz Teorema 4.2 (Potenciales de nudo)
<span class="anker" id="satz-4-2"></span>

Para valores cualesquiera de los $k-1$ potenciales de nudo se cumple toda ley de las mallas. A la inversa, a toda distribución de tensión que cumpla la ley de las mallas le corresponde exactamente un conjunto de potenciales de nudo.
:::

:::herleitung Por qué esto siempre funciona
⁠*Ley de las mallas.* A lo largo de una malla por los nudos $1,2,\dots,N$ se tiene $(U_1-U_2)+(U_2-U_3)+\dots+(U_N-U_1)=0$. Cada potencial aparece una vez con $+$ y una vez con $-$.

⁠*Completitud.* Se elige un árbol. En él hay exactamente un camino entre el nudo de referencia y cada nudo. La suma de las tensiones de rama a lo largo de ese camino define de forma unívoca el potencial de nudo. Con ello son correctas todas las diferencias en las ramas del árbol. Para cada rama de enlace es correcta porque cierra con ramas del árbol una malla cuya ley se cumple por hipótesis.
:::

⁠**Cómo leerlo:** $U_\mu$ es una tensión con flecha del nudo $\mu$ al nudo de referencia, unidad voltio. En el esquema, el símbolo de masa indica el nudo de referencia; en SPICE siempre se llama 0. El nudo de referencia se elige donde confluyen más ramas; así las ecuaciones son más cortas. **Validez:** El campo debe ser irrotacional. Un campo magnético variable a través de una malla destruye los potenciales ([Parte 1](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)); en los circuitos está en las bobinas.

**Ejemplo.** En la red modelo, $U_1=8$ V y $U_2=10$ V, como dio la etapa [3](das-maschenstromverfahren.html#stufe-3). La tensión en $R_3$ es $U_{12}=U_1-U_2=-2$ V, así que el nudo 2 está más alto y la corriente va de 2 a 1. Con $R_3=2\,\mathrm{k\Omega}$ son los 1 mA de la etapa [3](das-maschenstromverfahren.html#stufe-3). La vuelta da $(U_1-U_2)+U_2-U_1=0$ también para cualquier otro par de números. **Caso límite:** Una red con $k=2$ tiene un solo potencial de nudo. Es la tensión común de una conexión en paralelo.

:::frage ¿El potencial de nudo es entonces un potencial o una tensión?
Ambas cosas. Un potencial por sí solo tiene valor únicamente respecto a un punto cero ([Parte 1](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)). El potencial de nudo es la tensión respecto al punto cero elegido; por eso lleva el símbolo $U$. Un cambio de nudo de referencia cambia todos los potenciales de nudo, pero ni una sola tensión de rama.
:::

:::aufgabe Ejercicio 5 ★ Cambiar la referencia
<span class="anker" id="aufg-5"></span>

Elige en la red modelo el nudo 2 como nudo de referencia. (a) ¿Qué potenciales de nudo tienen la línea inferior y el nudo 1? (b) Calcula a partir de ellos la tensión entre el nudo 1 y la línea inferior. (c) ¿Por qué no cambia ninguna corriente?

:::loesung
(a) Todos los potenciales bajan 10 V: línea inferior $-10$ V, nudo 1 $-2$ V, nudo 2 0 V.

(b) $-2\,\mathrm{V}-(-10\,\mathrm{V})=8$ V, como antes.

(c) Las corrientes solo dependen de las diferencias, y estas no cambian.
:::
:::

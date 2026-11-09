---
title: Etapa 2: Las corrientes de malla cumplen la ley de los nudos
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / Análisis por mallas y por nudos
order: 1180400
summary: Se buscan m magnitudes de las que se deduzcan todas las corrientes de rama.
tags: ventanas
lang: es
---

<span class="anker" id="stufe-2"></span>

:::zweck
Se buscan $m$ magnitudes de las que se deduzcan todas las corrientes de rama. Esta etapa muestra por qué las corrientes circulantes lo consiguen y por qué la ley de los nudos se cumple entonces por sí sola.
:::

**La idea.** Se imagina en cada malla independiente una corriente propia que da vueltas en círculo (fig. [2](#abb-2)). El mecanismo está en la palabra círculo: si la corriente entra en un nudo por una rama, sale de él por otra rama de la misma malla. No aporta nada al nudo. Esto vale para cada corriente circulante, en cada nudo y para cada valor numérico. En una rama que pertenece a dos mallas se superponen ambas corrientes circulantes. Solo se mide esa suma.

:::analogie
Dos líneas circulares de autobús comparten una calle. Por la calle común pasan los autobuses de ambas líneas, y cada línea que entra en un cruce vuelve a salir de él. La analogía termina en lo individual: un electrón no pertenece a ninguna malla. Las corrientes de malla son magnitudes de cálculo; lo que circula de verdad es solo la corriente de rama.
:::

:::abbildung et1/k8kreis 2
El nudo 1 con las corrientes de malla I y II. Izquierda: cada corriente circulante atraviesa el nudo. Derecha: la misma situación como corrientes de rama. Hacia el nudo fluye $I_\mathrm I$; salen $I_\mathrm I-I_\mathrm{II}$ e $I_\mathrm{II}$. La suma es cero para todos los valores.
:::

:::satz Teorema 2.1 (Corrientes de malla)
<span class="anker" id="satz-2-1"></span>

Si en cada una de $m$ mallas independientes se pone una *corriente de malla* $I_\mu$ con sentido elegido libremente, la corriente de una rama es

<span class="anker" id="gl-2-1"></span>
$$I_\mathrm{rama}=\sum_{\mu=1}^{m}\sigma_\mu\,I_\mu,\qquad\sigma_\mu=\begin{cases}+1&\text{la malla }\mu\text{ va en el sentido de la flecha de la rama,}\\-1&\text{la malla }\mu\text{ va contra la flecha,}\\0&\text{la malla }\mu\text{ no contiene la rama.}\end{cases} \tag{2.1}$$

La ley de los nudos se cumple entonces para todos los valores de las $I_\mu$. A la inversa, toda distribución de corriente que cumpla la ley de los nudos se puede representar así.
:::

:::herleitung Por qué esto siempre funciona
⁠*Ley de los nudos.* En una malla, cada nudo está unido exactamente a dos ramas ([Parte 2](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)). Su corriente cuenta en el nudo una vez como entrante y una vez como saliente, y las contribuciones se cancelan.

⁠*Completitud.* Se elige un árbol. Cada rama de enlace cierra exactamente una malla; como corriente de esa malla se toma la corriente de la rama de enlace. Si se restan todas esas corrientes circulantes de la distribución dada, el resto sigue cumpliendo la ley de los nudos y es cero en todas las ramas de enlace. Solo puede circular por el árbol. Pero el árbol tiene un extremo, un nudo con una sola rama del árbol. Allí la ley de los nudos impone corriente cero. Se elimina esa rama y se repite. El resto es cero en todas partes.
:::

⁠**Cómo leerlo:** $\mu$ numera las mallas, en los ejemplos con números romanos. El sentido es libre; un valor negativo significa que la corriente circulante gira al revés. **Validez:** Las mallas deben ser independientes. Si la red se puede dibujar sin cruces, se eligen las __ventanas__, las superficies entre las ramas. Al construir desde el árbol, cada nueva rama de enlace divide exactamente una superficie en dos, así que hay exactamente $m$ ventanas.

::::beispiel
Si en la red modelo se agrupan la fuente de corriente y $R_5$ en una rama con fuente de tensión (etapa [3](das-maschenstromverfahren.html#stufe-3)), quedan tres ventanas I, II, III con corrientes de malla en sentido horario. De ellas se deducen las cinco corrientes de rama:

| Rama | izquierda, $R_1$ | $R_2$ | $R_3$ | $R_4$ | derecha, $R_5$ |
|---|---|---|---|---|---|
| Corriente | $I_\mathrm I$ | $I_\mathrm I-I_\mathrm{II}$ | $I_\mathrm{II}$ | $I_\mathrm{II}-I_\mathrm{III}$ | $I_\mathrm{III}$ |

En el nudo 1 esto da $I_\mathrm I-(I_\mathrm I-I_\mathrm{II})-I_\mathrm{II}=0$, sean cuales sean los valores de las corrientes.
::::

⁠**Casos límite:** Para $m=1$, la corriente de malla es la corriente de la conexión en serie. Para $I_\mathrm{II}=0$ desaparece la corriente en $R_3$; las mitades izquierda y derecha no intercambian nada.

:::frage ¿Qué mide un amperímetro en la rama de $R_2$, $I_\mathrm I$ o $I_\mathrm{II}$?
Ninguna de las dos, sino la corriente de rama $I_\mathrm I-I_\mathrm{II}$. Una corriente de malla solo se puede medir directamente donde circula sola, aquí por ejemplo $I_\mathrm I$ en $R_1$. Esa es la idea del árbol: la corriente de malla es la corriente de una rama que pertenece solo a esa malla.
:::

:::aufgabe Ejercicio 2 ★ De la corriente de malla a la corriente de rama
<span class="anker" id="aufg-2"></span>

Dos mallas comparten la resistencia vertical $R_\mathrm g=3\,\mathrm{k\Omega}$; la malla a está a su izquierda, la malla b a su derecha. Por lo demás, a solo contiene una fuente y $R_\mathrm a=2\,\mathrm{k\Omega}$, y b solo una fuente y $R_\mathrm b=1\,\mathrm{k\Omega}$. Ambas corrientes de malla van en sentido horario, $I_\mathrm a=3$ mA, $I_\mathrm b=-1$ mA.

<ol class="al">

<li>

¿Cuánto vale la corriente en $R_\mathrm g$ en el sentido de $I_\mathrm a$?

</li>

<li>

Comprueba la ley de los nudos en el extremo superior de $R_\mathrm g$.

</li>

<li>

¿Qué tensión debe impulsar la fuente de cada malla en el sentido de recorrido?

</li>

</ol>

:::loesung
(a) En la rama común, los dos círculos en sentido horario van uno contra otro: $I_\mathrm a-I_\mathrm b=3-(-1)=4$ mA en el sentido de $I_\mathrm a$.

(b) Si $R_\mathrm g$ está en vertical entre las mallas, arriba $I_\mathrm a$ va hacia el nudo e $I_\mathrm b$ se aleja de él. Salen $I_\mathrm a-I_\mathrm b$ hacia abajo e $I_\mathrm b$ hacia la derecha: $3-4-(-1)=0$.

(c) Malla a: $R_\mathrm a\,I_\mathrm a+R_\mathrm g\,(I_\mathrm a-I_\mathrm b)=6+12=18$ V. Malla b: $R_\mathrm b\,I_\mathrm b+R_\mathrm g\,(I_\mathrm b-I_\mathrm a)=-1-12=-13$ V. La fuente de b impulsa, por tanto, con 13 V en sentido antihorario.
:::
:::

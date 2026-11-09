---
title: Etapa 9: Thévenin y Norton
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / Fuentes y fuentes equivalentes
order: 1151100
summary: N debe alimentar muchas cargas distintas.
tags: fuente de tensión equivalente, fuente de corriente equivalente, característica de carga
lang: es
---

<span class="anker" id="stufe-9"></span>

:::zweck
N debe alimentar muchas cargas distintas. Hasta ahora habría que recalcular toda la red para cada carga. Esta etapa sustituye la red por una recta, y de una vez por todas.
:::

**La idea.** Imaginemos la carga sustituida por una fuente de corriente que extrae de la red exactamente la corriente $I_\mathrm{A}$. La red no nota ninguna diferencia, porque en los terminales solo percibe esta corriente. Ahora contiene solo resistencias y fuentes, así que la superposición está permitida. Por tanto, $U_\mathrm{AB}$ consta de dos partes: la contribución de las fuentes internas, que no depende de la corriente, y la contribución de $I_\mathrm{A}$, que es proporcional a ella. Una constante menos un factor por la corriente es una recta. Esa es toda la razón por la que una red lineal parece una recta desde fuera.

:::satz Teorema 9.1 (Fuentes equivalentes: Thévenin y Norton)
<span class="anker" id="satz-9-1"></span>

Todo monopuerto lineal se comporta en sus terminales como una __fuente de tensión equivalente__ y también como una __fuente de corriente equivalente__:

<span class="anker" id="gl-9-1"></span>
$$U_\mathrm{AB}=U_\mathrm{i}-R_\mathrm{i}\,I_\mathrm{A},\qquad\qquad I_\mathrm{A}=I_\mathrm{i}-G_\mathrm{i}\,U_\mathrm{AB}, \tag{9.1}$$

con

<span class="anker" id="gl-9-2"></span>
$$U_\mathrm{i}=U_\mathrm{CA},\qquad I_\mathrm{i}=I_\mathrm{CC},\qquad R_\mathrm{i}=\frac{1}{G_\mathrm{i}}=\frac{U_\mathrm{CA}}{I_\mathrm{CC}}. \tag{9.2}$$
:::

⁠**Cómo leerlo:** La primera forma lleva el nombre de Thévenin; la segunda, el de Norton. $U_\mathrm{CA}$ es la tensión con los terminales abiertos, $I_\mathrm{CC}$ la corriente por los terminales cortocircuitados. $R_\mathrm{i}$ es la misma en ambas formas. La recta se llama también __característica de carga__. Con $R_\mathrm{i}$ pequeña se suele elegir la forma de Thévenin; con $R_\mathrm{i}$ grande, la de Norton (etapa [6](spannungsquelle-oder-stromquelle.html#stufe-6)). **Validez:** El monopuerto debe ser lineal, la carga no. El enunciado solo vale para los terminales; no dice nada sobre las potencias en el interior (etapa [6](spannungsquelle-oder-stromquelle.html#stufe-6)).

:::herleitung La recta a partir de la superposición
Con la fuente de corriente imaginada $I_\mathrm{A}$ en los terminales, según [(8.1)](uberlagerung.html#gl-8-1) se cumple

$$U_\mathrm{AB}=\underbrace{\sum_k a_kU_{\mathrm{q}k}+\sum_k Z_kI_{\mathrm{q}k}}_{\text{fuentes internas}}\;\underbrace{-\,R_\mathrm{i}I_\mathrm{A}}_{\text{corriente en los terminales}}.$$

Para $I_\mathrm{A}=0$ queda la primera parte, que es por tanto $U_\mathrm{CA}$. Si se desactivan todas las fuentes internas, queda la segunda parte: ahí, $R_\mathrm{i}$ es la resistencia total de la red desactivada entre A y B. El signo menos procede de la flecha de referencia: $I_\mathrm{A}$ sale de A, es decir, en el interior va de B a A, y A queda más abajo. De $U_\mathrm{AB}=0$ se deduce $I_\mathrm{A}=I_\mathrm{CC}=U_\mathrm{CA}/R_\mathrm{i}$. Reordenando se obtiene la segunda forma.
:::

**Tres caminos hacia los dos números.**

<ol>

<li>

⁠**Circuito abierto y cortocircuito:** calcular o medir $U_\mathrm{CA}$ e $I_\mathrm{CC}$; $R_\mathrm{i}$ se deduce de [(9.2)](#gl-9-2).

</li>

<li>

⁠**Desactivar las fuentes:** fuentes de tensión como cables, fuentes de corriente como huecos, y luego determinar la resistencia total entre A y B. Esa es $R_\mathrm{i}$. Además, una de las dos magnitudes $U_\mathrm{CA}$ o $I_\mathrm{CC}$.

</li>

<li>

⁠**Dos casos de carga:** Si no se puede cortocircuitar, se miden con dos cargas los puntos $(I_\mathrm{x},U_\mathrm{x})$ e $(I_\mathrm{y},U_\mathrm{y})$. Ambos están en la recta, $U_\mathrm{x}=U_\mathrm{i}-R_\mathrm{i}I_\mathrm{x}$ y $U_\mathrm{y}=U_\mathrm{i}-R_\mathrm{i}I_\mathrm{y}$. Restar y sustituir da

<span class="anker" id="gl-9-3"></span>
$$R_\mathrm{i}=-\frac{U_\mathrm{x}-U_\mathrm{y}}{I_\mathrm{x}-I_\mathrm{y}},\qquad U_\mathrm{i}=U_\mathrm{x}+R_\mathrm{i}I_\mathrm{x}=\frac{U_\mathrm{x}I_\mathrm{y}-U_\mathrm{y}I_\mathrm{x}}{I_\mathrm{y}-I_\mathrm{x}}. \tag{9.3}$$

</li>

</ol>

:::abbildung et1/k5ersatz 10
A la izquierda, la red N; a la derecha, sus dos fuentes equivalentes. En los terminales, las tres son indistinguibles.
:::

::::beispiel
Para N, $U_\mathrm{CA}=9$ V se conoce de la etapa [8](uberlagerung.html#stufe-8). En el cortocircuito, $R_2$ queda entre dos terminales unidos y no conduce corriente. La fuente de tensión impulsa $U_\mathrm{q1}/R_1=3$ A por los terminales; la fuente de corriente, 1,5 A: $I_\mathrm{CC}=U_\mathrm{q1}/R_1+I_\mathrm{q2}=4{,}5$ A. De ahí se deduce $R_\mathrm{i}=9\,\mathrm{V}/4{,}5\,\mathrm{A}=2\,\Omega$. El segundo camino lo confirma: desactivadas las fuentes, $R_1$ y $R_2$ están en paralelo, $6\,\Omega\parallel3\,\Omega=2\,\Omega$. La forma de Norton tiene $I_\mathrm{i}=4{,}5$ A y $G_\mathrm{i}=0{,}5$ S (fig. [10](#abb-10)).

Estos son exactamente los números de la batería de la etapa [5](reale-quellen-und-der-arbeitspunkt.html#stufe-5). Sin volver a mirar la red, para 16 $\Omega$ resulta $I_\mathrm{A}=9\,\mathrm{V}/18\,\Omega=0{,}5$ A y $U_\mathrm{AB}=8$ V. **Comprobación** en el original: por $R_1$ llegan $(18-8)\,\mathrm{V}/6\,\Omega=1{,}667$ A, más 1,5 A, lo que hace 3,167 A. De ellos, $R_2$ toma la mayor parte con $8\,\mathrm{V}/3\,\Omega=2{,}667$ A, y 0,5 A van a la carga. Si fuera $I_\mathrm{q2}=0$, quedaría el divisor de tensión del circuito parcial 1 con $U_\mathrm{i}=\frac{R_2}{R_1+R_2}U_\mathrm{q1}=6$ V, $I_\mathrm{i}=U_\mathrm{q1}/R_1=3$ A y $R_\mathrm{i}=R_1\parallel R_2$ sin cambios.

:::abbildung et1/k5geraden 11
Las curvas características de N con una fuente y con las dos. Cada fuente desplaza la recta en paralelo hacia arriba; la pendiente $R_\mathrm{i}=2\,\Omega$ se mantiene, porque solo depende de las resistencias. La suma de 6 V y 3 V y la suma de 3 A y 1,5 A son la superposición.
:::
::::

::::beispiel [Segundo ejemplo] una fuente de corriente real
Una fuente de corriente ideal $I_\mathrm{q}=3$ A con $R_\mathrm{q}=20\,\Omega$ en paralelo alimenta el terminal A a través de $R_\mathrm{v}=10\,\Omega$. Su otro polo es B, y entre A y B hay $R_\mathrm{p}=30\,\Omega$. En cortocircuito, $R_\mathrm{p}$ queda puenteada, y el divisor de corriente da $I_\mathrm{CC}=I_\mathrm{q}\frac{R_\mathrm{q}}{R_\mathrm{q}+R_\mathrm{v}}=2$ A. En circuito abierto, $R_\mathrm{v}$ y $R_\mathrm{p}$ están en serie. Conducen $I_\mathrm{q}\frac{R_\mathrm{q}}{R_\mathrm{q}+R_\mathrm{v}+R_\mathrm{p}}=1$ A, así que $U_\mathrm{CA}=R_\mathrm{p}\cdot1\,\mathrm{A}=30$ V. El cociente es $R_\mathrm{i}=15\,\Omega$. Al desactivarla, la fuente de corriente se convierte en un hueco, y su resistencia en paralelo permanece: $R_\mathrm{i}=R_\mathrm{p}\parallel(R_\mathrm{q}+R_\mathrm{v})=15\,\Omega$, o como conductancia $G_\mathrm{i}=G_\mathrm{p}+\frac{1}{R_\mathrm{q}+R_\mathrm{v}}$.
::::

⁠**Casos límite:** Si una fuente de tensión ideal está directamente en los terminales, $R_\mathrm{i}=0$ y la forma de Norton no existe. Si una fuente de corriente ideal está en serie con un terminal, $R_\mathrm{i}=\infty$ y la forma de Thévenin no existe. Si las fuentes se anulan exactamente, $U_\mathrm{CA}=0$ e $I_\mathrm{CC}=0$. Entonces el cociente falla, pero el camino 2 sigue dando $R_\mathrm{i}$.

:::ltspice Red y fuente equivalente una al lado de la otra
⁠**Esquema:** N con `voltage` 18, `res` 6 y `res` 3, la fuente de corriente con 1.5 de masa a `a`. Al lado, por separado, la fuente equivalente con `voltage` 9 y `res` 2 hasta el nudo `b`. En `a` y en `b`, una fuente de corriente `current` con el valor `{IZ}` a masa.

⁠**Directivas:** `.param IZ=0`, `.step param IZ list 0 0.5 2.25 4.5`, `.op`

⁠**Lo que ves:** `V(a)` y `V(b)` coinciden: 9 V, 8 V, 4,5 V, 0 V. Monta del mismo modo la red del ejercicio [11](#aufg-11): con `IZ=0` aparece allí tu $U_\mathrm{CA}$, y con tu $I_\mathrm{CC}$, `V(a)` baja a cero.
:::

:::frage ¿N es ahora realmente lo mismo que la batería?
En los terminales sí. Toda carga muestra en ambas la misma corriente y la misma tensión. En el interior no: en N se transforman en circuito abierto 27 W en $R_2$ y 13,5 W en $R_1$, mientras que la batería está en reposo. Las fuentes equivalentes responden a preguntas en los terminales, y a ninguna otra.
:::

:::aufgabe Ejercicio 10 ★★ Dos casos de carga
<span class="anker" id="aufg-10"></span>

En un aparato lineal desconocido mides con 10 $\Omega$ en los terminales 10 V y 1 A, y luego con 4 $\Omega$, 8 V y 2 A. (a) Determina $R_\mathrm{i}$, $U_\mathrm{i}$ e $I_\mathrm{CC}$ con [(9.3)](#gl-9-3). (b) Predice la corriente y la tensión para 1 $\Omega$.

:::loesung
(a) $R_\mathrm{i}=-\frac{10-8}{1-2}\,\Omega=2\,\Omega$, $U_\mathrm{i}=10\,\mathrm{V}+2\,\Omega\cdot1\,\mathrm{A}=12$ V. Comprobación con la fracción: $\frac{10\cdot2-8\cdot1}{2-1}\,\mathrm{V}=12$ V. $I_\mathrm{CC}=6$ A.

(b) $I_\mathrm{A}=12\,\mathrm{V}/3\,\Omega=4$ A, $U_\mathrm{AB}=4$ V.
:::
:::

:::aufgabe Ejercicio 11 ★★★ Dos fuentes reales
<span class="anker" id="aufg-11"></span>

Entre B y un nudo C hay 2 $\Omega$ y, en paralelo, una fuente de corriente ideal de 5 A que impulsa de B a C. De C salen 3 $\Omega$ hacia un nudo D. De D sale una fuente de tensión ideal de 4 V hacia el terminal A, con su polo positivo en D. Entre A y B hay 5 $\Omega$. (a) Calcula $U_\mathrm{CA}$ por superposición. (b) Calcula $R_\mathrm{i}$ desactivando las fuentes y, a partir de ella, $I_\mathrm{CC}$. (c) Caso límite: la fuente de tensión tiene 10 V. ¿Qué muestran el circuito abierto y el cortocircuito, y cuánto vale ahora $R_\mathrm{i}$?

:::loesung
(a) Solo la fuente de corriente (fuente de tensión como cable, terminales abiertos): los 5 A alimentan 2 $\Omega$ en paralelo con $3\,\Omega+5\,\Omega$, es decir, $2\,\Omega\parallel8\,\Omega=1{,}6\,\Omega$, y en C hay 8 V respecto a B. El divisor de 3 $\Omega$ y 5 $\Omega$ da $U'=8\,\mathrm{V}\cdot\frac58=5$ V.

Solo la fuente de tensión (fuente de corriente abierta): impulsa $4\,\mathrm{V}/10\,\Omega=0{,}4$ A desde el polo positivo por 3 $\Omega$ y 2 $\Omega$ hasta B y por los 5 $\Omega$ de B a A. Por tanto, A está 2 V por debajo de B: $U''=-2$ V. En total: $U_\mathrm{CA}=3$ V. En general, $U_\mathrm{CA}=\frac{I_\mathrm{q2}R_\mathrm{q2}-U_\mathrm{q1}}{R_\mathrm{q1}+R_\mathrm{q2}+R_3}\,R_3$, si $R_\mathrm{q1}$ son los 3 $\Omega$, $R_\mathrm{q2}$ los 2 $\Omega$ y $R_3$ los 5 $\Omega$.

(b) Con las fuentes desactivadas, 3 $\Omega$ y 2 $\Omega$ están en serie y en paralelo con 5 $\Omega$: $R_\mathrm{i}=5\,\Omega\parallel5\,\Omega=2{,}5\,\Omega$. Con ello, $I_\mathrm{CC}=3\,\mathrm{V}/2{,}5\,\Omega=1{,}2$ A. Directamente: la fuente de corriente con 2 $\Omega$ actúa como 10 V con 2 $\Omega$ (etapa [6](spannungsquelle-oder-stromquelle.html#stufe-6)). Los 5 $\Omega$ están cortocircuitados, así que $I_\mathrm{CC}=(10\,\mathrm{V}-4\,\mathrm{V})/5\,\Omega=1{,}2$ A.

(c) Con 10 V, las dos contribuciones se anulan: $U_\mathrm{CA}=0$ e $I_\mathrm{CC}=0$. El cociente es indeterminado, pero $R_\mathrm{i}$ sigue siendo 2,5 $\Omega$, porque no depende de las fuentes. Desde fuera, la red es una resistencia pura.
:::
:::

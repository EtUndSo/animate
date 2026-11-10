---
title: Etapa 3: Estrella y triángulo
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / Fuentes y fuentes equivalentes
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen
knoten: Capítulo 5: Fuentes y fuentes equivalentes
order: 1150500
summary: Un puente no equilibrado no tiene ni grupos ni simetría.
tags: triángulo, estrella, elementos adyacentes, cuadripolos, red en \pi, red en T, atenuadores
lang: es
---

<span class="anker" id="stufe-3"></span>

:::zweck
Un puente no equilibrado no tiene ni grupos ni simetría. La transformación estrella-triángulo cambia un trozo de la red de modo que surjan grupos.
:::

**La idea.** Un __triángulo__ son tres resistencias entre tres terminales. Una __estrella__ son tres resistencias que van de tres terminales a un nudo interior común, el centro de la estrella. Ambos tienen tres terminales y tres números. Con los valores adecuados no se distinguen desde fuera. El cambio ayuda porque el centro de la estrella es un nudo nuevo en el que cada resistencia de la estrella queda en serie con la vecina que tiene detrás.

:::satz Teorema 3.1 (Transformación estrella-triángulo)
<span class="anker" id="satz-3-1"></span>

Terminales 1, 2, 3, centro de la estrella 0. Del triángulo a la estrella:

<span class="anker" id="gl-3-1"></span>
$$R_{10}=\frac{R_{12}R_{31}}{R_{12}+R_{23}+R_{31}},\qquad R_{20}=\frac{R_{12}R_{23}}{R_{12}+R_{23}+R_{31}},\qquad R_{30}=\frac{R_{23}R_{31}}{R_{12}+R_{23}+R_{31}}. \tag{3.1}$$

De la estrella al triángulo, con las conductancias $G_{ij}=1/R_{ij}$:

<span class="anker" id="gl-3-2"></span>
$$G_{12}=\frac{G_{10}G_{20}}{G_{10}+G_{20}+G_{30}},\qquad G_{23}=\frac{G_{20}G_{30}}{G_{10}+G_{20}+G_{30}},\qquad G_{31}=\frac{G_{30}G_{10}}{G_{10}+G_{20}+G_{30}}. \tag{3.2}$$
:::

⁠**Cómo leerlo:** $R_{10}$ va del terminal 1 al centro de la estrella, $R_{12}$ del terminal 1 al terminal 2. Los __elementos adyacentes__ son los dos elementos contiguos: para $R_{10}$, los lados del triángulo en el terminal 1; para $G_{12}$, las ramas de la estrella en los terminales 1 y 2. Como regla para recordar: resistencia de estrella = producto de las resistencias adyacentes dividido por la resistencia perimetral del triángulo. Conductancia de triángulo = producto de las conductancias adyacentes dividido por la suma de las conductancias de la estrella. Equivalente a [(3.2)](#gl-3-2) es $R_{12}=R_{10}+R_{20}+R_{10}R_{20}/R_{30}$ con índices permutados cíclicamente. **Validez:** La igualdad vale para cualquier circuito exterior, pero solo en los tres terminales. El centro de la estrella no es un nudo en el original, y las corrientes en las propias resistencias son distintas.

:::herleitung De la estrella al triángulo, y luego invertir
En la estrella, en el centro se cumple la ley de los nudos $G_{10}(\varphi_1-\varphi_0)+G_{20}(\varphi_2-\varphi_0)+G_{30}(\varphi_3-\varphi_0)=0$. Con $S=G_{10}+G_{20}+G_{30}$ resulta $\varphi_0=(G_{10}\varphi_1+G_{20}\varphi_2+G_{30}\varphi_3)/S$. La corriente en el terminal 1 es, por tanto,

$$I_1=G_{10}(\varphi_1-\varphi_0)=\frac{G_{10}G_{20}}{S}(\varphi_1-\varphi_2)+\frac{G_{10}G_{30}}{S}(\varphi_1-\varphi_3).$$

En el triángulo es $I_1=G_{12}(\varphi_1-\varphi_2)+G_{31}(\varphi_1-\varphi_3)$. La comparación da [(3.2)](#gl-3-2), y además para potenciales cualesquiera. El terminal 2 da de forma análoga $G_{23}$.

Para la inversión, sea $H=R_{10}R_{20}+R_{20}R_{30}+R_{30}R_{10}$. Entonces $S=H/(R_{10}R_{20}R_{30})$, y [(3.2)](#gl-3-2) se convierte en $R_{12}=H/R_{30}$, $R_{23}=H/R_{10}$, $R_{31}=H/R_{20}$. De ahí se deducen $R_{12}R_{31}=H^2/(R_{20}R_{30})$ y $R_{12}+R_{23}+R_{31}=H^2/(R_{10}R_{20}R_{30})$. El cociente es $R_{10}$, es decir, [(3.1)](#gl-3-1).
:::

:::abbildung et1/k5bruecke 4
A la izquierda, un puente no equilibrado con el triángulo 1-2-3 (azul). A la derecha, el triángulo se ha sustituido por una estrella (rojo). Ahora 4 $\Omega$ y 20 $\Omega$ están en serie, igual que 8 $\Omega$ y 16 $\Omega$.
:::

::::beispiel
En la fig. [4](#abb-4) es $R_{12}=10\,\Omega$, $R_{23}=R_{31}=20\,\Omega$, y el perímetro vale 50 $\Omega$. De [(3.1)](#gl-3-1) resultan $R_{10}=4\,\Omega$, $R_{20}=4\,\Omega$, $R_{30}=8\,\Omega$. El puente se descompone en grupos:

$$R_\mathrm{AB}=4\,\Omega+(4\,\Omega+20\,\Omega)\parallel(8\,\Omega+16\,\Omega)=4\,\Omega+12\,\Omega=16\,\Omega.$$
::::

⁠**Comprobación** en los terminales 1, 2 con el terminal 3 abierto: la estrella tiene $4+4=8\,\Omega$; el triángulo, $10\,\Omega\parallel40\,\Omega=8\,\Omega$. **Casos límite:** Tres resistencias de triángulo iguales dan una estrella con un tercio del valor. Para $R_{12}\to0$, $R_{10}$ y $R_{20}$ tienden a cero, y $R_{30}$ pasa a ser $R_{23}\parallel R_{31}$, que es exactamente lo que es el triángulo cortocircuitado.

**$\pi$ y T.** En los __cuadripolos__ ([capítulo 6](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore/zweitore.html)), el triángulo y la estrella se dibujan de modo que una entrada quede a la izquierda y una salida a la derecha. El triángulo se llama entonces __red en $\pi$__; la estrella, __red en T__. Las fórmulas y las reglas no cambian. En ingeniería de telecomunicaciones se construyen así __atenuadores__, que debilitan una señal en un factor fijo y presentan la misma resistencia de entrada en ambos pares de terminales (adaptación de potencia, [capítulo 7](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/leistung-anpassung-und-wirkungsgrad/leistung-und-anpassung.html)). También los filtros de bobinas y condensadores se pueden construir en una u otra forma.

:::frage ¿Qué triángulo debo convertir?
Cualquiera cuya conversión cree grupos. En un puente sirve también el triángulo inferior, o incluso una estrella convertida en triángulo. El resultado siempre es el mismo.
:::

:::aufgabe Ejercicio 4 ★★ Ida y vuelta
<span class="anker" id="aufg-4"></span>

(a) Tres resistencias de 12 $\Omega$ cada una forman un triángulo. ¿Cuánto valen las resistencias de la estrella? (b) En un puente, las tres resistencias superiores (triángulo A, C, D) valen 6 $\Omega$ cada una; de C sale 1 $\Omega$ y de D salen 4 $\Omega$ hacia B. Calcula $R_\mathrm{AB}$. (c) Convierte la estrella $R_{10}=5\,\Omega$, $R_{20}=R_{30}=10\,\Omega$ en un triángulo, una vez con [(3.2)](#gl-3-2) y otra con la forma en resistencias.

:::loesung
(a) Perímetro 36 $\Omega$, $R_\mathrm{estrella}=\frac{12\cdot12}{36}\,\Omega=4\,\Omega$, un tercio del valor del triángulo.

(b) El triángulo se convierte en tres resistencias de estrella de 2 $\Omega$ cada una. Entonces $R_\mathrm{AB}=2\,\Omega+(2\,\Omega+1\,\Omega)\parallel(2\,\Omega+4\,\Omega)=2\,\Omega+3\,\Omega\parallel6\,\Omega=4\,\Omega$.

(c) Conductancias 0,2 S, 0,1 S, 0,1 S, suma 0,4 S. $G_{12}=\frac{0{,}2\cdot0{,}1}{0{,}4}$ S $=0{,}05$ S, $G_{23}=0{,}025$ S, $G_{31}=0{,}05$ S. Esto da $R_{12}=20\,\Omega$, $R_{23}=40\,\Omega$, $R_{31}=20\,\Omega$. Forma en resistencias: $R_{12}=5+10+\frac{5\cdot10}{10}=20\,\Omega$, $R_{23}=10+10+\frac{10\cdot10}{5}=40\,\Omega$, $R_{31}=10+5+\frac{10\cdot5}{10}=20\,\Omega$.
:::
:::

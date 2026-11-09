---
title: Etapa 2: Cuatro magnitudes, dos ecuaciones, cuatro números
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / Cuadripolos
order: 1160400
summary: Cuatro magnitudes de puerto son cuatro incógnitas.
tags: funciones del cuadripolo, sistema simétrico de flechas, sistema de flechas en cadena, sistema mixto de flechas
lang: es
---

<span class="anker" id="stufe-2"></span>

:::zweck
Cuatro magnitudes de puerto son cuatro incógnitas. Esta etapa muestra por qué el cuadripolo aporta exactamente dos ecuaciones y por qué en ellas solo hay cuatro números.
:::

**La idea.** La fuente y la carga aportan cada una una ecuación entre la tensión y la corriente de su puerto. Faltan dos, y las aporta el cuadripolo. Si se fijan dos magnitudes de puerto, por ejemplo ambas corrientes, quedan fijadas todas las corrientes y tensiones del interior, y con ellas las otras dos magnitudes de puerto. Las magnitudes fijadas son las causas; las demás, los efectos. Si el cuadripolo es lineal y no contiene fuentes independientes, vale la superposición de la [Parte 5](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html): cada efecto es la suma de la parte debida a la primera causa y la parte debida a la segunda, cada parte proporcional a su causa. Dos efectos por dos causas dan cuatro factores.

:::satz Teorema 2.1 (Ecuaciones del cuadripolo)
<span class="anker" id="satz-2-1"></span>

Un cuadripolo invariante en el tiempo queda descrito por completo por dos __funciones del cuadripolo__, por ejemplo

<span class="anker" id="gl-2-1"></span>
$$I_1=f_1(U_1,U_2),\quad I_2=g_1(U_1,U_2)\qquad\text{o}\qquad U_1=f_2(I_1,I_2),\quad U_2=g_2(I_1,I_2). \tag{2.1}$$

Si es lineal y está libre de fuentes independientes, para los efectos $y_1,y_2$ y las causas $x_1,x_2$ se cumple

<span class="anker" id="gl-2-2"></span>
$$y_1=p_{11}x_1+p_{12}x_2,\qquad y_2=p_{21}x_1+p_{22}x_2. \tag{2.2}$$
:::

⁠**Cómo leerlo:** La primera cifra de un parámetro nombra el efecto; la segunda, la causa. Los parámetros solo dependen del cuadripolo, no de la fuente ni de la carga. Cuatro magnitudes se pueden repartir de seis maneras en dos causas y dos efectos. Las habituales son las cuatro formas de este capítulo. **Validez:** [(2.1)](#gl-2-1) vale también para cuadripolos no lineales, entonces como curvas. En el transistor se describe así o bien el comportamiento con magnitudes continuas o bien el comportamiento de señal con pequeñas magnitudes alternas. Un transformador con devanados separados solo transmite magnitudes variables en el tiempo. [(2.2)](#gl-2-2) exige linealidad.

**Flechas de referencia.** Para que los signos sean unívocos hace falta un acuerdo (fig. [3](#abb-3)). En el __sistema simétrico de flechas__, también llamado sentido matemático de los signos, rige en ambos puertos el convenio receptor de la [Parte 2](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html): las flechas de corriente apuntan hacia el cuadripolo. En el __sistema de flechas en cadena__, también llamado sistema técnico de flechas, rige solo en la entrada; en la salida rige el convenio generador: la corriente de salida apunta hacia fuera, hacia la carga. Este capítulo usa el __sistema mixto de flechas__: $I_1$ e $I_2$ apuntan siempre hacia dentro. Donde la forma en cadena necesita la corriente saliente, la escribe explícitamente como $-I_2$. Por eso, una carga da en funcionamiento normal un $I_2$ negativo.

:::abbildung et1/k6zaehlpfeile 3
Los tres sistemas de flechas. Izquierda, simétrico: ambas corrientes apuntan hacia el cuadripolo. Centro, en cadena: la corriente de salida apunta hacia la carga. Derecha, mixto, como en este capítulo: $I_2$ sigue definida como a la izquierda, y la corriente hacia la carga se llama $-I_2$.
:::

::::beispiel
En el punto medio del cuadripolo T se encuentran $I_1$ e $I_2$, y por $R_\mathrm{b}$ circula su suma. La ley de las mallas da

$$U_1=R_\mathrm{a}I_1+R_\mathrm{b}(I_1+I_2)=35\,\Omega\cdot I_1+20\,\Omega\cdot I_2,\qquad U_2=R_\mathrm{c}I_2+R_\mathrm{b}(I_1+I_2)=20\,\Omega\cdot I_1+40\,\Omega\cdot I_2.$$

El sumando $20\,\Omega\cdot I_2$ de $U_1$ es el mecanismo: la corriente del puerto 2 pasa por $R_\mathrm{b}$, eleva allí el potencial del punto medio, y el puerto 1 ve esa elevación. Con $I_1=250$ mA e $I_2=-50$ mA resulta $U_1=8{,}75\,\mathrm{V}-1\,\mathrm{V}=7{,}75$ V y $U_2=5\,\mathrm{V}-2\,\mathrm{V}=3$ V.
::::

⁠**Caso límite:** Sin causas, $I_1=I_2=0$, ambas tensiones son cero, como exige un cuadripolo sin fuentes propias. Con una fuente independiente en el interior, en cada ecuación se añadiría una constante.

⁠**En resumen:** Dos magnitudes son libres, y cada una de las otras dos es una suma con dos factores fijos.

:::frage ¿Quién decide qué dos magnitudes son las causas, la red?
No, el cálculo. Físicamente, todo se establece a la vez. Las ecuaciones describen una relación entre cuatro magnitudes, y se puede reordenar en torno a dos cualesquiera, siempre que estas sean realmente de libre elección. «Causa» significa aquí: lo que está a la derecha del signo igual.
:::

:::aufgabe Ejercicio 2 ★ Predecir una caja negra
<span class="anker" id="aufg-2"></span>

Un cuadripolo lineal desconocido sin fuentes propias da dos mediciones. Con $I_1=200$ mA, $I_2=0$ resulta $U_1=8$ V, $U_2=3$ V. Con $I_1=0$, $I_2=100$ mA resulta $U_1=1{,}5$ V, $U_2=3$ V.

<ol class="al">

<li>

Predice sin más mediciones $U_1$ y $U_2$ para $I_1=100$ mA, $I_2=200$ mA.

</li>

<li>

¿Qué resulta para $I_1=100$ mA, $I_2=-50$ mA? ¿Qué llama la atención en $U_2$?

</li>

</ol>

:::loesung
Las mediciones dan $Z_{11}=8\,\mathrm{V}/200\,\mathrm{mA}=40\,\Omega$, $Z_{21}=15\,\Omega$, $Z_{12}=1{,}5\,\mathrm{V}/100\,\mathrm{mA}=15\,\Omega$, $Z_{22}=30\,\Omega$. (a) $U_1=40\,\Omega\cdot0{,}1\,\mathrm{A}+15\,\Omega\cdot0{,}2\,\mathrm{A}=7$ V, $U_2=15\,\Omega\cdot0{,}1\,\mathrm{A}+30\,\Omega\cdot0{,}2\,\mathrm{A}=7{,}5$ V. (b) $U_1=4\,\mathrm{V}-0{,}75\,\mathrm{V}=3{,}25$ V, $U_2=1{,}5\,\mathrm{V}-1{,}5\,\mathrm{V}=0$. Así pues, este par de corrientes corresponde a un puerto 2 en cortocircuito.
:::
:::

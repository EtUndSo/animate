---
title: Etapa 5: Forma de admitancia y ensayo de cortocircuito
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / Cuadripolos
order: 1160700
summary: La segunda elección: las tensiones son las causas.
tags: parámetros Y, admitancia, conductancia de entrada en cortocircuito, conductancia de salida en cortocircuito, conductancia de transferencia en cortocircuito, transconductancia, característica de entrada, característica de transferencia
lang: es
---

<span class="anker" id="stufe-5"></span>

:::zweck
La segunda elección: las tensiones son las causas. Esta etapa traslada todo lo anterior y muestra por qué ahora el cortocircuito asume el papel del circuito abierto.
:::

**La idea.** Si las tensiones son las causas, una tensión debe desaparecer para que la otra parte quede sola. Una tensión es cero si un hilo puentea el puerto. El circuito abierto anula una corriente; el cortocircuito, una tensión. Qué ensayo es el correcto se deduce solo de la elección de las causas.

:::definition Definición 5.1 (Forma de admitancia, forma Y)
<span class="anker" id="satz-5-1"></span>

La forma de admitancia, también forma de conductancia, toma las tensiones como causas:

<span class="anker" id="gl-5-1"></span>
$$I_1=Y_{11}U_1+Y_{12}U_2,\quad I_2=Y_{21}U_1+Y_{22}U_2,\qquad\text{en breve}\quad\mathbf I=\mathbf Y\cdot\mathbf U,\quad\mathbf Y=\begin{pmatrix}Y_{11}&Y_{12}\\Y_{21}&Y_{22}\end{pmatrix}. \tag{5.1}$$

Los __parámetros Y__ se obtienen de dos ensayos de cortocircuito:

<span class="anker" id="gl-5-2"></span>
$$Y_{11}=\left.\frac{I_1}{U_1}\right|_{U_2=0},\quad Y_{21}=\left.\frac{I_2}{U_1}\right|_{U_2=0},\quad Y_{12}=\left.\frac{I_1}{U_2}\right|_{U_1=0},\quad Y_{22}=\left.\frac{I_2}{U_2}\right|_{U_1=0}. \tag{5.2}$$

Con una carga de conductancia $Y_\mathrm{L}$ en el puerto 2, $I_2=-Y_\mathrm{L}U_2$, se cumple

<span class="anker" id="gl-5-3"></span>
$$U_2=-\frac{Y_{21}}{Y_{22}+Y_\mathrm{L}}\,U_1,\qquad Y_1=\frac{I_1}{U_1}=Y_{11}-\frac{Y_{12}Y_{21}}{Y_{22}+Y_\mathrm{L}}, \tag{5.3}$$

con los casos límite

<span class="anker" id="gl-5-4"></span>
$$Y_{1,\mathrm{CC}}=Y_{11},\qquad Y_{1,\mathrm{CA}}=Y_{11}-\frac{Y_{12}Y_{21}}{Y_{22}}. \tag{5.4}$$
:::

⁠**Cómo leerlo:** $Y$ representa la __admitancia__, la inversa de la impedancia; aquí son conductancias reales en siemens, típicamente de micro- a milisiemens, $Y_{ii}=G_{ii}$. $Y_{11}$ es la __conductancia de entrada en cortocircuito__, $Y_{22}$ la __conductancia de salida en cortocircuito__. $Y_{21}$ es la __conductancia de transferencia en cortocircuito__ en sentido directo; en el transistor se llama __transconductancia__, en general transadmitancia: la influencia de la tensión de entrada sobre la corriente de salida. $Y_{12}$ es la misma conductancia en sentido inverso, la influencia de la tensión de salida sobre la corriente de entrada. El circuito equivalente (fig. [6](#abb-6), izquierda) es el homólogo de la forma Z: una suma de corrientes es una conexión en paralelo de una conductancia y una fuente de corriente controlada por tensión (VCCS). [(5.3)](#gl-5-3) se obtiene como en la etapa [4](das-zweitor-im-betrieb.html#stufe-4), solo que con la ley de los nudos en los nudos derecho e izquierdo en lugar de la ley de las mallas.

:::abbildung et1/k6yesb 6
Izquierda: circuito equivalente de la forma Y. Derecha: ensayo de cortocircuito en el puerto 2 con la tensión impuesta $U_\mathrm{q}$. Como $U_2=0$, desaparece la fuente $Y_{12}U_2$, e $Y_{22}$ no lleva corriente. Quedan $Y_{11}$ en la entrada y la fuente de corriente $Y_{21}U_1$, cuya corriente circula por el hilo.
:::

**Ejemplo.** En el cuadripolo T hay 9 V en el puerto 1, y el puerto 2 está en cortocircuito. El hilo pone $R_\mathrm{c}$ en paralelo con $R_\mathrm{b}$, la resistencia total es $15\,\Omega+10\,\Omega=25\,\Omega$, es decir, $I_1=360$ mA. Esta corriente se reparte por mitades, $I_2=-180$ mA, negativa porque sale del puerto 2. Con 9 V en el puerto 2 y cortocircuito en el puerto 1, la resistencia total es $20\,\Omega+15\,\Omega\parallel20\,\Omega$, $I_2=315$ mA e $I_1=-180$ mA. Esto da

$$\mathbf Y=\begin{pmatrix}40&-20\\-20&35\end{pmatrix}\mathrm{mS}.$$

Comprobación con el funcionamiento de la etapa [4](das-zweitor-im-betrieb.html#stufe-4): $I_1=40\,\mathrm{mS}\cdot7{,}75\,\mathrm{V}-20\,\mathrm{mS}\cdot3\,\mathrm{V}=250$ mA. La carga $Y_\mathrm{L}=16{,}67$ mS da $Y_1=40\,\mathrm{mS}-400\,\mathrm{mS^2}/51{,}67\,\mathrm{mS}=32{,}26$ mS, que es $1/(31\,\Omega)$. **Casos límite:** $Y_{1,\mathrm{CC}}=40$ mS es $1/(25\,\Omega)$, $Y_{1,\mathrm{CA}}=28{,}57$ mS es $1/(35\,\Omega)$, como en la etapa [4](das-zweitor-im-betrieb.html#stufe-4).

**Curvas características.** Las ecuaciones Y también se pueden dibujar. La __característica de entrada__ es $I_1=f_1(U_1)$ con $U_2$ fija; la __característica de transferencia__, $I_2=f_2(U_1)$ con $U_2$ fija; la __característica de salida__, $I_2=f_3(U_2)$ con $U_1$ fija. En un cuadripolo lineal son rectas (fig. [7](#abb-7)): su pendiente es un parámetro Y, y el valor fijo las desplaza en paralelo. Cada valor del parámetro fijo da una recta; juntas forman una familia de curvas.

:::abbildung et1/k6kennlinien 7
Curvas características del cuadripolo T. Izquierda, característica de entrada: pendiente $Y_{11}=40$ mS, cada voltio de $U_2$ la desplaza $Y_{12}\cdot1\,\mathrm{V}=-20$ mA. Centro, característica de transferencia: pendiente $Y_{21}=-20$ mS. Derecha, característica de salida: pendiente $Y_{22}=35$ mS. En el transistor, estas curvas son curvadas ([Parte 10](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor/der-bipolartransistor.html)).
:::

:::frage ¿Por qué $Y_{11}$ no es $1/Z_{11}$? Al fin y al cabo, ambos describen la entrada.
Ambos describen la entrada, pero con distinta terminación: $Z_{11}$ vale con la salida abierta; $Y_{11}$, con la salida en cortocircuito. En el cuadripolo T son 35 $\Omega$ y 25 $\Omega$. $1/Y_{11}=Z_{11}$ solo se cumple si $Z_{12}$ o $Z_{21}$ es cero.
:::

:::aufgabe Ejercicio 5 ★★ Una red en $\pi$
<span class="anker" id="aufg-5"></span>

Una red en $\pi$ tiene las conductancias transversales $G_1=10$ mS en la entrada y $G_3=20$ mS en la salida, y la conductancia longitudinal $G_2=40$ mS.

<ol class="al">

<li>

Determina $\mathbf Y$ con ensayos de cortocircuito. ¿Qué corrientes circulan con 2 V en el puerto 1?

</li>

<li>

Calcula $Y_{1,\mathrm{CA}}$ y comprueba el resultado con un cálculo directo de resistencias.

</li>

<li>

Predice: ¿cuánto vale $I_1$ para $U_1=0$, $U_2=5$ V, y en qué sentido circula?

</li>

</ol>

:::loesung
(a) Puerto 2 en corto: $Y_{11}=G_1+G_2=50$ mS, $Y_{21}=-G_2=-40$ mS. Puerto 1 en corto: $Y_{22}=G_2+G_3=60$ mS, $Y_{12}=-40$ mS. Con 2 V: $I_1=100$ mA, $I_2=-80$ mA. (b) $Y_{1,\mathrm{CA}}=50\,\mathrm{mS}-1600\,\mathrm{mS^2}/60\,\mathrm{mS}=23{,}33$ mS, que son 42,86 $\Omega$. Directamente: $100\,\Omega\parallel(25\,\Omega+50\,\Omega)=42{,}86\,\Omega$. (c) $I_1=Y_{12}U_2=-200$ mA. El puerto 1 está en cortocircuito; la corriente va del puerto 2 por $G_2$ y abandona el cuadripolo por el terminal 1.
:::
:::

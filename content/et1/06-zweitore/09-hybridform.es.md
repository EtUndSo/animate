---
title: Etapa 7: Forma híbrida
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / Cuadripolos
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore
knoten: Capítulo 6: Cuadripolos
order: 1160900
summary: En un amplificador es fácil fijar la corriente en la entrada y la tensión en la salida.
tags: parámetros H, resistencia de entrada en cortocircuito, relación de corrientes en cortocircuito, reacción de tensión en circuito abierto, conductancia de salida en circuito abierto
lang: es
---

<span class="anker" id="stufe-7"></span>

:::zweck
En un amplificador es fácil fijar la corriente en la entrada y la tensión en la salida. Esta etapa mezcla las causas.
:::

**La idea.** Nada obliga a tomar el mismo tipo de causa en ambos puertos. Si se toman $I_1$ y $U_2$, los efectos son $U_1$ e $I_2$. Esto encaja con componentes como el transistor bipolar: su entrada se controla con una corriente, y su salida actúa como una fuente de corriente con gran resistencia interna. Los ensayos vuelven a deducirse de la elección: $U_2=0$ significa cortocircuito en la salida; $I_1=0$, circuito abierto en la entrada.

:::definition Definición 7.1 (Forma híbrida, forma H)
<span class="anker" id="satz-7-1"></span>

La forma híbrida toma $I_1$ y $U_2$ como causas:

<span class="anker" id="gl-7-1"></span>
$$U_1=H_{11}I_1+H_{12}U_2,\quad I_2=H_{21}I_1+H_{22}U_2,\qquad\text{en breve}\quad \begin{pmatrix}U_1\\I_2\end{pmatrix}=\mathbf H\begin{pmatrix}I_1\\U_2\end{pmatrix}. \tag{7.1}$$

Los __parámetros H__ son

<span class="anker" id="gl-7-2"></span>
$$H_{11}=\left.\frac{U_1}{I_1}\right|_{U_2=0},\quad H_{21}=\left.\frac{I_2}{I_1}\right|_{U_2=0},\quad H_{12}=\left.\frac{U_1}{U_2}\right|_{I_1=0},\quad H_{22}=\left.\frac{I_2}{U_2}\right|_{I_1=0}. \tag{7.2}$$
:::

⁠**Cómo leerlo:** $H_{11}$ es la __resistencia de entrada en cortocircuito__ en $\Omega$, típicamente unos k$\Omega$ en el transistor. $H_{21}$ es la __relación de corrientes en cortocircuito__ en sentido directo, la ganancia de corriente, sin unidad, aproximadamente de 100 a 500. $H_{12}$ es la __reacción de tensión en circuito abierto__, sin unidad, en torno a $10^{-4}$. $H_{22}$ es la __conductancia de salida en circuito abierto__ en S, unas decenas de µ S. Las unidades son mixtas, de ahí el nombre. La matriz se llama también matriz serie-paralelo (etapa [9](zusammenschaltung.html#stufe-9)). En el circuito equivalente (fig. [9](#abb-9), izquierda), en la entrada se suman tensiones: conexión en serie de $H_{11}$ y una VCVS $H_{12}U_2$. En la salida se suman corrientes: conexión en paralelo de $H_{22}$ y una CCCS $H_{21}I_1$.

:::abbildung et1/k6hesb 9
Izquierda: circuito equivalente de la forma H, en la entrada una conexión en serie, en la salida una conexión en paralelo. Derecha: el modelo de amplificador con $H_{12}=0$ y la carga de 5 k$\Omega$. 10 µ A en la entrada controlan 1 mA, del que 0,8 mA circulan por la carga. En la salida hay $-4$ V.
:::

::::beispiel
El cuadripolo T con 100 mA en la entrada y la salida en cortocircuito: $U_1=2{,}5$ V, y la corriente se reparte por mitades, $I_2=-50$ mA, es decir, $H_{11}=25\,\Omega$, $H_{21}=-0{,}5$. Con la entrada abierta y $U_2=4$ V: $I_2=100$ mA, $U_1=2$ V, es decir, $H_{22}=25$ mS, $H_{12}=0{,}5$. El modelo de amplificador del capítulo tiene $H_{11}=2$ k$\Omega$, $H_{21}=100$, $H_{22}=50$ µ S, es decir, una resistencia de salida de 20 k$\Omega$, y $H_{12}=0$. Es una aproximación que supone alrededor del 1 % (ejercicio [7](#aufg-7)). Con $U_1=20$ mV circulan $I_1=10$ µ A, y la fuente de la salida impulsa 1 mA en $20\,\text{k}\Omega\parallel5\,\text{k}\Omega=4$ k$\Omega$. Esto da $U_2=-4$ V, una ganancia de tensión de $-200$. El signo menos se debe a que $H_{21}I_1$ entra en el puerto 2, de modo que la corriente recorre la carga de abajo arriba.
::::

⁠**Casos límite:** Para $H_{22}\to0$, la salida se convierte en una fuente de corriente ideal; para $H_{11}=0$, la entrada, en un cortocircuito. El modelo ideal de amplificador de corriente es exactamente eso: $U_1=0$, $I_2=H_{21}I_1$.

:::frage ¿Por qué $H_{21}$ lleva signo menos en el cuadripolo T, pero no en el amplificador?
En el cuadripolo T no hay ninguna fuente. Una corriente que entra por el puerto 1 solo puede salir por el puerto 2, $I_2$ es negativa y su módulo es menor que $I_1$. En el amplificador, $H_{21}$ es la ley de una fuente controlada, que fija por sí misma el sentido y el valor de la corriente y se alimenta de una fuente auxiliar.
:::

:::aufgabe Ejercicio 7 ★★ ¿Cuánto supone la reacción?
<span class="anker" id="aufg-7"></span>

El modelo de amplificador recibe una pequeña reacción $H_{12}=5\cdot10^{-5}$, con los demás valores iguales, carga de 5 k$\Omega$, $I_1=10$ µ A.

<ol class="al">

<li>

¿Cambian $U_2$ e $I_2$ respecto al ejemplo? Justifícalo con [(7.1)](#gl-7-1).

</li>

<li>

¿Cuánto vale ahora $U_1$? ¿En qué porcentaje cambia?

</li>

<li>

¿Cuánto valen la ganancia de tensión y la resistencia de entrada?

</li>

</ol>

:::loesung
(a) No. La segunda línea de [(7.1)](#gl-7-1) no contiene $H_{12}$, e $I_1$ es fija: $U_2=-4$ V, $I_2=0{,}8$ mA. (b) $U_1=20\,\mathrm{mV}+5\cdot10^{-5}\cdot(-4\,\mathrm{V})=19{,}8$ mV, un 1 % menos. (c) $U_2/U_1=-202$, $Z_1=19{,}8\,\mathrm{mV}/10\,\mu\text{A}=1{,}98$ k$\Omega$. Aquí la reacción es pequeña; por eso, a menudo se desprecia.
:::
:::

---
title: Etapa 3: Forma de impedancia y ensayo de circuito abierto
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / Cuadripolos
order: 1160500
summary: La primera elección: las corrientes son las causas.
tags: parámetros Z, resistencia de entrada en circuito abierto, resistencia de salida en circuito abierto, resistencia de transferencia en circuito abierto, magnitudes de dipolo, magnitudes de transferencia, impedancia
lang: es
---

<span class="anker" id="stufe-3"></span>

:::zweck
La primera elección: las corrientes son las causas. Esta etapa muestra por qué un puerto abierto deja al descubierto los cuatro números uno a uno.
:::

**La idea.** Cada tensión es una suma de una parte debida a $I_1$ y una parte debida a $I_2$. Para ver una parte sola, la otra debe desaparecer, es decir, su corriente debe ser cero. Una corriente es cero si su puerto está abierto. Con el puerto 2 abierto, en ambas ecuaciones solo quedan las partes debidas a $I_1$. Así, un ensayo da dos parámetros, y el ensayo con los puertos intercambiados da los otros dos.

:::definition Definición 3.1 (Forma de impedancia, forma Z)
<span class="anker" id="satz-3-1"></span>

La forma de impedancia, también forma de resistencia, toma las corrientes como causas:

<span class="anker" id="gl-3-1"></span>
$$U_1=Z_{11}I_1+Z_{12}I_2,\quad U_2=Z_{21}I_1+Z_{22}I_2,\qquad\text{en breve}\quad\mathbf U=\mathbf Z\cdot\mathbf I,\quad\mathbf Z=\begin{pmatrix}Z_{11}&Z_{12}\\mathbb{Z}_{21}&Z_{22}\end{pmatrix}. \tag{3.1}$$

Los __parámetros Z__ se obtienen de dos ensayos de circuito abierto:

<span class="anker" id="gl-3-2"></span>
$$Z_{11}=\left.\frac{U_1}{I_1}\right|_{I_2=0},\quad Z_{21}=\left.\frac{U_2}{I_1}\right|_{I_2=0},\quad Z_{12}=\left.\frac{U_1}{I_2}\right|_{I_1=0},\quad Z_{22}=\left.\frac{U_2}{I_2}\right|_{I_1=0}. \tag{3.2}$$
:::

⁠**Cómo leerlo:** $Z_{11}$ es la __resistencia de entrada en circuito abierto__, $Z_{22}$ la __resistencia de salida en circuito abierto__, $Z_{21}$ la __resistencia de transferencia en circuito abierto__ en sentido directo y $Z_{12}$ la de sentido inverso. Todas tienen la unidad $\Omega$; lo típico va de ohmios a megaohmios. Los parámetros con índices iguales se llaman __magnitudes de dipolo__: son la resistencia de un par de terminales con una terminación fija en el otro lado. Los parámetros con índices distintos se llaman __magnitudes de transferencia__: relacionan ambos lados. La letra $Z$ representa la __impedancia__. Generaliza la resistencia a condensadores y bobinas con magnitudes alternas. Aquí todas las $Z$ son resistencias reales, para las que vale $Z_{ii}=R_{ii}$. **Validez:** Ambas corrientes deben ser de libre elección (etapa [6](umrechnen-t-und.html#stufe-6)).

**Circuito equivalente.** Las dos ecuaciones se pueden dibujar (fig. [4](#abb-4), izquierda). Una suma de tensiones es una conexión en serie. $Z_{11}I_1$ depende de la corriente propia: es una resistencia. $Z_{12}I_2$ depende de la corriente ajena: es una fuente de tensión controlada (CCVS). El puerto 2 está construido igual. En esta imagen se ve el mecanismo del circuito abierto: con $I_2=0$, la fuente $Z_{12}I_2$ da cero voltios y $Z_{22}$ no lleva corriente (fig. [4](#abb-4), derecha). $U_1$ cae solo en $Z_{11}$, y $U_2$ es la tensión de fuente $Z_{21}I_1$.

:::abbildung et1/k6zesb 4
Izquierda: circuito equivalente de la forma Z, en cada lado una resistencia en serie con una fuente de tensión controlada por corriente. Derecha: ensayo de circuito abierto en el puerto 2 con la corriente impuesta $I_\mathrm{q}$. En gris, lo que desaparece por $I_2=0$. El ensayo con el puerto 1 abierto es la imagen especular y da $Z_{12}$ y $Z_{22}$.
:::

**Ejemplo.** En el cuadripolo T se impone en el puerto 1 la corriente de 100 mA, y el puerto 2 queda abierto. La corriente pasa por $R_\mathrm{a}$ y $R_\mathrm{b}$, $U_1=3{,}5$ V. $R_\mathrm{c}$ no lleva corriente, en ella no cae nada, y $U_2$ es la tensión en $R_\mathrm{b}$: 2 V. Por tanto, $Z_{11}=35\,\Omega$, $Z_{21}=20\,\Omega$. Lo mismo desde el puerto 2 da $U_2=4$ V, $U_1=2$ V, es decir,

$$\mathbf Z=\begin{pmatrix}R_\mathrm{a}+R_\mathrm{b}&R_\mathrm{b}\\mathbb{R}_\mathrm{b}&R_\mathrm{b}+R_\mathrm{c}\end{pmatrix}=\begin{pmatrix}35&20\\20&40\end{pmatrix}\Omega.$$

⁠**El puente.** Los ensayos no necesitan línea de masa. El puente de la fig. [2](vom-vierpol-zum-zweitor.html#abb-2), derecha, reparte una corriente en el puerto 1 por mitades, porque las resistencias de las ramas son iguales: ambas ramas tienen $R_\mathrm{x}+R_\mathrm{y}$. El puerto 2 está abierto, y la tensión entre los puntos medios de las ramas es $\frac{I_1}{2}R_\mathrm{y}-\frac{I_1}{2}R_\mathrm{x}$. Por simetría, lo mismo vale en sentido inverso:

<span class="anker" id="gl-3-3"></span>
$$Z_{11}=Z_{22}=(R_\mathrm{x}+R_\mathrm{y})\parallel(R_\mathrm{x}+R_\mathrm{y})=\frac{R_\mathrm{x}+R_\mathrm{y}}{2},\qquad Z_{21}=Z_{12}=\frac{R_\mathrm{y}-R_\mathrm{x}}{2}. \tag{3.3}$$

⁠**Casos límite:** Para $R_\mathrm{b}\to0$ son $Z_{12}=Z_{21}=0$: la rama transversal es un hilo, y los puertos quedan desacoplados. Para $R_\mathrm{x}=R_\mathrm{y}$, el puente está equilibrado ([Parte 4](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-und-spannung-messen/strom-und-spannung-messen.html)), y de nuevo $Z_{21}=0$.

:::frage ¿Por qué una corriente y no una tensión en la entrada? Una fuente de tensión la tengo más a mano.
También sirve. Solo cuenta que el otro puerto esté abierto. Entonces se miden $U_1$ e $I_1$ y se forma el cociente. La corriente impuesta solo encaja con la manera de pensar de esta forma: es la causa, y las tensiones son los efectos.
:::

:::aufgabe Ejercicio 3 ★★ El puente como cuadripolo
<span class="anker" id="aufg-3"></span>

En el puente de la fig. [2](vom-vierpol-zum-zweitor.html#abb-2) sean $R_\mathrm{x}=30\,\Omega$ y $R_\mathrm{y}=50\,\Omega$.

<ol class="al">

<li>

Determina $\mathbf Z$ y, a partir de ella, una red en T con los mismos cuatro parámetros.

</li>

<li>

Con 100 mA en el puerto 1 y el puerto 2 abierto: ¿cuánto valen $U_1$ y $U_2$?

</li>

<li>

Intercambia los valores, $R_\mathrm{x}=50\,\Omega$, $R_\mathrm{y}=30\,\Omega$. ¿Qué cambia en $\mathbf Z$ y en la red en T? ¿Qué significa el resultado?

</li>

</ol>

:::loesung
(a) Con [(3.3)](#gl-3-3): $Z_{11}=Z_{22}=40\,\Omega$, $Z_{12}=Z_{21}=10\,\Omega$. Red en T: $R_\mathrm{b}=Z_{12}=10\,\Omega$, $R_\mathrm{a}=R_\mathrm{c}=30\,\Omega$. (b) $U_1=40\,\Omega\cdot100\,\mathrm{mA}=4$ V, $U_2=10\,\Omega\cdot100\,\mathrm{mA}=1$ V. Directamente: 50 mA por cada rama, $U_2=50\,\mathrm{mA}\cdot(50-30)\,\Omega=1$ V. (c) $Z_{11}$ y $Z_{22}$ no cambian, $Z_{12}=Z_{21}=-10\,\Omega$. La red en T tendría $R_\mathrm{b}=-10\,\Omega$ y $R_\mathrm{a}=R_\mathrm{c}=50\,\Omega$. El elemento negativo no existe como componente; aquí la T es solo una magnitud de cálculo. Indica: con la misma $I_1$, $U_2$ tiene el signo contrario.
:::
:::

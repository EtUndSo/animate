---
title: Etapa 6: Conversión, T y $\pi$
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / Cuadripolos
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore
knoten: Capítulo 6: Cuadripolos
order: 1160800
summary: La forma Z y la forma Y describen el mismo cuadripolo.
tags: 
lang: es
---

<span class="anker" id="stufe-6"></span>

:::zweck
La forma Z y la forma Y describen el mismo cuadripolo. Esta etapa muestra cómo se pasa de una a otra, y cuándo una forma ni siquiera existe.
:::

**La idea.** La forma Y y la forma Z son las mismas dos ecuaciones. Una está despejada para las tensiones; la otra, para las corrientes. El paso de una a otra es, pues, la resolución de un sistema de ecuaciones, y eso lo hace la matriz inversa de la sección «Desde cero».

:::satz Teorema 6.1 (Conversión entre Z e Y)
<span class="anker" id="satz-6-1"></span>

La matriz de conductancias y la matriz de resistencias son inversas entre sí, $\mathbf Y\cdot\mathbf Z=\mathbf 1$:

<span class="anker" id="gl-6-1"></span>
$$\mathbf Y=\mathbf Z^{-1}=\frac{1}{\det\mathbf Z}\begin{pmatrix}Z_{22}&-Z_{12}\\-Z_{21}&Z_{11}\end{pmatrix},\qquad \mathbf Z=\mathbf Y^{-1}=\frac{1}{\det\mathbf Y}\begin{pmatrix}Y_{22}&-Y_{12}\\-Y_{21}&Y_{11}\end{pmatrix} \tag{6.1}$$

con $\det\mathbf Z=Z_{11}Z_{22}-Z_{12}Z_{21}$ y $\det\mathbf Y=Y_{11}Y_{22}-Y_{12}Y_{21}$.
:::

⁠**Cómo leerlo:** Se invierte la matriz entera, no cada número por separado. A cada elemento le corresponde el denominador entero; por eso, cada parámetro Y depende de todos los parámetros Z. **Validez:** El determinante no debe ser cero.

:::herleitung Dos caminos hacia la inversa
⁠**Con matrices.** De $\mathbf I=\mathbf Y\mathbf U$ y $\mathbf U=\mathbf Z\mathbf I$ se sigue $\mathbf I=\mathbf Y\mathbf Z\,\mathbf I$ para todo $\mathbf I$, es decir, $\mathbf Y\mathbf Z=\mathbf 1$.

⁠**Con ensayos de cortocircuito en el circuito equivalente Z.** Con $U_2=0$ se cumple $Z_{21}I_1=-Z_{22}I_2$, es decir, $I_2=-\frac{Z_{21}}{Z_{22}}I_1$ y $U_1=\bigl(Z_{11}-Z_{12}\frac{Z_{21}}{Z_{22}}\bigr)I_1$. Con ello

$$Y_{11}=\frac{I_1}{U_1}=\frac{Z_{22}}{Z_{11}Z_{22}-Z_{12}Z_{21}},\qquad Y_{21}=\frac{I_2}{U_1}=-\frac{Z_{21}}{Z_{11}Z_{22}-Z_{12}Z_{21}}.$$

Con $U_1=0$ se cumple $-Z_{11}I_1=Z_{12}I_2$, es decir, $I_1=-\frac{Z_{12}}{Z_{11}}I_2$ y $U_2=\bigl(Z_{22}-Z_{21}\frac{Z_{12}}{Z_{11}}\bigr)I_2$. Esto da

$$Y_{12}=-\frac{Z_{12}}{Z_{11}Z_{22}-Z_{12}Z_{21}},\qquad Y_{22}=\frac{Z_{11}}{Z_{11}Z_{22}-Z_{12}Z_{21}}.$$
:::

**T y $\pi$.** La matriz Z de la red en T de la etapa [3](impedanzform-und-leerlaufversuch.html#stufe-3) se puede invertir con [(6.1)](#gl-6-1); la matriz Y de la red en $\pi$ se lee directamente de los ensayos de cortocircuito. Con $D=R_\mathrm{a}R_\mathrm{b}+R_\mathrm{a}R_\mathrm{c}+R_\mathrm{b}R_\mathrm{c}=\det\mathbf Z$ y las conductancias $G_1$, $G_3$ transversales y $G_2$ longitudinal se cumple

<span class="anker" id="gl-6-2"></span>
$$\mathbf Y_\mathrm{T}=\frac1D\begin{pmatrix}R_\mathrm{b}+R_\mathrm{c}&-R_\mathrm{b}\\-R_\mathrm{b}&R_\mathrm{a}+R_\mathrm{b}\end{pmatrix},\qquad \mathbf Y_\pi=\begin{pmatrix}G_1+G_2&-G_2\\-G_2&G_2+G_3\end{pmatrix}. \tag{6.2}$$

Igualando ambas resultan $G_2=-Y_{12}$, $G_1=Y_{11}+Y_{12}$ y $G_3=Y_{22}+Y_{21}$. Para $G_3=0$, $\mathbf Y_\pi$ se convierte en el par $I_1=(G_1+G_2)U_1-G_2U_2$, $I_2=-G_2U_1+G_2U_2$. Esta es la transformación estrella-triángulo del [capítulo 5](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html): T es la estrella; $\pi$, el triángulo. La descripción con parámetros Z conduce por sí sola a la red en T; la descripción con parámetros Y, a la red en $\pi$, su dual. A la inversa, a todo cuadripolo con $Z_{12}=Z_{21}$ le corresponde un circuito equivalente en T y otro en $\pi$ sin fuentes (etapa [10](eigenschaften-und-alle-formen-im-uberblick.html#stufe-10)).

:::abbildung et1/k6tpi 8
Dos circuitos, el mismo cuadripolo. A la izquierda, la red en T con 15, 20 y 20 $\Omega$; a la derecha, la red en $\pi$ equivalente con 50, 50 y 66,7 $\Omega$. Ambas tienen $\det\mathbf Z=1000\,\Omega^2$. En los puertos, ninguna medición las distingue.
:::

::::beispiel
Se tiene $\det\mathbf Z=35\cdot40\,\Omega^2-20\cdot20\,\Omega^2=1000\,\Omega^2$, es decir,

$$\mathbf Y=\frac{1}{1000\,\Omega^2}\begin{pmatrix}40&-20\\-20&35\end{pmatrix}\Omega=\begin{pmatrix}40&-20\\-20&35\end{pmatrix}\mathrm{mS},$$

exactamente el resultado de los ensayos de cortocircuito. La red en $\pi$ tiene $G_2=20$ mS, $G_1=40\,\mathrm{mS}-20\,\mathrm{mS}=20$ mS, $G_3=15$ mS, es decir, 50 $\Omega$, 50 $\Omega$ y 66,7 $\Omega$. Con la misma fuente y carga da de nuevo 7,75 V y 3 V.
::::

⁠**Casos límite: no toda forma existe.** Una resistencia longitudinal $R$ y una resistencia transversal $R$, cada una sola entre los puertos, tienen

$$\mathbf Y_\text{long}=G\begin{pmatrix}1&-1\\-1&1\end{pmatrix},\qquad\mathbf Z_\text{trans}=R\begin{pmatrix}1&1\\1&1\end{pmatrix}.$$

Ambos determinantes son cero. La resistencia longitudinal no tiene forma Z: en ella siempre se cumple $I_2=-I_1$, las corrientes no son de libre elección y, por tanto, no sirven como causas. La resistencia transversal no tiene forma Y, porque siempre se cumple $U_1=U_2$. Lo mismo le ocurre a la fuente de corriente ideal controlada por corriente: sus corrientes están rígidamente acopladas.

:::frage ¿Por qué $Y_{11}$ es positivo, pero $Y_{21}$ negativo?
Se debe a las flechas de referencia. Con $U_2=0$, una tensión positiva en el puerto 1 impulsa una corriente hacia dentro, $Y_{11}>0$. Esa corriente sale por el otro puerto, pero se cuenta hacia dentro. Por eso, las conductancias de transferencia de circuitos pasivos como T y $\pi$ son negativas.
:::

:::aufgabe Ejercicio 6 ★ Ida y vuelta
<span class="anker" id="aufg-6"></span>

Un cuadripolo tiene $Z_{11}=20\,\Omega$, $Z_{12}=Z_{21}=10\,\Omega$, $Z_{22}=55\,\Omega$.

<ol class="al">

<li>

Calcula $\mathbf Y$.

</li>

<li>

Determina las resistencias de la red en T y de la red en $\pi$.

</li>

<li>

Escribe $\mathbf Y$ de una resistencia longitudinal de 100 $\Omega$. ¿Por qué falla $\mathbf Z=\mathbf Y^{-1}$?

</li>

</ol>

:::loesung
(a) $\det\mathbf Z=20\cdot55\,\Omega^2-10\cdot10\,\Omega^2=1000\,\Omega^2$, es decir, $Y_{11}=55$ mS, $Y_{12}=Y_{21}=-10$ mS, $Y_{22}=20$ mS. (b) T: $R_\mathrm{b}=10\,\Omega$, $R_\mathrm{a}=10\,\Omega$, $R_\mathrm{c}=45\,\Omega$. $\pi$: $G_2=10$ mS, $G_1=45$ mS, $G_3=10$ mS, es decir, 100 $\Omega$ longitudinal, 22,2 $\Omega$ y 100 $\Omega$ transversales. (c) $Y_{11}=Y_{22}=10$ mS, $Y_{12}=Y_{21}=-10$ mS, $\det\mathbf Y=0$. No hay inversa, porque siempre se cumple $I_2=-I_1$ y las corrientes no son de libre elección.
:::
:::

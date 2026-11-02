---
title: Etapa 8: Forma en cadena
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / Cuadripolos
order: 1161000
summary: A menudo se conectan cuadripolos uno detrás de otro.
tags: parámetros A, cadena
lang: es
---

<span class="anker" id="stufe-8"></span>

:::zweck
A menudo se conectan cuadripolos uno detrás de otro. La salida de uno alimenta la entrada del siguiente. Esta etapa elige las magnitudes de salida como causas y convierte eso en un producto de matrices.
:::

**La idea.** Si un cuadripolo va detrás de otro, las magnitudes de salida del primero son exactamente las magnitudes de entrada del segundo. Si una forma describe las magnitudes de entrada mediante las de salida, se pueden encadenar: se empieza en la carga y se calcula hacia atrás, etapa por etapa, hasta la fuente. Eso es exactamente lo que hace la forma en cadena. El signo menos delante de $I_2$ es la razón de que encaje: la corriente que sale de un cuadripolo es la corriente que entra en el siguiente.

:::definition Definición 8.1 (Forma en cadena, forma A)
<span class="anker" id="satz-8-1"></span>

La forma en cadena toma $U_2$ y $-I_2$ como causas:

<span class="anker" id="gl-8-1"></span>
$$U_1=A_{11}U_2+A_{12}(-I_2),\quad I_1=A_{21}U_2+A_{22}(-I_2),\qquad\text{en breve}\quad \begin{pmatrix}U_1\\I_1\end{pmatrix}=\mathbf A\begin{pmatrix}U_2\\-I_2\end{pmatrix}. \tag{8.1}$$

Los __parámetros A__ se obtienen de ensayos en la salida:

<span class="anker" id="gl-8-2"></span>
$$A_{11}=\left.\frac{U_1}{U_2}\right|_{I_2=0},\quad A_{21}=\left.\frac{I_1}{U_2}\right|_{I_2=0},\quad A_{12}=\left.-\frac{U_1}{I_2}\right|_{U_2=0},\quad A_{22}=\left.-\frac{I_1}{I_2}\right|_{U_2=0}. \tag{8.2}$$

Para dos cuadripolos en __cadena__ se cumple $\mathbf A=\mathbf A'\mathbf A''$.
:::

⁠**Cómo leerlo:** $A_{11}$ es la relación de tensiones recíproca en circuito abierto en sentido directo, $A_{21}$ la conductancia de transferencia en circuito abierto en sentido directo, $A_{12}$ la resistencia de transferencia en cortocircuito en sentido directo, $A_{22}$ la relación de corrientes recíproca en cortocircuito en sentido directo. Recíproca significa: es entrada entre salida, es decir, la inversa de la relación habitual. $A_{11}$ y $A_{22}$ no tienen unidad, $A_{12}$ tiene $\Omega$, $A_{21}$ tiene S. Un atenuador tiene $A_{11}>1$. **Validez:** La cadena exige el orden $\mathbf A'\mathbf A''$, con la fuente a la izquierda.

:::herleitung Por qué la cadena es un producto de matrices
Con una prima, el primer cuadripolo; con dos primas, el segundo. La conexión impone $U_2'=U_1''$ y $-I_2'=I_1''$. Sustituyendo:

$$\begin{pmatrix}U_1'\\I_1'\end{pmatrix}=\mathbf A'\begin{pmatrix}U_2'\\-I_2'\end{pmatrix}=\mathbf A'\begin{pmatrix}U_1''\\I_1''\end{pmatrix}=\mathbf A'\mathbf A''\begin{pmatrix}U_2''\\-I_2''\end{pmatrix}.$$
:::

:::abbildung et1/k6kette 10
Arriba: dos cuadripolos en cadena. La salida del primero y la entrada del segundo comparten tensión y corriente. Abajo: el cuadripolo T como cadena de tres cuadripolos elementales: resistencia longitudinal, conductancia transversal, resistencia longitudinal.
:::

**Ejemplo.** Los bloques más sencillos son la resistencia longitudinal y la conductancia transversal. En la resistencia longitudinal, $U_1=U_2+R(-I_2)$ e $I_1=-I_2$; en la conductancia transversal, $U_1=U_2$ e $I_1=G\,U_2+(-I_2)$:

$$\mathbf A_R=\begin{pmatrix}1&R\\0&1\end{pmatrix},\qquad \mathbf A_G=\begin{pmatrix}1&0\\G&1\end{pmatrix}.$$

El cuadripolo T es una cadena de $R_\mathrm{a}$, $G_\mathrm{b}=1/R_\mathrm{b}=50$ mS y $R_\mathrm{c}$ (fig. [10](#abb-10), abajo):

$$\mathbf A=\begin{pmatrix}1&15\,\Omega\\0&1\end{pmatrix}\begin{pmatrix}1&0\\50\,\mathrm{mS}&1\end{pmatrix}\begin{pmatrix}1&20\,\Omega\\0&1\end{pmatrix}=\begin{pmatrix}1{,}75&50\,\Omega\\50\,\mathrm{mS}&2\end{pmatrix}.$$

Hacia atrás desde la carga, con $U_2=3$ V y $-I_2=50$ mA: $U_1=5{,}25\,\mathrm{V}+2{,}5\,\mathrm{V}=7{,}75$ V e $I_1=150\,\mathrm{mA}+100\,\mathrm{mA}=250$ mA. Son los valores de la etapa [4](das-zweitor-im-betrieb.html#stufe-4), sin sistema de ecuaciones.

La red en $\pi$ equivalente, con las conductancias transversales $G_1$, $G_3$ y la conductancia longitudinal $G_2$, da en general

<span class="anker" id="gl-8-3"></span>
$$A_{11}=1+\frac{G_3}{G_2},\qquad A_{21}=G_1+G_3+\frac{G_1G_3}{G_2},\qquad A_{12}=\frac{1}{G_2},\qquad A_{22}=1+\frac{G_1}{G_2}, \tag{8.3}$$

por ejemplo, $A_{11}=1+15/20=1{,}75$. Con la salida abierta, $G_2$ y $G_3$ forman un divisor de tensión, $U_2=U_1\,G_2/(G_2+G_3)$, de ahí $A_{11}$. Los demás se obtienen igual de [(8.2)](#gl-8-2).

⁠**Casos límite:** $R=0$ y $G=0$ dan la matriz identidad, un cuadripolo que no hace nada. Dos cuadripolos T iguales en cadena tienen $A_{11}=5{,}56$, no $1{,}75^2=3{,}06$. El segundo carga al primero, y así la tensión intermedia baja por debajo del valor en circuito abierto.

:::frage La señal va hacia delante. ¿Por qué la forma en cadena calcula hacia atrás?
Porque es una regla de cálculo, no un desarrollo en el tiempo. En la salida, la carga fija $-I_2$ junto con $U_2$. A partir de ahí, cada etapa da las magnitudes anteriores sin sistema de ecuaciones. Físicamente, todo se establece conjuntamente.
:::

:::ltspice La cadena se carga a sí misma
⁠**Esquema:** fuente `voltage` con `9` de `1` a masa. Primera T: `Ra1` con `15` de `1` a `m1`, `Rb1` con `20` de `m1` a masa, `Rc1` con `20` de `m1` a `k`. Segunda T igual, de `k` por `m2` a `3`. `RL` con `1G` de `3` a masa, es decir, casi circuito abierto.

⁠**Directivas:** `.op`, `.meas op Uk FIND V(k)`, `.meas op Usal FIND V(3)`, `.meas op Ient FIND I(Ra1)`.

⁠**Lo que ves:** $\mathtt{V(3)}=1{,}618$ V, es decir, $9\,\mathrm{V}/1{,}618\,\mathrm{V}=5{,}56$, como $A_{11}$ de $\mathbf A\mathbf A$. En el punto `k` hay 2,83 V en lugar de los 5,14 V que tendría una sola T en circuito abierto. Pon `RL` a 60 y comprueba el ejercicio [8](#aufg-8)(c): $\mathtt{V(3)}=1{,}036$ V.
:::

:::aufgabe Ejercicio 8 ★★★ El orden importa
<span class="anker" id="aufg-8"></span>

Una resistencia longitudinal de 30 $\Omega$ y el cuadripolo T se conectan en cadena.

<ol class="al">

<li>

Calcula $\mathbf A$ para «T, luego resistencia longitudinal» y para «resistencia longitudinal, luego T».

</li>

<li>

Explica la diferencia en $A_{11}$ con corrientes y divisores de tensión, sin matrices.

</li>

<li>

Dos cuadripolos T iguales en cadena están conectados a una fuente ideal de 9 V y alimentan la carga de 60 $\Omega$. ¿Cuánto vale $U_2$? Calcula con $\mathbf A\mathbf A$.

</li>

</ol>

:::loesung
(a) T, luego resistencia longitudinal: $A_{11}=1{,}75$, $A_{12}=102{,}5\,\Omega$, $A_{21}=50$ mS, $A_{22}=3{,}5$. Resistencia longitudinal, luego T: $A_{11}=3{,}25$, $A_{12}=110\,\Omega$, $A_{21}=50$ mS, $A_{22}=2$.

(b) $A_{11}$ vale con la salida abierta. En el primer caso, la resistencia longitudinal queda abierta al final, no lleva corriente, y $A_{11}$ sigue siendo 1,75. En el segundo, está delante de la entrada de la T, que muestra 35 $\Omega$. Forma con ella un divisor de tensión, $65/35=1{,}857$, y $1{,}857\cdot1{,}75=3{,}25$.

(c) $\mathbf A\mathbf A$ tiene $A_{11}=5{,}5625$, $A_{12}=187{,}5\,\Omega$, $A_{21}=187{,}5$ mS, $A_{22}=6{,}5$. Con $-I_2=U_2/60\,\Omega$ es $U_1=(5{,}5625+187{,}5/60)\,U_2=8{,}6875\,U_2$, es decir, $U_2=1{,}036$ V.
:::
:::

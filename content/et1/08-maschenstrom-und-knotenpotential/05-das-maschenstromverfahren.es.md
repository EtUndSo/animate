---
title: Etapa 3: El análisis por mallas
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / Análisis por mallas y por nudos
order: 1180500
summary: La ley de los nudos ya está resuelta; quedan m leyes de las mallas con m incógnitas.
tags: resistencia de acoplamiento
lang: es
---

<span class="anker" id="stufe-3"></span>

:::zweck
La ley de los nudos ya está resuelta; quedan $m$ leyes de las mallas con $m$ incógnitas. Esta etapa las plantea y muestra por qué la matriz se puede leer.
:::

**La idea.** Se recorre una malla en el sentido de su corriente. En cada resistencia cae $R$ por la corriente de rama, y la corriente de rama es la corriente de malla propia más o menos la de las vecinas. Si se ordena por corrientes de malla, delante de la corriente propia queda la suma de todas las resistencias de la malla. Delante de una corriente ajena queda solo lo que ambas mallas recorren en común. Más no puede haber ahí. Por eso la matriz es una lista del circuito.

:::definition Definición 3.1 (Análisis por mallas)
<span class="anker" id="satz-3-1"></span>

El método tiene cuatro pasos:

<ol>

<li>

Convertir las fuentes de corriente reales en fuentes de tensión reales: $U_\mathrm q=I_\mathrm q\,R$, la misma resistencia en serie ([Parte 5](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)).

</li>

<li>

Elegir $m$ mallas independientes y poner en cada una una corriente de malla con sentido arbitrario. El sentido de recorrido de la malla es ese sentido.

</li>

<li>

Plantear la ley de las mallas para cada malla o leer directamente la matriz.

</li>

<li>

Resolver el sistema para las corrientes de malla y calcular a partir de ellas las corrientes y las tensiones de rama.

</li>

</ol>
:::

:::satz Teorema 3.2 (Forma matricial del análisis por mallas)
<span class="anker" id="satz-3-2"></span>

Las corrientes de malla cumplen $\mathbf Z\,\mathbf I=\mathbf U_\mathrm q$:

<span class="anker" id="gl-3-1"></span>
$$\begin{pmatrix}Z_{11}&Z_{12}&\dots&Z_{1m}\\mathbb{Z}_{21}&Z_{22}&\dots&Z_{2m}\\\vdots&\vdots&\ddots&\vdots\\mathbb{Z}_{m1}&Z_{m2}&\dots&Z_{mm}\end{pmatrix} \begin{pmatrix}I_1\\I_2\\\vdots\\I_m\end{pmatrix}= \begin{pmatrix}U_\mathrm{q1}\\U_\mathrm{q2}\\\vdots\\U_{\mathrm qm}\end{pmatrix}. \tag{3.1}$$

<ul>

<li>

$Z_{\mu\mu}$ es la suma de todas las resistencias de la malla $\mu$.

</li>

<li>

$Z_{\mu\nu}$ es la __resistencia de acoplamiento__, la suma de las resistencias que recorren ambas mallas: positiva si ambas corrientes circulan allí en el mismo sentido, negativa si van en sentidos opuestos, cero si no hay rama común. Se cumple $Z_{\mu\nu}=Z_{\nu\mu}$.

</li>

<li>

$U_{\mathrm q\mu}$ es la suma de las tensiones de fuente de la malla, positiva para cada fuente que impulsa la corriente de malla. Con flechas de tensión del polo positivo al negativo (CG, [Parte 2](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)) esto significa: una flecha contra el recorrido cuenta como positiva, una flecha con el recorrido como negativa.

</li>

</ul>
:::

:::herleitung De la ley de las mallas a la matriz
Para la malla $\mu$, la suma de todos los $R_a\,I_a$ es igual a la tensión impulsora $U_{\mathrm q\mu}$, porque las fuentes pasan al lado derecho. Aquí $I_a$ es la corriente en $R_a$, contada en el sentido de recorrido de $\mu$. Según [(2.1)](maschenstrome-erfullen-die-knotenregel.html#gl-2-1), $I_a=I_\mu+\sum_{\nu\neq\mu}\sigma_{a\nu}\,I_\nu$. Al reordenar queda delante de $I_\mu$ la suma de todos los $R_a$ y delante de $I_\nu$ la suma $\sum_a\sigma_{a\nu}R_a$ sobre las resistencias comunes. La malla $\nu$ recibe la misma resistencia con el mismo signo, porque «en el mismo sentido» es una relación entre dos mallas. Por eso $\mathbf Z$ es simétrica.
:::

⁠**Cómo leerlo:** La fila $\mu$ es la ley de las mallas de la malla $\mu$. La columna $\nu$ dice qué tensión produce un amperio de corriente de malla $\nu$ en cada malla. De ahí la unidad ohmio; aquí lo típico son kiloohmios. La letra $Z$ viene de impedancia ([Parte 6](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore/zweitore.html)); aquí son resistencias puras. **Validez:** La red contiene resistencias lineales y fuentes de tensión fijas. La simetría es además una comprobación: un error al plantear suele destruirla.

:::abbildung et1/k8maschen 3
La red modelo para el análisis por mallas. A la derecha, la fuente de corriente se ha convertido en fuente de tensión. En rojo, las resistencias comunes $R_2$ y $R_4$: están fuera de la diagonal de $\mathbf Z$. I y III no tienen rama común; por eso $Z_{13}=0$.
:::

::::beispiel
A la derecha, $U_\mathrm{q5}=I_\mathrm q\,R_5=20$ V con $R_5$ en serie (fig. [3](#abb-3)). Los tres recorridos en sentido horario son

$$\begin{aligned} \text{I:}\quad&R_1I_\mathrm I+R_2(I_\mathrm I-I_\mathrm{II})-U_\mathrm q=0,\\ \text{II:}\quad&R_2(I_\mathrm{II}-I_\mathrm I)+R_3I_\mathrm{II}+R_4(I_\mathrm{II}-I_\mathrm{III})=0,\\ \text{III:}\quad&R_4(I_\mathrm{III}-I_\mathrm{II})+R_5I_\mathrm{III}+U_\mathrm{q5}=0. \end{aligned}$$

Ordenado, en k$\Omega$, mA y V, esto es exactamente lo que también se lee directamente:

$$\begin{pmatrix}R_1+R_2&-R_2&0\\-R_2&R_2+R_3+R_4&-R_4\\0&-R_4&R_4+R_5\end{pmatrix} \begin{pmatrix}I_\mathrm I\\I_\mathrm{II}\\I_\mathrm{III}\end{pmatrix}= \begin{pmatrix}5&-4&0\\-4&16&-10\\0&-10&15\end{pmatrix} \begin{pmatrix}I_\mathrm I\\I_\mathrm{II}\\I_\mathrm{III}\end{pmatrix}= \begin{pmatrix}9\\0\\-20\end{pmatrix}.$$

Todos los elementos fuera de la diagonal son negativos, porque círculos vecinos con el mismo sentido de giro van uno contra otro en la rama común. $U_\mathrm q$ impulsa la malla I, $U_\mathrm{q5}$ actúa contra la malla III. Con [(0.1)](von-grund-auf-drei-gleichungen-drei-unbekannte.html#gl-0-1) y [(0.2)](von-grund-auf-drei-gleichungen-drei-unbekannte.html#gl-0-2) se obtiene

$$D=5\cdot140+4\cdot(-60)=460,\qquad D_1=9\cdot140+4\cdot(-200)=460,$$

$$D_2=5\cdot(-200)-9\cdot(-60)=-460,\qquad D_3=-1600+320+360=-920.$$

Por tanto, $I_\mathrm I=1$ mA, $I_\mathrm{II}=-1$ mA e $I_\mathrm{III}=-2$ mA. El signo menos dice: las mallas II y III van en realidad en sentido antihorario. Las corrientes de rama de la etapa [2](maschenstrome-erfullen-die-knotenregel.html#stufe-2) son 1 mA en $R_1$, 2 mA hacia abajo en $R_2$, 1 mA en $R_3$ del nudo 2 al nudo 1 y 1 mA hacia abajo en $R_4$. **Comprobación:** $U_1=R_2\cdot2\,\mathrm{mA}=8$ V y $U_2=R_4\cdot1\,\mathrm{mA}=10$ V. Malla I: $1+8-9=0$.
::::

⁠**Caso límite:** Para $R_2\to0$ resulta $Z_{12}=0$, y la malla I queda desacoplada: un hilo en el centro separa ambos lados, porque su tensión es cero, circule lo que circule por él.

:::frage ¿Tienen que girar todas las corrientes de malla en el mismo sentido?
No. El mismo sentido de giro solo es cómodo, porque entonces todos los elementos fuera de la diagonal son negativos. Si se invierte una corriente de malla, su fila y su columna cambian de signo, la diagonal se mantiene, y el valor de la corriente también cambia de signo. La corriente de rama no cambia.
:::

:::zusatz Fuente de corriente ideal
Para $R_5\to\infty$, $U_\mathrm{q5}$ crece sin límite y la conversión falla ([Parte 5](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)). Las mallas se colocan entonces de modo que solo una pase por la fuente de corriente. Su corriente de malla es conocida. La ecuación de esa malla se omite, porque contiene la tensión desconocida de la fuente. Una incógnita menos, una ecuación menos.
:::

:::aufgabe Ejercicio 3 ★★ La red de la Parte 2
<span class="anker" id="aufg-3"></span>

La red de la [Parte 2](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html) tiene una fuente ideal de 9 V entre $K_1$ y $K_4$ y $R_\mathrm a=2\,\mathrm{k\Omega}$ ($K_1K_2$), $R_\mathrm b=5\,\mathrm{k\Omega}$ ($K_2K_4$), $R_\mathrm c=3\,\mathrm{k\Omega}$ ($K_1K_3$), $R_\mathrm d=1\,\mathrm{k\Omega}$ ($K_3K_4$), $R_\mathrm e=2\,\mathrm{k\Omega}$ ($K_2K_3$). Las mallas van así: $I_\mathrm A$ por la fuente de $K_4$ a $K_1$, luego $K_2$ y de vuelta a $K_4$. $I_\mathrm B$ de $K_1$ a $K_3$, $K_2$ y de vuelta a $K_1$. $I_\mathrm C$ de $K_2$ a $K_3$, $K_4$ y de vuelta a $K_2$.

<ol class="al">

<li>

Lee $\mathbf Z$ y el lado derecho. Comprueba la simetría.

</li>

<li>

Calcula las corrientes de malla con la regla de Cramer.

</li>

<li>

Determina las cinco corrientes de las resistencias y compara con la [Parte 2](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html).

</li>

</ol>

:::loesung
(a) La malla A contiene $R_\mathrm a$, $R_\mathrm b$; la malla B, $R_\mathrm a$, $R_\mathrm c$, $R_\mathrm e$; la malla C, $R_\mathrm b$, $R_\mathrm d$, $R_\mathrm e$. Todas van en sentidos opuestos en las ramas comunes:

$$\mathbf Z=\begin{pmatrix}7&-2&-5\\-2&7&-2\\-5&-2&8\end{pmatrix}\mathrm{k\Omega},\qquad\mathbf U_\mathrm q=\begin{pmatrix}9\\0\\0\end{pmatrix}\mathrm V.$$

La matriz es simétrica.

(b) $D=7(56-4)+2(-16-10)-5(4+35)=364-52-195=117$. $D_1=9\cdot52=468$, $D_2=234$, $D_3=351$. Por tanto, $I_\mathrm A=4$ mA, $I_\mathrm B=2$ mA, $I_\mathrm C=3$ mA.

(c) $I_\mathrm a=I_\mathrm A-I_\mathrm B=2$ mA, $I_\mathrm b=I_\mathrm A-I_\mathrm C=1$ mA, $I_\mathrm c=I_\mathrm B=2$ mA, $I_\mathrm d=I_\mathrm C=3$ mA, $I_\mathrm e=I_\mathrm C-I_\mathrm B=1$ mA de $K_2$ a $K_3$. Es la tabla de la [Parte 2](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html), con tres ecuaciones en lugar de doce.
:::
:::

:::aufgabe Ejercicio 4 ★★ Invertir y cortocircuitar
<span class="anker" id="aufg-4"></span>

<ol class="al">

<li>

Invierte en la red modelo solo la corriente de malla II. ¿Cómo quedan $\mathbf Z$, el lado derecho e $I_\mathrm{II}$?

</li>

<li>

Predicción: $R_4$ se sustituye por un hilo. ¿Qué elementos de $\mathbf Z$ se anulan? Determina $I_\mathrm{III}$ sin sistema de ecuaciones.

</li>

</ol>

:::loesung
(a) La fila y la columna II cambian de signo, la diagonal se mantiene:

$$\mathbf Z=\begin{pmatrix}5&4&0\\4&16&10\\0&10&15\end{pmatrix}\mathrm{k\Omega},\qquad\mathbf U_\mathrm q=\begin{pmatrix}9\\0\\-20\end{pmatrix}\mathrm V,\qquad I_\mathrm{II}=+1\,\mathrm{mA}.$$

En ambas ramas comunes los círculos van ahora en el mismo sentido. El lado derecho se mantiene porque en la malla II no hay ninguna fuente.

(b) $Z_{23}=Z_{32}=0$, porque $R_4$ era la única resistencia común. La malla III solo contiene ya $R_5$ y $U_\mathrm{q5}$: $I_\mathrm{III}=-20\,\mathrm{V}/5\,\mathrm{k\Omega}=-4$ mA. Es la fuente de corriente convertida en cortocircuito, la corriente de cortocircuito de 4 mA. Las mallas I y II siguen acopladas.
:::
:::

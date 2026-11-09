---
title: Etapa 10: Propiedades y panorama de todas las formas
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / Cuadripolos
order: 1161200
summary: Los cuatro números revelan más que el comportamiento en los puertos.
tags: recíproco, activo, pasivo, funcionamiento en pequeña señal
lang: es
---

<span class="anker" id="stufe-10"></span>

:::zweck
Los cuatro números revelan más que el comportamiento en los puertos. Esta etapa lee en ellos tres propiedades: ¿actúa el cuadripolo igual en ambos sentidos? ¿Actúa siquiera hacia atrás? ¿Puede ganar potencia? Al final, todas las formas aparecen una junto a otra.
:::

**La idea.** Una resistencia no conoce sentido alguno; su corriente solo depende de la diferencia de tensión entre sus dos extremos. Por eso, una red de resistencias actúa del puerto 1 al puerto 2 con la misma fuerza que al revés: si se intercambian la causa y el lugar del efecto, el cociente no cambia. Una fuente controlada, en cambio, tiene un sentido. Actúa de la magnitud de control sobre su salida, nunca al revés. Solo ella puede romper la simetría. Y solo ella puede aportar energía desde fuera.

:::definition Definición 10.1 (Recíproco, unilateral, activo)
<span class="anker" id="satz-10-1"></span>

Un cuadripolo se llama __recíproco__ (también reversible, de transferencia simétrica) si una misma causa muestra el mismo efecto en ambos sentidos. Se llama unilateral si la entrada no depende de la salida:

<span class="anker" id="gl-10-1"></span>
<span class="anker" id="gl-10-2"></span>
$$\begin{aligned} \text{recíproco:}\quad&Z_{12}=Z_{21},\quad Y_{12}=Y_{21},\quad H_{12}=-H_{21},\quad\det\mathbf A=1,\\ \text{unilateral:}\quad&Z_{12}=0,\quad Y_{12}=0,\quad H_{12}=0,\quad\det\mathbf A=0. \end{aligned} \tag{10.1|10.2}$$

La potencia absorbida por el cuadripolo es, con $P_1=U_1I_1$ y la potencia entregada $P_2=-U_2I_2$,

<span class="anker" id="gl-10-3"></span>
$$P=P_1-P_2=U_1I_1+U_2I_2=Y_{11}U_1^2+(Y_{12}+Y_{21})U_1U_2+Y_{22}U_2^2. \tag{10.3}$$

El cuadripolo es __activo__ si en algún estado de funcionamiento es posible $P<0$, y __pasivo__ si siempre se cumple $P\ge0$.
:::

⁠**Cómo leerlo:** Si 1 A en el puerto 1 produce una tensión en el puerto 2 abierto, en el cuadripolo recíproco 1 A en el puerto 2 produce la misma tensión en el puerto 1 abierto (fig. [12](#abb-12)). Eso es $Z_{21}=Z_{12}$. En las ecuaciones de nudos ([Parte 8](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/maschenstrom-und-knotenpotentialverfahren/maschenstrom-und-knotenpotential.html)), cada resistencia inscribe su conductancia en dos lugares especulares; por eso, la matriz sigue siendo simétrica. Recíproco no significa especular: el cuadripolo T tiene $Z_{11}\neq Z_{22}$ y, aun así, es recíproco. Como el cuarto parámetro está fijado, un cuadripolo recíproco solo tiene tres parámetros libres, en correspondencia con los tres elementos de T y $\pi$. Siempre se puede reproducir con una red en T o en $\pi$ sin fuentes; los valores de los elementos pueden ser negativos. En el unilateral también son libres tres números: resistencia de entrada, resistencia de salida, magnitud de control. Es la forma básica del amplificador. Las condiciones para $\mathbf A$ y $\mathbf H$ se deducen de las conversiones de abajo. En [(10.3)](#gl-10-3), el signo menos está en $P_2$ porque $I_2$ apunta hacia dentro. La última forma se obtiene sustituyendo [(5.1)](admittanzform-und-kurzschlussversuch.html#gl-5-1).

:::abbildung et1/k6umkehr 12
Izquierda: cuadripolo T. 100 mA dan 2 V en el otro puerto, abierto, en ambos sentidos, aunque $R_\mathrm{a}\neq R_\mathrm{c}$. Derecha: modelo de amplificador. 1 µ A en el puerto 1 da $-2$ V en el puerto 2; 1 µ A en el puerto 2 da 0 V en el puerto 1.
:::

::::beispiel
El cuadripolo T absorbe $P_1=7{,}75\,\mathrm{V}\cdot250\,\mathrm{mA}=1{,}9375$ W y entrega $P_2=3\,\mathrm{V}\cdot50\,\mathrm{mA}=0{,}15$ W. La diferencia $P=1{,}7875$ W es exactamente el calor en las resistencias: $0{,}9375+0{,}8+0{,}05$ W. Cada resistencia absorbe $I^2R\geq0$; por eso, un cuadripolo de resistencias siempre es pasivo. Esto vale también con condensadores y bobinas. Los cuadripolos pasivos pueden incluso contener fuentes controladas; lo que decide es solo $P$. El modelo de amplificador absorbe $P_1=20\,\mathrm{mV}\cdot10\,\mu\text{A}=0{,}2$ µ W y entrega a la carga $P_2=4\,\mathrm{V}\cdot0{,}8\,\mathrm{mA}=3{,}2$ mW, 16 000 veces más. Es activo. La energía no procede de la señal de entrada, sino de una fuente auxiliar para la alimentación, que no aparece en el modelo del cuadripolo. Este modelo vale para señales pequeñas en torno a un estado fijo de continua (__funcionamiento en pequeña señal__, [Parte 10](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor/der-bipolartransistor.html)).
::::

⁠**Casos límite:** Para $U_1=U_2=0$ es $P=0$. Un cuadripolo de hilos ideales tiene $P=0$ en todo estado; es pasivo, y nada se pierde.

:::ltspice De dónde viene la potencia
⁠**Esquema:** fuente `voltage` con `20m` de `1` a masa, `Rent` con `2k` de `1` a masa. La fuente de corriente controlada `g` con `50m`: salida de `2` a masa, entrada de control de `1` a masa. `res` con `20k` y `res` con `5k` de `2` a masa. El valor es $Y_{21}=H_{21}/H_{11}$.

⁠**Directivas:** `.op`, `.meas op Usal FIND V(2)`, `.meas op Pent PARAM V(1)*I(Rent)`, `.meas op Pcarga PARAM V(2)*V(2)/5000`, `.meas op Pg PARAM V(2)*I(G1)`.

⁠**Lo que ves:** $\mathtt{Usal}=-4$ V, `Pent` $=0{,}2$ µ W, `Pcarga` $=3{,}2$ mW, `Pg` $=-4$ mW. La fuente controlada entrega 4 mW, de los que 3,2 mW van a la carga; el resto calienta los 20 k$\Omega$. Para el ejercicio [10](#aufg-10)(b), pon los valores `10m`, `1k`, `50m`, `50k` y `10k`: $\mathtt{Usal}=-4{,}17$ V.
:::

**Todas las formas de un vistazo.** Las mismas cuatro magnitudes, cuatro elecciones de las causas:

| Forma | Causas | Efectos | Cuadripolo T |
|---|---|---|---|
| Z (matriz de resistencias) | $I_1$, $I_2$ | $U_1$, $U_2$ | $Z_{11}=35\,\Omega$, $Z_{12}=Z_{21}=20\,\Omega$, $Z_{22}=40\,\Omega$ |
| Y (matriz de conductancias) | $U_1$, $U_2$ | $I_1$, $I_2$ | $Y_{11}=40$ mS, $Y_{12}=Y_{21}=-20$ mS, $Y_{22}=35$ mS |
| H (matriz serie-paralelo) | $I_1$, $U_2$ | $U_1$, $I_2$ | $H_{11}=25\,\Omega$, $H_{12}=0{,}5$, $H_{21}=-0{,}5$, $H_{22}=25$ mS |
| A (matriz de cadena) | $U_2$, $-I_2$ | $U_1$, $I_1$ | $A_{11}=1{,}75$, $A_{12}=50\,\Omega$, $A_{21}=50$ mS, $A_{22}=2$ |

Cada conversión se obtiene despejando las dos ecuaciones para las nuevas magnitudes. Para consulta, cada matriz buscada a partir de las otras tres:

$$\mathbf Z=\begin{pmatrix}\frac{Y_{22}}{\det\mathbf Y}&\frac{-Y_{12}}{\det\mathbf Y}\\[3pt]\frac{-Y_{21}}{\det\mathbf Y}&\frac{Y_{11}}{\det\mathbf Y}\end{pmatrix} =\begin{pmatrix}\frac{\det\mathbf H}{H_{22}}&\frac{H_{12}}{H_{22}}\\[3pt]\frac{-H_{21}}{H_{22}}&\frac{1}{H_{22}}\end{pmatrix} =\begin{pmatrix}\frac{A_{11}}{A_{21}}&\frac{\det\mathbf A}{A_{21}}\\[3pt]\frac{1}{A_{21}}&\frac{A_{22}}{A_{21}}\end{pmatrix},$$

$$\mathbf Y=\begin{pmatrix}\frac{Z_{22}}{\det\mathbf Z}&\frac{-Z_{12}}{\det\mathbf Z}\\[3pt]\frac{-Z_{21}}{\det\mathbf Z}&\frac{Z_{11}}{\det\mathbf Z}\end{pmatrix} =\begin{pmatrix}\frac{1}{H_{11}}&\frac{-H_{12}}{H_{11}}\\[3pt]\frac{H_{21}}{H_{11}}&\frac{\det\mathbf H}{H_{11}}\end{pmatrix} =\begin{pmatrix}\frac{A_{22}}{A_{12}}&\frac{-\det\mathbf A}{A_{12}}\\[3pt]\frac{-1}{A_{12}}&\frac{A_{11}}{A_{12}}\end{pmatrix},$$

$$\mathbf H=\begin{pmatrix}\frac{\det\mathbf Z}{Z_{22}}&\frac{Z_{12}}{Z_{22}}\\[3pt]\frac{-Z_{21}}{Z_{22}}&\frac{1}{Z_{22}}\end{pmatrix} =\begin{pmatrix}\frac{1}{Y_{11}}&\frac{-Y_{12}}{Y_{11}}\\[3pt]\frac{Y_{21}}{Y_{11}}&\frac{\det\mathbf Y}{Y_{11}}\end{pmatrix} =\begin{pmatrix}\frac{A_{12}}{A_{22}}&\frac{\det\mathbf A}{A_{22}}\\[3pt]\frac{-1}{A_{22}}&\frac{A_{21}}{A_{22}}\end{pmatrix},$$

$$\mathbf A=\begin{pmatrix}\frac{Z_{11}}{Z_{21}}&\frac{\det\mathbf Z}{Z_{21}}\\[3pt]\frac{1}{Z_{21}}&\frac{Z_{22}}{Z_{21}}\end{pmatrix} =\begin{pmatrix}\frac{-Y_{22}}{Y_{21}}&\frac{-1}{Y_{21}}\\[3pt]\frac{-\det\mathbf Y}{Y_{21}}&\frac{-Y_{11}}{Y_{21}}\end{pmatrix} =\begin{pmatrix}\frac{-\det\mathbf H}{H_{21}}&\frac{-H_{11}}{H_{21}}\\[3pt]\frac{-H_{22}}{H_{21}}&\frac{-1}{H_{21}}\end{pmatrix}.$$

De $\mathbf A$ se sigue la condición de [(10.1)](#gl-10-1) y [(10.2)](#gl-10-2): con la primera línea, $Z_{12}=\det\mathbf A/A_{21}$ y $Z_{21}=1/A_{21}$, es decir, $\det\mathbf A=Z_{12}/Z_{21}$. Esto es 1 en la reciprocidad y 0 en el caso unilateral. Del mismo modo, $Z_{12}=H_{12}/H_{22}$ y $Z_{21}=-H_{21}/H_{22}$, de ahí $H_{12}=-H_{21}$.

:::frage Entonces, ¿no recíproco significa activo?
No. La reciprocidad es una afirmación sobre la simetría; la actividad, sobre la potencia. Ambas dependen de las fuentes controladas, pero no son lo mismo. El ejercicio [10](#aufg-10)(d) muestra un cuadripolo con $Z_{12}\neq Z_{21}$ que nunca gana potencia.
:::

:::aufgabe Ejercicio 10 ★★ Leer las propiedades
<span class="anker" id="aufg-10"></span>

Comprueba para cada cuadripolo: ¿es recíproco? ¿Unilateral? ¿Activo o pasivo?

<ol class="al">

<li>

$Y_{11}=2$ mS, $Y_{12}=Y_{21}=-1$ mS, $Y_{22}=3$ mS. Pista: dibuja la red en $\pi$.

</li>

<li>

$H_{11}=1$ k$\Omega$, $H_{12}=0$, $H_{21}=50$, $H_{22}=20$ µ S, carga de 10 k$\Omega$, $U_1=10$ mV.

</li>

<li>

$A_{11}=2$, $A_{12}=30\,\Omega$, $A_{21}=0{,}1$ S, $A_{22}=2$.

</li>

<li>

$Z_{11}=Z_{22}=10\,\Omega$, $Z_{12}=5\,\Omega$, $Z_{21}=-5\,\Omega$. Para ello, calcula $P$ a partir de $U_1I_1+U_2I_2$.

</li>

</ol>

:::loesung
(a) Recíproco, $Y_{12}=Y_{21}$, no unilateral. Red en $\pi$ con $G_2=1$ mS, $G_1=1$ mS, $G_3=2$ mS, todas positivas: resistencias, luego pasivo.

(b) $H_{12}=0$: unilateral, no recíproco ($H_{21}\neq-H_{12}$). $I_1=10$ µ A, y la salida impulsa 0,5 mA en $50\,\text{k}\Omega\parallel10\,\text{k}\Omega=8{,}33$ k$\Omega$, $U_2=-4{,}17$ V. $P_1=0{,}1$ µ W, $P_2=U_2^2/R_\mathrm{L}=1{,}74$ mW. Activo.

(c) $\det\mathbf A=4-3=1$: recíproco, no unilateral. Con $Z_{11}=Z_{22}=20\,\Omega$, $Z_{12}=Z_{21}=10\,\Omega$, una T de resistencias positivas 10, 10, 10 $\Omega$: pasivo y, por $A_{11}=A_{22}$, incluso especular.

(d) $Z_{12}=5\,\Omega\neq Z_{21}=-5\,\Omega$: no recíproco, no unilateral. $P=I_1(10I_1+5I_2)+I_2(-5I_1+10I_2)=10\,\Omega\,(I_1^2+I_2^2)\geq0$: pasivo. Los términos mixtos se anulan. Es un cuadripolo no recíproco, pero pasivo.
:::
:::

---
title: Etapa 3: La zona de carga espacial
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / Semiconductores y diodos
order: 1190500
summary: Una pieza n y una pieza p son, por separado, solo resistencias.
tags: difusión, carga espacial, deriva, tensión de difusión
lang: es
---

<span class="anker" id="stufe-3"></span>

:::zweck
Una pieza n y una pieza p son, por separado, solo resistencias. Esta etapa muestra qué surge en su límite y por qué es una barrera.
:::

**La idea.** En un cristal, una región p limita con una región n. Ocurren cuatro pasos (fig. [4](#abb-4)):

<ol>

<li>

⁠**Difusión.** Los portadores de carga se mueven de forma desordenada. De la parte de alta densidad salen más de los que entran. Esta igualación por movimiento aleatorio se llama __difusión__. Los electrones pasan de la región n a la p, los huecos al revés.

</li>

<li>

⁠**Recombinación.** En la región ajena, los viajeros se encuentran con la mayoría de allí y desaparecen. Cerca del límite casi no quedan portadores libres.

</li>

<li>

⁠**Quedan iones fijos.** Allí los iones ya no están compensados: $\mathrm P^+$ en el lado n, $\mathrm B^-$ en el lado p. Esta carga fija se llama __carga espacial__, y la capa, zona de carga espacial.

</li>

<li>

⁠**El campo detiene la igualación.** Los iones crean un campo del lado n al lado p. Empuja a los electrones de vuelta a la región n y a los huecos de vuelta a la región p (__deriva__, [Parte 2](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)). La zona crece hasta que la corriente de deriva anula exactamente la corriente de difusión.

</li>

</ol>

:::abbildung et1/k9rlz 4
Unión pn sin tensión externa. Arriba: los recuadros son iones fijos, los círculos rellenos electrones, los círculos abiertos huecos. En la zona faltan los portadores móviles, y el campo $E$ apunta hacia el lado p. Abajo: el potencial sube solo en la zona, en total $U_\mathrm{D0}=0{,}71$ V. Este escalón de potencial frena a los electrones en su camino hacia el lado p.
:::

:::satz Teorema 3.1 (Tensión de difusión y anchura de la zona)
<span class="anker" id="satz-3-1"></span>

Para una unión abrupta, con la tensión térmica $U_T=k_\mathrm BT/e$, se cumple

<span class="anker" id="gl-3-1"></span>
$$U_\mathrm{D0}=U_T\ln\frac{N_\mathrm AN_\mathrm D}{n_\mathrm i^2},\qquad w=\sqrt{\frac{2\varepsilon}{e}\Bigl(\frac1{N_\mathrm A}+\frac1{N_\mathrm D}\Bigr)U_\mathrm{D0}},\qquad E_\mathrm{max}=\frac{2U_\mathrm{D0}}{w}. \tag{3.1}$$
:::

⁠**Cómo leerlo:** $U_\mathrm{D0}$ es la __tensión de difusión__, el escalón de potencial entre las dos regiones, de unos 0,7 a 0,9 V en el silicio. Camino del lado p, los electrones ven una barrera de energía $W_\mathrm B=e\,U_\mathrm{D0}$. $w$ es la anchura de la zona, $\varepsilon=\varepsilon_0\varepsilon_\mathrm r=1{,}04\cdot10^{-10}$ A s/(V m) la permitividad ([Parte 3](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator/der-kondensator.html)). La zona penetra más en la región menos dopada: $w_\mathrm n/w_\mathrm p=N_\mathrm A/N_\mathrm D$. **Validez:** equilibrio; introduce las densidades en [(3.1)](#gl-3-1) en 1/m$^3$.

:::herleitung Escalón de potencial y anchura
⁠**Escalón de potencial.** Un electrón en el lado p ha subido la barrera. Según [(0.1)](von-grund-auf-ventil-wechselspannung-und-warmeenergie.html#gl-0-1), para las densidades se cumple $n_\mathrm p/n_\mathrm n=\mathrm{e}^{-U_\mathrm{D0}/U_T}$. Con $n_\mathrm n=N_\mathrm D$ y $n_\mathrm p=n_\mathrm i^2/N_\mathrm A$ de [(2.1)](dotierung.html#gl-2-1) se obtiene la primera ecuación.

⁠**Anchura.** Los dos lados llevan la misma carga, así que $N_\mathrm Aw_\mathrm p=N_\mathrm Dw_\mathrm n$. El campo crece linealmente desde los bordes hasta el límite y allí alcanza el valor de una carga superficial ([Parte 3](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator/der-kondensator.html)), $E_\mathrm{max}=e\,N_\mathrm Dw_\mathrm n/\varepsilon$. La tensión es el área bajo la curva del campo, un triángulo: $U_\mathrm{D0}=\tfrac12E_\mathrm{max}w$. Con $w=w_\mathrm n+w_\mathrm p$ esto da [(3.1)](#gl-3-1).
:::

**Ejemplo.** $U_\mathrm{D0}=25{,}85\,\mathrm{mV}\cdot\ln10^{12}=0{,}714$ V, es decir, $27{,}6\,U_T$. Así, la barrera deja pasar la fracción $\mathrm{e}^{-27{,}6}=10^{-12}$, exactamente la relación $10^{4}/10^{16}$ de las densidades. Además, $w=0{,}43$ µ m, la mitad en cada región, y $E_\mathrm{max}=3{,}3$ MV/m, tanto como la intensidad de campo de ruptura del aire ([Parte 1](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)). **Casos límite:** Si un lado está mucho más dopado, la zona queda casi por completo en el otro. Diez veces más dopado en un lado solo sube $U_\mathrm{D0}$ 60 mV.

:::frage En el diodo hay 0,71 V. ¿Por qué se miden 0 V en él, y por qué no impulsa corriente?
El escalón de potencial es real, pero no es el único del circuito. Donde los contactos metálicos se encuentran con el semiconductor surgen otras tensiones de contacto. Alrededor de cualquier circuito cerrado su suma es cero, porque en equilibrio no hay fuente de energía. El escalón solo establece el equilibrio entre difusión y deriva.
:::

:::aufgabe Ejercicio 3 ★★ Una unión asimétrica
<span class="anker" id="aufg-3"></span>

Una unión pn tiene $N_\mathrm A=10^{18}\,\mathrm{cm^{-3}}$ y $N_\mathrm D=10^{15}\,\mathrm{cm^{-3}}$.

<ol class="al">

<li>

Calcula $U_\mathrm{D0}$, $w$ y $E_\mathrm{max}$.

</li>

<li>

¿Qué anchura tiene la zona en cada lado? ¿Por qué está casi por completo en la región poco dopada?

</li>

</ol>

:::loesung
(a) $U_\mathrm{D0}=25{,}85\,\mathrm{mV}\cdot\ln(10^{33}/10^{20})=0{,}774$ V. Como $1/N_\mathrm A$ es despreciable frente a $1/N_\mathrm D$, $w=\sqrt{2\varepsilon U_\mathrm{D0}/(e\,N_\mathrm D)}=1{,}00$ µ m y $E_\mathrm{max}=2U_\mathrm{D0}/w=1{,}55$ MV/m. (b) $w_\mathrm n/w_\mathrm p=1000$, así que $w_\mathrm n=1{,}00$ µ m y $w_\mathrm p=1{,}0$ nm. Los dos lados deben aportar la misma carga iónica. En la región poco dopada los iones están mil veces más dispersos, así que hace falta mil veces más profundidad.
:::
:::

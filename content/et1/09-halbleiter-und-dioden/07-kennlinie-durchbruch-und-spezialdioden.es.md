---
title: Etapa 5: Curva característica, ruptura y diodos especiales
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / Semiconductores y diodos
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden
knoten: Capítulo 9: Semiconductores y diodos
order: 1190700
summary: La ecuación está lista.
tags: ánodo, cátodo, efecto avalancha, efecto Zener, ruptura, capacidad de unión, fotones, efecto fotoeléctrico interno
lang: es
---

<span class="anker" id="stufe-5"></span>

:::zweck
La ecuación está lista. Esta etapa la lee como curva, añade la ruptura y muestra qué más se puede construir con las propiedades de la unión.
:::

**La idea.** El lado p se llama __ánodo__, el lado n __cátodo__; ambos llevan contactos metálicos. El triángulo del símbolo de circuito apunta en sentido directo. En representación lineal parece verse un codo en 0,6 V (fig. [6](#abb-6)). Se debe a la escala, porque una función exponencial no tiene umbral. En un eje hasta 10 mA, la curva alcanza el 1 % del valor final a 0,595 V; en un eje hasta 10 µ A, ya a 0,417 V. En escala logarítmica es una recta.

:::abbildung et1/k9kennlinie 6
Estructura, símbolo de circuito con flechas de referencia y curva característica del modelo de referencia. Centro: lineal; la corriente inversa $10^{-14}$ A es invisible. Derecha: en escala logarítmica, una recta que solo se curva cerca de $U=0$ por el sumando $-1$.
:::

**Ruptura.** Con una tensión inversa grande, el campo en la zona se hace tan intenso que los portadores liberan nuevos pares por colisiones (__efecto avalancha__) o los electrones pasan directamente de la BV a la BC (__efecto Zener__). La corriente inversa sube bruscamente; esto es la __ruptura__. En sí misma no hace daño. Un diodo solo se destruye por el calor $P=U\,I$ si nada limita la corriente.

**Diodo Zener.** Está hecho para funcionar en ruptura y tiene una tensión $U_\mathrm Z$ exactamente definida (fig. [7](#abb-7) izquierda). En sentido directo se comporta como un diodo pn. Más allá de $U_\mathrm Z$ la curva característica es casi vertical, y su pequeña resistencia es $r_\mathrm Z=\Delta U/\Delta I$. Una resistencia en serie absorbe las fluctuaciones de la fuente: la tensión en el componente apenas cambia, la corriente sí. Con $r_\mathrm Z=10\,\Omega$, un cambio de corriente de 18 mA causa solo 0,18 V.

**Diodo varicap.** La zona sin portadores es una capa aislante entre dos regiones conductoras, es decir, un condensador ([capítulo 3](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator/der-kondensator.html)) de área $A$ y separación $w$. La __capacidad de unión__ disminuye con la tensión inversa $U_\mathrm R=-U$, porque la zona crece:

<span class="anker" id="gl-5-1"></span>
$$C_\mathrm{j}=\frac{\varepsilon A}{w}=\frac{C_0}{\sqrt{1+U_\mathrm R/U_\mathrm{D0}}}. \tag{5.1}$$

Con $A=1\,\mathrm{mm^2}$, $C_0=241$ pF; a 25 V son 40 pF y $w=2{,}6$ µ m. **Validez:** unión abrupta, funcionamiento en sentido inverso. Los diodos con un efecto especialmente fuerte se llaman diodos varicap. Con ellos se ajusta por tensión la frecuencia de circuitos resonantes, por ejemplo en receptores de radio. Un circuito resonante de bobina y condensador oscila a una frecuencia que depende de $C$.

:::abbildung et1/k9spezial 7
Izquierda: diodo Zener con $U_\mathrm Z=5{,}1$ V y $r_\mathrm Z=10\,\Omega$. Centro: capacidad según [(5.1)](#gl-5-1). Derecha: célula solar con $I_\mathrm S=1$ nA para tres iluminaciones. La corriente sigue a la luz, la tensión de circuito abierto apenas. Abajo: símbolos de circuito y circuito equivalente del fotodiodo.
:::

**Fotodiodo.** La luz se compone de paquetes de energía, los __fotones__, con $W=h\,c/\lambda$ ($h$: constante de Planck, $c$: velocidad de la luz, $\lambda$: longitud de onda). Si $W\ge W_\mathrm g$, un fotón eleva un electrón a la BC (__efecto fotoeléctrico interno__). En el silicio esto exige $\lambda\le1107$ nm. El campo de la zona separa el par: el electrón va al lado n, el hueco al lado p. Esto es una corriente de cátodo a ánodo a través del diodo, es decir, en sentido inverso, y es proporcional a la potencia luminosa.

:::satz Teorema 5.1 (Diodo iluminado)
<span class="anker" id="satz-5-1"></span>

La curva característica se desplaza hacia abajo en la __fotocorriente__ $I_\mathrm{Ph}$. El circuito equivalente es una fuente de corriente en paralelo con el diodo:

<span class="anker" id="gl-5-2"></span>
$$I=I_\mathrm S\bigl(\mathrm{e}^{U/U_T}-1\bigr)-I_\mathrm{Ph},\qquad\text{circuito abierto }(I=0):\ U_\mathrm L=U_T\ln\Bigl(\frac{I_\mathrm{Ph}}{I_\mathrm S}+1\Bigr). \tag{5.2}$$
:::

⁠**Cómo leerlo:** Como sensor de luz, el fotodiodo se usa en sentido inverso; entonces $I\approx-I_\mathrm{Ph}$. Una __célula solar__ es un fotodiodo de gran superficie que trabaja con $U>0$ e $I<0$: el producto $U\,I$ es negativo, así que entrega potencia. Diez veces más luz multiplica $I_\mathrm{Ph}$ por diez, pero sube $U_\mathrm L$ solo 60 mV. La razón es el logaritmo de [(5.2)](#gl-5-2). La tensión depende sobre todo del material; en el silicio, en funcionamiento, unos 0,5 V. En el modelo con $I_\mathrm S=1$ nA, $U_\mathrm L=0{,}505$ V, 0,536 V y 0,564 V a 0,3 A, 1 A y 3 A. **Caso límite:** $I_\mathrm{Ph}=0$ da [(4.1)](warum-der-strom-exponentiell-wachst.html#gl-4-1) y $U_\mathrm L=0$.

:::frage Pero el diodo solo conduce a partir de 0,6 V. ¿No es eso un umbral?
En un circuito con corrientes de alrededor de 1 mA lo parece: a 0,4 V circulan solo 52 nA, apenas medibles. Pero la corriente crece de forma uniforme desde 0 V, un factor 10 por cada 60 mV. No hay ninguna tensión a la que algo conmute. Solo el valor se vuelve en algún momento importante para el circuito.
:::

:::aufgabe Ejercicio 5 ★★ Mantener una tensión
<span class="anker" id="aufg-5"></span>

Un diodo Zener con $U_\mathrm Z=5{,}1$ V y $r_\mathrm Z=10\,\Omega$ está conectado a través de $R=220\,\Omega$ a una fuente que fluctúa entre 10 V y 14 V.

<ol class="al">

<li>

¿Cuánto vale la corriente en los dos extremos si el diodo mantiene exactamente 5,1 V?

</li>

<li>

¿Cuánto cambia realmente la tensión del diodo? ¿En qué factor se ha reducido la fluctuación?

</li>

<li>

¿Qué potencia disipa el diodo a 14 V?

</li>

</ol>

:::loesung
(a) $I=(10\,\mathrm{V}-5{,}1\,\mathrm{V})/220\,\Omega=22{,}3$ mA y $(14\,\mathrm{V}-5{,}1\,\mathrm{V})/220\,\Omega=40{,}5$ mA. (b) $\Delta U=r_\mathrm Z\Delta I=10\,\Omega\cdot18{,}2\,\mathrm{mA}=0{,}18$ V. Más exactamente, $R$ divide con $r_\mathrm Z$: $4\,\mathrm{V}\cdot10/230=0{,}17$ V. La fluctuación es 23 veces menor. (c) $P=5{,}1\,\mathrm{V}\cdot40{,}5\,\mathrm{mA}=0{,}21$ W.
:::
:::

:::aufgabe Ejercicio 6 ★★ Célula solar
<span class="anker" id="aufg-6"></span>

Una célula tiene $I_\mathrm S=1$ nA y, a pleno sol, $I_\mathrm{Ph}=3$ A.

<ol class="al">

<li>

Calcula $U_\mathrm L$. ¿Cómo cambia $U_\mathrm L$ si la luz baja a un tercio?

</li>

<li>

Calcula $I$ y la potencia entregada con $U=0{,}5$ V.

</li>

<li>

¿Cuántas células en serie se necesitan para cargar una batería de 14 V con 0,5 V cada una?

</li>

</ol>

:::loesung
(a) $U_\mathrm L=25{,}85\,\mathrm{mV}\cdot\ln(3\cdot10^{9}+1)=0{,}564$ V. A 1 A, $U_\mathrm L=0{,}536$ V, solo 28 mV menos. (b) $I=10^{-9}\,\mathrm{A}\cdot(\mathrm{e}^{19{,}34}-1)-3\,\mathrm{A}=0{,}25\,\mathrm{A}-3\,\mathrm{A}=-2{,}75$ A. Se entregan $0{,}5\,\mathrm{V}\cdot2{,}75\,\mathrm{A}=1{,}37$ W. (c) $14\,\mathrm{V}/0{,}5\,\mathrm{V}=28$ células.
:::
:::

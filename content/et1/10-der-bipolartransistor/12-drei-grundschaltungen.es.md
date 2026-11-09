---
title: Etapa 10: Tres circuitos básicos
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / El transistor bipolar
order: 1201200
summary: La entrada y la salida necesitan dos terminales cada una, y el transistor tiene tres en total.
tags: circuito de emisor común, circuito de colector común, seguidor de emisor, circuito de base común, excursión de tensión, búfer
lang: es
---

<span class="anker" id="stufe-10"></span>

:::zweck
La entrada y la salida necesitan dos terminales cada una, y el transistor tiene tres en total. Por tanto, un terminal se hace común para la señal. Esta etapa calcula las tres posibilidades.
:::

**La idea.** El terminal común da nombre al circuito (fig. [12](#abb-12)). En el __circuito de emisor común__, la señal entra por la base y sale por el colector. $u_\mathrm{ent}$ cae por completo en el tramo BE y genera $i_\mathrm{c}=S\,u_\mathrm{ent}$. Esta corriente circula por $R_\mathrm{C}$ y hace bajar el potencial de colector: la salida está invertida. En el __circuito de colector común__, la señal entra por la base y sale por el emisor. El emisor sigue a la base: si se quedara quieto, $U_\mathrm{BE}$ cambiaría, y la corriente resultante lo elevaría enseguida a través de $R_\mathrm{E}$. Por eso se llama también __seguidor de emisor__. En el __circuito de base común__, la base está fija y la señal entra por el emisor. Si el emisor baja, $U_\mathrm{BE}$ sube, y más corriente hace bajar el colector: entrada y salida se mueven en el mismo sentido. El módulo corresponde al del circuito de emisor común.

:::abbildung et1/k10grundschaltungen 12
Arriba, los tres circuitos básicos; abajo, sus curvas características según el modelo de referencia con $U_\mathrm{CC}=12$ V. Emisor común ($R_\mathrm{C}=3$ k$\Omega$): decreciente, abrupta alrededor de 0,6 V. Colector común ($R_\mathrm{E}=3$ k$\Omega$): la salida está unos 0,6 V por debajo de la entrada (gris). Base común: como el emisor común, reflejada en el eje vertical, creciente.
:::

:::satz Teorema 10.1 (Ganancia de tensión de los circuitos básicos)
<span class="anker" id="satz-10-1"></span>

Para señales pequeñas en la región activa, despreciando $r_\mathrm{CE}$, con $A=u_\mathrm{sal}/u_\mathrm{ent}$:

<span class="anker" id="gl-10-1"></span>
$$A_\mathrm{emisor}=-S\,R_\mathrm{C}=-\frac{U_{R_\mathrm{C}}}{U_T},\qquad A_\mathrm{colector}=\frac{S\,R_\mathrm{E}}{1+S\,R_\mathrm{E}}<1,\qquad A_\mathrm{base}=+S\,R_\mathrm{C}. \tag{10.1}$$

Con resistencia de emisor es $A=-R_\mathrm{C}/(R_\mathrm{E}+1/S)\approx-R_\mathrm{C}/R_\mathrm{E}$; con $r_\mathrm{CE}$ es $A_\mathrm{emisor}=-S\,(R_\mathrm{C}\parallel r_\mathrm{CE})$.
:::

⁠**Cómo leerlo:** $U_{R_\mathrm{C}}=I_\mathrm{C}R_\mathrm{C}$ es la tensión continua en la resistencia de colector, 6 V en el modelo de referencia. **En resumen:** la ganancia del circuito de emisor común es la tensión continua en la resistencia de colector dividida por $U_T$. Ni $B$ ni el tipo de transistor aparecen en ella. **Validez:** $|u_\mathrm{be}|\ll U_T$, $R_\mathrm{C}\ll r_\mathrm{CE}$, excitación por una fuente de resistencia interna pequeña.

:::herleitung Tres mallas en pequeña señal
Para la señal, $U_\mathrm{CC}$ es masa. Emisor común: $u_\mathrm{be}=u_\mathrm{ent}$, $u_\mathrm{sal}=-R_\mathrm{C}i_\mathrm{c}=-R_\mathrm{C}S\,u_\mathrm{ent}$, y con $S=I_\mathrm{C}/U_T$ se deduce $S\,R_\mathrm{C}=I_\mathrm{C}R_\mathrm{C}/U_T$. Con resistencia de emisor: $u_\mathrm{ent}=u_\mathrm{be}+R_\mathrm{E}S\,u_\mathrm{be}$, la mayor parte de $u_\mathrm{ent}$ cae en $R_\mathrm{E}$, y el resto, $u_\mathrm{be}=u_\mathrm{ent}/(1+S\,R_\mathrm{E})$, controla. Colector común: $u_\mathrm{sal}=R_\mathrm{E}S\,u_\mathrm{be}$ con $u_\mathrm{be}=u_\mathrm{ent}-u_\mathrm{sal}$, despejar. Base común: la base está en reposo, así que $u_\mathrm{be}=-u_\mathrm{ent}$ y $u_\mathrm{sal}=-R_\mathrm{C}S\,u_\mathrm{be}=+S\,R_\mathrm{C}u_\mathrm{ent}$.
:::

::::beispiel
Emisor común en el punto A: $A=-6\,\mathrm{V}/26\,\mathrm{mV}=-231$, con $r_\mathrm{CE}$ más exactamente $-215$. 1 mV en la entrada se convierte en 0,23 V en la salida. El punto central permite una __excursión de tensión__, una amplitud de salida, de casi 6 V, pero con 25 mV en la entrada la tangente hace tiempo que ya no vale. Para el límite de pequeña señal de 2,6 mV son 0,6 V. En un amplificador, el punto de trabajo debe estar en la zona de pendiente casi constante, y la excursión debe ser lo mayor posible. La versión con realimentación negativa tiene $A=-3\,\text{k}\Omega/(1\,\text{k}\Omega+12{,}9\,\Omega)=-2{,}96$: solo el 1,3 % de $u_\mathrm{ent}$ cae en el tramo BE, pero a cambio la ganancia queda determinada casi solo por dos resistencias. Seguidor de emisor con $R_\mathrm{E}=3$ k$\Omega$ a 2 mA: $S\,R_\mathrm{E}=231$, $A=0{,}996$. Su punto fuerte no es la tensión, sino la corriente: la ganancia de corriente es $1+B=201$. Sirve de __búfer__: apenas carga la fuente y excita la carga con baja impedancia.
::::

⁠**Casos límite:** $R_\mathrm{E}\to0$ en la forma con realimentación negativa da $-S\,R_\mathrm{C}$. $R_\mathrm{E}\to\infty$ en el seguidor de emisor da $A\to1$.

| Circuito | $A$ | Resistencia de entrada | Resistencia de salida | Uso |
|---|---|---|---|---|
| Emisor común | $-231$ | $r_\mathrm{BE}=2{,}6$ k$\Omega$ | $R_\mathrm{C}=3$ k$\Omega$ | Amplificar tensión |
| Colector común | $0{,}996$ | $r_\mathrm{BE}+(1+B)R_\mathrm{E}=606$ k$\Omega$ | $1/S=13\,\Omega$ | Búfer, ganancia de corriente |
| Base común | $+231$ | $1/S=13\,\Omega$ | $R_\mathrm{C}=3$ k$\Omega$ | Amplificar una fuente de baja impedancia |

:::frage Un circuito de emisor común real tiene una curva característica más plana que el de base común. ¿Por qué iba a ser igual el módulo?
Es igual con excitación directa, igual $R_\mathrm{C}$ e igual corriente. Si delante de la base hay una resistencia en serie o una fuente con resistencia interna, esta forma con $r_\mathrm{BE}$ un divisor de tensión, y solo una parte de $u_\mathrm{ent}$ llega al tramo BE. Entonces la curva característica del circuito de emisor común es más plana. En el circuito de base común no existe este divisor, porque la fuente de baja impedancia está en el emisor.
:::

:::ltspice La curva característica de transferencia del circuito de emisor común
⁠**Esquema:** `voltage` `VCC` con 12 en `res` 3k hacia el colector (red `c`), `npn` con modelo `T`, emisor a masa, en la base `voltage` `VE`.

⁠**Directivas:** el modelo de la etapa [3](eine-flache-viele-kennlinien.html#stufe-3), `.dc VE 0.5 0.7 0.1m`, `.meas dc a1 FIND V(c) AT=0.5995`, `.meas dc a2 FIND V(c) AT=0.6005`, `.meas dc au PARAM (a2-a1)/1m`.

⁠**Lo que ves:** $U_\mathrm{sal}$ cae de 12 V hasta casi 0, en una ventana de unos 60 mV. `au` da $-213$, frente a $-215$ en el cálculo. LTspice calcula con $U_T=25{,}86$ mV y está en 1,98 mA con $U_\mathrm{BE}=0{,}6$ V. Para el ejercicio [12](#aufg-12), pon `VCC` en 9, la resistencia en 4.7k y los valores `AT` en 0.582 y 0.583: `au` da entonces $-169$ con 0,98 mA.
:::

:::aufgabe Ejercicio 12 ★★★ Amplificador y seguidor
<span class="anker" id="aufg-12"></span>

T trabaja con $I_\mathrm{C}=1$ mA y $U_\mathrm{CE}=4{,}3$ V con $U_\mathrm{CC}=9$ V, $R_\mathrm{C}=4{,}7$ k$\Omega$. (a) Predice cuánto vale $A$ del circuito de emisor común, solo a partir de la tensión en $R_\mathrm{C}$. (b) ¿Cuánto vale la amplitud de salida con $\hat u_\mathrm{ent}=2$ mV? ¿Cómo cambia $r_\mathrm{CE}$ el resultado? (c) Con una resistencia de emisor de 470 $\Omega$: ¿cuánto vale $A$? (d) Como seguidor de emisor con $R_\mathrm{E}=4{,}7$ k$\Omega$: ¿cuánto vale $A$? ¿Está invertida la salida?

:::loesung
(a) $U_{R_\mathrm{C}}=4{,}7$ V, así que $A=-4{,}7\,\mathrm{V}/26\,\mathrm{mV}=-181$.

(b) $\hat u_\mathrm{sal}=0{,}36$ V. Con $r_\mathrm{CE}=78$ k$\Omega$, $A=-S(R_\mathrm{C}\parallel r_\mathrm{CE})=-171$, solo un 6 % menos.

(c) $A=-4{,}7\,\text{k}\Omega/(470\,\Omega+26\,\Omega)=-9{,}5$. La aproximación $-R_\mathrm{C}/R_\mathrm{E}$ da $-10$.

(d) $S\,R_\mathrm{E}=181$, $A=0{,}994$. La salida no está invertida; el emisor sigue a la base en fase.
:::
:::

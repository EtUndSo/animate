---
title: Etapa 7: La realimentación negativa fija el punto de trabajo
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / El transistor bipolar
order: 1200900
summary: El punto de trabajo de la etapa 5 depende de B y de U BE , y ambos son poco fiables.
tags: realimentación de corriente, realimentación de tensión
lang: es
---

<span class="anker" id="stufe-7"></span>

:::zweck
El punto de trabajo de la etapa [5](der-arbeitspunkt.html#stufe-5) depende de $B$ y de $U_\mathrm{BE}$, y ambos son poco fiables. Esta etapa muestra cómo el circuito fija la corriente por sí mismo.
:::

**La idea.** En el modelo de referencia, $I_\mathrm{C}=B\cdot10$ µ A. Un ejemplar con $B=100$ lleva 1 mA ($U_\mathrm{CE}=9$ V), uno con $B=400$ alcanza la saturación. Una tensión $U_\mathrm{BE}$ fija sería peor: a corriente fija, $U_\mathrm{BE}$ baja unos 2 mV por kelvin, y 18 mV duplican la corriente, así que bastan 9 K de calentamiento para duplicar $I_\mathrm{C}$.

El remedio es una resistencia en el emisor. Un divisor mantiene casi fijo el potencial de base. La corriente recorre ahora un lazo contra sí misma:

$I_\mathrm{C}$ sube $\to$ sube la tensión en $R_\mathrm{E}$ $\to$ sube $\varphi_\mathrm{E}$ $\to$ baja $U_\mathrm{BE}=\varphi_\mathrm{B}-\varphi_\mathrm{E}$ $\to$ menos inyección $\to$ $I_\mathrm{C}$ baja.

El efecto debilita su causa: es realimentación negativa, aquí __realimentación de corriente__, porque la corriente por $R_\mathrm{E}$ genera la tensión opuesta. Al final, $U_\mathrm{BE}$ solo cambia en milivoltios, y la corriente se deduce de la ley de Ohm en $R_\mathrm{E}$ en lugar de la función exponencial. La segunda forma une $R_\mathrm{B}$ con el colector (fig. [8](#abb-8), centro). Si $I_\mathrm{C}$ sube, $U_\mathrm{CE}$ baja, y con ella baja $I_\mathrm{B}=(U_\mathrm{CE}-U_\mathrm{BE})/R_\mathrm{B}$. Es la __realimentación de tensión__.

:::abbildung et1/k10gegenkopplung 8
Izquierda, realimentación de corriente con divisor de base; centro, realimentación de tensión. Derecha, $I_\mathrm{C}$ en función de $B$ en el modelo de referencia. Sin realimentación, la corriente crece en proporción a $B$ hasta la saturación (gris). La realimentación de corriente (azul) permanece casi plana; la de tensión (naranja) queda en medio.
:::

:::satz Teorema 7.1 (Punto de trabajo con realimentación negativa)
<span class="anker" id="satz-7-1"></span>

Realimentación de corriente con el divisor $R_1$, $R_2$ y $R_\mathrm{i}=R_1\parallel R_2$:

<span class="anker" id="gl-7-1"></span>
$$U_\mathrm{q}=U_\mathrm{CC}\frac{R_2}{R_1+R_2},\quad I_\mathrm{B}=\frac{U_\mathrm{q}-U_\mathrm{BE}}{(1+B)R_\mathrm{E}+R_\mathrm{i}},\quad I_\mathrm{C}=\frac{U_\mathrm{q}-U_\mathrm{BE}}{R_\mathrm{E}\bigl(1+\frac1B\bigr)+\frac{R_\mathrm{i}}{B}}. \tag{7.1}$$

Para $R_\mathrm{E}\gg R_\mathrm{i}/B$ y $B\gg1$ es $I_\mathrm{C}\approx(U_\mathrm{q}-U_\mathrm{BE})/R_\mathrm{E}$; si además $U_\mathrm{q}\gg U_\mathrm{BE}$, es $I_\mathrm{C}\approx U_\mathrm{CC}R_2/\bigl(R_\mathrm{E}(R_1+R_2)\bigr)$.

Realimentación de tensión con $R_\mathrm{B}$ del colector a la base:

<span class="anker" id="gl-7-2"></span>
$$I_\mathrm{C}=\frac{U_\mathrm{CC}-U_\mathrm{BE}}{R_\mathrm{C}\bigl(1+\frac1B\bigr)+\frac{R_\mathrm{B}}{B}}\approx\frac{U_\mathrm{CC}-U_\mathrm{BE}}{R_\mathrm{C}+\frac{R_\mathrm{B}}{B}},\qquad\text{para } R_\mathrm{C}\gg\frac{R_\mathrm{B}}{B}:\ I_\mathrm{C}\approx\frac{U_\mathrm{CC}-U_\mathrm{BE}}{R_\mathrm{C}}. \tag{7.2}$$
:::

⁠**Cómo leerlo:** $U_\mathrm{q}$ y $R_\mathrm{i}$ describen el divisor como fuente de tensión equivalente ([Parte 5](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)): $U_\mathrm{q}$ es su tensión de circuito abierto, $R_\mathrm{i}$ su resistencia interna. En el denominador, $R_\mathrm{E}$ actúa casi por completo, $R_\mathrm{i}$ solo dividida por $B$. **Validez:** región activa. Hay que comprobarlo al final. $U_\mathrm{BE}$ es aquí un valor fijo; la última aproximación de [(7.1)](#gl-7-1) necesita una $U_\mathrm{q}$ grande.

:::herleitung Las fórmulas a partir de las mallas
El divisor se convierte en la fuente $U_\mathrm{q}$ con $R_\mathrm{i}$ en serie. Con $I_\mathrm{E}=(1+B)I_\mathrm{B}$, la malla por la base y el emisor es

$$U_\mathrm{q}=I_\mathrm{B}R_\mathrm{i}+U_\mathrm{BE}+I_\mathrm{B}(1+B)R_\mathrm{E}.$$

Despejando $I_\mathrm{B}$ y multiplicando por $B$ se obtiene [(7.1)](#gl-7-1). En la realimentación de tensión, por $R_\mathrm{C}$ circula la corriente $I_\mathrm{C}+I_\mathrm{B}$, y por $R_\mathrm{B}$ solo $I_\mathrm{B}$. Con $I_\mathrm{B}=I_\mathrm{C}/B$, la malla es

$$U_\mathrm{CC}-U_\mathrm{BE}=\Bigl(\frac{I_\mathrm{C}}{B}+I_\mathrm{C}\Bigr)R_\mathrm{C}+\frac{I_\mathrm{C}}{B}R_\mathrm{B}.$$

Despejando $I_\mathrm{C}$ se obtiene [(7.2)](#gl-7-2).
:::

**Ejemplo.** Modelo de referencia: $U_\mathrm{q}=2{,}7$ V, $R_\mathrm{i}=6{,}98$ k$\Omega$, $R_\mathrm{i}/B=35\,\Omega\ll1$ k$\Omega$. Con ello, $I_\mathrm{C}=2{,}1\,\mathrm{V}/1040\,\Omega=2{,}02$ mA y $U_\mathrm{CE}=12\,\mathrm{V}-6{,}06\,\mathrm{V}-2{,}03\,\mathrm{V}=3{,}91$ V, luego activa. El potencial de base es 2,63 V, y el divisor lleva 300 µ A, 30 veces $I_\mathrm{B}$.

| $I_\mathrm{C}$ con | $B=100$ | $B=200$ | $B=400$ |
|---|---|---|---|
| sin realimentación ($I_\mathrm{B}=10$ µ A) | 1 mA | 2 mA | 3,93 mA (saturación) |
| realimentación de tensión ($R_\mathrm{B}=540$ k$\Omega$) | 1,35 mA | 1,99 mA | 2,62 mA |
| realimentación de corriente | 1,94 mA | 2,02 mA | 2,06 mA |

Tampoco la temperatura influye ya apenas: 50 K de calentamiento bajan $U_\mathrm{BE}$ en 0,1 V, y con [(7.1)](#gl-7-1) $I_\mathrm{C}$ sube solo un 4,8 %. Con una tensión $U_\mathrm{BE}$ fija se multiplicaría por 47. La realimentación de tensión logra menos, porque aquí $R_\mathrm{B}/B=2{,}7$ k$\Omega$ no es pequeña frente a 3 k$\Omega$. Con $R_\mathrm{B}=100$ k$\Omega$, $I_\mathrm{C}$ solo varía entre 2,83 mA y 3,50 mA, pero entonces solo quedan $U_\mathrm{CE}=2{,}2$ V. **Casos límite:** $R_\mathrm{E}\to0$ da $I_\mathrm{C}=B(U_\mathrm{q}-U_\mathrm{BE})/R_\mathrm{i}$, la fórmula con resistencia de base de la etapa [5](der-arbeitspunkt.html#stufe-5). $B\to\infty$ da $I_\mathrm{C}=(U_\mathrm{q}-U_\mathrm{BE})/R_\mathrm{E}$.

:::frage ¿Qué cuesta la resistencia de emisor?
Dos cosas. La tensión en $R_\mathrm{E}$, aquí 2 V, le falta al colector para la excursión de la señal. Y la realimentación negativa actúa también sobre la señal: la ganancia de tensión baja mucho (etapa [10](drei-grundschaltungen.html#stufe-10)). Un condensador en paralelo con $R_\mathrm{E}$ actúa como un hilo para las señales alternas y elimina el segundo inconveniente.
:::

:::ltspice $I_\mathrm{C}$ es casi independiente de $B$
⁠**Esquema:** `voltage` `VCC` con 12 en la red `cc`. Divisor `res` 31k de `cc` a `b`, 9k de `b` a masa. `npn` con modelo `T`, `res` 3k de `cc` al colector, `res` 1k del emisor a masa.

⁠**Directivas:** `.model T NPN(IS=1.55e-13 BF={BF} VAF=74)`, `.param BF=186`, `.step param BF list 93 186 372`, `.dc VCC 0 12 0.1`, `.meas dc ic FIND Ic(Q1) AT=12`. Los tres valores corresponden a $B=100$, 200, 400 a 6 V.

⁠**Lo que ves:** Tres curvas casi coincidentes. A 12 V, LTspice da 1,94 mA; 2,02 mA; 2,06 mA, exactamente como el cálculo. Introduce los valores del ejercicio [8](#aufg-8) y comprueba tu dispersión.
:::

:::aufgabe Ejercicio 8 ★★★ Diseñar el punto de trabajo
<span class="anker" id="aufg-8"></span>

Diseña con T una realimentación de corriente para $U_\mathrm{CC}=15$ V, $I_\mathrm{C}=1$ mA, 2 V en $R_\mathrm{E}$ y $U_\mathrm{CE}=6$ V. (a) Determina $R_\mathrm{E}$ y $R_\mathrm{C}$ con valores redondos. (b) Por $R_2$ deben circular $10\,I_\mathrm{B}$. Determina $R_2$ y $R_1$ (redondea a 52 k$\Omega$ y 225 k$\Omega$). (c) Calcula $I_\mathrm{C}$ para $B=100$, 200, 400 y compara con el circuito de la tabla. ¿Por qué es mayor la dispersión? Predice el resultado antes de calcular.

:::loesung
(a) $R_\mathrm{E}=2\,\mathrm{V}/1\,\mathrm{mA}=2$ k$\Omega$, $R_\mathrm{C}=(15-6-2)\,\mathrm{V}/1\,\mathrm{mA}=7$ k$\Omega$.

(b) $I_\mathrm{B}=5$ µ A, potencial de base 2,6 V. $R_2=2{,}6\,\mathrm{V}/50\,\mu\text{A}=52$ k$\Omega$. Por $R_1$ circulan 55 µ A: $R_1=12{,}4\,\mathrm{V}/55\,\mu\text{A}=225$ k$\Omega$.

(c) $U_\mathrm{q}=2{,}82$ V, $R_\mathrm{i}=42{,}2$ k$\Omega$. Con [(7.1)](#gl-7-1) resultan $I_\mathrm{C}=0{,}91$ mA; 1,00 mA; 1,05 mA. Predicción: la dispersión es mayor porque $R_\mathrm{i}/B=211\,\Omega$ ya no es pequeña frente a $R_\mathrm{E}$. Aquí el divisor solo lleva diez veces $I_\mathrm{B}$, en lugar de treinta veces. LTspice: 0,92 mA; 1,01 mA; 1,06 mA.
:::
:::

:::aufgabe Ejercicio 9 ★★ Realimentación de tensión
<span class="anker" id="aufg-9"></span>

Toma la realimentación de tensión del ejemplo. (a) Comprueba $I_\mathrm{C}$ y $U_\mathrm{CE}$ para $B=200$. (b) Caso límite $R_\mathrm{B}\to0$: ¿qué valores tienen $U_\mathrm{CE}$ e $I_\mathrm{C}$? ¿Está entonces activo el transistor? Responde con [(4.3)](drei-bereiche-drei-ersatzschaltbilder.html#gl-4-3) y el significado de $U_\mathrm{CB}$.

:::loesung
(a) $I_\mathrm{C}=11{,}4\,\mathrm{V}/(3015\,\Omega+2700\,\Omega)=1{,}99$ mA, $U_\mathrm{CE}=12\,\mathrm{V}-3\,\text{k}\Omega\cdot2{,}005\,\mathrm{mA}=5{,}99$ V.

(b) Base y colector están unidos: $U_\mathrm{CE}=U_\mathrm{BE}=0{,}6$ V e $I_\mathrm{C}=11{,}4\,\mathrm{V}/3015\,\Omega=3{,}78$ mA. Como $U_\mathrm{CE}>0{,}2$ V, el transistor está activo, justo sobre la línea $U_\mathrm{CB}=0$. Es el T1 del espejo de corriente.
:::
:::

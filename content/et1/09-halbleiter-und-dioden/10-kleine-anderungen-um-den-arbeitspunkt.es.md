---
title: Etapa 8: Pequeños cambios alrededor del punto de trabajo
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / Semiconductores y diodos
order: 1191000
summary: A menudo una pequeña señal va montada sobre una tensión continua, y solo cuenta el cambio.
tags: resistencia diferencial, pequeña señal
lang: es
---

<span class="anker" id="stufe-8"></span>

:::zweck
A menudo una pequeña señal va montada sobre una tensión continua, y solo cuenta el cambio. Esta etapa muestra que, para pequeños cambios, el diodo actúa como una resistencia cuyo valor lo fija la corriente continua.
:::

**La idea.** Cerca del PT, toda curva suave coincide con su tangente (fig. [10](#abb-10)). El mecanismo: 1 mV más reduce la barrera en 1 meV. Con ello la fracción por encima de la barrera sube $1/25{,}85=3{,}9$ %, y siempre el mismo porcentaje de la corriente actual. Una corriente grande significa, por tanto, un cambio absoluto grande y, con ello, una resistencia pequeña.

:::abbildung et1/k9kleinsignal 10
Izquierda: detalle de la curva característica alrededor del PT (0,692 V | 4,31 mA). La tangente tiene la pendiente $1/r=0{,}167$ S y corta el eje en $U_\mathrm D-U_T=0{,}667$ V. Derecha: para la pequeña señal, la fuente de tensión continua desaparece y el diodo es la resistencia $r$.
:::

:::satz Teorema 8.1 (Resistencia diferencial)
<span class="anker" id="satz-8-1"></span>

En el PT con la corriente continua $I$, para pequeños cambios $u_\mathrm D$ e $i$ se cumple

<span class="anker" id="gl-8-1"></span>
$$r=\frac{\mathrm{d} U_\mathrm D}{\mathrm{d} I}=\frac{U_T}{I+I_\mathrm S}\approx\frac{U_T}{I},\qquad u_\mathrm D=r\,i. \tag{8.1}$$
:::

⁠**Cómo leerlo:** $r$ se llama __resistencia diferencial__; a 1 mA son 25,85 $\Omega$. Las letras minúsculas son las desviaciones respecto al PT, la __pequeña señal__. **Validez:** $|u_\mathrm D|\ll U_T$. Con 1 mV el error es del 2 %, con 5 mV del 10 %, con 25,85 mV ya del 72 %.

:::herleitung Pendiente de la curva característica
Derivando [(4.1)](warum-der-strom-exponentiell-wachst.html#gl-4-1): $\mathrm{d} I/\mathrm{d} U_\mathrm D=(I_\mathrm S/U_T)\,\mathrm{e}^{U_\mathrm D/U_T}=(I+I_\mathrm S)/U_T$. El inverso es $r$. La función exponencial se reproduce al derivar; por eso en el resultado solo aparece $I$, e $I_\mathrm S$ desaparece en sentido directo. Dos diodos con distinta $I_\mathrm S$ tienen la misma $r$ a la misma corriente.
:::

**Ejemplo.** En el modelo de referencia, $r=25{,}85\,\mathrm{mV}/4{,}31\,\mathrm{mA}=6{,}0\,\Omega$. A la fuente se le suma una senoide con 100 mV de valor de pico. Para los cambios, $R$ y $r$ forman un divisor de tensión:

$$\hat u_\mathrm D=100\,\mathrm{mV}\cdot\frac{6{,}0\,\Omega}{1000\,\mathrm{\Omega}+6{,}0\,\Omega}=0{,}60\,\mathrm{mV},\qquad\hat\imath=\frac{100\,\mathrm{mV}}{1006\,\mathrm{\Omega}}=99{,}4\,\mu\text{A}.$$

El cálculo exacto para $U_0=5{,}1$ V da $+0{,}59$ mV y $+99{,}4$ µ A. En la resistencia aparece casi toda la señal; en el diodo queda el 0,6 %. **Casos límite:** Para $I\to0$, $r=U_T/I_\mathrm S=2{,}6\,\mathrm{T\Omega}$, y el diodo aísla. Para $I$ grande, $r$ tiende a cero; en la realidad queda la resistencia de volumen.

:::ltspice Punto de trabajo y señal
⁠**Esquema:** fuente `voltage` de `in` a masa, valor `5`, en `Advanced` introduce `1` en AC Amplitude. `res` 1k de `in` a `d`, `diode` DM de `d` a masa, modelo como arriba.

⁠**Directivas:** primero `.op`, luego `.ac dec 1 1k 10k`

⁠**Lo que ves:** Con `.op` aparece $V(d)=0{,}693$ V e $I(D1)=4{,}31$ mA. Con `.ac`, en $V(d)$ aparece el valor $-44{,}5$ dB, es decir, la relación 0,00597. Es $r/(R+r)$ del ejemplo. Para el ejercicio [10](#aufg-10), cambia los valores y lee tu $r$.
:::

:::frage ¿Por qué la resistencia del diodo no es $U_\mathrm D/I$?
Eso sería la inversa de la pendiente de la línea del origen al PT: $0{,}692\,\mathrm{V}/4{,}31\,\mathrm{mA}=161\,\Omega$. Describe qué resistencia llevaría la misma corriente en el PT, pero no es una propiedad de la curva característica en ese punto. Cuánto responde la corriente a un cambio lo dice solo la tangente, y esta es 27 veces más empinada. En una resistencia óhmica ambas coinciden.
:::

:::aufgabe Ejercicio 10 ★★ Pendiente y tangente
<span class="anker" id="aufg-10"></span>

<ol class="al">

<li>

Calcula $r$ a 2 mA y a 20 mA.

</li>

<li>

A 2 mA la tensión sube 10 mV. ¿Qué corriente predice la tangente, y cuál la curva característica? ¿Por qué queda la tangente por debajo?

</li>

<li>

Tres diodos iguales en serie llevan 2 mA desde 12 V a través de una resistencia. Calcula la tensión en los tres diodos y la resistencia. ¿Cuánto cambia la tensión en los diodos si la fuente sube 1 V?

</li>

</ol>

:::loesung
(a) 12,9 $\Omega$ y 1,29 $\Omega$. (b) Tangente: $2\,\mathrm{mA}+10\,\mathrm{mV}/12{,}9\,\Omega=2{,}77$ mA. Curva característica: $2\,\mathrm{mA}\cdot\mathrm{e}^{0{,}387}=2{,}94$ mA. Una curva exponencial se curva hacia arriba y siempre queda por encima de su tangente. (c) Tensión $3\cdot0{,}673\,\mathrm{V}=2{,}02$ V, $R=(12\,\mathrm{V}-2{,}02\,\mathrm{V})/2\,\mathrm{mA}=5{,}0\,\mathrm{k\Omega}$. Los tres diodos juntos tienen $r=38{,}8\,\Omega$. De 1 V quedan $1\,\mathrm{V}\cdot38{,}8/5039=7{,}7$ mV.
:::
:::

---
title: Etapa 3: Potencia media con tensión sinusoidal
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / Potencia, adaptación y rendimiento
order: 1170400
summary: Con una tensión alterna, la potencia cambia constantemente.
tags: amplitudes, periodo, frecuencia angular, valor eficaz
lang: es
---

<span class="anker" id="stufe-3"></span>

:::zweck
Con una tensión alterna, la potencia cambia constantemente. Esta etapa encuentra el único número que determina el calentamiento.
:::

**La idea.** En una resistencia, $i$ es proporcional a $u$. Ambas cambian de signo a la vez; por eso su producto nunca es negativo. Si la carga corre hacia atrás, también la tensión está invertida, y vuelve a ceder energía. Ambas semiondas calientan (fig. [4](#abb-4)). La potencia pulsa entre cero y el valor de pico, el doble de rápido que la tensión. Su valor medio está a media altura.

:::abbildung et1/k7sinus 4
A la izquierda, la tensión y la corriente en la resistencia calefactora. A la derecha, la potencia instantánea $p(t)$. Oscila entre 0 y 20 W alrededor del valor medio $P=10$ W y alcanza su máximo el doble de veces que $u$.
:::

:::satz Teorema 3.1 (Potencia media en una resistencia)
<span class="anker" id="satz-3-1"></span>

Con $u(t)=\hat u\cos(\omega t)$ en $R$ circula $i(t)=\hat\imath\cos(\omega t)$, con $\hat\imath=\hat u/R$. El valor medio temporal de la potencia es

<span class="anker" id="gl-3-1"></span>
$$P=\frac1T\int_0^T u(t)\,i(t)\,\mathrm{d} t=\frac12\,\frac{\hat u^2}{R}=\frac12\,\hat\imath^2R. \tag{3.1}$$
:::

⁠**Cómo leerlo:** $\hat u$ y $\hat\imath$ son las __amplitudes__, los valores de pico. $T$ es el __periodo__; $\omega=2\pi/T$, la __frecuencia angular__. En la red eléctrica son $T=20$ ms y $\omega=314$ 1/s. **Validez:** El valor medio se toma sobre periodos enteros. La fórmula solo vale si $i$ es proporcional a $u$, es decir, para resistencias.

:::herleitung De dónde viene el factor $\frac12$
Al sustituir se obtiene $p=u\,i=u^2/R=(\hat u^2/R)\cos^2(\omega t)$. Con $\cos^2x=\frac12(1+\cos2x)$ resulta

$$P=\frac{1}{T\,R}\int_0^T\hat u^2\cos^2(\omega t)\,\mathrm{d} t=\frac{1}{T\,R}\int_0^T\hat u^2\,\frac12\bigl(1+\cos(2\omega t)\bigr)\,\mathrm{d} t=\frac12\,\frac{\hat u^2}{R}.$$

La parte del coseno recorre en $T$ dos oscilaciones completas; su integral es cero. Con $\hat u=R\,\hat\imath$ se obtiene la segunda forma.
:::

**Ejemplo.** Para $\hat u=10$ V y $R=5\,\Omega$ son $\hat\imath=2$ A, el valor de pico de la potencia 20 W y $P=10$ W. A 50 Hz fluyen 0,2 J por periodo a la red cristalina. **Caso límite:** Para $\omega\to0$, $u$ se convierte en una tensión continua y $p$ se queda en $\hat u^2/R$. El factor $\frac12$ desaparece, porque entonces ya no se puede promediar sobre periodos enteros.

:::zusatz Valor eficaz
Una tensión continua $U$ produce en $R$ el mismo calor si $U^2/R=\frac12\hat u^2/R$, es decir, $U=\hat u/\sqrt2$. Este valor se llama __valor eficaz__. Aquí son 7,07 V. Los 230 V del enchufe son un valor eficaz; la amplitud es de 325 V.
:::

:::ltspice Medir la potencia media
⁠**Esquema:** `voltage` de `a` a masa con `SINE(0 10 50)`, `res` `R1` con 5 de `a` a masa.

⁠**Directivas:** `.tran 0 40m 0 10u` y `.meas tran Pm AVG V(a)*I(R1) FROM=0 TO=40m`

⁠**Lo que ves:** Representa `V(a)*I(R1)`: la curva se mantiene entre 0 y 20 W y oscila a 100 Hz. El log indica `Pm` = 10 W. Para el ejercicio [3](#aufg-3), introduce la amplitud 325 y tu resistencia, y lee 2 kW y 4 kW.
:::

:::frage Con corriente alterna, los electrones solo oscilan de un lado a otro. ¿Cómo puede eso aportar energía?
Porque la energía no viaja con los electrones. Incluso con 1 A/mm$^2$ y 50 Hz, solo recorren unos 0,5 µ m por semiperiodo. El campo en la resistencia los acelera en ambos sentidos, y cada choque cede energía a la red cristalina. Para eso no hace falta avanzar, solo tensión y corriente.
:::

:::aufgabe Ejercicio 3 ★★ El calefactor
<span class="anker" id="aufg-3"></span>

Un calefactor absorbe en promedio 2 kW de una tensión sinusoidal con $\hat u=325$ V y 50 Hz. (a) ¿Cuánto valen $R$, $\hat\imath$ y el valor de pico de la potencia? (b) ¿Cuántas veces por segundo es $p=0$? (c) Un componente bloquea una de cada dos semiondas. Predice la potencia media si $R$ no cambia.

:::loesung
(a) De [(3.1)](#gl-3-1): $R=\hat u^2/(2P)=26{,}4\,\Omega$, $\hat\imath=\hat u/R=12{,}3$ A, valor de pico $\hat u\,\hat\imath=2P=4$ kW. (b) Dos veces por periodo, es decir, 100 veces por segundo. (c) Falta una de cada dos semiondas, es decir, la mitad de la energía: 1 kW.
:::
:::

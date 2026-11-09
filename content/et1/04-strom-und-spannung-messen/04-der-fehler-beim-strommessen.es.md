---
title: Etapa 3: El error al medir corriente
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / Medir corriente y tensión
order: 1140400
summary: El amperímetro tiene que entrar en el circuito.
tags: error relativo
lang: es
---

<span class="anker" id="stufe-3"></span>

:::zweck
El amperímetro tiene que entrar en el circuito. Esta etapa calcula cuánto reduce exactamente su resistencia interna la corriente que debe medir.
:::

**La idea.** Para medir se abre el circuito y se inserta el instrumento (fig. [4](#abb-4)). La malla contiene ahora $R$ y $R_\mathrm i$. La fuente mantiene $U$ fija y hace pasar menos corriente por la resistencia total mayor. La lectura es correcta: muestra la corriente que circula ahora. Lo único falso es concluir que la misma corriente circula también sin el instrumento.

:::abbildung et1/k4strom 4
El modelo de referencia sin y con amperímetro. En la resistencia interna caen 49,7 mV, que le faltan a la resistencia. La corriente baja un 0,55 %.
:::

:::satz Teorema 3.1 (Error del amperímetro)
<span class="anker" id="satz-3-1"></span>

Sin instrumento circula $I_R$; con instrumento, $I_R'$:

<span class="anker" id="gl-3-1"></span>
$$I_R=\frac UR,\qquad I_R'=\frac{U}{R+R_\mathrm i}<I_R,\qquad \frac{I_R}{I_R'}=\frac{R+R_\mathrm i}{R}=1+\frac{R_\mathrm i}{R}. \tag{3.1}$$

El __error relativo__ es $f=(I_R'-I_R)/I_R=-R_\mathrm i/(R+R_\mathrm i)$. Para $R_\mathrm i\ll R$ se cumple $f\approx-R_\mathrm i/R$.
:::

⁠**Cómo leerlo:** $U$ es la tensión de la fuente en V, $R$ la resistencia del circuito, $R_\mathrm i$ la del instrumento. La corriente con prima es la corriente con instrumento. En general, $f=(\text{lectura}-\text{valor verdadero})/\text{valor verdadero}$; un $f$ negativo significa que la lectura es demasiado pequeña. **Validez:** El circuito es una fuente ideal con una resistencia. Para un error pequeño hace falta $R_\mathrm i\ll R$; lo ideal es $R_\mathrm i=0$.

:::herleitung Error del amperímetro
La regla de las mallas dice $U=I_R'R+I_R'R_\mathrm i$, es decir, $I_R'=U/(R+R_\mathrm i)$. Con ello, $f=I_R'/I_R-1=R/(R+R_\mathrm i)-1=-R_\mathrm i/(R+R_\mathrm i)$.
:::

::::beispiel
$I_R=5$ mA, $I_R'=9\,\mathrm{V}/1810\,\Omega=4{,}972$ mA, es decir, $f=-0{,}55\,\%$. Con 1 $\Omega$, como en el multímetro digital, serían 4,997 mA y $f=-0{,}056\,\%$: error despreciable. Con una resistencia pequeña la cosa cambia: 0,9 V en 90 $\Omega$ dan 10 mA; con el instrumento, solo 9 mA, es decir, $f=-10\,\%$. No decide el instrumento por sí solo, sino la relación $R_\mathrm i/R$.
::::

⁠**Casos límite:** $R_\mathrm i\to0$ da $f\to0$. $R\to0$ da $I_R'\to U/R_\mathrm i$ y $f\to-100\,\%$: ya solo el instrumento limita la corriente. Eso es el ejercicio [1](das-messgerat-ist-ein-bauteil.html#aufg-1)(a).

:::frage ¿La corriente detrás del amperímetro es menor que delante?
No. En el instrumento no se pierde carga, solo energía. La corriente es la misma en todo el circuito y baja en todas partes a la vez, porque la resistencia total ha aumentado.
:::

:::aufgabe Ejercicio 3 ★★ ¿Qué rango?
<span class="anker" id="aufg-3"></span>

(a) ¿A partir de qué $R$ se mantiene el error del amperímetro de 10 $\Omega$ por debajo del 1 %? (b) A 9 V se conectan 90 k$\Omega$. Compara el rango de 10 mA con el de 250 µ A: el error debido a $R_\mathrm i$ y el error de lectura (1 % del valor de fondo de escala). ¿Qué rango mide mejor?

:::loesung
(a) $R_\mathrm i/(R+R_\mathrm i)\le0{,}01$ da $R\ge99\,R_\mathrm i=990\,\Omega$.

(b) La corriente verdadera es $9\,\mathrm{V}/90\,\mathrm{k\Omega}=100$ µ A. En el rango de 10 mA, $R_\mathrm i=10\,\Omega$, $f=-0{,}011\,\%$, pero el error de lectura es de $\pm100$ µ A, tanto como la propia corriente. En el rango de 250 µ A, $R_\mathrm i=100\,\mathrm{mV}/250\,\mu\text{A}=400\,\Omega$, $f=-0{,}44\,\%$, y el error de lectura es de $\pm2{,}5$ µ A, es decir, un 2,5 %. El rango pequeño interfiere más, pero mide mucho mejor. Además, el $-0{,}44\,\%$ se puede eliminar por cálculo.
:::
:::

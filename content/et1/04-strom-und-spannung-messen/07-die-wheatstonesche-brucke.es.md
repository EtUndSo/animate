---
title: Etapa 6: El puente de Wheatstone
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / Medir corriente y tensión
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-und-spannung-messen
knoten: Capítulo 4: Medir corriente y tensión
order: 1140700
summary: R=U/I suma los errores de dos lecturas.
tags: 
lang: es
---

<span class="anker" id="stufe-6"></span>

:::zweck
$R=U/I$ suma los errores de dos lecturas. En el modelo de referencia son $\pm1{,}1\,\%$ en la tensión y $\pm2\,\%$ en la corriente, en total hasta $\pm3{,}1\,\%$. El puente solo necesita de su instrumento una información: cero o no cero.
:::

**La idea.** Dos divisores de tensión están conectados a la misma fuente (fig. [8](#abb-8)). Un instrumento sensible une sus puntos medios. Si ambos dividen en la misma relación, los puntos medios están al mismo potencial, entre ellos no hay tensión y por el instrumento no circula corriente. Se ajusta una resistencia hasta que la aguja marca cero: el equilibrio. Si no circula corriente, el instrumento no toma nada del circuito. Su resistencia interna no influye y su escala no hace falta.

:::abbildung et1/k4bruecke 8
A la izquierda, el principio. A la derecha, la realización práctica: $R_1$ y $R_2$ son las partes de un hilo resistivo, y el contacto deslizante fija su relación.
:::

:::satz Teorema 6.1 (Condición de equilibrio)
<span class="anker" id="satz-6-1"></span>

Si no circula corriente por el instrumento, se cumple

<span class="anker" id="gl-6-1"></span>
$$R_4=R_3\,\frac{R_2}{R_1}. \tag{6.1}$$
:::

⁠**Cómo leerlo:** $R_3$ es una resistencia de referencia conocida con exactitud. De $R_1$ y $R_2$ solo cuenta la relación, ajustable y conocida; sus valores son indiferentes. $R_4$ es la incógnita. En la ecuación no aparecen ni $U_\mathrm q$ ni la resistencia interna del instrumento. Si la fuente fluctúa, ambos puntos medios se desplazan por igual. **Validez:** exacta en el equilibrio. La exactitud con que se alcanza depende de qué pequeña desviación pueda mostrar aún el instrumento.

:::herleitung Equilibrio
Sin corriente transversal, la regla de los nudos da $I_1=I_2$ e $I_3=I_4$. Los potenciales iguales de los puntos medios dan $U_{R2}=U_{R4}$ y $U_{R1}=U_{R3}$. Así pues,

$$\frac{U_{R4}}{U_{R3}}=\frac{U_{R2}}{U_{R1}} \quad\Rightarrow\quad \frac{I_4R_4}{I_3R_3}=\frac{I_2R_2}{I_1R_1} \quad\Rightarrow\quad \frac{R_4}{R_3}=\frac{R_2}{R_1}.$$
:::

::::beispiel
Con $R_2/R_1=1{,}8$ y $R_3=1$ k$\Omega$, la aguja marca cero con $R_4=1800\,\Omega$, y ambos puntos medios están a 5,786 V. Si $R_3$ y la relación son exactas al 0,1 % cada una, $R_4$ es exacta a $\pm0{,}2\,\%$, más de 15 veces mejor que $U/I$. La exactitud procede ahora de resistencias, y estas se fabrican con mucha más exactitud que las escalas de aguja.
::::

⁠**Caso límite:** Al crecer $R_4$, el punto medio derecho recorre de 0 a $U_\mathrm q$. La tensión en el instrumento cambia de signo exactamente una vez, así que hay exactamente una posición de equilibrio.

:::frage En el puente sí circula corriente. ¿Qué es exactamente cero?
Solo la corriente en la rama transversal. En el ejemplo circulan 3,214 mA por cada divisor; la fuente funciona con normalidad.
:::

**Hilo deslizante y décadas.** En el hilo deslizante (hilo resistivo uniforme con un contacto móvil, longitud $l$, resistencia total $R_0$), en la posición de contacto $x$ la parte inferior es $R_2=R_0\,x/l$ y la superior $R_1=R_0\,(1-x/l)$. De ahí se deduce $R_4=R_3\,x/(l-x)$, y $R_0$ desaparece. Para 1800 $\Omega$ con $l=1$ m, el contacto está en $x=642{,}9$ mm. Los puentes más exactos ajustan $R_3$ por décadas: conmutadores con $9\times100\,\Omega$, $9\times10\,\Omega$, $9\times1\,\Omega$ y $9\times0{,}1\,\Omega$ dan una cifra cada uno, y $R_2/R_1$ es un multiplicador conmutable en potencias de diez. Con el factor 10 y la posición 180,0 $\Omega$ resultan 1800 $\Omega$ en pasos de 1 $\Omega$. Como indicador de cero también sirve un voltímetro, porque en el equilibrio las tensiones en $R_2$ y $R_4$ son iguales.

:::ltspice El equilibrio no depende del instrumento
⁠**Esquema:** fuente `voltage` con 9 V en el nudo `o`. `R1` = 1k de `o` a `l`, `R2` = 1.8k de `l` a masa, `R3` = 1k de `o` a `r`, `R4` = `{RX}` de `r` a masa. El mecanismo de medida es `Rd` = 2k de `l` a `r`.

⁠**Directivas:** `.step param RX 1700 1900 10` y `.op`

⁠**Lo que ves:** Dibuja `I(Rd)` en función de `RX`: la curva pasa por cero en 1800; en 1700 son $+36{,}4$ µ A, en 1900 $-33{,}6$ µ A. Pon `Rd` a 1 o 1Meg: la curva cambia de altura, y el paso por cero sigue en 1800. Con una desviación del 0,1 % (1801,8 $\Omega$), por el mecanismo de medida solo circulan 0,63 µ A, es decir, el 1,3 % del fondo de escala. Para el ejercicio [7](#aufg-7): con `R1` = 356.1 y `R2` = 643.9 (contacto desplazado 1 mm), el paso por cero se traslada a 1808 $\Omega$.
:::

:::aufgabe Ejercicio 7 ★★ Hilo deslizante
<span class="anker" id="aufg-7"></span>

El hilo mide 1 m, $R_3=1$ k$\Omega$. (a) El equilibrio se alcanza en $x=642{,}9$ mm. ¿Cuánto vale $R_4$? (b) El contacto puede leerse con $\pm1$ mm. ¿Qué error de $R_4$ resulta? (c) Repite (b) para $R_3=1{,}8$ k$\Omega$ y $R_3=100\,\Omega$. ¿Por qué se elige $R_3$ del orden de $R_4$?

:::loesung
(a) $R_4=1\,\mathrm{k\Omega}\cdot642{,}9/357{,}1=1800\,\Omega$. (b) Un desplazamiento $\Delta x$ cambia $x/(l-x)$ en términos relativos en $\Delta x\,(1/x+1/(l-x))$. Eso son $1\,\mathrm{mm}\cdot(1/642{,}9+1/357{,}1)/\mathrm{mm}=\pm0{,}44\,\%$.

(c) $R_3=1{,}8$ k$\Omega$: $x=500$ mm, $\pm0{,}40\,\%$. $R_3=100\,\Omega$: $x=947{,}4$ mm, $\pm2{,}0\,\%$. El error es mínimo cuando el contacto está en el centro, es decir, con $R_3\approx R_4$. Cerca del extremo del hilo, el mismo milímetro pesa mucho en términos relativos.
:::
:::

---
title: Etapa 10: El convertidor R-2R
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / Fuentes y fuentes equivalentes
order: 1151200
summary: Un procesador solo conoce bits; un altavoz necesita una tensión.
tags: convertidor digital-analógico
lang: es
---

<span class="anker" id="stufe-10"></span>

:::zweck
Un procesador solo conoce bits; un altavoz necesita una tensión. El convertidor R-2R traduce entre ambos. Es superposición y fuente equivalente en un único circuito.
:::

**La idea.** Un __convertidor digital-analógico__ convierte un número binario con los bits $d_2d_1d_0$ en una tensión. En la fig. [12](#abb-12), cada interruptor conecta su resistencia 2$R$ a $U_\mathrm{ref}$ (bit 1) o a 0 V (bit 0). Un interruptor en 0 V es una fuente de tensión desactivada. Por tanto, la superposición ya está en la propia construcción: cada bit activo es una fuente, y todos los demás son cables. La escalera de $R$ y $2R$ está dimensionada de modo que cada peldaño divida el efecto por dos.

:::abbildung et1/k5r2r 12
Convertidor R-2R de tres bits en la posición 101. Cada conmutador conecta su resistencia a $U_\mathrm{ref}$ o a masa. La salida se toma arriba a la derecha.
:::

:::satz Teorema 10.1 (Escalera R-2R)
<span class="anker" id="satz-10-1"></span>

Para el convertidor de la fig. [12](#abb-12) con la salida abierta se cumple

<span class="anker" id="gl-10-1"></span>
$$U_\mathrm{sal}=U_\mathrm{ref}\left(\frac{d_2}{2}+\frac{d_1}{4}+\frac{d_0}{8}\right),\qquad R_\mathrm{i}=R. \tag{10.1}$$
:::

⁠**Cómo leerlo:** $d_k$ es 0 o 1, $U_\mathrm{ref}$ la tensión de referencia fija (unos voltios), $R$ normalmente unos k$\Omega$. El bit más significativo aporta la mitad de la tensión de referencia, y cada uno de los siguientes la mitad del anterior. $R_\mathrm{i}$ no depende de la posición de los interruptores: al desactivar, $U_\mathrm{ref}$ pasa a 0 V, y entonces toda rama lleva a masa, sea cual sea la posición de su interruptor. **Validez:** interruptores ideales sin resistencia propia, salida sin carga.

:::herleitung Fuente equivalente de izquierda a derecha
En el nudo izquierdo hay 2$R$ contra masa y 2$R$ contra $U_0=d_0U_\mathrm{ref}$. Esto es una fuente equivalente con $\frac12U_0$ y $2R\parallel2R=R$. Con la resistencia longitudinal se convierte en $\frac12U_0$ y $2R$. En el nudo siguiente esto se encuentra con 2$R$ contra $U_1=d_1U_\mathrm{ref}$: de nuevo dos ramas iguales, es decir, el promedio de [(7.2)](quellen-zusammenschalten.html#gl-7-2), la fuente equivalente $\frac12\bigl(\frac12U_0+U_1\bigr)$ y otra vez $R$. El último nudo lo repite:

$$U_\mathrm{sal}=\tfrac12\Bigl(\tfrac12\bigl(\tfrac12U_0+U_1\bigr)+U_2\Bigr)=\tfrac12U_2+\tfrac14U_1+\tfrac18U_0.$$

La superposición da el mismo número. Ejemplo, la fuente $U_1$: en el nudo central ve 2$R$ a la izquierda y $R+2R=3R$ a la derecha, en conjunto $\frac65R$. El divisor da allí $\frac{6/5}{6/5+2}=\frac38U_1$. El camino hasta la salida divide otra vez por $\frac{2R}{R+2R}=\frac23$, es decir, $\frac38\cdot\frac23=\frac14$.
:::

::::beispiel
Con $U_\mathrm{ref}=8$ V y $R=1$ k$\Omega$, los bits pesan 4 V, 2 V y 1 V. La posición 101 da 5 V. Una carga con $R_\mathrm{L}=R$ forma un divisor con $R_\mathrm{i}$ y reduce esto a la mitad, 2,5 V. Por eso, en los convertidores reales sigue un amplificador operacional ([Parte 11](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-operationsverstarker/der-operationsverstaerker.html)) con una resistencia de entrada muy alta: prácticamente no consume corriente, y la escalera queda en circuito abierto.
::::

⁠**Casos límite:** La posición 000 da 0 V, la posición 111 da 7 V, un escalón por debajo de $U_\mathrm{ref}$.

:::ltspice El convertidor cuenta
⁠**Esquema:** fig. [12](#abb-12) sin interruptores: 2$R$ del nudo `n0` a masa, luego 2$R$ de cada uno de `n0`, `n1`, `n2` a una fuente `voltage` contra masa y $R$ entre los nudos, $R=1$ k$\Omega$. Las fuentes cuentan en binario: `PULSE(0 8 1m 1u 1u 1m 2m)`, `PULSE(0 8 2m 1u 1u 2m 4m)`, `PULSE(0 8 4m 1u 1u 4m 8m)`.

⁠**Directiva:** `.tran 8m`

⁠**Lo que ves:** `V(n2)` es una escalera con escalones de 1 V, de 0 V a 7 V. Con una carga de 1 k$\Omega$ en `n2` solo sube hasta 3,5 V. Con 3 k$\Omega$ aparece en el escalón superior tu resultado del ejercicio [12](#aufg-12)(c).
:::

:::frage ¿Para qué sirve la resistencia 2$R$ suelta del extremo izquierdo?
Hace uniforme la escalera. Con ella, todo lo que hay a la izquierda de cada nudo es una fuente equivalente con $2R$, igual que la rama del propio interruptor. Solo así surgen dos ramas iguales y una media pura. Sin ella, la rama izquierda valdría $3R$, y los pesos ya no serían binarios.
:::

:::aufgabe Ejercicio 12 ★★ Cuatro bits
<span class="anker" id="aufg-12"></span>

(a) Un convertidor de cuatro bits funciona con $U_\mathrm{ref}=16$ V. ¿Cuánto valen el escalón, el valor máximo y la tensión para 1011? (b) ¿Cuánto vale un escalón con ocho bits a 5 V? (c) El convertidor de tres bits del ejemplo está en 111 y alimenta $R_\mathrm{L}=3R$. ¿Qué tensión se establece?

:::loesung
(a) Escalón $16\,\mathrm{V}/2^4=1$ V. Valor máximo $15$ V. 1011: $8+0+2+1=11$ V. La fórmula continúa con $d_3/2+d_2/4+d_1/8+d_0/16$.

(b) $5\,\mathrm{V}/256=19{,}5$ mV.

(c) Circuito abierto 7 V, resistencia interna $R$. Divisor: $7\,\mathrm{V}\cdot\frac{3R}{R+3R}=5{,}25$ V.
:::
:::

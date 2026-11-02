---
title: Etapa 7: Conexión en paralelo y en serie
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / El condensador
order: 1130800
summary: Varios condensadores pueden tratarse como uno solo.
tags: isla
lang: es
---

<span class="anker" id="stufe-7"></span>

:::zweck
Varios condensadores pueden tratarse como uno solo. La única pregunta es qué magnitud iguala el circuito para todos.
:::

**La idea.** ⁠**En paralelo:** Todas las placas superiores cuelgan de un cable; todas las inferiores, de otro. Un cable sin corriente tiene en todas partes el mismo potencial, por lo que todos los condensadores tienen la misma tensión. El circuito actúa como una placa ampliada, y las cargas se suman. **En serie:** La placa inferior de $C_1$ y la superior de $C_2$ forman con su cable de unión una __isla__: un trozo de conductor al que solo llegan aislantes (fig. [7](#abb-7)). La carga no puede entrar ni salir de ella. Si la isla estaba sin carga, su suma sigue siendo cero: si la placa superior con $+Q$ atrae $-Q$ en la isla, la contrapartida que falta debe ir como $+Q$ a la placa siguiente. Por tanto, todos llevan la misma carga, y las tensiones se suman. El circuito actúa como una separación ampliada.

:::abbildung et1/k3schaltungen 7
$C_1=100\,\mu\text{F}$ y $C_2=50\,\mu\text{F}$ a 9 V. En paralelo: la misma tensión; las cargas se suman hasta 1350 µC. En serie: la misma carga de 300 µC, porque la isla de contorno discontinuo sigue siendo neutra. El condensador más pequeño recibe la mayor tensión.
:::

:::satz Teorema 7.1 (Capacidad total)
<span class="anker" id="satz-7-1"></span>

Para $n$ condensadores conectados en paralelo (izquierda) y $n$ condensadores conectados en serie e inicialmente sin carga (derecha) se cumple

<span class="anker" id="gl-7-1"></span>
$$C_\mathrm{G}=\sum_{i=1}^nC_i,\qquad\qquad\frac{1}{C_\mathrm{G}}=\sum_{i=1}^n\frac{1}{C_i}. \tag{7.1}$$

Para dos condensadores en serie, $C_\mathrm{G}=\dfrac{C_1C_2}{C_1+C_2}$, y la tensión se reparte según $U_1=U_\mathrm{G}\,\dfrac{C_2}{C_1+C_2}$.
:::

:::herleitung Capacidad total
⁠**En paralelo.** Restricción del circuito: $U_i=U_\mathrm{G}$ para todo $i$. Carga individual: $Q_i=C_iU_i=C_iU_\mathrm{G}$. Carga total: $Q_\mathrm{G}=\sum Q_i=U_\mathrm{G}\sum C_i$. Con $C_\mathrm{G}=Q_\mathrm{G}/U_\mathrm{G}$ resulta la fórmula de la izquierda.

⁠**En serie.** Restricción del circuito: $Q_i=Q_\mathrm{G}$ para todo $i$. Tensión total: $U_\mathrm{G}=\sum U_i$. Tensión parcial: $U_i=Q_i/C_i=Q_\mathrm{G}/C_i$. Por tanto, $U_\mathrm{G}=Q_\mathrm{G}\sum 1/C_i$, y con $U_\mathrm{G}=Q_\mathrm{G}/C_\mathrm{G}$ resulta la fórmula de la derecha. Para el divisor: $U_1=Q_\mathrm{G}/C_1=U_\mathrm{G}\,C_\mathrm{G}/C_1=U_\mathrm{G}\,C_2/(C_1+C_2)$.
:::

⁠**Cómo leerlo:** $C_\mathrm{G}$ es la capacidad de un único condensador que muestra el mismo comportamiento en los dos terminales exteriores. En paralelo, $C_\mathrm{G}$ es mayor que cada valor individual; en serie, menor que el más pequeño. **Validez:** La fórmula de la derecha necesita islas sin carga al inicio. Si no, la carga anterior de la isla se conserva, y $Q_i=Q_\mathrm{G}$ solo vale para la carga que se añade.

**Ejemplo.** En paralelo: $C_\mathrm{G}=150\,\mu\text{F}$, $Q_1=900\,\mu\text{C}$, $Q_2=450\,\mu\text{C}$. En serie: $1/C_\mathrm{G}=1/(100\,\mu\text{F})+1/(50\,\mu\text{F})$, es decir, $C_\mathrm{G}=33{,}3\,\mu\text{F}$. A 9 V es $Q=300\,\mu\text{C}$, $U_1=3$ V y $U_2=6$ V.

⁠**Casos límite:** Para $C_2\to\infty$, en serie $C_\mathrm{G}\to C_1$: un condensador enorme se comporta como un cable. Para $C_2\to0$, en serie $C_\mathrm{G}\to0$: el hueco interrumpe; en paralelo queda $C_1$.

:::frage ¿Por qué las fórmulas son justo las inversas de las de las resistencias?
En las resistencias, $u=R\,i$: en serie, las tensiones se suman con la misma corriente, así que se suma $R$. En el condensador, $u=\frac1C\,q$: en serie, las tensiones se suman con la misma carga, así que se suma $1/C$. **En resumen:** En el condensador, $1/C$ hace el papel de $R$.
:::

:::aufgabe Ejercicio 8 ★★ Una red mixta
<span class="anker" id="aufg-8"></span>

<ol class="al">

<li>

Dos condensadores de 10 µF y 20 µF están en paralelo, y en serie con ellos hay uno de 60 µF, todo a 9 V. Calcula $C_\mathrm{G}$, la carga total, todas las tensiones y todas las cargas individuales.

</li>

<li>

Dos condensadores iguales de 100 µF y 16 V de tensión máxima están en serie. ¿Qué capacidad y qué tensión máxima tiene la cadena?

</li>

</ol>

:::loesung
(a) En paralelo: $10+20=30\,\mu\text{F}$. En serie con 60 µF: $C_\mathrm{G}=\frac{30\cdot60}{30+60}\,\mu\text{F}=20\,\mu\text{F}$. $Q=20\,\mu\text{F}\cdot9\,\mathrm{V}=180\,\mu\text{C}$. En el condensador de 60 µF: $180\,\mu\text{C}/60\,\mu\text{F}=3$ V. En el bloque en paralelo: $180\,\mu\text{C}/30\,\mu\text{F}=6$ V, en total 9 V. La carga se reparte: $10\,\mu\text{F}\cdot6\,\mathrm{V}=60\,\mu\text{C}$ y $20\,\mu\text{F}\cdot6\,\mathrm{V}=120\,\mu\text{C}$.

(b) $C_\mathrm{G}=50\,\mu\text{F}$. Con condensadores iguales, la tensión se reparte por igual: 16 V cada uno y 32 V en total.
:::
:::

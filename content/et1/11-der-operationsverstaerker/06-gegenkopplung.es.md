---
title: Etapa 4: Realimentación negativa
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / El amplificador operacional
order: 1210600
summary: Sin realimentación, el AO es un interruptor.
tags: realimentación, realimentación positiva, amplificador no inversor, seguidor de tensión
lang: es
---

<span class="anker" id="stufe-4"></span>

:::zweck
Sin realimentación, el AO es un interruptor. Esta etapa muestra por qué una parte realimentada de la salida lleva la diferencia de las entradas casi a cero y por qué la ganancia deja entonces de depender de $A$.
:::

**La idea.** La __realimentación__ significa que una parte de la magnitud de salida vuelve a la entrada. Si actúa contra la causa, es realimentación negativa; si la refuerza, __realimentación positiva__. En el AO, el camino hacia la entrada negativa da realimentación negativa, porque allí toda tensión actúa con signo negativo.

En el __amplificador no inversor__, $U_\mathrm{E}$ está en la entrada positiva (fig. [6](#abb-6)). El divisor formado por $R_2$ y $R_1$ comunica una quinta parte de la salida a la entrada negativa. Aplica ahora $U_\mathrm{E}=1$ V. Al principio, $U_\mathrm{A}=0$, así que $\varphi_-=0$ y $U_\mathrm{D}=1$ V. El valor objetivo $A\,U_\mathrm{D}$ serían 100 kV, y la salida sube. Con 4 V en la salida, $\varphi_-=0{,}8$ V y faltan aún 200 mV. Con 4,9 V faltan 20 mV; con 4,99 V, solo 2 mV, y el objetivo se ha reducido a 200 V. La salida alcanza su objetivo solo cuando ambos son iguales: $A\,U_\mathrm{D}=U_\mathrm{A}$. Eso ocurre con $U_\mathrm{A}\approx5$ V y $U_\mathrm{D}=5\,\mathrm{V}/100000=50$ µ V. También una bajada se corregiría al instante: si la salida cae, baja $\varphi_-$, crece $U_\mathrm{D}$ y la salida sube.

La pequeña diferencia no es, por tanto, una ley básica del componente, sino el resultado del lazo. No puede ser cero, porque sin diferencia no habría salida.

:::satz Teorema 4.1 (Amplificador con realimentación negativa)
<span class="anker" id="satz-4-1"></span>

Si la fracción $\beta$ de la salida se lleva a la entrada negativa y $U_\mathrm{E}$ está en la entrada positiva, en el rango lineal se cumple

<span class="anker" id="gl-4-1"></span>
$$U_\mathrm{D}=\frac{U_\mathrm{E}}{1+A\beta},\qquad G=\frac{U_\mathrm{A}}{U_\mathrm{E}}=\frac{A}{1+A\beta}=\frac1\beta\cdot\frac{1}{1+\dfrac1{A\beta}}. \tag{4.1}$$

Para $A\beta\gg1$ es $G\approx1/\beta$ con la desviación relativa $-1/(A\beta)$. Un cambio de $A$ actúa debilitado por el factor $1+A\beta$:

<span class="anker" id="gl-4-2"></span>
$$\frac{\Delta G}{G}\approx\frac{1}{1+A\beta}\cdot\frac{\Delta A}{A}. \tag{4.2}$$

Con el divisor, $\beta=R_1/(R_1+R_2)$, es decir, $G\approx1+R_2/R_1$.
:::

⁠**Cómo leerlo:** $\beta$ es la fracción realimentada, entre 0 y 1, aquí 0,2. $G$ es la ganancia de todo el circuito. $A\beta$ es la ganancia de lazo: un pequeño cambio en $U_\mathrm{D}$ se amplifica por $A$ y se comunica de vuelta debilitado por $\beta$. Aquí $A\beta=20000$; esta es la reserva que mantiene pequeña la desviación. **Validez:** $U_\mathrm{A,min}<U_\mathrm{A}<U_\mathrm{A,max}$, corriente de entrada pequeña frente a la corriente del divisor, $A$ a la frecuencia considerada (etapa [10](wo-die-regeln-enden.html#stufe-10)).

:::herleitung El lazo en equilibrio y en movimiento
Equilibrio: $U_\mathrm{A}=A\,U_\mathrm{D}$ y $U_\mathrm{D}=U_\mathrm{E}-\beta\,U_\mathrm{A}$. Sustituyendo resulta $U_\mathrm{D}=U_\mathrm{E}-A\beta\,U_\mathrm{D}$, y de ahí [(4.1)](#gl-4-1). Derivar $G$ respecto a $A$ da $\mathrm{d} G/\mathrm{d} A=1/(1+A\beta)^2$; dividiendo entre $G$ se obtiene [(4.2)](#gl-4-2).

Movimiento: dentro del AO, una corriente proporcional a $U_\mathrm{D}$ carga una capacidad. Por eso la salida no puede saltar, sino que corre tras su valor objetivo: $\tau\,\mathrm{d} U_\mathrm{A}/\mathrm{d} t=A\,U_\mathrm{D}-U_\mathrm{A}$, aquí con $\tau=A/(2\pi f_\mathrm{T})=15{,}9$ ms. Es la ecuación del circuito RC de la [Parte 3](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator/der-kondensator.html). Con $U_\mathrm{D}=U_\mathrm{E}-\beta\,U_\mathrm{A}$ resulta

$$\tau\,\frac{\mathrm{d} U_\mathrm{A}}{\mathrm{d} t}=A\,U_\mathrm{E}-(1+A\beta)\,U_\mathrm{A}.$$

El factor delante de $U_\mathrm{A}$ es negativo, así que toda desviación se extingue: $U_\mathrm{A}(t)=G\,U_\mathrm{E}\,(1-\mathrm{e}^{-t/\tau_G})$ con $\tau_G=\tau/(1+A\beta)=0{,}80$ µ s. El lazo es 20001 veces más rápido que el AO solo.
:::

:::abbildung et1/k11schleife 5
A la izquierda, el lazo como diagrama de bloques: en el punto de suma se resta $\beta\,U_\mathrm{A}$. A la derecha, la respuesta a un escalón de 0 a 1 V en el modelo lineal: $U_\mathrm{A}$ sube con $\tau_G=0{,}80$ µ s hasta 5 V, y $U_\mathrm{D}$ cae de 1 V a 50 µ V.
:::

**Ejemplo.** Con $A\beta=20000$, 1 V de entrada se convierte en $U_\mathrm{A}=4{,}99975$ V; la desviación respecto al ideal de 5 V es 0,005 % $=1/(A\beta)$. Los ejemplares se dispersan en un factor de cuatro:

| $A$ | $U_\mathrm{D}$ | $U_\mathrm{A}$ | Desviación respecto a 5 V |
|---|---|---|---|
| 50000 | 99,99 µ V | 4,99950 V | $-0{,}0100$ % |
| 100000 | 50,00 µ V | 4,99975 V | $-0{,}0050$ % |
| 200000 | 25,00 µ V | 4,99988 V | $-0{,}0025$ % |

Un cambio de $A$ del 300 % desplaza $G$ un 0,0075 %. Se cambia ganancia por precisión: 100000 se convierten en 5, pero a cambio dos resistencias determinan el resultado. **En resumen:** La ganancia es el inverso de la fracción realimentada. **Casos límite:** $A\to\infty$ da $U_\mathrm{D}\to0$ y $G=1/\beta$. $\beta\to0$ da $G\to A$; sin realimentación queda el lazo abierto.

**Entrada y salida.** En la entrada positiva solo hay $U_\mathrm{D}=50$ µ V sobre $r_\mathrm{e}$; circulan 50 pA, una dosmillonésima de la corriente del divisor de 100 µ A. Así, la resistencia de entrada sube a $r_\mathrm{e}(1+A\beta)=20$ G$\Omega$. En la salida, el lazo actúa contra cualquier carga: si una carga baja un poco $U_\mathrm{A}$, crece $U_\mathrm{D}$, y la tensión interna sube hasta compensar casi por completo la pérdida. La resistencia de salida baja a $r_\mathrm{a}/(1+A\beta)=3{,}75$ m$\Omega$.

**El seguidor de tensión.** Con $R_2=0$ y $R_1\to\infty$, la salida está unida directamente a la entrada negativa, $\beta=1$, $G=A/(1+A)=0{,}99999$. Este __seguidor de tensión__ no amplifica, sino que separa: resistencia de entrada 100 G$\Omega$, resistencia de salida 0,75 m$\Omega$. Un voltímetro de 1 M$\Omega$ en una fuente de 1 V y 100 k$\Omega$ de resistencia interna indica 0,909 V ([Parte 4](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-und-spannung-messen/strom-und-spannung-messen.html)). Con un seguidor de tensión delante indica 0,99999 V.

:::abbildung et1/k11nichtinv 6
A la izquierda, el amplificador no inversor con los potenciales del modelo de referencia. La entrada negativa está solo 50 µ V por debajo de la entrada positiva. A la derecha, el seguidor de tensión como caso límite $\beta=1$.
:::

:::frage ¿Por qué no usar directamente un amplificador con $G=5$, en lugar de comprar 100000 y desechar casi todo?
Porque ese 5 dependería de $B$, $U_\mathrm{Early}$ y la temperatura: un cambio del 1 % en el interior sería un 1 % en el resultado. Con la reserva $A\beta=20000$ se convierte en $5\cdot10^{-5}$ %.
:::

:::frage Ahora la salida está demasiado baja, así que salta hacia arriba, y entonces está demasiado alta. ¿No debería oscilar eternamente?
Lo haría si saltara de un paso a $A\,U_\mathrm{D}$: el error se multiplicaría por 20000 en cada vuelta. Pero la salida no salta. La capacidad interna limita su velocidad; avanza de forma continua y frena cuando $U_\mathrm{D}$ se reduce. Así llega sin sobreoscilación (deducción de arriba).
:::

:::ltspice Medir la diferencia
⁠**Esquema:** `voltage` `VE` con 1 del nudo `p` a masa. Una fuente controlada `e` como AO: salida del nudo `a` a masa, entradas de control `p` (más) y `m` (menos), valor `{A}`. `res` `R2` 40k de `a` a `m`, `R1` 10k de `m` a masa.

⁠**Directivas:** `.param A=1e5`, `.step param A list 5e4 1e5 2e5`, `.op`, `.options numdgt=15`, `.meas op ua FIND V(a) AT=1e5`, `.meas op ud FIND V(p,m) AT=1e5`.

⁠**Lo que ves:** `ua` = 4,99975 V, `ud` = 49,9975 µ V, como en el cálculo. Con `AT=5e4` salen 4,99950 V y 99,99 µ V. Para el ejercicio [4](#aufg-4), pon `R2` a 100k. Intercambia después `p` y `m`: `.op` muestra 5,00025 V. Por qué eso no se mantiene en la realidad lo aclara la etapa [9](mitkopplung-und-der-schmitt-trigger.html#stufe-9).
:::

:::aufgabe Ejercicio 4 ★★ Dispersión y reserva
<span class="anker" id="aufg-4"></span>

El amplificador debe tener $G=11$, con $R_1=10$ k$\Omega$. (a) Elige $R_2$. ¿Cuánto valen $\beta$ y $A\beta$? (b) ¿Cuánto vale $U_\mathrm{D}$ con $U_\mathrm{A}=5{,}5$ V? (c) Calcula $G$ para $A=50000$ y $200000$. (d) ¿Qué $A$ mínimo basta para una desviación del 0,1 %? (e) ¿Qué ocurre con $U_\mathrm{E}=2$ V? ¿Cuánto vale entonces $U_\mathrm{D}$?

:::loesung
(a) $1+R_2/R_1=11$, así que $R_2=100$ k$\Omega$. $\beta=1/11=0{,}0909$, $A\beta=9091$. (b) $5{,}5\,\mathrm{V}/100000=55$ µ V. (c) $G=10{,}99758$ y $10{,}99940$, una diferencia del 0,016 %. (d) $1/(1+1/(A\beta))=0{,}999$ da $A\beta=999$, así que $A\ge10989$. (e) Por cálculo, 22 V; la salida está en 11 V. Entonces $\varphi_-=\beta\cdot11\,\mathrm{V}=1$ V y $U_\mathrm{D}=1$ V; la regla no vale.
:::
:::

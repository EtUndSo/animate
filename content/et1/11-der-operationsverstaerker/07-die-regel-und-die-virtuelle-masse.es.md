---
title: Etapa 5: La regla y la masa virtual
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / El amplificador operacional
order: 1210700
summary: La etapa 4 calculó con A .
tags: amplificador inversor
lang: es
---

<span class="anker" id="stufe-5"></span>

:::zweck
La etapa [4](gegenkopplung.html#stufe-4) calculó con $A$. Pero la desviación es diminuta. Esta etapa la convierte en una regla para todos los circuitos con realimentación negativa y la aplica al caso más importante: la entrada en el terminal negativo.
:::

**La idea.** En todo circuito se cumple $|U_\mathrm{D}|\le11\,\mathrm{V}/100000=110$ µ V mientras la salida no llegue a su tope. Frente a tensiones del orden de voltios, eso no es nada. Si se calcula con $U_\mathrm{D}=0$, se comete un error del orden de $1/(A\beta)$. Con ello, $A$ deja de hacer falta.

:::satz Teorema 5.1 (La regla para el AO con realimentación negativa)
<span class="anker" id="satz-5-1"></span>

Mientras $U_\mathrm{A,min}<U_\mathrm{A}<U_\mathrm{A,max}$, se cumple

<ol>

<li>

$\varphi_+=\varphi_-$: La salida se ajusta de modo que la diferencia desaparezca.

</li>

<li>

$I_+=I_-=0$: No entra corriente en las entradas.

</li>

<li>

La salida entrega toda la corriente necesaria. Para el nudo de salida no se plantea ninguna ecuación de nudo.

</li>

</ol>

Se plantea la ley de los nudos en la entrada negativa, se despeja $U_\mathrm{A}$ y al final se comprueban los límites.
:::

En el __amplificador inversor__, la entrada positiva está a masa, $U_\mathrm{E}$ llega a través de $R_1$ a la entrada negativa, y $R_2$ vuelve desde la salida (fig. [7](#abb-7)). De $\varphi_-=\varphi_+=0$ e $I_-=0$ se sigue

<span class="anker" id="gl-5-1"></span>
$$\frac{U_\mathrm{E}}{R_1}+\frac{U_\mathrm{A}}{R_2}=0\quad\Rightarrow\quad U_\mathrm{A}=-\frac{R_2}{R_1}\,U_\mathrm{E},\qquad R_\mathrm{ent}=\frac{U_\mathrm{E}}{I_1}=R_1. \tag{5.1}$$

⁠**Cómo leerlo:** $I_1$ es la corriente por $R_1$. $R_\mathrm{ent}$ es la resistencia que ve la fuente: solo $R_1$, porque su extremo derecho está fijo en 0 V. Con $A$ finito, $G=-(R_2/R_1)\big/\bigl(1+1/(A\beta)\bigr)$ con el mismo $\beta=R_1/(R_1+R_2)$. **Validez:** como la regla, y $A\beta\gg1$.

:::herleitung $A$ finito en el inversor
La superposición en el divisor formado por $R_1$ y $R_2$ da $\varphi_-=(R_2\,U_\mathrm{E}+R_1\,U_\mathrm{A})/(R_1+R_2)$. Con $\varphi_+=0$ es $U_\mathrm{D}=-\varphi_-$, es decir, $U_\mathrm{A}=-A\,\varphi_-$. Despejando: $U_\mathrm{A}(1+A\beta)=-A\,(1-\beta)\,U_\mathrm{E}$ con $1-\beta=R_2/(R_1+R_2)$. Como $A(1-\beta)=A\beta\cdot R_2/R_1$, se obtiene la fórmula. El lazo ve $U_\mathrm{E}$ como un valor fijo; por eso $\beta$ es el mismo divisor que en la etapa [4](gegenkopplung.html#stufe-4).
:::

**El mecanismo de la masa virtual.** Con $U_\mathrm{E}=1$ V, la tensión en $R_1$ impulsa una corriente de 100 µ A hacia la entrada negativa. No puede entrar en el AO. Por tanto, tiene que pasar por $R_2$. Para 100 µ A a través de 40 k$\Omega$, el extremo derecho de $R_2$ debe estar 4 V más abajo, así que la salida va a $-4$ V. La corriente sigue hacia la salida y, por el transistor de salida inferior, hasta $U_\mathrm{B-}$ (línea roja en la fig. [7](#abb-7)). En el nudo queda solo la diminuta tensión $\varphi_-=-U_\mathrm{D}=U_\mathrm{A}/(-A)=+40$ µ V. El nudo se comporta como una masa, pero no lo es:

<ul>

<li>

Una masa real absorbe corriente. La virtual la pasa a $R_2$; entre el nudo y masa no circula nada.

</li>

<li>

Una masa real se queda siempre en 0 V. La virtual mantiene su potencial solo porque la salida reajusta sin cesar. Si la salida está en el tope, la masa virtual desaparece (fig. [7](#abb-7), abajo).

</li>

<li>

Si se une el nudo a masa con un cable, los 100 µ A circulan por él, $R_2$ queda sin corriente y $U_\mathrm{A}=0$.

</li>

</ul>

**Por qué, aun así, no circula corriente de entrada.** Entre las entradas casi no hay tensión, pero tampoco hay conductor. Tienen el mismo potencial, pero no están unidas: 40 µ V sobre $r_\mathrm{e}=1$ M$\Omega$ dan 40 pA, 2,5 millones de veces menos que $I_1$. Ambas cosas actúan juntas: la etapa diferencial tiene una resistencia alta, y el lazo casi no le deja tensión.

:::frage Con 0 V en el nudo y corriente llegando, ¿no debería tener la entrada negativa resistencia cero?
Así la ve la fuente: tras $R_1$ ve un punto que mantiene su potencial, sea cual sea la corriente que llega. Pero eso lo consigue la salida a través de $R_2$. La entrada misma sigue teniendo una resistencia alta de 1 M$\Omega$.
:::

:::abbildung et1/k11invert 7
Arriba, el amplificador inversor; en rojo, el camino de la corriente con $U_\mathrm{E}=+1$ V. Abajo, el límite: $\hat u_\mathrm{E}=3{,}5$ V daría 14 V, y la salida topa en $\pm11$ V. Entonces $\varphi_-$ sube hasta 0,6 V y la masa virtual desaparece.
:::

**Ejemplo.** $U_\mathrm{A}=-4\cdot1\,\mathrm{V}=-4$ V, con $A$ finito más exactamente $-3{,}9998$ V. $R_\mathrm{ent}=10$ k$\Omega$. Con una carga de 2 k$\Omega$ a masa circulan 2 mA, y la salida absorbe 2,1 mA: carga más realimentación. La fuente $U_\mathrm{E}$ no nota nada. **Casos límite:** $R_2=R_1$ solo invierte el signo. $R_2\to0$ da $U_\mathrm{A}=0$.

**El primer límite.** La regla 1 supone que la salida alcanza la tensión exigida. Con $G=-4$ esto termina en $|U_\mathrm{E}|=11\,\mathrm{V}/4=2{,}75$ V. Por encima, $U_\mathrm{A}=\mp11$ V está fijo, el lazo está abierto y el divisor formado por $R_1$ y $R_2$ determina el nudo: $\varphi_-=0{,}8\,U_\mathrm{E}+0{,}2\,U_\mathrm{A}$, es decir, $+0{,}6$ V con 3,5 V.

:::aufgabe Ejercicio 5 ★★ Amplificador inversor
<span class="anker" id="aufg-5"></span>

$R_1=4{,}7$ k$\Omega$, $R_2=47$ k$\Omega$, $U_\mathrm{E}=0{,}5$ V. (a) Determina $U_\mathrm{A}$, $I_1$ y $R_\mathrm{ent}$. (b) ¿Cuánto valen, con $A=100000$, $\varphi_-$ y el $G$ exacto? (c) A la salida está conectada una carga de 1 k$\Omega$. ¿Cuánto vale la corriente de salida y de dónde viene? (d) ¿Hasta qué $U_\mathrm{E}$ llega la salida? ¿Cuánto vale $\varphi_-$ con $U_\mathrm{E}=2$ V?

:::loesung
(a) $U_\mathrm{A}=-10\cdot0{,}5\,\mathrm{V}=-5$ V, $I_1=106{,}4$ µ A, $R_\mathrm{ent}=4{,}7$ k$\Omega$. (b) $\varphi_-=5\,\mathrm{V}/A=50$ µ V. Con $\beta=4{,}7/51{,}7=0{,}0909$ es $G=-10/(1+1{,}1\cdot10^{-4})=-9{,}9989$. (c) La carga conduce 5 mA; la realimentación, 0,106 mA. Hacia la salida circulan 5,11 mA, que siguen hasta $U_\mathrm{B-}$. (d) $|U_\mathrm{E}|\le1{,}1$ V. Con 2 V es $U_\mathrm{A}=-11$ V y $\varphi_-=(47\cdot2-4{,}7\cdot11)\,\mathrm{V}/51{,}7=0{,}818$ V.
:::
:::

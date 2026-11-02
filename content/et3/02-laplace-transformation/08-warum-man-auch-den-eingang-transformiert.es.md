---
title: Etapa 5: Por qué se transforma también la entrada
pfad: Ingeniería eléctrica / 3.er semestre / Señales y sistemas / Transformada de Laplace
order: 3220800
summary: Toda señal como superposición de $\ee^{pt}$, y por qué un sistema LTI convierte esto en una multiplicación
tags: 
lang: es
---

<span class="anker" id="stufe-5"></span>

:::frage Tiene sentido transformar $h(t)$ para poder multiplicar $H(p)$ por funciones propias y determinar la salida. Pero transformar $s(t)$, en principio, no tiene sentido: desde la teoría de sistemas no se puede hacer nada con ello. Claro, $s*h=h*s$, pero $h(t)$ la mayoría de las veces no es una función propia, así que no se puede escribir $h(t)\cdot S(p)$. ¿Qué significado tiene, en relación con el sistema, transformar una señal cualquiera?
⁠**Qué es correcto en la pregunta:** $H(p)$ dice qué hace el sistema con un bloque elemental $\mathrm{e}^{pt}$. Y $h(t)\cdot S(p)$, efectivamente, no tiene sentido.

⁠**Dónde está el error de razonamiento:** la entrada tampoco es casi nunca una función propia. Un escalón, una señal de voz o un pulso rectangular no son bloques elementales $\mathrm{e}^{pt}$ aislados. Por eso $H(p)\cdot s(t)$ tiene tan poco sentido como $h(t)\cdot S(p)$: $H(p)$ solo puede aplicarse a un bloque elemental, y para una $s(t)$ cualquiera ni siquiera está claro a qué $p$ se refiere. Antes de que $H(p)$ pueda hacer algo, la entrada tiene que estar descompuesta en bloques elementales. Eso es exactamente lo que hace $S(p)$.

⁠**La visión correcta:** en el teorema de convolución $G(p)=H(p)\,S(p)$, cada factor tiene un significado propio relacionado con el sistema:

<ul>

<li>

$S(p)$ es la *receta de la entrada*: cuánto del bloque elemental $\mathrm{e}^{pt}$ contiene la entrada;

</li>

<li>

$H(p)$ es el *efecto del sistema*: por qué número multiplica ese bloque;

</li>

<li>

$G(p)$ es la receta de la salida.

</li>

</ul>

Sin $S(p)$ solo se conoce el efecto sobre bloques aislados, pero no qué bloques llegan. $H(p)$ por sí sola responde a la pregunta «¿Qué ocurre con la salida?» solo en el caso particular de que la entrada sea ella misma un único bloque elemental.

⁠**Con el ejemplo del escalón y el filtro paso bajo RC.** El escalón tiene la receta $S(p)=1/p$. Sobre la recta $\sigma=0{,}5/\mathrm s$, $|S|=2$ en $f=0$, $0{,}16$ en 1 Hz y $0{,}016$ en 10 Hz. Los bloques rápidos son débiles, pero están presentes, y forman el flanco abrupto (fig. [3](der-trick-dampfen-zerlegen-zuruckmultiplizieren.html#abb-3): cuantos más bloques rápidos, más abrupto es el flanco). El filtro paso bajo RC los multiplica por $|H|=0{,}67$, $0{,}15$ y $0{,}016$. En la salida, los bloques rápidos son, por tanto, aproximadamente un factor $2\pi f\cdot RC$ más débiles todavía (para $f\gg1/(2\pi RC)=0{,}16$ Hz), y el flanco desaparece: $g(t)=1-\mathrm{e}^{-t}$ sube de forma continua. Esta explicación necesita las dos transformadas. $H$ por sí sola solo dice «los bloques rápidos se debilitan»; solo $S$ dice que el flanco está formado por bloques rápidos.

⁠**¿Y la simetría $s*h=h*s$?** Matemáticamente, ambas señales están en pie de igualdad: también puede leerse $h$ como entrada y $s$ como «sistema»; entonces $H(p)$ es la receta y $S(p)$, el efecto. La teoría de sistemas reparte los papeles solo según la física: una señal viene de fuera; la otra describe el circuito. En el dominio transformado se transforman siempre *las dos*.
:::

**Otras razones para transformar una señal por sí sola.**

<ul>

<li>

⁠**Medir un sistema.** Si se miden la entrada y la salida de un sistema desconocido, $H(p)=G(p)/S(p)$ da el sistema. Para ello se transforman dos señales, cada una por separado (ejercicio [9](#aufg-9)).

</li>

<li>

⁠**Entender la propia señal.** El sonido de una campana golpeada es una suma de oscilaciones amortiguadas, cada una un par de polos conjugados. $\operatorname{Im} p_r$ es la altura tonal de un parcial, y $-\operatorname{Re} p_r$, su tasa de decaimiento. Unos pocos polos describen todo el sonido. Un instrumento de medida que muestra un espectro hace lo mismo sobre la recta $\sigma=0$.

</li>

<li>

⁠**Convolución sin sistema.** La convolución superpone copias desplazadas y ponderadas de una señal. El sistema es una interpretación de esta operación, no la única. Un ejemplo sin ningún sistema es la suma de puntos de dos dados (capítulo sobre la convolución).

</li>

</ul>

:::ltspice Una red para dos mediciones
⁠**Esquema:** la red que has encontrado en el ejercicio [9](#aufg-9)(c), con la fuente `PULSE(0 1 0 1u 1u 100)` en la entrada y la salida en el nodo `out`. Al lado, sin conexión con el circuito, una fuente de comportamiento `bv` en el nodo `mess` con `V=1-exp(-2*time)`. Hace el papel de la curva de salida medida.

⁠**Directivas:** `.tran 0 3 0 1m`, `.meas tran abw MAX abs(V(out)-V(mess))`.

⁠**Lo que ves:** si la red y los valores de los componentes son correctos, `V(out)` y `V(mess)` quedan superpuestas, y la mayor desviación, `abw`, es prácticamente nula (inferior a $10^{-5}$). Compara así las curvas con tu resultado del ejercicio [9](#aufg-9)(c).
:::

:::aufgabe Ejercicio 8 ★★ ¿Qué bloques elementales forman el flanco?
<span class="anker" id="aufg-8"></span>

Entrada $\varepsilon(t)$; sistema: filtro paso bajo RC con $RC=1$ s. Considera los bloques elementales sobre la recta $\sigma=0{,}5/\mathrm s$.

<ol class="al">

<li>

Calcula $|S(p)|$, $|H(p)|$ y $|G(p)|$ para $f=0$, $1$ Hz y $10$ Hz.

</li>

<li>

¿En qué factor debilita el sistema los bloques de 10 Hz más que los de 1 Hz?

</li>

<li>

Explica con (a) y la fig. [3](der-trick-dampfen-zerlegen-zuruckmultiplizieren.html#abb-3) por qué la salida no tiene flanco. ¿Por qué no basta $H(p)$ por sí sola para esta explicación?

</li>

</ol>

:::loesung
(a) Con $p=0{,}5+\mathrm{j}2\pi f$ (en $1/\mathrm s$), $S=1/p$, $H=1/(p+1)$, $G=SH$:

| $f$ | $\vert S(p)\vert $ | $\vert H(p)\vert $ | $\vert G(p)\vert $ |
|---|---|---|---|
| 0 | 2 | 0,667 | 1,33 |
| 1 Hz | 0,159 | 0,155 | 0,0246 |
| 10 Hz | 0,0159 | 0,0159 | 0,000253 |

(b) $0{,}155/0{,}0159\approx9{,}7$, es decir, casi un factor 10, igual que la frecuencia. Para $|p|$ grande, $|H|\approx1/|p|\approx1/(2\pi f)$.

(c) El flanco del escalón está formado por los bloques rápidos: en la fig. [3](der-trick-dampfen-zerlegen-zuruckmultiplizieren.html#abb-3) se hace más abrupto cuantos más de ellos se toman. En la entrada, sus pesos decrecen como $1/f$; en la salida, como $1/f^2$. En la salida, los bloques rápidos son tan débiles que ya no se forma ningún flanco, y $g(t)$ sube de forma continua. $H(p)$ por sí sola solo dice que los bloques rápidos se debilitan. Que el flanco esté formado precisamente por esos bloques es una afirmación sobre la entrada, y esa está en $S(p)$.
:::
:::

:::aufgabe Ejercicio 9 ★★ Un sistema desconocido a partir de dos mediciones
<span class="anker" id="aufg-9"></span>

A un sistema LTI causal desconocido se le aplica en el instante $t=0$ una tensión de 1 V, $s(t)=\varepsilon(t)$ en V. En la salida se mide $g(t)=\bigl(1-\mathrm{e}^{-2t}\bigr)\varepsilon(t)$ en V ($t$ en s).

<ol class="al">

<li>

Transforma las dos señales, cada una por separado.

</li>

<li>

Determina $H(p)$ y, a partir de ella, $h(t)$.

</li>

<li>

¿De qué red podría tratarse? ¿Qué valor se obtiene?

</li>

<li>

¿Qué polo de $G(p)$ procede de la entrada y cuál del sistema?

</li>

</ol>

:::loesung
(a) $S(p)=\dfrac1p$ para $\operatorname{Re} p>0$. $G(p)=\dfrac1p-\dfrac{1}{p+2}=\dfrac{2}{p(p+2)}$ para $\operatorname{Re} p>0$ (par básico [(2.2)](konvergenzbereich-welche-dampfungen-funktionieren.html#gl-2-2) con $p_0=0$ y $p_0=-2$).

(b) $H(p)=\dfrac{G(p)}{S(p)}=\dfrac{2}{p+2}$. Como el sistema es causal, la región de convergencia está a la derecha del polo: $\operatorname{Re} p>-2$. Con [(2.2)](konvergenzbereich-welche-dampfungen-funktionieren.html#gl-2-2): $h(t)=2\,\mathrm{e}^{-2t}\varepsilon(t)$ en $1/\mathrm s$.

(c) Un filtro paso bajo RC tiene $H(p)=\dfrac{1}{1+pRC}=\dfrac{1/RC}{p+1/RC}$. La comparación con $\dfrac{2}{p+2}$ da $RC=0{,}5$ s, por ejemplo $R=500\,\mathrm{k\Omega}$ y $C=1$ µ F. (Cualquier otra red con la misma función de transferencia se comportaría igual en los bornes. Con mediciones en la entrada y la salida solo se conoce $H$, no los componentes.)

(d) El polo $p=0$ procede de la entrada (escalón), y el polo $p=-2$, del sistema. Al dividir $G/S$ se cancela justamente el polo de la entrada.
:::
:::

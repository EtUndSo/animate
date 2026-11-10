---
title: Derivación numérica y comprobación del gradiente
pfad: Informática / Aprendizaje automático / Fundamentos matemáticos / Derivada, gradiente y regla de la cadena
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Capítulo 3: Derivada, gradiente y regla de la cadena
nachschlagen: ja
order: 15231200
summary: Las derivadas también pueden estimarse sin fórmula: se evalúa la función en dos puntos cercanos y se forma el cociente incremental.
tags: diferencia progresiva, error de truncamiento, diferencia central, números en coma flotante, épsilon de máquina, cancelación catastrófica, comprobación del gradiente, error relativo
lang: es
---

<span class="anker" id="stufe-11"></span>

:::zweck
Las derivadas también pueden estimarse sin fórmula: se evalúa la función en dos puntos cercanos y se forma el cociente incremental. Esto es demasiado lento para calcular así todas las derivadas de una función con muchas entradas, pero ideal para comprobar una derivada deducida o programada. Esta sección muestra lo precisos que son los dos cocientes habituales, por qué perjudica un paso demasiado pequeño y cómo se realiza y se valora una comprobación del gradiente.
:::

### La diferencia progresiva

<span class="anker" id="stufe-11-1"></span>

Según la definición [(1.3)](die-ableitung.html#gl-1-3), el cociente incremental se acerca a la derivada cuando $h$ tiende a cero. Si se calcula con un $h$ pequeño fijo, se obtiene una aproximación, y la pregunta es lo buena que es.

:::definition Definición 11.1 (Diferencia progresiva)
<span class="anker" id="satz-11-1"></span>

Para un paso fijo $h>0$,

<span class="anker" id="gl-11-1"></span>
$$D_+f(x)=\frac{f(x+h)-f(x)}{h} \tag{11.1}$$

se llama la __diferencia progresiva__. Su desviación respecto de $f'(x)$, que se debe únicamente a que $h$ no es cero, se llama __error de truncamiento__.
:::

El error de truncamiento lo da la aproximación cuadrática [(1.6)](die-ableitung.html#gl-1-6): si se sustituye $f(x+h)\approx f(x)+f'(x)h+\tfrac12f''(x)h^2$, se tiene

<span class="anker" id="gl-11-2"></span>
$$D_+f(x)\approx f'(x)+\tfrac12f''(x)\,h . \tag{11.2}$$

El error es, pues, aproximadamente proporcional a $h$: un $h$ diez veces menor da un error de truncamiento aproximadamente diez veces menor.

::::beispiel [Ejemplo numérico]
Para $f(x)=x^3$ en el punto $2$ con $h=10^{-3}$ se tiene $2{,}001^3=8{,}012006001$ y

$$D_+f(2)=\frac{8{,}012006001-8}{0{,}001}=12{,}006001 .$$

El error $0{,}006001$ encaja con $\tfrac12f''(2)\,h=\tfrac12\cdot12\cdot0{,}001=0{,}006$; el resto, $0{,}000001=h^2$, es el término siguiente.
::::

⁠**En resumen:** La diferencia progresiva tiene un error de truncamiento de aproximadamente $\tfrac12f''(x)\,h$, proporcional al paso.

### La diferencia central

<span class="anker" id="stufe-11-2"></span>

La diferencia progresiva mide la pendiente de la secante entre $x$ y $x+h$, y en una curva con curvatura esta secante es sistemáticamente más empinada o más plana que la recta tangente en $x$. Si se coloca la secante simétricamente alrededor de $x$, de $x-h$ a $x+h$, este error se compensa.

:::definition Definición 11.2 (Diferencia central)
<span class="anker" id="satz-11-2"></span>

Para un paso fijo $h>0$,

<span class="anker" id="gl-11-3"></span>
$$D_0f(x)=\frac{f(x+h)-f(x-h)}{2h} \tag{11.3}$$

se llama la __diferencia central__.
:::

:::satz Teorema 11.3 (Error de truncamiento de la diferencia central)
<span class="anker" id="satz-11-3"></span>

Si $f$ tiene una tercera derivada continua, entonces

<span class="anker" id="gl-11-4"></span>
$$D_0f(x)\approx f'(x)+\tfrac16f'''(x)\,h^2 . \tag{11.4}$$

El error de truncamiento es, pues, aproximadamente proporcional a $h^2$.
:::

:::herleitung Por qué se cancela la curvatura
Se prolonga en un término la aproximación cuadrática de la sección [1.5](die-ableitung.html#stufe-1-5). Si, como allí con la parábola, se ajusta además la tercera derivada, se añade el término $\tfrac16f'''(x)\,h^3$; el factor $\tfrac16$ surge porque la tercera derivada de $h^3$ es igual a $6$. Así,

$$f(x\pm h)\approx f(x)\pm f'(x)\,h+\tfrac12f''(x)\,h^2\pm\tfrac16f'''(x)\,h^3 .$$

Si se restan las dos ecuaciones, desaparecen los términos con potencias pares de $h$, porque tienen el mismo signo en ambos lados: $f(x)$ y el término de curvatura $\tfrac12f''h^2$. Queda $f(x+h)-f(x-h)\approx2f'(x)\,h+\tfrac13f'''(x)\,h^3$, y al dividir entre $2h$ resulta [(11.4)](#gl-11-4). Intuitivamente: la curvatura hace más empinada la secante derecha y más plana la izquierda, y la diferencia central es la media de ambas.
:::

Para una función cuadrática, $f'''=0$, y la diferencia central es exacta para todo $h$. Necesita dos evaluaciones nuevas de $f$; la diferencia progresiva, solo una, si $f(x)$ ya se conoce.

::::beispiel [Ejemplo numérico]
Para $f(x)=x^3$ en el punto $2$ con $h=10^{-3}$ se tiene $1{,}999^3=7{,}988005999$ y

$$D_0f(2)=\frac{8{,}012006001-7{,}988005999}{0{,}002}=\frac{0{,}024000002}{0{,}002}=12{,}000001 .$$

El error es $0{,}000001=\tfrac16\cdot6\cdot h^2$, seis mil veces menor que con la diferencia progresiva.
::::

⁠**En resumen:** La diferencia central tiene un error de truncamiento de aproximadamente $\tfrac16f'''(x)\,h^2$, porque el término de curvatura se cancela.

### Lo que necesitas: números en coma flotante

<span class="anker" id="stufe-11-3"></span>

Según las dos fórmulas del error de truncamiento, bastaría con elegir $h$ lo bastante pequeño. Con la calculadora y con cualquier programa de cálculo esto sale mal, y la razón es la forma en que los ordenadores almacenan los números.

Los ordenadores almacenan los números decimales como __números en coma flotante__: como un número con una cantidad fija de cifras en el sistema binario, multiplicado por una potencia de dos. Lo habitual es la doble precisión según la norma IEEE 754, con $53$ dígitos binarios, que equivalen a unas $16$ cifras decimales. El resultado de cada operación se redondea al número representable más cercano. El error relativo de este redondeo es a lo sumo $2^{-53}\approx1{,}1\cdot10^{-16}$. La distancia de $1$ al siguiente número representable mayor es el doble,

$$\varepsilon_{\mathrm M}=2^{-52}\approx2{,}2\cdot10^{-16};$$

este número se llama __épsilon de máquina__, y los programas de cálculo lo muestran con el nombre eps. En simple precisión, con $24$ dígitos binarios, unas $7$ cifras decimales, $\varepsilon_{\mathrm M}=2^{-23}\approx1{,}2\cdot10^{-7}$.

El redondeo se vuelve peligroso al restar números casi iguales. Las cifras delanteras se cancelan, los errores de redondeo de las traseras permanecen, y del resultado solo unas pocas cifras siguen siendo correctas. Esto se llama __cancelación catastrófica__. Un cociente incremental resta precisamente números así, y cuanto menor es $h$, más se parecen.

::::beispiel [Ejemplo numérico]
Para $f(x)=x^3$ en el punto $2$ y $h=10^{-8}$ se tiene $f(2+h)=8{,}00000012\ldots$ Ambos valores de la función son aproximadamente $8$ y llevan cada uno un error de redondeo de hasta unos $8\cdot1{,}1\cdot10^{-16}\approx9\cdot10^{-16}$. Su diferencia es aproximadamente $1{,}2\cdot10^{-7}$; un error de $10^{-15}$ en ella es un error relativo de casi $10^{-8}$. De las $16$ cifras, tras la resta solo unas $8$ siguen siendo correctas, y la división entre $h$ no cambia nada.
::::

⁠**En resumen:** Los ordenadores redondean cada resultado a unas $16$ cifras, $\varepsilon_{\mathrm M}=2^{-52}$; al restar números casi iguales, de ellas solo quedan unas pocas cifras correctas.

### La curva de error

<span class="anker" id="stufe-11-4"></span>

En un cociente incremental actúan, pues, dos errores en sentidos opuestos. El error de truncamiento disminuye con un $h$ menor. El error de redondeo aumenta con un $h$ menor: el error de la diferencia del numerador se mantiene aproximadamente igual, pero se divide entre un $h$ cada vez menor.

:::satz Teorema 11.4 (Error total de los cocientes incrementales)
<span class="anker" id="satz-11-4"></span>

Si los valores de la función son exactos salvo un error relativo de a lo sumo $\tfrac12\varepsilon_{\mathrm M}$, el error total es aproximadamente, como máximo,

<span class="anker" id="gl-11-5"></span>
$$E_+(h)=\tfrac12|f''(x)|\,h+\frac{\varepsilon_{\mathrm M}|f(x)|}{h}\qquad\text{y}\qquad E_0(h)=\tfrac16|f'''(x)|\,h^2+\frac{\varepsilon_{\mathrm M}|f(x)|}{2h} \tag{11.5}$$

para la diferencia progresiva y la central, respectivamente. $E_+$ es mínimo en $h_+=\sqrt{2\varepsilon_{\mathrm M}|f|/|f''|}$, con el valor $\sqrt{2\varepsilon_{\mathrm M}|f|\,|f''|}$; $E_0$ es mínimo en $h_0=\bigl(\tfrac32\varepsilon_{\mathrm M}|f|/|f'''|\bigr)^{1/3}$.
:::

:::herleitung El mejor paso
En el numerador hay dos valores de la función, cada uno con un error de redondeo de hasta $\tfrac12\varepsilon_{\mathrm M}|f|$, en total hasta $\varepsilon_{\mathrm M}|f|$. En la diferencia progresiva esto se divide entre $h$; en la central, entre $2h$. A ello se suman los errores de truncamiento [(11.2)](#gl-11-2) y [(11.4)](#gl-11-4). Una función de la forma $a\,h+b/h$ con $a,b>0$ tiene la derivada $a-b/h^2$, que se anula en $h=\sqrt{b/a}$; allí el valor es $2\sqrt{ab}$. Con $a=\tfrac12|f''|$ y $b=\varepsilon_{\mathrm M}|f|$ resulta $h_+$. Para $a\,h^2+b/h$, la derivada es $2ah-b/h^2$, que se anula en $h^3=b/(2a)$; con $a=\tfrac16|f'''|$ y $b=\tfrac12\varepsilon_{\mathrm M}|f|$ resulta $h_0$.
:::

Si se representa el error frente a $h$ en escala doble logarítmica, aparece una V (fig. [20](#abb-20)). A la derecha, la curva sube con pendiente $1$ (progresiva) o $2$ (central), porque allí domina el error de truncamiento. A la izquierda baja con pendiente $-1$, porque allí domina el error de redondeo. Los puntos medidos de la izquierda se dispersan, pues los errores de redondeo resultan mayores o menores según el número; [(11.5)](#gl-11-5) solo da su orden de magnitud. Como regla práctica, se elige en la progresiva $h\approx\sqrt{\varepsilon_{\mathrm M}}\approx10^{-8}$ y en la central $h\approx\varepsilon_{\mathrm M}^{1/3}\approx6\cdot10^{-6}$, multiplicados en cada caso por el orden de magnitud de $x$ si $|x|$ es mayor que $1$.

:::abbildung ml/k3vkurve 20
El error de los dos cocientes incrementales para $f(x)=x^3$ en el punto $2$, calculado en doble precisión, frente al paso $h$ de $10^{-15}$ a $10^{-1}$, con ambos ejes en escala logarítmica. A la derecha domina el error de truncamiento (pendiente $1$ o $2$, respectivamente); a la izquierda, el error de redondeo (pendiente $-1$). Las curvas discontinuas son las estimaciones [(11.5)](#gl-11-5); los puntos más bajos están en $h\approx10^{-8}$ (progresiva) y en $h\approx3\cdot10^{-6}$ (central).
:::

::::beispiel [Ejemplo numérico]
Para $f(x)=x^3$ en el punto $2$ se tiene $|f|=8$, $|f''|=12$ y $|f'''|=6$. El mejor paso de la diferencia progresiva es $h_+=\sqrt{2\cdot2{,}2\cdot10^{-16}\cdot8/12}\approx1{,}7\cdot10^{-8}$, con un error de aproximadamente $\sqrt{2\cdot2{,}2\cdot10^{-16}\cdot8\cdot12}\approx2{,}1\cdot10^{-7}$; referido a $f'(2)=12$, son unas ocho cifras correctas. El mejor paso de la diferencia central es $h_0=(1{,}5\cdot2{,}2\cdot10^{-16}\cdot8/6)^{1/3}\approx7{,}6\cdot10^{-6}$, con un error de aproximadamente $(7{,}6\cdot10^{-6})^2+2{,}2\cdot10^{-16}\cdot8/(2\cdot7{,}6\cdot10^{-6})\approx1{,}7\cdot10^{-10}$, unas once cifras correctas. La fig. [20](#abb-20) confirma ambas cosas: se midieron $7{,}3\cdot10^{-8}$ en $h=10^{-8}$ y $2{,}0\cdot10^{-11}$ en $h\approx3{,}2\cdot10^{-6}$. Con $h=10^{-14}$, en cambio, en ambos cocientes ya es incorrecta la primera cifra decimal.
::::

⁠**En resumen:** Un $h$ demasiado grande da error de truncamiento, y uno demasiado pequeño, error de redondeo; lo mejor es $h\approx10^{-8}$ en la progresiva y $h\approx10^{-5}$ a $10^{-6}$ en la central, y la diferencia central alcanza así unas once cifras correctas en lugar de ocho.

### La comprobación del gradiente

<span class="anker" id="stufe-11-5"></span>

Quien deduce un gradiente a mano o lo programa como pasos hacia atrás comete errores con facilidad: un camino olvidado, una trasposición que falta, un factor incorrecto. Un cociente incremental no necesita deducción; solo evalúa la función. Si se comparan ambos, estos errores se encuentran de forma fiable.

:::definition Definición 11.5 (Comprobación del gradiente)
<span class="anker" id="satz-11-5"></span>

En la __comprobación del gradiente__ se compara un gradiente calculado $\mathbf{g}_{\mathrm a}$ en un punto $\mathbf{x}$ con el gradiente numérico $\mathbf{g}_{\mathrm n}$, cuyas componentes son diferencias centrales,

<span class="anker" id="gl-11-6"></span>
$$g_{\mathrm n,j}=\frac{f(\mathbf{x}+h\,\mathbf{e}_j)-f(\mathbf{x}-h\,\mathbf{e}_j)}{2h}. \tag{11.6}$$

Para cada componente se calcula el __error relativo__

<span class="anker" id="gl-11-7"></span>
$$\rho_j=\frac{|g_{\mathrm a,j}-g_{\mathrm n,j}|}{\max\bigl(|g_{\mathrm a,j}|,\,|g_{\mathrm n,j}|\bigr)}, \tag{11.7}$$

donde se toma $\rho_j=0$ si ambos valores son nulos.
:::

Se compara en términos relativos porque un error absoluto de $10^{-6}$ es excelente en una derivada de $10^{6}$, pero un fracaso completo en una derivada de $10^{-6}$. Con cálculo en doble precisión y $h$ del orden de $10^{-5}$ valen estos valores empíricos: un error relativo por encima de $10^{-2}$ significa casi con seguridad un error en la fórmula. Entre $10^{-2}$ y $10^{-4}$, el resultado es sospechoso. Por debajo de $10^{-4}$ suele estar bien en funciones con puntos angulosos, y $10^{-7}$ o menos es un buen resultado. Una comprobación cuesta $2n$ evaluaciones de $f$; por eso se comprueba solo en unos pocos puntos o solo algunas componentes. Para el cálculo propiamente dicho está el modo inverso; para su control, el cociente incremental.

::::beispiel [Ejemplo numérico 1]
Para $f(\mathbf{x})=x_1^2x_2+x_2^2$, alguien ha deducido el gradiente $(2x_1x_2,\ x_1^2+x_2)^{\top}$, con un factor $2$ olvidado. En el punto $(1,\,2)$ esto da $\mathbf{g}_{\mathrm a}=(4,\,3)^{\top}$. Con $h=0{,}001$ se tiene

$$\begin{aligned} g_{\mathrm n,1}&=\frac{f(1{,}001;\ 2)-f(0{,}999;\ 2)}{0{,}002}=\frac{6{,}004002-5{,}996002}{0{,}002}=4,\\ g_{\mathrm n,2}&=\frac{f(1;\ 2{,}001)-f(1;\ 1{,}999)}{0{,}002}=\frac{6{,}005001-5{,}995001}{0{,}002}=5 . \end{aligned}$$

Las diferencias centrales son aquí exactas, porque $f$ es a lo sumo cuadrática en cada variable por separado. Los errores relativos son $\rho_1=0$ y $\rho_2=|3-5|/5=0{,}4$: la segunda componente es incorrecta.
::::

::::beispiel [Ejemplo numérico 2]
Se comprueba la fórmula $\sigma'(x)=\sigma(x)(1-\sigma(x))$ en el punto $1$. Con diez cifras, $\sigma(1)\approx0{,}7310585786$, y la fórmula da $0{,}7310585786\cdot0{,}2689414214\approx0{,}1966119332$. Con $h=0{,}01$ se tiene $\sigma(1{,}01)\approx0{,}7330201492$ y $\sigma(0{,}99)\approx0{,}7290879223$, es decir,

$$g_{\mathrm n}=\frac{0{,}7330201492-0{,}7290879223}{0{,}02}=\frac{0{,}0039322269}{0{,}02}\approx0{,}196611345 .$$

El error relativo es $\rho\approx5{,}9\cdot10^{-7}/0{,}1966\approx3{,}0\cdot10^{-6}$. Procede del error de truncamiento del paso, relativamente grande, y está muy por debajo del umbral $10^{-2}$; la fórmula es correcta. En doble precisión con $h=10^{-5}$, baja a aproximadamente $10^{-11}$.
::::

⁠**En resumen:** La comprobación del gradiente compara un gradiente calculado, componente a componente, con diferencias centrales; errores relativos por encima de $10^{-2}$ indican un error en la fórmula, y por debajo de $10^{-7}$, una fórmula correcta.

### Puntos angulosos y otras trampas

<span class="anker" id="stufe-11-6"></span>

Una comprobación del gradiente puede dar la alarma aunque la fórmula sea correcta, o callar aunque sea incorrecta. Las causas más frecuentes pueden preverse.

La primera causa son los puntos angulosos. En un punto anguloso, como el de $|x|$ o $\max(x,\,0)$ en el punto $0$, no existe derivada. Si hay un punto anguloso entre $x-h$ y $x+h$, la diferencia central mide una mezcla de las dos pendientes a la izquierda y a la derecha, mientras que la derivada calculada solo conoce una de ellas. La segunda causa es una precisión demasiado baja. En simple precisión, $\varepsilon_{\mathrm M}\approx1{,}2\cdot10^{-7}$; según [(11.5)](#gl-11-5), el mejor paso de la diferencia central está entonces en torno a $10^{-2}$, y errores relativos de entre $10^{-5}$ y $10^{-3}$ son normales incluso con una fórmula correcta. La tercera es un paso demasiado pequeño, que dispara el error de redondeo. La cuarta son los gradientes muy pequeños: si ambos valores son casi nulos, el error relativo dice poco, y se examina además el error absoluto. Por último, conviene comprobar en un punto aleatorio, no en uno especial: en el punto $\mathbf{x}=\mathbf{0}$ desaparecen muchos términos de una fórmula, y con ellos los errores que contienen esos términos.

:::warnung Solo queda comprobado lo que se comprueba
Una comprobación del gradiente superada en un punto muestra que la fórmula es correcta allí, no en todas partes. Un término olvidado que es nulo en el punto comprobado pasa inadvertido. Por eso, comprueba en varios puntos con números irregulares y todas las componentes que se calculan de forma distinta.
:::

::::beispiel [Ejemplo numérico]
Para $f(x)=|x|$ en el punto $x=10^{-6}$, la derivada es $1$. Con $h=10^{-5}$, el punto anguloso en $0$ está entre $x-h$ y $x+h$, y

$$D_0f(10^{-6})=\frac{|1{,}1\cdot10^{-5}|-|-0{,}9\cdot10^{-5}|}{2\cdot10^{-5}}=\frac{0{,}2\cdot10^{-5}}{2\cdot10^{-5}}=0{,}1 .$$

El error relativo es $0{,}9$, aunque la fórmula $f'(x)=1$ para $x>0$ es correcta. Con $h=10^{-7}$, el punto anguloso queda fuera, y la diferencia central es exactamente $1$.
::::

⁠**En resumen:** Los puntos angulosos, la simple precisión, los pasos demasiado pequeños y los gradientes cercanos a cero falsean la comprobación; se comprueba en varios puntos irregulares.

:::aufgabe Ejercicio 39 ★ Dos cocientes incrementales
<span class="anker" id="aufg-39"></span>

Sea $f(x)=\mathrm{e}^x$ y $x=0$, es decir, $f'(0)=1$.

<ol class="al">

<li>

Calcula con la calculadora $D_+f(0)$ y $D_0f(0)$ para $h=0{,}1$ y $h=0{,}01$.

</li>

<li>

Compara los errores con las aproximaciones $\tfrac12f''(0)\,h$ y $\tfrac16f'''(0)\,h^2$.

</li>

</ol>

:::loesung
(a) Con $\mathrm{e}^{0{,}1}\approx1{,}105170918$, $\mathrm{e}^{-0{,}1}\approx0{,}904837418$, $\mathrm{e}^{0{,}01}\approx1{,}010050167$ y $\mathrm{e}^{-0{,}01}\approx0{,}990049834$:

$$\begin{aligned} h=0{,}1:&\quad D_+=\frac{1{,}105170918-1}{0{,}1}\approx1{,}05171,\\ &\quad D_0=\frac{1{,}105170918-0{,}904837418}{0{,}2}\approx1{,}001668;\\ h=0{,}01:&\quad D_+=\frac{1{,}010050167-1}{0{,}01}\approx1{,}005017,\\ &\quad D_0=\frac{1{,}010050167-0{,}990049834}{0{,}02}\approx1{,}0000167 . \end{aligned}$$

(b) Los errores de la diferencia progresiva son $0{,}0517$ y $0{,}0050$; la aproximación $\tfrac12h$ predice $0{,}05$ y $0{,}005$. Los errores de la diferencia central son $0{,}00167$ y $0{,}0000167$; la aproximación $\tfrac16h^2$ predice $0{,}00167$ y $0{,}0000167$. Un $h$ diez veces menor hace uno de los errores diez veces menor, y el otro, cien veces menor.
:::
:::

:::aufgabe Ejercicio 40 ★★ Una comprobación del gradiente
<span class="anker" id="aufg-40"></span>

Para $f(\mathbf{x})=x_1\,\mathrm{e}^{x_2}$, alguien afirma que $\nabla f(\mathbf{x})=(\mathrm{e}^{x_2},\ \mathrm{e}^{x_2})^{\top}$.

<ol class="al">

<li>

Calcula en el punto $(2,\,0)$ el gradiente numérico con $h=0{,}01$ y los errores relativos de ambas componentes. ¿Qué componente es incorrecta?

</li>

<li>

¿Por qué no habría sido adecuada la comprobación en el punto $(1,\,0)$?

</li>

</ol>

:::loesung
(a) Respecto de $x_1$: $\frac{f(2{,}01;\,0)-f(1{,}99;\,0)}{0{,}02}=\frac{2{,}01-1{,}99}{0{,}02}=1$; la afirmación dice $\mathrm{e}^0=1$, así que $\rho_1=0$. Respecto de $x_2$:

$$g_{\mathrm n,2}=\frac{2\,\mathrm{e}^{0{,}01}-2\,\mathrm{e}^{-0{,}01}}{0{,}02}\approx\frac{2{,}0201003-1{,}9800997}{0{,}02}\approx2{,}0000333 .$$

La afirmación dice $1$, así que $\rho_2=|1-2{,}0000333|/2{,}0000333\approx0{,}5$. La segunda componente es incorrecta; lo correcto es $x_1\mathrm{e}^{x_2}=2$.

(b) En el punto $(1,\,0)$ se tiene $x_1\mathrm{e}^{x_2}=1=\mathrm{e}^{x_2}$: allí, la fórmula incorrecta coincide por casualidad con la correcta, y la comprobación solo habría dado un error relativo de unos $2\cdot10^{-5}$, causado por el error de truncamiento. El error habría pasado inadvertido.
:::
:::

:::aufgabe Ejercicio 41 ★★ El mejor paso
<span class="anker" id="aufg-41"></span>

Sea $f(x)=\mathrm{e}^x$ en el punto $1$, es decir, $f=f''=f'''=\mathrm{e}$.

<ol class="al">

<li>

Calcula $h_+$, $h_0$ y los errores mínimos correspondientes según [(11.5)](#gl-11-5) para doble precisión.

</li>

<li>

Repite el cálculo para simple precisión. ¿Cuántas cifras correctas pueden esperarse entonces como máximo?

</li>

</ol>

:::loesung
(a) Con $|f|=|f''|=|f'''|=\mathrm{e}$ y $\varepsilon_{\mathrm M}\approx2{,}22\cdot10^{-16}$:

$$\begin{aligned} h_+&=\sqrt{2\varepsilon_{\mathrm M}}\approx2{,}1\cdot10^{-8}, & E_+(h_+)&=\mathrm{e}\sqrt{2\varepsilon_{\mathrm M}}\approx5{,}7\cdot10^{-8},\\ h_0&=(1{,}5\,\varepsilon_{\mathrm M})^{1/3}\approx6{,}9\cdot10^{-6}, & E_0(h_0)&=\tfrac{\mathrm{e}}6h_0^2+\frac{\varepsilon_{\mathrm M}\mathrm{e}}{2h_0}\approx6{,}5\cdot10^{-11}. \end{aligned}$$

Referidos a $f'(1)=\mathrm{e}$, son errores relativos de unos $2\cdot10^{-8}$ y $2\cdot10^{-11}$, es decir, casi ocho y casi once cifras correctas.

(b) Con $\varepsilon_{\mathrm M}\approx1{,}19\cdot10^{-7}$ se tiene $h_+\approx4{,}9\cdot10^{-4}$, con $E_+\approx1{,}3\cdot10^{-3}$, y $h_0\approx5{,}6\cdot10^{-3}$, con $E_0\approx4{,}3\cdot10^{-5}$. En relación con $\mathrm{e}$, son unos $5\cdot10^{-4}$ y $1{,}6\cdot10^{-5}$: como máximo pueden esperarse unas tres y unas cinco cifras correctas, respectivamente. Por eso, una comprobación del gradiente en simple precisión da, incluso con la fórmula correcta, errores relativos del orden de $10^{-5}$ a $10^{-3}$.
:::
:::

:::aufgabe Ejercicio 42 ★★★ Punto anguloso en el grafo
<span class="anker" id="aufg-42"></span>

Sea $f(\mathbf{x})=\max(x_1,\,x_2)\cdot x_3$.

<ol class="al">

<li>

Calcula en el modo inverso el gradiente en el punto $(2;\ 2{,}000001;\ 3)$.

</li>

<li>

Calcula la diferencia central respecto de $x_1$ con $h=10^{-5}$ y el error relativo. ¿Es incorrecta la fórmula?

</li>

<li>

¿Qué da el modo inverso en el punto $(2,\,2,\,3)$, y por qué no existe allí gradiente?

</li>

</ol>

:::loesung
(a) En el punto $(2;\ 2{,}000001;\ 3)$ se tiene $v=\max(x_1,x_2)=x_2=2{,}000001$ y $f=6{,}000003$. Hacia atrás: $\bar f=1$, $\bar v=x_3=3$, $\bar x_3=v=2{,}000001$; el máximo transmite $\bar v$ a la entrada mayor, $x_2$, es decir, $\bar x_2=3$ y $\bar x_1=0$. El gradiente es $(0;\ 3;\ 2{,}000001)^{\top}$.

(b) $f(2{,}00001;\ 2{,}000001;\ 3)=3\cdot2{,}00001=6{,}00003$ y $f(1{,}99999;\ 2{,}000001;\ 3)=3\cdot2{,}000001=6{,}000003$, así que

$$g_{\mathrm n,1}=\frac{6{,}00003-6{,}000003}{0{,}00002}=\frac{0{,}000027}{0{,}00002}=1{,}35$$

y $\rho_1=|0-1{,}35|/1{,}35=1$. Aun así, la fórmula es correcta. El punto anguloso en $x_1=x_2$ está entre $x_1-h$ y $x_1+h$: a su derecha, $f$ sube con la pendiente $3$ en $x_1$; a su izquierda, no sube en absoluto, y la diferencia central mezcla ambas cosas.

(c) En el punto $(2,\,2,\,3)$, las dos entradas del máximo son iguales. El modo inverso transmite $\bar v=3$ a una de las dos, según cuál trate el cálculo como mayor en caso de empate; da, por tanto, $(3,\,0,\,2)^{\top}$ o $(0,\,3,\,2)^{\top}$. Allí no existe gradiente: si se aumenta $x_1$, $f$ sube con la pendiente $3$; si se disminuye $x_1$, $f$ no cambia. Las pendientes laterales son distintas, como en $|x|$ en el punto $0$.
:::
:::

---
title: Funciones de correlación
pfad: Ingeniería eléctrica / 3.er semestre / Señales y sistemas / Funciones de correlación
order: 3260100
summary: ¿Cuánto se parecen dos señales y cómo se reparte la energía en frecuencia?
tags: energía de la señal, señal de energía, potencia, señal de potencia, coeficiente de correlación, ortogonales, función de autocorrelación, función de correlación cruzada
lang: es
---

## De qué trata

Un radar emite un pulso y busca su eco en la señal recibida. Un teléfono móvil busca en el ruido una secuencia de sincronización conocida. Ambos se plantean la misma pregunta: *¿Cuánto se parece una señal a otra y con qué desplazamiento se parecen más?* La respuesta la da la función de correlación. Su transformada de Fourier indica además cómo se reparte la energía de una señal entre las frecuencias.

:::merke La respuesta en tres frases (al final del artículo deberían resultar evidentes)
<ol>

<li>

La semejanza de dos señales se mide con la integral de su producto. La función de correlación lo hace para cada desplazamiento $\tau$; es una convolución con la señal reflejada.

</li>

<li>

La transformada de Fourier de la función de autocorrelación (FAC) es la densidad espectral de energía $|S(f)|^2$. En $\tau=0$ se obtiene la energía (Parseval).

</li>

<li>

Al pasar por un sistema LTI, las densidades espectrales de energía se multiplican por $|H(f)|^2$, y las funciones de autocorrelación se convolucionan con la función de autocorrelación de $h$.

</li>

</ol>
:::

**Un principio detrás de todos los resultados.** La correlación es una convolución con una señal reflejada. Por eso valen todas las herramientas de la convolución:

| Resultado | De dónde viene |
|---|---|
| Coeficiente de correlación | energía de la diferencia de dos señales normalizadas (etapa [2](#stufe-2)) |
| Producto de correlación | convolución con la señal reflejada y conjugada (etapa [3](#stufe-3)) |
| FAC par, máximo en 0 | reflejar, y a lo que más se parece una señal es a sí misma (etapa [3](#stufe-3)) |
| Densidad espectral de energía, Parseval | reflejar y conjugar da $S^*$, la convolución se convierte en producto (etapa [4](#stufe-4)) |
| Wiener-Lee | ley asociativa de la convolución (etapa [5](#stufe-5)) |
| Caso discreto, periódico, DFT | el mismo cálculo con sumas (etapa [7](#stufe-7)) |

**Cómo trabajar con este artículo.** Cada etapa tiene la idea, preguntas típicas con respuestas desplegables y ejercicios (de ★ a ★★★). Intenta resolverlos primero por tu cuenta; la solución se despliega justo debajo de cada ejercicio.

:::merke El modelo de referencia de este artículo
Pulso rectangular $\operatorname{rect}(t)$, triángulo $\Lambda(t)$, pulso exponencial $\varepsilon(t)\mathrm{e}^{-t}$ (la respuesta al impulso del circuito RC con $RC=1$ s) y la secuencia $(1,2,1)$. El script `rechnung_kap6.py` recalcula los números.
:::

## Etapa 1: Energía y potencia

<span class="anker" id="stufe-1"></span>

:::zweck
Antes de comparar señales hace falta una medida de su «tamaño». En teoría de sistemas, esa medida es la energía y, en las señales de duración infinita, la potencia.
:::

En una resistencia $R$, durante el intervalo de $t_1$ a $t_2$ se convierte en calor la energía $\frac1R\int u^2\mathrm{d} t$. Sin el factor $1/R$, la expresión se llama __energía de la señal__:

<span class="anker" id="gl-1-1"></span>
$$E_s=\int_{-\infty}^{\infty}|s(t)|^2\,\mathrm{d} t. \tag{1.1}$$

Si es finita, $s$ se llama __señal de energía__ (por ejemplo, cualquier pulso). Si una señal dura indefinidamente sin decaer (un coseno, un escalón), su energía es infinita. Entonces se mide la __potencia__ media:

<span class="anker" id="gl-1-2"></span>
$$L_s=\lim_{T\to\infty}\frac{1}{2T}\int_{-T}^{T}|s(t)|^2\,\mathrm{d} t. \tag{1.2}$$

Si es finita, $s$ se llama __señal de potencia__. En las señales periódicas basta con promediar sobre un periodo. Para los impulsos de Dirac no están definidas ni la energía ni la potencia ($\delta^2$ no existe).

:::aufgabe Ejercicio 1 ★ ¿Energía o potencia?
<span class="anker" id="aufg-1"></span>

Determina la energía o la potencia de (a) $a\operatorname{rect}(t/T)$, (b) $\varepsilon(t)\mathrm{e}^{-t}$, (c) $A\cos(2\pi Ft)$, (d) $\varepsilon(t)$.

:::loesung
(a) $E=a^2|T|$. (b) $E=\int_0^\infty\mathrm{e}^{-2t}\mathrm{d} t=\frac12$. (c) Energía infinita, potencia $\frac{A^2}{2}$ (el valor medio de $\cos^2$ es $\frac12$). (d) Energía infinita, potencia $\lim\frac{1}{2T}\int_0^T1\,\mathrm{d} t=\frac12$: la señal vale 1 durante la mitad del tiempo.
:::
:::

## Etapa 2: Medir la semejanza, el coeficiente de correlación

<span class="anker" id="stufe-2"></span>

:::zweck
¿Cómo se mide con un solo número cuánto se parecen dos señales? Midiendo lo grande que es su diferencia.
:::

**La idea.** La energía de la diferencia $\Delta(t)=s(t)-g(t)$ es pequeña si las señales se parecen. Desarrollando el producto:

$$E_\Delta=\int|s-g|^2\mathrm{d} t=E_s+E_g-\int s^*g\,\mathrm{d} t-\int g^*s\,\mathrm{d} t=E_s+E_g-2\operatorname{Re}\int s^*(t)g(t)\,\mathrm{d} t.$$

Así pues, la diferencia reside únicamente en la integral del producto. Para que el tamaño de las señales no cuente, se normalizan ambas a energía 1. Entonces $E_\Delta=2-2\operatorname{Re}\,p_{sg}$, con el __coeficiente de correlación__

<span class="anker" id="gl-2-1"></span>
$$p_{sg}=\frac{\int_{-\infty}^{\infty}s^*(t)\,g(t)\,\mathrm{d} t}{\sqrt{E_sE_g}}. \tag{2.1}$$

⁠**Cómo leerlo:** $|p_{sg}|\le1$ (desigualdad de Cauchy-Schwarz). $p=1$ significa $s=a\,g$ con $a>0$: la misma forma. $p=-1$ significa $s=-a\,g$: la misma forma, con el signo invertido. $p=0$ significa $\int s^*g\,\mathrm{d} t=0$: las señales son __ortogonales__, como los armónicos de una serie de Fourier en la [parte 3](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html). Ejemplo: $\operatorname{rect}(t)$ y $\Lambda(t)$ tienen $\int\operatorname{rect}\cdot\Lambda\,\mathrm{d} t=0{,}75$, $E_{\operatorname{rect}}=1$, $E_\Lambda=\frac23$; por tanto, $p=0{,}919$.

:::aufgabe Ejercicio 2 ★★ Coeficientes de correlación
<span class="anker" id="aufg-2"></span>

Calcula $p$ para (a) $\operatorname{rect}(t)$ y $\operatorname{rect}(t-0{,}5)$, (b) $\operatorname{rect}(t)$ y $\Lambda(t)$ (resultado de arriba), (c) $\operatorname{rect}(t)$ y $\operatorname{sgn}(t)\operatorname{rect}(t)$.

:::loesung
(a) Los rectángulos se solapan en una longitud de 0,5; por tanto, $\int=0{,}5$, y ambas energías valen 1: $p=0{,}5$. (b) $\int\operatorname{rect}\cdot\Lambda\,\mathrm{d} t=\int_{-1/2}^{1/2}(1-|t|)\mathrm{d} t=0{,}75$, $E_\Lambda=2\int_0^1(1-t)^2\mathrm{d} t=\frac23$: $p=\frac{0{,}75}{\sqrt{2/3}}=0{,}919$. Formas muy parecidas. (c) $\int\operatorname{sgn}(t)\operatorname{rect}^2(t)\mathrm{d} t=0$: $p=0$; las señales son ortogonales, aunque coinciden en la mitad derecha.
:::
:::

## Etapa 3: Función de correlación y producto de correlación

<span class="anker" id="stufe-3"></span>

:::zweck
Un eco se parece al pulso emitido, pero está desplazado. Por eso se compara para cada desplazamiento $\tau$.
:::

:::definition Definición 3.1 (Función de correlación para señales de energía)
<span class="anker" id="satz-3-1"></span>

<span class="anker" id="gl-3-1"></span>
$$\varphi^E_{sg}(\tau)=\int_{-\infty}^{\infty}s^*(t)\,g(t+\tau)\,\mathrm{d} t=s^*(-\tau)*g(\tau). \tag{3.1}$$

Para $g=s$ se llama __función de autocorrelación__ (FAC) $\varphi^E_{ss}(\tau)$; en otro caso, __función de correlación cruzada__ (FCC). Dividida por $\sqrt{E_sE_g}$, se llama normalizada.
:::

⁠**Cómo leerlo:** se desplaza $g$ una distancia $\tau$ hacia la izquierda y se calcula la integral del producto. El segundo signo igual es la clave: la correlación es una convolución con la señal reflejada y conjugada. Por eso se llama también __producto de correlación__. A diferencia de la convolución, aquí no se refleja nada: ambas señales avanzan en el mismo sentido.

:::herleitung correlación como convolución
En [(3.1)](#gl-3-1), sustituir $t=-\vartheta$: $\int s^*(-\vartheta)\,g(\tau-\vartheta)\,\mathrm{d}\vartheta$. Esta es la integral de convolución de $s^*(-\tau)$ con $g(\tau)$.
:::

:::satz Teorema 3.2 (Propiedades de las funciones de correlación)
<span class="anker" id="satz-3-2"></span>

<span class="anker" id="gl-3-2"></span>
<span class="anker" id="gl-3-3"></span>
$$\begin{aligned} &\varphi^E_{gs}(\tau)=\varphi^{E*}_{sg}(-\tau),\qquad\varphi^E_{ss}(\tau)=\varphi^{E*}_{ss}(-\tau)\ \ (\text{par para }s\text{ real}),\\ &|\varphi^E_{ss}(\tau)|\le\varphi^E_{ss}(0)=E_s. \end{aligned} \tag{3.2|3.3}$$

Una señal de duración limitada tiene una FAC de duración doble.
:::

⁠**Cómo leerlo:** a lo que más se parece una señal es a sí misma sin desplazar, y ahí la FAC es su energía. La FAC de un rectángulo es el triángulo: $\varphi^E_{ss}=\operatorname{rect}(-\tau)*\operatorname{rect}(\tau)=\Lambda(\tau)$, el doble de ancho que el rectángulo (fig. [1](#abb-1), izquierda).

**Ejemplo: encontrar un eco.** Se emite $s=\operatorname{rect}(t)$ y se recibe el eco atenuado y retrasado $g=0{,}5\operatorname{rect}(t-3)$. La FCC es $\varphi^E_{sg}(\tau)=0{,}5\,\Lambda(\tau-3)$: su máximo está en $\tau=3$, el retardo, y su altura $0{,}5=0{,}5\cdot E_s$ indica la atenuación (fig. [1](#abb-1), derecha). Así mide un radar la distancia.

:::abbildung et3/k6korr
Izquierda: la FAC del rectángulo es el triángulo, con máximo $=E_s=1$ en $\tau=0$ y el doble de anchura. Derecha: la FCC entre el pulso emitido y el eco $0{,}5\operatorname{rect}(t-3)$ tiene su máximo en el retardo $\tau=3$.
:::

:::frage La convolución y la correlación parecen casi iguales. ¿Dónde está la diferencia?
En la convolución, $\int s(\tau)h(t-\tau)\mathrm{d}\tau$, la segunda señal avanza hacia atrás ($-\tau$): el sistema «recuerda» el pasado. En la correlación, $\int s^*(t)g(t+\tau)\mathrm{d} t$, ambas avanzan hacia delante: se colocan dos formas una exactamente sobre la otra y se mide su coincidencia. En el cálculo, la diferencia es precisamente la reflexión; por eso la correlación es una convolución con la señal reflejada.
:::

:::ltspice Encontrar un eco con un integrador deslizante
Un filtro que en cada instante integra sobre el último segundo forma $y(t)=\int_{t-1}^{t}g(u)\,\mathrm{d} u$. Con $s=\operatorname{rect}(t)$, esto es exactamente la FCC [(3.1)](#gl-3-1), retrasada 0,5 s: $y(t)=\varphi^E_{sg}(t-0{,}5)$. El filtro la calcula para todos los $\tau$ mientras llega la señal.

⁠**Esquema:** fuente `voltage` en el nodo `g` con `PULSE(0 0.5 2.5 1u 1u 1)`, el eco $0{,}5\operatorname{rect}(t-3)$. Dos fuentes de comportamiento `bv`: en el nodo `int`, con `V=idt(V(g))` (integral acumulada), y en el nodo `y`, con `V=V(int)-delay(V(int),1)` (integral sobre el último segundo).

⁠**Directivas:** `.tran 0 6 0 1m`, `.meas tran ymax MAX V(y)`.

⁠**Lo que ves:** `V(y)` es el triángulo $0{,}5\,\Lambda(t-3{,}5)$, con el máximo 0,5 en $t=3{,}5$ s: el retardo de 3 s más 0,5 s, porque el filtro no termina de integrar hasta el final del eco. La altura 0,5 es la atenuación del eco.

⁠**Para el ejercicio [3](#aufg-3):** entrada `PULSE(0 1 0 1u 1u 1 2 2)`, el doble rectángulo, ambos rectángulos 0,5 s más tarde que en el texto. Para `y` tomas

`V=V(int)-delay(V(int),1)+delay(V(int),2)-delay(V(int),3)`.

Este filtro integra sobre dos ventanas que encajan con el doble rectángulo, y `V(y)` es su FAC, desplazada 3 s. Compara con tu resultado del ejercicio [3](#aufg-3)(a).
:::

:::aufgabe Ejercicio 3 ★★ Eco y repetición
<span class="anker" id="aufg-3"></span>

<ol class="al">

<li>

Una señal consta de dos rectángulos: $s(t)=\operatorname{rect}(t)+\operatorname{rect}(t-2)$. Determina su FAC. ¿En qué se ve la repetición?

</li>

<li>

Comprueba [(3.3)](#gl-3-3) para esta señal.

</li>

</ol>

:::loesung
(a) Con $\operatorname{rect}(-\tau)=\operatorname{rect}(\tau)$ y $\operatorname{rect}*\operatorname{rect}=\Lambda$, los cuatro productos parciales dan

$$\varphi^E_{ss}(\tau)=2\Lambda(\tau)+\Lambda(\tau-2)+\Lambda(\tau+2).$$

Los picos secundarios en $\tau=\pm2$ muestran la separación de la repetición. Allí, uno de los dos rectángulos queda sobre el otro. En $\tau=0$ quedan ambos superpuestos, lo que da la altura doble.

(b) $\varphi^E_{ss}(0)=2=E_s=1+1$, y los picos secundarios solo valen 1.
:::
:::

## Etapa 4: Densidad espectral de energía

<span class="anker" id="stufe-4"></span>

:::zweck
¿Cuál es la transformada de Fourier de una función de correlación? Muestra cómo se reparte la energía entre las frecuencias.
:::

:::satz Teorema 4.1 (Wiener-Khinchin para señales de energía)
<span class="anker" id="satz-4-1"></span>

<span class="anker" id="gl-4-1"></span>
$$\varphi^E_{ss}(\tau)=s^*(-\tau)*s(\tau)\;\circ\!\!-\!\!\bullet\;S^*(f)\,S(f)=|S(f)|^2,\qquad\varphi^E_{sg}(\tau)\;\circ\!\!-\!\!\bullet\;S^*(f)\,G(f). \tag{4.1}$$
:::

⁠**Cómo leerlo:** $|S(f)|^2$ se llama __densidad espectral de energía__. Es real, nunca negativa y, en las señales reales, par en $f$. La fase de la señal se pierde: todas las señales con el mismo espectro de amplitud tienen la misma FAC. $S^*G$ se llama __densidad espectral de energía cruzada__. La deducción solo necesita el teorema de convolución, la reflexión en el tiempo y la conjugación: $s^*(-\tau)\circ\!\!-\!\!\bullet\,S^*(f)$ ([parte 3](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)).

**Parseval.** En $\tau=0$, la FAC es la energía. Con el teorema del área:

<span class="anker" id="gl-4-2"></span>
$$E_s=\varphi^E_{ss}(0)=\int_{-\infty}^{\infty}|s(t)|^2\,\mathrm{d} t=\int_{-\infty}^{\infty}|S(f)|^2\,\mathrm{d} f. \tag{4.2}$$

Dos señales ortogonales tienen también espectros ortogonales: $\int s^*g\,\mathrm{d} t=\int S^*G\,\mathrm{d} f=0$.

**Ejemplo: el pulso exponencial.** $s(t)=\varepsilon(t)\mathrm{e}^{-t}$ tiene $S(f)=\frac{1}{1+\mathrm{j}2\pi f}$; por tanto, $|S|^2=\frac{1}{1+(2\pi f)^2}$. Esto es a la vez $\operatorname{Re}\{S\}$, y su transformada inversa es la parte par de la señal ([parte 3](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)):

$$\varphi^E_{ss}(\tau)=\tfrac12\mathrm{e}^{-|\tau|},\qquad E_s=\varphi^E_{ss}(0)=\tfrac12.$$

Lo mismo da $\int_0^\infty\mathrm{e}^{-2t}\mathrm{d} t=\frac12$ en el dominio del tiempo y $\int\frac{\mathrm{d} f}{1+(2\pi f)^2}=\frac12$ en el dominio de la frecuencia. La figura [2](#abb-2) muestra la señal, su FAC y los dos espectros.

:::abbildung et3/k6exp
Pulso exponencial ($RC=1$ s). A la izquierda, la señal y su FAC $\frac12\mathrm{e}^{-|\tau|}$ (par, máximo $=E_s=\frac12$). A la derecha, el espectro de amplitud y la densidad espectral de energía, que decae más deprisa: la energía se concentra en las frecuencias bajas.
:::

:::aufgabe Ejercicio 4 ★ Comprobar Parseval
<span class="anker" id="aufg-4"></span>

Calcula la energía de $\operatorname{rect}(t)$ en el dominio del tiempo y, con [(4.2)](#gl-4-2), a partir de su espectro. ¿Qué integral conocida de la función si se deduce de ello?

:::loesung
Dominio del tiempo: $E=\int\operatorname{rect}^2\mathrm{d} t=1$. Dominio de la frecuencia: $\int\operatorname{si}^2(\pi f)\mathrm{d} f$. De ahí se deduce $\int_{-\infty}^\infty\operatorname{si}^2(\pi f)\mathrm{d} f=1$.
:::
:::

## Etapa 5: Correlación y sistemas LTI

<span class="anker" id="stufe-5"></span>

:::zweck
¿Qué le hace un sistema LTI a la FAC y a la densidad espectral de energía? ¿Y cómo se mide un sistema con la correlación cruzada?
:::

:::satz Teorema 5.1 (Wiener-Lee)
<span class="anker" id="satz-5-1"></span>

Para $g=s*h$:

<span class="anker" id="gl-5-1"></span>
$$\varphi^E_{gg}(\tau)=\varphi^E_{ss}(\tau)*\varphi^E_{hh}(\tau)\;\circ\!\!-\!\!\bullet\;|G(f)|^2=|S(f)|^2\,|H(f)|^2, \tag{5.1}$$

<span class="anker" id="gl-5-2"></span>
$$\varphi^E_{sg}(\tau)=\varphi^E_{ss}(\tau)*h(\tau)\;\circ\!\!-\!\!\bullet\;|S(f)|^2\,H(f). \tag{5.2}$$
:::

:::herleitung Wiener-Lee
$\varphi^E_{gg}=g^*(-\tau)*g(\tau)=[s^*(-\tau)*h^*(-\tau)]*[s(\tau)*h(\tau)]$. Reordenar según las leyes conmutativa y asociativa: $[s^*(-\tau)*s(\tau)]*[h^*(-\tau)*h(\tau)]=\varphi^E_{ss}*\varphi^E_{hh}$. Del mismo modo, $\varphi^E_{sg}=s^*(-\tau)*s(\tau)*h(\tau)$.
:::

⁠**Cómo leerlo:** el sistema multiplica la energía en cada frecuencia por $|H|^2$. La fase del sistema no influye en la energía. La ecuación [(5.2)](#gl-5-2) es un método de medida: si la entrada tiene una FAC que es casi un impulso de Dirac ponderado $c\,\delta(\tau)$ (un pulso muy corto o ruido de banda ancha, [parte 7](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/zufallssignale/zufallssignale.html)), la correlación cruzada entre la entrada y la salida es casi $c\,h(\tau)$, es decir, la respuesta al impulso salvo el factor $c$. A diferencia de $|H|^2$, contiene también la fase.

:::ltspice Energía antes y después del circuito RC
⁠**Esquema:** fuente de comportamiento `bv` en el nodo `s` con `V=exp(-time)*(time>0)`, el pulso exponencial $\varepsilon(t)\mathrm{e}^{-t}$. El factor `(time>0)` hace que LTspice calcule el estado inicial en $t=0$ con 0 V y que el condensador empiece descargado. Detrás, el circuito RC (`res` con `1Meg`, `cap` con `1u`) con la salida en el nodo `g`.

⁠**Directivas:** `.tran 0 30 0 1m`, `.meas tran Es INTEG V(s)*V(s)` y `.meas tran Eg INTEG V(g)*V(g)`, las energías según [(1.1)](#gl-1-1).

⁠**Lo que ves:** `Es` $=0{,}500$, como $E_s=\varphi^E_{ss}(0)=\frac12$ en la etapa [4](#stufe-4). Compara `Eg` con tu resultado del ejercicio [5](#aufg-5). La energía de salida es menor porque el circuito RC multiplica la energía en cada frecuencia por $|H|^2\le1$.
:::

:::aufgabe Ejercicio 5 ★★ Energía a la salida
<span class="anker" id="aufg-5"></span>

El pulso exponencial $\varepsilon(t)\mathrm{e}^{-t}$ pasa por un circuito RC con $RC=1$ s.

<ol class="al">

<li>

Determina $|G(f)|^2$ y, a partir de ahí, la energía de salida. Pista: $\int_{-\infty}^\infty\frac{\mathrm{d} x}{(1+x^2)^2}=\frac\pi2$.

</li>

<li>

Compruébalo en el dominio del tiempo con $g(t)=t\,\mathrm{e}^{-t}\varepsilon(t)$ ([parte 1](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html), dos circuitos RC en cascada).

</li>

</ol>

:::loesung
(a) $|G|^2=|S|^2|H|^2=\frac{1}{(1+(2\pi f)^2)^2}$. Con $x=2\pi f$: $E_g=\frac{1}{2\pi}\int\frac{\mathrm{d} x}{(1+x^2)^2}=\frac{1}{2\pi}\cdot\frac\pi2=\frac14$.

(b) $\int_0^\infty t^2\mathrm{e}^{-2t}\mathrm{d} t=\frac{2}{2^3}=\frac14$. Ambos caminos coinciden. La energía baja de $\frac12$ a $\frac14$ porque el segundo circuito RC atenúa aún más las frecuencias altas.
:::
:::

## Etapa 6: Correlación de señales paso banda

<span class="anker" id="stufe-6"></span>

:::zweck
También las funciones de correlación de las señales paso banda se calculan con las envolventes complejas ([parte 5](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme/tiefpass-und-bandpasssysteme.html)).
:::

La FCC de dos señales paso banda reales vuelve a ser una señal paso banda:

$$\varphi^E_{sg}(\tau)=\operatorname{Re}\bigl\{\varphi^E_{sgT}(\tau)\,\mathrm{e}^{\mathrm{j}2\pi f_0\tau}\bigr\}.$$

La señal reflejada tiene la envolvente $s_T^*(-t)$, porque

$$s(-t)=\operatorname{Re}\bigl\{s_T(-t)\mathrm{e}^{-\mathrm{j}2\pi f_0t}\bigr\}=\operatorname{Re}\bigl\{s_T^*(-t)\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr\}.$$

Con la regla de transmisión $g_T=\frac12s_T*h_T$ de la [parte 5](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme/tiefpass-und-bandpasssysteme.html):

<span class="anker" id="gl-6-1"></span>
$$\varphi^E_{sgT}(\tau)=\tfrac12\bigl[s_T^*(-\tau)*g_T(\tau)\bigr]=\tfrac12\int_{-\infty}^{\infty}s_T^*(t)\,g_T(t+\tau)\,\mathrm{d} t,\qquad E_s=\varphi^E_{ss}(0)=\varphi^E_{ssT}(0). \tag{6.1}$$

⁠**Cómo leerlo:** la correlación de dos señales paso banda es la mitad de la correlación de sus envolventes, modulada sobre la portadora. La energía de una señal paso banda es la mitad de la energía de su envolvente compleja: un coseno de amplitud $|s_T|$ solo tiene, en promedio, la mitad de la potencia.

## Etapa 7: Correlación en tiempo discreto y periódica

<span class="anker" id="stufe-7"></span>

:::zweck
Con muestras, la integral se convierte en una suma. Con la DFT, las correlaciones se calculan rápidamente.
:::

:::satz Teorema 7.1 (Correlación en tiempo discreto)
<span class="anker" id="satz-7-1"></span>

<span class="anker" id="gl-7-1"></span>
$$\varphi^E_{sg}(m)=\sum_{n=-\infty}^{\infty}s^*(n)\,g(n+m)=s^*(-m)*g(m),\qquad E_s=\sum_n|s(n)|^2=\int_{-1/2}^{1/2}|S_\mathrm a(f)|^2\,\mathrm{d} f, \tag{7.1}$$

<span class="anker" id="gl-7-2"></span>
$$\varphi^E_{ss}(m)\;\circ\!\!-\!\!\bullet\;|S_\mathrm a(f)|^2\ (\text{periodo }1),\qquad\varphi^E_{gg}(m)=\varphi^E_{ss}(m)*\varphi^E_{hh}(m). \tag{7.2}$$
:::

Para señales paso bajo muestreadas se cumple $\varphi^E_{sg}(mT)=T\sum_ns^*(nT)g((n+m)T)$ y $E_s=T\sum_n|s(nT)|^2$. Una señal de energía en tiempo discreto es una secuencia de cuadrado sumable.

**Ejemplo.** $s=(1,2,1)$: $\varphi^E_{ss}=(1,4,6,4,1)$ para $m=-2,\dots,2$. Máximo $6=E_s$ en $m=0$, par, cinco valores en lugar de tres. Comprobación con Wiener-Khinchin en $f=0$: $|S_\mathrm a(0)|^2=(1+2+1)^2=16=\sum_m\varphi^E_{ss}(m)$.

**Correlación periódica.** Como en la convolución ([parte 4](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme/abtastung-und-zeitdiskrete-systeme.html)), para secuencias de periodo $M$ se cumple

<span class="anker" id="gl-7-3"></span>
$$\varphi^E_{sgd}(m)=\sum_{n=0}^{M-1}s_d^*(n)\,g_d(n+m)\;\circ\!\!-\!\!\bullet\;S_d^*(k)\,G_d(k). \tag{7.3}$$

Calculada con la FFT, se llama __correlación rápida__. Para que la correlación periódica reproduzca la ordinaria, $M$ tiene que ser suficientemente grande. Para $(1,2,1)$, $M=3$ da la secuencia solapada $(6,5,5)$; $M=5$, en cambio, da $(6,4,1,1,4)$, la FAC ordinaria dispuesta de forma cíclica.

**Señales de potencia.** Para señales de energía infinita se promedia:

<span class="anker" id="gl-7-4"></span>
$$\varphi^L_{sg}(\tau)=\lim_{T\to\infty}\frac1T\int_{-T/2}^{T/2}s^*(t)\,g(t+\tau)\,\mathrm{d} t. \tag{7.4}$$

Si ambas señales son periódicas con el mismo periodo, basta con un periodo, y la función de correlación también es periódica. Ejemplo: $A\cos(2\pi Ft+\varphi_0)$ tiene la FAC $\frac{A^2}{2}\cos(2\pi F\tau)$. La fase $\varphi_0$ ha desaparecido; en $\tau=0$ se obtiene la potencia $\frac{A^2}{2}$.

:::aufgabe Ejercicio 6 ★ FAC discreta
<span class="anker" id="aufg-6"></span>

<ol class="al">

<li>

Comprueba a mano la FAC de $(1,2,1)$.

</li>

<li>

Determina la FAC de $(1,-1)$. ¿Qué indica $\varphi(\pm1)<0$ sobre la señal?

</li>

</ol>

:::loesung
(a) $\varphi(0)=1+4+1=6$, $\varphi(\pm1)=1\cdot2+2\cdot1=4$, $\varphi(\pm2)=1\cdot1=1$.

(b) $\varphi(0)=2$, $\varphi(\pm1)=-1$. Un valor negativo con el desplazamiento 1 significa que los valores vecinos tienden a tener signos opuestos: la señal cambia rápidamente. En consonancia con ello, $|S_\mathrm a(f)|^2=|1-\mathrm{e}^{-\mathrm{j}2\pi f}|^2=2-2\cos(2\pi f)$ es nula en $f=0$ y máxima en $f=\frac12$: una señal paso alto.
:::
:::

:::aufgabe Ejercicio 7 ★★ FAC de un coseno
<span class="anker" id="aufg-7"></span>

Deduce la FAC de $A\cos(2\pi Ft+\varphi_0)$ con [(7.4)](#gl-7-4) sobre un periodo. ¿Por qué desaparece $\varphi_0$ y qué significa eso para la medida de la fase con la FAC?

:::loesung
Con $\omega=2\pi F$ y $\cos a\cos b=\frac12[\cos(a-b)+\cos(a+b)]$:

$$\frac1T\int_0^TA^2\cos(\omega t+\varphi_0)\cos(\omega t+\omega\tau+\varphi_0)\mathrm{d} t=\frac{A^2}{2}\cos(\omega\tau)+\frac{A^2}{2T}\int_0^T\cos(2\omega t+\omega\tau+2\varphi_0)\mathrm{d} t.$$

La segunda integral abarca dos periodos completos y es nula. La fase $\varphi_0$ solo desplaza el origen de tiempos, y el promedio sobre todos los instantes no conoce ningún origen. Por eso, con la FAC de una sola señal no se puede medir ninguna fase. En cambio, la diferencia de fase de *dos* señales sí la muestra la correlación cruzada.
:::
:::

:::kern Lo esencial
<ul>

<li>

$E_s=\int|s|^2\mathrm{d} t$; $L_s=\lim\frac{1}{2T}\int_{-T}^T|s|^2\mathrm{d} t$.

</li>

<li>

$p_{sg}=\frac{\int s^*g\,\mathrm{d} t}{\sqrt{E_sE_g}}$, $|p|\le1$, $p=0$: ortogonales.

</li>

<li>

$\varphi^E_{sg}(\tau)=\int s^*(t)g(t+\tau)\mathrm{d} t=s^*(-\tau)*g(\tau)$; $\varphi^E_{gs}(\tau)=\varphi^{E*}_{sg}(-\tau)$.

</li>

<li>

FAC: par (señal real), máximo $\varphi^E_{ss}(0)=E_s$, duración doble.

</li>

<li>

$\varphi^E_{ss}\leftrightarrow|S|^2$, $\varphi^E_{sg}\leftrightarrow S^*G$; Parseval $\int|s|^2\mathrm{d} t=\int|S|^2\mathrm{d} f$.

</li>

<li>

Wiener-Lee: $\varphi^E_{gg}=\varphi^E_{ss}*\varphi^E_{hh}$, $|G|^2=|S|^2|H|^2$; $\varphi^E_{sg}=\varphi^E_{ss}*h$.

</li>

<li>

Paso banda: $\varphi^E_{sgT}=\frac12s_T^*(-\tau)*g_T(\tau)$.

</li>

<li>

Discreto: $\varphi(m)=\sum s^*(n)g(n+m)$, $\leftrightarrow|S_\mathrm a|^2$; periódico: $S_d^*G_d$.

</li>

</ul>
:::

---
title: Señales aleatorias
pfad: Ingeniería eléctrica / 3.er semestre / Señales y sistemas / Señales aleatorias
order: 3270100
summary: Valores medios, distribuciones, densidad espectral de potencia, ruido en sistemas y el receptor óptimo
tags: función muestra, proceso aleatorio, variable aleatoria, valor esperado, función de autocorrelación, estacionario, ergódico, componente continua
lang: es
---

## De qué trata

El ruido de una resistencia, la voz, un flujo de datos: estas señales no se pueden predecir. No se conoce su evolución exacta, pero sí sus *propiedades en promedio*: qué tamaño tienen típicamente, con qué rapidez cambian, qué frecuencias contienen. Este artículo muestra cómo se describen estas señales aleatorias, qué hace con ellas un sistema LTI y cómo se reconoce con la mayor seguridad una señal conocida en medio del ruido.

:::merke La respuesta en tres frases (al final del artículo deberían resultar evidentes)
<ol>

<li>

Una señal aleatoria se describe mediante valores medios: valor medio, potencia, varianza, función de autocorrelación y densidad de probabilidad. En los procesos ergódicos pueden determinarse a partir de una única señal larga.

</li>

<li>

La transformada de Fourier de la función de autocorrelación es la densidad espectral de potencia. Un sistema LTI la multiplica por $|H(f)|^2$, exactamente igual que en las señales de energía ([parte 6](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen/korrelationsfunktionen.html)).

</li>

<li>

Frente al ruido blanco, el filtro adaptado $h(t)=s(T-t)$ es óptimo. Alcanza la relación señal-ruido $E_s/N_0$, independientemente de la forma de la señal.

</li>

</ol>
:::

**Un principio detrás de todos los resultados.** La señal desconocida se sustituye por sus valores medios, y para los valores medios rige la linealidad:

| Resultado | De dónde viene |
|---|---|
| Valor medio, potencia, varianza | media de conjunto y media temporal (etapas [1](#stufe-1)–[3](#stufe-3)) |
| FAC, covarianza, FCC | media de productos en dos instantes (etapa [4](#stufe-4)) |
| Densidad de probabilidad | fracción del tiempo o del conjunto por debajo de un umbral (etapa [5](#stufe-5)) |
| Suma de variables independientes | convolución de las densidades, de ahí Gauss (etapas [6](#stufe-6), [7](#stufe-7)) |
| Densidad espectral de potencia, Wiener-Lee | linealidad del valor medio en la integral de convolución (etapa [8](#stufe-8)) |
| Ruido blanco | densidad espectral de potencia constante, FAC $=N_0\delta$ (etapa [9](#stufe-9)) |
| Filtro adaptado | Cauchy-Schwarz: la correlación es máxima con la propia señal (etapa [10](#stufe-10)) |
| Probabilidad de error | área bajo una curva de Gauss más allá del umbral (etapa [11](#stufe-11)) |

**Cómo trabajar con este artículo.** Cada etapa tiene la idea, preguntas típicas con respuestas desplegables y ejercicios (de ★ a ★★★). Intenta resolverlos primero por tu cuenta; la solución se despliega justo debajo de cada ejercicio.

:::merke El modelo de referencia de este artículo
<ul>

<li>

⁠**Números aleatorios con distribución uniforme** entre $-\frac12$ y $\frac12$ (varianza $\frac{1}{12}$), también como ruido blanco en tiempo discreto.

</li>

<li>

⁠**Resistencia** $R=1\,\mathrm{k\Omega}$ a 290 K, ancho de banda de 20 kHz (audio).

</li>

<li>

⁠**Sistema recursivo** $g(n)=s(n)+0{,}6\,g(n-1)$ de la [parte 4](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme/abtastung-und-zeitdiskrete-systeme.html).

</li>

</ul>

El script `rechnung_kap7.py` recalcula los números, en parte como control con números aleatorios simulados.
:::

## Etapa 1: El proceso aleatorio

<span class="anker" id="stufe-1"></span>

:::zweck
¿Cómo se describe una señal cuya evolución no se conoce? Se imaginan muchas señales del mismo tipo y se promedia sobre ellas.
:::

**La idea.** Si se mide el ruido de muchas resistencias construidas de la misma manera y a la misma temperatura, se obtienen muchas curvas distintas ${}^ks(t)$, $k=1,2,\dots$ (fig. [1](#abb-1)). Cada una de ellas se llama __función muestra__ o realización. La totalidad imaginada de todas ellas se llama __proceso aleatorio__ $s(t)$. Los valores de todas las funciones muestra en un instante fijo $t_1$ forman una __variable aleatoria__ $s(t_1)$.

:::definition Definición 1.1 (Medias de conjunto)
<span class="anker" id="satz-1-1"></span>

<span class="anker" id="gl-1-1"></span>
<span class="anker" id="gl-1-2"></span>
$$\begin{aligned} \mathrm E\{s(t_1)\}&=\lim_{M\to\infty}\frac1M\sum_{k=1}^M{}^ks(t_1),\qquad \mathrm E\{F[s(t_1)]\}=\lim_{M\to\infty}\frac1M\sum_{k=1}^MF\bigl[{}^ks(t_1)\bigr],\\ \varphi_{ss}(t_1,t_2)&=\mathrm E\{s(t_1)\,s(t_2)\}. \end{aligned} \tag{1.1|1.2}$$
:::

⁠**Cómo leerlo:** $\mathrm E\{\cdot\}$ se llama __valor esperado__ (esperanza) o media de conjunto: se promedia sobre todas las funciones muestra en el mismo instante, es decir, en vertical en la fig. [1](#abb-1). Con $F[x]=x^2$ se obtiene el valor cuadrático medio. La __función de autocorrelación__ promedia el producto de los valores en dos instantes. Indica en qué medida el valor en $t_2$ está relacionado con el valor en $t_1$.

:::abbildung et3/k7schar
Tres funciones muestra de un proceso aleatorio (simuladas, valor medio 1). La media de conjunto se forma en vertical, sobre todas las funciones muestra en el mismo $t_1$ (rojo discontinuo). La media temporal se forma en horizontal, a lo largo de una función muestra.
:::

## Etapa 2: Estacionariedad y ergodicidad

<span class="anker" id="stufe-2"></span>

:::zweck
Nunca se dispone de un conjunto infinito; normalmente solo de una única señal. ¿Cuándo basta con ella?
:::

Un proceso se llama __estacionario__ si ninguno de sus valores medios cambia cuando todos los instantes de observación se desplazan un mismo tiempo $t_0$:

<span class="anker" id="gl-2-1"></span>
$$\mathrm E\{F[s(t_1)]\}=\mathrm E\{F[s(t_1+t_0)]\},\qquad\mathrm E\{F[s(t_1),s(t_2)]\}=\mathrm E\{F[s(t_1+t_0),s(t_2+t_0)]\}. \tag{2.1}$$

Entonces el valor medio $m_s=\mathrm E\{s(t)\}$ es una constante, y la FAC solo depende ya de la separación $\tau=t_2-t_1$: $\varphi_{ss}(\tau)=\mathrm E\{s(t)s(t+\tau)\}$. Un proceso estacionario se llama __ergódico__ si, además, toda media temporal de una función muestra es igual a la media de conjunto correspondiente:

<span class="anker" id="gl-2-2"></span>
$$\mathrm E\{F[s(t)]\}=\overline{F[{}^ks(t)]}=\lim_{T\to\infty}\frac{1}{2T}\int_{-T}^{T}F\bigl[{}^ks(t)\bigr]\,\mathrm{d} t\quad\text{para todo }k. \tag{2.2}$$

⁠**Cómo leerlo:** estacionario significa que la estadística no cambia con el tiempo. Ergódico significa que una única función muestra, observada durante mucho tiempo, muestra a lo largo del tiempo todo lo que muestra el conjunto entero. El ruido de una resistencia a temperatura constante es ergódico. Solo por eso se puede caracterizar el ruido con un único instrumento de medida.

:::frage ¿Todo proceso estacionario es también ergódico?
No. Ejemplo: cada función muestra es una constante cuyo valor se sortea una sola vez, ${}^ks(t)=c_k$. El proceso es estacionario, porque nada depende de $t$. Pero la media temporal de una función muestra es $c_k$, distinta para cada función muestra, y no la media de conjunto. Una función muestra aislada nunca «ve» los demás valores.
:::

## Etapa 3: Valor medio, potencia, varianza

<span class="anker" id="stufe-3"></span>

:::zweck
Los valores medios de primer orden más importantes y su significado intuitivo.
:::

El valor esperado es lineal: $\mathrm E\{\sum_ia_is_i\}=\sum_ia_i\mathrm E\{s_i\}$, para variables aleatorias cualesquiera. En los procesos estacionarios se define:

<span class="anker" id="gl-3-1"></span>
$$m_s=\mathrm E\{s(t)\},\qquad L_s=\mathrm E\{s^2(t)\},\qquad\sigma_s^2=L_s-m_s^2. \tag{3.1}$$

⁠**Cómo leerlo:** en un proceso ergódico, $m_s$ es la media temporal, es decir, la __componente continua__ de la señal, y $L_s$ es el valor cuadrático medio temporal, la __potencia__ ([parte 6](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen/korrelationsfunktionen.html)). La __varianza__ $\sigma_s^2$ es la potencia menos la potencia de la componente continua, es decir, la __potencia alterna__. Su raíz, la __desviación típica__ $\sigma_s$, es el valor eficaz de la componente alterna. Un multímetro en modo AC muestra $\sigma_s$; en modo DC, $m_s$.

:::aufgabe Ejercicio 1 ★ Valores medios de una señal
<span class="anker" id="aufg-1"></span>

Una señal ergódica tiene una componente continua de 2 V y un valor eficaz (todo junto, «true RMS») de 2,5 V. ¿Cuánto valen la potencia normalizada, la varianza y la desviación típica?

:::loesung
$L_s=2{,}5^2=6{,}25$ V$^2$, $\sigma_s^2=L_s-m_s^2=6{,}25-4=2{,}25$ V$^2$, $\sigma_s=1{,}5$ V. Un instrumento de medida en modo AC muestra 1,5 V.
:::
:::

## Etapa 4: Autocorrelación, covarianza y correlación cruzada

<span class="anker" id="stufe-4"></span>

:::zweck
¿Con qué rapidez cambia una señal aleatoria? Lo dice la FAC: cuánto se parece todavía la señal a sí misma al cabo del tiempo $\tau$.
:::

:::satz Teorema 4.1 (Propiedades de la FAC de procesos estacionarios)
<span class="anker" id="satz-4-1"></span>

<span class="anker" id="gl-4-1"></span>
$$\varphi_{ss}(0)=L_s,\qquad\varphi_{ss}(\tau)=\varphi_{ss}(-\tau),\qquad|\varphi_{ss}(\tau)|\le\varphi_{ss}(0). \tag{4.1}$$

Para procesos ergódicos, $\varphi_{ss}(\tau)=\overline{s(t)s(t+\tau)}$, es decir, la FAC de una señal de potencia de la [parte 6](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen/korrelationsfunktionen.html).
:::

:::herleitung máximo en $\tau=0$
$\mathrm E\{[s(t)\pm s(t+\tau)]^2\}\ge0$, porque el valor esperado de un cuadrado nunca es negativo. Desarrollando y aplicando la linealidad: $\mathrm E\{s^2(t)\}+\mathrm E\{s^2(t+\tau)\}\pm2\mathrm E\{s(t)s(t+\tau)\}\ge0$; por tanto, $2\varphi_{ss}(0)\pm2\varphi_{ss}(\tau)\ge0$. Paridad: $t\to t-\tau$ en la definición.
:::

**Covarianza.** Si antes se resta el valor medio, se obtiene la __función de autocovarianza__

<span class="anker" id="gl-4-2"></span>
$$\mu_{ss}(\tau)=\mathrm E\{[s(t)-m_s][s(t+\tau)-m_s]\}=\varphi_{ss}(\tau)-m_s^2,\qquad\mu_{ss}(0)=\sigma_s^2. \tag{4.2}$$

Si el proceso no contiene componentes periódicas, los valores muy separados se vuelven independientes: $\varphi_{ss}(\tau)\to m_s^2$ y $\mu_{ss}(\tau)\to0$ para $\tau\to\infty$.

**Correlación cruzada y sumas.** Para dos procesos, $\varphi_{uv}(\tau)=\mathrm E\{u(t)v(t+\tau)\}$, con $\varphi_{vu}(\tau)=\varphi_{uv}(-\tau)$, y la covarianza cruzada es $\mu_{uv}(\tau)=\varphi_{uv}(\tau)-m_um_v$. Para la suma $s=u+v$, desarrollando el producto se obtiene

<span class="anker" id="gl-4-3"></span>
$$\varphi_{ss}(\tau)=\varphi_{uu}+\varphi_{uv}+\varphi_{vu}+\varphi_{vv},\qquad L_s=L_u+L_v+2\varphi_{uv}(0),\qquad\sigma_s^2=\sigma_u^2+\sigma_v^2+2\mu_{uv}(0). \tag{4.3}$$

⁠**En resumen:** las potencias solo se suman si las señales están incorreladas. Si no, se añade el término cruzado. Dos señales iguales dan el cuádruple de la potencia; dos señales opuestas, potencia nula.

:::aufgabe Ejercicio 2 ★★ Dos fuentes de ruido
<span class="anker" id="aufg-2"></span>

Se suman dos tensiones de ruido de media nula con valores eficaces de 3 mV y 4 mV. ¿Cuánto vale el valor eficaz de la suma si (a) están incorreladas, (b) tienen la misma forma ($\varphi_{uv}(0)=\sigma_u\sigma_v$), (c) tienen la misma forma con el signo invertido ($\varphi_{uv}(0)=-\sigma_u\sigma_v$)?

:::loesung
(a) $\sigma=\sqrt{9+16}=5$ mV. (b) $\sigma^2=9+16+2\cdot12=49$, es decir, 7 mV: las amplitudes se suman. (c) $\sigma^2=9+16-24=1$, es decir, 1 mV: las señales casi se cancelan.
:::
:::

## Etapa 5: Función de distribución y densidad de probabilidad

<span class="anker" id="stufe-5"></span>

:::zweck
Los valores medios no lo dicen todo. ¿Con qué frecuencia toma una señal cada valor? Eso lo describe la distribución.
:::

:::definition Definición 5.1 (Distribución)
<span class="anker" id="satz-5-1"></span>

<span class="anker" id="gl-5-1"></span>
$$P_s(x)=\mathrm{Prob}[s(t)\le x],\qquad p_s(x)=\frac{\mathrm{d} P_s(x)}{\mathrm{d} x},\qquad P_s(x)=\int_{-\infty}^xp_s(\xi)\,\mathrm{d}\xi. \tag{5.1}$$
:::

⁠**Cómo leerlo:** la __función de distribución__ $P_s(x)$ es la fracción del conjunto (en los procesos ergódicos, la fracción del tiempo) en la que la señal está por debajo del umbral $x$. Crece de forma monótona desde $P_s(-\infty)=0$ hasta $P_s(\infty)=1$. La __densidad de probabilidad__ $p_s(x)$ nunca es negativa, tiene área 1, y $p_s(x)\,\mathrm{d} x$ es la probabilidad de que la señal esté entre $x$ y $x+\mathrm{d} x$. De ahí se obtienen todos los valores medios de primer orden:

<span class="anker" id="gl-5-2"></span>
$$m_s=\int x\,p_s(x)\,\mathrm{d} x,\qquad L_s=\int x^2p_s(x)\,\mathrm{d} x,\qquad\mathrm E\{F[s]\}=\int F(x)\,p_s(x)\,\mathrm{d} x. \tag{5.2}$$

**Ejemplo: distribución uniforme.** Todos los valores de un intervalo de anchura $a$ en torno a $m_s$ son igual de probables: $p_s(x)=\frac1a\operatorname{rect}\bigl(\frac{x-m_s}{a}\bigr)$. Entonces

$$L_s=\frac1a\int_{m_s-a/2}^{m_s+a/2}x^2\mathrm{d} x=\frac{a^2}{12}+m_s^2,\qquad\sigma_s^2=\frac{a^2}{12}.$$

Los números aleatorios del modelo de referencia ($a=1$, $m_s=0$) tienen la varianza $\frac1{12}=0{,}0833$.

**Características.** Si una señal pasa por una característica $y=k(x)$ (amplificador con saturación, rectificador, cuantizador), su distribución cambia. Con una característica monótona, la probabilidad de cada intervalo se conserva:

<span class="anker" id="gl-5-3"></span>
$$p_g(y)\,|\mathrm{d} y|=p_s(x)\,|\mathrm{d} x|\qquad\Longrightarrow\qquad p_g(y)=\frac{p_s(x)}{|k'(x)|},\qquad P_g\bigl(k(x)\bigr)=P_s(x)\ \ (k\text{ creciente}). \tag{5.3}$$

Donde la característica es empinada, los valores se reparten sobre un rango amplio y la densidad disminuye. Con esta regla, cualquier distribución puede transformarse en otra deseada. Ejemplo: $k(x)=(2|x|-x^2)\operatorname{sgn}x$ convierte una distribución triangular en $[-1,1]$ en una distribución uniforme (ejercicio [4](#aufg-4)).

**Cuantización.** Un __cuantizador__ sustituye cada valor por el más cercano de $M$ niveles. Con niveles uniformes de anchura $\Delta$ y sin saturación, el error está distribuido de forma aproximadamente uniforme entre $-\frac\Delta2$ y $\frac\Delta2$; tiene, por tanto, la varianza $\frac{\Delta^2}{12}$. Para una señal con distribución uniforme sobre los $M$ niveles (varianza $\frac{(M\Delta)^2}{12}$), la relación señal-ruido es $M^2$, en decibelios $20\lg M\approx6\,\text{dB por bit}$: 48 dB con 8 bits, 96 dB con 16 bits.

:::aufgabe Ejercicio 3 ★ Distribución uniforme
<span class="anker" id="aufg-3"></span>

Una señal tiene distribución uniforme entre 1 V y 3 V. Calcula $m_s$, $L_s$, $\sigma_s^2$ y la probabilidad de que esté por encima de 2,5 V.

:::loesung
$a=2$ V, $m_s=2$ V. $\sigma_s^2=\frac{a^2}{12}=\frac13$ V$^2$, $L_s=\frac13+4=4{,}33$ V$^2$. Por encima de 2,5 V queda una cuarta parte del intervalo; por tanto, $\mathrm{Prob}=\frac{0{,}5}{2}=0{,}25$.
:::
:::

:::aufgabe Ejercicio 4 ★★ Transformar distribuciones
<span class="anker" id="aufg-4"></span>

Una señal tiene la densidad triangular $p_s(x)=\Lambda(x)$ en $[-1,1]$.

<ol class="al">

<li>

Determina $P_s(x)$ para $0\le x\le1$.

</li>

<li>

Demuestra con [(5.3)](#gl-5-3) que $k(x)=(2x-x^2)$ para $x\ge0$ (y prolongada de forma impar) genera una distribución uniforme en $[-1,1]$. Pista: para la distribución uniforme, $P_g(y)=\frac12+\frac y2$.

</li>

</ol>

:::loesung
(a) $P_s(x)=\frac12+\int_0^x(1-\xi)\,\mathrm{d}\xi=\frac12+x-\frac{x^2}{2}$ para $0\le x\le1$.

(b) Según [(5.3)](#gl-5-3), tiene que cumplirse $P_g(k(x))=P_s(x)$, es decir, $\frac12+\frac{k(x)}{2}=\frac12+x-\frac{x^2}{2}$. De ahí resulta $k(x)=2x-x^2$. La característica es empinada en $x=0$ (pendiente 2), donde la densidad triangular es máxima, y plana en el borde. Así, los valores frecuentes se separan y los poco frecuentes se juntan. Una simulación da un histograma plano de altura 0,5.
:::
:::

:::aufgabe Ejercicio 4a ★★★ (Para profundizar) El cuantizador óptimo
<span class="anker" id="aufg-4a"></span>

Un cuantizador con los umbrales $u_i$ y los valores de nivel $v_i$ (el nivel $i$ rige para $u_i<x\le u_{i+1}$) tiene el error cuadrático medio $N_q=\sum_i\int_{u_i}^{u_{i+1}}(v_i-x)^2p_s(x)\,\mathrm{d} x$.

<ol class="al">

<li>

Demuestra derivando respecto a $v_i$: en el óptimo, $v_i$ está en el centro de gravedad de la densidad sobre su intervalo.

</li>

<li>

Demuestra derivando respecto a $u_i$: en el óptimo, $u_i$ está justo en el punto medio entre $v_{i-1}$ y $v_i$.

</li>

<li>

¿Por qué, para una señal con distribución uniforme, el cuantizador uniforme es óptimo?

</li>

</ol>

:::loesung
(a) $\frac{\partial N_q}{\partial v_i}=\int_{u_i}^{u_{i+1}}2(v_i-x)p_s(x)\mathrm{d} x=0$; por tanto, $v_i=\dfrac{\int_{u_i}^{u_{i+1}}x\,p_s\,\mathrm{d} x}{\int_{u_i}^{u_{i+1}}p_s\,\mathrm{d} x}$, el centro de gravedad.

(b) $u_i$ aparece como límite superior del intervalo $i-1$ y como límite inferior del intervalo $i$: $\frac{\partial N_q}{\partial u_i}=(v_{i-1}-u_i)^2p_s(u_i)-(v_i-u_i)^2p_s(u_i)=0$; por tanto, $u_i=\frac12(v_{i-1}+v_i)$. Cada valor se asigna al nivel cuyo valor de nivel está más cerca.

(c) Con densidad constante, el centro de gravedad de cada intervalo es su punto medio. Intervalos de igual anchura con sus puntos medios como valores de nivel cumplen ambas condiciones, con la anchura de nivel $\Delta=a/M$.
:::
:::

## Etapa 6: Distribución conjunta, independencia, incorrelación

<span class="anker" id="stufe-6"></span>

:::zweck
Dos variables aleatorias a la vez: ¿cuándo están relacionadas y qué se deduce de ello para su suma?
:::

La __distribución conjunta__ de dos variables es $P_{sg}(x,y)=\mathrm{Prob}[s\le x\ \text{y}\ g\le y]$, y su densidad, $p_{sg}=\frac{\partial^2P_{sg}}{\partial x\,\partial y}$. De ella se obtienen las distribuciones individuales ($P_{sg}(x,\infty)=P_s(x)$) y la correlación $\varphi_{sg}=\iint xy\,p_{sg}(x,y)\,\mathrm{d} x\,\mathrm{d} y$. En procesos conjuntamente estacionarios, todo depende solo del desplazamiento temporal $\tau$ entre $s(t)$ y $g(t+\tau)$.

:::definition Definición 6.1 (Independientes, incorreladas)
<span class="anker" id="satz-6-1"></span>

$s$ y $g$ son __estadísticamente independientes__ si $p_{sg}(x,y)=p_s(x)\,p_g(y)$. Son __incorreladas__ si $\mu_{sg}=\varphi_{sg}-m_sm_g=0$.
:::

De la independencia se deduce la incorrelación: $\varphi_{sg}=\int xp_s\mathrm{d} x\cdot\int yp_g\mathrm{d} y=m_sm_g$. Al revés, no: incorreladas solo significa que no existe una relación *lineal* (ejercicio [5](#aufg-5)).

**La suma de dos variables independientes.** La suma $s=f+g$ toma el valor $x$ cuando $f=u$ y $g=x-u$, para algún $u$:

<span class="anker" id="gl-6-1"></span>
$$p_s(x)=\int_{-\infty}^{\infty}p_{fg}(u,x-u)\,\mathrm{d} u=p_f(x)*p_g(x)\quad(\text{independientes}). \tag{6.1}$$

Es la convolución de la [parte 1](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html), allí con el ejemplo de los dados. Dos variables con distribución uniforme dan una densidad triangular; tres, una que ya tiene casi forma de campana (fig. [2](#abb-2)).

:::abbildung et3/k7summen
Densidades de probabilidad de sumas de variables aleatorias independientes con distribución uniforme en $[-\frac12,\frac12]$. La suma de tres ya está cerca de la curva de Gauss con la misma varianza (en $x=0$: 0,75 frente a 0,80).
:::

:::aufgabe Ejercicio 5 ★★ Incorreladas, pero dependientes
<span class="anker" id="aufg-5"></span>

$s$ tiene distribución uniforme en $[-1,1]$ y $g=s^2$. Demuestra que $s$ y $g$ están incorreladas, aunque $g$ está completamente determinada por $s$.

:::loesung
$m_s=0$ y $\mathrm E\{sg\}=\mathrm E\{s^3\}=\frac12\int_{-1}^1x^3\mathrm{d} x=0$; por tanto, $\mu_{sg}=0-0\cdot m_g=0$: incorreladas. Aun así, $s$ fija el valor de $g$. La relación es cuadrática, y una correlación solo capta relaciones lineales: para $s$ positivo, $g$ crece con $s$; para $s$ negativo, decrece; en promedio, ambas tendencias se compensan.
:::
:::

## Etapa 7: La distribución gaussiana

<span class="anker" id="stufe-7"></span>

:::zweck
¿Por qué el ruido tiene tan a menudo una distribución gaussiana y cómo se calcula con ella?
:::

Si se convolucionan muchas densidades entre sí, el resultado se aproxima a una curva de Gauss (__teorema central del límite__, [parte 3](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)). El ruido es casi siempre la suma de muchísimas contribuciones pequeñas e independientes, por ejemplo de los movimientos de muchos electrones. Por eso tiene una distribución gaussiana.

:::satz Teorema 7.1 (Distribución gaussiana)
<span class="anker" id="satz-7-1"></span>

<span class="anker" id="gl-7-1"></span>
$$p_s(x)=\frac{1}{\sqrt{2\pi\sigma_s^2}}\,\mathrm{e}^{-(x-m_s)^2/(2\sigma_s^2)},\qquad P_s(x)=\frac12+\frac12\operatorname{erf}\Bigl(\frac{x-m_s}{\sqrt{2\sigma_s^2}}\Bigr)=\frac12\operatorname{erfc}\Bigl(\frac{m_s-x}{\sqrt{2\sigma_s^2}}\Bigr) \tag{7.1}$$

con la __función de error__ $\operatorname{erf}(x)=\frac{2}{\sqrt\pi}\int_0^x\mathrm{e}^{-\xi^2}\mathrm{d}\xi$ y $\operatorname{erfc}=1-\operatorname{erf}$.
:::

⁠**Cómo leerlo:** el valor medio y la varianza determinan por completo la distribución gaussiana (o normal). Dentro de $\pm\sigma_s$ en torno al valor medio está el 68,3 % de los valores; dentro de $\pm2\sigma_s$, el 95,4 %; dentro de $\pm3\sigma_s$, el 99,73 %. La integral de la curva de Gauss no tiene forma cerrada; de ahí la función erf, que se tabula o se calcula numéricamente. Para $x$ grande, $\operatorname{erfc}(x)\approx\frac{\mathrm{e}^{-x^2}}{\sqrt\pi\,x}$.

**Reglas de cálculo.** La suma de dos variables gaussianas independientes es gaussiana con $m_s=m_1+m_2$ y $\sigma_s^2=\sigma_1^2+\sigma_2^2$. Un proceso gaussiano sigue siendo gaussiano tras un sistema LTI, porque la integral de convolución es una suma ponderada (infinita). Y para dos variables conjuntamente gaussianas, «incorreladas» es lo mismo que «independientes»: si la covarianza cruzada normalizada $\rho=\mu_{sg}/(\sigma_s\sigma_g)$ es nula, la densidad conjunta se descompone en un producto.

:::zusatz la densidad gaussiana bidimensional
Para $s,g$ de media nula y conjuntamente gaussianas con el coeficiente de correlación $\rho$:

$$p_{sg}(x,y)=\frac{1}{2\pi\sigma_s\sigma_g\sqrt{1-\rho^2}}\exp\Bigl(-\frac{\sigma_g^2x^2+\sigma_s^2y^2-2\rho\sigma_s\sigma_gxy}{2\sigma_s^2\sigma_g^2(1-\rho^2)}\Bigr).$$

Se obtiene a través de las variables normalizadas suma y diferencia $\frac{s}{\sigma_s}\pm\frac{g}{\sigma_g}$: están incorreladas, tienen las varianzas $2(1\pm\rho)$ y, al ser gaussianas, son independientes. Las líneas de igual densidad son elipses. En las coordenadas normalizadas $x/\sigma_s$, $y/\sigma_g$, sus ejes siguen la dirección de estas sumas y diferencias. Para $\rho=0$ se convierten en circunferencias (si $\sigma_s=\sigma_g$), y la densidad es el producto de las densidades individuales.
:::

:::aufgabe Ejercicio 6 ★ Calcular con la distribución gaussiana
<span class="anker" id="aufg-6"></span>

Una tensión de ruido tiene distribución gaussiana con $m=0$ y $\sigma=1$ mV.

<ol class="al">

<li>

¿Con qué probabilidad es mayor que 2 mV? (Pista: $\operatorname{erfc}(1{,}414)=0{,}0455$.)

</li>

<li>

Se suman dos de estas tensiones, independientes. ¿Qué distribución tiene la suma?

</li>

</ol>

:::loesung
(a) $\mathrm{Prob}[x>2\,\mathrm{mV}]=\frac12\operatorname{erfc}\bigl(\frac{2}{\sqrt2}\bigr)=\frac12\operatorname{erfc}(1{,}414)=0{,}023$, es decir, el 2,3 %.

(b) Gaussiana con $m=0$ y $\sigma^2=2$ mV$^2$, $\sigma=1{,}41$ mV.
:::
:::

## Etapa 8: Señal aleatoria y sistema LTI, densidad espectral

<span class="anker" id="stufe-8"></span>

:::zweck
¿Qué hace un sistema LTI con una señal aleatoria? Cada función muestra se convoluciona. Por eso, para los valores medios rigen reglas sencillas.
:::

**Valor medio.** Para cada función muestra, ${}^kg={}^ks*h$. El valor esperado es lineal y puede entrar en la integral de convolución:

<span class="anker" id="gl-8-1"></span>
$$m_g=\mathrm E\Bigl\{\int s(\tau)h(t-\tau)\mathrm{d}\tau\Bigr\}=\int\mathrm E\{s(\tau)\}\,h(t-\tau)\,\mathrm{d}\tau=m_s\int h\,\mathrm{d}\tau=m_s\,H(0). \tag{8.1}$$

El valor medio se transmite como una componente continua.

:::satz Teorema 8.1 (Wiener-Lee para procesos estacionarios)
<span class="anker" id="satz-8-1"></span>

<span class="anker" id="gl-8-2"></span>
$$\varphi_{gg}(\tau)=\varphi_{ss}(\tau)*\varphi^E_{hh}(\tau),\qquad\Phi_{gg}(f)=\Phi_{ss}(f)\,|H(f)|^2, \tag{8.2}$$

con la FAC de energía $\varphi^E_{hh}(\tau)=\int h(\vartheta)h(\vartheta+\tau)\mathrm{d}\vartheta$ de la respuesta al impulso y la __densidad espectral de potencia__ $\Phi_{ss}(f)\;\bullet\!\!-\!\!\circ\;\varphi_{ss}(\tau)$. La potencia es

<span class="anker" id="gl-8-3"></span>
$$L_s=\varphi_{ss}(0)=\int_{-\infty}^{\infty}\Phi_{ss}(f)\,\mathrm{d} f. \tag{8.3}$$
:::

:::herleitung Wiener-Lee
Escribir las dos integrales de convolución, con variables distintas:

$$g(t)g(t+\tau)=\iint s(t-\alpha)\,s(t+\tau-\beta)\,h(\alpha)h(\beta)\,\mathrm{d}\alpha\,\mathrm{d}\beta.$$

Llevar el valor esperado dentro de la integral doble. Por la estacionariedad, $\mathrm E\{s(t-\alpha)s(t+\tau-\beta)\}=\varphi_{ss}(\tau-\beta+\alpha)$. Con $\vartheta=\beta-\alpha$:

$$\varphi_{gg}(\tau)=\int\varphi_{ss}(\tau-\vartheta)\underbrace{\int h(\alpha)h(\alpha+\vartheta)\,\mathrm{d}\alpha}_{\varphi^E_{hh}(\vartheta)}\,\mathrm{d}\vartheta=\varphi_{ss}*\varphi^E_{hh}.$$

En el dominio de la frecuencia, $\varphi^E_{hh}$ se convierte en $|H|^2$ ([parte 6](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen/korrelationsfunktionen.html)).
:::

⁠**Cómo leerlo:** $\Phi_{ss}(f)$ indica cómo se reparte la potencia entre las frecuencias. Es real, nunca negativa y, en las señales reales, par. Un sistema LTI multiplica la potencia en cada frecuencia por $|H(f)|^2$; su fase no influye. Es la misma regla que para las señales de energía de la [parte 6](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen/korrelationsfunktionen.html), ahora para procesos. (Complemento: en sentido estricto, $\Phi_{ss}$ se define como el límite $\lim_{T\to\infty}\frac1T\mathrm E\{|S_T(f)|^2\}$ de espectros de tiempo corto de fragmentos de duración $T$. Que esto sea lo mismo que la transformada de la FAC es la afirmación propiamente dicha del teorema de Wiener-Khinchin.)

:::ltspice Ruido con valor medio a través de un paso bajo y un paso alto
⁠**Esquema:** fuente de comportamiento `bv` en el nodo `s` con `V=1+white(1e3*time)`. `white(x)` da valores aleatorios entre $-0{,}5$ y $0{,}5$, uno nuevo en cada $x$ entero, unidos de forma suave; aquí, por tanto, uno cada milisegundo. Conectados en paralelo a ella, un paso bajo RC (`res` con `1Meg` hacia `tp`, `cap` con `1u` a masa) y un paso alto CR (`cap` con `1u` hacia `hp`, `res` con `1Meg` a masa).

⁠**Directiva:** `.tran 0 200 0 0.1m`.

⁠**Lectura:** amplía la vista de 20 s a 200 s, es decir, al tiempo posterior al transitorio. Un clic con la tecla Ctrl pulsada sobre el nombre de una curva muestra el valor medio (Average) y el valor eficaz (RMS) en el intervalo visible.

⁠**Lo que ves:** la entrada tiene el valor medio 1 V. Compara los valores medios de `V(tp)` y `V(hp)` con tu resultado del ejercicio [7](#aufg-7). Las fluctuaciones son mucho menores en el paso bajo: haz que se dibujen `V(s)-1` y `V(tp)-1`; sus valores eficaces son de aproximadamente 0,25 y 0,01. De la ancha densidad espectral de potencia, el paso bajo solo deja pasar aproximadamente la parte por debajo de $1/(2\pi RC)=0{,}16$ Hz, y según [(8.3)](#gl-8-3) la potencia es el área bajo la densidad espectral de potencia.
:::

:::aufgabe Ejercicio 7 ★ Valor medio a través de un filtro
<span class="anker" id="aufg-7"></span>

Un ruido con un valor medio de 1 V pasa por un paso bajo RC y por un paso alto CR. ¿Qué valores medios tienen las salidas y por qué?

:::loesung
Paso bajo RC: $H(0)=1$, valor medio 1 V. Paso alto CR: $H(0)=0$, valor medio 0. El condensador no deja pasar la corriente continua; la componente continua queda bloqueada.
:::
:::

## Etapa 9: Ruido blanco y ruido térmico

<span class="anker" id="stufe-9"></span>

:::zweck
El modelo más importante de las perturbaciones: ruido con la misma densidad espectral de potencia en todas las frecuencias.
:::

:::definition Definición 9.1 (Ruido blanco)
<span class="anker" id="satz-9-1"></span>

Un proceso de media nula con $\Phi_{ss}(f)=N_0$ para todo $f$ se llama __ruido blanco__. Su FAC es $\varphi_{ss}(\tau)=N_0\,\delta(\tau)$.
:::

⁠**Cómo leerlo:** los valores en instantes distintos están incorrelados, por muy próximos que estén. La potencia $\int N_0\mathrm{d} f$ es infinita: el ruido blanco es un modelo límite, como el impulso de Dirac. Lo que se mide en realidad es siempre ruido filtrado, «coloreado»:

<span class="anker" id="gl-9-1"></span>
$$\Phi_{gg}(f)=N_0|H(f)|^2,\qquad\varphi_{gg}(\tau)=N_0\,\varphi^E_{hh}(\tau),\qquad L_g=N_0\int|h(t)|^2\mathrm{d} t=N_0\int|H(f)|^2\mathrm{d} f. \tag{9.1}$$

Tras un paso bajo ideal con $f_\mathrm g$: $L_g=2N_0f_\mathrm g$ y $\varphi_{gg}(\tau)=2N_0f_\mathrm g\operatorname{si}(2\pi f_\mathrm g\tau)$ (fig. [3](#abb-3)). La FAC es nula en los puntos $\tau=k/(2f_\mathrm g)$, $k\neq0$: las muestras separadas según la tasa de Nyquist están incorreladas.

:::abbildung et3/k7tp
FAC del ruido blanco tras un paso bajo ideal: $2N_0f_\mathrm g\operatorname{si}(2\pi f_\mathrm g\tau)$. En $\tau=0$, la potencia $2N_0f_\mathrm g$. En los puntos rojos ($\tau=k/(2f_\mathrm g)$) es nula.
:::

**Ruido térmico.** El movimiento térmico de los electrones genera en toda resistencia $R$ una tensión de ruido. En circuito abierto, medida en el rango de frecuencias $|f|\le f_\mathrm g$:

<span class="anker" id="gl-9-2"></span>
$$\mathrm E\{u^2\}=4kT_\mathrm{abs}Rf_\mathrm g,\qquad N_0=2kT_\mathrm{abs}R,\qquad L_{\max}=kT_\mathrm{abs}f_\mathrm g, \tag{9.2}$$

con la constante de Boltzmann $k=1{,}38\cdot10^{-23}$ W s/K. A temperatura ambiente (290 K), $kT\approx4\cdot10^{-21}$ W/Hz, es decir, 4 pW por GHz de ancho de banda. $L_{\max}$ es la potencia máxima que puede extraerse de la resistencia con adaptación de potencia. En el modelo de referencia ($1\,\mathrm{k\Omega}$, 20 kHz), el valor eficaz es $\sqrt{\mathrm E\{u^2\}}=0{,}57$ µ V. Este orden de magnitud limita la sensibilidad que puede tener un amplificador de micrófono. El espectro es plano hasta aproximadamente $10^{12}$ Hz.

:::ltspice Medir el ruido térmico
LTspice asigna a cada resistencia su ruido térmico. El análisis `.noise` calcula en un nodo la densidad de ruido `V(onoise)` en V$/\sqrt{\mathrm{Hz}}$. La medida `.meas noise urms INTEG V(onoise)` la integra cuadráticamente sobre el rango de frecuencias del análisis, como en [(8.3)](#gl-8-3), y da el valor eficaz. `.temp 16.85` ajusta 290 K.

⁠**Resistencia:** `res` con `{Rx}` del nodo `a` a masa y, en paralelo, una fuente `current` con el valor 0 (nombre `I1`). No carga nada; `.noise` solo la necesita como fuente de referencia. Directivas `.param Rx=1k` y `.noise V(a) I1 lin 20001 1 20k`. Resultado: 4,0 nV$/\sqrt{\mathrm{Hz}}$ y `urms` $=0{,}57$ µ V, como arriba. Pon `Rx=1Meg` y compara con tu resultado del ejercicio [8](#aufg-8).

⁠**$kT/C$:** fuente `voltage` `V1` con el valor 0 y `AC 1`, `res` con `{Rx}` hacia `out`, `cap` con `1p` a masa. Directivas `.step param Rx list 1k 1Meg` y `.noise V(out) V1 dec 200 1 1T` y, de nuevo, `.temp 16.85` y la medida `urms`. `urms` es igual para ambas resistencias. Compara el valor con tu resultado del ejercicio [9](#aufg-9)(b).
:::

:::aufgabe Ejercicio 8 ★ Ruido de una resistencia
<span class="anker" id="aufg-8"></span>

Calcula el valor eficaz del ruido de una resistencia de $1\,\mathrm{M\Omega}$ a 290 K y con 20 kHz de ancho de banda. ¿En qué factor es mayor que en la resistencia de $1\,\mathrm{k\Omega}$ y por qué precisamente en ese?

:::loesung
El valor eficaz crece con $\sqrt R$: es $\sqrt{1000}=31{,}6$ veces mayor, es decir, $0{,}566\cdot31{,}6=17{,}9$ µ V.
:::
:::

:::aufgabe Ejercicio 9 ★★ El ruido $kT/C$
<span class="anker" id="aufg-9"></span>

El ruido térmico de la resistencia ($N_0=2kTR$) pasa por el circuito RC que forma con un condensador $C$ ($h(t)=\frac{1}{RC}\mathrm{e}^{-t/RC}\varepsilon(t)$).

<ol class="al">

<li>

Demuestra con [(9.1)](#gl-9-1) que la potencia de ruido en el condensador es $kT/C$, independientemente de $R$.

</li>

<li>

¿Cuánto vale el valor eficaz con $C=1$ pF y 290 K? ¿Por qué aquí no ayuda una resistencia más pequeña?

</li>

</ol>

:::loesung
(a) $\int h^2\mathrm{d} t=\frac{1}{(RC)^2}\int_0^\infty\mathrm{e}^{-2t/RC}\mathrm{d} t=\frac{1}{2RC}$. Por tanto, $L=N_0\cdot\frac{1}{2RC}=\frac{2kTR}{2RC}=\frac{kT}{C}$.

(b) $\sqrt{4\cdot10^{-21}/10^{-12}}\,\mathrm{V}=\sqrt{4\cdot10^{-9}}\,\mathrm{V}=63$ µ V. Una resistencia más pequeña genera, es cierto, menos ruido por hercio, pero el circuito RC se vuelve de banda más ancha ($1/RC$ mayor). Ambos efectos se compensan exactamente. Solo un condensador mayor reduce el ruido.
:::
:::

## Etapa 10: El filtro adaptado (matched filter)

<span class="anker" id="stufe-10"></span>

:::zweck
Un pulso conocido $s(t)$ llega con ruido. ¿Con qué filtro se hace más visible en el instante de muestreo $T$?
:::

**El planteamiento.** A la entrada del receptor llega $s(t)+n(t)$, con ruido blanco $n$. Un filtro $h$ entrega $y=g+n_e$, con la componente útil $g=s*h$ y la componente de ruido $n_e=n*h$. Se muestrea en $T$. La relación señal-ruido en ese instante es

$$\frac{S_a}{N}=\frac{g^2(T)}{\mathrm E\{n_e^2(T)\}}=\frac{\bigl[\int h(\tau)s(T-\tau)\mathrm{d}\tau\bigr]^2}{N_0\int|h(\tau)|^2\mathrm{d}\tau}=\frac{E_s}{N_0}\cdot\underbrace{\frac{\bigl[\int h(\tau)s(T-\tau)\mathrm{d}\tau\bigr]^2}{\int|h|^2\mathrm{d}\tau\int|s(T-\tau)|^2\mathrm{d}\tau}}_{=|p|^2\le1}.$$

La fracción de la derecha es el cuadrado de un coeficiente de correlación ([parte 6](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen/korrelationsfunktionen.html)), entre $h(\tau)$ y $s(T-\tau)$. Vale como máximo 1, y lo alcanza exactamente cuando ambas tienen la misma forma.

:::satz Teorema 10.1 (Filtro adaptado)
<span class="anker" id="satz-10-1"></span>

Frente al ruido blanco, la mejor relación señal-ruido alcanzable es

<span class="anker" id="gl-10-1"></span>
$$\Bigl(\frac{S_a}{N}\Bigr)_{\max}=\frac{E_s}{N_0},\qquad\text{alcanzada con}\qquad h(t)=a\,s(T-t),\quad H(f)=a\,S^*(f)\,\mathrm{e}^{-\mathrm{j}2\pi fT}. \tag{10.1}$$
:::

⁠**Cómo leerlo:** la mejor respuesta al impulso es la propia señal reflejada en el tiempo y desplazada $T$: el __filtro adaptado__ (también filtro de correlación, en inglés *matched filter*). Su salida sin ruido es $g(t)=a\,\varphi^E_{ss}(t-T)$, la FAC desplazada de la señal, y se muestrea justo en su máximo. Lo sorprendente es que el resultado solo depende de la *energía* de la señal, no de su forma. Un pulso corto y alto es tan bueno como uno largo y plano con la misma energía. Para que el filtro sea causal, $T$ tiene que ser como mínimo la duración de la señal. Equivalente es un __correlador__ (receptor de correlación): multiplica la señal recibida por $s(t)$ e integra sobre la duración de la señal.

:::aufgabe Ejercicio 10 ★★ Un pulso rectangular en el ruido
<span class="anker" id="aufg-10"></span>

Un pulso rectangular de altura 1 V y duración 1 ms se recibe con ruido blanco de densidad espectral de potencia $N_0=10^{-6}$ V$^2$/Hz.

<ol class="al">

<li>

¿Cómo es el filtro adaptado y qué $S_a/N$ (en dB) alcanza?

</li>

<li>

¿Cómo es la salida sin ruido y cuándo hay que muestrear?

</li>

<li>

El pulso se acorta a 0,25 ms, con la misma altura. ¿Qué cambia?

</li>

</ol>

:::loesung
(a) $h(t)=a\,s(T-t)$: de nuevo un rectángulo de 1 ms, causal con $T\ge1$ ms. $E_s=1\,\mathrm{V^2}\cdot1\,\mathrm{ms}=10^{-3}$ V$^2$s; por tanto, $S_a/N=10^{-3}/10^{-6}=1000$, es decir, 30 dB.

(b) La FAC del rectángulo, un triángulo de anchura 2 ms, desplazado $T$: empieza a subir en $t=T-1\,\mathrm{ms}$ y alcanza su máximo en $t=T$. Con $T=1$ ms se muestrea justo al final del pulso; entonces el filtro lo ha «visto» entero.

(c) $E_s$ baja a la cuarta parte, $S_a/N=250$, es decir, 24 dB, 6 dB peor. Solo cuenta la energía. Con la misma altura, un pulso más corto significa menos energía.
:::
:::

## Etapa 11: Probabilidad de error en la recepción binaria

<span class="anker" id="stufe-11"></span>

:::zweck
El receptor debe decidir: ¿se envió el pulso o no? ¿Con qué frecuencia se equivoca?
:::

**La idea.** La muestra a la salida del filtro adaptado tiene distribución gaussiana con la varianza $N$ (ruido) y el valor medio $\sqrt{S_a}$ si se envió el pulso, o 0 si no se envió. El receptor la compara con un umbral de decisión $C$. Se produce un error cuando el ruido empuja el valor al otro lado del umbral. Las dos probabilidades de error son las áreas de las dos curvas de Gauss más allá del umbral:

<span class="anker" id="gl-11-1"></span>
$$P_{e1}=\mathrm{Prob}[y_1\le C]=\tfrac12\operatorname{erfc}\Bigl(\frac{\sqrt{S_a}-C}{\sqrt{2N}}\Bigr),\qquad P_{e0}=\mathrm{Prob}[y_0>C]=\tfrac12\operatorname{erfc}\Bigl(\frac{C}{\sqrt{2N}}\Bigr). \tag{11.1}$$

Si ambos casos se envían con la misma frecuencia, la probabilidad de error media es $\frac12(P_{e1}+P_{e0})$. Es mínima cuando el umbral está justo en el punto medio, $C=\sqrt{S_a}/2$. Con el filtro adaptado ($S_a/N=E_s/N_0$):

<span class="anker" id="gl-11-2"></span>
$$P_{e,\min}=\tfrac12\operatorname{erfc}\sqrt{\frac{E_s}{8N_0}}. \tag{11.2}$$

⁠**Cómo leerlo:** la probabilidad de error solo depende de $E_s/N_0$ y cae con muchísima rapidez: con 10 dB, $5{,}7\cdot10^{-2}$; con 16 dB, $8\cdot10^{-4}$; con 20 dB, $2{,}9\cdot10^{-7}$ (fig. [4](#abb-4)). Unos pocos decibelios más de energía de la señal convierten una transmisión inservible en una casi libre de errores.

:::abbildung et3/k7pe
Probabilidad de error mínima en la recepción todo-nada con filtro adaptado. Puntos rojos: 10 dB, 16 dB, 20 dB.
:::

:::aufgabe Ejercicio 11 ★★ Probabilidad de error
<span class="anker" id="aufg-11"></span>

<ol class="al">

<li>

Calcula $P_{e,\min}$ para $E_s/N_0=10$ dB. Pista: $\operatorname{erfc}(1{,}118)=0{,}114$.

</li>

<li>

¿Por qué el umbral óptimo está en el punto medio entre 0 y $\sqrt{S_a}$? ¿Qué les ocurre a $P_{e1}$ y $P_{e0}$ si se desplaza hacia arriba?

</li>

</ol>

:::loesung
(a) $E_s/N_0=10$: $\sqrt{10/8}=1{,}118$, $P_{e,\min}=\frac12\cdot0{,}114=0{,}057$.

(b) Las dos curvas de Gauss tienen la misma anchura. La suma de las dos áreas de error es mínima donde se cortan las curvas, y por simetría ese punto es el punto medio. Si se desplaza el umbral hacia arriba, $P_{e0}$ disminuye, pero $P_{e1}$ crece más, porque el umbral se adentra en la parte densa de la curva superior.
:::
:::

## Etapa 12: Señales aleatorias en tiempo discreto

<span class="anker" id="stufe-12"></span>

:::zweck
Todo vale también para secuencias de números aleatorios, con sumas en lugar de integrales.
:::

Si se muestrea un proceso de banda limitada a $f_\mathrm g$ con $T\le\frac{1}{2f_\mathrm g}$, las muestras forman un proceso en tiempo discreto $s(n)$. Las distribuciones, los valores esperados y las correlaciones se definen como antes; las medias temporales son sumas, por ejemplo $\varphi_{ss}(m)=\lim_{M\to\infty}\frac{1}{2M+1}\sum_{n=-M}^{M}s(n)s(n+m)$. A través de un sistema LSI con $h(n)$:

<span class="anker" id="gl-12-1"></span>
$$m_g=m_s\sum_nh(n),\qquad\varphi_{gg}(m)=\varphi_{ss}(m)*\varphi^E_{hh}(m),\qquad\Phi_{gg,\mathrm a}(f)=\Phi_{ss,\mathrm a}(f)\,|H_\mathrm a(f)|^2, \tag{12.1}$$

con la densidad espectral de potencia periódica $\Phi_{ss,\mathrm a}(f)=\sum_m\varphi_{ss}(m)\mathrm{e}^{-\mathrm{j}2\pi fm}$ y $L_s=\int_{-1/2}^{1/2}\Phi_{ss,\mathrm a}\mathrm{d} f$. El __ruido blanco en tiempo discreto__ tiene $\Phi_{ss,\mathrm a}=N$ y $\varphi_{ss}(m)=N\delta(m)$: los números consecutivos están incorrelados. A diferencia del caso continuo, su potencia es finita, $L_s=N$.

**Ejemplo 1: promedio de dos valores.** Ruido blanco con distribución uniforme ($\sigma_s^2=\frac1{12}$) a través de $h(n)=\frac12[\delta(n)+\delta(n-1)]$, es decir, $g(n)=\frac12[s(n)+s(n-1)]$. Con $\varphi^E_{hh}=\frac14\delta(m+1)+\frac12\delta(m)+\frac14\delta(m-1)$:

$$\varphi_{gg}(m)=\tfrac{\sigma_s^2}{4}\delta(m+1)+\tfrac{\sigma_s^2}{2}\delta(m)+\tfrac{\sigma_s^2}{4}\delta(m-1).$$

La varianza se reduce a la mitad, a $\frac{1}{24}$, y los valores de salida vecinos están ahora correlados (comparten un valor de entrada). Los valores de salida tienen distribución triangular, porque cada uno es la semisuma de dos números independientes con distribución uniforme. Una simulación con 200 000 números da la varianza 0,0415 en lugar de $\frac1{24}=0{,}0417$.

**Ejemplo 2: filtro recursivo (proceso AR(1)).** Ruido blanco de varianza $\sigma_s^2$ a través de $h(n)=b^n\varepsilon(n)$ ([parte 4](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme/abtastung-und-zeitdiskrete-systeme.html)). Con $\varphi^E_{hh}(m)=\sum_kb^kb^{k+|m|}=\frac{b^{|m|}}{1-b^2}$:

<span class="anker" id="gl-12-2"></span>
$$\varphi_{gg}(m)=\frac{\sigma_s^2}{1-b^2}\,b^{|m|},\qquad\Phi_{gg,\mathrm a}(f)=\frac{\sigma_s^2}{1-2b\cos(2\pi f)+b^2}. \tag{12.2}$$

Para $b=0{,}6$, la varianza es $1{,}56$ veces la varianza de entrada, y los valores vecinos tienen el coeficiente de correlación $0{,}6$. Cuanto más se acerca $b$ a 1, más intensas son las frecuencias bajas (fig. [5](#abb-5)).

:::abbildung et3/k7ar
Densidades espectrales de potencia de procesos AR(1), periódicas con periodo 1. Para $b=0{,}6$ van de 6,25 ($f=0$) a 0,39 ($f=\frac12$); para $b=0{,}9$, de 100 a 0,28.
:::

:::aufgabe Ejercicio 12 ★★ Proceso AR(1)
<span class="anker" id="aufg-12"></span>

Ruido blanco con distribución uniforme ($\sigma_s^2=\frac1{12}$) pasa por $g(n)=s(n)+0{,}6\,g(n-1)$.

<ol class="al">

<li>

Calcula la varianza de salida y $\varphi_{gg}(1)/\varphi_{gg}(0)$.

</li>

<li>

Deduce $\varphi^E_{hh}(m)=\frac{b^{|m|}}{1-b^2}$ con la serie geométrica.

</li>

<li>

¿Sigue teniendo la salida distribución uniforme? ¿Qué distribución esperas aproximadamente y por qué?

</li>

</ol>

:::loesung
(a) $\sigma_g^2=\frac{1/12}{1-0{,}36}=0{,}130$, $\varphi_{gg}(1)/\varphi_{gg}(0)=b=0{,}6$. La simulación da 0,130 y 0,600.

(b) Para $m\ge0$: $\sum_{k\ge0}b^kb^{k+m}=b^m\sum_kb^{2k}=\frac{b^m}{1-b^2}$. La FAC de energía de la respuesta al impulso es par; por tanto, rige $b^{|m|}$.

(c) Ya no tiene distribución uniforme: cada valor de salida es una suma ponderada de muchos valores de entrada independientes, $g(n)=\sum_kb^ks(n-k)$. Según el teorema central del límite, tiene aproximadamente distribución gaussiana. Con $b=0{,}6$ solo contribuyen de forma apreciable unos pocos sumandos; por eso la aproximación es burda, pero la distribución ya tiene claramente forma de campana.
:::
:::

:::kern Lo esencial
<ul>

<li>

Media de conjunto $\mathrm E\{\cdot\}$; estacionario: independiente del desplazamiento; ergódico: media temporal $=$ media de conjunto.

</li>

<li>

$m_s$ (componente continua), $L_s=\mathrm E\{s^2\}$ (potencia), $\sigma_s^2=L_s-m_s^2$ (potencia alterna).

</li>

<li>

FAC: $\varphi_{ss}(0)=L_s$, par, máximo en 0; covarianza $\mu=\varphi-m^2$; suma: $\sigma_s^2=\sigma_u^2+\sigma_v^2+2\mu_{uv}(0)$.

</li>

<li>

$P_s(x)=\mathrm{Prob}[s\le x]$, $p_s=P_s'$; $m_s=\int xp_s$, $L_s=\int x^2p_s$; distribución uniforme $\sigma^2=a^2/12$.

</li>

<li>

Característica: $p_g(y)|\mathrm{d} y|=p_s(x)|\mathrm{d} x|$; error de cuantización $\Delta^2/12$, 6 dB por bit.

</li>

<li>

Independientes $\Rightarrow$ incorreladas; suma de independientes: $p_s=p_f*p_g$; Gauss: $\frac{1}{\sqrt{2\pi\sigma^2}}\mathrm{e}^{-(x-m)^2/2\sigma^2}$.

</li>

<li>

LTI: $m_g=m_sH(0)$, $\varphi_{gg}=\varphi_{ss}*\varphi^E_{hh}$, $\Phi_{gg}=\Phi_{ss}|H|^2$, $L=\int\Phi\,\mathrm{d} f$.

</li>

<li>

Blanco: $\Phi=N_0$, $\varphi=N_0\delta$; térmico $\mathrm E\{u^2\}=4kTRf_\mathrm g$, $kT\approx4$ pW/GHz.

</li>

<li>

Filtro adaptado: $h=a\,s(T-t)$, $(S_a/N)_{\max}=E_s/N_0$; $P_{e,\min}=\frac12\operatorname{erfc}\sqrt{E_s/(8N_0)}$.

</li>

</ul>
:::

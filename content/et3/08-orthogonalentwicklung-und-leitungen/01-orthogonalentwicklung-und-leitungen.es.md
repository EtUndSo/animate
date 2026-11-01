---
title: Desarrollo ortogonal y líneas de transmisión
pfad: Ingeniería eléctrica / 3.er semestre / Señales y sistemas / Desarrollo ortogonal y líneas de transmisión
order: 3280100
summary: Dos temas complementarios: señales como vectores, ondas en líneas eléctricas
tags: ortogonales, ortonormal, teorema de Parseval generalizado, parámetros por unidad de longitud, ecuación de onda, constante de propagación, impedancia característica, constante de atenuación
lang: es
---

## De qué trata

Este artículo completa las partes 1 a 7 con dos temas. El primero generaliza la serie de Fourier: una señal se descompone según funciones ortogonales cualesquiera, igual que un vector se descompone en sus componentes. El segundo muestra lo que ocurre en una línea de transmisión larga: la tensión y la corriente se propagan como ondas, que pueden reflejarse en el extremo. El cuantizador óptimo, que podría ser un tercer tema complementario, ya se encuentra en la [parte 7](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/zufallssignale/zufallssignale.html) (etapa 5).

:::merke La respuesta en tres frases (al final del artículo deberían resultar evidentes)
<ol>

<li>

Con funciones base ortonormales, el mejor coeficiente de una función es su correlación con la función base, y la energía es la suma de los cuadrados de los coeficientes.

</li>

<li>

En una línea de transmisión, toda tensión es una superposición de una onda incidente (progresiva) y una onda reflejada (regresiva). La línea queda descrita por la constante de propagación $\gamma$ y la impedancia característica $Z$.

</li>

<li>

Si la línea se termina con su impedancia característica, la onda reflejada desaparece. En una línea sin pérdidas, todas las frecuencias se propagan igual de rápido, y las señales llegan sin distorsión.

</li>

</ol>
:::

**Cómo trabajar con este artículo.** Cada etapa tiene la idea, preguntas típicas con respuestas desplegables y ejercicios (de ★ a ★★★). Intenta resolverlos primero por tu cuenta; la solución se despliega justo debajo de cada ejercicio.

:::merke Los modelos de referencia de este artículo
<ul>

<li>

⁠**Desarrollo ortogonal** de $f(t)=t^2$ en $[0,1]$ según los polinomios ortonormales $s_0=1$, $s_1=\sqrt3(2t-1)$, $s_2=\sqrt5(6t^2-6t+1)$.

</li>

<li>

⁠**Cable coaxial** con $Z=50\,\Omega$ y $C'=100$ pF/m, sin pérdidas.

</li>

</ul>
:::

## Etapa 1: Señales como vectores, el desarrollo ortogonal

<span class="anker" id="stufe-1"></span>

:::zweck
La serie de Fourier descompone una señal en oscilaciones. Lo mismo puede hacerse con cualquier sistema de funciones ortogonales. Esta etapa muestra cómo se hallan los coeficientes y por qué dan la mejor aproximación.
:::

**La idea.** Un vector en el espacio tiene las componentes $b_i=\vec f\cdot\vec e_i$ respecto a unos vectores unitarios perpendiculares $\vec e_i$. Para señales en un intervalo $[0,T]$, la integral $\int_0^Tf(t)g(t)\mathrm{d} t$ desempeña el papel del producto escalar. Dos señales se llaman __ortogonales__ si esa integral es nula ([parte 6](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen/korrelationsfunktionen.html)). Un sistema de $M$ funciones $s_i(t)$ se llama __ortonormal__ si

<span class="anker" id="gl-1-1"></span>
$$\int_0^Ts_i(t)\,s_j(t)\,\mathrm{d} t=\begin{cases}1&i=j\\0&i\neq j\end{cases}. \tag{1.1}$$

Se aproxima una señal de energía $f(t)$ mediante $\sum_{i=0}^{M-1}b_is_i(t)$, y queda un resto $r(t)=f(t)-\sum b_is_i(t)$.

:::satz Teorema 1.1 (Desarrollo ortogonal)
<span class="anker" id="satz-1-1"></span>

La energía del resto, $E_r=\int_0^Tr^2\mathrm{d} t$, es mínima para

<span class="anker" id="gl-1-2"></span>
$$b_i=\int_0^Tf(t)\,s_i(t)\,\mathrm{d} t. \tag{1.2}$$

Entonces $E_r=E_f-\sum_ib_i^2$. Si $E_r\to0$ al crecer $M$ (sistema completo), se cumple el __teorema de Parseval generalizado__ $E_f=\sum_ib_i^2$.
:::

:::herleitung coeficientes y energía del resto
$E_r=\int_0^T\bigl(f-\sum_ib_is_i\bigr)^2\mathrm{d} t$. Derivar respecto a $b_j$ e igualar a cero:

$$\frac{\partial E_r}{\partial b_j}=-2\int_0^T\Bigl(f-\sum_ib_is_i\Bigr)s_j\,\mathrm{d} t=0\quad\Longrightarrow\quad\int_0^Tfs_j\,\mathrm{d} t=\sum_ib_i\int_0^Ts_is_j\,\mathrm{d} t=b_j.$$

La ortonormalidad solo deja $i=j$ en la suma. Si se sustituyen estos $b_i$ y se desarrolla el cuadrado, los términos cruzados se anulan, de nuevo por la ortonormalidad: $E_r=E_f-2\sum b_i^2+\sum b_i^2=E_f-\sum b_i^2$.
:::

⁠**Cómo leerlo:** cada coeficiente se determina por separado, con independencia de los demás. Si se añade una función base, los coeficientes anteriores no cambian. Esa es la ventaja de los sistemas ortogonales, exactamente como en la serie de Fourier ([parte 3](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)). $b_i$ es la correlación cruzada $\varphi^E_{fs_i}(0)$. Por eso los coeficientes pueden medirse con un banco de filtros adaptados $h_i(t)=s_i(T-t)$, cuyas salidas se muestrean en $t=T$ ([parte 7](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/zufallssignale/zufallssignale.html)).

**Ejemplo.** $f(t)=t^2$ en $[0,1]$, $E_f=\frac15$. Con $s_0=1$ y $s_1=\sqrt3(2t-1)$:

$$b_0=\int_0^1t^2\mathrm{d} t=\tfrac13,\qquad b_1=\sqrt3\int_0^1t^2(2t-1)\mathrm{d} t=\tfrac{\sqrt3}{6}=0{,}289,\qquad\sum b_i^2=\tfrac19+\tfrac1{12}=\tfrac{7}{36}.$$

La aproximación es $\frac13+\frac{\sqrt3}{6}\sqrt3(2t-1)=t-\frac16$, la mejor recta en el sentido de la energía. La energía del resto es $\frac15-\frac7{36}=\frac{1}{180}=0{,}0056$, es decir, el 2,8 % de $E_f$. Con $s_2=\sqrt5(6t^2-6t+1)$ se añade $b_2=\frac{\sqrt5}{30}=0{,}075$, y el resto se anula, porque $t^2$ ya es un polinomio de grado dos.

:::aufgabe Ejercicio 1 ★ Comprobar la ortonormalidad
<span class="anker" id="aufg-1"></span>

Demuestra que $s_0=1$ y $s_1=\sqrt3(2t-1)$ son ortonormales en $[0,1]$. ¿Por qué necesita $s_1$ el factor $\sqrt3$?

:::loesung
$\int_0^11\cdot\sqrt3(2t-1)\mathrm{d} t=\sqrt3\,[t^2-t]_0^1=0$: ortogonales. $\int_0^11^2\mathrm{d} t=1$. $\int_0^13(2t-1)^2\mathrm{d} t=3\cdot\bigl[\frac{(2t-1)^3}{6}\bigr]_0^1=3\cdot\frac{1+1}{6}=1$. Sin el factor, la energía de $2t-1$ sería solo $\frac13$. El factor $\sqrt3$ la normaliza a 1; si no, $b_1=\int fs_1\mathrm{d} t$ no sería el coeficiente correcto.
:::
:::

:::aufgabe Ejercicio 2 ★★ La mejor aproximación
<span class="anker" id="aufg-2"></span>

<ol class="al">

<li>

Recalcula $b_1$ para $f(t)=t^2$ y confirma la aproximación $t-\frac16$.

</li>

<li>

Comprueba $E_r=\frac{1}{180}$ calculando directamente $\int_0^1\bigl(t^2-t+\frac16\bigr)^2\mathrm{d} t$.

</li>

<li>

Determina los coeficientes de $f(t)=\sqrt2\cos(2\pi t)$ respecto a $s_0$ y $s_1$. ¿Qué significa el resultado?

</li>

</ol>

:::loesung
(a) $\int_0^1t^2(2t-1)\mathrm{d} t=\frac24-\frac13=\frac16$; por tanto, $b_1=\frac{\sqrt3}{6}$. Aproximación: $\frac13+\frac{\sqrt3}{6}\cdot\sqrt3(2t-1)=\frac13+t-\frac12=t-\frac16$.

(b) $\int_0^1\bigl(t^2-t+\tfrac16\bigr)^2\mathrm{d} t=\int_0^1\bigl(t^4-2t^3+\tfrac43t^2-\tfrac13t+\tfrac1{36}\bigr)\mathrm{d} t=\tfrac15-\tfrac12+\tfrac49-\tfrac16+\tfrac1{36}=\tfrac{1}{180}$.

(c) $b_0=\sqrt2\int_0^1\cos(2\pi t)\mathrm{d} t=0$ y $b_1=\sqrt6\int_0^1(2t-1)\cos(2\pi t)\mathrm{d} t=0$ (el coseno es simétrico respecto a $t=\frac12$, y $2t-1$, antisimétrico). Ambos coeficientes son nulos: la función es ortogonal a las dos funciones base, la aproximación es nula y todo el contenido de la señal queda en el resto. Una base solo sirve para señales que se parezcan a sus funciones.
:::
:::

## Etapa 2: Las ecuaciones de la línea de transmisión

<span class="anker" id="stufe-2"></span>

:::zweck
Hasta ahora, las líneas eran conexiones ideales. Si una línea es larga en comparación con la longitud de onda, una señal necesita un tiempo apreciable para recorrerla. Esta etapa plantea las ecuaciones que lo describen.
:::

**La idea.** La línea se divide en tramos cortos de longitud $\mathrm{d} s$. Cada tramo tiene una resistencia serie y una inductancia serie (los conductores de ida y de retorno), además de una capacidad en paralelo y una conductancia en paralelo (entre los conductores). En una línea uniforme, estas magnitudes son proporcionales a la longitud: $R'\mathrm{d} s$, $L'\mathrm{d} s$, $C'\mathrm{d} s$, $G'\mathrm{d} s$, con los __parámetros por unidad de longitud__ $R'$, $L'$, $C'$, $G'$ (valores por metro, fig. [1](#abb-1)).

:::abbildung et3/k8element
Circuito equivalente de un tramo corto de línea de longitud $\mathrm{d} s$, con los parámetros por unidad de longitud $R'$, $L'$, $G'$, $C'$.
:::

:::satz Teorema 2.1 (Ecuaciones de la línea de transmisión, ecuaciones del telegrafista)
<span class="anker" id="satz-2-1"></span>

<span class="anker" id="gl-2-1"></span>
$$\frac{\partial u}{\partial s}=-\Bigl(R'+L'\frac{\partial}{\partial t}\Bigr)i,\qquad\frac{\partial i}{\partial s}=-\Bigl(G'+C'\frac{\partial}{\partial t}\Bigr)u. \tag{2.1}$$
:::

:::herleitung ecuaciones de la línea de transmisión
Ley de mallas a lo largo del tramo: $u=R'\mathrm{d} s\,i+L'\mathrm{d} s\,\frac{\partial i}{\partial t}+\bigl(u+\frac{\partial u}{\partial s}\mathrm{d} s\bigr)$, es decir, $\frac{\partial u}{\partial s}\mathrm{d} s=-R'\mathrm{d} s\,i-L'\mathrm{d} s\,\frac{\partial i}{\partial t}$. Ley de nudos: de la corriente $i$, una parte se deriva por $G'\mathrm{d} s$ y $C'\mathrm{d} s$, $i=G'\mathrm{d} s\,u+C'\mathrm{d} s\,\frac{\partial u}{\partial t}+\bigl(i+\frac{\partial i}{\partial s}\mathrm{d} s\bigr)$. Dividir entre $\mathrm{d} s$. (En sentido estricto, en la ley de nudos aparece la tensión al final del tramo; la diferencia es de segundo orden en $\mathrm{d} s$.)
:::

⁠**Cómo leerlo:** la tensión cae a lo largo de la línea porque circula corriente por los elementos serie. La corriente disminuye porque se deriva por los elementos en paralelo, entre los conductores. Las dos ecuaciones acoplan $u$ e $i$ en la posición y en el tiempo.

## Etapa 3: Ondas con excitación sinusoidal

<span class="anker" id="stufe-3"></span>

:::zweck
Con fasores, las ecuaciones en derivadas parciales se convierten en una ecuación ordinaria en la posición. Su solución son dos ondas que se propagan en sentidos opuestos.
:::

Con $u(s,t)=\sqrt2\operatorname{Re}\{\underline U(s)\mathrm{e}^{\mathrm{j}2\pi ft}\}$, y lo mismo para $i$, $\frac{\partial}{\partial t}$ se convierte en $\mathrm{j}2\pi f$:

$$\frac{\mathrm{d}\underline U}{\mathrm{d} s}=-(R'+\mathrm{j}2\pi fL')\,\underline I,\qquad\frac{\mathrm{d}\underline I}{\mathrm{d} s}=-(G'+\mathrm{j}2\pi fC')\,\underline U.$$

Derivando la primera ecuación y sustituyendo la segunda resulta la __ecuación de onda__ $\frac{\mathrm{d}^2\underline U}{\mathrm{d} s^2}=\gamma^2\underline U$.

:::satz Teorema 3.1 (Onda incidente y onda reflejada)
<span class="anker" id="satz-3-1"></span>

<span class="anker" id="gl-3-1"></span>
$$\underline U(s)=\underline U_1\mathrm{e}^{-\gamma s}+\underline U_2\mathrm{e}^{\gamma s},\qquad\underline I(s)=\frac{1}{Z}\bigl(\underline U_1\mathrm{e}^{-\gamma s}-\underline U_2\mathrm{e}^{\gamma s}\bigr), \tag{3.1}$$

con la __constante de propagación__ y la __impedancia característica__

<span class="anker" id="gl-3-2"></span>
$$\gamma=\sqrt{(R'+\mathrm{j}2\pi fL')(G'+\mathrm{j}2\pi fC')}=\alpha+\mathrm{j}\beta,\qquad Z=\sqrt{\frac{R'+\mathrm{j}2\pi fL'}{G'+\mathrm{j}2\pi fC'}}. \tag{3.2}$$
:::

⁠**Cómo leerlo:** con $\gamma=\alpha+\mathrm{j}\beta$, el primer sumando se convierte, en el dominio del tiempo, en $\hat u_1\mathrm{e}^{-\alpha s}\cos(2\pi ft-\beta s+\varphi_1)$: una onda que se propaga en el sentido de $s$ creciente y que, al hacerlo, decae con la __constante de atenuación__ $\alpha$. Un paso por cero se desplaza con la velocidad $v=2\pi f/\beta$; la longitud de onda es $\lambda=2\pi/\beta$. El segundo sumando se propaga en sentido contrario. $Z$ es la razón entre tensión y corriente en una sola onda. Las condiciones de contorno fijan las constantes $\underline U_1$, $\underline U_2$, por ejemplo la tensión y la corriente al principio de la línea: $\underline U_{1,2}=\frac12(\underline U_a\pm Z\underline I_a)$.

**Reflexión en el extremo.** Si la línea está terminada en su extremo ($s=l$) con una resistencia $R_\mathrm E=\underline U_e/\underline I_e$, la tensión puede escribirse como

<span class="anker" id="gl-3-3"></span>
$$\underline U(s)=\tfrac12(R_\mathrm E+Z)\,\underline I_e\,\mathrm{e}^{\gamma(l-s)}+\tfrac12(R_\mathrm E-Z)\,\underline I_e\,\mathrm{e}^{-\gamma(l-s)}. \tag{3.3}$$

El primer sumando es la onda incidente; el segundo, la onda reflejada, que vuelve desde el extremo. Para $R_\mathrm E=Z$ desaparece la onda reflejada: una terminación (carga) con la impedancia característica absorbe por completo la onda que llega, como si la línea continuara indefinidamente. La razón entre las dos ondas en el extremo es el __coeficiente de reflexión__ $r=\frac{R_\mathrm E-Z}{R_\mathrm E+Z}$ (además: cortocircuito, $r=-1$; circuito abierto, $r=+1$).

:::frage ¿Por qué una terminación incorrecta no molesta en las líneas cortas?
Porque entonces la onda reflejada vuelve casi de inmediato. Si el tiempo de propagación a lo largo de la línea es pequeño frente a la duración de los cambios de la señal (línea corta frente a la longitud de onda), la onda incidente y la reflejada se superponen prácticamente a la vez, y solo se nota la resistencia de terminación. Solo cuando el tiempo de propagación se vuelve comparable, por ejemplo con señales digitales rápidas o en alta frecuencia, las reflexiones aparecen como ecos y distorsionan la señal.
:::

## Etapa 4: La línea de transmisión sin pérdidas

<span class="anker" id="stufe-4"></span>

:::zweck
Sin pérdidas ($R'=G'=0$), la impedancia característica y la velocidad se vuelven independientes de la frecuencia. Entonces la solución en forma de ondas vale para señales cualesquiera, no solo para oscilaciones sinusoidales.
:::

Con $R'=G'=0$ se tiene $\gamma=\mathrm{j}2\pi f\sqrt{L'C'}$: no hay atenuación ($\alpha=0$), y $\beta$ es proporcional a $f$. De ahí:

<span class="anker" id="gl-4-1"></span>
$$Z=\sqrt{\frac{L'}{C'}},\qquad v=\frac{1}{\sqrt{L'C'}},\qquad\frac{\partial^2u}{\partial s^2}=L'C'\frac{\partial^2u}{\partial t^2}. \tag{4.1}$$

:::satz Teorema 4.1 (Solución de d'Alembert)
<span class="anker" id="satz-4-1"></span>

Toda solución de la ecuación de onda [(4.1)](#gl-4-1) tiene la forma

<span class="anker" id="gl-4-2"></span>
$$u(s,t)=u_\mathrm{prog}(s-vt)+u_\mathrm{reg}(s+vt) \tag{4.2}$$

con funciones cualesquiera (dos veces derivables) $u_\mathrm{prog}$ (progresiva) y $u_\mathrm{reg}$ (regresiva).
:::

⁠**Cómo leerlo:** una forma de señal cualquiera se propaga sin cambios a lo largo de la línea con la velocidad $v$. Esto se debe a que todas las componentes de frecuencia son igual de rápidas y se atenúan igual de poco: la línea es un sistema sin distorsión en el sentido de la [parte 5](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme/tiefpass-und-bandpasssysteme.html), con el retardo $l/v$. La ecuación de onda para $u$ se obtiene de [(2.1)](#gl-2-1) derivando la primera ecuación respecto a $s$ y la segunda respecto a $t$, y eliminando $i$.

**Ejemplo: cable coaxial.** $Z=50\,\Omega$ y $C'=100$ pF/m dan $L'=Z^2C'=250$ nH/m y $v=\frac{1}{\sqrt{L'C'}}=2\cdot10^8$ m/s, dos tercios de la velocidad de la luz (debido al dieléctrico del cable). Una señal tarda 50 ns en recorrer 10 m de cable. Si el cable se termina con 75 $\Omega$ en lugar de 50 $\Omega$, $r=\frac{75-50}{75+50}=0{,}2$: el 20 % de la amplitud de tensión vuelve como eco.

:::ltspice Reflexiones en una línea
⁠**Esquema:** fuente `voltage` con `PULSE(0 2 0 1n 1n 10n 1)` y una resistencia interna `res` con `50` hacia el nodo `in`. Desde `in`, una línea sin pérdidas `tline` con `Td=50n Z0=50` (el cable coaxial de 10 m del ejemplo) hasta el nodo `end`, y ahí `res` con `{RE}` a masa. Como la resistencia interna es igual a $Z$, sale una onda de 1 V, y el eco se absorbe por completo en la fuente.

⁠**Directivas:** `.param RE=75`, `.step param RE list 1m 50 75 1G` (casi cortocircuito, adaptación, 75 $\Omega$, casi circuito abierto), `.tran 0 200n 0 0.1n`.

⁠**Lo que ves:** en `in`, primero el pulso de 1 V. Al cabo de $2\cdot50\,\mathrm{ns}=100$ ns vuelve el eco con la altura $r\cdot1$ V: $-1$; $0$; $0{,}2$ y $+1$, exactamente $r=\frac{R_\mathrm E-Z}{R_\mathrm E+Z}$. En `end` aparece, a partir de 50 ns, la suma de la onda incidente y la reflejada, $(1+r)\cdot1$ V. Ajusta `Td` y `Z0` a tus valores del ejercicio [4](#aufg-4)(a), pon `RE` a 100 y compara la altura del eco con tu resultado del ejercicio [4](#aufg-4)(b).
:::

:::aufgabe Ejercicio 3 ★★ Comprobar d'Alembert
<span class="anker" id="aufg-3"></span>

Demuestra por sustitución que $u(s,t)=u_\mathrm{prog}(s-vt)$ resuelve la ecuación de onda [(4.1)](#gl-4-1) con $v=1/\sqrt{L'C'}$. ¿Cómo se relaciona la corriente correspondiente con la tensión? Pista: primera ecuación de la línea con $R'=0$.

:::loesung
Con $x=s-vt$: $\frac{\partial^2u}{\partial s^2}=u_\mathrm{prog}''(x)$ y $\frac{\partial^2u}{\partial t^2}=v^2u_\mathrm{prog}''(x)$. La ecuación de onda exige $u''=L'C'v^2u''$, es decir, $v^2=\frac{1}{L'C'}$. Corriente: con $R'=0$ se tiene $\frac{\partial u}{\partial s}=-L'\frac{\partial i}{\partial t}$, es decir, $u_\mathrm{prog}'(x)=-L'\frac{\partial i}{\partial t}$. El planteamiento $i=u_\mathrm{prog}(x)/Z$ da $\frac{\partial i}{\partial t}=-\frac vZu'_\mathrm{prog}$, y esto encaja, porque $L'v/Z=L'\cdot\frac{1}{\sqrt{L'C'}}\cdot\sqrt{\frac{C'}{L'}}=1$. En la onda progresiva, la tensión y la corriente están en todas partes en la razón $Z$.
:::
:::

:::aufgabe Ejercicio 4 ★★ Cable y terminación
<span class="anker" id="aufg-4"></span>

Un cable sin pérdidas tiene $L'=300$ nH/m y $C'=120$ pF/m.

<ol class="al">

<li>

Calcula $Z$, $v$ y el tiempo de propagación para 5 m.

</li>

<li>

¿Con qué resistencia hay que terminarlo para que no se refleje nada? ¿Qué coeficiente de reflexión resulta con 100 $\Omega$?

</li>

<li>

¿Hasta qué frecuencia pueden tratarse todavía los 5 m como «cortos», si la línea debe medir como máximo una décima parte de la longitud de onda?

</li>

</ol>

:::loesung
(a) $Z=\sqrt{300/120}\cdot\sqrt{\frac{\text{nH}}{\text{pF}}}=\sqrt{2{,}5\cdot10^3}\,\Omega=50\,\Omega$. $v=\frac{1}{\sqrt{300\cdot10^{-9}\cdot120\cdot10^{-12}}}\,\mathrm{m/s}=\frac{1}{\sqrt{3{,}6\cdot10^{-17}}}\,\mathrm{m/s}=1{,}67\cdot10^8$ m/s. Tiempo de propagación para 5 m: 30 ns.

(b) Con $Z=50\,\Omega$. Con 100 $\Omega$: $r=\frac{100-50}{150}=\frac13$.

(c) $\lambda=v/f\ge50$ m; por tanto, $f\le\frac{1{,}67\cdot10^8}{50}\,\mathrm{Hz}=3{,}3$ MHz.
:::
:::

:::kern Lo esencial
<ul>

<li>

Ortonormal: $\int s_is_j\mathrm{d} t=\delta_{ij}$; mejores coeficientes $b_i=\int fs_i\mathrm{d} t$; $E_r=E_f-\sum b_i^2$; completo: $E_f=\sum b_i^2$.

</li>

<li>

Ecuaciones de la línea: $\partial_su=-(R'+L'\partial_t)i$, $\partial_si=-(G'+C'\partial_t)u$.

</li>

<li>

Fasores (con $\omega=2\pi f$): $\underline U=\underline U_1\mathrm{e}^{-\gamma s}+\underline U_2\mathrm{e}^{\gamma s}$; $\gamma=\sqrt{(R'+\mathrm{j}\omega L')(G'+\mathrm{j}\omega C')}=\alpha+\mathrm{j}\beta$; $Z=\sqrt{\frac{R'+\mathrm{j}\omega L'}{G'+\mathrm{j}\omega C'}}$.

</li>

<li>

Terminación con $Z$: sin reflexión; $r=\frac{R_\mathrm E-Z}{R_\mathrm E+Z}$.

</li>

<li>

Sin pérdidas: $Z=\sqrt{L'/C'}$, $v=1/\sqrt{L'C'}$, $u=u_\mathrm{prog}(s-vt)+u_\mathrm{reg}(s+vt)$.

</li>

</ul>
:::

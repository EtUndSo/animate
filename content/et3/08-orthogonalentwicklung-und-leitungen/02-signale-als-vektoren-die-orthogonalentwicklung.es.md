---
title: Etapa 1: Señales como vectores, el desarrollo ortogonal
pfad: Ingeniería eléctrica / 3.er semestre / ET3 – Fundamentos de ingeniería eléctrica 3: señales y sistemas / Desarrollo ortogonal y líneas de transmisión
adresse: elektrotechnik/3-semester/signale-und-systeme/orthogonalentwicklung-und-leitungen
knoten: Capítulo 8: Desarrollo ortogonal y líneas de transmisión
order: 3280200
summary: La serie de Fourier descompone una señal en oscilaciones.
tags: ortogonales, ortonormal, teorema de Parseval generalizado
lang: es
---

<span class="anker" id="stufe-1"></span>

:::zweck
La serie de Fourier descompone una señal en oscilaciones. Lo mismo puede hacerse con cualquier sistema de funciones ortogonales. Esta etapa muestra cómo se hallan los coeficientes y por qué dan la mejor aproximación.
:::

**La idea.** Un vector en el espacio tiene las componentes $b_i=\vec f\cdot\vec e_i$ respecto a unos vectores unitarios perpendiculares $\vec e_i$. Para señales en un intervalo $[0,T]$, la integral $\int_0^Tf(t)g(t)\mathrm{d} t$ desempeña el papel del producto escalar. Dos señales se llaman __ortogonales__ si esa integral es nula ([capítulo 6](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen/korrelationsfunktionen.html)). Un sistema de $M$ funciones $s_i(t)$ se llama __ortonormal__ si

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

⁠**Cómo leerlo:** cada coeficiente se determina por separado, con independencia de los demás. Si se añade una función base, los coeficientes anteriores no cambian. Esa es la ventaja de los sistemas ortogonales, exactamente como en la serie de Fourier ([capítulo 3](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)). $b_i$ es la correlación cruzada $\varphi^E_{fs_i}(0)$. Por eso los coeficientes pueden medirse con un banco de filtros adaptados $h_i(t)=s_i(T-t)$, cuyas salidas se muestrean en $t=T$ ([capítulo 7](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/zufallssignale/zufallssignale.html)).

::::beispiel
$f(t)=t^2$ en $[0,1]$, $E_f=\frac15$. Con $s_0=1$ y $s_1=\sqrt3(2t-1)$:

$$b_0=\int_0^1t^2\mathrm{d} t=\tfrac13,\qquad b_1=\sqrt3\int_0^1t^2(2t-1)\mathrm{d} t=\tfrac{\sqrt3}{6}=0{,}289,\qquad\sum b_i^2=\tfrac19+\tfrac1{12}=\tfrac{7}{36}.$$

La aproximación es $\frac13+\frac{\sqrt3}{6}\sqrt3(2t-1)=t-\frac16$, la mejor recta en el sentido de la energía. La energía del resto es $\frac15-\frac7{36}=\frac{1}{180}=0{,}0056$, es decir, el 2,8 % de $E_f$. Con $s_2=\sqrt5(6t^2-6t+1)$ se añade $b_2=\frac{\sqrt5}{30}=0{,}075$, y el resto se anula, porque $t^2$ ya es un polinomio de grado dos.
::::

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

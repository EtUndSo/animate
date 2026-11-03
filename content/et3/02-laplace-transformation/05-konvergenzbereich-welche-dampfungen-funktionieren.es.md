---
title: Región de convergencia: qué amortiguamientos funcionan
pfad: Ingeniería eléctrica / 3.er semestre / Señales y sistemas / Transformada de Laplace
order: 3220500
summary: Toda señal como superposición de $\mathrm{e}^{pt}$, y por qué un sistema LTI convierte esto en una multiplicación
tags: 
lang: es
---

<span class="anker" id="stufe-2-3"></span>

**La idea.** El factor $\mathrm{e}^{-\sigma t}$ actúa a ambos lados del eje temporal, pero de forma opuesta. Para $t\to+\infty$ amortigua tanto más cuanto mayor es $\sigma$. Para $t\to-\infty$, $\mathrm{e}^{-\sigma t}=\mathrm{e}^{\sigma|t|}$, y allí un $\sigma$ grande amplifica. De ahí se siguen las tres formas de la región de convergencia:

<ul>

<li>

⁠**señal por la derecha (causal)**, $s(t)=0$ para $t<0$, que crece como mucho como $\mathrm{e}^{\alpha t}$: sirve cualquier $\sigma>\alpha$. Región de convergencia: el semiplano a la *derecha* de una frontera.

</li>

<li>

⁠**señal por la izquierda (anticausal)**: solo cuenta el lado $t\to-\infty$; ayudan los $\sigma$ pequeños. Región de convergencia: un semiplano a la *izquierda* de una frontera.

</li>

<li>

⁠**señal bilateral**: ambas condiciones deben cumplirse a la vez. Región de convergencia: una *franja*, que también puede estar vacía.

</li>

</ul>

¿Por qué las fronteras son siempre verticales? Se cumple $|\mathrm{e}^{-pt}|=\mathrm{e}^{-\sigma t}$. Que $\int|s(t)\mathrm{e}^{-pt}|\mathrm{d} t$ sea finita depende solo de $\sigma$, nunca de $f$.

⁠**En resumen:** la región de convergencia es el conjunto de todos los amortiguamientos $\sigma$ con los que $s(t)\,\mathrm{e}^{-\sigma t}$ se vuelve absolutamente integrable.

:::merke Los pares básicos de transformadas (se usan en todo el capítulo)
Para un número complejo $p_0$ cualquiera:

<span class="anker" id="gl-2-2"></span>
<span class="anker" id="gl-2-3"></span>
<span class="anker" id="gl-2-4"></span>
<span class="anker" id="gl-2-5"></span>
$$\begin{aligned} \mathrm{e}^{p_0t}\,\varepsilon(t)\quad&\longleftrightarrow\quad\frac{1}{p-p_0},&&\operatorname{Re} p>\operatorname{Re} p_0,\\ -\mathrm{e}^{p_0t}\,\varepsilon(-t)\quad&\longleftrightarrow\quad\frac{1}{p-p_0},&&\operatorname{Re} p<\operatorname{Re} p_0,\\ \delta(t)\quad&\longleftrightarrow\quad1,&&\text{todo }p,\\ t\,\varepsilon(t)\quad&\longleftrightarrow\quad\frac{1}{p^2},&&\operatorname{Re} p>0. \end{aligned} \tag{2.2|2.3|2.4|2.5}$$

Con $p_0=0$, de [(2.2)](#gl-2-2) se obtiene el escalón: $\varepsilon(t)\leftrightarrow1/p$ para $\operatorname{Re} p>0$. Las dos primeras líneas tienen la *misma* expresión y distintas regiones de convergencia: solo las dos cosas juntas determinan la señal.
:::

:::herleitung pares básicos de transformadas
[(2.2)](#gl-2-2): $\int_0^\infty\mathrm{e}^{-(p-p_0)t}\mathrm{d} t=\Bigl[\frac{-\mathrm{e}^{-(p-p_0)t}}{p-p_0}\Bigr]_0^\infty=\frac{1}{p-p_0}$. El valor en el límite superior se anula si y solo si $\operatorname{Re}(p-p_0)>0$.

[(2.3)](#gl-2-3): $-\int_{-\infty}^0\mathrm{e}^{-(p-p_0)t}\mathrm{d} t=-\Bigl[\frac{-\mathrm{e}^{-(p-p_0)t}}{p-p_0}\Bigr]_{-\infty}^0=\frac{1}{p-p_0}$. El valor para $t\to-\infty$ se anula si y solo si $\operatorname{Re}(p-p_0)<0$.

[(2.4)](#gl-2-4): propiedad de selección, $\int\delta(t)\mathrm{e}^{-pt}\mathrm{d} t=\mathrm{e}^{0}=1$.

[(2.5)](#gl-2-5): integración por partes, $\int_0^\infty t\,\mathrm{e}^{-pt}\mathrm{d} t=\Bigl[\frac{-t\,\mathrm{e}^{-pt}}{p}\Bigr]_0^\infty+\frac1p\int_0^\infty\mathrm{e}^{-pt}\mathrm{d} t=0+\frac{1}{p^2}$ para $\operatorname{Re} p>0$.
:::

:::frage Al calcular $\int_0^\infty\mathrm{e}^{-bt}\mathrm{e}^{-pt}\mathrm{d} t$, ¿por qué desaparecen los términos exponenciales y por qué sale $\frac{1}{b+p}$ y no $\frac{1}{-(b+p)}$?
Ambas cosas se deben a la evaluación en los límites. La primitiva de $\mathrm{e}^{-(b+p)t}$ es $-\frac{\mathrm{e}^{-(b+p)t}}{b+p}$, con signo menos, porque al derivar aparece el factor $-(b+p)$. Después se calcula «límite superior menos límite inferior»:

$$\int_0^\infty\mathrm{e}^{-(b+p)t}\mathrm{d} t=\underbrace{\lim_{t\to\infty}\Bigl(-\frac{\mathrm{e}^{-(b+p)t}}{b+p}\Bigr)}_{=\,0}-\Bigl(-\frac{\mathrm{e}^{0}}{b+p}\Bigr)=\frac{1}{b+p}.$$

<ul>

<li>

⁠**Límite superior:** $|\mathrm{e}^{-(b+p)t}|=\mathrm{e}^{-(\operatorname{Re} b+\sigma)t}$ tiende a cero si y solo si $\operatorname{Re} p>-\operatorname{Re} b$. Esta condición *es* la región de convergencia. Fuera de ella, el término exponencial no desaparecería y crecería sin límite.

</li>

<li>

⁠**Límite inferior:** $\mathrm{e}^0=1$; allí no queda ningún término exponencial.

</li>

<li>

⁠**Signo:** el menos de la primitiva se encuentra con el menos con el que se resta el límite inferior. Menos por menos da más.

</li>

</ul>

Con el pulso por la izquierda $\mathrm{e}^{-bt}\varepsilon(-t)$ ocurre lo contrario. Se integra de $-\infty$ a $0$; ahora $t=0$ es el límite *superior*. Su contribución $-\frac{1}{b+p}$ no se resta, y el signo menos se mantiene. El límite inferior $t\to-\infty$ solo se anula para $\operatorname{Re}(b+p)<0$; por eso esta región de convergencia está a la izquierda. Con $p_0=-b$, estos son los pares básicos [(2.2)](#gl-2-2) y [(2.3)](#gl-2-3).
:::

:::frage ¿Se miran las partes reales de $b$ y $p$ porque el decaimiento del integrando decide la integrabilidad? Para algunos $b$ la señal decae; para otros crece, no baja a cero, y la integral no converge porque siempre se sigue sumando algo.
Sí, exactamente. El módulo del integrando es

$$\bigl|\mathrm{e}^{-(b+p)t}\bigr|=\mathrm{e}^{-\operatorname{Re}(b+p)\,t}\cdot\underbrace{\bigl|\mathrm{e}^{-\mathrm{j}\operatorname{Im}(b+p)\,t}\bigr|}_{=\,1}.$$

La parte imaginaria solo hace girar el integrando en el plano complejo; no cambia su módulo. Si crece o decae lo decide únicamente la parte real. Tres precisiones:

<ul>

<li>

Cuenta la *suma* $\operatorname{Re} b+\sigma$. La señal puede crecer por sí misma ($\operatorname{Re} b<0$), siempre que el amortiguamiento $\sigma$ sea más fuerte. Es el truco «amortiguar» del apartado 2.2.

</li>

<li>

«Tiende a cero» no basta por sí solo. También $1/t$ tiende a cero, pero $\int_1^\infty\frac{\mathrm{d} t}{t}=\infty$, porque las contribuciones disminuyen demasiado despacio. El decaimiento exponencial es lo bastante rápido: $\int_0^\infty\mathrm{e}^{-\operatorname{Re}(b+p)t}\mathrm{d} t=\frac{1}{\operatorname{Re}(b+p)}$ es finita.

</li>

<li>

En la frontera $\operatorname{Re}(b+p)=0$, el integrando tiene módulo constante 1 y solo gira. La integral oscila entonces en lugar de acercarse a un valor, y justo en el polo incluso crece linealmente (ejercicio [3a](#aufg-3a)). Por eso la recta frontera no pertenece a la región de convergencia.

</li>

</ul>
:::

:::frage Entonces, ¿vale esto para cualquier función?
No, solo para funciones con región de convergencia no vacía. Tres contraejemplos:

<ul>

<li>

$\mathrm{e}^{t^2}\varepsilon(t)$ crece más rápido que cualquier función exponencial. $\mathrm{e}^{t^2-\sigma t}\to\infty$ para todo $\sigma$; ningún amortiguamiento basta.

</li>

<li>

$\mathrm{e}^{|t|}$: la mitad derecha exige $\sigma>1$, y la izquierda, $\sigma<-1$. Ambas cosas a la vez son imposibles.

</li>

<li>

Incluso la constante $s(t)=1$ para todo $t$: a la derecha $\sigma>0$, a la izquierda $\sigma<0$. La transformada de Fourier abarca aun así este tipo de señales, con un impulso de Dirac en el espectro.

</li>

</ul>

Para señales por la derecha con crecimiento como mucho exponencial, siempre funciona. Entre ellas está toda señal que se conecta en un circuito en $t=0$.
:::

:::frage ¿Por qué basta una sola recta, si el plano $p$ es bidimensional?
Toda recta de la región de convergencia da la misma $s(t)$: con un $\sigma$ mayor se amortigua más en el paso 1 y se compensa más en el paso 3; ambos efectos se anulan. Comprobado numéricamente: con $\sigma=0{,}2$ y $\sigma=1/\mathrm s$ se obtiene para el escalón en ambos casos $s(1\,\mathrm{s})\approx1{,}00$ y $s(-1\,\mathrm{s})\approx0{,}00$. Así pues, el plano contiene más de lo que hace falta para la superposición. Su utilidad está en otra parte: en el plano, $S(p)$ puede describirse con pocos números, los polos y los ceros. (Nota adicional: $S(p)$ es derivable en sentido complejo en la región de convergencia; por eso los valores sobre una recta determinan la función en toda la región.)
:::

:::aufgabe Ejercicio 2 ★ Laplace es Fourier de una señal amortiguada
<span class="anker" id="aufg-2"></span>

<ol class="al">

<li>

Demuestra que $S(\sigma+\mathrm{j}2\pi f)=\mathcal{F}\{s(t)\,\mathrm{e}^{-\sigma t}\}(f)$ descomponiendo $\mathrm{e}^{-pt}$ en dos factores.

</li>

<li>

Compruébalo con el escalón: calcula directamente $\mathcal{F}\{\mathrm{e}^{-\sigma t}\varepsilon(t)\}$ para $\sigma>0$ y compáralo con $S(p)=1/p$.

</li>

</ol>

:::loesung
(a) $S(\sigma+\mathrm{j}2\pi f)=\int s(t)\,\mathrm{e}^{-(\sigma+\mathrm{j}2\pi f)t}\mathrm{d} t=\int\bigl[s(t)\mathrm{e}^{-\sigma t}\bigr]\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t=\mathcal{F}\{s(t)\mathrm{e}^{-\sigma t}\}(f)$.

(b) $\mathcal{F}\{\mathrm{e}^{-\sigma t}\varepsilon(t)\}=\int_0^\infty\mathrm{e}^{-(\sigma+\mathrm{j}2\pi f)t}\mathrm{d} t=\dfrac{1}{\sigma+\mathrm{j}2\pi f}$ para $\sigma>0$. Es $1/p$ en el punto $p=\sigma+\mathrm{j}2\pi f$.
:::
:::

:::aufgabe Ejercicio 3 ★★ Una señal creciente
<span class="anker" id="aufg-3"></span>

$s(t)=\mathrm{e}^{2t}\varepsilon(t)$, por ejemplo la respuesta al impulso de un sistema inestable ($t$ en s).

<ol class="al">

<li>

¿Por qué no existe transformada de Fourier en sentido clásico?

</li>

<li>

¿Para qué $\sigma$ es $s(t)\,\mathrm{e}^{-\sigma t}$ absolutamente integrable?

</li>

<li>

Calcula $S(p)$ directamente a partir de la integral. Dibuja el polo y la región de convergencia en el plano $p$.

</li>

<li>

¿Qué $\sigma$ puedes usar en la fórmula de inversión? La expresión $S(\mathrm{j}2\pi f)$ es finita. ¿Por qué, aun así, no puedes elegir $\sigma=0$, y qué señal se obtendría con $\sigma=0$? (Pista: [(2.3)](#gl-2-3).)

</li>

</ol>

:::loesung
(a) $\int_0^\infty\mathrm{e}^{2t}\mathrm{d} t=\infty$: la señal no es absolutamente integrable. Intuitivamente: con oscilaciones de amplitud constante no puede componerse nada que crezca.

(b) $|s(t)\mathrm{e}^{-\sigma t}|=\mathrm{e}^{(2-\sigma)t}$ para $t>0$, integrable si y solo si $\sigma>2/\mathrm s$.

(c) $S(p)=\int_0^\infty\mathrm{e}^{-(p-2)t}\mathrm{d} t=\dfrac{1}{p-2}$ para $\operatorname{Re} p>2$. Polo en $p=2$, región de convergencia a su derecha, como en toda señal por la derecha. Comprobación numérica: $S(3)=1$, $S(2{,}5+\mathrm{j})=0{,}4-0{,}8\mathrm{j}$.

(d) Cualquier $\sigma>2/\mathrm s$, por ejemplo $\sigma=3/\mathrm s$. $\sigma=0$ está a la izquierda del polo, es decir, fuera de la región de convergencia. La expresión $1/(\mathrm{j}2\pi f-2)$ es finita, pero corresponde a *otra* señal: según [(2.3)](#gl-2-3), también $-\mathrm{e}^{2t}\varepsilon(-t)$ tiene la transformada $1/(p-2)$, con región de convergencia $\operatorname{Re} p<2$. Con $\sigma=0$ se obtendría esta señal por la izquierda, que decae. Es la señal cuya transformada de Fourier es realmente $1/(\mathrm{j}2\pi f-2)$.
:::
:::

:::aufgabe Ejercicio 3a ★★ Qué ocurre en la frontera
<span class="anker" id="aufg-3a"></span>

$s(t)=\mathrm{e}^{(1+3\mathrm{j})t}\varepsilon(t)$, es decir, $b=-1-3\mathrm{j}$ ($t$ en s).

<ol class="al">

<li>

¿Para qué $\sigma$ converge $\int_0^\infty s(t)\,\mathrm{e}^{-pt}\mathrm{d} t$? ¿Qué papel desempeña el 3?

</li>

<li>

Toma $p=1+\mathrm{j}\omega$, es decir, justo sobre la frontera, y calcula $\int_0^T s(t)\,\mathrm{e}^{-pt}\mathrm{d} t$. ¿Qué ocurre para $T\to\infty$? Distingue $\omega\neq3$ y $\omega=3$. ¿Dónde está el polo?

</li>

</ol>

:::loesung
(a) $b+p=(\sigma-1)+\mathrm{j}(\omega-3)$ con $p=\sigma+\mathrm{j}\omega$. El módulo del integrando es $\mathrm{e}^{-(\sigma-1)t}$; la integral converge si y solo si $\sigma>1$. El 3 (la frecuencia angular de la señal) no aparece en el módulo. Solo determina dónde está el polo sobre la recta frontera: $S(p)=\frac{1}{p-(1+3\mathrm{j})}$, polo en $p=1+3\mathrm{j}$.

(b) Con $p=1+\mathrm{j}\omega$, $b+p=\mathrm{j}(\omega-3)$.

<ul>

<li>

$\omega\neq3$: $\displaystyle\int_0^T\mathrm{e}^{-\mathrm{j}(\omega-3)t}\mathrm{d} t=\frac{1-\mathrm{e}^{-\mathrm{j}(\omega-3)T}}{\mathrm{j}(\omega-3)}$. Al crecer $T$, el numerador gira sobre una circunferencia centrada en 1 y no se acerca a ningún valor. La integral permanece acotada, pero no tiene límite.

</li>

<li>

$\omega=3$, es decir, justo en el polo $p=1+3\mathrm{j}$: el integrando vale constantemente 1, la integral vale $T$ y crece sin límite.

</li>

</ul>

Así pues, sobre la recta frontera la integral no converge en ningún punto. La región de convergencia es el semiplano abierto $\operatorname{Re} p>1$.
:::
:::

:::aufgabe Ejercicio 4 ★ ¿Verdadero o falso? Con justificación
<span class="anker" id="aufg-4"></span>

<ol class="al">

<li>

Toda función tiene transformada de Laplace.

</li>

<li>

Que $p$ esté en la región de convergencia depende solo de $\operatorname{Re} p$.

</li>

<li>

Si el eje imaginario está en la región de convergencia, $S(\mathrm{j}2\pi f)$ es la transformada de Fourier de $s(t)$.

</li>

<li>

En la fórmula de inversión, $\sigma=1/\mathrm s$ da una señal distinta de la que da $\sigma=2/\mathrm s$ si ambos valores están en la región de convergencia.

</li>

<li>

$\cos(2\pi f_0t)$ es función propia de todo sistema LTI.

</li>

</ol>

:::loesung
(a) Falso. Contraejemplos: $\mathrm{e}^{t^2}\varepsilon(t)$, $\mathrm{e}^{|t|}$, la constante bilateral.

(b) Verdadero. $|s(t)\mathrm{e}^{-pt}|=|s(t)|\mathrm{e}^{-\sigma t}$; la frecuencia $f$ no aparece en el módulo. Por eso la región de convergencia está formada por rectas verticales completas.

(c) Verdadero. Con $\sigma=0$, $S(\mathrm{j}2\pi f)=\int s(t)\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t=\mathcal{F}\{s\}(f)$.

(d) Falso. Toda recta de la región de convergencia da la misma señal, porque el amortiguamiento $\mathrm{e}^{-\sigma t}$ y la compensación con $\mathrm{e}^{\sigma t}$ se anulan.

(e) Falso. La salida es $|H|\cos(2\pi f_0t+\varphi)$ con $H=H(\mathrm{j}2\pi f_0)$. Solo es un múltiplo de $\cos(2\pi f_0t)$ si $\varphi=0$ o $\varphi=\pi$, es decir, si $H(\mathrm{j}2\pi f_0)$ es real. Para el filtro paso bajo RC esto no ocurre a ninguna frecuencia $f_0>0$.
:::
:::

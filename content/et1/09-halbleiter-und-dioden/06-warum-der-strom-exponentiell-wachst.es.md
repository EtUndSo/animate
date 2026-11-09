---
title: Etapa 4: Por qué la corriente crece exponencialmente
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / Semiconductores y diodos
order: 1190600
summary: La barrera está ahí.
tags: corriente inversa de saturación, tensión térmica, década, resistencia de volumen
lang: es
---

<span class="anker" id="stufe-4"></span>

:::zweck
La barrera está ahí. Esta etapa aplica una tensión externa y muestra por qué la corriente crece exponencialmente en un sentido y se queda casi en cero en el otro.
:::

**La idea.** Una tensión externa $U$ entre el lado p (ánodo) y el lado n (cátodo) cae casi por completo en la zona, porque solo allí faltan portadores de carga. Las regiones neutras conducen bien. Por tanto, la barrera cambia a $W_\mathrm B=e(U_\mathrm{D0}-U)$ (fig. [5](#abb-5)). Por la zona pasan dos corrientes de electrones:

<ul>

<li>

⁠**Cuesta arriba:** electrones mayoritarios de la región n. Solo la fracción $\mathrm{e}^{-W_\mathrm B/(k_\mathrm BT)}$ supera la barrera. Cada $k_\mathrm BT$ menos de barrera la aumenta un factor 2,718.

</li>

<li>

⁠**Cuesta abajo:** electrones minoritarios de la región p que llegan al borde de la zona. Para ellos el escalón de potencial es una pendiente, y siempre pasan. Su número no depende de la barrera.

</li>

</ul>

Para los huecos ocurre lo mismo en sentido contrario. Sin tensión, ambas corrientes son iguales, por eso no circula nada.

:::abbildung et1/k9barriere 5
Energía de un electrón frente a la posición; puntos: electrones, cada fila más alta contiene menos (distribución esquemática, las proporciones reales son mucho más extremas). Rojo: electrones por encima de la barrera $W_\mathrm B$, que van hacia la izquierda. La flecha azul arriba a la izquierda es la corriente de la minoría cuesta abajo, siempre igual. Con $U=0$, ambas corrientes se anulan.
:::

:::satz Teorema 4.1 (Ecuación de Shockley)
<span class="anker" id="satz-4-1"></span>

Para el diodo ideal, con $U$ de ánodo a cátodo e $I$ de ánodo a cátodo, se cumple

<span class="anker" id="gl-4-1"></span>
$$I=I_\mathrm S\bigl(\mathrm{e}^{U/U_T}-1\bigr),\qquad U_T=\frac{k_\mathrm BT}{e}. \tag{4.1}$$
:::

⁠**Cómo leerlo:** $I_\mathrm S$ es la __corriente inversa de saturación__ (abreviado, corriente inversa), de $10^{-15}$ a $10^{-9}$ A según el área y el dopado. La __tensión térmica__ $U_T$ es la energía térmica $k_\mathrm BT$ en voltios, dividida por $e$; a 300 K son 25,85 mV. Importante: $k_\mathrm BT$ sola es una energía; solo $k_\mathrm BT/e$ es una tensión. El factor 10 (una __década__) cuesta $U_T\ln10=59{,}5$ mV, es decir, unos 60 mV. **Validez:** [(4.1)](#gl-4-1) vale para $U<U_\mathrm{D0}$ y sin ruptura (etapa [5](kennlinie-durchbruch-und-spezialdioden.html#stufe-5)). En sentido directo basta $I\approx I_\mathrm S\mathrm{e}^{U/U_T}$.

:::herleitung De la barrera a la curva característica
<ol>

<li>

Cuesta arriba: la corriente es proporcional a la fracción por encima de la barrera, $I_\text{sub}=c\,\mathrm{e}^{-(U_\mathrm{D0}-U)/U_T}=I_0\,\mathrm{e}^{U/U_T}$. Aquí $I_0=c\,\mathrm{e}^{-U_\mathrm{D0}/U_T}$ reúne todo lo que no depende de $U$.

</li>

<li>

Cuesta abajo: $I_\text{baj}$ no depende de $U$.

</li>

<li>

Con $U=0$ no circula corriente, así que $I_\text{baj}=I_0$. La corriente neta es $I=I_\text{sub}-I_\text{baj}=I_0(\mathrm{e}^{U/U_T}-1)$.

</li>

<li>

Electrones y huecos tienen la misma barrera, y sus corrientes se suman con el mismo factor: $I_0$ pasa a ser $I_\mathrm S$.

</li>

</ol>

Simplificación: en realidad, el valor de $I_\mathrm S$ lo determina la difusión de la minoría en las regiones neutras detrás de la zona. El factor $\mathrm{e}^{U/U_T}$ se mantiene, porque fija la densidad de portadores en el borde de la zona.
:::

::::beispiel
Con [(4.1)](#gl-4-1) se obtiene en el modelo de referencia:

| $I$ | 1 µ A | 10 µ A | 100 µ A | 1 mA | 10 mA |
|---|---|---|---|---|---|
| $U$ | 0,476 V | 0,536 V | 0,595 V | 0,655 V | 0,714 V |

A 0,655 V la barrera se ha reducido a $2{,}3\,U_T$, y la fracción ha subido de $10^{-12}$ a 0,1.
::::

⁠**Casos límite:** Con $U=0$, $I=0$. Para $U\ll-U_T$ queda $I=-I_\mathrm S$: ya a $-5\,U_T$ es el 99,3 % de ese valor. A partir de $U=119$ mV, el sumando $-1$ es menor que el 1 % del primero.

**Sentido inverso.** Con $U<0$ la barrera crece y la zona se ensancha. La corriente cuesta arriba se extingue y solo queda la corriente de la minoría. No depende de la altura de la barrera, solo de cuántos portadores llegan a su borde. Por eso se satura en $I_\mathrm S$. Los diodos reales bloquean con pA a nA, porque además se generan pares en la zona.

:::ltspice La curva característica del diodo del modelo de referencia
⁠**Esquema:** `voltage` llamada `V1` de `a` a masa, `diode` de `a` a masa, valor `DM`.

⁠**Directivas:** `.model DM D(Is=1e-14)` y `.dc V1 0 0.8 1m`

⁠**Lo que ves:** `I(D1)` parece empezar en 0,6 V. Pon el eje de corriente en escala logarítmica: se convierte en una recta. A 0,6547 V lees 0,98 mA, a 0,7142 V 9,8 mA, a 0,7737 V 98 mA. LTspice calcula a 27 °C, de ahí la desviación del 2 % respecto a 1, 10 y 100 mA. Comprueba así el ejercicio [4](#aufg-4)(a).
:::

:::frage ¿Qué ocurre si $U$ se hace mayor que $U_\mathrm{D0}$? ¿Desaparece entonces la barrera?
La fórmula ya no vale ahí. Con una corriente tan alta, los portadores que han superado la barrera son tan densos en la región ajena como el dopado, y las regiones neutras tienen una resistencia apreciable (__resistencia de volumen__, unos pocos $\Omega$). El resto de la tensión externa cae allí, y la curva característica se vuelve más plana y casi recta. La barrera nunca se hace negativa.
:::

:::zusatz Temperatura
$I_\mathrm S$ contiene $n_\mathrm i^2$ y crece alrededor de un factor 4 por cada 10 K. Esto supera el crecimiento de $U_T$: a corriente fija, la tensión baja unos 2 mV/K. Los diodos reales siguen a menudo $\mathrm{e}^{U/(mU_T)}$ con $1\le m\le2$.
:::

:::aufgabe Ejercicio 4 ★ Décadas
<span class="anker" id="aufg-4"></span>

<ol class="al">

<li>

El diodo del modelo de referencia muestra 0,655 V a 1 mA. Estima sin calculadora $U$ a 100 mA y a 10 µ A.

</li>

<li>

¿Cuántos mV sube $U$ si la corriente se duplica? ¿Y si se triplica?

</li>

<li>

¿Qué corriente circula con $U=-1$ V y con $U=-0{,}2$ V?

</li>

</ol>

:::loesung
(a) 100 mA son dos décadas más: $0{,}655\,\mathrm{V}+2\cdot0{,}060\,\mathrm{V}=0{,}775$ V (exacto 0,774 V). 10 µ A son dos décadas menos: 0,535 V (exacto 0,536 V). (b) Duplicar: $U_T\ln2=17{,}9$ mV. Triplicar: $U_T\ln3=28{,}4$ mV. (c) A $-1$ V, $\mathrm{e}^{U/U_T}\approx0$, así que $I=-10^{-14}$ A. A $-0{,}2$ V, $\mathrm{e}^{-7{,}7}=4{,}4\cdot10^{-4}$, así que también $I=-10^{-14}$ A con una precisión del 0,05 %.
:::
:::

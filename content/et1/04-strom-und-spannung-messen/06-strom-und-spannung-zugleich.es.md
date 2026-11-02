---
title: Etapa 5: Corriente y tensión a la vez
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / Medir corriente y tensión
order: 1140600
summary: Quien determina una resistencia a partir de R=U/I necesita ambos instrumentos.
tags: 
lang: es
---

<span class="anker" id="stufe-5"></span>

:::zweck
Quien determina una resistencia a partir de $R=U/I$ necesita ambos instrumentos. Uno de ellos queda entonces en el circuito de medida del otro. Esta etapa compara los dos circuitos posibles.
:::

**La idea.** El voltímetro puede conectarse antes o después del amperímetro (fig. [6](#abb-6)). Si está antes del amperímetro, el amperímetro cuenta exactamente la corriente por $R$, pero el voltímetro mide la tensión en $R$ y en el amperímetro juntos. Si está directamente en $R$, la tensión es correcta, pero el amperímetro cuenta también la corriente del voltímetro.

:::abbildung et1/k4richtig 6
Los dos circuitos de medida. En verde, la lectura correcta; en rojo, la lectura con la contribución del otro instrumento.
:::

:::definition Definición 5.1 (Medición de corriente correcta y de tensión correcta)
<span class="anker" id="satz-5-1"></span>

$U$ e $I$ son las lecturas; $U_R$ e $I_R$, los valores en la resistencia.

Corriente correcta: $I=I_R$, pero $U=U_R+U_\mathrm{iA}\neq U_R$. De ahí se deduce

<span class="anker" id="gl-5-1"></span>
$$\frac UI=R+R_\mathrm{iA},\qquad f=+\frac{R_\mathrm{iA}}{R}. \tag{5.1}$$

Tensión correcta: $U=U_R$, pero $I=I_R+I_\mathrm{iV}\neq I_R$. De ahí se deduce

<span class="anker" id="gl-5-2"></span>
$$\frac UI=R\parallel R_\mathrm{iV},\qquad f=-\frac{R}{R+R_\mathrm{iV}}. \tag{5.2}$$
:::

⁠**Cómo leerlo:** $U_\mathrm{iA}$ es la caída de tensión en el amperímetro; $I_\mathrm{iV}$, la corriente por el voltímetro. $f$ es el error de $U/I$ respecto a $R$. No es posible leer correctamente a la vez la corriente y la tensión en una resistencia. Pero si se conocen las resistencias internas, el resultado se puede corregir: $R=U/I-R_\mathrm{iA}$ o $1/R=I/U-1/R_\mathrm{iV}$, respectivamente.

:::herleitung Cociente de las lecturas
Corriente correcta: $U/I=(I_RR+I_RR_\mathrm{iA})/I_R=R+R_\mathrm{iA}$. Tensión correcta: $I/U=(I_R+I_\mathrm{iV})/U_R=1/R+1/R_\mathrm{iV}$, es decir, $U/I=R\parallel R_\mathrm{iV}$ y $f=(R\parallel R_\mathrm{iV})/R-1=-R/(R+R_\mathrm{iV})$.
:::

**Ejemplo.** El modelo de referencia en ambos circuitos:

|  | Lectura $U$ | Lectura $I$ | $U/I$ y error |
|---|---|---|---|
| corriente correcta | 9,000 V (en $R$: 8,950 V) | 4,972 mA | 1810 $\Omega$, $+0{,}56\,\%$ |
| tensión correcta | 8,950 V | 5,017 mA (por $R$: 4,972 mA) | 1783,9 $\Omega$, $-0{,}89\,\%$ |

La corrección por cálculo lleva en ambos casos de vuelta a 1800 $\Omega$.

**¿Qué circuito?** La fig. [7](#abb-7) muestra ambos errores en función de $R$. Las resistencias pequeñas se miden con el circuito de tensión correcta, porque su corriente supera con mucho la del voltímetro. Las grandes se miden con el circuito de corriente correcta, porque su tensión supera con mucho la caída en el amperímetro. Las curvas se cruzan cerca de 1,4 k$\Omega$ (ejercicio [6](#aufg-6)). Con 1,8 k$\Omega$, el circuito de corriente correcta es algo mejor.

:::abbildung et1/k4fehler 7
Valor absoluto del error relativo de $U/I$ para $R_\mathrm{iA}=10\,\Omega$ y $R_\mathrm{iV}=200$ k$\Omega$, ambos ejes logarítmicos. Los puntos corresponden al modelo de referencia.
:::

:::ltspice Los dos circuitos de medida
⁠**Esquema:** fuente `voltage` con 9 V en el nudo `q`. El amperímetro es un `res` con 10; el voltímetro, un `res` con 200k. Corriente correcta: `RA1` de `q` a `a`, `RX1` = 1.8k de `a` a masa, `RV1` de `q` a masa. Tensión correcta: `RA2` de `q` a `b`, `RX2` = 1.8k y `RV2` de `b` a masa.

⁠**Directivas:** `.op`

⁠**Lo que ves:** `I(RA1)` = 4,972 mA con `V(q)` = 9 V, es decir, 1810 $\Omega$. `I(RA2)` = 5,017 mA con `V(b)` = 8,950 V, es decir, 1783,9 $\Omega$. Introduce luego los valores del ejercicio [5](#aufg-5) y compara.
:::

:::frage ¿Por qué no medir una cosa tras otra, primero la corriente y luego la tensión?
Aquí eso no ayuda. Por sí solo en el circuito, el amperímetro vuelve a mostrar 4,972 mA; por sí solo en $R$, el voltímetro muestra 9,000 V. El resultado es 1810 $\Omega$, como en el circuito de corriente correcta: el error propio de cada instrumento permanece.
:::

**Medir resistencia sin amperímetro.** Por eso, un multímetro digital mide las resistencias de otra manera. Una fuente de corriente constante exacta (fuente de corriente con una corriente conocida y fija) hace pasar la corriente $I_\mathrm q$ por $R$, y solo se mide la tensión: $R=U/I_\mathrm q\propto U$. La corriente es una potencia de diez exacta, de modo que la indicación solo tiene que poner la coma y el prefijo (mili, kilo, mega): 1 mA en 1,8 k$\Omega$ da 1,800 V, que se muestra como 1,800 k$\Omega$. Queda el error $R/(R+R_\mathrm{iV})$, con 10 M$\Omega$, por tanto, 0,018 %. Con resistencias pequeñas molestan los cables de conexión: 0,1 $\Omega$ de cable sobre 0,5 $\Omega$ son un 20 %. Por eso, la medición Kelvin separa los caminos: dos cables llevan la corriente y otros dos toman la tensión directamente en el componente. Por estos no circula casi corriente, así que su resistencia no influye.

:::aufgabe Ejercicio 5 ★★ ¿Qué circuito?
<span class="anker" id="aufg-5"></span>

Instrumentos como en el modelo de referencia, rangos elegidos adecuadamente, resistencias internas sin cambios. Calcula $U/I$ y $f$ en ambos circuitos para (a) $R=100\,\Omega$ a 0,9 V y (b) $R=180$ k$\Omega$ a 9 V. (c) Demuestra que ambas fórmulas de corrección devuelven 1800 $\Omega$ en el modelo de referencia.

:::loesung
(a) Corriente correcta: $U/I=110\,\Omega$, $f=+10\,\%$. Tensión correcta: $U/I=100\,\Omega\parallel200\,\mathrm{k\Omega}=99{,}95\,\Omega$, $f=-0{,}05\,\%$.

(b) Corriente correcta: $U/I=180{,}01$ k$\Omega$, $f=+0{,}0056\,\%$. Tensión correcta: $U/I=180\,\mathrm{k\Omega}\parallel200\,\mathrm{k\Omega}=94{,}74$ k$\Omega$, $f=-47{,}4\,\%$: por el voltímetro circula casi tanta corriente como por $R$ (45 µ A frente a 50 µ A). Así pues, las pequeñas con tensión correcta y las grandes con corriente correcta.

(c) $1810\,\Omega-10\,\Omega=1800\,\Omega$ y $1/(1/1783{,}94\,\Omega-1/200\,\mathrm{k\Omega})=1800\,\Omega$.
:::
:::

:::aufgabe Ejercicio 6 ★★★ Mismo error
<span class="anker" id="aufg-6"></span>

¿Para qué $R$ son iguales en magnitud ambos errores? Calcula el valor exacto y demuestra que, para $R_\mathrm{iA}\ll R\ll R_\mathrm{iV}$, se cumple aproximadamente $R\approx\sqrt{R_\mathrm{iA}R_\mathrm{iV}}$.

:::loesung
$R_\mathrm{iA}/R=R/(R+R_\mathrm{iV})$ lleva a $R^2-R_\mathrm{iA}R-R_\mathrm{iA}R_\mathrm{iV}=0$, con la solución positiva

$$R=\frac{R_\mathrm{iA}}{2}+\sqrt{\frac{R_\mathrm{iA}^2}{4}+R_\mathrm{iA}R_\mathrm{iV}}=1419\,\Omega.$$

Para $R\ll R_\mathrm{iV}$, el miembro derecho se convierte en $R/R_\mathrm{iV}$, es decir, $R^2\approx R_\mathrm{iA}R_\mathrm{iV}$ y $R\approx1414\,\Omega$. Allí, ambos errores son de alrededor del 0,7 %.
:::
:::

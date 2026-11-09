---
title: Etapa 4: El cuadripolo en funcionamiento
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / Cuadripolos
order: 1160600
summary: En funcionamiento, ningún puerto está abierto.
tags: reacción, unilateral
lang: es
---

<span class="anker" id="stufe-4"></span>

:::zweck
En funcionamiento, ningún puerto está abierto. Esta etapa muestra cómo la carga actúa de vuelta sobre la entrada a través del parámetro $Z_{12}$ y qué es el cuadripolo para la carga.
:::

**La idea.** La carga toma una corriente del puerto 2, así que $I_2\neq0$. A través de la fuente $Z_{12}I_2$, esta corriente aparece como una tensión en la entrada. En el cuadripolo T se ve de forma palpable: una parte de la corriente que de otro modo circularía por $R_\mathrm{b}$ se desvía por $R_\mathrm{c}$ hacia la carga. En $R_\mathrm{b}$ cae menos, $U_1$ baja, y la entrada parece de menor resistencia. Esta acción de la salida sobre la entrada se llama __reacción__.

:::satz Teorema 4.1 (Resistencia de entrada y lado de salida)
<span class="anker" id="satz-4-1"></span>

Con la carga $Z_\mathrm{L}$ en el puerto 2 se cumple $U_2=-Z_\mathrm{L}I_2$ y

<span class="anker" id="gl-4-1"></span>
$$I_2=-\frac{Z_{21}}{Z_{22}+Z_\mathrm{L}}\,I_1,\qquad Z_1=\frac{U_1}{I_1}=Z_{11}-\frac{Z_{12}Z_{21}}{Z_{22}+Z_\mathrm{L}}. \tag{4.1}$$

Los casos límite son la resistencia de entrada en circuito abierto y en cortocircuito:

<span class="anker" id="gl-4-2"></span>
$$Z_{1,\mathrm{CA}}=Z_{11},\qquad Z_{1,\mathrm{CC}}=Z_{11}-\frac{Z_{12}Z_{21}}{Z_{22}}. \tag{4.2}$$

Si una fuente $U_\mathrm{q}$, $R_\mathrm{q}$ alimenta el puerto 1, el puerto 2 actúa como fuente de tensión equivalente ([Parte 5](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)) con

<span class="anker" id="gl-4-3"></span>
$$U_\mathrm{i}=\frac{Z_{21}}{Z_{11}+R_\mathrm{q}}\,U_\mathrm{q},\qquad R_\mathrm{i}=Z_{22}-\frac{Z_{12}Z_{21}}{Z_{11}+R_\mathrm{q}}. \tag{4.3}$$
:::

⁠**Cómo leerlo:** $Z_\mathrm{L}$ es la carga, aquí una resistencia. El signo menos de $U_2=-Z_\mathrm{L}I_2$ aparece porque $I_2$ apunta hacia el cuadripolo y, por tanto, en contra de la corriente por la carga. La fracción de [(4.1)](#gl-4-1) es la cantidad en que la carga cambia la resistencia de entrada. Si $Z_{12}=0$, es cero: la entrada no nota nada de la carga, y el cuadripolo se llama __unilateral__. **Validez:** El cuadripolo debe ser lineal; las fórmulas de la fuente equivalente suponen una fuente lineal.

:::herleitung Resistencia de entrada y lado de salida
Malla derecha: $U_2=Z_{21}I_1+Z_{22}I_2=-Z_\mathrm{L}I_2$; despejando $I_2$ se obtiene la primera parte de [(4.1)](#gl-4-1). Sustituyendo en la malla izquierda $U_1=Z_{11}I_1+Z_{12}I_2$ y dividiendo por $I_1$ resulta $Z_1$. Para $Z_\mathrm{L}\to\infty$ desaparece la fracción; para $Z_\mathrm{L}=0$ resulta $Z_{1,\mathrm{CC}}$ con $I_2=-Z_{21}I_1/Z_{22}$.

Para [(4.3)](#gl-4-3) se sustituye la carga. La fuente impone $U_1=U_\mathrm{q}-R_\mathrm{q}I_1$. Con $I_2=0$ es $I_1=U_\mathrm{q}/(Z_{11}+R_\mathrm{q})$ y $U_\mathrm{i}=Z_{21}I_1$. Con $U_\mathrm{q}=0$, el puerto 1 queda terminado por $R_\mathrm{q}$, y $R_\mathrm{i}$ es $Z_1$ con los índices intercambiados.
:::

:::abbildung et1/k6betrieb 5
Circuito equivalente del cuadripolo T con fuente y carga. Circulan $I_1=250$ mA e $I_2=-50$ mA. La reacción vale $Z_{12}I_2=-1$ V, y la fuente directa da $Z_{21}I_1=5$ V. La entrada muestra 31 $\Omega$ en lugar de 35 $\Omega$.
:::

::::beispiel
Para el cuadripolo T, $Z_{1,\mathrm{CA}}=35\,\Omega$ y $Z_{1,\mathrm{CC}}=35\,\Omega-400\,\Omega^2/40\,\Omega=25\,\Omega$, que es $R_\mathrm{a}+R_\mathrm{b}\parallel R_\mathrm{c}$. Con $R_\mathrm{L}=60\,\Omega$ resulta

$$Z_1=35\,\Omega-\frac{400\,\Omega^2}{100\,\Omega}=31\,\Omega,\quad I_1=\frac{9\,\mathrm{V}}{5\,\Omega+31\,\Omega}=250\,\mathrm{mA},\quad I_2=-\frac{20}{100}\,I_1=-50\,\mathrm{mA}.$$

En la entrada, $U_1=9\,\mathrm{V}-5\,\Omega\cdot250\,\mathrm{mA}=7{,}75$ V; en la salida, $U_2=60\,\Omega\cdot50\,\mathrm{mA}=3$ V. Por $R_\mathrm{b}$ circulan $I_1+I_2=200$ mA en lugar de 250 mA, lo que baja $U_1$ exactamente 1 V (fig. [5](#abb-5)). Visto desde la carga: $U_\mathrm{i}=\frac{20}{40}\cdot9\,\mathrm{V}=4{,}5$ V, $R_\mathrm{i}=40\,\Omega-400\,\Omega^2/40\,\Omega=30\,\Omega$. Entonces $I=4{,}5\,\mathrm{V}/90\,\Omega=50$ mA, la misma corriente. Así pues, la fuente equivalente de la [Parte 5](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html) está contenida en los cuatro números.
::::

⁠**Casos límite:** $R_\mathrm{L}\to\infty$ da $Z_1\to35\,\Omega$, $R_\mathrm{L}\to0$ da $25\,\Omega$. Toda carga queda en medio.

:::frage La carga solo está en el puerto 2. ¿Cómo se entera de ella la entrada?
Por los componentes comunes. En el cuadripolo T, ambos puertos pasan por $R_\mathrm{b}$, y su caída de tensión depende de $I_1+I_2$. En general, $Z_{12}$ es la medida de este acoplamiento. No hace falta ninguna transmisión de señal hacia atrás: las tensiones se establecen conjuntamente en la red.
:::

:::ltspice Cuadripolo T en funcionamiento
⁠**Esquema:** fuente `voltage` con `9` de `q` a masa, `res` con `5` de `q` a `1`, `Ra` con `15` de `1` a `m`, `Rb` con `20` de `m` a masa, `Rc` con `20` de `m` a `2`, `RL` con `{RL}` de `2` a masa.

⁠**Directivas:** `.param RL=60`, `.op`, `.meas op Uent FIND V(1)`, `.meas op Ient FIND I(Ra)`, `.meas op Zent PARAM Uent/Ient`, `.meas op Usal FIND V(2)`.

⁠**Lo que ves:** $\mathtt{V(1)}=7{,}75$ V, $\mathtt{I(Ra)}=250$ mA, `Zent` $=31\,\Omega$, $\mathtt{V(2)}=3$ V. Con `RL=1m`, `Zent` pasa a 25,0 $\Omega$; con `RL=1G`, a 35,0 $\Omega$ y $\mathtt{V(2)}=4{,}5$ V, la tensión $U_\mathrm{i}$. Pon `RL=10` y comprueba el ejercicio [4](#aufg-4)(a) y (c).
:::

:::aufgabe Ejercicio 4 ★★ La carga en el cuadripolo T
<span class="anker" id="aufg-4"></span>

<ol class="al">

<li>

¿Cuánto vale $Z_1$ para $R_\mathrm{L}=10\,\Omega$?

</li>

<li>

¿Con qué carga muestra la entrada $Z_1=30\,\Omega$?

</li>

<li>

Calcula para $R_\mathrm{L}=10\,\Omega$, con la fuente, las corrientes $I_1$, $I_2$ y $U_2$. Comprueba la corriente de carga con la fuente equivalente.

</li>

</ol>

:::loesung
(a) $Z_1=35\,\Omega-400\,\Omega^2/50\,\Omega=27\,\Omega$. (b) $400\,\Omega^2/(40\,\Omega+R_\mathrm{L})=5\,\Omega$, es decir, $R_\mathrm{L}=40\,\Omega$. (c) $I_1=9\,\mathrm{V}/32\,\Omega=281{,}25$ mA, $I_2=-\frac{20}{50}I_1=-112{,}5$ mA, $U_2=1{,}125$ V. La fuente equivalente da $4{,}5\,\mathrm{V}/(30\,\Omega+10\,\Omega)=112{,}5$ mA.
:::
:::

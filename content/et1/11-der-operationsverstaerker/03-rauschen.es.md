---
title: Etapa 1: Ruido
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / El amplificador operacional
order: 1210300
summary: Un sensor entrega milivoltios, y todo conductor genera una tensión perturbadora aleatoria.
tags: densidad de tensión de ruido, relación señal-ruido, decibelios, constante de Boltzmann, Ruido térmico, Ruido de disparo, Ruido 1/f, ruido blanco
lang: es
---

<span class="anker" id="stufe-1"></span>

:::zweck
Un sensor entrega milivoltios, y todo conductor genera una tensión perturbadora aleatoria. Esta etapa aclara de dónde viene, cómo se mide y qué puede hacer un amplificador contra ella.
:::

**La idea.** El ruido es una perturbación formada por muchas oscilaciones de distinta frecuencia y amplitud. Su evolución es aleatoria y solo se puede describir estadísticamente: la media es cero, y el valor eficaz mide su intensidad. Como las perturbaciones independientes unas veces se refuerzan y otras se anulan, no se suman sus valores eficaces, sino los cuadrados de estos. Por eso el ruido se describe mediante la __densidad de tensión de ruido__ $|u_\mathrm{r}(f)|^2$: la contribución de cada franja de frecuencia de 1 Hz de ancho al cuadrado del valor eficaz.

:::definition Definición 1.1 (Ruido)
<span class="anker" id="satz-1-1"></span>

El valor eficaz de la tensión de ruido y la densidad del ruido térmico de una resistencia son

<span class="anker" id="gl-1-1"></span>
$$u_\mathrm{r,eff}=\sqrt{\int_0^\infty|u_\mathrm{r}(f)|^2\,\mathrm{d} f},\qquad |u_\mathrm{r,R}(f)|^2=4\,k_\mathrm{B}\,T\,R. \tag{1.1}$$

La __relación señal-ruido__ es el cociente de las potencias, escrito en __decibelios__ (dB):

<span class="anker" id="gl-1-2"></span>
$$\mathrm{SNR}=\frac{P_\mathrm{s}}{P_\mathrm{r}}=\Bigl(\frac{u_\mathrm{s,eff}}{u_\mathrm{r,eff}}\Bigr)^2,\qquad \mathrm{SNR}_\mathrm{dB}=10\lg\frac{P_\mathrm{s}}{P_\mathrm{r}}=20\lg\frac{u_\mathrm{s,eff}}{u_\mathrm{r,eff}}. \tag{1.2}$$
:::

⁠**Cómo leerlo:** $[|u_\mathrm{r}|^2]=\mathrm{V^2/Hz}$. $k_\mathrm{B}=1{,}381\cdot10^{-23}$ J/K es la __constante de Boltzmann__: convierte temperatura en energía térmica media por partícula. $T$ es la temperatura absoluta en K; $R$, la resistencia. $\lg$ es el logaritmo decimal. 20 dB significan un factor 10 en tensión y 100 en potencia. **Validez:** La parte derecha de [(1.1)](#gl-1-1) vale hasta mucho más allá de las frecuencias de la electrónica.

| Tipo | Mecanismo | Densidad |
|---|---|---|
| __Ruido térmico__ | Movimiento térmico de los portadores de carga en todo conductor. Las acumulaciones aleatorias en los extremos producen una tensión, incluso sin corriente. | constante, $\sim T\,R$ |
| __Ruido de disparo__ | La corriente consta de cargas individuales que cruzan una barrera de potencial en instantes aleatorios, por ejemplo en la unión pn. | constante |
| __Ruido 1/f__ | Recarga de estados superficiales, número fluctuante de portadores libres en el semiconductor. | $\sim1/f$, molesta hasta unos 10 kHz |

Una densidad constante se llama __ruido blanco__, por la luz blanca, compuesta de todos los colores. Es una forma del espectro, no una causa. Integrada sobre todas las frecuencias daría una potencia infinita. Eso es un límite del modelo: las densidades reales caen a frecuencias muy altas, y todo circuito tiene un __ancho de banda__ $\Delta f$ finito, el rango de frecuencias que deja pasar. Para el ruido blanco, la integral se convierte en $u_\mathrm{r,eff}=\sqrt{|u_\mathrm{r}|^2\,\Delta f}$.

:::abbildung et1/k11rauschen 1
A la izquierda, la densidad de una resistencia de 10 k$\Omega$ con una componente 1/f por debajo de 1 kHz: plana por encima (blanca), creciente por debajo. A la derecha, la misma señal útil sin ruido y con ruido a 20 dB, es decir, a una décima parte de su valor eficaz.
:::

:::herleitung Por qué se suman los cuadrados
Para dos perturbaciones independientes, $(u_1+u_2)^2=u_1^2+2u_1u_2+u_2^2$. En la media temporal, el producto $u_1u_2$ es positivo tan a menudo como negativo, y su media se anula. Queda $u_\mathrm{tot,eff}^2=u_\mathrm{1,eff}^2+u_\mathrm{2,eff}^2$. La integral de [(1.1)](#gl-1-1) es esta suma sobre todas las franjas de frecuencia.
:::

::::beispiel
La resistencia del sensor tiene $|u_\mathrm{r,R}|^2=4\cdot1{,}381\cdot10^{-23}\cdot300\cdot10^4=1{,}66\cdot10^{-16}\,\mathrm{V^2/Hz}$; en 20 kHz, por tanto, $u_\mathrm{r,eff}=1{,}82$ µ V. La señal útil de 1 mV es 549 veces mayor: $\mathrm{SNR}=54{,}8$ dB. La mitad del ancho de banda reduce el ruido en un factor $\sqrt2$, es decir, 3 dB.
::::

⁠**Casos límite:** Para $R\to0$ o $T\to0$ desaparece el ruido térmico.

**Qué cambia un amplificador.** Eleva la señal y el ruido presente en su entrada en el mismo factor, así que la SNR sigue igual o empeora por su ruido propio. Solo ayuda contra las perturbaciones que se añaden *detrás* de él y tienen un tamaño fijo. Si la línea hasta el siguiente aparato añade 100 µ V, sin amplificador quedan 20,0 dB. Con una ganancia de 100 en el sensor son $0{,}1\,\mathrm{V}/\sqrt{(182\,\mathrm{\mu\text{} V})^2+(100\,\mathrm{\mu\text{} V})^2}$, es decir, 53,7 dB. El segundo recurso es la diferencia: una perturbación que afecta por igual a dos líneas desaparece si solo se evalúa su diferencia. Eso lo consigue la etapa [2](der-differenzverstarker.html#stufe-2).

:::aufgabe Ejercicio 1 ★★ Ruido térmico
<span class="anker" id="aufg-1"></span>

(a) ¿Cuánto vale el ruido de 47 k$\Omega$ en 10 kHz a 300 K, y cuánto a 77 K? (b) Detrás de los 47 k$\Omega$ hay 53 k$\Omega$ en serie. Suma correctamente ambas tensiones de ruido y compara con una sola resistencia de 100 k$\Omega$. (c) Una señal de 200 µ V con el ruido de (a) pasa por una línea que añade 50 µ V. ¿Cuánto vale la SNR sin y con una ganancia de 1000 antes de la línea?

:::loesung
(a) $u_\mathrm{r,eff}=\sqrt{4k_\mathrm{B}\cdot300\,\mathrm{K}\cdot47\,\mathrm{k\Omega}\cdot10\,\mathrm{kHz}}=2{,}79$ µ V; a 77 K, menor en un factor $\sqrt{77/300}$: 1,41 µ V. (b) 53 k$\Omega$ dan 2,96 µ V. Las perturbaciones independientes se suman cuadráticamente: $\sqrt{2{,}79^2+2{,}96^2}\,\mu\text{V}=4{,}07$ µ V, exactamente el valor de 100 k$\Omega$. La suma lineal 5,75 µ V sería incorrecta. (c) Sin amplificador: $200/\sqrt{2{,}79^2+50^2}=4{,}0$, es decir, 12,0 dB. Con ganancia 1000: $200\,\mathrm{mV}/\sqrt{(2{,}79\,\mathrm{mV})^2+(0{,}05\,\mathrm{mV})^2}=71{,}7$, es decir, 37,1 dB. Es casi la SNR en la entrada; la línea ya no importa.
:::
:::

---
title: Etapa 10: Dónde terminan las reglas
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / El amplificador operacional
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-operationsverstarker
knoten: Capítulo 11: El amplificador operacional
order: 1211200
summary: Hasta aquí, el AO era ideal salvo por A y los topes.
tags: Tensión de offset, Corriente de polarización de entrada, rechazo de modo común, frecuencia de transición, velocidad de subida, sobreexcitado
lang: es
---

<span class="anker" id="stufe-10"></span>

:::zweck
Hasta aquí, el AO era ideal salvo por $A$ y los topes. Esta etapa ordena las desviaciones reales por tamaño y resume el procedimiento.
:::

**La idea.** Las desviaciones reales actúan por dos vías. Unas desplazan el punto hacia el que regula el lazo: los transistores T1 y T2 nunca son exactamente iguales, así que el punto de reposo no es $U_\mathrm{D}=0$, sino $U_\mathrm{D}=U_\mathrm{off}$. Las otras reducen la reserva $A\beta$. Sobre todo la frecuencia: para que el lazo no oscile, una capacidad interna limita el ancho de banda. La tensión en ella no puede seguir a las señales rápidas, y $A$ cae.

| Magnitud | Causa | Efecto en el modelo de referencia |
|---|---|---|
| $A$ finito, de $10^5$ a $10^6$ | Ganancia de etapa limitada | Desviación $1/(A\beta)=0{,}005$ % |
| __Tensión de offset__ $U_\mathrm{off}$ | Transistores de entrada desiguales; cambia con la temperatura, la alimentación y la edad | En la salida $U_\mathrm{off}/\beta=5$ mV, también con $U_\mathrm{E}=0$ |
| __Corriente de polarización de entrada__ $I_\mathrm{B}$ | Corrientes de base de T1 y T2 | Por $R_2$: $I_\mathrm{B}R_2=2$ mV |
| Modo común | Fuente de corriente real T3, ramas desiguales | véase abajo |
| $A(f)$ | Capacidad interna | $\vert A(f)\vert \approx f_\mathrm{T}/f$, véase abajo |
| Salida | Transistores de la etapa de salida | $\pm11$ V, 20 mA, $r_\mathrm{a}/(1+A\beta)=3{,}75$ m$\Omega$ |
| Ruido | Transistores propios | 10 nV/$\sqrt{\text{Hz}}$: 1,41 µ V en 20 kHz |

El offset es la tensión de entrada con la que la salida se hace cero. En el lazo se establece $\varphi_+-\varphi_-=U_\mathrm{off}$, y el divisor lo amplía en $1/\beta$. El ruido propio del AO se suma cuadráticamente al del sensor de la etapa [1](rauschen.html#stufe-1): 2,31 µ V en lugar de 1,82 µ V, y la SNR baja 2,1 dB hasta 52,7 dB.

:::definition Definición 10.1 (Rechazo de modo común)
<span class="anker" id="satz-10-1"></span>

El __rechazo de modo común__ CMRR (common mode rejection ratio) compara la ganancia de la diferencia con la del modo común:

<span class="anker" id="gl-10-1"></span>
$$\mathrm{CMRR}=\frac{A}{A_\mathrm{mc}},\qquad \mathrm{CMRR}_\mathrm{dB}=20\lg\frac{A}{A_\mathrm{mc}}. \tag{10.1}$$

Lo ideal es $\mathrm{CMRR}\to\infty$; lo habitual son de 60 dB ($A_\mathrm{mc}/A=10^{-3}$) a 120 dB ($10^{-6}$).
:::

⁠**Cómo leerlo:** Mecanismo: un T3 real tiene una $r_\mathrm{CE}$ finita. Si sube el modo común, sube E, y la corriente total crece en $U_\mathrm{mc}/r_\mathrm{CE}$. En el amplificador diferencial de la etapa [2](der-differenzverstarker.html#stufe-2), con $r_\mathrm{CE}=40$ k$\Omega$, cada colector cambia con el factor $R_\mathrm{C}/(2r_\mathrm{CE})=0{,}0375$ frente a 57,7 para la diferencia: 63,7 dB. En el modelo de referencia son 90 dB, es decir, $A_\mathrm{mc}=3{,}16$. En el restador de la etapa [6](mehrere-eingange-mehrere-stufen.html#stufe-6), 2 V de modo común actúan como $2\,\mathrm{V}/31600=63$ µ V de diferencia, que son 0,32 mV en la salida, el 0,16 % de los 0,2 V medidos.

**La frecuencia.** Por encima de $f_A=f_\mathrm{T}/A=10$ Hz, $A$ cae un factor 10 por década, $|A(f)|\approx f_\mathrm{T}/f$. A la __frecuencia de transición__ $f_\mathrm{T}$ es $|A|=1$. El lazo actúa mientras $|A(f)|\,\beta\gg1$. La reserva se agota en $f_G=\beta\,f_\mathrm{T}$:

<span class="anker" id="gl-10-2"></span>
$$|G(f)|=\frac{1/\beta}{\sqrt{1+(f/f_G)^2}},\qquad f_G=\beta\,f_\mathrm{T},\qquad G\,f_G=f_\mathrm{T}. \tag{10.2}$$

⁠**Cómo leerlo:** Con $G=5$, el ancho de banda llega hasta 200 kHz. El producto de ganancia y ancho de banda es fijo: con $G=1$ serían 1 MHz; con $G=100$, solo 10 kHz. La constante de tiempo $\tau_G=0{,}80$ µ s de la etapa [4](gegenkopplung.html#stufe-4) es el mismo valor: $1/(2\pi\cdot200\,\mathrm{kHz})$. **Caso límite:** Para $f\gg f_G$ es $|G|\to|A|$; la realimentación ya no actúa.

:::abbildung et1/k11bode 12
Ganancia en lazo abierto y ganancia del circuito en función de la frecuencia, ambos ejes logarítmicos. La distancia entre las curvas es la reserva $|A|\beta$. A 1 kHz es todavía 200, y a 200 kHz se ha agotado.
:::

:::ltspice Ancho de banda y enclavamiento
⁠**Esquema:** Símbolo `UniversalOpAmp2` (carpeta OpAmps) con `Avol=100k GBW=1Meg Slew=0.5Meg`, `Ilimit=20m Rail=1`, alimentación `voltage` $\pm12$. Conexionado como en el recuadro de la etapa [4](gegenkopplung.html#stufe-4), `VE` con `AC 1`.

⁠**Directivas:** `.ac dec 50 1 10Meg`, `.meas ac g0 FIND mag(V(a)) AT=10`, `.meas ac fg WHEN mag(V(a))=g0/sqrt(2)`.

⁠**Lo que ves:** `fg` = 199 kHz frente a 200 kHz en el cálculo. Intercambia después las entradas, da a `VE` el valor `PULSE(-3 3 1m 1u 1u 1m 2m)` y ejecuta `.tran 4m`: `V(a)` salta entre $\pm10{,}98$ V. Con $\pm1$ V en lugar de $\pm3$ V, la salida se queda quieta; esa es la histéresis de la etapa [9](mitkopplung-und-der-schmitt-trigger.html#stufe-9). Para el ejercicio [11](#aufg-11), pon `R1` a 1k y `R2` a 100k.
:::

:::zusatz Velocidad de subida
La corriente interna de carga está limitada. Por eso la salida tiene una velocidad máxima, la __velocidad de subida__, típicamente 0,5 V/µ s. El escalón de la fig. [5](gegenkopplung.html#abb-5) tarda así en realidad unos 10 µ s en lugar de pocos µ s. Un seno de 11 V de amplitud solo se mantiene sin distorsión hasta unos 7,2 kHz, aunque el ancho de banda es mucho mayor.
:::

:::merke El esquema de cálculo
<ol>

<li>

⁠**Sin realimentación** (comparador): $U_\mathrm{A}=U_\mathrm{A,max}$ o $U_\mathrm{A,min}$, $U_\mathrm{D}\ne0$.

</li>

<li>

⁠**Comprobar el signo:** Sube mentalmente la salida. Si $U_\mathrm{D}$ baja, es realimentación negativa; si sube, positiva.

</li>

<li>

⁠**Realimentación negativa:** Supón $U_\mathrm{D}=0$ y calcula $U_\mathrm{A}$ con la ley de los nudos y la ley de Ohm. Si está dentro de los límites, el cálculo es válido. Si no, el AO está __sobreexcitado__: $U_\mathrm{A}$ está en el tope, $U_\mathrm{D}\ne0$, y se calcula la red con ese $U_\mathrm{A}$ fijo.

</li>

<li>

⁠**Realimentación positiva:** Por lo general, $U_\mathrm{A}$ en el tope, $U_\mathrm{D}\ne0$. Los umbrales se siguen del cambio de signo de $U_\mathrm{D}$.

</li>

<li>

⁠**Precisión:** $1/(A\beta)$ a la frecuencia de la señal, $U_\mathrm{off}/\beta$ e $I_\mathrm{B}R_2$ en la salida.

</li>

</ol>
:::

:::aufgabe Ejercicio 11 ★★★ Amplificador de medida
<span class="anker" id="aufg-11"></span>

Un sensor de 10 mV debe amplificarse con V hasta alrededor de 1 V: $R_1=1$ k$\Omega$, $R_2=100$ k$\Omega$, no inversor. (a) ¿Cuánto valen $\beta$, $G$ y la desviación debida a $A$? (b) ¿Hasta qué frecuencia llega el circuito? ¿Cuánto vale $|G|$ a 5 kHz? (c) ¿Cuánto vale el offset en la salida y qué parte de la señal representa? ¿Cuánto añade $I_\mathrm{B}$? (d) ¿Hasta qué entrada llega la salida? (e) Un integrador con $R\,C=10$ ms tiene el mismo offset. ¿A qué velocidad se mueve su salida con $U_\mathrm{E}=0$ y cuándo llega al tope?

:::loesung
(a) $\beta=1/101$, $G\approx101$, desviación $101/A=0{,}10$ %. (b) $f_G=1\,\mathrm{MHz}/101=9{,}9$ kHz. $|G(5\,\mathrm{kHz})|=101/\sqrt{1+(5/9{,}9)^2}=90{,}2$. Un circuito así pierde ya una décima parte a 5 kHz. (c) $101\cdot1\,\mathrm{mV}=101$ mV, es decir, el 10 % de la señal de 1,01 V. A esto se añaden $I_\mathrm{B}R_2=5$ mV. (d) $11\,\mathrm{V}/101=109$ mV. (e) $1\,\mathrm{mV}/10\,\mathrm{ms}=0{,}1$ V/s; en el tope tras 110 s. Por eso, un integrador real necesita un interruptor de reinicio o una resistencia grande en paralelo con $C$.
:::
:::

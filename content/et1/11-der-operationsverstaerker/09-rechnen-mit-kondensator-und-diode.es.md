---
title: Etapa 7: Calcular con condensador y diodo
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / El amplificador operacional
order: 1210900
summary: Hasta ahora, una resistencia convertía tensión en corriente y otra corriente en tensión.
tags: 
lang: es
---

<span class="anker" id="stufe-7"></span>

:::zweck
Hasta ahora, una resistencia convertía tensión en corriente y otra corriente en tensión. Esta etapa utiliza otros componentes sin cambiar la regla. De ahí viene el nombre del AO: realiza operaciones de cálculo.
:::

**La idea.** Si la entrada positiva está a masa, la ley de los nudos en la entrada negativa dice: la corriente del componente de entrada circula íntegramente por el componente de realimentación, $I_\mathrm{ent}=-I_\mathrm{rea}$. El componente de entrada ve $U_\mathrm{E}$ y entrega una corriente. El componente de realimentación ve $U_\mathrm{A}$ y tiene que conducir esa misma corriente. Qué función resulta lo fija únicamente su ley de corriente y tensión (fig. [9](#abb-9)).

:::satz Teorema 7.1 (Operaciones)
<span class="anker" id="satz-7-1"></span>

Con la entrada positiva a masa y un AO ideal se cumple

<span class="anker" id="gl-7-1"></span>
<span class="anker" id="gl-7-2"></span>
<span class="anker" id="gl-7-3"></span>
<span class="anker" id="gl-7-4"></span>
$$\begin{aligned} \text{Integrador: }&u_\mathrm{A}(t)=u_\mathrm{A}(0)-\frac{1}{R\,C}\int_0^t u_\mathrm{E}(t')\,\mathrm{d} t', \\ \text{Derivador: }&u_\mathrm{A}(t)=-R\,C\,\frac{\mathrm{d} u_\mathrm{E}}{\mathrm{d} t}, \\ \text{Amplificador logarítmico: }&U_\mathrm{A}=-U_T\,\ln\frac{U_\mathrm{E}}{R\,I_\mathrm{S}}, \\ \text{Amplificador exponencial: }&U_\mathrm{A}=-R\,I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{E}/U_T}. \end{aligned} \tag{7.1|7.2|7.3|7.4}$$
:::

⁠**Cómo leerlo:** $R\,C$ es una constante de tiempo en s; $I_\mathrm{S}$, la corriente inversa de saturación del diodo; $U_T=26$ mV. **Validez:** [(7.3)](#gl-7-3) exige $U_\mathrm{E}>0$ y $U_\mathrm{E}/R\gg I_\mathrm{S}$, [(7.4)](#gl-7-4) exige $U_\mathrm{E}\gg U_T$, y todas exigen una salida dentro de sus límites.

:::herleitung Cuatro leyes de los nudos
Integrador: por $R$ circula $i=u_\mathrm{E}/R$. Carga el condensador, $C\,\mathrm{d} u_C/\mathrm{d} t=i$. La placa izquierda está fija en 0, así que $u_\mathrm{A}=-u_C$. Derivador: $i=C\,\mathrm{d} u_\mathrm{E}/\mathrm{d} t$ por el condensador de la entrada, $u_\mathrm{A}=-R\,i$. Amplificador logarítmico: $I=U_\mathrm{E}/R$ circula por el diodo, así que $I=I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{F}/U_T}$ con la tensión de diodo $U_\mathrm{F}=-U_\mathrm{A}$. Despejando se obtiene [(7.3)](#gl-7-3). Amplificador exponencial: $U_\mathrm{E}$ está aplicada al diodo, y su corriente $I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{E}/U_T}$ circula por $R$.
:::

:::abbildung et1/k11bauteile 9
Cuatro circuitos, una regla: el componente de la izquierda convierte la tensión de entrada en una corriente, y el de arriba exige para ella una tensión de salida. Los nudos están a masa virtual.
:::

::::beispiel [Ejemplos]
⁠*Integrador* con $R=10$ k$\Omega$, $C=10$ nF, es decir, $R\,C=100$ µ s. Con $U_\mathrm{E}=1$ V circula una corriente fija de 100 µ A. A diferencia del circuito RC de la [Parte 3](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator/der-kondensator.html), no disminuye durante la carga, porque la tensión en $R$ sigue siendo 1 V. $u_\mathrm{A}$ cae uniformemente 10 V/ms y alcanza $-11$ V tras 1,1 ms. Una onda cuadrada de $\pm1$ V a 1 kHz se convierte en una onda triangular de $\pm2{,}5$ V. *Derivador* con el mismo $R\,C$: una onda triangular de $\pm1$ V a 1 kHz sube 4 V/ms, y $u_\mathrm{A}$ se convierte en una onda cuadrada de $\pm0{,}4$ V. Para un seno, su módulo crece con la frecuencia, $\hat u_\mathrm{A}/\hat u_\mathrm{E}=2\pi f\,R\,C$: 0,63 a 1 kHz, 62,8 a 100 kHz. Por eso amplifica especialmente el ruido de alta frecuencia (etapa [1](rauschen.html#stufe-1)). *Amplificador logarítmico* con $R=10$ k$\Omega$ e $I_\mathrm{S}=1{,}9\cdot10^{-13}$ A: 0,1 V, 1 V, 10 V dan $-0{,}462$ V, $-0{,}522$ V, $-0{,}582$ V. Cada década (factor 10) aporta $U_T\ln10=59{,}9$ mV. *Amplificador exponencial* con los mismos valores: 0,5 V dan $-0{,}427$ V, y cada 18 mV más duplican el módulo.
::::

⁠**Casos límite:** $u_\mathrm{E}=0$ deja quieto al integrador, que mantiene $u_\mathrm{A}(0)$. Con $U_\mathrm{E}<0$ el diodo del amplificador logarítmico bloquea, la realimentación se interrumpe y la salida va al tope: la regla solo vale mientras el camino de vuelta conduzca.

**Multiplicar.** Como $\ln x+\ln y=\ln(x\,y)$, una cadena multiplica de forma analógica: dos amplificadores logarítmicos, un sumador, un amplificador exponencial. En la salida aparece, salvo un factor fijo, el producto $U_x\,U_y$. Como $U_T$ e $I_\mathrm{S}$ dependen de la temperatura, en la práctica los diodos se sustituyen por transistores con compensación de temperatura adicional. Antes de los ordenadores digitales, estos circuitos formaban máquinas de calcular; de ahí el nombre amplificador operacional.

:::aufgabe Ejercicio 7 ★★ Integrador
<span class="anker" id="aufg-7"></span>

$R=100$ k$\Omega$, $C=10$ nF, $u_\mathrm{A}(0)=0$. (a) ¿Cuánto vale $R\,C$? ¿Dónde está $u_\mathrm{A}$ tras 10 ms con $U_\mathrm{E}=-0{,}2$ V? (b) ¿Cuándo llega la salida al tope? (c) Se aplica una onda cuadrada de $\pm0{,}5$ V a 100 Hz. ¿Qué amplitud tiene la onda triangular? ¿Qué ocurre a 20 Hz?

:::loesung
(a) $R\,C=1$ ms. $u_\mathrm{A}$ sube a 200 V/s, hasta $+2$ V tras 10 ms. (b) Tras $11\,\mathrm{V}/(200\,\mathrm{V/s})=55$ ms. (c) Un semiperiodo de 5 ms cambia $u_\mathrm{A}$ en 2,5 V; la amplitud es 1,25 V. A 20 Hz, la excursión es de 12,5 V. Con $u_\mathrm{A}(0)=0$ y un comienzo positivo, la onda triangular alcanza $-11$ V y llega al tope.
:::
:::

:::aufgabe Ejercicio 8 ★★ Amplificador logarítmico
<span class="anker" id="aufg-8"></span>

$R=1$ k$\Omega$, $I_\mathrm{S}=1{,}9\cdot10^{-13}$ A. (a) Calcula $U_\mathrm{A}$ para 1 V y 2 V. Predice la diferencia sin usar $I_\mathrm{S}$. (b) ¿Qué recorrido tiene $U_\mathrm{A}$ cuando $U_\mathrm{E}$ va de 10 mV a 10 V? (c) A 330 K en lugar de 300 K, $U_T=28{,}6$ mV. ¿Cuánto desplaza esto por sí solo $U_\mathrm{A}$ con una corriente de 100 µ A?

:::loesung
(a) 1 mA da $-0{,}582$ V; 2 mA dan $-0{,}600$ V. La diferencia es $U_T\ln2=18$ mV, sin $I_\mathrm{S}$. (b) Tres décadas: $3\cdot59{,}9\,\mathrm{mV}=180$ mV. (c) $U_\mathrm{F}$ crece de 0,522 V a 0,574 V, es decir, 52 mV. En realidad también $I_\mathrm{S}$ sube mucho; por eso hace falta la compensación de temperatura.
:::
:::

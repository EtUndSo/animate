---
title: Etapa 4: Autocorrelación, covarianza y correlación cruzada
pfad: Ingeniería eléctrica / 3.er semestre / ET3 – Fundamentos de ingeniería eléctrica 3: señales y sistemas / Señales aleatorias
adresse: elektrotechnik/3-semester/signale-und-systeme/zufallssignale
knoten: Capítulo 7: Señales aleatorias
order: 3270500
summary: ¿Con qué rapidez cambia una señal aleatoria?
tags: función de autocovarianza
lang: es
---

<span class="anker" id="stufe-4"></span>

:::zweck
¿Con qué rapidez cambia una señal aleatoria? Lo dice la FAC: cuánto se parece todavía la señal a sí misma al cabo del tiempo $\tau$.
:::

:::satz Teorema 4.1 (Propiedades de la FAC de procesos estacionarios)
<span class="anker" id="satz-4-1"></span>

<span class="anker" id="gl-4-1"></span>
$$\varphi_{ss}(0)=L_s,\qquad\varphi_{ss}(\tau)=\varphi_{ss}(-\tau),\qquad|\varphi_{ss}(\tau)|\le\varphi_{ss}(0). \tag{4.1}$$

Para procesos ergódicos, $\varphi_{ss}(\tau)=\overline{s(t)s(t+\tau)}$, es decir, la FAC de una señal de potencia del [capítulo 6](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen/korrelationsfunktionen.html).
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

---
title: Etapa 8: Señal aleatoria y sistema LTI, densidad espectral
pfad: Ingeniería eléctrica / 3.er semestre / ET3 – Fundamentos de ingeniería eléctrica 3: señales y sistemas / Señales aleatorias
adresse: elektrotechnik/3-semester/signale-und-systeme/zufallssignale
knoten: Capítulo 7: Señales aleatorias
order: 3270900
summary: ¿Qué hace un sistema LTI con una señal aleatoria?
tags: densidad espectral de potencia
lang: es
---

<span class="anker" id="stufe-8"></span>

:::zweck
¿Qué hace un sistema LTI con una señal aleatoria? Cada función muestra se convoluciona. Por eso, para los valores medios rigen reglas sencillas.
:::

**Valor medio.** Para cada función muestra, ${}^kg={}^ks*h$. El valor esperado es lineal y puede entrar en la integral de convolución:

<span class="anker" id="gl-8-1"></span>
$$m_g=\mathrm E\Bigl\{\int s(\tau)h(t-\tau)\mathrm{d}\tau\Bigr\}=\int\mathrm E\{s(\tau)\}\,h(t-\tau)\,\mathrm{d}\tau=m_s\int h\,\mathrm{d}\tau=m_s\,H(0). \tag{8.1}$$

El valor medio se transmite como una componente continua.

:::satz Teorema 8.1 (Wiener-Lee para procesos estacionarios)
<span class="anker" id="satz-8-1"></span>

<span class="anker" id="gl-8-2"></span>
$$\varphi_{gg}(\tau)=\varphi_{ss}(\tau)*\varphi^E_{hh}(\tau),\qquad\Phi_{gg}(f)=\Phi_{ss}(f)\,|H(f)|^2, \tag{8.2}$$

con la FAC de energía $\varphi^E_{hh}(\tau)=\int h(\vartheta)h(\vartheta+\tau)\mathrm{d}\vartheta$ de la respuesta al impulso y la __densidad espectral de potencia__ $\Phi_{ss}(f)\;\bullet\!\!-\!\!\circ\;\varphi_{ss}(\tau)$. La potencia es

<span class="anker" id="gl-8-3"></span>
$$L_s=\varphi_{ss}(0)=\int_{-\infty}^{\infty}\Phi_{ss}(f)\,\mathrm{d} f. \tag{8.3}$$
:::

:::herleitung Wiener-Lee
Escribir las dos integrales de convolución, con variables distintas:

$$g(t)g(t+\tau)=\iint s(t-\alpha)\,s(t+\tau-\beta)\,h(\alpha)h(\beta)\,\mathrm{d}\alpha\,\mathrm{d}\beta.$$

Llevar el valor esperado dentro de la integral doble. Por la estacionariedad, $\mathrm E\{s(t-\alpha)s(t+\tau-\beta)\}=\varphi_{ss}(\tau-\beta+\alpha)$. Con $\vartheta=\beta-\alpha$:

$$\varphi_{gg}(\tau)=\int\varphi_{ss}(\tau-\vartheta)\underbrace{\int h(\alpha)h(\alpha+\vartheta)\,\mathrm{d}\alpha}_{\varphi^E_{hh}(\vartheta)}\,\mathrm{d}\vartheta=\varphi_{ss}*\varphi^E_{hh}.$$

En el dominio de la frecuencia, $\varphi^E_{hh}$ se convierte en $|H|^2$ ([capítulo 6](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen/korrelationsfunktionen.html)).
:::

⁠**Cómo leerlo:** $\Phi_{ss}(f)$ indica cómo se reparte la potencia entre las frecuencias. Es real, nunca negativa y, en las señales reales, par. Un sistema LTI multiplica la potencia en cada frecuencia por $|H(f)|^2$; su fase no influye. Es la misma regla que para las señales de energía del [capítulo 6](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen/korrelationsfunktionen.html), ahora para procesos. (Complemento: en sentido estricto, $\Phi_{ss}$ se define como el límite $\lim_{T\to\infty}\frac1T\mathrm E\{|S_T(f)|^2\}$ de espectros de tiempo corto de fragmentos de duración $T$. Que esto sea lo mismo que la transformada de la FAC es la afirmación propiamente dicha del teorema de Wiener-Khinchin.)

:::ltspice Ruido con valor medio a través de un paso bajo y un paso alto
⁠**Esquema:** fuente de comportamiento `bv` en el nodo `s` con `V=1+white(1e3*time)`. `white(x)` da valores aleatorios entre $-0{,}5$ y $0{,}5$, uno nuevo en cada $x$ entero, unidos de forma suave; aquí, por tanto, uno cada milisegundo. Conectados en paralelo a ella, un paso bajo RC (`res` con `1Meg` hacia `tp`, `cap` con `1u` a masa) y un paso alto CR (`cap` con `1u` hacia `hp`, `res` con `1Meg` a masa).

⁠**Directiva:** `.tran 0 200 0 0.1m`.

⁠**Lectura:** amplía la vista de 20 s a 200 s, es decir, al tiempo posterior al transitorio. Un clic con la tecla Ctrl pulsada sobre el nombre de una curva muestra el valor medio (Average) y el valor eficaz (RMS) en el intervalo visible.

⁠**Lo que ves:** la entrada tiene el valor medio 1 V. Compara los valores medios de `V(tp)` y `V(hp)` con tu resultado del ejercicio [7](#aufg-7). Las fluctuaciones son mucho menores en el paso bajo: haz que se dibujen `V(s)-1` y `V(tp)-1`; sus valores eficaces son de aproximadamente 0,25 y 0,01. De la ancha densidad espectral de potencia, el paso bajo solo deja pasar aproximadamente la parte por debajo de $1/(2\pi RC)=0{,}16$ Hz, y según [(8.3)](#gl-8-3) la potencia es el área bajo la densidad espectral de potencia.
:::

:::aufgabe Ejercicio 7 ★ Valor medio a través de un filtro
<span class="anker" id="aufg-7"></span>

Un ruido con un valor medio de 1 V pasa por un paso bajo RC y por un paso alto CR. ¿Qué valores medios tienen las salidas y por qué?

:::loesung
Paso bajo RC: $H(0)=1$, valor medio 1 V. Paso alto CR: $H(0)=0$, valor medio 0. El condensador no deja pasar la corriente continua; la componente continua queda bloqueada.
:::
:::

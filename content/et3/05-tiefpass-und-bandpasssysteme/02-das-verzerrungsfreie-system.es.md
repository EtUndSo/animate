---
title: Etapa 1: El sistema sin distorsión
pfad: Ingeniería eléctrica / 3.er semestre / Señales y sistemas / Sistemas paso bajo y paso banda
order: 3250200
summary: ¿Qué debe lograr exactamente una «buena» transmisión?
tags: retardo de fase, retardo de grupo
lang: es
---

<span class="anker" id="stufe-1"></span>

:::zweck
¿Qué debe lograr exactamente una «buena» transmisión? ¿Y con qué magnitudes características se mide cuánto se aparta de ello un sistema?
:::

**La idea.** Una señal ha llegado sin distorsión si solo se ha vuelto más intensa o más débil y más tardía, pero conserva su forma:

<span class="anker" id="gl-1-1"></span>
$$g(t)=h_0\,s(t-t_0)\qquad\Longleftrightarrow\qquad h(t)=h_0\,\delta(t-t_0),\qquad H(f)=h_0\,\mathrm{e}^{-\mathrm{j}2\pi t_0f}. \tag{1.1}$$

En el espectro, esto significa: cada oscilación se multiplica por el mismo factor $h_0$, y cada una se desplaza el mismo tiempo $t_0$. A la frecuencia $f$, un desplazamiento temporal $t_0$ equivale al ángulo $2\pi ft_0$. Por eso la fase $\varphi(f)=-2\pi t_0f$ tiene que ser una recta que pasa por el origen.

:::definition Definición 1.1 (Magnitudes características de un sistema LTI)
<span class="anker" id="satz-1-1"></span>

<span class="anker" id="gl-1-2"></span>
<span class="anker" id="gl-1-3"></span>
<span class="anker" id="gl-1-4"></span>
<span class="anker" id="gl-1-5"></span>
$$\begin{aligned} &\text{Atenuación:} && a(f)=-20\lg|H(f)|\ \text{dB}\quad\text{o}\quad a(f)=-\ln|H(f)|\ \text{Np},\\ &\text{Desfase:} && b(f)=-\varphi(f),\\ &\text{Retardo de fase:} && t_\mathrm p(f)=-\frac{\varphi(f)}{2\pi f},\\ &\text{Retardo de grupo:} && t_\mathrm g(f)=-\frac{1}{2\pi}\frac{\mathrm{d}\varphi(f)}{\mathrm{d} f}. \end{aligned} \tag{1.2|1.3|1.4|1.5}$$
:::

⁠**Cómo leerlo:** el __retardo de fase__ es el retardo de una única oscilación de frecuencia $f$. El __retardo de grupo__ es el retardo de un grupo de frecuencias vecinas, es decir, de una envolvente (etapa [11](phasen-und-gruppenlaufzeit-beim-bandpass.html#stufe-11)). En el sistema sin distorsión, $a$, $t_\mathrm p$ y $t_\mathrm g$ son constantes y $t_\mathrm p=t_\mathrm g=t_0$.

**Ejemplo: el circuito RC.** Con $\varphi=-\arctan(2\pi f\,RC)$ y $RC=1$ s:

$$t_\mathrm p=\frac{\arctan(2\pi f\,RC)}{2\pi f},\qquad t_\mathrm g=\frac{RC}{1+(2\pi f\,RC)^2}.$$

Para $f\to0$, ambos valen $RC=1$ s. En $f=0{,}159$ Hz ($2\pi fRC=1$), $t_\mathrm p=0{,}785$ s, $t_\mathrm g=0{,}5$ s y $a=3{,}0$ dB. Así pues, el circuito RC no está libre de distorsión: su atenuación depende de la frecuencia, y las distintas frecuencias llegan en instantes distintos.

:::ltspice Leer la atenuación y los retardos del circuito RC
⁠**Esquema:** circuito RC (`res` con `1Meg`, `cap` con `1u`), valor de fuente `AC 1`, directiva `.ac dec 100 0.01 10`.

⁠**Lectura:** el eje izquierdo muestra $20\lg|H|=-a$ en dB. Lleva el ratón al eje derecho (fase) hasta que el puntero se convierta en una regla, haz clic y elige «Group Delay»: entonces el eje muestra $t_\mathrm g(f)$ según [(1.5)](#gl-1-5). El retardo de fase lo calculas a partir de la fase, $t_\mathrm p=-\varphi/(2\pi f)$, con $\varphi$ en radianes.

⁠**Lo que ves:** hacia las frecuencias bajas, $t_\mathrm g$ tiende a 1 s. En 0,159 Hz lees $a=3{,}0$ dB, $\varphi=-45^\circ$ y $t_\mathrm g=0{,}5$ s; de ahí, $t_\mathrm p=0{,}785$ s. Compara los valores en $2\pi fRC=10$ con tu resultado del ejercicio [1](#aufg-1)(b).
:::

:::aufgabe Ejercicio 1 ★ Retardos del circuito RC
<span class="anker" id="aufg-1"></span>

<ol class="al">

<li>

Deduce $t_\mathrm g$ del circuito RC a partir de [(1.5)](#gl-1-5).

</li>

<li>

Calcula $t_\mathrm p$, $t_\mathrm g$ y $a$ para $2\pi fRC=10$. ¿En qué rango de frecuencias está el circuito RC aproximadamente libre de distorsión?

</li>

</ol>

:::loesung
(a) $\varphi=-\arctan(2\pi fRC)$, $\frac{\mathrm{d}\varphi}{\mathrm{d} f}=-\frac{2\pi RC}{1+(2\pi fRC)^2}$; por tanto, $t_\mathrm g=-\frac{1}{2\pi}\frac{\mathrm{d}\varphi}{\mathrm{d} f}=\frac{RC}{1+(2\pi fRC)^2}$.

(b) Para $2\pi fRC=10$: $t_\mathrm p=\frac{\arctan10}{10}RC=0{,}147$ s, $t_\mathrm g=\frac{RC}{101}=0{,}0099$ s, $a=20{,}0$ dB. El circuito RC solo está aproximadamente libre de distorsión para $2\pi fRC\ll1$, es decir, muy por debajo de 0,16 Hz: ahí $|H|\approx1$ y $t_\mathrm p\approx t_\mathrm g\approx RC$.
:::
:::

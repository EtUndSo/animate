---
title: Lo esencial
pfad: Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos / El amplificador operacional
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-operationsverstarker
knoten: Capítulo 11: El amplificador operacional
order: 1211300
summary: Cómo un factor enorme e impreciso se convierte en un componente cuyo comportamiento solo depende de las resistencias
tags: amplificador diferencial, ganancia de lazo, masa virtual, Ruido, Comparador
lang: es
---

:::merke La respuesta en tres frases
<ol>

<li>

En su interior hay un __amplificador diferencial__, un circuito que solo reacciona a la diferencia entre dos tensiones: $U_\mathrm{A}=A\,U_\mathrm{D}$ con $U_\mathrm{D}=\varphi_+-\varphi_-$. Con $A=100000$ y como máximo 11 V en la salida, a $U_\mathrm{D}$ le queda una ventana de $\pm110$ µ V.

</li>

<li>

La realimentación negativa lleva la fracción $\beta$ de la salida a la entrada negativa. La salida se mueve hasta que el lazo se aquieta, y eso ocurre cuando $U_\mathrm{D}$ basta justo para la salida: 5 V necesitan 50 µ V. La ganancia pasa a ser $G\approx1/\beta$, y la __ganancia de lazo__ $A\beta$ (el factor de una vuelta por el lazo) ya solo fija la pequeña desviación.

</li>

<li>

De ahí sale una regla: potenciales iguales en las entradas, ninguna corriente hacia ellas, ley de los nudos en la entrada negativa. Explica la __masa virtual__ (un nudo a 0 V sin conexión con masa) y todos los circuitos básicos. Termina donde la salida llega a su tope, donde la realimentación cambia de signo y donde $A\beta$ se hace pequeño.

</li>

</ol>
:::

:::kern Lo esencial
<ul>

<li>

Ruido: $u_\mathrm{r,eff}=\sqrt{\int|u_\mathrm{r}(f)|^2\mathrm{d} f}$, térmico $|u_\mathrm{r,R}|^2=4k_\mathrm{B}TR$. Amplificar no cambia la SNR; solo ayuda contra perturbaciones posteriores. $\mathrm{SNR}_\mathrm{dB}=20\lg(u_\mathrm{s}/u_\mathrm{r})$.

</li>

<li>

Amplificador diferencial: corriente total fija, $U_\mathrm{A}=S\,R_\mathrm{C}\,U_\mathrm{D}$, cada unión BE soporta $U_\mathrm{D}/2$, el modo común no actúa.

</li>

<li>

Modelo: $U_\mathrm{A}=A(\varphi_+-\varphi_-)$ hasta los topes. Ventana $\pm110$ µ V; sin realimentación, comparador.

</li>

<li>

Realimentación negativa: $U_\mathrm{D}=U_\mathrm{E}/(1+A\beta)$, $G=\frac1\beta\cdot\frac1{1+1/(A\beta)}$, $\Delta G/G=\frac{1}{1+A\beta}\Delta A/A$. La salida se mueve hasta que el lazo se aquieta. Con 5 V quedan 50 µ V.

</li>

<li>

Regla: $\varphi_+=\varphi_-$, $I_\pm=0$, ley de los nudos en la entrada negativa, al final comprobar los límites. Masa virtual: 0 V por regulación, sin camino a masa. La corriente pasa por la realimentación hacia la salida.

</li>

<li>

$G=-R_2/R_1$, $G=1+R_2/R_1$, $U_\mathrm{A}=-R_\mathrm{F}\sum U_{\mathrm{E}i}/R_{\mathrm{E}i}$, $U_\mathrm{A}=\frac{R_2}{R_1}(U_\mathrm{E2}-U_\mathrm{E1})$, integrador $-\frac{1}{RC}\int u_\mathrm{E}\mathrm{d} t$, derivador $-RC\,\mathrm{d} u_\mathrm{E}/\mathrm{d} t$, amplificador logarítmico $-U_T\ln(U_\mathrm{E}/RI_\mathrm{S})$, amplificador exponencial $-RI_\mathrm{S}\mathrm{e}^{U_\mathrm{E}/U_T}$, transimpedancia $-R\,I_\mathrm{E}$, NIC $R_\mathrm{ent}=-R_2$.

</li>

<li>

Realimentación positiva: el efecto refuerza la causa, salida en el tope, umbrales $\beta\,U_\mathrm{A,max}$ y $\beta\,U_\mathrm{A,min}$.

</li>

<li>

Límites: sobreexcitación, $U_\mathrm{off}/\beta$, $I_\mathrm{B}R_2$, CMRR, $G\,f_G=f_\mathrm{T}$.

</li>

</ul>
:::

**Un principio detrás de todos los resultados.** La salida de un AO con realimentación negativa no es un cálculo con $A$, sino el estado en que el lazo se aquieta. Para ello, $A$ solo tiene que ser grande; su valor exacto no cuenta.

| Resultado | De dónde viene |
|---|---|
| __Ruido__ (tensión perturbadora aleatoria), relación señal-ruido | Las cargas individuales se mueven al azar; amplificar eleva por igual la señal y la perturbación (etapa [1](rauschen.html#stufe-1)) |
| $U_\mathrm{A}=S\,R_\mathrm{C}\,U_\mathrm{D}$, modo común sin efecto | Una corriente total fija: solo puede cambiar su reparto (etapa [2](der-differenzverstarker.html#stufe-2)) |
| __Comparador__ (circuito que compara tensiones) | Sin realimentación, casi ninguna tensión de entrada cabe en la ventana (etapa [3](der-opv-ohne-ruckfuhrung.html#stufe-3)) |
| $U_\mathrm{D}=U_\mathrm{A}/A$, $G\approx1/\beta$ | La salida se mueve hasta que el lazo se aquieta (etapa [4](gegenkopplung.html#stufe-4)) |
| $G=-R_2/R_1$, masa virtual | Regla y ley de los nudos en la entrada negativa (etapa [5](die-regel-und-die-virtuelle-masse.html#stufe-5)) |
| Sumador, restador, cadena | Las corrientes se suman, los efectos se superponen (etapa [6](mehrere-eingange-mehrere-stufen.html#stufe-6)) |
| Integrador, amplificador logarítmico | Un componente fija la corriente; el otro, la tensión (etapa [7](rechnen-mit-kondensator-und-diode.html#stufe-7)) |
| Convertidor de corriente a tensión, resistencia negativa | La salida entrega cualquier corriente que exija la regla (etapa [8](strom-als-signal.html#stufe-8)) |
| Disparador de Schmitt | Signo equivocado: el efecto refuerza su causa (etapa [9](mitkopplung-und-der-schmitt-trigger.html#stufe-9)) |
| Límites de la regla | Todo lo que reduce $A\beta$ o desplaza $U_\mathrm{D}$ (etapa [10](wo-die-regeln-enden.html#stufe-10)) |

---
title: Lo esencial
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / Potencia, adaptación y rendimiento
order: 1170900
summary: Por qué en el máximo de potencia la mitad de la energía se queda en la fuente
tags: calor de Joule, adaptación de potencia, rendimiento, adaptación de tensión, adaptación de corriente
lang: es
---

:::merke La respuesta en tres frases
<ol>

<li>

La tensión es energía por unidad de carga, la corriente es carga por unidad de tiempo. Su producto es energía por unidad de tiempo: $p=u\,i$.

</li>

<li>

En la resistencia, el campo acelera los electrones, y cada choque entrega la energía ganada a la red cristalina. Por eso, allí toda la potencia se convierte en calor, el __calor de Joule__, con $P=R\,I^2$.

</li>

<li>

Una fuente con resistencia interna $R_\mathrm{i}$ entrega la mayor potencia a la carga $R_\mathrm{L}=R_\mathrm{i}$. Esto se llama __adaptación de potencia__. En ese punto, la energía de cada carga se reparte a partes iguales entre fuente y carga conectada, y el __rendimiento__, la fracción de la potencia que se aprovecha, es del 50 %. Una tensión fija la proporciona la __adaptación de tensión__ (carga grande frente a la fuente); una corriente fija, la __adaptación de corriente__ (carga pequeña frente a la fuente).

</li>

</ol>
:::

:::kern Lo esencial
<ul>

<li>

La potencia es energía por culombio multiplicada por culombios por segundo: $p=u\,i$. La energía es su integral en el tiempo.

</li>

<li>

En la resistencia, los choques lo ceden todo a la red cristalina: $P=R\,I^2=U^2/R$, limitada por $P_\mathrm{max}$.

</li>

<li>

En una resistencia con tensión sinusoidal, $P=\frac12\hat u^2/R=\frac12\hat\imath^2R$.

</li>

<li>

La misma potencia con una tensión $n$ veces mayor reduce la pérdida en la línea a $1/n^2$.

</li>

<li>

Balance: $P_\mathrm{q}=P_\mathrm{v}+P_\mathrm{L}$. Rendimiento: $\eta=U_\mathrm{L}/U_\mathrm{q}=R_\mathrm{L}/(R_\mathrm{L}+R_\mathrm{i})$.

</li>

<li>

Máxima potencia con $R_\mathrm{L}=R_\mathrm{i}$: $P_\mathrm{L,max}=U_\mathrm{q}^2/(4R_\mathrm{i})$, con $\eta=\frac12$, porque la corriente y el rendimiento varían linealmente en sentidos opuestos.

</li>

<li>

La ingeniería de potencia quiere $R_\mathrm{L}\gg R_\mathrm{i}$; la transmisión de señales, $R_\mathrm{L}=R_\mathrm{i}$. Las fuentes equivalentes dan bien el máximo, pero no el rendimiento.

</li>

</ul>
:::

**Un principio detrás de todos los resultados.** Toda potencia es el producto de dos respuestas: ¿cuánta energía cede un culombio en este lugar, y cuántos culombios pasan por segundo?

| Resultado | De dónde viene |
|---|---|
| $p=u\,i$ | Energía por unidad de carga multiplicada por carga por unidad de tiempo (etapa [1](energie-je-ladung-mal-ladung-je-zeit.html#stufe-1)) |
| $P=R\,I^2=U^2/R$, potencia nominal | Los choques lo ceden todo a la red cristalina; el doble de corriente significa el doble de culombios, cada uno de los cuales cede el doble (etapa [2](warum-der-widerstand-warm-wird.html#stufe-2)) |
| $P=\frac12\hat u^2/R$ | $u$ e $i$ cambian de signo a la vez, $\cos^2$ tiene el valor medio $\frac12$ (etapa [3](mittlere-leistung-bei-sinusspannung.html#stufe-3)) |
| Líneas de alta tensión | La misma potencia con menos culombios, cada uno de los cuales pierde menos (etapa [4](leitungsverluste.html#stufe-4)) |
| $\eta=U_\mathrm{L}/U_\mathrm{q}$ | Fracción de la energía por culombio que llega a la carga (etapa [5](wohin-die-leistung-einer-quelle-geht.html#stufe-5)) |
| $R_\mathrm{L}=R_\mathrm{i}$ | La corriente y la tensión en la carga varían linealmente en sentidos opuestos, su producto es máximo en el centro (etapa [6](leistungsanpassung.html#stufe-6)) |
| $\eta=50\,\%$ en el máximo | El centro significa: la mitad de la energía por culombio se queda dentro (etapa [7](warum-50-und-welches-ziel-gilt.html#stufe-7)) |

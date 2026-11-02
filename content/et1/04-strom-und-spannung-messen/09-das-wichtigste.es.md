---
title: Lo esencial
pfad: Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica / Medir corriente y tensión
order: 1140900
summary: Por qué todo instrumento modifica el circuito y cómo medir con exactitud a pesar de ello
tags: amperímetro, voltímetro, medición de corriente correcta, medición de tensión correcta, puente de Wheatstone, equilibrio
lang: es
---

:::merke La respuesta en tres frases
<ol>

<li>

Un __amperímetro__ (medidor de corriente) se conecta en serie en el circuito y le añade su resistencia interna. Un __voltímetro__ (medidor de tensión) se conecta en paralelo y abre un segundo camino para la corriente. Ambos muestran el valor del circuito modificado.

</li>

<li>

El error relativo es aproximadamente $R_\mathrm i/R$ en el amperímetro y aproximadamente $R/R_\mathrm i$ en el voltímetro. Si se miden ambas magnitudes a la vez, solo una lectura es correcta: __medición de corriente correcta__ (la corriente es la correcta) o __medición de tensión correcta__ (la tensión es la correcta).

</li>

<li>

El __puente de Wheatstone__ (dos divisores de tensión en una misma fuente y un instrumento entre ellos) compara resistencias. En el __equilibrio__ (ajustado a lectura cero) no circula corriente por el instrumento. Por eso, su resistencia interna, su escala y la tensión de la fuente desaparecen del resultado $R_4=R_3R_2/R_1$.

</li>

</ol>
:::

:::kern Lo esencial
<ul>

<li>

Un instrumento de medida es una resistencia y muestra el valor del circuito modificado.

</li>

<li>

Amperímetro: $I_R/I_R'=1+R_\mathrm i/R$. Voltímetro: $U_L/U_L'=1+R_L/R_\mathrm i$.

</li>

<li>

Ampliar el rango: $R_\mathrm{Shunt}=R_\mathrm{viejo}I_\mathrm{viejo}/(I_\mathrm{nuevo}-I_\mathrm{viejo})$ y $R_\mathrm V=R_\mathrm{viejo}(\alpha-1)$.

</li>

<li>

Corriente correcta $U/I=R+R_\mathrm{iA}$ para $R$ grandes, tensión correcta $U/I=R\parallel R_\mathrm{iV}$ para $R$ pequeñas.

</li>

<li>

Equilibrio: $R_4=R_3R_2/R_1$, independiente de la resistencia interna, la escala y la tensión de la fuente.

</li>

<li>

Desequilibrado: $U_\mathrm d\approx\frac14U_\mathrm q\,\Delta R/R$. Sin la tensión común basta un rango pequeño.

</li>

</ul>
:::

**Un principio detrás de todos los resultados.** Para el circuito, un instrumento de medida es una resistencia más. Todos los errores se deducen de las mismas reglas que en la [Parte 2](/wissen/es/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html): regla de las mallas, regla de los nudos, ley de Ohm.

| Resultado | De dónde viene |
|---|---|
| Resistencia interna | El instrumento necesita corriente y su bobina tiene resistencia (etapa [1](das-messgerat-ist-ein-bauteil.html#stufe-1)) |
| Shunt y resistencia en serie | El divisor de corriente y el divisor de tensión protegen el instrumento (etapa [2](den-messbereich-erweitern.html#stufe-2)) |
| $I_R'=U/(R+R_\mathrm i)$ | Una resistencia más en la malla (etapa [3](der-fehler-beim-strommessen.html#stufe-3)) |
| $U_L'=U_L/(1+R_L/R_\mathrm i)$ | Una rama más en el nudo (etapa [4](der-fehler-beim-spannungsmessen.html#stufe-4)) |
| Corriente correcta y tensión correcta | Cada instrumento está en el circuito de medida del otro (etapa [5](strom-und-spannung-zugleich.html#stufe-5)) |
| Equilibrio $R_4=R_3R_2/R_1$ | Sin corriente, el instrumento no toma nada del puente (etapa [6](die-wheatstonesche-brucke.html#stufe-6)) |
| $U_\mathrm d\approx\frac14U_\mathrm q\,\Delta R/R$ | El puente resta la tensión común (etapa [7](die-verstimmte-brucke.html#stufe-7)) |

---
title: Etapa 3: Valor medio, potencia, varianza
pfad: Ingeniería eléctrica / 3.er semestre / ET3 – Fundamentos de ingeniería eléctrica 3: señales y sistemas / Señales aleatorias
adresse: elektrotechnik/3-semester/signale-und-systeme/zufallssignale
knoten: Capítulo 7: Señales aleatorias
order: 3270400
summary: Los valores medios de primer orden más importantes y su significado intuitivo.
tags: componente continua, potencia, varianza, potencia alterna, desviación típica
lang: es
---

<span class="anker" id="stufe-3"></span>

:::zweck
Los valores medios de primer orden más importantes y su significado intuitivo.
:::

El valor esperado es lineal: $\mathrm E\{\sum_ia_is_i\}=\sum_ia_i\mathrm E\{s_i\}$, para variables aleatorias cualesquiera. En los procesos estacionarios se define:

<span class="anker" id="gl-3-1"></span>
$$m_s=\mathrm E\{s(t)\},\qquad L_s=\mathrm E\{s^2(t)\},\qquad\sigma_s^2=L_s-m_s^2. \tag{3.1}$$

⁠**Cómo leerlo:** en un proceso ergódico, $m_s$ es la media temporal, es decir, la __componente continua__ de la señal, y $L_s$ es el valor cuadrático medio temporal, la __potencia__ ([capítulo 6](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen/korrelationsfunktionen.html)). La __varianza__ $\sigma_s^2$ es la potencia menos la potencia de la componente continua, es decir, la __potencia alterna__. Su raíz, la __desviación típica__ $\sigma_s$, es el valor eficaz de la componente alterna. Un multímetro en modo AC muestra $\sigma_s$; en modo DC, $m_s$.

:::aufgabe Ejercicio 1 ★ Valores medios de una señal
<span class="anker" id="aufg-1"></span>

Una señal ergódica tiene una componente continua de 2 V y un valor eficaz (todo junto, «true RMS») de 2,5 V. ¿Cuánto valen la potencia normalizada, la varianza y la desviación típica?

:::loesung
$L_s=2{,}5^2=6{,}25$ V$^2$, $\sigma_s^2=L_s-m_s^2=6{,}25-4=2{,}25$ V$^2$, $\sigma_s=1{,}5$ V. Un instrumento de medida en modo AC muestra 1,5 V.
:::
:::

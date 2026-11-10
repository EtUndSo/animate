---
title: Lo esencial
pfad: Ingeniería eléctrica / 3.er semestre / ET3 – Fundamentos de ingeniería eléctrica 3: señales y sistemas / Señales aleatorias
adresse: elektrotechnik/3-semester/signale-und-systeme/zufallssignale
knoten: Capítulo 7: Señales aleatorias
order: 3271400
summary: Valores medios, distribuciones, densidad espectral de potencia, ruido en sistemas y el receptor óptimo
tags: 
lang: es
---

:::merke La respuesta en tres frases
<ol>

<li>

Una señal aleatoria se describe mediante valores medios: valor medio, potencia, varianza, función de autocorrelación y densidad de probabilidad. En los procesos ergódicos pueden determinarse a partir de una única señal larga.

</li>

<li>

La transformada de Fourier de la función de autocorrelación es la densidad espectral de potencia. Un sistema LTI la multiplica por $|H(f)|^2$, exactamente igual que en las señales de energía ([capítulo 6](/wissen/es/elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen/korrelationsfunktionen.html)).

</li>

<li>

Frente al ruido blanco, el filtro adaptado $h(t)=s(T-t)$ es óptimo. Alcanza la relación señal-ruido $E_s/N_0$, independientemente de la forma de la señal.

</li>

</ol>
:::

:::kern Lo esencial
<ul>

<li>

Media de conjunto $\mathrm E\{\cdot\}$; estacionario: independiente del desplazamiento; ergódico: media temporal $=$ media de conjunto.

</li>

<li>

$m_s$ (componente continua), $L_s=\mathrm E\{s^2\}$ (potencia), $\sigma_s^2=L_s-m_s^2$ (potencia alterna).

</li>

<li>

FAC: $\varphi_{ss}(0)=L_s$, par, máximo en 0; covarianza $\mu=\varphi-m^2$; suma: $\sigma_s^2=\sigma_u^2+\sigma_v^2+2\mu_{uv}(0)$.

</li>

<li>

$P_s(x)=\mathrm{Prob}[s\le x]$, $p_s=P_s'$; $m_s=\int xp_s$, $L_s=\int x^2p_s$; distribución uniforme $\sigma^2=a^2/12$.

</li>

<li>

Característica: $p_g(y)|\mathrm{d} y|=p_s(x)|\mathrm{d} x|$; error de cuantización $\Delta^2/12$, 6 dB por bit.

</li>

<li>

Independientes $\Rightarrow$ incorreladas; suma de independientes: $p_s=p_f*p_g$; Gauss: $\frac{1}{\sqrt{2\pi\sigma^2}}\mathrm{e}^{-(x-m)^2/2\sigma^2}$.

</li>

<li>

LTI: $m_g=m_sH(0)$, $\varphi_{gg}=\varphi_{ss}*\varphi^E_{hh}$, $\Phi_{gg}=\Phi_{ss}|H|^2$, $L=\int\Phi\,\mathrm{d} f$.

</li>

<li>

Blanco: $\Phi=N_0$, $\varphi=N_0\delta$; térmico $\mathrm E\{u^2\}=4kTRf_\mathrm g$, $kT\approx4$ pW/GHz.

</li>

<li>

Filtro adaptado: $h=a\,s(T-t)$, $(S_a/N)_{\max}=E_s/N_0$; $P_{e,\min}=\frac12\operatorname{erfc}\sqrt{E_s/(8N_0)}$.

</li>

</ul>
:::

**Un principio detrás de todos los resultados.** La señal desconocida se sustituye por sus valores medios, y para los valores medios rige la linealidad:

| Resultado | De dónde viene |
|---|---|
| Valor medio, potencia, varianza | media de conjunto y media temporal (etapas [1](der-zufallsprozess.html#stufe-1)–[3](mittelwert-leistung-varianz.html#stufe-3)) |
| FAC, covarianza, FCC | media de productos en dos instantes (etapa [4](autokorrelation-kovarianz-und-kreuzkorrelation.html#stufe-4)) |
| Densidad de probabilidad | fracción del tiempo o del conjunto por debajo de un umbral (etapa [5](verteilungsfunktion-und-verteilungsdichte.html#stufe-5)) |
| Suma de variables independientes | convolución de las densidades, de ahí Gauss (etapas [6](verbundverteilung-unabhangigkeit-unkorreliertheit.html#stufe-6), [7](die-gau-verteilung.html#stufe-7)) |
| Densidad espectral de potencia, Wiener-Lee | linealidad del valor medio en la integral de convolución (etapa [8](zufallssignale-in-lti-systemen-leistungsdichte.html#stufe-8)) |
| Ruido blanco | densidad espectral de potencia constante, FAC $=N_0\delta$ (etapa [9](weies-rauschen-und-thermisches-rauschen.html#stufe-9)) |
| Filtro adaptado | Cauchy-Schwarz: la correlación es máxima con la propia señal (etapa [10](das-korrelationsfilter-matched-filter.html#stufe-10)) |
| Probabilidad de error | área bajo una curva de Gauss más allá del umbral (etapa [11](fehlerwahrscheinlichkeit-beim-binarempfang.html#stufe-11)) |

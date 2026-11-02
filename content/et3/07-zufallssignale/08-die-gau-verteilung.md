---
title: Stufe 7: Die Gauß-Verteilung
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / Zufallssignale
order: 3270800
summary: Warum ist Rauschen so oft gaußverteilt, und wie rechnet man mit der Gauß-Verteilung?
tags: zentraler Grenzwertsatz, Fehlerfunktion
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Warum ist Rauschen so oft gaußverteilt, und wie rechnet man mit der Gauß-Verteilung?
:::

Faltet man viele Dichten miteinander, nähert sich das Ergebnis einer Gaußkurve (__zentraler Grenzwertsatz__, [Teil 3](/wissen/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)). Rauschen ist meist die Summe sehr vieler kleiner, unabhängiger Beiträge, etwa der Bewegungen vieler Elektronen. Deshalb ist es gaußverteilt.

:::satz Satz 7.1 (Gauß-Verteilung)
<span class="anker" id="satz-7-1"></span>

<span class="anker" id="gl-7-1"></span>
$$p_s(x)=\frac{1}{\sqrt{2\pi\sigma_s^2}}\,\mathrm{e}^{-(x-m_s)^2/(2\sigma_s^2)},\qquad P_s(x)=\frac12+\frac12\operatorname{erf}\Bigl(\frac{x-m_s}{\sqrt{2\sigma_s^2}}\Bigr)=\frac12\operatorname{erfc}\Bigl(\frac{m_s-x}{\sqrt{2\sigma_s^2}}\Bigr) \tag{7.1}$$

mit der __Fehlerfunktion__ $\operatorname{erf}(x)=\frac{2}{\sqrt\pi}\int_0^x\mathrm{e}^{-\xi^2}\mathrm{d}\xi$ und $\operatorname{erfc}=1-\operatorname{erf}$.
:::

⁠**So liest man das:** Mittelwert und Varianz legen die Gauß-Verteilung vollständig fest. Innerhalb von $\pm\sigma_s$ um den Mittelwert liegen 68,3 % der Werte, innerhalb $\pm2\sigma_s$ 95,4 %, innerhalb $\pm3\sigma_s$ 99,73 %. Das Integral der Gaußkurve hat keine geschlossene Form, deshalb die Funktion erf, die man tabelliert oder numerisch berechnet. Für große $x$ gilt $\operatorname{erfc}(x)\approx\frac{\mathrm{e}^{-x^2}}{\sqrt\pi\,x}$.

**Rechenregeln.** Die Summe zweier unabhängiger gaußverteilter Größen ist gaußverteilt mit $m_s=m_1+m_2$ und $\sigma_s^2=\sigma_1^2+\sigma_2^2$. Ein Gauß-Prozess bleibt nach einem LTI-System ein Gauß-Prozess, denn das Faltungsintegral ist eine (unendliche) gewichtete Summe. Und bei zwei gemeinsam gaußverteilten Größen ist „unkorreliert“ dasselbe wie „unabhängig“: Ist die normierte Kreuzkovarianz $\rho=\mu_{sg}/(\sigma_s\sigma_g)$ null, zerfällt die Verbunddichte in ein Produkt.

:::zusatz Die zweidimensionale Gauß-Dichte
Für mittelwertfreie, gemeinsam gaußverteilte $s,g$ mit dem Korrelationskoeffizienten $\rho$ ist

$$p_{sg}(x,y)=\frac{1}{2\pi\sigma_s\sigma_g\sqrt{1-\rho^2}}\exp\Bigl(-\frac{\sigma_g^2x^2+\sigma_s^2y^2-2\rho\sigma_s\sigma_gxy}{2\sigma_s^2\sigma_g^2(1-\rho^2)}\Bigr).$$

Man erhält sie über die normierten Summen- und Differenzgrößen $\frac{s}{\sigma_s}\pm\frac{g}{\sigma_g}$: Sie sind unkorreliert, haben die Varianzen $2(1\pm\rho)$ und sind als Gauß-Größen unabhängig. Linien gleicher Dichte sind Ellipsen. In den normierten Koordinaten $x/\sigma_s$, $y/\sigma_g$ liegen ihre Achsen entlang dieser Summen und Differenzen. Für $\rho=0$ werden sie zu Kreisen (bei $\sigma_s=\sigma_g$), und die Dichte ist das Produkt der Einzeldichten.
:::

:::aufgabe Aufgabe 6 ★ Mit der Gauß-Verteilung rechnen
<span class="anker" id="aufg-6"></span>

Eine Rauschspannung ist gaußverteilt mit $m=0$ und $\sigma=1$ mV.

<ol class="al">

<li>

Mit welcher Wahrscheinlichkeit ist sie größer als 2 mV? (Tipp: $\operatorname{erfc}(1{,}414)=0{,}0455$.)

</li>

<li>

Zwei solche unabhängige Spannungen werden addiert. Welche Verteilung hat die Summe?

</li>

</ol>

:::loesung
(a) $\mathrm{Prob}[x>2\,\mathrm{mV}]=\frac12\operatorname{erfc}\bigl(\frac{2}{\sqrt2}\bigr)=\frac12\operatorname{erfc}(1{,}414)=0{,}023$, also 2,3 %.

(b) Gaußverteilt mit $m=0$ und $\sigma^2=2$ mV$^2$, $\sigma=1{,}41$ mV.
:::
:::

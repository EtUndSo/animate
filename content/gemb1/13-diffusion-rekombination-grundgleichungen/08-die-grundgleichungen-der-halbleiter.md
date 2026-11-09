---
title: Stufe 6: Die Grundgleichungen der Halbleiter
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Diffusion, Rekombination und Grundgleichungen
order: 4230800
summary: Drift, Diffusion, Generation und Rekombination stehen einzeln.
tags: Poisson-Gleichung für den Bandverlauf, selbstkonsistent, Nichtgleichgewichts-Green-Funktionen
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Drift, Diffusion, Generation und Rekombination stehen einzeln. In einem Bauelement wirken sie zugleich, und die Träger erzeugen selbst ein Feld. Diese Stufe fasst alles in einem Satz gekoppelter Gleichungen zusammen.
:::

**Die Idee.** Drei Fragen beschreiben jedes Bauelement. Wie strömen die Träger? (Stromgleichungen: Drift plus Diffusion.) Wie ändern die Ströme die Dichten? (Kontinuitätsgleichung für jede Sorte.) Welches Feld erzeugen die Dichten? (Poisson-Gleichung.) Das Feld wirkt wieder auf die Ströme, und der Kreis schließt sich (Abb. [6](#abb-6)).

:::abbildung gemb1/k13kreis 6
Die Grundgleichungen als Kreis. Die Dichten bestimmen das Feld, Feld und Dichten die Ströme, die Ströme die Änderung der Dichten. Von außen kommen die festen Ionen und die Raten $G$ und $R$.
:::

:::satz Satz 6.1 (Grundgleichungen)
<span class="anker" id="satz-6-1"></span>

⁠**Stromgleichungen** (Drift-Diffusion-Gleichungen), mit $e\,n\,\mu_\mathrm n=\sigma_\mathrm n$ und $e\,p\,\mu_\mathrm p=\sigma_\mathrm p$:

<span class="anker" id="gl-6-1"></span>
<span class="anker" id="gl-6-2"></span>
$$\begin{aligned} \boldsymbol j_\mathrm n&=e\,n\,\mu_\mathrm n\boldsymbol{\mathcal E}+e\,\frac{k_\mathrm BT}e\,\mu_\mathrm n\nabla n=e\,n\,\mu_\mathrm n\boldsymbol{\mathcal E}+e\,D_\mathrm n\operatorname{grad}n,\\ \boldsymbol j_\mathrm p&=e\,p\,\mu_\mathrm p\boldsymbol{\mathcal E}-e\,\frac{k_\mathrm BT}e\,\mu_\mathrm p\nabla p=e\,p\,\mu_\mathrm p\boldsymbol{\mathcal E}-e\,D_\mathrm p\operatorname{grad}p. \end{aligned} \tag{6.1|6.2}$$

⁠**Kontinuitätsgleichungen:**

<span class="anker" id="gl-6-3"></span>
$$\frac{\partial n}{\partial t}=\frac1e\,\nabla\cdot\boldsymbol j_\mathrm n+G_\mathrm n-R_\mathrm n,\qquad\frac{\partial p}{\partial t}=-\frac1e\,\nabla\cdot\boldsymbol j_\mathrm p+G_\mathrm p-R_\mathrm p. \tag{6.3}$$

⁠**Poisson-Gleichung** mit der Raumladungsdichte $\rho$:

<span class="anker" id="gl-6-4"></span>
$$\Delta\varphi(\boldsymbol r)=-\frac{\rho(\boldsymbol r)}{\varepsilon_0\varepsilon_\mathrm r}=-\frac e{\varepsilon_0\varepsilon_\mathrm r}\bigl(p(\boldsymbol r)-n(\boldsymbol r)+N_\mathrm D^+(\boldsymbol r)-N_\mathrm A^-(\boldsymbol r)\bigr),\qquad\boldsymbol{\mathcal E}=-\nabla\varphi. \tag{6.4}$$
:::

⁠**So liest man das:** Die Vorzeichen in [(6.3)](#gl-6-3) folgen aus Stufe [2](die-kontinuitatsgleichung.html#stufe-2) mit $\boldsymbol{\mathcal J}_\mathrm n=-\boldsymbol j_\mathrm n/e$ und $\boldsymbol{\mathcal J}_\mathrm p=+\boldsymbol j_\mathrm p/e$, $G$ und $R$ sind Quelle und Senke. $\rho$ ist hier die Ladungsdichte in C/cm$^3$, nicht der spezifische Widerstand aus [Teil 12](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/strom-im-halbleiter/strom-im-halbleiter.html). $\rho=0$ ist die Neutralität aus [Teil 11](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/eigenhalbleiter-und-dotierung/eigenhalbleiter-und-dotierung.html). Die Gleichung folgt aus $\operatorname{div}(\varepsilon_0\varepsilon_\mathrm r\boldsymbol{\mathcal E})=\rho$: Positive Ladung erzeugt einen Berg im Potential. Wegen $E_\mathrm C=\text{konst}-e\varphi$ gilt für die Bänder die __Poisson-Gleichung für den Bandverlauf__

<span class="anker" id="gl-6-5"></span>
$$\frac{\partial^2E_\mathrm C}{\partial x^2}=\frac{e\,\rho}{\varepsilon_0\varepsilon_\mathrm r}. \tag{6.5}$$

⁠**Gültigkeit:** Boltzmann-Näherung, $T$ konstant, Dichten ändern sich auf Längen weit über $l_\mathrm{mfp}$. Die Gleichungen sind gekoppelt und nichtlinear, denn $n\,\mathcal E$ ist ein Produkt zweier Unbekannter. Man löst sie gemeinsam und __selbstkonsistent__, also so, dass Feld und Dichten zueinander passen. Das leistet jede Bauelementsimulation.

:::herleitung Die Kontinuitätsgleichung als nulltes Moment
Summiert man [(0.1)](von-grund-auf-was-aus-fruheren-teilen-gebraucht-wird.html#gl-0-1) über alle $k$ ohne Faktor, entstehen $\partial n/\partial t$ und $\partial\mathcal J_\mathrm n/\partial x$. Die Summe von $\partial f/\partial k$ über eine Zone ist null, weil $f$ periodisch ist. Der Stoßterm enthält Stöße im Band und Generation mit Rekombination. Stöße im Band ändern die Zahl der Träger nicht, also bleibt rechts $G_\mathrm n-R_\mathrm n$. Ohne Feld und homogen ist $\partial f/\partial t=-(f-f^0)/\tau_\text{rec}$, und die Summe gibt $\partial\Delta n/\partial t=-\Delta n/\tau_\text{rec}=-(R_\mathrm n-G_\mathrm n)$, das Zerfallsgesetz. Das nullte Moment liefert die Kontinuität, das erste die Stromgleichung. Beschreibungsebenen von grob nach fein: Drift-Diffusion (makroskopisch, klassisch), Boltzmann-Gleichung (mikroskopisch, semiklassisch), __Nichtgleichgewichts-Green-Funktionen__ (quantenmechanisch).
:::

**Eine Richtung.** [(6.1)](#gl-6-1) und [(6.2)](#gl-6-2) in [(6.3)](#gl-6-3) ergeben, wenn $\mu_\mathrm n,\mu_\mathrm p,D_\mathrm n,D_\mathrm p$ nicht vom Ort abhängen,

<span class="anker" id="gl-6-6"></span>
<span class="anker" id="gl-6-7"></span>
$$\begin{aligned} \frac{\partial n}{\partial t}&=\frac{\partial}{\partial x}(n\,\mu_\mathrm n\mathcal E)+D_\mathrm n\frac{\partial^2n}{\partial x^2}+G_\mathrm n-R_\mathrm n=\frac{\partial n}{\partial x}\mu_\mathrm n\mathcal E+n\,\mu_\mathrm n\frac{\partial\mathcal E}{\partial x}+D_\mathrm n\frac{\partial^2n}{\partial x^2}+G_\mathrm n-R_\mathrm n,\\ \frac{\partial p}{\partial t}&=-\frac{\partial p}{\partial x}\mu_\mathrm p\mathcal E-p\,\mu_\mathrm p\frac{\partial\mathcal E}{\partial x}+D_\mathrm p\frac{\partial^2p}{\partial x^2}+G_\mathrm p-R_\mathrm p. \end{aligned} \tag{6.6|6.7}$$

Bei schwacher Injektion und gleichem $\tau_\text{rec}$ folgt daraus die Gleichung der Minderheit im p- und im n-Gebiet:

<span class="anker" id="gl-6-8"></span>
<span class="anker" id="gl-6-9"></span>
$$\begin{aligned} \frac{\partial\Delta n_\mathrm p}{\partial t}&=G_\mathrm n-\frac{\Delta n_\mathrm p}{\tau_\text{rec}}+\mu_\mathrm n\mathcal E\,\frac{\partial\Delta n_\mathrm p}{\partial x}+n_\mathrm p\mu_\mathrm n\frac{\partial\mathcal E}{\partial x}+D_\mathrm n\frac{\partial^2\Delta n_\mathrm p}{\partial x^2},\\ \frac{\partial\Delta p_\mathrm n}{\partial t}&=G_\mathrm p-\frac{\Delta p_\mathrm n}{\tau_\text{rec}}-\mu_\mathrm p\mathcal E\,\frac{\partial\Delta p_\mathrm n}{\partial x}-p_\mathrm n\mu_\mathrm p\frac{\partial\mathcal E}{\partial x}+D_\mathrm p\frac{\partial^2\Delta p_\mathrm n}{\partial x^2}. \end{aligned} \tag{6.8|6.9}$$

::::beispiel
Fehlen über 1 µ m nur $10^{12}\,\mathrm{cm^{-3}}$ Elektronen, ein Zehntausendstel von $N_\mathrm D$, entstehen schon $\mathcal E=1{,}5$ kV/m und 0,8 mV. Winzige Abweichungen von der Neutralität erzeugen also merkliche Felder.
::::

⁠**Grenzfälle:** Die früheren Ergebnisse sind Sonderfälle:

| Annahme | bleibt übrig | Ergebnis |
|---|---|---|
| homogen, $\mathcal E$ konstant, stationär | $j=(\sigma_\mathrm n+\sigma_\mathrm p)\mathcal E$ | ohmsches Gesetz |
| kein Feld, $G=R=0$ | $\partial n/\partial t=D_\mathrm n\,\partial^2n/\partial x^2$ | zweites Fick-Gesetz |
| $n$ im Ort konstant, $\mathcal E$ konstant | $\partial\Delta n/\partial t=-(R_\mathrm n-G_\mathrm n)=-\Delta n/\tau_\text{rec}$ | Zerfallsgesetz |
| Gleichgewicht, $j_\mathrm n=0$ | $e\,n\,\mu_\mathrm n\mathcal E=-e\,D_\mathrm n\,\mathrm{d} n/\mathrm{d} x$ | Einstein-Beziehung |

:::frage Warum steht bei den Elektronen $+\frac1e\nabla\cdot\boldsymbol j_\mathrm n$? Heißt mehr Strom hinaus nicht weniger Elektronen?
$\boldsymbol j_\mathrm n$ ist der elektrische Strom, er zeigt gegen die Laufrichtung der Elektronen. Strömt $\boldsymbol j_\mathrm n$ aus einem Volumen heraus, laufen Elektronen hinein, und $n$ steigt. Für die Teilchenstromdichte $\boldsymbol{\mathcal J}_\mathrm n$ steht wie immer das Minus.
:::

:::aufgabe Aufgabe 7 ★★ Gleichungen zuschneiden
<span class="anker" id="aufg-7"></span>

<ol class="al">

<li>

Leite [(6.9)](#gl-6-9) aus [(6.2)](#gl-6-2) und [(6.3)](#gl-6-3) her. Warum entfällt $p_{\mathrm n0}$? Welche Art von Differentialgleichung ist das?

</li>

<li>

Welche Terme bleiben für (i) homogene Beleuchtung ohne Feld, (ii) eine lokale Störung in einer dunklen Probe im konstanten Feld?

</li>

<li>

Ein Überschuss fällt wie $\mathrm{e}^{-x/L}$ mit $L=33$ µ m ab. Vergleiche Drift- und Diffusionsterm für $\mathcal E=1$ V/cm. Bei welchem Feld sind sie gleich?

</li>

<li>

Eine Schicht hat $\rho=e\cdot10^{15}\,\mathrm{cm^{-3}}$. Wie groß ist $\partial^2\varphi/\partial x^2$? Welche Spannung baut sie über 1 µ m auf, wenn $\mathcal E$ am Rand null ist?

</li>

</ol>

:::loesung
(a) [(6.2)](#gl-6-2) in [(6.3)](#gl-6-3) gibt [(6.7)](#gl-6-7). Mit $p_\mathrm n=p_{\mathrm n0}+\Delta p_\mathrm n$ und $R_\mathrm p=\Delta p_\mathrm n/\tau_\text{rec}$ folgt [(6.9)](#gl-6-9), denn $p_{\mathrm n0}$ ist in Ort und Zeit konstant. Für gegebenes $\mathcal E$ ist das eine lineare partielle Differentialgleichung zweiter Ordnung. (b) (i) $\partial\Delta p_\mathrm n/\partial t=G_\mathrm p-\Delta p_\mathrm n/\tau_\text{rec}$. (ii) Alle Terme außer $G_\mathrm p$ und dem mit $\partial\mathcal E/\partial x$. (c) Verhältnis Drift zu Diffusion $\mu_\mathrm p\mathcal EL/D_\mathrm p=\mathcal EL/(k_\mathrm BT/e)=0{,}13$. Gleich bei $\mathcal E=(k_\mathrm BT/e)/L=7{,}8$ V/cm. (d) $\partial^2\varphi/\partial x^2=-\rho/(\varepsilon_0\varepsilon_\mathrm r)=-1{,}55\cdot10^{12}\,\mathrm{V/m^2}$, $U=\frac12\cdot1{,}55\cdot10^{12}\,\mathrm{V/m^2}\cdot(1\,\mu\text{m})^2=0{,}77$ V.
:::
:::

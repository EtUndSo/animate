---
title: Stufe 3: Sprungantwort und Einschwingzeit
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / Tiefpass- und Bandpasssysteme
order: 3250400
summary: Wie reagiert der ideale Tiefpass auf einen Sprung?
tags: Integralsinus, Einschwingzeit
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Wie reagiert der ideale Tiefpass auf einen Sprung? Wie schnell steigt er, und wie weit schießt er über?
:::

Die Sprungantwort ist das laufende Integral der Impulsantwort ([Teil 1](/wissen/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html)). Mit dem __Integralsinus__

<span class="anker" id="gl-3-1"></span>
$$\operatorname{Si}(x)=\int_0^x\operatorname{si}(\xi)\,\mathrm{d}\xi,\qquad\operatorname{Si}(-x)=-\operatorname{Si}(x),\qquad\operatorname{Si}(\infty)=\frac\pi2 \tag{3.1}$$

ergibt sich

<span class="anker" id="gl-3-2"></span>
$$h_\varepsilon(t)=\int_{-\infty}^t2f_\mathrm g\operatorname{si}(2\pi f_\mathrm g\tau)\,\mathrm{d}\tau=\frac12+\frac1\pi\operatorname{Si}(2\pi f_\mathrm gt). \tag{3.2}$$

:::herleitung Sprungantwort
Das Integral bis $t$ teilt man bei 0. Der Teil von $-\infty$ bis 0 ist die halbe Fläche von $h$, also $\frac12H(0)=\frac12$, weil $h$ gerade ist. Für den Rest substituiert man $\xi=2\pi f_\mathrm g\tau$, $\mathrm{d}\tau=\mathrm{d}\xi/(2\pi f_\mathrm g)$: $\int_0^t2f_\mathrm g\operatorname{si}(2\pi f_\mathrm g\tau)\mathrm{d}\tau=\frac1\pi\operatorname{Si}(2\pi f_\mathrm gt)$. Den Wert $\operatorname{Si}(\infty)=\frac\pi2$ liefert der Flächensatz: $\int_{-\infty}^\infty\operatorname{si}(\pi u)\mathrm{d} u=1$, also $\int_0^\infty\operatorname{si}(\xi)\mathrm{d}\xi=\frac\pi2$.
:::

⁠**So liest man das:** Bei $t=0$ ist die Antwort genau $\frac12$, sie beginnt schon vorher (nicht kausal) und strebt gegen 1. Die __Einschwingzeit__ $t_e$ definiert man als Anstiegszeit einer Rampe mit der größten Steigung der Sprungantwort. Die größte Steigung ist $h(0)=2f_\mathrm g$, also

<span class="anker" id="gl-3-3"></span>
$$t_e=\frac{h_\varepsilon(\infty)}{\max\dot h_\varepsilon}=\frac{1}{2f_\mathrm g}. \tag{3.3}$$

Die Sprungantwort schießt um $8{,}95\,\%$ über (bei $t=\frac{1}{2f_\mathrm g}$). Das ist das Gibbs-Phänomen aus [Teil 3](/wissen/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html): Ein größeres $f_\mathrm g$ verkürzt die Einschwingzeit, das Überschwingen bleibt (Abb. [1](#abb-1)).

:::abbildung et3/k5sprung 1
Sprungantwort des idealen Tiefpasses für $f_\mathrm g=1$ Hz und 2 Hz. Gestrichelt die Rampe mit der größten Steigung: Ihre Anstiegszeit ist $t_e=1/(2f_\mathrm g)=0{,}5$ s. Beide Kurven schießen gleich weit über, auf 1,0895.
:::

:::frage Ein Tiefpass mit mehr Bandbreite ist doch „besser“. Warum wird das Überschwingen dann nicht kleiner?
Weil es von der *Form* des Frequenzgangs kommt, nicht von seiner Breite. Das Überschwingen entsteht an der senkrechten Kante bei $f_\mathrm g$: Alle Frequenzen bis dorthin kommen voll an, alle darüber gar nicht. Verschiebt man die Kante, bleibt sie senkrecht, und die Sprungantwort wird nur zeitlich gestaucht. Kleiner wird das Überschwingen erst, wenn die Kante weich wird (Stufe [5](echomethode-und-pulsformfilter.html#stufe-5)).
:::

:::aufgabe Aufgabe 3 ★★ Integralsinus
<span class="anker" id="aufg-3"></span>

<ol class="al">

<li>

Zeige $h_\varepsilon(0)=\frac12$ und $h_\varepsilon(\infty)=1$ mit [(3.1)](#gl-3-1).

</li>

<li>

Wo liegt das Maximum der Sprungantwort? Tipp: Die Ableitung der Sprungantwort ist die Impulsantwort.

</li>

</ol>

:::loesung
(a) $h_\varepsilon(0)=\frac12+\frac1\pi\operatorname{Si}(0)=\frac12$, $h_\varepsilon(\infty)=\frac12+\frac1\pi\cdot\frac\pi2=1$.

(b) Die Steigung der Sprungantwort ist $h(t)=2f_\mathrm g\operatorname{si}(2\pi f_\mathrm gt)$. Sie wird zum ersten Mal bei $2\pi f_\mathrm gt=\pi$ null und wechselt dort von positiv zu negativ. Das Maximum liegt also bei $t=\frac{1}{2f_\mathrm g}$ und ist $\frac12+\frac{\operatorname{Si}(\pi)}{\pi}=\frac12+\frac{1{,}852}{\pi}=1{,}0895$.
:::
:::

---
title: Stufe 5: Symmetrien im Signal und im Spektrum
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / Fourier-Reihe und -Transformation
order: 3230600
summary: Ob ein Signal reell, gerade oder ungerade ist, sieht man seinem Spektrum sofort an.
tags: gerade, ungerade
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Ob ein Signal reell, gerade oder ungerade ist, sieht man seinem Spektrum sofort an. Diese Stufe leitet die Regeln her.
:::

**Gerade und ungerade Anteile.** Eine komplexe Funktion heißt __gerade__, wenn $x(t)=x^*(-t)$, und __ungerade__, wenn $x(t)=-x^*(-t)$. (Für reelle Funktionen ist das die übliche Spiegel- bzw. Punktsymmetrie.) Jedes Signal zerfällt eindeutig in beide Anteile:

<span class="anker" id="gl-5-1"></span>
$$s(t)=s_g(t)+s_u(t),\qquad s_g(t)=\tfrac12\bigl[s(t)+s^*(-t)\bigr],\qquad s_u(t)=\tfrac12\bigl[s(t)-s^*(-t)\bigr]. \tag{5.1}$$

:::satz Satz 5.1 (Symmetrien)
<span class="anker" id="satz-5-1"></span>

<span class="anker" id="gl-5-2"></span>
$$s_g(t)\;\circ\!\!-\!\!\bullet\;\operatorname{Re}\{S(f)\},\qquad s_u(t)\;\circ\!\!-\!\!\bullet\;\mathrm{j}\operatorname{Im}\{S(f)\}. \tag{5.2}$$

Für **reelle** Signale gilt $S(-f)=S^*(f)$: Der Realteil und der Betrag $|S|$ sind gerade in $f$, der Imaginärteil und die Phase ungerade. Ein reelles, gerades Signal hat ein reelles, gerades Spektrum. Ein reelles, ungerades Signal hat ein rein imaginäres, ungerades Spektrum.
:::

:::herleitung Symmetrien
Zuerst: $\mathcal{F}\{s^*(-t)\}=\int s^*(-t)\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t$. Mit $\tau=-t$ ist das $\int s^*(\tau)\mathrm{e}^{\mathrm{j}2\pi f\tau}\mathrm{d}\tau=\bigl(\int s(\tau)\mathrm{e}^{-\mathrm{j}2\pi f\tau}\mathrm{d}\tau\bigr)^*=S^*(f)$. Damit

$$\mathcal{F}\{s_g\}=\tfrac12\bigl[S(f)+S^*(f)\bigr]=\operatorname{Re}\{S(f)\},\qquad\mathcal{F}\{s_u\}=\tfrac12\bigl[S(f)-S^*(f)\bigr]=\mathrm{j}\operatorname{Im}\{S(f)\}.$$

Für reelles $s$ ist $\mathcal{F}\{s^*(t)\}=\mathcal{F}\{s(t)\}$. Allgemein gilt $\mathcal{F}\{s^*(t)\}=\int s^*\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t=\bigl(\int s\,\mathrm{e}^{\mathrm{j}2\pi ft}\mathrm{d} t\bigr)^*=S^*(-f)$. Also $S(f)=S^*(-f)$.
:::

⁠**Kurz gesagt:** Bei einem reellen Signal ist die negative Hälfte des Spektrums das konjugierte Spiegelbild der positiven. Sie enthält keine neue Information.

::::beispiel
Der Exponentialimpuls $\varepsilon(t)\mathrm{e}^{-t}$ (reell) hat den geraden Anteil $\frac12\mathrm{e}^{-|t|}$ und den ungeraden $\frac12\operatorname{sgn}(t)\mathrm{e}^{-|t|}$. Sein Spektrum $H(f)=\frac{1}{1+\mathrm{j}2\pi f}$ hat den geraden Realteil $\frac{1}{1+(2\pi f)^2}$, die Transformierte von $\frac12\mathrm{e}^{-|t|}$, und den ungeraden Imaginärteil $\frac{-2\pi f}{1+(2\pi f)^2}$ (Abb. [5](#abb-5)).

:::abbildung et3/k3gerade 5
Der Exponentialimpuls ($RC=1$ s), zerlegt in einen geraden (blau) und einen ungeraden Anteil (rot). Rechts das Spektrum: Der gerade Anteil liefert den Realteil (gerade in $f$), der ungerade Anteil den Imaginärteil (ungerade in $f$).
:::
::::

:::aufgabe Aufgabe 5 ★ Symmetrie ablesen
<span class="anker" id="aufg-5"></span>

Was lässt sich ohne Rechnung über das Spektrum sagen? (a) $s(t)=\operatorname{rect}(t)$, (b) $s(t)=\operatorname{sgn}(t)\operatorname{rect}(t/2)$, (c) $s(t)=\mathrm{e}^{\mathrm{j}2\pi t}\operatorname{rect}(t)$, (d) ein reelles Signal mit $S(1\,\mathrm{Hz})=2-3\mathrm{j}$: Was ist $S(-1\,\mathrm{Hz})$?

:::loesung
(a) Reell und gerade: Spektrum reell und gerade ($\operatorname{si}(\pi f)$). (b) Reell und ungerade: Spektrum rein imaginär und ungerade. (c) Komplex, aber $x^*(-t)=\mathrm{e}^{-\mathrm{j}2\pi(-t)}\operatorname{rect}(-t)=x(t)$: Im Sinne der Definition ist das Signal gerade, also ist sein Spektrum reell. Nach der Modulationsregel ist es $\operatorname{si}(\pi(f-1))$, reell, aber nicht symmetrisch um $f=0$, weil das Signal nicht reell ist. (d) $S(-1\,\mathrm{Hz})=S^*(1\,\mathrm{Hz})=2+3\mathrm{j}$.
:::
:::

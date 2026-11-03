---
title: Stufe 2: Ein Signal aus lauter Bausteinen
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / Laplace-Transformation
order: 3220300
summary: Stufe 1 gilt für einen einzelnen Baustein.
tags: absolut integrierbares, Fourier-Darstellung, Spektrum
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Stufe [1](warum-gerade.html#stufe-1) gilt für einen einzelnen Baustein. Nützlich wird sie erst, wenn sich jedes Signal aus Bausteinen $\mathrm{e}^{pt}$ zusammensetzen lässt. Diese Stufe zeigt, dass das geht, wie die Gewichte heißen und wo die Grenzen liegen.
:::

### Ausgangspunkt $\sigma=0$: reine Schwingungen

<span class="anker" id="stufe-2-1"></span>

Auf der imaginären Achse ($\sigma=0$) sind die Bausteine reine Schwingungen $\mathrm{e}^{\mathrm{j}2\pi ft}$. Ein __absolut integrierbares__ Signal ($\int|s(t)|\,\mathrm{d} t<\infty$, es klingt also nach beiden Seiten schnell genug ab) lässt sich aus ihnen zusammensetzen. Das ist die __Fourier-Darstellung__. Hier genügt ihre Formel. Die Funktion $\mathcal{F}\{s\}(f)$ heißt __Spektrum__, sie gibt das Gewicht der Schwingung mit der Frequenz $f$ an:

$$s(t)=\int_{-\infty}^{\infty}\mathcal{F}\{s\}(f)\,\mathrm{e}^{\mathrm{j}2\pi ft}\,\mathrm{d} f,\qquad \mathcal{F}\{s\}(f)=\int_{-\infty}^{\infty}s(t)\,\mathrm{e}^{-\mathrm{j}2\pi ft}\,\mathrm{d} t.$$

Für viele Signale der Systemtheorie reicht das nicht. Der Sprung $\varepsilon(t)$ klingt nicht ab, $\mathrm{e}^{2t}\varepsilon(t)$ (die Impulsantwort eines instabilen Systems) wächst sogar. Aus Schwingungen mit konstanter Amplitude lässt sich ein Signal, das über alle Grenzen wächst, nicht zusammensetzen.

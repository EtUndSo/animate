---
title: Das Wichtigste
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Diffusion, Rekombination und Grundgleichungen
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/diffusion-rekombination-und-grundgleichungen
knoten: Kapitel 13: Diffusion, Rekombination und Grundgleichungen
order: 4231100
summary: Wie weit zusätzliche Ladungsträger kommen und welche Gleichungen alles zusammenfassen
tags: 
lang: de
---

:::kern Das Wichtigste
<ul>

<li>

⁠**Fick:** $\mathcal J=-D\,\partial N/\partial x$, $\partial N/\partial t=D\,\partial^2N/\partial x^2$, $D=D_0\exp(-E_\text{Diff}/(k_\mathrm BT))$. **Kontinuität:** $\partial N/\partial t=-\operatorname{div}\boldsymbol{\mathcal J}+r_\mathrm Q-r_\mathrm S$.

</li>

<li>

⁠**Quellen:** $N=N_0[1-\operatorname{erf}(x/x_0)]$, $N=N_0d\,\mathrm{e}^{-x^2/x_0^2}/\sqrt{\pi Dt}$, $x_0=2\sqrt{Dt}$.

</li>

<li>

⁠**Einstein:** $D_\mathrm n=(k_\mathrm BT/e)\,\mu_\mathrm n$, $D_\mathrm p=(k_\mathrm BT/e)\,\mu_\mathrm p$, $j_{\mathrm n,\text{diff}}=eD_\mathrm n\,\partial n/\partial x$, $j_{\mathrm p,\text{diff}}=-eD_\mathrm p\,\partial p/\partial x$.

</li>

<li>

⁠**Rekombination:** schwache Injektion: $R=\Delta p_\mathrm n/\tau_\text{rec}$, Abklingen mit $\mathrm{e}^{-t/\tau_\text{rec}}$, stationär $\Delta p_\mathrm n=G_\mathrm p\tau_\text{rec}$.

</li>

<li>

⁠**Grundgleichungen:** $\boldsymbol j_\mathrm n=en\mu_\mathrm n\boldsymbol{\mathcal E}+eD_\mathrm n\nabla n$, $\boldsymbol j_\mathrm p=ep\mu_\mathrm p\boldsymbol{\mathcal E}-eD_\mathrm p\nabla p$, $\partial_tn=\frac1e\nabla\cdot\boldsymbol j_\mathrm n+G_\mathrm n-R_\mathrm n$, $\partial_tp=-\frac1e\nabla\cdot\boldsymbol j_\mathrm p+G_\mathrm p-R_\mathrm p$, $\Delta\varphi=-e(p-n+N_\mathrm D^+-N_\mathrm A^-)/(\varepsilon_0\varepsilon_\mathrm r)$.

</li>

<li>

⁠**Relaxation:** $\tau_\varepsilon=\varepsilon_0\varepsilon_\mathrm r/\sigma$. Ambipolar: $D_\mathrm a=D_\mathrm nD_\mathrm p(n+p)/(nD_\mathrm n+pD_\mathrm p)$. **Diffusionslänge:** $\Delta p_\mathrm n(x)=\Delta p_\mathrm n(0)\mathrm{e}^{-x/L_\text{diff,p}}$, $L_\text{diff,p}=\sqrt{D_\mathrm p\tau_\text{rec}}$.

</li>

</ul>
:::

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Ungeordnete Bewegung treibt einen Strom gegen jedes Dichtegefälle, $\mathcal J=-D\,\partial N/\partial x$, und weil dieselben Stöße Diffusion und Drift begrenzen, ist $D_\mathrm n=(k_\mathrm BT/e)\,\mu_\mathrm n$, für Löcher ebenso.

</li>

<li>

Zusätzliche Paare verschwinden bei schwacher Injektion mit der Zeitkonstante $\tau_\text{rec}$ und kommen bis zur Diffusionslänge, im n-Gebiet $\sqrt{D_\mathrm p\tau_\text{rec}}$.

</li>

<li>

Stromgleichungen, Kontinuität und Poisson-Gleichung bilden einen geschlossenen Kreis, aus dem alle diese Ergebnisse als Sonderfälle folgen.

</li>

</ol>
:::

**Ein Prinzip hinter allen Ergebnissen.** Teilchen werden gezählt (Änderung gleich hinein minus heraus plus erzeugt minus vernichtet), und Ströme folgen aus Gefällen von Dichte und Potential.

| Ergebnis | Woher es kommt |
|---|---|
| Fick-Gesetze | Von der dichten Seite kommen mehr, ein Stromgefälle ändert $N$ (Stufe [1](warum-teilchen-ohne-kraft-stromen.html#stufe-1) und [2](die-kontinuitatsgleichung.html#stufe-2)) |
| Tiefe $\propto\sqrt{Dt}$ | Der Antrieb wird mit der Tiefe flacher (Stufe [3](erganzung-diffusion-aus-unendlicher-und-endlicher-quelle.html#stufe-3)) |
| $D_\mathrm n=(k_\mathrm BT/e)\,\mu_\mathrm n$ | Dieselben Stöße, und im Gleichgewicht ist der Strom null (Stufe [4](diffusionsstrom-und-einstein-beziehung.html#stufe-4)) |
| Zerfallsgesetz | Die Mehrheit bietet feste Partner, die Rate folgt dem Überschuss (Stufe [5](generation-und-rekombination.html#stufe-5)) |
| Grundgleichungen | Zählen je Sorte, Strom aus Gefällen, Feld aus Ladung (Stufe [6](die-grundgleichungen-der-halbleiter.html#stufe-6)) |
| $\tau_\varepsilon=\varepsilon_0\varepsilon_\mathrm r/\sigma$ | Zählen der Ladung, Strom aus ihrem eigenen Feld (Stufe [7](erganzung-raumladungen-und-relaxation.html#stufe-7)) |
| $L_\text{diff,p}=\sqrt{D_\mathrm p\tau_\text{rec}}$ | Zählen mit Senke: Diffusion füllt nach, was rekombiniert (Stufe [8](die-diffusionslange.html#stufe-8)) |

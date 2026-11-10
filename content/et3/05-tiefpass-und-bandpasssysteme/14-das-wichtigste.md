---
title: Das Wichtigste
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Tiefpass- und Bandpasssysteme
adresse: elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme
knoten: Kapitel 5: Tiefpass- und Bandpasssysteme
order: 3251400
summary: Verzerrungsfreie Übertragung, idealer Tiefpass, komplexe Hüllkurve und Gruppenlaufzeit
tags: 
lang: de
---

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Unverzerrt heißt: nur verstärkt und verzögert. Dazu braucht man einen konstanten Betrag und eine Phase, die linear mit der Frequenz fällt.

</li>

<li>

Ein scharf begrenzter (idealer) Tiefpass ist nicht kausal, schwingt bei Sprüngen um etwa 9 % über und braucht eine Einschwingzeit von $1/(2f_\mathrm g)$. Weichere Flanken verringern das Überschwingen auf Kosten der Schärfe.

</li>

<li>

Ein Bandpasssignal ist ein Tiefpasssignal (die komplexe Hüllkurve) auf einem Träger. Man rechnet mit der Hüllkurve wie mit einem Tiefpasssignal: Sie wird um die Gruppenlaufzeit verzögert, der Träger um die Phasenlaufzeit.

</li>

</ol>
:::

:::kern Das Wichtigste
<ul>

<li>

Verzerrungsfrei: $h=h_0\delta(t-t_0)$, $H=h_0\mathrm{e}^{-\mathrm{j}2\pi t_0f}$: konstanter Betrag, lineare Phase.

</li>

<li>

$a=-20\lg|H|$ dB; $t_\mathrm p=-\frac{\varphi}{2\pi f}$; $t_\mathrm g=-\frac{1}{2\pi}\frac{\mathrm{d}\varphi}{\mathrm{d} f}$.

</li>

<li>

Idealer Tiefpass: $\operatorname{rect}(f/2f_\mathrm g)\leftrightarrow2f_\mathrm g\operatorname{si}(2\pi f_\mathrm gt)$, nicht kausal; $f_\mathrm g t_m=\frac12$; Überschwingen 21,7 % (Impuls), 8,95 % (Sprung).

</li>

<li>

Sprungantwort $\frac12+\frac1\pi\operatorname{Si}(2\pi f_\mathrm gt)$, $\operatorname{Si}(\infty)=\frac\pi2$, Einschwingzeit $\frac{1}{2f_\mathrm g}$.

</li>

<li>

Abschneiden der Impulsantwort $=$ Faltung im Spektrum; weiche Fenster: tiefere Sperrung, flachere Flanke.

</li>

<li>

Pulsformfilter: $T\operatorname{rect}(Tf)[1+\cos(2\pi Tf)]$, wenig Überschwingen.

</li>

<li>

$H(f)=\frac12H_T(f-f_0)+\frac12H_T^*(-f-f_0)$; $s=\operatorname{Re}\{s_T\mathrm{e}^{\mathrm{j}2\pi f_0t}\}=s_{Tr}\cos-s_{Ti}\sin$; $s_T=2s_+\mathrm{e}^{-\mathrm{j}2\pi f_0t}$.

</li>

<li>

$g_T=\frac12s_T*h_T$; Hüllkurve um $t_\mathrm g$, Träger um $t_\mathrm p$ verzögert.

</li>

<li>

Bandpass-Abtastung: $2\Delta f$ Werte je Sekunde; digitaler Hochpass: $(-1)^nh_{\mathrm{TP}}(n)$.

</li>

</ul>
:::

**Ein Prinzip hinter allen Ergebnissen.**

| Ergebnis | Woher es kommt |
|---|---|
| verzerrungsfreies System | jede Schwingung gleich verstärkt und um dieselbe Zeit verzögert (Stufe [1](das-verzerrungsfreie-system.html#stufe-1)) |
| Phasen- und Gruppenlaufzeit | Verzögerung des Trägers bzw. der Hüllkurve (Stufen [1](das-verzerrungsfreie-system.html#stufe-1), [11](phasen-und-gruppenlaufzeit-beim-bandpass.html#stufe-11)) |
| Signaldauer $\cdot$ Bandbreite $=$ konst. | Ähnlichkeitssatz (Stufe [2](der-ideale-tiefpass.html#stufe-2)) |
| Überschwingen 21,7 % und 8,95 % | Nebenzipfel der si-Funktion, Gibbs (Stufen [2](der-ideale-tiefpass.html#stufe-2), [3](sprungantwort-und-einschwingzeit.html#stufe-3)) |
| kausale Näherung, Fensterentwurf | Abschneiden der Impulsantwort = Faltung im Spektrum (Stufen [4](kausale-naherung.html#stufe-4), [6](zeitdiskrete-tiefpasse-entwurf-mit-fenstern.html#stufe-6)) |
| Pulsformfilter | weiche Flanke im Spektrum, schnell abklingende Impulsantwort (Stufe [5](echomethode-und-pulsformfilter.html#stufe-5)) |
| äquivalenter Tiefpass, komplexe Hüllkurve | positive Frequenzen nach null verschieben (Stufen [7](der-ideale-bandpass-und-sein-aquivalenter-tiefpass.html#stufe-7), [8](komplexe-hullkurve-und-quadraturkomponenten.html#stufe-8)) |
| Quadraturschaltung, Bandpass-Abtastung | Bandpass im Tiefpassbereich rechnen (Stufe [10](quadraturschaltung-und-bandpass-abtastung.html#stufe-10)) |

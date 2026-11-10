---
title: Das Wichtigste
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Abtastung und zeitdiskrete Systeme
adresse: elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme
knoten: Kapitel 4: Abtastung und zeitdiskrete Systeme
order: 3241300
summary: Vom kontinuierlichen Signal zur Zahlenfolge: Abtasttheorem, diskrete Faltung, DFT, FFT und z-Transformation
tags: 
lang: de
---

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Abtasten ist Multiplizieren mit einem Dirac-Kamm. Im Spektrum wird daraus eine Faltung mit einem Kamm: Das Spektrum wiederholt sich periodisch mit der Abtastrate.

</li>

<li>

Liegen die Wiederholungen nicht übereinander (Abtastrate über der doppelten höchsten Frequenz), lässt sich das Signal mit einem idealen Tiefpass exakt zurückgewinnen. Andernfalls entsteht Aliasing.

</li>

<li>

Für Zahlenfolgen gelten dieselben Werkzeuge wie für Funktionen: Faltung als Summe, Fourier-Transformation mit periodischem Spektrum, DFT als deren Abtastwerte, z-Transformation als Gegenstück zur Laplace-Transformation.

</li>

</ol>
:::

:::kern Das Wichtigste
<ul>

<li>

Ideale Abtastung: $s_\mathrm a=\sum s(nT)\delta(t-nT)$; Spektrum $\frac1T\sum_kS(f-k/T)$, periodisch mit $1/T$.

</li>

<li>

Abtasttheorem: $f_\mathrm A\ge2f_\mathrm g$; Rückgewinnung $s(t)=\sum s(nT)\operatorname{si}(\pi(t-nT)/T)$; sonst Aliasing.

</li>

<li>

Diskret im einen Bereich heißt periodisch im anderen.

</li>

<li>

Diskrete Faltung $g(n)=\sum_ms(m)h(n-m)$; $h(n)=\operatorname{Tr}\{\delta(n)\}$; stabil: $\sum|h(n)|<\infty$.

</li>

<li>

Rekursiv $g(n)=s(n)+bg(n-1)$: $h(n)=b^n\varepsilon(n)$, $H_\mathrm a=\frac{1}{1-b\mathrm{e}^{-\mathrm{j}2\pi f}}$.

</li>

<li>

$S_\mathrm a(f)=\sum s(n)\mathrm{e}^{-\mathrm{j}2\pi nf}$, Periode 1; $s(n)=\int_{-1/2}^{1/2}S_\mathrm a\mathrm{e}^{\mathrm{j}2\pi nf}\mathrm{d} f$.

</li>

<li>

DFT: $S_d(k)=\sum_{n=0}^{M-1}s_d(n)\mathrm{e}^{-\mathrm{j}2\pi kn/M}$, $s_d=\frac1M\sum S_d\mathrm{e}^{\mathrm{j}2\pi kn/M}$; FFT $\approx M\,\mathrm{lb}\,M$; zyklische Faltung $\leftrightarrow S_dH_d$.

</li>

<li>

Herabtasten dehnt das Band (Aliasing, wenn $cf_\mathrm g>\frac12$), Hochtasten erzeugt Spiegelspektren.

</li>

<li>

$S(z)=\sum s(n)z^{-n}$; $z^{-n_0}$ = Verzögerung; $H(z)=\frac{\sum a_qz^{-q}}{1-\sum b_pz^{-p}}$; kausal und stabil: alle Pole in $|z|<1$.

</li>

</ul>
:::

**Ein Prinzip hinter allen Ergebnissen: Diskret in einem Bereich heißt periodisch im anderen.**

| Ergebnis | Woher es kommt |
|---|---|
| periodisches Spektrum nach Abtastung | Zeit diskret $\Rightarrow$ Spektrum periodisch (Stufe [2](das-spektrum-des-abgetasteten-signals.html#stufe-2)) |
| Abtasttheorem, Aliasing | ob sich die periodischen Kopien überlappen (Stufe [3](abtasttheorem-und-ruckgewinnung.html#stufe-3)) |
| si-Interpolation | idealer Tiefpass schneidet eine Kopie aus (Stufe [3](abtasttheorem-und-ruckgewinnung.html#stufe-3)) |
| Fourier-Reihe | Spektrum diskret $\Rightarrow$ Zeit periodisch (Stufe [4](abtastung-im-frequenzbereich.html#stufe-4)) |
| diskrete Faltung | Faltungsintegral über Dirac-gewichtete Abtastwerte (Stufe [5](zeitdiskrete-signale-und-die-diskrete-faltung.html#stufe-5)) |
| zeitdiskrete Fourier-Transformation | Spektrum der Abtastwerte, periodisch mit 1 (Stufe [7](fourier-transformation-zeitdiskreter-signale.html#stufe-7)) |
| DFT | beides diskret $\Rightarrow$ beides periodisch (Stufe [8](die-diskrete-fourier-transformation-dft.html#stufe-8)) |
| Dezimation, Interpolation | Abtasten einer schon abgetasteten Folge (Stufe [10](abtastrate-andern-dezimation-und-interpolation.html#stufe-10)) |
| z-Transformation | Laplace-Gedanke für Folgen: erst gewichten, dann transformieren (Stufe [11](die-z-transformation.html#stufe-11)) |

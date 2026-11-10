---
title: Stufe 8: Komplexe Hüllkurve und Quadraturkomponenten
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Tiefpass- und Bandpasssysteme
adresse: elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme
knoten: Kapitel 5: Tiefpass- und Bandpasssysteme
order: 3250900
summary: Was für Systeme gilt, gilt auch für Signale: Ein Bandpasssignal ist ein Tiefpasssignal auf einem Träger.
tags: komplexe Hüllkurve, komplexer Träger, Quadraturkomponenten, Einhüllende
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Was für Systeme gilt, gilt auch für Signale: Ein Bandpasssignal ist ein Tiefpasssignal auf einem Träger. Diese Stufe zeigt die verschiedenen Arten, das hinzuschreiben.
:::

Die Rücktransformation von [(7.2)](der-ideale-bandpass-und-sein-aquivalenter-tiefpass.html#gl-7-2) ergibt mit der Modulationsregel $h(t)=\frac12h_T(t)\mathrm{e}^{\mathrm{j}2\pi f_0t}+\frac12\bigl[h_T(t)\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr]^*$, also wegen $z+z^*=2\operatorname{Re} z$:

<span class="anker" id="gl-8-1"></span>
$$h(t)=\operatorname{Re}\bigl\{h_T(t)\,\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr\},\qquad s(t)=\operatorname{Re}\bigl\{s_T(t)\,\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr\}. \tag{8.1}$$

$s_T(t)$ heißt __komplexe Hüllkurve__, $\mathrm{e}^{\mathrm{j}2\pi f_0t}$ __komplexer Träger__. Ihr halbes Produkt ist die analytische Komponente aus [Kapitel 3](/wissen/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html), $s_+(t)=\frac12s_T(t)\mathrm{e}^{\mathrm{j}2\pi f_0t}$, also $s_T=2s_+\mathrm{e}^{-\mathrm{j}2\pi f_0t}$.

:::satz Satz 8.1 (Quadraturdarstellung)
<span class="anker" id="satz-8-1"></span>

Mit $s_T=s_{Tr}+\mathrm{j} s_{Ti}$ und der Hilbert-Transformierten $\hat s=s*\frac{1}{\pi t}$:

<span class="anker" id="gl-8-2"></span>
<span class="anker" id="gl-8-3"></span>
<span class="anker" id="gl-8-4"></span>
$$\begin{aligned} s(t)&=s_{Tr}(t)\cos(2\pi f_0t)-s_{Ti}(t)\sin(2\pi f_0t),\\ s_{Tr}(t)&=s(t)\cos(2\pi f_0t)+\hat s(t)\sin(2\pi f_0t),\qquad s_{Ti}(t)=\hat s(t)\cos(2\pi f_0t)-s(t)\sin(2\pi f_0t),\\ s(t)&=|s_T(t)|\cos\bigl(2\pi f_0t+\varphi_T(t)\bigr),\qquad|s_T|=\sqrt{s_{Tr}^2+s_{Ti}^2}. \end{aligned} \tag{8.2|8.3|8.4}$$
:::

⁠**So liest man das:** $s_{Tr}$ und $s_{Ti}$ heißen __Quadraturkomponenten__: Die eine moduliert den Kosinus, die andere den Sinus des Trägers. $|s_T|$ ist die __Einhüllende__, die man auf einem Oszilloskop als „Umriss“ des Signals sieht, und $\varphi_T$ die Phasenabweichung des Trägers. Ist die Hüllkurve reell (symmetrischer Fall), ist $s(t)=s_T(t)\cos(2\pi f_0t)$: ein amplitudenmodulierter Kosinus.

:::herleitung Quadraturkomponenten
[(8.2)](#gl-8-2): $\operatorname{Re}\{(s_{Tr}+\mathrm{j} s_{Ti})(\cos+\mathrm{j}\sin)\}=s_{Tr}\cos-s_{Ti}\sin$. Für [(8.3)](#gl-8-3): $2s_+=s+\mathrm{j}\hat s$ ([Kapitel 3](/wissen/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)), also

$$s_T=(s+\mathrm{j}\hat s)(\cos-\mathrm{j}\sin)=(s\cos+\hat s\sin)+\mathrm{j}(\hat s\cos-s\sin).$$
:::

:::aufgabe Aufgabe 8 ★★ Komplexe Hüllkurven bestimmen
<span class="anker" id="aufg-8"></span>

Bestimme $s_T$, $s_{Tr}$, $s_{Ti}$ und $|s_T|$ bezüglich $f_0=10$ Hz für (a) $s(t)=\bigl[1+0{,}5\cos(2\pi\cdot1\,\mathrm{Hz}\cdot t)\bigr]\cos(2\pi\cdot10\,\mathrm{Hz}\cdot t)$, (b) $s(t)=\cos(2\pi\cdot10\,\mathrm{Hz}\cdot t+0{,}3)$, (c) $s(t)=\sin(2\pi\cdot10\,\mathrm{Hz}\cdot t)$. Prüfe (c) mit [(8.2)](#gl-8-2).

:::loesung
(a) $s_T=1+0{,}5\cos(2\pi t)$, reell: $s_{Tr}=s_T$, $s_{Ti}=0$, $|s_T|=1+0{,}5\cos(2\pi t)$ zwischen 0,5 und 1,5. Ein amplitudenmodulierter Kosinus.

(b) $s_T=\mathrm{e}^{\mathrm{j}0{,}3}$: $s_{Tr}=\cos0{,}3=0{,}955$, $s_{Ti}=\sin0{,}3=0{,}296$, $|s_T|=1$. Die Hüllkurve ist konstant, nur die Phase ist um 0,3 verschoben.

(c) $\sin x=\operatorname{Re}\{-\mathrm{j}\,\mathrm{e}^{\mathrm{j} x}\}$, also $s_T=-\mathrm{j}$: $s_{Tr}=0$, $s_{Ti}=-1$, $|s_T|=1$. Probe: $0\cdot\cos-(-1)\sin=\sin$.
:::
:::

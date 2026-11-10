---
title: Stufe 6: Korrelation von Bandpasssignalen
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Korrelationsfunktionen
adresse: elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen
knoten: Kapitel 6: Korrelationsfunktionen
order: 3260700
summary: Auch Korrelationsfunktionen von Bandpasssignalen rechnet man mit den komplexen Hüllkurven (Kapitel 5).
tags: 
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Auch Korrelationsfunktionen von Bandpasssignalen rechnet man mit den komplexen Hüllkurven ([Kapitel 5](/wissen/elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme/tiefpass-und-bandpasssysteme.html)).
:::

Die KKF zweier reeller Bandpasssignale ist wieder ein Bandpasssignal:

$$\varphi^E_{sg}(\tau)=\operatorname{Re}\bigl\{\varphi^E_{sgT}(\tau)\,\mathrm{e}^{\mathrm{j}2\pi f_0\tau}\bigr\}.$$

Das gespiegelte Signal hat die Hüllkurve $s_T^*(-t)$, denn

$$s(-t)=\operatorname{Re}\bigl\{s_T(-t)\mathrm{e}^{-\mathrm{j}2\pi f_0t}\bigr\}=\operatorname{Re}\bigl\{s_T^*(-t)\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr\}.$$

Mit der Übertragungsregel $g_T=\frac12s_T*h_T$ aus [Kapitel 5](/wissen/elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme/tiefpass-und-bandpasssysteme.html):

<span class="anker" id="gl-6-1"></span>
$$\varphi^E_{sgT}(\tau)=\tfrac12\bigl[s_T^*(-\tau)*g_T(\tau)\bigr]=\tfrac12\int_{-\infty}^{\infty}s_T^*(t)\,g_T(t+\tau)\,\mathrm{d} t,\qquad E_s=\varphi^E_{ss}(0)=\varphi^E_{ssT}(0). \tag{6.1}$$

⁠**So liest man das:** Die Korrelation zweier Bandpasssignale ist die halbe Korrelation ihrer Hüllkurven, aufmoduliert auf den Träger. Die Energie eines Bandpasssignals ist die halbe Energie seiner komplexen Hüllkurve: Ein Kosinus der Amplitude $|s_T|$ hat im Mittel nur die halbe Leistung.

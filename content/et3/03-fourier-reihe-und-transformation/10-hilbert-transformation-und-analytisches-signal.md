---
title: Stufe 9: Hilbert-Transformation und analytisches Signal
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Fourier-Reihe und -Transformation
adresse: elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation
knoten: Kapitel 3: Fourier-Reihe und -Transformation
order: 3231000
summary: Bei einem kausalen Signal hängen Real- und Imaginärteil des Spektrums zusammen: Der eine legt den anderen fest.
tags: Hilbert-Transformation, analytische Komponente, Allpass
lang: de
---

<span class="anker" id="stufe-9"></span>

:::zweck
Bei einem kausalen Signal hängen Real- und Imaginärteil des Spektrums zusammen: Der eine legt den anderen fest. Dieselbe Rechnung liefert ein Signal, das nur positive Frequenzen enthält.
:::

**Kausale Signale.** Ist $s(t)=0$ für $t<0$, dann sind gerader und ungerader Anteil für $t>0$ gleich ($\frac12s$) und für $t<0$ entgegengesetzt. Also $s_u(t)=s_g(t)\operatorname{sgn}(t)$ und $s_g(t)=s_u(t)\operatorname{sgn}(t)$. Im Frequenzbereich wird die Multiplikation mit $\operatorname{sgn}$ zur Faltung mit $\frac{1}{\mathrm{j}\pi f}$:

:::satz Satz 9.1 (Hilbert-Beziehung kausaler Signale)
<span class="anker" id="satz-9-1"></span>

Für ein kausales Signal gilt

<span class="anker" id="gl-9-1"></span>
$$\operatorname{Re}\{S(f)\}=\operatorname{Im}\{S(f)\}*\frac{1}{\pi f},\qquad\operatorname{Im}\{S(f)\}=-\operatorname{Re}\{S(f)\}*\frac{1}{\pi f}. \tag{9.1}$$
:::

⁠**So liest man das:** Die Faltung mit $\frac{1}{\pi f}$ heißt __Hilbert-Transformation__. Bei einem kausalen System genügt es, den Realteil des Frequenzgangs zu kennen, der Imaginärteil folgt daraus. Kausalität ist also eine starke Einschränkung für das Spektrum.

**Analytische Komponente.** Mit dem Sprung im *Frequenzbereich* schneidet man die negativen Frequenzen ab: $S_+(f)=S(f)\,\varepsilon(f)$. Aus der Symmetrie folgt $\varepsilon(f)\;\bullet\!\!-\!\!\circ\;\frac12\delta(t)+\frac{\mathrm{j}}{2\pi t}$, also

<span class="anker" id="gl-9-2"></span>
$$s_+(t)=\frac12s(t)+\frac{\mathrm{j}}{2}\,\hat s(t),\qquad\hat s(t)=s(t)*\frac{1}{\pi t}\;\circ\!\!-\!\!\bullet\;-\mathrm{j}\operatorname{sgn}(f)\,S(f). \tag{9.2}$$

$s_+$ heißt __analytische Komponente__, $\hat s$ die Hilbert-Transformierte von $s$. Für reelle Signale ist $S_-(f)=S_+^*(-f)$, also $s_-=s_+^*$ und $s(t)=s_++s_-=2\operatorname{Re}\{s_+(t)\}$. Real- und Imaginärteil von $s_+$ sind wieder Hilbert-Transformierte voneinander.

**Der Hilbert-Transformator.** Das LTI-System mit $h(t)=\frac{1}{\pi t}$ hat $H(f)=-\mathrm{j}\operatorname{sgn}(f)$: Betrag 1 bei allen Frequenzen (ein __Allpass__), Phase $-90^\circ$ für $f>0$ und $+90^\circ$ für $f<0$. Aus $\cos(2\pi Ft)$ macht er

$$\tfrac12\bigl[\delta(f+F)+\delta(f-F)\bigr]\cdot\bigl(-\mathrm{j}\operatorname{sgn}(f)\bigr)=\tfrac{\mathrm{j}}{2}\delta(f+F)-\tfrac{\mathrm{j}}{2}\delta(f-F)\;\bullet\!\!-\!\!\circ\;\sin(2\pi Ft).$$

⁠**Kurz gesagt:** Der Hilbert-Transformator dreht jede Schwingung um $90^\circ$, ohne ihre Amplitude zu ändern.

:::aufgabe Aufgabe 12 ★★ Hilbert-Transformator
<span class="anker" id="aufg-12"></span>

<ol class="al">

<li>

Was macht der Hilbert-Transformator aus $\sin(2\pi Ft)$? Was ergibt zweimaliges Anwenden?

</li>

<li>

Bestimme die analytische Komponente $s_+(t)$ von $\cos(2\pi Ft)$ und prüfe $s=2\operatorname{Re}\{s_+\}$.

</li>

<li>

Warum ist der Hilbert-Transformator nicht kausal? Schau auf $h(t)$.

</li>

</ol>

:::loesung
(a) $\sin(2\pi Ft)\circ\!\!-\!\!\bullet\frac{\mathrm{j}}{2}\delta(f+F)-\frac{\mathrm{j}}{2}\delta(f-F)$. Multiplikation mit $-\mathrm{j}\operatorname{sgn}(f)$: bei $-F$ mit $+\mathrm{j}$, bei $+F$ mit $-\mathrm{j}$. Ergebnis $-\frac12\delta(f+F)-\frac12\delta(f-F)$, also $-\cos(2\pi Ft)$. Zweimal angewandt: $(-\mathrm{j}\operatorname{sgn}f)^2=-1$, das Signal wird invertiert.

(b) $S_+(f)=S(f)\varepsilon(f)=\frac12\delta(f-F)$, also $s_+(t)=\frac12\mathrm{e}^{\mathrm{j}2\pi Ft}=\frac12\bigl[\cos(2\pi Ft)+\mathrm{j}\sin(2\pi Ft)\bigr]$. Das passt zu $\frac12(s+\mathrm{j}\hat s)$ mit $\hat s=\sin$. $2\operatorname{Re}\{s_+\}=\cos(2\pi Ft)$.

(c) $h(t)=\frac{1}{\pi t}$ ist auch für $t<0$ von null verschieden. Der Ausgang zur Zeit $t$ hängt also von zukünftigen Eingangswerten ab. In der Praxis nähert man den Hilbert-Transformator mit einer abgeschnittenen Impulsantwort und nimmt dafür eine Verzögerung in Kauf.
:::
:::

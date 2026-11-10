---
title: Stufe 9: Bandpasssignal durch Bandpasssystem
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Tiefpass- und Bandpasssysteme
adresse: elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme
knoten: Kapitel 5: Tiefpass- und Bandpasssysteme
order: 3251000
summary: Der Nutzen der Hüllkurven: Wie ein Bandpass auf ein Bandpasssignal wirkt, rechnet man vollständig im Tiefpassbereich.
tags: 
lang: de
---

<span class="anker" id="stufe-9"></span>

:::zweck
Der Nutzen der Hüllkurven: Wie ein Bandpass auf ein Bandpasssignal wirkt, rechnet man vollständig im Tiefpassbereich.
:::

:::satz Satz 9.1 (Übertragung im äquivalenten Tiefpassbereich)
<span class="anker" id="satz-9-1"></span>

Erfüllen $S_T$ und $H_T$ beide [(7.2)](der-ideale-bandpass-und-sein-aquivalenter-tiefpass.html#gl-7-2) (nichts unterhalb von $-f_0$), dann gilt für die Hüllkurve des Ausgangs

<span class="anker" id="gl-9-1"></span>
$$G_T(f)=\tfrac12S_T(f)\,H_T(f)\qquad\bullet\!\!-\!\!\circ\qquad g_T(t)=\tfrac12\bigl[s_T(t)*h_T(t)\bigr],\qquad g(t)=\operatorname{Re}\bigl\{g_T(t)\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr\}. \tag{9.1}$$
:::

:::herleitung Übertragung
$G=S\cdot H$ mit beiden Darstellungen [(7.2)](der-ideale-bandpass-und-sein-aquivalenter-tiefpass.html#gl-7-2) ausmultipliziert gibt vier Produkte. Die gemischten, etwa $S_T(f-f_0)H_T^*(-f-f_0)$, sind null: Der erste Faktor lebt bei positiven, der zweite bei negativen Frequenzen. Es bleibt $G=\frac14S_T(f-f_0)H_T(f-f_0)+\frac14S_T^*(-f-f_0)H_T^*(-f-f_0)$. Der Vergleich mit $G=\frac12G_T(f-f_0)+\frac12G_T^*(-f-f_0)$ gibt $G_T=\frac12S_TH_T$.
:::

⁠**So liest man das:** Der Faktor $\frac12$ gleicht aus, dass $S_T$ und $H_T$ beide verdoppelt wurden. Sonst ist es der gewohnte Faltungssatz, nur für die Hüllkurven. Der Träger muss gar nicht mitgerechnet werden.

::::beispiel eingeschalteter Kosinus durch den idealen Bandpass
$s(t)=\varepsilon(t)\cos(2\pi f_0t)$ mit $f_0=10$ Hz, Bandpass mit $\Delta f=2$ Hz um $f_0$. Die Hüllkurve des Eingangs ist $s_T\approx\varepsilon(t)$. (Näherung: Das Spektrum des Sprungs ist nicht auf $f>-f_0$ begrenzt, im Durchlassbereich $|f|\le\Delta f/2\ll f_0$ stimmt es aber.) Mit $h_T=2\Delta f\operatorname{si}(\pi\Delta f\,t)$:

$$g_T(t)\approx\tfrac12\bigl[\varepsilon(t)*2\Delta f\operatorname{si}(\pi\Delta f\,t)\bigr]=\frac12+\frac1\pi\operatorname{Si}(\pi\Delta f\,t),\qquad g(t)\approx\Bigl[\frac12+\frac1\pi\operatorname{Si}(\pi\Delta f\,t)\Bigr]\cos(2\pi f_0t).$$

Die Hüllkurve ist die Sprungantwort eines idealen Tiefpasses mit $f_\mathrm g=\Delta f/2$: Einschwingzeit $1/\Delta f=0{,}5$ s, Überschwingen 8,95 % (Abb. [5](#abb-5)). Ein schmaler Bandpass braucht lange, bis er „eingeschwungen“ ist.

:::abbildung et3/k5bandpass 5
Antwort des idealen Bandpasses ($f_0=10$ Hz, $\Delta f=2$ Hz) auf einen bei $t=0$ eingeschalteten Kosinus der Mittenfrequenz. Blau das Ausgangssignal, rot die Einhüllende $\pm g_T(t)$. Sie steigt in etwa 0,5 s an und schwingt auf 1,09 über.
:::
::::

:::ltspice Eingeschalteter Träger durch einen Schwingkreis
Einen idealen Bandpass kann man nicht bauen, einen Reihenschwingkreis schon. **Zeichnen:** Quelle `voltage` am Netz `in`, dann in Reihe `ind` mit `{L}`, `cap` mit `{1/((2*pi*f0)**2*L)}` und `res` mit `{2*pi*df*L}` nach Masse. Der Ausgang `out` ist die Spannung am Widerstand. Mit `.param f0=10 df=2 L=1` ist die Mittenfrequenz 10 Hz und die Bandbreite zwischen den $-3$-dB-Punkten 2 Hz.

⁠**Kontrolle:** Quellwert `AC 1` und `.ac lin 2001 5 15` zeigen das Maximum 1 bei 10 Hz und die $-3$-dB-Punkte bei 9,05 Hz und 11,05 Hz.

⁠**Versuch:** Quelle `SINE(0 1 10 0 0 90)`, das ist $\varepsilon(t)\cos(2\pi f_0t)$, und `.tran 0 3 0 0.1m`. Die Hüllkurve steigt ohne Überschwingen an: Die Spitzen des Trägers erreichen 0,72 bei 0,2 s, 0,96 bei 0,5 s und praktisch 1 nach 1 s, fast genau wie $1-\mathrm{e}^{-t/0{,}16\,\mathrm s}$. Der ideale Bandpass schwingt dagegen auf 1,09 über (Abb. [5](#abb-5)). Der Grund ist derselbe wie beim Tiefpass in Stufe [3](sprungantwort-und-einschwingzeit.html#stufe-3): Die Flanken des Schwingkreises sind weich, die des idealen Bandpasses senkrecht.
:::

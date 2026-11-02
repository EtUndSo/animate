---
title: Stufe 7: Zeitdiskrete und periodische Korrelation
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / Korrelationsfunktionen
order: 3260800
summary: Für Abtastwerte wird aus dem Integral eine Summe.
tags: schnelle Korrelation
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Für Abtastwerte wird aus dem Integral eine Summe. Mit der DFT rechnet man Korrelationen schnell.
:::

:::satz Satz 7.1 (Zeitdiskrete Korrelation)
<span class="anker" id="satz-7-1"></span>

<span class="anker" id="gl-7-1"></span>
$$\varphi^E_{sg}(m)=\sum_{n=-\infty}^{\infty}s^*(n)\,g(n+m)=s^*(-m)*g(m),\qquad E_s=\sum_n|s(n)|^2=\int_{-1/2}^{1/2}|S_\mathrm a(f)|^2\,\mathrm{d} f, \tag{7.1}$$

<span class="anker" id="gl-7-2"></span>
$$\varphi^E_{ss}(m)\;\circ\!\!-\!\!\bullet\;|S_\mathrm a(f)|^2\ (\text{Periode }1),\qquad\varphi^E_{gg}(m)=\varphi^E_{ss}(m)*\varphi^E_{hh}(m). \tag{7.2}$$
:::

Für abgetastete Tiefpasssignale gilt $\varphi^E_{sg}(mT)=T\sum_ns^*(nT)g((n+m)T)$ und $E_s=T\sum_n|s(nT)|^2$. Ein zeitdiskretes Energiesignal ist eine quadratisch summierbare Folge.

**Beispiel.** $s=(1,2,1)$: $\varphi^E_{ss}=(1,4,6,4,1)$ für $m=-2,\dots,2$. Maximum $6=E_s$ bei $m=0$, gerade, fünf Werte statt drei. Probe mit Wiener-Khintchine bei $f=0$: $|S_\mathrm a(0)|^2=(1+2+1)^2=16=\sum_m\varphi^E_{ss}(m)$.

**Periodische Korrelation.** Wie bei der Faltung ([Teil 4](/wissen/elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme/abtastung-und-zeitdiskrete-systeme.html)) gilt für Folgen der Periode $M$

<span class="anker" id="gl-7-3"></span>
$$\varphi^E_{sgd}(m)=\sum_{n=0}^{M-1}s_d^*(n)\,g_d(n+m)\;\circ\!\!-\!\!\bullet\;S_d^*(k)\,G_d(k). \tag{7.3}$$

Mit der FFT berechnet heißt das __schnelle Korrelation__. Damit die periodische Korrelation die gewöhnliche wiedergibt, muss $M$ groß genug sein. Für $(1,2,1)$ ergibt $M=3$ die überlappte Folge $(6,5,5)$, $M=5$ dagegen $(6,4,1,1,4)$, die gewöhnliche AKF zyklisch angeordnet.

**Leistungssignale.** Für Signale unendlicher Energie mittelt man:

<span class="anker" id="gl-7-4"></span>
$$\varphi^L_{sg}(\tau)=\lim_{T\to\infty}\frac1T\int_{-T/2}^{T/2}s^*(t)\,g(t+\tau)\,\mathrm{d} t. \tag{7.4}$$

Sind beide Signale mit derselben Periode periodisch, genügt eine Periode, und die Korrelationsfunktion ist ebenfalls periodisch. Beispiel: $A\cos(2\pi Ft+\varphi_0)$ hat die AKF $\frac{A^2}{2}\cos(2\pi F\tau)$. Die Phase $\varphi_0$ ist verschwunden, bei $\tau=0$ steht die Leistung $\frac{A^2}{2}$.

:::aufgabe Aufgabe 6 ★ Diskrete AKF
<span class="anker" id="aufg-6"></span>

<ol class="al">

<li>

Rechne die AKF von $(1,2,1)$ von Hand nach.

</li>

<li>

Bestimme die AKF von $(1,-1)$. Was sagt $\varphi(\pm1)<0$ über das Signal?

</li>

</ol>

:::loesung
(a) $\varphi(0)=1+4+1=6$, $\varphi(\pm1)=1\cdot2+2\cdot1=4$, $\varphi(\pm2)=1\cdot1=1$.

(b) $\varphi(0)=2$, $\varphi(\pm1)=-1$. Ein negativer Wert bei der Verschiebung 1 heißt: Benachbarte Werte haben eher entgegengesetztes Vorzeichen, das Signal wechselt schnell. Passend dazu ist $|S_\mathrm a(f)|^2=|1-\mathrm{e}^{-\mathrm{j}2\pi f}|^2=2-2\cos(2\pi f)$ bei $f=0$ null und bei $f=\frac12$ maximal: ein Hochpasssignal.
:::
:::

:::aufgabe Aufgabe 7 ★★ AKF eines Kosinus
<span class="anker" id="aufg-7"></span>

Leite die AKF von $A\cos(2\pi Ft+\varphi_0)$ mit [(7.4)](#gl-7-4) über eine Periode her. Warum fällt $\varphi_0$ heraus, und was bedeutet das für die Messung der Phase mit der AKF?

:::loesung
Mit $\omega=2\pi F$ und $\cos a\cos b=\frac12[\cos(a-b)+\cos(a+b)]$:

$$\frac1T\int_0^TA^2\cos(\omega t+\varphi_0)\cos(\omega t+\omega\tau+\varphi_0)\mathrm{d} t=\frac{A^2}{2}\cos(\omega\tau)+\frac{A^2}{2T}\int_0^T\cos(2\omega t+\omega\tau+2\varphi_0)\mathrm{d} t.$$

Das zweite Integral läuft über zwei volle Perioden und ist null. $\varphi_0$ verschiebt nur den Zeitnullpunkt, und die Mittelung über alle Zeiten kennt keinen Nullpunkt. Mit der AKF eines einzelnen Signals kann man deshalb keine Phase messen. Die Phasendifferenz *zweier* Signale zeigt dagegen die Kreuzkorrelation.
:::
:::

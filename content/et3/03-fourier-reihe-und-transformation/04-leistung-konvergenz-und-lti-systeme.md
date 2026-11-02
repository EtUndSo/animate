---
title: Stufe 3: Leistung, Konvergenz und LTI-Systeme
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / Fourier-Reihe und -Transformation
order: 3230400
summary: Wie viel trägt jede Harmonische zum Signal bei, wie gut nähert eine abgebrochene Reihe das Signal, und was macht ein LTI-System mit einem periodischen Eingang?
tags: Leistung, Teilsumme, Gibbs-Phänomen
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Wie viel trägt jede Harmonische zum Signal bei, wie gut nähert eine abgebrochene Reihe das Signal, und was macht ein LTI-System mit einem periodischen Eingang?
:::

:::satz Satz 3.1 (Parseval für Fourier-Reihen)
<span class="anker" id="satz-3-1"></span>

<span class="anker" id="gl-3-1"></span>
$$L_s=\frac1T\int_0^T|s_p(t)|^2\,\mathrm{d} t=\sum_{k=-\infty}^{\infty}|S_p(k)|^2. \tag{3.1}$$
:::

⁠**So liest man das:** Die mittlere __Leistung__ des Signals ist die Summe der Leistungen der einzelnen Harmonischen. Mischterme fallen weg, weil verschiedene Harmonische orthogonal sind. Für die Rechteckschwingung ist $L_s=\frac12$. Der Gleichanteil trägt $0{,}25$ bei, also 50 %. Mit $k=\pm1$ sind es 90,5 %, mit $|k|\le3$ 95,0 %, mit $|k|\le9$ 98,0 %.

:::herleitung Parseval
$|s_p|^2=s_ps_p^*=\sum_k\sum_lS_p(k)S_p^*(l)\,\mathrm{e}^{\mathrm{j}2\pi(k-l)Ft}$. Über eine Periode gemittelt bleibt nach [(2.4)](periodische-signale-die-fourier-reihe.html#gl-2-4) nur $k=l$: $\sum_k|S_p(k)|^2$.
:::

**Abgebrochene Reihe und Gibbs-Phänomen.** Nimmt man nur die Harmonischen bis $|k|\le N$, ist die __Teilsumme__ $s_{p,N}(t)=\sum_{k=-N}^{N}S_p(k)\mathrm{e}^{\mathrm{j}2\pi kFt}$. Die Leistung des Fehlers $s_p-s_{p,N}$ ist die Summe der weggelassenen $|S_p(k)|^2$ und geht für $N\to\infty$ gegen null, wenn das Signal eine endliche Leistung hat. An einer Sprungstelle bleibt aber ein Überschwinger stehen (Abb. [2](#abb-2)): Er wird mit wachsendem $N$ schmaler, seine Höhe strebt aber gegen etwa 9 % der Sprunghöhe (10,0 % bei $N=3$, 9,1 % bei $N=9$, 9,0 % bei $N=27$, Grenzwert 8,95 %). Das ist das __Gibbs-Phänomen__. Es widerspricht der Konvergenz nicht: Die Fläche unter dem Überschwinger und damit die Fehlerleistung geht trotzdem gegen null.

:::abbildung et3/k3gibbs 2
Teilsummen der Rechteckschwingung ($T=2\pi$ s) mit den Harmonischen bis $|k|\le N$. An den Kanten bleibt ein Überschwinger von etwa 9 % der Sprunghöhe, der mit wachsendem $N$ nur schmaler wird.
:::

**Periodischer Eingang an einem LTI-System.** Jede Harmonische ist eine Eigenfunktion und wird mit $H(kF)$ multipliziert. Der Ausgang hat deshalb dieselbe Periode, und seine Koeffizienten sind

<span class="anker" id="gl-3-2"></span>
$$G_p(k)=S_p(k)\,H(kF). \tag{3.2}$$

Im Rechenmodell ist $H(kF)=1/(1+\mathrm{j} k)$. Die Grundschwingung wird mit $|H|=0{,}707$ und $-45^\circ$ übertragen, die dritte Harmonische mit $0{,}316$ und $-71{,}6^\circ$, die fünfte mit $0{,}196$ und $-78{,}7^\circ$. Am Ausgang ist die dritte Harmonische nur noch 15 % so groß wie die erste statt 33 % am Eingang. Das RC-Glied rundet die Kanten ab (Abb. [3](#abb-3)). Der Ausgang pendelt zwischen 0,041 und 0,959.

:::abbildung et3/k3rc 3
Rechteckschwingung durch den RC-Tiefpass mit $RC=1$ s, berechnet als Summe der Harmonischen mit $G_p(k)=S_p(k)/(1+\mathrm{j} k)$. Der Ausgang lädt und entlädt sich exponentiell zwischen 0,041 und 0,959.
:::

:::frage Ist eine Rechnung über unendlich viele Harmonische nicht viel umständlicher als die Differentialgleichung?
Für eine einzelne Rechteckschwingung durch ein RC-Glied ja: Lade- und Entladekurve kann man direkt hinschreiben. Die Reihe zeigt dafür, *warum* der Ausgang so aussieht. Die Kanten bestehen aus den hohen Harmonischen, und genau diese schwächt das RC-Glied. Außerdem funktioniert [(3.2)](#gl-3-2) für jedes LTI-System, auch für solche, deren Differentialgleichung man gar nicht kennt, sondern nur ihren gemessenen Frequenzgang.
:::

:::ltspice Rechteckschwingung durch das RC-Glied
⁠**Zeichnen:** RC-Glied (`res` mit `1Meg`, `cap` mit `1u`) mit der Quelle `PULSE(0 1 0 1u 1u {pi} {2*pi})`: Periode $2\pi$ s, Tastgrad $\frac12$.

⁠**Direktiven:** `.tran 0 {20*pi} 0 1m`, `.four {1/(2*pi)} 5 V(in) V(out)` und `.options plotwinsize=0`. Die letzte schaltet die Datenkompression ab, ohne sie rechnet `.four` ungenau. `.four` zerlegt die letzte Periode in Harmonische und schreibt das Ergebnis ins SPICE Error Log.

⁠**Was du siehst:** Im eingeschwungenen Zustand pendelt `V(out)` zwischen 0,041 und 0,959. `.four` gibt für $k\ge1$ die Amplituden $2|S_p(k)|$ der Kosinusschwingungen in [(2.2)](periodische-signale-die-fourier-reihe.html#gl-2-2) an. Am Eingang sind das 0,637; 0; 0,212; 0; 0,127: Die geraden Harmonischen fehlen. Am Ausgang ist die dritte Harmonische nur noch 15 % so groß wie die erste statt 33 %. Die Phasen am Ausgang sind um $45^\circ$, $71{,}6^\circ$ und $78{,}7^\circ$ größer als am Eingang, denn `.four` zählt eine Nacheilung positiv. Halbiere die Ausgangsamplituden und vergleiche mit deinem Ergebnis aus Aufgabe [3](#aufg-3)(b). Die FFT-Ansicht (Rechtsklick ins Diagramm, View, FFT) zeigt dieselben Linien bei den ungeraden Vielfachen von 0,159 Hz.
:::

:::aufgabe Aufgabe 3 ★★ Leistung und Oberschwingungen
<span class="anker" id="aufg-3"></span>

<ol class="al">

<li>

Bestätige mit [(3.1)](#gl-3-1): Die Harmonischen $k=0,\pm1$ der Rechteckschwingung tragen 90,5 % der Leistung.

</li>

<li>

Berechne $|G_p(1)|$, $|G_p(3)|$, $|G_p(5)|$ für den RC-Ausgang. Welcher Anteil der Wechselleistung des Ausgangs (ohne $k=0$) steckt in der Grundschwingung, wenn du nur $k=\pm1,\pm3,\pm5$ berücksichtigst?

</li>

<li>

Warum sieht der Ausgang schon „sinusähnlicher“ aus als der Eingang?

</li>

</ol>

:::loesung
(a) $|S_p(0)|^2+2|S_p(1)|^2=0{,}25+2/\pi^2=0{,}25+0{,}2026=0{,}4526$, von $0{,}5$ sind das 90,5 %.

(b) $|G_p(k)|=|S_p(k)|/\sqrt{1+k^2}$: $|G_p(1)|=0{,}2251$, $|G_p(3)|=0{,}0336$, $|G_p(5)|=0{,}0125$. Wechselleistung aus diesen Harmonischen: $2(0{,}0507+0{,}0011+0{,}0002)=0{,}1039$. Der Anteil der Grundschwingung ist $0{,}0507/0{,}0519=97{,}5\,\%$. Am Eingang wären es für dieselben Harmonischen nur 86,9 %.

(c) $|H(kF)|=1/\sqrt{1+k^2}\approx1/k$: Die Oberschwingungen werden umso stärker geschwächt, je höher sie sind. Übrig bleibt vor allem die Grundschwingung, und ein Signal, das fast nur aus der Grundschwingung besteht, ist fast ein Sinus.
:::
:::

---
title: Stufe 10: Das Korrelationsfilter (Matched Filter)
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Zufallssignale
adresse: elektrotechnik/3-semester/signale-und-systeme/zufallssignale
knoten: Kapitel 7: Zufallssignale
order: 3271100
summary: Ein bekannter Impuls s(t) kommt verrauscht an.
tags: Korrelationsfilter, Korrelator
lang: de
---

<span class="anker" id="stufe-10"></span>

:::zweck
Ein bekannter Impuls $s(t)$ kommt verrauscht an. Mit welchem Filter wird er im Abtastzeitpunkt $T$ am deutlichsten sichtbar?
:::

**Der Ansatz.** Am Empfängereingang liegt $s(t)+n(t)$ mit weißem Rauschen $n$. Ein Filter $h$ liefert $y=g+n_e$ mit dem Nutzanteil $g=s*h$ und dem Störanteil $n_e=n*h$. Abgetastet wird bei $T$. Das Signal-Rausch-Verhältnis dort ist

$$\frac{S_a}{N}=\frac{g^2(T)}{\mathrm E\{n_e^2(T)\}}=\frac{\bigl[\int h(\tau)s(T-\tau)\mathrm{d}\tau\bigr]^2}{N_0\int|h(\tau)|^2\mathrm{d}\tau}=\frac{E_s}{N_0}\cdot\underbrace{\frac{\bigl[\int h(\tau)s(T-\tau)\mathrm{d}\tau\bigr]^2}{\int|h|^2\mathrm{d}\tau\int|s(T-\tau)|^2\mathrm{d}\tau}}_{=|p|^2\le1}.$$

Der rechte Bruch ist das Quadrat eines Korrelationskoeffizienten ([Kapitel 6](/wissen/elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen/korrelationsfunktionen.html)), zwischen $h(\tau)$ und $s(T-\tau)$. Er ist höchstens 1, und zwar genau dann, wenn beide dieselbe Form haben.

:::satz Satz 10.1 (Korrelationsfilter)
<span class="anker" id="satz-10-1"></span>

Gegen weißes Rauschen ist das beste erreichbare Signal-Rausch-Verhältnis

<span class="anker" id="gl-10-1"></span>
$$\Bigl(\frac{S_a}{N}\Bigr)_{\max}=\frac{E_s}{N_0},\qquad\text{erreicht mit}\qquad h(t)=a\,s(T-t),\quad H(f)=a\,S^*(f)\,\mathrm{e}^{-\mathrm{j}2\pi fT}. \tag{10.1}$$
:::

⁠**So liest man das:** Die beste Impulsantwort ist das zeitgespiegelte, um $T$ verschobene Signal selbst, das __Korrelationsfilter__ (matched filter). Sein Ausgang ohne Rauschen ist $g(t)=a\,\varphi^E_{ss}(t-T)$, die verschobene AKF des Signals, und wird genau in ihrem Maximum abgetastet. Erstaunlich ist: Das Ergebnis hängt nur von der *Energie* des Signals ab, nicht von seiner Form. Ein kurzer, hoher Impuls ist so gut wie ein langer, flacher mit derselben Energie. Damit das Filter kausal ist, muss $T$ mindestens die Dauer des Signals sein. Gleichwertig ist ein __Korrelator__: Er multipliziert das Empfangssignal mit $s(t)$ und integriert über die Dauer des Signals.

:::aufgabe Aufgabe 10 ★★ Ein Rechteckimpuls im Rauschen
<span class="anker" id="aufg-10"></span>

Ein Rechteckimpuls der Höhe 1 V und Dauer 1 ms wird mit weißem Rauschen der Leistungsdichte $N_0=10^{-6}$ V$^2$/Hz empfangen.

<ol class="al">

<li>

Wie sieht das Korrelationsfilter aus, und welches $S_a/N$ (in dB) erreicht es?

</li>

<li>

Wie sieht der Ausgang ohne Rauschen aus, und wann muss abgetastet werden?

</li>

<li>

Der Impuls wird auf 0,25 ms verkürzt, bei gleicher Höhe. Was ändert sich?

</li>

</ol>

:::loesung
(a) $h(t)=a\,s(T-t)$: wieder ein Rechteck von 1 ms, mit $T\ge1$ ms kausal. $E_s=1\,\mathrm{V^2}\cdot1\,\mathrm{ms}=10^{-3}$ V$^2$s, also $S_a/N=10^{-3}/10^{-6}=1000$, das sind 30 dB.

(b) Die AKF des Rechtecks, ein Dreieck der Breite 2 ms, verschoben um $T$: Es steigt ab $t=T-1\,\mathrm{ms}$ an und erreicht bei $t=T$ sein Maximum. Bei $T=1$ ms tastet man genau am Ende des Impulses ab, dann hat das Filter ihn ganz „gesehen“.

(c) $E_s$ sinkt auf ein Viertel, $S_a/N=250$, also 24 dB, 6 dB schlechter. Es zählt nur die Energie. Bei gleicher Höhe bedeutet ein kürzerer Impuls weniger Energie.
:::
:::

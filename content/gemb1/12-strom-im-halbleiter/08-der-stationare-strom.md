---
title: Stufe 6: Der stationäre Strom
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Strom im Halbleiter
order: 4220800
summary: Alle Teile liegen bereit.
tags: Moment, Fermi-Kanten
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Alle Teile liegen bereit. Diese Stufe löst [(5.4)](der-streuterm-und-die-relaxationszeit.html#gl-5-4) für eine homogene Probe im konstanten Feld, gewinnt das Gasmodell aus [Teil 1](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/welle-teilchen-und-schrodinger-gleichung/welle-teilchen-und-schroedinger-gleichung.html) zurück und zeigt, was die Gleichung darüber hinaus leistet.
:::

**Die Idee.** Das Feld schiebt die Verteilung mit der Rate $F/\hbar$ durch $k$, die Stöße ziehen sie mit der Rate $1/\tau_\text{scat}$ zurück. Dazwischen stellt sich eine feste, winzige Verschiebung ein (Abb. [6](#abb-6)), und aus ihr folgt der Strom nach [(1.4)](strom-aus-besetzten-zustanden.html#gl-1-4).

:::satz Satz 6.1 (Stationärer homogener Fall)
<span class="anker" id="satz-6-1"></span>

Mit $\partial f/\partial t=0$, $\partial f/\partial x=0$ und $F=-e\mathcal E$ wird [(5.4)](der-streuterm-und-die-relaxationszeit.html#gl-5-4) zu

<span class="anker" id="gl-6-1"></span>
$$-\frac{e\mathcal E}\hbar\,\frac{\partial f}{\partial k}=-\frac{f-f^0}{\tau_\text{scat}}. \tag{6.1}$$

Für kleine Felder ist die Lösung die verschobene Gleichgewichtsverteilung, und im Parabelband folgt das ohmsche Gesetz:

<span class="anker" id="gl-6-2"></span>
$$f(k)\approx f^0(k)+\frac{e\mathcal E\tau_\text{scat}}\hbar\frac{\partial f^0}{\partial k}\approx f^0(k-\delta k),\qquad\delta k=-\frac{e\mathcal E\tau_\text{scat}}\hbar, \tag{6.2}$$

<span class="anker" id="gl-6-3"></span>
$$j=\underbrace{e\,n\,\mu}_{\sigma}\,\mathcal E,\qquad\mu=\frac{e\,\tau_\text{scat}}{m^*}. \tag{6.3}$$
:::

⁠**So liest man das:** Die Driftgeschwindigkeit ist $v_\mathrm d=\hbar\,\delta k/m^*=-\mu\mathcal E$, $\mu$ hat die Einheit (cm/s)/(V/cm) $=\mathrm{cm^2/(V\,s)}$. $\tau_\text{scat}$ sagt, wie lange ein Träger im Mittel ungestört beschleunigt wird. **Gültigkeit:** Parabelband, $|v_\mathrm d|\ll v_\text{th}$. In Silizium ist $|v_\mathrm d|$ bei $10^5$ V/m schon 6 % von $v_\text{th}$, darüber ändert sich $\tau_\text{scat}$ mit dem Feld.

:::herleitung Das erste Moment
Eine Gleichung mit einer Potenz von $k$ multiplizieren und über $k$ integrieren heißt __Moment__ bilden. Hier wendet man $\frac1\pi\int\mathrm{d} k\;k$ auf [(6.1)](#gl-6-1) an und benutzt [(3.1)](vom-wellenpaket-zur-verteilungsfunktion.html#gl-3-1).

<ol>

<li>

Links gibt partielle Integration $-\frac{e\mathcal E}\hbar\frac1\pi\int\mathrm{d} k\;k\,\frac{\partial f}{\partial k}=+\frac{e\mathcal E}\hbar\frac1\pi\int\mathrm{d} k\;f=\frac{e\mathcal E}\hbar\,n$, denn $f$ verschwindet für große $|k|$.

</li>

<li>

Rechts ist $\int\mathrm{d} k\;k\,f^0=0$, weil $f^0$ gerade ist. Mit $k=m^*v/\hbar$ bleibt $-\frac1{\tau_\text{scat}}\frac1\pi\int\mathrm{d} k\;\frac{m^*}\hbar\,v\,f=+\frac{m^*}{\hbar\,\tau_\text{scat}}\,\frac je$.

</li>

<li>

Gleichsetzen ergibt $j=e^2\,n\,\tau_\text{scat}\,\mathcal E/m^*$.

</li>

</ol>

Für [(6.2)](#gl-6-2) setzt man rechts in $f=f^0+(e\mathcal E\tau_\text{scat}/\hbar)\,\partial f/\partial k$ näherungsweise $f^0$ ein.
:::

:::abbildung gemb1/k12verschoben 6
Oben: Gleichgewicht (gestrichelt) und stationäre Verteilung $f$, Verschiebung stark übertrieben. Unten: Abweichung $f-f^0$. Im Halbleiter ändert sich die ganze Verteilung, im Metall nur die __Fermi-Kanten__ $\pm k_\mathrm F$, wo $f$ von 1 auf 0 fällt.
:::

**Beispiel.** Die Probe hat $\mu_\mathrm n=1200\,\mathrm{cm^2/(V\,s)}$. Bei $\mathcal E=1000$ V/m folgen $|\delta k|=2{,}7\cdot10^{-4}\,\mathrm{nm^{-1}}$, das sind $5\cdot10^{-4}$ von $k_\text{th}$, sowie $|v_\mathrm d|=120$ m/s, 1900-mal weniger als $v_\text{th}$, und $j=1{,}9\cdot10^{5}\,\mathrm{A/m^2}$ mit $\sigma=192$ S/m. **Grenzfall:** Für $\tau_\text{scat}\to\infty$ wächst $\delta k$ ohne Grenze, und es bleibt die Bloch-Schwingung.

**Was die Gleichung mehr leistet.** Die Form $j=e\,n\,\mu\,\mathcal E$ gab schon das Gasmodell. Der Unterschied liegt in dem, was darin steckt:

| Frage | Gasmodell | Transportgleichung |
|---|---|---|
| Woran stößt der Träger? | an den Rümpfen, $l_\mathrm{mfp}\approx1$ nm | an Störungen der Periode, $S(k\to k')$, in Silizium $l_\mathrm{mfp}=47$ nm |
| Welche Masse? | $m_0$ | Krümmung des Bands, $m^*$ |
| Wer trägt den Strom? | alle gleich, mit $v_\mathrm e$ | wo $\partial f^0/\partial k\neq0$ ist, im Metall nur die Fermi-Kante mit $v_\mathrm F$ |
| Ort und Zeit? | nur homogen, stationär | $f(x,k,t)$, auch bei Gefällen in $E_\mathrm F$ und $T$ |

Das löst die Rätsel aus [Teil 1](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/welle-teilchen-und-schrodinger-gleichung/welle-teilchen-und-schroedinger-gleichung.html). Das Gasmodell gibt $\mu=15\,\mathrm{cm^2/(V\,s)}$, Silizium hat 1400. Vom Faktor 93 stammen 24 aus der längeren Streuzeit und 3,8 aus der kleineren Masse. In $m_\mathrm n^*=3/(1/m_\mathrm h^*+2/m_\mathrm l^*)=0{,}26\,m_0$ zählt der Mittelwert von $1/m$ über die Richtungen der Täler ([Teil 9](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/bandstrukturen-lesen/bandstrukturen-lesen.html)), nicht $m_\mathrm C^*=1{,}08\,m_0$ aus $N_\mathrm C$, das Plätze zählt. Im Metall ändert sich nur die Fermi-Kante, trotzdem steht in [(6.3)](#gl-6-3) das ganze $n$: Die partielle Integration macht aus der schmalen Änderung die Fläche unter $f$. Wenige schnelle Elektronen wirken wie viele langsame.

:::frage Eine Verschiebung von einem Zweitausendstel der Breite: Wie kann daraus ein merklicher Strom werden?
Ohne Feld heben sich $10^{16}$ Beiträge je cm$^3$ exakt auf. Die kleine Schieflage bricht das für alle Elektronen zugleich. Der Strom ist die winzige Differenz zweier riesiger Teilströme.
:::

:::aufgabe Aufgabe 6 ★★ GaAs nachrechnen
<span class="anker" id="aufg-6"></span>

GaAs hat bei 300 K $\mu_\mathrm n=8500\,\mathrm{cm^2/(V\,s)}$ und $m^*=0{,}067\,m_0$.

<ol class="al">

<li>

Berechne $\tau_\text{scat}$, $v_\text{th}$ und $l_\mathrm{mfp}=v_\text{th}\tau_\text{scat}$. Zeige, dass $e\tau/m$ die Einheit m$^2$/(V s) hat.

</li>

<li>

Berechne bei $\mathcal E=500$ V/m die Größen $|v_\mathrm d|$, $|\delta k|$ und $|\delta k|/k_\text{th}$.

</li>

</ol>

:::loesung
(a) $\tau_\text{scat}=\mu\,m^*/e=0{,}32$ ps, $v_\text{th}=4{,}5\cdot10^5$ m/s, $l_\mathrm{mfp}=146$ nm. Einheit: C s/kg $=$ m$^2$/(V s), weil 1 kg $=1\,\mathrm{J\,s^2/m^2}$ und J/C $=$ V. (b) $|v_\mathrm d|=425$ m/s, $|\delta k|=2{,}5\cdot10^{-4}\,\mathrm{nm^{-1}}$, mit $k_\text{th}=0{,}26\,\mathrm{nm^{-1}}$ das Verhältnis $9{,}4\cdot10^{-4}$, gleich $|v_\mathrm d|/v_\text{th}$.
:::
:::

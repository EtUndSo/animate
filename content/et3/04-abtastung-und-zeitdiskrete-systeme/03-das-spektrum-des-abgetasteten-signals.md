---
title: Stufe 2: Das Spektrum des abgetasteten Signals
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Abtastung und zeitdiskrete Systeme
adresse: elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme
knoten: Kapitel 4: Abtastung und zeitdiskrete Systeme
order: 3240300
summary: Was macht das Abtasten mit dem Spektrum?
tags: Spiegelspektren
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Was macht das Abtasten mit dem Spektrum? Diese Stufe zeigt: Es wiederholt sich periodisch.
:::

**Die Idee.** Zwei Schwingungen, deren Frequenzen sich um ein Vielfaches der Abtastrate $1/T$ unterscheiden, haben dieselben Abtastwerte:

$$\mathrm{e}^{\mathrm{j}2\pi(f_0+k/T)nT}=\mathrm{e}^{\mathrm{j}2\pi f_0nT}\cdot\underbrace{\mathrm{e}^{\mathrm{j}2\pi kn}}_{=1}.$$

Die Abtastwerte können sie nicht unterscheiden. Deshalb muss das Spektrum der Abtastwerte bei $f_0$ und bei $f_0+k/T$ gleich aussehen. Es ist periodisch.

:::satz Satz 2.1 (Spektrum des ideal abgetasteten Signals)
<span class="anker" id="satz-2-1"></span>

<span class="anker" id="gl-2-1"></span>
$$S_\mathrm a(f)=\frac1T\sum_{k=-\infty}^{\infty}S\Bigl(f-\frac kT\Bigr)\qquad(T>0). \tag{2.1}$$
:::

⁠**So liest man das:** Das Spektrum des Originals erscheint unverändert in der Form, aber mit dem Faktor $1/T$ und an jedem Vielfachen der Abtastrate wiederholt. Die Kopien heißen __Spiegelspektren__.

:::herleitung Spektrum des abgetasteten Signals
Multiplikation wird Faltung ([Kapitel 3](/wissen/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)), und das Spektrum des Dirac-Kamms ist wieder ein Kamm:

$$s(t)\cdot\sum_n\delta(t-nT)\;\circ\!\!-\!\!\bullet\;S(f)*\frac1T\sum_k\delta\Bigl(f-\frac kT\Bigr)=\frac1T\sum_kS\Bigl(f-\frac kT\Bigr).$$

Die Faltung mit einem verschobenen Dirac-Impuls verschiebt das Spektrum.
:::

:::abbildung et3/k4spektrum 1
Ein Spektrum bis $f_\mathrm g=300$ Hz (blau, dreieckig zur Übersicht), abgetastet. Oben mit 1 kHz: Die Kopien bei Vielfachen von 1 kHz liegen getrennt. Unten mit 500 Hz: Kopien im Abstand 500 Hz überlappen, die Summe (rot) ist nicht mehr das Original. Der Faktor $1/T$ ist weggelassen.
:::

:::frage Woher „weiß“ das Spektrum, dass abgetastet wurde? Das Signal zwischen den Abtastpunkten ist doch einfach weg.
Genau deshalb. Zwischen den Abtastpunkten ist das abgetastete Signal null, außer an den Impulsen. Jede Schwingung, die an allen Punkten $nT$ dieselben Werte hat, beschreibt dieses Signal gleich gut. Das Spektrum kann sich zwischen ihnen nicht entscheiden und enthält alle: das Original und seine Kopien bei jedem Vielfachen von $1/T$.
:::

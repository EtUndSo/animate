---
title: Stufe 9: FFT und schnelle Faltung
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / Abtastung und zeitdiskrete Systeme
order: 3241000
summary: Die DFT braucht M 2 Multiplikationen.
tags: schnelle Fourier-Transformation, zyklische
lang: de
---

<span class="anker" id="stufe-9"></span>

:::zweck
Die DFT braucht $M^2$ Multiplikationen. Die FFT kommt mit ungefähr $M\,\mathrm{lb}\,M$ aus. Damit wird auch die Faltung über den Frequenzbereich schnell.
:::

**Die Idee der FFT.** Mit $W_M=\mathrm{e}^{-\mathrm{j}2\pi/M}$ ist $S_d(k)=\sum_ns_d(n)W_M^{kn}$. Für gerades $M$ teilt man in Werte mit geradem und ungeradem Index:

<span class="anker" id="gl-9-1"></span>
$$S_d(k)=\underbrace{\sum_{n=0}^{M/2-1}s_d(2n)\,W_{M/2}^{kn}}_{S_{d,1}(k)}+W_M^k\underbrace{\sum_{n=0}^{M/2-1}s_d(2n+1)\,W_{M/2}^{kn}}_{S_{d,2}(k)}, \tag{9.1}$$

denn $W_M^{2kn}=W_{M/2}^{kn}$. Statt einer DFT der Länge $M$ braucht man zwei der Länge $M/2$ und $M$ Multiplikationen mit $W_M^k$, also $2(M/2)^2+M$ statt $M^2$. Beide Teil-DFTs sind periodisch mit $M/2$, deshalb liefern sie auch die Werte für $k\ge M/2$. Ist $M$ eine Zweierpotenz, wiederholt man die Teilung $\mathrm{lb}\,M$-mal. Der Aufwand sinkt auf etwa $M\,\mathrm{lb}\,M$. Bei $M=1024$ sind das 10 240 statt 1 048 576 Multiplikationen, rund hundertmal weniger. Das ist die __schnelle Fourier-Transformation__ (FFT).

**Zyklische Faltung.** Für periodische Folgen der Periode $M$ gilt die __zyklische__ (periodische) Faltung

<span class="anker" id="gl-9-2"></span>
$$g_d(n)=\sum_{m=0}^{M-1}s_d(m)\,h_d\bigl((n-m)\bmod M\bigr)\;\circ\!\!-\!\!\bullet\;G_d(k)=S_d(k)\,H_d(k). \tag{9.2}$$

Sie ist das periodisch wiederholte Ergebnis der gewöhnlichen Faltung. Ist $M$ zu klein, überlappen die Wiederholungen. Für $s=(1,1,1)$ und $h=(1,2)$ ist die gewöhnliche Faltung $(1,3,3,2)$ mit vier Werten. Mit $M=3$ fällt der letzte Wert auf den ersten: $(3,3,3)$. Mit $M=4$ stimmt es: $(1,3,3,2)$. Allgemein muss $M\ge M_1+M_2-1$ sein ($M_1$, $M_2$: Längen der beiden Folgen), dazu füllt man mit Nullen auf.

**Schnelle Faltung.** Statt die Faltungssumme direkt auszurechnen, transformiert man beide Folgen mit der FFT, multipliziert und transformiert zurück. Ein beliebig langes Signal zerlegt man in Blöcke, faltet jeden Block einzeln und addiert die Ergebnisse. Das ist erlaubt, weil die Faltung distributiv ist:

$$s(n)*h(n)=\Bigl[\sum_is_i(n)\Bigr]*h(n)=\sum_i\bigl[s_i(n)*h(n)\bigr].$$

:::aufgabe Aufgabe 9 ★★ Zyklisch oder linear
<span class="anker" id="aufg-9"></span>

<ol class="al">

<li>

Rechne die zyklische Faltung von $(1,1,1)$ und $(1,2,0)$ mit $M=3$ von Hand. Welcher Wert der linearen Faltung ist wohin gewandert?

</li>

<li>

Ein Signal mit 1000 Werten soll mit einem Filter mit 25 Werten über die DFT gefaltet werden. Wie lang muss die DFT mindestens sein?

</li>

</ol>

:::loesung
(a) $g(0)=s_0h_0+s_1h_2+s_2h_1=1+0+2=3$, $g(1)=s_0h_1+s_1h_0+s_2h_2=2+1+0=3$, $g(2)=s_0h_2+s_1h_1+s_2h_0=0+2+1=3$. Der vierte Wert der linearen Faltung (2 bei $n=3$) ist zyklisch auf $n=0$ gewandert: $1+2=3$.

(b) Mindestens $1000+25-1=1024$. Das ist praktischerweise eine Zweierpotenz.
:::
:::

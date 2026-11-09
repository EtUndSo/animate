---
title: Stufe 8: Singuläre Signale und Linienspektren
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / Fourier-Reihe und -Transformation
order: 3230900
summary: Konstanten, Schwingungen, der Sprung und periodische Signale sind nicht absolut integrierbar.
tags: Linienspektrum, Dirac-Kamm
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Konstanten, Schwingungen, der Sprung und periodische Signale sind nicht absolut integrierbar. Mit Dirac-Impulsen im Spektrum lassen sie sich trotzdem transformieren. So werden Fourier-Reihe und Fourier-Integral eins.
:::

:::satz Satz 8.1 (Singuläre Paare)
<span class="anker" id="satz-8-1"></span>

<span class="anker" id="gl-8-1"></span>
<span class="anker" id="gl-8-2"></span>
<span class="anker" id="gl-8-3"></span>
<span class="anker" id="gl-8-4"></span>
<span class="anker" id="gl-8-5"></span>
<span class="anker" id="gl-8-6"></span>
<span class="anker" id="gl-8-7"></span>
$$\begin{aligned} \delta(t)&\;\circ\!\!-\!\!\bullet\;1, & c&\;\circ\!\!-\!\!\bullet\;c\,\delta(f),\\ \mathrm{e}^{\mathrm{j}2\pi Ft}&\;\circ\!\!-\!\!\bullet\;\delta(f-F), & \cos(2\pi Ft)&\;\circ\!\!-\!\!\bullet\;\tfrac12\delta(f+F)+\tfrac12\delta(f-F),\\ & & \sin(2\pi Ft)&\;\circ\!\!-\!\!\bullet\;\tfrac{\mathrm{j}}{2}\delta(f+F)-\tfrac{\mathrm{j}}{2}\delta(f-F),\\ \textstyle\sum_kS_p(k)\mathrm{e}^{\mathrm{j}2\pi kFt}&\;\circ\!\!-\!\!\bullet\;\textstyle\sum_kS_p(k)\,\delta(f-kF),\\ \textstyle\sum_n\delta(t-nT)&\;\circ\!\!-\!\!\bullet\;\frac{1}{|T|}\textstyle\sum_k\delta\Bigl(f-\frac kT\Bigr),\\ \varepsilon(t)&\;\circ\!\!-\!\!\bullet\;\tfrac12\delta(f)+\frac{1}{\mathrm{j}2\pi f}, & \operatorname{sgn}(t)&\;\circ\!\!-\!\!\bullet\;\frac{1}{\mathrm{j}\pi f},\\ \int_{-\infty}^ts(\tau)\mathrm{d}\tau&\;\circ\!\!-\!\!\bullet\;\frac{S(f)}{\mathrm{j}2\pi f}+\tfrac12S(0)\,\delta(f). \end{aligned} \tag{8.1|8.2|8.3|8.4|8.5|8.6|8.7}$$
:::

⁠**So liest man das:**

<ul>

<li>

Eine Konstante ist eine Schwingung der Frequenz 0, ihr Spektrum ist eine einzige Linie bei $f=0$. Eine Schwingung $\mathrm{e}^{\mathrm{j}2\pi Ft}$ ist eine Linie bei $F$. Ein reeller Kosinus hat zwei halbe Linien bei $\pm F$.

</li>

<li>

Ein periodisches Signal hat ein __Linienspektrum__: Dirac-Impulse bei den Harmonischen, mit den Fourier-Koeffizienten als Gewichten. Die Fourier-Reihe ist also ein Sonderfall des Fourier-Integrals.

</li>

<li>

Der __Dirac-Kamm__ (Impulse im Abstand $T$) hat wieder einen Dirac-Kamm als Spektrum, mit dem Abstand $1/T$ und dem Gewicht $1/|T|$ (Abb. [7](#abb-7)).

</li>

<li>

Der Sprung hat einen Gleichanteil $\frac12$ (Linie $\frac12\delta(f)$) und einen Wechselanteil $\frac12\operatorname{sgn}(t)$, dessen Spektrum wie $1/f$ abfällt.

</li>

</ul>

:::herleitung Singuläre Paare
⁠**Konstante, Schwingung:** Symmetrie auf $\delta(t)\circ\!\!-\!\!\bullet\,1$ anwenden: $1\circ\!\!-\!\!\bullet\,\delta(-f)=\delta(f)$. Modulation verschiebt die Linie: $\mathrm{e}^{\mathrm{j}2\pi Ft}\cdot1\circ\!\!-\!\!\bullet\,\delta(f-F)$. Kosinus und Sinus folgen mit den Euler-Formeln.

⁠**Linienspektrum:** Superposition über alle Harmonischen.

⁠**Dirac-Kamm:** Er ist periodisch mit $T$. Seine Fourier-Koeffizienten sind $S_p(k)=\frac1T\int_{-T/2}^{T/2}\delta(t)\mathrm{e}^{-\mathrm{j}2\pi kFt}\mathrm{d} t=\frac1T$ für alle $k$. Mit dem Linienspektrum folgt [(8.5)](#gl-8-5).

⁠**Signum:** $\operatorname{sgn}(t)$ ist der Grenzfall von $\operatorname{sgn}(t)\mathrm{e}^{-a|t|}$ für $a\to0$:

$$\int_0^\infty\mathrm{e}^{-(a+\mathrm{j}2\pi f)t}\mathrm{d} t-\int_{-\infty}^0\mathrm{e}^{(a-\mathrm{j}2\pi f)t}\mathrm{d} t=\frac{1}{a+\mathrm{j}2\pi f}-\frac{1}{a-\mathrm{j}2\pi f}=\frac{-\mathrm{j}4\pi f}{a^2+(2\pi f)^2}\;\xrightarrow{a\to0}\;\frac{1}{\mathrm{j}\pi f}.$$

⁠**Sprung:** $\varepsilon(t)=\frac12+\frac12\operatorname{sgn}(t)$, also $\frac12\delta(f)+\frac{1}{\mathrm{j}2\pi f}$.

⁠**Integration:** $\int_{-\infty}^ts\,\mathrm{d}\tau=s*\varepsilon$, Faltungssatz und Siebeigenschaft $S(f)\delta(f)=S(0)\delta(f)$.
:::

:::abbildung et3/k3kamm 7
Dirac-Kamm mit $T=0{,}5$ s und sein Spektrum: wieder ein Kamm, mit dem Abstand $1/T=2$ Hz und dem Gewicht $1/T=2$. Je dichter die Impulse in der Zeit, desto weiter auseinander die Linien.
:::

:::frage Aus $\frac{\mathrm{d}}{\mathrm{d} t}\varepsilon=\delta$ folgt doch $\mathrm{j}2\pi f\,S(f)=1$, also $S(f)=\frac{1}{\mathrm{j}2\pi f}$. Woher kommt das $\frac12\delta(f)$?
Die Gleichung $\mathrm{j}2\pi f\,S(f)=1$ legt $S$ nur für $f\neq0$ fest. Bei $f=0$ steht links $0\cdot S(0)$, und ein Summand $c\,\delta(f)$ fällt wegen $f\delta(f)=0$ heraus. Das ist das Gegenstück dazu, dass Ableiten eine Konstante „vergisst“: $\varepsilon(t)$ und $\varepsilon(t)+b$ haben dieselbe Ableitung. Welche Konstante richtig ist, entscheidet der gerade Anteil: $\varepsilon$ hat den Mittelwert $\frac12$, also $c=\frac12$.
:::

::::beispiel der eingeschaltete Kosinus
$\varepsilon(t)\cos(2\pi Ft)$. Multiplikation wird Faltung, und die Faltung mit einem Dirac-Impuls verschiebt:

$$\Bigl[\tfrac12\delta(f)+\tfrac{1}{\mathrm{j}2\pi f}\Bigr]*\tfrac12\bigl[\delta(f+F)+\delta(f-F)\bigr] =\tfrac14\bigl[\delta(f+F)+\delta(f-F)\bigr]-\frac{\mathrm{j}}{4\pi}\Bigl[\frac{1}{f+F}+\frac{1}{f-F}\Bigr].$$

Neben den halbierten Linien bei $\pm F$ entsteht ein breites Spektrum: Der Einschaltvorgang selbst enthält Frequenzen nahe $\pm F$.
::::

:::aufgabe Aufgabe 10 ★ Linienspektren
<span class="anker" id="aufg-10"></span>

<ol class="al">

<li>

Gib das Spektrum von $s(t)=3+2\cos(2\pi\cdot50\,\mathrm{Hz}\cdot t)$ an und skizziere es.

</li>

<li>

Gib das Spektrum der Rechteckschwingung des Rechenmodells für $|f|\le0{,}5$ Hz an.

</li>

</ol>

:::loesung
(a) $3\,\delta(f)+\delta(f-50\,\mathrm{Hz})+\delta(f+50\,\mathrm{Hz})$: eine Linie mit Gewicht 3 bei null, zwei mit Gewicht 1 bei $\pm50$ Hz.

(b) $F=0{,}159$ Hz. Bis 0,5 Hz liegen $k=0,\pm1,\pm2,\pm3$, aber $k=\pm2$ fehlt:

$$0{,}5\,\delta(f)+0{,}318\bigl[\delta(f-0{,}159)+\delta(f+0{,}159)\bigr]-0{,}106\bigl[\delta(f-0{,}477)+\delta(f+0{,}477)\bigr].$$
:::
:::

:::aufgabe Aufgabe 11 ★★ Signum und Integration
<span class="anker" id="aufg-11"></span>

<ol class="al">

<li>

Prüfe mit [(5.2)](symmetrien-im-signal-und-im-spektrum.html#gl-5-2): Das Spektrum von $\operatorname{sgn}(t)$ muss rein imaginär und ungerade sein.

</li>

<li>

Berechne mit [(8.7)](#gl-8-7) das Spektrum von $\int_{-\infty}^t\operatorname{rect}(\tau)\mathrm{d}\tau$. Welches Signal ist das?

</li>

</ol>

:::loesung
(a) $\frac{1}{\mathrm{j}\pi f}=-\frac{\mathrm{j}}{\pi f}$: rein imaginär, und $-\frac{\mathrm{j}}{\pi(-f)}=+\frac{\mathrm{j}}{\pi f}$, also ungerade. Passt zu einem reellen, ungeraden Signal.

(b) $\frac{\operatorname{si}(\pi f)}{\mathrm{j}2\pi f}+\frac12\delta(f)$. Das Signal ist das laufende Integral des Rechtecks: 0 für $t\le-\frac12$, dann eine Rampe bis 1 bei $t=\frac12$, danach konstant 1. Der Mittelwert über alle Zeiten ist $\frac12$, daher $\frac12\delta(f)$.
:::
:::

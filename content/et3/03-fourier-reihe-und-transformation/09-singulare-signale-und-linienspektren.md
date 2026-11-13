---
title: Stufe 8: Singuläre Signale und Linienspektren
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Fourier-Reihe und -Transformation
adresse: elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation
knoten: Kapitel 3: Fourier-Reihe und -Transformation
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

::::kurzfassung
Konstanten, Schwingungen, der Sprung und periodische Signale sind nicht absolut integrierbar. Mit Dirac-Impulsen im Spektrum lassen sie sich trotzdem transformieren, und die Fourier-Reihe wird ein Sonderfall des Fourier-Integrals.

Eine Konstante ist eine Schwingung der Frequenz 0, ihr Spektrum eine einzige Linie: $c\;\circ\!\!-\!\!\bullet\;c\,\delta(f)$. Eine Schwingung ist eine Linie bei ihrer Frequenz, $\mathrm{e}^{\mathrm{j}2\pi Ft}\;\circ\!\!-\!\!\bullet\;\delta(f-F)$; ein reeller Kosinus besteht aus zwei halben Linien bei $\pm F$. Ein periodisches Signal hat deshalb ein __Linienspektrum__: Dirac-Impulse bei den Harmonischen, mit den Fourier-Koeffizienten als Gewichten.

$$\sum_kS_p(k)\mathrm{e}^{\mathrm{j}2\pi kFt}\;\circ\!\!-\!\!\bullet\;\sum_kS_p(k)\,\delta(f-kF).$$

Der __Dirac-Kamm__ $\sum_n\delta(t-nT)$ hat als Spektrum wieder einen Kamm, mit dem Abstand $1/T$ und dem Gewicht $1/|T|$. Der Sprung hat das Spektrum $\tfrac12\delta(f)+\frac{1}{\mathrm{j}2\pi f}$, das Signum das Spektrum $\frac{1}{\mathrm{j}\pi f}$.

Der Grund: Die Symmetrie macht aus $\delta(t)\;\circ\!\!-\!\!\bullet\;1$ das Paar $1\;\circ\!\!-\!\!\bullet\;\delta(f)$, und die Modulation verschiebt diese Linie nach $F$. Beim Sprung kommt die Linie $\tfrac12\delta(f)$ vom Gleichanteil $\tfrac12$. Der Wechselanteil $\tfrac12\operatorname{sgn}(t)$ liefert den Teil, der wie $1/f$ abfällt.

Falle: Aus $\frac{\mathrm{d}}{\mathrm{d} t}\varepsilon=\delta$ folgt nur $\mathrm{j}2\pi f\,S(f)=1$. Das legt $S$ bei $f=0$ nicht fest, denn wegen $f\delta(f)=0$ fällt jeder Summand $c\,\delta(f)$ heraus. Ableiten vergisst Konstanten; die Linie $\tfrac12\delta(f)$ ergänzt man aus dem Mittelwert $\tfrac12$ des Sprungs.
::::

::::formelsammlung
**Dirac-Impuls und Konstante**

$$\delta(t)\;\circ\!\!-\!\!\bullet\;1,\qquad c\;\circ\!\!-\!\!\bullet\;c\,\delta(f)$$

Die Konstante $c$ ist eine Schwingung der Frequenz 0: eine einzige Linie bei $f=0$. Folgt mit der Symmetrie aus $\delta(t)\;\circ\!\!-\!\!\bullet\;1$.

**Komplexe Schwingung**

$$\mathrm{e}^{\mathrm{j}2\pi Ft}\;\circ\!\!-\!\!\bullet\;\delta(f-F)$$

Eine Linie bei $F$; die Modulation verschiebt die Linie von $f=0$ nach $F$.

**Kosinus**

$$\cos(2\pi Ft)\;\circ\!\!-\!\!\bullet\;\tfrac12\delta(f+F)+\tfrac12\delta(f-F)$$

Zwei halbe Linien bei $\pm F$; mit der Eulerschen Formel.

**Sinus**

$$\sin(2\pi Ft)\;\circ\!\!-\!\!\bullet\;\tfrac{\mathrm{j}}{2}\delta(f+F)-\tfrac{\mathrm{j}}{2}\delta(f-F)$$

Mit der Eulerschen Formel.

**Linienspektrum eines periodischen Signals**

$$\sum_kS_p(k)\mathrm{e}^{\mathrm{j}2\pi kFt}\;\circ\!\!-\!\!\bullet\;\sum_kS_p(k)\,\delta(f-kF)$$

Dirac-Impulse bei den Harmonischen, die Fourier-Koeffizienten sind ihre Gewichte. Die Fourier-Reihe ist ein Sonderfall des Fourier-Integrals.

**Dirac-Kamm**

$$\sum_n\delta(t-nT)\;\circ\!\!-\!\!\bullet\;\frac{1}{|T|}\sum_k\delta\Bigl(f-\frac kT\Bigr)$$

Impulse im Abstand $T$; das Spektrum ist wieder ein Kamm, mit dem Abstand $1/T$ und dem Gewicht $1/|T|$.

**Sprung und Signum**

$$\varepsilon(t)\;\circ\!\!-\!\!\bullet\;\tfrac12\delta(f)+\frac{1}{\mathrm{j}2\pi f},\qquad\operatorname{sgn}(t)\;\circ\!\!-\!\!\bullet\;\frac{1}{\mathrm{j}\pi f}$$

Signum als Grenzfall von $\operatorname{sgn}(t)\mathrm{e}^{-a|t|}$ für $a\to0$. Mit $\varepsilon(t)=\frac12+\frac12\operatorname{sgn}(t)$ gibt der Gleichanteil $\tfrac12$ die Linie $\tfrac12\delta(f)$.

**Integration**

$$\int_{-\infty}^ts(\tau)\mathrm{d}\tau\;\circ\!\!-\!\!\bullet\;\frac{S(f)}{\mathrm{j}2\pi f}+\tfrac12S(0)\,\delta(f)$$

Weil $\int_{-\infty}^ts\,\mathrm{d}\tau=s*\varepsilon$; Faltungssatz.

**Rechnen mit Dirac-Impulsen im Spektrum**

$$f\delta(f)=0,\qquad S(f)\delta(f)=S(0)\delta(f)$$

Deshalb legt $\mathrm{j}2\pi f\,S(f)=1$, aus $\frac{\mathrm{d}}{\mathrm{d} t}\varepsilon=\delta$, das Spektrum bei $f=0$ nicht fest. Die Linie $\tfrac12\delta(f)$ des Sprungs folgt aus seinem Mittelwert $\tfrac12$.

**Eingeschalteter Kosinus**

$$\varepsilon(t)\cos(2\pi Ft)\;\circ\!\!-\!\!\bullet\;\tfrac14\bigl[\delta(f+F)+\delta(f-F)\bigr]-\frac{\mathrm{j}}{4\pi}\Bigl[\frac{1}{f+F}+\frac{1}{f-F}\Bigr]$$

Multiplikation wird Faltung. Neben den halbierten Linien bei $\pm F$ entsteht ein breites Spektrum des Einschaltvorgangs.
::::

::::lernkarten
:::karte formel Dirac-Impuls und Konstante
Welche Spektren haben der Dirac-Impuls $\delta(t)$ und eine Konstante $c$, und wie hängen die beiden Paare zusammen?
---
$\delta(t)\;\circ\!\!-\!\!\bullet\;1$ und $c\;\circ\!\!-\!\!\bullet\;c\,\delta(f)$. Die Konstante ist eine Schwingung der Frequenz 0, ihr Spektrum eine einzige Linie bei $f=0$. Das zweite Paar folgt aus dem ersten mit der Symmetrie.
--- falsch
$\delta(t)\;\circ\!\!-\!\!\bullet\;1$ und $c\;\circ\!\!-\!\!\bullet\;c$. Eine Konstante hat ein konstantes Spektrum, weil sie zu allen Zeiten gleich ist und deshalb alle Frequenzen gleich stark enthält.
--- falsch
$\delta(t)\;\circ\!\!-\!\!\bullet\;\delta(f)$ und $c\;\circ\!\!-\!\!\bullet\;c\,\delta(f)$. Beide haben eine Linie bei $f=0$, weil beide keinen Wechselanteil enthalten; der Dirac-Impuls ist nur eine sehr hohe Konstante.
--- falsch
$\delta(t)\;\circ\!\!-\!\!\bullet\;1$, eine Konstante hat dagegen kein Spektrum. Sie ist nicht absolut integrierbar, und ohne diese Bedingung gibt es die Fourier-Transformierte überhaupt nicht.
:::
:::karte formel Komplexe Schwingung und Kosinus
Welche Spektren haben die komplexe Schwingung $\mathrm{e}^{\mathrm{j}2\pi Ft}$ und der reelle Kosinus $\cos(2\pi Ft)$?
---
$\mathrm{e}^{\mathrm{j}2\pi Ft}\;\circ\!\!-\!\!\bullet\;\delta(f-F)$: eine Linie bei $F$. $\cos(2\pi Ft)\;\circ\!\!-\!\!\bullet\;\tfrac12\delta(f+F)+\tfrac12\delta(f-F)$: zwei halbe Linien bei $\pm F$, nach der Euler-Formel.
--- falsch
$\mathrm{e}^{\mathrm{j}2\pi Ft}\;\circ\!\!-\!\!\bullet\;\delta(f-F)$: eine Linie bei $F$. $\cos(2\pi Ft)\;\circ\!\!-\!\!\bullet\;\delta(f-F)$: ebenfalls nur eine Linie bei $F$, denn negative Frequenzen kommen bei reellen Signalen nicht vor.
--- falsch
$\mathrm{e}^{\mathrm{j}2\pi Ft}\;\circ\!\!-\!\!\bullet\;\delta(f+F)$: eine Linie bei $-F$. $\cos(2\pi Ft)\;\circ\!\!-\!\!\bullet\;\delta(f+F)+\delta(f-F)$: zwei ganze Linien bei $\pm F$, eine für jeden Exponentialanteil.
--- falsch
$\mathrm{e}^{\mathrm{j}2\pi Ft}\;\circ\!\!-\!\!\bullet\;\delta(f-F)$: eine Linie bei $F$. $\cos(2\pi Ft)\;\circ\!\!-\!\!\bullet\;\tfrac12\delta(f+F)-\tfrac12\delta(f-F)$: zwei halbe Linien mit entgegengesetztem Vorzeichen.
:::
:::karte formel Sinus
Welches Spektrum hat der reelle Sinus $\sin(2\pi Ft)$, und wie unterscheidet es sich von dem des Kosinus?
---
$\sin(2\pi Ft)\;\circ\!\!-\!\!\bullet\;\tfrac{\mathrm{j}}{2}\delta(f+F)-\tfrac{\mathrm{j}}{2}\delta(f-F)$: zwei halbe, rein imaginäre Linien bei $\pm F$ mit entgegengesetztem Vorzeichen. Der Kosinus hat dort zwei reelle Linien $\tfrac12$.
--- falsch
$\sin(2\pi Ft)\;\circ\!\!-\!\!\bullet\;\tfrac{\mathrm{j}}{2}\delta(f-F)-\tfrac{\mathrm{j}}{2}\delta(f+F)$: zwei halbe, rein imaginäre Linien bei $\pm F$, die bei $+F$ mit dem Gewicht $+\tfrac{\mathrm{j}}{2}$. Der Kosinus hat dort zwei reelle Linien $\tfrac12$.
--- falsch
$\sin(2\pi Ft)\;\circ\!\!-\!\!\bullet\;\tfrac12\delta(f+F)+\tfrac12\delta(f-F)$, dasselbe wie beim Kosinus. Sinus und Kosinus unterscheiden sich nur durch eine Verschiebung, und die ändert den Betrag des Spektrums nicht.
--- falsch
$\sin(2\pi Ft)\;\circ\!\!-\!\!\bullet\;\tfrac12\delta(f+F)-\tfrac12\delta(f-F)$: zwei halbe, reelle Linien mit entgegengesetztem Vorzeichen. Der Kosinus hat dort zwei reelle Linien mit gleichem Vorzeichen.
:::
:::karte herleitung Konstante und Schwingungen aus dem Dirac-Impuls
Wie folgen die Spektren der Konstanten, der Schwingung $\mathrm{e}^{\mathrm{j}2\pi Ft}$ und des Kosinus aus dem Paar $\delta(t)\;\circ\!\!-\!\!\bullet\;1$?
---
Man wendet die Symmetrie auf $\delta(t)\circ\!\!-\!\!\bullet\,1$ an und erhält $1\circ\!\!-\!\!\bullet\,\delta(-f)=\delta(f)$, weil die Symmetrie Zeit und Frequenz vertauscht und der Dirac-Impuls beim Spiegeln gleich bleibt. Mit der Superposition folgt $c\;\circ\!\!-\!\!\bullet\;c\,\delta(f)$.
---
Die Modulation verschiebt diese Linie, weil die Multiplikation mit $\mathrm{e}^{\mathrm{j}2\pi Ft}$ das ganze Spektrum um $F$ verschiebt: $\mathrm{e}^{\mathrm{j}2\pi Ft}\cdot1\circ\!\!-\!\!\bullet\,\delta(f-F)$.
---
Kosinus und Sinus folgen mit den Euler-Formeln und der Superposition, weil beide aus zwei Schwingungen bei $\pm F$ bestehen; beim Kosinus ergibt sich $\cos(2\pi Ft)\;\circ\!\!-\!\!\bullet\;\tfrac12\delta(f+F)+\tfrac12\delta(f-F)$.
:::
:::karte zusammenhang Transformierbar mit Dirac-Impulsen
Wie lassen sich Konstanten, Schwingungen und der Sprung Fourier-transformieren, obwohl sie nicht absolut integrierbar sind?
---
Man lässt im Spektrum Dirac-Impulse zu. Die Paare gewinnt man aus $\delta(t)\;\circ\!\!-\!\!\bullet\;1$ mit den Theoremen, ohne das Integral über das Signal direkt auszurechnen: Die Konstante wird zur Linie $c\,\delta(f)$, eine Schwingung zur Linie bei ihrer Frequenz.
--- falsch
Man schneidet sie nach endlicher Zeit ab und transformiert nur dieses Stück. Das Ergebnis hängt zwar von der Länge des Stücks ab, aber für ein genügend langes Stück ist der Unterschied zum wahren Spektrum vernachlässigbar klein.
--- falsch
Gar nicht: Signale, die nicht absolut integrierbar sind, haben kein Spektrum. Für sie ist ausschließlich die Laplace-Transformation zuständig, die mit dem Faktor $\mathrm{e}^{-\sigma t}$ jedes beliebige Signal integrierbar macht.
--- falsch
Man ersetzt sie durch ihren Mittelwert über alle Zeiten. Eine Konstante hat dann das Spektrum $c$, eine Schwingung das Spektrum null, weil ihr Mittelwert verschwindet, und der Sprung hat das Spektrum $\tfrac12$.
:::
:::karte begriff Linienspektrum
Was versteht man unter dem Linienspektrum eines periodischen Signals, und was folgt daraus für Fourier-Reihe und Fourier-Integral?
---
Das Spektrum aus Dirac-Impulsen bei den Harmonischen, mit den Fourier-Koeffizienten als Gewichten: $\sum_kS_p(k)\mathrm{e}^{\mathrm{j}2\pi kFt}\;\circ\!\!-\!\!\bullet\;\sum_kS_p(k)\,\delta(f-kF)$. Die Fourier-Reihe ist damit ein Sonderfall des Fourier-Integrals.
--- falsch
Das Spektrum aus Dirac-Impulsen bei den Harmonischen, alle mit dem Gewicht 1: $\sum_kS_p(k)\mathrm{e}^{\mathrm{j}2\pi kFt}\;\circ\!\!-\!\!\bullet\;\sum_k\delta(f-kF)$. Die Koeffizienten bestimmen nur, welche der Linien fehlen.
--- falsch
Das Spektrum aus endlich hohen Strichen bei den Harmonischen, mit den Fourier-Koeffizienten als Höhen. Es ist keine Fourier-Transformierte, denn Fourier-Reihe und Fourier-Integral bleiben getrennte Verfahren.
--- falsch
Die Hüllkurve, auf der die Fourier-Koeffizienten liegen: eine stetige Funktion der Frequenz, deren Werte an den Stellen $kF$ die Koeffizienten sind. Zwischen den Harmonischen ist sie im Allgemeinen nicht null.
:::
:::karte begriff Dirac-Kamm
Was ist ein Dirac-Kamm, und welches Spektrum hat er?
---
Eine Folge von Dirac-Impulsen im Abstand $T$. Sein Spektrum ist wieder ein Dirac-Kamm, mit dem Abstand $1/T$ und dem Gewicht $1/|T|$: $\sum_n\delta(t-nT)\;\circ\!\!-\!\!\bullet\;\frac{1}{|T|}\sum_k\delta\Bigl(f-\frac kT\Bigr)$.
--- falsch
Eine Folge von Dirac-Impulsen im Abstand $T$. Sein Spektrum ist ein Dirac-Kamm mit demselben Abstand $T$ und dem Gewicht 1, weil der Kamm periodisch ist und sich beim Transformieren deshalb nicht verändert.
--- falsch
Eine Folge von Dirac-Impulsen im Abstand $T$. Sein Spektrum ist die Konstante $1/T$, weil jeder einzelne Dirac-Impuls alle Frequenzen mit gleichem Gewicht enthält und sich diese Gewichte einfach addieren.
--- falsch
Eine Folge von Rechteckimpulsen der Breite $T$, die lückenlos aneinanderliegen. Sein Spektrum ist ein Dirac-Kamm mit dem Abstand $T$, weil die Kanten der Rechtecke im Abstand $T$ aufeinander folgen.
:::
:::karte herleitung Spektrum des Dirac-Kamms
Wie folgt das Spektrum des Dirac-Kamms $\sum_n\delta(t-nT)$ aus der Fourier-Reihe und dem Linienspektrum?
---
Der Kamm ist periodisch mit $T$, weil in jedem Abschnitt der Länge $T$ genau ein Impuls liegt. Er hat deshalb eine Fourier-Reihe mit der Grundfrequenz $F=1/T$.
---
Seine Koeffizienten sind $S_p(k)=\frac1T\int_{-T/2}^{T/2}\delta(t)\mathrm{e}^{-\mathrm{j}2\pi kFt}\mathrm{d} t=\frac1T$ für alle $k$, weil in dieser Periode nur der Impuls bei $t=0$ liegt und die Exponentialfunktion dort den Wert 1 hat.
---
Das Linienspektrum setzt bei jeder Harmonischen eine Linie mit diesem Gewicht, weil ein periodisches Signal Dirac-Impulse bei den Vielfachen von $F$ mit den Koeffizienten als Gewichten hat. So ergibt sich wieder ein Kamm.
:::
:::karte formel Sprung und Signum
Welche Spektren haben das Signum $\operatorname{sgn}(t)$ und der Sprung $\varepsilon(t)$, und wie hängen sie zusammen?
---
$\operatorname{sgn}(t)\;\circ\!\!-\!\!\bullet\;\frac{1}{\mathrm{j}\pi f}$ und $\varepsilon(t)\;\circ\!\!-\!\!\bullet\;\tfrac12\delta(f)+\frac{1}{\mathrm{j}2\pi f}$. Wegen $\varepsilon(t)=\frac12+\frac12\operatorname{sgn}(t)$ besteht der Sprung aus dem Gleichanteil $\frac12$ mit der Linie $\tfrac12\delta(f)$ und dem halben Signum.
--- falsch
$\operatorname{sgn}(t)\;\circ\!\!-\!\!\bullet\;\frac{1}{\mathrm{j}\pi f}$ und $\varepsilon(t)\;\circ\!\!-\!\!\bullet\;\frac{1}{\mathrm{j}2\pi f}$. Der Sprung ist das halbe Signum, nach oben verschoben, und eine Verschiebung in der Höhe ändert das Spektrum nicht, weil sie keine Schwingung hinzufügt.
--- falsch
$\operatorname{sgn}(t)\;\circ\!\!-\!\!\bullet\;\frac{1}{\pi f}$ und $\varepsilon(t)\;\circ\!\!-\!\!\bullet\;\tfrac12\delta(f)+\frac{1}{2\pi f}$. Beide Spektren sind reell, weil Signum und Sprung reelle Signale sind und reelle Signale stets reelle Spektren haben.
--- falsch
$\operatorname{sgn}(t)\;\circ\!\!-\!\!\bullet\;\delta(f)$ und $\varepsilon(t)\;\circ\!\!-\!\!\bullet\;\tfrac12\delta(f)$. Beide Signale sind für $t\neq0$ abschnittsweise konstant, und Konstanten haben nur eine einzige Linie bei $f=0$.
:::
:::karte herleitung Spektrum des Signums als Grenzfall
Wie berechnet man das Spektrum von $\operatorname{sgn}(t)$, obwohl das Fourier-Integral des Signums nicht direkt konvergiert, und wie folgt daraus das des Sprungs?
---
Man betrachtet $\operatorname{sgn}(t)\mathrm{e}^{-a|t|}$ mit $a>0$, weil dieses Signal absolut integrierbar ist und für $a\to0$ in das Signum übergeht.
---
Man teilt das Integral bei $t=0$, weil das Signum dort das Vorzeichen wechselt: $\int_0^\infty\mathrm{e}^{-(a+\mathrm{j}2\pi f)t}\mathrm{d} t-\int_{-\infty}^0\mathrm{e}^{(a-\mathrm{j}2\pi f)t}\mathrm{d} t$.
---
Beide Integrale lassen sich ausrechnen, weil die Integranden abklingen: $\frac{1}{a+\mathrm{j}2\pi f}-\frac{1}{a-\mathrm{j}2\pi f}=\frac{-\mathrm{j}4\pi f}{a^2+(2\pi f)^2}$.
---
Für $a\to0$ fällt $a^2$ im Nenner weg, und Kürzen ergibt $\frac{1}{\mathrm{j}\pi f}$, weil $\frac{1}{\mathrm{j}\pi f}=-\frac{\mathrm{j}}{\pi f}$ ist.
---
Für den Sprung nutzt man $\varepsilon(t)=\frac12+\frac12\operatorname{sgn}(t)$, weil die Konstante $\frac12$ die Linie $\tfrac12\delta(f)$ und das halbe Signum $\frac{1}{\mathrm{j}2\pi f}$ liefert.
:::
:::karte zusammenhang Linie beim Sprung
Aus $\frac{\mathrm{d}}{\mathrm{d} t}\varepsilon=\delta$ folgt $\mathrm{j}2\pi f\,S(f)=1$. Warum ist das Spektrum des Sprungs trotzdem nicht einfach $\frac{1}{\mathrm{j}2\pi f}$?
---
Die Gleichung legt $S$ nur für $f\neq0$ fest: Bei $f=0$ steht links $0\cdot S(0)$, und ein Summand $c\,\delta(f)$ fällt wegen $f\delta(f)=0$ heraus. Welcher richtig ist, entscheidet der gerade Anteil: $\varepsilon$ hat den Mittelwert $\frac12$, also kommt $\frac12\delta(f)$ hinzu.
--- falsch
Weil $\frac{1}{\mathrm{j}2\pi f}$ bei $f=0$ unendlich wird und man diese Stelle durch einen Dirac-Impuls ersetzen muss. Sein Gewicht ist 1, weil der Sprung die Höhe 1 hat; zum Spektrum kommt also der volle Dirac-Impuls $\delta(f)$ hinzu.
--- falsch
Weil der Ableitungssatz für den Sprung nicht gilt: $\varepsilon$ ist bei $t=0$ nicht differenzierbar. Das richtige Spektrum erhält man nur durch direktes Integrieren, und das ergibt allein die Linie $\tfrac12\delta(f)$ ohne jeden weiteren Anteil.
--- falsch
Die Gleichung legt $S$ nur für $f\neq0$ fest, und bei $f=0$ darf ein Summand $c\,\delta(f)$ hinzukommen. Welcher, entscheidet der Wert des Sprungs bei $t=0$: Mit dem Wert 1 dort kommt der volle Dirac-Impuls $\delta(f)$ hinzu.
:::
:::karte formel Integration
Welches Spektrum hat das laufende Integral $\int_{-\infty}^ts(\tau)\mathrm{d}\tau$ eines Signals, und warum?
---
$\int_{-\infty}^ts(\tau)\mathrm{d}\tau\;\circ\!\!-\!\!\bullet\;\frac{S(f)}{\mathrm{j}2\pi f}+\tfrac12S(0)\,\delta(f)$. Das laufende Integral ist die Faltung $s*\varepsilon$; nach dem Faltungssatz multipliziert man mit dem Spektrum des Sprungs, und die Siebeigenschaft gibt $S(f)\delta(f)=S(0)\delta(f)$.
--- falsch
$\int_{-\infty}^ts(\tau)\mathrm{d}\tau\;\circ\!\!-\!\!\bullet\;\frac{S(f)}{\mathrm{j}2\pi f}$. Integrieren ist die Umkehrung des Ableitens, und der Ableitungssatz multipliziert mit $\mathrm{j}2\pi f$; also teilt man einfach durch diesen Faktor, ohne weiteren Anteil.
--- falsch
$\int_{-\infty}^ts(\tau)\mathrm{d}\tau\;\circ\!\!-\!\!\bullet\;\mathrm{j}2\pi f\,S(f)+\tfrac12S(0)\,\delta(f)$. Das laufende Integral ist die Faltung $s*\varepsilon$, und das Spektrum des Sprungs wächst mit $f$, weil der Sprung so steil ist.
--- falsch
$\int_{-\infty}^ts(\tau)\mathrm{d}\tau\;\circ\!\!-\!\!\bullet\;\frac{S(f)}{\mathrm{j}2\pi f}+S(0)\,\delta(f)$. Das laufende Integral ist die Faltung $s*\varepsilon$, und die Linie erhält das volle Gewicht $S(0)$, weil die Fläche des Signals ganz erhalten bleibt.
:::
:::karte zusammenhang Eingeschalteter Kosinus
Warum hat der eingeschaltete Kosinus $\varepsilon(t)\cos(2\pi Ft)$ neben Linien bei $\pm F$ auch ein breites Spektrum?
---
Die Multiplikation wird zur Faltung der Spektren, und die Faltung mit den Dirac-Impulsen des Kosinus verschiebt das Spektrum des Sprungs nach $\pm F$. Neben halbierten Linien entsteht ein breiter Anteil: Der Einschaltvorgang selbst enthält Frequenzen nahe $\pm F$.
--- falsch
Weil der Kosinus durch das Einschalten seine Frequenz verliert: Vor $t=0$ ist er null und hat keine Frequenz, deshalb mittelt sich die Frequenz über alle Zeiten zu einem breiten Band um null, das die Linien bei $\pm F$ umgibt.
--- falsch
Die Multiplikation wird zur Addition der Spektren: Zu den Linien des Kosinus kommt das Spektrum des Sprungs hinzu, also $\tfrac12\delta(f)$ und $\frac{1}{\mathrm{j}2\pi f}$. Daraus entsteht ein breiter Anteil um $f=0$, während die Linien bei $\pm F$ in voller Höhe erhalten bleiben.
--- falsch
Die Multiplikation wird zur Faltung der Spektren, und die Faltung mit dem Sprungspektrum verbreitert jede Linie zu einem Rechteck. Die Linien bei $\pm F$ verschwinden dabei ganz, und übrig bleibt nur ein breites Band der Breite $2F$.
:::
::::

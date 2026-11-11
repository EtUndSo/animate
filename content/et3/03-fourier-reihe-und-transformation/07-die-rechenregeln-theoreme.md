---
title: Stufe 6: Die Rechenregeln (Theoreme)
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Fourier-Reihe und -Transformation
adresse: elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation
knoten: Kapitel 3: Fourier-Reihe und -Transformation
order: 3230700
summary: Statt jedes Integral neu auszurechnen, benutzt man Regeln: Was passiert mit dem Spektrum, wenn man das Signal verschiebt, staucht, ableitet, moduliert?
tags: Energiedichte
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Statt jedes Integral neu auszurechnen, benutzt man Regeln: Was passiert mit dem Spektrum, wenn man das Signal verschiebt, staucht, ableitet, moduliert? Jede Regel folgt daraus, was die Operation mit einer einzelnen Schwingung macht.
:::

:::satz Satz 6.1 (Theoreme der Fourier-Transformation)
<span class="anker" id="satz-6-1"></span>

<span class="anker" id="gl-6-1"></span>
<span class="anker" id="gl-6-2"></span>
<span class="anker" id="gl-6-3"></span>
<span class="anker" id="gl-6-4"></span>
<span class="anker" id="gl-6-5"></span>
<span class="anker" id="gl-6-6"></span>
<span class="anker" id="gl-6-7"></span>
<span class="anker" id="gl-6-8"></span>
<span class="anker" id="gl-6-9"></span>
<span class="anker" id="gl-6-10"></span>
<span class="anker" id="gl-6-11"></span>
$$\begin{aligned} &\text{Superposition:} && \textstyle\sum_ia_is_i(t)\;\circ\!\!-\!\!\bullet\;\sum_ia_iS_i(f)\\ &\text{Konjugation:} && s^*(t)\;\circ\!\!-\!\!\bullet\;S^*(-f)\\ &\text{Ähnlichkeit:} && s(bt)\;\circ\!\!-\!\!\bullet\;\frac{1}{|b|}S\Bigl(\frac fb\Bigr),\quad b\neq0;\qquad s(-t)\;\circ\!\!-\!\!\bullet\;S(-f)\\ &\text{Verschiebung:} && s(t-t_0)\;\circ\!\!-\!\!\bullet\;S(f)\,\mathrm{e}^{-\mathrm{j}2\pi ft_0},\qquad\delta(t-t_0)\;\circ\!\!-\!\!\bullet\;\mathrm{e}^{-\mathrm{j}2\pi ft_0}\\ &\text{Ableitung:} && \frac{\mathrm{d}^n}{\mathrm{d} t^n}s(t)\;\circ\!\!-\!\!\bullet\;(\mathrm{j}2\pi f)^nS(f)\\ &\text{Symmetrie (Dualität):} && S(t)\;\circ\!\!-\!\!\bullet\;s(-f)\\ &\text{Modulation:} && \mathrm{e}^{\mathrm{j}2\pi Ft}s(t)\;\circ\!\!-\!\!\bullet\;S(f-F)\\ &\text{Ableitung im Frequenzbereich:} && -\mathrm{j}2\pi t\,s(t)\;\circ\!\!-\!\!\bullet\;\frac{\mathrm{d}}{\mathrm{d} f}S(f)\\ &\text{Faltung, Multiplikation:} && s_1*s_2\;\circ\!\!-\!\!\bullet\;S_1S_2,\qquad s_1s_2\;\circ\!\!-\!\!\bullet\;S_1*S_2\\ &\text{Flächen:} && \int s(t)\mathrm{d} t=S(0),\qquad\int S(f)\mathrm{d} f=s(0)\\ &\text{Parseval:} && \int|s(t)|^2\mathrm{d} t=\int|S(f)|^2\mathrm{d} f \end{aligned} \tag{6.1|6.2|6.3|6.4|6.5|6.6|6.7|6.8|6.9|6.10|6.11}$$
:::

⁠**So liest man die wichtigsten:**

<ul>

<li>

⁠**Ähnlichkeit:** Ein zeitlich gestauchtes Signal ($|b|>1$) hat ein breiteres Spektrum. Kurze Signale brauchen viele Frequenzen. Dauer und Bandbreite verhalten sich umgekehrt.

</li>

<li>

⁠**Verschiebung:** Eine Verzögerung ändert den Betrag nicht, nur die Phase, und zwar linear in $f$: Jede Schwingung wird um dieselbe Zeit verschoben, das ist bei höherer Frequenz ein größerer Winkel.

</li>

<li>

⁠**Ableitung:** $\frac{\mathrm{d}}{\mathrm{d} t}\mathrm{e}^{\mathrm{j}2\pi ft}=\mathrm{j}2\pi f\,\mathrm{e}^{\mathrm{j}2\pi ft}$. Ableiten verstärkt hohe Frequenzen.

</li>

<li>

⁠**Symmetrie:** Hin- und Rücktransformation unterscheiden sich nur im Vorzeichen des Exponenten. Jedes Transformationspaar liefert deshalb ein zweites mit vertauschten Rollen.

</li>

<li>

⁠**Modulation:** Multiplikation mit $\mathrm{e}^{\mathrm{j}2\pi Ft}$ verschiebt das ganze Spektrum um $F$. So arbeitet jeder Rundfunksender.

</li>

<li>

⁠**Multiplikation:** Das Produkt zweier Signale hat als Spektrum die Faltung der Spektren, das Gegenstück zum Faltungssatz.

</li>

<li>

⁠**Parseval:** Die Energie ist in beiden Bereichen dieselbe. $|S(f)|^2$ ist die __Energiedichte__ über der Frequenz.

</li>

</ul>

:::herleitung Ähnlichkeit, Verschiebung, Ableitung, Symmetrie, Modulation, Multiplikation, Parseval
⁠**Ähnlichkeit** ($b>0$, $\tau=bt$): $\int s(bt)\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t=\frac1b\int s(\tau)\mathrm{e}^{-\mathrm{j}2\pi(f/b)\tau}\mathrm{d}\tau=\frac1bS(f/b)$. Für $b<0$ kehren sich die Grenzen um, daher $1/|b|$.

⁠**Verschiebung** ($\tau=t-t_0$): $\int s(\tau)\mathrm{e}^{-\mathrm{j}2\pi f(\tau+t_0)}\mathrm{d}\tau=\mathrm{e}^{-\mathrm{j}2\pi ft_0}S(f)$. Mit $s=\delta$ folgt das Paar für $\delta(t-t_0)$.

⁠**Ableitung:** Die Rücktransformation nach $t$ ableiten, $\frac{\mathrm{d}}{\mathrm{d} t}\int S\mathrm{e}^{\mathrm{j}2\pi ft}\mathrm{d} f=\int\mathrm{j}2\pi f\,S\,\mathrm{e}^{\mathrm{j}2\pi ft}\mathrm{d} f$.

⁠**Symmetrie:** In der Rücktransformation $t$ durch $-t$ ersetzen: $s(-t)=\int S(f)\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} f$. Jetzt die Namen der Variablen $t$ und $f$ tauschen: $s(-f)=\int S(t)\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t$, das ist die Hintransformation von $S(t)$.

⁠**Modulation:** $\int\mathrm{e}^{\mathrm{j}2\pi Ft}s(t)\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t=\int s(t)\mathrm{e}^{-\mathrm{j}2\pi(f-F)t}\mathrm{d} t=S(f-F)$. Die Ableitung im Frequenzbereich folgt ebenso durch Ableiten der Hintransformation nach $f$.

⁠**Multiplikation:** Faltungssatz für die Signale $s_1(t)$ und $s_2(t)$, also $s_1*s_2\;\circ\!\!-\!\!\bullet\;S_1S_2$, dann die Symmetrie auf dieses Paar anwenden: $S_1(t)S_2(t)\;\circ\!\!-\!\!\bullet\;s_1(-f)*s_2(-f)$. Umbenennen ergibt [(6.9)](#gl-6-9).

⁠**Flächen:** $f=0$ in die Hin-, $t=0$ in die Rücktransformation einsetzen.

⁠**Parseval:** $\int|s|^2\mathrm{d} t=\int s\,s^*\mathrm{d} t$ ist das Produkt $s(t)s^*(t)$, integriert, also nach Multiplikation, Konjugation und Flächensatz $\bigl[S(f)*S^*(-f)\bigr]_{f=0}=\int S(\nu)S^*(\nu)\mathrm{d}\nu$.
:::

:::frage Warum ändert eine Verzögerung den Betrag des Spektrums nicht?
Weil eine Verzögerung keine Schwingung schwächt oder verstärkt, sie verschiebt jede nur. Jede Schwingung wird um dieselbe Zeit $t_0$ verschoben, das ist bei der Frequenz $f$ der Winkel $2\pi ft_0$. Deshalb ist die Phase eine Gerade in $f$ mit der Steigung $-2\pi t_0$. Ein System mit $|H|=1$ und linearer Phase verzögert ein Signal, ohne seine Form zu ändern.
:::

:::aufgabe Aufgabe 6 ★★ Theoreme anwenden
<span class="anker" id="aufg-6"></span>

Benutze $\operatorname{rect}(t)\;\circ\!\!-\!\!\bullet\;\operatorname{si}(\pi f)$ (direkt aus der Definition: $\int_{-1/2}^{1/2}\mathrm{e}^{-\mathrm{j}2\pi ft}\,\mathrm{d} t=\operatorname{si}(\pi f)$) und die Theoreme.

<ol class="al">

<li>

Bestimme das Spektrum eines Rechteckimpulses der Höhe 1 von $t=0$ bis $t=2$ s. Wie groß ist sein Betrag bei $f=0$, wo liegt die erste Nullstelle?

</li>

<li>

Bestimme das Spektrum von $\cos(2\pi F_0t)\operatorname{rect}(t)$ mit $F_0=5$ Hz und skizziere es.

</li>

</ol>

:::loesung
(a) Der Impuls ist $\operatorname{rect}\bigl(\frac{t-1}{2}\bigr)$. Ähnlichkeit ($T=2$) und Verschiebung ($t_0=1$ s): $2\operatorname{si}(2\pi f)\,\mathrm{e}^{-\mathrm{j}2\pi f}$. Betrag bei $f=0$: 2 (die Fläche). Erste Nullstelle bei $f=0{,}5$ Hz. Die Verschiebung ändert nur die Phase.

(b) $\cos(2\pi F_0t)=\frac12\mathrm{e}^{\mathrm{j}2\pi F_0t}+\frac12\mathrm{e}^{-\mathrm{j}2\pi F_0t}$, Modulation: $\frac12\operatorname{si}(\pi(f-5))+\frac12\operatorname{si}(\pi(f+5))$. Zwei si-Hauptkeulen der Höhe $\frac12$ bei $\pm5$ Hz mit den ersten Nullstellen 1 Hz daneben.
:::
:::

:::aufgabe Aufgabe 7 ★★ Symmetrie als Werkzeug
<span class="anker" id="aufg-7"></span>

Aus Aufgabe [4](vom-periodischen-zum-einmaligen-signal.html#aufg-4) weißt du $\mathrm{e}^{-|t|}\;\circ\!\!-\!\!\bullet\;\frac{2}{1+(2\pi f)^2}$. Bestimme damit ohne Integral das Spektrum von $\frac{1}{1+t^2}$.

:::loesung
Symmetrie auf das Paar anwenden: $\frac{2}{1+(2\pi t)^2}\;\circ\!\!-\!\!\bullet\;\mathrm{e}^{-|f|}$. Jetzt die Zeit dehnen. Mit $x(t)=\frac{2}{1+(2\pi t)^2}$ ist $x\bigl(\frac{t}{2\pi}\bigr)=\frac{2}{1+t^2}$, nach dem Ähnlichkeitssatz mit $b=\frac1{2\pi}$ also $\circ\!\!-\!\!\bullet\;2\pi\,\mathrm{e}^{-2\pi|f|}$. Halbieren:

$$\frac{1}{1+t^2}\;\circ\!\!-\!\!\bullet\;\pi\,\mathrm{e}^{-2\pi|f|}.$$

Probe mit dem Flächensatz: $\int\frac{\mathrm{d} t}{1+t^2}=\pi=S(0)$.
:::
:::

::::kurzfassung
Die Rechenregeln der Fourier-Transformation sagen, wie sich das Spektrum ändert, wenn man das Signal verschiebt, dehnt, ableitet oder moduliert. Jede folgt daraus, was die Operation mit einer einzelnen Schwingung $\mathrm{e}^{\mathrm{j}2\pi ft}$ macht. Die wichtigsten:

<ul>

<li>

__Ähnlichkeit__: $s(bt)\;\circ\!\!-\!\!\bullet\;\frac{1}{|b|}S\bigl(\frac fb\bigr)$ für $b\neq0$. Ein gestauchtes Signal hat ein breiteres Spektrum; Dauer und Bandbreite verhalten sich umgekehrt.

</li>

<li>

__Verschiebung__: $s(t-t_0)\;\circ\!\!-\!\!\bullet\;S(f)\,\mathrm{e}^{-\mathrm{j}2\pi ft_0}$. Der Betrag bleibt, nur die Phase ändert sich, und zwar linear in $f$.

</li>

<li>

Ableitung: $\frac{\mathrm{d}}{\mathrm{d} t}$ wird zur Multiplikation mit $\mathrm{j}2\pi f$; hohe Frequenzen werden verstärkt.

</li>

<li>

__Modulation__: $\mathrm{e}^{\mathrm{j}2\pi Ft}s(t)\;\circ\!\!-\!\!\bullet\;S(f-F)$, das Spektrum wird um $F$ verschoben.

</li>

<li>

__Symmetrie__ oder Dualität: $S(t)\;\circ\!\!-\!\!\bullet\;s(-f)$. Jedes Paar liefert ein zweites mit vertauschten Rollen.

</li>

</ul>

Außerdem wird ein Produkt zweier Signale zur Faltung ihrer Spektren. Nach Parseval ist die Energie in beiden Bereichen gleich, $|S(f)|^2$ ist die __Energiedichte__ über der Frequenz.

Der Grund am Beispiel der Verschiebung: Eine Verzögerung um $t_0$ verschiebt jede Schwingung um dieselbe Zeit. Bei der Frequenz $f$ ist das der Winkel $2\pi ft_0$, bei höherer Frequenz also ein größerer. Die Symmetrie gilt, weil sich Hin- und Rücktransformation nur im Vorzeichen des Exponenten unterscheiden.

Falle: Beim Dehnen steht $f/b$ im Argument und $1/|b|$ davor, mit Betrag. Für $b<0$ wäre ein Faktor $\frac1b$ negativ, die Fläche eines Signals ändert aber durch Spiegeln ihr Vorzeichen nicht.
::::

::::formelsammlung
**Superposition**

$$\sum_ia_is_i(t)\;\circ\!\!-\!\!\bullet\;\sum_ia_iS_i(f)$$

Für beliebige Konstanten $a_i$.

**Konjugation**

$$s^*(t)\;\circ\!\!-\!\!\bullet\;S^*(-f)$$

Für reelle Signale folgt daraus $S(-f)=S^*(f)$.

**Ähnlichkeit**

$$s(bt)\;\circ\!\!-\!\!\bullet\;\frac{1}{|b|}S\Bigl(\frac fb\Bigr),\quad b\neq0;\qquad s(-t)\;\circ\!\!-\!\!\bullet\;S(-f)$$

Zeitlich gestaucht ($|b|>1$): breiteres Spektrum; Dauer und Bandbreite verhalten sich umgekehrt. Betrag $|b|$, weil sich für $b<0$ die Integrationsgrenzen umkehren.

**Verschiebung**

$$s(t-t_0)\;\circ\!\!-\!\!\bullet\;S(f)\,\mathrm{e}^{-\mathrm{j}2\pi ft_0},\qquad\delta(t-t_0)\;\circ\!\!-\!\!\bullet\;\mathrm{e}^{-\mathrm{j}2\pi ft_0}$$

Betrag unverändert. Die Phase sinkt um $2\pi ft_0$, ist also eine Gerade in $f$ mit der Steigung $-2\pi t_0$. Ein System mit $|H|=1$ und linearer Phase verzögert ein Signal, ohne seine Form zu ändern.

**Ableitung**

$$\frac{\mathrm{d}^n}{\mathrm{d} t^n}s(t)\;\circ\!\!-\!\!\bullet\;(\mathrm{j}2\pi f)^nS(f)$$

Grund: $\frac{\mathrm{d}}{\mathrm{d} t}\mathrm{e}^{\mathrm{j}2\pi ft}=\mathrm{j}2\pi f\,\mathrm{e}^{\mathrm{j}2\pi ft}$. Ableiten verstärkt hohe Frequenzen.

**Symmetrie (Dualität)**

$$S(t)\;\circ\!\!-\!\!\bullet\;s(-f)$$

Für jedes Paar $s(t)\;\circ\!\!-\!\!\bullet\;S(f)$. Hin- und Rücktransformation unterscheiden sich nur im Vorzeichen des Exponenten.

**Modulation**

$$\mathrm{e}^{\mathrm{j}2\pi Ft}s(t)\;\circ\!\!-\!\!\bullet\;S(f-F)$$

Multiplikation mit $\mathrm{e}^{\mathrm{j}2\pi Ft}$ verschiebt das ganze Spektrum um $F$.

**Ableitung im Frequenzbereich**

$$-\mathrm{j}2\pi t\,s(t)\;\circ\!\!-\!\!\bullet\;\frac{\mathrm{d}}{\mathrm{d} f}S(f)$$

Folgt durch Ableiten der Hintransformation nach $f$.

**Faltung und Multiplikation**

$$s_1*s_2\;\circ\!\!-\!\!\bullet\;S_1S_2,\qquad s_1s_2\;\circ\!\!-\!\!\bullet\;S_1*S_2$$

Das Produkt zweier Signale hat als Spektrum die Faltung der Spektren, das Gegenstück zum Faltungssatz.

**Flächensätze**

$$\int s(t)\mathrm{d} t=S(0),\qquad\int S(f)\mathrm{d} f=s(0)$$

Integrale über alle Zeiten bzw. alle Frequenzen; $f=0$ in die Hin-, $t=0$ in die Rücktransformation eingesetzt.

**Parseval**

$$\int|s(t)|^2\mathrm{d} t=\int|S(f)|^2\mathrm{d} f$$

Die Energie ist in beiden Bereichen dieselbe; $|S(f)|^2$ ist die Energiedichte über der Frequenz.

**Ein Paar aus der Symmetrie**

$$\frac{1}{1+t^2}\;\circ\!\!-\!\!\bullet\;\pi\,\mathrm{e}^{-2\pi|f|}$$

Aus $\mathrm{e}^{-|t|}\;\circ\!\!-\!\!\bullet\;\frac{2}{1+(2\pi f)^2}$ mit Symmetrie und Ähnlichkeit.
::::

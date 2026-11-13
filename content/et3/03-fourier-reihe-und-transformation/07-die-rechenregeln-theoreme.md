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

::::lernkarten
:::karte formel Ähnlichkeit
Wie ändert sich das Spektrum, wenn man ein Signal mit $s(bt)$, $b\neq0$, in der Zeit staucht oder dehnt?
---
$s(bt)\;\circ\!\!-\!\!\bullet\;\frac{1}{|b|}S\Bigl(\frac fb\Bigr)$. Ein gestauchtes Signal ($|b|>1$) hat ein breiteres, niedrigeres Spektrum: Dauer und Bandbreite verhalten sich umgekehrt. Für $b=-1$ folgt $s(-t)\;\circ\!\!-\!\!\bullet\;S(-f)$.
--- falsch
$s(bt)\;\circ\!\!-\!\!\bullet\;|b|\,S(bf)$. Ein gestauchtes Signal ($|b|>1$) hat ein schmaleres, höheres Spektrum: Dauer und Bandbreite verhalten sich gleichsinnig, kurze Signale brauchen also nur wenige Frequenzen.
--- falsch
$s(bt)\;\circ\!\!-\!\!\bullet\;\frac{1}{b}S\Bigl(\frac fb\Bigr)$, ohne Betrag. Ein gestauchtes Signal ($b>1$) hat ein breiteres Spektrum; für $b<0$ wird das Spektrum zusätzlich mit $-1$ multipliziert und kehrt sein Vorzeichen um.
--- falsch
$s(bt)\;\circ\!\!-\!\!\bullet\;S(f)\,\mathrm{e}^{-\mathrm{j}2\pi fb}$. Stauchen ändert nur die Phase des Spektrums, nicht seine Breite, denn jede Schwingung wird dabei lediglich um eine andere Zeit verschoben.
:::
:::karte herleitung Ähnlichkeitssatz durch Substitution
Wie folgt der Ähnlichkeitssatz $s(bt)\;\circ\!\!-\!\!\bullet\;\frac{1}{|b|}S\Bigl(\frac fb\Bigr)$ aus der Definition der Fourier-Transformation?
---
Man setzt $s(bt)$ in die Hintransformation ein und substituiert $\tau=bt$, weil dann wieder das ursprüngliche Signal $s(\tau)$ im Integral steht.
---
Für $b>0$ ergibt das $\int s(bt)\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t=\frac1b\int s(\tau)\mathrm{e}^{-\mathrm{j}2\pi(f/b)\tau}\mathrm{d}\tau$, weil das Differential den Faktor $\frac1b$ liefert und im Exponenten $f/b$ statt $f$ steht.
---
Das rechte Integral ist die Fourier-Transformierte an der Stelle $f/b$, weil nur die Frequenz umbenannt ist; es ergibt sich $\frac1bS(f/b)$.
---
Für $b<0$ kehren sich die Integrationsgrenzen um, weil $\tau=bt$ dann von plus nach minus unendlich läuft. Das Zurücktauschen liefert ein Minus, daher steht $1/|b|$ vor dem Spektrum.
:::
:::karte formel Verschiebung
Was macht eine zeitliche Verschiebung $s(t-t_0)$ mit dem Spektrum, und was gilt speziell für den verschobenen Dirac-Impuls?
---
$s(t-t_0)\;\circ\!\!-\!\!\bullet\;S(f)\,\mathrm{e}^{-\mathrm{j}2\pi ft_0}$: Der Betrag bleibt, die Phase sinkt um $2\pi ft_0$, linear in $f$. Für den Dirac-Impuls folgt $\delta(t-t_0)\;\circ\!\!-\!\!\bullet\;\mathrm{e}^{-\mathrm{j}2\pi ft_0}$.
--- falsch
$s(t-t_0)\;\circ\!\!-\!\!\bullet\;S(f-t_0)$: Das Spektrum wird um $t_0$ verschoben, so wie das Signal. Für den Dirac-Impuls folgt $\delta(t-t_0)\;\circ\!\!-\!\!\bullet\;1$, weil seine Lage für das Spektrum keine Rolle spielt.
--- falsch
$s(t-t_0)\;\circ\!\!-\!\!\bullet\;S(f)\,\mathrm{e}^{\mathrm{j}2\pi ft_0}$: Der Betrag bleibt, die Phase steigt um $2\pi ft_0$, linear in $f$. Für den Dirac-Impuls folgt $\delta(t-t_0)\;\circ\!\!-\!\!\bullet\;\mathrm{e}^{\mathrm{j}2\pi ft_0}$.
--- falsch
$s(t-t_0)\;\circ\!\!-\!\!\bullet\;S(f)\,\mathrm{e}^{-t_0f}$: Der Betrag nimmt mit der Frequenz exponentiell ab, umso stärker, je größer $t_0$ ist. Für den Dirac-Impuls folgt $\delta(t-t_0)\;\circ\!\!-\!\!\bullet\;\mathrm{e}^{-t_0f}$.
:::
:::karte zusammenhang Verzögerung und lineare Phase
Warum ändert eine Verzögerung um $t_0$ den Betrag des Spektrums nicht, wohl aber die Phase, und zwar linear in $f$?
---
Eine Verzögerung schwächt oder verstärkt keine Schwingung, sie verschiebt jede um dieselbe Zeit $t_0$. Bei der Frequenz $f$ ist das der Winkel $2\pi ft_0$, bei höherer Frequenz also ein größerer. Die Phase ist eine Gerade in $f$ mit der Steigung $-2\pi t_0$.
--- falsch
Eine Verzögerung verschiebt jede Schwingung um denselben Winkel, unabhängig von der Frequenz. Weil sich dieser Winkel aber bei negativen Frequenzen umkehrt, wird die Phase insgesamt zu einer Geraden mit der Steigung $-2\pi t_0$.
--- falsch
Eine Verzögerung schwächt die hohen Frequenzen ab, weil sie sich in der Zeit $t_0$ öfter wiederholen. Diese Schwächung gleicht sie genau durch eine Phasendrehung aus, sodass der Betrag am Ende unverändert bleibt.
--- falsch
Eine Verzögerung verschiebt jede Schwingung um dieselbe Zeit $t_0$. Bei der Frequenz $f$ ist das der Winkel $2\pi t_0/f$, bei höherer Frequenz also ein kleinerer. Die Phase fällt deshalb wie $1/f$ ab und ist keine Gerade.
:::
:::karte formel Ableitung
Was wird bei der Fourier-Transformation aus der $n$-ten Ableitung eines Signals, und warum verstärkt Ableiten hohe Frequenzen?
---
$\frac{\mathrm{d}^n}{\mathrm{d} t^n}s(t)\;\circ\!\!-\!\!\bullet\;(\mathrm{j}2\pi f)^nS(f)$. Grund: $\frac{\mathrm{d}}{\mathrm{d} t}\mathrm{e}^{\mathrm{j}2\pi ft}=\mathrm{j}2\pi f\,\mathrm{e}^{\mathrm{j}2\pi ft}$, jede Schwingung wird mit $\mathrm{j}2\pi f$ multipliziert, also umso stärker, je höher ihre Frequenz ist.
--- falsch
$\frac{\mathrm{d}^n}{\mathrm{d} t^n}s(t)\;\circ\!\!-\!\!\bullet\;\frac{S(f)}{(\mathrm{j}2\pi f)^n}$. Grund: Jede Schwingung wird beim Ableiten durch $\mathrm{j}2\pi f$ geteilt, die tiefen Frequenzen werden also stärker verändert als die hohen, die im Verhältnis wachsen.
--- falsch
$\frac{\mathrm{d}^n}{\mathrm{d} t^n}s(t)\;\circ\!\!-\!\!\bullet\;(2\pi f)^nS(f)$, ohne $\mathrm{j}$, weil Ableiten nur die Amplitude ändert. Hohe Frequenzen werden verstärkt, die Phase des Spektrums bleibt aber unverändert, wie oft man auch ableitet.
--- falsch
$\frac{\mathrm{d}^n}{\mathrm{d} t^n}s(t)\;\circ\!\!-\!\!\bullet\;\frac{\mathrm{d}^n}{\mathrm{d} f^n}S(f)$. Grund: Ableiten im Zeitbereich ist Ableiten im Frequenzbereich, und die Ableitung des Spektrums ist bei hohen Frequenzen am größten.
:::
:::karte formel Modulation
Was macht die Multiplikation eines Signals mit $\mathrm{e}^{\mathrm{j}2\pi Ft}$ mit seinem Spektrum, und wo nutzt man das?
---
$\mathrm{e}^{\mathrm{j}2\pi Ft}s(t)\;\circ\!\!-\!\!\bullet\;S(f-F)$: Das ganze Spektrum wird um $F$ verschoben, seine Form bleibt. So arbeitet jeder Rundfunksender.
--- falsch
$\mathrm{e}^{\mathrm{j}2\pi Ft}s(t)\;\circ\!\!-\!\!\bullet\;S(f+F)$: Das ganze Spektrum wird um $F$ zu tieferen Frequenzen verschoben, seine Form bleibt dabei erhalten. So arbeitet jeder Rundfunksender.
--- falsch
$\mathrm{e}^{\mathrm{j}2\pi Ft}s(t)\;\circ\!\!-\!\!\bullet\;S(f)\,\mathrm{e}^{-\mathrm{j}2\pi fF}$: Das Spektrum behält seine Lage, nur seine Phase dreht sich linear in $f$. So arbeitet jede Verzögerungsleitung.
--- falsch
$\mathrm{e}^{\mathrm{j}2\pi Ft}s(t)\;\circ\!\!-\!\!\bullet\;S(f)\cdot\delta(f-F)$: Vom Spektrum bleibt nur der Wert bei $F$ übrig, alle anderen Frequenzen verschwinden. So arbeitet ein schmales Filter.
:::
:::karte formel Symmetrie
Welches zweite Transformationspaar liefert die Symmetrie (Dualität) zu einem Paar $s(t)\;\circ\!\!-\!\!\bullet\;S(f)$, und warum gibt es sie?
---
$S(t)\;\circ\!\!-\!\!\bullet\;s(-f)$: Man nimmt das Spektrum als Zeitsignal. Das geht, weil sich Hin- und Rücktransformation nur im Vorzeichen des Exponenten unterscheiden. Jedes Paar liefert so ein zweites mit vertauschten Rollen.
--- falsch
$S(t)\;\circ\!\!-\!\!\bullet\;s(f)$: Man nimmt das Spektrum als Zeitsignal und erhält das ursprüngliche Signal als Spektrum, ganz ohne Spiegelung, weil Hin- und Rücktransformation genau dieselbe Formel sind.
--- falsch
$S^*(t)\;\circ\!\!-\!\!\bullet\;s^*(f)$: Man nimmt das konjugierte Spektrum als Zeitsignal. Das geht nur bei reellen Signalen, weil sich nur dort Hin- und Rücktransformation durch Konjugieren ineinander überführen lassen.
--- falsch
$S(t)\;\circ\!\!-\!\!\bullet\;\frac{1}{s(f)}$: Man nimmt das Spektrum als Zeitsignal und erhält den Kehrwert des Signals als Spektrum, weil Hin- und Rücktransformation zueinander invers sind.
:::
:::karte herleitung Symmetrie aus der Rücktransformation
Wie gewinnt man aus der Rücktransformation $s(t)=\int_{-\infty}^{\infty}S(f)\,\mathrm{e}^{\mathrm{j}2\pi ft}\,\mathrm{d} f$ die Symmetrie $S(t)\;\circ\!\!-\!\!\bullet\;s(-f)$?
---
Man ersetzt in der Rücktransformation $t$ durch $-t$, weil dann im Exponenten das Minuszeichen der Hintransformation steht: $s(-t)=\int S(f)\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} f$.
---
Man tauscht die Namen der Variablen $t$ und $f$, weil Variablen beliebig heißen dürfen: $s(-f)=\int S(t)\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t$.
---
Rechts steht jetzt die Hintransformation der Zeitfunktion $S(t)$, weil über $t$ mit dem Faktor $\mathrm{e}^{-\mathrm{j}2\pi ft}$ integriert wird. Also ist $s(-f)$ ihr Spektrum.
:::
:::karte formel Faltung und Multiplikation
Welches Spektrum hat das Produkt $s_1s_2$ zweier Signale, und woraus folgt diese Regel?
---
$s_1s_2\;\circ\!\!-\!\!\bullet\;S_1*S_2$: die Faltung der Spektren, das Gegenstück zum Faltungssatz $s_1*s_2\;\circ\!\!-\!\!\bullet\;S_1S_2$. Sie folgt, indem man die Symmetrie auf den Faltungssatz anwendet.
--- falsch
$s_1s_2\;\circ\!\!-\!\!\bullet\;S_1S_2$: das Produkt der Spektren, genau wie bei der Faltung. Produkt und Faltung zweier Signale haben also dasselbe Spektrum, weil beide Operationen linear sind.
--- falsch
$s_1s_2\;\circ\!\!-\!\!\bullet\;S_1+S_2$: die Summe der Spektren. Sie folgt aus der Superposition, denn jede Schwingung des einen Signals überlagert sich mit jeder des anderen, ohne dass neue Frequenzen entstehen.
--- falsch
$s_1s_2\;\circ\!\!-\!\!\bullet\;S_1*S_2$, aber nur, wenn eines der Signale reell ist. Sie folgt aus dem Ableitungssatz, weil die Ableitung eines Produkts nach der Produktregel zu einer Faltung wird.
:::
:::karte formel Flächensätze
Wie erhält man die Fläche eines Signals aus seinem Spektrum, und wie den Signalwert bei $t=0$?
---
$\int s(t)\mathrm{d} t=S(0)$ und $\int S(f)\mathrm{d} f=s(0)$, integriert über alle Zeiten bzw. alle Frequenzen. Man setzt $f=0$ in die Hin- und $t=0$ in die Rücktransformation ein, denn dort ist der Exponentialfaktor 1.
--- falsch
$\int s(t)\mathrm{d} t=s(0)$ und $\int S(f)\mathrm{d} f=S(0)$: Die Fläche eines Signals ist sein Wert in der Mitte, die Fläche des Spektrums dessen Wert bei $f=0$, weil der Exponentialfaktor dort 1 ist.
--- falsch
$\int s(t)\mathrm{d} t=\int S(f)\mathrm{d} f$: Signal und Spektrum haben stets dieselbe Fläche, weil die Fourier-Transformation Flächen erhält. Den Wert $s(0)$ kann man aus dem Spektrum dagegen nicht ablesen.
--- falsch
$\int s(t)\mathrm{d} t=|S(0)|^2$ und $\int S(f)\mathrm{d} f=|s(0)|^2$: Man setzt $f=0$ bzw. $t=0$ ein und quadriert den Betrag, weil Flächen Energien sind und Energien quadratisch eingehen.
:::
:::karte begriff Energiedichte
Was gibt $|S(f)|^2$ nach dem Satz von Parseval für die Fourier-Transformation an?
---
Die Energiedichte des Signals über der Frequenz: Nach Parseval ist $\int|s(t)|^2\mathrm{d} t=\int|S(f)|^2\mathrm{d} f$, die Energie ist in beiden Bereichen dieselbe. $|S(f)|^2$ sagt, wie sich diese Energie auf die Frequenzen verteilt.
--- falsch
Die Leistung der Harmonischen mit der Frequenz $f$: Nach Parseval ist die Energie die Summe der Werte $|S(kF)|^2$, sie verteilt sich also auf einzelne Linien endlicher Leistung bei den Vielfachen von $F$.
--- falsch
Die Energiedichte über der Zeit: Nach Parseval ist $|s(t)|^2=|S(t)|^2$ für jedes $t$, das Spektrum zeigt also, wann im Signal wie viel Energie steckt, und zwar zu jedem einzelnen Zeitpunkt.
--- falsch
Die Energiedichte über der Frequenz, aber erst nach Multiplikation mit $2\pi$: Nach Parseval ist $\int|s(t)|^2\mathrm{d} t=2\pi\int|S(f)|^2\mathrm{d} f$, weil über $f$ statt über $2\pi f$ integriert wird.
:::
:::karte formel Ein Paar aus der Symmetrie
Welches Spektrum hat $\frac{1}{1+t^2}$, wenn man vom Paar $\mathrm{e}^{-|t|}\;\circ\!\!-\!\!\bullet\;\frac{2}{1+(2\pi f)^2}$ ausgeht und nur die Theoreme benutzt?
---
$\frac{1}{1+t^2}\;\circ\!\!-\!\!\bullet\;\pi\,\mathrm{e}^{-2\pi|f|}$. Die Symmetrie liefert $\frac{2}{1+(2\pi t)^2}\;\circ\!\!-\!\!\bullet\;\mathrm{e}^{-|f|}$, die Ähnlichkeit mit $b=\frac1{2\pi}$ dehnt die Zeit, Halbieren ergibt das Paar. Probe: $\int\frac{\mathrm{d} t}{1+t^2}=\pi=S(0)$.
--- falsch
$\frac{1}{1+t^2}\;\circ\!\!-\!\!\bullet\;\frac12\mathrm{e}^{-|f|}$. Die Symmetrie liefert $\frac{2}{1+(2\pi t)^2}\;\circ\!\!-\!\!\bullet\;\mathrm{e}^{-|f|}$, und weil $2\pi$ nur ein Maßstab ist, genügt Halbieren. Probe: Die Fläche ist $S(0)=\frac12$.
--- falsch
$\frac{1}{1+t^2}\;\circ\!\!-\!\!\bullet\;\pi\,\mathrm{e}^{-2\pi f}$ für alle $f$. Die Symmetrie liefert das gespiegelte Paar, und die Ähnlichkeit mit $b=\frac1{2\pi}$ dehnt die Zeit; der Betrag im Exponenten fällt dabei weg, weil $b>0$ ist.
--- falsch
$\frac{1}{1+t^2}\;\circ\!\!-\!\!\bullet\;2\pi\,\mathrm{e}^{-|f|/(2\pi)}$. Die Ähnlichkeit mit $b=2\pi$ staucht die Zeit, und das Spektrum wird dabei breiter und höher. Probe: Die Fläche ist $S(0)=2\pi$, wie es die Dehnung verlangt.
:::
::::

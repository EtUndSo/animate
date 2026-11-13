---
title: Stufe 5: Symmetrien im Signal und im Spektrum
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Fourier-Reihe und -Transformation
adresse: elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation
knoten: Kapitel 3: Fourier-Reihe und -Transformation
order: 3230600
summary: Ob ein Signal reell, gerade oder ungerade ist, sieht man seinem Spektrum sofort an.
tags: gerade, ungerade
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Ob ein Signal reell, gerade oder ungerade ist, sieht man seinem Spektrum sofort an. Diese Stufe leitet die Regeln her.
:::

**Gerade und ungerade Anteile.** Eine komplexe Funktion heißt __gerade__, wenn $x(t)=x^*(-t)$, und __ungerade__, wenn $x(t)=-x^*(-t)$. (Für reelle Funktionen ist das die übliche Spiegel- bzw. Punktsymmetrie.) Jedes Signal zerfällt eindeutig in beide Anteile:

<span class="anker" id="gl-5-1"></span>
$$s(t)=s_g(t)+s_u(t),\qquad s_g(t)=\tfrac12\bigl[s(t)+s^*(-t)\bigr],\qquad s_u(t)=\tfrac12\bigl[s(t)-s^*(-t)\bigr]. \tag{5.1}$$

:::satz Satz 5.1 (Symmetrien)
<span class="anker" id="satz-5-1"></span>

<span class="anker" id="gl-5-2"></span>
$$s_g(t)\;\circ\!\!-\!\!\bullet\;\operatorname{Re}\{S(f)\},\qquad s_u(t)\;\circ\!\!-\!\!\bullet\;\mathrm{j}\operatorname{Im}\{S(f)\}. \tag{5.2}$$

Für **reelle** Signale gilt $S(-f)=S^*(f)$: Der Realteil und der Betrag $|S|$ sind gerade in $f$, der Imaginärteil und die Phase ungerade. Ein reelles, gerades Signal hat ein reelles, gerades Spektrum. Ein reelles, ungerades Signal hat ein rein imaginäres, ungerades Spektrum.
:::

:::herleitung Symmetrien
Zuerst: $\mathcal{F}\{s^*(-t)\}=\int s^*(-t)\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t$. Mit $\tau=-t$ ist das $\int s^*(\tau)\mathrm{e}^{\mathrm{j}2\pi f\tau}\mathrm{d}\tau=\bigl(\int s(\tau)\mathrm{e}^{-\mathrm{j}2\pi f\tau}\mathrm{d}\tau\bigr)^*=S^*(f)$. Damit

$$\mathcal{F}\{s_g\}=\tfrac12\bigl[S(f)+S^*(f)\bigr]=\operatorname{Re}\{S(f)\},\qquad\mathcal{F}\{s_u\}=\tfrac12\bigl[S(f)-S^*(f)\bigr]=\mathrm{j}\operatorname{Im}\{S(f)\}.$$

Für reelles $s$ ist $\mathcal{F}\{s^*(t)\}=\mathcal{F}\{s(t)\}$. Allgemein gilt $\mathcal{F}\{s^*(t)\}=\int s^*\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t=\bigl(\int s\,\mathrm{e}^{\mathrm{j}2\pi ft}\mathrm{d} t\bigr)^*=S^*(-f)$. Also $S(f)=S^*(-f)$.
:::

⁠**Kurz gesagt:** Bei einem reellen Signal ist die negative Hälfte des Spektrums das konjugierte Spiegelbild der positiven. Sie enthält keine neue Information.

::::beispiel
Der Exponentialimpuls $\varepsilon(t)\mathrm{e}^{-t}$ (reell) hat den geraden Anteil $\frac12\mathrm{e}^{-|t|}$ und den ungeraden $\frac12\operatorname{sgn}(t)\mathrm{e}^{-|t|}$. Sein Spektrum $H(f)=\frac{1}{1+\mathrm{j}2\pi f}$ hat den geraden Realteil $\frac{1}{1+(2\pi f)^2}$, die Transformierte von $\frac12\mathrm{e}^{-|t|}$, und den ungeraden Imaginärteil $\frac{-2\pi f}{1+(2\pi f)^2}$ (Abb. [5](#abb-5)).

:::abbildung et3/k3gerade 5
Der Exponentialimpuls ($RC=1$ s), zerlegt in einen geraden (blau) und einen ungeraden Anteil (rot). Rechts das Spektrum: Der gerade Anteil liefert den Realteil (gerade in $f$), der ungerade Anteil den Imaginärteil (ungerade in $f$).
:::
::::

:::aufgabe Aufgabe 5 ★ Symmetrie ablesen
<span class="anker" id="aufg-5"></span>

Was lässt sich ohne Rechnung über das Spektrum sagen? (a) $s(t)=\operatorname{rect}(t)$, (b) $s(t)=\operatorname{sgn}(t)\operatorname{rect}(t/2)$, (c) $s(t)=\mathrm{e}^{\mathrm{j}2\pi t}\operatorname{rect}(t)$, (d) ein reelles Signal mit $S(1\,\mathrm{Hz})=2-3\mathrm{j}$: Was ist $S(-1\,\mathrm{Hz})$?

:::loesung
(a) Reell und gerade: Spektrum reell und gerade ($\operatorname{si}(\pi f)$). (b) Reell und ungerade: Spektrum rein imaginär und ungerade. (c) Komplex, aber $x^*(-t)=\mathrm{e}^{-\mathrm{j}2\pi(-t)}\operatorname{rect}(-t)=x(t)$: Im Sinne der Definition ist das Signal gerade, also ist sein Spektrum reell. Nach der Modulationsregel ist es $\operatorname{si}(\pi(f-1))$, reell, aber nicht symmetrisch um $f=0$, weil das Signal nicht reell ist. (d) $S(-1\,\mathrm{Hz})=S^*(1\,\mathrm{Hz})=2+3\mathrm{j}$.
:::
:::

::::kurzfassung
Ob ein Signal reell, gerade oder ungerade ist, liest man direkt an seinem Spektrum ab. Bei einem reellen Signal ist die Hälfte des Spektrums bei negativen Frequenzen schon durch die positive Hälfte festgelegt.

Eine komplexe Funktion heißt __gerade__, wenn $x(t)=x^*(-t)$, und __ungerade__, wenn $x(t)=-x^*(-t)$. Für reelle Funktionen ist das die übliche Spiegel- bzw. Punktsymmetrie. Jedes Signal zerfällt eindeutig in einen geraden Anteil $s_g(t)=\tfrac12\bigl[s(t)+s^*(-t)\bigr]$ und einen ungeraden Anteil $s_u(t)=\tfrac12\bigl[s(t)-s^*(-t)\bigr]$. Ihre Spektren sind Real- und Imaginärteil des ganzen Spektrums:

$$s_g(t)\;\circ\!\!-\!\!\bullet\;\operatorname{Re}\{S(f)\},\qquad s_u(t)\;\circ\!\!-\!\!\bullet\;\mathrm{j}\operatorname{Im}\{S(f)\}.$$

Für reelle Signale gilt $S(-f)=S^*(f)$: Realteil und Betrag sind gerade in $f$, Imaginärteil und Phase ungerade. Ein reelles, gerades Signal hat deshalb ein reelles, gerades Spektrum, ein reelles, ungerades Signal ein rein imaginäres, ungerades.

Der Grund: Spiegeln und Konjugieren des Signals konjugiert das Spektrum, $\mathcal{F}\{s^*(-t)\}=S^*(f)$. Damit wird aus $\tfrac12\bigl[s(t)+s^*(-t)\bigr]$ im Spektrum $\tfrac12\bigl[S(f)+S^*(f)\bigr]=\operatorname{Re}\{S(f)\}$. Ein reelles Signal enthält jede Schwingung zusammen mit ihrer konjugierten Partnerin bei der negativen Frequenz.

Falle: $S(-f)=S^*(f)$ gilt nur für reelle Signale. Ein komplexes Signal kann bei positiven und negativen Frequenzen völlig verschiedene Anteile haben; dort enthält die negative Hälfte eigene Information.
::::

::::formelsammlung
**Gerade und ungerade Funktion**

$$x(t)=x^*(-t),\qquad x(t)=-x^*(-t)$$

Links gerade, rechts ungerade. Für reelle Funktionen die übliche Spiegel- bzw. Punktsymmetrie.

**Zerlegung in geraden und ungeraden Anteil**

$$s(t)=s_g(t)+s_u(t),\qquad s_g(t)=\tfrac12\bigl[s(t)+s^*(-t)\bigr],\qquad s_u(t)=\tfrac12\bigl[s(t)-s^*(-t)\bigr]$$

Für jedes Signal, eindeutig.

**Gespiegeltes und konjugiertes Signal**

$$\mathcal{F}\{s^*(-t)\}=S^*(f)$$

Spiegeln und Konjugieren des Signals konjugiert das Spektrum.

**Symmetriesatz**

$$s_g(t)\;\circ\!\!-\!\!\bullet\;\operatorname{Re}\{S(f)\},\qquad s_u(t)\;\circ\!\!-\!\!\bullet\;\mathrm{j}\operatorname{Im}\{S(f)\}$$

Der gerade Anteil liefert den Realteil, der ungerade Anteil den mit $\mathrm{j}$ multiplizierten Imaginärteil des Spektrums.

**Reelle Signale**

$$S(-f)=S^*(f)$$

Realteil und Betrag $|S|$ gerade in $f$, Imaginärteil und Phase ungerade. Reell und gerade: Spektrum reell und gerade. Reell und ungerade: Spektrum rein imaginär und ungerade.
::::

::::lernkarten
:::karte begriff gerade und ungerade
Wann heißt eine komplexe Funktion $x(t)$ gerade und wann ungerade?
---
Gerade, wenn $x(t)=x^*(-t)$, ungerade, wenn $x(t)=-x^*(-t)$: Spiegeln an $t=0$ und Konjugieren ergibt die Funktion selbst bzw. ihr Negatives. Für reelle Funktionen ist das die übliche Spiegel- bzw. Punktsymmetrie.
--- falsch
Gerade, wenn $x(t)=x(-t)$, ungerade, wenn $x(t)=-x(-t)$, ganz ohne Konjugation: Bei komplexen Funktionen müssen Real- und Imaginärteil jeweils für sich spiegelsymmetrisch bzw. punktsymmetrisch sein.
--- falsch
Gerade, wenn $x(t)=x^*(t)$, ungerade, wenn $x(t)=-x^*(t)$: Die Funktion ist also gerade, wenn sie reell ist, und ungerade, wenn sie rein imaginär ist. Die Zeit wird dabei nicht gespiegelt.
--- falsch
Gerade, wenn $x(t)=x^*(-t)$, ungerade, wenn $x(t)=-x^*(-t)$. Für reelle Funktionen ist gerade dabei die Punktsymmetrie zum Ursprung und ungerade die Spiegelsymmetrie zur senkrechten Achse.
:::
:::karte formel Zerlegung in geraden und ungeraden Anteil
Wie zerlegt man ein beliebiges Signal $s(t)$ in seinen geraden und seinen ungeraden Anteil?
---
$s(t)=s_g(t)+s_u(t)$ mit $s_g(t)=\tfrac12\bigl[s(t)+s^*(-t)\bigr]$ und $s_u(t)=\tfrac12\bigl[s(t)-s^*(-t)\bigr]$. Diese Zerlegung gibt es für jedes Signal, und sie ist eindeutig.
--- falsch
$s(t)=s_g(t)+s_u(t)$ mit $s_g(t)=\operatorname{Re}\{s(t)\}$ und $s_u(t)=\mathrm{j}\operatorname{Im}\{s(t)\}$. Der Realteil ist stets gerade, der Imaginärteil stets ungerade, und die Zerlegung ist eindeutig.
--- falsch
$s(t)=s_g(t)\cdot s_u(t)$ mit $s_g(t)=|s(t)|$ und $s_u(t)=s(t)/|s(t)|$. Der Betrag ist gerade, der Faktor mit der Phase ungerade; die Zerlegung gibt es nur für Signale ohne Nullstellen.
--- falsch
$s(t)=s_g(t)+s_u(t)$ mit $s_g(t)=\tfrac12\bigl[s(t)+s^*(t)\bigr]$ und $s_u(t)=\tfrac12\bigl[s(t)-s^*(t)\bigr]$. Die Zeit wird nicht gespiegelt; für reelle Signale ist der ungerade Anteil deshalb null.
:::
:::karte formel Symmetriesatz
Welche Teile des Spektrums $S(f)$ gehören zum geraden und welche zum ungeraden Anteil eines Signals?
---
$s_g(t)\;\circ\!\!-\!\!\bullet\;\operatorname{Re}\{S(f)\}$ und $s_u(t)\;\circ\!\!-\!\!\bullet\;\mathrm{j}\operatorname{Im}\{S(f)\}$: Der gerade Anteil liefert den Realteil, der ungerade den mit $\mathrm{j}$ multiplizierten Imaginärteil des Spektrums.
--- falsch
$s_g(t)\;\circ\!\!-\!\!\bullet\;\mathrm{j}\operatorname{Im}\{S(f)\}$ und $s_u(t)\;\circ\!\!-\!\!\bullet\;\operatorname{Re}\{S(f)\}$: Der gerade Anteil liefert den mit $\mathrm{j}$ multiplizierten Imaginärteil, der ungerade den Realteil des Spektrums.
--- falsch
$s_g(t)\;\circ\!\!-\!\!\bullet\;|S(f)|$ und $s_u(t)\;\circ\!\!-\!\!\bullet\;\arg S(f)$: Der gerade Anteil legt den Betrag des Spektrums fest, der ungerade Anteil seine Phase, und zwar für jede Frequenz einzeln.
--- falsch
$s_g(t)\;\circ\!\!-\!\!\bullet\;S(f)$ für $f>0$ und $s_u(t)\;\circ\!\!-\!\!\bullet\;S(f)$ für $f<0$: Der gerade Anteil liefert die positive, der ungerade die negative Hälfte des Spektrums.
:::
:::karte herleitung Spektren des geraden und des ungeraden Anteils
Wie folgt aus der Definition der Fourier-Transformation, dass der gerade Anteil eines Signals das Spektrum $\operatorname{Re}\{S(f)\}$ hat und der ungerade das Spektrum $\mathrm{j}\operatorname{Im}\{S(f)\}$?
---
Zuerst transformiert man das gespiegelte, konjugierte Signal, weil es in beiden Anteilen vorkommt: $\mathcal{F}\{s^*(-t)\}=\int s^*(-t)\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t$.
---
Mit $\tau=-t$ wird daraus $\int s^*(\tau)\mathrm{e}^{\mathrm{j}2\pi f\tau}\mathrm{d}\tau$, weil sich die vertauschten Integrationsgrenzen und das Minus aus dem Differential aufheben.
---
Das ist $\bigl(\int s(\tau)\mathrm{e}^{-\mathrm{j}2\pi f\tau}\mathrm{d}\tau\bigr)^*=S^*(f)$, weil man die Konjugation vor das Integral ziehen darf und sie das Vorzeichen im Exponenten umkehrt.
---
Damit ist $\mathcal{F}\{s_g\}=\tfrac12\bigl[S(f)+S^*(f)\bigr]=\operatorname{Re}\{S(f)\}$, weil die Transformation linear ist und eine Zahl plus ihre konjugierte das Doppelte des Realteils ergibt.
---
Ebenso ist $\mathcal{F}\{s_u\}=\tfrac12\bigl[S(f)-S^*(f)\bigr]=\mathrm{j}\operatorname{Im}\{S(f)\}$, weil eine Zahl minus ihre konjugierte das $2\mathrm{j}$-Fache des Imaginärteils ergibt.
:::
:::karte formel Spektrum reeller Signale
Welche Symmetrie hat das Spektrum eines reellen Signals, und was folgt daraus für Real- und Imaginärteil, Betrag und Phase?
---
$S(-f)=S^*(f)$, denn für reelles $s$ stimmt $\mathcal{F}\{s^*(t)\}=S^*(-f)$ mit $S(f)$ überein. Realteil und Betrag $|S|$ sind gerade in $f$, Imaginärteil und Phase ungerade.
--- falsch
$S(-f)=S(f)$, denn ein reelles Signal bevorzugt keine Richtung auf der Frequenzachse. Realteil, Imaginärteil, Betrag und Phase sind deshalb alle gerade in $f$.
--- falsch
$S(-f)=S^*(f)$, denn für reelles $s$ ist das Konjugieren wirkungslos. Realteil und Phase sind gerade in $f$, Imaginärteil und Betrag ungerade, weil das Konjugieren nur den Imaginärteil umdreht.
--- falsch
$S(-f)=-S(f)$, denn das Spektrum eines reellen Signals ist punktsymmetrisch. Betrag und Phase sind ungerade in $f$, und deshalb ist bei reellen Signalen stets $S(0)=0$.
:::
:::karte zusammenhang Negative Frequenzen reeller Signale
Warum enthält bei einem reellen Signal die negative Hälfte des Spektrums keine neue Information?
---
Wegen $S(-f)=S^*(f)$ ist sie das konjugierte Spiegelbild der positiven Hälfte. Die Schwingungen eines reellen Signals treten in konjugierten Paaren auf, und erst ein solches Paar ergibt eine reelle Schwingung.
--- falsch
Weil negative Frequenzen physikalisch nicht vorkommen. Die negative Hälfte ist bei reellen Signalen stets null, und man zeichnet sie nur der Vollständigkeit halber mit, damit die Formeln symmetrisch bleiben.
--- falsch
Wegen $S(-f)=S(f)$ ist sie eine exakte Kopie der positiven Hälfte. Jede Schwingung tritt zweimal mit demselben Gewicht auf, und die beiden Hälften zusammen ergeben das doppelte Signal.
--- falsch
Weil sie nur den Imaginärteil des Signals beschreibt, die positive Hälfte dagegen den Realteil. Bei einem reellen Signal ist der Imaginärteil null, und die negative Hälfte trägt deshalb nichts bei.
:::
:::karte zusammenhang Reelle gerade und reelle ungerade Signale
Was lässt sich ohne Rechnung über das Spektrum eines reellen, geraden und über das eines reellen, ungeraden Signals sagen?
---
Ein reelles, gerades Signal hat ein reelles, gerades Spektrum, denn sein ungerader Anteil und damit $\operatorname{Im}\{S(f)\}$ sind null. Ein reelles, ungerades Signal hat ein rein imaginäres, ungerades Spektrum, denn hier ist $\operatorname{Re}\{S(f)\}$ null.
--- falsch
Ein reelles, gerades Signal hat ein rein imaginäres, gerades Spektrum, ein reelles, ungerades ein reelles, ungerades Spektrum. Der Imaginärteil des Spektrums gehört also zum geraden Anteil, der Realteil zum ungeraden.
--- falsch
Ein reelles, gerades Signal hat ein reelles Spektrum, das aber ungerade ist; ein reelles, ungerades Signal hat ein imaginäres, gerades Spektrum. Die Symmetrie in $f$ ist also stets entgegengesetzt zu der in $t$.
--- falsch
Beide haben ein reelles Spektrum, weil das Signal reell ist. Ob das Spektrum gerade oder ungerade ist, hängt nicht von der Symmetrie des Signals ab, sondern nur davon, ob sein Mittelwert null ist.
:::
:::karte zusammenhang Komplexes gerades Signal
Warum hat das komplexe Signal $\mathrm{e}^{\mathrm{j}2\pi t}\operatorname{rect}(t)$ ein reelles Spektrum, das aber nicht symmetrisch um $f=0$ liegt?
---
Es ist im Sinne der Definition gerade, denn $x^*(-t)=\mathrm{e}^{-\mathrm{j}2\pi(-t)}\operatorname{rect}(-t)=x(t)$, und ein gerades Signal hat ein reelles Spektrum. Die Symmetrie $S(-f)=S^*(f)$ gilt aber nur für reelle Signale, und dieses ist nicht reell.
--- falsch
Weil jedes Signal, das nur in einem endlichen Zeitbereich von null verschieden ist, ein reelles Spektrum hat. Die fehlende Symmetrie um $f=0$ kommt daher, dass das Rechteck an seinen beiden Rändern springt.
--- falsch
Es ist reell, weil $\mathrm{e}^{\mathrm{j}2\pi t}$ den Betrag 1 hat und ein Signal mit reellem Betrag stets ein reelles Spektrum hat. Symmetrisch um $f=0$ wäre das Spektrum nur, wenn auch die Phase des Signals konstant wäre.
--- falsch
Es ist im Sinne der Definition ungerade, denn $x^*(-t)=-x(t)$, und ein ungerades Signal hat ein reelles Spektrum. Die Symmetrie um $f=0$ geht verloren, weil das Signal komplex ist und keine konjugierten Paare bildet.
:::
:::karte formel Exponentialimpuls zerlegt
In welche Anteile zerfällt der reelle Exponentialimpuls $\varepsilon(t)\mathrm{e}^{-t}$, und welche Teile seines Spektrums $H(f)=\frac{1}{1+\mathrm{j}2\pi f}$ gehören zu ihnen?
---
Der gerade Anteil $\frac12\mathrm{e}^{-|t|}$ liefert den geraden Realteil $\frac{1}{1+(2\pi f)^2}$. Der ungerade Anteil $\frac12\operatorname{sgn}(t)\mathrm{e}^{-|t|}$ liefert den ungeraden Imaginärteil $\frac{-2\pi f}{1+(2\pi f)^2}$.
--- falsch
Der gerade Anteil $\frac12\mathrm{e}^{-|t|}$ liefert den ungeraden Imaginärteil $\frac{-2\pi f}{1+(2\pi f)^2}$. Der ungerade Anteil $\frac12\operatorname{sgn}(t)\mathrm{e}^{-|t|}$ liefert den geraden Realteil $\frac{1}{1+(2\pi f)^2}$.
--- falsch
Der gerade Anteil $\mathrm{e}^{-|t|}$ liefert den Realteil $\frac{1}{1+(2\pi f)^2}$. Der ungerade Anteil ist null, weil der Impuls für $t<0$ verschwindet; der Imaginärteil kommt allein aus dem Sprung bei $t=0$.
--- falsch
Der gerade Anteil $\frac12\mathrm{e}^{-|t|}$ liefert den Betrag $\frac{1}{\sqrt{1+(2\pi f)^2}}$ des Spektrums. Der ungerade Anteil $\frac12\operatorname{sgn}(t)\mathrm{e}^{-|t|}$ liefert seine Phase $-\arctan(2\pi f)$.
:::
::::

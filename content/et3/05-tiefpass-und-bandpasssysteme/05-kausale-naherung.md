---
title: Stufe 4: Kausale Näherung
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / Tiefpass- und Bandpasssysteme
order: 3250500
summary: Wie baut man etwas, das dem idealen Tiefpass möglichst nahekommt?
tags: 
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Wie baut man etwas, das dem idealen Tiefpass möglichst nahekommt? Man verzögert die Impulsantwort und schneidet den Rest ab.
:::

**Die Idee.** Man verschiebt $h(t)$ um $t_0$ nach rechts, bis der Teil bei $t<0$ vernachlässigbar ist, und schneidet ihn ab. Die Hüllkurve der si-Funktion fällt wie $1/(2\pi f_\mathrm g|t|)$. Soll sie vor $t=0$ unter 1 % des Maximums liegen, braucht man $t_0\approx16/f_\mathrm g$. Mit einem symmetrischen Fenster der Breite $2t_0$:

<span class="anker" id="gl-4-1"></span>
$$h_k(t)=2f_\mathrm g\operatorname{si}\bigl(2\pi f_\mathrm g(t-t_0)\bigr)\operatorname{rect}\Bigl(\frac{t-t_0}{2t_0}\Bigr)\;\circ\!\!-\!\!\bullet\;H_k(f)=\Bigl[\operatorname{rect}\Bigl(\frac{f}{2f_\mathrm g}\Bigr)*2t_0\operatorname{si}(2\pi t_0f)\Bigr]\mathrm{e}^{-\mathrm{j}2\pi t_0f}. \tag{4.1}$$

⁠**So liest man das:** Das Abschneiden ist eine Multiplikation mit einem Fenster, im Spektrum also eine Faltung mit dessen si-Spektrum. Die scharfe Kante wird verschmiert und bekommt Wellen. Der Faktor $\mathrm{e}^{-\mathrm{j}2\pi t_0f}$ ist die Verzögerung: Das kausale Filter hat eine lineare Phase, es verzögert alle Frequenzen gleich (Abb. [2](#abb-2)). Je größer $t_0$, desto schmaler der Übergang, aber desto später die Antwort.

:::abbildung et3/k5kausal 2
Betrag des kausal gefensterten Tiefpasses mit $f_\mathrm g=1$ Hz und $t_0=3$ s (blau), gestrichelt das Ideal. An der Kante entsteht ein Übergangsbereich mit $|H_k(f_\mathrm g)|=0{,}49$, davor Wellen bis 1,10.
:::

:::aufgabe Aufgabe 4 ★★ Wie viel Verzögerung kostet die Kausalität?
<span class="anker" id="aufg-4"></span>

Ein Tiefpass mit $f_\mathrm g=1$ kHz soll kausal angenähert werden. Der verschobene ideale Tiefpass soll vor $t=0$, also im abgeschnittenen Teil, unter 1 % seines Maximums liegen.

<ol class="al">

<li>

Wie groß muss $t_0$ mindestens sein?

</li>

<li>

Was bedeutet das für ein Telefongespräch mit einer Kette aus zehn solchen Filtern?

</li>

</ol>

:::loesung
(a) Hüllkurve $\frac{1}{2\pi f_\mathrm g|t|}<0{,}01$ verlangt $|t|>\frac{100}{2\pi f_\mathrm g}=15{,}9$ ms. Also $t_0\approx16$ ms.

(b) Zehn Filter verzögern um etwa 0,16 s. Das merkt man im Gespräch als Verzögerung. Die Kausalität eines steilen Filters kostet Zeit, und zwar umso mehr, je schmaler das Band ist.
:::
:::

---
title: Stufe 1: Die Energiekurve der Bindung
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Chemische Bindung
order: 4150300
summary: Zwei weit entfernte Atome spüren einander nicht, und sehr dicht lassen sie sich nicht zusammendrücken.
tags: freien Energie, Bindungsabstand, Gleichverteilungssatz, thermischen Ausdehnung, Ausdehnungskoeffizient
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Zwei weit entfernte Atome spüren einander nicht, und sehr dicht lassen sie sich nicht zusammendrücken. Diese Stufe zeigt, warum dazwischen ein fester Abstand entsteht und was Wärme daran ändert.
:::

**Die Idee.** Die Bindung entsteht aus der Wechselwirkung der äußeren, teilbesetzten Orbitale. Zwischen zwei Bausteinen (Atomen, Ionen, Molekülen) wirken zwei Kräfte. Die Anziehung reicht weit, ihr Ursprung unterscheidet die Bindungstypen. Die Abstoßung setzt ein, wenn sich die Elektronenhüllen überlappen: Das Pauli-Prinzip verbietet zwei Elektronen denselben Zustand, also müssen welche in höhere Zustände ausweichen, und die Energie steigt steil. Die Summe hat ein Minimum (Abb. [1](#abb-1)). Triebkraft jeder Bindung ist diese Absenkung der potentiellen Energie, genauer der __freien Energie__, die zusätzlich die Unordnung bewertet. Bei vielen Bindungen liegt das Minimum dort, wo die Atome die Edelgaskonfiguration erreichen.

:::abbildung gemb1/k5kurve 1
Links: Kraft und Energie eines Paars. Anziehung (grün) und Abstoßung (orange) ergeben die blaue Kurve. Rechts: Mulde des Ionenpaars K$^+$Cl$^-$. Eine Schwingung liegt um $k_\mathrm BT$ über dem Minimum und reicht von Wand zu Wand (rot). Ihre Mitte (Punkte) wandert mit der Temperatur nach rechts.
:::

:::satz Satz 1.1 (Energiekurve eines Paars)
<span class="anker" id="satz-1-1"></span>

Als Modell gilt für den Abstand $r$

<span class="anker" id="gl-1-1"></span>
$$E_\mathrm{pot}(r)=-\frac{K_\mathrm{an}}{r^{\gamma_\mathrm{an}}}+\frac{K_\mathrm{ab}}{r^{\gamma_\mathrm{ab}}},\qquad\gamma_\mathrm{ab}>\gamma_\mathrm{an}. \tag{1.1}$$

Die Kraft folgt aus dem Energiegefälle, $F=-\mathrm{d} E_\mathrm{pot}/\mathrm{d} r$, allgemein $\boldsymbol F=-\operatorname{grad}E_\mathrm{pot}$. Beim __Bindungsabstand__ $r_0$ herrscht Kräftegleichgewicht, $F_\mathrm{an}=-F_\mathrm{ab}$, und $E_\mathrm{pot}$ hat dort sein Minimum:

<span class="anker" id="gl-1-2"></span>
$$r_0^{\,\gamma_\mathrm{ab}-\gamma_\mathrm{an}}=\frac{\gamma_\mathrm{ab}K_\mathrm{ab}}{\gamma_\mathrm{an}K_\mathrm{an}},\quad E_\mathrm B=-E_\mathrm{pot}(r_0)=\frac{K_\mathrm{an}}{r_0^{\gamma_\mathrm{an}}}\Bigl(1-\frac{\gamma_\mathrm{an}}{\gamma_\mathrm{ab}}\Bigr),\quad D=\frac{\mathrm{d}^2E_\mathrm{pot}}{\mathrm{d} r^2}\bigg|_{r_0}=\frac{\gamma_\mathrm{an}\gamma_\mathrm{ab}E_\mathrm B}{r_0^2}. \tag{1.2}$$
:::

⁠**So liest man das:** $r_0$ ist typisch 0,1 bis 0,4 nm. $K_\mathrm{an},K_\mathrm{ab}>0$ messen die Stärke beider Anteile. $\gamma_\mathrm{an}$ ist 1 für zwei Ionen (Coulomb-Energie, also $F_\mathrm{an}\propto r^{-2}$). $\gamma_\mathrm{ab}$ liegt bei 9 bis 12, manche Rechnungen nehmen statt der Potenz eine Exponentialfunktion. $F>0$ schiebt auseinander, $F<0$ zieht zusammen. $E_\mathrm B>0$ ist die Bindungsenergie, je nach Typ 0,01 bis 10 eV, $D$ die Federkonstante in N/m. **Gültigkeit:** [(1.1)](#gl-1-1) ist ein Modell, der genaue Verlauf der Anziehung verlangt aufwändige quantenmechanische Rechnungen.

:::herleitung Minimum und Federkonstante
$\mathrm{d} E_\mathrm{pot}/\mathrm{d} r=0$ ergibt $\gamma_\mathrm{ab}K_\mathrm{ab}r_0^{-\gamma_\mathrm{ab}}=\gamma_\mathrm{an}K_\mathrm{an}r_0^{-\gamma_\mathrm{an}}$. Die Abstoßung ist am Minimum also der Bruchteil $\gamma_\mathrm{an}/\gamma_\mathrm{ab}$ der Anziehung, das ergibt $E_\mathrm B$. Nochmaliges Ableiten ergibt $D$.
:::

**Beispiel.** K$^+$ und Cl$^-$ mit $K_\mathrm{an}=1{,}44$ eV nm, $\gamma_\mathrm{an}=1$, $\gamma_\mathrm{ab}=9$, $r_0=0{,}267$ nm: Die Coulomb-Energie ist $-5{,}39$ eV, die Abstoßung $+0{,}60$ eV, also $E_\mathrm B=4{,}79$ eV. Bei $0{,}8\,r_0$ beträgt die Abstoßung schon $+4{,}46$ eV. An jedem Ion zieht $F_\mathrm{an}=20{,}2$ eV/nm $=3{,}24$ nN, die Abstoßung hält genau dagegen. $D=605$ eV/nm$^2=97$ N/m. **Grenzfall:** Für $\gamma_\mathrm{ab}\to\infty$ wird die Abstoßung zur harten Wand bei $r_0$, und $E_\mathrm B\to K_\mathrm{an}/r_0^{\gamma_\mathrm{an}}$.

**Was Wärme ändert.** Die Atome schwingen um $r_0$. Nach dem __Gleichverteilungssatz__ hat jede Schwingung im Mittel die thermische Energie $k_\mathrm BT$, die Bewegung liegt also um $k_\mathrm BT$ über dem Minimum und ist durch die Kurve begrenzt. Diese ist links steil und rechts flach. Bei 300 K reicht die Schwingung im Ionenpaar 8,6 pm nach innen und 10,0 pm nach außen, ihre Mitte liegt 0,7 pm oder 0,26 % über $r_0$. Das ist die Ursache der __thermischen Ausdehnung__. Für die Modellkurve gilt $\Delta r/r_0=\frac{\gamma_\mathrm{an}+\gamma_\mathrm{ab}+3}{3\gamma_\mathrm{an}\gamma_\mathrm{ab}}\,k_\mathrm BT/E_\mathrm B$, also der __Ausdehnungskoeffizient__ $\alpha_\mathrm{th}=\Delta r/(r_0T)=8{,}7\cdot10^{-6}$ K$^{-1}$: Schwache Bindungen dehnen sich stärker aus. Mit steigender Temperatur gewinnt die Schwingung gegen die Bindung. Festkörper schmelzen, viele organische Moleküle zersetzen sich, und bei genügend hoher Temperatur werden alle Stoffe oder ihre Zerfallsprodukte gasförmig.

:::frage Am Minimum ist die Kraft null. Ist die Bindung dort nicht am schwächsten?
Nein. $F=0$ heißt Gleichgewicht, nicht fehlender Halt. Zieht man die Atome auseinander, wächst die Rückstellkraft. Wie fest die Bindung hält, sagen $E_\mathrm B$ und $D$. Die größte Haltekraft liegt rechts von $r_0$, wo die Kurve am steilsten steigt.
:::

:::aufgabe Aufgabe 1 ★★ Eine Energiekurve auswerten
<span class="anker" id="aufg-1"></span>

Zwei Moleküle haben $E_\mathrm{pot}(r)=-K_\mathrm{an}/r^6+K_\mathrm{ab}/r^{12}$ mit $K_\mathrm{an}=1{,}2\cdot10^{-3}$ eV nm$^6$, $K_\mathrm{ab}=8{,}0\cdot10^{-7}$ eV nm$^{12}$.

<ol class="al">

<li>

Berechne $r_0$ und $E_\mathrm B$. Zeige, dass hier $E_\mathrm B=K_\mathrm{an}^2/(4K_\mathrm{ab})$ gilt.

</li>

<li>

Berechne $D$ in eV/nm$^2$ und in N/m.

</li>

<li>

Bei welchem Abstand ist die Anziehung am größten, und wie groß ist die Kraft dort in pN?

</li>

<li>

Vorhersage: Hält die Bindung bei 300 K? Vergleiche $k_\mathrm BT$ mit $E_\mathrm B$.

</li>

</ol>

:::loesung
(a) Mit $\gamma_\mathrm{an}=6$, $\gamma_\mathrm{ab}=12$ ist $r_0^6=2K_\mathrm{ab}/K_\mathrm{an}$, also $r_0=0{,}332$ nm. $E_\mathrm B=\frac12K_\mathrm{an}/r_0^6=K_\mathrm{an}^2/(4K_\mathrm{ab})=0{,}450$ eV. (b) $D=72\,E_\mathrm B/r_0^2=294$ eV/nm$^2=47{,}2$ N/m. (c) Die Anziehung ist am größten, wo $\mathrm{d} F/\mathrm{d} r=0$ ist: $r=(13/7)^{1/6}r_0=1{,}109\,r_0=0{,}368$ nm mit $F=-3{,}65$ eV/nm $=-585$ pN. Dort ist die Kurve am steilsten, also rechts vom Minimum. (d) $k_\mathrm BT/E_\mathrm B=0{,}057$. Die Bindung hält, die Schwingung bleibt tief in der Mulde.
:::
:::

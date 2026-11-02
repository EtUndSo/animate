---
title: Stufe 1: Strom aus besetzten Zuständen
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Strom im Halbleiter
order: 4220300
summary: Teil 1 hat den Strom aus einer einzigen mittleren Geschwindigkeit berechnet.
tags: 
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
[Teil 1](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/welle-teilchen-und-schrodinger-gleichung/welle-teilchen-und-schroedinger-gleichung.html) hat den Strom aus einer einzigen mittleren Geschwindigkeit berechnet. Im Kristall hat jeder Zustand seine eigene Geschwindigkeit. Diese Stufe summiert über alle Zustände und zeigt, wann die Summe null ist und wann nicht.
:::

**Die Idee.** Ein Elektron im Zustand $k$ ist eine Welle, die über die ganze Kette reicht. Seine Ladung $-e$ verteilt sich auf die Länge $L$ und wandert mit der Geschwindigkeit $v(k)$. Das ergibt einen kleinen Strombeitrag, und der Gesamtstrom ist die Summe aller Beiträge. Zu jedem Zustand $k$ gehört ein Partner $-k$ mit gleicher Energie und entgegengesetzter Geschwindigkeit. Sind beide gleich wahrscheinlich besetzt, heben sie sich auf. Strom verlangt also nicht viele Elektronen, sondern eine Schieflage der Besetzung.

:::satz Satz 1.1 (Stromdichte aus den Zuständen)
<span class="anker" id="satz-1-1"></span>

Ein Elektron im Zustand $\phi_k(x)=\mathrm{e}^{\mathrm{j} kx}/\sqrt L$ trägt $j_k=-e\,|\phi_k(x)|^2\,v(k)$. Alle Zustände zusammen, jeder mit seiner Besetzung $f(k)$, tragen

<span class="anker" id="gl-1-1"></span>
$$j=-\frac eL\sum_kv(k)\,f(k),\qquad v(k)=\frac1\hbar\frac{\partial E}{\partial k}. \tag{1.1}$$
:::

⁠**So liest man das:** $-e|\phi_k|^2=-e/L$ ist die Ladung je Länge, mal Geschwindigkeit ergibt das einen Strom in A. In drei Dimensionen steht $L^3$ statt $L$, und $j$ hat die Einheit A/m$^2$. Die Summe läuft über alle Plätze, jedes $k$ zählt wegen des Spins zweimal. Im Gleichgewicht ist $f(k)$ die Fermi-Verteilung mit $E=E(k)$, nahe der Bandkante mit $E(k)=\hbar^2k^2/(2m^*)+V_0$. Ein Elektron der Kette mit $v=3{,}8\cdot10^5$ m/s trägt bei $L=1$ µ m den Strom 61 nA. **Gültigkeit:** Im Kristall schwankt $|\psi|^2$ innerhalb der Zelle, sein Mittel bleibt aber $1/L$, und das Paket läuft mit $v(k)$.

:::herleitung Gleichgewicht und volles Band
⁠**Gleichgewicht.** $f$ hängt nur von der Energie ab, und es ist $E(-k)=E(k)$, denn zu jeder Lösung gehört ihre konjugiert komplexe mit gleicher Energie. Die Ableitung einer geraden Funktion ist ungerade: $v(-k)=-v(k)$. In [(1.1)](#gl-1-1) heben sich die Paare auf, $v(k)f(k)+v(-k)f(-k)=0$, bei jeder Temperatur.

⁠**Volles Band.** Mit $f=1$ wird die Summe zum Integral über die Zone:

$$\sum_kv(k)=2\,\frac L{2\pi}\int_{-\pi/a}^{\pi/a}\frac1\hbar\frac{\partial E}{\partial k}\,\mathrm{d} k=\frac L{\pi\hbar}\Bigl[E(\pi/a)-E(-\pi/a)\Bigr]=0,$$

weil $E(k)$ periodisch ist. Das gilt auch unter einer Kraft: Wer bei $\pi/a$ die Zone verlässt, tritt bei $-\pi/a$ wieder ein, jeder Platz bleibt besetzt. Volle Bänder tragen also nicht zum Strom bei. Bei $T=0$ fließt im Halbleiter nichts, obwohl fast alle Elektronen vorhanden sind.
:::

**Die Kraft verschiebt die Besetzung.** Eine Kraft, etwa $F=-e\mathcal E$ im Feld, ändert den Wellenvektor jedes Elektrons:

<span class="anker" id="gl-1-2"></span>
$$k(t>0)=k(0)+\frac F\hbar\,t. \tag{1.2}$$

Alle Elektronen rutschen um dasselbe $\delta k=Ft/\hbar$ (Abb. [1](#abb-1)). Im Leitungsband sitzen dann mehr Elektronen bei $k>0$, dort ist $v>0$, also $j<0$. Im Valenzband rutschen die Elektronen mit, also wandern auch die leeren Plätze zu $k>0$. Dort fällt das Band, $v<0$. Das volle Band trägt keinen Strom, es bleiben die fehlenden Elektronen:

<span class="anker" id="gl-1-3"></span>
$$j_\mathrm V=-\frac eL\Bigl(\sum_\text{alle}v-\sum_\text{leer}v\Bigr)=+\frac eL\sum_\text{leer}v(k)<0. \tag{1.3}$$

Beide Bänder tragen mit demselben Vorzeichen bei, ihre Ströme addieren sich.

:::abbildung gemb1/k12besetzung 1
Kosinus-Bänder mit wenigen Plätzen, blau besetzt, rot umrandet leer. Links symmetrisch, $j=0$. Rechts hat eine Kraft $F>0$ alles um zwei Plätze geschoben. Elektronen mit $v>0$ und fehlende Elektronen mit $v<0$ geben beide $j<0$.
:::

**Beispiel.** Nahe der Unterkante ist $v=\hbar k/m^*$. Nach der Verschiebung hat jedes Elektron im Mittel $\Delta v=\hbar\,\delta k/m^*$ dazubekommen, und [(1.1)](#gl-1-1) wird mit $n=N_\mathrm e/L$ zu

<span class="anker" id="gl-1-4"></span>
$$j=-e\,n\,\frac{\hbar\,\delta k}{m^*}. \tag{1.4}$$

Bei $\mathcal E=10^4$ V/m wächst $\delta k$ in 1 ps auf $0{,}0152\,\mathrm{nm^{-1}}$, das sind 0,12 % des Wegs zum Zonenrand, und in der Kette ist $\Delta v=1440$ m/s. **Grenzfälle:** Für $F=0$ ist $j=0$. Ein leeres Band trägt nichts.

:::aufgabe Aufgabe 1 ★★ Die Summe von Hand
<span class="anker" id="aufg-1"></span>

Eine Kette aus 8 Zellen ($a=0{,}25$ nm, $t_0=0{,}5$ eV) hat die Zustände $k_na=n\pi/4$ mit $n=-3,\dots,4$. Zähle jeden Zustand einmal.

<ol class="al">

<li>

Berechne $v(k_n)/v_\text{max}$ und den Vorfaktor $e\,v_\text{max}/L$.

</li>

<li>

Besetzt sind $n=-1,0,1$. Eine Kraft schiebt die Besetzung Schritt für Schritt auf $n=0,1,2$, dann $1,2,3$, dann $2,3,4$, dann $3,4,-3$. Berechne $j$ jeweils. Was fällt dir auf?

</li>

<li>

Vorhersage: Alle Zustände sind besetzt, nur $n=2$ fehlt. Wie groß ist $j$, und welches Teilchen trägt ihn?

</li>

</ol>

:::loesung
(a) $v/v_\text{max}=\sin(n\pi/4)$: $-0{,}707;\,-1;\,-0{,}707;\,0;\,0{,}707;\,1;\,0{,}707;\,0$. Mit $v_\text{max}=3{,}80\cdot10^5$ m/s und $L=2$ nm ist $e\,v_\text{max}/L=30{,}4$ µ A. (b) $n=-1,0,1$: Summe 0, $j=0$. $n=0,1,2$: Summe 1,707, $j=-51{,}9$ µ A. $n=1,2,3$: Summe 2,414, $j=-73{,}5$ µ A. $n=2,3,4$: wieder $-51{,}9$ µ A. $n=3,4,-3$: Summe 0, $j=0$. Der Strom wächst und verschwindet wieder, obwohl die Kraft gleich bleibt: Jenseits von $ka=\pi/2$ werden die Elektronen langsamer. (c) Die Summe aller acht ist null, ohne $n=2$ also $-1$, und $j=+30{,}4$ µ A. Das ist nach [(1.3)](#gl-1-3) der Strom eines Lochs mit $+e$.
:::
:::

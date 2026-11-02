---
title: Stufe 8: Die diskrete Fourier-Transformation (DFT)
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / Abtastung und zeitdiskrete Systeme
order: 3240900
summary: S mathrm a(f) ist eine stetige Funktion, ein Rechner braucht aber endlich viele Zahlen.
tags: 
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
$S_\mathrm a(f)$ ist eine stetige Funktion, ein Rechner braucht aber endlich viele Zahlen. Für eine Folge endlicher Länge genügen endlich viele Abtastwerte des Spektrums.
:::

**Die Idee.** Ist $s(n)$ auf $M$ Werte begrenzt, genügen nach Stufe [4](abtastung-im-frequenzbereich.html#stufe-4) Abtastwerte des Spektrums im Abstand $F=1/M$. Dazu gehört das mit $M$ periodisch wiederholte Signal $s_d(n)$. Weil auch das Spektrum periodisch ist (Zeit diskret), reichen $M$ Spektralwerte. Beide Seiten sind jetzt diskret und periodisch.

:::satz Satz 8.1 (Diskrete Fourier-Transformation)
<span class="anker" id="satz-8-1"></span>

<span class="anker" id="gl-8-1"></span>
$$S_d(k)=\sum_{n=0}^{M-1}s_d(n)\,\mathrm{e}^{-\mathrm{j}2\pi kn/M},\qquad s_d(n)=\frac1M\sum_{k=0}^{M-1}S_d(k)\,\mathrm{e}^{\mathrm{j}2\pi kn/M},\qquad k,n=0,\dots,M-1. \tag{8.1}$$
:::

⁠**So liest man das:** $S_d(k)$ ist der Wert des Spektrums $S_\mathrm a(f)$ bei $f=k/M$. Der Index $k$ zählt Schwingungen, die in die $M$ Werte genau $k$-mal passen. Die Rücktransformation ist eine Fourier-Reihe mit $M$ Gliedern. Die Theoreme gelten sinngemäß, etwa die Verschiebung $s_d(n-m)\;\circ\!\!-\!\!\bullet\;S_d(k)\mathrm{e}^{-\mathrm{j}2\pi mk/M}$ (zyklisch: Was hinten herausgeschoben wird, kommt vorne wieder herein) und Parseval $\sum_n|s_d(n)|^2=\frac1M\sum_k|S_d(k)|^2$.

**Beispiel.** $s_d=(1,\,2,\,0,\,-1)$, $M=4$, $\mathrm{e}^{-\mathrm{j}2\pi/4}=-\mathrm{j}$:

$$S_d(k)=\sum_{n=0}^{3}s_d(n)(-\mathrm{j})^{kn}:\qquad S_d(0)=2,\quad S_d(1)=1-3\mathrm{j},\quad S_d(2)=0,\quad S_d(3)=1+3\mathrm{j}.$$

Probe: $S_d(3)=S_d^*(1)$, weil das Signal reell ist ($k=3$ entspricht $k=-1$). Parseval: $1+4+0+1=6=\frac14(4+10+0+10)$.

:::aufgabe Aufgabe 8 ★★ DFT von Hand
<span class="anker" id="aufg-8"></span>

<ol class="al">

<li>

Rechne $S_d(1)$ für $s_d=(1,2,0,-1)$ nach.

</li>

<li>

Bestimme mit dem Verschiebungssatz die DFT der zyklisch verschobenen Folge $(-1,1,2,0)$ und prüfe $S_d(1)$ direkt.

</li>

</ol>

:::loesung
(a) $S_d(1)=1+2(-\mathrm{j})+0\cdot(-1)+(-1)(-\mathrm{j})^3=1-2\mathrm{j}-\mathrm{j}=1-3\mathrm{j}$, weil $(-\mathrm{j})^3=\mathrm{j}$.

(b) Verschiebung um $m=1$: $S_d(k)\,(-\mathrm{j})^k$, also $(2,\;(1-3\mathrm{j})(-\mathrm{j}),\;0,\;(1+3\mathrm{j})\mathrm{j})=(2,\;-3-\mathrm{j},\;0,\;-3+\mathrm{j})$. Direkt: $S_d(1)=-1+1\cdot(-\mathrm{j})+2\cdot(-1)+0=-3-\mathrm{j}$.
:::
:::

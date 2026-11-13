---
title: Stufe 8: Die diskrete Fourier-Transformation (DFT)
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Abtastung und zeitdiskrete Systeme
adresse: elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme
knoten: Kapitel 4: Abtastung und zeitdiskrete Systeme
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

::::beispiel
$s_d=(1,\,2,\,0,\,-1)$, $M=4$, $\mathrm{e}^{-\mathrm{j}2\pi/4}=-\mathrm{j}$:

$$S_d(k)=\sum_{n=0}^{3}s_d(n)(-\mathrm{j})^{kn}:\qquad S_d(0)=2,\quad S_d(1)=1-3\mathrm{j},\quad S_d(2)=0,\quad S_d(3)=1+3\mathrm{j}.$$

Probe: $S_d(3)=S_d^*(1)$, weil das Signal reell ist ($k=3$ entspricht $k=-1$). Parseval: $1+4+0+1=6=\frac14(4+10+0+10)$.
::::

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

::::formelsammlung
**Diskrete Fourier-Transformation**

$$S_d(k)=\sum_{n=0}^{M-1}s_d(n)\,\mathrm{e}^{-\mathrm{j}2\pi kn/M},\qquad s_d(n)=\frac1M\sum_{k=0}^{M-1}S_d(k)\,\mathrm{e}^{\mathrm{j}2\pi kn/M}$$

$k,n=0,\dots,M-1$; $s_d$ ist die mit $M$ periodisch wiederholte, auf $M$ Werte begrenzte Folge. $S_d(k)$ ist der Wert von $S_\mathrm a(f)$ bei $f=k/M$; beide Seiten sind diskret und periodisch.

**Verschiebungssatz der DFT**

$$s_d(n-m)\;\circ\!\!-\!\!\bullet\;S_d(k)\mathrm{e}^{-\mathrm{j}2\pi mk/M}$$

Zyklisch: Was hinten herausgeschoben wird, kommt vorne wieder herein.

**Parseval für die DFT**

$$\sum_n|s_d(n)|^2=\frac1M\sum_k|S_d(k)|^2$$

Summen über eine Periode.
::::

::::lernkarten
:::karte zusammenhang Endlich viele Spektralwerte
Warum genügen für eine auf $M$ Werte begrenzte Folge $M$ Werte ihres Spektrums?
---
Bei einer auf $M$ Werte begrenzten Folge genügen Spektralwerte im Abstand $F=1/M$; dazu gehört die mit $M$ periodisch wiederholte Folge $s_d(n)$. Weil das Spektrum zudem periodisch mit 1 ist, liegen in einer Periode genau $M$ Werte.
--- falsch
Weil eine Folge mit $M$ Werten nur die Frequenzen $0$ bis $M$ enthalten kann. Darüber ist das Spektrum null, und $M$ Werte im Abstand 1 decken den ganzen Bereich der vorkommenden Frequenzen lückenlos ab.
--- falsch
Weil das Spektrum zwischen den Werten bei $k/M$ linear verläuft. Man kann es deshalb aus $M$ Stützstellen durch Geraden exakt ergänzen, ohne dabei Information zu verlieren.
--- falsch
Sie genügen nicht exakt, sondern nur näherungsweise. Je größer $M$ ist, desto feiner wird das Raster der Spektralwerte, und erst für unendlich großes $M$ verschwindet der Fehler der Darstellung ganz, wie bei jeder Abtastung.
:::
:::karte formel Diskrete Fourier-Transformation
Wie lauten die diskrete Fourier-Transformation (DFT) einer mit $M$ periodischen Folge $s_d(n)$ und ihre Rücktransformation?
---
$S_d(k)=\sum_{n=0}^{M-1}s_d(n)\,\mathrm{e}^{-\mathrm{j}2\pi kn/M}$ und $s_d(n)=\frac1M\sum_{k=0}^{M-1}S_d(k)\,\mathrm{e}^{\mathrm{j}2\pi kn/M}$ für $k,n=0,\dots,M-1$. Beide Seiten sind diskret und periodisch mit $M$; die Rücktransformation ist eine Fourier-Reihe mit $M$ Gliedern.
--- falsch
$S_d(k)=\sum_{n=0}^{M-1}s_d(n)\,\mathrm{e}^{-\mathrm{j}2\pi kn/M}$ und $s_d(n)=\sum_{k=0}^{M-1}S_d(k)\,\mathrm{e}^{\mathrm{j}2\pi kn/M}$ ohne Vorfaktor, weil Hin- und Rücktransformation symmetrisch sind. Beide Seiten sind diskret.
--- falsch
$S_d(k)=\sum_{n=-\infty}^{\infty}s_d(n)\,\mathrm{e}^{-\mathrm{j}2\pi kn/M}$ und $s_d(n)=\int_{-1/2}^{1/2}S_\mathrm a(f)\,\mathrm{e}^{\mathrm{j}2\pi nf}\,\mathrm{d} f$. Die Hintransformation ist diskret, die Rücktransformation bleibt dagegen ein Integral über eine ganze Periode des Spektrums.
--- falsch
$S_d(k)=\sum_{n=0}^{M-1}s_d(n)\,\mathrm{e}^{-\mathrm{j}2\pi kn/M}$ und $s_d(n)=\frac1M\sum_{k=0}^{M-1}S_d(k)\,\mathrm{e}^{\mathrm{j}2\pi kn/M}$, aber nur für $k=0,\dots,M/2$. Die übrigen Werte von $S_d(k)$ sind null, weil Frequenzen über der halben Abtastrate fehlen.
:::
:::karte zusammenhang Bedeutung der DFT-Werte
Was bedeutet der DFT-Wert $S_d(k)$, und was zählt der Index $k$?
---
$S_d(k)$ ist der Wert des Spektrums $S_\mathrm a(f)$ der begrenzten Folge bei $f=k/M$. Der Index $k$ zählt Schwingungen, die in die $M$ Werte genau $k$-mal passen.
--- falsch
$S_d(k)$ ist der Mittelwert des Spektrums $S_\mathrm a(f)$ zwischen den Frequenzen $k/M$ und $(k+1)/M$. Der Index $k$ zählt die Abtastwerte der Folge, beginnend bei null.
--- falsch
$S_d(k)$ ist der Wert des Spektrums bei der Frequenz $f=k$ in Hertz. Der Index $k$ zählt Schwingungen, die in eine Sekunde genau $k$-mal passen, unabhängig von der Länge $M$.
--- falsch
$S_d(k)$ ist der $k$-te Abtastwert der Folge, mit dem Faktor $M$ gewichtet. Der Index $k$ zählt Zeitpunkte, und erst die Rücktransformation macht daraus das Spektrum der Folge.
:::
:::karte formel Verschiebungssatz der DFT
Was wird aus der DFT, wenn man die Folge $s_d(n)$ um $m$ Stellen verschiebt, und warum heißt diese Verschiebung zyklisch?
---
$s_d(n-m)\;\circ\!\!-\!\!\bullet\;S_d(k)\mathrm{e}^{-\mathrm{j}2\pi mk/M}$: Jeder Wert wird mit einer Phasendrehung multipliziert, sein Betrag bleibt. Zyklisch heißt: Was hinten herausgeschoben wird, kommt vorne wieder herein, weil $s_d$ periodisch mit $M$ ist.
--- falsch
$s_d(n-m)\;\circ\!\!-\!\!\bullet\;S_d(k-m)$: Das Spektrum wird ebenfalls um $m$ Stellen verschoben. Zyklisch heißt: Was hinten herausgeschoben wird, kommt vorne wieder herein, weil $S_d$ periodisch mit $M$ ist.
--- falsch
$s_d(n-m)\;\circ\!\!-\!\!\bullet\;S_d(k)\mathrm{e}^{-\mathrm{j}2\pi mk/M}$: Jeder Wert wird mit einer Phasendrehung multipliziert. Zyklisch heißt: Die herausgeschobenen Werte gehen verloren und werden vorne durch Nullen ersetzt, wie bei jeder Verzögerung.
--- falsch
$s_d(n-m)\;\circ\!\!-\!\!\bullet\;S_d(k)\mathrm{e}^{\mathrm{j}2\pi mk}$: Jeder Wert wird mit einem Faktor multipliziert, der stets 1 ist; die DFT ändert sich also nicht. Zyklisch heißt: Die Folge dreht sich im Kreis, ohne dass man es am Spektrum sieht.
:::
:::karte formel Parseval für die DFT
Wie hängt die Summe der Betragsquadrate einer Folge $s_d(n)$ mit ihren DFT-Werten $S_d(k)$ zusammen?
---
$\sum_n|s_d(n)|^2=\frac1M\sum_k|S_d(k)|^2$. Im Beispiel $s_d=(1,\,2,\,0,\,-1)$ ist die linke Seite $1+4+0+1=6$, die rechte $\frac14(4+10+0+10)$, ebenfalls 6. Bis auf den Faktor $1/M$ bleibt die Summe der Betragsquadrate also erhalten.
--- falsch
$\sum_n|s_d(n)|^2=\sum_k|S_d(k)|^2$ ohne Faktor. Im Beispiel $s_d=(1,\,2,\,0,\,-1)$ sind beide Seiten 6, weil die DFT die Summe der Betragsquadrate unverändert überträgt.
--- falsch
$\sum_n|s_d(n)|^2=M\sum_k|S_d(k)|^2$. Die DFT verteilt die Summe der Betragsquadrate auf $M$ Spektralwerte, deshalb muss man die rechte Seite mit $M$ multiplizieren, damit beide Seiten übereinstimmen.
--- falsch
$\sum_n|s_d(n)|=\frac1M\sum_k|S_d(k)|$, also für die Beträge selbst, nicht für ihre Quadrate. Im Beispiel $s_d=(1,\,2,\,0,\,-1)$ ist die linke Seite 4, und die rechte ist ebenfalls 4.
:::
:::karte zusammenhang DFT reeller Folgen
Warum ist bei der Folge $s_d=(1,\,2,\,0,\,-1)$ mit $M=4$ der Wert $S_d(3)$ der konjugiert komplexe Wert von $S_d(1)$?
---
Die Folge ist reell, deshalb gehören zu $k$ und $-k$ konjugiert komplexe Werte. Die DFT ist periodisch mit $M=4$, also entspricht $k=3$ dem Wert $k=-1$, und es gilt $S_d(3)=S_d^*(1)$, hier $1+3\mathrm{j}$ und $1-3\mathrm{j}$.
--- falsch
Weil die Folge symmetrisch ist, ihr erster Wert also gleich ihrem letzten. Bei symmetrischen Folgen sind gegenüberliegende DFT-Werte zueinander konjugiert, bei allen anderen Folgen nicht.
--- falsch
Weil $S_d(2)=0$ ist und die Werte links und rechts einer Nullstelle stets konjugiert komplex sind. Ohne die Nullstelle bei $k=2$ wären $S_d(1)$ und $S_d(3)$ unabhängig voneinander.
--- falsch
Das ist Zufall dieses Beispiels: Die Summe $S_d(1)+S_d(3)$ ist reell, weil die Werte der Folge zusammen 2 ergeben. Bei einer anderen reellen Folge wären die beiden Werte unabhängig voneinander.
:::
::::

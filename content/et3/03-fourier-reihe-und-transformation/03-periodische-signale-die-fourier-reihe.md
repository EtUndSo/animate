---
title: Stufe 2: Periodische Signale, die Fourier-Reihe
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Fourier-Reihe und -Transformation
adresse: elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation
knoten: Kapitel 3: Fourier-Reihe und -Transformation
order: 3230300
summary: Ein periodisches Signal wiederholt sich nach T .
tags: Grundfrequenz, Harmonischen, Fourier-Reihe, Gleichanteil, orthogonal
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Ein periodisches Signal wiederholt sich nach $T$. Es lässt sich aus Schwingungen zusammensetzen, aber nur aus ganz bestimmten. Diese Stufe zeigt, aus welchen, und wie man ihre Gewichte findet.
:::

**Die Idee.** Eine Schwingung $\mathrm{e}^{\mathrm{j}2\pi ft}$ wiederholt sich nach $T$ genau dann, wenn $fT$ eine ganze Zahl ist. Also kommen in einem Signal mit der Periode $T$ nur die Frequenzen $f_k=kF$ mit der __Grundfrequenz__ $F=1/T$ vor, die __Harmonischen__:

<span class="anker" id="gl-2-1"></span>
$$s_p(t)=\sum_{k=-\infty}^{\infty}S_p(k)\,\mathrm{e}^{\mathrm{j}2\pi kFt}. \tag{2.1}$$

Das ist die __Fourier-Reihe__ (Synthese). $S_p(k)$ ist das komplexe Gewicht der $k$-ten Harmonischen.

**Reelle Signale.** Für ein reelles Signal gilt $s_p=s_p^*$. Konjugiert man [(2.1)](#gl-2-1), wird aus $\mathrm{e}^{\mathrm{j}2\pi kFt}$ die Schwingung mit $-k$. Der Vergleich der Koeffizienten ergibt

$$S_p(-k)=S_p^*(k).$$

Jedes Paar $k,-k$ ergibt dann $2\operatorname{Re}\{S_p(k)\mathrm{e}^{\mathrm{j}2\pi kFt}\}$, eine reelle Kosinusschwingung. Mit $S_p(k)=|S_p(k)|\,\mathrm{e}^{\mathrm{j}\varphi_p(k)}$:

<span class="anker" id="gl-2-2"></span>
<span class="anker" id="gl-2-3"></span>
$$\begin{aligned} s_p(t)&=S_p(0)+2\sum_{k=1}^{\infty}|S_p(k)|\cos\bigl(2\pi kFt+\varphi_p(k)\bigr)\\ &=S_p(0)+2\sum_{k=1}^{\infty}\Bigl[\operatorname{Re}\{S_p(k)\}\cos(2\pi kFt)-\operatorname{Im}\{S_p(k)\}\sin(2\pi kFt)\Bigr]. \end{aligned} \tag{2.2|2.3}$$

Die Phase $\varphi_p(k)$ bestimmt man wie bei jeder komplexen Zahl mit $\arctan$ und der Quadrantenkorrektur ($+\pi$ bei negativem Realteil). $S_p(0)$ ist der __Gleichanteil__, der Mittelwert des Signals.

**Die Gewichte finden: Orthogonalität.** Wie holt man ein einzelnes $S_p(n)$ aus der Summe heraus? Man multipliziert mit $\mathrm{e}^{-\mathrm{j}2\pi nFt}$ und mittelt über eine Periode. Dabei verschwinden alle anderen Harmonischen:

<span class="anker" id="gl-2-4"></span>
$$\frac1T\int_0^T\mathrm{e}^{\mathrm{j}2\pi(k-n)Ft}\,\mathrm{d} t=\begin{cases}1&k=n\\0&k\neq n\end{cases}. \tag{2.4}$$

Für $k\neq n$ dreht sich der Zeiger $\mathrm{e}^{\mathrm{j}2\pi(k-n)Ft}$ in der Periode genau $|k-n|$-mal ganz herum, und sein Mittelwert ist null. Für $k=n$ steht er still. Schwingungen verschiedener Frequenz heißen deshalb __orthogonal__. Es bleibt:

:::satz Satz 2.1 (Fourier-Reihe)
<span class="anker" id="satz-2-1"></span>

Ein Signal mit der Periode $T=1/F$ und endlicher Leistung (der Mittelwert von $|s(t)|^2$ über eine Periode ist endlich) hat die Darstellung [(2.1)](#gl-2-1) mit

<span class="anker" id="gl-2-5"></span>
$$S_p(k)=\frac1T\int_{t_1}^{t_1+T}s_p(t)\,\mathrm{e}^{-\mathrm{j}2\pi kFt}\,\mathrm{d} t, \tag{2.5}$$

wobei $t_1$ beliebig ist (Analyse). Das Gleichheitszeichen in [(2.1)](#gl-2-1) gilt im quadratischen Mittel: Der Mittelwert von $\bigl|s_p(t)-\sum_{|k|\le N}S_p(k)\,\mathrm{e}^{\mathrm{j}2\pi kFt}\bigr|^2$ über eine Periode, die Leistung des Fehlers, geht für $N\to\infty$ gegen null. In einzelnen Punkten, etwa an Sprungstellen, muss die Reihe nicht den Signalwert liefern.
:::

⁠**So liest man das:** $S_p(k)$ ist der Mittelwert des Signals, nachdem man es mit der $k$-ten Harmonischen „entgegengedreht“ hat. Steckt die Harmonische im Signal, dreht sich der Zeiger an dieser Stelle nicht mehr, und ihr Anteil bleibt im Mittel übrig. $S_p(0)$ ist einfach der Mittelwert.

:::herleitung Analyseformel
[(2.1)](#gl-2-1) mit $\mathrm{e}^{-\mathrm{j}2\pi nFt}$ multiplizieren, über eine Periode integrieren, Summe und Integral vertauschen:

$$\int_0^Ts_p(t)\mathrm{e}^{-\mathrm{j}2\pi nFt}\mathrm{d} t=\sum_kS_p(k)\int_0^T\mathrm{e}^{\mathrm{j}2\pi(k-n)Ft}\mathrm{d} t=S_p(n)\,T.$$

Für $k\neq n$ ist das Integral $\frac{\mathrm{e}^{\mathrm{j}2\pi(k-n)FT}-1}{\mathrm{j}2\pi(k-n)F}=0$, weil $\mathrm{e}^{\mathrm{j}2\pi(k-n)}=1$. Da der Integrand die Periode $T$ hat, darf man über jedes Intervall der Länge $T$ integrieren.
:::

::::beispiel eine endliche Reihe
$s_p(t)=1+2\cos(2\pi Ft)+\sin(4\pi Ft)$. Mit den Euler-Formeln liest man die Koeffizienten ab, ohne zu integrieren:

$$2\cos(2\pi Ft)=\mathrm{e}^{\mathrm{j}2\pi Ft}+\mathrm{e}^{-\mathrm{j}2\pi Ft},\qquad\sin(4\pi Ft)=\frac{1}{2\mathrm{j}}\mathrm{e}^{\mathrm{j}4\pi Ft}-\frac{1}{2\mathrm{j}}\mathrm{e}^{-\mathrm{j}4\pi Ft},$$

also $S_p(0)=1$, $S_p(\pm1)=1$, $S_p(2)=-\tfrac{\mathrm{j}}{2}$, $S_p(-2)=\tfrac{\mathrm{j}}{2}$, alle anderen null. Probe: $S_p(-2)=S_p^*(2)$.
::::

::::beispiel die Rechteckschwingung
Für das Rechenmodell (1 für $|t|\le T_1/2$ mit $T_1=T/2$):

<span class="anker" id="gl-2-6"></span>
$$S_p(0)=\frac{T_1}{T},\qquad S_p(k)=\frac1T\int_{-T_1/2}^{T_1/2}\mathrm{e}^{-\mathrm{j}2\pi kFt}\mathrm{d} t=\frac{\sin(\pi kT_1/T)}{\pi k}\quad(k\neq0). \tag{2.6}$$

Mit $T_1=T/2$: $S_p(0)=0{,}5$, $S_p(\pm1)=1/\pi=0{,}318$, $S_p(\pm2)=0$, $S_p(\pm3)=-0{,}106$, $S_p(\pm5)=0{,}064$. Die geraden Harmonischen fehlen, weil $\sin(\pi k/2)=0$ für gerade $k$. Alle Koeffizienten sind reell, weil das Signal gerade ist, $s(-t)=s(t)$: Der Imaginärteil von $S_p(k)$ ist $-\frac1T\int_{-T/2}^{T/2}s(t)\sin(2\pi kFt)\,\mathrm{d} t$ und verschwindet, denn der Integrand ist ungerade: Er wechselt bei $t\to-t$ das Vorzeichen, und die Beiträge links und rechts von null heben sich auf. Abbildung [1](#abb-1) zeigt sie für zwei Tastgrade: Je schmaler der Impuls, desto langsamer fallen die Koeffizienten ab.

:::abbildung et3/k3koeff 1
Fourier-Koeffizienten der Rechteckschwingung (0/1) für zwei Impulsbreiten. Gestrichelt die Hüllkurve $\frac{T_1}{T}\operatorname{si}(\pi kT_1/T)$. Bei $T_1=T/2$ fehlen die geraden Harmonischen, bei $T_1=T/4$ jede vierte.
:::
::::

:::frage Warum kommen in einem periodischen Signal keine Frequenzen zwischen den Harmonischen vor?
Weil jede Schwingung in der Summe selbst die Periode $T$ haben muss, sonst wäre die Summe nicht periodisch. Eine Schwingung mit $f=1{,}5F$ hat nach $T$ erst anderthalb Umdrehungen gemacht und steht anders als am Anfang. Kein noch so geschicktes Gewicht kann das ausgleichen, denn verschiedene Frequenzen sind orthogonal und können sich nicht gegenseitig aufheben.
:::

:::aufgabe Aufgabe 1 ★ Koeffizienten ablesen
<span class="anker" id="aufg-1"></span>

$s_p(t)=\frac12+\cos\bigl(2\pi Ft+\frac\pi3\bigr)+\frac12\sin(6\pi Ft)$.

<ol class="al">

<li>

Bestimme alle $S_p(k)$ mit den Euler-Formeln. Prüfe $S_p(-k)=S_p^*(k)$.

</li>

<li>

Gib $|S_p(1)|$ und $\varphi_p(1)$ an und vergleiche mit [(2.2)](#gl-2-2).

</li>

</ol>

:::loesung
(a) $\cos(x+\frac\pi3)=\frac12\mathrm{e}^{\mathrm{j}\pi/3}\mathrm{e}^{\mathrm{j} x}+\frac12\mathrm{e}^{-\mathrm{j}\pi/3}\mathrm{e}^{-\mathrm{j} x}$ und $\frac12\sin(3x)=\frac{1}{4\mathrm{j}}\mathrm{e}^{\mathrm{j}3x}-\frac{1}{4\mathrm{j}}\mathrm{e}^{-\mathrm{j}3x}$ mit $x=2\pi Ft$:

$$S_p(0)=\tfrac12,\quad S_p(\pm1)=\tfrac12\mathrm{e}^{\pm\mathrm{j}\pi/3}=0{,}25\pm0{,}433\mathrm{j},\quad S_p(3)=-\tfrac{\mathrm{j}}{4},\quad S_p(-3)=\tfrac{\mathrm{j}}{4},$$

alle anderen null. $S_p(-1)=S_p^*(1)$ und $S_p(-3)=S_p^*(3)$ stimmen.

(b) $|S_p(1)|=\frac12$, $\varphi_p(1)=60^\circ$. In [(2.2)](#gl-2-2): $2\cdot\frac12\cos(2\pi Ft+60^\circ)$, genau der Kosinusterm des Signals. (Leistung nach Parseval: $\frac14+2\cdot\frac14+2\cdot\frac1{16}=0{,}875$.)
:::
:::

:::aufgabe Aufgabe 2 ★★ Die schmale Rechteckschwingung
<span class="anker" id="aufg-2"></span>

Rechteckschwingung mit $T_1=T/4$.

<ol class="al">

<li>

Berechne $S_p(0)$, $S_p(1)$, $S_p(2)$ und $S_p(4)$ aus [(2.6)](#gl-2-6).

</li>

<li>

Warum ist $S_p(4)=0$? Deute es mit der Orthogonalität: Wie viele Perioden der vierten Harmonischen passen in den Impuls?

</li>

</ol>

:::loesung
(a) $S_p(0)=\frac14$, $S_p(1)=\frac{\sin(\pi/4)}{\pi}=0{,}225$, $S_p(2)=\frac{\sin(\pi/2)}{2\pi}=0{,}159$, $S_p(4)=\frac{\sin\pi}{4\pi}=0$.

(b) Die vierte Harmonische hat die Periode $T/4$, genau die Impulsbreite. Die Analyseformel integriert $\mathrm{e}^{-\mathrm{j}2\pi4Ft}$ über den Impuls, also über genau eine volle Umdrehung des Zeigers. Der Mittelwert ist null. Allgemein verschwindet $S_p(k)$, wenn eine ganze Zahl von Perioden der $k$-ten Harmonischen in den Impuls passt.
:::
:::

::::kurzfassung
Ein periodisches Signal lässt sich aus Schwingungen zusammensetzen, aber nur aus solchen, deren Frequenz ein ganzzahliges Vielfaches einer Grundfrequenz ist. Ihre Gewichte findet man durch Mitteln über eine Periode.

Das Signal $s_p(t)$ wiederhole sich nach der Periode $T$. Die __Grundfrequenz__ ist $F=1/T$, die __Harmonischen__ sind die Schwingungen mit den Frequenzen $f_k=kF$. Die __Fourier-Reihe__ setzt das Signal aus ihnen zusammen (Synthese), die Analyseformel liefert die komplexen Gewichte $S_p(k)$:

$$s_p(t)=\sum_{k=-\infty}^{\infty}S_p(k)\,\mathrm{e}^{\mathrm{j}2\pi kFt},\qquad S_p(k)=\frac1T\int_{t_1}^{t_1+T}s_p(t)\,\mathrm{e}^{-\mathrm{j}2\pi kFt}\,\mathrm{d} t.$$

Das gilt für Signale mit endlicher Leistung, bei denen also der Mittelwert von $|s_p(t)|^2$ über eine Periode endlich ist; $t_1$ ist beliebig. $S_p(0)$ ist der __Gleichanteil__, der Mittelwert des Signals. Für reelle Signale gilt $S_p(-k)=S_p^*(k)$. Jedes Paar $k,-k$ ergibt dann eine reelle Kosinusschwingung mit der Amplitude $2|S_p(k)|$ und der Phase $\varphi_p(k)$.

Der Grund: Eine Schwingung $\mathrm{e}^{\mathrm{j}2\pi ft}$ hat die Periode $T$ genau dann, wenn $fT$ ganzzahlig ist. Um ein Gewicht herauszuholen, multipliziert man mit $\mathrm{e}^{-\mathrm{j}2\pi nFt}$, bringt so die $n$-te Harmonische zum Stillstand und mittelt. Jede andere Harmonische dreht sich dabei in der Periode $|k-n|$-mal ganz herum und mittelt sich zu null weg. Schwingungen verschiedener Frequenz heißen deshalb __orthogonal__.

Falle: Die Amplitude der reellen Kosinusschwingung ist $2|S_p(k)|$, nicht $|S_p(k)|$, denn $k$ und $-k$ tragen je die Hälfte bei. Nur der Gleichanteil $S_p(0)$ steht ohne Faktor 2.
::::

::::formelsammlung
**Grundfrequenz und Harmonische**

$$F=1/T,\qquad f_k=kF$$

$T$ Periode, $k$ ganzzahlig. Eine Schwingung $\mathrm{e}^{\mathrm{j}2\pi ft}$ hat die Periode $T$ genau dann, wenn $fT$ ganzzahlig ist.

**Fourier-Reihe (Synthese)**

$$s_p(t)=\sum_{k=-\infty}^{\infty}S_p(k)\,\mathrm{e}^{\mathrm{j}2\pi kFt}$$

$s_p$ periodisch mit $T=1/F$ und endlicher Leistung: Der Mittelwert von $|s_p(t)|^2$ über eine Periode ist endlich. $S_p(k)$ komplexes Gewicht der $k$-ten Harmonischen.

**Orthogonalität**

$$\frac1T\int_0^T\mathrm{e}^{\mathrm{j}2\pi(k-n)Ft}\,\mathrm{d} t=\begin{cases}1&k=n\\0&k\neq n\end{cases}$$

$k$, $n$ ganzzahlig. Für $k\neq n$ dreht sich der Zeiger in der Periode $|k-n|$-mal ganz herum, sein Mittelwert ist null.

**Fourier-Koeffizienten (Analyse)**

$$S_p(k)=\frac1T\int_{t_1}^{t_1+T}s_p(t)\,\mathrm{e}^{-\mathrm{j}2\pi kFt}\,\mathrm{d} t$$

$t_1$ beliebig, integriert wird über eine Periode. $S_p(0)$ ist der Gleichanteil, der Mittelwert des Signals.

**Reelle Signale**

$$S_p(-k)=S_p^*(k)$$

Für $s_p=s_p^*$. Jedes Paar $k,-k$ ergibt $2\operatorname{Re}\{S_p(k)\mathrm{e}^{\mathrm{j}2\pi kFt}\}$, eine reelle Kosinusschwingung.

**Kosinusform**

$$s_p(t)=S_p(0)+2\sum_{k=1}^{\infty}|S_p(k)|\cos\bigl(2\pi kFt+\varphi_p(k)\bigr)$$

Reelles Signal, $S_p(k)=|S_p(k)|\,\mathrm{e}^{\mathrm{j}\varphi_p(k)}$. Die Phase $\varphi_p(k)$ bestimmt man mit $\arctan$ und Quadrantenkorrektur ($+\pi$ bei negativem Realteil).

**Kosinus-Sinus-Form**

$$s_p(t)=S_p(0)+2\sum_{k=1}^{\infty}\Bigl[\operatorname{Re}\{S_p(k)\}\cos(2\pi kFt)-\operatorname{Im}\{S_p(k)\}\sin(2\pi kFt)\Bigr]$$

Reelles Signal.

**Koeffizienten der Rechteckschwingung**

$$S_p(0)=\frac{T_1}{T},\qquad S_p(k)=\frac{\sin(\pi kT_1/T)}{\pi k}\quad(k\neq0)$$

Signal 1 für $|t|\le T_1/2$ und 0 im Rest der Periode $T$. Das Signal ist gerade, deshalb sind alle Koeffizienten reell. Bei $T_1=T/2$ fehlen die geraden Harmonischen.
::::

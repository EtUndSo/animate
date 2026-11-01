---
title: Fourier-Reihe und Fourier-Transformation
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / Fourier-Reihe und -Transformation
order: 3230100
summary: Jedes Signal als Überlagerung von Schwingungen
tags: Spektrum, Frequenzgang, Grundfrequenz, Harmonischen, Fourier-Reihe, Gleichanteil, orthogonal, Leistung
lang: de
---

## Worum es geht

[Teil 2](/wissen/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html) hat gezeigt: Jedes Signal ist eine Überlagerung von Bausteinen $\mathrm{e}^{pt}$, und ein LTI-System multipliziert jeden Baustein nur mit einer Zahl. Die Fourier-Beschreibung benutzt davon nur die Bausteine auf der imaginären Achse, $p=\mathrm{j}2\pi f$: reine Schwingungen $\mathrm{e}^{\mathrm{j}2\pi ft}$, die weder wachsen noch abklingen. Das hat einen großen Vorteil. Eine Schwingung hat eine Frequenz, die man hören, messen und filtern kann. Das __Spektrum__ $S(f)$ sagt, mit welcher Amplitude und Phase jede Frequenz im Signal steckt.

:::merke Die Antwort in drei Sätzen (am Ende des Artikels sollen sie selbstverständlich sein)
<ol>

<li>

Ein periodisches Signal ist eine Summe von Schwingungen bei Vielfachen der Grundfrequenz (Fourier-Reihe), ein einmaliges Signal ein Integral über alle Frequenzen (Fourier-Integral).

</li>

<li>

Jede Schwingung $\mathrm{e}^{\mathrm{j}2\pi ft}$ ist eine Eigenfunktion: Ein LTI-System multipliziert sie mit $H(f)$, deshalb wird aus der Faltung das Produkt $G(f)=S(f)\,H(f)$.

</li>

<li>

Alle Rechenregeln (Verschiebung, Dehnung, Modulation, Symmetrie) folgen daraus, was die jeweilige Operation mit einer einzelnen Schwingung macht.

</li>

</ol>
:::

**Ein Prinzip hinter allen Ergebnissen.**

| Ergebnis | Woher es kommt |
|---|---|
| Frequenzgang $H(f)$ | Eigenwert der Schwingung $\mathrm{e}^{\mathrm{j}2\pi ft}$ (Stufe [1](#stufe-1)) |
| Fourier-Reihe, nur Vielfache von $F$ | nur diese Schwingungen haben die Periode $T$ (Stufe [2](#stufe-2)) |
| Analyseformel der Reihe | Schwingungen verschiedener Frequenz sind orthogonal (Stufe [2](#stufe-2)) |
| Parseval, Gibbs, LTI mit periodischem Eingang | jede Harmonische für sich (Stufe [3](#stufe-3)) |
| Fourier-Integral | Periode $\to\infty$, die Linien rücken zusammen (Stufe [4](#stufe-4)) |
| $S(-f)=S^*(f)$ bei reellen Signalen | Schwingungen treten in konjugierten Paaren auf (Stufe [5](#stufe-5)) |
| Verschiebung, Dehnung, Ableitung, Modulation | was die Operation mit $\mathrm{e}^{\mathrm{j}2\pi ft}$ macht (Stufe [6](#stufe-6)) |
| Symmetrie (Dualität) | Hin- und Rücktransformation unterscheiden sich nur im Vorzeichen (Stufe [6](#stufe-6)) |
| Linienspektren, Dirac-Kamm, Sprung | Grenzfälle mit Dirac-Impulsen (Stufe [8](#stufe-8)) |
| Hilbert-Transformation | ein kausales Signal ist durch eine Hälfte festgelegt (Stufe [9](#stufe-9)) |
| Kurzzeit-Fourier | Spektrum eines Ausschnitts (Stufe [10](#stufe-10)) |

**So arbeitest du mit dem Artikel.** Jede Stufe hat die Idee, typische Fragen mit aufklappbaren Antworten und Aufgaben (★ bis ★★★). Versuche die Aufgaben zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf.

:::merke Das Rechenmodell für diesen Artikel
<ul>

<li>

⁠**Rechteckschwingung** zwischen 0 und 1 mit der Periode $T=2\pi$ s und dem Tastgrad $\frac12$: 1 für $|t|\le T/4$, 0 für $T/4<|t|\le T/2$, periodisch fortgesetzt. Grundfrequenz $F=1/T=0{,}159$ Hz, also $2\pi F=1/\mathrm s$.

</li>

<li>

⁠**RC-Tiefpass** mit $RC=1$ s, $H(f)=1/(1+\mathrm{j}2\pi f\,RC)$. Bei der $k$-ten Harmonischen der Rechteckschwingung ist $2\pi kF\cdot RC=k$, also $H(kF)=1/(1+\mathrm{j} k)$.

</li>

<li>

⁠**Rechteckimpuls** $\operatorname{rect}(t)$ und $\operatorname{si}(x)=\sin(x)/x$.

</li>

</ul>

Die Zahlen und Kurven rechnet `rechnung_kap3.py` nach.
:::

## Stufe 1: Schwingungen als Eigenfunktionen

<span class="anker" id="stufe-1"></span>

:::zweck
Von den Bausteinen $\mathrm{e}^{pt}$ werden jetzt nur die reinen Schwingungen benutzt. Diese Stufe zeigt, was ein LTI-System mit ihnen macht.
:::

Für rein imaginäres $p=\mathrm{j}2\pi f$ wird der Baustein zur Schwingung mit konstanter Amplitude:

$$\mathrm{e}^{\mathrm{j}2\pi ft}=\cos(2\pi ft)+\mathrm{j}\sin(2\pi ft).$$

Wie jeder Baustein ist sie eine Eigenfunktion jedes LTI-Systems (Verzögern ist Multiplizieren mit $\mathrm{e}^{-\mathrm{j}2\pi f\tau}$):

<span class="anker" id="gl-1-1"></span>
$$\mathrm{e}^{\mathrm{j}2\pi ft}*h(t)=H(f)\,\mathrm{e}^{\mathrm{j}2\pi ft},\qquad H(f)=\int_{-\infty}^{\infty}h(t)\,\mathrm{e}^{-\mathrm{j}2\pi ft}\,\mathrm{d} t. \tag{1.1}$$

$H(f)$ heißt __Frequenzgang__ oder Übertragungsfunktion. Sein Betrag sagt, wie stark die Schwingung der Frequenz $f$ verstärkt oder geschwächt wird, seine Phase, wie weit sie verschoben wird. Zwei Systeme in Kette multiplizieren nacheinander: $H(f)=H_1(f)H_2(f)$. Wo die Laplace-Transformierte $H(p)$ auf der imaginären Achse existiert, ist $H(f)=H(p)|_{p=\mathrm{j}2\pi f}$.

⁠**Kurz gesagt:** Der Frequenzgang ist die Zahl, mit der ein LTI-System eine reine Schwingung multipliziert.

## Stufe 2: Periodische Signale, die Fourier-Reihe

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

Ein Signal mit der Periode $T=1/F$ und endlicher Leistung hat die Darstellung [(2.1)](#gl-2-1) mit

<span class="anker" id="gl-2-5"></span>
$$S_p(k)=\frac1T\int_{t_1}^{t_1+T}s_p(t)\,\mathrm{e}^{-\mathrm{j}2\pi kFt}\,\mathrm{d} t, \tag{2.5}$$

wobei $t_1$ beliebig ist (Analyse).
:::

⁠**So liest man das:** $S_p(k)$ ist der Mittelwert des Signals, nachdem man es mit der $k$-ten Harmonischen „entgegengedreht“ hat. Steckt die Harmonische im Signal, dreht sich der Zeiger an dieser Stelle nicht mehr, und ihr Anteil bleibt im Mittel übrig. $S_p(0)$ ist einfach der Mittelwert.

:::herleitung Analyseformel
[(2.1)](#gl-2-1) mit $\mathrm{e}^{-\mathrm{j}2\pi nFt}$ multiplizieren, über eine Periode integrieren, Summe und Integral vertauschen:

$$\int_0^Ts_p(t)\mathrm{e}^{-\mathrm{j}2\pi nFt}\mathrm{d} t=\sum_kS_p(k)\int_0^T\mathrm{e}^{\mathrm{j}2\pi(k-n)Ft}\mathrm{d} t=S_p(n)\,T.$$

Für $k\neq n$ ist das Integral $\frac{\mathrm{e}^{\mathrm{j}2\pi(k-n)FT}-1}{\mathrm{j}2\pi(k-n)F}=0$, weil $\mathrm{e}^{\mathrm{j}2\pi(k-n)}=1$. Da der Integrand die Periode $T$ hat, darf man über jedes Intervall der Länge $T$ integrieren.
:::

**Beispiel: eine endliche Reihe.** $s_p(t)=1+2\cos(2\pi Ft)+\sin(4\pi Ft)$. Mit den Euler-Formeln liest man die Koeffizienten ab, ohne zu integrieren:

$$2\cos(2\pi Ft)=\mathrm{e}^{\mathrm{j}2\pi Ft}+\mathrm{e}^{-\mathrm{j}2\pi Ft},\qquad\sin(4\pi Ft)=\frac{1}{2\mathrm{j}}\mathrm{e}^{\mathrm{j}4\pi Ft}-\frac{1}{2\mathrm{j}}\mathrm{e}^{-\mathrm{j}4\pi Ft},$$

also $S_p(0)=1$, $S_p(\pm1)=1$, $S_p(2)=-\tfrac{\mathrm{j}}{2}$, $S_p(-2)=\tfrac{\mathrm{j}}{2}$, alle anderen null. Probe: $S_p(-2)=S_p^*(2)$.

**Beispiel: die Rechteckschwingung.** Für das Rechenmodell (1 für $|t|\le T_1/2$ mit $T_1=T/2$):

<span class="anker" id="gl-2-6"></span>
$$S_p(0)=\frac{T_1}{T},\qquad S_p(k)=\frac1T\int_{-T_1/2}^{T_1/2}\mathrm{e}^{-\mathrm{j}2\pi kFt}\mathrm{d} t=\frac{\sin(\pi kT_1/T)}{\pi k}\quad(k\neq0). \tag{2.6}$$

Mit $T_1=T/2$: $S_p(0)=0{,}5$, $S_p(\pm1)=1/\pi=0{,}318$, $S_p(\pm2)=0$, $S_p(\pm3)=-0{,}106$, $S_p(\pm5)=0{,}064$. Die geraden Harmonischen fehlen, weil $\sin(\pi k/2)=0$ für gerade $k$. Alle Koeffizienten sind reell, weil das Signal gerade ist (Stufe [5](#stufe-5)). Abbildung [1](#abb-1) zeigt sie für zwei Tastgrade: Je schmaler der Impuls, desto langsamer fallen die Koeffizienten ab.

:::abbildung et3/k3koeff
Fourier-Koeffizienten der Rechteckschwingung (0/1) für zwei Impulsbreiten. Gestrichelt die Hüllkurve $\frac{T_1}{T}\operatorname{si}(\pi kT_1/T)$. Bei $T_1=T/2$ fehlen die geraden Harmonischen, bei $T_1=T/4$ jede vierte.
:::

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

## Stufe 3: Leistung, Konvergenz und LTI-Systeme

<span class="anker" id="stufe-3"></span>

:::zweck
Wie viel trägt jede Harmonische zum Signal bei, wie gut nähert eine abgebrochene Reihe das Signal, und was macht ein LTI-System mit einem periodischen Eingang?
:::

:::satz Satz 3.1 (Parseval für Fourier-Reihen)
<span class="anker" id="satz-3-1"></span>

<span class="anker" id="gl-3-1"></span>
$$L_s=\frac1T\int_0^T|s_p(t)|^2\,\mathrm{d} t=\sum_{k=-\infty}^{\infty}|S_p(k)|^2. \tag{3.1}$$
:::

⁠**So liest man das:** Die mittlere __Leistung__ des Signals ist die Summe der Leistungen der einzelnen Harmonischen. Mischterme fallen weg, weil verschiedene Harmonische orthogonal sind. Für die Rechteckschwingung ist $L_s=\frac12$. Der Gleichanteil trägt $0{,}25$ bei, also 50 %. Mit $k=\pm1$ sind es 90,5 %, mit $|k|\le3$ 95,0 %, mit $|k|\le9$ 98,0 %.

:::herleitung Parseval
$|s_p|^2=s_ps_p^*=\sum_k\sum_lS_p(k)S_p^*(l)\,\mathrm{e}^{\mathrm{j}2\pi(k-l)Ft}$. Über eine Periode gemittelt bleibt nach [(2.4)](#gl-2-4) nur $k=l$: $\sum_k|S_p(k)|^2$.
:::

**Abgebrochene Reihe und Gibbs-Phänomen.** Nimmt man nur die Harmonischen bis $|k|\le N$, ist die __Teilsumme__ $s_{p,N}(t)=\sum_{k=-N}^{N}S_p(k)\mathrm{e}^{\mathrm{j}2\pi kFt}$. Die Leistung des Fehlers $s_p-s_{p,N}$ ist die Summe der weggelassenen $|S_p(k)|^2$ und geht für $N\to\infty$ gegen null, wenn das Signal eine endliche Leistung hat. An einer Sprungstelle bleibt aber ein Überschwinger stehen (Abb. [2](#abb-2)): Er wird mit wachsendem $N$ schmaler, seine Höhe strebt aber gegen etwa 9 % der Sprunghöhe (10,0 % bei $N=3$, 9,1 % bei $N=9$, 9,0 % bei $N=27$, Grenzwert 8,95 %). Das ist das __Gibbs-Phänomen__. Es widerspricht der Konvergenz nicht: Die Fläche unter dem Überschwinger und damit die Fehlerleistung geht trotzdem gegen null.

:::abbildung et3/k3gibbs
Teilsummen der Rechteckschwingung ($T=2\pi$ s) mit den Harmonischen bis $|k|\le N$. An den Kanten bleibt ein Überschwinger von etwa 9 % der Sprunghöhe, der mit wachsendem $N$ nur schmaler wird.
:::

**Periodischer Eingang an einem LTI-System.** Jede Harmonische ist eine Eigenfunktion und wird mit $H(kF)$ multipliziert. Der Ausgang hat deshalb dieselbe Periode, und seine Koeffizienten sind

<span class="anker" id="gl-3-2"></span>
$$G_p(k)=S_p(k)\,H(kF). \tag{3.2}$$

Im Rechenmodell ist $H(kF)=1/(1+\mathrm{j} k)$. Die Grundschwingung wird mit $|H|=0{,}707$ und $-45^\circ$ übertragen, die dritte Harmonische mit $0{,}316$ und $-71{,}6^\circ$, die fünfte mit $0{,}196$ und $-78{,}7^\circ$. Am Ausgang ist die dritte Harmonische nur noch 15 % so groß wie die erste statt 33 % am Eingang. Das RC-Glied rundet die Kanten ab (Abb. [3](#abb-3)). Der Ausgang pendelt zwischen 0,041 und 0,959.

:::abbildung et3/k3rc
Rechteckschwingung durch den RC-Tiefpass mit $RC=1$ s, berechnet als Summe der Harmonischen mit $G_p(k)=S_p(k)/(1+\mathrm{j} k)$. Der Ausgang lädt und entlädt sich exponentiell zwischen 0,041 und 0,959.
:::

:::frage Ist eine Rechnung über unendlich viele Harmonische nicht viel umständlicher als die Differentialgleichung?
Für eine einzelne Rechteckschwingung durch ein RC-Glied ja: Lade- und Entladekurve kann man direkt hinschreiben. Die Reihe zeigt dafür, *warum* der Ausgang so aussieht. Die Kanten bestehen aus den hohen Harmonischen, und genau diese schwächt das RC-Glied. Außerdem funktioniert [(3.2)](#gl-3-2) für jedes LTI-System, auch für solche, deren Differentialgleichung man gar nicht kennt, sondern nur ihren gemessenen Frequenzgang.
:::

:::ltspice Rechteckschwingung durch das RC-Glied
⁠**Zeichnen:** RC-Glied (`res` mit `1Meg`, `cap` mit `1u`) mit der Quelle `PULSE(0 1 0 1u 1u {pi} {2*pi})`: Periode $2\pi$ s, Tastgrad $\frac12$.

⁠**Direktiven:** `.tran 0 {20*pi} 0 1m`, `.four {1/(2*pi)} 5 V(in) V(out)` und `.options plotwinsize=0`. Die letzte schaltet die Datenkompression ab, ohne sie rechnet `.four` ungenau. `.four` zerlegt die letzte Periode in Harmonische und schreibt das Ergebnis ins SPICE Error Log.

⁠**Was du siehst:** Im eingeschwungenen Zustand pendelt `V(out)` zwischen 0,041 und 0,959. `.four` gibt für $k\ge1$ die Amplituden $2|S_p(k)|$ der Kosinusschwingungen in [(2.2)](#gl-2-2) an. Am Eingang sind das 0,637; 0; 0,212; 0; 0,127: Die geraden Harmonischen fehlen. Am Ausgang ist die dritte Harmonische nur noch 15 % so groß wie die erste statt 33 %. Die Phasen am Ausgang sind um $45^\circ$, $71{,}6^\circ$ und $78{,}7^\circ$ größer als am Eingang, denn `.four` zählt eine Nacheilung positiv. Halbiere die Ausgangsamplituden und vergleiche mit deinem Ergebnis aus Aufgabe [3](#aufg-3)(b). Die FFT-Ansicht (Rechtsklick ins Diagramm, View, FFT) zeigt dieselben Linien bei den ungeraden Vielfachen von 0,159 Hz.
:::

:::aufgabe Aufgabe 3 ★★ Leistung und Oberschwingungen
<span class="anker" id="aufg-3"></span>

<ol class="al">

<li>

Bestätige mit [(3.1)](#gl-3-1): Die Harmonischen $k=0,\pm1$ der Rechteckschwingung tragen 90,5 % der Leistung.

</li>

<li>

Berechne $|G_p(1)|$, $|G_p(3)|$, $|G_p(5)|$ für den RC-Ausgang. Welcher Anteil der Wechselleistung des Ausgangs (ohne $k=0$) steckt in der Grundschwingung, wenn du nur $k=\pm1,\pm3,\pm5$ berücksichtigst?

</li>

<li>

Warum sieht der Ausgang schon „sinusähnlicher“ aus als der Eingang?

</li>

</ol>

:::loesung
(a) $|S_p(0)|^2+2|S_p(1)|^2=0{,}25+2/\pi^2=0{,}25+0{,}2026=0{,}4526$, von $0{,}5$ sind das 90,5 %.

(b) $|G_p(k)|=|S_p(k)|/\sqrt{1+k^2}$: $|G_p(1)|=0{,}2251$, $|G_p(3)|=0{,}0336$, $|G_p(5)|=0{,}0125$. Wechselleistung aus diesen Harmonischen: $2(0{,}0507+0{,}0011+0{,}0002)=0{,}1039$. Der Anteil der Grundschwingung ist $0{,}0507/0{,}0519=97{,}5\,\%$. Am Eingang wären es für dieselben Harmonischen nur 86,9 %.

(c) $|H(kF)|=1/\sqrt{1+k^2}\approx1/k$: Die Oberschwingungen werden umso stärker geschwächt, je höher sie sind. Übrig bleibt vor allem die Grundschwingung, und ein Signal, das fast nur aus der Grundschwingung besteht, ist fast ein Sinus.
:::
:::

## Stufe 4: Vom periodischen zum einmaligen Signal

<span class="anker" id="stufe-4"></span>

:::zweck
Ein einzelner Impuls ist nicht periodisch. Man kann ihn aber als periodisches Signal mit unendlich langer Periode auffassen. Dabei wird aus der Summe ein Integral.
:::

**Die Idee.** Man setzt einen Impuls $s(t)$ der Dauer kleiner als $T$ periodisch fort. Die Koeffizienten der Reihe sind dann Werte einer festen Funktion:

$$S_p(k)=\frac1T\int_{-\infty}^{\infty}s(t)\mathrm{e}^{-\mathrm{j}2\pi kFt}\mathrm{d} t=F\cdot S(kF),\qquad S(f)=\int_{-\infty}^{\infty}s(t)\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t.$$

Verdoppelt man die Periode, halbiert sich der Linienabstand $F$, und die Linien tasten dieselbe Hüllkurve $S(f)$ doppelt so dicht ab (Abb. [4](#abb-4)). Im Grenzfall $T\to\infty$ wird aus dem Abstand $F$ das Differential $\mathrm{d} f$ und aus der Summe $\sum_kS(kF)\mathrm{e}^{\mathrm{j}2\pi kFt}F$ das Integral.

:::abbildung et3/k3grenz
Ein Rechteckimpuls $\operatorname{rect}(t)$, periodisch fortgesetzt mit $T=2$ s und $T=4$ s. Die mit $T$ multiplizierten Fourier-Koeffizienten liegen auf derselben Hüllkurve $S(f)=\operatorname{si}(\pi f)$, mit dem Abstand $1/T$. Für $T\to\infty$ füllen sie die Kurve lückenlos.
:::

:::satz Satz 4.1 (Fourier-Transformation)
<span class="anker" id="satz-4-1"></span>

<span class="anker" id="gl-4-1"></span>
$$S(f)=\int_{-\infty}^{\infty}s(t)\,\mathrm{e}^{-\mathrm{j}2\pi ft}\,\mathrm{d} t,\qquad s(t)=\int_{-\infty}^{\infty}S(f)\,\mathrm{e}^{\mathrm{j}2\pi ft}\,\mathrm{d} f. \tag{4.1}$$

Kurzschreibweise: $s(t)\;\circ\!\!-\!\!\bullet\;S(f)$ oder $S(f)=\mathcal{F}\{s(t)\}$.
:::

⁠**So liest man das:** $S(f)$ ist eine __Spektraldichte__: Gewicht pro Frequenzintervall. Ist $s$ eine Spannung in V, hat $S$ die Einheit V/Hz. Die Rücktransformation setzt das Signal aus allen Schwingungen zusammen, jede mit dem Gewicht $S(f)\,\mathrm{d} f$. Hinreichend für die Existenz ist $\int|s(t)|\mathrm{d} t<\infty$. Die Fourier-Transformierte ist die Laplace-Transformierte auf der imaginären Achse, $S(f)=S_{\mathcal{L}}(\mathrm{j}2\pi f)$, sofern diese im Konvergenzbereich liegt ([Teil 2](/wissen/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html)).

⁠**Faltung wird Produkt.** Wie in [Teil 2](/wissen/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html): $s(t)*h(t)\;\circ\!\!-\!\!\bullet\;S(f)\,H(f)$. Aus $s*\delta=s$ folgt $S(f)\cdot\mathcal{F}\{\delta\}=S(f)$, also $\delta(t)\;\circ\!\!-\!\!\bullet\;1$: Der Dirac-Impuls enthält alle Frequenzen mit gleichem Gewicht.

**Beispiel: der Exponentialimpuls.** Die Impulsantwort des RC-Glieds, $h(t)=\frac1{RC}\varepsilon(t)\mathrm{e}^{-t/RC}$:

$$H(f)=\frac1{RC}\int_0^\infty\mathrm{e}^{-(1/RC+\mathrm{j}2\pi f)t}\mathrm{d} t=\frac{1}{1+\mathrm{j}2\pi f\,RC}.$$

Das ist derselbe Frequenzgang wie aus der Wechselstromrechnung ([Teil 1](/wissen/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html)). Die Impulsantwort enthält also die ganze Information über das Frequenzverhalten.

:::frage Was ist der Unterschied zwischen $S_p(k)$ und $S(f)$, außer dass das eine diskret ist?
Die Einheit. $S_p(k)$ ist eine Amplitude (V): Die $k$-te Harmonische hat wirklich diese Stärke. $S(f)$ ist eine Dichte (V/Hz): Bei einem einmaligen Signal hat keine einzelne Frequenz eine endliche Amplitude, erst ein Frequenzband $\Delta f$ trägt etwa $S(f)\,\Delta f$. Deshalb ist $S_p(k)=F\cdot S(kF)$: Jede Linie vertritt ein Band der Breite $F$.
:::

:::aufgabe Aufgabe 4 ★ Der zweiseitige Exponentialimpuls
<span class="anker" id="aufg-4"></span>

Berechne $\mathcal{F}\{\mathrm{e}^{-a|t|}\}$ für $a>0$, indem du das Integral in $t<0$ und $t>0$ teilst. Zeige, dass das Ergebnis reell und gerade ist, und begründe das mit der Symmetrie des Signals.

:::loesung
$$\int_{-\infty}^0\mathrm{e}^{at}\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t+\int_0^\infty\mathrm{e}^{-at}\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t=\frac{1}{a-\mathrm{j}2\pi f}+\frac{1}{a+\mathrm{j}2\pi f}=\frac{2a}{a^2+(2\pi f)^2}.$$

Reell und gerade in $f$. Das muss so sein: Das Signal ist reell und gerade, also ist sein ungerader Anteil null und damit auch $\operatorname{Im} S$ (Stufe [5](#stufe-5)).
:::
:::

## Stufe 5: Symmetrien im Signal und im Spektrum

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

**Beispiel.** Der Exponentialimpuls $\varepsilon(t)\mathrm{e}^{-t}$ (reell) hat den geraden Anteil $\frac12\mathrm{e}^{-|t|}$ und den ungeraden $\frac12\operatorname{sgn}(t)\mathrm{e}^{-|t|}$. Sein Spektrum $H(f)=\frac{1}{1+\mathrm{j}2\pi f}$ hat den geraden Realteil $\frac{1}{1+(2\pi f)^2}$, die Transformierte von $\frac12\mathrm{e}^{-|t|}$, und den ungeraden Imaginärteil $\frac{-2\pi f}{1+(2\pi f)^2}$ (Abb. [5](#abb-5)).

:::abbildung et3/k3gerade
Der Exponentialimpuls ($RC=1$ s), zerlegt in einen geraden (blau) und einen ungeraden Anteil (rot). Rechts das Spektrum: Der gerade Anteil liefert den Realteil (gerade in $f$), der ungerade Anteil den Imaginärteil (ungerade in $f$).
:::

:::aufgabe Aufgabe 5 ★ Symmetrie ablesen
<span class="anker" id="aufg-5"></span>

Was lässt sich ohne Rechnung über das Spektrum sagen? (a) $s(t)=\operatorname{rect}(t)$, (b) $s(t)=\operatorname{sgn}(t)\operatorname{rect}(t/2)$, (c) $s(t)=\mathrm{e}^{\mathrm{j}2\pi t}\operatorname{rect}(t)$, (d) ein reelles Signal mit $S(1\,\mathrm{Hz})=2-3\mathrm{j}$: Was ist $S(-1\,\mathrm{Hz})$?

:::loesung
(a) Reell und gerade: Spektrum reell und gerade ($\operatorname{si}(\pi f)$). (b) Reell und ungerade: Spektrum rein imaginär und ungerade. (c) Komplex, aber $x^*(-t)=\mathrm{e}^{-\mathrm{j}2\pi(-t)}\operatorname{rect}(-t)=x(t)$: Im Sinne der Definition ist das Signal gerade, also ist sein Spektrum reell. Nach der Modulationsregel ist es $\operatorname{si}(\pi(f-1))$, reell, aber nicht symmetrisch um $f=0$, weil das Signal nicht reell ist. (d) $S(-1\,\mathrm{Hz})=S^*(1\,\mathrm{Hz})=2+3\mathrm{j}$.
:::
:::

## Stufe 6: Die Rechenregeln (Theoreme)

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

Benutze $\operatorname{rect}(t)\;\circ\!\!-\!\!\bullet\;\operatorname{si}(\pi f)$ (Stufe [7](#stufe-7)) und die Theoreme.

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

Aus Aufgabe [4](#aufg-4) weißt du $\mathrm{e}^{-|t|}\;\circ\!\!-\!\!\bullet\;\frac{2}{1+(2\pi f)^2}$. Bestimme damit ohne Integral das Spektrum von $\frac{1}{1+t^2}$.

:::loesung
Symmetrie auf das Paar anwenden: $\frac{2}{1+(2\pi t)^2}\;\circ\!\!-\!\!\bullet\;\mathrm{e}^{-|f|}$. Jetzt die Zeit dehnen. Mit $x(t)=\frac{2}{1+(2\pi t)^2}$ ist $x\bigl(\frac{t}{2\pi}\bigr)=\frac{2}{1+t^2}$, nach dem Ähnlichkeitssatz mit $b=\frac1{2\pi}$ also $\circ\!\!-\!\!\bullet\;2\pi\,\mathrm{e}^{-2\pi|f|}$. Halbieren:

$$\frac{1}{1+t^2}\;\circ\!\!-\!\!\bullet\;\pi\,\mathrm{e}^{-2\pi|f|}.$$

Probe mit dem Flächensatz: $\int\frac{\mathrm{d} t}{1+t^2}=\pi=S(0)$.
:::
:::

## Stufe 7: Rechteck, si-Funktion und Dreieck

<span class="anker" id="stufe-7"></span>

:::zweck
Drei Transformationspaare kommen ständig vor. Mit den Theoremen folgen sie aus einer einzigen Rechnung.
:::

**Rechteck.** Mit $\operatorname{si}(x)=\sin(x)/x$:

$$\int_{-1/2}^{1/2}\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t=\frac{\mathrm{e}^{-\mathrm{j}\pi f}-\mathrm{e}^{\mathrm{j}\pi f}}{-\mathrm{j}2\pi f}=\frac{\sin(\pi f)}{\pi f}=\operatorname{si}(\pi f).$$

:::satz Satz 7.1 (Rechteck, si und Dreieck)
<span class="anker" id="satz-7-1"></span>

<span class="anker" id="gl-7-1"></span>
<span class="anker" id="gl-7-2"></span>
<span class="anker" id="gl-7-3"></span>
<span class="anker" id="gl-7-4"></span>
$$\begin{aligned} \operatorname{rect}\Bigl(\frac tT\Bigr)&\;\circ\!\!-\!\!\bullet\;|T|\operatorname{si}(\pi Tf),\\ \operatorname{si}\Bigl(\frac{\pi t}{T}\Bigr)&\;\circ\!\!-\!\!\bullet\;|T|\operatorname{rect}(Tf),\\ \Lambda(t)=\operatorname{rect}(t)*\operatorname{rect}(t)&\;\circ\!\!-\!\!\bullet\;\operatorname{si}^2(\pi f),\\ \operatorname{si}(\pi t)*\operatorname{si}(\pi t)&=\operatorname{si}(\pi t). \end{aligned} \tag{7.1|7.2|7.3|7.4}$$
:::

⁠**So liest man das:** Ein Rechteck der Dauer $T$ hat ein Spektrum der Höhe $T$ (seine Fläche) mit Nullstellen bei allen von null verschiedenen Vielfachen von $1/T$. Doppelt so lang heißt halb so breit im Spektrum (Abb. [6](#abb-6)). [(7.2)](#gl-7-2) folgt aus der Symmetrie, [(7.3)](#gl-7-3) aus dem Faltungssatz, und [(7.4)](#gl-7-4) gilt, weil im Frequenzbereich $\operatorname{rect}(f)\cdot\operatorname{rect}(f)=\operatorname{rect}(f)$ ist: Ein idealer Tiefpass ändert ein Signal nicht, das schon auf sein Band begrenzt ist.

:::abbildung et3/k3rectsi
$\operatorname{rect}(t/T)$ und sein Spektrum $|T|\operatorname{si}(\pi Tf)$ für $T=1$ s und $T=2$ s. Doppelte Dauer: doppelte Höhe ($=$ Fläche), halbe Breite, erste Nullstelle bei $1/T$.
:::

:::ltspice Spektrum eines Rechteckimpulses
⁠**Zeichnen:** nur eine Quelle `voltage` mit `PULSE(0 1 0 1u 1u {T0} 16)`: ein Rechteck der Dauer $T_0$, alle 16 s wiederholt.

⁠**Direktiven:** `.param T0=1`, `.step param T0 list 1 2`, `.tran 0 16 0 1m`, `.options plotwinsize=0`, `.four 0.0625 40 V(in)`.

⁠**Was du siehst:** Die Wiederholung alle 16 s macht aus dem Spektrum Linien im Abstand $1/16$ Hz (Stufe [4](#stufe-4)). `.four` gibt ihre Amplituden $\frac{2}{16}\,|T_0\operatorname{si}(\pi T_0f)|$ an, also Abtastwerte der si-Hüllkurve. Bei $T_0=1$ s sind die Linien bei 1 Hz und 2 Hz null, bei $T_0=2$ s schon die bei 0,5 Hz, 1 Hz, 1,5 Hz und 2 Hz. Der Gleichanteil verdoppelt sich von 0,0625 auf 0,125. Doppelte Dauer heißt also halbe Breite und doppelte Höhe, wie in Abb. [6](#abb-6). In der FFT-Ansicht siehst du die Hüllkurve mit ihren Nullstellen direkt.
:::

:::aufgabe Aufgabe 8 ★ Flächen und Energie der si-Funktion
<span class="anker" id="aufg-8"></span>

Berechne ohne Integration $\int_{-\infty}^\infty\operatorname{si}(\pi t)\mathrm{d} t$ und $\int_{-\infty}^\infty\operatorname{si}^2(\pi t)\mathrm{d} t$. Benutze den Flächensatz und Parseval.

:::loesung
Flächensatz: $\int\operatorname{si}(\pi t)\mathrm{d} t=\mathcal{F}\{\operatorname{si}(\pi t)\}(0)=\operatorname{rect}(0)=1$. Parseval: $\int\operatorname{si}^2(\pi t)\mathrm{d} t=\int\operatorname{rect}^2(f)\mathrm{d} f=1$.
:::
:::

:::aufgabe Aufgabe 9 ★★ Dreieck und Mehrfachfaltung
<span class="anker" id="aufg-9"></span>

<ol class="al">

<li>

Bestimme das Spektrum von $\Lambda(t/2)$ (Dreieck der halben Breite 2 s). Wo liegen die Nullstellen?

</li>

<li>

Welches Spektrum hat $\operatorname{rect}*\operatorname{rect}*\operatorname{rect}$? Warum fallen die Nebenzipfel umso schneller ab, je öfter man faltet?

</li>

</ol>

:::loesung
(a) $\Lambda(t)\circ\!\!-\!\!\bullet\operatorname{si}^2(\pi f)$ und Ähnlichkeit mit $T=2$: $\Lambda(t/2)\circ\!\!-\!\!\bullet\,2\operatorname{si}^2(2\pi f)$. Nullstellen bei $f=k/2$, $k\neq0$.

(b) $\operatorname{si}^3(\pi f)$. Jede weitere Faltung multipliziert das Spektrum mit $\operatorname{si}(\pi f)$, das in den Nebenzipfeln wie $1/(\pi f)$ abfällt. Bei $M$ gefalteten Rechtecken fallen die Nebenzipfel wie $1/f^M$. Im Zeitbereich: Das Rechteck springt (Abfall $1/f$), das Dreieck hat Knicke ($1/f^2$), die dreifache Faltung hat eine stetige Ableitung ($1/f^3$). Je glatter ein Signal, desto schneller fällt sein Spektrum ab.
:::
:::

## Stufe 8: Singuläre Signale und Linienspektren

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

Der __Dirac-Kamm__ (Impulse im Abstand $T$) hat wieder einen Dirac-Kamm als Spektrum, mit dem Abstand $1/T$ und dem Gewicht $1/|T|$ (Abb. [7](#abb-7)). Dieses Paar wird bei der Abtastung ([Teil 4](/wissen/elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme/abtastung-und-zeitdiskrete-systeme.html)) entscheidend.

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

:::abbildung et3/k3kamm
Dirac-Kamm mit $T=0{,}5$ s und sein Spektrum: wieder ein Kamm, mit dem Abstand $1/T=2$ Hz und dem Gewicht $1/T=2$. Je dichter die Impulse in der Zeit, desto weiter auseinander die Linien.
:::

:::frage Aus $\frac{\mathrm{d}}{\mathrm{d} t}\varepsilon=\delta$ folgt doch $\mathrm{j}2\pi f\,S(f)=1$, also $S(f)=\frac{1}{\mathrm{j}2\pi f}$. Woher kommt das $\frac12\delta(f)$?
Die Gleichung $\mathrm{j}2\pi f\,S(f)=1$ legt $S$ nur für $f\neq0$ fest. Bei $f=0$ steht links $0\cdot S(0)$, und ein Summand $c\,\delta(f)$ fällt wegen $f\delta(f)=0$ heraus. Das ist das Gegenstück dazu, dass Ableiten eine Konstante „vergisst“: $\varepsilon(t)$ und $\varepsilon(t)+b$ haben dieselbe Ableitung. Welche Konstante richtig ist, entscheidet der gerade Anteil: $\varepsilon$ hat den Mittelwert $\frac12$, also $c=\frac12$.
:::

**Beispiel: der eingeschaltete Kosinus.** $\varepsilon(t)\cos(2\pi Ft)$. Multiplikation wird Faltung, und die Faltung mit einem Dirac-Impuls verschiebt:

$$\Bigl[\tfrac12\delta(f)+\tfrac{1}{\mathrm{j}2\pi f}\Bigr]*\tfrac12\bigl[\delta(f+F)+\delta(f-F)\bigr] =\tfrac14\bigl[\delta(f+F)+\delta(f-F)\bigr]-\frac{\mathrm{j}}{4\pi}\Bigl[\frac{1}{f+F}+\frac{1}{f-F}\Bigr].$$

Neben den halbierten Linien bei $\pm F$ entsteht ein breites Spektrum: Der Einschaltvorgang selbst enthält Frequenzen nahe $\pm F$.

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

Prüfe mit [(5.2)](#gl-5-2): Das Spektrum von $\operatorname{sgn}(t)$ muss rein imaginär und ungerade sein.

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

## Stufe 9: Hilbert-Transformation und analytisches Signal

<span class="anker" id="stufe-9"></span>

:::zweck
Bei einem kausalen Signal hängen Real- und Imaginärteil des Spektrums zusammen: Der eine legt den anderen fest. Dieselbe Rechnung liefert ein Signal, das nur positive Frequenzen enthält.
:::

**Kausale Signale.** Ist $s(t)=0$ für $t<0$, dann sind gerader und ungerader Anteil für $t>0$ gleich ($\frac12s$) und für $t<0$ entgegengesetzt. Also $s_u(t)=s_g(t)\operatorname{sgn}(t)$ und $s_g(t)=s_u(t)\operatorname{sgn}(t)$. Im Frequenzbereich wird die Multiplikation mit $\operatorname{sgn}$ zur Faltung mit $\frac{1}{\mathrm{j}\pi f}$:

:::satz Satz 9.1 (Hilbert-Beziehung kausaler Signale)
<span class="anker" id="satz-9-1"></span>

Für ein kausales Signal gilt

<span class="anker" id="gl-9-1"></span>
$$\operatorname{Re}\{S(f)\}=\operatorname{Im}\{S(f)\}*\frac{1}{\pi f},\qquad\operatorname{Im}\{S(f)\}=-\operatorname{Re}\{S(f)\}*\frac{1}{\pi f}. \tag{9.1}$$
:::

⁠**So liest man das:** Die Faltung mit $\frac{1}{\pi f}$ heißt __Hilbert-Transformation__. Bei einem kausalen System genügt es, den Realteil des Frequenzgangs zu kennen, der Imaginärteil folgt daraus. Kausalität ist also eine starke Einschränkung für das Spektrum.

**Analytische Komponente.** Mit dem Sprung im *Frequenzbereich* schneidet man die negativen Frequenzen ab: $S_+(f)=S(f)\,\varepsilon(f)$. Aus der Symmetrie folgt $\varepsilon(f)\;\bullet\!\!-\!\!\circ\;\frac12\delta(t)+\frac{\mathrm{j}}{2\pi t}$, also

<span class="anker" id="gl-9-2"></span>
$$s_+(t)=\frac12s(t)+\frac{\mathrm{j}}{2}\,\hat s(t),\qquad\hat s(t)=s(t)*\frac{1}{\pi t}\;\circ\!\!-\!\!\bullet\;-\mathrm{j}\operatorname{sgn}(f)\,S(f). \tag{9.2}$$

$s_+$ heißt __analytische Komponente__, $\hat s$ die Hilbert-Transformierte von $s$. Für reelle Signale ist $S_-(f)=S_+^*(-f)$, also $s_-=s_+^*$ und $s(t)=s_++s_-=2\operatorname{Re}\{s_+(t)\}$. Real- und Imaginärteil von $s_+$ sind wieder Hilbert-Transformierte voneinander.

**Der Hilbert-Transformator.** Das LTI-System mit $h(t)=\frac{1}{\pi t}$ hat $H(f)=-\mathrm{j}\operatorname{sgn}(f)$: Betrag 1 bei allen Frequenzen (ein __Allpass__), Phase $-90^\circ$ für $f>0$ und $+90^\circ$ für $f<0$. Aus $\cos(2\pi Ft)$ macht er

$$\tfrac12\bigl[\delta(f+F)+\delta(f-F)\bigr]\cdot\bigl(-\mathrm{j}\operatorname{sgn}(f)\bigr)=\tfrac{\mathrm{j}}{2}\delta(f+F)-\tfrac{\mathrm{j}}{2}\delta(f-F)\;\bullet\!\!-\!\!\circ\;\sin(2\pi Ft).$$

⁠**Kurz gesagt:** Der Hilbert-Transformator dreht jede Schwingung um $90^\circ$, ohne ihre Amplitude zu ändern.

:::aufgabe Aufgabe 12 ★★ Hilbert-Transformator
<span class="anker" id="aufg-12"></span>

<ol class="al">

<li>

Was macht der Hilbert-Transformator aus $\sin(2\pi Ft)$? Was ergibt zweimaliges Anwenden?

</li>

<li>

Bestimme die analytische Komponente $s_+(t)$ von $\cos(2\pi Ft)$ und prüfe $s=2\operatorname{Re}\{s_+\}$.

</li>

<li>

Warum ist der Hilbert-Transformator nicht kausal? Schau auf $h(t)$.

</li>

</ol>

:::loesung
(a) $\sin(2\pi Ft)\circ\!\!-\!\!\bullet\frac{\mathrm{j}}{2}\delta(f+F)-\frac{\mathrm{j}}{2}\delta(f-F)$. Multiplikation mit $-\mathrm{j}\operatorname{sgn}(f)$: bei $-F$ mit $+\mathrm{j}$, bei $+F$ mit $-\mathrm{j}$. Ergebnis $-\frac12\delta(f+F)-\frac12\delta(f-F)$, also $-\cos(2\pi Ft)$. Zweimal angewandt: $(-\mathrm{j}\operatorname{sgn}f)^2=-1$, das Signal wird invertiert.

(b) $S_+(f)=S(f)\varepsilon(f)=\frac12\delta(f-F)$, also $s_+(t)=\frac12\mathrm{e}^{\mathrm{j}2\pi Ft}=\frac12\bigl[\cos(2\pi Ft)+\mathrm{j}\sin(2\pi Ft)\bigr]$. Das passt zu $\frac12(s+\mathrm{j}\hat s)$ mit $\hat s=\sin$. $2\operatorname{Re}\{s_+\}=\cos(2\pi Ft)$.

(c) $h(t)=\frac{1}{\pi t}$ ist auch für $t<0$ von null verschieden. Der Ausgang zur Zeit $t$ hängt also von zukünftigen Eingangswerten ab. In der Praxis nähert man den Hilbert-Transformator mit einer abgeschnittenen Impulsantwort und nimmt dafür eine Verzögerung in Kauf.
:::
:::

## Stufe 10: Kurzzeit-Fourier-Transformation

<span class="anker" id="stufe-10"></span>

:::zweck
Das Spektrum $S(f)$ beschreibt ein Signal über alle Zeiten. Sprache oder Musik ändern ihre Frequenzen aber laufend. Die Kurzzeit-Fourier-Transformation fragt: Welche Frequenzen enthält das Signal *um den Zeitpunkt $t$*?
:::

**Die Idee.** Man schneidet um $t$ einen Ausschnitt heraus und transformiert nur ihn. Mit einem Rechteckfenster der Breite $T_0$:

$$s_T(\tau,t)=s(\tau)\operatorname{rect}\Bigl(\frac{\tau-t}{T_0}\Bigr)\;\circ\!\!-\!\!\bullet\;S_T(f,t)=S(f)*\bigl[T_0\operatorname{si}(\pi T_0f)\,\mathrm{e}^{-\mathrm{j}2\pi tf}\bigr].$$

Das Spektrum des Ausschnitts ist das wahre Spektrum, verschmiert mit dem si-Spektrum des Fensters. Ein kurzes Fenster lokalisiert gut in der Zeit, verschmiert aber stark in der Frequenz (Ähnlichkeitssatz). Die harten Kanten des Rechtecks erzeugen zudem langsam abfallende Nebenzipfel. Weiche Fenster sind deshalb besser, zum Beispiel das __Hann-Fenster__

<span class="anker" id="gl-10-1"></span>
$$w(\tau)=\tfrac12\Bigl[1+\cos\Bigl(\frac{2\pi\tau}{T_0}\Bigr)\Bigr]\operatorname{rect}\Bigl(\frac{\tau}{T_0}\Bigr)=\cos^2\Bigl(\frac{\pi\tau}{T_0}\Bigr)\operatorname{rect}\Bigl(\frac{\tau}{T_0}\Bigr). \tag{10.1}$$

:::satz Satz 10.1 (Kurzzeit-Fourier-Transformation)
<span class="anker" id="satz-10-1"></span>

<span class="anker" id="gl-10-2"></span>
$$S_T(f,t)=\int_{-\infty}^{\infty}s(\tau)\,w(\tau-t)\,\mathrm{e}^{-\mathrm{j}2\pi f\tau}\,\mathrm{d}\tau. \tag{10.2}$$

Ergänzen sich die um $T$ verschobenen Fenster zu einer Konstanten, $\sum_nw(\tau-nT)=c$, dann gilt

<span class="anker" id="gl-10-3"></span>
$$s(\tau)=\frac1c\sum_ns(\tau)\,w(\tau-nT),\qquad S(f)=\frac1c\sum_nS_T(f,nT). \tag{10.3}$$
:::

⁠**So liest man das:** $S_T(f,t)$ ist ein Spektrum, das von der Zeit abhängt. Trägt man $|S_T|$ über $t$ und $f$ auf, entsteht ein __Spektrogramm__. Beim Hann-Fenster mit dem Versatz $T=T_0/2$ ist $c=1$, weil $\cos^2x+\sin^2x=1$ ist (Abb. [8](#abb-8)): Die Ausschnitte setzen sich lückenlos zum ganzen Signal zusammen, und die Summe ihrer Spektren ist das ganze Spektrum.

:::abbildung et3/k3hann
Hann-Fenster der Breite $T_0=2$ s, jeweils um $T=1$ s versetzt (blau). Ihre Summe ist überall genau 1 (rot).
:::

:::aufgabe Aufgabe 13 ★ Hann-Fenster
<span class="anker" id="aufg-13"></span>

Zeige: Für $T=T_0/2$ ist $\sum_nw(\tau-nT)=1$. Tipp: In jedem Punkt überlappen genau zwei Fenster. Schreibe das zweite mit $\cos^2(x-\frac\pi2)$.

:::loesung
Für $\tau$ zwischen $nT$ und $(n+1)T$ mit $T=T_0/2$ sind genau die Fenster $n$ und $n+1$ von null verschieden. Mit $x=\pi(\tau-nT)/T_0$:

$$w(\tau-nT)+w(\tau-(n+1)T)=\cos^2x+\cos^2\Bigl(x-\frac\pi2\Bigr)=\cos^2x+\sin^2x=1.$$
:::
:::

## Stufe 11: Fourier und Laplace, Grenzen der Existenz

<span class="anker" id="stufe-11"></span>

:::zweck
Wann existiert das Fourier-Integral, und wie hängt es mit der Laplace-Transformation zusammen?
:::

Hinreichend für die Existenz ist absolute Integrierbarkeit, $\int|s(t)|\mathrm{d} t<\infty$. Die Laplace-Transformation erweitert die Klasse, indem sie vorher mit $\mathrm{e}^{-\sigma t}$ gewichtet ([Teil 2](/wissen/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html)):

$$S_{\mathcal{L}}(\sigma+\mathrm{j}2\pi f)=\mathcal{F}\bigl\{s(t)\mathrm{e}^{-\sigma t}\bigr\}(f).$$

Sie untersucht ein Signal also auf zweierlei: auf Frequenzanteile wie die Fourier-Transformation und auf exponentielles Wachsen oder Abklingen. Liegt $\sigma=0$ im Konvergenzbereich, ist die Fourier-Transformierte die Laplace-Transformierte auf der imaginären Achse. Mit Dirac-Impulsen (Stufe [8](#stufe-8)) fasst die Fourier-Transformation aber auch Signale, die die Laplace-Transformation nicht fasst: Konstanten und Schwingungen über alle Zeiten. Allgemein genügt es, dass $\int|s(t)|\mathrm{e}^{-c|t|}\mathrm{d} t<\infty$ für jedes $c>0$ gilt. Dann darf das Signal wie eine Potenz $t^n$ wachsen, aber nicht exponentiell.

:::zusatz Warum Mehrfachfaltungen gaußförmig werden
Faltet man $M$ Rechtecke $\operatorname{rect}(t)$ miteinander, ist das Spektrum $\operatorname{si}^M(\pi f)$. Für kleine $f$ ist $\operatorname{si}(\pi f)\approx1-\frac{(\pi f)^2}{6}$ und $\ln(1+w)\approx w$, also

$$\operatorname{si}^M(\pi f)=\mathrm{e}^{M\ln\operatorname{si}(\pi f)}\approx\mathrm{e}^{-M(\pi f)^2/6}\;\bullet\!\!-\!\!\circ\;\sqrt{\frac{6}{\pi M}}\,\mathrm{e}^{-6t^2/M}.$$

Für große $M$ trägt nur der Bereich kleiner $f$ bei, die Näherung wird immer besser. Bei $M=4$ ist der Wert bei $t=0$ exakt $0{,}667$, die Gaußkurve gibt $0{,}691$. Das ist ein Fall des __zentralen Grenzwertsatzes__ (Teil zur Statistik): Die Faltung vieler positiver Impulse endlicher Fläche nähert sich einer Gaußkurve. Ein Beispiel ist die Impulsantwort einer Kette vieler kurzer Integratoren.
:::

:::aufgabe Aufgabe 14 ★★★ (Vertiefung) Die Gaußnäherung prüfen
<span class="anker" id="aufg-14"></span>

<ol class="al">

<li>

Vergleiche für $M=2$ den exakten Wert $\Lambda(0)=1$ mit der Gaußnäherung.

</li>

<li>

Zeige, dass die Gaußkurve $\sqrt{6/(\pi M)}\,\mathrm{e}^{-6t^2/M}$ die Fläche 1 hat. Warum muss das so sein?

</li>

</ol>

:::loesung
(a) $M=2$: $\sqrt{6/(2\pi)}=0{,}977$ statt $\Lambda(0)=1$, also 2,3 % zu wenig. Bei $M=4$: 0,691 statt 0,667, also 3,6 % zu viel. Schon nach wenigen Faltungen liegt die Gaußkurve also nahe am exakten Ergebnis. Beliebig gut wird die Näherung erst für große $M$, weil erst dann nur noch kleine $f$ zum Spektrum beitragen.

(b) $\int\mathrm{e}^{-6t^2/M}\mathrm{d} t=\sqrt{\pi M/6}$, mal $\sqrt{6/(\pi M)}$ ergibt 1. Das muss so sein: Die Fläche einer Faltung ist das Produkt der Flächen, hier $1^M=1$. Im Spektrum ist das der Wert bei $f=0$, $\operatorname{si}^M(0)=1$, und die Näherung $\mathrm{e}^{-M(\pi f)^2/6}$ hat dort ebenfalls 1.
:::
:::

:::kern Das Wichtigste
<ul>

<li>

$\mathrm{e}^{\mathrm{j}2\pi ft}*h=H(f)\mathrm{e}^{\mathrm{j}2\pi ft}$; $H(f)=\int h\,\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t$.

</li>

<li>

Reihe: $s_p=\sum S_p(k)\mathrm{e}^{\mathrm{j}2\pi kFt}$, $S_p(k)=\frac1T\int_Ts_p\mathrm{e}^{-\mathrm{j}2\pi kFt}\mathrm{d} t$; reell: $S_p(-k)=S_p^*(k)$.

</li>

<li>

Parseval: $\frac1T\int_T|s_p|^2=\sum|S_p(k)|^2$; Gibbs: etwa 9 % Überschwingen an Sprüngen; LTI: $G_p(k)=S_p(k)H(kF)$.

</li>

<li>

$S(f)=\int s\,\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t$, $s=\int S\mathrm{e}^{\mathrm{j}2\pi ft}\mathrm{d} f$; $s*h\leftrightarrow SH$, $s_1s_2\leftrightarrow S_1*S_2$.

</li>

<li>

Reell: $S(-f)=S^*(f)$; gerade $\leftrightarrow\operatorname{Re} S$, ungerade $\leftrightarrow\mathrm{j}\operatorname{Im} S$.

</li>

<li>

$s(bt)\leftrightarrow\frac1{|b|}S(f/b)$; $s(t-t_0)\leftrightarrow S\mathrm{e}^{-\mathrm{j}2\pi ft_0}$; $\frac{\mathrm{d}}{\mathrm{d} t}\leftrightarrow\mathrm{j}2\pi f$; $\mathrm{e}^{\mathrm{j}2\pi Ft}s\leftrightarrow S(f-F)$; $S(t)\leftrightarrow s(-f)$.

</li>

<li>

$\operatorname{rect}(t/T)\leftrightarrow|T|\operatorname{si}(\pi Tf)$; $\Lambda\leftrightarrow\operatorname{si}^2$; $\delta\leftrightarrow1$; $1\leftrightarrow\delta(f)$; $\cos\leftrightarrow\frac12[\delta(f+F)+\delta(f-F)]$.

</li>

<li>

Kamm $\leftrightarrow$ Kamm: $\sum\delta(t-nT)\leftrightarrow\frac1{|T|}\sum\delta(f-k/T)$; $\varepsilon\leftrightarrow\frac12\delta(f)+\frac{1}{\mathrm{j}2\pi f}$.

</li>

<li>

Hilbert: $h=\frac{1}{\pi t}$, $H=-\mathrm{j}\operatorname{sgn}(f)$; $s_+=\frac12(s+\mathrm{j}\hat s)$, $s=2\operatorname{Re} s_+$.

</li>

</ul>
:::

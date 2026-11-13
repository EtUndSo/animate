---
title: Stufe 3: Leistung, Konvergenz und LTI-Systeme
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Fourier-Reihe und -Transformation
adresse: elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation
knoten: Kapitel 3: Fourier-Reihe und -Transformation
order: 3230400
summary: Wie viel trägt jede Harmonische zum Signal bei, wie gut nähert eine abgebrochene Reihe das Signal, und was macht ein LTI-System mit einem periodischen Eingang?
tags: Leistung, Teilsumme, Gibbs-Phänomen
lang: de
---

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
$|s_p|^2=s_ps_p^*=\sum_k\sum_lS_p(k)S_p^*(l)\,\mathrm{e}^{\mathrm{j}2\pi(k-l)Ft}$. Über eine Periode gemittelt bleibt nach [(2.4)](periodische-signale-die-fourier-reihe.html#gl-2-4) nur $k=l$: $\sum_k|S_p(k)|^2$.
:::

**Abgebrochene Reihe und Gibbs-Phänomen.** Nimmt man nur die Harmonischen bis $|k|\le N$, ist die __Teilsumme__ $s_{p,N}(t)=\sum_{k=-N}^{N}S_p(k)\mathrm{e}^{\mathrm{j}2\pi kFt}$. Die Leistung des Fehlers $s_p-s_{p,N}$ ist die Summe der weggelassenen $|S_p(k)|^2$ und geht für $N\to\infty$ gegen null, wenn das Signal eine endliche Leistung hat. An einer Sprungstelle bleibt aber ein Überschwinger stehen (Abb. [2](#abb-2)): Er wird mit wachsendem $N$ schmaler, seine Höhe strebt aber gegen etwa 9 % der Sprunghöhe (10,0 % bei $N=3$, 9,1 % bei $N=9$, 9,0 % bei $N=27$, Grenzwert 8,95 %). Das ist das __Gibbs-Phänomen__. Es widerspricht der Konvergenz nicht: Die Fläche unter dem Überschwinger und damit die Fehlerleistung geht trotzdem gegen null.

:::abbildung et3/k3gibbs 2
Teilsummen der Rechteckschwingung ($T=2\pi$ s) mit den Harmonischen bis $|k|\le N$. An den Kanten bleibt ein Überschwinger von etwa 9 % der Sprunghöhe, der mit wachsendem $N$ nur schmaler wird.
:::

**Periodischer Eingang an einem LTI-System.** Jede Harmonische ist eine Eigenfunktion und wird mit $H(kF)$ multipliziert. Der Ausgang hat deshalb dieselbe Periode, und seine Koeffizienten sind

<span class="anker" id="gl-3-2"></span>
$$G_p(k)=S_p(k)\,H(kF). \tag{3.2}$$

Im Rechenmodell ist $H(kF)=1/(1+\mathrm{j} k)$. Die Grundschwingung wird mit $|H|=0{,}707$ und $-45^\circ$ übertragen, die dritte Harmonische mit $0{,}316$ und $-71{,}6^\circ$, die fünfte mit $0{,}196$ und $-78{,}7^\circ$. Am Ausgang ist die dritte Harmonische nur noch 15 % so groß wie die erste statt 33 % am Eingang. Das RC-Glied rundet die Kanten ab (Abb. [3](#abb-3)). Der Ausgang pendelt zwischen 0,041 und 0,959.

:::abbildung et3/k3rc 3
Rechteckschwingung durch den RC-Tiefpass mit $RC=1$ s, berechnet als Summe der Harmonischen mit $G_p(k)=S_p(k)/(1+\mathrm{j} k)$. Der Ausgang lädt und entlädt sich exponentiell zwischen 0,041 und 0,959.
:::

:::frage Ist eine Rechnung über unendlich viele Harmonische nicht viel umständlicher als die Differentialgleichung?
Für eine einzelne Rechteckschwingung durch ein RC-Glied ja: Lade- und Entladekurve kann man direkt hinschreiben. Die Reihe zeigt dafür, *warum* der Ausgang so aussieht. Die Kanten bestehen aus den hohen Harmonischen, und genau diese schwächt das RC-Glied. Außerdem funktioniert [(3.2)](#gl-3-2) für jedes LTI-System, auch für solche, deren Differentialgleichung man gar nicht kennt, sondern nur ihren gemessenen Frequenzgang.
:::

:::ltspice Rechteckschwingung durch das RC-Glied
⁠**Zeichnen:** RC-Glied (`res` mit `1Meg`, `cap` mit `1u`) mit der Quelle `PULSE(0 1 0 1u 1u {pi} {2*pi})`: Periode $2\pi$ s, Tastgrad $\frac12$.

⁠**Direktiven:** `.tran 0 {20*pi} 0 1m`, `.four {1/(2*pi)} 5 V(in) V(out)` und `.options plotwinsize=0`. Die letzte schaltet die Datenkompression ab, ohne sie rechnet `.four` ungenau. `.four` zerlegt die letzte Periode in Harmonische und schreibt das Ergebnis ins SPICE Error Log.

⁠**Was du siehst:** Im eingeschwungenen Zustand pendelt `V(out)` zwischen 0,041 und 0,959. `.four` gibt für $k\ge1$ die Amplituden $2|S_p(k)|$ der Kosinusschwingungen in [(2.2)](periodische-signale-die-fourier-reihe.html#gl-2-2) an. Am Eingang sind das 0,637; 0; 0,212; 0; 0,127: Die geraden Harmonischen fehlen. Am Ausgang ist die dritte Harmonische nur noch 15 % so groß wie die erste statt 33 %. Die Phasen am Ausgang sind um $45^\circ$, $71{,}6^\circ$ und $78{,}7^\circ$ größer als am Eingang, denn `.four` zählt eine Nacheilung positiv. Halbiere die Ausgangsamplituden und vergleiche mit deinem Ergebnis aus Aufgabe [3](#aufg-3)(b). Die FFT-Ansicht (Rechtsklick ins Diagramm, View, FFT) zeigt dieselben Linien bei den ungeraden Vielfachen von 0,159 Hz.
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

::::kurzfassung
Weil die Harmonischen orthogonal sind, lassen sich drei Fragen Harmonische für Harmonische beantworten: wie viel Leistung jede trägt, wie gut eine abgebrochene Reihe das Signal nähert und was ein LTI-System mit einem periodischen Eingang macht.

Die mittlere __Leistung__ $L_s$ ist der Mittelwert von $|s_p(t)|^2$ über eine Periode. Der Satz von Parseval verteilt sie auf die Harmonischen:

$$L_s=\frac1T\int_0^T|s_p(t)|^2\,\mathrm{d} t=\sum_{k=-\infty}^{\infty}|S_p(k)|^2.$$

Die __Teilsumme__ $s_{p,N}(t)$ enthält nur die Harmonischen mit $|k|\le N$. Die Leistung ihres Fehlers ist die Summe der weggelassenen $|S_p(k)|^2$ und geht für $N\to\infty$ gegen null. In diesem Sinn stellt die Reihe das Signal dar. Ein LTI-System mit dem Frequenzgang $H(f)$ multipliziert jede Harmonische mit $H(kF)$. Der Ausgang hat dieselbe Periode und die Koeffizienten $G_p(k)=S_p(k)\,H(kF)$.

Der Grund: In $|s_p|^2$ entstehen Mischterme aus zwei verschiedenen Harmonischen; über eine Periode gemittelt verschwinden sie wegen der Orthogonalität. Im LTI-System ist jede Harmonische eine Eigenfunktion und wird für sich übertragen. Ein Tiefpass schwächt deshalb die hohen Harmonischen, aus denen die Kanten bestehen, und rundet die Kanten ab.

Falle: An einer Sprungstelle bleibt ein Überschwinger stehen, das __Gibbs-Phänomen__. Er wird mit wachsendem $N$ nur schmaler, nicht niedriger; seine Höhe strebt gegen 8,95 % der Sprunghöhe. Das widerspricht der Konvergenz nicht, denn seine Fläche und damit die Fehlerleistung gehen gegen null. Die Reihe nähert das Signal im Mittel, aber nicht in jedem Punkt gleich gut.
::::

::::formelsammlung
**Parseval für Fourier-Reihen**

$$L_s=\frac1T\int_0^T|s_p(t)|^2\,\mathrm{d} t=\sum_{k=-\infty}^{\infty}|S_p(k)|^2$$

Mittlere Leistung gleich Summe der Leistungen der Harmonischen; die Mischterme verschwinden wegen der Orthogonalität.

**Teilsumme**

$$s_{p,N}(t)=\sum_{k=-N}^{N}S_p(k)\mathrm{e}^{\mathrm{j}2\pi kFt}$$

Nur die Harmonischen mit $|k|\le N$. An Sprungstellen bleibt ein Überschwinger (Gibbs-Phänomen); seine Höhe strebt für $N\to\infty$ gegen 8,95 % der Sprunghöhe, er wird nur schmaler.

**Fehlerleistung der Teilsumme**

$$\frac1T\int_0^T|s_p(t)-s_{p,N}(t)|^2\,\mathrm{d} t=\sum_{|k|>N}|S_p(k)|^2$$

Summe der weggelassenen $|S_p(k)|^2$; geht für $N\to\infty$ gegen null, wenn das Signal endliche Leistung hat. In diesem Sinn stellt die Reihe das Signal dar, nicht unbedingt in jedem Punkt.

**LTI-System mit periodischem Eingang**

$$G_p(k)=S_p(k)\,H(kF)$$

$G_p(k)$ Fourier-Koeffizienten des Ausgangs, $H(f)$ Frequenzgang. Der Ausgang hat dieselbe Periode wie der Eingang.
::::

::::lernkarten
:::karte begriff Leistung
Was versteht man unter der mittleren Leistung $L_s$ eines periodischen Signals $s_p(t)$?
---
Den Mittelwert des Betragsquadrats über eine Periode: $L_s=\frac1T\int_0^T|s_p(t)|^2\,\mathrm{d} t$. Ist er endlich, hat das Signal eine endliche Leistung, und die Fourier-Reihe stellt es im quadratischen Mittel dar.
--- falsch
Den Mittelwert des Signals selbst über eine Periode: $L_s=\frac1T\int_0^Ts_p(t)\,\mathrm{d} t$. Ist er endlich, hat das Signal eine endliche Leistung, und die Fourier-Reihe stellt es in jedem Punkt dar.
--- falsch
Das Integral des Betragsquadrats über alle Zeiten: $L_s=\int_{-\infty}^{\infty}|s_p(t)|^2\,\mathrm{d} t$. Bei einem periodischen Signal ist es immer endlich, weil sich das Signal ständig wiederholt.
--- falsch
Den größten Wert von $|s_p(t)|^2$ in einer Periode, also das Quadrat der Spitzenamplitude. Ist er endlich, hat das Signal eine endliche Leistung, und die Fourier-Reihe stellt es in jedem Punkt dar.
:::
:::karte formel Parseval für Fourier-Reihen
Wie verteilt sich nach dem Satz von Parseval die mittlere Leistung eines periodischen Signals auf seine Harmonischen?
---
$L_s=\frac1T\int_0^T|s_p(t)|^2\,\mathrm{d} t=\sum_{k=-\infty}^{\infty}|S_p(k)|^2$: Die Leistung ist die Summe der Leistungen der einzelnen Harmonischen. Mischterme fallen weg, weil verschiedene Harmonische orthogonal sind.
--- falsch
$L_s=\frac1T\int_0^T|s_p(t)|^2\,\mathrm{d} t=\Bigl|\sum_{k=-\infty}^{\infty}S_p(k)\Bigr|^2$: Man addiert erst alle Koeffizienten und quadriert dann den Betrag der Summe, weil sich die Harmonischen im Signal zu einer einzigen Kurve überlagern.
--- falsch
$L_s=\frac1T\int_0^T|s_p(t)|^2\,\mathrm{d} t=\sum_{k=-\infty}^{\infty}|S_p(k)|$: Die Leistung ist die Summe der Beträge der Koeffizienten, weil jede Harmonische mit ihrer Amplitude zur Leistung beiträgt, nicht mit deren Quadrat.
--- falsch
$L_s=\frac1T\int_0^T|s_p(t)|^2\,\mathrm{d} t=\sum_{k=1}^{\infty}|S_p(k)|^2$: Die Leistung ist die Summe über die positiven Harmonischen; der Gleichanteil und die negativen $k$ tragen keine Leistung.
:::
:::karte herleitung Parseval aus der Orthogonalität
Wie folgt aus der Fourier-Reihe und der Orthogonalität der Harmonischen, dass $\frac1T\int_0^T|s_p(t)|^2\,\mathrm{d} t=\sum_{k=-\infty}^{\infty}|S_p(k)|^2$ ist?
---
Man schreibt das Betragsquadrat als Produkt mit dem konjugierten Signal, weil das Betragsquadrat einer komplexen Zahl das Produkt mit ihrer konjugierten ist.
---
Für beide Faktoren setzt man die Reihe ein, und es entsteht eine Doppelsumme, weil jede Harmonische mit jeder anderen multipliziert wird: $|s_p|^2=s_ps_p^*=\sum_k\sum_lS_p(k)S_p^*(l)\,\mathrm{e}^{\mathrm{j}2\pi(k-l)Ft}$.
---
Man mittelt über eine Periode, weil die mittlere Leistung genau dieser Mittelwert ist.
---
Es bleibt nur $k=l$ übrig, weil der Mittelwert von $\mathrm{e}^{\mathrm{j}2\pi(k-l)Ft}$ nach der Orthogonalität für verschiedene $k$ und $l$ null und für $k=l$ eins ist. Das Ergebnis ist $\sum_k|S_p(k)|^2$.
:::
:::karte begriff Teilsumme
Was ist die Teilsumme $s_{p,N}(t)$ einer Fourier-Reihe, und wie groß ist die Leistung ihres Fehlers?
---
Die abgebrochene Reihe aus den Harmonischen mit $|k|\le N$: $s_{p,N}(t)=\sum_{k=-N}^{N}S_p(k)\mathrm{e}^{\mathrm{j}2\pi kFt}$. Die Leistung des Fehlers $s_p-s_{p,N}$ ist die Summe der weggelassenen $|S_p(k)|^2$.
--- falsch
Die abgebrochene Reihe aus den Harmonischen mit $0\le k\le N$: $s_{p,N}(t)=\sum_{k=0}^{N}S_p(k)\mathrm{e}^{\mathrm{j}2\pi kFt}$. Die Leistung des Fehlers ist das Betragsquadrat des ersten weggelassenen Koeffizienten.
--- falsch
Die abgebrochene Reihe aus den Harmonischen mit $|k|\le N$: $s_{p,N}(t)=\sum_{k=-N}^{N}S_p(k)\mathrm{e}^{\mathrm{j}2\pi kFt}$. Die Leistung des Fehlers ist die Summe der Beträge $|S_p(k)|$ der weggelassenen Koeffizienten.
--- falsch
Die Summe der ersten $N$ Abtastwerte des Signals in einer Periode, gleichmäßig verteilt. Die Leistung des Fehlers ist der Abstand zwischen dem letzten Abtastwert und dem Mittelwert, zum Quadrat genommen.
:::
:::karte begriff Gibbs-Phänomen
Was beschreibt das Gibbs-Phänomen bei den Teilsummen der Fourier-Reihe eines Signals mit Sprungstelle?
---
Den Überschwinger, der an einer Sprungstelle stehen bleibt. Mit wachsendem $N$ wird er nur schmaler, seine Höhe strebt gegen etwa 9 % der Sprunghöhe (Grenzwert 8,95 %).
--- falsch
Den Überschwinger an einer Sprungstelle, der mit wachsendem $N$ immer niedriger wird. Seine Höhe nimmt etwa wie $1/N$ ab und liegt bei $N=27$ schon unter 1 % der Sprunghöhe.
--- falsch
Das Schwingen der Teilsumme zwischen den Sprungstellen, das mit wachsendem $N$ immer stärker wird. Die Reihe nähert das Signal deshalb nur für kleine $N$ gut und weicht für große $N$ wieder ab.
--- falsch
Den Überschwinger, der an einer Sprungstelle stehen bleibt. Mit wachsendem $N$ wird er nur schmaler, seine Höhe strebt aber gegen die halbe Sprunghöhe, also gegen 50 %.
:::
:::karte zusammenhang Gibbs-Phänomen und Konvergenz
Warum widerspricht der stehende Überschwinger an einer Sprungstelle nicht der Aussage, dass die Fourier-Reihe gegen das Signal konvergiert?
---
Die Reihe konvergiert im quadratischen Mittel, also in der Fehlerleistung. Der Überschwinger wird mit wachsendem $N$ immer schmaler. Seine Fläche und damit die Fehlerleistung gehen gegen null, auch wenn seine Höhe bleibt.
--- falsch
Weil die Reihe in jedem Punkt konvergiert und der Überschwinger nur bei endlichem $N$ auftritt. Für $N\to\infty$ verschwindet er in einem einzigen Schritt, sodass seine Höhe am Ende doch null ist.
--- falsch
Weil der Überschwinger genau auf der Sprungstelle liegt, wo das Signal ohnehin keinen festen Wert hat. Außerhalb dieses einen Punktes stimmt die Teilsumme schon bei endlichem $N$ exakt mit dem Signal überein.
--- falsch
Die Reihe konvergiert im quadratischen Mittel. Der Überschwinger wird zwar nicht schmaler, aber seine Höhe ist mit 9 % so klein, dass seine Leistung gegenüber der Signalleistung nicht ins Gewicht fällt.
:::
:::karte formel LTI-System mit periodischem Eingang
Welche Fourier-Koeffizienten $G_p(k)$ hat der Ausgang eines LTI-Systems mit dem Frequenzgang $H(f)$, wenn der periodische Eingang die Koeffizienten $S_p(k)$ hat?
---
$G_p(k)=S_p(k)\,H(kF)$. Jede Harmonische ist eine Eigenfunktion und wird mit dem Frequenzgang bei ihrer Frequenz $kF$ multipliziert. Der Ausgang hat deshalb dieselbe Periode wie der Eingang.
--- falsch
$G_p(k)=S_p(k)\,H(F)$ für alle $k$. Das System sieht nur die Grundfrequenz, weil sich das ganze Signal mit ihr wiederholt; alle Harmonischen erhalten deshalb denselben Faktor.
--- falsch
$G_p(k)=S_p(k)*H(kF)$, die Faltung von Eingangskoeffizienten und Frequenzgang. Der Ausgang hat deshalb mehr Harmonische als der Eingang und im Allgemeinen eine längere Periode.
--- falsch
$G_p(k)=S_p(k)+H(kF)$. Jede Harmonische ist eine Eigenfunktion, und das System addiert zu ihr den Frequenzgang bei ihrer Frequenz. Der Ausgang hat dieselbe Periode wie der Eingang.
:::
:::karte zusammenhang RC-Tiefpass rundet die Kanten
Warum sieht die Rechteckschwingung des Rechenmodells nach dem RC-Tiefpass mit $H(kF)=1/(1+\mathrm{j} k)$ sinusähnlicher aus als am Eingang?
---
Wegen $|H(kF)|=1/\sqrt{1+k^2}\approx1/k$ werden die Oberschwingungen umso stärker geschwächt, je höher sie sind, und gerade sie bilden die Kanten. Übrig bleibt vor allem die Grundschwingung: Die dritte Harmonische ist am Ausgang nur noch 15 % so groß wie die erste statt 33 %.
--- falsch
Weil der RC-Tiefpass die Grundschwingung verstärkt und die Oberschwingungen unverändert lässt. Dadurch wird die Grundschwingung im Verhältnis größer; am Ausgang ist sie etwa dreimal so stark wie am Eingang, die Kanten treten dagegen zurück.
--- falsch
Weil der RC-Tiefpass die Phasen aller Harmonischen gleich macht. Liegen alle Harmonischen in Phase, addieren sie sich zu einer sinusähnlichen Kurve; die Amplituden der Harmonischen bleiben dabei unverändert, nur ihre Lage ändert sich.
--- falsch
Wegen $|H(kF)|=1/(1+k^2)$ werden nur die geraden Harmonischen geschwächt, die ungeraden bleiben erhalten. Da die Kanten aus den geraden Harmonischen bestehen, werden sie abgerundet, und die Grundschwingung bleibt unverändert stehen.
:::
:::karte zusammenhang Reihe statt Differentialgleichung
Wozu rechnet man einen periodischen Eingang über seine Harmonischen, obwohl man beim RC-Glied Lade- und Entladekurve direkt hinschreiben kann?
---
Die Reihe zeigt, warum der Ausgang so aussieht: Die Kanten bestehen aus den hohen Harmonischen, und genau diese schwächt das RC-Glied. Außerdem gilt $G_p(k)=S_p(k)\,H(kF)$ für jedes LTI-System, auch wenn man nur seinen gemessenen Frequenzgang kennt.
--- falsch
Weil die Reihe genauer ist: Die Lade- und Entladekurve ist nur eine Näherung für kleine Zeitkonstanten, während die Summe der Harmonischen den Ausgang für jedes $RC$ exakt liefert, und zwar schon mit wenigen Gliedern.
--- falsch
Weil die Differentialgleichung für periodische Eingänge keine Lösung hat. Sie gilt nur für einmalige Signale wie den Sprung, sodass man bei periodischen Signalen auf die Fourier-Reihe ausweichen muss, um überhaupt etwas zu erhalten.
--- falsch
Weil die Reihe weniger Rechenaufwand braucht: Schon die Grundschwingung allein gibt den Ausgang exakt wieder, denn alle Oberschwingungen werden vom RC-Glied vollständig gesperrt und tragen zum Ausgang nichts bei.
:::
::::

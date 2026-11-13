---
title: Stufe 12: Zeitdiskrete Zufallssignale
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Zufallssignale
adresse: elektrotechnik/3-semester/signale-und-systeme/zufallssignale
knoten: Kapitel 7: Zufallssignale
order: 3271300
summary: Alles gilt auch für Folgen von Zufallszahlen, mit Summen statt Integralen.
tags: Zeitdiskretes weißes Rauschen
lang: de
---

<span class="anker" id="stufe-12"></span>

:::zweck
Alles gilt auch für Folgen von Zufallszahlen, mit Summen statt Integralen.
:::

Tastet man einen auf $f_\mathrm g$ bandbegrenzten Prozess mit $T\le\frac{1}{2f_\mathrm g}$ ab, bilden die Abtastwerte einen zeitdiskreten Prozess $s(n)$. Verteilungen, Erwartungswerte und Korrelationen sind wie zuvor definiert, die Zeitmittel sind Summen, etwa $\varphi_{ss}(m)=\lim_{M\to\infty}\frac{1}{2M+1}\sum_{n=-M}^{M}s(n)s(n+m)$. Durch ein LSI-System mit $h(n)$:

<span class="anker" id="gl-12-1"></span>
$$m_g=m_s\sum_nh(n),\qquad\varphi_{gg}(m)=\varphi_{ss}(m)*\varphi^E_{hh}(m),\qquad\Phi_{gg,\mathrm a}(f)=\Phi_{ss,\mathrm a}(f)\,|H_\mathrm a(f)|^2, \tag{12.1}$$

mit dem periodischen Leistungsdichtespektrum $\Phi_{ss,\mathrm a}(f)=\sum_m\varphi_{ss}(m)\mathrm{e}^{-\mathrm{j}2\pi fm}$ und $L_s=\int_{-1/2}^{1/2}\Phi_{ss,\mathrm a}\mathrm{d} f$. __Zeitdiskretes weißes Rauschen__ hat $\Phi_{ss,\mathrm a}=N$ und $\varphi_{ss}(m)=N\delta(m)$: Aufeinanderfolgende Zahlen sind unkorreliert. Anders als im Kontinuierlichen ist seine Leistung endlich, $L_s=N$.

::::beispiel [Beispiel 1] Mittelung zweier Werte
Gleichverteiltes weißes Rauschen ($\sigma_s^2=\frac1{12}$) durch $h(n)=\frac12[\delta(n)+\delta(n-1)]$, also $g(n)=\frac12[s(n)+s(n-1)]$. Mit $\varphi^E_{hh}=\frac14\delta(m+1)+\frac12\delta(m)+\frac14\delta(m-1)$:

$$\varphi_{gg}(m)=\tfrac{\sigma_s^2}{4}\delta(m+1)+\tfrac{\sigma_s^2}{2}\delta(m)+\tfrac{\sigma_s^2}{4}\delta(m-1).$$

Die Varianz halbiert sich auf $\frac{1}{24}$, und benachbarte Ausgangswerte sind jetzt korreliert (sie teilen sich einen Eingangswert). Die Ausgangswerte sind dreieckverteilt, weil jeder die halbe Summe zweier unabhängiger, gleichverteilter Zahlen ist. Eine Simulation mit 200 000 Zahlen ergibt die Varianz 0,0415 statt $\frac1{24}=0{,}0417$.
::::

::::beispiel [Beispiel 2] Rekursives Filter (AR(1)-Prozess)
Weißes Rauschen der Varianz $\sigma_s^2$ durch $h(n)=b^n\varepsilon(n)$ ([Kapitel 4](/wissen/elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme/abtastung-und-zeitdiskrete-systeme.html)). Mit $\varphi^E_{hh}(m)=\sum_kb^kb^{k+|m|}=\frac{b^{|m|}}{1-b^2}$:

<span class="anker" id="gl-12-2"></span>
$$\varphi_{gg}(m)=\frac{\sigma_s^2}{1-b^2}\,b^{|m|},\qquad\Phi_{gg,\mathrm a}(f)=\frac{\sigma_s^2}{1-2b\cos(2\pi f)+b^2}. \tag{12.2}$$

Für $b=0{,}6$ ist die Varianz das $1{,}56$-Fache der Eingangsvarianz, und benachbarte Werte haben den Korrelationskoeffizienten $0{,}6$. Je näher $b$ an 1, desto stärker die tiefen Frequenzen (Abb. [5](#abb-5)).

:::abbildung et3/k7ar 5
Leistungsdichtespektren von AR(1)-Prozessen, periodisch mit 1. Bei $b=0{,}6$ reicht es von 6,25 ($f=0$) bis 0,39 ($f=\frac12$), bei $b=0{,}9$ von 100 bis 0,28.
:::
::::

:::aufgabe Aufgabe 12 ★★ AR(1)-Prozess
<span class="anker" id="aufg-12"></span>

Gleichverteiltes weißes Rauschen ($\sigma_s^2=\frac1{12}$) läuft durch $g(n)=s(n)+0{,}6\,g(n-1)$.

<ol class="al">

<li>

Berechne die Ausgangsvarianz und $\varphi_{gg}(1)/\varphi_{gg}(0)$.

</li>

<li>

Leite $\varphi^E_{hh}(m)=\frac{b^{|m|}}{1-b^2}$ mit der geometrischen Reihe her.

</li>

<li>

Ist der Ausgang noch gleichverteilt? Welche Verteilung erwartest du ungefähr, und warum?

</li>

</ol>

:::loesung
(a) $\sigma_g^2=\frac{1/12}{1-0{,}36}=0{,}130$, $\varphi_{gg}(1)/\varphi_{gg}(0)=b=0{,}6$. Die Simulation ergibt 0,130 und 0,600.

(b) Für $m\ge0$: $\sum_{k\ge0}b^kb^{k+m}=b^m\sum_kb^{2k}=\frac{b^m}{1-b^2}$. Die Impuls-AKF ist gerade, also gilt $b^{|m|}$.

(c) Nicht mehr gleichverteilt: Jeder Ausgangswert ist eine gewichtete Summe vieler unabhängiger Eingangswerte, $g(n)=\sum_kb^ks(n-k)$. Nach dem zentralen Grenzwertsatz ist das ungefähr gaußverteilt. Bei $b=0{,}6$ tragen nur wenige Summanden merklich bei, die Näherung ist deshalb grob, aber die Verteilung ist schon deutlich glockenförmig.
:::
:::

::::formelsammlung
**AKF einer Folge als Zeitmittel**

$$\varphi_{ss}(m)=\lim_{M\to\infty}\frac{1}{2M+1}\sum_{n=-M}^{M}s(n)s(n+m)$$

Abtastwerte eines auf $f_\mathrm g$ bandbegrenzten Prozesses mit $T\le\frac{1}{2f_\mathrm g}$; Summen statt Integrale.

**Zufallsfolgen in LSI-Systemen**

$$m_g=m_s\sum_nh(n),\qquad\varphi_{gg}(m)=\varphi_{ss}(m)*\varphi^E_{hh}(m),\qquad\Phi_{gg,\mathrm a}(f)=\Phi_{ss,\mathrm a}(f)\,|H_\mathrm a(f)|^2$$

Dieselben Regeln wie im Zeitkontinuierlichen.

**Periodisches Leistungsdichtespektrum**

$$\Phi_{ss,\mathrm a}(f)=\sum_m\varphi_{ss}(m)\mathrm{e}^{-\mathrm{j}2\pi fm},\qquad L_s=\int_{-1/2}^{1/2}\Phi_{ss,\mathrm a}\mathrm{d} f$$

Periodisch mit 1; die Leistung ist die Fläche über eine Periode.

**Zeitdiskretes weißes Rauschen**

$$\Phi_{ss,\mathrm a}=N,\qquad\varphi_{ss}(m)=N\delta(m),\qquad L_s=N$$

Aufeinanderfolgende Zahlen sind unkorreliert; anders als im Kontinuierlichen ist die Leistung endlich.

**AR(1)-Prozess**

$$\varphi_{gg}(m)=\frac{\sigma_s^2}{1-b^2}\,b^{|m|},\qquad\Phi_{gg,\mathrm a}(f)=\frac{\sigma_s^2}{1-2b\cos(2\pi f)+b^2}$$

Weißes Rauschen der Varianz $\sigma_s^2$ durch $h(n)=b^n\varepsilon(n)$ mit der Impuls-AKF $\varphi^E_{hh}(m)=\frac{b^{|m|}}{1-b^2}$. Je näher $b$ an 1, desto stärker die tiefen Frequenzen.
::::

::::lernkarten
:::karte formel AKF einer Folge als Zeitmittel
Wie berechnet man die AKF eines zeitdiskreten Prozesses $s(n)$ als Zeitmittel über eine Musterfunktion?
---
$\varphi_{ss}(m)=\lim_{M\to\infty}\frac{1}{2M+1}\sum_{n=-M}^{M}s(n)s(n+m)$: Das Integral wird zur Summe, und man teilt durch die Zahl $2M+1$ der Summanden.
--- falsch
$\varphi_{ss}(m)=\sum_{n=-\infty}^{\infty}s(n)s(n+m)$: Man summiert die Produkte über alle $n$, ohne zu teilen, genau wie bei der Energie einer Folge.
--- falsch
$\varphi_{ss}(m)=\lim_{M\to\infty}\frac{1}{2M+1}\sum_{n=-M}^{M}\bigl[s(n)+s(n+m)\bigr]$: Man mittelt die Summe der beiden Werte, weil Produkte von Zufallszahlen nicht definiert sind.
--- falsch
$\varphi_{ss}(m)=\lim_{M\to\infty}\frac{1}{2M}\int_{-M}^{M}s(n)s(n+m)\,\mathrm{d} n$: Man integriert auch bei Folgen über $n$, weil man sich die Abtastwerte durch Geraden verbunden denkt.
:::
:::karte formel Zufallsfolgen in LSI-Systemen
Wie überträgt ein LSI-System mit der Impulsantwort $h(n)$ Mittelwert, AKF und Leistungsdichtespektrum eines zeitdiskreten Prozesses?
---
$m_g=m_s\sum_nh(n)$, $\varphi_{gg}(m)=\varphi_{ss}(m)*\varphi^E_{hh}(m)$ und $\Phi_{gg,\mathrm a}(f)=\Phi_{ss,\mathrm a}(f)\,|H_\mathrm a(f)|^2$: dieselben Regeln wie im Kontinuierlichen, mit Summen statt Integralen.
--- falsch
$m_g=m_s\,h(0)$, $\varphi_{gg}(m)=\varphi_{ss}(m)*h(m)$ und $\Phi_{gg,\mathrm a}(f)=\Phi_{ss,\mathrm a}(f)\,H_\mathrm a(f)$: Bei Folgen gilt Wiener-Lee nicht, und die Phase des Systems geht mit ein.
--- falsch
$m_g=m_s\sum_nh(n)$, $\varphi_{gg}(m)=\varphi_{ss}(m)\,\varphi^E_{hh}(m)$ und $\Phi_{gg,\mathrm a}(f)=\Phi_{ss,\mathrm a}(f)*|H_\mathrm a(f)|^2$: Bei Folgen multipliziert man die AKFs und faltet die Spektren.
--- falsch
$m_g=m_s$, $\varphi_{gg}(m)=\varphi_{ss}(m)*\varphi^E_{hh}(m)$ und $\Phi_{gg,\mathrm a}(f)=\Phi_{ss,\mathrm a}(f)\,|H_\mathrm a(f)|^2$: Ein LSI-System verändert den Mittelwert einer Folge nie, nur ihre Korrelation.
:::
:::karte formel Periodisches Leistungsdichtespektrum
Wie sind das Leistungsdichtespektrum und die Leistung eines zeitdiskreten Prozesses definiert?
---
$\Phi_{ss,\mathrm a}(f)=\sum_m\varphi_{ss}(m)\mathrm{e}^{-\mathrm{j}2\pi fm}$, periodisch mit 1, und $L_s=\int_{-1/2}^{1/2}\Phi_{ss,\mathrm a}\mathrm{d} f$: Die Leistung ist die Fläche über eine Periode des Spektrums.
--- falsch
$\Phi_{ss,\mathrm a}(f)=\sum_m\varphi_{ss}(m)\mathrm{e}^{-\mathrm{j}2\pi fm}$, periodisch mit 1, und $L_s=\int_{-\infty}^{\infty}\Phi_{ss,\mathrm a}\mathrm{d} f$: Die Leistung ist die Fläche über alle Perioden des Spektrums.
--- falsch
$\Phi_{ss,\mathrm a}(f)=\sum_ms(m)\mathrm{e}^{-\mathrm{j}2\pi fm}$, das Spektrum der Folge selbst, und $L_s=\Phi_{ss,\mathrm a}(0)$: Die Leistung ist der Wert dieses Spektrums bei der Frequenz null.
--- falsch
$\Phi_{ss,\mathrm a}(f)=\sum_m\varphi_{ss}(m)\mathrm{e}^{-\mathrm{j}2\pi fm}$, das nicht periodisch ist, und $L_s=\sum_m\varphi_{ss}(m)$: Die Leistung ist die Summe aller Werte der AKF.
:::
:::karte begriff Zeitdiskretes weißes Rauschen
Was versteht man unter zeitdiskretem weißem Rauschen, und welche Leistung hat es?
---
Eine Zufallsfolge mit konstantem Leistungsdichtespektrum $\Phi_{ss,\mathrm a}=N$ und der AKF $\varphi_{ss}(m)=N\delta(m)$: Aufeinanderfolgende Zahlen sind unkorreliert. Anders als im Kontinuierlichen ist seine Leistung endlich, $L_s=N$.
--- falsch
Eine Zufallsfolge mit konstantem Leistungsdichtespektrum $\Phi_{ss,\mathrm a}=N$ und der AKF $\varphi_{ss}(m)=N\delta(m)$. Wie im Kontinuierlichen ist seine Leistung unendlich, weil das Spektrum bei allen Frequenzen gleich $N$ ist.
--- falsch
Eine Zufallsfolge, deren Werte alle gleich groß sind, mit der AKF $\varphi_{ss}(m)=N$ für alle $m$. Ihre Leistung ist $N$, und aufeinanderfolgende Zahlen sind vollständig miteinander korreliert.
--- falsch
Eine Zufallsfolge, deren Werte gleichverteilt sein müssen, mit $\Phi_{ss,\mathrm a}=\frac{1}{12}$. Folgen mit anderen Verteilungen ergeben kein weißes Rauschen, weil ihr Leistungsdichtespektrum nicht flach ist.
:::
:::karte zusammenhang Endliche Leistung im Zeitdiskreten
Warum hat zeitdiskretes weißes Rauschen eine endliche Leistung, kontinuierliches weißes Rauschen aber nicht?
---
Weil das Leistungsdichtespektrum einer Folge periodisch ist und die Leistung $L_s=\int_{-1/2}^{1/2}\Phi_{ss,\mathrm a}\mathrm{d} f$ nur über eine Periode integriert wird; mit $\Phi_{ss,\mathrm a}=N$ ergibt das $L_s=N$. Kontinuierlich läuft $\int N_0\mathrm{d} f$ über alle Frequenzen.
--- falsch
Weil eine Folge nur abzählbar viele Werte hat und jeder Wert eine endliche Leistung beiträgt; im Kontinuierlichen gibt es überabzählbar viele Werte, deren Leistungen sich zu einer unendlichen Summe addieren.
--- falsch
Weil zeitdiskretes Rauschen immer gleichverteilt ist und gleichverteilte Werte beschränkt sind; kontinuierliches Rauschen ist dagegen gaußverteilt und kann deshalb beliebig große Werte annehmen.
--- falsch
Weil das Leistungsdichtespektrum einer Folge oberhalb von $f=\frac12$ von selbst null ist, sodass seine Fläche endlich bleibt, während es im Kontinuierlichen bei allen Frequenzen gleich $N_0$ bleibt.
:::
:::karte zusammenhang Mittelung zweier Werte
Was passiert mit Varianz und Korrelation, wenn gleichverteiltes weißes Rauschen durch $g(n)=\frac12[s(n)+s(n-1)]$ läuft?
---
Die Varianz halbiert sich von $\frac1{12}$ auf $\frac{1}{24}$, und benachbarte Ausgangswerte werden korreliert, weil sie sich einen Eingangswert teilen. Die Ausgangswerte sind dreieckverteilt.
--- falsch
Die Varianz viertelt sich von $\frac1{12}$ auf $\frac{1}{48}$, weil jeder Wert mit $\frac12$ gewichtet wird; die Ausgangswerte bleiben unkorreliert und gleichverteilt.
--- falsch
Die Varianz bleibt $\frac1{12}$, weil sich durch das Mitteln nur der Mittelwert ändert; benachbarte Ausgangswerte sind unkorreliert, weil die Eingangswerte es sind.
--- falsch
Die Varianz halbiert sich auf $\frac{1}{24}$, aber die Ausgangswerte bleiben unkorreliert und gleichverteilt, weil der Mittelwert zweier gleichverteilter Zahlen gleichverteilt ist.
:::
:::karte formel AR(1)-Prozess
Welche AKF und welches Leistungsdichtespektrum hat weißes Rauschen der Varianz $\sigma_s^2$ hinter dem rekursiven Filter $h(n)=b^n\varepsilon(n)$?
---
$\varphi_{gg}(m)=\frac{\sigma_s^2}{1-b^2}\,b^{|m|}$ und $\Phi_{gg,\mathrm a}(f)=\frac{\sigma_s^2}{1-2b\cos(2\pi f)+b^2}$. Je näher $b$ an 1 liegt, desto stärker sind die tiefen Frequenzen vertreten.
--- falsch
$\varphi_{gg}(m)=\sigma_s^2\,b^{m}$ für alle $m$ und $\Phi_{gg,\mathrm a}(f)=\frac{\sigma_s^2}{1-b\cos(2\pi f)}$. Je näher $b$ an 1 liegt, desto stärker sind die hohen Frequenzen vertreten.
--- falsch
$\varphi_{gg}(m)=\frac{\sigma_s^2}{1-b}\,b^{|m|}$ und $\Phi_{gg,\mathrm a}(f)=\frac{\sigma_s^2}{1+2b\cos(2\pi f)+b^2}$. Je näher $b$ an 1 liegt, desto flacher wird das Spektrum.
--- falsch
$\varphi_{gg}(m)=\frac{\sigma_s^2}{1-b^2}\,\delta(m)$ und $\Phi_{gg,\mathrm a}(f)=\frac{\sigma_s^2}{1-b^2}$: Das Filter vergrößert nur die Varianz; der Ausgang bleibt weiß, weil der Eingang weiß ist.
:::
:::karte herleitung Impuls-AKF des rekursiven Filters
Wie folgt mit der geometrischen Reihe die Impuls-AKF $\varphi^E_{hh}(m)=\frac{b^{|m|}}{1-b^2}$ des Filters $h(n)=b^n\varepsilon(n)$, und welche AKF hat damit der Ausgang?
---
Für $m\ge0$ ist die Impuls-AKF die Summe $\sum_{k\ge0}b^kb^{k+m}$, weil man die Impulsantwort mit ihrer um $m$ verschobenen Kopie multipliziert und $h$ erst bei $k=0$ beginnt.
---
Man zieht den Faktor heraus, $\sum_{k\ge0}b^kb^{k+m}=b^m\sum_kb^{2k}$, weil $b^m$ nicht vom Summationsindex $k$ abhängt.
---
Die geometrische Reihe mit dem Quotienten $b^2$ ergibt $\frac{b^m}{1-b^2}$, weil sie bei einem stabilen Filter, also für $b$ zwischen $-1$ und 1, konvergiert.
---
Für negative $m$ gilt dasselbe mit $|m|$, weil die Impuls-AKF gerade ist; so folgt $\varphi^E_{hh}(m)=\frac{b^{|m|}}{1-b^2}$.
---
Mit Wiener-Lee folgt $\varphi_{gg}(m)=\frac{\sigma_s^2}{1-b^2}\,b^{|m|}$, weil die AKF des weißen Eingangs ein mit der Varianz $\sigma_s^2$ gewichteter Einheitsimpuls ist.
:::
:::karte zusammenhang Rekursives System mit dem Faktor 0,6
Wie verändert das rekursive System $g(n)=s(n)+0{,}6\,g(n-1)$ die Varianz von gleichverteiltem weißem Rauschen, und wie stark sind benachbarte Ausgangswerte korreliert?
---
Die Varianz wird das $1{,}56$-Fache der Eingangsvarianz, $\sigma_g^2=\frac{1/12}{1-0{,}36}=0{,}130$. Benachbarte Werte haben den Korrelationskoeffizienten $\varphi_{gg}(1)/\varphi_{gg}(0)=b=0{,}6$.
--- falsch
Die Varianz wird das $0{,}6$-Fache der Eingangsvarianz, weil jeder Wert mit 0,6 gewichtet wird, also etwa 0,05. Benachbarte Werte bleiben unkorreliert, weil der Eingang weiß ist.
--- falsch
Die Varianz wird das $2{,}5$-Fache der Eingangsvarianz, $\sigma_g^2=\frac{1/12}{1-0{,}6}=0{,}208$. Benachbarte Werte haben den Korrelationskoeffizienten $0{,}36$, das Quadrat von $b$.
--- falsch
Die Varianz bleibt $\frac1{12}$, weil ein stabiles Filter die Leistung erhält. Benachbarte Werte haben den Korrelationskoeffizienten $0{,}6$, weil jeder Wert 60 % des vorigen enthält.
:::
:::karte zusammenhang Verteilung am Ausgang des rekursiven Filters
Warum ist der Ausgang des rekursiven Filters bei gleichverteiltem Eingang nicht mehr gleichverteilt, sondern ungefähr gaußverteilt?
---
Weil jeder Ausgangswert eine gewichtete Summe vieler unabhängiger Eingangswerte ist, $g(n)=\sum_kb^ks(n-k)$. Nach dem zentralen Grenzwertsatz ist das ungefähr gaußverteilt; bei $b=0{,}6$ tragen nur wenige Summanden merklich bei, die Näherung ist grob.
--- falsch
Weil die Rückkopplung die großen Werte stärker dämpft als die kleinen; dadurch sammeln sich die Werte um null, und die Verteilung wird glockenförmig, unabhängig davon, wie viele Eingangswerte zu einem Ausgangswert beitragen.
--- falsch
Weil ein LSI-System aus jeder Verteilung eine Gauß-Verteilung macht: Schon ein einzelner Verzögerungsschritt formt die Dichte exakt in eine Gaußkurve um, gleichgültig, wie groß der Faktor $b$ ist.
--- falsch
Weil der Ausgang die Varianz $0{,}130$ hat und jede Verteilung mit dieser Varianz eine Gauß-Verteilung ist; die Form der Verteilung folgt allein aus der Varianz, nicht aus der Entstehung des Signals.
:::
::::

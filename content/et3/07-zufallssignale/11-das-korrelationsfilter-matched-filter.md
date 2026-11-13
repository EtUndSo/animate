---
title: Stufe 10: Das Korrelationsfilter (Matched Filter)
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Zufallssignale
adresse: elektrotechnik/3-semester/signale-und-systeme/zufallssignale
knoten: Kapitel 7: Zufallssignale
order: 3271100
summary: Ein bekannter Impuls s(t) kommt verrauscht an.
tags: Korrelationsfilter, Korrelator
lang: de
---

<span class="anker" id="stufe-10"></span>

:::zweck
Ein bekannter Impuls $s(t)$ kommt verrauscht an. Mit welchem Filter wird er im Abtastzeitpunkt $T$ am deutlichsten sichtbar?
:::

**Der Ansatz.** Am Empfängereingang liegt $s(t)+n(t)$ mit weißem Rauschen $n$. Ein Filter $h$ liefert $y=g+n_e$ mit dem Nutzanteil $g=s*h$ und dem Störanteil $n_e=n*h$. Abgetastet wird bei $T$. Das Signal-Rausch-Verhältnis dort ist

$$\frac{S_a}{N}=\frac{g^2(T)}{\mathrm E\{n_e^2(T)\}}=\frac{\bigl[\int h(\tau)s(T-\tau)\mathrm{d}\tau\bigr]^2}{N_0\int|h(\tau)|^2\mathrm{d}\tau}=\frac{E_s}{N_0}\cdot\underbrace{\frac{\bigl[\int h(\tau)s(T-\tau)\mathrm{d}\tau\bigr]^2}{\int|h|^2\mathrm{d}\tau\int|s(T-\tau)|^2\mathrm{d}\tau}}_{=|p|^2\le1}.$$

Der rechte Bruch ist das Quadrat eines Korrelationskoeffizienten ([Kapitel 6](/wissen/elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen/korrelationsfunktionen.html)), zwischen $h(\tau)$ und $s(T-\tau)$. Er ist höchstens 1, und zwar genau dann, wenn beide dieselbe Form haben.

:::satz Satz 10.1 (Korrelationsfilter)
<span class="anker" id="satz-10-1"></span>

Gegen weißes Rauschen ist das beste erreichbare Signal-Rausch-Verhältnis

<span class="anker" id="gl-10-1"></span>
$$\Bigl(\frac{S_a}{N}\Bigr)_{\max}=\frac{E_s}{N_0},\qquad\text{erreicht mit}\qquad h(t)=a\,s(T-t),\quad H(f)=a\,S^*(f)\,\mathrm{e}^{-\mathrm{j}2\pi fT}. \tag{10.1}$$
:::

⁠**So liest man das:** Die beste Impulsantwort ist das zeitgespiegelte, um $T$ verschobene Signal selbst, das __Korrelationsfilter__ (matched filter). Sein Ausgang ohne Rauschen ist $g(t)=a\,\varphi^E_{ss}(t-T)$, die verschobene AKF des Signals, und wird genau in ihrem Maximum abgetastet. Erstaunlich ist: Das Ergebnis hängt nur von der *Energie* des Signals ab, nicht von seiner Form. Ein kurzer, hoher Impuls ist so gut wie ein langer, flacher mit derselben Energie. Damit das Filter kausal ist, muss $T$ mindestens die Dauer des Signals sein. Gleichwertig ist ein __Korrelator__: Er multipliziert das Empfangssignal mit $s(t)$ und integriert über die Dauer des Signals.

:::aufgabe Aufgabe 10 ★★ Ein Rechteckimpuls im Rauschen
<span class="anker" id="aufg-10"></span>

Ein Rechteckimpuls der Höhe 1 V und Dauer 1 ms wird mit weißem Rauschen der Leistungsdichte $N_0=10^{-6}$ V$^2$/Hz empfangen.

<ol class="al">

<li>

Wie sieht das Korrelationsfilter aus, und welches $S_a/N$ (in dB) erreicht es?

</li>

<li>

Wie sieht der Ausgang ohne Rauschen aus, und wann muss abgetastet werden?

</li>

<li>

Der Impuls wird auf 0,25 ms verkürzt, bei gleicher Höhe. Was ändert sich?

</li>

</ol>

:::loesung
(a) $h(t)=a\,s(T-t)$: wieder ein Rechteck von 1 ms, mit $T\ge1$ ms kausal. $E_s=1\,\mathrm{V^2}\cdot1\,\mathrm{ms}=10^{-3}$ V$^2$s, also $S_a/N=10^{-3}/10^{-6}=1000$, das sind 30 dB.

(b) Die AKF des Rechtecks, ein Dreieck der Breite 2 ms, verschoben um $T$: Es steigt ab $t=T-1\,\mathrm{ms}$ an und erreicht bei $t=T$ sein Maximum. Bei $T=1$ ms tastet man genau am Ende des Impulses ab, dann hat das Filter ihn ganz „gesehen“.

(c) $E_s$ sinkt auf ein Viertel, $S_a/N=250$, also 24 dB, 6 dB schlechter. Es zählt nur die Energie. Bei gleicher Höhe bedeutet ein kürzerer Impuls weniger Energie.
:::
:::

::::formelsammlung
**Signal-Rausch-Verhältnis am Filterausgang**

$$\frac{S_a}{N}=\frac{g^2(T)}{\mathrm E\{n_e^2(T)\}}=\frac{\bigl[\int h(\tau)s(T-\tau)\mathrm{d}\tau\bigr]^2}{N_0\int|h(\tau)|^2\mathrm{d}\tau}$$

Eingang $s(t)+n(t)$ mit weißem Rauschen, Nutzanteil $g=s*h$, Störanteil $n_e=n*h$, Abtastzeitpunkt $T$.

**Korrelationsfilter**

$$\Bigl(\frac{S_a}{N}\Bigr)_{\max}=\frac{E_s}{N_0},\qquad h(t)=a\,s(T-t),\quad H(f)=a\,S^*(f)\,\mathrm{e}^{-\mathrm{j}2\pi fT}$$

Gegen weißes Rauschen optimal; das Ergebnis hängt nur von der Energie des Signals ab, nicht von seiner Form. Kausal für $T$ mindestens gleich der Signaldauer. Gleichwertig: Korrelator (Multiplikation mit $s(t)$ und Integration über die Signaldauer).

**Ausgang ohne Rauschen**

$$g(t)=a\,\varphi^E_{ss}(t-T)$$

Die verschobene AKF des Signals, im Maximum bei $t=T$ abgetastet.
::::

::::lernkarten
:::karte formel Signal-Rausch-Verhältnis am Filterausgang
Wie lautet das Signal-Rausch-Verhältnis im Abtastzeitpunkt $T$ am Ausgang eines Filters $h$, wenn am Eingang $s(t)+n(t)$ mit weißem Rauschen $n$ liegt?
---
$\frac{S_a}{N}=\frac{g^2(T)}{\mathrm E\{n_e^2(T)\}}=\frac{\bigl[\int h(\tau)s(T-\tau)\mathrm{d}\tau\bigr]^2}{N_0\int|h(\tau)|^2\mathrm{d}\tau}$: das Quadrat des Nutzanteils $g=s*h$ bei $T$, geteilt durch die Leistung des Störanteils $n_e=n*h$.
--- falsch
$\frac{S_a}{N}=\frac{g(T)}{\mathrm E\{n_e(T)\}}=\frac{\int h(\tau)s(T-\tau)\mathrm{d}\tau}{N_0\int h(\tau)\mathrm{d}\tau}$: der Nutzanteil $g=s*h$ bei $T$, geteilt durch den Mittelwert des Störanteils $n_e=n*h$ zum selben Zeitpunkt.
--- falsch
$\frac{S_a}{N}=\frac{\int|s(t)|^2\mathrm{d} t}{N_0}$ für jedes Filter: Das Signal-Rausch-Verhältnis ist die Signalenergie durch die Leistungsdichte des Rauschens, unabhängig davon, welches Filter man verwendet.
--- falsch
$\frac{S_a}{N}=\frac{g^2(T)}{\mathrm E\{n_e^2(T)\}}=\frac{\bigl[\int h(\tau)s(T-\tau)\mathrm{d}\tau\bigr]^2}{N_0}$: Das Filter ändert nur den Nutzanteil; die Rauschleistung am Ausgang bleibt $N_0$, weil das Rauschen weiß ist.
:::
:::karte zusammenhang Obergrenze des Signal-Rausch-Verhältnisses
Warum kann das Signal-Rausch-Verhältnis am Ausgang eines Filters gegen weißes Rauschen den Wert $E_s/N_0$ nicht übersteigen?
---
Weil es gleich $E_s/N_0$ mal dem Quadrat eines Korrelationskoeffizienten zwischen $h(\tau)$ und $s(T-\tau)$ ist. Dieses Quadrat ist höchstens 1, und zwar genau dann gleich 1, wenn beide dieselbe Form haben.
--- falsch
Weil jedes Filter einen Teil der Signalenergie in Wärme umsetzt: Am Ausgang steht deshalb höchstens die Energie $E_s$, und das Rauschen bleibt mindestens $N_0$, gleichgültig, welches Filter man wählt.
--- falsch
Weil das Rauschen am Filterausgang stets die Leistung $N_0$ mal der Signaldauer hat; ein längeres Filter sammelt zwar mehr Signal, aber im gleichen Maß auch mehr Rauschen.
--- falsch
Weil es gleich $E_s/N_0$ mal dem Korrelationskoeffizienten zwischen $h(\tau)$ und $s(\tau)$ ist, ohne jede Spiegelung. Dieser ist höchstens 1, und zwar dann, wenn beide Funktionen gleich groß sind.
:::
:::karte herleitung Korrelationsfilter
Wie folgt aus dem Signal-Rausch-Verhältnis am Filterausgang, dass $h(t)=a\,s(T-t)$ das beste Filter gegen weißes Rauschen ist?
---
Man setzt $\frac{S_a}{N}=\frac{g^2(T)}{\mathrm E\{n_e^2(T)\}}$ an, weil im Abtastzeitpunkt $T$ der Nutzanteil $g=s*h$ und der Störanteil $n_e=n*h$ vorliegen.
---
Der Zähler ist $\bigl[\int h(\tau)s(T-\tau)\mathrm{d}\tau\bigr]^2$, weil $g(T)$ das Faltungsintegral bei $t=T$ ist; der Nenner ist $N_0\int|h(\tau)|^2\mathrm{d}\tau$, weil gefiltertes weißes Rauschen $N_0$ mal die Energie der Impulsantwort als Leistung hat.
---
Man erweitert mit der Signalenergie $E_s=\int|s(T-\tau)|^2\mathrm{d}\tau$ und erhält $E_s/N_0$ mal einen Bruch, weil dieser Bruch dann genau das Quadrat des Korrelationskoeffizienten zwischen $h(\tau)$ und $s(T-\tau)$ ist.
---
Dieses Quadrat ist höchstens 1 und genau dann gleich 1, wenn $h(\tau)$ und $s(T-\tau)$ dieselbe Form haben, also für $h(t)=a\,s(T-t)$, weil ein Korrelationskoeffizient nach Cauchy-Schwarz betragsmäßig höchstens 1 ist.
:::
:::karte begriff Korrelationsfilter
Was ist das Korrelationsfilter (matched filter) für einen bekannten Impuls $s(t)$ in weißem Rauschen?
---
Das Filter, dessen Impulsantwort das zeitgespiegelte, um $T$ verschobene Signal selbst ist: $h(t)=a\,s(T-t)$, also $H(f)=a\,S^*(f)\,\mathrm{e}^{-\mathrm{j}2\pi fT}$. Es erreicht das bestmögliche Signal-Rausch-Verhältnis.
--- falsch
Das Filter, dessen Impulsantwort das Signal selbst ist, ohne Spiegelung: $h(t)=a\,s(t)$, also $H(f)=a\,S(f)$. Es lässt genau die Frequenzen durch, die im Signal vorkommen, und sperrt alle anderen.
--- falsch
Das Filter, dessen Frequenzgang der Kehrwert des Signalspektrums ist: $H(f)=a/S(f)$. Es formt das Signal zu einem Dirac-Impuls, der sich vom Rauschen am deutlichsten abhebt.
--- falsch
Ein idealer Tiefpass, dessen Grenzfrequenz an die höchste Frequenz des Signals angepasst ist. Er lässt das ganze Signal durch und sperrt das ganze Rauschen oberhalb davon.
:::
:::karte formel Bestes Signal-Rausch-Verhältnis
Welches Signal-Rausch-Verhältnis erreicht das Korrelationsfilter gegen weißes Rauschen, und wovon hängt es ab?
---
$\Bigl(\frac{S_a}{N}\Bigr)_{\max}=\frac{E_s}{N_0}$: Es hängt nur von der Energie $E_s$ des Signals und von der Leistungsdichte $N_0$ des Rauschens ab, nicht von der Form des Signals.
--- falsch
$\Bigl(\frac{S_a}{N}\Bigr)_{\max}=\frac{E_s}{N_0}$: Es hängt von der Energie und von der Form des Signals ab; ein kurzer, hoher Impuls ist bei gleicher Energie besser zu erkennen als ein flacher.
--- falsch
$\Bigl(\frac{S_a}{N}\Bigr)_{\max}=\frac{\max|s(t)|^2}{N_0}$: Es hängt nur von der Spitzenleistung des Signals ab; deshalb sendet man möglichst hohe Impulse.
--- falsch
$\Bigl(\frac{S_a}{N}\Bigr)_{\max}=\frac{E_s}{2N_0}$: Es hängt nur von der Energie ab, aber die Hälfte geht verloren, weil das Filter das Signal zeitlich spiegelt.
:::
:::karte zusammenhang Ausgang des Korrelationsfilters
Welches Signal liefert das Korrelationsfilter ohne Rauschen am Ausgang, und warum tastet man es bei $T$ ab?
---
Die verschobene AKF des Signals, $g(t)=a\,\varphi^E_{ss}(t-T)$. Bei $t=T$ liegt ihr Maximum, denn ein Signal ist sich selbst ohne Verschiebung am ähnlichsten; dort ist der Nutzanteil am größten.
--- falsch
Das Signal selbst, um $T$ verzögert, $g(t)=a\,s(t-T)$. Bei $t=T$ beginnt der Impuls, und man tastet gleich zu Beginn ab, bevor sich das Rauschen am Ausgang ansammeln kann.
--- falsch
Das gespiegelte Signal, $g(t)=a\,s(T-t)$. Bei $t=T$ ist es null, und man tastet dort ab, weil dann nur noch das Rauschen übrig ist und man es vom Empfangssignal abziehen kann.
--- falsch
Die Energie des Signals als Konstante, $g(t)=a\,E_s$. Der Abtastzeitpunkt $T$ ist deshalb beliebig, weil der Ausgang nicht von der Zeit abhängt und überall gleich groß ist.
:::
:::karte zusammenhang Nur die Energie zählt
Warum ist ein kurzer, hoher Impuls im weißen Rauschen genauso gut zu erkennen wie ein langer, flacher Impuls derselben Energie?
---
Weil das beste erreichbare Signal-Rausch-Verhältnis $E_s/N_0$ nur von der Energie des Signals abhängt, nicht von seiner Form. Das Korrelationsfilter ist an jede Form angepasst.
--- falsch
Weil beide Impulse dieselbe Spitzenleistung haben, wenn ihre Energie gleich ist; das Signal-Rausch-Verhältnis hängt beim Korrelationsfilter nur von dieser Spitzenleistung ab.
--- falsch
Weil das Filter beide Impulse vor dem Abtasten auf dieselbe Dauer streckt; danach sind sie nicht mehr zu unterscheiden, und das Rauschen wirkt auf beide gleich stark.
--- falsch
Weil der kurze Impuls zwar weniger Energie hat, aber durch seine Höhe das Rauschen übertönt; beide Vorteile gleichen sich bei jedem beliebigen Filter genau aus.
:::
:::karte zusammenhang Kausales Korrelationsfilter
Wie groß muss der Abtastzeitpunkt $T$ mindestens sein, damit das Korrelationsfilter kausal ist, und warum?
---
Mindestens so groß wie die Dauer des Signals, weil $h(t)=a\,s(T-t)$ das gespiegelte Signal um $T$ nach rechts schiebt. Erst dann ist $h(t)$ für negative Zeiten null.
--- falsch
Mindestens doppelt so groß wie die Dauer des Signals, weil die AKF am Ausgang doppelt so lang ist wie das Signal und das Filter ihre ganze Länge abwarten muss.
--- falsch
Beliebig klein, auch null, weil ein Filter, dessen Impulsantwort aus dem Signal gebildet wird, immer kausal ist; das Signal beginnt ja erst bei $t=0$.
--- falsch
Mindestens so groß wie die Zeitkonstante des Rauschens, weil das Filter erst abtasten darf, wenn das Rauschen abgeklungen ist; die Dauer des Signals spielt keine Rolle.
:::
:::karte begriff Korrelator
Was macht ein Korrelator im Empfänger, und wie verhält er sich zum Korrelationsfilter?
---
Er multipliziert das Empfangssignal mit dem bekannten Signal $s(t)$ und integriert über die Dauer des Signals. Er ist dem Korrelationsfilter gleichwertig.
--- falsch
Er berechnet die AKF des Empfangssignals für alle Verschiebungen und sucht ihr Maximum. Er ist genauer als das Korrelationsfilter, weil er das Rauschen mitkorreliert.
--- falsch
Er addiert das bekannte Signal $s(t)$ zum Empfangssignal und mittelt über die Dauer des Signals. So verdoppelt er den Nutzanteil, ist dem Korrelationsfilter aber unterlegen.
--- falsch
Er multipliziert das Empfangssignal mit sich selbst und integriert über die Dauer des Signals. So misst er dessen Energie und muss das gesendete Signal nicht kennen.
:::
:::karte zusammenhang Kürzerer Rechteckimpuls
Was ändert sich am Signal-Rausch-Verhältnis des Korrelationsfilters, wenn ein Rechteckimpuls bei gleicher Höhe von 1 ms auf 0,25 ms verkürzt wird, und warum?
---
Es sinkt von 1000 (30 dB) auf 250 (24 dB), also um 6 dB, weil die Energie $E_s$ bei gleicher Höhe auf ein Viertel sinkt. Es zählt nur die Energie.
--- falsch
Es bleibt bei 30 dB, weil die Höhe gleich bleibt und das Korrelationsfilter nur die Höhe des Impulses auswertet, nicht seine Dauer.
--- falsch
Es steigt auf 36 dB, weil ein kürzerer Impuls schärfer ist und sich deutlicher vom Rauschen abhebt; das Filter wird kürzer und sammelt weniger Rauschen.
--- falsch
Es sinkt von 30 dB auf 15 dB, also auf die Hälfte, weil sich das Verhältnis in Dezibel proportional zur Dauer des Impulses ändert.
:::
::::

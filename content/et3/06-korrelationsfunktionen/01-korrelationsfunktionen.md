---
title: Korrelationsfunktionen
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / Korrelationsfunktionen
order: 3260100
summary: Wie ähnlich sind zwei Signale, und wie verteilt sich die Energie über die Frequenz?
tags: Signalenergie, Energiesignal, Leistung, Leistungssignal, Korrelationskoeffizienten, orthogonal, Autokorrelationsfunktion, Kreuzkorrelationsfunktion
lang: de
---

## Worum es geht

Ein Radar sendet einen Impuls und sucht im Empfangssignal sein Echo. Ein Mobiltelefon sucht im Rauschen eine bekannte Synchronisationsfolge. Beide stellen dieselbe Frage: *Wie ähnlich ist ein Signal einem anderen, und bei welcher Verschiebung am ähnlichsten?* Die Antwort liefert die Korrelationsfunktion. Ihre Fourier-Transformierte sagt außerdem, wie sich die Energie eines Signals auf die Frequenzen verteilt.

:::merke Die Antwort in drei Sätzen (am Ende des Artikels sollen sie selbstverständlich sein)
<ol>

<li>

Die Ähnlichkeit zweier Signale misst man am Integral ihres Produkts. Die Korrelationsfunktion tut das für jede Verschiebung $\tau$, sie ist eine Faltung mit dem gespiegelten Signal.

</li>

<li>

Die Fourier-Transformierte der Autokorrelationsfunktion ist das Energiedichtespektrum $|S(f)|^2$. Bei $\tau=0$ steht die Energie (Parseval).

</li>

<li>

Durch ein LTI-System werden Energiedichtespektren mit $|H(f)|^2$ multipliziert und Autokorrelationsfunktionen mit der Autokorrelationsfunktion von $h$ gefaltet.

</li>

</ol>
:::

**Ein Prinzip hinter allen Ergebnissen.** Korrelation ist Faltung mit einem gespiegelten Signal. Deshalb gelten alle Werkzeuge der Faltung:

| Ergebnis | Woher es kommt |
|---|---|
| Korrelationskoeffizient | Energie der Differenz zweier normierter Signale (Stufe [2](#stufe-2)) |
| Korrelationsprodukt | Faltung mit dem gespiegelten, konjugierten Signal (Stufe [3](#stufe-3)) |
| AKF gerade, Maximum bei 0 | Spiegeln, und am ähnlichsten ist ein Signal sich selbst (Stufe [3](#stufe-3)) |
| Energiedichtespektrum, Parseval | Spiegeln und Konjugieren wird $S^*$, Faltung wird Produkt (Stufe [4](#stufe-4)) |
| Wiener-Lee | Assoziativgesetz der Faltung (Stufe [5](#stufe-5)) |
| zeitdiskret, periodisch, DFT | dieselbe Rechnung mit Summen (Stufe [7](#stufe-7)) |

**So arbeitest du mit dem Artikel.** Jede Stufe hat die Idee, typische Fragen mit aufklappbaren Antworten und Aufgaben (★ bis ★★★). Versuche die Aufgaben zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf.

:::merke Das Rechenmodell für diesen Artikel
Rechteckimpuls $\operatorname{rect}(t)$, Dreieck $\Lambda(t)$, Exponentialimpuls $\varepsilon(t)\mathrm{e}^{-t}$ (die Impulsantwort des RC-Glieds mit $RC=1$ s) und die Folge $(1,2,1)$. Die Zahlen rechnet `rechnung_kap6.py` nach.
:::

## Stufe 1: Energie und Leistung

<span class="anker" id="stufe-1"></span>

:::zweck
Bevor man Signale vergleicht, braucht man ein Maß für ihre „Größe“. In der Systemtheorie ist das die Energie, bei unendlich langen Signalen die Leistung.
:::

An einem Widerstand $R$ wird in der Zeit von $t_1$ bis $t_2$ die Energie $\frac1R\int u^2\mathrm{d} t$ in Wärme umgesetzt. Ohne den Faktor $1/R$ heißt der Ausdruck __Signalenergie__:

<span class="anker" id="gl-1-1"></span>
$$E_s=\int_{-\infty}^{\infty}|s(t)|^2\,\mathrm{d} t. \tag{1.1}$$

Ist sie endlich, heißt $s$ __Energiesignal__ (zum Beispiel jeder Impuls). Dauert ein Signal unendlich lange an, ohne abzuklingen (ein Kosinus, ein Sprung), ist die Energie unendlich. Dann misst man die mittlere __Leistung__:

<span class="anker" id="gl-1-2"></span>
$$L_s=\lim_{T\to\infty}\frac{1}{2T}\int_{-T}^{T}|s(t)|^2\,\mathrm{d} t. \tag{1.2}$$

Ist sie endlich, heißt $s$ __Leistungssignal__. Bei periodischen Signalen genügt die Mittelung über eine Periode. Für Dirac-Impulse sind Energie und Leistung nicht definiert ($\delta^2$ gibt es nicht).

:::aufgabe Aufgabe 1 ★ Energie oder Leistung?
<span class="anker" id="aufg-1"></span>

Bestimme Energie oder Leistung von (a) $a\operatorname{rect}(t/T)$, (b) $\varepsilon(t)\mathrm{e}^{-t}$, (c) $A\cos(2\pi Ft)$, (d) $\varepsilon(t)$.

:::loesung
(a) $E=a^2|T|$. (b) $E=\int_0^\infty\mathrm{e}^{-2t}\mathrm{d} t=\frac12$. (c) Energie unendlich, Leistung $\frac{A^2}{2}$ (Mittelwert von $\cos^2$ ist $\frac12$). (d) Energie unendlich, Leistung $\lim\frac{1}{2T}\int_0^T1\,\mathrm{d} t=\frac12$: Die Hälfte der Zeit ist das Signal 1.
:::
:::

## Stufe 2: Ähnlichkeit messen, der Korrelationskoeffizient

<span class="anker" id="stufe-2"></span>

:::zweck
Wie misst man mit einer Zahl, wie ähnlich zwei Signale sind? Man misst, wie groß ihre Differenz ist.
:::

**Die Idee.** Die Energie der Differenz $\Delta(t)=s(t)-g(t)$ ist klein, wenn die Signale ähnlich sind. Ausmultipliziert:

$$E_\Delta=\int|s-g|^2\mathrm{d} t=E_s+E_g-\int s^*g\,\mathrm{d} t-\int g^*s\,\mathrm{d} t=E_s+E_g-2\operatorname{Re}\int s^*(t)g(t)\,\mathrm{d} t.$$

Der Unterschied steckt also allein im Integral des Produkts. Damit die Größe der Signale nicht mitzählt, normiert man beide auf die Energie 1. Dann ist $E_\Delta=2-2\operatorname{Re}\,p_{sg}$ mit dem __Korrelationskoeffizienten__

<span class="anker" id="gl-2-1"></span>
$$p_{sg}=\frac{\int_{-\infty}^{\infty}s^*(t)\,g(t)\,\mathrm{d} t}{\sqrt{E_sE_g}}. \tag{2.1}$$

⁠**So liest man das:** $|p_{sg}|\le1$ (Cauchy-Schwarz-Ungleichung). $p=1$ heißt $s=a\,g$ mit $a>0$: gleiche Form. $p=-1$ heißt $s=-a\,g$: gleiche Form, umgekehrtes Vorzeichen. $p=0$ heißt $\int s^*g\,\mathrm{d} t=0$, die Signale sind __orthogonal__, wie die Harmonischen einer Fourier-Reihe in [Teil 3](/wissen/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html). Beispiel: $\operatorname{rect}(t)$ und $\Lambda(t)$ haben $\int\operatorname{rect}\cdot\Lambda\,\mathrm{d} t=0{,}75$, $E_{\operatorname{rect}}=1$, $E_\Lambda=\frac23$, also $p=0{,}919$.

:::aufgabe Aufgabe 2 ★★ Korrelationskoeffizienten
<span class="anker" id="aufg-2"></span>

Berechne $p$ für (a) $\operatorname{rect}(t)$ und $\operatorname{rect}(t-0{,}5)$, (b) $\operatorname{rect}(t)$ und $\Lambda(t)$ (Ergebnis oben), (c) $\operatorname{rect}(t)$ und $\operatorname{sgn}(t)\operatorname{rect}(t)$.

:::loesung
(a) Die Rechtecke überlappen auf der Länge 0,5, also $\int=0{,}5$, beide Energien 1: $p=0{,}5$. (b) $\int\operatorname{rect}\cdot\Lambda\,\mathrm{d} t=\int_{-1/2}^{1/2}(1-|t|)\mathrm{d} t=0{,}75$, $E_\Lambda=2\int_0^1(1-t)^2\mathrm{d} t=\frac23$: $p=\frac{0{,}75}{\sqrt{2/3}}=0{,}919$. Sehr ähnliche Formen. (c) $\int\operatorname{sgn}(t)\operatorname{rect}^2(t)\mathrm{d} t=0$: $p=0$, die Signale sind orthogonal, obwohl sie auf der rechten Hälfte gleich sind.
:::
:::

## Stufe 3: Korrelationsfunktion und Korrelationsprodukt

<span class="anker" id="stufe-3"></span>

:::zweck
Ein Echo ist dem Sendeimpuls ähnlich, aber verschoben. Man vergleicht deshalb für jede Verschiebung $\tau$.
:::

:::definition Definition 3.1 (Korrelationsfunktion für Energiesignale)
<span class="anker" id="satz-3-1"></span>

<span class="anker" id="gl-3-1"></span>
$$\varphi^E_{sg}(\tau)=\int_{-\infty}^{\infty}s^*(t)\,g(t+\tau)\,\mathrm{d} t=s^*(-\tau)*g(\tau). \tag{3.1}$$

Für $g=s$ heißt sie __Autokorrelationsfunktion__ (AKF) $\varphi^E_{ss}(\tau)$, sonst __Kreuzkorrelationsfunktion__ (KKF). Geteilt durch $\sqrt{E_sE_g}$ heißt sie normiert.
:::

⁠**So liest man das:** Man schiebt $g$ um $\tau$ nach links und bildet das Integral des Produkts. Das zweite Gleichheitszeichen ist der Kern: Korrelation ist Faltung mit dem gespiegelten, konjugierten Signal. Deshalb heißt sie auch __Korrelationsprodukt__. Im Unterschied zur Faltung wird hier nicht gespiegelt, beide Signale laufen in dieselbe Richtung.

:::herleitung Korrelation als Faltung
In [(3.1)](#gl-3-1) $t=-\vartheta$ setzen: $\int s^*(-\vartheta)\,g(\tau-\vartheta)\,\mathrm{d}\vartheta$. Das ist das Faltungsintegral von $s^*(-\tau)$ mit $g(\tau)$.
:::

:::satz Satz 3.2 (Eigenschaften der Korrelationsfunktionen)
<span class="anker" id="satz-3-2"></span>

<span class="anker" id="gl-3-2"></span>
<span class="anker" id="gl-3-3"></span>
$$\begin{aligned} &\varphi^E_{gs}(\tau)=\varphi^{E*}_{sg}(-\tau),\qquad\varphi^E_{ss}(\tau)=\varphi^{E*}_{ss}(-\tau)\ \ (\text{bei reellem }s\text{ gerade}),\\ &|\varphi^E_{ss}(\tau)|\le\varphi^E_{ss}(0)=E_s. \end{aligned} \tag{3.2|3.3}$$

Ein zeitbegrenztes Signal hat eine AKF der doppelten Dauer.
:::

⁠**So liest man das:** Am ähnlichsten ist ein Signal sich selbst ohne Verschiebung, und dort ist die AKF seine Energie. Die AKF eines Rechtecks ist das Dreieck: $\varphi^E_{ss}=\operatorname{rect}(-\tau)*\operatorname{rect}(\tau)=\Lambda(\tau)$, doppelt so breit wie das Rechteck (Abb. [1](#abb-1) links).

**Beispiel: ein Echo finden.** Gesendet wird $s=\operatorname{rect}(t)$, empfangen das abgeschwächte, verzögerte Echo $g=0{,}5\operatorname{rect}(t-3)$. Die KKF ist $\varphi^E_{sg}(\tau)=0{,}5\,\Lambda(\tau-3)$: Ihr Maximum liegt bei $\tau=3$, der Verzögerung, und seine Höhe $0{,}5=0{,}5\cdot E_s$ gibt die Dämpfung an (Abb. [1](#abb-1) rechts). So misst ein Radar die Entfernung.

:::abbildung et3/k6korr
Links: Die AKF des Rechtecks ist das Dreieck, Maximum $=E_s=1$ bei $\tau=0$, doppelte Breite. Rechts: Die KKF zwischen Sendeimpuls und Echo $0{,}5\operatorname{rect}(t-3)$ hat ihr Maximum bei der Verzögerung $\tau=3$.
:::

:::frage Faltung und Korrelation sehen fast gleich aus. Wo ist der Unterschied?
Bei der Faltung $\int s(\tau)h(t-\tau)\mathrm{d}\tau$ läuft das zweite Signal rückwärts ($-\tau$): Das System „erinnert“ sich an die Vergangenheit. Bei der Korrelation $\int s^*(t)g(t+\tau)\mathrm{d} t$ laufen beide vorwärts: Man legt zwei Formen deckungsgleich übereinander und misst die Übereinstimmung. Rechnerisch ist der Unterschied genau das Spiegeln, deshalb ist Korrelation Faltung mit dem gespiegelten Signal.
:::

:::ltspice Ein Echo mit einem gleitenden Integrator finden
Ein Filter, das in jedem Moment über die letzte Sekunde integriert, bildet $y(t)=\int_{t-1}^{t}g(u)\,\mathrm{d} u$. Mit $s=\operatorname{rect}(t)$ ist das genau die KKF [(3.1)](#gl-3-1), um 0,5 s verzögert: $y(t)=\varphi^E_{sg}(t-0{,}5)$. Das Filter rechnet sie für alle $\tau$, während das Signal hereinkommt.

⁠**Zeichnen:** Quelle `voltage` am Netz `g` mit `PULSE(0 0.5 2.5 1u 1u 1)`, das Echo $0{,}5\operatorname{rect}(t-3)$. Zwei Verhaltensquellen `bv`: am Netz `int` mit `V=idt(V(g))` (laufendes Integral) und am Netz `y` mit `V=V(int)-delay(V(int),1)` (Integral über die letzte Sekunde).

⁠**Direktiven:** `.tran 0 6 0 1m`, `.meas tran ymax MAX V(y)`.

⁠**Was du siehst:** `V(y)` ist das Dreieck $0{,}5\,\Lambda(t-3{,}5)$ mit dem Maximum 0,5 bei $t=3{,}5$ s: die Verzögerung 3 s plus 0,5 s, weil das Filter erst am Ende des Echos fertig integriert hat. Die Höhe 0,5 ist die Dämpfung des Echos.

⁠**Zu Aufgabe [3](#aufg-3):** Eingang `PULSE(0 1 0 1u 1u 1 2 2)`, das Doppelrechteck, je 0,5 s später als im Text. Für `y` nimmst du

`V=V(int)-delay(V(int),1)+delay(V(int),2)-delay(V(int),3)`.

Dieses Filter integriert über zwei Fenster, die zum Doppelrechteck passen, und `V(y)` ist dessen AKF, um 3 s verschoben. Vergleiche mit deinem Ergebnis aus Aufgabe [3](#aufg-3)(a).
:::

:::aufgabe Aufgabe 3 ★★ Echo und Wiederholung
<span class="anker" id="aufg-3"></span>

<ol class="al">

<li>

Ein Signal besteht aus zwei Rechtecken: $s(t)=\operatorname{rect}(t)+\operatorname{rect}(t-2)$. Bestimme seine AKF. Woran sieht man die Wiederholung?

</li>

<li>

Prüfe [(3.3)](#gl-3-3) für dieses Signal.

</li>

</ol>

:::loesung
(a) Mit $\operatorname{rect}(-\tau)=\operatorname{rect}(\tau)$ und $\operatorname{rect}*\operatorname{rect}=\Lambda$ ergeben die vier Teilprodukte

$$\varphi^E_{ss}(\tau)=2\Lambda(\tau)+\Lambda(\tau-2)+\Lambda(\tau+2).$$

Die Nebenspitzen bei $\tau=\pm2$ zeigen den Abstand der Wiederholung. Dort liegt jeweils eines der beiden Rechtecke über dem anderen. Bei $\tau=0$ liegen beide übereinander, das gibt die doppelte Höhe.

(b) $\varphi^E_{ss}(0)=2=E_s=1+1$, und die Nebenspitzen haben nur den Wert 1.
:::
:::

## Stufe 4: Energiedichtespektrum

<span class="anker" id="stufe-4"></span>

:::zweck
Was ist die Fourier-Transformierte einer Korrelationsfunktion? Sie zeigt, wie sich die Energie über die Frequenzen verteilt.
:::

:::satz Satz 4.1 (Wiener-Khintchine für Energiesignale)
<span class="anker" id="satz-4-1"></span>

<span class="anker" id="gl-4-1"></span>
$$\varphi^E_{ss}(\tau)=s^*(-\tau)*s(\tau)\;\circ\!\!-\!\!\bullet\;S^*(f)\,S(f)=|S(f)|^2,\qquad\varphi^E_{sg}(\tau)\;\circ\!\!-\!\!\bullet\;S^*(f)\,G(f). \tag{4.1}$$
:::

⁠**So liest man das:** $|S(f)|^2$ heißt __Energiedichtespektrum__. Es ist reell, nie negativ und bei reellen Signalen gerade in $f$. Die Phase des Signals geht verloren: Alle Signale mit demselben Betragsspektrum haben dieselbe AKF. $S^*G$ heißt __Kreuzenergiedichtespektrum__. Die Herleitung braucht nur Faltungssatz, Zeitspiegelung und Konjugation: $s^*(-\tau)\circ\!\!-\!\!\bullet\,S^*(f)$ ([Teil 3](/wissen/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)).

**Parseval.** Bei $\tau=0$ ist die AKF die Energie. Mit dem Flächensatz:

<span class="anker" id="gl-4-2"></span>
$$E_s=\varphi^E_{ss}(0)=\int_{-\infty}^{\infty}|s(t)|^2\,\mathrm{d} t=\int_{-\infty}^{\infty}|S(f)|^2\,\mathrm{d} f. \tag{4.2}$$

Zwei orthogonale Signale haben auch orthogonale Spektren: $\int s^*g\,\mathrm{d} t=\int S^*G\,\mathrm{d} f=0$.

**Beispiel: der Exponentialimpuls.** $s(t)=\varepsilon(t)\mathrm{e}^{-t}$ hat $S(f)=\frac{1}{1+\mathrm{j}2\pi f}$, also $|S|^2=\frac{1}{1+(2\pi f)^2}$. Das ist zugleich $\operatorname{Re}\{S\}$, und dessen Rücktransformation ist der gerade Anteil des Signals ([Teil 3](/wissen/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)):

$$\varphi^E_{ss}(\tau)=\tfrac12\mathrm{e}^{-|\tau|},\qquad E_s=\varphi^E_{ss}(0)=\tfrac12.$$

Dasselbe gibt $\int_0^\infty\mathrm{e}^{-2t}\mathrm{d} t=\frac12$ im Zeitbereich und $\int\frac{\mathrm{d} f}{1+(2\pi f)^2}=\frac12$ im Frequenzbereich. Abbildung [2](#abb-2) zeigt das Signal, seine AKF und die beiden Spektren.

:::abbildung et3/k6exp
Exponentialimpuls ($RC=1$ s). Links das Signal und seine AKF $\frac12\mathrm{e}^{-|\tau|}$ (gerade, Maximum $=E_s=\frac12$). Rechts Betragsspektrum und Energiedichtespektrum, das schneller abfällt: Die Energie sitzt bei tiefen Frequenzen.
:::

:::aufgabe Aufgabe 4 ★ Parseval prüfen
<span class="anker" id="aufg-4"></span>

Berechne die Energie von $\operatorname{rect}(t)$ im Zeitbereich und mit [(4.2)](#gl-4-2) aus seinem Spektrum. Welches bekannte Integral über die si-Funktion folgt daraus?

:::loesung
Zeitbereich: $E=\int\operatorname{rect}^2\mathrm{d} t=1$. Frequenzbereich: $\int\operatorname{si}^2(\pi f)\mathrm{d} f$. Also folgt $\int_{-\infty}^\infty\operatorname{si}^2(\pi f)\mathrm{d} f=1$.
:::
:::

## Stufe 5: Korrelation und LTI-Systeme

<span class="anker" id="stufe-5"></span>

:::zweck
Was macht ein LTI-System mit der AKF und dem Energiedichtespektrum? Und wie misst man ein System mit der Kreuzkorrelation?
:::

:::satz Satz 5.1 (Wiener-Lee)
<span class="anker" id="satz-5-1"></span>

Für $g=s*h$:

<span class="anker" id="gl-5-1"></span>
$$\varphi^E_{gg}(\tau)=\varphi^E_{ss}(\tau)*\varphi^E_{hh}(\tau)\;\circ\!\!-\!\!\bullet\;|G(f)|^2=|S(f)|^2\,|H(f)|^2, \tag{5.1}$$

<span class="anker" id="gl-5-2"></span>
$$\varphi^E_{sg}(\tau)=\varphi^E_{ss}(\tau)*h(\tau)\;\circ\!\!-\!\!\bullet\;|S(f)|^2\,H(f). \tag{5.2}$$
:::

:::herleitung Wiener-Lee
$\varphi^E_{gg}=g^*(-\tau)*g(\tau)=[s^*(-\tau)*h^*(-\tau)]*[s(\tau)*h(\tau)]$. Nach Kommutativ- und Assoziativgesetz umsortieren: $[s^*(-\tau)*s(\tau)]*[h^*(-\tau)*h(\tau)]=\varphi^E_{ss}*\varphi^E_{hh}$. Ebenso $\varphi^E_{sg}=s^*(-\tau)*s(\tau)*h(\tau)$.
:::

⁠**So liest man das:** Das System multipliziert die Energie bei jeder Frequenz mit $|H|^2$. Die Phase des Systems spielt für die Energie keine Rolle. [(5.2)](#gl-5-2) ist ein Messverfahren: Hat der Eingang eine AKF, die fast ein gewichteter Dirac-Impuls $c\,\delta(\tau)$ ist (ein sehr kurzer Impuls oder breitbandiges Rauschen, [Teil 7](/wissen/elektrotechnik/3-semester/signale-und-systeme/zufallssignale/zufallssignale.html)), dann ist die Kreuzkorrelation zwischen Eingang und Ausgang fast $c\,h(\tau)$, also bis auf den Faktor $c$ die Impulsantwort. Anders als $|H|^2$ enthält sie auch die Phase.

:::ltspice Energie vor und hinter dem RC-Glied
⁠**Zeichnen:** Verhaltensquelle `bv` am Netz `s` mit `V=exp(-time)*(time>0)`, der Exponentialimpuls $\varepsilon(t)\mathrm{e}^{-t}$. Der Faktor `(time>0)` sorgt dafür, dass LTspice den Anfangszustand bei $t=0$ mit 0 V rechnet und der Kondensator leer startet. Dahinter das RC-Glied (`res` mit `1Meg`, `cap` mit `1u`) mit dem Ausgang am Netz `g`.

⁠**Direktiven:** `.tran 0 30 0 1m`, `.meas tran Es INTEG V(s)*V(s)` und `.meas tran Eg INTEG V(g)*V(g)`, die Energien nach [(1.1)](#gl-1-1).

⁠**Was du siehst:** `Es` $=0{,}500$, wie $E_s=\varphi^E_{ss}(0)=\frac12$ in Stufe [4](#stufe-4). Vergleiche `Eg` mit deinem Ergebnis aus Aufgabe [5](#aufg-5). Die Ausgangsenergie ist kleiner, weil das RC-Glied die Energie bei jeder Frequenz mit $|H|^2\le1$ multipliziert.
:::

:::aufgabe Aufgabe 5 ★★ Energie am Ausgang
<span class="anker" id="aufg-5"></span>

Der Exponentialimpuls $\varepsilon(t)\mathrm{e}^{-t}$ geht durch ein RC-Glied mit $RC=1$ s.

<ol class="al">

<li>

Bestimme $|G(f)|^2$ und daraus die Ausgangsenergie. Tipp: $\int_{-\infty}^\infty\frac{\mathrm{d} x}{(1+x^2)^2}=\frac\pi2$.

</li>

<li>

Prüfe im Zeitbereich mit $g(t)=t\,\mathrm{e}^{-t}\varepsilon(t)$ ([Teil 1](/wissen/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html), zwei RC-Glieder in Kette).

</li>

</ol>

:::loesung
(a) $|G|^2=|S|^2|H|^2=\frac{1}{(1+(2\pi f)^2)^2}$. Mit $x=2\pi f$: $E_g=\frac{1}{2\pi}\int\frac{\mathrm{d} x}{(1+x^2)^2}=\frac{1}{2\pi}\cdot\frac\pi2=\frac14$.

(b) $\int_0^\infty t^2\mathrm{e}^{-2t}\mathrm{d} t=\frac{2}{2^3}=\frac14$. Beide Wege stimmen überein. Die Energie sinkt von $\frac12$ auf $\frac14$, weil das zweite RC-Glied die höheren Frequenzen weiter dämpft.
:::
:::

## Stufe 6: Korrelation von Bandpasssignalen

<span class="anker" id="stufe-6"></span>

:::zweck
Auch Korrelationsfunktionen von Bandpasssignalen rechnet man mit den komplexen Hüllkurven ([Teil 5](/wissen/elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme/tiefpass-und-bandpasssysteme.html)).
:::

Die KKF zweier reeller Bandpasssignale ist wieder ein Bandpasssignal:

$$\varphi^E_{sg}(\tau)=\operatorname{Re}\bigl\{\varphi^E_{sgT}(\tau)\,\mathrm{e}^{\mathrm{j}2\pi f_0\tau}\bigr\}.$$

Das gespiegelte Signal hat die Hüllkurve $s_T^*(-t)$, denn

$$s(-t)=\operatorname{Re}\bigl\{s_T(-t)\mathrm{e}^{-\mathrm{j}2\pi f_0t}\bigr\}=\operatorname{Re}\bigl\{s_T^*(-t)\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr\}.$$

Mit der Übertragungsregel $g_T=\frac12s_T*h_T$ aus [Teil 5](/wissen/elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme/tiefpass-und-bandpasssysteme.html):

<span class="anker" id="gl-6-1"></span>
$$\varphi^E_{sgT}(\tau)=\tfrac12\bigl[s_T^*(-\tau)*g_T(\tau)\bigr]=\tfrac12\int_{-\infty}^{\infty}s_T^*(t)\,g_T(t+\tau)\,\mathrm{d} t,\qquad E_s=\varphi^E_{ss}(0)=\varphi^E_{ssT}(0). \tag{6.1}$$

⁠**So liest man das:** Die Korrelation zweier Bandpasssignale ist die halbe Korrelation ihrer Hüllkurven, aufmoduliert auf den Träger. Die Energie eines Bandpasssignals ist die halbe Energie seiner komplexen Hüllkurve: Ein Kosinus der Amplitude $|s_T|$ hat im Mittel nur die halbe Leistung.

## Stufe 7: Zeitdiskrete und periodische Korrelation

<span class="anker" id="stufe-7"></span>

:::zweck
Für Abtastwerte wird aus dem Integral eine Summe. Mit der DFT rechnet man Korrelationen schnell.
:::

:::satz Satz 7.1 (Zeitdiskrete Korrelation)
<span class="anker" id="satz-7-1"></span>

<span class="anker" id="gl-7-1"></span>
$$\varphi^E_{sg}(m)=\sum_{n=-\infty}^{\infty}s^*(n)\,g(n+m)=s^*(-m)*g(m),\qquad E_s=\sum_n|s(n)|^2=\int_{-1/2}^{1/2}|S_\mathrm a(f)|^2\,\mathrm{d} f, \tag{7.1}$$

<span class="anker" id="gl-7-2"></span>
$$\varphi^E_{ss}(m)\;\circ\!\!-\!\!\bullet\;|S_\mathrm a(f)|^2\ (\text{Periode }1),\qquad\varphi^E_{gg}(m)=\varphi^E_{ss}(m)*\varphi^E_{hh}(m). \tag{7.2}$$
:::

Für abgetastete Tiefpasssignale gilt $\varphi^E_{sg}(mT)=T\sum_ns^*(nT)g((n+m)T)$ und $E_s=T\sum_n|s(nT)|^2$. Ein zeitdiskretes Energiesignal ist eine quadratisch summierbare Folge.

**Beispiel.** $s=(1,2,1)$: $\varphi^E_{ss}=(1,4,6,4,1)$ für $m=-2,\dots,2$. Maximum $6=E_s$ bei $m=0$, gerade, fünf Werte statt drei. Probe mit Wiener-Khintchine bei $f=0$: $|S_\mathrm a(0)|^2=(1+2+1)^2=16=\sum_m\varphi^E_{ss}(m)$.

**Periodische Korrelation.** Wie bei der Faltung ([Teil 4](/wissen/elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme/abtastung-und-zeitdiskrete-systeme.html)) gilt für Folgen der Periode $M$

<span class="anker" id="gl-7-3"></span>
$$\varphi^E_{sgd}(m)=\sum_{n=0}^{M-1}s_d^*(n)\,g_d(n+m)\;\circ\!\!-\!\!\bullet\;S_d^*(k)\,G_d(k). \tag{7.3}$$

Mit der FFT berechnet heißt das __schnelle Korrelation__. Damit die periodische Korrelation die gewöhnliche wiedergibt, muss $M$ groß genug sein. Für $(1,2,1)$ ergibt $M=3$ die überlappte Folge $(6,5,5)$, $M=5$ dagegen $(6,4,1,1,4)$, die gewöhnliche AKF zyklisch angeordnet.

**Leistungssignale.** Für Signale unendlicher Energie mittelt man:

<span class="anker" id="gl-7-4"></span>
$$\varphi^L_{sg}(\tau)=\lim_{T\to\infty}\frac1T\int_{-T/2}^{T/2}s^*(t)\,g(t+\tau)\,\mathrm{d} t. \tag{7.4}$$

Sind beide Signale mit derselben Periode periodisch, genügt eine Periode, und die Korrelationsfunktion ist ebenfalls periodisch. Beispiel: $A\cos(2\pi Ft+\varphi_0)$ hat die AKF $\frac{A^2}{2}\cos(2\pi F\tau)$. Die Phase $\varphi_0$ ist verschwunden, bei $\tau=0$ steht die Leistung $\frac{A^2}{2}$.

:::aufgabe Aufgabe 6 ★ Diskrete AKF
<span class="anker" id="aufg-6"></span>

<ol class="al">

<li>

Rechne die AKF von $(1,2,1)$ von Hand nach.

</li>

<li>

Bestimme die AKF von $(1,-1)$. Was sagt $\varphi(\pm1)<0$ über das Signal?

</li>

</ol>

:::loesung
(a) $\varphi(0)=1+4+1=6$, $\varphi(\pm1)=1\cdot2+2\cdot1=4$, $\varphi(\pm2)=1\cdot1=1$.

(b) $\varphi(0)=2$, $\varphi(\pm1)=-1$. Ein negativer Wert bei der Verschiebung 1 heißt: Benachbarte Werte haben eher entgegengesetztes Vorzeichen, das Signal wechselt schnell. Passend dazu ist $|S_\mathrm a(f)|^2=|1-\mathrm{e}^{-\mathrm{j}2\pi f}|^2=2-2\cos(2\pi f)$ bei $f=0$ null und bei $f=\frac12$ maximal: ein Hochpasssignal.
:::
:::

:::aufgabe Aufgabe 7 ★★ AKF eines Kosinus
<span class="anker" id="aufg-7"></span>

Leite die AKF von $A\cos(2\pi Ft+\varphi_0)$ mit [(7.4)](#gl-7-4) über eine Periode her. Warum fällt $\varphi_0$ heraus, und was bedeutet das für die Messung der Phase mit der AKF?

:::loesung
Mit $\omega=2\pi F$ und $\cos a\cos b=\frac12[\cos(a-b)+\cos(a+b)]$:

$$\frac1T\int_0^TA^2\cos(\omega t+\varphi_0)\cos(\omega t+\omega\tau+\varphi_0)\mathrm{d} t=\frac{A^2}{2}\cos(\omega\tau)+\frac{A^2}{2T}\int_0^T\cos(2\omega t+\omega\tau+2\varphi_0)\mathrm{d} t.$$

Das zweite Integral läuft über zwei volle Perioden und ist null. $\varphi_0$ verschiebt nur den Zeitnullpunkt, und die Mittelung über alle Zeiten kennt keinen Nullpunkt. Mit der AKF eines einzelnen Signals kann man deshalb keine Phase messen. Die Phasendifferenz *zweier* Signale zeigt dagegen die Kreuzkorrelation.
:::
:::

:::kern Das Wichtigste
<ul>

<li>

$E_s=\int|s|^2\mathrm{d} t$; $L_s=\lim\frac{1}{2T}\int_{-T}^T|s|^2\mathrm{d} t$.

</li>

<li>

$p_{sg}=\frac{\int s^*g\,\mathrm{d} t}{\sqrt{E_sE_g}}$, $|p|\le1$, $p=0$: orthogonal.

</li>

<li>

$\varphi^E_{sg}(\tau)=\int s^*(t)g(t+\tau)\mathrm{d} t=s^*(-\tau)*g(\tau)$; $\varphi^E_{gs}(\tau)=\varphi^{E*}_{sg}(-\tau)$.

</li>

<li>

AKF: gerade (reell), Maximum $\varphi^E_{ss}(0)=E_s$, doppelte Dauer.

</li>

<li>

$\varphi^E_{ss}\leftrightarrow|S|^2$, $\varphi^E_{sg}\leftrightarrow S^*G$; Parseval $\int|s|^2\mathrm{d} t=\int|S|^2\mathrm{d} f$.

</li>

<li>

Wiener-Lee: $\varphi^E_{gg}=\varphi^E_{ss}*\varphi^E_{hh}$, $|G|^2=|S|^2|H|^2$; $\varphi^E_{sg}=\varphi^E_{ss}*h$.

</li>

<li>

Bandpass: $\varphi^E_{sgT}=\frac12s_T^*(-\tau)*g_T(\tau)$.

</li>

<li>

Diskret: $\varphi(m)=\sum s^*(n)g(n+m)$, $\leftrightarrow|S_\mathrm a|^2$; periodisch: $S_d^*G_d$.

</li>

</ul>
:::

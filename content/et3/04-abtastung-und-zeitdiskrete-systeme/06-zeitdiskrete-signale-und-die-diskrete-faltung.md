---
title: Stufe 5: Zeitdiskrete Signale und die diskrete Faltung
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Abtastung und zeitdiskrete Systeme
adresse: elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme
knoten: Kapitel 4: Abtastung und zeitdiskrete Systeme
order: 3240600
summary: Ab jetzt rechnet man nur noch mit den Zahlenfolgen s(n) .
tags: diskrete Faltung, Einheitsimpuls, verschiebungsinvariant, LSI-System, Impulsantwort, Differenz, Akkumulation, FIR-Filter
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Ab jetzt rechnet man nur noch mit den Zahlenfolgen $s(n)$. Diese Stufe überträgt Faltung, Elementarsignale und LTI-Systeme auf Folgen.
:::

**Faltung der Abtastwerte.** Sind Eingang $s$ und Impulsantwort $h$ eines Systems Tiefpasssignale und wird mit der Nyquist-Rate abgetastet, lässt sich jedes als si-Reihe [(3.3)](abtasttheorem-und-ruckgewinnung.html#gl-3-3) schreiben. Weil $\operatorname{si}(\pi t/T)*\operatorname{si}(\pi t/T)=T\operatorname{si}(\pi t/T)$ ist ([Kapitel 3](/wissen/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)), folgt für die Abtastwerte des Ausgangs allein

$$g(nT)=T\sum_{m=-\infty}^{\infty}s(mT)\,h\bigl((n-m)T\bigr).$$

Normiert auf $T=1$ ist das die __diskrete Faltung__:

<span class="anker" id="gl-5-1"></span>
$$g(n)=\sum_{m=-\infty}^{\infty}s(m)\,h(n-m)=s(n)*h(n). \tag{5.1}$$

**Elementarfolgen.**

$$\delta(n)=\begin{cases}1&n=0\\0&n\neq0\end{cases},\qquad \varepsilon(n)=\sum_{m=-\infty}^n\delta(m)=\begin{cases}0&n<0\\1&n\ge0\end{cases},\qquad \varepsilon(n)\,a^n,\qquad \mathrm{e}^{\mathrm{j}2\pi Fn}.$$

Der __Einheitsimpuls__ $\delta(n)$ ist eine gewöhnliche Folge, keine Distribution: Er hat bei $n=0$ den Wert 1. Er ist das Einselement der diskreten Faltung, $s(n)*\delta(n)=s(n)$. Ein Rechteck aus $2M+1$ Einsen um $n=0$ ist $\varepsilon(n+M)-\varepsilon(n-M-1)$.

**Linear und verschiebungsinvariant.** Ein zeitdiskretes System heißt linear, wenn der Überlagerungssatz gilt, und __verschiebungsinvariant__, wenn $\operatorname{Tr}\{s(n-m)\}=g(n-m)$ für jede ganze Zahl $m$. Zusammen heißt es __LSI-System__. Mit der __Impulsantwort__ $h(n)=\operatorname{Tr}\{\delta(n)\}$ folgt wie in [Kapitel 1](/wissen/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html):

$$g(n)=\operatorname{Tr}\Bigl\{\sum_ms(m)\delta(n-m)\Bigr\}=\sum_ms(m)\operatorname{Tr}\{\delta(n-m)\}=\sum_ms(m)\,h(n-m).$$

Hier braucht man keinen Grenzübergang: Eine Folge *ist* schon eine Summe gewichteter, verschobener Einheitsimpulse.

**Differenz und Summe.** Das Gegenstück zur Ableitung ist die __Differenz__ $g(n)=s(n)-s(n-1)$, also $h(n)=\delta(n)-\delta(n-1)$. Das Gegenstück zum Integral ist die __Akkumulation__ $g(n)=\sum_{m\le n}s(m)=s(n)*\varepsilon(n)$. Beide heben sich auf: $[\delta(n)-\delta(n-1)]*\varepsilon(n)=\varepsilon(n)-\varepsilon(n-1)=\delta(n)$.

**Differenzengleichungen, FIR und IIR.** Statt Differentialgleichungen beschreiben Differenzengleichungen zeitdiskrete Systeme:

<span class="anker" id="gl-5-2"></span>
$$g(n)=\underbrace{\sum_{q=0}^{Q}a_q\,s(n-q)}_{\text{FIR-Teil}}+\underbrace{\sum_{p=1}^{P}b_p\,g(n-p)}_{\text{IIR-Teil}}. \tag{5.2}$$

Der Ausgang ist eine gewichtete Summe vergangener Eingangs- und Ausgangswerte. Hängt er nur von Eingangswerten ab ($b_p=0$), ist die Impulsantwort nach $Q+1$ Werten zu Ende: ein __FIR-Filter__ (finite impulse response). Mit Rückkopplung ($b_p\neq0$) kann die Impulsantwort unendlich lang sein: ein __IIR-Filter__ (infinite impulse response). Gebaut wird beides aus Verzögerungsgliedern (Speicher für einen Takt), Multiplizierern und Addierern (Abb. [4](#abb-4)).

:::abbildung et3/k4block 4
System erster Ordnung $g(n)=a_0s(n)+a_1s(n-1)+b_1g(n-1)$. Das Kästchen $T$ speichert einen Wert für einen Takt. Links der nichtrekursive Teil, rechts die Rückkopplung des Ausgangs.
:::

:::aufgabe Aufgabe 4 ★ Diskrete Faltung von Hand
<span class="anker" id="aufg-4"></span>

Falte $s=(1,1,1)$ mit $h=(1,2)$, beide beginnend bei $n=0$. Wie lang ist das Ergebnis, und warum?

:::loesung
$g(0)=1$, $g(1)=1\cdot2+1\cdot1=3$, $g(2)=3$, $g(3)=1\cdot2=2$: $(1,3,3,2)$. Länge $3+2-1=4$: Der letzte von null verschiedene Wert entsteht, wenn der letzte Wert von $h$ auf den letzten Wert von $s$ trifft.
:::
:::

::::formelsammlung
**Abtastwerte des Ausgangs**

$$g(nT)=T\sum_{m=-\infty}^{\infty}s(mT)\,h\bigl((n-m)T\bigr)$$

Eingang $s$ und Impulsantwort $h$ Tiefpasssignale, abgetastet mit der Nyquist-Rate; folgt aus den si-Reihen mit $\operatorname{si}(\pi t/T)*\operatorname{si}(\pi t/T)=T\operatorname{si}(\pi t/T)$.

**Diskrete Faltung**

$$g(n)=\sum_{m=-\infty}^{\infty}s(m)\,h(n-m)=s(n)*h(n)$$

Normiert auf $T=1$. Zwei endliche Folgen mit $M_1$ und $M_2$ Werten ergeben $M_1+M_2-1$ Werte.

**Einheitsimpuls**

$$\delta(n)=\begin{cases}1&n=0\\0&n\neq0\end{cases}$$

Gewöhnliche Folge, keine Distribution. Einselement der diskreten Faltung: $s(n)*\delta(n)=s(n)$.

**Elementarfolgen**

$$\varepsilon(n)=\sum_{m=-\infty}^n\delta(m)=\begin{cases}0&n<0\\1&n\ge0\end{cases},\qquad\varepsilon(n)\,a^n,\qquad\mathrm{e}^{\mathrm{j}2\pi Fn}$$

Sprung, abklingende oder wachsende Exponentialfolge, Schwingung.

**Rechteck aus Einsen**

$$\varepsilon(n+M)-\varepsilon(n-M-1)$$

$2M+1$ Einsen um $n=0$.

**Verschiebungsinvarianz**

$$\operatorname{Tr}\{s(n-m)\}=g(n-m)$$

Für jede ganze Zahl $m$. Linear und verschiebungsinvariant zusammen: LSI-System.

**Faltungssumme eines LSI-Systems**

$$g(n)=\operatorname{Tr}\Bigl\{\sum_ms(m)\delta(n-m)\Bigr\}=\sum_ms(m)\operatorname{Tr}\{\delta(n-m)\}=\sum_ms(m)\,h(n-m)$$

Impulsantwort $h(n)=\operatorname{Tr}\{\delta(n)\}$. Kein Grenzübergang nötig, weil jede Folge schon eine Summe gewichteter, verschobener Einheitsimpulse ist.

**Differenz**

$$g(n)=s(n)-s(n-1)$$

Gegenstück zur Ableitung; Impulsantwort $h(n)=\delta(n)-\delta(n-1)$.

**Akkumulation**

$$g(n)=\sum_{m\le n}s(m)=s(n)*\varepsilon(n)$$

Gegenstück zum Integral.

**Differenz und Akkumulation heben sich auf**

$$[\delta(n)-\delta(n-1)]*\varepsilon(n)=\varepsilon(n)-\varepsilon(n-1)=\delta(n)$$

Hintereinandergeschaltet werden die Impulsantworten gefaltet.

**Differenzengleichung**

$$g(n)=\sum_{q=0}^{Q}a_q\,s(n-q)+\sum_{p=1}^{P}b_p\,g(n-p)$$

Erste Summe FIR-Teil, zweite IIR-Teil (Rückkopplung). Mit $b_p=0$: FIR-Filter, Impulsantwort nach $Q+1$ Werten zu Ende. Mit $b_p\neq0$: IIR-Filter, Impulsantwort kann unendlich lang sein.

**System erster Ordnung**

$$g(n)=a_0s(n)+a_1s(n-1)+b_1g(n-1)$$

Aus einem Verzögerungsglied je Zweig (speichert einen Wert für einen Takt), Multiplizierern und Addierern; $a_0$, $a_1$ nichtrekursiver Teil, $b_1$ Rückkopplung des Ausgangs.
::::

::::lernkarten
:::karte herleitung Faltung der Abtastwerte
Wie folgt für Tiefpasssignale $s$ und $h$, die mit der Nyquist-Rate abgetastet sind, dass $g(nT)=T\sum_{m=-\infty}^{\infty}s(mT)\,h\bigl((n-m)T\bigr)$ gilt?
---
Man schreibt $s$ und $h$ als si-Reihen der Form $\sum_ns(nT)\operatorname{si}(\pi(t-nT)/T)$, weil beide Tiefpasssignale sind und mit der Nyquist-Rate abgetastet wurden.
---
Man faltet die beiden Reihen Summand für Summand, weil die Faltung linear ist; dabei wird jeweils eine verschobene si-Funktion mit einer anderen verschobenen si-Funktion gefaltet.
---
Jede dieser Faltungen ist wieder eine si-Funktion mit dem Faktor $T$, weil $\operatorname{si}(\pi t/T)*\operatorname{si}(\pi t/T)=T\operatorname{si}(\pi t/T)$ ist und sich die beiden Verschiebungen addieren.
---
Der Ausgang ist damit selbst eine si-Reihe, und ihre Werte an den Punkten $nT$ sind die Gewichte, weil jede si-Funktion an ihrem Abtastpunkt 1 und an allen anderen null ist. Sammelt man alle Beiträge zum Punkt $nT$, entsteht $T\sum_{m=-\infty}^{\infty}s(mT)\,h\bigl((n-m)T\bigr)$.
:::
:::karte begriff diskrete Faltung
Was berechnet die diskrete Faltung zweier Folgen $s(n)$ und $h(n)$, und wie hängt sie mit der Faltung der Abtastwerte zusammen?
---
Die Folge $g(n)=\sum_{m=-\infty}^{\infty}s(m)\,h(n-m)=s(n)*h(n)$, das Gegenstück zum Faltungsintegral mit einer Summe. Sie ist die Faltung der Abtastwerte, normiert auf $T=1$, sodass der Faktor $T$ entfällt.
--- falsch
Die Folge $g(n)=\sum_{m=-\infty}^{\infty}s(m)\,h(m)$, die Summe der Produkte gleichzeitiger Werte. Sie ist die Faltung der Abtastwerte, normiert auf $T=1$, sodass alle Verschiebungen entfallen.
--- falsch
Die Folge $g(n)=s(n)\,h(n)$, das Produkt der Werte zu jedem Zeitpunkt. Bei Folgen fällt die Faltung mit der Multiplikation zusammen, weil zwischen den Abtastpunkten nichts zu integrieren ist.
--- falsch
Die Folge $g(n)=\sum_{m=-\infty}^{\infty}s(m)\,h(n+m)$, eine Summe über verschobene Produkte. Sie folgt aus dem Faltungsintegral, indem man es an den Punkten $nT$ auswertet, ohne die Funktionen als si-Reihen zu schreiben.
:::
:::karte zusammenhang Länge der diskreten Faltung
Wie viele Werte hat die diskrete Faltung zweier endlicher Folgen mit $M_1$ und $M_2$ Werten, etwa $s=(1,1,1)$ und $h=(1,2)$, und warum?
---
$M_1+M_2-1$ Werte, hier $(1,3,3,2)$ mit vier Werten. Der letzte von null verschiedene Wert entsteht, wenn der letzte Wert von $h$ auf den letzten Wert von $s$ trifft.
--- falsch
$M_1\cdot M_2$ Werte, hier sechs, weil jeder Wert von $s$ mit jedem Wert von $h$ multipliziert wird und jedes dieser Produkte einen eigenen Wert der Faltung bildet.
--- falsch
So viele Werte wie die längere Folge, hier drei: $(1,3,3)$. Die Faltung kann nicht länger sein als die längere Folge, weil $h$ nur innerhalb von $s$ verschoben wird.
--- falsch
$M_1+M_2$ Werte, hier fünf: $(1,3,3,2,0)$. Der letzte Wert entsteht erst, wenn $h$ vollständig über das Ende von $s$ hinausgeschoben ist und nichts mehr überlappt.
:::
:::karte begriff Einheitsimpuls
Was ist der Einheitsimpuls $\delta(n)$ bei Folgen, und welche Rolle spielt er bei der diskreten Faltung?
---
Die Folge mit dem Wert 1 bei $n=0$ und 0 sonst, eine gewöhnliche Folge und keine Distribution. Er ist das Einselement der diskreten Faltung: $s(n)*\delta(n)=s(n)$.
--- falsch
Ein Dirac-Impuls bei $n=0$ mit unendlicher Höhe und der Fläche 1, eine Distribution wie bei Funktionen. Er ist das Einselement der diskreten Faltung: $s(n)*\delta(n)=s(n)$.
--- falsch
Die Folge mit dem Wert 1 für alle $n\ge0$ und 0 sonst. Er ist das Einselement der diskreten Faltung, weil die Faltung mit ihm jeden Wert der Folge unverändert lässt.
--- falsch
Die Folge mit dem Wert 1 bei $n=0$ und 0 sonst, eine gewöhnliche Folge. Er ist das Nullelement der diskreten Faltung: Die Faltung mit ihm ergibt für jede Folge außer $\delta(n)$ selbst null.
:::
:::karte formel Rechteck aus Einsen
Wie schreibt man ein Rechteck aus $2M+1$ Einsen um $n=0$ mit der Folge $\varepsilon(n)=\sum_{m=-\infty}^n\delta(m)$?
---
Als $\varepsilon(n+M)-\varepsilon(n-M-1)$. Die Folge $\varepsilon(n)$ ist 0 für $n<0$ und 1 für $n\ge0$; die erste springt bei $-M$ auf 1, die zweite erst bei $M+1$, und ihre Differenz ist nur dazwischen 1.
--- falsch
Als $\varepsilon(n+M)+\varepsilon(n-M-1)$. Die Folge $\varepsilon(n)$ ist 0 für $n<0$ und 1 für $n\ge0$; die beiden Sprünge begrenzen das Rechteck links und rechts, deshalb werden sie addiert.
--- falsch
Als $\varepsilon(n-M)-\varepsilon(n+M)$. Die Folge $\varepsilon(n)$ ist 0 für $n<0$ und 1 für $n\ge0$; der erste Sprung liegt links, der zweite rechts, und die Differenz ist dazwischen 1.
--- falsch
Als $\varepsilon(n+M)-\varepsilon(n-M)$. Die Folge $\varepsilon(n)$ ist 0 für $n<0$ und 1 für $n\ge0$; die Differenz ist für $-M\le n\le M$ gleich 1, das sind genau die $2M+1$ Einsen.
:::
:::karte begriff verschiebungsinvariant
Wann heißt ein zeitdiskretes System verschiebungsinvariant?
---
Wenn eine Verschiebung des Eingangs um $m$ Takte den Ausgang genauso verschiebt: $\operatorname{Tr}\{s(n-m)\}=g(n-m)$ für jede ganze Zahl $m$. Das System reagiert also zu jeder Zeit gleich.
--- falsch
Wenn sein Ausgang nicht von einer Verschiebung des Eingangs abhängt: $\operatorname{Tr}\{s(n-m)\}=g(n)$ für jede ganze Zahl $m$. Eine Verzögerung des Eingangs ändert den Ausgang also überhaupt nicht.
--- falsch
Wenn sich seine Impulsantwort mit der Zeit nicht ändert, also $h(n)$ für alle $n$ denselben Wert hat. Ein solches System verstärkt jeden Wert gleich, egal wann er ankommt.
--- falsch
Wenn der Überlagerungssatz gilt: Die Antwort auf eine Summe von Eingängen ist die Summe der einzelnen Antworten. Verschiebungen des Eingangs spielen dabei keine Rolle.
:::
:::karte begriff LSI-System
Was ist ein LSI-System, und wodurch ist es vollständig beschrieben?
---
Ein zeitdiskretes System, das linear (Überlagerungssatz) und verschiebungsinvariant ist. Es ist vollständig durch seine Impulsantwort $h(n)=\operatorname{Tr}\{\delta(n)\}$ beschrieben, denn der Ausgang ist die Faltung $s(n)*h(n)$.
--- falsch
Ein zeitdiskretes System, das linear und stabil ist. Es ist vollständig durch seine Sprungantwort beschrieben, denn der Ausgang ist die Summe der mit dem Eingang gewichteten Sprungantworten.
--- falsch
Ein zeitdiskretes System, das linear und verschiebungsinvariant ist. Es ist vollständig durch seine Antwort auf eine einzige Schwingung beschrieben, denn jede Folge ist eine Verschiebung dieser Schwingung.
--- falsch
Ein zeitdiskretes System, das linear und verschiebungsinvariant ist und nur endlich lange Impulsantworten hat. Es ist durch die Koeffizienten $a_q$ beschrieben, eine Rückkopplung ist dabei ausgeschlossen.
:::
:::karte herleitung Faltungssumme aus der Impulsantwort
Wie folgt für ein LSI-System mit der Impulsantwort $h(n)=\operatorname{Tr}\{\delta(n)\}$, dass $g(n)=\sum_ms(m)\,h(n-m)$ ist?
---
Man schreibt den Eingang als $\sum_ms(m)\delta(n-m)$, weil jede Folge schon eine Summe gewichteter, verschobener Einheitsimpulse ist.
---
Man zieht die Summe und die Gewichte $s(m)$ aus $\operatorname{Tr}$ heraus, weil das System linear ist: $g(n)=\sum_ms(m)\operatorname{Tr}\{\delta(n-m)\}$.
---
Man ersetzt $\operatorname{Tr}\{\delta(n-m)\}$ durch $h(n-m)$, weil das System verschiebungsinvariant ist und ein um $m$ verschobener Impuls die um $m$ verschobene Impulsantwort liefert.
---
Es bleibt $g(n)=\sum_ms(m)\,h(n-m)$; ein Grenzübergang wie bei kontinuierlichen Signalen ist nicht nötig, weil die Zerlegung in Einheitsimpulse hier exakt ist.
:::
:::karte zusammenhang Impulsantwort
Warum braucht man bei zeitdiskreten Systemen keinen Grenzübergang, um den Ausgang aus der Impulsantwort zu gewinnen, anders als bei kontinuierlichen Systemen?
---
Eine Folge ist schon exakt eine Summe gewichteter, verschobener Einheitsimpulse, $\sum_ms(m)\delta(n-m)$. Eine Funktion dagegen muss man erst aus immer schmaleren Rechtecken zusammensetzen.
--- falsch
Weil die Impulsantwort eines zeitdiskreten Systems immer endlich lang ist. Die Faltungssumme hat deshalb nur endlich viele Glieder, und ein Grenzübergang wäre in jedem Fall überflüssig.
--- falsch
Weil der Einheitsimpuls eine Distribution mit unendlicher Höhe ist. Er enthält damit bereits den ganzen Grenzübergang, der bei Funktionen erst mit immer schmaleren Rechtecken entsteht.
--- falsch
Weil zeitdiskrete Systeme nicht linear sein müssen. Der Ausgang ergibt sich direkt aus dem Eingang zum selben Zeitpunkt, und die Impulsantwort dient dabei nur zur Kontrolle des Ergebnisses.
:::
:::karte begriff Differenz
Was ist die Differenz als zeitdiskretes System, und welche Impulsantwort hat sie?
---
Das Gegenstück zur Ableitung: $g(n)=s(n)-s(n-1)$, der Unterschied zwischen dem aktuellen und dem vorigen Wert. Ihre Impulsantwort ist $h(n)=\delta(n)-\delta(n-1)$.
--- falsch
Das Gegenstück zum Integral: Sie bildet die Summe aller Werte bis zum aktuellen, $g(n)=\sum_{m\le n}s(m)$. Ihre Impulsantwort ist deshalb die Folge $\varepsilon(n)$.
--- falsch
Das Gegenstück zur Ableitung: $g(n)=s(n+1)-s(n-1)$, der Unterschied zwischen dem nächsten und dem vorigen Wert. Ihre Impulsantwort ist $h(n)=\delta(n+1)-\delta(n-1)$.
--- falsch
Das Gegenstück zur Ableitung: $g(n)=s(n)-s(n-1)$. Ihre Impulsantwort ist $h(n)=\delta(n)$, weil ein einzelner Impuls keinen Vorgänger hat, von dem etwas abgezogen werden könnte.
:::
:::karte begriff Akkumulation
Was ist die Akkumulation als zeitdiskretes System, und wie schreibt man sie als Faltung?
---
Das Gegenstück zum Integral: Sie summiert alle Werte bis zum aktuellen, $g(n)=\sum_{m\le n}s(m)=s(n)*\varepsilon(n)$. Ihre Impulsantwort ist also die Folge $\varepsilon(n)$.
--- falsch
Das Gegenstück zum Integral: Sie summiert alle Werte, $g(n)=\sum_{m=-\infty}^{\infty}s(m)$, also auch die künftigen. Als Faltung ist das $s(n)*\delta(n)$, weil jeder Wert genau einmal zählt.
--- falsch
Das Gegenstück zur Ableitung: Sie bildet den Unterschied aufeinanderfolgender Werte, $g(n)=s(n)-s(n-1)=s(n)*\varepsilon(n)$. Ihre Impulsantwort ist also die Folge $\varepsilon(n)$.
--- falsch
Das Gegenstück zum Integral: Sie summiert die letzten zwei Werte, $g(n)=s(n)+s(n-1)$. Als Faltung ist das $s(n)*[\delta(n)+\delta(n-1)]$, ihre Impulsantwort hat also zwei Werte.
:::
:::karte zusammenhang Differenz und Akkumulation
Warum heben sich Differenz und Akkumulation gegenseitig auf, wenn man sie hintereinander schaltet?
---
Hintereinander werden die Impulsantworten gefaltet: $[\delta(n)-\delta(n-1)]*\varepsilon(n)=\varepsilon(n)-\varepsilon(n-1)=\delta(n)$. Die Sprungfolge minus ihre um einen Takt verzögerte Kopie ist nur bei $n=0$ von null verschieden.
--- falsch
Weil beide Systeme dieselbe Impulsantwort $\delta(n)$ haben und die Faltung von $\delta(n)$ mit sich selbst wieder $\delta(n)$ ergibt. Jedes der beiden Systeme allein lässt das Signal deshalb schon unverändert.
--- falsch
Sie heben sich nur auf, wenn die Akkumulation zuerst kommt. Umgekehrt entsteht $\varepsilon(n)$, weil die Differenz den ersten Wert verliert und die Akkumulation ihn nicht mehr zurückholen kann.
--- falsch
Weil sich die Impulsantworten addieren: $[\delta(n)-\delta(n-1)]+\varepsilon(n)=\delta(n)$. Die Sprungfolge füllt genau die Lücke, die die Differenz an der Stelle $n=1$ hinterlassen hat.
:::
:::karte formel Differenzengleichung
Wie lautet die allgemeine Differenzengleichung eines zeitdiskreten Systems, und welche Teile unterscheidet man darin?
---
$g(n)=\sum_{q=0}^{Q}a_q\,s(n-q)+\sum_{p=1}^{P}b_p\,g(n-p)$. Der erste Teil gewichtet aktuelle und vergangene Eingangswerte (FIR-Teil), der zweite vergangene Ausgangswerte (IIR-Teil, Rückkopplung).
--- falsch
$g(n)=\sum_{q=0}^{Q}a_q\,s(n-q)+\sum_{p=0}^{P}b_p\,g(n-p)$. Der erste Teil gewichtet Eingangswerte (FIR-Teil), der zweite Ausgangswerte einschließlich des aktuellen (IIR-Teil), sodass $g(n)$ auf beiden Seiten steht.
--- falsch
$g(n)=\sum_{q=0}^{Q}a_q\,s(n+q)+\sum_{p=1}^{P}b_p\,g(n+p)$. Der erste Teil gewichtet künftige Eingangswerte (FIR-Teil), der zweite künftige Ausgangswerte (IIR-Teil), weil der Ausgang vorausschauend berechnet wird.
--- falsch
$g(n)=\sum_{q=0}^{Q}a_q\,\frac{\mathrm{d}^q s}{\mathrm{d} n^q}+\sum_{p=1}^{P}b_p\,\frac{\mathrm{d}^p g}{\mathrm{d} n^p}$. Der erste Teil enthält Ableitungen des Eingangs (FIR-Teil), der zweite Ableitungen des Ausgangs (IIR-Teil).
:::
:::karte begriff FIR-Filter
Was ist ein FIR-Filter, und warum ist seine Impulsantwort endlich lang?
---
Ein System, dessen Ausgang nur von Eingangswerten abhängt ($b_p=0$, keine Rückkopplung). Ein Impuls am Eingang wirkt nur über die $Q+1$ Gewichte $a_q$, deshalb ist die Impulsantwort nach $Q+1$ Werten zu Ende (finite impulse response).
--- falsch
Ein System mit Rückkopplung ($b_p\neq0$), dessen Rückkopplung den Impuls nach $Q+1$ Takten wieder löscht. Deshalb ist die Impulsantwort nach $Q+1$ Werten zu Ende (finite impulse response).
--- falsch
Ein System, dessen Ausgang nur von Eingangswerten abhängt ($b_p=0$). Seine Impulsantwort ist endlich lang, weil sie mit der Zeit abklingt und ab einer gewissen Schwelle als null gilt, wie bei jedem stabilen System.
--- falsch
Ein System, das nur den aktuellen Eingangswert gewichtet ($Q=0$). Seine Impulsantwort ist endlich lang, weil sie aus genau einem Wert besteht; mehr Werte würden immer eine Rückkopplung erfordern.
:::
:::karte begriff IIR-Filter
Was ist ein IIR-Filter, und wodurch kann seine Impulsantwort unendlich lang werden?
---
Ein System mit Rückkopplung ($b_p\neq0$), dessen Ausgang auch von vergangenen Ausgangswerten abhängt. Ein Impuls läuft immer wieder durch die Rückkopplung, deshalb kann die Impulsantwort unendlich lang sein.
--- falsch
Ein System ohne Rückkopplung ($b_p=0$) mit unendlich vielen Koeffizienten $a_q$. Nur so kann die Impulsantwort unendlich lang werden, denn jeder ihrer Werte braucht einen eigenen Koeffizienten $a_q$.
--- falsch
Ein System mit Rückkopplung ($b_p\neq0$), das grundsätzlich instabil ist. Seine Impulsantwort wächst ohne Grenze, weil jeder Durchlauf durch die Rückkopplung den Impuls weiter verstärkt.
--- falsch
Ein System, das kontinuierliche Signale verarbeitet und deshalb unendlich viele Werte liefert. Bei Folgen gibt es keine IIR-Filter, weil eine Folge im Rechner stets nach endlich vielen Werten abbricht.
:::
::::

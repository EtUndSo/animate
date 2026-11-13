---
title: Stufe 1: Signalklassen und ideale Abtastung
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Abtastung und zeitdiskrete Systeme
adresse: elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme
knoten: Kapitel 4: Abtastung und zeitdiskrete Systeme
order: 3240200
summary: Welche Arten von Signalen gibt es, und wie beschreibt man das Abtasten mathematisch?
tags: analoges, zeitdiskretes, digitales, ideale Abtaster
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Welche Arten von Signalen gibt es, und wie beschreibt man das Abtasten mathematisch?
:::

**Vier Klassen.** Zeit und Amplitude können jeweils kontinuierlich oder diskret sein. Ein __analoges__ Signal ist in beiden kontinuierlich. Ein __zeitdiskretes__ Signal hat Werte nur zu den Zeiten $nT$, diese aber beliebig genau. Ein __digitales__ Signal ist zusätzlich in der Amplitude gestuft (quantisiert), weil ein Rechner nur endlich viele Zahlen darstellen kann. Dieses Kapitel behandelt die Diskretisierung der Zeit. Die Quantisierung der Amplitude ist ein eigenes Thema.

**Vom realen zum idealen Abtaster.** Ein realer Abtaster schließt in jedem Takt für die kurze Zeit $T_0$ einen Schalter:

<span class="anker" id="gl-1-1"></span>
$$s_0(t)=s(t)\sum_{n=-\infty}^{\infty}\operatorname{rect}\Bigl(\frac{t-nT}{T_0}\Bigr)=s(t)\Bigl[\operatorname{rect}\Bigl(\frac{t}{T_0}\Bigr)*\sum_n\delta(t-nT)\Bigr]. \tag{1.1}$$

Macht man $T_0$ immer kürzer, bleiben nur noch die Werte $s(nT)$ übrig. Mathematisch ersetzt man das Rechteck durch einen Dirac-Impuls. Das ist der __ideale Abtaster__:

<span class="anker" id="gl-1-2"></span>
$$s_\mathrm a(t)=s(t)\sum_{n=-\infty}^{\infty}\delta(t-nT)=\sum_{n=-\infty}^{\infty}s(nT)\,\delta(t-nT). \tag{1.2}$$

Das abgetastete Signal ist eine Folge von Dirac-Impulsen, jeder mit einem Abtastwert als Gewicht. Der zweite Schritt ist die Siebeigenschaft $s(t)\delta(t-nT)=s(nT)\delta(t-nT)$. In dieser Form lassen sich abgetastete Signale mit allen Werkzeugen für kontinuierliche Signale behandeln.

::::formelsammlung
**Realer Abtaster**

$$s_0(t)=s(t)\sum_{n=-\infty}^{\infty}\operatorname{rect}\Bigl(\frac{t-nT}{T_0}\Bigr)=s(t)\Bigl[\operatorname{rect}\Bigl(\frac{t}{T_0}\Bigr)*\sum_n\delta(t-nT)\Bigr]$$

$T$ Abtastintervall, $T_0$ kurze Schließzeit des Schalters in jedem Takt. Das Signal wird mit einer periodischen Folge von Rechtecken multipliziert.

**Idealer Abtaster**

$$s_\mathrm a(t)=s(t)\sum_{n=-\infty}^{\infty}\delta(t-nT)=\sum_{n=-\infty}^{\infty}s(nT)\,\delta(t-nT)$$

Grenzfall immer kürzerer Schließzeit $T_0$: Das Rechteck wird durch einen Dirac-Impuls ersetzt. Ergebnis: Dirac-Impulse mit den Abtastwerten $s(nT)$ als Gewichten, eine Funktion der kontinuierlichen Zeit.

**Siebeigenschaft**

$$s(t)\delta(t-nT)=s(nT)\delta(t-nT)$$

Der Impuls bei $nT$ greift nur den Wert des Signals an dieser Stelle heraus; daraus folgt die zweite Form des ideal abgetasteten Signals.
::::

::::lernkarten
:::karte begriff analoges Signal
Was kennzeichnet ein analoges Signal, wenn man Signale danach einteilt, ob Zeit und Amplitude kontinuierlich oder diskret sind?
---
Ein analoges Signal ist in Zeit und Amplitude kontinuierlich: Es hat zu jedem Zeitpunkt einen Wert, und dieser Wert kann jede Zahl eines Bereichs annehmen.
--- falsch
Ein analoges Signal ist in der Zeit kontinuierlich, in der Amplitude aber gestuft: Es hat zu jedem Zeitpunkt einen Wert, der jedoch nur endlich viele Stufen annehmen kann.
--- falsch
Ein analoges Signal hat Werte nur zu den Zeitpunkten $nT$, diese aber beliebig genau. Es entsteht, wenn man ein Signal im festen Takt misst und die Werte unverändert speichert.
--- falsch
Ein analoges Signal ist jedes Signal, das aus einer elektrischen Größe wie einer Spannung stammt; ob Zeit und Amplitude kontinuierlich oder diskret sind, spielt für die Einteilung keine Rolle.
:::
:::karte begriff zeitdiskretes Signal
Was ist ein zeitdiskretes Signal, und worin unterscheidet es sich von einem digitalen Signal?
---
Ein zeitdiskretes Signal hat Werte nur zu den Zeiten $nT$, diese aber beliebig genau. Ein digitales Signal ist zusätzlich in der Amplitude gestuft (quantisiert).
--- falsch
Ein zeitdiskretes Signal hat Werte nur zu den Zeiten $nT$, und diese sind stets auf endlich viele Stufen gerundet. Ein digitales Signal ist dasselbe, nur in binärer Form gespeichert.
--- falsch
Ein zeitdiskretes Signal ist zu jeder Zeit definiert, aber in der Amplitude gestuft. Ein digitales Signal hat zusätzlich nur Werte zu den Zeiten $nT$.
--- falsch
Ein zeitdiskretes Signal ist nur für eine begrenzte Zeit von null verschieden. Ein digitales Signal ist ein solches Signal, das nur zwei mögliche Werte annimmt.
:::
:::karte begriff digitales Signal
Was ist ein digitales Signal, und warum arbeitet ein Rechner mit solchen Signalen?
---
Ein digitales Signal ist zeitdiskret und zusätzlich in der Amplitude gestuft (quantisiert). Ein Rechner braucht diese Stufung, weil er nur endlich viele Zahlen darstellen kann.
--- falsch
Ein digitales Signal ist zeitdiskret, seine Werte sind aber beliebig genau. Ein Rechner kann solche Werte speichern, weil Gleitkommazahlen jede reelle Zahl exakt darstellen.
--- falsch
Ein digitales Signal ist in der Zeit kontinuierlich und nur in der Amplitude gestuft. Ein Rechner braucht diese Stufung, weil er nur endlich viele Zahlen darstellen kann.
--- falsch
Ein digitales Signal kennt nur die beiden Werte 0 und 1. Ein Rechner arbeitet damit, weil seine Schaltungen nur zwei Zustände unterscheiden und jedes Signal so übertragen wird.
:::
:::karte begriff Abtastwerte
Was sind die Abtastwerte eines Signals $s(t)$, das im festen Takt $T$ gemessen wird?
---
Die Werte $s(nT)$ des Signals zu den Zeitpunkten $nT$ mit ganzzahligem $n$. Diese Zahlenfolge speichert ein Rechner anstelle der Funktion $s(t)$.
--- falsch
Die Mittelwerte von $s(t)$ über jeweils ein Intervall der Länge $T$. Diese Zahlenfolge speichert ein Rechner anstelle der Funktion, weil Mittelwerte unempfindlich gegen Störungen sind.
--- falsch
Die Werte $s(nT)$ zu den Zeitpunkten $nT$, jedoch nur die von null verschiedenen. Die Nullen zwischen ihnen werden weggelassen, weil sie keine Information tragen.
--- falsch
Die Werte der Ableitung von $s(t)$ zu den Zeitpunkten $nT$. Aus ihnen setzt ein Rechner das Signal durch Aufsummieren wieder zusammen, deshalb genügt ein fester Takt.
:::
:::karte formel Realer Abtaster
Wie beschreibt man einen realen Abtaster, der in jedem Takt $T$ für die kurze Zeit $T_0$ einen Schalter schließt?
---
$s_0(t)=s(t)\sum_{n=-\infty}^{\infty}\operatorname{rect}\Bigl(\frac{t-nT}{T_0}\Bigr)$: Das Signal wird mit einer periodischen Folge von Rechtecken der Breite $T_0$ im Abstand $T$ multipliziert. Zwischen den Rechtecken ist $s_0(t)$ null.
--- falsch
$s_0(t)=s(t)*\sum_n\operatorname{rect}\bigl(\frac{t-nT}{T_0}\bigr)$: Das Signal wird mit einer periodischen Folge von Rechtecken gefaltet, sodass jedes Rechteck den Mittelwert des Signals über die Zeit $T_0$ bildet.
--- falsch
$s_0(t)=s(t)\sum_n\operatorname{rect}\bigl(\frac{t-nT_0}{T}\bigr)$: Das Signal wird mit Rechtecken der Breite $T$ im Abstand $T_0$ multipliziert, weil der Schalter die ganze Taktzeit über geschlossen bleibt.
--- falsch
$s_0(t)=s(t)+\sum_n\operatorname{rect}\bigl(\frac{t-nT}{T_0}\bigr)$: Zum Signal wird in jedem Takt ein Rechteckimpuls der Breite $T_0$ addiert, der den Schaltvorgang im Signal markiert.
:::
:::karte begriff idealer Abtaster
Was versteht man unter dem idealen Abtaster, und wie entsteht er aus dem realen?
---
Man macht die Schließzeit $T_0$ des Schalters immer kürzer und ersetzt das Rechteck mathematisch durch einen Dirac-Impuls. Der ideale Abtaster multipliziert das Signal also mit einem Dirac-Kamm: $s_\mathrm a(t)=s(t)\sum_{n=-\infty}^{\infty}\delta(t-nT)$.
--- falsch
Man macht die Schließzeit $T_0$ immer länger, bis sie den ganzen Takt $T$ füllt. Der ideale Abtaster hält dann jeden Wert bis zum nächsten Takt fest und liefert eine lückenlose Treppenkurve.
--- falsch
Man macht den Takt $T$ immer kürzer, bis er gegen null geht. Der ideale Abtaster misst dann zu jedem Zeitpunkt und gibt das Signal $s(t)$ unverändert und ohne jeden Informationsverlust weiter, sodass man gar keine einzelnen Werte mehr braucht.
--- falsch
Man ersetzt das Rechteck durch einen Dirac-Impuls und addiert den Dirac-Kamm zum Signal: $s(t)+\sum_n\delta(t-nT)$. Die Impulse markieren dann die Zeitpunkte, zu denen der Schalter gemessen hat.
:::
:::karte formel Ideal abgetastetes Signal
Wie sieht das ideal abgetastete Signal $s_\mathrm a(t)$ aus, wenn man es durch die Abtastwerte ausdrückt, und welche Eigenschaft benutzt man dafür?
---
$s_\mathrm a(t)=\sum_{n=-\infty}^{\infty}s(nT)\,\delta(t-nT)$: eine Folge von Dirac-Impulsen, jeder mit einem Abtastwert als Gewicht. Man benutzt die Siebeigenschaft $s(t)\delta(t-nT)=s(nT)\delta(t-nT)$.
--- falsch
$s_\mathrm a(t)=\sum_{n=-\infty}^{\infty}s(nT)$: die Summe aller Abtastwerte, also eine einzige Zahl. Man benutzt die Siebeigenschaft, nach der jeder Dirac-Impuls bei der Integration den Wert 1 ergibt.
--- falsch
$s_\mathrm a(t)=\sum_{n=-\infty}^{\infty}s(nT)\,\delta(t-nT)$: eine Folge von Dirac-Impulsen mit den Abtastwerten als Gewichten. Man benutzt dafür, dass das Signal $s(t)$ zwischen den Abtastpunkten null ist, weil der Abtaster dort nichts misst.
--- falsch
$s_\mathrm a(t)=\sum_{n=-\infty}^{\infty}s(nT)\operatorname{rect}\bigl(\frac{t-nT}{T}\bigr)$: eine Treppe aus Rechtecken der Höhe $s(nT)$. Man benutzt die Siebeigenschaft, die jeden Impuls zu einem Rechteck der Breite $T$ verbreitert.
:::
:::karte zusammenhang Abtasten mit Dirac-Impulsen
Warum beschreibt man das abgetastete Signal als Folge gewichteter Dirac-Impulse und nicht nur als Zahlenfolge $s(nT)$?
---
In dieser Form ist das abgetastete Signal wieder eine Funktion der kontinuierlichen Zeit. Deshalb lässt es sich mit allen Werkzeugen für kontinuierliche Signale behandeln, etwa mit der Fourier-Transformation und der Faltung.
--- falsch
Weil Dirac-Impulse die Werte zwischen den Abtastpunkten speichern. Die Zahlenfolge allein verliert diese Zwischenwerte, die Impulsfolge dagegen enthält das vollständige Signal $s(t)$ samt seinem Verlauf zwischen den Abtastpunkten.
--- falsch
Weil ein realer Abtaster genau solche Impulse erzeugt. Die Darstellung bildet die Schaltung exakt nach; eine Zahlenfolge würde dagegen die endliche Schließzeit des Schalters vernachlässigen.
--- falsch
Weil eine Zahlenfolge kein Spektrum haben kann. Erst die Dirac-Impulse machen aus den Werten ein Signal mit Energie, und nur Signale mit endlicher Energie lassen sich überhaupt transformieren.
:::
::::

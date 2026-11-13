---
title: Stufe 9: FFT und schnelle Faltung
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Abtastung und zeitdiskrete Systeme
adresse: elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme
knoten: Kapitel 4: Abtastung und zeitdiskrete Systeme
order: 3241000
summary: Die DFT braucht M 2 Multiplikationen.
tags: schnelle Fourier-Transformation, zyklische
lang: de
---

<span class="anker" id="stufe-9"></span>

:::zweck
Die DFT braucht $M^2$ Multiplikationen. Die FFT kommt mit ungefähr $M\,\mathrm{lb}\,M$ aus. Damit wird auch die Faltung über den Frequenzbereich schnell.
:::

**Die Idee der FFT.** Mit $W_M=\mathrm{e}^{-\mathrm{j}2\pi/M}$ ist $S_d(k)=\sum_ns_d(n)W_M^{kn}$. Für gerades $M$ teilt man in Werte mit geradem und ungeradem Index:

<span class="anker" id="gl-9-1"></span>
$$S_d(k)=\underbrace{\sum_{n=0}^{M/2-1}s_d(2n)\,W_{M/2}^{kn}}_{S_{d,1}(k)}+W_M^k\underbrace{\sum_{n=0}^{M/2-1}s_d(2n+1)\,W_{M/2}^{kn}}_{S_{d,2}(k)}, \tag{9.1}$$

denn $W_M^{2kn}=W_{M/2}^{kn}$. Statt einer DFT der Länge $M$ braucht man zwei der Länge $M/2$ und $M$ Multiplikationen mit $W_M^k$, also $2(M/2)^2+M$ statt $M^2$. Beide Teil-DFTs sind periodisch mit $M/2$, deshalb liefern sie auch die Werte für $k\ge M/2$. Ist $M$ eine Zweierpotenz, wiederholt man die Teilung $\mathrm{lb}\,M$-mal. Der Aufwand sinkt auf etwa $M\,\mathrm{lb}\,M$. Bei $M=1024$ sind das 10 240 statt 1 048 576 Multiplikationen, rund hundertmal weniger. Das ist die __schnelle Fourier-Transformation__ (FFT).

**Zyklische Faltung.** Für periodische Folgen der Periode $M$ gilt die __zyklische__ (periodische) Faltung

<span class="anker" id="gl-9-2"></span>
$$g_d(n)=\sum_{m=0}^{M-1}s_d(m)\,h_d\bigl((n-m)\bmod M\bigr)\;\circ\!\!-\!\!\bullet\;G_d(k)=S_d(k)\,H_d(k). \tag{9.2}$$

Sie ist das periodisch wiederholte Ergebnis der gewöhnlichen Faltung. Ist $M$ zu klein, überlappen die Wiederholungen. Für $s=(1,1,1)$ und $h=(1,2)$ ist die gewöhnliche Faltung $(1,3,3,2)$ mit vier Werten. Mit $M=3$ fällt der letzte Wert auf den ersten: $(3,3,3)$. Mit $M=4$ stimmt es: $(1,3,3,2)$. Allgemein muss $M\ge M_1+M_2-1$ sein ($M_1$, $M_2$: Längen der beiden Folgen), dazu füllt man mit Nullen auf.

**Schnelle Faltung.** Statt die Faltungssumme direkt auszurechnen, transformiert man beide Folgen mit der FFT, multipliziert und transformiert zurück. Ein beliebig langes Signal zerlegt man in Blöcke, faltet jeden Block einzeln und addiert die Ergebnisse. Das ist erlaubt, weil die Faltung distributiv ist:

$$s(n)*h(n)=\Bigl[\sum_is_i(n)\Bigr]*h(n)=\sum_i\bigl[s_i(n)*h(n)\bigr].$$

:::aufgabe Aufgabe 9 ★★ Zyklisch oder linear
<span class="anker" id="aufg-9"></span>

<ol class="al">

<li>

Rechne die zyklische Faltung von $(1,1,1)$ und $(1,2,0)$ mit $M=3$ von Hand. Welcher Wert der linearen Faltung ist wohin gewandert?

</li>

<li>

Ein Signal mit 1000 Werten soll mit einem Filter mit 25 Werten über die DFT gefaltet werden. Wie lang muss die DFT mindestens sein?

</li>

</ol>

:::loesung
(a) $g(0)=s_0h_0+s_1h_2+s_2h_1=1+0+2=3$, $g(1)=s_0h_1+s_1h_0+s_2h_2=2+1+0=3$, $g(2)=s_0h_2+s_1h_1+s_2h_0=0+2+1=3$. Der vierte Wert der linearen Faltung (2 bei $n=3$) ist zyklisch auf $n=0$ gewandert: $1+2=3$.

(b) Mindestens $1000+25-1=1024$. Das ist praktischerweise eine Zweierpotenz.
:::
:::

::::formelsammlung
**DFT in Kurzschreibweise**

$$S_d(k)=\sum_ns_d(n)W_M^{kn}$$

Mit $W_M=\mathrm{e}^{-\mathrm{j}2\pi/M}$.

**Teilung in gerade und ungerade Indizes**

$$S_d(k)=\sum_{n=0}^{M/2-1}s_d(2n)\,W_{M/2}^{kn}+W_M^k\sum_{n=0}^{M/2-1}s_d(2n+1)\,W_{M/2}^{kn}$$

$M$ gerade; denn $W_M^{2kn}=W_{M/2}^{kn}$. Zwei DFTs der Länge $M/2$, periodisch mit $M/2$ (sie liefern auch die Werte für $k\ge M/2$), und $M$ Multiplikationen mit $W_M^k$.

**Aufwand der FFT**

$$M\,\mathrm{lb}\,M$$

Ungefähre Zahl der Multiplikationen statt $M^2$ bei der direkten DFT, für $M$ als Zweierpotenz: Die Teilung, die allein $2(M/2)^2+M$ statt $M^2$ kostet, wird $\mathrm{lb}\,M$-mal wiederholt.

**Zyklische Faltung**

$$g_d(n)=\sum_{m=0}^{M-1}s_d(m)\,h_d\bigl((n-m)\bmod M\bigr)\;\circ\!\!-\!\!\bullet\;G_d(k)=S_d(k)\,H_d(k)$$

Für Folgen der Periode $M$; das periodisch wiederholte Ergebnis der gewöhnlichen Faltung.

**Länge für die lineare Faltung über die DFT**

$$M\ge M_1+M_2-1$$

$M_1$, $M_2$ Längen der beiden Folgen; man füllt mit Nullen auf. Sonst überlappen die Wiederholungen.

**Blockweise Faltung**

$$s(n)*h(n)=\Bigl[\sum_is_i(n)\Bigr]*h(n)=\sum_i\bigl[s_i(n)*h(n)\bigr]$$

Die Faltung ist distributiv: Ein langes Signal wird in Blöcke zerlegt, jeder Block einzeln (schnell über die FFT) gefaltet, die Ergebnisse werden addiert.
::::

::::lernkarten
:::karte begriff schnelle Fourier-Transformation
Was ist die schnelle Fourier-Transformation (FFT), und wie viele Multiplikationen spart sie?
---
Ein Rechenverfahren für die DFT, das die Folge wiederholt in Werte mit geradem und ungeradem Index teilt. Bei $M$ als Zweierpotenz sinkt der Aufwand von $M^2$ auf etwa $M\,\mathrm{lb}\,M$ Multiplikationen, bei $M=1024$ rund hundertmal weniger.
--- falsch
Eine Näherung der DFT, die nur die Werte mit geradem Index berechnet und die übrigen interpoliert. Der Aufwand sinkt von $M^2$ auf $M^2/2$ Multiplikationen, das Ergebnis ist dafür etwas ungenauer als bei der DFT.
--- falsch
Eine eigene Transformation mit einem anderen Spektrum als die DFT, die nur für Zweierpotenzen definiert ist. Sie braucht $M\,\mathrm{lb}\,M$ Multiplikationen, ihr Ergebnis muss aber anschließend noch in die DFT umgerechnet werden, was weitere Schritte kostet.
--- falsch
Ein Rechenverfahren für die DFT, das alle $M^2$ Multiplikationen gleichzeitig ausführt. Es spart keine Rechenschritte, ist aber schneller, weil es die Arbeit auf viele Recheneinheiten verteilt.
:::
:::karte herleitung Teilung in gerade und ungerade Indizes
Wie zerlegt man für gerades $M$ die DFT $S_d(k)=\sum_ns_d(n)W_M^{kn}$ mit $W_M=\mathrm{e}^{-\mathrm{j}2\pi/M}$ in zwei DFTs der Länge $M/2$?
---
Man teilt die Summe in die Werte mit geradem Index $2n$ und die mit ungeradem Index $2n+1$, weil so zwei halb so lange Summen entstehen.
---
Bei den geraden Werten wird $W_M^{2kn}=W_{M/2}^{kn}$, weil das Quadrat von $W_M$ gleich $W_{M/2}$ ist; die erste Summe ist also eine DFT der Länge $M/2$.
---
Bei den ungeraden Werten zieht man den Faktor $W_M^k$ vor die Summe, weil $W_M^{k(2n+1)}=W_M^k\,W_M^{2kn}$ ist; übrig bleibt wieder eine DFT der Länge $M/2$.
---
Für $k\ge M/2$ liefern die beiden Teil-DFTs ihre Werte erneut, weil sie periodisch mit $M/2$ sind; man braucht sie also nur einmal zu berechnen.
---
Statt $M^2$ braucht man so $2(M/2)^2+M$ Multiplikationen, weil zwei DFTs der Länge $M/2$ und $M$ Multiplikationen mit $W_M^k$ anfallen.
:::
:::karte zusammenhang Aufwand der FFT
Warum sinkt der Aufwand der FFT auf etwa $M\,\mathrm{lb}\,M$ Multiplikationen, wenn $M$ eine Zweierpotenz ist?
---
Jede Teilung ersetzt eine DFT durch zwei halb so lange und kostet nur etwa $M$ zusätzliche Multiplikationen. Bei einer Zweierpotenz lässt sich die Teilung $\mathrm{lb}\,M$-mal wiederholen, das ergibt zusammen etwa $M\,\mathrm{lb}\,M$.
--- falsch
Weil die FFT nur jeden $\mathrm{lb}\,M$-ten Wert des Spektrums berechnet und die übrigen aus der Symmetrie reeller Folgen ergänzt. Bei einer Zweierpotenz liegen diese Werte gleichmäßig über die Periode verteilt.
--- falsch
Weil bei einer Zweierpotenz alle Faktoren $W_M^{kn}$ gleich 1 oder $-1$ sind. Multiplikationen damit sind nur Vorzeichenwechsel, und es bleiben etwa $\mathrm{lb}\,M$ echte Multiplikationen für jeden Spektralwert.
--- falsch
Weil die Teilung nur einmal möglich ist, dann aber $\mathrm{lb}\,M$ gleich lange Teilfolgen entstehen. Jede dieser Teilfolgen braucht $M$ Multiplikationen, zusammen ergibt das also $M\,\mathrm{lb}\,M$.
:::
:::karte begriff zyklische Faltung
Was ist die zyklische Faltung zweier Folgen mit der Periode $M$, und was wird aus ihr unter der DFT?
---
Die Faltung über eine Periode mit Indizes modulo $M$: $g_d(n)=\sum_{m=0}^{M-1}s_d(m)\,h_d\bigl((n-m)\bmod M\bigr)$. Unter der DFT wird sie zum Produkt, $G_d(k)=S_d(k)\,H_d(k)$. Sie ist das periodisch wiederholte Ergebnis der gewöhnlichen Faltung.
--- falsch
Die gewöhnliche Faltung zweier Folgen, deren Ergebnis man nach $M$ Werten abschneidet: $g_d(n)=\sum_{m=0}^{n}s_d(m)\,h_d(n-m)$. Unter der DFT wird sie zum Produkt, $G_d(k)=S_d(k)\,H_d(k)$.
--- falsch
Die Faltung über eine Periode mit Indizes modulo $M$. Unter der DFT wird sie zur zyklischen Faltung der Spektren, weil beide Seiten der DFT periodisch sind und sich das Verfahren dort wiederholt.
--- falsch
Die mehrfache Faltung einer Folge mit sich selbst, bis sich das Ergebnis nach $M$ Schritten wiederholt. Unter der DFT wird sie zur $M$-ten Potenz des Spektrums, $G_d(k)=S_d(k)^M$.
:::
:::karte zusammenhang Zyklische und lineare Faltung
Wie hängt die zyklische Faltung mit der gewöhnlichen zusammen, etwa bei $s=(1,1,1)$ und $h=(1,2)$ mit $M=3$ und mit $M=4$?
---
Sie ist das mit $M$ periodisch wiederholte Ergebnis der gewöhnlichen Faltung $(1,3,3,2)$. Bei $M=3$ überlappen die Wiederholungen, der letzte Wert fällt auf den ersten: $(3,3,3)$. Bei $M=4$ stimmt das Ergebnis: $(1,3,3,2)$.
--- falsch
Sie ist die gewöhnliche Faltung, nach $M$ Werten abgeschnitten. Bei $M=3$ fehlt deshalb einfach der letzte Wert: $(1,3,3)$. Bei $M=4$ stimmt das Ergebnis mit der gewöhnlichen Faltung überein: $(1,3,3,2)$.
--- falsch
Sie ist mit der gewöhnlichen immer gleich, nur in Stücken zu $M$ Werten aufgeschrieben. Bei $M=3$ ergibt sich $(1,3,3)$, und der letzte Wert wird eine Periode später angehängt; bei $M=4$ entsteht $(1,3,3,2)$.
--- falsch
Sie ist das mit $M$ periodisch wiederholte Ergebnis, wobei überlappende Werte sich auslöschen. Bei $M=3$ fällt der letzte Wert auf den ersten und tilgt ihn: $(0,3,3)$. Bei $M=4$ stimmt das Ergebnis: $(1,3,3,2)$.
:::
:::karte formel Mindestlänge der DFT
Wie lang muss die DFT mindestens sein, wenn man zwei Folgen mit $M_1$ und $M_2$ Werten über die DFT linear falten will?
---
$M\ge M_1+M_2-1$; die Folgen füllt man dazu mit Nullen auf. Dann überlappen die periodischen Wiederholungen nicht. Ein Signal mit 1000 Werten und ein Filter mit 25 Werten brauchen also mindestens $1000+25-1=1024$.
--- falsch
So lang wie die längere der beiden Folgen; die kürzere füllt man mit Nullen auf. Mehr ist nicht nötig, weil die DFT ohnehin periodisch ist. Ein Signal mit 1000 Werten und ein Filter mit 25 Werten brauchen also 1000.
--- falsch
$M\ge M_1\cdot M_2$, weil jeder Wert der einen Folge mit jedem Wert der anderen multipliziert wird. Ein Signal mit 1000 Werten und ein Filter mit 25 Werten brauchen also mindestens 25 000.
--- falsch
$M\ge M_1+M_2$, damit am Ende eine Null als Abstand bleibt. Ohne diesen Abstand berührt das Ende der Faltung den Anfang der nächsten Wiederholung. Bei 1000 und 25 Werten also mindestens 1025.
:::
:::karte zusammenhang Schnelle Faltung
Wie faltet man ein beliebig langes Signal schnell mit einem Filter, und warum ist die Zerlegung in Blöcke erlaubt?
---
Man zerlegt das Signal in Blöcke, transformiert jeden Block und das Filter mit der FFT, multipliziert, transformiert zurück und addiert die Ergebnisse. Erlaubt ist das, weil die Faltung distributiv ist: $s(n)*h(n)=\sum_i\bigl[s_i(n)*h(n)\bigr]$.
--- falsch
Man rechnet die Faltungssumme direkt aus, aber nur für jeden zweiten Wert, und interpoliert die übrigen. Erlaubt ist das, weil das Ergebnis einer Faltung stets glatter ist als das Signal selbst und keine Sprünge mehr enthält.
--- falsch
Man zerlegt das Signal in Blöcke und faltet nur den ersten Block, weil die Faltung verschiebungsinvariant ist. Alle übrigen Blöcke liefern dasselbe Ergebnis, nur zeitlich verschoben, und werden einfach kopiert.
--- falsch
Man transformiert das ganze Signal auf einmal mit der FFT und multipliziert mit dem Spektrum des Filters. Blöcke sind nicht erlaubt, weil die Faltung an den Blockgrenzen nicht distributiv ist.
:::
::::

---
title: Stufe 10: Der R-2R-Wandler
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Quellen und Ersatzquellen
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen
knoten: Kapitel 5: Quellen und Ersatzquellen
order: 1151200
summary: Ein Prozessor kennt nur Bits, ein Lautsprecher braucht eine Spannung.
tags: Digital-Analog-Wandler
lang: de
---

<span class="anker" id="stufe-10"></span>

:::zweck
Ein Prozessor kennt nur Bits, ein Lautsprecher braucht eine Spannung. Der R-2R-Wandler übersetzt das. Er ist Überlagerung und Ersatzquelle in einer einzigen Schaltung.
:::

**Die Idee.** Ein __Digital-Analog-Wandler__ macht aus einer Binärzahl mit den Bits $d_2d_1d_0$ eine Spannung. In Abb. [12](#abb-12) legt jeder Schalter seinen 2$R$-Widerstand entweder an $U_\mathrm{ref}$ (Bit 1) oder an 0 V (Bit 0). Ein Schalter auf 0 V ist eine abgeschaltete Spannungsquelle. Die Überlagerung steckt also schon im Aufbau: Jedes gesetzte Bit ist eine Quelle, alle anderen sind Drähte. Die Leiter aus $R$ und $2R$ ist so bemessen, dass jede Sprosse die Wirkung halbiert.

:::abbildung et1/k5r2r 12
R-2R-Wandler für drei Bit in der Stellung 101. Jeder Umschalter verbindet seinen Widerstand mit $U_\mathrm{ref}$ oder mit Masse. Abgegriffen wird rechts oben.
:::

:::satz Satz 10.1 (R-2R-Leiter)
<span class="anker" id="satz-10-1"></span>

Für den Wandler aus Abb. [12](#abb-12) bei offenem Ausgang gilt

<span class="anker" id="gl-10-1"></span>
$$U_\mathrm{aus}=U_\mathrm{ref}\left(\frac{d_2}{2}+\frac{d_1}{4}+\frac{d_0}{8}\right),\qquad R_\mathrm{i}=R. \tag{10.1}$$
:::

⁠**So liest man das:** $d_k$ ist 0 oder 1, $U_\mathrm{ref}$ die feste Bezugsspannung (einige Volt), $R$ meist einige k$\Omega$. Das höchstwertige Bit trägt die halbe Bezugsspannung bei, jedes weitere die Hälfte des vorigen. $R_\mathrm{i}$ hängt nicht von der Schalterstellung ab: Beim Abschalten wird $U_\mathrm{ref}$ zu 0 V, und dann führt jeder Zweig nach Masse, wie auch immer sein Schalter steht. **Gültigkeit:** ideale Schalter ohne eigenen Widerstand, Ausgang unbelastet.

:::herleitung Ersatzquelle von links nach rechts
Am linken Knoten liegen 2$R$ gegen Masse und 2$R$ gegen $U_0=d_0U_\mathrm{ref}$. Das ist eine Ersatzquelle mit $\frac12U_0$ und $2R\parallel2R=R$. Mit dem Längswiderstand werden daraus $\frac12U_0$ und $2R$. Am nächsten Knoten trifft das auf 2$R$ gegen $U_1=d_1U_\mathrm{ref}$: wieder zwei gleiche Zweige, also die Mittelwertsbildung aus [(7.2)](quellen-zusammenschalten.html#gl-7-2), die Ersatzquelle $\frac12\bigl(\frac12U_0+U_1\bigr)$ und wieder $R$. Der letzte Knoten wiederholt das:

$$U_\mathrm{aus}=\tfrac12\Bigl(\tfrac12\bigl(\tfrac12U_0+U_1\bigr)+U_2\Bigr)=\tfrac12U_2+\tfrac14U_1+\tfrac18U_0.$$

Dieselbe Zahl liefert die Überlagerung. Beispiel Quelle $U_1$: Am mittleren Knoten sieht sie links 2$R$ und rechts $R+2R=3R$, zusammen $\frac65R$. Der Teiler ergibt dort $\frac{6/5}{6/5+2}=\frac38U_1$. Der Weg zum Ausgang teilt noch einmal mit $\frac{2R}{R+2R}=\frac23$, also $\frac38\cdot\frac23=\frac14$.
:::

::::beispiel
Mit $U_\mathrm{ref}=8$ V und $R=1$ k$\Omega$ wiegen die Bits 4 V, 2 V und 1 V. Die Stellung 101 ergibt 5 V. Eine Last mit $R_\mathrm{L}=R$ bildet mit $R_\mathrm{i}$ einen Teiler und halbiert das auf 2,5 V. Deshalb folgt in echten Wandlern ein Operationsverstärker ([Kapitel 11](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-operationsverstarker/der-operationsverstaerker.html)) mit sehr hohem Eingangswiderstand: Er zieht praktisch keinen Strom, die Leiter bleibt im Leerlauf.
::::

⁠**Grenzfälle:** Stellung 000 ergibt 0 V, Stellung 111 ergibt 7 V, eine Stufe unter $U_\mathrm{ref}$.

:::ltspice Der Wandler zählt
⁠**Zeichnen:** Abb. [12](#abb-12) ohne Schalter: 2$R$ von Knoten `n0` nach Masse, dann je 2$R$ von `n0`, `n1`, `n2` zu einer Quelle `voltage` gegen Masse und $R$ zwischen den Knoten, $R=1$ k$\Omega$. Die Quellen zählen binär: `PULSE(0 8 1m 1u 1u 1m 2m)`, `PULSE(0 8 2m 1u 1u 2m 4m)`, `PULSE(0 8 4m 1u 1u 4m 8m)`.

⁠**Direktive:** `.tran 8m`

⁠**Was du siehst:** `V(n2)` ist eine Treppe mit Stufen von 1 V, von 0 V bis 7 V. Mit einer Last von 1 k$\Omega$ an `n2` steigt sie nur noch bis 3,5 V. Mit 3 k$\Omega$ erscheint auf der obersten Stufe dein Ergebnis aus Aufgabe [12](#aufg-12)(c).
:::

:::frage Wozu dient der einzelne 2$R$-Widerstand ganz links?
Er macht die Leiter gleichmäßig. Mit ihm ist alles links von jedem Knoten eine Ersatzquelle mit $2R$, genau wie der Zweig des eigenen Schalters. Nur dann entstehen zwei gleiche Zweige und ein reiner Mittelwert. Ohne ihn wäre der linke Zweig $3R$ groß, und die Gewichte wären nicht mehr binär.
:::

:::aufgabe Aufgabe 12 ★★ Vier Bit
<span class="anker" id="aufg-12"></span>

(a) Ein Wandler mit vier Bit läuft an $U_\mathrm{ref}=16$ V. Wie groß sind die Stufe, der Höchstwert und die Spannung bei 1011? (b) Wie groß ist eine Stufe bei acht Bit an 5 V? (c) Der Drei-Bit-Wandler aus dem Beispiel steht auf 111 und speist $R_\mathrm{L}=3R$. Welche Spannung stellt sich ein?

:::loesung
(a) Stufe $16\,\mathrm{V}/2^4=1$ V. Höchstwert $15$ V. 1011: $8+0+2+1=11$ V. Die Formel läuft weiter mit $d_3/2+d_2/4+d_1/8+d_0/16$.

(b) $5\,\mathrm{V}/256=19{,}5$ mV.

(c) Leerlauf 7 V, Innenwiderstand $R$. Teiler: $7\,\mathrm{V}\cdot\frac{3R}{R+3R}=5{,}25$ V.
:::
:::

::::formelsammlung
**R-2R-Leiter mit drei Bit**

$$U_\mathrm{aus}=U_\mathrm{ref}\left(\frac{d_2}{2}+\frac{d_1}{4}+\frac{d_0}{8}\right),\qquad R_\mathrm{i}=R$$

$d_k$ ist 0 oder 1, $U_\mathrm{ref}$ die feste Bezugsspannung, $R$ meist einige k$\Omega$. Jedes Bit trägt die Hälfte des vorigen bei. $R_\mathrm{i}$ hängt nicht von der Schalterstellung ab, denn abgeschaltet führt jeder Zweig nach Masse. Gilt für ideale Schalter und unbelasteten Ausgang; eine Last bildet mit $R_\mathrm{i}$ einen Teiler.

**Ersatzquellen von links nach rechts**

$$U_\mathrm{aus}=\tfrac12\Bigl(\tfrac12\bigl(\tfrac12U_0+U_1\bigr)+U_2\Bigr)=\tfrac12U_2+\tfrac14U_1+\tfrac18U_0$$

$U_0=d_0U_\mathrm{ref}$, $U_1=d_1U_\mathrm{ref}$ und entsprechend $U_2$ sind die Spannungen an den Schaltern. An jedem Knoten treffen zwei gleiche Zweige mit $2R$ zusammen; das ergibt den Mittelwert ihrer Spannungen und wieder $R$.

**Vier Bit**

$$U_\mathrm{aus}=U_\mathrm{ref}\,(d_3/2+d_2/4+d_1/8+d_0/16)$$

Die Formel läuft mit jedem weiteren Bit so weiter. Eine Stufe ist bei vier Bit an 16 V gleich $16\,\mathrm{V}/2^4=1$ V, der Höchstwert 15 V.
::::

::::lernkarten
:::karte begriff Digital-Analog-Wandler
Was leistet ein Digital-Analog-Wandler, etwa zwischen einem Prozessor und einem Lautsprecher?
---
Er macht aus einer Binärzahl, etwa mit den Bits $d_2d_1d_0$, eine Spannung. Der Prozessor kennt nur Bits, der Lautsprecher braucht eine Spannung.
--- falsch
Er macht aus einer Spannung eine Binärzahl, damit der Prozessor sie verarbeiten kann. Der Lautsprecher liefert ihm dabei die Spannung.
--- falsch
Er verstärkt die Spannung eines Prozessorausgangs, damit sie einen Lautsprecher treiben kann. Die Bits bleiben dabei unverändert.
--- falsch
Er wandelt Wechselspannung in Gleichspannung, damit der Prozessor seine Bits speichern kann. Ohne ihn gingen die Bits verloren.
:::
:::karte zusammenhang Überlagerung im Aufbau
Warum steckt die Überlagerung schon im Aufbau eines R-2R-Wandlers?
---
Jeder Schalter legt seinen 2$R$-Widerstand an $U_\mathrm{ref}$ (Bit 1) oder an 0 V (Bit 0). Ein Schalter auf 0 V ist eine abgeschaltete Quelle, also ein Draht. Jedes gesetzte Bit ist eine Quelle, ihre Wirkungen addieren sich.
--- falsch
Weil alle Schalter in Reihe liegen und sich ihre Spannungen deshalb wie bei Batterien in Reihe addieren. Jedes gesetzte Bit liefert dieselbe Teilspannung $U_\mathrm{ref}$ zum Ausgang.
--- falsch
Weil der Wandler für jedes Bit eine eigene Quelle mit eigener Spannung braucht, $U_\mathrm{ref}$, $U_\mathrm{ref}/2$ und $U_\mathrm{ref}/4$. Diese drei Spannungen addieren sich am Ausgang, die Widerstände der Leiter verbinden sie nur miteinander.
--- falsch
Weil ein Schalter auf 0 V eine Lücke im Netz erzeugt. Nur die gesetzten Bits bleiben angeschlossen, und ihre Spannungen bilden am Ausgang den einfachen Mittelwert, gleich wie viele Bits gesetzt sind.
:::
:::karte formel R-2R-Leiter
Welche Ausgangsspannung und welchen Innenwiderstand hat ein R-2R-Wandler für drei Bit bei offenem Ausgang?
---
$U_\mathrm{aus}=U_\mathrm{ref}\left(\frac{d_2}{2}+\frac{d_1}{4}+\frac{d_0}{8}\right)$ und $R_\mathrm{i}=R$, für ideale Schalter. Das höchstwertige Bit trägt die halbe Bezugsspannung bei, jedes weitere die Hälfte des vorigen.
--- falsch
$U_\mathrm{aus}=U_\mathrm{ref}\left(\frac{d_2}{2}+\frac{d_1}{4}+\frac{d_0}{8}\right)$ und $R_\mathrm{i}=2R$. Das niedrigstwertige Bit trägt die halbe Bezugsspannung bei, jedes höhere die Hälfte des vorigen.
--- falsch
$U_\mathrm{aus}=U_\mathrm{ref}\left(\frac{d_2}{3}+\frac{d_1}{3}+\frac{d_0}{3}\right)$ und $R_\mathrm{i}=R$. Jedes gesetzte Bit trägt ein Drittel der Bezugsspannung bei, weil die Leiter aus drei gleich gebauten Sprossen besteht.
--- falsch
$U_\mathrm{aus}=U_\mathrm{ref}\left(\frac{d_2}{2}+\frac{d_1}{4}+\frac{d_0}{8}\right)$, aber $R_\mathrm{i}$ hängt von der Schalterstellung ab: Je mehr Bits gesetzt sind, desto kleiner ist der Innenwiderstand.
:::
:::karte zusammenhang Innenwiderstand unabhängig von den Bits
Warum hängt der Innenwiderstand eines R-2R-Wandlers nicht von der Schalterstellung ab?
---
Beim Abschalten wird $U_\mathrm{ref}$ zu 0 V. Dann führt jeder Zweig nach Masse, wie auch immer sein Schalter steht, und das abgeschaltete Netz ist in jeder Stellung dasselbe.
--- falsch
Weil die Schalter selbst einen Widerstand von genau $R$ haben, der in jeder Stellung gleich bleibt und deshalb allein den Innenwiderstand des Wandlers festlegt.
--- falsch
Er hängt davon ab: Ein gesetztes Bit legt seinen Zweig an $U_\mathrm{ref}$ und nimmt ihn damit aus der Rechnung für $R_\mathrm{i}$ heraus, sodass $R_\mathrm{i}$ wächst.
--- falsch
Weil bei offenem Ausgang kein Strom fließt. Sobald eine Last anliegt, ändert sich $R_\mathrm{i}$ mit jeder Schalterstellung, und die Gewichte der Bits verschieben sich gegeneinander.
:::
:::karte herleitung Ersatzquelle von links nach rechts
Leite die Ausgangsspannung des Drei-Bit-R-2R-Wandlers her, indem du von links nach rechts Knoten für Knoten Ersatzquellen bildest.
---
Am linken Knoten liegen 2$R$ gegen Masse und 2$R$ gegen $U_0=d_0U_\mathrm{ref}$. Das ist eine Ersatzquelle mit $\frac12U_0$ und $2R\parallel2R=R$, weil zwei gleiche Zweige die Spannung halbieren und parallel den halben Widerstand haben.
---
Mit dem Längswiderstand werden daraus $\frac12U_0$ und $2R$, weil der Längswiderstand in Reihe zum Innenwiderstand liegt und bei offenem Ausgang die Leerlaufspannung nicht ändert.
---
Am nächsten Knoten trifft das auf 2$R$ gegen $U_1=d_1U_\mathrm{ref}$. Zwei gleiche Zweige ergeben die Ersatzquelle $\frac12\bigl(\frac12U_0+U_1\bigr)$ und wieder $R$, weil parallele Quellen mit gleichem Innenwiderstand den Mittelwert ihrer Spannungen bilden.
---
Der letzte Knoten wiederholt das: $U_\mathrm{aus}=\tfrac12\Bigl(\tfrac12\bigl(\tfrac12U_0+U_1\bigr)+U_2\Bigr)=\tfrac12U_2+\tfrac14U_1+\tfrac18U_0$, weil derselbe Schritt mit $U_2$ noch einmal halbiert.
:::
:::karte herleitung Gewicht eines Bits durch Überlagerung
Zeige mit der Überlagerung, dass die Quelle $U_1$ des mittleren Bits am Ausgang des Drei-Bit-R-2R-Wandlers mit dem Faktor $\frac14$ wirkt.
---
Alle anderen Quellen sind abgeschaltet und damit Drähte nach Masse, weil die Überlagerung jede Quelle für sich rechnet.
---
Am mittleren Knoten sieht $U_1$ links 2$R$ und rechts $R+2R=3R$, zusammen $\frac65R$, weil links der abgeschaltete linke Teil mit 2$R$ und rechts der Längswiderstand mit dem 2$R$-Zweig des letzten Bits liegt.
---
Der Teiler ergibt dort $\frac{6/5}{6/5+2}=\frac38U_1$, weil $U_1$ über ihren eigenen 2$R$-Zweig gegen diese $\frac65R$ arbeitet.
---
Der Weg zum Ausgang teilt noch einmal mit $\frac{2R}{R+2R}=\frac23$, also $\frac38\cdot\frac23=\frac14$, weil Längswiderstand und 2$R$-Zweig am Ausgang einen Spannungsteiler bilden.
:::
:::karte zusammenhang Der einzelne Widerstand ganz links
Wozu dient der einzelne 2$R$-Widerstand ganz links in der R-2R-Leiter?
---
Er macht die Leiter gleichmäßig: Mit ihm ist alles links von jedem Knoten eine Ersatzquelle mit $2R$, wie der Zweig des eigenen Schalters. So entstehen zwei gleiche Zweige und ein reiner Mittelwert; ohne ihn wären die Gewichte nicht binär.
--- falsch
Er begrenzt den Strom, falls alle Schalter zugleich auf $U_\mathrm{ref}$ stehen und die Leiter sonst zu viel Strom aus der Bezugsquelle zöge. Für die Gewichte der Bits spielt er keine Rolle, man könnte ihn ebenso gut weglassen oder durch einen Draht ersetzen.
--- falsch
Er ist der Lastwiderstand des Wandlers: An ihm wird die Ausgangsspannung abgegriffen, und deshalb muss er genau $2R$ haben, damit die Spannung am Ausgang im richtigen Verhältnis zu $U_\mathrm{ref}$ steht.
--- falsch
Er gleicht den Widerstand der Schalter aus. Ohne ihn wäre der Innenwiderstand um $2R$ kleiner, die Gewichte der Bits blieben aber binär, nur die Ausgangsspannung wäre etwas höher.
:::
:::karte zusammenhang Last am Wandler
Was geschieht mit der Ausgangsspannung eines R-2R-Wandlers, wenn man eine Last $R_\mathrm{L}=R$ anschließt, und was tut man dagegen?
---
Die Last bildet mit $R_\mathrm{i}=R$ einen Teiler und halbiert die Spannung, etwa 5 V auf 2,5 V. Deshalb folgt ein Operationsverstärker mit sehr hohem Eingangswiderstand, der praktisch keinen Strom zieht; die Leiter bleibt im Leerlauf.
--- falsch
Nichts, weil der Wandler wie eine ideale Spannungsquelle wirkt. Die Ausgangsspannung hängt nur von den Bits und von $U_\mathrm{ref}$ ab, gleich welche Last man anschließt; deshalb braucht man hinter der Leiter auch keine weitere Stufe.
--- falsch
Sie verdoppelt sich, weil die Last parallel zu $R_\mathrm{i}$ liegt und den Innenwiderstand halbiert. Man schaltet deshalb einen Vorwiderstand zwischen Wandler und Last, der die Spannung wieder auf den richtigen Wert herunterteilt.
--- falsch
Die Gewichte der Bits verschieben sich, die Spannung bleibt im Mittel aber gleich. Man gleicht die Verschiebung aus, indem man $U_\mathrm{ref}$ etwas erhöht.
:::
:::karte formel Bitgewichte
Wie groß sind bei einem Drei-Bit-R-2R-Wandler mit $U_\mathrm{ref}=8$ V die Beiträge der Bits, und welche Spannungen liefern die Stellungen 101 und 111?
---
Die Bits wiegen 4 V, 2 V und 1 V. Die Stellung 101 ergibt 5 V, die Stellung 111 ergibt 7 V, eine Stufe unter $U_\mathrm{ref}$.
--- falsch
Die Bits wiegen 4 V, 2 V und 1 V. Die Stellung 101 ergibt 5 V, die Stellung 111 ergibt genau $U_\mathrm{ref}=8$ V, den Höchstwert.
--- falsch
Jedes Bit wiegt ein Drittel von 8 V, also 2,67 V. Die Stellung 101 ergibt 5,33 V, die Stellung 111 ergibt 8 V.
--- falsch
Die Bits wiegen 8 V, 4 V und 2 V. Die Stellung 101 ergibt 10 V, die Stellung 111 ergibt 14 V, fast das Doppelte von $U_\mathrm{ref}$.
:::
:::karte formel Mehr Bits
Wie groß ist eine Stufe eines R-2R-Wandlers mit vier Bit an $U_\mathrm{ref}=16$ V, und wie setzt sich die Formel für mehr Bits fort?
---
$16\,\mathrm{V}/2^4=1$ V, der Höchstwert ist 15 V. Die Formel läuft weiter mit $d_3/2+d_2/4+d_1/8+d_0/16$: Jedes weitere Bit halbiert das Gewicht.
--- falsch
$16\,\mathrm{V}/4=4$ V, weil sich die Bezugsspannung gleichmäßig auf die vier Bits verteilt. Der Höchstwert ist 16 V, die Formel bekommt vier gleiche Glieder.
--- falsch
$16\,\mathrm{V}/2^4=1$ V, der Höchstwert ist 16 V. Die Formel läuft weiter mit $d_3/2+d_2/4+d_1/8+d_0/8$, weil das letzte Bit das Gewicht des vorigen übernimmt.
--- falsch
$16\,\mathrm{V}/2^3=2$ V, weil das höchste Bit nicht mitzählt. Der Höchstwert ist 14 V, und jedes weitere Bit verdoppelt das Gewicht des vorigen.
:::
::::

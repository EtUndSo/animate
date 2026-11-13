---
title: Stufe 7: Fourier-Transformation zeitdiskreter Signale
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Abtastung und zeitdiskrete Systeme
adresse: elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme
knoten: Kapitel 4: Abtastung und zeitdiskrete Systeme
order: 3240800
summary: Welches Spektrum hat eine Zahlenfolge?
tags: periodische Faltung
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Welches Spektrum hat eine Zahlenfolge? Es ist das Spektrum des ideal abgetasteten Signals, direkt aus den Abtastwerten berechnet.
:::

Setzt man $s_\mathrm a(t)=\sum_ns(nT)\delta(t-nT)$ in das Fourier-Integral ein, bleibt mit der Siebeigenschaft eine Summe. Normiert auf $T=1$:

:::satz Satz 7.1 (Fourier-Transformation zeitdiskreter Signale)
<span class="anker" id="satz-7-1"></span>

<span class="anker" id="gl-7-1"></span>
$$S_\mathrm a(f)=\sum_{n=-\infty}^{\infty}s(n)\,\mathrm{e}^{-\mathrm{j}2\pi nf},\qquad s(n)=\int_{-1/2}^{1/2}S_\mathrm a(f)\,\mathrm{e}^{\mathrm{j}2\pi nf}\,\mathrm{d} f. \tag{7.1}$$
:::

⁠**So liest man das:** $S_\mathrm a(f)$ ist periodisch mit der Periode 1, das ist die Abtastrate. Eine Periode, $|f|\le\frac12$, enthält alles. Deshalb integriert die Rücktransformation nur über ein Intervall der Länge 1. Die Summe ist eine Fourier-Reihe in $f$, mit den Abtastwerten als Koeffizienten.

::::beispiel
Für $s(n)=\varepsilon(n)\,b^n$ mit $|b|<1$ (geometrische Reihe):

<span class="anker" id="gl-7-2"></span>
$$S_\mathrm a(f)=\sum_{n=0}^{\infty}\bigl(b\,\mathrm{e}^{-\mathrm{j}2\pi f}\bigr)^n=\frac{1}{1-b\,\mathrm{e}^{-\mathrm{j}2\pi f}},\qquad|S_\mathrm a(f)|^2=\frac{1}{1+b^2-2b\cos(2\pi f)}. \tag{7.2}$$

Das ist zugleich der Frequenzgang $H_\mathrm a(f)$ des rekursiven Systems aus Stufe [6](ein-rekursives-system.html#stufe-6). Für $b=0{,}6$: $|H_\mathrm a|=2{,}5$ bei $f=0$, $1{,}60$ bei $f=0{,}1$, $0{,}86$ bei $f=0{,}25$, $0{,}625$ bei $f=0{,}5$ (Abb. [6](#abb-6)). Das System ist ein Tiefpass, aber mit periodischem Frequenzgang: Bei $f=1$ verstärkt es wieder so stark wie bei $f=0$.

:::abbildung et3/k4dtft 6
Betrag des Frequenzgangs des rekursiven Systems mit $b=0{,}6$. Er ist periodisch mit der Abtastrate. Zwischen den roten Linien liegt die eine Periode, die alles beschreibt.
:::
::::

**Faltung und Multiplikation.** Wie bei Funktionen gilt $s(n)*h(n)\;\circ\!\!-\!\!\bullet\;S_\mathrm a(f)H_\mathrm a(f)$. Das Produkt zweier Folgen ergibt die __periodische Faltung__ der Spektren über eine Periode:

<span class="anker" id="gl-7-3"></span>
$$s(n)\cdot h(n)\;\circ\!\!-\!\!\bullet\;\int_{-1/2}^{1/2}S_\mathrm a(\nu)\,H_\mathrm a(f-\nu)\,\mathrm{d}\nu. \tag{7.3}$$

:::aufgabe Aufgabe 7 ★ Gleitender Mittelwert
<span class="anker" id="aufg-7"></span>

$h(n)=\frac13\bigl[\delta(n)+\delta(n-1)+\delta(n-2)\bigr]$ mittelt drei aufeinanderfolgende Werte.

<ol class="al">

<li>

Zeige $H_\mathrm a(f)=\frac13\mathrm{e}^{-\mathrm{j}2\pi f}\bigl[1+2\cos(2\pi f)\bigr]$.

</li>

<li>

Bei welcher Frequenz ist $H_\mathrm a=0$? Welche Schwingung löscht das Filter also vollständig aus, und warum (Tipp: Summe dreier Werte einer Schwingung mit der Periode 3)?

</li>

</ol>

:::loesung
(a) $\frac13\bigl(1+\mathrm{e}^{-\mathrm{j}2\pi f}+\mathrm{e}^{-\mathrm{j}4\pi f}\bigr)=\frac13\mathrm{e}^{-\mathrm{j}2\pi f}\bigl(\mathrm{e}^{\mathrm{j}2\pi f}+1+\mathrm{e}^{-\mathrm{j}2\pi f}\bigr)=\frac13\mathrm{e}^{-\mathrm{j}2\pi f}\bigl[1+2\cos(2\pi f)\bigr]$.

(b) $\cos(2\pi f)=-\frac12$, also $f=\frac13$ (bei $f_\mathrm A=1$ kHz: 333 Hz). Eine Schwingung mit drei Werten je Periode besteht aus drei Zeigern im Abstand $120^\circ$. Ihre Summe ist null, das Filter sieht in jedem Fenster genau eine ganze Periode.
:::
:::

::::formelsammlung
**Fourier-Transformation zeitdiskreter Signale**

$$S_\mathrm a(f)=\sum_{n=-\infty}^{\infty}s(n)\,\mathrm{e}^{-\mathrm{j}2\pi nf},\qquad s(n)=\int_{-1/2}^{1/2}S_\mathrm a(f)\,\mathrm{e}^{\mathrm{j}2\pi nf}\,\mathrm{d} f$$

Normiert auf $T=1$. $S_\mathrm a(f)$ ist periodisch mit der Periode 1 (Abtastrate); eine Periode $|f|\le\frac12$ enthält alles. Die Summe ist eine Fourier-Reihe in $f$ mit den Abtastwerten als Koeffizienten.

**Spektrum der Exponentialfolge**

$$S_\mathrm a(f)=\frac{1}{1-b\,\mathrm{e}^{-\mathrm{j}2\pi f}},\qquad|S_\mathrm a(f)|^2=\frac{1}{1+b^2-2b\cos(2\pi f)}$$

Für $s(n)=\varepsilon(n)\,b^n$ mit $|b|<1$ (geometrische Reihe); zugleich der Frequenzgang $H_\mathrm a(f)$ des rekursiven Systems. Für $b=0{,}6$ ein Tiefpass mit periodischem Frequenzgang.

**Faltungssatz für Folgen**

$$s(n)*h(n)\;\circ\!\!-\!\!\bullet\;S_\mathrm a(f)H_\mathrm a(f)$$

Wie bei Funktionen: Ein LSI-System multipliziert das Spektrum des Eingangs mit seinem Frequenzgang.

**Produkt zweier Folgen**

$$s(n)\cdot h(n)\;\circ\!\!-\!\!\bullet\;\int_{-1/2}^{1/2}S_\mathrm a(\nu)\,H_\mathrm a(f-\nu)\,\mathrm{d}\nu$$

Periodische Faltung der Spektren über eine Periode.

**Gleitender Mittelwert über drei Werte**

$$H_\mathrm a(f)=\frac13\mathrm{e}^{-\mathrm{j}2\pi f}\bigl[1+2\cos(2\pi f)\bigr]$$

Für $h(n)=\frac13\bigl[\delta(n)+\delta(n-1)+\delta(n-2)\bigr]$. Null bei $f=\frac13$: Eine Schwingung mit drei Werten je Periode wird vollständig ausgelöscht.
::::

::::lernkarten
:::karte formel Fourier-Transformation zeitdiskreter Signale
Wie berechnet man das Spektrum $S_\mathrm a(f)$ einer Zahlenfolge $s(n)$, und wie gewinnt man die Folge daraus zurück?
---
$S_\mathrm a(f)=\sum_{n=-\infty}^{\infty}s(n)\,\mathrm{e}^{-\mathrm{j}2\pi nf}$ und $s(n)=\int_{-1/2}^{1/2}S_\mathrm a(f)\,\mathrm{e}^{\mathrm{j}2\pi nf}\,\mathrm{d} f$, normiert auf $T=1$. Die Rücktransformation integriert nur über eine Periode.
--- falsch
$S_\mathrm a(f)=\int_{-\infty}^{\infty}s(n)\,\mathrm{e}^{-\mathrm{j}2\pi nf}\,\mathrm{d} n$ und $s(n)=\sum_fS_\mathrm a(f)\,\mathrm{e}^{\mathrm{j}2\pi nf}$, normiert auf $T=1$. Die Rücktransformation summiert über alle Frequenzen der Folge.
--- falsch
$S_\mathrm a(f)=\sum_{n=-\infty}^{\infty}s(n)\,\mathrm{e}^{-\mathrm{j}2\pi nf}$ und $s(n)=\int_{-\infty}^{\infty}S_\mathrm a(f)\,\mathrm{e}^{\mathrm{j}2\pi nf}\,\mathrm{d} f$, normiert auf $T=1$. Die Rücktransformation integriert über alle Frequenzen.
--- falsch
$S_\mathrm a(f)=\sum_{n=-\infty}^{\infty}s(n)\,\mathrm{e}^{-\mathrm{j}2\pi nf}$ und $s(n)=\int_0^{1/2}S_\mathrm a(f)\,\mathrm{e}^{\mathrm{j}2\pi nf}\,\mathrm{d} f$, normiert auf $T=1$. Die Rücktransformation braucht nur positive Frequenzen bis zur halben Abtastrate.
:::
:::karte zusammenhang Eine Periode genügt
Warum integriert die Rücktransformation der Fourier-Transformation zeitdiskreter Signale nur über ein Intervall der Länge 1?
---
$S_\mathrm a(f)$ ist periodisch mit der Periode 1, der Abtastrate; eine Periode, $|f|\le\frac12$, enthält schon alles. Die Summe ist eine Fourier-Reihe in $f$, und ihre Koeffizienten, die Abtastwerte, gewinnt man durch Integration über eine Periode.
--- falsch
Weil eine Folge nur Frequenzen bis $\frac12$ enthalten kann. Darüber ist $S_\mathrm a(f)$ null, deshalb trägt der Rest der Frequenzachse nichts bei, und das Integral bricht dort ohne Fehler ab.
--- falsch
Weil das Integral über alle Frequenzen nicht konvergiert. Man schneidet es deshalb nach einer Länge 1 ab und nimmt den kleinen Fehler in Kauf, der durch die fehlenden hohen Frequenzen entsteht und bei Folgen meist kaum auffällt.
--- falsch
Weil die Folge selbst die Periode 1 hat. Ein Signal, das sich nach jedem Takt wiederholt, braucht nur ein Frequenzintervall der Länge 1, um vollständig beschrieben zu werden.
:::
:::karte herleitung Spektrum aus den Abtastwerten
Wie entsteht aus dem Fourier-Integral des ideal abgetasteten Signals $s_\mathrm a(t)=\sum_ns(nT)\delta(t-nT)$ die Summe $S_\mathrm a(f)=\sum_{n=-\infty}^{\infty}s(n)\,\mathrm{e}^{-\mathrm{j}2\pi nf}$?
---
Man setzt $s_\mathrm a(t)$ in das Fourier-Integral ein und vertauscht Summe und Integral, weil das Integral linear ist; es bleibt ein Integral je Impuls.
---
Jedes dieser Integrale liefert den Abtastwert $s(nT)$ mal dem Wert der Schwingung zur Zeit $nT$, weil die Siebeigenschaft den Wert des Integranden an der Stelle des Impulses herausgreift.
---
Übrig bleibt eine Summe statt eines Integrals, weil von jedem Impuls nur ein einzelner Wert beiträgt.
---
Normiert auf $T=1$ wird daraus $\sum_{n=-\infty}^{\infty}s(n)\,\mathrm{e}^{-\mathrm{j}2\pi nf}$, weil die Abtastzeiten $nT$ dann einfach die ganzen Zahlen $n$ sind und die Frequenz auf die Abtastrate bezogen ist.
:::
:::karte formel Spektrum der Exponentialfolge
Welches Spektrum und welches Betragsquadrat hat die Folge $s(n)=\varepsilon(n)\,b^n$ mit $|b|<1$?
---
Mit der geometrischen Reihe: $S_\mathrm a(f)=\frac{1}{1-b\,\mathrm{e}^{-\mathrm{j}2\pi f}}$ und $|S_\mathrm a(f)|^2=\frac{1}{1+b^2-2b\cos(2\pi f)}$. Das ist zugleich der Frequenzgang $H_\mathrm a(f)$ des rekursiven Systems $g(n)=s(n)+b\,g(n-1)$.
--- falsch
Mit der geometrischen Reihe: $S_\mathrm a(f)=\frac{1}{1+b\,\mathrm{e}^{-\mathrm{j}2\pi f}}$ und $|S_\mathrm a(f)|^2=\frac{1}{1+b^2+2b\cos(2\pi f)}$. Das ist zugleich die Impulsantwort des rekursiven Systems $g(n)=s(n)+b\,g(n-1)$.
--- falsch
Mit der geometrischen Reihe: $S_\mathrm a(f)=\frac{1}{1-b\,\mathrm{e}^{-\mathrm{j}2\pi f}}$, aber nur für $|f|\le\frac12$, außerhalb ist es null. Das Betragsquadrat ist $|S_\mathrm a(f)|^2=\frac{1}{(1-b)^2}$, für jede Frequenz gleich.
--- falsch
Mit der geometrischen Reihe: $S_\mathrm a(f)=\frac{b}{1-\mathrm{e}^{-\mathrm{j}2\pi f}}$ und $|S_\mathrm a(f)|^2=\frac{b^2}{2-2\cos(2\pi f)}$. Es ist bei $f=0$ unendlich groß, weil die Folge unendlich lang ist und nie ganz verschwindet.
:::
:::karte zusammenhang Periodischer Tiefpass
Warum ist das rekursive System mit $b=0{,}6$ ein Tiefpass, der bei $f=1$ trotzdem wieder so stark verstärkt wie bei $f=0$?
---
Sein Frequenzgang hat bei $f=0$ den Betrag 2,5 und fällt bis $f=0{,}5$ auf 0,625, deshalb ist es ein Tiefpass. Der Frequenzgang einer Folge ist aber periodisch mit der Abtastrate, bei $f=1$ gilt also derselbe Wert wie bei $f=0$.
--- falsch
Weil der Frequenzgang bei $f=1$ eine zweite Resonanz hat. Die Rückkopplung schwingt dort mit, und diese Resonanz liegt zufällig genau so hoch wie der Wert bei $f=0$, nämlich bei 2,5.
--- falsch
Es verstärkt bei $f=1$ nicht wieder, der Betrag fällt über $f=0{,}5$ hinaus weiter ab. Die Kurve sieht nur periodisch aus, weil man sie zur Darstellung an der halben Abtastrate spiegelt und dabei eine Kopie mitzeichnet.
--- falsch
Weil der Kosinus im Nenner bei $f=1$ wieder 1 ist. Periodisch ist der Frequenzgang aber nur für $b=0{,}6$; mit jedem anderen $b$ würde er über $f=0{,}5$ hinaus weiter abfallen.
:::
:::karte formel Faltungssatz für Folgen
Was wird aus der Faltung $s(n)*h(n)$ zweier Folgen im Frequenzbereich, und was bedeutet das für ein LSI-System?
---
Das Produkt der Spektren: $s(n)*h(n)\;\circ\!\!-\!\!\bullet\;S_\mathrm a(f)H_\mathrm a(f)$, wie bei Funktionen. Ein LSI-System multipliziert also das Spektrum des Eingangs mit seinem Frequenzgang $H_\mathrm a(f)$.
--- falsch
Die Summe der Spektren: $s(n)*h(n)\;\circ\!\!-\!\!\bullet\;S_\mathrm a(f)+H_\mathrm a(f)$. Ein LSI-System addiert also seinen Frequenzgang $H_\mathrm a(f)$ zum Spektrum des Eingangs.
--- falsch
Die periodische Faltung der Spektren über eine Periode. Ein LSI-System verschmiert also das Spektrum des Eingangs mit seinem Frequenzgang, statt es Frequenz für Frequenz zu gewichten.
--- falsch
Das Produkt der Spektren, aber nur für endlich lange Folgen. Bei unendlich langen Folgen wie $\varepsilon(n)\,b^n$ gilt der Satz nicht, weil ihre Spektren periodisch sind und sich nicht multiplizieren lassen.
:::
:::karte begriff periodische Faltung
Was ist die periodische Faltung zweier Spektren, und wo tritt sie bei Folgen auf?
---
Die Faltung über nur eine Periode, $\int_{-1/2}^{1/2}S_\mathrm a(\nu)\,H_\mathrm a(f-\nu)\,\mathrm{d}\nu$, für periodische Spektren. Sie ist das Spektrum des Produkts $s(n)\cdot h(n)$ zweier Folgen.
--- falsch
Die gewöhnliche Faltung über die ganze Frequenzachse, $\int_{-\infty}^{\infty}S_\mathrm a(\nu)\,H_\mathrm a(f-\nu)\,\mathrm{d}\nu$. Sie ist das Spektrum des Produkts $s(n)\cdot h(n)$ zweier Folgen.
--- falsch
Die Faltung über nur eine Periode, $\int_{-1/2}^{1/2}S_\mathrm a(\nu)\,H_\mathrm a(f-\nu)\,\mathrm{d}\nu$. Sie ist das Spektrum der Faltung $s(n)*h(n)$ zweier Folgen, also des Ausgangs eines LSI-Systems.
--- falsch
Die wiederholte Faltung eines Spektrums mit sich selbst, bis das Ergebnis periodisch wird. Sie ist das Spektrum einer Folge, die mehrmals hintereinander durch dasselbe System läuft.
:::
:::karte zusammenhang Gleitender Mittelwert
Welche Schwingung löscht der gleitende Mittelwert $h(n)=\frac13\bigl[\delta(n)+\delta(n-1)+\delta(n-2)\bigr]$ vollständig aus, und warum?
---
Die mit $f=\frac13$, also mit drei Werten je Periode; dort ist $H_\mathrm a(f)=\frac13\mathrm{e}^{-\mathrm{j}2\pi f}\bigl[1+2\cos(2\pi f)\bigr]$ null. Drei Zeiger im Abstand $120^\circ$ ergeben die Summe null: Das Filter sieht in jedem Fenster genau eine ganze Periode.
--- falsch
Die mit $f=\frac12$, also mit zwei Werten je Periode. Bei ihr wechseln die Werte das Vorzeichen, und drei aufeinanderfolgende Werte heben sich in jedem Fenster genau gegeneinander auf, sodass am Ausgang nichts übrig bleibt.
--- falsch
Die mit $f=0$, also den Gleichanteil. Ein Mittelwertfilter entfernt den Mittelwert des Signals, weil es von jedem Wert den Durchschnitt seiner beiden Nachbarn abzieht.
--- falsch
Die mit $f=3$, also mit drei Perioden zwischen zwei Werten. Das Filter mittelt über drei Werte, und eine Schwingung, die zwischen zwei Werten dreimal umläuft, mittelt sich dabei heraus.
:::
::::

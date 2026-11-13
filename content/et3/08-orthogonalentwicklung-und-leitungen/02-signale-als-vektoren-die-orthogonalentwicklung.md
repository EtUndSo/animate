---
title: Stufe 1: Signale als Vektoren, die Orthogonalentwicklung
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Orthogonalentwicklung und Leitungen
adresse: elektrotechnik/3-semester/signale-und-systeme/orthogonalentwicklung-und-leitungen
knoten: Kapitel 8: Orthogonalentwicklung und Leitungen
order: 3280200
summary: Die Fourier-Reihe zerlegt ein Signal nach Schwingungen.
tags: orthogonal, orthonormal, verallgemeinerte Parseval-Theorem
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Die Fourier-Reihe zerlegt ein Signal nach Schwingungen. Dasselbe geht mit jedem System orthogonaler Funktionen. Diese Stufe zeigt, wie man die Koeffizienten findet und warum sie die beste Näherung liefern.
:::

**Die Idee.** Ein Vektor im Raum hat die Komponenten $b_i=\vec f\cdot\vec e_i$ bezüglich senkrechter Einheitsvektoren $\vec e_i$. Für Signale auf einem Intervall $[0,T]$ spielt das Integral $\int_0^Tf(t)g(t)\mathrm{d} t$ die Rolle des Skalarprodukts. Zwei Signale heißen __orthogonal__, wenn es null ist ([Kapitel 6](/wissen/elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen/korrelationsfunktionen.html)). Ein System von $M$ Funktionen $s_i(t)$ heißt __orthonormal__, wenn

<span class="anker" id="gl-1-1"></span>
$$\int_0^Ts_i(t)\,s_j(t)\,\mathrm{d} t=\begin{cases}1&i=j\\0&i\neq j\end{cases}. \tag{1.1}$$

Man nähert ein Energiesignal $f(t)$ durch $\sum_{i=0}^{M-1}b_is_i(t)$, und es bleibt ein Rest $r(t)=f(t)-\sum b_is_i(t)$.

:::satz Satz 1.1 (Orthogonalentwicklung)
<span class="anker" id="satz-1-1"></span>

Die Energie des Rests $E_r=\int_0^Tr^2\mathrm{d} t$ ist am kleinsten für

<span class="anker" id="gl-1-2"></span>
$$b_i=\int_0^Tf(t)\,s_i(t)\,\mathrm{d} t. \tag{1.2}$$

Dann gilt $E_r=E_f-\sum_ib_i^2$. Wird $E_r\to0$ mit wachsendem $M$ (vollständiges System), gilt das __verallgemeinerte Parseval-Theorem__ $E_f=\sum_ib_i^2$.
:::

:::herleitung Koeffizienten und Restenergie
$E_r=\int_0^T\bigl(f-\sum_ib_is_i\bigr)^2\mathrm{d} t$. Ableiten nach $b_j$ und null setzen:

$$\frac{\partial E_r}{\partial b_j}=-2\int_0^T\Bigl(f-\sum_ib_is_i\Bigr)s_j\,\mathrm{d} t=0\quad\Longrightarrow\quad\int_0^Tfs_j\,\mathrm{d} t=\sum_ib_i\int_0^Ts_is_j\,\mathrm{d} t=b_j.$$

Die Orthonormalität lässt aus der Summe nur $i=j$ übrig. Setzt man diese $b_i$ ein und multipliziert aus, heben sich die gemischten Glieder wieder wegen der Orthonormalität weg: $E_r=E_f-2\sum b_i^2+\sum b_i^2=E_f-\sum b_i^2$.
:::

⁠**So liest man das:** Jeder Koeffizient wird für sich bestimmt, unabhängig von den anderen. Nimmt man eine Basisfunktion hinzu, ändern sich die bisherigen Koeffizienten nicht. Das ist der Vorteil orthogonaler Systeme, genau wie bei der Fourier-Reihe ([Kapitel 3](/wissen/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)). $b_i$ ist die Kreuzkorrelation $\varphi^E_{fs_i}(0)$. Deshalb kann man die Koeffizienten mit einer Bank von Korrelationsfiltern $h_i(t)=s_i(T-t)$ messen, deren Ausgänge man bei $t=T$ abtastet ([Kapitel 7](/wissen/elektrotechnik/3-semester/signale-und-systeme/zufallssignale/zufallssignale.html)).

::::beispiel
$f(t)=t^2$ auf $[0,1]$, $E_f=\frac15$. Mit $s_0=1$ und $s_1=\sqrt3(2t-1)$:

$$b_0=\int_0^1t^2\mathrm{d} t=\tfrac13,\qquad b_1=\sqrt3\int_0^1t^2(2t-1)\mathrm{d} t=\tfrac{\sqrt3}{6}=0{,}289,\qquad\sum b_i^2=\tfrac19+\tfrac1{12}=\tfrac{7}{36}.$$

Die Näherung ist $\frac13+\frac{\sqrt3}{6}\sqrt3(2t-1)=t-\frac16$, die beste Gerade im Sinne der Energie. Die Restenergie ist $\frac15-\frac7{36}=\frac{1}{180}=0{,}0056$, also 2,8 % von $E_f$. Mit $s_2=\sqrt5(6t^2-6t+1)$ kommt $b_2=\frac{\sqrt5}{30}=0{,}075$ dazu, und der Rest wird null, weil $t^2$ selbst ein Polynom zweiten Grades ist.
::::

:::aufgabe Aufgabe 1 ★ Orthonormal prüfen
<span class="anker" id="aufg-1"></span>

Zeige, dass $s_0=1$ und $s_1=\sqrt3(2t-1)$ auf $[0,1]$ orthonormal sind. Warum braucht $s_1$ den Faktor $\sqrt3$?

:::loesung
$\int_0^11\cdot\sqrt3(2t-1)\mathrm{d} t=\sqrt3\,[t^2-t]_0^1=0$: orthogonal. $\int_0^11^2\mathrm{d} t=1$. $\int_0^13(2t-1)^2\mathrm{d} t=3\cdot\bigl[\frac{(2t-1)^3}{6}\bigr]_0^1=3\cdot\frac{1+1}{6}=1$. Ohne den Faktor wäre die Energie von $2t-1$ nur $\frac13$. Der Faktor $\sqrt3$ normiert sie auf 1, sonst wäre $b_1=\int fs_1\mathrm{d} t$ nicht der richtige Koeffizient.
:::
:::

:::aufgabe Aufgabe 2 ★★ Beste Näherung
<span class="anker" id="aufg-2"></span>

<ol class="al">

<li>

Rechne $b_1$ für $f(t)=t^2$ nach und bestätige die Näherung $t-\frac16$.

</li>

<li>

Prüfe $E_r=\frac{1}{180}$, indem du $\int_0^1\bigl(t^2-t+\frac16\bigr)^2\mathrm{d} t$ direkt berechnest.

</li>

<li>

Bestimme die Koeffizienten von $f(t)=\sqrt2\cos(2\pi t)$ bezüglich $s_0$ und $s_1$. Was bedeutet das Ergebnis?

</li>

</ol>

:::loesung
(a) $\int_0^1t^2(2t-1)\mathrm{d} t=\frac24-\frac13=\frac16$, also $b_1=\frac{\sqrt3}{6}$. Näherung: $\frac13+\frac{\sqrt3}{6}\cdot\sqrt3(2t-1)=\frac13+t-\frac12=t-\frac16$.

(b) $\int_0^1\bigl(t^2-t+\tfrac16\bigr)^2\mathrm{d} t=\int_0^1\bigl(t^4-2t^3+\tfrac43t^2-\tfrac13t+\tfrac1{36}\bigr)\mathrm{d} t=\tfrac15-\tfrac12+\tfrac49-\tfrac16+\tfrac1{36}=\tfrac{1}{180}$.

(c) $b_0=\sqrt2\int_0^1\cos(2\pi t)\mathrm{d} t=0$ und $b_1=\sqrt6\int_0^1(2t-1)\cos(2\pi t)\mathrm{d} t=0$ (der Kosinus ist symmetrisch um $t=\frac12$, $2t-1$ antisymmetrisch). Beide Koeffizienten sind null: Die Funktion ist zu beiden Basisfunktionen orthogonal, die Näherung ist null, und der ganze Signalinhalt bleibt im Rest. Eine Basis taugt nur für Signale, die ihren Funktionen ähneln.
:::
:::

::::formelsammlung
**Orthonormales System**

$$\int_0^Ts_i(t)\,s_j(t)\,\mathrm{d} t=\begin{cases}1&i=j\\0&i\neq j\end{cases}$$

Für $M$ Funktionen $s_i(t)$ auf $[0,T]$: Je zwei verschiedene sind orthogonal, jede hat die Energie 1. Das Integral $\int_0^Tf(t)g(t)\mathrm{d} t$ spielt die Rolle des Skalarprodukts; ist es null, heißen zwei Signale orthogonal.

**Beste Koeffizienten**

$$b_i=\int_0^Tf(t)\,s_i(t)\,\mathrm{d} t,\qquad b_i=\varphi^E_{fs_i}(0)$$

Für ein orthonormales System: Mit diesen $b_i$ ist die Energie des Rests $r(t)=f(t)-\sum b_is_i(t)$, also $E_r=\int_0^Tr^2\mathrm{d} t$, am kleinsten. Jeder Koeffizient wird für sich bestimmt; eine neue Basisfunktion ändert die bisherigen nicht. $b_i$ ist die Kreuzkorrelation bei null und lässt sich mit Korrelationsfiltern $h_i(t)=s_i(T-t)$ messen, deren Ausgänge man bei $t=T$ abtastet.

**Restenergie**

$$E_r=E_f-\sum_ib_i^2$$

Mit den besten Koeffizienten; $E_f$ ist die Energie des Signals $f(t)$.

**Verallgemeinertes Parseval-Theorem**

$$E_f=\sum_ib_i^2$$

Für ein vollständiges System, bei dem $E_r\to0$ mit wachsender Zahl $M$ der Basisfunktionen.
::::

::::lernkarten
:::karte zusammenhang Skalarprodukt und orthogonal
Warum kann man Signale auf einem Intervall $[0,T]$ wie Vektoren behandeln, und was bedeutet dann orthogonal?
---
Weil das Integral $\int_0^Tf(t)g(t)\mathrm{d} t$ dieselbe Rolle spielt wie das Skalarprodukt zweier Vektoren. Ist es null, heißen die Signale orthogonal, so wie zwei senkrechte Vektoren.
--- falsch
Weil jedes Signal auf $[0,T]$ nur endlich viele Werte annimmt, die man als Komponenten eines Vektors aufschreibt. Orthogonal heißen zwei Signale, wenn sie nie gleichzeitig von null verschieden sind.
--- falsch
Weil das Integral $\int_0^Tf(t)g(t)\mathrm{d} t$ die Länge eines Signals angibt. Ist es eins, heißen die Signale orthogonal, so wie zwei Einheitsvektoren, die senkrecht aufeinander stehen.
--- falsch
Weil man die Werte eines Signals zu jedem Zeitpunkt als Winkel deuten kann. Orthogonal heißen zwei Signale, wenn sie überall um eine Viertelperiode gegeneinander verschoben sind.
:::
:::karte begriff orthonormal
Wann heißt ein System von $M$ Funktionen $s_i(t)$ auf dem Intervall $[0,T]$ orthonormal?
---
Wenn je zwei verschiedene Funktionen orthogonal sind und jede die Energie 1 hat: $\int_0^Ts_i(t)\,s_j(t)\,\mathrm{d} t$ ist 1 für $i=j$ und 0 für $i\neq j$.
--- falsch
Wenn je zwei verschiedene Funktionen orthogonal sind; wie groß die Energie jeder einzelnen Funktion ist, spielt dabei keine Rolle, solange sie nicht null ist.
--- falsch
Wenn jede Funktion die Energie 1 hat, $\int_0^Ts_i^2(t)\,\mathrm{d} t=1$. Ob zwei verschiedene Funktionen zueinander orthogonal sind, spielt für diese Bezeichnung keine Rolle.
--- falsch
Wenn alle Funktionen zusammen die Energie 1 haben, also $\sum_i\int_0^Ts_i^2(t)\,\mathrm{d} t=1$, und je zwei verschiedene Funktionen zueinander orthogonal sind.
:::
:::karte formel Koeffizienten der Orthogonalentwicklung
Wie berechnet man die Koeffizienten $b_i$, mit denen $\sum_{i=0}^{M-1}b_is_i(t)$ ein Energiesignal $f(t)$ nach einem orthonormalen System am besten nähert?
---
$b_i=\int_0^Tf(t)\,s_i(t)\,\mathrm{d} t$: Jeder Koeffizient ist das Skalarprodukt von $f$ mit seiner Basisfunktion. Diese Wahl macht die Energie des Rests $E_r=\int_0^Tr^2\mathrm{d} t$ am kleinsten.
--- falsch
$b_i=\int_0^Tf^2(t)\,s_i(t)\,\mathrm{d} t$: Jeder Koeffizient gewichtet die Energie von $f$ mit seiner Basisfunktion. Diese Wahl macht die Energie des Rests $E_r=\int_0^Tr^2\mathrm{d} t$ am kleinsten.
--- falsch
$b_i=f(t_i)/s_i(t_i)$ an einem passend gewählten Zeitpunkt $t_i$: Jeder Koeffizient wird so gewählt, dass die Näherung an diesem Punkt genau mit dem Signal $f$ übereinstimmt.
--- falsch
Man löst ein Gleichungssystem für alle $b_i$ gemeinsam, weil jeder Koeffizient von allen anderen abhängt. Erst die gemeinsame Lösung macht die Energie des Rests am kleinsten.
:::
:::karte formel Restenergie
Wie groß ist die Energie des Rests $r(t)=f(t)-\sum b_is_i(t)$, wenn man die besten Koeffizienten verwendet?
---
$E_r=E_f-\sum_ib_i^2$: Von der Energie des Signals wird für jede Basisfunktion das Quadrat ihres Koeffizienten abgezogen; jede neue Basisfunktion verringert den Rest um $b_i^2$.
--- falsch
$E_r=E_f-\sum_ib_i$: Von der Energie des Signals wird jeder Koeffizient selbst abgezogen. Deshalb wählt man möglichst viele Basisfunktionen mit großen positiven Koeffizienten.
--- falsch
$E_r=E_f-\bigl(\sum_ib_i\bigr)^2$: Die Restenergie sinkt um das Quadrat der Summe aller Koeffizienten, weil die gemischten Glieder $b_ib_j$ beim Ausmultiplizieren erhalten bleiben.
--- falsch
$E_r=E_f-\sum_ib_i^2$, aber nur, wenn alle $b_i$ gleich groß sind; sonst hängt die Restenergie zusätzlich von den Produkten $b_ib_j$ verschiedener Koeffizienten ab.
:::
:::karte begriff verallgemeinertes Parseval-Theorem
Was besagt das verallgemeinerte Parseval-Theorem für die Orthogonalentwicklung eines Signals $f(t)$?
---
Die Energie des Signals ist gleich der Summe der Koeffizientenquadrate, $E_f=\sum_ib_i^2$. Es gilt für ein vollständiges System, bei dem die Restenergie $E_r$ mit wachsendem $M$ gegen null geht.
--- falsch
Die Energie des Signals ist gleich der Summe der Koeffizientenquadrate, $E_f=\sum_ib_i^2$. Es gilt für jedes orthonormale System, auch wenn es nur aus wenigen Basisfunktionen besteht.
--- falsch
Die Energie des Signals ist gleich dem Quadrat der Summe der Koeffizienten, $E_f=\bigl(\sum_ib_i\bigr)^2$. Es gilt für ein vollständiges System, bei dem die Restenergie gegen null geht.
--- falsch
Die Energie des Signals ist gleich der Summe der Beträge der Koeffizienten, $E_f=\sum_i|b_i|$, weil jede Basisfunktion die Energie 1 hat und nur mit ihrem Koeffizienten gewichtet wird.
:::
:::karte herleitung Koeffizienten und Restenergie
Wie folgt aus der Restenergie $E_r=\int_0^T\bigl(f-\sum_ib_is_i\bigr)^2\mathrm{d} t$, dass $b_i=\int_0^Tf(t)\,s_i(t)\,\mathrm{d} t$ die besten Koeffizienten sind und $E_r=E_f-\sum b_i^2$ gilt?
---
Man leitet $E_r$ nach $b_j$ ab und setzt null, weil die Restenergie im Minimum in Richtung keines Koeffizienten mehr abnimmt: $\frac{\partial E_r}{\partial b_j}=-2\int_0^T\Bigl(f-\sum_ib_is_i\Bigr)s_j\,\mathrm{d} t=0$.
---
Daraus folgt $\int_0^Tfs_j\,\mathrm{d} t=\sum_ib_i\int_0^Ts_is_j\,\mathrm{d} t$, weil man das Integral über die Summe gliedweise nehmen darf.
---
Von der Summe bleibt nur das Glied $i=j$ übrig, weil die Orthonormalität $\int_0^Ts_is_j\,\mathrm{d} t$ für $i\neq j$ zu null und für $i=j$ zu eins macht; also ist $b_j=\int_0^Tfs_j\,\mathrm{d} t$.
---
Setzt man diese $b_i$ ein und multipliziert aus, wird $E_r=E_f-2\sum b_i^2+\sum b_i^2=E_f-\sum b_i^2$, weil sich die gemischten Glieder mit $i\neq j$ wieder wegen der Orthonormalität wegheben.
:::
:::karte zusammenhang bisherige Koeffizienten
Was passiert mit den schon berechneten Koeffizienten einer Orthogonalentwicklung, wenn man eine weitere orthonormale Basisfunktion hinzunimmt, und warum?
---
Sie ändern sich nicht. Jeder Koeffizient $b_i=\int_0^Tf(t)\,s_i(t)\,\mathrm{d} t$ hängt nur vom Signal und von seiner eigenen Basisfunktion ab, weil die Orthonormalität alle anderen Glieder entfernt.
--- falsch
Sie müssen alle neu berechnet werden, weil die neue Basisfunktion einen Teil des Signals übernimmt, den bisher die anderen Funktionen mit dargestellt haben.
--- falsch
Sie werden alle um denselben Faktor kleiner, weil sich die Energie des Signals nun auf mehr Basisfunktionen verteilt und die Summe der Quadrate gleich bleiben muss.
--- falsch
Sie ändern sich nur, wenn die neue Basisfunktion eine größere Energie hat als die bisherigen, weil sie dann den größten Teil des Signals an sich zieht und die anderen verdrängt.
:::
:::karte zusammenhang Bank von Korrelationsfiltern
Wie kann man die Koeffizienten $b_i$ einer Orthogonalentwicklung mit Filtern messen, und warum funktioniert das?
---
Mit einer Bank von Korrelationsfiltern $h_i(t)=s_i(T-t)$, deren Ausgänge man bei $t=T$ abtastet. Das funktioniert, weil $b_i$ die Kreuzkorrelation $\varphi^E_{fs_i}(0)$ ist, die ein solches Filter bei $t=T$ liefert.
--- falsch
Mit einer Bank von Bandpässen, deren Mittenfrequenzen bei den Frequenzen der Basisfunktionen liegen. Das funktioniert, weil jede Basisfunktion eine Sinusschwingung mit einer eigenen Frequenz ist.
--- falsch
Mit einer Bank von Filtern $h_i(t)=s_i(t)$, deren Ausgänge man bei $t=0$ abtastet. Das funktioniert, weil jedes dieser Filter im ersten Augenblick die Energie seiner Basisfunktion $s_i$ misst.
--- falsch
Mit einer Bank von Korrelationsfiltern $h_i(t)=s_i(T-t)$, deren Ausgänge man über die ganze Zeit mittelt. Das funktioniert, weil der zeitliche Mittelwert jedes Ausgangs die Energie von $f$ ist.
:::
:::karte zusammenhang Normierung der Basisfunktion
Warum braucht die Basisfunktion $s_1=\sqrt3(2t-1)$ auf dem Intervall $[0,1]$ den Faktor $\sqrt3$?
---
Weil $2t-1$ auf $[0,1]$ nur die Energie $\frac13$ hat. Der Faktor $\sqrt3$ normiert sie auf 1; nur dann ist $b_1=\int fs_1\mathrm{d} t$ der richtige Koeffizient.
--- falsch
Weil $2t-1$ ohne den Faktor nicht orthogonal zu $s_0=1$ wäre; erst durch $\sqrt3$ wird das Integral des Produkts mit $s_0$ über $[0,1]$ zu null.
--- falsch
Weil der Mittelwert von $2t-1$ auf $[0,1]$ ohne den Faktor nicht null wäre; erst der Faktor $\sqrt3$ verschiebt die Gerade so, dass sie symmetrisch um null liegt.
--- falsch
Weil die Steigung jeder Basisfunktion der Wurzel aus einer ungeraden Zahl entsprechen muss; deshalb hat $s_1$ den Faktor $\sqrt3$ und $s_2$ den Faktor $\sqrt5$.
:::
:::karte zusammenhang Polynom zweiten Grades
Warum wird die Restenergie bei der Entwicklung von $f(t)=t^2$ auf $[0,1]$ null, sobald man $s_2=\sqrt5(6t^2-6t+1)$ zu $s_0$ und $s_1$ hinzunimmt?
---
Weil $t^2$ selbst ein Polynom zweiten Grades ist und sich deshalb aus $s_0$, $s_1$ und $s_2$ genau zusammensetzen lässt; mit $b_2=\frac{\sqrt5}{30}$ bleibt kein Rest.
--- falsch
Weil $s_2$ die größte Energie der drei Basisfunktionen hat und deshalb den ganzen bisherigen Rest aufnimmt, gleich welches Signal man auf $[0,1]$ entwickelt.
--- falsch
Weil drei Basisfunktionen für jedes Signal auf $[0,1]$ ausreichen: Jede Funktion lässt sich aus $s_0$, $s_1$ und $s_2$ ohne Rest zusammensetzen.
--- falsch
Weil durch $s_2$ die Koeffizienten $b_0$ und $b_1$ neu berechnet werden und erst diese neuen Werte zusammen mit $b_2$ genau die Funktion $t^2$ ergeben.
:::
:::karte zusammenhang Wahl der Basis
Was ergibt die Entwicklung von $f(t)=\sqrt2\cos(2\pi t)$ auf $[0,1]$ nach $s_0=1$ und $s_1=\sqrt3(2t-1)$, und was folgt daraus für die Wahl der Basis?
---
Beide Koeffizienten sind null, weil die Funktion zu beiden Basisfunktionen orthogonal ist. Alles bleibt im Rest: Eine Basis taugt nur für Signale, die ihren Funktionen ähneln.
--- falsch
Beide Koeffizienten sind null, weil der Kosinus auf $[0,1]$ den Mittelwert null hat. Die Näherung ist trotzdem gut, denn wenn alle Koeffizienten verschwinden, ist auch die Restenergie null.
--- falsch
Es ergeben sich $b_0=\sqrt2$ und $b_1=0$, weil der Kosinus bei $t=0$ den Wert $\sqrt2$ hat. Die Näherung ist eine Konstante, die den Anfangswert des Signals genau trifft.
--- falsch
Beide Koeffizienten sind gleich groß, weil der Kosinus symmetrisch um $t=\frac12$ liegt. Die Näherung ist eine Gerade, die das Signal im Mittel über das ganze Intervall gut beschreibt.
:::
::::

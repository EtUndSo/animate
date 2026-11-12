---
title: Stufe 4: Das Faltungsintegral
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / LTI-Systeme und Faltung
adresse: elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung
knoten: Kapitel 1: LTI-Systeme und Faltung
order: 3210500
summary: Mit Linearität und Zeitinvarianz lässt sich die Antwort auf jedes Signal aus der Antwort auf einen einzigen kurzen Impuls berechnen.
tags: Dirac-Impuls, Impulsantwort
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Mit Linearität und Zeitinvarianz lässt sich die Antwort auf *jedes* Signal aus der Antwort auf einen einzigen kurzen Impuls berechnen. Das Ergebnis ist das Faltungsintegral.
:::

**Die Idee in vier Schritten.**

<ol>

<li>

⁠**Zerlegen.** Man nähert das Eingangssignal durch eine Treppe aus schmalen Rechtecken der Breite $T_0$. Als Baustein dient ein Rechteck $s_0(t)$ der Dauer $T_0$ und der Höhe $1/T_0$, also der Fläche 1. Die Stufe bei $nT_0$ ist dieser Baustein, verschoben um $nT_0$ und gewichtet mit $s(nT_0)\,T_0$, der Fläche des Streifens:

$$s(t)\approx s_a(t)=\sum_{n=-\infty}^{\infty}s(nT_0)\,s_0(t-nT_0)\,T_0.$$

</li>

<li>

⁠**Ein Baustein durch das System.** Auf $s_0$ antwortet das System mit $g_0(t)$. Das muss man einmal kennen.

</li>

<li>

⁠**Zusammensetzen.** Zeitinvarianz: Der verschobene Baustein erzeugt die verschobene Antwort. Linearität: Gewichte und Summe gehen durch. Also

$$g_a(t)=\sum_{n=-\infty}^{\infty}s(nT_0)\,g_0(t-nT_0)\,T_0\approx g(t).$$

</li>

<li>

⁠**Grenzübergang $T_0\to0$.** Die Treppe wird zum Signal. Das Rechteck der Fläche 1 wird zum __Dirac-Impuls__ $\delta(t)$, einem unendlich kurzen Stoß der Fläche 1. Seine Antwort heißt __Impulsantwort__ $h(t)$. Aus $nT_0$ wird die stetige Variable $\tau$, aus $T_0$ das Differential $\mathrm{d}\tau$, aus den Summen Integrale.

</li>

</ol>

:::abbildung et3/k1treppe 5
Oben: Ein Dreieckimpuls $s(t)=\Lambda(t-1)$ und seine Treppennäherung mit $T_0=0{,}5$ s. Unten: die exakte Antwort des RC-Glieds und die Summe der verschobenen Rechteckantworten. Die größte Abweichung sinkt von 0,17 ($T_0=0{,}5$ s) über 0,08 ($0{,}25$ s) auf 0,03 ($0{,}1$ s).
:::

:::satz Satz 4.1 (Faltungsintegral)
<span class="anker" id="satz-4-1"></span>

Für jedes Signal $s(t)$ gilt

<span class="anker" id="gl-4-1"></span>
$$s(t)=\int_{-\infty}^{\infty}s(\tau)\,\delta(t-\tau)\,\mathrm{d}\tau, \tag{4.1}$$

und ein LTI-System mit der Impulsantwort $h(t)$ antwortet darauf mit

<span class="anker" id="gl-4-2"></span>
$$g(t)=\int_{-\infty}^{\infty}s(\tau)\,h(t-\tau)\,\mathrm{d}\tau. \tag{4.2}$$
:::

⁠**So liest man das:** $\tau$ ist der Zeitpunkt eines Eingangsstoßes, $s(\tau)\,\mathrm{d}\tau$ sein Gewicht (die Fläche des Streifens). $h(t-\tau)$ ist die Antwort des Systems zur Zeit $t$ auf einen Stoß, der zur Zeit $\tau$ kam, also vor $t-\tau$ Sekunden. Der Ausgang sammelt alle Stöße der Vergangenheit, jeden gewichtet damit, wie stark sich das System nach dieser Zeit noch an ihn „erinnert“. Die Gleichung gilt exakt und für jedes LTI-System.

⁠**Kurz gesagt:** Der Ausgang eines LTI-Systems ist die Überlagerung seiner Impulsantworten, verschoben an jeden Zeitpunkt des Eingangs und gewichtet mit dem Eingang dort.

:::frage Warum müssen die Rechteckbausteine die Fläche 1 haben?
Damit die Antwort auf den Baustein beim Grenzübergang eine feste Form behält. Ein Rechteck der festen Höhe 1 hätte für $T_0\to0$ die Fläche null, und seine Antwort würde verschwinden. Mit der Höhe $1/T_0$ bleibt die Fläche 1, und die Antwort strebt gegen $h(t)$. Beim RC-Glied ist die Spitze der Antwort $(1-\mathrm{e}^{-T_0})/T_0$: 0,632 für $T_0=1$ s, 0,787 für 0,5 s, 0,952 für 0,1 s, und für $T_0\to0$ wird sie $1=h(0^+)$. Die Fläche der Antwort bleibt dabei immer 1.
:::

:::frage Gibt es den Stoß $\delta(t)$ in Wirklichkeit? Wie misst man dann $h(t)$?
Einen unendlich kurzen Stoß gibt es nicht. Es genügt aber jeder Impuls, der viel kürzer ist als die Zeitkonstanten des Systems. Dann sieht das System nur seine Fläche, und die Antwort ist praktisch $(\text{Fläche})\cdot h(t)$. Beim RC-Glied mit $RC=1$ s weicht die Spitze der Antwort auf einen 1-ms-Impuls nur um 0,05 % von $h(0^+)$ ab. So misst man Impulsantworten auch: Man klatscht in einem Raum in die Hände und nimmt den Nachhall auf.
:::

:::ltspice Impulsantwort mit einem kurzen Rechteck nähern
⁠**Zeichnen:** das RC-Glied aus Stufe [2](ein-erstes-system-das-rc-glied.html#stufe-2) mit der Quelle `PULSE(0 {1/T0} 0 1n 1n {T0})`: ein Rechteck der Breite $T_0$ und der Höhe $1/T_0$, also der Fläche 1.

⁠**Direktiven:** `.param T0=1`, `.step param T0 list 1 0.5 0.1 1m`, `.tran 0 10 0 1m`, `.meas tran spitze MAX V(out)`, `.meas tran flaeche INTEG V(out)`.

⁠**Was du siehst:** Die Spitzen sind 0,632; 0,787; 0,952 und 0,9995, wie $(1-\mathrm{e}^{-T_0})/T_0$. Beim 1-ms-Impuls ist die Antwort praktisch schon $h(t)=\mathrm{e}^{-t}$. Die Fläche ist in allen vier Läufen 1,000: Ein Impuls, der viel kürzer ist als $RC$, wirkt nur über seine Fläche.
:::

:::aufgabe Aufgabe 4 ★★ Die Treppe genauer
<span class="anker" id="aufg-4"></span>

<ol class="al">

<li>

Berechne die Antwort $g_0(t)$ des RC-Glieds ($RC=1$ s) auf das Rechteck der Höhe $1/T_0$ von $0$ bis $T_0$. Benutze dazu [(2.5)](ein-erstes-system-das-rc-glied.html#gl-2-5) und schreibe das Rechteck als Differenz zweier Sprünge.

</li>

<li>

Zeige, dass $g_0(T_0)=(1-\mathrm{e}^{-T_0})/T_0$ ist und für $T_0\to0$ gegen 1 strebt.

</li>

<li>

Warum ist die Näherung $g_a$ in Abb. [5](#abb-5) zu spät? (Tipp: Wo liegt die Stufe im Vergleich zum Dreieck auf der steigenden und auf der fallenden Flanke?)

</li>

</ol>

:::loesung
(a) Das Rechteck ist $\frac{1}{T_0}[\varepsilon(t)-\varepsilon(t-T_0)]$. Linearität und Zeitinvarianz mit der Sprungantwort [(2.5)](ein-erstes-system-das-rc-glied.html#gl-2-5):

$$g_0(t)=\frac{1}{T_0}\Bigl[\bigl(1-\mathrm{e}^{-t}\bigr)\varepsilon(t)-\bigl(1-\mathrm{e}^{-(t-T_0)}\bigr)\varepsilon(t-T_0)\Bigr].$$

(b) Bei $t=T_0$ ist der zweite Summand null: $g_0(T_0)=(1-\mathrm{e}^{-T_0})/T_0$. Mit $\mathrm{e}^{-T_0}\approx1-T_0+T_0^2/2$ für kleine $T_0$ ist das $\approx1-T_0/2\to1=h(0^+)$. Zahlen: 0,632; 0,787; 0,952 für $T_0=1$; 0,5; 0,1 s.

(c) Jede Stufe hält den Wert $s(nT_0)$ vom *Anfang* des Intervalls bis zu dessen Ende. Auf der steigenden Flanke liegt die Treppe deshalb unter dem Dreieck, auf der fallenden darüber: Sie ist im Mittel um $T_0/2$ verzögert. Der Ausgang erbt diese Verzögerung, auf der abfallenden Seite liegt $g_a$ über $g$ ($g_a(2)=0{,}508$ statt $0{,}400$ für $T_0=0{,}5$ s). Mit kleinerem $T_0$ schrumpft die Verzögerung und mit ihr der Fehler.
:::
:::

::::kurzfassung
Ein LTI-System ist durch seine Antwort auf einen einzigen, unendlich kurzen Stoß vollständig beschrieben. Die Antwort auf jedes andere Signal liefert das Faltungsintegral.

Man nähert den Eingang durch eine Treppe aus schmalen Rechtecken der Breite $T_0$. Baustein ist ein Rechteck $s_0(t)$ der Höhe $1/T_0$, also der Fläche 1; die Stufe bei $nT_0$ trägt das Gewicht $s(nT_0)\,T_0$. Das System antwortet auf $s_0$ mit $g_0(t)$. Die Zeitinvarianz liefert zu jedem verschobenen Baustein die verschobene Antwort, die Linearität überträgt Gewichte und Summe. Für $T_0\to0$ wird das Rechteck der Fläche 1 zum __Dirac-Impuls__ $\delta(t)$, einem unendlich kurzen Stoß der Fläche 1. Die Antwort darauf heißt __Impulsantwort__ $h(t)$. Aus der Summe wird das Integral

$$g(t)=\int_{-\infty}^{\infty}s(\tau)\,h(t-\tau)\,\mathrm{d}\tau .$$

Darin ist $\tau$ der Zeitpunkt eines Eingangsstoßes und $s(\tau)\,\mathrm{d}\tau$ sein Gewicht. $h(t-\tau)$ ist die Antwort zur Zeit $t$ auf einen Stoß, der vor $t-\tau$ Sekunden kam. Der Eingang selbst ist eine Überlagerung solcher Stöße, $s(t)=\int_{-\infty}^{\infty}s(\tau)\,\delta(t-\tau)\,\mathrm{d}\tau$. Die Zerlegung gilt für jedes Signal, das Faltungsintegral exakt für jedes LTI-System.

Anschaulich sammelt der Ausgang alle Stöße der Vergangenheit, jeden gewichtet damit, wie stark sich das System nach dieser Zeit noch an ihn „erinnert“.

Falle: Die Bausteine brauchen die Fläche 1. Ein Rechteck der festen Höhe 1 hätte für $T_0\to0$ die Fläche null, und seine Antwort würde verschwinden. Zum Messen von $h(t)$ genügt ein Impuls, der viel kürzer ist als die Zeitkonstanten des Systems, beim RC-Glied also viel kürzer als $RC$: Das System sieht dann nur seine Fläche.
::::

::::formelsammlung
**Treppennäherung des Eingangs**

$$s(t)\approx s_a(t)=\sum_{n=-\infty}^{\infty}s(nT_0)\,s_0(t-nT_0)\,T_0$$

$s_0(t)$ Rechteck der Dauer $T_0$ und der Höhe $1/T_0$, also der Fläche 1; $s(nT_0)\,T_0$ Fläche des Streifens bei $nT_0$.

**Summe der Bausteinantworten**

$$g_a(t)=\sum_{n=-\infty}^{\infty}s(nT_0)\,g_0(t-nT_0)\,T_0\approx g(t)$$

$g_0(t)$ Antwort des Systems auf $s_0(t)$; folgt aus Zeitinvarianz (verschobener Baustein, verschobene Antwort) und Linearität (Gewichte und Summe).

**Zerlegung in Stöße**

$$s(t)=\int_{-\infty}^{\infty}s(\tau)\,\delta(t-\tau)\,\mathrm{d}\tau$$

Für jedes Signal $s(t)$. Grenzübergang $T_0\to0$: $s_0$ wird zum Dirac-Impuls $\delta(t)$ (unendlich kurzer Stoß der Fläche 1), $nT_0\to\tau$, $T_0\to\mathrm{d}\tau$.

**Faltungsintegral**

$$g(t)=\int_{-\infty}^{\infty}s(\tau)\,h(t-\tau)\,\mathrm{d}\tau$$

Exakt für jedes LTI-System; $h(t)$ Impulsantwort (Antwort auf $\delta(t)$). $\tau$ Zeitpunkt eines Eingangsstoßes, $s(\tau)\,\mathrm{d}\tau$ sein Gewicht, $h(t-\tau)$ Antwort zur Zeit $t$ auf einen Stoß, der vor $t-\tau$ Sekunden kam.
::::

::::lernkarten
:::karte begriff Dirac-Impuls
Was ist der Dirac-Impuls $\delta(t)$, und aus welchen Bausteinen entsteht er beim Grenzübergang?
---
Ein unendlich kurzer Stoß der Fläche 1. Er entsteht aus dem Rechteckbaustein der Dauer $T_0$ und der Höhe $1/T_0$, wenn $T_0\to0$ geht; die Fläche bleibt dabei 1.
--- falsch
Ein unendlich kurzer Stoß der Höhe 1. Er entsteht aus einem Rechteck der Höhe 1, wenn seine Dauer $T_0\to0$ geht; die Fläche spielt dabei keine Rolle.
--- falsch
Ein kurzer Rechteckimpuls von 1 ms Dauer und 1 V Höhe, wie ihn ein Pulsgenerator liefert. Kürzere Impulse lassen sich nicht erzeugen, deshalb nimmt man diesen.
--- falsch
Ein Sprung von 0 auf 1 bei $t=0$. Er entsteht aus dem Rechteckbaustein der Höhe $1/T_0$, wenn seine Dauer $T_0\to\infty$ geht und er so nie mehr endet.
:::
:::karte begriff Impulsantwort
Was ist die Impulsantwort $h(t)$ eines LTI-Systems, und warum ist sie so wichtig?
---
Die Antwort des Systems auf den Dirac-Impuls $\delta(t)$. Mit ihr liefert das Faltungsintegral den Ausgang für jedes Eingangssignal; sie beschreibt das System also vollständig.
--- falsch
Die Antwort des Systems auf den Sprung $\varepsilon(t)$. Mit ihr liefert das Faltungsintegral den Ausgang für jedes Eingangssignal; sie beschreibt das System also vollständig.
--- falsch
Die Antwort des Systems auf den Dirac-Impuls $\delta(t)$. Sie beschreibt nur das Verhalten bei kurzen Eingängen; für lange Signale braucht man zusätzlich die Sprungantwort.
--- falsch
Der Eingangsimpuls, den man braucht, damit das System einen gewünschten Ausgang liefert. Sie hängt deshalb vom Ausgang ab und muss für jeden neu bestimmt werden.
:::
:::karte formel Faltungsintegral
Wie berechnet man den Ausgang $g(t)$ eines LTI-Systems mit der Impulsantwort $h(t)$ aus dem Eingang $s(t)$?
---
$$g(t)=\int_{-\infty}^{\infty}s(\tau)\,h(t-\tau)\,\mathrm{d}\tau$$

$\tau$ ist der Zeitpunkt eines Eingangsstoßes, $s(\tau)\,\mathrm{d}\tau$ sein Gewicht, $h(t-\tau)$ die Antwort zur Zeit $t$ auf einen Stoß, der vor $t-\tau$ Sekunden kam. Die Gleichung gilt exakt für jedes LTI-System.
--- falsch
$$g(t)=s(t)\,h(t)$$

Der Ausgang ist zu jedem Zeitpunkt das Produkt aus Eingang und Impulsantwort zur selben Zeit; ein Integral braucht man nicht, weil das System jeden Zeitpunkt einzeln behandelt. Die Gleichung gilt exakt für jedes LTI-System.
--- falsch
$$g(t)=\int_{-\infty}^{\infty}s(\tau)\,h(\tau-t)\,\mathrm{d}\tau$$

$\tau$ ist der Zeitpunkt eines Eingangsstoßes, $s(\tau)\,\mathrm{d}\tau$ sein Gewicht, $h(\tau-t)$ die Antwort auf einen Stoß, der erst nach $\tau-t$ Sekunden kommt. Die Gleichung gilt exakt für jedes LTI-System.
--- falsch
$$g(t)=\int_{-\infty}^{\infty}s(\tau)\,h(t-\tau)\,\mathrm{d}\tau$$

$\tau$ ist der Zeitpunkt eines Eingangsstoßes, $s(\tau)\,\mathrm{d}\tau$ sein Gewicht. Die Gleichung gilt aber nur näherungsweise, weil die Treppe aus Rechtecken immer eine endliche Breite behält.
:::
:::karte formel Zerlegung in Stöße
Wie lässt sich jedes Signal $s(t)$ als Überlagerung von Dirac-Impulsen schreiben?
---
$$s(t)=\int_{-\infty}^{\infty}s(\tau)\,\delta(t-\tau)\,\mathrm{d}\tau$$

An jeder Stelle $\tau$ steht ein Stoß mit dem Gewicht $s(\tau)\,\mathrm{d}\tau$, der Fläche des Streifens.
--- falsch
$$s(t)=\int_{-\infty}^{\infty}s(\tau)\,\delta(t-\tau)\,\mathrm{d}\tau$$

An jeder Stelle $\tau$ steht ein Stoß mit dem Gewicht $s(\tau)$; das $\mathrm{d}\tau$ gibt nur die Integrationsvariable an.
--- falsch
$$s(t)=\int_{-\infty}^{\infty}\delta(t-\tau)\,\mathrm{d}\tau$$

An jeder Stelle steht ein Stoß der Fläche 1; welches Signal entsteht, legt erst das System fest, durch das es läuft.
--- falsch
$$s(t)=\sum_{n=-\infty}^{\infty}\delta(t-n)$$

An jeder ganzen Zahl $n$ steht ein Stoß der Fläche 1; die Höhe des Signals steckt im Abstand der Stöße.
:::
:::karte herleitung Faltungsintegral in vier Schritten
Wie folgt aus Linearität und Zeitinvarianz, dass ein LTI-System auf jedes Signal $s(t)$ mit $g(t)=\int_{-\infty}^{\infty}s(\tau)\,h(t-\tau)\,\mathrm{d}\tau$ antwortet?
---
Zerlegen: $s(t)\approx s_a(t)=\sum_{n=-\infty}^{\infty}s(nT_0)\,s_0(t-nT_0)\,T_0$, weil sich das Signal durch eine Treppe aus Rechteckbausteinen $s_0$ der Fläche 1 nähern lässt, jeder gewichtet mit der Fläche $s(nT_0)\,T_0$ seines Streifens.
---
Ein Baustein durch das System: Auf $s_0$ antwortet es mit $g_0(t)$. Das muss man nur einmal kennen, weil alle Stufen denselben Baustein benutzen.
---
Zusammensetzen: $g_a(t)=\sum_{n=-\infty}^{\infty}s(nT_0)\,g_0(t-nT_0)\,T_0\approx g(t)$, weil der verschobene Baustein die verschobene Antwort erzeugt (Zeitinvarianz) und Gewichte und Summe durchgehen (Linearität).
---
Grenzübergang $T_0\to0$: $s_0$ wird zu $\delta(t)$ und $g_0$ zu $h(t)$, aus $nT_0$ wird $\tau$, aus $T_0$ das Differential $\mathrm{d}\tau$, aus den Summen Integrale. Das Ergebnis gilt exakt, weil die Treppe dabei zum Signal wird.
:::
:::karte zusammenhang Bausteine der Fläche 1
Warum müssen die Rechteckbausteine bei der Herleitung des Faltungsintegrals die Fläche 1 haben?
---
Damit die Antwort auf den Baustein beim Grenzübergang eine feste Form behält. Ein Rechteck der festen Höhe 1 hätte für $T_0\to0$ die Fläche null, seine Antwort verschwände; mit der Höhe $1/T_0$ strebt sie gegen $h(t)$.
--- falsch
Damit die Höhe der Bausteine beim Grenzübergang fest bleibt. Die Fläche 1 ergibt sich bei einem Rechteck der Höhe 1 von selbst, solange die Breite $T_0$ klein ist, und die Antwort strebt dann gegen $h(t)$.
--- falsch
Weil ein LTI-System nur auf Impulse der Fläche 1 linear antwortet. Bei anderen Flächen gilt der Überlagerungssatz nicht mehr, und die Antworten der Bausteine ließen sich nicht einfach addieren.
--- falsch
Damit die Summe aller Bausteine die Fläche 1 hat. Jedes Eingangssignal wird so auf die Fläche 1 normiert, bevor es durch das System geht; sonst hinge die Impulsantwort von der Signalgröße ab.
:::
:::karte zusammenhang Impulsantwort messen
Wie misst man eine Impulsantwort, obwohl es einen unendlich kurzen Stoß in Wirklichkeit nicht gibt?
---
Mit einem Impuls, der viel kürzer ist als die Zeitkonstanten des Systems. Dann sieht das System nur seine Fläche, und die Antwort ist praktisch $(\text{Fläche})\cdot h(t)$. In einem Raum etwa klatscht man in die Hände und nimmt den Nachhall auf.
--- falsch
Mit einem Impuls, der viel länger ist als die Zeitkonstanten des Systems, damit das System sicher eingeschwungen ist. Die Antwort ist dann $h(t)$ selbst. In einem Raum etwa lässt man einen Dauerton laufen und misst den Pegel.
--- falsch
Mit einem möglichst hohen Impuls beliebiger Dauer. Entscheidend ist die Höhe, weil der Dirac-Impuls unendlich hoch ist; die Dauer spielt keine Rolle. In einem Raum etwa nimmt man den lautesten verfügbaren Knall.
--- falsch
Gar nicht direkt: Man misst die Antworten auf viele Sinusschwingungen und liest $h(t)$ an der höchsten Frequenz ab, weil sie dem Stoß am nächsten kommt. Ein Klatschen enthält dafür zu wenige Frequenzen.
:::
:::karte zusammenhang Überlagerung der Impulsantworten
Wie lässt sich der Ausgang eines LTI-Systems in einem Satz durch seine Impulsantwort beschreiben?
---
Er ist die Überlagerung seiner Impulsantworten, verschoben an jeden Zeitpunkt des Eingangs und gewichtet mit dem Eingang dort.
--- falsch
Er ist die Impulsantwort, multipliziert mit dem Mittelwert des Eingangs; die Form des Ausgangs ist deshalb immer die von $h(t)$.
--- falsch
Er ist die Überlagerung der Impulsantworten zu den Zeitpunkten, an denen der Eingang null wird; dazwischen trägt das Signal nichts bei.
--- falsch
Er ist der Eingang, verzögert um die Dauer der Impulsantwort; die Impulsantwort legt nur fest, wie spät der Ausgang erscheint.
:::
:::karte zusammenhang Antwort auf schmalere Bausteine
Wie verändert sich beim RC-Glied die Antwort auf den Rechteckbaustein der Fläche 1, wenn seine Dauer $T_0$ schrumpft?
---
Die Spitze $(1-\mathrm{e}^{-T_0})/T_0$ steigt: 0,632 für $T_0=1$ s, 0,787 für 0,5 s, 0,952 für 0,1 s, und für $T_0\to0$ wird sie $1=h(0^+)$. Die Fläche der Antwort bleibt immer 1.
--- falsch
Die Spitze sinkt gegen null, weil der Kondensator in kürzerer Zeit weniger Ladung aufnimmt: 0,632 für $T_0=1$ s, 0,393 für 0,5 s, 0,095 für 0,1 s. Die Fläche der Antwort sinkt mit.
--- falsch
Die Spitze wächst wie $1/T_0$ über alle Grenzen, weil der Baustein immer höher wird: 1 für $T_0=1$ s, 2 für 0,5 s, 10 für 0,1 s. Die Fläche der Antwort bleibt dabei 1.
--- falsch
Die Spitze bleibt bei 0,632, weil sie nur von $RC$ abhängt und nicht von der Form des Bausteins. Nur die Fläche der Antwort ändert sich mit $T_0$ und strebt für $T_0\to0$ gegen 1.
:::
:::karte zusammenhang Treppennäherung kommt zu spät
Warum kommt die Näherung $g_a$ aus der Treppe etwas zu spät gegenüber dem exakten Ausgang?
---
Jede Stufe hält den Wert $s(nT_0)$ vom Anfang ihres Intervalls bis zu dessen Ende. Die Treppe ist daher im Mittel um $T_0/2$ verzögert, und der Ausgang erbt diese Verzögerung; mit kleinerem $T_0$ schrumpft sie und mit ihr der Fehler.
--- falsch
Weil das System auf jeden Baustein erst nach seiner Zeitkonstante antwortet. Die Verzögerung hängt nur von $RC$ ab und bleibt deshalb auch bei kleinerem $T_0$ gleich groß; man muss sie am Ende von Hand abziehen.
--- falsch
Weil die Bausteine die Fläche 1 statt der Höhe 1 haben. Ihre große Höhe $1/T_0$ bei kleinem $T_0$ verschiebt die Antwort nach rechts; mit Bausteinen der Höhe 1 käme der Ausgang genau rechtzeitig.
--- falsch
Weil die Summe in $g_a$ erst bei $n=0$ beginnt. Die Anteile mit negativem $n$ fehlen, und der Ausgang setzt verspätet ein; mit kleinerem $T_0$ bleibt der Fehler gleich, weil immer dieselben Anteile fehlen.
:::
::::

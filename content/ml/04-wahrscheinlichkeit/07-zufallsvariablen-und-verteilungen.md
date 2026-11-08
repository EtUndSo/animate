---
title: Zufallsvariablen und Verteilungen
pfad: Informatik / Machine Learning / Mathematische Grundlagen / Wahrscheinlichkeit
knoten: Grundlagen 4: Wahrscheinlichkeit
nachschlagen: ja
order: 15240700
summary: Bisher waren Ereignisse Aussagen wie „gerade“ oder „defekt“.
tags: Zufallsvariable, Wert, Verteilung, diskret, Wahrscheinlichkeitsfunktion, identisch verteilt, Integral, Stammfunktion
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Bisher waren Ereignisse Aussagen wie „gerade“ oder „defekt“. Mit Daten rechnet man aber mit Zahlen: Augenzahlen, Spannungen, Mieten. Dieser Abschnitt führt Zufallsvariablen ein, Größen, deren Wert vom Zufall abhängt, und beschreibt, wie sich ihre Werte verteilen: bei endlich vielen Werten durch eine Liste von Wahrscheinlichkeiten, bei kontinuierlichen Werten durch eine Dichte, deren Fläche die Wahrscheinlichkeit ist. Die Verteilungsfunktion fasst beide Fälle zusammen.
:::

### Zufallsvariablen

<span class="anker" id="stufe-6-1"></span>

Wirft man eine Münze dreimal, ist ein Ergebnis eine Folge wie $(\text K,\text Z,\text K)$ aus Kopf und Zahl. Meist interessiert aber nur eine Zahl, die man daraus berechnet, etwa die Anzahl der Köpfe. Diese Zahl hängt vom Ergebnis ab und ist damit selbst zufällig.

:::definition Definition 6.1 (Zufallsvariable)
<span class="anker" id="satz-6-1"></span>

Eine __Zufallsvariable__ $X$ ist eine Funktion, die jedem Ergebnis $\omega\in\Omega$ eine reelle Zahl $X(\omega)$ zuordnet. Die Zahl $X(\omega)$ heißt der __Wert__ von $X$ beim Ergebnis $\omega$.
:::

Der Name führt in die Irre: Eine Zufallsvariable ist weder zufällig noch eine Variable, sondern eine feste Funktion. Zufällig ist nur, bei welchem Ergebnis sie ausgewertet wird. Zufallsvariablen schreibt man mit großen Buchstaben $X,Y,Z$, ihre möglichen Werte mit kleinen $x,y,z$. Aussagen über Werte sind Ereignisse: $\{X=x\}$ ist die Menge aller Ergebnisse $\omega$ mit $X(\omega)=x$, $\{X\le x\}$ die mit $X(\omega)\le x$. Man schreibt kurz $P(X=x)$ statt $P(\{X=x\})$.

⁠**Rechenbeispiel:** Bei drei fairen Münzwürfen hat $\Omega$ die $8$ gleich wahrscheinlichen Ergebnisse KKK, KKZ, KZK, ZKK, KZZ, ZKZ, ZZK, ZZZ. Die Zufallsvariable $X$ = „Anzahl der Köpfe“ hat die Werte $3,2,2,2,1,1,1,0$. Das Ereignis $\{X=2\}$ ist $\{\text{KKZ},\text{KZK},\text{ZKK}\}$, also ist $P(X=2)=3/8$. Ebenso ist $P(X=0)=P(X=3)=1/8$ und $P(X=1)=3/8$.

⁠**Kurz gesagt:** Eine Zufallsvariable ordnet jedem Ergebnis eine Zahl zu; Aussagen über ihren Wert sind Ereignisse.

### Diskrete Verteilungen

<span class="anker" id="stufe-6-2"></span>

Für Rechnungen mit $X$ braucht man das Ergebnis $\omega$ meist nicht mehr. Es genügt zu wissen, welche Werte $X$ annehmen kann und wie wahrscheinlich jeder ist. Diese Angabe heißt die __Verteilung__ von $X$.

:::definition Definition 6.2 (Diskrete Zufallsvariable, Wahrscheinlichkeitsfunktion)
<span class="anker" id="satz-6-2"></span>

Eine Zufallsvariable heißt __diskret__, wenn sie nur endlich viele oder abzählbar unendlich viele Werte $x_1,x_2,\dots$ annehmen kann. Die Zuordnung

<span class="anker" id="gl-6-1"></span>
$$x_k\mapsto P(X=x_k) \tag{6.1}$$

heißt ihre __Wahrscheinlichkeitsfunktion__. Es gilt $P(X=x_k)\ge0$ und $\sum_kP(X=x_k)=1$.
:::

Die Summe ist $1$, weil die Ereignisse $\{X=x_k\}$ eine Zerlegung von $\Omega$ bilden: Bei jedem Ergebnis hat $X$ genau einen Wert. Umgekehrt ist jede Liste nichtnegativer Zahlen mit der Summe $1$ die Wahrscheinlichkeitsfunktion einer Zufallsvariablen. Man zeichnet sie als Stabdiagramm (Abb. [5](#abb-5), links). Für jede Menge $\mathcal M$ von Werten ist $P(X\in\mathcal M)=\sum_{x_k\in\mathcal M}P(X=x_k)$. Zwei Zufallsvariablen mit derselben Wahrscheinlichkeitsfunktion heißen __identisch verteilt__, auch wenn sie auf verschiedenen Ergebnisräumen leben.

⁠**Rechenbeispiel:** Für die Anzahl $X$ der Köpfe bei drei Münzwürfen ist die Wahrscheinlichkeitsfunktion $\tfrac18,\tfrac38,\tfrac38,\tfrac18$ an den Stellen $0,1,2,3$, mit der Summe $\tfrac88=1$. Die Wahrscheinlichkeit, mindestens zwei Köpfe zu werfen, ist $P(X\ge2)=\tfrac38+\tfrac18=\tfrac12$.

⁠**Kurz gesagt:** Die Verteilung einer diskreten Zufallsvariablen ist die Liste ihrer Werte mit deren Wahrscheinlichkeiten, die sich zu $1$ addieren.

### Was du dafür brauchst: Integrale

<span class="anker" id="stufe-6-3"></span>

Für Zufallsvariablen mit kontinuierlichen Werten werden Summen zu Integralen. Hier das Nötige. Für eine Funktion $f\ge0$ auf einem Intervall $[a,\,b]$ ist das __Integral__

$$\int_a^bf(x)\,\mathrm{d} x$$

der Flächeninhalt zwischen dem Graphen von $f$ und der $x$-Achse von $a$ bis $b$. Man kann es als Grenzwert von Summen verstehen: Man teilt $[a,\,b]$ in $n$ Stücke der Breite $\Delta x=(b-a)/n$ mit Mittelpunkten $x_1,\dots,x_n$, ersetzt die Fläche über jedem Stück durch ein Rechteck der Höhe $f(x_k)$ und addiert: $\sum_{k=1}^nf(x_k)\,\Delta x$. Für $n\to\infty$ geht diese Summe gegen das Integral. Wo $f$ negativ ist, zählt die Fläche negativ.

Ausgerechnet wird ein Integral mit einer __Stammfunktion__ $F$, also einer Funktion mit $F'=f$: Es ist $\int_a^bf(x)\,\mathrm{d} x=F(b)-F(a)$. Integrale über unbeschränkte Bereiche sind Grenzwerte, etwa $\int_{-\infty}^\infty f(x)\,\mathrm{d} x=\lim_{a\to-\infty,\,b\to\infty}\int_a^bf(x)\,\mathrm{d} x$. Zwei Rechenregeln werden gebraucht: Das Integral ist linear, $\int(\alpha f+\beta g)=\alpha\int f+\beta\int g$, und Integrale über aneinandergrenzende Intervalle addieren sich.

⁠**Rechenbeispiel:** Für $f(x)=2x$ auf $[0,\,1]$ ist $F(x)=x^2$ eine Stammfunktion, also $\int_0^12x\,\mathrm{d} x=1-0=1$: Das Dreieck unter der Geraden hat die Grundseite $1$ und die Höhe $2$. Ebenso ist $\int_0^{1/2}2x\,\mathrm{d} x=\tfrac14$. Die Summe mit $n=2$ Rechtecken liefert $\bigl(2\cdot\tfrac14+2\cdot\tfrac34\bigr)\cdot\tfrac12=1$; sie ist hier schon exakt, weil sich bei einer Geraden die Fehler über und unter den Rechteckkanten aufheben.

⁠**Kurz gesagt:** Ein Integral ist der Grenzwert von Summen aus Funktionswert mal Breite, also ein Flächeninhalt; ausgerechnet wird es mit einer Stammfunktion.

### Dichten

<span class="anker" id="stufe-6-4"></span>

Eine Zufallsvariable $T$ beschreibe den Zeitpunkt, zu dem ein Impuls innerhalb einer halben Sekunde eintrifft, wobei kein Zeitpunkt bevorzugt ist. Wie wahrscheinlich ist $T=0{,}2\,\mathrm s$ genau? Weil es unendlich viele mögliche Zeitpunkte gibt, die alle gleich wahrscheinlich sind, muss diese Wahrscheinlichkeit null sein; jeder positive Wert, unendlich oft addiert, ergäbe mehr als $1$. Sinnvoll sind nur Fragen nach Intervallen: Mit welcher Wahrscheinlichkeit liegt $T$ zwischen $0{,}1\,\mathrm s$ und $0{,}3\,\mathrm s$? Hier offenbar $0{,}2/0{,}5=0{,}4$. Solche Wahrscheinlichkeiten beschreibt man als Flächen unter einer Kurve.

:::definition Definition 6.3 (Dichte, stetige Zufallsvariable)
<span class="anker" id="satz-6-3"></span>

Eine Funktion $p$ mit $p(x)\ge0$ für alle $x$ und $\int_{-\infty}^\infty p(x)\,\mathrm{d} x=1$ heißt __Dichte__. Eine Zufallsvariable $X$ heißt __stetig verteilt__ mit der Dichte $p$, wenn für alle $a\le b$

<span class="anker" id="gl-6-2"></span>
$$P(a\le X\le b)=\int_a^bp(x)\,\mathrm{d} x . \tag{6.2}$$
:::

Für eine stetig verteilte Zufallsvariable ist $P(X=x)=\int_x^xp=0$ für jedes einzelne $x$. Deshalb ist es gleichgültig, ob man die Intervallgrenzen mitzählt: $P(a<X<b)=P(a\le X\le b)$. Für ein kurzes Intervall der Breite $\Delta x$ ist die Fläche fast ein Rechteck, also

<span class="anker" id="gl-6-3"></span>
$$P(x\le X\le x+\Delta x)\approx p(x)\,\Delta x . \tag{6.3}$$

Die Dichte ist also eine Wahrscheinlichkeit pro Längeneinheit, wie eine Massendichte eine Masse pro Volumen ist. Dieses Kapitel schreibt $P$ für Wahrscheinlichkeiten und für die Werte einer Wahrscheinlichkeitsfunktion und $p$ für Dichten. Gibt es mehrere Zufallsvariablen, so heißt die Dichte von $X$ auch $p_X$. Für „$X$ ist mit der Dichte $p$ verteilt“ schreibt man kurz $X\sim p$.

:::abbildung ml/k4dichte 5
(a) Die Anzahl der Köpfe bei drei Münzwürfen: Die Wahrscheinlichkeiten sind die Höhen der Stäbe. (b) Der Eintreffzeitpunkt, gleichmäßig verteilt auf $[0;\ 0{,}5]\,\mathrm s$: Die Dichte hat die Höhe $2$ pro Sekunde, und die Wahrscheinlichkeit für $0{,}1\le T\le0{,}3$ ist die Fläche $0{,}2\cdot2=0{,}4$. Bei einer Dichte ist die Höhe keine Wahrscheinlichkeit; erst die Fläche ist eine.
:::

⁠**Rechenbeispiel:** Für den Eintreffzeitpunkt ist $p(t)=2/\mathrm s$ für $0\le t\le0{,}5\,\mathrm s$ und $p(t)=0$ sonst (Abb. [5](#abb-5), rechts). Die Gesamtfläche ist $2\cdot0{,}5=1$. Es ist $P(0{,}1\le T\le0{,}3)=2\cdot0{,}2=0{,}4$ und $P(T\le0{,}1)=0{,}2$. Der Zahlenwert $2$ der Dichte ist größer als $1$, und das ist kein Widerspruch, denn die Dichte ist keine Wahrscheinlichkeit.

⁠**Kurz gesagt:** Bei stetig verteilten Zufallsvariablen ist jeder einzelne Wert unwahrscheinlich; Wahrscheinlichkeiten sind Flächen unter der Dichte, und die Dichte ist Wahrscheinlichkeit pro Längeneinheit.

:::hintergrund Warum eine Dichte eine Einheit hat und größer als $1$ sein darf
In [(6.3)](#gl-6-3) ist $P$ eine reine Zahl und $\Delta x$ hat die Einheit von $x$, etwa Sekunden. Also hat die Dichte die Einheit $1/\mathrm s$, und erst das Produkt $p(x)\,\Delta x$ ist einheitenlos. Rechnet man den Eintreffzeitpunkt in Millisekunden, so liegt er gleichmäßig in $[0,\,500]\,\mathrm{ms}$, und seine Dichte ist $1/500\,\mathrm{ms}^{-1}=0{,}002\,\mathrm{ms}^{-1}$: dieselbe Verteilung, eine andere Zahl. Die Höhe einer Dichte hängt also von der Einheit ab, ihre Flächen nicht. Verlangt ist nur, dass die Gesamtfläche $1$ ist. Eine Dichte, die auf einem kurzen Intervall lebt, muss deshalb hoch sein: Auf $[0;\ 0{,}5]$ braucht sie die Höhe $2$, auf $[0;\ 0{,}001]$ die Höhe $1\,000$. Wer Dichtewerte verschiedener Verteilungen vergleicht, muss deshalb dieselben Einheiten benutzen.
:::

### Die Verteilungsfunktion

<span class="anker" id="stufe-6-5"></span>

Diskrete und stetige Zufallsvariablen werden bisher verschieden beschrieben, einmal durch Stäbe, einmal durch eine Kurve. Eine Beschreibung, die in beiden Fällen gleich aussieht, liefert die Frage: Wie wahrscheinlich ist $X$ höchstens $x$?

:::definition Definition 6.4 (Verteilungsfunktion)
<span class="anker" id="satz-6-4"></span>

Die __Verteilungsfunktion__ einer Zufallsvariablen $X$ ist

<span class="anker" id="gl-6-4"></span>
$$F(x)=P(X\le x)\qquad\text{für alle }x\in\mathbb{R} . \tag{6.4}$$
:::

$F$ steigt von $0$ für sehr kleine $x$ bis $1$ für sehr große $x$ und fällt nie, denn mit wachsendem $x$ wird das Ereignis $\{X\le x\}$ größer. Für $a<b$ ist $P(a<X\le b)=F(b)-F(a)$, weil $\{X\le b\}$ die disjunkte Vereinigung von $\{X\le a\}$ und $\{a<X\le b\}$ ist. Bei einer diskreten Zufallsvariablen ist $F$ eine Treppe, die an jedem Wert $x_k$ um $P(X=x_k)$ springt. Bei einer stetig verteilten ist $F(x)=\int_{-\infty}^xp(t)\,\mathrm{d} t$ die Fläche links von $x$; $F$ hat keine Sprünge, und wo $p$ stetig ist, gilt $F'(x)=p(x)$ (Abb. [6](#abb-6)).

:::abbildung ml/k4vertfkt 6
Verteilungsfunktionen. (a) Bei der diskreten Anzahl der Köpfe eine Treppe mit Stufen der Höhe $\tfrac18,\tfrac38,\tfrac38,\tfrac18$; der gefüllte Punkt zeigt den Wert an der Sprungstelle. (b) Beim gleichmäßig verteilten Eintreffzeitpunkt eine Rampe mit der Steigung $2/\mathrm s$, der Dichte; der Abstand der gestrichelten Linien ist $F(0{,}3)-F(0{,}1)=0{,}4$.
:::

⁠**Rechenbeispiel:** Für die Anzahl der Köpfe ist $F(x)=0$ für $x<0$, $F(x)=\tfrac18$ für $0\le x<1$, $F(x)=\tfrac48$ für $1\le x<2$, $F(x)=\tfrac78$ für $2\le x<3$ und $F(x)=1$ ab $3$. Also ist $P(1<X\le3)=F(3)-F(1)=1-\tfrac12=\tfrac12$. Für den Eintreffzeitpunkt ist $F(t)=2t/\mathrm s$ zwischen $0$ und $0{,}5\,\mathrm s$, und $F(0{,}3)-F(0{,}1)=0{,}6-0{,}2=0{,}4$, wie in Unterabschnitt [6.4](#stufe-6-4).

⁠**Kurz gesagt:** Die Verteilungsfunktion $F(x)=P(X\le x)$ steigt von $0$ auf $1$; bei diskreten Größen ist sie eine Treppe, bei stetig verteilten die Fläche links von $x$ mit $F'=p$.

:::hintergrund Verteilungen, die weder diskret noch stetig sind
Ein Verstärker, der höchstens $5\,\mathrm V$ ausgeben kann, liefert für jedes Eingangssignal, das eigentlich mehr ergäbe, genau $5\,\mathrm V$; man sagt, er geht in die Begrenzung. Ist die unbegrenzte Ausgangsspannung stetig verteilt und mit $10\,\%$ Wahrscheinlichkeit größer als $5\,\mathrm V$, so hat die tatsächliche Ausgangsspannung unterhalb von $5\,\mathrm V$ eine Dichte, aber der einzelne Wert $5\,\mathrm V$ hat die Wahrscheinlichkeit $0{,}1$. Ihre Verteilungsfunktion steigt erst stetig an und springt bei $5\,\mathrm V$ um $0{,}1$ auf $1$. Eine solche Verteilung hat weder eine Wahrscheinlichkeitsfunktion noch eine Dichte, wohl aber eine Verteilungsfunktion. Deshalb ist die Verteilungsfunktion die allgemeinste Beschreibung einer Verteilung.
:::

:::aufgabe Aufgabe 15 ★ Die Augensumme
<span class="anker" id="aufg-15"></span>

Zwei faire Würfel werden geworfen, $G$ sei die Augensumme.

<ol class="al">

<li>

Stelle die Wahrscheinlichkeitsfunktion von $G$ als Tabelle auf und prüfe, dass die Summe $1$ ist.

</li>

<li>

Berechne $P(G\le4)$ und $P(5\le G\le9)$.

</li>

<li>

Gib die Verteilungsfunktion an den Stellen $4$, $4{,}5$ und $12$ an.

</li>

</ol>

:::loesung
(a) Für $s=2,3,\dots,12$ ist $P(G=s)=\tfrac1{36},\tfrac2{36},\tfrac3{36},\tfrac4{36},\tfrac5{36},\tfrac6{36},\tfrac5{36},\tfrac4{36},\tfrac3{36},\tfrac2{36},\tfrac1{36}$, mit der Summe $\tfrac{36}{36}=1$.

(b) $P(G\le4)=\tfrac{1+2+3}{36}=\tfrac16$, $P(5\le G\le9)=\tfrac{4+5+6+5+4}{36}=\tfrac{24}{36}=\tfrac23$.

(c) $F(4)=\tfrac16$, $F(4{,}5)=\tfrac16$, weil zwischen $4$ und $5$ kein Wert liegt, und $F(12)=1$.
:::
:::

:::aufgabe Aufgabe 16 ★★ Eine Dichte bestimmen
<span class="anker" id="aufg-16"></span>

Eine Zufallsvariable $X$ habe die Dichte $p(x)=c\,x^2$ für $0\le x\le2$ und $p(x)=0$ sonst.

<ol class="al">

<li>

Bestimme $c$.

</li>

<li>

Berechne $P(X\le1)$ und $P(1\le X\le2)$.

</li>

<li>

Gib die Verteilungsfunktion an und prüfe $F'=p$. Wo ist die Dichte größer als $1$?

</li>

</ol>

:::loesung
(a) $\int_0^2c\,x^2\,\mathrm{d} x=c\cdot\tfrac83=1$, also $c=\tfrac38$.

(b) $P(X\le1)=\tfrac38\cdot\tfrac13=\tfrac18$ und $P(1\le X\le2)=1-\tfrac18=\tfrac78$.

(c) $F(x)=0$ für $x<0$, $F(x)=\tfrac38\cdot\tfrac{x^3}3=\tfrac{x^3}8$ für $0\le x\le2$, $F(x)=1$ für $x>2$. Es ist $F'(x)=\tfrac38x^2=p(x)$. Die Dichte ist größer als $1$ für $\tfrac38x^2>1$, also für $x>\sqrt{8/3}\approx1{,}63$; bei $x=2$ ist sie $1{,}5$.
:::
:::

:::aufgabe Aufgabe 17 ★★ Dichte und Einheit
<span class="anker" id="aufg-17"></span>

Das Rauschen eines Messgeräts sei gleichmäßig verteilt auf $[-0{,}5\,\mathrm{mV};\ 0{,}5\,\mathrm{mV}]$.

<ol class="al">

<li>

Gib die Dichte in $1/\mathrm{mV}$ und in $1/\mathrm V$ an.

</li>

<li>

Berechne mit beiden Angaben die Wahrscheinlichkeit, dass das Rauschen zwischen $0{,}1\,\mathrm{mV}$ und $0{,}3\,\mathrm{mV}$ liegt.

</li>

</ol>

:::loesung
(a) Das Intervall ist $1\,\mathrm{mV}$ lang, also ist die Dichte $1\,\mathrm{mV}^{-1}$. In Volt ist das Intervall $0{,}001\,\mathrm V$ lang, und die Dichte ist $1\,000\,\mathrm V^{-1}$.

(b) Mit Millivolt: $0{,}2\,\mathrm{mV}\cdot1\,\mathrm{mV}^{-1}=0{,}2$. Mit Volt: $0{,}0002\,\mathrm V\cdot1\,000\,\mathrm V^{-1}=0{,}2$. Die Höhe der Dichte hängt von der Einheit ab, die Wahrscheinlichkeit nicht.
:::
:::

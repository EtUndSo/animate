---
title: Stufe 5: Rechenregeln
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Folgen und Grenzwerte
adresse: elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte
knoten: Kapitel 4: Folgen und Grenzwerte
order: 1240700
summary: Epsilontik verlangt, den Grenzwert vorher zu kennen.
tags: 
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Epsilontik verlangt, den Grenzwert vorher zu kennen. Rechenregeln liefern ihn aus den Bausteinen, ganz ohne $\varepsilon$.
:::

**Die Idee.** Liegt $a_n$ nah bei $a$ und $b_n$ nah bei $b$, liegt die Summe nah bei $a+b$: Die Fehler addieren sich höchstens. Beim Produkt zeigt Abb. [6](#abb-6) den Mechanismus: Der Unterschied zwischen den Rechtecken $a_nb_n$ und $ab$ besteht aus zwei Streifen, jeder hat eine Seite, die gegen 0 geht.

:::satz Satz 5.1 (Rechenregeln für konvergente Folgen)
<span class="anker" id="satz-5-1"></span>

Seien $\{a_n\}$, $\{b_n\}$ konvergent mit Grenzwerten $a,b\in\mathbb{R}$. Dann konvergieren die folgenden Folgen, und es gilt:

<ol class="rm">

<li>

$\lim\limits_{n\to\infty}(a_n+b_n)=\Bigl(\lim\limits_{n\to\infty}a_n\Bigr)+\Bigl(\lim\limits_{n\to\infty}b_n\Bigr)=a+b$,

</li>

<li>

$\lim\limits_{n\to\infty}(a_n\cdot b_n)=\Bigl(\lim\limits_{n\to\infty}a_n\Bigr)\cdot\Bigl(\lim\limits_{n\to\infty}b_n\Bigr)=a\cdot b$,

</li>

<li>

falls $a_n\ne0$ für alle $n$ und $a\ne0$: $\lim\limits_{n\to\infty}\dfrac1{a_n}=\Bigl(\lim\limits_{n\to\infty}a_n\Bigr)^{-1}=a^{-1}$,

</li>

<li>

$\lim\limits_{n\to\infty}|a_n|=\Bigl|\lim\limits_{n\to\infty}a_n\Bigr|=|a|$,

</li>

<li>

falls $a_n\ge0$ für alle $n$: $\lim\limits_{n\to\infty}\sqrt{a_n}=\sqrt{\lim\limits_{n\to\infty}a_n}=\sqrt a$.

</li>

</ol>
:::

⁠**So liest man das:** Jede Regel sagt zweierlei: Die neue Folge konvergiert, und ihr Grenzwert lässt sich aus $a$ und $b$ rechnen. Lesen darf man die Gleichung nur von rechts nach links: Existieren die Grenzwerte rechts, existiert der links. Aus der Konvergenz von $a_n+b_n$ folgt nichts über die Summanden, wie $(-1)^n+(-1)^{n+1}=0$ zeigt. **Voraussetzung nötig:** In (iii) darf $a$ nicht 0 sein: $a_n=\frac1n$ hat Grenzwert 0, aber $1/a_n=n$ ist unbeschränkt.

:::abbildung hm1/k4produkt 6
Produktregel als Fläche: $a_nb_n-ab=(a_n-a)\,b_n+a\,(b_n-b)$. Die Fläche $a_nb_n$ ist das ganze Rechteck, $ab$ der blaue Teil. Für größere $n$ werden beide Streifen schmaler, ihre Fläche geht gegen 0. Das Bild zeigt positive Größen, die Gleichung gilt für alle.
:::

:::beweis Rechenregeln
Alle Teile führen den Abstand auf die Nullfolgen $a_n-a$ und $b_n-b$ zurück.

(i) $(a_n+b_n)-(a+b)=(a_n-a)+(b_n-b)$ ist nach Satz [3.2](nullfolgen-vergleichen.html#satz-3-2) (i) eine Nullfolge.

(ii) Einschieben von $\pm a\,b_n$ gibt $|a_nb_n-ab|=|(a_n-a)\,b_n+a\,(b_n-b)|\le|b_n|\,|a_n-a|+|a|\,|b_n-b|$. Nach Satz [4.2](der-grenzwert.html#satz-4-2) (ii) ist $|b_n|\le C$, also ist $C\,|a_n-a|+|a|\,|b_n-b|$ eine Majorante.

(iii) Zu $\varepsilon=|a|/2$ gibt es $N_0$ mit $|a_n-a|<|a|/2$ für $n>N_0$. Die untere Dreiecksungleichung gibt dort $|a_n|\ge|a|-|a_n-a|>|a|/2$. Also ist $\bigl|\frac1{a_n}-\frac1a\bigr|=\frac{|a-a_n|}{|a_n|\,|a|}\le\frac2{a^2}\,|a_n-a|$ eine Majorante.

(iv) Die untere Dreiecksungleichung gibt $\bigl||a_n|-|a|\bigr|\le|a_n-a|$, eine Majorante.

(v) Es ist $a\ge0$, denn für $a<0$ läge kein Glied $a_n\ge0$ im Schlauch mit $\varepsilon=|a|$. Für $a=0$ ist das Satz [3.2](nullfolgen-vergleichen.html#satz-3-2) (ii). Für $a>0$ gilt nach der dritten binomischen Formel $(\sqrt{a_n}-\sqrt a)(\sqrt{a_n}+\sqrt a)=a_n-a$, also $|\sqrt{a_n}-\sqrt a|=\dfrac{|a_n-a|}{\sqrt{a_n}+\sqrt a}\le\dfrac{|a_n-a|}{\sqrt a}$, wieder eine Majorante.
:::

::::beispiel
Für $r_n=\dfrac{3n^2-n+5}{n^2+4n+1}$ passen die Regeln nicht direkt, denn Zähler und Nenner sind unbeschränkt. Kürzen mit der höchsten Potenz $n^2$ macht aus beiden konvergente Folgen:

$$r_n=\frac{3-\frac1n+\frac5{n^2}}{1+\frac4n+\frac1{n^2}}\ \longrightarrow\ \frac{3-0+0}{1+0+0}=3.$$

Dabei sind $\frac1n$, $\frac1{n^2}$ Nullfolgen, die Regeln (i) und (ii) geben Zähler und Nenner, (iii) und (ii) den Bruch. Zahlen: $r_{10}=2{,}092$, $r_{100}=2{,}875$, $r_{1000}=2{,}987$. Im Rechenmodell gilt ebenso $a_n+s_n\to4$, $a_n\cdot s_n\to4$, $1/a_n\to\frac12$ und $\sqrt{s_n}\to\sqrt2$.
::::

⁠**Grenzfälle:** Ist der Grad des Zählers kleiner als der des Nenners, ergibt das Kürzen 0, ist er größer, wird die Folge unbeschränkt. Bei gleichem Grad zählt das Verhältnis der führenden Koeffizienten, hier $3/1$.

:::frage Bei $\sqrt{n+4}-\sqrt n$ gilt doch „unendlich minus unendlich gleich null“?
Das Ergebnis stimmt, die Begründung nicht. Regel (i) setzt konvergente Summanden voraus, $\sqrt n$ konvergiert nicht. Dass die Differenz zweier unbeschränkter Folgen nichts Bestimmtes ergibt, zeigen $(n+4)-n=4$ und $(2n)-n=n$. Hier hilft erst das Umformen.
:::

:::aufgabe Aufgabe 7 ★★ Grenzwerte ausrechnen
<span class="anker" id="aufg-7"></span>

Bestimme die Grenzwerte und nenne jede benutzte Regel, oder begründe, warum keiner existiert. (a) $\dfrac{5n^2+2}{2n^2-n}$, (b) $\sqrt{n^2+6n}-n$, (c) $\dfrac{4n+1}{n^2+3}+0{,}9^n\,\dfrac{n}{n+1}$, (d) $\dfrac{3^n}{n^5}$.

:::loesung
(a) Kürzen mit $n^2$: $\dfrac{5+2/n^2}{2-1/n}\to\frac52$ nach (i), (ii), (iii). (b) Erweitern: $\dfrac{(n^2+6n)-n^2}{\sqrt{n^2+6n}+n}=\dfrac6{\sqrt{1+6/n}+1}\to\dfrac6{1+1}=3$ nach (i), (iii), (v). (c) Der erste Summand ist $\dfrac{4/n+1/n^2}{1+3/n^2}\to0$. Der zweite ist die Nullfolge $0{,}9^n$ mal der beschränkten Folge $n/(n+1)$. Der Grenzwert ist 0. (d) Mit $q=3^{-1/5}<1$ ist $n^5/3^n=(n\,q^n)^5\to0$ nach Satz [3.4](nullfolgen-vergleichen.html#satz-3-4) (ii) und Regel (ii). Der Kehrwert einer positiven Nullfolge wächst über jede Schranke: Die Folge ist bestimmt divergent.
:::
:::

::::formelsammlung
**Summe und Produkt**

$$\lim_{n\to\infty}(a_n+b_n)=a+b,\qquad\lim_{n\to\infty}(a_n\cdot b_n)=a\cdot b$$

Für $a_n\to a$, $b_n\to b$; die linken Folgen konvergieren. Nur von rechts nach links lesen: Aus der Konvergenz der Summe folgt nichts über die Summanden.

**Kehrwert**

$$\lim_{n\to\infty}\frac1{a_n}=a^{-1}$$

Falls $a_n\ne0$ für alle $n$ und $a\ne0$.

**Betrag und Wurzel**

$$\lim_{n\to\infty}|a_n|=|a|,\qquad\lim_{n\to\infty}\sqrt{a_n}=\sqrt a$$

Die Wurzelregel, falls $a_n\ge0$ für alle $n$; dann ist auch $a\ge0$.

**Produkt als Fläche**

$$a_nb_n-ab=(a_n-a)\,b_n+a\,(b_n-b)$$

Zwei Streifen, jeder mit einer Seite, die gegen 0 geht. Bei Quotienten von Polynomen kürzt man mit der höchsten Potenz.
::::

::::lernkarten
:::karte formel Rechenregeln für Summe und Produkt
Was sagen die Rechenregeln über Summe und Produkt zweier konvergenter Folgen mit $a_n\to a$ und $b_n\to b$?
---
Beide konvergieren, und $\lim_{n\to\infty}(a_n+b_n)=a+b$, $\lim_{n\to\infty}(a_n\cdot b_n)=a\cdot b$: Der Grenzwert der Summe ist die Summe der Grenzwerte, der des Produkts das Produkt.
--- falsch
Beide konvergieren, und $\lim_{n\to\infty}(a_n+b_n)=a+b$; für das Produkt gilt $\lim_{n\to\infty}(a_n\cdot b_n)=a\cdot b$ aber nur, wenn eine der beiden Folgen konstant ist, sonst addieren sich die Fehler.
--- falsch
Beide konvergieren nur, wenn $a$ und $b$ positiv sind; dann gilt $\lim_{n\to\infty}(a_n+b_n)=a+b$ und $\lim_{n\to\infty}(a_n\cdot b_n)=a\cdot b$, sonst kann das Vorzeichen die Konvergenz zerstören.
--- falsch
Beide konvergieren, und $\lim_{n\to\infty}(a_n+b_n)=\max\{a,b\}$, $\lim_{n\to\infty}(a_n\cdot b_n)=a\cdot b$: Bei der Summe setzt sich die größere Folge durch, beim Produkt zählen beide.
:::
:::karte formel Kehrwert, Betrag und Wurzel
Unter welchen Voraussetzungen gelten die Rechenregeln für Kehrwert, Betrag und Wurzel einer konvergenten Folge mit $a_n\to a$?
---
$\lim_{n\to\infty}\frac1{a_n}=a^{-1}$, falls $a_n\ne0$ für alle $n$ und $a\ne0$; $\lim_{n\to\infty}|a_n|=|a|$ ohne Zusatz; $\lim_{n\to\infty}\sqrt{a_n}=\sqrt a$, falls $a_n\ge0$ für alle $n$.
--- falsch
$\lim_{n\to\infty}\frac1{a_n}=a^{-1}$, falls nur $a_n\ne0$ für alle $n$ gilt, auch bei $a=0$; $\lim_{n\to\infty}|a_n|=|a|$ ohne Zusatz; $\lim_{n\to\infty}\sqrt{a_n}=\sqrt a$, falls $a_n\ge0$ für alle $n$.
--- falsch
$\lim_{n\to\infty}\frac1{a_n}=a^{-1}$, falls $a_n\ne0$ für alle $n$ und $a\ne0$; $\lim_{n\to\infty}|a_n|=|a|$ nur für $a_n\ge0$; $\lim_{n\to\infty}\sqrt{a_n}=\sqrt a$ für jede Folge, mit $\sqrt{|a_n|}$ gelesen.
--- falsch
$\lim_{n\to\infty}\frac1{a_n}=-a$, falls $a_n\ne0$ für alle $n$ und $a\ne0$; $\lim_{n\to\infty}|a_n|=|a|$ ohne Zusatz; $\lim_{n\to\infty}\sqrt{a_n}=\sqrt a$, falls $a>0$ ist, gleich wo die Glieder liegen.
:::
:::karte zusammenhang Lesrichtung der Rechenregeln
In welche Richtung darf man die Gleichungen der Rechenregeln lesen, und was folgt aus der Konvergenz von $a_n+b_n$ über die Summanden?
---
Nur von rechts nach links: Existieren die Grenzwerte rechts, existiert der links. Aus der Konvergenz von $a_n+b_n$ folgt nichts über die Summanden, wie $(-1)^n+(-1)^{n+1}=0$ zeigt.
--- falsch
In beide Richtungen: Konvergiert $a_n+b_n$, konvergieren auch $a_n$ und $b_n$, weil man jeden Summanden aus der Summe und dem anderen Summanden zurückrechnen kann.
--- falsch
Nur von links nach rechts: Konvergiert die Summe, konvergieren die Summanden; dass umgekehrt konvergente Summanden eine konvergente Summe ergeben, muss man jeweils neu prüfen.
--- falsch
In beide Richtungen, aber nur bei der Summe: Aus der Konvergenz von $a_n+b_n$ folgt die beider Summanden; beim Produkt kann ein Faktor dagegen divergieren, wenn der andere gegen 0 geht.
:::
:::karte zusammenhang Kehrwert bei Grenzwert null
Warum darf in der Kehrwertregel der Grenzwert $a$ nicht 0 sein?
---
Weil der Kehrwert sonst über alle Grenzen wachsen kann: $a_n=\frac1n$ hat den Grenzwert 0, aber $1/a_n=n$ ist unbeschränkt. Im Beweis braucht man ab einem Index $|a_n|>|a|/2>0$, die Glieder müssen von 0 wegbleiben.
--- falsch
Weil $a^{-1}$ für $a=0$ als $\infty$ festgelegt ist und $\infty$ keine reelle Zahl ist; die Folge $1/a_n$ konvergiert trotzdem, nur eben gegen $\infty$ statt gegen eine Zahl, und das schließt die Regel aus.
--- falsch
Weil dann einzelne Glieder $a_n=0$ sein könnten; sind dagegen alle $a_n\ne0$, gilt die Regel auch für $a=0$, und der Grenzwert $\frac10$ ist dann als Ergebnis erlaubt, etwa bei $a_n=\frac1n$.
--- falsch
Weil der Kehrwert einer Nullfolge wieder eine Nullfolge ist: $1/a_n$ ginge dann gegen 0 statt gegen $a^{-1}$, und die Regel lieferte das falsche Ergebnis. Für $a\ne0$ tritt das nicht auf.
:::
:::karte zusammenhang Produktregel als Fläche
Warum geht $a_nb_n-ab$ gegen 0, wenn $a_n\to a$ und $b_n\to b$, und wie zeigt das Bild der Rechtecke den Mechanismus?
---
Weil $a_nb_n-ab=(a_n-a)\,b_n+a\,(b_n-b)$ ist: Der Unterschied der Rechtecke $a_nb_n$ und $ab$ besteht aus zwei Streifen, jeder hat eine Seite, die gegen 0 geht. Die andere Seite bleibt beschränkt, also schrumpft die Fläche.
--- falsch
Weil $a_nb_n-ab=(a_n-a)(b_n-b)$ ist: Der Unterschied der Rechtecke ist ein einziges kleines Rechteck, dessen beide Seiten gegen 0 gehen, sodass seine Fläche sogar quadratisch schnell verschwindet.
--- falsch
Weil $a_nb_n-ab=(a_n-a)+(b_n-b)$ ist: Der Unterschied der Rechtecke besteht aus zwei Streifen der Breite 1, deren Längen gegen 0 gehen, also schrumpft die Fläche der beiden Streifen.
--- falsch
Weil $a_nb_n-ab=(a_n-a)\,b_n+a\,(b_n-b)$ ist; die Streifen werden schmaler, aber ihre Längen wachsen mit, sodass die Fläche nur dann schrumpft, wenn $a$ und $b$ beide positiv sind.
:::
:::karte herleitung Produktregel
Wie beweist man, dass $a_n\cdot b_n\to a\cdot b$ gilt, wenn $a_n\to a$ und $b_n\to b$?
---
Man schiebt $\pm a\,b_n$ ein, weil dann jeder Teil eine der Nullfolgen $a_n-a$ und $b_n-b$ enthält: $a_nb_n-ab=(a_n-a)\,b_n+a\,(b_n-b)$.
---
Es folgt $|a_nb_n-ab|\le|b_n|\,|a_n-a|+|a|\,|b_n-b|$, weil der Betrag einer Summe nach der Dreiecksungleichung höchstens die Summe der Beträge ist.
---
Es gibt ein $C$ mit $|b_n|\le C$, weil die konvergente Folge $\{b_n\}$ beschränkt ist.
---
Also ist $C\,|a_n-a|+|a|\,|b_n-b|$ eine Majorante, weil Vielfache und Summen von Nullfolgen Nullfolgen sind; das Vergleichskriterium gibt die Behauptung.
:::
:::karte herleitung Kehrwertregel
Wie beweist man $\frac1{a_n}\to\frac1a$ für $a_n\to a$ mit $a\ne0$ und $a_n\ne0$ für alle $n$?
---
Zu $\varepsilon=|a|/2$ gibt es $N_0$ mit $|a_n-a|<|a|/2$ für $n>N_0$, weil $|a|/2>0$ eine erlaubte Toleranz ist.
---
Dort gilt $|a_n|\ge|a|-|a_n-a|>|a|/2$, weil die untere Dreiecksungleichung $\bigl||a_n|-|a|\bigr|\le|a_n-a|$ das liefert; die Glieder bleiben also von 0 weg.
---
Damit ist $\bigl|\frac1{a_n}-\frac1a\bigr|=\frac{|a-a_n|}{|a_n|\,|a|}\le\frac2{a^2}\,|a_n-a|$, weil der Nenner $|a_n|\,|a|$ größer als $a^2/2$ ist.
---
Rechts steht ein festes Vielfaches der Nullfolge $|a_n-a|$, also eine Majorante, weil $\frac2{a^2}$ nicht von $n$ abhängt; das Vergleichskriterium gibt die Behauptung.
:::
:::karte zusammenhang Kürzen mit der höchsten Potenz
Wie bestimmt man den Grenzwert von $r_n=\frac{3n^2-n+5}{n^2+4n+1}$, obwohl die Rechenregeln nicht direkt passen?
---
Zähler und Nenner sind unbeschränkt, also kürzt man mit der höchsten Potenz $n^2$: $r_n=\frac{3-\frac1n+\frac5{n^2}}{1+\frac4n+\frac1{n^2}}$. Nun sind Zähler und Nenner konvergent, und die Regeln geben $\frac{3-0+0}{1+0+0}=3$.
--- falsch
Man setzt $n=\infty$ ein und kürzt $\infty^2$ heraus, sodass $\frac{3\infty^2}{\infty^2}=3$ bleibt. Die Rechenregeln passen direkt, weil Zähler und Nenner beide gegen $\infty$ gehen und sich gleiche Grenzwerte kürzen lassen.
--- falsch
Man kürzt mit der niedrigsten Potenz $n$: $r_n=\frac{3n-1+\frac5n}{n+4+\frac1n}$. Dann sind Zähler und Nenner konvergent, und die Quotientenregel gibt den Grenzwert $-\frac14$ aus den beiden Absolutgliedern.
--- falsch
Zähler und Nenner sind unbeschränkt, also kürzt man mit $n^2$; die Regeln geben dann das Verhältnis der Absolutglieder, also $\frac51=5$, weil alle Terme mit $n$ beim Grenzübergang verschwinden.
:::
:::karte zusammenhang Grad von Zähler und Nenner
Was ergibt das Kürzen mit der höchsten Potenz bei einem Quotienten zweier Polynome in $n$, je nachdem, wie die Grade von Zähler und Nenner zueinander stehen?
---
Ist der Grad des Zählers kleiner als der des Nenners, ergibt sich der Grenzwert 0; ist er größer, wird die Folge unbeschränkt. Bei gleichem Grad zählt das Verhältnis der führenden Koeffizienten.
--- falsch
Ist der Grad des Zählers kleiner als der des Nenners, wird die Folge unbeschränkt; ist er größer, ergibt sich der Grenzwert 0. Bei gleichem Grad zählt das Verhältnis der führenden Koeffizienten.
--- falsch
Ist der Grad des Zählers kleiner als der des Nenners, ergibt sich 0; ist er größer, ebenfalls 0, weil beide unbeschränkt sind. Bei gleichem Grad zählt das Verhältnis der Absolutglieder.
--- falsch
Ist der Grad des Zählers kleiner als der des Nenners, ergibt sich 0; ist er größer, das Verhältnis der führenden Koeffizienten. Bei gleichem Grad ist der Grenzwert immer 1.
:::
:::karte zusammenhang unendlich minus unendlich
Warum ist „unendlich minus unendlich gleich null“ keine gültige Begründung dafür, dass $\sqrt{n+4}-\sqrt n$ gegen 0 geht?
---
Die Summenregel setzt konvergente Summanden voraus, und $\sqrt n$ konvergiert nicht. Die Differenz zweier unbeschränkter Folgen ergibt nichts Bestimmtes, wie $(n+4)-n=4$ und $(2n)-n=n$ zeigen; hier hilft erst das Umformen.
--- falsch
Sie ist gültig, denn zwei Folgen, die beide gegen $\infty$ gehen, haben denselben Grenzwert, und die Summenregel gibt dann $\infty-\infty=0$. Das Umformen mit der dritten binomischen Formel ist nur eine Kontrolle.
--- falsch
Weil $\infty-\infty$ nach den Rechenregeln $\infty$ ergibt: Der größere der beiden Terme, hier $\sqrt{n+4}$, setzt sich durch, und das Ergebnis 0 stimmt deshalb nur zufällig, weil sich die Fehler gerade aufheben.
--- falsch
Weil die Summenregel nur für Summen gilt, nicht für Differenzen. Schreibt man die Differenz als Summe $\sqrt{n+4}+(-\sqrt n)$, ist die Begründung dagegen korrekt, und das Ergebnis 0 folgt unmittelbar.
:::
:::karte zusammenhang Grenzwert nicht negativer Folgen
Warum hat eine konvergente Folge mit $a_n\ge0$ für alle $n$ einen Grenzwert $a\ge0$?
---
Wäre $a<0$, läge im Schlauch um $a$ mit $\varepsilon=|a|$ kein einziges Glied $a_n\ge0$, denn dieser Schlauch reicht nur bis 0 und enthält nur negative Zahlen. Das widerspricht der Konvergenz, also ist $a\ge0$.
--- falsch
Weil die Wurzelregel $\lim\sqrt{a_n}=\sqrt a$ verlangt, dass $\sqrt a$ existiert; also muss $a\ge0$ sein, und das folgt aus der Regel selbst, ohne dass man den Schlauch betrachten muss.
--- falsch
Das gilt nur für monotone Folgen: Eine fallende Folge aus nicht negativen Gliedern kann sich einem negativen Grenzwert nähern, wenn sie schnell genug fällt, wie etwa die Folge $\frac1n-1$.
--- falsch
Weil der Grenzwert stets eines der Folgenglieder ist, nämlich das, bei dem die Folge zur Ruhe kommt; und weil alle Glieder nicht negativ sind, ist es auch dieses eine Glied, der Grenzwert.
:::
::::

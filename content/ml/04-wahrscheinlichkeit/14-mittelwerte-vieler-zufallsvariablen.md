---
title: Mittelwerte vieler Zufallsvariablen
pfad: Informatik / Machine Learning / Mathematische Grundlagen / Wahrscheinlichkeit
adresse: informatik/machine-learning/mathematische-grundlagen/wahrscheinlichkeit
knoten: Kapitel 4: Wahrscheinlichkeit
nachschlagen: ja
order: 15241400
summary: Mittelt man viele unabhängige Messungen, so wird das Ergebnis immer genauer, und seine Schwankungen haben fast immer dieselbe Glockenform, gleichgültig, wie die einzelnen Messungen verteilt sind.
tags: Standardfehler, schwaches, starke
lang: de
---

<span class="anker" id="stufe-13"></span>

:::zweck
Mittelt man viele unabhängige Messungen, so wird das Ergebnis immer genauer, und seine Schwankungen haben fast immer dieselbe Glockenform, gleichgültig, wie die einzelnen Messungen verteilt sind. Dieser Abschnitt rechnet nach, wie schnell der Mittelwert genauer wird, beweist das Gesetz der großen Zahlen, das den Mittelwert eines Datensatzes mit dem Erwartungswert verbindet, und stellt den zentralen Grenzwertsatz vor, der erklärt, warum die Normalverteilung überall auftritt.
:::

### Der Mittelwert unabhängiger Zufallsvariablen

<span class="anker" id="stufe-13-1"></span>

Ein verrauschter Messwert schwankt mit der Standardabweichung $\sigma$. Misst man $n$-mal und mittelt, so heben sich die Abweichungen teilweise auf. Wie stark?

:::satz Satz 13.1 (Erwartungswert und Varianz des Mittelwerts)
<span class="anker" id="satz-13-1"></span>

Es seien $X_1,\dots,X_n$ i.i.d. mit dem Erwartungswert $\mu$ und der Varianz $\sigma^2$, und $\bar X_n=\frac1n\sum_{i=1}^nX_i$ ihr Mittelwert. Dann ist

<span class="anker" id="gl-13-1"></span>
$$\mathbb{E}[\bar X_n]=\mu,\qquad \operatorname{Var}(\bar X_n)=\frac{\sigma^2}n,\qquad \sigma_{\bar X_n}=\frac\sigma{\sqrt n}. \tag{13.1}$$

Die Standardabweichung $\sigma/\sqrt n$ des Mittelwerts heißt __Standardfehler__.
:::

Der Erwartungswert folgt aus der Linearität. Für die Varianz addieren sich nach [(10.4)](kovarianz-und-korrelation.html#gl-10-4) die $n$ Varianzen zu $n\sigma^2$, und der Faktor $\tfrac1n$ geht nach [(7.8)](erwartungswert-und-varianz.html#gl-7-8) quadriert ein: $\tfrac1{n^2}\cdot n\sigma^2=\sigma^2/n$. Dabei braucht man nur, dass die $X_i$ paarweise unkorreliert sind. Der Mittelwert wird also mit wachsendem $n$ genauer, aber langsam: Für die halbe Streuung braucht man viermal so viele Messungen, für ein Zehntel hundertmal so viele.

::::beispiel [Rechenbeispiel]
Eine Küchenwaage habe Rauschen mit $\sigma=5\,\mathrm g$. Der Mittelwert aus $16$ Wägungen hat den Standardfehler $5/4=1{,}25\,\mathrm g$, der aus $100$ Wägungen $0{,}5\,\mathrm g$. Mitteln über $n$ Wiederholungen macht den zufälligen Fehler also $\sqrt n$-mal kleiner: Für ein zehnmal genaueres Ergebnis braucht man hundertmal so viele Messungen. Der Mittelwert von $100$ Würfen eines Würfels hat den Standardfehler $1{,}708/10\approx0{,}171$.
::::

⁠**Kurz gesagt:** Der Mittelwert von $n$ unabhängigen Größen hat denselben Erwartungswert und die Standardabweichung $\sigma/\sqrt n$: Er wird genauer, aber nur mit der Wurzel aus $n$.

### Die Tschebyschow-Ungleichung

<span class="anker" id="stufe-13-2"></span>

Die Varianz sagt, wie weit eine Zufallsvariable typischerweise streut. Wie wahrscheinlich ist eine große Abweichung? Ohne die Verteilung zu kennen, lässt sich das nicht genau sagen, aber eine obere Schranke gibt es immer.

:::satz Satz 13.2 (Tschebyschow-Ungleichung)
<span class="anker" id="satz-13-2"></span>

Für jede Zufallsvariable $X$ mit dem Erwartungswert $\mu$ und der Varianz $\sigma^2$ und jedes $\varepsilon>0$ ist

<span class="anker" id="gl-13-2"></span>
$$P\bigl(|X-\mu|\ge\varepsilon\bigr)\le\frac{\sigma^2}{\varepsilon^2} . \tag{13.2}$$
:::

:::beweis Tschebyschow-Ungleichung
Es sei $A$ das Ereignis $|X-\mu|\ge\varepsilon$. Auf $A$ ist $(X-\mu)^2\ge\varepsilon^2$, außerhalb von $A$ ist $(X-\mu)^2\ge0$. Also ist $(X-\mu)^2\ge\varepsilon^2\,\mathbb 1_A$ für jedes Ergebnis, und der Erwartungswert ergibt $\sigma^2\ge\varepsilon^2\,P(A)$.
:::

Mit $\varepsilon=k\sigma$ heißt das: Um mindestens $k$ Standardabweichungen weicht eine Zufallsvariable höchstens mit der Wahrscheinlichkeit $1/k^2$ ab, gleich wie sie verteilt ist. Für $k=2$ sind das $25\,\%$, für $k=3$ etwa $11\,\%$. Bei der Normalverteilung sind es nur $4{,}6\,\%$ und $0{,}3\,\%$. Die Schranke ist grob, weil sie für jede Verteilung gelten muss, aber sie braucht nur die Varianz.

::::beispiel [Rechenbeispiel]
Für einen Würfel ist $P(|X-3{,}5|\ge2{,}5)\le\frac{35/12}{6{,}25}\approx0{,}467$. Tatsächlich ist die Wahrscheinlichkeit $P(X\in\{1,6\})=\tfrac13$.
::::

⁠**Kurz gesagt:** Eine Abweichung um mindestens $\varepsilon$ hat höchstens die Wahrscheinlichkeit $\sigma^2/\varepsilon^2$, für jede Verteilung.

### Das Gesetz der großen Zahlen

<span class="anker" id="stufe-13-3"></span>

Abschnitt [2](wahrscheinlichkeit-2.html#stufe-2) hat Wahrscheinlichkeiten mit relativen Häufigkeiten begründet, die sich bei vielen Wiederholungen einpendeln. Mit den beiden letzten Unterabschnitten lässt sich beweisen, dass sie das tun.

:::satz Satz 13.3 (Gesetz der großen Zahlen)
<span class="anker" id="satz-13-3"></span>

Es seien $X_1,X_2,\dots$ i.i.d. mit dem Erwartungswert $\mu$ und der Varianz $\sigma^2$. Dann gilt für jedes $\varepsilon>0$

<span class="anker" id="gl-13-3"></span>
$$P\bigl(|\bar X_n-\mu|\ge\varepsilon\bigr)\le\frac{\sigma^2}{n\,\varepsilon^2}\quad\longrightarrow\quad0\qquad\text{für }n\to\infty . \tag{13.3}$$
:::

Das folgt aus der Tschebyschow-Ungleichung für $\bar X_n$ mit der Varianz $\sigma^2/n$ aus [(13.1)](#gl-13-1). Wie klein man die Toleranz $\varepsilon$ auch wählt: Die Wahrscheinlichkeit, dass der Mittelwert um mehr als $\varepsilon$ danebenliegt, geht gegen null. Abb. [19](#abb-19) zeigt drei Folgen von Würfen, deren laufende Mittelwerte sich der $3{,}5$ nähern.

:::abbildung ml/k4lln 19
Drei Folgen von je $10\,000$ Würfen eines fairen Würfels, mit einem Rechner erzeugt. Aufgetragen ist der Mittelwert der ersten $n$ Würfe gegen $n$, waagrecht logarithmisch. Die gestrichelten Kurven liegen bei $3{,}5\pm2\sigma/\sqrt n$ mit $\sigma=\sqrt{35/12}$: Zwischen ihnen liegt der laufende Mittelwert für großes $n$ mit etwa $95\,\%$ Wahrscheinlichkeit. Die Abweichungen von $3{,}5$ schrumpfen wie $1/\sqrt n$, nach $10\,000$ Würfen auf wenige Hundertstel.
:::

Zwei Folgerungen schließen Kreise. Erstens: Ist $X_i$ die Indikatorvariable eines Ereignisses $A$ im $i$-ten Versuch, so ist $\bar X_n$ die relative Häufigkeit $h_n(A)$ und $\mu=P(A)$. Die relative Häufigkeit nähert sich also der Wahrscheinlichkeit, mit dem Standardfehler $\sqrt{P(A)(1-P(A))/n}$. Das ist die Brücke zwischen der Deutung als Häufigkeit und den Axiomen aus Unterabschnitt [2.2](wahrscheinlichkeit-2.html#stufe-2-2). Zweitens: Der Mittelwert eines Datensatzes aus $N$ i.i.d. Datenpunkten nähert sich mit wachsendem $N$ dem Erwartungswert der Verteilung, aus der die Daten stammen. Das ist die Antwort auf die Frage aus Unterabschnitt [7.7](erwartungswert-und-varianz.html#stufe-7-7): Der Mittelwert der Daten ist zufällig, aber er streut immer enger um den Erwartungswert, mit dem Standardfehler $\sigma/\sqrt N$.

::::beispiel [Rechenbeispiel]
Für $1\,000$ Würfe eines Würfels und $\varepsilon=0{,}1$ gibt [(13.3)](#gl-13-3) $P(|\bar X_{1000}-3{,}5|\ge0{,}1)\le\frac{35/12}{1000\cdot0{,}01}\approx0{,}29$. Die Schranke ist grob; der zentrale Grenzwertsatz im nächsten Unterabschnitt liefert etwa $0{,}064$.
::::

⁠**Kurz gesagt:** Der Mittelwert vieler unabhängiger Wiederholungen nähert sich dem Erwartungswert; relative Häufigkeiten nähern sich den Wahrscheinlichkeiten und Mittelwerte von Daten den Erwartungswerten.

:::hintergrund Herkunft und Grenzen des Gesetzes
Den ersten Beweis für relative Häufigkeiten gab Jakob Bernoulli; sein Buch erschien 1713, acht Jahre nach seinem Tod. Die hier bewiesene Form heißt __schwaches__ Gesetz der großen Zahlen, weil sie nur sagt, dass große Abweichungen bei großem $n$ unwahrscheinlich werden. Das __starke__ Gesetz sagt mehr: Mit Wahrscheinlichkeit $1$ konvergiert die Folge der Mittelwerte selbst; es gilt schon, wenn $\mathbb{E}[|X|]$ endlich ist. Ohne Erwartungswert gilt keines von beiden. Die Verteilung mit der Dichte $1/(\pi(1+x^2))$ hat zum Beispiel keinen Erwartungswert, weil $\int|x|/(\pi(1+x^2))\,\mathrm{d} x$ unendlich ist; der Mittelwert von $n$ unabhängigen solchen Größen hat wieder genau dieselbe Verteilung wie eine einzelne, und Mitteln hilft überhaupt nicht. Solche Verteilungen treten auf, wenn gelegentlich riesige Ausreißer vorkommen; Mittelwerte sind dann wertlos, Mediane nicht.
:::

### Der zentrale Grenzwertsatz

<span class="anker" id="stufe-13-4"></span>

Das Gesetz der großen Zahlen sagt, dass der Mittelwert sich auf $\mu$ zusammenzieht. Vergrößert man die Abweichungen mit dem Faktor $\sqrt n/\sigma$, sodass ihre Varianz $1$ bleibt, sieht man eine erstaunliche Gestalt: Gleichgültig, wie die einzelnen $X_i$ verteilt sind, die standardisierten Mittelwerte werden normalverteilt. Abb. [20](#abb-20) zeigt das für Würfel. Ein einzelner Würfel ist gleichmäßig verteilt, der Mittelwert zweier Würfel dreieckig, der von drei Würfeln schon gerundet, und bei zehn Würfeln ist er von der Glocke kaum zu unterscheiden.

:::abbildung ml/k4zgws 20
Die Verteilung des Mittelwerts von $n$ fairen Würfeln, genau berechnet, für $n=1$, $2$, $3$ und $10$. Jeder mögliche Mittelwert ist ein Balken; seine Höhe ist die Wahrscheinlichkeit geteilt durch den Abstand $1/n$ benachbarter Werte, sodass die Balken die Gesamtfläche $1$ haben und mit einer Dichte vergleichbar sind. Rot die Dichte der Normalverteilung mit demselben Erwartungswert $3{,}5$ und derselben Varianz $\tfrac{35}{12n}$.
:::

:::satz Satz 13.4 (Zentraler Grenzwertsatz)
<span class="anker" id="satz-13-4"></span>

Es seien $X_1,X_2,\dots$ i.i.d. mit dem Erwartungswert $\mu$ und einer endlichen Varianz $\sigma^2>0$. Dann gilt für jedes $z\in\mathbb{R}$

<span class="anker" id="gl-13-4"></span>
$$P\Bigl(\frac{\bar X_n-\mu}{\sigma/\sqrt n}\le z\Bigr)\ \longrightarrow\ \Phi(z)\qquad\text{für }n\to\infty . \tag{13.4}$$
:::

Für großes $n$ ist $\bar X_n$ also näherungsweise $\mathcal N(\mu,\sigma^2/n)$-verteilt und die Summe $X_1+\dots+X_n$ näherungsweise $\mathcal N(n\mu,\,n\sigma^2)$-verteilt. Der Satz ist ohne Beweis angegeben; der Beweis braucht mehr Analysis, als dieses Kapitel bereitstellt. Wie groß $n$ sein muss, hängt von der Verteilung der $X_i$ ab: Bei symmetrischen Verteilungen wie dem Würfel genügen wenige Summanden, bei sehr schiefen braucht man mehr. Für die Binomialverteilung als Summe von Bernoulli-Variablen sagt der Satz, dass $\mathrm{Bin}(n,\theta)$ für großes $n$ fast eine Normalverteilung mit $n\theta$ und $n\theta(1-\theta)$ ist; das war die erste Form des Satzes, gefunden 1733 von Abraham de Moivre.

::::beispiel [Rechenbeispiel]
Für den Mittelwert von $1\,000$ Würfen ist $\sigma/\sqrt n=1{,}708/\sqrt{1000}\approx0{,}054$. Eine Abweichung von mindestens $0{,}1$ sind $0{,}1/0{,}054\approx1{,}85$ Standardfehler, also ist $P(|\bar X_{1000}-3{,}5|\ge0{,}1)\approx2\,\bigl(1-\Phi(1{,}85)\bigr)\approx0{,}064$. Eine Waage mit beliebig verteiltem Rauschen der Standardabweichung $2\,\mathrm g$ liefert über $100$ Wägungen gemittelt einen Wert, der mit etwa $95\,\%$ Wahrscheinlichkeit um höchstens $1{,}96\cdot0{,}2\,\mathrm g\approx0{,}39\,\mathrm g$ vom wahren Wert abweicht.
::::

⁠**Kurz gesagt:** Mittelwerte und Summen vieler unabhängiger Größen mit endlicher Varianz sind näherungsweise normalverteilt, gleich wie die einzelnen Größen verteilt sind.

:::hintergrund Warum die Glocke entsteht: Faltung
Die Verteilung einer Summe unabhängiger Größen ist die Faltung ihrer Verteilungen, dieselbe Rechnung wie bei der Nachwirkung im Kaminofen aus [Kapitel 1, Abschnitt 8.2](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/lineare-abbildungen.html#stufe-8-2): Die Augensumme $s$ zweier Würfel entsteht aus allen Paaren $(k,\,s-k)$, also ist $P(X+Y=s)=\sum_kP(X=k)\,P(Y=s-k)$, mit Dichten ebenso als Integral. Abb. [20](#abb-20) ist so berechnet. Die Faltung zweier Rechtecke ist ein Dreieck, die von drei Rechtecken ein Stück aus Parabeln, und wiederholte Faltung glättet jede Form weiter. Bei jeder Faltung addieren sich die Erwartungswerte und die Varianzen, wie Abschnitt [10](kovarianz-und-korrelation.html#stufe-10) gezeigt hat. Nach dem Standardisieren sind Erwartungswert und Varianz festgelegt, und alle feineren Eigenheiten der Ausgangsverteilung werden mit wachsendem $n$ ausgeglättet. Genauer: Die größte Abweichung zwischen der Verteilungsfunktion des standardisierten Mittelwerts und $\Phi$ ist höchstens eine feste Zahl mal $\mathbb{E}[|X-\mu|^3]/(\sigma^3\sqrt n)$; sie schrumpft also mit $1/\sqrt n$, und schiefe, weit ausladende Verteilungen brauchen mehr Summanden. Bei der Normalverteilung selbst ändert das Falten die Form gar nicht, denn die Summe unabhängiger normalverteilter Größen ist wieder normalverteilt. Sie ist deshalb die Form, auf die wiederholtes Falten zuläuft.
:::

:::hintergrund Warum Rauschen so oft normalverteilt ist
Ein Messfehler hat selten nur eine Ursache. Beim Wiegen tragen ein Luftzug, eine leichte Erschütterung, die Temperatur der Waage, ein nicht ganz gerader Boden und vieles mehr je ein kleines Stück bei, mal in die eine, mal in die andere Richtung und unabhängig voneinander. Nach dem zentralen Grenzwertsatz ist eine solche Summe vieler kleiner Beiträge näherungsweise normalverteilt. Sehen kann man das an einem Galtonbrett, einem schrägen Brett mit versetzten Reihen von Nägeln: Jede Kugel prallt an jeder Reihe zufällig nach links oder rechts ab, ihre Endlage ist die Summe vieler solcher kleinen Schritte, und unten stapeln sich die Kugeln zu einer Glocke. Dasselbe Argument erklärt, warum die Körpergrößen Erwachsener eines Geschlechts ungefähr glockenförmig verteilt sind: Viele Erbanlagen und Einflüsse der Umwelt tragen je ein kleines Stück bei. Ein Messfehler, der aus vielen kleinen, unabhängigen Störungen zusammengesetzt ist, ist also näherungsweise normalverteilt. Deshalb ist die Normalverteilung die natürliche erste Annahme für das Rauschen $\nu$ in [(8.8)](wichtige-verteilungen.html#gl-8-8), und ein Fehler, der sich deutlich nicht normal verhält, ist ein Hinweis auf wenige große Störquellen.
:::

:::aufgabe Aufgabe 41 ★ Dreißig Würfe (praktisch)
<span class="anker" id="aufg-41"></span>

Würfle $30$-mal und notiere die Augenzahlen.

<ol class="al">

<li>

Berechne den laufenden Mittelwert nach $1,2,5,10,20$ und $30$ Würfen und trage ihn in eine Skizze wie Abb. [19](#abb-19) ein.

</li>

<li>

Liegen deine Werte zwischen $3{,}5-2\sigma/\sqrt n$ und $3{,}5+2\sigma/\sqrt n$? Berechne diese Grenzen für $n=10$ und $n=30$.

</li>

<li>

Wie viele Würfe bräuchtest du, damit der Standardfehler unter $0{,}05$ liegt?

</li>

</ol>

:::loesung
(a) Die Werte hängen von deinen Würfen ab.

(b) Mit $\sigma=\sqrt{35/12}\approx1{,}708$ ist $2\sigma/\sqrt{10}\approx1{,}08$ und $2\sigma/\sqrt{30}\approx0{,}62$: Die Grenzen sind $2{,}42$ bis $4{,}58$ für $n=10$ und $2{,}88$ bis $4{,}12$ für $n=30$. Etwa $95\,\%$ aller Versuchsreihen liegen dazwischen. Liegt deine knapp außerhalb, ist das kein Fehler; eine von zwanzig Reihen tut das.

(c) $\sigma/\sqrt n<0{,}05$ verlangt $n>(1{,}708/0{,}05)^2\approx1\,167$. Für eine weitere Stelle Genauigkeit braucht man hundertmal so viele Würfe.
:::
:::

:::aufgabe Aufgabe 42 ★★ Wie oft messen?
<span class="anker" id="aufg-42"></span>

Eine Küchenwaage hat Rauschen mit der Standardabweichung $5\,\mathrm g$.

<ol class="al">

<li>

Wie viele Wägungen muss man mitteln, damit der Standardfehler höchstens $0{,}5\,\mathrm g$ ist?

</li>

<li>

Wie viele, damit der Mittelwert nach der Tschebyschow-Ungleichung mit mindestens $95\,\%$ Wahrscheinlichkeit um weniger als $1\,\mathrm g$ vom wahren Wert abweicht? Wie viele nach dem zentralen Grenzwertsatz?

</li>

<li>

Warum hilft Mitteln nicht gegen einen festen Versatz der Waage?

</li>

</ol>

:::loesung
(a) $5/\sqrt n\le0{,}5$ ergibt $\sqrt n\ge10$, also $n\ge100$.

(b) Tschebyschow: $\frac{25}{n\cdot1^2}\le0{,}05$ ergibt $n\ge500$. Zentraler Grenzwertsatz: $1{,}96\cdot5/\sqrt n\le1$ ergibt $\sqrt n\ge9{,}8$, also $n\ge97$. Die Tschebyschow-Schranke gilt für jede Verteilung und verlangt deshalb fünfmal so viele Messungen.

(c) Ein fester Versatz ist bei jeder Messung derselbe. Er gehört nicht zum Rauschen mit Erwartungswert $0$, sondern verschiebt den Erwartungswert, und der Mittelwert nähert sich dem verschobenen Erwartungswert. Gegen einen Versatz hilft nur Kalibrieren.
:::
:::

:::aufgabe Aufgabe 43 ★★ Zwölf Gleichverteilte
<span class="anker" id="aufg-43"></span>

Es sei $Q=U_1+\dots+U_{12}-6$ mit unabhängigen, auf $[0,\,1]$ gleichverteilten $U_i$.

<ol class="al">

<li>

Berechne $\mathbb{E}[Q]$ und $\operatorname{Var}(Q)$.

</li>

<li>

Warum ist $Q$ näherungsweise standardnormalverteilt? Wie wahrscheinlich ist ungefähr $|Q|\le1$?

</li>

<li>

Welche Werte kann $Q$ nicht annehmen, die eine standardnormalverteilte Größe annehmen kann? Was bedeutet das für die Wahrscheinlichkeit sehr großer Abweichungen?

</li>

</ol>

:::loesung
(a) $\mathbb{E}[Q]=12\cdot\tfrac12-6=0$ und $\operatorname{Var}(Q)=12\cdot\tfrac1{12}=1$, weil sich die Varianzen der unabhängigen Summanden addieren und die Verschiebung um $6$ nichts ändert.

(b) $Q$ ist bis auf die Verschiebung eine Summe von zwölf unabhängigen, identisch verteilten Größen; nach dem zentralen Grenzwertsatz und Abb. [20](#abb-20) sieht eine solche Summe schon fast wie eine Glocke aus. Also ist $P(|Q|\le1)\approx0{,}683$.

(c) $Q$ liegt immer zwischen $-6$ und $6$. Eine standardnormalverteilte Größe ist mit kleiner, aber positiver Wahrscheinlichkeit größer als $6$. Für sehr große Abweichungen ist die Näherung deshalb schlecht: $Q$ hat zu dünne Ränder. Für die meisten Zwecke ist das ohne Bedeutung, denn $P(|Z|>6)\approx2\cdot10^{-9}$.
:::
:::

:::aufgabe Aufgabe 44 ★★★ Binomial und normal
<span class="anker" id="aufg-44"></span>

Eine faire Münze wird $100$-mal geworfen, $X$ ist die Anzahl der Köpfe.

<ol class="al">

<li>

Gib Erwartungswert und Standardabweichung von $X$ an.

</li>

<li>

Nähere $P(X\le40)$ mit dem zentralen Grenzwertsatz. Benutze als Grenze $40{,}5$ statt $40$ und begründe, warum das bei einer ganzzahligen Größe besser ist.

</li>

<li>

Wie wahrscheinlich ist nach der Näherung eine Abweichung um mindestens $15$ von $50$? Was sagt die Tschebyschow-Ungleichung?

</li>

</ol>

:::loesung
(a) $\mathbb{E}[X]=50$, $\sigma=\sqrt{100\cdot\tfrac14}=5$.

(b) $P(X\le40)\approx\Phi\bigl((40{,}5-50)/5\bigr)=\Phi(-1{,}9)\approx0{,}0287$. Genau ist $P(X\le40)\approx0{,}0284$. $X$ nimmt nur ganze Werte an; der Balken bei $40$ reicht von $39{,}5$ bis $40{,}5$. Mit der Grenze $40$ schnitte man ihn halb ab und erhielte $\Phi(-2)\approx0{,}0228$, deutlich zu wenig.

(c) $P(X\le35)+P(X\ge65)\approx2\,\Phi\bigl((35{,}5-50)/5\bigr)=2\,\Phi(-2{,}9)\approx0{,}0037$; genau sind es etwa $0{,}0035$. Die Tschebyschow-Ungleichung gibt nur $P(|X-50|\ge15)\le25/225\approx0{,}11$, dreißigmal mehr.
:::
:::

---
title: Punktweise und gleichmäßige Konvergenz
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Konvergenz von Funktionenfolgen
order: 3060100
summary: Von Grund auf – bei Funktionenfolgen $f_n$ gibt es mehr als einen Konvergenzbegriff. Punktweise Konvergenz fordert $f_n(x)\to f(x)$ für jedes feste $x$; gleichmäßige Konvergenz verlangt $\sup_x|f_n(x)-f(x)|\to0$ – ein gemeinsames Tempo für alle $x$. Gleichmäßig impliziert punktweise, aber nicht umgekehrt (Gegenbeispiel $x^n$). Das Cauchy-Kriterium charakterisiert gleichmäßige Konvergenz ohne Kenntnis der Grenzfunktion.
tags: Funktionenfolge, punktweise Konvergenz, gleichmäßige Konvergenz, Supremumsnorm, Cauchy-Kriterium, Grenzfunktion
---

:::grafik
Einstiegs-Animation: Eine Funktionenfolge $f_n$ (dünne Kurven) nähert sich einer Grenzfunktion $f$ (dicke Kurve). Zwei
Modi im Vergleich: Links **punktweise** — an jeder einzelnen Stelle $x$ kriecht $f_n(x)$ irgendwann an $f(x)$ heran,
aber an verschiedenen Stellen **unterschiedlich schnell**; es gibt immer noch eine „Beule", die nur wandert. Rechts
**gleichmäßig** — um die Grenzfunktion wird ein $\varepsilon$-Schlauch gelegt, und ab einem Index $N$ liegt die
**ganze** Kurve $f_n$ darin. Kernbotschaft: Punktweise = jede Stelle für sich; gleichmäßig = alle Stellen im
Gleichschritt.
:::

:::konzept
Bei Zahlenfolgen $(a_n)$ gibt es nur **einen** Konvergenzbegriff. Bei __Funktionenfolgen__ $(f_n)$ ist das anders: Eine
Folge von Funktionen kann auf **verschiedene Weisen** gegen eine Grenzfunktion streben, und man muss immer dazusagen,
in **welchem Sinne**. Der schwächste nützliche Begriff ist __punktweise__ (jede Stelle konvergiert für sich), der
entscheidende ist __gleichmäßig__ (alle Stellen konvergieren „im Gleichschritt"). Der Unterschied ist nicht
Haarspalterei: Nur die gleichmäßige Konvergenz erlaubt es später, Grenzwert mit Stetigkeit, Integration und
Differentiation zu **vertauschen** — die Grundlage für Potenz- und Fourier-Reihen.
:::

**Worum es geht:** Wir definieren __punktweise__ und __gleichmäßige__ Konvergenz, sehen am Standardbeispiel $x^n$,
dass sie verschieden sind, und lernen das __Cauchy-Kriterium__ für gleichmäßige Konvergenz.

## Die zwei Konvergenzbegriffe

Wir betrachten Folgen $(f_n)_{n\in\mathbb{N}}$ beschränkter Funktionen $f_n:[a,b]\to\mathbb{R}$ (oder $\mathbb{C}$) und
eine beschränkte Grenzfunktion $f$ (Definition 6.1).

**Punktweise Konvergenz.** $f_n$ konvergiert für $n\to\infty$ __punktweise__ gegen $f$, wenn

$$\lim_{n\to\infty}f_n(x)=f(x)\quad\forall x\in[a,b], \qquad\text{gleichbedeutend}\qquad \lim_{n\to\infty}|f_n(x)-f(x)|=0\quad\forall x\in[a,b].$$

Entscheidend: Das „$\forall x$" steht **außen**. Für jedes $x$ darf die Folge in ihrem eigenen Tempo konvergieren — der
Index $N$, ab dem $|f_n(x)-f(x)|<\varepsilon$ gilt, darf von $x$ abhängen.

**Gleichmäßige Konvergenz.** $f_n$ konvergiert __gleichmäßig__ gegen $f$, wenn

$$\lim_{n\to\infty}\ \sup_{x\in[a,b]}|f_n(x)-f(x)|=0.$$

Hier wird zuerst über **alle** $x$ das Supremum gebildet — der größte Abstand irgendwo — und erst dieser soll gegen
null gehen. Das verlangt **ein gemeinsames** $N$, das für alle $x$ zugleich funktioniert. Mit der __Supremumsnorm__
$\|g\|_\infty:=\sup_{x\in[a,b]}|g(x)|$ schreibt sich das kompakt als $\|f_n-f\|_\infty\to0$.

Offensichtlich gilt: **Gleichmäßige Konvergenz impliziert punktweise Konvergenz** (ist das Supremum klein, ist jeder
einzelne Abstand klein) — aber **nicht umgekehrt**.

## Warum die Umkehrung scheitert: das Beispiel $x^n$

Betrachte auf $[0,1]$ die Folge $f_n(x)=x^n$ (Beispiel 6.2). Punktweise ist

$$\lim_{n\to\infty}x^n=\begin{cases}0, & 0\le x<1,\\ 1, & x=1,\end{cases}$$

also konvergiert $f_n$ punktweise gegen die Funktion $f$, die auf $[0,1)$ null ist und bei $x=1$ den Wert $1$ hat.
Diese Grenzfunktion ist **unstetig** — obwohl alle $f_n$ stetig sind! Gleichmäßig ist die Konvergenz **nicht**: Für
jedes $n$ ist $\sup_{x\in[0,1]}|x^n-f(x)|=1$ (nahe $x=1$ bleibt $x^n$ dicht bei $1$, während $f=0$ ist), und $1\not\to
0$. Anschaulich: Die „Beule" an der Stelle $1$ wird nie flacher, sie rutscht nur immer näher an den Rand. Genau solche
wandernden Beulen verbietet die gleichmäßige Konvergenz.

**Eigenes Gegenbeispiel (umgekehrter Fall).** Die Folge $f_n(x)=\frac{\sin(nx)}{n}$ auf $\mathbb{R}$ konvergiert
**gleichmäßig** gegen $0$, denn $\sup_x\big|\frac{\sin(nx)}{n}\big|=\frac1n\to0$ — obwohl die Ableitungen $f_n'(x)=
\cos(nx)$ wild oszillieren und **nicht** konvergieren. Gleichmäßige Konvergenz der Funktionen sagt also nichts über die
Ableitungen (dazu später Satz 6.8).

:::grafik
Links $f_n(x)=x^n$ auf $[0,1]$: die Kurvenschar wird zum Rand hin immer steiler, die Grenzfunktion springt bei $x=1$
von $0$ auf $1$ (unstetig); der maximale Abstand bleibt $1$. Rechts $f_n(x)=\sin(nx)/n$: eine immer flachere
Oszillation, komplett in einem $\varepsilon$-Schlauch um $0$ — gleichmäßige Konvergenz.
:::

## Das Cauchy-Kriterium

Oft will man gleichmäßige Konvergenz nachweisen, **ohne die Grenzfunktion zu kennen**. Das leistet — wie bei
Zahlenfolgen — ein Cauchy-Kriterium (Lemma 6.3): Eine Folge $(f_n)$ konvergiert genau dann gleichmäßig, wenn

$$\sup_{x\in[a,b]}|f_m(x)-f_n(x)|\longrightarrow 0 \qquad\text{für } m,n\to\infty.$$

*Warum?* Die **Notwendigkeit** folgt aus der Dreiecksungleichung $|f_m(x)-f_n(x)|\le|f_m(x)-f(x)|+|f_n(x)-f(x)|$ —
sind beide Summanden gleichmäßig klein, auch die linke Seite. Für die **Umkehrung** liefert das Cauchy-Kriterium für
Zahlenfolgen zunächst die punktweise Konvergenz gegen eine Grenzfunktion $f(x):=\lim_n f_n(x)$. Nach Voraussetzung gibt
es zu jedem $\varepsilon>0$ ein $N(\varepsilon)$ mit $|f_m(x)-f_n(x)|<\varepsilon$ für alle $m\ge n\ge N(\varepsilon)$
und alle $x$. Lässt man $m\to\infty$ laufen, folgt

$$|f(x)-f_n(x)|=\lim_{m\to\infty}|f_m(x)-f_n(x)|\le\varepsilon \qquad\text{für alle } n\ge N(\varepsilon),\ x\in[a,b],$$

und das ist gerade die gleichmäßige Konvergenz gegen $f$.

**Stolperstein:** (1) Der Unterschied steckt allein in der **Reihenfolge der Quantoren**: punktweise „$\forall x\,
\exists N$", gleichmäßig „$\exists N\,\forall x$" — bei gleichmäßiger Konvergenz **ein** $N$ für alle Stellen. (2)
Punktweise Grenzfunktionen stetiger Funktionen können **unstetig** sein ($x^n$); gleichmäßige Grenzfunktionen nicht
(Satz 6.4). (3) Gleichmäßige Konvergenz der $f_n$ erzwingt **nicht** die Konvergenz der Ableitungen $f_n'$.

:::kern
Für beschränkte $f_n,f:[a,b]\to\mathbb{R}$ (oder $\mathbb{C}$): __punktweise__ $\lim_n f_n(x)=f(x)\ \forall x$ (jedes
$x$ eigenes Tempo, $N=N(x)$); __gleichmäßig__ $\sup_{x\in[a,b]}|f_n(x)-f(x)|=\|f_n-f\|_\infty\to0$ (ein gemeinsames
$N$ für alle $x$). __Gleichmäßig ⇒ punktweise__, nicht umgekehrt: $f_n(x)=x^n$ auf $[0,1]$ konvergiert punktweise gegen
eine **unstetige** Grenzfunktion ($0$ auf $[0,1)$, $1$ bei $x{=}1$), aber $\sup|x^n-f|=1\not\to0$ — nicht gleichmäßig.
__Cauchy-Kriterium__ (Lemma 6.3): $(f_n)$ gleichmäßig konvergent $\Leftrightarrow\sup_x|f_m(x)-f_n(x)|\to0$ für
$m,n\to\infty$ — Nachweis **ohne** Kenntnis der Grenzfunktion. Quantoren-Merksatz: punktweise $\forall x\,\exists N$,
gleichmäßig $\exists N\,\forall x$.
:::

Warum gleichmäßige Konvergenz so viel stärker ist, zeigt der nächste Artikel: Nur sie erlaubt die __Vertauschung von
Grenzprozessen__ — der gleichmäßige Limes stetiger Funktionen ist stetig, und Grenzwert und Integral (bzw. Ableitung)
dürfen vertauscht werden.

:::quiz
F: Warum braucht man bei Funktionenfolgen überhaupt mehr als einen Konvergenzbegriff, bei Zahlenfolgen aber nicht?
A: Eine Zahlenfolge strebt einfach gegen eine Zahl. Eine Funktionenfolge hat unendlich viele Stellen, an denen sie zugleich konvergieren soll — und die Qualität dieses Zusammenspiels (jede Stelle für sich oder alle im Gleichschritt) macht den Unterschied, der später über Stetigkeit und Vertauschbarkeit entscheidet.
F: Worin liegt der genaue Unterschied zwischen punktweiser und gleichmäßiger Konvergenz?
A: Er steckt in der Reihenfolge der Quantoren: punktweise heißt „zu jedem $x$ gibt es ein $N$" ($\forall x\,\exists N$), das $N$ darf von $x$ abhängen. Gleichmäßig heißt „es gibt ein $N$ für alle $x$" ($\exists N\,\forall x$) — ein gemeinsames Tempo.
F: Was bedeutet die Supremumsnorm $\|f_n-f\|_\infty\to0$ anschaulich?
A: Man misst den größten Abstand zwischen $f_n$ und $f$ irgendwo im Intervall. Geht dieser größte Abstand gegen null, liegt die ganze Kurve $f_n$ ab einem Index in einem beliebig dünnen $\varepsilon$-Schlauch um $f$ — das ist gleichmäßige Konvergenz.
F: Warum impliziert gleichmäßige Konvergenz die punktweise, aber nicht umgekehrt?
A: Ist das Supremum aller Abstände klein, ist erst recht jeder einzelne Abstand klein — also folgt punktweise aus gleichmäßig. Umgekehrt können die einzelnen Stellen konvergieren, während das Supremum (eine wandernde Beule) nie kleiner wird.
F: Warum konvergiert $f_n(x)=x^n$ auf $[0,1]$ punktweise, aber nicht gleichmäßig?
A: Für $x<1$ geht $x^n\to0$, bei $x=1$ bleibt es $1$ — punktweise Grenzfunktion existiert. Aber $\sup_{x}|x^n-f(x)|=1$ für jedes $n$ (nahe $x=1$ ist $x^n$ fast $1$, während $f=0$), das Supremum geht nie gegen null.
F: Was lehrt das Beispiel $x^n$ über Stetigkeit von Grenzfunktionen?
A: Alle $f_n=x^n$ sind stetig, ihre punktweise Grenzfunktion springt aber bei $x=1$ von $0$ auf $1$ — ist also unstetig. Punktweise Konvergenz kann die Stetigkeit zerstören; gleichmäßige nicht.
F: Was ist die „wandernde Beule", und warum verbietet gleichmäßige Konvergenz sie?
A: Bei $x^n$ bleibt nahe $x=1$ stets ein Bereich, wo $f_n$ fast $1$ ist, obwohl die Grenzfunktion dort $0$ ist; diese Beule flacht nicht ab, sie rutscht nur zum Rand. Gleichmäßige Konvergenz verlangt, dass der maximale Abstand überall gegen null geht — eine bleibende Beule ist damit ausgeschlossen.
F: Warum zeigt $f_n(x)=\sin(nx)/n$, dass gleichmäßige Konvergenz nichts über die Ableitungen aussagt?
A: $\sup_x|\sin(nx)/n|=1/n\to0$, also konvergiert $f_n$ gleichmäßig gegen $0$. Die Ableitungen $f_n'=\cos(nx)$ oszillieren aber wild und konvergieren überhaupt nicht — Konvergenz der Funktionen überträgt sich nicht auf die Ableitungen.
F: Welchen Vorteil bietet das Cauchy-Kriterium gegenüber der Definition der gleichmäßigen Konvergenz?
A: Man kann gleichmäßige Konvergenz nachweisen, ohne die Grenzfunktion zu kennen: Es genügt zu zeigen, dass $\sup_x|f_m(x)-f_n(x)|\to0$ für $m,n\to\infty$. Das ist oft prüfbar, wenn man die Grenzfunktion gar nicht explizit hat.
F: Wie gewinnt man aus dem Cauchy-Kriterium die gleichmäßige Konvergenz gegen eine konkrete Grenzfunktion?
A: Aus dem Cauchy-Kriterium für jedes feste $x$ folgt zunächst punktweise Konvergenz gegen $f(x):=\lim_n f_n(x)$. Lässt man dann in $|f_m(x)-f_n(x)|<\varepsilon$ den Index $m\to\infty$ laufen, erhält man $|f(x)-f_n(x)|\le\varepsilon$ für alle $x$ zugleich — also gleichmäßige Konvergenz.
:::

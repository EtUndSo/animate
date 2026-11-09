---
title: Mehrfachintegrale
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Integralrechnung im Rⁿ
order: 3120400
summary: Eine Funktion von zwei oder mehr Variablen soll über ein Rechteck oder einen Quader integriert werden.
tags: Quader, Volumen, Abschluss, iteriertes Integral, Säulensumme, Mehrfachintegral, Volumenintegral, kompakten Träger
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Eine Funktion von zwei oder mehr Variablen soll über ein Rechteck oder einen Quader integriert werden. Dieser Abschnitt führt das auf Integrale über eine Variable zurück, klärt, ob die Reihenfolge der Variablen eine Rolle spielt, und legt damit fest, was das Integral über einen Quader ist.
:::

### Was du dafür brauchst: Quader

<span class="anker" id="stufe-3-1"></span>

Der einfachste Bereich, über den man in mehreren Variablen integriert, entsteht, wenn jede Variable ihr eigenes Intervall durchläuft.

Für Intervalle $[a_1,b_1],\dots,[a_n,b_n]$ heißt die Menge

$$Q=[a_1,b_1]\times\dots\times[a_n,b_n]=\{\boldsymbol{x}\in\mathbb{R}^n:\ a_j\le x_j\le b_j\ \text{für }j=1,\dots,n\}$$

ein $n$-dimensionaler __Quader__. Für $n=2$ ist das ein Rechteck, für $n=3$ ein Quader im gewohnten Sinn. Die Zahl

$$|Q|=(b_1-a_1)\cdot(b_2-a_2)\cdots(b_n-a_n)$$

heißt das __Volumen__ des Quaders; für $n=2$ ist das der Flächeninhalt, für $n=1$ die Länge. Ein Quader ist abgeschlossen und beschränkt, also kompakt.

::::beispiel
$Q=[0,1]\times[0,2]\times[0,3]$ besteht aus allen Punkten $(x,y,z)$ mit $0\le x\le1$, $0\le y\le2$ und $0\le z\le3$. Sein Volumen ist $|Q|=1\cdot2\cdot3=6$.
::::

⁠**Kurz gesagt:** Ein Quader ist ein Produkt von Intervallen; sein Volumen ist das Produkt der Intervalllängen.

### Was du dafür brauchst: der Abschluss einer Menge

<span class="anker" id="stufe-3-2"></span>

Manche Mengen sind nicht abgeschlossen, weil ihnen Randpunkte fehlen. Fügt man diese hinzu, entsteht eine abgeschlossene Menge.

Die Menge $M$ zusammen mit allen ihren Randpunkten heißt der __Abschluss__ von $M$. Der Abschluss ist immer abgeschlossen, und eine abgeschlossene Menge ist ihr eigener Abschluss.

::::beispiel
Der Abschluss von $(0,1]$ ist $[0,1]$. Der Abschluss der offenen Kreisscheibe $\{|\boldsymbol{x}|<1\}$ ist die Kreisscheibe mit Rand, $\{|\boldsymbol{x}|\le1\}$. Der Abschluss der Menge $\{x\in\mathbb{R}:x\neq0\}$ ist ganz $\mathbb{R}$, denn $0$ ist ihr einziger Randpunkt.
::::

⁠**Kurz gesagt:** Der Abschluss einer Menge ist die Menge mit ihrem Rand.

### Das iterierte Integral

<span class="anker" id="stufe-3-3"></span>

Der Graph einer Funktion $f(x,y)$ über einem Rechteck ist ein Gebirge. Wie groß ist das Volumen unter diesem Gebirge? Zur Verfügung stehen nur Integrale über eine Variable.

Man schneidet das Gebirge in dünne Scheiben, wie einen Brotlaib. Hält man $y$ fest, ist die Scheibe eine Fläche unter der Kurve $x\mapsto f(x,y)$, und ihr Inhalt ist $\int f(x,y)\,\mathrm{d} x$. Summiert man diese Flächen über $y$, entsteht das Volumen (Abb. [9](#abb-9), links).

:::abbildung hm3/k2fubini 9
Dasselbe Gebirge über demselben Rechteck, in zwei Richtungen geschnitten. Links ist $y$ fest; die Scheibe hat die Fläche $\int f\,\mathrm{d} x$. Rechts ist $x$ fest; die Scheibe hat die Fläche $\int f\,\mathrm{d} y$.
:::

:::definition Definition 3.1 (Iteriertes Integral)
<span class="anker" id="satz-3-1"></span>

Sei $Q=[a_1,b_1]\times\dots\times[a_n,b_n]$ ein Quader und $f\colon Q\to\mathbb{R}$ stetig. Der Ausdruck

<span class="anker" id="gl-3-1"></span>
$$\int_{a_n}^{b_n}\Bigl(\cdots\int_{a_2}^{b_2}\Bigl(\int_{a_1}^{b_1}f(x_1,\dots,x_n)\,\mathrm{d} x_1\Bigr)\mathrm{d} x_2\cdots\Bigr)\mathrm{d} x_n \tag{3.1}$$

heißt ein __iteriertes Integral__ von $f$ über $Q$.
:::

⁠**So liest man das:** Man integriert von innen nach außen. Zuerst nach $x_1$, wobei $x_2,\dots,x_n$ als Parameter festgehalten werden; das Ergebnis ist eine Funktion von $x_2,\dots,x_n$. Dann nach $x_2$, und so weiter. Jeder Schritt nimmt eine Variable weg, am Ende bleibt eine Zahl.

⁠**Warum es existiert:** Jedes innere Integral ist eine stetige Funktion der Variablen, die noch übrig sind. Für $n=2$ ist das Satz [1.9](integrale-mit-parameter-uber-endlichen-intervallen.html#satz-1-9): Ist $f\colon[a,b]\times[c,d]\to\mathbb{R}$ stetig, dann ist $F(y)=\int_a^bf(x,y)\,\mathrm{d} x$ stetig auf $[c,d]$, und deshalb existiert $\int_c^dF(y)\,\mathrm{d} y$. Für mehr Variablen überträgt sich der Beweis von Satz [1.7](integrale-mit-parameter-uber-endlichen-intervallen.html#satz-1-7) wörtlich, denn $f$ ist auf dem kompakten Quader gleichmäßig stetig.

::::beispiel
Die *Kuppelfunktion* $f(x,y)=4-x^2-y^2$ auf $Q=[0,1]\times[-1,1]$. Zuerst nach $x$:

$$\int_0^1(4-x^2-y^2)\,\mathrm{d} x=4-\frac13-y^2=\frac{11}3-y^2,\qquad\int_{-1}^1\Bigl(\frac{11}3-y^2\Bigr)\mathrm{d} y=\frac{22}3-\frac23=\frac{20}3 .$$

Zur Plausibilität: Das Rechteck hat den Flächeninhalt $2$, die Höhe liegt zwischen $2$ und $4$, das Volumen also zwischen $4$ und $8$.
::::

⁠**Kurz gesagt:** Ein iteriertes Integral integriert Variable für Variable, von innen nach außen; innen stehen die übrigen Variablen als Parameter.

### Der Satz von Fubini

<span class="anker" id="stufe-3-4"></span>

Man kann das Gebirge auch in der anderen Richtung schneiden: erst bei festem $x$ über $y$ integrieren, dann über $x$. Kommt dasselbe heraus?

Abb. [9](#abb-9) zeigt beide Schnittrichtungen. Es ist dasselbe Gebirge, also sollte dasselbe Volumen herauskommen. Eine Näherung macht das glaubhaft: Man teilt das Rechteck in kleine Rechtecke und stellt auf jedes eine Säule, so hoch wie ein Funktionswert darin. Die Summe der Säulenvolumina heißt hier __Säulensumme__. Sie ist eine endliche Summe, und die darf man Zeile für Zeile oder Spalte für Spalte addieren. Beweisen muss man aber, dass das auch für das Integral gilt.

:::satz Satz 3.2 (Satz von Fubini)
<span class="anker" id="satz-3-2"></span>

Für stetige Funktionen $f\colon[a,b]\times[c,d]\to\mathbb{R}$ gilt

<span class="anker" id="gl-3-2"></span>
$$\int_c^d\Bigl(\int_a^bf(x,y)\,\mathrm{d} x\Bigr)\mathrm{d} y=\int_a^b\Bigl(\int_c^df(x,y)\,\mathrm{d} y\Bigr)\mathrm{d} x . \tag{3.2}$$

Entsprechendes gilt in beliebigen Dimensionen: Für stetiges $f$ auf einem Quader darf man die Variablen in jeder Reihenfolge abarbeiten.
:::

⁠**So liest man das:** Links ist $y$ die äußere Variable, rechts $x$. Das innere Integral behandelt die äußere Variable als Parameter. Die Voraussetzungen sind die Stetigkeit von $f$ und das kompakte Rechteck.

:::beweis Beide Reihenfolgen haben dieselbe Ableitung
⁠**Schritt 1: Hilfsfunktion.** Für $(p,q)\in[a,b]\times[c,d]$ setze

$$w(p,q):=\int_a^p\Bigl(\int_c^qf(x,y)\,\mathrm{d} y\Bigr)\mathrm{d} x-\int_c^q\Bigl(\int_a^pf(x,y)\,\mathrm{d} x\Bigr)\mathrm{d} y .$$

Das sind die beiden Reihenfolgen, mit variablen oberen Grenzen $p$ und $q$. Zu zeigen ist $w(b,d)=0$.

⁠**Schritt 2: Ableiten nach $p$.** Im ersten Term ist $p$ die obere Grenze, und der innere Ausdruck $\int_c^qf(x,y)\,\mathrm{d} y$ ist nach Satz [1.9](integrale-mit-parameter-uber-endlichen-intervallen.html#satz-1-9) stetig in $x$. Der Hauptsatz ergibt als Ableitung $\int_c^qf(p,y)\,\mathrm{d} y$. Im zweiten Term ist $p$ ein Parameter des Integrals über $y$. Sein Integrand ist $J(a,p,y)=\int_a^pf(x,y)\,\mathrm{d} x$ mit $J$ aus der Herleitung der Leibnizregel. Er hat nach dem Hauptsatz die Ableitung $\partial J(a,p,y)/\partial p=f(p,y)$, und die ist stetig in $(p,y)$. Satz [1.9](integrale-mit-parameter-uber-endlichen-intervallen.html#satz-1-9) erlaubt deshalb, unter dem Integral nach $p$ abzuleiten; das ergibt ebenfalls $\int_c^qf(p,y)\,\mathrm{d} y$. Also ist $\partial w/\partial p=0$.

⁠**Schritt 3: Ableiten nach $q$.** Mit vertauschten Rollen von $x$ und $y$ folgt ebenso $\partial w/\partial q=0$.

⁠**Schritt 4: Schluss.** Auf jeder Strecke parallel zu einer Achse ist $w$ eine Funktion einer Variablen mit der Ableitung null, nach dem Mittelwertsatz also konstant. Von $(a,c)$ kommt man über $(a,q)$ nach $(p,q)$ längs zweier solcher Strecken, also ist $w(p,q)=w(a,c)$. Bei $(p,q)=(a,c)$ sind beide Integrale leer, also ist $w(a,c)=0$ und damit $w(b,d)=0$. In höheren Dimensionen vertauscht man auf diese Weise je zwei benachbarte Variablen und hält die übrigen fest.
:::

::::beispiel
Die Kuppelfunktion auf $[0,1]\times[-1,1]$, diesmal zuerst nach $y$:

$$\int_{-1}^1(4-x^2-y^2)\,\mathrm{d} y=8-2x^2-\frac23=\frac{22}3-2x^2,\qquad\int_0^1\Bigl(\frac{22}3-2x^2\Bigr)\mathrm{d} x=\frac{22}3-\frac23=\frac{20}3 .$$

Beide Reihenfolgen ergeben $\frac{20}3$.
::::

⁠**Grenzfall:** Für $f\equiv1$ ergeben beide Reihenfolgen den Flächeninhalt $(b-a)(d-c)$ des Rechtecks.

**Die Reihenfolge wählen.** Weil beide Reihenfolgen dasselbe ergeben, nimmt man die bequemere. Bei $\int_0^2\bigl(\int_0^1y\,\mathrm{e}^{xy}\,\mathrm{d} x\bigr)\mathrm{d} y$ ist innen $\int_0^1y\,\mathrm{e}^{xy}\,\mathrm{d} x=\bigl[\mathrm{e}^{xy}\bigr]_{x=0}^{1}=\mathrm{e}^y-1$; der Faktor $y$ kürzt sich gegen die Stammfunktion. Außen bleibt $\int_0^2(\mathrm{e}^y-1)\,\mathrm{d} y=\mathrm{e}^2-3\approx4{,}39$. In der anderen Reihenfolge bräuchte man innen eine partielle Integration und außen einen Kunstgriff.

:::hintergrund Warum man die Reihenfolge vertauschen darf: eine Summe ist eine Summe
Man teilt das Rechteck in $N\times N$ kleine Rechtecke mit den Seiten $\Delta x=(b-a)/N$ und $\Delta y=(d-c)/N$ und wählt in jedem einen Punkt $(x_j,y_k)$. Über jedem kleinen Rechteck steht eine Säule mit dem Volumen $f(x_j,y_k)\,\Delta x\,\Delta y$. Die Säulensumme

$$V_N=\sum_{k=1}^N\sum_{j=1}^Nf(x_j,y_k)\,\Delta x\,\Delta y$$

ist eine endliche Summe. Man darf sie zeilenweise oder spaltenweise addieren, es kommt dasselbe heraus (Abb. [10](#abb-10)).

:::abbildung hm3/k2riemann 10
Dieselben Säulen über einem in kleine Rechtecke geteilten Rechteck, zweimal addiert. Links Zeile für Zeile: Jede Zeilensumme ist eine Riemann-Summe für $\int f(x,y_k)\,\mathrm{d} x$. Rechts Spalte für Spalte: Jede Spaltensumme ist eine Riemann-Summe für $\int f(x_j,y)\,\mathrm{d} y$. Weil es dieselbe endliche Summe ist, stimmen beide Ergebnisse überein.
:::

Zeilenweise addiert ist $V_N=\sum_k\bigl[\sum_jf(x_j,y_k)\,\Delta x\bigr]\Delta y$. Die eckige Klammer ist eine Riemann-Summe für $F(y_k)=\int_a^bf(x,y_k)\,\mathrm{d} x$. Weil $f$ auf dem kompakten Rechteck gleichmäßig stetig ist, weicht sie für große $N$ um weniger als $\varepsilon\,(b-a)$ von $F(y_k)$ ab, und zwar für alle $k$ zugleich, wie im Hintergrund zu Satz [1.5](integrale-mit-parameter-uber-endlichen-intervallen.html#satz-1-5). Also liegt $V_N$ nahe bei $\sum_kF(y_k)\,\Delta y$, einer Riemann-Summe für $\int_c^dF(y)\,\mathrm{d} y$. Damit strebt $V_N$ gegen das iterierte Integral mit $x$ innen. Spaltenweise addiert strebt dieselbe Zahl $V_N$ gegen das iterierte Integral mit $y$ innen. Eine Folge hat nur einen Grenzwert, also sind beide gleich.

Der Mechanismus ist also: Für endliche Summen ist die Reihenfolge immer egal. Die gleichmäßige Stetigkeit sorgt dafür, dass beim Übergang zum Integral in beiden Richtungen nichts verloren geht. Für die Kuppelfunktion auf $[0,1]\times[-1,1]$ ergibt die Säulensumme mit $N=4$ und den Mittelpunkten der kleinen Rechtecke $\frac{215}{32}\approx6{,}72$, schon nahe bei $\frac{20}3\approx6{,}67$.
:::

:::hintergrund Wann die Reihenfolge doch eine Rolle spielt
Ohne Stetigkeit auf dem ganzen abgeschlossenen Rechteck kann der Satz falsch werden. Für

$$f(x,y)=\frac{x^2-y^2}{(x^2+y^2)^2}\quad\text{auf }(0,1]\times(0,1]$$

ist $f=\partial_y\frac y{x^2+y^2}$, also $\int_0^1f\,\mathrm{d} y=\frac1{1+x^2}$ und $\int_0^1\bigl(\int_0^1f\,\mathrm{d} y\bigr)\mathrm{d} x=\frac\pi4$. Wegen $f(x,y)=-f(y,x)$ ergibt die andere Reihenfolge $-\frac\pi4$.

Der Grund: $f$ ist unterhalb der Diagonalen ($x>y$) positiv, oberhalb negativ, und nahe der Ecke $(0,0)$ unbeschränkt. Schon der positive Teil hat unendliches Volumen: Für festes $x$ ist $\int_0^x\frac{x^2-y^2}{(x^2+y^2)^2}\,\mathrm{d} y=\frac1{2x}$, und $\int_0^1\frac{\mathrm{d} x}{2x}=\infty$. Ebenso hat der negative Teil unendliches Volumen. Beide iterierten Integrale berechnen also „unendlich minus unendlich“, nur in verschiedener Reihenfolge, und jede Reihenfolge lässt einen anderen Rest übrig. Dasselbe kennt man von Doppelsummen: Steht in einem Zahlenschema auf der Diagonalen immer $1$ und direkt rechts daneben immer $-1$, dann ist jede Zeilensumme $0$, die Spaltensummen aber $1,0,0,\dots$ mit der Summe $1$. Die Säulensummen aus dem letzten Kasten konvergieren hier nicht, weil eine einzige Säule nahe der Ecke beliebig groß werden kann.
:::

⁠**Kurz gesagt:** Für stetige Funktionen auf einem kompakten Rechteck oder Quader ist die Integrationsreihenfolge gleichgültig; man wählt die bequemste.

### Das Mehrfachintegral

<span class="anker" id="stufe-3-5"></span>

Nach dem Satz von Fubini liefern alle Reihenfolgen dieselbe Zahl. Sie bekommt deshalb einen eigenen Namen, der keine Reihenfolge mehr nennt.

:::definition Definition 3.3 (Mehrfachintegral)
<span class="anker" id="satz-3-3"></span>

Sei $Q=[a_1,b_1]\times\dots\times[a_n,b_n]$ und $f\colon Q\to\mathbb{R}$ stetig. Das iterierte Integral [(3.1)](#gl-3-1) heißt das __Mehrfachintegral__ von $f$ über $Q$ und wird

$$\int_Qf(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x}$$

geschrieben.
:::

Statt $\mathrm{d}\boldsymbol{x}$ schreibt man auch $\mathrm{d}^n\boldsymbol{x}$, $\mathrm{d} x_1\dots\mathrm{d} x_n$ oder $\mathrm{d}(x_1,\dots,x_n)$. Für $n=3$ heißt das Mehrfachintegral oft __Volumenintegral__, mit den Schreibweisen

$$\iiint_Qf(x,y,z)\,\mathrm{d} x\,\mathrm{d} y\,\mathrm{d} z=\iiint_Qf(x,y,z)\,\mathrm{d} V .$$

::::beispiel
$\int_Q(x+y+z)\,\mathrm{d} V$ über $Q=[0,1]\times[0,2]\times[0,3]$. Innen nach $x$: $\int_0^1(x+y+z)\,\mathrm{d} x=\frac12+y+z$. Dann nach $y$: $\int_0^2\bigl(\frac12+y+z\bigr)\mathrm{d} y=1+2+2z=3+2z$. Außen nach $z$: $\int_0^3(3+2z)\,\mathrm{d} z=9+9=18$.
::::

:::hintergrund Zwei Wege zur selben Zahl: iterierte Integrale und Säulensummen
Viele Lehrbücher erklären das Mehrfachintegral anders: als Grenzwert der Säulensummen $\sum f(\boldsymbol{x}_i)\,|Q_i|$ über immer feinere Zerlegungen des Quaders in kleine Teilquader $Q_i$, so wie im Hintergrund zum Satz von Fubini. Diese Erklärung überträgt die Riemann-Summen aus Unterabschnitt [1.1](integrale-mit-parameter-uber-endlichen-intervallen.html#stufe-1-1) direkt und behandelt alle Variablen gleich. Sie zeigt auch, warum das Integral ein Volumen ist: Es ist die Summe der Säulenvolumina „Höhe mal Grundfläche“. Für stetiges $f$ auf einem kompakten Quader ergeben beide Erklärungen dieselbe Zahl; das ist die Rechnung im Hintergrund zum Satz von Fubini, die sich auf $n$ Variablen überträgt. Die Erklärung über iterierte Integrale hat den Vorteil, dass man das Integral sofort ausrechnen kann. Ihr Preis ist, dass man zeigen muss, dass die Reihenfolge keine Rolle spielt. Genau das leistet der Satz von Fubini.
:::

⁠**Kurz gesagt:** Das Mehrfachintegral über einen Quader ist das iterierte Integral, in welcher Reihenfolge auch immer.

### Linearität und Monotonie

<span class="anker" id="stufe-3-6"></span>

Mit dem Mehrfachintegral rechnet man wie mit dem Integral einer Variablen. Zwei Regeln und eine Abschätzung gehen direkt über.

:::satz Satz 3.4 (Linearität und Monotonie)
<span class="anker" id="satz-3-4"></span>

Für stetige Funktionen $f_1,f_2$ auf dem endlichen Quader $Q$ und Zahlen $\lambda_1,\lambda_2\in\mathbb{R}$ gilt

$$\int_Q(\lambda_1f_1+\lambda_2f_2)\,\mathrm{d}\boldsymbol{x}=\lambda_1\int_Qf_1\,\mathrm{d}\boldsymbol{x}+\lambda_2\int_Qf_2\,\mathrm{d}\boldsymbol{x}$$

und

$$\int_Qf_1\,\mathrm{d}\boldsymbol{x}\le\int_Qf_2\,\mathrm{d}\boldsymbol{x},\quad\text{falls }f_1\le f_2\text{ in }Q .$$

Insbesondere gilt für stetiges $f$ auf $Q$

<span class="anker" id="gl-3-3"></span>
$$\Bigl|\int_Qf(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x}\Bigr|\le|Q|\,\sup_{\boldsymbol{x}\in Q}|f(\boldsymbol{x})| . \tag{3.3}$$
:::

⁠**So liest man das:** Beide Regeln gelten für jedes Integral über eine Variable (Unterabschnitt [1.1](integrale-mit-parameter-uber-endlichen-intervallen.html#stufe-1-1)). Im iterierten Integral wendet man sie Schritt für Schritt an, vom innersten Integral bis zum äußersten. Für [(3.3)](#gl-3-3) sei $S=\sup_Q|f|$; das ist nach dem Satz vom Maximum eine endliche Zahl. Man integriert $-S\le f\le S$ und benutzt $\int_QS\,\mathrm{d}\boldsymbol{x}=S\,|Q|$.

::::beispiel
Für die Kuppelfunktion auf $Q=[0,1]\times[-1,1]$ ist $|Q|=2$. Ihr größter Wert ist $4$, im Punkt $(0,0)$, ihr kleinster $2$, in den Ecken $(1,\pm1)$. Mit der Monotonie folgt $2\cdot2\le\int_Qf\,\mathrm{d}\boldsymbol{x}\le4\cdot2$, also $4\le\frac{20}3\le8$.
::::

⁠**Kurz gesagt:** Das Mehrfachintegral ist linear und monoton, und sein Betrag ist höchstens Volumen mal größter Betrag des Integranden.

### Funktionen mit kompaktem Träger

<span class="anker" id="stufe-3-7"></span>

Manche Funktionen sind nur in einem beschränkten Gebiet von null verschieden. Über den ganzen Raum integriert man sie, ohne uneigentliche Integrale zu brauchen.

Man stellt sich eine Funktion vor, die außerhalb einer großen Kugel überall null ist. Dann trägt alles außerhalb nichts bei, und man kann sich auf einen Quader beschränken, der die Kugel enthält.

:::definition Definition 3.5 (Kompakter Träger)
<span class="anker" id="satz-3-5"></span>

Eine stetige Funktion $f\colon\mathbb{R}^n\to\mathbb{R}$ hat einen __kompakten Träger__, wenn es ein $\rho>0$ gibt mit $f(\boldsymbol{x})=0$ für alle $\boldsymbol{x}\in\mathbb{R}^n$ mit $|\boldsymbol{x}|>\rho$. Für solche $f$ setzt man

$$\int_{\mathbb{R}^n}f(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x}:=\int_Qf(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x}$$

mit einem Quader $Q$, außerhalb dessen $f=0$ ist.
:::

⁠**So liest man das:** Der Name kommt so zustande: Der Abschluss der Menge $\{\boldsymbol{x}:f(\boldsymbol{x})\neq0\}$ heißt der __Träger__ von $f$. Er liegt hier in der Kugel mit dem Radius $\rho$, ist also beschränkt und als Abschluss abgeschlossen, also kompakt. Welchen Quader man nimmt, ist gleichgültig: Ein größerer Quader fügt nur Stücke hinzu, auf denen $f=0$ ist, und in jedem inneren Integral tragen diese Stücke null bei.

::::beispiel
Die Pyramide $f(x,y)=\max(0,\,1-|x|-|y|)$. Für $|(x,y)|>1$ ist $|x|+|y|\ge|(x,y)|>1$, also $f=0$; sie hat einen kompakten Träger mit $\rho=1$. Ihr Träger ist das Quadrat $\{|x|+|y|\le1\}$, dessen Ecken auf den Achsen liegen. Mit $Q=[-1,1]^2$ ist für festes $y$ das innere Integral die Fläche eines Dreiecks mit der Grundseite $2(1-|y|)$ und der Höhe $1-|y|$:

$$\int_{-1}^1f(x,y)\,\mathrm{d} x=(1-|y|)^2,\qquad\int_{\mathbb{R}^2}f\,\mathrm{d}\boldsymbol{x}=\int_{-1}^1(1-|y|)^2\,\mathrm{d} y=\frac23 .$$

Zur Kontrolle: Eine Pyramide mit der Grundfläche $2$ und der Höhe $1$ hat das Volumen $\frac13\cdot2\cdot1=\frac23$.
::::

⁠**Kurz gesagt:** Eine Funktion mit kompaktem Träger verschwindet außerhalb einer Kugel; ihr Integral über den ganzen Raum ist das Integral über einen genügend großen Quader.

### Über stetige Funktionen hinaus: das Lebesgue-Integral

<span class="anker" id="stufe-3-8"></span>

Bisher sind alle Integranden stetig. Viele natürliche Integranden sind es nicht, etwa eine Funktion, die innerhalb eines Körpers einen Wert hat und außerhalb null ist.

Es liegt nahe, den Integralbegriff auf Funktionen zu erweitern, die in einem geeigneten Sinn Grenzwerte stetiger Funktionen mit kompaktem Träger sind. Der passende Rahmen dafür ist das __Lebesgue-Integral__. Seine Theorie wird in diesem Kapitel nicht entwickelt; wo ein Ergebnis von ihr gebraucht wird, wird es an dieser Stelle genannt.

:::hintergrund Warum das Riemann-Integral dafür nicht reicht
Das Integral aus Riemann-Summen verträgt Grenzwerte schlecht. Man zählt die rationalen Zahlen in $[0,1]$ der Reihe nach ab und setzt $u_N(t)=1$ an den ersten $N$ von ihnen und $u_N(t)=0$ sonst. Jedes $u_N$ weicht nur an endlich vielen Stellen von null ab und hat das Integral $0$. Für $N\to\infty$ strebt $u_N$ an jeder Stelle gegen die Funktion, die auf den rationalen Zahlen $1$ und sonst $0$ ist. Deren Riemann-Summen sind aber $1$, wenn man rationale Stellen $t_k$ wählt, und $0$ bei irrationalen; sie haben keinen gemeinsamen Grenzwert. Die Grenzfunktion hat also kein Integral im Sinn der Riemann-Summen, obwohl alle $u_N$ das Integral $0$ haben. Das Lebesgue-Integral ordnet ihr den Wert $0$ zu und erlaubt viel allgemeiner, Grenzwert und Integral zu vertauschen, wenn eine Majorante existiert.
:::

⁠**Kurz gesagt:** Für Integranden, die keine stetigen Funktionen sind, ist das Lebesgue-Integral der passende Rahmen.

### Aufgaben

<span class="anker" id="stufe-3-9"></span>

:::aufgabe Aufgabe 9 ★★ Die günstige Reihenfolge
<span class="anker" id="aufg-9"></span>

<ol class="al">

<li>

Berechne $\int_0^1\int_0^1\frac y{1+xy}\,\mathrm{d} x\,\mathrm{d} y$. Welche Reihenfolge ist bequemer?

</li>

<li>

Berechne $\int_0^1\frac{t^3-t}{\ln t}\,\mathrm{d} t$. Tipp: Für $0<t<1$ ist $\frac{t^3-t}{\ln t}=\int_1^3t^y\,\mathrm{d} y$.

</li>

</ol>

:::loesung
(a) Der Integrand ist auf $[0,1]^2$ stetig, die Reihenfolge ist also frei. Zuerst nach $x$: $\int_0^1\frac y{1+xy}\,\mathrm{d} x=\bigl[\ln(1+xy)\bigr]_{x=0}^1=\ln(1+y)$, denn der Faktor $y$ ist die innere Ableitung. Dann $\int_0^1\ln(1+y)\,\mathrm{d} y=\bigl[(1+y)\ln(1+y)-y\bigr]_0^1=2\ln2-1\approx0{,}386$. Zuerst nach $y$ wäre eine Partialbruchzerlegung nötig, und das äußere Integral würde unbequem.

(b) Für $0<t<1$ ist $\int_1^3t^y\,\mathrm{d} y=\bigl[\frac{t^y}{\ln t}\bigr]_{y=1}^{3}=\frac{t^3-t}{\ln t}$. Die Funktion $(t,y)\mapsto t^y$ ist auf $[0,1]\times[1,3]$ stetig, auch bei $t=0$, wo sie wegen $y\ge1$ gegen $0$ geht. Nach dem Satz von Fubini ist also

$$\int_0^1\frac{t^3-t}{\ln t}\,\mathrm{d} t=\int_0^1\Bigl(\int_1^3t^y\,\mathrm{d} y\Bigr)\mathrm{d} t=\int_1^3\Bigl(\int_0^1t^y\,\mathrm{d} t\Bigr)\mathrm{d} y=\int_1^3\frac{\mathrm{d} y}{1+y}=\ln\frac42=\ln2 .$$

Derselbe Wert ergibt sich durch Ableiten unter dem Integral: $I(y)=\int_0^1\frac{t^y-t}{\ln t}\,\mathrm{d} t$ hat $I'(y)=\int_0^1t^y\,\mathrm{d} t=\frac1{y+1}$ und $I(1)=0$, also $I(3)=\ln4-\ln2=\ln2$.
:::
:::

:::aufgabe Aufgabe 10 ★★ Wenn das Rechteck unendlich lang ist
<span class="anker" id="aufg-10"></span>

Sei $f(x,y)=(3-xy)(xy)^2\,\mathrm{e}^{-xy}$ auf $[0,1]\times[0,\infty)$.

<ol class="al">

<li>

Zeige $f=\partial_x\bigl(x^3y^2\mathrm{e}^{-xy}\bigr)=\partial_y\bigl(x^2y^3\mathrm{e}^{-xy}\bigr)$.

</li>

<li>

Berechne $\int_0^\infty\bigl(\int_0^1f\,\mathrm{d} x\bigr)\mathrm{d} y$ und $\int_0^1\bigl(\int_0^\infty f\,\mathrm{d} y\bigr)\mathrm{d} x$.

</li>

<li>

Warum widerspricht das Ergebnis nicht dem Satz von Fubini? Welcher Fluchtweg aus Abb. [7](uneigentliche-parameterintegrale.html#abb-7) liegt hier vor?

</li>

</ol>

:::loesung
(a) $\partial_x\bigl(x^3y^2\mathrm{e}^{-xy}\bigr)=3x^2y^2\mathrm{e}^{-xy}-x^3y^3\mathrm{e}^{-xy}$ und $\partial_y\bigl(x^2y^3\mathrm{e}^{-xy}\bigr)=3x^2y^2\mathrm{e}^{-xy}-x^3y^3\mathrm{e}^{-xy}$. Beides ist $(3-xy)(xy)^2\mathrm{e}^{-xy}=f$.

(b) Erste Reihenfolge: $\int_0^1f\,\mathrm{d} x=\bigl[x^3y^2\mathrm{e}^{-xy}\bigr]_{x=0}^1=y^2\mathrm{e}^{-y}$ und $\int_0^\infty y^2\mathrm{e}^{-y}\,\mathrm{d} y=\Gamma(3)=2$. Zweite Reihenfolge: Für $x>0$ ist $\int_0^\infty f\,\mathrm{d} y=\bigl[x^2y^3\mathrm{e}^{-xy}\bigr]_{y=0}^\infty=0$, und für $x=0$ ist $f=0$. Die zweite Reihenfolge ergibt also $0$.

(c) Der Satz von Fubini verlangt ein kompaktes Rechteck; hier ist der $y$-Bereich unbeschränkt. Mit $s=xy$ ist $f=(3-s)s^2\mathrm{e}^{-s}$: Für festes $x$ sitzt der positive Teil von $f$ bei $y<3/x$ und der negative bei $y>3/x$, beide mit einer Fläche proportional zu $1/x$. Für $x\to0$ wandern sie nach rechts und werden größer. Das ist der Fluchtweg „nach rechts“ aus Abb. [7](uneigentliche-parameterintegrale.html#abb-7), und $\int_0^1\int_0^\infty|f|\,\mathrm{d} y\,\mathrm{d} x$ ist unendlich.
:::
:::

:::aufgabe Aufgabe 11 ★★ Zwei Reihenfolgen, zwei Ergebnisse
<span class="anker" id="aufg-11"></span>

Sei $f(x,y)=\dfrac{x^2-y^2}{(x^2+y^2)^2}$ auf $(0,1]\times(0,2]$.

<ol class="al">

<li>

Berechne $\int_0^1\bigl(\int_0^2f\,\mathrm{d} y\bigr)\mathrm{d} x$ und $\int_0^2\bigl(\int_0^1f\,\mathrm{d} x\bigr)\mathrm{d} y$. Tipp: $f=\partial_y\frac y{x^2+y^2}=-\partial_x\frac x{x^2+y^2}$.

</li>

<li>

Zeige, dass die beiden Ergebnisse verschieden sind, und erkläre, warum das dem Satz von Fubini nicht widerspricht.

</li>

</ol>

:::loesung
(a) Mit $f=\partial_y\frac y{x^2+y^2}$ ist $\int_0^2f\,\mathrm{d} y=\frac2{x^2+4}$ für $x>0$ und

$$\int_0^1\frac{2\,\mathrm{d} x}{x^2+4}=\Bigl[\arctan\frac x2\Bigr]_0^1=\arctan\frac12\approx0{,}464 .$$

Mit $f=-\partial_x\frac x{x^2+y^2}$ ist $\int_0^1f\,\mathrm{d} x=-\frac1{1+y^2}$ für $y>0$ und

$$\int_0^2\Bigl(-\frac1{1+y^2}\Bigr)\mathrm{d} y=-\arctan2\approx-1{,}107 .$$

(b) Das eine Ergebnis ist positiv, das andere negativ; wegen $\arctan\frac12+\arctan2=\frac\pi2$ unterscheiden sie sich um $\frac\pi2$. Kein Widerspruch: Der Satz von Fubini verlangt eine stetige Funktion auf dem abgeschlossenen Rechteck $[0,1]\times[0,2]$. Diese Funktion lässt sich in der Ecke $(0,0)$ nicht stetig ergänzen, sie ist dort nicht einmal beschränkt. Wie im Hintergrund zum Satz von Fubini haben positiver und negativer Teil beide unendliches Volumen, und jede Reihenfolge rechnet „unendlich minus unendlich“ anders aus.
:::
:::

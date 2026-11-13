---
title: Stufe 4: Verknüpfen und Umkehren
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Funktionen und Polynome
adresse: elektrotechnik/1-semester/hohere-mathematik-1/funktionen-und-polynome
knoten: Kapitel 3: Funktionen und Polynome
order: 1230600
summary: Stufe 3 sagt, wann f(x)=y genau eine Lösung hat.
tags: Summe, Differenz, Produkt, Quotient, Komposition, n-te Wurzel
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Stufe [3](ruckwarts-injektiv-surjektiv-bijektiv.html#stufe-3) sagt, wann $f(x)=y$ genau eine Lösung hat. Diese Stufe macht aus der Lösung eine Funktion. Dazu muss man Funktionen hintereinander ausführen können.
:::

**Die Idee.** Die Umkehrfunktion macht rückgängig, was $f$ tut: Erst $f$, dann $g$ führt zurück zum Anfang, und erst $g$, dann $f$ ebenso (Abb. [5](#abb-5), links). Aus Funktionen entstehen so neue Funktionen, wie aus Zahlen durch Rechnen neue Zahlen.

:::definition Definition 4.1 (Verknüpfungen)
<span class="anker" id="satz-4-1"></span>

Für reelle Funktionen $f,g$ sei $M:=\mathcal D(f)\cap\mathcal D(g)$ und $M':=\{x\in M:g(x)\neq0\}$. Dann sind __Summe__, __Differenz__ und __Produkt__ auf $M$ und der __Quotient__ auf $M'$ erklärt durch

<span class="anker" id="gl-4-1"></span>
$$(f\pm g)(x):=f(x)\pm g(x),\qquad(f\cdot g)(x):=f(x)\cdot g(x),\qquad\Bigl(\frac fg\Bigr)(x):=\frac{f(x)}{g(x)}. \tag{4.1}$$

Für $f:A\to B$ und $g:B\to C$ ist die __Komposition__ oder Hintereinanderausführung $g\circ f:A\to C$ erklärt durch

<span class="anker" id="gl-4-2"></span>
$$(g\circ f)(x):=g\bigl(f(x)\bigr)\quad\text{für alle }x\in A. \tag{4.2}$$
:::

⁠**So liest man das:** $g\circ f$ spricht man „$g$ nach $f$“: $f$ wirkt zuerst, $f(x)$ liegt in $B$, dort darf $g$ wirken. Der Graph ist $\{(x,y)\in A\times C:\text{es gibt }z\in B\text{ mit }f(x)=z,\ g(z)=y\}$. Die Reihenfolge zählt: Für $f(x)=2x$, $g(x)=x+1$ ist $(g\circ f)(1)=3$, aber $(f\circ g)(1)=4$. Summe und Produkt rechnet man Stelle für Stelle aus, etwa $(h/b)(2)=-1/0{,}2=-5$.

:::satz Satz 4.2 (Charakterisierung von injektiv, surjektiv, bijektiv)
<span class="anker" id="satz-4-2"></span>

Sei $f:A\to B$ eine Funktion, $A$ nicht leer. Dann gilt:

<ol class="rm">

<li>

$f$ injektiv $\Leftrightarrow$ es gibt $g:B\to A$ mit $(g\circ f)(x)=x$ für alle $x\in A$ (I).

</li>

<li>

$f$ surjektiv $\Leftrightarrow$ es gibt $g:B\to A$ mit $(f\circ g)(y)=y$ für alle $y\in B$ (S).

</li>

<li>

$f$ bijektiv $\Leftrightarrow$ es gibt genau eine Funktion $g:B\to A$ mit (I) und (S).

</li>

</ol>
:::

:::beweis Charakterisierung
(i) „$\Leftarrow$“: Aus $f(x_1)=f(x_2)$ folgt $x_1=g(f(x_1))=g(f(x_2))=x_2$. „$\Rightarrow$“ als Idee: $g$ gibt jedem $y\in\mathcal W(f)$ sein einziges Urbild und allen anderen $y$ einen festen Wert aus $A$.

(ii) „$\Leftarrow$“: Zu $y\in B$ setze $z:=g(y)\in A$, dann ist $f(z)=(f\circ g)(y)=y$, also $y\in\mathcal W(f)$. „$\Rightarrow$“ als Idee: $g$ wählt zu jedem $y$ eines seiner Urbilder.

(iii) „$\Leftarrow$“: (I) ergibt injektiv, (S) ergibt surjektiv. „$\Rightarrow$“: Bijektiv heißt, jedes $y$ hat genau ein Urbild $g(y)$, dieses $g$ erfüllt (I) und (S). Erfüllt auch $\hat g$ beide, ist $\hat g(y)=\hat g\bigl(f(g(y))\bigr)=g(y)$ nach (S) für $g$ und (I) für $\hat g$.
:::

⁠**So liest man das:** Merkhilfe: Bei „surjektiv“ geht es um die Bilder, also steht (S) für alle $y\in B$. **Warum „bijektiv“ für die Eindeutigkeit nötig ist:** $h:\mathbb{R}\to[-1,\infty)$ ist nur surjektiv, und sowohl $g_1(y)=2+\sqrt{y+1}$ als auch $g_2(y)=2-\sqrt{y+1}$ erfüllen (S). $h:[2,\infty)\to\mathbb{R}$ ist nur injektiv, und $g(y)=2+\sqrt{y+1}$ für $y\ge-1$, $g(y)=c$ für $y<-1$ erfüllt (I) für jedes feste $c\ge2$.

:::definition Definition 4.3 (Umkehrfunktion und Wurzel)
<span class="anker" id="satz-4-3"></span>

Die Funktion $g$ aus Satz [4.2](#satz-4-2)(iii) heißt Umkehrfunktion von $f$, geschrieben $f^{-1}:=g$. Für alle $x\in A$, $y\in B$ gilt

<span class="anker" id="gl-4-3"></span>
$$f(x)=y\ \Leftrightarrow\ x=f^{-1}(y),\qquad f^{-1}\bigl(f(x)\bigr)=x,\qquad f\bigl(f^{-1}(y)\bigr)=y. \tag{4.3}$$

Die Umkehrfunktion von $x\mapsto x^n$ (auf $\mathbb{R}_0^+$ für gerades $n$, auf $\mathbb{R}$ für ungerades $n$) heißt __$n$-te Wurzel__, $f^{-1}(y)=\sqrt[n]{y}=y^{1/n}$.
:::

⁠**So liest man das:** Die erste Aussage sagt: $f^{-1}$ löst die Gleichung $f(x)=y$. Beweis: Aus $f(x)=y$ folgt $x=g(f(x))=g(y)$ nach (I), aus $g(y)=x$ folgt $y=f(g(y))=f(x)$ nach (S). Für die Wurzel lauten die beiden anderen Aussagen $\sqrt[n]{y^n}=y$ und $(\sqrt[n]{y})^n=y$. **Achtung:** $f^{-1}(y)$ ist nicht $1/f(y)$. Für $h$ auf $[2,\infty)$ ist $h^{-1}(8)=5$, aber $1/h(8)=1/35$.

**Der Graph.** Wegen [(4.3)](#gl-4-3) ist $\mathcal G(f)=\{(x,f(x))\}=\{(g(y),y):y\in B\}$, während $\mathcal G(g)=\{(y,g(y)):y\in B\}$ ist. Die Paare sind vertauscht, und Vertauschen der Koordinaten ist die Spiegelung an der Winkelhalbierenden $\{(x,y)\in\mathbb{R}^2:x=y\}$ (Abb. [5](#abb-5), rechts).

:::abbildung hm1/k3spiegel 5
Links der Hin- und Rückweg für $h$ auf $[2,\infty)$: $h(5)=8$ und $h^{-1}(8)=5$. Rechts die Graphen von $h$ und $h^{-1}(y)=2+\sqrt{y+1}$: Der Punkt $(4\,|\,3)$ geht durch Spiegeln an der gestrichelten Geraden in $(3\,|\,4)$ über.
:::

:::satz Satz 4.4 (Monotonie vererbt sich)
<span class="anker" id="satz-4-4"></span>

Sei $f:A\to B$ reell, surjektiv und streng monoton wachsend (fallend). Dann existiert $g=f^{-1}:B\to A$ und ist ebenfalls streng monoton wachsend (fallend).
:::

:::beweis Monotonie vererbt sich
Für wachsendes $f$ (fallend geht gleich): $f$ ist injektiv wie in Satz [3.2](ruckwarts-injektiv-surjektiv-bijektiv.html#satz-3-2) und surjektiv, also existiert $g$. Sei $y_1<y_2$. Wäre $g(y_1)\ge g(y_2)$, ergäbe Anwenden von $f$ den Widerspruch $y_1\ge y_2$. Also $g(y_1)<g(y_2)$.
:::

⁠**So liest man das und warum die Voraussetzungen nötig sind:** Ohne „surjektiv“ fehlt $g$ für manche $y\in B$. Ohne Monotonie gibt es auch nichts zu vererben. **Anwendung:** $\sqrt[n]{y}$ ist streng monoton wachsend. **Grenzfall:** Für $f(x)=x$ ist $f^{-1}=f$, der Graph liegt auf der Spiegelachse.

:::frage Warum steht in [(4.3)](#gl-4-3) für die Wurzel nicht $\sqrt{y^2}=y$ für alle $y$?
Weil die Umkehrung nur zur Funktion auf $\mathbb{R}_0^+$ gehört. Für $y=-3$ ist $\sqrt{(-3)^2}=3$, also allgemein $\sqrt{y^2}=|y|$. Der Fehler entsteht, wenn man den Definitionsbereich vergisst, in dem $f$ umkehrbar ist.
:::

:::aufgabe Aufgabe 4 ★★ Eine Umkehrfunktion bestimmen
<span class="anker" id="aufg-4"></span>

Sei $f:[2,\infty)\to(2,5]$, $f(x)=\dfrac{2x+1}{x-1}=2+\dfrac{3}{x-1}$. (a) Zeige, dass $f$ streng monoton fällt. (b) Bestimme $f^{-1}$. (c) Vergleiche $f^{-1}(4)$ mit $1/f(4)$. (d) Vorhersage: Ist $f^{-1}$ wachsend oder fallend? Prüfe mit $y=3$ und $y=4$.

:::loesung
(a) Aus $2\le x_1<x_2$ folgt $0<x_1-1<x_2-1$, also $\frac{3}{x_1-1}>\frac{3}{x_2-1}$ und $f(x_1)>f(x_2)$. (b) Aus $y=2+\frac{3}{x-1}$ folgt $x-1=\frac{3}{y-2}$, also $f^{-1}(y)=1+\frac{3}{y-2}=\frac{y+1}{y-2}$ für $y\in(2,5]$. (c) $f^{-1}(4)=\frac52$ (Probe: $f(\frac52)=6/1{,}5=4$), dagegen $1/f(4)=\frac13$. (d) Fallend nach Satz [4.4](#satz-4-4): $f^{-1}(3)=4>f^{-1}(4)=\frac52$.
:::
:::

:::aufgabe Aufgabe 5 ★★★ Umkehren einer Kette
<span class="anker" id="aufg-5"></span>

Seien $f(x)=2x+1$, $g(x)=x^3$ auf $\mathbb{R}$. (a) Berechne $(g\circ f)(1)$ und $(f\circ g)(1)$. (b) Zeige allgemein für bijektive $f:A\to B$, $g:B\to C$: $(g\circ f)^{-1}=f^{-1}\circ g^{-1}$. Warum dreht sich die Reihenfolge um? (c) Bestimme $(g\circ f)^{-1}(y)$ und prüfe mit $y=27$.

:::loesung
(a) $(g\circ f)(1)=g(3)=27$, $(f\circ g)(1)=f(1)=3$. (b) $f^{-1}\bigl(g^{-1}(g(f(x)))\bigr)=f^{-1}(f(x))=x$, ebenso in der anderen Reihenfolge für $y\in C$. Damit gelten (I) und (S), und nach Satz [4.2](#satz-4-2)(iii) gibt es nur eine solche Funktion. Der Rückweg muss den letzten Schritt zuerst rückgängig machen. (c) $g^{-1}(y)=\sqrt[3]{y}$, $f^{-1}(y)=\frac{y-1}{2}$, also $(g\circ f)^{-1}(y)=\frac{\sqrt[3]{y}-1}{2}$. Bei $y=27$: $(3-1)/2=1$.
:::
:::

::::formelsammlung
**Summe, Differenz, Produkt und Quotient**

$$(f\pm g)(x):=f(x)\pm g(x),\qquad(f\cdot g)(x):=f(x)\cdot g(x),\qquad\Bigl(\frac fg\Bigr)(x):=\frac{f(x)}{g(x)}$$

Summe, Differenz und Produkt auf $M:=\mathcal D(f)\cap\mathcal D(g)$, der Quotient auf $M':=\{x\in M:g(x)\neq0\}$; gerechnet wird Stelle für Stelle.

**Komposition**

$$(g\circ f)(x):=g\bigl(f(x)\bigr)\quad\text{für alle }x\in A$$

Für $f:A\to B$ und $g:B\to C$ ist $g\circ f:A\to C$, gesprochen „$g$ nach $f$“: $f$ wirkt zuerst. Die Reihenfolge zählt.

**Charakterisierung von injektiv, surjektiv, bijektiv**

$$(g\circ f)(x)=x,\qquad(f\circ g)(y)=y$$

Für $f:A\to B$ mit nicht leerem $A$ und $g:B\to A$. Die linke Gleichung für alle $x\in A$ heißt (I), die rechte für alle $y\in B$ heißt (S). $f$ injektiv $\Leftrightarrow$ es gibt $g$ mit (I); $f$ surjektiv $\Leftrightarrow$ es gibt $g$ mit (S); $f$ bijektiv $\Leftrightarrow$ es gibt genau ein $g$ mit (I) und (S).

**Umkehrfunktion**

$$f(x)=y\ \Leftrightarrow\ x=f^{-1}(y),\qquad f^{-1}\bigl(f(x)\bigr)=x,\qquad f\bigl(f^{-1}(y)\bigr)=y$$

Für bijektives $f:A\to B$ ist $f^{-1}:=g$ die eindeutige Funktion mit (I) und (S); die Gleichungen gelten für alle $x\in A$, $y\in B$. Achtung: $f^{-1}(y)$ ist nicht $1/f(y)$.

**Graph der Umkehrfunktion**

$$\mathcal G(f)=\{(g(y),y):y\in B\},\qquad\mathcal G(g)=\{(y,g(y)):y\in B\}$$

Für $g=f^{-1}$: Die Paare sind vertauscht, der Graph von $f^{-1}$ ist der an der Winkelhalbierenden $y=x$ gespiegelte Graph von $f$.

**$n$-te Wurzel**

$$f^{-1}(y)=\sqrt[n]{y}=y^{1/n},\qquad\sqrt[n]{y^n}=y,\qquad(\sqrt[n]{y})^n=y$$

Umkehrfunktion von $x\mapsto x^n$, auf $\mathbb{R}_0^+$ für gerades $n$ und auf $\mathbb{R}$ für ungerades $n$; die Gleichungen gelten dort. Für alle reellen $y$ gilt nur $\sqrt{y^2}=|y|$.

**Monotonie vererbt sich**

$$g=f^{-1}:B\to A$$

Ist $f:A\to B$ reell, surjektiv und streng monoton wachsend (fallend), so existiert $g$ und ist ebenfalls streng monoton wachsend (fallend); so ist $\sqrt[n]{y}$ streng monoton wachsend.

**Umkehrung einer Kette**

$$(g\circ f)^{-1}=f^{-1}\circ g^{-1}$$

Für bijektive $f:A\to B$ und $g:B\to C$; der Rückweg macht den letzten Schritt zuerst rückgängig.
::::

::::lernkarten
:::karte formel Summe, Differenz, Produkt und Quotient
Wie sind Summe, Differenz, Produkt und Quotient zweier reeller Funktionen $f$ und $g$ erklärt, und auf welchen Mengen?
---
$(f\pm g)(x):=f(x)\pm g(x)$ und $(f\cdot g)(x):=f(x)\cdot g(x)$ auf $M:=\mathcal D(f)\cap\mathcal D(g)$, $\bigl(\frac fg\bigr)(x):=\frac{f(x)}{g(x)}$ auf $M':=\{x\in M:g(x)\neq0\}$; gerechnet wird Stelle für Stelle.
--- falsch
$(f\pm g)(x):=f(x)\pm g(x)$ und $(f\cdot g)(x):=f(x)\cdot g(x)$ auf $M:=\mathcal D(f)\cup\mathcal D(g)$, $\bigl(\frac fg\bigr)(x):=\frac{f(x)}{g(x)}$ auf ganz $M$; wo eine Funktion fehlt, zählt sie als null.
--- falsch
$(f\pm g)(x):=f(x)\pm g(x)$ und $(f\cdot g)(x):=f(g(x))$ auf $M:=\mathcal D(f)\cap\mathcal D(g)$, $\bigl(\frac fg\bigr)(x):=\frac{f(x)}{g(x)}$ auf $M':=\{x\in M:g(x)\neq0\}$; das Produkt ist die Hintereinanderausführung.
--- falsch
$(f\pm g)(x):=f(x)\pm g(x)$ und $(f\cdot g)(x):=f(x)\cdot g(x)$ auf $M:=\mathcal D(f)\cap\mathcal D(g)$, $\bigl(\frac fg\bigr)(x):=\frac{f(x)}{g(x)}$ auf $M':=\{x\in M:f(x)\neq0\}$; der Zähler darf nicht null werden.
:::
:::karte zusammenhang Quotient
Warum ist der Quotient $f/g$ zweier reeller Funktionen nur auf einer kleineren Menge erklärt als Summe und Produkt?
---
Weil er Stelle für Stelle als $\frac{f(x)}{g(x)}$ gerechnet wird und man durch null nicht teilen kann: Neben $x\in\mathcal D(f)\cap\mathcal D(g)$ braucht er $g(x)\neq0$. Summe und Produkt brauchen nur beide Werte.
--- falsch
Weil man $f$ durch $g$ nur teilen kann, wenn $g$ nirgends null ist: Hat $g$ auch nur eine einzige Nullstelle, ist der Quotient $f/g$ auf keiner Menge erklärt.
--- falsch
Weil beim Teilen der Wertebereich kleiner wird: Der Quotient nimmt weniger Werte an als $f$ und $g$, deshalb verkleinert man auch seinen Definitionsbereich auf $\mathcal W(f)\cap\mathcal W(g)$.
--- falsch
Weil man durch null nicht teilen kann: Er braucht $f(x)\neq0$ und $g(x)\neq0$, denn auch null geteilt durch $g(x)$ ist nicht erklärt. Summe und Produkt brauchen nur, dass beide Werte existieren.
:::
:::karte begriff Komposition
Was ist die Komposition $g\circ f$ zweier Funktionen $f:A\to B$ und $g:B\to C$, und welche der beiden wirkt zuerst?
---
Die Hintereinanderausführung $g\circ f:A\to C$, $(g\circ f)(x):=g\bigl(f(x)\bigr)$ für alle $x\in A$, gesprochen „$g$ nach $f$“: $f$ wirkt zuerst, $f(x)$ liegt in $B$, dort wirkt $g$.
--- falsch
Die Hintereinanderausführung $g\circ f:A\to C$, $(g\circ f)(x):=f\bigl(g(x)\bigr)$ für alle $x\in A$, gesprochen „$g$ vor $f$“: $g$ wirkt zuerst, weil es links steht, danach wirkt $f$.
--- falsch
Das Produkt $g\circ f:A\to C$, $(g\circ f)(x):=g(x)\cdot f(x)$ für alle $x\in A$; der Kreis ist nur ein anderes Malzeichen, beide Faktoren wirken gleichzeitig an derselben Stelle.
--- falsch
Die Hintereinanderausführung $g\circ f:A\to C$, $(g\circ f)(x):=g\bigl(f(x)\bigr)$; welche Funktion zuerst wirkt, spielt keine Rolle, weil stets $g\circ f=f\circ g$ gilt.
:::
:::karte zusammenhang Reihenfolge der Komposition
Warum kommt es bei der Komposition auf die Reihenfolge an, und welches Beispiel zeigt das?
---
Weil die zweite Funktion auf das Ergebnis der ersten wirkt: Für $f(x)=2x$ und $g(x)=x+1$ ist $(g\circ f)(1)=3$, aber $(f\circ g)(1)=4$. Erst verdoppeln und dann addieren ist etwas anderes als umgekehrt.
--- falsch
Weil die Komposition nur für Funktionen mit gleichem Definitionsbereich erklärt ist; in der anderen Reihenfolge passt er meist nicht, sonst ergäben $g\circ f$ und $f\circ g$ dasselbe.
--- falsch
Sie kommt nur bei nicht linearen Funktionen darauf an: Für $f(x)=2x$ und $g(x)=x+1$ ist $(g\circ f)(1)=(f\circ g)(1)=3$, weil lineare Funktionen vertauschbar sind.
--- falsch
Weil die links stehende Funktion zuerst wirkt: Für $f(x)=2x$ und $g(x)=x+1$ ist $(g\circ f)(1)=4$, aber $(f\circ g)(1)=3$, also hängt das Ergebnis davon ab, was links steht.
:::
:::karte formel Charakterisierung von injektiv, surjektiv, bijektiv
Wie lassen sich injektiv, surjektiv und bijektiv für $f:A\to B$ mit nicht leerem $A$ durch eine Funktion $g:B\to A$ ausdrücken?
---
Injektiv $\Leftrightarrow$ es gibt $g$ mit $(g\circ f)(x)=x$ für alle $x\in A$ (I); surjektiv $\Leftrightarrow$ es gibt $g$ mit $(f\circ g)(y)=y$ für alle $y\in B$ (S); bijektiv $\Leftrightarrow$ es gibt genau ein $g$ mit (I) und (S).
--- falsch
Injektiv $\Leftrightarrow$ es gibt $g$ mit $(f\circ g)(y)=y$ für alle $y\in B$; surjektiv $\Leftrightarrow$ es gibt $g$ mit $(g\circ f)(x)=x$ für alle $x\in A$; bijektiv $\Leftrightarrow$ es gibt genau ein $g$ mit beidem.
--- falsch
Injektiv $\Leftrightarrow$ es gibt $g$ mit $(g\circ f)(x)=x$ für alle $x\in A$ (I); surjektiv $\Leftrightarrow$ es gibt $g$ mit $(f\circ g)(y)=y$ für alle $y\in B$ (S); bijektiv $\Leftrightarrow$ es gibt ein $g$ mit (I) oder (S).
--- falsch
Injektiv $\Leftrightarrow$ es gibt genau ein $g$ mit $(g\circ f)(x)=x$ für alle $x\in A$; surjektiv $\Leftrightarrow$ es gibt genau ein $g$ mit $(f\circ g)(y)=y$ für alle $y\in B$; bijektiv, wenn beide $g$ verschieden sind.
:::
:::karte herleitung Charakterisierung
Wie zeigt man, dass (I) injektiv und (S) surjektiv ergibt, und dass es zu bijektivem $f$ genau eine Funktion $g$ mit (I) und (S) gibt?
---
(I) ergibt injektiv: Aus $f(x_1)=f(x_2)$ folgt $x_1=g(f(x_1))=g(f(x_2))=x_2$, weil $g$ jedes $f(x)$ auf $x$ zurückführt.
---
(S) ergibt surjektiv: Zu $y\in B$ setzt man $z:=g(y)\in A$; dann ist $f(z)=(f\circ g)(y)=y$, weil (S) für alle $y\in B$ gilt, also ist $y\in\mathcal W(f)$.
---
Ist $f$ bijektiv, hat jedes $y$ genau ein Urbild $g(y)$; dieses $g$ erfüllt (I) und (S), weil es jedem Bild sein einziges Urbild zuordnet.
---
Erfüllt auch $\hat g$ beide, ist $\hat g(y)=\hat g\bigl(f(g(y))\bigr)=g(y)$, weil das innere $f(g(y))=y$ nach (S) für $g$ gilt und $\hat g$ nach (I) jedes Bild $f(x)$ auf $x$ zurückführt.
:::
:::karte zusammenhang Eindeutigkeit braucht bijektiv
Warum gibt es zu einer nur surjektiven Funktion wie $h:\mathbb{R}\to[-1,\infty)$ keine eindeutige Funktion $g$ mit (S)?
---
Weil manche $y$ mehrere Urbilder haben und $g$ eines davon wählen darf: $g_1(y)=2+\sqrt{y+1}$ und $g_2(y)=2-\sqrt{y+1}$ erfüllen beide (S). Eindeutig wird $g$ erst, wenn $f$ bijektiv ist.
--- falsch
Weil es gar keine Funktion mit (S) gibt: (S) verlangt, dass $h$ injektiv ist, und $h$ trifft die Höhe $3$ zweimal. Erst wenn $h$ bijektiv ist, existiert überhaupt ein solches $g$.
--- falsch
Weil $g$ nur auf $\mathcal W(h)$ festliegt und außerhalb beliebig ist: Für $y<-1$ darf $g(y)$ jeden Wert haben. Bei surjektivem $h$ ist das die einzige Freiheit, die $g$ hat.
--- falsch
Weil $g_1(y)=2+\sqrt{y+1}$ zwar (S) erfüllt, $g_2(y)=2-\sqrt{y+1}$ aber nicht, da es negative Werte liefert. Eindeutig ist $g$ also doch, nur schwer zu finden.
:::
:::karte begriff Umkehrfunktion
Was ist die Umkehrfunktion $f^{-1}$ einer bijektiven Funktion $f:A\to B$, und welche Gleichungen erfüllt sie?
---
Die eindeutige Funktion $g:B\to A$ mit (I) und (S), $f^{-1}:=g$. Für alle $x\in A$, $y\in B$ gilt $f(x)=y\ \Leftrightarrow\ x=f^{-1}(y)$, $f^{-1}\bigl(f(x)\bigr)=x$ und $f\bigl(f^{-1}(y)\bigr)=y$.
--- falsch
Der Kehrwert $f^{-1}(y):=1/f(y)$, erklärt für alle $y$ mit $f(y)\neq0$. Für ihn gilt $f(y)\cdot f^{-1}(y)=1$, so wie für Zahlen das Produkt mit dem Inversen eins ergibt.
--- falsch
Die eindeutige Funktion $g:B\to A$ mit (I) und (S), $f^{-1}:=g$. Für alle $x\in A$, $y\in B$ gilt $f(x)=y\ \Leftrightarrow\ y=f^{-1}(x)$, $f^{-1}\bigl(f(x)\bigr)=f(x)$ und $f\bigl(f^{-1}(y)\bigr)=f(y)$.
--- falsch
Eine Funktion $g:B\to A$ mit (S), die zu jeder surjektiven Funktion existiert; sie ist eindeutig, weil jedes $y$ ein Urbild hat. Es gilt $f\bigl(g(y)\bigr)=y$ für alle $y\in B$.
:::
:::karte zusammenhang Umkehrfunktion und Kehrwert
Warum darf man den Wert $f^{-1}(y)$ der Umkehrfunktion nicht mit dem Kehrwert $1/f(y)$ verwechseln?
---
Weil $f^{-1}(y)$ die Lösung $x$ von $f(x)=y$ ist und $1/f(y)$ nur den Wert von $f$ an der Stelle $y$ umkehrt: Für $h$ auf $[2,\infty)$ ist $h^{-1}(8)=5$, aber $1/h(8)=1/35$.
--- falsch
Weil sie sich nur im Vorzeichen unterscheiden: Es gilt $f^{-1}(y)=-1/f(y)$, denn die Umkehrfunktion spiegelt den Graphen, und Spiegeln bringt ein Minuszeichen.
--- falsch
Man darf sie verwechseln, sie sind gleich: Das Zeichen ${}^{-1}$ bedeutet wie bei Zahlen den Kehrwert, also $f^{-1}(y)=1/f(y)$; „Umkehrfunktion“ ist nur ein anderer Name dafür.
--- falsch
Weil $1/f(y)$ nur für bijektive $f$ erklärt ist, $f^{-1}(y)$ dagegen für jede Funktion: Für $h$ auf $\mathbb{R}$ ist $h^{-1}(8)$ erklärt, der Kehrwert $1/h(8)$ dagegen nicht.
:::
:::karte begriff n-te Wurzel
Wie ist die $n$-te Wurzel als Umkehrfunktion erklärt, und welche Gleichungen gelten für sie?
---
Als Umkehrfunktion von $x\mapsto x^n$, auf $\mathbb{R}_0^+$ für gerades $n$ und auf $\mathbb{R}$ für ungerades $n$: $f^{-1}(y)=\sqrt[n]{y}=y^{1/n}$. Dort gilt $\sqrt[n]{y^n}=y$ und $(\sqrt[n]{y})^n=y$.
--- falsch
Als Umkehrfunktion von $x\mapsto x^n$ auf ganz $\mathbb{R}$ für jedes $n$: $f^{-1}(y)=\sqrt[n]{y}=y^{1/n}$. Für alle reellen $y$ gilt $\sqrt[n]{y^n}=y$ und $(\sqrt[n]{y})^n=y$.
--- falsch
Als Kehrwert der $n$-ten Potenz, $\sqrt[n]{y}:=1/y^n$, erklärt für alle $y\neq0$ und für jedes $n$. Es gilt $\sqrt[n]{y}\cdot y^n=1$; deshalb schreibt man die $n$-te Wurzel auch als $y^{-n}$.
--- falsch
Als Umkehrfunktion von $x\mapsto x^n$, auf $\mathbb{R}$ für gerades $n$ und auf $\mathbb{R}_0^+$ für ungerades $n$: $f^{-1}(y)=\sqrt[n]{y}=y^{1/n}$. Dort gilt $\sqrt[n]{y^n}=y$ und $(\sqrt[n]{y})^n=y$.
:::
:::karte zusammenhang Graph der Umkehrfunktion
Warum ist der Graph der Umkehrfunktion $g=f^{-1}$ der an der Geraden $y=x$ gespiegelte Graph von $f$?
---
Weil $\mathcal G(f)=\{(x,f(x))\}=\{(g(y),y):y\in B\}$ und $\mathcal G(g)=\{(y,g(y)):y\in B\}$ dieselben Paare mit vertauschten Koordinaten enthalten; das Vertauschen ist die Spiegelung an der Winkelhalbierenden.
--- falsch
Weil $g$ die Werte von $f$ mit $-1$ multipliziert: Aus jedem Punkt $(x,f(x))$ wird $(x,-f(x))$. Das ist die Spiegelung an der Winkelhalbierenden, die durch den Ursprung geht.
--- falsch
Weil $g$ rückwärts läuft: Aus jedem Punkt $(x,f(x))$ wird $(-x,f(x))$, der Graph wird also von rechts nach links durchlaufen. Das ist die Spiegelung an der Geraden $y=x$.
--- falsch
Weil $\mathcal G(g)=\mathcal G(f)$ gilt: Beide Graphen bestehen aus denselben Punkten, man liest sie nur einmal von der $x$-Achse und einmal von der $y$-Achse aus; gespiegelt wird nur die Beschriftung.
:::
:::karte formel Monotonie vererbt sich
Was sagt der Satz „Monotonie vererbt sich“ über die Umkehrfunktion einer streng monotonen Funktion, und was setzt er voraus?
---
Ist $f:A\to B$ reell, surjektiv und streng monoton wachsend (fallend), so existiert $g=f^{-1}:B\to A$ und ist ebenfalls streng monoton wachsend (fallend). Ohne „surjektiv“ fehlt $g$ für manche $y\in B$.
--- falsch
Ist $f:A\to B$ reell, surjektiv und streng monoton wachsend (fallend), so existiert $g=f^{-1}:B\to A$ und ist streng monoton fallend (wachsend), denn die Spiegelung an $y=x$ kehrt die Richtung um.
--- falsch
Ist $f:A\to B$ reell und monoton wachsend (fallend), so existiert $g=f^{-1}:B\to A$ immer und ist ebenfalls monoton wachsend (fallend). Weitere Voraussetzungen braucht der Satz nicht.
--- falsch
Ist $f:A\to B$ reell und streng monoton wachsend (fallend), so existiert $g=f^{-1}:B\to A$ auch ohne Surjektivität, denn streng monotone Funktionen treffen jede Höhe in $B$.
:::
:::karte herleitung Monotonie vererbt sich
Wie zeigt man, dass die Umkehrfunktion einer surjektiven, streng monoton wachsenden reellen Funktion $f:A\to B$ existiert und ebenfalls streng monoton wächst?
---
$g=f^{-1}$ existiert, weil $f$ bijektiv ist: injektiv wie im Satz „Streng monoton ergibt bijektiv“ und surjektiv nach Voraussetzung.
---
Seien $y_1<y_2$ in $B$; zu zeigen ist $g(y_1)<g(y_2)$, weil das die Definition von streng wachsend für $g$ ist.
---
Wäre $g(y_1)\ge g(y_2)$, ergäbe Anwenden von $f$ den Widerspruch $y_1\ge y_2$, weil $f$ wachsend ist und $f(g(y))=y$ gilt.
---
Also ist $g(y_1)<g(y_2)$; der fallende Fall geht gleich, weil sich dort nur beide Ungleichungen umdrehen.
:::
:::karte zusammenhang Wurzel aus einem Quadrat
Warum gilt die Gleichung $\sqrt{y^2}=y$ nicht für alle reellen $y$, obwohl die Wurzel die Umkehrfunktion des Quadrats ist?
---
Weil die Umkehrung nur zur Funktion $x^2$ auf $\mathbb{R}_0^+$ gehört: Für $y=-3$ ist $\sqrt{(-3)^2}=3$, allgemein $\sqrt{y^2}=|y|$. Der Fehler entsteht, wenn man den Definitionsbereich vergisst.
--- falsch
Weil die Wurzel zwei Werte hat, $\pm y$: Für $y=-3$ ist $\sqrt{(-3)^2}=\pm3$, und man muss je nach Aufgabe den passenden Wert wählen. Die Gleichung gilt also nur bis aufs Vorzeichen.
--- falsch
Doch, sie gilt für alle reellen $y$, denn Quadrieren und Wurzelziehen heben sich immer auf; $\sqrt{(-3)^2}=-3$ ist nur ungewohnt, weil Wurzeln meist positiv geschrieben werden.
--- falsch
Weil $y^2$ für negative $y$ negativ ist und die Wurzel daraus nicht existiert: Für $y=-3$ ist $\sqrt{(-3)^2}$ nicht erklärt, die Gleichung gilt deshalb nur für $y\ge0$.
:::
:::karte zusammenhang Umkehren einer Kette
Warum dreht sich beim Umkehren einer Komposition bijektiver Funktionen die Reihenfolge um, also $(g\circ f)^{-1}=f^{-1}\circ g^{-1}$?
---
Weil der Rückweg den letzten Schritt zuerst rückgängig machen muss: $f^{-1}\bigl(g^{-1}(g(f(x)))\bigr)=f^{-1}(f(x))=x$, ebenso andersherum, und es gibt nur eine solche Funktion.
--- falsch
Sie dreht sich gar nicht um: $(g\circ f)^{-1}=g^{-1}\circ f^{-1}$, denn man kehrt jede Funktion einzeln um und behält ihre Reihenfolge bei, wie beim Kehrwert eines Produkts von Zahlen.
--- falsch
Weil die Komposition vertauschbar ist: $f^{-1}\circ g^{-1}$ und $g^{-1}\circ f^{-1}$ sind dieselbe Funktion, man schreibt nur gewöhnlich die zuerst umgekehrte Funktion links.
--- falsch
Weil $g\circ f$ als Produkt $g\cdot f$ zu lesen ist und für den Kehrwert $(g\cdot f)^{-1}=f^{-1}\cdot g^{-1}$ gilt; die Reihenfolge der Faktoren kehrt sich beim Kehrwert immer um.
:::
::::

---
title: Stufe 7: Maximum, Minimum, gleichmäßige Stetigkeit
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Exponentialfunktion und Stetigkeit
adresse: elektrotechnik/1-semester/hohere-mathematik-1/exponentialfunktion-und-stetigkeit
knoten: Kapitel 5: Exponentialfunktion und Stetigkeit
order: 1250900
summary: Hat eine stetige Funktion einen größten Wert?
tags: Minimum, Maximum, nicht konstruktiv, gleichmäßig stetig
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Hat eine stetige Funktion einen größten Wert? Reicht eine Eingangstoleranz für alle Stellen? Auf $[a,b]$ ja. Diese Stufe zeigt warum und was geschieht, wenn eine Voraussetzung fehlt.
:::

**Die Idee.** Man nimmt Stellen $x_n$, an denen $f$ dem Supremum immer näher kommt. Eine Teilfolge läuft gegen eine Stelle $x_1$. Die Abgeschlossenheit hält $x_1$ im Intervall, die Stetigkeit nimmt die Werte mit: $f(x_1)$ ist das Supremum.

:::satz Satz 7.1 (Stetig auf [a,b] ist beschränkt)
<span class="anker" id="satz-7-1"></span>

Sei $a<b$ und $f:[a,b]\to\mathbb{R}$ stetig. Dann ist $f$ beschränkt: Es gibt $K>0$ mit $|f(x)|\le K$ für alle $x\in[a,b]$.
:::

:::beweis Indirekt mit Bolzano-Weierstraß
Sei $f$ ohne Einschränkung nach oben unbeschränkt (sonst betrachte $-f$). Dann gibt es zu jedem $n\in\mathbb{N}$ ein $x_n\in[a,b]$ mit $f(x_n)>n$. Die Folge $\{x_n\}$ ist beschränkt, also gibt es eine Teilfolge $x_{n_k}\to\bar x$. Wegen $a\le x_{n_k}\le b$ gilt $\bar x\in[a,b]$. Die Folgenstetigkeit gibt $f(x_{n_k})\to f(\bar x)\in\mathbb{R}$. Konvergente Folgen sind beschränkt, aber $f(x_{n_k})>n_k\ge k$. Widerspruch.
:::

⁠**So liest man das:** Der Graph liegt in einem waagerechten Streifen der Höhe $2K$.

:::satz Satz 7.2 (Weierstraß, Satz vom Maximum)
<span class="anker" id="satz-7-2"></span>

Sei $f:[a,b]\to\mathbb{R}$ stetig. Dann nimmt $f$ das Infimum $m=\inf\mathcal W(f)\in\mathbb{R}$ und das Supremum $M=\sup\mathcal W(f)\in\mathbb{R}$ als Wert an:

<ol class="rm">

<li>

$m\in\mathcal W(f)$: Es gibt $x_0\in[a,b]$ mit $f(x)\ge m=f(x_0)$ für alle $x\in[a,b]$, also ist $\inf\mathcal W(f)$ ein __Minimum__.

</li>

<li>

$M\in\mathcal W(f)$: Es gibt $x_1\in[a,b]$ mit $f(x)\le M=f(x_1)$ für alle $x\in[a,b]$, also ist $\sup\mathcal W(f)$ ein __Maximum__.

</li>

</ol>
:::

:::beweis Teilfolge wählen, Wert mitnehmen
Nach Satz [7.1](#satz-7-1) ist $\mathcal W(f)$ beschränkt und nicht leer, das Vollständigkeitsaxiom gibt $M\in\mathbb{R}$. Da $M-\frac1n$ keine obere Schranke ist, gibt es $x_n\in[a,b]$ mit $M-\frac1n<f(x_n)\le M$, also $f(x_n)\to M$. Bolzano-Weierstraß gibt eine Teilfolge $x_{n_k}\to x_1$, und $x_1\in[a,b]$ wie oben. Die Folgenstetigkeit gibt $f(x_1)=\lim_{k\to\infty}f(x_{n_k})=M$. Für $m$ wendet man das auf $-f$ an.
:::

⁠**So liest man das:** Ein Supremum muss kein Funktionswert sein, hier ist es einer. Wo, sagt der Beweis nicht: Er ist __nicht konstruktiv__.

::::beispiel [Beispiele]
Die wachsende Prüffunktion hat auf $[0,1]$ das Minimum $k(0)=1$ und das Maximum $k(1)=3{,}718$. Die Kurve $i(x)=x\,\mathrm{e}^{-x}$ auf $[0,2]$ (so verläuft der Strom eines kritisch gedämpften Schwingkreises) hat das Minimum $i(0)=0$ und das Maximum $i(1)=\frac{1}{\mathrm{e}}=0{,}3679$. Das zeigt Satz [2.1](wachstum-logarithmus-allgemeine-potenz.html#satz-2-1) (i): Aus $\mathrm{e}^{x-1}\ge x$ folgt $x\,\mathrm{e}^{-x}\le\mathrm{e}^{-1}$.
::::

⁠**Grenzfall:** Für konstantes $f$ ist $m=M$.

**Jede Voraussetzung wird gebraucht (Abb. [7](#abb-7)).**

| Was fehlt | Gegenbeispiel | Was im Beweis bricht |
|---|---|---|
| abgeschlossen | $1/x$ auf $(0,1]$: unbeschränkt. $x$ auf $[0,1)$: beschränkt, Supremum 1 kein Wert | Der Grenzpunkt $\bar x=0$ bzw. $1$ liegt nicht im Intervall |
| beschränktes Intervall | $\mathrm{e}^x$ auf $[0,\infty)$: unbeschränkt, kein Maximum | $\{x_n\}$ läuft weg, Bolzano-Weierstraß greift nicht |
| stetig | $f(x)=\frac1{x-1}$, $f(1)=0$ auf $[0,2]$: unbeschränkt. $v(x)=x$ für $x<1$, $v(1)=0$ auf $[0,1]$: beschränkt, Supremum 1 kein Wert | Der Wert $f(\bar x)$ folgt den $f(x_{n_k})$ nicht |

:::abbildung hm1/k5maximum 7
Links wächst $1/x$ auf $(0,1]$ ohne Grenze, die 0 fehlt. Mitte: $v$ springt bei 1 nach unten, das Supremum 1 wird nicht erreicht. Rechts steigt $\mathrm{e}^x$ auf $[0,\infty)$ immer weiter.
:::

**Eine Eingangstoleranz für alle Stellen.** In Stufe [4](stetigkeit-und-epsilon-delta.html#stufe-4) hing $\delta_0$ von $x_0$ ab. Bei $1/x$ auf $(0,1]$ muss man das: Für $\varepsilon=1$ ist die größte Antwort $\delta_0=\frac16$ bei $x_0=\frac12$, aber nur $\frac1{20}$ bei $x_0=\frac14$. Allgemein ist sie $\frac{\varepsilon x_0^2}{1+\varepsilon x_0}$, und das schrumpft mit $x_0$ gegen 0. Keine Antwort gewinnt überall.

:::definition Definition 7.3 (Gleichmäßige Stetigkeit)
<span class="anker" id="satz-7-3"></span>

Sei $f:M\to\mathbb{R}$, $M\subset\mathbb{R}$. Dann heißt $f$ auf $M$ __gleichmäßig stetig__, wenn es zu jedem $\varepsilon>0$ ein $\delta_0=\delta_0(\varepsilon)>0$ gibt, so dass für alle $x,y\in M$ gilt:

<span class="anker" id="gl-7-1"></span>
$$|x-y|<\delta_0\quad\Longrightarrow\quad|f(x)-f(y)|<\varepsilon. \tag{7.1}$$
:::

⁠**So liest man das:** Im Unterschied zum $\varepsilon$-$\delta$-Kriterium darf $\delta_0$ nicht von $x$ oder $y$ abhängen. Hält man $y=x_0$ fest, entsteht [(4.1)](stetigkeit-und-epsilon-delta.html#gl-4-1): Gleichmäßig stetig auf $(a,b)$ ergibt stetig in jedem Punkt. Die Umkehrung gilt nicht, wie $1/x$ auf $(0,1]$ zeigt: Für $x=\frac1n$, $y=\frac1{n+1}$ ist $|x-y|=\frac1{n(n+1)}\to0$, aber $|f(x)-f(y)|=1$.

::::beispiel
$x^2$ auf $[0,3]$: Es ist $|x^2-y^2|=|x-y|\,|x+y|\le6\,|x-y|$, also gewinnt $\delta_0=\varepsilon/6$ überall. Auf ganz $\mathbb{R}$ fehlt die Schranke für $|x+y|$.
::::

:::satz Satz 7.4 (Stetig auf [a,b] ist gleichmäßig stetig)
<span class="anker" id="satz-7-4"></span>

Sei $f:[a,b]\to\mathbb{R}$ stetig. Dann ist $f$ auf $[a,b]$ gleichmäßig stetig.
:::

:::beweis Wieder Teilfolge und Stetigkeit
Wäre $f$ nicht gleichmäßig stetig, gäbe es $\varepsilon_1>0$ und zu jedem $n$ Stellen $x_n,y_n\in[a,b]$ mit $|x_n-y_n|<\frac1n$ und $|f(x_n)-f(y_n)|\ge\varepsilon_1$. Bolzano-Weierstraß gibt eine Teilfolge $x_{n_k}\to\bar x\in[a,b]$. Wegen $y_{n_k}=(y_{n_k}-x_{n_k})+x_{n_k}$ läuft auch $y_{n_k}\to\bar x$. Die Folgenstetigkeit gibt $f(x_{n_k})\to f(\bar x)$ und $f(y_{n_k})\to f(\bar x)$, also $|f(x_{n_k})-f(y_{n_k})|\to0$. Das widerspricht $\ge\varepsilon_1$.
:::

⁠**So liest man das:** Auf $[a,b]$ reicht eine Eingangstoleranz für alle Stellen. Auf $(0,1]$ fehlt der Grenzpunkt 0, deshalb scheitert $1/x$.

:::aufgabe Aufgabe 7 ★★ Satz anwendbar?
<span class="anker" id="aufg-7"></span>

Entscheide jeweils, ob der Satz vom Maximum gilt. Gib Maximum und Minimum an oder begründe, warum eines fehlt. (a) $x^2$ auf $[-1,2]$. (b) $x^2$ auf $(-1,1)$. (c) $\mathrm{e}^{-x}$ auf $[0,\infty)$. (d) $H$ auf $[-1,1]$. (e) Bestimme das Minimum von $x-\log x$ auf $[\frac12,2]$ mit Satz [2.3](wachstum-logarithmus-allgemeine-potenz.html#satz-2-3) (iv).

:::loesung
(a) Gilt: Maximum 4 bei 2, Minimum 0 bei 0. (b) Nicht abgeschlossen: Minimum 0, Supremum 1 wird nicht angenommen. (c) Unbeschränktes Intervall: Maximum 1 bei 0, Infimum 0 wird nicht angenommen. (d) Nicht stetig. Hier existieren trotzdem Maximum 1 und Minimum 0: Der Satz ist hinreichend, nicht notwendig. (e) Aus $\log x\le x-1$ folgt $x-\log x\ge1$, Gleichheit bei $x=1$: Das Minimum ist 1.
:::
:::

::::formelsammlung
**Beschränktheit**

$$|f(x)|\le K\quad\text{für alle }x\in[a,b]$$

Für $f:[a,b]\to\mathbb{R}$ stetig, $a<b$, gibt es ein solches $K>0$.

**Satz vom Maximum**

$$f(x)\ge m=f(x_0),\qquad f(x)\le M=f(x_1)\qquad\text{für alle }x\in[a,b]$$

Für $f:[a,b]\to\mathbb{R}$ stetig, mit $m=\inf\mathcal W(f)$, $M=\sup\mathcal W(f)$ und Stellen $x_0,x_1\in[a,b]$: Minimum und Maximum werden angenommen. Der Beweis ist nicht konstruktiv. Jede Voraussetzung wird gebraucht (abgeschlossen, beschränkt, stetig).

**Gleichmäßige Stetigkeit**

$$|x-y|<\delta_0\quad\Longrightarrow\quad|f(x)-f(y)|<\varepsilon$$

Für alle $x,y\in M$, mit $\delta_0=\delta_0(\varepsilon)$ zu jedem $\varepsilon>0$, unabhängig von $x$ und $y$.

**Größte Eingangstoleranz für den Kehrwert**

$$\delta_0=\frac{\varepsilon x_0^2}{1+\varepsilon x_0}$$

Für $1/x$ auf $(0,1]$; schrumpft mit $x_0$ gegen 0, deshalb ist $1/x$ dort nicht gleichmäßig stetig.

**Stetig auf abgeschlossenem Intervall**

$$f:[a,b]\to\mathbb{R}\ \text{stetig}\quad\Longrightarrow\quad f\ \text{gleichmäßig stetig auf }[a,b]$$

Auf $(0,1]$ fehlt der Grenzpunkt 0, deshalb scheitert $1/x$.
::::

::::lernkarten
:::karte formel Stetig auf einem abgeschlossenen Intervall ist beschränkt
Was gilt für die Werte einer stetigen Funktion $f:[a,b]\to\mathbb{R}$ mit $a<b$?
---
$f$ ist beschränkt: Es gibt $K>0$ mit $|f(x)|\le K$ für alle $x\in[a,b]$. Der Graph liegt in einem waagerechten Streifen der Höhe $2K$.
--- falsch
$f$ ist beschränkt, aber nur, wenn $f$ zusätzlich monoton ist: Dann liegen alle Werte zwischen $f(a)$ und $f(b)$.
--- falsch
$f$ ist nach unten beschränkt, weil $f(a)$ ein fester Startwert ist; nach oben kann $f$ dagegen unbeschränkt wachsen, etwa wie $\frac1{x-1}$ auf $[0,2]$.
--- falsch
$f$ ist beschränkt, und die Schranke ist stets $K=\max\{|f(a)|,|f(b)|\}$: Die größten Beträge nimmt eine stetige Funktion an den Rändern an.
:::
:::karte formel Satz vom Maximum
Was besagt der Satz vom Maximum (Weierstraß) für eine stetige Funktion $f:[a,b]\to\mathbb{R}$?
---
$f$ nimmt $m=\inf\mathcal W(f)\in\mathbb{R}$ und $M=\sup\mathcal W(f)\in\mathbb{R}$ als Wert an: Es gibt $x_0,x_1\in[a,b]$ mit $f(x)\ge m=f(x_0)$ und $f(x)\le M=f(x_1)$ für alle $x\in[a,b]$. Das Infimum ist also ein Minimum, das Supremum ein Maximum.
--- falsch
$f$ besitzt ein Supremum $M=\sup\mathcal W(f)$ und ein Infimum $m=\inf\mathcal W(f)$ in $\mathbb{R}$; ob sie als Werte angenommen werden, lässt der Satz offen, das hängt von $f$ ab.
--- falsch
$f$ nimmt $M=\sup\mathcal W(f)$ als Wert an, das Infimum $m$ dagegen nicht unbedingt, weil der Beweis nur Folgen benutzt, deren Werte dem Supremum näher kommen.
--- falsch
$f$ nimmt $m$ und $M$ als Wert an, und zwar stets an den Rändern: $\{f(a),f(b)\}=\{m,M\}$, weil eine stetige Funktion im Inneren keinen größten Wert haben kann.
:::
:::karte zusammenhang Maximum und Minimum
Was bedeutet es im Satz vom Maximum, dass $\sup\mathcal W(f)$ ein Maximum und $\inf\mathcal W(f)$ ein Minimum ist?
---
Supremum und Infimum des Wertebereichs sind selbst Funktionswerte, $f$ nimmt sie an Stellen von $[a,b]$ an. Im Allgemeinen gilt das nicht: $x$ auf $[0,1)$ hat das Supremum 1, nimmt es aber nicht an.
--- falsch
Supremum und Infimum liegen im Inneren von $(a,b)$, nicht an den Rändern. Ein Maximum ist ein Supremum, das an einer inneren Stelle erreicht wird; ein Wert am Rand zählt nicht als Maximum, sondern nur als Randwert.
--- falsch
Supremum und Infimum sind endliche Zahlen. Mehr sagen die Wörter Maximum und Minimum nicht aus; ob die Werte auch angenommen werden, ist damit nicht gesagt, das muss man an der Funktion einzeln prüfen.
--- falsch
Supremum und Infimum werden an genau einer Stelle angenommen: Ein Maximum ist eindeutig, eine Funktion kann ihren größten Wert nicht an zwei Stellen haben, sonst wäre keiner der beiden der größte.
:::
:::karte herleitung Teilfolge wählen, Wert mitnehmen
Wie beweist man, dass eine stetige Funktion $f:[a,b]\to\mathbb{R}$ ihr Supremum $M$ als Wert annimmt?
---
$\mathcal W(f)$ ist beschränkt und nicht leer, also gibt es $M=\sup\mathcal W(f)\in\mathbb{R}$, weil stetige Funktionen auf $[a,b]$ beschränkt sind und das Vollständigkeitsaxiom gilt.
---
Zu jedem $n$ gibt es $x_n\in[a,b]$ mit $M-\frac1n<f(x_n)\le M$, weil $M-\frac1n$ keine obere Schranke ist; also gilt $f(x_n)\to M$.
---
Bolzano-Weierstraß gibt eine Teilfolge $x_{n_k}\to x_1$ mit $x_1\in[a,b]$, weil $\{x_n\}$ beschränkt ist und $a\le x_{n_k}\le b$ auch für den Grenzwert gilt.
---
Die Folgenstetigkeit gibt $f(x_1)=\lim_{k\to\infty}f(x_{n_k})=M$, weil die Bilder einer konvergenten Folge gegen das Bild des Grenzwerts laufen.
---
Für das Minimum wendet man dasselbe auf $-f$ an, weil das Supremum von $-f$ das Negative des Infimums von $f$ ist.
:::
:::karte begriff nicht konstruktiv
Was bedeutet es, dass der Beweis des Satzes vom Maximum nicht konstruktiv ist?
---
Ein Beweis heißt nicht konstruktiv, wenn er zeigt, dass etwas existiert, ohne zu sagen, wo es liegt oder wie man es berechnet. Hier sichert er eine Stelle $x_1$ mit $f(x_1)=M$, nennt sie aber nicht.
--- falsch
Ein Beweis heißt nicht konstruktiv, wenn er indirekt geführt wird, also mit einem Widerspruch endet. Hier nimmt er an, das Maximum fehle, und leitet daraus einen Widerspruch her.
--- falsch
Ein Beweis heißt nicht konstruktiv, wenn er nur für Beispiele gilt und nicht allgemein. Hier zeigt er das Maximum nur für die Prüffunktion $k$ und die Kurve $i(x)=x\,\mathrm{e}^{-x}$ auf $[0,2]$.
--- falsch
Ein Beweis heißt nicht konstruktiv, wenn er Lücken hat, die man später schließen muss. Hier fehlt etwa die Begründung, dass der Grenzwert der Teilfolge im Intervall $[a,b]$ bleibt.
:::
:::karte zusammenhang Voraussetzungen des Satzes vom Maximum
Welche Voraussetzung des Satzes vom Maximum fehlt bei $1/x$ auf $(0,1]$ und bei $\mathrm{e}^x$ auf $[0,\infty)$, und welcher Beweisschritt bricht jeweils?
---
Bei $1/x$ auf $(0,1]$ fehlt die Abgeschlossenheit: Der Grenzpunkt $\bar x=0$ liegt nicht im Intervall. Bei $\mathrm{e}^x$ auf $[0,\infty)$ fehlt ein beschränktes Intervall: $\{x_n\}$ läuft weg, Bolzano-Weierstraß greift nicht.
--- falsch
Bei beiden fehlt die Stetigkeit: $1/x$ springt bei 0 ins Unendliche, $\mathrm{e}^x$ springt bei $\infty$. Deshalb folgt in beiden Fällen der Wert $f(\bar x)$ den Bildern $f(x_{n_k})$ der Teilfolge nicht.
--- falsch
Bei $1/x$ fehlt ein beschränktes Intervall, weil $1/x$ unbeschränkt ist; bei $\mathrm{e}^x$ fehlt die Abgeschlossenheit, weil $[0,\infty)$ rechts offen ist. In beiden Fällen bricht nur die Monotonie.
--- falsch
Es fehlt keine Voraussetzung: Beide Funktionen haben ein Maximum, nur liegt es an einer Stelle, die der Beweis nicht findet, weil er nicht konstruktiv ist und keine Stelle nennt.
:::
:::karte zusammenhang Stetigkeit nötig
Warum nimmt $v(x)=x$ für $x<1$, $v(1)=0$ auf $[0,1]$ sein Supremum nicht an, obwohl das Intervall abgeschlossen und beschränkt ist?
---
Weil $v$ bei 1 nicht stetig ist: Die Werte $v(x)$ kommen dem Supremum 1 beliebig nahe, aber der Wert $v(1)=0$ an der Grenzstelle folgt ihnen nicht.
--- falsch
Weil $v$ nicht monoton ist: Der Satz vom Maximum gilt nur für monotone Funktionen, bei denen das Maximum an einem Rand liegt; $v$ fällt bei 1 aber plötzlich ab.
--- falsch
Doch, $v$ nimmt sein Supremum an: Das Supremum ist $v(1)=0$, weil der Wert am rechten Rand stets als größter Wert eines abgeschlossenen Intervalls zählt.
--- falsch
Weil $v$ unbeschränkt ist: Nahe 1 wachsen die Werte über jede Grenze, und ein unbeschränkter Wertebereich hat kein Supremum, das angenommen werden könnte.
:::
:::karte zusammenhang hinreichend, nicht notwendig
Folgt aus der Existenz von Maximum und Minimum einer Funktion auf $[-1,1]$, dass sie dort stetig ist?
---
Nein: Der Schalter $H$ ist auf $[-1,1]$ nicht stetig und hat trotzdem das Maximum 1 und das Minimum 0. Der Satz vom Maximum ist hinreichend, nicht notwendig.
--- falsch
Ja: Der Satz vom Maximum gilt in beiden Richtungen; hat eine Funktion auf einem abgeschlossenen Intervall Maximum und Minimum, so muss sie dort stetig sein.
--- falsch
Ja, sofern das Intervall abgeschlossen und beschränkt ist; ohne Stetigkeit kann eine Funktion auf $[-1,1]$ weder ein Maximum noch ein Minimum haben.
--- falsch
Nein, aber nur, weil $[-1,1]$ negative Zahlen enthält; auf Intervallen aus nicht negativen Zahlen folgt aus Maximum und Minimum die Stetigkeit.
:::
:::karte begriff gleichmäßig stetig
Wann heißt $f:M\to\mathbb{R}$ auf $M\subset\mathbb{R}$ gleichmäßig stetig, mit den Quantoren in der richtigen Reihenfolge?
---
Wenn es zu jedem $\varepsilon>0$ ein $\delta_0=\delta_0(\varepsilon)>0$ gibt, so dass für alle $x,y\in M$ gilt: $|x-y|<\delta_0\Longrightarrow|f(x)-f(y)|<\varepsilon$. Das $\delta_0$ hängt nur von $\varepsilon$ ab, nicht von $x$ oder $y$.
--- falsch
Wenn es zu jedem $\varepsilon>0$ und jedem $x\in M$ ein $\delta_0=\delta_0(\varepsilon,x)>0$ gibt, so dass für alle $y\in M$ gilt: $|x-y|<\delta_0\Longrightarrow|f(x)-f(y)|<\varepsilon$. Das $\delta_0$ darf sich von Stelle zu Stelle ändern.
--- falsch
Wenn es ein $\delta_0>0$ gibt, so dass für alle $\varepsilon>0$ und alle $x,y\in M$ gilt: $|x-y|<\delta_0\Longrightarrow|f(x)-f(y)|<\varepsilon$. Ein einziges $\delta_0$ passt dann für jede Toleranz $\varepsilon$.
--- falsch
Wenn es zu jedem $\varepsilon>0$ ein $\delta_0>0$ gibt, so dass für alle $x,y\in M$ gilt: $|f(x)-f(y)|<\varepsilon\Longrightarrow|x-y|<\delta_0$. Nahe Werte gehören also stets zu nahe beieinander liegenden Stellen.
:::
:::karte zusammenhang Unterschied zum Epsilon-Delta-Kriterium
Worin unterscheidet sich gleichmäßige Stetigkeit vom Epsilon-Delta-Kriterium, und welche Richtung der Folgerung gilt zwischen beiden?
---
Beim Kriterium darf $\delta_0$ von der Stelle $x_0$ abhängen, bei gleichmäßiger Stetigkeit nicht. Hält man $y=x_0$ fest, entsteht das Kriterium: Gleichmäßig stetig auf $(a,b)$ ergibt stetig in jedem Punkt; die Umkehrung gilt nicht.
--- falsch
Gleichmäßige Stetigkeit erlaubt ein $\delta_0$, das von $x$ und $y$ abhängt, das Kriterium nur eines, das von $\varepsilon$ abhängt. Deshalb ergibt stetig in jedem Punkt stets gleichmäßig stetig, und die Umkehrung gilt nicht.
--- falsch
Es gibt keinen Unterschied: Beide verlangen zu jedem $\varepsilon$ ein $\delta_0$, und weil $\delta_0$ in beiden Fällen von $\varepsilon$ abhängt, sind die beiden Begriffe gleichwertig und folgen auseinander.
--- falsch
Bei gleichmäßiger Stetigkeit hängt $\delta_0$ nicht von der Stelle ab. Trotzdem folgt aus ihr die Stetigkeit in den einzelnen Punkten nicht, weil das Kriterium dort ein eigenes $\delta_0$ für jede Stelle verlangt.
:::
:::karte zusammenhang Kehrwert nahe null
Warum ist $1/x$ auf $(0,1]$ in jedem Punkt stetig, aber nicht gleichmäßig stetig?
---
Die größte Antwort $\delta_0=\frac{\varepsilon x_0^2}{1+\varepsilon x_0}$ schrumpft mit $x_0$ gegen 0; keine Antwort gewinnt überall. Für $x=\frac1n$, $y=\frac1{n+1}$ ist $|x-y|=\frac1{n(n+1)}\to0$, aber $|f(x)-f(y)|=1$.
--- falsch
Weil $1/x$ auf $(0,1]$ gar nicht stetig ist: Bei 0 wächst die Funktion über jede Grenze, und eine Funktion mit Pol ist an keiner Stelle ihres Definitionsbereichs stetig.
--- falsch
Weil $1/x$ fällt: Fallende Funktionen sind nie gleichmäßig stetig, weil sich ihr $\delta_0$ mit der Richtung ändert, in der man die Stelle verlässt.
--- falsch
Doch, sie ist gleichmäßig stetig: Das $\delta_0=\frac16$ aus der Stelle $x_0=\frac12$ passt für $\varepsilon=1$ an allen Stellen, weil $1/x$ überall dieselbe Form hat.
:::
:::karte formel Stetig auf einem abgeschlossenen Intervall ist gleichmäßig stetig
Was gilt nach dem Satz über stetige Funktionen $f:[a,b]\to\mathbb{R}$ für ihre Eingangstoleranzen, und warum scheitert $1/x$ auf $(0,1]$ daran?
---
$f$ ist auf $[a,b]$ gleichmäßig stetig: Eine Eingangstoleranz $\delta_0(\varepsilon)$ reicht für alle Stellen. Auf $(0,1]$ fehlt der Grenzpunkt 0, deshalb scheitert $1/x$.
--- falsch
$f$ ist auf $[a,b]$ gleichmäßig stetig, aber nur, wenn $f$ dort monoton wächst; $1/x$ scheitert auf $(0,1]$ deshalb, weil $1/x$ fällt statt zu wachsen.
--- falsch
$f$ braucht auch auf $[a,b]$ an jeder Stelle eine eigene Eingangstoleranz; gleichmäßig stetig sind nur lineare Funktionen, und $1/x$ ist nicht linear.
--- falsch
$f$ ist auf $[a,b]$ gleichmäßig stetig, und dasselbe gilt auf jedem Intervall; $1/x$ scheitert auf $(0,1]$ nur, weil $1/x$ bei 0 nicht stetig ist.
:::
:::karte herleitung Beweis der gleichmäßigen Stetigkeit
Wie beweist man indirekt, dass eine stetige Funktion $f:[a,b]\to\mathbb{R}$ gleichmäßig stetig ist?
---
Wäre $f$ nicht gleichmäßig stetig, gäbe es $\varepsilon_1>0$ und zu jedem $n$ Stellen $x_n,y_n\in[a,b]$ mit $|x_n-y_n|<\frac1n$ und $|f(x_n)-f(y_n)|\ge\varepsilon_1$, weil man die Definition verneint und $\delta_0=\frac1n$ einsetzt.
---
Bolzano-Weierstraß gibt eine Teilfolge $x_{n_k}\to\bar x\in[a,b]$, weil $\{x_n\}$ beschränkt ist und das Intervall abgeschlossen ist.
---
Auch $y_{n_k}\to\bar x$, weil $y_{n_k}=(y_{n_k}-x_{n_k})+x_{n_k}$ ist und der erste Summand eine Nullfolge ist.
---
Die Folgenstetigkeit gibt $f(x_{n_k})\to f(\bar x)$ und $f(y_{n_k})\to f(\bar x)$, also $|f(x_{n_k})-f(y_{n_k})|\to0$, weil beide Bildfolgen denselben Grenzwert haben.
---
Das widerspricht $|f(x_n)-f(y_n)|\ge\varepsilon_1$, weil eine Nullfolge nicht ständig mindestens $\varepsilon_1$ betragen kann.
:::
::::

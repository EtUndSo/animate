---
title: Stufe 2: Gerade, monoton, beschränkt
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Funktionen und Polynome
adresse: elektrotechnik/1-semester/hohere-mathematik-1/funktionen-und-polynome
knoten: Kapitel 3: Funktionen und Polynome
order: 1230400
summary: Die Definition sagt, was eine Funktion ist, aber nicht, wie sie aussieht.
tags: gerade, ungerade, monoton wachsend, streng monoton wachsend, monoton fallend, streng monoton fallend, beschränkt
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Die Definition sagt, was eine Funktion ist, aber nicht, wie sie aussieht. Drei Eigenschaften sparen Rechnung: Symmetrie halbiert die Arbeit, Monotonie ordnet die Werte, Beschränktheit begrenzt sie.
:::

**Die Idee.** Hängt $f(x)$ nur vom Abstand zur Null ab, sind die Werte links ein Spiegelbild der Werte rechts (Abb. [3](#abb-3)). Wächst $f$ mit $x$, folgt aus $x<y$ schon etwas über die Werte, ohne sie zu rechnen. Bleibt $f$ unter einer festen Zahl, kann nichts über alle Grenzen wachsen.

:::definition Definition 2.1 (Symmetrie, Monotonie, Beschränktheit)
<span class="anker" id="satz-2-1"></span>

Sei $f$ eine reelle Funktion. Enthält $\mathcal D(f)$ mit $x$ auch $-x$, so heißt $f$ __gerade__, falls $f(x)=f(-x)$ für alle $x\in\mathcal D(f)$, und __ungerade__, falls $f(x)=-f(-x)$ für alle $x\in\mathcal D(f)$. Weiter heißt $f$, jeweils für alle $x,y\in\mathcal D(f)$,

<ol class="rm">

<li>

__monoton wachsend__, falls aus $x<y$ folgt $f(x)\le f(y)$;

</li>

<li>

__streng monoton wachsend__, falls aus $x<y$ folgt $f(x)<f(y)$;

</li>

<li>

__monoton fallend__, falls aus $x<y$ folgt $f(x)\ge f(y)$;

</li>

<li>

__streng monoton fallend__, falls aus $x<y$ folgt $f(x)>f(y)$.

</li>

</ol>

$f$ heißt nach oben (unten) __beschränkt__, wenn es eine Zahl $K$ gibt mit $f(x)\le K$ ($f(x)\ge K$) für alle $x\in\mathcal D(f)$, also wenn die Menge $\mathcal W(f)$ nach oben (unten) beschränkt ist. Gilt beides, heißt $f$ beschränkt.
:::

⁠**So liest man das:** Gerade heißt: Der Graph geht durch Spiegeln an der $y$-Achse in sich über. Ungerade heißt: Er geht durch Punktspiegelung am Ursprung in sich über. Die Namen kommen von den Potenzen: $(-x)^{2n}=x^{2n}$ und $(-x)^{2n+1}=-x^{2n+1}$. Es genügt daher, die Werte auf $\mathcal D(f)\cap\mathbb{R}_0^+$ zu kennen, den Rest liefert die Spiegelung. Fallend und wachsend hängen zusammen: $f$ ist genau dann (streng) monoton fallend, wenn $-f$ (streng) monoton wachsend ist, denn Multiplikation mit $-1$ dreht die Ungleichung um.

:::abbildung hm1/k3eigenschaften 3
Links die gerade Glocke $b$: Die Werte bei $\pm1{,}5$ sind gleich. Mitte die ungerade Funktion $x^3-3x$: Die Werte bei $\pm1{,}5$ sind entgegengesetzt, $\mp1{,}125$. Rechts eine monoton wachsende Funktion mit waagerechtem Stück: Sie ist nicht streng monoton.
:::

:::satz Satz 2.2 (Potenzen sind monoton)
<span class="anker" id="satz-2-2"></span>

Sei $n\in\mathbb{N}$. Für ungerades $n$ ist $f(x)=x^n$ auf $\mathbb{R}$ streng monoton wachsend, für gerades $n$ auf $\mathbb{R}_0^+$.
:::

:::beweis Potenzen
⁠**Fall $0\le x<y$, jedes $n$:** Induktion über $n$. Für $n=1$ steht es da. Aus $x^n<y^n$ folgt $x^{n+1}=x\cdot x^n\le y\cdot x^n<y\cdot y^n=y^{n+1}$. Der erste Schritt benutzt $x<y$ und $x^n\ge0$, der zweite $y>0$. Das erledigt gerades $n$. **Fall $x<y\le0$, $n$ ungerade:** Es ist $0\le-y<-x$, nach dem ersten Fall $(-y)^n<(-x)^n$, und weil $n$ ungerade ist, $-y^n<-x^n$, also $x^n<y^n$. **Fall $x<0<y$, $n$ ungerade:** $x^n<0<y^n$.
:::

⁠**So liest man das:** $n$ ist die feste Potenz. **Warum „auf $\mathbb{R}_0^+$“ nötig ist:** Für gerades $n$ ist $f$ auf ganz $\mathbb{R}$ nicht monoton, es ist $-2<-1$, aber $(-2)^2>(-1)^2$.

::::beispiel [Beispiele]
$h$ ist nach unten durch $-1$ beschränkt, nach oben nicht. Die Glocke ist beschränkt und auf $\mathbb{R}_0^+$ streng fallend: Aus $0\le x<y$ folgt $1+x^2<1+y^2$, also $b(x)>b(y)$. Summe und Produkt beschränkter Funktionen sind wieder beschränkt: Aus $|f|\le K$ und $|g|\le L$ folgt $|f+g|\le K+L$ und $|f\cdot g|\le K\,L$.
::::

⁠**Grenzfälle:** Eine konstante Funktion ist monoton wachsend und fallend zugleich, aber nicht streng. $f(x)=0$ ist gerade und ungerade zugleich.

:::frage Ist eine Funktion, die nicht gerade ist, automatisch ungerade?
Bei Zahlen stimmt das, bei Funktionen nicht: $f(x)=x^2+x$ hat $f(1)=2$ und $f(-1)=0$: weder gleich noch entgegengesetzt. Die meisten Funktionen sind beides nicht.
:::

:::aufgabe Aufgabe 2 ★★ Symmetrie und Schranken
<span class="anker" id="aufg-2"></span>

(a) Gerade, ungerade oder keins: $f_1(x)=x^4-3x^2$, $f_2(x)=x^3+x$, $f_3(x)=x^2+x$, $f_4(x)=x\,|x|$? (b) Zeige: Das Produkt zweier ungerader Funktionen ist gerade. (c) Bestimme für $v(x)=3/(2+x^2)$ Schranken und den Wertebereich, und zeige, dass $v$ auf $\mathbb{R}_0^+$ streng monoton fällt.

:::loesung
(a) $f_1(-x)=f_1(x)$: gerade. $f_2(-x)=-x^3-x=-f_2(x)$: ungerade. $f_3(1)=2$, $f_3(-1)=0$: keins. $f_4(-x)=-x\,|x|=-f_4(x)$: ungerade. (b) Mit $f(-x)=-f(x)$ und $g(-x)=-g(x)$ ist $(f\cdot g)(-x)=(-f(x))(-g(x))=(f\cdot g)(x)$. (c) Wegen $2+x^2\ge2$ ist $0<v(x)\le\frac32$. Jedes $y\in(0,\frac32]$ wird von $x=\sqrt{3/y-2}$ getroffen, also $\mathcal W(v)=(0,\frac32]$. Für $0\le x<y$ wächst der Nenner, der Bruch fällt.
:::
:::

::::formelsammlung
**Gerade und ungerade**

$$f(x)=f(-x),\qquad f(x)=-f(-x)$$

Jeweils für alle $x\in\mathcal D(f)$, wenn $\mathcal D(f)$ mit $x$ auch $-x$ enthält. Gerade: Spiegelung an der $y$-Achse; ungerade: Punktspiegelung am Ursprung. Die Namen kommen von $(-x)^{2n}=x^{2n}$ und $(-x)^{2n+1}=-x^{2n+1}$.

**Monoton wachsend und monoton fallend**

$$x<y\ \Rightarrow\ f(x)\le f(y),\qquad x<y\ \Rightarrow\ f(x)\ge f(y)$$

Jeweils für alle $x,y\in\mathcal D(f)$. $f$ ist genau dann (streng) monoton fallend, wenn $-f$ (streng) monoton wachsend ist; eine konstante Funktion ist beides, aber nicht streng.

**Streng monoton wachsend und streng monoton fallend**

$$x<y\Rightarrow f(x)<f(y),\qquad x<y\Rightarrow f(x)>f(y)$$

Jeweils für alle $x,y\in\mathcal D(f)$; gleiche Werte an verschiedenen Stellen kommen nicht vor.

**Beschränkt**

$$f(x)\le K,\qquad f(x)\ge K$$

Nach oben bzw. nach unten beschränkt, wenn es eine Zahl $K$ gibt, mit der das für alle $x\in\mathcal D(f)$ gilt, also wenn $\mathcal W(f)$ nach oben bzw. unten beschränkt ist. Gilt beides, heißt $f$ beschränkt, kurz $|f|\le K$.

**Potenzen sind monoton**

$$0\le x<y\ \Rightarrow\ x^n<y^n$$

Für jedes $n\in\mathbb{N}$: $f(x)=x^n$ ist auf $\mathbb{R}_0^+$ streng monoton wachsend, für ungerades $n$ sogar auf $\mathbb{R}$. Für gerades $n$ nicht auf ganz $\mathbb{R}$: $-2<-1$, aber $(-2)^2>(-1)^2$.

**Summe und Produkt beschränkter Funktionen**

$$|f+g|\le K+L,\qquad|f\cdot g|\le K\,L$$

Aus $|f|\le K$ und $|g|\le L$.
::::

::::lernkarten
:::karte begriff gerade
Wann heißt eine reelle Funktion $f$ gerade, und was muss dafür ihr Definitionsbereich erfüllen?
---
Wenn $\mathcal D(f)$ mit $x$ auch $-x$ enthält und $f(x)=f(-x)$ für alle $x\in\mathcal D(f)$ gilt. Der Graph geht dann durch Spiegeln an der $y$-Achse in sich über.
--- falsch
Wenn $\mathcal D(f)$ mit $x$ auch $-x$ enthält und $f(x)=-f(-x)$ für alle $x\in\mathcal D(f)$ gilt. Der Graph geht dann durch Spiegeln an der $y$-Achse in sich über.
--- falsch
Wenn ihr Graph eine Gerade ist, also $f(x)=ax+b$ gilt. Der Definitionsbereich muss dafür ein Intervall sein, damit die Gerade nirgends unterbrochen ist.
--- falsch
Wenn $f(x)=f(-x)$ für alle $x\ge0$ gilt; der Definitionsbereich darf dabei beliebig sein, etwa $[0,\infty)$. Der Graph geht dann durch Punktspiegelung am Ursprung in sich über.
:::
:::karte begriff ungerade
Wann heißt eine reelle Funktion $f$ ungerade, und welche Symmetrie hat dann ihr Graph?
---
Wenn $\mathcal D(f)$ mit $x$ auch $-x$ enthält und $f(x)=-f(-x)$ für alle $x\in\mathcal D(f)$ gilt. Der Graph geht dann durch Punktspiegelung am Ursprung in sich über.
--- falsch
Wenn $\mathcal D(f)$ mit $x$ auch $-x$ enthält und $f(x)=-f(-x)$ für alle $x\in\mathcal D(f)$ gilt. Der Graph geht dann durch Spiegeln an der $x$-Achse in sich über.
--- falsch
Wenn $f$ nicht gerade ist, also $f(x)\neq f(-x)$ für mindestens ein $x$ gilt. Jede reelle Funktion ist damit entweder gerade oder ungerade, wie jede ganze Zahl.
--- falsch
Wenn $f(x)=-f(x)$ für alle $x\in\mathcal D(f)$ gilt, ohne Bedingung an den Definitionsbereich. Der Graph geht dann durch Spiegeln an der $y$-Achse in sich über.
:::
:::karte begriff monoton wachsend und monoton fallend
Wann heißt eine reelle Funktion $f$ monoton wachsend, und wann heißt sie monoton fallend?
---
Monoton wachsend, falls für alle $x,y\in\mathcal D(f)$ aus $x<y$ folgt $f(x)\le f(y)$; monoton fallend, falls aus $x<y$ folgt $f(x)\ge f(y)$. Gleiche Werte sind dabei erlaubt.
--- falsch
Monoton wachsend, falls für alle $x,y\in\mathcal D(f)$ aus $x<y$ folgt $f(x)<f(y)$; monoton fallend, falls aus $x<y$ folgt $f(x)>f(y)$. Gleiche Werte an verschiedenen Stellen sind verboten.
--- falsch
Monoton wachsend, falls $f(x)\ge0$ für alle $x\in\mathcal D(f)$ gilt; monoton fallend, falls $f(x)\le0$ für alle $x$ gilt. Es kommt also nur auf das Vorzeichen der Werte an.
--- falsch
Monoton wachsend, falls es zwei Stellen $x<y$ mit $f(x)\le f(y)$ gibt; monoton fallend, falls es zwei Stellen $x<y$ mit $f(x)\ge f(y)$ gibt. Eine Funktion kann beides sein.
:::
:::karte begriff streng monoton wachsend und streng monoton fallend
Wann heißt eine reelle Funktion $f$ streng monoton wachsend, und wann heißt sie streng monoton fallend?
---
Streng monoton wachsend, falls für alle $x,y\in\mathcal D(f)$ aus $x<y$ folgt $f(x)<f(y)$; streng monoton fallend, falls aus $x<y$ folgt $f(x)>f(y)$. Gleiche Werte kommen nicht vor.
--- falsch
Streng monoton wachsend, falls für alle $x,y\in\mathcal D(f)$ aus $x<y$ folgt $f(x)\le f(y)$; streng monoton fallend, falls daraus $f(x)\ge f(y)$ folgt. „Streng“ betont nur, dass es für alle $x,y$ gilt.
--- falsch
Streng monoton wachsend, falls $f$ monoton wächst und über alle Grenzen wächst; streng monoton fallend, falls $f$ monoton fällt und unter jede Grenze sinkt. Beschränkte Funktionen sind nie streng monoton.
--- falsch
Streng monoton wachsend, falls aus $x<y$ folgt $f(x)<f(y)$, aber nur für benachbarte ganze Zahlen $x$ und $y=x+1$; streng monoton fallend entsprechend mit $f(x)>f(y)$.
:::
:::karte zusammenhang beschränkt
Was bedeutet es, dass eine reelle Funktion $f$ beschränkt ist, und wie hängt das mit der Beschränktheit von Mengen zusammen?
---
$f$ heißt nach oben (unten) beschränkt, wenn es eine Zahl $K$ gibt mit $f(x)\le K$ ($f(x)\ge K$) für alle $x\in\mathcal D(f)$, also wenn die Menge $\mathcal W(f)$ so beschränkt ist; gilt beides, heißt $f$ beschränkt.
--- falsch
$f$ heißt beschränkt, wenn ihr Definitionsbereich $\mathcal D(f)$ eine beschränkte Menge ist, etwa ein Intervall $[a,b]$. Auf einem unbeschränkten Definitionsbereich wie $\mathbb{R}$ ist $f$ nie beschränkt.
--- falsch
$f$ heißt nach oben beschränkt, wenn es zu jedem $x\in\mathcal D(f)$ eine Zahl $K$ mit $f(x)\le K$ gibt; das trifft auf jede reelle Funktion zu, weil $f(x)$ selbst eine solche Zahl ist.
--- falsch
$f$ heißt beschränkt, wenn sie einen größten und einen kleinsten Wert annimmt. Die Glocke $b$ ist deshalb nicht beschränkt, weil sie den Wert $0$ nie erreicht.
:::
:::karte formel Potenzen sind monoton
Auf welchen Mengen ist die Potenzfunktion $f(x)=x^n$ mit $n\in\mathbb{N}$ streng monoton wachsend?
---
Für ungerades $n$ ist $f(x)=x^n$ auf $\mathbb{R}$ streng monoton wachsend, für gerades $n$ auf $\mathbb{R}_0^+$. Auf ganz $\mathbb{R}$ geht das für gerades $n$ nicht: $-2<-1$, aber $(-2)^2>(-1)^2$.
--- falsch
Für jedes $n\in\mathbb{N}$ ist $f(x)=x^n$ auf ganz $\mathbb{R}$ streng monoton wachsend, denn aus $x<y$ folgt durch Potenzieren $x^n<y^n$; das Potenzieren erhält jede Ungleichung.
--- falsch
Für gerades $n$ ist $f(x)=x^n$ auf $\mathbb{R}$ streng monoton wachsend, für ungerades $n$ nur auf $\mathbb{R}_0^+$, weil ungerade Potenzen negativer Zahlen negativ werden.
--- falsch
Für jedes $n\in\mathbb{N}$ ist $f(x)=x^n$ nur auf $\mathbb{R}_0^+$ streng monoton wachsend. Auf den negativen Zahlen fallen alle Potenzen, auch die ungeraden, weil dort jedes Minus eine Ungleichung umdreht.
:::
:::karte herleitung Potenzen sind monoton
Wie zeigt man, dass aus $0\le x<y$ für jedes $n\in\mathbb{N}$ die Ungleichung $x^n<y^n$ folgt, und wie überträgt man das für ungerades $n$ auf ganz $\mathbb{R}$?
---
Für $n=1$ ist $x^n<y^n$ die Voraussetzung $x<y$ selbst, weil die erste Potenz die Zahl selbst ist; das ist der Induktionsanfang.
---
Aus $x^n<y^n$ folgt $x^{n+1}=x\cdot x^n\le y\cdot x^n<y\cdot y^n=y^{n+1}$, weil $x<y$ und $x^n\ge0$ den ersten und $y>0$ den zweiten Schritt tragen.
---
Für $x<y\le0$ und ungerades $n$ ist $0\le-y<-x$, nach dem ersten Fall also $(-y)^n<(-x)^n$; weil $n$ ungerade ist, heißt das $-y^n<-x^n$, also $x^n<y^n$.
---
Für $x<0<y$ und ungerades $n$ gilt $x^n<0<y^n$, weil eine ungerade Potenz das Vorzeichen ihrer Grundzahl behält.
:::
:::karte zusammenhang wachsend und fallend
Warum ist eine reelle Funktion $f$ genau dann (streng) monoton fallend, wenn $-f$ (streng) monoton wachsend ist?
---
Weil Multiplikation mit $-1$ jede Ungleichung umdreht: Aus $f(x)\ge f(y)$ wird $-f(x)\le-f(y)$, aus $f(x)>f(y)$ wird $-f(x)<-f(y)$. Fallen und Wachsen tauschen also die Rollen.
--- falsch
Weil $-f$ der an der $y$-Achse gespiegelte Graph von $f$ ist: Spiegeln vertauscht links und rechts, und was nach rechts fällt, wächst nach dem Spiegeln nach rechts.
--- falsch
Weil $-f$ dieselben Werte wie $f$ hat, nur in umgekehrter Reihenfolge durchlaufen; die Monotonie hängt allein von der Menge der Werte ab, nicht von ihrem Vorzeichen.
--- falsch
Weil Multiplikation mit $-1$ eine Ungleichung erhält, solange sie streng ist: Aus $f(x)>f(y)$ wird $-f(x)>-f(y)$; nur eine Ungleichung mit $\ge$ dreht sich dabei um.
:::
:::karte zusammenhang konstant und monoton
Warum ist eine konstante Funktion monoton wachsend und monoton fallend zugleich, aber nicht streng monoton?
---
Weil stets $f(x)=f(y)$ gilt: Das erfüllt $f(x)\le f(y)$ und $f(x)\ge f(y)$, aber weder $f(x)<f(y)$ noch $f(x)>f(y)$. Gleiche Werte erlaubt nur die einfache Monotonie.
--- falsch
Weil sie an jeder Stelle denselben Wert hat und deshalb gerade ist: Gerade Funktionen sind immer wachsend und fallend zugleich, streng monoton sind dagegen nur die ungeraden.
--- falsch
Weil $f(x)=f(y)$ sowohl $f(x)<f(y)$ als auch $f(x)>f(y)$ erfüllt, solange $x\neq y$ ist. Streng monoton ist sie nicht, weil sie dafür über alle Grenzen wachsen müsste.
--- falsch
Weil die Definition der Monotonie nur für Funktionen mit mindestens zwei verschiedenen Werten gilt; für alle anderen gilt sie automatisch, die strenge Monotonie dagegen nie.
:::
:::karte zusammenhang weder gerade noch ungerade
Ist eine reelle Funktion, die nicht gerade ist, automatisch ungerade?
---
Nein. $f(x)=x^2+x$ hat $f(1)=2$ und $f(-1)=0$, die Werte sind weder gleich noch entgegengesetzt; die meisten Funktionen sind beides nicht. $f(x)=0$ ist sogar beides zugleich.
--- falsch
Ja. Bei jeder Funktion ist entweder $f(-x)=f(x)$ oder $f(-x)=-f(x)$, denn $f(-x)$ kann sich von $f(x)$ nur im Vorzeichen unterscheiden, wie bei geraden und ungeraden Zahlen.
--- falsch
Ja, sofern ihr Definitionsbereich mit $x$ auch $-x$ enthält. Nur Funktionen auf unsymmetrischen Bereichen wie $[0,\infty)$ können weder gerade noch ungerade sein.
--- falsch
Nein, aber nur wegen der Null: Bis auf $f(x)=0$, die weder gerade noch ungerade ist, ist jede Funktion auf $\mathbb{R}$ entweder gerade oder ungerade.
:::
:::karte zusammenhang Namen gerade und ungerade
Woher haben gerade und ungerade Funktionen ihren Namen, und warum genügt es, ihre Werte für $x\ge0$ zu kennen?
---
Von den Potenzen: $(-x)^{2n}=x^{2n}$ und $(-x)^{2n+1}=-x^{2n+1}$. Die Werte auf $\mathcal D(f)\cap\mathbb{R}_0^+$ genügen, weil die Spiegelung an der $y$-Achse bzw. am Ursprung den Rest liefert.
--- falsch
Von den Potenzen: $(-x)^{2n}=-x^{2n}$ und $(-x)^{2n+1}=x^{2n+1}$. Die Werte für $x\ge0$ genügen, weil man die übrigen durch Verschieben des Graphen nach links erhält.
--- falsch
Von der Spiegelung: Gerade heißt, dass man den Graphen an einer Geraden spiegelt, ungerade, dass man an einem Punkt spiegelt. Die Werte für $x\ge0$ genügen nur bei geraden Funktionen.
--- falsch
Von den Potenzen: $(-x)^{2n}=x^{2n}$ und $(-x)^{2n+1}=-x^{2n+1}$. Die Werte für $x\ge0$ genügen aber nur bei Polynomen, weil nur deren Werte sich aus Potenzen zusammensetzen.
:::
:::karte formel Summe und Produkt beschränkter Funktionen
Welche Schranken haben Summe und Produkt zweier beschränkter Funktionen mit $|f|\le K$ und $|g|\le L$?
---
$|f+g|\le K+L$ und $|f\cdot g|\le K\,L$. Summe und Produkt beschränkter Funktionen sind also wieder beschränkt; die Schranken addieren bzw. multiplizieren sich.
--- falsch
$|f+g|\le K+L$ und $|f\cdot g|\le K+L$. Summe und Produkt beschränkter Funktionen sind also wieder beschränkt, und zwar beide mit derselben Schranke.
--- falsch
$|f+g|\le\max(K,L)$ und $|f\cdot g|\le K\,L$. Die Summe ist höchstens so groß wie die größere der beiden Schranken, das Produkt wie deren Produkt.
--- falsch
$|f+g|\le K+L$; das Produkt ist dagegen im Allgemeinen nicht beschränkt: Zwei beschränkte Faktoren können zusammen über jede Grenze wachsen.
:::
:::karte zusammenhang Glocke fällt
Warum ist die Glocke $b(x)=1/(1+x^2)$ auf $\mathbb{R}_0^+$ streng monoton fallend und zugleich beschränkt?
---
Aus $0\le x<y$ folgt $1+x^2<1+y^2$, also $b(x)>b(y)$, denn ein größerer positiver Nenner ergibt einen kleineren Bruch. Wegen $1+x^2\ge1$ gilt außerdem $0<b(x)\le1$.
--- falsch
Weil ihr Zähler konstant $1$ ist: Funktionen mit konstantem Zähler fallen immer streng. Beschränkt ist sie, weil ihr Definitionsbereich $\mathbb{R}_0^+$ nach unten durch $0$ beschränkt ist.
--- falsch
Aus $0\le x<y$ folgt $1+x^2<1+y^2$, also $b(x)<b(y)$, denn der Nenner wächst. Beschränkt ist sie nur nach unten, durch $0$, weil sie für große $x$ beliebig groß wird.
--- falsch
Weil sie gerade ist: Jede gerade Funktion fällt rechts von null streng, wenn sie links davon wächst. Beschränkt ist sie wegen $1+x^2\ge1$, also $0<b(x)\le1$.
:::
::::

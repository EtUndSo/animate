---
title: Stufe 5: Vollständige Induktion, Summe und Produkt
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Mengen, Logik und reelle Zahlen
adresse: elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen
knoten: Kapitel 1: Mengen, Logik und reelle Zahlen
order: 1210700
summary: Aussagen über alle ninmathbb N lassen sich nicht durch Probieren beweisen.
tags: Induktionsanfang, Induktionsschritt, Induktionsvoraussetzung, Induktionsschluss
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Aussagen über alle $n\in\mathbb{N}$ lassen sich nicht durch Probieren beweisen. Diese Stufe liefert das Verfahren und damit eine saubere Definition von Summe, Produkt und Potenz.
:::

**Die Idee.** Jede natürliche Zahl entsteht aus der 1 durch wiederholtes Weiterzählen. Zeigt man eine Aussage für die 1 und zeigt man, dass sie sich von jedem $n$ auf $n+1$ überträgt, dann erreicht die Kette jede Zahl (Abb. [5](#abb-5)).

:::satz Satz 5.1 (Vollständige Induktion)
<span class="anker" id="satz-5-1"></span>

$\mathcal A(n)$ seien Aussagen mit $n\in\mathbb{N}$. Ist (1) $\mathcal A(1)$ wahr (__Induktionsanfang__) und (2) für beliebiges $n$ die Implikation $\mathcal A(n)\Rightarrow\mathcal A(n+1)$ wahr (__Induktionsschritt__, $\mathcal A(n)$ heißt __Induktionsvoraussetzung__), dann ist $\mathcal A(n)$ für alle $n\in\mathbb{N}$ wahr (__Induktionsschluss__).

⁠**Zweite Version:** Sei $n_0\in\mathbb{N}$ fest. Ist $\mathcal A(n_0)$ wahr und gilt für jedes $n\ge n_0$

$$\bigl(\mathcal A(n_0)\wedge\mathcal A(n_0+1)\wedge\dots\wedge\mathcal A(n)\bigr)\Rightarrow\mathcal A(n+1),$$

dann ist $\mathcal A(n)$ für alle $n\ge n_0$ wahr.
:::

⁠**So liest man das:** Die zweite Version erlaubt einen späteren Start und alle früheren Fälle als Voraussetzung. **Warum beide Teile:** Ohne Anfang: $\mathcal A(n):=(n=n+1)$ hat einen gültigen Schritt (auf beiden Seiten 1 addieren), ist aber immer falsch. Ohne Schritt: $n^2-n+41$ ist für $n=1,\dots,40$ eine Primzahl, für $n=41$ aber $41^2$.

:::frage Setzt man im Schritt nicht voraus, was man beweisen will?
Nein. Man setzt $\mathcal A(n)$ für ein beliebiges, aber festes $n$ voraus und zeigt nur die Implikation $\mathcal A(n)\Rightarrow\mathcal A(n+1)$. Dass $\mathcal A(n)$ wahr ist, folgt erst aus dem Anfang und der Kette.
:::

:::beweis Warum Induktion gilt
$\mathbb{N}$ hat die Eigenschaft: Ist $M\subset\mathbb{N}$ mit $1\in M$ und folgt aus $n\in M$ stets $n+1\in M$, dann ist $M=\mathbb{N}$. Das ist der Aufbau von $\mathbb{N}$ selbst. Man setzt $M:=\{n\in\mathbb{N}:\mathcal A(n)\text{ wahr}\}$. Für die zweite Version sei $\mathcal B(n):=\mathcal A(n_0)\wedge\dots\wedge\mathcal A(n)$. Dann folgt aus der Voraussetzung $\mathcal B(n)\Rightarrow\mathcal B(n+1)$, und dieselbe Eigenschaft von $\mathbb{N}$, gestartet bei $n_0$, gibt $\mathcal B(n)$ für alle $n\ge n_0$.
:::

:::definition Definition 5.2 (Summe, Produkt, Potenz: rekursiv)
<span class="anker" id="satz-5-2"></span>

Für $x_1,x_2,\ldots\in\mathbb K$ setzt man

<span class="anker" id="gl-5-1"></span>
$$\sum_{i=1}^{1}x_i:=x_1,\quad\sum_{i=1}^{n+1}x_i:=\Bigl(\sum_{i=1}^{n}x_i\Bigr)+x_{n+1},\qquad \prod_{i=1}^{1}x_i:=x_1,\quad\prod_{i=1}^{n+1}x_i:=\Bigl(\prod_{i=1}^{n}x_i\Bigr)\cdot x_{n+1}. \tag{5.1}$$

Sind alle $x_i=x$, dann ist $x^n:=\prod_{i=1}^nx$. Für $x\ne0$ und $n\in\mathbb{N}$ setzt man $x^0:=1$ und $x^{-n}:=(x^n)^{-1}=(\frac1x)^n$. Zudem ist $n!:=\prod_{i=1}^ni$ und $0^0:=1$.
:::

⁠**So liest man das:** $\sum_{i=1}^nx_i=x_1+\dots+x_n$, die Pünktchen sind nun durch die Rekursion erklärt, nach Satz [5.1](#satz-5-1) ist der Wert für jedes $n$ festgelegt. $x^0:=1$ ist erzwungen, weil $x^n\cdot x^0=x^{n+0}$ gelten soll. $0^0:=1$ ist eine Festlegung: Damit setzt sich $x^0=1$ bei $x=0$ fort, und $(x+y)^2=x^2y^0+2x^1y^1+x^0y^2$ bleibt für $x=0$ oder $y=0$ richtig.

:::satz Satz 5.3 (Rechenregeln für Summe, Produkt, Potenz)
<span class="anker" id="satz-5-3"></span>

In jedem Körper gilt:

<ol class="rm">

<li>

Der Wert von $\sum_{i=1}^nx_i$ und $\prod_{i=1}^nx_i$ hängt nicht von der Reihenfolge der $x_i$ ab.

</li>

<li>

Produkt von Summen: $\Bigl(\sum_{i=1}^nx_i\Bigr)\Bigl(\sum_{j=1}^Ny_j\Bigr)=\sum_{i=1}^n\Bigl(\sum_{j=1}^Nx_iy_j\Bigr)$.

</li>

<li>

Potenzgesetze für $x,y\ne0$, $p,q\in\mathbb{Z}$: $x^px^q=x^{p+q}$, $(x^p)^q=x^{p\cdot q}$, $(xy)^p=x^py^p$.

</li>

</ol>
:::

⁠**So liest man das:** (i) ist die Induktion über (A1), (A2), (M1), (M2). (ii) sagt „jeder mit jedem“, das ist (AM) wiederholt. Für $p,q\in\mathbb{N}$ ist (iii) Umnummerieren: $x^px^q=\prod_{i=1}^{p+q}x=x^{p+q}$. **Warum $x\ne0$:** $0^{-1}$ gibt es nicht, für $x=0$ sind nur Exponenten $n\ge0$ erlaubt, und $0^n=0$ für $n\ge1$. Für $x,y>0$ gelten die Gesetze auch mit rationalen Exponenten, etwa $x^{1/2}=\sqrt x$ ([Kapitel 5](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/exponentialfunktion-und-stetigkeit/exponentialfunktion-und-stetigkeit.html)).

:::abbildung hm1/k1induktion 5
Links ist jede Farbe ein Winkelstück. Rechts der Induktionsschritt: $n^2$ wächst um $2n+1$ Felder.
:::

::::beispiel [Beispiel 1] Summe der ungeraden Zahlen
Behauptung: $\sum_{i=1}^n(2i-1)=n^2$. **Anfang:** $2\cdot1-1=1=1^2$. **Schritt:** Gilt die Formel für $n$, dann ist $\sum_{i=1}^{n+1}(2i-1)=n^2+2(n+1)-1=n^2+2n+1=(n+1)^2$. **Schluss:** Sie gilt für alle $n$. Ebenso beweist man $\sum_{i=1}^ni=\frac{n(n+1)}2$ und $\sum_{i=1}^ni^3=\frac{n^2(n+1)^2}4$ (Aufgabe [6](#aufg-6)).
::::

::::beispiel [Beispiel 2] später Start
$n!>2^n$ für $n\ge n_0=4$. Anfang: $24>16$. Schritt: $(n+1)!=(n+1)\,n!>(n+1)\,2^n\ge2\cdot2^n$, denn $n+1\ge2$.
::::

⁠**Grenzfall:** Für $n=3$ ist $6<8$, der Start bei 4 ist nötig.

::::beispiel [Beispiel 3] alle früheren Fälle
Jedes $n\ge2$ ist ein Produkt von Primzahlen. Anfang: 2 ist prim. Schritt: Ist $n+1$ nicht prim, ist $n+1=ab$ mit $2\le a,b\le n$. Hier reicht $\mathcal A(n)$ allein nicht, man braucht $\mathcal A(a)$ und $\mathcal A(b)$.
::::

:::aufgabe Aufgabe 6 ★★ Induktion üben
<span class="anker" id="aufg-6"></span>

<ol class="al">

<li>

Beweise $\sum_{i=1}^ni^3=\frac{n^2(n+1)^2}4$ und prüfe $n=3$.

</li>

<li>

Berechne $\prod_{i=1}^5(1+\frac1i)$. Sage die Formel für $\prod_{i=1}^n(1+\frac1i)$ voraus und beweise sie.

</li>

<li>

Finde den Fehler: „Alle Kabel haben dieselbe Farbe. Anfang: Ein Kabel hat eine Farbe. Schritt: Von $n+1$ Kabeln nimm eines weg, die übrigen $n$ sind gleichfarbig. Nimm ein anderes weg, ebenso. Also sind alle gleichfarbig.“

</li>

</ol>

:::loesung
(a) Anfang: $1=\frac{1\cdot4}4$. Schritt: $\frac{n^2(n+1)^2}4+(n+1)^3=\frac{(n+1)^2(n^2+4n+4)}4=\frac{(n+1)^2(n+2)^2}4$. Prüfung: $1+8+27=36=\frac{9\cdot16}4$. (b) $2\cdot\frac32\cdot\frac43\cdot\frac54\cdot\frac65=6$. Vermutung: $n+1$. Anfang: $1+\frac11=2$. Schritt: $(n+1)(1+\frac1{n+1})=n+2$. (c) Der Schritt scheitert bei $n=1$: Von zwei Kabeln bleibt nach dem Wegnehmen je ein anderes übrig, die Reste haben kein gemeinsames Kabel. Der Schritt muss für jedes $n$ gelten.
:::
:::

::::formelsammlung
**Vollständige Induktion**

$$\mathcal A(1)\ \text{wahr}\quad\text{und}\quad\mathcal A(n)\Rightarrow\mathcal A(n+1)\ \text{für beliebiges}\ n\qquad\Longrightarrow\qquad\mathcal A(n)\ \text{wahr für alle}\ n\in\mathbb{N}$$

Induktionsanfang $\mathcal A(1)$, Induktionsschritt mit der Induktionsvoraussetzung $\mathcal A(n)$, Induktionsschluss. Grundlage ist der Aufbau von $\mathbb{N}$: Ist $M\subset\mathbb{N}$ mit $1\in M$ und folgt aus $n\in M$ stets $n+1\in M$, dann ist $M=\mathbb{N}$.

**Zweite Version der Induktion**

$$\bigl(\mathcal A(n_0)\wedge\mathcal A(n_0+1)\wedge\dots\wedge\mathcal A(n)\bigr)\Rightarrow\mathcal A(n+1)$$

Gilt das für jedes $n\ge n_0$ und ist $\mathcal A(n_0)$ wahr, dann ist $\mathcal A(n)$ für alle $n\ge n_0$ wahr: späterer Start und alle früheren Fälle als Voraussetzung.

**Summe und Produkt, rekursiv**

$$\sum_{i=1}^{1}x_i:=x_1,\quad\sum_{i=1}^{n+1}x_i:=\Bigl(\sum_{i=1}^{n}x_i\Bigr)+x_{n+1},\qquad\prod_{i=1}^{1}x_i:=x_1,\quad\prod_{i=1}^{n+1}x_i:=\Bigl(\prod_{i=1}^{n}x_i\Bigr)\cdot x_{n+1}$$

Für $x_1,x_2,\ldots\in\mathbb K$. Der Wert hängt nicht von der Reihenfolge der $x_i$ ab.

**Potenz und Fakultät**

$$x^n:=\prod_{i=1}^nx,\qquad x^0:=1,\qquad x^{-n}:=(x^n)^{-1}=(\frac1x)^n,\qquad n!:=\prod_{i=1}^ni,\qquad0^0:=1$$

$x^0$ und $x^{-n}$ für $x\ne0$ und $n\in\mathbb{N}$. $x^0:=1$ ist erzwungen, weil $x^n\cdot x^0=x^{n+0}$ gelten soll; $0^0:=1$ ist eine Festlegung.

**Produkt von Summen**

$$\Bigl(\sum_{i=1}^nx_i\Bigr)\Bigl(\sum_{j=1}^Ny_j\Bigr)=\sum_{i=1}^n\Bigl(\sum_{j=1}^Nx_iy_j\Bigr)$$

„Jeder mit jedem“: das wiederholte Distributivgesetz.

**Potenzgesetze**

$$x^px^q=x^{p+q},\qquad(x^p)^q=x^{p\cdot q},\qquad(xy)^p=x^py^p$$

Für $x,y\ne0$ und $p,q\in\mathbb{Z}$. Für $x=0$ sind nur Exponenten $n\ge0$ erlaubt, und $0^n=0$ für $n\ge1$.

**Summenformeln**

$$\sum_{i=1}^n(2i-1)=n^2,\qquad\sum_{i=1}^ni=\frac{n(n+1)}2,\qquad\sum_{i=1}^ni^3=\frac{n^2(n+1)^2}4$$

Für alle $n\in\mathbb{N}$, jeweils durch Induktion bewiesen.
::::

::::lernkarten
:::karte begriff vollständige Induktion
Was ist die vollständige Induktion, und welche zwei Teile braucht ein Beweis damit?
---
Ein Beweisverfahren für Aussagen $\mathcal A(n)$ über alle $n\in\mathbb{N}$: Ist $\mathcal A(1)$ wahr und für beliebiges $n$ die Implikation $\mathcal A(n)\Rightarrow\mathcal A(n+1)$ wahr, dann ist $\mathcal A(n)$ für alle $n\in\mathbb{N}$ wahr.
--- falsch
Ein Beweisverfahren für Aussagen $\mathcal A(n)$ über alle $n\in\mathbb{N}$: Ist $\mathcal A(n)$ für $n=1,\dots,10$ wahr, dann ist es nach dem Muster der ersten Fälle auch für alle weiteren $n$ wahr.
--- falsch
Ein Beweisverfahren für Aussagen $\mathcal A(n)$ über alle $n\in\mathbb{N}$: Ist für beliebiges $n$ die Implikation $\mathcal A(n)\Rightarrow\mathcal A(n+1)$ wahr, dann ist $\mathcal A(n)$ für alle $n\in\mathbb{N}$ wahr; ein Anfang ist nicht nötig.
--- falsch
Ein Beweisverfahren für Aussagen $\mathcal A(n)$ über alle $n\in\mathbb{N}$: Ist $\mathcal A(1)$ wahr und für beliebiges $n$ die Implikation $\mathcal A(n+1)\Rightarrow\mathcal A(n)$ wahr, dann ist $\mathcal A(n)$ für alle $n\in\mathbb{N}$ wahr.
:::
:::karte begriff Induktionsanfang und Induktionsschluss
Was sind Induktionsanfang und Induktionsschluss in einem Beweis durch vollständige Induktion?
---
Der Induktionsanfang ist der Nachweis, dass $\mathcal A(1)$ wahr ist, bei späterem Start $\mathcal A(n_0)$. Der Induktionsschluss ist die Folgerung, dass $\mathcal A(n)$ dann für alle $n\in\mathbb{N}$ wahr ist, bei späterem Start für alle $n\ge n_0$.
--- falsch
Der Induktionsanfang ist die Annahme, dass $\mathcal A(n)$ für ein festes $n$ wahr ist. Der Induktionsschluss ist der Nachweis, dass daraus die Aussage $\mathcal A(n+1)$ für die nächste Zahl folgt.
--- falsch
Der Induktionsanfang ist der Nachweis, dass $\mathcal A(1)$ wahr ist. Der Induktionsschluss ist der Nachweis für die letzte Zahl $n$, bis zu der die Aussage gelten soll, damit die Kette dort endet.
--- falsch
Der Induktionsanfang ist der Nachweis für die kleinste Zahl, für die die Aussage falsch ist. Der Induktionsschluss zeigt dann, dass ab dort auch alle weiteren Fälle falsch sind.
:::
:::karte begriff Induktionsschritt und Induktionsvoraussetzung
Was zeigt man im Induktionsschritt, und welche Rolle spielt dabei die Induktionsvoraussetzung?
---
Im Induktionsschritt zeigt man für beliebiges $n$ die Implikation $\mathcal A(n)\Rightarrow\mathcal A(n+1)$. Die Induktionsvoraussetzung ist $\mathcal A(n)$; man setzt sie für ein beliebiges, aber festes $n$ voraus.
--- falsch
Im Induktionsschritt zeigt man, dass $\mathcal A(n)$ für alle $n$ wahr ist. Die Induktionsvoraussetzung ist genau diese Behauptung, die man dafür als schon bekannt voraussetzt.
--- falsch
Im Induktionsschritt zeigt man für beliebiges $n$ die Implikation $\mathcal A(n+1)\Rightarrow\mathcal A(n)$. Die Induktionsvoraussetzung ist $\mathcal A(n+1)$, das man für ein festes $n$ annimmt.
--- falsch
Im Induktionsschritt rechnet man $\mathcal A(n)$ für die nächsten Zahlen $n=2,3,4$ nach. Die Induktionsvoraussetzung ist dabei der schon gezeigte Induktionsanfang $\mathcal A(1)$.
:::
:::karte zusammenhang kein Zirkelschluss
Warum ist es kein Zirkelschluss, im Induktionsschritt $\mathcal A(n)$ vorauszusetzen?
---
Weil man $\mathcal A(n)$ nur für ein beliebiges, aber festes $n$ voraussetzt und allein die Implikation $\mathcal A(n)\Rightarrow\mathcal A(n+1)$ zeigt. Dass $\mathcal A(n)$ wahr ist, folgt erst aus dem Anfang und der Kette.
--- falsch
Weil man im Induktionsschritt gar nichts voraussetzt: $\mathcal A(n)$ wird dort für jedes $n$ direkt bewiesen, und der Induktionsanfang dient nur als zusätzliche Probe für den kleinsten Fall.
--- falsch
Es ist ein Zirkelschluss, der aber erlaubt ist, weil die natürlichen Zahlen unendlich viele Fälle haben und ein direkter Beweis für alle Fälle sonst gar nicht möglich wäre.
--- falsch
Weil man $\mathcal A(n)$ nur für $n=1$ voraussetzt, und das ist im Induktionsanfang schon gezeigt. Für die größeren $n$ setzt man im Schritt nichts mehr voraus.
:::
:::karte zusammenhang Anfang und Schritt nötig
Warum braucht ein Induktionsbeweis sowohl den Anfang als auch den Schritt?
---
Ohne Anfang hat $\mathcal A(n):=(n=n+1)$ einen gültigen Schritt und ist doch immer falsch. Ohne Schritt reichen auch viele geprüfte Fälle nicht: $n^2-n+41$ ist für $n=1,\dots,40$ eine Primzahl, für $n=41$ aber $41^2$.
--- falsch
Ohne Anfang fehlt nur eine Probe, der Beweis bleibt gültig, weil der Schritt jedes $n$ erfasst. Ohne Schritt genügen dagegen genügend viele geprüfte Fälle, etwa die ersten vierzig, denn ein Muster, das so lange hält, bricht nicht mehr ab.
--- falsch
Ohne Anfang wäre der Schritt nicht beweisbar, weil man $\mathcal A(n)$ dort aus $\mathcal A(1)$ ausrechnet. Ohne Schritt fehlt nur die Angabe, bis zu welchem $n$ die Aussage gilt; sie bleibt für die geprüften Fälle bewiesen.
--- falsch
Beide sind nur aus Gewohnheit üblich: Eine Aussage mit gültigem Schritt ist immer wahr, und eine Aussage, die für die ersten vierzig Fälle stimmt, ebenfalls; der Anfang ist eine Probe.
:::
:::karte zusammenhang Warum Induktion gilt
Auf welcher Eigenschaft der natürlichen Zahlen beruht die vollständige Induktion?
---
Auf dem Aufbau von $\mathbb{N}$: Ist $M\subset\mathbb{N}$ mit $1\in M$, und folgt aus $n\in M$ stets $n+1\in M$, dann ist $M=\mathbb{N}$. Man wendet das auf $M:=\{n\in\mathbb{N}:\mathcal A(n)\text{ wahr}\}$ an.
--- falsch
Darauf, dass $\mathbb{N}$ nur endlich viele Elemente hat: Man kann deshalb alle Fälle nacheinander prüfen, und die Induktion fasst diese lange Prüfung nur kurz zusammen.
--- falsch
Darauf, dass jede Teilmenge $M\subset\mathbb{N}$ mit $1\in M$ schon ganz $\mathbb{N}$ ist. Den Schritt von $n$ auf $n+1$ braucht man dafür nicht, die $1$ allein genügt.
--- falsch
Darauf, dass $\mathbb{N}$ nach oben beschränkt ist: Eine Aussage, die an der oberen Schranke gilt, überträgt sich rückwärts auf alle kleineren natürlichen Zahlen.
:::
:::karte formel zweite Version der Induktion
Wie lautet die zweite Version der vollständigen Induktion mit spätem Start und allen früheren Fällen?
---
Ist $\mathcal A(n_0)$ wahr und gilt für jedes $n\ge n_0$ die Implikation $\bigl(\mathcal A(n_0)\wedge\mathcal A(n_0+1)\wedge\dots\wedge\mathcal A(n)\bigr)\Rightarrow\mathcal A(n+1)$, dann ist $\mathcal A(n)$ für alle $n\ge n_0$ wahr.
--- falsch
Ist $\mathcal A(n_0)$ wahr und gilt für jedes $n\ge n_0$ die Implikation $\mathcal A(n)\Rightarrow\mathcal A(n+1)$, dann ist $\mathcal A(n)$ für alle $n\in\mathbb{N}$ wahr, also auch für die $n<n_0$ vor dem Start.
--- falsch
Ist $\mathcal A(n)$ für alle $n\le n_0$ wahr, dann ist es für alle $n\in\mathbb{N}$ wahr; einen Schritt braucht man bei dieser Version nicht, wenn man genügend viele Fälle geprüft hat.
--- falsch
Ist $\mathcal A(n_0)$ wahr und gilt für jedes $n\ge n_0$ die Implikation $\mathcal A(n+1)\Rightarrow\bigl(\mathcal A(n_0)\wedge\dots\wedge\mathcal A(n)\bigr)$, dann ist $\mathcal A(n)$ für alle $n\ge n_0$ wahr.
:::
:::karte formel Summe und Produkt
Wie sind die Summe $\sum_{i=1}^nx_i$ und das Produkt $\prod_{i=1}^nx_i$ rekursiv definiert?
---
$\sum_{i=1}^{1}x_i:=x_1$, $\sum_{i=1}^{n+1}x_i:=\Bigl(\sum_{i=1}^{n}x_i\Bigr)+x_{n+1}$, ebenso $\prod_{i=1}^{1}x_i:=x_1$, $\prod_{i=1}^{n+1}x_i:=\Bigl(\prod_{i=1}^{n}x_i\Bigr)\cdot x_{n+1}$. Nach der Induktion ist der Wert für jedes $n$ festgelegt.
--- falsch
$\sum_{i=1}^{1}x_i:=0$, $\sum_{i=1}^{n+1}x_i:=\Bigl(\sum_{i=1}^{n}x_i\Bigr)+x_{n}$, ebenso $\prod_{i=1}^{1}x_i:=1$, $\prod_{i=1}^{n+1}x_i:=\Bigl(\prod_{i=1}^{n}x_i\Bigr)\cdot x_{n}$. Nach der Induktion ist der Wert für jedes $n$ festgelegt.
--- falsch
Als $x_1+\dots+x_n$ und $x_1\cdot\ldots\cdot x_n$; die Pünktchen erklären den Wert schon vollständig, eine Rekursion ist dafür nicht nötig und nur eine andere Schreibweise für dasselbe.
--- falsch
$\sum_{i=1}^{n+1}x_i:=\Bigl(\sum_{i=1}^{n}x_i\Bigr)+x_{n+1}$ und $\prod_{i=1}^{n+1}x_i:=\Bigl(\prod_{i=1}^{n}x_i\Bigr)\cdot x_{n+1}$; einen Anfangswert braucht die Rekursion nicht, weil sie bei jedem $n$ beginnen kann.
:::
:::karte formel Potenz und Fakultät
Wie sind die Potenzen $x^n$, $x^0$, $x^{-n}$ und die Fakultät $n!$ definiert?
---
$x^n:=\prod_{i=1}^nx$; für $x\ne0$ und $n\in\mathbb{N}$ ist $x^0:=1$ und $x^{-n}:=(x^n)^{-1}=(\frac1x)^n$. Weiter ist $n!:=\prod_{i=1}^ni$ und $0^0:=1$.
--- falsch
$x^n:=\sum_{i=1}^nx=nx$; für $x\ne0$ ist $x^0:=0$ und $x^{-n}:=-x^n$. Weiter ist $n!:=\sum_{i=1}^ni$, und $0^0$ ist nicht festgelegt.
--- falsch
$x^n:=\prod_{i=1}^nx$; für $x\ne0$ ist $x^0:=x$ und $x^{-n}:=-(x^n)$. Weiter ist $n!:=\prod_{i=1}^ni$ und $0^0:=0$, weil $0^n=0$ ist.
--- falsch
$x^n:=\prod_{i=1}^nx$; für $x\ne0$ ist $x^0:=1$ und $x^{-n}:=(x^{-1})^{-n}$. Weiter ist $n!:=\prod_{i=1}^{n}(i+1)$ und $0^0:=0$.
:::
:::karte zusammenhang null als Exponent
Warum setzt man $x^0:=1$, und warum ist auch die Festlegung $0^0:=1$ sinnvoll?
---
$x^0:=1$ ist erzwungen, weil $x^n\cdot x^0=x^{n+0}$ gelten soll. $0^0:=1$ ist eine Festlegung: Damit setzt sich $x^0=1$ bei $x=0$ fort, und $(x+y)^2=x^2y^0+2x^1y^1+x^0y^2$ bleibt für $x=0$ oder $y=0$ richtig.
--- falsch
$x^0:=1$ ist eine reine Festlegung ohne Grund, die man auch anders treffen könnte. $0^0:=1$ folgt dagegen zwingend aus den Körperaxiomen, weil $0\cdot0^{-1}=1$ ist.
--- falsch
$x^0:=1$ ist erzwungen, weil $x^n\cdot x^0=x^{n\cdot0}$ gelten soll. $0^0:=1$ ist ebenfalls erzwungen, weil $0^n=0$ für $n\ge1$ gilt und die Werte von $0^n$ sonst springen würden.
--- falsch
$x^0:=1$ folgt aus $x^0=x\cdot x^{-1}$. Bei $x=0$ gibt es $0^{-1}$ nicht, deshalb ist $0^0$ nicht erklärt, und die Festlegung $0^0:=1$ führt zu einem Widerspruch in den Potenzgesetzen.
:::
:::karte formel Potenzgesetze
Welche Potenzgesetze gelten in jedem Körper, und unter welchen Voraussetzungen?
---
Für $x,y\ne0$ und $p,q\in\mathbb{Z}$: $x^px^q=x^{p+q}$, $(x^p)^q=x^{p\cdot q}$, $(xy)^p=x^py^p$. Für $x=0$ sind nur Exponenten $n\ge0$ erlaubt, weil es $0^{-1}$ nicht gibt.
--- falsch
Für $x,y\ne0$ und $p,q\in\mathbb{Z}$: $x^px^q=x^{p\cdot q}$, $(x^p)^q=x^{p+q}$, $(xy)^p=x^py^p$. Für $x=0$ gelten sie mit allen Exponenten, weil $0^p=0$ für jedes $p$ ist.
--- falsch
Für alle $x,y$ und $p,q\in\mathbb{Z}$: $x^px^q=x^{p+q}$, $(x^p)^q=x^{p\cdot q}$, $(xy)^p=x^p+y^p$. Eine Voraussetzung an $x$ und $y$ braucht man dabei nicht.
--- falsch
Für $x,y\ne0$ und $p,q\in\mathbb{Z}$: $x^px^q=x^{p+q}$, $(x^p)^q=x^{p\cdot q}$, $(xy)^p=x^py^p$. Sie gelten aber nur in $\mathbb{R}$, weil man dafür die Vollständigkeit braucht.
:::
:::karte herleitung Summe der ungeraden Zahlen
Wie beweist man $\sum_{i=1}^n(2i-1)=n^2$ durch vollständige Induktion?
---
Anfang: Für $n=1$ ist $2\cdot1-1=1=1^2$, weil die Summe dann nur aus dem ersten Summanden besteht.
---
Schritt: Man setzt voraus, dass die Formel für ein festes $n$ gilt, weil der Induktionsschritt nur $\mathcal A(n)\Rightarrow\mathcal A(n+1)$ zeigen muss.
---
Dann ist $\sum_{i=1}^{n+1}(2i-1)=n^2+2(n+1)-1=n^2+2n+1=(n+1)^2$, weil die Summe bis $n+1$ nach der rekursiven Definition die Summe bis $n$ plus der Summand $2(n+1)-1$ ist.
---
Schluss: Die Formel gilt für alle $n\in\mathbb{N}$, weil Anfang und Schritt bewiesen sind.
:::
:::karte formel Summenformeln
Welche Summenformeln für $\sum_{i=1}^ni$ und $\sum_{i=1}^ni^3$ beweist man durch vollständige Induktion?
---
$\sum_{i=1}^ni=\frac{n(n+1)}2$ und $\sum_{i=1}^ni^3=\frac{n^2(n+1)^2}4$, beide für alle $n\in\mathbb{N}$ und jeweils mit Anfang und Schritt bewiesen. Probe für $n=3$: $1+8+27=36=\frac{9\cdot16}4$.
--- falsch
$\sum_{i=1}^ni=\frac{n(n-1)}2$ und $\sum_{i=1}^ni^3=\frac{n^3(n+1)^3}8$ für alle $n\in\mathbb{N}$; beide folgen unmittelbar aus der Formel für die ungeraden Zahlen.
--- falsch
$\sum_{i=1}^ni=n^2$ und $\sum_{i=1}^ni^3=n^4$ für alle $n\in\mathbb{N}$, weil die Summe der ersten $n$ Zahlen ungefähr $n$-mal die größte Zahl ist.
--- falsch
$\sum_{i=1}^ni=\frac{n(n+1)}2$ und $\sum_{i=1}^ni^3=\frac{n^2(n+1)^2}4$, aber nur für gerade $n$; für ungerade $n$ ergibt der Bruch keine ganze Zahl.
:::
:::karte zusammenhang später Start
Warum beginnt der Induktionsbeweis von $n!>2^n$ erst bei $n_0=4$?
---
Weil die Aussage für kleinere $n$ falsch ist, etwa $6<8$ für $n=3$. Ab $n_0=4$ trägt die Kette: Anfang $24>16$, Schritt $(n+1)!=(n+1)\,n!>(n+1)\,2^n\ge2\cdot2^n$, denn $n+1\ge2$.
--- falsch
Weil der Schritt für $n<4$ nicht funktioniert, die Aussage selbst dort aber stimmt: Auch für $n=3$ ist $3!=6$ größer als $2^3$, nur der Beweis klappt dort nicht.
--- falsch
Weil $n!$ erst ab $n=4$ definiert ist; für kleinere $n$ ist das Produkt $\prod_{i=1}^ni$ noch zu kurz, um eine Fakultät zu bilden, und hat keinen Wert.
--- falsch
Weil man bei jedem Induktionsbeweis die ersten drei Fälle überspringt; sie sind zu einfach und werden nach einer festen Regel immer weggelassen.
:::
:::karte zusammenhang alle früheren Fälle
Warum braucht der Beweis, dass jedes $n\ge2$ ein Produkt von Primzahlen ist, die zweite Version der Induktion?
---
Weil $n+1$, wenn es nicht prim ist, als $n+1=ab$ mit $2\le a,b\le n$ zerfällt. Dann braucht man $\mathcal A(a)$ und $\mathcal A(b)$, also frühere Fälle; $\mathcal A(n)$ allein reicht nicht.
--- falsch
Weil der Anfang bei $n_0=2$ statt bei 1 liegt; abgesehen vom späteren Start reicht der gewöhnliche Schritt $\mathcal A(n)\Rightarrow\mathcal A(n+1)$ wie in jedem anderen Beweis.
--- falsch
Weil Primzahlen keine Teiler haben: Für eine Primzahl $n+1$ kann man $\mathcal A(n)$ nicht verwenden und muss stattdessen alle Fälle bis $n+1$ einzeln nachrechnen.
--- falsch
Weil $n+1=ab$ mit $a=n$ und $b=1$ zerfällt; dann braucht man $\mathcal A(n)$ und $\mathcal A(1)$, und $\mathcal A(1)$ liegt vor dem Start bei $n_0=2$.
:::
:::karte zusammenhang Fehler im Farbbeweis
Wo steckt der Fehler im „Beweis“, dass alle Kabel dieselbe Farbe haben, bei dem man von $n+1$ Kabeln je eines wegnimmt?
---
Der Schritt scheitert bei $n=1$: Von zwei Kabeln bleibt nach dem Wegnehmen je ein anderes übrig, die Reste haben kein gemeinsames Kabel. Der Schritt muss aber für jedes $n$ gelten.
--- falsch
Der Anfang ist falsch: Ein einzelnes Kabel kann mehrere Farben haben, deshalb trägt schon der erste Fall nicht, und alles Weitere steht ohne Grundlage da.
--- falsch
Der Schritt scheitert bei großen $n$: Bei sehr vielen Kabeln verliert man beim Wegnehmen den Überblick; für kleine $n$ ist das Argument dagegen völlig in Ordnung.
--- falsch
Der Fehler liegt im Schluss: Die vollständige Induktion beweist Aussagen nur über Zahlen, nicht über Gegenstände wie Kabel und ihre Farben, die keine Nachfolger haben.
:::
::::

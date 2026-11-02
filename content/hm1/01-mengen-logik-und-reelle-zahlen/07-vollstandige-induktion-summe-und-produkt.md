---
title: Stufe 5: Vollständige Induktion, Summe und Produkt
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Mengen, Logik und reelle Zahlen
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

⁠**So liest man das:** (i) ist die Induktion über (A1), (A2), (M1), (M2). (ii) sagt „jeder mit jedem“, das ist (AM) wiederholt. Für $p,q\in\mathbb{N}$ ist (iii) Umnummerieren: $x^px^q=\prod_{i=1}^{p+q}x=x^{p+q}$. **Warum $x\ne0$:** $0^{-1}$ gibt es nicht, für $x=0$ sind nur Exponenten $n\ge0$ erlaubt, und $0^n=0$ für $n\ge1$. Für $x,y>0$ gelten die Gesetze auch mit rationalen Exponenten, etwa $x^{1/2}=\sqrt x$ ([Teil 5](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/exponentialfunktion-und-stetigkeit/exponentialfunktion-und-stetigkeit.html)).

:::abbildung hm1/k1induktion 5
Links ist jede Farbe ein Winkelstück. Rechts der Induktionsschritt: $n^2$ wächst um $2n+1$ Felder.
:::

**Beispiel 1: Summe der ungeraden Zahlen.** Behauptung: $\sum_{i=1}^n(2i-1)=n^2$. **Anfang:** $2\cdot1-1=1=1^2$. **Schritt:** Gilt die Formel für $n$, dann ist $\sum_{i=1}^{n+1}(2i-1)=n^2+2(n+1)-1=n^2+2n+1=(n+1)^2$. **Schluss:** Sie gilt für alle $n$. Ebenso beweist man $\sum_{i=1}^ni=\frac{n(n+1)}2$ und $\sum_{i=1}^ni^3=\frac{n^2(n+1)^2}4$ (Aufgabe [6](#aufg-6)).

**Beispiel 2: später Start.** $n!>2^n$ für $n\ge n_0=4$. Anfang: $24>16$. Schritt: $(n+1)!=(n+1)\,n!>(n+1)\,2^n\ge2\cdot2^n$, denn $n+1\ge2$. **Grenzfall:** Für $n=3$ ist $6<8$, der Start bei 4 ist nötig.

**Beispiel 3: alle früheren Fälle.** Jedes $n\ge2$ ist ein Produkt von Primzahlen. Anfang: 2 ist prim. Schritt: Ist $n+1$ nicht prim, ist $n+1=ab$ mit $2\le a,b\le n$. Hier reicht $\mathcal A(n)$ allein nicht, man braucht $\mathcal A(a)$ und $\mathcal A(b)$.

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

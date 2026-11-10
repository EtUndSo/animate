---
title: Stufe 6: Die Dimension
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Vektorprodukt und Basen
adresse: elektrotechnik/1-semester/hohere-mathematik-1/vektorprodukt-und-basen
knoten: Kapitel 9: Vektorprodukt und Basen
order: 1290800
summary: Ein Vektorraum hat viele Basen.
tags: endlichdimensional, unendlichdimensional, Dimension, Basisauswahl:
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Ein Vektorraum hat viele Basen. Diese Stufe zeigt, dass alle gleich lang sind, und dass es überhaupt eine gibt. Erst dann ist „Dimension“ eine sinnvolle Zahl.
:::

**Die Idee.** Reichen $n$ Richtungen, können $n+1$ Vektoren nicht unabhängig sein. Der Mechanismus ist Wegrechnen: Mit einem Vektor zieht man aus allen anderen den Anteil längs einer Basisrichtung heraus. Übrig bleiben $n$ Vektoren in einem Raum mit $n-1$ Richtungen, also dasselbe Problem eine Nummer kleiner (Abb. [6](#abb-6)).

:::abbildung hm1/k9dim 6
Drei Vektoren im $\mathbb{R}^2$. Links $\vec a_1=(2,1)$, $\vec a_2=(1,2)$, $\vec a_3=(-1,2)$. Rechts ist aus $\vec a_2$ und $\vec a_3$ der Anteil längs $\vec e_1$ herausgerechnet: $\vec c_2=\vec a_2-\frac12\vec a_1=(0,\frac32)$, $\vec c_3=\vec a_3+\frac12\vec a_1=(0,\frac52)$. Beide liegen auf einer Geraden, also ist $5\vec c_2-3\vec c_3=\vec0$. Das ergibt $-4\vec a_1+5\vec a_2-3\vec a_3=\vec0$.
:::

:::satz Satz 6.1 (Zu viele Vektoren sind abhängig)
<span class="anker" id="satz-6-1"></span>

Sei $\mathcal B=(\vec b_1,\dots,\vec b_n)$, $n\in\mathbb{N}$, eine Basis von $V\ne\{\vec0\}$. Dann sind $m$ Vektoren $\vec a_1,\dots,\vec a_m\in V$ mit $m>n$ stets linear abhängig.
:::

⁠**So liest man das:** Vier Vektoren im $\mathbb{R}^3$ sind immer abhängig. Es genügt, $m=n+1$ zu zeigen: Kann man mit $n+1$ Vektoren die Null nichttrivial kombinieren, geht das mit mehr Vektoren erst recht (Koeffizient 0 für den Rest).

:::beweis Induktion über $n$
Behauptet wird für alle $n$: Hat ein Vektorraum eine Basis mit $n$ Elementen, sind $n+1$ seiner Vektoren abhängig.

⁠**Anfang $n=1$.** Sei $(\vec b_1)$ eine Basis. Dann ist $\vec a_1=\alpha\vec b_1$, $\vec a_2=\beta\vec b_1$. Für $\alpha=0$ ist $\vec a_1=\vec0$, die Vektoren sind abhängig. Für $\alpha\ne0$ ist $\vec a_2=\frac\beta\alpha\vec a_1$.

⁠**Schritt $n\to n+1$.** Sei $(\vec b_1,\dots,\vec b_{n+1})$ Basis von $V$ und seien $\vec a_1,\dots,\vec a_{n+2}\in V$. Die Basis liefert eindeutige Koeffizienten mit

$$\vec a_i=\sum_{j=1}^{n+1}\alpha_{ij}\vec b_j,\quad i=1,\dots,n+2.$$

Ist $\vec a_1=\vec0$, sind die Vektoren abhängig. Sonst gibt es ein $\alpha_{1j}\ne0$, nach Umnummerieren der $\vec b_j$ ist $\alpha_{11}\ne0$. Setze

$$\vec c_i:=\vec a_i-\frac{\alpha_{i1}}{\alpha_{11}}\vec a_1=\sum_{j=1}^{n+1}\Bigl(\alpha_{ij}-\frac{\alpha_{i1}}{\alpha_{11}}\alpha_{1j}\Bigr)\vec b_j,\quad i=2,\dots,n+2.$$

Für $j=1$ verschwindet der Koeffizient. Die $n+1$ Vektoren $\vec c_2,\dots,\vec c_{n+2}$ liegen also im Unterraum $\operatorname{span}\{\vec b_2,\dots,\vec b_{n+1}\}$, und der hat die Basis $(\vec b_2,\dots,\vec b_{n+1})$ mit $n$ Elementen. Nach Induktionsvoraussetzung gibt es $\beta_2,\dots,\beta_{n+2}$, nicht alle 0, mit $\sum_{i=2}^{n+2}\beta_i\vec c_i=\vec0$. Einsetzen von $\vec c_i$ ergibt

$$\vec0=\sum_{i=2}^{n+2}\beta_i\vec a_i+\beta_1\vec a_1\qquad\text{mit}\quad\beta_1:=-\frac1{\alpha_{11}}\sum_{i=2}^{n+2}\beta_i\alpha_{i1}.$$

Da nicht alle $\beta_i$ null sind, sind $\vec a_1,\dots,\vec a_{n+2}$ abhängig.
:::

:::satz Satz 6.2 (Alle Basen sind gleich lang)
<span class="anker" id="satz-6-2"></span>

Ist $(\vec b_1,\dots,\vec b_n)$ eine Basis von $V\ne\{\vec0\}$, hat jede andere Basis von $V$ genau $n$ Elemente.
:::

⁠**Beweis:** Hätte eine Basis $\mathcal C$ mehr als $n$ Elemente, wären diese nach Satz [6.1](#satz-6-1) abhängig, ein Widerspruch zu Satz [5.2](die-basis.html#satz-5-2). Hätte $\mathcal C$ weniger als $n$ Elemente, wären nach Satz [6.1](#satz-6-1), angewandt auf die Basis $\mathcal C$, die $\vec b_1,\dots,\vec b_n$ abhängig, ebenfalls ein Widerspruch.

:::definition Definition 6.3 (Dimension)
<span class="anker" id="satz-6-3"></span>

$V$ heißt __endlichdimensional__, wenn es endlich viele $\vec w_1,\dots,\vec w_r\in V$ gibt mit $V=\operatorname{span}\{\vec w_1,\dots,\vec w_r\}$, also ein endliches Erzeugendensystem. Sonst heißt $V$ __unendlichdimensional__. Die gemeinsame Länge $n$ aller Basen eines endlichdimensionalen $V\ne\{\vec0\}$ heißt __Dimension__: $\dim V=n$. Man setzt $\dim\{\vec0\}:=0$, und für unendlichdimensionales $V$ setzt man $\dim V:=\infty$.
:::

Noch ist offen, ob ein endlichdimensionaler Raum überhaupt eine Basis hat, die Definition braucht das. Die Antwort: Aus jedem Erzeugendensystem lässt sich eine auswählen.

:::satz Satz 6.4 (Basisergänzung)
<span class="anker" id="satz-6-4"></span>

Sei $V=\operatorname{span}\{\vec a_1,\dots,\vec a_n\}$ endlichdimensional und seien $\vec v_1,\dots,\vec v_m\in V$ ($m\ge1$) linear unabhängig, aber keine Basis von $V$. Dann lassen sich $\vec v_1,\dots,\vec v_m$ durch Hinzunahme geeigneter $\vec a_i$ zu einer Basis von $V$ ergänzen.
:::

⁠**So liest man das:** Aus dem Erzeugendensystem holt man Vektoren, bis alles erzeugt ist. Die Unabhängigkeit der $\vec v_i$ ist nötig: Eine Abhängigkeit bleibt beim Ergänzen bestehen.

:::beweis Ein Vektor von außen
Nach Satz [5.2](die-basis.html#satz-5-2) ist $\operatorname{span}\{\vec v_1,\dots,\vec v_m\}\ne V$. Also gibt es ein $j$ mit $\vec a_j\notin\operatorname{span}\{\vec v_1,\dots,\vec v_m\}$ (Aussage $*$), sonst läge schon jede Linearkombination der $\vec a_i$ im Aufspann. **Behauptung:** $\vec v_1,\dots,\vec v_m,\vec a_j$ sind unabhängig. Wären sie abhängig, gäbe es $(\alpha_1,\dots,\alpha_m,\alpha)\ne(0,\dots,0)$ mit $\sum_i\alpha_i\vec v_i+\alpha\vec a_j=\vec0$. Für $\alpha\ne0$ widerspricht das $*$. Für $\alpha=0$ ist ein $\alpha_i\ne0$, und die $\vec v_i$ wären abhängig. Setze $\vec v_{m+1}:=\vec a_j$. Ist das eine Basis, ist man fertig, sonst wiederholt man den Schritt. Jeder Schritt nimmt ein neues $\vec a_j$, denn die bisherigen liegen im Aufspann. Nach höchstens $n$ Schritten ist also Schluss, und das geht nur bei einer Basis.
:::

:::satz Satz 6.5 (Folgerungen)
<span class="anker" id="satz-6-5"></span>

Für einen Vektorraum $V$ gilt:

<ol class="rm">

<li>

__Basisauswahl:__ Ist $V=\operatorname{span}\{\vec a_1,\dots,\vec a_n\}\ne\{\vec0\}$, gibt es eine Basis von $V$ aus einer Teilmenge von $\{\vec a_1,\dots,\vec a_n\}$.

</li>

<li>

Ist $\dim V=n$ und sind $\vec v_1,\dots,\vec v_n$ linear unabhängig, ist $(\vec v_1,\dots,\vec v_n)$ bereits eine Basis.

</li>

<li>

Sind $\vec v_1,\dots,\vec v_k\in V$ linear unabhängig, ist $U:=\operatorname{span}\{\vec v_1,\dots,\vec v_k\}$ ein Unterraum mit $\dim U=k$.

</li>

</ol>
:::

⁠**Beweis:** (i) Wähle $\vec v_1:=\vec a_{i_0}\ne\vec0$. Dieser Vektor ist unabhängig. Ist er keine Basis, ergänzt ihn Satz [6.4](#satz-6-4). (ii) Wäre es keine Basis, ergänzte man mit Vektoren einer Basis von $V$ zu einer Basis mit mindestens $n+1$ Elementen, Widerspruch zu Satz [6.2](#satz-6-2). (iii) $(\vec v_1,\dots,\vec v_k)$ ist nach Satz [5.2](die-basis.html#satz-5-2) eine Basis von $U$.

::::beispiel [Beispiele]
$\dim\mathbb{R}^n=n$, $\dim\mathbb{C}^n=n$ über $\mathbb{C}$, aber $\dim\mathbb{C}^n=2n$ über $\mathbb{R}$ (Stufe [5](die-basis.html#stufe-5)). Die Polynome vom Grad höchstens $m$ haben die Basis $1,x,\dots,x^m$, also die Dimension $m+1$. Alle Polynome zusammen bilden einen unendlichdimensionalen Raum: $1,x,\dots,x^m$ sind für jedes $m$ unabhängig. Ein Erzeugendensystem mit $r$ Elementen gäbe nach (i) eine Basis mit höchstens $r$ Elementen, und dann wären $1,x,\dots,x^r$ abhängig. Im Modell ist $\operatorname{span}\{\vec u,\vec v,\vec w\}$ wegen $\vec w=2\vec u-\vec v$ zweidimensional, die Auswahl $(\vec u,\vec v)$ ist eine Basis. Sie lässt sich mit $\vec k$ zu einer Basis des $\mathbb{R}^3$ ergänzen, denn $\operatorname{spat}(\vec k,\vec u,\vec v)=6\ne0$.
::::

**Zwei offene Punkte.** Seien $\vec b,\vec c\in\mathbb{R}^3$ unabhängig und $\vec n:=\vec b\times\vec c\ne\vec0$. Dann sind $\vec b,\vec c,\vec n$ unabhängig: Aus $\beta\vec b+\gamma\vec c+\delta\vec n=\vec0$ folgt nach Skalarprodukt mit $\vec n$ erst $\delta=0$, dann $\beta=\gamma=0$. Nach (ii) ist $(\vec b,\vec c,\vec n)$ eine Basis des $\mathbb{R}^3$. Für $\vec a=\beta\vec b+\gamma\vec c+\delta\vec n$ ist $\langle\vec a,\vec n\rangle=\delta\|\vec n\|^2$. Also liegt $\vec a$ genau dann in $\operatorname{span}\{\vec b,\vec c\}$, wenn $\langle\vec a,\vec n\rangle=0$ ist. Das zeigt $(U^\perp)^\perp=U$ in Satz [4.6](orthonormalsysteme-und-projektion.html#satz-4-6) und die Umkehrung in Satz [3.3](spatprodukt-und-volumen.html#satz-3-3) (iii): Aus $\operatorname{spat}(\vec a,\vec b,\vec c)=0$ folgt $\vec a\in\operatorname{span}\{\vec b,\vec c\}$. Sind schon $\vec b,\vec c$ abhängig, ist nichts zu zeigen.

:::frage Heißt „keine Basis“, dass etwas zu viel oder zu wenig ist?
Beides kommt vor. Zu viele Vektoren sind abhängig (Satz [6.1](#satz-6-1)). Zu wenige erzeugen nicht, sonst gäbe die Basisauswahl eine kürzere Basis. Genau $\dim V$ unabhängige Vektoren sind nach (ii) immer eine Basis, man muss nur eines von beiden prüfen.
:::

:::aufgabe Aufgabe 7 ★★ Auswählen und ergänzen
<span class="anker" id="aufg-7"></span>

Sei $\vec a_1=(1,2,0)$, $\vec a_2=(2,4,0)$, $\vec a_3=(0,1,1)$, $\vec a_4=(1,3,1)$, $U=\operatorname{span}\{\vec a_1,\dots,\vec a_4\}$. (a) Wähle eine Basis von $U$ aus. Wie groß ist $\dim U$? (b) Ergänze sie mit einem Einheitsvektor zu einer Basis des $\mathbb{R}^3$. Welcher kommt in Frage? (c) Sage vorher, wie viele Vektoren man höchstens aus dem $\mathbb{R}^3$ wählen kann, die unabhängig sind.

:::loesung
(a) $\vec a_2=2\vec a_1$ und $\vec a_4=\vec a_1+\vec a_3$ sind überflüssig. $(\vec a_1,\vec a_3)$ ist unabhängig, $\dim U=2$. (b) $\vec a_1\times\vec a_3=(2,-1,1)$. Das Spatprodukt mit $\vec e_i$ ist die $i$-te Komponente davon, also $\ne0$ für alle drei. Jeder Einheitsvektor kommt in Frage, nach Satz [6.5](#satz-6-5) (ii) ist $(\vec a_1,\vec a_3,\vec e_1)$ eine Basis. (c) Drei, denn vier Vektoren sind nach Satz [6.1](#satz-6-1) abhängig.
:::
:::

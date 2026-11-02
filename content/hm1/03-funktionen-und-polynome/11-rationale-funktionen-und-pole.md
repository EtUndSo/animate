---
title: Stufe 9: Rationale Funktionen und Pole
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Funktionen und Polynome
order: 1231100
summary: Der Rest T/Q aus Stufe 6 hat Stellen, an denen sein Nenner null wird.
tags: Pol, Ordnung, Lücke, Asymptote
lang: de
---

<span class="anker" id="stufe-9"></span>

:::zweck
Der Rest $T/Q$ aus Stufe [6](division-mit-rest.html#stufe-6) hat Stellen, an denen sein Nenner null wird. Dort ist die Funktion nicht erklärt. Was passiert in der Nähe, und was für große $|x|$?
:::

**Die Idee.** Teilt man eine feste Zahl durch etwas sehr Kleines, wird das Ergebnis sehr groß. Bei $x=2$ ist $Q(2)=0$, der Zähler bleibt aber bei $P(2)=-12$. Bei $x=2{,}01$ ist $Q=0{,}0301$ und $R=-398$, bei $x=1{,}99$ ist $Q=-0{,}0299$ und $R=+402$. Der Mechanismus ist der kleine Faktor $x-2$ im Nenner: Er wechselt bei 2 das Vorzeichen, und mit ihm wechselt $R$. Ist auch der Zähler dort null, kann sich der Faktor dagegen wegkürzen.

:::definition Definition 9.1 (Pol und Lücke)
<span class="anker" id="satz-9-1"></span>

Sei $R=P_n/Q_m$. Man kürzt alle gemeinsamen Linearfaktoren von Zähler und Nenner. Eine Stelle $x_0$ mit $Q_m(x_0)=0$ heißt

<ul>

<li>

__Pol__ (Polstelle) der __Ordnung__ $m_0$, wenn sie nach dem Kürzen eine $m_0$-fache Nullstelle des Nenners ist und keine des Zählers;

</li>

<li>

__Lücke__, wenn sie nach dem Kürzen keine Nullstelle des Nenners mehr ist.

</li>

</ul>
:::

⁠**So liest man das:** Nahe einem Pol ist $R(x)=A(x)/(x-x_0)^{m_0}$ mit $A(x_0)\neq0$: Der Zähler bleibt nahe $A(x_0)$, der Nenner wird beliebig klein, $|R|$ wächst über jede Grenze. ([Teil 4](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte/folgen-und-grenzwerte.html) fasst das mit Grenzwerten genau.) Ungerade Ordnung heißt Vorzeichenwechsel, gerade Ordnung keiner, aus demselben Grund wie in Stufe [8](jede-nullstelle-spaltet-einen-linearfaktor-ab.html#stufe-8): $1/(x-2)^2$ ist bei $2{,}01$ und bei $1{,}99$ gleich $10\,000$. Bei einer Lücke bleibt $R$ endlich, aber auch dort gilt $x_0\notin\mathcal D(R)$. **Beispiel Lücke:** $L(x)=(x^2-4)/(x-2)$ stimmt für $x\neq2$ mit $x+2$ überein, $L(2{,}01)=4{,}01$, bei $x=2$ ist nur ein Punkt des Graphen entfernt.

:::abbildung hm1/k3pole 10
Links $R=P/Q$: Pole bei $x=-1$ und $x=2$ (senkrecht gestrichelt), Nullstellen bei $-2$, $\frac12$ und $3$. Für große $|x|$ nähert sich $R$ der Geraden $2x-1$, dem Polynomteil. Rechts $L=(x^2-4)/(x-2)$: Der Graph ist die Gerade $x+2$ ohne den Punkt bei $x=2$.
:::

**Große $|x|$.** Nach [(6.2)](division-mit-rest.html#gl-6-2) ist $R=S+T/Q$. Wegen $\operatorname{grad}T<\operatorname{grad}Q$ wird $T/Q$ für große $|x|$ beliebig klein, denn die höchste Potenz des Nenners wächst schneller. Also nähert sich $R$ dem Polynom $S$, der __Asymptote__ (für $n-m=1$ eine Gerade). Im Rechenmodell ist $R(100)=198{,}92$ und $2\cdot100-1=199$, der Rest macht nur $-0{,}08$ aus. **Grenzfälle:** Für $n<m$ ist $S=0$, und $R$ nähert sich 0. Für $n=m$ ist $S=a_n/b_m$ eine Konstante.

:::zusatz Partialbruchzerlegung
Der Rest lässt sich weiter zerlegen, sodass jeder Pol seinen eigenen Summanden bekommt:

$$R(x)=2x-1+\frac{A}{x-2}+\frac{B}{x+1}.$$

Multipliziert man $\frac{-8x+4}{(x-2)(x+1)}=\frac{A}{x-2}+\frac{B}{x+1}$ mit $x-2$ und setzt $x=2$, bleibt $A=-12/3=-4$, ebenso $B=12/(-3)=-4$. Bei Polen der Ordnung 1 genügt das. In der Elektrotechnik zerlegt man so Übertragungsfunktionen, die beschreiben, wie eine Schaltung ein Signal verändert, in Anteile je Pol.
:::

:::frage Ist eine Lücke nicht dasselbe wie ein Pol, weil beide Male der Nenner null ist?
Der Nenner ist in beiden Fällen null, das stimmt. Der Unterschied liegt im Zähler. Beim Pol bleibt er von null verschieden, ein endlicher Wert durch fast null wird groß. Bei der Lücke ist er auch null, der gemeinsame Faktor fällt weg, und der Quotient bleibt endlich.
:::

:::aufgabe Aufgabe 10 ★★ Pol oder Lücke
<span class="anker" id="aufg-10"></span>

Sei $L_2(x)=\dfrac{x^2-1}{x^2-3x+2}$. (a) Bestimme $\mathcal D(L_2)$, Pole und Lücken. (b) Berechne $L_2(2{,}01)$ und $L_2(1{,}99)$ und erkläre das Vorzeichen. (c) Welchem Wert nähert sich $L_2$ für große $|x|$? Prüfe mit $x=1000$.

:::loesung
(a) $L_2(x)=\frac{(x-1)(x+1)}{(x-1)(x-2)}$, also $\mathcal D(L_2)=\mathbb{R}\setminus\{1,2\}$. Gekürzt: $\frac{x+1}{x-2}$. Bei $x=1$ Lücke (Wert der gekürzten Form: $-2$), bei $x=2$ Pol der Ordnung 1. (b) $L_2(2{,}01)=3{,}01/0{,}01=301$, $L_2(1{,}99)=2{,}99/(-0{,}01)=-299$. Der Zähler ist nahe 3 positiv, der Nenner $x-2$ wechselt das Vorzeichen. (c) Es ist $n=m=2$, also $L_2\to1/1=1$. $L_2(1000)=1001/998=1{,}003$.
:::
:::

:::aufgabe Aufgabe 11 ★★★ Asymptote mit Horner
<span class="anker" id="aufg-11"></span>

Sei $W(x)=\dfrac{x^2+x+1}{x-1}$. (a) Teile mit dem Horner-Schema und gib Polynomteil und Rest an. (b) Wo liegt der Pol, welche Ordnung hat er? (c) Wie weit liegt $W$ bei $x=100$ über der Asymptote?

:::loesung
(a) Schema bei $x_0=1$ mit $1,1,1$: $1,2,3$. Also $x^2+x+1=(x-1)(x+2)+3$ und $W(x)=x+2+\frac{3}{x-1}$. (b) Bei $x=1$, denn der Zähler ist dort 3. Der Nennerfaktor tritt einmal auf: Ordnung 1. (c) Abstand $3/99=0{,}0303$, oberhalb der Asymptote, denn $x-1>0$.
:::
:::

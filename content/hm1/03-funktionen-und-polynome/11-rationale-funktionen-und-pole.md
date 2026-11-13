---
title: Stufe 9: Rationale Funktionen und Pole
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Funktionen und Polynome
adresse: elektrotechnik/1-semester/hohere-mathematik-1/funktionen-und-polynome
knoten: Kapitel 3: Funktionen und Polynome
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

⁠**So liest man das:** Nahe einem Pol ist $R(x)=A(x)/(x-x_0)^{m_0}$ mit $A(x_0)\neq0$: Der Zähler bleibt nahe $A(x_0)$, der Nenner wird beliebig klein, $|R|$ wächst über jede Grenze. ([Kapitel 4](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte/folgen-und-grenzwerte.html) fasst das mit Grenzwerten genau.) Ungerade Ordnung heißt Vorzeichenwechsel, gerade Ordnung keiner, aus demselben Grund wie in Stufe [8](jede-nullstelle-spaltet-einen-linearfaktor-ab.html#stufe-8): $1/(x-2)^2$ ist bei $2{,}01$ und bei $1{,}99$ gleich $10\,000$. Bei einer Lücke bleibt $R$ endlich, aber auch dort gilt $x_0\notin\mathcal D(R)$. **Beispiel Lücke:** $L(x)=(x^2-4)/(x-2)$ stimmt für $x\neq2$ mit $x+2$ überein, $L(2{,}01)=4{,}01$, bei $x=2$ ist nur ein Punkt des Graphen entfernt.

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

::::formelsammlung
**Verhalten nahe einem Pol**

$$R(x)=A(x)/(x-x_0)^{m_0}$$

Mit $A(x_0)\neq0$: Nach dem Kürzen aller gemeinsamen Linearfaktoren ist $x_0$ eine $m_0$-fache Nullstelle des Nenners und keine des Zählers, ein Pol der Ordnung $m_0$; $|R|$ wächst über jede Grenze. Ungerade Ordnung: Vorzeichenwechsel, gerade: keiner. Bei einer Lücke ist $x_0$ nach dem Kürzen keine Nullstelle des Nenners mehr; $R$ bleibt endlich, aber $x_0\notin\mathcal D(R)$.

**Asymptote**

$$R=S+T/Q$$

Wegen $\operatorname{grad}T<\operatorname{grad}Q$ wird $T/Q$ für große $|x|$ beliebig klein, und $R$ nähert sich dem Polynomteil $S$ (für $n-m=1$ eine Gerade). Für $n<m$ ist $S=0$, für $n=m$ ist $S=a_n/b_m$.
::::

::::lernkarten
:::karte begriff Pol und Polstelle
Wann heißt eine Nullstelle $x_0$ des Nenners einer rationalen Funktion $R=P_n/Q_m$ ein Pol oder eine Polstelle?
---
Wenn $x_0$ nach dem Kürzen aller gemeinsamen Linearfaktoren von Zähler und Nenner noch eine $m_0$-fache Nullstelle des Nenners ist, aber keine des Zählers; dort wächst $|R|$ über jede Grenze.
--- falsch
Wenn $x_0$ vor dem Kürzen eine Nullstelle des Nenners ist, gleich ob auch der Zähler dort null ist; jede Nullstelle des Nenners ist ein Pol, und dort wächst $|R|$ über jede Grenze.
--- falsch
Wenn $x_0$ nach dem Kürzen eine Nullstelle des Zählers ist, aber keine des Nenners; dort wird $R$ null, und der Graph berührt oder kreuzt die Achse wie bei einer Nullstelle.
--- falsch
Wenn $x_0$ nach dem Kürzen keine Nullstelle des Nenners mehr ist; dann bleibt $R$ nahe $x_0$ endlich, und dem Graphen fehlt dort nur ein einzelner Punkt.
:::
:::karte begriff Ordnung
Was gibt die Ordnung $m_0$ eines Pols $x_0$ einer rationalen Funktion an?
---
Die Vielfachheit, mit der $x_0$ nach dem Kürzen aller gemeinsamen Linearfaktoren Nullstelle des Nenners ist. Nahe dem Pol ist $R(x)=A(x)/(x-x_0)^{m_0}$ mit $A(x_0)\neq0$.
--- falsch
Die Vielfachheit, mit der $x_0$ vor dem Kürzen Nullstelle des Zählers ist. Nahe dem Pol ist $R(x)=(x-x_0)^{m_0}\,A(x)$ mit $A(x_0)\neq0$, und $R$ wird dort klein.
--- falsch
Die Zahl der Pole, die $R$ insgesamt hat; sie ist gleich dem Grad $m$ des Nenners. Nahe jedem Pol ist $R(x)=A(x)/(x-x_0)^{m}$ mit demselben Exponenten $m$.
--- falsch
Die Vielfachheit, mit der $x_0$ vor dem Kürzen Nullstelle des Nenners ist, gemeinsame Faktoren mitgezählt. Nahe dem Pol ist $R(x)=A(x)/(x-x_0)^{m_0}$, wobei $A(x_0)=0$ sein darf.
:::
:::karte begriff Lücke
Wann heißt eine Nullstelle $x_0$ des Nenners einer rationalen Funktion eine Lücke, und wie verhält sich $R$ dort?
---
Wenn $x_0$ nach dem Kürzen aller gemeinsamen Linearfaktoren keine Nullstelle des Nenners mehr ist. $R$ bleibt dann nahe $x_0$ endlich, aber auch dort gilt $x_0\notin\mathcal D(R)$; dem Graphen fehlt ein Punkt.
--- falsch
Wenn $x_0$ nach dem Kürzen eine Nullstelle des Nenners bleibt, der Zähler dort aber ebenfalls null ist. $R$ bleibt dann endlich, und nach dem Kürzen gehört $x_0$ wieder ganz normal zu $\mathcal D(R)$.
--- falsch
Wenn $x_0$ nach dem Kürzen keine Nullstelle des Nenners mehr ist. Dann gehört $x_0$ zu $\mathcal D(R)$, weil man den gekürzten Ausdruck einsetzen darf; der Graph ist vollständig.
--- falsch
Wenn $x_0$ eine Nullstelle des Nenners von gerader Ordnung ist. $R$ wechselt dort nicht das Vorzeichen, sondern springt von großen Werten zurück, und dem Graphen fehlt ein Stück.
:::
:::karte begriff Asymptote
Was ist die Asymptote einer rationalen Funktion $R=S+T/Q$ aus der Division mit Rest, und wann ist sie eine Gerade?
---
Das Polynom $S$, dem sich $R$ für große $|x|$ nähert, weil $T/Q$ wegen $\operatorname{grad}T<\operatorname{grad}Q$ beliebig klein wird. Für $n-m=1$ ist sie eine Gerade, im Rechenmodell $2x-1$.
--- falsch
Die senkrechte Gerade durch einen Pol, der sich $R$ nähert, wenn $x$ gegen den Pol geht. Sie ist immer eine Gerade, im Rechenmodell $x=2$ und $x=-1$, und hängt nicht von $S$ ab.
--- falsch
Der Rest $T/Q$, dem sich $R$ für große $|x|$ nähert, weil der Polynomteil $S$ dort beliebig klein wird. Für $n-m=1$ ist sie eine Gerade, im Rechenmodell $-8x+4$.
--- falsch
Das Polynom $S$, dem sich $R$ für große $|x|$ nähert, weil $T/Q$ dann beliebig groß wird und $S$ überdeckt. Eine Gerade ist sie nur für $n=m$, im Rechenmodell nie.
:::
:::karte zusammenhang Betrag am Pol
Warum wächst der Betrag einer rationalen Funktion $R$ nahe einem Pol $x_0$ über jede Grenze?
---
Weil nahe dem Pol $R(x)=A(x)/(x-x_0)^{m_0}$ mit $A(x_0)\neq0$ ist: Der Zähler bleibt nahe $A(x_0)$, der Nenner wird beliebig klein. Eine feste Zahl durch fast null ergibt sehr Großes.
--- falsch
Weil der Zähler nahe dem Pol über jede Grenze wächst, während der Nenner fest bleibt; der Pol ist eine Stelle, an der das Polynom im Zähler unendlich wird.
--- falsch
Weil Zähler und Nenner nahe dem Pol beide gegen null gehen und $0/0$ als unendlich gilt; je schneller der Zähler null wird, desto größer wird $|R|$.
--- falsch
Weil $R$ am Pol selbst den Wert $\infty$ annimmt und eine Funktion nahe einer Stelle ungefähr ihren Wert an dieser Stelle hat; $\infty$ gehört dort zum Wertebereich.
:::
:::karte zusammenhang Vorzeichen am Pol
Woran liegt es, ob eine rationale Funktion an einem Pol das Vorzeichen wechselt?
---
An der Ordnung: Nahe dem Pol bestimmt $(x-x_0)^{m_0}$ das Vorzeichen, bei ungerader Ordnung wechselt es, bei gerader nicht. So ist $1/(x-2)^2$ bei $2{,}01$ und bei $1{,}99$ gleich $10\,000$.
--- falsch
Am Vorzeichen des Zählers: Ist der Zähler am Pol positiv, wechselt $R$ das Vorzeichen, ist er negativ, nicht. Die Ordnung des Pols spielt dafür keine Rolle.
--- falsch
An der Ordnung: Bei gerader Ordnung wechselt das Vorzeichen, bei ungerader nicht, weil eine gerade Zahl von Faktoren $x-x_0$ das Vorzeichen zweimal umdreht.
--- falsch
Jede rationale Funktion wechselt an jedem Pol das Vorzeichen, weil der Nenner dort durch null geht. So ist $1/(x-2)^2$ bei $2{,}01$ positiv und bei $1{,}99$ negativ.
:::
:::karte zusammenhang Lücke oder Pol
Worin unterscheiden sich Lücke und Pol, wenn doch in beiden Fällen der Nenner null ist?
---
Im Zähler: Beim Pol bleibt er von null verschieden, ein endlicher Wert durch fast null wird groß. Bei der Lücke ist er auch null, der gemeinsame Faktor fällt weg, der Quotient bleibt endlich.
--- falsch
Im Nenner: Beim Pol ist der Nenner von gerader Ordnung null, bei der Lücke von ungerader. Der Zähler spielt keine Rolle, weil durch null ohnehin nicht geteilt werden darf.
--- falsch
Im Definitionsbereich: Ein Pol gehört nicht zu $\mathcal D(R)$, eine Lücke dagegen schon, weil man dort den gekürzten Ausdruck einsetzt. Der Zähler ist in beiden Fällen nicht null, nur der Nenner unterscheidet sich.
--- falsch
Im Zähler: Bei der Lücke bleibt er von null verschieden, und der Wert bleibt endlich, weil der Nenner nur kurz null wird. Beim Pol ist der Zähler auch null, und $0/0$ wird unendlich.
:::
:::karte zusammenhang Annäherung an die Asymptote
Warum nähert sich eine rationale Funktion $R=S+T/Q$ für große $|x|$ dem Polynomteil $S$?
---
Weil $\operatorname{grad}T<\operatorname{grad}Q$ ist: Die höchste Potenz des Nenners wächst schneller, und $T/Q$ wird für große $|x|$ beliebig klein. Im Rechenmodell ist $R(100)=198{,}92$ gegen $2\cdot100-1=199$.
--- falsch
Weil der Rest $T$ eine Konstante ist und eine Konstante gegen große Werte von $S$ nicht ins Gewicht fällt; deshalb gilt das nur, wenn der Nenner den Grad 1 hat.
--- falsch
Weil $S$ für große $|x|$ ebenfalls beliebig klein wird und $R$ dann gegen null geht; die Asymptote ist deshalb immer die $x$-Achse, gleich welcher Grad vorliegt.
--- falsch
Weil $T$ und $Q$ für große $|x|$ gleich schnell wachsen und $T/Q$ sich eins nähert; $R$ nähert sich also $S+1$, im Rechenmodell der Geraden $2x$.
:::
:::karte formel Asymptote in den Grenzfällen
Welchem Polynom $S$ nähert sich $R=P_n/Q_m$ für große $|x|$, wenn der Zählergrad $n$ kleiner als der Nennergrad $m$ oder gleich ihm ist?
---
Für $n<m$ ist $S=0$, und $R$ nähert sich 0. Für $n=m$ ist $S=a_n/b_m$ eine Konstante, der Quotient der höchsten Koeffizienten von Zähler und Nenner.
--- falsch
Für $n<m$ ist $S=a_n/b_m$, und $R$ nähert sich diesem Quotienten. Für $n=m$ ist $S=0$, weil sich die höchsten Potenzen gegenseitig aufheben.
--- falsch
Für $n<m$ wächst $R$ über jede Grenze, weil der Nenner schneller wächst. Für $n=m$ ist $S=1$, weil Zähler und Nenner gleich schnell wachsen.
--- falsch
Für $n<m$ ist $S=0$, und $R$ nähert sich 0. Für $n=m$ ist $S=a_0/b_0$, der Quotient der Summanden ohne $x$, weil diese für große $|x|$ übrig bleiben.
:::
:::karte zusammenhang Graph mit Lücke
Wie sieht der Graph von $L(x)=(x^2-4)/(x-2)$ aus, und warum sieht er so aus?
---
Wie die Gerade $x+2$ ohne den Punkt bei $x=2$: Für $x\neq2$ kürzt sich der gemeinsame Faktor $x-2$, etwa $L(2{,}01)=4{,}01$; bei $x=2$ ist $L$ nicht erklärt, und es entsteht eine Lücke.
--- falsch
Wie die Gerade $x+2$ mit einem Pol bei $x=2$: Nahe $x=2$ wächst $|L|$ über jede Grenze, weil der Nenner dort null wird, und der Graph springt von unten nach oben.
--- falsch
Wie die Gerade $x+2$, vollständig: Nach dem Kürzen ist $L(x)=x+2$ für alle $x$, also auch $L(2)=4$; der Nenner $x-2$ spielt nach dem Kürzen keine Rolle mehr.
--- falsch
Wie die Parabel $x^2-4$, verschoben um 2: Der Nenner $x-2$ verschiebt den Graphen nach rechts, und bei $x=2$ hat $L$ eine Nullstelle, weil dort der Zähler null ist.
:::
:::karte zusammenhang Partialbruchzerlegung
Wie bestimmt man bei Polen der Ordnung 1 den Zähler $A$ in der Partialbruchzerlegung $R(x)=2x-1+\frac{A}{x-2}+\frac{B}{x+1}$?
---
Man multipliziert $\frac{-8x+4}{(x-2)(x+1)}=\frac{A}{x-2}+\frac{B}{x+1}$ mit $x-2$ und setzt $x=2$: Der Summand mit $B$ fällt weg, es bleibt $A=-12/3=-4$; ebenso $B=12/(-3)=-4$.
--- falsch
Man setzt $x=2$ direkt in die Gleichung ein, ohne vorher zu multiplizieren: Dann wird der Summand mit $A$ null, und $A$ ist der Wert der übrigen Summanden an dieser Stelle.
--- falsch
Man multipliziert die Gleichung mit $x-2$ und setzt $x=0$: Dann fallen alle Potenzen von $x$ weg, und $A$ ist der Summand ohne $x$, hier also $A=4$.
--- falsch
Man vergleicht die höchsten Koeffizienten von Zähler und Nenner: $A$ ist der Quotient $-8/1$, und $B$ ist der Rest, der zum Zähler $-8x+4$ noch fehlt.
:::
::::

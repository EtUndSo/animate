---
title: Die Ableitung
pfad: Informatik / Machine Learning / Mathematische Grundlagen / Ableitung, Gradient und Kettenregel
knoten: Grundlagen 3: Ableitung, Gradient und Kettenregel
nachschlagen: ja
order: 15230200
summary: Die Ableitung misst, wie stark eine Funktion einer Variablen auf eine kleine Änderung ihrer Eingabe reagiert.
tags: Sekante, Differenzenquotient, Grenzwert, differenzierbar, Ableitung, Tangente, Knick, lineare Näherung
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Die Ableitung misst, wie stark eine Funktion einer Variablen auf eine kleine Änderung ihrer Eingabe reagiert. Dieser Abschnitt führt sie als Grenzwert von Steigungen ein, deutet sie als die Steigung der Geraden, die sich der Kurve am besten anschmiegt, und stellt die Rechenregeln bereit, mit denen man Ableitungen ausrechnet, ohne jedes Mal einen Grenzwert zu bilden. Am Ende steht die zweite Ableitung, die beschreibt, wie sich die Steigung selbst ändert.
:::

### Änderungsrate und Differenzenquotient

<span class="anker" id="stufe-1-1"></span>

Eine Funktion $f$ ordnet jeder Zahl $x$ eine Zahl $f(x)$ zu. Vergrößert man $x$ um ein kleines Stück $h$, ändert sich in der Regel auch der Wert, und zwar um $f(x+h)-f(x)$. Ob das viel oder wenig ist, sagt erst der Vergleich mit $h$: Eine Wertänderung von $0{,}1$ ist groß, wenn $x$ nur um $0{,}001$ gewachsen ist, und klein, wenn $x$ um $100$ gewachsen ist. Man teilt deshalb die beiden Änderungen durcheinander.

Im Bild des Graphen ist das eine Steigung. Man legt eine Gerade durch die beiden Punkte $(x,\,f(x))$ und $(x+h,\,f(x+h))$ des Graphen. Eine solche Gerade durch zwei Punkte einer Kurve heißt __Sekante__. Ihre Steigung ist der Höhenunterschied der beiden Punkte geteilt durch ihren waagrechten Abstand. Sie gibt an, wie stark der Graph zwischen den beiden Punkten im Mittel ansteigt.

:::definition Definition 1.1 (Differenzenquotient)
<span class="anker" id="satz-1-1"></span>

Für eine Funktion $f$, eine Stelle $x$ und eine Zahl $h\ne0$ heißt

<span class="anker" id="gl-1-1"></span>
$$\frac{f(x+h)-f(x)}{h} \tag{1.1}$$

der __Differenzenquotient__ von $f$ an der Stelle $x$ zur Schrittweite $h$. Er ist die Steigung der Sekante durch $(x,\,f(x))$ und $(x+h,\,f(x+h))$.
:::

Die Schrittweite $h$ darf auch negativ sein; dann liegt der zweite Punkt links von $x$. Für $h=0$ ist der Quotient nicht erklärt, weil man nicht durch null teilen kann.

⁠**Rechenbeispiel:** Es sei $f(x)=x^3$ und $x=2$, also $f(2)=8$. Für drei Schrittweiten ist

$$\frac{3^3-8}{1}=19,\qquad \frac{2{,}5^3-8}{0{,}5}=\frac{15{,}625-8}{0{,}5}=15{,}25,\qquad \frac{2{,}1^3-8}{0{,}1}=\frac{9{,}261-8}{0{,}1}=12{,}61 .$$

Die Sekanten werden flacher, je näher der zweite Punkt an $(2,\,8)$ heranrückt (Abb. [1](#abb-1)). Für ein beliebiges $h$ rechnet man mit $(2+h)^3=8+12h+6h^2+h^3$:

<span class="anker" id="gl-1-2"></span>
$$\frac{(2+h)^3-8}{h}=\frac{12h+6h^2+h^3}{h}=12+6h+h^2 . \tag{1.2}$$

Mit $h=1$, $h=0{,}5$ und $h=0{,}1$ ergibt diese Formel wieder $19$, $15{,}25$ und $12{,}61$. Mit $h=0{,}01$ ergibt sie $12{,}0601$, mit $h=-0{,}1$ ergibt sie $12-0{,}6+0{,}01=11{,}41$.

:::abbildung ml/k3sekante 1
Sekanten des Graphen von $f(x)=x^3$ durch den Punkt $(2,\,8)$, mit den Steigungen $19$ für $h=1$ (rot) und $15{,}25$ für $h=0{,}5$ (orange). Mit kleinerer Schrittweite $h$ rückt der zweite Punkt näher heran, die Sekante wird flacher, und ihre Steigung $12+6h+h^2$ nähert sich der Steigung $12$ der Tangente (gestrichelt).
:::

⁠**Kurz gesagt:** Der Differenzenquotient ist die Änderung des Funktionswerts geteilt durch die Änderung der Eingabe, die mittlere Steigung zwischen zwei Punkten des Graphen.

### Die Ableitung

<span class="anker" id="stufe-1-2"></span>

Im Rechenbeispiel liegen die Sekantensteigungen umso näher bei $12$, je kleiner $|h|$ ist, und zwar von beiden Seiten: $12{,}61$ für $h=0{,}1$, $11{,}41$ für $h=-0{,}1$. Den Wert $12$ selbst erreichen sie für kein $h\ne0$, aber sie kommen ihm beliebig nahe. Man nennt $12$ deshalb den Grenzwert der Sekantensteigungen. Allgemein hat eine Größe, die von $h$ abhängt, für $h\to0$ den __Grenzwert__ $c$, wenn sie beliebig nah an $c$ liegt, sobald $h$ nah genug bei $0$ liegt und nicht gleich $0$ ist. Dabei zählen positive und negative $h$ gleichermaßen.

:::definition Definition 1.2 (Ableitung)
<span class="anker" id="satz-1-2"></span>

Eine Funktion $f$ heißt an der Stelle $x$ __differenzierbar__, wenn der Differenzenquotient für $h\to0$ einen Grenzwert hat. Dieser Grenzwert

<span class="anker" id="gl-1-3"></span>
$$f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h} \tag{1.3}$$

heißt die __Ableitung__ von $f$ an der Stelle $x$. Man schreibt auch $\frac{\mathrm{d} f}{\mathrm{d} x}(x)$. Die Gerade durch $(x,\,f(x))$ mit der Steigung $f'(x)$ heißt __Tangente__ an den Graphen.
:::

Ist $f$ an jeder Stelle differenzierbar, so ist $f'$ wieder eine Funktion: Sie ordnet jedem $x$ die Steigung des Graphen an dieser Stelle zu. Sie heißt Ableitungsfunktion oder kurz ebenfalls Ableitung. Die Schreibweise $\frac{\mathrm{d} f}{\mathrm{d} x}$ erinnert an den Quotienten aus [(1.1)](#gl-1-1), ist aber selbst kein Bruch, sondern das Zeichen für den Grenzwert.

⁠**Rechenbeispiel 1:** Nach [(1.2)](#gl-1-2) ist der Differenzenquotient von $f(x)=x^3$ an der Stelle $2$ gleich $12+6h+h^2$. Für $h\to0$ werden $6h$ und $h^2$ beliebig klein, also ist $f'(2)=12$. Dieselbe Rechnung an einer beliebigen Stelle $x$ ergibt mit $(x+h)^3=x^3+3x^2h+3xh^2+h^3$ den Quotienten $3x^2+3xh+h^2$ und damit $f'(x)=3x^2$.

⁠**Rechenbeispiel 2:** Die Betragsfunktion $f(x)=|x|$ hat an der Stelle $0$ keine Ableitung. Ihr Differenzenquotient ist $|h|/h$, also $1$ für jedes $h>0$ und $-1$ für jedes $h<0$. Es gibt keine Zahl, der er von beiden Seiten nahekommt. Der Graph hat bei $0$ einen __Knick__: Links steigt er mit $-1$, rechts mit $+1$, und keine Gerade schmiegt sich beiden Seiten zugleich an. An jeder anderen Stelle ist $|x|$ differenzierbar, mit der Ableitung $1$ für $x>0$ und $-1$ für $x<0$.

⁠**Kurz gesagt:** Die Ableitung $f'(x)$ ist der Grenzwert der Sekantensteigungen, also die Steigung der Tangente; an einem Knick gibt es sie nicht.

### Die lineare Näherung

<span class="anker" id="stufe-1-3"></span>

Wozu braucht man die Tangente? Betrachtet man einen glatten Graphen durch eine immer stärkere Lupe, so sieht man von ihm immer weniger Krümmung. Im starken Vergrößerungsglas ist von der Kurve nur noch ein gerades Stück übrig, und dieses Stück liegt auf der Tangente (Abb. [2](#abb-2)). In der Nähe der Stelle $x$ darf man die Funktion deshalb durch ihre Tangente ersetzen. Mit einer Geraden rechnet es sich viel leichter als mit der Funktion selbst.

:::abbildung ml/k3lupe 2
Die Lupe: der Graph von $f(x)=x^3$ (blau) und seine Tangente $8+12\,(x-2)$ an der Stelle $2$ (rot gestrichelt) in drei Ausschnitten, jeder zehnmal schmaler als der vorige. Im letzten Ausschnitt sind Kurve und Tangente nicht mehr zu unterscheiden.
:::

:::satz Satz 1.3 (Lineare Näherung)
<span class="anker" id="satz-1-3"></span>

Ist $f$ an der Stelle $x$ differenzierbar, so gilt

<span class="anker" id="gl-1-4"></span>
$$f(x+h)=f(x)+f'(x)\,h+r(h)\qquad\text{mit}\qquad \lim_{h\to0}\frac{r(h)}{h}=0 . \tag{1.4}$$

Der Ausdruck $f(x)+f'(x)\,h$ heißt die __lineare Näherung__ von $f$ an der Stelle $x$, und $r(h)$ ist ihr Fehler.
:::

:::beweis Lineare Näherung
Man setzt $r(h)=f(x+h)-f(x)-f'(x)\,h$; dann gilt die Gleichung links nach Konstruktion. Für $h\ne0$ ist

$$\frac{r(h)}{h}=\frac{f(x+h)-f(x)}{h}-f'(x),$$

und nach [(1.3)](#gl-1-3) geht der erste Summand gegen $f'(x)$, die Differenz also gegen $0$.
:::

Die Bedingung $r(h)/h\to0$ sagt mehr, als dass der Fehler klein wird. Auch $h$ selbst wird klein; entscheidend ist, dass der Fehler schneller verschwindet als $h$. Halbiert man $h$, so wird die Änderung $f'(x)\,h$ halb so groß, der Fehler aber deutlich mehr als halb so klein. Das ist die genaue Bedeutung der Lupe.

Die Gleichung [(1.4)](#gl-1-4) liefert auch die anschaulichste Deutung der Ableitung. Eine kleine Änderung $h$ der Eingabe kommt am Ausgang ungefähr als $f'(x)\,h$ an. Die Ableitung ist also der *Faktor*, mit dem die Funktion kleine Änderungen weitergibt, ihre Empfindlichkeit an der Stelle $x$. Ein großes $|f'(x)|$ bedeutet, dass schon kleine Änderungen der Eingabe den Wert stark verändern; ein negatives $f'(x)$ bedeutet, dass der Wert fällt, wenn die Eingabe wächst.

⁠**Rechenbeispiel:** Für $f(x)=x^3$ an der Stelle $2$ und $h=0{,}01$ liefert die lineare Näherung

$$f(2{,}01)\approx8+12\cdot0{,}01=8{,}12 .$$

Genau ist $f(2{,}01)=2{,}01^3=8{,}120601$. Der Fehler ist $r(0{,}01)=0{,}000601$, nach der Rechnung zu [(1.2)](#gl-1-2) allgemein $r(h)=6h^2+h^3$. Der Quotient $r(h)/h=6h+h^2$ ist für $h=0{,}01$ gleich $0{,}0601$ und für $h=0{,}001$ gleich $0{,}006001$: Er geht gegen null, wie der Satz verlangt.

⁠**Kurz gesagt:** Nahe bei $x$ ist $f(x+h)\approx f(x)+f'(x)\,h$; die Ableitung ist der Faktor, mit dem kleine Änderungen weitergegeben werden, und der Fehler verschwindet schneller als $h$.

:::hintergrund Warum gerade die Tangente die beste Gerade ist
Jede Gerade durch den Punkt $(x,\,f(x))$ liefert eine Näherung $f(x+h)\approx f(x)+m\,h$ mit irgendeiner Steigung $m$. Ihr Fehler ist $f(x+h)-f(x)-m\,h$. Teilt man ihn durch $h$, so erhält man den Differenzenquotienten minus $m$, und das geht für $h\to0$ gegen $f'(x)-m$. Nur für $m=f'(x)$ ist dieser Grenzwert null. Für jede andere Steigung bleibt der Fehler auf Dauer etwa $|f'(x)-m|\cdot|h|$ groß, er schrumpft also nur so schnell wie $h$ selbst. Die Tangente ist demnach die einzige Gerade durch den Punkt, deren Fehler schneller als $h$ verschwindet. In diesem Sinn ist sie die beste lineare Näherung, und genau so lässt sich die Ableitung auch definieren: als die eine Zahl $m$, für die $f(x+h)-f(x)-m\,h$ schneller als $h$ gegen null geht. Diese Form der Definition hat den Vorteil, dass sie sich ohne Änderung auf Funktionen mit vielen Eingängen überträgt, wo es keinen Quotienten mehr gibt, weil man nicht durch einen Vektor teilen kann. Abschnitt [3](partielle-ableitungen-und-der-gradient.html#stufe-3) macht davon Gebrauch.
:::

### Ableitungsregeln

<span class="anker" id="stufe-1-4"></span>

Jede Ableitung über den Grenzwert auszurechnen ist mühsam. Zum Glück genügen wenige Grundableitungen und vier Regeln, um fast jede Formel abzuleiten, die aus Grundrechenarten und bekannten Funktionen zusammengesetzt ist. Tabelle [1](#tab-1) stellt die Grundableitungen zusammen, die dieses Kapitel benutzt.

<span class="anker" id="tab-1"></span>

**Tabelle 1:** Grundableitungen. Die Potenzregel gilt für jede reelle Hochzahl $n$, für nicht ganzzahlige $n$ nur bei $x>0$. Die Winkel in $\sin$ und $\cos$ sind im Bogenmaß gemessen.

| Funktion $f(x)$ | Ableitung $f'(x)$ | Beispiel |
|---|---|---|
| $c$ (Konstante) | $0$ | $f(x)=7$: $f'(x)=0$ |
| $x^n$ | $n\,x^{n-1}$ | $x^3\mapsto3x^2$, $\ \tfrac1x=x^{-1}\mapsto-\tfrac1{x^2}$, $\ \sqrt x=x^{1/2}\mapsto\tfrac1{2\sqrt x}$ |
| $\mathrm{e}^x$ | $\mathrm{e}^x$ | an der Stelle $0$: Steigung $1$ |
| $\ln x$ ($x>0$) | $\tfrac1x$ | an der Stelle $1$: Steigung $1$ |
| $\sin x$ | $\cos x$ | an der Stelle $0$: Steigung $1$ |
| $\cos x$ | $-\sin x$ | an der Stelle $0$: Steigung $0$ |

:::satz Satz 1.4 (Ableitungsregeln)
<span class="anker" id="satz-1-4"></span>

Sind $u$ und $v$ an der Stelle $x$ differenzierbar und ist $c$ eine Zahl, so gilt dort:

<span class="anker" id="gl-1-5"></span>
$$\begin{aligned} (u+v)'&=u'+v' &&\text{(Summenregel)}\\ (c\,u)'&=c\,u' &&\text{(Faktorregel)}\\ (u\,v)'&=u'\,v+u\,v' &&\text{(Produktregel)}\\ \Bigl(\frac uv\Bigr)'&=\frac{u'\,v-u\,v'}{v^2}\quad\text{falls }v(x)\ne0 &&\text{(Quotientenregel)} \end{aligned} \tag{1.5}$$
:::

Die ersten beiden Regeln folgen sofort aus der Definition, weil sich Differenzenquotienten von Summen und Vielfachen genauso zerlegen. Die Produktregel ist weniger offensichtlich. Ein Bild macht sie klar: Man denke sich $u\,v$ als Fläche eines Rechtecks mit den Seiten $u$ und $v$. Wachsen die Seiten um $\Delta u$ und $\Delta v$, so kommen drei Streifen hinzu: $u\,\Delta v$, $v\,\Delta u$ und das kleine Eckstück $\Delta u\,\Delta v$. Bei kleinen Änderungen ist das Eckstück ein Produkt zweier kleiner Größen und verschwindet schneller als die beiden Streifen. Übrig bleibt $\Delta(uv)\approx v\,\Delta u+u\,\Delta v$, und Teilen durch $h$ ergibt die Produktregel.

:::beweis Produktregel und Potenzregel
Mit $\Delta u=u(x+h)-u(x)$ und $\Delta v=v(x+h)-v(x)$ ist genau

$$u(x+h)\,v(x+h)-u(x)\,v(x)=v(x)\,\Delta u+u(x)\,\Delta v+\Delta u\,\Delta v .$$

Teilt man durch $h$, so gehen $\Delta u/h$ gegen $u'(x)$ und $\Delta v/h$ gegen $v'(x)$. Der letzte Summand ist $(\Delta u/h)\cdot\Delta v$; sein erster Faktor geht gegen $u'(x)$, sein zweiter gegen $0$, denn eine differenzierbare Funktion ändert sich bei kleinem $h$ nur wenig. Also geht der ganze Quotient gegen $u'(x)\,v(x)+u(x)\,v'(x)$.

Für die Potenzregel mit einer natürlichen Zahl $n$ multipliziert man $(x+h)^n$ aus. Nach dem binomischen Lehrsatz ist

$$(x+h)^n=x^n+n\,x^{n-1}h+(\text{Summanden mit }h^2,h^3,\dots,h^n),$$

also ist der Differenzenquotient $n\,x^{n-1}$ plus Summanden, die noch mindestens ein $h$ enthalten. Für $h\to0$ bleibt $n\,x^{n-1}$. Die Quotientenregel folgt aus der Produktregel, angewandt auf $u=(u/v)\cdot v$.
:::

⁠**Rechenbeispiel:** Es sei $f(x)=(x^2+1)(x-3)$ und gesucht ist $f'(2)$. Mit $u=x^2+1$, $u'=2x$, $v=x-3$, $v'=1$ liefert die Produktregel

$$f'(x)=2x\,(x-3)+(x^2+1)\cdot1,\qquad f'(2)=4\cdot(-1)+5\cdot1=1 .$$

Probe: Ausmultipliziert ist $f(x)=x^3-3x^2+x-3$, also $f'(x)=3x^2-6x+1$ und $f'(2)=12-12+1=1$.

⁠**Kurz gesagt:** Mit den Grundableitungen der Tabelle und den Regeln für Summe, Vielfaches, Produkt und Quotient leitet man zusammengesetzte Formeln ab, ohne einen Grenzwert zu bilden.

:::hintergrund Warum die e-Funktion ihre eigene Ableitung ist
Für jede Basis $a>0$ ist $a^{x+h}-a^x=a^x\,(a^h-1)$. Der Differenzenquotient von $a^x$ ist deshalb $a^x$ mal dem Differenzenquotienten von $a^x$ an der Stelle $0$, also $a^x\cdot\frac{a^h-1}{h}$: Die Steigung an jeder Stelle ist der Funktionswert mal der Steigung an der Stelle $0$. Für $a=2$ ist diese Steigung an der Stelle $0$ etwa $0{,}693$, für $a=3$ etwa $1{,}099$. Dazwischen gibt es genau eine Basis, für die sie $1$ ist, und diese Basis ist die Eulersche Zahl $\mathrm{e}\approx2{,}718$. Für sie ist die Steigung überall gleich dem Funktionswert. Die Ableitung von $\ln x$ folgt daraus, denn der Logarithmus macht die e-Funktion rückgängig: Ist $y=\ln x$, so ist $x=\mathrm{e}^y$, und eine kleine Änderung von $y$ verändert $x$ um das $\mathrm{e}^y=x$-fache. Umgekehrt verändert eine kleine Änderung von $x$ also $y$ um das $1/x$-fache.
:::

### Die zweite Ableitung und die quadratische Näherung

<span class="anker" id="stufe-1-5"></span>

Die Tangente gibt die Richtung des Graphen an, aber nicht, wie er sich von ihr wegbiegt. Ob die Kurve nach oben oder nach unten von der Tangente abweicht und wie stark, hängt davon ab, wie sich die Steigung selbst ändert. Diese Änderung misst man wieder mit einer Ableitung, nämlich mit der Ableitung der Ableitung.

:::definition Definition 1.5 (Höhere Ableitungen)
<span class="anker" id="satz-1-5"></span>

Ist die Ableitungsfunktion $f'$ an der Stelle $x$ differenzierbar, so heißt $f''(x)=(f')'(x)$ die __zweite Ableitung__ von $f$ an der Stelle $x$. Entsprechend ist $f'''=(f'')'$ die dritte Ableitung, und allgemein schreibt man $f^{(k)}$ für die $k$-te Ableitung.
:::

Ist $f''(x)>0$, so wächst die Steigung bei $x$; der Graph biegt sich nach oben von der Tangente weg und liegt in der Nähe von $x$ über ihr. Ist $f''(x)<0$, biegt er sich nach unten. Die zweite Ableitung misst also die __Krümmung__ des Graphen, genauer: wie schnell sich seine Steigung ändert.

Mit der zweiten Ableitung wird die Näherung genauer. Man ersetzt die Tangente durch die Parabel, die an der Stelle $x$ denselben Wert, dieselbe Steigung und dieselbe zweite Ableitung hat wie $f$. Eine Parabel $p(h)=a+b\,h+c\,h^2$ hat $p(0)=a$, $p'(0)=b$ und $p''(0)=2c$. Damit diese drei Zahlen zu $f(x)$, $f'(x)$ und $f''(x)$ passen, muss $a=f(x)$, $b=f'(x)$ und $c=\tfrac12f''(x)$ sein. Daher kommt der Faktor $\tfrac12$.

:::satz Satz 1.6 (Quadratische Näherung)
<span class="anker" id="satz-1-6"></span>

Ist $f$ in der Nähe von $x$ zweimal differenzierbar und $f''$ an der Stelle $x$ stetig, so gilt

<span class="anker" id="gl-1-6"></span>
$$f(x+h)=f(x)+f'(x)\,h+\tfrac12f''(x)\,h^2+r_2(h)\qquad\text{mit}\qquad\lim_{h\to0}\frac{r_2(h)}{h^2}=0 . \tag{1.6}$$
:::

Stetig heißt dabei, dass sich $f''$ bei kleinen Änderungen der Stelle nur wenig ändert, ohne Sprung. Den Beweis führt man ähnlich wie bei der linearen Näherung, mit einem Schritt mehr; die Aussage heißt Satz von Taylor. Der Fehler $r_2(h)$ verschwindet jetzt schneller als $h^2$, also bei kleinem $h$ noch viel schneller als der Fehler der linearen Näherung.

⁠**Rechenbeispiel:** Für $f(x)=x^3$ ist $f'(x)=3x^2$, $f''(x)=6x$ und $f'''(x)=6$. An der Stelle $2$ ist $f''(2)=12>0$: Der Graph biegt sich nach oben von der Tangente weg, wie Abb. [2](#abb-2) links zeigt. Die quadratische Näherung für $h=0{,}01$ ist

$$f(2{,}01)\approx8+12\cdot0{,}01+\tfrac12\cdot12\cdot0{,}01^2=8+0{,}12+0{,}0006=8{,}1206 .$$

Der genaue Wert ist $8{,}120601$, der Fehler nur noch $0{,}000001=h^3$. Abb. [3](#abb-3) zeigt die Summe der drei Glieder.

:::abbildung ml/k3rtaylor1 3
Die quadratische Näherung von $f(x)=x^3$ an der Stelle $2$ für $h=0{,}01$ als Summe aus Wert, Steigungsglied und Krümmungsglied.
:::

⁠**Kurz gesagt:** Die zweite Ableitung misst, wie schnell sich die Steigung ändert, also die Krümmung; mit ihr wird die Näherung zu $f(x+h)\approx f(x)+f'(x)\,h+\tfrac12f''(x)\,h^2$.

:::hintergrund Taylorpolynome höherer Ordnung
Man kann weitergehen und auch die dritte und alle weiteren Ableitungen anpassen. Das Polynom

$$f(x)+f'(x)\,h+\frac{f''(x)}{2}\,h^2+\frac{f'''(x)}{6}\,h^3+\dots+\frac{f^{(k)}(x)}{k!}\,h^k$$

heißt Taylorpolynom $k$-ter Ordnung; dabei ist $k!=1\cdot2\cdots k$. Die Nenner $k!$ kommen wie der Faktor $\tfrac12$ daher, dass die $k$-te Ableitung von $h^k$ gleich $k!$ ist. Für $f(x)=x^3$ ist schon das Taylorpolynom dritter Ordnung exakt: $8+12h+6h^2+h^3$ ist genau $(2+h)^3$. Für die meisten Funktionen wird die Näherung mit jeder Ordnung besser, solange $h$ klein genug ist. Für dieses Kapitel genügen die Ordnungen eins und zwei.
:::

:::aufgabe Aufgabe 1 ★ Sekanten und Tangente
<span class="anker" id="aufg-1"></span>

Es sei $f(x)=x^2$.

<ol class="al">

<li>

Berechne den Differenzenquotienten an der Stelle $3$ für $h=1$, $h=0{,}1$ und $h=-0{,}1$.

</li>

<li>

Zeige, dass der Differenzenquotient an der Stelle $3$ gleich $6+h$ ist, und bestimme $f'(3)$.

</li>

<li>

Gib die Tangente an der Stelle $3$ an und berechne mit ihr eine Näherung für $3{,}02^2$. Wie groß ist der Fehler?

</li>

</ol>

:::loesung
(a) Mit $f(3)=9$ ist

$$\frac{4^2-9}{1}=7,\qquad \frac{3{,}1^2-9}{0{,}1}=\frac{9{,}61-9}{0{,}1}=6{,}1,\qquad \frac{2{,}9^2-9}{-0{,}1}=\frac{8{,}41-9}{-0{,}1}=5{,}9 .$$

Die Sekante nach rechts ist steiler, die nach links flacher als die Tangente, weil der Graph der Parabel nach oben gekrümmt ist.

(b) $(3+h)^2=9+6h+h^2$, also ist der Differenzenquotient $\frac{6h+h^2}{h}=6+h$. Für $h\to0$ geht er von beiden Seiten gegen $6$; es ist $f'(3)=6$, passend zur Regel $(x^2)'=2x$.

(c) Die Tangente ist $t(x)=9+6\,(x-3)$. Sie liefert $3{,}02^2\approx9+6\cdot0{,}02=9{,}12$. Genau ist $3{,}02^2=9{,}1204$. Der Fehler $0{,}0004=0{,}02^2$ ist genau $h^2$, denn $f(3+h)-9-6h=h^2$. Er verschwindet schneller als $h$, wie die lineare Näherung verspricht.
:::
:::

:::aufgabe Aufgabe 2 ★ Ableiten mit den Regeln
<span class="anker" id="aufg-2"></span>

Leite ab und werte an der angegebenen Stelle aus.

<ol class="al">

<li>

$f(x)=4x^3-2x+7$ an der Stelle $1$;

</li>

<li>

$f(x)=x^2\,\mathrm{e}^x$ an den Stellen $0$ und $1$;

</li>

<li>

$f(x)=\dfrac{x}{1+x^2}$ an den Stellen $0$ und $1$. Was bedeutet das Ergebnis an der Stelle $1$ für den Graphen?

</li>

</ol>

:::loesung
(a) Summen- und Faktorregel mit der Potenzregel: $f'(x)=12x^2-2$, also $f'(1)=10$.

(b) Produktregel mit $u=x^2$, $v=\mathrm{e}^x$: $f'(x)=2x\,\mathrm{e}^x+x^2\,\mathrm{e}^x=(2x+x^2)\,\mathrm{e}^x$. Also $f'(0)=0$ und $f'(1)=3\mathrm{e}\approx8{,}155$.

(c) Quotientenregel mit $u=x$, $u'=1$, $v=1+x^2$, $v'=2x$:

$$f'(x)=\frac{1\cdot(1+x^2)-x\cdot2x}{(1+x^2)^2}=\frac{1-x^2}{(1+x^2)^2},\qquad f'(0)=1,\qquad f'(1)=0 .$$

An der Stelle $1$ hat der Graph eine waagrechte Tangente. Dort liegt sein höchster Punkt: Für alle $x$ ist $\frac{x}{1+x^2}\le\frac12$, weil $1+x^2-2x=(x-1)^2\ge0$ ist, und $f(1)=\tfrac12$.
:::
:::

:::aufgabe Aufgabe 3 ★★ Wurzeln mit der Lupe
<span class="anker" id="aufg-3"></span>

Es sei $f(x)=\sqrt x$.

<ol class="al">

<li>

Berechne $f'(x)$ und $f''(x)$ mit der Potenzregel.

</li>

<li>

Berechne mit der linearen und mit der quadratischen Näherung an der Stelle $4$ einen Näherungswert für $\sqrt{4{,}1}$. Vergleiche beide mit dem Taschenrechner.

</li>

<li>

Liegt die Tangente über oder unter dem Graphen? Begründe mit dem Vorzeichen von $f''(4)$.

</li>

</ol>

:::loesung
(a) Mit $\sqrt x=x^{1/2}$ ist $f'(x)=\tfrac12x^{-1/2}=\frac1{2\sqrt x}$ und $f''(x)=-\tfrac14x^{-3/2}$.

(b) An der Stelle $4$ ist $f(4)=2$, $f'(4)=\tfrac14$ und $f''(4)=-\tfrac14\cdot\tfrac18=-\tfrac1{32}$. Mit $h=0{,}1$:

$$\text{linear: }2+\tfrac14\cdot0{,}1=2{,}025,\qquad \text{quadratisch: }2{,}025-\tfrac12\cdot\tfrac1{32}\cdot0{,}01=2{,}025-0{,}00015625=2{,}02484375 .$$

Der Taschenrechner gibt $\sqrt{4{,}1}\approx2{,}0248457$. Der Fehler der linearen Näherung ist etwa $1{,}5\cdot10^{-4}$, der der quadratischen nur etwa $1{,}9\cdot10^{-6}$.

(c) Wegen $f''(4)<0$ biegt sich der Graph nach unten von der Tangente weg; die Tangente liegt über dem Graphen. Deshalb ist die lineare Näherung $2{,}025$ zu groß.
:::
:::

:::aufgabe Aufgabe 4 ★★ Knick oder kein Knick
<span class="anker" id="aufg-4"></span>

<ol class="al">

<li>

Zeige mit dem Differenzenquotienten, dass $g(x)=x\,|x|$ an der Stelle $0$ differenzierbar ist, und bestimme $g'(0)$.

</li>

<li>

Bestimme $g'(x)$ für $x>0$ und für $x<0$. Hat $g'$ selbst an der Stelle $0$ eine Ableitung?

</li>

<li>

Die Funktion $m(x)=\max(x,\,0)$ gibt $x$ zurück, wenn $x$ positiv ist, und sonst $0$. Wo ist sie differenzierbar, und welche Werte haben dort ihre Ableitungen?

</li>

</ol>

:::loesung
(a) Es ist $g(0)=0$ und $\frac{g(h)-g(0)}{h}=\frac{h\,|h|}{h}=|h|$. Das geht von beiden Seiten gegen $0$, also ist $g'(0)=0$. Der Betrag allein hat einen Knick, aber der Faktor $x$ drückt die beiden Äste im Nullpunkt flach.

(b) Für $x>0$ ist $g(x)=x^2$ und $g'(x)=2x$; für $x<0$ ist $g(x)=-x^2$ und $g'(x)=-2x$. Zusammen mit (a) ist $g'(x)=2|x|$ für alle $x$. Diese Funktion hat bei $0$ einen Knick, ihr Differenzenquotient $2|h|/h$ ist $\pm2$. Also ist $g$ einmal, aber nicht zweimal differenzierbar.

(c) Für $x>0$ ist $m(x)=x$ mit $m'(x)=1$, für $x<0$ ist $m(x)=0$ mit $m'(x)=0$. An der Stelle $0$ ist der Differenzenquotient $1$ für $h>0$ und $0$ für $h<0$; dort gibt es keine Ableitung. Der Graph hat bei $0$ einen Knick.
:::
:::

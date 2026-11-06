---
title: Informationsgehalt und Entropie
pfad: Informatik / Machine Learning / Statistik und Information
order: 6250900
summary: Ein seltenes Ereignis überrascht mehr als ein häufiges.
tags: Informationsgehalt, nat, Entropie, Code, Präfixcode, Kraft-Ungleichung, binäre Entropie
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Ein seltenes Ereignis überrascht mehr als ein häufiges. Dieser Abschnitt macht aus der Überraschung ein Maß, den Informationsgehalt, mittelt ihn über eine Verteilung zur Entropie und zeigt, dass die Entropie angibt, wie viele Binärziffern man im Mittel braucht, um die Ergebnisse eines Zufallsexperiments aufzuschreiben.
:::

### Der Informationsgehalt

<span class="anker" id="stufe-8-1"></span>

Die Nachricht „Die Münze zeigt Kopf“ überrascht wenig, die Nachricht „Der Würfel zeigt viermal hintereinander eine Sechs“ deutlich mehr, und die Nachricht „Die Sonne ist aufgegangen“ gar nicht. Ein Maß für die Überraschung, die ein Ereignis $A$ beim Eintreten auslöst, sollte vier Forderungen erfüllen. Es hängt nur von $P(A)$ ab. Es ist umso größer, je kleiner $P(A)$ ist. Ein sicheres Ereignis überrascht gar nicht. Und für zwei unabhängige Ereignisse addieren sich die Überraschungen: Wer erfährt, dass zwei unabhängige Münzen beide Kopf zeigen, hat zweimal die Überraschung eines Kopfs erlebt. Weil sich bei unabhängigen Ereignissen die Wahrscheinlichkeiten multiplizieren, muss das Maß aus einem Produkt eine Summe machen. Das tut der Logarithmus.

:::definition Definition 8.1 (Informationsgehalt)
<span class="anker" id="satz-8-1"></span>

Der __Informationsgehalt__ eines Ereignisses $A$ mit $P(A)>0$ ist

<span class="anker" id="gl-8-1"></span>
$$I(A)=\log_2\frac1{P(A)}=-\log_2P(A)\quad\text{bit}. \tag{8.1}$$

Mit $\ln$ statt $\log_2$ misst man ihn in __nat__.
:::

Die Einheit bit steht für *binary digit*, Binärziffer: Ein Ereignis mit der Wahrscheinlichkeit $\tfrac12$ hat den Informationsgehalt $1$ bit, ein Ereignis mit der Wahrscheinlichkeit $2^{-k}$ hat $k$ bit, so viel, wie man braucht, um einen von $2^k$ gleich wahrscheinlichen Fällen mit Binärziffern zu benennen. Nach [(4.2)](die-likelihood.html#gl-4-2) ist der Informationsgehalt in nat das $\ln2$-Fache des Werts in bit: $1\,\mathrm{bit}=\ln2\approx0{,}693\,\mathrm{nat}$ und $1\,\mathrm{nat}=1/\ln2\approx1{,}443\,\mathrm{bit}$. Die Überraschung $-\ln P(X=x_i\mid\theta)$ aus dem Hintergrund-Kasten in Unterabschnitt [5.2](die-maximum-likelihood-schatzung.html#stufe-5-2) ist der Informationsgehalt des Datenpunkts $x_i$ unter dem Modell $\theta$, gemessen in nat.

⁠**Rechenbeispiel:** Kopf bei einer fairen Münze hat $\log_22=1$ bit. Eine Sechs beim Würfel hat $\log_26\approx2{,}585$ bit, viermal hintereinander eine Sechs $4\cdot2{,}585=10{,}34$ bit. Eine bestimmte Karte aus einem Spiel mit $32$ Karten hat $\log_232=5$ bit. Ein Ereignis mit der Wahrscheinlichkeit $\tfrac1{1024}$ hat $10$ bit, ein sicheres Ereignis $0$ bit.

⁠**Kurz gesagt:** Der Informationsgehalt $\log_2(1/P(A))$ misst die Überraschung über ein Ereignis in bit; seltene Ereignisse tragen viel Information, und unabhängige Informationen addieren sich.

:::herleitung Warum es der Logarithmus sein muss
Es sei $I(A)=f(P(A))$ mit einer Funktion $f$, die fällt und für unabhängige Ereignisse $f(pq)=f(p)+f(q)$ erfüllt. Man setzt $g(t)=f(2^{-t})$ für $t\ge0$. Aus $2^{-s}\cdot2^{-t}=2^{-(s+t)}$ folgt $g(s+t)=g(s)+g(t)$. Damit ist $g(kt)=k\,g(t)$ für jede natürliche Zahl $k$, und mit $t=1/m$ auch $g(1)=m\,g(1/m)$, also $g(k/m)=\frac km\,g(1)$ für alle Brüche. Weil $g$ wächst, liegt $g(t)$ für jedes reelle $t$ zwischen den Werten an den Brüchen links und rechts davon, und es folgt $g(t)=c\,t$ mit $c=g(1)>0$. Zurückgerechnet ist $f(p)=c\log_2\frac1p$. Bis auf die Wahl der Einheit, also der Zahl $c$, ist der Informationsgehalt durch die Forderungen festgelegt.
:::

:::hintergrund Shannon und das Bit
Der amerikanische Ingenieur Claude Shannon hat 1948 in seiner Arbeit „A Mathematical Theory of Communication“ die Informationstheorie begründet, die die Nachrichtentechnik bis heute trägt. Den Namen bit für die Einheit zur Basis $2$ übernahm er nach eigener Angabe von seinem Kollegen John Tukey. Shannon begründete seine Formeln mit Forderungen wie den obigen, schrieb aber selbst, dass diese Forderungen für seine Theorie nicht nötig seien: Die eigentliche Rechtfertigung der Definitionen liege in ihren Folgerungen. Die wichtigste dieser Folgerungen zeigt Unterabschnitt [8.3](#stufe-8-3).
:::

### Die Entropie

<span class="anker" id="stufe-8-2"></span>

Ein Zufallsexperiment mit $K$ möglichen Ergebnissen liefert bei jeder Durchführung eine Überraschung. Wie groß ist sie im Mittel? Hat das Ergebnis $k$ die Wahrscheinlichkeit $p_k$ und den Informationsgehalt $\log_2(1/p_k)$, so ist der Erwartungswert nach [Teil 4](/wissen/informatik/machine-learning/wahrscheinlichkeit/wahrscheinlichkeit.html), Abschnitt 7.2, die mit $p_k$ gewichtete Summe. Die Wahrscheinlichkeiten schreibt man wie in [Teil 4](/wissen/informatik/machine-learning/wahrscheinlichkeit/wahrscheinlichkeit.html), Abschnitt 7.1, als Vektor $\mathbf{p}=(p_1,\dots,p_K)^{\top}$ mit $p_k\ge0$ und $\sum_kp_k=1$.

:::definition Definition 8.2 (Entropie)
<span class="anker" id="satz-8-2"></span>

Die __Entropie__ einer Verteilung $\mathbf{p}=(p_1,\dots,p_K)^{\top}$ ist der Erwartungswert des Informationsgehalts:

<span class="anker" id="gl-8-2"></span>
$$H(\mathbf{p})=\sum_{k=1}^Kp_k\log_2\frac1{p_k}\quad\text{bit}. \tag{8.2}$$

Summanden mit $p_k=0$ lässt man weg. Mit $\ln$ statt $\log_2$ misst man die Entropie in nat.
:::

Das Weglassen ist sinnvoll, weil $p\log_2(1/p)$ für $p\to0$ gegen null geht: Ein Ergebnis, das nie eintritt, trägt zur mittleren Überraschung nichts bei. Viele Texte schreiben die Entropie einer Zufallsvariablen $X$ als $H(X)$. Das kursive $H$ mit einer Verteilung als Argument ist eine Zahl; es hat nichts mit der fett geschriebenen Hesse-Matrix $\mathbf{H}_f$ aus [Teil 3](/wissen/informatik/machine-learning/ableitung-gradient-und-kettenregel/ableitung-gradient-und-kettenregel.html), Abschnitt 8, zu tun, die zu einer Funktion $f$ gehört.

:::satz Satz 8.3 (Die Entropie ist nicht negativ)
<span class="anker" id="satz-8-3"></span>

Es ist $H(\mathbf{p})\ge0$, und $H(\mathbf{p})=0$ gilt genau dann, wenn ein $p_k$ gleich $1$ ist und alle anderen null sind.
:::

Denn jeder Summand $p_k\log_2(1/p_k)$ ist wegen $0<p_k\le1$ nicht negativ und nur für $p_k=1$ null. Die Entropie ist null genau dann, wenn das Ergebnis sicher ist.

⁠**Rechenbeispiel:** Eine Quelle sendet die Zeichen A, B, C, D mit den Wahrscheinlichkeiten $\mathbf{p}=(\tfrac12,\,\tfrac14,\,\tfrac18,\,\tfrac18)^{\top}$. Ihre Entropie ist $\tfrac74=1{,}75$ bit (Abb. [13](#abb-13)). Eine faire Münze hat die Entropie $1$ bit, ein fairer Würfel $\log_26\approx2{,}585$ bit. Eine Münze mit den Wahrscheinlichkeiten $0{,}9$ und $0{,}1$ hat $0{,}9\log_2\frac1{0{,}9}+0{,}1\log_2\frac1{0{,}1}\approx0{,}137+0{,}332=0{,}469$ bit: Ihr Ergebnis ist meistens vorhersagbar.

:::abbildung ml/k5rentropie 13
Die Entropie der Quelle mit $\mathbf{p}=(\tfrac12,\tfrac14,\tfrac18,\tfrac18)^{\top}$: jeder Informationsgehalt $\log_2(1/p_k)$, gewichtet mit seiner Wahrscheinlichkeit.
:::

⁠**Kurz gesagt:** Die Entropie ist die mittlere Überraschung einer Verteilung, $\sum_kp_k\log_2(1/p_k)$; sie ist null bei Gewissheit und umso größer, je weniger vorhersagbar das Ergebnis ist.

### Entropie und Codelänge

<span class="anker" id="stufe-8-3"></span>

Die Quelle aus dem vorigen Rechenbeispiel soll ihre Zeichen über eine Leitung schicken, die nur Nullen und Einsen überträgt. Ein __Code__ ordnet jedem Zeichen eine Folge von Binärziffern zu, sein Codewort. Der einfachste Code gibt jedem Zeichen zwei Ziffern: A $=00$, B $=01$, C $=10$, D $=11$. Besser ist es, häufigen Zeichen kurze Codewörter zu geben, wie im Morsealphabet, in dem das häufige E nur ein Punkt ist. Damit man die Folge ohne Trennzeichen wieder zerlegen kann, darf kein Codewort der Anfang eines anderen sein. Ein solcher Code heißt __Präfixcode__.

:::abbildung ml/k5code 14
Ein Präfixcode als Baum. Von der Wurzel oben führt jede gelesene Ziffer nach links ($0$) oder rechts ($1$), bis ein Blatt mit einem Zeichen erreicht ist; dann beginnt das nächste Codewort wieder oben. Weil die Zeichen nur an Blättern stehen, ist kein Codewort der Anfang eines anderen. Die Tiefe jedes Blatts ist $\log_2(1/p_k)$.
:::

Abb. [14](#abb-14) zeigt den Präfixcode A $=0$, B $=10$, C $=110$, D $=111$. Die Folge `0110100` zerfällt eindeutig in `0`, `110`, `10`, `0`, also A, C, B, A. Die mittlere Länge eines Codes mit den Codewortlängen $l_k$ ist der Erwartungswert $L=\sum_kp_k\,l_k$, das Skalarprodukt $\mathbf{p}^{\top}\mathbf l$ der Wahrscheinlichkeiten mit dem Vektor $\mathbf l=(l_1,\dots,l_K)^{\top}$ der Längen.

⁠**Rechenbeispiel:** Für den Code aus Abb. [14](#abb-14) ist $\mathbf l=(1,\,2,\,3,\,3)^{\top}$ und die mittlere Länge $1{,}75$ Ziffern je Zeichen (Abb. [15](#abb-15)), genau die Entropie. Der Code mit zwei Ziffern je Zeichen braucht $2$, also $14\,\%$ mehr. Dass beide Zahlen übereinstimmen, liegt daran, dass jede Codewortlänge genau der Informationsgehalt ihres Zeichens ist: $l_k=\log_2(1/p_k)$.

:::abbildung ml/k5rcode 15
Die mittlere Codewortlänge als Skalarprodukt der Wahrscheinlichkeiten mit den Codewortlängen, Komponente für Komponente.
:::

Lässt sich die Entropie unterbieten? Shannon hat gezeigt: nein.

:::satz Satz 8.4 (Quellencodierungssatz)
<span class="anker" id="satz-8-4"></span>

Für jeden Präfixcode mit den Codewortlängen $l_1,\dots,l_K$ gilt die __Kraft-Ungleichung__ $\sum_k2^{-l_k}\le1$, und seine mittlere Länge ist mindestens die Entropie:

<span class="anker" id="gl-8-3"></span>
$$L=\sum_{k=1}^Kp_k\,l_k\ge H(\mathbf{p}) . \tag{8.3}$$

Gleichheit gilt genau dann, wenn $l_k=\log_2(1/p_k)$ für alle $k$ ist. Umgekehrt gibt es immer einen Präfixcode mit $L<H(\mathbf{p})+1$.
:::

Die Kraft-Ungleichung sieht man am Baum. Ein Codewort der Länge $l$ belegt ein Blatt in der Tiefe $l$, und darunter hängen keine weiteren Codewörter. Denkt man sich den Baum bis zu einer großen Tiefe $T$ voll ausgebaut, so sperrt dieses Blatt $2^{T-l}$ der $2^T$ untersten Plätze, also den Anteil $2^{-l}$. Die gesperrten Anteile verschiedener Codewörter überlappen nicht, also ist ihre Summe höchstens $1$. Für den Code aus Abb. [14](#abb-14) ist sie $\tfrac12+\tfrac14+\tfrac18+\tfrac18=1$. Die untere Schranke [(8.3)](#gl-8-3) beweist Unterabschnitt [9.4](kreuzentropie-und-kl-divergenz.html#stufe-9-4). Für die obere wählt man $l_k=\lceil\log_2(1/p_k)\rceil$, die nächste ganze Zahl nach oben. Diese Längen erfüllen die Kraft-Ungleichung, weil $2^{-l_k}\le p_k$ ist, und jede Länge ist um weniger als $1$ größer als $\log_2(1/p_k)$. Zu Längen, die die Kraft-Ungleichung erfüllen, gibt es auch immer einen Präfixcode: Man vergibt die Codewörter der Länge nach, das kürzeste zuerst, und setzt jedes an den am weitesten links liegenden freien Platz seiner Tiefe; die gesperrten Anteile lassen dafür stets genug Platz.

⁠**Kurz gesagt:** Die Entropie ist die kleinste mittlere Codelänge, die ein Präfixcode erreichen kann; erreicht wird sie, wenn jedes Codewort so lang ist wie der Informationsgehalt seines Zeichens.

:::hintergrund Die Entropie in der Nachrichtentechnik
In der Nachrichtentechnik heißt das Verdichten einer Quelle auf möglichst wenige Binärziffern Quellencodierung. Der Satz sagt, wie weit man dabei gehen kann: bis zur Entropie, nicht weiter. Ein Verfahren, das für jede Verteilung den Präfixcode mit der kleinsten mittleren Länge findet, gab David Huffman 1952 an. Es fasst immer die zwei seltensten Zeichen zu einem neuen Zeichen zusammen und baut so den Baum von unten auf. Exakt erreicht wird die Entropie nur, wenn alle Wahrscheinlichkeiten Zweierpotenzen sind, sonst müssten die Codewörter gebrochene Längen haben. Fasst man aber viele Zeichen zu Blöcken zusammen und codiert die Blöcke, kommt man der Entropie je Zeichen beliebig nahe; Unterabschnitt [8.4](#stufe-8-4) rechnet ein Beispiel.
:::

### Die binäre Entropie

<span class="anker" id="stufe-8-4"></span>

Ein Ja-Nein-Experiment mit der Erfolgswahrscheinlichkeit $\theta$ hat die Entropie

<span class="anker" id="gl-8-4"></span>
$$H_{\mathrm b}(\theta)=\theta\log_2\frac1\theta+(1-\theta)\log_2\frac1{1-\theta}\quad\text{bit}, \tag{8.4}$$

die __binäre Entropie__. Sie ist die Entropie der Verteilung $\mathrm{Ber}(\theta)$, als Funktion von $\theta$ gelesen (Abb. [16](#abb-16)).

:::abbildung ml/k5entropie 16
Die binäre Entropie eines Ja-Nein-Experiments. Sie ist $1$ bit bei $\theta=\tfrac12$, wo das Ergebnis am wenigsten vorhersagbar ist, und fällt zu beiden Rändern auf $0$. Sie ist symmetrisch um $\tfrac12$: Ob Kopf oder Zahl der häufige Ausgang ist, ändert die Unvorhersagbarkeit nicht. Markiert sind $H_{\mathrm b}(0{,}7)\approx0{,}881$ und $H_{\mathrm b}(0{,}9)\approx0{,}469$ bit.
:::

:::satz Satz 8.5 (Größte binäre Entropie)
<span class="anker" id="satz-8-5"></span>

$H_{\mathrm b}$ ist am größten bei $\theta=\tfrac12$, mit dem Wert $1$ bit.
:::

:::herleitung Größte binäre Entropie
Mit $\log_2x=\ln x/\ln2$ und der Ableitung $(x\ln x)'=\ln x+1$ ist

$$H_{\mathrm b}'(\theta)=\frac1{\ln2}\bigl(-\ln\theta-1+\ln(1-\theta)+1\bigr)=\log_2\frac{1-\theta}\theta .$$

Für $\theta<\tfrac12$ ist $(1-\theta)/\theta>1$ und die Ableitung positiv, für $\theta>\tfrac12$ negativ. Nach dem Satz über den Vorzeichenwechsel in Unterabschnitt [5.1](die-maximum-likelihood-schatzung.html#stufe-5-1) liegt bei $\tfrac12$ der höchste Punkt, mit $H_{\mathrm b}(\tfrac12)=\tfrac12+\tfrac12=1$.
:::

Dieselbe Stelle hatte schon die Varianz $\theta(1-\theta)$ der Bernoulli-Verteilung als größten Wert, nach [Teil 4](/wissen/informatik/machine-learning/wahrscheinlichkeit/wahrscheinlichkeit.html), Abschnitt 8.1: Ein Ja-Nein-Ausgang ist am unsichersten, wenn beide Ausgänge gleich wahrscheinlich sind. Die verbogene Münze mit $\theta=0{,}7$ hat $H_{\mathrm b}(0{,}7)\approx0{,}881$ bit.

⁠**Rechenbeispiel:** Für eine Münze mit $\theta=0{,}9$ ist $H_{\mathrm b}(0{,}9)\approx0{,}469$ bit. Ein Präfixcode für einzelne Würfe braucht aber mindestens eine Ziffer je Wurf, denn es gibt nur zwei Zeichen. Fasst man je zwei Würfe zu einem Block zusammen, so haben die vier Blöcke KK, KZ, ZK, ZZ die Wahrscheinlichkeiten $0{,}81$, $0{,}09$, $0{,}09$, $0{,}01$. Der Präfixcode $0$, $10$, $110$, $111$ hat die mittlere Länge $0{,}81\cdot1+0{,}09\cdot2+0{,}09\cdot3+0{,}01\cdot3=1{,}29$ Ziffern je Block, also $0{,}645$ je Wurf. Mit längeren Blöcken kommt man der Entropie $0{,}469$ immer näher.

⁠**Kurz gesagt:** Die binäre Entropie $H_{\mathrm b}(\theta)$ ist $1$ bit bei $\theta=\tfrac12$ und fällt zu den Rändern auf null; sie misst, wie unvorhersagbar ein Ja-Nein-Ausgang ist.

:::aufgabe Aufgabe 33 ★ Informationsgehalt
<span class="anker" id="aufg-33"></span>

<ol class="al">

<li>

Welchen Informationsgehalt hat die Nachricht „Im Lotto 6 aus 49 wurden genau meine sechs Zahlen gezogen“? Es gibt $\binom{49}6=13\,983\,816$ Möglichkeiten.

</li>

<li>

Ein Würfel zeigt eine gerade Zahl. Wie viel bit sind das? Wie viel kommt hinzu, wenn man danach erfährt, dass es die Sechs war?

</li>

<li>

Rechne die Ergebnisse aus (a) in nat um.

</li>

</ol>

:::loesung
(a) $\log_2(13\,983\,816)\approx23{,}74$ bit.

(b) Eine gerade Zahl hat die Wahrscheinlichkeit $\tfrac12$, also $1$ bit. Unter den drei geraden Zahlen ist die Sechs eine, also kommen $\log_23\approx1{,}585$ bit hinzu. Zusammen sind das $2{,}585$ bit, genau der Informationsgehalt der Sechs: Informationen, die nacheinander kommen, addieren sich.

(c) $23{,}74\cdot\ln2\approx16{,}45$ nat.
:::
:::

:::aufgabe Aufgabe 34 ★ Entropien
<span class="anker" id="aufg-34"></span>

Berechne die Entropie in bit für

<ol class="al">

<li>

$\mathbf{p}=(\tfrac14,\tfrac14,\tfrac14,\tfrac14)^{\top}$ und $\mathbf{p}=(\tfrac12,\tfrac12,0,0)^{\top}$;

</li>

<li>

die Quelle mit acht Zeichen und den Wahrscheinlichkeiten $\tfrac12,\tfrac14,\tfrac18,\tfrac1{16},\tfrac1{64},\tfrac1{64},\tfrac1{64},\tfrac1{64}$;

</li>

<li>

die Augensumme zweier fairer Würfel.

</li>

</ol>

:::loesung
(a) $\log_24=2$ bit; $\tfrac12\cdot1+\tfrac12\cdot1=1$ bit, die beiden Nullen tragen nichts bei.

(b) $\tfrac12\cdot1+\tfrac14\cdot2+\tfrac18\cdot3+\tfrac1{16}\cdot4+4\cdot\tfrac1{64}\cdot6=\tfrac12+\tfrac12+\tfrac38+\tfrac14+\tfrac38=2$ bit.

(c) Die Summen $2$ bis $12$ haben die Wahrscheinlichkeiten $\tfrac1{36},\tfrac2{36},\dots,\tfrac6{36},\dots,\tfrac1{36}$. Die Entropie ist $\sum_kp_k\log_2\frac1{p_k}\approx3{,}274$ bit, weniger als die $\log_211\approx3{,}459$ bit für elf gleich wahrscheinliche Ergebnisse und weniger als die $2\log_26\approx5{,}17$ bit für das Paar der Augenzahlen: Die Summe verrät nicht, welcher Würfel was gezeigt hat.
:::
:::

:::aufgabe Aufgabe 35 ★★ Ein Code für acht Zeichen
<span class="anker" id="aufg-35"></span>

Gib für die Quelle aus Aufgabe [34](#aufg-34) (b) einen Präfixcode an, dessen mittlere Länge gleich der Entropie ist, und prüfe die Kraft-Ungleichung. Wie viele Ziffern je Zeichen braucht ein Code mit gleich langen Codewörtern?

:::loesung
Die Längen $l_k=\log_2(1/p_k)$ sind $1,2,3,4,6,6,6,6$, zum Beispiel mit dem Code $0$, $10$, $110$, $1110$, $111100$, $111101$, $111110$, $111111$. Kraft: $\tfrac12+\tfrac14+\tfrac18+\tfrac1{16}+4\cdot\tfrac1{64}=1$. Die mittlere Länge ist die Entropie $2$ bit. Ein Code mit gleich langen Codewörtern braucht für acht Zeichen $3$ Ziffern.
:::
:::

:::aufgabe Aufgabe 36 ★★ Entropie zweier unabhängiger Größen
<span class="anker" id="aufg-36"></span>

Zwei unabhängige Zufallsgrößen haben die Verteilungen $\mathbf{p}=(p_1,\dots,p_K)^{\top}$ und $\mathbf{q}=(q_1,\dots,q_M)^{\top}$. Das Paar hat die $KM$ Ergebnisse $(k,m)$ mit den Wahrscheinlichkeiten $p_kq_m$.

<ol class="al">

<li>

Zeige, dass die Entropie des Paars $H(\mathbf{p})+H(\mathbf{q})$ ist.

</li>

<li>

Prüfe das an zwei fairen Münzen und an einer fairen Münze zusammen mit einem fairen Würfel.

</li>

</ol>

:::loesung
(a) Mit $\log_2\frac1{p_kq_m}=\log_2\frac1{p_k}+\log_2\frac1{q_m}$ ist

$$\sum_{k,m}p_kq_m\log_2\frac1{p_kq_m}=\sum_kp_k\log_2\frac1{p_k}\sum_mq_m+\sum_mq_m\log_2\frac1{q_m}\sum_kp_k=H(\mathbf{p})+H(\mathbf{q}) .$$

(b) Zwei faire Münzen: vier gleich wahrscheinliche Paare, $\log_24=2=1+1$ bit. Münze und Würfel: zwölf gleich wahrscheinliche Paare, $\log_212=\log_22+\log_26\approx1+2{,}585=3{,}585$ bit.
:::
:::

:::aufgabe Aufgabe 37 ★★★ Drei Würfe in einem Block
<span class="anker" id="aufg-37"></span>

Eine Münze habe $\theta=0{,}9$. Fasse je drei Würfe zu einem Block zusammen.

<ol class="al">

<li>

Gib die acht Blöcke mit ihren Wahrscheinlichkeiten an.

</li>

<li>

Der Präfixcode habe für KKK die Länge $1$, für die drei Blöcke mit einem Z die Längen $3$, $3$, $3$ und für die vier übrigen Blöcke die Länge $5$. Prüfe die Kraft-Ungleichung und berechne die mittlere Länge je Wurf. Vergleiche mit $0{,}645$ und $0{,}469$.

</li>

</ol>

:::loesung
(a) KKK: $0{,}729$; die drei Blöcke mit einem Z: je $0{,}081$; die drei mit zwei Z: je $0{,}009$; ZZZ: $0{,}001$.

(b) Kraft: $\tfrac12+3\cdot\tfrac18+4\cdot\tfrac1{32}=\tfrac12+\tfrac38+\tfrac18=1$. Die mittlere Länge je Block ist $0{,}729\cdot1+3\cdot0{,}081\cdot3+(3\cdot0{,}009+0{,}001)\cdot5=0{,}729+0{,}729+0{,}14=1{,}598$, je Wurf $0{,}533$. Das ist besser als die $0{,}645$ der Zweierblöcke und kommt der Entropie $0{,}469$ näher.
:::
:::

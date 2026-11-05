---
title: Automatische Differentiation
pfad: Informatik / Machine Learning / Ableitung, Gradient und Kettenregel
order: 6231100
summary: Mit dem Rechengraphen lassen sich Ableitungen mechanisch berechnen, ohne Formeln umzuformen und genau bis auf die Rundung der Grundoperationen.
tags: Automatische Differentiation, Vorwärtsmodus, Tangentenwert, Adjungierte, Rückwärtsmodus
lang: de
---

<span class="anker" id="stufe-10"></span>

:::zweck
Mit dem Rechengraphen lassen sich Ableitungen mechanisch berechnen, ohne Formeln umzuformen und genau bis auf die Rundung der Grundoperationen. Das heißt automatische Differentiation. Es gibt zwei Arten, die lokalen Ableitungen zu kombinieren: vorwärts, im Gleichschritt mit der Rechnung, oder rückwärts, vom Ergebnis zu den Eingängen. Der Rückwärtsmodus liefert die Ableitung einer Zahl nach allen ihren Eingängen in einem einzigen Durchlauf, und dieser Abschnitt zeigt, warum das so wenig kostet.
:::

### Was automatische Differentiation ist

<span class="anker" id="stufe-10-1"></span>

Es gibt drei Wege, die Ableitung einer Rechnung zu bekommen. Man kann die Formel mit den Regeln umformen; das heißt symbolisches Ableiten, und nach Abschnitt [9.1](rechengraphen.html#stufe-9-1) wachsen die Formeln dabei schnell. Man kann die Funktion an zwei nahen Stellen auswerten und einen Differenzenquotienten bilden; das heißt numerisches Ableiten, es ist nur ungefähr richtig, und Abschnitt [11](numerische-ableitung-und-gradientenprufung.html#stufe-11) untersucht seinen Fehler. Der dritte Weg verbindet die Vorteile der beiden anderen.

:::definition Definition 10.1 (Automatische Differentiation)
<span class="anker" id="satz-10-1"></span>

__Automatische Differentiation__ berechnet Ableitungen einer Rechnung, indem sie die Kettenregel auf deren Rechengraphen anwendet: Sie wertet die lokalen Ableitungen mit den Zahlen der Rechnung aus und kombiniert sie nach der Summe über die Wege.
:::

Automatische Differentiation rechnet mit Zahlen, nicht mit Formeln, und deshalb wachsen keine Ausdrücke an. Sie nähert nichts an: Das Ergebnis ist die exakte Ableitung, verfälscht nur durch die Rundung der einzelnen Rechenschritte. Und sie funktioniert für jedes Programm, das aus Grundoperationen besteht, auch mit Schleifen und Verzweigungen, denn für die gegebenen Eingänge liefert das Programm einen Rechengraphen. Die schrittweise Rechnung im Beispiel zu Abschnitt [9.1](rechengraphen.html#stufe-9-1) war schon automatische Differentiation.

⁠**Rechenbeispiel:** Für [(9.1)](rechengraphen.html#gl-9-1) hat der vorige Abschnitt die Ableitungen $5$, $8$ und $3$ aus den lokalen Ableitungen zusammengesetzt, ohne die Formel von $f$ auszumultiplizieren oder abzuleiten. Das war automatische Differentiation, wenn auch noch ohne festes Verfahren für die Reihenfolge der Rechnung. Die beiden folgenden Unterabschnitte geben diese Reihenfolge an.

⁠**Kurz gesagt:** Automatische Differentiation wendet die Kettenregel mit Zahlen auf den Rechengraphen an; sie ist exakt bis auf Rundung und braucht keine Formel.

### Der Vorwärtsmodus

<span class="anker" id="stufe-10-2"></span>

Die erste Möglichkeit folgt der Rechnung selbst. Man legt fest, in welche Richtung man die Eingänge verändert, und führt bei jedem Knoten neben seinem Wert mit, wie schnell er sich bei dieser Veränderung ändert.

:::definition Definition 10.2 (Vorwärtsmodus)
<span class="anker" id="satz-10-2"></span>

Im __Vorwärtsmodus__ wählt man eine Richtung $\dot{\mathbf{x}}\in\mathbb{R}^n$ für die Eingänge und berechnet zu jedem Knoten $b$ neben seinem Wert die Zahl

<span class="anker" id="gl-10-1"></span>
$$\dot b=\sum_{a\text{ Vorgänger von }b}\frac{\partial b}{\partial a}\,\dot a , \tag{10.1}$$

in derselben Reihenfolge wie die Werte. Diese Zahl heißt der __Tangentenwert__ von $b$; die Eingangsknoten erhalten die Komponenten von $\dot{\mathbf{x}}$ als Tangentenwerte.
:::

Der Name erinnert an die Tangente aus Abschnitt [1.2](die-ableitung.html#stufe-1-2), ist aber eine Zahl: Der Tangentenwert $\dot b$ ist die Änderungsrate des Knotens $b$, wenn man die Eingänge entlang der Geraden $\mathbf{x}+t\,\dot{\mathbf{x}}$ verschiebt. Die Formel [(10.1)](#gl-10-1) ist die Kettenregel entlang dieser Kurve, [(6.4)](die-kettenregel-fur-mehrere-variablen.html#gl-6-4), für einen einzigen Knoten. Am Ergebnis steht nach einem Durchlauf $\dot f=\nabla f(\mathbf{x})^{\top}\dot{\mathbf{x}}$. Hat die Rechnung mehrere Ausgänge, so steht dort das Produkt $\mathbf J\,\dot{\mathbf{x}}$ der Jacobi-Matrix mit der Richtung. Mit $\dot{\mathbf{x}}=\mathbf{e}_j$ liefert ein Durchlauf die partielle Ableitung nach $x_j$, bei mehreren Ausgängen die Spalte $j$ der Jacobi-Matrix. Für den ganzen Gradienten einer Funktion von $n$ Variablen braucht der Vorwärtsmodus also $n$ Durchläufe.

⁠**Rechenbeispiel:** Für [(9.1)](rechengraphen.html#gl-9-1) an der Stelle $(1,\,2,\,3)$ mit der Richtung $\dot{\mathbf{x}}=\mathbf{e}_2=(0,\,1,\,0)^{\top}$ ergibt sich Tabelle [5](#tab-5). Am Ergebnis steht $\dot f=8=\partial f/\partial x_2$. Für $\partial f/\partial x_1$ und $\partial f/\partial x_3$ braucht man zwei weitere Durchläufe mit $\mathbf{e}_1$ und $\mathbf{e}_3$.

<span class="anker" id="tab-5"></span>

**Tabelle 5:** Der Vorwärtsmodus für $f=(x_1+x_2)\,(x_2+x_3)$ an der Stelle $(1,\,2,\,3)$ in Richtung $\dot{\mathbf{x}}=\mathbf{e}_2$.

| Knoten | Rechnung | Wert | Tangentenwert |  |
|---|---|---|---|---|
| $x_1$ | Eingang | $1$ | $\dot x_1$ | $0$ |
| $x_2$ | Eingang | $2$ | $\dot x_2$ | $1$ |
| $x_3$ | Eingang | $3$ | $\dot x_3$ | $0$ |
| $v_1$ | $x_1+x_2$ | $3$ | $\dot v_1=\dot x_1+\dot x_2$ | $1$ |
| $v_2$ | $x_2+x_3$ | $5$ | $\dot v_2=\dot x_2+\dot x_3$ | $1$ |
| $f$ | $v_1\cdot v_2$ | $15$ | $\dot f=v_2\,\dot v_1+v_1\,\dot v_2$ | $5+3=8$ |

⁠**Kurz gesagt:** Der Vorwärtsmodus führt zu jedem Wert seinen Tangentenwert mit; ein Durchlauf liefert die Ableitung in einer Richtung, also eine Spalte der Jacobi-Matrix.

:::hintergrund Der Vorwärtsmodus mit dualen Zahlen
Der Vorwärtsmodus lässt sich als Rechnen mit erweiterten Zahlen auffassen. Man rechnet mit Paaren $a+\dot a\,\varepsilon$, wobei $\varepsilon$ ein neues Symbol mit der einzigen Regel $\varepsilon^2=0$ ist; solche Zahlen heißen duale Zahlen. Addition und Multiplikation gehen wie gewohnt: $(a+\dot a\varepsilon)+(b+\dot b\varepsilon)=(a+b)+(\dot a+\dot b)\varepsilon$ und $(a+\dot a\varepsilon)(b+\dot b\varepsilon)=ab+(a\dot b+\dot ab)\varepsilon$, weil das Glied $\dot a\dot b\varepsilon^2$ wegfällt. Der Faktor vor $\varepsilon$ folgt also genau der Summen- und der Produktregel. Für [(9.1)](rechengraphen.html#gl-9-1) setzt man $x_1=1$, $x_2=2+\varepsilon$, $x_3=3$ und erhält $(3+\varepsilon)(5+\varepsilon)=15+8\varepsilon+\varepsilon^2=15+8\varepsilon$: Wert und Ableitung nach $x_2$ in einer Rechnung. Für eine Funktion $\varphi$ einer Variablen setzt man $\varphi(a+\dot a\varepsilon)=\varphi(a)+\varphi'(a)\,\dot a\,\varepsilon$, was der linearen Näherung entspricht, bei der das Quadrat des kleinen Glieds keine Rolle spielt. Duale Zahlen hat William Kingdon Clifford 1873 eingeführt, lange vor jedem Rechner.
:::

### Der Rückwärtsmodus

<span class="anker" id="stufe-10-3"></span>

Der Vorwärtsmodus fragt für einen Eingang, wie stark jeder Knoten von ihm abhängt. Der Rückwärtsmodus stellt die umgekehrte Frage: Wie stark hängt das Ergebnis von jedem Knoten ab? Diese Frage lässt sich vom Ergebnis aus rückwärts beantworten, und am Ende kennt man die Antwort für alle Eingänge zugleich.

:::definition Definition 10.3 (Rückwärtsmodus)
<span class="anker" id="satz-10-3"></span>

Die __Adjungierte__ eines Knotens $a$ ist $\bar a=\partial f/\partial a$, die Ableitung des Ergebnisses nach diesem Knoten, wenn man ihn als Eingang der restlichen Rechnung auffasst. Im __Rückwärtsmodus__ berechnet man zuerst die Vorwärtsrechnung und speichert alle Werte. Dann setzt man $\bar f=1$ und berechnet die Knoten in umgekehrter Reihenfolge,

<span class="anker" id="gl-10-2"></span>
$$\bar a=\sum_{b\text{ Nachfolger von }a}\bar b\,\frac{\partial b}{\partial a}. \tag{10.2}$$

Die Adjungierten der Eingangsknoten bilden den Gradienten $\nabla f(\mathbf{x})$.
:::

Die umgekehrte Reihenfolge ist nötig, weil jeder Knoten die Adjungierten seiner Nachfolger braucht, und die kommen in der Rechnung nach ihm. Jede Adjungierte hat dieselbe Form wie ihr Knoten; ist ein Knoten ein Vektor oder eine Matrix, so ist auch die Adjungierte ein Vektor oder eine Matrix, wie bei der Rückwärtsregel des Matrixprodukts in Abschnitt [7.6](ableiten-nach-vektoren-und-matrizen.html#stufe-7-6).

:::satz Satz 10.4 (Der Rückwärtsmodus liefert den Gradienten)
<span class="anker" id="satz-10-4"></span>

Für jeden Knoten $a$ ist die nach [(10.2)](#gl-10-2) berechnete Zahl $\bar a$ die Summe über alle Wege von $a$ zum Ergebnis, entlang jedes Wegs das Produkt der lokalen Ableitungen. Für die Eingangsknoten ist das nach Abschnitt [9.4](rechengraphen.html#stufe-9-4) die partielle Ableitung von $f$.
:::

:::beweis Der Rückwärtsmodus liefert den Gradienten
Man ordnet alle Wege von $a$ zum Ergebnis nach ihrer ersten Kante. Jeder Weg beginnt mit einer Kante zu einem Nachfolger $b$ und setzt sich dann als Weg von $b$ zum Ergebnis fort. Die Wege, die über $b$ gehen, tragen deshalb zusammen $\frac{\partial b}{\partial a}$ mal die Summe über alle Wege von $b$ zum Ergebnis bei. Ist diese Summe für alle Nachfolger schon richtig berechnet, also gleich $\bar b$, so ist die Summe für $a$ genau [(10.2)](#gl-10-2). Für das Ergebnis selbst stimmt die Aussage mit $\bar f=1$, dem leeren Weg. Weil man rückwärts rechnet, sind die Nachfolger immer vor $a$ an der Reihe, und die Aussage überträgt sich Knoten für Knoten bis zu den Eingängen.
:::

⁠**Rechenbeispiel:** Für [(9.1)](rechengraphen.html#gl-9-1) an der Stelle $(1,\,2,\,3)$ ergibt sich Tabelle [6](#tab-6) und Abb. [19](#abb-19). Ein einziger Rückwärtsdurchlauf liefert alle drei partiellen Ableitungen $(5,\,8,\,3)$, die der Vorwärtsmodus nur mit drei Durchläufen bekam.

<span class="anker" id="tab-6"></span>

**Tabelle 6:** Der Rückwärtsmodus für $f=(x_1+x_2)\,(x_2+x_3)$ an der Stelle $(1,\,2,\,3)$; die Werte stammen aus Tabelle [3](rechengraphen.html#tab-3).

| Knoten | Rechnung nach [(10.2)](#gl-10-2) | Adjungierte |
|---|---|---|
| $f$ | Start | $\bar f=1$ |
| $v_2$ | $\bar f\cdot\partial f/\partial v_2=1\cdot v_1$ | $\bar v_2=3$ |
| $v_1$ | $\bar f\cdot\partial f/\partial v_1=1\cdot v_2$ | $\bar v_1=5$ |
| $x_3$ | $\bar v_2\cdot1$ | $\bar x_3=3$ |
| $x_2$ | $\bar v_1\cdot1+\bar v_2\cdot1$ | $\bar x_2=5+3=8$ |
| $x_1$ | $\bar v_1\cdot1$ | $\bar x_1=5$ |

:::abbildung ml/k3rueckwaerts 19
Vorwärts- und Rückwärtswerte im Rechengraphen von $f=(x_1+x_2)\,(x_2+x_3)$ an der Stelle $(1,\,2,\,3)$: grün die Werte der Vorwärtsrechnung, rot die Adjungierten, grau an den Kanten die lokalen Ableitungen. Beim Rückwärtsrechnen wandert jede Adjungierte entgegen der Pfeilrichtung, wird mit der lokalen Ableitung der Kante multipliziert, und wo zwei Kanten von einem Knoten ausgehen, wie bei $x_2$, werden die Beiträge addiert.
:::

⁠**Kurz gesagt:** Der Rückwärtsmodus rechnet erst vorwärts und speichert alle Werte, dann rückwärts die Adjungierten $\bar a=\sum\bar b\,\partial b/\partial a$; ein Rückwärtsdurchlauf liefert den ganzen Gradienten.

### Muster im Rückwärtsfluss

<span class="anker" id="stufe-10-4"></span>

Nach Tabelle [4](rechengraphen.html#tab-4) verhalten sich die Grundoperationen beim Rückwärtsrechnen auf einfache, wiederkehrende Weise. Wer diese Muster kennt, kann Adjungierte fast ohne Rechnung hinschreiben und Fehler in Herleitungen schnell erkennen.

:::satz Satz 10.5 (Muster der Grundoperationen)
<span class="anker" id="satz-10-5"></span>

<ol class="al">

<li>

Eine *Addition* gibt ihre Adjungierte unverändert an jeden Eingang weiter.

</li>

<li>

Eine *Multiplikation* gibt an jeden Eingang ihre Adjungierte mal dem Wert des *anderen* Eingangs weiter.

</li>

<li>

Ein *Maximum* gibt seine Adjungierte ganz an den größeren Eingang weiter, der kleinere erhält $0$.

</li>

<li>

Eine Funktion einer Variablen multipliziert die Adjungierte mit ihrer lokalen Ableitung, bei der logistischen Funktion also mit $b\,(1-b)$.

</li>

<li>

Wird ein Knoten mehrfach verwendet, so *addieren* sich die Beiträge aller seiner Nachfolger.

</li>

</ol>
:::

Jede Aussage ist [(10.2)](#gl-10-2) mit den lokalen Ableitungen aus Tabelle [4](rechengraphen.html#tab-4). Aus (b) folgt eine nützliche Beobachtung: Ist ein Faktor tausendmal so groß wie der andere, so ist die Adjungierte des kleineren Faktors tausendmal so groß wie die des größeren. Große Unterschiede in den Größenordnungen der Eingänge führen deshalb zu ebenso großen Unterschieden in den partiellen Ableitungen.

⁠**Rechenbeispiel:** In Tabelle [6](#tab-6) hat die Multiplikation vertauscht: $v_1$ erhielt $v_2=5$, $v_2$ erhielt $v_1=3$. Die Additionen haben diese Werte unverändert weitergereicht, und $x_2$ hat als Knoten mit zwei Nachfolgern $5+3=8$ gesammelt. Ein Beispiel mit Maximum: Für $f=\max(x_1,x_2)\cdot x_3$ an der Stelle $(1,\,2,\,3)$ ist $v=\max(1,2)=2$ und $f=6$. Rückwärts ist $\bar v=x_3=3$ und $\bar x_3=v=2$; das Maximum gibt $\bar v$ an den größeren Eingang $x_2$, also $\bar x_2=3$ und $\bar x_1=0$. Tatsächlich ändert eine kleine Änderung von $x_1$ das Ergebnis nicht, solange $x_1<x_2$ bleibt.

⁠**Kurz gesagt:** Addition verteilt, Multiplikation vertauscht, Maximum leitet weiter, und an Verzweigungen wird addiert.

### Der Aufwand

<span class="anker" id="stufe-10-5"></span>

Warum ist der Rückwärtsmodus so wichtig? Weil er den Gradienten einer Funktion mit sehr vielen Eingängen fast so billig liefert wie den Funktionswert selbst. Der Vergleich der Verfahren macht das deutlich.

Der Vorwärtsmodus braucht für den Gradienten einer Funktion von $n$ Variablen $n$ Durchläufe, je einen pro Eingangsrichtung. Ein Durchlauf kostet ein kleines Vielfaches einer Auswertung von $f$, denn zu jeder Grundoperation kommt ihr Tangentenwert hinzu. Differenzenquotienten brauchen sogar $n+1$ oder $2n$ Auswertungen. Der Rückwärtsmodus braucht dagegen immer genau eine Vorwärtsrechnung und einen Rückwärtsdurchlauf, gleich wie groß $n$ ist. Im Rückwärtsdurchlauf wird jede Kante genau einmal benutzt, mit einer Multiplikation und einer Addition. Er kostet also ebenfalls nur ein kleines Vielfaches der Vorwärtsrechnung.

:::satz Satz 10.6 (Aufwand von Vorwärts- und Rückwärtsmodus)
<span class="anker" id="satz-10-6"></span>

Es sei $\mathbf g:\mathbb{R}^n\to\mathbb{R}^m$ durch einen Rechengraphen aus Grundoperationen gegeben, und eine Auswertung koste die Zeit $T$. Dann kostet die ganze Jacobi-Matrix im Vorwärtsmodus etwa $c\cdot n\cdot T$, im Rückwärtsmodus etwa $c\cdot m\cdot T$. Die Zahl $c$ hängt nicht von $n$ und $m$ ab. Zählt man jede Grundrechenart als einen Schritt, so lässt sich zeigen, dass Funktionswert und Gradient zusammen höchstens viermal so viele Schritte brauchen wie der Funktionswert allein; rechnet man auch die Speicherzugriffe mit, bleibt $c$ unter $6$, und in der Praxis liegt es oft bei $2$ bis $3$. Für eine Zahl ($m=1$) kostet der ganze Gradient im Rückwärtsmodus also nur ein festes kleines Vielfaches einer Auswertung.
:::

Den Satz beweist man, indem man für jede Grundoperation abzählt, wie viele Rechenschritte ihr Rückwärtsschritt im Verhältnis zu ihr selbst braucht. Daraus folgt eine Faustregel: Viele Eingänge und ein Ausgang, wie bei einer Zahl, die von Millionen Stellschrauben abhängt, verlangen den Rückwärtsmodus. Wenige Eingänge und viele Ausgänge verlangen den Vorwärtsmodus. Für die vollständige Jacobi-Matrix einer Funktion mit vielen Ein- und Ausgängen gibt es keinen solchen Trick; dort kostet jedes Verfahren viele Durchläufe.

Einen Preis hat der Rückwärtsmodus: Speicher. Der Rückwärtsdurchlauf braucht alle Werte der Vorwärtsrechnung, denn die lokalen Ableitungen werden mit ihnen ausgewertet. Man muss also jeden Zwischenwert aufheben, bis der Rückwärtsdurchlauf an ihm vorbeigekommen ist. Bei langen Rechnungen ist dieser Speicher oft die eigentliche Grenze.

⁠**Rechenbeispiel:** Eine Funktion habe $n=10^6$ Eingänge, und eine Auswertung dauere eine Sekunde. Der Vorwärtsmodus braucht für den Gradienten $10^6$ Durchläufe, also mindestens $10^6$ Sekunden, gut $11$ Tage. Zentrale Differenzenquotienten brauchen $2\cdot10^6$ Auswertungen, gut $23$ Tage, und sind dann nur ungefähr richtig. Der Rückwärtsmodus braucht eine Vorwärtsrechnung und einen Rückwärtsdurchlauf, mit $c\approx3$ also wenige Sekunden.

⁠**Kurz gesagt:** Der Rückwärtsmodus liefert alle $n$ partiellen Ableitungen einer Zahl für ein kleines festes Vielfaches einer Auswertung, unabhängig von $n$; er bezahlt dafür mit dem Speicher für alle Zwischenwerte.

:::hintergrund Warum der Rückwärtsmodus so billig ist, und woher er kommt
Die Summe über alle Wege kann sehr viele Summanden haben. Hängt man zehn Rechenschritte hintereinander, von denen jeder seinen Vorgänger zweimal benutzt, etwa $v_{k+1}=v_k\cdot v_k$, so gibt es zwischen Eingang und Ergebnis $2^{10}=1024$ Wege, bei $50$ Schritten mehr als $10^{15}$. Der Rückwärtsmodus zählt diese Wege nie einzeln. Er fasst alle Wege, die durch denselben Knoten gehen, in dessen Adjungierter zusammen und verwendet diese Zwischensumme für alle Vorgänger weiter. Das ist dieselbe Idee wie bei der schrittweisen Produktregel in Abschnitt [9.1](rechengraphen.html#stufe-9-1): Ein Zwischenergebnis wird einmal berechnet und dann oft benutzt. So kostet jede Kante eine Multiplikation und eine Addition, und der Aufwand wächst mit der Zahl der Kanten, nicht mit der Zahl der Wege. Den Speicherbedarf kann man senken, indem man nur einige Zwischenwerte aufhebt und die übrigen im Rückwärtsdurchlauf neu berechnet; geschickt verteilt wachsen dann Speicher und Rechenzeit nur noch logarithmisch mit der Länge der Rechnung.

Der Vorwärtsmodus wurde 1964 als Rechnerprogramm beschrieben. Den Rückwärtsmodus entwickelte Seppo Linnainmaa 1970 in seiner Abschlussarbeit an der Universität Helsinki, um abzuschätzen, wie sich die Rundungsfehler aller Rechenschritte auf das Ergebnis auswirken; die Empfindlichkeit des Ergebnisses für jeden Zwischenschritt ist genau dessen Adjungierte. Ein Programm, das den Rückwärtsmodus für beliebige Rechnungen automatisch erzeugte, folgte 1980.
:::

### Klammerung: Vektor mal Jacobi-Matrix

<span class="anker" id="stufe-10-6"></span>

Der Unterschied der beiden Modi lässt sich auch mit Matrizen beschreiben. Eine Rechnung, die aus Stufen $\mathbf g_1,\dots,\mathbf g_L$ besteht und mit einer Zahl endet, hat nach [(6.1)](die-kettenregel-fur-mehrere-variablen.html#gl-6-1) die Jacobi-Matrix

$$\mathbf J=\mathbf J_L\,\mathbf J_{L-1}\cdots\mathbf J_1 ,$$

wobei $\mathbf J_L$ eine Zeile ist, weil die letzte Stufe nur einen Ausgang hat. Das Produkt ist dasselbe, wie man es auch klammert; nach [Teil 1](/wissen/informatik/machine-learning/vektoren-und-matrizen/vektoren-und-matrizen.html), Abschnitt 9.3, ist der Aufwand aber sehr verschieden. Der Rückwärtsmodus klammert von links: $\bigl((\mathbf J_L\mathbf J_{L-1})\,\mathbf J_{L-2}\bigr)\cdots$. Jeder Schritt multipliziert eine Zeile mit einer Matrix und ergibt wieder eine Zeile, die transponierte Adjungierte der jeweiligen Stufe. Der Vorwärtsmodus klammert von rechts: $\mathbf J_L\bigl(\cdots(\mathbf J_2\,(\mathbf J_1\dot{\mathbf{x}}))\bigr)$. Für einen einzelnen Vektor $\dot{\mathbf{x}}$ ist auch das billig; für den ganzen Gradienten braucht er aber $n$ solche Vektoren, und das ist so teuer, als würde man die Matrizen $\mathbf J_2\mathbf J_1$, $\mathbf J_3\mathbf J_2\mathbf J_1,\dots$ vollständig ausmultiplizieren.

Ein zweiter Punkt kommt hinzu: Man bildet die Jacobi-Matrizen nie. Jeder Rückwärtsschritt berechnet direkt das Produkt aus Adjungierter und Jacobi-Matrix, mit den Regeln der Grundoperationen. Für ein Matrix-Vektor-Produkt $\mathbf{y}=\mathbf{A}\mathbf{x}$ ist das nach [(7.6)](ableiten-nach-vektoren-und-matrizen.html#gl-7-6) $\bar{\mathbf{x}}=\mathbf{A}^{\top}\bar{\mathbf{y}}$, ohne eine weitere Matrix; für eine elementweise Funktion ist es nach [(5.4)](die-jacobi-matrix.html#gl-5-4) das komponentenweise Produkt mit den Ableitungen, ohne eine Diagonalmatrix aufzustellen. Das ist auch nötig: Hat eine Stufe $10^5$ Eingänge und $10^5$ Ausgänge, so hat ihre Jacobi-Matrix $10^{10}$ Einträge, bei acht Byte je Zahl also $80$ Gigabyte.

⁠**Rechenbeispiel:** Eine Rechnung bestehe aus drei Stufen $\mathbb{R}^{1000}\to\mathbb{R}^{1000}$ und einer letzten Stufe $\mathbb{R}^{1000}\to\mathbb{R}$. Ein Produkt aus Zeile und $1000\times1000$-Matrix kostet nach [Teil 1](/wissen/informatik/machine-learning/vektoren-und-matrizen/vektoren-und-matrizen.html), Abschnitt 9.3, etwa $2\cdot10^6$ Grundrechenarten, ein Produkt zweier solcher Matrizen etwa $2\cdot10^9$. Von links geklammert sind es drei Produkte aus Zeile und Matrix, zusammen etwa $6\cdot10^6$. Von rechts geklammert sind es zwei Matrizenprodukte und ein Produkt aus Zeile und Matrix, zusammen etwa $4\cdot10^9$, rund $670$-mal so viel.

⁠**Kurz gesagt:** Der Rückwärtsmodus multipliziert die Kette der Jacobi-Matrizen von links mit einer Zeile, der Vorwärtsmodus von rechts mit einer Spalte; die Jacobi-Matrizen selbst werden nie gebildet.

:::aufgabe Aufgabe 35 ★ Rückwärts durch ein Quadrat
<span class="anker" id="aufg-35"></span>

Es sei $f=(x_1x_2+x_3)^2$ wie in Aufgabe [32](rechengraphen.html#aufg-32).

<ol class="al">

<li>

Berechne an der Stelle $(1,\,2,\,3)$ alle Adjungierten im Rückwärtsmodus und stelle sie in einer Tabelle wie Tabelle [6](#tab-6) dar.

</li>

<li>

Wie viele Durchläufe bräuchte der Vorwärtsmodus für denselben Gradienten? Führe den Durchlauf für $\dot{\mathbf{x}}=\mathbf{e}_1$ aus.

</li>

</ol>

:::loesung
(a) Mit den Werten aus Aufgabe [32](rechengraphen.html#aufg-32):

| Knoten | Rechnung | Adjungierte |
|---|---|---|
| $f$ | Start | $\bar f=1$ |
| $v_2$ | $\bar f\cdot2v_2$ | $\bar v_2=10$ |
| $v_1$ | $\bar v_2\cdot1$ | $\bar v_1=10$ |
| $x_3$ | $\bar v_2\cdot1$ | $\bar x_3=10$ |
| $x_2$ | $\bar v_1\cdot x_1$ | $\bar x_2=10$ |
| $x_1$ | $\bar v_1\cdot x_2$ | $\bar x_1=20$ |

(b) Drei Durchläufe, einen je Eingang. Mit $\dot{\mathbf{x}}=\mathbf{e}_1$: $\dot v_1=x_2\dot x_1+x_1\dot x_2=2$, $\dot v_2=\dot v_1+\dot x_3=2$, $\dot f=2v_2\,\dot v_2=10\cdot2=20=\partial f/\partial x_1$.
:::
:::

:::aufgabe Aufgabe 36 ★★ Die logistische Funktion im Graphen
<span class="anker" id="aufg-36"></span>

Es sei $f(x_1,x_2)=\sigma(2x_1-x_2)$ mit der logistischen Funktion $\sigma$.

<ol class="al">

<li>

Zeichne den Graphen mit $v_1=2x_1$, $v_2=v_1-x_2$, $f=\sigma(v_2)$ und rechne an der Stelle $(1,\,1)$ vorwärts.

</li>

<li>

Berechne alle Adjungierten. Welche gespeicherte Zahl braucht der Knoten $\sigma$ für seine lokale Ableitung?

</li>

<li>

Rechne nach: $\nabla f(\mathbf{x})=\sigma'(2x_1-x_2)\,(2,\,-1)^{\top}$.

</li>

</ol>

:::loesung
(a) Der Graph hat die Kanten $x_1\to v_1$, $v_1\to v_2$, $x_2\to v_2$ und $v_2\to f$. Vorwärts an der Stelle $(1,\,1)$: $v_1=2$, $v_2=1$, $f=\sigma(1)\approx0{,}7311$.

(b) $\bar f=1$; $\bar v_2=\bar f\cdot f\,(1-f)\approx0{,}7311\cdot0{,}2689\approx0{,}1966$; $\bar v_1=\bar v_2\cdot1\approx0{,}1966$; $\bar x_2=\bar v_2\cdot(-1)\approx-0{,}1966$; $\bar x_1=\bar v_1\cdot2\approx0{,}3932$. Der Knoten $\sigma$ braucht für seine lokale Ableitung nur seinen eigenen gespeicherten Ausgang $f$, nach Tabelle [4](rechengraphen.html#tab-4).

(c) Nach der Kettenregel ist $\nabla f=\sigma'(2x_1-x_2)\,\nabla(2x_1-x_2)=\sigma'(2x_1-x_2)\,(2,\,-1)^{\top}$, an der Stelle $(1,\,1)$ also $0{,}1966\cdot(2,\,-1)^{\top}=(0{,}3932;\ -0{,}1966)^{\top}$.
:::
:::

:::aufgabe Aufgabe 37 ★★ Duale Zahlen
<span class="anker" id="aufg-37"></span>

<ol class="al">

<li>

Berechne $p(x)=(x+1)(x+2)(x+3)(x+4)$ mit der dualen Zahl $x=0+1\varepsilon$ und lies $p(0)$ und $p'(0)$ ab.

</li>

<li>

Berechne ebenso $(x^2+1)^3$ an der Stelle $x=1+\varepsilon$ und vergleiche mit der Kettenregel.

</li>

</ol>

:::loesung
(a) Mit $x=\varepsilon$:

$$(1+\varepsilon)(2+\varepsilon)=2+3\varepsilon,\quad (2+3\varepsilon)(3+\varepsilon)=6+11\varepsilon,\quad (6+11\varepsilon)(4+\varepsilon)=24+50\varepsilon .$$

Also $p(0)=24$ und $p'(0)=50$; die Faktoren vor $\varepsilon$ sind genau die $p_k'$ aus dem Rechenbeispiel zu Abschnitt [9.1](rechengraphen.html#stufe-9-1).

(b) $(1+\varepsilon)^2=1+2\varepsilon$, plus $1$ ergibt $2+2\varepsilon$; $(2+2\varepsilon)^2=4+8\varepsilon$ und $(4+8\varepsilon)(2+2\varepsilon)=8+24\varepsilon$. Die Kettenregel gibt $3\,(x^2+1)^2\cdot2x=3\cdot4\cdot2=24$ an der Stelle $1$.
:::
:::

:::aufgabe Aufgabe 38 ★★★ Welcher Modus?
<span class="anker" id="aufg-38"></span>

<ol class="al">

<li>

Eine Rechnung hat $3$ Eingänge und $1000$ Ausgänge, eine andere $1000$ Eingänge und $3$ Ausgänge. Wie viele Durchläufe brauchen Vorwärts- und Rückwärtsmodus jeweils für die ganze Jacobi-Matrix?

</li>

<li>

Es sei $f(\mathbf{x})=\mathbf{c}^{\top}\mathbf{B}\mathbf{x}$ mit einer vollbesetzten Matrix $\mathbf{B}\in\mathbb{R}^{n\times n}$, gerechnet in zwei Stufen $\mathbf{y}=\mathbf{B}\mathbf{x}$ und $f=\mathbf{c}^{\top}\mathbf{y}$. Ein Vorwärtsdurchlauf berechnet $\mathbf{c}^{\top}(\mathbf{B}\dot{\mathbf{x}})$, ein Rückwärtsdurchlauf $\bar{\mathbf{x}}=\mathbf{B}^{\top}\mathbf{c}$. Zähle für beide Wege die Grundrechenarten, die der ganze Gradient kostet, wenn ein Matrix-Vektor-Produkt etwa $2n^2$ und ein Skalarprodukt etwa $2n$ kostet.

</li>

<li>

Warum braucht der Rückwärtsmodus mehr Speicher als der Vorwärtsmodus? Welche Werte darf der Vorwärtsmodus sofort vergessen?

</li>

</ol>

:::loesung
(a) Mit $3$ Eingängen und $1000$ Ausgängen braucht der Vorwärtsmodus $3$ Durchläufe, der Rückwärtsmodus $1000$; man nimmt den Vorwärtsmodus. Mit $1000$ Eingängen und $3$ Ausgängen ist es umgekehrt: $1000$ Vorwärtsdurchläufe gegen $3$ Rückwärtsdurchläufe.

(b) Vorwärts braucht der Gradient $n$ Durchläufe mit $\dot{\mathbf{x}}=\mathbf{e}_1,\dots,\mathbf{e}_n$, jeder mit einem Matrix-Vektor-Produkt $\mathbf{B}\dot{\mathbf{x}}$ und einem Skalarprodukt, zusammen etwa $n\,(2n^2+2n)\approx2n^3$ Grundrechenarten. Rückwärts ist $\bar{\mathbf{y}}=\mathbf{c}$, und $\bar{\mathbf{x}}=\mathbf{B}^{\top}\mathbf{c}$ kostet ein Matrix-Vektor-Produkt, etwa $2n^2$; dazu kommt die Vorwärtsrechnung mit etwa $2n^2+2n$. Der Rückwärtsmodus ist also etwa $n/2$-mal so schnell.

(c) Der Rückwärtsdurchlauf braucht die Werte der Vorwärtsrechnung, um die lokalen Ableitungen auszuwerten, und er kommt erst nach dem Ende der Vorwärtsrechnung. Alle Zwischenwerte müssen deshalb bis dahin aufgehoben werden. Im Vorwärtsmodus laufen Wert und Tangentenwert gemeinsam vorwärts; beide werden nicht mehr gebraucht, sobald alle seine Nachfolger berechnet sind, und dürfen dann vergessen werden.
:::
:::

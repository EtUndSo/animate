---
title: Wahrscheinlichkeit
pfad: Informatik / Machine Learning / Mathematische Grundlagen / Wahrscheinlichkeit
knoten: Grundlagen 4: Wahrscheinlichkeit
nachschlagen: ja
order: 15240300
summary: Eine Wahrscheinlichkeit ordnet jedem Ereignis eine Zahl zwischen null und eins zu, die angibt, wie sehr man mit ihm rechnen kann.
tags: absolute Häufigkeit, relative Häufigkeit, Wahrscheinlichkeit, Axiome, Wahrscheinlichkeitsraum, Additionssatz, Laplace-Experiment
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Eine Wahrscheinlichkeit ordnet jedem Ereignis eine Zahl zwischen null und eins zu, die angibt, wie sehr man mit ihm rechnen kann. Dieser Abschnitt gewinnt die Regeln dafür aus der relativen Häufigkeit, schreibt sie als drei Axiome auf und leitet daraus die Rechenregeln ab, mit denen der Rest des Kapitels arbeitet. Am Ende steht der einfache Fall gleich wahrscheinlicher Ergebnisse, in dem Wahrscheinlichkeiten Abzählaufgaben werden.
:::

### Die relative Häufigkeit

<span class="anker" id="stufe-2-1"></span>

Wie wahrscheinlich ein Ereignis ist, zeigt sich, wenn man das Experiment oft wiederholt: Ein wahrscheinliches Ereignis tritt in vielen Wiederholungen ein, ein unwahrscheinliches in wenigen. Das macht man zu einer Zahl.

:::definition Definition 2.1 (Relative Häufigkeit)
<span class="anker" id="satz-2-1"></span>

Ein Zufallsexperiment werde $n$-mal unter gleichen Bedingungen wiederholt, und das Ereignis $A$ trete dabei $n_A$-mal ein. Die Zahl $n_A$ heißt die __absolute Häufigkeit__ von $A$. Der Anteil

<span class="anker" id="gl-2-1"></span>
$$h_n(A)=\frac{n_A}{n} \tag{2.1}$$

heißt die __relative Häufigkeit__ von $A$ in diesen $n$ Wiederholungen.
:::

Drei Eigenschaften folgen sofort aus dem Zählen. Erstens ist $0\le h_n(A)\le1$. Zweitens ist $h_n(\Omega)=1$, denn $\Omega$ tritt in jeder Wiederholung ein. Drittens addieren sich die relativen Häufigkeiten unvereinbarer Ereignisse: Sind $A$ und $B$ disjunkt, so wird jede Wiederholung, in der $A\cup B$ eintritt, genau einmal mitgezählt, entweder bei $A$ oder bei $B$. Also ist $n_{A\cup B}=n_A+n_B$ und

<span class="anker" id="gl-2-2"></span>
$$h_n(A\cup B)=h_n(A)+h_n(B)\qquad\text{für disjunkte }A,B . \tag{2.2}$$

Die relative Häufigkeit selbst schwankt: Eine andere Folge von $n$ Würfen liefert meist eine andere Zahl. Mit wachsendem $n$ schwankt sie aber immer weniger. Warum das so ist und wie schnell es geht, zeigt Abschnitt [13](mittelwerte-vieler-zufallsvariablen.html#stufe-13).

⁠**Rechenbeispiel:** In $20$ Würfen fiel $9$-mal eine gerade Augenzahl, $3$-mal die Fünf und $8$-mal die Eins oder die Drei. Also ist $h_{20}(\{2,4,6\})=9/20=0{,}45$ und $h_{20}(\{5\})=3/20=0{,}15$. Die beiden Ereignisse sind disjunkt, und „gerade oder Fünf“ trat $9+3=12$-mal ein: $h_{20}(\{2,4,5,6\})=0{,}6=0{,}45+0{,}15$.

⁠**Kurz gesagt:** Die relative Häufigkeit ist der Anteil der Wiederholungen, in denen ein Ereignis eintritt; sie liegt zwischen $0$ und $1$, ist für $\Omega$ gleich $1$ und addiert sich bei unvereinbaren Ereignissen.

### Die Axiome der Wahrscheinlichkeit

<span class="anker" id="stufe-2-2"></span>

Eine Wahrscheinlichkeit soll das sein, worauf sich die relative Häufigkeit bei vielen Wiederholungen einpendelt. Man kann sie aber nicht einfach als Grenzwert der relativen Häufigkeiten definieren: Eine Folge von Würfen ist zufällig, und nichts garantiert, dass ihre relativen Häufigkeiten einen Grenzwert haben und dass es der richtige ist. Auch die Folge, in der immer die Sechs fällt, ist möglich; in ihr ist die relative Häufigkeit der Sechs immer $1$. Stattdessen verlangt man von ihr genau die drei Eigenschaften, die jede relative Häufigkeit hat, und baut alles Weitere darauf auf.

:::definition Definition 2.2 (Wahrscheinlichkeit)
<span class="anker" id="satz-2-2"></span>

Eine __Wahrscheinlichkeit__ $P$ ordnet jedem Ereignis $A$ eine Zahl $P(A)$ zu, sodass gilt:

<ol class="rm">

<li>

$P(A)\ge0$ für jedes Ereignis $A$;

</li>

<li>

$P(\Omega)=1$;

</li>

<li>

für Ereignisse $A_1,A_2,\dots$, von denen je zwei disjunkt sind,

<span class="anker" id="gl-2-3"></span>
$$P\Bigl(\bigcup_iA_i\Bigr)=\sum_iP(A_i). \tag{2.3}$$

</li>

</ol>

Diese drei Forderungen heißen die __Axiome__ der Wahrscheinlichkeit. $\Omega$ mit den Ereignissen und $P$ heißt __Wahrscheinlichkeitsraum__.
:::

Das dritte Axiom gilt für endlich viele und für abzählbar unendlich viele Ereignisse. Bei zwei Ereignissen ist es die Regel [(2.2)](#gl-2-2). Ein Axiom wird nicht bewiesen; es ist eine Festlegung, an der man messen kann, ob eine Zuordnung von Zahlen zu Ereignissen eine Wahrscheinlichkeit ist. Welche Zahlen man im Einzelfall wählt, sagen die Axiome nicht. Das entscheidet man mit Wissen über das Experiment, etwa über die Symmetrie eines Würfels, oder mit Daten.

⁠**Rechenbeispiel:** Für einen fairen Würfel setzt man $P(\{k\})=1/6$ für $k=1,\dots,6$ und für ein Ereignis $A$ die Summe über seine Elemente. Dann ist $P(A)\ge0$, $P(\Omega)=6\cdot\tfrac16=1$, und die Additivität gilt, weil disjunkte Ereignisse keine gemeinsamen Summanden haben. Ein gezinkter Würfel mit $P(\{6\})=0{,}25$ und $P(\{k\})=0{,}15$ für $k=1,\dots,5$ erfüllt die Axiome ebenfalls, denn $5\cdot0{,}15+0{,}25=1$. Dort ist $P(\{2,4,6\})=0{,}15+0{,}15+0{,}25=0{,}55$.

⁠**Kurz gesagt:** Eine Wahrscheinlichkeit ist nichtnegativ, gibt dem sicheren Ereignis den Wert $1$ und addiert sich über unvereinbare Ereignisse.

:::hintergrund Warum gerade diese drei Axiome, und was eine Wahrscheinlichkeit „ist“
Die Axiome sind genau die Eigenschaften, die jede relative Häufigkeit hat. Deshalb kann eine Wahrscheinlichkeit, die diese Axiome erfüllt, das Verhalten relativer Häufigkeiten beschreiben, ohne ihnen zu widersprechen. Die Additivität stammt vom Zählen: Wer unvereinbare Fälle zusammenfasst, zählt jeden Versuch höchstens einmal. Aufgeschrieben hat die Axiome Andrei Kolmogorow 1933. Erst damit wurde die Wahrscheinlichkeitsrechnung ein Teil der Mathematik mit klaren Grundlagen.

Was eine Wahrscheinlichkeit bedeutet, legen die Axiome nicht fest. Zwei Deutungen sind verbreitet. Die eine sieht in $P(A)$ den Anteil, mit dem $A$ auf lange Sicht eintritt; sie passt zu Würfeln, Bauteilen aus einer Fertigung und Rauschen. Die andere sieht in $P(A)$ den Grad, mit dem man nach dem eigenen Wissen von $A$ überzeugt sein sollte; sie passt auch zu einmaligen Fragen wie „Ist dieses Bauteil defekt?“. Für endlich viele Ereignisse führen beide Deutungen auf dieselben Rechenregeln. Für die zweite Deutung zeigte Richard Cox 1946: Wer Überzeugungen mit einer Zahl misst und einige natürliche Forderungen an widerspruchsfreies Schließen stellt, landet zwangsläufig bei den Regeln der Wahrscheinlichkeit. Wie natürlich diese Forderungen sind, ist bis heute umstritten. Für die Rechnungen in diesem Kapitel spielt die Deutung keine Rolle.
:::

### Rechenregeln

<span class="anker" id="stufe-2-3"></span>

Aus den drei Axiomen folgen die Regeln, mit denen man tatsächlich rechnet. Sie entsprechen der Anschauung, dass Wahrscheinlichkeit sich wie ein Flächeninhalt verhält: Man stelle sich $\Omega$ als Fläche vom Inhalt $1$ vor und jedes Ereignis als Teilfläche.

:::satz Satz 2.3 (Rechenregeln für Wahrscheinlichkeiten)
<span class="anker" id="satz-2-3"></span>

Für Ereignisse $A$ und $B$ gilt:

<ol class="al">

<li>

$P(A^{\mathrm c})=1-P(A)$, insbesondere $P(\emptyset)=0$;

</li>

<li>

aus $A\subseteq B$ folgt $P(A)\le P(B)$, insbesondere $P(A)\le1$;

</li>

<li>

$P(A\cup B)=P(A)+P(B)-P(A\cap B)$.

</li>

</ol>
:::

:::beweis Rechenregeln
(a) $A$ und $A^{\mathrm c}$ sind disjunkt, und ihre Vereinigung ist $\Omega$. Nach den Axiomen (ii) und (iii) ist $1=P(A)+P(A^{\mathrm c})$. Mit $A=\Omega$ folgt $P(\emptyset)=0$.

(b) Ist $A\subseteq B$, so ist $B$ die disjunkte Vereinigung von $A$ und $B\cap A^{\mathrm c}$. Also ist $P(B)=P(A)+P(B\cap A^{\mathrm c})\ge P(A)$ nach Axiom (i).

(c) $A\cup B$ ist die disjunkte Vereinigung von $A$ und $B\cap A^{\mathrm c}$, und $B$ ist die disjunkte Vereinigung von $A\cap B$ und $B\cap A^{\mathrm c}$. Also ist $P(A\cup B)=P(A)+P(B\cap A^{\mathrm c})$ und $P(B)=P(A\cap B)+P(B\cap A^{\mathrm c})$. Zieht man die zweite Gleichung von der ersten ab, fällt $P(B\cap A^{\mathrm c})$ heraus.
:::

Regel (c) heißt __Additionssatz__. Das abgezogene Glied verhindert, dass die gemeinsame Teilfläche doppelt gezählt wird. Sind $A$ und $B$ unvereinbar, so ist es null, und es bleibt Axiom (iii). Regel (a) ist oft der kürzeste Weg: Statt „mindestens einmal“ rechnet man „keinmal“ und zieht von $1$ ab.

⁠**Rechenbeispiel:** Für den fairen Würfel mit $A=\{2,4,6\}$ und $B=\{5,6\}$ ist $P(A\cup B)=\tfrac36+\tfrac26-\tfrac16=\tfrac46=\tfrac23$. Zählt man nach, so hat $A\cup B=\{2,4,5,6\}$ tatsächlich vier Elemente. Beim gezinkten Würfel aus Unterabschnitt [2.2](#stufe-2-2) ist $P(\text{keine Sechs})=1-0{,}25=0{,}75$.

⁠**Kurz gesagt:** Wahrscheinlichkeiten verhalten sich wie Teilflächen einer Fläche vom Inhalt $1$; das Gegenereignis hat $1-P(A)$, und bei überlappenden Ereignissen zieht man den Schnitt einmal ab.

### Gleich wahrscheinliche Ergebnisse

<span class="anker" id="stufe-2-4"></span>

Bei einer Münze, einem Würfel oder einem gut gemischten Kartenspiel gibt es keinen Grund, ein Ergebnis einem anderen vorzuziehen. Man gibt dann allen Ergebnissen dieselbe Wahrscheinlichkeit. Weil sie sich zu $1$ addieren müssen, ist sie bei $\#\Omega$ Ergebnissen $1/\#\Omega$.

:::satz Satz 2.4 (Gleich wahrscheinliche Ergebnisse)
<span class="anker" id="satz-2-4"></span>

Ist $\Omega$ endlich und haben alle Ergebnisse dieselbe Wahrscheinlichkeit, so ist für jedes Ereignis

<span class="anker" id="gl-2-4"></span>
$$P(A)=\frac{\#A}{\#\Omega}=\frac{\text{Anzahl der Ergebnisse in }A}{\text{Anzahl aller Ergebnisse}} . \tag{2.4}$$
:::

Das folgt aus Axiom (iii), denn $A$ ist die disjunkte Vereinigung seiner $\#A$ Elementarereignisse. Ein solches Experiment heißt __Laplace-Experiment__. In ihm sind Wahrscheinlichkeiten Abzählaufgaben.

:::warnung Nicht jeder Ergebnisraum hat gleich wahrscheinliche Ergebnisse
Beim Wurf zweier Würfel ist die Augensumme eine der Zahlen $2,\dots,12$. Diese elf Ausgänge sind aber nicht gleich wahrscheinlich: Die Summe $2$ entsteht nur aus $(1,1)$, die Summe $7$ aus sechs Paaren. Gleich wahrscheinlich sind die $36$ Paare des Ergebnisraums aus Unterabschnitt [1.2](zufall-und-ereignisse.html#stufe-1-2). Formel [(2.4)](#gl-2-4) gilt nur für einen Ergebnisraum, dessen Ergebnisse wirklich gleich wahrscheinlich sind.
:::

⁠**Rechenbeispiel:** Beim Wurf zweier fairer Würfel hat „Augensumme $7$“ die sechs Ergebnisse $(1,6)$, $(2,5)$, $(3,4)$, $(4,3)$, $(5,2)$, $(6,1)$. Also ist $P(\text{Summe }7)=6/36=1/6$. „Augensumme $2$“ hat nur das Ergebnis $(1,1)$ und die Wahrscheinlichkeit $1/36$.

⁠**Kurz gesagt:** Sind alle Ergebnisse gleich wahrscheinlich, so ist die Wahrscheinlichkeit eines Ereignisses der Anteil seiner Ergebnisse an allen Ergebnissen.

:::aufgabe Aufgabe 3 ★ Abzählen beim Doppelwurf
<span class="anker" id="aufg-3"></span>

Zwei faire Würfel werden geworfen.

<ol class="al">

<li>

Berechne $P(\text{Augensumme}\ge10)$.

</li>

<li>

Berechne $P(\text{mindestens eine Sechs})$ einmal durch Abzählen und einmal über das Gegenereignis.

</li>

<li>

Berechne $P(\text{Augensumme}\ge10\text{ oder mindestens eine Sechs})$ mit dem Additionssatz.

</li>

</ol>

:::loesung
(a) Summe $10$: $(4,6),(5,5),(6,4)$; Summe $11$: $(5,6),(6,5)$; Summe $12$: $(6,6)$. Zusammen $6$ von $36$, also $P=\tfrac16$.

(b) Abzählen: $6$ Paare mit Sechs beim roten Würfel, $6$ beim blauen, eines davon, $(6,6)$, in beiden: $11$ Paare, $P=\tfrac{11}{36}$. Über das Gegenereignis: Keine Sechs heißt, beide Würfel zeigen eine der Zahlen $1$ bis $5$, das sind $5\cdot5=25$ Paare. Also $P=1-\tfrac{25}{36}=\tfrac{11}{36}$.

(c) Im Schnitt liegen die Paare mit Summe mindestens $10$ und einer Sechs: $(4,6)$, $(6,4)$, $(5,6)$, $(6,5)$ und $(6,6)$, also $5$ Paare. Der Additionssatz ergibt $\tfrac6{36}+\tfrac{11}{36}-\tfrac5{36}=\tfrac{12}{36}=\tfrac13$.
:::
:::

:::aufgabe Aufgabe 4 ★★ Schranken aus den Axiomen
<span class="anker" id="aufg-4"></span>

<ol class="al">

<li>

Zeige, dass $P(A\cup B)\le P(A)+P(B)$ für beliebige Ereignisse gilt.

</li>

<li>

Zeige $P(A\cap B)\ge P(A)+P(B)-1$. Was folgt daraus für zwei Ereignisse mit $P(A)=P(B)=0{,}9$?

</li>

<li>

Ein Gerät besteht aus $20$ Baugruppen, jede fällt mit der Wahrscheinlichkeit $0{,}001$ aus. Schätze mit (a), wie wahrscheinlich mindestens ein Ausfall höchstens ist, ohne etwas über das Zusammenspiel der Baugruppen zu wissen.

</li>

</ol>

:::loesung
(a) Nach dem Additionssatz ist $P(A\cup B)=P(A)+P(B)-P(A\cap B)$, und $P(A\cap B)\ge0$ nach Axiom (i).

(b) Nach Regel (b) ist $P(A\cup B)\le1$, also $P(A\cap B)=P(A)+P(B)-P(A\cup B)\ge P(A)+P(B)-1$. Für $P(A)=P(B)=0{,}9$ ist $P(A\cap B)\ge0{,}8$: Zwei sehr wahrscheinliche Ereignisse treten auch gemeinsam mit großer Wahrscheinlichkeit ein, ganz gleich, wie sie zusammenhängen.

(c) Wendet man (a) wiederholt an, so ist die Wahrscheinlichkeit einer Vereinigung höchstens die Summe der einzelnen Wahrscheinlichkeiten: $P(\text{mindestens ein Ausfall})\le20\cdot0{,}001=0{,}02$. Die Schranke gilt ohne jede Annahme über Abhängigkeiten. Fallen die Baugruppen unabhängig aus, ist der genaue Wert $1-0{,}999^{20}\approx0{,}0198$, fast dieselbe Zahl, weil das Abgezogene bei kleinen Wahrscheinlichkeiten sehr klein ist.
:::
:::

:::aufgabe Aufgabe 5 ★ Eine Münze, dreißig Würfe (praktisch)
<span class="anker" id="aufg-5"></span>

Wirf eine Münze $30$-mal und notiere jedes Ergebnis.

<ol class="al">

<li>

Berechne die relative Häufigkeit von „Kopf“ nach $10$, nach $20$ und nach $30$ Würfen.

</li>

<li>

Berechne dieselbe Häufigkeit getrennt für die Würfe $1$ bis $10$, $11$ bis $20$ und $21$ bis $30$. Schwanken diese drei Zahlen stärker oder schwächer als die drei Zahlen aus (a)? Warum?

</li>

</ol>

:::loesung
(a) Die Zahlen hängen von deinen Würfen ab. Typisch liegen die drei relativen Häufigkeiten in der Nähe von $0{,}5$, die nach $10$ Würfen oft deutlich daneben, etwa bei $0{,}3$ oder $0{,}7$.

(b) Die drei Häufigkeiten aus je $10$ Würfen schwanken stärker als die laufenden Häufigkeiten aus (a). Jede beruht auf nur $10$ Würfen. Die laufenden Häufigkeiten nach $20$ und $30$ Würfen beruhen auf mehr Würfen und enthalten die früheren schon, sodass einzelne Ausreißer weniger Gewicht haben. Abschnitt [13](mittelwerte-vieler-zufallsvariablen.html#stufe-13) macht daraus eine Formel: Die Standardabweichung einer relativen Häufigkeit aus $n$ Würfen ist $\sqrt{0{,}25/n}$, für $n=10$ etwa $0{,}16$, für $n=30$ etwa $0{,}09$.
:::
:::

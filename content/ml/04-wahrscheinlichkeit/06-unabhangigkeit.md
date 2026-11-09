---
title: Unabhängigkeit
pfad: Informatik / Machine Learning / Mathematische Grundlagen / Wahrscheinlichkeit
knoten: Grundlagen 4: Wahrscheinlichkeit
nachschlagen: ja
order: 15240600
summary: Manchmal ändert eine Information gar nichts: Ob der rote Würfel eine Sechs zeigt, sagt nichts über den blauen.
tags: unabhängig, abhängig, gegenseitig unabhängig, paarweise unabhängig, bedingt unabhängig
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Manchmal ändert eine Information gar nichts: Ob der rote Würfel eine Sechs zeigt, sagt nichts über den blauen. Dieser Abschnitt macht diese Unabhängigkeit zu einer Formel, grenzt sie von der Unvereinbarkeit ab, mit der sie oft verwechselt wird, und erweitert sie auf mehrere Ereignisse und auf Ereignisse, die erst unter einer Bedingung unabhängig werden. Unabhängigkeit ist die wichtigste Vereinfachung der Wahrscheinlichkeitsrechnung: Sie macht aus gemeinsamen Wahrscheinlichkeiten Produkte.
:::

### Unabhängige Ereignisse

<span class="anker" id="stufe-5-1"></span>

Ein Ereignis $B$ sagt nichts über $A$, wenn die Information „$B$ ist eingetreten“ die Wahrscheinlichkeit von $A$ nicht ändert: $P(A\mid B)=P(A)$. Mit der Produktregel wird daraus $P(A\cap B)=P(A)\,P(B)$. Diese Form ist symmetrisch in $A$ und $B$ und braucht keine Voraussetzung $P(B)>0$. Man nimmt sie deshalb als Definition.

:::definition Definition 5.1 (Unabhängige Ereignisse)
<span class="anker" id="satz-5-1"></span>

Zwei Ereignisse $A$ und $B$ heißen __unabhängig__, wenn

<span class="anker" id="gl-5-1"></span>
$$P(A\cap B)=P(A)\,P(B). \tag{5.1}$$

Andernfalls heißen sie __abhängig__.
:::

Ist $P(B)>0$, so ist [(5.1)](#gl-5-1) gleichbedeutend mit $P(A\mid B)=P(A)$, und ist $P(A)>0$, mit $P(B\mid A)=P(B)$. Unabhängigkeit ist eine Eigenschaft der Zahlen $P$, nicht der Physik. Oft folgt sie aus dem Aufbau des Experiments, etwa bei zwei getrennten Würfeln. Man kann sie aber auch nachrechnen, und dann zeigen sich manchmal Ereignisse als unabhängig, bei denen man es nicht erwartet.

::::beispiel [Rechenbeispiel]
Beim fairen Würfel sei $A=\{2,4,6\}$ und $B=\{1,2\}$. Es ist $P(A\cap B)=P(\{2\})=\tfrac16$ und $P(A)\,P(B)=\tfrac12\cdot\tfrac13=\tfrac16$: $A$ und $B$ sind unabhängig, obwohl sie dasselbe Ergebnis $2$ enthalten. Mit $C=\{1,2,3\}$ ist $P(A\cap C)=\tfrac16$, aber $P(A)\,P(C)=\tfrac14$: abhängig. In Tabelle [1](bedingte-wahrscheinlichkeit.html#tab-1) sind „Sonne“ und „Fahrrad“ abhängig, denn $P(\text{Sonne}\cap\text{Fahrrad})=0{,}3$, aber $0{,}4\cdot0{,}4=0{,}16$.
::::

⁠**Kurz gesagt:** Unabhängig heißt: Die gemeinsame Wahrscheinlichkeit ist das Produkt der einzelnen; die Information über das eine ändert nichts an der Wahrscheinlichkeit des anderen.

### Unabhängig ist nicht unvereinbar

<span class="anker" id="stufe-5-2"></span>

Die Wörter klingen ähnlich, bedeuten aber fast das Gegenteil. Unvereinbare Ereignisse schließen einander aus. Weiß man, dass das eine eingetreten ist, weiß man sicher, dass das andere nicht eingetreten ist. Das ist die stärkste denkbare Abhängigkeit.

:::satz Satz 5.2 (Unvereinbare Ereignisse sind abhängig)
<span class="anker" id="satz-5-2"></span>

Sind $A$ und $B$ unvereinbar und haben beide positive Wahrscheinlichkeit, so sind sie abhängig.
:::

Denn $P(A\cap B)=P(\emptyset)=0$, aber $P(A)\,P(B)>0$. Umgekehrt vererbt sich Unabhängigkeit auf die Gegenereignisse: Sind $A$ und $B$ unabhängig, so auch $A$ und $B^{\mathrm c}$, denn nach der Summenregel ist $P(A\cap B^{\mathrm c})=P(A)-P(A)P(B)=P(A)\,P(B^{\mathrm c})$. Ebenso sind dann $A^{\mathrm c}$ und $B^{\mathrm c}$ unabhängig.

::::beispiel [Rechenbeispiel]
Beim Würfel sind $\{1\}$ und $\{2\}$ unvereinbar. Weiß man, dass die Eins gefallen ist, so ist $P(\{2\}\mid\{1\})=0$ statt $\tfrac16$. Für die unabhängigen Ereignisse $A=\{2,4,6\}$ und $B=\{1,2\}$ aus Unterabschnitt [5.1](#stufe-5-1) ist $P(A\cap B^{\mathrm c})=P(\{4,6\})=\tfrac13=\tfrac12\cdot\tfrac23=P(A)\,P(B^{\mathrm c})$.
::::

⁠**Kurz gesagt:** Unvereinbare Ereignisse mit positiver Wahrscheinlichkeit sind nie unabhängig; unabhängige Ereignisse bleiben unabhängig, wenn man eines durch sein Gegenereignis ersetzt.

### Mehrere unabhängige Ereignisse

<span class="anker" id="stufe-5-3"></span>

Bei mehr als zwei Ereignissen reicht es nicht, jedes Paar zu prüfen. Unabhängigkeit soll heißen, dass keine Auswahl der Ereignisse etwas über die übrigen verrät. Das verlangt die Produktformel für jede Auswahl.

:::definition Definition 5.3 (Gegenseitige Unabhängigkeit)
<span class="anker" id="satz-5-3"></span>

Ereignisse $A_1,\dots,A_m$ heißen __unabhängig__, genauer __gegenseitig unabhängig__, wenn für jede Auswahl von mindestens zwei verschiedenen Indizes $i_1<\dots<i_r$

<span class="anker" id="gl-5-2"></span>
$$P(A_{i_1}\cap\dots\cap A_{i_r})=P(A_{i_1})\cdots P(A_{i_r}). \tag{5.2}$$

Gilt die Formel nur für je zwei Ereignisse, heißen sie __paarweise unabhängig__.
:::

Für unabhängige Ereignisse wird die Wahrscheinlichkeit, dass alle eintreten, ein einfaches Produkt, und mit dem Gegenereignis ebenso die Wahrscheinlichkeit, dass mindestens eines eintritt: $P(\text{mindestens ein }A_i)=1-\prod_i\bigl(1-P(A_i)\bigr)$, weil auch die Gegenereignisse unabhängig sind.

::::beispiel [Rechenbeispiel 1]
Zehn Bauteile fallen unabhängig voneinander mit je $5\,\%$ Wahrscheinlichkeit aus. Dann fällt keines aus mit der Wahrscheinlichkeit $0{,}95^{10}\approx0{,}599$, und mindestens eines mit $1-0{,}95^{10}\approx0{,}401$.
::::

::::beispiel [Rechenbeispiel 2] paarweise, aber nicht gegenseitig
Zwei Bits $b_1$ und $b_2$ werden durch faire, unabhängige Münzwürfe bestimmt. Ein drittes Bit ist das Paritätsbit $b_3=b_1\oplus b_2$, also $1$, wenn genau eines der beiden Bits $1$ ist. Die vier gleich wahrscheinlichen Fälle sind $(b_1,b_2,b_3)\in\{(0,0,0),(0,1,1),(1,0,1),(1,1,0)\}$. Es sei $A_k$ = „$b_k=1$“. Jedes $A_k$ hat die Wahrscheinlichkeit $\tfrac12$, und je zwei treten in genau einem der vier Fälle gemeinsam ein, mit der Wahrscheinlichkeit $\tfrac14=\tfrac12\cdot\tfrac12$. Also sind die drei Ereignisse paarweise unabhängig. Aber $A_1\cap A_2\cap A_3$ tritt nie ein, denn wenn $b_1=b_2=1$ ist, ist $b_3=0$: $P(A_1\cap A_2\cap A_3)=0\ne\tfrac18$. Jedes Bit für sich verrät nichts über ein anderes, zwei Bits zusammen legen das dritte fest. Genau darauf beruht die Fehlererkennung mit Paritätsbits.
::::

⁠**Kurz gesagt:** Mehrere Ereignisse sind unabhängig, wenn die Produktformel für jede Auswahl gilt; paarweise Unabhängigkeit reicht dafür nicht.

### Bedingte Unabhängigkeit

<span class="anker" id="stufe-5-4"></span>

Ein Teil wird von zwei Prüfgeräten derselben Bauart unabhängig voneinander geprüft. Für ein defektes Teil gibt jedes Gerät mit $99\,\%$ Alarm, für ein intaktes mit $5\,\%$, und die beiden Geräte beeinflussen sich nicht. Sind die beiden Alarme dann unabhängig? Nicht ohne Weiteres: Hat das erste Gerät Alarm gegeben, ist das Teil eher defekt, und dann gibt auch das zweite eher Alarm. Unabhängig sind die Alarme erst, wenn man den Zustand des Teils kennt.

:::definition Definition 5.4 (Bedingte Unabhängigkeit)
<span class="anker" id="satz-5-4"></span>

Zwei Ereignisse $A$ und $B$ heißen __bedingt unabhängig__ gegeben ein Ereignis $C$ mit $P(C)>0$, wenn

<span class="anker" id="gl-5-3"></span>
$$P(A\cap B\mid C)=P(A\mid C)\,P(B\mid C). \tag{5.3}$$
:::

Unabhängigkeit und bedingte Unabhängigkeit folgen nicht auseinander. Das Beispiel zeigt die eine Richtung. Die andere: Zwei unabhängige Münzen $A$ = „erste Münze Kopf“ und $B$ = „zweite Münze Kopf“ sind gegeben $C$ = „genau eine Münze zeigt Kopf“ abhängig, denn unter $C$ schließen sie einander aus.

::::beispiel [Rechenbeispiel]
Es seien $W_1$, $W_2$ die Alarme der beiden Geräte, bedingt unabhängig gegeben $D$ und gegeben $D^{\mathrm c}$. Dann ist

$$P(W_1\cap W_2)=0{,}99^2\cdot0{,}01+0{,}05^2\cdot0{,}99=0{,}009801+0{,}002475=0{,}012276 .$$

Mit $P(W_1)=P(W_2)=0{,}0594$ aus Unterabschnitt [4.2](der-satz-von-bayes.html#stufe-4-2) ist $P(W_1)\,P(W_2)\approx0{,}00353$, viel weniger: Ohne Kenntnis des Zustands sind die Alarme abhängig. Wie wahrscheinlich ist ein Teil defekt, das bei beiden Geräten Alarm auslöst? Nach Bayes ist $P(D\mid W_1\cap W_2)=0{,}009801/0{,}012276\approx0{,}798$. Dasselbe erhält man, wenn man Bayes zweimal nacheinander anwendet: Nach dem ersten Alarm ist $P(D\mid W_1)=\tfrac16$, und diese Zahl dient beim zweiten Gerät als neue Basisrate,

$$P(D\mid W_1\cap W_2)=\frac{0{,}99\cdot\tfrac16}{0{,}99\cdot\tfrac16+0{,}05\cdot\tfrac56}=\frac{0{,}165}{0{,}165+0{,}041\overline6}\approx0{,}798 .$$

Ein zweiter Befund, der gegeben den Zustand des Teils unabhängig vom ersten ist, hebt die Wahrscheinlichkeit von $17\,\%$ auf $80\,\%$.
::::

⁠**Kurz gesagt:** Bedingt unabhängig heißt unabhängig, sobald man die Bedingung kennt; zwei Befunde derselben Ursache sind meist bedingt unabhängig, aber nicht unabhängig.

:::aufgabe Aufgabe 12 ★ Unabhängig oder nicht?
<span class="anker" id="aufg-12"></span>

Zwei faire Würfel werden geworfen. $A$ sei „der rote Würfel zeigt eine gerade Zahl“, $B$ „die Augensumme ist $7$“, $C$ „die Augensumme ist $8$“.

<ol class="al">

<li>

Sind $A$ und $B$ unabhängig?

</li>

<li>

Sind $A$ und $C$ unabhängig?

</li>

<li>

Erkläre anschaulich, warum die Antworten verschieden ausfallen.

</li>

</ol>

:::loesung
(a) $P(A)=\tfrac12$, $P(B)=\tfrac16$. $A\cap B$ enthält $(2,5)$, $(4,3)$, $(6,1)$, also $P(A\cap B)=\tfrac3{36}=\tfrac1{12}=\tfrac12\cdot\tfrac16$: unabhängig.

(b) $P(C)=\tfrac5{36}$, denn $C$ enthält $(2,6),(3,5),(4,4),(5,3),(6,2)$. $A\cap C$ enthält $(2,6)$, $(4,4)$, $(6,2)$, also $P(A\cap C)=\tfrac3{36}=\tfrac1{12}$, aber $P(A)P(C)=\tfrac5{72}$: abhängig.

(c) Zur Summe $7$ passt jede Augenzahl des roten Würfels mit genau einer des blauen. Gegeben die Summe $7$ ist der rote Würfel deshalb weiterhin gleichmäßig auf $1$ bis $6$ verteilt, und gerade ist er mit $\tfrac12$. Zur Summe $8$ passt eine Eins des roten Würfels nicht; es bleiben die fünf Werte $2$ bis $6$, von denen drei gerade sind. Die Information „Summe $8$“ macht eine gerade Augenzahl also wahrscheinlicher, $\tfrac35$ statt $\tfrac12$.
:::
:::

:::aufgabe Aufgabe 13 ★★ Reihen- und Parallelschaltung
<span class="anker" id="aufg-13"></span>

Drei Bauteile arbeiten unabhängig voneinander und funktionieren jeweils mit der Wahrscheinlichkeit $0{,}9$.

<ol class="al">

<li>

In Reihe geschaltet funktioniert die Schaltung nur, wenn alle drei funktionieren. Wie wahrscheinlich ist das?

</li>

<li>

Parallel geschaltet funktioniert sie, wenn mindestens eines funktioniert. Wie wahrscheinlich ist das?

</li>

<li>

Wie viele parallele Bauteile braucht man, damit die Schaltung mit mindestens $99{,}99\,\%$ funktioniert?

</li>

</ol>

:::loesung
(a) $0{,}9^3=0{,}729$.

(b) Die Schaltung fällt nur aus, wenn alle drei ausfallen; das hat die Wahrscheinlichkeit $0{,}1^3=0{,}001$. Also funktioniert sie mit $0{,}999$.

(c) $1-0{,}1^n\ge0{,}9999$ verlangt $0{,}1^n\le10^{-4}$, also $n\ge4$. Vier parallele Bauteile genügen.
:::
:::

:::aufgabe Aufgabe 14 ★★★ Paritätsbits
<span class="anker" id="aufg-14"></span>

Es seien $b_1,\dots,b_{n}$ unabhängige faire Bits und $b_{n+1}=b_1\oplus\dots\oplus b_n$ ihr Paritätsbit, sodass die Summe aller $n+1$ Bits gerade ist.

<ol class="al">

<li>

Zeige für $n=2$, dass die Ereignisse $b_1=1$ und $b_3=0$ unabhängig sind.

</li>

<li>

Zeige für allgemeines $n$: Je $n$ der $n+1$ Bits sind gegenseitig unabhängig, alle $n+1$ zusammen nicht.

</li>

</ol>

:::loesung
(a) $b_3=0$ heißt $b_1=b_2$. Also ist $P(b_1=1,\ b_3=0)=P(b_1=1,\ b_2=1)=\tfrac14=\tfrac12\cdot\tfrac12$, und die Ereignisse sind unabhängig.

(b) Lässt man ein Bit $b_j$ mit $j\le n$ weg, so bleiben $n-1$ der freien Bits und das Paritätsbit. Gegeben die $n-1$ freien Bits ist das Paritätsbit $b_{n+1}=c\oplus b_j$ mit einer festen Zahl $c$; weil $b_j$ fair und unabhängig ist, ist $b_{n+1}$ dann mit je $\tfrac12$ null oder eins. Also sind alle $2^n$ Belegungen der verbleibenden $n$ Bits gleich wahrscheinlich, jede mit $2^{-n}$, und das ist gegenseitige Unabhängigkeit fairer Bits: Jede Produktformel [(5.2)](#gl-5-2) gilt, weil auch jede Teilauswahl alle ihre Belegungen gleich wahrscheinlich annimmt. Lässt man das Paritätsbit weg, sind es die freien Bits, die nach Voraussetzung unabhängig sind. Alle $n+1$ Bits zusammen sind nicht unabhängig, denn nur die $2^n$ Belegungen mit gerader Summe kommen vor: Eine Belegung mit ungerader Summe hat die Wahrscheinlichkeit $0$, nicht $2^{-(n+1)}$.
:::
:::

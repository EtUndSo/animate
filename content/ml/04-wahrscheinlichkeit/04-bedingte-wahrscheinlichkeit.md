---
title: Bedingte Wahrscheinlichkeit
pfad: Informatik / Machine Learning / Wahrscheinlichkeit
order: 6240400
summary: Erfährt man etwas über den Ausgang eines Experiments, ändern sich die Wahrscheinlichkeiten.
tags: gemeinsame Wahrscheinlichkeit, Randwahrscheinlichkeiten, Summenregel, bedingte Wahrscheinlichkeit, Verkettung, Zerlegung
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Erfährt man etwas über den Ausgang eines Experiments, ändern sich die Wahrscheinlichkeiten. Dieser Abschnitt zeigt an einer Zähltabelle, wie man das rechnet: Man betrachtet nur noch die Fälle, die zur neuen Information passen. Daraus folgen die Produktregel für das gemeinsame Eintreten mehrerer Ereignisse und der Satz von der totalen Wahrscheinlichkeit, der eine Wahrscheinlichkeit aus Fallunterscheidungen zusammensetzt.
:::

### Wahrscheinlichkeiten aus einer Zähltabelle

<span class="anker" id="stufe-3-1"></span>

Beobachtet man zwei Merkmale zugleich, ordnet man die Beobachtungen in eine Tabelle. Jemand notiert an $200$ Tagen, ob die Sonne scheint oder es regnet und ob er mit dem Fahrrad zur Arbeit fährt (Tabelle [1](#tab-1)). In jeder Zelle steht, wie oft beide Merkmale zusammen auftraten, am Rand stehen die Zeilen- und Spaltensummen.

<span class="anker" id="tab-1"></span>

**Tabelle 1:** Zähltabelle für $200$ Tage: Wetter und Verkehrsmittel. Am rechten und unteren Rand die Summen.

|  | Fahrrad | kein Fahrrad | Summe |
|---|---|---|---|
| Sonne | $60$ | $20$ | $80$ |
| Regen | $20$ | $100$ | $120$ |
| Summe | $80$ | $120$ | $200$ |

Teilt man jede Zahl durch $200$, entstehen relative Häufigkeiten. Sie sind genau die Wahrscheinlichkeiten für einen Tag, den man aus diesen $200$ Tagen rein zufällig herausgreift, und mit ihnen rechnet dieser Abschnitt. Die Zelle „Sonne und Fahrrad“ ergibt $60/200=0{,}3$. Das ist der Anteil der Tage, an denen beides zusammen eintrat. Eine Wahrscheinlichkeit $P(A\cap B)$ für das gemeinsame Eintreten zweier Ereignisse heißt __gemeinsame Wahrscheinlichkeit__. Die Zeilensumme „Sonne“ ergibt $80/200=0{,}4$, die Wahrscheinlichkeit von „Sonne“ allein, gleichgültig, wie man zur Arbeit kommt. Weil solche Zahlen am Rand der Tabelle stehen, heißen sie __Randwahrscheinlichkeiten__.

Die Randsumme entsteht, indem man über die Zellen einer Zeile addiert. In Wahrscheinlichkeiten ausgedrückt: Die Ereignisse „Sonne und Fahrrad“ und „Sonne und kein Fahrrad“ sind unvereinbar, und ihre Vereinigung ist „Sonne“. Allgemein gilt nach Axiom (iii) für zwei Ereignisse

<span class="anker" id="gl-3-1"></span>
$$P(A)=P(A\cap B)+P(A\cap B^{\mathrm c}). \tag{3.1}$$

Diese Regel heißt __Summenregel__.

⁠**Rechenbeispiel:** Aus Tabelle [1](#tab-1) ist $P(\text{Sonne}\cap\text{Fahrrad})=0{,}3$, $P(\text{Sonne}\cap\text{kein Fahrrad})=0{,}1$, $P(\text{Regen}\cap\text{Fahrrad})=0{,}1$ und $P(\text{Regen}\cap\text{kein Fahrrad})=0{,}5$. Die Summenregel ergibt $P(\text{Sonne})=0{,}3+0{,}1=0{,}4$ und $P(\text{Fahrrad})=0{,}3+0{,}1=0{,}4$. Alle vier Zellen zusammen ergeben $1$.

⁠**Kurz gesagt:** In einer Zähltabelle stehen in den Zellen die gemeinsamen Wahrscheinlichkeiten und am Rand die Randwahrscheinlichkeiten; eine Randwahrscheinlichkeit ist die Summe ihrer Zeile oder Spalte.

### Bedingte Wahrscheinlichkeit

<span class="anker" id="stufe-3-2"></span>

Angenommen, man weiß schon, dass heute die Sonne scheint. Wie wahrscheinlich ist es dann, dass die Person mit dem Fahrrad fährt? Die Regentage spielen keine Rolle mehr; es zählt nur noch die Zeile „Sonne“ in Tabelle [1](#tab-1). An $60$ von $80$ Sonnentagen fuhr sie Fahrrad, also in $75\,\%$ der Fälle. Der Ergebnisraum ist auf die Sonnentage geschrumpft, und man misst Anteile in ihm.

:::definition Definition 3.1 (Bedingte Wahrscheinlichkeit)
<span class="anker" id="satz-3-1"></span>

Für Ereignisse $A$ und $B$ mit $P(B)>0$ heißt

<span class="anker" id="gl-3-2"></span>
$$P(A\mid B)=\frac{P(A\cap B)}{P(B)} \tag{3.2}$$

die __bedingte Wahrscheinlichkeit__ von $A$ unter der Bedingung $B$, kurz „$A$ gegeben $B$“.
:::

Der Zähler ist der Teil von $A$, der in $B$ liegt, der Nenner der Inhalt von $B$. Die Division sorgt dafür, dass $B$ selbst die Wahrscheinlichkeit $1$ bekommt: $P(B\mid B)=1$. Als Funktion von $A$ erfüllt $P(\,\cdot\mid B)$ alle drei Axiome. Bedingte Wahrscheinlichkeiten sind also gewöhnliche Wahrscheinlichkeiten auf dem geschrumpften Ergebnisraum $B$, und alle Rechenregeln aus Abschnitt [2](wahrscheinlichkeit.html#stufe-2) gelten für sie, etwa $P(A^{\mathrm c}\mid B)=1-P(A\mid B)$.

⁠**Rechenbeispiel 1:** Aus Tabelle [1](#tab-1) ist $P(\text{Fahrrad}\mid\text{Sonne})=0{,}3/0{,}4=0{,}75$ und $P(\text{Fahrrad}\mid\text{Regen})=0{,}1/0{,}6=1/6\approx0{,}167$. Ohne Information über das Wetter ist $P(\text{Fahrrad})=0{,}4$. Die Information „Sonne“ hebt die Wahrscheinlichkeit also deutlich, die Information „Regen“ senkt sie.

⁠**Rechenbeispiel 2:** Beim fairen Würfel ist $P(\{6\}\mid\text{gerade})=\frac{1/6}{1/2}=\frac13$: Unter den drei geraden Zahlen ist die Sechs eine. Umgekehrt ist $P(\text{gerade}\mid\{6\})=1$.

:::warnung $P(A\mid B)$ und $P(B\mid A)$ sind verschiedene Zahlen
Das zweite Rechenbeispiel zeigt es: $P(\{6\}\mid\text{gerade})=\tfrac13$, aber $P(\text{gerade}\mid\{6\})=1$. Die beiden Zahlen haben denselben Zähler $P(A\cap B)$, aber verschiedene Nenner. Wer sie verwechselt, macht einen der häufigsten Fehler im Umgang mit Wahrscheinlichkeiten. Abschnitt [4](der-satz-von-bayes.html#stufe-4) zeigt, wie man von der einen zur anderen kommt und wie groß der Unterschied werden kann.
:::

⁠**Kurz gesagt:** Bedingen heißt, nur noch die Fälle zu betrachten, in denen $B$ eingetreten ist, und Anteile in ihnen zu messen: $P(A\mid B)=P(A\cap B)/P(B)$.

:::hintergrund Bedingen heißt beobachten, nicht eingreifen
$P(\text{Fahrrad}\mid\text{Sonne})=0{,}75$ beschreibt, was man an Sonnentagen beobachtet. Es sagt nicht, was geschähe, wenn man die Sonne scheinen ließe, und umgekehrt bringt das Fahrradfahren keinen Sonnenschein, obwohl $P(\text{Sonne}\mid\text{Fahrrad})=0{,}75$ ebenfalls groß ist. Ein deutlicheres Beispiel: Wer fließend Deutsch spricht, stammt mit hoher Wahrscheinlichkeit aus einem deutschsprachigen Land. Wer Deutsch lernt, ändert seine Herkunft aber nicht. Eine bedingte Wahrscheinlichkeit misst einen Zusammenhang in den beobachteten Fällen. Ob eine Größe die andere verursacht, ist eine andere Frage, die man mit Beobachtungen allein meist nicht beantworten kann. Für Verfahren, die aus Daten lernen, ist das eine wichtige Grenze: Sie lernen Zusammenhänge, keine Ursachen.
:::

### Die Produktregel

<span class="anker" id="stufe-3-3"></span>

Oft kennt man bedingte Wahrscheinlichkeiten und sucht die gemeinsame. Ein Teil wird geprüft, und man kennt den Anteil defekter Teile und die Trefferquote der Prüfung; gesucht ist der Anteil der Teile, die defekt sind und erkannt werden. Dafür löst man die Definition [(3.2)](#gl-3-2) nach dem Zähler auf.

:::satz Satz 3.2 (Produktregel)
<span class="anker" id="satz-3-2"></span>

Für Ereignisse $A$ und $B$ gilt

<span class="anker" id="gl-3-3"></span>
$$P(A\cap B)=P(A\mid B)\,P(B)=P(B\mid A)\,P(A), \tag{3.3}$$

wobei die erste Form $P(B)>0$ und die zweite $P(A)>0$ voraussetzt. Für mehrere Ereignisse gilt die __Verkettung__

<span class="anker" id="gl-3-4"></span>
$$P(A_1\cap A_2\cap\dots\cap A_m)=P(A_1)\,P(A_2\mid A_1)\,P(A_3\mid A_1\cap A_2)\cdots P(A_m\mid A_1\cap\dots\cap A_{m-1}). \tag{3.4}$$
:::

Die Verkettung folgt, indem man die Produktregel wiederholt anwendet, zuerst auf $A_1\cap\dots\cap A_{m-1}$ und $A_m$, dann auf den Rest. Sie liest sich wie eine Geschichte in Schritten: Zuerst muss $A_1$ eintreten, dann, nachdem $A_1$ eingetreten ist, $A_2$, und so weiter.

⁠**Rechenbeispiel:** In einer Kiste liegen $10$ Bauteile, davon $2$ defekte. Man entnimmt nacheinander drei, ohne sie zurückzulegen. $A_k$ sei „das $k$-te entnommene Teil ist intakt“. Beim ersten Griff sind $8$ von $10$ Teilen intakt, beim zweiten, nachdem ein intaktes fehlt, $7$ von $9$, beim dritten $6$ von $8$. Die Verkettung multipliziert diese drei Anteile und ergibt $P(\text{alle drei intakt})=\tfrac7{15}\approx0{,}467$ (Abb. [1](#abb-1)). Mit über $50\,\%$ ist also mindestens ein defektes Teil dabei.

:::abbildung ml/k4rverkettung 1
Die Verkettung für drei Entnahmen ohne Zurücklegen: Jeder Faktor ist der Anteil intakter Teile unter denen, die noch in der Kiste liegen.
:::

:::warnung Zwei Kettenregeln
Manche Texte nennen die Verkettung [(3.4)](#gl-3-4) „Kettenregel der Wahrscheinlichkeit“. Mit der Kettenregel der Ableitung aus [Teil 3](/wissen/informatik/machine-learning/ableitung-gradient-und-kettenregel/ableitung-gradient-und-kettenregel.html), Abschnitt 2.2, hat sie nichts zu tun. Gemeinsam ist beiden nur, dass ein Ganzes als Produkt von Schritten geschrieben wird.
:::

⁠**Kurz gesagt:** Die gemeinsame Wahrscheinlichkeit ist bedingte Wahrscheinlichkeit mal Wahrscheinlichkeit der Bedingung; bei mehreren Ereignissen multipliziert man Schritt für Schritt.

### Die totale Wahrscheinlichkeit

<span class="anker" id="stufe-3-4"></span>

Bauteile kommen aus zwei Fabriken, die verschieden sorgfältig arbeiten. Wie groß ist der Ausschussanteil insgesamt? Man unterscheidet die Fälle: Für jede Fabrik kennt man ihren Ausschussanteil und ihren Anteil an der Lieferung. Der Gesamtanteil ist dann ein gewichteter Mittelwert der Ausschussanteile, gewichtet mit den Lieferanteilen.

Für die Fallunterscheidung braucht man Ereignisse, die alle Möglichkeiten abdecken und sich nicht überschneiden. Ereignisse $B_1,\dots,B_k$ mit positiven Wahrscheinlichkeiten heißen eine __Zerlegung__ von $\Omega$, wenn je zwei disjunkt sind und ihre Vereinigung $\Omega$ ist. Bei jedem Ausgang des Experiments tritt dann genau eines von ihnen ein.

:::satz Satz 3.3 (Totale Wahrscheinlichkeit)
<span class="anker" id="satz-3-3"></span>

Ist $B_1,\dots,B_k$ eine Zerlegung von $\Omega$, so gilt für jedes Ereignis $A$

<span class="anker" id="gl-3-5"></span>
$$P(A)=\sum_{i=1}^kP(A\mid B_i)\,P(B_i). \tag{3.5}$$
:::

:::beweis Totale Wahrscheinlichkeit
Die Mengen $A\cap B_1,\dots,A\cap B_k$ sind disjunkt, und ihre Vereinigung ist $A$, denn jedes Ergebnis aus $A$ liegt in genau einem $B_i$. Nach Axiom (iii) ist $P(A)=\sum_iP(A\cap B_i)$, und nach der Produktregel ist $P(A\cap B_i)=P(A\mid B_i)\,P(B_i)$.
:::

Für die Zerlegung $B$, $B^{\mathrm c}$ ist das die Summenregel [(3.1)](#gl-3-1), mit der Produktregel umgeschrieben. Der Satz ist ein gewichteter Mittelwert: Die Gewichte $P(B_i)$ sind nichtnegativ und ergeben zusammen $1$, also liegt $P(A)$ immer zwischen der kleinsten und der größten der Zahlen $P(A\mid B_i)$.

⁠**Rechenbeispiel:** Fabrik 1 liefert $60\,\%$ der Teile mit $1\,\%$ Ausschuss, Fabrik 2 liefert $40\,\%$ mit $3\,\%$ Ausschuss. Mit $B_i$ = „aus Fabrik $i$“ und $A$ = „Ausschuss“ ergibt [(3.5)](#gl-3-5) einen Ausschussanteil von $1{,}8\,\%$ (Abb. [2](#abb-2)). Er liegt zwischen $1\,\%$ und $3\,\%$, näher bei $1\,\%$, weil Fabrik 1 mehr liefert. Ebenso ergibt Tabelle [1](#tab-1) $P(\text{Fahrrad})=0{,}75\cdot0{,}4+\tfrac16\cdot0{,}6=0{,}3+0{,}1=0{,}4$.

:::abbildung ml/k4rtotal 2
Der Satz von der totalen Wahrscheinlichkeit für zwei Fabriken: Ausschussanteil jeder Fabrik mal ihr Lieferanteil, dann die Summe.
:::

⁠**Kurz gesagt:** Eine Wahrscheinlichkeit ist der mit $P(B_i)$ gewichtete Mittelwert der bedingten Wahrscheinlichkeiten über alle Fälle einer Zerlegung.

:::aufgabe Aufgabe 6 ★ Eine Prüftabelle
<span class="anker" id="aufg-6"></span>

Von $500$ geprüften Bauteilen stammen $300$ von Lieferant A und $200$ von Lieferant B. Von denen aus A waren $12$ defekt, von denen aus B $18$.

<ol class="al">

<li>

Stelle die Zähltabelle mit Randsummen auf und gib alle gemeinsamen Wahrscheinlichkeiten und die Randwahrscheinlichkeiten an.

</li>

<li>

Berechne $P(\text{defekt}\mid\text{A})$, $P(\text{defekt}\mid\text{B})$ und $P(\text{A}\mid\text{defekt})$.

</li>

</ol>

:::loesung
(a) Lieferant A: $12$ defekt, $288$ in Ordnung, Summe $300$; Lieferant B: $18$ defekt, $182$ in Ordnung, Summe $200$; Spaltensummen $30$ defekt und $470$ in Ordnung, insgesamt $500$. Geteilt durch $500$: $P(\text{A}\cap\text{defekt})=0{,}024$, $P(\text{A}\cap\text{ok})=0{,}576$, $P(\text{B}\cap\text{defekt})=0{,}036$, $P(\text{B}\cap\text{ok})=0{,}364$. Randwahrscheinlichkeiten: $P(\text A)=0{,}6$, $P(\text B)=0{,}4$, $P(\text{defekt})=0{,}06$, $P(\text{ok})=0{,}94$.

(b) $P(\text{defekt}\mid\text A)=12/300=0{,}04$, $P(\text{defekt}\mid\text B)=18/200=0{,}09$ und $P(\text A\mid\text{defekt})=12/30=0{,}4$. Obwohl A mehr liefert, stammen nur $40\,\%$ der defekten Teile von A, weil B mehr als doppelt so oft defekte Teile liefert.
:::
:::

:::aufgabe Aufgabe 7 ★★ Entnahme ohne Zurücklegen
<span class="anker" id="aufg-7"></span>

In der Kiste aus dem Rechenbeispiel zu Unterabschnitt [3.3](#stufe-3-3) liegen $10$ Teile, davon $2$ defekte.

<ol class="al">

<li>

Man entnimmt zwei Teile. Wie wahrscheinlich sind beide defekt?

</li>

<li>

Wie wahrscheinlich ist das zweite entnommene Teil defekt, wenn man über das erste nichts weiß? Benutze die totale Wahrscheinlichkeit mit der Zerlegung nach dem ersten Teil.

</li>

<li>

Wie wahrscheinlich ist unter drei entnommenen Teilen genau ein defektes?

</li>

</ol>

:::loesung
(a) $P(\text{beide defekt})=\tfrac2{10}\cdot\tfrac19=\tfrac2{90}=\tfrac1{45}\approx0{,}022$.

(b) Mit $D_k$ = „das $k$-te Teil ist defekt“:

$$P(D_2)=P(D_2\mid D_1)\,P(D_1)+P(D_2\mid D_1^{\mathrm c})\,P(D_1^{\mathrm c})=\tfrac19\cdot\tfrac2{10}+\tfrac29\cdot\tfrac8{10}=\tfrac{2+16}{90}=\tfrac15 .$$

Ohne Information über das erste Teil ist das zweite genauso wahrscheinlich defekt wie das erste. Das ist keine Unabhängigkeit, sondern Symmetrie: Jedes der zehn Teile landet mit derselben Wahrscheinlichkeit an zweiter Stelle.

(c) Das defekte Teil kann an erster, zweiter oder dritter Stelle kommen. Jede dieser Reihenfolgen hat nach der Verkettung die Wahrscheinlichkeit $\tfrac{2\cdot8\cdot7}{10\cdot9\cdot8}=\tfrac{112}{720}$, zum Beispiel $\tfrac2{10}\cdot\tfrac89\cdot\tfrac78$. Zusammen $\tfrac{336}{720}=\tfrac7{15}\approx0{,}467$. Probe: Null defekte $\tfrac7{15}$, ein defektes $\tfrac7{15}$, zwei defekte $3\cdot\tfrac{2\cdot1\cdot8}{720}=\tfrac1{15}$, Summe $1$.
:::
:::

:::aufgabe Aufgabe 8 ★★ Drei Maschinen
<span class="anker" id="aufg-8"></span>

Drei Maschinen fertigen $50\,\%$, $30\,\%$ und $20\,\%$ der Teile mit Ausschussanteilen von $2\,\%$, $3\,\%$ und $5\,\%$.

<ol class="al">

<li>

Berechne den gesamten Ausschussanteil.

</li>

<li>

Um wie viel sinkt er, wenn man die dritte Maschine so einstellt, dass sie nur noch $2\,\%$ Ausschuss hat?

</li>

</ol>

:::loesung
(a) $0{,}5\cdot0{,}02+0{,}3\cdot0{,}03+0{,}2\cdot0{,}05=0{,}010+0{,}009+0{,}010=0{,}029$, also $2{,}9\,\%$.

(b) $0{,}010+0{,}009+0{,}2\cdot0{,}02=0{,}023$. Der Anteil sinkt um $0{,}006$, also um $0{,}6$ Prozentpunkte. Obwohl die dritte Maschine nur $20\,\%$ liefert, trug sie über ein Drittel des Ausschusses bei.
:::
:::

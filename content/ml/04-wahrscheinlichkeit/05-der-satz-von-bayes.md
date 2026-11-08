---
title: Der Satz von Bayes
pfad: Informatik / Machine Learning / Mathematische Grundlagen / Wahrscheinlichkeit
knoten: Grundlagen 4: Wahrscheinlichkeit
nachschlagen: ja
order: 15240500
summary: Häufig kennt man, wie wahrscheinlich ein Befund bei einer Ursache ist, und will umgekehrt wissen, wie wahrscheinlich die Ursache ist, wenn man den Befund beobachtet hat.
tags: Ausgangswahrscheinlichkeit, Fehlalarm, natürliche Häufigkeiten, Basisrate, Basisratenfehler
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Häufig kennt man, wie wahrscheinlich ein Befund bei einer Ursache ist, und will umgekehrt wissen, wie wahrscheinlich die Ursache ist, wenn man den Befund beobachtet hat. Ein Prüfgerät erkennt defekte Teile fast immer; wie sicher ist ein Teil defekt, wenn das Gerät Alarm gibt? Dieser Abschnitt leitet die Formel für die Umkehrung her, rechnet sie mit natürlichen Häufigkeiten nach und zeigt, warum die Antwort so stark davon abhängt, wie häufig die Ursache überhaupt ist.
:::

### Die Bedingung umdrehen

<span class="anker" id="stufe-4-1"></span>

Die Produktregel [(3.3)](bedingte-wahrscheinlichkeit.html#gl-3-3) schreibt dieselbe gemeinsame Wahrscheinlichkeit auf zwei Arten: $P(A\mid B)\,P(B)=P(B\mid A)\,P(A)$. Teilt man durch $P(A)$, steht die gesuchte Umkehrung da.

:::satz Satz 4.1 (Satz von Bayes)
<span class="anker" id="satz-4-1"></span>

Für Ereignisse $A$ und $B$ mit $P(A)>0$ und $P(B)>0$ gilt

<span class="anker" id="gl-4-1"></span>
$$P(B\mid A)=\frac{P(A\mid B)\,P(B)}{P(A)} . \tag{4.1}$$

Ist $B_1,\dots,B_k$ eine Zerlegung von $\Omega$, so ist für jedes $j$

<span class="anker" id="gl-4-2"></span>
$$P(B_j\mid A)=\frac{P(A\mid B_j)\,P(B_j)}{\sum_{i=1}^kP(A\mid B_i)\,P(B_i)} . \tag{4.2}$$
:::

Die zweite Form setzt für den Nenner die totale Wahrscheinlichkeit [(3.5)](bedingte-wahrscheinlichkeit.html#gl-3-5) ein. Sie zeigt, was der Satz tut. Jeder Fall $B_i$ hat eine __Ausgangswahrscheinlichkeit__ $P(B_i)$, die gilt, bevor man $A$ beobachtet. Jeder Fall bekommt das Gewicht $P(A\mid B_i)\,P(B_i)$: seine Ausgangswahrscheinlichkeit mal der Wahrscheinlichkeit, mit der er die Beobachtung hervorbringt. Dann teilt man alle Gewichte durch ihre Summe, sodass sie zusammen $1$ ergeben. Fälle, die die Beobachtung gut erklären, gewinnen; Fälle, die sie schlecht erklären, verlieren.

⁠**Rechenbeispiel:** Ein Teil aus der Lieferung von Unterabschnitt [3.4](bedingte-wahrscheinlichkeit.html#stufe-3-4) ist Ausschuss. Aus welcher Fabrik stammt es? Vor der Beobachtung spricht mehr für Fabrik 1, denn sie liefert $60\,\%$. Nach [(4.2)](#gl-4-2) ist

$$P(B_2\mid A)=\frac{0{,}03\cdot0{,}4}{0{,}018}=\frac{0{,}012}{0{,}018}=\frac23,\qquad P(B_1\mid A)=\frac{0{,}006}{0{,}018}=\frac13 .$$

Der Ausschuss kehrt das Verhältnis um: Weil Fabrik 2 dreimal so viel Ausschuss macht, stammen zwei Drittel des Ausschusses von ihr, obwohl sie weniger liefert.

⁠**Kurz gesagt:** Der Satz von Bayes dreht eine Bedingung um: Ausgangswahrscheinlichkeit mal Wahrscheinlichkeit der Beobachtung, geteilt durch die Summe dieser Produkte über alle Fälle.

### Natürliche Häufigkeiten

<span class="anker" id="stufe-4-2"></span>

Ein Prüfgerät untersucht Bauteile. $1\,\%$ der Teile ist defekt. Ist ein Teil defekt, gibt das Gerät mit $99\,\%$ Wahrscheinlichkeit Alarm; ist es intakt, gibt es trotzdem mit $5\,\%$ Wahrscheinlichkeit Alarm, einen __Fehlalarm__. Ein Teil löst Alarm aus. Wie wahrscheinlich ist es defekt? Viele schätzen etwa $95\,\%$. Die Rechnung wird durchsichtig, wenn man statt mit Wahrscheinlichkeiten mit Anzahlen in einer gedachten großen Menge rechnet.

Solche Anzahlen heißen __natürliche Häufigkeiten__: Man stellt sich eine feste Zahl von Fällen vor, etwa $10\,000$ Teile, und verteilt sie mit den gegebenen Anteilen auf die Zweige eines Baums (Abb. [3](#abb-3)). Von $10\,000$ Teilen sind $100$ defekt und $9\,900$ intakt. Von den $100$ defekten erkennt das Gerät $99$. Von den $9\,900$ intakten meldet es $5\,\%$, also $495$. Insgesamt gibt es $99+495=594$ Alarme, und nur $99$ davon gehören zu defekten Teilen.

:::abbildung ml/k4baum 3
Das Prüfgerät mit natürlichen Häufigkeiten: $10\,000$ gedachte Teile werden mit den gegebenen Anteilen auf die Zweige verteilt. Die Alarme (rot) stammen zum größten Teil von intakten Teilen, weil es so viel mehr intakte als defekte Teile gibt.
:::

Der Baum ist die Verkettung [(3.4)](bedingte-wahrscheinlichkeit.html#gl-3-4) in Bildform: Jeder Pfad multipliziert die Anteile an seinen Kanten, und die Zahl am Blatt ist die gemeinsame Häufigkeit. Mit dem Satz von Bayes ergibt sich dasselbe. Mit $D$ = „defekt“ und $W$ = „Alarm“ ist $P(W)=0{,}99\cdot0{,}01+0{,}05\cdot0{,}99=0{,}0594$ und $P(D\mid W)=0{,}0099/0{,}0594=1/6$ (Abb. [4](#abb-4)).

:::abbildung ml/k4rbayes 4
Das Prüfgerät mit dem Satz von Bayes: Der Nenner ist die totale Wahrscheinlichkeit eines Alarms, die Summe aus echten Alarmen und Fehlalarmen.
:::

⁠**Rechenbeispiel:** Das Gerät gibt bei einem Teil keinen Alarm. Im Baum gibt es $1+9\,405=9\,406$ Teile ohne Alarm, davon $1$ defektes. Also ist $P(D\mid W^{\mathrm c})=1/9\,406\approx0{,}011\,\%$. Ein Teil ohne Alarm ist fast sicher intakt.

⁠**Kurz gesagt:** Natürliche Häufigkeiten verteilen eine gedachte große Zahl von Fällen auf die Zweige eines Baums; die gesuchte bedingte Wahrscheinlichkeit ist dann ein einfacher Anteil.

### Die Basisrate

<span class="anker" id="stufe-4-3"></span>

Das Prüfgerät erkennt $99\,\%$ der Defekte und irrt sich bei intakten Teilen nur in $5\,\%$ der Fälle, und trotzdem ist nur jedes sechste Teil mit Alarm defekt. Der Grund liegt nicht im Gerät, sondern darin, wie selten Defekte sind.

:::definition Definition 4.2 (Basisrate)
<span class="anker" id="satz-4-2"></span>

Die Wahrscheinlichkeit einer Ursache, bevor man einen Befund beobachtet hat, heißt __Basisrate__. Beim Prüfgerät ist sie der Anteil defekter Teile, $P(D)$.
:::

In [(4.1)](#gl-4-1) steht die Basisrate im Zähler. Ist sie klein, so ist auch die Zahl der echten Alarme klein, und die Fehlalarme aus der großen Masse intakter Teile überwiegen. Tabelle [2](#tab-2) zeigt, wie stark das Ergebnis davon abhängt.

<span class="anker" id="tab-2"></span>

**Tabelle 2:** Das Prüfgerät ($99\,\%$ Erkennung, $5\,\%$ Fehlalarm) bei verschiedenen Basisraten.

| Basisrate $P(D)$ | echte Alarme je $10\,000$ | Fehlalarme je $10\,000$ | $P(D\mid W)$ |
|---|---|---|---|
| $0{,}1\,\%$ | $9{,}9$ | $499{,}5$ | $1{,}9\,\%$ |
| $1\,\%$ | $99$ | $495$ | $16{,}7\,\%$ |
| $10\,\%$ | $990$ | $450$ | $68{,}8\,\%$ |
| $50\,\%$ | $4\,950$ | $250$ | $95{,}2\,\%$ |

⁠**Rechenbeispiel:** Bei einer Basisrate von $10\,\%$ sind von $10\,000$ Teilen $1\,000$ defekt, davon lösen $990$ Alarm aus; von den $9\,000$ intakten lösen $450$ einen Fehlalarm aus. Also ist $P(D\mid W)=990/1\,440=0{,}6875$. Dasselbe Gerät liefert bei $0{,}1\,\%$ Basisrate nur $9{,}9/509{,}4\approx1{,}9\,\%$.

⁠**Kurz gesagt:** Wie viel ein Befund beweist, hängt nicht nur vom Prüfverfahren ab, sondern stark von der Basisrate: Bei seltenen Ursachen sind die meisten positiven Befunde Fehlalarme.

:::hintergrund Warum wir die Basisrate übersehen
Die Intuition setzt $P(D\mid W)$ gern mit $P(W\mid D)=99\,\%$ gleich oder mit $1-P(W\mid D^{\mathrm c})=95\,\%$. Beide Zahlen beschreiben das Gerät, nicht die Teile, die Alarm auslösen. Die Fehlalarme sind selten pro intaktem Teil, aber es gibt $99$-mal so viele intakte wie defekte Teile; selten mal sehr viele ergibt viele. Diesen Denkfehler nennt man __Basisratenfehler__. Er ist auch bei Fachleuten verbreitet. In einer Befragung von 1978 sollten $60$ Ärztinnen, Ärzte und Studierende der Medizin einschätzen, wie wahrscheinlich jemand mit positivem Test krank ist, wenn die Krankheit einen von $1\,000$ Menschen betrifft und der Test bei Gesunden in $5\,\%$ der Fälle anschlägt. Fast die Hälfte antwortete $95\,\%$; richtig ist etwa $2\,\%$, und nur $11$ der $60$ fanden es. Spätere Versuche zeigten, dass Menschen solche Aufgaben viel öfter richtig lösen, wenn man die Angaben als natürliche Häufigkeiten statt als Prozente formuliert; in einer Untersuchung von 1995 stieg der Anteil richtiger Lösungswege je nach Aufgabenform von $16$ auf $46\,\%$ und von $28$ auf $50\,\%$. Der Baum macht die beiden Gruppen sichtbar, deren Größen die Prozentangaben verstecken.

Derselbe Fehler hat vor Gericht einen eigenen Namen, den Trugschluss des Anklägers: Aus „Wäre der Angeklagte unschuldig, wäre dieses Beweisstück sehr unwahrscheinlich“ wird fälschlich „Der Angeklagte ist sehr wahrscheinlich schuldig“. Ob der zweite Satz stimmt, hängt wie beim Prüfgerät von der Ausgangswahrscheinlichkeit der Schuld ab. Den Satz selbst fand der englische Pfarrer Thomas Bayes; sein Aufsatz wurde nach seinem Tod 1763 veröffentlicht. Pierre-Simon Laplace fand ihn unabhängig davon wieder und machte ihn zu einem allgemeinen Werkzeug.
:::

:::aufgabe Aufgabe 9 ★ Ein medizinischer Test
<span class="anker" id="aufg-9"></span>

Eine Krankheit betrifft $0{,}2\,\%$ der Bevölkerung. Ein Test ist bei Kranken in $90\,\%$ der Fälle positiv, bei Gesunden in $3\,\%$ der Fälle.

<ol class="al">

<li>

Zeichne den Baum mit natürlichen Häufigkeiten für $100\,000$ Personen.

</li>

<li>

Wie wahrscheinlich ist eine Person mit positivem Test krank?

</li>

<li>

Wie wahrscheinlich ist eine Person mit negativem Test gesund?

</li>

</ol>

:::loesung
(a) Von $100\,000$ Personen sind $200$ krank; davon sind $180$ positiv und $20$ negativ. Von den $99\,800$ Gesunden sind $3\,\%$, also $2\,994$, positiv und $96\,806$ negativ.

(b) Positiv sind $180+2\,994=3\,174$ Personen, davon $180$ krank: $P(\text{krank}\mid\text{positiv})=180/3\,174\approx5{,}7\,\%$. Trotz eines guten Tests ist nur etwa jede achtzehnte positiv getestete Person krank, weil die Basisrate sehr klein ist.

(c) Negativ sind $20+96\,806=96\,826$, davon $96\,806$ gesund: $P(\text{gesund}\mid\text{negativ})\approx99{,}98\,\%$. Ein negativer Test ist fast sicher richtig.
:::
:::

:::aufgabe Aufgabe 10 ★★ Zwei Kartons
<span class="anker" id="aufg-10"></span>

In Karton A liegen Widerstände, von denen $3$ von $10$ außerhalb der Toleranz liegen, in Karton B nur $1$ von $10$. Jemand wählt mit einem Münzwurf einen Karton und zieht daraus einen Widerstand. Er liegt außerhalb der Toleranz.

<ol class="al">

<li>

Wie wahrscheinlich stammt er aus Karton A?

</li>

<li>

Aus demselben Karton wird ein zweiter Widerstand gezogen (der erste wird zurückgelegt). Wie wahrscheinlich liegt auch er außerhalb der Toleranz?

</li>

</ol>

:::loesung
(a) Mit $T$ = „außerhalb der Toleranz“ ist $P(T)=0{,}5\cdot0{,}3+0{,}5\cdot0{,}1=0{,}2$ und $P(\text A\mid T)=0{,}15/0{,}2=0{,}75$.

(b) Nach der ersten Beobachtung gilt $P(\text A)=0{,}75$ und $P(\text B)=0{,}25$. Die totale Wahrscheinlichkeit mit diesen neuen Gewichten ergibt $0{,}75\cdot0{,}3+0{,}25\cdot0{,}1=0{,}25$. Vor der ersten Ziehung war die Wahrscheinlichkeit $0{,}2$. Der erste Widerstand außerhalb der Toleranz macht den schlechteren Karton wahrscheinlicher und damit auch einen zweiten solchen Widerstand. Die beiden Ziehungen sind bedingt unabhängig gegeben den Karton, aber nicht unabhängig.
:::
:::

:::aufgabe Aufgabe 11 ★★★ Wie gut muss das Gerät sein?
<span class="anker" id="aufg-11"></span>

Beim Prüfgerät aus Unterabschnitt [4.2](#stufe-4-2) bleibe die Basisrate $1\,\%$ und die Erkennung $99\,\%$.

<ol class="al">

<li>

Wie klein muss die Fehlalarmquote $f$ sein, damit $P(D\mid W)\ge\tfrac12$ ist?

</li>

<li>

Zeige allgemein: $P(D\mid W)\ge\tfrac12$ gilt genau dann, wenn $P(W\mid D)\,P(D)\ge P(W\mid D^{\mathrm c})\,P(D^{\mathrm c})$, wenn also die echten Alarme mindestens so häufig sind wie die Fehlalarme.

</li>

<li>

Die Erkennung werde auf $100\,\%$ verbessert, die Fehlalarmquote bleibe $5\,\%$. Wie sehr ändert sich $P(D\mid W)$? Was lehrt das über die beiden Kenngrößen?

</li>

</ol>

:::loesung
(a) $P(D\mid W)=\frac{0{,}0099}{0{,}0099+0{,}99\,f}\ge\tfrac12$ genau dann, wenn $0{,}0099\ge0{,}99\,f$, also $f\le0{,}01$. Die Fehlalarmquote muss auf $1\,\%$ sinken, ein Fünftel des jetzigen Werts.

(b) $P(D\mid W)=\frac{a}{a+b}$ mit $a=P(W\mid D)P(D)$ und $b=P(W\mid D^{\mathrm c})P(D^{\mathrm c})$. Es ist $\frac a{a+b}\ge\tfrac12$ genau dann, wenn $2a\ge a+b$, also $a\ge b$.

(c) Mit $P(W\mid D)=1$ ist $P(D\mid W)=\frac{0{,}01}{0{,}01+0{,}0495}\approx0{,}168$ statt $0{,}167$: fast keine Änderung. Bei kleiner Basisrate bestimmt die Fehlalarmquote, wie aussagekräftig ein Alarm ist; die Erkennungsquote ist schon nahe am Höchstwert und kann den Anteil echter Alarme kaum noch steigern.
:::
:::

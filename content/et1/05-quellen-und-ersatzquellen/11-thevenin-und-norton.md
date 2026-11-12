---
title: Stufe 9: Thevenin und Norton
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Quellen und Ersatzquellen
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen
knoten: Kapitel 5: Quellen und Ersatzquellen
order: 1151100
summary: N soll viele verschiedene Lasten speisen.
tags: Ersatzspannungsquelle, Ersatzstromquelle, Belastungskennlinie
lang: de
---

<span class="anker" id="stufe-9"></span>

:::zweck
N soll viele verschiedene Lasten speisen. Bisher müsste man für jede Last das ganze Netz neu rechnen. Diese Stufe ersetzt das Netz durch eine Gerade, und zwar ein für alle Mal.
:::

**Die Idee.** Man denkt sich die Last durch eine Stromquelle ersetzt, die dem Netz genau den Strom $I_\mathrm{A}$ entzieht. Das Netz merkt keinen Unterschied, es spürt an den Klemmen nur diesen Strom. Jetzt enthält es nur Widerstände und Quellen, Überlagerung ist erlaubt. $U_\mathrm{AB}$ besteht also aus zwei Teilen: dem Anteil der inneren Quellen, der vom Strom nicht abhängt, und dem Anteil von $I_\mathrm{A}$, der ihm proportional ist. Konstante minus Faktor mal Strom ist eine Gerade. Das ist der ganze Grund dafür, dass ein lineares Netz von außen wie eine Gerade aussieht.

:::satz Satz 9.1 (Ersatzquellen: Thevenin und Norton)
<span class="anker" id="satz-9-1"></span>

Jedes lineare Eintor verhält sich an seinen Klemmen wie eine __Ersatzspannungsquelle__ und ebenso wie eine __Ersatzstromquelle__:

<span class="anker" id="gl-9-1"></span>
$$U_\mathrm{AB}=U_\mathrm{i}-R_\mathrm{i}\,I_\mathrm{A},\qquad\qquad I_\mathrm{A}=I_\mathrm{i}-G_\mathrm{i}\,U_\mathrm{AB}, \tag{9.1}$$

mit

<span class="anker" id="gl-9-2"></span>
$$U_\mathrm{i}=U_\mathrm{LL},\qquad I_\mathrm{i}=I_\mathrm{KS},\qquad R_\mathrm{i}=\frac{1}{G_\mathrm{i}}=\frac{U_\mathrm{LL}}{I_\mathrm{KS}}. \tag{9.2}$$
:::

⁠**So liest man das:** Die erste Form heißt nach Thevenin, die zweite nach Norton. $U_\mathrm{LL}$ ist die Spannung an offenen Klemmen, $I_\mathrm{KS}$ der Strom durch die kurzgeschlossenen Klemmen. $R_\mathrm{i}$ ist in beiden Formen derselbe. Die Gerade heißt auch __Belastungskennlinie__. Bei kleinem $R_\mathrm{i}$ wählt man meist die Thevenin-Form, bei großem die Norton-Form (Stufe [6](spannungsquelle-oder-stromquelle.html#stufe-6)). **Gültigkeit:** Das Eintor muss linear sein, die Last nicht. Die Aussage gilt nur für die Klemmen, über Leistungen im Inneren sagt sie nichts (Stufe [6](spannungsquelle-oder-stromquelle.html#stufe-6)).

:::herleitung Die Gerade aus der Überlagerung
Mit der gedachten Stromquelle $I_\mathrm{A}$ an den Klemmen gilt nach [(8.1)](uberlagerung.html#gl-8-1)

$$U_\mathrm{AB}=\underbrace{\sum_k a_kU_{\mathrm{q}k}+\sum_k Z_kI_{\mathrm{q}k}}_{\text{innere Quellen}}\;\underbrace{-\,R_\mathrm{i}I_\mathrm{A}}_{\text{Klemmenstrom}}.$$

Für $I_\mathrm{A}=0$ bleibt der erste Teil stehen, er ist also $U_\mathrm{LL}$. Sind alle inneren Quellen abgeschaltet, bleibt der zweite Teil: Dort ist $R_\mathrm{i}$ der Gesamtwiderstand des abgeschalteten Netzes zwischen A und B. Das Minus kommt vom Zählpfeil: $I_\mathrm{A}$ fließt aus A heraus, im Inneren also von B nach A, dabei liegt A tiefer. Aus $U_\mathrm{AB}=0$ folgt $I_\mathrm{A}=I_\mathrm{KS}=U_\mathrm{LL}/R_\mathrm{i}$. Umstellen ergibt die zweite Form.
:::

**Drei Wege zu den zwei Zahlen.**

<ol>

<li>

⁠**Leerlauf und Kurzschluss:** $U_\mathrm{LL}$ und $I_\mathrm{KS}$ rechnen oder messen, $R_\mathrm{i}$ folgt aus [(9.2)](#gl-9-2).

</li>

<li>

⁠**Quellen abschalten:** Spannungsquellen als Draht, Stromquellen als Lücke, dann den Gesamtwiderstand zwischen A und B bestimmen. Das ist $R_\mathrm{i}$. Dazu eine der beiden Größen $U_\mathrm{LL}$ oder $I_\mathrm{KS}$.

</li>

<li>

⁠**Zwei Lastfälle:** Wenn man nicht kurzschließen darf, misst man mit zwei Lasten die Punkte $(I_\mathrm{x},U_\mathrm{x})$ und $(I_\mathrm{y},U_\mathrm{y})$. Beide liegen auf der Geraden, $U_\mathrm{x}=U_\mathrm{i}-R_\mathrm{i}I_\mathrm{x}$ und $U_\mathrm{y}=U_\mathrm{i}-R_\mathrm{i}I_\mathrm{y}$. Subtrahieren und Einsetzen ergibt

<span class="anker" id="gl-9-3"></span>
$$R_\mathrm{i}=-\frac{U_\mathrm{x}-U_\mathrm{y}}{I_\mathrm{x}-I_\mathrm{y}},\qquad U_\mathrm{i}=U_\mathrm{x}+R_\mathrm{i}I_\mathrm{x}=\frac{U_\mathrm{x}I_\mathrm{y}-U_\mathrm{y}I_\mathrm{x}}{I_\mathrm{y}-I_\mathrm{x}}. \tag{9.3}$$

</li>

</ol>

:::abbildung et1/k5ersatz 10
Links das Netzwerk N, rechts seine zwei Ersatzquellen. An den Klemmen sind alle drei nicht zu unterscheiden.
:::

::::beispiel
Für N ist $U_\mathrm{LL}=9$ V aus Stufe [8](uberlagerung.html#stufe-8) bekannt. Beim Kurzschluss liegt $R_2$ zwischen zwei verbundenen Klemmen und führt keinen Strom. Die Spannungsquelle treibt $U_\mathrm{q1}/R_1=3$ A durch die Klemmen, die Stromquelle 1,5 A: $I_\mathrm{KS}=U_\mathrm{q1}/R_1+I_\mathrm{q2}=4{,}5$ A. Daraus folgt $R_\mathrm{i}=9\,\mathrm{V}/4{,}5\,\mathrm{A}=2\,\Omega$. Der zweite Weg bestätigt das: Abgeschaltet liegen $R_1$ und $R_2$ parallel, $6\,\Omega\parallel3\,\Omega=2\,\Omega$. Die Norton-Form hat $I_\mathrm{i}=4{,}5$ A und $G_\mathrm{i}=0{,}5$ S (Abb. [10](#abb-10)).

Das sind genau die Zahlen der Batterie aus Stufe [5](reale-quellen-und-der-arbeitspunkt.html#stufe-5). Ohne das Netz noch einmal anzusehen, folgt für 16 $\Omega$: $I_\mathrm{A}=9\,\mathrm{V}/18\,\Omega=0{,}5$ A und $U_\mathrm{AB}=8$ V. **Kontrolle** im Original: Durch $R_1$ kommen $(18-8)\,\mathrm{V}/6\,\Omega=1{,}667$ A, dazu 1,5 A, das sind 3,167 A. Davon nimmt $R_2$ mit $8\,\mathrm{V}/3\,\Omega=2{,}667$ A den größten Teil, 0,5 A gehen zur Last. Wäre $I_\mathrm{q2}=0$, bliebe der Spannungsteiler aus Teilbild 1 mit $U_\mathrm{i}=\frac{R_2}{R_1+R_2}U_\mathrm{q1}=6$ V, $I_\mathrm{i}=U_\mathrm{q1}/R_1=3$ A und unverändertem $R_\mathrm{i}=R_1\parallel R_2$.

:::abbildung et1/k5geraden 11
Die Kennlinien von N mit einer Quelle und mit beiden. Jede Quelle schiebt die Gerade parallel nach oben, die Neigung $R_\mathrm{i}=2\,\Omega$ bleibt, denn sie hängt nur an den Widerständen. Die Summe von 6 V und 3 V und die Summe von 3 A und 1,5 A sind die Überlagerung.
:::
::::

::::beispiel [Zweites Beispiel] eine reale Stromquelle
Eine ideale Stromquelle $I_\mathrm{q}=3$ A mit $R_\mathrm{q}=20\,\Omega$ parallel speist über $R_\mathrm{v}=10\,\Omega$ die Klemme A. Ihr anderer Pol ist B, zwischen A und B liegen $R_\mathrm{p}=30\,\Omega$. Im Kurzschluss ist $R_\mathrm{p}$ überbrückt, und der Stromteiler ergibt $I_\mathrm{KS}=I_\mathrm{q}\frac{R_\mathrm{q}}{R_\mathrm{q}+R_\mathrm{v}}=2$ A. Im Leerlauf liegen $R_\mathrm{v}$ und $R_\mathrm{p}$ in Reihe. Sie führen $I_\mathrm{q}\frac{R_\mathrm{q}}{R_\mathrm{q}+R_\mathrm{v}+R_\mathrm{p}}=1$ A, also ist $U_\mathrm{LL}=R_\mathrm{p}\cdot1\,\mathrm{A}=30$ V. Der Quotient ist $R_\mathrm{i}=15\,\Omega$. Abgeschaltet wird die Stromquelle zur Lücke, ihr Parallelwiderstand bleibt: $R_\mathrm{i}=R_\mathrm{p}\parallel(R_\mathrm{q}+R_\mathrm{v})=15\,\Omega$, oder als Leitwert $G_\mathrm{i}=G_\mathrm{p}+\frac{1}{R_\mathrm{q}+R_\mathrm{v}}$.
::::

⁠**Grenzfälle:** Liegt eine ideale Spannungsquelle direkt an den Klemmen, ist $R_\mathrm{i}=0$ und die Norton-Form existiert nicht. Liegt eine ideale Stromquelle in Reihe zu einer Klemme, ist $R_\mathrm{i}=\infty$ und die Thevenin-Form existiert nicht. Heben sich die Quellen genau auf, sind $U_\mathrm{LL}=0$ und $I_\mathrm{KS}=0$. Dann versagt der Quotient, Weg 2 liefert $R_\mathrm{i}$ trotzdem.

:::ltspice Netzwerk und Ersatzquelle nebeneinander
⁠**Zeichnen:** N mit `voltage` 18, `res` 6 und `res` 3, die Stromquelle mit 1.5 von Masse nach `a`. Daneben getrennt die Ersatzquelle mit `voltage` 9 und `res` 2 bis zum Netz `b`. An `a` und an `b` je eine Stromquelle `current` mit dem Wert `{IZ}` nach Masse.

⁠**Direktiven:** `.param IZ=0`, `.step param IZ list 0 0.5 2.25 4.5`, `.op`

⁠**Was du siehst:** `V(a)` und `V(b)` liegen übereinander: 9 V, 8 V, 4,5 V, 0 V. Baue ebenso das Netz aus Aufgabe [11](#aufg-11) auf: Bei `IZ=0` steht dort dein $U_\mathrm{LL}$, und bei deinem $I_\mathrm{KS}$ fällt `V(a)` auf null.
:::

:::frage Ist N jetzt wirklich dasselbe wie die Batterie?
An den Klemmen ja. Jede Last zeigt an beiden denselben Strom und dieselbe Spannung. Im Inneren nein: In N werden im Leerlauf 27 W in $R_2$ und 13,5 W in $R_1$ umgesetzt, die Batterie ruht. Ersatzquellen beantworten Fragen an den Klemmen, sonst keine.
:::

:::aufgabe Aufgabe 10 ★★ Zwei Lastfälle
<span class="anker" id="aufg-10"></span>

An einem unbekannten linearen Gerät misst du mit 10 $\Omega$ an den Klemmen 10 V und 1 A, mit 4 $\Omega$ dann 8 V und 2 A. (a) Bestimme $R_\mathrm{i}$, $U_\mathrm{i}$ und $I_\mathrm{KS}$ mit [(9.3)](#gl-9-3). (b) Sage Strom und Spannung für 1 $\Omega$ voraus.

:::loesung
(a) $R_\mathrm{i}=-\frac{10-8}{1-2}\,\Omega=2\,\Omega$, $U_\mathrm{i}=10\,\mathrm{V}+2\,\Omega\cdot1\,\mathrm{A}=12$ V. Probe mit dem Bruch: $\frac{10\cdot2-8\cdot1}{2-1}\,\mathrm{V}=12$ V. $I_\mathrm{KS}=6$ A.

(b) $I_\mathrm{A}=12\,\mathrm{V}/3\,\Omega=4$ A, $U_\mathrm{AB}=4$ V.
:::
:::

:::aufgabe Aufgabe 11 ★★★ Zwei reale Quellen
<span class="anker" id="aufg-11"></span>

Zwischen B und einem Knoten C liegen 2 $\Omega$ und parallel dazu eine ideale Stromquelle mit 5 A, die von B nach C treibt. Von C führen 3 $\Omega$ zu einem Knoten D. Von D führt eine ideale Spannungsquelle mit 4 V zu Klemme A, ihr Pluspol liegt an D. Zwischen A und B liegen 5 $\Omega$. (a) Berechne $U_\mathrm{LL}$ durch Überlagerung. (b) Berechne $R_\mathrm{i}$ durch Abschalten und daraus $I_\mathrm{KS}$. (c) Grenzfall: Die Spannungsquelle hat 10 V. Was zeigen Leerlauf und Kurzschluss, und wie groß ist $R_\mathrm{i}$ jetzt?

:::loesung
(a) Nur Stromquelle (Spannungsquelle als Draht, offene Klemmen): Die 5 A speisen 2 $\Omega$ parallel zu $3\,\Omega+5\,\Omega$, also $2\,\Omega\parallel8\,\Omega=1{,}6\,\Omega$, an C stehen 8 V gegen B. Der Teiler aus 3 $\Omega$ und 5 $\Omega$ ergibt $U'=8\,\mathrm{V}\cdot\frac58=5$ V.

Nur Spannungsquelle (Stromquelle offen): Sie treibt $4\,\mathrm{V}/10\,\Omega=0{,}4$ A vom Pluspol über 3 $\Omega$ und 2 $\Omega$ nach B und durch die 5 $\Omega$ von B nach A. Also liegt A um 2 V tiefer als B: $U''=-2$ V. Zusammen: $U_\mathrm{LL}=3$ V. Allgemein ist $U_\mathrm{LL}=\frac{I_\mathrm{q2}R_\mathrm{q2}-U_\mathrm{q1}}{R_\mathrm{q1}+R_\mathrm{q2}+R_3}\,R_3$, wenn $R_\mathrm{q1}$ die 3 $\Omega$, $R_\mathrm{q2}$ die 2 $\Omega$ und $R_3$ die 5 $\Omega$ sind.

(b) Abgeschaltet liegen 3 $\Omega$ und 2 $\Omega$ in Reihe und parallel zu 5 $\Omega$: $R_\mathrm{i}=5\,\Omega\parallel5\,\Omega=2{,}5\,\Omega$. Damit $I_\mathrm{KS}=3\,\mathrm{V}/2{,}5\,\Omega=1{,}2$ A. Direkt: Die Stromquelle mit 2 $\Omega$ wirkt wie 10 V mit 2 $\Omega$ (Stufe [6](spannungsquelle-oder-stromquelle.html#stufe-6)). Die 5 $\Omega$ sind kurzgeschlossen, also $I_\mathrm{KS}=(10\,\mathrm{V}-4\,\mathrm{V})/5\,\Omega=1{,}2$ A.

(c) Mit 10 V heben sich beide Anteile auf: $U_\mathrm{LL}=0$ und $I_\mathrm{KS}=0$. Der Quotient ist unbestimmt, $R_\mathrm{i}$ bleibt aber 2,5 $\Omega$, denn er hängt nicht von den Quellen ab. Von außen ist das Netz ein reiner Widerstand.
:::
:::

::::formelsammlung
**Ersatzquellen nach Thevenin und Norton**

$$U_\mathrm{AB}=U_\mathrm{i}-R_\mathrm{i}\,I_\mathrm{A},\qquad\qquad I_\mathrm{A}=I_\mathrm{i}-G_\mathrm{i}\,U_\mathrm{AB}$$

Jedes lineare Eintor verhält sich an seinen Klemmen wie eine Ersatzspannungsquelle (Thevenin) und wie eine Ersatzstromquelle (Norton). Die Gerade heißt Belastungskennlinie. Das Eintor muss linear sein, die Last nicht; die Aussage gilt nur für die Klemmen. Bei kleinem $R_\mathrm{i}$ meist die Thevenin-Form, bei großem die Norton-Form.

**Kennwerte der Ersatzquelle**

$$U_\mathrm{i}=U_\mathrm{LL},\qquad I_\mathrm{i}=I_\mathrm{KS},\qquad R_\mathrm{i}=\frac{1}{G_\mathrm{i}}=\frac{U_\mathrm{LL}}{I_\mathrm{KS}}$$

$U_\mathrm{LL}$ Spannung an offenen Klemmen, $I_\mathrm{KS}$ Strom durch die kurzgeschlossenen Klemmen; $R_\mathrm{i}$ ist in beiden Formen derselbe. $R_\mathrm{i}$ ist auch der Gesamtwiderstand zwischen A und B, wenn man Spannungsquellen durch Drähte und Stromquellen durch Lücken ersetzt; das hilft, wenn sich die Quellen aufheben und $U_\mathrm{LL}=0$ und $I_\mathrm{KS}=0$ sind.

**Zerlegung der Klemmenspannung**

$$U_\mathrm{AB}=\sum_k a_kU_{\mathrm{q}k}+\sum_k Z_kI_{\mathrm{q}k}-R_\mathrm{i}I_\mathrm{A}$$

Die Last ist durch eine gedachte Stromquelle $I_\mathrm{A}$ ersetzt. Der Anteil der inneren Quellen hängt nicht vom Strom ab und ist $U_\mathrm{LL}$; der Anteil des Klemmenstroms ist ihm proportional. Das Minus kommt vom Zählpfeil.

**Zwei Lastfälle**

$$R_\mathrm{i}=-\frac{U_\mathrm{x}-U_\mathrm{y}}{I_\mathrm{x}-I_\mathrm{y}},\qquad U_\mathrm{i}=U_\mathrm{x}+R_\mathrm{i}I_\mathrm{x}=\frac{U_\mathrm{x}I_\mathrm{y}-U_\mathrm{y}I_\mathrm{x}}{I_\mathrm{y}-I_\mathrm{x}}$$

Zwei gemessene Punkte $(I_\mathrm{x},U_\mathrm{x})$ und $(I_\mathrm{y},U_\mathrm{y})$ auf der Geraden, etwa wenn man nicht kurzschließen darf. Folgt aus $U_\mathrm{x}=U_\mathrm{i}-R_\mathrm{i}I_\mathrm{x}$ und $U_\mathrm{y}=U_\mathrm{i}-R_\mathrm{i}I_\mathrm{y}$ durch Subtrahieren und Einsetzen.
::::

::::lernkarten
:::karte zusammenhang Warum ein Netz eine Gerade ist
Warum verhält sich jedes lineare Netz an zwei Klemmen wie eine Gerade im Strom-Spannungs-Diagramm?
---
Man ersetzt die Last gedanklich durch eine Stromquelle $I_\mathrm{A}$; das Netz merkt keinen Unterschied. Nach der Überlagerung besteht $U_\mathrm{AB}$ dann aus einem festen Anteil der inneren Quellen und einem Anteil, der $I_\mathrm{A}$ proportional ist. Konstante minus Faktor mal Strom ist eine Gerade.
--- falsch
Weil alle Widerstände im Netz in Reihe liegen und sich zu einem einzigen addieren lassen. Netze mit Parallelzweigen haben dagegen gekrümmte Kennlinien, weil sich der Strom dort je nach Last anders auf die Zweige aufteilt und die Teilströme deshalb nicht proportional wachsen.
--- falsch
Weil die angeschlossene Last linear ist: Ihre Arbeitsgerade zwingt auch das Netz auf eine Gerade, denn Strom und Spannung an den Klemmen sind für beide gleich. Mit einer Glühlampe als Last ist die Kennlinie des Netzes keine Gerade mehr und muss neu bestimmt werden.
--- falsch
Weil man das Netz nur an zwei Punkten misst und zwei Punkte immer eine Gerade festlegen. In Wahrheit ist die Kennlinie meist gekrümmt, die Gerade ist nur eine Näherung für kleine Ströme.
:::
:::karte begriff Ersatzspannungsquelle und Ersatzstromquelle
Wie sehen die Ersatzspannungsquelle nach Thevenin und die Ersatzstromquelle nach Norton eines linearen Eintors aus?
---
Thevenin: $U_\mathrm{AB}=U_\mathrm{i}-R_\mathrm{i}\,I_\mathrm{A}$, eine ideale Spannungsquelle $U_\mathrm{i}=U_\mathrm{LL}$ in Reihe mit $R_\mathrm{i}$. Norton: $I_\mathrm{A}=I_\mathrm{i}-G_\mathrm{i}\,U_\mathrm{AB}$, eine ideale Stromquelle $I_\mathrm{i}=I_\mathrm{KS}$ parallel zu $G_\mathrm{i}$. $R_\mathrm{i}$ ist derselbe.
--- falsch
Thevenin: eine ideale Spannungsquelle $U_\mathrm{i}=U_\mathrm{LL}$ parallel zu $R_\mathrm{i}$. Norton: eine ideale Stromquelle $I_\mathrm{i}=I_\mathrm{KS}$ in Reihe mit $G_\mathrm{i}$. $R_\mathrm{i}$ ist in beiden Formen derselbe, nur die Anordnung der Elemente ist vertauscht.
--- falsch
Thevenin: $U_\mathrm{AB}=U_\mathrm{i}+R_\mathrm{i}\,I_\mathrm{A}$ mit $U_\mathrm{i}=U_\mathrm{LL}$. Norton: $I_\mathrm{A}=I_\mathrm{i}+G_\mathrm{i}\,U_\mathrm{AB}$ mit $I_\mathrm{i}=I_\mathrm{KS}$. Die Spannung steigt, je mehr Strom die Last zieht.
--- falsch
Thevenin: $U_\mathrm{AB}=U_\mathrm{i}-R_\mathrm{i}\,I_\mathrm{A}$ mit $U_\mathrm{i}=U_\mathrm{LL}$. Norton: $I_\mathrm{A}=I_\mathrm{i}-G_\mathrm{i}\,U_\mathrm{AB}$ mit $G_\mathrm{i}=R_\mathrm{i}$. Beide Formen gelten auch für die Leistungen im Inneren des Eintors.
:::
:::karte begriff Leerlaufspannung
Was ist die Leerlaufspannung $U_\mathrm{LL}$ eines linearen Eintors, und welche Rolle spielt sie in der Ersatzspannungsquelle?
---
Die Spannung an den offenen Klemmen, $I_\mathrm{A}=0$. Sie ist der Anteil der inneren Quellen, der nicht vom Klemmenstrom abhängt, und die Quellenspannung der Ersatzspannungsquelle: $U_\mathrm{i}=U_\mathrm{LL}$.
--- falsch
Die Spannung an den kurzgeschlossenen Klemmen. Sie ist die Quellenspannung der Ersatzspannungsquelle und deshalb bei jedem Netz ohne äußere Last gleich null, gleich welche Quellen es enthält.
--- falsch
Die Spannung, die bei der angeschlossenen Last an den Klemmen liegt. Sie ändert sich mit der Last und legt deshalb auch den Innenwiderstand der Ersatzspannungsquelle fest.
--- falsch
Die Spannung an den offenen Klemmen. Sie hängt nur von den Widerständen ab, nicht von den Quellen, und ist die Neigung der Geraden, nicht ihre Höhe über der Stromachse.
:::
:::karte formel Innenwiderstand aus Leerlauf und Kurzschluss
Wie hängen die Zahlen der Ersatzquellen mit Leerlauf und Kurzschluss eines linearen Eintors zusammen?
---
$U_\mathrm{i}=U_\mathrm{LL}$, $I_\mathrm{i}=I_\mathrm{KS}$ und $R_\mathrm{i}=\frac{1}{G_\mathrm{i}}=\frac{U_\mathrm{LL}}{I_\mathrm{KS}}$, mit der Spannung an offenen Klemmen und dem Strom durch die kurzgeschlossenen Klemmen. Das Eintor muss linear sein, die Last nicht.
--- falsch
$U_\mathrm{i}=U_\mathrm{LL}$, $I_\mathrm{i}=I_\mathrm{KS}$ und $R_\mathrm{i}=U_\mathrm{LL}\cdot I_\mathrm{KS}$, mit der Spannung an offenen Klemmen und dem Kurzschlussstrom. Das gilt nur, wenn auch die angeschlossene Last linear ist, etwa ein Widerstand.
--- falsch
$U_\mathrm{i}=U_\mathrm{LL}$, $I_\mathrm{i}=I_\mathrm{KS}$ und $R_\mathrm{i}=\frac{I_\mathrm{KS}}{U_\mathrm{LL}}$, mit der Spannung an offenen Klemmen und dem Kurzschlussstrom. Das Eintor muss linear sein, die Last nicht.
--- falsch
$U_\mathrm{i}$ ist die Spannung bei angeschlossener Last, $I_\mathrm{i}$ der Laststrom und $R_\mathrm{i}=\frac{U_\mathrm{LL}}{I_\mathrm{KS}}$. Diese Werte gelten nur für die Last, an der man gemessen hat.
:::
:::karte begriff Ersatzquelle
Was bedeutet es, dass ein lineares Netzwerk an seinen Klemmen durch eine Ersatzquelle ersetzt werden kann, und worüber sagt sie nichts aus?
---
Das Netzwerk verhält sich an den Klemmen für jede Last wie eine Quelle mit Innenwiderstand. Über das Innere sagt die Ersatzquelle nichts: In N werden im Leerlauf 27 W in $R_2$ und 13,5 W in $R_1$ umgesetzt, die Batterie ruht.
--- falsch
Das Netzwerk ist innen genauso aufgebaut wie die Ersatzquelle. Deshalb stimmen auch die Leistungen in seinen Widerständen mit denen der Ersatzquelle überein; nur über die Last sagt sie nichts aus.
--- falsch
Das Netzwerk verhält sich wie eine Quelle mit Innenwiderstand, aber nur bei der Last, für die man gerechnet hat. Über andere Lasten sagt die Ersatzquelle nichts; für jede neue Last braucht man eine neue Ersatzquelle mit anderen Zahlen.
--- falsch
Das Netzwerk verhält sich wie eine ideale Quelle ohne Innenwiderstand, weil die Quellen die Widerstände im Netz überbrücken. Über die Widerstände im Netz sagt die Ersatzquelle deshalb nichts aus.
:::
:::karte begriff Belastungskennlinie
Was nennt man die Belastungskennlinie eines linearen Eintors, und wo schneidet sie die Achsen?
---
Die Gerade $U_\mathrm{AB}=U_\mathrm{i}-R_\mathrm{i}\,I_\mathrm{A}$ an seinen Klemmen. Sie schneidet die Spannungsachse bei $U_\mathrm{LL}$ und die Stromachse bei $I_\mathrm{KS}$, ihre Neigung ist $R_\mathrm{i}$.
--- falsch
Die Gerade $U_\mathrm{AB}=R_\mathrm{L}I_\mathrm{A}$ der angeschlossenen Last durch den Ursprung. Sie schneidet keine Achse außer im Ursprung, ihre Neigung ist $R_\mathrm{L}$.
--- falsch
Die Kurve der Leistung, die das Eintor bei wachsender Belastung abgibt. Sie schneidet die Stromachse bei $I_\mathrm{KS}$, wo die abgegebene Leistung am größten ist.
--- falsch
Die Gerade $U_\mathrm{AB}=U_\mathrm{i}-R_\mathrm{i}\,I_\mathrm{A}$. Sie schneidet die Stromachse bei $U_\mathrm{LL}$ und die Spannungsachse bei $I_\mathrm{KS}$, ihre Neigung ist $G_\mathrm{i}$.
:::
:::karte herleitung Die Gerade aus der Überlagerung
Leite mit der Überlagerung her, dass ein lineares Eintor an seinen Klemmen die Kennlinie $U_\mathrm{AB}=U_\mathrm{LL}-R_\mathrm{i}\,I_\mathrm{A}$ hat.
---
Man ersetzt die Last durch eine gedachte Stromquelle $I_\mathrm{A}$, weil das Netz an den Klemmen nur diesen Strom spürt; jetzt enthält es nur Widerstände und Quellen.
---
Nach der Superposition gilt $U_\mathrm{AB}=\sum_k a_kU_{\mathrm{q}k}+\sum_k Z_kI_{\mathrm{q}k}-R_\mathrm{i}I_\mathrm{A}$, weil auch $I_\mathrm{A}$ eine Quelle ist, deren Beitrag ihr proportional ist.
---
Für $I_\mathrm{A}=0$ bleibt der Anteil der inneren Quellen stehen, er ist also $U_\mathrm{LL}$, weil offene Klemmen den Leerlauf bedeuten.
---
Sind alle inneren Quellen abgeschaltet, bleibt $-R_\mathrm{i}I_\mathrm{A}$, und $R_\mathrm{i}$ ist der Gesamtwiderstand des abgeschalteten Netzes zwischen A und B; das Minus steht da, weil $I_\mathrm{A}$ im Inneren von B nach A fließt und A dabei tiefer liegt.
---
Aus $U_\mathrm{AB}=0$ folgt $I_\mathrm{A}=I_\mathrm{KS}=U_\mathrm{LL}/R_\mathrm{i}$, weil der Kurzschluss die Klemmenspannung null erzwingt; Umstellen ergibt die Norton-Form.
:::
:::karte zusammenhang Innenwiderstand durch Abschalten
Wie bestimmt man den Innenwiderstand $R_\mathrm{i}$ eines linearen Eintors, indem man seine inneren Quellen abschaltet, und warum geht das?
---
Man ersetzt Spannungsquellen durch Drähte und Stromquellen durch Lücken und bestimmt den Gesamtwiderstand zwischen A und B. Das geht, weil $R_\mathrm{i}$ nur von den Widerständen abhängt, nicht von den Quellen.
--- falsch
Man ersetzt Spannungsquellen durch Lücken und Stromquellen durch Drähte und bestimmt den Gesamtwiderstand. Die Art des Ersatzes ist beliebig, weil die abgeschalteten Quellen ohnehin den Wert null haben.
--- falsch
Man entfernt alle Quellen samt ihren Innenwiderständen und addiert die übrigen Widerstände. $R_\mathrm{i}$ ist deren Summe, gleich wie sie verschaltet sind, weil ohne Quellen alle in Reihe liegen.
--- falsch
Man schaltet die Quellen ab und misst dann die Leerlaufspannung. Diese ist zahlenmäßig gleich $R_\mathrm{i}$, weil ohne Quellen kein Strom mehr fließt und nur der Widerstand übrig bleibt.
:::
:::karte formel Zwei Lastfälle
Wie bestimmt man $R_\mathrm{i}$ und $U_\mathrm{i}$ aus zwei Lastfällen $(I_\mathrm{x},U_\mathrm{x})$ und $(I_\mathrm{y},U_\mathrm{y})$, wenn man ein Gerät nicht kurzschließen darf?
---
$R_\mathrm{i}=-\frac{U_\mathrm{x}-U_\mathrm{y}}{I_\mathrm{x}-I_\mathrm{y}}$ und $U_\mathrm{i}=U_\mathrm{x}+R_\mathrm{i}I_\mathrm{x}$: Beide Punkte liegen auf der Geraden; Subtrahieren liefert die Neigung, Einsetzen die Höhe.
--- falsch
$R_\mathrm{i}=\frac{U_\mathrm{x}-U_\mathrm{y}}{I_\mathrm{x}-I_\mathrm{y}}$ und $U_\mathrm{i}=U_\mathrm{x}-R_\mathrm{i}I_\mathrm{x}$, weil die Steigung der Geraden direkt der Innenwiderstand ist, ohne Vorzeichenwechsel.
--- falsch
$R_\mathrm{i}=\frac{U_\mathrm{x}}{I_\mathrm{x}}$ und $U_\mathrm{i}=U_\mathrm{y}$: Der erste Lastfall liefert den Innenwiderstand, der zweite die Spannung, sofern die zweite Last groß genug ist, um fast den Leerlauf zu erreichen.
--- falsch
$R_\mathrm{i}=-\frac{U_\mathrm{x}-U_\mathrm{y}}{I_\mathrm{x}-I_\mathrm{y}}$, aber $U_\mathrm{i}$ lässt sich aus zwei Lastfällen nicht bestimmen; dafür braucht man immer die Messung im Leerlauf.
:::
:::karte formel Ersatzquelle von N
Welche Ersatzquelle hat das Netzwerk N mit $U_\mathrm{q1}=18$ V, $R_1=6\,\Omega$, $R_2=3\,\Omega$ und $I_\mathrm{q2}=1{,}5$ A, und wie findet man sie?
---
$U_\mathrm{LL}=9$ V aus der Überlagerung. Im Kurzschluss ist $R_2$ stromlos, $I_\mathrm{KS}=U_\mathrm{q1}/R_1+I_\mathrm{q2}=4{,}5$ A. Also $R_\mathrm{i}=2\,\Omega$, bestätigt durch $6\,\Omega\parallel3\,\Omega=2\,\Omega$: genau die Zahlen der Batterie.
--- falsch
$U_\mathrm{LL}=9$ V und $I_\mathrm{KS}=3$ A, weil im Kurzschluss nur die Spannungsquelle Strom durch die Klemmen treibt und die Stromquelle kurzgeschlossen ist. Also $R_\mathrm{i}=3\,\Omega$, gleich $R_2$.
--- falsch
$U_\mathrm{LL}=18$ V, die Spannung der Quelle, und $I_\mathrm{KS}=4{,}5$ A. Also $R_\mathrm{i}=4\,\Omega$, doppelt so viel wie bei der Batterie, mit der N deshalb nicht austauschbar ist.
--- falsch
$R_\mathrm{i}=9\,\Omega$, weil $R_1$ und $R_2$ abgeschaltet in Reihe liegen. Mit $U_\mathrm{LL}=9$ V folgt $I_\mathrm{KS}=1$ A, also weniger als die Stromquelle allein liefert.
:::
:::karte zusammenhang Grenzfälle der Ersatzquellen
Wann existiert die Norton-Form oder die Thevenin-Form eines Eintors nicht, und was hilft, wenn sich die inneren Quellen genau aufheben?
---
Liegt eine ideale Spannungsquelle direkt an den Klemmen, ist $R_\mathrm{i}=0$: keine Norton-Form. Liegt eine ideale Stromquelle in Reihe zu einer Klemme, ist $R_\mathrm{i}=\infty$: keine Thevenin-Form. Heben sich die Quellen auf, versagt der Quotient, das Abschalten liefert $R_\mathrm{i}$.
--- falsch
Liegt eine ideale Spannungsquelle direkt an den Klemmen, ist $R_\mathrm{i}=\infty$, und die Thevenin-Form fehlt; liegt eine ideale Stromquelle in Reihe, ist $R_\mathrm{i}=0$, und die Norton-Form fehlt. Heben sich die Quellen auf, ist $R_\mathrm{i}=0$, weil dann im ganzen Netz kein Strom mehr fließt.
--- falsch
Beide Formen existieren bei jedem linearen Eintor, gleich wie die Quellen angeordnet sind. Heben sich die Quellen genau auf, ist auch $R_\mathrm{i}=0$, weil dann kein Strom mehr fließt, und das Netz wirkt von außen wie ein Draht.
--- falsch
Liegt eine ideale Spannungsquelle direkt an den Klemmen, fehlt die Norton-Form. Heben sich die Quellen genau auf, ist $R_\mathrm{i}$ unbestimmt, und das Netz lässt sich nicht mehr als Gerade beschreiben.
:::
:::karte zusammenhang Quellen verschieben die Gerade
Was ändert jede einzelne Quelle in N an der Kennlinie des Netzes, und was bleibt dabei gleich?
---
Jede Quelle schiebt die Gerade parallel nach oben; die Neigung $R_\mathrm{i}=2\,\Omega$ bleibt, weil sie nur an den Widerständen hängt. 6 V plus 3 V und 3 A plus 1,5 A sind die Überlagerung.
--- falsch
Jede Quelle macht die Gerade steiler; mit beiden Quellen hat sie die doppelte Neigung, weil sich die Innenwiderstände der beiden Quellen dabei addieren.
--- falsch
Jede Quelle dreht die Gerade um ihren Schnittpunkt mit der Stromachse; der Kurzschlussstrom bleibt dabei gleich, nur die Leerlaufspannung wächst mit jeder weiteren Quelle im Netz an.
--- falsch
Jede Quelle schiebt die Gerade nach oben und verringert dabei ihre Neigung; mit beiden Quellen ist $R_\mathrm{i}$ nur noch 1 $\Omega$, halb so viel wie mit einer Quelle.
:::
::::

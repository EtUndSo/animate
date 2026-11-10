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

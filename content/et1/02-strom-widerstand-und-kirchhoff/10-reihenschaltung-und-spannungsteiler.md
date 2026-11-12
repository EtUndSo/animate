---
title: Stufe 9: Reihenschaltung und Spannungsteiler
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Strom, Widerstand und Kirchhoff
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff
knoten: Kapitel 2: Strom, Widerstand und Kirchhoff
order: 1121000
summary: Viele Netze setzen sich aus zwei Grundmustern zusammen.
tags: Reihenschaltung, Gesamtwiderstand, unbelastet, Digital-Analog-Wandler, Bit, Puffer, Komparator, Decoder
lang: de
---

<span class="anker" id="stufe-9"></span>

:::zweck
Viele Netze setzen sich aus zwei Grundmustern zusammen. Diese Stufe fasst hintereinanderliegende Widerstände zusammen, zeigt, wie sich die Spannung aufteilt, und baut daraus einen Wandler.
:::

**Die Idee.** Zwischen den Widerständen zweigt nichts ab, die Knotenregel erzwingt in allen denselben Strom. Der Mittelpunkt stellt sich auf das Potenzial ein, bei dem das gilt. Derselbe Strom braucht in einem größeren Widerstand mehr Antrieb: Das Feld verrichtet dort mehr Arbeit je Ladung, an ihm fällt mehr Spannung ab.

:::satz Satz 9.1 (Reihenschaltung und Spannungsteiler)
<span class="anker" id="satz-9-1"></span>

Für $N$ Widerstände in __Reihenschaltung__ gilt

<span class="anker" id="gl-9-1"></span>
<span class="anker" id="gl-9-2"></span>
$$\begin{aligned} I&=I_1=I_2=\dots=I_N,\qquad U=U_1+U_2+\dots+U_N,\qquad U_i=R_i\,I,\\ R_\mathrm{ges}&=\sum_{i=1}^{N}R_i,\qquad\frac{U_\nu}{U}=\frac{R_\nu}{\sum_{i=1}^NR_i}, \end{aligned} \tag{9.1|9.2}$$

für zwei Widerstände also die Spannungsteilerregel

<span class="anker" id="gl-9-3"></span>
$$\frac{U_2}{U}=\frac{R_2}{R_1+R_2},\qquad\frac{U_1}{U_2}=\frac{R_1}{R_2}. \tag{9.3}$$
:::

⁠**So liest man das:** $R_\mathrm{ges}$ ist der __Gesamtwiderstand__, der eine Widerstand, der die Kette ersetzt. Die Spannungen verhalten sich wie die Widerstände. **Gültigkeit:** Die Teilerregel gilt nur __unbelastet__: Am Abgriff darf kein Strom entnommen werden, sonst ist $I_1\neq I_2$ (Stufe [10](parallelschaltung-stromteiler-und-belastung.html#stufe-10)).

:::herleitung Gesamtwiderstand und Teilerregel
Die Maschenregel gibt $U=\sum U_i$, das ohmsche Gesetz $U_i=R_i\,I$ mit demselben $I$. Also $U=(R_1+\dots+R_N)\,I$. Der Quotient aus $U_\nu=R_\nu\,I$ und $U$ kürzt $I$ heraus.
:::

::::beispiel
Die Kette hat $R_\mathrm{ges}=3\,\mathrm{k\Omega}$, also $I=3$ mA, $U_1=6$ V und $U_2=3$ V (Abb. [10](#abb-10) links). Aus [(9.3)](#gl-9-3): $U_2=9\,\mathrm{V}\cdot1/3=3$ V.
::::

⁠**Grenzfälle:** $R_2\to0$ ergibt $U_2\to0$, ein Kurzschluss trägt keine Spannung. $R_2\to\infty$ ergibt $U_2\to U$, eine offene Stelle trägt die ganze Spannung. $R_1=R_2$ halbiert $U$.

:::abbildung et1/k2teiler 10
Links: der Spannungsteiler des Rechenmodells. Mitte: Kette eines 3-Bit-Wandlers an $U_\mathrm{ref}=3{,}2$ V. Die Enden $R/2$ verschieben alle Abgriffe um eine halbe Stufe. Rechts: Ausgang über der Zahl $Z$. Die Treppe liegt mittig um die gestrichelte ideale Gerade, der Fehler ist höchstens eine halbe Stufe.
:::

**Anwendung: Digital-Analog-Wandler.** Ein __Digital-Analog-Wandler__ (D/A-Wandler) macht aus einer Zahl eine Spannung. Drei __Bit__ (Binärstellen $b_0$, $b_1$, $b_2$) ergeben die Zahlen $Z=0$ bis 7. Eine Kette aus $R/2$, sieben $R$ und $R/2$ hat den Gesamtwiderstand $8R$ und teilt $U_\mathrm{ref}$ in acht Stufen. An den Abgriffen liegt

<span class="anker" id="gl-9-4"></span>
$$U_Z=\Bigl(Z+\frac12\Bigr)\frac{U_\mathrm{ref}}{8}. \tag{9.4}$$

Ein Baum aus Schaltern, je Bit eine Ebene, lässt genau einen Abgriff durch. Ein __Puffer__, ein Verstärker mit dem Faktor 1, gibt die Spannung aus, ohne der Kette Strom zu entnehmen, damit der Teiler unbelastet bleibt. Mit $U_\mathrm{ref}=3{,}2$ V ist die Stufe 0,4 V, und $Z=5$ ergibt 2,2 V.

**Anwendung: Flash-Analog-Digital-Wandler.** Dieselbe Kette arbeitet auch umgekehrt. Ein __Komparator__, ein Baustein, der meldet, welche von zwei Spannungen höher ist, vergleicht die Eingangsspannung mit jedem Abgriff, alle gleichzeitig. Ein __Decoder__, eine Logikschaltung, macht aus den Meldungen die Dreibit-Zahl. Für die Zahlen 0 bis 7 genügen sieben Schwellen, hier 0,2 bis 2,6 V. Eine achte Schwelle kann einen Überlauf melden. Bei 1,3 V liegen drei Schwellen darunter, der Wandler gibt $Z=3$ aus, das ist $3\cdot0{,}4\,\mathrm{V}=1{,}2$ V, das nächste Vielfache der Stufe.

:::frage Bremst der erste Widerstand den Strom nicht, sodass im zweiten weniger ankommt?
Nein, Strom wird nicht verbraucht (Stufe [1](strom-ist-bewegte-ladung.html#stufe-1)). Die Elektronen stauen sich nicht vor $R_2$: Sonst würde sich der Mittelpunkt aufladen, bis beide Ströme gleich sind. $R_2$ wirkt auf den ganzen Kreis zurück, denn der eine gemeinsame Strom wird durch $R_1+R_2$ festgelegt.
:::

:::aufgabe Aufgabe 9 ★ Teiler entwerfen
<span class="anker" id="aufg-9"></span>

<ol class="al">

<li>

Aus 12 V sollen 3,3 V entstehen, $R_2=3{,}3\,\mathrm{k\Omega}$. Berechne $R_1$. Welche E24-Werte (8,2 und 9,1 k$\Omega$) liegen daneben, und welche Spannung ergeben sie?

</li>

<li>

Eine Kette aus $1$, $2$, $3$ und $6\,\mathrm{k\Omega}$ liegt an 24 V. Gib Strom und Teilspannungen an.

</li>

<li>

Ein 3-Bit-Wandler hat $U_\mathrm{ref}=5$ V. Welche Spannung gibt er bei $Z=6$ aus?

</li>

</ol>

:::loesung
(a) $R_1=R_2\,(12-3{,}3)/3{,}3=8{,}7\,\mathrm{k\Omega}$. Mit $8{,}2\,\mathrm{k\Omega}$ ergeben sich 3,44 V ($+4{,}3\,\%$), mit $9{,}1\,\mathrm{k\Omega}$ 3,19 V ($-3{,}2\,\%$). (b) $R_\mathrm{ges}=12\,\mathrm{k\Omega}$, $I=2$ mA, Teilspannungen 2, 4, 6 und 12 V. (c) $U_6=6{,}5\cdot5\,\mathrm{V}/8=4{,}06$ V.
:::
:::

::::formelsammlung
**Reihenschaltung**

$$I=I_1=I_2=\dots=I_N,\qquad U=U_1+U_2+\dots+U_N,\qquad U_i=R_i\,I$$

$N$ Widerstände hintereinander, zwischen ihnen zweigt nichts ab.

**Gesamtwiderstand der Reihe**

$$R_\mathrm{ges}=\sum_{i=1}^{N}R_i$$

Der eine Widerstand, der die Kette ersetzt.

**Spannungsteiler, allgemein**

$$\frac{U_\nu}{U}=\frac{R_\nu}{\sum_{i=1}^NR_i}$$

Die Spannungen verhalten sich wie die Widerstände. Gilt nur unbelastet: Am Abgriff wird kein Strom entnommen.

**Spannungsteilerregel**

$$\frac{U_2}{U}=\frac{R_2}{R_1+R_2},\qquad\frac{U_1}{U_2}=\frac{R_1}{R_2}$$

Zwei Widerstände in Reihe, unbelastet. Grenzfälle: $R_2\to0$ ergibt $U_2\to0$, $R_2\to\infty$ ergibt $U_2\to U$, $R_1=R_2$ halbiert $U$.

**Digital-Analog-Wandler mit Widerstandskette**

$$U_Z=\Bigl(Z+\frac12\Bigr)\frac{U_\mathrm{ref}}{8}$$

3-Bit-Wandler, Zahl $Z=0$ bis 7; Kette aus $R/2$, sieben $R$ und $R/2$ mit dem Gesamtwiderstand $8R$. Ein Puffer gibt die Spannung aus, ohne der Kette Strom zu entnehmen.
::::

::::lernkarten
:::karte begriff Reihenschaltung
Was kennzeichnet eine Reihenschaltung von Widerständen?
---
Die Widerstände liegen hintereinander, zwischen ihnen zweigt nichts ab. Durch alle fließt derselbe Strom, $I=I_1=I_2=\dots=I_N$, und die Spannungen addieren sich.
--- falsch
Die Widerstände liegen nebeneinander an denselben zwei Knoten. An allen liegt dieselbe Spannung, und die Ströme addieren sich.
--- falsch
Die Widerstände liegen hintereinander, und jeder bremst den Strom ein Stück weiter. Durch den letzten fließt der kleinste Strom, die Spannungen sind gleich.
--- falsch
Die Widerstände liegen nach ihrem Wert sortiert hintereinander, der größte zuerst. Der Strom teilt sich im Verhältnis ihrer Werte auf.
:::
:::karte formel Gesamtwiderstand
Wie groß ist der Gesamtwiderstand von $N$ Widerständen in Reihe, und was bedeutet er?
---
$R_\mathrm{ges}=\sum_{i=1}^{N}R_i$: der eine Widerstand, der die ganze Kette ersetzt, mit demselben Strom bei derselben Gesamtspannung.
--- falsch
$R_\mathrm{ges}=\Bigl(\sum_{i=1}^N\frac1{R_i}\Bigr)^{-1}$: der eine Widerstand, der die ganze Kette ersetzt; er ist stets kleiner als der kleinste einzelne.
--- falsch
$R_\mathrm{ges}$ ist der größte der Widerstände: Er bestimmt den Strom allein, die kleineren spielen daneben keine Rolle.
--- falsch
$R_\mathrm{ges}=\frac1N\sum_{i=1}^{N}R_i$: der Mittelwert der Widerstände, weil sich der Strom gleichmäßig auf sie verteilt.
:::
:::karte formel Spannungsteilerregel
Welcher Anteil der Gesamtspannung $U$ liegt im unbelasteten Spannungsteiler aus $R_1$ und $R_2$ an $R_2$?
---
$\frac{U_2}{U}=\frac{R_2}{R_1+R_2}$, und $\frac{U_1}{U_2}=\frac{R_1}{R_2}$: Die Spannungen verhalten sich wie die Widerstände.
--- falsch
$\frac{U_2}{U}=\frac{R_1}{R_1+R_2}$, und $\frac{U_1}{U_2}=\frac{R_2}{R_1}$: Am größeren Widerstand liegt die kleinere Spannung.
--- falsch
$\frac{U_2}{U}=\frac{R_2}{R_1}$, und $\frac{U_1}{U_2}=\frac{R_1}{R_2}$: Die Spannungen verhalten sich wie die Widerstände.
--- falsch
$\frac{U_2}{U}=\frac12$, gleich wie groß die Widerstände sind: Die Reihe teilt die Spannung immer in zwei gleiche Teile.
:::
:::karte begriff unbelastet
Wann heißt ein Spannungsteiler unbelastet, und warum ist das für die Teilerregel wichtig?
---
Wenn am Abgriff kein Strom entnommen wird. Nur dann fließt durch beide Widerstände derselbe Strom, und die Teilerregel gilt.
--- falsch
Wenn an seinem Eingang keine Quelle angeschlossen ist. Dann fließt kein Strom, und an jedem Widerstand liegt die halbe Spannung.
--- falsch
Wenn beide Widerstände gleich groß sind. Nur dann teilt sich die Spannung im Verhältnis der Widerstände auf.
--- falsch
Wenn er keinen Strom aus der Quelle zieht. Nur dann bleibt die Quellenspannung an seinen Enden voll erhalten.
:::
:::karte herleitung Gesamtwiderstand und Teilerregel
Leite für $N$ Widerstände in Reihe den Gesamtwiderstand $R_\mathrm{ges}=\sum R_i$ und die Teilerregel $U_\nu/U=R_\nu/\sum R_i$ her.
---
Durch alle Widerstände fließt derselbe Strom $I$, weil zwischen ihnen nichts abzweigt und die Knotenregel dann $I_1=I_2$ ergibt.
---
Die Maschenregel gibt $U=\sum U_i$, weil die Teilspannungen zusammen mit der Gesamtspannung einen Umlauf bilden.
---
Mit $U_i=R_i\,I$ folgt $U=(R_1+\dots+R_N)\,I$, also $R_\mathrm{ges}=\sum R_i$, weil derselbe Strom $I$ in jedem Summanden steht.
---
Der Quotient aus $U_\nu=R_\nu\,I$ und $U$ ergibt $U_\nu/U=R_\nu/\sum R_i$, weil sich $I$ herauskürzt.
:::
:::karte zusammenhang Mehr Spannung am größeren Widerstand
Warum fällt in einer Reihenschaltung am größeren Widerstand die größere Spannung ab?
---
Weil derselbe Strom in einem größeren Widerstand mehr Antrieb braucht: Das Feld verrichtet dort mehr Arbeit je Ladung, also ist $U_i=R_i\,I$ größer.
--- falsch
Weil sich vor dem größeren Widerstand die Elektronen stauen. Der Stau erhöht dort die Spannung so lange, bis der Strom wieder ungehindert fließen kann.
--- falsch
Weil durch den größeren Widerstand mehr Strom fließt. Mehr Strom bedeutet nach $U=R\,I$ auch mehr Spannung.
--- falsch
Weil der größere Widerstand näher an der Quelle liegen muss. Dort ist die Spannung noch nicht von den anderen aufgebraucht.
:::
:::karte zusammenhang Kein Stau vor dem zweiten Widerstand
Bremst der erste Widerstand einer Reihe den Strom, sodass im zweiten weniger ankommt?
---
Nein, Strom wird nicht verbraucht. Stauten sich Elektronen vor $R_2$, würde sich der Mittelpunkt aufladen, bis beide Ströme gleich sind.
--- falsch
Ja: Der erste Widerstand nimmt einen Teil des Stroms auf und wandelt ihn in Wärme um. Der zweite Widerstand erhält nur noch den Rest.
--- falsch
Ja, aber nur wenig: Der Unterschied ist so klein wie der Widerstand der Zuleitungen und darf deshalb entfallen.
--- falsch
Nein: Der zweite Widerstand erhält sogar mehr Strom, weil der erste die Elektronen bündelt und dadurch beschleunigt.
:::
:::karte zusammenhang Grenzfälle des Teilers
Was passiert mit der Teilspannung $U_2$, wenn $R_2$ gegen null oder gegen unendlich geht?
---
Für $R_2\to0$ geht $U_2\to0$: Ein Kurzschluss trägt keine Spannung. Für $R_2\to\infty$ geht $U_2\to U$: Eine offene Stelle trägt die ganze Spannung.
--- falsch
Für $R_2\to0$ geht $U_2\to U$: Der Kurzschluss zieht die ganze Spannung an sich. Für $R_2\to\infty$ geht $U_2\to0$: An einer offenen Stelle liegt keine Spannung.
--- falsch
In beiden Fällen geht $U_2\to0$: Ohne Strom durch die offene Stelle und ohne Widerstand im Kurzschluss bleibt keine Spannung übrig.
--- falsch
In beiden Fällen bleibt $U_2=U/2$: Die Reihe teilt die Spannung immer in zwei gleiche Teile, gleich wie groß $R_2$ ist.
:::
:::karte begriff Digital-Analog-Wandler
Was macht ein Digital-Analog-Wandler, und welche Spannung liefert die Widerstandskette eines 3-Bit-Wandlers am Abgriff für die Zahl $Z$?
---
Er macht aus einer Zahl eine Spannung. Eine Kette aus $R/2$, sieben $R$ und $R/2$ teilt $U_\mathrm{ref}$ in acht Stufen: $U_Z=\Bigl(Z+\frac12\Bigr)\frac{U_\mathrm{ref}}{8}$.
--- falsch
Er macht aus einer Spannung eine Zahl. Eine Kette aus acht gleichen $R$ teilt $U_\mathrm{ref}$ in acht Stufen: $U_Z=Z\,U_\mathrm{ref}/8$.
--- falsch
Er macht aus einer Zahl eine Spannung. Eine Kette aus acht gleichen $R$ teilt $U_\mathrm{ref}$ in acht Stufen: $U_Z=Z\,U_\mathrm{ref}/7$.
--- falsch
Er macht aus einer Zahl eine Spannung, indem er $U_\mathrm{ref}$ mit $Z$ multipliziert: $U_Z=Z\,U_\mathrm{ref}$; eine Widerstandskette braucht er dafür nicht.
:::
:::karte begriff Bit
Was ist ein Bit, und wie viele Zahlen lassen sich mit drei Bit darstellen?
---
Eine Binärstelle; drei Bit $b_0$, $b_1$, $b_2$ ergeben die acht Zahlen $Z=0$ bis 7.
--- falsch
Eine Spannungsstufe des Wandlers; drei Bit ergeben drei Stufen, also die Zahlen $Z=0$ bis 2.
--- falsch
Eine Dezimalstelle; drei Bit ergeben die tausend Zahlen $Z=0$ bis 999.
--- falsch
Eine Binärstelle; drei Bit ergeben die sechs Zahlen $Z=0$ bis 5, zwei je Stelle.
:::
:::karte begriff Puffer
Wozu dient der Puffer am Ausgang eines Digital-Analog-Wandlers mit Widerstandskette?
---
Ein Puffer ist ein Verstärker mit dem Faktor 1. Er gibt die Spannung aus, ohne der Kette Strom zu entnehmen, damit der Teiler unbelastet bleibt.
--- falsch
Ein Puffer ist ein Speicher, der die zuletzt ausgegebene Zahl festhält. So bleibt die Ausgangsspannung erhalten, auch wenn die Zahl am Eingang wechselt.
--- falsch
Ein Puffer ist ein Verstärker mit dem Faktor 8. Er hebt die kleinen Stufen der Kette auf die volle Spannung $U_\mathrm{ref}$ an.
--- falsch
Ein Puffer ist ein Widerstand am Ausgang, der den Strom begrenzt. Er schützt die Kette vor einem Kurzschluss am Ausgang.
:::
:::karte begriff Komparator und Decoder
Welche Aufgaben haben Komparator und Decoder in einem Flash-Analog-Digital-Wandler?
---
Ein Komparator meldet, welche von zwei Spannungen höher ist; je einer vergleicht die Eingangsspannung mit einem Abgriff der Kette, alle zugleich. Der Decoder, eine Logikschaltung, macht daraus die Dreibit-Zahl.
--- falsch
Ein Komparator misst die Eingangsspannung genau und gibt ihren Wert als Zahl aus. Der Decoder rechnet diese Zahl in die Spannung des passenden Abgriffs zurück.
--- falsch
Ein Komparator meldet, welche von zwei Spannungen höher ist; ein einziger vergleicht die Eingangsspannung nacheinander mit allen Abgriffen der Kette. Der Decoder, ein Speicher, hält die Meldungen der Reihe nach fest.
--- falsch
Ein Komparator verstärkt die Differenz zweier Spannungen mit dem Faktor 1. Der Decoder teilt die Eingangsspannung wie ein Spannungsteiler in acht Stufen.
:::
::::

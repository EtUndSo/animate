---
title: Stufe 9: Reihenschaltung und Spannungsteiler
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Strom, Widerstand und Kirchhoff
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

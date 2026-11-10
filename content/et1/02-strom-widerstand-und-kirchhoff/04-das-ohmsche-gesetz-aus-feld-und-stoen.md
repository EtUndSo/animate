---
title: Stufe 3: Das ohmsche Gesetz aus Feld und Stößen
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Strom, Widerstand und Kirchhoff
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff
knoten: Kapitel 2: Strom, Widerstand und Kirchhoff
order: 1120400
summary: Stufe 2 hat gezeigt: Die Drift ist dem Feld proportional.
tags: Leitfähigkeit, spezifische Widerstand, Leitwert, linear, homogen, Leistung
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Stufe [2](langsame-elektronen-sofortiger-strom.html#stufe-2) hat gezeigt: Die Drift ist dem Feld proportional. Diese Stufe macht daraus in wenigen Schritten das wichtigste Gesetz der Schaltungstechnik.
:::

**Die Idee.** Mehr Spannung bedeutet stärkeres Feld im Leiter, stärkeres Feld bedeutet schnellere Drift, schnellere Drift bedeutet mehr Strom. Jeder Schritt ist eine Proportionalität, also auch der ganze Weg von $U$ nach $I$. Der Faktor enthält das Material und die Form (Abb. [4](#abb-4)).

:::abbildung et1/k2ohm 4
Links: Leiter mit der Länge $L$ und dem Querschnitt $A$. Das Feld $E$ und die Stromdichte $j$ sind überall gleich. Rechts: Kennlinien im Rechenmodell. $I$ über $U$ ist eine Gerade durch den Ursprung, ihre Steigung ist der Leitwert $G=\Delta I/\Delta U$, der Kehrwert von $R=\Delta U/\Delta I$. Der Punkt gehört zu 9 V an $R_1+R_2=3\,\mathrm{k\Omega}$.
:::

:::satz Satz 3.1 (Ohmsches Gesetz)
<span class="anker" id="satz-3-1"></span>

Für einen Leiter mit der Elektronendichte $n$ gilt

<span class="anker" id="gl-3-1"></span>
<span class="anker" id="gl-3-2"></span>
$$\begin{aligned} \vec j&=\sigma\,\vec E,\qquad\sigma=n\,e\,\mu,\qquad\rho=\frac1\sigma,\\ U&=R\,I,\qquad R=\frac{L}{\sigma\,A}=\rho\,\frac LA,\qquad G=\frac1R=\frac IU. \end{aligned} \tag{3.1|3.2}$$
:::

⁠**So liest man das:** $\sigma$ ist die __Leitfähigkeit__ in S/m, $\rho$ der __spezifische Widerstand__ in $\Omega\,\mathrm m$. Oft steht er in $\Omega\,\mathrm{mm^2/m}$, Kupfer hat dann 0,017. $R$ ist der Widerstand in $\Omega$ (Ohm), $1\,\Omega=1$ V/A: m$\Omega$ im Draht, k$\Omega$ in Schaltungen. Sein Schaltzeichen ist ein Rechteck (Abb. [6](zweipole-und-zahlpfeile.html#abb-6)). $G$ ist der __Leitwert__ in S (Siemens), $1\,\mathrm{S}=1\,\Omega^{-1}$. Die Einheiten tragen die Namen von Georg Simon Ohm und Werner von Siemens. **Gültigkeit:** Der Leiter muss __linear__ sein ($\vec j$ proportional zu $\vec E$) und __homogen__ (überall dasselbe Material). Die Temperatur muss konstant sein (Stufe [4](reale-widerstande-werte-und-temperatur.html#stufe-4)), und es muss $L\gg\sqrt A$ gelten, damit das Feld an den Enden keine Rolle spielt. Die Linearität gilt in Metallen sehr genau: Die Flugzeit $T$ hängt nicht von $E$ ab, weil die Drift mehr als $10^{9}$-mal kleiner ist als die ungeordnete Bewegung.

:::herleitung Vom Feld zum Bauteil
Stromdichte der Elektronen, Stufe [1](strom-ist-bewegte-ladung.html#stufe-1), mit $q=-n\,e$ und [(2.1)](langsame-elektronen-sofortiger-strom.html#gl-2-1):

$$\vec j=q\,\vec v_\mathrm D=(-n\,e)(-\mu\,\vec E)=n\,e\,\mu\,\vec E=\sigma\,\vec E.$$

Das Feld ist gleichmäßig, also $U=E\,L$ ([Kapitel 1](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)). Damit

$$I=j\,A=\sigma\,E\,A=\frac{\sigma\,A}{L}\,U\quad\Longrightarrow\quad U=\frac{L}{\sigma\,A}\,I=R\,I.$$
:::

| Leiter | $\rho$ in $10^{-8}\,\Omega\,\mathrm m$ | $\sigma$ in $10^{6}$ S/m | Leiter | $\rho$ in $10^{-8}\,\Omega\,\mathrm m$ | $\sigma$ in $10^{6}$ S/m |
|---|---|---|---|---|---|
| Silber | 1,6 | 62 | Messing | 7 bis 9 | 14 bis 11 |
| Kupfer | 1,7 | 59 | Eisen | 10 bis 15 | 10 bis 7 |
| Gold | 2,3 | 43 | Platin | 11 | 9 |
| Aluminium | 2,8 | 36 | Konstantan | 50 | 2 |
| Wolfram | 5,5 | 18 | Kohle | 5000 bis 10000 | 0,02 bis 0,01 |

::::beispiel
Der Draht hat $R=\rho\,L/A=34\,\mathrm{m\Omega}$. Bei 3 mA fallen an ihm 0,10 mV ab, das ist $1{,}1\cdot10^{-5}$ der 9 V. Das begründet, warum Schaltpläne Drähte als ideal zeichnen, ohne Spannung längs des Drahts. Dieselbe Rechnung zeigt, warum Widerstände nicht aus Kupfer sind: $2\,\mathrm{k\Omega}$ bräuchten bei $0{,}01\,\mathrm{mm^2}$ Querschnitt 1,2 km Kupfer, aber nur 40 m Konstantan.
::::

⁠**Grenzfälle:** Doppelte Länge halbiert bei gleicher Spannung das Feld und damit den Strom. Doppelter Querschnitt wirkt wie zwei Drähte nebeneinander, der Strom verdoppelt sich. $U=0$ ergibt $I=0$.

**Wohin die Energie geht.** Bei jedem Stoß gibt das Elektron die im Feld gewonnene Bewegungsenergie an das Gitter ab. Das Gitter schwingt stärker, und das ist Wärme. Jedes Coulomb gibt die Energie $U$ in Joule ab, je Sekunde laufen $I$ Coulomb durch. Die __Leistung__, die Energie je Zeit, ist daher $P=U\,I=R\,I^2$. Die Kette setzt $9\,\mathrm{V}\cdot3\,\mathrm{mA}=27$ mW um. [Kapitel 7](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/leistung-anpassung-und-wirkungsgrad/leistung-und-anpassung.html) behandelt die Leistung genauer.

:::frage $R=U/I$ kann man doch immer ausrechnen. Was sagt das ohmsche Gesetz dann noch?
Der Quotient $U/I$ existiert bei jedem Bauteil. Das Gesetz sagt mehr: Er ist *konstant*, unabhängig von $U$. Das ist eine Aussage über das Material und folgt aus der festen Flugzeit. Bei einer Glühlampe gilt sie nicht (Stufe [4](reale-widerstande-werte-und-temperatur.html#stufe-4)).
:::

:::aufgabe Aufgabe 3 ★★ Widerstand aus der Geometrie
<span class="anker" id="aufg-3"></span>

Eine Zuleitung besteht aus Hin- und Rückleiter, je 20 m Kupfer mit $1{,}5\,\mathrm{mm^2}$ Querschnitt.

<ol class="al">

<li>

Berechne ihren Widerstand und die Spannung, die bei 16 A an ihr abfällt.

</li>

<li>

Welchen Querschnitt bräuchte Aluminium für denselben Widerstand?

</li>

<li>

Vorhersage: Ein Draht wird auf die doppelte Länge gezogen, sein Volumen bleibt gleich. Um welchen Faktor ändert sich $R$?

</li>

</ol>

:::loesung
(a) $R=\rho\cdot40\,\mathrm{m}/1{,}5\,\mathrm{mm^2}=0{,}453\,\Omega$. Es fallen $0{,}453\,\Omega\cdot16\,\mathrm{A}=7{,}3$ V ab, 3,2 % von 230 V. (b) $R$ gleich heißt $\rho/A$ gleich: $A_\mathrm{Al}=1{,}5\,\mathrm{mm^2}\cdot2{,}8/1{,}7=2{,}5\,\mathrm{mm^2}$. (c) Volumen $L\,A$ konstant: $L\to2L$ erzwingt $A\to A/2$. Also $R\to4R$.
:::
:::

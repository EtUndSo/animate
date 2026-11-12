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

::::formelsammlung
**Ohmsches Gesetz im Material**

$$\vec j=\sigma\,\vec E,\qquad\sigma=n\,e\,\mu,\qquad\rho=\frac1\sigma$$

$\sigma$ Leitfähigkeit in S/m, $\rho$ spezifischer Widerstand in $\Omega\,\mathrm m$ (oft in $\Omega\,\mathrm{mm^2/m}$). Folgt aus $\vec j=q\,\vec v_\mathrm D$ mit $q=-n\,e$ und $\vec v_\mathrm D=-\mu\,\vec E$.

**Ohmsches Gesetz am Bauteil**

$$U=R\,I$$

$R$ Widerstand in $\Omega$, $1\,\Omega=1$ V/A. Gilt für lineare ($\vec j$ proportional zu $\vec E$) und homogene Leiter bei konstanter Temperatur und $L\gg\sqrt A$; dann ist der Quotient $U/I$ unabhängig von $U$.

**Widerstand aus der Geometrie**

$$R=\frac{L}{\sigma\,A}=\rho\,\frac LA$$

Leiter der Länge $L$ mit dem Querschnitt $A$.

**Leitwert**

$$G=\frac1R=\frac IU$$

Einheit Siemens, $1\,\mathrm{S}=1\,\Omega^{-1}$; in der Kennlinie $I$ über $U$ die Steigung.

**Leistung**

$$P=U\,I=R\,I^2$$

Energie je Zeit, die der Widerstand in Wärme umsetzt: Jedes Coulomb gibt die Energie $U$ ab, je Sekunde laufen $I$ Coulomb durch.
::::

::::lernkarten
:::karte begriff Leitfähigkeit
Was gibt die Leitfähigkeit $\sigma$ eines Materials an, und wie hängt sie mit den freien Elektronen zusammen?
---
Den Faktor zwischen Stromdichte und Feld, $\vec j=\sigma\,\vec E$, in S/m. Für Elektronen ist $\sigma=n\,e\,\mu$: Elektronendichte mal Elementarladung mal Beweglichkeit.
--- falsch
Den Faktor zwischen Strom und Spannung eines Bauteils, $I=\sigma\,U$, in Siemens. Er hängt von Länge und Querschnitt des Bauteils ab, nicht vom Material.
--- falsch
Den Faktor zwischen Stromdichte und Feld, $\vec j=\sigma\,\vec E$, in S/m. Für Elektronen ist $\sigma=n\,e/\mu$: Je beweglicher die Elektronen, desto schlechter leitet das Material.
--- falsch
Den Faktor zwischen Feld und Stromdichte, $\vec E=\sigma\,\vec j$, in $\Omega\,\mathrm m$. Er ist umso größer, je schlechter das Material leitet.
:::
:::karte begriff spezifischer Widerstand
Was gibt der spezifische Widerstand $\rho$ eines Leitermaterials an, und wie folgt daraus der Widerstand eines Drahts?
---
Den Kehrwert der Leitfähigkeit, $\rho=\frac1\sigma$, in $\Omega\,\mathrm m$; eine Materialkonstante. Ein Leiter der Länge $L$ mit dem Querschnitt $A$ hat $R=\rho\,\frac LA$.
--- falsch
Den Kehrwert der Leitfähigkeit, $\rho=\frac1\sigma$, in $\Omega\,\mathrm m$; eine Materialkonstante. Ein Leiter der Länge $L$ mit dem Querschnitt $A$ hat $R=\rho\,\frac AL$.
--- falsch
Den Widerstand eines Drahts von genau einem Meter Länge, in $\Omega$. Er hängt nicht vom Querschnitt ab; ein Draht der Länge $L$ hat $R=\rho\,L$.
--- falsch
Das Produkt aus Leitfähigkeit und Widerstand, $\rho=\sigma\,R$, in $\Omega\,\mathrm m$. Er hängt von der Form des Leiters ab, nicht von seinem Material.
:::
:::karte begriff Leitwert
Was gibt der Leitwert $G$ eines Bauteils an, und in welcher Einheit misst man ihn?
---
Den Kehrwert des Widerstands, $G=\frac1R=\frac IU$, in Siemens, $1\,\mathrm{S}=1\,\Omega^{-1}$. In der Kennlinie $I$ über $U$ ist er die Steigung.
--- falsch
Den Kehrwert des Widerstands, $G=\frac UI$, in Siemens, $1\,\mathrm{S}=1\,\Omega$. In der Kennlinie $I$ über $U$ ist er die Fläche unter der Geraden.
--- falsch
Die Leitfähigkeit des Materials, in S/m, unabhängig von der Form. Zwei Drähte aus demselben Kupfer haben deshalb immer denselben Leitwert.
--- falsch
Den Strom, den ein Bauteil bei 1 V führt, in Ampere. Er ändert sich mit der angelegten Spannung, weil der Strom mit ihr wächst.
:::
:::karte begriff linear und homogen
Was bedeuten die Bedingungen linear und homogen, unter denen das ohmsche Gesetz für einen Leiter gilt?
---
Linear heißt: $\vec j$ ist proportional zu $\vec E$. Homogen heißt: Der Leiter besteht überall aus demselben Material.
--- falsch
Linear heißt: Der Leiter ist gerade und nicht gebogen. Homogen heißt: Er hat überall denselben Querschnitt.
--- falsch
Linear heißt: Der Strom wächst mit der Zeit gleichmäßig an. Homogen heißt: Das Feld im Leiter ist überall null.
--- falsch
Linear heißt: $\vec j$ ist proportional zu $\vec E^2$. Homogen heißt: Die Temperatur ist überall gleich, das Material darf wechseln.
:::
:::karte begriff Leistung
Was gibt die elektrische Leistung an einem Widerstand an, und wie berechnet man sie?
---
Die Energie je Zeit, die das Bauteil umsetzt: $P=U\,I=R\,I^2$, in Watt. Jedes Coulomb gibt die Energie $U$ ab, je Sekunde laufen $I$ Coulomb durch.
--- falsch
Die Energie je Zeit, die das Bauteil umsetzt: $P=U/I$, in Watt. Sie ist deshalb gleich dem Widerstand und hängt nicht vom Strom ab.
--- falsch
Die gesamte Energie, die das Bauteil seit dem Einschalten aufgenommen hat: $P=U\,I\,t$, in Watt. Sie wächst mit der Zeit an.
--- falsch
Die Energie je Zeit, die das Bauteil umsetzt: $P=U\,I=R\,I$, in Watt. Jedes Coulomb gibt die Energie $R$ ab, je Sekunde laufen $I$ Coulomb durch das Bauteil.
:::
:::karte formel Ohmsches Gesetz
Wie hängen Spannung und Strom an einem Leiter der Länge $L$ mit dem Querschnitt $A$ zusammen, und wann gilt das?
---
$U=R\,I$ mit $R=\frac{L}{\sigma\,A}=\rho\,\frac LA$. Gültig für lineare, homogene Leiter bei konstanter Temperatur und $L\gg\sqrt A$.
--- falsch
$U=R\,I$ mit $R=\frac{\sigma\,A}{L}$. Gültig für jedes Material und jede Temperatur, weil der Quotient $U/I$ bei jedem Bauteil existiert.
--- falsch
$U=R\,I^2$ mit $R=\rho\,\frac LA$. Gültig für lineare, homogene Leiter bei konstanter Temperatur und $L\gg\sqrt A$.
--- falsch
$I=R\,U$ mit $R=\rho\,\frac LA$. Gültig für lineare, homogene Leiter bei konstanter Temperatur und $L\gg\sqrt A$.
:::
:::karte herleitung Vom Feld zum Bauteil
Leite aus der Drift $\vec v_\mathrm D=-\mu\,\vec E$ her, dass für einen Leiter der Länge $L$ mit dem Querschnitt $A$ das ohmsche Gesetz $U=R\,I$ mit $R=\frac{L}{\sigma\,A}$ gilt.
---
Die Stromdichte der Elektronen ist $\vec j=q\,\vec v_\mathrm D$ mit $q=-n\,e$, weil die Elektronen negativ geladen sind.
---
Einsetzen ergibt $\vec j=(-n\,e)(-\mu\,\vec E)=n\,e\,\mu\,\vec E=\sigma\,\vec E$, weil sich die beiden Minuszeichen aufheben.
---
Das Feld ist im Leiter gleichmäßig, also $U=E\,L$, weil die Spannung im homogenen Feld Feldstärke mal Weg ist.
---
Damit ist $I=j\,A=\sigma\,E\,A=\frac{\sigma\,A}{L}\,U$, weil der Strom die Stromdichte mal Querschnitt ist. Umgestellt: $U=\frac{L}{\sigma\,A}\,I=R\,I$.
:::
:::karte zusammenhang Strom proportional zur Spannung
Warum folgt aus dem Stoßmodell, dass der Strom durch einen Metalldraht proportional zur Spannung ist?
---
Weil jeder Schritt proportional ist: Mehr Spannung gibt ein stärkeres Feld im Leiter, das stärkere Feld eine schnellere Drift, die schnellere Drift mehr Strom.
--- falsch
Weil mehr Spannung mehr freie Elektronen im Leiter erzeugt. Die Drift bleibt gleich, aber es laufen entsprechend mehr Ladungsträger mit.
--- falsch
Weil mehr Spannung die Stöße seltener macht. Die Flugzeit wächst proportional zum Feld, und die Elektronen werden zwischen den Stößen entsprechend schneller.
--- falsch
Weil die Elektronen bei mehr Spannung länger beschleunigt werden. Ihre Geschwindigkeit wächst so lange, bis die Spannung abgeschaltet wird.
:::
:::karte zusammenhang Aussage des ohmschen Gesetzes
Den Quotienten $U/I$ kann man an jedem Bauteil ausrechnen. Was sagt das ohmsche Gesetz darüber hinaus aus?
---
Dass dieser Quotient konstant ist, unabhängig von $U$. Das ist eine Aussage über das Material und folgt aus der festen Flugzeit; bei einer Glühlampe gilt sie nicht.
--- falsch
Dass dieser Quotient für alle Bauteile gleich ist, unabhängig vom Material. Das folgt aus der Ladungserhaltung und gilt deshalb auch für Glühlampen und alle anderen Bauteile.
--- falsch
Dass dieser Quotient mit der Spannung wächst. Das folgt aus den häufigeren Stößen bei stärkerem Feld und gilt für alle Metalle.
--- falsch
Nichts weiter: Das ohmsche Gesetz ist nur die Definition $R=U/I$. Es gilt deshalb bei jedem Bauteil, auch bei der Glühlampe.
:::
:::karte zusammenhang Feste Flugzeit
Warum hängt die Flugzeit $T$ zwischen zwei Stößen in einem Metall nicht vom Feld ab?
---
Weil die Drift mehr als $10^{9}$-mal kleiner ist als die ungeordnete Bewegung: Das Feld ändert die Geschwindigkeit der Elektronen und damit die Zeit bis zum nächsten Stoß praktisch nicht.
--- falsch
Weil die Elektronen im Metall gar nicht stoßen. Ihre Flugzeit ist unbegrenzt lang und deshalb von jedem Feld unabhängig.
--- falsch
Weil das Feld im Draht genau null ist. Ohne Feld gibt es keinen Einfluss auf die Flugzeit; die Drift entsteht allein durch die Quelle.
--- falsch
Weil die Drift viel schneller ist als die ungeordnete Bewegung. Die Elektronen fliegen deshalb geradlinig durch das Gitter und stoßen nur an den Enden des Drahts, gleich wie stark das Feld ist.
:::
:::karte zusammenhang Wärme im Widerstand
Warum erwärmt sich ein Widerstand, durch den Strom fließt?
---
Weil jedes Elektron bei jedem Stoß die im Feld gewonnene Bewegungsenergie an das Gitter abgibt. Das Gitter schwingt stärker, und das ist Wärme.
--- falsch
Weil die Elektronen aneinander reiben, wenn sie sich durch den engen Querschnitt drängen. Die Reibung der Elektronen untereinander erzeugt die Wärme im Bauteil.
--- falsch
Weil sich im Widerstand Ladung ansammelt. Die gestaute Ladung erhitzt das Material so lange, bis sie wieder abfließt.
--- falsch
Weil die Elektronen im Widerstand verbraucht werden. Ihre Masse wird dabei in Wärme umgewandelt, und es fließen weniger heraus.
:::
:::karte zusammenhang Ideale Drähte
Warum dürfen Schaltpläne Drähte als ideal zeichnen, ohne Spannung längs des Drahts?
---
Weil ein Draht einen winzigen Widerstand hat: Ein Meter Kupfer mit $0{,}5\,\mathrm{mm^2}$ hat $34\,\mathrm{m\Omega}$, bei 3 mA fallen nur 0,10 mV ab, rund $10^{-5}$ von 9 V.
--- falsch
Weil im Draht kein Strom fließt, sondern nur ein Feld läuft. Ohne Strom fällt nach $U=R\,I$ längs des Drahts keine Spannung ab.
--- falsch
Weil Kupfer keinen Widerstand hat: Die Elektronen stoßen im Kupfer nicht an das Gitter und verlieren deshalb keine Energie.
--- falsch
Weil die Spannung längs des Drahts zwar groß ist, sich aber auf Hin- und Rückleiter genau aufhebt. In der Summe der beiden bleibt deshalb nichts übrig.
:::
::::

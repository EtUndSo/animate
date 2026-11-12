---
title: Stufe 3: Impedanzform und Leerlaufversuch
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Zweitore
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore
knoten: Kapitel 6: Zweitore
order: 1160500
summary: Die erste Wahl: Die Ströme sind die Ursachen.
tags: Z-Parameter, Eingangsleerlaufwiderstand, Ausgangsleerlaufwiderstand, Leerlaufübertragungswiderstand, Zweipolgrößen, Transfergrößen, Impedanz
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Die erste Wahl: Die Ströme sind die Ursachen. Diese Stufe zeigt, warum ein offenes Tor die vier Zahlen einzeln freilegt.
:::

**Die Idee.** Jede Spannung ist eine Summe aus einem Anteil von $I_1$ und einem Anteil von $I_2$. Um einen Anteil allein zu sehen, muss der andere verschwinden, also sein Strom null sein. Ein Strom ist null, wenn sein Tor offen ist. Bei offenem Tor 2 bleiben in beiden Gleichungen nur die Anteile von $I_1$ übrig. Ein Versuch liefert also zwei Parameter, der Versuch mit vertauschten Toren die anderen zwei.

:::definition Definition 3.1 (Impedanzform, Z-Form)
<span class="anker" id="satz-3-1"></span>

Die Impedanzform, auch Widerstandsform, nimmt die Ströme als Ursachen:

<span class="anker" id="gl-3-1"></span>
$$U_1=Z_{11}I_1+Z_{12}I_2,\quad U_2=Z_{21}I_1+Z_{22}I_2,\qquad\text{kurz}\quad\mathbf U=\mathbf Z\cdot\mathbf I,\quad\mathbf Z=\begin{pmatrix}Z_{11}&Z_{12}\\mathbb{Z}_{21}&Z_{22}\end{pmatrix}. \tag{3.1}$$

Die __Z-Parameter__ folgen aus zwei Leerlaufversuchen:

<span class="anker" id="gl-3-2"></span>
$$Z_{11}=\left.\frac{U_1}{I_1}\right|_{I_2=0},\quad Z_{21}=\left.\frac{U_2}{I_1}\right|_{I_2=0},\quad Z_{12}=\left.\frac{U_1}{I_2}\right|_{I_1=0},\quad Z_{22}=\left.\frac{U_2}{I_2}\right|_{I_1=0}. \tag{3.2}$$
:::

⁠**So liest man das:** $Z_{11}$ ist der __Eingangsleerlaufwiderstand__, $Z_{22}$ der __Ausgangsleerlaufwiderstand__, $Z_{21}$ der __Leerlaufübertragungswiderstand__ vorwärts und $Z_{12}$ der rückwärts. Alle haben die Einheit $\Omega$, typisch sind Ohm bis Megaohm. Parameter mit gleichen Indizes heißen __Zweipolgrößen__: Sie sind der Widerstand eines Klemmenpaars bei festem Abschluss der anderen Seite. Parameter mit verschiedenen Indizes heißen __Transfergrößen__: Sie verknüpfen beide Seiten. Der Buchstabe $Z$ steht für die __Impedanz__. Sie verallgemeinert den Widerstand auf Kondensatoren und Spulen bei Wechselgrößen. Hier sind alle $Z$ reelle Widerstände, für sie gilt $Z_{ii}=R_{ii}$. **Gültigkeit:** Beide Ströme müssen frei wählbar sein (Stufe [6](umrechnen-t-und.html#stufe-6)).

**Ersatzschaltbild.** Die beiden Gleichungen lassen sich zeichnen (Abb. [4](#abb-4) links). Eine Summe von Spannungen ist eine Reihenschaltung. $Z_{11}I_1$ hängt vom eigenen Strom ab, das ist ein Widerstand. $Z_{12}I_2$ hängt vom fremden Strom ab, das ist eine gesteuerte Spannungsquelle (CCVS). Tor 2 ist genauso aufgebaut. In diesem Bild sieht man den Mechanismus des Leerlaufs: Bei $I_2=0$ liefert die Quelle $Z_{12}I_2$ null Volt, und $Z_{22}$ ist stromlos (Abb. [4](#abb-4) rechts). $U_1$ fällt nur an $Z_{11}$ ab, und $U_2$ ist die Quellenspannung $Z_{21}I_1$.

:::abbildung et1/k6zesb 4
Links: Ersatzschaltbild der Z-Form, je ein Widerstand in Reihe mit einer stromgesteuerten Spannungsquelle. Rechts: Leerlaufversuch an Tor 2 mit eingeprägtem Strom $I_\mathrm{q}$. Grau ist, was durch $I_2=0$ wegfällt. Der Versuch mit offenem Tor 1 ist das Spiegelbild und liefert $Z_{12}$ und $Z_{22}$.
:::

::::beispiel
Am T-Zweitor prägt man an Tor 1 den Strom 100 mA ein, Tor 2 bleibt offen. Der Strom läuft durch $R_\mathrm{a}$ und $R_\mathrm{b}$, $U_1=3{,}5$ V. $R_\mathrm{c}$ ist stromlos, an ihm fällt nichts ab, und $U_2$ ist die Spannung an $R_\mathrm{b}$: 2 V. Also $Z_{11}=35\,\Omega$, $Z_{21}=20\,\Omega$. Dasselbe von Tor 2 aus ergibt $U_2=4$ V, $U_1=2$ V, also

$$\mathbf Z=\begin{pmatrix}R_\mathrm{a}+R_\mathrm{b}&R_\mathrm{b}\\mathbb{R}_\mathrm{b}&R_\mathrm{b}+R_\mathrm{c}\end{pmatrix}=\begin{pmatrix}35&20\\20&40\end{pmatrix}\Omega.$$
::::

⁠**Die Brücke.** Die Versuche brauchen keine Masseleitung. Die Brücke in Abb. [2](vom-vierpol-zum-zweitor.html#abb-2) rechts teilt einen Strom an Tor 1 wegen der gleichen Zweigwiderstände je zur Hälfte auf, beide Zweige haben $R_\mathrm{x}+R_\mathrm{y}$. Tor 2 ist offen, und die Spannung zwischen den Zweigmitten ist $\frac{I_1}{2}R_\mathrm{y}-\frac{I_1}{2}R_\mathrm{x}$. Aus Symmetrie gilt dasselbe rückwärts:

<span class="anker" id="gl-3-3"></span>
$$Z_{11}=Z_{22}=(R_\mathrm{x}+R_\mathrm{y})\parallel(R_\mathrm{x}+R_\mathrm{y})=\frac{R_\mathrm{x}+R_\mathrm{y}}{2},\qquad Z_{21}=Z_{12}=\frac{R_\mathrm{y}-R_\mathrm{x}}{2}. \tag{3.3}$$

⁠**Grenzfälle:** Für $R_\mathrm{b}\to0$ sind $Z_{12}=Z_{21}=0$: Der Querzweig ist ein Draht, die Tore sind entkoppelt. Für $R_\mathrm{x}=R_\mathrm{y}$ ist die Brücke abgeglichen ([Kapitel 4](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-und-spannung-messen/strom-und-spannung-messen.html)), und wieder ist $Z_{21}=0$.

:::frage Warum ein Strom und nicht eine Spannung am Eingang? Eine Spannungsquelle habe ich eher zur Hand.
Das geht auch. Es zählt nur, dass das andere Tor offen ist. Dann misst man $U_1$ und $I_1$ und bildet den Quotienten. Der eingeprägte Strom passt nur zur Denkweise der Form: Er ist die Ursache, die Spannungen sind die Wirkungen.
:::

:::aufgabe Aufgabe 3 ★★ Die Brücke als Zweitor
<span class="anker" id="aufg-3"></span>

In der Brücke aus Abb. [2](vom-vierpol-zum-zweitor.html#abb-2) sei $R_\mathrm{x}=30\,\Omega$ und $R_\mathrm{y}=50\,\Omega$.

<ol class="al">

<li>

Bestimme $\mathbf Z$ und daraus eine T-Schaltung mit denselben vier Parametern.

</li>

<li>

Bei 100 mA an Tor 1 und offenem Tor 2: Wie groß sind $U_1$ und $U_2$?

</li>

<li>

Tausche die Werte, $R_\mathrm{x}=50\,\Omega$, $R_\mathrm{y}=30\,\Omega$. Was ändert sich an $\mathbf Z$ und an der T-Schaltung? Was bedeutet das Ergebnis?

</li>

</ol>

:::loesung
(a) Mit [(3.3)](#gl-3-3): $Z_{11}=Z_{22}=40\,\Omega$, $Z_{12}=Z_{21}=10\,\Omega$. T-Schaltung: $R_\mathrm{b}=Z_{12}=10\,\Omega$, $R_\mathrm{a}=R_\mathrm{c}=30\,\Omega$. (b) $U_1=40\,\Omega\cdot100\,\mathrm{mA}=4$ V, $U_2=10\,\Omega\cdot100\,\mathrm{mA}=1$ V. Direkt: je 50 mA durch beide Zweige, $U_2=50\,\mathrm{mA}\cdot(50-30)\,\Omega=1$ V. (c) $Z_{11}$ und $Z_{22}$ bleiben, $Z_{12}=Z_{21}=-10\,\Omega$. Die T-Schaltung hätte $R_\mathrm{b}=-10\,\Omega$ und $R_\mathrm{a}=R_\mathrm{c}=50\,\Omega$. Das negative Element gibt es nicht als Bauteil, das T ist hier nur eine Rechengröße. Es besagt: $U_2$ hat bei gleichem $I_1$ das umgekehrte Vorzeichen.
:::
:::

::::formelsammlung
**Impedanzform (Z-Form)**

$$U_1=Z_{11}I_1+Z_{12}I_2,\quad U_2=Z_{21}I_1+Z_{22}I_2,\qquad\text{kurz}\quad\mathbf U=\mathbf Z\cdot\mathbf I,\quad\mathbf Z=\begin{pmatrix}Z_{11}&Z_{12}\\mathbb{Z}_{21}&Z_{22}\end{pmatrix}$$

Die Ströme sind die Ursachen; auch Widerstandsform. Alle $Z$ in $\Omega$, hier reelle Widerstände, $Z_{ii}=R_{ii}$. Beide Ströme müssen frei wählbar sein.

**Z-Parameter aus Leerlaufversuchen**

$$Z_{11}=\left.\frac{U_1}{I_1}\right|_{I_2=0},\quad Z_{21}=\left.\frac{U_2}{I_1}\right|_{I_2=0},\quad Z_{12}=\left.\frac{U_1}{I_2}\right|_{I_1=0},\quad Z_{22}=\left.\frac{U_2}{I_2}\right|_{I_1=0}$$

Ein offenes Tor setzt seinen Strom null. $Z_{11}$ Eingangsleerlaufwiderstand, $Z_{22}$ Ausgangsleerlaufwiderstand (Zweipolgrößen), $Z_{21}$ Leerlaufübertragungswiderstand vorwärts, $Z_{12}$ rückwärts (Transfergrößen).

**T-Schaltung**

$$\mathbf Z=\begin{pmatrix}R_\mathrm{a}+R_\mathrm{b}&R_\mathrm{b}\\mathbb{R}_\mathrm{b}&R_\mathrm{b}+R_\mathrm{c}\end{pmatrix}$$

Längswiderstand $R_\mathrm{a}$ am Eingang, Querwiderstand $R_\mathrm{b}$, Längswiderstand $R_\mathrm{c}$ am Ausgang. Für $R_\mathrm{b}\to0$ sind $Z_{12}=Z_{21}=0$, die Tore sind entkoppelt.

**Brücke**

$$Z_{11}=Z_{22}=(R_\mathrm{x}+R_\mathrm{y})\parallel(R_\mathrm{x}+R_\mathrm{y})=\frac{R_\mathrm{x}+R_\mathrm{y}}{2},\qquad Z_{21}=Z_{12}=\frac{R_\mathrm{y}-R_\mathrm{x}}{2}$$

Erdsymmetrische Brücke aus zwei Widerstandspaaren $R_\mathrm{x}$, $R_\mathrm{y}$; beide Zweige haben $R_\mathrm{x}+R_\mathrm{y}$, ein Strom an Tor 1 teilt sich je zur Hälfte. Für $R_\mathrm{x}=R_\mathrm{y}$ ist die Brücke abgeglichen und $Z_{21}=0$.
::::

::::lernkarten
:::karte begriff Impedanzform
Was ist die Impedanzform eines Zweitors, und welche Torgrößen sind darin die Ursachen?
---
Die Form der Zweitorgleichungen mit den Strömen als Ursachen: $U_1=Z_{11}I_1+Z_{12}I_2$, $U_2=Z_{21}I_1+Z_{22}I_2$, kurz $\mathbf U=\mathbf Z\cdot\mathbf I$. Sie heißt auch Widerstandsform oder Z-Form.
--- falsch
Die Form mit den Spannungen als Ursachen: $I_1=Z_{11}U_1+Z_{12}U_2$, $I_2=Z_{21}U_1+Z_{22}U_2$, kurz $\mathbf I=\mathbf Z\cdot\mathbf U$. Sie heißt auch Widerstandsform oder Z-Form.
--- falsch
Die Form mit den Strömen als Ursachen: $U_1=Z_{11}I_1+Z_{21}I_2$, $U_2=Z_{12}I_1+Z_{22}I_2$, kurz $\mathbf U=\mathbf Z\cdot\mathbf I$. Die erste Ziffer nennt hier die Ursache.
--- falsch
Die Form mit den Strömen als Ursachen: $U_1=Z_{11}I_1$, $U_2=Z_{22}I_2$, kurz $\mathbf U=\mathbf Z\cdot\mathbf I$. Jede Spannung hängt nur vom Strom ihres eigenen Tors ab, die Tore beeinflussen sich nicht.
:::
:::karte formel Z-Parameter
Wie bestimmt man die Z-Parameter eines Zweitors durch Versuche an den Toren?
---
Aus zwei Leerlaufversuchen: $Z_{11}=\left.\frac{U_1}{I_1}\right|_{I_2=0}$ und $Z_{21}=\left.\frac{U_2}{I_1}\right|_{I_2=0}$ bei offenem Tor 2, $Z_{12}=\left.\frac{U_1}{I_2}\right|_{I_1=0}$ und $Z_{22}=\left.\frac{U_2}{I_2}\right|_{I_1=0}$ bei offenem Tor 1.
--- falsch
Aus zwei Kurzschlussversuchen: $Z_{11}=\left.\frac{U_1}{I_1}\right|_{U_2=0}$ und $Z_{21}=\left.\frac{U_2}{I_1}\right|_{U_2=0}$ bei kurzgeschlossenem Tor 2, $Z_{12}$ und $Z_{22}$ ebenso bei kurzgeschlossenem Tor 1.
--- falsch
Aus einem einzigen Versuch im Betrieb mit Quelle und Last: Man misst $U_1$, $I_1$, $U_2$, $I_2$ und bildet $Z_{11}$ als $U_1$ durch $I_1$, $Z_{21}$ als $U_2$ durch $I_1$ und so weiter, alles aus denselben vier Messwerten.
--- falsch
Aus zwei Leerlaufversuchen mit denselben Quotienten, aber anders verteilt: Der Versuch mit offenem Tor 2 liefert $Z_{11}$ und $Z_{12}$, der Versuch mit offenem Tor 1 liefert $Z_{21}$ und $Z_{22}$.
:::
:::karte zusammenhang Warum der Leerlauf die Parameter freilegt
Warum legt ein offenes Tor die Z-Parameter einzeln frei?
---
Jede Spannung ist eine Summe aus einem Anteil von $I_1$ und einem von $I_2$. Ein offenes Tor setzt seinen Strom null, dann bleiben nur die Anteile des anderen Stroms. Ein Versuch liefert so zwei Parameter.
--- falsch
Weil im Leerlauf keine Leistung umgesetzt wird. Die Spannungen an den Toren sind dann gleich den Leerlaufspannungen der Quelle, und jede dieser Spannungen liefert für sich genau einen der vier Parameter.
--- falsch
Weil ein offenes Tor seine Spannung null setzt. Dann bleibt in jeder Gleichung nur der Anteil des Stroms am anderen Tor übrig, und jeder Versuch liefert so zwei Parameter.
--- falsch
Weil im Leerlauf alle Ströme im Inneren null sind. Die Spannungen an den Toren hängen dann nur noch von den Bauteilwerten ab und nicht mehr von den Strömen.
:::
:::karte begriff Eingangsleerlaufwiderstand und Ausgangsleerlaufwiderstand
Was geben der Eingangsleerlaufwiderstand $Z_{11}$ und der Ausgangsleerlaufwiderstand $Z_{22}$ eines Zweitors an?
---
$Z_{11}$ ist der Widerstand an Tor 1 bei offenem Tor 2, $Z_{22}$ der Widerstand an Tor 2 bei offenem Tor 1. Beide haben die Einheit $\Omega$.
--- falsch
$Z_{11}$ ist der Widerstand an Tor 1 bei kurzgeschlossenem Tor 2, $Z_{22}$ der an Tor 2 bei kurzgeschlossenem Tor 1. Beide haben die Einheit $\Omega$.
--- falsch
$Z_{11}$ ist der Innenwiderstand der Quelle am Eingang, $Z_{22}$ der Widerstand der Last am Ausgang, jeweils vom Zweitor getrennt gemessen.
--- falsch
$Z_{11}$ ist der Leitwert an Tor 1 bei offenem Tor 2, $Z_{22}$ der Leitwert an Tor 2 bei offenem Tor 1. Beide haben die Einheit Siemens.
:::
:::karte begriff Leerlaufübertragungswiderstand
Was gibt der Leerlaufübertragungswiderstand $Z_{21}$ an, und wie hängt er mit $Z_{12}$ zusammen?
---
$Z_{21}$ ist die Spannung am offenen Tor 2 je Strom in Tor 1, der Leerlaufübertragungswiderstand vorwärts. $Z_{12}$ ist derselbe Widerstand rückwärts. Beide haben die Einheit $\Omega$.
--- falsch
$Z_{21}$ ist der Strom an Tor 2 je Spannung an Tor 1 bei offenem Ausgang, ein Leitwert in Siemens. $Z_{12}$ ist derselbe Leitwert in Rückwärtsrichtung.
--- falsch
$Z_{21}$ ist der Widerstand der Leitung zwischen Tor 1 und Tor 2, über die im Leerlauf Strom übertragen wird. $Z_{12}$ ist dieselbe Leitung, rückwärts durchlaufen, also stets derselbe Wert.
--- falsch
$Z_{21}$ ist die Spannung am offenen Tor 1 je Strom in Tor 2, der Wert vorwärts. $Z_{12}$ ist der Wert rückwärts, die Spannung am offenen Tor 2 je Strom in Tor 1.
:::
:::karte begriff Zweipolgrößen und Transfergrößen
Was unterscheidet Zweipolgrößen von Transfergrößen unter den Parametern eines Zweitors?
---
Zweipolgrößen haben gleiche Indizes: Sie sind der Widerstand eines Klemmenpaars bei festem Abschluss der anderen Seite. Transfergrößen haben verschiedene Indizes: Sie verknüpfen beide Seiten.
--- falsch
Zweipolgrößen haben verschiedene Indizes und verknüpfen beide Seiten. Transfergrößen haben gleiche Indizes und geben an, wie viel Energie durch ein einzelnes Tor in das Zweitor übertragen wird.
--- falsch
Zweipolgrößen beschreiben das Zweitor im Leerlauf, Transfergrößen im Kurzschluss. Welche Indizes sie tragen, spielt für diese Einteilung keine Rolle.
--- falsch
Zweipolgrößen sind Widerstände in $\Omega$, Transfergrößen sind Leitwerte in Siemens, weil sie einen Strom von einem Tor zum anderen übertragen.
:::
:::karte begriff Impedanz
Wofür steht der Buchstabe $Z$ in der Impedanzform, und was ist er bei den Gleichgrößen dieses Kapitels?
---
Für die Impedanz. Sie verallgemeinert den Widerstand auf Kondensatoren und Spulen bei Wechselgrößen. Bei Gleichgrößen sind alle $Z$ reelle Widerstände, $Z_{ii}=R_{ii}$.
--- falsch
Für die Impedanz, einen Widerstand, den es nur bei Wechselgrößen gibt. Bei Gleichgrößen sind alle $Z$ null, und man rechnet stattdessen nur mit den Widerständen $R$.
--- falsch
Für die Impedanz, den Kehrwert des Widerstands in Siemens. Bei Gleichgrößen sind alle $Z$ deshalb reelle Leitwerte, also $Z_{ii}=G_{ii}$.
--- falsch
Für die Impedanz, den Widerstand des Zweitors als Ganzes zwischen Klemme 1 und Klemme 2. Bei Gleichgrößen ist sie die Summe aller Widerstände.
:::
:::karte zusammenhang Ersatzschaltbild der Z-Form
Wie sieht das Ersatzschaltbild der Z-Form aus, und warum gerade so?
---
An jedem Tor ein Widerstand in Reihe mit einer stromgesteuerten Spannungsquelle (CCVS). Spannungen addieren sich in Reihe; $Z_{11}I_1$ hängt vom eigenen Strom ab, ein Widerstand, $Z_{12}I_2$ vom fremden, eine gesteuerte Quelle.
--- falsch
An jedem Tor ein Widerstand parallel zu einer spannungsgesteuerten Stromquelle (VCCS). Die Ströme sind die Ursachen, und Ströme addieren sich in einer Parallelschaltung; deshalb liegen beide Bauteile parallel am Tor.
--- falsch
An jedem Tor ein Widerstand in Reihe mit einer idealen Spannungsquelle mit festem Wert. Die Parameter $Z_{12}$ und $Z_{21}$ sind feste Zahlen, also liefern auch die Quellen feste Spannungen.
--- falsch
An jedem Tor ein Widerstand in Reihe mit einer stromgesteuerten Stromquelle (CCCS). Die Ursachen sind Ströme, deshalb muss auch die gesteuerte Quelle einen Strom liefern, der zum Tor passt.
:::
:::karte formel Z-Matrix der T-Schaltung
Wie lautet die Z-Matrix der T-Schaltung mit dem Längswiderstand $R_\mathrm{a}$ am Eingang, dem Querwiderstand $R_\mathrm{b}$ und dem Längswiderstand $R_\mathrm{c}$ am Ausgang?
---
$\mathbf Z=\begin{pmatrix}R_\mathrm{a}+R_\mathrm{b}&R_\mathrm{b}\\mathbb{R}_\mathrm{b}&R_\mathrm{b}+R_\mathrm{c}\end{pmatrix}$. Bei offenem Tor 2 fließt der Strom durch $R_\mathrm{a}$ und $R_\mathrm{b}$, $R_\mathrm{c}$ ist stromlos, und $U_2$ ist die Spannung an $R_\mathrm{b}$.
--- falsch
$\mathbf Z=\begin{pmatrix}R_\mathrm{a}&R_\mathrm{b}\\mathbb{R}_\mathrm{b}&R_\mathrm{c}\end{pmatrix}$. Jeder Längswiderstand gehört zu seinem eigenen Tor, und der Querwiderstand verknüpft als Transfergröße die beiden Seiten.
--- falsch
$\mathbf Z=\begin{pmatrix}R_\mathrm{a}+R_\mathrm{b}&R_\mathrm{b}\\mathbb{R}_\mathrm{b}&R_\mathrm{b}+R_\mathrm{c}\end{pmatrix}$. Bei offenem Tor 2 fließt der Strom durch alle drei Widerstände, und $U_2$ ist die Spannung an $R_\mathrm{c}$.
--- falsch
$\mathbf Z=\begin{pmatrix}R_\mathrm{a}+R_\mathrm{b}&R_\mathrm{a}\\mathbb{R}_\mathrm{c}&R_\mathrm{b}+R_\mathrm{c}\end{pmatrix}$. Die Transfergrößen sind die Längswiderstände, weil durch sie der Strom von Tor zu Tor fließt.
:::
:::karte formel Z-Parameter der Brücke
Wie lauten die Z-Parameter der erdsymmetrischen Brücke aus zwei Widerstandspaaren $R_\mathrm{x}$, $R_\mathrm{y}$, und warum?
---
$Z_{11}=Z_{22}=\frac{R_\mathrm{x}+R_\mathrm{y}}{2}$ und $Z_{21}=Z_{12}=\frac{R_\mathrm{y}-R_\mathrm{x}}{2}$. Ein Strom an Tor 1 teilt sich je zur Hälfte auf zwei Zweige mit $R_\mathrm{x}+R_\mathrm{y}$, und die Spannung zwischen den Zweigmitten ist $\frac{I_1}{2}R_\mathrm{y}-\frac{I_1}{2}R_\mathrm{x}$.
--- falsch
$Z_{11}=Z_{22}=R_\mathrm{x}+R_\mathrm{y}$ und $Z_{21}=Z_{12}=0$. Ohne Masseleitung haben die beiden Tore keinen gemeinsamen Widerstand, deshalb gibt es auch keine Kopplung zwischen ihnen, gleich wie die Werte gewählt sind.
--- falsch
$Z_{11}=Z_{22}=\frac{R_\mathrm{x}+R_\mathrm{y}}{2}$ und $Z_{21}=Z_{12}=\frac{R_\mathrm{x}R_\mathrm{y}}{R_\mathrm{x}+R_\mathrm{y}}$. Die Transfergrößen entsprechen der Parallelschaltung der beiden Widerstände eines Zweigs, über die der Strom zum anderen Tor gelangt.
--- falsch
$Z_{11}=Z_{22}=2(R_\mathrm{x}+R_\mathrm{y})$ und $Z_{21}=Z_{12}=R_\mathrm{y}-R_\mathrm{x}$. Der Strom an Tor 1 fließt nacheinander durch beide Zweige, die in Reihe liegen, und am Ausgang bleibt die Differenz.
:::
:::karte zusammenhang Entkoppelte Tore
Unter welcher Bedingung ist $Z_{21}=0$ beim T-Zweitor und bei der Brücke, sodass ein Strom an Tor 1 am offenen Tor 2 keine Spannung erzeugt?
---
Beim T-Zweitor für $R_\mathrm{b}\to0$: Der Querzweig ist ein Draht, die Tore sind entkoppelt, $Z_{12}=Z_{21}=0$. Bei der Brücke für $R_\mathrm{x}=R_\mathrm{y}$: Sie ist dann abgeglichen.
--- falsch
Beim T-Zweitor für $R_\mathrm{b}\to\infty$, weil dann kein Strom mehr durch den Querzweig fließt. Bei der Brücke für $R_\mathrm{y}=2R_\mathrm{x}$, weil sich dann die Zweigspannungen aufheben.
--- falsch
Beim T-Zweitor für $R_\mathrm{a}=R_\mathrm{c}$, weil sich dann die Spannungen an beiden Längswiderständen gegenseitig aufheben. Bei der Brücke für $R_\mathrm{x}=R_\mathrm{y}$.
--- falsch
Nie: Jedes Zweitor überträgt einen Teil der Eingangsspannung an den Ausgang, sonst wäre es kein Zweitor. $Z_{21}$ kann nur sehr klein werden, aber nicht null.
:::
:::karte zusammenhang Strom oder Spannung beim Leerlaufversuch
Muss man beim Leerlaufversuch an Tor 1 einen Strom einprägen, oder geht auch eine Spannungsquelle?
---
Eine Spannungsquelle geht auch. Es zählt nur, dass das andere Tor offen ist; man misst $U_1$ und $I_1$ und bildet den Quotienten. Der eingeprägte Strom passt nur zur Denkweise der Form.
--- falsch
Man muss einen Strom einprägen, weil eine Spannungsquelle am Eingang das offene Tor 2 über das Zweitor kurzschließen würde und dann ein unbegrenzt großer Strom durch das Zweitor flösse.
--- falsch
Eine Spannungsquelle geht nur, wenn man zusätzlich Tor 2 kurzschließt, denn sonst ist der Strom $I_1$ nicht festgelegt und der Quotient bleibt unbestimmt.
--- falsch
Man muss einen Strom einprägen, weil die Z-Parameter Quotienten mit dem Strom im Nenner sind und eine Spannungsquelle keinen bekannten, festen Strom liefern kann.
:::
::::

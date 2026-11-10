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

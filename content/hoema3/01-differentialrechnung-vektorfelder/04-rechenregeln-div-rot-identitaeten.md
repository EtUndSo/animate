---
title: Rechenregeln und Identitäten für Divergenz und Rotation
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Differentialrechnung für Vektorfelder
order: 3010400
summary: Von Grund auf – das Handwerkszeug für Rechnungen mit $\nabla$, jede Regel hergeleitet. Kreuzprodukt in Indexschreibweise (Levi-Civita, Kronecker-Delta), Produktregeln für $\operatorname{div}(\phi\vec E)$ und $\operatorname{rot}(\phi\vec E)$, Spatprodukt und Graßmann-Identität, die Produktregeln für $\vec E\times\vec B$ und die zwei zentralen Identitäten $\operatorname{div}\operatorname{rot}\vec E=0$ und $\operatorname{rot}\operatorname{rot}\vec E=\nabla\operatorname{div}\vec E-\Delta\vec E$. Dazu Vektorpotentiale, Eichfreiheit und Coulomb-Eichung.
tags: Produktregel, Levi-Civita-Symbol, Kronecker-Delta, Spatprodukt, Graßmann-Identität, div rot, rot rot, Vektorpotential, Eichfreiheit, Coulomb-Eichung
---

## Anschaulich

Stell dir eine **Wasserströmung** vor: An jedem Ort hat das Wasser eine Geschwindigkeit — ein Vektorfeld $\vec E$. Zwei
Messgeräte aus dem vorigen Artikel kennen wir schon. Ein winziges **Kästchen** zählt, wie viel Wasser netto
herausströmt — die Divergenz. Ein winziges **Schaufelrad** zeigt, wie stark die Strömung wirbelt — die Rotation.

Jetzt kippen wir einen **Farbstoff** ins Wasser. Seine Konzentration ist ein Skalarfeld $\phi$, eine Zahl pro Ort, und
der Farbstoff wird mit der Strömung mitgetragen. Sein Fluss ist das Produkt $\phi\,\vec E$: viel Farbstoff dort, wo
die Konzentration hoch **und** die Strömung schnell ist.

Die Rechenregeln dieses Artikels beantworten Fragen wie: Wie stark quillt der Farbstofffluss aus einem Kästchen, wenn
man weiß, wie das Wasser quillt und wie sich die Konzentration ändert? Und warum kann sich ein Schaufelrad drehen,
obwohl das Wasser selbst gar nicht wirbelt? Dieses Bild — Strömung, Farbstoff, Kästchen und Schaufelrad — begleitet
uns durch den ganzen Artikel.

Dabei hat der Nabla-Operator $\nabla$ zwei Gesichter. Er verhält sich wie ein **Vektor** — man bildet Skalar- und
Kreuzprodukte mit ihm. Und er ist ein **Ableitungsoperator** — es gelten Produktregeln. Aus diesem Doppelleben
entstehen elegante Identitäten und ein paar Fallstricke.

Zwei der Identitäten sind Spiegelbilder: Die Steigungspfeile einer Landschaft wirbeln nie (voriger Artikel), und ein
reiner Wirbel quillt nie. Eine dritte steckt direkt hinter der Wellengleichung des Lichts.

:::grafik
Szene: hoema3/differentialrechnung-vektorfelder/04-farbstoff-stroemung · Vorlage: stroemung-farbstoff-2d
Eine Wasserströmung $\vec E$ als Pfeilfeld, darin eine Farbstoffwolke mit ortsabhängiger Konzentration $\phi$ (Farbe).
An einer Stelle ein kleines Kästchen, das den Netto-Ausfluss des Farbstoffs $\phi\vec E$ zählt, an einer anderen ein
Schaufelrad, das sich in einer Scherströmung dreht. Schaltflächen blenden die beiden Ursachen getrennt ein: „Wasser
quillt" und „Konzentration ändert sich längs der Strömung". (Blau = Strömung, rot = Farbstofffluss, orange =
Kästchen/Schaufelrad, grau = Konzentrations-Höhenlinien.)
:::

## Werkzeug: das Kreuzprodukt in Indexschreibweise

Für Rechnungen mit Kreuzprodukten und Rotationen braucht man zwei kleine Symbole. Im ganzen Artikel laufen die Indizes
$i,j,k,l,m$ über $1,2,3$, und $\partial_j$ ist die Abkürzung für die partielle Ableitung $\partial/\partial x_j$.

Das __Kronecker-Delta__ zeigt an, ob zwei Indizes gleich sind:

$$\delta_{ij} = \begin{cases} 1, & i=j,\\ 0, & i\neq j. \end{cases}$$

Das __Levi-Civita-Symbol__ zeigt an, ob drei Indizes eine **gerade** oder **ungerade** Umordnung von $(1,2,3)$ sind:

$$\varepsilon_{ijk} = \begin{cases} +1, & (i,j,k)\in\{(1,2,3),\,(2,3,1),\,(3,1,2)\},\\ -1, & (i,j,k)\in\{(3,2,1),\,(1,3,2),\,(2,1,3)\},\\ \ \ 0, & \text{sonst, also wenn zwei Indizes gleich sind.} \end{cases}$$

**Im Bild:** $\varepsilon_{ijk}$ ist ein Orientierungsmesser für drei Achsenrichtungen. Es gibt $+1$ für eine
rechtshändige Reihenfolge (Daumen, Zeigefinger, Mittelfinger der rechten Hand), $-1$ für eine linkshändige und $0$,
wenn zwei Richtungen zusammenfallen — dann spannen sie keinen Raum auf. Vertauscht man zwei Indizes, wechselt das
Vorzeichen: Das Symbol ist __antisymmetrisch__. Zyklisches Weiterrücken ändert dagegen nichts.

Beides liest man direkt an der Definition ab. Tauscht man in $(1,2,3)$ die ersten beiden Indizes, entsteht $(2,1,3)$ aus
der Minus-Zeile. Rückt man dagegen zyklisch weiter, entsteht $(2,3,1)$ aus der Plus-Zeile. Im Bild: Ein Tausch spiegelt
die Hand, ein zyklisches Weiterrücken dreht sie nur.

Damit schreibt sich das Kreuzprodukt zweier Vektoren $\vec a,\vec b\in\mathbb{R}^3$ komponentenweise in einer Zeile:

$$(\vec a\times\vec b)_i = \sum_{j,k=1}^{3}\varepsilon_{ijk}\,a_j\,b_k.$$

:::herleitung
Wir rechnen die erste Komponente aus. Alle Terme mit einem doppelten Index fallen weg, übrig bleiben genau zwei:

$$(\vec a\times\vec b)_1 = \varepsilon_{123}\,a_2b_3 + \varepsilon_{132}\,a_3b_2 = (+1)\,a_2b_3 + (-1)\,a_3b_2 = a_2b_3 - a_3b_2.$$

Das ist genau die erste Komponente des Kreuzprodukts. Die zweite und dritte Komponente entstehen genauso, die Indizes
rücken nur zyklisch weiter.
:::

Ersetzt man den Vektor $\vec a$ durch den Nabla-Operator, also $a_j$ durch $\partial_j$, entsteht dieselbe Schreibweise
für die Rotation eines Feldes $\vec E$ (vorheriger Artikel):

$$(\operatorname{rot}\vec E)_i = \sum_{j,k=1}^{3}\varepsilon_{ijk}\,\partial_j E_k.$$

Dabei steht $\partial_j$ immer links von $E_k$: Der Operator wirkt auf die Komponente.

:::herleitung
Die Rotation ist das formale Kreuzprodukt $\nabla\times\vec E$ (vorheriger Artikel). Die Herleitung der Indexformel hat
nur benutzt, **welche** Komponenten miteinander kombiniert werden — nicht, dass $a_j$ eine Zahl ist. Darum gilt sie
wörtlich auch, wenn man $a_j$ durch $\partial_j$ und $b_k$ durch $E_k$ ersetzt. Die erste Komponente lautet

$$(\operatorname{rot}\vec E)_1 = \varepsilon_{123}\,\partial_2E_3 + \varepsilon_{132}\,\partial_3E_2 = \partial_2E_3 - \partial_3E_2.$$

Das ist genau die erste Komponente aus der Definition der Rotation; die anderen beiden folgen zyklisch.
:::

:::grafik
Szene: hoema3/differentialrechnung-vektorfelder/04-levi-civita-hand · Vorlage: rechte-hand-achsen-3d
Drei Achsen $\vec e_1,\vec e_2,\vec e_3$ als rechte Hand (Daumen, Zeige-, Mittelfinger). Ein Index-Tripel $(i,j,k)$ wird
ausgewählt; die Hand zeigt $+1$ (rechtshändige Reihenfolge), $-1$ (Spiegelbild, linke Hand) oder $0$ (zwei Finger
fallen zusammen, flach). Daneben das Kreuzprodukt $\vec a\times\vec b$ mit der Komponente $(\vec a\times\vec b)_1=a_2b_3-a_3b_2$.
(Rot = gewähltes Tripel, orange = Ergebnis, grau = Achsen.)
:::

## Produktregeln mit einem Skalarfeld

Sei $U\subseteq\mathbb{R}^3$ offen, $\phi:U\to\mathbb{R}$ ein differenzierbares Skalarfeld — die
Farbstoff-Konzentration — und $\vec E:U\to\mathbb{R}^3$ ein differenzierbares Vektorfeld — die Strömung. Dann gilt:

:::formel Lemma
$$\operatorname{div}(\phi\,\vec E) = \nabla\phi\cdot\vec E + \phi\,\operatorname{div}\vec E, \qquad \operatorname{rot}(\phi\,\vec E) = \nabla\phi\times\vec E + \phi\,\operatorname{rot}\vec E.$$
:::

**So liest man das:** Beide Regeln haben die Struktur der HM1-Produktregel, „Ableitung des ersten Faktors mal zweiten
plus ersten mal Ableitung des zweiten". Einmal wird $\phi$ abgeleitet — das gibt den Gradienten $\nabla\phi$, der dann
per Skalar- bzw. Kreuzprodukt mit $\vec E$ verknüpft wird. Einmal wird $\vec E$ abgeleitet — das gibt $\phi$ mal
Divergenz bzw. Rotation von $\vec E$.

**Im Bild (Divergenz):** Der Farbstofffluss kann aus zwei Gründen aus einem Kästchen herausquellen. Entweder das Wasser
selbst quillt, dann nimmt es Farbstoff mit hinaus (der Term $\phi\,\operatorname{div}\vec E$).

Oder die Konzentration ändert sich längs der Strömung (der Term $\nabla\phi\cdot\vec E$). Fließt das Wasser in Richtung
**steigender** Konzentration, tritt auf der einen Seite dünnes Farbwasser ein und auf der anderen dichtes aus. Dann
verlässt mehr Farbstoff das Kästchen, als hineinkommt, obwohl das Wasser gar nicht quillt — der Term ist positiv.
Fließt es in Richtung fallender Konzentration, sammelt sich Farbstoff im Kästchen, der Term ist negativ.

:::herleitung
Die Divergenz ist eine Summe von Ableitungen, und auf jeden Summanden wirkt die gewöhnliche Produktregel aus HM1:

$$\operatorname{div}(\phi\,\vec E) = \sum_{j}\partial_j(\phi\,E_j) = \sum_{j}\big(\partial_j\phi\;E_j + \phi\;\partial_j E_j\big).$$

Die erste Teilsumme ist das Skalarprodukt aus $\nabla\phi$ und $\vec E$, die zweite ist $\phi$ mal die Divergenz:

$$\sum_{j}\partial_j\phi\;E_j = \nabla\phi\cdot\vec E, \qquad \sum_{j}\phi\;\partial_j E_j = \phi\,\operatorname{div}\vec E.$$

Nirgends wurde benutzt, dass es drei Dimensionen sind — die erste Regel gilt deshalb in jedem $\mathbb{R}^n$.
:::

**Zahlenbeispiel: Farbstoff, der stromabwärts dichter wird.** Das Wasser fließt gleichmäßig nach rechts, und die
Konzentration nimmt nach rechts zu:

$$\vec E(x,y,z) = (1,0,0), \qquad \phi(x,y,z) = x, \qquad \phi\,\vec E = (x,0,0).$$

Das Wasser quillt nicht, trotzdem quillt der Farbstofffluss. Die Produktregel liefert

$$\nabla\phi\cdot\vec E = (1,0,0)\cdot(1,0,0) = 1, \qquad \phi\,\operatorname{div}\vec E = x\cdot0 = 0,$$

und direkt nachgerechnet stimmt das:

$$\operatorname{div}(x,0,0) = \partial_x x = 1.$$

**Im Bild:** Nimm den Würfel $[0,1]^3\subseteq\mathbb{R}^3$. Durch die linke Wand bei $x=0$ kommt Wasser ohne Farbstoff
herein, durch die rechte Wand bei $x=1$ verlässt Wasser mit Konzentration $1$ den Würfel; durch die übrigen Wände fließt
nichts. Netto verlässt also pro Zeiteinheit eine Einheit Farbstoff den Würfel — bei Volumen $1$ genau die Divergenz $1$.

**Im Bild (Rotation):** Ein Schaufelrad dreht sich, wenn das Wasser selbst wirbelt (der Term
$\phi\,\operatorname{rot}\vec E$). Es dreht sich aber auch, wenn die Gewichtung $\phi$ die Strömung auf einer Seite des
Rades stärker macht als auf der anderen — wie in einem Fluss, der an der Oberfläche schneller fließt als am Grund
(der Term $\nabla\phi\times\vec E$). Das ist ein Gedankenbild: Ein echtes Rad reagiert auf die Wassergeschwindigkeit,
hier steht es für die Rotation des gewichteten Feldes $\phi\vec E$.

:::herleitung
Für die Rotation nimmt man die Indexschreibweise und wieder die Produktregel aus HM1:

$$(\operatorname{rot}(\phi\,\vec E))_i = \sum_{j,k}\varepsilon_{ijk}\,\partial_j(\phi\,E_k) = \sum_{j,k}\varepsilon_{ijk}\,(\partial_j\phi)\,E_k + \phi\sum_{j,k}\varepsilon_{ijk}\,\partial_j E_k.$$

Die erste Summe ist nach der Indexformel des Kreuzprodukts die $i$-te Komponente von $\nabla\phi\times\vec E$, die
zweite die $i$-te Komponente von $\operatorname{rot}\vec E$:

$$(\operatorname{rot}(\phi\,\vec E))_i = (\nabla\phi\times\vec E)_i + \phi\,(\operatorname{rot}\vec E)_i.$$
:::

**Zahlenbeispiel: die Scherströmung.** Wir nehmen eine gleichmäßige Strömung nach rechts, die selbst nicht wirbelt,
und eine Gewichtung, die nach oben zunimmt:

$$\vec E(x,y,z) = (1,0,0), \qquad \phi(x,y,z) = y, \qquad \phi\,\vec E = (y,0,0).$$

Das gewichtete Feld fließt oben schneller als unten. Die Produktregel liefert seine Rotation:

$$\nabla\phi = (0,1,0), \qquad \nabla\phi\times\vec E = (0,1,0)\times(1,0,0) = (0,0,-1), \qquad \phi\,\operatorname{rot}\vec E = \vec 0.$$

Direkt nachgerechnet stimmt das:

$$\operatorname{rot}(y,0,0) = \big(\partial_y 0-\partial_z 0,\ \partial_z y-\partial_x 0,\ \partial_x 0-\partial_y y\big) = (0,0,-1).$$

**Im Bild:** Die Drehachse zeigt in die negative $z$-Richtung. Blickt man von der positiven $z$-Achse auf die
$xy$-Ebene, dreht sich das Rad im Uhrzeigersinn, weil seine obere Hälfte stärker nach rechts geschoben wird als die
untere. Eine geradlinige Strömung kann also wirbeln!

:::grafik
Szene: hoema3/differentialrechnung-vektorfelder/04-scherstroemung · Vorlage: scherstroemung-schaufelrad-2d
Die Scherströmung $\phi\vec E=(y,0,0)$: waagerechte Pfeile nach rechts, die nach oben länger werden. Ein Schaufelrad in
der Mitte dreht sich im Uhrzeigersinn, weil seine obere Hälfte stärker angeströmt wird; daneben die Zerlegung
$\nabla\phi\times\vec E=(0,0,-1)$ (Drehachse nach unten). Zum Vergleich die gleichmäßige Strömung $\vec E=(1,0,0)$, in der
das Rad stillsteht. (Blau = Strömung, orange = Schaufelrad, rot = Rotationsvektor, grau = Gitter.)
:::

**Die ebene Version.** Für ein ebenes Feld $\vec E=(E_1,E_2)$ mit der skalaren 2D-Rotation (vorheriger Artikel) lautet
die zweite Regel

$$\operatorname{rot}(\phi\,\vec E) = \big(\partial_1\phi\;E_2 - \partial_2\phi\;E_1\big) + \phi\,\operatorname{rot}\vec E.$$

Das Kreuzprodukt wird dabei durch das „äußere Produkt" $\partial_1\phi\,E_2-\partial_2\phi\,E_1$ in der Ebene ersetzt.

:::herleitung
Die 2D-Rotation eines Feldes ist $\partial_1 E_2 - \partial_2 E_1$. Für das Feld $\phi\vec E$ liefert die Produktregel aus
HM1 in beiden Termen je zwei Summanden:

$$\operatorname{rot}(\phi\,\vec E) = \partial_1(\phi E_2) - \partial_2(\phi E_1) = \partial_1\phi\;E_2 + \phi\,\partial_1E_2 - \partial_2\phi\;E_1 - \phi\,\partial_2E_1.$$

Die Summanden mit abgeleitetem $\phi$ bilden den Klammerterm, die mit abgeleitetem $\vec E$ ergeben $\phi$ mal die
2D-Rotation.

**Im Bild:** Man kann das ebene Feld auch als räumliches Feld $(E_1,E_2,0)$ auffassen, das ebenso wie $\phi$ nicht von
$x_3$ abhängt — eine Strömung aus lauter gleichen, übereinanderliegenden Schichten. Seine räumliche Rotation zeigt dann
senkrecht zur Ebene, und ihre dritte Komponente ist die 2D-Rotation. Ebenso ist die dritte Komponente des Kreuzprodukts

$$(\nabla\phi\times\vec E)_3 = \partial_1\phi\;E_2 - \partial_2\phi\;E_1.$$

Die ebene Regel ist also einfach die dritte Komponente der räumlichen.
:::

## Spatprodukt und Graßmann-Identität

Für die Produktregeln mit **zwei** Vektorfeldern braucht man zwei Identitäten aus der Vektorrechnung.

**Das Spatprodukt.** Für drei Vektoren $\vec a,\vec b,\vec c\in\mathbb{R}^3$ ist

$$\vec a\cdot(\vec b\times\vec c) = \det(\vec a\,|\,\vec b\,|\,\vec c).$$

Rechts steht die Determinante der $3\times3$-Matrix mit den Spalten $\vec a,\vec b,\vec c$. Das Spatprodukt ist
**zyklisch vertauschbar**:

$$\vec a\cdot(\vec b\times\vec c) = \vec b\cdot(\vec c\times\vec a) = \vec c\cdot(\vec a\times\vec b).$$

**Im Bild:** Die drei Vektoren spannen einen schiefen Kasten auf, einen __Spat__. Seine Grundfläche ist das
Parallelogramm aus $\vec b$ und $\vec c$. Dessen Flächeninhalt ist $\lvert\vec b\times\vec c\rvert$, und der Vektor
$\vec b\times\vec c$ steht senkrecht darauf (beides aus der linearen Algebra). Zerlegt man das Spatprodukt mit dem
Einheitsnormalenvektor, erkennt man Grundfläche mal Höhe (für $\vec b\times\vec c\neq\vec 0$):

$$\vec a\cdot(\vec b\times\vec c) = \underbrace{\lvert\vec b\times\vec c\rvert}_{\text{Grundfläche}}\;\cdot\;\underbrace{\vec a\cdot\frac{\vec b\times\vec c}{\lvert\vec b\times\vec c\rvert}}_{\text{Höhe mit Vorzeichen}}.$$

Der zweite Faktor ist der Anteil von $\vec a$ senkrecht zur Grundfläche. Das Spatprodukt ist also das **orientierte
Volumen** — positiv für eine rechtshändige Reihenfolge, negativ für eine linkshändige.

:::herleitung
Mit der Indexformel des Kreuzprodukts ist

$$\vec a\cdot(\vec b\times\vec c) = \sum_i a_i\sum_{j,k}\varepsilon_{ijk}\,b_j\,c_k = \sum_{i,j,k}\varepsilon_{ijk}\,a_i\,b_j\,c_k.$$

Schreibt man die sechs von null verschiedenen Terme aus, entsteht genau die Regel von Sarrus für die Determinante:

$$a_1b_2c_3 + a_2b_3c_1 + a_3b_1c_2 - a_3b_2c_1 - a_1b_3c_2 - a_2b_1c_3 = \det(\vec a\,|\,\vec b\,|\,\vec c).$$

Zyklisches Vertauschen von $\vec a,\vec b,\vec c$ entspricht zyklischem Weiterrücken der Indizes von $\varepsilon_{ijk}$, und
das ändert das Symbol nicht.
:::

**Die Graßmann-Identität.** Sie löst ein doppeltes Kreuzprodukt auf:

:::formel Lemma
$$\vec a\times(\vec b\times\vec c) = (\vec a\cdot\vec c)\,\vec b - (\vec a\cdot\vec b)\,\vec c.$$
:::

**Im Bild:** $\vec b\times\vec c$ steht senkrecht auf der Ebene, die $\vec b$ und $\vec c$ aufspannen. Kreuzt man das noch
einmal mit $\vec a$, steht das Ergebnis senkrecht auf dieser Normalen — es liegt also wieder **in** der Ebene von $\vec b$
und $\vec c$. Darum ist es eine Kombination aus $\vec b$ und $\vec c$. Merkregel: „BAC minus CAB".

:::herleitung
**Schritt 1 — eine Identität für zwei Levi-Civita-Symbole.** Es gilt

$$\sum_{k}\varepsilon_{ijk}\,\varepsilon_{klm} = \delta_{il}\,\delta_{jm} - \delta_{im}\,\delta_{jl}.$$

Man prüft alle Fälle:

- Sind die ersten beiden Indizes $i$ und $j$ gleich, ist $\varepsilon_{ijk}$ null. Rechts heben sich die beiden Produkte
  dann genau auf — beide Seiten sind null.
- Sind $i$ und $j$ verschieden, überlebt links nur das eine $k$, das von beiden verschieden ist. Dann ist
  $\varepsilon_{klm}$ nur von null verschieden, wenn $l$ und $m$ dieselben zwei Zahlen sind wie $i$ und $j$. Andernfalls
  sind beide Seiten null, denn auch rechts verlangt jedes Delta-Produkt genau das.
- Gleiche Reihenfolge ($l$ wie $i$, $m$ wie $j$): Dann ist $\varepsilon_{klm}$ das Symbol $\varepsilon_{kij}$, also
  $\varepsilon_{ijk}$ zyklisch weitergerückt, mit demselben Wert. Das Produkt ist ein Quadrat, also $+1$. Rechts steht
  ebenfalls $1\cdot1-0$.
- Vertauschte Reihenfolge ($l$ wie $j$, $m$ wie $i$): Jetzt ist zusätzlich ein Indexpaar getauscht, das Produkt ist
  $-1$. Rechts steht ebenfalls $0-1\cdot1$.

**Schritt 2 — einsetzen.** Mit zweimal der Indexformel des Kreuzprodukts:

$$\big[\vec a\times(\vec b\times\vec c)\big]_i = \sum_{j,k}\varepsilon_{ijk}\,a_j\sum_{l,m}\varepsilon_{klm}\,b_l\,c_m = \sum_{j,l,m}\big(\delta_{il}\delta_{jm}-\delta_{im}\delta_{jl}\big)\,a_j\,b_l\,c_m.$$

Ein Kronecker-Delta in einer Summe wirkt wie ein **Filter**: Von allen Summanden über $l$ lässt $\delta_{il}$ nur den
einen übrig, in dem $l$ gleich $i$ ist — es setzt den Summationsindex fest. So wählen die Deltas die Indizes aus:

$$\text{erster Term: } l=i,\ m=j, \qquad \text{zweiter Term: } m=i,\ l=j.$$

Übrig bleibt

$$\sum_j a_j c_j\; b_i - \sum_j a_j b_j\; c_i = (\vec a\cdot\vec c)\,b_i - (\vec a\cdot\vec b)\,c_i.$$
:::

**Zahlenbeispiel.** Wir wählen drei Standard-Einheitsvektoren, also Achsenrichtungen:

$$\vec a = \vec e_1, \qquad \vec b = \vec e_1, \qquad \vec c = \vec e_2.$$

Links ergibt sich

$$\vec b\times\vec c = \vec e_1\times\vec e_2 = \vec e_3, \qquad \vec a\times(\vec b\times\vec c) = \vec e_1\times\vec e_3 = -\vec e_2,$$

und rechts ebenso

$$(\vec a\cdot\vec c)\,\vec b - (\vec a\cdot\vec b)\,\vec c = 0\cdot\vec e_1 - 1\cdot\vec e_2 = -\vec e_2.$$

:::grafik
Szene: hoema3/differentialrechnung-vektorfelder/04-spat-grassmann · Vorlage: spat-und-doppelkreuz-3d
Links der Spat aus $\vec a,\vec b,\vec c$: Grundfläche $\lvert\vec b\times\vec c\rvert$, Höhe als Anteil von $\vec a$ senkrecht
dazu, Volumen $=\vec a\cdot(\vec b\times\vec c)$. Rechts die Ebene von $\vec b$ und $\vec c$ mit der Normalen $\vec b\times\vec c$;
das doppelte Kreuzprodukt $\vec a\times(\vec b\times\vec c)$ klappt zurück in die Ebene und wird als Kombination
$(\vec a\cdot\vec c)\vec b-(\vec a\cdot\vec b)\vec c$ zerlegt. (Rot = Ergebnis, orange = Normale, blau = $\vec b,\vec c$, grau =
Ebene.)
:::

## Produktregeln für Kreuzprodukte von Vektorfeldern

Für zwei differenzierbare Vektorfelder $\vec E,\vec B:U\to\mathbb{R}^3$ auf $U\subseteq\mathbb{R}^3$ gilt:

:::formel Lemma
$$\operatorname{div}(\vec E\times\vec B) = \vec B\cdot\operatorname{rot}\vec E - \vec E\cdot\operatorname{rot}\vec B,$$

$$\operatorname{rot}(\vec E\times\vec B) = \vec E\,\operatorname{div}\vec B - \vec B\,\operatorname{div}\vec E + (\vec B\cdot\nabla)\vec E - (\vec E\cdot\nabla)\vec B.$$
:::

Dabei bedeutet $(\vec E\cdot\nabla)\vec B$ die Ableitung des Feldes $\vec B$ in Richtung von $\vec E$, komponentenweise:

$$(\vec E\cdot\nabla)\vec B = \sum_{j}E_j\,\frac{\partial\vec B}{\partial x_j}, \qquad \frac{\partial\vec B}{\partial x_j} = \Big(\frac{\partial B_1}{\partial x_j},\frac{\partial B_2}{\partial x_j},\frac{\partial B_3}{\partial x_j}\Big)^{T}.$$

**Im Bild:** $(\vec E\cdot\nabla)\vec B$ fragt: Wie ändert sich der Pfeil $\vec B$, wenn man ein Stück in Richtung von $\vec E$
geht? Es ist die Richtungsableitung aus dem Gradienten-Artikel, angewandt auf jede Komponente von $\vec B$ und
multipliziert mit der Länge von $\vec E$.

:::herleitung
Die $k$-te Komponente ist ein Skalarprodukt mit dem Gradienten von $B_k$. Für $\vec E\neq\vec 0$ zieht man die Länge
heraus:

$$\big((\vec E\cdot\nabla)\vec B\big)_k = \sum_j E_j\,\partial_j B_k = \vec E\cdot\nabla B_k = \lvert\vec E\rvert\;\frac{\vec E}{\lvert\vec E\rvert}\cdot\nabla B_k.$$

Der letzte Faktor ist die Richtungsableitung von $B_k$ in Richtung des Einheitsvektors $\vec E/\lvert\vec E\rvert$
(Gradienten-Artikel).
:::

**Stolperstein — $\nabla$ ist kein gewöhnlicher Vektor.** Würde man $\operatorname{div}(\vec E\times\vec B)$ wie ein
Spatprodukt behandeln und zyklisch vertauschen, käme nur $\vec B\cdot\operatorname{rot}\vec E$ heraus. Der zweite Term
fehlt dann, weil $\nabla$ als Ableitung auf **beide** Faktoren wirkt — die Produktregel erzeugt zwei Terme. Die korrekten
Formeln sind genau das Ergebnis dieser achtsamen Buchführung.

:::herleitung
**Divergenz.** Mit der Indexformel und der Produktregel aus HM1:

$$\operatorname{div}(\vec E\times\vec B) = \sum_i\partial_i\sum_{j,k}\varepsilon_{ijk}\,E_j B_k = \sum_{i,j,k}\varepsilon_{ijk}\,(\partial_i E_j)\,B_k + \sum_{i,j,k}\varepsilon_{ijk}\,E_j\,(\partial_i B_k).$$

Im ersten Term rückt man die Indizes zyklisch weiter, das ändert $\varepsilon$ nicht. Im zweiten vertauscht man $i$ und
$j$, das kehrt das Vorzeichen um:

$$\sum_k B_k\sum_{i,j}\varepsilon_{kij}\,\partial_i E_j - \sum_j E_j\sum_{i,k}\varepsilon_{jik}\,\partial_i B_k = \sum_k B_k\,(\operatorname{rot}\vec E)_k - \sum_j E_j\,(\operatorname{rot}\vec B)_j.$$

Das ist $\vec B\cdot\operatorname{rot}\vec E-\vec E\cdot\operatorname{rot}\vec B$.
:::

:::herleitung
**Rotation.** Jetzt braucht man zweimal die Indexformel und die Identität für zwei Levi-Civita-Symbole aus dem
Graßmann-Beweis:

$$\big(\operatorname{rot}(\vec E\times\vec B)\big)_i = \sum_{j,k}\varepsilon_{ijk}\,\partial_j\sum_{l,m}\varepsilon_{klm}\,E_l B_m = \sum_{j,l,m}\big(\delta_{il}\delta_{jm}-\delta_{im}\delta_{jl}\big)\,\partial_j(E_l B_m).$$

Die Deltas wählen die Indizes aus, danach wirkt die Produktregel:

$$\sum_j\partial_j(E_i B_j) - \sum_j\partial_j(E_j B_i) = \sum_j\big(B_j\,\partial_j E_i + E_i\,\partial_j B_j\big) - \sum_j\big(B_i\,\partial_j E_j + E_j\,\partial_j B_i\big).$$

Die vier Summen sind der Reihe nach die $i$-ten Komponenten von $(\vec B\cdot\nabla)\vec E$, $\vec E\,\operatorname{div}\vec B$,
$\vec B\,\operatorname{div}\vec E$ und $(\vec E\cdot\nabla)\vec B$ — genau die behauptete Formel.
:::

**Bedeutung in der Elektrotechnik.** Mit dem elektrischen Feld $\vec E$ und dem Magnetfeld $\vec H$ ist
$\vec E\times\vec H$ der __Poynting-Vektor__, die Energiestromdichte des Feldes. Die erste Regel zerlegt seine Divergenz
— wie viel Energie aus einem Kästchen herausströmt — in Terme mit den beiden Rotationen. Für diese Rotationen setzt man
die Maxwell-Gleichungen ein, und so entsteht die Energiebilanz des elektromagnetischen Feldes.

## Die zwei zentralen Identitäten

Die wichtigsten Regeln des Kapitels entstehen, wenn man **zwei** Operatoren hintereinander anwendet. Sei
$\vec E:U\to\mathbb{R}^3$ auf $U\subseteq\mathbb{R}^3$ zweimal stetig differenzierbar.

**1. Ein Wirbel quillt nie.**

:::formel Lemma
$$\operatorname{div}\operatorname{rot}\vec E = 0.$$
:::

**Im Bild:** Ein reines Wirbelfeld lässt das Wasser im Kreis laufen. Aus keinem Kästchen strömt dabei netto etwas heraus
— was auf einer Seite hineinläuft, läuft auf der anderen wieder hinaus. Das ist das genaue Spiegelbild zur Aussage des
vorigen Artikels: Die Steigungspfeile einer Landschaft wirbeln nie.

:::herleitung
Mit der Indexformel der Rotation ist

$$S := \operatorname{div}\operatorname{rot}\vec E = \sum_i\partial_i\sum_{j,k}\varepsilon_{ijk}\,\partial_j E_k = \sum_{i,j,k}\varepsilon_{ijk}\,\partial_i\partial_j E_k.$$

Jetzt benennt man die Summationsindizes $i$ und $j$ einfach um — das ändert die Summe nicht. Danach benutzt man, dass
$\varepsilon$ beim Vertauschen von $i$ und $j$ das Vorzeichen wechselt, die zweite Ableitung aber nach dem Satz von
Schwarz nicht:

$$S = \sum_{i,j,k}\varepsilon_{jik}\,\partial_j\partial_i E_k = -\sum_{i,j,k}\varepsilon_{ijk}\,\partial_i\partial_j E_k = -S.$$

Eine Zahl, die gleich ihrem Negativen ist, ist null. Im Bild: Jeder Beitrag wird von einem gespiegelten Beitrag mit
umgekehrtem Vorzeichen ausgelöscht — symmetrisch mal antisymmetrisch ergibt null.
:::

**2. Die Rotation der Rotation.**

:::formel Lemma
$$\operatorname{rot}\operatorname{rot}\vec E = \nabla(\operatorname{div}\vec E) - \Delta\vec E.$$
:::

Dabei ist $\Delta\vec E$ der komponentenweise angewandte Laplace-Operator:

$$\Delta\vec E = (\Delta E_1,\ \Delta E_2,\ \Delta E_3).$$

**Im Bild:** Die doppelte Rotation zerfällt in einen **Quellen-Anteil** $\nabla\operatorname{div}\vec E$ und einen
**Krümmungs-Anteil** $\Delta\vec E$. Der Quellen-Anteil ist der Gradient der Quellstärke, er zeigt dorthin, wo das Feld
stärker quillt. Der Krümmungs-Anteil misst, wie stark jede Komponente vom Mittel ihrer Umgebung abweicht (vorheriger
Artikel).

:::herleitung
Mit zweimal der Indexformel und der Identität für zwei Levi-Civita-Symbole:

$$(\operatorname{rot}\operatorname{rot}\vec E)_i = \sum_{j,k}\varepsilon_{ijk}\,\partial_j\sum_{l,m}\varepsilon_{klm}\,\partial_l E_m = \sum_{j,l,m}\big(\delta_{il}\delta_{jm}-\delta_{im}\delta_{jl}\big)\,\partial_j\partial_l E_m.$$

Die Deltas filtern wie im Graßmann-Beweis die Indizes heraus:

$$\text{erster Term: } l=i,\ m=j, \qquad \text{zweiter Term: } m=i,\ l=j.$$

Mit dem Satz von Schwarz zieht man im ersten Term $\partial_i$ nach vorn:

$$\sum_j\partial_j\partial_i E_j - \sum_j\partial_j\partial_j E_i = \partial_i\Big(\sum_j\partial_j E_j\Big) - \Delta E_i = \partial_i(\operatorname{div}\vec E) - \Delta E_i.$$

Als **Merkregel** kann man die Graßmann-Identität formal anwenden, indem man für die ersten beiden Vektoren den
Nabla-Operator und für den dritten das Feld einsetzt:

$$\nabla\times(\nabla\times\vec E) = \nabla(\nabla\cdot\vec E) - (\nabla\cdot\nabla)\,\vec E.$$

Dabei muss das Feld immer an letzter Stelle stehen, weil $\nabla$ nach rechts ableitet.
:::

**Zahlenbeispiel.** Für das Feld

$$\vec E(x,y,z) = (0,\;0,\;x^2)$$

ergibt sich zuerst

$$\operatorname{rot}\vec E = (0,\;-2x,\;0), \qquad \operatorname{rot}\operatorname{rot}\vec E = (0,\;0,\;-2).$$

Die rechte Seite der Identität stimmt damit überein:

$$\operatorname{div}\vec E = 0, \qquad \Delta\vec E = (0,\;0,\;2), \qquad \nabla(\operatorname{div}\vec E)-\Delta\vec E = (0,\;0,\;-2).$$

:::grafik
Szene: hoema3/differentialrechnung-vektorfelder/04-nullregeln-spiegel · Vorlage: zwei-nullregeln-2d
Zwei „Nullregeln" als spiegelnde Merkbilder. Oben die Steigungspfeile einer Landschaft (senkrecht auf Höhenlinien) mit
einem Schaufelrad, das stillsteht: „Rotation einer Steigung = 0". Unten ein reiner Wirbel (kreisende Pfeile) mit einem
Kästchen, aus dem netto nichts herausfließt: „Divergenz eines Wirbels = 0". Rechts die Zerlegung
$\operatorname{rot}\operatorname{rot}\vec E=\nabla\operatorname{div}\vec E-\Delta\vec E$ mit dem Hinweis „→ Wellengleichung".
(Rot = Gradientenfeld, orange = Wirbelfeld, grau = Höhenlinien/Kästchen.)
:::

## Vektorpotentiale und Eichfreiheit

Die Identität „ein Wirbel quillt nie" führt — spiegelbildlich zum Skalarpotential — auf einen neuen Begriff. Ein
Vektorfeld $\vec B:U\to\mathbb{R}^3$ auf $U\subseteq\mathbb{R}^3$ heißt __Wirbelfeld__ (oder Rotationsfeld), wenn es die
Rotation eines anderen differenzierbaren Feldes $\vec A:U\to\mathbb{R}^3$ ist:

:::formel Definition
$$\vec B = \operatorname{rot}\vec A.$$
:::

Dann heißt $\vec A$ ein __Vektorpotential__ von $\vec B$. Das Magnetfeld ist das wichtigste Beispiel: Es hat ein
Vektorpotential.

**Wirbelfelder sind quellenfrei.** Ist das Vektorpotential zweimal stetig differenzierbar, so ist das Wirbelfeld
divergenzfrei. Das ist eine **notwendige** Bedingung — ein Feld mit Quellen kann kein zweimal stetig differenzierbares
Vektorpotential haben.

:::herleitung
Nach der ersten zentralen Identität, angewandt auf $\vec A$:

$$\operatorname{div}\vec B = \operatorname{div}\operatorname{rot}\vec A = 0.$$
:::

**Notwendig, aber nicht hinreichend.** Wie bei den Gradientenfeldern gilt die Umkehrung im Allgemeinen nicht; sie
hängt von der Gestalt des Gebiets ab. Das Gegenbeispiel ist das Coulomb-Feld $\vec x/\lvert\vec x\rvert^3$ auf
$\mathbb{R}^3\setminus\{\vec 0\}$. Nach der Radialformel aus dem Gradienten-Artikel ist es der negative Gradient von
$1/\lvert\vec x\rvert$:

$$\nabla\frac{1}{\lvert\vec x\rvert} = -\frac{1}{\lvert\vec x\rvert^2}\,\frac{\vec x}{\lvert\vec x\rvert} = -\frac{\vec x}{\lvert\vec x\rvert^3}.$$

Die Funktion $1/\lvert\vec x\rvert$ ist dort harmonisch — bis auf den Faktor $Q/(4\pi)$ ist sie das Coulomb-Potential
aus dem vorigen Artikel. Also ist das Feld divergenzfrei:

$$\operatorname{div}\frac{\vec x}{\lvert\vec x\rvert^3} = -\operatorname{div}\nabla\frac{1}{\lvert\vec x\rvert} = -\Delta\frac{1}{\lvert\vec x\rvert} = 0.$$

Trotzdem besitzt es dort kein Vektorpotential. Das zeigt erst der Satz von Stokes im Kapitel über Integralsätze: Sein
Fluss durch jede Kugel um den Ursprung ist $4\pi$, der Fluss eines Wirbelfeldes durch eine geschlossene Fläche wäre
null. **Im Bild:** Die Quelle sitzt im Ursprung, und genau diesen Punkt spart das Gebiet aus. Überall sonst quillt
nichts, und doch strömt durch jede Kugel um den Ursprung etwas heraus.

**Eichfreiheit.** Vektorpotentiale sind nicht eindeutig: Mit $\vec A$ ist auch $\vec A+\nabla\psi$ ein Vektorpotential
desselben Feldes, für jedes zweimal stetig differenzierbare Skalarfeld $\psi$. **Im Bild:** Steigungspfeile einer
Landschaft wirbeln nicht — fügt man sie dem Potential hinzu, entsteht kein zusätzlicher Wirbel. Das Gegenstück beim
Skalarpotential ist die Konstante, um die man die ganze Landschaft anheben darf.

:::herleitung
Weil die Rotation eines Gradientenfelds verschwindet (vorheriger Artikel), ist

$$\operatorname{rot}(\vec A+\nabla\psi) = \operatorname{rot}\vec A + \operatorname{rot}\nabla\psi = \operatorname{rot}\vec A = \vec B.$$
:::

**Die Coulomb-Eichung.** Diese Freiheit nutzt man, um ein besonders bequemes Vektorpotential zu wählen — eines ohne
Quellen. Ist $\operatorname{div}\vec A\neq0$ und löst $\psi$ die Poisson-Gleichung

$$\Delta\psi = \operatorname{div}\vec A,$$

so ist das neue Potential $\vec A'=\vec A-\nabla\psi$ quellenfrei und beschreibt dasselbe Feld $\vec B$. In dieser Eichung
vereinfacht sich die rot-rot-Identität:

$$\operatorname{rot}\vec B = \operatorname{rot}\operatorname{rot}\vec A' = -\Delta\vec A'.$$

:::herleitung
Die Divergenz des neuen Potentials ist

$$\operatorname{div}\vec A' = \operatorname{div}\vec A - \operatorname{div}\nabla\psi = \operatorname{div}\vec A - \Delta\psi = 0.$$

Nach der Eichfreiheit beschreibt das neue Potential dasselbe Feld $\vec B$. Mit der rot-rot-Identität und der eben
gezeigten Quellenfreiheit folgt

$$\operatorname{rot}\vec B = \operatorname{rot}\operatorname{rot}\vec A' = \nabla(\operatorname{div}\vec A') - \Delta\vec A' = -\Delta\vec A'.$$

Dass die Poisson-Gleichung tatsächlich eine Lösung hat, zeigt erst das Kapitel über die Integralsätze.
:::

:::grafik
Szene: hoema3/differentialrechnung-vektorfelder/04-eichfreiheit · Vorlage: vektorpotential-eichung-3d
Ein Wirbelfeld $\vec B$ mit mehreren möglichen Vektorpotentialen $\vec A$ und $\vec A'=\vec A-\nabla\psi$, die alle dieselbe
Rotation geben (Eichfreiheit: „$+\nabla\psi$ ändert $\vec B$ nicht"). Hervorgehoben die Coulomb-Eichung
$\operatorname{div}\vec A'=0$ als die „quellenfreie" Wahl; parallel das Spiegelbild: eine Landschaft als
Skalarpotential, die man um eine Konstante anheben darf. (Rot = $\vec B$, orange = verschiedene $\vec A$, grau =
$\nabla\psi$.)
:::

## Bedeutung und Ausblick

Mit diesen Regeln ist die **Differentialrechnung** für Felder vollständig: Gradient, Divergenz, Rotation, Laplace und
ihre Rechenregeln. Sie sind das Handwerkszeug, mit dem man in der Elektrodynamik die Feldgleichungen umformt.

Das schönste Beispiel ist die Wellengleichung. Im ladungsfreien Vakuum gelten die Maxwell-Gleichungen, mit der
Lichtgeschwindigkeit $c$ und der Zeit $t$:

$$\operatorname{rot}\vec E = -\frac{\partial\vec B}{\partial t}, \qquad \operatorname{rot}\vec B = \frac{1}{c^2}\,\frac{\partial\vec E}{\partial t}, \qquad \operatorname{div}\vec E = 0.$$

Bildet man von der ersten Gleichung die Rotation, setzt die zweite ein und benutzt die rot-rot-Identität mit
$\operatorname{div}\vec E=0$, so entsteht

$$-\Delta\vec E = \operatorname{rot}\operatorname{rot}\vec E = -\frac{\partial}{\partial t}\operatorname{rot}\vec B = -\frac{1}{c^2}\,\frac{\partial^2\vec E}{\partial t^2}.$$

Im zweiten Schritt wird die Rotation (Ableitungen nach dem Ort) mit der Zeitableitung vertauscht. Das erlaubt der Satz
von Schwarz, wenn die Felder zweimal stetig differenzierbar sind. Das ist die **Wellengleichung**: Elektromagnetische Wellen — Licht — breiten sich mit der Geschwindigkeit $c$ aus.

$$\Delta\vec E = \frac{1}{c^2}\,\frac{\partial^2\vec E}{\partial t^2}.$$

Als Nächstes kommt die **Integralseite**: zunächst, wie man Integrale differenziert, die von einem Parameter abhängen,
und wie man über mehrdimensionale Bereiche integriert — das Kapitel __Integralrechnung im $\mathbb{R}^n$__.

:::kern
- __Kronecker-Delta__ $\delta_{ij}$ (gleich oder nicht) und __Levi-Civita-Symbol__ $\varepsilon_{ijk}$ (Orientierung) schreiben das Kreuzprodukt kompakt: $(\vec a\times\vec b)_i=\sum\varepsilon_{ijk}a_jb_k$.
- Produktregel Divergenz: $\operatorname{div}(\phi\vec E)=\nabla\phi\cdot\vec E+\phi\operatorname{div}\vec E$ (in jedem $\mathbb{R}^n$) — Farbstoff quillt heraus, weil das Wasser quillt oder weil die Konzentration stromabwärts zunimmt.
- Produktregel Rotation: $\operatorname{rot}(\phi\vec E)=\nabla\phi\times\vec E+\phi\operatorname{rot}\vec E$ (auch eben) — eine Scherströmung wirbelt, obwohl sie geradlinig ist.
- __Spatprodukt__: $\vec a\cdot(\vec b\times\vec c)=\det(\vec a|\vec b|\vec c)$, das orientierte Volumen des Spats, zyklisch vertauschbar.
- __Graßmann__: $\vec a\times(\vec b\times\vec c)=(\vec a\cdot\vec c)\vec b-(\vec a\cdot\vec b)\vec c$ — das Ergebnis liegt in der Ebene von $\vec b$ und $\vec c$.
- Werkzeug dafür: $\sum_k\varepsilon_{ijk}\varepsilon_{klm}=\delta_{il}\delta_{jm}-\delta_{im}\delta_{jl}$.
- Kreuzprodukt-Regel Divergenz: $\operatorname{div}(\vec E\times\vec B)=\vec B\cdot\operatorname{rot}\vec E-\vec E\cdot\operatorname{rot}\vec B$ (Poynting-Satz).
- Kreuzprodukt-Regel Rotation: $\operatorname{rot}(\vec E\times\vec B)=\vec E\operatorname{div}\vec B-\vec B\operatorname{div}\vec E+(\vec B\cdot\nabla)\vec E-(\vec E\cdot\nabla)\vec B$; dabei ist $(\vec E\cdot\nabla)\vec B$ die Ableitung von $\vec B$ in Richtung $\vec E$.
- Ein Wirbel quillt nie: $\operatorname{div}\operatorname{rot}\vec E=0$ (symmetrisch mal antisymmetrisch).
- Doppelte Rotation: $\operatorname{rot}\operatorname{rot}\vec E=\nabla\operatorname{div}\vec E-\Delta\vec E$ — der Schlüssel zur Wellengleichung.
- __Vektorpotential__ $\vec A$ eines Wirbelfeldes: $\vec B=\operatorname{rot}\vec A$. Jedes Wirbelfeld ist quellenfrei (notwendig, nicht hinreichend — Gegenbeispiel Coulomb-Feld).
- __Eichfreiheit__: $\vec A+\nabla\psi$ beschreibt dasselbe $\vec B$, weil Gradientenfelder nicht wirbeln.
- __Coulomb-Eichung__ (quellenfreies Potential): Löst $\psi$ die Poisson-Gleichung $\Delta\psi=\operatorname{div}\vec A$, so ist $\vec A-\nabla\psi$ quellenfrei.
:::

:::quiz
F: Warum hat $\operatorname{div}(\phi\vec E)$ zwei Terme — formal und im Bild des Farbstoffs?
A: Formal wirkt in jedem Summanden $\partial_j(\phi E_j)$ die Produktregel aus HM1; das liefert $\nabla\phi\cdot\vec E+\phi\,\operatorname{div}\vec E$. Im Bild quillt der Farbstofffluss aus zwei Gründen: weil das Wasser selbst quillt, oder weil die Konzentration längs der Strömung zunimmt — dann tritt dünnes Farbwasser ein und dichtes aus (Beispiel $\vec E=(1,0,0)$, $\phi=x$: Divergenz $1$).
F: Wie kann $\operatorname{rot}(\phi\vec E)$ von null verschieden sein, obwohl $\operatorname{rot}\vec E=\vec 0$ ist — am Beispiel $\vec E=(1,0,0)$, $\phi=y$?
A: Der Term $\nabla\phi\times\vec E$ bleibt übrig: $(0,1,0)\times(1,0,0)=(0,0,-1)$. Das gewichtete Feld $(y,0,0)$ ist eine Scherströmung, oben schneller als unten — ein Schaufelrad wird oben stärker angeschoben und dreht sich, obwohl die Strömung geradlinig ist.
F: Was misst das Levi-Civita-Symbol, und wie schreibt man damit das Kreuzprodukt?
A: $\varepsilon_{ijk}$ ist $+1$ für eine rechtshändige Reihenfolge der Achsen, $-1$ für eine linkshändige und $0$, wenn zwei Indizes gleich sind. Damit ist $(\vec a\times\vec b)_i=\sum_{j,k}\varepsilon_{ijk}a_jb_k$; für $i=1$ bleiben genau $a_2b_3-a_3b_2$ übrig.
F: Warum ist das Spatprodukt $\vec a\cdot(\vec b\times\vec c)$ eine Determinante, und was bedeutet es anschaulich?
A: In Indexschreibweise ist es $\sum\varepsilon_{ijk}a_ib_jc_k$ — ausgeschrieben genau die Regel von Sarrus für $\det(\vec a|\vec b|\vec c)$. Anschaulich ist es das orientierte Volumen des schiefen Kastens, den die drei Vektoren aufspannen: Grundfläche $|\vec b\times\vec c|$ mal Höhe.
F: Warum liegt $\vec a\times(\vec b\times\vec c)$ in der Ebene von $\vec b$ und $\vec c$, und wie beweist man die Graßmann-Identität?
A: $\vec b\times\vec c$ steht senkrecht auf dieser Ebene; ein weiteres Kreuzprodukt steht senkrecht auf dieser Normalen und liegt damit wieder in der Ebene. Formal setzt man die Indexformel zweimal ein und benutzt $\sum_k\varepsilon_{ijk}\varepsilon_{klm}=\delta_{il}\delta_{jm}-\delta_{im}\delta_{jl}$; die Deltas lassen $(\vec a\cdot\vec c)\vec b-(\vec a\cdot\vec b)\vec c$ übrig.
F: Warum darf man $\operatorname{div}(\vec E\times\vec B)$ nicht wie ein Spatprodukt einfach zyklisch vertauschen?
A: Dann käme nur $\vec B\cdot\operatorname{rot}\vec E$ heraus. $\nabla$ ist aber auch ein Ableitungsoperator und wirkt nach der Produktregel auf beide Faktoren — daher der zweite Term $-\vec E\cdot\operatorname{rot}\vec B$.
F: Was bedeutet der Ausdruck $(\vec E\cdot\nabla)\vec B$?
A: Er ist $\sum_jE_j\,\partial\vec B/\partial x_j$: die Ableitung des Feldes $\vec B$ in Richtung von $\vec E$, komponentenweise und mit der Länge von $\vec E$ gewichtet. Er beantwortet, wie sich der Pfeil $\vec B$ ändert, wenn man ein Stück in Richtung $\vec E$ geht.
F: Warum ist $\operatorname{div}\operatorname{rot}\vec E=0$ — formal und anschaulich?
A: Formal ist $S=\sum\varepsilon_{ijk}\partial_i\partial_jE_k$; Umbenennen von $i$ und $j$ zeigt mit der Antisymmetrie von $\varepsilon$ und dem Satz von Schwarz $S=-S$, also $S=0$. Anschaulich lässt ein reiner Wirbel das Wasser im Kreis laufen, aus keinem Kästchen strömt netto etwas heraus.
F: Woher kommt $\operatorname{rot}\operatorname{rot}\vec E=\nabla\operatorname{div}\vec E-\Delta\vec E$, und wofür braucht man die Identität?
A: Zweimal die Indexformel der Rotation und die Identität für zwei Levi-Civita-Symbole ergeben $\partial_i(\operatorname{div}\vec E)-\Delta E_i$. Im ladungsfreien Vakuum wird damit aus den Maxwell-Gleichungen die Wellengleichung $\Delta\vec E=\frac{1}{c^2}\partial^2\vec E/\partial t^2$.
F: Was bedeutet Eichfreiheit beim Vektorpotential, und wie erreicht man die Coulomb-Eichung?
A: Mit $\vec A$ ist auch $\vec A+\nabla\psi$ ein Vektorpotential desselben $\vec B$, weil Gradientenfelder nicht wirbeln. Löst $\psi$ die Gleichung $\Delta\psi=\operatorname{div}\vec A$, so ist $\vec A'=\vec A-\nabla\psi$ quellenfrei, und es gilt $\operatorname{rot}\vec B=-\Delta\vec A'$.
:::

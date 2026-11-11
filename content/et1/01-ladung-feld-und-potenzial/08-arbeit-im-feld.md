---
title: Stufe 6: Arbeit im Feld
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Ladung, Feld und Potenzial
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial
knoten: Kapitel 1: Ladung, Feld und Potenzial
order: 1110800
summary: Bewegt sich eine Ladung im Feld, verrichtet die Feldkraft Arbeit.
tags: wirbelfrei, elektrostatisch
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Bewegt sich eine Ladung im Feld, verrichtet die Feldkraft Arbeit. Diese Stufe berechnet sie und zeigt die Eigenschaft, auf der alles Weitere beruht: Die Arbeit hängt nicht vom Weg ab.
:::

**Die Idee.** Eine Ladung im Feld verhält sich wie der Rucksack aus Stufe [1](groen-kraft-und-arbeit.html#stufe-1), die Kraft ist jetzt $Q\vec E$. Läuft eine positive Ladung in Feldrichtung, gibt das Feld Energie an sie ab. Läuft sie dagegen, muss jemand anderes die Arbeit aufbringen, und die Energie wandert ins Feld. Quer zum Feld passiert nichts.

:::satz Satz 6.1 (Arbeit im elektrischen Feld)
<span class="anker" id="satz-6-1"></span>

Geht eine Ladung $Q$ von $P_1$ nach $P_2$, verrichtet das Feld an ihr die Arbeit

<span class="anker" id="gl-6-1"></span>
$$W_{12}=\int_{P_1}^{P_2}\vec F\cdot\mathrm{d}\vec s=Q\int_{P_1}^{P_2}\vec E\cdot\mathrm{d}\vec s,\qquad\text{im homogenen Feld}\quad W_{12}=Q\,E\,s\cos\alpha. \tag{6.1}$$

Im Feld ruhender Ladungen hängt $W_{12}$ nur von $P_1$ und $P_2$ ab, nicht vom Weg. Gleichbedeutend ist das Integral über jeden geschlossenen Weg null, das Feld ist __wirbelfrei__:

<span class="anker" id="gl-6-2"></span>
$$\oint_L\vec E\cdot\mathrm{d}\vec s=0. \tag{6.2}$$
:::

⁠**So liest man das:** $Q$ ist die bewegte Ladung mit Vorzeichen, $s$ die Länge eines geraden Wegs unter dem Winkel $\alpha$ zu $\vec E$. Der Kreis im Integral bedeutet: Der Weg $L$ endet, wo er begann. $W_{12}>0$ heißt, das Feld gibt Energie an die Ladung ab, sie wird *frei*. $W_{12}<0$ heißt, von außen muss $W_\text{außen}=-W_{12}$ aufgewendet werden, sofern die Ladung dabei nicht schneller oder langsamer wird. Bei 1 nC und einigen Volt sind es Nanojoule. **Gültigkeit:** [(6.2)](#gl-6-2) verlangt ruhende Ladungen und kein sich änderndes Magnetfeld (Stufe [10](grenze-des-bildes-magnetismus-und-induktion.html#stufe-10)). Ein solches Feld heißt __elektrostatisch__.

:::herleitung Warum die Arbeit nicht vom Weg abhängt
⁠**Eine Punktladung.** $Q$ laufe im Feld von $Q_0$ von $r_1$ nach $r_2$. Man zerlegt den Weg in Stücke längs des Radius und quer dazu. Quer zum Radius steht das Feld senkrecht zum Weg, es zählt nur die Änderung des Abstands:

$$W_{12}=Q\int_{r_1}^{r_2}k\,\frac{Q_0}{r^2}\,\mathrm{d} r=k\,Q\,Q_0\Bigl(\frac{1}{r_1}-\frac{1}{r_2}\Bigr).$$

⁠**Beliebige ruhende Ladungen.** Jedes solche Feld ist eine Summe von Punktladungsfeldern, die Arbeit die Summe der Einzelarbeiten.

⁠**Geschlossener Weg.** Führt Weg $a$ von $P_1$ nach $P_2$ und Weg $b$ zurück, ändert der Rückweg in umgekehrter Richtung gelesen das Vorzeichen: $\oint\vec E\cdot\mathrm{d}\vec s=\int_a\vec E\cdot\mathrm{d}\vec s-\int_{b,\,P_1\to P_2}\vec E\cdot\mathrm{d}\vec s=0$, weil beide Wege denselben Wert liefern.
:::

:::abbildung et1/k1feldarbeit 7
Ausschnitt des Plattenpaars, maßstäblich. Eine Probeladung $+1$ nC läuft um das Dreieck. Von 1 nach 2 gewinnt sie 9 nJ. Von 2 nach 3 läuft sie quer zum Feld: keine Arbeit. Von 3 nach 1 verliert sie 9 nJ. Der Umlauf ergibt null.
:::

::::beispiel
In Abb. [7](#abb-7) ist $F=Q\,E=3$ µ N in $x$-Richtung und $W_{12}=10^{-9}\,\mathrm{C}\cdot3000\,\mathrm{V/m}\cdot3\,\mathrm{mm}=9$ nJ. Direkt von 1 nach 3 ist der Weg 5 mm lang, mit $\cos\alpha=0{,}6$: wieder 9 nJ. Im Feld von Kugel A ($Q_0=+10$ nC) gewinnt $+1$ nC von 3 cm bis 6 cm die Energie $k\cdot1\,\mathrm{nC}\cdot10\,\mathrm{nC}\cdot(1/r_1-1/r_2)=1{,}5$ µ J.
::::

⁠**Grenzfälle:** Für $\alpha=90^\circ$ und für $P_2=P_1$ ist $W=0$. Bei negativer Ladung kehrt sich das Vorzeichen um: Ein Elektron gewinnt Energie, wenn es gegen $\vec E$ läuft. Für $r_2\to\infty$ bleibt $W_{12}=kQQ_0/r_1$ endlich.

:::frage Hin und zurück ergibt doch immer null. Warum ist das eine besondere Aussage?
Auf demselben Weg hin und zurück stimmt das für jedes Kraftfeld. [(6.2)](#gl-6-2) ist stärker: Es gilt auch, wenn der Rückweg anders verläuft. Sonst könnte man eine Ladung im Kreis laufen lassen und bei jedem Umlauf Energie gewinnen.
:::

:::aufgabe Aufgabe 6 ★★ Wege im Feld
<span class="anker" id="aufg-6"></span>

Im homogenen Feld $E=3$ kV/m in $x$-Richtung läuft $Q=+2$ nC von $P_1=(0;\,0)$ nach $P_2=(2\,\mathrm{mm};\,1{,}5\,\mathrm{mm})$.

<ol class="al">

<li>

Berechne $W_{12}$ auf dem geraden Weg.

</li>

<li>

Berechne $W_{12}$ auf dem Umweg erst in $y$-Richtung, dann in $x$-Richtung.

</li>

<li>

Was ändert sich für $Q=-2$ nC?

</li>

</ol>

:::loesung
(a) Länge $s=\sqrt{2^2+1{,}5^2}\,\mathrm{mm}=2{,}5$ mm, $\cos\alpha=0{,}8$: $W_{12}=2\,\mathrm{nC}\cdot3000\,\mathrm{V/m}\cdot2{,}5\,\mathrm{mm}\cdot0{,}8=12$ nJ. (b) In $y$-Richtung steht der Weg senkrecht zu $\vec E$: 0. In $x$-Richtung: $2\,\mathrm{nC}\cdot3000\,\mathrm{V/m}\cdot2\,\mathrm{mm}=12$ nJ. (c) $W_{12}=-12$ nJ, von außen müssen 12 nJ aufgewendet werden.
:::
:::

::::lernkarten
:::karte formel Arbeit im elektrischen Feld
Welche Arbeit $W_{12}$ verrichtet das Feld an einer Ladung $Q$, die von $P_1$ nach $P_2$ geht?
---
$W_{12}=Q\int_{P_1}^{P_2}\vec E\cdot\mathrm{d}\vec s$, im homogenen Feld $W_{12}=Q\,E\,s\cos\alpha$. $Q$ zählt mit Vorzeichen, $\alpha$ ist der Winkel zwischen Weg und $\vec E$. $W_{12}>0$ heißt: Das Feld gibt Energie an die Ladung ab.
--- falsch
$W_{12}=Q\int_{P_1}^{P_2}\vec E\cdot\mathrm{d}\vec s$, im homogenen Feld $W_{12}=Q\,E\,s\sin\alpha$. $Q$ zählt mit Vorzeichen, $\alpha$ ist der Winkel zwischen Weg und $\vec E$. $W_{12}>0$ heißt: Das Feld gibt Energie an die Ladung ab.
--- falsch
$W_{12}=Q\int_{P_1}^{P_2}\vec E\cdot\mathrm{d}\vec s$, im homogenen Feld $W_{12}=Q\,E\,s\cos\alpha$. $Q$ zählt mit Vorzeichen, $\alpha$ ist der Winkel zwischen Weg und $\vec E$. $W_{12}>0$ heißt: Von außen muss Energie aufgewendet werden.
--- falsch
$W_{12}=\int_{P_1}^{P_2}\vec E\cdot\mathrm{d}\vec s$, im homogenen Feld $W_{12}=E\,s\cos\alpha$. Die Ladung kommt nicht vor, weil das Feld an jeder Ladung dieselbe Arbeit verrichtet. $W_{12}>0$ heißt: Das Feld gibt Energie ab.
:::
:::karte begriff wirbelfrei
Wann heißt ein elektrisches Feld wirbelfrei?
---
Wenn das Integral von $\vec E$ über jeden geschlossenen Weg null ist, $\oint_L\vec E\cdot\mathrm{d}\vec s=0$. Gleichbedeutend hängt die Arbeit an einer Ladung nur von Start und Ziel ab, nicht vom Weg.
--- falsch
Wenn das Integral von $\vec E$ über jeden geschlossenen Weg null ist. Das gilt für jedes elektrische Feld, denn auf einem Umlauf kehrt man zum Start zurück.
--- falsch
Wenn seine Feldlinien nirgends gekrümmt sind. Gekrümmte Linien, wie zwischen zwei ungleichnamigen Ladungen, bilden Wirbel, und die Arbeit hängt dort vom Weg ab.
--- falsch
Wenn $\vec E$ überall null ist. Nur dann hängt die Arbeit an einer Ladung nicht vom Weg ab, weil das Feld auf keinem Weg Arbeit verrichtet.
:::
:::karte begriff elektrostatisches Feld
Was ist ein elektrostatisches Feld?
---
Das elektrische Feld ruhender Ladungen ohne ein sich änderndes Magnetfeld. In ihm gilt $\oint_L\vec E\cdot\mathrm{d}\vec s=0$: Die Arbeit an einer Ladung hängt nicht vom Weg ab.
--- falsch
Ein elektrisches Feld, dessen Betrag und Richtung überall gleich sind. In ihm gilt $W_{12}=Q\,E\,s\cos\alpha$ für jeden geraden Weg, an jedem Ort.
--- falsch
Das elektrische Feld ruhender Ladungen, in dem ruhende Ladungen keine Kraft erfahren. Nur Ladungen, die sich bewegen, spüren dieses Feld.
--- falsch
Das elektrische Feld ruhender Ladungen, in dem die Arbeit an einer Ladung vom gewählten Weg abhängt, nicht nur von Start und Ziel; Umwege kosten mehr Arbeit.
:::
:::karte herleitung Wegunabhängigkeit der Arbeit
Zeige, dass die Arbeit im Feld ruhender Ladungen nicht vom Weg abhängt. Beginne mit einer Ladung $Q$ im Feld einer Punktladung $Q_0$.
---
Man zerlegt den Weg von $r_1$ nach $r_2$ in Stücke längs des Radius und quer dazu, weil sich jeder Weg so beliebig genau annähern lässt.
---
Auf den Stücken quer zum Radius steht das Feld senkrecht zum Weg und verrichtet keine Arbeit, weil $\alpha=90^\circ$ ist. Es zählt nur die Änderung des Abstands.
---
Damit ist $W_{12}=Q\int_{r_1}^{r_2}k\,\frac{Q_0}{r^2}\,\mathrm{d} r=k\,Q\,Q_0\Bigl(\frac{1}{r_1}-\frac{1}{r_2}\Bigr)$, weil $\vec E=k\,\frac{Q_0}{r^2}\cdot\frac{\vec r}{r}$ radial zeigt. Das Ergebnis hängt nur von $r_1$ und $r_2$ ab.
---
Jedes Feld ruhender Ladungen ist eine Summe von Punktladungsfeldern, weil sich Felder überlagern. Die Arbeit ist die Summe der Einzelarbeiten und damit ebenfalls wegunabhängig.
---
Für einen geschlossenen Weg, hin auf $a$ und zurück auf $b$, folgt $\oint\vec E\cdot\mathrm{d}\vec s=\int_a\vec E\cdot\mathrm{d}\vec s-\int_{b,\,P_1\to P_2}\vec E\cdot\mathrm{d}\vec s=0$, weil der Rückweg das Vorzeichen umkehrt und beide Wege denselben Wert liefern.
:::
:::karte zusammenhang Negative Ladung im Feld
Was passiert mit der Arbeit des Felds, wenn statt einer positiven eine negative Ladung denselben Weg läuft?
---
Ihr Vorzeichen kehrt sich um, weil $Q$ mit Vorzeichen in $W_{12}=Q\int_{P_1}^{P_2}\vec E\cdot\mathrm{d}\vec s$ eingeht. Ein Elektron gewinnt deshalb Energie, wenn es gegen $\vec E$ läuft.
--- falsch
Nichts: Die Arbeit hängt nur vom Feld und vom Weg ab. Das Vorzeichen der Ladung legt nur fest, in welche Richtung die Kraft auf sie zeigt.
--- falsch
Nur ihr Betrag: Eine negative Ladung erfährt im selben Feld eine schwächere Kraft, das Feld verrichtet an ihr deshalb weniger Arbeit.
--- falsch
Ihr Vorzeichen kehrt sich um, weil $Q$ mit Vorzeichen eingeht. Ein Elektron gewinnt deshalb Energie, wenn es in Richtung von $\vec E$ läuft.
:::
:::karte zusammenhang Umlauf ohne Energiegewinn
Warum sagt $\oint_L\vec E\cdot\mathrm{d}\vec s=0$ mehr als „hin und zurück ergibt null“?
---
Weil es auch gilt, wenn der Rückweg anders verläuft als der Hinweg; auf demselben Weg ergibt jedes Kraftfeld null. Sonst könnte eine Ladung bei jedem Umlauf Energie gewinnen.
--- falsch
Weil es auch für bewegte Ladungen und sich ändernde Magnetfelder gilt. Es beschreibt damit jedes elektrische Feld ohne Ausnahme, nicht nur das Feld ruhender Ladungen, und ist deshalb allgemeiner.
--- falsch
Weil es zusätzlich verlangt, dass die Ladung auf keinem Teilstück des Wegs Energie gewinnt oder verliert. Auf jedem einzelnen Stück ist die Arbeit null.
--- falsch
Weil es auch für Wege gilt, die nicht zum Start zurückführen. Die Arbeit des Felds ist dann ebenfalls null, gleich an welchem Punkt der Weg endet.
:::
:::karte formel Arbeit von außen
Welche Arbeit muss man von außen aufwenden, wenn das Feld an einer Ladung die Arbeit $W_{12}<0$ verrichtet?
---
$W_\text{außen}=-W_{12}$, sofern die Ladung dabei weder schneller noch langsamer wird. Die aufgewendete Energie wandert ins Feld.
--- falsch
$W_\text{außen}=W_{12}$, also ebenfalls einen negativen Betrag. Die Energie wandert dabei aus dem Feld zur Ladung.
--- falsch
$W_\text{außen}=-W_{12}$, gleich ob die Ladung dabei schneller oder langsamer wird. Die aufgewendete Energie wandert ins Feld.
--- falsch
Keine: Bei $W_{12}<0$ gibt das Feld Energie an die Ladung ab; diese Energie wird frei und treibt die Ladung an.
:::
::::

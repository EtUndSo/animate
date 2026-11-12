---
title: Stufe 8: Ladungserhaltung beim Umschalten
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Der Kondensator
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator
knoten: Kapitel 3: Der Kondensator
order: 1130900
summary: Schaltet man geladene Kondensatoren um, lässt sich die neue Spannung ohne jede Stromrechnung finden.
tags: 
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Schaltet man geladene Kondensatoren um, lässt sich die neue Spannung ohne jede Stromrechnung finden. Es genügt, Ladung zu zählen.
:::

**Die Idee.** In einem abgeschlossenen System bleibt die Summe der Ladungen konstant ([Kapitel 1](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)). In Schaltungen entsteht ein solches System, wenn jeder Pfad von einem Knoten zur Masse über einen Kondensator führt. Das ist die Insel aus Stufe [7](parallel-und-reihenschaltung.html#stufe-7): Die Dielektrika sperren alle Wege. Ladung kann sich innerhalb der Insel umverteilen, aber sie nicht verlassen. Vergleicht man vorher und nachher, muss man nicht wissen, wie der Ausgleich verlief.

:::satz Satz 8.1 (Ladungserhaltung auf einer Insel)
<span class="anker" id="satz-8-1"></span>

Führt jeder Pfad von einem Knoten nach Masse über eine Kapazität, bleibt die Summe der Ladungen auf den angeschlossenen Platten konstant:

<span class="anker" id="gl-8-1"></span>
$$Q_\mathrm{ges}=\sum_iC_iU_i=\text{const}. \tag{8.1}$$
:::

⁠**So liest man das:** $U_i$ ist die Spannung vom Knoten zur Gegenplatte, $C_iU_i$ also die Ladung der Platte am Knoten, mit Vorzeichen. Der Vergleich gilt zwischen zwei Ruhezuständen, $Q=C\,U$ liefert die Spannungen. **Gültigkeit:** Am Knoten darf kein Widerstand und keine Quelle nach außen hängen, und der Ausgleich muss schnell gegen die Selbstentladung sein.

:::abbildung et1/k3umladen 8
Stellung 1: $C_1$ lädt sich auf 9 V, $C_2$ ist leer. Stellung 2: Die gestrichelte Insel enthält die oberen Platten beider Kondensatoren. Die 900 µC verteilen sich, bis beide Spannungen gleich sind.
:::

::::beispiel
In Abb. [8](#abb-8) trägt $C_1$ in Stellung 1 die Ladung $C_1U_0=900\,\mu\text{C}$, und $C_2$ ist leer. Der Schalter geht auf Stellung 2. Beide oberen Platten hängen nun an einem Draht, also gilt nach dem Ausgleich dieselbe Spannung $U$. Aus [(8.1)](#gl-8-1) folgt

<span class="anker" id="gl-8-2"></span>
$$C_1U+C_2U=C_1U_0\quad\Longrightarrow\quad U=U_0\,\frac{C_1}{C_1+C_2}=9\,\mathrm{V}\cdot\frac{100}{150}=6\,\mathrm{V}. \tag{8.2}$$

Danach trägt $C_1$ noch 600 µC, $C_2$ hat 300 µC erhalten.
::::

**Die Energie bleibt nicht erhalten.** Vorher sind $\frac12C_1U_0^2=4{,}05$ mJ gespeichert, nachher $\frac12(C_1+C_2)U^2=2{,}70$ mJ. Es fehlen 1,35 mJ, ein Drittel. Der Ausgleichsstrom erwärmt die Leitungen und den Schalter. Der Verlust hängt nicht von deren Widerstand ab: Ein kleinerer Widerstand ergibt einen größeren Strom für kürzere Zeit, und beides hebt sich genau auf. Allgemein gehen beim Ausgleich zweier Spannungen $U_1$ und $U_2$ verloren:

<span class="anker" id="gl-8-3"></span>
$$W_\mathrm{V}=\frac12\,\frac{C_1C_2}{C_1+C_2}\,(U_1-U_2)^2. \tag{8.3}$$

:::herleitung Verlust beim Ausgleich
Mit $U=\frac{C_1U_1+C_2U_2}{C_1+C_2}$ aus [(8.1)](#gl-8-1) ist

$$W_\mathrm{V}=\tfrac12C_1U_1^2+\tfrac12C_2U_2^2-\tfrac12\,\frac{(C_1U_1+C_2U_2)^2}{C_1+C_2}.$$

Auf dem Hauptnenner $2(C_1+C_2)$ heben sich $C_1^2U_1^2$ und $C_2^2U_2^2$ auf. Im Zähler bleibt $C_1C_2(U_1^2-2U_1U_2+U_2^2)$, das ist [(8.3)](#gl-8-3).
:::

⁠**Grenzfälle:** Für $C_2\to0$ bleibt $U=U_0$, und nichts geht verloren. Für $C_2\gg C_1$ geht $U\to0$: Die Ladung verschwindet nicht, verteilt sich aber auf einen so großen Kondensator, dass kaum Spannung bleibt.

:::frage Beim Laden in Stellung 1 ändert sich die Ladung doch auch. Warum gilt die Erhaltung dort nicht?
Weil dort keine Insel vorliegt. Der Knoten hängt über die Batterie direkt an der Masse, das ist ein Pfad ohne Kapazität. Durch ihn fließt die Ladung zu. Die Erhaltung gilt immer für das Ganze, aber [(8.1)](#gl-8-1) braucht einen Knoten, den alle Wege über Dielektrika verlassen.
:::

:::ltspice Umladen über einen Widerstand
⁠**Zeichnen:** `cap` mit `100u` von `a` nach Masse, Anfangswert `IC=9`. `cap` mit `50u` von `b` nach Masse, Anfangswert `IC=0`. `res` mit `{Rv}` von `a` nach `b`. Dieser Widerstand steht für Leitungen und Schalter.

⁠**Direktiven:** `.param Rv=10`, `.step param Rv list 1 10 100`, `.tran 0 100m 0 1u uic`, dazu `.meas tran ua FIND V(a) AT=100m` und `.meas tran wr INTEG V(a,b)*I(R1)`. Das Ergebnis steht im SPICE Error Log.

⁠**Was du siehst:** Für alle drei Widerstände ist `ua` $=6$ V und `wr` $=1{,}35$ mJ, wie in [(8.2)](#gl-8-2) und [(8.3)](#gl-8-3). Nur die Zeit des Ausgleichs ändert sich. Setze `IC=3` an $C_2$ und vergleiche mit Aufgabe [9](#aufg-9)(a).
:::

:::aufgabe Aufgabe 9 ★★ Umladen mit Vorladung
<span class="anker" id="aufg-9"></span>

$C_1=100\,\mu\text{F}$ trägt 9 V. Dann wird $C_2=50\,\mu\text{F}$ zugeschaltet, das schon geladen ist.

<ol class="al">

<li>

$C_2$ trägt $+3$ V, gleichsinnig mit $C_1$. Wie groß ist die Endspannung? Wie viel Energie geht verloren?

</li>

<li>

$C_2$ trägt $-3$ V, also verpolt. Wie groß sind nun Endspannung und Verlust?

</li>

<li>

Grenzfall: Was ergibt sich für $U_2=9$ V, und warum fließt kein Ausgleichsstrom?

</li>

</ol>

:::loesung
(a) $Q=100\,\mu\text{F}\cdot9\,\mathrm{V}+50\,\mu\text{F}\cdot3\,\mathrm{V}=1050\,\mu\text{C}$, $U=1050\,\mu\text{C}/150\,\mu\text{F}=7$ V. Verlust nach [(8.3)](#gl-8-3): $\frac12\cdot33{,}3\,\mu\text{F}\cdot(9\,\mathrm{V}-3\,\mathrm{V})^2=0{,}60$ mJ. Probe: vorher 4,275 mJ, nachher 3,675 mJ.

(b) $Q=900\,\mu\text{C}-150\,\mu\text{C}=750\,\mu\text{C}$, $U=5$ V. Verlust: $\frac12\cdot33{,}3\,\mu\text{F}\cdot(12\,\mathrm{V})^2=2{,}40$ mJ. Die Differenz der Spannungen ist 12 V, nicht 6 V.

(c) $U=9$ V, $W_\mathrm{V}=0$. Beide Knoten liegen schon auf demselben Potenzial, also treibt nichts einen Strom.
:::
:::

::::formelsammlung
**Ladungserhaltung auf einer Insel**

$$Q_\mathrm{ges}=\sum_iC_iU_i=\text{const}$$

$U_i$ Spannung vom Knoten zur Gegenplatte, $C_iU_i$ Ladung der Platte am Knoten mit Vorzeichen. Gilt, wenn jeder Pfad vom Knoten nach Masse über eine Kapazität führt, also kein Widerstand und keine Quelle nach außen hängt, und der Ausgleich schnell gegen die Selbstentladung ist. Verglichen werden zwei Ruhezustände.

**Spannung nach dem Umladen**

$$C_1U+C_2U=C_1U_0\quad\Longrightarrow\quad U=U_0\,\frac{C_1}{C_1+C_2}$$

$C_1$ auf $U_0$ geladen, $C_2$ leer; danach liegt an beiden dieselbe Spannung $U$.

**Ausgleich zweier Spannungen**

$$U=\frac{C_1U_1+C_2U_2}{C_1+C_2}$$

Gemeinsame Spannung, wenn $C_1$ mit $U_1$ und $C_2$ mit $U_2$ verbunden werden; die Spannungen zählen mit Vorzeichen.

**Verlust beim Ausgleich**

$$W_\mathrm{V}=\frac12\,\frac{C_1C_2}{C_1+C_2}\,(U_1-U_2)^2$$

Die Energie bleibt nicht erhalten, der Ausgleichsstrom erwärmt Leitungen und Schalter. Der Verlust hängt nicht von deren Widerstand ab: Kleinerer Widerstand ergibt größeren Strom für kürzere Zeit.
::::

::::lernkarten
:::karte formel Ladungserhaltung auf einer Insel
Welche Größe bleibt beim Umschalten geladener Kondensatoren an einem Knoten konstant, und unter welcher Bedingung?
---
$Q_\mathrm{ges}=\sum_iC_iU_i=\text{const}$, die Summe der Ladungen der Platten am Knoten. Bedingung: Jeder Pfad vom Knoten nach Masse führt über eine Kapazität.
--- falsch
$W_\mathrm{ges}=\sum_i\frac12C_iU_i^2=\text{const}$, die Summe der gespeicherten Energien am Knoten. Bedingung: Jeder Pfad vom Knoten nach Masse führt über eine Kapazität.
--- falsch
$Q_\mathrm{ges}=\sum_iC_iU_i=\text{const}$, die Summe der Ladungen am Knoten. Bedingung: Der Knoten hängt über eine Quelle direkt an der Masse, die die Ladung dort festhält.
--- falsch
$U_\mathrm{ges}=\sum_iU_i=\text{const}$, die Summe der Spannungen vom Knoten zu den Gegenplatten. Bedingung: Jeder Pfad vom Knoten nach Masse führt über eine Kapazität.
:::
:::karte zusammenhang Ladung zählen statt Strom rechnen
Warum kann man die Spannung nach dem Umschalten geladener Kondensatoren finden, ohne den Verlauf des Ausgleichsstroms zu kennen?
---
Weil die Insel abgeschlossen ist: Die Dielektrika sperren alle Wege, die Ladung verteilt sich nur um. Es genügt, die Ruhezustände vorher und nachher zu vergleichen; $Q=C\,U$ liefert die Spannungen.
--- falsch
Weil der Ausgleichsstrom immer gleich groß ist, gleich welche Kondensatoren beteiligt sind und wie sie geladen sind; man kennt ihn deshalb schon vor dem Umschalten und kann ihn einfach einsetzen.
--- falsch
Weil die Energie beim Umschalten erhalten bleibt; aus der Energie vorher folgt mit $W=\frac12\,C\,U^2$ direkt die gemeinsame Spannung nachher, ohne jede Stromrechnung.
--- falsch
Weil beim Umschalten gar kein Strom fließt; die Spannungen springen sofort auf ihre neuen Werte, und die Ladung bleibt dabei jeweils auf ihrer eigenen Platte sitzen, wo sie vorher war.
:::
:::karte formel Spannung nach dem Umladen
Welche gemeinsame Spannung $U$ stellt sich ein, wenn ein auf $U_0$ geladener Kondensator $C_1$ mit einem leeren Kondensator $C_2$ verbunden wird?
---
$U=U_0\,\frac{C_1}{C_1+C_2}$, aus $C_1U+C_2U=C_1U_0$: Die Ladung von $C_1$ verteilt sich auf beide, bis beide Spannungen gleich sind.
--- falsch
$U=U_0/2$: Die Spannung halbiert sich immer, weil sich die Ladung zu gleichen Teilen auf die beiden Kondensatoren verteilt, gleich wie groß sie sind.
--- falsch
$U=U_0\,\frac{C_2}{C_1+C_2}$, aus der Ladungserhaltung: Je größer der leere Kondensator, desto höher die gemeinsame Spannung danach.
--- falsch
$U=U_0$: Beide tragen danach die volle Spannung, weil $C_1$ wie eine Quelle wirkt, die ihre Spannung festhält, während sie Ladung abgibt.
:::
:::karte zusammenhang Energie beim Umladen
Was geschieht mit der gespeicherten Energie, wenn ein geladener Kondensator mit einem leeren verbunden wird?
---
Sie bleibt nicht erhalten: Mit $C_1=100\,\mu\text{F}$ und $C_2=50\,\mu\text{F}$ fehlt nachher ein Drittel. Der Ausgleichsstrom erwärmt Leitungen und Schalter.
--- falsch
Sie bleibt erhalten, weil auch die Ladung erhalten bleibt; die Energie verteilt sich nur auf die beiden Kondensatoren, im Verhältnis ihrer Kapazitäten.
--- falsch
Sie wächst, weil nun zwei Kondensatoren Energie speichern statt einem; den Zuwachs liefert das Feld des zweiten, der vorher leer war.
--- falsch
Sie geht nur verloren, wenn Leitungen und Schalter einen Widerstand haben; bei idealen Drähten bliebe sie vollständig erhalten.
:::
:::karte formel Verlust beim Ausgleich
Wie viel Energie geht verloren, wenn sich zwei Kondensatoren mit den Spannungen $U_1$ und $U_2$ ausgleichen?
---
$W_\mathrm{V}=\frac12\,\frac{C_1C_2}{C_1+C_2}\,(U_1-U_2)^2$: Der Verlust wächst mit dem Quadrat der Spannungsdifferenz und ist null, wenn beide Spannungen schon gleich sind.
--- falsch
$W_\mathrm{V}=\frac12\,\frac{C_1C_2}{C_1+C_2}\,(U_1^2-U_2^2)$: Der Verlust ist null, wenn beide Spannungen gleich groß sind, auch dann, wenn ihre Vorzeichen entgegengesetzt sind.
--- falsch
$W_\mathrm{V}=\frac12\,(C_1+C_2)\,(U_1-U_2)^2$: Der Verlust wächst mit der Summe der beiden Kapazitäten und dem Quadrat der Spannungsdifferenz.
--- falsch
$W_\mathrm{V}=\frac12\,\frac{C_1C_2}{C_1+C_2}\,(U_1-U_2)$: Der Verlust wächst linear mit der Spannungsdifferenz und ist null, wenn beide Spannungen gleich sind.
:::
:::karte zusammenhang Verlust unabhängig vom Widerstand
Warum hängt der Energieverlust beim Ausgleich zweier Kondensatoren nicht vom Widerstand der Leitungen ab?
---
Ein kleinerer Widerstand ergibt einen größeren Strom für kürzere Zeit, und beides hebt sich genau auf. Der Widerstand bestimmt nur, wie lange der Ausgleich dauert.
--- falsch
Weil ideale Leitungen gar keinen Widerstand haben; der ganze Verlust entsteht allein im Schalter, dessen Widerstand bei jedem Umschalten derselbe ist, gleich wie man schaltet.
--- falsch
Weil der Ausgleichsstrom durch die Dielektrika fließt und nicht durch die Leitungen; die Wärme entsteht deshalb im Isolator, dessen Widerstand fest ist.
--- falsch
Weil der Ausgleichsstrom allein durch die Spannungsdifferenz festgelegt ist, gleich wie groß der Widerstand ist; deshalb entsteht immer dieselbe Wärme.
:::
:::karte herleitung Verlust beim Ausgleich
Leite aus der Ladungserhaltung her, dass beim Ausgleich zweier Kondensatoren die Energie $W_\mathrm{V}=\frac12\,\frac{C_1C_2}{C_1+C_2}\,(U_1-U_2)^2$ verloren geht.
---
Die Endspannung ist $U=\frac{C_1U_1+C_2U_2}{C_1+C_2}$, weil die Summe der Ladungen auf der Insel erhalten bleibt und danach beide dieselbe Spannung haben.
---
Der Verlust ist $W_\mathrm{V}=\tfrac12C_1U_1^2+\tfrac12C_2U_2^2-\tfrac12\,\frac{(C_1U_1+C_2U_2)^2}{C_1+C_2}$, weil er die Energie vorher minus die Energie nachher ist und jeder Kondensator $\frac12CU^2$ speichert.
---
Auf dem Hauptnenner $2(C_1+C_2)$ heben sich $C_1^2U_1^2$ und $C_2^2U_2^2$ auf, weil sie in der Energie vorher und im Quadrat der Summe gleich vorkommen.
---
Im Zähler bleibt $C_1C_2(U_1^2-2U_1U_2+U_2^2)$, also das Quadrat $(U_1-U_2)^2$, weil das die binomische Formel ist.
:::
:::karte zusammenhang Keine Insel beim Laden
Warum gilt die Ladungserhaltung am Knoten nicht, solange $C_1$ über die Batterie geladen wird?
---
Weil dort keine Insel vorliegt: Der Knoten hängt über die Batterie direkt an der Masse, ein Pfad ohne Kapazität, durch den Ladung zufließt.
--- falsch
Weil die Ladungserhaltung nur gilt, solange kein Strom fließt; beim Laden fließt Strom, und dabei entsteht am Knoten ständig neue Ladung aus dem Draht.
--- falsch
Weil $C_1$ beim Laden noch keine Spannung hat; die Erhaltung gilt erst, wenn alle angeschlossenen Kondensatoren geladen sind.
--- falsch
Sie gilt dort doch: Die Ladung am Knoten bleibt auch beim Laden konstant, nur ihre Verteilung auf die Platten ändert sich.
:::
:::karte zusammenhang Grenzfälle des Umladens
Was ergibt das Umladen, wenn der leere Kondensator $C_2$ sehr viel größer ist als $C_1$, und was, wenn er sehr klein ist?
---
Für $C_2\gg C_1$ geht $U\to0$: Die Ladung verschwindet nicht, verteilt sich aber auf einen so großen Kondensator, dass kaum Spannung bleibt. Für $C_2\to0$ bleibt $U=U_0$, nichts geht verloren.
--- falsch
Für $C_2\gg C_1$ geht $U\to U_0$, weil der große Kondensator die Spannung festhält und $C_1$ nichts abgeben muss. Für $C_2\to0$ geht $U\to0$, weil die Ladung über den kleinen abfließt.
--- falsch
Für $C_2\gg C_1$ geht die Ladung verloren, weil sie sich im großen Kondensator auflöst und dort nicht mehr messbar ist. Für $C_2\to0$ halbiert sich die Spannung, wie bei jedem Umladen.
--- falsch
In beiden Fällen halbiert sich die Spannung, weil sich die Ladung beim Umladen stets zu gleichen Teilen auf beide Kondensatoren aufteilt, gleich wie groß der zweite ist.
:::
::::

---
title: Stufe 4: Leitungsverluste
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Leistung, Anpassung und Wirkungsgrad
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/leistung-anpassung-und-wirkungsgrad
knoten: Kapitel 7: Leistung, Anpassung und Wirkungsgrad
order: 1170500
summary: Zwischen Quelle und Last liegt die Leitung, und auch sie ist ein Widerstand.
tags: Spannungsabfall, Verlustleistung, Nutzleistung, Nennspannung
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Zwischen Quelle und Last liegt die Leitung, und auch sie ist ein Widerstand. Diese Stufe zeigt, warum große Leistungen über hohe Spannungen laufen.
:::

**Die Idee.** Die Leitung liegt in Reihe mit der Last, der ganze Strom muss durch sie (Abb. [5](#abb-5)). Jedes Coulomb verliert in ihr $R_\mathrm{Kabel}I$ Joule, bevor es die Last erreicht. Eine feste Leistung lässt sich auf zwei Arten übertragen: mit hoher Spannung und kleinem Strom oder umgekehrt. Bei hoher Spannung bringt jedes Coulomb viel Energie mit, also genügen wenige. Der kleine Strom hilft doppelt: Jedes Coulomb verliert weniger, und es sind weniger.

:::abbildung et1/k7leitung 5
Quelle, Leitung und Last. $R_\mathrm{Kabel}$ fasst Hin- und Rückleiter zusammen. Rechts die zwei Fälle des Beispiels.
:::

:::satz Satz 4.1 (Leitungsverluste)
<span class="anker" id="satz-4-1"></span>

Fließt der Strom $I$ über eine Leitung mit $R_\mathrm{Kabel}$ zur Last, gelten

<span class="anker" id="gl-4-1"></span>
$$U_\mathrm{Kabel}=R_\mathrm{Kabel}\,I,\qquad P_\mathrm{Kabel}=U_\mathrm{Kabel}\,I=R_\mathrm{Kabel}\,I^2,\qquad P_\mathrm{Nutz}=(U_\mathrm{q}-U_\mathrm{Kabel})\,I \tag{4.1}$$

und damit

<span class="anker" id="gl-4-2"></span>
$$\frac{P_\mathrm{Nutz}}{P_\mathrm{q}}=\frac{(U_\mathrm{q}-U_\mathrm{Kabel})\,I}{U_\mathrm{q}\,I}=1-\frac{U_\mathrm{Kabel}}{U_\mathrm{q}}. \tag{4.2}$$

Für zwei Spannungen mit gleicher Lastleistung $P_\mathrm{L}=U_\mathrm{L1}I_1=U_\mathrm{L2}I_2$ gilt

<span class="anker" id="gl-4-3"></span>
$$\frac{I_1}{I_2}=\frac{U_\mathrm{L2}}{U_\mathrm{L1}},\qquad\frac{P_\mathrm{Kabel,1}}{P_\mathrm{Kabel,2}}=\left(\frac{U_\mathrm{L2}}{U_\mathrm{L1}}\right)^{\!2}. \tag{4.3}$$
:::

⁠**So liest man das:** $U_\mathrm{Kabel}$ ist der __Spannungsabfall__ längs der Leitung. $P_\mathrm{Kabel}$ ist die __Verlustleistung__, $P_\mathrm{Nutz}=P_\mathrm{L}$ die __Nutzleistung__ der Last, $P_\mathrm{q}=U_\mathrm{q}I$ die Leistung der Quelle. $U_\mathrm{L}$ ist die Spannung an der Last. **Gültigkeit:** Die Formeln gelten für Gleichgrößen und für den Widerstand der Leitung. Bei Wechselspannung und ohmscher Last gelten sie mit Effektivwerten.

::::beispiel
Die Last braucht 40 kW, $R_\mathrm{Kabel}=1\,\Omega$. Bei $U_\mathrm{L}=400$ V sind $I=100$ A, $U_\mathrm{Kabel}=100$ V und $P_\mathrm{Kabel}=10$ kW. Die Quelle muss 500 V liefern, nach [(4.2)](#gl-4-2) kommen $1-100/500=80$ % an. Bei 20 kV sind $I=2$ A, $U_\mathrm{Kabel}=2$ V und $P_\mathrm{Kabel}=4$ W, es kommen 99,99 % an. Der Strom sinkt um den Faktor 50, der Verlust um $50^2=2500$.
::::

⁠**Grenzfall:** Für $R_\mathrm{Kabel}\to0$ wird $U_\mathrm{Kabel}=0$ und [(4.2)](#gl-4-2) ergibt 1. Über längere Strecken ist Energie nur bei hoher Spannung zu übertragen, deshalb baut man das Netz in Ebenen. Die __Nennspannung__ ist die Spannung, für die ein Netz ausgelegt ist:

| Ebene | Nennspannung | Reichweite | Aufgabe |
|---|---|---|---|
| Niederspannung | 230/400 V | einige 100 m | Haushalte und Gewerbe im Ort |
| Mittelspannung | 10 kV | bis rund 10 km | Verteilung in Großstädten |
| Mittelspannung | 20 kV | bis rund 25 km | Verteilung auf dem Land und in Mittelstädten |
| Hochspannung | 110 kV | bis rund 100 km | Versorgung der Mittelspannungsnetze |
| Höchstspannung | 220 kV, 380 kV | einige 100 bis über 1000 km | Verbund im Land und in Europa |

Bis in die Wohnung lässt sich Hochspannung nicht führen: Luft schlägt bei rund 3 kV/mm durch ([Kapitel 1](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)), Freileitungen brauchen deshalb Abstände von mehreren Metern. Transformatoren setzen die Wechselspannung für den Transport herauf und vor den Verbrauchern wieder herab.

:::frage Nach $P=U^2/R$ wächst die Leistung mit der Spannung. Müssten höhere Spannungen nicht mehr Verlust bringen?
Die Formel stimmt, aber sie braucht die Spannung am selben Widerstand. Am Kabel liegen im Beispiel nicht 20 kV, sondern $U_\mathrm{Kabel}=2$ V, und $(2\,\mathrm{V})^2/1\,\Omega$ sind die 4 W. Die hohe Spannung liegt an der Last. $U_\mathrm{Kabel}$ sinkt, weil der Strom sinkt.
:::

:::aufgabe Aufgabe 4 ★★ Die Hütte am Waldrand
<span class="anker" id="aufg-4"></span>

Eine Hütte nimmt 480 W bei 48 V Gleichspannung auf, die Zuleitung hat $R_\mathrm{Kabel}=0{,}2\,\Omega$. (a) Berechne $I$, $U_\mathrm{Kabel}$, $P_\mathrm{Kabel}$, $U_\mathrm{q}$ und den Anteil, der ankommt. (b) Dasselbe für 480 W bei 12 V. (c) Welche Spannung $U_\mathrm{L}$ begrenzt den Verlust auf 1 % der Lastleistung?

:::loesung
(a) $I=480\,\mathrm{W}/48\,\mathrm{V}=10$ A, $U_\mathrm{Kabel}=2$ V, $P_\mathrm{Kabel}=20$ W, $U_\mathrm{q}=50$ V. Es kommen $1-2/50=96$ % an. (b) $I=40$ A, $U_\mathrm{Kabel}=8$ V, $P_\mathrm{Kabel}=320$ W, $U_\mathrm{q}=20$ V. Es kommen nur 60 % an. Vierfacher Strom ergibt sechzehnfachen Verlust. (c) $R_\mathrm{Kabel}\,P_\mathrm{L}^2/U_\mathrm{L}^2\le0{,}01\,P_\mathrm{L}$ ergibt $U_\mathrm{L}\ge\sqrt{R_\mathrm{Kabel}\,P_\mathrm{L}/0{,}01}=98$ V.
:::
:::

::::formelsammlung
**Leitungsverluste**

$$U_\mathrm{Kabel}=R_\mathrm{Kabel}\,I,\qquad P_\mathrm{Kabel}=U_\mathrm{Kabel}\,I=R_\mathrm{Kabel}\,I^2,\qquad P_\mathrm{Nutz}=(U_\mathrm{q}-U_\mathrm{Kabel})\,I$$

$R_\mathrm{Kabel}$ fasst Hin- und Rückleiter zusammen. $U_\mathrm{Kabel}$ Spannungsabfall längs der Leitung, $P_\mathrm{Kabel}$ Verlustleistung, $P_\mathrm{Nutz}=P_\mathrm{L}$ Nutzleistung der Last. Für Gleichgrößen; bei Wechselspannung und ohmscher Last mit Effektivwerten.

**Anteil, der ankommt**

$$\frac{P_\mathrm{Nutz}}{P_\mathrm{q}}=\frac{(U_\mathrm{q}-U_\mathrm{Kabel})\,I}{U_\mathrm{q}\,I}=1-\frac{U_\mathrm{Kabel}}{U_\mathrm{q}}$$

$P_\mathrm{q}=U_\mathrm{q}I$ ist die Leistung der Quelle. Für $R_\mathrm{Kabel}\to0$ wird der Anteil 1.

**Gleiche Lastleistung bei zwei Spannungen**

$$P_\mathrm{L}=U_\mathrm{L1}I_1=U_\mathrm{L2}I_2,\qquad\frac{I_1}{I_2}=\frac{U_\mathrm{L2}}{U_\mathrm{L1}},\qquad\frac{P_\mathrm{Kabel,1}}{P_\mathrm{Kabel,2}}=\left(\frac{U_\mathrm{L2}}{U_\mathrm{L1}}\right)^{\!2}$$

$U_\mathrm{L}$ ist die Spannung an der Last. Gleiche Leistung bei $n$-facher Spannung senkt den Leitungsverlust auf $1/n^2$.
::::

::::lernkarten
:::karte begriff Spannungsabfall
Was bezeichnet man als Spannungsabfall längs einer Leitung, über die der Strom $I$ zur Last fließt, und wie groß ist er?
---
Die Spannung $U_\mathrm{Kabel}=R_\mathrm{Kabel}\,I$ am Widerstand der Leitung. Um sie liegt an der Last weniger an, als die Quelle liefert: Jedes Coulomb verliert in der Leitung $R_\mathrm{Kabel}I$ Joule.
--- falsch
Die Spannung an der Last, also $U_\mathrm{q}-R_\mathrm{Kabel}\,I$. Sie heißt so, weil die Energie der Coulomb in der Last „abfällt“; längs der Leitung selbst fällt keine Spannung ab.
--- falsch
Die Abnahme der Quellenspannung, wenn die Leitung länger wird. Sie hängt nur von der Länge der Leitung ab, nicht vom Strom, und ist $U_\mathrm{Kabel}=R_\mathrm{Kabel}\,U_\mathrm{q}$.
--- falsch
Die Spannung $U_\mathrm{Kabel}=R_\mathrm{Kabel}\,I$ am Widerstand der Leitung. Sie geht der Last nicht verloren, weil die Leitung in Reihe liegt und die Last diese Spannung noch zusätzlich erhält.
:::
:::karte begriff Verlustleistung
Was ist die Verlustleistung einer Leitung zwischen Quelle und Last, und wie hängt sie vom Strom ab?
---
Die Leistung, die im Widerstand der Leitung zu Wärme wird und die Last nicht erreicht: $P_\mathrm{Kabel}=U_\mathrm{Kabel}\,I=R_\mathrm{Kabel}\,I^2$. Sie wächst mit dem Quadrat des Stroms.
--- falsch
Die Leistung, die die Last wegen ihres eigenen Widerstands nicht nutzen kann: $P_\mathrm{Kabel}=R_\mathrm{L}\,I^2$. Sie wächst mit dem Quadrat des Stroms und mit der Last.
--- falsch
Die Leistung, die im Widerstand der Leitung zu Wärme wird: $P_\mathrm{Kabel}=R_\mathrm{Kabel}\,I$. Sie wächst linear mit dem Strom, weil jedes Coulomb dieselbe Energie verliert.
--- falsch
Die Leistung, die im Widerstand der Leitung zu Wärme wird: $P_\mathrm{Kabel}=U_\mathrm{q}\,I$. Sie hängt von der Quellenspannung ab, weil die ganze Spannung am Kabel anliegt.
:::
:::karte begriff Nutzleistung
Was bezeichnet die Nutzleistung bei der Übertragung über eine Leitung, und wie berechnet man sie aus Quellenspannung und Spannungsabfall?
---
Die Leistung $P_\mathrm{L}$, die an der Last ankommt und dort genutzt wird: $P_\mathrm{Nutz}=(U_\mathrm{q}-U_\mathrm{Kabel})\,I$, die Leistung der Quelle abzüglich des Verlusts in der Leitung.
--- falsch
Die Leistung, die die Quelle abgibt: $P_\mathrm{Nutz}=U_\mathrm{q}\,I$. Sie kommt vollständig an der Last an, weil die Leitung den Strom nur weiterleitet und nichts davon behält.
--- falsch
Die Leistung, die in der Leitung zu Wärme wird und deshalb nicht genutzt werden kann: $P_\mathrm{Nutz}=U_\mathrm{Kabel}\,I$, also der Teil, den die Quelle umsonst liefert.
--- falsch
Die Leistung, die an der Last ankommt: $P_\mathrm{Nutz}=(U_\mathrm{q}+U_\mathrm{Kabel})\,I$, weil sich die Spannungen von Quelle und Leitung in der Reihenschaltung addieren.
:::
:::karte begriff Nennspannung
Was gibt die Nennspannung eines Netzes an, und welche Nennspannungen haben die Ebenen des Stromnetzes?
---
Die Spannung, für die ein Netz ausgelegt ist. Niederspannung 230/400 V, Mittelspannung 10 oder 20 kV, Hochspannung 110 kV, Höchstspannung 220 und 380 kV.
--- falsch
Die höchste Spannung, die im Netz kurz auftreten darf, bevor die Sicherung auslöst. Niederspannung 400 V, Mittelspannung 1 kV, Hochspannung 10 kV, Höchstspannung 110 kV.
--- falsch
Die Spannung, die nach Abzug des Spannungsabfalls an der Last ankommt. Niederspannung 230 V, Mittelspannung 2 kV, Hochspannung 20 kV, Höchstspannung 200 kV.
--- falsch
Die Spannung, für die ein Netz ausgelegt ist. Sie ist in allen Ebenen gleich, 230 V, damit jedes Gerät überall angeschlossen werden kann; nur die Ströme unterscheiden sich.
:::
:::karte formel Anteil der Leistung, der ankommt
Welcher Anteil der Quellenleistung kommt bei einer Leitung mit dem Spannungsabfall $U_\mathrm{Kabel}$ an der Last an?
---
$\frac{P_\mathrm{Nutz}}{P_\mathrm{q}}=1-\frac{U_\mathrm{Kabel}}{U_\mathrm{q}}$, mit $P_\mathrm{q}=U_\mathrm{q}I$. Der Strom kürzt sich, weil Leitung und Last denselben Strom führen. Bei 100 V Abfall von 500 V kommen 80 % an.
--- falsch
$\frac{P_\mathrm{Nutz}}{P_\mathrm{q}}=\frac{U_\mathrm{Kabel}}{U_\mathrm{q}}$, mit $P_\mathrm{q}=U_\mathrm{q}I$. Der Strom kürzt sich, weil Leitung und Last denselben Strom führen. Bei 100 V Abfall von 500 V kommen also nur 20 % an.
--- falsch
$\frac{P_\mathrm{Nutz}}{P_\mathrm{q}}=1-\left(\frac{U_\mathrm{Kabel}}{U_\mathrm{q}}\right)^2$, weil der Verlust quadratisch mit dem Strom wächst. Bei 100 V Abfall von 500 V kommen 96 % an.
--- falsch
$\frac{P_\mathrm{Nutz}}{P_\mathrm{q}}=1-\frac{U_\mathrm{Kabel}}{U_\mathrm{q}}$. Das gilt nur bei Gleichspannung; bei Wechselspannung kommt stets mehr an, weil der Strom nur zeitweise fließt.
:::
:::karte formel Gleiche Leistung bei zwei Spannungen
Wie verhalten sich Strom und Leitungsverlust, wenn dieselbe Lastleistung einmal bei der Lastspannung $U_\mathrm{L1}$ und einmal bei $U_\mathrm{L2}$ übertragen wird?
---
$\frac{I_1}{I_2}=\frac{U_\mathrm{L2}}{U_\mathrm{L1}}$ und $\frac{P_\mathrm{Kabel,1}}{P_\mathrm{Kabel,2}}=\left(\frac{U_\mathrm{L2}}{U_\mathrm{L1}}\right)^{\!2}$. Gleiche Leistung bei $n$-facher Spannung senkt den Leitungsverlust auf $1/n^2$.
--- falsch
$\frac{I_1}{I_2}=\frac{U_\mathrm{L2}}{U_\mathrm{L1}}$ und $\frac{P_\mathrm{Kabel,1}}{P_\mathrm{Kabel,2}}=\frac{U_\mathrm{L2}}{U_\mathrm{L1}}$. Gleiche Leistung bei $n$-facher Spannung senkt den Leitungsverlust auf $1/n$, wie den Strom.
--- falsch
$\frac{I_1}{I_2}=\frac{U_\mathrm{L1}}{U_\mathrm{L2}}$ und $\frac{P_\mathrm{Kabel,1}}{P_\mathrm{Kabel,2}}=\left(\frac{U_\mathrm{L1}}{U_\mathrm{L2}}\right)^{\!2}$. Gleiche Leistung bei $n$-facher Spannung erhöht den Leitungsverlust auf das $n^2$-Fache.
--- falsch
Der Strom bleibt gleich, weil die Last ihn bestimmt, und $\frac{P_\mathrm{Kabel,1}}{P_\mathrm{Kabel,2}}=1$. Die Spannung entscheidet nur darüber, wie stark man die Leitung isolieren muss.
:::
:::karte zusammenhang Kleiner Strom hilft doppelt
Warum senkt eine höhere Übertragungsspannung bei gleicher Leistung die Leitungsverluste mit dem Quadrat und nicht nur proportional?
---
Bei hoher Spannung bringt jedes Coulomb viel Energie mit, also genügen wenige. Der kleine Strom hilft doppelt: Jedes Coulomb verliert in der Leitung weniger, nämlich $R_\mathrm{Kabel}I$, und es sind weniger.
--- falsch
Weil eine hohe Spannung die Leitung zusätzlich kühlt: Das stärkere Feld treibt die Elektronen schneller hindurch, sodass ihnen auf dem Weg durch die Leitung weniger Zeit für Stöße mit dem Gitter bleibt.
--- falsch
Weil der Widerstand der Leitung mit der Spannung sinkt: Bei doppelter Spannung halbiert er sich, und zusammen mit dem halben Strom ergibt das ein Viertel des Verlusts.
--- falsch
Weil die Spannung am Kabel mit der Übertragungsspannung steigt und nach $P=U^2/R$ quadratisch eingeht; da der Strom zugleich sinkt, bleibt am Ende das Quadrat übrig.
:::
:::karte zusammenhang Hohe Spannung und Leitungsverlust
Warum bringt eine höhere Übertragungsspannung weniger Verlust in der Leitung, obwohl nach $P=U^2/R$ die Leistung mit der Spannung wächst?
---
Die Formel braucht die Spannung am selben Widerstand. Am Kabel liegt nicht die hohe Spannung, sondern $U_\mathrm{Kabel}$, und sie sinkt, weil der Strom sinkt. Die hohe Spannung liegt an der Last.
--- falsch
Weil $P=U^2/R$ nur für Gleichspannung gilt. Bei Wechselspannung zählt der Effektivwert, und der ist bei hohen Spannungen so viel kleiner, dass der Verlust insgesamt sinkt.
--- falsch
Die Formel gilt hier, aber der Widerstand der Leitung wächst bei hoher Spannung so stark, dass $U^2/R$ trotzdem kleiner wird. Deshalb sind Hochspannungsleitungen dünn.
--- falsch
Weil die hohe Spannung nur an der Quelle anliegt. Bis zur Last ist sie längs der Leitung schon fast ganz abgefallen, deshalb liegt am Kabel im Mittel nur eine kleine Spannung an.
:::
:::karte zusammenhang Netz in Ebenen
Warum führt man die Hochspannung nicht bis in die Wohnung, sondern baut das Stromnetz in Ebenen mit verschiedenen Nennspannungen auf?
---
Über längere Strecken lässt sich Energie nur bei hoher Spannung übertragen. In der Wohnung ginge das nicht, weil Luft bei rund 3 kV/mm durchschlägt; Transformatoren setzen die Spannung vorher herab.
--- falsch
Weil Hochspannung nur über Freileitungen fließen kann, nicht durch Erdkabel. In der Stadt muss man deshalb auf Niederspannung wechseln; die Transformatoren dafür arbeiten mit Gleichspannung.
--- falsch
Weil hohe Spannungen auf langen Leitungen höhere Verluste bringen als niedrige. Man nutzt die Hochspannung deshalb nur auf kurzen Strecken und überbrückt weite Entfernungen mit Niederspannung.
--- falsch
Weil Geräte nur für 230 V gebaut werden. Technisch ließe sich Hochspannung ohne Weiteres bis in die Wohnung führen, sie brächte dort aber keinen Vorteil, weil die Leitungen kurz sind.
:::
::::

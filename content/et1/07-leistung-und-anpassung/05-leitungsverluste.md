---
title: Stufe 4: Leitungsverluste
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Leistung, Anpassung und Wirkungsgrad
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

**Beispiel.** Die Last braucht 40 kW, $R_\mathrm{Kabel}=1\,\Omega$. Bei $U_\mathrm{L}=400$ V sind $I=100$ A, $U_\mathrm{Kabel}=100$ V und $P_\mathrm{Kabel}=10$ kW. Die Quelle muss 500 V liefern, nach [(4.2)](#gl-4-2) kommen $1-100/500=80$ % an. Bei 20 kV sind $I=2$ A, $U_\mathrm{Kabel}=2$ V und $P_\mathrm{Kabel}=4$ W, es kommen 99,99 % an. Der Strom sinkt um den Faktor 50, der Verlust um $50^2=2500$. **Grenzfall:** Für $R_\mathrm{Kabel}\to0$ wird $U_\mathrm{Kabel}=0$ und [(4.2)](#gl-4-2) ergibt 1. Über längere Strecken ist Energie nur bei hoher Spannung zu übertragen, deshalb baut man das Netz in Ebenen. Die __Nennspannung__ ist die Spannung, für die ein Netz ausgelegt ist:

| Ebene | Nennspannung | Reichweite | Aufgabe |
|---|---|---|---|
| Niederspannung | 230/400 V | einige 100 m | Haushalte und Gewerbe im Ort |
| Mittelspannung | 10 kV | bis rund 10 km | Verteilung in Großstädten |
| Mittelspannung | 20 kV | bis rund 25 km | Verteilung auf dem Land und in Mittelstädten |
| Hochspannung | 110 kV | bis rund 100 km | Versorgung der Mittelspannungsnetze |
| Höchstspannung | 220 kV, 380 kV | einige 100 bis über 1000 km | Verbund im Land und in Europa |

Bis in die Wohnung lässt sich Hochspannung nicht führen: Luft schlägt bei rund 3 kV/mm durch ([Teil 1](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)), Freileitungen brauchen deshalb Abstände von mehreren Metern. Transformatoren setzen die Wechselspannung für den Transport herauf und vor den Verbrauchern wieder herab.

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

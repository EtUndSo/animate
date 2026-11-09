---
title: Stufe 5: Wohin die Leistung einer Quelle geht
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Leistung, Anpassung und Wirkungsgrad
order: 1170600
summary: Auch die Quelle hat einen Widerstand in sich.
tags: 
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Auch die Quelle hat einen Widerstand in sich. Diese Stufe stellt die Bilanz auf und definiert den Wirkungsgrad.
:::

**Die Idee.** In der Quelle bekommt jedes Coulomb die Energie $U_\mathrm{q}$ in Joule, weil die Chemie es gegen das Feld zum höheren Potenzial schiebt. Einen Teil $U_\mathrm{Ri}$ verliert es in $R_\mathrm{i}$ als Wärme, den Rest $U_\mathrm{L}$ gibt es in der Last ab (Abb. [6](#abb-6)). Dann ist es wieder am Ausgangspunkt. Alle Coulomb machen dieselbe Runde, also bestimmt das Verhältnis der Spannungen, welcher Anteil der Leistung ankommt.

:::abbildung et1/k7kreis 6
Links die Quelle an der Last. Rechts das Potenzial einer Ladung auf dem Umlauf für $R_\mathrm{L}=16\,\Omega$, mit B als Bezugspunkt. Die Quelle hebt sie um 9 V, $R_\mathrm{i}$ nimmt 1 V, die Last 8 V.
:::

:::definition Definition 5.1 (Leistungsbilanz und Wirkungsgrad)
<span class="anker" id="satz-5-1"></span>

Im Stromkreis mit $I=U_\mathrm{q}/(R_\mathrm{i}+R_\mathrm{L})$ gelten

<span class="anker" id="gl-5-1"></span>
$$P_\mathrm{q}=U_\mathrm{q}\,I,\qquad P_\mathrm{v}=U_\mathrm{Ri}\,I=I^2R_\mathrm{i},\qquad P_\mathrm{L}=U_\mathrm{L}\,I=I^2R_\mathrm{L},\qquad P_\mathrm{q}=P_\mathrm{v}+P_\mathrm{L}. \tag{5.1}$$

Der Wirkungsgrad ist die genutzte Leistung, bezogen auf die gesamte aufgewendete Leistung der Quelle:

<span class="anker" id="gl-5-2"></span>
$$\eta=\frac{P_\mathrm{L}}{P_\mathrm{q}}=\frac{I\,U_\mathrm{L}}{I\,U_\mathrm{q}}=\frac{U_\mathrm{L}}{U_\mathrm{q}}=\frac{R_\mathrm{L}}{R_\mathrm{L}+R_\mathrm{i}}=\frac{R_\mathrm{L}/R_\mathrm{i}}{1+R_\mathrm{L}/R_\mathrm{i}}. \tag{5.2}$$
:::

⁠**So liest man das:** $P_\mathrm{q}$ ist die Leistung, die die Quelle erzeugt, $P_\mathrm{v}$ die Verlustleistung in ihrem Innenwiderstand, $P_\mathrm{L}$ die Nutzleistung. $U_\mathrm{Ri}=R_\mathrm{i}I$ ist die Spannung an $R_\mathrm{i}$. $\eta$ ist eine reine Zahl zwischen 0 und 1 und hängt nur vom Verhältnis $R_\mathrm{L}/R_\mathrm{i}$ ab. **Gültigkeit:** Das gilt für die Reihenschaltung aus idealer Quelle, $R_\mathrm{i}$ und $R_\mathrm{L}$. Bei einer Ersatzquelle stimmen die inneren Größen nicht (Stufe [7](warum-50-und-welches-ziel-gilt.html#stufe-7)).

:::herleitung Die Bilanz ist die Maschenregel mal Strom
Die Maschenregel lautet $U_\mathrm{q}=U_\mathrm{Ri}+U_\mathrm{L}$. Multipliziert mit $I$ ergibt sie $P_\mathrm{q}=P_\mathrm{v}+P_\mathrm{L}$. In [(5.2)](#gl-5-2) kürzt sich $I$, denn beide Widerstände führen denselben Strom. Der Spannungsteiler ([Teil 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)) liefert $U_\mathrm{L}=U_\mathrm{q}\,R_\mathrm{L}/(R_\mathrm{L}+R_\mathrm{i})$.
:::

::::beispiel
Die Batterie an vier Lasten:

| $R_\mathrm{L}$ in $\Omega$ | $I$ in A | $U_\mathrm{L}$ in V | $P_\mathrm{L}$ in W | $P_\mathrm{v}$ in W | $P_\mathrm{q}$ in W | $\eta$ |
|---|---|---|---|---|---|---|
| 0,5 | 3,6 | 1,8 | 6,48 | 25,92 | 32,4 | 20 % |
| 2 | 2,25 | 4,5 | 10,125 | 10,125 | 20,25 | 50 % |
| 8 | 0,9 | 7,2 | 6,48 | 1,62 | 8,1 | 80 % |
| 16 | 0,5 | 8 | 4 | 0,5 | 4,5 | 88,9 % |
::::

⁠**Grenzfälle:** Im Kurzschluss $R_\mathrm{L}=0$ ist $\eta=0$: Die Last bleibt kalt, die ganze Leistung $P_\mathrm{q}=40{,}5$ W heizt $R_\mathrm{i}$. Im Leerlauf $R_\mathrm{L}\to\infty$ geht $\eta\to1$, doch $I\to0$ und damit $P_\mathrm{L}\to0$.

:::frage Der Wirkungsgrad steigt mit $R_\mathrm{L}$ immer weiter. Warum macht man die Last nicht beliebig groß?
Weil $\eta$ ein Anteil ist und keine Menge. Bei großem $R_\mathrm{L}$ gibt jedes Coulomb fast alles in der Last ab, aber es kommen kaum noch Coulomb. Die Tabelle zeigt es: Von 8 $\Omega$ nach 16 $\Omega$ steigt $\eta$, die Leistung $P_\mathrm{L}$ sinkt.
:::

:::aufgabe Aufgabe 5 ★ Bilanz aufstellen
<span class="anker" id="aufg-5"></span>

Eine Quelle hat $U_\mathrm{q}=12$ V und $R_\mathrm{i}=3\,\Omega$. (a) Berechne für $R_\mathrm{L}=9\,\Omega$ alle Größen aus [(5.1)](#gl-5-1) und $\eta$. (b) Welche Last ergibt $\eta=90$ %, und was kommt dann an? (c) Was geschieht im Kurzschluss?

:::loesung
(a) $I=12\,\mathrm{V}/12\,\Omega=1$ A, $U_\mathrm{Ri}=3$ V, $U_\mathrm{L}=9$ V, $P_\mathrm{q}=12$ W, $P_\mathrm{v}=3$ W, $P_\mathrm{L}=9$ W, $\eta=75$ %. (b) $R_\mathrm{L}/(R_\mathrm{L}+3\,\Omega)=0{,}9$ ergibt $R_\mathrm{L}=27\,\Omega$, $I=0{,}4$ A, $P_\mathrm{L}=4{,}32$ W. (c) $I_\mathrm{KS}=4$ A, alle 48 W entstehen in $R_\mathrm{i}$, $\eta=0$.
:::
:::

---
title: Stufe 7: Warum 50 %, und welches Ziel gilt
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Leistung, Anpassung und Wirkungsgrad
order: 1170800
summary: Das Leistungsmaximum verschwendet die Hälfte.
tags: 
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Das Leistungsmaximum verschwendet die Hälfte. Diese Stufe zeigt, warum das zwangsläufig so ist, und wann man es trotzdem will.
:::

**Die Idee.** Aus $\eta=U_\mathrm{L}/U_\mathrm{q}$ und der Quellengeraden folgt: Der Wirkungsgrad fällt linear mit dem Strom, denn je mehr Strom, desto mehr Spannung bleibt in $R_\mathrm{i}$. Die Leistung der Quelle $P_\mathrm{q}=U_\mathrm{q}I$ steigt dagegen linear mit dem Strom. An der Last kommt das Produkt an, $P_\mathrm{L}=P_\mathrm{q}\,\eta$. Das Produkt einer steigenden und einer fallenden Geraden ist eine Parabel mit dem Scheitel in der Mitte, und dort steht die fallende Gerade auf halber Höhe (Abb. [8](#abb-8)). Die 50 % sind weder Zufall noch eine Materialfrage.

:::satz Satz 7.1 (Leistung und Wirkungsgrad)
<span class="anker" id="satz-7-1"></span>

Teilt man $U_\mathrm{L}=U_\mathrm{q}-R_\mathrm{i}I$ durch $U_\mathrm{q}$, folgt mit $x=I/I_\mathrm{KS}$

<span class="anker" id="gl-7-1"></span>
$$\eta=1-x,\qquad\frac{P_\mathrm{L}}{P_\mathrm{KS}}=x\,\eta=x(1-x). \tag{7.1}$$

Bei Leistungsanpassung ist $x=\frac12$, also $\eta=\frac12$.
:::

⁠**So liest man das:** $x$ ist der Strom als Bruchteil des Kurzschlussstroms, $\eta$ der Bruchteil der Energie je Coulomb, der die Last erreicht. **Kurz gesagt:** Am Leistungsmaximum gibt jede Ladung die eine Hälfte ihrer Energie in der Quelle ab und die andere in der Last. **Gültigkeit:** wie Stufe [5](wohin-die-leistung-einer-quelle-geht.html#stufe-5). **Grenzfälle:** $x=0$ ist der Leerlauf mit $\eta=1$, $x=1$ der Kurzschluss mit $\eta=0$. In beiden ist $P_\mathrm{L}=0$.

:::abbildung et1/k7kurven 8
Links: Leistung an der Last und Wirkungsgrad über $R_\mathrm{L}/R_\mathrm{i}$. Das Leistungsmaximum liegt bei 1, dort ist $\eta=0{,}5$. Rechts dieselben Kurven über dem Strom: $\eta$ wird zur Geraden, die Leistung zur Parabel. Normiert ist auf $P_\mathrm{L,max}=P_\mathrm{KS}/4$.
:::

**Drei Ziele.** Welcher Betrieb richtig ist, hängt davon ab, was zählt.

| Anpassung | Bedingung | Ergebnis | $\eta$ | Einsatz |
|---|---|---|---|---|
| Spannung | $R_\mathrm{L}\gg R_\mathrm{i}$ | $U_\mathrm{L}\approx U_\mathrm{q}$, kaum lastabhängig | nahe 1 | Stromnetz, Batterie, Spannungsmesser |
| Strom | $R_\mathrm{L}\ll R_\mathrm{i}$ | $I\approx I_\mathrm{KS}$, kaum lastabhängig | nahe 0 | Strommesser, Stromquellen |
| Leistung | $R_\mathrm{L}=R_\mathrm{i}$ | $P_\mathrm{L}$ maximal | $\frac12$ | Antennen, Signalverarbeitung |

::::beispiel [Beispiele]
An der Batterie ergibt $R_\mathrm{L}=200\,\Omega$ die Spannung 8,91 V, 99 % von $U_\mathrm{q}$. Mit $R_\mathrm{L}=0{,}02\,\Omega$ fließen 4,46 A, 99 % von $I_\mathrm{KS}$. Der Schritt von 2 $\Omega$ auf 8 $\Omega$ kostet 36 % der Leistung und senkt die Wärme in der Batterie auf 16 %.
::::

⁠**Energietechnik.** Die Leistungen liegen im kW-Bereich, jede Wärme in der Quelle kostet Geld und gefährdet sie. Man will hohen Wirkungsgrad, also $R_\mathrm{i}\ll R_\mathrm{L}$. Ein Werkzeug-Akku mit 18 V und 60 m$\Omega$ erreicht beim Anlauf mit 120 A noch $\eta=1-7{,}2\,\mathrm{V}/18\,\mathrm{V}=60$ %, innen entstehen $(120\,\mathrm{A})^2\cdot60\,\mathrm{m\Omega}=864$ W. Eine Arbeitsleuchte mit 1,8 W wirkt wie 180 $\Omega$, und $\eta=180/180{,}06=99{,}97$ %. Anpassung bedeutete hier 1350 W Wärme im Akku.

⁠**Nachrichtentechnik.** Die Leistungen liegen im µ W-Bereich. Ein Empfänger kann nur nehmen, was die Antenne anbietet. Es zählt die absolute Leistung, nicht der Anteil, und die Wärme in der Quelle schadet nicht. Eine Antenne mit 10 mV und 50 $\Omega$ gibt an 50 $\Omega$ genau 0,5 µ W ab, an 5 $\Omega$ oder 500 $\Omega$ nur 0,165 µ W.

**Ersatzquellen: Das Maximum bleibt, die 50 % nicht.** Oft ist die Quelle ein Netz. Abb. [9](#abb-9) zeigt eine Quelle mit $R_\mathrm{q}$ und parallel dazu $R$. Bezüglich der Klemmen A, B ist es eine Ersatzquelle ([Teil 5](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)) mit $R_\mathrm{i}=R_\mathrm{q}\parallel R$ und $U_\mathrm{LL}=U_\mathrm{q}R/(R_\mathrm{q}+R)$. Für die Last zählt nur die Klemmengerade, also liegt das Maximum bei $R_\mathrm{L}=R_\mathrm{i}$, mit

<span class="anker" id="gl-7-2"></span>
$$U_\mathrm{L}=U_\mathrm{q}\,\frac{R}{2(R_\mathrm{q}+R)},\qquad P_\mathrm{L}=\frac{U_\mathrm{L}^2}{R_\mathrm{L}}=\frac{U_\mathrm{q}^2\,R}{4\,R_\mathrm{q}(R_\mathrm{q}+R)}. \tag{7.2}$$

Die echte Quelle arbeitet aber auf $R_\mathrm{ges}=R_\mathrm{q}+R\parallel R_\mathrm{L}$, und dabei ergibt sich

<span class="anker" id="gl-7-3"></span>
$$P_\mathrm{q}=\frac{U_\mathrm{q}^2}{R_\mathrm{ges}}=\frac{U_\mathrm{q}^2\,(2R_\mathrm{q}+R)}{2R_\mathrm{q}(R_\mathrm{q}+R)},\qquad\eta=\frac{P_\mathrm{L}}{P_\mathrm{q}}=\frac12\,\frac{R}{2R_\mathrm{q}+R}<\frac12\quad\text{für }R<\infty. \tag{7.3}$$

:::abbildung et1/k7netz 9
Links das Netz bei Anpassung mit den wirklichen Leistungen. Rechts seine Ersatzquelle. Für die Last sind beide gleich, in der Quelle nicht.
:::

:::herleitung Die Umformungen zu [(7.3)](#gl-7-3)
Mit $R_\mathrm{L}=R_\mathrm{q}R/(R_\mathrm{q}+R)$ ist $R\parallel R_\mathrm{L}=R^2R_\mathrm{q}/(R^2+2R_\mathrm{q}R)=R\,R_\mathrm{q}/(R+2R_\mathrm{q})$. Das ergibt $R_\mathrm{ges}=2R_\mathrm{q}(R_\mathrm{q}+R)/(2R_\mathrm{q}+R)$. Allgemein gilt der Spannungsteiler $U_\mathrm{L}=U_\mathrm{q}(R\parallel R_\mathrm{L})/R_\mathrm{ges}=U_\mathrm{q}\,R\,R_\mathrm{L}/\bigl(R_\mathrm{q}(R+R_\mathrm{L})+R\,R_\mathrm{L}\bigr)$. Einsetzen ergibt die Formel in [(7.2)](#gl-7-2). Damit ist $P_\mathrm{L}=U_\mathrm{L}^2(R_\mathrm{q}+R)/(R_\mathrm{q}R)$. Der Quotient aus $P_\mathrm{L}$ und $P_\mathrm{q}$ kürzt sich auf [(7.3)](#gl-7-3).
:::

::::beispiel
Für $U_\mathrm{q}=18$ V, $R_\mathrm{q}=6\,\Omega$ und $R=3\,\Omega$ sind $R_\mathrm{i}=2\,\Omega$ und $U_\mathrm{LL}=6$ V. Bei $R_\mathrm{L}=2\,\Omega$ liegen 3 V an der Last, sie bekommt 4,5 W. Durch $R_\mathrm{q}$ fließen 2,5 A, davon 1 A durch $R$. Das ergibt 37,5 W in $R_\mathrm{q}$, 3 W in $R$, zusammen mit der Last $P_\mathrm{q}=45$ W und $\eta=10$ %. Die Ersatzquelle zeigt scheinbar 50 %, denn sie sagt über das Innere nichts aus. Der Strom durch $R$ fließt auch ohne Last, schon im Leerlauf heizt das Netz mit 36 W.
::::

⁠**Grenzfall:** Für $R\to\infty$ fällt dieser Zweig weg, und [(7.3)](#gl-7-3) ergibt wieder $\eta=\frac12$.

:::frage Heißt $\eta=50$ % am Maximum, dass ich mit Anpassung die Hälfte der Energie „verliere“?
Bei einer Quelle mit echtem Innenwiderstand ja, sie heizt sich so stark wie die Last. Bei kleiner Leistung ist das tragbar. Wo Energie teuer oder die Quelle empfindlich ist, arbeitet man weit rechts vom Maximum.
:::

:::aufgabe Aufgabe 7 ★ Welches Ziel liegt vor?
<span class="anker" id="aufg-7"></span>

Ordne zu und rechne nach: (a) Ein Spannungsmesser mit 10 M$\Omega$ an der Batterie. Wie viel weicht die Anzeige von 9 V ab? (b) Ein Strommesser mit 0,1 $\Omega$ in einem Kreis aus 5 V und 1 k$\Omega$. Um wie viel Prozent ändert er den Strom? (c) Ein Netzteil mit 12 V und 50 m$\Omega$ an 6 $\Omega$. Wie groß ist $\eta$? (d) Was ergäbe am selben Netzteil Leistungsanpassung?

:::loesung
(a) Spannungsanpassung: $R_\mathrm{L}\gg R_\mathrm{i}$. Es fließen 0,9 µ A, innen fallen 1,8 µ V ab. (b) Stromanpassung: Die Quelle wirkt hochohmig. Der Strom sinkt von 5 mA um 0,01 %. (c) Spannungsanpassung: $\eta=6/6{,}05=99{,}2$ %. (d) $R_\mathrm{L}=50$ m$\Omega$ ergäbe 720 W an der Last und 720 W im Netzteil, das wäre zerstörerisch.
:::
:::

:::aufgabe Aufgabe 8 ★★★ Das Netz bei Anpassung
<span class="anker" id="aufg-8"></span>

Eine Quelle mit $U_\mathrm{q}=24$ V und $R_\mathrm{q}=4\,\Omega$ wird mit $R=12\,\Omega$ belastet, die Last liegt parallel zu $R$. (a) Bestimme $R_\mathrm{i}$ und $U_\mathrm{LL}$. (b) Berechne $U_\mathrm{L}$ und $P_\mathrm{L}$ bei Anpassung. (c) Berechne $P_\mathrm{q}$ und $\eta$, einmal aus den Strömen, einmal mit [(7.3)](#gl-7-3). (d) Wie groß muss $R$ sein, damit $\eta=45$ % wird?

:::loesung
(a) $R_\mathrm{i}=4\,\Omega\parallel12\,\Omega=3\,\Omega$, $U_\mathrm{LL}=24\,\mathrm{V}\cdot12/16=18$ V. (b) $U_\mathrm{L}=9$ V, $P_\mathrm{L}=(9\,\mathrm{V})^2/3\,\Omega=27$ W $=U_\mathrm{LL}^2/(4R_\mathrm{i})$. (c) 3 A durch die Last, 0,75 A durch $R$, also 3,75 A aus der Quelle. $P_\mathrm{q}=90$ W $=56{,}25\,\mathrm{W}+6{,}75\,\mathrm{W}+27\,\mathrm{W}$, $\eta=30$ %, wie $\frac12\cdot12/20$. (d) $\frac12R/(8\,\Omega+R)=0{,}45$ ergibt $R=72\,\Omega$.
:::
:::

---
title: Stufe 7: Warum 50 %, und welches Ziel gilt
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Leistung, Anpassung und Wirkungsgrad
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/leistung-anpassung-und-wirkungsgrad
knoten: Kapitel 7: Leistung, Anpassung und Wirkungsgrad
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

**Ersatzquellen: Das Maximum bleibt, die 50 % nicht.** Oft ist die Quelle ein Netz. Abb. [9](#abb-9) zeigt eine Quelle mit $R_\mathrm{q}$ und parallel dazu $R$. Bezüglich der Klemmen A, B ist es eine Ersatzquelle ([Kapitel 5](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)) mit $R_\mathrm{i}=R_\mathrm{q}\parallel R$ und $U_\mathrm{LL}=U_\mathrm{q}R/(R_\mathrm{q}+R)$. Für die Last zählt nur die Klemmengerade, also liegt das Maximum bei $R_\mathrm{L}=R_\mathrm{i}$, mit

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

::::formelsammlung
**Wirkungsgrad und Leistung über dem Strom**

$$\eta=1-x,\qquad\frac{P_\mathrm{L}}{P_\mathrm{KS}}=x\,\eta=x(1-x)$$

$x=I/I_\mathrm{KS}$; folgt aus $U_\mathrm{L}=U_\mathrm{q}-R_\mathrm{i}I$, geteilt durch $U_\mathrm{q}$. Bei Leistungsanpassung ist $x=\frac12$, also $\eta=\frac12$ (Antennen, Signalverarbeitung). $x=0$ ist der Leerlauf mit $\eta=1$, $x=1$ der Kurzschluss mit $\eta=0$, in beiden ist $P_\mathrm{L}=0$. Gilt für die Reihenschaltung aus idealer Quelle, $R_\mathrm{i}$ und $R_\mathrm{L}$.

**Spannungsanpassung**

$$R_\mathrm{L}\gg R_\mathrm{i},\qquad U_\mathrm{L}\approx U_\mathrm{q}$$

Spannung kaum lastabhängig, $\eta$ nahe 1. Einsatz: Stromnetz, Batterie, Spannungsmesser; allgemein die Energietechnik.

**Stromanpassung**

$$R_\mathrm{L}\ll R_\mathrm{i},\qquad I\approx I_\mathrm{KS}$$

Strom kaum lastabhängig, $\eta$ nahe 0. Einsatz: Strommesser, Stromquellen.

**Ersatzquelle eines Netzes**

$$R_\mathrm{i}=R_\mathrm{q}\parallel R,\qquad U_\mathrm{LL}=U_\mathrm{q}R/(R_\mathrm{q}+R)$$

Quelle $U_\mathrm{q}$ mit $R_\mathrm{q}$ und dem Widerstand $R$ parallel zu den Klemmen A, B.

**Netz bei Leistungsanpassung**

$$U_\mathrm{L}=U_\mathrm{q}\,\frac{R}{2(R_\mathrm{q}+R)},\qquad P_\mathrm{L}=\frac{U_\mathrm{L}^2}{R_\mathrm{L}}=\frac{U_\mathrm{q}^2\,R}{4\,R_\mathrm{q}(R_\mathrm{q}+R)}$$

Last $R_\mathrm{L}=R_\mathrm{i}$. Das Maximum liegt richtig, weil für die Last nur die Klemmengerade zählt.

**Leistung der echten Quelle bei Anpassung**

$$R_\mathrm{ges}=R_\mathrm{q}+R\parallel R_\mathrm{L},\qquad P_\mathrm{q}=\frac{U_\mathrm{q}^2}{R_\mathrm{ges}}=\frac{U_\mathrm{q}^2\,(2R_\mathrm{q}+R)}{2R_\mathrm{q}(R_\mathrm{q}+R)}$$

Die echte Quelle arbeitet auf $R_\mathrm{ges}$, nicht auf $R_\mathrm{i}+R_\mathrm{L}$; der Strom durch $R$ fließt auch ohne Last.

**Wirkungsgrad des Netzes**

$$\eta=\frac{P_\mathrm{L}}{P_\mathrm{q}}=\frac12\,\frac{R}{2R_\mathrm{q}+R}<\frac12\quad\text{für }R<\infty$$

Die Ersatzquelle zeigt scheinbar 50 %, denn sie sagt über das Innere nichts aus. Für $R\to\infty$ wird wieder $\eta=\frac12$.
::::

::::lernkarten
:::karte begriff Spannungsanpassung
Was versteht man unter Spannungsanpassung einer Last an eine Quelle, und wo setzt man sie ein?
---
Den Betrieb mit $R_\mathrm{L}\gg R_\mathrm{i}$, bei dem die Quelle eine feste Spannung liefert: $U_\mathrm{L}\approx U_\mathrm{q}$, kaum lastabhängig, und $\eta$ nahe 1. Einsatz: Stromnetz, Batterie, Spannungsmesser.
--- falsch
Den Betrieb mit $R_\mathrm{L}\ll R_\mathrm{i}$, bei dem die Quelle eine feste Spannung liefert: $U_\mathrm{L}\approx U_\mathrm{q}$, kaum lastabhängig, und $\eta$ nahe 0. Einsatz: Strommesser, Stromquellen.
--- falsch
Den Betrieb mit $R_\mathrm{L}=R_\mathrm{i}$, bei dem an der Last genau die halbe Quellenspannung liegt: $U_\mathrm{L}=U_\mathrm{q}/2$, und $\eta=\frac12$. Einsatz: Stromnetz, Batterie, Spannungsmesser.
--- falsch
Das Nachregeln der Quellenspannung, bis die Last ihre Nennspannung erhält: $U_\mathrm{q}$ wird erhöht, bis $U_\mathrm{L}$ stimmt, und $\eta$ bleibt dabei gleich. Einsatz: Netzteile und Ladegeräte.
:::
:::karte begriff Stromanpassung
Was versteht man unter Stromanpassung einer Last an eine Quelle, und wo setzt man sie ein?
---
Den Betrieb mit $R_\mathrm{L}\ll R_\mathrm{i}$, bei dem die Quelle einen festen Strom liefert: $I\approx I_\mathrm{KS}$, kaum lastabhängig, und $\eta$ nahe 0. Einsatz: Strommesser, Stromquellen.
--- falsch
Den Betrieb mit $R_\mathrm{L}\gg R_\mathrm{i}$, bei dem die Quelle einen festen Strom liefert: $I\approx I_\mathrm{KS}$, kaum lastabhängig, und $\eta$ nahe 1. Einsatz: Spannungsmesser, Batterien.
--- falsch
Den Betrieb mit $R_\mathrm{L}\ll R_\mathrm{i}$, bei dem die Quelle einen festen Strom liefert: $I\approx I_\mathrm{KS}$, und $\eta$ nahe 1, weil an der Last kaum Spannung verloren geht. Einsatz: Stromnetz.
--- falsch
Die Wahl des Leitungsquerschnitts passend zum Strom der Last, damit die Leitung nicht überlastet wird: $I\le I_\mathrm{max}$, und $\eta$ bleibt nahe 1. Einsatz: Hausinstallation.
:::
:::karte formel Leistung und Wirkungsgrad über dem Strom
Wie hängen Wirkungsgrad und Lastleistung vom Strombruchteil $x=I/I_\mathrm{KS}$ ab, und welcher Wirkungsgrad gehört zur Leistungsanpassung?
---
$\eta=1-x$ und $\frac{P_\mathrm{L}}{P_\mathrm{KS}}=x\,\eta=x(1-x)$. Bei Leistungsanpassung ist $x=\frac12$, also $\eta=\frac12$. Im Leerlauf $x=0$ ist $\eta=1$, im Kurzschluss $x=1$ ist $\eta=0$.
--- falsch
$\eta=x$ und $\frac{P_\mathrm{L}}{P_\mathrm{KS}}=x\,\eta=x^2$. Bei Leistungsanpassung ist $x=1$, also $\eta=1$: Am Leistungsmaximum kommt die ganze Energie jeder Ladung an der Last an.
--- falsch
$\eta=1-x$ und $\frac{P_\mathrm{L}}{P_\mathrm{KS}}=x(1-x)$. Bei Leistungsanpassung ist $x=\frac12$, aber $\eta=\frac14$, weil an der Last nur ein Viertel der Kurzschlussleistung ankommt.
--- falsch
$\eta=1-x^2$ und $\frac{P_\mathrm{L}}{P_\mathrm{KS}}=x(1-x^2)$, weil die Verluste quadratisch mit dem Strom wachsen. Bei Leistungsanpassung ist $x=\frac12$, also $\eta=\frac34$.
:::
:::karte zusammenhang Wirkungsgrad fällt linear
Warum fällt der Wirkungsgrad einer Quelle mit Innenwiderstand linear mit dem Strom?
---
Weil $\eta=U_\mathrm{L}/U_\mathrm{q}$ ist und die Lastspannung auf der Quellengeraden $U_\mathrm{L}=U_\mathrm{q}-R_\mathrm{i}I$ linear mit dem Strom sinkt: Je mehr Strom, desto mehr Spannung bleibt in $R_\mathrm{i}$.
--- falsch
Weil der Innenwiderstand linear mit dem Strom wächst: Je mehr Strom, desto wärmer wird die Quelle und desto größer $R_\mathrm{i}$, sodass immer mehr Energie im Inneren bleibt.
--- falsch
Weil die Verlustleistung $I^2R_\mathrm{i}$ linear mit dem Strom wächst, während die Leistung der Quelle konstant bleibt. Der Anteil der Last nimmt deshalb gleichmäßig ab.
--- falsch
Er fällt nicht linear, sondern quadratisch, weil die Verluste in $R_\mathrm{i}$ mit $I^2$ wachsen. Linear fiele er nur, wenn die Quelle keinen Innenwiderstand hätte.
:::
:::karte zusammenhang Warum genau die Hälfte
Warum beträgt der Wirkungsgrad am Leistungsmaximum zwangsläufig 50 % und hängt nicht vom Material der Quelle ab?
---
$\eta$ fällt linear mit dem Strom, $P_\mathrm{q}=U_\mathrm{q}I$ steigt linear, und an der Last kommt das Produkt $P_\mathrm{L}=P_\mathrm{q}\,\eta$ an. Diese Parabel hat ihren Scheitel in der Mitte, und dort steht die fallende Gerade auf halber Höhe.
--- falsch
Weil jede reale Quelle im Inneren aus zwei gleich großen Hälften besteht, einer chemischen und einer ohmschen. Am Leistungsmaximum arbeiten beide gleich stark, deshalb geht dort genau die Hälfte der Energie verloren.
--- falsch
Weil am Leistungsmaximum Strom und Spannung an der Last zahlenmäßig gleich groß sind. Ihr Verhältnis ist dort 1, und davon erreicht im Mittel genau die Hälfte die Last.
--- falsch
Weil die Quelle am Leistungsmaximum den vollen Kurzschlussstrom liefert. Dann fällt die halbe Spannung innen ab, und trotz des großen Stroms bleibt der Anteil bei der Hälfte.
:::
:::karte zusammenhang Energietechnik
Warum betreibt man in der Energietechnik Quellen weit entfernt von der Leistungsanpassung, mit $R_\mathrm{i}\ll R_\mathrm{L}$?
---
Die Leistungen liegen im kW-Bereich, und jede Wärme in der Quelle kostet Geld und gefährdet sie. Man will hohen Wirkungsgrad; beim Werkzeug-Akku brächte Anpassung 1350 W Wärme im Akku.
--- falsch
Weil Quellen der Energietechnik keinen Innenwiderstand haben. Leistungsanpassung wäre dort gar nicht möglich, weil man dafür auch $R_\mathrm{L}$ gleich null machen müsste und dann nichts mehr ankäme.
--- falsch
Weil bei großen Leistungen das Maximum der Lastleistung bei $R_\mathrm{L}\gg R_\mathrm{i}$ liegt. Die Regel $R_\mathrm{L}=R_\mathrm{i}$ gilt nur für kleine Signale im µ W-Bereich, nicht für Netze.
--- falsch
Weil Verbraucher im Netz einen festen Strom brauchen. Mit $R_\mathrm{i}\ll R_\mathrm{L}$ liefert die Quelle nahezu den Kurzschlussstrom, und zwar unabhängig davon, welche Last gerade angeschlossen ist.
:::
:::karte zusammenhang Nachrichtentechnik
Warum ist in der Nachrichtentechnik die Leistungsanpassung das richtige Ziel, obwohl dabei die Hälfte der Leistung in der Quelle bleibt?
---
Die Leistungen liegen im µ W-Bereich, und ein Empfänger kann nur nehmen, was die Antenne anbietet. Es zählt die absolute Leistung, nicht der Anteil, und die Wärme in der Quelle schadet nicht.
--- falsch
Weil Antennen keinen Innenwiderstand haben und deshalb bei Anpassung überhaupt keine Leistung verlieren. Die Hälfte bleibt nur bei Quellen zurück, die wie Batterien chemische Energie umwandeln.
--- falsch
Weil der Wirkungsgrad bei kleinen Leistungen nicht mehr linear vom Strom abhängt. Bei Signalen im µ W-Bereich liegt er am Leistungsmaximum deutlich über 50 %.
--- falsch
Weil bei Anpassung das Signal die größte Spannung am Empfänger erzeugt. Es zählt die Spannung, nicht die Leistung, und diese ist bei $R_\mathrm{L}=R_\mathrm{i}$ am größten.
:::
:::karte formel Netz bei Leistungsanpassung
Welche Spannung und Leistung erhält eine angepasste Last an einem Netz aus der Quelle $U_\mathrm{q}$, $R_\mathrm{q}$ mit dem Widerstand $R$ parallel zu den Klemmen?
---
Die Ersatzquelle hat $R_\mathrm{i}=R_\mathrm{q}\parallel R$ und $U_\mathrm{LL}=U_\mathrm{q}R/(R_\mathrm{q}+R)$. Bei $R_\mathrm{L}=R_\mathrm{i}$ sind $U_\mathrm{L}=U_\mathrm{q}\,\frac{R}{2(R_\mathrm{q}+R)}$ und $P_\mathrm{L}=\frac{U_\mathrm{q}^2\,R}{4\,R_\mathrm{q}(R_\mathrm{q}+R)}$.
--- falsch
Die Ersatzquelle hat $R_\mathrm{i}=R_\mathrm{q}+R$ und $U_\mathrm{LL}=U_\mathrm{q}$, weil beide Widerstände im Weg liegen. Bei $R_\mathrm{L}=R_\mathrm{i}$ sind $U_\mathrm{L}=U_\mathrm{q}/2$ und $P_\mathrm{L}=\frac{U_\mathrm{q}^2}{4\,(R_\mathrm{q}+R)}$.
--- falsch
Die Ersatzquelle hat $R_\mathrm{i}=R_\mathrm{q}\parallel R$ und $U_\mathrm{LL}=U_\mathrm{q}$, weil $R$ im Leerlauf keinen Strom führt. Bei $R_\mathrm{L}=R_\mathrm{i}$ sind $U_\mathrm{L}=U_\mathrm{q}/2$ und $P_\mathrm{L}=\frac{U_\mathrm{q}^2}{4\,R_\mathrm{i}}$.
--- falsch
Anpassung verlangt hier $R_\mathrm{L}=R_\mathrm{q}$, weil nur die echte Quelle einen Innenwiderstand hat und $R$ zur Last gehört. Dann sind $U_\mathrm{L}=U_\mathrm{q}/2$ und $P_\mathrm{L}=\frac{U_\mathrm{q}^2}{4\,R_\mathrm{q}}$.
:::
:::karte formel Wirkungsgrad des Netzes bei Anpassung
Welchen Wirkungsgrad hat das Netz aus $U_\mathrm{q}$, $R_\mathrm{q}$ und parallelem $R$, wenn die Last an seine Ersatzquelle angepasst ist?
---
$\eta=\frac{P_\mathrm{L}}{P_\mathrm{q}}=\frac12\,\frac{R}{2R_\mathrm{q}+R}<\frac12$ für $R<\infty$, weil die echte Quelle auf $R_\mathrm{ges}=R_\mathrm{q}+R\parallel R_\mathrm{L}$ arbeitet. Erst für $R\to\infty$ wird $\eta=\frac12$.
--- falsch
$\eta=\frac12$, wie bei jeder Leistungsanpassung, weil sich die Energie jeder Ladung zu gleichen Teilen auf Ersatzquelle und Last aufteilt. Der Widerstand $R$ ändert daran nichts.
--- falsch
$\eta=\frac12\,\frac{2R_\mathrm{q}+R}{R}>\frac12$ für $R<\infty$, weil $R$ einen Teil des Stroms an der Last vorbeiführt und so den Innenwiderstand der Quelle entlastet.
--- falsch
$\eta=\frac{R}{R_\mathrm{q}+R}$, weil der Teil des Stroms, der durch $R$ fließt, verloren ist und der Rest vollständig die Last erreicht. Für $R\to\infty$ wird $\eta=1$.
:::
:::karte zusammenhang Ersatzquelle und Wirkungsgrad
Warum zeigt die Ersatzquelle eines Netzes das Leistungsmaximum richtig, den Wirkungsgrad von 50 % aber nicht?
---
Für die Last zählt nur die Klemmengerade, deshalb liegt das Maximum bei $R_\mathrm{L}=R_\mathrm{i}$. Über das Innere sagt die Ersatzquelle nichts aus: Im Netz fließt durch $R$ auch ohne Last ein Strom, und diese Wärme fehlt in ihrer Bilanz.
--- falsch
Weil eine Ersatzquelle nur für Gleichspannung gültig ist. Bei Wechselspannung verschiebt sich der Wirkungsgrad des Netzes, das Maximum der Leistung bleibt aber an derselben Stelle wie bei der Ersatzquelle, also bei $R_\mathrm{L}=R_\mathrm{i}$.
--- falsch
Sie zeigt beides richtig: Auch im echten Netz teilt sich bei Anpassung die Leistung zu gleichen Teilen auf Quelle und Last auf, weil $R$ nur im Leerlauf einen nennenswerten Strom führt.
--- falsch
Weil die Ersatzquelle den Innenwiderstand zu groß angibt. Im echten Netz ist der Widerstand vor der Last kleiner, deshalb liegt der Wirkungsgrad dort über den angezeigten 50 %.
:::
:::karte zusammenhang Hälfte verloren
Verliert man bei Leistungsanpassung tatsächlich die Hälfte der Energie, und wann nimmt man das in Kauf?
---
Bei einer Quelle mit echtem Innenwiderstand ja, sie heizt sich so stark wie die Last. Bei kleiner Leistung ist das tragbar; wo Energie teuer oder die Quelle empfindlich ist, arbeitet man bei großem $R_\mathrm{L}$.
--- falsch
Nein, die Hälfte bleibt nur scheinbar in der Quelle: Sie wird in ihr gespeichert und bei kleinerem Strom wieder an die Last abgegeben. Deshalb nimmt man Anpassung überall in Kauf.
--- falsch
Ja, und deshalb nutzt man Anpassung gerade bei großen Leistungen: Dort lohnt es sich am meisten, die größtmögliche Leistung herauszuholen, auch wenn die Quelle dabei sehr heiß wird.
--- falsch
Nein, verloren geht nur ein Viertel der Kurzschlussleistung $P_\mathrm{KS}$, der Rest erreicht die Last. Diesen kleinen Verlust nimmt man deshalb bei jeder Leistung in Kauf, auch bei großen Quellen.
:::
:::karte herleitung Wirkungsgrad des Netzes
Leite für das Netz aus $U_\mathrm{q}$, $R_\mathrm{q}$ und parallelem $R$ bei angepasster Last den Wirkungsgrad $\eta=\frac12\,\frac{R}{2R_\mathrm{q}+R}$ her.
---
Bei Anpassung ist $R_\mathrm{L}=R_\mathrm{q}R/(R_\mathrm{q}+R)$, also $R\parallel R_\mathrm{L}=R\,R_\mathrm{q}/(R+2R_\mathrm{q})$, weil der Innenwiderstand der Ersatzquelle $R_\mathrm{q}\parallel R$ ist.
---
Das ergibt $R_\mathrm{ges}=2R_\mathrm{q}(R_\mathrm{q}+R)/(2R_\mathrm{q}+R)$, weil die echte Quelle auf $R_\mathrm{q}$ in Reihe mit $R\parallel R_\mathrm{L}$ arbeitet.
---
Der Spannungsteiler $U_\mathrm{L}=U_\mathrm{q}(R\parallel R_\mathrm{L})/R_\mathrm{ges}$ ergibt $U_\mathrm{L}=U_\mathrm{q}\,\frac{R}{2(R_\mathrm{q}+R)}$, weil an $R$ und Last dieselbe Spannung liegt.
---
Damit ist $P_\mathrm{L}=U_\mathrm{L}^2(R_\mathrm{q}+R)/(R_\mathrm{q}R)$ und $P_\mathrm{q}=\frac{U_\mathrm{q}^2}{R_\mathrm{ges}}$, weil $P_\mathrm{L}=\frac{U_\mathrm{L}^2}{R_\mathrm{L}}$ ist und die Quelle $U_\mathrm{q}$ an $R_\mathrm{ges}$ liegt.
---
Der Quotient aus $P_\mathrm{L}$ und $P_\mathrm{q}$ kürzt sich auf $\eta=\frac12\,\frac{R}{2R_\mathrm{q}+R}$, weil sich $U_\mathrm{q}^2$, $R_\mathrm{q}$ und $R_\mathrm{q}+R$ herausheben.
:::
::::

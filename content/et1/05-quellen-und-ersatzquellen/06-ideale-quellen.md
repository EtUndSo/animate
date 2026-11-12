---
title: Stufe 4: Ideale Quellen
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Quellen und Ersatzquellen
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen
knoten: Kapitel 5: Quellen und Ersatzquellen
order: 1150600
summary: Bisher fehlt, was den Strom antreibt.
tags: ideale Spannungsquelle, ideale Stromquelle, Quellenspannung, Quellenstrom
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Bisher fehlt, was den Strom antreibt. Diese Stufe führt die zwei Grundbausteine ein, die Energie in ein Netz bringen.
:::

**Die Idee.** Eine Quelle hält eine einzige Größe fest. Die andere bestimmt das angeschlossene Netz. Eine __ideale Spannungsquelle__ hält die Potenzialdifferenz zwischen ihren Klemmen. Welcher Strom dabei fließt, entscheidet die Last. Eine __ideale Stromquelle__ hält den Strom in ihrem Zweig. Welche Spannung sich dazu einstellt, entscheidet ebenfalls die Last. Beide sind Modelle. Bauen kann man sie nicht, ein geregeltes Netzteil oder eine Transistorschaltung ([Kapitel 10](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor/der-bipolartransistor.html)) kommt ihnen in einem begrenzten Bereich aber nahe.

:::abbildung et1/k5ideal 5
Links die ideale Spannungsquelle: Im Diagramm eine Waagerechte, die Spannung hängt nicht vom Strom ab. Rechts die ideale Stromquelle: eine Senkrechte, der Strom hängt nicht von der Spannung ab. Der Strich im Schaltzeichen zeigt das Verhalten beim Wert null: Längs durchgezogen ist die Leitung geschlossen, quer ist sie unterbrochen.
:::

:::definition Definition 4.1 (Ideale Quellen)
<span class="anker" id="satz-4-1"></span>

Für die ideale Spannungsquelle und die ideale Stromquelle gilt

<span class="anker" id="gl-4-1"></span>
$$U_\mathrm{AB}=U_\mathrm{q}\quad\text{für jeden Strom},\qquad\qquad I_\mathrm{A}=I_\mathrm{q}\quad\text{für jede Spannung}. \tag{4.1}$$
:::

⁠**So liest man das:** $U_\mathrm{q}$ ist die __Quellenspannung__ in V, von Millivolt bis Kilovolt, hier 9 V. $I_\mathrm{q}$ ist der __Quellenstrom__ in A, von Mikroampere bis Ampere. In Abb. [5](#abb-5) ist die Steigung der Kennlinie der Innenwiderstand mit negativem Vorzeichen: bei der Spannungsquelle null, bei der Stromquelle unendlich. Beim Rechnen ersetzt eine Spannungsquelle die Differenz zweier Knotenpotenziale durch einen bekannten Wert, eine Stromquelle legt den Strom eines Zweigs fest.

⁠**Gültigkeit:** Zwei Beschaltungen widersprechen dem Modell. Eine kurzgeschlossene Spannungsquelle soll zugleich $U_\mathrm{AB}=U_\mathrm{q}$ und $U_\mathrm{AB}=0$ erfüllen. Eine offene Stromquelle soll zugleich $I_\mathrm{A}=I_\mathrm{q}$ und $I_\mathrm{A}=0$ erfüllen, denn ein Strom braucht einen geschlossenen Weg.

::::beispiel
Die 9-V-Quelle an 16 $\Omega$ liefert 0,5625 A, an 1 $\Omega$ liefert sie 9 A, an 1 m$\Omega$ wären es 9000 A. Eine 0,5-A-Quelle erzeugt an 16 $\Omega$ 8 V, an 1 k$\Omega$ 500 V, an 1 M$\Omega$ wären es 500 kV.
::::

⁠**Grenzfall:** Je extremer die Last, desto weiter entfernt sich das Modell von jedem echten Gerät. Das ist der Grund für die nächste Stufe.

:::frage Kann der Strom auch rückwärts durch eine Quelle fließen?
Ja. Eine ideale Quelle legt nur ihre eine Größe fest. Fließt der Strom in den Pluspol einer Spannungsquelle hinein, ist $I_\mathrm{A}<0$, und die Quelle nimmt Leistung auf. So lädt man einen Akku.
:::

:::aufgabe Aufgabe 5 ★ Was ändert sich?
<span class="anker" id="aufg-5"></span>

Eine ideale Stromquelle mit 2 mA speist 1 k$\Omega$. (a) Wie groß ist die Spannung, wie groß mit 4,7 k$\Omega$? (b) In Reihe zur Quelle kommt ein zweiter Widerstand mit 1 k$\Omega$. Was ändert sich am ersten, was an der Quelle? (c) Parallel zu einer idealen 5-V-Quelle, die 1 k$\Omega$ speist, kommen 10 $\Omega$. Was ändert sich an der Last, was an der Quelle?

:::loesung
(a) $2\,\mathrm{mA}\cdot1\,\mathrm{k\Omega}=2$ V, mit 4,7 k$\Omega$ sind es 9,4 V. Der Strom bleibt.

(b) Am ersten Widerstand ändert sich nichts: Der Strom ist fest, die Spannung bleibt 2 V. Die Quelle muss 4 V aufbringen. In Reihe zu einer idealen Stromquelle ist ein Widerstand von außen unsichtbar.

(c) An der Last ändert sich nichts, sie bleibt bei 5 V und 5 mA. Die Quelle liefert 505 mA statt 5 mA. Parallel zu einer idealen Spannungsquelle ist ein Widerstand von außen unsichtbar.
:::
:::

::::formelsammlung
**Ideale Spannungsquelle**

$$U_\mathrm{AB}=U_\mathrm{q}\quad\text{für jeden Strom}$$

$U_\mathrm{q}$ Quellenspannung in V, von Millivolt bis Kilovolt. Den Strom bestimmt die Last. Die Kennlinie ist eine Waagerechte, der Innenwiderstand null. Kurzgeschlossen widerspricht die Quelle dem Modell.

**Ideale Stromquelle**

$$I_\mathrm{A}=I_\mathrm{q}\quad\text{für jede Spannung}$$

$I_\mathrm{q}$ Quellenstrom in A, von Mikroampere bis Ampere. Die Spannung bestimmt die Last. Die Kennlinie ist eine Senkrechte, der Innenwiderstand unendlich. Offen widerspricht die Quelle dem Modell, denn ein Strom braucht einen geschlossenen Weg.
::::

::::lernkarten
:::karte begriff ideale Spannungsquelle
Was hält eine ideale Spannungsquelle fest, und was bestimmt dabei die angeschlossene Last?
---
Die Potenzialdifferenz zwischen ihren Klemmen: $U_\mathrm{AB}=U_\mathrm{q}$ für jeden Strom. Welcher Strom fließt, entscheidet die Last; im Diagramm ist ihre Kennlinie eine Waagerechte.
--- falsch
Den Strom in ihrem Zweig, gleich welche Last angeschlossen ist. Welche Spannung sich einstellt, entscheidet die Last; im Diagramm ist ihre Kennlinie eine Senkrechte.
--- falsch
Ihre Spannung, solange die Last nicht zu klein ist. Bei kleiner Last begrenzt sie den Strom selbst auf einen Höchstwert; ihre Kennlinie ist deshalb eine fallende Gerade.
--- falsch
Spannung und Strom zugleich, die Last kann daran nichts ändern. Im Diagramm ist ihre Kennlinie deshalb ein einzelner fester Punkt, gleich welche Last anliegt.
:::
:::karte begriff ideale Stromquelle
Was hält eine ideale Stromquelle fest, und wovon hängt die Spannung an ihren Klemmen ab?
---
Den Strom in ihrem Zweig: $I_\mathrm{A}=I_\mathrm{q}$ für jede Spannung. Welche Spannung sich dazu einstellt, entscheidet die Last; im Diagramm ist ihre Kennlinie eine Senkrechte.
--- falsch
Die Spannung zwischen ihren Klemmen. Welcher Strom fließt, entscheidet die Last; im Diagramm ist ihre Kennlinie eine Waagerechte in der Höhe der Quellenspannung.
--- falsch
Den Strom in ihrem Zweig, $I_\mathrm{A}=I_\mathrm{q}$. Die Spannung an ihren Klemmen ist dabei stets null, weil die Quelle innen wie ein Stück Draht wirkt.
--- falsch
Den Strom in ihrem Zweig, solange die Spannung unter einem Nennwert bleibt. Die Spannung hängt deshalb nicht von der Last ab, sondern nur von der Quelle.
:::
:::karte begriff Quellenspannung und Quellenstrom
Was geben die Quellenspannung $U_\mathrm{q}$ und der Quellenstrom $I_\mathrm{q}$ einer idealen Quelle an, und in welchen Größenordnungen kommen sie vor?
---
$U_\mathrm{q}$ ist die Spannung, die eine ideale Spannungsquelle festhält, in V, von Millivolt bis Kilovolt. $I_\mathrm{q}$ ist der Strom, den eine ideale Stromquelle festhält, in A, von Mikroampere bis Ampere.
--- falsch
$U_\mathrm{q}$ ist die Spannung, die eine Quelle im Kurzschluss abgibt, $I_\mathrm{q}$ der Strom, den sie im Leerlauf liefert. Beide gehören zu jeder Quelle zugleich und liegen meist bei einigen Volt und Ampere.
--- falsch
$U_\mathrm{q}$ ist die Spannung, die an der Last abfällt, und hängt deshalb von der Last ab. $I_\mathrm{q}$ ist der Strom durch die Last, bei üblichen Quellen einige Kiloampere.
--- falsch
$U_\mathrm{q}$ ist die Leistung je Ampere, die eine Quelle höchstens liefern kann, in W/A. $I_\mathrm{q}$ ist der Strom, ab dem die Quelle sich abschaltet, in A, meist einige Milliampere.
:::
:::karte formel Kennlinien idealer Quellen
Wie lauten die Gleichungen der idealen Spannungsquelle und der idealen Stromquelle, und welche Steigung haben ihre Kennlinien?
---
$U_\mathrm{AB}=U_\mathrm{q}$ für jeden Strom und $I_\mathrm{A}=I_\mathrm{q}$ für jede Spannung. Die Steigung ist der Innenwiderstand mit negativem Vorzeichen: bei der Spannungsquelle null, bei der Stromquelle unendlich.
--- falsch
$U_\mathrm{AB}=U_\mathrm{q}$ für jeden Strom und $I_\mathrm{A}=I_\mathrm{q}$ für jede Spannung. Die Steigung ist der Innenwiderstand: bei der Spannungsquelle unendlich, bei der Stromquelle null.
--- falsch
$U_\mathrm{AB}=U_\mathrm{q}$ für jeden Strom und $I_\mathrm{A}=I_\mathrm{q}$ für jede Spannung. Die Steigung ist bei beiden der Widerstand der Last, denn nur die Last legt sie fest.
--- falsch
$U_\mathrm{AB}=U_\mathrm{q}$ nur im Leerlauf und $I_\mathrm{A}=I_\mathrm{q}$ nur im Kurzschluss. Dazwischen verbindet eine fallende Gerade beide Punkte, ihre Steigung ist der Innenwiderstand mit negativem Vorzeichen.
:::
:::karte zusammenhang Widerspruch im Modell
Welche zwei Beschaltungen widersprechen dem Modell der idealen Quellen, und warum?
---
Eine kurzgeschlossene Spannungsquelle soll zugleich $U_\mathrm{AB}=U_\mathrm{q}$ und $U_\mathrm{AB}=0$ erfüllen. Eine offene Stromquelle soll zugleich $I_\mathrm{A}=I_\mathrm{q}$ und $I_\mathrm{A}=0$ erfüllen, denn ein Strom braucht einen geschlossenen Weg.
--- falsch
Eine offene Spannungsquelle und eine kurzgeschlossene Stromquelle: Ohne Last kann die Spannungsquelle keine Spannung halten, und im Kurzschluss fehlt der Stromquelle die Spannung, die ihren Strom durch den Draht antreiben könnte.
--- falsch
Eine Spannungsquelle an einem großen Widerstand und eine Stromquelle an einem kleinen: Dort werden Strom und Spannung so klein, dass das Modell sie nicht mehr darstellen kann.
--- falsch
Keine: Ideale Quellen passen zu jeder Beschaltung, weil sich die Last immer nach der festgehaltenen Größe richtet. Verbotene Fälle gibt es nur bei realen Quellen.
:::
:::karte zusammenhang Grenze des Modells
Warum entfernt sich das Modell der idealen Spannungsquelle bei sehr kleinem Lastwiderstand immer weiter von jedem echten Gerät?
---
Das Modell hält $U_\mathrm{q}$ bei jedem Strom: Die 9-V-Quelle gäbe an 1 m$\Omega$ 9000 A ab. Kein echtes Gerät hält seine Spannung bei so großem Strom, und je extremer die Last, desto weiter liegt das Modell daneben.
--- falsch
Weil die ideale Spannungsquelle bei kleiner Last den Strom selbst begrenzt: Das Modell liefert dann zu wenig Strom, ein echtes Gerät liefert in diesem Fall deutlich mehr, als das Modell vorhersagt.
--- falsch
Es entfernt sich gar nicht: Bei kleiner Last stimmt das Modell am besten. Abweichungen vom echten Gerät gibt es nur bei sehr großen Lastwiderständen.
--- falsch
Weil das Modell bei kleiner Last die Spannung auf null setzt, während ein echtes Gerät dann noch einen Teil seiner Spannung hält und begrenzten Strom liefert.
:::
:::karte zusammenhang Strom rückwärts durch die Quelle
Kann der Strom auch rückwärts durch eine ideale Spannungsquelle fließen, und was bedeutet das für die Leistung der Quelle?
---
Ja, eine ideale Quelle legt nur ihre eine Größe fest. Fließt der Strom in den Pluspol hinein, ist $I_\mathrm{A}<0$, und die Quelle nimmt Leistung auf; so lädt man einen Akku.
--- falsch
Nein: Eine ideale Spannungsquelle lässt Strom nur aus ihrem Pluspol heraus. Ein Strom in den Pluspol hinein würde ihre Spannung umkehren, also ist $I_\mathrm{A}<0$ ausgeschlossen.
--- falsch
Ja, dann ist $I_\mathrm{A}<0$, aber die Quelle gibt weiter Leistung ab, weil ihre Spannung unverändert bleibt und die Leistung nur von der Spannung abhängt.
--- falsch
Nur bei einer Stromquelle; bei einer Spannungsquelle legt ihre Spannung die Richtung fest, und der Strom fließt stets aus dem Pluspol in die Last hinein.
:::
:::karte zusammenhang Unsichtbare Widerstände
Was ändert ein Widerstand in Reihe zu einer idealen Stromquelle oder parallel zu einer idealen Spannungsquelle an der Last?
---
Nichts: Die Quelle hält ihre Größe fest, die Last behält Strom und Spannung. Nur die Quelle muss mehr Spannung beziehungsweise mehr Strom aufbringen; von außen ist der Widerstand unsichtbar.
--- falsch
Die Last bekommt weniger: Der Reihenwiderstand nimmt der Stromquelle einen Teil des Stroms weg, der Parallelwiderstand der Spannungsquelle einen Teil der Spannung, während die Quelle selbst unverändert bleibt.
--- falsch
Die Last bekommt mehr, weil der zusätzliche Widerstand die Quelle entlastet. Die Quelle muss dann weniger leisten, und ihre feste Größe steigt ein wenig an.
--- falsch
Nichts an der Last und nichts an der Quelle: Ein solcher Widerstand führt keinen Strom, weil die ideale Quelle ihn überbrückt und er deshalb stromlos bleibt.
:::
::::

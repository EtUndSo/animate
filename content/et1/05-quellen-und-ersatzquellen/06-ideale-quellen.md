---
title: Stufe 4: Ideale Quellen
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Quellen und Ersatzquellen
order: 1150600
summary: Bisher fehlt, was den Strom antreibt.
tags: ideale Spannungsquelle, ideale Stromquelle, Quellenspannung, Quellenstrom
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Bisher fehlt, was den Strom antreibt. Diese Stufe führt die zwei Grundbausteine ein, die Energie in ein Netz bringen.
:::

**Die Idee.** Eine Quelle hält eine einzige Größe fest. Die andere bestimmt das angeschlossene Netz. Eine __ideale Spannungsquelle__ hält die Potenzialdifferenz zwischen ihren Klemmen. Welcher Strom dabei fließt, entscheidet die Last. Eine __ideale Stromquelle__ hält den Strom in ihrem Zweig. Welche Spannung sich dazu einstellt, entscheidet ebenfalls die Last. Beide sind Modelle. Bauen kann man sie nicht, ein geregeltes Netzteil oder eine Transistorschaltung ([Teil 10](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor/der-bipolartransistor.html)) kommt ihnen in einem begrenzten Bereich aber nahe.

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

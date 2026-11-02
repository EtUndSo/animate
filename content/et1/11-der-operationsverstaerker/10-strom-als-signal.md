---
title: Stufe 8: Strom als Signal
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Der Operationsverstärker
order: 1211000
summary: Bisher war die Spannung das Signal.
tags: Transimpedanzverstärker, differenzieller Widerstand, Negativimpedanzkonverter
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Bisher war die Spannung das Signal. Viele Quellen liefern aber einen Strom. Diese Stufe wandelt Strom in Spannung und zeigt, dass der OPV einen negativen Widerstand nachbilden kann.
:::

**Strom in Spannung.** Eine Fotodiode liefert einen Strom, der von ihrer Spannung kaum abhängt. Im __Transimpedanzverstärker__ fließt er direkt in die virtuelle Masse und muss durch $R$ (Abb. [10](#abb-10) links):

<span class="anker" id="gl-8-1"></span>
$$U_\mathrm{A}=-R\,I_\mathrm{E},\qquad r_\mathrm{ein}=\frac{\Delta U_-}{\Delta I_\mathrm{E}}=\frac{R}{1+A}. \tag{8.1}$$

Mit $R=1$ M$\Omega$ werden 2 µ A zu $-2$ V. Der Knoten bewegt sich dabei nur um $2\,\mathrm{V}/A=20$ µ V. Das ist der kleine Eingangswiderstand von 10 $\Omega$, ein Wert für Änderungen (__differenzieller Widerstand__). Die Quelle sieht fast einen Kurzschluss, ihr Innenwiderstand spielt keine Rolle.

**Ein negativer Widerstand.** Ein Widerstand zieht bei positiver Spannung Strom in Zählpfeilrichtung (Verbraucherzählpfeilsystem, [Teil 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)). Der __Negativimpedanzkonverter__ (NIC) schiebt stattdessen Strom heraus (Abb. [10](#abb-10) rechts). Klemme 1 liegt am Plus-Eingang, von dort führt ein $R$ zum Ausgang. Vom Ausgang führt ein gleiches $R$ zum Minus-Eingang, von dort $R_2$ nach Masse. Aus $\varphi_+=\varphi_-$ folgt $U_1=U_2$.

:::satz Satz 8.1 (NIC)
<span class="anker" id="satz-8-1"></span>

<span class="anker" id="gl-8-2"></span>
$$R_\mathrm{ein}=\frac{U_1}{I_1}=-R_2. \tag{8.2}$$

Die Regel gilt nur, solange der Widerstand $R_\mathrm{i}$, der an Klemme 1 gegen Masse wirkt, kleiner als $R_2$ ist.
:::

⁠**So liest man das:** $I_1$ zählt in Klemme 1 hinein, $U_1$ gegen Masse. $U_2$ und $I_2$ gehören zu $R_2$. $R_\mathrm{i}$ ist alles, was außen an Klemme 1 hängt, etwa Quelle und Last parallel. **Gültigkeit:** $U_\mathrm{A}=U_1(1+R/R_2)$ muss in den Grenzen liegen.

:::herleitung Warum das Vorzeichen kippt und wann die Regel hält
Durch $R_2$ fließt $I_2=U_2/R_2$, kein Strom geht in den Eingang, also fließt er auch durch das untere $R$: Der Ausgang liegt bei $U_\mathrm{A}=U_2+R\,I_2$. Das obere $R$ hat dieselbe Spannung und führt denselben Strom, vom Ausgang zu Klemme 1. Also ist $I_1=-I_2$ und $R_\mathrm{ein}=U_1/I_1=-R_2$.

Hier gibt es zwei Rückführungen, das untere $R$ gegenkoppelt, das linke mitkoppelt. Ändert sich $U_\mathrm{A}$, dann ändert sich $\varphi_-$ um den Anteil $\beta_-=R_2/(R_2+R)$ und $\varphi_+$ um $\beta_+=R_\mathrm{i}/(R_\mathrm{i}+R)$. Nur für $\beta_->\beta_+$ überwiegt die Gegenkopplung, also für $R_\mathrm{i}<R_2$.
:::

:::abbildung et1/k11nic 10
Links der Transimpedanzverstärker mit Stromquelle als Eingang. Rechts der NIC mit $R=10$ k$\Omega$ und $R_2=5$ k$\Omega$ bei 1 V an Klemme 1: Der Ausgang steht auf 3 V und schiebt 0,2 mA aus der Klemme heraus.
:::

**Beispiel.** Mit $R=10$ k$\Omega$, $R_2=5$ k$\Omega$ und $U_1=1$ V ist $I_2=0{,}2$ mA, $U_\mathrm{A}=3$ V, $I_1=-0{,}2$ mA, also $R_\mathrm{ein}=-5$ k$\Omega$. Die Energie kommt aus der Versorgung des OPV. *Anwendung:* Eine Stromquelle mit 1 mA und Innenwiderstand $R_\mathrm{q}=10$ k$\Omega$ gibt an 1 k$\Omega$ nur 0,909 mA ab, weil ein Teil durch $R_\mathrm{q}$ geht. Parallel dazu ein NIC mit $R_2=R_\mathrm{q}$: Der Leitwert $1/R_\mathrm{q}-1/R_2$ verschwindet, die Last bekommt 1 mA. Die reale Quelle wirkt wie eine ideale. Der NIC liefert genau die 0,1 mA, die $R_\mathrm{q}$ abzweigt. **Grenzfall:** Ohne Last ist $R_\mathrm{i}=R_\mathrm{q}=R_2$, beide Rückführungen sind gleich stark, die Schleifenverstärkung ist null, und die Regel gilt nicht mehr.

:::aufgabe Aufgabe 9 ★★★ Stromquelle kompensieren
<span class="anker" id="aufg-9"></span>

Ein NIC mit $R=10$ k$\Omega$ und $R_2=4{,}7$ k$\Omega$ liegt parallel zu einer Quelle mit 2 mA und $R_\mathrm{q}=4{,}7$ k$\Omega$. Die Last ist 1 k$\Omega$. (a) Welchen Strom bekommt die Last ohne NIC, welchen mit NIC? (b) Wo steht der OPV-Ausgang? (c) Bis zu welchem Lastwiderstand reicht der Ausgang von 11 V? (d) Warum ist die Schaltung mit Last stabil, ohne Last aber nicht?

:::loesung
(a) Ohne NIC $2\,\mathrm{mA}\cdot4{,}7/5{,}7=1{,}65$ mA, mit NIC 2 mA. (b) $U_1=2$ V, $I_2=0{,}426$ mA, $U_\mathrm{A}=2\,\mathrm{V}+10\,\mathrm{k\Omega}\cdot0{,}426\,\mathrm{mA}=6{,}26$ V. (c) $U_\mathrm{A}=U_1(1+R/R_2)=3{,}13\,U_1\le11$ V ergibt $U_1\le3{,}52$ V, also $R_\mathrm{L}\le1{,}76$ k$\Omega$. (d) Mit Last ist $R_\mathrm{i}=R_\mathrm{q}\parallel1\,\mathrm{k\Omega}=825\,\Omega<R_2$, die Gegenkopplung überwiegt. Ohne Last ist $R_\mathrm{i}=R_2$, die beiden Rückführungen heben sich auf.
:::
:::

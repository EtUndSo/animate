---
title: Stufe 7: Hybridform
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Zweitore
order: 1160900
summary: Bei einem Verstärker ist es am Eingang leicht, den Strom vorzugeben, am Ausgang die Spannung.
tags: H-Parameter, Kurzschlusseingangswiderstand, Kurzschlussstromübersetzung, Leerlauf-Spannungsrückwirkung, Leerlaufausgangsleitwert
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Bei einem Verstärker ist es am Eingang leicht, den Strom vorzugeben, am Ausgang die Spannung. Diese Stufe mischt die Ursachen.
:::

**Die Idee.** Nichts zwingt dazu, an beiden Toren dieselbe Art von Ursache zu nehmen. Nimmt man $I_1$ und $U_2$, sind $U_1$ und $I_2$ die Wirkungen. Das passt zu Bauteilen wie dem Bipolartransistor: Sein Eingang wird über einen Strom gesteuert, sein Ausgang wirkt wie eine Stromquelle mit großem Innenwiderstand. Die Versuche folgen wieder aus der Wahl: $U_2=0$ heißt Kurzschluss am Ausgang, $I_1=0$ heißt Leerlauf am Eingang.

:::definition Definition 7.1 (Hybridform, H-Form)
<span class="anker" id="satz-7-1"></span>

Die Hybridform nimmt $I_1$ und $U_2$ als Ursachen:

<span class="anker" id="gl-7-1"></span>
$$U_1=H_{11}I_1+H_{12}U_2,\quad I_2=H_{21}I_1+H_{22}U_2,\qquad\text{kurz}\quad \begin{pmatrix}U_1\\I_2\end{pmatrix}=\mathbf H\begin{pmatrix}I_1\\U_2\end{pmatrix}. \tag{7.1}$$

Die __H-Parameter__ sind

<span class="anker" id="gl-7-2"></span>
$$H_{11}=\left.\frac{U_1}{I_1}\right|_{U_2=0},\quad H_{21}=\left.\frac{I_2}{I_1}\right|_{U_2=0},\quad H_{12}=\left.\frac{U_1}{U_2}\right|_{I_1=0},\quad H_{22}=\left.\frac{I_2}{U_2}\right|_{I_1=0}. \tag{7.2}$$
:::

⁠**So liest man das:** $H_{11}$ ist der __Kurzschlusseingangswiderstand__ in $\Omega$, typisch beim Transistor einige k$\Omega$. $H_{21}$ ist die __Kurzschlussstromübersetzung__ vorwärts, die Stromverstärkung, ohne Einheit, etwa 100 bis 500. $H_{12}$ ist die __Leerlauf-Spannungsrückwirkung__, ohne Einheit, um $10^{-4}$. $H_{22}$ ist der __Leerlaufausgangsleitwert__ in S, einige zehn µ S. Die Einheiten sind gemischt, daher der Name. Die Matrix heißt auch Reihenparallelmatrix (Stufe [9](zusammenschaltung.html#stufe-9)). Im Ersatzschaltbild (Abb. [9](#abb-9) links) addieren sich am Eingang Spannungen: Reihenschaltung aus $H_{11}$ und einer VCVS $H_{12}U_2$. Am Ausgang addieren sich Ströme: Parallelschaltung aus $H_{22}$ und einer CCCS $H_{21}I_1$.

:::abbildung et1/k6hesb 9
Links: Ersatzschaltbild der H-Form, am Eingang eine Reihenschaltung, am Ausgang eine Parallelschaltung. Rechts: Das Verstärkermodell mit $H_{12}=0$ und der Last 5 k$\Omega$. 10 µ A am Eingang steuern 1 mA, von denen 0,8 mA durch die Last fließen. Am Ausgang stehen $-4$ V.
:::

**Beispiel.** Das T-Zweitor mit 100 mA am Eingang und kurzgeschlossenem Ausgang: $U_1=2{,}5$ V, und der Strom teilt sich hälftig, $I_2=-50$ mA, also $H_{11}=25\,\Omega$, $H_{21}=-0{,}5$. Bei offenem Eingang und $U_2=4$ V: $I_2=100$ mA, $U_1=2$ V, also $H_{22}=25$ mS, $H_{12}=0{,}5$. Das Verstärkermodell des Kapitels hat $H_{11}=2$ k$\Omega$, $H_{21}=100$, $H_{22}=50$ µ S, also einen Ausgangswiderstand von 20 k$\Omega$, und $H_{12}=0$. Das ist eine Näherung, die rund 1 % ausmacht (Aufgabe [7](#aufg-7)). Bei $U_1=20$ mV fließen $I_1=10$ µ A, die Quelle am Ausgang treibt 1 mA in $20\,\text{k}\Omega\parallel5\,\text{k}\Omega=4$ k$\Omega$. Das ergibt $U_2=-4$ V, eine Spannungsverstärkung von $-200$. Das Minus kommt daher, dass $H_{21}I_1$ in Tor 2 hineinläuft, der Strom also von unten durch die Last fließt.

⁠**Grenzfälle:** Für $H_{22}\to0$ wird der Ausgang eine ideale Stromquelle, für $H_{11}=0$ der Eingang ein Kurzschluss. Das ideale Stromverstärker-Modell ist genau das: $U_1=0$, $I_2=H_{21}I_1$.

:::frage Warum hat $H_{21}$ im T-Zweitor ein Minus, im Verstärker aber nicht?
Im T-Zweitor gibt es keine Quelle. Ein Strom in Tor 1 kann nur aus Tor 2 herauslaufen, $I_2$ ist negativ, und sein Betrag ist kleiner als $I_1$. Im Verstärker ist $H_{21}$ das Gesetz einer gesteuerten Quelle, die den Strom in Richtung und Größe selbst vorgibt und aus einer Hilfsquelle gespeist wird.
:::

:::aufgabe Aufgabe 7 ★★ Wie viel macht die Rückwirkung?
<span class="anker" id="aufg-7"></span>

Das Verstärkermodell bekommt eine kleine Rückwirkung $H_{12}=5\cdot10^{-5}$, sonst gleiche Werte, Last 5 k$\Omega$, $I_1=10$ µ A.

<ol class="al">

<li>

Ändern sich $U_2$ und $I_2$ gegenüber dem Beispiel? Begründe mit [(7.1)](#gl-7-1).

</li>

<li>

Wie groß ist nun $U_1$? Um wie viel Prozent ändert es sich?

</li>

<li>

Wie groß sind Spannungsverstärkung und Eingangswiderstand?

</li>

</ol>

:::loesung
(a) Nein. Die zweite Zeile von [(7.1)](#gl-7-1) enthält $H_{12}$ nicht, und $I_1$ ist fest: $U_2=-4$ V, $I_2=0{,}8$ mA. (b) $U_1=20\,\mathrm{mV}+5\cdot10^{-5}\cdot(-4\,\mathrm{V})=19{,}8$ mV, 1 % weniger. (c) $U_2/U_1=-202$, $Z_1=19{,}8\,\mathrm{mV}/10\,\mu\text{A}=1{,}98$ k$\Omega$. Die Rückwirkung ist hier klein, weshalb man sie oft vernachlässigt.
:::
:::

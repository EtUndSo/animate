---
title: Stufe 7: Hybridform
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Zweitore
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore
knoten: Kapitel 6: Zweitore
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

::::beispiel
Das T-Zweitor mit 100 mA am Eingang und kurzgeschlossenem Ausgang: $U_1=2{,}5$ V, und der Strom teilt sich hälftig, $I_2=-50$ mA, also $H_{11}=25\,\Omega$, $H_{21}=-0{,}5$. Bei offenem Eingang und $U_2=4$ V: $I_2=100$ mA, $U_1=2$ V, also $H_{22}=25$ mS, $H_{12}=0{,}5$. Das Verstärkermodell des Kapitels hat $H_{11}=2$ k$\Omega$, $H_{21}=100$, $H_{22}=50$ µ S, also einen Ausgangswiderstand von 20 k$\Omega$, und $H_{12}=0$. Das ist eine Näherung, die rund 1 % ausmacht (Aufgabe [7](#aufg-7)). Bei $U_1=20$ mV fließen $I_1=10$ µ A, die Quelle am Ausgang treibt 1 mA in $20\,\text{k}\Omega\parallel5\,\text{k}\Omega=4$ k$\Omega$. Das ergibt $U_2=-4$ V, eine Spannungsverstärkung von $-200$. Das Minus kommt daher, dass $H_{21}I_1$ in Tor 2 hineinläuft, der Strom also von unten durch die Last fließt.
::::

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

::::formelsammlung
**Hybridform (H-Form)**

$$U_1=H_{11}I_1+H_{12}U_2,\quad I_2=H_{21}I_1+H_{22}U_2,\qquad\text{kurz}\quad \begin{pmatrix}U_1\\I_2\end{pmatrix}=\mathbf H\begin{pmatrix}I_1\\U_2\end{pmatrix}$$

Ursachen sind $I_1$ und $U_2$. Passt zu Bauteilen mit Stromeingang und Stromquellenausgang wie dem Bipolartransistor. Die Einheiten sind gemischt, daher der Name; auch Reihenparallelmatrix.

**H-Parameter**

$$H_{11}=\left.\frac{U_1}{I_1}\right|_{U_2=0},\quad H_{21}=\left.\frac{I_2}{I_1}\right|_{U_2=0},\quad H_{12}=\left.\frac{U_1}{U_2}\right|_{I_1=0},\quad H_{22}=\left.\frac{I_2}{U_2}\right|_{I_1=0}$$

$H_{11}$ Kurzschlusseingangswiderstand in $\Omega$ (Transistor: einige k$\Omega$), $H_{21}$ Kurzschlussstromübersetzung vorwärts, die Stromverstärkung, ohne Einheit (etwa 100 bis 500), $H_{12}$ Leerlauf-Spannungsrückwirkung ohne Einheit (um $10^{-4}$), $H_{22}$ Leerlaufausgangsleitwert in S (einige zehn µ S).
::::

::::lernkarten
:::karte begriff Hybridform
Was ist die Hybridform eines Zweitors, und welche Torgrößen sind darin die Ursachen?
---
Die Form der Zweitorgleichungen mit $I_1$ und $U_2$ als Ursachen: $U_1=H_{11}I_1+H_{12}U_2$, $I_2=H_{21}I_1+H_{22}U_2$. Ihre Parameter haben gemischte Einheiten, daher der Name.
--- falsch
Die Form mit $U_1$ und $I_2$ als Ursachen: $I_1=H_{11}U_1+H_{12}I_2$, $U_2=H_{21}U_1+H_{22}I_2$. Ihre Parameter haben gemischte Einheiten, daher der Name.
--- falsch
Die Form mit beiden Strömen als Ursachen: $U_1=H_{11}I_1+H_{12}I_2$, $U_2=H_{21}I_1+H_{22}I_2$. Sie ist eine Mischung aus Z-Form und Y-Form, daher der Name.
--- falsch
Die Form $U_1=H_{11}I_1+H_{12}U_2$, $I_2=H_{21}I_1+H_{22}U_2$ mit $U_1$ und $I_2$ als Ursachen, weil man diese beiden Größen an einem Bauteil am leichtesten messen kann.
:::
:::karte zusammenhang Wozu die Hybridform passt
Warum passt die Hybridform zu Bauteilen wie dem Bipolartransistor?
---
Sein Eingang wird über einen Strom gesteuert, sein Ausgang wirkt wie eine Stromquelle mit großem Innenwiderstand. Leicht vorzugeben sind also der Eingangsstrom und die Ausgangsspannung, die Ursachen der Hybridform.
--- falsch
Weil der Transistor drei Anschlüsse hat und die Hybridform als einzige Form auch für Dreipole gilt. Die anderen Formen verlangen eine erdsymmetrische Schaltung mit vier getrennten Anschlüssen und ohne Masseleitung.
--- falsch
Sein Eingang wird über eine Spannung gesteuert, sein Ausgang wirkt wie eine ideale Spannungsquelle ohne Innenwiderstand. Genau diese beiden Spannungen sind die Ursachen der Hybridform.
--- falsch
Weil der Transistor mit Gleichgrößen und Wechselgrößen zugleich arbeitet. Die Hybridform verbindet beide Arten von Größen in einer einzigen Gleichung, daher auch ihr Name.
:::
:::karte formel H-Parameter
Wie sind die H-Parameter durch Versuche an den Toren festgelegt?
---
$H_{11}=\left.\frac{U_1}{I_1}\right|_{U_2=0}$ und $H_{21}=\left.\frac{I_2}{I_1}\right|_{U_2=0}$ bei kurzgeschlossenem Ausgang, $H_{12}=\left.\frac{U_1}{U_2}\right|_{I_1=0}$ und $H_{22}=\left.\frac{I_2}{U_2}\right|_{I_1=0}$ bei offenem Eingang.
--- falsch
$H_{11}=\left.\frac{U_1}{I_1}\right|_{I_2=0}$ und $H_{21}=\left.\frac{I_2}{I_1}\right|_{I_2=0}$ bei offenem Ausgang, $H_{12}=\left.\frac{U_1}{U_2}\right|_{U_1=0}$ und $H_{22}=\left.\frac{I_2}{U_2}\right|_{U_1=0}$ bei kurzgeschlossenem Eingang.
--- falsch
Alle vier aus einem einzigen Kurzschlussversuch am Ausgang: $H_{11}$ als $U_1$ durch $I_1$, $H_{12}$ als $U_1$ durch $U_2$, $H_{21}$ als $I_2$ durch $I_1$ und $H_{22}$ als $I_2$ durch $U_2$, alles bei derselben Messung.
--- falsch
$H_{11}=\left.\frac{I_1}{U_1}\right|_{U_2=0}$ und $H_{21}=\left.\frac{I_1}{I_2}\right|_{U_2=0}$ bei kurzgeschlossenem Ausgang, $H_{12}=\left.\frac{U_2}{U_1}\right|_{I_1=0}$ und $H_{22}=\left.\frac{U_2}{I_2}\right|_{I_1=0}$ bei offenem Eingang.
:::
:::karte begriff Kurzschlusseingangswiderstand und Leerlaufausgangsleitwert
Was geben der Kurzschlusseingangswiderstand $H_{11}$ und der Leerlaufausgangsleitwert $H_{22}$ an, und welche Werte sind beim Transistor typisch?
---
$H_{11}$ ist der Widerstand an Tor 1 bei kurzgeschlossenem Ausgang, in $\Omega$, beim Transistor einige k$\Omega$. $H_{22}$ ist der Leitwert an Tor 2 bei offenem Eingang, in S, einige zehn µ S.
--- falsch
$H_{11}$ ist der Widerstand an Tor 1 bei offenem Ausgang, beim Transistor einige M$\Omega$. $H_{22}$ ist der Leitwert an Tor 2 bei kurzgeschlossenem Eingang, beim Transistor einige Siemens.
--- falsch
$H_{11}$ ist der Leitwert an Tor 1 bei kurzgeschlossenem Ausgang, in S. $H_{22}$ ist der Widerstand an Tor 2 bei offenem Eingang, in $\Omega$, beim Transistor einige zehn k$\Omega$.
--- falsch
$H_{11}$ und $H_{22}$ sind Kehrwerte voneinander, weil beide denselben Widerstand des Zweitors von verschiedenen Seiten messen; beim Transistor typisch 1 k$\Omega$ und 1 mS.
:::
:::karte begriff Kurzschlussstromübersetzung
Was gibt die Kurzschlussstromübersetzung $H_{21}$ an, und welche Werte hat sie beim Transistor?
---
Das Verhältnis von Ausgangsstrom zu Eingangsstrom bei kurzgeschlossenem Ausgang, die Stromverstärkung. Sie hat keine Einheit, beim Transistor etwa 100 bis 500.
--- falsch
Das Verhältnis von Eingangsstrom zu Ausgangsstrom bei offenem Ausgang, also die Stromdämpfung. Sie hat keine Einheit und liegt beim Transistor um $10^{-4}$.
--- falsch
Den Strom, der bei kurzgeschlossenem Ausgang aus Tor 2 herausfließt, gemessen in Ampere. Er liegt beim Transistor etwa bei 100 bis 500 mA.
--- falsch
Das Verhältnis von Ausgangsspannung zu Eingangsspannung bei kurzgeschlossenem Ausgang, also die Spannungsverstärkung, beim Transistor ebenfalls etwa 100 bis 500.
:::
:::karte begriff Leerlauf-Spannungsrückwirkung
Was gibt die Leerlauf-Spannungsrückwirkung $H_{12}$ an, und wie groß ist sie beim Transistor etwa?
---
Das Verhältnis von Eingangsspannung zu Ausgangsspannung bei offenem Eingang, also wie stark $U_2$ auf den Eingang zurückwirkt. Sie hat keine Einheit und liegt beim Transistor um $10^{-4}$.
--- falsch
Das Verhältnis von Ausgangsspannung zu Eingangsspannung bei offenem Ausgang, also die Spannungsverstärkung. Sie hat keine Einheit und liegt beim Transistor bei einigen Hundert.
--- falsch
Den Widerstand, über den der Ausgang auf den Eingang zurückwirkt, gemessen in $\Omega$. Er liegt beim Transistor bei einigen k$\Omega$ und begrenzt den Eingangsstrom.
--- falsch
Das Verhältnis von Eingangsspannung zu Ausgangsspannung bei kurzgeschlossenem Eingang. Sie hat keine Einheit und liegt beim Transistor etwa bei 100 bis 500.
:::
:::karte zusammenhang Ersatzschaltbild der H-Form
Wie sieht das Ersatzschaltbild der H-Form aus, und warum ist es am Eingang anders aufgebaut als am Ausgang?
---
Am Eingang addieren sich Spannungen: Reihenschaltung aus $H_{11}$ und einer VCVS $H_{12}U_2$. Am Ausgang addieren sich Ströme: Parallelschaltung aus $H_{22}$ und einer CCCS $H_{21}I_1$.
--- falsch
Am Eingang addieren sich Ströme: Parallelschaltung aus $H_{11}$ und einer CCCS $H_{12}U_2$. Am Ausgang addieren sich Spannungen: Reihenschaltung aus $H_{22}$ und einer VCVS $H_{21}I_1$.
--- falsch
An beiden Toren eine Reihenschaltung aus einem Widerstand und einer stromgesteuerten Spannungsquelle wie bei der Z-Form. Die H-Form ändert nur die Namen der vier Parameter.
--- falsch
Am Eingang Reihenschaltung aus $H_{11}$ und einer CCVS $H_{12}U_2$, am Ausgang Parallelschaltung aus $H_{22}$ und einer VCCS $H_{21}I_1$, weil jede Quelle vom eigenen Tor gesteuert wird.
:::
:::karte zusammenhang Vorzeichen der Stromübersetzung
Warum ist $H_{21}$ im T-Zweitor negativ, im Verstärkermodell aber positiv?
---
Im T-Zweitor gibt es keine Quelle: Ein Strom in Tor 1 kann nur aus Tor 2 herauslaufen, $I_2$ ist negativ. Im Verstärker ist $H_{21}$ das Gesetz einer gesteuerten Quelle, die den Strom in Richtung und Größe selbst vorgibt.
--- falsch
Weil das T-Zweitor erdunsymmetrisch ist und das Verstärkermodell erdsymmetrisch. Bei erdsymmetrischen Zweitoren fließt der Ausgangsstrom immer in das Zweitor hinein, bei erdunsymmetrischen dagegen immer heraus zur Last.
--- falsch
Weil das Verstärkermodell im Kettenpfeilsystem gezählt wird und das T-Zweitor im gemischten Pfeilsystem. Mit gleichen Zählpfeilen hätten beide Zweitore ein Minus vor $H_{21}$.
--- falsch
Weil der Strom im T-Zweitor durch den Querwiderstand $R_\mathrm{b}$ umgelenkt wird. Im Verstärker gibt es keinen Querwiderstand, deshalb fließt der Strom dort geradeaus hindurch.
:::
:::karte zusammenhang Spannungsverstärkung des Verstärkermodells
Welche Spannungsverstärkung hat das Verstärkermodell mit 2 k$\Omega$ am Eingang, Stromverstärkung 100, 20 k$\Omega$ am Ausgang und 5 k$\Omega$ Last, und woher kommt ihr Vorzeichen?
---
$-200$: 10 µ A am Eingang steuern 1 mA, der in $20\,\text{k}\Omega\parallel5\,\text{k}\Omega=4$ k$\Omega$ fließt, $U_2=-4$ V bei 20 mV. Das Minus: $H_{21}I_1$ läuft in Tor 2 hinein, der Strom fließt also von unten durch die Last.
--- falsch
$+200$: 10 µ A am Eingang steuern 1 mA, der in 4 k$\Omega$ fließt, also 4 V bei 20 mV. Das Vorzeichen ist positiv, weil $H_{21}=100$ positiv ist und eine positive Stromverstärkung nichts umkehrt.
--- falsch
$-250$: 10 µ A am Eingang steuern 1 mA, der ganz durch die Last von 5 k$\Omega$ fließt, also $-5$ V bei 20 mV. Das Minus kommt allein vom gemischten Pfeilsystem des Kapitels.
--- falsch
$-100$: Die Spannungsverstärkung ist gleich der Stromverstärkung $H_{21}$, weil Eingang und Ausgang über dieselbe gesteuerte Quelle verbunden sind. Das Minus kommt vom gemischten Pfeilsystem.
:::
:::karte zusammenhang Ideale Grenzfälle der H-Form
Was wird aus dem Ausgang für $H_{22}\to0$ und aus dem Eingang für $H_{11}=0$, und welches Modell entsteht so?
---
Für $H_{22}\to0$ wird der Ausgang eine ideale Stromquelle, für $H_{11}=0$ der Eingang ein Kurzschluss. Zusammen ist das das ideale Stromverstärker-Modell: $U_1=0$, $I_2=H_{21}I_1$.
--- falsch
Für $H_{22}\to0$ wird der Ausgang ein Leerlauf ohne Strom, für $H_{11}=0$ der Eingang ein offenes Tor. Zusammen entsteht ein Zweitor, das gar nichts mehr überträgt.
--- falsch
Für $H_{22}\to0$ wird der Ausgang eine ideale Spannungsquelle, für $H_{11}=0$ der Eingang ein Kurzschluss. Zusammen ist das das ideale Spannungsverstärker-Modell mit $U_1=0$.
--- falsch
Für $H_{22}\to0$ wird der Ausgang ein Kurzschluss, für $H_{11}=0$ der Eingang eine ideale Stromquelle. Zusammen ist das das ideale Stromverstärker-Modell: $U_2=0$, $I_1=H_{21}I_2$.
:::
::::

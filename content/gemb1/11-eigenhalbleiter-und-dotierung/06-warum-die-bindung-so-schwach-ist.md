---
title: Stufe 4: Warum die Bindung so schwach ist
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Eigenhalbleiter und Dotierung
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/eigenhalbleiter-und-dotierung
knoten: Kapitel 11: Eigenhalbleiter und Dotierung
order: 4210600
summary: Ein freies Phosphoratom hält sein äußerstes Elektron mit rund 10 eV, im Kristall bleiben 45 meV.
tags: 
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Ein freies Phosphoratom hält sein äußerstes Elektron mit rund 10 eV, im Kristall bleiben 45 meV. Diese Stufe erklärt den Faktor 200 mit dem Wasserstoffmodell.
:::

**Die Idee.** Das fünfte Elektron sieht einen Rumpf mit einer Elementarladung Überschuss, wie das Elektron im Wasserstoff sein Proton. Zwei Dinge sind anders. Erstens bewegt es sich nicht im Vakuum, sondern im Leitungsband, mit der effektiven Masse $m^*$. Zweitens verschieben sich die Bindungselektronen ringsum, der Kristall wird polarisiert und schirmt die Ladung ab. Das Feld ist um den Faktor $\varepsilon_\mathrm r$ schwächer. Die Energie null ist die Bandkante $E_\mathrm C$, denn „frei“ heißt hier: im Leitungsband.

:::abbildung gemb1/k11wasserstoff 4
Coulomb-Potential und Grundzustand. Links Wasserstoff im Vakuum. Rechts das Modell im Silizium mit $m_\mathrm l^*=0{,}19\,m_0$ und $\varepsilon_\mathrm r=11{,}7$. Die Form ist gleich, die Achsen unterscheiden sich um die Faktoren 720 in der Energie und 62 im Radius. Die grauen Punkte haben den Abstand der Gitterkonstanten 0,543 nm.
:::

:::satz Satz 4.1 (Wasserstoffmodell der flachen Störstelle)
<span class="anker" id="satz-4-1"></span>

Für ein Elektron der Masse $m^*$ im Coulomb-Feld $V(r)=-e^2/(4\pi\varepsilon_\mathrm r\varepsilon_0r)$ gilt

<span class="anker" id="gl-4-1"></span>
$$\Delta E_\mathrm D\approx\frac{e^4m^*}{2\,(4\pi\varepsilon_\mathrm r\varepsilon_0\hbar)^2}=13{,}6\,\mathrm{eV}\cdot\frac{m^*/m_0}{\varepsilon_\mathrm r^2},\qquad r_\mathrm D=r_1\,\frac{\varepsilon_\mathrm r}{m^*/m_0}. \tag{4.1}$$
:::

:::herleitung Zwei Ersetzungen
In [Kapitel 4](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/atome-und-orbitale/atome-und-orbitale.html) ist $|E_1|=m_0e^4/(8\varepsilon_0^2h^2)$. Das Potential unterscheidet sich nur durch $\varepsilon_0\to\varepsilon_\mathrm r\varepsilon_0$, die kinetische Energie durch $m_0\to m^*$. Also gilt dieselbe Rechnung mit diesen Ersetzungen, und mit $h=2\pi\hbar$ ist $8h^2=2(4\pi\hbar)^2$. Die Energie wächst mit der Masse und fällt mit $\varepsilon_\mathrm r^2$. Der Radius $r_1=4\pi\varepsilon_0\hbar^2/(m_0e^2)$ verhält sich umgekehrt zur Masse und wächst mit $\varepsilon_\mathrm r$.
:::

⁠**So liest man das:** $\varepsilon_\mathrm r$ ist die relative Permittivität, $r_\mathrm D$ der Radius der Bahn um den Donator. Für Akzeptoren gilt dasselbe mit der Lochmasse: Das Loch umkreist die negative Ladung. **Gültigkeit:** Die Bahn muss groß gegen den Atomabstand sein, denn nur dann mittelt das Elektron über viele Atome, und $m^*$ und $\varepsilon_\mathrm r$ sind die richtigen Größen. Bei tiefen Störstellen ist das nicht der Fall, das Modell gilt dort nicht.

::::beispiel
Mit $m_\mathrm l^*=0{,}19\,m_0$ und $\varepsilon_\mathrm r=11{,}7$ folgen $\Delta E_\mathrm D=18{,}9$ meV und $r_\mathrm D=3{,}26$ nm. Das sind sechs Gitterkonstanten, in der Kugel liegen rund 7000 Atome: Das Modell ist in sich stimmig. Gemessen sind 33 bis 69 meV für die flachen Donatoren. Die Größenordnung stimmt. Der Rest stammt aus der Nähe des Rumpfs, wo die Abschirmung unvollständig ist und jedes Element etwas anders bindet. Für Löcher mit $m_\mathrm{hh}^*=0{,}49\,m_0$ folgen 48,7 meV, Bor hat 45 meV. Beide Effekte zusammen machen die Bindung so klein, dass sie mit $k_\mathrm BT=25{,}85$ meV vergleichbar ist: Für Phosphor ist $\mathrm{e}^{-\Delta E_\mathrm D/(k_\mathrm BT)}=0{,}18$.
::::

⁠**Grenzfall:** Für $m^*=m_0$ und $\varepsilon_\mathrm r=1$ folgt wieder Wasserstoff.

:::frage Warum zählt schon $E_\mathrm C$ als „frei“? Das Elektron ist doch noch im Kristall.
Gebunden heißt im Modell: an einen Ort gefesselt. Im Leitungsband ist das Elektron eine laufende Welle durch den ganzen Kristall ([Kapitel 8](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/vom-atom-zum-band/vom-atom-zum-band.html)), es gehört keinem Rumpf mehr. Der Austritt aus dem Kristall spielt für die Dotierung keine Rolle.
:::

:::aufgabe Aufgabe 5 ★★ GaAs als Wasserstoff
<span class="anker" id="aufg-5"></span>

GaAs hat $\varepsilon_\mathrm r=13{,}1$, $m_\mathrm C^*=0{,}067\,m_0$ und $m_\mathrm{hh}^*=0{,}45\,m_0$.

<ol class="al">

<li>

Berechne $\Delta E_\mathrm D$ und $r_\mathrm D$. Vergleiche mit gemessenen rund 6 meV.

</li>

<li>

Schätze $\Delta E_\mathrm A$ ab. Warum ist die Akzeptorbahn viel kleiner?

</li>

<li>

Ab welcher Dichte stoßen die Bahnen an, wenn die Donatoren den Abstand $2r_\mathrm D$ haben?

</li>

</ol>

:::loesung
(a) $\Delta E_\mathrm D=13{,}6\,\mathrm{eV}\cdot0{,}067/13{,}1^2=5{,}3$ meV, $r_\mathrm D=0{,}0529\,\mathrm{nm}\cdot13{,}1/0{,}067=10{,}4$ nm. Das passt gut, denn die Bahn überdeckt viele Atome. (b) 35,7 meV. Die Lochmasse ist 6,7-mal größer, also ist die Bahn 6,7-mal kleiner, 1,5 nm. (c) $N=1/(2r_\mathrm D)^3=1{,}1\cdot10^{17}\,\mathrm{cm^{-3}}$.
:::
:::

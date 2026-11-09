---
title: Stufe 4: Was das Gleichgewicht verlangt
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Strom im Halbleiter
order: 4220600
summary: Die Fermi-Verteilung aus Teil 10 galt für einen einheitlichen Kristall.
tags: Quasi-Fermi-Niveau, Driftanteil, Diffusionsanteil, elektrochemisches Potential
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Die Fermi-Verteilung aus [Teil 10](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/zustandsdichte-und-fermi-verteilung/zustandsdichte-und-fermi-verteilung.html) galt für einen einheitlichen Kristall. Diese Stufe macht sie ortsabhängig, setzt sie in die Gleichung ein und findet so heraus, was einen Strom antreibt.
:::

**Die Idee.** Liegt ein Feld an oder ändert sich die Dotierung, wird die Leitungsbandkante zu $E_\mathrm C(x)$. An jedem Ort darf sich trotzdem eine Fermi-Verteilung einstellen, mit örtlichen Werten. Prüft man, ob das eine Lösung ohne Strom ist, fällt der Einfluss der Bandkante heraus. Fermi-Energie und Temperatur müssen überall gleich sein. Ihre Unterschiede sind die treibenden Kräfte.

:::definition Definition 4.1 (Lokales Gleichgewicht)
<span class="anker" id="satz-4-1"></span>

Mit $E(k)$ von der Bandkante aus gezählt, etwa $E(k)=\hbar^2k^2/(2m^*)$, lautet die örtliche Verteilung

<span class="anker" id="gl-4-1"></span>
$$f^0(x,k)=\frac1{1+\exp\Bigl(\dfrac{E_\mathrm C(x)+E(k)-E_\mathrm F(x)}{k_\mathrm BT(x)}\Bigr)}. \tag{4.1}$$
:::

⁠**So liest man das:** Die Gesamtenergie ist Bandkante plus Bandstruktur, im Valenzband entsprechend mit $E_\mathrm V(x)$. $E_\mathrm F(x)$ heißt __Quasi-Fermi-Niveau__, das örtliche Fermi-Niveau außerhalb des Gleichgewichts, $T(x)$ die örtliche Temperatur. **Gültigkeit:** Beide ändern sich zwischen zwei Stößen nur wenig.

:::satz Satz 4.2 (Bedingungen für das Gleichgewicht)
<span class="anker" id="satz-4-2"></span>

[(4.1)](#gl-4-1) löst [(3.2)](vom-wellenpaket-zur-verteilungsfunktion.html#gl-3-2) mit $\mathrm{d} f/\mathrm{d} t=0$ und $\partial f/\partial t=0$ genau dann, wenn

<span class="anker" id="gl-4-2"></span>
$$\frac{\mathrm{d} E_\mathrm F(x)}{\mathrm{d} x}=0\qquad\text{und}\qquad\frac{\mathrm{d}}{\mathrm{d} x}\frac1T=-\frac1{T^2}\frac{\mathrm{d} T}{\mathrm{d} x}=0. \tag{4.2}$$
:::

⁠**So liest man das:** Treibende Kräfte für das Nichtgleichgewicht und damit für Strom sind verschiedene Fermi-Niveaus und Temperaturunterschiede. Eine Neigung von $E_\mathrm C$ allein gehört nicht dazu.

:::herleitung Einsetzen in die Boltzmann-Gleichung
Es bleibt $v\,\partial f/\partial x+(F/\hbar)\,\partial f/\partial k=0$. Mit $f^0=1/(1+\mathrm{e}^y)$ und $y=(E_\mathrm C+E(k)-E_\mathrm F)/(k_\mathrm BT)$ gibt die Kettenregel, weil $\partial f/\partial y\neq0$ ist, $v\,\partial y/\partial x+(F/\hbar)\,\partial y/\partial k=0$, mit

$$\frac{\partial y}{\partial x}=\frac1{k_\mathrm BT}\Bigl(\frac{\mathrm{d} E_\mathrm C}{\mathrm{d} x}-\frac{\mathrm{d} E_\mathrm F}{\mathrm{d} x}\Bigr)+\frac1{k_\mathrm B}\bigl(E_\mathrm C+E(k)-E_\mathrm F\bigr)\frac{\mathrm{d}}{\mathrm{d} x}\frac1T,\qquad\frac{\partial y}{\partial k}=\frac1{k_\mathrm BT}\frac{\mathrm{d} E}{\mathrm{d} k}=\frac{\hbar v}{k_\mathrm BT}.$$

Die Kraft ist das Gefälle der Bandkante, $\mathrm{d} E_\mathrm C/\mathrm{d} x=-F$. Einsetzen:

$$\frac v{k_\mathrm BT}\Bigl(-F-\frac{\mathrm{d} E_\mathrm F}{\mathrm{d} x}\Bigr)+\frac v{k_\mathrm B}\bigl(E_\mathrm C+E(k)-E_\mathrm F\bigr)\frac{\mathrm{d}}{\mathrm{d} x}\frac1T+\frac F{k_\mathrm BT}\,v=0.$$

Die Terme mit $F$ heben sich auf. Der Rest muss für jedes $k$ null sein. Nur der zweite Term enthält $E(k)$, also verschwindet $\mathrm{d}(1/T)/\mathrm{d} x$, danach auch $\mathrm{d} E_\mathrm F/\mathrm{d} x$.
:::

**Feld und Dichte.** Mit $\zeta=E_\mathrm F-E_\mathrm C=-k_\mathrm BT\ln(N_\mathrm C/n)$ und $\mathrm{d} E_\mathrm C/\mathrm{d} x=e\mathcal E$ gilt bei fester Temperatur

<span class="anker" id="gl-4-3"></span>
$$E_\mathrm F(x)=E_\mathrm C(x)+\zeta(x),\qquad\frac{\mathrm{d} E_\mathrm F}{\mathrm{d} x}=e\mathcal E+\frac{k_\mathrm BT}n\frac{\mathrm{d} n}{\mathrm{d} x}. \tag{4.3}$$

Der erste Summand ist der __Driftanteil__, der zweite der __Diffusionsanteil__. $\zeta$ misst, wie voll das Band ist, und $E_\mathrm C=\text{konst}-e\varphi$ enthält das elektrostatische Potential $\varphi$. Ein zusätzliches Elektron bringt also Füllenergie plus Energie im Potential, $E_\mathrm{ges}=TS-pV+\zeta N-e\varphi N$. Deshalb heißt $E_\mathrm F$ auch __elektrochemisches Potential__. In [Teil 10](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/zustandsdichte-und-fermi-verteilung/zustandsdichte-und-fermi-verteilung.html) war $E_\mathrm C$ überall gleich, und beide Begriffe fielen zusammen. Im Gleichgewicht halten sich Feld und Dichteunterschied genau die Waage.

:::analogie
Zwei Wasserbecken werden verbunden. Wasser fließt, bis die Pegel gleich sind. Der Pegel ist $E_\mathrm F$. Stehen die Becken verschieden hoch, sind Tiefe (Füllung) und Boden (Bandkante) verschieden, und bei gleichem Pegel fließt nichts. Das Bild endet bei den Kräften: Wasser drückt mit seinem Gewicht, Elektronen gleichen Dichten durch Wärmebewegung aus.
:::

:::abbildung gemb1/k12gleichgewicht 4
Energie über dem Ort, Punkte: Elektronen, eng, wo die Dichte hoch ist. Links fällt $N_\mathrm D$ von $10^{17}$ auf $10^{15}\,\mathrm{cm^{-3}}$, die Bandkante steigt, $E_\mathrm F$ bleibt waagerecht. Rechts ist die Probe homogen, 100 mV liegen an, $E_\mathrm F$ neigt sich.
:::

::::beispiel
Auf 100 µ m fällt $N_\mathrm D$ exponentiell von $10^{17}$ auf $10^{15}\,\mathrm{cm^{-3}}$ (Abb. [4](#abb-4)). Bei waagerechtem $E_\mathrm F$ ist $E_\mathrm C-E_\mathrm F$ links 146 meV und rechts 265 meV. Im Kristall herrscht also $\mathcal E=1190$ V/m, obwohl kein Strom fließt.
::::

⁠**Grenzfall:** In homogener Probe ist $\mathrm{d} E_\mathrm F/\mathrm{d} x=e\mathcal E$: Jedes Feld treibt dann Strom.

:::frage Im Beispiel herrscht ein echtes Feld. Warum treibt es keinen Strom?
Es zieht die Elektronen zum dichten Gebiet zurück, ihre Wärmebewegung drängt sie von dort weg, und beide Anteile heben sich auf. Das Feld stammt von wenigen abgewanderten Elektronen, die ihre ortsfesten Donatoren zurückgelassen haben.
:::

:::aufgabe Aufgabe 4 ★★ Ein Dotierverlauf
<span class="anker" id="aufg-4"></span>

In Silizium fällt $N_\mathrm D$ auf 40 µ m exponentiell von $5\cdot10^{16}$ auf $2\cdot10^{14}\,\mathrm{cm^{-3}}$, bei 300 K ohne äußere Spannung.

<ol class="al">

<li>

Berechne $E_\mathrm C-E_\mathrm F$ an beiden Enden und in der Mitte.

</li>

<li>

Wie groß ist das Feld, und wohin zeigt die Kraft auf ein Elektron? Wie groß ist die Stufe der Bandkante bei 350 K?

</li>

<li>

Vorhersage: Du legst außen eine kleine Spannung an. Was geschieht mit $E_\mathrm F$?

</li>

</ol>

:::loesung
(a) Mit $k_\mathrm BT\ln(N_\mathrm C/n)$ ergeben sich links 164 meV, rechts 306 meV und in der Mitte, bei $n=\sqrt{5\cdot10^{16}\cdot2\cdot10^{14}}=3{,}2\cdot10^{15}\,\mathrm{cm^{-3}}$, 235 meV. (b) Die Bandkante steigt um 143 meV auf 40 µ m, also $\mathcal E=3{,}57$ kV/m zu größerem $x$. Die Kraft $F=-e\mathcal E$ zeigt zum dichten Gebiet. Bei 350 K ist die Stufe $k_\mathrm BT\ln250=167$ meV. (c) $E_\mathrm F$ neigt sich, Strom fließt, und die Neigung sitzt vor allem im schwach dotierten Ende, wo $n$ klein ist.
:::
:::

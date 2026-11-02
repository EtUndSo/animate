---
title: Stufe 5: Freies Elektron, ebene Welle, Dispersion
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Welle, Teilchen und Schrödinger-Gleichung
order: 4110700
summary: Die Gleichung steht.
tags: frei, Dispersionsrelation, ebene Welle
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Die Gleichung steht. Diese Stufe löst sie für den einfachsten Fall, ein überall gleiches Potential. Das Ergebnis verknüpft Energie und Wellenzahl.
:::

**Die Idee.** Ist $V(x)=V_0$ konstant, wirkt keine Kraft, denn $F=-\mathrm{d} V/\mathrm{d} x=0$. Das Elektron heißt dann __frei__. Alle Orte sind gleichwertig, also sollte auch die Aufenthaltswahrscheinlichkeit überall gleich sein. Das leistet eine Welle mit fester Wellenzahl. Zweimal Ableiten von $\mathrm{e}^{\mathrm{j} kx}$ gibt den Faktor $-k^2$, und aus der Differentialgleichung wird eine algebraische Gleichung.

:::satz Satz 5.1 (Lösung bei konstantem Potential)
<span class="anker" id="satz-5-1"></span>

Für $V(x)=V_0$ und $E\ge V_0$ löst

<span class="anker" id="gl-5-1"></span>
$$\psi(x)=C_+\,\mathrm{e}^{\mathrm{j} kx}+C_-\,\mathrm{e}^{-\mathrm{j} kx},\qquad k=\frac{\sqrt{2m(E-V_0)}}\hbar, \tag{5.1}$$

die zeitunabhängige Schrödinger-Gleichung, und es gilt die __Dispersionsrelation__

<span class="anker" id="gl-5-2"></span>
$$E(k)=\frac{\hbar^2k^2}{2m}+V_0=E_\mathrm{kin}+E_\mathrm{pot}. \tag{5.2}$$

Ein einzelner Summand heißt __ebene Welle__ (im Raum sind die Flächen gleicher Phase Ebenen), auf die Länge $L$ normiert $\psi(x)=\mathrm{e}^{\mathrm{j} kx}/\sqrt L$, in drei Dimensionen $\psi(\boldsymbol r)=C\,\mathrm{e}^{\mathrm{j}\boldsymbol k\cdot\boldsymbol r}$ mit

<span class="anker" id="gl-5-3"></span>
$$E(k_x,k_y,k_z)=\frac{\hbar^2k_x^2}{2m}+\frac{\hbar^2k_y^2}{2m}+\frac{\hbar^2k_z^2}{2m}+V_0. \tag{5.3}$$
:::

:::herleitung Ansatz einsetzen
Mit $V=V_0$ und der Abkürzung $k^2=2m(E-V_0)/\hbar^2$ wird [(4.3)](die-schrodinger-gleichung.html#gl-4-3) zu

$$\frac{\mathrm{d}^2\psi}{\mathrm{d} x^2}=-k^2\,\psi.$$

Das ist die Gleichung einer Welle. Ihre allgemeine Lösung ist [(5.1)](#gl-5-1) oder gleichwertig reell $\psi(x)=C_1\sin kx+C_2\cos kx$. Einsetzen von $\mathrm{e}^{\mathrm{j} kx}$ in [(4.3)](die-schrodinger-gleichung.html#gl-4-3) gibt $\bigl(\hbar^2k^2/(2m)+V_0\bigr)\psi=E\,\psi$, also [(5.2)](#gl-5-2).
:::

⁠**So liest man das:** Die Kurve $E(k)$ ist eine Parabel (Abb. [5](#abb-5)). Ihr Scheitel $V_0$ ist die potentielle Energie, die Höhe über dem Scheitel die kinetische. Jedes $k$ ist erlaubt, denn nichts schränkt das Elektron ein. $+k$ läuft nach rechts, $-k$ nach links, beide mit derselben Energie. Mit Zeitfaktor ist die ebene Welle die Welle [(3.3)](die-wellenfunktion-und-ihre-deutung.html#gl-3-3) mit $\hbar\omega=E$. Der Vergleich mit der Klassik liefert die de-Broglie-Beziehung aus der Gleichung selbst:

<span class="anker" id="gl-5-4"></span>
$$E_\mathrm{kin}=\frac12mv^2=\frac{(mv)^2}{2m}=\frac{p^2}{2m}=\frac{\hbar^2k^2}{2m}\quad\Rightarrow\quad p=\hbar k,\qquad E_\mathrm{kin}=\frac{\hbar^2(2\pi)^2}{2m\lambda^2}=\frac{h^2}{2m\lambda^2}. \tag{5.4}$$

Dasselbe sagt der Operator: $\hat p\,\mathrm{e}^{\mathrm{j} kx}=\hbar k\,\mathrm{e}^{\mathrm{j} kx}$, die ebene Welle hat einen festen Impuls. $E$ misst man in J oder eV. **Gültigkeit:** $V$ konstant und $E\ge V_0$. Für $E<V_0$ wäre $k^2$ negativ und die kinetische Energie klassisch kleiner als null, eine ebene Welle gibt es dann nicht.

:::abbildung gemb1/k1parabel 5
Links: Dispersionsrelation für $V_0=1$ eV und $m=m_0$. Am grünen Punkt ($k=5{,}12$/nm) ist die kinetische Energie 1 eV. Rechts: Die Wellen $\operatorname{Re}\psi$ zu den vier markierten Punkten, jeweils auf der Höhe ihrer Energie. Je höher die Energie, desto kürzer die Wellenlänge.
:::

**Beispiel.** Es ist $\hbar^2/(2m_0)=0{,}0381\,\mathrm{eV\,nm^2}$. Das Probe-Elektron mit $k=5{,}12$/nm und $V_0=0$ hat $E=0{,}0381\cdot5{,}12^2\,\mathrm{eV}=1{,}00$ eV. Bei $V_0=2$ eV liegt dieselbe Welle bei 3 eV: Nur $E-V_0$ bestimmt die Welle. **Grenzfälle:** Für $k\to0$ gehen $E\to V_0$ und $\lambda\to\infty$, $\psi$ wird konstant, das Elektron ruht. Für $m\to\infty$ wird die Parabel flach.

:::frage Quantenmechanik heißt doch, dass Energie nur in Stufen vorkommt. Warum ist hier jedes $k$ erlaubt?
Stufen entstehen erst, wenn ein Potential das Elektron einschränkt (Stufe [4](die-schrodinger-gleichung.html#stufe-4)). Die Energie des freien Elektrons kann jeden Wert ab $V_0$ annehmen. Quantenmechanisch ist hier die Beschreibung als Welle, nicht die Energie.
:::

:::aufgabe Aufgabe 5 ★ Über eine Stufe
<span class="anker" id="aufg-5"></span>

Ein Elektron mit der Gesamtenergie $E=0{,}5$ eV läuft aus einem Gebiet mit $V=0$ in ein Gebiet mit $V=0{,}35$ eV.

<ol class="al">

<li>

Berechne $k$, $\lambda$ und die Geschwindigkeit $v=p/m_0$ in beiden Gebieten.

</li>

<li>

Skizziere beide Parabeln mit derselben Energie $E$. Wodurch wird das Elektron rechts langsamer?

</li>

<li>

Was ändert sich grundsätzlich, wenn rechts $V=0{,}6$ eV gilt?

</li>

</ol>

:::loesung
(a) Links ist $E_\mathrm{kin}=0{,}5$ eV: $k=3{,}62\cdot10^{9}\,\mathrm{m^{-1}}$, $\lambda=1{,}73$ nm, $v=4{,}19\cdot10^{5}$ m/s. Rechts ist $E_\mathrm{kin}=0{,}15$ eV: $k=1{,}98\cdot10^{9}\,\mathrm{m^{-1}}$, $\lambda=3{,}17$ nm, $v=2{,}30\cdot10^{5}$ m/s. (b) Die Gesamtenergie bleibt gleich, der Scheitel der Parabel liegt rechts um 0,35 eV höher. Vom Abstand zum Scheitel bleibt weniger, also sinken $k$ und $v$, die Wellenlänge wächst. (c) Dann ist $E<V$ und $k^2<0$. Es gibt rechts keine ebene Welle mehr.
:::
:::

:::aufgabe Aufgabe 6 ★★ Drei Dimensionen
<span class="anker" id="aufg-6"></span>

<ol class="al">

<li>

Setze $\psi(x,y,z)=\psi_1(x)\,\psi_2(y)\,\psi_3(z)$ in die Gleichung für $V=V_0$ ein und leite [(5.3)](#gl-5-3) her.

</li>

<li>

Für $(k_x,k_y,k_z)=(2;\,1;\,2)\cdot10^{9}\,\mathrm{m^{-1}}$ und $V_0=0{,}1$ eV: Berechne $|\boldsymbol k|$, $\lambda$, $E$ und die Laufrichtung.

</li>

</ol>

:::loesung
(a) Teilen durch $\psi_1\psi_2\psi_3$ gibt $-\frac{\hbar^2}{2m}\bigl(\psi_1''/\psi_1+\psi_2''/\psi_2+\psi_3''/\psi_3\bigr)+V_0=E$. Jeder Quotient hängt nur von einer Variablen ab, die Summe ist konstant, also ist jeder einzelne konstant: $\psi_1''/\psi_1=-k_x^2$ und so weiter. Daraus folgen $\psi_1=\mathrm{e}^{\mathrm{j} k_xx}$, $\psi_2=\mathrm{e}^{\mathrm{j} k_yy}$, $\psi_3=\mathrm{e}^{\mathrm{j} k_zz}$, das Produkt $\mathrm{e}^{\mathrm{j}\boldsymbol k\cdot\boldsymbol r}$ und [(5.3)](#gl-5-3). (b) $|\boldsymbol k|=3\cdot10^{9}\,\mathrm{m^{-1}}$, $\lambda=2{,}09$ nm, $E_\mathrm{kin}=0{,}0381\cdot9\,\mathrm{eV}=0{,}343$ eV, $E=0{,}443$ eV. Die Laufrichtung ist $(2;1;2)/3$.
:::
:::

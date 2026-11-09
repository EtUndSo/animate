---
title: Stufe 7: Die Inversionsschicht als Quantentopf
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Die MOS-Kapazität
order: 4250900
summary: Die Elektronen sitzen in einer Schicht von wenigen Nanometern.
tags: Subbändern, zweidimensionales Elektronengas
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Die Elektronen sitzen in einer Schicht von wenigen Nanometern. Diese Stufe zeigt, dass dann die Quantenmechanik die erlaubten Energien festlegt.
:::

**Die Idee.** Auf der einen Seite begrenzt der Isolator die Elektronen mit einer Wand von 3,15 eV, auf der anderen drückt das Feld sie zur Grenzfläche zurück. So entsteht ein Topf, im Wesentlichen dreieckig (Abb. [7](#abb-7), grau). Er ist schmaler als die Wellenlänge der Elektronen, die bei der Energie $k_\mathrm BT$ und der Masse $0{,}19\,m_0$ rund 18 nm beträgt. Die Bewegung senkrecht zur Grenzfläche ist also eingesperrt wie in der Box ([Teil 2](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/das-teilchen-in-der-box/das-teilchen-in-der-box.html)), parallel dazu bleibt sie frei. Aus dem Leitungsband wird eine Folge von __Subbändern__, die Elektronen bilden ein __zweidimensionales Elektronengas__.

:::satz Satz 7.1 (Subbänder im Kastenmodell)
<span class="anker" id="satz-7-1"></span>

Ein Kasten der Breite $L_x$ senkrecht zur Grenzfläche ergibt $k_x=n\pi/L_x$ mit $n=1,2,\dots$ und

<span class="anker" id="gl-7-1"></span>
$$E=\frac{\hbar^2k_y^2}{2m_y}+\frac{\hbar^2k_z^2}{2m_z}+E_n+V_0,\qquad E_n=\frac{\hbar^2\pi^2n^2}{2m_xL_x^2}. \tag{7.1}$$
:::

⁠**So liest man das:** $x$ zeigt ins Substrat, $y$ und $z$ liegen in der Grenzfläche. $V_0=E_\mathrm{C,0}$ ist der Boden des Topfs. Der Kasten ist eine Näherung für das Dreieck. Jedes $n$ gibt ein Subband mit eigener Parabel in $k_y$, $k_z$. In Silizium zählt zusätzlich, wie die sechs Täler ([Teil 9](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/bandstrukturen-lesen/bandstrukturen-lesen.html)) liegen. An einer $(100)$-Grenzfläche zeigen zwei Täler mit der langen Achse in $x$-Richtung: $m_x=m_\mathrm h^*=0{,}92\,m_0$, in der Ebene $0{,}19\,m_0$. Die vier anderen haben $m_x=m_\mathrm l^*=0{,}19\,m_0$, in der Ebene $0{,}92\,m_0$ und $0{,}19\,m_0$. Große $m_x$ gibt kleine $E_n$, also entstehen zwei Leitern von Subbändern, $E_n^\mathrm h$ und $E_n^\mathrm l$.

:::abbildung gemb1/k15topf 7
Links: Kasten mit $L_x=5$ nm und seine Niveaus, grau der klassisch gerechnete Verlauf von $E_\mathrm C$ bei $V_\mathrm G=V_\mathrm{th}+1$ V. Blau die schwere Leiter $E_n^\mathrm h$, orange die leichte $E_1^\mathrm l$. Rechts: Die Flächenzustandsdichte wächst an jedem Niveau um eine Stufe.
:::

Jedes Subband hat eine konstante Zustandsdichte ([Teil 10](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/zustandsdichte-und-fermi-verteilung/zustandsdichte-und-fermi-verteilung.html)), je Tal $\sqrt{m_ym_z}/(\pi\hbar^2)$ pro Fläche und Energie. Die Flächendichte der Elektronen und ihre Ladung sind

<span class="anker" id="gl-7-2"></span>
$$n_\mathrm s=\int\!\mathrm{d} E\,D_\mathrm s(E)\,f(E),\qquad Q'_\mathrm{inv}=-e\,n_\mathrm s=\int_0^\infty\!\mathrm{d} x\,\bigl(-e\,n(x)\bigr). \tag{7.2}$$

Mit wachsender Gatespannung rückt $E_\mathrm F$ über weitere Stufen von $D_\mathrm s$. Die Zustandsdichte nimmt zu, also auch die Ladungsträgerdichte.

::::beispiel
Mit $L_x=5$ nm ist $E_1^\mathrm h=16$ meV, $E_2^\mathrm h=65$ meV und $E_1^\mathrm l=79$ meV. Die Abstände liegen also bei wenigen $k_\mathrm BT$, und die Quantisierung ist bei 300 K deutlich. Die schwere Leiter hat zwei Täler mit $D_\mathrm s=2\cdot0{,}19\,m_0/(\pi\hbar^2)=1{,}59\cdot10^{14}/(\mathrm{eV\,cm^2})$, die leichte vier mit $4\cdot0{,}418\,m_0/(\pi\hbar^2)=6{,}99\cdot10^{14}/(\mathrm{eV\,cm^2})$. Die $1{,}6\cdot10^{12}$ Elektronen je cm$^2$ aus Stufe [6](die-schwellspannung.html#stufe-6) füllen nur 10 meV des untersten Subbands bei $T=0$.
::::

⁠**Grenzfall:** Für $L_x\to\infty$ rücken die Stufen zusammen, die Treppe wird zur Wurzelkurve der dreidimensionalen Zustandsdichte.

:::frage Wenn die Elektronen quantisiert sind, stimmt dann die klassische Rechnung aus Stufe [6](die-schwellspannung.html#stufe-6) noch?
Für die Ladung fast ganz. Sie folgt aus dem Plattenkondensator [(6.2)](die-schwellspannung.html#gl-6-2), nicht aus den Details der Schicht. Die Quantisierung hebt das unterste Niveau um einige 10 meV, das ändert $V_\mathrm{th}$ nur wenig. Für die Form der Schicht und die Zahl der Zustände braucht man sie aber.
:::

:::aufgabe Aufgabe 9 ★★ Subbänder füllen
<span class="anker" id="aufg-9"></span>

Eine Inversionsschicht wird durch $L_x=4$ nm beschrieben.

<ol class="al">

<li>

Berechne $E_1^\mathrm h$, $E_2^\mathrm h$ und $E_1^\mathrm l$. Welches Niveau folgt auf $E_1^\mathrm h$?

</li>

<li>

Bei $T=0$ gilt im untersten Subband $n_\mathrm s=D_\mathrm s(E_\mathrm F-V_0-E_1^\mathrm h)$. Wie weit liegt $E_\mathrm F$ über $V_0+E_1^\mathrm h$ bei $n_\mathrm s=3\cdot10^{12}\,\mathrm{cm^{-2}}$?

</li>

<li>

Wie viele Elektronen je cm$^2$ passen unter das nächste Niveau?

</li>

<li>

Vorhersage: Wie ändert sich $E_1^\mathrm h$, wenn die Schicht doppelt so breit ist?

</li>

</ol>

:::loesung
(a) $E_1^\mathrm h=0{,}376\,\mathrm{eV\,nm^2}/(0{,}92\cdot16\,\mathrm{nm^2})=25{,}5$ meV, $E_2^\mathrm h=102$ meV, $E_1^\mathrm l=124$ meV. Als Nächstes folgt $E_2^\mathrm h$. (b) $n_\mathrm s/D_\mathrm s=3\cdot10^{12}/1{,}59\cdot10^{14}\,\mathrm{eV}=18{,}9$ meV. (c) Abstand $E_2^\mathrm h-E_1^\mathrm h=76{,}6$ meV, also $n_\mathrm s=1{,}2\cdot10^{13}\,\mathrm{cm^{-2}}$. (d) $E_n\propto1/L_x^2$: ein Viertel, 6,4 meV.
:::
:::

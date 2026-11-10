---
title: Stufe 4: Feld, Potential und Weite der Zone
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Der p-n-Übergang
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/der-p-n-ubergang
knoten: Kapitel 14: Der p-n-Übergang
order: 4240600
summary: Die Ladung ist nun ein Kasten.
tags: 
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Die Ladung ist nun ein Kasten. Diese Stufe integriert ihn zweimal und bestimmt daraus, wie breit die Zone wird und wie stark ihr Feld ist.
:::

**Die Idee.** Abb. [4](#abb-4) zeigt die Kette von oben nach unten. Konstante Ladung ergibt nach [(1.2)](wie-ladung-die-bander-verbiegt.html#gl-1-2) ein lineares Feld, ein lineares Feld ein parabelförmiges Potential. Am Rand der Zone endet das Feld, denn jenseits ist alles neutral. Zwei Bedingungen legen die Weiten fest. Beide Seiten tragen gleich viel Ladung, sonst bliebe draußen ein Feld. Und die Stufe beider Parabeln zusammen muss $\Phi_\mathrm{bi}$ ergeben.

:::abbildung gemb1/k14verlauf 4
Der Übergang des Rechenmodells in Schottky-Näherung, von oben nach unten: Raumladung als Kasten, Feld als Dreieck mit dem Maximum 4,43 MV/m bei $x=0$, Potential mit 0,762 V Stufe, Bänder als Spiegelbild des Potentials. Die Zone reicht 57 nm in das p-Gebiet und 287 nm in das n-Gebiet.
:::

:::satz Satz 4.1 (Feld und Bandverlauf)
<span class="anker" id="satz-4-1"></span>

In der Zone gilt, bezogen auf $\varphi(-L_\mathrm{depl}^\mathrm A)=0$,

<span class="anker" id="gl-4-1"></span>
$$\mathcal E(x)=\begin{cases}-\dfrac{eN_\mathrm A}{\varepsilon}\bigl(x+L_\mathrm{depl}^\mathrm A\bigr),&x\le0,\\[2mm]-\dfrac{eN_\mathrm D}{\varepsilon}\bigl(L_\mathrm{depl}^\mathrm D-x\bigr),&x\ge0,\end{cases}\quad \varphi(x)=\begin{cases}\dfrac{eN_\mathrm A}{2\varepsilon}\bigl(x+L_\mathrm{depl}^\mathrm A\bigr)^2,&x\le0,\\[2mm]U_\mathrm d-\dfrac{eN_\mathrm D}{2\varepsilon}\bigl(L_\mathrm{depl}^\mathrm D-x\bigr)^2,&x\ge0.\end{cases} \tag{4.1}$$

Als Bandverlauf $\Phi=e(U_\mathrm d-\varphi)$, bezogen auf das n-Gebiet, mit $\varepsilon=\varepsilon_0\varepsilon_\mathrm r$:

<span class="anker" id="gl-4-2"></span>
$$\Phi_\mathrm n(x)=\frac{e^2}{2\varepsilon}N_\mathrm D\bigl(L_\mathrm{depl}^\mathrm D-x\bigr)^2,\ x\ge0,\qquad\Phi_\mathrm p(x)=\Phi_\mathrm{bi}-\frac{e^2}{2\varepsilon}N_\mathrm A\bigl(L_\mathrm{depl}^\mathrm A+x\bigr)^2,\ x\le0. \tag{4.2}$$
:::

:::satz Satz 4.2 (Weite der Zone)
<span class="anker" id="satz-4-2"></span>

Mit der Ladungsneutralität $L_\mathrm{depl}^\mathrm AN_\mathrm A=L_\mathrm{depl}^\mathrm DN_\mathrm D$ gilt

<span class="anker" id="gl-4-3"></span>
$$L_\mathrm{depl}^\mathrm A=\sqrt{\frac{N_\mathrm D}{N_\mathrm A+N_\mathrm D}\cdot\frac{2\varepsilon\,\Phi_\mathrm{bi}}{e^2N_\mathrm A}},\qquad L_\mathrm{depl}^\mathrm D=\sqrt{\frac{N_\mathrm A}{N_\mathrm A+N_\mathrm D}\cdot\frac{2\varepsilon\,\Phi_\mathrm{bi}}{e^2N_\mathrm D}}, \tag{4.3}$$

<span class="anker" id="gl-4-4"></span>
$$L_\mathrm{depl}=L_\mathrm{depl}^\mathrm A+L_\mathrm{depl}^\mathrm D=\sqrt{\frac{2\varepsilon U_\mathrm d}{e}\cdot\frac{N_\mathrm A+N_\mathrm D}{N_\mathrm AN_\mathrm D}},\qquad|\mathcal E_\mathrm{max}|=\frac{eN_\mathrm DL_\mathrm{depl}^\mathrm D}{\varepsilon}=\frac{2U_\mathrm d}{L_\mathrm{depl}}. \tag{4.4}$$
:::

⁠**So liest man das:** $\mathcal E<0$ heißt: Das Feld zeigt nach links, vom n- zum p-Gebiet. Es ist bei $x=0$ am größten, denn dort liegt die ganze negative Ladung links und die ganze positive rechts. $U_\mathrm d$ ist die Fläche unter dem Felddreieck. $L_\mathrm{depl}$ liegt bei 10 nm bis einige µ m. **Gültigkeit:** Gleichgewicht, Schottky-Näherung, Dichten in m$^{-3}$ einsetzen.

:::herleitung Zweimal integrieren
⁠**Feld:** Auf der p-Seite ist $\mathrm{d}\mathcal E/\mathrm{d} x=-eN_\mathrm A/\varepsilon$ mit $\mathcal E(-L_\mathrm{depl}^\mathrm A)=0$, auf der n-Seite $\mathrm{d}\mathcal E/\mathrm{d} x=+eN_\mathrm D/\varepsilon$ mit $\mathcal E(L_\mathrm{depl}^\mathrm D)=0$. Bei $x=0$ liegt keine Flächenladung, also ist $\mathcal E$ dort stetig. Das verlangt $N_\mathrm AL_\mathrm{depl}^\mathrm A=N_\mathrm DL_\mathrm{depl}^\mathrm D$, und das ist die Ladungsneutralität.

⁠**Potential:** Integrieren von $\mathrm{d}\varphi/\mathrm{d} x=-\mathcal E$ mit $\varphi(-L_\mathrm{depl}^\mathrm A)=0$ und $\varphi(L_\mathrm{depl}^\mathrm D)=U_\mathrm d$ ergibt [(4.1)](#gl-4-1). Der Bandverlauf ist überall stetig. Bei $x=0$ heißt das

<span class="anker" id="gl-4-5"></span>
$$\frac{eN_\mathrm A}{2\varepsilon}\bigl(L_\mathrm{depl}^\mathrm A\bigr)^2=U_\mathrm d-\frac{eN_\mathrm D}{2\varepsilon}\bigl(L_\mathrm{depl}^\mathrm D\bigr)^2,\quad\text{also}\quad\frac{2\varepsilon U_\mathrm d}{e}=N_\mathrm A\bigl(L_\mathrm{depl}^\mathrm A\bigr)^2+N_\mathrm D\bigl(L_\mathrm{depl}^\mathrm D\bigr)^2. \tag{4.5}$$

⁠**Weiten:** Einsetzen von $L_\mathrm{depl}^\mathrm A=L_\mathrm{depl}^\mathrm DN_\mathrm D/N_\mathrm A$ ergibt $\bigl(L_\mathrm{depl}^\mathrm D\bigr)^2N_\mathrm D(N_\mathrm A+N_\mathrm D)/N_\mathrm A=2\varepsilon U_\mathrm d/e$. Mit $\Phi_\mathrm{bi}=eU_\mathrm d$ ist das [(4.3)](#gl-4-3).
:::

::::beispiel
Mit $U_\mathrm d=0{,}762$ V ergibt [(4.3)](#gl-4-3) $L_\mathrm{depl}^\mathrm A=57$ nm und $L_\mathrm{depl}^\mathrm D=287$ nm, zusammen 344 nm. Beide Seiten tragen $2{,}87\cdot10^{11}$ Ionen je cm$^2$. Das Feld erreicht ohne äußere Spannung 4,43 MV/m, also 44 kV/cm. Die Bandverbiegung verteilt sich wie die Weiten: 0,635 eV im n-Gebiet, 0,127 eV im p-Gebiet.
::::

⁠**Grenzfälle:** Für $N_\mathrm A=N_\mathrm D$ ist die Zone symmetrisch. Für $N_\mathrm A\gg N_\mathrm D$ liegt sie fast ganz im n-Gebiet, $L_\mathrm{depl}\approx\sqrt{2\varepsilon U_\mathrm d/(eN_\mathrm D)}$: Das ist ein einseitiger Übergang.

:::frage Warum reicht die Zone weiter in das schwächer dotierte Gebiet?
Beide Seiten müssen dieselbe Ladung stellen. Im schwach dotierten Gebiet sitzen die Ionen dünner, also braucht es mehr Tiefe. Das Verhältnis ist exakt $L_\mathrm{depl}^\mathrm D/L_\mathrm{depl}^\mathrm A=N_\mathrm A/N_\mathrm D$. Stärkere Dotierung macht die Zone dünner: Dieselbe Ladung passt in eine schmalere Schicht.
:::

:::aufgabe Aufgabe 4 ★★ Dotierung erhöhen
<span class="anker" id="aufg-4"></span>

Ein Übergang hat $N_\mathrm D=2\cdot10^{16}\,\mathrm{cm^{-3}}$. Vergleiche $N_\mathrm A=2\cdot10^{16}$, $2\cdot10^{17}$ und $2\cdot10^{18}\,\mathrm{cm^{-3}}$.

<ol class="al">

<li>

Berechne jeweils $U_\mathrm d$, $L_\mathrm{depl}^\mathrm A$, $L_\mathrm{depl}^\mathrm D$, $L_\mathrm{depl}$ und $|\mathcal E_\mathrm{max}|$.

</li>

<li>

Vorhersage: Warum ändert sich $L_\mathrm{depl}^\mathrm D$ im letzten Schritt kaum noch?

</li>

<li>

Zeige für $N_\mathrm A=N_\mathrm D$: $L_\mathrm{depl}^\mathrm A=L_\mathrm{Deb}\sqrt{\Phi_\mathrm{bi}/(k_\mathrm BT)}$. Warum ist die Schottky-Näherung bei jeder Dotierung ähnlich gut?

</li>

</ol>

:::loesung
(a) Für $N_\mathrm A=2\cdot10^{16}$: 0,756 V, 156 nm, 156 nm, 313 nm, 4,84 MV/m. Für $2\cdot10^{17}$: 0,816 V, 21,9 nm, 219 nm, 241 nm, 6,77 MV/m. Für $2\cdot10^{18}$: 0,875 V, 2,4 nm, 237 nm, 239 nm, 7,32 MV/m. (b) Für $N_\mathrm A\gg N_\mathrm D$ ist $L_\mathrm{depl}^\mathrm D\approx\sqrt{2\varepsilon U_\mathrm d/(eN_\mathrm D)}$, das hängt kaum noch von $N_\mathrm A$ ab. (c) Für $N_\mathrm A=N_\mathrm D=N$ ist $(L_\mathrm{depl}^\mathrm A)^2=\varepsilon\Phi_\mathrm{bi}/(e^2N)=L_\mathrm{Deb}^2\,\Phi_\mathrm{bi}/(k_\mathrm BT)$. Die Wurzel ist hier 5,4. $\Phi_\mathrm{bi}$ hängt nur logarithmisch von $N$ ab: Von $10^{14}$ bis $10^{18}\,\mathrm{cm^{-3}}$ wächst die Wurzel nur von 4,3 auf 6,1.
:::
:::

:::aufgabe Aufgabe 5 ★★★ Eine Zone nach Maß
<span class="anker" id="aufg-5"></span>

Ein Übergang mit $N_\mathrm A=10^{18}\,\mathrm{cm^{-3}}$ soll ohne äußere Spannung eine Zone von $L_\mathrm{depl}=2$ µ m haben.

<ol class="al">

<li>

Bestimme $N_\mathrm D$. $U_\mathrm d$ hängt selbst von $N_\mathrm D$ ab: Beginne mit $U_\mathrm d=0{,}8$ V und iteriere.

</li>

<li>

Wie groß sind $L_\mathrm{depl}^\mathrm A$ und $|\mathcal E_\mathrm{max}|$?

</li>

<li>

Ist die Schottky-Näherung auf beiden Seiten gerechtfertigt? Warum stört das Ergebnis der p-Seite nicht?

</li>

</ol>

:::loesung
(a) Einseitiger Übergang: $N_\mathrm D=2\varepsilon U_\mathrm d/(eL_\mathrm{depl}^2)$. Mit 0,8 V ist $N_\mathrm D=2{,}59\cdot10^{14}\,\mathrm{cm^{-3}}$, damit $U_\mathrm d=0{,}745$ V und $N_\mathrm D=2{,}41\cdot10^{14}\,\mathrm{cm^{-3}}$, dann $U_\mathrm d=0{,}743$ V und $N_\mathrm D=2{,}40\cdot10^{14}\,\mathrm{cm^{-3}}$. (b) $L_\mathrm{depl}^\mathrm A=L_\mathrm{depl}^\mathrm DN_\mathrm D/N_\mathrm A=0{,}48$ nm, $|\mathcal E_\mathrm{max}|=2U_\mathrm d/L_\mathrm{depl}=0{,}743$ MV/m. (c) n-Seite: $L_\mathrm{Deb}=264$ nm, Verhältnis 7,6, die Näherung gilt. p-Seite: $L_\mathrm{Deb}=4{,}1$ nm ist größer als $L_\mathrm{depl}^\mathrm A$, dort gibt es keinen Kasten. Das stört nicht: Auf diese Seite entfällt nur der Anteil $2{,}4\cdot10^{-4}$ der Verbiegung.
:::
:::

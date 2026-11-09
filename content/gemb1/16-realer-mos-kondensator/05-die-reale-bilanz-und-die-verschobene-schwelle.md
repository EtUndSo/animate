---
title: Stufe 3: Die reale Bilanz und die verschobene Schwelle
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Der reale MOS-Kondensator
order: 4260500
summary: Austrittsarbeit und Ladungen stecken nun in einer Zahl.
tags: 
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Austrittsarbeit und Ladungen stecken nun in einer Zahl. Diese Stufe zeigt, dass alle Gleichungen des idealen Kondensators weitergelten, nur um $V_\mathrm{FB}$ verschoben, und berechnet die reale Schwellspannung.
:::

**Die Idee.** Stellt man zuerst $V_\mathrm G=V_\mathrm{FB}$ ein, ist der Halbleiter genau im Zustand des idealen Kondensators ohne Spannung. Jede weitere Spannung $V_\mathrm G-V_\mathrm{FB}$ wirkt, als läge sie am idealen Kondensator, denn die festen Ladungen ändern sich nicht mehr. Alle Kurven des idealen Kondensators wandern also als Ganzes um $V_\mathrm{FB}$ auf der Spannungsachse (Abb. [3](#abb-3)).

:::satz Satz 3.1 (Bilanz des realen Kondensators)
<span class="anker" id="satz-3-1"></span>

<span class="anker" id="gl-3-1"></span>
$$V_\mathrm G=V_\mathrm{FB}+\varphi_\mathrm s-\frac{Q'_\mathrm{SC}}{C'_\mathrm{IS}}=\frac{\Delta\Phi}{e}+\varphi_\mathrm s+V_\mathrm{IS},\qquad V_\mathrm{IS}=-\frac{Q'_\mathrm{SC}}{C'_\mathrm{IS}}-\frac{Q'_\mathrm{IS}}{C'_\mathrm{IS}}-\frac{Q'_\mathrm{SS}}{C'_\mathrm{IS}}. \tag{3.1}$$

Für ein p-Substrat in Verarmung und schwacher Inversion gilt mit $\gamma=\sqrt{2\varepsilon eN_\mathrm A}/C'_\mathrm{IS}$

<span class="anker" id="gl-3-2"></span>
$$V_\mathrm G=V_\mathrm{FB}+\varphi_\mathrm s+\gamma\sqrt{\varphi_\mathrm s},\qquad V_\mathrm{WI}=V_\mathrm{FB}+\varphi_\mathrm{s,WI}+\gamma\sqrt{\varphi_\mathrm{s,WI}},\qquad V_\mathrm{th}=V_\mathrm{FB}+\varphi_\mathrm{s,SI}+\gamma\sqrt{\varphi_\mathrm{s,SI}}. \tag{3.2}$$
:::

⁠**So liest man das:** $V_\mathrm{IS}$ ist die ganze Spannung über dem Isolator. Sie enthält die Flachbandanteile und den Anteil $-Q'_\mathrm{SC}/C'_\mathrm{IS}$ der Ladung im Halbleiter. Oberhalb der Schwelle gilt weiter $Q'_\mathrm{inv}\approx-C'_\mathrm{IS}(V_\mathrm G-V_\mathrm{th})$. Für ein n-Substrat ist $\varphi_\mathrm s<0$ und $V_\mathrm{th}=V_\mathrm{FB}+\varphi_\mathrm{s,SI}-\gamma\sqrt{|\varphi_\mathrm{s,SI}|}$ mit $N_\mathrm D$ in $\gamma$. **Gültigkeit:** Die Ladungen hängen nicht von $V_\mathrm G$ ab.

:::herleitung Neutralität einsetzen
Mit Ladung im Halbleiter ist $Q'_\mathrm M=-Q'_\mathrm{SC}-Q'_\mathrm{IS}-Q'_\mathrm{SS}$ und $V_\mathrm{IS}=Q'_\mathrm M/C'_\mathrm{IS}$. Einsetzen in [(1.2)](verschiedene-austrittsarbeiten.html#gl-1-2) ergibt die zweite Form von [(3.1)](#gl-3-1), mit [(2.1)](feste-ladungen-im-isolator.html#gl-2-1) die erste. Die Ladung der Verarmung aus [Teil 15](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/die-mos-kapazitat/die-mos-kapazitaet.html) liefert [(3.2)](#gl-3-2).
:::

:::abbildung gemb1/k16schwelle 3
Oberflächenpotential des Rechenmodells, exakt gerechnet. Die reale Kurve (blau) ist die ideale (grau) um $V_\mathrm{FB}=-0{,}96$ V verschoben. Die Punkte markieren Flachband, Einsatz der schwachen und der starken Inversion.
:::

::::beispiel
Mit $V_\mathrm{FB}=-0{,}964$ V wird aus den idealen Werten $V_\mathrm{WI}=-0{,}964+0{,}749=-0{,}215$ V und $V_\mathrm{th}=-0{,}964+1{,}287=0{,}323$ V. Bei $V_\mathrm G=0$ ist $\varphi_\mathrm{s0}=0{,}539$ V (exakt 0,547 V), die Zone ist 152 nm breit. Die Isolatorspannung ist $-0{,}065$ V bei $V_\mathrm{FB}$, 0,360 V bei $V_\mathrm G=0$ und 0,445 V bei $V_\mathrm{th}$. Mit $\varphi_\mathrm s=0$, 0,539 und 0,777 V erfüllt jeder Wert [(3.1)](#gl-3-1) mit $\Delta\Phi/e=-0{,}899$ V. Bei $V_\mathrm{th}$ herrschen im Isolator 22,2 MV/m, im idealen Fall waren es 25,5 MV/m. **Stellschrauben:** $\Phi_\mathrm M=4{,}60$, 5,00 und 5,20 eV ergeben $V_\mathrm{th}=0{,}823$, 1,223 und 1,423 V. Die Dotierung wirkt über $\Phi_\mathrm{SC}$, $\varphi_\mathrm{s,SI}$ und $\gamma$. Ein n-Substrat mit $N_\mathrm D=3\cdot10^{16}\,\mathrm{cm^{-3}}$ und demselben Gate hat $\Phi_\mathrm{SC}=4{,}22$ eV, $V_\mathrm{FB}=-0{,}186$ V und $V_\mathrm{th}=-0{,}186-0{,}777-0{,}510=-1{,}473$ V.
::::

⁠**Grenzfall sehr dünner Isolator:** Ist $|Q'_\mathrm{SC}|/C'_\mathrm{IS}\ll|\varphi_\mathrm s|$, vereinfacht sich die Verarmung zu $V_\mathrm G\approx V_\mathrm{FB}+\varphi_\mathrm s$ und $V_\mathrm{IS}\approx-(Q'_\mathrm{IS}+Q'_\mathrm{SS})/C'_\mathrm{IS}$. Im p-Substrat wird dann $C'_\mathrm{depl}\approx\sqrt{e\varepsilon N_\mathrm A/(2(V_\mathrm G-V_\mathrm{FB}))}$, im n-Substrat steht $V_\mathrm{FB}-V_\mathrm G$. Bei $\varphi_\mathrm s=0{,}3$ V ist der Fehler mit 2 nm Oxid 0,03 V, im Rechenmodell mit 20 nm aber 0,32 V. Dort gilt die Vereinfachung nicht.

:::frage Die Schwelle liegt bei 0,32 V. Ist die Oberfläche bei $V_\mathrm G=0$ dann schon invertiert?
Schwach ja, stark nein. Es gilt $V_\mathrm{WI}<0<V_\mathrm{th}$. An der Grenzfläche überwiegen Elektronen mit $3{,}0\cdot10^{12}\,\mathrm{cm^{-3}}$ gegen $2{,}6\cdot10^{7}\,\mathrm{cm^{-3}}$ Löcher, aber die Dichte liegt weit unter $N_\mathrm A$.
:::

:::aufgabe Aufgabe 4 ★★ Einen realen Kondensator durchrechnen
<span class="anker" id="aufg-4"></span>

Gegeben sind $N_\mathrm A=2\cdot10^{16}\,\mathrm{cm^{-3}}$, 12 nm $\mathrm{SiO_2}$, $\Phi_\mathrm M=4{,}70$ eV, $Q'_\mathrm{IS}=-6\,\mathrm{nC/cm^2}$ und $Q'_\mathrm{SS}=+10\,\mathrm{nC/cm^2}$.

<ol class="al">

<li>

Berechne $\Delta\Phi$ und $V_\mathrm{FB}$.

</li>

<li>

Berechne $V_\mathrm{WI}$ und $V_\mathrm{th}$.

</li>

<li>

Berechne $\varphi_\mathrm{s0}$ und die Weite der Zone bei $V_\mathrm G=0$.

</li>

<li>

Berechne $V_\mathrm{IS}$ bei $V_\mathrm{FB}$, bei $V_\mathrm G=0$ und bei $V_\mathrm{th}$ sowie das Feld im Isolator bei $V_\mathrm{th}$.

</li>

</ol>

:::loesung
(a) $C'_\mathrm{IS}=287{,}8\,\mathrm{nF/cm^2}$, $\Phi_\mathrm{SC}=4{,}988$ eV, $\Delta\Phi=-0{,}288$ eV. Die Ladungen ergeben $-(-6+10)/287{,}8\,\mathrm{V}=-0{,}014$ V, also $V_\mathrm{FB}=-0{,}302$ V. (b) $\gamma=0{,}283\,\sqrt{\mathrm V}$, $V_\mathrm{WI}=-0{,}302+0{,}378+0{,}174=0{,}250$ V, $V_\mathrm{th}=-0{,}302+0{,}756+0{,}246=0{,}700$ V. (c) $\sqrt{\varphi_\mathrm{s0}}=-0{,}142+\sqrt{0{,}0200+0{,}302}=0{,}426$, also $\varphi_\mathrm{s0}=0{,}181$ V und $L_\mathrm{depl}=108$ nm. (d) $V_\mathrm{IS}=-0{,}014$ V bei $V_\mathrm{FB}$. Aus [(3.1)](#gl-3-1) folgen $0{,}288-0{,}181=0{,}107$ V bei $V_\mathrm G=0$ und $0{,}700+0{,}288-0{,}756=0{,}232$ V bei $V_\mathrm{th}$. Das Feld ist dort 19,4 MV/m.
:::
:::

:::aufgabe Aufgabe 5 ★★★ Schwelle einstellen
<span class="anker" id="aufg-5"></span>

Das Rechenmodell mit seinen festen Ladungen soll $V_\mathrm{th}=0{,}50$ V haben.

<ol class="al">

<li>

Welches $\Phi_\mathrm M$ braucht das Gate?

</li>

<li>

Ein späterer Schritt senkt $V_\mathrm{th}$ um 0,12 V. Welche zusätzliche Ladung an der Grenzfläche erklärt das?

</li>

<li>

Stattdessen steigt bei festem Gate die Dotierung auf $N_\mathrm A=5\cdot10^{16}\,\mathrm{cm^{-3}}$. Wie groß wird $V_\mathrm{th}$? Welche drei Größen ändern sich dabei?

</li>

</ol>

:::loesung
(a) $V_\mathrm{FB}=0{,}50-1{,}287=-0{,}787$ V. Mit dem Ladungsanteil $-0{,}065$ V folgt $\Delta\Phi=-0{,}722$ eV und $\Phi_\mathrm M=4{,}277$ eV. (b) Positive Ladung $0{,}12\,\mathrm{V}\cdot C'_\mathrm{IS}=20{,}7\,\mathrm{nC/cm^2}$. (c) Es ändern sich $\Phi_\mathrm{SC}=5{,}012$ eV, $\varphi_\mathrm{s,SI}=0{,}804$ V und $\gamma=0{,}746\,\sqrt{\mathrm V}$. Damit ist $V_\mathrm{th}=-0{,}800+0{,}804+0{,}669=0{,}673$ V.
:::
:::

---
title: Stufe 5: Transferkennlinie und Schwellspannung
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Der MOSFET
order: 4270700
summary: Bisher war V GS der Parameter einer Kurvenschar und V th eine gegebene Zahl.
tags: Body-Effekt
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Bisher war $V_\mathrm{GS}$ der Parameter einer Kurvenschar und $V_\mathrm{th}$ eine gegebene Zahl. Diese Stufe trägt den Strom über $V_\mathrm{GS}$ auf und zeigt, was $V_\mathrm{th}$ festlegt.
:::

**Die Idee.** $I_\mathrm D$ hängt von zwei Spannungen ab, ist also eine Fläche über der Ebene aus $V_\mathrm{GS}$ und $V_\mathrm{DS}$. Eine Ausgangskennlinie ist ein Schnitt bei festem $V_\mathrm{GS}$, die Transferkennlinie, auch Eingangskennlinie, ein Schnitt bei festem $V_\mathrm{DS}$. In Sättigung ist sie eine Parabel, die bei $V_\mathrm{th}$ beginnt.

$V_\mathrm{th}$ ist keine Eigenschaft des Siliziums. Bringt man Metall, Isolator und Silizium zusammen, stellt sich ein gemeinsames Fermi-Niveau ein, und an den Grenzflächen müssen Austrittsarbeiten und Elektronenaffinitäten zusammenpassen. Die Bänder sind deshalb schon ohne Spannung verbogen, die Gatespannung setzt auf diesem Zustand auf. Zwei Stellschrauben gibt es: die Austrittsarbeit des Gates und die Dotierung des Substrats.

:::satz Satz 5.1 (Transferkennlinie und Schwellspannung)
<span class="anker" id="satz-5-1"></span>

In Sättigung gilt [(4.1)](ausgangskennlinien.html#gl-4-1) mit

<span class="anker" id="gl-5-1"></span>
$$V_\mathrm{th}=V_\mathrm{FB}+\varphi_\mathrm{s,SI}-\frac{Q'_\mathrm{SC}(\varphi_\mathrm{s,SI})}{C'_\mathrm{IS}}=V_\mathrm{FB}+\varphi_\mathrm{s,SI}+\gamma\sqrt{\varphi_\mathrm{s,SI}},\qquad\gamma=\frac{\sqrt{2\varepsilon eN_\mathrm A}}{C'_\mathrm{IS}}. \tag{5.1}$$

Die schwache Inversion beginnt bei $V_\mathrm{WI}=V_\mathrm{FB}+\varphi_\mathrm{s,WI}+\gamma\sqrt{\varphi_\mathrm{s,WI}}$. Mit einer Spannung $V_\mathrm{SB}\ge0$ zwischen Source und Substrat wird daraus

<span class="anker" id="gl-5-2"></span>
$$V_\mathrm{th}(V_\mathrm{SB})=V_\mathrm{FB}+\varphi_\mathrm{s,SI}+\gamma\sqrt{\varphi_\mathrm{s,SI}+V_\mathrm{SB}}. \tag{5.2}$$
:::

⁠**So liest man das:** Die drei Summanden sind der Ausgleich der Materialien, die Bandverbiegung bis zur starken Inversion und die Ionenladung $Q'_\mathrm{SC}(\varphi_\mathrm{s,SI})=-eN_\mathrm AL_\mathrm{depl}=-\sqrt{2\varepsilon eN_\mathrm A\varphi_\mathrm{s,SI}}$ über dem Isolator. $\gamma$ heißt Substratsteuerfaktor. Die Änderung durch $V_\mathrm{SB}$ heißt __Body-Effekt__. **Gültigkeit:** Schottky-Näherung, Störstellenerschöpfung, $V_\mathrm{SB}\ge0$, sodass der Übergang zwischen Source und Substrat sperrt.

:::herleitung Warum das Substrat mitsteuert
Zwischen Gate und Substrat liegt $V_\mathrm{GS}+V_\mathrm{SB}$. Die Elektronen der Source stehen um $eV_\mathrm{SB}$ tiefer als die Löcher des Substrats. Die Bänder müssen deshalb um $V_\mathrm{SB}$ weiter biegen, also $\varphi_\mathrm s=\varphi_\mathrm{s,SI}+V_\mathrm{SB}$. Einsetzen in [(0.1)](von-grund-auf-was-aus-fruheren-teilen-gebraucht-wird.html#gl-0-1) mit der Ionenladung gibt $V_\mathrm{GS}+V_\mathrm{SB}=V_\mathrm{FB}+\varphi_\mathrm{s,SI}+V_\mathrm{SB}+\gamma\sqrt{\varphi_\mathrm{s,SI}+V_\mathrm{SB}}$. $V_\mathrm{SB}$ hebt sich einmal weg, unter der Wurzel bleibt es: Die Verarmungszone ist breiter, ihre Ladung trägt zusätzlich der Isolator.
:::

:::abbildung gemb1/k17schwelle 5
Links: Transferkennlinie des Rechenmodells in Sättigung. Die Farben zeigen den Zustand der Oberfläche: grau Akkumulation, orange Verarmung, hellblau schwache, blau starke Inversion. Rechts: $V_\mathrm{th}$ über der Dotierung bei 20 nm Isolator, rot das Rechenmodell. Das Gate verschiebt die Kurve, die Ionenladung biegt sie nach oben.
:::

::::beispiel
Das Rechenmodell hat $V_\mathrm{th}=-0{,}964+0{,}777+0{,}510=0{,}323$ V. Mit $V_\mathrm{WI}=-0{,}215$ V liegen die Zustände so:

| Akkumulation | Verarmung | schwache Inversion | starke Inversion |
|---|---|---|---|
| $V_\mathrm{GS}<-0{,}96$ V | $-0{,}96$ V bis $-0{,}21$ V | $-0{,}21$ V bis $0{,}32$ V | $V_\mathrm{GS}>0{,}32$ V |

Am Isolator liegt $V_\mathrm{IS}=-(Q'_\mathrm{SC}+Q'_\mathrm{IS}+Q'_\mathrm{SS})/C'_\mathrm{IS}$, an den drei Grenzen also $-0{,}065$, 0,295 und 0,445 V. Ein Gate mit $\Phi_\mathrm M=5{,}1$ eV hebt $V_\mathrm{th}$ auf 1,323 V, jedes eV mehr ergibt 1 V mehr. Mit Aluminium gibt $N_\mathrm A=10^{16}$ und $10^{17}\,\mathrm{cm^{-3}}$ die Werte 0,07 und 0,81 V. Unter $6{,}5\cdot10^{15}\,\mathrm{cm^{-3}}$ wird $V_\mathrm{th}$ negativ, der Transistor leitet dann schon bei $V_\mathrm{GS}=0$. $V_\mathrm{SB}=1$ V hebt $V_\mathrm{th}$ auf 0,584 V, $L_\mathrm{depl}$ wächst von 183 auf 277 nm, und $I_\mathrm{D,sat}$ fällt bei $V_\mathrm{GS}=3$ V von 3,09 auf 2,52 mA.
::::

⁠**Grenzfall:** Für $\gamma\to0$ (dünner Isolator) ist $V_\mathrm{th}\to V_\mathrm{FB}+\varphi_\mathrm{s,SI}$, und $V_\mathrm{SB}$ wirkt nicht mehr.

:::frage Warum wirkt eine Spannung am Substrat, wenn doch das Gate den Kanal steuert?
Die Verarmungszone ist die zweite Platte eines Kondensators zwischen Kanal und Substrat. Das Substrat zieht darüber am selben Oberflächenpotential wie das Gate. Es wirkt wie ein zweites, schwächeres Gate.
:::

:::aufgabe Aufgabe 6 ★★ Schwellspannung und Zustände
<span class="anker" id="aufg-6"></span>

Ein MOSFET hat $N_\mathrm A=5\cdot10^{16}\,\mathrm{cm^{-3}}$, 15 nm $\mathrm{SiO_2}$, $\Phi_\mathrm M=4{,}6$ eV und $Q'_\mathrm{IS}+Q'_\mathrm{SS}=6\,\mathrm{nC/cm^2}$.

<ol class="al">

<li>

Berechne $\Phi_\mathrm{SC}$, $V_\mathrm{FB}$, $\varphi_\mathrm{s,WI}$, $\varphi_\mathrm{s,SI}$ und $\gamma$.

</li>

<li>

Berechne $V_\mathrm{WI}$ und $V_\mathrm{th}$ und gib die Bereiche von $V_\mathrm{GS}$ für die vier Zustände an.

</li>

<li>

Welche Spannung liegt an den drei Grenzen am Isolator?

</li>

</ol>

:::loesung
(a) $\varphi_\mathrm{s,WI}=0{,}402$ V, $\varphi_\mathrm{s,SI}=0{,}804$ V, $\Phi_\mathrm{SC}=4{,}05+0{,}56+0{,}402=5{,}012$ eV. $C'_\mathrm{IS}=230{,}2\,\mathrm{nF/cm^2}$, also $(Q'_\mathrm{IS}+Q'_\mathrm{SS})/C'_\mathrm{IS}=0{,}026$ V und $V_\mathrm{FB}=-0{,}412-0{,}026=-0{,}438$ V. $\gamma=0{,}560\,\sqrt{\mathrm V}$. (b) $V_\mathrm{WI}=-0{,}438+0{,}402+0{,}355=0{,}319$ V, $V_\mathrm{th}=-0{,}438+0{,}804+0{,}502=0{,}868$ V. Akkumulation unter $-0{,}438$ V, Verarmung bis 0,319 V, schwache Inversion bis 0,868 V, darüber starke Inversion. (c) $V_\mathrm{IS}=-0{,}026$ V im Flachbandfall, $-(-81{,}7+6)/230{,}2\,\mathrm{V}=0{,}329$ V und $-(-115{,}5+6)/230{,}2\,\mathrm{V}=0{,}476$ V. Probe: $-0{,}412+0{,}804+0{,}476=0{,}868$ V.
:::
:::

:::aufgabe Aufgabe 7 ★★★ Vom Messwert zum Bauelement
<span class="anker" id="aufg-7"></span>

An einem Transistor misst man $V_\mathrm{th}=2{,}36$ V, $V_\mathrm{FB}=-0{,}90$ V und $\gamma=2{,}64\,\sqrt{\mathrm V}$, der Isolator ist $\mathrm{SiO_2}$. Bei $V_\mathrm{GS}=5$ V und $V_\mathrm{DS}=2$ V fließen 12 mA.

<ol class="al">

<li>

Ist das Substrat p- oder n-dotiert? Begründe mit den Vorzeichen.

</li>

<li>

Berechne $\varphi_\mathrm{s,SI}$, die Dotierung und $d_\mathrm{IS}$.

</li>

<li>

Bei welchem $V_\mathrm{GS}$ ist $p(0)=n_\mathrm i$?

</li>

<li>

Bestimme $K$. Welcher Strom fließt bei $V_\mathrm{SB}=0{,}5$ V, $V_\mathrm{GS}=4$ V und $V_\mathrm{DS}=1$ V?

</li>

</ol>

:::loesung
(a) $V_\mathrm{th}-V_\mathrm{FB}=3{,}26$ V ist positiv, die Bänder müssen nach unten biegen, also ist das Substrat p-dotiert. (b) Aus $\varphi+2{,}64\sqrt\varphi=3{,}26$ folgt $\sqrt\varphi=0{,}917$, also $\varphi_\mathrm{s,SI}=0{,}840$ V. Dann ist $N_\mathrm A=n_\mathrm i\mathrm{e}^{0{,}420/0{,}02585}=1{,}0\cdot10^{17}\,\mathrm{cm^{-3}}$, $C'_\mathrm{IS}=\sqrt{2\varepsilon eN_\mathrm A}/\gamma=69{,}5\,\mathrm{nF/cm^2}$ und $d_\mathrm{IS}=50$ nm. (c) Das ist der Einsatz der schwachen Inversion: $V_\mathrm{WI}=-0{,}90+0{,}420+2{,}64\cdot0{,}648=1{,}23$ V. (d) $V_\mathrm{GS}-V_\mathrm{th}=2{,}64$ V ist größer als 2 V, also ungesättigt: $K=12\,\mathrm{mA}/(2{,}64\cdot2-2)\,\mathrm{V^2}=3{,}66$ mA/V$^2$. Mit $V_\mathrm{SB}=0{,}5$ V ist $V_\mathrm{th}=-0{,}90+0{,}840+2{,}64\sqrt{1{,}340}=3{,}00$ V. Dann ist $V_\mathrm{GS}-V_\mathrm{th}=1{,}00$ V, knapp über $V_\mathrm{DS}$, und $I_\mathrm D=3{,}66\,\mathrm{mA/V^2}\cdot(1{,}00-0{,}5)\,\mathrm{V^2}=1{,}84$ mA. Ohne $V_\mathrm{SB}$ wären es 4,17 mA.
:::
:::

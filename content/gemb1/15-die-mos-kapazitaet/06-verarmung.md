---
title: Stufe 4: Verarmung
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Die MOS-Kapazität
order: 4250600
summary: Bei V mathrm G>0 drückt das Gate die Löcher von der Grenzfläche weg.
tags: Verarmungszone, Substratsteuerfaktor
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Bei $V_\mathrm G>0$ drückt das Gate die Löcher von der Grenzfläche weg. Diese Stufe berechnet, wie breit die entstehende Zone wird und welche Spannung dazu gehört.
:::

**Die Idee.** Das Gate stößt die freien Löcher ins Substrat. Zurück bleiben die ortsfesten Akzeptorionen $N_\mathrm A^-$. Sie sind vollständig ionisiert, denn $E_\mathrm F$ liegt weit über dem Akzeptorniveau, und Elektronen gibt es noch fast keine. Die Raumladung besteht also nur aus Ionen, wie auf einer Seite des p-n-Übergangs ([Teil 14](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/der-p-n-ubergang/der-p-n-uebergang.html)). Mehr als alle Löcher kann das Gate nicht entfernen. Mehr Ladung geht deshalb nur, wenn die Zone tiefer ins Substrat wächst. Ihre Dichte bleibt dabei $eN_\mathrm A$.

:::satz Satz 4.1 (Verarmungszone in der Schottky-Näherung)
<span class="anker" id="satz-4-1"></span>

Die __Verarmungszone__ reicht bis $L_\mathrm{depl}$, dort ist $\rho=-eN_\mathrm A$, dahinter $\rho=0$. Für $0\le x\le L_\mathrm{depl}$ gilt

<span class="anker" id="gl-4-1"></span>
$$\mathcal E(x)=\frac{eN_\mathrm A}{\varepsilon}\bigl(L_\mathrm{depl}-x\bigr),\qquad\varphi(x)=\frac{eN_\mathrm A}{2\varepsilon}\bigl(L_\mathrm{depl}-x\bigr)^2, \tag{4.1}$$

und jenseits davon $\mathcal E=\varphi=0$. Daraus folgen

<span class="anker" id="gl-4-2"></span>
$$L_\mathrm{depl}=\sqrt{\frac{2\varepsilon\,\varphi_\mathrm s}{eN_\mathrm A}},\qquad Q'_\mathrm{SC}=-eN_\mathrm AL_\mathrm{depl}=-\sqrt{2\varepsilon eN_\mathrm A\varphi_\mathrm s}, \tag{4.2}$$

<span class="anker" id="gl-4-3"></span>
$$V_\mathrm G=\varphi_\mathrm s+\gamma\sqrt{\varphi_\mathrm s},\qquad\gamma=\frac{\sqrt{2\varepsilon eN_\mathrm A}}{C'_\mathrm{IS}}. \tag{4.3}$$
:::

⁠**So liest man das:** $L_\mathrm{depl}$ ist die Weite der Zone, $\gamma$ der __Substratsteuerfaktor__, im Rechenmodell 0,578 $\sqrt{\mathrm V}$. Für ein n-Substrat sind $\rho=+eN_\mathrm D$, $\varphi(x)=-\frac{eN_\mathrm D}{2\varepsilon}(L_\mathrm{depl}-x)^2$ und $L_\mathrm{depl}=\sqrt{2\varepsilon|\varphi_\mathrm s|/(eN_\mathrm D)}$. **Gültigkeit:** Der Kasten braucht einen scharfen Rand, also $L_\mathrm{depl}\gg L_\mathrm D$. Wegen $L_\mathrm{depl}=L_\mathrm D\sqrt{2\varphi_\mathrm s/V_\mathrm T}$ heißt das $\varphi_\mathrm s\gg V_\mathrm T$. Außerdem muss $n(0)\ll N_\mathrm A$ sein.

:::herleitung Zweimal integrieren
Aus [(0.3)](von-grund-auf-was-aus-fruheren-teilen-gebraucht-wird.html#gl-0-3) folgt $\mathrm{d}\mathcal E/\mathrm{d} x=-eN_\mathrm A/\varepsilon$, mit $\mathcal E(L_\mathrm{depl})=0$ als Randbedingung, denn dahinter ist der Halbleiter neutral. Das gibt das Feld. $\mathrm{d}\varphi/\mathrm{d} x=-\mathcal E$ mit $\varphi(L_\mathrm{depl})=0$ gibt die Parabel. Bei $x=0$ steht $\varphi_\mathrm s=eN_\mathrm AL_\mathrm{depl}^2/(2\varepsilon)$, das ergibt $L_\mathrm{depl}$. Die Ladung ist Dichte mal Breite, und [(2.2)](wie-sich-die-gatespannung-aufteilt.html#gl-2-2) gibt $V_\mathrm G$.
:::

:::abbildung gemb1/k15verarmung 4
Rechenmodell bei $\varphi_\mathrm s=0{,}3$ V: Raumladung, Feld und Potential. Blau die Schottky-Näherung mit $L_\mathrm{depl}=114$ nm, grau die exakte Lösung. Die Löcher kehren über wenige $L_\mathrm D$ zurück, der wahre Rand ist also weich.
:::

**Beispiel.** Bei $\varphi_\mathrm s=0{,}3$ V ist $L_\mathrm{depl}=114$ nm, das 4,8-Fache von $L_\mathrm D$. Die Ladung ist $Q'_\mathrm{SC}=-54{,}7\,\mathrm{nC/cm^2}$, damit $V_\mathrm{IS}=0{,}317$ V und $V_\mathrm G=0{,}617$ V. Am Rand ist $\mathcal E(0)=2\varphi_\mathrm s/L_\mathrm{depl}=5{,}3$ MV/m, im Isolator 15,8 MV/m. Das Verhältnis ist $\varepsilon/\varepsilon_\mathrm{IS}=3$, denn die Grenzfläche trägt keine Ladung. Umgekehrt ist [(4.3)](#gl-4-3) eine quadratische Gleichung: $\sqrt{\varphi_\mathrm s}=-\gamma/2+\sqrt{\gamma^2/4+V_\mathrm G}$. **Grenzfall:** Bei sehr dünnem Isolator ist $\gamma\to0$ und $V_\mathrm G\approx\varphi_\mathrm s$. Mit 2 nm Oxid wären es hier nur 0,03 V am Isolator. Bei 20 nm liegen $V_\mathrm{IS}$ und $\varphi_\mathrm s$ dagegen gleichauf, $V_\mathrm{IS}$ darf man also nicht weglassen.

:::frage Warum wächst die Zone nur mit der Wurzel der Bandverbiegung?
Wächst die Zone, kommt zweierlei zusammen: mehr Ladung, und diese Ladung sitzt weiter weg. Die Spannung ist Ladung mal Abstand. Deshalb geht $L_\mathrm{depl}$ quadratisch ein: Die doppelte Bandverbiegung braucht nur die $\sqrt2$-fache Breite, 161 nm bei 0,6 V.
:::

:::aufgabe Aufgabe 4 ★★ Eine Verarmungszone durchrechnen
<span class="anker" id="aufg-4"></span>

Gegeben sind $N_\mathrm A=10^{17}\,\mathrm{cm^{-3}}$ und $d_\mathrm{IS}=10$ nm $\mathrm{SiO_2}$.

<ol class="al">

<li>

Berechne bei $\varphi_\mathrm s=0{,}4$ V die Größen $L_\mathrm{depl}$, $Q'_\mathrm{SC}$, $\mathcal E(0)$, $V_\mathrm{IS}$ und $V_\mathrm G$. Ist $L_\mathrm{depl}\gg L_\mathrm D$?

</li>

<li>

Welches $\varphi_\mathrm s$ stellt sich bei $V_\mathrm G=0{,}6$ V ein?

</li>

</ol>

:::loesung
$C'_\mathrm{IS}=345{,}3\,\mathrm{nF/cm^2}$, $\gamma=0{,}528\,\sqrt{\mathrm V}$. (a) $L_\mathrm{depl}=71{,}9$ nm, das 5,6-Fache von $L_\mathrm D=12{,}9$ nm. $Q'_\mathrm{SC}=-115{,}2\,\mathrm{nC/cm^2}$, $\mathcal E(0)=2\varphi_\mathrm s/L_\mathrm{depl}=11{,}1$ MV/m, $V_\mathrm{IS}=0{,}334$ V, $V_\mathrm G=0{,}734$ V. (b) $\sqrt{\varphi_\mathrm s}=-0{,}264+\sqrt{0{,}0696+0{,}6}=0{,}554$, also $\varphi_\mathrm s=0{,}307$ V und $V_\mathrm{IS}=0{,}293$ V.
:::
:::

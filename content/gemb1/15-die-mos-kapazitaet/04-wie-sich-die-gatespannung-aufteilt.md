---
title: Stufe 2: Wie sich die Gatespannung aufteilt
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Die MOS-Kapazität
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/die-mos-kapazitat
knoten: Kapitel 15: Die MOS-Kapazität
order: 4250400
summary: Eine Spannung am Gate muss irgendwo abfallen.
tags: Gatespannung
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Eine Spannung am Gate muss irgendwo abfallen. Diese Stufe zeigt, wo sie abfällt und wie die Bandverbiegung die Dichten an der Grenzfläche festlegt.
:::

**Die Idee.** Die __Gatespannung__ $V_\mathrm G$ liegt zwischen Gate und Substratrückseite. Im Metall schirmen freie Elektronen jedes Feld sofort ab, tief im Halbleiter ist alles neutral und feldfrei. Die Spannung fällt also nur im Isolator und in der Randschicht des Halbleiters ab, in der die Gegenladung sitzt. Da kein Strom fließt, ist jeder Stoff für sich im Gleichgewicht: $E_\mathrm F$ ist im Halbleiter waagerecht, $E_\mathrm{F,M}$ im Metall, und beide liegen um $eV_\mathrm G$ auseinander. Für das Bänderdiagramm (Abb. [2](#abb-2)) gelten drei Regeln. Im Halbleiter verlaufen $E_\mathrm{vac}$, $E_\mathrm C$, $E_\mathrm{Fi}$ und $E_\mathrm V$ parallel. Nur ihr Abstand zu $E_\mathrm F$ ändert sich mit dem Ort, und daraus entsteht die Raumladung. Im Isolator sitzt keine Ladung, das Feld ist konstant, die Bänder sind gerade und geneigt. An den Grenzflächen bleiben die Sprünge $E_\mathrm{C,IS}-E_\mathrm C$ und $E_\mathrm{C,IS}-E_\mathrm{F,M}$ erhalten.

:::abbildung gemb1/k15teilung 2
Links: Bänderdiagramm des Rechenmodells bei $V_\mathrm G=0{,}6$ V. Isolator und Metall sind breiter gezeichnet, Energien maßstäblich. Die 0,6 V teilen sich in $V_\mathrm{IS}=0{,}31$ V und $\varphi_\mathrm s=0{,}29$ V. Rechts: Die positive Ladung auf dem Metall und die negative Ladung im Halbleiter sind gleich groß (Höhen schematisch).
:::

:::definition Definition 2.1 (Oberflächenpotential)
<span class="anker" id="satz-2-1"></span>

$\varphi(x)$ ist das Potential im Halbleiter, $x=0$ die Grenzfläche zum Isolator, $x>0$ zeigt ins Substrat und $\varphi(x\to\infty)=0$. Das Oberflächenpotential ist

<span class="anker" id="gl-2-1"></span>
$$\varphi_\mathrm s=\varphi(0),\qquad e\varphi_\mathrm s=E_\mathrm{C,\infty}-E_\mathrm{C,0}. \tag{2.1}$$
:::

⁠**So liest man das:** $E_\mathrm{C,0}$ ist die Bandkante an der Grenzfläche, $E_\mathrm{C,\infty}$ die tief im Substrat. Bei $\varphi_\mathrm s>0$ biegen die Bänder zur Grenzfläche nach unten, bei $\varphi_\mathrm s<0$ nach oben.

:::satz Satz 2.2 (Spannungsbilanz des idealen MIS-Kondensators)
<span class="anker" id="satz-2-2"></span>

<span class="anker" id="gl-2-2"></span>
$$V_\mathrm G=V_\mathrm{IS}+\varphi_\mathrm s,\qquad V_\mathrm{IS}=-\frac{Q'_\mathrm{SC}}{C'_\mathrm{IS}},\qquad C'_\mathrm{IS}=\frac{\varepsilon_\mathrm{IS}}{d_\mathrm{IS}},\qquad E_\mathrm F-E_\mathrm{F,M}=eV_\mathrm G. \tag{2.2}$$
:::

⁠**So liest man das:** $Q'_\mathrm{SC}$ ist die gesamte Flächenladung im Halbleiter, $V_\mathrm{IS}$ die Spannung über dem Isolator. $C'_\mathrm{IS}$ ist im Rechenmodell 172,7 nF/cm$^2$. Bei $V_\mathrm G>0$ liegt $E_\mathrm{F,M}$ unter $E_\mathrm F$, denn positive Spannung senkt die Energie der Elektronen im Metall. **Gültigkeit:** kein Strom und keine weiteren Ladungen, also der ideale Fall aus Stufe [1](drei-stoffe-auf-einer-energieskala.html#stufe-1).

:::herleitung Plattenkondensator und Umlauf
Die ganze Struktur ist neutral, das Metall trägt also $Q'_\mathrm M=-Q'_\mathrm{SC}$. Das Feld im Isolator ist $\mathcal E_\mathrm{IS}=Q'_\mathrm M/\varepsilon_\mathrm{IS}$, die Spannung darüber $V_\mathrm{IS}=\mathcal E_\mathrm{IS}\,d_\mathrm{IS}=Q'_\mathrm M/C'_\mathrm{IS}$. Vom Gate bis ins Substrat fällt zuerst $V_\mathrm{IS}$ ab, dann $\varphi_\mathrm s-\varphi(\infty)=\varphi_\mathrm s$.
:::

:::satz Satz 2.3 (Dichten an der Grenzfläche)
<span class="anker" id="satz-2-3"></span>

Für ein p-Substrat mit $p_{p0}=N_\mathrm A$ und $n_{p0}=n_\mathrm i^2/N_\mathrm A$ gilt

<span class="anker" id="gl-2-3"></span>
$$p(0)=N_\mathrm A\exp\Bigl(-\frac{\varphi_\mathrm s}{V_\mathrm T}\Bigr),\quad n(0)=n_{p0}\exp\Bigl(\frac{\varphi_\mathrm s}{V_\mathrm T}\Bigr),\quad\varphi_\mathrm s=V_\mathrm T\ln\frac{N_\mathrm A}{p(0)}=V_\mathrm T\ln\frac{n(0)\,N_\mathrm A}{n_\mathrm i^2}. \tag{2.3}$$

Für ein n-Substrat ist $n(0)=N_\mathrm D\exp(\varphi_\mathrm s/V_\mathrm T)$ und $p(0)=(n_\mathrm i^2/N_\mathrm D)\exp(-\varphi_\mathrm s/V_\mathrm T)$.
:::

:::herleitung Nur die Bandkante verschiebt sich
Tief im Substrat ist $n_{p0}=N_\mathrm C\exp\bigl(-(E_\mathrm{C,\infty}-E_\mathrm F)/(k_\mathrm BT)\bigr)$, an der Grenzfläche steht $E_\mathrm{C,0}$ statt $E_\mathrm{C,\infty}$. Mit [(2.1)](#gl-2-1) wird daraus

$$n(0)=N_\mathrm C\exp\Bigl(-\frac{E_\mathrm{C,\infty}-e\varphi_\mathrm s-E_\mathrm F}{k_\mathrm BT}\Bigr)=n_{p0}\exp\Bigl(\frac{e\varphi_\mathrm s}{k_\mathrm BT}\Bigr).$$

$n\cdot p=n_\mathrm i^2$ gilt im Gleichgewicht an jedem Ort, also $p(0)=n_\mathrm i^2/n(0)$. Dasselbe gilt an jeder Stelle $x$ mit $\varphi(x)$ statt $\varphi_\mathrm s$.
:::

::::beispiel
Bei $\varphi_\mathrm s=0{,}2$ V ist $\varphi_\mathrm s/V_\mathrm T=7{,}74$. Dann ist $p(0)=1{,}3\cdot10^{13}\,\mathrm{cm^{-3}}$ und $n(0)=6{,}0\cdot10^{6}\,\mathrm{cm^{-3}}$. Je 59,5 mV ändern beide Dichten sich um den Faktor 10, die eine nach oben, die andere nach unten.
::::

⁠**Grenzfall:** $\varphi_\mathrm s=0$ ergibt die Werte tief im Substrat, keine Raumladung und $V_\mathrm G=0$.

:::frage Metall und Halbleiter haben verschiedene Fermi-Niveaus. Warum fließt dann kein Strom?
Verschiedene Fermi-Niveaus treiben nur dann einen Strom, wenn es einen Weg gibt. Der Isolator versperrt ihn. Beim Anlegen der Spannung fließt nur kurz der Ladestrom, bis die Platten geladen sind.
:::

:::aufgabe Aufgabe 2 ★★ Vom Messwert zum Potential
<span class="anker" id="aufg-2"></span>

Ein Substrat hat $N_\mathrm A=10^{16}\,\mathrm{cm^{-3}}$.

<ol class="al">

<li>

Berechne $\varphi_\mathrm s$ für $p(0)=2\cdot10^{18}$, $10^{16}$ und $10^{12}\,\mathrm{cm^{-3}}$. In welche Richtung biegen die Bänder jeweils?

</li>

<li>

Welches $\varphi_\mathrm s$ gehört zu $n(0)=10^{16}\,\mathrm{cm^{-3}}$? Wie groß ist dann $p(0)$?

</li>

<li>

Prüfe bei $\varphi_\mathrm s=0{,}2$ V, dass $n(0)\,p(0)$ nicht von $\varphi_\mathrm s$ abhängt. Warum muss das so sein?

</li>

</ol>

:::loesung
(a) Aus $\varphi_\mathrm s=V_\mathrm T\ln(N_\mathrm A/p(0))$: $-0{,}137$ V (Bänder nach oben), 0 (flach), $+0{,}238$ V (nach unten). (b) $\varphi_\mathrm s=V_\mathrm T\ln(10^{16}\cdot10^{16}/(8{,}9\cdot10^{9})^2)=0{,}72$ V, $p(0)=n_\mathrm i^2/n(0)=7{,}9\cdot10^{3}\,\mathrm{cm^{-3}}$. (c) $n(0)=7{,}9\cdot10^{3}\cdot\mathrm{e}^{7{,}74}\,\mathrm{cm^{-3}}$ und $p(0)=10^{16}\cdot\mathrm{e}^{-7{,}74}\,\mathrm{cm^{-3}}$, die Exponenten heben sich auf: $n(0)\,p(0)=7{,}9\cdot10^{19}\,\mathrm{cm^{-6}}=n_\mathrm i^2$. Der Grund: $E_\mathrm C$ und $E_\mathrm V$ verschieben sich um denselben Betrag, ihr Abstand $E_\mathrm g$ allein bestimmt das Produkt.
:::
:::

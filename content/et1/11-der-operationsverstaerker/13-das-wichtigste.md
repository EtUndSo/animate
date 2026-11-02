---
title: Das Wichtigste
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Der Operationsverstärker
order: 1211300
summary: Wie aus einem riesigen, ungenauen Faktor ein Bauteil wird, dessen Verhalten nur noch die Widerstände bestimmen
tags: Differenzverstärker, Schleifenverstärkung, virtuelle Masse, Rauschen, Komparator
lang: de
---

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Im Inneren sitzt ein __Differenzverstärker__, eine Schaltung, die nur auf den Unterschied zweier Spannungen reagiert: $U_\mathrm{A}=A\,U_\mathrm{D}$ mit $U_\mathrm{D}=\varphi_+-\varphi_-$. Bei $A=100000$ und höchstens 11 V am Ausgang bleibt für $U_\mathrm{D}$ ein Fenster von $\pm110$ µ V.

</li>

<li>

Gegenkopplung führt den Anteil $\beta$ des Ausgangs auf den Minus-Eingang. Der Ausgang läuft, bis die Schleife zur Ruhe kommt, und das ist, wenn $U_\mathrm{D}$ gerade für den Ausgang reicht: 5 V brauchen 50 µ V. Die Verstärkung wird $G\approx1/\beta$, die __Schleifenverstärkung__ $A\beta$ (der Faktor für einen Umlauf durch die Schleife) legt nur noch die kleine Abweichung fest.

</li>

<li>

Daraus folgt eine Regel: gleiche Potenziale an den Eingängen, kein Strom hinein, Knotenregel am Minus-Eingang. Sie erklärt die __virtuelle Masse__ (ein Knoten auf 0 V ohne Verbindung zur Masse) und alle Grundschaltungen. Sie endet, wo der Ausgang anschlägt, wo die Rückführung das Vorzeichen wechselt und wo $A\beta$ klein wird.

</li>

</ol>
:::

:::kern Das Wichtigste
<ul>

<li>

Rauschen: $u_\mathrm{r,eff}=\sqrt{\int|u_\mathrm{r}(f)|^2\mathrm{d} f}$, thermisch $|u_\mathrm{r,R}|^2=4k_\mathrm{B}TR$. Verstärken ändert das SNR nicht, es hilft nur gegen spätere Störungen. $\mathrm{SNR}_\mathrm{dB}=20\lg(u_\mathrm{s}/u_\mathrm{r})$.

</li>

<li>

Differenzverstärker: fester Summenstrom, $U_\mathrm{A}=S\,R_\mathrm{C}\,U_\mathrm{D}$, jede BE-Strecke trägt $U_\mathrm{D}/2$, Gleichtakt wirkt nicht.

</li>

<li>

Modell: $U_\mathrm{A}=A(\varphi_+-\varphi_-)$ bis zu den Anschlägen. Fenster $\pm110$ µ V, ohne Rückführung Komparator.

</li>

<li>

Gegenkopplung: $U_\mathrm{D}=U_\mathrm{E}/(1+A\beta)$, $G=\frac1\beta\cdot\frac1{1+1/(A\beta)}$, $\Delta G/G=\frac{1}{1+A\beta}\Delta A/A$. Der Ausgang läuft, bis die Schleife ruht. Bei 5 V bleiben 50 µ V.

</li>

<li>

Regel: $\varphi_+=\varphi_-$, $I_\pm=0$, Knotenregel am Minus-Eingang, zuletzt Grenzen prüfen. Virtuelle Masse: 0 V durch Regeln, kein Weg zur Masse. Der Strom läuft durch die Rückführung in den Ausgang.

</li>

<li>

$G=-R_2/R_1$, $G=1+R_2/R_1$, $U_\mathrm{A}=-R_\mathrm{F}\sum U_{\mathrm{E}i}/R_{\mathrm{E}i}$, $U_\mathrm{A}=\frac{R_2}{R_1}(U_\mathrm{E2}-U_\mathrm{E1})$, Integrierer $-\frac{1}{RC}\int u_\mathrm{E}\mathrm{d} t$, Differenzierer $-RC\,\mathrm{d} u_\mathrm{E}/\mathrm{d} t$, Logarithmierer $-U_T\ln(U_\mathrm{E}/RI_\mathrm{S})$, Exponential $-RI_\mathrm{S}\mathrm{e}^{U_\mathrm{E}/U_T}$, Transimpedanz $-R\,I_\mathrm{E}$, NIC $R_\mathrm{ein}=-R_2$.

</li>

<li>

Mitkopplung: Die Wirkung verstärkt die Ursache, Ausgang am Anschlag, Schwellen $\beta\,U_\mathrm{A,max}$ und $\beta\,U_\mathrm{A,min}$.

</li>

<li>

Grenzen: Übersteuerung, $U_\mathrm{off}/\beta$, $I_\mathrm{B}R_2$, CMRR, $G\,f_G=f_\mathrm{T}$.

</li>

</ul>
:::

**Ein Prinzip hinter allen Ergebnissen.** Der Ausgang eines gegengekoppelten OPV ist keine Rechnung mit $A$, sondern der Zustand, in dem die Schleife zur Ruhe kommt. $A$ muss dafür nur groß sein, sein genauer Wert zählt nicht.

| Ergebnis | Woher es kommt |
|---|---|
| __Rauschen__ (zufällige Störspannung), Signal-Rausch-Verhältnis | Einzelne Ladungen bewegen sich zufällig, Verstärken hebt Signal und Störung gleich (Stufe [1](rauschen.html#stufe-1)) |
| $U_\mathrm{A}=S\,R_\mathrm{C}\,U_\mathrm{D}$, Gleichtakt wirkungslos | Ein fester Summenstrom: Nur seine Aufteilung kann sich ändern (Stufe [2](der-differenzverstarker.html#stufe-2)) |
| __Komparator__ (Spannungsvergleicher) | Ohne Rückführung passt fast keine Eingangsspannung ins Fenster (Stufe [3](der-opv-ohne-ruckfuhrung.html#stufe-3)) |
| $U_\mathrm{D}=U_\mathrm{A}/A$, $G\approx1/\beta$ | Der Ausgang läuft, bis die Schleife zur Ruhe kommt (Stufe [4](gegenkopplung.html#stufe-4)) |
| $G=-R_2/R_1$, virtuelle Masse | Regel und Knotenregel am Minus-Eingang (Stufe [5](die-regel-und-die-virtuelle-masse.html#stufe-5)) |
| Addierer, Subtrahierer, Kette | Ströme addieren sich, Wirkungen überlagern sich (Stufe [6](mehrere-eingange-mehrere-stufen.html#stufe-6)) |
| Integrierer, Logarithmierer | Ein Bauteil macht den Strom, das andere die Spannung (Stufe [7](rechnen-mit-kondensator-und-diode.html#stufe-7)) |
| Strom-Spannungs-Wandler, negativer Widerstand | Der Ausgang liefert jeden Strom, den die Regel verlangt (Stufe [8](strom-als-signal.html#stufe-8)) |
| Schmitt-Trigger | Falsches Vorzeichen: Die Wirkung verstärkt ihre Ursache (Stufe [9](mitkopplung-und-der-schmitt-trigger.html#stufe-9)) |
| Grenzen der Regel | Alles, was $A\beta$ verkleinert oder $U_\mathrm{D}$ verschiebt (Stufe [10](wo-die-regeln-enden.html#stufe-10)) |

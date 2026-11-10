---
title: Das Wichtigste
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Ladung, Feld und Potenzial
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial
knoten: Kapitel 1: Ladung, Feld und Potenzial
order: 1111300
summary: Warum Spannung eine Differenz ist und was sie mit einer Ladung macht
tags: 
lang: de
---

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Ladung ist eine Eigenschaft der Elektronen und Protonen, der geladenen Bausteine der Atome. Gleichnamige Ladungen stoßen sich ab, ungleichnamige ziehen sich an, und die Summe aller Ladungen bleibt erhalten.

</li>

<li>

Jede Ladung erzeugt um sich ein Feld. Das Feld $\vec E$ bestimmt an jedem Ort die Kraft je Ladung: $\vec F=Q\,\vec E$.

</li>

<li>

Im ruhenden Feld hängt die Arbeit an einer Ladung nur von Start und Ziel ab, nicht vom Weg. Deshalb hat jeder Punkt ein Potenzial $\varphi$, und die Spannung $U_{12}=\varphi_1-\varphi_2$ ist die Energie je Ladung, die das Feld auf dem Weg von Punkt 1 nach Punkt 2 abgibt.

</li>

</ol>
:::

:::kern Das Wichtigste
<ul>

<li>

Größe = Zahlenwert $\cdot$ Einheit. $1\,\mathrm{V}=1\,\mathrm{J/C}$, $1\,\mathrm{C}=1\,\mathrm{A\,s}$, $1\,\mathrm{N}=1\,\mathrm{kg\,m/s^2}$.

</li>

<li>

Arbeit: $W=\int\vec F\cdot\mathrm{d}\vec s$, im Geraden $F\,s\cos\alpha$. Bewegungsenergie: $\frac12mv^2$.

</li>

<li>

Ladung: $Q=(N_\mathrm{p}-N_\mathrm{e})\,e$; sie bleibt erhalten.

</li>

<li>

Coulomb: $F=k\,|Q_\mathrm{A}Q_\mathrm{B}|/r^2$, gleichnamig stößt ab, ungleichnamig zieht an.

</li>

<li>

Feld: $\vec F=Q\vec E$, Richtung wie die Kraft auf positive Ladung; Punktladung $E=k|Q_0|/r^2$.

</li>

<li>

Feldlinien: von $+$ nach $-$, schneiden sich nie, senkrecht auf Leitern; im Metall $\vec E=0$.

</li>

<li>

Arbeit des Felds: $W_{12}=Q\int_{P_1}^{P_2}\vec E\cdot\mathrm{d}\vec s$; wirbelfrei: $\oint\vec E\cdot\mathrm{d}\vec s=0$.

</li>

<li>

Potenzial: $\varphi(P)=\int_P^{P_0}\vec E\cdot\mathrm{d}\vec s$; Punktladung $\varphi=kQ_0/r$; $\vec E$ zeigt zu fallendem $\varphi$.

</li>

<li>

Spannung: $U_{12}=\varphi_1-\varphi_2=\int_{P_1}^{P_2}\vec E\cdot\mathrm{d}\vec s=W_{12}/Q$, $U_{21}=-U_{12}$; homogen $E=U/d$.

</li>

<li>

Masse: $\varphi:=0$; ihre Lage ändert keine Spannung.

</li>

<li>

Ladung im Feld: $\frac12mv^2+Q\varphi$ konstant; aus der Ruhe $v=\sqrt{2|QU|/m}$.

</li>

<li>

Induktion: $u_\mathrm{ind}=-N\,\mathrm{d}\Phi/\mathrm{d} t$; dann ist das Feld nicht mehr wirbelfrei.

</li>

</ul>
:::

**Ausblick auf [Kapitel 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html).** In einem Draht treibt das Feld sehr viele Ladungen zugleich: Ladung fließt, ein Strom entsteht. [Kapitel 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html) zeigt, warum Spannung und Strom proportional sind und wie sie sich in einem Netz aufteilen.

**Ein Prinzip hinter allen Ergebnissen.** Kraft und Energie einer Ladung hängen von den anderen Ladungen ringsum und von ihr selbst ab. Teilt man durch die eigene Ladung, bleibt eine Eigenschaft des Orts: Aus der Kraft wird die Feldstärke, aus der Energie das Potenzial.

| Ergebnis | Woher es kommt |
|---|---|
| Feldstärke $\vec E=\vec F/Q$ | Kraft je Ladung: die Probeladung ist herausgeteilt (Stufe [4](die-feldstarke.html#stufe-4)) |
| Feldlinien, Abschirmung | Bild von $\vec E$; freie Elektronen stellen sich im Metall so ein, dass keine Kraft bleibt (Stufe [5](feldlinien-und-leiter.html#stufe-5)) |
| $W_{12}=Q\int\vec E\cdot\mathrm{d}\vec s$, wegunabhängig | Arbeit ist Kraft mal Weg; Coulomb-Kräfte zeigen radial, nur der Abstand zählt (Stufe [6](arbeit-im-feld.html#stufe-6)) |
| Potenzial $\varphi$ | Arbeit je Ladung bis zum Bezugspunkt (Stufe [7](das-potenzial.html#stufe-7)) |
| Spannung, Masse | Arbeit je Ladung zwischen zwei Punkten; der Nullpunkt ist frei wählbar (Stufe [8](spannung-und-masse.html#stufe-8)) |
| Geschwindigkeit einer Ladung | Die Energie $QU$ wird zu Bewegungsenergie (Stufe [9](was-die-spannung-mit-einer-ladung-macht.html#stufe-9)) |
| Induktion | Grenze des Prinzips: Ändert sich ein Magnetfeld, hängt die Arbeit vom Weg ab (Stufe [10](grenze-des-bildes-magnetismus-und-induktion.html#stufe-10)) |

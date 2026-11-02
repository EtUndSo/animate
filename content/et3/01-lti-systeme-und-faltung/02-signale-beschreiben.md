---
title: Stufe 1: Signale beschreiben
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / LTI-Systeme und Faltung
order: 3210200
summary: Bevor man Systeme untersucht, braucht man eine Sprache für Signale: einige Grundformen und zwei Operationen auf der Zeitachse, Verschieben und Dehnen.
tags: Signal, normiert, Periodendauer, Frequenz
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Bevor man Systeme untersucht, braucht man eine Sprache für Signale: einige Grundformen und zwei Operationen auf der Zeitachse, Verschieben und Dehnen.
:::

Ein __Signal__ ist der Verlauf einer physikalischen Größe über der Zeit, geschrieben als Funktion $s(t)$. In der Systemtheorie rechnet man meist __normiert__: Zeiten in Vielfachen von 1 s, Spannungen in Vielfachen von 1 V. Dann werden Größengleichungen zu Zahlenwertgleichungen, und $\mathrm{e}^{-t}$ ist ohne Einheitenproblem hinschreibbar.

**Elementarsignale.** Einige Signale lassen sich durch einen einfachen Ausdruck beschreiben und kommen immer wieder vor (Abb. [1](#abb-1)):

$$\begin{gathered} \sin(2\pi t),\qquad \mathrm{e}^{-\pi t^2}\ \text{(Gauß)},\qquad \varepsilon(t)=\begin{cases}0&t<0\\1&t\ge0\end{cases},\\ \operatorname{rect}(t)=\begin{cases}1&|t|\le\frac12\\0&|t|>\frac12\end{cases},\qquad \Lambda(t)=\begin{cases}1-|t|&|t|\le1\\0&|t|>1\end{cases}. \end{gathered}$$

Sprung $\varepsilon(t)$ und Rechteck $\operatorname{rect}(t)$ springen. Welcher Wert genau an der Sprungstelle gilt, ist Vereinbarungssache. Oft wählt man dort $\tfrac12$: Dann ergeben aneinandergesetzte Rechtecke überall genau 1.

:::abbildung et3/k1elementar 1
Elementarsignale. Unten rechts ein verschobenes und gedehntes Rechteck: Mitte bei $t_0=2$, Breite $T=2$, Höhe $a=0{,}8$.
:::

**Verschieben und Dehnen.** Aus einem Signal entstehen neue, wenn man die Zeitachse umrechnet:

<ul>

<li>

⁠**Verschieben:** $t\to t-t_0$. Für $t_0>0$ wird das Signal um $t_0$ *verzögert*, also nach rechts geschoben.

</li>

<li>

⁠**Dehnen:** $t\to t/T$. Für $|T|>1$ wird das Signal breiter, für $0<|T|<1$ schmaler, für $T<0$ zusätzlich gespiegelt.

</li>

</ul>

Beides zusammen, dazu eine Amplitude $a$, ergibt zum Beispiel den Rechteckimpuls

<span class="anker" id="gl-1-1"></span>
$$s(t)=a\operatorname{rect}\Bigl(\frac{t-t_0}{T}\Bigr)=\begin{cases}a & |t-t_0|\le |T|/2\\ 0 & \text{sonst}\end{cases} \tag{1.1}$$

mit der Mitte $t_0$, der Dauer $|T|$ und der Höhe $a$. Man prüft es, indem man das Argument $(t-t_0)/T$ in die Definition von $\operatorname{rect}$ einsetzt. Ebenso ist $\sin(2\pi t/T)=\sin(2\pi Ft)$ der gedehnte Sinus mit der __Periodendauer__ $T$ und der __Frequenz__ $F=1/T$.

:::frage Warum verschiebt $t-t_0$ das Signal nach rechts, obwohl man etwas abzieht?
Das neue Signal zeigt zur Zeit $t$ den Wert, den das alte zur Zeit $t-t_0$ hatte, also *früher*. Alles, was das alte Signal tat, tut das neue $t_0$ später. Am einfachsten prüft man es an einer markanten Stelle: Die Kante von $\varepsilon(t-t_0)$ liegt dort, wo das Argument null wird, bei $t=t_0$.
:::

**Die komplexe Exponentialfunktion.** Für die Systemtheorie am wichtigsten ist

$$\mathrm{e}^{\mathrm{j}2\pi Ft}=\cos(2\pi Ft)+\mathrm{j}\sin(2\pi Ft).$$

Aus einem konjugiert komplexen Paar entstehen nach Euler die reellen Schwingungen:

$$\cos(2\pi Ft)=\frac{\mathrm{e}^{\mathrm{j}2\pi Ft}+\mathrm{e}^{-\mathrm{j}2\pi Ft}}{2},\qquad \sin(2\pi Ft)=\frac{\mathrm{e}^{\mathrm{j}2\pi Ft}-\mathrm{e}^{-\mathrm{j}2\pi Ft}}{2\mathrm{j}}.$$

Eine Verzögerung um $t_0$ erscheint bei einer Schwingung als Phasenverschiebung:

<span class="anker" id="gl-1-2"></span>
$$\cos\bigl(2\pi F(t-t_0)\bigr)=\cos(2\pi Ft+\varphi)=\operatorname{Re}\bigl\{\mathrm{e}^{\mathrm{j}2\pi Ft}\,\mathrm{e}^{\mathrm{j}\varphi}\bigr\},\qquad\varphi=-2\pi Ft_0. \tag{1.2}$$

⁠**Kurz gesagt:** Bei einer Schwingung ist Verzögern dasselbe wie Phasedrehen, und bei $\mathrm{e}^{\mathrm{j}2\pi Ft}$ ist es sogar dasselbe wie Multiplizieren mit der Zahl $\mathrm{e}^{\mathrm{j}\varphi}$.

:::aufgabe Aufgabe 1 ★ Verschieben, dehnen, Phase
<span class="anker" id="aufg-1"></span>

<ol class="al">

<li>

Wo beginnt und endet $s(t)=2\operatorname{rect}\bigl(\frac{t-3}{4}\bigr)$, und wie hoch ist der Impuls?

</li>

<li>

Schreibe einen Rechteckimpuls, der von $t=1$ s bis $t=4$ s die Höhe 0,5 V hat.

</li>

<li>

Skizziere $s(-t)$ für $s(t)=\varepsilon(t-1)$. Wo liegt die Kante?

</li>

<li>

Ein Kosinus mit $F=50$ Hz wird um $t_0=5$ ms verzögert. Welche Phase $\varphi$ hat er danach?

</li>

</ol>

:::loesung
(a) Mitte $t_0=3$, Dauer $T=4$: von $t=1$ bis $t=5$, Höhe 2.

(b) Mitte 2,5 s, Dauer 3 s: $s(t)=0{,}5\operatorname{rect}\bigl(\frac{t-2{,}5}{3}\bigr)$.

(c) $s(-t)=\varepsilon(-t-1)$. Die Kante liegt dort, wo das Argument null wird: $-t-1=0$, also $t=-1$. Der Wert ist 1, wo das Argument $\ge0$ ist, also für $t\le-1$. Ein gespiegelter Sprung: 1 links von $-1$, 0 rechts davon.

(d) $\varphi=-2\pi Ft_0=-2\pi\cdot50\,\mathrm{Hz}\cdot5\,\mathrm{ms}=-\pi/2=-90^\circ$. Eine Viertelperiode Verzögerung ist eine Viertelumdrehung.
:::
:::

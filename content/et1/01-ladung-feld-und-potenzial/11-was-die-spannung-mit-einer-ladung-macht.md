---
title: Stufe 9: Was die Spannung mit einer Ladung macht
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Ladung, Feld und Potenzial
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial
knoten: Kapitel 1: Ladung, Feld und Potenzial
order: 1111100
summary: Diese Stufe führt Feld, Potenzial und Spannung an einem einzelnen Elektron zusammen: Welche Kraft wirkt, welche Energie gewinnt es, wie schnell wird es?
tags: Elektronenvolt
lang: de
---

<span class="anker" id="stufe-9"></span>

:::zweck
Diese Stufe führt Feld, Potenzial und Spannung an einem einzelnen Elektron zusammen: Welche Kraft wirkt, welche Energie gewinnt es, wie schnell wird es?
:::

**Die Idee.** Ein Elektron löst sich von Platte B und startet aus der Ruhe. Das Feld zeigt von A nach B. Wegen $\vec F=Q\vec E$ und $Q=-e$ wirkt die Kraft entgegen dem Feld, zu Platte A hin. Sie ist überall gleich groß, die Beschleunigung ist also konstant, und [(1.4)](groen-kraft-und-arbeit.html#gl-1-4) gilt. Unterwegs wandelt sich potenzielle Energie in Bewegungsenergie um. Das Elektron läuft zum hohen Potenzial, seine Energie $Q\varphi$ fällt trotzdem, weil $Q$ negativ ist.

:::satz Satz 9.1 (Ladung im Feld)
<span class="anker" id="satz-9-1"></span>

Im elektrostatischen Feld bleibt die Summe aus Bewegungsenergie und potenzieller Energie konstant:

<span class="anker" id="gl-9-1"></span>
$$\tfrac12m\,v^2+Q\,\varphi=\text{konstant}. \tag{9.1}$$

Eine Ladung, die aus der Ruhe die Spannung $U$ durchläuft, erreicht im homogenen Feld der Länge $d$

<span class="anker" id="gl-9-2"></span>
$$v=\sqrt{\frac{2\,|Q\,U|}{m}},\qquad a=\frac{|Q|\,E}{m},\qquad t=\frac{2\,d}{v}. \tag{9.2}$$
:::

:::herleitung Energiesatz und Flugzeit
Die Arbeit des Felds wird vollständig zu Bewegungsenergie: $\frac12mv_2^2-\frac12mv_1^2=W_{12}=Q(\varphi_1-\varphi_2)$. Umstellen ergibt [(9.1)](#gl-9-1). Mit $v_1=0$ folgt $|Q\,U|=\frac12m\,v^2$. Bei konstanter Beschleunigung ist die mittlere Geschwindigkeit $v/2$, also $t=d/(v/2)$.
:::

⁠**So liest man das:** $m$ ist die Masse in kg, $\varphi$ das Potenzial am Ort. In $v$ kommt der Weg nicht vor, allein die Spannung bestimmt die Energie. **Gültigkeit und Vernachlässigungen:** Die Gleichungen gelten im Vakuum. In Luft stößt ein Elektron schon nach Bruchteilen eines Mikrometers mit einem Molekül zusammen. Die Gewichtskraft $m_\mathrm{e}g=8{,}9\cdot10^{-30}$ N entfällt, sie ist $5{,}4\cdot10^{13}$-mal kleiner als die Feldkraft. Außerdem muss $v\ll c$ gelten. Hier ist $v$ nur 0,6 % der Lichtgeschwindigkeit $c$, die Korrektur der Bewegungsenergie beträgt 0,003 %.

:::abbildung et1/k1elektron 11
Links: Das Elektron startet an Platte B und läuft gegen das Feld zu Platte A. Rechts: Von $x=3$ mm nach $x=0$ wächst die Bewegungsenergie auf $1{,}44\cdot10^{-18}$ J, die potenzielle Energie fällt um denselben Betrag, Bezugspunkt B. Die Summe bleibt null.
:::

::::beispiel
Für das Elektron im Plattenpaar ist

$$\begin{aligned} F&=e\,E=4{,}81\cdot10^{-16}\,\mathrm{N},\qquad a=\frac{F}{m_\mathrm{e}}=5{,}28\cdot10^{14}\,\mathrm{m/s^2},\qquad W=e\,U=1{,}44\cdot10^{-18}\,\mathrm{J},\\ v&=\sqrt{\frac{2\cdot1{,}44\cdot10^{-18}\,\mathrm{J}}{9{,}109\cdot10^{-31}\,\mathrm{kg}}}=1{,}78\cdot10^{6}\,\mathrm{m/s},\qquad t=\frac{2\cdot3\,\mathrm{mm}}{v}=3{,}37\,\mathrm{ns}. \end{aligned}$$

Ein Proton läuft von A nach B. Es gewinnt dieselbe Energie, ist aber 1836-mal schwerer: $v=4{,}15\cdot10^4$ m/s, $\sqrt{1836}=42{,}9$-mal langsamer, Flugzeit 144 ns.
::::

⁠**Kurz gesagt:** Durchläuft eine Ladung im Vakuum eine Spannung, ändert sich ihre Bewegungsenergie um Ladung mal Spannung, unabhängig von Weg und Abstand.

⁠**Grenzfälle:** Für $U\to0$ geht $v\to0$. Doppelter Plattenabstand bei gleicher Spannung halbiert $E$ und $a$, ändert $v$ aber nicht: Das Elektron beschleunigt schwächer, dafür länger, und braucht 6,74 ns. Vierfache Spannung ergibt doppelte Geschwindigkeit.

:::frage Läuft das Elektron wirklich gegen das Feld? Ein Feld treibt Ladungen doch in seine Richtung.
Es treibt *positive* Ladungen in seine Richtung, so ist die Richtung von $\vec E$ festgelegt. Jede Ladung läuft von selbst dorthin, wo ihre potenzielle Energie $Q\varphi$ kleiner wird. Beim Elektron ist das das höhere Potenzial.
:::

:::zusatz Das Elektronenvolt
Die Energie, die eine Elementarladung beim Durchlaufen von 1 V gewinnt, heißt __Elektronenvolt__: $1\,\mathrm{eV}=1{,}602\cdot10^{-19}$ J. Das Elektron im Beispiel gewinnt 9 eV.
:::

:::aufgabe Aufgabe 10 ★★★ Elektron gegen das Feld
<span class="anker" id="aufg-10"></span>

Ein Elektron verlässt Platte A des Rechenmodells mit $v_0=1{,}0\cdot10^6$ m/s in Richtung Platte B.

<ol class="al">

<li>

Erreicht es Platte B? Vergleiche seine Bewegungsenergie mit der nötigen Energie.

</li>

<li>

An welchem Ort $x$ kehrt es um? Rechne einmal mit dem Energiesatz und einmal mit [(1.4)](groen-kraft-und-arbeit.html#gl-1-4).

</li>

<li>

Wann ist es wieder an Platte A, und mit welcher Geschwindigkeit?

</li>

<li>

Welche Startgeschwindigkeit bräuchte es, um B gerade noch zu erreichen?

</li>

</ol>

:::loesung
(a) $W_\mathrm{kin}=\frac12m_\mathrm{e}v_0^2=4{,}55\cdot10^{-19}$ J. Bis B wären $e\cdot9\,\mathrm{V}=1{,}44\cdot10^{-18}$ J nötig. Es erreicht B nicht. (b) Energiesatz: Es kommt so weit, bis $\Delta\varphi=W_\mathrm{kin}/e=2{,}84$ V aufgezehrt sind. Bei 3 V/mm ist $x=0{,}948$ mm. Mit [(1.4)](groen-kraft-und-arbeit.html#gl-1-4): Bremsung $a=5{,}28\cdot10^{14}\,\mathrm{m/s^2}$, Umkehr bei $t=v_0/a$, also $x=v_0^2/(2a)=0{,}948$ mm.

(c) Hin und zurück: $t=2v_0/a=3{,}79$ ns. Das Potenzial ist wieder dasselbe, also nach [(9.1)](#gl-9-1) $v=v_0=1{,}0\cdot10^6$ m/s, in Gegenrichtung. (d) Genau die Energie aus dem Beispiel: $v_0=1{,}78\cdot10^6$ m/s.
:::
:::

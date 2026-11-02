---
title: Stufe 3: Der Fehler beim Strommessen
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Strom und Spannung messen
order: 1140400
summary: Das Amperemeter muss in den Stromkreis.
tags: relative Fehler
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Das Amperemeter muss in den Stromkreis. Diese Stufe berechnet, wie stark sein Innenwiderstand genau den Strom senkt, den es messen soll.
:::

**Die Idee.** Zum Messen trennt man den Kreis auf und setzt das Instrument ein (Abb. [4](#abb-4)). Die Masche enthält nun $R$ und $R_\mathrm i$. Die Quelle hält $U$ fest und treibt durch den größeren Gesamtwiderstand weniger Strom. Die Anzeige stimmt: Sie zeigt den Strom, der jetzt fließt. Falsch ist nur der Schluss, derselbe Strom fließe auch ohne Gerät.

:::abbildung et1/k4strom 4
Das Rechenmodell ohne und mit Amperemeter. Am Innenwiderstand fallen 49,7 mV ab, die dem Widerstand fehlen. Der Strom sinkt um 0,55 %.
:::

:::satz Satz 3.1 (Fehler des Amperemeters)
<span class="anker" id="satz-3-1"></span>

Ohne Gerät fließt $I_R$, mit Gerät $I_R'$:

<span class="anker" id="gl-3-1"></span>
$$I_R=\frac UR,\qquad I_R'=\frac{U}{R+R_\mathrm i}<I_R,\qquad \frac{I_R}{I_R'}=\frac{R+R_\mathrm i}{R}=1+\frac{R_\mathrm i}{R}. \tag{3.1}$$

Der __relative Fehler__ ist $f=(I_R'-I_R)/I_R=-R_\mathrm i/(R+R_\mathrm i)$. Für $R_\mathrm i\ll R$ gilt $f\approx-R_\mathrm i/R$.
:::

⁠**So liest man das:** $U$ ist die Quellspannung in V, $R$ der Widerstand der Schaltung, $R_\mathrm i$ der des Geräts. Der gestrichene Strom ist der Strom mit Gerät. Allgemein gilt $f=(\text{Anzeige}-\text{wahrer Wert})/\text{wahrer Wert}$, ein negatives $f$ heißt: Die Anzeige ist zu klein. **Gültigkeit:** Die Schaltung ist eine ideale Quelle mit einem Widerstand. Für einen kleinen Fehler braucht es $R_\mathrm i\ll R$, ideal $R_\mathrm i=0$.

:::herleitung Fehler des Amperemeters
Die Maschenregel lautet $U=I_R'R+I_R'R_\mathrm i$, also $I_R'=U/(R+R_\mathrm i)$. Damit ist $f=I_R'/I_R-1=R/(R+R_\mathrm i)-1=-R_\mathrm i/(R+R_\mathrm i)$.
:::

**Beispiel.** $I_R=5$ mA, $I_R'=9\,\mathrm{V}/1810\,\Omega=4{,}972$ mA, also $f=-0{,}55\,\%$. Mit 1 $\Omega$ wie beim Digitalmultimeter wären es 4,997 mA und $f=-0{,}056\,\%$: Fehler vernachlässigbar. An einem kleinen Widerstand sieht es anders aus: 0,9 V an 90 $\Omega$ ergeben 10 mA, mit dem Instrument nur 9 mA, also $f=-10\,\%$. Nicht das Gerät allein entscheidet, sondern das Verhältnis $R_\mathrm i/R$.

⁠**Grenzfälle:** $R_\mathrm i\to0$ ergibt $f\to0$. $R\to0$ ergibt $I_R'\to U/R_\mathrm i$ und $f\to-100\,\%$: Nur noch das Instrument begrenzt den Strom. Das ist Aufgabe [1](das-messgerat-ist-ein-bauteil.html#aufg-1)(a).

:::frage Ist der Strom hinter dem Amperemeter kleiner als davor?
Nein. Im Instrument geht keine Ladung verloren, nur Energie. Der Strom ist im ganzen Kreis gleich und sinkt überall zugleich, weil der Gesamtwiderstand gestiegen ist.
:::

:::aufgabe Aufgabe 3 ★★ Welcher Bereich?
<span class="anker" id="aufg-3"></span>

(a) Ab welchem $R$ bleibt der Fehler des 10-$\Omega$-Amperemeters unter 1 %? (b) An 9 V liegen 90 k$\Omega$. Vergleiche den 10-mA-Bereich mit dem 250-µ A-Bereich: den Fehler durch $R_\mathrm i$ und den Anzeigefehler (1 % des Bereichsendwerts). Welcher Bereich misst besser?

:::loesung
(a) $R_\mathrm i/(R+R_\mathrm i)\le0{,}01$ ergibt $R\ge99\,R_\mathrm i=990\,\Omega$.

(b) Der wahre Strom ist $9\,\mathrm{V}/90\,\mathrm{k\Omega}=100$ µ A. Im 10-mA-Bereich ist $R_\mathrm i=10\,\Omega$, $f=-0{,}011\,\%$, aber der Anzeigefehler beträgt $\pm100$ µ A, so viel wie der Strom selbst. Im 250-µ A-Bereich ist $R_\mathrm i=100\,\mathrm{mV}/250\,\mu\text{A}=400\,\Omega$, $f=-0{,}44\,\%$, der Anzeigefehler beträgt $\pm2{,}5$ µ A, also 2,5 %. Der kleine Bereich greift stärker ein, misst aber viel besser. Die $-0{,}44\,\%$ lassen sich zudem herausrechnen.
:::
:::

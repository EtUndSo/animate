---
title: Stufe 6: Der Transistor als Schalter
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Der Bipolartransistor
order: 1200800
summary: Ein Schalter soll ganz aus oder ganz ein sein.
tags: Inverter, Logikpegel, Leistungshyperbel
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Ein Schalter soll ganz aus oder ganz ein sein. Diese Stufe zeigt, warum er dafür die Enden der Arbeitsgeraden benutzt, baut daraus den Inverter und nennt die Grenzen des Bauteils.
:::

**Die Idee.** Der Transistor setzt die Leistung $P=U_\mathrm{CE}I_\mathrm{C}+U_\mathrm{BE}I_\mathrm{B}$ in Wärme um, praktisch nur den ersten Teil. Im Sperrbereich ist $I_\mathrm{C}=0$, in der Sättigung ist $U_\mathrm{CE}$ klein. In beiden Punkten bleibt das Produkt gering. In der Mitte der Arbeitsgeraden ist es am größten. Ein Schalter springt deshalb zwischen Z und S. Der Abstand der beiden Ausgangspegel ist so am größten, und es gibt keine Mechanik: Der Transistor schaltet sehr schnell und ohne Verschleiß. Ein Verstärker arbeitet dagegen im aktiven Bereich. Dort ist die Kennlinie näherungsweise linear, und die höhere Verlustleistung zählt weniger als ein unverzerrtes Signal.

Die kleinste Logikschaltung ist der __Inverter__: dieselbe Schaltung wie in Abb. [6](der-arbeitspunkt.html#abb-6), mit $U_\mathrm{aus}=U_\mathrm{CE}$ als Ausgang. Hohe Eingangsspannung gibt niedrige Ausgangsspannung und umgekehrt. Als __Logikpegel__ gelten eine niedrige Spannung als 0 und eine hohe als 1.

:::satz Satz 6.1 (Kennlinie des Inverters)
<span class="anker" id="satz-6-1"></span>

Mit dem linearen Modell gilt

<span class="anker" id="gl-6-1"></span>
$$U_\mathrm{aus}= \begin{cases} U_\mathrm{CC} & U_\mathrm{ein}<U_\mathrm{BE},\\[2pt] U_\mathrm{CC}-B\,R_\mathrm{C}\dfrac{U_\mathrm{ein}-U_\mathrm{BE}}{R_\mathrm{B}} & U_\mathrm{BE}\le U_\mathrm{ein}\le U_\mathrm{ein,sat},\\[6pt] U_\mathrm{CE,sat} & U_\mathrm{ein}>U_\mathrm{ein,sat}, \end{cases} \tag{6.1}$$

<span class="anker" id="gl-6-2"></span>
$$U_\mathrm{ein,sat}=\frac{(U_\mathrm{CC}-U_\mathrm{CE,sat})\,R_\mathrm{B}}{B\,R_\mathrm{C}}+U_\mathrm{BE}. \tag{6.2}$$
:::

⁠**So liest man das:** Der mittlere Ast ist eine Gerade mit der Steigung $-B\,R_\mathrm{C}/R_\mathrm{B}$. $U_\mathrm{ein,sat}$ ist die Eingangsspannung, bei der der Transistor die Sättigung erreicht. Unter $U_\mathrm{BE}$ gilt der Eingang als 0, über $U_\mathrm{ein,sat}$ als 1. Dazwischen ist das Signal nicht eindeutig. Deshalb wählt man $R_\mathrm{B}$ klein genug, dass $U_\mathrm{ein,sat}$ nah an $U_\mathrm{BE}$ rückt. Die Herleitung ist [(5.2)](der-arbeitspunkt.html#gl-5-2) mit [(5.1)](der-arbeitspunkt.html#gl-5-1), nach $U_\mathrm{ein}$ aufgelöst bei $U_\mathrm{CE}=U_\mathrm{CE,sat}$. **Gültigkeit:** für langsame Signale. Sehr schnelle Wechsel begrenzt die Ladung in der Basis.

:::abbildung et1/k10schalter 7
Links die Inverterkennlinie mit $R_\mathrm{B}=20$ k$\Omega$, Knicke bei 0,6 V und 0,99 V. Mitte ein Rechtecksignal zwischen 0 und 5 V am Eingang (grau) und der invertierte Ausgang zwischen 12 V und 0,2 V (blau). Rechts die zulässigen Arbeitspunkte: unter der Leistungshyperbel, $I_\mathrm{C,max}$ und $U_\mathrm{CE,max}$. Der Arbeitspunkt A liegt mit 12 mW tief im erlaubten Gebiet.
:::

::::beispiel
Mit $R_\mathrm{B}=20$ k$\Omega$ ist die Steigung $-30$ und $U_\mathrm{ein,sat}=0{,}99$ V. Ein Logikeingang mit 5 V ergibt $I_\mathrm{B}=220$ µ A und $B\,I_\mathrm{B}=44$ mA, weit über den 3,93 mA, die $R_\mathrm{C}$ zulässt. Der Transistor ist also elffach übersteuert und bleibt auch bei einem schlechten Exemplar sicher eingeschaltet. In ihm entstehen $0{,}2\,\mathrm{V}\cdot3{,}93\,\mathrm{mA}+0{,}6\,\mathrm{V}\cdot0{,}22\,\mathrm{mA}=0{,}92$ mW, während er in $R_\mathrm{C}$ eine Leistung von 46 mW schaltet. Im Punkt A wären es 12 mW im Transistor.
::::

⁠**Grenzfall:** Für $B\,R_\mathrm{C}/R_\mathrm{B}\to\infty$ wird die Kennlinie ein senkrechter Sprung bei $U_\mathrm{BE}$.

**Betriebsgrenzen.** Drei Werte begrenzen die erlaubten Arbeitspunkte (Abb. [7](#abb-7), rechts). Über $U_\mathrm{CE,max}$ schlägt die CB-Grenze durch. Über $I_\mathrm{C,max}$ überlasten Basis und Anschlussdrähte. Über der __Leistungshyperbel__ $I_\mathrm{C}=P_\mathrm{max}/U_\mathrm{CE}$ wird das Bauteil zu heiß. Außerhalb sinkt die Lebensdauer rapide, oder das Bauteil fällt sofort aus. Für T liegt die Hyperbel bei 40 V auf 10 mA, bei 4 V auf 100 mA.

:::aufgabe Aufgabe 7 ★★ Inverter
<span class="anker" id="aufg-7"></span>

Ein Inverter mit T läuft an $U_\mathrm{CC}=5$ V mit $R_\mathrm{C}=1$ k$\Omega$ und $R_\mathrm{B}=10$ k$\Omega$. (a) Bestimme Steigung und $U_\mathrm{ein,sat}$. (b) Am Eingang liegen 3,3 V. Bestimme $I_\mathrm{B}$, $I_\mathrm{C}$ und die Leistung im Transistor. Vergleiche sie mit dem Höchstwert auf der Arbeitsgeraden. (c) Reicht ein Eingang von 3,3 V auch bei $B=50$?

:::loesung
(a) Steigung $-200\cdot1\,\text{k}\Omega/10\,\text{k}\Omega=-20$. $U_\mathrm{ein,sat}=4{,}8\,\mathrm{V}/20+0{,}6\,\mathrm{V}=0{,}84$ V.

(b) $I_\mathrm{B}=2{,}7\,\mathrm{V}/10\,\text{k}\Omega=270$ µ A, $B\,I_\mathrm{B}=54$ mA, weit über $I_\mathrm{C}=4{,}8\,\mathrm{V}/1\,\text{k}\Omega=4{,}8$ mA, also Sättigung. $P=0{,}2\,\mathrm{V}\cdot4{,}8\,\mathrm{mA}+0{,}6\,\mathrm{V}\cdot0{,}27\,\mathrm{mA}=1{,}12$ mW. Auf der Arbeitsgeraden ist $U_\mathrm{CE}I_\mathrm{C}=U_\mathrm{CE}(U_\mathrm{CC}-U_\mathrm{CE})/R_\mathrm{C}$. Das Maximum liegt bei $U_\mathrm{CC}/2$ mit $U_\mathrm{CC}^2/(4R_\mathrm{C})=6{,}25$ mW.

(c) $U_\mathrm{ein,sat}=4{,}8\,\mathrm{V}/5+0{,}6\,\mathrm{V}=1{,}56$ V $<3{,}3$ V: Ja.
:::
:::

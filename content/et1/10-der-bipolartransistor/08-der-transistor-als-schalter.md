---
title: Stufe 6: Der Transistor als Schalter
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Der Bipolartransistor
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor
knoten: Kapitel 10: Der Bipolartransistor
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

::::formelsammlung
**Leistung im Transistor**

$$P=U_\mathrm{CE}I_\mathrm{C}+U_\mathrm{BE}I_\mathrm{B}$$

Wird in Wärme umgesetzt, praktisch nur der erste Teil. Klein im Sperrbereich ($I_\mathrm{C}=0$) und in der Sättigung ($U_\mathrm{CE}$ klein), am größten in der Mitte der Arbeitsgeraden.

**Leistung auf der Arbeitsgeraden**

$$U_\mathrm{CE}I_\mathrm{C}=U_\mathrm{CE}(U_\mathrm{CC}-U_\mathrm{CE})/R_\mathrm{C}$$

Das Maximum liegt bei $U_\mathrm{CC}/2$ und beträgt $U_\mathrm{CC}^2/(4R_\mathrm{C})$.

**Kennlinie des Inverters**

$$U_\mathrm{aus}= \begin{cases} U_\mathrm{CC} & U_\mathrm{ein}<U_\mathrm{BE},\\[2pt] U_\mathrm{CC}-B\,R_\mathrm{C}\dfrac{U_\mathrm{ein}-U_\mathrm{BE}}{R_\mathrm{B}} & U_\mathrm{BE}\le U_\mathrm{ein}\le U_\mathrm{ein,sat},\\[6pt] U_\mathrm{CE,sat} & U_\mathrm{ein}>U_\mathrm{ein,sat}, \end{cases}$$

Lineares Modell, Ausgang $U_\mathrm{aus}=U_\mathrm{CE}$; der mittlere Ast hat die Steigung $-B\,R_\mathrm{C}/R_\mathrm{B}$. Logikpegel: Unter $U_\mathrm{BE}$ gilt der Eingang als 0, über $U_\mathrm{ein,sat}$ als 1. Gilt für langsame Signale.

**Eingangsspannung an der Sättigungsgrenze**

$$U_\mathrm{ein,sat}=\frac{(U_\mathrm{CC}-U_\mathrm{CE,sat})\,R_\mathrm{B}}{B\,R_\mathrm{C}}+U_\mathrm{BE}$$

Eingangsspannung, bei der der Transistor die Sättigung erreicht. Man wählt $R_\mathrm{B}$ klein genug, dass sie nahe an $U_\mathrm{BE}$ rückt.

**Leistungshyperbel**

$$I_\mathrm{C}=P_\mathrm{max}/U_\mathrm{CE}$$

Arbeitspunkte darüber machen das Bauteil zu heiß. Weitere Grenzen: $U_\mathrm{CE,max}$ (die CB-Grenze schlägt durch) und $I_\mathrm{C,max}$.
::::

::::lernkarten
:::karte formel Leistung im Transistor
Welche Leistung setzt ein Transistor in Wärme um, und welcher Teil davon überwiegt?
---
$P=U_\mathrm{CE}I_\mathrm{C}+U_\mathrm{BE}I_\mathrm{B}$, praktisch nur der erste Teil, weil der Basisstrom viel kleiner ist als der Kollektorstrom.
--- falsch
$P=U_\mathrm{CC}I_\mathrm{C}$, die ganze Leistung der Versorgung, weil der Kollektorwiderstand selbst keine Leistung aufnimmt.
--- falsch
$P=U_\mathrm{BE}I_\mathrm{B}$, nur die Leistung am Eingang, weil der Kollektorstrom ohne Spannungsabfall durch den Transistor fließt.
--- falsch
$P=U_\mathrm{CE}I_\mathrm{B}+U_\mathrm{BE}I_\mathrm{C}$, praktisch nur der zweite Teil, weil $U_\mathrm{BE}$ größer als $U_\mathrm{CE}$ ist.
:::
:::karte zusammenhang Schalter an den Enden der Arbeitsgeraden
Warum springt ein Transistor als Schalter zwischen Sperrbereich und Sättigung, statt in der Mitte der Arbeitsgeraden zu arbeiten?
---
Im Sperrbereich ist $I_\mathrm{C}=0$, in der Sättigung ist $U_\mathrm{CE}$ klein, das Produkt $U_\mathrm{CE}I_\mathrm{C}$ bleibt an beiden Enden gering; in der Mitte ist es am größten. Zugleich ist der Abstand der beiden Ausgangspegel so am größten.
--- falsch
In der Mitte der Arbeitsgeraden ist der Transistor gesperrt, an den Enden leitet er. Ein Schalter muss leiten, deshalb nutzt er nur die beiden Enden, an denen ein Strom fließt und die übertragene Leistung am größten ist.
--- falsch
An den Enden ist die Kennlinie am steilsten, deshalb genügt dort die kleinste Änderung am Eingang. In der Mitte bräuchte der Schalter viel größere Eingangsspannungen, um umzuschalten.
--- falsch
In der Mitte der Arbeitsgeraden ist die Verlustleistung null, an den Enden am größten. Ein Schalter nutzt die Enden trotzdem, weil dort die Ausgangspegel am weitesten auseinanderliegen.
:::
:::karte zusammenhang Verstärker im aktiven Bereich
Warum arbeitet ein Verstärker trotz höherer Verlustleistung im aktiven Bereich und nicht an den Enden der Arbeitsgeraden?
---
Dort ist die Kennlinie näherungsweise linear, und ein unverzerrtes Signal zählt mehr als die höhere Verlustleistung.
--- falsch
Dort ist die Verlustleistung am kleinsten, und die Kennlinie springt sauber zwischen zwei festen Pegeln hin und her.
--- falsch
Dort ist der Transistor gesperrt, und das Signal läuft ohne Verluste über den Kollektorwiderstand.
--- falsch
Dort ist die Basis mit Elektronen gesättigt, deshalb folgt der Ausgang dem Eingang ohne Verzögerung.
:::
:::karte begriff Inverter
Wie ist ein Inverter mit einem Transistor aufgebaut, und was macht er mit dem Eingangssignal?
---
Die Schaltung mit Basis- und Kollektorwiderstand und dem Emitter an Masse, mit $U_\mathrm{aus}=U_\mathrm{CE}$ als Ausgang. Hohe Eingangsspannung gibt niedrige Ausgangsspannung und umgekehrt; er ist die kleinste Logikschaltung.
--- falsch
Die Schaltung mit Basis- und Kollektorwiderstand, mit $U_\mathrm{aus}=U_\mathrm{BE}$ als Ausgang. Er gibt die Eingangsspannung um 0,6 V verkleinert, aber mit demselben Vorzeichen und Verlauf, an die Last weiter, ohne sie umzukehren.
--- falsch
Die Schaltung mit Emitterwiderstand, mit der Spannung an $R_\mathrm{E}$ als Ausgang. Hohe Eingangsspannung gibt hohe Ausgangsspannung; er verstärkt Logiksignale auf den vollen Pegel.
--- falsch
Die Schaltung mit Basis- und Kollektorwiderstand, mit $U_\mathrm{aus}=U_\mathrm{CE}$ als Ausgang. Er kehrt das Vorzeichen der Eingangsspannung um: Aus $+5$ V am Eingang werden $-5$ V am Ausgang und umgekehrt.
:::
:::karte begriff Logikpegel
Was versteht man unter Logikpegeln, und welche Eingangsspannungen gelten beim Inverter als 0 und als 1?
---
Die Zuordnung von Spannungen zu logischen Werten: Eine niedrige Spannung gilt als 0, eine hohe als 1. Beim Inverter gilt ein Eingang unter $U_\mathrm{BE}$ als 0, über $U_\mathrm{ein,sat}$ als 1.
--- falsch
Die Zuordnung von Strömen zu logischen Werten: Fließt Basisstrom, gilt das als 1, sonst als 0. Beim Inverter gilt jeder Eingang über 0 V als 1, weil schon ein kleiner Basisstrom den Transistor leitend macht.
--- falsch
Die Zuordnung von Spannungen zu logischen Werten: Eine hohe Spannung gilt als 0, eine niedrige als 1. Beim Inverter gilt deshalb ein Eingang über $U_\mathrm{BE}$ als 0, darunter als 1.
--- falsch
Die beiden Versorgungsspannungen einer Logikschaltung, meist 0 V und 5 V. Beim Inverter gilt jeder Eingang zwischen diesen beiden Werten als gültige 1.
:::
:::karte formel Kennlinie des Inverters
Wie verläuft die Kennlinie des Inverters im linearen Modell in ihren drei Abschnitten?
---
Unter $U_\mathrm{BE}$ ist $U_\mathrm{aus}=U_\mathrm{CC}$. Von $U_\mathrm{BE}$ bis $U_\mathrm{ein,sat}$ fällt sie als Gerade, $U_\mathrm{aus}=U_\mathrm{CC}-B\,R_\mathrm{C}\dfrac{U_\mathrm{ein}-U_\mathrm{BE}}{R_\mathrm{B}}$, mit der Steigung $-B\,R_\mathrm{C}/R_\mathrm{B}$. Darüber bleibt $U_\mathrm{aus}=U_\mathrm{CE,sat}$.
--- falsch
Unter $U_\mathrm{BE}$ ist $U_\mathrm{aus}=0$. Von $U_\mathrm{BE}$ bis $U_\mathrm{ein,sat}$ steigt sie als Gerade, $U_\mathrm{aus}=B\,R_\mathrm{C}\dfrac{U_\mathrm{ein}-U_\mathrm{BE}}{R_\mathrm{B}}$, mit der Steigung $+B\,R_\mathrm{C}/R_\mathrm{B}$. Darüber bleibt $U_\mathrm{aus}=U_\mathrm{CC}$.
--- falsch
Unter $U_\mathrm{BE}$ ist $U_\mathrm{aus}=U_\mathrm{CC}$. Von $U_\mathrm{BE}$ bis $U_\mathrm{ein,sat}$ fällt sie als Gerade, $U_\mathrm{aus}=U_\mathrm{CC}-R_\mathrm{B}\dfrac{U_\mathrm{ein}-U_\mathrm{BE}}{B\,R_\mathrm{C}}$, mit der Steigung $-R_\mathrm{B}/(B\,R_\mathrm{C})$. Darüber bleibt $U_\mathrm{aus}=0$.
--- falsch
Unter $U_\mathrm{BE}$ ist $U_\mathrm{aus}=U_\mathrm{CC}$. Von $U_\mathrm{BE}$ bis $U_\mathrm{ein,sat}$ fällt sie exponentiell mit $\mathrm{e}^{-U_\mathrm{ein}/U_T}$, ohne gerades Stück. Darüber bleibt $U_\mathrm{aus}=U_\mathrm{CE,sat}$.
:::
:::karte formel Eingangsspannung an der Sättigungsgrenze
Bei welcher Eingangsspannung $U_\mathrm{ein,sat}$ erreicht der Inverter die Sättigung, und woher kommt die Formel?
---
$U_\mathrm{ein,sat}=\frac{(U_\mathrm{CC}-U_\mathrm{CE,sat})\,R_\mathrm{B}}{B\,R_\mathrm{C}}+U_\mathrm{BE}$. Man setzt den Basisstrom aus der Eingangsmasche in $U_\mathrm{CE}=U_\mathrm{CC}-B\,I_\mathrm{B}R_\mathrm{C}$ ein und löst bei $U_\mathrm{CE}=U_\mathrm{CE,sat}$ nach $U_\mathrm{ein}$ auf.
--- falsch
$U_\mathrm{ein,sat}=\frac{(U_\mathrm{CC}-U_\mathrm{CE,sat})\,B\,R_\mathrm{C}}{R_\mathrm{B}}+U_\mathrm{BE}$. Man setzt den Kollektorstrom aus der Arbeitsgeraden in die Eingangsmasche ein und löst bei $U_\mathrm{CE}=0$ nach $U_\mathrm{ein}$ auf.
--- falsch
$U_\mathrm{ein,sat}=U_\mathrm{CC}-U_\mathrm{CE,sat}$. Die Sättigung beginnt, sobald die Eingangsspannung so groß ist wie die Spannung am Kollektorwiderstand; $B$ und $R_\mathrm{B}$ spielen dafür keine Rolle.
--- falsch
$U_\mathrm{ein,sat}=\frac{U_\mathrm{CE,sat}\,R_\mathrm{B}}{B\,R_\mathrm{C}}-U_\mathrm{BE}$. Man setzt $I_\mathrm{C}=0$ in die Arbeitsgerade ein und löst nach $U_\mathrm{ein}$ auf, weil der Sperrbereich dort beginnt.
:::
:::karte zusammenhang Kleiner Basiswiderstand im Inverter
Warum wählt man beim Inverter $R_\mathrm{B}$ klein genug, dass $U_\mathrm{ein,sat}$ nahe an $U_\mathrm{BE}$ rückt?
---
Zwischen $U_\mathrm{BE}$ und $U_\mathrm{ein,sat}$ ist das Signal weder eindeutig 0 noch 1. Ein kleines $R_\mathrm{B}$ macht die Steigung $-B\,R_\mathrm{C}/R_\mathrm{B}$ steil und dieses Zwischengebiet schmal.
--- falsch
Ein kleines $R_\mathrm{B}$ senkt den Basisstrom und damit die Verlustleistung. Der Inverter bleibt dann auch bei hohem Eingang im aktiven Bereich, wo er linear arbeitet.
--- falsch
Ein kleines $R_\mathrm{B}$ verschiebt $U_\mathrm{BE}$ zu höheren Werten, sodass Störungen den Eingang nicht mehr über die Schwelle heben können. Die Steigung bleibt dabei gleich.
--- falsch
Ein kleines $R_\mathrm{B}$ macht die Steigung $-B\,R_\mathrm{C}/R_\mathrm{B}$ flach, sodass der Ausgang langsam und ohne Sprung umschaltet. So entstehen keine Störungen in der Versorgung.
:::
:::karte zusammenhang Übersteuerter Schalter
Warum bleibt ein Inverter mit $R_\mathrm{B}=20$ k$\Omega$ bei 5 V am Eingang auch mit einem schlechten Exemplar sicher eingeschaltet?
---
$I_\mathrm{B}=220$ µ A ergibt $B\,I_\mathrm{B}=44$ mA, weit über den 3,93 mA, die $R_\mathrm{C}$ zulässt. Der Transistor ist elffach übersteuert, auch ein deutlich kleineres $B$ hält ihn in der Sättigung.
--- falsch
$I_\mathrm{B}=220$ µ A ist größer als der Kollektorstrom, deshalb bestimmt der Basisstrom allein den Zustand. Ein schlechtes Exemplar hat dasselbe $I_\mathrm{B}$ und schaltet deshalb ebenso sicher.
--- falsch
5 V liegen weit über der Schwellspannung von 0,6 V, und jede Spannung über der Schwelle schaltet den Transistor voll ein, unabhängig von $B$, $R_\mathrm{B}$ und dem Strom, den $R_\mathrm{C}$ zulässt.
--- falsch
$B\,I_\mathrm{B}=44$ mA liegt genau bei dem Strom, den $R_\mathrm{C}$ zulässt. Der Transistor steht also exakt an der Grenze zur Sättigung, wo $B$ keine Rolle spielt.
:::
:::karte formel Leistung auf der Arbeitsgeraden
Wo auf der Arbeitsgeraden ist die Leistung $U_\mathrm{CE}I_\mathrm{C}$ im Transistor am größten, und wie groß ist sie dort?
---
Mit $U_\mathrm{CE}I_\mathrm{C}=U_\mathrm{CE}(U_\mathrm{CC}-U_\mathrm{CE})/R_\mathrm{C}$ liegt das Maximum bei $U_\mathrm{CC}/2$ und beträgt $U_\mathrm{CC}^2/(4R_\mathrm{C})$.
--- falsch
Mit $U_\mathrm{CE}I_\mathrm{C}=U_\mathrm{CC}^2/R_\mathrm{C}$ ist sie überall gleich groß, weil die Versorgung auf der ganzen Geraden dieselbe Leistung liefert.
--- falsch
Mit $U_\mathrm{CE}I_\mathrm{C}=U_\mathrm{CE}(U_\mathrm{CC}+U_\mathrm{CE})/R_\mathrm{C}$ liegt das Maximum bei $U_\mathrm{CE}=U_\mathrm{CC}$ und beträgt $2\,U_\mathrm{CC}^2/R_\mathrm{C}$.
--- falsch
Das Maximum liegt in der Sättigung bei $U_\mathrm{CE,sat}$, weil dort der größte Strom fließt; es beträgt $U_\mathrm{CC}^2/R_\mathrm{C}$.
:::
:::karte begriff Leistungshyperbel
Was beschreibt die Leistungshyperbel im Ausgangskennlinienfeld eines Transistors?
---
Die Grenzkurve $I_\mathrm{C}=P_\mathrm{max}/U_\mathrm{CE}$, auf der die Leistung im Transistor gleich $P_\mathrm{max}$ ist. Arbeitspunkte darüber machen das Bauteil zu heiß; für T liegt sie bei 40 V auf 10 mA.
--- falsch
Die Grenzkurve $I_\mathrm{C}=U_\mathrm{CE}/P_\mathrm{max}$, die mit der Spannung ansteigt. Arbeitspunkte darunter sind verboten, weil dort zu wenig Leistung für einen sicheren Betrieb des Transistors ankommt.
--- falsch
Die Arbeitsgerade bei voller Last, auf der die Leistung im Kollektorwiderstand konstant ist. Arbeitspunkte darüber überlasten den Widerstand, nicht den Transistor.
--- falsch
Die Kurve, auf der $U_\mathrm{CE}I_\mathrm{C}$ am kleinsten ist. Ein Schalter muss seine beiden Arbeitspunkte genau auf diese Kurve legen, sonst schaltet er nicht.
:::
:::karte zusammenhang Betriebsgrenzen
Welche drei Grenzwerte beschränken die erlaubten Arbeitspunkte eines Transistors, und was geschieht jenseits davon?
---
Über $U_\mathrm{CE,max}$ schlägt die CB-Grenze durch, über $I_\mathrm{C,max}$ überlasten Basis und Anschlussdrähte, über der Leistungshyperbel wird das Bauteil zu heiß. Außerhalb sinkt die Lebensdauer rapide.
--- falsch
$U_\mathrm{BE,max}$, $I_\mathrm{B,max}$ und $B_\mathrm{max}$: Über ihnen leitet die BE-Diode zu stark. Außerhalb arbeitet der Transistor weiter, nur mit kleinerer Verstärkung und etwas mehr Rauschen.
--- falsch
Über $U_\mathrm{CE,max}$ sperrt der Transistor dauerhaft, über $I_\mathrm{C,max}$ geht er in die Sättigung, über der Leistungshyperbel sinkt $B$ stark ab. Außerhalb arbeitet er deshalb nur noch als Schalter, aber ohne Schaden.
--- falsch
Über $U_\mathrm{CC}$, über $U_\mathrm{CC}/R_\mathrm{C}$ und über der Arbeitsgeraden. Diese Grenzen legt allein die Schaltung fest, das Bauteil selbst hat keine.
:::
::::

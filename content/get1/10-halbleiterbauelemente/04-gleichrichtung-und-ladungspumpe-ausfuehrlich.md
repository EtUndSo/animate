---
title: Gleichrichtung und Ladungspumpe
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Halbleiterbauelemente
order: 100600
summary: Wie Dioden aus Wechselspannung eine Gleichspannung machen und mit Kondensatoren eine Spannung sogar vervielfachen: Brückenschaltung nach Graetz mit Strompfaden und Totzone, Mittelwert, Glättung mit dem Ladekondensator und Brummspannung, Ladungspumpe mit Ladungsausgleich und Last. Ausführliche Fassung mit allen Herleitungen, einer Simulation der Glättung und der Energiebilanz der Ladungspumpe.
tags: Gleichrichter, Einweggleichrichter, Brückengleichrichter, Graetz, Glättung, Brummspannung, Ladungspumpe
stil: 3
fassung: ausfuehrlich
---

## Worum es geht

Das Stromnetz liefert Wechselspannung, Elektronik braucht Gleichspannung: Jedes Netzteil und jedes Ladegerät muss die Richtung des Stroms festlegen. Dioden können das, weil sie Strom nur in einer Richtung durchlassen.
**Eine Diode lässt Strom nur in eine Richtung: Gleichrichter lenken damit beide Halbwellen in derselben Richtung durch die Last, Kondensatoren halten die Ladung zwischen den Spitzen fest und glätten oder stapeln so die Spannung, und jede leitende Diode kostet ihre Durchlassspannung.**

Vorausgesetzt werden [Die Diode und ihre Kennlinie](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie.html), die Ersatzschaltungen und das Verfahren mit Annahmen aus [Arbeitspunkt und Ersatzschaltung der Diode](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/arbeitspunkt-und-ersatzschaltung.html) und der [Kondensator](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/kondensator/kondensator-und-kapazitaet.html).

:::grafik
Szene: get1/halbleiterbauelemente/04-bruecke-strompfade · Vorlage: schaltung-strompfade
**Abbildung 1:** Brückenschaltung nach Graetz mit Wechselspannungsquelle (10 V Scheitelwert), vier Dioden und Lastwiderstand. (a) In der positiven Halbwelle fließt der Strom über D1, die Last und D3; (b) in der negativen über D4, die Last und D2. Durch die Last fließt er in beiden Halbwellen in derselben Richtung.
:::

## Die Brückenschaltung nach Graetz

*Wie macht man aus beiden Halbwellen einen Strom, der die Last immer in derselben Richtung durchfließt?*

**Die Akteure:**

- __$u_e$__: Eingangsspannung, eine Sinusspannung mit dem Scheitelwert $\hat u_e$ = 10 V und der Frequenz 50 Hz; klein geschrieben, weil sie sich mit der Zeit ändert.
- __$u_a$__: Spannung an der Last, oben positiv gezählt.
- __$U_{F0}$__: Durchlassspannung im Ersatzschaltbild, wie im Skript 0,6 V.

**Das Zusammenspiel in Schritten:**

**Schritt 1**: Ist der obere Eingang positiv, liegt D1 mit ihrer Anode an ihm und kann leiten; der Strom fließt über D1 zum oberen Ende der Last, durch die Last nach unten und über D3 zurück zum unteren Eingang (Abbildung 1a). D2 und D4 liegen in Sperrrichtung.

**Schritt 2**: In der negativen Halbwelle ist der untere Eingang positiv. Jetzt leiten D4 und D2: Der Strom fließt vom unteren Eingang über D4 wieder zum oberen Ende der Last, durch sie nach unten und über D2 zum oberen Eingang (Abbildung 1b). D1 und D3 sperren.

**Schritt 3**: In beiden Fällen durchfließt der Strom die Last von oben nach unten. Die Last sieht den Betrag der Eingangsspannung, und die negative Halbwelle wird mitgenutzt; deshalb heißt die Schaltung __Doppelweggleichrichter__, im Gegensatz zum __Einweggleichrichter__ mit einer einzigen Diode, der nur die positiven Halbwellen durchlässt ([Halbleiter und das Bändermodell, ausführliche Fassung](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/halbleiter-und-baendermodell-ausfuehrlich.html), Abbildung 2).

**Schritt 4**: In jedem Strompfad liegen zwei leitende Dioden in Reihe. Jede kostet ihre Durchlassspannung; am Ausgang fehlen deshalb 1,2 V, und solange der Betrag der Eingangsspannung unter 1,2 V liegt, sperren alle vier Dioden (Abbildung 2).

:::formel Formel
$$\hat u_a = \hat u_e - 2\,U_{F0}$$

$$u_a = |u_e| - 2\,U_{F0} \quad\text{für } |u_e| > 2\,U_{F0}, \qquad u_a = 0 \quad\text{sonst}$$
:::

**So liest man das:** Eingabe ist die Eingangsspannung, Ausgabe die Spannung an der Last. Die Spitze am Ausgang ist um zwei Durchlassspannungen kleiner, 8,8 V statt 10 V, wie im Skript (Bild 10.29, S. 173). Um jeden Nulldurchgang gibt es eine __Totzone__, in der kein Strom fließt; bei 10 V Scheitelwert dauert sie 0,77 ms von jeder 10 ms langen Halbperiode.

**Kurz gesagt:** Bei vier gleichen Dioden ändert sich an der Last nichts, wenn man die beiden Anschlüsse der Quelle vertauscht; es zählt nur der Betrag der Eingangsspannung.

Idee der Herleitung: Maschenregel entlang des Strompfads mit zwei leitenden Dioden im Modell mit Durchlassspannung.

:::herleitung
**Ausgangspunkt:** die Maschenregel ([Kirchhoffsche Gesetze](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/strome-und-spannungen-in-netzen/kirchhoffsche-gesetze.html)) und das Modell mit Durchlassspannung aus [Arbeitspunkt und Ersatzschaltung der Diode](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/arbeitspunkt-und-ersatzschaltung.html): Eine leitende Diode ist eine Quelle $U_{F0}$, eine sperrende eine Unterbrechung.

**Annahmen:** (i) Modell mit $U_{F0}$; (ii) die Quelle hat keinen Innenwiderstand; (iii) die Last ist ohmsch.

**Schritt 1**: Positive Halbwelle, Annahme: D1 und D3 leiten, D2 und D4 sperren. Maschenregel entlang Quelle, D1, Last, D3:

$$u_e = U_{F0} + u_a + U_{F0} \quad\Rightarrow\quad u_a = u_e - 2\,U_{F0}$$

**Schritt 2** (entscheidender Schritt): Probe. Der Strom durch die Last und damit durch D1 und D3 ist $u_a/R$; er ist positiv, solange $u_e$ größer als $2U_{F0}$ ist. An D2 und D4 liegt dann die Spannung $-(u_a + U_{F0})$, also negativ: Sie sperren, die Annahme stimmt.

**Schritt 3**: Negative Halbwelle: Mit D2 und D4 ergibt dieselbe Masche, mit vertauschter Rolle der Eingänge,

$$u_a = -u_e - 2\,U_{F0}$$

Beides zusammen ist der Betrag der Eingangsspannung minus zwei Durchlassspannungen. Ist der Betrag kleiner als zwei Durchlassspannungen, ergäbe sich ein negativer Strom durch die angeblich leitenden Dioden; dann sperren alle vier, und die Ausgangsspannung ist null.

**Ergebnis:**

$$\hat u_a = \hat u_e - 2\,U_{F0}$$

$$u_a = |u_e| - 2\,U_{F0} \quad\text{für } |u_e| > 2\,U_{F0}, \qquad u_a = 0 \quad\text{sonst}$$

**Woher die Faktoren kommen:** Die 2 zählt die beiden Dioden, die in jedem Strompfad in Reihe liegen; der Betrag entsteht, weil die Brücke die Polung der negativen Halbwelle umkehrt.

**Proben:** Mit idealen Dioden ist die Ausgangsspannung der Betrag der Eingangsspannung. Mit 0,6 V: Spitze 8,8 V. Mit zwei Beispieldioden und ihrer exakten Kennlinie an 1 kΩ ergeben sich 8,60 V, weil bei 8,6 mA jede 0,70 V braucht.

**Grenzen:** Bei großen Strömen kommen Bahnwiderstände und der Innenwiderstand der Quelle hinzu; Gleichrichterdioden wie die 1N4001 haben bei 1 A bis zu 1,1 V.
:::

:::grafik
Szene: get1/halbleiterbauelemente/04-bruecke-zeitverlauf · Vorlage: zeitverlauf
**Abbildung 2:** Eingangsspannung (gestrichelt, Scheitelwert 10 V) und Ausgangsspannung der Brücke über 40 ms. Der Ausgang ist der Betrag des Eingangs minus 1,2 V, mit der Spitze 8,8 V und einer Totzone von 0,77 ms um jeden Nulldurchgang; die waagrechte Linie zeigt den Mittelwert von 5,21 V.
:::

Das Skript schreibt für die negative Halbwelle, bei negativer „oder sehr kleiner positiver“ Eingangsspannung leiteten D2 und D4 (S. 172). Bei kleiner positiver Spannung leiten sie nicht; für Beträge unter 1,2 V sperren alle vier Dioden, wie das Skript wenige Zeilen später selbst schreibt. D2 und D4 leiten erst unterhalb von −1,2 V.

:::frage
„Warum braucht man vier Dioden? Zwei würden doch reichen.“
Mit zwei Dioden geht es auch, aber nur mit einem Transformator, dessen Ausgangswicklung eine Mittelanzapfung hat: Jede Diode bedient dann eine Hälfte der Wicklung, und die Last liegt zwischen den Dioden und der Mitte (Mittelpunktschaltung). Dafür nutzt jede Halbwelle nur die halbe Wicklung. Die Brücke braucht keine Anzapfung und nutzt die ganze Wicklung in beiden Halbwellen; der Preis sind zwei Durchlassspannungen statt einer.
:::

:::fehlvorstellung
„Hinter dem Brückengleichrichter liegt eine Gleichspannung von 10 V.“
Das liegt nahe, weil die Spannung an der Last ihr Vorzeichen nicht mehr wechselt. Sie pulsiert aber zwischen null und 8,8 V im Takt von 100 Hz, zwei Pulse je Netzperiode; ihr Mittelwert liegt bei 5,21 V. Eine annähernd konstante Spannung entsteht erst mit einem Ladekondensator, und auch dann nicht 10 V, sondern etwas unter der Spitze von 8,8 V.
:::

## Mittelwert der gleichgerichteten Spannung

*Welche Gleichspannung steckt in einer pulsierenden Spannung?*

**Die Akteure:**

- __$\overline{u}$__: arithmetischer __Mittelwert__ über eine Periode, also die konstante Spannung, die in derselben Zeit dieselbe Spannungs-Zeit-Fläche hätte; ein Drehspulmessgerät oder ein Multimeter im Gleichspannungsbereich zeigt ihn an.

:::formel Formel
$$\overline{u}_\mathrm{Doppelweg} = \frac{2}{\pi}\,\hat u, \qquad \overline{u}_\mathrm{Einweg} = \frac{1}{\pi}\,\hat u$$
:::

**So liest man das:** Eingabe ist der Scheitelwert der Spannung, die gleichgerichtet wird, Ausgabe der Mittelwert der gleichgerichteten Spannung bei idealen Dioden. Der Doppelweggleichrichter liefert bei 10 V Scheitelwert 6,37 V, der Einweggleichrichter die Hälfte, 3,18 V, weil er jede zweite Halbwelle verwirft. Mit zwei Durchlassspannungen von je 0,6 V sinkt der Mittelwert der Brücke auf 5,21 V; wie man ihn ausrechnet, steht am Ende der Herleitung, und Abbildung 2 zeigt ihn als waagrechte Linie.

**Kurz gesagt:** Ohne Ladekondensator senken die beiden Durchlassspannungen den Mittelwert gegenüber idealen Dioden um weniger als $2U_{F0}$: Solange die Dioden leiten, fehlen dem Ausgang genau $2U_{F0}$, in der Totzone aber nur der Betrag der Eingangsspannung, der dort unter $2U_{F0}$ liegt.

Idee der Herleitung: Man berechnet die Fläche unter einer Sinushalbwelle und teilt durch die Dauer.

:::herleitung
**Ausgangspunkt:** die Definition des Mittelwerts als Fläche geteilt durch die Zeit:

$$\overline{u} = \frac{1}{T}\int_0^T u(t)\,\mathrm{d}t$$

**Annahmen:** (i) ideale Dioden; (ii) Sinusspannung $\hat u \sin(\omega t)$ mit der Kreisfrequenz $\omega = 2\pi/T$.

**Schritt 1**: Beim Doppelweggleichrichter wiederholt sich die Spannung nach einer halben Periode; es genügt, über eine Halbwelle zu mitteln:

$$\overline{u}_\mathrm{Doppelweg} = \frac{2}{T}\int_0^{T/2} \hat u\,\sin(\omega t)\,\mathrm{d}t$$

**Schritt 2** (entscheidender Schritt): Die Fläche unter einer Sinushalbwelle ist $2/\omega$ mal den Scheitelwert:

$$\int_0^{T/2} \sin(\omega t)\,\mathrm{d}t = \Big[-\frac{\cos(\omega t)}{\omega}\Big]_0^{T/2} = \frac{2}{\omega} = \frac{T}{\pi}$$

**Schritt 3**: Eingesetzt:

$$\overline{u}_\mathrm{Doppelweg} = \frac{2}{T}\cdot\hat u\cdot\frac{T}{\pi} = \frac{2}{\pi}\,\hat u$$

Der Einweggleichrichter hat in jeder Periode nur eine Halbwelle, also die halbe Fläche bei gleicher Periodendauer.

**Ergebnis:**

$$\overline{u}_\mathrm{Doppelweg} = \frac{2}{\pi}\,\hat u, \qquad \overline{u}_\mathrm{Einweg} = \frac{1}{\pi}\,\hat u$$

**Woher die Faktoren kommen:** $2/\pi$ ist die mittlere Höhe einer Sinushalbwelle, bezogen auf ihre Spitze; der Einweggleichrichter halbiert sie, weil er die Hälfte der Zeit nichts liefert.

**Proben:** Einheit V. Zahlenwert: 2 durch π mal 10 V ergibt 6,37 V; die numerische Mittelung im Zahlenwerk liefert dasselbe.

**Grenzen:** Mit Durchlassspannungen fehlen an jeder Halbwelle 1,2 V und die Stücke um die Nulldurchgänge. Die Dioden leiten dann nur zwischen den Winkeln $\theta_1$ und $\pi - \theta_1$, wobei $\theta$ für $\omega t$ steht und

$$\theta_1 = \arcsin\frac{2\,U_{F0}}{\hat u}$$

die Grenze der Totzone ist. Gemittelt wird weiter über die ganze Halbwelle, integriert aber nur über die Leitphase:

$$\overline{u} = \frac{1}{\pi}\int_{\theta_1}^{\pi-\theta_1}\big(\hat u\sin\theta - 2\,U_{F0}\big)\,\mathrm{d}\theta$$

Der Sinus liefert das Doppelte von $\hat u\cos\theta_1$, die Konstante ihr Produkt mit der Dauer der Leitphase $\pi - 2\theta_1$:

$$\overline{u} = \frac{2}{\pi}\Big[\hat u\cos\theta_1 - 2\,U_{F0}\Big(\frac{\pi}{2} - \theta_1\Big)\Big]$$

Mit 10 V und 0,6 V ist $\theta_1$ = 0,1203, und es ergeben sich 5,21 V wie bei der numerischen Mittelung im Zahlenwerk.
:::

::::beispiel Brücke ohne Glättung bei 10 V Scheitelwert
**Gegeben:** Sinusspannung mit 10 V Scheitelwert und 50 Hz; Brücke mit vier Dioden im 0,6 V-Modell; Last 1 kΩ.

**Gesucht:** Spitze am Ausgang, Dauer der Totzone, Mittelwert, Sperrspannung an den Dioden.

**Rechnung:** Spitze nach Formel 1:

$$\hat u_a = 10\ \mathrm{V} - 2\cdot0{,}6\ \mathrm{V} = 8{,}8\ \mathrm{V}$$

Die Totzone reicht vom Nulldurchgang bis $|u_e|$ = 1,2 V, auf beiden Seiten. Der Winkel, bei dem die Sinusspannung 1,2 V erreicht, und die zugehörige Dauer bei 50 Hz:

$$\omega t_1 = \arcsin\frac{1{,}2\ \mathrm{V}}{10\ \mathrm{V}} = 0{,}1203, \qquad 2\,t_1 = \frac{2\cdot0{,}1203}{2\pi\cdot50\ \mathrm{Hz}} = 0{,}77\ \mathrm{ms}$$

Mittelwert ideal nach Formel 2, mit den Durchlassspannungen nach der Formel am Ende der Herleitung:

$$\overline{u}_\mathrm{ideal} = \frac{2}{\pi}\cdot10\ \mathrm{V} = 6{,}37\ \mathrm{V}, \qquad \overline{u} = 5{,}21\ \mathrm{V}$$

Eine sperrende Diode liegt parallel zur Reihe aus Last und leitender Diode, an ihr liegt also bis zu

$$\hat u_e - U_{F0} = 9{,}4\ \mathrm{V}$$

**Ergebnis:** **Spitze 8,8 V, Totzone 0,77 ms je Nulldurchgang, Mittelwert 5,21 V, Sperrspannung bis 9,4 V.**

**Einordnung:** Mit den exakten Kennlinien zweier Beispieldioden wäre die Spitze 8,60 V, weil die Dioden bei 8,6 mA je 0,70 V brauchen. Die Dioden müssen in Sperrrichtung nur den Scheitelwert der Eingangsspannung aushalten; beim Einweggleichrichter mit Ladekondensator ist es rund das Doppelte, 19,4 V, weil dort der geladene Kondensator und die Quelle in Reihe gegen die Diode stehen.
::::

## Glättung mit dem Ladekondensator

*Wie wird aus der pulsierenden Spannung eine fast konstante?*

:::grafik
Szene: get1/halbleiterbauelemente/04-glaettung · Vorlage: schaltung-und-zeitverlauf
**Abbildung 3:** (a) Brücke mit Ladekondensator 470 µF parallel zur Last 470 Ω; die Quelle hat 5 Ω Innenwiderstand. (b) Oben die Kondensatorspannung zwischen 8,05 und 8,34 V, gestrichelt der Betrag der Eingangsspannung minus 1,2 V; unten der Diodenstrom: Pulse von 2,2 ms mit 118 mA Spitze, dazu der Laststrom von 17,4 mA. Der Kondensator wird nur kurz um die Spitzen nachgeladen und speist die Last dazwischen allein.
:::

**Die Akteure:**

- __$C$__: __Ladekondensator__ parallel zur Last; 470 µF im Beispiel.
- __$I_L$__: Laststrom, der fast konstant ist, weil die Spannung kaum schwankt; 17,4 mA im Beispiel.
- __$\Delta U$__: __Brummspannung__, die Schwankung der geglätteten Spannung von Spitze zu Spitze.
- __$f$__: Netzfrequenz, 50 Hz; der Brückengleichrichter liefert zwei Pulse je Periode, also 100 je Sekunde.

**Das Zusammenspiel in Schritten:**

**Schritt 1**: Steigt der Betrag der Eingangsspannung über die Kondensatorspannung plus 1,2 V, leiten zwei Dioden und laden den Kondensator nach, bis kurz nach der Spitze.

**Schritt 2**: Kurz nach der Spitze fällt die Eingangsspannung schneller, als der Kondensator sich über die Last entlädt. Sobald ihr Betrag unter die Kondensatorspannung plus 1,2 V sinkt, kann sie keinen Strom mehr über zwei Dioden in den Kondensator treiben, und alle vier sperren; im Beispiel bei 9,54 V am Eingang und 8,34 V am Kondensator.

**Schritt 3**: Bis zur nächsten Spitze speist der Kondensator die Last allein. Er gibt dabei Ladung ab, und seine Spannung sinkt fast linear, um die Brummspannung (Abbildung 3b oben).

**Schritt 4**: Die ganze Ladung, die die Last in 10 ms verbraucht, muss in den kurzen Leitphasen nachfließen. Die Dioden leiten deshalb nur gut 2 ms je Halbwelle, ein __Stromflusswinkel__ von 40° von 180°, und führen dabei Spitzenströme vom Siebenfachen des Laststroms (Abbildung 3b unten).

:::formel Formel
$$\Delta U \approx \frac{I_L}{2\,f\,C}$$
:::

**So liest man das:** Eingabe sind Laststrom, Netzfrequenz und Kapazität, Ausgabe die Brummspannung. Doppelter Laststrom gibt doppelten Brumm, doppelte Kapazität den halben. Die Formel ist eine obere Schätzung, weil sie annimmt, dass der Kondensator die ganze Halbperiode entladen wird. Beim Einweggleichrichter steht im Nenner $f$ statt $2f$, der Brumm ist bei gleichem Kondensator doppelt so groß.

Idee der Herleitung: Zwischen zwei Ladepulsen gibt der Kondensator den Laststrom ab; die Spannung sinkt um Ladung durch Kapazität.

:::herleitung
**Ausgangspunkt:** die Beziehung zwischen Strom und Spannung am Kondensator ([Kondensator und Kapazität](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/kondensator/kondensator-und-kapazitaet.html)):

$$i_C = C\,\frac{\mathrm{d}u_C}{\mathrm{d}t}$$

**Annahmen:** (i) Die Brummspannung ist klein gegen die Ausgangsspannung; der Laststrom ist deshalb fast konstant $I_L$. (ii) Die Ladephasen sind kurz; der Kondensator entlädt sich höchstens eine halbe Netzperiode lang, $1/(2f)$.

**Schritt 1**: Während die Dioden sperren, fließt der Laststrom allein aus dem Kondensator:

$$C\,\frac{\mathrm{d}u_C}{\mathrm{d}t} = -I_L$$

**Schritt 2** (entscheidender Schritt): Bei konstantem Strom sinkt die Spannung linear; über die Entladezeit $1/(2f)$ um

$$\Delta U = \frac{I_L}{C}\cdot\frac{1}{2\,f}$$

**Ergebnis:**

$$\Delta U \approx \frac{I_L}{2\,f\,C}$$

**Woher die Faktoren kommen:** $I_L/C$ ist die Geschwindigkeit, mit der die Spannung sinkt; $1/(2f)$ ist die Zeit zwischen zwei Pulsen der Brücke.

**Proben:** Einheit A durch Hz mal F ergibt A s durch F, also V. Zahlenwert: 17,4 mA durch 100 Hz mal 470 µF ergibt 0,37 V. Die Simulation liefert 0,29 V: Der Kondensator entlädt sich nicht 10 ms, sondern nur etwa 7,8 ms, solange die Dioden sperren, und 0,37 V mal 0,78 ergibt 0,29 V.

**Grenzen:** Bei großem Brumm sinkt der Laststrom mit der Spannung, und die Ladephasen werden lang; die Schätzung wird dann ungenau.
:::

::::beispiel Ladekondensator für ein kleines Netzteil
**Gegeben:** Quelle mit 10 V Scheitelwert, 50 Hz und 5 Ω Innenwiderstand; Brücke im 0,6 V-Modell; Last 470 Ω; Ladekondensator 470 µF (Simulation im Zahlenwerk).

**Gesucht:** Ausgangsspannung, Brummspannung nach der Schätzung und nach der Simulation, Leitdauer und Spitzenstrom der Dioden; die Kapazität für 0,1 V Brumm.

**Rechnung:** Die Simulation ergibt eine Kondensatorspannung zwischen 8,05 und 8,34 V, im Mittel 8,19 V, also einen Laststrom von

$$I_L = \frac{8{,}19\ \mathrm{V}}{470\ \Omega} = 17{,}4\ \mathrm{mA}$$

Schätzung nach Formel 3:

$$\Delta U \approx \frac{17{,}4\ \mathrm{mA}}{2\cdot50\ \mathrm{Hz}\cdot470\ \mu\mathrm{F}} = 0{,}37\ \mathrm{V}$$

Die Simulation zeigt 0,29 V; die Dioden leiten je Halbwelle 2,2 ms mit bis zu 118 mA. Für 0,1 V Brumm braucht man nach der Schätzung

$$C = \frac{17{,}4\ \mathrm{mA}}{2\cdot50\ \mathrm{Hz}\cdot0{,}1\ \mathrm{V}} = 1740\ \mu\mathrm{F}$$

Die Simulation kommt schon mit 1375 µF auf 0,1 V, denn die Schätzung überschätzt den Brumm hier wie bei 470 µF um gut ein Viertel.

**Ergebnis:** **8,19 V im Mittel mit 0,29 V Brumm (Schätzung 0,37 V); Ladepulse von 2,2 ms und 118 mA; für 0,1 V Brumm nach der Schätzung rund 1700 µF, nach der Simulation genügen rund 1400 µF.**

**Einordnung:** Der Brumm sinkt mit der Kapazität, der Spitzenstrom nicht: Mit 100 µF beträgt er 109 mA, mit 1000 µF 119 mA, denn immer muss dieselbe Ladung in die kurzen Phasen nahe der Spitze passen. Netzteile mit großem Ladekondensator belasten Transformator und Netz deshalb mit kurzen, hohen Strompulsen; feinere Stabilisierung übernehmen danach Spannungsregler.
::::

:::fehlvorstellung
„Die Dioden im Netzteil führen den Laststrom gleichmäßig.“
Das liegt nahe, weil der Laststrom selbst fast konstant ist. Die Dioden leiten aber nur, solange der Betrag der Eingangsspannung um mehr als 1,2 V über der Kondensatorspannung liegt, im Beispiel gut 2 ms je Halbwelle. In dieser Zeit muss die Ladung für die ganzen 10 ms nachfließen; die Spitzenströme erreichen deshalb 118 mA bei 17,4 mA Laststrom. Dioden und Transformator müssen für diese Pulse bemessen sein.
:::

:::frage
„Was begrenzt den Spitzenstrom, wenn die Dioden leiten?“
Im Modell allein der Innenwiderstand der Quelle, im Beispiel 5 Ω, also der Widerstand der Transformatorwicklung, dazu die Bahnwiderstände der Dioden. Beim Einschalten ist der Kondensator leer, und der erste Puls ist viel größer: Er lädt den Kondensator über diese wenigen Ohm von null auf; im Beispiel erreicht er 1,76 A, wenn man im Scheitel einschaltet, und 0,8 A beim Einschalten im Nulldurchgang. Größere Netzteile begrenzen diesen Einschaltstrom deshalb eigens.
:::

## Die Ladungspumpe

*Wie kann eine Schaltung aus 5 V fast das Doppelte machen?*

:::grafik
Szene: get1/halbleiterbauelemente/04-ladungspumpe-takte · Vorlage: schaltung-zustaende
**Abbildung 4:** Die Ladungspumpe des Skripts mit 5 V Eingangsspannung. (a) Takt 1: Die Unterseite von C1 liegt an Masse, über D1 und R1 lädt C1 auf 4,4 V. (b) Takt 2: Die Unterseite von C1 liegt an 5 V, seine Oberseite damit auf 9,4 V; D1 sperrt, über R2 und D2 fließt Ladung in C2, der sich 8,8 V nähert. Der geladene Kondensator wird auf die Eingangsspannung gestapelt.
:::

**Die Akteure:**

- __$U_e$__: Eingangsspannung, 5 V.
- __$C_1$__: __Pumpkondensator__, der abwechselnd geladen und auf die Eingangsspannung gestapelt wird; 1 µF.
- __$C_2$__: __Ausgangskondensator__, an dem die erhöhte Spannung $U_a$ abgenommen wird; 1 µF.
- __$f$__: Taktfrequenz des Umschalters, 10 kHz. Eine __Periode__ von 100 µs besteht aus Takt 1 und Takt 2 mit je 50 µs; in der Praxis schalten Transistoren.
- __$R_1$__, __$R_2$__: Widerstände, die die Ströme beim Umladen begrenzen; mit 10 Ω ist die Zeitkonstante 10 µs, kurz gegen einen Takt.

**Das Zusammenspiel in Schritten:**

**Schritt 1**: In Takt 1 liegt die Unterseite von C1 an Masse. Über D1 und R1 lädt die Quelle C1 auf ihre Spannung abzüglich der Durchlassspannung von D1, auf 4,4 V (Abbildung 4a).

**Schritt 2**: In Takt 2 schaltet der Umschalter die Unterseite von C1 an die Eingangsspannung. Der geladene Kondensator steht damit auf den 5 V, seine Oberseite springt auf die Summe, 9,4 V. D1 sperrt, denn ihre Kathode liegt nun 4,4 V über ihrer Anode. Im Skriptbild (Bild 10.23 und 10.24, S. 171) ist die Unterseite von C1 zusätzlich fest mit Masse verbunden; das ist ein Zeichenfehler, denn über diese Leitung schlösse der Umschalter in Takt 2 die Quelle kurz.

**Schritt 3**: Über R2 und D2 fließt Ladung von C1 nach C2, bis die Oberseite von C1 nur noch eine Durchlassspannung über C2 liegt. Dabei gleichen sich die beiden Kondensatoren aus: C1 verliert Spannung, C2 gewinnt.

**Schritt 4**: Periode für Periode wiederholt sich das. Nur in der allerersten leitet D2 schon in Takt 1: C2 ist noch leer, und die Quelle lädt ihn über D1 und D2 mit auf, bis auf zwei Durchlassspannungen unter der Eingangsspannung, 3,8 V. Danach halbiert bei gleichen Kapazitäten jede Periode den Abstand zwischen der Spannung an C2 und dem Endwert, der eine Durchlassspannung unter den 9,4 V liegt, also bei 8,8 V: Am Ende der Perioden liegt C2 bei 6,3 V, 7,55 V, 8,18 V, 8,49 V und so weiter (Abbildung 5). Das Skript gibt „ca. 2 U_e“ an und betrachtet die Dioden als ideal (S. 171), schreibt am Kondensator aber $U_e - U_{D1}$; mit Durchlassspannungen sind es 8,8 V statt 10 V.

**Schritt 5**: Zieht eine Last Strom, muss C1 jede Periode die verbrauchte Ladung nachliefern und sich dafür in Takt 2 weiter entladen; der Ausgang bleibt unter dem Endwert. D2 bleibt dabei nach dem Ausgleich leitend: Sobald die Last C2 ein wenig entlädt, liegt an D2 wieder mehr als die Durchlassspannung, und C1 speist mit. Bis zum Ende von Takt 2 teilen sich C1 und C2 deshalb den Laststrom; in Takt 1 speist C2 die Last allein.

:::formel Formel
$$U_a = 2\,U_e - 2\,U_{F0} - \frac{I_L}{f\,C_1}$$
:::

**So liest man das:** Eingabe sind Eingangsspannung, Laststrom, Taktfrequenz und Pumpkondensator, Ausgabe die Spannung an C2 am Ende von Takt 2. Ohne Last ist sie das Doppelte der Eingangsspannung abzüglich zweier Durchlassspannungen. Last zieht sie herunter, als hätte die Pumpe einen Innenwiderstand $1/(f\,C_1)$, bei 10 kHz und 1 µF 100 Ω; ein größerer Pumpkondensator oder ein schnellerer Takt verkleinert ihn. Um diesen Wert pendelt der Ausgang: In Takt 1 sinkt er, weil C2 allein speist, beim Ausgleich springt er hoch, und im Rest von Takt 2 sinkt er langsamer, weil C1 mitspeist.

Idee der Herleitung: Ladungserhaltung beim Ausgleich zwischen C1 und C2 und Ladungsbilanz je Periode.

:::herleitung
**Ausgangspunkt:** die Maschenregel, die Beziehung zwischen Ladung und Spannung am Kondensator und die Erhaltung der Ladung beim Umladen.

**Annahmen:** (i) Modell mit Durchlassspannung $U_{F0}$; (ii) jeder Takt dauert lang gegen die Zeitkonstanten, die Kondensatoren gleichen sich vollständig aus; (iii) im eingeschwungenen Zustand hat C2 am Ende jeder Periode wieder dieselbe Spannung.

**Schritt 1**: Takt 1, Masche aus Quelle, D1 und C1:

$$U_{C1} = U_e - U_{F0}$$

**Schritt 2**: Takt 2: Die Oberseite von C1 liegt auf $U_e + U_{C1}$. D2 leitet, solange diese Spannung um mehr als $U_{F0}$ über $U_{C2}$ liegt. Fließt dabei die Ladung $\Delta Q$, sinkt $U_{C1}$ um $\Delta Q/C_1$ und $U_{C2}$ steigt um $\Delta Q/C_2$. Der Ausgleich endet, wenn

$$U_e + U_{C1} - \frac{\Delta Q}{C_1} = U_{C2} + \frac{\Delta Q}{C_2} + U_{F0}$$

**Schritt 3**: Mit Schritt 1 und dem Endwert $U^* = 2U_e - 2U_{F0}$ aufgelöst:

$$\Delta Q\,\Big(\frac{1}{C_1} + \frac{1}{C_2}\Big) = U^* - U_{C2}$$

Ohne Last wächst $U_{C2}$ damit je Periode um den Anteil $C_1/(C_1 + C_2)$ des Abstands zu $U^*$, bei gleichen Kapazitäten um die Hälfte.

**Schritt 4**: Mit Last bleibt D2 nach dem Ausgleich leitend, denn die Last senkt $U_{C2}$ weiter, und an D2 läge sonst mehr als $U_{F0}$. Am Ende von Takt 2 gilt deshalb die Masche über Quelle, C1, D2 und C2:

$$U_a = U_e + U_{C1,\mathrm{Ende}} - U_{F0}$$

**Schritt 5** (entscheidender Schritt): Ladungsbilanz. Weil C2 am Ende jeder Periode wieder dieselbe Spannung hat, fließt die ganze Ladung, die die Last in einer Periode verbraucht, in Takt 2 über D2 aus C1:

$$\Delta Q = \frac{I_L}{f}$$

C1 beginnt Takt 2 mit $U_e - U_{F0}$ und verliert diese Ladung:

$$U_{C1,\mathrm{Ende}} = U_e - U_{F0} - \frac{I_L}{f\,C_1}$$

In Schritt 4 eingesetzt:

$$U_a = U_e + \Big(U_e - U_{F0} - \frac{I_L}{f\,C_1}\Big) - U_{F0}$$

**Ergebnis:**

$$U_a = 2\,U_e - 2\,U_{F0} - \frac{I_L}{f\,C_1}$$

**Woher die Faktoren kommen:** Die 2 vor $U_e$ entsteht durch das Stapeln von C1 auf die Quelle, die 2 vor $U_{F0}$ durch die beiden Dioden; $I_L/(f\,C_1)$ ist die Spannung, um die C1 sich je Periode entladen muss, um die Ladung der Last zu liefern.

**Proben:** Ohne Last: 8,8 V. Mit 1 mA, 10 kHz und 1 µF: 0,1 V weniger, 8,7 V am Ende von Takt 2. Die Rechnung Takt für Takt im Zahlenwerk ergibt nach dem Einschwingen genau diesen Wert und dazu den Verlauf: In Takt 1 fällt der Ausgang um 0,05 V auf 8,65 V, beim Ausgleich springt er auf 8,725 V, im Rest von Takt 2 fällt er um 0,025 V zurück auf 8,70 V. Einheit: A durch Hz mal F ergibt V.

**Grenzen:** Sind die Zeitkonstanten nicht kurz gegen einen Takt, gleichen sich die Kondensatoren nicht vollständig aus, und der Ausgang sinkt weiter; mit den 10 Ω des Beispiels liegt er im Mittel bei 8,68 statt 8,69 V. Reale Dioden haben bei kleinen Strömen kleinere Durchlassspannungen als 0,6 V.
:::

:::grafik
Szene: get1/halbleiterbauelemente/04-ladungspumpe-aufladen · Vorlage: treppenverlauf
**Abbildung 5:** Spannung an C2. (a) Ohne Last über die ersten zehn Perioden (1 ms): nach dem ersten Takt 1 schon 3,8 V, weil D2 mitleitet, am Ende der Perioden 6,30, 7,55, 8,18, 8,49, 8,64 V und so weiter gegen 8,8 V; jede Periode halbiert den Abstand zum Endwert. (b) Mit 1 mA Last im eingeschwungenen Zustand, zwei Perioden vergrößert: Abfall um 0,05 V in Takt 1, Sprung um 0,075 V beim Ausgleich, Abfall um 0,025 V im Rest von Takt 2. Der Ausgang pendelt zwischen 8,65 und 8,725 V; am Ende von Takt 2 liegt er bei 8,70 V, 0,1 V unter dem Endwert.
:::

::::beispiel Ladungspumpe an 5 V
**Gegeben:** Eingangsspannung 5 V; 0,6 V-Modell für beide Dioden; C1 = C2 = 1 µF; Taktfrequenz 10 kHz; (a) ohne Last, (b) mit 1 mA Last.

**Gesucht:** Spannung an C2 in den ersten Perioden, Endwert, Ausgang unter Last, Strom aus der Quelle.

**Rechnung:** (a) Endwert:

$$U^* = 2\cdot5\ \mathrm{V} - 2\cdot0{,}6\ \mathrm{V} = 8{,}8\ \mathrm{V}$$

Im ersten Takt 1 lädt die Quelle C2 über D2 auf 5 V minus 1,2 V, also 3,8 V; der Abstand zum Endwert ist dann 5 V. Jede Periode halbiert ihn: Am Ende der Perioden liegt C2 bei 6,3 V, 7,55 V, 8,18 V, und nach zehn Perioden, also 1 ms, fehlen nur noch

$$U^* - U_{C2} = \frac{5\ \mathrm{V}}{2^{10}} = 4{,}9\ \mathrm{mV}$$

(b) Ausgang unter Last am Ende von Takt 2 nach Formel 4:

$$U_a = 8{,}8\ \mathrm{V} - \frac{1\ \mathrm{mA}}{10\ \mathrm{kHz}\cdot1\ \mu\mathrm{F}} = 8{,}7\ \mathrm{V}$$

In Takt 1 speist C2 die Last allein, seine Spannung sinkt in den 50 µs um

$$\frac{I_L}{2\,f\,C_2} = \frac{1\ \mathrm{mA}}{2\cdot10\ \mathrm{kHz}\cdot1\ \mu\mathrm{F}} = 0{,}05\ \mathrm{V}$$

Beim Ausgleich springt sie um 0,075 V auf 8,725 V; im Rest von Takt 2 speisen C1 und C2 gemeinsam, und sie sinkt nur um die Hälfte davon, 0,025 V, zurück auf 8,7 V.

Je Periode fließen 100 nC zur Last. Die Quelle liefert diese Ladung zweimal: in Takt 1 in C1, in Takt 2 durch C1 nach C2. Ihr mittlerer Strom ist deshalb 2 mA.

**Ergebnis:** **Ohne Last 8,8 V nach etwa zehn Perioden; mit 1 mA zwischen 8,65 und 8,725 V, am Ende von Takt 2 8,7 V, bei 2 mA aus der Quelle.**

**Einordnung:** Die Quelle gibt 10 mW ab, am Ausgang kommen im Mittel 8,69 mW an; 1,2 mW verbrauchen die Dioden, die übrigen 0,11 mW gehen beim Umladen in R1 und R2 verloren. Eine Simulation der Schaltung mit den 10-Ω-Widerständen bestätigt das: Sie liefert 8,64 bis 8,71 V und 8,68 mW. Mit einem zehnmal kleineren Pumpkondensator, 0,1 µF, sänke der Ausgang bei derselben Last auf 7,8 V.
::::

:::fehlvorstellung
„Die Ladungspumpe gewinnt Leistung, weil sie die Spannung verdoppelt.“
Das liegt nahe, weil am Ausgang fast die doppelte Spannung anliegt. Die Quelle liefert aber auch den doppelten Strom: Jede Ladung, die zur Last fließt, kommt zweimal aus ihr, einmal beim Laden von C1 und einmal beim Umladen nach C2. Im Beispiel stehen 10 mW aus der Quelle 8,69 mW an der Last gegenüber; der Rest wird in den Dioden und Widerständen zu Wärme.
:::

Nach demselben Schema lassen sich mehrere Stufen hintereinanderschalten (Skript, S. 171): Jede weitere stapelt einen Kondensator mehr auf, und die Leerlaufspannung wächst mit jeder Stufe um etwa die Eingangsspannung, abzüglich der Durchlassspannungen. So erzeugen Ladungspumpen in Chips die Programmierspannung von Flash-Speichern und in Hochspannungsgeräten Kilovolt aus Netzspannung.

## Alles hängt an einem Prinzip

| Einzelheit | welche Seite des Prinzips sie zeigt |
|---|---|
| Brückenschaltung | Vier Ventile lenken beide Halbwellen in dieselbe Richtung durch die Last. |
| 1,2 V Verlust und Totzone | Jede leitende Diode kostet ihre Durchlassspannung, im Pfad liegen zwei. |
| Ladekondensator und Brumm | Der Kondensator hält die Ladung von Spitze zu Spitze; die Dioden sperren dazwischen. |
| kurze Ladepulse | Die Ventile öffnen nur, wenn die Quelle um zwei Durchlassspannungen über dem Speicher liegt. |
| Ladungspumpe | Ventile und Umschalter stapeln einen geladenen Kondensator auf die Quelle. |
| Energiebilanz | Stapeln verdoppelt die Spannung, nicht die Leistung; die Quelle liefert doppelten Strom. |

Eine Diode lässt Strom nur in eine Richtung: Gleichrichter lenken damit beide Halbwellen in derselben Richtung durch die Last, Kondensatoren halten die Ladung zwischen den Spitzen fest und glätten oder stapeln so die Spannung, und jede leitende Diode kostet ihre Durchlassspannung.

## Bedeutung und Ausblick

Die meisten Netzteile mit Transformator beginnen mit einem Brückengleichrichter und einem Ladekondensator; auch Schaltnetzteile richten die Netzspannung zuerst so gleich. Ladungspumpen versorgen Schnittstellenbausteine mit Hilfsspannungen und erzeugen in Speicherchips die Programmierspannung.
Die geglättete Spannung schwankt noch mit der Last und dem Netz; wie man sie mit einer Z-Diode und einem Transistor stabilisiert, behandelt das Skript in Kapitel 11.6 (S. 192; der Verweis auf S. 170 nennt versehentlich 11.5), die Grundlage dafür der Artikel [Die Diode und ihre Kennlinie](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie.html).
Der nächste Artikel, [Aufbau und Wirkungsweise des Bipolartransistors](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/aufbau-und-wirkungsweise.html), setzt zwei pn-Übergänge zu einem Verstärker zusammen.

:::kern
- In der Brücke leiten je Halbwelle zwei Dioden in Reihe; der Strom durchfließt die Last immer in derselben Richtung.
- Ausgang ohne Glättung: $u_a = |u_e| - 2U_{F0}$; um jeden Nulldurchgang sperren alle Dioden.
- Ein Ladekondensator hält die Ladung von Spitze zu Spitze; dazwischen sperren die Dioden, und er speist die Last allein.
- Brummspannung: $\Delta U \approx I_L/(2fC)$ als obere Schätzung; die Dioden leiten nur kurz, mit Spitzenströmen weit über dem Laststrom.
- Ladungspumpe: Takt 1 lädt den Pumpkondensator, Takt 2 stapelt ihn auf die Eingangsspannung; der Ausgang strebt gegen $2U_e - 2U_{F0}$.
- Unter Last: $U_a = 2U_e - 2U_{F0} - I_L/(fC_1)$; die Quelle liefert den doppelten Strom, Leistung entsteht keine.
:::

:::quiz
F: Warum fließt der Strom in der Brückenschaltung in beiden Halbwellen in derselben Richtung durch die Last?
A: In der positiven Halbwelle leiten D1 und D3, in der negativen D2 und D4. Beide Paare führen den Strom zum selben Ende der Last, die Brücke kehrt die Polung der negativen Halbwelle um.
F: Warum ist die Spitze am Ausgang der Brücke 1,2 V kleiner als die Spitze am Eingang?
A: In jedem Strompfad liegen zwei leitende Dioden in Reihe, jede mit 0,6 V im Modell des Skripts. Aus 10 V werden 8,8 V.
F: Stimmt es, dass hinter einem Brückengleichrichter ohne Kondensator eine Gleichspannung liegt?
A: Nein. Die Spannung wechselt ihr Vorzeichen nicht mehr, pulsiert aber zwischen null und 8,8 V im Takt von 100 Hz; ihr Mittelwert liegt bei 5,21 V.
F: Welchen Mittelwert hat eine doppelweg gleichgerichtete Sinusspannung mit 10 V Scheitelwert bei idealen Dioden?
A: Zwei durch π mal den Scheitelwert, 6,37 V; beim Einweggleichrichter die Hälfte, 3,18 V.
F: Warum leiten die Dioden mit Ladekondensator nur kurz?
A: Weil sie nur leiten, solange der Betrag der Eingangsspannung um mehr als 1,2 V über der Kondensatorspannung liegt, und das ist nur kurz um die Spitzen der Fall. Im Beispiel gut 2 ms je Halbwelle.
F: Wie groß ist die Brummspannung nach der Schätzung bei 17,4 mA Laststrom, 50 Hz und 470 µF hinter einer Brücke?
A: 17,4 mA durch 2 mal 50 Hz mal 470 µF ergibt 0,37 V. Die Simulation liefert 0,29 V, weil der Kondensator sich nicht die ganze Halbperiode entlädt.
F: Stimmt es, dass die Dioden im Netzteil den Laststrom gleichmäßig führen?
A: Nein. Sie liefern die Ladung in kurzen Pulsen nahe der Spitzen; im Beispiel mit 118 mA Spitze bei 17,4 mA Laststrom.
F: Warum sperrt D1 in Takt 2 der Ladungspumpe?
A: Weil die Unterseite von C1 nun an 5 V liegt und seine Oberseite damit auf 9,4 V. An der Kathode von D1 liegt also mehr Spannung als an ihrer Anode mit 5 V.
F: Stimmt es, dass die Ladungspumpe Leistung gewinnt, weil sie die Spannung fast verdoppelt?
A: Nein. Die Quelle liefert jede Ladung zweimal, ihr Strom ist doppelt so groß wie der Laststrom. Im Beispiel stehen 10 mW aus der Quelle 8,69 mW am Ausgang gegenüber.
F: Wie stark sinkt die Ausgangsspannung der Ladungspumpe mit 10 kHz Taktfrequenz und 1 µF Pumpkondensator bei 1 mA Last?
A: Um den Laststrom geteilt durch Taktfrequenz mal Pumpkapazität, 1 mA durch 10 kHz mal 1 µF, also um 0,1 V: von 8,8 auf 8,7 V am Ende von Takt 2.
:::

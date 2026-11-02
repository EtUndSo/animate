---
title: Stufe 1: Rauschen
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Der Operationsverstärker
order: 1210300
summary: Ein Sensor liefert Millivolt, und jeder Leiter erzeugt eine zufällige Störspannung.
tags: Rauschspannungsdichte, Signal-Rausch-Verhältnis, Dezibel, Boltzmann-Konstante, Thermisches Rauschen, Schrotrauschen, 1/f-Rauschen, weißes Rauschen
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Ein Sensor liefert Millivolt, und jeder Leiter erzeugt eine zufällige Störspannung. Diese Stufe klärt, woher sie kommt, wie man sie misst und was ein Verstärker dagegen tun kann.
:::

**Die Idee.** Rauschen ist eine Störgröße aus vielen Schwingungen verschiedener Frequenz und Amplitude. Sein Verlauf ist zufällig und lässt sich nur statistisch beschreiben: Der Mittelwert ist null, die Stärke misst der Effektivwert. Weil unabhängige Störungen sich mal verstärken und mal aufheben, addieren sich nicht ihre Effektivwerte, sondern deren Quadrate. Deshalb beschreibt man Rauschen durch die __Rauschspannungsdichte__ $|u_\mathrm{r}(f)|^2$: den Beitrag jedes Frequenzstreifens von 1 Hz Breite zum Quadrat des Effektivwerts.

:::definition Definition 1.1 (Rauschen)
<span class="anker" id="satz-1-1"></span>

Der Effektivwert der Rauschspannung und die Dichte des thermischen Rauschens eines Widerstands sind

<span class="anker" id="gl-1-1"></span>
$$u_\mathrm{r,eff}=\sqrt{\int_0^\infty|u_\mathrm{r}(f)|^2\,\mathrm{d} f},\qquad |u_\mathrm{r,R}(f)|^2=4\,k_\mathrm{B}\,T\,R. \tag{1.1}$$

Das __Signal-Rausch-Verhältnis__ ist das Verhältnis der Leistungen, in __Dezibel__ (dB) geschrieben:

<span class="anker" id="gl-1-2"></span>
$$\mathrm{SNR}=\frac{P_\mathrm{s}}{P_\mathrm{r}}=\Bigl(\frac{u_\mathrm{s,eff}}{u_\mathrm{r,eff}}\Bigr)^2,\qquad \mathrm{SNR}_\mathrm{dB}=10\lg\frac{P_\mathrm{s}}{P_\mathrm{r}}=20\lg\frac{u_\mathrm{s,eff}}{u_\mathrm{r,eff}}. \tag{1.2}$$
:::

⁠**So liest man das:** $[|u_\mathrm{r}|^2]=\mathrm{V^2/Hz}$. $k_\mathrm{B}=1{,}381\cdot10^{-23}$ J/K ist die __Boltzmann-Konstante__: Sie rechnet Temperatur in mittlere thermische Energie je Teilchen um. $T$ ist die absolute Temperatur in K, $R$ der Widerstand. $\lg$ ist der Zehnerlogarithmus. 20 dB bedeuten den Faktor 10 in der Spannung und 100 in der Leistung. **Gültigkeit:** [(1.1)](#gl-1-1) rechts gilt bis weit über die Frequenzen der Elektronik hinaus.

| Art | Mechanismus | Dichte |
|---|---|---|
| __Thermisches Rauschen__ | Wärmebewegung der Ladungsträger in jedem Leiter. Zufällige Ansammlungen an den Enden ergeben eine Spannung, auch ohne Stromfluss. | konstant, $\sim T\,R$ |
| __Schrotrauschen__ | Strom besteht aus Einzelladungen, die eine Potenzialbarriere zu zufälligen Zeiten überqueren, etwa im pn-Übergang. | konstant |
| __1/f-Rauschen__ | Umladung von Oberflächenzuständen, schwankende Zahl freier Ladungsträger im Halbleiter. | $\sim1/f$, stört bis rund 10 kHz |

Konstante Dichte heißt __weißes Rauschen__, nach dem weißen Licht aus allen Farben. Das ist eine Form des Spektrums, keine Ursache. Über alle Frequenzen integriert ergäbe sie unendliche Leistung. Das ist eine Grenze des Modells: Echte Dichten fallen bei sehr hohen Frequenzen ab, und jede Schaltung hat eine endliche __Bandbreite__ $\Delta f$, den Frequenzbereich, den sie durchlässt. Für weißes Rauschen wird das Integral zu $u_\mathrm{r,eff}=\sqrt{|u_\mathrm{r}|^2\,\Delta f}$.

:::abbildung et1/k11rauschen 1
Links die Dichte eines 10-k$\Omega$-Widerstands mit 1/f-Anteil unterhalb von 1 kHz: oberhalb flach (weiß), darunter steigend. Rechts dasselbe Nutzsignal ohne Rauschen und mit Rauschen bei 20 dB, also einem Zehntel seines Effektivwerts.
:::

:::herleitung Warum sich Quadrate addieren
Für zwei unabhängige Störungen ist $(u_1+u_2)^2=u_1^2+2u_1u_2+u_2^2$. Im Mittel über die Zeit ist das Produkt $u_1u_2$ gleich oft positiv wie negativ, sein Mittelwert verschwindet. Es bleibt $u_\mathrm{ges,eff}^2=u_\mathrm{1,eff}^2+u_\mathrm{2,eff}^2$. Das Integral in [(1.1)](#gl-1-1) ist diese Summe über alle Frequenzstreifen.
:::

**Beispiel.** Der Sensorwiderstand hat $|u_\mathrm{r,R}|^2=4\cdot1{,}381\cdot10^{-23}\cdot300\cdot10^4=1{,}66\cdot10^{-16}\,\mathrm{V^2/Hz}$, in 20 kHz also $u_\mathrm{r,eff}=1{,}82$ µ V. Das Nutzsignal mit 1 mV ist 549-mal größer: $\mathrm{SNR}=54{,}8$ dB. Halbe Bandbreite senkt das Rauschen um $\sqrt2$, das sind 3 dB. **Grenzfälle:** Für $R\to0$ oder $T\to0$ verschwindet das thermische Rauschen.

**Was ein Verstärker ändert.** Er hebt Signal und anliegendes Rauschen um denselben Faktor, das SNR bleibt also gleich oder wird durch sein Eigenrauschen schlechter. Er hilft nur gegen Störungen, die *hinter* ihm dazukommen und eine feste Größe haben. Fügt die Leitung zum nächsten Gerät 100 µ V hinzu, bleiben ohne Verstärker 20,0 dB. Mit 100-facher Verstärkung am Sensor sind es $0{,}1\,\mathrm{V}/\sqrt{(182\,\mathrm{\mu\text{} V})^2+(100\,\mathrm{\mu\text{} V})^2}$, also 53,7 dB. Das zweite Mittel ist die Differenz: Eine Störung, die zwei Leitungen gleich trifft, verschwindet, wenn man nur ihren Unterschied auswertet. Das leistet Stufe [2](der-differenzverstarker.html#stufe-2).

:::aufgabe Aufgabe 1 ★★ Thermisches Rauschen
<span class="anker" id="aufg-1"></span>

(a) Wie groß ist das Rauschen von 47 k$\Omega$ in 10 kHz bei 300 K, wie groß bei 77 K? (b) Hinter 47 k$\Omega$ liegen 53 k$\Omega$ in Reihe. Addiere beide Rauschspannungen richtig und vergleiche mit einem Widerstand von 100 k$\Omega$. (c) Ein Signal von 200 µ V mit dem Rauschen aus (a) läuft über eine Leitung, die 50 µ V dazugibt. Wie groß ist das SNR ohne und mit 1000-facher Verstärkung vor der Leitung?

:::loesung
(a) $u_\mathrm{r,eff}=\sqrt{4k_\mathrm{B}\cdot300\,\mathrm{K}\cdot47\,\mathrm{k\Omega}\cdot10\,\mathrm{kHz}}=2{,}79$ µ V, bei 77 K um $\sqrt{77/300}$ kleiner: 1,41 µ V. (b) 53 k$\Omega$ ergeben 2,96 µ V. Unabhängige Störungen addieren sich quadratisch: $\sqrt{2{,}79^2+2{,}96^2}\,\mu\text{V}=4{,}07$ µ V, genau der Wert von 100 k$\Omega$. Die lineare Summe 5,75 µ V wäre falsch. (c) Ohne Verstärker: $200/\sqrt{2{,}79^2+50^2}=4{,}0$, also 12,0 dB. Mit 1000-fach: $200\,\mathrm{mV}/\sqrt{(2{,}79\,\mathrm{mV})^2+(0{,}05\,\mathrm{mV})^2}=71{,}7$, also 37,1 dB. Das ist fast das SNR am Eingang, die Leitung spielt keine Rolle mehr.
:::
:::

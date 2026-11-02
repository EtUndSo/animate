---
title: Stufe 3: Eine Fläche, viele Kennlinien
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Der Bipolartransistor
order: 1200500
summary: Datenblätter zeigen mehrere Kennlinien mit verschiedenen Achsen.
tags: Kennlinie, Schnitt, Kurvenschar, Eingangskennlinie, Steuerkennlinie, Stromsteuerkennlinie, Ausgangskennlinie, Übertragungskennlinie
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Datenblätter zeigen mehrere Kennlinien mit verschiedenen Achsen. Diese Stufe führt sie auf ein Objekt zurück.
:::

**Die Idee.** $I_\mathrm{C}$ hängt von zwei Spannungen ab. Eine Funktion von zwei Variablen ist eine Fläche, wie ein Gelände über einer Landkarte: Die Karte hat die Richtungen $U_\mathrm{BE}$ und $U_\mathrm{CE}$, die Geländehöhe ist $I_\mathrm{C}$ (Abb. [3](#abb-3)). Eine __Kennlinie__ (Zusammenhang zweier Größen, [Teil 5](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)) entsteht, wenn man eine Spannung festhält: ein __Schnitt__ durch das Gelände. Mehrere parallele Schnitte ergeben eine __Kurvenschar__. Es gibt also nicht viele Abhängigkeiten, sondern ein Gelände mit mehreren Ansichten. In Richtung $U_\mathrm{BE}$ ist es ein steiler Hang (rot), in Richtung $U_\mathrm{CE}$ eine Kante und dann eine fast waagerechte Ebene (grün).

:::abbildung et1/k10flaeche 3
Die Fläche $I_\mathrm{C}(U_\mathrm{BE},U_\mathrm{CE})$ des Rechenmodells. Rot: Schnitt bei $U_\mathrm{CE}=6$ V, exponentiell. Grün: Schnitt bei $U_\mathrm{BE}=0{,}6$ V, erst steil, dann fast waagerecht. Beide treffen sich im Arbeitspunkt.
:::

:::satz Satz 3.1 (Die Modellfläche)
<span class="anker" id="satz-3-1"></span>

Für $U_\mathrm{BE}\gg U_T$ und $U_\mathrm{CE}\ge0$ gilt im Rechenmodell

<span class="anker" id="gl-3-1"></span>
$$I_\mathrm{C}=\underbrace{I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{BE}/U_T}}_{\text{Injektion}}\cdot\underbrace{\bigl(1-\mathrm{e}^{-U_\mathrm{CE}/U_T}\bigr)}_{\text{Abholen}}\cdot\underbrace{\Bigl(1+\frac{U_\mathrm{CE}-6\,\mathrm{V}}{80\,\mathrm{V}}\Bigr)}_{\text{kleine Neigung}},\qquad I_\mathrm{B}=\frac{I_\mathrm{S}}{B}\,\mathrm{e}^{U_\mathrm{BE}/U_T}. \tag{3.1}$$
:::

⁠**So liest man das:** Der erste Faktor ist [(2.1)](warum-strom-durch-die-gesperrte-diode-fliet.html#gl-2-1). Der zweite geht gegen 1, sobald der Kollektor einige $U_T$ über dem Emitter liegt: Er zählt, wie viele Elektronen der Kollektor zurückschickt, bei $U_\mathrm{CE}=0{,}05$ V sind es 15 %, bei 0,1 V noch 2 %, bei 0,2 V nur 0,05 %. Der dritte Faktor beschreibt die leichte Zunahme mit $U_\mathrm{CE}$ (Stufe [9](tangente-statt-kurve.html#stufe-9)). $I_\mathrm{S}$ und $B$ gelten bei $U_\mathrm{CE}=6$ V. **Gültigkeit:** ein Modell für kleine und mittlere Ströme.

:::herleitung Der Faktor $1-\mathrm{e}^{-U_\mathrm{CE}/U_T}$
Der Elektronenstrom durch die Basis ist proportional zum Dichtegefälle zwischen ihren beiden Rändern. Jeder Rand folgt der Spannung an seiner Grenze: $\mathrm{e}^{U_\mathrm{BE}/U_T}$ am Emitter, $\mathrm{e}^{U_\mathrm{BC}/U_T}$ am Kollektor, mit $U_\mathrm{BC}=-U_\mathrm{CB}=U_\mathrm{BE}-U_\mathrm{CE}$ nach [(1.1)](drei-schichten-zwei-spannungen.html#gl-1-1). Also ist $I_\mathrm{C}\sim\mathrm{e}^{U_\mathrm{BE}/U_T}-\mathrm{e}^{(U_\mathrm{BE}-U_\mathrm{CE})/U_T}=\mathrm{e}^{U_\mathrm{BE}/U_T}(1-\mathrm{e}^{-U_\mathrm{CE}/U_T})$. Die Exponentialfunktion in $U_\mathrm{BE}$ und die Kante in $U_\mathrm{CE}$ sind zwei Seiten einer Differenz.
:::

:::abbildung et1/k10schnitte 4
Vier Schnitte aus Gleichung [(3.1)](#gl-3-1). Links Eingangs- und Steuerkennlinie bei $U_\mathrm{CE}=6$ V: dieselbe Form, die $I_\mathrm{B}$-Achse ist um den Faktor 200 anders geteilt. Mitte Ausgangskennlinien für $I_\mathrm{B}=5$ bis 20 µ A, gestrichelt die Grenze $U_\mathrm{CE}=U_\mathrm{BE}$. Rechts Stromsteuerkennlinie mit Steigung $B$.
:::

| Kennlinie | festgehalten | Achsen | Form und Grund |
|---|---|---|---|
| __Eingangskennlinie__ | $U_\mathrm{CE}$ | $I_\mathrm{B}$ über $U_\mathrm{BE}$ | Diode, Knick um 0,6 V: Die BE-Grenze ist eine Diode |
| __Steuerkennlinie__ | $U_\mathrm{CE}$ | $I_\mathrm{C}$ über $U_\mathrm{BE}$ | Gleiche Form, $B$-mal höher: Injektion |
| __Stromsteuerkennlinie__ | $U_\mathrm{CE}$ | $I_\mathrm{C}$ über $I_\mathrm{B}$ | Gerade mit Steigung $B$: Die e-Funktion kürzt sich heraus |
| __Ausgangskennlinie__ | $U_\mathrm{BE}$ oder $I_\mathrm{B}$ | $I_\mathrm{C}$ über $U_\mathrm{CE}$ | Steil, dann fast flach wie eine Stromquelle: Abholen |

Die Stromsteuerkennlinie heißt auch __Übertragungskennlinie__. Bei sehr großen Strömen flacht sie ab, $B$ sinkt: Die Basis ist dann so voll von Elektronen, dass die einfache Rechnung nicht mehr gilt. Die Grenze $U_\mathrm{CE}=U_\mathrm{BE}$ in Abb. [4](#abb-4) ist der Ort $U_\mathrm{CB}=0$. Links davon leitet die CB-Diode bereits schwach, die Kurve knickt aber erst unter rund 0,2 V ein.

**Beispiel.** Schnitt bei $U_\mathrm{CE}=6$ V: 0,582 V, 0,600 V und 0,618 V ergeben 1,0 mA, 2,0 mA und 4,0 mA. Schnitt bei $U_\mathrm{BE}=0{,}6$ V: $U_\mathrm{CE}=0{,}05$ V; 0,2 V; 6 V; 14 V ergeben 1,58 mA; 1,85 mA; 2,00 mA; 2,20 mA. **Grenzfall:** Für $U_\mathrm{CE}=0$ ist $I_\mathrm{C}=0$: Beide Ränder der Basis liegen gleich hoch, es gibt kein Gefälle.

:::frage Hängt der Strom jetzt von $U_\mathrm{CE}$ ab oder nicht?
Ja, aber verschieden stark. Bis 0,2 V stark, danach um rund 1 % je Volt. Zum Vergleich: 1 mV an $U_\mathrm{BE}$ wirkt 3,9 %. „Hängt ab“ heißt nicht „hängt gleich stark ab“. Das Gelände hat in beiden Richtungen eine Steigung, nur sind sie sehr verschieden.
:::

:::ltspice Das Ausgangskennlinienfeld
⁠**Zeichnen:** `npn` mit dem Modellnamen `T`, Emitter an Masse, am Kollektor `voltage` namens `VCE`, an der Basis `current` mit `{IB0}` von Masse zur Basis.

⁠**Direktiven:** `.model T NPN(IS=1.55e-13 BF=186 VAF=74)`, `.param IB0=10u`, `.step param IB0 list 5u 10u 15u 20u`, `.dc VCE 0 12 0.02`. Diese Parameter ergeben bei 6 V und 27 °C die Werte von T, denn LTspice zählt $B$ und $I_\mathrm{S}$ bei $U_\mathrm{CB}=0$.

⁠**Was du siehst:** Vier Kurven in `Ic(Q1)`, steil bis 0,2 V, dann leicht ansteigend. Bei $I_\mathrm{B}=10$ µ A zeigt LTspice bei 6 V 1,996 mA und bei 12 V 2,147 mA, die Rechnung ergibt 2,00 mA und 2,15 mA. Vergleiche mit Aufgabe [3](#aufg-3).
:::

:::aufgabe Aufgabe 3 ★ Schnitte lesen
<span class="anker" id="aufg-3"></span>

(a) Bestimme aus [(3.1)](#gl-3-1) $I_\mathrm{C}$ bei $U_\mathrm{BE}=0{,}6$ V für $U_\mathrm{CE}=0{,}1$ V und 12 V. Welche Kennlinie berechnest du? (b) Bestimme $I_\mathrm{C}$ bei $U_\mathrm{CE}=6$ V für $U_\mathrm{BE}=0{,}56$ V und 0,62 V. Welche Kennlinie ist das? (c) Sage vorher: Wie sieht die Kurve $I_\mathrm{C}(I_\mathrm{B})$ bei $U_\mathrm{CE}=0{,}05$ V aus, verglichen mit der bei 6 V?

:::loesung
(a) $1{,}81$ mA und $2{,}15$ mA, ein Schnitt bei festem $U_\mathrm{BE}$: Ausgangskennlinie. (b) 0,43 mA und 4,32 mA, ein Schnitt bei festem $U_\mathrm{CE}$: Steuerkennlinie. 60 mV machen den Faktor 10. (c) Wieder eine Gerade durch den Ursprung, nur flacher. $I_\mathrm{B}$ hängt in [(3.1)](#gl-3-1) nicht von $U_\mathrm{CE}$ ab, die beiden anderen Faktoren sind bei festem $U_\mathrm{CE}$ Konstanten: $0{,}854\cdot0{,}926=0{,}79$, die Steigung ist 158 statt 200.
:::
:::

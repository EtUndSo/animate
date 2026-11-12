---
title: Stufe 3: Eine Fläche, viele Kennlinien
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Der Bipolartransistor
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor
knoten: Kapitel 10: Der Bipolartransistor
order: 1200500
summary: Datenblätter zeigen mehrere Kennlinien mit verschiedenen Achsen.
tags: Kennlinie, Schnitt, Kurvenschar, Eingangskennlinie, Steuerkennlinie, Stromsteuerkennlinie, Ausgangskennlinie, Übertragungskennlinie
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Datenblätter zeigen mehrere Kennlinien mit verschiedenen Achsen. Diese Stufe führt sie auf ein Objekt zurück.
:::

**Die Idee.** $I_\mathrm{C}$ hängt von zwei Spannungen ab. Eine Funktion von zwei Variablen ist eine Fläche, wie ein Gelände über einer Landkarte: Die Karte hat die Richtungen $U_\mathrm{BE}$ und $U_\mathrm{CE}$, die Geländehöhe ist $I_\mathrm{C}$ (Abb. [3](#abb-3)). Eine __Kennlinie__ (Zusammenhang zweier Größen, [Kapitel 5](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)) entsteht, wenn man eine Spannung festhält: ein __Schnitt__ durch das Gelände. Mehrere parallele Schnitte ergeben eine __Kurvenschar__. Es gibt also nicht viele Abhängigkeiten, sondern ein Gelände mit mehreren Ansichten. In Richtung $U_\mathrm{BE}$ ist es ein steiler Hang (rot), in Richtung $U_\mathrm{CE}$ eine Kante und dann eine fast waagerechte Ebene (grün).

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

::::beispiel
Schnitt bei $U_\mathrm{CE}=6$ V: 0,582 V, 0,600 V und 0,618 V ergeben 1,0 mA, 2,0 mA und 4,0 mA. Schnitt bei $U_\mathrm{BE}=0{,}6$ V: $U_\mathrm{CE}=0{,}05$ V; 0,2 V; 6 V; 14 V ergeben 1,58 mA; 1,85 mA; 2,00 mA; 2,20 mA.
::::

⁠**Grenzfall:** Für $U_\mathrm{CE}=0$ ist $I_\mathrm{C}=0$: Beide Ränder der Basis liegen gleich hoch, es gibt kein Gefälle.

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

::::formelsammlung
**Modellfläche**

$$I_\mathrm{C}=I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{BE}/U_T}\cdot\bigl(1-\mathrm{e}^{-U_\mathrm{CE}/U_T}\bigr)\cdot\Bigl(1+\frac{U_\mathrm{CE}-6\,\mathrm{V}}{80\,\mathrm{V}}\Bigr)$$

Rechenmodell für $U_\mathrm{BE}\gg U_T$ und $U_\mathrm{CE}\ge0$, kleine und mittlere Ströme; $I_\mathrm{S}$ und $B$ gelten bei $U_\mathrm{CE}=6$ V. Die Faktoren beschreiben Injektion, Abholen und eine kleine Neigung von rund 1 % je Volt. Der zweite geht gegen 1, sobald der Kollektor einige $U_T$ über dem Emitter liegt; für $U_\mathrm{CE}=0$ ist $I_\mathrm{C}=0$.

**Basisstrom in der Modellfläche**

$$I_\mathrm{B}=\frac{I_\mathrm{S}}{B}\,\mathrm{e}^{U_\mathrm{BE}/U_T}$$

Hängt nicht von $U_\mathrm{CE}$ ab. Die Eingangskennlinie hat deshalb die Form einer Diodenkennlinie, die Stromsteuerkennlinie ist eine Gerade mit der Steigung $B$.
::::

::::lernkarten
:::karte zusammenhang Kennlinie
Warum zeigen Datenblätter mehrere Kennlinien eines Transistors, obwohl $I_\mathrm{C}$ nur durch eine Abhängigkeit bestimmt ist?
---
$I_\mathrm{C}$ hängt von zwei Spannungen ab und ist eine Fläche, wie ein Gelände über einer Landkarte. Jede Kennlinie ist ein Schnitt durch dieses eine Gelände: ein Objekt mit mehreren Ansichten.
--- falsch
Jeder Anschluss des Transistors hat seine eigene, unabhängige Abhängigkeit. Die Kennlinien beschreiben deshalb verschiedene Vorgänge im Bauteil, die man getrennt messen und berechnen muss.
--- falsch
$I_\mathrm{C}$ hängt nur von $U_\mathrm{BE}$ ab, die übrigen Kennlinien zeigen Messfehler bei verschiedenen Temperaturen. Sie sind Kopien derselben Kurve unter anderen Bedingungen.
--- falsch
Jede Kennlinie gilt für einen anderen Transistortyp derselben Reihe. Das Datenblatt fasst so mehrere Bauteile zusammen, die sich nur in der Stromverstärkung unterscheiden.
:::
:::karte begriff Schnitt und Kurvenschar
Wie entsteht aus der Fläche $I_\mathrm{C}(U_\mathrm{BE},U_\mathrm{CE})$ ein Schnitt, und wie eine Kurvenschar?
---
Ein Schnitt entsteht, wenn man eine der beiden Spannungen festhält; er ist eine Kennlinie durch das Gelände. Mehrere parallele Schnitte bei verschiedenen festen Werten bilden eine Kurvenschar.
--- falsch
Ein Schnitt entsteht, wenn man beide Spannungen festhält; er ist ein einzelner Punkt der Fläche. Eine Kurvenschar ist die Verbindung mehrerer solcher Punkte zu einer Kennlinie.
--- falsch
Ein Schnitt entsteht, wenn man $I_\mathrm{C}$ festhält; er ist eine Höhenlinie des Geländes. Eine Kurvenschar ist das Bündel aller Höhenlinien, gezeichnet über $U_\mathrm{BE}$.
--- falsch
Ein Schnitt ist die Kennlinie bei $U_\mathrm{CE}=0$, an der die Fläche beginnt. Eine Kurvenschar entsteht, wenn man diese Kennlinie für verschiedene Transistoren desselben Typs übereinanderzeichnet.
:::
:::karte formel Modellfläche
Wie lautet die Modellfläche für $I_\mathrm{C}$ im Rechenmodell, und was beschreiben ihre drei Faktoren?
---
$I_\mathrm{C}=I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{BE}/U_T}\cdot\bigl(1-\mathrm{e}^{-U_\mathrm{CE}/U_T}\bigr)\cdot\Bigl(1+\frac{U_\mathrm{CE}-6\,\mathrm{V}}{80\,\mathrm{V}}\Bigr)$: Injektion, Abholen und kleine Neigung mit $U_\mathrm{CE}$. Gültig für $U_\mathrm{BE}\gg U_T$ und $U_\mathrm{CE}\ge0$.
--- falsch
$I_\mathrm{C}=I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{BE}/U_T}\cdot\bigl(1-\mathrm{e}^{-U_\mathrm{BE}/U_T}\bigr)\cdot\Bigl(1+\frac{U_\mathrm{CE}-6\,\mathrm{V}}{80\,\mathrm{V}}\Bigr)$: Injektion, Rekombination und Neigung. Gültig für $U_\mathrm{BE}\gg U_T$ und jedes $U_\mathrm{CE}$.
--- falsch
$I_\mathrm{C}=I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{CE}/U_T}\cdot\bigl(1-\mathrm{e}^{-U_\mathrm{BE}/U_T}\bigr)\cdot\Bigl(1+\frac{U_\mathrm{BE}-6\,\mathrm{V}}{80\,\mathrm{V}}\Bigr)$: Abholen, Injektion und Neigung. Gültig für $U_\mathrm{CE}\gg U_T$ und $U_\mathrm{BE}\ge0$.
--- falsch
$I_\mathrm{C}=I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{BE}/U_T}+\bigl(1-\mathrm{e}^{-U_\mathrm{CE}/U_T}\bigr)+\frac{U_\mathrm{CE}-6\,\mathrm{V}}{80\,\mathrm{V}}$: Injektion, Abholen und Neigung addieren sich. Gültig für $U_\mathrm{BE}\gg U_T$ und $U_\mathrm{CE}\ge0$.
:::
:::karte herleitung Faktor des Abholens
Wie folgt aus dem Dichtegefälle in der Basis, dass $I_\mathrm{C}$ den Faktor $1-\mathrm{e}^{-U_\mathrm{CE}/U_T}$ enthält?
---
Der Elektronenstrom durch die Basis ist proportional zum Dichtegefälle zwischen ihren beiden Rändern, weil die Elektronen dort vom dichten zum dünnen Ort diffundieren.
---
Der Emitterrand folgt $\mathrm{e}^{U_\mathrm{BE}/U_T}$, der Kollektorrand $\mathrm{e}^{U_\mathrm{BC}/U_T}$, weil jeder Rand der Spannung an seiner Grenze folgt.
---
Dabei ist $U_\mathrm{BC}=-U_\mathrm{CB}=U_\mathrm{BE}-U_\mathrm{CE}$, weil nach der Maschenregel $U_\mathrm{CE}=U_\mathrm{CB}+U_\mathrm{BE}$ gilt.
---
Also ist $I_\mathrm{C}\sim\mathrm{e}^{U_\mathrm{BE}/U_T}-\mathrm{e}^{(U_\mathrm{BE}-U_\mathrm{CE})/U_T}=\mathrm{e}^{U_\mathrm{BE}/U_T}(1-\mathrm{e}^{-U_\mathrm{CE}/U_T})$, weil man den gemeinsamen Faktor $\mathrm{e}^{U_\mathrm{BE}/U_T}$ ausklammern kann.
:::
:::karte zusammenhang Kein Strom ohne Kollektor-Emitter-Spannung
Warum ist im Modell $I_\mathrm{C}=0$, wenn $U_\mathrm{CE}=0$ ist?
---
Dann liegen beide Ränder der Basis gleich hoch, und es gibt kein Dichtegefälle, das Elektronen zum Kollektor treibt. Der Faktor $1-\mathrm{e}^{-U_\mathrm{CE}/U_T}$ wird null.
--- falsch
Dann sperrt die BE-Diode, weil Basis und Emitter dasselbe Potenzial haben. Ohne Injektion gelangen keine Elektronen in die Basis, und der erste Faktor wird null.
--- falsch
Dann ist die Raumladungszone der CB-Grenze verschwunden, und die Elektronen rekombinieren alle in der Basis. Der Faktor der kleinen Neigung wird deshalb null.
--- falsch
Dann fließt der ganze Emitterstrom über die Basis ab, weil sie das höchste Potenzial hat. Im Modell ist $I_\mathrm{C}$ deshalb nicht null, sondern gleich $-I_\mathrm{B}$.
:::
:::karte zusammenhang Zurückgeschickte Elektronen
Welchen Anteil der Elektronen schickt der Kollektor bei $U_\mathrm{CE}=0{,}05$ V, 0,1 V und 0,2 V zurück, und was folgt daraus für das Abholen?
---
15 %, 2 % und 0,05 %. Der Faktor $1-\mathrm{e}^{-U_\mathrm{CE}/U_T}$ geht also gegen 1, sobald der Kollektor einige $U_T$ über dem Emitter liegt: Dann holt er fast alle ab.
--- falsch
85 %, 98 % und 99,95 %. Je höher $U_\mathrm{CE}$, desto mehr Elektronen stößt das Feld zurück, und der Kollektorstrom sinkt mit steigender Spannung deutlich.
--- falsch
15 %, 10 % und 5 %. Der Anteil sinkt linear mit $U_\mathrm{CE}$, und der Kollektor holt erst bei rund 1 V alle Elektronen ab.
--- falsch
Bei allen drei Spannungen keinen, weil die CB-Diode schon ab 0 V sperrt. Der Faktor des Abholens ist deshalb für jedes $U_\mathrm{CE}\ge0$ genau 1.
:::
:::karte zusammenhang Eingangskennlinie
Warum hat die Eingangskennlinie $I_\mathrm{B}$ über $U_\mathrm{BE}$ die Form einer Diodenkennlinie mit Knick um 0,6 V?
---
Weil die BE-Grenze eine Diode ist: $I_\mathrm{B}=\frac{I_\mathrm{S}}{B}\,\mathrm{e}^{U_\mathrm{BE}/U_T}$ wächst exponentiell mit $U_\mathrm{BE}$. Festgehalten wird dabei $U_\mathrm{CE}$.
--- falsch
Weil die CB-Grenze eine Diode ist: Der Basisstrom ist ihr Sperrstrom und wächst exponentiell mit $U_\mathrm{CE}$. Festgehalten wird dabei $U_\mathrm{BE}$.
--- falsch
Weil der Basisanschluss einen Widerstand enthält, der erst ab 0,6 V durchbricht. Darunter fließt kein Strom, darüber wächst er linear mit $U_\mathrm{BE}$.
--- falsch
Weil die BE-Grenze eine Diode ist, deren Strom $I_\mathrm{B}=B\,I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{BE}/U_T}$ $B$-mal größer ist als der Kollektorstrom. Festgehalten wird dabei $I_\mathrm{C}$.
:::
:::karte begriff Steuerkennlinie
Was zeigt die Steuerkennlinie eines Transistors, und wie unterscheidet sie sich von der Eingangskennlinie?
---
Die Kennlinie $I_\mathrm{C}$ über $U_\mathrm{BE}$ bei festem $U_\mathrm{CE}$. Sie hat dieselbe exponentielle Form wie die Eingangskennlinie, liegt aber $B$-mal höher, weil sie die Injektion zeigt.
--- falsch
Die Kennlinie $I_\mathrm{C}$ über $U_\mathrm{CE}$ bei festem $U_\mathrm{BE}$. Sie steigt erst steil, dann fast waagerecht und hat deshalb eine ganz andere Form als die Eingangskennlinie.
--- falsch
Die Kennlinie $I_\mathrm{C}$ über $U_\mathrm{BE}$ bei festem $U_\mathrm{CE}$. Sie hat dieselbe Form wie die Eingangskennlinie, liegt aber $B$-mal tiefer, weil nur ein Teil der Elektronen ankommt.
--- falsch
Die Kennlinie $I_\mathrm{B}$ über $I_\mathrm{C}$ bei festem $U_\mathrm{CE}$. Sie ist eine Gerade mit der Steigung $1/B$ und zeigt, wie viel Basisstrom ein Kollektorstrom braucht.
:::
:::karte begriff Stromsteuerkennlinie
Was zeigt die Stromsteuerkennlinie eines Transistors, und warum ist sie eine Gerade?
---
Die Kennlinie $I_\mathrm{C}$ über $I_\mathrm{B}$ bei festem $U_\mathrm{CE}$. Sie ist eine Gerade durch den Ursprung mit der Steigung $B$, weil sich die e-Funktion aus beiden Strömen herauskürzt.
--- falsch
Die Kennlinie $I_\mathrm{C}$ über $U_\mathrm{BE}$ bei festem $U_\mathrm{CE}$. Sie ist eine Gerade, weil der Transistor im aktiven Bereich linear arbeitet; ihre Steigung ist dort $B$.
--- falsch
Die Kennlinie $I_\mathrm{C}$ über $I_\mathrm{B}$ bei festem $U_\mathrm{BE}$. Sie ist eine Gerade, weil $I_\mathrm{B}$ dann konstant ist, und steht deshalb senkrecht im Diagramm.
--- falsch
Die Kennlinie $I_\mathrm{B}$ über $U_\mathrm{CE}$ bei festem $I_\mathrm{C}$. Sie ist eine waagerechte Gerade, weil der Basisstrom nicht von der Kollektorspannung abhängt, sondern nur von $I_\mathrm{C}$.
:::
:::karte zusammenhang Übertragungskennlinie
Was passiert mit der Übertragungskennlinie $I_\mathrm{C}(I_\mathrm{B})$ bei sehr großen Strömen, und warum?
---
Sie flacht ab, $B$ sinkt: Die Basis ist dann so voll von Elektronen, dass die einfache Rechnung nicht mehr gilt.
--- falsch
Sie wird steiler, $B$ steigt: Bei großen Strömen saugt das Feld der CB-Grenze stärker, und mehr Elektronen erreichen den Kollektor.
--- falsch
Sie bleibt eine Gerade mit Steigung $B$, weil sich die e-Funktion bei jedem Strom herauskürzt. Erst die Leistungsgrenze beendet sie.
--- falsch
Sie knickt senkrecht nach oben ab, weil die BE-Diode bei großen Strömen durchbricht und der Basisstrom dann keine Rolle mehr spielt.
:::
:::karte zusammenhang Ausgangskennlinie
Warum verläuft die Ausgangskennlinie $I_\mathrm{C}$ über $U_\mathrm{CE}$ erst steil und ab etwa 0,2 V fast flach?
---
Bei kleinem $U_\mathrm{CE}$ schickt der Kollektor noch Elektronen zurück, der Faktor des Abholens ist kleiner als 1. Ab etwa 0,2 V holt er fast alle ab, und $I_\mathrm{C}$ wächst nur noch um rund 1 % je Volt.
--- falsch
Bei kleinem $U_\mathrm{CE}$ wirkt der Transistor wie ein Widerstand, ab 0,2 V wie ein Kurzschluss. Der Strom ist dann durch den Kollektorwiderstand begrenzt und bleibt deshalb konstant, gleich wie groß $U_\mathrm{CE}$ wird.
--- falsch
Bei kleinem $U_\mathrm{CE}$ ist die BE-Diode noch gesperrt und öffnet erst langsam. Ab 0,2 V leitet sie voll, und der Strom hängt danach überhaupt nicht mehr von $U_\mathrm{CE}$ ab.
--- falsch
Bei kleinem $U_\mathrm{CE}$ rekombinieren fast alle Elektronen in der Basis. Ab 0,2 V ist die Basis mit Elektronen gesättigt, deshalb kann der Strom nicht weiter wachsen.
:::
:::karte zusammenhang Zwei verschieden steile Richtungen
Wie stark hängt $I_\mathrm{C}$ oberhalb von 0,2 V von $U_\mathrm{CE}$ ab, verglichen mit der Abhängigkeit von $U_\mathrm{BE}$?
---
Um rund 1 % je Volt $U_\mathrm{CE}$, aber um 3,9 % je Millivolt $U_\mathrm{BE}$. Das Gelände steigt in beiden Richtungen, nur sehr verschieden stark.
--- falsch
Gar nicht: Oberhalb von 0,2 V ist die Fläche in Richtung $U_\mathrm{CE}$ exakt waagerecht. Nur $U_\mathrm{BE}$ verändert dort noch den Strom, dann aber stark.
--- falsch
Etwa gleich stark: rund 4 % je Volt in beiden Richtungen. Die Fläche ist deshalb eine schräge Ebene ohne bevorzugte Richtung.
--- falsch
Um rund 10 % je Volt $U_\mathrm{CE}$, dagegen um 1 % je Volt $U_\mathrm{BE}$. Die Ausgangsspannung wirkt also stärker als die Steuerspannung selbst.
:::
:::karte zusammenhang Grenze im Ausgangskennlinienfeld
Was bedeutet die Grenze $U_\mathrm{CE}=U_\mathrm{BE}$ im Ausgangskennlinienfeld, und was geschieht links davon?
---
Sie ist der Ort $U_\mathrm{CB}=0$. Links davon leitet die CB-Diode bereits schwach, die Kurve knickt aber erst unter rund 0,2 V ein.
--- falsch
Sie ist der Ort $U_\mathrm{BE}=0$. Links davon sperrt die BE-Diode, und der Kollektorstrom fällt dort sofort auf null.
--- falsch
Sie ist der Ort $U_\mathrm{CB}=0$. Links davon sperren beide Dioden, und die Kurve bricht genau an dieser Grenze senkrecht ab.
--- falsch
Sie ist die Leistungsgrenze des Transistors. Links davon wird das Bauteil zu heiß, und die Kurven dürfen dort nicht benutzt werden.
:::
::::

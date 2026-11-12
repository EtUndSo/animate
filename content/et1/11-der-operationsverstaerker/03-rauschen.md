---
title: Stufe 1: Rauschen
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Der Operationsverstärker
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-operationsverstarker
knoten: Kapitel 11: Der Operationsverstärker
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

::::beispiel
Der Sensorwiderstand hat $|u_\mathrm{r,R}|^2=4\cdot1{,}381\cdot10^{-23}\cdot300\cdot10^4=1{,}66\cdot10^{-16}\,\mathrm{V^2/Hz}$, in 20 kHz also $u_\mathrm{r,eff}=1{,}82$ µ V. Das Nutzsignal mit 1 mV ist 549-mal größer: $\mathrm{SNR}=54{,}8$ dB. Halbe Bandbreite senkt das Rauschen um $\sqrt2$, das sind 3 dB.
::::

⁠**Grenzfälle:** Für $R\to0$ oder $T\to0$ verschwindet das thermische Rauschen.

**Was ein Verstärker ändert.** Er hebt Signal und anliegendes Rauschen um denselben Faktor, das SNR bleibt also gleich oder wird durch sein Eigenrauschen schlechter. Er hilft nur gegen Störungen, die *hinter* ihm dazukommen und eine feste Größe haben. Fügt die Leitung zum nächsten Gerät 100 µ V hinzu, bleiben ohne Verstärker 20,0 dB. Mit 100-facher Verstärkung am Sensor sind es $0{,}1\,\mathrm{V}/\sqrt{(182\,\mathrm{\mu\text{} V})^2+(100\,\mathrm{\mu\text{} V})^2}$, also 53,7 dB. Das zweite Mittel ist die Differenz: Eine Störung, die zwei Leitungen gleich trifft, verschwindet, wenn man nur ihren Unterschied auswertet. Das leistet Stufe [2](der-differenzverstarker.html#stufe-2).

:::aufgabe Aufgabe 1 ★★ Thermisches Rauschen
<span class="anker" id="aufg-1"></span>

(a) Wie groß ist das Rauschen von 47 k$\Omega$ in 10 kHz bei 300 K, wie groß bei 77 K? (b) Hinter 47 k$\Omega$ liegen 53 k$\Omega$ in Reihe. Addiere beide Rauschspannungen richtig und vergleiche mit einem Widerstand von 100 k$\Omega$. (c) Ein Signal von 200 µ V mit dem Rauschen aus (a) läuft über eine Leitung, die 50 µ V dazugibt. Wie groß ist das SNR ohne und mit 1000-facher Verstärkung vor der Leitung?

:::loesung
(a) $u_\mathrm{r,eff}=\sqrt{4k_\mathrm{B}\cdot300\,\mathrm{K}\cdot47\,\mathrm{k\Omega}\cdot10\,\mathrm{kHz}}=2{,}79$ µ V, bei 77 K um $\sqrt{77/300}$ kleiner: 1,41 µ V. (b) 53 k$\Omega$ ergeben 2,96 µ V. Unabhängige Störungen addieren sich quadratisch: $\sqrt{2{,}79^2+2{,}96^2}\,\mu\text{V}=4{,}07$ µ V, genau der Wert von 100 k$\Omega$. Die lineare Summe 5,75 µ V wäre falsch. (c) Ohne Verstärker: $200/\sqrt{2{,}79^2+50^2}=4{,}0$, also 12,0 dB. Mit 1000-fach: $200\,\mathrm{mV}/\sqrt{(2{,}79\,\mathrm{mV})^2+(0{,}05\,\mathrm{mV})^2}=71{,}7$, also 37,1 dB. Das ist fast das SNR am Eingang, die Leitung spielt keine Rolle mehr.
:::
:::

::::formelsammlung
**Effektivwert der Rauschspannung**

$$u_\mathrm{r,eff}=\sqrt{\int_0^\infty|u_\mathrm{r}(f)|^2\,\mathrm{d} f}$$

$|u_\mathrm{r}(f)|^2$ ist die Rauschspannungsdichte in $\mathrm{V^2/Hz}$: der Beitrag jedes Frequenzstreifens von 1 Hz Breite zum Quadrat des Effektivwerts.

**Thermisches Rauschen eines Widerstands**

$$|u_\mathrm{r,R}(f)|^2=4\,k_\mathrm{B}\,T\,R$$

Konstante (weiße) Dichte; $k_\mathrm{B}=1{,}381\cdot10^{-23}$ J/K ist die Boltzmann-Konstante, $T$ die absolute Temperatur in K, $R$ der Widerstand. Gilt bis weit über die Frequenzen der Elektronik hinaus.

**Weißes Rauschen in der Bandbreite**

$$u_\mathrm{r,eff}=\sqrt{|u_\mathrm{r}|^2\,\Delta f}$$

Für konstante Dichte und eine Schaltung, die den Frequenzbereich $\Delta f$ durchlässt.

**Unabhängige Störungen**

$$u_\mathrm{ges,eff}^2=u_\mathrm{1,eff}^2+u_\mathrm{2,eff}^2$$

Es addieren sich die Quadrate der Effektivwerte, nicht die Effektivwerte selbst.

**Signal-Rausch-Verhältnis**

$$\mathrm{SNR}=\frac{P_\mathrm{s}}{P_\mathrm{r}}=\Bigl(\frac{u_\mathrm{s,eff}}{u_\mathrm{r,eff}}\Bigr)^2$$

Verhältnis von Signalleistung zu Rauschleistung.

**Signal-Rausch-Verhältnis in Dezibel**

$$\mathrm{SNR}_\mathrm{dB}=10\lg\frac{P_\mathrm{s}}{P_\mathrm{r}}=20\lg\frac{u_\mathrm{s,eff}}{u_\mathrm{r,eff}}$$

$\lg$ ist der Zehnerlogarithmus. 20 dB bedeuten den Faktor 10 in der Spannung und 100 in der Leistung.
::::

::::lernkarten
:::karte begriff Rauschen
Was versteht man unter Rauschen in einer elektronischen Schaltung, und womit misst man seine Stärke?
---
Eine zufällige Störgröße aus vielen Schwingungen verschiedener Frequenz und Amplitude. Ihr Verlauf lässt sich nur statistisch beschreiben: Der Mittelwert ist null, die Stärke misst der Effektivwert.
--- falsch
Eine periodische Störspannung mit fester Frequenz, meist der des Stromnetzes. Ihr Verlauf ist vorhersagbar, die Stärke misst man an der Amplitude dieser einen Schwingung.
--- falsch
Eine zufällige Störgröße aus vielen Schwingungen verschiedener Frequenz. Ihr Mittelwert ist positiv und gleich der Störung, deshalb misst man die Stärke mit dem Mittelwert.
--- falsch
Eine Störspannung, die nur in übersteuerten Verstärkern entsteht. Bei kleinen Signalen und ohne Verstärker gibt es kein Rauschen, nur feste Fehler der Leitungen.
:::
:::karte begriff Rauschspannungsdichte
Was gibt die Rauschspannungsdichte $|u_\mathrm{r}(f)|^2$ an, und warum beschreibt man Rauschen gerade durch Quadrate?
---
Den Beitrag jedes Frequenzstreifens von 1 Hz Breite zum Quadrat des Effektivwerts, in $\mathrm{V^2/Hz}$. Unabhängige Störungen addieren sich nicht in ihren Effektivwerten, sondern in deren Quadraten.
--- falsch
Den Effektivwert der Rauschspannung in einem Streifen von 1 Hz Breite, in V/Hz. Quadrate braucht man nur, weil die Leistung an einem Widerstand mit $u^2$ wächst.
--- falsch
Die Rauschspannung je Ohm Widerstand, gemittelt über alle Frequenzen, in V$^2/\Omega$. Die Quadrate entstehen, weil Widerstand und Spannung beide eingehen.
--- falsch
Den Beitrag jedes Streifens von 1 Hz Breite zum Effektivwert selbst, in V/Hz. Unabhängige Störungen addieren sich nämlich direkt in ihren Effektivwerten.
:::
:::karte formel Effektivwert der Rauschspannung
Wie berechnet man den Effektivwert der Rauschspannung aus der Rauschspannungsdichte, und warum steht dabei eine Wurzel?
---
$u_\mathrm{r,eff}=\sqrt{\int_0^\infty|u_\mathrm{r}(f)|^2\,\mathrm{d} f}$. Die Dichte liefert Quadrate des Effektivwerts, die sich über alle Streifen addieren; die Wurzel macht daraus wieder eine Spannung.
--- falsch
$u_\mathrm{r,eff}=\int_0^\infty|u_\mathrm{r}(f)|\,\mathrm{d} f$, ohne Wurzel: Die Effektivwerte der Frequenzstreifen addieren sich direkt, weil jede Schwingung unabhängig von den anderen ihren vollen Betrag beiträgt.
--- falsch
$u_\mathrm{r,eff}=\sqrt{\int_0^\infty|u_\mathrm{r}(f)|^2\,\mathrm{d} f}$, aber nur für weißes Rauschen; beim 1/f-Rauschen addieren sich die Effektivwerte der Streifen direkt und ohne Wurzel.
--- falsch
$u_\mathrm{r,eff}=\bigl(\int_0^\infty|u_\mathrm{r}(f)|^2\,\mathrm{d} f\bigr)^2$: Die Dichte ist schon die Wurzel einer Leistung, deshalb muss man das Integral noch einmal quadrieren.
:::
:::karte begriff Thermisches Rauschen
Wodurch entsteht thermisches Rauschen in einem Leiter, und wie groß ist seine Dichte?
---
Durch die Wärmebewegung der Ladungsträger: Zufällige Ansammlungen an den Enden ergeben eine Spannung, auch ohne Stromfluss. Die Dichte ist konstant, $|u_\mathrm{r,R}(f)|^2=4\,k_\mathrm{B}\,T\,R$.
--- falsch
Durch den Strom, der durch den Leiter fließt; ohne Stromfluss rauscht ein Widerstand nicht. Die Dichte ist konstant, $|u_\mathrm{r,R}(f)|^2=4\,k_\mathrm{B}\,T\,R$.
--- falsch
Durch Umladung von Oberflächenzuständen im Leiter. Die Dichte fällt mit $1/f$, deshalb stört es nur unterhalb von rund 10 kHz und verschwindet bei hohen Frequenzen.
--- falsch
Durch Ladungen, die eine Potenzialbarriere zu zufälligen Zeiten überqueren. Die Dichte ist $4\,k_\mathrm{B}\,T/R$, sie sinkt also mit wachsendem Widerstand und steigt mit der Temperatur.
:::
:::karte formel Rauschen in der Bandbreite
Wie groß ist der Effektivwert der Rauschspannung eines Widerstands $R$ bei der Temperatur $T$ in einer Schaltung mit der Bandbreite $\Delta f$?
---
$u_\mathrm{r,eff}=\sqrt{|u_\mathrm{r}|^2\,\Delta f}$ mit der konstanten Dichte $|u_\mathrm{r,R}(f)|^2=4\,k_\mathrm{B}\,T\,R$. Halbe Bandbreite senkt das Rauschen um $\sqrt2$, also um 3 dB.
--- falsch
$u_\mathrm{r,eff}=|u_\mathrm{r}|^2\,\Delta f$ mit $|u_\mathrm{r,R}(f)|^2=4\,k_\mathrm{B}\,T\,R$. Das Rauschen wächst linear mit $T$, $R$ und $\Delta f$; halbe Bandbreite halbiert es, das sind 6 dB.
--- falsch
$u_\mathrm{r,eff}=\sqrt{|u_\mathrm{r}|^2/\Delta f}$ mit $|u_\mathrm{r,R}(f)|^2=4\,k_\mathrm{B}\,T\,R$. Eine größere Bandbreite verteilt das Rauschen auf mehr Frequenzen und senkt seinen Effektivwert.
--- falsch
$u_\mathrm{r,eff}=\sqrt{|u_\mathrm{r}|^2\,\Delta f}$ mit $|u_\mathrm{r,R}(f)|^2=4\,k_\mathrm{B}\,T\,R$, aber nur oberhalb von 1 M$\Omega$; kleinere Widerstände rauschen praktisch nicht.
:::
:::karte begriff Schrotrauschen
Wodurch entsteht Schrotrauschen, etwa an einem pn-Übergang, und wie hängt seine Dichte von der Frequenz ab?
---
Dadurch, dass der Strom aus Einzelladungen besteht, die eine Potenzialbarriere zu zufälligen Zeiten überqueren. Seine Dichte ist konstant über der Frequenz.
--- falsch
Durch die Wärmebewegung der Ladungsträger, die auch ohne Stromfluss eine Spannung an den Enden erzeugt. Seine Dichte ist konstant über der Frequenz und proportional zur Temperatur.
--- falsch
Durch Umladung von Oberflächenzuständen im Halbleiter. Seine Dichte fällt mit $1/f$, deshalb stört es vor allem bei tiefen Frequenzen.
--- falsch
Dadurch, dass die Einzelladungen im gleichen Takt über die Barriere laufen. Seine Dichte hat deshalb eine Spitze bei genau dieser Taktfrequenz.
:::
:::karte begriff 1/f-Rauschen
Was kennzeichnet das 1/f-Rauschen, und woher kommt es im Halbleiter?
---
Seine Dichte fällt mit $1/f$, es stört deshalb vor allem bei tiefen Frequenzen bis rund 10 kHz. Ursachen sind die Umladung von Oberflächenzuständen und eine schwankende Zahl freier Ladungsträger.
--- falsch
Seine Dichte steigt mit $f$, es stört deshalb vor allem oberhalb von rund 10 kHz. Ursache ist die Wärmebewegung der Ladungsträger, die bei hohen Frequenzen schneller wird.
--- falsch
Seine Dichte ist konstant; den Namen trägt es nach der Einheit 1/Hz der Dichte. Ursache sind Einzelladungen, die eine Potenzialbarriere zu zufälligen Zeiten überqueren.
--- falsch
Seine Dichte fällt mit $1/f$, es stört deshalb bei tiefen Frequenzen. Ursache ist allein die Temperatur; bei 0 K verschwindet es wie das thermische Rauschen.
:::
:::karte begriff weißes Rauschen
Was bedeutet die Bezeichnung weißes Rauschen, und beschreibt sie eine Ursache des Rauschens?
---
Rauschen mit konstanter Dichte über der Frequenz, benannt nach dem weißen Licht aus allen Farben. Es ist eine Form des Spektrums, keine Ursache; thermisches Rauschen und Schrotrauschen sind weiß.
--- falsch
Rauschen, das nur bei sehr hohen Frequenzen auftritt, benannt nach dem hellen Licht kurzer Wellen. Es ist eine eigene Ursache neben dem thermischen und dem Schrotrauschen und tritt in jeder Schaltung auf.
--- falsch
Rauschen mit einer Dichte, die mit $1/f$ fällt, benannt nach dem weißen Licht. Es ist eine Form des Spektrums; das 1/f-Rauschen ist das typische weiße Rauschen.
--- falsch
Rauschen mit konstanter Dichte über der Frequenz. Es ist die Ursache des thermischen Rauschens, denn die gleichmäßige Dichte versetzt die Ladungsträger in Bewegung.
:::
:::karte begriff Bandbreite
Was ist die Bandbreite einer Schaltung, und warum braucht man sie, um weißes Rauschen zu berechnen?
---
Der Frequenzbereich $\Delta f$, den die Schaltung durchlässt. Weißes Rauschen ergäbe über alle Frequenzen integriert unendliche Leistung; es zählt nur das Rauschen innerhalb der Bandbreite.
--- falsch
Die höchste Spannung, die eine Schaltung unverzerrt durchlässt. Rauschspitzen über dieser Spannung werden abgeschnitten, deshalb bleibt die Rauschleistung endlich.
--- falsch
Der Frequenzbereich, in dem eine Schaltung selbst rauscht. Außerhalb davon ist jede Dichte null, deshalb hängt das Rauschen nicht vom Durchlassbereich ab.
--- falsch
Die Breite eines einzelnen Frequenzstreifens, also 1 Hz. Mit ihr rechnet man die Dichte in eine Spannung um; die Schaltung selbst spielt dafür keine Rolle.
:::
:::karte zusammenhang Boltzmann-Konstante
Warum steht die Boltzmann-Konstante $k_\mathrm{B}$ in der Dichte $4\,k_\mathrm{B}\,T\,R$ des thermischen Rauschens?
---
Sie rechnet die Temperatur in die mittlere thermische Energie je Teilchen um. Thermisches Rauschen entsteht aus der Wärmebewegung der Ladungsträger, deshalb wächst seine Dichte mit $k_\mathrm{B}T$.
--- falsch
Sie gibt die Ladung eines einzelnen Elektrons an. Thermisches Rauschen entsteht aus Einzelladungen, die zu zufälligen Zeiten fließen, deshalb wächst die Dichte mit $k_\mathrm{B}$ und mit dem Strom durch den Leiter.
--- falsch
Sie rechnet den Widerstand in eine Erwärmung um. Ein großer Widerstand wird bei gleichem Strom wärmer und rauscht deshalb mehr, die Dichte wächst mit $k_\mathrm{B}R$.
--- falsch
Sie rechnet die Frequenz in eine Energie um. Hohe Frequenzen tragen mehr Energie, deshalb wächst das thermische Rauschen mit der Frequenz immer weiter an.
:::
:::karte begriff Signal-Rausch-Verhältnis
Was gibt das Signal-Rausch-Verhältnis an, und wie hängt es mit den Effektivwerten von Signal und Rauschen zusammen?
---
Das Verhältnis der Signalleistung zur Rauschleistung: $\mathrm{SNR}=\frac{P_\mathrm{s}}{P_\mathrm{r}}=\Bigl(\frac{u_\mathrm{s,eff}}{u_\mathrm{r,eff}}\Bigr)^2$. Spannungen gehen quadratisch ein.
--- falsch
Das Verhältnis der Effektivwerte, $u_\mathrm{s,eff}/u_\mathrm{r,eff}$, ohne Quadrat; Spannungen vergleicht man direkt, Leistungen spielen beim Rauschen keine Rolle.
--- falsch
Das Verhältnis der Rauschleistung zur Signalleistung, $P_\mathrm{r}/P_\mathrm{s}$. Ein großer Wert bedeutet also ein stark verrauschtes Signal und eine schlechte Messung.
--- falsch
Die Differenz $P_\mathrm{s}-P_\mathrm{r}$ aus Signal- und Rauschleistung, in Watt. Sie gibt an, wie viel Leistung nach Abzug des Rauschens für das Signal bleibt.
:::
:::karte begriff Dezibel
Was bedeutet die Angabe eines Signal-Rausch-Verhältnisses in Dezibel, und wie rechnet man sie aus Leistungen und aus Spannungen?
---
Ein logarithmisches Maß für das Verhältnis: $\mathrm{SNR}_\mathrm{dB}=10\lg\frac{P_\mathrm{s}}{P_\mathrm{r}}=20\lg\frac{u_\mathrm{s,eff}}{u_\mathrm{r,eff}}$. 20 dB bedeuten den Faktor 10 in der Spannung und 100 in der Leistung.
--- falsch
$\mathrm{SNR}_\mathrm{dB}=20\lg\frac{P_\mathrm{s}}{P_\mathrm{r}}=10\lg\frac{u_\mathrm{s,eff}}{u_\mathrm{r,eff}}$ mit dem Zehnerlogarithmus. 20 dB bedeuten den Faktor 100 in der Spannung und 10 in der Leistung.
--- falsch
$\mathrm{SNR}_\mathrm{dB}=10\lg\frac{P_\mathrm{s}}{P_\mathrm{r}}=10\lg\frac{u_\mathrm{s,eff}}{u_\mathrm{r,eff}}$ mit dem Zehnerlogarithmus. Leistung und Spannung zählen gleich, 20 dB bedeuten in beiden den Faktor 100, weil der Logarithmus beide gleich behandelt.
--- falsch
Ein Maß mit dem natürlichen Logarithmus, $\mathrm{SNR}_\mathrm{dB}=\ln\frac{P_\mathrm{s}}{P_\mathrm{r}}$. 20 dB bedeuten also den Faktor $\mathrm{e}^{20}$ in der Leistung und $\mathrm{e}^{10}$ in der Spannung.
:::
:::karte herleitung Warum sich Quadrate addieren
Wie folgt für zwei unabhängige Störungen $u_1$ und $u_2$, dass sich die Quadrate ihrer Effektivwerte addieren und nicht die Effektivwerte selbst?
---
Man quadriert die Summe, $(u_1+u_2)^2=u_1^2+2u_1u_2+u_2^2$, weil das Quadrat des Effektivwerts der zeitliche Mittelwert des Quadrats ist.
---
Das Produkt $u_1u_2$ ist im Mittel über die Zeit gleich oft positiv wie negativ, weil die beiden Störungen unabhängig sind; sein Mittelwert verschwindet.
---
Es bleibt $u_\mathrm{ges,eff}^2=u_\mathrm{1,eff}^2+u_\mathrm{2,eff}^2$, weil nur die beiden Quadrate einen Mittelwert ungleich null haben.
---
Das Integral über die Rauschspannungsdichte ist dieselbe Summe über alle Frequenzstreifen, weil jeder Streifen einen solchen unabhängigen Beitrag liefert.
:::
:::karte zusammenhang Widerstände in Reihe
Warum rauschen zwei Widerstände von 47 k$\Omega$ und 53 k$\Omega$ in Reihe genauso stark wie ein einzelner Widerstand von 100 k$\Omega$?
---
Ihre unabhängigen Rauschspannungen addieren sich quadratisch, und jedes Quadrat ist proportional zum Widerstand. Die Summe der Quadrate ist deshalb das Quadrat für 100 k$\Omega$.
--- falsch
Ihre Rauschspannungen addieren sich linear zu 5,75 µ V, und das ist derselbe Wert wie bei 100 k$\Omega$, weil die Dichte proportional zum Widerstand ist und sich die Beiträge einfach summieren.
--- falsch
Sie rauschen nicht gleich stark: Zwei Widerstände sind zwei unabhängige Quellen und rauschen deshalb doppelt so stark wie einer mit demselben Gesamtwert.
--- falsch
Ihre Rauschspannungen heben sich in Reihe teilweise auf; die Summe ist kleiner als jeder Einzelwert, und das gleicht den größeren Gesamtwiderstand gerade aus.
:::
:::karte zusammenhang Verstärker gegen Rauschen
Warum verbessert ein Verstärker direkt am Sensor das Signal-Rausch-Verhältnis nur gegenüber Störungen, die erst hinter ihm dazukommen?
---
Er hebt Signal und anliegendes Rauschen um denselben Faktor, ihr Verhältnis bleibt höchstens gleich. Eine feste Störung danach ist gegen das verstärkte Signal aber klein.
--- falsch
Er verstärkt nur das Signal, weil das Rauschen außerhalb seiner Bandbreite liegt; deshalb verbessert er das Verhältnis gegenüber jeder Störung, auch der am Sensor selbst.
--- falsch
Er verstärkt das Rauschen stärker als das Signal, weil Rauschen mehr Frequenzen enthält; erst die Störungen hinter ihm sind gegen dieses Rauschen wieder klein.
--- falsch
Er hebt Signal und Rauschen um denselben Faktor; Störungen hinter ihm werden dabei ebenfalls mit demselben Faktor verstärkt, deshalb ändert er auch an ihnen nichts.
:::
::::

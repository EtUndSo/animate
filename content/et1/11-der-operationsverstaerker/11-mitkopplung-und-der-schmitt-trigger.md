---
title: Stufe 9: Mitkopplung und der Schmitt-Trigger
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Der Operationsverstärker
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-operationsverstarker
knoten: Kapitel 11: Der Operationsverstärker
order: 1211100
summary: Vertauscht man im nicht-invertierenden Verstärker die Eingänge, ergeben dieselben Gleichungen dieselbe Zahl.
tags: Hysterese, Schmitt-Trigger, instabil
lang: de
---

<span class="anker" id="stufe-9"></span>

:::zweck
Vertauscht man im nicht-invertierenden Verstärker die Eingänge, ergeben dieselben Gleichungen dieselbe Zahl. Die Schaltung tut aber etwas völlig anderes. Diese Stufe klärt, warum die Regel hier versagt und was stattdessen geschieht.
:::

**Die Idee.** Nun liegt $U_\mathrm{E}$ am Minus-Eingang, der Teiler führt auf den Plus-Eingang (Abb. [11](#abb-11)). Die Rechnung $U_\mathrm{D}=\beta\,U_\mathrm{A}-U_\mathrm{E}$ und $U_\mathrm{A}=A\,U_\mathrm{D}$ hat bei $U_\mathrm{E}=1$ V die Lösung $U_\mathrm{A}=5{,}00025$ V. Das ist ein Gleichgewicht, aber ein instabiles, wie eine Kugel auf einer Kuppe. Eine Störung von 1 µ V nach oben hebt den Plus-Eingang, also wächst $U_\mathrm{D}$, also steigt der Ausgang weiter. Die Wirkung verstärkt ihre Ursache. Der Ausgang läuft bis zum Anschlag und bleibt dort. Dort gilt die Regel nicht: $U_\mathrm{D}\ne0$.

Am Anschlag merkt sich die Schaltung ihren Zustand. Steht der Ausgang auf $+11$ V, liegt der Plus-Eingang bei $+2{,}2$ V. Solange $U_\mathrm{E}$ darunter bleibt, ist $U_\mathrm{D}>0$ und nichts ändert sich. Überschreitet $U_\mathrm{E}$ die 2,2 V, kippt der Ausgang, und der Plus-Eingang springt auf $-2{,}2$ V. Das verstärkt das Kippen. Um zurückzukippen, muss $U_\mathrm{E}$ unter $-2{,}2$ V sinken. Der Ausgang hängt von der Vorgeschichte ab, das nennt man __Hysterese__. Die Schaltung heißt invertierender __Schmitt-Trigger__.

:::satz Satz 9.1 (Schmitt-Trigger)
<span class="anker" id="satz-9-1"></span>

Mit $\beta=R_1/(R_1+R_2)$ kippt der Ausgang

<span class="anker" id="gl-9-1"></span>
$$\text{nach unten bei }U_\mathrm{E}=\beta\,U_\mathrm{A,max},\qquad\text{nach oben bei }U_\mathrm{E}=\beta\,U_\mathrm{A,min}. \tag{9.1}$$

Die Breite der Hysterese ist $\beta\,(U_\mathrm{A,max}-U_\mathrm{A,min})$. Zwischen den Schwellen sind beide Zustände möglich.
:::

⁠**So liest man das:** Der Ausgang wechselt, sobald $U_\mathrm{D}$ das Vorzeichen wechselt. **Gültigkeit:** $A\beta>1$, sonst reicht die Mitkopplung nicht zum Kippen.

:::herleitung Dieselbe Gleichung, anderes Vorzeichen
Mit der Trägheit aus Stufe [4](gegenkopplung.html#stufe-4) gilt nun $\tau\,\mathrm{d} U_\mathrm{A}/\mathrm{d} t=A(\beta\,U_\mathrm{A}-U_\mathrm{E})-U_\mathrm{A}=(A\beta-1)\,U_\mathrm{A}-A\,U_\mathrm{E}$. Der Faktor vor $U_\mathrm{A}$ ist jetzt positiv. Eine Abweichung vom Gleichgewicht wächst wie $\mathrm{e}^{+t/\tau_\mathrm{M}}$ mit $\tau_\mathrm{M}=\tau/(A\beta-1)=0{,}80$ µ s, derselben Größe wie in Stufe [4](gegenkopplung.html#stufe-4). Aus 1 µ V Störung werden so in 13 µ s die 11 V. Eine unbegrenzte Versorgung gäbe einen unbegrenzten Anstieg, die Schaltung wäre __instabil__. Erst die Sättigung stoppt ihn.
:::

:::abbildung et1/k11schmitt 11
Links der invertierende Schmitt-Trigger. Rechts die Hystereseschleife im Rechenmodell, $\beta=0{,}2$: Wer von links kommt, kippt bei $+2{,}2$ V, wer von rechts kommt, bei $-2{,}2$ V. Die Pfeile geben die Laufrichtung.
:::

::::beispiel
Die Schwellen sind $\pm0{,}2\cdot11\,\mathrm{V}=\pm2{,}2$ V, die Hysterese ist 4,4 V breit. Kurz nach dem Kippen bei $U_\mathrm{E}=2{,}2$ V ist $U_\mathrm{D}=-2{,}2\,\mathrm{V}-2{,}2\,\mathrm{V}=-4{,}4$ V, weit weg vom Fenster. Nutzen: Ein verrauschtes Signal, das langsam durch eine Schwelle läuft, schaltet einen Komparator viele Male hin und her. Beim Schmitt-Trigger springt die Schwelle nach dem ersten Kippen um 4,4 V weg, Rauschen unter dieser Breite löst kein zweites Kippen aus.
::::

⁠**Grenzfälle:** $\beta\to0$ ergibt den Komparator aus Stufe [3](der-opv-ohne-ruckfuhrung.html#stufe-3). $U_\mathrm{E}=0$ lässt beide Zustände zu, je nach Vorgeschichte.

:::frage LTspice zeigte in `.op` bei vertauschten Eingängen 5,00025 V. Ist die Simulation falsch?
Nein, sie beantwortet eine andere Frage. `.op` löst die Gleichgewichtsgleichung, und diese Lösung existiert. Ob ein Gleichgewicht hält, entscheidet erst der Zeitverlauf. Im Bauteil rauscht immer etwas, darum läuft der Ausgang davon. Der LTspice-Kasten in Stufe [10](wo-die-regeln-enden.html#stufe-10) zeigt das in `.tran`.
:::

:::aufgabe Aufgabe 10 ★★ Schmitt-Trigger
<span class="anker" id="aufg-10"></span>

(a) Bei $R_1=10$ k$\Omega$, $R_2=90$ k$\Omega$: Wo liegen die Schwellen, wie breit ist die Hysterese? (b) Wähle $R_2$ für die Schwellen $\pm1$ V bei $R_1=10$ k$\Omega$. (c) Mit (a) läuft $U_\mathrm{E}$ von $-5$ V auf $+5$ V und zurück. Skizziere $U_\mathrm{A}(U_\mathrm{E})$. (d) Eine Versorgung von 0 bis 5 V ergibt einen Ausgang von 0,5 V bis 4,5 V, $\beta=0{,}2$. Wo liegen die Schwellen?

:::loesung
(a) $\beta=0{,}1$: Schwellen $\pm1{,}1$ V, Breite 2,2 V. (b) $\beta=1/11$, also $R_2=100$ k$\Omega$. (c) Bei $-5$ V steht der Ausgang auf $+11$ V. Er bleibt dort bis $U_\mathrm{E}=+1{,}1$ V, springt auf $-11$ V und bleibt dort bis $5$ V. Beim Rückweg springt er erst bei $-1{,}1$ V zurück. (d) $0{,}2\cdot4{,}5\,\mathrm{V}=0{,}9$ V und $0{,}2\cdot0{,}5\,\mathrm{V}=0{,}1$ V.
:::
:::

::::formelsammlung
**Schwellen des Schmitt-Triggers**

$$\text{nach unten bei }U_\mathrm{E}=\beta\,U_\mathrm{A,max},\qquad\text{nach oben bei }U_\mathrm{E}=\beta\,U_\mathrm{A,min}$$

Invertierender Schmitt-Trigger mit $\beta=R_1/(R_1+R_2)$. Der Ausgang wechselt, sobald $U_\mathrm{D}$ das Vorzeichen wechselt. Gilt für $A\beta>1$.

**Breite der Hysterese**

$$\beta\,(U_\mathrm{A,max}-U_\mathrm{A,min})$$

Zwischen den Schwellen sind beide Zustände möglich.

**Anwachsen bei Mitkopplung**

$$\tau\,\mathrm{d} U_\mathrm{A}/\mathrm{d} t=(A\beta-1)\,U_\mathrm{A}-A\,U_\mathrm{E},\qquad \tau_\mathrm{M}=\tau/(A\beta-1)$$

Der Faktor vor $U_\mathrm{A}$ ist positiv: Eine Abweichung wächst wie $\mathrm{e}^{+t/\tau_\mathrm{M}}$, bis die Sättigung sie stoppt.
::::

::::lernkarten
:::karte zusammenhang Instabiles Gleichgewicht
Warum stellt sich an einem OPV mit vertauschten Eingängen der rechnerische Wert $U_\mathrm{A}=5{,}00025$ V nicht ein?
---
Er ist ein instabiles Gleichgewicht. Eine Störung von 1 µ V nach oben hebt den Plus-Eingang, $U_\mathrm{D}$ wächst, und der Ausgang steigt weiter, bis er am Anschlag steht.
--- falsch
Der Wert ist falsch berechnet: Mit vertauschten Eingängen haben die Gleichungen gar keine Lösung, nur ein Rundungsfehler der Simulation erzeugt eine scheinbare Lösung im Gleichgewicht.
--- falsch
Er ist ein stabiles Gleichgewicht, das der Ausgang aber erst nach Sekunden erreicht; bis dahin pendelt er zwischen den beiden Anschlägen hin und her, gedämpft wie ein Pendel.
--- falsch
Die Mitkopplung macht die Leerlaufverstärkung negativ; der Ausgang stellt sich deshalb auf $-5{,}00025$ V ein statt auf den positiven Wert.
:::
:::karte begriff instabil
Wann nennt man eine Schaltung wie den mitgekoppelten OPV instabil?
---
Wenn eine Abweichung vom Gleichgewicht nicht abklingt, sondern wächst, hier wie $\mathrm{e}^{+t/\tau_\mathrm{M}}$. Mit einer unbegrenzten Versorgung gäbe das einen unbegrenzten Anstieg.
--- falsch
Wenn ihr Ausgang durch Rauschen leicht um einen festen Wert schwankt; im Mittel bleibt sie dabei aber im Gleichgewicht und kehrt immer dorthin zurück, wie eine Kugel in einer Mulde.
--- falsch
Wenn ihre Versorgungsspannung schwankt; mit einer stabilisierten Versorgung arbeitet dieselbe Schaltung ruhig in ihrem Gleichgewicht.
--- falsch
Wenn eine Abweichung vom Gleichgewicht wie $\mathrm{e}^{-t/\tau_\mathrm{M}}$ abklingt, dabei aber überschwingt; der Ausgang erreicht sein Ziel erst nach einigen Schwingungen.
:::
:::karte herleitung Dieselbe Gleichung, anderes Vorzeichen
Wie folgt aus der Trägheit des OPV-Ausgangs, dass die Schaltung mit Rückführung auf den Plus-Eingang instabil ist?
---
Mit $U_\mathrm{D}=\beta\,U_\mathrm{A}-U_\mathrm{E}$ wird die Trägheitsgleichung zu $\tau\,\mathrm{d} U_\mathrm{A}/\mathrm{d} t=A(\beta\,U_\mathrm{A}-U_\mathrm{E})-U_\mathrm{A}=(A\beta-1)\,U_\mathrm{A}-A\,U_\mathrm{E}$, weil der zurückgeführte Anteil am Plus-Eingang positiv zählt.
---
Der Faktor $A\beta-1$ vor $U_\mathrm{A}$ ist positiv, weil $A\beta$ viel größer als 1 ist.
---
Eine Abweichung vom Gleichgewicht wächst deshalb wie $\mathrm{e}^{+t/\tau_\mathrm{M}}$ mit $\tau_\mathrm{M}=\tau/(A\beta-1)$, weil ihre Änderung immer vom Gleichgewicht weg zeigt.
---
Aus 1 µ V Störung werden so in 13 µ s die 11 V, weil jede Zeitkonstante $\tau_\mathrm{M}$, hier 0,80 µ s, den Abstand um den Faktor $\mathrm{e}$ vergrößert; erst die Sättigung stoppt den Anstieg.
:::
:::karte begriff Schmitt-Trigger
Was ist ein invertierender Schmitt-Trigger, und wie ist er beschaltet?
---
Ein mitgekoppelter OPV: $U_\mathrm{E}$ liegt am Minus-Eingang, ein Teiler führt den Anteil $\beta$ des Ausgangs auf den Plus-Eingang. Er kippt an zwei verschiedenen Schwellen.
--- falsch
Ein gegengekoppelter OPV: $U_\mathrm{E}$ liegt am Plus-Eingang, ein Teiler führt auf den Minus-Eingang; er verstärkt linear mit $1/\beta$ und hat keine Schwellen.
--- falsch
Ein OPV ohne Rückführung, dessen Ausgang bei $U_\mathrm{D}=0$ kippt; er hat eine einzige Schwelle, die in beide Richtungen gleich wirkt, und keine Hysterese.
--- falsch
Ein mitgekoppelter OPV mit $U_\mathrm{E}$ am Plus-Eingang und dem Teiler auf den Minus-Eingang; er kippt in beide Richtungen bei $U_\mathrm{E}=0$.
:::
:::karte zusammenhang Hysterese
Warum hängt der Ausgang eines Schmitt-Triggers von der Vorgeschichte ab?
---
Der Ausgang bestimmt die Schwelle: Bei $+11$ V liegt der Plus-Eingang bei $+2{,}2$ V, nach dem Kippen bei $-2{,}2$ V. Zurück kippt der Ausgang also erst, wenn $U_\mathrm{E}$ unter $-2{,}2$ V sinkt.
--- falsch
Der Kondensator im OPV speichert den letzten Zustand; nach einigen Millisekunden ist er entladen, und der Ausgang folgt dann wieder nur $U_\mathrm{E}$ ohne jede Schwelle und ohne Gedächtnis.
--- falsch
Der Plus-Eingang liegt fest auf $+2{,}2$ V; der Ausgang kippt in beide Richtungen an dieser Schwelle, nur mit einer kleinen Verzögerung durch die innere Kapazität.
--- falsch
Die Eingänge ziehen nach dem Kippen einen Strom, der $U_\mathrm{E}$ verschiebt; so merkt sich die Signalquelle den Zustand der Schaltung.
:::
:::karte formel Schwellen des Schmitt-Triggers
Bei welchen Eingangsspannungen kippt der invertierende Schmitt-Trigger mit $\beta=R_1/(R_1+R_2)$, und wie breit ist seine Hysterese?
---
Nach unten bei $U_\mathrm{E}=\beta\,U_\mathrm{A,max}$, nach oben bei $U_\mathrm{E}=\beta\,U_\mathrm{A,min}$. Die Breite ist $\beta\,(U_\mathrm{A,max}-U_\mathrm{A,min})$.
--- falsch
Nach unten bei $U_\mathrm{E}=\beta\,U_\mathrm{A,min}$, nach oben bei $U_\mathrm{E}=\beta\,U_\mathrm{A,max}$. Die Breite ist $\beta\,(U_\mathrm{A,max}-U_\mathrm{A,min})$, also 4,4 V.
--- falsch
In beide Richtungen bei $U_\mathrm{E}=\beta\,U_\mathrm{A,max}$. Die Breite ist null; der Teiler verschiebt nur die gemeinsame Schwelle von 0 auf 2,2 V.
--- falsch
Nach unten bei $U_\mathrm{E}=U_\mathrm{A,max}/\beta$, nach oben bei $U_\mathrm{E}=U_\mathrm{A,min}/\beta$. Mit $\beta=0{,}2$ und $\pm11$ V sind das $\pm55$ V.
:::
:::karte zusammenhang Nutzen der Hysterese
Warum schaltet ein Schmitt-Trigger bei einem verrauschten Signal, das langsam durch die Schwelle läuft, nur einmal, ein Komparator aber viele Male?
---
Beim Komparator schaltet Rauschen um die feste Schwelle mehrfach. Beim Schmitt-Trigger springt die Schwelle nach dem ersten Kippen weg; Rauschen unter der Breite der Hysterese kippt nichts mehr.
--- falsch
Der Schmitt-Trigger glättet das Rauschen mit seiner inneren Kapazität; seine Schwelle liegt fest wie beim Komparator, nur das Signal ist sauberer und kreuzt die Schwelle deshalb genau einmal.
--- falsch
Der Schmitt-Trigger ist gegengekoppelt und hat deshalb $U_\mathrm{D}=0$; die Schleife regelt das Rauschen aus, bevor es den Ausgang erreicht.
--- falsch
Der Komparator hat die kleinere Leerlaufverstärkung und reagiert langsamer; das Rauschen sammelt sich in ihm an und schaltet ihn mehrfach.
:::
:::karte zusammenhang Gleichgewicht in der Simulation
Warum zeigt die Arbeitspunktrechnung von LTspice bei vertauschten Eingängen 5,00025 V, obwohl die Schaltung so nie arbeitet?
---
Die Gleichgewichtsgleichung hat diese Lösung. Ob ein Gleichgewicht hält, entscheidet erst der Zeitverlauf; im Bauteil rauscht immer etwas, darum läuft der Ausgang davon.
--- falsch
Die Simulation rechnet mit einem idealen OPV ohne Grenzen; mit einem realen OPV-Modell läge auch das berechnete Gleichgewicht am Anschlag bei $+11$ V.
--- falsch
Die Simulation ist an dieser Stelle fehlerhaft; ein korrektes Programm fände keine Lösung, weil die Gleichungen einander widersprechen und sich nicht gleichzeitig erfüllen lassen.
--- falsch
Sie zeigt den Mittelwert über das Pendeln zwischen den Anschlägen; die Schaltung schwingt tatsächlich ständig um 5,00025 V herum.
:::
:::karte zusammenhang Bedingung zum Kippen
Was wird aus dem Schmitt-Trigger, wenn $A\beta$ kleiner als 1 ist oder $\beta$ gegen null geht?
---
Er arbeitet nur für $A\beta>1$, sonst reicht die Mitkopplung nicht zum Kippen. Für $\beta\to0$ schrumpft die Hysterese auf null, und es bleibt der Komparator ohne Rückführung.
--- falsch
Für $A\beta<1$ wird die Hysterese besonders breit, weil der Ausgang langsamer kippt; für $\beta\to0$ bleibt der Ausgang dauerhaft am oberen Anschlag und kippt auch bei großem Eingang nie.
--- falsch
$A\beta$ spielt keine Rolle, nur $\beta$; für $\beta\to0$ wird die Schaltung zum nicht-invertierenden Verstärker mit sehr großer Verstärkung.
--- falsch
Für $A\beta<1$ wird die Schaltung gegengekoppelt und verstärkt linear; für $\beta\to0$ wird die Hysterese dagegen unendlich breit.
:::
::::

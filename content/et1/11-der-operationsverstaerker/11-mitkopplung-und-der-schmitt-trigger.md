---
title: Stufe 9: Mitkopplung und der Schmitt-Trigger
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Der Operationsverstärker
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

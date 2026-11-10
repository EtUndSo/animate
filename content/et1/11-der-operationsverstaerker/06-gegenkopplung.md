---
title: Stufe 4: Gegenkopplung
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Der Operationsverstärker
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-operationsverstarker
knoten: Kapitel 11: Der Operationsverstärker
order: 1210600
summary: Ohne Rückführung ist der OPV ein Schalter.
tags: Rückkopplung, Mitkopplung, nicht-invertierenden Verstärker, Impedanzwandler
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Ohne Rückführung ist der OPV ein Schalter. Diese Stufe zeigt, warum ein zurückgeführter Teil des Ausgangs die Differenz der Eingänge fast auf null bringt und warum die Verstärkung dann nicht mehr von $A$ abhängt.
:::

**Die Idee.** __Rückkopplung__ heißt: Ein Teil der Ausgangsgröße gelangt zum Eingang zurück. Wirkt er der Ursache entgegen, ist es Gegenkopplung, verstärkt er sie, __Mitkopplung__. Beim OPV bringt der Weg zum Minus-Eingang Gegenkopplung, denn dort wirkt jede Spannung mit negativem Vorzeichen.

Beim __nicht-invertierenden Verstärker__ liegt $U_\mathrm{E}$ am Plus-Eingang (Abb. [6](#abb-6)). Der Teiler aus $R_2$ und $R_1$ meldet ein Fünftel des Ausgangs an den Minus-Eingang. Lege nun $U_\mathrm{E}=1$ V an. Zu Beginn ist $U_\mathrm{A}=0$, also $\varphi_-=0$ und $U_\mathrm{D}=1$ V. Der Zielwert $A\,U_\mathrm{D}$ wären 100 kV, der Ausgang läuft aufwärts. Bei 4 V Ausgang ist $\varphi_-=0{,}8$ V, es fehlen noch 200 mV. Bei 4,9 V fehlen 20 mV, bei 4,99 V nur 2 mV, das Ziel ist auf 200 V geschrumpft. Der Ausgang holt sein Ziel erst ein, wenn beide gleich sind: $A\,U_\mathrm{D}=U_\mathrm{A}$. Das passiert bei $U_\mathrm{A}\approx5$ V und $U_\mathrm{D}=5\,\mathrm{V}/100000=50$ µ V. Auch ein Absinken wäre sofort korrigiert: Fällt der Ausgang, sinkt $\varphi_-$, $U_\mathrm{D}$ wächst, der Ausgang steigt.

Die kleine Differenz ist also kein Grundgesetz des Bauteils, sondern das Ergebnis der Schleife. Null kann sie nicht sein, denn ohne Differenz gäbe es keinen Ausgang.

:::satz Satz 4.1 (Gegengekoppelter Verstärker)
<span class="anker" id="satz-4-1"></span>

Wird der Anteil $\beta$ des Ausgangs auf den Minus-Eingang geführt und liegt $U_\mathrm{E}$ am Plus-Eingang, gilt im linearen Bereich

<span class="anker" id="gl-4-1"></span>
$$U_\mathrm{D}=\frac{U_\mathrm{E}}{1+A\beta},\qquad G=\frac{U_\mathrm{A}}{U_\mathrm{E}}=\frac{A}{1+A\beta}=\frac1\beta\cdot\frac{1}{1+\dfrac1{A\beta}}. \tag{4.1}$$

Für $A\beta\gg1$ ist $G\approx1/\beta$ mit der relativen Abweichung $-1/(A\beta)$. Eine Änderung von $A$ wirkt um den Faktor $1+A\beta$ geschwächt:

<span class="anker" id="gl-4-2"></span>
$$\frac{\Delta G}{G}\approx\frac{1}{1+A\beta}\cdot\frac{\Delta A}{A}. \tag{4.2}$$

Mit dem Teiler ist $\beta=R_1/(R_1+R_2)$, also $G\approx1+R_2/R_1$.
:::

⁠**So liest man das:** $\beta$ ist der zurückgeführte Anteil, zwischen 0 und 1, hier 0,2. $G$ ist die Verstärkung der ganzen Schaltung. $A\beta$ ist die Schleifenverstärkung: Eine kleine Änderung bei $U_\mathrm{D}$ wird mit $A$ verstärkt und mit $\beta$ abgeschwächt zurückgemeldet. Hier ist $A\beta=20000$, das ist die Reserve, die die Abweichung klein hält. **Gültigkeit:** $U_\mathrm{A,min}<U_\mathrm{A}<U_\mathrm{A,max}$, Eingangsstrom klein gegen den Teilerstrom, $A$ bei der betrachteten Frequenz (Stufe [10](wo-die-regeln-enden.html#stufe-10)).

:::herleitung Die Schleife im Gleichgewicht und in Bewegung
Gleichgewicht: $U_\mathrm{A}=A\,U_\mathrm{D}$ und $U_\mathrm{D}=U_\mathrm{E}-\beta\,U_\mathrm{A}$. Einsetzen ergibt $U_\mathrm{D}=U_\mathrm{E}-A\beta\,U_\mathrm{D}$, daraus [(4.1)](#gl-4-1). Ableiten von $G$ nach $A$ ergibt $\mathrm{d} G/\mathrm{d} A=1/(1+A\beta)^2$, geteilt durch $G$ folgt [(4.2)](#gl-4-2).

Bewegung: Im OPV lädt ein Strom proportional zu $U_\mathrm{D}$ eine Kapazität. Der Ausgang kann deshalb nicht springen, sondern läuft seinem Zielwert nach: $\tau\,\mathrm{d} U_\mathrm{A}/\mathrm{d} t=A\,U_\mathrm{D}-U_\mathrm{A}$, hier mit $\tau=A/(2\pi f_\mathrm{T})=15{,}9$ ms. Das ist die Gleichung des RC-Glieds aus [Kapitel 3](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator/der-kondensator.html). Mit $U_\mathrm{D}=U_\mathrm{E}-\beta\,U_\mathrm{A}$ wird daraus

$$\tau\,\frac{\mathrm{d} U_\mathrm{A}}{\mathrm{d} t}=A\,U_\mathrm{E}-(1+A\beta)\,U_\mathrm{A}.$$

Der Faktor vor $U_\mathrm{A}$ ist negativ, jede Abweichung klingt ab: $U_\mathrm{A}(t)=G\,U_\mathrm{E}\,(1-\mathrm{e}^{-t/\tau_G})$ mit $\tau_G=\tau/(1+A\beta)=0{,}80$ µ s. Die Schleife ist 20001-mal schneller als der OPV allein.
:::

:::abbildung et1/k11schleife 5
Links die Schleife als Blockbild: Am Summierpunkt wird $\beta\,U_\mathrm{A}$ abgezogen. Rechts die Antwort auf einen Sprung von 0 auf 1 V im linearen Modell: $U_\mathrm{A}$ steigt mit $\tau_G=0{,}80$ µ s auf 5 V, $U_\mathrm{D}$ fällt von 1 V auf 50 µ V.
:::

::::beispiel
Mit $A\beta=20000$ wird aus 1 V Eingang $U_\mathrm{A}=4{,}99975$ V, die Abweichung vom Ideal 5 V ist 0,005 % $=1/(A\beta)$. Die Exemplare streuen um den Faktor vier:

| $A$ | $U_\mathrm{D}$ | $U_\mathrm{A}$ | Abweichung von 5 V |
|---|---|---|---|
| 50000 | 99,99 µ V | 4,99950 V | $-0{,}0100$ % |
| 100000 | 50,00 µ V | 4,99975 V | $-0{,}0050$ % |
| 200000 | 25,00 µ V | 4,99988 V | $-0{,}0025$ % |

Eine Änderung von $A$ um 300 % verschiebt $G$ um 0,0075 %. Man tauscht Verstärkung gegen Genauigkeit: 100000 werden zu 5, dafür bestimmen zwei Widerstände das Ergebnis.
::::

⁠**Kurz gesagt:** Die Verstärkung ist der Kehrwert des zurückgeführten Anteils. **Grenzfälle:** $A\to\infty$ ergibt $U_\mathrm{D}\to0$ und $G=1/\beta$. $\beta\to0$ ergibt $G\to A$, ohne Rückführung bleibt der Leerlauf.

**Eingang und Ausgang.** Am Plus-Eingang liegt nur $U_\mathrm{D}=50$ µ V über $r_\mathrm{e}$, es fließen 50 pA, ein Zweimillionstel des Teilerstroms von 100 µ A. Der Eingangswiderstand steigt so auf $r_\mathrm{e}(1+A\beta)=20$ G$\Omega$. Am Ausgang wirkt die Schleife gegen jede Belastung: Zieht eine Last $U_\mathrm{A}$ etwas herunter, wächst $U_\mathrm{D}$, und die innere Spannung steigt, bis der Verlust fast ausgeglichen ist. Der Ausgangswiderstand sinkt auf $r_\mathrm{a}/(1+A\beta)=3{,}75$ m$\Omega$.

**Der Impedanzwandler.** Mit $R_2=0$ und $R_1\to\infty$ ist der Ausgang direkt mit dem Minus-Eingang verbunden, $\beta=1$, $G=A/(1+A)=0{,}99999$. Dieser __Impedanzwandler__ verstärkt nicht, sondern trennt: Eingangswiderstand 100 G$\Omega$, Ausgangswiderstand 0,75 m$\Omega$. Ein Spannungsmesser mit 1 M$\Omega$ an einer Quelle mit 1 V und 100 k$\Omega$ Innenwiderstand zeigt 0,909 V ([Kapitel 4](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-und-spannung-messen/strom-und-spannung-messen.html)). Mit vorgeschaltetem Impedanzwandler zeigt er 0,99999 V.

:::abbildung et1/k11nichtinv 6
Links der nicht-invertierende Verstärker mit Potenzialen im Rechenmodell. Der Minus-Eingang liegt nur 50 µ V unter dem Plus-Eingang. Rechts der Impedanzwandler als Grenzfall $\beta=1$.
:::

:::frage Warum nimmt man nicht gleich einen Verstärker mit $G=5$, statt 100000 zu kaufen und fast alles zu verwerfen?
Weil dessen 5 von $B$, $U_\mathrm{Early}$ und der Temperatur abhingen: 1 % Änderung im Inneren wäre 1 % im Ergebnis. Mit der Reserve $A\beta=20000$ werden daraus $5\cdot10^{-5}$ %.
:::

:::frage Eben liegt der Ausgang zu tief, also springt er hoch, dann liegt er zu hoch. Müsste er nicht ewig hin und her pendeln?
Das täte er, wenn er in einem Schritt auf $A\,U_\mathrm{D}$ spränge: Der Fehler würde bei jedem Umlauf mit 20000 multipliziert. Der Ausgang springt aber nicht. Die innere Kapazität begrenzt sein Tempo, er läuft stetig und bremst, wenn $U_\mathrm{D}$ schrumpft. So kommt er ohne Überschwingen an (Herleitung oben).
:::

:::ltspice Die Differenz messen
⁠**Zeichnen:** `voltage` `VE` mit 1 von Netz `p` nach Masse. Eine gesteuerte Quelle `e` als OPV: Ausgang von Netz `a` nach Masse, Steuereingänge `p` (plus) und `m` (minus), Wert `{A}`. `res` `R2` 40k von `a` nach `m`, `R1` 10k von `m` nach Masse.

⁠**Direktiven:** `.param A=1e5`, `.step param A list 5e4 1e5 2e5`, `.op`, `.options numdgt=15`, `.meas op ua FIND V(a) AT=1e5`, `.meas op ud FIND V(p,m) AT=1e5`.

⁠**Was du siehst:** `ua` = 4,99975 V, `ud` = 49,9975 µ V, wie in der Rechnung. Mit `AT=5e4` kommen 4,99950 V und 99,99 µ V. Setze für Aufgabe [4](#aufg-4) `R2` auf 100k. Vertausche dann `p` und `m`: `.op` zeigt 5,00025 V. Warum das in Wirklichkeit nicht hält, klärt Stufe [9](mitkopplung-und-der-schmitt-trigger.html#stufe-9).
:::

:::aufgabe Aufgabe 4 ★★ Streuung und Reserve
<span class="anker" id="aufg-4"></span>

Der Verstärker soll $G=11$ haben, $R_1=10$ k$\Omega$. (a) Wähle $R_2$. Wie groß sind $\beta$ und $A\beta$? (b) Wie groß ist $U_\mathrm{D}$ bei $U_\mathrm{A}=5{,}5$ V? (c) Berechne $G$ für $A=50000$ und $200000$. (d) Welches $A$ genügt mindestens für 0,1 % Abweichung? (e) Was geschieht bei $U_\mathrm{E}=2$ V? Wie groß ist dann $U_\mathrm{D}$?

:::loesung
(a) $1+R_2/R_1=11$, also $R_2=100$ k$\Omega$. $\beta=1/11=0{,}0909$, $A\beta=9091$. (b) $5{,}5\,\mathrm{V}/100000=55$ µ V. (c) $G=10{,}99758$ und $10{,}99940$, Unterschied 0,016 %. (d) $1/(1+1/(A\beta))=0{,}999$ ergibt $A\beta=999$, also $A\ge10989$. (e) Rechnerisch 22 V, der Ausgang steht auf 11 V. Dann ist $\varphi_-=\beta\cdot11\,\mathrm{V}=1$ V und $U_\mathrm{D}=1$ V, die Regel gilt nicht.
:::
:::

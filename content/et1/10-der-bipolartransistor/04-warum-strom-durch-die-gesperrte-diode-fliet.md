---
title: Stufe 2: Warum Strom durch die gesperrte Diode fließt
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Der Bipolartransistor
order: 1200400
summary: Die CB-Diode sperrt, trotzdem fließen durch sie Milliampere.
tags: Injektion, Diffusionslänge, Transferstrom, aktive Bereich
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Die CB-Diode sperrt, trotzdem fließen durch sie Milliampere. Diese Stufe verfolgt den Weg der Elektronen und zeigt, warum dabei nur ein kleiner Basisstrom nötig ist.
:::

**Die Idee.** Eine gesperrte Diode sperrt nicht, weil ihre Grenze undurchlässig wäre. Sie sperrt, weil auf der p-Seite fast keine freien Elektronen bereitstehen. Das Feld der Raumladungszone treibt jedes Elektron, das von der p-Seite an die Grenze kommt, in das n-Gebiet hinüber. Für solche Elektronen ist die Grenze ein Abhang (Abb. [2](#abb-2), unten). Der Transistor liefert genau diese fehlenden Elektronen, in vier Schritten:

<ol>

<li>

⁠**Injektion.** $U_\mathrm{BE}$ senkt die Barriere an der BE-Grenze. Elektronen aus dem Emitter gelangen in die Basis. Dieses Einbringen heißt __Injektion__. Die Elektronendichte am Emitterrand der Basis wächst dabei mit $\mathrm{e}^{U_\mathrm{BE}/U_T}$.

</li>

<li>

⁠**Durchqueren.** In der p-Basis sind Elektronen eine Minderheit unter vielen Löchern. Sie diffundieren zum Kollektorrand, wo ihre Dichte fast null ist. Die Basis ist viel schmaler als die __Diffusionslänge__, die mittlere Strecke bis zur Rekombination, einige 10 µ m. Deshalb kommen fast alle durch.

</li>

<li>

⁠**Absaugen.** Am Kollektorrand erfasst das Feld der CB-Grenze jedes ankommende Elektron und zieht es in den Kollektor. Wie groß $U_\mathrm{CB}$ ist, spielt kaum eine Rolle, das Feld holt immer alle ab. Deshalb hängt $I_\mathrm{C}$ kaum von $U_\mathrm{CE}$ ab.

</li>

<li>

⁠**Nachliefern.** Zwei kleine Verluste bleiben: Löcher aus der Basis gelangen in den Emitter, und einige Elektronen rekombinieren in der Basis. Beides zehrt Löcher auf. Der Basisanschluss muss sie ersetzen. Dieser Ersatz ist der Basisstrom. Er bleibt klein, weil der Emitter viel stärker dotiert ist als die Basis und die Basis so schmal ist.

</li>

</ol>

Die Elektronen laufen vom Emitter zum Kollektor. Der technische Strom $I_\mathrm{C}$ zählt entgegengesetzt, vom Kollektor zum Emitter ([Teil 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)).

:::abbildung et1/k10basis 2
Oben: Weg der Elektronen im Arbeitspunkt. Der Emitterstrom von 2,01 mA teilt sich in 2 mA zum Kollektor und 10 µ A zur Basis. Unten: Energie eines Elektrons über dem Ort, schematisch. $U_\mathrm{BE}$ senkt die kleine Stufe am Emitter, $U_\mathrm{CB}$ vertieft den Abhang zum Kollektor.
:::

:::satz Satz 2.1 (Ströme im Normalbetrieb)
<span class="anker" id="satz-2-1"></span>

Leitet die BE-Diode mit $U_\mathrm{BE}\gg U_T$ und liegt der Kollektor über der Basis, gilt

<span class="anker" id="gl-2-1"></span>
$$I_\mathrm{C}=I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{BE}/U_T},\qquad I_\mathrm{B}=\frac{I_\mathrm{C}}{B},\qquad I_\mathrm{E}=\Bigl(1+\frac1B\Bigr)I_\mathrm{C}. \tag{2.1}$$
:::

⁠**So liest man das:** $I_\mathrm{C}$ heißt auch __Transferstrom__, weil er durch die Basis hindurch übertragen wird. $I_\mathrm{S}$ in A ist winzig, hier $1{,}9\cdot10^{-13}$ A, und hängt von Fläche und Dotierung ab. $U_T=k_\mathrm{B}T/e$ ist rund 26 mV bei 300 K. $B$ hat keine Einheit und liegt zwischen 10 und 1000. Der Wert hängt von Dotierung und Geometrie ab und streut: Exemplare eines Typs unterscheiden sich oft um den Faktor 2. **Gültigkeit:** der __aktive Bereich__ (Stufe [4](drei-bereiche-drei-ersatzschaltbilder.html#stufe-4)), bei nicht zu großem Strom.

:::herleitung Warum $I_\mathrm{B}$ proportional zu $I_\mathrm{C}$ ist
Elektronen und Löcher überqueren dieselbe Barriere. Die Elektronendichte am Emitterrand der Basis und die Löcherdichte am Basisrand des Emitters wachsen beide mit $\mathrm{e}^{U_\mathrm{BE}/U_T}$. Der Kollektorstrom ist proportional zur ersten Dichte, die Rekombination in der Basis ebenso, der Löcherstrom zur zweiten. Alle Anteile tragen denselben Faktor, ihr Verhältnis $B=I_\mathrm{C}/I_\mathrm{B}$ hängt deshalb nicht von $U_\mathrm{BE}$ ab.
:::

**Wer steuert?** Physikalisch steuert $U_\mathrm{BE}$, denn nur die Spannung senkt die Barriere. Der Basisstrom ist der Preis dafür. In Schaltungen rechnet man trotzdem oft mit $I_\mathrm{B}$: Wegen $I_\mathrm{C}=B\,I_\mathrm{B}$ verhält sich der Transistor wie eine stromgesteuerte Stromquelle (CCCS, [Teil 6](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore/zweitore.html)). Beide Sichten beschreiben dieselbe Proportionalität. Die Steuerung über $U_\mathrm{BE}$ erklärt das Exponentialgesetz, die Sicht über $I_\mathrm{B}$ ist bequem, wenn ein Widerstand den Basisstrom vorgibt.

**Beispiel.** $U_\mathrm{BE}=0{,}6$ V ergibt $I_\mathrm{C}=1{,}9\cdot10^{-13}\,\mathrm{A}\cdot\mathrm{e}^{23{,}08}=2{,}00$ mA, $I_\mathrm{B}=10$ µ A, $I_\mathrm{E}=2{,}01$ mA. Das sind $1{,}25\cdot10^{16}$ Elektronen je Sekunde im Kollektor, und vom Emitterstrom kommen 99,5 % dort an. Die e-Funktion ist empfindlich: $+18$ mV verdoppeln den Strom ($U_T\ln2$), $+60$ mV verzehnfachen ihn ($U_T\ln10$), $+1$ mV bringt $+3{,}9$ %. **Grenzfälle:** Bei $U_\mathrm{BE}=0{,}4$ V fließen nur 0,9 µ A, der Transistor ist praktisch aus. Für $B\to\infty$ verschwindet $I_\mathrm{B}$, und $I_\mathrm{E}=I_\mathrm{C}$.

:::analogie
Eine große Wasserrinne ist durch eine Klappe verschlossen. Ein dünner Strahl aus einer Seitenrinne drückt die Klappe auf. Ohne Steuerstrahl fließt nichts, je stärker er ist, desto mehr strömt, und unten vereinigen sich beide Ströme. Das Bild trägt für drei Aussagen: Klein steuert groß, ohne Steuerung sperrt der Transistor, $I_\mathrm{E}=I_\mathrm{B}+I_\mathrm{C}$. Es stimmt nicht für den Mechanismus: Im Transistor bewegt nichts eine Klappe, die Spannung senkt eine Barriere, und der Zusammenhang ist exponentiell.
:::

:::frage Woher kommt die zusätzliche Leistung am Ausgang?
Aus der Versorgung $U_\mathrm{CC}$. Der Kollektorstrom läuft durch den ganzen Ausgangskreis, und die Quelle gibt dabei $U_\mathrm{CC}I_\mathrm{C}$ ab. Das Eingangssignal bezahlt nur $U_\mathrm{BE}I_\mathrm{B}$ und entscheidet damit, wie viel die Quelle liefert.
:::

:::aufgabe Aufgabe 2 ★★ Elektronen zählen
<span class="anker" id="aufg-2"></span>

Rechne mit Transistor T. (a) Wie viele Elektronen erreichen bei $I_\mathrm{C}=2$ mA je Sekunde den Kollektor? (b) Welche $U_\mathrm{BE}$ gehören zu 5 mA und zu 0,5 mA? Wie groß ist die Differenz, und warum hängt sie nicht von $I_\mathrm{S}$ ab? (c) Ein anderes Exemplar hat $B=50$. Welcher Anteil des Emitterstroms fließt über die Basis ab?

:::loesung
(a) $2\,\mathrm{mA}/e=1{,}25\cdot10^{16}$ je Sekunde. (b) $U_\mathrm{BE}=U_T\ln(I_\mathrm{C}/I_\mathrm{S})$ ergibt 0,624 V und 0,564 V. Die Differenz ist $U_T\ln10=59{,}9$ mV. In der Differenz zweier Logarithmen kürzt sich $I_\mathrm{S}$ heraus. (c) $I_\mathrm{B}/I_\mathrm{E}=1/(1+B)=1/51=2{,}0$ %.
:::
:::

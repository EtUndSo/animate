---
title: Stufe 2: Warum Strom durch die gesperrte Diode fließt
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Der Bipolartransistor
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor
knoten: Kapitel 10: Der Bipolartransistor
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

Die Elektronen laufen vom Emitter zum Kollektor. Der technische Strom $I_\mathrm{C}$ zählt entgegengesetzt, vom Kollektor zum Emitter ([Kapitel 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)).

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

**Wer steuert?** Physikalisch steuert $U_\mathrm{BE}$, denn nur die Spannung senkt die Barriere. Der Basisstrom ist der Preis dafür. In Schaltungen rechnet man trotzdem oft mit $I_\mathrm{B}$: Wegen $I_\mathrm{C}=B\,I_\mathrm{B}$ verhält sich der Transistor wie eine stromgesteuerte Stromquelle (CCCS, [Kapitel 6](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore/zweitore.html)). Beide Sichten beschreiben dieselbe Proportionalität. Die Steuerung über $U_\mathrm{BE}$ erklärt das Exponentialgesetz, die Sicht über $I_\mathrm{B}$ ist bequem, wenn ein Widerstand den Basisstrom vorgibt.

::::beispiel
$U_\mathrm{BE}=0{,}6$ V ergibt $I_\mathrm{C}=1{,}9\cdot10^{-13}\,\mathrm{A}\cdot\mathrm{e}^{23{,}08}=2{,}00$ mA, $I_\mathrm{B}=10$ µ A, $I_\mathrm{E}=2{,}01$ mA. Das sind $1{,}25\cdot10^{16}$ Elektronen je Sekunde im Kollektor, und vom Emitterstrom kommen 99,5 % dort an. Die e-Funktion ist empfindlich: $+18$ mV verdoppeln den Strom ($U_T\ln2$), $+60$ mV verzehnfachen ihn ($U_T\ln10$), $+1$ mV bringt $+3{,}9$ %.
::::

⁠**Grenzfälle:** Bei $U_\mathrm{BE}=0{,}4$ V fließen nur 0,9 µ A, der Transistor ist praktisch aus. Für $B\to\infty$ verschwindet $I_\mathrm{B}$, und $I_\mathrm{E}=I_\mathrm{C}$.

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

::::formelsammlung
**Ströme im Normalbetrieb**

$$I_\mathrm{C}=I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{BE}/U_T},\qquad I_\mathrm{B}=\frac{I_\mathrm{C}}{B},\qquad I_\mathrm{E}=\Bigl(1+\frac1B\Bigr)I_\mathrm{C}$$

Gilt im aktiven Bereich: Die BE-Diode leitet mit $U_\mathrm{BE}\gg U_T$, der Kollektor liegt über der Basis, der Strom ist nicht zu groß. $I_\mathrm{C}$ heißt Transferstrom. $I_\mathrm{S}$ in A hängt von Fläche und Dotierung ab, hier $1{,}9\cdot10^{-13}$ A. $B$ hat keine Einheit, liegt zwischen 10 und 1000 und streut oft um den Faktor 2.

**Temperaturspannung**

$$U_T=k_\mathrm{B}T/e$$

Rund 26 mV bei 300 K.

**Transistor als stromgesteuerte Stromquelle**

$$I_\mathrm{C}=B\,I_\mathrm{B}$$

Physikalisch steuert $U_\mathrm{BE}$; beide Sichten beschreiben dieselbe Proportionalität. Die Sicht über $I_\mathrm{B}$ ist bequem, wenn ein Widerstand den Basisstrom vorgibt.

**Spannung zu einem Kollektorstrom**

$$U_\mathrm{BE}=U_T\ln(I_\mathrm{C}/I_\mathrm{S})$$

Umkehrung der Exponentialfunktion. $U_T\ln2$, rund 18 mV, verdoppeln $I_\mathrm{C}$, $U_T\ln10$, rund 60 mV, verzehnfachen ihn; $+1$ mV bringt $+3{,}9$ %.

**Anteil des Basisstroms am Emitterstrom**

$$I_\mathrm{B}/I_\mathrm{E}=1/(1+B)$$

Folgt aus $I_\mathrm{E}=I_\mathrm{B}+I_\mathrm{C}$ und $I_\mathrm{C}=B\,I_\mathrm{B}$. Bei $B=200$ kommen 99,5 % des Emitterstroms im Kollektor an.
::::

::::lernkarten
:::karte zusammenhang Warum eine gesperrte Diode sperrt
Warum fließt durch eine gesperrte Diode kaum Strom, obwohl ihre Grenze für Elektronen von der p-Seite ein Abhang ist?
---
Die Grenze ist nicht undurchlässig. Auf der p-Seite stehen nur fast keine freien Elektronen bereit; jedes, das dort an die Grenze kommt, treibt das Feld ins n-Gebiet hinüber.
--- falsch
Die Grenze ist für Elektronen undurchlässig, weil die Raumladungszone keine freien Träger enthält. Ein Elektron, das von der p-Seite kommt, wird deshalb zurückgeworfen.
--- falsch
Auf der p-Seite gibt es viele freie Elektronen, doch das Feld der Raumladungszone treibt sie vom n- ins p-Gebiet zurück. Nur wenige schaffen es gegen das Feld.
--- falsch
Die Grenze sperrt, weil die Sperrspannung alle freien Elektronen aus dem n-Gebiet abzieht. Ohne Elektronen im n-Gebiet kann kein Strom über die Grenze fließen.
:::
:::karte begriff Injektion
Was bezeichnet man beim Transistor als Injektion, und wie hängt sie von $U_\mathrm{BE}$ ab?
---
Das Einbringen von Elektronen aus dem Emitter in die Basis, wenn $U_\mathrm{BE}$ die Barriere an der BE-Grenze senkt. Die Elektronendichte am Emitterrand der Basis wächst dabei mit $\mathrm{e}^{U_\mathrm{BE}/U_T}$.
--- falsch
Das Einbringen von Elektronen aus dem Kollektor in die Basis, wenn $U_\mathrm{CB}$ die Barriere an der CB-Grenze senkt. Die Elektronendichte in der Basis wächst dabei linear mit der Sperrspannung $U_\mathrm{CB}$.
--- falsch
Das Einbringen von Löchern über den Basisanschluss, die der Basisstrom liefert. Die Löcherdichte in der Basis wächst dabei linear mit $I_\mathrm{B}$, nicht mit $U_\mathrm{BE}$.
--- falsch
Das Einbringen von Elektronen aus dem Emitter in die Basis, wenn $U_\mathrm{BE}$ die Barriere hebt. Die Elektronendichte am Emitterrand der Basis sinkt dabei mit $\mathrm{e}^{-U_\mathrm{BE}/U_T}$.
:::
:::karte begriff Diffusionslänge
Was gibt die Diffusionslänge für Elektronen in der Basis an, und wie groß ist sie im Vergleich zur Basisbreite?
---
Die mittlere Strecke, die ein Elektron bis zur Rekombination zurücklegt, einige 10 µ m. Die Basis ist mit rund 1 µ m viel schmaler, deshalb kommen fast alle Elektronen durch.
--- falsch
Die Breite der Raumladungszone zwischen Emitter und Basis, rund 1 µ m. Die Basis ist mit einigen 10 µ m viel breiter, deshalb rekombinieren dort fast alle Elektronen.
--- falsch
Die mittlere Strecke, die ein Elektron bis zur Rekombination zurücklegt, rund 0,1 µ m. Die Basis ist zehnmal breiter, deshalb erreicht nur jedes zehnte Elektron den Kollektor.
--- falsch
Die Strecke, die ein Elektron im Feld der CB-Grenze zurücklegt, bevor es den Kollektor erreicht. Sie wächst mit $U_\mathrm{CB}$ und bestimmt, wie schnell der Transistor schaltet.
:::
:::karte zusammenhang Vier Schritte im Transistor
In welchen vier Schritten gelangen Elektronen im Normalbetrieb vom Emitter in den Kollektor, und was leistet dabei die Basis?
---
Injektion: $U_\mathrm{BE}$ senkt die Barriere, Elektronen gelangen in die Basis. Durchqueren: Sie diffundieren durch die schmale Basis. Absaugen: Das Feld der CB-Grenze zieht sie in den Kollektor. Nachliefern: Der Basisstrom ersetzt die verbrauchten Löcher.
--- falsch
Injektion: Der Basisstrom bringt Elektronen in die Basis. Durchqueren: Das Feld der BE-Grenze treibt sie hindurch. Absaugen: $U_\mathrm{CE}$ zieht sie in den Kollektor. Nachliefern: Der Emitter ersetzt die Elektronen, die über die Basis abfließen.
--- falsch
Injektion: $U_\mathrm{CB}$ senkt die Barriere am Kollektor. Durchqueren: Elektronen diffundieren vom Kollektor zum Emitter. Absaugen: Der Emitter nimmt sie auf. Nachliefern: Der Basisstrom bringt neue Elektronen in den Kollektor.
--- falsch
Injektion: $U_\mathrm{BE}$ senkt die Barriere, Elektronen gelangen in die Basis. Durchqueren: Fast alle rekombinieren dort mit Löchern. Absaugen: Der Basisanschluss zieht sie ab. Nachliefern: Der Kollektor liefert die fehlenden Elektronen nach.
:::
:::karte zusammenhang Absaugen am Kollektor
Warum hängt $I_\mathrm{C}$ im Normalbetrieb kaum von $U_\mathrm{CE}$ ab?
---
Am Kollektorrand erfasst das Feld der CB-Grenze jedes ankommende Elektron und zieht es in den Kollektor. Wie groß $U_\mathrm{CB}$ ist, spielt kaum eine Rolle, das Feld holt immer alle ab.
--- falsch
Die CB-Diode sperrt, deshalb fließt durch sie nur ein winziger Sperrstrom. Er hängt von $U_\mathrm{CB}$ nicht ab, und der Kollektorstrom ist genau dieser kleine Sperrstrom der gesperrten CB-Diode.
--- falsch
$U_\mathrm{CE}$ fällt fast ganz am Kollektorwiderstand ab, nicht am Transistor. Im Inneren kommt deshalb keine Spannung an, die den Strom verändern könnte.
--- falsch
Je größer $U_\mathrm{CB}$, desto stärker bremst das Feld die Elektronen. Dafür kommen mehr von ihnen an, und beide Wirkungen heben sich gerade auf.
:::
:::karte zusammenhang Woraus der Basisstrom besteht
Woraus besteht der Basisstrom eines Transistors, und warum bleibt er klein?
---
Löcher gelangen aus der Basis in den Emitter, und einige Elektronen rekombinieren in der Basis; der Basisanschluss ersetzt die verbrauchten Löcher. Er bleibt klein, weil der Emitter viel stärker dotiert und die Basis schmal ist.
--- falsch
Er besteht aus den Elektronen, die der Kollektor nicht abholt und die über die Basis abfließen. Er bleibt klein, weil die CB-Diode sperrt und deshalb nur ein winziger Sperrstrom fließt, der kaum von $U_\mathrm{BE}$ und gar nicht von der Basisbreite abhängt.
--- falsch
Er ist der Strom, der die Barriere an der BE-Grenze senkt, wie ein Steuerstrahl eine Klappe öffnet. Er bleibt klein, weil die Basis ein hochohmiges, schwach dotiertes Gebiet ist.
--- falsch
Er besteht aus Elektronen, die vom Basisanschluss in die Basis fließen und dort den Kollektorstrom auslösen. Er bleibt klein, weil jedes Elektron, das in die Basis fließt, dort durch Stöße viele weitere freisetzt.
:::
:::karte formel Ströme im Normalbetrieb
Wie hängen $I_\mathrm{C}$, $I_\mathrm{B}$ und $I_\mathrm{E}$ im Normalbetrieb von $U_\mathrm{BE}$ ab, und unter welchen Bedingungen gilt das?
---
$I_\mathrm{C}=I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{BE}/U_T}$, $I_\mathrm{B}=\frac{I_\mathrm{C}}{B}$, $I_\mathrm{E}=\Bigl(1+\frac1B\Bigr)I_\mathrm{C}$. Das gilt, wenn die BE-Diode mit $U_\mathrm{BE}\gg U_T$ leitet und der Kollektor über der Basis liegt, bei nicht zu großem Strom.
--- falsch
$I_\mathrm{C}=I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{BE}/U_T}$, $I_\mathrm{B}=B\,I_\mathrm{C}$, $I_\mathrm{E}=(1+B)\,I_\mathrm{C}$. Das gilt, wenn die BE-Diode mit $U_\mathrm{BE}\gg U_T$ leitet und der Kollektor über der Basis liegt. Dann holt der Kollektor alle Elektronen ab.
--- falsch
$I_\mathrm{C}=I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{CE}/U_T}$, $I_\mathrm{B}=\frac{I_\mathrm{C}}{B}$, $I_\mathrm{E}=\Bigl(1+\frac1B\Bigr)I_\mathrm{C}$. Das gilt, wenn beide Dioden leiten und der Kollektor unter der Basis liegt, bei jedem noch so großen Strom.
--- falsch
$I_\mathrm{C}=B\,\mathrm{e}^{U_\mathrm{BE}/U_T}$, $I_\mathrm{B}=I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{BE}/U_T}$, $I_\mathrm{E}=I_\mathrm{C}-I_\mathrm{B}$. Das gilt für jedes $U_\mathrm{BE}$, auch wenn die BE-Diode sperrt, weil die e-Funktion nie null wird.
:::
:::karte begriff Transferstrom
Was meint man, wenn man den Kollektorstrom als Transferstrom bezeichnet?
---
Den Kollektorstrom $I_\mathrm{C}=I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{BE}/U_T}$, so genannt, weil er durch die Basis hindurch vom Emitter zum Kollektor übertragen wird.
--- falsch
Den Basisstrom, so genannt, weil er die Steuerung von der Basis auf den Kollektor überträgt. Er ist der Anteil, der in der Basis rekombiniert.
--- falsch
Den Sperrstrom der CB-Diode, so genannt, weil er vom Kollektor in die Basis übertritt. Er hängt nicht von $U_\mathrm{BE}$ ab, sondern nur von $U_\mathrm{CB}$.
--- falsch
Den Kollektorstrom, so genannt, weil er Energie vom Eingangssignal auf den Ausgang überträgt. Er ist deshalb immer kleiner als der Basisstrom.
:::
:::karte begriff aktiver Bereich
Was kennzeichnet den aktiven Bereich eines npn-Transistors, und welche Gleichungen gelten dort?
---
Der Betriebszustand, in dem die BE-Diode mit $U_\mathrm{BE}\gg U_T$ leitet und der Kollektor über der Basis liegt, die CB-Diode also sperrt. Dort gelten $I_\mathrm{C}=I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{BE}/U_T}$ und $I_\mathrm{B}=I_\mathrm{C}/B$.
--- falsch
Der Betriebszustand, in dem BE-Diode und CB-Diode beide leiten, sodass der Strom ungehindert vom Kollektor zum Emitter fließt. Dort gelten $I_\mathrm{C}=I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{CE}/U_T}$ und $I_\mathrm{B}=0$.
--- falsch
Der Betriebszustand, in dem die BE-Diode sperrt und nur die CB-Diode leitet, weil der Kollektor unter der Basis liegt. Dort gilt $I_\mathrm{C}=B\,I_\mathrm{B}$ für jedes $U_\mathrm{BE}$.
--- falsch
Der Betriebszustand, in dem der Transistor seinen größten Strom führt, weil $U_\mathrm{CE}$ nahe null liegt. Dort gelten $I_\mathrm{C}=I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{BE}/U_T}$ und $I_\mathrm{B}=B\,I_\mathrm{C}$.
:::
:::karte zusammenhang Stromverstärkung
Woran liegt es, dass man sich beim Entwurf einer Schaltung nicht auf einen genauen Wert der Stromverstärkung $B$ verlassen kann?
---
$B$ hängt von Dotierung und Geometrie ab und streut: Exemplare eines Typs unterscheiden sich oft um den Faktor 2. Je nach Typ liegt der Wert zwischen 10 und 1000.
--- falsch
$B$ hängt stark von $U_\mathrm{BE}$ ab, weil Kollektor- und Basisstrom verschieden schnell mit der Spannung wachsen. Schon 18 mV mehr an der Basis verdoppeln deshalb $B$.
--- falsch
$B$ ändert sich mit $U_\mathrm{CE}$ um den Faktor 2 je Volt, weil das Feld der CB-Grenze mit der Spannung wächst. Bei festem $U_\mathrm{CE}$ ist $B$ dagegen genau bekannt.
--- falsch
$B$ hat die Einheit A/V und hängt deshalb vom gewählten Arbeitspunkt ab. Erst wenn der Arbeitspunkt feststeht, lässt sich $B$ aus dem Datenblatt ablesen.
:::
:::karte herleitung Basisstrom proportional zum Kollektorstrom
Wie folgt aus dem Überqueren derselben Barriere, dass das Verhältnis $B=I_\mathrm{C}/I_\mathrm{B}$ nicht von $U_\mathrm{BE}$ abhängt?
---
Elektronen aus dem Emitter und Löcher aus der Basis überqueren dieselbe Barriere an der BE-Grenze, weil $U_\mathrm{BE}$ sie für die Mehrheitsträger beider Seiten senkt.
---
Die Elektronendichte am Emitterrand der Basis und die Löcherdichte am Basisrand des Emitters wachsen deshalb beide mit $\mathrm{e}^{U_\mathrm{BE}/U_T}$, weil die Barriere für beide um dieselbe Spannung sinkt.
---
Der Kollektorstrom und die Rekombination in der Basis sind proportional zur ersten Dichte, der Löcherstrom in den Emitter zur zweiten, weil jeder Anteil von den Trägern lebt, die die Grenze überquert haben.
---
Alle Anteile tragen denselben Faktor $\mathrm{e}^{U_\mathrm{BE}/U_T}$, und er kürzt sich im Verhältnis $B=I_\mathrm{C}/I_\mathrm{B}$ heraus, weil der Basisstrom nur aus Rekombination und Löcherstrom besteht.
:::
:::karte zusammenhang Wer den Transistor steuert
Warum rechnet man in Schaltungen oft mit $I_\mathrm{B}$ als Steuergröße, obwohl physikalisch $U_\mathrm{BE}$ steuert?
---
Wegen $I_\mathrm{C}=B\,I_\mathrm{B}$ wirkt der Transistor wie eine stromgesteuerte Stromquelle. Beide Sichten beschreiben dieselbe Proportionalität; die über $I_\mathrm{B}$ ist bequem, wenn ein Widerstand den Basisstrom vorgibt.
--- falsch
Weil in Wahrheit der Basisstrom die Barriere senkt und $U_\mathrm{BE}$ nur dessen Folge ist. Die Sicht über $U_\mathrm{BE}$ ist eine Näherung, die nur für sehr kleine Ströme und tiefe Temperaturen gilt.
--- falsch
Weil $I_\mathrm{C}$ linear mit $U_\mathrm{BE}$ wächst und man deshalb ebenso gut den Basisstrom nehmen kann. Beide Sichten liefern aber verschiedene Kollektorströme, je nach Arbeitspunkt und Exemplar, weil $B$ streut.
--- falsch
Weil $U_\mathrm{BE}$ im Betrieb nie gemessen werden kann, $I_\mathrm{B}$ dagegen schon. Physikalisch wäre die Sicht über $U_\mathrm{BE}$ richtig, praktisch ist sie aber unbrauchbar.
:::
:::karte formel Empfindlichkeit der e-Funktion
Um wie viel muss $U_\mathrm{BE}$ steigen, damit sich $I_\mathrm{C}$ verdoppelt oder verzehnfacht, und warum gilt das bei jedem Strom?
---
Um $U_T\ln2$, rund 18 mV, für das Doppelte und um $U_T\ln10$, rund 60 mV, für das Zehnfache. Weil $I_\mathrm{C}$ exponentiell von $U_\mathrm{BE}$ abhängt, gehört zu einer festen Spannungsstufe immer derselbe Faktor.
--- falsch
Um $U_T\ln2$, rund 18 mV, für das Doppelte und um $10\,U_T\ln2$, rund 180 mV, für das Zehnfache. Das gilt aber nur bei 2 mA, weil die Kurve bei anderen Strömen anders gekrümmt ist und andere Stufen braucht.
--- falsch
Um 0,6 V für das Doppelte und um 6 V für das Zehnfache, weil $I_\mathrm{C}$ proportional zu $U_\mathrm{BE}$ ist. Bei jedem Strom gehört deshalb zur doppelten Spannung der doppelte Strom.
--- falsch
Um $U_T$, also 26 mV, für das Doppelte und um $10\,U_T$ für das Zehnfache, weil sich der Strom je $U_T$ genau verdoppelt. Bei kleinen Strömen sind die nötigen Stufen größer.
:::
:::karte zusammenhang Leistung am Ausgang
Woher kommt die zusätzliche Leistung am Ausgang eines Transistors, wenn das Eingangssignal nur wenig liefert?
---
Aus der Versorgung $U_\mathrm{CC}$: Der Kollektorstrom läuft durch den Ausgangskreis, und die Quelle gibt $U_\mathrm{CC}I_\mathrm{C}$ ab. Das Eingangssignal bezahlt nur $U_\mathrm{BE}I_\mathrm{B}$ und entscheidet damit, wie viel die Quelle liefert.
--- falsch
Aus dem Transistor selbst: Jedes Elektron, das die Basis durchquert, nimmt dort Energie aus dem Kristallgitter auf. Das Eingangssignal liefert nur den Anstoß, die Versorgung trägt zur Ausgangsleistung nichts bei.
--- falsch
Aus dem Eingangssignal: Der Transistor sammelt dessen Leistung über viele Perioden und gibt sie gebündelt am Ausgang ab. Im Mittel ist die Leistung am Ausgang deshalb gleich der am Eingang.
--- falsch
Aus der Versorgung $U_\mathrm{CC}$, aber nur über den Basisstrom: Die Quelle gibt $U_\mathrm{CC}I_\mathrm{B}$ ab, und der Transistor verstärkt genau diese Leistung um den Faktor $B$ und gibt sie an den Ausgang weiter.
:::
::::

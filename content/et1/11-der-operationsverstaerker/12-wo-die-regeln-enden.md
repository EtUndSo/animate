---
title: Stufe 10: Wo die Regeln enden
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Der Operationsverstärker
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-operationsverstarker
knoten: Kapitel 11: Der Operationsverstärker
order: 1211200
summary: Bis hier war der OPV bis auf A und die Anschläge ideal.
tags: Offsetspannung, Eingangsruhestrom, Gleichtaktunterdrückung, Transitfrequenz, Anstiegsrate, übersteuert
lang: de
---

<span class="anker" id="stufe-10"></span>

:::zweck
Bis hier war der OPV bis auf $A$ und die Anschläge ideal. Diese Stufe ordnet die realen Abweichungen nach Größe und fasst das Vorgehen zusammen.
:::

**Die Idee.** Reale Abweichungen wirken auf zwei Wegen. Die einen verschieben den Punkt, auf den die Schleife regelt: Die Transistoren T1 und T2 sind nie exakt gleich, also ist nicht $U_\mathrm{D}=0$ der Ruhepunkt, sondern $U_\mathrm{D}=U_\mathrm{off}$. Die anderen verkleinern die Reserve $A\beta$. Vor allem die Frequenz: Damit die Schleife nicht schwingt, begrenzt eine innere Kapazität die Bandbreite. Die Spannung an ihr kann bei schnellen Signalen nicht folgen, $A$ fällt.

| Größe | Ursache | Wirkung im Rechenmodell |
|---|---|---|
| $A$ endlich, $10^5$ bis $10^6$ | Begrenzte Stufenverstärkung | Abweichung $1/(A\beta)=0{,}005$ % |
| __Offsetspannung__ $U_\mathrm{off}$ | Ungleiche Eingangstransistoren, ändert sich mit Temperatur, Versorgung, Alter | Am Ausgang $U_\mathrm{off}/\beta=5$ mV, auch bei $U_\mathrm{E}=0$ |
| __Eingangsruhestrom__ $I_\mathrm{B}$ | Basisströme von T1 und T2 | Durch $R_2$: $I_\mathrm{B}R_2=2$ mV |
| Gleichtakt | Reale Stromquelle T3, ungleiche Zweige | siehe unten |
| $A(f)$ | Innere Kapazität | $\vert A(f)\vert \approx f_\mathrm{T}/f$, siehe unten |
| Ausgang | Transistoren der Endstufe | $\pm11$ V, 20 mA, $r_\mathrm{a}/(1+A\beta)=3{,}75$ m$\Omega$ |
| Rauschen | Eigene Transistoren | 10 nV/$\sqrt{\text{Hz}}$: 1,41 µ V in 20 kHz |

Der Offset ist die Eingangsspannung, bei der der Ausgang null wird. In der Schleife stellt sich $\varphi_+-\varphi_-=U_\mathrm{off}$ ein, der Teiler vergrößert das um $1/\beta$. Das eigene Rauschen des OPV addiert sich quadratisch zum Sensor aus Stufe [1](rauschen.html#stufe-1): 2,31 µ V statt 1,82 µ V, das SNR sinkt um 2,1 dB auf 52,7 dB.

:::definition Definition 10.1 (Gleichtaktunterdrückung)
<span class="anker" id="satz-10-1"></span>

Die __Gleichtaktunterdrückung__ CMRR (common mode rejection ratio) vergleicht die Verstärkung der Differenz mit der des Gleichtakts:

<span class="anker" id="gl-10-1"></span>
$$\mathrm{CMRR}=\frac{A}{A_\mathrm{gl}},\qquad \mathrm{CMRR}_\mathrm{dB}=20\lg\frac{A}{A_\mathrm{gl}}. \tag{10.1}$$

Ideal ist $\mathrm{CMRR}\to\infty$, üblich sind 60 dB ($A_\mathrm{gl}/A=10^{-3}$) bis 120 dB ($10^{-6}$).
:::

⁠**So liest man das:** Mechanismus: Ein realer T3 hat ein endliches $r_\mathrm{CE}$. Steigt der Gleichtakt, steigt E, und der Summenstrom wächst um $U_\mathrm{gl}/r_\mathrm{CE}$. Bei der Differenzstufe aus Stufe [2](der-differenzverstarker.html#stufe-2) mit $r_\mathrm{CE}=40$ k$\Omega$ ändert sich jeder Kollektor mit dem Faktor $R_\mathrm{C}/(2r_\mathrm{CE})=0{,}0375$ gegen 57,7 bei der Differenz: 63,7 dB. Im Rechenmodell sind es 90 dB, also $A_\mathrm{gl}=3{,}16$. Am Subtrahierer aus Stufe [6](mehrere-eingange-mehrere-stufen.html#stufe-6) wirken 2 V Gleichtakt wie $2\,\mathrm{V}/31600=63$ µ V Differenz, das sind 0,32 mV am Ausgang, 0,16 % der gemessenen 0,2 V.

**Die Frequenz.** Oberhalb von $f_A=f_\mathrm{T}/A=10$ Hz fällt $A$ um den Faktor 10 je Dekade, $|A(f)|\approx f_\mathrm{T}/f$. Bei der __Transitfrequenz__ $f_\mathrm{T}$ ist $|A|=1$. Die Schleife wirkt, solange $|A(f)|\,\beta\gg1$ ist. Die Reserve ist bei $f_G=\beta\,f_\mathrm{T}$ aufgebraucht:

<span class="anker" id="gl-10-2"></span>
$$|G(f)|=\frac{1/\beta}{\sqrt{1+(f/f_G)^2}},\qquad f_G=\beta\,f_\mathrm{T},\qquad G\,f_G=f_\mathrm{T}. \tag{10.2}$$

⁠**So liest man das:** Mit $G=5$ reicht die Bandbreite bis 200 kHz. Das Produkt aus Verstärkung und Bandbreite ist fest: Mit $G=1$ wären es 1 MHz, mit $G=100$ nur 10 kHz. Die Zeitkonstante $\tau_G=0{,}80$ µ s aus Stufe [4](gegenkopplung.html#stufe-4) ist derselbe Wert: $1/(2\pi\cdot200\,\mathrm{kHz})$. **Grenzfall:** Für $f\gg f_G$ ist $|G|\to|A|$, die Rückführung wirkt nicht mehr.

:::abbildung et1/k11bode 12
Leerlaufverstärkung und Verstärkung der Schaltung über der Frequenz, beide Achsen logarithmisch. Der Abstand der Kurven ist die Reserve $|A|\beta$. Sie ist bei 1 kHz noch 200 und bei 200 kHz aufgebraucht.
:::

:::ltspice Bandbreite und Einrasten
⁠**Zeichnen:** Symbol `UniversalOpAmp2` (Ordner OpAmps) mit `Avol=100k GBW=1Meg Slew=0.5Meg`, `Ilimit=20m Rail=1`, Versorgung `voltage` $\pm12$. Beschaltung wie im Kasten in Stufe [4](gegenkopplung.html#stufe-4), `VE` mit `AC 1`.

⁠**Direktiven:** `.ac dec 50 1 10Meg`, `.meas ac g0 FIND mag(V(a)) AT=10`, `.meas ac fg WHEN mag(V(a))=g0/sqrt(2)`.

⁠**Was du siehst:** `fg` = 199 kHz gegen 200 kHz in der Rechnung. Tausche dann die Eingänge, gib `VE` den Wert `PULSE(-3 3 1m 1u 1u 1m 2m)` und rechne `.tran 4m`: `V(a)` springt zwischen $\pm10{,}98$ V. Mit $\pm1$ V statt $\pm3$ V bleibt der Ausgang stehen, das ist die Hysterese aus Stufe [9](mitkopplung-und-der-schmitt-trigger.html#stufe-9). Setze für Aufgabe [11](#aufg-11) `R1` auf 1k und `R2` auf 100k.
:::

:::zusatz Anstiegsrate
Der innere Ladestrom ist begrenzt. Darum hat der Ausgang eine höchste Geschwindigkeit, die __Anstiegsrate__, typisch 0,5 V/µ s. Der Sprung aus Abb. [5](gegenkopplung.html#abb-5) dauert damit real rund 10 µ s statt weniger µ s. Ein Sinus mit 11 V Amplitude bleibt nur bis rund 7,2 kHz unverzerrt, obwohl die Bandbreite viel größer ist.
:::

:::merke Das Rechenschema
<ol>

<li>

⁠**Keine Rückführung** (Komparator): $U_\mathrm{A}=U_\mathrm{A,max}$ oder $U_\mathrm{A,min}$, $U_\mathrm{D}\ne0$.

</li>

<li>

⁠**Vorzeichen prüfen:** Hebe den Ausgang in Gedanken. Sinkt $U_\mathrm{D}$, ist es Gegenkopplung, steigt es, Mitkopplung.

</li>

<li>

⁠**Gegenkopplung:** $U_\mathrm{D}=0$ annehmen, mit Knotenregel und ohmschem Gesetz $U_\mathrm{A}$ berechnen. Liegt es in den Grenzen, ist die Rechnung gültig. Sonst ist der OPV __übersteuert__: $U_\mathrm{A}$ steht am Anschlag, $U_\mathrm{D}\ne0$, und man rechnet das Netz mit diesem festen $U_\mathrm{A}$.

</li>

<li>

⁠**Mitkopplung:** In der Regel $U_\mathrm{A}$ am Anschlag, $U_\mathrm{D}\ne0$. Die Schwellen folgen aus dem Vorzeichenwechsel von $U_\mathrm{D}$.

</li>

<li>

⁠**Genauigkeit:** $1/(A\beta)$ bei der Signalfrequenz, $U_\mathrm{off}/\beta$ und $I_\mathrm{B}R_2$ am Ausgang.

</li>

</ol>
:::

:::aufgabe Aufgabe 11 ★★★ Messverstärker
<span class="anker" id="aufg-11"></span>

Ein Sensor mit 10 mV soll mit V auf rund 1 V verstärkt werden: $R_1=1$ k$\Omega$, $R_2=100$ k$\Omega$, nicht-invertierend. (a) Wie groß sind $\beta$, $G$ und die Abweichung durch $A$? (b) Bis zu welcher Frequenz reicht die Schaltung? Wie groß ist $|G|$ bei 5 kHz? (c) Wie groß ist der Offset am Ausgang, und welchen Anteil hat er am Signal? Wie viel kommt durch $I_\mathrm{B}$ dazu? (d) Bis zu welchem Eingang reicht der Ausgang? (e) Ein Integrierer mit $R\,C=10$ ms hat denselben Offset. Wie schnell läuft sein Ausgang bei $U_\mathrm{E}=0$, und wann schlägt er an?

:::loesung
(a) $\beta=1/101$, $G\approx101$, Abweichung $101/A=0{,}10$ %. (b) $f_G=1\,\mathrm{MHz}/101=9{,}9$ kHz. $|G(5\,\mathrm{kHz})|=101/\sqrt{1+(5/9{,}9)^2}=90{,}2$. Eine solche Schaltung verliert schon bei 5 kHz ein Zehntel. (c) $101\cdot1\,\mathrm{mV}=101$ mV, also 10 % des Signals von 1,01 V. Dazu $I_\mathrm{B}R_2=5$ mV. (d) $11\,\mathrm{V}/101=109$ mV. (e) $1\,\mathrm{mV}/10\,\mathrm{ms}=0{,}1$ V/s, nach 110 s am Anschlag. Ein realer Integrierer braucht deshalb einen Rücksetzschalter oder einen großen Widerstand parallel zu $C$.
:::
:::

::::formelsammlung
**Fehlerbeiträge**

$$1/(A\beta),\qquad U_\mathrm{off}/\beta,\qquad I_\mathrm{B}R_2$$

Relative Abweichung durch endliches $A$ bei der Signalfrequenz; Offsetspannung und Eingangsruhestrom als Spannungen am Ausgang des nicht-invertierenden Verstärkers.

**Gleichtaktunterdrückung**

$$\mathrm{CMRR}=\frac{A}{A_\mathrm{gl}},\qquad \mathrm{CMRR}_\mathrm{dB}=20\lg\frac{A}{A_\mathrm{gl}}$$

Ideal $\mathrm{CMRR}\to\infty$, üblich 60 bis 120 dB.

**Gleichtakt in der realen Differenzstufe**

$$R_\mathrm{C}/(2r_\mathrm{CE})$$

Faktor, mit dem sich jeder Kollektor bei Gleichtakt ändert, wenn T3 ein endliches $r_\mathrm{CE}$ hat; der Summenstrom wächst um $U_\mathrm{gl}/r_\mathrm{CE}$.

**Leerlaufverstärkung über der Frequenz**

$$|A(f)|\approx f_\mathrm{T}/f,\qquad f_A=f_\mathrm{T}/A$$

Oberhalb von $f_A$ fällt $A$ um den Faktor 10 je Dekade; bei der Transitfrequenz $f_\mathrm{T}$ ist $|A|=1$.

**Frequenzgang der gegengekoppelten Schaltung**

$$|G(f)|=\frac{1/\beta}{\sqrt{1+(f/f_G)^2}},\qquad f_G=\beta\,f_\mathrm{T},\qquad G\,f_G=f_\mathrm{T}$$

Die Schleife wirkt, solange $|A(f)|\,\beta\gg1$ ist; für $f\gg f_G$ geht $|G|\to|A|$.
::::

::::lernkarten
:::karte zusammenhang Zwei Wege realer Abweichungen
Wie wirken reale Abweichungen eines OPV auf den Punkt, auf den die Schleife regelt, und auf ihre Reserve $A\beta$?
---
Die einen verschieben den Ruhepunkt auf $U_\mathrm{D}=U_\mathrm{off}$, weil die Eingangstransistoren nie gleich sind. Die anderen verkleinern $A\beta$, vor allem die Frequenz, weil $A$ dann fällt.
--- falsch
Sie verkleinern alle nur $A$; der Ruhepunkt der Schleife bleibt immer bei $U_\mathrm{D}=0$, weil die Gegenkopplung ihn unabhängig vom Bauteil erzwingt und jeden Versatz ausregelt.
--- falsch
Die Frequenz verschiebt den Ruhepunkt, weil $A$ fällt; ungleiche Eingangstransistoren verkleinern dagegen die Reserve $A\beta$, weil sie $A$ senken und die Schleife schwächen.
--- falsch
Mit Gegenkopplung werden alle realen Abweichungen um den Faktor $1+A\beta$ geschwächt; sie zählen deshalb nur bei einem OPV ohne Rückführung, etwa beim Komparator oder beim Schmitt-Trigger.
:::
:::karte begriff Offsetspannung
Was ist die Offsetspannung eines OPV, und woher kommt sie?
---
Die Eingangsspannung, bei der der Ausgang null wird. Sie entsteht, weil die Eingangstransistoren nie exakt gleich sind, und ändert sich mit Temperatur, Versorgung und Alter.
--- falsch
Die Spannung am Ausgang ohne Eingangssignal; bei einem guten OPV ist sie genau 0 V, sonst entsteht sie nur durch das Rauschen der Transistoren.
--- falsch
Die kleinste Eingangsspannung, die der OPV überhaupt verstärkt, rund 1 mV; darunter bleibt der Ausgang wegen einer Schwelle der Transistoren auf null.
--- falsch
Die Eingangsspannung, bei der der Ausgang null wird; sie ist ein fester Wert des Exemplars, der sich mit Temperatur, Versorgung und Alter nicht ändert und deshalb einmal abgeglichen wird.
:::
:::karte begriff Eingangsruhestrom
Was ist der Eingangsruhestrom $I_\mathrm{B}$ eines OPV, und warum gibt es ihn?
---
Der Strom, den die Eingänge auch ohne Signal ziehen, im Rechenmodell 50 nA. Es sind die Basisströme der Eingangstransistoren T1 und T2.
--- falsch
Der Strom, den der OPV ohne Last aus seiner Versorgung zieht; er heizt das Bauteil im Ruhezustand und fließt nicht durch die Eingänge.
--- falsch
Der Strom, der wegen der Offsetspannung über $r_\mathrm{e}$ fließt, also 1 nA; ohne Offsetspannung wäre der Eingangsruhestrom null.
--- falsch
Der Kollektorstrom der Eingangstransistoren T1 und T2, je 1 mA; er fließt aus den Eingängen heraus in die Signalquelle.
:::
:::karte formel Fehler durch Offset und Eingangsruhestrom
Wie groß sind die Fehler, die Offsetspannung und Eingangsruhestrom am Ausgang eines nicht-invertierenden Verstärkers erzeugen?
---
Der Offset erscheint am Ausgang als $U_\mathrm{off}/\beta$, im Rechenmodell 5 mV, auch bei $U_\mathrm{E}=0$. Der Eingangsruhestrom fließt durch $R_2$ und gibt $I_\mathrm{B}R_2$, hier 2 mV.
--- falsch
Der Offset erscheint unverstärkt als $U_\mathrm{off}=1$ mV, weil die Schleife ihn nicht vergrößert; der Eingangsruhestrom gibt $I_\mathrm{B}R_1$, hier 0,5 mV, weil er durch $R_1$ nach Masse fließt.
--- falsch
Der Offset erscheint als $A\,U_\mathrm{off}$, also 100 V, und treibt den Ausgang an den Anschlag; der Eingangsruhestrom spielt daneben keine Rolle.
--- falsch
Der Offset erscheint als $U_\mathrm{off}\,\beta$, hier 0,2 mV; der Eingangsruhestrom gibt $I_\mathrm{B}R_2$, hier 2 mV, aber nur, solange $U_\mathrm{E}\ne0$ ist.
:::
:::karte begriff Gleichtaktunterdrückung
Was gibt die Gleichtaktunterdrückung CMRR eines OPV an, und welche Werte sind üblich?
---
Das Verhältnis von Differenz- zu Gleichtaktverstärkung, $\mathrm{CMRR}=\frac{A}{A_\mathrm{gl}}$, in Dezibel $\mathrm{CMRR}_\mathrm{dB}=20\lg\frac{A}{A_\mathrm{gl}}$. Ideal ist $\mathrm{CMRR}\to\infty$, üblich sind 60 bis 120 dB.
--- falsch
Sie ist das Verhältnis der Gleichtaktverstärkung zur Differenzverstärkung, $A_\mathrm{gl}/A$; ideal ist es unendlich groß, weil der Gleichtakt dann voll durchkommt, üblich sind 60 bis 120 dB.
--- falsch
Sie vergleicht die Verstärkung der Differenz mit der des Gleichtakts, in Dezibel $10\lg\frac{A}{A_\mathrm{gl}}$; ideal ist null, üblich sind 3 bis 6 dB.
--- falsch
Sie gibt die größte Gleichtaktspannung an, die der OPV verarbeitet, ohne anzuschlagen; ideal ist sie unendlich, üblich sind 60 bis 120 V.
:::
:::karte zusammenhang Gleichtakt in der realen Differenzstufe
Warum dringt bei einer realen Differenzstufe ein Teil des Gleichtakts zum Ausgang durch?
---
Ein realer T3 hat ein endliches $r_\mathrm{CE}$: Steigt der Gleichtakt, steigt E, und der Summenstrom wächst um $U_\mathrm{gl}/r_\mathrm{CE}$. Jeder Kollektor ändert sich dann mit dem Faktor $R_\mathrm{C}/(2r_\mathrm{CE})$.
--- falsch
Die Kollektorwiderstände sind nie exakt gleich; 1 % Unterschied lässt 1 % des Gleichtakts durch, die Stromquelle T3 spielt dafür keine Rolle, solange sie überhaupt einen Strom liefert und nicht sperrt.
--- falsch
Der Gleichtakt verschiebt die Basisströme, die an den Innenwiderständen der Quellen eine Spannung erzeugen; genau diese erscheint am Ausgang.
--- falsch
Ein realer T3 hat ein endliches $r_\mathrm{CE}$: Steigt der Gleichtakt, sinkt E, und der Summenstrom fällt auf null, bis der Gleichtakt zurückgeht und T3 wieder leitet.
:::
:::karte zusammenhang Transitfrequenz
Warum fällt die Leerlaufverstärkung eines OPV oberhalb von $f_A=f_\mathrm{T}/A$, und was gibt die Transitfrequenz $f_\mathrm{T}$ dabei an?
---
Damit die Schleife nicht schwingt, begrenzt eine innere Kapazität die Bandbreite. $A$ fällt um den Faktor 10 je Dekade, $|A(f)|\approx f_\mathrm{T}/f$, und bei der Transitfrequenz ist $|A|=1$.
--- falsch
Die Eingangstransistoren sind für höhere Frequenzen zu langsam; $A$ fällt deshalb sprunghaft auf 1, und zwar genau bei der Transitfrequenz von rund 10 Hz.
--- falsch
Die Transitfrequenz ist die Frequenz, ab der $A$ zu fallen beginnt, hier 1 MHz; darunter bleibt $A$ konstant 100000, darüber fällt es schnell auf null.
--- falsch
Eine innere Kapazität begrenzt die Bandbreite; $A$ fällt um den Faktor 2 je Dekade, und bei der Transitfrequenz ist $A$ auf die Hälfte gefallen, also auf 50000.
:::
:::karte formel Frequenzgang der gegengekoppelten Schaltung
Wie hängt der Betrag der Verstärkung $|G(f)|$ eines gegengekoppelten Verstärkers von der Frequenz ab, und bis wohin reicht seine Bandbreite?
---
$|G(f)|=\frac{1/\beta}{\sqrt{1+(f/f_G)^2}}$ mit $f_G=\beta\,f_\mathrm{T}$. Das Produkt ist fest, $G\,f_G=f_\mathrm{T}$: Mit $G=5$ reicht die Bandbreite bis 200 kHz.
--- falsch
$|G(f)|=\frac{1/\beta}{\sqrt{1+(f/f_G)^2}}$ mit $f_G=f_\mathrm{T}/\beta$: Je größer $G$, desto größer die Bandbreite, mit $G=5$ also 5 MHz.
--- falsch
$|G(f)|=1/\beta$ für alle Frequenzen bis $f_\mathrm{T}$: Die Gegenkopplung gleicht den Abfall von $A$ vollständig aus, die Bandbreite ist immer 1 MHz.
--- falsch
$|G(f)|=\frac{1/\beta}{1+f/f_G}$ mit $f_G=\beta\,f_\mathrm{T}$: Das Produkt $G\,f_G$ wächst mit $G$, mit $G=100$ sind es 100 MHz.
:::
:::karte zusammenhang Reserve aufgebraucht
Was passiert mit der Wirkung der Rückführung, wenn die Frequenz weit über $f_G$ steigt?
---
Die Schleife wirkt nur, solange $|A(f)|\,\beta\gg1$ ist; bei $f_G$ ist diese Reserve aufgebraucht. Für $f\gg f_G$ ist $|G|\to|A|$, die Rückführung wirkt nicht mehr.
--- falsch
Die Rückführung wird stärker, weil die innere Kapazität sie bei hohen Frequenzen kurzschließt; $|G|$ fällt deshalb auf null.
--- falsch
Nichts: Die Verstärkung bleibt $1/\beta$, weil die Widerstände der Rückführung nicht von der Frequenz abhängen.
--- falsch
Die Schleife wird zur Mitkopplung, weil sich das Vorzeichen bei hohen Frequenzen umkehrt; der Ausgang läuft an einen Anschlag.
:::
:::karte begriff Anstiegsrate
Was ist die Anstiegsrate eines OPV, und warum begrenzt sie einen Sinus mit großer Amplitude?
---
Die höchste Geschwindigkeit, mit der sich der Ausgang ändern kann, 0,5 V/µ s. Ein Sinus mit 11 V Amplitude bleibt deshalb nur bis rund 7,2 kHz unverzerrt.
--- falsch
Die Frequenz, bis zu der der OPV überhaupt verstärkt, typisch 0,5 MHz; ein Sinus jeder Amplitude bleibt bis zu dieser Frequenz unverzerrt und darüber abgeschnitten.
--- falsch
Die Geschwindigkeit, mit der $A$ über der Frequenz fällt, der Faktor 10 je Dekade; sie gilt nur für kleine Signale und begrenzt große nicht.
--- falsch
Die höchste Änderungsgeschwindigkeit des Ausgangs, typisch 0,5 V/µ s; sie hängt nur von der Gegenkopplung ab und ist bei $G=1$ unbegrenzt und bei großem $G$ am kleinsten.
:::
:::karte begriff übersteuert
Wann nennt man einen gegengekoppelten OPV übersteuert, und wie rechnet man die Schaltung dann?
---
Wenn die mit $U_\mathrm{D}=0$ berechnete Ausgangsspannung außerhalb der Grenzen liegt. Dann steht $U_\mathrm{A}$ am Anschlag, und man rechnet das Netz mit diesem festen Wert.
--- falsch
Wenn am Eingang mehr als 1 V liegt; dann rechnet man mit der halben Verstärkung weiter, weil die Kennlinie des Ausgangs abflacht und $A$ dort halbiert ist.
--- falsch
Wenn der Ausgangsstrom über 20 mA steigt; dann gilt weiter $U_\mathrm{D}=0$, und nur die Ausgangsspannung sinkt um $r_\mathrm{a}$ mal Strom.
--- falsch
Wenn die berechnete Ausgangsspannung außerhalb der Grenzen liegt; man rechnet dann weiter mit $U_\mathrm{D}=0$ und setzt den Anschlag nur beim Strom ein.
:::
:::karte zusammenhang Vorzeichen der Rückführung prüfen
Woran erkennt man in einer OPV-Schaltung, ob die Rückführung gegenkoppelt oder mitkoppelt, und was folgt daraus für die Rechnung?
---
Man hebt den Ausgang in Gedanken. Sinkt dadurch $U_\mathrm{D}$, ist es Gegenkopplung; steigt $U_\mathrm{D}$, ist es Mitkopplung, und der Ausgang steht am Anschlag.
--- falsch
Man schaut, an welchem Eingang $U_\mathrm{E}$ liegt: Am Plus-Eingang ist es immer Gegenkopplung, am Minus-Eingang immer Mitkopplung.
--- falsch
Man hebt den Ausgang in Gedanken. Steigt dadurch $U_\mathrm{D}$, ist es Gegenkopplung, weil der Ausgang nachregeln kann; sinkt es, ist es Mitkopplung mit Hysterese.
--- falsch
Man zählt die Widerstände in der Rückführung: Einer bedeutet Gegenkopplung, zwei oder mehr bedeuten Mitkopplung mit Hysterese und zwei Schwellen.
:::
:::karte zusammenhang Eigenrauschen des OPV
Wie verändert das Eigenrauschen des OPV das Signal-Rausch-Verhältnis des Sensors aus dem Rechenmodell?
---
Die 1,41 µ V des OPV addieren sich quadratisch zu den 1,82 µ V des Sensors, zusammen 2,31 µ V. Das SNR sinkt um 2,1 dB auf 52,7 dB.
--- falsch
Die Rauschspannungen addieren sich linear zu 3,23 µ V; das SNR sinkt dadurch um 5,0 dB auf 49,8 dB.
--- falsch
Gar nicht: Der OPV verstärkt Signal und Rauschen um denselben Faktor, sein eigenes Rauschen fällt dabei heraus wie ein Gleichtakt.
--- falsch
Das kleinere Rauschen des OPV wird vom größeren des Sensors verdeckt; es zählt nur der größere Wert, das SNR bleibt bei 54,8 dB.
:::
:::karte zusammenhang Offset am Integrierer
Warum braucht ein realer Integrierer einen Rücksetzschalter oder einen großen Widerstand parallel zu $C$?
---
Der Offset wirkt wie eine kleine feste Eingangsspannung, die er auch bei $U_\mathrm{E}=0$ integriert. Mit 1 mV und $R\,C=10$ ms läuft der Ausgang mit 0,1 V/s und schlägt nach 110 s an.
--- falsch
Der Kondensator entlädt sich sonst über den Eingang des OPV; ohne diese Bauteile verliert der Integrierer seinen Wert nach wenigen Sekunden.
--- falsch
Der Rauschstrom der Eingänge lädt den Kondensator in wenigen Mikrosekunden auf; ohne Rücksetzen stünde der Ausgang immer am Anschlag.
--- falsch
Der Eingangsruhestrom fließt sonst in den Ausgang; ohne zusätzlichen Weg würde der OPV überhitzen, weil der Strom nirgends abfließen kann.
:::
::::

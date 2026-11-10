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

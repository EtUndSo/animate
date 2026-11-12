---
title: Stufe 10: Drei Grundschaltungen
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Der Bipolartransistor
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor
knoten: Kapitel 10: Der Bipolartransistor
order: 1201200
summary: Eingang und Ausgang brauchen je zwei Klemmen, der Transistor hat insgesamt drei.
tags: Emitterschaltung, Kollektorschaltung, Emitterfolger, Basisschaltung, Spannungshub, Puffer
lang: de
---

<span class="anker" id="stufe-10"></span>

:::zweck
Eingang und Ausgang brauchen je zwei Klemmen, der Transistor hat insgesamt drei. Ein Anschluss wird also für das Signal gemeinsam. Diese Stufe rechnet die drei Möglichkeiten aus.
:::

**Die Idee.** Der gemeinsame Anschluss gibt der Schaltung den Namen (Abb. [12](#abb-12)). In der __Emitterschaltung__ kommt das Signal an die Basis und geht vom Kollektor weg. $u_\mathrm{ein}$ liegt voll an der BE-Strecke und erzeugt $i_\mathrm{c}=S\,u_\mathrm{ein}$. Dieser Strom fließt durch $R_\mathrm{C}$ und zieht das Kollektorpotenzial herab: Der Ausgang ist invertiert. In der __Kollektorschaltung__ kommt das Signal an die Basis und geht vom Emitter weg. Der Emitter folgt der Basis: Stünde er still, änderte sich $U_\mathrm{BE}$, und der entstehende Strom höbe ihn über $R_\mathrm{E}$ sofort nach. Deshalb heißt sie auch __Emitterfolger__. In der __Basisschaltung__ liegt die Basis fest, das Signal kommt an den Emitter. Sinkt der Emitter, steigt $U_\mathrm{BE}$, mehr Strom zieht den Kollektor herab: Ein- und Ausgang bewegen sich gleichsinnig. Der Betrag entspricht der Emitterschaltung.

:::abbildung et1/k10grundschaltungen 12
Oben die drei Grundschaltungen, unten ihre Kennlinien aus dem Rechenmodell mit $U_\mathrm{CC}=12$ V. Emitterschaltung ($R_\mathrm{C}=3$ k$\Omega$): fallend, steil um 0,6 V. Kollektorschaltung ($R_\mathrm{E}=3$ k$\Omega$): Der Ausgang liegt rund 0,6 V unter dem Eingang (grau). Basisschaltung: wie die Emitterschaltung, an der senkrechten Achse gespiegelt, steigend.
:::

:::satz Satz 10.1 (Spannungsverstärkung der Grundschaltungen)
<span class="anker" id="satz-10-1"></span>

Für kleine Signale im aktiven Bereich, $r_\mathrm{CE}$ vernachlässigt, $A=u_\mathrm{aus}/u_\mathrm{ein}$:

<span class="anker" id="gl-10-1"></span>
$$A_\mathrm{Emitter}=-S\,R_\mathrm{C}=-\frac{U_{R_\mathrm{C}}}{U_T},\qquad A_\mathrm{Kollektor}=\frac{S\,R_\mathrm{E}}{1+S\,R_\mathrm{E}}<1,\qquad A_\mathrm{Basis}=+S\,R_\mathrm{C}. \tag{10.1}$$

Mit Emitterwiderstand ist $A=-R_\mathrm{C}/(R_\mathrm{E}+1/S)\approx-R_\mathrm{C}/R_\mathrm{E}$, mit $r_\mathrm{CE}$ ist $A_\mathrm{Emitter}=-S\,(R_\mathrm{C}\parallel r_\mathrm{CE})$.
:::

⁠**So liest man das:** $U_{R_\mathrm{C}}=I_\mathrm{C}R_\mathrm{C}$ ist die Gleichspannung am Kollektorwiderstand, 6 V im Rechenmodell. **Kurz gesagt:** Die Verstärkung der Emitterschaltung ist die Gleichspannung am Kollektorwiderstand geteilt durch $U_T$. Weder $B$ noch der Transistortyp kommen darin vor. **Gültigkeit:** $|u_\mathrm{be}|\ll U_T$, $R_\mathrm{C}\ll r_\mathrm{CE}$, Ansteuerung durch eine Quelle mit kleinem Innenwiderstand.

:::herleitung Drei Maschen im Kleinsignal
$U_\mathrm{CC}$ ist für das Signal Masse. Emitterschaltung: $u_\mathrm{be}=u_\mathrm{ein}$, $u_\mathrm{aus}=-R_\mathrm{C}i_\mathrm{c}=-R_\mathrm{C}S\,u_\mathrm{ein}$, und mit $S=I_\mathrm{C}/U_T$ folgt $S\,R_\mathrm{C}=I_\mathrm{C}R_\mathrm{C}/U_T$. Mit Emitterwiderstand: $u_\mathrm{ein}=u_\mathrm{be}+R_\mathrm{E}S\,u_\mathrm{be}$, der Großteil von $u_\mathrm{ein}$ liegt an $R_\mathrm{E}$, und der Rest $u_\mathrm{be}=u_\mathrm{ein}/(1+S\,R_\mathrm{E})$ steuert. Kollektorschaltung: $u_\mathrm{aus}=R_\mathrm{E}S\,u_\mathrm{be}$ mit $u_\mathrm{be}=u_\mathrm{ein}-u_\mathrm{aus}$, auflösen. Basisschaltung: Die Basis ruht, also $u_\mathrm{be}=-u_\mathrm{ein}$ und $u_\mathrm{aus}=-R_\mathrm{C}S\,u_\mathrm{be}=+S\,R_\mathrm{C}u_\mathrm{ein}$.
:::

::::beispiel
Emitterschaltung im Punkt A: $A=-6\,\mathrm{V}/26\,\mathrm{mV}=-231$, mit $r_\mathrm{CE}$ genauer $-215$. Aus 1 mV am Eingang werden 0,23 V am Ausgang. Der Punkt in der Mitte erlaubt einen __Spannungshub__, eine Ausgangsamplitude, von fast 6 V, doch bei 25 mV am Eingang ist die Tangente längst ungültig. Für die Kleinsignalgrenze 2,6 mV sind es 0,6 V. Für einen Verstärker muss der Arbeitspunkt im Gebiet nahezu konstanter Steigung liegen, und der Hub soll möglichst groß sein. Die gegengekoppelte Fassung hat $A=-3\,\text{k}\Omega/(1\,\text{k}\Omega+12{,}9\,\Omega)=-2{,}96$: nur 1,3 % von $u_\mathrm{ein}$ liegen an der BE-Strecke, dafür ist die Verstärkung fast nur durch zwei Widerstände bestimmt. Emitterfolger mit $R_\mathrm{E}=3$ k$\Omega$ bei 2 mA: $S\,R_\mathrm{E}=231$, $A=0{,}996$. Seine Stärke ist nicht die Spannung, sondern der Strom: Die Stromverstärkung ist $1+B=201$. Er dient als __Puffer__: Er belastet die Quelle kaum und treibt die Last niederohmig.
::::

⁠**Grenzfälle:** $R_\mathrm{E}\to0$ in der gegengekoppelten Form ergibt $-S\,R_\mathrm{C}$. $R_\mathrm{E}\to\infty$ beim Emitterfolger ergibt $A\to1$.

| Schaltung | $A$ | Eingangswiderstand | Ausgangswiderstand | Einsatz |
|---|---|---|---|---|
| Emitter | $-231$ | $r_\mathrm{BE}=2{,}6$ k$\Omega$ | $R_\mathrm{C}=3$ k$\Omega$ | Spannung verstärken |
| Kollektor | $0{,}996$ | $r_\mathrm{BE}+(1+B)R_\mathrm{E}=606$ k$\Omega$ | $1/S=13\,\Omega$ | Puffer, Stromverstärkung |
| Basis | $+231$ | $1/S=13\,\Omega$ | $R_\mathrm{C}=3$ k$\Omega$ | Niederohmige Quelle verstärken |

:::frage Eine reale Emitterschaltung hat doch eine flachere Kennlinie als die Basisschaltung. Wieso soll der Betrag gleich sein?
Gleich ist er bei direkter Ansteuerung, gleichem $R_\mathrm{C}$ und gleichem Strom. Liegt vor der Basis ein Vorwiderstand oder eine Quelle mit Innenwiderstand, bildet er mit $r_\mathrm{BE}$ einen Spannungsteiler, und nur ein Teil von $u_\mathrm{ein}$ erreicht die BE-Strecke. Dann ist die Kennlinie der Emitterschaltung flacher. In der Basisschaltung entfällt dieser Teiler, weil die niederohmige Quelle am Emitter liegt.
:::

:::ltspice Die Übertragungskennlinie der Emitterschaltung
⁠**Zeichnen:** `voltage` `VCC` mit 12 an `res` 3k zum Kollektor (Netz `c`), `npn` mit Modell `T`, Emitter an Masse, an der Basis `voltage` `VE`.

⁠**Direktiven:** das Modell aus Stufe [3](eine-flache-viele-kennlinien.html#stufe-3), `.dc VE 0.5 0.7 0.1m`, `.meas dc a1 FIND V(c) AT=0.5995`, `.meas dc a2 FIND V(c) AT=0.6005`, `.meas dc au PARAM (a2-a1)/1m`.

⁠**Was du siehst:** $U_\mathrm{aus}$ fällt von 12 V bis nahe 0, in einem Fenster von rund 60 mV. `au` ergibt $-213$, gegen $-215$ in der Rechnung. LTspice rechnet mit $U_T=25{,}86$ mV und steht bei $U_\mathrm{BE}=0{,}6$ V auf 1,98 mA. Für Aufgabe [12](#aufg-12) setze `VCC` auf 9, den Widerstand auf 4.7k und die `AT`-Werte auf 0.582 und 0.583: `au` ergibt bei 0,98 mA dann $-169$.
:::

:::aufgabe Aufgabe 12 ★★★ Verstärker und Folger
<span class="anker" id="aufg-12"></span>

T arbeitet bei $I_\mathrm{C}=1$ mA und $U_\mathrm{CE}=4{,}3$ V mit $U_\mathrm{CC}=9$ V, $R_\mathrm{C}=4{,}7$ k$\Omega$. (a) Sage vorher, wie groß $A$ der Emitterschaltung ist, nur aus der Spannung an $R_\mathrm{C}$. (b) Wie groß ist die Ausgangsamplitude bei $\hat u_\mathrm{ein}=2$ mV? Wie ändert $r_\mathrm{CE}$ das Ergebnis? (c) Mit einem Emitterwiderstand 470 $\Omega$: Wie groß ist $A$? (d) Als Emitterfolger mit $R_\mathrm{E}=4{,}7$ k$\Omega$: Wie groß ist $A$? Ist der Ausgang invertiert?

:::loesung
(a) $U_{R_\mathrm{C}}=4{,}7$ V, also $A=-4{,}7\,\mathrm{V}/26\,\mathrm{mV}=-181$.

(b) $\hat u_\mathrm{aus}=0{,}36$ V. Mit $r_\mathrm{CE}=78$ k$\Omega$ ist $A=-S(R_\mathrm{C}\parallel r_\mathrm{CE})=-171$, nur 6 % weniger.

(c) $A=-4{,}7\,\text{k}\Omega/(470\,\Omega+26\,\Omega)=-9{,}5$. Die Näherung $-R_\mathrm{C}/R_\mathrm{E}$ ergibt $-10$.

(d) $S\,R_\mathrm{E}=181$, $A=0{,}994$. Der Ausgang ist nicht invertiert, der Emitter folgt der Basis gleichphasig.
:::
:::

::::formelsammlung
**Spannungsverstärkung der Grundschaltungen**

$$A_\mathrm{Emitter}=-S\,R_\mathrm{C}=-\frac{U_{R_\mathrm{C}}}{U_T},\qquad A_\mathrm{Kollektor}=\frac{S\,R_\mathrm{E}}{1+S\,R_\mathrm{E}}<1,\qquad A_\mathrm{Basis}=+S\,R_\mathrm{C}$$

$A=u_\mathrm{aus}/u_\mathrm{ein}$ für kleine Signale im aktiven Bereich, $r_\mathrm{CE}$ vernachlässigt, $R_\mathrm{C}\ll r_\mathrm{CE}$, Ansteuerung durch eine Quelle mit kleinem Innenwiderstand. $U_{R_\mathrm{C}}=I_\mathrm{C}R_\mathrm{C}$ ist die Gleichspannung am Kollektorwiderstand. Die Emitterschaltung invertiert, die Basisschaltung nicht.

**Emitterschaltung mit Emitterwiderstand**

$$A=-R_\mathrm{C}/(R_\mathrm{E}+1/S)\approx-R_\mathrm{C}/R_\mathrm{E}$$

Nur $u_\mathrm{be}=u_\mathrm{ein}/(1+S\,R_\mathrm{E})$ steuert, der Großteil von $u_\mathrm{ein}$ liegt an $R_\mathrm{E}$. Die Verstärkung ist fast nur durch zwei Widerstände bestimmt.

**Emitterschaltung mit Ausgangswiderstand**

$$A_\mathrm{Emitter}=-S\,(R_\mathrm{C}\parallel r_\mathrm{CE})$$

Berücksichtigt den endlichen Ausgangswiderstand $r_\mathrm{CE}$.

**Eingangswiderstand der Kollektorschaltung**

$$r_\mathrm{BE}+(1+B)R_\mathrm{E}$$

Kollektorschaltung (Emitterfolger): Ausgangswiderstand $1/S$, Stromverstärkung $1+B$. Emitterschaltung: Eingang $r_\mathrm{BE}$, Ausgang $R_\mathrm{C}$. Basisschaltung: Eingang $1/S$, Ausgang $R_\mathrm{C}$.
::::

::::lernkarten
:::karte zusammenhang Gemeinsamer Anschluss
Warum ist bei einer Verstärkerschaltung mit einem Transistor ein Anschluss für das Signal am Eingang und am Ausgang gemeinsam?
---
Eingang und Ausgang brauchen je zwei Klemmen, der Transistor hat insgesamt nur drei. Ein Anschluss wird also für das Signal gemeinsam, und er gibt der Grundschaltung ihren Namen.
--- falsch
Damit Eingangs- und Ausgangsstrom gleich groß sind; ein gemeinsamer Anschluss erzwingt nach der Knotenregel denselben Strom. Er gibt der Schaltung deshalb ihre Stromverstärkung 1.
--- falsch
Weil der gemeinsame Anschluss immer an der Versorgung liegen muss. Nur so erhält der Transistor Energie, und der Anschluss bestimmt, wie groß die Versorgungsspannung ist.
--- falsch
Weil das Signal sonst den Arbeitspunkt verschieben würde. Der gemeinsame Anschluss hält den Gleichstrom fest, er ist deshalb immer der Emitter mit seinem Widerstand.
:::
:::karte begriff Emitterschaltung
Wie wird das Signal in der Emitterschaltung zu- und abgeführt, und warum ist ihr Ausgang invertiert?
---
Die Grundschaltung, in der das Signal an die Basis kommt und vom Kollektor weggeht. $u_\mathrm{ein}$ erzeugt $i_\mathrm{c}=S\,u_\mathrm{ein}$, der durch $R_\mathrm{C}$ das Kollektorpotenzial herabzieht: Der Ausgang ist invertiert.
--- falsch
Die Grundschaltung, in der das Signal an den Emitter kommt und vom Kollektor weggeht. Sinkt der Emitter, steigt der Strom und hebt das Kollektorpotenzial deutlich an: Der Ausgang ist deshalb invertiert.
--- falsch
Die Grundschaltung, in der das Signal an die Basis kommt und vom Emitter weggeht. Der Emitter läuft der Basis entgegen, weil $U_\mathrm{BE}$ konstant bleiben muss: Der Ausgang ist invertiert.
--- falsch
Die Grundschaltung, in der das Signal an die Basis kommt und vom Kollektor weggeht. Der Ausgang ist invertiert, weil die Versorgung $U_\mathrm{CC}$ das Vorzeichen jeder Änderung umdreht.
:::
:::karte begriff Kollektorschaltung und Emitterfolger
Wie ist die Kollektorschaltung beschaltet, und warum heißt sie auch Emitterfolger?
---
Die Grundschaltung, in der das Signal an die Basis kommt und vom Emitter weggeht. Der Emitter folgt der Basis: Stünde er still, änderte sich $U_\mathrm{BE}$, und der entstehende Strom höbe ihn über $R_\mathrm{E}$ sofort nach.
--- falsch
Die Grundschaltung, in der das Signal an den Kollektor kommt und vom Emitter weggeht. Der Emitter folgt dem Kollektor, weil beide über die gesperrte CB-Diode fest miteinander verbunden sind.
--- falsch
Die Grundschaltung, in der das Signal an die Basis kommt und vom Kollektor weggeht. Der Emitter folgt dem Kollektor, weil der Kollektorstrom über $R_\mathrm{E}$ das Emitterpotenzial mitnimmt.
--- falsch
Die Grundschaltung, in der die Basis festliegt und das Signal vom Emitter kommt. Sie heißt Emitterfolger, weil der Emitter als erster Anschluss das Signal aufnimmt und es unverändert an den Kollektor weitergibt.
:::
:::karte begriff Basisschaltung
Wie ist die Basisschaltung beschaltet, und in welche Richtung bewegt sich ihr Ausgang?
---
Die Grundschaltung, in der die Basis festliegt und das Signal an den Emitter kommt, der Ausgang ist der Kollektor. Sinkt der Emitter, steigt $U_\mathrm{BE}$, mehr Strom zieht den Kollektor herab: Ein- und Ausgang bewegen sich gleichsinnig.
--- falsch
Die Grundschaltung, in der das Signal an die Basis kommt und vom Emitter weggeht. Steigt die Basis, folgt der Emitter, weil $U_\mathrm{BE}$ fast konstant bleibt: Ein- und Ausgang bewegen sich gleichsinnig, mit Verstärkung knapp unter 1.
--- falsch
Die Grundschaltung, in der die Basis festliegt und das Signal an den Emitter kommt. Sinkt der Emitter, sinkt $U_\mathrm{BE}$, weniger Strom hebt den Kollektor an: Ein- und Ausgang bewegen sich gegensinnig.
--- falsch
Die Grundschaltung, in der das Signal an die Basis kommt und der Ausgang am Kollektor liegt. Der Emitter liegt fest an Masse, und steigt die Basis, sinkt der Kollektor: Ein- und Ausgang bewegen sich gegensinnig.
:::
:::karte formel Spannungsverstärkung der Grundschaltungen
Wie groß ist die Spannungsverstärkung $A=u_\mathrm{aus}/u_\mathrm{ein}$ der drei Grundschaltungen für kleine Signale?
---
$A_\mathrm{Emitter}=-S\,R_\mathrm{C}=-\frac{U_{R_\mathrm{C}}}{U_T}$, $A_\mathrm{Kollektor}=\frac{S\,R_\mathrm{E}}{1+S\,R_\mathrm{E}}<1$, $A_\mathrm{Basis}=+S\,R_\mathrm{C}$. Gültig im aktiven Bereich für $|u_\mathrm{be}|\ll U_T$, mit $r_\mathrm{CE}$ vernachlässigt.
--- falsch
$A_\mathrm{Emitter}=-B\,R_\mathrm{C}$, $A_\mathrm{Kollektor}=1+S\,R_\mathrm{E}>1$, $A_\mathrm{Basis}=-S\,R_\mathrm{C}$. Gültig im aktiven Bereich für $|u_\mathrm{be}|\ll U_T$, mit $r_\mathrm{CE}$ vernachlässigt.
--- falsch
$A_\mathrm{Emitter}=-S\,R_\mathrm{C}$, $A_\mathrm{Kollektor}=-S\,R_\mathrm{E}$, $A_\mathrm{Basis}=+\frac{S\,R_\mathrm{C}}{1+S\,R_\mathrm{C}}<1$. Gültig für jede Signalgröße, solange der Transistor nicht in die Sättigung gerät.
--- falsch
$A_\mathrm{Emitter}=-\frac{U_T}{U_{R_\mathrm{C}}}$, $A_\mathrm{Kollektor}=\frac{1}{1+S\,R_\mathrm{E}}$, $A_\mathrm{Basis}=+\frac{U_T}{U_{R_\mathrm{C}}}$. Gültig im aktiven Bereich für $|u_\mathrm{be}|\ll U_T$, mit $r_\mathrm{CE}$ vernachlässigt.
:::
:::karte zusammenhang Verstärkung aus der Spannung am Kollektorwiderstand
Warum kommen in der Spannungsverstärkung der Emitterschaltung weder $B$ noch der Transistortyp vor?
---
Mit $S=I_\mathrm{C}/U_T$ wird $S\,R_\mathrm{C}=I_\mathrm{C}R_\mathrm{C}/U_T$, also die Gleichspannung $U_{R_\mathrm{C}}$ am Kollektorwiderstand geteilt durch $U_T$. Im Rechenmodell ergibt das $-6\,\mathrm{V}/26\,\mathrm{mV}=-231$.
--- falsch
Weil $B$ sich zwischen Eingangs- und Ausgangsstrom herauskürzt und nur der Kollektorwiderstand übrig bleibt. Die Verstärkung ist deshalb einfach $-R_\mathrm{C}$ in Kiloohm, im Rechenmodell $-3$.
--- falsch
Weil alle Siliziumtransistoren dasselbe $B$ und dasselbe $I_\mathrm{S}$ haben. Die Verstärkung ist deshalb eine Eigenschaft des Werkstoffs, im Rechenmodell immer $-200$.
--- falsch
Mit $S=B/r_\mathrm{BE}$ kürzt sich $B$ gegen den Eingangswiderstand heraus, und es bleibt $-R_\mathrm{C}/r_\mathrm{BE}$. Im Rechenmodell ergibt das $-3\,\text{k}\Omega/2{,}6\,\text{k}\Omega\approx-1{,}2$.
:::
:::karte formel Emitterschaltung mit Emitterwiderstand
Wie groß ist die Spannungsverstärkung der Emitterschaltung mit Emitterwiderstand $R_\mathrm{E}$, und wie verändert sie $r_\mathrm{CE}$?
---
Mit Emitterwiderstand ist $A=-R_\mathrm{C}/(R_\mathrm{E}+1/S)\approx-R_\mathrm{C}/R_\mathrm{E}$, fast nur durch zwei Widerstände bestimmt. Mit $r_\mathrm{CE}$ ist $A_\mathrm{Emitter}=-S\,(R_\mathrm{C}\parallel r_\mathrm{CE})$, etwas kleiner im Betrag.
--- falsch
Mit Emitterwiderstand ist $A=-S\,(R_\mathrm{C}+R_\mathrm{E})$, der Betrag wächst also um den Emitterwiderstand. Mit $r_\mathrm{CE}$ ist $A_\mathrm{Emitter}=-S\,(R_\mathrm{C}+r_\mathrm{CE})$, im Betrag deutlich größer.
--- falsch
Mit Emitterwiderstand ist $A=-R_\mathrm{E}/R_\mathrm{C}$, unabhängig vom Transistor. Mit $r_\mathrm{CE}$ ändert sich nichts, weil $r_\mathrm{CE}$ im Kleinsignal-Ersatzschaltbild in Reihe mit der Quelle liegt.
--- falsch
Mit Emitterwiderstand ist $A=-S\,R_\mathrm{C}$ wie ohne, weil $R_\mathrm{E}$ nur den Gleichstrom festlegt. Mit $r_\mathrm{CE}$ ist $A_\mathrm{Emitter}=-S\,r_\mathrm{CE}$, weil $R_\mathrm{C}$ dann keine Rolle mehr spielt.
:::
:::karte herleitung Drei Maschen im Kleinsignal
Wie folgen aus den Maschen im Kleinsignal die Verstärkungen der Emitter-, Kollektor- und Basisschaltung?
---
$U_\mathrm{CC}$ ist für das Signal Masse, weil eine konstante Spannung im Kleinsignal zum Draht wird.
---
Emitterschaltung: $u_\mathrm{be}=u_\mathrm{ein}$ und $u_\mathrm{aus}=-R_\mathrm{C}i_\mathrm{c}=-R_\mathrm{C}S\,u_\mathrm{ein}$, weil das Signal voll an der BE-Strecke liegt und $i_\mathrm{c}$ durch $R_\mathrm{C}$ das Kollektorpotenzial herabzieht.
---
Kollektorschaltung: $u_\mathrm{aus}=R_\mathrm{E}S\,u_\mathrm{be}$ mit $u_\mathrm{be}=u_\mathrm{ein}-u_\mathrm{aus}$; Auflösen ergibt $\frac{S\,R_\mathrm{E}}{1+S\,R_\mathrm{E}}$, weil die Steuerspannung zwischen Basis und dem mitlaufenden Emitter liegt.
---
Basisschaltung: $u_\mathrm{be}=-u_\mathrm{ein}$ und $u_\mathrm{aus}=-R_\mathrm{C}S\,u_\mathrm{be}=+S\,R_\mathrm{C}u_\mathrm{ein}$, weil die Basis ruht und das Signal am Emitter liegt.
:::
:::karte herleitung Emitterwiderstand im Kleinsignal
Wie folgt im Kleinsignal, dass ein Emitterwiderstand die Verstärkung der Emitterschaltung auf $A=-R_\mathrm{C}/(R_\mathrm{E}+1/S)$ senkt?
---
Es gilt $u_\mathrm{ein}=u_\mathrm{be}+R_\mathrm{E}S\,u_\mathrm{be}$, weil der Strom $S\,u_\mathrm{be}$ auch durch $R_\mathrm{E}$ fließt und dort eine Spannung erzeugt.
---
Daraus folgt $u_\mathrm{be}=u_\mathrm{ein}/(1+S\,R_\mathrm{E})$, weil man nach $u_\mathrm{be}$ auflöst; nur dieser Rest steuert, der Großteil von $u_\mathrm{ein}$ liegt an $R_\mathrm{E}$.
---
Der Ausgang ist weiterhin $-R_\mathrm{C}S\,u_\mathrm{be}$; mit dem Rest $u_\mathrm{be}$ und nach Kürzen durch $S$ folgt $A=-R_\mathrm{C}/(R_\mathrm{E}+1/S)$, weil der Kollektorstrom nur von $u_\mathrm{be}$ abhängt.
:::
:::karte begriff Spannungshub
Was bezeichnet man als Spannungshub, und wie groß ist er bei der Emitterschaltung im Punkt A?
---
Eine Ausgangsamplitude, also wie weit die Ausgangsspannung um den Arbeitspunkt schwingen kann. Der Punkt in der Mitte erlaubt fast 6 V, an der Kleinsignalgrenze von 2,6 mV am Eingang sind es nur 0,6 V.
--- falsch
Den Unterschied zwischen Versorgungsspannung und Ausgangsspannung, also den Spannungsabfall am Kollektorwiderstand. Im Punkt A sind es 6 V, die Hälfte der Versorgung, die sich mit dem Signal nicht ändert.
--- falsch
Eine Eingangsamplitude, also wie weit die Eingangsspannung schwingen darf, bevor der Transistor sperrt. Im Punkt A sind es 0,6 V, genau die Schwellspannung der BE-Diode.
--- falsch
Den Sprung der Ausgangsspannung, wenn ein Inverter zwischen Sperrung und Sättigung umschaltet. Im Punkt A sind es 11,8 V, von 12 V bis hinunter auf 0,2 V.
:::
:::karte zusammenhang Puffer
Warum eignet sich der Emitterfolger als Puffer, obwohl seine Spannungsverstärkung kleiner als 1 ist?
---
Seine Stärke ist der Strom: Die Stromverstärkung ist $1+B=201$. Mit 606 k$\Omega$ Eingangswiderstand belastet er die Quelle kaum, mit 13 $\Omega$ Ausgangswiderstand treibt er die Last niederohmig.
--- falsch
Seine Stärke ist die Phasenumkehr: Er dreht das Signal um, ohne es zu verstärken. Mit 13 $\Omega$ Eingangswiderstand nimmt er der Quelle viel Strom ab und gibt ihn invertiert an die Last.
--- falsch
Seine Stärke ist die Spannung: Sie ist bei großer Last höher als bei der Emitterschaltung. Mit 3 k$\Omega$ Eingangs- und 606 k$\Omega$ Ausgangswiderstand trennt er Quelle und Last.
--- falsch
Seine Stärke ist die Temperatur: Ohne Verstärkung erwärmt er sich nicht. Mit 2,6 k$\Omega$ Eingangs- und 3 k$\Omega$ Ausgangswiderstand passt er jede Quelle an jede Last an.
:::
:::karte formel Widerstände der Grundschaltungen
Welche Eingangs- und Ausgangswiderstände haben die drei Grundschaltungen im Rechenmodell, und wozu dient deshalb jede?
---
Emitter: $r_\mathrm{BE}=2{,}6$ k$\Omega$ und $R_\mathrm{C}=3$ k$\Omega$, Spannung verstärken. Kollektor: $r_\mathrm{BE}+(1+B)R_\mathrm{E}=606$ k$\Omega$ und $1/S=13\,\Omega$, Puffer. Basis: $1/S=13\,\Omega$ und $R_\mathrm{C}=3$ k$\Omega$, niederohmige Quelle verstärken.
--- falsch
Emitter: $1/S=13\,\Omega$ und $R_\mathrm{C}=3$ k$\Omega$, Puffer. Kollektor: $r_\mathrm{BE}=2{,}6$ k$\Omega$ und $R_\mathrm{E}=3$ k$\Omega$, Spannung verstärken. Basis: $r_\mathrm{BE}+(1+B)R_\mathrm{E}=606$ k$\Omega$ und $1/S=13\,\Omega$, hochohmige Quelle verstärken.
--- falsch
Alle drei haben denselben Eingangswiderstand $r_\mathrm{BE}=2{,}6$ k$\Omega$ und denselben Ausgangswiderstand $R_\mathrm{C}=3$ k$\Omega$, weil der Transistor derselbe ist; sie unterscheiden sich nur im Vorzeichen der Verstärkung.
--- falsch
Emitter: $R_\mathrm{C}=3$ k$\Omega$ und $r_\mathrm{BE}=2{,}6$ k$\Omega$, Puffer. Kollektor: $1/S=13\,\Omega$ und $606$ k$\Omega$, Spannung verstärken. Basis: $R_\mathrm{C}=3$ k$\Omega$ und $1/S=13\,\Omega$, Strom verstärken.
:::
:::karte zusammenhang Gegengekoppelte Emitterschaltung
Was gewinnt man mit einem Emitterwiderstand in der Emitterschaltung, obwohl die Verstärkung im Rechenmodell von $-231$ auf $-2{,}96$ sinkt?
---
Nur 1,3 % von $u_\mathrm{ein}$ liegen dann an der BE-Strecke, und die Verstärkung ist fast nur durch zwei Widerstände bestimmt, $A\approx-R_\mathrm{C}/R_\mathrm{E}$, nicht mehr durch den Transistor.
--- falsch
Die Verstärkung wird positiv, der Ausgang ist also nicht mehr invertiert. Dafür liegt fast das ganze $u_\mathrm{ein}$ an der BE-Strecke, und der Transistor bestimmt die Verstärkung allein.
--- falsch
Man gewinnt nichts: Der Emitterwiderstand dient nur dem Arbeitspunkt. Für das Signal ist er ein reiner Verlust, den man immer mit einem Kondensator überbrücken muss.
--- falsch
Der Ausgangswiderstand sinkt auf $1/S$, und die Schaltung treibt jede Last. Die Verstärkung hängt dann nur noch von $B$ ab, $A\approx-B$, und nicht mehr von den Widerständen.
:::
:::karte zusammenhang Vorwiderstand vor der Basis
Warum hat eine reale Emitterschaltung mit Vorwiderstand eine flachere Kennlinie als die Basisschaltung, obwohl der Betrag der Verstärkung gleich sein soll?
---
Gleich ist er nur bei direkter Ansteuerung. Ein Vorwiderstand bildet mit $r_\mathrm{BE}$ einen Spannungsteiler, nur ein Teil von $u_\mathrm{ein}$ erreicht die BE-Strecke. In der Basisschaltung liegt die niederohmige Quelle am Emitter, der Teiler entfällt.
--- falsch
Der Vorwiderstand erhöht den Arbeitspunktstrom und damit $S$, die Kennlinie wird aber flacher, weil der Transistor schneller in die Sättigung gerät. In der Basisschaltung fehlt die Sättigung.
--- falsch
Die Emitterschaltung hat grundsätzlich die halbe Verstärkung der Basisschaltung, weil ihr Ausgang invertiert ist. Mit Vorwiderstand ändert sich daran nichts, er erklärt den Unterschied nicht.
--- falsch
Der Vorwiderstand bildet mit $R_\mathrm{C}$ einen Teiler am Ausgang, der die Ausgangsspannung ungefähr halbiert. In der Basisschaltung liegt kein Widerstand am Kollektor, deshalb fehlt dort dieser Teiler, und die Kennlinie bleibt steil.
:::
::::

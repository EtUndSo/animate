---
title: Stufe 2: Der Differenzverstärker
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Der Operationsverstärker
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-operationsverstarker
knoten: Kapitel 11: Der Operationsverstärker
order: 1210400
summary: Eine Störung auf beiden Leitungen soll verschwinden, der Unterschied zwischen ihnen soll verstärkt werden.
tags: Gleichtaktspannung, nicht-invertierender Eingang, invertierender Eingang
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Eine Störung auf beiden Leitungen soll verschwinden, der Unterschied zwischen ihnen soll verstärkt werden. Dazu braucht man eine Schaltung, deren Ausgang nur von der Differenz zweier Spannungen abhängt.
:::

**Die Idee.** Zwei gleiche Transistoren T1 und T2 hängen mit den Emittern am gemeinsamen Knoten E (Abb. [2](#abb-2)). Darunter sitzt T3. Seine Basis liegt an der festen Spannung $U_\mathrm{bias}$, deshalb wirkt er als Stromquelle ([Kapitel 10](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor/der-bipolartransistor.html)) und zieht den festen Strom $I_0$ aus dem Knoten. Die Basisströme sind klein, also gilt $I_\mathrm{C1}+I_\mathrm{C2}=I_0$. Die Summe steht fest, nur die Aufteilung kann sich ändern.

Steigen beide Basen um dasselbe Stück, steigt E mit, denn T3 hält den Strom fest und damit auch $U_\mathrm{BE}$. Es ändert sich nichts. Diesen gemeinsamen Anteil nennt man __Gleichtaktspannung__, $U_\mathrm{gl}=(\varphi_++\varphi_-)/2$. Steigt nur die Basis von T2, zieht T2 mehr Strom. T1 bekommt um genau diesen Betrag weniger. Am rechten Kollektorwiderstand fällt mehr Spannung ab, am linken weniger, und die Spannung zwischen den Kollektoren schlägt aus.

:::abbildung et1/k11diff 2
Links der Differenzverstärker mit $I_0=2$ mA und $R_\mathrm{C}=3$ k$\Omega$. T3 hält die Summe fest. Rechts die Aufteilung: Um $U_\mathrm{D}=0$ fließt in jedem Zweig 1 mA, bei 100 mV fließen 97,9 % durch T2.
:::

:::satz Satz 2.1 (Differenzverstärker)
<span class="anker" id="satz-2-1"></span>

T1 hat die Basis am Eingang $\varphi_-$, T2 am Eingang $\varphi_+$. Mit $U_\mathrm{D}=\varphi_+-\varphi_-$ und $U_\mathrm{A}=U_\mathrm{a1}-U_\mathrm{a2}$ gilt

<span class="anker" id="gl-2-1"></span>
$$I_\mathrm{C2}=\frac{I_0}{1+\mathrm{e}^{-U_\mathrm{D}/U_T}},\qquad I_\mathrm{C1}=\frac{I_0}{1+\mathrm{e}^{U_\mathrm{D}/U_T}},\qquad U_\mathrm{A}=R_\mathrm{C}\,(I_\mathrm{C2}-I_\mathrm{C1}). \tag{2.1}$$

Für $|U_\mathrm{D}|\ll U_T$ ist das eine Gerade:

<span class="anker" id="gl-2-2"></span>
$$U_\mathrm{A}=A_\mathrm{D}\,U_\mathrm{D},\qquad A_\mathrm{D}=S\,R_\mathrm{C}=\frac{I_0\,R_\mathrm{C}}{2\,U_T}=\frac{U_{R_\mathrm{C}}}{U_T}. \tag{2.2}$$
:::

⁠**So liest man das:** $S=I_\mathrm{C}/U_T$ ist die Steilheit eines Transistors bei $I_\mathrm{C}=I_0/2$. $U_{R_\mathrm{C}}=I_0R_\mathrm{C}/2$ ist die Ruhespannung an einem Kollektorwiderstand. $\varphi_+$ heißt __nicht-invertierender Eingang__, weil der Ausgang ihm gleichsinnig folgt, $\varphi_-$ __invertierender Eingang__. **Gültigkeit:** gleiche Transistoren, beide im aktiven Bereich, Basisströme klein gegen $I_0$.

:::herleitung Teilung und Verstärkung
Beide Emitter liegen auf demselben Potenzial, also $U_\mathrm{BE2}-U_\mathrm{BE1}=U_\mathrm{D}$. Mit $I_\mathrm{C}=I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{BE}/U_T}$ folgt $I_\mathrm{C2}/I_\mathrm{C1}=\mathrm{e}^{U_\mathrm{D}/U_T}$. Zusammen mit $I_\mathrm{C1}+I_\mathrm{C2}=I_0$ ergibt das [(2.1)](#gl-2-1). Für kleine Änderungen gilt: Die Summe ist fest, also $\Delta I_\mathrm{C1}=-\Delta I_\mathrm{C2}$. Beide sind $S$ mal der Änderung der eigenen $U_\mathrm{BE}$, die Änderungen sind also entgegengesetzt gleich. Ihre Differenz ist $U_\mathrm{D}$, also trägt jede Strecke $\pm U_\mathrm{D}/2$. Damit ist $\Delta I_\mathrm{C2}=S\,U_\mathrm{D}/2$ und $U_\mathrm{A}=2R_\mathrm{C}\,\Delta I_\mathrm{C2}=S\,R_\mathrm{C}\,U_\mathrm{D}$.
:::

::::beispiel
In Ruhe fließen je 1 mA, die Kollektoren liegen bei $12\,\mathrm{V}-3\,\mathrm{V}=9$ V. $S=38{,}5$ mS, also $A_\mathrm{D}=3\,\mathrm{V}/26\,\mathrm{mV}=115$. Bei $U_\mathrm{D}=1$ mV wandert $\pm19{,}2$ µ A zwischen den Zweigen, jeder Kollektor bewegt sich um 57,7 mV, zusammen sind das $U_\mathrm{A}=115$ mV. Eine Störung von 100 mV auf beiden Eingängen ändert daran nichts.
::::

⁠**Grenzfälle:** $U_\mathrm{D}=0$ ergibt $I_0/2$ je Zweig. Bei $|U_\mathrm{D}|\gg U_T$ fließt alles durch einen Transistor, $U_\mathrm{A}\to\pm R_\mathrm{C}I_0=\pm6$ V. Der lineare Bereich ist nur wenige $U_T$ breit: Bei 26 mV liefert die Gerade 3,0 V, die exakte Kurve 2,77 V.

**Eingang.** Ein Eingangssignal $U_\mathrm{D}$ liegt an zwei BE-Strecken in Reihe, der Eingangswiderstand ist $2\,r_\mathrm{BE}=2B/S=10{,}4$ k$\Omega$. Bei 20 µ A Summenstrom statt 2 mA sind es 1,04 M$\Omega$, und jede Basis zieht nur 50 nA. Daher stammen $r_\mathrm{e}$ und $I_\mathrm{B}$ im Rechenmodell.

**Vom Differenzverstärker zum OPV.** $A_\mathrm{D}=U_{R_\mathrm{C}}/U_T$ bleibt bei einigen Hundert, denn $U_{R_\mathrm{C}}$ kann die Versorgung nicht übersteigen. Ein Stromspiegel ([Kapitel 10](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor/der-bipolartransistor.html)) statt der Widerstände führt beide Stromänderungen auf eine Seite und wirkt dort wie die Parallelschaltung zweier $r_\mathrm{CE}$. Das ergibt $S\,r_\mathrm{CE}/2=U_\mathrm{Early}/(2U_T)\approx1400$. Dahinter folgen eine Spannungsverstärkerstufe und ein Emitterfolger für den niedrigen Ausgangswiderstand. Zusammen sind es $10^5$ bis $10^6$. Dieser Wert hängt von $B$, $U_\mathrm{Early}$ und der Temperatur ab: groß, aber ungenau.

:::frage Warum liegt an jedem Transistor nur die halbe Differenz, wenn ich nur eine Basis anhebe?
Weil der Knoten E um die Hälfte mitgeht. T2 will mehr Strom, die Summe ist aber fest, also hebt sich E, bis T1 genau so viel abgibt. Die feste Summe verlangt entgegengesetzt gleiche Änderungen von $U_\mathrm{BE}$. Wer die ganze Differenz auf eine Strecke legt, erhält das Doppelte des wahren $A_\mathrm{D}$.
:::

:::ltspice Die Stromaufteilung
⁠**Zeichnen:** Zwei `npn` Q1, Q2 mit Modell `T`. Die Kollektoren über je einen `res` 3k an `voltage` 12, Netze `a1`, `a2`. Beide Emitter an Netz `e`, von dort `current` 2m nach einer `voltage` $-12$. Basis Q1 an Masse, Basis Q2 an `voltage` `VP`.

⁠**Direktiven:** `.model T NPN(IS=1.55e-13 BF=186 VAF=74)`, `.dc VP -0.2 0.2 0.1m`, `.meas dc u1 FIND V(a1)-V(a2) AT=-0.5m`, `.meas dc u2 FIND V(a1)-V(a2) AT=0.5m`, `.meas dc ad PARAM (u2-u1)/1m`.

⁠**Was du siehst:** `Ic(Q1)` und `Ic(Q2)` kreuzen sich bei 0, bei 100 mV führt Q2 97,8 % des Stroms. `ad` ergibt 111,4 gegen 115 in der Rechnung, denn LTspice rechnet mit $U_T=25{,}85$ mV und zählt $r_\mathrm{CE}$ mit. Setze die Werte aus Aufgabe [2](#aufg-2) ein.
:::

:::aufgabe Aufgabe 2 ★★ Differenzstufe
<span class="anker" id="aufg-2"></span>

Eine Differenzstufe aus Transistoren T arbeitet mit $I_0=1$ mA, $R_\mathrm{C}=5$ k$\Omega$ und $U_\mathrm{CC}=12$ V. (a) Bestimme $S$, $A_\mathrm{D}$ und das Ruhepotenzial der Kollektoren. (b) Wie groß ist $U_\mathrm{A}$ bei $U_\mathrm{D}=2$ mV? Wie viel Strom wandert? (c) Beide Eingänge steigen um 1 V. Was passiert mit E, den Strömen und $U_\mathrm{A}$? (d) Sage vorher: Ändert sich $A_\mathrm{D}$, wenn $I_0$ doppelt so groß und $R_\mathrm{C}$ halb so groß wird?

:::loesung
(a) $S=0{,}5\,\mathrm{mA}/26\,\mathrm{mV}=19{,}2$ mS, $A_\mathrm{D}=96{,}2$, Kollektoren bei $12\,\mathrm{V}-2{,}5\,\mathrm{V}=9{,}5$ V. (b) $U_\mathrm{A}=192$ mV. Es wandern $S\,U_\mathrm{D}/2=19{,}2$ µ A. (c) E steigt um 1 V, $U_\mathrm{BE}$ und die Ströme bleiben, $U_\mathrm{A}=0$. (d) Nein: $A_\mathrm{D}=U_{R_\mathrm{C}}/U_T$, und $U_{R_\mathrm{C}}=2{,}5$ V bleibt gleich.
:::
:::

::::formelsammlung
**Differenz und Gleichtakt der Eingänge**

$$U_\mathrm{D}=\varphi_+-\varphi_-,\qquad U_\mathrm{gl}=(\varphi_++\varphi_-)/2$$

$\varphi_+$ ist der nicht-invertierende, $\varphi_-$ der invertierende Eingang; T2 hat die Basis an $\varphi_+$, T1 an $\varphi_-$.

**Fester Summenstrom**

$$I_\mathrm{C1}+I_\mathrm{C2}=I_0$$

Die Stromquelle T3 hält die Summe fest, die Basisströme sind klein; nur die Aufteilung kann sich ändern.

**Stromaufteilung**

$$I_\mathrm{C2}=\frac{I_0}{1+\mathrm{e}^{-U_\mathrm{D}/U_T}},\qquad I_\mathrm{C1}=\frac{I_0}{1+\mathrm{e}^{U_\mathrm{D}/U_T}},\qquad U_\mathrm{A}=R_\mathrm{C}\,(I_\mathrm{C2}-I_\mathrm{C1})$$

$U_\mathrm{A}=U_\mathrm{a1}-U_\mathrm{a2}$ ist die Spannung zwischen den Kollektoren. Gilt für gleiche Transistoren, beide im aktiven Bereich, Basisströme klein gegen $I_0$. Für $|U_\mathrm{D}|\gg U_T$ geht $U_\mathrm{A}\to\pm R_\mathrm{C}I_0$.

**Differenzverstärkung**

$$U_\mathrm{A}=A_\mathrm{D}\,U_\mathrm{D},\qquad A_\mathrm{D}=S\,R_\mathrm{C}=\frac{I_0\,R_\mathrm{C}}{2\,U_T}=\frac{U_{R_\mathrm{C}}}{U_T}$$

Für $|U_\mathrm{D}|\ll U_T$. $S=I_\mathrm{C}/U_T$ ist die Steilheit bei $I_\mathrm{C}=I_0/2$, $U_{R_\mathrm{C}}=I_0R_\mathrm{C}/2$ die Ruhespannung an einem Kollektorwiderstand. Jede BE-Strecke trägt $\pm U_\mathrm{D}/2$.

**Eingangswiderstand der Differenzstufe**

$$2\,r_\mathrm{BE}=2B/S$$

Das Signal $U_\mathrm{D}$ liegt an zwei BE-Strecken in Reihe; ein kleiner Summenstrom ergibt einen großen Eingangswiderstand.

**Verstärkung mit Stromspiegel**

$$S\,r_\mathrm{CE}/2=U_\mathrm{Early}/(2U_T)$$

Ein Stromspiegel statt der Kollektorwiderstände wirkt wie die Parallelschaltung zweier $r_\mathrm{CE}$. Mit Spannungsverstärkerstufe und Emitterfolger erreicht der OPV $10^5$ bis $10^6$.
::::

::::lernkarten
:::karte begriff Differenzverstärker
Was ist ein Differenzverstärker, und wie ist er aus Transistoren aufgebaut?
---
Eine Schaltung, die nur auf den Unterschied zweier Spannungen reagiert. Zwei gleiche Transistoren hängen mit den Emittern an einem gemeinsamen Knoten, aus dem eine Stromquelle den festen Strom $I_0$ zieht.
--- falsch
Eine Schaltung, die zwei Spannungen addiert und ihre Summe verstärkt. Zwei Transistoren hängen mit den Kollektoren an einem Knoten, an dem sich ihre Ströme zu $I_0$ summieren.
--- falsch
Eine Schaltung, die auf den Unterschied zweier Spannungen reagiert. Zwei Transistoren liegen mit den Emittern direkt an Masse, jeder verstärkt für sich, der Ausgang ist die Differenz ihrer Kollektorspannungen.
--- falsch
Ein Verstärker mit einem einzigen Transistor, dessen Basis und Emitter je einen Eingang bilden. Er verstärkt die Spannung zwischen Basis und Emitter, also eine Differenz.
:::
:::karte begriff Gleichtaktspannung
Was ist die Gleichtaktspannung an den beiden Eingängen eines Differenzverstärkers, und was bewirkt sie am Ausgang?
---
Der gemeinsame Anteil beider Eingangspotenziale, $U_\mathrm{gl}=(\varphi_++\varphi_-)/2$. Steigt nur sie, steigt der Emitterknoten mit, und am Ausgang ändert sich nichts.
--- falsch
Die Differenz der Eingangspotenziale, $\varphi_+-\varphi_-$. Sie ist genau die Spannung, die der Differenzverstärker verstärkt und am Ausgang ausgibt.
--- falsch
Der gemeinsame Anteil beider Eingangspotenziale, $U_\mathrm{gl}=\varphi_++\varphi_-$. Er wird genauso verstärkt wie die Differenz, weil beide Transistoren mitgehen und ihre Ströme gemeinsam wachsen.
--- falsch
Die Spannung, die beide Kollektoren in Ruhe gemeinsam haben, hier 9 V. Sie legt fest, wie weit der Ausgang in jede Richtung ausschlagen kann.
:::
:::karte begriff nicht-invertierender Eingang und invertierender Eingang
Welcher Eingang eines Differenzverstärkers heißt nicht-invertierender Eingang, welcher invertierender Eingang, und warum?
---
$\varphi_+$ ist der nicht-invertierende Eingang, weil der Ausgang ihm gleichsinnig folgt. $\varphi_-$ ist der invertierende: Er geht mit negativem Vorzeichen in $U_\mathrm{D}=\varphi_+-\varphi_-$ ein, steigt er, sinkt der Ausgang.
--- falsch
$\varphi_-$ ist der nicht-invertierende Eingang, weil der Ausgang ihm gleichsinnig folgt. $\varphi_+$ ist der invertierende, weil er in $U_\mathrm{D}$ vom anderen Eingang abgezogen wird.
--- falsch
Der Eingang mit der höheren Spannung ist der nicht-invertierende, der mit der niedrigeren der invertierende. Die Rollen wechseln deshalb, sobald das Signal seine Polung wechselt und der andere Eingang höher liegt.
--- falsch
Der nicht-invertierende Eingang ist der, an dem das Signal liegt, der invertierende der, an dem Masse liegt. Vertauscht man die Beschaltung, tauschen auch die beiden Namen.
:::
:::karte formel Stromaufteilung
Wie teilt sich der feste Strom $I_0$ eines Differenzverstärkers auf die beiden Transistoren auf, und wie groß ist die Ausgangsspannung zwischen den Kollektoren?
---
$I_\mathrm{C2}=\frac{I_0}{1+\mathrm{e}^{-U_\mathrm{D}/U_T}}$, $I_\mathrm{C1}=\frac{I_0}{1+\mathrm{e}^{U_\mathrm{D}/U_T}}$ und $U_\mathrm{A}=R_\mathrm{C}\,(I_\mathrm{C2}-I_\mathrm{C1})$; gültig für gleiche Transistoren im aktiven Bereich mit kleinen Basisströmen.
--- falsch
$I_\mathrm{C2}=\frac{I_0}{1+\mathrm{e}^{U_\mathrm{D}/U_T}}$, $I_\mathrm{C1}=\frac{I_0}{1+\mathrm{e}^{-U_\mathrm{D}/U_T}}$ und $U_\mathrm{A}=R_\mathrm{C}\,(I_\mathrm{C2}-I_\mathrm{C1})$: Der Transistor am höheren Eingang führt den kleineren Strom.
--- falsch
$I_\mathrm{C2}=I_0\,\mathrm{e}^{U_\mathrm{D}/U_T}$ und $I_\mathrm{C1}=I_0\,\mathrm{e}^{-U_\mathrm{D}/U_T}$: Die Summe der beiden Ströme ist nicht fest, sondern wächst mit $|U_\mathrm{D}|$, und $U_\mathrm{A}$ wächst exponentiell.
--- falsch
$I_\mathrm{C2}=\frac{I_0}{2}+\frac{U_\mathrm{D}}{R_\mathrm{C}}$ und $I_\mathrm{C1}=\frac{I_0}{2}-\frac{U_\mathrm{D}}{R_\mathrm{C}}$: Die Aufteilung ist für jedes $U_\mathrm{D}$ eine Gerade, bis einer der beiden Ströme null wird und der andere ganz $I_0$ führt.
:::
:::karte formel Differenzverstärkung
Wie groß ist die Verstärkung $A_\mathrm{D}$ eines Differenzverstärkers für kleine Eingangsdifferenzen, und wovon hängt sie ab?
---
$U_\mathrm{A}=A_\mathrm{D}\,U_\mathrm{D}$ mit $A_\mathrm{D}=S\,R_\mathrm{C}=\frac{I_0\,R_\mathrm{C}}{2\,U_T}=\frac{U_{R_\mathrm{C}}}{U_T}$, gültig für $|U_\mathrm{D}|\ll U_T$. $S$ ist die Steilheit bei $I_0/2$, $U_{R_\mathrm{C}}$ die Ruhespannung an einem Kollektorwiderstand.
--- falsch
$A_\mathrm{D}=2\,S\,R_\mathrm{C}=\frac{I_0\,R_\mathrm{C}}{U_T}$, gültig für $|U_\mathrm{D}|\ll U_T$: Die ganze Differenz $U_\mathrm{D}$ liegt an jeder BE-Strecke, deshalb zählt der doppelte Wert, den die Kollektoren gemeinsam ausgeben.
--- falsch
$A_\mathrm{D}=S\,R_\mathrm{C}=\frac{I_0\,R_\mathrm{C}}{2\,U_T}$ für jedes $U_\mathrm{D}$, auch weit über $U_T$: Der Ausgang folgt dieser Geraden bis zur Versorgungsspannung.
--- falsch
$A_\mathrm{D}=R_\mathrm{C}/S=\frac{2\,U_T\,R_\mathrm{C}}{I_0}$, gültig für $|U_\mathrm{D}|\ll U_T$: Mehr Ruhestrom macht die Stufe weniger empfindlich, weil $S$ dann wächst.
:::
:::karte herleitung Teilung und Verstärkung
Wie folgen aus $I_\mathrm{C}=I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{BE}/U_T}$ und dem festen Summenstrom $I_0$ die Stromaufteilung und die Verstärkung $A_\mathrm{D}=S\,R_\mathrm{C}$?
---
Beide Emitter liegen auf demselben Potenzial, also ist $U_\mathrm{BE2}-U_\mathrm{BE1}=U_\mathrm{D}$, weil die Basen an $\varphi_+$ und $\varphi_-$ liegen.
---
Damit ist $I_\mathrm{C2}/I_\mathrm{C1}=\mathrm{e}^{U_\mathrm{D}/U_T}$, weil jeder Kollektorstrom exponentiell von seiner eigenen $U_\mathrm{BE}$ abhängt; zusammen mit $I_\mathrm{C1}+I_\mathrm{C2}=I_0$ folgt die Aufteilung.
---
Für kleine Änderungen gilt $\Delta I_\mathrm{C1}=-\Delta I_\mathrm{C2}$, weil die Summe fest ist.
---
Jede Stromänderung ist $S$ mal die Änderung der eigenen $U_\mathrm{BE}$, also ändern sich beide $U_\mathrm{BE}$ entgegengesetzt gleich; weil ihre Differenz $U_\mathrm{D}$ ist, trägt jede Strecke $\pm U_\mathrm{D}/2$.
---
Also ist $\Delta I_\mathrm{C2}=S\,U_\mathrm{D}/2$ und $U_\mathrm{A}=2R_\mathrm{C}\,\Delta I_\mathrm{C2}=S\,R_\mathrm{C}\,U_\mathrm{D}$, weil sich beide Kollektoren entgegengesetzt um $R_\mathrm{C}\,\Delta I_\mathrm{C2}$ bewegen.
:::
:::karte zusammenhang Gleichtakt wirkungslos
Warum ändert sich am Ausgang eines Differenzverstärkers nichts, wenn beide Basen um dasselbe Stück steigen?
---
Der Emitterknoten E steigt mit, weil die Stromquelle T3 den Summenstrom $I_0$ und damit auch $U_\mathrm{BE}$ festhält. Die Ströme und ihre Aufteilung bleiben, also auch die Spannungen an den Kollektoren.
--- falsch
Beide Kollektorströme wachsen um denselben Betrag, und beide Kollektorspannungen sinken gleich stark. Die Differenz bleibt deshalb null, obwohl sich beide Ströme ändern und insgesamt mehr Strom fließt.
--- falsch
Bei gleicher Basisspannung fließen keine Basisströme, und beide Transistoren sperren kurz. Erst eine Differenz der Eingänge schaltet einen von ihnen wieder ein.
--- falsch
Der Knoten E bleibt fest, weil T3 sein Potenzial hält. Beide $U_\mathrm{BE}$ steigen gleich, beide Ströme wachsen gleich, und ihre Wirkungen heben sich am Ausgang gerade auf.
:::
:::karte zusammenhang Halbe Differenz an jeder BE-Strecke
Warum liegt an jedem Transistor des Differenzverstärkers nur die halbe Differenz, wenn man nur eine Basis anhebt?
---
Weil der Knoten E um die Hälfte mitgeht: T2 will mehr Strom, die Summe ist aber fest, also hebt sich E, bis T1 genau so viel abgibt.
--- falsch
Weil an einem Basiswiderstand die Hälfte der Spannung abfällt; ohne diesen Widerstand läge die ganze Differenz an der Strecke des angehobenen Transistors.
--- falsch
Weil der Knoten E fest bleibt und die Stromquelle T3 die Hälfte der Differenz aufnimmt; die andere Hälfte liegt an der Strecke des angehobenen Transistors.
--- falsch
Das gilt nur bei gleichen Kollektorwiderständen; bei ungleichen liegt die ganze Differenz an dem Transistor mit dem kleineren Kollektorwiderstand.
:::
:::karte zusammenhang Linearer Bereich
Was passiert mit der Ausgangsspannung eines Differenzverstärkers, wenn $|U_\mathrm{D}|$ viel größer als $U_T$ wird?
---
Der ganze Strom fließt durch einen Transistor, und $U_\mathrm{A}$ nähert sich $\pm R_\mathrm{C}I_0$. Der lineare Bereich ist nur wenige $U_T$ breit.
--- falsch
$U_\mathrm{A}$ wächst weiter mit $A_\mathrm{D}\,U_\mathrm{D}$, bis die Versorgungsspannung erreicht ist; der lineare Bereich reicht also über viele Volt am Eingang.
--- falsch
Beide Transistoren sperren, weil die Differenz die Basis-Emitter-Spannung übersteigt; $U_\mathrm{A}$ fällt dann auf null zurück, bis $U_\mathrm{D}$ wieder klein ist.
--- falsch
Der Strom teilt sich weiter gleich auf, aber $U_\mathrm{A}$ steigt exponentiell mit $U_\mathrm{D}$, weil die Kennlinien der Transistoren exponentiell verlaufen.
:::
:::karte zusammenhang Vom Differenzverstärker zum OPV
Warum bleibt die Verstärkung einer Differenzstufe mit Kollektorwiderständen bei einigen Hundert, und wie erreicht der OPV trotzdem $10^5$ bis $10^6$?
---
In $A_\mathrm{D}=U_{R_\mathrm{C}}/U_T$ kann $U_{R_\mathrm{C}}$ die Versorgung nicht übersteigen. Ein Stromspiegel bringt $S\,r_\mathrm{CE}/2=U_\mathrm{Early}/(2U_T)\approx1400$; dahinter folgen eine Spannungsverstärkerstufe und ein Emitterfolger.
--- falsch
$U_T$ ist mit 26 mV zu groß; der OPV kühlt seine Eingangstransistoren, damit $U_T$ sinkt, und erreicht so schon in einer einzigen Stufe $10^5$.
--- falsch
Die Basisströme begrenzen $A_\mathrm{D}$; der OPV nimmt deshalb Kollektorwiderstände von vielen Megaohm und erreicht damit in einer Stufe $10^5$ bis $10^6$ ohne weitere Stufen.
--- falsch
Größere Kollektorwiderstände würden die Transistoren sperren; der OPV schaltet deshalb zehn gleiche Differenzstufen mit Widerständen hintereinander, deren Verstärkungen sich multiplizieren.
:::
:::karte zusammenhang Eingangswiderstand der Differenzstufe
Warum hat eine Differenzstufe mit 20 µ A Summenstrom einen viel größeren Eingangswiderstand als eine mit 2 mA?
---
Das Signal liegt an zwei BE-Strecken in Reihe, der Eingangswiderstand ist $2\,r_\mathrm{BE}=2B/S$. Die Steilheit sinkt mit dem Strom, also steigt der Widerstand.
--- falsch
Bei kleinem Strom sperren die Transistoren fast, und ein gesperrter Transistor hat einen unendlichen Eingangswiderstand; bei 20 µ A ist er praktisch unendlich.
--- falsch
Der Eingangswiderstand ist $2\,r_\mathrm{BE}=2S/B$; bei kleinem Strom wächst die Steilheit, deshalb steigt der Widerstand hundertfach auf 1,04 M$\Omega$.
--- falsch
Der Eingangswiderstand hängt nur von $R_\mathrm{C}$ ab; bei kleinem Strom wählt man $R_\mathrm{C}$ hundertmal größer, damit die Verstärkung gleich bleibt.
:::
::::

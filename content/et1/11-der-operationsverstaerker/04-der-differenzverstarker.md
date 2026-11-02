---
title: Stufe 2: Der Differenzverstärker
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Der Operationsverstärker
order: 1210400
summary: Eine Störung auf beiden Leitungen soll verschwinden, der Unterschied zwischen ihnen soll verstärkt werden.
tags: Gleichtaktspannung, nicht-invertierender Eingang, invertierender Eingang
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Eine Störung auf beiden Leitungen soll verschwinden, der Unterschied zwischen ihnen soll verstärkt werden. Dazu braucht man eine Schaltung, deren Ausgang nur von der Differenz zweier Spannungen abhängt.
:::

**Die Idee.** Zwei gleiche Transistoren T1 und T2 hängen mit den Emittern am gemeinsamen Knoten E (Abb. [2](#abb-2)). Darunter sitzt T3. Seine Basis liegt an der festen Spannung $U_\mathrm{bias}$, deshalb wirkt er als Stromquelle ([Teil 10](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor/der-bipolartransistor.html)) und zieht den festen Strom $I_0$ aus dem Knoten. Die Basisströme sind klein, also gilt $I_\mathrm{C1}+I_\mathrm{C2}=I_0$. Die Summe steht fest, nur die Aufteilung kann sich ändern.

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

**Beispiel.** In Ruhe fließen je 1 mA, die Kollektoren liegen bei $12\,\mathrm{V}-3\,\mathrm{V}=9$ V. $S=38{,}5$ mS, also $A_\mathrm{D}=3\,\mathrm{V}/26\,\mathrm{mV}=115$. Bei $U_\mathrm{D}=1$ mV wandert $\pm19{,}2$ µ A zwischen den Zweigen, jeder Kollektor bewegt sich um 57,7 mV, zusammen sind das $U_\mathrm{A}=115$ mV. Eine Störung von 100 mV auf beiden Eingängen ändert daran nichts. **Grenzfälle:** $U_\mathrm{D}=0$ ergibt $I_0/2$ je Zweig. Bei $|U_\mathrm{D}|\gg U_T$ fließt alles durch einen Transistor, $U_\mathrm{A}\to\pm R_\mathrm{C}I_0=\pm6$ V. Der lineare Bereich ist nur wenige $U_T$ breit: Bei 26 mV liefert die Gerade 3,0 V, die exakte Kurve 2,77 V.

**Eingang.** Ein Eingangssignal $U_\mathrm{D}$ liegt an zwei BE-Strecken in Reihe, der Eingangswiderstand ist $2\,r_\mathrm{BE}=2B/S=10{,}4$ k$\Omega$. Bei 20 µ A Summenstrom statt 2 mA sind es 1,04 M$\Omega$, und jede Basis zieht nur 50 nA. Daher stammen $r_\mathrm{e}$ und $I_\mathrm{B}$ im Rechenmodell.

**Vom Differenzverstärker zum OPV.** $A_\mathrm{D}=U_{R_\mathrm{C}}/U_T$ bleibt bei einigen Hundert, denn $U_{R_\mathrm{C}}$ kann die Versorgung nicht übersteigen. Ein Stromspiegel ([Teil 10](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor/der-bipolartransistor.html)) statt der Widerstände führt beide Stromänderungen auf eine Seite und wirkt dort wie die Parallelschaltung zweier $r_\mathrm{CE}$. Das ergibt $S\,r_\mathrm{CE}/2=U_\mathrm{Early}/(2U_T)\approx1400$. Dahinter folgen eine Spannungsverstärkerstufe und ein Emitterfolger für den niedrigen Ausgangswiderstand. Zusammen sind es $10^5$ bis $10^6$. Dieser Wert hängt von $B$, $U_\mathrm{Early}$ und der Temperatur ab: groß, aber ungenau.

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

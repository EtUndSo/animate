---
title: Stufe 6: Mehrere Eingänge, mehrere Stufen
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Der Operationsverstärker
order: 1210800
summary: Die Regel galt für einen Eingang und einen OPV.
tags: Addierer, Subtrahierer
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Die Regel galt für einen Eingang und einen OPV. Diese Stufe zeigt, dass sie mehrere Eingänge und ganze Ketten ohne neue Idee behandelt, weil alle Gleichungen linear bleiben.
:::

**Die Idee.** Im __Addierer__ führen mehrere Widerstände auf den Minus-Eingang (Abb. [8](#abb-8)). Der Knoten bleibt auf 0 V, jede Quelle sieht also nur ihren eigenen Widerstand und treibt $U_{\mathrm{E}i}/R_{\mathrm{E}i}$, unabhängig von den anderen. Die virtuelle Masse entkoppelt die Quellen. Alle Ströme zusammen fließen durch $R_\mathrm{F}$, den Widerstand der Rückführung. Im __Subtrahierer__ kommt eine Spannung an jeden Eingang. Hier hilft die Überlagerung aus [Teil 5](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html): Man rechnet jede Quelle für sich, die andere wird zum Draht.

:::satz Satz 6.1 (Addierer, Subtrahierer, Kette)
<span class="anker" id="satz-6-1"></span>

<span class="anker" id="gl-6-1"></span>
$$U_\mathrm{A}=-R_\mathrm{F}\sum_i\frac{U_{\mathrm{E}i}}{R_{\mathrm{E}i}}, \tag{6.1}$$

<span class="anker" id="gl-6-2"></span>
$$U_\mathrm{A}=\frac{R_1+R_2}{R_1}\cdot\frac{R_4}{R_3+R_4}\,U_\mathrm{E2}-\frac{R_2}{R_1}\,U_\mathrm{E1}. \tag{6.2}$$

Für $R_3=R_1$ und $R_4=R_2$ bleibt $U_\mathrm{A}=\frac{R_2}{R_1}\,(U_\mathrm{E2}-U_\mathrm{E1})$. Stufen in Kette multiplizieren sich: $G=G_1\,G_2$.
:::

⁠**So liest man das:** In [(6.2)](#gl-6-2) liegen $U_\mathrm{E1}$ über $R_1$ am Minus-Eingang und $U_\mathrm{E2}$ am Teiler $R_3$, $R_4$ vor dem Plus-Eingang, $R_2$ führt zurück. **Gültigkeit:** OPV im linearen Bereich. Bei der Überlagerung muss nur die Summe in den Grenzen liegen, die Teilergebnisse sind Rechengrößen.

:::herleitung Subtrahierer durch Überlagerung
Mit $U_\mathrm{E2}=0$ fließt durch $R_3$, $R_4$ kein Strom, der Plus-Eingang liegt auf 0 V. Das ist der Invertierer: $U_\mathrm{A1}=-(R_2/R_1)\,U_\mathrm{E1}$. Mit $U_\mathrm{E1}=0$ wird die Quelle zum Draht, $R_1$ bleibt also an Masse und darf nicht entfallen, denn der Ausgang treibt über $R_2$ Strom hindurch. Das ist der nicht-invertierende Verstärker mit $\varphi_+=U_\mathrm{E2}\,R_4/(R_3+R_4)$: $U_\mathrm{A2}=\bigl(1+R_2/R_1\bigr)\varphi_+$. Die Summe ist [(6.2)](#gl-6-2).
:::

:::abbildung et1/k11addsub 8
Links der Addierer: Die Ströme der drei Quellen treffen sich am Knoten und fließen durch $R_\mathrm{F}$. Rechts der Subtrahierer mit $R_1=R_3$ und $R_2=R_4$: Bei 2,00 V und 2,05 V liegen beide Eingänge auf 1,64 V.
:::

::::beispiel [Beispiele]
⁠*Addierer* mit $R_\mathrm{F}=40$ k$\Omega$, $R_\mathrm{E1}=R_\mathrm{E2}=10$ k$\Omega$, $R_\mathrm{E3}=20$ k$\Omega$ und $0{,}5$ V, $-0{,}2$ V, $0{,}1$ V: Die Ströme sind 50, $-20$ und 5 µ A, zusammen 35 µ A, also $U_\mathrm{A}=-1{,}4$ V. *Subtrahierer* mit $R_1=R_3=10$ k$\Omega$, $R_2=R_4=40$ k$\Omega$, $U_\mathrm{E1}=2{,}00$ V, $U_\mathrm{E2}=2{,}05$ V: $\varphi_+=0{,}8\cdot2{,}05\,\mathrm{V}=1{,}64$ V. Durch $R_1$ fließen $(2{,}00-1{,}64)\,\mathrm{V}/10\,\mathrm{k\Omega}=36$ µ A, also $U_\mathrm{A}=1{,}64\,\mathrm{V}-36\,\mu\text{A}\cdot40\,\mathrm{k\Omega}=0{,}2$ V. Die Überlagerung ergibt $-8{,}0\,\mathrm{V}+8{,}2\,\mathrm{V}$, dasselbe. Der Gleichtakt von rund 2 V ist fort. *Kette* aus zwei Invertierern mit $G_1=-4$ und $G_2=-2$: Aus 0,5 V wird $-2$ V, dann $+4$ V, also $G=+8$.
::::

⁠**Grenzfall:** $U_\mathrm{E1}=U_\mathrm{E2}$ ergibt 0.

**Vorgehen bei größeren Schaltungen.** Zuerst die Potenziale der Eingänge bestimmen, dann Stufe für Stufe von links nach rechts rechnen. In einer Kette ist jeder Ausgang der Eingang der nächsten Stufe, ein Potenzial mit festem Wert.

:::frage In Teil 6 belasteten sich Zweitore in einer Kette gegenseitig. Warum darf ich hier multiplizieren?
Weil der Ausgangswiderstand der ersten Stufe fast null ist. Die 10 k$\Omega$ der zweiten Stufe belasten 3,75 m$\Omega$, der Spannungsverlust ist $4\cdot10^{-7}$ des Werts. Die Schleife der ersten Stufe gleicht ihn aus.
:::

:::aufgabe Aufgabe 6 ★★★ Addierer und ungleiche Widerstände
<span class="anker" id="aufg-6"></span>

(a) Ein Addierer hat $R_\mathrm{F}=20$ k$\Omega$ und die Eingangswiderstände 10, 20 und 5 k$\Omega$. Wie groß ist $U_\mathrm{A}$ für 1 V, $-2$ V und 0,5 V? (b) Am Subtrahierer aus dem Beispiel weicht $R_4$ um 1 % nach oben ab (40,4 k$\Omega$). Berechne die Faktoren vor $U_\mathrm{E2}$ und $U_\mathrm{E1}$. (c) Welche Ausgangsspannung entsteht bei $U_\mathrm{E1}=U_\mathrm{E2}=2$ V? (d) Welchen Wert hat $U_\mathrm{A}$ nun bei 2,00 V und 2,05 V? Warum muss ein Subtrahierer eng tolerierte Widerstände haben?

:::loesung
(a) $U_\mathrm{A}=-(2\cdot1+1\cdot(-2)+4\cdot0{,}5)\,\mathrm{V}=-2$ V. (b) Vor $U_\mathrm{E2}$: $5\cdot40{,}4/50{,}4=4{,}0079$, vor $U_\mathrm{E1}$: 4. (c) $2\,\mathrm{V}\cdot0{,}0079=15{,}9$ mV statt 0. (d) $4{,}0079\cdot2{,}05\,\mathrm{V}-8\,\mathrm{V}=0{,}216$ V statt 0,200 V. Die 8 % Fehler stammen fast nur aus dem Gleichtakt. Ein Widerstand mit 1 % Abweichung macht die Unterdrückung $4/0{,}0079$, also 54 dB, schlechter als der OPV selbst.
:::
:::

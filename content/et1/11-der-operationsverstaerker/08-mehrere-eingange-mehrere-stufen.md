---
title: Stufe 6: Mehrere Eingänge, mehrere Stufen
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Der Operationsverstärker
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-operationsverstarker
knoten: Kapitel 11: Der Operationsverstärker
order: 1210800
summary: Die Regel galt für einen Eingang und einen OPV.
tags: Addierer, Subtrahierer
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Die Regel galt für einen Eingang und einen OPV. Diese Stufe zeigt, dass sie mehrere Eingänge und ganze Ketten ohne neue Idee behandelt, weil alle Gleichungen linear bleiben.
:::

**Die Idee.** Im __Addierer__ führen mehrere Widerstände auf den Minus-Eingang (Abb. [8](#abb-8)). Der Knoten bleibt auf 0 V, jede Quelle sieht also nur ihren eigenen Widerstand und treibt $U_{\mathrm{E}i}/R_{\mathrm{E}i}$, unabhängig von den anderen. Die virtuelle Masse entkoppelt die Quellen. Alle Ströme zusammen fließen durch $R_\mathrm{F}$, den Widerstand der Rückführung. Im __Subtrahierer__ kommt eine Spannung an jeden Eingang. Hier hilft die Überlagerung aus [Kapitel 5](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html): Man rechnet jede Quelle für sich, die andere wird zum Draht.

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

:::frage In Kapitel 6 belasteten sich Zweitore in einer Kette gegenseitig. Warum darf ich hier multiplizieren?
Weil der Ausgangswiderstand der ersten Stufe fast null ist. Die 10 k$\Omega$ der zweiten Stufe belasten 3,75 m$\Omega$, der Spannungsverlust ist $4\cdot10^{-7}$ des Werts. Die Schleife der ersten Stufe gleicht ihn aus.
:::

:::aufgabe Aufgabe 6 ★★★ Addierer und ungleiche Widerstände
<span class="anker" id="aufg-6"></span>

(a) Ein Addierer hat $R_\mathrm{F}=20$ k$\Omega$ und die Eingangswiderstände 10, 20 und 5 k$\Omega$. Wie groß ist $U_\mathrm{A}$ für 1 V, $-2$ V und 0,5 V? (b) Am Subtrahierer aus dem Beispiel weicht $R_4$ um 1 % nach oben ab (40,4 k$\Omega$). Berechne die Faktoren vor $U_\mathrm{E2}$ und $U_\mathrm{E1}$. (c) Welche Ausgangsspannung entsteht bei $U_\mathrm{E1}=U_\mathrm{E2}=2$ V? (d) Welchen Wert hat $U_\mathrm{A}$ nun bei 2,00 V und 2,05 V? Warum muss ein Subtrahierer eng tolerierte Widerstände haben?

:::loesung
(a) $U_\mathrm{A}=-(2\cdot1+1\cdot(-2)+4\cdot0{,}5)\,\mathrm{V}=-2$ V. (b) Vor $U_\mathrm{E2}$: $5\cdot40{,}4/50{,}4=4{,}0079$, vor $U_\mathrm{E1}$: 4. (c) $2\,\mathrm{V}\cdot0{,}0079=15{,}9$ mV statt 0. (d) $4{,}0079\cdot2{,}05\,\mathrm{V}-8\,\mathrm{V}=0{,}216$ V statt 0,200 V. Die 8 % Fehler stammen fast nur aus dem Gleichtakt. Ein Widerstand mit 1 % Abweichung macht die Unterdrückung $4/0{,}0079$, also 54 dB, schlechter als der OPV selbst.
:::
:::

::::formelsammlung
**Addierer**

$$U_\mathrm{A}=-R_\mathrm{F}\sum_i\frac{U_{\mathrm{E}i}}{R_{\mathrm{E}i}}$$

Eingänge über $R_{\mathrm{E}i}$ am Minus-Eingang, $R_\mathrm{F}$ in der Rückführung. Die virtuelle Masse entkoppelt die Quellen.

**Subtrahierer**

$$U_\mathrm{A}=\frac{R_1+R_2}{R_1}\cdot\frac{R_4}{R_3+R_4}\,U_\mathrm{E2}-\frac{R_2}{R_1}\,U_\mathrm{E1}$$

$U_\mathrm{E1}$ über $R_1$ am Minus-Eingang, $U_\mathrm{E2}$ am Teiler $R_3$, $R_4$ vor dem Plus-Eingang, $R_2$ führt zurück. OPV im linearen Bereich; bei der Überlagerung muss nur die Summe in den Grenzen liegen.

**Subtrahierer mit gleichen Widerstandspaaren**

$$U_\mathrm{A}=\frac{R_2}{R_1}\,(U_\mathrm{E2}-U_\mathrm{E1})$$

Für $R_3=R_1$ und $R_4=R_2$; der Gleichtakt fällt nur heraus, wenn die Widerstände genau stimmen.

**Stufen in Kette**

$$G=G_1\,G_2$$

Erlaubt, weil der Ausgangswiderstand jeder gegengekoppelten Stufe fast null ist.
::::

::::lernkarten
:::karte begriff Addierer
Wie ist ein Addierer mit einem OPV aufgebaut, und was gibt er aus?
---
Mehrere Widerstände führen Eingangsspannungen auf den Minus-Eingang, $R_\mathrm{F}$ führt zurück. Der Ausgang ist die gewichtete Summe mit umgekehrtem Vorzeichen, $U_\mathrm{A}=-R_\mathrm{F}\sum_i\frac{U_{\mathrm{E}i}}{R_{\mathrm{E}i}}$.
--- falsch
Mehrere Widerstände führen die Eingänge auf den Plus-Eingang, $R_\mathrm{F}$ führt zurück. Der Ausgang ist die Summe mit gleichem Vorzeichen, $U_\mathrm{A}=R_\mathrm{F}\sum_i U_{\mathrm{E}i}/R_{\mathrm{E}i}$, weil der Plus-Eingang nicht invertiert.
--- falsch
Mehrere OPV-Stufen in Kette, jede mit einem eigenen Eingang. Der Ausgang ist die Summe der einzelnen Verstärkungen, $G=G_1+G_2$, mal der Eingangsspannung.
--- falsch
Mehrere Widerstände führen auf den Minus-Eingang. Der Ausgang ist der Mittelwert der Eingänge, $U_\mathrm{A}=-\frac{1}{n}\sum_i U_{\mathrm{E}i}$, unabhängig von den Widerständen.
:::
:::karte zusammenhang Entkoppelte Quellen
Warum beeinflussen sich die Quellen an einem Addierer gegenseitig nicht?
---
Der Knoten am Minus-Eingang bleibt auf 0 V; jede Quelle sieht nur ihren eigenen Widerstand und treibt $U_{\mathrm{E}i}/R_{\mathrm{E}i}$. Die virtuelle Masse entkoppelt die Quellen.
--- falsch
Jede Quelle hat einen sehr großen Innenwiderstand, ihr Strom hängt deshalb nicht von der Spannung am Knoten ab; der Knoten selbst bewegt sich aber mit den Eingängen.
--- falsch
Die Eingangswiderstände sind alle gleich groß gewählt; bei ungleichen Widerständen würden sich die Quellen über den Knoten gegenseitig belasten.
--- falsch
Der Knoten am Minus-Eingang folgt der größten Eingangsspannung; die Quellen mit kleinerer Spannung sind dann gesperrt und belasten nichts.
:::
:::karte begriff Subtrahierer
Wie ist ein Subtrahierer beschaltet, und was gibt er bei passend gewählten Widerständen aus?
---
$U_\mathrm{E1}$ liegt über $R_1$ am Minus-Eingang, $U_\mathrm{E2}$ über den Teiler $R_3$, $R_4$ am Plus-Eingang, und $R_2$ führt zurück. Für $R_3=R_1$ und $R_4=R_2$ gibt er $U_\mathrm{A}=\frac{R_2}{R_1}\,(U_\mathrm{E2}-U_\mathrm{E1})$ aus.
--- falsch
Beide Spannungen liegen über je einen Widerstand am Minus-Eingang, eine davon mit umgedrehter Polung. Der Ausgang ist $-(U_\mathrm{E2}-U_\mathrm{E1})$, unabhängig von den Widerständen.
--- falsch
$U_\mathrm{E1}$ liegt direkt am Plus-Eingang, $U_\mathrm{E2}$ direkt am Minus-Eingang, ganz ohne Widerstände. Der Ausgang ist dann $A\,(U_\mathrm{E1}-U_\mathrm{E2})$.
--- falsch
$U_\mathrm{E1}$ liegt über $R_1$ am Minus-Eingang, $U_\mathrm{E2}$ über den Teiler am Plus-Eingang. Für $R_3=R_1$ und $R_4=R_2$ gibt er $U_\mathrm{A}=\frac{R_1}{R_2}\,(U_\mathrm{E1}-U_\mathrm{E2})$ aus.
:::
:::karte formel Subtrahierer mit beliebigen Widerständen
Wie hängt die Ausgangsspannung eines Subtrahierers allgemein von $U_\mathrm{E1}$, $U_\mathrm{E2}$ und den vier Widerständen ab?
---
$U_\mathrm{A}=\frac{R_1+R_2}{R_1}\cdot\frac{R_4}{R_3+R_4}\,U_\mathrm{E2}-\frac{R_2}{R_1}\,U_\mathrm{E1}$. Der erste Teil ist der nicht-invertierende Verstärker hinter dem Teiler $R_3$, $R_4$, der zweite der Invertierer.
--- falsch
$U_\mathrm{A}=\frac{R_4}{R_3+R_4}\,U_\mathrm{E2}-\frac{R_2}{R_1}\,U_\mathrm{E1}$: Der Plus-Zweig ist nur der Teiler, dessen Spannung der OPV unverstärkt weitergibt; gilt im linearen Bereich des OPV.
--- falsch
$U_\mathrm{A}=\frac{R_2}{R_1}\,(U_\mathrm{E2}-U_\mathrm{E1})$ für beliebige $R_3$ und $R_4$: Der Teiler am Plus-Eingang beeinflusst das Ergebnis nicht, nur $R_1$ und $R_2$ zählen für die Verstärkung der Differenz.
--- falsch
$U_\mathrm{A}=\frac{R_1+R_2}{R_1}\cdot\frac{R_4}{R_3+R_4}\,U_\mathrm{E1}-\frac{R_2}{R_1}\,U_\mathrm{E2}$: $U_\mathrm{E1}$ wirkt über den Teiler, $U_\mathrm{E2}$ über $R_1$; gilt im linearen Bereich.
:::
:::karte herleitung Subtrahierer durch Überlagerung
Wie folgt die Ausgangsspannung des Subtrahierers aus der Überlagerung der Wirkungen von $U_\mathrm{E1}$ und $U_\mathrm{E2}$?
---
Mit $U_\mathrm{E2}=0$ fließt durch $R_3$, $R_4$ kein Strom, und der Plus-Eingang liegt auf 0 V, weil kein Strom in den Eingang fließt.
---
Das ist der Invertierer, $U_\mathrm{A1}=-(R_2/R_1)\,U_\mathrm{E1}$, weil $U_\mathrm{E1}$ über $R_1$ am Minus-Eingang liegt und $R_2$ zurückführt.
---
Mit $U_\mathrm{E1}=0$ wird die Quelle zum Draht, und $R_1$ bleibt an Masse; er darf nicht entfallen, weil der Ausgang über $R_2$ Strom durch ihn treibt.
---
Das ist der nicht-invertierende Verstärker mit $\varphi_+=U_\mathrm{E2}\,R_4/(R_3+R_4)$, also $U_\mathrm{A2}=\bigl(1+R_2/R_1\bigr)\varphi_+$, weil der Teiler den Plus-Eingang speist.
---
Die Summe beider Teilergebnisse ist die Formel des Subtrahierers, weil alle Gleichungen linear sind und sich die Wirkungen überlagern.
:::
:::karte formel Kette von Stufen
Wie berechnet man die Verstärkung zweier OPV-Stufen in Kette, und warum darf man dabei einfach multiplizieren?
---
$G=G_1\,G_2$. Der Ausgangswiderstand der ersten Stufe ist fast null, hier 3,75 m$\Omega$; die 10 k$\Omega$ der zweiten Stufe kosten nur $4\cdot10^{-7}$ des Werts.
--- falsch
$G=G_1+G_2$, weil sich die Ausgangsspannungen der beiden Stufen addieren; zwei Invertierer mit $G_1=-4$ und $G_2=-2$ ergeben also zusammen $G=-6$.
--- falsch
$G=G_1\,G_2$, aber nur mit einem Impedanzwandler dazwischen; ohne ihn belastet die zweite Stufe die erste so stark, dass die Rechnung nicht mehr stimmt.
--- falsch
$G=G_1\,G_2/(G_1+G_2)$, weil sich zwei Stufen wie parallele Widerstände gegenseitig belasten; die Kette verstärkt also weniger als jede Stufe allein.
:::
:::karte zusammenhang Gleichtakt am Subtrahierer
Warum verschwindet am Subtrahierer mit $R_3=R_1$ und $R_4=R_2$ der gemeinsame Anteil beider Eingangsspannungen?
---
Beide Eingänge werden mit demselben Faktor $R_2/R_1$ gewichtet, einmal positiv, einmal negativ. Bei 2,00 V und 2,05 V bleibt nur die verstärkte Differenz, 0,2 V.
--- falsch
Der OPV unterdrückt den Gleichtakt selbst mit 90 dB; die Widerstände spielen dafür keine Rolle, sie legen nur die Verstärkung der Differenz fest.
--- falsch
Beide Eingänge liegen auf 0 V, weil der Minus-Eingang eine virtuelle Masse ist; die gemeinsame Spannung erreicht den OPV deshalb überhaupt nicht.
--- falsch
Der gemeinsame Anteil wird in den Widerständen in Wärme umgesetzt; nur die Differenz der Eingänge treibt einen Strom durch $R_2$ zum Ausgang.
:::
:::karte zusammenhang Eng tolerierte Widerstände
Warum braucht ein Subtrahierer eng tolerierte Widerstände?
---
Weicht ein Widerstand ab, sind die Faktoren beider Eingänge ungleich, und der Gleichtakt erscheint am Ausgang. Schon 1 % Abweichung von $R_4$ macht aus 2 V Gleichtakt 15,9 mV.
--- falsch
Ungenaue Widerstände rauschen stärker; ihr Rauschen wird mit $R_2/R_1$ verstärkt und überdeckt kleine Differenzen der beiden Eingangsspannungen.
--- falsch
Weicht ein Widerstand ab, ändert sich nur die Verstärkung der Differenz um denselben Prozentsatz; der Gleichtakt bleibt dabei vollständig unterdrückt, solange der OPV ideal ist.
--- falsch
Weicht ein Widerstand ab, geht die virtuelle Masse verloren, und der Ausgang schlägt an; mit 1 % Abweichung steht er bei 2 V Gleichtakt schon auf 11 V am oberen Anschlag.
:::
:::karte zusammenhang Teilergebnisse der Überlagerung
Warum darf ein Teilergebnis der Überlagerung am Subtrahierer, etwa $-8{,}0$ V, nahe an der Grenze des Ausgangs oder sogar darüber liegen?
---
Die Teilergebnisse sind Rechengrößen, die der Ausgang nie wirklich annimmt. Er führt nur ihre Summe, hier 0,2 V, und nur sie muss in den Grenzen liegen.
--- falsch
Es darf das nicht: Jedes Teilergebnis muss für sich in den Grenzen liegen, sonst ist die Überlagerung ungültig, auch wenn die Summe passt und der Ausgang nicht anschlägt.
--- falsch
Weil man die Teilergebnisse quadratisch addiert, da die Quellen unabhängig sind; die Summe ist dann mit rund 11,5 V gerade noch erlaubt.
--- falsch
Weil der Ausgang die Teilergebnisse nacheinander durchläuft und dabei nur kurz anschlägt; der Fehler ist danach wieder ausgeregelt.
:::
::::

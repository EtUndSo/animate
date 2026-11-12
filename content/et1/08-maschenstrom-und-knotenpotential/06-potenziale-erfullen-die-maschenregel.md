---
title: Stufe 4: Potenziale erfüllen die Maschenregel
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Maschenstrom- und Knotenpotentialverfahren
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/maschenstrom-und-knotenpotentialverfahren
knoten: Kapitel 8: Maschenstrom- und Knotenpotentialverfahren
order: 1180600
summary: Von z Spannungen sind nur k-1 frei.
tags: 
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Von $z$ Spannungen sind nur $k-1$ frei. Diese Stufe zeigt, warum die Potenziale der Knoten diese Rolle übernehmen und warum die Maschenregel dabei von selbst gilt.
:::

**Die Idee.** Jeder Knoten hat ein Potenzial ([Kapitel 1](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)), wie jeder Punkt einer Landschaft eine Höhe. Die Spannung eines Zweigs ist der Höhenunterschied seiner Enden. Wer im Kreis läuft, kommt auf der Ausgangshöhe an, gleich welche Höhen man den Knoten zugewiesen hat (Abb. [4](#abb-4)). Die Maschenregel lässt sich so gar nicht verletzen. Da nur Differenzen zählen, darf man eine Höhe frei festlegen. Das spart eine Unbekannte, und es bleiben $k-1$.

:::abbildung et1/k8hoehen 4
Die Knoten des Rechenmodells als Höhen. Der Umlauf von 0 über 1 und 2 zurück nach 0 steigt um 8 V und 2 V und fällt um 10 V. Die Summe ist null, und sie bliebe null, wenn man die Höhen 1 und 2 beliebig verschöbe.
:::

:::definition Definition 4.1 (Bezugsknoten und Knotenpotential)
<span class="anker" id="satz-4-1"></span>

Ein frei gewählter Knoten 0 ist der *Bezugsknoten*, sein Potenzial ist $\varphi_0=0$. Das *Knotenpotential* eines anderen Knotens $\mu$ ist seine Spannung gegen den Bezugsknoten:

<span class="anker" id="gl-4-1"></span>
$$U_\mu=\varphi_\mu-\varphi_0. \tag{4.1}$$

Die Spannung eines Zweigs zwischen den Knoten $\mu$ und $\nu$ ist $U_{\mu\nu}=U_\mu-U_\nu$, zum Bezugsknoten hin $U_{\mu0}=U_\mu$.
:::

:::satz Satz 4.2 (Knotenpotentiale)
<span class="anker" id="satz-4-2"></span>

Für beliebige Werte der $k-1$ Knotenpotentiale ist jede Maschenregel erfüllt. Umgekehrt gehört zu jeder Spannungsverteilung, die die Maschenregel erfüllt, genau ein Satz Knotenpotentiale.
:::

:::herleitung Warum das immer geht
⁠*Maschenregel.* Längs einer Masche über die Knoten $1,2,\dots,N$ ist $(U_1-U_2)+(U_2-U_3)+\dots+(U_N-U_1)=0$. Jedes Potenzial tritt einmal mit $+$ und einmal mit $-$ auf.

⁠*Vollständigkeit.* Man wählt einen Baum. Zwischen dem Bezugsknoten und jedem Knoten gibt es darin genau einen Weg. Die Summe der Zweigspannungen längs dieses Wegs definiert das Knotenpotential eindeutig. Für die Baumzweige stimmen damit alle Differenzen. Für jeden Verbindungszweig stimmt sie, weil er mit Baumzweigen eine Masche schließt, deren Regel nach Voraussetzung gilt.
:::

⁠**So liest man das:** $U_\mu$ ist eine Spannung mit Pfeil von Knoten $\mu$ zum Bezugsknoten, Einheit Volt. Im Schaltplan zeigt das Massezeichen den Bezugsknoten an, in SPICE heißt er immer 0. Den Bezugsknoten wählt man dort, wo die meisten Zweige zusammenkommen, dann werden die Gleichungen am kürzesten. **Gültigkeit:** Das Feld muss wirbelfrei sein. Ein veränderliches Magnetfeld durch eine Masche zerstört die Potenziale ([Kapitel 1](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)), in Schaltungen sitzt es in Spulen.

::::beispiel
Im Rechenmodell sind $U_1=8$ V und $U_2=10$ V, wie Stufe [3](das-maschenstromverfahren.html#stufe-3) ergab. Die Spannung an $R_3$ ist $U_{12}=U_1-U_2=-2$ V, also liegt Knoten 2 höher, und der Strom läuft von 2 nach 1. Mit $R_3=2\,\mathrm{k\Omega}$ sind das die 1 mA aus Stufe [3](das-maschenstromverfahren.html#stufe-3). Der Umlauf ergibt $(U_1-U_2)+U_2-U_1=0$ auch für jedes andere Zahlenpaar.
::::

⁠**Grenzfall:** Ein Netz mit $k=2$ hat ein einziges Knotenpotential. Das ist die gemeinsame Spannung einer Parallelschaltung.

:::frage Ist das Knotenpotential nun ein Potenzial oder eine Spannung?
Beides. Ein Potenzial für sich hat nur gegenüber einem Nullpunkt einen Wert ([Kapitel 1](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)). Das Knotenpotential ist die Spannung gegen den gewählten Nullpunkt, deshalb trägt es das Zeichen $U$. Ein Wechsel des Bezugsknotens ändert alle Knotenpotentiale, aber keine einzige Zweigspannung.
:::

:::aufgabe Aufgabe 5 ★ Bezug wechseln
<span class="anker" id="aufg-5"></span>

Wähle im Rechenmodell Knoten 2 als Bezugsknoten. (a) Welche Knotenpotentiale haben die untere Leitung und Knoten 1? (b) Berechne daraus die Spannung zwischen Knoten 1 und unterer Leitung. (c) Warum ändert sich kein Strom?

:::loesung
(a) Alle Potenziale sinken um 10 V: untere Leitung $-10$ V, Knoten 1 $-2$ V, Knoten 2 0 V.

(b) $-2\,\mathrm{V}-(-10\,\mathrm{V})=8$ V, wie vorher.

(c) Ströme hängen nur von Differenzen ab, und die bleiben gleich.
:::
:::

::::formelsammlung
**Knotenpotential**

$$U_\mu=\varphi_\mu-\varphi_0$$

Spannung des Knotens $\mu$ gegen den frei gewählten Bezugsknoten 0 mit $\varphi_0=0$, Pfeil vom Knoten zum Bezugsknoten, Einheit Volt. Ein Wechsel des Bezugsknotens ändert alle Knotenpotentiale, aber keine Zweigspannung. Gilt, solange das Feld wirbelfrei ist.

**Zweigspannung aus Knotenpotentialen**

$$U_{\mu\nu}=U_\mu-U_\nu,\qquad U_{\mu0}=U_\mu$$

Spannung des Zweigs zwischen den Knoten $\mu$ und $\nu$; zum Bezugsknoten hin ist sie das Knotenpotential selbst.

**Maschenregel mit Knotenpotentialen**

$$(U_1-U_2)+(U_2-U_3)+\dots+(U_N-U_1)=0$$

Umlauf über die Knoten $1,2,\dots,N$: Jedes Potenzial tritt einmal mit $+$ und einmal mit $-$ auf. Deshalb ist jede Maschenregel für beliebige Werte der $k-1$ Knotenpotentiale erfüllt.
::::

::::lernkarten
:::karte begriff Bezugsknoten
Was ist der Bezugsknoten eines Netzes, und wo wählt man ihn am besten?
---
Ein frei gewählter Knoten 0 mit $\varphi_0=0$, gegen den alle Knotenpotentiale zählen; im Schaltplan zeigt ihn das Massezeichen. Man legt ihn dorthin, wo die meisten Zweige zusammenkommen, dann werden die Gleichungen am kürzesten.
--- falsch
Der Knoten, an dem eine Quelle mit ihrem Minuspol hängt, weil nur dort das Potenzial null ist. Er ist durch die Schaltung festgelegt und nicht frei wählbar. Im Schaltplan zeigt ihn das Massezeichen an, das stets am Minuspol steht.
--- falsch
Ein frei gewählter Knoten 0 mit dem Potenzial $\varphi_0=0$. Man legt ihn dorthin, wo die wenigsten Zweige zusammenkommen, weil dann die wenigsten Ströme zu ihm hin gezählt werden müssen und die Matrix kleiner wird.
--- falsch
Ein frei gewählter Knoten, dessen Potenzial man gleich der größten Quellenspannung setzt. Dann sind alle Knotenpotentiale negativ, und man erkennt sofort, wohin der Strom fließt.
:::
:::karte begriff Knotenpotential
Was gibt das Knotenpotential $U_\mu$ eines Knotens an, und welche Einheit hat es?
---
Die Spannung des Knotens $\mu$ gegen den Bezugsknoten, $U_\mu=\varphi_\mu-\varphi_0$, mit dem Pfeil vom Knoten zum Bezugsknoten, in Volt. Es ist zugleich das Potenzial gegenüber dem gewählten Nullpunkt.
--- falsch
Die Summe der Spannungen aller Zweige, die am Knoten $\mu$ enden, in Volt. Nach der Maschenregel ist sie null, solange der Knoten nicht an einer Quelle hängt; sonst ist sie gleich der Quellenspannung.
--- falsch
Das Potenzial des Knotens für sich, unabhängig von jedem Nullpunkt, in Volt. Es ändert sich nicht, wenn man einen anderen Knoten als Bezugsknoten wählt.
--- falsch
Die Spannung des Bezugsknotens gegen den Knoten $\mu$, $U_\mu=\varphi_0-\varphi_\mu$, in Volt. Liegt der Knoten höher als der Bezugsknoten, ist es deshalb negativ.
:::
:::karte formel Zweigspannung aus Knotenpotentialen
Wie berechnet man die Spannung eines Zweigs zwischen den Knoten $\mu$ und $\nu$ aus den Knotenpotentialen?
---
$U_{\mu\nu}=U_\mu-U_\nu$, die Differenz der beiden Knotenpotentiale. Führt der Zweig zum Bezugsknoten, ist $U_{\mu0}=U_\mu$, weil dessen Potenzial null ist.
--- falsch
$U_{\mu\nu}=U_\mu+U_\nu$, die Summe der beiden Knotenpotentiale, weil beide gegen denselben Bezugsknoten zählen. Führt der Zweig zum Bezugsknoten, ist $U_{\mu0}=U_\mu$.
--- falsch
$U_{\mu\nu}=U_\mu-U_\nu$, die Differenz der beiden Knotenpotentiale. Führt der Zweig zum Bezugsknoten, ist $U_{\mu0}=0$, weil dort alle Spannungen enden.
--- falsch
$U_{\mu\nu}=U_\nu-U_\mu$, das Potenzial des Zielknotens minus das des Startknotens, weil die Spannung dorthin zeigt, wohin der Strom fließt. Zum Bezugsknoten ist $U_{\mu0}=-U_\mu$.
:::
:::karte zusammenhang Maschenregel von selbst
Warum ist die Maschenregel für beliebige Werte der Knotenpotentiale von selbst erfüllt?
---
Jede Zweigspannung ist eine Differenz zweier Knotenpotentiale. Längs einer Masche tritt jedes Potenzial einmal mit Plus und einmal mit Minus auf: $(U_1-U_2)+(U_2-U_3)+\dots+(U_N-U_1)=0$. Wer im Kreis läuft, kommt auf der Ausgangshöhe an.
--- falsch
Weil man die Knotenpotentiale so berechnet, dass die Maschenregel stimmt. Erst die Lösung des Gleichungssystems sorgt dafür, dass jeder Umlauf die Summe null ergibt; für beliebige andere Werte der Potenziale gilt sie nicht.
--- falsch
Weil alle Knotenpotentiale gegen denselben Bezugsknoten zählen und deshalb gleich groß sind. Gleiche Potenziale ergeben in jeder Masche lauter Zweigspannungen null, und deren Summe ist null.
--- falsch
Jede Zweigspannung ist eine Differenz zweier Knotenpotentiale. Die Maschenregel gilt aber nur für Maschen, die durch den Bezugsknoten laufen, weil nur dort ein Potenzial festgelegt ist.
:::
:::karte zusammenhang Eine Höhe frei festlegen
Warum darf man das Potenzial eines Knotens frei festlegen, und was gewinnt man dadurch?
---
Weil für Spannungen und Ströme nur Potenzialdifferenzen zählen. Legt man ein Potenzial fest, spart man eine Unbekannte, und es bleiben die $k-1$ freien Spannungen.
--- falsch
Weil der Bezugsknoten keinen Strom führt und deshalb kein Potenzial braucht. Man spart so eine Knotengleichung, die Zahl der Unbekannten bleibt aber $k$.
--- falsch
Weil das Potenzial des Bezugsknotens ohnehin durch die Quelle festgelegt ist. Man gewinnt dadurch nichts, es ist nur eine Vereinbarung für den Schaltplan.
--- falsch
Weil nur Differenzen zählen. Legt man ein Potenzial fest, spart man eine Unbekannte, und es bleiben die $z-k+1$ freien Spannungen des Netzes übrig.
:::
:::karte herleitung Vollständigkeit der Knotenpotentiale
Zeige, dass zu jeder Spannungsverteilung, die die Maschenregel erfüllt, genau ein Satz Knotenpotentiale gehört.
---
Man wählt einen Baum, weil es darin zwischen dem Bezugsknoten und jedem Knoten genau einen Weg gibt.
---
Die Summe der Zweigspannungen längs dieses Wegs legt das Knotenpotential fest, und zwar eindeutig, weil es im Baum nur diesen einen Weg gibt.
---
Für die Baumzweige stimmen damit alle Differenzen, weil jedes Potenzial über die Baumzweige aufsummiert wurde.
---
Für jeden Verbindungszweig stimmt die Differenz ebenfalls, weil er mit Baumzweigen eine Masche schließt, deren Maschenregel nach Voraussetzung gilt.
:::
:::karte zusammenhang Bezugsknoten wechseln
Was ändert sich an Knotenpotentialen, Zweigspannungen und Strömen, wenn man einen anderen Knoten als Bezugsknoten wählt?
---
Alle Knotenpotentiale verschieben sich um denselben Betrag, aber keine einzige Zweigspannung, weil sie Differenzen sind. Da die Ströme nur von Differenzen abhängen, ändert sich auch kein Strom.
--- falsch
Die Knotenpotentiale bleiben gleich, weil sie fest zu den Knoten gehören. Nur die Zweigspannungen zum neuen Bezugsknoten ändern sich, und mit ihnen die Ströme dorthin.
--- falsch
Alle Knotenpotentiale und alle Zweigspannungen verschieben sich um denselben Betrag. Die Ströme bleiben trotzdem gleich, weil die Quellen dieselben bleiben und ihre Ströme unverändert einspeisen.
--- falsch
Alle Knotenpotentiale ändern sich, und mit ihnen die Ströme, weil jeder Strom vom Potenzial seines Knotens abhängt. Nur die Quellenspannungen bleiben gleich.
:::
:::karte zusammenhang Gültigkeit der Knotenpotentiale
Unter welcher Bedingung lassen sich die Spannungen eines Netzes durch Knotenpotentiale beschreiben, und wo ist diese Bedingung in Schaltungen verletzt?
---
Das Feld muss wirbelfrei sein. Ein veränderliches Magnetfeld durch eine Masche zerstört die Potenziale; in Schaltungen sitzt es in Spulen.
--- falsch
Das Netz muss sich ohne Kreuzungen zeichnen lassen. Bei Kreuzungen ist nicht klar, welche Höhe ein Knoten hat; in Schaltungen betrifft das vor allem große Platinen.
--- falsch
Alle Bauteile müssen linear sein. Nichtlineare Bauteile verschieben die Potenziale je nach Strom; in Schaltungen betrifft das vor allem die Halbleiter.
--- falsch
Das Netz darf keine Stromquellen enthalten. Eine Stromquelle legt keine Spannung fest, deshalb fehlt dort ein Potenzial; in Schaltungen betrifft das jede Stromversorgung.
:::
:::karte zusammenhang Potenzial oder Spannung
Ist das Knotenpotential ein Potenzial oder eine Spannung, und warum trägt es das Zeichen $U$?
---
Beides. Ein Potenzial für sich hat nur gegenüber einem Nullpunkt einen Wert. Das Knotenpotential ist die Spannung gegen den gewählten Nullpunkt, den Bezugsknoten, deshalb trägt es das Zeichen $U$.
--- falsch
Eine Spannung, weil es zwischen zwei Zweigen am Knoten gemessen wird. Ein Potenzial wäre nur der Wert an einer einzelnen Stelle, ganz ohne Bezugspunkt, deshalb trägt es das Zeichen $U$ und nicht $\varphi$.
--- falsch
Ein Potenzial, weil es zu einem einzelnen Knoten gehört und keinen Nullpunkt braucht. Das Zeichen $U$ ist nur eine Abkürzung und hat mit einer Spannung nichts zu tun.
--- falsch
Beides, je nach Netz: In Netzen mit Spannungsquelle ist es eine Spannung, ohne Spannungsquelle ein Potenzial, weil dann kein Nullpunkt festgelegt ist.
:::
:::karte zusammenhang Netz mit zwei Knoten
Welche Bedeutung hat das einzige Knotenpotential eines Netzes mit nur zwei Knoten?
---
Es ist die gemeinsame Spannung einer Parallelschaltung. Alle Zweige liegen zwischen denselben zwei Knoten, also tragen sie alle diese eine Spannung.
--- falsch
Es ist null, weil einer der beiden Knoten der Bezugsknoten ist und der andere ihm gegenüber kein eigenes Potenzial hat.
--- falsch
Es ist der gemeinsame Strom einer Reihenschaltung, weil alle Zweige zwischen zwei Knoten hintereinander liegen und denselben Strom führen.
--- falsch
Es ist die Summe der Spannungen aller Zweige, weil jeder Zweig zwischen den beiden Knoten einen eigenen Anteil zur Knotenspannung beiträgt.
:::
::::

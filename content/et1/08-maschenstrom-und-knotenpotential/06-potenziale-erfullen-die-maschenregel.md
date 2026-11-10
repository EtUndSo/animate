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

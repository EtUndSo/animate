---
title: Stufe 1: Das Messgerät ist ein Bauteil
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Strom und Spannung messen
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-und-spannung-messen
knoten: Kapitel 4: Strom und Spannung messen
order: 1140200
summary: Bevor sich ein Fehler berechnen lässt, muss klar sein, was ein Messgerät elektrisch ist: ein Bauteil mit zwei Anschlüssen und einem Widerstand dazwischen.
tags: Bereichsendwert
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Bevor sich ein Fehler berechnen lässt, muss klar sein, was ein Messgerät elektrisch ist: ein Bauteil mit zwei Anschlüssen und einem Widerstand dazwischen.
:::

**Die Idee.** Im Zeigerinstrument sitzt eine drehbare Spule aus dünnem Draht zwischen den Polen eines Dauermagneten (Abb. [1](#abb-1)). Fließt Strom, übt das Magnetfeld auf die bewegten Elektronen im Draht eine Kraft aus, und die Spule dreht sich gegen eine Spiralfeder. Die Drehkraft wächst mit dem Strom, die Gegenkraft der Feder mit dem Winkel. Deshalb ist der Ausschlag dem Strom proportional. Zwei Dinge lassen sich nicht vermeiden: Ohne Strom gibt es keinen Ausschlag, und mit Strom fällt am Draht Spannung ab. Ein Digitalmultimeter (Gerät mit Zahlenanzeige) wandelt die Spannung an einem internen Widerstand in eine Zahl um. Auch dort fließt Strom durch einen Widerstand.

:::abbildung et1/k4messwerk 1
Links das Messwerk: Die Spule dreht sich im Magnetfeld gegen eine Feder (nicht gezeichnet). Rechts die Ersatzbilder: ideales Instrument plus Innenwiderstand, in Reihe oder parallel.
:::

:::definition Definition 1.1 (Messbereich und Innenwiderstand)
<span class="anker" id="satz-1-1"></span>

Der Messbereich reicht bis zum __Bereichsendwert__, dem größten anzeigbaren Wert (beim Zeiger der Vollausschlag). Der Innenwiderstand $R_\mathrm i$ ist der Widerstand zwischen den Anschlüssen.

<ul>

<li>

Ein Amperemeter wird in Reihe geschaltet. Ideal ist $R_\mathrm i=0$, real etwa $R_\mathrm i\approx1\,\Omega$.

</li>

<li>

Ein Voltmeter wird parallel geschaltet. Ideal ist $R_\mathrm i\to\infty$, real etwa $R_\mathrm i\approx10\,\mathrm{M\Omega}$.

</li>

</ul>
:::

⁠**So liest man das:** Strom ist Ladung, die durch einen Querschnitt läuft. Deshalb trennt man den Stromkreis auf und schickt den ganzen Strom durch das Amperemeter. An ihm soll keine Spannung abfallen, also soll $R_\mathrm i$ klein sein. Spannung ist die Differenz zwischen zwei Punkten. Deshalb legt man das Voltmeter an beide Punkte, ohne den Kreis zu öffnen. Durch es soll kein Strom fließen, also soll $R_\mathrm i$ groß sein. Die Zahlenwerte sind typisch für Digitalmultimeter. **Gültigkeit:** $R_\mathrm i$ gilt für einen Messbereich und ändert sich beim Umschalten (Stufe [2](den-messbereich-erweitern.html#stufe-2)).

::::beispiel
Das Messwerk des Rechenmodells ist schon beides. Bei Vollausschlag fließen 50 µ A durch 2 k$\Omega$, also liegen $U_\mathrm M=R_\mathrm MI_\mathrm M=100$ mV an. Die Skala ließe sich mit 50 µ A oder mit 100 mV beschriften: zwei Namen für denselben Ausschlag.
::::

⁠**Grenzfall:** Für $R_\mathrm i=0$ wirkt das Amperemeter wie ein Stück Draht, für $R_\mathrm i\to\infty$ das Voltmeter wie eine offene Stelle. Ideale Instrumente sind für die Schaltung nicht vorhanden.

:::frage Wenn durch ein ideales Voltmeter kein Strom fließt, wie kann es dann etwas anzeigen?
Ein Zeiger könnte es nicht, denn ohne Strom gibt es keinen Ausschlag. Der ideale Fall ist eine Grenze, kein Gerät. Ein großer Innenwiderstand macht den Strom klein, nicht null. Digitale Geräte kommen mit sehr wenig Strom aus, weil die Energie für die Anzeige aus ihrer eigenen Batterie stammt, nicht aus der gemessenen Schaltung.
:::

:::aufgabe Aufgabe 1 ★ Falsch angeschlossen
<span class="anker" id="aufg-1"></span>

Sage zuerst vorher, welches Gerät in Gefahr ist. (a) Das Amperemeter des Rechenmodells liegt versehentlich direkt an der 9-V-Quelle. Welcher Strom fließt? (b) Das Voltmeter liegt versehentlich in Reihe mit $R$ an der Quelle. Was zeigt es an, welcher Strom fließt?

:::loesung
(a) In Gefahr ist das Amperemeter, denn sein kleiner Widerstand begrenzt den Strom kaum: $I=9\,\mathrm{V}/10\,\Omega=0{,}9$ A, das Neunzigfache des Bereichs. Durch das Messwerk fließen 4,5 mA statt 50 µ A, im Shunt werden 8,06 W frei.

(b) $I=9\,\mathrm{V}/201{,}8\,\mathrm{k\Omega}=44{,}6$ µ A. Das Voltmeter zeigt $44{,}6\,\mu\text{A}\cdot200\,\mathrm{k\Omega}=8{,}92$ V, an $R$ bleiben 80 mV. Nichts geht kaputt, aber die Schaltung arbeitet nicht mehr.
:::
:::

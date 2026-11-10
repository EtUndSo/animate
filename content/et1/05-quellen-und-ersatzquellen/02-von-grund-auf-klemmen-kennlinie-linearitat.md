---
title: Von Grund auf: Klemmen, Kennlinie, Linearität
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Quellen und Ersatzquellen
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen
knoten: Kapitel 5: Quellen und Ersatzquellen
order: 1150200
summary: Warum zwei Zahlen ein ganzes Netzwerk ersetzen
tags: Klemme, Eintor, Kennlinie, Leerlauf, linear
lang: de
---

Eine __Klemme__ ist ein Anschlusspunkt nach außen. Ein __Eintor__ ist ein Netzwerk mit genau zwei Klemmen, die ein Paar bilden: Der Strom, der an A hinausfließt, kommt an B wieder herein, denn Ladung geht nicht verloren (Knotenregel, [Kapitel 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)). Ein Eintor hat deshalb nur einen Strom und eine Spannung. Es ist ein Zweipol aus [Kapitel 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html), auch wenn es innen viele Bauteile enthält. Die __Kennlinie__ ist der Zusammenhang dieser beiden Größen. Sie steht in diesem Kapitel immer im selben Diagramm: Klemmenstrom waagerecht, Klemmenspannung senkrecht.

Die Zählpfeile gelten im ganzen Kapitel: $U_\mathrm{AB}=\varphi_\mathrm{A}-\varphi_\mathrm{B}$ zählt von A nach B, $I_\mathrm{A}$ zählt aus der Klemme A heraus. Für die angeschlossene Last zeigen beide Pfeile in dieselbe Richtung (Verbraucher-Zählpfeile, [Kapitel 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)), für das Eintor selbst entgegengesetzt (Erzeuger-Zählpfeile). Sind beide positiv, gibt das Eintor Leistung ab. __Leerlauf__ heißt: Die Klemmen sind offen, $I_\mathrm{A}=0$. Kurzschluss heißt: Die Klemmen sind durch einen Draht verbunden, $U_\mathrm{AB}=0$.

Ein Bauteil ist __linear__, wenn sein Strom proportional zu seiner Spannung ist. Ein Widerstand ist das, solange $R$ nicht vom Strom abhängt: Seine Kennlinie ist eine Gerade durch den Ursprung. Eine Glühlampe oder eine Diode ([Kapitel 9](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden/halbleiter-und-dioden.html)) ist es nicht. Das Zeichen $\parallel$ steht für den Widerstand einer Parallelschaltung, $R_1\parallel R_2=\frac{R_1R_2}{R_1+R_2}$ ([Kapitel 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)). Es bindet stärker als das Plus, wie die Punktrechnung.

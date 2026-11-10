---
title: Überblick: Statistik und Information
kurz: Überblick
pfad: Informatik / Machine Learning / Mathematische Grundlagen / Statistik und Information
adresse: informatik/machine-learning/mathematische-grundlagen/statistik-und-information
knoten: Kapitel 5: Statistik und Information
nachschlagen: ja
order: 15250100
summary: Aus Daten schätzen und Überraschung messen
tags: 
lang: de
---

## Worum es geht

In [Kapitel 4](/wissen/informatik/machine-learning/mathematische-grundlagen/wahrscheinlichkeit/wahrscheinlichkeit.html) war die Verteilung immer bekannt, und gefragt war, wie wahrscheinlich bestimmte Daten sind. Zeigt eine Münze mit der Wahrscheinlichkeit $0{,}7$ Kopf, so fällt bei zehn Würfen mit der Wahrscheinlichkeit $0{,}267$ genau siebenmal Kopf. In der Praxis ist die Lage fast immer umgekehrt. Man hat die Daten und kennt die Verteilung nicht. Eine Münze mit verbogenem Rand zeigt in zehn Würfen siebenmal Kopf: Wie wahrscheinlich ist Kopf bei dieser Münze? Vier Wägungen desselben Pakets schwanken um $5\,\mathrm{kg}$: Wie schwer ist es wirklich, und wie stark rauscht die Waage?

Dieses Kapitel geht den Weg von den Daten zurück zur Verteilung. Es fragt: Wie macht man aus Daten eine Zahl für eine unbekannte Größe, und woran erkennt man, ob diese Zahl gut ist? Welche Werte der unbekannten Größe passen am besten zu den Daten? Wie verbindet man die Daten mit dem, was man vorher schon wusste? Und wie misst man, wie überraschend ein Ergebnis ist und wie schlecht eine angenommene Verteilung zur Wirklichkeit passt?

Unterwegs beantwortet das Kapitel drei Fragen, die in [Kapitel 1](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/vektoren-und-matrizen.html) und [Kapitel 4](/wissen/informatik/machine-learning/mathematische-grundlagen/wahrscheinlichkeit/wahrscheinlichkeit.html) offengeblieben sind: warum viele Texte und Taschenrechner eine Quadratsumme durch $N-1$ statt durch $N$ teilen, wie man den Satz von Bayes auf eine unbekannte Größe anwendet, die eine ganze Spanne von Werten haben kann, und warum die Normalverteilung neben dem zentralen Grenzwertsatz noch einen zweiten Grund hat, so oft aufzutreten.

Der Nutzen: Mit den Antworten schätzt man unbekannte Größen aus Messwerten und gibt an, wie genau die Schätzung ist. Man baut Vorwissen nachvollziehbar in eine Schätzung ein. Man misst Information in Bit, der Einheit, in der auch Speicher und Dateien gemessen werden, und sieht, dass zwei auf den ersten Blick verschiedene Fragen dieselbe Antwort haben: die nach den Parametern, die die Daten am besten erklären, und die nach der Verteilung, die am wenigsten von den Daten abweicht.

**So arbeitest du mit diesem Kapitel.** Die Abschnitte bauen aufeinander auf, jeder neue Begriff hat einen eigenen Unterabschnitt mit Beispiel. Kästen zum Aufklappen enthalten Hintergrund (warum ein Verfahren funktioniert und woher es kommt), Herleitungen und Beweise; zum Weiterlesen braucht man sie nicht. Versuche die Aufgaben (★ bis ★★★) zuerst selbst und führe Programme wirklich aus; die Lösung klappst du direkt unter der Aufgabe auf.

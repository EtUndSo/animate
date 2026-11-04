---
title: Überblick: Projektion, Eigenwerte und Zerlegungen
kurz: Überblick
pfad: Informatik / Machine Learning / Projektion, Eigenwerte und Zerlegungen
order: 6220100
summary: Nächste Punkte, natürliche Richtungen und die Bausteine einer Matrix
tags: 
lang: de
---

## Worum es geht

In [Teil 1](/wissen/informatik/machine-learning/vektoren-und-matrizen/vektoren-und-matrizen.html) ist eine Frage offengeblieben. Vier Wohnungen sind durch ihre Fläche und ihre Zimmerzahl beschrieben, und ihre Preise sind bekannt. Gesucht sind zwei Gewichte, mit denen die gewichtete Summe jeden Preis trifft. Solche Gewichte gibt es nicht: Vier Gleichungen mit zwei Unbekannten widersprechen einander. Mit Messdaten geht es fast immer so. Man hat mehr Messungen als Unbekannte, jede Messung ist ein wenig ungenau, und das Gleichungssystem hat keine Lösung. Trotzdem braucht man Gewichte, und zwar die, die so wenig wie möglich danebenliegen.

Dieses Kapitel geht dieser Frage nach und zwei weiteren, die sich als eng verwandt herausstellen. Gibt es Richtungen, in die eine Matrix einen Pfeil nur länger oder kürzer macht, ohne ihn zu drehen, und was verraten diese Richtungen über die Matrix? Und lässt sich jede Matrix in wenige einfache Bausteine zerlegen, nach ihrer Wichtigkeit geordnet, sodass man die unwichtigen weglassen kann? Dazu kommt eine praktische Frage: Wie stark verändert sich das Ergebnis einer Rechnung, wenn die Daten ein wenig falsch sind?

Der Nutzen: Mit den Antworten passt man eine Gerade oder eine andere einfache Vorschrift so an Messwerte an, dass der Fehler so klein wie möglich wird. Man erkennt, ob eine Funktion mehrerer Variablen eine Mulde, einen Kamm oder einen Sattel hat. Man nähert ein Bild oder eine große Tabelle mit wenigen Zahlen an und weiß, wie viel dabei verloren geht. Und man kann einschätzen, ob man einem Rechenergebnis trauen darf. Die Werkzeuge dieses Kapitels tauchen in fast allen weiteren Teilen der Reihe auf.

**So arbeitest du mit diesem Kapitel.** Die Abschnitte bauen aufeinander auf, jeder neue Begriff hat einen eigenen Unterabschnitt mit Beispiel. Kästen zum Aufklappen enthalten Hintergrund (warum ein Verfahren funktioniert und woher es kommt), Herleitungen und Beweise; zum Weiterlesen braucht man sie nicht. Versuche die Aufgaben (★ bis ★★★) zuerst selbst und führe Programme wirklich aus; die Lösung klappst du direkt unter der Aufgabe auf.

---
title: Überblick: Wahrscheinlichkeit
kurz: Überblick
pfad: Informatik / Machine Learning / Wahrscheinlichkeit
order: 6240100
summary: Unsicherheit rechnen: Ereignisse, Verteilungen, Kovarianz und die Normalverteilung
tags: 
lang: de
---

## Worum es geht

Daten sind nie ganz sicher. Misst man dieselbe Spannung zweimal, zeigt das Messgerät zwei verschiedene Werte, weil sich dem Signal ein Rauschen überlagert. Ein Datensatz mit hundert Wohnungen ist nur eine Auswahl aus allen Wohnungen einer Stadt; eine andere Auswahl hätte andere Zahlen geliefert. Und oft fehlt Information: Zwei Wohnungen mit gleicher Fläche, gleicher Zimmerzahl und gleicher Lage können trotzdem verschiedene Mieten haben, weil vieles, was den Preis bestimmt, gar nicht im Datensatz steht.

Dieses Kapitel fragt: Wie rechnet man genau mit dem, was man nicht sicher weiß? Wie stark sollte eine Beobachtung die eigene Einschätzung ändern, etwa ein Alarm eines Prüfgeräts, das sich manchmal irrt? Was ist der typische Wert einer schwankenden Größe, und wie weit schwankt sie um ihn? Wie beschreibt man, dass zwei Größen gemeinsam schwanken? Und warum sehen die Schwankungen so vieler Messgrößen, vom Rauschen eines Widerstands bis zum Mittelwert vieler Messungen, immer wieder gleich aus?

Der Nutzen: Mit den Antworten kann man aus unsicheren Angaben sichere Schlüsse über Häufigkeiten ziehen, kann Fehlalarme und echte Befunde richtig gewichten und kann sagen, wie genau ein Mittelwert aus vielen Messungen ist. Fast jedes Verfahren, das aus Daten lernt, beschreibt seine Daten und seine Vorhersagen in dieser Sprache.

**So arbeitest du mit diesem Kapitel.** Die Abschnitte bauen aufeinander auf, jeder neue Begriff hat einen eigenen Unterabschnitt mit Beispiel. Kästen zum Aufklappen enthalten Hintergrund (warum ein Verfahren funktioniert und woher es kommt), Herleitungen und Beweise; zum Weiterlesen braucht man sie nicht. Versuche die Aufgaben (★ bis ★★★) zuerst selbst und führe Programme wirklich aus; die Lösung klappst du direkt unter der Aufgabe auf.

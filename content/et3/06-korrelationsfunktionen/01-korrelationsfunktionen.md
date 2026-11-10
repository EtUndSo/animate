---
title: Überblick: Korrelationsfunktionen
kurz: Überblick
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Korrelationsfunktionen
adresse: elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen
knoten: Kapitel 6: Korrelationsfunktionen
order: 3260100
summary: Wie ähnlich sind zwei Signale, und wie verteilt sich die Energie über die Frequenz?
tags: 
lang: de
---

## Worum es geht

Ein Radar sendet einen Impuls und sucht im Empfangssignal sein Echo. Ein Mobiltelefon sucht im Rauschen eine bekannte Synchronisationsfolge. Beide stellen dieselbe Frage: *Wie ähnlich ist ein Signal einem anderen, und bei welcher Verschiebung am ähnlichsten?* Die Antwort liefert die Korrelationsfunktion. Ihre Fourier-Transformierte sagt außerdem, wie sich die Energie eines Signals auf die Frequenzen verteilt.



**So arbeitest du mit diesem Kapitel.** Die Abschnitte bauen aufeinander auf, jeder neue Begriff hat einen eigenen Unterabschnitt mit Beispiel. Kästen zum Aufklappen enthalten Hintergrund (warum etwas so ist und woher es kommt), Herleitungen und Hinweise zur Simulation; zum Weiterlesen braucht man sie nicht. Versuche die Aufgaben (★ bis ★★★) zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf.

:::merke Das Rechenmodell für dieses Kapitel
Rechteckimpuls $\operatorname{rect}(t)$, Dreieck $\Lambda(t)$, Exponentialimpuls $\varepsilon(t)\mathrm{e}^{-t}$ (die Impulsantwort des RC-Glieds mit $RC=1$ s) und die Folge $(1,2,1)$. Die Zahlen rechnet `rechnung_kap6.py` nach.
:::

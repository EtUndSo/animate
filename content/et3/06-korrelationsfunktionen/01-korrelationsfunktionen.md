---
title: Überblick: Korrelationsfunktionen
kurz: Überblick
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / Korrelationsfunktionen
order: 3260100
summary: Wie ähnlich sind zwei Signale, und wie verteilt sich die Energie über die Frequenz?
tags: 
lang: de
---

## Worum es geht

Ein Radar sendet einen Impuls und sucht im Empfangssignal sein Echo. Ein Mobiltelefon sucht im Rauschen eine bekannte Synchronisationsfolge. Beide stellen dieselbe Frage: *Wie ähnlich ist ein Signal einem anderen, und bei welcher Verschiebung am ähnlichsten?* Die Antwort liefert die Korrelationsfunktion. Ihre Fourier-Transformierte sagt außerdem, wie sich die Energie eines Signals auf die Frequenzen verteilt.



**So arbeitest du mit diesem Kapitel.** Jede Stufe ist ein eigener kurzer Artikel mit der Idee, typischen Fragen zum Aufklappen und Aufgaben (★ bis ★★★). Versuche die Aufgaben zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf. Schließe eine Stufe ab, bevor du zur nächsten gehst.

:::merke Das Rechenmodell für dieses Kapitel
Rechteckimpuls $\operatorname{rect}(t)$, Dreieck $\Lambda(t)$, Exponentialimpuls $\varepsilon(t)\mathrm{e}^{-t}$ (die Impulsantwort des RC-Glieds mit $RC=1$ s) und die Folge $(1,2,1)$. Die Zahlen rechnet `rechnung_kap6.py` nach.
:::

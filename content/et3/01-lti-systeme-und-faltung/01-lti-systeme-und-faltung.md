---
title: Überblick: Signale, LTI-Systeme und die Faltung
kurz: Überblick
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / LTI-Systeme und Faltung
adresse: elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung
knoten: Kapitel 1: LTI-Systeme und Faltung
order: 3210100
summary: Warum die Antwort auf einen einzigen Stoß das ganze System beschreibt
tags: 
lang: de
---

## Worum es geht

Ein System nimmt ein Signal auf und gibt ein anderes ab: Ein RC-Glied glättet eine Spannung, ein Lautsprechergehäuse färbt einen Klang, ein Messverstärker verzögert und verstärkt. Die Frage dieses Kapitels lautet: *Was muss man über ein System wissen, um für jedes beliebige Eingangssignal den Ausgang ausrechnen zu können?*

Für die große Klasse der linearen, zeitinvarianten Systeme (LTI-Systeme) ist die Antwort überraschend knapp: die Antwort auf einen einzigen, unendlich kurzen Stoß. Das Werkzeug, das aus dieser einen Antwort jede andere macht, ist die Faltung.



**So arbeitest du mit diesem Kapitel.** Die Abschnitte bauen aufeinander auf, jeder neue Begriff hat einen eigenen Unterabschnitt mit Beispiel. Kästen zum Aufklappen enthalten Hintergrund (warum etwas so ist und woher es kommt), Herleitungen und Hinweise zur Simulation; zum Weiterlesen braucht man sie nicht. Versuche die Aufgaben (★ bis ★★★) zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf.

:::merke Das Rechenmodell für dieses Kapitel
<ul>

<li>

⁠**RC-Tiefpass** mit $T=RC=1$ s (zum Beispiel $R=1\,\mathrm{M\Omega}$, $C=1\,\mu\text{F}$). Zeiten in s, Spannungen in V, also dimensionslos gerechnet.

</li>

<li>

⁠**Rechteckimpuls** der Höhe $a=1$ V und Dauer $T_0=1$ s, beginnend bei $t=0$.

</li>

</ul>

Die Zahlen und Kurven rechnet `rechnung_kap1.py` nach.
:::

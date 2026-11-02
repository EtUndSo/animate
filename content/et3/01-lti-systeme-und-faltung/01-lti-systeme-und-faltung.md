---
title: Überblick: Signale, LTI-Systeme und die Faltung
kurz: Überblick
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / LTI-Systeme und Faltung
order: 3210100
summary: Warum die Antwort auf einen einzigen Stoß das ganze System beschreibt
tags: 
lang: de
---

## Worum es geht

Ein System nimmt ein Signal auf und gibt ein anderes ab: Ein RC-Glied glättet eine Spannung, ein Lautsprechergehäuse färbt einen Klang, ein Messverstärker verzögert und verstärkt. Die Frage dieses Kapitels lautet: *Was muss man über ein System wissen, um für jedes beliebige Eingangssignal den Ausgang ausrechnen zu können?*

Für die große Klasse der linearen, zeitinvarianten Systeme (LTI-Systeme) ist die Antwort überraschend knapp: die Antwort auf einen einzigen, unendlich kurzen Stoß. Das Werkzeug, das aus dieser einen Antwort jede andere macht, ist die Faltung.



**So arbeitest du mit diesem Kapitel.** Jede Stufe ist ein eigener kurzer Artikel mit der Idee, typischen Fragen zum Aufklappen und Aufgaben (★ bis ★★★). Versuche die Aufgaben zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf. Schließe eine Stufe ab, bevor du zur nächsten gehst.

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

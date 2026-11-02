---
title: Überblick: Abtastung und zeitdiskrete Systeme
kurz: Überblick
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / Abtastung und zeitdiskrete Systeme
order: 3240100
summary: Vom kontinuierlichen Signal zur Zahlenfolge: Abtasttheorem, diskrete Faltung, DFT, FFT und z-Transformation
tags: Abtastwerten
lang: de
---

## Worum es geht

Ein Rechner kann keine Funktion $s(t)$ speichern, nur eine Folge von Zahlen. Man misst das Signal deshalb im festen Takt $T$ und arbeitet mit den __Abtastwerten__ $s(nT)$. Zwei Fragen bestimmen dieses Kapitel: *Geht dabei Information verloren?* Und: *Wie rechnet man mit Zahlenfolgen so, wie die [Teile 1](/wissen/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html) bis 3 mit Funktionen gerechnet haben?*



**So arbeitest du mit diesem Kapitel.** Jede Stufe ist ein eigener kurzer Artikel mit der Idee, typischen Fragen zum Aufklappen und Aufgaben (★ bis ★★★). Versuche die Aufgaben zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf. Schließe eine Stufe ab, bevor du zur nächsten gehst.

:::merke Das Rechenmodell für dieses Kapitel
<ul>

<li>

⁠**Abtastrate** $f_\mathrm A=1/T=1$ kHz ($T=1$ ms). Testsignale: Kosinusschwingungen mit 300 Hz und 700 Hz.

</li>

<li>

Bei Folgen wird die Frequenz auf die Abtastrate bezogen: $f=1$ entspricht $f_\mathrm A$. Bei $f_\mathrm A=1$ kHz bedeutet $f=0{,}3$ also 300 Hz.

</li>

<li>

⁠**Rekursives System** $g(n)=s(n)+0{,}6\,g(n-1)$.

</li>

<li>

⁠**DFT-Beispiel** $s_d=(1,\,2,\,0,\,-1)$.

</li>

</ul>

Die Zahlen und Kurven rechnet `rechnung_kap4.py` nach.
:::

---
title: Überblick: Tiefpass- und Bandpasssysteme
kurz: Überblick
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / Tiefpass- und Bandpasssysteme
order: 3250100
summary: Verzerrungsfreie Übertragung, idealer Tiefpass, komplexe Hüllkurve und Gruppenlaufzeit
tags: 
lang: de
---

## Worum es geht

Fast jede Übertragung soll ein Signal möglichst unverändert ankommen lassen, aber nur in einem bestimmten Frequenzbereich: Ein Tiefpass lässt die tiefen Frequenzen durch, ein Bandpass ein Band um eine Trägerfrequenz. Dieses Kapitel fragt: *Was heißt „unverändert“ genau, was kostet ein scharf begrenztes Band, und wie rechnet man mit Signalen, die auf einem hochfrequenten Träger sitzen?*



**So arbeitest du mit diesem Kapitel.** Die Abschnitte bauen aufeinander auf, jeder neue Begriff hat einen eigenen Unterabschnitt mit Beispiel. Kästen zum Aufklappen enthalten Hintergrund (warum etwas so ist und woher es kommt), Herleitungen und Hinweise zur Simulation; zum Weiterlesen braucht man sie nicht. Versuche die Aufgaben (★ bis ★★★) zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf.

:::merke Das Rechenmodell für dieses Kapitel
<ul>

<li>

⁠**RC-Tiefpass** mit $RC=1$ s wie in den [Teilen 1](/wissen/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html) bis 3.

</li>

<li>

⁠**Idealer Tiefpass** mit $f_\mathrm g=1$ Hz (zum Vergleich auch 2 Hz).

</li>

<li>

⁠**Idealer Bandpass** mit der Mittenfrequenz $f_0=10$ Hz und der Bandbreite $\Delta f=2$ Hz.

</li>

<li>

⁠**Zeitdiskreter Tiefpass** mit $f_\mathrm g=0{,}2$ (bezogen auf die Abtastrate) und 21 Koeffizienten.

</li>

</ul>

Die Zahlen und Kurven rechnet `rechnung_kap5.py` nach. $\operatorname{si}(x)=\sin(x)/x$ wie in [Teil 3](/wissen/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html).
:::

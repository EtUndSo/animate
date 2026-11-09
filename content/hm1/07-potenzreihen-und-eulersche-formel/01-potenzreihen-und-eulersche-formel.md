---
title: Überblick: Potenzreihen und Eulersche Formel
kurz: Überblick
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Potenzreihen und Eulersche Formel
order: 1270100
summary: Wie eine einzige Reihe Exponentialfunktion, Sinus und Cosinus enthält und warum Multiplizieren komplexer Zahlen Drehen und Strecken ist
tags: 
lang: de
---

## Worum es geht

Auf dem Taschenrechner sind $\mathrm{e}^x$, $\sin x$ und $\cos x$ drei getrennte Tasten, und [Teil 2](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/komplexe-zahlen/komplexe-zahlen.html) hat die Polarform offen gelassen. Die Frage lautet: *Wie hängen die drei Funktionen zusammen, und warum ist Multiplizieren in $\mathbb{C}$ ein Drehen und Strecken?*



**So arbeitest du mit diesem Kapitel.** Die Abschnitte bauen aufeinander auf, jeder neue Begriff hat einen eigenen Unterabschnitt mit Beispiel. Kästen zum Aufklappen enthalten Hintergrund (warum etwas so ist und woher es kommt), Herleitungen und Hinweise zur Simulation; zum Weiterlesen braucht man sie nicht. Versuche die Aufgaben (★ bis ★★★) zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf.

:::merke Das Rechenmodell für dieses Kapitel
<ul>

<li>

⁠**Zwei Potenzreihen:** $f(x)=\sum_{n=1}^\infty\frac{x^n}{n\,2^n}$ und $g(x)=\sum_{n=0}^\infty\frac{x^{2n}}{4^n}$ (nur gerade Potenzen), beide mit Radius 2.

</li>

<li>

⁠**Eine Stelle:** $x=1$ mit $\sin1\approx0{,}8415$ und $\cos1\approx0{,}5403$, also $\mathrm{e}^{\mathrm{i}}\approx0{,}5403+0{,}8415\,\mathrm{i}$.

</li>

<li>

⁠**Zwei komplexe Zahlen aus [Teil 2](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/komplexe-zahlen/komplexe-zahlen.html):** $z_1=3+\mathrm{i}$ und $z_2=1+2\mathrm{i}$ mit $z_1z_2=1+7\mathrm{i}$: Beträge $\sqrt{10}\cdot\sqrt5=\sqrt{50}$, Winkel $18{,}43^\circ+63{,}43^\circ=81{,}87^\circ$.

</li>

<li>

⁠**Eine Gleichung:** $z^3=8\mathrm{i}$ mit den Lösungen $\sqrt3+\mathrm{i}$, $-\sqrt3+\mathrm{i}$ und $-2\mathrm{i}$.

</li>

</ul>

Alle Zahlen rechnet `rechnung_kap7.py` nach.
:::

---
title: Überblick: Konvergenz von Funktionenfolgen
kurz: Überblick
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Konvergenz von Funktionenfolgen
order: 3160100
summary: Wann man mit dem Grenzwert rechnen darf wie mit den Näherungen
tags: Funktionenfolge, punktweise Konvergenz, gleichmäßige Konvergenz, Funktionenreihe, Konvergenzradius, Supremumsnorm, Vollständigkeit, Konvergenz im quadratischen Mittel
lang: de
---

## Worum es geht

Schwierige Funktionen kennt man oft nur über Näherungen. Die Funktion $\mathrm{e}^x$ lässt sich durch Summen immer weiterer Potenzen annähern, eine Simulation nähert einen Spannungsverlauf Schritt für Schritt an. So entsteht eine Folge von Funktionen $f_1,f_2,f_3,\dots$, die sich einer Zielfunktion nähert. Die Frage dieses Kapitels lautet: *Wann darf man mit der Zielfunktion so rechnen wie mit den Näherungen?* Bleibt sie stetig, wenn alle Näherungen stetig sind? Darf man erst integrieren und dann zum Grenzwert gehen? Darf man eine unendliche Summe Glied für Glied ableiten? Der Nutzen: Man erkennt, wann eine Näherung überall gut ist und wann sie nur an jeder Stelle einzeln gut aussieht.

Der Weg führt über acht Begriffe. Eine __Funktionenfolge__ ist eine Folge, deren Glieder Funktionen sind. Die __punktweise Konvergenz__ prüft jede Stelle einzeln, die __gleichmäßige Konvergenz__ prüft den größten Abstand über alle Stellen. Eine __Funktionenreihe__ ist eine unendliche Summe von Funktionen. Der __Konvergenzradius__ sagt, wie weit um ihren Mittelpunkt eine Potenzreihe konvergiert. Die __Supremumsnorm__ misst die Größe einer Funktion durch ihren größten Betrag. __Vollständigkeit__ heißt, dass in einem Raum jede Folge, deren Glieder einander beliebig nahe kommen, einen Grenzwert hat. Die __Konvergenz im quadratischen Mittel__ misst den Abstand durch ein Integral über die quadrierte Abweichung.

**So arbeitest du mit diesem Kapitel.** Die Abschnitte bauen aufeinander auf, jeder neue Begriff hat einen eigenen Unterabschnitt mit Beispiel. Kästen zum Aufklappen enthalten Hintergrund (warum etwas so ist und woher es kommt), Herleitungen und Hinweise zur Simulation; zum Weiterlesen braucht man sie nicht. Versuche die Aufgaben (★ bis ★★★) zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf.

:::merke Die Rechenmodelle für dieses Kapitel
<ul>

<li>

⁠**Entladekurven** $u_n(x)=\mathrm{e}^{-nx}$ auf $[0,1]$: Spannung an einem Kondensator, der sich umso schneller entlädt, je größer $n$ ist. Bei $n=2$ und $x=\tfrac12$ ist $u_n(x)=\mathrm{e}^{-1}\approx0{,}368$.

</li>

<li>

⁠**Beulen** $b_n(x)=n^2x\,\mathrm{e}^{-nx}$ auf $[0,1]$: Die Spitze liegt bei $x=1/n$ und hat die Höhe $n/\mathrm{e}$. Sie wandert nach links und wächst dabei.

</li>

<li>

⁠**Rippel** $w_n(x)=\frac1n\sin(nx)$ auf $[0,\pi]$: eine Welle, die mit wachsendem $n$ kleiner und zugleich dichter wird.

</li>

</ul>

Vorausgesetzt werden das Integral einer Variablen und der Hauptsatz ([Teil 2](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/integralrechnung-im-rn/integralrechnung-im-rn.html)). Folgen, Reihen und das Supremum wiederholt der nächste Abschnitt. $n$ zählt immer die Glieder einer Folge, $x$ ist die Stelle auf der Achse.
:::

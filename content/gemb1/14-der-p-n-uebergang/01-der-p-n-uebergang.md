---
title: Überblick: Der p-n-Übergang
kurz: Überblick
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Der p-n-Übergang
order: 4240100
summary: Wie aus zwei dotierten Gebieten ein Ventil für Strom wird
tags: p-n-Übergang, Diode, Bandverbiegung, Raumladungszone, Diffusionsspannung, Schottky-Näherung, Diodenkennlinie, Sperrsättigungsstrom
lang: de
---

## Worum es geht

Ein Stück dotiertes Silizium ist ein Widerstand: Es leitet in beide Richtungen gleich gut. Grenzen aber im selben Kristall ein p-dotiertes und ein n-dotiertes Gebiet aneinander, lässt das Stück Strom in der einen Richtung durch und sperrt ihn in der anderen. Darauf beruhen Gleichrichter, Solarzellen und Leuchtdioden. Die Frage dieses Kapitels lautet: *Was geschieht an der Grenze, warum hängt der Strom so stark von der Richtung ab, und wie rechnet man ihn aus?* Wer das kann, sagt aus Dotierung und Materialdaten die Kennlinie eines solchen Bauelements voraus.

Der Weg führt über acht Begriffe. Ein __p-n-Übergang__ ist die Grenze zwischen einem p- und einem n-Gebiet im selben Kristall, eine __Diode__ das Bauelement daraus. __Bandverbiegung__ heißt, dass die Bandkanten einem ortsabhängigen Potential folgen. Die __Raumladungszone__ ist eine Schicht, in der ortsfeste Ladung nicht ausgeglichen ist. Die __Diffusionsspannung__ ist die Potentialdifferenz über dieser Schicht. Die __Schottky-Näherung__ ersetzt ihre Ladung durch ein Kastenprofil. Die __Diodenkennlinie__ ist der Strom als Funktion der Spannung, der __Sperrsättigungsstrom__ der kleine Strom, der in der sperrenden Richtung bleibt.

**So arbeitest du mit diesem Kapitel.** Die Abschnitte bauen aufeinander auf, jeder neue Begriff hat einen eigenen Unterabschnitt mit Beispiel. Kästen zum Aufklappen enthalten Hintergrund (warum etwas so ist und woher es kommt), Herleitungen und Hinweise zur Simulation; zum Weiterlesen braucht man sie nicht. Versuche die Aufgaben (★ bis ★★★) zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf.

:::merke Das Rechenmodell für dieses Kapitel
<ul>

<li>

⁠**Silizium bei 300 K:** $k_\mathrm BT=25{,}85$ meV, $E_\mathrm g=1{,}12$ eV, $N_\mathrm C=2{,}82\cdot10^{19}\,\mathrm{cm^{-3}}$, $N_\mathrm V=1{,}83\cdot10^{19}\,\mathrm{cm^{-3}}$, $n_\mathrm i=8{,}9\cdot10^{9}\,\mathrm{cm^{-3}}$ ([Teil 11](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/eigenhalbleiter-und-dotierung/eigenhalbleiter-und-dotierung.html)), $\varepsilon_\mathrm r=11{,}7$, also $\varepsilon=\varepsilon_0\varepsilon_\mathrm r=1{,}036\cdot10^{-10}$ A s/(V m).

</li>

<li>

⁠**Diode:** links p-Gebiet mit $N_\mathrm A=5\cdot10^{16}\,\mathrm{cm^{-3}}$, rechts n-Gebiet mit $N_\mathrm D=10^{16}\,\mathrm{cm^{-3}}$, Grenze bei $x=0$, Fläche $A=1\,\mathrm{mm^2}$.

</li>

<li>

⁠**Minoritätsträger:** Elektronen im p-Gebiet mit $\mu_\mathrm n=925\,\mathrm{cm^2/(V\,s)}$, Löcher im n-Gebiet mit $\mu_\mathrm p=419\,\mathrm{cm^2/(V\,s)}$ ([Teil 12](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/strom-im-halbleiter/strom-im-halbleiter.html)), Rekombinationszeit auf beiden Seiten $\tau_\text{rec}=1$ µ s. Alle Zahlen rechnet `rechnung_kap14.py` nach.

</li>

</ul>
:::

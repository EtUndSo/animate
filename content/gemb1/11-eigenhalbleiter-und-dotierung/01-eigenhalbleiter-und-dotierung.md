---
title: Überblick: Eigenhalbleiter und Dotierung
kurz: Überblick
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Eigenhalbleiter und Dotierung
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/eigenhalbleiter-und-dotierung
knoten: Kapitel 11: Eigenhalbleiter und Dotierung
order: 4210100
summary: Wie viele Ladungsträger ein Halbleiter hat und wie man ihre Zahl festlegt
tags: Halbleiter, Eigenhalbleiter, Dotierung, Donator, Akzeptor, Ladungsneutralität, Störstellenerschöpfung, Störstellenreserve
lang: de
---

## Worum es geht

Ein Stück reines Silizium enthält bei Raumtemperatur so wenige bewegliche Ladungen, dass es kaum leitet. Ein Chip braucht aber Gebiete, in denen ihre Zahl genau festgelegt ist und sich beim Erwärmen kaum ändert. Die Frage dieses Kapitels lautet: *Wie viele Ladungsträger enthält ein Halbleiter, wie stellt man ihre Zahl gezielt ein, und was geschieht mit ihr, wenn sich die Temperatur ändert?* Wer das beantworten kann, kann für jedes Material, jede Dotierung und jede Temperatur angeben, wie viele Elektronen und Löcher vorhanden sind und wo die Fermi-Energie liegt.

Der Weg führt über acht Begriffe. Ein __Halbleiter__ ist ein Kristall, dessen Bandlücke so klein ist, dass Wärme einige Elektronen ins Leitungsband hebt. Ein __Eigenhalbleiter__ ist ein reiner Halbleiter ohne Fremdatome. __Dotierung__ heißt: Man baut gezielt wenige Fremdatome ein. Ein __Donator__ ist ein Fremdatom, das ein Elektron abgibt, ein __Akzeptor__ eines, das ein Elektron aufnimmt. Die __Ladungsneutralität__ verlangt, dass ein Stück Kristall insgesamt ungeladen ist. Die __Störstellenerschöpfung__ ist der Temperaturbereich, in dem alle Fremdatome ionisiert sind, die __Störstellenreserve__ der Bereich, in dem ein Teil von ihnen neutral bleibt.

**So arbeitest du mit diesem Kapitel.** Die Abschnitte bauen aufeinander auf, jeder neue Begriff hat einen eigenen Unterabschnitt mit Beispiel. Kästen zum Aufklappen enthalten Hintergrund (warum etwas so ist und woher es kommt), Herleitungen und Hinweise zur Simulation; zum Weiterlesen braucht man sie nicht. Versuche die Aufgaben (★ bis ★★★) zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf.

:::merke Das Rechenmodell für dieses Kapitel
<ul>

<li>

⁠**Wärme:** $k_\mathrm B=8{,}617\cdot10^{-5}$ eV/K, also $k_\mathrm BT=25{,}85$ meV bei $T=300$ K.

</li>

<li>

⁠**Silizium:** $E_\mathrm g=1{,}12$ eV, in den Rechnungen temperaturunabhängig. $m_\mathrm C^*=1{,}08\,m_0$ und $m_\mathrm V^*=0{,}81\,m_0$ wie in [Kapitel 10](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/zustandsdichte-und-fermi-verteilung/zustandsdichte-und-fermi-verteilung.html), also bei 300 K $N_\mathrm C=2{,}82\cdot10^{19}\,\mathrm{cm^{-3}}$ und $N_\mathrm V=1{,}83\cdot10^{19}\,\mathrm{cm^{-3}}$. Dazu $\varepsilon_\mathrm r=11{,}7$ und $5{,}0\cdot10^{22}$ Atome je cm$^3$.

</li>

<li>

⁠**Probe:** Phosphor mit $N_\mathrm D=10^{16}\,\mathrm{cm^{-3}}$ und $\Delta E_\mathrm D=45$ meV.

</li>

</ul>
:::

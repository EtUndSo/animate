---
title: Überblick: Strom im Halbleiter
kurz: Überblick
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Strom im Halbleiter
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/strom-im-halbleiter
knoten: Kapitel 12: Strom im Halbleiter
order: 4220100
summary: Wie aus einer verschobenen Besetzung ein Strom wird und was ihn bremst
tags: Stromdichte, Streuung, Phonon, Verteilungsfunktion, Boltzmann-Transportgleichung, Beweglichkeit, Leitfähigkeit, Hall-Effekt
lang: de
---

## Worum es geht

Ein Stück Silizium liegt an einer Spannung, und es fließt Strom. Die früheren Teile haben gezählt, wie viele Elektronen und Löcher dafür bereitstehen. Offen ist, was diese Teilchen im Kristall tun. Die Frage dieses Kapitels lautet: *Wie wird aus besetzten Zuständen ein Strom, was bremst ihn, und wie hängt er von Temperatur und Dotierung ab?* Wer das beantworten kann, kann den Widerstand jedes Halbleitergebiets berechnen, gezielt einstellen und aus einer Messung die Eigenschaften der Ladungsträger bestimmen.

Der Weg führt über acht Begriffe. Die __Stromdichte__ ist der Strom je Querschnittsfläche. __Streuung__ heißen die Stöße, die einen Ladungsträger aus seinem Zustand werfen. Ein __Phonon__ ist ein Energiequant der Gitterschwingung. Die __Verteilungsfunktion__ sagt, wie wahrscheinlich ein Zustand an einem Ort besetzt ist, die __Boltzmann-Transportgleichung__, wie sie sich ändert. Die __Beweglichkeit__ ist die Driftgeschwindigkeit je Feldstärke, die __Leitfähigkeit__ die Stromdichte je Feldstärke. Der __Hall-Effekt__ ist eine Querspannung im Magnetfeld.

**So arbeitest du mit diesem Kapitel.** Die Abschnitte bauen aufeinander auf, jeder neue Begriff hat einen eigenen Unterabschnitt mit Beispiel. Kästen zum Aufklappen enthalten Hintergrund (warum etwas so ist und woher es kommt), Herleitungen und Hinweise zur Simulation; zum Weiterlesen braucht man sie nicht. Versuche die Aufgaben (★ bis ★★★) zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf.

:::merke Das Rechenmodell für dieses Kapitel
<ul>

<li>

⁠**Silizium bei 300 K** wie in [Kapitel 11](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/eigenhalbleiter-und-dotierung/eigenhalbleiter-und-dotierung.html): $k_\mathrm BT=25{,}85$ meV, $E_\mathrm g=1{,}12$ eV, $N_\mathrm C=2{,}82\cdot10^{19}\,\mathrm{cm^{-3}}$, $N_\mathrm V=1{,}83\cdot10^{19}\,\mathrm{cm^{-3}}$, $n_\mathrm i=8{,}9\cdot10^{9}\,\mathrm{cm^{-3}}$. **Probe:** n-Typ mit $N_\mathrm D=10^{16}\,\mathrm{cm^{-3}}$, $\Delta E_\mathrm D=45$ meV.

</li>

<li>

⁠**Träger:** im reinen Kristall $\mu_\mathrm n=1400$ und $\mu_\mathrm p=450\,\mathrm{cm^2/(V\,s)}$, effektive Massen $m_\mathrm n^*=0{,}26\,m_0$ und $m_\mathrm p^*=0{,}37\,m_0$.

</li>

<li>

⁠**Kette:** $a=0{,}25$ nm, $t_0=0{,}5$ eV, Band $E(k)=E_\mathrm C+2t_0(1-\cos(ka))$ mit $m^*=1{,}22\,m_0$ an der Unterkante ([Kapitel 2](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/das-teilchen-in-der-box/das-teilchen-in-der-box.html)). Alle Zahlen rechnet `rechnung_kap12.py` nach.

</li>

</ul>
:::

---
title: Überblick: Diffusion, Rekombination und Grundgleichungen
kurz: Überblick
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Diffusion, Rekombination und Grundgleichungen
order: 4230100
summary: Wie weit zusätzliche Ladungsträger kommen und welche Gleichungen alles zusammenfassen
tags: Diffusion, Teilchenstromdichte, Fick-Gesetz, Kontinuitätsgleichung, Generation, Rekombination, Einstein-Beziehung, Diffusionslänge
lang: de
---

## Worum es geht

Trifft Licht auf einen Halbleiter, entstehen dort zusätzliche Elektronen und Löcher. Sie bleiben nicht, wo sie entstanden sind. Sie breiten sich auch ohne Feld aus, und nach kurzer Zeit sind sie wieder fort. Die Frage dieses Kapitels lautet: *Wie weit kommen zusätzliche Ladungsträger, bevor sie verschwinden, und welche Gleichungen beschreiben alles, was im Halbleiter geschieht?* Wer das beantworten kann, kann berechnen, wo im Kristall wie viele Träger sitzen und welcher Strom fließt, sobald das Gleichgewicht gestört ist.

Der Weg führt über acht Begriffe. __Diffusion__ ist die Ausbreitung von Teilchen durch ihre ungeordnete Bewegung. Die __Teilchenstromdichte__ zählt die Teilchen, die je Fläche und Zeit eine Ebene durchqueren. Das __Fick-Gesetz__ verknüpft sie mit dem Gefälle der Dichte. Die __Kontinuitätsgleichung__ ist die Buchführung über die Teilchen in einem Volumen. __Generation__ ist das Entstehen eines Paars aus Elektron und Loch, __Rekombination__ sein Verschwinden. Die __Einstein-Beziehung__ verbindet Diffusion und Beweglichkeit. Die __Diffusionslänge__ ist die mittlere Tiefe, die ein Ladungsträger bis zu seiner Rekombination erreicht.

**So arbeitest du mit diesem Kapitel.** Die Abschnitte bauen aufeinander auf, jeder neue Begriff hat einen eigenen Unterabschnitt mit Beispiel. Kästen zum Aufklappen enthalten Hintergrund (warum etwas so ist und woher es kommt), Herleitungen und Hinweise zur Simulation; zum Weiterlesen braucht man sie nicht. Versuche die Aufgaben (★ bis ★★★) zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf.

:::merke Das Rechenmodell für dieses Kapitel
<ul>

<li>

⁠**Silizium bei 300 K:** $k_\mathrm BT/e=25{,}85$ mV, $\varepsilon_0\varepsilon_\mathrm r=1{,}04\cdot10^{-10}$ A s/(V m), $n_\mathrm i=8{,}9\cdot10^{9}\,\mathrm{cm^{-3}}$ ([Teil 11](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/eigenhalbleiter-und-dotierung/eigenhalbleiter-und-dotierung.html)).

</li>

<li>

⁠**Probe:** n-Silizium, $N_\mathrm D=10^{16}\,\mathrm{cm^{-3}}$, $\mu_\mathrm n=1200$ und $\mu_\mathrm p=419\,\mathrm{cm^2/(V\,s)}$ ([Teil 12](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/strom-im-halbleiter/strom-im-halbleiter.html)), $\tau_\text{rec}=1$ µ s.

</li>

<li>

⁠**Dotieren:** Bor in Silizium, $D_0=6\,\mathrm{cm^2/s}$, $E_\text{Diff}=3{,}6$ eV, 1100 °C. Alle Zahlen rechnet `rechnung_kap13.py` nach.

</li>

</ul>
:::

---
title: Überblick: Der reale MOS-Kondensator
kurz: Überblick
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Der reale MOS-Kondensator
order: 4260100
summary: Was einen gebauten Kondensator vom idealen unterscheidet und wie die Kapazität es verrät
tags: Austrittsarbeitsdifferenz, Oxidladung, Grenzflächenladung, Flachbandspannung, Interfacezustand, C-V-Kennlinie, Tiefenverarmung, Charge-Coupled Device
lang: de
---

## Worum es geht

[Teil 15](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/die-mos-kapazitat/die-mos-kapazitaet.html) hat einen Kondensator berechnet, in dem Metall und Halbleiter dieselbe Austrittsarbeit haben und im Isolator keine einzige Ladung sitzt. So einen Kondensator gibt es nicht. Die Frage dieses Kapitels lautet: *Was ändert sich am idealen Modell, wenn man wirkliche Stoffe verwendet, und wie findet man durch eine Messung heraus, was in einem fertigen Kondensator steckt?* Wer das beantworten kann, kann vorhersagen, bei welcher Spannung die Oberfläche eines gebauten Bauelements umschlägt, und aus einer Messkurve auf Schichten schließen, die man nicht sehen kann.

Der Weg führt über acht Begriffe. Die __Austrittsarbeitsdifferenz__ ist der Unterschied der Austrittsarbeiten von Metall und Halbleiter. Eine __Oxidladung__ sitzt fest im Isolator, eine __Grenzflächenladung__ fest an seiner Grenze zum Halbleiter. Die __Flachbandspannung__ ist die Gatespannung, bei der die Bänder im Halbleiter flach verlaufen. Ein __Interfacezustand__ ist ein Zustand an der Grenzfläche, der Elektronen aufnehmen und abgeben kann. Die __C-V-Kennlinie__ ist die Kapazität über der Gatespannung. __Tiefenverarmung__ heißt, dass die Verarmungszone weiter wächst, als es im Gleichgewicht möglich wäre. Ein __Charge-Coupled Device__ schiebt Ladung von Kondensator zu Kondensator.

**So arbeitest du mit diesem Kapitel.** Die Abschnitte bauen aufeinander auf, jeder neue Begriff hat einen eigenen Unterabschnitt mit Beispiel. Kästen zum Aufklappen enthalten Hintergrund (warum etwas so ist und woher es kommt), Herleitungen und Hinweise zur Simulation; zum Weiterlesen braucht man sie nicht. Versuche die Aufgaben (★ bis ★★★) zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf.

:::merke Das Rechenmodell für dieses Kapitel
Es ist der Kondensator aus [Teil 15](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/die-mos-kapazitat/die-mos-kapazitaet.html), jetzt mit einem wirklichen Gate.

<ul>

<li>

⁠**Aus [Teil 15](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/die-mos-kapazitat/die-mos-kapazitaet.html):** $T=300$ K, $V_\mathrm T=25{,}85$ mV, Silizium mit $n_\mathrm i=8{,}9\cdot10^{9}\,\mathrm{cm^{-3}}$, $\varepsilon=11{,}7\,\varepsilon_0$ und $\chi_\mathrm{SC}=4{,}05$ eV. p-Substrat mit $N_\mathrm A=3\cdot10^{16}\,\mathrm{cm^{-3}}$ in Störstellenerschöpfung. 20 nm $\mathrm{SiO_2}$ mit $\varepsilon_\mathrm{IS}=3{,}9\,\varepsilon_0$.

</li>

<li>

⁠**Daraus:** $C'_\mathrm{IS}=172{,}7\,\mathrm{nF/cm^2}$, $\gamma=0{,}578\,\sqrt{\mathrm V}$, $\varphi_\mathrm{s,WI}=0{,}389$ V, $\varphi_\mathrm{s,SI}=0{,}777$ V, $L_\mathrm{depl,max}=183$ nm, $\Phi_\mathrm{SC}=5{,}00$ eV.

</li>

<li>

⁠**Neu:** Das Gate besteht aus Aluminium mit $\Phi_\mathrm M=4{,}10$ eV. Alle Zahlen rechnet `rechnung_kap16.py` nach.

</li>

</ul>
:::

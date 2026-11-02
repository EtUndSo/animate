---
title: Überblick: Die MOS-Kapazität
kurz: Überblick
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Die MOS-Kapazität
order: 4250100
summary: Wie eine Spannung am Gate die Oberfläche eines Halbleiters umdreht
tags: MIS-Kondensator, Gate, Oberflächenpotential, Flachbandfall, Akkumulation, Verarmung, Inversion, Schwellspannung
lang: de
---

## Worum es geht

Ein Kondensator aus zwei Metallplatten speichert Ladung, und sonst geschieht in den Platten nichts. Ersetzt man eine Platte durch einen Halbleiter, greift das Feld in das Material hinein und ordnet dort die Ladungsträger um. Die Frage dieses Kapitels lautet: *Was geschieht in einem Halbleiter unter einer isolierten Metallplatte, wenn man an diese Platte eine Spannung legt, und wie groß sind Ladung, Bandverbiegung und Kapazität?* Wer das beantworten kann, kann die Leitfähigkeit einer Halbleiteroberfläche berechnen, die sich über eine Elektrode steuern lässt, durch die kein Strom fließt.

Der Weg führt über acht Begriffe. Der __MIS-Kondensator__ besteht aus Metall, Isolator und Halbleiter. Das __Gate__ ist seine Metallelektrode. Das __Oberflächenpotential__ gibt an, wie stark sich die Bänder an der Grenzfläche zum Isolator verbiegen. Im __Flachbandfall__ verbiegen sie sich gar nicht. Bei __Akkumulation__ sammeln sich die Majoritätsträger an der Grenzfläche, bei __Verarmung__ werden sie von dort verdrängt, bei __Inversion__ überwiegen dort die Minoritätsträger. Die __Schwellspannung__ ist die Gatespannung, ab der diese Umkehr vollständig ist.

**So arbeitest du mit diesem Kapitel.** Jede Stufe ist ein eigener kurzer Artikel mit der Idee, typischen Fragen zum Aufklappen und Aufgaben (★ bis ★★★). Versuche die Aufgaben zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf. Schließe eine Stufe ab, bevor du zur nächsten gehst.

:::merke Das Rechenmodell für dieses Kapitel
<ul>

<li>

⁠**Wärme:** $T=300$ K, $k_\mathrm BT=25{,}85$ meV, __Temperaturspannung__ $V_\mathrm T=k_\mathrm BT/e=25{,}85$ mV.

</li>

<li>

⁠**Silizium:** $E_\mathrm g=1{,}12$ eV, $N_\mathrm C=2{,}82\cdot10^{19}\,\mathrm{cm^{-3}}$, $N_\mathrm V=1{,}83\cdot10^{19}\,\mathrm{cm^{-3}}$, $n_\mathrm i=8{,}9\cdot10^{9}\,\mathrm{cm^{-3}}$ wie in [Teil 11](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/eigenhalbleiter-und-dotierung/eigenhalbleiter-und-dotierung.html). Permittivität $\varepsilon=\varepsilon_0\varepsilon_\mathrm r=1{,}036\cdot10^{-10}$ F/m mit $\varepsilon_\mathrm r=11{,}7$. $E_\mathrm{Fi}$ gilt als Bandmitte, es liegt nur 6 meV darunter.

</li>

<li>

⁠**Substrat:** p-Silizium, $N_\mathrm A=3\cdot10^{16}\,\mathrm{cm^{-3}}$, in Störstellenerschöpfung.

</li>

<li>

⁠**Isolator:** $\mathrm{SiO_2}$ mit $d_\mathrm{IS}=20$ nm und $\varepsilon_\mathrm{IS}=3{,}9\,\varepsilon_0$. Alle Zahlen rechnet `rechnung_kap15.py` nach.

</li>

</ul>
:::

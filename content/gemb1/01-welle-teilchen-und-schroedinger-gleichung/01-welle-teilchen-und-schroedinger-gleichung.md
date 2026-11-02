---
title: Überblick: Welle, Teilchen und Schrödinger-Gleichung
kurz: Überblick
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Welle, Teilchen und Schrödinger-Gleichung
order: 4110100
summary: Was ein Elektron im Material ist und wie man es berechnet
tags: Elektronen, Leitfähigkeit, Quantenmechanik, Bauelemente
lang: de
---

## Worum es geht

Ein Kupferkabel leitet Strom, seine Kunststoffhülle nicht, und im Chip eines Telefons schalten Milliarden winziger Schalter aus Silizium. In allen diesen Stoffen sitzen __Elektronen__, die leichten, negativ geladenen Teilchen der Atomhülle. Und doch unterscheiden sich die Stoffe in ihrer __Leitfähigkeit__, dem Maß dafür, wie gut ein Stoff Strom leitet, um fast 30 Zehnerpotenzen. Die Frage dieses Kapitels lautet: *Was ist ein Elektron im Material, und mit welcher Gleichung rechnet man es aus?* Die Antwort gibt die __Quantenmechanik__, die Physik der kleinsten Teilchen. Sie ist das Werkzeug, mit dem man Stoffe versteht und __Bauelemente__ wie Dioden und Transistoren berechnet.

**So arbeitest du mit diesem Kapitel.** Jede Stufe ist ein eigener kurzer Artikel mit der Idee, typischen Fragen zum Aufklappen und Aufgaben (★ bis ★★★). Versuche die Aufgaben zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf. Schließe eine Stufe ab, bevor du zur nächsten gehst.

:::merke Das Rechenmodell für dieses Kapitel
<ul>

<li>

⁠**Konstanten:** Elementarladung $e=1{,}602\cdot10^{-19}$ C, Planck-Konstante $h=6{,}626\cdot10^{-34}$ J s, $\hbar=h/(2\pi)=1{,}055\cdot10^{-34}$ J s $=6{,}58\cdot10^{-16}$ eV s, Elektronenmasse $m_0=9{,}109\cdot10^{-31}$ kg, Boltzmann-Konstante $k_\mathrm B=1{,}381\cdot10^{-23}$ J/K.

</li>

<li>

⁠**Stoff:** Kupfer bei $T=300$ K mit der Leitfähigkeit $\sigma=5{,}9\cdot10^{7}$ S/m und $n=8{,}5\cdot10^{28}$ freien Elektronen je m$^3$, eines je Atom.

</li>

<li>

⁠**Probe-Elektron:** frei, Masse $m_0$, Bewegungsenergie 1 eV.

</li>

<li>

⁠**Anordnung:** zwei Metallplatten im Abstand $d=100$ nm an der Spannung $U=1$ V.

</li>

</ul>

Alle Zahlen rechnet `rechnung_kap1.py` nach.
:::

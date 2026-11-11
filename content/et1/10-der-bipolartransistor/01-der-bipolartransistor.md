---
title: Überblick: Der Bipolartransistor
kurz: Überblick
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Der Bipolartransistor
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor
knoten: Kapitel 10: Der Bipolartransistor
order: 1200100
summary: Wie eine kleine Spannung einen großen Strom durch eine gesperrte Diode steuert
tags: Bipolartransistor
lang: de
---

## Worum es geht

Ein Mikrofon liefert Millivolt, ein Lautsprecher braucht Volt. Ein Rechnerausgang liefert Milliampere, ein Motor braucht Ampere. Dazwischen sitzt ein Bauteil, das mit einem kleinen Signal einen großen Strom steuert. Der klassische Vertreter ist der __Bipolartransistor__, ein Halbleiterbauelement aus drei Schichten mit drei Anschlüssen. Die Energie kommt aus der Versorgungsspannung, das Signal stellt nur ein. Der andere wichtige Typ, der MOSFET, prägt die Digitaltechnik und ist nicht Thema dieses Kapitels. Die Frage lautet: *Wie kann eine Spannung von 0,6 V einen Strom steuern, der durch eine gesperrte Diode fließt?*

**So arbeitest du mit diesem Kapitel.** Die Abschnitte bauen aufeinander auf, jeder neue Begriff hat einen eigenen Unterabschnitt mit Beispiel. Kästen zum Aufklappen enthalten Hintergrund (warum etwas so ist und woher es kommt), Herleitungen und Hinweise zur Simulation; zum Weiterlesen braucht man sie nicht. Versuche die Aufgaben (★ bis ★★★) zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf.

:::merke Das Rechenmodell für dieses Kapitel
<ul>

<li>

⁠**Transistor T:** ein npn-Kleinsignaltransistor aus Silizium mit $B=200$, $I_\mathrm{S}=1{,}9\cdot10^{-13}$ A (Sättigungssperrstrom, [Kapitel 9](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden/halbleiter-und-dioden.html)) und $U_T=26$ mV (Temperaturspannung bei 300 K, gerundet aus 25,85 mV). Zum Rechnen von Hand nähert man $U_\mathrm{BE}=0{,}6$ V, wenn der Transistor leitet, und $U_\mathrm{CE,sat}=0{,}2$ V, wenn er ganz durchgeschaltet ist. Grenzdaten: $U_\mathrm{CE,max}=40$ V, $I_\mathrm{C,max}=100$ mA, $P_\mathrm{max}=400$ mW.

</li>

<li>

⁠**Schaltung:** Versorgung $U_\mathrm{CC}=12$ V, Kollektorwiderstand $R_\mathrm{C}=3$ k$\Omega$, Basiswiderstand $R_\mathrm{B}=440$ k$\Omega$, Eingangsspannung $U_\mathrm{ein}=5$ V. Das ergibt den Arbeitspunkt $I_\mathrm{B}=10$ µ A, $I_\mathrm{C}=2$ mA, $U_\mathrm{CE}=6$ V.

</li>

<li>

⁠**Gegengekoppelte Fassung:** Basisteiler $R_1=31$ k$\Omega$, $R_2=9$ k$\Omega$, Emitterwiderstand $R_\mathrm{E}=1$ k$\Omega$ (Stufe [7](gegenkopplung-halt-den-arbeitspunkt-fest.html#stufe-7)).

</li>

</ul>

:::

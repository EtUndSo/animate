---
title: Überblick: Zustandsdichte und Fermi-Verteilung
kurz: Überblick
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Zustandsdichte und Fermi-Verteilung
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/zustandsdichte-und-fermi-verteilung
knoten: Kapitel 10: Zustandsdichte und Fermi-Verteilung
order: 4200100
summary: Plätze mal Besetzung: Wie viele Ladungsträger ein Kristall enthält
tags: Ladungsträger, Ladungsträgerdichte, k-Raum, Zustandsdichte, Entropie, Fermi-Verteilung, Fermi-Energie, effektive Zustandsdichte
lang: de
---

## Worum es geht

In einem Stück Kupfer und in einem Stück Silizium stecken gleichermaßen unvorstellbar viele Elektronen. Fast alle sitzen fest. Die wenigen, die sich bewegen können, sind es, die ein Material brauchbar machen. Die Frage dieses Kapitels lautet: *Wie viele bewegliche Elektronen und Löcher enthält ein Stoff bei gegebener Temperatur, und wie rechnet man das aus, ohne ein einziges Teilchen zu verfolgen?* Wer das kann, versteht, warum sich Stoffe mit ähnlich vielen Elektronen elektrisch um viele Größenordnungen unterscheiden und wie stark die Temperatur eingreift.

Der Weg führt über acht Begriffe. __Ladungsträger__ sind bewegliche Ladungen, also Elektronen im Leitungsband und Löcher im Valenzband. Die __Ladungsträgerdichte__ ist ihre Zahl je Volumen. Der __k-Raum__ ist der Raum der Wellenvektoren, in dem man Zustände abzählt. Die __Zustandsdichte__ nennt die Zahl der Plätze für Elektronen je Energieintervall und Volumen. Die __Entropie__ misst, auf wie viele Arten sich eine Verteilung verwirklichen lässt. Die __Fermi-Verteilung__ gibt an, mit welcher Wahrscheinlichkeit ein Platz besetzt ist, die __Fermi-Energie__ ist ihr Bezugspunkt. Die __effektive Zustandsdichte__ fasst ein ganzes Band zu einer einzigen Zahl zusammen.

**So arbeitest du mit diesem Kapitel.** Die Abschnitte bauen aufeinander auf, jeder neue Begriff hat einen eigenen Unterabschnitt mit Beispiel. Kästen zum Aufklappen enthalten Hintergrund (warum etwas so ist und woher es kommt), Herleitungen und Hinweise zur Simulation; zum Weiterlesen braucht man sie nicht. Versuche die Aufgaben (★ bis ★★★) zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf.

:::merke Das Rechenmodell für dieses Kapitel
<ul>

<li>

⁠**Wärme:** $T=300$ K, also $k_\mathrm BT=25{,}85$ meV.

</li>

<li>

⁠**Silizium:** $E_\mathrm g=1{,}12$ eV, effektive Masse $m_\mathrm C^*=1{,}08\,m_0$ im Leitungsband und $m_\mathrm V^*=0{,}81\,m_0$ im Valenzband.

</li>

<li>

⁠**Kette:** $a=0{,}25$ nm, $t_0=0{,}5$ eV, Bandbreite 2 eV, $m^*=1{,}22\,m_0$ am unteren Rand.

</li>

<li>

⁠**Metall:** Kupfer mit einem beweglichen Elektron je Atom, FCC mit $a=0{,}3615$ nm ([Kapitel 6](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/kristallgitter/kristallgitter.html)), also $n=8{,}47\cdot10^{22}\,\mathrm{cm^{-3}}$.

</li>

<li>

⁠**Konstante:** $\hbar^2/(2m_0)=0{,}0381\,\mathrm{eV\,nm^2}$. Zahlen: `rechnung_kap10.py`.

</li>

</ul>
:::

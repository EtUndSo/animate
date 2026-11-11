---
title: Überblick: Der Operationsverstärker
kurz: Überblick
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Der Operationsverstärker
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-operationsverstarker
knoten: Kapitel 11: Der Operationsverstärker
order: 1210100
summary: Wie aus einem riesigen, ungenauen Faktor ein Bauteil wird, dessen Verhalten nur noch die Widerstände bestimmen
tags: Operationsverstärker, Leerlaufverstärkung, Gegenkopplung
lang: de
---

## Worum es geht

Ein __Operationsverstärker__, kurz OPV, ist ein integrierter Verstärker aus einigen Dutzend Transistoren. Er verstärkt die Spannung zwischen seinen zwei Eingängen rund 100000-fach. Dieser Faktor heißt __Leerlaufverstärkung__. Er schwankt von Exemplar zu Exemplar um den Faktor vier und ändert sich mit der Temperatur. Trotzdem baut man aus diesem Bauteil Verstärker, die von dieser Schwankung nur 0,01 % spüren, dazu Addierer und Integrierer. Die Frage lautet: *Wie wird aus einem riesigen, ungenauen Faktor ein Bauteil, dessen Verhalten nur noch die Widerstände bestimmen?* Die Antwort heißt __Gegenkopplung__: Ein Teil der Ausgangsspannung wird so zum Eingang zurückgeführt, dass er seiner eigenen Ursache entgegenwirkt.

**So arbeitest du mit diesem Kapitel.** Die Abschnitte bauen aufeinander auf, jeder neue Begriff hat einen eigenen Unterabschnitt mit Beispiel. Kästen zum Aufklappen enthalten Hintergrund (warum etwas so ist und woher es kommt), Herleitungen und Hinweise zur Simulation; zum Weiterlesen braucht man sie nicht. Versuche die Aufgaben (★ bis ★★★) zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf.

:::merke Das Rechenmodell für dieses Kapitel
<ul>

<li>

⁠**OPV V:** Leerlaufverstärkung $A=100000$ (Exemplare 50000 bis 200000), Eingangswiderstand $r_\mathrm{e}=1$ M$\Omega$, Ausgangswiderstand $r_\mathrm{a}=75\,\Omega$. Versorgung $\pm12$ V, der Ausgang erreicht $\pm11$ V und höchstens 20 mA. Für Stufe [10](wo-die-regeln-enden.html#stufe-10): Transitfrequenz $f_\mathrm{T}=1$ MHz (dort ist $A$ auf 1 gefallen), Offset $U_\mathrm{off}=1$ mV (Rest-Differenz der Eingänge), Eingangsruhestrom $I_\mathrm{B}=50$ nA (Basisstrom der Eingangstransistoren), Gleichtaktunterdrückung 90 dB (Dämpfung gemeinsamer Störungen).

</li>

<li>

⁠**Beschaltung:** $R_1=10$ k$\Omega$, $R_2=40$ k$\Omega$, $U_\mathrm{E}=1$ V.

</li>

<li>

⁠**Differenzstufe:** Transistoren T aus [Kapitel 10](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor/der-bipolartransistor.html) ($B=200$, $U_T=26$ mV), $I_0=2$ mA, $R_\mathrm{C}=3$ k$\Omega$.

</li>

<li>

⁠**Sensor:** 1 mV effektiv, Innenwiderstand 10 k$\Omega$, Bandbreite (durchgelassener Frequenzbereich) 20 kHz, Temperatur 300 K.

</li>

</ul>

:::

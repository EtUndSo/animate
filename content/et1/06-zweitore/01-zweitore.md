---
title: Überblick: Zweitore
kurz: Überblick
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Zweitore
order: 1160100
summary: Warum vier Zahlen ein ganzes Netzwerk ersetzen und jede Parameterform nur eine andere Wahl ist
tags: Zweitor, Tor
lang: de
---

## Worum es geht

Zwischen Quelle und Last sitzt oft ein weiteres Netzwerk: ein Kabel, ein Filter, ein Dämpfungsglied oder ein Verstärker. Es hat eine Eingangsseite und eine Ausgangsseite, und von außen zählt nur, was es mit Spannung und Strom macht. Ein Netzwerk mit zwei solchen Anschlusspaaren heißt __Zweitor__, jedes Anschlusspaar ist ein __Tor__. [Teil 5](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html) hat ein Netzwerk an einem Klemmenpaar durch zwei Zahlen ersetzt, Ersatzspannung und Innenwiderstand. Die Frage dieses Kapitels lautet: *Wie viele Zahlen braucht man bei zwei Klemmenpaaren, und wie misst man sie von außen?*



**So arbeitest du mit diesem Kapitel.** Jede Stufe ist ein eigener kurzer Artikel mit der Idee, typischen Fragen zum Aufklappen und Aufgaben (★ bis ★★★). Versuche die Aufgaben zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf. Schließe eine Stufe ab, bevor du zur nächsten gehst.

:::merke Das Rechenmodell für dieses Kapitel
<ul>

<li>

⁠**T-Zweitor:** eine T-Schaltung ([Teil 5](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)) mit dem Längswiderstand $R_\mathrm{a}=15\,\Omega$ am Eingang, dem Querwiderstand $R_\mathrm{b}=20\,\Omega$ zur durchgehenden unteren Leitung und dem Längswiderstand $R_\mathrm{c}=20\,\Omega$ am Ausgang.

</li>

<li>

⁠**Betrieb:** An Tor 1 liegt eine reale Spannungsquelle mit $U_\mathrm{q}=9$ V und $R_\mathrm{q}=5\,\Omega$, an Tor 2 die Last $R_\mathrm{L}=60\,\Omega$.

</li>

<li>

⁠**Verstärker:** ein Modell mit 2 k$\Omega$ am Eingang, Stromverstärkung 100, 20 k$\Omega$ am Ausgang, Last 5 k$\Omega$, gezeigt in Stufe [7](hybridform.html#stufe-7).

</li>

<li>

Alle Größen sind Gleichgrößen. Alle Zahlen rechnet `rechnung_kap6.py` nach.

</li>

</ul>
:::

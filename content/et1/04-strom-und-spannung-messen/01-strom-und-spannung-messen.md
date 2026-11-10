---
title: Überblick: Strom und Spannung messen
kurz: Überblick
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Strom und Spannung messen
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-und-spannung-messen
knoten: Kapitel 4: Strom und Spannung messen
order: 1140100
summary: Warum jedes Messgerät die Schaltung verändert und wie man trotzdem genau misst
tags: Innenwiderstand, Messwerk, Messbereich
lang: de
---

## Worum es geht

An einem Spannungsteiler sollen 3 V liegen, das Messgerät zeigt 2,73 V. Der Teiler ist in Ordnung, und die Anzeige stimmt: Sie zeigt die Spannung, die anliegt, seit das Gerät angeschlossen ist. Denn ein Messgerät ist ein Bauteil mit einem __Innenwiderstand__, dem Widerstand zwischen seinen Anschlüssen. Die Frage lautet: *Warum verändert jedes Messgerät die Schaltung, die es misst, wie groß ist der Fehler, und warum misst eine Brücke genauer als ein Instrument allein?*



**So arbeitest du mit diesem Kapitel.** Die Abschnitte bauen aufeinander auf, jeder neue Begriff hat einen eigenen Unterabschnitt mit Beispiel. Kästen zum Aufklappen enthalten Hintergrund (warum etwas so ist und woher es kommt), Herleitungen und Hinweise zur Simulation; zum Weiterlesen braucht man sie nicht. Versuche die Aufgaben (★ bis ★★★) zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf.

:::merke Das Rechenmodell für dieses Kapitel
<ul>

<li>

⁠**Instrument:** ein __Messwerk__ (der Teil des Geräts, der Strom in einen Zeigerausschlag umsetzt) mit Vollausschlag bei $I_\mathrm M=50$ µ A und dem Eigenwiderstand $R_\mathrm M=2$ k$\Omega$. Als Amperemeter im __Messbereich__ (Wertebereich der Anzeige) bis 10 mA hat es $R_\mathrm{iA}=10\,\Omega$, als Voltmeter im Bereich bis 10 V hat es $R_\mathrm{iV}=200$ k$\Omega$ (Stufe [2](den-messbereich-erweitern.html#stufe-2)). Seine Anzeige weicht höchstens um 1 % des Bereichsendwerts ab.

</li>

<li>

⁠**Messobjekt:** $R=1{,}8$ k$\Omega$ an einer idealen Spannungsquelle $U=9$ V (sie hält 9 V bei jedem Strom). Ohne Messgerät fließen 5 mA.

</li>

<li>

⁠**Teiler:** $R_1=60$ k$\Omega$ und $R_2=30$ k$\Omega$ in Reihe an 9 V, an $R_2$ liegen 3 V.

</li>

<li>

⁠**Brücke:** $R_1=1$ k$\Omega$, $R_2=1{,}8$ k$\Omega$, $R_3=1$ k$\Omega$ an 9 V; gesucht ist $R_4$. Für kleine Änderungen vier Widerstände von je 350 $\Omega$ an 9 V.

</li>

</ul>

Alle Zahlen rechnet `rechnung_kap4.py` nach.
:::

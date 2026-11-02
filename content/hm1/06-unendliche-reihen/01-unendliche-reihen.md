---
title: Überblick: Unendliche Reihen
kurz: Überblick
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Unendliche Reihen
order: 1260100
summary: Wann hat eine Summe ohne Ende einen Wert?
tags: Teilsumme, Reihe, Konvergenz, geometrische Reihe, harmonische Reihe, absolute Konvergenz, Quotientenkriterium, Umordnung
lang: de
---

## Worum es geht

Ein Signal läuft in einer Rückkopplungsschleife im Kreis, jeder Umlauf halbiert es. Am Ausgang addieren sich die Anteile $1+\frac12+\frac14+\frac18+\dots$ Das sind unendlich viele Summanden, das Ergebnis ist die endliche Zahl 2. Auch bei $1+\frac12+\frac13+\frac14+\dots$ schrumpfen die Summanden, doch diese Summe wächst über jede Grenze. Die Frage lautet: *Was ist eine Summe mit unendlich vielen Summanden, und woran erkennt man, ob sie einen Wert hat?*

Die Antwort: Man addiert die ersten $N$ Zahlen, das ergibt eine __Teilsumme__, und lässt $N$ wachsen. Die Folge der Teilsummen heißt __Reihe__. Hat sie einen Grenzwert, liegt __Konvergenz__ vor. Der Maßstab ist die __geometrische Reihe__ $1+q+q^2+\dots$, in der jeder Summand das $q$-Fache des vorigen ist. Die __harmonische Reihe__ $1+\frac12+\frac13+\dots$ zeigt, dass schrumpfende Summanden nicht reichen. Eine __absolute Konvergenz__ liegt vor, wenn die Reihe auch dann konvergiert, wenn man alle Minuszeichen durch Pluszeichen ersetzt. Das __Quotientenkriterium__, ein Test mit dem Verhältnis benachbarter Summanden, prüft das am häufigsten. Eine __Umordnung__, also dieselben Summanden in anderer Reihenfolge, kann ohne absolute Konvergenz den Wert ändern.



**So arbeitest du mit diesem Kapitel.** Jede Stufe ist ein eigener kurzer Artikel mit der Idee, typischen Fragen zum Aufklappen und Aufgaben (★ bis ★★★). Versuche die Aufgaben zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf. Schließe eine Stufe ab, bevor du zur nächsten gehst.

:::merke Das Rechenmodell für dieses Kapitel
<ul>

<li>

⁠**Halbierungsreihe:** $G_N=\sum_{n=0}^N(\frac12)^n$, also $1;\ 1{,}5;\ 1{,}75;\ \dots$ Das ist die Summenfolge aus [Teil 4](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte/folgen-und-grenzwerte.html). Sie strebt gegen 2.

</li>

<li>

⁠**Harmonische Reihe:** $H_N=\sum_{n=1}^N\frac1n$, also $1;\ 1{,}5;\ 1{,}833;\ 2{,}083;\ \dots$ Sie wächst über jede Grenze.

</li>

<li>

⁠**Alternierende harmonische Reihe** (die Vorzeichen wechseln): $L_N=\sum_{n=1}^N(-1)^{n+1}\frac1n$, also $1;\ 0{,}5;\ 0{,}833;\ 0{,}583;\ \dots$ Sie konvergiert, aber nur dank der Vorzeichen.

</li>

<li>

⁠**Quadratreihe:** $Q_N=\sum_{n=1}^N\frac1{n^2}$, also $1;\ 1{,}25;\ 1{,}361;\ 1{,}424;\ \dots$ Sie konvergiert ohne jede Hilfe von Vorzeichen.

</li>

</ul>

Alle Zahlen rechnet `rechnung_kap6.py` nach.
:::

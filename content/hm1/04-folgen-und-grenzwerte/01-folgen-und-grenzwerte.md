---
title: Überblick: Folgen und Grenzwerte
kurz: Überblick
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Folgen und Grenzwerte
order: 1240100
summary: Was „beliebig nah“ heißt und warum die reellen Zahlen keine Lücke haben dürfen
tags: Folge, Grenzwert, Epsilon-Kriterium, Konvergenz, Nullfolge, Vollständigkeit, Monotonie, Cauchy-Folge
lang: de
---

## Worum es geht

Die Zahlen $1;\ 1{,}5;\ 1{,}75;\ 1{,}875;\ \dots$ legen jeweils die Hälfte des Rests bis 2 zurück und erreichen die 2 nie. Eine solche nie endende Liste heißt __Folge__, ihr Zielwert __Grenzwert__. Die Frage lautet: *Was heißt „beliebig nah“ genau, und woran erkennt man, dass es einen Grenzwert gibt?*

Die Antwort ist ein Toleranztest, das __Epsilon-Kriterium__. Wer ihn besteht, zeigt __Konvergenz__ (die Folge hat einen Grenzwert), bei Grenzwert 0 heißt sie __Nullfolge__. Die __Vollständigkeit__ der reellen Zahlen (keine Lücken, [Teil 1](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html)) gibt Folgen mit __Monotonie__ (sie laufen nur in eine Richtung) und jeder __Cauchy-Folge__ (die Glieder kommen einander beliebig nah) ein Ziel.



**So arbeitest du mit diesem Kapitel.** Jede Stufe ist ein eigener kurzer Artikel mit der Idee, typischen Fragen zum Aufklappen und Aufgaben (★ bis ★★★). Versuche die Aufgaben zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf. Schließe eine Stufe ab, bevor du zur nächsten gehst.

:::merke Das Rechenmodell für dieses Kapitel
<ul>

<li>

⁠**Pendelfolge:** $a_n=2+d_n$ mit der Abweichung $d_n=(-1)^n\,\frac3n$, also $-1;\ 3{,}5;\ 1;\ 2{,}75;\ 1{,}4;\ 2{,}5;\ \dots$ Sie springt um die 2 herum, die Sprünge schrumpfen.

</li>

<li>

⁠**Summenfolge:** $s_n=\sum_{k=0}^n(\frac12)^k=1+\frac12+\dots+(\frac12)^n$, also $1;\ 1{,}5;\ 1{,}75;\ \dots$ Der Rest bis 2 halbiert sich in jedem Schritt.

</li>

<li>

⁠**Wurzelfolge:** $x_1=2$, $x_{n+1}=\frac12(x_n+2/x_n)$, also $2;\ \frac32;\ \frac{17}{12};\ \frac{577}{408};\ \dots$ Das sind lauter Brüche. Das Verfahren heißt __Heron-Verfahren__, seine Glieder nähern sich $\sqrt2$.

</li>

<li>

⁠**Divergente Vergleichsfolgen:** $(-1)^n$ springt ewig, $n^2$ wächst ohne Grenze.

</li>

</ul>

Alle Zahlen rechnet `rechnung_kap4.py` nach.
:::

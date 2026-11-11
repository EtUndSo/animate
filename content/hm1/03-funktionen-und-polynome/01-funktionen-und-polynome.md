---
title: Überblick: Funktionen und Polynome
kurz: Überblick
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Funktionen und Polynome
adresse: elektrotechnik/1-semester/hohere-mathematik-1/funktionen-und-polynome
knoten: Kapitel 3: Funktionen und Polynome
order: 1230100
summary: Wann sich eine Gleichung rückwärts lösen lässt und warum jede Nullstelle einen Faktor abspaltet
tags: Funktion, Umkehrfunktion, Polynom, Nullstelle, Linearfaktor, Horner-Schema, rationale Funktion, Polstelle
lang: de
---

## Worum es geht

Ein Temperatursensor liefert zu jeder Temperatur genau eine Spannung. Eine solche Zuordnung heißt __Funktion__: Jeder Eingang $x$ bekommt genau einen Ausgang $f(x)$. Vorwärts genügt Einsetzen. Gebraucht wird meist der Rückweg: Zur gemessenen Spannung $y$ ist die Temperatur $x$ gesucht, also die Lösung der Gleichung $f(x)=y$. Die Frage dieses Kapitels lautet: *Wann hat $f(x)=y$ genau eine Lösung, und wie findet man bei den wichtigsten Funktionen, den Polynomen, die Lösungen von $P(x)=0$?*

Die Antwort führt über sieben Begriffe. Die __Umkehrfunktion__ liefert den Rückweg als eigene Funktion. Ein __Polynom__ ist eine Summe von Potenzen von $x$ mit festen Zahlen davor. Eine __Nullstelle__ ist ein $x_0$ mit $P(x_0)=0$, zu ihr gehört ein __Linearfaktor__ $x-x_0$, ein Faktor ersten Grades. Das __Horner-Schema__ ist das Rechenverfahren, das ihn abspaltet. Dazu kommen die __rationale Funktion__, ein Quotient zweier Polynome, und die __Polstelle__, an der ihr Nenner null wird und ihr Betrag über jede Grenze wächst.

**So arbeitest du mit diesem Kapitel.** Die Abschnitte bauen aufeinander auf, jeder neue Begriff hat einen eigenen Unterabschnitt mit Beispiel. Kästen zum Aufklappen enthalten Hintergrund (warum etwas so ist und woher es kommt), Herleitungen und Hinweise zur Simulation; zum Weiterlesen braucht man sie nicht. Versuche die Aufgaben (★ bis ★★★) zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf.

:::merke Das Rechenmodell für dieses Kapitel
<ul>

<li>

⁠**Parabel** $h(x)=x^2-4x+3=(x-2)^2-1=(x-1)(x-3)$, tiefster Punkt $(2\,|\,{-1})$.

</li>

<li>

⁠**Glocke** $b(x)=1/(1+x^2)$ mit $b(0)=1$, $b(1)=0{,}5$, $b(3)=0{,}1$.

</li>

<li>

⁠**Polynom** $P(x)=2x^3-3x^2-11x+6=(x-3)(2x-1)(x+2)$ mit den Nullstellen $3$, $\tfrac12$ und $-2$.

</li>

<li>

⁠**Nenner** $Q(x)=x^2-x-2=(x-2)(x+1)$, zusammen die rationale Funktion $R(x)=P(x)/Q(x)$.

</li>

<li>

⁠**Polynom vierten Grades** $S(x)=x^4-3x^3+x^2+4=(x-2)^2(x^2+x+1)$ mit doppelter Nullstelle.

</li>

</ul>

:::

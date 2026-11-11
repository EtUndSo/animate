---
title: Überblick: Exponentialfunktion und Stetigkeit
kurz: Überblick
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Exponentialfunktion und Stetigkeit
adresse: elektrotechnik/1-semester/hohere-mathematik-1/exponentialfunktion-und-stetigkeit
knoten: Kapitel 5: Exponentialfunktion und Stetigkeit
order: 1250100
summary: Was alles daraus folgt, dass kleine Änderungen am Eingang kleine Änderungen am Ausgang machen
tags: Exponentialfunktion, Logarithmus, Stetigkeit, Grenzwert, Epsilon-Delta-Kriterium, Häufungspunkt, Satz vom Maximum, Zwischenwertsatz
lang: de
---

## Worum es geht

$2^{3/2}$ ist die Wurzel aus $2^3$, aber $2^{\sqrt2}$ hatte bisher keinen Sinn. Die Antwort liefern die __Exponentialfunktion__ $\exp(x)=\mathrm{e}^x$, die aus fortlaufender Verzinsung entsteht, und ihre Umkehrung, der __Logarithmus__. Wer $\sqrt2$ auf $1{,}414$ rundet, erwartet trotzdem ein fast richtiges Ergebnis. Dahinter steht die __Stetigkeit__: Kleine Änderungen am Eingang machen kleine Änderungen am Ausgang. Exakt fassen sie der __Grenzwert__ einer Funktion (der Wert, dem sich $f(x)$ nähert, wenn $x$ gegen eine Stelle läuft) und das __Epsilon-Delta-Kriterium__ (ein Toleranztest wie in [Kapitel 4](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte/folgen-und-grenzwerte.html)). Auf einem abgeschlossenen Intervall folgen daraus mit dem __Häufungspunkt__ (einer Stelle, um die sich unendlich viele Folgenglieder sammeln) der __Satz vom Maximum__ (es gibt einen größten Funktionswert) und der __Zwischenwertsatz__ (kein Wert wird übersprungen).

**So arbeitest du mit diesem Kapitel.** Die Abschnitte bauen aufeinander auf, jeder neue Begriff hat einen eigenen Unterabschnitt mit Beispiel. Kästen zum Aufklappen enthalten Hintergrund (warum etwas so ist und woher es kommt), Herleitungen und Hinweise zur Simulation; zum Weiterlesen braucht man sie nicht. Versuche die Aufgaben (★ bis ★★★) zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf.

:::merke Das Rechenmodell für dieses Kapitel
<ul>

<li>

⁠**Zinsfolge:** $z_n(x)=(1+\frac xn)^n$, zum Beispiel $z_{10}(1)=2{,}5937$. Sie führt zu $\mathrm{e}^x$.

</li>

<li>

⁠**Prüffunktion:** $k(x)=\mathrm{e}^x+x$ auf $[0,1]$, mit $k(0)=1$, $k(1)=\mathrm{e}+1=3{,}718$. Die Gleichung $k(x)=2$ lässt sich mit den bisherigen Funktionen nicht nach $x$ auflösen, die Lösung ist $x^*=0{,}4429$. Solche Gleichungen entstehen bei einer Diode mit Vorwiderstand: Die Spannung steht im Exponenten und außerhalb.

</li>

<li>

⁠**Störfälle:** Der Schalter $H(x)=0$ für $x<0$ und $H(x)=1$ für $x\ge0$ springt. Der Lücke $L(x)=\frac{x^2-4}{x-2}$ aus [Kapitel 3](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/funktionen-und-polynome/funktionen-und-polynome.html) fehlt bei 2 ein Punkt. Der Kehrwert $1/x$ wächst bei 0 ohne Grenze.

</li>

</ul>

:::

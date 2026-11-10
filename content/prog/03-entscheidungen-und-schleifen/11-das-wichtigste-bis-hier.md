---
title: Das Wichtigste bis hier
pfad: Informatik / Programmieren / Python / Entscheidungen und Schleifen
adresse: informatik/programmieren/python/entscheidungen-und-schleifen
knoten: Kapitel 3: Entscheidungen und Schleifen
order: 6041100
summary: Bedingungen, if, while und for, Wurzeln und Nullstellen durch Raten, Halbieren und Tangenten
tags: 
lang: de
---

:::kern Das Wichtigste bis hier
<ul>

<li>

Vergleiche liefern `bool`; `a <= x <= b` prüft einen Bereich. Zeichenketten werden Zeichen für Zeichen nach ihren Nummern verglichen, `"10" < "9"`.

</li>

<li>

`not`, `and`, `or` mit der Rangfolge `not` vor `and` vor `or`. `and` und `or` werten kurz aus und liefern einen ihrer Operanden.

</li>

<li>

Von den bisher bekannten Werten sind `False`, `None`, jede Null und `""` falsch, alle anderen wahr.

</li>

<li>

`if`, `elif`, `else`: Es läuft der Block der ersten wahren Bedingung. Ein Block ist an seiner Einrückung zu erkennen, üblich sind vier Leerzeichen.

</li>

<li>

`while Bedingung:` wiederholt, solange die Bedingung vor dem Durchlauf wahr ist; ändert der Block nichts an ihr, läuft die Schleife endlos, Strg+C bricht mit `KeyboardInterrupt` ab. Nie mit `!=` auf einen `float` warten.

</li>

<li>

`for k in range(start, stop, schritt):` durchläuft ganze Zahlen bis vor `stop`; Gleitkomma-Schritte rechnet man aus dem Zähler aus.

</li>

<li>

`break` beendet die innerste Schleife, `continue` den laufenden Durchlauf. Ein Akkumulator startet mit 0 (Summe, Anzahl) oder 1 (Produkt).

</li>

<li>

Raten und Prüfen: etwa $\sqrt a$ Schritte. Schrittverfahren mit Toleranz: etwa $a/\varepsilon$ Schritte, zu große Schritte springen über die Lösung.

</li>

<li>

Bisektion: Vorzeichenwechsel, Intervall halbieren, $\lceil\log_2(L/\varepsilon)\rceil$ Schritte bei der Anfangsbreite $L$, ein Bit je Schritt.

</li>

<li>

Newton: $g\leftarrow g-f(g)/f'(g)$, für die Wurzel das Heron-Rezept; $d_{n+1}=d_n^2/(2g_n)$, die Stellen verdoppeln sich, aber nur nahe der Lösung und mit $f'\ne0$.

</li>

</ul>
:::

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Ein Programm geht je nach Daten verschiedene Wege, indem es den Wahrheitswert einer Bedingung prüft und davon abhängig einen eingerückten Block einmal (`if`) oder immer wieder (`while`, `for`) ausführt.

</li>

<li>

Die Wurzel aus 2 ist die Nullstelle von $x^2-2$; die Bisektion halbiert ein Intervall mit Vorzeichenwechsel und braucht für zwölf Stellen 41 Schritte, das Newton-Verfahren folgt der Tangente, quadriert dabei den Fehler und braucht nur 5.

</li>

<li>

Weil Gleitkommazahlen gerundet sind, endet jedes solche Verfahren nicht bei Gleichheit, sondern bei einer Toleranz, und die Toleranz muss zur Größe der Zahlen passen, sonst läuft die Schleife endlos.

</li>

</ol>
:::

**Ein Prinzip hinter allen Ergebnissen.** Fast alles in diesem Kapitel folgt aus zwei Gedanken: Jede Entscheidung und jede Wiederholung hängt an einem Wahrheitswert, und jedes Näherungsverfahren ist eine Schleife, die einen Bereich der Unsicherheit verkleinert, bis er unter einer Toleranz liegt. Wie schnell das geht, hängt davon ab, wie viel ein einzelner Schritt über die Lösung erfährt.

| Ergebnis | Woher es kommt |
|---|---|
| `1 < x < 10` meint dasselbe wie in der Mathematik | verketteter Vergleich wird zu `and` (Abschnitt [1](bedingungen-vergleiche-und-logische-operatoren.html#stufe-1)) |
| `n != 0 and 10 / n > 1` ist sicher | Kurzschlussauswertung: rechts nur, wenn nötig (Abschnitt [1](bedingungen-vergleiche-und-logische-operatoren.html#stufe-1)) |
| `eingabe or "Standard"` | `or` liefert den entscheidenden Operanden (Abschnitt [1](bedingungen-vergleiche-und-logische-operatoren.html#stufe-1)) |
| Einrückung ist Pflicht | sie ersetzt die Klammern um einen Block (Abschnitt [2](entscheidungen-if-elif-und-else.html#stufe-2)) |
| `while x != 1.0` endet nicht | Rundungsfehler häufen sich, $1{,}0$ wird übersprungen (Abschnitt [3](wiederholen-mit-while.html#stufe-3)) |
| `range(n)` hat genau $n$ Zahlen | der Stopp gehört nicht dazu (Abschnitt [4](zahlen-mit-for-und-range.html#stufe-4)) |
| Summe beginnt bei 0, Produkt bei 1 | leere Summe und leeres Produkt (Abschnitt [5](schleifen-steuern-verschachteln-und-ergebnisse-sammeln.html#stufe-5)) |
| Raten und Schritte sind langsam | ein Schritt schließt nur einen Kandidaten oder ein Stück $h$ aus (Abschnitt [6](losungen-durch-probieren-raten-und-prufen-naherung-mit-toleranz.html#stufe-6)) |
| Bisektion: 41 Schritte für $\sqrt2$ | ein Schritt halbiert den Bereich, ein Bit je Schritt (Abschnitt [7](die-bisektion.html#stufe-7)) |
| Newton: 5 Schritte für $\sqrt2$ | die Tangente hat einen quadratischen Fehler (Abschnitt [8](das-newton-verfahren.html#stufe-8)) |
| Newton kriecht bei einem Startzins weit weg | dort ist $f/f'\approx q/n$, $q$ sinkt je Schritt nur um etwa den $n$-ten Teil (Abschnitt [9](anwendung-der-zinssatz-eines-ratenkredits.html#stufe-9)) |

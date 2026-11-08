---
title: Das Wichtigste bis hier
pfad: Informatik / Programmieren / Python / Werte, Typen und Variablen
knoten: Python 2: Werte, Typen und Variablen
order: 6031200
summary: Ganze Zahlen, Gleitkommazahlen und komplexe Zahlen, Namen für Objekte, Text, Ein- und Ausgabe
tags: 
lang: de
---

:::kern Das Wichtigste bis hier
<ul>

<li>

Jeder Wert ist ein Objekt mit Typ, Identität und Wert; `type` und `id` zeigen Typ und Identität. Der Typ legt fest, was erlaubt ist; Methoden ruft man mit `objekt.name()` auf.

</li>

<li>

`int` ist exakt und beliebig groß. `/` liefert immer einen `float`; `//` rundet nach $-\infty$, und es gilt $a=(a\,/\!/\,b)\cdot b+a\,\%\,b$ mit dem Rest im Vorzeichen von $b$. `**` geht vor dem Vorzeichen und gruppiert von rechts.

</li>

<li>

Binärzahl: $\sum b_i2^i$; Bit, Byte (8 Bit, 0 bis 255), hexadezimal (4 Bit je Ziffer). Ein Bruch endet binär genau dann, wenn sein gekürzter Nenner eine Zweierpotenz ist; $0{,}1=0{,}0\,0011\,0011\ldots{}_2$.

</li>

<li>

`float` = binary64: $x=(-1)^s(1+t/2^{52})\cdot2^{c-1023}$, 53 Stellen Mantisse, Bereich bis $1{,}8\cdot10^{308}$. Gespeichert wird der nächste `float`, bei Gleichstand der mit gerader Mantisse; `0.1` ist $3602879701896397/2^{55}$. Angezeigt wird die kürzeste Dezimalzahl, die denselben `float` ergibt.

</li>

<li>

Jede Rechnung wird gerundet, relativ höchstens um $\varepsilon_{\mathrm M}/2=2^{-53}$; $\varepsilon_{\mathrm M}=2^{-52}\approx2{,}2\cdot10^{-16}$. Fehler summieren sich, kleine Summanden werden absorbiert, fast gleiche Zahlen löschen sich aus. Überlauf ergibt `inf`, ungültige Rechnungen `nan`.

</li>

<li>

Eine Zuweisung bindet einen Namen an ein Objekt und kopiert nichts. Namen: Buchstaben, Ziffern, `_`, keine Ziffer vorn, kein Schlüsselwort. `x += a` heißt `x = x + (a)`.

</li>

<li>

Vergleiche liefern `bool`. Gleitkommazahlen vergleicht man mit Toleranz, $|a-b|\le\max(r\max(|a|,|b|),t_{\mathrm{abs}})$, fertig mit `math.isclose`. `is` prüft die Identität, etwa `x is None`.

</li>

<li>

`import modul` bindet einen Modulnamen; `math` für reelle, `cmath` für komplexe Funktionen, `sys.float_info` für die Grenzen des `float`.

</li>

<li>

`complex`: zwei `float`, imaginäre Einheit `1j`, Attribute `real` und `imag`; Betrag `abs`, Phase `cmath.phase` oder von Hand `math.atan2(y, x)`.

</li>

<li>

Text: `+` verkettet, `*` wiederholt, `len` zählt; f-Strings mit Formatangaben; `input` liefert immer `str`; `int`, `float`, `str` wandeln um; `round` rundet zur nächsten, bei Hälften zur geraden Zahl.

</li>

</ul>
:::

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Jeder Wert ist ein Objekt, dessen Typ festlegt, wie der Wert gespeichert wird und was man mit ihm tun kann; Namen sind nur Etiketten, die eine Zuweisung an Objekte heftet.

</li>

<li>

Ein `int` speichert ganze Zahlen exakt mit beliebig vielen Stellen, ein `float` speichert jede Zahl als Binärbruch mit 53 Stellen mal einer Zweierpotenz, deshalb ist schon $0{,}1$ nur genähert und jedes Rechenergebnis relativ um bis zu $2^{-53}$ gerundet.

</li>

<li>

Daraus folgen die Arbeitsregeln: Gleitkommazahlen mit Toleranz vergleichen, Rundungsfehler bei vielen Schritten und beim Abziehen fast gleicher Zahlen erwarten, und Text und Zahlen ausdrücklich ineinander umwandeln.

</li>

</ol>
:::

**Ein Prinzip hinter allen Ergebnissen.** Fast alles in diesem Kapitel folgt daraus, dass der Typ eines Objekts festlegt, wie sein Wert im Speicher steht: als Ziffernfolge beliebiger Länge, als Binärbruch mit 53 Stellen und einem Exponenten, als Paar solcher Binärbrüche oder als Folge von Zeichen. Aus dieser Darstellung ergeben sich die Rechenregeln.

| Ergebnis | Woher es kommt |
|---|---|
| `"2" + 3` ist ein Fehler | der Typ legt fest, was `+` bedeutet (Abschnitte [1](objekte-und-typen.html#stufe-1) und [10](zeichenketten-eingabe-und-ausgabe.html#stufe-10)) |
| `int` läuft nie über | Ziffern zur Basis $2^{30}$, so viele wie nötig (Abschnitt [2](ganze-zahlen-und-rechenoperatoren.html#stufe-2)) |
| `//` und `%` runden nach $-\infty$ | der Rest soll für $b>0$ zwischen 0 und $b-1$ liegen (Abschnitt [2](ganze-zahlen-und-rechenoperatoren.html#stufe-2)) |
| $0{,}1$ ist nicht exakt | der Nenner 10 enthält den Primfaktor 5, ein `float` nur Zweierpotenzen (Abschnitte [3](zahlen-im-binarsystem.html#stufe-3) und [4](gleitkommazahlen-der-typ-float.html#stufe-4)) |
| `0.1` wird als `0.1` angezeigt | kürzeste Dezimalzahl, die denselben `float` ergibt (Abschnitt [4](gleitkommazahlen-der-typ-float.html#stufe-4)) |
| Abstände der `float` wachsen mit dem Betrag | feste Zahl von 53 Mantissenstellen (Abschnitte [4](gleitkommazahlen-der-typ-float.html#stufe-4) und [5](rechnen-mit-gleitkommazahlen.html#stufe-5)) |
| `0.1 + 0.2 != 0.3` | jede Rechnung wird gerundet, hier ein Gleichstand zur geraden Mantisse (Abschnitte [5](rechnen-mit-gleitkommazahlen.html#stufe-5) und [7](wahrheitswerte-und-vergleiche.html#stufe-7)) |
| Vergleich mit Toleranz | Rundungsfehler sind relativ zum Betrag (Abschnitte [7](wahrheitswerte-und-vergleiche.html#stufe-7) und [8](module-math-und-sys.html#stufe-8)) |
| `y = x` kopiert nicht | Namen sind Etiketten an Objekten (Abschnitt [6](variablen-namen-fur-objekte.html#stufe-6)) |
| `abs` und `cmath.phase` für Impedanzen | `complex` ist ein Paar von `float` (Abschnitt [9](komplexe-zahlen.html#stufe-9)) |
| `round(2.5)` ergibt 2 | Runden zur geraden Zahl, dieselbe Regel wie beim Speichern (Abschnitt [10](zeichenketten-eingabe-und-ausgabe.html#stufe-10)) |

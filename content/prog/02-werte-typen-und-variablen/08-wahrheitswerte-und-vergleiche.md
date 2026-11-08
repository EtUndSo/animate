---
title: Wahrheitswerte und Vergleiche
pfad: Informatik / Programmieren / Python / Werte, Typen und Variablen
knoten: Python 2: Werte, Typen und Variablen
order: 6030800
summary: Ob ein Messwert eine Grenze überschreitet und ob zwei Ergebnisse übereinstimmen, sind Fragen mit der Antwort ja oder nein.
tags: Vergleichsoperatoren, gleich bis auf die relative Toleranz
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Ob ein Messwert eine Grenze überschreitet und ob zwei Ergebnisse übereinstimmen, sind Fragen mit der Antwort ja oder nein. Dieser Abschnitt führt den Typ dafür ein, zeigt, wie man Zahlen vergleicht, warum man Gleitkommazahlen dabei nicht auf Gleichheit prüfen sollte, und was der Wert `None` bedeutet.
:::

### Der Typ `bool`

<span class="anker" id="stufe-7-1"></span>

„Ist die Spannung größer als 5 V?“ Die Antwort ist kein Zahlenwert, sondern ja oder nein. Python braucht Werte, die genau das ausdrücken.

**Ein Schalter mit zwei Stellungen.** Wie ein einzelnes Bit kennt ein Wahrheitswert nur zwei Zustände: wahr und falsch.

:::definition Definition 7.1 (Der Typ `bool`)
<span class="anker" id="satz-7-1"></span>

Der Typ `bool` hat genau zwei Werte, `True` (wahr) und `False` (falsch). Beide sind Schlüsselwörter.
:::

Der Name erinnert an George Boole, der im 19. Jahrhundert das Rechnen mit wahr und falsch begründete. Rechnet man mit Wahrheitswerten, behandelt Python `True` wie 1 und `False` wie 0.

**Beispiel.** Der Typ von `True`, und Rechnen mit Wahrheitswerten:

```console
>>> type(True)
<class 'bool'>
>>> True + True
2
>>> True * 10
10
```

⁠**Kurz gesagt:** `bool` hat die Werte `True` und `False`; beim Rechnen zählen sie als 1 und 0.

### Die Vergleichsoperatoren

<span class="anker" id="stufe-7-2"></span>

Woher kommen Wahrheitswerte? Meist aus einem Vergleich zweier Werte.

:::definition Definition 7.2 (Vergleichsoperatoren)
<span class="anker" id="satz-7-2"></span>

Die __Vergleichsoperatoren__ vergleichen zwei Werte und liefern einen `bool`:

|  |  |  |  |
|---|---|---|---|
| `==` | gleich | `!=` | ungleich |
| `<` | kleiner | `<=` | kleiner oder gleich |
| `>` | größer | `>=` | größer oder gleich |

Sie haben einen niedrigeren Rang als alle arithmetischen Operatoren: Python rechnet beide Seiten zuerst aus und vergleicht dann.
:::

Das doppelte `==` vergleicht, das einfache `=` bindet einen Namen. Schreibt man versehentlich `x == 5`, wo eine Zuweisung gemeint war, bindet Python nichts: Es vergleicht nur und zeigt im interaktiven Modus `True` oder `False` an.

**Beispiel.** Zahlen verschiedener Typen vergleicht Python nach ihrem Wert; eine Zahl und eine Zeichenkette sind nie gleich:

```console
>>> 7 > 5
True
>>> 2 + 3 == 5
True
>>> 3 != 3
False
>>> 1 == 1.0
True
>>> "2" == 2
False
>>> spannung = 5.3
>>> spannung > 5
True
```

⁠**Kurz gesagt:** `==`, `!=`, `<`, `<=`, `>`, `>=` vergleichen zwei Werte und liefern `True` oder `False`.

### Gleitkommazahlen nicht auf Gleichheit prüfen

<span class="anker" id="stufe-7-3"></span>

Mit dem Operator `==` lässt sich jetzt prüfen, was Abschnitt [5](rechnen-mit-gleitkommazahlen.html#stufe-5) gezeigt hat.

:::satz Satz 7.3 (Gleichheit von `float`)
<span class="anker" id="satz-7-3"></span>

Zwei `float` sind für `==` genau dann gleich, wenn sie denselben Wert haben, also bis auf die letzte Binärstelle übereinstimmen. Zwei Rechenwege, die mathematisch dasselbe ergeben, liefern wegen der Rundung oft verschiedene `float`. Und `nan` ist zu keinem Wert gleich, nicht einmal zu sich selbst.
:::

**Beispiel.** Drei Vergleiche nach einer Rechnung, dann `nan`:

```console
>>> 0.1 + 0.2 == 0.3
False
>>> 0.1 * 3 == 0.3
False
>>> 0.1 * 10 == 1.0
True
>>> nan = 1e309 - 1e309
>>> nan == nan
False
>>> nan != nan
True
```

Ob `==` bei Gleitkommazahlen `True` oder `False` liefert, hängt also vom Zufall der Rundung ab. Die dritte Zeile ist zufällig wahr, die ersten beiden zufällig falsch. Für Ergebnisse von Rechnungen ist `==` deshalb kein brauchbarer Test.

⁠**Kurz gesagt:** Ergebnisse von Gleitkommarechnungen nie mit `==` vergleichen.

### Der Vergleich mit Toleranz

<span class="anker" id="stufe-7-4"></span>

Wenn `==` nicht taugt, wie prüft man dann, ob ein Ergebnis stimmt? Man fragt nicht „gleich?“, sondern „nah genug?“.

**Wie bei Bauteiltoleranzen.** Ein Widerstand mit $4{,}7\,\mathrm{k\Omega}$ und 5 % Toleranz gilt als in Ordnung, wenn er um höchstens 5 % vom Nennwert abweicht. Die erlaubte Abweichung ist ein *Anteil* des Werts, keine feste Zahl von Ohm. Genauso vergleicht man Gleitkommazahlen.

:::definition Definition 7.4 (Vergleich mit relativer Toleranz)
<span class="anker" id="satz-7-4"></span>

Zwei Zahlen $a$ und $b$ sind __gleich bis auf die relative Toleranz__ $r$, wenn

$$|a-b|\le r\cdot\max(|a|,|b|) .$$
:::

Der Faktor $\max(|a|,|b|)$ macht den Vergleich symmetrisch: Es ist gleich, welche der beiden Zahlen man $a$ nennt. Eine übliche Wahl ist $r=10^{-9}$. Das ist weit mehr als die Rundungsfehler einer überschaubaren Rechnung, die nach Satz [5.3](rechnen-mit-gleitkommazahlen.html#satz-5-3) bei etwa $10^{-16}$ je Schritt liegen, und verlangt trotzdem neun übereinstimmende Stellen.

**Erst von Hand.** Python bringt die eingebaute Funktion `abs` für den Betrag und die eingebaute Funktion `max` für den größten von mehreren Werten mit. Damit lässt sich die Definition direkt hinschreiben:

```console
>>> abs(-3.5)
3.5
>>> max(2, 7.5, 3)
7.5
>>> a = 0.1 + 0.2
>>> b = 0.3
>>> abs(a - b) <= 1e-9 * max(abs(a), abs(b))
True
```

**Die Grenze des relativen Vergleichs.** Ist eine der beiden Zahlen 0, versagt der relative Vergleich: Dann ist $\max(|a|,|b|)=|a-b|$, und die Bedingung $|a-b|\le r\,|a-b|$ ist für $r<1$ nur erfüllt, wenn beide Zahlen genau 0 sind. Ein Ergebnis wie $10^{-20}$ ist dann nie „nah genug“ an 0. Für Vergleiche mit 0 braucht man zusätzlich eine *absolute* Toleranz $t_{\mathrm{abs}}$ mit der Einheit der Größe:

$$|a-b|\le\max\bigl(r\cdot\max(|a|,|b|),\ t_{\mathrm{abs}}\bigr).$$

Welcher Wert für $t_{\mathrm{abs}}$ passt, hängt von der Größe ab: Bei Spannungen in Volt vielleicht $10^{-9}$, bei Kapazitäten in Farad sicher viel weniger.

⁠**Kurz gesagt:** Gleitkommazahlen vergleicht man mit relativer Toleranz, $|a-b|\le r\max(|a|,|b|)$; in der Nähe von 0 braucht man zusätzlich eine absolute Toleranz.

:::hintergrund Dieselbe Prüfung in jedem Schaltungssimulator
Ein Schaltungssimulator wie SPICE berechnet die Spannungen einer Schaltung mit nichtlinearen Bauteilen schrittweise: Er verbessert eine Schätzung so lange, bis sie sich nicht mehr nennenswert ändert. Ob sie das noch tut, prüft er mit genau dieser Art von Vergleich. Der freie Simulator ngspice verlangt zum Beispiel für jede Knotenspannung:

$$|v_{k+1}-v_k|\le\mathrm{RELTOL}\cdot\max(|v_{k+1}|,|v_k|)+\mathrm{VNTOL},$$

mit den Voreinstellungen $\mathrm{RELTOL}=10^{-3}$ und $\mathrm{VNTOL}=1\,\mu\mathrm V$. Die absolute Toleranz VNTOL gibt es aus demselben Grund wie oben: Liegt eine Knotenspannung nahe 0, würde ein rein relativer Vergleich eine Genauigkeit verlangen, die schon die Rundung der Gleitkommazahlen nicht mehr hergibt, und der Simulator käme nie zum Ende. Der einzige Unterschied: SPICE addiert die beiden Toleranzen, statt das Größere zu nehmen.
:::

### Der Identitätsvergleich

<span class="anker" id="stufe-7-5"></span>

Die Vergleichsoperatoren fragen nach dem Wert. Manchmal will man aber wissen, ob zwei Namen am selben Objekt hängen, ob also zwei Etiketten am selben Kasten kleben.

:::definition Definition 7.5 (Identitätsvergleich)
<span class="anker" id="satz-7-5"></span>

Der Operator `is` liefert `True`, wenn seine beiden Operanden dasselbe Objekt sind, also dieselbe Identität haben. `is not` ist seine Verneinung.
:::

**Beispiel.** Zwei getrennt eingetippte Zahlen mit gleichem Wert sind hier zwei Objekte:

```console
>>> x = 1000.5
>>> y = 1000.5
>>> x == y
True
>>> x is y
False
>>> z = x
>>> z is x
True
```

`x` und `y` haben denselben Wert, hängen aber an zwei verschiedenen Kästen. `z = x` heftet ein zweites Etikett an den Kasten von `x`.

Für Zahlen und Zeichenketten ist `is` der falsche Operator. Ob Python für zwei gleiche Werte ein Objekt oder zwei anlegt, ist nicht festgelegt und kann sich von Version zu Version ändern. Zahlen vergleicht man mit `==`, Gleitkommazahlen mit Toleranz.

⁠**Kurz gesagt:** `is` fragt, ob zwei Namen dasselbe Objekt meinen, `==` fragt, ob zwei Werte gleich sind.

:::hintergrund Warum `is` bei kleinen Zahlen manchmal `True` liefert
CPython legt beim Start die ganzen Zahlen von $-5$ bis 256 als Objekte an und benutzt sie immer wieder, statt jedes Mal ein neues Objekt zu erzeugen; kleine Zahlen kommen in fast jedem Programm ständig vor. Deshalb ist im interaktiven Modus nach `x = 256` und `y = 256` der Vergleich `x is y` wahr, bei 257 aber nicht. Die Grenze ist eine Eigenschaft von CPython, keine Regel der Sprache, und in neueren Entwicklungsständen von CPython ist der Bereich größer. Python warnt sogar, wenn man `is` direkt mit einer Zahl im Quelltext benutzt:

```console
>>> x = 257
>>> x is 257
<python-input-1>:1: SyntaxWarning: "is" with 'int' literal. Did you mean "=="?
  x is 257
False
```
:::

### Der Wert `None`

<span class="anker" id="stufe-7-6"></span>

Manche Funktionen haben kein Ergebnis, das sie zurückgeben könnten. `print` zum Beispiel schreibt etwas ins Terminal, aber was ist der Wert des Aufrufs `print("Hallo")`? Python braucht einen Wert, der „kein Wert“ bedeutet.

:::definition Definition 7.6 (`None`)
<span class="anker" id="satz-7-6"></span>

`None` ist der einzige Wert des Typs `NoneType`. Er steht für „kein Wert“. Funktionen ohne eigentliches Ergebnis, etwa `print`, liefern `None`.
:::

Es gibt nur ein einziges Objekt `None`. Ob ein Name an `None` gebunden ist, prüft man deshalb mit `is`: `x is None`.

**Beispiel.** Der Wert eines `print`-Aufrufs:

```console
>>> ergebnis = print("Hallo")
Hallo
>>> ergebnis
>>> print(ergebnis)
None
>>> type(ergebnis)
<class 'NoneType'>
>>> ergebnis is None
True
```

Die erste Zeile schreibt `Hallo` und bindet `ergebnis` an den Wert des Aufrufs, also an `None`. Der interaktive Modus zeigt `None` nicht an; das ist der Grund, warum nach einem `print`-Aufruf keine zweite Zeile erscheint ([Programmieren, Python 1, Abschnitt 4.8](/wissen/informatik/programmieren/python/programme-und-der-python-interpreter/der-interaktive-modus.html#stufe-4-8)). Erst `print` macht `None` sichtbar.

⁠**Kurz gesagt:** `None` bedeutet „kein Wert“; man prüft darauf mit `is None`.

### Aufgaben zu Abschnitt [7](#stufe-7)

<span class="anker" id="stufe-7-7"></span>

:::aufgabe Aufgabe 25 ★ Wahrheitswerte vorhersagen
<span class="anker" id="aufg-25"></span>

Sage vorher und prüfe: (a) `3 == 3.0`, (b) `"3" == 3`, (c) `2 ** 10 > 1000`, (d) `7 // 2 == 3.5`, (e) `True + True + True`, (f) `0.5 + 0.25 == 0.75`, (g) `0.1 + 0.7 == 0.8`. Warum ist (f) wahr, obwohl man Gleitkommazahlen nicht auf Gleichheit prüfen soll?

:::loesung
```console
>>> 3 == 3.0
True
>>> "3" == 3
False
>>> 2 ** 10 > 1000
True
>>> 7 // 2 == 3.5
False
>>> True + True + True
3
>>> 0.5 + 0.25 == 0.75
True
>>> 0.1 + 0.7 == 0.8
False
```

(a) Zahlen werden nach dem Wert verglichen. (b) Ein Text ist nie gleich einer Zahl. (c) $1024>1000$. (d) $7\,/\!/\,2=3$. (e) `True` zählt als 1. (f) $0{,}5$, $0{,}25$ und $0{,}75$ sind endliche Binärbrüche, alle exakt gespeichert, und auch ihre Summe ist exakt darstellbar: Es entsteht kein Rundungsfehler. Das ist aber Glück der gewählten Zahlen; im Allgemeinen weiß man nicht, ob alle beteiligten Werte exakt sind. (g) `0.1 + 0.7` ergibt `0.7999999999999999`.
:::
:::

:::aufgabe Aufgabe 26 ★★ Ist der Widerstand in Ordnung?
<span class="anker" id="aufg-26"></span>

Ein Widerstand hat den Nennwert $4{,}7\,\mathrm{k\Omega}$ und 5 % Toleranz. Gemessen werden $4{,}52\,\mathrm{k\Omega}$ und $4{,}43\,\mathrm{k\Omega}$.

<ol class="al">

<li>

Prüfe beide Messwerte mit einem Ausdruck, der `True` oder `False` liefert. Die Toleranz bezieht sich auf den Nennwert.

</li>

<li>

Worin unterscheidet sich dein Ausdruck von der Definition in Unterabschnitt [7.4](#stufe-7-4)? Für welches Paar aus Messwert und Nennwert liefern beide Formen verschiedene Antworten? Gib ein Beispiel.

</li>

</ol>

:::loesung
(a) Erlaubt sind $5\,\%$ von $4700\,\Omega$, also $235\,\Omega$:

```console
>>> nenn = 4700
>>> abs(4520 - nenn) <= 0.05 * nenn
True
>>> abs(4430 - nenn) <= 0.05 * nenn
False
```

$4{,}52\,\mathrm{k\Omega}$ weicht um $180\,\Omega$ ab und ist in Ordnung, $4{,}43\,\mathrm{k\Omega}$ um $270\,\Omega$ und nicht.

(b) Hier bezieht sich die Toleranz auf den Nennwert, in der Definition auf den größeren der beiden Beträge. Ist der Messwert größer als der Nennwert, ist die erlaubte Abweichung in der Definition etwas größer. Beispiel $4940\,\Omega$: Die Abweichung ist $240\,\Omega$; bezogen auf den Nennwert sind nur $235\,\Omega$ erlaubt, bezogen auf $\max(4940,4700)$ aber $247\,\Omega$:

```console
>>> abs(4940 - nenn) <= 0.05 * nenn
False
>>> abs(4940 - nenn) <= 0.05 * max(abs(4940), abs(nenn))
True
```

Für Rundungsfehler mit $r=10^{-9}$ spielt der Unterschied keine Rolle; bei einer Bauteiltoleranz muss man sich an die Festlegung halten, dass sie sich auf den Nennwert bezieht.
:::
:::

:::aufgabe Aufgabe 27 ★★ Vergleiche nahe null
<span class="anker" id="aufg-27"></span>

Ein Programm prüft, ob ein berechneter Strom 0 ist. Herausgekommen ist `i = 3e-19`.

<ol class="al">

<li>

Was liefern `i == 0` und der relative Vergleich mit $r=10^{-9}$?

</li>

<li>

Wähle eine sinnvolle absolute Toleranz für Ströme in Ampere in einer Schaltung, in der Ströme im Milliamperebereich fließen, und prüfe mit der Formel mit beiden Toleranzen.

</li>

</ol>

:::loesung
(a)

```console
>>> i = 3e-19
>>> i == 0
False
>>> abs(i - 0) <= 1e-9 * max(abs(i), abs(0))
False
```

Beide sagen „nicht null“. Beim relativen Vergleich steht rechts $10^{-9}\cdot3\cdot10^{-19}$, und das ist kleiner als $3\cdot10^{-19}$: An der Null versagt der relative Vergleich immer.

(b) Ströme im Milliamperebereich tragen Rundungsfehler von etwa $10^{-3}\cdot10^{-16}=10^{-19}\,\mathrm A$. Eine absolute Toleranz von $10^{-12}\,\mathrm A=1\,\mathrm{pA}$ liegt weit darüber und weit unter jedem Strom, der in der Schaltung zählt; derselbe Wert ist in SPICE als ABSTOL voreingestellt:

```console
>>> abs(i - 0) <= max(1e-9 * max(abs(i), abs(0)), 1e-12)
True
```
:::
:::

:::aufgabe Aufgabe 28 ★ Was liefert `print`?
<span class="anker" id="aufg-28"></span>

Sage vorher, was der interaktive Modus bei jeder Zeile anzeigt, und prüfe:

```python
x = print(42)
x
print(x)
x is None
print(print("a"))
```

:::loesung
```console
>>> x = print(42)
42
>>> x
>>> print(x)
None
>>> x is None
True
>>> print(print("a"))
a
None
```

Die erste Zeile schreibt 42 und bindet `x` an `None`, den Wert des Aufrufs. `x` allein zeigt nichts, weil der interaktive Modus `None` nicht anzeigt. `print(x)` macht `None` sichtbar. In der letzten Zeile wertet Python zuerst das innere `print("a")` aus: Es schreibt `a` und liefert `None`. Das äußere `print` schreibt dann dieses `None`.
:::
:::

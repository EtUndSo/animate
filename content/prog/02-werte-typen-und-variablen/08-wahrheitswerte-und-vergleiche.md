---
title: Wahrheitswerte und Vergleiche
pfad: Informatik / Programmieren / Python / Werte, Typen und Variablen
adresse: informatik/programmieren/python/werte-typen-und-variablen
knoten: Kapitel 2: Werte, Typen und Variablen
order: 6030800
summary: Ob eine Temperatur eine Grenze überschreitet und ob zwei Ergebnisse übereinstimmen, sind Fragen mit der Antwort ja oder nein.
tags: Vergleichsoperatoren, gleich bis auf die relative Toleranz
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Ob eine Temperatur eine Grenze überschreitet und ob zwei Ergebnisse übereinstimmen, sind Fragen mit der Antwort ja oder nein. Dieser Abschnitt führt den Typ dafür ein, zeigt, wie man Zahlen vergleicht, warum man Gleitkommazahlen dabei nicht auf Gleichheit prüfen sollte, und was der Wert `None` bedeutet.
:::

### Der Typ `bool`

<span class="anker" id="stufe-7-1"></span>

„Ist es draußen wärmer als $30\,{}^\circ\mathrm C$?“ Die Antwort ist kein Zahlenwert, sondern ja oder nein. Python braucht Werte, die genau das ausdrücken.

**Ein Schalter mit zwei Stellungen.** Wie ein einzelnes Bit kennt ein Wahrheitswert nur zwei Zustände: wahr und falsch.

:::definition Definition 7.1 (Der Typ `bool`)
<span class="anker" id="satz-7-1"></span>

Der Typ `bool` hat genau zwei Werte, `True` (wahr) und `False` (falsch). Beide sind Schlüsselwörter.
:::

Der Name erinnert an George Boole, der im 19. Jahrhundert das Rechnen mit wahr und falsch begründete. Rechnet man mit Wahrheitswerten, behandelt Python `True` wie 1 und `False` wie 0.

::::beispiel
Der Typ von `True`, und Rechnen mit Wahrheitswerten:

```console
>>> type(True)
<class 'bool'>
>>> True + True
2
>>> True * 10
10
```
::::

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

::::beispiel
Zahlen verschiedener Typen vergleicht Python nach ihrem Wert; eine Zahl und eine Zeichenkette sind nie gleich:

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
>>> temperatur = 31.5
>>> temperatur > 30
True
```
::::

⁠**Kurz gesagt:** `==`, `!=`, `<`, `<=`, `>`, `>=` vergleichen zwei Werte und liefern `True` oder `False`.

### Gleitkommazahlen nicht auf Gleichheit prüfen

<span class="anker" id="stufe-7-3"></span>

Mit dem Operator `==` lässt sich jetzt prüfen, was Abschnitt [5](rechnen-mit-gleitkommazahlen.html#stufe-5) gezeigt hat.

:::satz Satz 7.3 (Gleichheit von `float`)
<span class="anker" id="satz-7-3"></span>

Zwei `float` sind für `==` genau dann gleich, wenn sie denselben Wert haben, also bis auf die letzte Binärstelle übereinstimmen. Zwei Rechenwege, die mathematisch dasselbe ergeben, liefern wegen der Rundung oft verschiedene `float`. Und `nan` ist zu keinem Wert gleich, nicht einmal zu sich selbst.
:::

::::beispiel
Drei Vergleiche nach einer Rechnung, dann `nan`:

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
::::

⁠**Kurz gesagt:** Ergebnisse von Gleitkommarechnungen nie mit `==` vergleichen.

### Der Vergleich mit Toleranz

<span class="anker" id="stufe-7-4"></span>

Wenn `==` nicht taugt, wie prüft man dann, ob ein Ergebnis stimmt? Man fragt nicht „gleich?“, sondern „nah genug?“.

**Wie beim Abwiegen in der Küche.** Verlangt ein Rezept $500\,\mathrm g$ Mehl, sind $510\,\mathrm g$ kein Problem. Verlangt es $5\,\mathrm g$ Salz, wären $10\,\mathrm g$ mehr, also $15\,\mathrm g$, viel zu viel. Was als „genau genug“ gilt, ist ein *Anteil* des Werts, etwa 2 %, keine feste Zahl von Gramm. Genauso vergleicht man Gleitkommazahlen.

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

Welcher Wert für $t_{\mathrm{abs}}$ passt, hängt von der Größe und ihrer Einheit ab: Bei Geldbeträgen in Euro ist $10^{-9}$ weit weniger als ein Cent; bei Entfernungen in Lichtjahren wären $10^{-9}$ schon fast $9500\,\mathrm{km}$, dort braucht man viel weniger.

⁠**Kurz gesagt:** Gleitkommazahlen vergleicht man mit relativer Toleranz, $|a-b|\le r\max(|a|,|b|)$; in der Nähe von 0 braucht man zusätzlich eine absolute Toleranz.

:::hintergrund Dieselbe Prüfung beendet Rechenrezepte
Das Heron-Rezept aus [Kapitel 1, Abschnitt 1.1](/wissen/informatik/programmieren/python/programme-und-der-python-interpreter/programme-und-programmiersprachen.html#stufe-1-1) verbessert eine Schätzung $g$ für $\sqrt a$ mit jedem Durchgang: Aus $g$ wird $\frac12\bigl(g+\frac ag\bigr)$. Ein Programm, das solche Durchgänge selbst wiederholt, muss entscheiden, wann es aufhört. Die übliche Regel: wenn sich die Schätzung nicht mehr nennenswert ändert. Ob sie das noch tut, prüft es mit genau dieser Art von Vergleich zwischen der alten Schätzung $g_{\mathrm{alt}}$ und der neuen $g_{\mathrm{neu}}$:

$$|g_{\mathrm{neu}}-g_{\mathrm{alt}}|\le\max\bigl(r\cdot\max(|g_{\mathrm{neu}}|,|g_{\mathrm{alt}}|),\ t_{\mathrm{abs}}\bigr).$$

Die absolute Toleranz braucht man aus demselben Grund wie oben. Für $a=0$ ist $\frac ag=0$, und jeder Durchgang halbiert nur die Schätzung. Die Änderung ist dann immer genau die Hälfte des alten Werts, und ein rein relativer Vergleich mit $r<\frac12$ ist nie erfüllt, obwohl die Schätzung schnell praktisch 0 ist. Ohne absolute Toleranz liefe das Rezept, von $g=1$ aus, 1075 Durchgänge lang, bis die Schätzung unter den kleinsten positiven `float` fällt und genau 0 wird; im nächsten Durchgang scheitert dann $\frac ag$ an der Division durch null. Manche Programme addieren die beiden Toleranzen auch, statt die größere zu nehmen; die erlaubte Abweichung ändert sich dadurch höchstens um den Faktor 2.
:::

### Der Identitätsvergleich

<span class="anker" id="stufe-7-5"></span>

Die Vergleichsoperatoren fragen nach dem Wert. Manchmal will man aber wissen, ob zwei Namen am selben Objekt hängen, ob also zwei Etiketten am selben Kasten kleben.

:::definition Definition 7.5 (Identitätsvergleich)
<span class="anker" id="satz-7-5"></span>

Der Operator `is` liefert `True`, wenn seine beiden Operanden dasselbe Objekt sind, also dieselbe Identität haben. `is not` ist seine Verneinung.
:::

::::beispiel
Zwei getrennt eingetippte Zahlen mit gleichem Wert sind hier zwei Objekte:

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
::::

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

::::beispiel
Der Wert eines `print`-Aufrufs:

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

Die erste Zeile schreibt `Hallo` und bindet `ergebnis` an den Wert des Aufrufs, also an `None`. Der interaktive Modus zeigt `None` nicht an; das ist der Grund, warum nach einem `print`-Aufruf keine zweite Zeile erscheint ([Kapitel 1, Abschnitt 4.8](/wissen/informatik/programmieren/python/programme-und-der-python-interpreter/der-interaktive-modus.html#stufe-4-8)). Erst `print` macht `None` sichtbar.
::::

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

:::aufgabe Aufgabe 26 ★★ Ist das Brot in Ordnung?
<span class="anker" id="aufg-26"></span>

Eine Bäckerei backt Brote mit dem Sollgewicht $750\,\mathrm g$ und lässt 5 % Abweichung zu. Gewogen werden zwei Brote mit $718\,\mathrm g$ und $709\,\mathrm g$.

<ol class="al">

<li>

Prüfe beide Gewichte mit einem Ausdruck, der `True` oder `False` liefert. Die 5 % beziehen sich auf das Sollgewicht.

</li>

<li>

Worin unterscheidet sich dein Ausdruck von der Definition in Unterabschnitt [7.4](#stufe-7-4)? Für welches Paar aus gewogenem Gewicht und Sollgewicht liefern beide Formen verschiedene Antworten? Gib ein Beispiel.

</li>

</ol>

:::loesung
(a) Erlaubt sind $5\,\%$ von $750\,\mathrm g$, also $37{,}5\,\mathrm g$:

```console
>>> soll = 750
>>> abs(718 - soll) <= 0.05 * soll
True
>>> abs(709 - soll) <= 0.05 * soll
False
```

Das Brot mit $718\,\mathrm g$ weicht um $32\,\mathrm g$ ab und ist in Ordnung, das mit $709\,\mathrm g$ um $41\,\mathrm g$ und nicht.

(b) Hier beziehen sich die 5 % auf das Sollgewicht, in der Definition auf den größeren der beiden Beträge. Ist das gewogene Gewicht größer als das Sollgewicht, ist die erlaubte Abweichung in der Definition etwas größer. Beispiel $789\,\mathrm g$: Die Abweichung ist $39\,\mathrm g$; bezogen auf das Sollgewicht sind nur $37{,}5\,\mathrm g$ erlaubt, bezogen auf $\max(789,750)$ aber $39{,}45\,\mathrm g$:

```console
>>> abs(789 - soll) <= 0.05 * soll
False
>>> abs(789 - soll) <= 0.05 * max(abs(789), abs(soll))
True
```

Für Rundungsfehler mit $r=10^{-9}$ spielt der Unterschied keine Rolle; bei einer Vorgabe wie der der Bäckerei muss man sich an die Festlegung halten, dass sie sich auf das Sollgewicht bezieht.
:::
:::

:::aufgabe Aufgabe 27 ★★ Vergleiche nahe null
<span class="anker" id="aufg-27"></span>

Ein Programm rechnet Rezepte um und prüft, ob von einer Zutat nichts mehr übrig ist. Es rechnet in Kilogramm, und die kleinsten Zutaten wiegen einige Gramm, also einige $10^{-3}\,\mathrm{kg}$. Herausgekommen ist `rest = 3e-19`.

<ol class="al">

<li>

Was liefern `rest == 0` und der relative Vergleich mit $r=10^{-9}$?

</li>

<li>

Wähle eine sinnvolle absolute Toleranz für Mengen in Kilogramm, wenn die kleinsten Mengen einige Gramm wiegen, und prüfe mit der Formel mit beiden Toleranzen.

</li>

</ol>

:::loesung
(a)

```console
>>> rest = 3e-19
>>> rest == 0
False
>>> abs(rest - 0) <= 1e-9 * max(abs(rest), abs(0))
False
```

Beide sagen „nicht null“. Beim relativen Vergleich steht rechts $10^{-9}\cdot3\cdot10^{-19}$, und das ist kleiner als $3\cdot10^{-19}$: An der Null versagt der relative Vergleich immer.

(b) Mengen von einigen Gramm, also einigen $10^{-3}\,\mathrm{kg}$, tragen Rundungsfehler von etwa $10^{-3}\cdot10^{-16}=10^{-19}\,\mathrm{kg}$. Eine absolute Toleranz von $10^{-12}\,\mathrm{kg}$, einem Milliardstel Gramm, liegt weit darüber und weit unter jeder Menge, die in einer Küche zählt:

```console
>>> abs(rest - 0) <= max(1e-9 * max(abs(rest), abs(0)), 1e-12)
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

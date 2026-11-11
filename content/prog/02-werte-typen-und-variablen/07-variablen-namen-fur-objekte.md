---
title: Variablen: Namen für Objekte
pfad: Informatik / Programmieren / Python / Werte, Typen und Variablen
adresse: informatik/programmieren/python/werte-typen-und-variablen
knoten: Kapitel 2: Werte, Typen und Variablen
order: 6030700
summary: Eine Rechnung wird lesbar, wenn die Werte Namen haben: preis / gewicht statt 4.49 / 0.45 .
tags: Zuweisung, Variable, erweiterte Zuweisung
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Eine Rechnung wird lesbar, wenn die Werte Namen haben: `preis / gewicht` statt `4.49 / 0.45`. Dieser Abschnitt zeigt, wie Python einen Namen mit einem Objekt verbindet, welche Namen erlaubt sind und warum eine Zuweisung nichts kopiert.
:::

### Die Zuweisung

<span class="anker" id="stufe-6-1"></span>

Im interaktiven Modus hält der Unterstrich `_` das letzte Ergebnis fest ([Kapitel 1, Abschnitt 4.4](/wissen/informatik/programmieren/python/programme-und-der-python-interpreter/der-interaktive-modus.html#stufe-4-4)), aber nur dieses eine und nur bis zur nächsten Rechnung. Wer einen Wert mehrmals braucht, will ihn unter einem selbst gewählten Namen aufheben.

**Ein Etikett an den Kasten heften.** Ein Objekt ist ein Kasten im Arbeitsspeicher (Abb. [1](objekte-und-typen.html#abb-1)). Man kann ein Etikett mit einem Wort beschriften und es an einen Kasten heften. Über das Wort findet man den Kasten später wieder. Ein Wort ohne Anführungszeichen hält Python für einen solchen Namen; das hat schon der `NameError` in [Kapitel 1](/wissen/informatik/programmieren/python/programme-und-der-python-interpreter/programme-und-der-python-interpreter.html) gezeigt ([Kapitel 1, Abschnitt 6.3](/wissen/informatik/programmieren/python/programme-und-der-python-interpreter/fehler-lesen-und-verstehen.html#stufe-6-3)).

:::definition Definition 6.1 (Zuweisung)
<span class="anker" id="satz-6-1"></span>

Eine __Zuweisung__ ist eine Anweisung der Form

⁠*name* `=` *ausdruck*

Python wertet den Ausdruck rechts aus und verbindet dann den Namen links mit dem Objekt, das dabei entstanden ist. Man sagt: Der Name wird an das Objekt *gebunden*.
:::

Das Gleichheitszeichen ist hier keine Gleichung wie in der Mathematik, sondern ein Auftrag: „Kapitel den Namen links an das Ergebnis rechts.“ Die Richtung ist fest: Der Name steht immer links.

::::beispiel
Preis, Gewicht und Kilopreis der Schokocreme aus [Kapitel 1, Abschnitt 4.4](/wissen/informatik/programmieren/python/programme-und-der-python-interpreter/der-interaktive-modus.html#stufe-4-4), dazu der Preis für 100 g:

```console
>>> preis = 4.49
>>> gewicht = 0.45
>>> preis / gewicht
9.977777777777778
>>> kilopreis = preis / gewicht
>>> kilopreis / 10
0.9977777777777778
```

Nach einer Zuweisung zeigt der interaktive Modus nichts an. Eine Zuweisung ist eine Anweisung ([Kapitel 1, Abschnitt 1.1](/wissen/informatik/programmieren/python/programme-und-der-python-interpreter/programme-und-programmiersprachen.html#stufe-1-1)) und kein Ausdruck; sie hat keinen Wert, den man anzeigen könnte. Ihr Ergebnis ist nur, dass der Name ab jetzt etwas bedeutet.
::::

⁠**Kurz gesagt:** `name = ausdruck` rechnet den Ausdruck aus und bindet den Namen an das Ergebnis.

### Die Variable

<span class="anker" id="stufe-6-2"></span>

Nach einigen Zuweisungen gibt es mehrere Namen, jeder an einem Objekt. Für dieses Paar aus Name und Objekt braucht man ein eigenes Wort.

**Ein Diagramm aus Namen und Pfeilen.** Man zeichnet die Namen links, die Objekte rechts und von jedem Namen einen Pfeil zu seinem Objekt. Ein solches Bild heißt Zustandsdiagramm: Es zeigt den Zustand des Programms in einem Augenblick (Abb. [9](#abb-9), links).

:::definition Definition 6.2 (Variable)
<span class="anker" id="satz-6-2"></span>

Ein Name, der an ein Objekt gebunden ist, heißt __Variable__. Der Wert der Variablen ist der Wert dieses Objekts.
:::

Eine Variable entsteht mit ihrer ersten Zuweisung. Davor ist der Name unbekannt, und Python meldet einen `NameError`.

::::beispiel
Die Sitzung aus dem letzten Unterabschnitt geht weiter:

```console
>>> kg_fuer_zehn
Traceback (most recent call last):
  File "<python-input-5>", line 1, in <module>
    kg_fuer_zehn
NameError: name 'kg_fuer_zehn' is not defined
>>> kg_fuer_zehn = 10 / kilopreis
>>> kg_fuer_zehn
1.0022271714922049
```

Erst die Zuweisung macht aus dem Namen `kg_fuer_zehn` eine Variable: So viele Kilogramm Schokocreme bekommt man für 10 Euro. Danach steht im Zustandsdiagramm ein vierter Name mit einem Pfeil auf ein `float`-Objekt mit dem Wert $1{,}002$.
::::

⁠**Kurz gesagt:** Eine Variable ist ein Name, der an ein Objekt gebunden ist; sie entsteht mit der ersten Zuweisung.

### Neu binden statt kopieren

<span class="anker" id="stufe-6-3"></span>

Was passiert bei `y = x`? Bekommt `y` eine Kopie des Werts von `x`? Und was geschieht mit `y`, wenn man danach `x` verändert?

**Etiketten umhängen.** Im Bild der Etiketten ist die Antwort einfach: `y = x` heftet ein zweites Etikett an *denselben* Kasten. `x = x + 1` rechnet mit dem Kasten, an dem `x` hängt, legt das Ergebnis in einen neuen Kasten und hängt das Etikett `x` dorthin um. Das Etikett `y` bleibt, wo es war (Abb. [9](#abb-9)).

:::abbildung prog/k2etikett 9
Zustandsdiagramme. Links: Nach `y = x` sind beide Namen an dasselbe Objekt gebunden; nichts wurde kopiert. Rechts: `x = x + 1` legt ein neues Objekt mit dem Wert 6 an und bindet `x` daran. Das Objekt 5 bleibt unverändert, und `y` hängt weiter an ihm.
:::

:::satz Satz 6.3 (Zuweisung kopiert nicht)
<span class="anker" id="satz-6-3"></span>

Eine Zuweisung legt nie eine Kopie eines Objekts an. `y = x` bindet `y` an dasselbe Objekt, an das `x` gebunden ist. Eine spätere Zuweisung an `x` bindet nur `x` neu; `y` bleibt an seinem Objekt.
:::

::::beispiel
Die Identität (Unterabschnitt [1.3](objekte-und-typen.html#stufe-1-3)) macht sichtbar, welches Objekt hinter einem Namen steht:

```console
>>> x = 5
>>> y = x
>>> id(x)
11370224
>>> id(y)
11370224
>>> x = x + 1
>>> x
6
>>> y
5
>>> id(x)
11370256
```

Nach `y = x` haben beide Namen dieselbe Identität: ein Objekt, zwei Etiketten. Nach `x = x + 1` hat `x` eine neue Identität, `y` die alte. Das Objekt 5 hat sich nicht verändert; das kann es auch nicht, denn der Wert einer Zahl bleibt für immer derselbe (Unterabschnitt [1.3](objekte-und-typen.html#stufe-1-3)).
::::

⁠**Kurz gesagt:** Eine Zuweisung heftet ein Etikett an ein Objekt oder hängt es um; sie kopiert nichts.

:::hintergrund Kästchen oder Etikett: der Unterschied zu C
In C ist eine Variable ein fester Platz im Speicher, ein Kästchen mit einem bestimmten Typ. `y = x` kopiert dort den Inhalt des Kästchens `x` in das Kästchen `y`; danach gibt es zwei unabhängige Kopien. In Python ist eine Variable dagegen ein Name, der auf ein Objekt verweist. Das Objekt trägt den Typ, der Name nicht. Deshalb darf derselbe Name erst an eine Zahl und danach an eine Zeichenkette gebunden werden, was in C nicht ginge.

Bei Zahlen fällt der Unterschied nicht auf: Ob `y` eine Kopie der 5 hat oder auf dieselbe 5 zeigt, ändert nichts, weil sich eine Zahl nie verändert. Trotzdem lohnt es sich, gleich das richtige Bild im Kopf zu haben, also Etiketten statt Kästchen. Es erklärt die Identitäten in der Sitzung oben, und es bleibt auch bei allen anderen Typen richtig.
:::

### Die Namensregeln

<span class="anker" id="stufe-6-4"></span>

Nicht jedes Wort taugt als Name. Python muss beim Übersetzen einen Namen von einer Zahl, einem Operator und den festen Wörtern der Sprache unterscheiden können.

:::definition Definition 6.4 (Namensregeln)
<span class="anker" id="satz-6-4"></span>

Ein Name besteht aus Buchstaben, Ziffern und dem Unterstrich `_`. Er darf nicht mit einer Ziffer beginnen und kein Schlüsselwort sein. Groß- und Kleinbuchstaben sind verschieden: `Wert` und `wert` sind zwei Namen.
:::

Ein Schlüsselwort ist ein Wort, das in Python eine feste Bedeutung hat. Python 3.13 und 3.14 haben 35 davon:

|  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
| `False` | `None` | `True` | `and` | `as` | `assert` | `async` |
| `await` | `break` | `class` | `continue` | `def` | `del` | `elif` |
| `else` | `except` | `finally` | `for` | `from` | `global` | `if` |
| `import` | `in` | `is` | `lambda` | `nonlocal` | `not` | `or` |
| `pass` | `raise` | `return` | `try` | `while` | `with` | `yield` |

Buchstaben mit Umlaut sind in Namen erlaubt, `größe` ist ein gültiger Name. Üblich sind aber Namen aus Kleinbuchstaben ohne Umlaute, Wörter durch Unterstriche getrennt: `preis_pro_kg`, `gewicht_g`. Daran halten sich die Programme dieses Kapitels.

::::beispiel
Drei Verstöße, jeder mit seiner Meldung:

```console
>>> 3d = 4
  File "<python-input-0>", line 1
    3d = 4
    ^
SyntaxError: invalid decimal literal
>>> mein-wert = 4
  File "<python-input-1>", line 1
    mein-wert = 4
    ^^^^^^^^^
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
>>> class = 4
  File "<python-input-2>", line 1
    class = 4
          ^
SyntaxError: invalid syntax
```

`3d` beginnt mit einer Ziffer; Python liest den Anfang als Zahl und stolpert über das `d`. `mein-wert` liest Python als Rechnung `mein` minus `wert`, und an eine Rechnung kann man nichts binden. Der Vorschlag mit `==` hilft hier nicht; gemeint war ein Name, also `mein_wert`. `class` ist ein Schlüsselwort.
::::

**Eine Falle: eingebaute Namen überschreiben.** `print`, `type`, `id` und die anderen eingebauten Funktionen sind ebenfalls Namen, aber keine Schlüsselwörter. Man darf sie neu binden, und dann sind sie weg:

```console
>>> print = 5
>>> print("Hallo")
Traceback (most recent call last):
  File "<python-input-1>", line 1, in <module>
    print("Hallo")
    ~~~~~^^^^^^^^^
TypeError: 'int' object is not callable
```

Der Name `print` hängt jetzt an der Zahl 5, und eine Zahl kann man nicht aufrufen. Abhilfe: einen anderen Namen wählen und den interaktiven Modus neu starten.

⁠**Kurz gesagt:** Namen bestehen aus Buchstaben, Ziffern und `_`, beginnen nicht mit einer Ziffer und sind keine Schlüsselwörter; eingebaute Namen sollte man nicht neu binden.

### Die erweiterte Zuweisung

<span class="anker" id="stufe-6-5"></span>

Zähler hochzählen und Werte aufsummieren kommt so oft vor, dass Python dafür eine Kurzschreibweise hat. `zaehler = zaehler + 1` nennt den Namen zweimal.

:::definition Definition 6.5 (Erweiterte Zuweisung)
<span class="anker" id="satz-6-5"></span>

Für einen arithmetischen Operator $\circ$ aus `+ - * / // % **` bedeutet die __erweiterte Zuweisung__ *name* $\circ$`=` *ausdruck* bei Zahlen dasselbe wie *name* `=` *name* $\circ$ `(`*ausdruck*`)`.
:::

Wichtig sind die Klammern: Der ganze Ausdruck rechts wird zuerst ausgerechnet. `x *= 2 + 3` verfünffacht `x`.

::::beispiel
Ein Zähler und eine Summe aus Schritten von $0{,}1$, wie in Unterabschnitt [5.1](rechnen-mit-gleitkommazahlen.html#stufe-5-1):

```console
>>> zaehler = 0
>>> zaehler += 1
>>> zaehler += 1
>>> zaehler
2
>>> summe = 0.0
>>> summe += 0.1
>>> summe += 0.1
>>> summe += 0.1
>>> summe
0.30000000000000004
>>> x = 10
>>> x *= 2 + 3
>>> x
50
```

Auch eine erweiterte Zuweisung bindet den Namen neu: `zaehler += 1` erzeugt ein neues `int`-Objekt und hängt das Etikett `zaehler` daran.
::::

⁠**Kurz gesagt:** `x += a` ist für Zahlen die Kurzform von `x = x + (a)`; ebenso `-=`, `*=`, `/=`, `//=`, `%=` und `**=`.

### Variablen im Skript

<span class="anker" id="stufe-6-6"></span>

Mit Variablen wird ein Skript zur wiederverwendbaren Rechnung: Die Annahmen stehen oben, jede einmal, und die Formeln darunter lesen sich wie im Lehrbuch. [Kapitel 1](/wissen/informatik/programmieren/python/programme-und-der-python-interpreter/programme-und-der-python-interpreter.html) hat ein Rezept für Pizzateig mit festen Zahlen von 4 auf 6 Personen umgerechnet ([Kapitel 1, Abschnitt 5.3](/wissen/informatik/programmieren/python/programme-und-der-python-interpreter/skripte-schreiben-und-ausfuhren.html#stufe-5-3)). Mit Namen sieht dasselbe Skript so aus:

```python rezept_variablen.py
# Pizzateig umrechnen, mit Namen für jede Größe
personen = 6          # so viele essen mit
personen_rezept = 4   # für so viele Personen ist das Rezept
mehl_rezept = 500     # Mehl im Rezept in g
wasser_rezept = 300   # Wasser im Rezept in ml

faktor = personen / personen_rezept   # so oft braucht man das Rezept
mehl = mehl_rezept * faktor
wasser = wasser_rezept * faktor

print("Mehl in g:", mehl)
print("Wasser in ml:", wasser)
```

```console Windows (PowerShell)
PS> py rezept_variablen.py
Mehl in g: 750.0
Wasser in ml: 450.0
```

```console Linux
$ python3 rezept_variablen.py
Mehl in g: 750.0
Wasser in ml: 450.0
```

Für eine andere Zahl von Gästen ändert man nur die zweite Zeile. Jeder Name sagt, was die Zahl bedeutet, und die Einheit steht im Kommentar dahinter, denn Python kennt keine Einheiten.

⁠**Kurz gesagt:** Variablen machen aus festen Zahlen benannte Annahmen; die Formeln darunter rechnen mit den Namen.

### Aufgaben zu Abschnitt [6](#stufe-6)

<span class="anker" id="stufe-6-7"></span>

:::aufgabe Aufgabe 21 ★ Zustandsdiagramm vorhersagen
<span class="anker" id="aufg-21"></span>

Zeichne nach jeder Zeile das Zustandsdiagramm und gib am Ende die Werte von `a`, `b` und `c` an. Prüfe im interaktiven Modus und vergleiche die Identitäten mit `id`.

```python
a = 10
b = a
a = a * 2
c = b
b = b - 1
```

:::loesung
| nach der Zeile | Bindungen | neues Objekt? |
|---|---|---|
| `a = 10` | `a` $\to$ 10 | ja, 10 |
| `b = a` | `a`, `b` $\to$ 10 | nein |
| `a = a * 2` | `a` $\to$ 20, `b` $\to$ 10 | ja, 20 |
| `c = b` | `a` $\to$ 20, `b`, `c` $\to$ 10 | nein |
| `b = b - 1` | `a` $\to$ 20, `b` $\to$ 9, `c` $\to$ 10 | ja, 9 |

Am Ende ist $a=20$, $b=9$, $c=10$. Im interaktiven Modus:

```console
>>> a = 10
>>> b = a
>>> a = a * 2
>>> c = b
>>> b = b - 1
>>> a
20
>>> b
9
>>> c
10
>>> id(c)
11370384
>>> id(b)
11370352
```

`c` hängt am ursprünglichen Objekt 10, das zuerst `a` und dann `b` hatte. Keine Zeile hat ein Objekt verändert; jede Rechnung hat ein neues angelegt, und die Zuweisungen haben nur Etiketten umgehängt.
:::
:::

:::aufgabe Aufgabe 22 ★ Erlaubte Namen
<span class="anker" id="aufg-22"></span>

Welche Namen sind erlaubt, welche nicht, und welche sind erlaubt, aber ungünstig? Begründe.

`preis_1`, `1preis`, `T_max`, `T-max`, `for`, `For`, `_zwischen`, `größe`, `type`

:::loesung
<ul>

<li>

`preis_1`: erlaubt und gut.

</li>

<li>

`1preis`: nicht erlaubt, beginnt mit einer Ziffer.

</li>

<li>

`T_max`: erlaubt; üblich wären Kleinbuchstaben, `t_max`. In einer Formel mit Formelzeichen, etwa $T$ für eine Temperatur, kann der Großbuchstabe aber sinnvoll sein.

</li>

<li>

`T-max`: nicht erlaubt; Python liest `T` minus `max`.

</li>

<li>

`for`: nicht erlaubt, Schlüsselwort.

</li>

<li>

`For`: erlaubt, weil Groß- und Kleinschreibung zählt, aber verwirrend nah am Schlüsselwort.

</li>

<li>

`_zwischen`: erlaubt; ein Unterstrich am Anfang ist zulässig.

</li>

<li>

`größe`: erlaubt, aber gegen die übliche Schreibweise ohne Umlaute.

</li>

<li>

`type`: erlaubt, aber ungünstig: Der Name der eingebauten Funktion `type` ist danach verdeckt.

</li>

</ul>
:::
:::

:::aufgabe Aufgabe 23 ★★ Erweiterte Zuweisungen
<span class="anker" id="aufg-23"></span>

Sage den Wert von `x` nach jeder Zeile vorher. Prüfe dann im interaktiven Modus.

```python
x = 7
x //= 2
x **= 3
x %= 5
x -= 2 * 3
x /= 4
```

:::loesung
```console
>>> x = 7
>>> x //= 2
>>> x
3
>>> x **= 3
>>> x
27
>>> x %= 5
>>> x
2
>>> x -= 2 * 3
>>> x
-4
>>> x /= 4
>>> x
-1.0
```

$7\,/\!/\,2=3$; $3^3=27$; $27\,\%\,5=2$; $2-(2\cdot3)=-4$, die rechte Seite wird ganz ausgerechnet; $-4/4=-1{,}0$, ein `float`, weil `/` immer einen `float` liefert.
:::
:::

:::aufgabe Aufgabe 24 ★★ Das Rezept-Skript umbauen
<span class="anker" id="aufg-24"></span>

<ol class="al">

<li>

Ändere `rezept_variablen.py` für 9 Personen und einen Brotteig: Das Rezept ist für 4 Personen und braucht $600\,\mathrm g$ Mehl und $400\,\mathrm{ml}$ Wasser. Welche Zeilen musst du ändern?

</li>

<li>

Ergänze eine Variable `mehl_kg` für das Mehl in Kilogramm und gib sie mit aus. Warum ist es besser, sie aus `mehl` zu berechnen, als die Zahl 1.35 von Hand einzutippen?

</li>

</ol>

:::loesung
(a) Nur die Annahmen oben ändern sich, hier drei davon: `personen`, `mehl_rezept` und `wasser_rezept`; das Rezept ist weiter für 4 Personen. Die Formeln bleiben. (b) `mehl_kg` wird aus `mehl` berechnet. Ändert man später die Zahl der Personen, stimmt die Anzeige in Kilogramm automatisch mit, und es gibt keine zweite Stelle, an der man die Zahl vergessen könnte:

```python rezept_brot.py
# Brotteig umrechnen, mit Namen für jede Größe
personen = 9          # so viele essen mit
personen_rezept = 4   # für so viele Personen ist das Rezept
mehl_rezept = 600     # Mehl im Rezept in g
wasser_rezept = 400   # Wasser im Rezept in ml

faktor = personen / personen_rezept   # so oft braucht man das Rezept
mehl = mehl_rezept * faktor
wasser = wasser_rezept * faktor
mehl_kg = mehl / 1000                 # Mehl in kg, aus mehl berechnet

print("Mehl in kg:", mehl_kg)
print("Mehl in g:", mehl)
print("Wasser in ml:", wasser)
```

```console Linux
$ python3 rezept_brot.py
Mehl in kg: 1.35
Mehl in g: 1350.0
Wasser in ml: 900.0
```

Probe im Kopf: 9 Personen sind $2{,}25$-mal 4 Personen, und $2{,}25\cdot600\,\mathrm g=1350\,\mathrm g$, $2{,}25\cdot400\,\mathrm{ml}=900\,\mathrm{ml}$. Unter Windows (`py rezept_brot.py`) erscheint dieselbe Ausgabe.
:::
:::

---
title: Fehler lesen und verstehen
pfad: Informatik / Programmieren / Python / Programme und der Python-Interpreter
adresse: informatik/programmieren/python/programme-und-der-python-interpreter
knoten: Kapitel 1: Programme und der Python-Interpreter
order: 6020700
summary: Jeder, der programmiert, macht Fehler.
tags: Syntaxfehler, Laufzeitfehler, Ausnahme, Traceback, Logikfehler
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Jeder, der programmiert, macht Fehler. Dieser Abschnitt unterscheidet drei Arten von Fehlern, zeigt, wann Python sie bemerkt, und wie man seine Fehlermeldungen liest.
:::

### Der Syntaxfehler

<span class="anker" id="stufe-6-1"></span>

Die erste Art von Fehler betrifft die Form des Quelltexts.

**Ein unleserliches Rezept.** Ein Koch, der beim Durchlesen eines Rezepts auf einen unleserlichen Satz stößt, fängt gar nicht erst an zu kochen. Er meldet zuerst, welcher Satz nicht zu lesen ist.

:::definition Definition 6.1 (Syntaxfehler)
<span class="anker" id="satz-6-1"></span>

Ein __Syntaxfehler__ ist eine Stelle im Quelltext, die gegen die Syntax der Sprache verstößt. Python meldet ihn, bevor irgendeine Zeile der Datei ausgeführt wird.
:::

Das folgt aus den zwei Phasen aus Unterabschnitt [2.4](vom-quelltext-zur-ausfuhrung-compiler-und-interpreter.html#stufe-2-4): Erst wird die ganze Datei übersetzt, und mit einem Syntaxfehler entsteht kein Bytecode, der laufen könnte.

::::beispiel
In der dritten Zeile fehlt die schließende Klammer:

```python syntaxfehler.py
print("Zeile 1")
print("Zeile 2")
print("Zeile 3"
```

```console Linux
$ python3 syntaxfehler.py
  File "/home/student/python-kurs/syntaxfehler.py", line 3
    print("Zeile 3"
         ^
SyntaxError: '(' was never closed
```

```console Windows (PowerShell)
PS> py syntaxfehler.py
  File "C:\Users\student\python-kurs\syntaxfehler.py", line 3
    print("Zeile 3"
         ^
SyntaxError: '(' was never closed
```

Obwohl die ersten beiden Zeilen fehlerfrei sind, erscheint nicht einmal „Zeile 1“. Die Meldung besteht aus vier Zeilen: Datei und Zeilennummer, die betroffene Zeile, ein Zeichen `^` unter der Stelle, an der Python den Fehler festmacht, und zuletzt die Fehlerart `SyntaxError` mit einer Beschreibung: „die Klammer wurde nie geschlossen“.
::::

Weitere häufige Syntaxfehler und ihre Meldungen:

| Zeile | Meldung und Ursache |
|---|---|
| `print("Ende)` | `unterminated string literal`: Die Zeichenkette wird nie geschlossen. |
| `print("Hallo"))` | `unmatched ')'`: Eine Klammer wird geschlossen, die nie geöffnet wurde. |
| `print(„Hallo“)` | `invalid character '„' (U+201E)`: typografisches statt gerades Anführungszeichen. |
| eine Zeile, die mit Leerzeichen beginnt | `IndentationError: unexpected indent`: Leerzeichen am Zeilenanfang haben in Python eine Bedeutung und dürfen dort nicht ohne Grund stehen. |

Im interaktiven Modus betrifft ein Syntaxfehler nur die eine Eingabe; danach erscheint wieder `>>>`.

⁠**Kurz gesagt:** Ein Syntaxfehler verletzt die Form; Python meldet ihn vor dem Start, und keine Zeile der Datei läuft.

:::hintergrund Warum typografische Anführungszeichen ein Syntaxfehler sind
Die Syntax von Python lässt als Anfang und Ende einer Zeichenkette nur das gerade Anführungszeichen `"` und den Apostroph `'` zu. Die Zeichen „ und “, die ein Textverarbeitungsprogramm beim Tippen einsetzt, sind für Python ganz andere Zeichen. Innerhalb einer Zeichenkette sind sie erlaubt, außerhalb gehören sie zu keinem Bestandteil der Sprache. Eine Datei mit der Zeile `print(„Hallo“)` weist Python deshalb schon beim Übersetzen zurück:

```text
  File "/home/student/python-kurs/anfuehrungszeichen.py", line 1
    print(„Hallo“)
          ^
SyntaxError: invalid character '„' (U+201E)
```

Die Meldung nennt das unerlaubte Zeichen und dazu seine Nummer: Jedes Schriftzeichen hat eine weltweit festgelegte Nummer, und U+201E ist die des unteren Anführungszeichens. Am Bildschirm sehen die Zeichen „ und `"` einander ähnlich, die Nummer unterscheidet sie eindeutig.
:::

### Der Laufzeitfehler

<span class="anker" id="stufe-6-2"></span>

Ein Quelltext kann in der Form völlig richtig sein und trotzdem etwas verlangen, das sich nicht ausführen lässt.

**Eine fehlende Zutat.** Der Koch hat das Rezept gelesen und beginnt. Bei Schritt 2 stellt er fest, dass die Eier fehlen. Schritt 1 hat er da schon erledigt; weiter als bis Schritt 2 kommt er nicht.

:::definition Definition 6.2 (Laufzeitfehler)
<span class="anker" id="satz-6-2"></span>

Ein __Laufzeitfehler__ ist ein Fehler, der erst beim Ausführen einer Zeile auftritt. Alle Zeilen davor sind schon gelaufen; das Programm bricht an dieser Stelle ab.
:::

::::beispiel
Die Division durch null ist in der Form erlaubt, lässt sich aber nicht ausführen:

```python laufzeitfehler.py
print("Zeile 1")
print(5 / 0)
print("Zeile 3")
```

```console Linux
$ python3 laufzeitfehler.py
Zeile 1
Traceback (most recent call last):
  File "/home/student/python-kurs/laufzeitfehler.py", line 2, in <module>
    print(5 / 0)
          ~~^~~
ZeroDivisionError: division by zero
```

```console Windows (PowerShell)
PS> py laufzeitfehler.py
Zeile 1
Traceback (most recent call last):
  File "C:\Users\student\python-kurs\laufzeitfehler.py", line 2, in <module>
    print(5 / 0)
          ~~^~~
ZeroDivisionError: division by zero
```

Diesmal erscheint „Zeile 1“: Die Datei wurde fehlerfrei übersetzt, und die erste Zeile ist gelaufen. In der zweiten Zeile scheitert die Division, das Programm bricht ab, und „Zeile 3“ erscheint nie. Abbildung [4](#abb-4) stellt die beiden Fälle gegenüber.

:::abbildung prog/k1fehlerarten 4
Syntaxfehler und Laufzeitfehler. Links verhindert ein Formfehler in Zeile 3 schon das Übersetzen; keine Zeile läuft. Rechts gelingt das Übersetzen, Zeile 1 läuft, und erst beim Ausführen von Zeile 2 tritt der Fehler auf.
:::
::::

⁠**Kurz gesagt:** Ein Laufzeitfehler tritt beim Ausführen einer Zeile auf; alles davor ist gelaufen, alles danach nicht.

:::hintergrund Warum ein Syntaxfehler alles stoppt, ein Laufzeitfehler aber erst ab seiner Zeile
Der Grund sind die zwei Phasen von CPython (Unterabschnitt [2.4](vom-quelltext-zur-ausfuhrung-compiler-und-interpreter.html#stufe-2-4)). In der ersten Phase prüft der Übersetzer nur die Form, und zwar die der ganzen Datei. Ohne gültige Form entsteht kein Bytecode, und die zweite Phase beginnt gar nicht. Ob sich eine Zeile auch ausführen lässt, zeigt sich erst in der zweiten Phase, wenn die Interpreterschleife bei ihr ankommt.

Bemerkenswert ist das bei `5 / 0`. Der Übersetzer rechnet feste Zahlenausdrücke wie `2 + 3` zwar schon vorab aus (Unterabschnitt [2.4](vom-quelltext-zur-ausfuhrung-compiler-und-interpreter.html#stufe-2-4)), die Division durch null aber nicht: Er lässt sie absichtlich im Bytecode stehen. Ihre Bedeutung ist nämlich festgelegt als „beim Ausführen dieser Zeile tritt ein Fehler auf“. Würde der Übersetzer sie vorab ausrechnen und dabei scheitern, liefe auch Zeile 1 nicht mehr, und das Programm verhielte sich anders, als die Semantik es vorschreibt.
:::

### Die Ausnahme

<span class="anker" id="stufe-6-3"></span>

Python braucht eine einheitliche Art, einen Fehler zu melden und das Programm an dieser Stelle anzuhalten.

:::definition Definition 6.3 (Ausnahme)
<span class="anker" id="satz-6-3"></span>

Eine __Ausnahme__ ist das Ereignis, mit dem Python einen Fehler meldet. Sie hat eine Art, zum Beispiel `ZeroDivisionError`, und eine Beschreibung, zum Beispiel `division by zero`. Tritt sie beim Ausführen auf, bricht sie das Programm an dieser Stelle ab.
:::

Ein Laufzeitfehler löst also eine Ausnahme aus. Auch einen Syntaxfehler meldet Python als Ausnahme, mit der Art `SyntaxError`, nur eben schon beim Übersetzen.

::::beispiel
Drei Arten von Ausnahmen, die in diesem Kapitel vorkommen:

<ul>

<li>

`SyntaxError`: Der Quelltext verletzt die Syntax.

</li>

<li>

`ZeroDivisionError`: Eine Division durch null.

</li>

<li>

`NameError`: Python kennt einen Namen nicht. Das passiert typischerweise, wenn bei einem Text die Anführungszeichen fehlen. Ohne Anführungszeichen hält Python ein Wort für einen Namen, wie es `print` einer ist, und sucht etwas, das so heißt:

</li>

</ul>

```python namefehler.py
print("Zeile 1")
print(Hallo)
```

```console Linux
$ python3 namefehler.py
Zeile 1
Traceback (most recent call last):
  File "/home/student/python-kurs/namefehler.py", line 2, in <module>
    print(Hallo)
          ^^^^^
NameError: name 'Hallo' is not defined
```

Die Beschreibung hängt manchmal von der Version ab. Teilt man eine Zahl mit Nachkommastellen durch null, meldet Python 3.13 unter Windows `ZeroDivisionError: float division by zero`, Python 3.14 unter Linux nur `ZeroDivisionError: division by zero`. Die Art bleibt dieselbe.
::::

⁠**Kurz gesagt:** Eine Ausnahme meldet einen Fehler mit Art und Beschreibung; beim Ausführen bricht sie das Programm ab.

### Der Traceback

<span class="anker" id="stufe-6-4"></span>

Bricht eine Ausnahme ein Programm ab, will man wissen: was, wo und warum. Python liefert dafür einen festen Bericht.

:::definition Definition 6.4 (Traceback)
<span class="anker" id="satz-6-4"></span>

Der __Traceback__ ist der Bericht, den Python ausgibt, wenn eine Ausnahme beim Ausführen ein Programm abbricht. Er nennt die Stelle im Quelltext, an der die Ausnahme auftrat, und in seiner letzten Zeile die Art und die Beschreibung der Ausnahme.
:::

::::beispiel
Abbildung [5](#abb-5) zerlegt den Traceback von `laufzeitfehler.py` in seine Teile.

:::abbildung prog/k1traceback 5
Ein Traceback, in seine Teile zerlegt (Linux; unter Windows steht in Zeile 2 der Windows-Pfad). Gelesen wird von unten: zuerst die Ausnahme (5), dann die Stelle (2 bis 4).
:::
::::

Man liest einen Traceback *von unten*: Die letzte Zeile sagt, was passiert ist, die Zeilen darüber sagen, wo. Bei längeren Programmen stehen über der Fehlerstelle weitere Ortszeilen, weil der Traceback den ganzen Weg bis zur Fehlerstelle nachzeichnet; die unterste Ortszeile ist immer die Stelle, an der die Ausnahme tatsächlich auftrat.

Die Markierung unter der Zeile gibt es seit Python 3.11. Betrifft der Fehler die ganze Zeile, lässt Python sie weg. Im interaktiven Modus steht statt eines Dateinamens `<python-input-0>`, gezählt ab der ersten Eingabe; in der einfacheren früheren Fassung des interaktiven Modus steht `<stdin>`:

```console
>>> 5 / 0
Traceback (most recent call last):
  File "<python-input-0>", line 1, in <module>
    5 / 0
    ~~^~~
ZeroDivisionError: division by zero
>>>
```

Nach dem Traceback wartet der interaktive Modus einfach auf die nächste Eingabe.

⁠**Kurz gesagt:** Ein Traceback nennt Ort und Art einer Ausnahme; man liest ihn von unten.

:::hintergrund Warum die wichtigste Zeile unten steht
Die Kopfzeile sagt es schon: *most recent call last*, der jüngste Schritt zuletzt. Ein Traceback ist chronologisch geordnet. Er beginnt dort, wo das Programm angefangen hat, und endet dort, wo es gescheitert ist. In den Programmen dieses Kapitels ist dieser Weg nur einen Schritt lang. Größere Programme bestehen aus Teilen, die einander aufrufen; dann listet der Traceback jeden Teil auf dem Weg zur Fehlerstelle, und die Liste wird lang. Für die Fehlersuche zählt aber fast immer zuerst das Ende des Weges. Deshalb liest man von unten.

Ein praktischer Nebeneffekt: Im Terminal scrollt die Ausgabe nach oben weg, die letzten Zeilen bleiben sichtbar. Bei einem langen Traceback steht das Wichtigste also genau dort, wo das Auge nach dem Programmende hinschaut.
:::

### Der Logikfehler

<span class="anker" id="stufe-6-5"></span>

Die gefährlichste Art von Fehler meldet Python überhaupt nicht.

**Das falsche Rezept.** Ein Koch befolgt ein Rezept, in dem „Salz“ statt „Zucker“ steht. Jeder Schritt ist lesbar und ausführbar; der Kuchen gelingt auch, er schmeckt nur nicht.

:::definition Definition 6.5 (Logikfehler)
<span class="anker" id="satz-6-5"></span>

Ein __Logikfehler__ ist ein Fehler, bei dem ein Programm ohne Fehlermeldung läuft, aber nicht das berechnet, was gemeint war.
:::

::::beispiel hin und zurück
Wer eine Strecke hin mit 60 km/h und zurück mit 40 km/h fährt, ist im Schnitt nicht 50 km/h schnell, sondern langsamer: Auf dem Rückweg ist man länger unterwegs, das langsame Tempo zählt also länger. Ist jede Richtung 120 km lang, dauert der Hinweg 2 Stunden und der Rückweg 3. Für 240 km braucht man dann 5 Stunden, im Schnitt also $240/5=48$ km/h. Allgemein gilt für das Durchschnittstempo $v=\frac{2v_1v_2}{v_1+v_2}$; darin ist $v_1$ das Tempo auf dem Hinweg und $v_2$ das auf dem Rückweg. Hier ergibt das $\frac{2\cdot60\cdot40}{60+40}=48$. Im folgenden Skript fehlen die Klammern um den Nenner:

```python schnitt.py
# Durchschnittstempo: hin mit 60 km/h, zurueck mit 40 km/h
# Formel: v = 2 * v1 * v2 / (v1 + v2)
print("Durchschnitt in km/h:", 2 * 60 * 40 / 60 + 40)
```

```console Linux
$ python3 schnitt.py
Durchschnitt in km/h: 120.0
```

Python rechnet nach seinen Regeln $2\cdot60\cdot40/60+40=80+40=120$ und hat damit recht; gemeint war etwas anderes. Der Durchschnitt muss zwischen den beiden Geschwindigkeiten liegen, also zwischen 40 und 60 km/h; 120 km/h kann nicht stimmen. Mit `2 * 60 * 40 / (60 + 40)` kommt `48.0` heraus.
::::

Weitere typische Logikfehler aus diesem Kapitel:

<ul>

<li>

ein Komma statt eines Punkts: `2,5 * 2` ergibt zwei Werte statt 5,0 (Unterabschnitt [4.4](der-interaktive-modus.html#stufe-4-4));

</li>

<li>

`^` statt `**`: `2 ^ 3` ergibt 1 statt 8;

</li>

<li>

eine falsche Einheit: Ein Preis in Euro wird mit „Cent“ beschriftet.

</li>

</ul>

**Was dagegen hilft.** Prüfe jedes Ergebnis mit einem Fall, dessen Antwort du kennst, oder mit einer Überschlagsrechnung. Für den Durchschnitt eignen sich zwei gleiche Geschwindigkeiten: Wer hin und zurück 50 km/h fährt, ist im Schnitt 50 km/h schnell. Die richtige Formel liefert 50, die falsche 150.

⁠**Kurz gesagt:** Ein Logikfehler läuft ohne Meldung und liefert ein falsches Ergebnis; man findet ihn nur, indem man Ergebnisse prüft.

:::hintergrund Warum kein Werkzeug alle Logikfehler finden kann
Python prüft beim Übersetzen die Form und beim Ausführen, ob sich jede Zeile ausführen lässt. Was der Verfasser gemeint hat, steht nirgends im Quelltext, also kann Python es auch nicht prüfen.

Dahinter steckt eine grundsätzliche Grenze. Die Informatik hat bewiesen, dass es kein Verfahren geben kann, das für jedes beliebige Programm entscheidet, ob sein Verhalten eine bestimmte Eigenschaft hat, die manche Programme haben und andere nicht, etwa „gibt immer die richtige Durchschnittsgeschwindigkeit aus“. Das ist der Satz von Rice aus dem Jahr 1953. Werkzeuge können viele typische Fehler finden, aber nie alle. Ergebnisse mit bekannten Fällen zu vergleichen, bleibt deshalb unverzichtbar.
:::

### Aufgaben zu Abschnitt [6](#stufe-6)

<span class="anker" id="stufe-6-6"></span>

:::aufgabe Aufgabe 16 ★ Einen Traceback lesen
<span class="anker" id="aufg-16"></span>

Ein Skript `strecke.py` hat folgende Ausgabe erzeugt:

```console Linux
$ python3 strecke.py
Tempo 18 km/h, Fahrzeit 2 h 30 min
Strecke in km: 45.0
Traceback (most recent call last):
  File "/home/student/python-kurs/strecke.py", line 4, in <module>
    print("Strecke in m:", Strecke * 1000)
                           ^^^^^^^
NameError: name 'Strecke' is not defined
```

<ol class="al">

<li>

Welche Art von Ausnahme ist aufgetreten, und in welcher Zeile?

</li>

<li>

Welche Zeilen des Skripts sind gelaufen? Woran erkennst du das?

</li>

<li>

Was hat der Verfasser vermutlich gemeint, und wie lautet die Zeile richtig, wenn die Strecke in Metern ausgegeben werden soll?

</li>

</ol>

:::loesung
(a) Ein `NameError` in Zeile 4 (`line 4` in der Ortszeile, die Art in der letzten Zeile).

(b) Die Zeilen 1 bis 3. Zeile 1 ist ein Kommentar und bewirkt nichts; die Ausgaben von Zeile 2 und 3 stehen vor dem Traceback. Zeile 4 ist die Fehlerstelle; sie hat nichts ausgegeben, weil Python den Ausdruck `Strecke * 1000` auswerten wollte, bevor es `print` aufruft.

(c) Gemeint war vermutlich die Strecke aus Zeile 3, 45 km. Der Name `Strecke` kommt aber nirgends vor; Python kennt ihn nicht. Richtig ist, den Ausdruck selbst hinzuschreiben, mit 2,5 Stunden für 2 h 30 min: `print("Strecke in m:", 18 * 2.5 * 1000)`. Dann erscheint `Strecke in m: 45000.0`.
:::
:::

:::aufgabe Aufgabe 17 ★★ Fehler vorhersagen
<span class="anker" id="aufg-17"></span>

Schreibe für jedes der drei Skripte auf, was es ausgibt, und ordne den Fehler einer der drei Arten zu. Prüfe danach am Rechner.

```python fehler_a.py
print("Start")
print("Liter pro km:", 45 / 750)
print("Ende)
```

```python fehler_b.py
print("Start")
print("Liter pro km:", 45 / 0)
print("Ende")
```

```python fehler_c.py
print("Start")
print("Liter pro 100 km:", 45 / 750)
print("Ende")
```

Achte bei `fehler_b.py` genau darauf, ob „Liter pro km:“ noch erscheint.

:::loesung
⁠**`fehler_a.py`** ist ein Syntaxfehler: In Zeile 3 wird die Zeichenkette nie geschlossen. Deshalb läuft keine Zeile, nicht einmal „Start“ erscheint:

```console Linux
$ python3 fehler_a.py
  File "/home/student/python-kurs/fehler_a.py", line 3
    print("Ende)
          ^
SyntaxError: unterminated string literal (detected at line 3)
```

⁠**`fehler_b.py`** ist ein Laufzeitfehler: Zeile 1 läuft, Zeile 2 bricht ab. „Liter pro km:“ erscheint *nicht*, denn Python wertet zuerst alle Werte in den Klammern aus, auch `45 / 0`, und erst danach würde `print` etwas schreiben. Die Markierung zeigt auf die Division:

```console Linux
$ python3 fehler_b.py
Start
Traceback (most recent call last):
  File "/home/student/python-kurs/fehler_b.py", line 2, in <module>
    print("Liter pro km:", 45 / 0)
                           ~~~^~~
ZeroDivisionError: division by zero
```

⁠**`fehler_c.py`** läuft ohne Meldung durch, enthält aber einen Logikfehler: `45 / 750` ist der Verbrauch für einen Kilometer, beschriftet ist er als Verbrauch für 100 Kilometer.

```console Linux
$ python3 fehler_c.py
Start
Liter pro 100 km: 0.06
Ende
```

Richtig wäre `print("Liter pro 100 km:", 45 / 750 * 100)` mit der Ausgabe `6.0`, oder die Beschriftung „Liter pro km:“. Unter Windows sind alle drei Ausgaben gleich; nur die Ortszeilen nennen den Windows-Pfad.
:::
:::

:::aufgabe Aufgabe 18 ★★ Einen Logikfehler finden
<span class="anker" id="aufg-18"></span>

Anna und Ben kaufen gemeinsam ein Los. Anna zahlt 1 €, Ben 2 €. Das Los gewinnt 12 €, und der Gewinn wird im Verhältnis der Einsätze geteilt: Bens Anteil ist der Gewinn mal Bens Einsatz geteilt durch die Summe beider Einsätze.

```python gewinn.py
# Gewinn 12 Euro; Einsatz: Anna 1 Euro, Ben 2 Euro
# Bens Anteil = Gewinn * Bens Einsatz / (Annas Einsatz + Bens Einsatz)
print("Bens Anteil in Euro:", 12 * 2 / 1 + 2)
```

<ol class="al">

<li>

Das Skript gibt `Bens Anteil in Euro: 26.0` aus. Woran erkennst du ohne Rechnung, dass das nicht stimmen kann?

</li>

<li>

Finde den Fehler und berichtige die Zeile.

</li>

<li>

Prüfe die berichtigte Formel mit einem Fall, dessen Ergebnis du kennst.

</li>

</ol>

:::loesung
(a) Ein Anteil kann nie größer sein als der ganze Gewinn, hier 12 €. 26 € für Ben ist also unmöglich.

(b) Um den Nenner fehlen Klammern. Python rechnet $12\cdot2/1+2=24+2=26$. Richtig:

```python
print("Bens Anteil in Euro:", 12 * 2 / (1 + 2))
```

Ausgabe: `Bens Anteil in Euro: 8.0`. Ben bekommt 8 €, Anna die übrigen 4 €; das passt, denn Ben hat doppelt so viel eingezahlt.

(c) Bei gleichen Einsätzen muss jeder genau die Hälfte bekommen: `12 * 1 / (1 + 1)` ergibt `6.0`. Ein zweiter bekannter Fall: Zahlt Ben viel mehr als Anna, bekommt er fast den ganzen Gewinn; zahlt er nichts, bekommt er nichts.
:::
:::

:::aufgabe Aufgabe 19 ★★★ Den Bytecode beobachten
<span class="anker" id="aufg-19"></span>

Python bringt ein Werkzeug mit, das den Bytecode einer Datei anzeigt, ohne sie auszuführen. Man ruft es im Terminal mit `py -m dis` beziehungsweise `python3 -m dis` und dem Dateinamen auf. Speichere dazu dieses Skript:

```python rechnung.py
# Dieser Kommentar ist nur fuer Menschen da.
print(2 + 3)
print(5 / 0)
```

<ol class="al">

<li>

Lass dir den Bytecode anzeigen: `python3 -m dis rechnung.py` (Linux) oder `py -m dis rechnung.py` (Windows). Jede Gruppe von Befehlen beginnt mit der Nummer der Quelltextzeile, aus der sie stammt. Findest du den Kommentar wieder?

</li>

<li>

Suche die Befehle zu Zeile 2. Steht dort noch eine Addition, oder schon die Zahl 5?

</li>

<li>

Suche die Befehle zu Zeile 3. Ist `5 / 0` vorab ausgerechnet? Erkläre mit dem Hintergrund-Kasten in Unterabschnitt [6.2](#stufe-6-2), warum.

</li>

<li>

Führe das Skript danach aus. Was erscheint, bevor der Traceback kommt?

</li>

</ol>

Die Befehlsnamen hängen von der Python-Version ab; die Beobachtungen nicht.

:::loesung
Die Ausgaben auf den beiden Testrechnern:

```console Windows (PowerShell), Python 3.13
PS> py -m dis rechnung.py
  0           RESUME                   0

  2           LOAD_NAME                0 (print)
              PUSH_NULL
              LOAD_CONST               0 (5)
              CALL                     1
              POP_TOP

  3           LOAD_NAME                0 (print)
              PUSH_NULL
              LOAD_CONST               0 (5)
              LOAD_CONST               1 (0)
              BINARY_OP               11 (/)
              CALL                     1
              POP_TOP
              RETURN_CONST             2 (None)
```

```console Linux, Python 3.14
$ python3 -m dis rechnung.py
  0           RESUME                   0

  2           LOAD_NAME                0 (print)
              PUSH_NULL
              LOAD_SMALL_INT           5
              CALL                     1
              POP_TOP

  3           LOAD_NAME                0 (print)
              PUSH_NULL
              LOAD_SMALL_INT           5
              LOAD_SMALL_INT           0
              BINARY_OP               11 (/)
              CALL                     1
              POP_TOP
              LOAD_CONST               1 (None)
              RETURN_VALUE
```

(a) Zu Zeile 1 gibt es keine Befehle; der Kommentar ist beim Übersetzen verschwunden. Die erste Gruppe nach dem Startbefehl `RESUME` beginnt mit der Zeilennummer 2.

(b) In Zeile 2 gibt es keine Addition. Der Übersetzer hat `2 + 3` schon ausgerechnet: Python 3.13 lädt die fertige Zahl mit `LOAD_CONST 0 (5)`, Python 3.14 mit `LOAD_SMALL_INT 5`. Danach folgt der Aufruf von `print` (`CALL`).

(c) In Zeile 3 werden 5 und 0 einzeln geladen, danach folgt `BINARY_OP 11 (/)`: Die Division findet erst beim Ausführen statt. Der Übersetzer rechnet vorab nur, was gelingt. Würde er `5 / 0` schon beim Übersetzen ausrechnen, träte der Fehler auf, bevor Zeile 2 läuft. Die Semantik verlangt aber, dass der Fehler genau beim Ausführen von Zeile 3 auftritt und alles davor gelaufen ist.

(d) Zuerst erscheint `5` aus Zeile 2, dann der Traceback mit `ZeroDivisionError` in Zeile 3:

```console Linux
$ python3 rechnung.py
5
Traceback (most recent call last):
  File "/home/student/python-kurs/rechnung.py", line 3, in <module>
    print(5 / 0)
          ~~^~~
ZeroDivisionError: division by zero
```

Dass sich die Befehlsnamen der beiden Versionen unterscheiden (`LOAD_CONST` gegenüber `LOAD_SMALL_INT`, `RETURN_CONST` gegenüber `LOAD_CONST` und `RETURN_VALUE`), zeigt, dass der Bytecode ein inneres Werkzeug von CPython ist, das sich mit jeder Version ändern darf.
:::
:::

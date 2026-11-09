---
title: Skripte schreiben und ausführen
pfad: Informatik / Programmieren / Python / Programme und der Python-Interpreter
knoten: Python 1: Programme und der Python-Interpreter
order: 6020600
summary: Was man im interaktiven Modus eintippt, ist nach dem Beenden verloren.
tags: Editor, Skript, Kommentar
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Was man im interaktiven Modus eintippt, ist nach dem Beenden verloren. Dieser Abschnitt zeigt, wie man ein Programm in einer Datei speichert, mit welchem Werkzeug man diese Datei schreibt und wie man sie ausführt.
:::

### Der Editor

<span class="anker" id="stufe-5-1"></span>

Ein Programm in einer Datei zu speichern, verlangt ein Programm, mit dem man reinen Text schreibt und speichert, ohne dass etwas hinzugefügt wird.

**Reiner Text.** Eine Programmdatei darf nur die Zeichen enthalten, die man tippt. Ein Textverarbeitungsprogramm wie Word speichert dagegen zusätzlich Schriftarten, Seitenränder und Absatzformate, und es ersetzt beim Tippen gerade Anführungszeichen durch typografische. Python erkennt typografische Anführungszeichen aber nicht als Anfang oder Ende einer Zeichenkette. Für Programme ist ein Textverarbeitungsprogramm deshalb ungeeignet.

:::definition Definition 5.1 (Editor)
<span class="anker" id="satz-5-1"></span>

Ein __Editor__ ist ein Programm, mit dem man reine Textdateien schreibt und speichert. Ein Editor für Programmierer hilft zusätzlich beim Schreiben von Quelltext: Er färbt ihn nach seiner Syntax ein, markiert Verstöße gegen die Syntax schon beim Tippen und kann ein Programm auf Knopfdruck ausführen.
:::

::::beispiel zwei Editoren für dieses Kapitel
<ul>

<li>

⁠**Visual Studio Code** (kurz VS Code) ist ein kostenloser Editor für Windows und Linux, den man auf `code.visualstudio.com` bekommt. Unter Ubuntu installiert man ihn alternativ mit `sudo snap install --classic code`. Nach dem ersten Start installiert man über das Erweiterungen-Symbol am linken Rand die Erweiterung „Python“ von Microsoft. Sie bringt die Einfärbung, die Fehlermarkierung und den Knopf zum Ausführen mit; Python selbst enthält sie nicht.

</li>

<li>

⁠**IDLE** ist ein einfacher Editor, der zu Python gehört. Unter Windows richtet der Python install manager im Startmenü den Eintrag „IDLE (Python 3.14)“ ein, passend zur installierten Version. Unter Ubuntu installiert man ihn mit `sudo apt install idle` und startet ihn mit dem Befehl `idle`. Ein neues Programm beginnt man mit „File“, „New File“.

</li>

</ul>

Lege für die Programme dieses Kapitels einen Ordner `python-kurs` in deinem persönlichen Ordner an und speichere alle Dateien dort. In VS Code öffnest du diesen Ordner mit „File“, „Open Folder“ (mit deutschem Sprachpaket „Datei“, „Ordner öffnen“); neue Dateien legst du dann darin an.
::::

Unter Windows blendet der Explorer Dateiendungen oft aus. Schalte sie ein („Anzeigen“, „Einblenden“, „Dateinamenerweiterungen“), damit du siehst, ob eine Datei wirklich `hallo.py` heißt und nicht `hallo.py.txt`.

⁠**Kurz gesagt:** Programme schreibt man mit einem Editor, der reinen Text speichert, am besten mit einem Editor für Programmierer wie VS Code oder IDLE.

:::hintergrund Woher ein Editor für Programmierer die Syntax kennt
Ein Editor für Programmierer liest den Quelltext beim Tippen ständig mit und zerlegt ihn so, wie es auch der Übersetzer von CPython in seiner ersten Phase tut (Unterabschnitt [2.4](vom-quelltext-zur-ausfuhrung-compiler-und-interpreter.html#stufe-2-4)): in Zahlen, Rechenzeichen, Klammern, Zeichenketten und Namen. Jede Art von Bestandteil bekommt ihre eigene Farbe; eine Zeichenkette, die nie geschlossen wird, färbt deshalb sichtbar den Rest der Zeile mit ein. Danach prüft er die Bestandteile gegen die Grammatik der Sprache und unterstreicht jede Stelle, an der sie verletzt ist. Diese Prüfung ist dieselbe Art von Prüfung, die CPython vor dem Ausführen macht; der Editor macht sie nur früher, nämlich schon beim Schreiben. Was beim Ausführen passieren wird, kann er dagegen nicht vollständig vorhersehen.
:::

### Das Skript

<span class="anker" id="stufe-5-2"></span>

Mit einem Editor kann man den Quelltext eines Programms in eine Datei schreiben und so oft ausführen, wie man will.

:::definition Definition 5.2 (Skript)
<span class="anker" id="satz-5-2"></span>

Ein __Skript__ ist eine Textdatei mit Python-Quelltext, deren Name auf `.py` endet. Python führt ein Skript aus, indem es die Datei übersetzt und ihre Zeilen dann von oben nach unten je einmal ausführt.
:::

**Ordner vorbereiten.** Zwei Befehle genügen, und sie heißen unter Windows und Linux gleich: `mkdir python-kurs` legt den Ordner `python-kurs` an, `cd python-kurs` wechselt im Terminal hinein. Ein neu geöffnetes Terminal steht im persönlichen Ordner; dort wird der Ordner angelegt. Hast du ihn schon im Editor angelegt, entfällt `mkdir`. Ausführlich: Linux 2.

::::beispiel
Schreibe im Editor diese drei Zeilen und speichere sie als `hallo.py` im Ordner `python-kurs`:

```python hallo.py
print("Hallo, Welt!")
print(2 + 3)
print("2 + 3")
```

Im Terminal wechselst du in den Ordner und startest das Skript, indem du hinter `py` beziehungsweise `python3` den Dateinamen schreibst:

```console Windows (PowerShell)
PS> cd python-kurs
PS> py hallo.py
Hallo, Welt!
5
2 + 3
```

```console Linux
$ cd python-kurs
$ python3 hallo.py
Hallo, Welt!
5
2 + 3
```

Python übersetzt die Datei, führt die drei Zeilen der Reihe nach aus und endet; danach steht wieder die Eingabeaufforderung des Terminals da. Die zweite Zeile gibt den Wert von `2 + 3` aus, die dritte die Zeichenkette `"2 + 3"` wörtlich. In VS Code führt der Knopf mit dem Dreieck oben rechts („Run Python File“) denselben Befehl im Terminal unten im Fenster aus.
::::

**Im Skript zeigt nur `print` etwas an.** Den wichtigsten Unterschied zum interaktiven Modus zeigt dieses Skript:

```python ausdruck.py
print("Vorher")
2 + 3
print("Nachher")
```

```console Linux
$ python3 ausdruck.py
Vorher
Nachher
```

Die Zeile `2 + 3` wird ausgeführt, aber ihr Wert erscheint nirgends. Im interaktiven Modus hätte dieselbe Zeile `5` angezeigt. In einem Skript erscheint nur, was ein Aufruf von `print` ausgibt. Abbildung [3](#abb-3) stellt beide Arbeitsweisen nebeneinander. Unter Windows sieht die Ausgabe genauso aus.

:::abbildung prog/k1modi 3
Zwei Arbeitsweisen. Links der interaktive Modus: Er liest eine Eingabe, wertet sie aus, zeigt den Wert an und beginnt von vorn. Rechts ein Skript: Python übersetzt die ganze Datei und führt dann die Zeilen nacheinander aus; sichtbar wird nur, was `print` ausgibt.
:::

⁠**Kurz gesagt:** Ein Skript ist eine `.py`-Datei, die man mit `py datei.py` oder `python3 datei.py` ausführt; sichtbar wird darin nur, was `print` ausgibt.

:::hintergrund Warum ein Skript die Werte seiner Zeilen nicht anzeigt
Die Regel steht so in der Sprachreferenz von Python: Ist eine Zeile nur ein Ausdruck, wird im interaktiven Modus ihr Wert angezeigt, im Skript wird er ausgerechnet und verworfen. Technisch übersetzt der interaktive Modus jede Eingabe in einer eigenen Betriebsart, die am Ende einen Befehl „Wert anzeigen“ anhängt; beim Übersetzen eines Skripts fehlt dieser Befehl. Bei `2 + 3` geht der Übersetzer sogar noch weiter: Er rechnet die Zeile vorab aus, erkennt, dass ihr Wert nirgends gebraucht wird, und lässt sie im Bytecode ganz weg.

Der Grund für die Regel ist praktisch. Ein Programm soll genau das ausgeben, was sein Verfasser will. Würde ein Skript mit hundert Rechenzeilen jedes Zwischenergebnis anzeigen, ginge das eigentliche Ergebnis darin unter. Beim Ausprobieren im interaktiven Modus will man dagegen jeden Wert sofort sehen.
:::

### Der Kommentar

<span class="anker" id="stufe-5-3"></span>

Ein Skript liest man öfter, als man es schreibt, und nach ein paar Wochen weiß man selbst nicht mehr, was `(9 - 2) / 0.02` bedeuten sollte. Man braucht Platz für Erklärungen, die Python nicht stören.

:::definition Definition 5.3 (Kommentar)
<span class="anker" id="satz-5-3"></span>

Ein __Kommentar__ beginnt mit dem Zeichen `#` und reicht bis zum Ende der Zeile. Python überliest ihn vollständig.
:::

::::beispiel ein LED-Vorwiderstand
Eine rote Leuchtdiode an einer 9-V-Batterie braucht etwa 2 V und soll 20 mA bekommen. Am Vorwiderstand liegen dann $9\,\mathrm V-2\,\mathrm V=7\,\mathrm V$:

```python led.py
# Vorwiderstand einer roten LED an einer 9-V-Batterie
# Annahmen: Die LED braucht 2 V und soll 20 mA bekommen.
# Am Widerstand liegen also 9 V - 2 V = 7 V.
print("Vorwiderstand in Ohm:", (9 - 2) / 0.02)        # R = U / I
print("Leistung im Widerstand in W:", (9 - 2) * 0.02)  # P = U * I
```

```console Linux
$ python3 led.py
Vorwiderstand in Ohm: 350.0
Leistung im Widerstand in W: 0.14
```

Unter Windows (`py led.py`) erscheint dieselbe Ausgabe. Die ersten drei Zeilen sind ganz Kommentar. In den letzten beiden steht der Kommentar hinter der Anweisung: Python führt den Aufruf von `print` aus und überliest den Rest der Zeile ab `#`.
::::

Gute Kommentare sagen, was eine Zahl bedeutet und warum gerechnet wird, nicht was ohnehin dasteht. Im Beispiel nennen sie die Annahmen und die Einheiten, denn die kennt Python nicht. Man kann mit einem `#` am Zeilenanfang auch eine Zeile vorübergehend abschalten, ohne sie zu löschen.

⁠**Kurz gesagt:** Ein Kommentar beginnt mit `#`, gilt bis zum Zeilenende und ist nur für Menschen da.

:::hintergrund Wo der Kommentar bleibt
Beim Übersetzen zerlegt CPython den Quelltext zuerst in seine kleinsten Bestandteile: Zahlen, Namen, Rechenzeichen, Klammern, Zeichenketten. Ein Kommentar wird schon in diesem allerersten Schritt weggeworfen. Im Bytecode kommt er nicht mehr vor, und beim Ausführen kostet er deshalb keine Zeit, so lang er auch ist.

Ein `#` innerhalb einer Zeichenkette beginnt keinen Kommentar, denn dort gehört es zum Text: `print("Nr. # 5")` gibt `Nr. # 5` aus.
:::

### Aufgaben zu Abschnitt [5](#stufe-5)

<span class="anker" id="stufe-5-4"></span>

:::aufgabe Aufgabe 13 ★ Das erste Skript
<span class="anker" id="aufg-13"></span>

Schreibe mit einem Editor das Skript `hallo.py` aus Unterabschnitt [5.2](#stufe-5-2) und füge als vierte Zeile `7 * 6` hinzu.

<ol class="al">

<li>

Schreibe auf, was das Skript ausgeben wird, bevor du es startest.

</li>

<li>

Starte es im Terminal und vergleiche.

</li>

<li>

Ändere die vierte Zeile so, dass auch ihr Wert erscheint.

</li>

</ol>

:::loesung
(a) und (b) Das Skript gibt drei Zeilen aus; die vierte Zeile `7 * 6` wird ausgerechnet, ihr Wert erscheint aber nicht, denn in einem Skript zeigt nur `print` etwas an:

```console Linux
$ python3 hallo.py
Hallo, Welt!
5
2 + 3
```

Unter Windows (`py hallo.py`) ist die Ausgabe dieselbe.

(c) Die vierte Zeile muss `print(7 * 6)` heißen; dann erscheint zusätzlich `42`.
:::
:::

:::aufgabe Aufgabe 14 ★★ Eine LED an 12 V
<span class="anker" id="aufg-14"></span>

Schreibe nach dem Vorbild von `led.py` ein Skript `led12.py` für eine LED mit 2 V und 20 mA an einer 12-V-Versorgung. Es soll den Vorwiderstand in Ohm und die Leistung im Widerstand in Watt ausgeben. Kommentiere die Annahmen und die Formeln. Rechne das Ergebnis zur Probe im Kopf nach.

:::loesung
```python led12.py
# Vorwiderstand einer LED an 12 V
# Annahmen: Die LED braucht 2 V und soll 20 mA bekommen.
# Am Widerstand liegen also 12 V - 2 V = 10 V.
print("Vorwiderstand in Ohm:", (12 - 2) / 0.02)        # R = U / I
print("Leistung im Widerstand in W:", (12 - 2) * 0.02)  # P = U * I
```

```console Linux
$ python3 led12.py
Vorwiderstand in Ohm: 500.0
Leistung im Widerstand in W: 0.2
```

Probe im Kopf: $10\,\mathrm V/0{,}02\,\mathrm A=500\,\Omega$ und $10\,\mathrm V\cdot0{,}02\,\mathrm A=0{,}2\,\mathrm W$. Ein üblicher Widerstand mit $0{,}25\,\mathrm W$ Belastbarkeit hält das aus, aber nur knapp. Unter Windows ist die Ausgabe dieselbe.
:::
:::

:::aufgabe Aufgabe 15 ★★ Vom interaktiven Modus zum Skript
<span class="anker" id="aufg-15"></span>

Jemand hat im interaktiven Modus gerechnet:

```console
>>> 9 / 1500
0.006
>>> _ * 1000
6.0
>>> 9 ** 2 / 1500
0.054
```

Schreibe ein Skript `batterie.py`, das dieselben drei Ergebnisse mit erklärendem Text ausgibt, etwa `Strom in A: 0.006`. Warum kannst du `_` dabei nicht benutzen? Ersetze es durch einen Ausdruck, der ohne `_` auskommt.

:::loesung
```python batterie.py
# Widerstand von 1,5 kOhm an einer 9-V-Batterie
print("Strom in A:", 9 / 1500)             # I = U / R
print("Strom in mA:", 9 / 1500 * 1000)
print("Leistung in W:", 9 ** 2 / 1500)     # P = U^2 / R
```

```console Linux
$ python3 batterie.py
Strom in A: 0.006
Strom in mA: 6.0
Leistung in W: 0.054
```

Unter Windows ist die Ausgabe dieselbe. Das Zeichen `_` merkt sich nur der interaktive Modus; in einem Skript gibt es kein „zuletzt angezeigtes Ergebnis“, weil ein Skript Werte gar nicht anzeigt. Schreibt man trotzdem `print("Strom in mA:", _ * 1000)` in ein Skript, bricht es mit `NameError: name '_' is not defined` ab. Deshalb steht in der zweiten Zeile der ganze Ausdruck `9 / 1500 * 1000`.
:::
:::

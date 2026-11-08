---
title: Vom Quelltext zur Ausführung: Compiler und Interpreter
pfad: Informatik / Programmieren / Python / Programme und der Python-Interpreter
knoten: Python 1: Programme und der Python-Interpreter
order: 6020300
summary: Der Prozessor versteht nur Maschinencode, Menschen schreiben Quelltext.
tags: Compiler, ausführbare Datei, Interpreter, Python, CPython, Bytecode, Interpreterschleife
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Der Prozessor versteht nur Maschinencode, Menschen schreiben Quelltext. Dieser Abschnitt zeigt die zwei grundsätzlichen Wege, diese Lücke zu schließen, und welchen Weg Python geht.
:::

### Der Compiler

<span class="anker" id="stufe-2-1"></span>

Quelltext muss in Maschinencode übersetzt werden. Das kann ein Programm übernehmen.

**Ein Buchübersetzer.** Ein Buch wird einmal vollständig übersetzt, dann gedruckt und verkauft. Die Leser der Übersetzung brauchen den Übersetzer nicht mehr; sie halten ein fertiges Buch in der Hand.

:::definition Definition 2.1 (Compiler)
<span class="anker" id="satz-2-1"></span>

Ein __Compiler__ ist ein Programm, das einen Quelltext vollständig in Maschinencode übersetzt, bevor dieser ausgeführt wird. Das Ergebnis wird als eigene Datei gespeichert, die ohne den Compiler läuft.
:::

Eine solche Datei heißt __ausführbare Datei__. Unter Windows endet ihr Name meist auf `.exe`.

**Beispiel.** Programme in der Sprache C werden so übersetzt. Aus dem Quelltext `hallo.c` macht der Compiler `gcc` die ausführbare Datei `hallo.exe` (Windows) oder `hallo` (Linux). Diese Datei startet man danach direkt, beliebig oft und ohne den Compiler. Sie enthält Maschinencode für eine bestimmte Prozessorfamilie und ein bestimmtes Betriebssystem; für einen anderen Rechner muss man neu übersetzen.

⁠**Kurz gesagt:** Ein Compiler übersetzt den ganzen Quelltext einmal vorab in eine ausführbare Datei aus Maschinencode.

### Der Interpreter

<span class="anker" id="stufe-2-2"></span>

Es geht auch ohne ausführbare Datei: Ein Programm kann den Quelltext lesen und selbst tun, was darin steht.

**Ein Dolmetscher.** Bei einem Gespräch zwischen zwei Sprachen sitzt ein Dolmetscher dabei und übersetzt, während gesprochen wird. Es entsteht kein schriftliches Ergebnis; beim nächsten Gespräch muss er wieder dabei sein. (Das Bild trifft die Rolle des Interpreters, nicht jede Einzelheit seiner Arbeitsweise.)

:::definition Definition 2.2 (Interpreter)
<span class="anker" id="satz-2-2"></span>

Ein __Interpreter__ ist ein Programm, das einen Quelltext liest und die darin beschriebenen Schritte selbst ausführt. Er erzeugt keine ausführbare Datei und muss deshalb bei jedem Start des Programms dabei sein.
:::

**Beispiel.** Python-Programme laufen so. Den Quelltext `hallo.py` startet man mit einem Befehl wie `python hallo.py`. Das Programm `python` ist der Interpreter: Es liest die Datei und führt aus, was darin steht. Der Prozessor führt dabei die ganze Zeit den Maschinencode des Interpreters aus, nie den Python-Quelltext selbst.

Die beiden Wege im Vergleich:

|  | Compiler | Interpreter |
|---|---|---|
| übersetzt wird | einmal, vor allen Starts | bei jedem Start |
| Ergebnis | ausführbare Datei | keine Datei, nur die Wirkung |
| weitergeben | die ausführbare Datei | den Quelltext; der Empfänger braucht den Interpreter |
| läuft auf | der Prozessorfamilie und dem Betriebssystem, für die übersetzt wurde | jedem Rechner, für den es den Interpreter gibt |
| Tempo | schnell | langsamer, weil der Interpreter bei jedem Schritt mitarbeitet |

⁠**Kurz gesagt:** Ein Interpreter führt den Quelltext selbst aus, ohne eine ausführbare Datei zu erzeugen.

:::hintergrund Warum Python einen Interpreter benutzt
Ein Interpreter hat zwei Vorteile, die für Python den Ausschlag geben. Man kann eine Zeile eintippen und sieht sofort, was sie bewirkt, ohne Übersetzungsschritt dazwischen. Und derselbe Quelltext läuft unverändert unter Windows, Linux und macOS, auf PC-Prozessoren wie auf einem Raspberry Pi; nur den Interpreter selbst muss es für jedes System geben.

Der Preis ist Tempo. Der Interpreter muss bei jedem Schritt erst selbst Arbeit leisten, bevor die eigentliche Rechnung geschieht. Rechenintensive Programme schreibt man deshalb oft so, dass die schweren Teile in fertigem, übersetztem Maschinencode laufen, den Python nur aufruft.
:::

### Python und CPython

<span class="anker" id="stufe-2-3"></span>

Das Wort „Python“ bezeichnet zwei verschiedene Dinge: eine Sprache und ein Programm.

:::definition Definition 2.3 (Python und CPython)
<span class="anker" id="satz-2-3"></span>

__Python__ ist eine Programmiersprache; ihre Syntax und Semantik sind in der Sprachreferenz von Python festgelegt. __CPython__ ist das Programm, das Python-Quelltext ausführt und auf `python.org` angeboten wird; es ist selbst in der Sprache C geschrieben.
:::

CPython ist das ursprüngliche und mit Abstand meistbenutzte Programm dieser Art. Neue Sprachmittel erscheinen meist zuerst dort.

**Beispiel.** Es gibt weitere Programme, die Python-Quelltext ausführen, etwa PyPy, das viele Programme schneller abarbeitet. Sie halten sich an dieselbe Sprachreferenz, also an dieselbe Syntax und Semantik. In dieser Reihe ist mit dem Programm `python` immer CPython gemeint.

⁠**Kurz gesagt:** Python ist die Sprache, CPython das Programm, das sie ausführt.

### Der Bytecode

<span class="anker" id="stufe-2-4"></span>

CPython ist ein Interpreter, liest den Quelltext aber nicht Zeile für Zeile wie ein Dolmetscher. Es arbeitet in zwei Phasen.

**Ein Koch mit Karteikarten.** Ein Koch liest zuerst das ganze Rezept durch und schreibt jeden Schritt in seiner eigenen Kurzschrift auf Karteikarten. Findet er dabei einen unleserlichen Satz, fängt er gar nicht erst an. Erst wenn alle Karten fertig sind, arbeitet er sie der Reihe nach ab. (Ein Bild; was „Karten“ und „Kurzschrift“ bei CPython sind, folgt jetzt.)

:::definition Definition 2.4 (Bytecode)
<span class="anker" id="satz-2-4"></span>

Der __Bytecode__ ist eine Folge einfacher Befehle, in die CPython den ganzen Quelltext übersetzt, bevor es mit der Ausführung beginnt. Die Befehle sind für eine gedachte Maschine entworfen, nicht für einen wirklichen Prozessor.
:::

Den Bytecode arbeitet anschließend ein Teil von CPython Befehl für Befehl ab: die __Interpreterschleife__.

Ein Python-Programm läuft also so ab (Abbildung [2](#abb-2), links):

<ol>

<li>

⁠**Übersetzen.** CPython liest die ganze Datei, prüft ihre Syntax und erzeugt daraus Bytecode. Dabei wird noch nichts ausgeführt.

</li>

<li>

⁠**Ausführen.** Die Interpreterschleife nimmt einen Bytecode-Befehl nach dem anderen. Für jeden Befehl führt der Prozessor ein Stück Maschinencode aus, das in CPython steckt und genau diesen Befehl umsetzt.

</li>

</ol>

Für ein Programm, das du startest, legt CPython den Bytecode nur im Arbeitsspeicher an. Eine ausführbare Datei entsteht nicht. Das Bild vom Dolmetscher aus Unterabschnitt [2.2](#stufe-2-2) stimmt also nur zur Hälfte: CPython übersetzt erst die ganze Datei und führt dann aus.

:::abbildung prog/k1wege 2
Zwei Wege vom Quelltext zur Ausführung. Links Python: Das Programm `python` (CPython) übersetzt bei jedem Start die ganze Datei in Bytecode und arbeitet diesen danach in seiner Interpreterschleife ab. Rechts C: Der Compiler übersetzt einmal vorab in eine ausführbare Datei, die der Prozessor danach ohne Compiler ausführt.
:::

**Beispiel.** Aus der Zeile `(1 + 2 / 1) / 2` entstehen Bytecode-Befehle der Art „lege die Zahl 1 bereit“, „teile“, „addiere“. Der Übersetzer geht dabei sogar einen Schritt weiter: Einen Ausdruck, der nur aus festen Zahlen besteht, rechnet er schon beim Übersetzen aus. Im Bytecode steht dann gleich die Zahl 1,5, und beim Ausführen ist nichts mehr zu rechnen. Wie der Bytecode genau aussieht, hängt von der Python-Version ab; er ist ein inneres Werkzeug von CPython und kann sich mit jeder neuen Version ändern.

Eine Folge der zwei Phasen ist für die Praxis wichtig: Verstößt irgendeine Stelle der Datei gegen die Syntax, entsteht gar kein Bytecode. Dann läuft keine einzige Zeile, auch nicht die erste.

⁠**Kurz gesagt:** CPython übersetzt die ganze Datei zuerst in Bytecode und führt danach diesen Bytecode Befehl für Befehl aus.

:::hintergrund Warum CPython den Umweg über Bytecode nimmt
Einen Text zu zerlegen und auf seine Syntax zu prüfen, ist aufwendig. Würde CPython den Text bei jedem Schritt neu lesen, müsste es dieselbe Zeile tausendmal zerlegen, wenn sie tausendmal ausgeführt wird. Mit Bytecode geschieht das Zerlegen einmal am Anfang. Die Bytecode-Befehle sind danach einfach und gleichförmig, und die Interpreterschleife kann jeden von ihnen schnell erkennen und ausführen.

Dazu kommt, dass der Bytecode auf allen Prozessoren gleich ist. Nur CPython selbst muss für jede Prozessorfamilie und jedes Betriebssystem einmal mit einem Compiler übersetzt werden; danach führt es überall denselben Bytecode aus. Deshalb sagt man, Python werde interpretiert, obwohl darin ein kleiner Übersetzer steckt. Die Grenze zwischen „übersetzt“ und „interpretiert“ ist bei Python fließend.
:::

:::hintergrund Die Interpreterschleife spielt Prozessor
Die Interpreterschleife ist im Kern eine einzige Schleife im C-Quelltext von CPython: nächsten Bytecode-Befehl holen, nachsehen, welcher Befehl es ist, das passende Stück Maschinencode ausführen, wieder von vorn. Das ist derselbe Kreislauf, den der Prozessor mit seinen Maschinenbefehlen abarbeitet: holen, entschlüsseln, ausführen (Unterabschnitt [1.2](programme-und-programmiersprachen.html#stufe-1-2)). Deshalb spricht man von einer gedachten oder *virtuellen* Maschine: CPython spielt in Software einen Prozessor, dessen Befehle der Bytecode sind.
:::

### Aufgaben zu Abschnitt [2](#stufe-2)

<span class="anker" id="stufe-2-5"></span>

:::aufgabe Aufgabe 4 ★ Compiler, Interpreter oder CPython?
<span class="anker" id="aufg-4"></span>

Für welche der drei Programmarten gilt die Aussage: einen Compiler wie `gcc`, einen Interpreter, der wie ein Dolmetscher Zeile für Zeile übersetzt und sofort ausführt, oder CPython? Mehrere Antworten sind möglich.

<ol class="al">

<li>

Es entsteht eine Datei, die ohne das übersetzende Programm läuft.

</li>

<li>

Das Programm muss bei jedem Start dabei sein.

</li>

<li>

Der ganze Quelltext wird übersetzt, bevor die erste Anweisung ausgeführt wird.

</li>

<li>

Der Prozessor führt die Übersetzung des Quelltexts unmittelbar aus.

</li>

</ol>

:::loesung
(a) Nur der Compiler: Er erzeugt eine ausführbare Datei. CPython legt den Bytecode nur im Arbeitsspeicher an, der Dolmetscher-Interpreter erzeugt gar kein Übersetzungsergebnis.

(b) Der Dolmetscher-Interpreter und CPython. Beide führen das Programm selbst aus und müssen deshalb bei jedem Start dabei sein.

(c) Der Compiler und CPython. CPython übersetzt in seiner ersten Phase die ganze Datei in Bytecode, bevor die erste Zeile läuft. Nur der Dolmetscher-Interpreter übersetzt jede Zeile erst, wenn er bei ihr ankommt.

(d) Nur der Compiler: Seine ausführbare Datei enthält Maschinencode, den der Prozessor unmittelbar ausführt. Den Bytecode von CPython führt nicht der Prozessor aus, sondern die Interpreterschleife; der Prozessor führt dabei den Maschinencode von CPython aus.
:::
:::

:::aufgabe Aufgabe 5 ★★ Programme weitergeben
<span class="anker" id="aufg-5"></span>

Du hast unter Windows zwei kleine Programme geschrieben, die dasselbe tun: `rechner.c` in C, daraus mit dem Compiler `rechner.exe` erzeugt, und `rechner.py` in Python. Eine Freundin benutzt Linux und hat Python installiert, aber keinen C-Compiler.

<ol class="al">

<li>

Kann sie `rechner.exe` starten? Begründe.

</li>

<li>

Kann sie `rechner.py` ausführen? Was braucht sie dafür?

</li>

<li>

Was müsste sie tun, um das C-Programm zu benutzen?

</li>

</ol>

:::loesung
(a) Nein. `rechner.exe` ist eine ausführbare Datei für Windows. Sie hat das Dateiformat von Windows und benutzt Dienste von Windows; ein Linux-System kann sie nicht direkt starten, selbst wenn der Prozessor derselben Familie angehört.

(b) Ja. Sie braucht nur einen Python-Interpreter, den sie hat, in einer Version, die alle benutzten Sprachmittel kennt. Sie startet das Programm mit `python3 rechner.py`. Der Quelltext ist für alle Systeme derselbe.

(c) Sie braucht den Quelltext `rechner.c` und einen C-Compiler für Linux, zum Beispiel `gcc`. Damit übersetzt sie den Quelltext auf ihrem Rechner neu und startet die entstandene ausführbare Datei. Die Datei `rechner.exe` hilft ihr dabei nicht.
:::
:::

:::aufgabe Aufgabe 6 ★★ Wann fällt der Fehler auf?
<span class="anker" id="aufg-6"></span>

Ein Python-Programm hat 1000 Zeilen. In Zeile 1000 fehlt eine schließende Klammer, alle anderen Zeilen sind in Ordnung.

<ol class="al">

<li>

Wie viele Zeilen führt CPython aus, bevor es den Fehler meldet? Begründe mit den zwei Phasen.

</li>

<li>

Wie viele Zeilen würde ein Interpreter ausführen, der wirklich wie ein Dolmetscher arbeitet, also jede Zeile erst übersetzt, wenn er bei ihr ankommt?

</li>

<li>

Welches Verhalten ist dir lieber, wenn das Programm in Zeile 500 eine Datei überschreibt? Warum?

</li>

</ol>

:::loesung
(a) Keine einzige. CPython übersetzt in der ersten Phase die ganze Datei. Der Syntaxfehler in Zeile 1000 verhindert, dass Bytecode entsteht, und ohne Bytecode beginnt die zweite Phase nicht. Die Meldung erscheint, bevor Zeile 1 läuft.

(b) 999 Zeilen. Ein solcher Interpreter merkt den Fehler erst, wenn er bei Zeile 1000 ankommt; alles davor hat er schon ausgeführt.

(c) Das Verhalten von CPython. Bei einem Dolmetscher-Interpreter wäre die Datei in Zeile 500 schon überschrieben, wenn das Programm in Zeile 1000 abbricht: Es bliebe ein halb erledigter Zustand zurück. Bei CPython läuft ein Programm mit Syntaxfehler gar nicht erst los und kann deshalb auch nichts halb erledigen. Gegen Laufzeitfehler schützt das allerdings nicht: Sie treten erst beim Ausführen auf.
:::
:::

---
title: Das Wichtigste bis hier
pfad: Informatik / Programmieren / Python / Programme und der Python-Interpreter
knoten: Python 1: Programme und der Python-Interpreter
order: 6020800
summary: Was ein Programm ist, wie Python es ausführt, interaktiv rechnen, Skripte schreiben und Fehlermeldungen lesen
tags: 
lang: de
---

:::kern Das Wichtigste bis hier
<ul>

<li>

Ein Programm ist eine Folge eindeutiger Arbeitsschritte (Anweisungen), die ein Rechner ohne Rückfrage ausführt. Der Prozessor versteht nur Maschinenbefehle; Menschen schreiben Quelltext in einer Programmiersprache mit fester Syntax (Form) und Semantik (Bedeutung).

</li>

<li>

Ein Compiler übersetzt den ganzen Quelltext einmal vorab in eine ausführbare Datei; ein Interpreter führt den Quelltext selbst aus. CPython, das Programm `python`, übersetzt bei jedem Start die ganze Datei in Bytecode und führt diesen dann in seiner Interpreterschleife aus.

</li>

<li>

Windows: Python install manager, Befehl `py`. Linux: vorinstalliertes `python3`, das System-Python nicht antasten. Versionsnummern wie 3.14.4 vergleicht man Teil für Teil.

</li>

<li>

Interaktiver Modus (`>>>`): Jeder Ausdruck wird ausgewertet und sein Wert angezeigt. Rechenzeichen `+ - * / **`, Klammern wie in der Mathematik, Punkt statt Komma, `e` für Zehnerpotenzen, `_` für das letzte Ergebnis.

</li>

<li>

Zeichenketten stehen in geraden Anführungszeichen. Ein Funktionsaufruf ist Name plus runde Klammern; `print` schreibt Werte ins Terminal.

</li>

<li>

Ein Skript ist eine `.py`-Datei, geschrieben mit einem Editor und gestartet mit `py datei.py` bzw. `python3 datei.py`; sichtbar wird nur, was `print` ausgibt. Kommentare beginnen mit `#`.

</li>

<li>

Syntaxfehler: vor dem Start, keine Zeile läuft. Laufzeitfehler: beim Ausführen, eine Ausnahme bricht ab, alles davor ist gelaufen. Logikfehler: keine Meldung, falsches Ergebnis. Den Traceback liest man von unten.

</li>

</ul>
:::

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Ein Programm ist ein Rezept aus eindeutigen Schritten, das man in einer Programmiersprache als Quelltext aufschreibt, weil der Prozessor nur Maschinenbefehle versteht und Alltagssprache mehrdeutig ist.

</li>

<li>

Python-Quelltext tippt man entweder im interaktiven Modus Zeile für Zeile ein, der jeden Wert sofort anzeigt, oder man speichert ihn als Skript, das man mit `py` bzw. `python3` startet und das nur mit `print` etwas ausgibt.

</li>

<li>

CPython übersetzt zuerst die ganze Datei und führt sie dann aus; deshalb verhindert ein Syntaxfehler jede Ausführung, ein Laufzeitfehler bricht erst in seiner Zeile ab, und ein Logikfehler fällt nur auf, wenn man das Ergebnis prüft.

</li>

</ol>
:::

**Ein Prinzip hinter allen Ergebnissen.** Fast alles in diesem Kapitel folgt daraus, dass CPython in zwei Phasen arbeitet: zuerst die ganze Datei übersetzen, dann den Bytecode ausführen. Die Form wird vor dem Start geprüft, die Ausführbarkeit beim Ausführen, die Absicht des Verfassers nie.

| Ergebnis | Woher es kommt |
|---|---|
| Python-Programme laufen auf jedem Rechner mit CPython | der Bytecode ist auf allen Prozessoren gleich, nur CPython ist übersetzt (Abschnitt [2](vom-quelltext-zur-ausfuhrung-compiler-und-interpreter.html#stufe-2)) |
| feste Ausdrücke wie `2 + 3` stehen schon als 5 im Bytecode | der Übersetzer rechnet in der ersten Phase vorab (Abschnitt [2](vom-quelltext-zur-ausfuhrung-compiler-und-interpreter.html#stufe-2)) |
| im Skript zeigt nur `print` etwas an | das Skript wird ohne den Befehl „Wert anzeigen“ übersetzt (Abschnitt [5](skripte-schreiben-und-ausfuhren.html#stufe-5)) |
| Kommentare kosten beim Ausführen nichts | sie fallen schon beim Zerlegen des Quelltexts weg (Abschnitt [5](skripte-schreiben-und-ausfuhren.html#stufe-5)) |
| ein Syntaxfehler verhindert jede Ausführung | ohne gültige Form entsteht kein Bytecode (Abschnitt [6](fehler-lesen-und-verstehen.html#stufe-6)) |
| ein Laufzeitfehler bricht erst in seiner Zeile ab | ausgeführt wird erst in der zweiten Phase, Zeile für Zeile (Abschnitt [6](fehler-lesen-und-verstehen.html#stufe-6)) |
| `5 / 0` wird nicht vorab ausgerechnet | der Fehler muss genau beim Ausführen der Zeile auftreten (Abschnitt [6](fehler-lesen-und-verstehen.html#stufe-6)) |
| Logikfehler meldet niemand | Python prüft Form und Ausführbarkeit, nicht die Absicht (Abschnitt [6](fehler-lesen-und-verstehen.html#stufe-6)) |

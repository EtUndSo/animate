---
title: Das Wichtigste bis hier
pfad: Informatik / Linux und Kommandozeile / Shell-Skripte
adresse: informatik/linux-und-kommandozeile/shell-skripte
knoten: Kapitel 10: Shell-Skripte
order: 6151200
summary: Wie aus einer Folge von Befehlen ein kleines Programm wird, das Argumente annimmt, Entscheidungen trifft, Dateien der Reihe nach bearbeitet, Fehler meldet und hinter sich aufräumt
tags: 
lang: de
---

:::kern Das Wichtigste bis hier
<ul>

<li>

Ein Skript ist eine Textdatei mit Befehlen; `bash skript` liest sie in einem Kindprozess, `source skript` in der eigenen Shell. `cd` und Variablen im Skript wirken nicht nach außen.

</li>

<li>

`#!/bin/bash` in der ersten Zeile nennt den Interpreter; `./skript` braucht `x` (der Kernel startet) und `r` (die bash liest). Windows-Zeilenenden machen daraus `bad interpreter`; `sed -i 's/\r$//'` hilft.

</li>

<li>

`$1` … `${10}`, `$0`, `$#`; `"$@"` reicht jedes Argument unverändert weiter, `"$*"` verbindet sie zu einem Text, `$*` zerlegt sie; `shift` rückt nach.

</li>

<li>

`if`, `while` und `until` prüfen Exit-Status. `[ ]` ist der Befehl `test` (Leerzeichen, Anführungszeichen, `-eq`/`-lt` für Zahlen, `=` für Text); `[[ ]]` kennt Muster und `=~`, ohne Worttrennung; `(( ))` vergleicht Zahlen und meldet Wert 0 als Status 1; `case` wählt den ersten passenden Fall.

</li>

<li>

`for` über Wörter, Muster, `"$@"` oder mit Zähler; nie über `$(ls)`. `while read -r … done < datei` liest Zeilen, `IFS=,` trennt Felder. Hinter einer Pipe verliert eine Schleife ihre Variablen.

</li>

<li>

Arrays: `a=(…)`, `"${a[@]}"`, `${#a[@]}`. Funktionen laufen in der eigenen Shell; `local` schirmt ab; Antwort über Exit-Status oder Ausgabe.

</li>

<li>

Erfolg als `exit 0`, Fehler 1, falscher Aufruf 2; Meldungen mit `>&2`; kritische Schritte mit `|| exit 1` prüfen. `set -u` meldet Tippfehler, `pipefail` Fehler vorn in Pipelines, `set -e` hat viele Ausnahmen.

</li>

<li>

`mktemp` plus `trap '…' EXIT` räumt auch bei Strg+C und `kill` auf, nicht bei `kill -9`. Prüfen mit `bash -n`, `bash -x`, `shellcheck`, Probelauf und Testfällen.

</li>

</ul>
:::

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Ein Skript ist eine Befehlsfolge in einer Datei, die eine eigene bash nach denselben Regeln für Wörter, Expansion und Quoting abarbeitet wie die Befehlszeile; die Shebang-Zeile sagt dem Kernel, welcher Interpreter sie bekommt.

</li>

<li>

Argumente kommen als Positionsparameter an und werden mit `"$@"` unverändert weitergereicht; Entscheidungen und Schleifen hängen am Exit-Status von Befehlen wie `test`, `[[ ]]`, `(( ))` und `read`.

</li>

<li>

Robust wird ein Skript, wenn es jede Variable in Anführungszeichen setzt, jeden kritischen Schritt selbst prüft, Fehler mit Status und Meldung auf der Fehlerausgabe meldet, Zwischendateien mit `mktemp` und `trap` verwaltet und vor dem Einsatz mit ShellCheck und Testfällen geprüft wird.

</li>

</ol>
:::

**Ein Prinzip hinter allen Ergebnissen.** Fast alles in diesem Kapitel folgt aus zwei Gedanken. Erstens: Ein Skript ist nichts Besonderes, sondern eine Folge gewöhnlicher Befehlszeilen, die eine bash in einem eigenen Prozess abarbeitet; jede Variable wird nach den Regeln von [Kapitel 5](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/expansion-quoting-variablen-und-umgebung.html) zu Wörtern, und jeder Prozess erbt nur Kopien. Zweitens: Die Shell kennt keine Wahrheitswerte, sondern nur Exit-Status; jede Bedingung, jede Schleife und jede Fehlerprüfung fragt, ob ein Befehl mit 0 geendet hat.

| Ergebnis | Woher es kommt |
|---|---|
| `cd` und Variablen im Skript wirken nicht nach außen | das Skript läuft in einem Kindprozess mit Kopien (Abschnitt [1](vom-befehl-zum-skript.html#stufe-1)) |
| `./skript` braucht `x` und `r` | der Kernel startet die Datei, die bash liest sie (Abschnitt [1](vom-befehl-zum-skript.html#stufe-1)) |
| `bad interpreter: /bin/bash^M` | der Wagenrücklauf gehört zum Namen des Interpreters (Abschnitt [1](vom-befehl-zum-skript.html#stufe-1)) |
| `"$@"` statt `$*` | Ersetzungen ohne Anführungszeichen durchlaufen Worttrennung und Muster (Abschnitt [2](argumente-ubergeben-positionsparameter.html#stufe-2)) |
| `[ $x = a ]` scheitert bei leerem `x` | `[` ist ein Befehl und bekommt nur fertige Wörter (Abschnitt [3](verzweigen-if-und-test.html#stufe-3)) |
| `[ 10 > 9 ]` ist immer wahr | `>` ist eine Umleitung (Abschnitt [3](verzweigen-if-und-test.html#stufe-3)) |
| `[[ ]]` verträgt Variablen ohne Anführungszeichen | ein Schlüsselwort, das die Shell selbst auswertet (Abschnitt [4](bequemer-prufen-und-case.html#stufe-4)) |
| `(( 0 ))` ist falsch | Wert 0 wird zu Status 1 (Abschnitt [4](bequemer-prufen-und-case.html#stufe-4)) |
| `for f in $(ls)` zerbricht Namen | die Ausgabe wird an Leerzeichen zerlegt, Muster liefern ganze Namen (Abschnitt [5](schleifen-for-und-while.html#stufe-5)) |
| eine Schleife hinter `\|` verliert ihre Variablen | jeder Teil einer Pipeline ist ein Kindprozess (Abschnitt [6](zeilen-lesen-und-listen-speichern.html#stufe-6)) |
| `read` braucht `-r` | sonst ist `\` ein Steuerzeichen (Abschnitt [6](zeilen-lesen-und-listen-speichern.html#stufe-6)) |
| eine Funktion kann `cd`, ein Skript nicht | die Funktion läuft in der aufrufenden Shell (Abschnitt [7](funktionen.html#stufe-7)) |
| Meldungen gehören auf die Fehlerausgabe | Daten und Meldungen bleiben getrennt (Abschnitt [8](fehler-erkennen-und-melden.html#stufe-8)) |
| `set -e` greift in `if` und hinter `\|\|` nicht | der Exit-Status ist dort eine Antwort, kein Fehler (Abschnitt [8](fehler-erkennen-und-melden.html#stufe-8)) |
| `trap … EXIT` hilft nicht gegen `kill -9` | SIGKILL kann kein Prozess abfangen (Abschnitt [9](aufraumen-temporare-dateien-und-trap.html#stufe-9)) |
| ein Archiv erscheint ganz oder gar nicht | Umbenennen im selben Dateisystem ist ein einziger Schritt (Abschnitt [9](aufraumen-temporare-dateien-und-trap.html#stufe-9)) |
| `bash -n` meldet den Fehler am `done` | die Shell bemerkt ein offenes `if` erst beim nächsten unpassenden Wort (Abschnitt [10](skripte-prufen-und-fehler-finden.html#stufe-10)) |

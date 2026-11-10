---
title: Das Wichtigste bis hier
pfad: Informatik / Linux und Kommandozeile / Die Shell: erste Befehle
adresse: informatik/linux-und-kommandozeile/die-shell-erste-befehle
knoten: Kapitel 2: Die Shell: erste Befehle
order: 6070900
summary: Terminal und Shell, der Aufbau eines Befehls, Hilfe zu jedem Befehl und die ersten Schritte durch das eigene System
tags: 
lang: de
---

:::kern Das Wichtigste bis hier
<ul>

<li>

Im Terminalfenster arbeiten zwei Programme: Der Terminalemulator zeichnet Zeichen und reicht Tastendrücke weiter, die Shell liest Befehlszeilen und lässt sie ausführen. Unter Ubuntu ist die Shell bash, ein gewöhnliches Programm im Benutzermodus.

</li>

<li>

Die Eingabeaufforderung zeigt Benutzer, Rechner und aktuellen Ordner; `$` steht für einen gewöhnlichen Benutzer, `#` für root. Jedes Fenster hat seine eigene Shell und damit seine eigene Sitzung.

</li>

<li>

Die Shell zerlegt eine Zeile an Leerzeichen in Wörter. Das erste ist der Befehl, die übrigen sind Argumente; Optionen beginnen mit `-` oder `--`, kurze lassen sich bündeln, manche verlangen einen Wert, und nach `--` ist jedes Wort ein gewöhnliches Argument. Was ein Wort bedeutet, entscheidet das Programm.

</li>

<li>

Ein Befehl ist ein Alias, ein eingebauter Befehl oder eine Programmdatei im Suchpfad; `type` sagt, welches, `which` sieht nur den Suchpfad. Befehle, die die Shell selbst verändern, wie `cd` und `exit`, müssen eingebaut sein.

</li>

<li>

Hilfe gibt es dreifach: `--help` für den Überblick, `help` für eingebaute Befehle, `man` für die vollständige Handbuchseite mit fester Gliederung und nummerierten Abschnitten; `apropos` findet Seiten über ihre Kurzbeschreibung.

</li>

<li>

Die Tabulatortaste vervollständigt, der Verlauf merkt sich jede Zeile, Strg+R sucht darin. Strg+C bricht ab, Strg+D meldet das Ende der Eingabe; bei einem laufenden Programm wertet der Kernel beide Tasten im Pseudoterminal aus, bevor das Programm sie liest.

</li>

<li>

`uname`, `whoami`, `id`, `date`, `uptime`, `free` und `df` ergeben einen Steckbrief des Systems. Ubuntu 26.04 liefert die meisten Grundbefehle als uutils; die GNU-Fassung heißt dort `gnu`….

</li>

</ul>
:::

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Mit einem Rechner, der nur Text versteht, spricht man über die Shell: Sie liest eine Befehlszeile, zerlegt sie in Wörter, findet den Befehl als Alias, eingebauten Befehl oder Programmdatei und lässt ihn ausführen.

</li>

<li>

Wie die Wörter heißen und was sie bedeuten, legt jedes Programm selbst fest, nach gemeinsamen Regeln für Optionen und Argumente; nachlesen kann man es jederzeit mit `--help`, `help` oder `man`.

</li>

<li>

Vervollständigung, Verlauf und Tastenkürzel sparen Tipparbeit, und schon wenige Befehle verraten Kernel, Distribution, Benutzer, Speicher und Plattenplatz des eigenen Systems.

</li>

</ol>
:::

**Ein Prinzip hinter allen Ergebnissen.** Fast alles in diesem Kapitel folgt aus einem Gedanken: Die Shell vermittelt, sie arbeitet nicht selbst. Sie zerlegt Zeilen, sucht Befehle und startet Programme; was ein Wort bedeutet, entscheidet das Programm, und was die Hardware oder das Terminal betrifft, erledigt der Kernel. Nur was die Shell an sich selbst ändern muss, tut sie selbst.

| Ergebnis | Woher es kommt |
|---|---|
| das Terminal kann man austauschen, ohne dass sich an den Befehlen etwas ändert | das Fenster zeichnet nur Zeichen, verstanden werden sie erst von der Shell (Abschnitt [1](terminal-und-shell.html#stufe-1)) |
| zwei Fenster haben verschiedene aktuelle Ordner | jedes Fenster hat seine eigene Shell und Sitzung (Abschnitt [1](terminal-und-shell.html#stufe-1)) |
| `echo Hallo Welt` gibt nur ein Leerzeichen aus | die Shell übergibt Wörter, keine Leerzeichen (Abschnitt [2](der-aufbau-einer-befehlszeile.html#stufe-2)) |
| `uname -mrs` und `uname -srm` geben dasselbe aus | das Programm deutet die Optionen und wählt die Reihenfolge (Abschnitt [2](der-aufbau-einer-befehlszeile.html#stufe-2)) |
| nach `--` ist `-l` ein Dateiname | gemeinsame Regeln für Optionen, die das Programm umsetzt (Abschnitt [2](der-aufbau-einer-befehlszeile.html#stufe-2)) |
| `cd` und `exit` sind eingebaut | nur die Shell kann ihren eigenen Ordner wechseln und sich selbst beenden (Abschnitt [3](arten-von-befehlen.html#stufe-3)) |
| `which cd` findet unter Ubuntu nichts, `type cd` schon | `which` ist ein eigenes Programm und sieht nur den Suchpfad (Abschnitt [3](arten-von-befehlen.html#stufe-3)) |
| `type ls` meldet unter Ubuntu einen Alias | die Shell ersetzt Aliase schon beim Einlesen (Abschnitt [3](arten-von-befehlen.html#stufe-3)) |
| `man cd` findet nichts, `help cd` schon | eingebaute Befehle beschreibt die Shell selbst (Abschnitt [4](hilfe-finden.html#stufe-4)) |
| `man passwd` zeigt den Befehl, nicht die Datei | ohne Nummer gewinnt der erste passende Abschnitt (Abschnitt [4](hilfe-finden.html#stufe-4)) |
| Strg+C bricht auch ein Programm ab, das nicht auf Tasten achtet | der Kernel wertet die Taste im Pseudoterminal aus (Abschnitt [5](schneller-arbeiten-vervollstandigung-verlauf-tastenkurzel.html#stufe-5)) |
| Strg+D beendet `cat` und in einer leeren Zeile auch die Shell | ein Lesen mit null Zeichen heißt „Ende der Eingabe“; bash wertet die Taste ebenso aus (Abschnitt [5](schneller-arbeiten-vervollstandigung-verlauf-tastenkurzel.html#stufe-5)) |
| `free` ist klein, `available` groß | der Kernel nutzt freien Speicher als Zwischenspeicher für Dateien (Abschnitt [6](das-system-erkunden.html#stufe-6)) |
| `ls` und `uname` sind unter Ubuntu 26.04 dieselbe Datei | das Multicall-Programm liest den Namen, unter dem es gestartet wurde (Abschnitt [7](zwei-fassungen-der-grundbefehle-gnu-und-uutils.html#stufe-7)) |

---
title: Das Wichtigste bis hier
pfad: Informatik / Linux und Kommandozeile / Ströme, Umleitung, Pipes und Exit-Status
adresse: informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status
knoten: Kapitel 4: Ströme, Umleitung, Pipes und Exit-Status
order: 6090900
summary: Was ein laufendes Programm liest und schreibt, wie man Ausgaben in Dateien lenkt, Programme zu Ketten verbindet und auf Erfolg und Misserfolg reagiert
tags: 
lang: de
---

:::kern Das Wichtigste bis hier
<ul>

<li>

Ein Prozess ist eine laufende Ausführung eines Programms mit eigenem Speicher, eigenen geöffneten Dateien und eigener Nummer. Die Shell startet für jedes Programm einen neuen Prozess.

</li>

<li>

Jeder Prozess hat drei Standardströme: die Standardeingabe (Deskriptor 0), die Standardausgabe für Ergebnisse (1) und die Standardfehlerausgabe für Meldungen (2). Im Terminal führen alle drei zum Terminal; ein Deskriptor ist die Nummer, unter der der Prozess eine geöffnete Datei beim Kernel anspricht.

</li>

<li>

Umleitungen verbinden Deskriptoren vor dem Programmstart mit Dateien: `>` (leeren und schreiben), `>>` (anhängen), `2>` (Fehlerausgabe), `2>&1` (Kopie eines Deskriptors), `&>` (beide), `<` (Eingabe), `<<ENDE` und `<<<` (Text als Eingabe). `/dev/null` verschluckt alles.

</li>

<li>

Umleitungen wirken von links nach rechts, deshalb `> datei 2>&1`. Die Shell leert die Zieldatei vor dem Start, deshalb nie `befehl datei > datei`.

</li>

<li>

Eine Pipe verbindet die Standardausgabe eines Programms mit der Standardeingabe des nächsten; eine Pipeline reiht Filter wie `sort`, `uniq`, `grep`, `head` und `wc` aneinander, `tee` zweigt eine Kopie ab. Meldungen laufen an der Pipe vorbei.

</li>

<li>

Jeder Prozess endet mit einem Exit-Status von 0 bis 255; 0 heißt Erfolg, `$?` liefert den letzten. Die Shell setzt 127 (nicht gefunden), 126 (nicht ausführbar) und $128 + n$ (Abbruch durch Unterbrechungsnachricht $n$).

</li>

<li>

`;` führt nacheinander aus, `&&` nur bei Erfolg, `||` nur bei Misserfolg; `a && b || c` ist kein sicheres „wenn, dann, sonst“. Eine Pipeline hat den Exit-Status ihres letzten Befehls; `PIPESTATUS` und `pipefail` zeigen frühere Fehler.

</li>

<li>

`xargs` macht aus einem Strom Argumente, mit `-n` in Portionen; `find -print0 | xargs -0` und `find -exec … +` übergeben auch Namen mit Leerzeichen richtig.

</li>

</ul>
:::

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Jedes Programm läuft als Prozess mit drei Standardströmen, die es nur über die Nummern 0, 1 und 2 kennt; wohin diese führen, legt die Shell vor dem Start fest.

</li>

<li>

Mit Umleitungen verbindet man sie mit Dateien, mit Pipes mit anderen Programmen, und so werden aus kleinen Filtern Werkzeugketten, die gemeinsam Fragen beantworten, für die es kein eigenes Programm gibt.

</li>

<li>

Am Exit-Status erkennt die Shell Erfolg und Misserfolg und macht mit `&&` und `||` den nächsten Schritt davon abhängig.

</li>

</ol>
:::

**Ein Prinzip hinter allen Ergebnissen.** Fast alles in diesem Kapitel folgt aus einem Gedanken: Ein Programm liest und schreibt nur über seine Deskriptoren, und die Shell entscheidet vor dem Start, wohin diese führen. Das Programm muss deshalb nichts über Dateien, Terminals oder andere Programme wissen, und dieselben kleinen Werkzeuge lassen sich auf immer neue Weise verbinden.

| Ergebnis | Woher es kommt |
|---|---|
| `readlink /proc/self` zeigt jedes Mal eine andere Zahl | jeder Befehl läuft in einem neuen Prozess mit eigener Nummer (Abschnitt [1](prozesse-und-ihre-drei-strome.html#stufe-1)) |
| eine Fehlermeldung erscheint trotz `>` am Bildschirm | sie geht durch Deskriptor 2, umgeleitet war nur die 1 (Abschnitte [1](prozesse-und-ihre-drei-strome.html#stufe-1) und [2](ausgaben-umleiten.html#stufe-2)) |
| `echo Hallo > gruss.txt` schreibt nur `Hallo` in die Datei | die Shell entfernt die Umleitung aus den Argumenten (Abschnitt [2](ausgaben-umleiten.html#stufe-2)) |
| `2>&1 > datei` lässt die Meldung am Bildschirm | Umleitungen wirken von links nach rechts, `2>&1` kopiert das momentane Ziel (Abschnitt [2](ausgaben-umleiten.html#stufe-2)) |
| `sort a > a` hinterlässt eine leere Datei | die Shell leert `a`, bevor `sort` liest (Abschnitt [2](ausgaben-umleiten.html#stufe-2)) |
| `wc -l < datei` schreibt keinen Namen | `wc` bekommt nur einen Strom (Abschnitt [3](eingaben-umleiten.html#stufe-3)) |
| `wc -l < fehlt.txt` meldet einen Fehler von bash | die Shell öffnet die Datei, `wc` startet gar nicht (Abschnitt [3](eingaben-umleiten.html#stufe-3)) |
| `ls /gibtsnicht \| wc -l` zählt 0 | die Pipe verbindet nur Deskriptor 1 mit 0, die Meldung geht an den Bildschirm (Abschnitt [4](pipes-und-filter.html#stufe-4)) |
| `uniq` braucht ein `sort` davor | es vergleicht jede Zeile nur mit der direkt davor (Abschnitt [4](pipes-und-filter.html#stufe-4)) |
| das zweite `echo $?` zeigt 0 | `$?` gilt immer für den zuletzt beendeten Befehl (Abschnitt [5](der-exit-status.html#stufe-5)) |
| Strg+C hinterlässt 130 | Abbruch durch die Nachricht 2, und $128 + 2 = 130$ (Abschnitt [5](der-exit-status.html#stufe-5)) |
| `sort fehlt.txt \| head` meldet Erfolg | eine Pipeline hat den Exit-Status ihres letzten Befehls (Abschnitt [6](befehle-verketten.html#stufe-6)) |
| `a && b \|\| c` führt `c` aus, obwohl `a` gelang | beide Verknüpfungen sind gleichrangig und gelten von links (Abschnitt [6](befehle-verketten.html#stufe-6)) |
| `echo datei \| rm` löscht nichts | eine Pipe liefert Eingabe, keine Argumente (Abschnitt [7](aus-einer-ausgabe-argumente-machen.html#stufe-7)) |
| `xargs` zerlegt `mein foto.jpg` in zwei Namen | es trennt an Leerzeichen; nur das Nullbyte kommt in keinem Namen vor (Abschnitt [7](aus-einer-ausgabe-argumente-machen.html#stufe-7)) |

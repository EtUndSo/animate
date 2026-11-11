---
title: Das Wichtigste bis hier
pfad: Informatik / Linux und Kommandozeile / Textwerkzeuge und reguläre Ausdrücke
adresse: informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke
knoten: Kapitel 6: Textwerkzeuge und reguläre Ausdrücke
order: 6111200
summary: Zeilen auswählen, Spalten schneiden, sortieren, zählen, umformen und rechnen, und wie man nach der Form eines Textes sucht statt nach festen Wörtern
tags: 
lang: de
---

:::kern Das Wichtigste bis hier
<ul>

<li>

Eine Tabelle als Text besteht aus Datensätzen, einer je Zeile, und Feldern, getrennt durch ein Trennzeichen; eine CSV-Datei trennt mit Kommas und hat oft eine Kopfzeile. Windows hängt vor jedes Zeilenende einen Wagenrücklauf, den `cat -A` als `^M` zeigt und `tr -d '\r'` entfernt.

</li>

<li>

`tail -n +2` entfernt die Kopfzeile, `tail -f` folgt einer wachsenden Datei. `cut -d, -f2` schneidet Felder aus, `tr` ersetzt oder löscht Zeichen, `paste` legt Spalten nebeneinander.

</li>

<li>

`sort` vergleicht Zeichen für Zeichen, `-n` nach dem Zahlenwert, `-t, -k3,3` nach einem Feld; die Spracheinstellung bestimmt die Ordnung, `LC_ALL=C` macht sie überall gleich. `uniq` vergleicht nur Nachbarn; `sort | uniq -c | sort -rn` zählt Häufigkeiten.

</li>

<li>

`nl` nummeriert, `seq` erzeugt Zahlenfolgen, `diff` zeigt mit `a`, `c` und `d`, was zwischen zwei Dateien anders ist.

</li>

<li>

`grep` schreibt die Zeilen mit einem Treffer; `-i -v -c -n -o -r -l` ändern, was es sucht und ausgibt.

</li>

<li>

Ein regulärer Ausdruck beschreibt eine Menge von Zeichenketten: `.` ein beliebiges Zeichen, `[…]` eines aus einer Liste, `[[:digit:]]` eine Klasse, `^` und `$` Anfang und Ende, `*` `+` `?` `{n,m}` Wiederholungen, `( )` Gruppen, `|` Alternativen; `\` oder `grep -F` nehmen Zeichen wörtlich. Die Grundform braucht vor `{ }` und `( )` einen umgekehrten Schrägstrich, `-E` schaltet die erweiterte ein.

</li>

<li>

Es gewinnt der Treffer, der am weitesten links beginnt, und von dort der längste. Ein Ausdruck prüft Form, nicht Bedeutung. Muster für Dateinamen wertet die Shell aus, reguläre Ausdrücke das Programm; deshalb stehen Ausdrücke in einfachen Anführungszeichen.

</li>

<li>

`sed` bearbeitet einen Strom Zeile für Zeile: `s/ausdruck/ersatz/g` ersetzt, `\1` setzt Gruppen ein, Zeilenadressen wählen Zeilen, `d` löscht, `-n` mit `p` gibt aus. `sed -i` ändert die Datei über eine neue Datei; eine Umleitung in dieselbe Datei leert sie.

</li>

<li>

`awk` wendet Regeln `bedingung {aktion}` auf jede Zeile an, kennt Felder `$1` bis `$NF`, die Zeilennummer `NR`, rechnet mit Kommazahlen, sammelt in Variablen und assoziativen Arrays und gibt in `END` das Ergebnis aus.

</li>

</ul>
:::

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Fragen an eine Textdatei beantwortet man mit kleinen Werkzeugen in einer Pipeline: Zeilen wählen mit `grep`, Spalten schneiden mit `cut`, ordnen mit `sort`, zählen mit `uniq -c`, umformen mit `tr` und `sed`, rechnen mit `awk`.

</li>

<li>

Statt fester Wörter beschreiben reguläre Ausdrücke die Form gesuchter Zeichenketten, mit Platzhaltern, Auswahlen, Ankern, Wiederholungen und Alternativen.

</li>

<li>

Die Werkzeuge lesen Zeile für Zeile und Zeichen für Zeichen und kennen nur Zeichen, keine Bedeutung; daraus folgen ihre Überraschungen, von `10` vor `9` bis zum unsichtbaren Wagenrücklauf.

</li>

</ol>
:::

**Ein Prinzip hinter allen Ergebnissen.** Fast alles in diesem Kapitel folgt aus zwei Gedanken. Erstens: Die Werkzeuge sehen Zeichen, keine Bedeutung. Sie lesen einen Strom Zeile für Zeile, vergleichen Zeichen für Zeichen und wissen nicht, ob eine Ziffernfolge eine Zahl, ein Datum oder ein Name ist, solange man es ihnen nicht ausdrücklich sagt. Zweitens: Kleine Werkzeuge, die Text lesen und Text schreiben, lassen sich zu Antworten auf Fragen verbinden, an die beim Bau keiner von ihnen gedacht hat.

| Ergebnis | Woher es kommt |
|---|---|
| `grep -c ',28$'` findet die Zeile in der Windows-Datei nicht | der Wagenrücklauf steht vor dem Zeilenende (Abschnitte [1](textdaten-datensatze-felder-und-zeilenenden.html#stufe-1) und [6](regulare-ausdrucke-zeichen-klassen-und-anker.html#stufe-6)) |
| `cut -f2` liefert ganze Zeilen | ohne `-d` trennt `cut` nur an Tabulatoren (Abschnitt [2](spalten-ausschneiden-und-zeichen-ersetzen-cut-tr-und-paste.html#stufe-2)) |
| `tr a-z A-Z` lässt das ä klein | `tr` arbeitet Byte für Byte (Abschnitt [2](spalten-ausschneiden-und-zeichen-ersetzen-cut-tr-und-paste.html#stufe-2)) |
| `sort` stellt `10` vor `9` | Vergleich Zeichen für Zeichen (Abschnitt [3](sortieren-und-zahlen-sort-und-uniq.html#stufe-3)) |
| die Kopfzeile steht bei `sort -n` vorn | Text ohne Zahl zählt als 0 (Abschnitt [3](sortieren-und-zahlen-sort-und-uniq.html#stufe-3)) |
| dieselbe Liste sortiert auf einem anderen Rechner anders | die Spracheinstellung bestimmt die Ordnung (Abschnitt [3](sortieren-und-zahlen-sort-und-uniq.html#stufe-3)) |
| `uniq -c` ohne `sort` zählt jede Zeile einzeln | `uniq` vergleicht nur Nachbarn (Abschnitt [3](sortieren-und-zahlen-sort-und-uniq.html#stufe-3)) |
| `grep '5.0'` findet auch `520` | der Punkt ist ein beliebiges Zeichen (Abschnitt [6](regulare-ausdrucke-zeichen-klassen-und-anker.html#stufe-6)) |
| `grep -c 'a*'` zählt jede Zeile | der Stern erlaubt null Wiederholungen (Abschnitt [7](regulare-ausdrucke-wiederholungen-gruppen-und-alternativen.html#stufe-7)) |
| `grep ',[0-9]{3}$'` findet nichts | in der Grundform sind `{ }` gewöhnliche Zeichen (Abschnitt [7](regulare-ausdrucke-wiederholungen-gruppen-und-alternativen.html#stufe-7)) |
| `A.*km` reicht bis zum letzten `km` | der längste Treffer gewinnt (Abschnitt [7](regulare-ausdrucke-wiederholungen-gruppen-und-alternativen.html#stufe-7)) |
| `2026-13-45` passt auf den Ausdruck für ein Datum | ein Ausdruck prüft Form, nicht Bedeutung (Abschnitt [7](regulare-ausdrucke-wiederholungen-gruppen-und-alternativen.html#stufe-7)) |
| `grep -c Ann*` meldet 0 | ohne Anführungszeichen macht die Shell daraus ein Muster (Abschnitt [7](regulare-ausdrucke-wiederholungen-gruppen-und-alternativen.html#stufe-7)) |
| `sed … datei > datei` hinterlässt eine leere Datei | die Shell leert sie vor dem Start, `sed -i` nicht (Abschnitt [8](umformen-im-strom-sed.html#stufe-8)) |
| `awk '$3 > 10'` liefert die Kopfzeile mit | `km` ist keine Zahl und wird als Text verglichen (Abschnitt [9](rechnen-mit-spalten-awk.html#stufe-9)) |
| `for (p in n)` gibt ungeordnet aus | ein assoziatives Array hat keine Reihenfolge (Abschnitt [9](rechnen-mit-spalten-awk.html#stufe-9)) |

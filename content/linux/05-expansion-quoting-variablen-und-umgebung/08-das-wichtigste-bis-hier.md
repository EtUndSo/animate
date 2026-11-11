---
title: Das Wichtigste bis hier
pfad: Informatik / Linux und Kommandozeile / Wie die Shell eine Befehlszeile liest: Expansion, Quoting, Variablen, Umgebung
adresse: informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung
knoten: Kapitel 5: Wie die Shell eine Befehlszeile liest: Expansion, Quoting, Variablen, Umgebung
order: 6100800
summary: Was die Shell aus einer Zeile macht, bevor ein Programm startet, wie man das mit Anführungszeichen steuert, was ein Programm von der Shell mitbekommt und wie die Shell es findet
tags: 
lang: de
---

:::kern Das Wichtigste bis hier
<ul>

<li>

Zwischen dem Tippen und dem Programmstart schreibt die Shell die Zeile um, die Expansion. Das Programm bekommt nur die fertige Argumentliste.

</li>

<li>

Die Pfadnamen-Erweiterung ersetzt Muster durch die sortierten passenden Namen; versteckte Dateien nur mit Punkt im Muster, ohne Treffer bleibt das Muster stehen. Die Klammererweiterung erzeugt Wörter ohne Blick auf Dateien, die Tilde-Erweiterung setzt Heimatverzeichnisse ein.

</li>

<li>

`NAME=wert` ohne Leerzeichen legt eine Shell-Variable an; `$NAME` oder `${NAME}` setzt ihren Wert ein, `$(befehl)` die Ausgabe eines Befehls, `$((…))` das Ergebnis einer Rechnung mit ganzen Zahlen.

</li>

<li>

Die Worttrennung zerlegt die Ergebnisse ungeschützter Erweiterungen an Leerzeichen, Tabulatoren und Zeilenenden; danach wirken darin Musterzeichen. Einfache Anführungszeichen schützen alles, doppelte alles außer `$`, `` ` `` und `\`, ein umgekehrter Schrägstrich ein Zeichen; zum Schluss entfernt die Shell die getippten Anführungszeichen.

</li>

<li>

Reihenfolge: Zerlegen, Klammern, dann Tilde, Parameter, Arithmetik, Befehlsersetzung, dann Worttrennung, Muster, Entfernen der Anführungszeichen. Regel: `"$variable"` und `"$(befehl)"`.

</li>

<li>

Jeder Prozess bekommt beim Start eine Umgebung aus Einträgen `NAME=wert`. `export` nimmt eine Variable darin auf, `NAME=wert befehl` gilt nur für einen Befehl, `env` und `printenv` zeigen und verändern sie. Ein Kind bekommt eine Kopie und kann nichts zurückgeben.

</li>

<li>

`PATH` ist der Suchpfad: Verzeichnisse mit Doppelpunkten, durchsucht von links nach rechts, nur bei Namen ohne Schrägstrich. Das Arbeitsverzeichnis gehört nicht dazu, deshalb `./programm`.

</li>

<li>

Eine neue interaktive bash liest `~/.bashrc`, eine Anmelde-Shell `/etc/profile` und `~/.profile`. `source` führt eine Datei in der laufenden Shell aus. Aliase gelten nur in interaktiven Shells.

</li>

</ul>
:::

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Bevor sie ein Programm startet, ersetzt die Shell Muster, Klammern, Tilden, Variablen, Befehle und Rechnungen, zerlegt die Ergebnisse in Wörter und entfernt die Anführungszeichen, in fester Reihenfolge; mit Anführungszeichen und dem umgekehrten Schrägstrich bestimmst du, was davon geschieht.

</li>

<li>

Das Programm bekommt die fertigen Wörter als Argumente und dazu eine Kopie der Umgebung mit allen exportierten Variablen; zurückgeben kann es davon nichts.

</li>

<li>

Gefunden wird ein Programm über die Verzeichnisse in `PATH`, und alles, was eine Shell bei jedem Start wissen soll, steht in Startdateien wie `~/.bashrc`.

</li>

</ol>
:::

**Ein Prinzip hinter allen Ergebnissen.** Fast alles in diesem Kapitel folgt aus zwei Gedanken. Erstens: Die Shell bereitet vor, das Programm führt aus. Alles, was mit der getippten Zeile geschieht, erledigt die Shell, bevor das Programm startet, und das Programm sieht nur das Ergebnis. Zweitens: Ein Prozess erbt, er kann nicht zurückgeben. Ein Kind bekommt eine Kopie, und was es damit macht, bleibt bei ihm.

| Ergebnis | Woher es kommt |
|---|---|
| `ls` merkt nicht, ob `*.txt` oder die Namen getippt wurden | die Shell ersetzt das Muster vor dem Start (Abschnitt [1](expansion-muster-klammern-und-tilde.html#stufe-1)) |
| `rm *.bak` meldet einen Namen mit Stern | ohne Treffer bleibt das Muster stehen (Abschnitt [1](expansion-muster-klammern-und-tilde.html#stufe-1)) |
| `ls foto{1,2,3}.jpg` meldet eine fehlende Datei | Klammern erzeugen Wörter, ohne nach Dateien zu sehen (Abschnitt [1](expansion-muster-klammern-und-tilde.html#stufe-1)) |
| `wohnort = Hamburg` ergibt „command not found“ | das erste Wort ist der Befehl (Abschnitt [2](variablen-befehlsersetzung-und-arithmetik.html#stufe-2)) |
| `$datei1.jpg` ergibt `.jpg` | ohne Klammern gehört die 1 zum Namen (Abschnitt [2](variablen-befehlsersetzung-und-arithmetik.html#stufe-2)) |
| `$((7 / 2))` ergibt 3 | die Shell rechnet nur mit ganzen Zahlen (Abschnitt [2](variablen-befehlsersetzung-und-arithmetik.html#stufe-2)) |
| `ls $datei` sucht `mein` und `bericht.txt` | Worttrennung des eingesetzten Werts (Abschnitt [3](worttrennung-und-quoting.html#stufe-3)) |
| `echo $(cat einkauf.txt)` schreibt eine Zeile | die Worttrennung trennt auch an Zeilenenden (Abschnitt [3](worttrennung-und-quoting.html#stufe-3)) |
| `{1..$n}` bleibt stehen | die Klammererweiterung kommt vor der Parametererweiterung (Abschnitt [3](worttrennung-und-quoting.html#stufe-3)) |
| `bash -c 'echo $obst'` zeigt nichts | das Kind bekommt nur exportierte Variablen (Abschnitt [4](umgebung-und-vererbung.html#stufe-4)) |
| ein `export` im Kind ändert die Shell nicht | das Kind hat nur eine Kopie (Abschnitt [4](umgebung-und-vererbung.html#stufe-4)) |
| `TZ=Asia/Tokyo date` ändert die Shell nicht | die Zuweisung gilt nur für diesen Befehl (Abschnitt [4](umgebung-und-vererbung.html#stufe-4)) |
| `meinbaum` wird nicht gefunden, `./meinbaum` schon | ohne Schrägstrich nur Suche in `PATH` (Abschnitt [5](wie-die-shell-programme-findet-path.html#stufe-5)) |
| eine neue Variable fehlt im nächsten Terminal | jede Shell beginnt neu, nur Startdateien bleiben (Abschnitt [6](startdateien-und-aliase.html#stufe-6)) |
| `source ~/.bashrc` wirkt, eine Kind-Shell nicht | `source` läuft im selben Prozess (Abschnitt [6](startdateien-und-aliase.html#stufe-6)) |

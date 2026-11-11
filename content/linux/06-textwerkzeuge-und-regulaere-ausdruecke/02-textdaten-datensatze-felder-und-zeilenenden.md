---
title: Textdaten: Datensätze, Felder und Zeilenenden
pfad: Informatik / Linux und Kommandozeile / Textwerkzeuge und reguläre Ausdrücke
adresse: informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke
knoten: Kapitel 6: Textwerkzeuge und reguläre Ausdrücke
order: 6110200
summary: Bevor man Daten auswertet, muss man wissen, wie sie in einer Textdatei liegen.
tags: Datensatz, Felder, Trennzeichen, Spalte, CSV-Datei, Kopfzeile, Wagenrücklauf
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Bevor man Daten auswertet, muss man wissen, wie sie in einer Textdatei liegen. Dieser Abschnitt zeigt, wie eine Tabelle als Text aussieht, legt die Datei an, mit der das ganze Kapitel arbeitet, erklärt, warum Dateien aus Windows ein unsichtbares Zeichen mehr haben, und zeigt, wie man Teile einer Datei herausgreift und einer wachsenden Datei beim Wachsen zusieht.
:::

:::::vorwissen Was du dafür brauchst: Textdatei, Filter, Pipeline und Quoting

<span class="anker" id="stufe-1-1"></span>

Dieses Kapitel setzt die [Kapitel 1](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/ein-linux-zum-ueben.html) bis 5 voraus. Daraus brauchst du vor allem diese Dinge.

<ul>

<li>

Eine Textdatei besteht nur aus Zeichen und ist in Zeilen gegliedert; jede Zeile endet mit dem Zeilenende, dem Byte 10, geschrieben `\n`. Ein Umlaut belegt in UTF-8 zwei Bytes ([Kapitel 3, Abschnitt 4.1](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-ansehen.html#stufe-4-1)). `cat` gibt Dateien aus, `head` und `tail` zeigen Anfang und Ende, `wc` zählt Zeilen, Wörter und Bytes, `file` bestimmt die Art einer Datei ([Kapitel 3, Abschnitte 4.2](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-ansehen.html#stufe-4-2) bis 4.6).

</li>

<li>

Ein Programm liest seine Standardeingabe und schreibt in seine Standardausgabe. `>` lenkt die Ausgabe in eine Datei, `<` holt die Eingabe aus einer Datei, ein Here-Document liefert mehrere getippte Zeilen als Eingabe ([Kapitel 4, Abschnitte 2.1](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/ausgaben-umleiten.html#stufe-2-1), 3.1 und 3.2). Wer mit `>` in dieselbe Datei schreibt, aus der er liest, findet sie leer vor, die Kürzungsfalle ([Kapitel 4, Abschnitt 2.7](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/ausgaben-umleiten.html#stufe-2-7)).

</li>

<li>

Eine Pipe `|` verbindet die Ausgabe eines Programms mit der Eingabe des nächsten. Ein Filter liest seine Standardeingabe, formt sie um und schreibt das Ergebnis aus; mehrere Filter hintereinander bilden eine Pipeline ([Kapitel 4, Abschnitte 4.1](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/pipes-und-filter.html#stufe-4-1) bis 4.3). `sort`, `uniq`, `grep` und `tr` hast du dort in ihrer einfachsten Form gesehen. Jeder Befehl meldet mit seinem Exit-Status, ob er Erfolg hatte; `$?` zeigt ihn ([Kapitel 4, Abschnitte 5.1](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/der-exit-status.html#stufe-5-1) und [5.2](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/der-exit-status.html#stufe-5-2)).

</li>

<li>

`printf` schreibt Text nach einer Vorlage; `%s` steht für das nächste Argument, und die Vorlage wird wiederholt, solange Argumente übrig sind ([Kapitel 5, Abschnitt 3.1](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/worttrennung-und-quoting.html#stufe-3-1)). Zwischen einfachen Anführungszeichen nimmt die Shell jedes Zeichen wörtlich ([Kapitel 5, Abschnitt 3.4](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/worttrennung-und-quoting.html#stufe-3-4)). `$(befehl)` setzt die Ausgabe eines Befehls ein, `$((…))` das Ergebnis einer Rechnung mit ganzen Zahlen ([Kapitel 5, Abschnitte 2.3](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/variablen-befehlsersetzung-und-arithmetik.html#stufe-2-3) und [2.4](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/variablen-befehlsersetzung-und-arithmetik.html#stufe-2-4)). `NAME=wert befehl` setzt eine Variable nur für diesen einen Befehl ([Kapitel 5, Abschnitt 4.6](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/umgebung-und-vererbung.html#stufe-4-6)).

</li>

<li>

Strg+C bricht ein laufendes Programm ab ([Kapitel 2, Abschnitt 5.4](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/schneller-arbeiten-vervollstandigung-verlauf-tastenkurzel.html#stufe-5-4)). Mit der Vorsilbe `gnu` ruft man unter Ubuntu 26.04 die GNU-Fassung eines Grundbefehls auf, etwa `gnusort` ([Kapitel 2, Abschnitt 7.3](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/zwei-fassungen-der-grundbefehle-gnu-und-uutils.html#stufe-7-3)).

</li>

</ul>

⁠**Kurz gesagt:** Du brauchst Textdateien und Zeilenenden, die Befehle aus [Kapitel 3](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-verzeichnisse-und-pfade.html) zum Ansehen, Umleitung, Pipe und Filter, `printf`, einfache Anführungszeichen und die Rechnung mit `$((…))`.

:::warnung Nur im eigenen Übungsverzeichnis
Einige Befehle dieses Kapitels legen Dateien an, ändern oder leeren sie. Lege dir deshalb ein eigenes Übungsverzeichnis an und arbeite dort:

```console
$ mkdir ~/linuxk6
$ cd ~/linuxk6
```

Alle Dateinamen in den Beispielen beziehen sich auf dieses Verzeichnis.
:::

:::::

### Datensatz und Feld

<span class="anker" id="stufe-1-2"></span>

Ein Lauftreff schreibt nach jedem Lauf auf, wann, wer, wie weit und wie lange gelaufen ist. Auf Papier oder in einem Tabellenprogramm wäre das eine Tabelle mit Zeilen und Spalten. Eine Textdatei kennt aber keine Kästchen, nur Zeichen und Zeilenenden. Abbildung [1](#abb-1) zeigt, wie eine Tabelle trotzdem in eine Textdatei passt.

:::abbildung linux/k6tabelle 1
Oben eine kleine Tabelle mit den Spalten Datum, Name, Strecke in Kilometern und Dauer in Minuten. Unten dieselben Werte als Text: Jede Tabellenzeile wird eine Zeile der Datei, die Werte einer Zeile stehen hintereinander, getrennt durch Kommas. Die Kommas leuchten auf, dann bekommen die vier Werte der Zeile `2026-11-02,Ben,10.5,62` ihre Nummern 1 bis 4.
:::

:::definition Definition 1.1 (Datensatz, Feld)
<span class="anker" id="satz-1-1"></span>

Ein __Datensatz__ ist eine Zeile einer Textdatei, die die Werte einer Tabellenzeile enthält. Seine einzelnen Werte heißen __Felder__; sie stehen in fester Reihenfolge hintereinander. Zwischen zwei Feldern steht jeweils ein vereinbartes Zeichen, das __Trennzeichen__. Die Felder eines Datensatzes zählt man von links mit 1 beginnend.
:::

Welches Zeichen trennt, legt derjenige fest, der die Datei schreibt; üblich sind Komma, Semikolon, Doppelpunkt und der Tabulator. Ein Trennzeichen darf in den Werten selbst nicht vorkommen, sonst wäre nicht mehr klar, wo ein Feld endet. Die Felder mit derselben Nummer in allen Datensätzen bilden zusammen eine __Spalte__.

::::beispiel Ein Datensatz zerlegt
Im Datensatz `2026-11-02,Ben,10.5,62` trennen drei Kommas vier Felder. Feld 1 ist das Datum `2026-11-02`, Feld 2 der Name `Ben`, Feld 3 die Strecke `10.5` in Kilometern und Feld 4 die Dauer `62` in Minuten. Kommazahlen stehen mit Punkt da, so wie die meisten Programme sie schreiben; sonst wäre das Komma in `10,5` nicht von einem Trennzeichen zu unterscheiden. Auch die Benutzerliste `/etc/passwd` aus [Kapitel 3, Abschnitt 4.4](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-ansehen.html#stufe-4-4) besteht aus Datensätzen; dort trennt ein Doppelpunkt die sieben Felder.
::::

⁠**Kurz gesagt:** Eine Zeile mit den Werten einer Tabellenzeile ist ein Datensatz; seine Werte sind die Felder, getrennt durch ein Trennzeichen und von links gezählt.

### Die CSV-Datei und ihre Kopfzeile

<span class="anker" id="stufe-1-3"></span>

Für Tabellen in Textform gibt es eine Form, die fast jedes Programm lesen und schreiben kann, vom Tabellenprogramm bis zum Onlinebanking. In dieser Form legst du jetzt das Lauftagebuch an, mit dem das Kapitel bis zum Schluss arbeitet.

:::definition Definition 1.2 (CSV-Datei, Kopfzeile)
<span class="anker" id="satz-1-2"></span>

Eine __CSV-Datei__ ist eine Textdatei, in der jede Zeile ein Datensatz ist und das Komma die Felder trennt. Der Name kommt von englisch „comma-separated values“, durch Kommas getrennte Werte. Oft enthält die erste Zeile statt Werten die Namen der Spalten; sie heißt __Kopfzeile__.
:::

Die Kopfzeile ist für Menschen gedacht und für Programme, die Spalten über ihren Namen ansprechen. Die Werkzeuge dieses Kapitels behandeln sie wie jede andere Zeile; wo sie stört, nimmt man sie vorher heraus.

Das Lauftagebuch entsteht mit einem Here-Document aus [Kapitel 4, Abschnitt 3.2](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/eingaben-umleiten.html#stufe-3-2). Tippe die erste Zeile, dann die zehn Zeilen der Tabelle und zum Schluss `ENDE`; die Shell zeigt vor jeder Folgezeile ein `>`:

```console
$ cat > laeufe.csv <<ENDE
> datum,name,km,minuten
> 2026-11-02,Anna,5.0,28
> 2026-11-02,Ben,10.5,62
> 2026-11-03,Clara,7.2,41
> 2026-11-04,Anna,6.4,35
> 2026-11-05,Ben,5.0,31
> 2026-11-06,Anna,12.0,70
> 2026-11-07,Clara,8.0,44
> 2026-11-08,Ben,21.1,128
> 2026-11-09,Anna,5.0,27
> ENDE
$ head -n 3 laeufe.csv
datum,name,km,minuten
2026-11-02,Anna,5.0,28
2026-11-02,Ben,10.5,62
```

Die Datei `laeufe.csv` hat eine Kopfzeile und neun Datensätze: neun Läufe von Anna, Ben und Clara zwischen dem 2. und dem 9. November 2026. Das Datum steht in der Form Jahr-Monat-Tag, damit es sich wie Text richtig sortieren lässt.

⁠**Kurz gesagt:** Eine CSV-Datei ist eine Tabelle als Text mit einem Datensatz je Zeile und Kommas zwischen den Feldern; die erste Zeile nennt oft die Spaltennamen.

:::hintergrund Warum CSV nicht überall gleich aussieht
Für CSV gibt es kein Gesetz, nur eine Beschreibung, die 2005 als RFC 4180 erschien und die verbreitete Praxis festhält. Danach darf ein Feld, das selbst ein Komma, ein Anführungszeichen oder ein Zeilenende enthält, in doppelte Anführungszeichen gesetzt werden, etwa `"Berg, Anna"`. Die einfachen Werkzeuge dieses Kapitels kennen diese Regel nicht; für sie ist jedes Komma ein Trennzeichen. Für Dateien mit solchen Feldern gibt es eigene Programme, die CSV vollständig verstehen. Tabellenprogramme mit deutscher Spracheinstellung trennen beim Speichern als CSV oft mit Semikolons, weil das Komma dort das Dezimalzeichen ist. Wer eine fremde CSV-Datei auswertet, sieht deshalb zuerst mit `head` hinein, welches Trennzeichen sie benutzt und ob Felder in Anführungszeichen stehen.
:::

### Das Zeilenende unter Windows

<span class="anker" id="stufe-1-4"></span>

CSV-Dateien kommen oft von einem Windows-Rechner, aus einem Tabellenprogramm oder einem Download. Solche Dateien sehen im Terminal ganz normal aus und verhalten sich trotzdem manchmal seltsam. Der Grund ist ein Zeichen, das man nicht sieht. Abbildung [2](#abb-2) zeigt es.

:::abbildung linux/k6zeilenende 2
Das Ende der Zeile `2026-11-02,Anna,5.0,28` als Bytes, oben in einer Linux-Datei, unten in einer Windows-Datei. Bis zur 8 sind beide gleich (grau). Danach folgt unter Linux nur das Zeilenende 10; unter Windows steht davor zusätzlich der Wagenrücklauf 13, der aufleuchtet. Für ein Programm, das bis zum Zeilenende liest, gehört er zum letzten Feld: Es liest `28` und ein unsichtbares Zeichen.
:::

:::definition Definition 1.3 (Wagenrücklauf, Windows-Zeilenende)
<span class="anker" id="satz-1-3"></span>

Der __Wagenrücklauf__ ist ein unsichtbares Zeichen mit dem Wert 13, in Programmen oft `\r` geschrieben. Windows schließt in Textdateien jede Zeile mit zwei Bytes ab, dem Wagenrücklauf und dem Zeilenende, also 13 und 10. Linux und die anderen Unix-Systeme benutzen nur das Zeilenende.
:::

Ein Linux-Programm hält den Wagenrücklauf für ein gewöhnliches Zeichen am Ende der Zeile. Deshalb gehört er zum letzten Feld eines Datensatzes und stört, sobald ein Werkzeug dieses Feld mit einem Wert vergleicht oder nach etwas sucht, das direkt vor dem Zeilenende stehen soll.

Eine kleine Datei mit Windows-Zeilenenden legst du mit `printf` an. Die Vorlage `'%s\r\n'` schreibt jedes Argument, einen Wagenrücklauf und ein Zeilenende; `printf` wendet sie auf jedes der drei Argumente an. Der Befehl `cat` mit der Option `-A` macht unsichtbare Zeichen sichtbar: Er schreibt den Wagenrücklauf als `^M` und setzt an jedes Zeilenende ein `$`.

```console
$ printf '%s\r\n' datum,name,km,minuten 2026-11-02,Anna,5.0,28 2026-11-02,Ben,10.5,62 > windows.csv
$ cat windows.csv
datum,name,km,minuten
2026-11-02,Anna,5.0,28
2026-11-02,Ben,10.5,62
$ cat -A windows.csv
datum,name,km,minuten^M$
2026-11-02,Anna,5.0,28^M$
2026-11-02,Ben,10.5,62^M$
```

Ohne `-A` sieht die Datei aus wie die ersten drei Zeilen von `laeufe.csv`. Erst `cat -A` verrät den Wagenrücklauf vor jedem Zeilenende. Für einen Vergleich speicherst du die ersten drei Zeilen des Lauftagebuchs in einer eigenen Datei und zählst die Bytes:

```console
$ head -n 3 laeufe.csv > drei.csv
$ wc -c drei.csv windows.csv
 68 drei.csv
 71 windows.csv
139 total
```

Drei Zeilen, drei Bytes mehr: ein Wagenrücklauf je Zeile.

::::beispiel Die Bytes einzeln
`od -c` aus [Kapitel 3, Abschnitt 4.1](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-ansehen.html#stufe-4-1) zeigt jedes Byte als Zeichen; den Wagenrücklauf schreibt es als `\r`:

```console
$ od -An -c windows.csv | head -n 2
   d   a   t   u   m   ,   n   a   m   e   ,   k   m   ,   m   i
   n   u   t   e   n  \r  \n   2   0   2   6   -   1   1   -   0
```

Nach `minuten` folgen `\r` und `\n`, dann beginnt die nächste Zeile. Und `file`? Es hält beide Dateien für CSV und verrät hier nichts:

```console
$ file laeufe.csv windows.csv
laeufe.csv:  CSV ASCII text
windows.csv: CSV ASCII text
```

Bei einer gewöhnlichen Textdatei, etwa einem kurzen Gruß, meldet `file` Windows-Zeilenenden dagegen mit dem Zusatz „with CRLF line terminators“. Verlass dich bei CSV-Dateien deshalb auf `cat -A`.
::::

⁠**Kurz gesagt:** Windows beendet Zeilen mit Wagenrücklauf und Zeilenende; der unsichtbare Wagenrücklauf wird unter Linux zum letzten Zeichen jeder Zeile, `cat -A` zeigt ihn als `^M`.

:::hintergrund Warum es zwei Zeichen gibt und Linux mit einem auskommt
Die Namen stammen von Fernschreibern, auf denen die ersten Rechner ihre Ausgaben druckten. Der Wagenrücklauf (englisch „carriage return“, kurz CR) schob den Druckkopf zurück an den Zeilenanfang, der Zeilenvorschub (englisch „line feed“, kurz LF, unser Zeilenende) drehte das Papier eine Zeile weiter. Für eine neue Zeile brauchte das Gerät beides. Windows hat diese Paarung von seinen Vorgängern übernommen und speichert sie in jeder Datei. Unix ging einen anderen Weg: In der Datei steht nur ein Zeichen, und erst der Treiber des Terminals macht beim Ausgeben daraus, was das Gerät braucht. Diese Übersetzung ist bis heute eine Einstellung des Terminals:

```console
$ stty -a | grep onlcr
opost -olcuc -ocrnl onlcr -onocr -onlret -ofdel nl0 cr0 tab0 bs0 vt0 ff0
```

`onlcr` ohne Minus davor heißt: Beim Ausgeben (o für „output“) wird aus jedem Zeilenende (nl für „newline“) ein Wagenrücklauf mit Zeilenende (cr für „carriage return“, dann nl). Die Dateien bleiben so kürzer und einfacher, und jedes Programm muss nur ein Zeichen als Zeilenende kennen.
:::

### Zeilen ab einer Stelle: tail -n +K und head -n -K

<span class="anker" id="stufe-1-5"></span>

Die Kopfzeile stört, sobald man zählen oder rechnen will: Sie ist kein Lauf. `head -n K` und `tail -n K` aus [Kapitel 3, Abschnitt 4.4](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-ansehen.html#stufe-4-4) greifen eine feste Zahl von Zeilen am Anfang oder am Ende. Gebraucht wird aber „alles ab Zeile 2“, egal wie lang die Datei ist. Abbildung [3](#abb-3) zeigt, wie ein Vorzeichen die Zählrichtung umdreht.

:::abbildung linux/k6ausschnitt 3
Die zehn Zeilen des Lauftagebuchs zweimal als Stapel. Links `tail -n +8`: Es zählt vom Anfang bis Zeile 8 und nimmt alles ab dort, die Zeilen 8 bis 10. Rechts `head -n -7`: Es zählt sieben Zeilen vom Ende her ab und nimmt alles davor, die Zeilen 1 bis 3.
:::

:::definition Definition 1.4 (tail -n +K, head -n -K)
<span class="anker" id="satz-1-4"></span>

`tail -n +K` schreibt alle Zeilen ab der Zeile Nummer $K$ bis zum Ende. `head -n -K` schreibt alle Zeilen außer den letzten $K$.
:::

Das Pluszeichen macht aus „die letzten $K$ Zeilen“ also „ab Zeile $K$“, das Minuszeichen aus „die ersten $K$ Zeilen“ „alle bis auf die letzten $K$“. `tail -n +2` ist damit der übliche Weg, eine Kopfzeile abzuschneiden.

::::beispiel Läufe zählen, Anfang und Ende
```console
$ wc -l laeufe.csv
10 laeufe.csv
$ tail -n +2 laeufe.csv | wc -l
9
$ tail -n +8 laeufe.csv
2026-11-07,Clara,8.0,44
2026-11-08,Ben,21.1,128
2026-11-09,Anna,5.0,27
$ head -n -7 laeufe.csv
datum,name,km,minuten
2026-11-02,Anna,5.0,28
2026-11-02,Ben,10.5,62
```

Die Datei hat zehn Zeilen, ohne Kopfzeile bleiben neun Läufe. `tail -n +8` liefert die Zeilen 8 bis 10, `head -n -7` die Zeilen 1 bis 3.
::::

⁠**Kurz gesagt:** `tail -n +K` beginnt bei Zeile $K$, `head -n -K` hört $K$ Zeilen vor dem Ende auf; `tail -n +2` entfernt eine Kopfzeile.

### Einer wachsenden Datei folgen: tail -f

<span class="anker" id="stufe-1-6"></span>

Manche Dateien wachsen, während man sie liest: Protokolle, in die ein Programm seine Meldungen schreibt, oder ein Tagebuch, in das jemand neue Einträge anhängt. Man möchte dann nicht immer wieder `tail` aufrufen, sondern sehen, was neu dazukommt, sobald es dazukommt. Abbildung [4](#abb-4) zeigt, was die Option dafür tut.

:::abbildung linux/k6tailf 4
Links eine Datei als Stapel von Zeilen, rechts das Terminal mit `tail -n 2 -f`. Zuerst erscheinen die letzten zwei Zeilen, dann wartet `tail`. Unten kommt eine neue Zeile an die Datei; sie erscheint sofort auch im Terminal. Erst Strg+C beendet das Warten.
:::

:::definition Definition 1.5 (tail -f)
<span class="anker" id="satz-1-5"></span>

`tail -f datei` schreibt zuerst wie gewohnt die letzten Zeilen der Datei. Danach endet es nicht, sondern wartet und schreibt alles, was später an die Datei angehängt wird, sobald es dort ankommt. Es läuft, bis man es mit Strg+C abbricht.
:::

Der Buchstabe steht für englisch „follow“, folgen. Damit das Lauftagebuch selbst unverändert bleibt, probierst du es an einer Kopie aus:

```console
$ cp laeufe.csv neu.csv
```

Starte im ersten Terminal `tail` mit den letzten zwei Zeilen. Öffne dann ein zweites Terminalfenster, wechsle dort mit `cd ~/linuxk6` ins Übungsverzeichnis und hänge einen neuen Lauf an:

```console
$ echo 2026-11-10,Clara,6.0,33 >> neu.csv
```

Im ersten Terminal erscheint die neue Zeile sofort unter den beiden alten. Danach beendest du `tail` mit Strg+C:

```console
$ tail -n 2 -f neu.csv
2026-11-08,Ben,21.1,128
2026-11-09,Anna,5.0,27
2026-11-10,Clara,6.0,33
^C
```

Die ersten beiden Zeilen standen schon in der Datei, die dritte kam aus dem zweiten Terminal. `neu.csv` hat jetzt einen Lauf mehr als `laeufe.csv`.

⁠**Kurz gesagt:** `tail -f` zeigt das Ende einer Datei und danach alles, was angehängt wird, bis Strg+C.

:::hintergrund Wie tail merkt, dass etwas dazukommt
Beide Fassungen von `tail` auf dem Testsystem bitten unter Linux den Kernel, ihnen Bescheid zu geben, sobald sich die Datei ändert; die Ausgabe kommt dann ohne Verzögerung. Wo das nicht geht, sieht die GNU-Fassung einmal pro Sekunde nach, ob die Datei länger geworden ist. Für Protokolldateien gibt es eine Feinheit: Viele Systeme benennen eine volle Protokolldatei in regelmäßigen Abständen um und beginnen eine neue unter dem alten Namen. `tail -f` folgt der Datei, die es geöffnet hat, und bleibt dann bei der umbenannten alten hängen. `tail -F` folgt dagegen dem Namen und öffnet die neue Datei, sobald sie auftaucht.
:::

### Aufgaben zu Abschnitt [1](#stufe-1)

<span class="anker" id="stufe-1-7"></span>

:::aufgabe Aufgabe 1 ★ Das Lauftagebuch vermessen
<span class="anker" id="aufg-1"></span>

(a) Wie viele Zeilen und wie viele Bytes hat `laeufe.csv`? Benutze einen einzigen Aufruf von `wc`. (b) Gib die Zeilen 4 bis 6 aus, einmal mit `head` vor `tail` und einmal umgekehrt. (c) Wie viele Bytes hätte die Datei, wenn sie Windows-Zeilenenden hätte? Begründe ohne Rechner.

:::loesung
```console
$ wc -l -c laeufe.csv
 10 232 laeufe.csv
$ head -n 6 laeufe.csv | tail -n 3
2026-11-03,Clara,7.2,41
2026-11-04,Anna,6.4,35
2026-11-05,Ben,5.0,31
$ tail -n +4 laeufe.csv | head -n 3
2026-11-03,Clara,7.2,41
2026-11-04,Anna,6.4,35
2026-11-05,Ben,5.0,31
```

(a) Zehn Zeilen und 232 Bytes; `wc` schreibt die Zahlen in der Reihenfolge Zeilen, Bytes, unabhängig von der Reihenfolge der Optionen. (b) Erster Weg: `head -n 6` behält die Zeilen 1 bis 6, `tail -n 3` davon die letzten drei, also 4 bis 6. Zweiter Weg: `tail -n +4` beginnt bei Zeile 4, `head -n 3` behält drei Zeilen. (c) Jede der zehn Zeilen bekäme einen Wagenrücklauf vor ihr Zeilenende, also ein Byte mehr: $232 + 10 = 242$ Bytes. So war es auch bei `drei.csv` und `windows.csv` in Unterabschnitt [1.4](#stufe-1-4): drei Zeilen, drei Bytes mehr.
:::
:::

:::aufgabe Aufgabe 2 ★★ Windows-Zeilenenden erkennen
<span class="anker" id="aufg-2"></span>

Lege mit `printf` eine Datei `gruss.txt` mit den beiden Zeilen `Hallo` und `Welt` im Windows-Format an. (a) Sage voraus, wie viele Bytes `wc -c` meldet. (b) Prüfe mit `cat -A` und `od -An -c`. (c) Was meldet `file` für diese Datei?

:::loesung
```console
$ printf 'Hallo\r\nWelt\r\n' > gruss.txt
$ wc -c gruss.txt
13 gruss.txt
$ cat -A gruss.txt
Hallo^M$
Welt^M$
$ od -An -c gruss.txt
   H   a   l   l   o  \r  \n   W   e   l   t  \r  \n
$ file gruss.txt
gruss.txt: ASCII text, with CRLF line terminators
```

(a) `Hallo` hat 5 Zeichen, `Welt` 4, jede Zeile endet mit zwei Bytes: $5 + 2 + 4 + 2 = 13$. (b) `cat -A` zeigt vor jedem `$` ein `^M`, `od` die Bytes `\r` und `\n` einzeln. (c) Bei dieser gewöhnlichen Textdatei nennt `file` das Windows-Zeilenende ausdrücklich, anders als bei der CSV-Datei in Unterabschnitt [1.4](#stufe-1-4).
:::
:::

:::aufgabe Aufgabe 3 ★★ Einer Datei folgen
<span class="anker" id="aufg-3"></span>

Kopiere `laeufe.csv` nach `probe.csv`. (a) Starte `tail -n 0 -f probe.csv`. Was erscheint sofort, und warum? (b) Hänge im zweiten Terminal zwei Läufe an. Was zeigt das erste Terminal? (c) Warum endet `tail -f` nicht von selbst, wenn das Ende der Datei erreicht ist, `tail` ohne `-f` dagegen schon?

:::loesung
Im ersten Terminal startest du `tail -n 0 -f probe.csv`, im zweiten hängst du zwei Läufe an:

```console
$ echo 2026-11-10,Ben,8.4,49 >> probe.csv
```

```console
$ echo 2026-11-10,Anna,5.0,26 >> probe.csv
```

Das erste Terminal zeigt danach, bis du Strg+C drückst:

```console
$ cp laeufe.csv probe.csv
$ tail -n 0 -f probe.csv
2026-11-10,Ben,8.4,49
2026-11-10,Anna,5.0,26
^C
```

(a) Sofort erscheint nichts: `-n 0` verlangt null der vorhandenen Zeilen. (b) Jede angehängte Zeile erscheint, sobald sie in der Datei steht. (c) `tail` ohne `-f` liest bis zum Ende der Datei, schreibt die letzten Zeilen und ist fertig. `tail -f` rechnet damit, dass am Ende noch etwas angehängt wird; das Ende der Datei ist für es nur der Stand von jetzt. Wann niemand mehr schreibt, kann es nicht wissen, deshalb beendet erst Strg+C das Warten.
:::
:::

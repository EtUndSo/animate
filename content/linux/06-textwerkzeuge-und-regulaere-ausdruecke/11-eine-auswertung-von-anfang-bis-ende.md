---
title: Eine Auswertung von Anfang bis Ende
pfad: Informatik / Linux und Kommandozeile / Textwerkzeuge und reguläre Ausdrücke
adresse: informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke
knoten: Kapitel 6: Textwerkzeuge und reguläre Ausdrücke
order: 6111100
summary: Jetzt steht der ganze Werkzeugkasten bereit.
tags: 
lang: de
---

<span class="anker" id="stufe-10"></span>

:::zweck
Jetzt steht der ganze Werkzeugkasten bereit. Dieser Abschnitt zeigt, welches Werkzeug für welche Teilfrage passt, wie man eine Auswertung Schritt für Schritt aufbaut, ohne sich zu verlaufen, und an einer berühmten Pipeline, wie wenig man für eine überraschend schwierige Frage braucht.
:::

### Welches Werkzeug wofür

<span class="anker" id="stufe-10-1"></span>

Eine Textdatei mit Datensätzen ist eine Tabelle. Die Werkzeuge dieses Kapitels unterscheiden sich darin, was sie aus dieser Tabelle machen. Abbildung [34](#abb-34) ordnet sie danach.

:::abbildung linux/k6werkzeuge 34
Das Lauftagebuch als Tabelle. `grep` und `sed -n` heben ganze Zeilen heraus; `cut` eine Spalte; `sort` ordnet die Zeilen neu; `tr` und `sed` verändern Zeichen in den Zellen; `uniq -c` und `awk` fassen viele Zeilen zu wenigen Ergebniszeilen zusammen. Jedes Werkzeug erscheint mit seiner Wirkung an derselben Tabelle.
:::

:::satz Satz 10.1 (Werkzeugwahl)
<span class="anker" id="satz-10-1"></span>

Zeilen nach Inhalt wählt man mit `grep`, nach Nummer mit `head`, `tail` oder `sed -n`. Spalten wählt man mit `cut` oder `awk`. Zeichen ersetzt `tr`, Teile von Zeilen `sed`. Ordnen erledigt `sort`, Zählen gleicher Zeilen `sort | uniq -c`. Rechnen mit Feldern und Sammeln je Gruppe erledigt `awk`.
:::

`awk` kann fast alles davon allein; trotzdem greift man für einfache Teilaufgaben zum einfachen Werkzeug, weil der Befehl kürzer und auf einen Blick lesbar ist.

⁠**Kurz gesagt:** Für jede Teilfrage gibt es ein passendes kleines Werkzeug; `awk` ist das vielseitigste, aber nicht immer das einfachste.

### Eine Pipeline Schritt für Schritt bauen

<span class="anker" id="stufe-10-2"></span>

Wer ist insgesamt am weitesten gelaufen, und wer am schnellsten? Für solche Fragen schreibt man die Pipeline nicht in einem Zug hin, sondern baut sie Stufe für Stufe auf und sieht nach jeder Stufe nach, ob das Zwischenergebnis stimmt.

:::satz Satz 10.2 (Schrittweise bauen)
<span class="anker" id="satz-10-2"></span>

Baue eine Auswertung Stufe für Stufe. Sieh dir nach jeder neuen Stufe das Zwischenergebnis an, bei langen Ausgaben mit `head`. Speichere ein Zwischenergebnis, das mehrere Fragen brauchen, in einer Datei.
:::

::::beispiel Die längste Gesamtstrecke und das schnellste Tempo
Schritt 1: ohne Kopfzeile, kurz hineinsehen.

```console
$ tail -n +2 laeufe.csv | head -n 3
2026-11-02,Anna,5.0,28
2026-11-02,Ben,10.5,62
2026-11-03,Clara,7.2,41
```

Schritt 2: je Person Kilometer und Minuten summieren, geordnet in einer Datei speichern.

```console
$ tail -n +2 laeufe.csv | awk -F, '{km[$2] += $3; min[$2] += $4} END {for (p in km) print p, km[p], min[p]}' | sort > summen.txt
$ cat summen.txt
Anna 28.4 160
Ben 36.6 221
Clara 15.2 85
```

Schritt 3: das Tempo, Minuten je Kilometer. `summen.txt` trennt mit Leerzeichen, also ohne `-F`.

```console
$ awk '{printf "%s %.1f %.2f\n", $1, $2, $3 / $2}' summen.txt > tempo.txt
$ cat tempo.txt
Anna 28.4 5.63
Ben 36.6 6.04
Clara 15.2 5.59
```

Schritt 4: zweimal sortieren, je nach Frage.

```console
$ sort -k2,2nr tempo.txt | head -n 1
Ben 36.6 6.04
$ sort -k3,3n tempo.txt | head -n 1
Clara 15.2 5.59
```

Ben ist mit 36,6 km am weitesten gelaufen, Clara war mit 5,59 Minuten je Kilometer im Mittel am schnellsten. Ohne `-t` trennt `sort` an Leerzeichen, passend zu `tempo.txt`.
::::

⁠**Kurz gesagt:** Eine Pipeline wächst Stufe für Stufe, jedes Zwischenergebnis wird angesehen, und was mehrfach gebraucht wird, landet in einer Datei.

### Wörter zählen: eine berühmte Pipeline

<span class="anker" id="stufe-10-3"></span>

Welche Wörter kommen in einem Text am häufigsten vor? Die Frage klingt nach einem eigenen Programm mit Wörterbuch und Zählern. Mit den Werkzeugen dieses Kapitels genügt eine Zeile. Als Text dient die Lizenz GPL-3 aus [Kapitel 3, Abschnitt 4.3](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-ansehen.html#stufe-4-3), die auf jedem Ubuntu liegt.

::::beispiel Die häufigsten Wörter der Lizenz
Zuerst muss aus dem Text eine Liste mit einem Wort je Zeile werden. `tr` mit `-c` nimmt dafür das Gegenteil der ersten Menge, also alles außer Buchstaben, und `-s` fasst Wiederholungen zusammen. Jede Folge von Zeichen, die keine Buchstaben sind, wird so zu einem einzigen Zeilenende:

```console
$ tr -cs 'A-Za-z' '\n' < /usr/share/common-licenses/GPL-3 | head -n 4

GNU
GENERAL
PUBLIC
```

Die erste Zeile ist leer, weil die Lizenz mit Leerzeichen beginnt. Dann folgen die Wörter, eines je Zeile. Der Rest ist die Häufigkeitstabelle aus Unterabschnitt [3.6](sortieren-und-zahlen-sort-und-uniq.html#stufe-3-6), mit einem `tr`, das vorher alle Großbuchstaben klein macht:

```console
$ tr -cs 'A-Za-z' '\n' < /usr/share/common-licenses/GPL-3 | tr A-Z a-z | sort | uniq -c | sort -rn | head -n 5
    345 the
    221 of
    192 to
    184 a
    151 or
```

`the` steht 345-mal in der Lizenz. Jede Stufe dieser Pipeline erledigt eine kleine Aufgabe: Wörter trennen, klein schreiben, ordnen, zählen, nach Anzahl ordnen, die ersten fünf behalten. Keine weiß etwas von Wörtern oder Lizenzen.
::::

⁠**Kurz gesagt:** Sechs kleine Werkzeuge in einer Pipeline beantworten eine Frage, für die man sonst ein ganzes Programm schreiben würde.

:::hintergrund Sechs Zeilen gegen ein ganzes Programm
Diese Pipeline ist berühmt. Jon Bentley schrieb in der Fachzeitschrift Communications of the ACM die Kolumne „Programming Pearls“. Für eine Folge im Jahr 1986 bat er den Informatiker Donald Knuth um ein Programm, das die $k$ häufigsten Wörter eines Texts ausgibt. Knuth schrieb ein sorgfältig erklärtes, mehrere Seiten langes Programm mit einer ausgeklügelten Datenstruktur, ganz von Grund auf. Doug McIlroy, von dem die Idee der Pipe aus [Kapitel 4](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/stroeme-umleitung-pipes-und-exit-status.html) stammt, sollte es begutachten. Er würdigte die sorgfältige Darstellung und stellte daneben sechs Zeilen Shell, im Wesentlichen die Pipeline oben, nur mit `sed` und dem Befehl `q` statt `head` am Ende. Seine Pointe war die Unix-Philosophie aus [Kapitel 4, Abschnitt 4.5](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/pipes-und-filter.html#stufe-4-5): Statt alles neu zu programmieren, verbindet man vorhandene kleine Werkzeuge, die Text lesen und schreiben, und ist damit oft in wenigen Minuten fertig.
:::

**Zum Weiterüben.** Die frei zugängliche Übungsplattform pwn.college bietet unter dem Namen „Linux Luminarium“ kleine Aufgaben im Browser an; das Modul „Data Manipulation“ passt zu diesem Kapitel. Es läuft auf einem fremden Rechner, nicht auf deinem eigenen.

### Aufgaben zu Abschnitt [10](#stufe-10)

<span class="anker" id="stufe-10-4"></span>

:::aufgabe Aufgabe 28 ★★★ Eine eigene Auswertung
<span class="anker" id="aufg-28"></span>

(a) An welchem Tag wurden insgesamt die meisten Kilometer gelaufen, und an welchem die zweitmeisten? (b) An welchem Tag liefen mehrere Personen? Antworte jeweils mit einer Pipeline und baue sie Stufe für Stufe auf.

:::loesung
```console
$ awk -F, 'NR > 1 {t[$1] += $3} END {for (d in t) print d, t[d]}' laeufe.csv | sort -k2,2nr | head -n 2
2026-11-08 21.1
2026-11-02 15.5
```

(a) Stufe für Stufe: zuerst das `awk`-Programm allein, das je Datum die Strecken summiert und eine Zeile je Tag ausgibt; dann `sort -k2,2nr` nach der Summe absteigend; zuletzt `head -n 2`. Am 8. November kamen mit Bens Halbmarathon 21,1 km zusammen, am 2. November mit zwei Läufen $5{,}0 + 10{,}5 = 15{,}5$ km.

```console
$ tail -n +2 laeufe.csv | cut -d, -f1 | sort | uniq -d
2026-11-02
```

(b) Die Daten aller Läufe, geordnet; `uniq -d` schreibt nur Werte, die mehrfach hintereinander vorkommen. Nur am 2. November liefen zwei Personen.
:::
:::

:::aufgabe Aufgabe 29 ★★ Wörter in einer anderen Lizenz
<span class="anker" id="aufg-29"></span>

In `/usr/share/common-licenses/Apache-2.0` liegt eine weitere Lizenz. (a) Welches sind ihre drei häufigsten Wörter? (b) Wie viele verschiedene Wörter enthält sie? Achte darauf, was die leere erste Zeile dabei ausmacht.

:::loesung
```console
$ tr -cs 'A-Za-z' '\n' < /usr/share/common-licenses/Apache-2.0 | tr A-Z a-z | sort | uniq -c | sort -rn | head -n 3
    100 the
     69 or
     67 of
$ tr -cs 'A-Za-z' '\n' < /usr/share/common-licenses/Apache-2.0 | tr A-Z a-z | sort -u | wc -l
442
$ tr -cs 'A-Za-z' '\n' < /usr/share/common-licenses/Apache-2.0 | head -n 2 | cat -A
$
Apache$
```

(a) Dieselbe Pipeline wie in Unterabschnitt [10.3](#stufe-10-3), nur mit einer anderen Datei: `the`, `or` und `of`. (b) `sort -u` lässt jedes Wort einmal übrig, `wc -l` zählt 442 Zeilen. Wie bei der GPL beginnt auch diese Lizenz mit Leerzeichen, und die erste Zeile der Wortliste ist leer, wie `cat -A` zeigt; diese leere Zeile ist kein Wort. Die Lizenz enthält also 441 verschiedene Wörter.
:::
:::

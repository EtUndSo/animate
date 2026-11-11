---
title: Nummerieren, Zahlenfolgen und Unterschiede: nl, seq und diff
pfad: Informatik / Linux und Kommandozeile / Textwerkzeuge und reguläre Ausdrücke
adresse: informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke
knoten: Kapitel 6: Textwerkzeuge und reguläre Ausdrücke
order: 6110500
summary: Drei kleine Werkzeuge runden den Werkzeugkasten ab: eines nummeriert Zeilen, eines erzeugt Folgen von Zahlen, und eines zeigt, worin sich zwei Dateien unterscheiden.
tags: nl, seq, diff
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Drei kleine Werkzeuge runden den Werkzeugkasten ab: eines nummeriert Zeilen, eines erzeugt Folgen von Zahlen, und eines zeigt, worin sich zwei Dateien unterscheiden.
:::

### Zeilen nummerieren: nl

<span class="anker" id="stufe-4-1"></span>

Wer mit anderen über eine Datei spricht, will auf Zeilen zeigen können: „In Zeile 7 steht ein Tippfehler.“ Dafür braucht man die Nummern vor den Zeilen.

:::definition Definition 4.1 (nl)
<span class="anker" id="satz-4-1"></span>

Der Befehl __nl__ schreibt jede Zeile seiner Eingabe mit einer laufenden Nummer davor aus, getrennt durch einen Tabulator. Ohne Option nummeriert er nur Zeilen, die nicht leer sind; mit `-ba` nummeriert er alle.
:::

Der Name steht für englisch „number lines“.

::::beispiel Nummern mit und ohne leere Zeilen
```console
$ nl laeufe.csv | head -n 3
     1  datum,name,km,minuten
     2  2026-11-02,Anna,5.0,28
     3  2026-11-02,Ben,10.5,62
```

Die Nummern stehen rechtsbündig in einer sechs Zeichen breiten Spalte. Eine leere Zeile bekommt ohne Option keine Nummer:

```console
$ printf '%s\n' Anna '' Ben | nl
     1  Anna

     2  Ben
$ printf '%s\n' Anna '' Ben | nl -ba
     1  Anna
     2
     3  Ben
```

`printf` hat aus dem leeren Argument `''` eine leere Zeile gemacht. Ohne Option überspringt `nl` sie beim Zählen, mit `-ba` nicht.
::::

⁠**Kurz gesagt:** `nl` setzt Zeilennummern vor die Zeilen; leere Zeilen zählt es nur mit `-ba`.

### Zahlenfolgen erzeugen: seq

<span class="anker" id="stufe-4-2"></span>

Zum Ausprobieren braucht man oft eine Folge von Zahlen: die Tage eines Monats, die Zahlen von 1 bis 100, Kilometermarken im Abstand von 0,5. Die Klammererweiterung aus [Kapitel 5, Abschnitt 1.6](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/expansion-muster-klammern-und-tilde.html#stufe-1-6) kann das nur mit ganzen Zahlen, und sie geschieht, bevor Variablen eingesetzt werden. Ein Programm, das Zahlen in seine Standardausgabe schreibt, hat beide Grenzen nicht. Abbildung [13](#abb-13) zeigt, wie es eine Folge bildet.

:::abbildung linux/k6seq 13
Ein Zahlenstrahl von 0 bis 10. `seq 1 4 10` setzt eine Marke bei 1, springt um 4 weiter zu 5 und zu 9; der nächste Sprung landete bei 13, jenseits der 10, und bleibt grau. Darunter `seq 0 0.5 2` mit Marken im Abstand 0,5 bis genau 2.
:::

:::definition Definition 4.2 (seq)
<span class="anker" id="satz-4-2"></span>

Der Befehl __seq__ schreibt eine Folge von Zahlen, eine je Zeile. `seq ende` zählt von 1 bis `ende`, `seq anfang ende` von `anfang` bis `ende`, `seq anfang schritt ende` in Schritten der angegebenen Größe. Die Folge endet mit der letzten Zahl, die `ende` nicht überschreitet. `-s` legt ein anderes Trennzeichen als das Zeilenende fest, `-w` füllt mit führenden Nullen auf gleiche Breite auf.
:::

::::beispiel Folgen
```console
$ seq 3
1
2
3
$ seq -s' ' 2 2 10
2 4 6 8 10
$ seq -s' ' 0 0.5 2
0.0 0.5 1.0 1.5 2.0
$ seq -w -s' ' 8 11
08 09 10 11
$ seq -s' ' 1 4 10
1 5 9
```

Mit einem Schritt von 0,5 schreibt `seq` alle Zahlen mit einer Nachkommastelle. Die letzte Folge endet bei 9, denn 13 läge über 10.
::::

::::beispiel [Zweites Beispiel] Eine Grenze aus einer Variablen
[Kapitel 5, Abschnitt 3.9](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/worttrennung-und-quoting.html#stufe-3-9) hat gezeigt, dass `{1..$n}` nicht funktioniert, weil die Klammererweiterung vor der Parametererweiterung kommt. `seq` bekommt die Grenze dagegen als gewöhnliches Argument, nachdem die Shell `$n` eingesetzt hat:

```console
$ n=5
$ echo {1..$n}
{1..5}
$ seq -s' ' 1 $n
1 2 3 4 5
```
::::

⁠**Kurz gesagt:** `seq anfang schritt ende` schreibt eine Zahlenfolge, auch mit Kommazahlen und Grenzen aus Variablen.

### Unterschiede finden: diff

<span class="anker" id="stufe-4-3"></span>

Zwei Fassungen einer Datei sehen fast gleich aus: eine ältere und eine neuere, eine eigene und eine aus dem Netz. Zeile für Zeile mit dem Auge zu vergleichen, ist mühsam und fehleranfällig. Abbildung [14](#abb-14) zeigt, was ein Werkzeug stattdessen meldet.

:::abbildung linux/k6diff 14
Links die ersten fünf Zeilen des Lauftagebuchs, rechts dieselben fünf Zeilen mit kleinem b in `ben`. Gleiche Zeilen werden durch graue Linien verbunden. Nur Zeile 3 unterscheidet sich, `Ben` gegen `ben`; sie leuchtet auf beiden Seiten auf. Darunter erscheint die Meldung von `diff`: `3c3`, die alte Zeile mit `<`, drei Striche, die neue Zeile mit `>`.
:::

:::definition Definition 4.3 (diff)
<span class="anker" id="satz-4-3"></span>

Der Befehl __diff__ vergleicht zwei Textdateien Zeile für Zeile und gibt aus, was man an der ersten ändern müsste, um die zweite zu erhalten. Jede Änderung beginnt mit einer Zeile aus Zeilennummern und einem Buchstaben: `a` für anfügen, `c` für ändern, `d` für löschen. Darunter stehen die betroffenen Zeilen der ersten Datei mit `<` davor und die der zweiten mit `>`. Der Exit-Status ist 0 bei gleichen Dateien, 1 bei Unterschieden und 2 bei einem Fehler.
:::

Links vom Buchstaben steht die Zeilennummer in der ersten Datei, rechts die in der zweiten; ein Bereich wird mit Komma geschrieben, `6,10`. Sind die Dateien gleich, schreibt `diff` nichts.

Für die Vergleiche legst du zwei kürzere Dateien an: `kurz.csv` mit den ersten fünf Zeilen des Lauftagebuchs und `klein.csv`, in der zusätzlich jedes große B klein geschrieben ist:

```console
$ head -n 5 laeufe.csv > kurz.csv
$ head -n 5 laeufe.csv | tr B b > klein.csv
```

::::beispiel Anfügen, löschen, ändern
`neu.csv` aus Unterabschnitt [1.6](textdaten-datensatze-felder-und-zeilenenden.html#stufe-1-6) hat einen Lauf mehr als `laeufe.csv`:

```console
$ diff laeufe.csv neu.csv
10a11
> 2026-11-10,Clara,6.0,33
$ echo $?
1
$ diff laeufe.csv laeufe.csv
$ echo $?
0
```

`10a11`: Hinter Zeile 10 der ersten Datei ist anzufügen, was in der zweiten Zeile 11 ist. Nun das Lauftagebuch gegen seine ersten fünf Zeilen:

```console
$ diff laeufe.csv kurz.csv
6,10d5
< 2026-11-05,Ben,5.0,31
< 2026-11-06,Anna,12.0,70
< 2026-11-07,Clara,8.0,44
< 2026-11-08,Ben,21.1,128
< 2026-11-09,Anna,5.0,27
```

`6,10d5`: Die Zeilen 6 bis 10 der ersten Datei sind zu löschen; danach stimmt sie mit der zweiten bis zu deren Zeile 5 überein. Zuletzt die beiden kurzen Dateien:

```console
$ diff kurz.csv klein.csv
3c3
< 2026-11-02,Ben,10.5,62
---
> 2026-11-02,ben,10.5,62
```

`3c3`: Zeile 3 ist zu ändern; die drei Striche trennen die alte Fassung von der neuen.
::::

⁠**Kurz gesagt:** `diff a b` zeigt mit `a`, `c` und `d`, welche Zeilen man in `a` anfügen, ändern oder löschen müsste, um `b` zu erhalten; der Exit-Status sagt, ob es Unterschiede gibt.

:::hintergrund Das Format für Änderungsvorschläge: diff -u
Mit `-u` schreibt `diff` ein ausführlicheres Format, das Entwickler zum Austausch von Änderungen benutzen:

```console
$ diff -u kurz.csv klein.csv
--- kurz.csv    2026-11-10 11:10:24.238033361 +0100
+++ klein.csv   2026-11-10 11:10:24.842034058 +0100
@@ -1,5 +1,5 @@
 datum,name,km,minuten
 2026-11-02,Anna,5.0,28
-2026-11-02,Ben,10.5,62
+2026-11-02,ben,10.5,62
 2026-11-03,Clara,7.2,41
 2026-11-04,Anna,6.4,35
```

Die Kopfzeilen nennen beide Dateien mit ihrer Änderungszeit. `@@ -1,5 +1,5 @@` heißt: fünf Zeilen ab Zeile 1 in beiden Dateien. Zeilen mit `-` fallen weg, Zeilen mit `+` kommen hinzu, Zeilen mit einem Leerzeichen am Anfang stehen zur Orientierung dabei. Das Programm `patch` kann einen solchen Unterschied auf eine andere Kopie der ersten Datei anwenden. So schicken Entwickler einander Änderungen, statt ganze Dateien zu verschicken.
:::

### Aufgaben zu Abschnitt [4](#stufe-4)

<span class="anker" id="stufe-4-4"></span>

:::aufgabe Aufgabe 11 ★★ Zahlen erzeugen und nummerieren
<span class="anker" id="aufg-11"></span>

(a) Was gibt `seq -s+ 10` aus? (b) Berechne mit `seq` und der Arithmetik der Shell die Summe der Zahlen von 1 bis 100, und prüfe das Ergebnis mit der Formel $n(n+1)/2$. (c) Nummeriere die Zeilen `Anna`, eine leere Zeile und `Ben` mit `cat -n`. Mit welcher Form von `nl` stimmt das Ergebnis überein?

:::loesung
```console
$ seq -s+ 10
1+2+3+4+5+6+7+8+9+10
$ echo $(( $(seq -s+ 100) ))
5050
$ printf '%s\n' Anna '' Ben | cat -n
     1  Anna
     2
     3  Ben
```

(a) Die Zahlen von 1 bis 10, getrennt durch Pluszeichen statt Zeilenenden. (b) Dieselbe Rechnung bis 100 setzt die Befehlsersetzung in die Arithmetik ein: 5050. Die Formel liefert $100 \cdot 101 / 2 = 5050$. (c) `cat -n` nummeriert jede Zeile, auch die leere; das entspricht `nl -ba`, nicht `nl` ohne Option.
:::
:::

:::aufgabe Aufgabe 12 ★★ Was hat sich geändert?
<span class="anker" id="aufg-12"></span>

Lege mit `printf` eine Einkaufsliste `liste1.txt` mit Milch, Brot, Äpfel und eine `liste2.txt` mit Milch, Butter, Äpfel, Kaffee an, je ein Eintrag pro Zeile. (a) Sage voraus, was `diff liste1.txt liste2.txt` ausgibt und welchen Exit-Status es meldet. (b) Welchen Exit-Status meldet `diff`, wenn die zweite Datei fehlt?

:::loesung
```console
$ printf '%s\n' Milch Brot Äpfel > liste1.txt
$ printf '%s\n' Milch Butter Äpfel Kaffee > liste2.txt
$ diff liste1.txt liste2.txt
2c2
< Brot
---
> Butter
3a4
> Kaffee
$ echo $?
1
$ diff liste1.txt fehlt.txt
diff: fehlt.txt: No such file or directory
$ echo $?
2
```

(a) Zeile 2 ist zu ändern, Brot wird Butter; hinter Zeile 3 ist anzufügen, was in der zweiten Liste Zeile 4 ist, Kaffee. Die Dateien sind verschieden, der Exit-Status ist 1. (b) Fehlt eine Datei, ist das ein Fehler: Exit-Status 2 und eine Meldung auf der Fehlerausgabe.
:::
:::

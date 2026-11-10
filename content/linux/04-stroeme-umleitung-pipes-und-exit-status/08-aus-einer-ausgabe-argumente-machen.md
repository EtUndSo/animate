---
title: Aus einer Ausgabe Argumente machen
pfad: Informatik / Linux und Kommandozeile / Ströme, Umleitung, Pipes und Exit-Status
adresse: informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status
knoten: Kapitel 4: Ströme, Umleitung, Pipes und Exit-Status
order: 6090800
summary: Eine Pipe liefert Daten an die Standardeingabe.
tags: xargs, Grenze der Argumentliste
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Eine Pipe liefert Daten an die Standardeingabe. Manche Programme lesen ihre Standardeingabe aber nicht, sondern erwarten Dateinamen als Argumente. Dieser Abschnitt zeigt, wie man eine Liste von Namen aus einer Pipe in Argumente verwandelt, wie man das mit Namen schafft, die Leerzeichen enthalten, und wie `find` seine Treffer selbst an einen Befehl übergibt.
:::

### Strom oder Argument

<span class="anker" id="stufe-7-1"></span>

Liefert eine Pipe eine Liste von Dateinamen, liegt der Gedanke nahe, sie direkt an `rm` oder `wc` weiterzureichen. Das geht schief, und zwar auf zwei verschiedene Arten. Abbildung [26](#abb-26) zeigt, warum: Ein Prozess bekommt Daten auf zwei getrennten Wegen.

:::abbildung linux/k4stromargument 26
Zwei getrennte Wege in einen Prozess: Die Argumente legt die Shell beim Start fest, die Standardeingabe ist ein Strom, der danach fließt. Bei `echo probe2.txt | rm` kommt der Name im Strom an, die Argumentliste von `rm` bleibt leer. Bei `echo einkauf.txt | wc -l` liest `wc` den Namen als eine Zeile Daten.
:::

:::satz Satz 7.1 (Strom und Argument)
<span class="anker" id="satz-7-1"></span>

Eine Pipe verbindet Ströme, keine Argumente. Was durch die Pipe kommt, steht in der Standardeingabe des nächsten Programms und nie in seiner Argumentliste. Ein Programm, das seine Standardeingabe nicht liest, sieht davon nichts; ein Filter behandelt es als Daten, nicht als Dateinamen.
:::

::::beispiel Zwei Arten, aneinander vorbeizureden
```console
$ echo probe2.txt | rm
rm: missing operand
Try 'rm --help' for more information.
$ echo einkauf.txt | wc -l
1
```

`rm` liest seine Standardeingabe nicht, bekam kein Argument und beschwert sich, dass ihm der Name fehlt. `wc -l` hat seine Standardeingabe gelesen und darin eine Zeile gezählt, nämlich die Zeile `einkauf.txt`; die Datei selbst hat es nie geöffnet. Sie hat fünf Zeilen.
::::

⁠**Kurz gesagt:** Was durch eine Pipe kommt, ist Eingabe, kein Argument; Programme ohne Eingabe sehen es nicht, Filter halten es für Daten.

### Der Befehl xargs

<span class="anker" id="stufe-7-2"></span>

Zwischen Pipe und Programm fehlt also ein Übersetzer, der die Wörter aus dem Strom nimmt und sie als Argumente an das Programm hängt. Abbildung [27](#abb-27) zeigt ihn bei der Arbeit.

:::abbildung linux/k4xargs 27
`xargs` als Übersetzer: Aus der Standardeingabe kommen die Wörter `einkauf.txt` und `obst.txt`. `xargs` hängt sie an die Befehlszeile `wc -l` an und startet `wc -l einkauf.txt obst.txt` als neuen Prozess.
:::

:::definition Definition 7.2 (xargs)
<span class="anker" id="satz-7-2"></span>

Der Befehl __xargs__ liest seine Standardeingabe und zerlegt sie an Leerzeichen, Tabulatoren und Zeilenenden in Wörter. Dann startet er den Befehl, der ihm als Argumente folgt, und hängt diese Wörter als zusätzliche Argumente hinten an. Ohne Befehl nimmt er `echo`.
:::

::::beispiel Zwei Dateien zählen
```console
$ echo einkauf.txt obst.txt | xargs wc -l
 5 einkauf.txt
 7 obst.txt
12 total
```

`xargs` hat `wc -l einkauf.txt obst.txt` gestartet; `wc` hat beide Dateien geöffnet und ihre Zeilen gezählt.
::::

::::beispiel [Zweites Beispiel] Alle Textdateien, die find findet
Erst mit `find` ([Kapitel 3, Abschnitt 10.1](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-finden-und-platz-messen.html#stufe-10-1)) zeigt `xargs`, wozu es gut ist: Die Liste der Namen entsteht beim Suchen, niemand muss sie tippen.

```console
$ find . -name "*.txt" | xargs wc -l
  5 ./probe.txt
  7 ./obst.txt
  0 ./leer.txt
...
  5 ./einkauf.txt
  2 ./alles.txt
  2 ./beides.txt
 54 total
```

`find` schreibt jeden Treffer in eine Zeile, `xargs` macht aus allen Zeilen Argumente für einen einzigen Aufruf von `wc -l`. Die Reihenfolge ist die, in der `find` die Einträge antrifft.
::::

⁠**Kurz gesagt:** `xargs befehl` macht aus den Wörtern seiner Standardeingabe Argumente für den Befehl.

### Portionen: xargs -n und die Grenze der Argumentliste

<span class="anker" id="stufe-7-3"></span>

Manche Befehle nehmen nur ein Argument auf einmal, und kein Befehl verträgt beliebig viele: Für alle Argumente eines Programmstarts zusammen hat der Kernel eine Obergrenze. `xargs` kann die Wörter deshalb in Portionen aufteilen und den Befehl mehrmals starten. Abbildung [28](#abb-28) zeigt das.

:::abbildung linux/k4portionen 28
Drei Wörter, zwei Arten zu portionieren. Oben ohne `-n`: ein Aufruf mit allen drei Wörtern. Unten mit `-n 1`: drei Aufrufe mit je einem Wort.
:::

:::definition Definition 7.3 (Grenze der Argumentliste, xargs -n)
<span class="anker" id="satz-7-3"></span>

Der Kernel begrenzt, wie viele Bytes alle Argumente eines Programmstarts zusammen haben dürfen; `getconf ARG_MAX` zeigt diese __Grenze der Argumentliste__. `xargs` hält sie von selbst ein und startet den Befehl so oft wie nötig. Mit `-n zahl` übergibt es höchstens `zahl` Wörter pro Aufruf.
:::

In die Grenze zählen neben den Argumenten noch einige weitere Angaben, die jedes Programm beim Start mitbekommt. Scheitert ein Programmstart an der Grenze, meldet die Shell „Argument list too long“.

::::beispiel Ein Aufruf oder drei
```console
$ echo Apfel Birne Kiwi | xargs -n 1 echo Obst:
Obst: Apfel
Obst: Birne
Obst: Kiwi
$ echo Apfel Birne Kiwi | xargs echo Obst:
Obst: Apfel Birne Kiwi
```

Mit `-n 1` hat `xargs` dreimal `echo Obst:` gestartet, jedes Mal mit einem Wort; ohne `-n` einmal mit allen dreien.
::::

::::beispiel [Zweites Beispiel] Wie groß die Grenze ist
```console
$ getconf ARG_MAX
2097152
```

Das sind $2\,097\,152$ Bytes, also genau 2 MiB. Die tausend Namen aus `/usr/bin` brauchen davon nur einen kleinen Teil; bei Hunderttausenden von Dateien wird die Grenze aber schnell erreicht.
::::

⁠**Kurz gesagt:** Für die Argumente eines Programmstarts gibt es eine Obergrenze; `xargs` verteilt die Wörter von selbst auf mehrere Aufrufe, mit `-n` auf Portionen fester Größe.

:::hintergrund Woher die Grenze kommt
Beim Laden eines Programms mit `exec` kopiert der Kernel alle Argumente in den Speicher des Prozesses, und zwar in den Bereich, der dem Programm auch für seine laufende Arbeit dient, den sogenannten Stapel. Damit für diese Arbeit genug Platz bleibt, dürfen die Argumente unter Linux höchstens ein Viertel des Stapels belegen. Der Stapel ist auf dem Testsystem 8 MiB groß, ein Viertel davon sind 2 MiB, genau der Wert, den `getconf ARG_MAX` zeigt. Wer den Stapel größer einstellt, darf auch mehr Argumente übergeben, allerdings nicht beliebig viele.
:::

### Namen mit Leerzeichen: das Nullbyte als Trenner

<span class="anker" id="stufe-7-4"></span>

`xargs` trennt die Wörter an Leerzeichen. Ein Dateiname wie `mein foto.jpg` zerfällt dabei in zwei Wörter, und `xargs` übergibt zwei Namen, die es beide nicht gibt. Gebraucht wird ein Trennzeichen, das in Dateinamen nie vorkommt. Abbildung [29](#abb-29) zeigt den Unterschied.

:::abbildung linux/k4leerzeichen 29
Oben trennt `xargs` an Leerzeichen und Zeilenenden: Aus `./mein foto.jpg` werden die zwei falschen Namen `./mein` und `foto.jpg`. Unten stehen Nullbytes zwischen den Namen, und `xargs -0` trennt nur dort: Beide Namen bleiben ganz.
:::

:::definition Definition 7.4 (-print0 und xargs -0)
<span class="anker" id="satz-7-4"></span>

Die Aktion `-print0` von `find` schreibt hinter jeden Treffer ein Nullbyte, also das Byte mit dem Wert 0, statt eines Zeilenendes. Die Option `-0` lässt `xargs` seine Eingabe nur an Nullbytes zerlegen; Leerzeichen und Zeilenenden gehören dann zum Namen.
:::

Das funktioniert immer, weil ein Dateiname alle Zeichen enthalten darf außer dem Schrägstrich und dem Nullbyte ([Kapitel 3, Abschnitt 3.7](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/den-inhalt-eines-verzeichnisses-anzeigen.html#stufe-3-7)). Das Nullbyte kann deshalb nie mitten in einem Namen stehen.

::::beispiel Ein Urlaubsfoto mit Leerzeichen
```console
$ touch "mein foto.jpg" urlaub.jpg
$ find . -name "*.jpg" | xargs ls
ls: cannot access './mein': No such file or directory
ls: cannot access 'foto.jpg': No such file or directory
./urlaub.jpg
$ find . -name "*.jpg" -print0 | xargs -0 ls
'./mein foto.jpg'   ./urlaub.jpg
```

Beim ersten Versuch bekam `ls` drei Namen, von denen es zwei nicht gibt. Beim zweiten bekam es die beiden richtigen; die Anführungszeichen hat `ls` bei der Anzeige selbst hinzugefügt, damit man sieht, dass das Leerzeichen zum Namen gehört.
::::

Ohne `-0` deutet `xargs` außerdem Anführungszeichen und den umgekehrten Schrägstrich in seiner Eingabe als Zeichen, die das Zerlegen verhindern sollen. Ein Name mit einem einzelnen Apostroph bringt es deshalb ganz aus dem Takt:

```console
$ echo "Gabi's Café.jpg" | xargs ls
xargs: unmatched single quote; by default quotes are special to xargs unless you use the -0 option
```

`xargs` hat den Apostroph für den Anfang eines Abschnitts in Anführungszeichen gehalten, dessen Ende fehlt, und `ls` gar nicht erst gestartet. Mit `-print0` und `-0` gibt es auch dieses Problem nicht.

⁠**Kurz gesagt:** Mit `find -print0` und `xargs -0` trennt das Nullbyte die Namen, und Leerzeichen bleiben Teil des Namens.

:::warnung xargs mit rm nur mit -print0 und -0
Bei `rm` kann das Zerlegen an Leerzeichen gefährlich werden: Wird aus `alte liste.txt` das Wort `liste.txt`, löscht `rm` eine Datei dieses Namens, falls es sie gibt, und zwar eine ganz andere als gemeint. Wer Treffer von `find` an `rm` gibt, benutzt deshalb immer `-print0` und `-0` und probiert den Befehl vorher mit `ls` statt `rm` aus.
:::

### Der Weg ohne Pipe: find -exec

<span class="anker" id="stufe-7-5"></span>

`find` kann seine Treffer auch selbst an einen Befehl übergeben, ohne Pipe und ohne `xargs`. [Kapitel 3, Abschnitt 10.6](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-finden-und-platz-messen.html#stufe-10-6) hat schon Aktionen wie `-print` und `-delete` gezeigt; eine weitere startet einen beliebigen Befehl.

:::definition Definition 7.5 (-exec)
<span class="anker" id="satz-7-5"></span>

Die Aktion `-exec befehl {} \;` von `find` startet den Befehl für jeden Treffer einmal und setzt den Namen des Treffers an die Stelle von `{}`. Die Aktion `-exec befehl {} +` sammelt die Namen wie `xargs` und startet den Befehl so selten wie möglich, mit vielen Namen auf einmal; `{}` muss dabei direkt vor dem `+` stehen.
:::

Das Semikolon am Ende braucht einen umgekehrten Schrägstrich davor: Ohne ihn hielte die Shell es für das Semikolon aus Unterabschnitt [6.1](befehle-verketten.html#stufe-6-1) und gäbe es `find` gar nicht weiter. Weil `find` die Namen direkt als Argumente übergibt, ohne sie durch einen Strom zu schicken, gibt es mit Leerzeichen keine Probleme.

::::beispiel Einzeln und gesammelt
```console
$ find . -name "*.jpg" -exec ls {} \;
./urlaub.jpg
'./mein foto.jpg'
$ find . -name "*.jpg" -exec ls {} +
'./mein foto.jpg'   ./urlaub.jpg
```

Mit `\;` lief `ls` zweimal, jedes Mal mit einem Namen, und schrieb jeden in eine eigene Zeile. Mit `+` lief es einmal mit beiden Namen, sortierte sie und setzte sie nebeneinander.
::::

⁠**Kurz gesagt:** `find … -exec befehl {} +` gibt die Treffer direkt als Argumente an einen Befehl, auch Namen mit Leerzeichen; mit `\;` statt `+` einzeln.

:::hintergrund Eine Ausgabe, die wie eine Datei aussieht
Manche Programme wollen unbedingt Dateinamen und lesen keine Standardeingabe, oder sie sollen zwei Eingaben auf einmal bekommen. Dafür kennt bash eine weitere Schreibweise, die Prozesssubstitution: `<(befehl)` startet den Befehl mit seiner Standardausgabe in einer Pipe und setzt an seine Stelle einen Dateinamen, unter dem das Leseende dieser Pipe zu erreichen ist.

```console
$ wc -l <(ls /usr/bin) <(ls /usr/sbin)
   1018 /dev/fd/63
    176 /dev/fd/62
   1194 total
$ ls -l <(true)
lr-x------ 1 student student 64 Nov 10 05:15 /dev/fd/63 -> 'pipe:[3582]'
```

`wc` hat zwei „Dateien“ gezählt, `/dev/fd/63` und `/dev/fd/62`. Das sind die Deskriptoren 63 und 62, die die Shell für die beiden Pipes geöffnet und `wc` vererbt hat; `ls -l` zeigt, dass hinter einem solchen Namen eine Pipe steckt. Hier zahlt sich der Grundgedanke aus, dass alles eine Datei ist: `wc` öffnet einen Namen und liest, ohne zu wissen, dass am anderen Ende ein Programm schreibt.
:::

### Aufgaben zu Abschnitt [7](#stufe-7)

<span class="anker" id="stufe-7-6"></span>

:::aufgabe Aufgabe 23 ★ Mit und ohne xargs
<span class="anker" id="aufg-23"></span>

Sage voraus, was `echo obst.txt | wc -l` und `echo obst.txt | xargs wc -l` ausgeben, und prüfe es. Erkläre den Unterschied in einem Satz.

:::loesung
```console
$ echo obst.txt | wc -l
1
$ echo obst.txt | xargs wc -l
7 obst.txt
```

Ohne `xargs` zählt `wc` die eine Zeile, die durch die Pipe kommt; mit `xargs` bekommt es `obst.txt` als Argument, öffnet die Datei und zählt ihre sieben Zeilen.
:::
:::

:::aufgabe Aufgabe 24 ★★ Alle Wörter aller Listen
<span class="anker" id="aufg-24"></span>

Zähle mit einer einzigen Befehlszeile die Wörter aller Dateien in deinem Übungsverzeichnis, deren Name auf `.txt` endet, einschließlich der Unterverzeichnisse. Löse es einmal mit `find` und `xargs` und einmal mit `find -exec`. Warum ist die Gesamtzahl bei beiden Wegen dieselbe?

:::loesung
```console
$ find . -name "*.txt" | xargs wc -w
  9 ./fehler2.txt
  1 ./aus.txt
...
  5 ./einkauf.txt
 73 total
$ find . -name "*.txt" -exec wc -w {} +
  9 ./fehler2.txt
  1 ./aus.txt
...
  5 ./einkauf.txt
 73 total
```

Welche Dateien und welche Summe erscheinen, hängt davon ab, was in deinem Übungsverzeichnis liegt; hier waren es 13 Dateien mit zusammen 73 Wörtern. Beide Wege starten `wc -w` einmal mit allen Namen, in der Reihenfolge, in der `find` sie findet. `wc` bekommt also in beiden Fällen dieselben Argumente und rechnet dieselbe Summe aus. Mit `xargs` ginge es nur so glatt, solange kein Name ein Leerzeichen enthält; der Weg über `-exec … +` ist auch dann sicher.
:::
:::

:::aufgabe Aufgabe 25 ★★★ Die alte Liste
<span class="anker" id="aufg-25"></span>

Lege im Übungsverzeichnis zwei Dateien an: `touch "alte liste.txt" liste.txt`. (a) Sage voraus, was `find . -name "alte*" | xargs rm` bewirkt: Welche Datei wird gelöscht, welche Meldung erscheint, welche Datei bleibt? (b) Prüfe es mit `ls`. (c) Lege die gelöschte Datei wieder an und lösche `alte liste.txt` auf zwei sichere Arten.

:::loesung
(a) Vorhersage: `xargs` zerlegt `./alte liste.txt` in die Wörter `./alte` und `liste.txt` und startet `rm ./alte liste.txt`. `./alte` gibt es nicht, das meldet `rm`. `liste.txt` gibt es, und `rm` löscht sie, obwohl niemand sie löschen wollte. `alte liste.txt` bleibt.

(b)

```console
$ touch "alte liste.txt" liste.txt
$ find . -name "alte*" | xargs rm
rm: cannot remove './alte': No such file or directory
$ ls
 a.txt             b.txt   einkauf.txt   obst.txt    woche.txt
'alte liste.txt'   c.txt   fehler2.txt   sicherung   zahlen.txt
 aus.txt           d.txt   gross.txt     tag.txt
```

`liste.txt` fehlt, `alte liste.txt` ist noch da. Genau davor warnt der Kasten in Unterabschnitt [7.4](#stufe-7-4).

(c) Mit dem Nullbyte als Trenner oder mit `-exec … +`:

```console
$ touch liste.txt
$ find . -name "alte*" -print0 | xargs -0 rm
$ ls
a.txt    c.txt        fehler2.txt  obst.txt   woche.txt
aus.txt  d.txt        gross.txt    sicherung  zahlen.txt
b.txt    einkauf.txt  liste.txt    tag.txt
$ touch "alte liste.txt"
$ find . -name "alte*" -exec rm {} +
$ ls
a.txt    c.txt        fehler2.txt  obst.txt   woche.txt
aus.txt  d.txt        gross.txt    sicherung  zahlen.txt
b.txt    einkauf.txt  liste.txt    tag.txt
```

Beide Male verschwindet nur `alte liste.txt`, und `liste.txt` bleibt. Für eine einzige bekannte Datei geht es natürlich auch ohne `find`: `rm "alte liste.txt"`.
:::
:::

**Zum Weiterüben.** Die frei zugängliche Übungsplattform pwn.college bietet unter dem Namen „Linux Luminarium“ kleine Aufgaben im Browser an; die Module „Practicing Piping“ und „Chaining Commands“ passen zu diesem Kapitel. Sie laufen auf einem fremden Rechner, nicht auf deinem eigenen.

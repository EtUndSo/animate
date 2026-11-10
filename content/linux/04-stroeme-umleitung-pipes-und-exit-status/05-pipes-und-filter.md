---
title: Pipes und Filter
pfad: Informatik / Linux und Kommandozeile / Ströme, Umleitung, Pipes und Exit-Status
adresse: informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status
knoten: Kapitel 4: Ströme, Umleitung, Pipes und Exit-Status
order: 6090500
summary: Bisher führte die Ausgabe eines Programms zum Bildschirm oder in eine Datei.
tags: Pipe, Filter, Pipeline, tee, Unix-Philosophie
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Bisher führte die Ausgabe eines Programms zum Bildschirm oder in eine Datei. Dieser Abschnitt verbindet die Standardausgabe eines Programms direkt mit der Standardeingabe eines anderen. Er erklärt die Pipe, die Programme, die sich für solche Verbindungen eignen, Ketten aus vielen Programmen, einen Abzweig, der ein Zwischenergebnis festhält, und den Grundsatz, nach dem Unix-Programme gebaut sind.
:::

### Die Pipe

<span class="anker" id="stufe-4-1"></span>

Wie viele Programme liegen in `/usr/bin`? `ls` kann sie auflisten, `wc -l` kann Zeilen zählen. Mit dem, was die Abschnitte [2](ausgaben-umleiten.html#stufe-2) und [3](eingaben-umleiten.html#stufe-3) gezeigt haben, geht es über eine Zwischendatei:

```console
$ ls /usr/bin > liste.txt
$ wc -l < liste.txt
1018
$ rm liste.txt
```

Das sind drei Befehle und eine Datei, die man hinterher wieder löschen muss. Bequemer wäre es, die Standardausgabe von `ls` direkt an die Standardeingabe von `wc` zu stecken. Abbildung [14](#abb-14) zeigt diese Verbindung.

:::abbildung linux/k4pipe 14
Die Pipe `ls /usr/bin | wc -l`: Beide Prozesse laufen gleichzeitig. Was `ls` in Deskriptor 1 schreibt, sammelt sich in einem Puffer im Kernel, aus dem `wc` über Deskriptor 0 liest. Am Ende schreibt `wc` die Zahl 1018 an den Bildschirm.
:::

:::definition Definition 4.1 (Pipe)
<span class="anker" id="satz-4-1"></span>

Eine __Pipe__ verbindet die Standardausgabe eines Prozesses mit der Standardeingabe eines anderen. Die Schreibweise `befehl1 | befehl2` weist die Shell an, beide Programme gleichzeitig zu starten, jedes in einem eigenen Prozess, und Deskriptor 1 des ersten mit Deskriptor 0 des zweiten zu verbinden. Die Bytes laufen dabei durch einen Zwischenspeicher im Kernel, nicht durch eine Datei.
:::

Das englische Wort *pipe* heißt Rohr; das Zeichen `|` heißt auf Deutsch senkrechter Strich und liegt auf deutschen Tastaturen auf AltGr+<. Wie bei einer Umleitung merken die beiden Programme nichts von der Verbindung: `ls` schreibt in Deskriptor 1, `wc` liest aus Deskriptor 0.

::::beispiel Die Programme in /usr/bin zählen
```console
$ ls /usr/bin | wc -l
1018
```

Dieselbe Zahl wie über die Zwischendatei, mit einem einzigen Befehl und ohne Datei. Auf deinem Rechner hängt die Zahl davon ab, was installiert ist.
::::

Die Shell verbindet die Pipe, bevor sie die Umleitungen der einzelnen Befehle ausführt. Steht beim ersten Befehl selbst eine Umleitung, etwa `ls > liste.txt | wc -l`, wirkt sie deshalb nach der Pipe und gewinnt: Deskriptor 1 führt dann in die Datei, und durch die Pipe kommt nichts.

Eine Pipe verbindet nur Deskriptor 1 mit Deskriptor 0. Die Standardfehlerausgabe des ersten Programms führt weiter zum Bildschirm. Soll auch sie durch die Pipe, schreibt man `2>&1` als letzte Umleitung vor das `|`. bash kennt dafür die Kurzform `|&`; sie wirkt genau so, als stünde `2>&1` hinter allen Umleitungen des ersten Befehls, unmittelbar vor dem `|`. Abbildung [15](#abb-15) zeigt beide Fälle.

:::abbildung linux/k4pipefehler 15
Oben `ls /gibtsnicht | wc -l`: Die Meldung von `ls` läuft über Deskriptor 2 an der Pipe vorbei zum Bildschirm, durch die Pipe kommt nichts, und `wc` zählt 0. Unten mit `|&`: Auch Deskriptor 2 führt in die Pipe, und `wc` zählt die Meldung als eine Zeile.
:::

::::beispiel [Zweites Beispiel] Die Meldung läuft an der Pipe vorbei
```console
$ ls /gibtsnicht | wc -l
ls: cannot access '/gibtsnicht': No such file or directory
0
$ ls /gibtsnicht |& wc -l
1
```

Beim ersten Aufruf zählt `wc` null Zeilen, denn durch die Pipe kam nichts; die Meldung erscheint am Bildschirm. Beim zweiten kam die Meldung durch die Pipe, und `wc` zählt sie als eine Zeile. Genau dafür ist die Standardfehlerausgabe getrennt: Meldungen sollen nicht in die Daten des nächsten Programms geraten.
::::

⁠**Kurz gesagt:** `befehl1 | befehl2` verbindet die Standardausgabe des ersten mit der Standardeingabe des zweiten Programms; beide laufen gleichzeitig, die Meldungen gehen weiter an den Bildschirm.

:::warnung > und | nicht verwechseln
`>` verbindet ein Programm mit einer Datei, `|` mit einem anderen Programm. Wer `ls > wc` tippt, startet nicht `wc`, sondern schreibt die Ausgabe von `ls` in eine Datei mit dem Namen `wc`; gäbe es dort schon eine Datei dieses Namens, wäre sie überschrieben:

```console
$ ls > wc
$ ls
alles.txt   einkauf.txt  gruss.txt   leer.txt  obst.txt   probe2.txt
beides.txt  fehler.txt   inhalt.txt  nur.txt   probe.txt  wc
$ rm wc
```

In einem Verzeichnis voller Programme wie `/usr/bin` könnte derselbe Tippfehler als root ([Kapitel 2, Abschnitt 1.4](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/terminal-und-shell.html#stufe-1-4)) ein Programm des Systems zerstören.
:::

:::hintergrund Wie eine Pipe im Kernel arbeitet
Eine Pipe ist ein Zwischenspeicher im Kernel mit zwei Enden, einem zum Schreiben und einem zum Lesen; unter Linux fasst er in der Regel 65 536 Bytes. Die Shell legt die Pipe an, bevor sie die beiden Programme startet, und gibt jedem Prozess das passende Ende als Deskriptor 1 beziehungsweise 0. Danach regelt der Kernel den Verkehr: Ist der Speicher leer, wartet der Leser, bis Bytes kommen; ist er voll, wartet der Schreiber, bis der Leser Platz geschaffen hat. So laufen beide Programme gleichzeitig, und auch eine riesige Ausgabe braucht nie mehr als diesen kleinen Speicher. Hat der Schreiber sein Ende geschlossen, etwa weil er fertig ist, und ist der Speicher leer, liefert die nächste Leseanfrage null Bytes: Der Leser sieht das Ende des Stroms. Umgekehrt beendet der Kernel einen Schreiber, der in eine Pipe schreiben will, die niemand mehr liest, mit einer Unterbrechungsnachricht ([Kapitel 2, Abschnitt 5.4](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/schneller-arbeiten-vervollstandigung-verlauf-tastenkurzel.html#stufe-5-4)). Deshalb endet die folgende Pipeline, obwohl der Befehl `yes` ohne Ende Zeilen mit `y` schreibt:

```console
$ yes | head -n 3
y
y
y
```

`head` hört nach drei Zeilen auf und schließt damit das Leseende; beim nächsten Schreibversuch beendet der Kernel `yes`.
:::

:::hintergrund Woher die Pipe kommt
Die Idee ist älter als Unix. 1964 schrieb Doug McIlroy in einer Notiz bei den Bell Labs, man solle Programme verbinden können wie einen Gartenschlauch, an den man ein weiteres Stück schraubt, wenn die Daten auf eine andere Weise bearbeitet werden sollen. Umgesetzt wurde sie erst 1972 oder 1973, als Ken Thompson den Systemaufruf für die Pipe in einer einzigen Nacht in Unix einbaute; die Quellen nennen unterschiedliche Jahre. Die erste Schreibweise benutzte noch dieselben Zeichen wie die Umleitung und hielt nur wenige Monate, dann kam der senkrechte Strich. Dennis Ritchie sah das Geniale darin, dass eine Pipeline aus genau den Programmen besteht, die man ohnehin jeden Tag einzeln benutzt.
:::

### Der Filter

<span class="anker" id="stufe-4-2"></span>

Nicht jedes Programm passt hinter eine Pipe. `wc` passt, denn es liest seine Standardeingabe, wenn es keinen Dateinamen bekommt. `ls` dagegen liest seine Standardeingabe nie; was man ihm durch eine Pipe schickt, kommt nie an. Programme der ersten Art haben einen eigenen Namen. Abbildung [16](#abb-16) zeigt vier von ihnen an derselben Eingabe.

:::abbildung linux/k4filter 16
Vier Filter, dieselbe Eingabe: die sieben Zeilen der Obstliste. `sort` ordnet sie, `head -n 2` behält die ersten zwei, `grep Apfel` nur die Zeilen mit `Apfel`, und `uniq` ändert hier nichts, weil keine zwei gleichen Zeilen direkt untereinander stehen.
:::

:::definition Definition 4.2 (Filter)
<span class="anker" id="satz-4-2"></span>

Ein __Filter__ ist ein Programm, das Daten aus seiner Standardeingabe liest, sie umformt und das Ergebnis in seine Standardausgabe schreibt. Die meisten Filter lesen stattdessen Dateien, wenn man ihnen deren Namen als Argumente gibt.
:::

In diesem Kapitel kommen diese Filter vor, jeder hier nur in seiner einfachsten Form:

<ul>

<li>

`sort` ordnet die Zeilen;

</li>

<li>

`head -n zahl` behält die ersten Zeilen ([Kapitel 3, Abschnitt 4.4](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-ansehen.html#stufe-4-4));

</li>

<li>

`wc` zählt Zeilen, Wörter und Bytes ([Kapitel 3, Abschnitt 4.5](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-ansehen.html#stufe-4-5));

</li>

<li>

`grep wort` behält nur die Zeilen, in denen `wort` vorkommt;

</li>

<li>

`uniq` lässt von mehreren gleichen Zeilen, die direkt untereinander stehen, nur eine stehen;

</li>

<li>

`tr` ersetzt Zeichen (Unterabschnitt [3.3](eingaben-umleiten.html#stufe-3-3)).

</li>

</ul>

Keine Filter sind `ls`, `echo`, `mkdir`, `cp` und `rm`: Sie lesen keine Daten aus ihrer Standardeingabe.

::::beispiel Vier Filter an der Obstliste
```console
$ sort obst.txt
Apfel
Apfel
Apfel
Banane
Birne
Birne
Kiwi
$ head -n 2 obst.txt
Apfel
Birne
$ grep Apfel obst.txt
Apfel
Apfel
Apfel
$ uniq obst.txt
Apfel
Birne
Apfel
Kiwi
Banane
Apfel
Birne
```

`uniq` hat alle sieben Zeilen stehen lassen, denn in der Obstliste stehen nirgends zwei gleiche Zeilen direkt untereinander.
::::

::::beispiel [Zweites Beispiel] Ein Filter liest seine Standardeingabe
Hier bekommt `sort` keinen Dateinamen; die Obstliste kommt über die Umleitung aus Unterabschnitt [3.1](eingaben-umleiten.html#stufe-3-1), und das Ergebnis geht durch eine Pipe an `head`:

```console
$ sort < obst.txt | head -n 2
Apfel
Apfel
```
::::

⁠**Kurz gesagt:** Ein Filter liest seine Standardeingabe, formt sie um und schreibt das Ergebnis in seine Standardausgabe; deshalb passt er hinter eine Pipe.

### Die Pipeline

<span class="anker" id="stufe-4-3"></span>

Wie viele verschiedene Sorten Obst stehen auf der Liste? Dafür braucht man drei Schritte: die Zeilen ordnen, damit gleiche untereinander stehen, die Wiederholungen streichen und die übrigen Zeilen zählen. Jeder Schritt ist ein Filter, und die Filter lassen sich hintereinanderstecken wie die Stationen eines Fließbands. Abbildung [17](#abb-17) zeigt das Fließband mit dem Zwischenergebnis nach jeder Station.

:::abbildung linux/k4fliessband 17
Die Pipeline `sort obst.txt | uniq | wc -l` als Fließband. Unter jeder Pipe steht, was gerade durch sie fließt: nach `sort` die sieben geordneten Zeilen, nach `uniq` die vier Sorten, am Ende die Zahl 4.
:::

:::definition Definition 4.3 (Pipeline)
<span class="anker" id="satz-4-3"></span>

Eine __Pipeline__ ist eine Folge von Befehlen, die durch `|` verbunden sind. Die Shell startet alle Befehle gleichzeitig, jeden in einem eigenen Prozess, und verbindet die Standardausgabe jedes Befehls mit der Standardeingabe des nächsten. Die Standardausgabe des letzten Befehls führt dorthin, wohin sie ohne Pipeline geführt hätte; umgeleitet werden kann sie wie jede andere.
:::

Für die Shell ist auch ein einzelner Befehl ohne `|` eine Pipeline, eine mit nur einer Stufe. Wichtig ist die Reihenfolge der Stufen: `uniq` vergleicht jede Zeile nur mit der direkt davor, deshalb muss `sort` vorher gleiche Zeilen zusammenbringen.

::::beispiel Die Sorten der Obstliste
```console
$ sort obst.txt | uniq
Apfel
Banane
Birne
Kiwi
$ sort obst.txt | uniq | wc -l
4
```

Die erste Pipeline zeigt die vier Sorten, je einmal. Die zweite hängt `wc -l` an und beantwortet die Frage mit einer Zahl. Ohne `sort` hätte `uniq` nichts gestrichen, wie das Beispiel in Unterabschnitt [4.2](#stufe-4-2) gezeigt hat, und `wc -l` hätte 7 gezählt.
::::

Eine Datei an den Anfang einer Pipeline holt man am einfachsten, indem man ihren Namen dem ersten Filter als Argument gibt, wie bei `sort obst.txt`, oder mit `<`. Die Schreibweise `cat obst.txt | sort` funktioniert auch, startet aber einen Prozess mehr, der nur weiterreicht.

⁠**Kurz gesagt:** Eine Pipeline reiht Filter wie Stationen eines Fließbands aneinander; jede Station arbeitet mit dem, was die vorige liefert.

### Der Abzweig: tee

<span class="anker" id="stufe-4-4"></span>

Manchmal will man ein Zwischenergebnis einer Pipeline aufheben und trotzdem weiterverarbeiten, etwa die Liste der Sorten speichern und zugleich zählen. Mit `>` ginge das nicht, denn dann käme beim nächsten Filter nichts mehr an. Gebraucht wird ein Abzweig in der Leitung, wie ihn Abbildung [18](#abb-18) zeigt.

:::abbildung linux/k4tee 18
`tee` als T-Stück in der Leitung: Was von links ankommt, fließt unverändert nach rechts weiter zum nächsten Filter und zugleich nach unten in die Datei `sorten.txt`.
:::

:::definition Definition 4.4 (tee)
<span class="anker" id="satz-4-4"></span>

Der Befehl __tee__ liest seine Standardeingabe und schreibt alles, was er liest, sowohl in seine Standardausgabe als auch in jede Datei, die als Argument genannt ist. Er legt diese Dateien an oder leert sie vorher; mit der Option `-a` hängt er an.
:::

Der Name kommt vom T-Stück in einer Rohrleitung, englisch *tee*, das einen Strom auf zwei Wege verteilt.

::::beispiel Sorten speichern und zählen
```console
$ sort obst.txt | uniq | tee sorten.txt | wc -l
4
$ cat sorten.txt
Apfel
Banane
Birne
Kiwi
```

`wc -l` hat die vier Zeilen gezählt, die `tee` weitergereicht hat; dieselben vier Zeilen stehen in `sorten.txt`.
::::

⁠**Kurz gesagt:** `tee datei` gibt seine Eingabe unverändert weiter und schreibt zugleich eine Kopie in die Datei.

### Die Unix-Philosophie

<span class="anker" id="stufe-4-5"></span>

Warum gibt es kein Programm „Obstsorten zählen“, sondern drei kleine, die man verbinden muss? Hinter dieser Bauweise steckt ein Grundsatz, der die Werkzeuge von Unix und Linux seit den 1970er-Jahren prägt.

:::definition Definition 4.5 (Unix-Philosophie)
<span class="anker" id="satz-4-5"></span>

Die __Unix-Philosophie__ ist ein Grundsatz für den Bau von Programmen. Jedes Programm soll eine einzige Sache gut machen. Programme sollen Text lesen und schreiben, ohne überflüssige Zutaten, damit die Ausgabe jedes Programms die Eingabe eines anderen werden kann. Neue Aufgaben löst man, indem man vorhandene Programme verbindet, statt ein großes neues zu schreiben.
:::

Der Vorteil zeigt sich, sobald die Frage sich ändert. Dieselben kleinen Programme beantworten, neu verbunden, ganz andere Fragen, für die niemand ein eigenes Programm geschrieben hat.

::::beispiel Neue Fragen, alte Programme
Wie oft steht `Apfel` auf der Obstliste, und wie viele Einträge hat die Einkaufsliste?

```console
$ grep Apfel obst.txt | wc -l
3
$ wc -l < einkauf.txt
5
```

`grep` sucht, `wc` zählt; keines der beiden weiß etwas von Obst oder Einkäufen. Damit das klappt, schreiben Filter nur ihre Daten und keine Überschriften oder Hinweise dazwischen, die der nächste Filter für Daten halten würde.
::::

⁠**Kurz gesagt:** Kleine Programme, die eine Sache gut machen und Text lesen und schreiben, lassen sich zu immer neuen Werkzeugketten verbinden.

:::hintergrund Der Grundsatz im Original
1978 schrieben Doug McIlroy und zwei Kollegen im Vorwort zu einer Sammlung von Aufsätzen über Unix einige Stilregeln auf, die bis heute als Kern der Unix-Philosophie gelten. Sinngemäß lauten sie: Jedes Programm soll eine Sache gut machen; für eine neue Aufgabe baut man lieber ein neues Programm, als ein altes mit zusätzlichen Funktionen zu überladen. Man soll damit rechnen, dass die Ausgabe jedes Programms zur Eingabe eines anderen wird, das es noch gar nicht gibt; deshalb keine überflüssigen Angaben in der Ausgabe, keine Eingabeformate mit starren Spalten oder aus Binärdaten, und kein Programm soll darauf bestehen, seine Eingaben im Dialog mit einem Menschen zu bekommen. Daraus folgen viele Eigenheiten, die in diesem Kapitel vorkamen: `ls` schreibt in eine Datei einen Namen pro Zeile und keine Spalten; Meldungen gehen in einen eigenen Strom; und die Programme sind klein genug, dass man sie in einer Zeile kombinieren kann. Die gemeinsame Sprache ist Text in Zeilen: Jedes Programm, das Zeilen liest und Zeilen schreibt, lässt sich mit jedem anderen dieser Art verbinden.
:::

### Aufgaben zu Abschnitt [4](#stufe-4)

<span class="anker" id="stufe-4-6"></span>

:::aufgabe Aufgabe 13 ★★ Pipelines bauen
<span class="anker" id="aufg-13"></span>

(a) Wie viele Einträge haben `/usr/sbin` und `/etc`? Schreibe je eine Pipeline. (b) Welche fünf Dateien in `/usr/bin` sind die größten? Benutze `ls -S` aus [Kapitel 3, Abschnitt 3.6](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/den-inhalt-eines-verzeichnisses-anzeigen.html#stufe-3-6) und `head`. (c) Erweitere (b) so, dass die fünf Namen zusätzlich in der Datei `gross.txt` landen und am Bildschirm nur ihre Anzahl erscheint.

:::loesung
```console
$ ls /usr/sbin | wc -l
176
$ ls /etc | wc -l
174
$ ls -S /usr/bin | head -n 5
x86_64-linux-gnu-lto-dump-15
snap
shellcheck
coreutils
gdb
$ ls -S /usr/bin | head -n 5 | tee gross.txt | wc -l
5
$ cat gross.txt
x86_64-linux-gnu-lto-dump-15
snap
shellcheck
coreutils
gdb
```

(a) Auf dem Testsystem 176 und 174 Einträge; auf deinem Rechner hängen die Zahlen davon ab, was installiert ist. Versteckte Einträge zählt `ls` ohne `-a` nicht mit. (b) `ls -S` sortiert nach Größe, die größte zuerst, und `head -n 5` behält die ersten fünf. Dass auch `coreutils` dabei ist, passt zu [Kapitel 2, Abschnitt 7.2](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/zwei-fassungen-der-grundbefehle-gnu-und-uutils.html#stufe-7-2): Diese eine Datei enthält alle Grundbefehle der uutils-Fassung. (c) `tee` schreibt die fünf Namen in `gross.txt` und reicht sie an `wc -l` weiter, das am Bildschirm nur die Anzahl zeigt.
:::
:::

:::aufgabe Aufgabe 14 ★★ Was fließt durch die Pipes?
<span class="anker" id="aufg-14"></span>

Schreibe für `sort obst.txt | uniq | head -n 2` auf, was durch die erste und was durch die zweite Pipe fließt und was am Ende erscheint. Was ändert sich, wenn du `sort` und `uniq` vertauschst?

:::loesung
Durch die erste Pipe fließen die sieben Zeilen der Obstliste, geordnet: `Apfel` dreimal, `Banane`, `Birne` zweimal, `Kiwi`. `uniq` streicht die Wiederholungen; durch die zweite Pipe fließen `Apfel`, `Banane`, `Birne`, `Kiwi`. `head -n 2` behält die ersten beiden.

```console
$ sort obst.txt | uniq | head -n 2
Apfel
Banane
$ uniq obst.txt | sort
Apfel
Apfel
Apfel
Banane
Birne
Birne
Kiwi
$ uniq obst.txt | sort | head -n 2
Apfel
Apfel
```

Vertauscht arbeitet `uniq` zuerst. In der ungeordneten Liste stehen keine zwei gleichen Zeilen untereinander, also streicht es nichts; `sort` ordnet danach alle sieben Zeilen, und `head -n 2` zeigt zweimal `Apfel`. Die Reihenfolge der Stufen gehört zur Bedeutung einer Pipeline.
:::
:::

:::aufgabe Aufgabe 15 ★ Ein Tippfehler
<span class="anker" id="aufg-15"></span>

Jemand wollte die ersten zwei Zeilen der geordneten Obstliste sehen und tippte `sort obst.txt > head -n 2`. Was erscheint am Bildschirm, und welche Datei gibt es danach im Übungsverzeichnis? Wie lautet der richtige Befehl?

:::loesung
```console
$ sort obst.txt > head -n 2
sort: cannot read: 2: No such file or directory
$ ls
a.txt    c.txt        fehler2.txt  obst.txt   zahlen.txt
aus.txt  d.txt        gross.txt    tag.txt
b.txt    einkauf.txt  head         woche.txt
$ cat head
$ rm head
```

Die Shell hat `> head` als Umleitung in eine Datei namens `head` gelesen und die Umleitung aus der Zeile entfernt. Übrig blieb `sort obst.txt -n 2`: `sort` bekam die Option `-n` und zwei Dateinamen, `obst.txt` und `2`. Die Datei `2` gibt es nicht, `sort` meldet das und gibt nichts aus; die Datei `head` ist leer. Gemeint war `sort obst.txt | head -n 2`. Die Liste auf deinem Rechner sieht anders aus, je nachdem, welche Aufgaben du schon gemacht hast.
:::
:::

:::aufgabe Aufgabe 16 ★★★ Eine Meldung und eine Pipe
<span class="anker" id="aufg-16"></span>

Sage voraus, was `echo "Achtung" >&2 | wc -l` ausgibt, und prüfe es. Erkläre beide Zeilen der Ausgabe. Was ändert sich mit `|&` statt `|`?

:::loesung
```console
$ echo "Achtung" >&2 | wc -l
Achtung
0
$ echo "Achtung" >&2 |& wc -l
Achtung
0
```

Die Shell verbindet zuerst Deskriptor 1 von `echo` mit der Pipe. Dann führt sie die Umleitung `>&2` aus: Deskriptor 1 wird eine Kopie von Deskriptor 2 und führt damit zum Terminal. `echo` schreibt also ans Terminal, dort erscheint `Achtung`. Durch die Pipe kommt nichts, `wc -l` zählt 0 Zeilen.

Mit `|&` ändert sich nichts, und das überrascht zunächst. `|&` wirkt wie `2>&1` hinter allen Umleitungen, die beim Befehl selbst stehen (Unterabschnitt [4.1](#stufe-4-1)). Zu diesem Zeitpunkt führt Deskriptor 1 wegen `>&2` schon zum Terminal, also bekommt auch Deskriptor 2 das Terminal. Auch hier gilt: Jede Kopie übernimmt das Ziel, das gerade da ist.
:::
:::

:::aufgabe Aufgabe 17 ★★★ Die Deskriptoren in einer Pipe
<span class="anker" id="aufg-17"></span>

Führe `ls -l /proc/self/fd` dreimal aus: einmal so, einmal als `ls -l /proc/self/fd | cat` und einmal als `ls -l /proc/self/fd 2> /dev/null | cat`. Wohin führen die Deskriptoren 0, 1 und 2 von `ls` jeweils? Erkläre jeden Unterschied mit dem, was die Shell vor dem Start eingerichtet hat.

:::loesung
Direkt im Terminal führen 0, 1 und 2 zum Terminal, wie in Unterabschnitt [1.7](prozesse-und-ihre-drei-strome.html#stufe-1-7). In den Pipelines:

```console
$ ls -l /proc/self/fd | cat
total 0
lrwx------ 1 student student 64 Nov 10 05:32 0 -> /dev/pts/2
l-wx------ 1 student student 64 Nov 10 05:32 1 -> pipe:[9901]
lrwx------ 1 student student 64 Nov 10 05:32 2 -> /dev/pts/2
lr-x------ 1 student student 64 Nov 10 05:32 3 -> /proc/719/fd
$ ls -l /proc/self/fd 2> /dev/null | cat
total 0
lrwx------ 1 student student 64 Nov 10 05:32 0 -> /dev/pts/2
l-wx------ 1 student student 64 Nov 10 05:32 1 -> pipe:[9903]
l-wx------ 1 student student 64 Nov 10 05:32 2 -> /dev/null
lr-x------ 1 student student 64 Nov 10 05:32 3 -> /proc/721/fd
```

In der ersten Pipeline führt Deskriptor 1 zu einer Pipe; die Zahl in den eckigen Klammern ist ihre Nummer im Kernel. Das hat die Shell vor dem Start eingerichtet, weil `|` folgt. Deskriptor 0 und 2 führen weiter zum Terminal, denn eine Pipe verbindet nur die Standardausgabe. In der zweiten Pipeline führt zusätzlich Deskriptor 2 nach `/dev/null`, wegen `2> /dev/null`. In allen drei Fällen bemerkt `ls` nichts davon; es schreibt seine Liste wie immer in Deskriptor 1.
:::
:::

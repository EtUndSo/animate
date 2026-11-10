---
title: Eingaben umleiten
pfad: Informatik / Linux und Kommandozeile / Ströme, Umleitung, Pipes und Exit-Status
adresse: informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status
knoten: Kapitel 4: Ströme, Umleitung, Pipes und Exit-Status
order: 6090400
summary: Was mit der Ausgabe geht, geht auch mit der Eingabe: Die Shell kann die Standardeingabe eines Programms mit einer Datei verbinden oder ihm ein paar Zeilen Text mitgeben, die direkt in der Befehlszeile stehen.
tags: Here-Document, Here-String
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Was mit der Ausgabe geht, geht auch mit der Eingabe: Die Shell kann die Standardeingabe eines Programms mit einer Datei verbinden oder ihm ein paar Zeilen Text mitgeben, die direkt in der Befehlszeile stehen. Dieser Abschnitt zeigt drei Wege dafür.
:::

### Die Umleitung der Eingabe: <

<span class="anker" id="stufe-3-1"></span>

`wc -l einkauf.txt` zählt die Zeilen und schreibt den Dateinamen dahinter. Wer nur die Zahl haben will, etwa um sie weiterzuverarbeiten, muss `wc` die Datei so geben, dass es ihren Namen gar nicht erfährt. Abbildung [11](#abb-11) stellt die beiden Wege nebeneinander.

:::abbildung linux/k4eingabe 11
Zwei Wege, eine Datei zu zählen. Links `wc -l einkauf.txt`: `wc` bekommt den Namen als Argument, öffnet die Datei selbst und schreibt den Namen hinter die Zahl. Rechts `wc -l < einkauf.txt`: Die Shell öffnet die Datei und verbindet sie mit Deskriptor 0; `wc` liest nur einen Strom ohne Namen und schreibt nur die Zahl.
:::

:::definition Definition 3.1 (Umleitung der Eingabe)
<span class="anker" id="satz-3-1"></span>

Die Schreibweise `befehl < datei` öffnet die Datei zum Lesen und verbindet sie mit der Standardeingabe des neuen Prozesses. Das Programm bekommt keinen Dateinamen, sondern nur den Strom.
:::

::::beispiel Mit und ohne Namen
```console
$ wc -l einkauf.txt
5 einkauf.txt
$ wc -l < einkauf.txt
5
```

Beim zweiten Aufruf hat `wc` kein Argument bekommen, also liest es seine Standardeingabe; dass dahinter `einkauf.txt` steht, weiß es nicht.
::::

::::beispiel [Zweites Beispiel] Wer meldet den Fehler?
```console
$ wc -l < fehlt.txt
bash: fehlt.txt: No such file or directory
```

Die Meldung beginnt mit `bash`, nicht mit `wc`. Die Shell konnte die Datei nicht öffnen und hat `wc` deshalb gar nicht erst gestartet. Das zeigt noch einmal, wer eine Umleitung einrichtet.
::::

⁠**Kurz gesagt:** `befehl < datei` macht eine Datei zur Standardeingabe; das Programm liest einen Strom und kennt den Namen nicht.

### Das Here-Document

<span class="anker" id="stufe-3-2"></span>

Manchmal braucht ein Programm nur ein paar Zeilen als Eingabe, und es lohnt nicht, dafür erst eine Datei anzulegen. Praktisch wäre es, die Zeilen gleich in die Befehlszeile zu schreiben und der Shell zu sagen, wo sie aufhören. Abbildung [12](#abb-12) zeigt, wie die Shell solche Zeilen sammelt.

:::abbildung linux/k4heredoc 12
Ein Here-Document: Die Shell liest die Zeilen nach `cat <<ENDE`, bis eine Zeile nur `ENDE` enthält. Die gesammelten Zeilen ohne die Endzeile gibt sie `cat` als Standardeingabe.
:::

:::definition Definition 3.2 (Here-Document)
<span class="anker" id="satz-3-2"></span>

Ein __Here-Document__ ist eine Umleitung der Form `befehl <<ENDWORT`, auf die Textzeilen folgen und zum Schluss eine Zeile, die nur das Endwort enthält. Die Shell sammelt die Zeilen dazwischen und gibt sie dem Befehl als Standardeingabe; die Zeile mit dem Endwort gehört nicht dazu.
:::

Der englische Name bedeutet etwa „Dokument an Ort und Stelle“: Der Text steht dort, wo er gebraucht wird. Das Endwort darf man frei wählen; üblich sind `ENDE` oder `EOF`, die Abkürzung für „end of file“. Tippt man ein Here-Document im Terminal, zeigt die Shell vor jeder weiteren Zeile das Zeichen `>` als Zeichen dafür, dass der Befehl noch nicht vollständig ist; dieses `>` tippst du nicht mit, und mit einer Umleitung hat es nichts zu tun.

::::beispiel Zwei Zeilen für cat
Tippe `cat <<ENDE`, dann die Zeilen `Milch`, `Brot` und `ENDE`:

```console
$ cat <<ENDE
> Milch
> Brot
> ENDE
Milch
Brot
```

Erst nach der Zeile `ENDE` startet `cat`, liest die beiden Zeilen aus seiner Standardeingabe und schreibt sie aus.
::::

Umleitungen lassen sich kombinieren: Das Here-Document liefert die Eingabe, `>` schickt die Ausgabe in eine Datei. So entsteht die Obstliste, mit der die folgenden Abschnitte arbeiten; lege sie in deinem Übungsverzeichnis an:

```console
$ cat > obst.txt <<ENDE
> Apfel
> Birne
> Apfel
> Kiwi
> Banane
> Apfel
> Birne
> ENDE
$ wc -l obst.txt
7 obst.txt
```

⁠**Kurz gesagt:** Ein Here-Document gibt einem Befehl die folgenden Zeilen bis zum Endwort als Standardeingabe.

:::hintergrund Ein Dollarzeichen im Here-Document
Ganz wörtlich nimmt die Shell den Text eines Here-Documents nicht: Ein `$` leitet für sie eine Ersetzung ein, bei der sie an dieser Stelle einen Wert einsetzt, den sie sich gemerkt hat; für `$5` hat sie hier keinen, und es bleibt nichts übrig. Steht das Endwort in Anführungszeichen, übernimmt sie den Text Zeichen für Zeichen:

```console
$ cat <<ENDE
> Eis: $5 pro Kugel
> ENDE
Eis:  pro Kugel
$ cat <<'ENDE'
> Eis: $5 pro Kugel
> ENDE
Eis: $5 pro Kugel
```

Im ersten Fall ist der Preis verschwunden, mit `'ENDE'` bleibt der Text, wie er ist.
:::

### Der Here-String

<span class="anker" id="stufe-3-3"></span>

Ist die Eingabe nur eine einzige Zeile, ist selbst ein Here-Document mit Endzeile umständlich. Dafür gibt es eine kürzere Form. Abbildung [13](#abb-13) zeigt, welchen Strom die Shell daraus macht.

:::abbildung linux/k4herestring 13
Aus `<<< "Linux"` macht die Shell einen Strom von sechs Bytes: die fünf Buchstaben und ein angehängtes Zeilenende. `wc -c` zählt deshalb 6.
:::

:::definition Definition 3.3 (Here-String)
<span class="anker" id="satz-3-3"></span>

Ein __Here-String__ ist eine Umleitung der Form `befehl <<< "text"`. Die Shell gibt dem Befehl den Text als Standardeingabe und hängt ein Zeilenende an.
:::

::::beispiel Wörter zählen, Buchstaben tauschen
```console
$ wc -w <<< "Heute gibt es Kuchen"
4
$ tr a-z A-Z <<< "hallo linux"
HALLO LINUX
$ wc -c <<< "Linux"
6
```

`wc -w` zählt vier Wörter. Der Befehl `tr` liest seine Standardeingabe und ersetzt jedes Zeichen aus der ersten Liste durch das Zeichen an derselben Stelle der zweiten; `a-z` steht für alle Kleinbuchstaben von a bis z, `A-Z` für die Großbuchstaben. `wc -c` zählt sechs Bytes für ein Wort aus fünf Buchstaben: Das sechste ist das Zeilenende, das die Shell angehängt hat.
::::

⁠**Kurz gesagt:** Ein Here-String gibt einem Befehl eine Zeile Text als Standardeingabe, mit angehängtem Zeilenende.

### Aufgaben zu Abschnitt [3](#stufe-3)

<span class="anker" id="stufe-3-4"></span>

:::aufgabe Aufgabe 10 ★ Mit oder ohne Namen
<span class="anker" id="aufg-10"></span>

Vergleiche `wc -c einkauf.txt` und `wc -c < einkauf.txt`. (a) Was ist gleich, was verschieden? (b) Warum kann `wc` im zweiten Fall den Namen gar nicht ausgeben? (c) Was meldet `wc -c < gibtsnicht.txt`, und welches Programm schreibt die Meldung?

:::loesung
```console
$ wc -c einkauf.txt
32 einkauf.txt
$ wc -c < einkauf.txt
32
$ wc -c < gibtsnicht.txt
bash: gibtsnicht.txt: No such file or directory
```

(a) Gleich ist die Zahl, 32 Bytes. Verschieden ist, dass nur der erste Aufruf den Namen dahinterschreibt. (b) Beim zweiten Aufruf hat `wc` kein Argument bekommen; die Shell hat die Datei geöffnet und mit Deskriptor 0 verbunden. `wc` liest einen Strom, und ein Strom hat keinen Namen. (c) Die Meldung schreibt die Shell, zu erkennen am Anfang `bash:`. Sie konnte die Datei nicht öffnen und hat `wc` deshalb nicht gestartet.
:::
:::

:::aufgabe Aufgabe 11 ★★ Eine Woche als Here-Document
<span class="anker" id="aufg-11"></span>

(a) Lege mit einem Here-Document die Datei `woche.txt` an, die die sieben Wochentage enthält, jeden in einer eigenen Zeile. (b) Prüfe mit `wc -l`, dass es sieben Zeilen sind. (c) Hänge mit einem zweiten Here-Document die Zeilen `Feiertag` und `Urlaub` an `woche.txt` an, ohne die Wochentage zu verlieren, und prüfe mit `wc -l`, dass es jetzt neun Zeilen sind.

:::loesung
```console
$ cat > woche.txt <<ENDE
> Montag
> Dienstag
> Mittwoch
> Donnerstag
> Freitag
> Samstag
> Sonntag
> ENDE
$ wc -l woche.txt
7 woche.txt
$ cat >> woche.txt <<ENDE
> Feiertag
> Urlaub
> ENDE
$ wc -l woche.txt
9 woche.txt
```

(a) und (b): Das Here-Document liefert die sieben Zeilen als Standardeingabe von `cat`, `>` schickt sie in die Datei. Die Zeile `ENDE` gehört nicht dazu, deshalb sind es sieben Zeilen und nicht acht. (c) Die Eingabe kommt wieder aus einem Here-Document, die Ausgabe geht diesmal mit `>>` in die Datei; die Shell leert sie also nicht, und die zwei neuen Zeilen kommen hinter die sieben alten. Mit `>` stünden danach nur noch `Feiertag` und `Urlaub` darin.
:::
:::

:::aufgabe Aufgabe 12 ★ Bytes im Here-String
<span class="anker" id="aufg-12"></span>

Sage voraus, was `wc -c <<< "Kaffee"` und `wc -c <<< "Äpfel"` ausgeben, und prüfe es. Erkläre beide Zahlen.

:::loesung
```console
$ wc -c <<< "Kaffee"
7
$ wc -c <<< "Äpfel"
7
```

`Kaffee` hat sechs Buchstaben zu je einem Byte, dazu kommt das Zeilenende, das der Here-String anhängt: 7. `Äpfel` hat nur fünf Buchstaben, doch das `Ä` belegt in UTF-8 zwei Bytes ([Kapitel 3, Abschnitt 4.1](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-ansehen.html#stufe-4-1)): $2 + 4 + 1 = 7$.
:::
:::

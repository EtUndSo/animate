---
title: Worttrennung und Quoting
pfad: Informatik / Linux und Kommandozeile / Wie die Shell eine Befehlszeile liest: Expansion, Quoting, Variablen, Umgebung
adresse: informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung
knoten: Kapitel 5: Wie die Shell eine Befehlszeile liest: Expansion, Quoting, Variablen, Umgebung
order: 6100400
summary: Nach den Erweiterungen zerlegt die Shell manche Ergebnisse noch einmal in Wörter.
tags: printf, Worttrennung, Quoting, umgekehrter Schrägstrich
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Nach den Erweiterungen zerlegt die Shell manche Ergebnisse noch einmal in Wörter. Das ist der Grund für die Überraschung mit `mein bericht.txt` aus „Worum es geht“. Dieser Abschnitt zeigt, wann die Shell das tut, wie man mit Anführungszeichen und dem umgekehrten Schrägstrich steuert, was sie verändern darf, und in welcher Reihenfolge alle Schritte der Expansion ablaufen.
:::

### Argumente einzeln anzeigen: printf

<span class="anker" id="stufe-3-1"></span>

`echo` schreibt seine Argumente mit je einem Leerzeichen dazwischen. Ob es ein Argument mit einem Leerzeichen darin bekommen hat oder zwei Argumente, sieht man der Ausgabe nicht an. Für diesen Abschnitt braucht man aber genau das: die Grenzen zwischen den Argumenten. Abbildung [10](#abb-10) zeigt ein Werkzeug, das sie sichtbar macht.

:::abbildung linux/k5printf 10
`printf "[%s]\n" eins zwei`: `printf` legt seine Vorlage über das erste übrige Argument und schreibt `[eins]` mit Zeilenende. Weil noch ein Argument übrig ist, legt es die Vorlage ein zweites Mal an und schreibt `[zwei]`. Jede Zeile der Ausgabe ist ein Argument.
:::

:::definition Definition 3.1 (printf)
<span class="anker" id="satz-3-1"></span>

Der eingebaute Befehl __printf__ schreibt Text nach einer Vorlage, seinem ersten Argument. In der Vorlage steht `%s` für das nächste Argument und `\n` für ein Zeilenende. Bleiben nach dem Durchgang durch die Vorlage noch Argumente übrig, wendet `printf` die Vorlage erneut an.
:::

Mit der Vorlage `"[%s]\n"` schreibt `printf` also jedes Argument in eckigen Klammern auf eine eigene Zeile. Die Anführungszeichen halten die Vorlage als ein Argument zusammen und schützen die eckigen Klammern und den umgekehrten Schrägstrich vor der Shell, so wie die Anführungszeichen um das Muster bei `find -name "*.txt"` in [Kapitel 3, Abschnitt 10.2](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-finden-und-platz-messen.html#stufe-10-2); was sie dabei genau bewirken, zeigt dieser Abschnitt.

::::beispiel Zwei Wörter, zwei Argumente
```console
$ echo eins    zwei
eins zwei
$ printf "[%s]\n" eins    zwei
[eins]
[zwei]
```

Die vier Leerzeichen zwischen `eins` und `zwei` trennen nur zwei Wörter; `echo` setzt beim Schreiben ein einziges Leerzeichen dazwischen. `printf` zeigt die zwei Argumente als zwei Zeilen.
::::

⁠**Kurz gesagt:** `printf "[%s]\n"` schreibt jedes Argument in Klammern auf eine eigene Zeile und macht so sichtbar, welche Argumente ein Befehl bekommt.

### Die Worttrennung

<span class="anker" id="stufe-3-2"></span>

Zwei Beobachtungen passen zunächst nicht zusammen. Die Einkaufsliste hat vier Zeilen, doch `echo $(cat einkauf.txt)` schreibt sie in eine einzige Zeile. Und eine Variable, die den Namen `mein bericht.txt` enthält, hilft `ls` nicht weiter:

```console
$ echo $(cat einkauf.txt)
Milch Brot Äpfel Kaffee
$ touch "mein bericht.txt"
$ datei="mein bericht.txt"
$ ls $datei
ls: cannot access 'mein': No such file or directory
ls: cannot access 'bericht.txt': No such file or directory
```

Die Datei `mein bericht.txt` gibt es, die Variable enthält genau diesen Namen, und doch sucht `ls` zwei Dateien. Beide Rätsel haben dieselbe Ursache, die Abbildung [11](#abb-11) zeigt.

:::abbildung linux/k5worttrennung 11
`ls $datei` mit dem Wert `mein bericht.txt`. Die Parametererweiterung setzt den Wert ein, ein Wort mit einem Leerzeichen darin. Danach zerlegt die Worttrennung dieses Ergebnis am Leerzeichen in zwei Wörter, und `ls` bekommt zwei Argumente. Darunter `ls "$datei"`: Die Anführungszeichen verhindern die Zerlegung, `ls` bekommt ein Argument.
:::

:::definition Definition 3.2 (Worttrennung)
<span class="anker" id="satz-3-2"></span>

Die __Worttrennung__ zerlegt die Ergebnisse der Parametererweiterung, der Befehlsersetzung und der Arithmetik in einzelne Wörter, sofern diese Erweiterungen nicht zwischen doppelten Anführungszeichen standen. Getrennt wird an Leerzeichen, Tabulatoren und Zeilenenden; mehrere davon hintereinander zählen wie eines, am Anfang und am Ende fallen sie weg. Text, den du selbst getippt hast, zerlegt die Worttrennung kein zweites Mal.
:::

Die Wörter, die dabei entstehen, durchlaufen danach noch die Pfadnamen-Erweiterung: Enthält ein solches Wort ein Musterzeichen, wird es wie ein getipptes Muster durch Dateinamen ersetzt. Ein Ergebnis, das ganz leer ist oder nur aus solchen Trennzeichen besteht, ergibt gar kein Wort.

::::beispiel Die Rätsel aufgelöst
```console
$ liste=$(cat einkauf.txt)
$ printf "[%s]\n" $liste
[Milch]
[Brot]
[Äpfel]
[Kaffee]
```

In der Variablen `liste` stehen die vier Zeilen, getrennt durch Zeilenenden; nur das letzte hat die Befehlsersetzung entfernt. Ohne Anführungszeichen zerlegt die Worttrennung den Wert an den Zeilenenden in vier Wörter; `echo` hätte sie mit Leerzeichen dazwischen in eine Zeile geschrieben. Mit dem Dateinamen geschieht dasselbe am Leerzeichen:

```console
$ printf "[%s]\n" $datei
[mein]
[bericht.txt]
```
::::

::::beispiel [Zweites Beispiel] Leere Werte und Muster in Variablen
```console
$ leer=
$ printf "[%s]\n" $leer Ende
[Ende]
$ muster="*.jpg"
$ echo $muster
foto1.jpg foto10.jpg foto2.jpg
```

Die leere Variable ergibt kein Wort, `printf` bekommt nur `Ende`. In `muster` steht der Text `*.jpg`; nach der Worttrennung durchläuft er die Pfadnamen-Erweiterung, und `echo` bekommt die Namen der Fotos.
::::

⁠**Kurz gesagt:** Die Worttrennung zerlegt die Ergebnisse von Erweiterungen ohne doppelte Anführungszeichen an Leerzeichen, Tabulatoren und Zeilenenden; danach wirken darin auch Musterzeichen.

:::hintergrund Woher die Shell die Trennzeichen nimmt
Die Zeichen, an denen die Worttrennung zerlegt, stehen in einer Variablen der Shell namens `IFS` (von englisch „internal field separator“). `printf` mit der Vorlage `%q` schreibt einen Wert so, dass man unsichtbare Zeichen erkennt:

```console
$ printf "%q\n" "$IFS"
$' \t\n'
```

Zwischen `$'` und `'` stehen ein Leerzeichen, `\t` für den Tabulator und `\n` für das Zeilenende. Ältere Shells zerlegten mit diesen Zeichen jedes Wort einer Zeile, auch getippte. Der heutige Standard für Unix-Shells beschränkt die Worttrennung auf die Ergebnisse von Erweiterungen; seine Begründung nennt ausdrücklich auch die Sicherheit. Man kann `IFS` ändern, etwa auf einen Doppelpunkt; in der interaktiven Shell wirkt das aber auf jeden folgenden Befehl, deshalb lässt man es dort besser bleiben.
:::

### Das Quoting

<span class="anker" id="stufe-3-3"></span>

Expansion und Worttrennung sind meist erwünscht, manchmal aber nicht: Ein Dateiname soll ein Wort bleiben, ein Muster soll unverändert bei `find` ankommen, ein Dollarzeichen soll ein Dollarzeichen sein. Man braucht deshalb eine Möglichkeit, der Shell zu sagen: Diese Zeichen bitte wörtlich nehmen.

:::definition Definition 3.3 (Quoting)
<span class="anker" id="satz-3-3"></span>

__Quoting__ heißt, Zeichen einer Befehlszeile so zu kennzeichnen, dass die Shell sie wörtlich nimmt, statt ihnen eine besondere Bedeutung zu geben. Die drei grundlegenden Mittel dafür sind einfache Anführungszeichen, doppelte Anführungszeichen und der umgekehrte Schrägstrich. Was so gekennzeichnet ist, bleibt bei der Zerlegung in Wörter zusammen.
:::

Das englische Wort „quote“ bedeutet hier „in Anführungszeichen setzen“. Die drei Mittel unterscheiden sich darin, wie viel sie schützen. In allen drei Fällen entfernt die Shell die Anführungszeichen und Schrägstriche, bevor das Programm startet.

::::beispiel Dreimal derselbe Name
```console
$ printf "[%s]\n" 'mein bericht.txt' "mein bericht.txt" mein\ bericht.txt
[mein bericht.txt]
[mein bericht.txt]
[mein bericht.txt]
```

Alle drei Schreibweisen ergeben dasselbe einzelne Argument, ohne Anführungszeichen und ohne Schrägstrich.
::::

⁠**Kurz gesagt:** Quoting kennzeichnet Zeichen, die die Shell wörtlich nehmen soll; es gibt einfache und doppelte Anführungszeichen und den umgekehrten Schrägstrich.

:::hintergrund Eine vierte Form: $'…'
bash und seit 2024 auch der Standard für Unix-Shells kennen eine weitere Form, einfache Anführungszeichen mit einem Dollarzeichen davor. Darin gelten Schreibweisen wie `\n` für ein Zeilenende und `\t` für einen Tabulator; sonst ist alles wörtlich wie zwischen einfachen Anführungszeichen:

```console
$ echo $'Milch\nBrot'
Milch
Brot
```

Dieselbe Form hat `printf` im Hintergrund-Kasten zur Worttrennung benutzt, um die unsichtbaren Zeichen in `IFS` zu zeigen.
:::

### Einfache Anführungszeichen

<span class="anker" id="stufe-3-4"></span>

Das stärkste Mittel braucht man, wenn ein Text ganz genau so beim Programm ankommen soll, wie er dasteht: ein Muster für `find`, ein Satz mit Dollarzeichen.

:::definition Definition 3.4 (Einfache Anführungszeichen)
<span class="anker" id="satz-3-4"></span>

Zwischen einfachen Anführungszeichen `'…'` nimmt die Shell jedes Zeichen wörtlich. Es findet keine Erweiterung statt, und alles dazwischen bleibt ein Wort. Ein einfaches Anführungszeichen selbst kann darin nicht vorkommen, auch nicht mit einem umgekehrten Schrägstrich davor.
:::

::::beispiel Alles bleibt, wie es ist
```console
$ echo '$HOME ~ *.txt {a,b} $((1+1))'
$HOME ~ *.txt {a,b} $((1+1))
$ echo Preis: $5
Preis:
$ echo 'Preis: $5'
Preis: $5
$ echo 'Gabi'\''s Café'
Gabi's Café
```

Ohne Anführungszeichen hält die Shell `$5` für einen Parameter wie `$?`, der hier keinen Wert hat, und der Preis verschwindet. Ein Apostroph im Text gelingt mit einem Umweg: Man beendet die einfachen Anführungszeichen, schreibt `\'` und beginnt neue. Die Shell fügt die Stücke zu einem Wort zusammen.
::::

⁠**Kurz gesagt:** Zwischen einfachen Anführungszeichen ist alles wörtlich; nur ein einfaches Anführungszeichen selbst geht dort nicht.

### Doppelte Anführungszeichen

<span class="anker" id="stufe-3-5"></span>

Oft will man beides: Ein Wert soll eingesetzt werden, aber danach nicht zerfallen. Das ist genau der Fall von `ls $datei`.

:::definition Definition 3.5 (Doppelte Anführungszeichen)
<span class="anker" id="satz-3-5"></span>

Zwischen doppelten Anführungszeichen `"…"` nimmt die Shell alle Zeichen wörtlich, außer drei: `$` leitet weiterhin eine Parametererweiterung, eine Befehlsersetzung oder eine Arithmetik ein, `` ` `` eine Befehlsersetzung in alter Schreibweise, und `\` wirkt noch vor `$`, `` ` ``, `"`, `\` und dem Zeilenende. Worttrennung, Pfadnamen-Erweiterung, Tilde- und Klammererweiterung finden nicht statt; das Ganze bleibt ein Wort.
:::

::::beispiel Einsetzen ja, Zerlegen nein
```console
$ ls "$datei"
'mein bericht.txt'
$ echo "$HOME ~ *.txt {a,b} $((1+1))"
/home/student ~ *.txt {a,b} 2
$ echo "$(cat einkauf.txt)"
Milch
Brot
Äpfel
Kaffee
$ echo "Preis: \$5"
Preis: $5
$ echo "Gabi's Café"
Gabi's Café
```

Jetzt findet `ls` die Datei; die Anführungszeichen, die es um den Namen setzt, kennst du aus [Kapitel 3, Abschnitt 3.7](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/den-inhalt-eines-verzeichnisses-anzeigen.html#stufe-3-7). In der zweiten Zeile werden `$HOME` und `$((1+1))` eingesetzt, Tilde, Muster und Klammern bleiben stehen. Die Einkaufsliste behält ihre Zeilenenden, weil die Worttrennung ausbleibt. Der umgekehrte Schrägstrich macht aus `$5` ein gewöhnliches Dollarzeichen, und ein Apostroph ist zwischen doppelten Anführungszeichen ein gewöhnliches Zeichen.
::::

⁠**Kurz gesagt:** Zwischen doppelten Anführungszeichen setzt die Shell Werte mit `$` ein, zerlegt sie aber nicht und wertet keine Muster, Tilden und Klammern aus.

:::hintergrund Das Ausrufezeichen
In der interaktiven bash hat das Ausrufezeichen eine Sonderrolle: Es ruft frühere Befehle aus dem Verlauf auf, wie `!!` in [Kapitel 2, Abschnitt 5.2](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/schneller-arbeiten-vervollstandigung-verlauf-tastenkurzel.html#stufe-5-2). Diese Bedeutung behält es auch zwischen doppelten Anführungszeichen:

```console
$ echo "Achtung!Neu"
bash: !Neu: event not found
$ echo 'Achtung!Neu'
Achtung!Neu
```

Die Shell hat in der ersten Zeile im Verlauf nach einem Befehl gesucht, der mit `Neu` beginnt, keinen gefunden und die ganze Zeile verworfen; `echo` ist nicht gelaufen. Zwischen einfachen Anführungszeichen ist das Ausrufezeichen ein gewöhnliches Zeichen. Folgt auf das Ausrufezeichen ein Leerzeichen oder steht es direkt vor dem schließenden Anführungszeichen, bleibt es auch zwischen doppelten Anführungszeichen harmlos.
:::

### Der umgekehrte Schrägstrich

<span class="anker" id="stufe-3-6"></span>

Manchmal soll nur ein einzelnes Zeichen seine Sonderbedeutung verlieren: ein Leerzeichen in einem Namen, ein Stern, ein Dollarzeichen. Anführungszeichen um das ganze Wort wären dafür mehr als nötig.

:::definition Definition 3.6 (Umgekehrter Schrägstrich)
<span class="anker" id="satz-3-6"></span>

Ein __umgekehrter Schrägstrich__ `\` außerhalb von Anführungszeichen nimmt dem Zeichen direkt dahinter seine besondere Bedeutung. Steht er am Ende einer Zeile, verbindet er sie mit der nächsten Zeile zu einer einzigen Befehlszeile.
:::

Die Tabulatortaste setzt ihn von selbst vor Leerzeichen in Dateinamen ([Kapitel 3, Abschnitt 3.7](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/den-inhalt-eines-verzeichnisses-anzeigen.html#stufe-3-7)). Wenn du eine Zeile mit `\` beendest und die Eingabetaste drückst, zeigt die Shell am Anfang der nächsten Zeile ein `>`, wie beim Here-Document in [Kapitel 4, Abschnitt 3.2](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/eingaben-umleiten.html#stufe-3-2), und wartet auf den Rest.

::::beispiel Einzelne Zeichen schützen
```console
$ echo \$HOME \* \~
$HOME * ~
$ ls mein\ bericht.txt
'mein bericht.txt'
$ echo Milch Brot \
> Äpfel Kaffee
Milch Brot Äpfel Kaffee
```

In der ersten Zeile bleiben Dollarzeichen, Stern und Tilde gewöhnliche Zeichen. In der letzten verbindet der umgekehrte Schrägstrich zwei getippte Zeilen; `echo` bekommt vier Argumente.
::::

Tabelle [1](#tab-1) stellt zusammen, was die drei Mittel des Quotings verhindern.

<span class="anker" id="tab-1"></span>

**Tabelle 1:** Was die Shell mit einem Wort noch macht, je nach Quoting. „ja“ heißt: Die Shell wertet das Zeichen aus; „nein“: Sie nimmt es wörtlich.

|  | ohne | `"…"` | `'…'` | `\` vor dem Zeichen |
|---|---|---|---|---|
| Leerzeichen trennt Wörter | ja | nein | nein | nein |
| Muster `*` `?` `[…]` | ja | nein | nein | nein |
| Tilde und Klammern `{…}` | ja | nein | nein | nein |
| `$NAME`, `$(…)`, `$((…))` | ja | ja | nein | nein |
| Worttrennung des eingesetzten Werts | ja | nein | entfällt | entfällt |

⁠**Kurz gesagt:** Der umgekehrte Schrägstrich schützt genau ein Zeichen; am Zeilenende setzt er die Befehlszeile in der nächsten Zeile fort.

### Das Entfernen der Anführungszeichen

<span class="anker" id="stufe-3-7"></span>

Die Anführungszeichen kommen beim Programm nicht an; das hat schon [Kapitel 3](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-verzeichnisse-und-pfade.html) gesagt. Offen ist noch, was mit Anführungszeichen geschieht, die man aneinanderhängt, die nichts umschließen oder die in einem Wert stehen. Abbildung [12](#abb-12) zeigt den letzten Schritt der Expansion.

:::abbildung linux/k5entfernen 12
Das getippte Wort `"mein "'bericht'.txt` besteht aus drei Stücken: einem Stück in doppelten Anführungszeichen, einem in einfachen und einem ohne. Die Shell entfernt die vier Anführungszeichen und hängt die Stücke aneinander; übrig bleibt das eine Argument `mein bericht.txt`.
:::

:::definition Definition 3.7 (Entfernen der Anführungszeichen)
<span class="anker" id="satz-3-7"></span>

Als letzten Schritt der Expansion entfernt die Shell alle Anführungszeichen und umgekehrten Schrägstriche, die du getippt hast und die nicht selbst geschützt sind. Zeichen dieser Art, die erst durch eine Erweiterung in die Zeile gekommen sind, etwa aus dem Wert einer Variablen, bleiben stehen.
:::

::::beispiel Zusammengesetzt, leer und im Wert
```console
$ printf "[%s]\n" "mein "'bericht'.txt
[mein bericht.txt]
$ printf "[%s]\n" "" Ende
[]
[Ende]
$ x='"a b"'
$ printf "[%s]\n" $x
["a]
[b"]
```

Stücke ohne Leerzeichen dazwischen bilden ein Wort. Zwei Anführungszeichen ohne Inhalt ergeben ein leeres Argument, das erhalten bleibt, anders als eine leere Variable ohne Anführungszeichen in Unterabschnitt [3.2](#stufe-3-2). Die Anführungszeichen im Wert von `x` sind dagegen Daten: Sie schützen nichts, die Worttrennung zerlegt den Wert am Leerzeichen, und die Anführungszeichen landen in den Argumenten.
::::

⁠**Kurz gesagt:** Zum Schluss entfernt die Shell die getippten Anführungszeichen und Schrägstriche und fügt die Stücke eines Worts zusammen; Anführungszeichen aus Werten bleiben gewöhnliche Zeichen.

### Die Regel: Erweiterungen in doppelte Anführungszeichen

<span class="anker" id="stufe-3-8"></span>

Aus den letzten Unterabschnitten ergibt sich eine Gewohnheit, die viele Fehler verhindert. Wie wichtig sie ist, zeigt ein Versuch, bei dem ohne sie die falschen Dateien verschwinden.

:::satz Satz 3.8 (Regel für das Quoting)
<span class="anker" id="satz-3-8"></span>

Setze jede Parametererweiterung und jede Befehlsersetzung in doppelte Anführungszeichen, also `"$datei"` und `"$(befehl)"`, außer du willst ausdrücklich, dass ihr Ergebnis in Wörter zerfällt. Setze Text, den ein Programm unverändert bekommen soll, etwa ein Muster für `find`, in einfache Anführungszeichen.
:::

:::warnung rm $datei ohne Anführungszeichen
Ohne Anführungszeichen kann `rm` andere Dateien löschen als die gemeinte. Probiere es nur in deinem Übungsverzeichnis aus. Dort liegt `mein bericht.txt`, und `datei` enthält diesen Namen. Lege zusätzlich zwei Dateien namens `mein` und `bericht.txt` an:

```console
$ touch mein bericht.txt
$ ls
 bericht.txt   foto1.jpg    foto2.jpg  'mein bericht.txt'   urlaub
 einkauf.txt   foto10.jpg   mein        notiz.txt
$ rm $datei
$ ls
 einkauf.txt   foto10.jpg  'mein bericht.txt'   urlaub
 foto1.jpg     foto2.jpg    notiz.txt
```

Gemeint war `mein bericht.txt`, gelöscht wurden `mein` und `bericht.txt`, ohne Rückfrage und ohne Meldung. Abbildung [13](#abb-13) zeigt, wie es dazu kam. Mit `rm "$datei"` wäre genau die gemeinte Datei verschwunden.
:::

:::abbildung linux/k5datensteuerung 13
`rm $datei` mit dem Wert `mein bericht.txt` in einem Verzeichnis, in dem es auch `mein` und `bericht.txt` gibt. Die zwei Argumente, die die Worttrennung aus dem einen Namen gemacht hat, treffen zwei andere Dateien: `rm` löscht sie, die gemeinte bleibt liegen.
:::

⁠**Kurz gesagt:** Erweiterungen gehören in doppelte Anführungszeichen, Text für Programme in einfache; sonst kann ein Wert zu mehreren Argumenten werden.

:::hintergrund Daten werden zu Steuerung
Was bei `rm $datei` schiefgeht, hat ein allgemeines Muster. Der Wert der Variablen ist als Daten gemeint, als ein einziger Dateiname. Ohne Anführungszeichen deutet die Shell Teile davon als Steuerzeichen: das Leerzeichen als Grenze zwischen Argumenten, einen Stern als Muster. Ein Minus am Anfang des Werts deutet dagegen erst das Programm als Beginn einer Option, und das auch zwischen Anführungszeichen; davor schützt nur `--` aus [Kapitel 2, Abschnitt 2.7](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/der-aufbau-einer-befehlszeile.html#stufe-2-7). Wer den Wert bestimmt, etwa durch einen geschickt gewählten Dateinamen, bestimmt so mit, was der Befehl tut. Dieselbe Verwechslung von Daten und Befehl steckt hinter vielen Sicherheitslücken in Programmen, die Texte von außen in Befehle einbauen; die Reihe Cybersecurity greift das auf. Die Abhilfe ist hier immer dieselbe: Daten so kennzeichnen, dass sie Daten bleiben. Erfahrene Anwender halten sich deshalb an die einfache Regel, im Zweifel jede Erweiterung in doppelte Anführungszeichen zu setzen.
:::

### Die Reihenfolge aller Schritte

<span class="anker" id="stufe-3-9"></span>

Jetzt sind alle Erweiterungen bekannt. Manche Überraschung erklärt sich erst, wenn man weiß, in welcher Reihenfolge die Shell sie ausführt. Als Bild zur Orientierung ist das eine Werkstatt mit mehreren Stationen, durch die jede Befehlszeile der Reihe nach läuft; erst am Ende wird das Programm mit der fertigen Liste der Argumente gestartet. Abbildung [14](#abb-14) schickt eine Zeile hindurch.

:::abbildung linux/k5werkstatt 14
Die Werkstatt der Shell. Die Zeile `ls -l {foto,notiz}* "$HOME"` läuft durch die Stationen: Zerlegen in Wörter, Klammererweiterung (`foto* notiz*`), Parametererweiterung (`/home/student`), Worttrennung (ändert hier nichts), Pfadnamen-Erweiterung (die Namen der Fotos und `notiz.txt`), Entfernen der Anführungszeichen. Unten steht die fertige Argumentliste, mit der `ls` startet.
:::

:::satz Satz 3.9 (Reihenfolge der Expansion)
<span class="anker" id="satz-3-9"></span>

Die Shell bearbeitet eine Befehlszeile in dieser Reihenfolge:

<ol>

<li>

Sie zerlegt die Zeile in Wörter und beachtet dabei das Quoting; ist das erste Wort ein Alias, ersetzt sie es ([Kapitel 2, Abschnitt 3.4](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/arten-von-befehlen.html#stufe-3-4)).

</li>

<li>

Klammererweiterung.

</li>

<li>

Tilde-Erweiterung, Parametererweiterung, Arithmetik und Befehlsersetzung, in einem Durchgang von links nach rechts.

</li>

<li>

Worttrennung der Ergebnisse aus Schritt 3, die nicht zwischen doppelten Anführungszeichen stehen.

</li>

<li>

Pfadnamen-Erweiterung.

</li>

<li>

Entfernen der Anführungszeichen.

</li>

</ol>

Danach richtet sie die Umleitungen ein ([Kapitel 4, Abschnitt 2](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/ausgaben-umleiten.html#stufe-2)) und führt den Befehl aus.
:::

Jeder Schritt arbeitet nur mit dem, was der vorige übrig gelassen hat. Was ein späterer Schritt erzeugt, sieht ein früherer nie. Mit `printf` lässt sich die fertige Argumentliste aus Abbildung [14](#abb-14) nachprüfen; statt `ls` bekommt `printf` dieselben Wörter:

```console
$ printf "[%s]\n" -l {foto,notiz}* "$HOME"
[-l]
[foto1.jpg]
[foto10.jpg]
[foto2.jpg]
[notiz.txt]
[/home/student]
```

::::beispiel Was aus der Reihenfolge folgt
```console
$ n=3
$ echo {1..$n}
{1..3}
$ ordner="~/linuxk5"
$ ls $ordner
ls: cannot access '~/linuxk5': No such file or directory
$ muster="*.jpg"
$ echo $muster "$muster"
foto1.jpg foto10.jpg foto2.jpg *.jpg
```

Die Klammererweiterung kommt vor der Parametererweiterung; sie sah `{1..$n}` und darin keine gültige Folge, und als `$n` danach zu `3` wurde, war ihr Schritt vorbei. In `ordner` steht wegen der Anführungszeichen eine echte Tilde; die Tilde-Erweiterung ersetzt aber nur getippte Tilden, keine, die eine Erweiterung eingesetzt hat. Die Pfadnamen-Erweiterung kommt nach der Worttrennung und wirkt deshalb auf das ungeschützte `$muster`, nicht auf `"$muster"`.
::::

⁠**Kurz gesagt:** Zerlegen, Klammern, dann Tilde, Parameter, Arithmetik und Befehlsersetzung von links nach rechts, dann Worttrennung, Muster und zum Schluss das Entfernen der Anführungszeichen.

:::hintergrund Klammern kennt nicht jede Shell
Der Standard für Unix-Shells beschreibt die Schritte 1 und 3 bis 6. Die Klammererweiterung ist eine Besonderheit von bash und einigen anderen Shells. Unter Ubuntu startet der Befehl `sh` die kleine Shell dash, die sich eng an den Standard hält:

```console
$ bash -c 'echo {a,b}'
a b
$ sh -c 'echo {a,b}'
{a,b}
```

`bash -c` und `sh -c` führen den Text in den einfachen Anführungszeichen in einer neuen Shell aus. dash lässt die Klammern stehen. Wer Befehle für andere Shells schreibt, verlässt sich deshalb nicht auf Klammern.
:::

### Aufgaben zu Abschnitt [3](#stufe-3)

<span class="anker" id="stufe-3-10"></span>

:::aufgabe Aufgabe 9 ★ Dreimal HOME
<span class="anker" id="aufg-9"></span>

Sage voraus, was `echo "$HOME" '$HOME' \$HOME "~" ~ "*.txt" *.txt` in deinem Übungsverzeichnis ausgibt, und prüfe es. Ordne jedem der sieben Wörter zu, welche Erweiterung gewirkt hat und welche das Quoting verhindert hat.

:::loesung
```console
$ echo "$HOME" '$HOME' \$HOME "~" ~ "*.txt" *.txt
/home/student $HOME $HOME ~ /home/student *.txt Lea_notizen.txt einkauf.txt notiz.txt
```

`"$HOME"`: Parametererweiterung, auch zwischen doppelten Anführungszeichen. `'$HOME'`: einfache Anführungszeichen verhindern jede Erweiterung. `\$HOME`: Der umgekehrte Schrägstrich nimmt dem Dollarzeichen die Bedeutung. `"~"`: Zwischen doppelten Anführungszeichen gibt es keine Tilde-Erweiterung. `~`: Tilde-Erweiterung. `"*.txt"`: Zwischen doppelten Anführungszeichen gibt es keine Pfadnamen-Erweiterung. `*.txt`: Pfadnamen-Erweiterung zu den Textdateien; in der Testsitzung lag dort noch `Lea_notizen.txt` aus Aufgabe [5](variablen-befehlsersetzung-und-arithmetik.html#aufg-5). Die sieben getippten Wörter wurden so zu neun Argumenten.
:::
:::

:::aufgabe Aufgabe 10 ★★ Ein Name mit Leerzeichen
<span class="anker" id="aufg-10"></span>

Lege im Übungsverzeichnis ein Unterverzeichnis `versuch` an, wechsle hinein und lege dort die Datei `mein bericht.txt` an. Weise den Namen der Variablen `datei` zu. (a) Sage voraus, was `ls $datei` und `ls "$datei"` melden, und prüfe es. (b) Du willst eine Kopie namens `sicherung.txt` anlegen. Was meldet `cp $datei sicherung.txt`, und warum? Wie lautet die richtige Zeile? (c) Weise `X="a b"` zu und vergleiche `printf "[%s]\n" $X` mit `printf "[%s]\n" "$X"`.

:::loesung
```console
$ mkdir versuch
$ cd versuch
$ touch "mein bericht.txt"
$ datei="mein bericht.txt"
$ ls $datei
ls: cannot access 'mein': No such file or directory
ls: cannot access 'bericht.txt': No such file or directory
$ ls "$datei"
'mein bericht.txt'
$ cp $datei sicherung.txt
cp: target 'sicherung.txt': No such file or directory
$ cp "$datei" sicherung.txt
$ ls
'mein bericht.txt'   sicherung.txt
$ X="a   b"
$ printf "[%s]\n" $X
[a]
[b]
$ printf "[%s]\n" "$X"
[a   b]
$ cd ..
```

(a) Ohne Anführungszeichen zerlegt die Worttrennung den Wert am Leerzeichen; `ls` sucht `mein` und `bericht.txt`. Mit Anführungszeichen bekommt es ein Argument und findet die Datei. (b) `cp` bekommt drei Argumente: `mein`, `bericht.txt` und `sicherung.txt`. Bei mehr als zwei Argumenten muss das letzte ein Verzeichnis sein, in das die übrigen kopiert werden ([Kapitel 3, Abschnitt 6.1](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/kopieren-verschieben-loschen.html#stufe-6-1)); ein Verzeichnis `sicherung.txt` gibt es nicht, also bricht `cp` ab. Richtig ist `cp "$datei" sicherung.txt`. (c) Ohne Anführungszeichen zerfällt der Wert in zwei Wörter, und die drei Leerzeichen verschwinden; mit Anführungszeichen bleibt er ein Wort, samt allen Leerzeichen.
:::
:::

:::aufgabe Aufgabe 11 ★★ Argumente zählen
<span class="anker" id="aufg-11"></span>

Die Variable `leer` hat einen leeren Wert. Wie viele Argumente bekommt `printf` in dieser Zeile, und wie lauten sie? Prüfe deine Antwort am Rechner.

```console
$ printf "[%s]\n" a"b c"d 'e f'g "" h\ i $leer
```

:::loesung
Vier Argumente: `ab cd`, `e fg`, ein leeres und `h i`.

```console
$ printf "[%s]\n" a"b c"d 'e f'g "" h\ i $leer
[ab cd]
[e fg]
[]
[h i]
```

`a"b c"d` besteht aus drei Stücken ohne Leerzeichen dazwischen, also aus einem Wort; das Leerzeichen in den Anführungszeichen gehört dazu. Ebenso `'e f'g`. `""` ist ein leeres, aber vorhandenes Argument. In `h\ i` ist das Leerzeichen geschützt. `$leer` ohne Anführungszeichen ergibt nach der Worttrennung gar kein Wort.
:::
:::

:::aufgabe Aufgabe 12 ★★★ Drei Überraschungen
<span class="anker" id="aufg-12"></span>

Erkläre jedes der drei Ergebnisse mit der Reihenfolge aus Unterabschnitt [3.9](#stufe-3-9) und gib an, wie man es richtig macht, soweit das mit den Mitteln dieses Kapitels geht: (a) Nach `n=5` gibt `echo {1..$n}` nicht die Zahlen 1 bis 5 aus. (b) Nach `muster='*.txt'` zeigt `ls $muster` Dateien, `ls "$muster"` dagegen eine Fehlermeldung. (c) Nach `ordner='~/linuxk5'` scheitert `cd $ordner`.

:::loesung
```console
$ n=5
$ echo {1..$n}
{1..5}
$ muster='*.txt'
$ ls $muster
Lea_notizen.txt  einkauf.txt  notiz.txt
$ ls "$muster"
ls: cannot access '*.txt': No such file or directory
$ ordner='~/linuxk5'
$ cd $ordner
bash: cd: ~/linuxk5: No such file or directory
$ ordner=~/linuxk5
$ cd $ordner
$ pwd
/home/student/linuxk5
```

(a) Die Klammererweiterung ist Schritt 2, die Parametererweiterung Schritt 3. Als die Klammern geprüft wurden, stand dort `{1..$n}`, keine gültige Folge; danach wurde `$n` ersetzt, aber Schritt 2 war vorbei. Mit der Klammererweiterung allein lässt sich das nicht lösen: Sie kennt nur Grenzen, die als Zahlen in der Zeile stehen, etwa `{1..5}`. (b) In `muster` steht der Text `*.txt`. Ohne Anführungszeichen durchläuft das Ergebnis der Parametererweiterung Worttrennung und Pfadnamen-Erweiterung (Schritte 4 und 5) und wird zu Dateinamen. Mit Anführungszeichen entfallen beide Schritte, `ls` bekommt den Text `*.txt` und sucht eine Datei dieses Namens. (c) Die einfachen Anführungszeichen haben eine echte Tilde in die Variable gelegt. Die Tilde-Erweiterung wirkt aber nur auf getippte Tilden am Wortanfang, nicht auf Text, den eine Erweiterung eingesetzt hat. Richtig ist `ordner=~/linuxk5` ohne Anführungszeichen, dann ersetzt die Shell die Tilde schon bei der Zuweisung, oder `ordner="$HOME/linuxk5"`.
:::
:::

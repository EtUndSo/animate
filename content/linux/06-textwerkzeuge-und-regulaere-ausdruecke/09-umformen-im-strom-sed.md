---
title: Umformen im Strom: sed
pfad: Informatik / Linux und Kommandozeile / Textwerkzeuge und reguläre Ausdrücke
adresse: informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke
knoten: Kapitel 6: Textwerkzeuge und reguläre Ausdrücke
order: 6110900
summary: grep wählt Zeilen aus, tr ersetzt einzelne Zeichen.
tags: sed, Zeilenadresse, Rückverweis
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
`grep` wählt Zeilen aus, `tr` ersetzt einzelne Zeichen. Oft möchte man aber ganze Stücke einer Zeile umformen: ein Datum in deutscher Schreibweise, Kommas zu Semikolons, zwei Felder vertauscht. Dieser Abschnitt zeigt ein Werkzeug, das Zeilen beim Durchlaufen bearbeitet, mit regulären Ausdrücken ersetzt, Zeilen auswählt und löscht und bei Bedarf die Datei selbst ändert.
:::

### Der Strom-Editor sed

<span class="anker" id="stufe-8-1"></span>

Einen Texteditor wie `nano` aus [Kapitel 3](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-verzeichnisse-und-pfade.html) bedient man von Hand: Cursor setzen, tippen, speichern. Für hundert gleiche Änderungen in tausend Zeilen ist das zu mühsam. Ein Editor ohne Bildschirm, der dieselben Befehle auf jede Zeile eines Stroms anwendet, erledigt das in einem Zug. Abbildung [26](#abb-26) zeigt seinen Ablauf.

:::abbildung linux/k6sed 26
Der Kreislauf von `sed`: Eine Zeile kommt aus der Eingabe in einen Zwischenspeicher. Die Befehle laufen der Reihe nach über den Zwischenspeicher, hier `s/,/;/`, das erste Komma wird ein Semikolon. Dann wird der Zwischenspeicher ausgegeben und die nächste Zeile geholt. Die Datei, aus der gelesen wird, bleibt grau und unverändert.
:::

:::definition Definition 8.1 (sed)
<span class="anker" id="satz-8-1"></span>

Der Befehl __sed__, kurz für „stream editor“, liest seine Eingabe Zeile für Zeile. Jede Zeile legt er in einen Zwischenspeicher, wendet darauf der Reihe nach die Befehle an, die in seinem ersten Argument nach den Optionen stehen, und schreibt den Zwischenspeicher danach aus. Die gelesenen Dateien ändert er dabei nicht.
:::

Das erste Argument steht in einfachen Anführungszeichen, denn es enthält meist reguläre Ausdrücke. Ohne Dateinamen liest `sed` seine Standardeingabe; es ist also ein Filter.

::::beispiel Ein Komma je Zeile
```console
$ sed 's/,/;/' laeufe.csv | head -n 3
datum;name,km,minuten
2026-11-02;Anna,5.0,28
2026-11-02;Ben,10.5,62
```

Der Befehl `s/,/;/` hat in jeder Zeile das erste Komma durch ein Semikolon ersetzt. `laeufe.csv` selbst ist unverändert.
::::

⁠**Kurz gesagt:** `sed` wendet seine Befehle auf jede Zeile eines Stroms an und schreibt das Ergebnis aus, ohne die Datei zu ändern.

### Ersetzen: der Befehl s

<span class="anker" id="stufe-8-2"></span>

Der wichtigste Befehl von `sed` sucht in der Zeile mit einem regulären Ausdruck und ersetzt den Treffer.

:::definition Definition 8.2 (Der Befehl s)
<span class="anker" id="satz-8-2"></span>

`s/ausdruck/ersatz/` ersetzt in jeder Zeile den ersten Treffer des regulären Ausdrucks durch den Ersatztext. Mit dem Zusatz `g` dahinter, `s/ausdruck/ersatz/g`, ersetzt er alle Treffer der Zeile. Ein `&` im Ersatztext steht für den gefundenen Treffer. Statt des Schrägstrichs darf jedes andere Zeichen außer dem umgekehrten Schrägstrich und dem Zeilenende die drei Teile trennen.
:::

`sed` benutzt ohne Option die Grundform aus Unterabschnitt [7.5](regulare-ausdrucke-wiederholungen-gruppen-und-alternativen.html#stufe-7-5), mit `-E` die erweiterte. Für den Treffer gilt die Regel vom längsten Treffer aus Unterabschnitt [7.6](regulare-ausdrucke-wiederholungen-gruppen-und-alternativen.html#stufe-7-6).

::::beispiel Alle Kommas, Zahlen in Klammern, Pfade
```console
$ sed 's/,/;/g' laeufe.csv | head -n 3
datum;name;km;minuten
2026-11-02;Anna;5.0;28
2026-11-02;Ben;10.5;62
$ echo 'Anna lief 5 km' | sed 's/[0-9][0-9]*/[&]/'
Anna lief [5] km
$ echo '/home/student/linuxk6' | sed 's|/|:|g'
:home:student:linuxk6
```

Mit `g` werden aus allen Kommas Semikolons, so wie ein Tabellenprogramm mit deutscher Einstellung es erwartet. `[0-9][0-9]*` ist „eine Ziffer und beliebig viele weitere“ in der Grundform; `&` setzt die gefundene Zahl in eckige Klammern. Im letzten Befehl trennen senkrechte Striche die Teile, weil die Schrägstriche selbst ersetzt werden sollen.
::::

⁠**Kurz gesagt:** `s/ausdruck/ersatz/` ersetzt den ersten Treffer je Zeile, mit `g` alle; `&` ist der Treffer selbst.

### Zeilen auswählen: Zeilenadressen, -n und p

<span class="anker" id="stufe-8-3"></span>

Nicht jede Änderung soll jede Zeile treffen: nur die Kopfzeile, nur Bens Läufe, nur die Zeilen 2 bis 4. Außerdem kann `sed` Zeilen nicht nur ändern, sondern auch auswählen wie `grep`, `head` oder `tail`. Abbildung [27](#abb-27) zeigt vier Arten, Zeilen zu wählen.

:::abbildung linux/k6zeilenadressen 27
Die zehn Zeilen des Lauftagebuchs, viermal nebeneinander. Bei `2,4` leuchten die Zeilen 2 bis 4, bei `$` die letzte, bei `/Clara/` die beiden Zeilen mit Clara, bei `1` die Kopfzeile. Über jeder Spalte steht die Zeilenadresse, darunter, welche Zeilen ein Befehl mit ihr trifft.
:::

:::definition Definition 8.3 (Zeilenadresse, -n, p)
<span class="anker" id="satz-8-3"></span>

Eine __Zeilenadresse__ vor einem Befehl wählt die Zeilen, auf die er wirkt: eine Zeilennummer, `$` für die letzte Zeile, `/ausdruck/` für alle Zeilen mit einem Treffer, oder zwei Zeilenadressen mit einem Komma dazwischen für alle Zeilen von der einen bis zur anderen. Ohne Zeilenadresse wirkt ein Befehl auf jede Zeile. Die Option `-n` schaltet die Ausgabe nach jeder Zeile ab; dann schreibt nur noch der Befehl `p` Zeilen aus.
:::

`sed -n '2,4p'` schreibt also nur die Zeilen 2 bis 4. Ohne `-n` erschienen sie doppelt, einmal durch `p` und einmal durch die gewöhnliche Ausgabe.

::::beispiel Auswählen und gezielt ändern
```console
$ sed -n '2,4p' laeufe.csv
2026-11-02,Anna,5.0,28
2026-11-02,Ben,10.5,62
2026-11-03,Clara,7.2,41
$ sed -n '/Clara/p' laeufe.csv
2026-11-03,Clara,7.2,41
2026-11-07,Clara,8.0,44
$ sed -n '$p' laeufe.csv
2026-11-09,Anna,5.0,27
$ sed '/Ben/s/,/;/g' laeufe.csv | head -n 4
datum,name,km,minuten
2026-11-02,Anna,5.0,28
2026-11-02;Ben;10.5;62
2026-11-03,Clara,7.2,41
```

Die ersten drei Befehle tun, was `head` mit `tail`, `grep` und `tail -n 1` tun. Im letzten wirkt das Ersetzen nur auf Zeilen mit `Ben`; die anderen gehen unverändert durch.
::::

⁠**Kurz gesagt:** Eine Zeilenadresse wie `3`, `$`, `/ausdruck/` oder `2,4` beschränkt einen Befehl auf bestimmte Zeilen; `-n` mit `p` gibt nur diese aus.

### Zeilen löschen: der Befehl d

<span class="anker" id="stufe-8-4"></span>

Das Gegenstück zum Auswählen ist das Weglassen: die Kopfzeile, alle Läufe einer Person.

:::definition Definition 8.4 (Der Befehl d)
<span class="anker" id="satz-8-4"></span>

Der Befehl `d` löscht den Zwischenspeicher, gibt nichts aus und beginnt sofort mit der nächsten Zeile. Mit einer Zeilenadresse davor fallen genau die gewählten Zeilen aus dem Strom.
:::

Gelöscht wird nur im Strom, nicht in der Datei.

::::beispiel Kopfzeile weg, Anna weg
```console
$ sed '1d' laeufe.csv | head -n 2
2026-11-02,Anna,5.0,28
2026-11-02,Ben,10.5,62
$ sed '/Anna/d' laeufe.csv
datum,name,km,minuten
2026-11-02,Ben,10.5,62
2026-11-03,Clara,7.2,41
2026-11-05,Ben,5.0,31
2026-11-07,Clara,8.0,44
2026-11-08,Ben,21.1,128
```

`sed '1d'` leistet dasselbe wie `tail -n +2`, `sed '/Anna/d'` dasselbe wie `grep -v Anna`.
::::

⁠**Kurz gesagt:** `d` lässt die gewählten Zeilen aus dem Strom fallen; `1d` entfernt die Kopfzeile.

:::hintergrund Früher aufhören: der Befehl q
Der Befehl `q` beendet `sed`, nachdem die aktuelle Zeile ausgegeben ist. `sed 3q` schreibt deshalb die ersten drei Zeilen und hört auf zu lesen, wie `head -n 3`:

```console
$ sed 3q laeufe.csv
datum,name,km,minuten
2026-11-02,Anna,5.0,28
2026-11-02,Ben,10.5,62
```

Weil `sed` danach nicht weiterliest, ist das auch bei riesigen Dateien schnell.
:::

### Gruppen und Rückverweise

<span class="anker" id="stufe-8-5"></span>

Das Datum im Lauftagebuch steht als `2026-11-02`; wer es in deutscher Schreibweise `02.11.2026` haben will, muss Teile des Treffers in anderer Reihenfolge wieder einsetzen. Abbildung [28](#abb-28) zeigt, wie das geht.

:::abbildung linux/k6gruppen 28
Oben das Datum `2026-11-02` und der Ausdruck `^([0-9]{4})-([0-9]{2})-([0-9]{2})`. Die drei Gruppen färben je ein Stück des Datums: `2026` als 1, `11` als 2, `02` als 3. Unten der Ersatz `\3.\2.\1`: Die gefärbten Stücke wandern in der neuen Reihenfolge an ihre Plätze, dazwischen Punkte. Es entsteht `02.11.2026`.
:::

:::definition Definition 8.5 (Rückverweis)
<span class="anker" id="satz-8-5"></span>

Jede Gruppe eines Ausdrucks merkt sich das Stück, auf das sie gepasst hat. Im Ersatztext von `s` setzt ein __Rückverweis__ `\1` bis `\9` das Stück der ersten bis neunten Gruppe ein; gezählt werden die öffnenden Klammern von links.
:::

In der erweiterten Form, mit `sed -E`, schreibt man die Gruppen mit einfachen runden Klammern.

::::beispiel Datum umdrehen, Felder tauschen
```console
$ sed -E 's/^([0-9]{4})-([0-9]{2})-([0-9]{2})/\3.\2.\1/' laeufe.csv | head -n 3
datum,name,km,minuten
02.11.2026,Anna,5.0,28
02.11.2026,Ben,10.5,62
$ sed -E 's/^([^,]*),([^,]*)/\2,\1/' laeufe.csv | head -n 3
name,datum,km,minuten
Anna,2026-11-02,5.0,28
Ben,2026-11-02,10.5,62
```

In der Kopfzeile steht kein Datum, also kein Treffer, und sie bleibt, wie sie war. Im zweiten Befehl ist `[^,]*` ein Feld, eine Folge von Zeichen ohne Komma; die ersten beiden Felder tauschen die Plätze, in jeder Zeile, auch in der Kopfzeile.
::::

⁠**Kurz gesagt:** Gruppen merken sich ihre Treffer, und `\1` bis `\9` setzen sie im Ersatztext in beliebiger Reihenfolge wieder ein.

:::hintergrund Dieselbe Ersetzung in der Grundform und Rückverweise im Ausdruck
In der Grundform braucht jede Klammer einen umgekehrten Schrägstrich, und der Befehl wird schwer lesbar:

```console
$ sed 's/^\([0-9]\{4\}\)-\([0-9]\{2\}\)-\([0-9]\{2\}\)/\3.\2.\1/' laeufe.csv | sed -n 2p
02.11.2026,Anna,5.0,28
```

Rückverweise funktionieren nicht nur im Ersatztext, sondern auch im Ausdruck selbst. `\(.\)\1` heißt: ein beliebiges Zeichen und dann dasselbe Zeichen noch einmal. Welcher Name enthält einen doppelten Buchstaben?

```console
$ cut -d, -f2 laeufe.csv | sort -u | grep '\(.\)\1'
Anna
```

Ein solcher Ausdruck muss sich merken, was er gelesen hat, und genau das kann ein endlicher Automat aus Unterabschnitt [7.7](regulare-ausdrucke-wiederholungen-gruppen-und-alternativen.html#stufe-7-7) nicht. Rückverweise im Ausdruck gehen deshalb über reguläre Ausdrücke im mathematischen Sinn hinaus. Der Standard für Unix-Werkzeuge kennt sie nur in der Grundform; GNU `grep` und `sed` erlauben sie auch in der erweiterten. Das Handbuch von GNU `grep` warnt, dass sie eine Suche erheblich verlangsamen können.
:::

### Die Datei selbst ändern: sed -i

<span class="anker" id="stufe-8-6"></span>

Bisher hat `sed` nur in die Standardausgabe geschrieben. Will man das Ergebnis in der Datei haben, liegt die Umleitung in dieselbe Datei nahe.

:::warnung sed mit Umleitung in dieselbe Datei
`sed 's/Ben/Benjamin/' kopie.csv > kopie.csv` hinterlässt eine leere Datei: Die Shell leert `kopie.csv` für die Umleitung, bevor `sed` startet, und `sed` liest dann nichts mehr. Das ist die Kürzungsfalle aus [Kapitel 4, Abschnitt 2.7](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/ausgaben-umleiten.html#stufe-2-7); sie gilt für jedes Werkzeug, nicht nur für `sed`.
:::

:::definition Definition 8.6 (sed -i)
<span class="anker" id="satz-8-6"></span>

Mit der Option `-i` schreibt `sed` das Ergebnis nicht in die Standardausgabe, sondern in eine neue Datei und ersetzt danach die gelesene Datei durch sie. Steht direkt hinter `-i` eine Endung, etwa `-i.bak`, behält `sed` die alte Fassung unter dem Namen mit dieser Endung.
:::

Das „i“ steht für englisch „in place“, an Ort und Stelle. Abbildung [29](#abb-29) zeigt, warum dabei nichts verloren geht.

:::abbildung linux/k6sedi 29
`sed -i` an der Datei `kopie.csv`: `sed` liest die alte Datei Zeile für Zeile und schreibt jede bearbeitete Zeile in eine neue Datei daneben; die alte bleibt dabei unverändert. Erst am Ende nimmt die neue Datei den Namen `kopie.csv` ein, und die alte verschwindet.
:::

::::beispiel Ändern an Ort und Stelle, mit Sicherung
```console
$ cp laeufe.csv kopie.csv
$ sed -i 's/Ben/Benjamin/' kopie.csv
$ grep -c Benjamin kopie.csv
3
```

`sed` schreibt nichts ins Terminal; die drei Änderungen stehen in der Datei. Mit einer Endung bleibt die alte Fassung erhalten:

```console
$ sed -i.bak '1d' kopie.csv
$ head -n 1 kopie.csv kopie.csv.bak
==> kopie.csv <==
2026-11-02,Anna,5.0,28

==> kopie.csv.bak <==
datum,name,km,minuten
```

`head` mit zwei Dateien schreibt über jede ihren Namen. Die Kopfzeile fehlt jetzt in `kopie.csv`, die Sicherung hat sie noch.
::::

:::warnung sed -i fragt nicht nach
`sed -i` ändert die Datei ohne Rückfrage und ohne Papierkorb. Ein Tippfehler im Ausdruck kann Zeilen löschen oder zerstören. Probiere einen Befehl deshalb zuerst ohne `-i` aus, sieh dir die Ausgabe an, und schreibe erst dann `-i` oder `-i.bak` dazu.
:::

⁠**Kurz gesagt:** `sed -i` schreibt das Ergebnis in eine neue Datei, die die alte ersetzt; `-i.bak` behält die alte Fassung. Eine Umleitung in dieselbe Datei leert sie dagegen.

:::hintergrund sed -i und ein zweiter Name
Dass `sed -i` eine neue Datei anlegt, hat eine Folge für harte Links aus [Kapitel 3, Abschnitt 8.3](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/inode-und-links.html#stufe-8-3). Gibt man einer frischen Kopie einen zweiten Namen und ändert die Datei dann mit `sed -i`, gilt die Änderung nur unter dem einen Namen:

```console
$ cp laeufe.csv kopie.csv
$ ln kopie.csv zweitname.csv
$ ls -l kopie.csv zweitname.csv
-rw-r--r-- 2 student student 232 Nov 10 11:10 kopie.csv
-rw-r--r-- 2 student student 232 Nov 10 11:10 zweitname.csv
$ sed -i 's/Clara/Klara/' kopie.csv
$ grep -c Klara kopie.csv zweitname.csv
kopie.csv:2
zweitname.csv:0
$ ls -l kopie.csv zweitname.csv
-rw-r--r-- 1 student student 232 Nov 10 11:10 kopie.csv
-rw-r--r-- 1 student student 232 Nov 10 11:10 zweitname.csv
```

Vorher zeigten beide Namen auf dieselbe Inode, der Linkzähler war 2. `sed -i` hat eine neue Datei angelegt und ihr den Namen `kopie.csv` gegeben; `zweitname.csv` zeigt weiter auf die alte, unveränderte Inode, und beide Zähler sind jetzt 1. Für symbolische Links aus [Kapitel 3, Abschnitt 8.5](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/inode-und-links.html#stufe-8-5) nennt das Handbuch von GNU `sed` dieselbe Folge ausdrücklich: Ohne weitere Option ersetzt `sed -i` den Link durch eine gewöhnliche Datei, und das Ziel des Links bleibt unverändert.
:::

### Aufgaben zu Abschnitt [8](#stufe-8)

<span class="anker" id="stufe-8-7"></span>

:::aufgabe Aufgabe 22 ★★ Für ein Tabellenprogramm umformen
<span class="anker" id="aufg-22"></span>

Ein Tabellenprogramm mit deutscher Einstellung erwartet Semikolons und keine Kopfzeile. (a) Erzeuge diese Fassung mit zwei Aufrufen von `sed` in einer Pipeline. (b) Erzeuge sie mit einem einzigen Aufruf; mehrere Befehle trennt man im ersten Argument durch ein Semikolon. (c) Vertausche zusätzlich Datum und Name, wie im Beispiel zu den Rückverweisen.

:::loesung
```console
$ sed '1d' laeufe.csv | sed 's/,/;/g' | head -n 3
2026-11-02;Anna;5.0;28
2026-11-02;Ben;10.5;62
2026-11-03;Clara;7.2;41
$ sed '1d; s/,/;/g' laeufe.csv | head -n 3
2026-11-02;Anna;5.0;28
2026-11-02;Ben;10.5;62
2026-11-03;Clara;7.2;41
$ sed -E '1d; s/^([^,]*),([^,]*)/\2,\1/; s/,/;/g' laeufe.csv | head -n 3
Anna;2026-11-02;5.0;28
Ben;2026-11-02;10.5;62
Clara;2026-11-03;7.2;41
```

(a) Das erste `sed` löscht die Kopfzeile, das zweite ersetzt alle Kommas. (b) Beide Befehle in einem Aufruf: Für jede Zeile führt `sed` sie der Reihe nach aus; bei Zeile 1 beendet `d` die Arbeit an dieser Zeile, bevor `s` an die Reihe kommt. `head -n 3` kürzt nur die Anzeige. (c) Die Reihenfolge der Befehle zählt: Erst tauschen, solange noch Kommas die Felder trennen, dann die Kommas ersetzen. Andersherum fände der Ausdruck mit `[^,]` keine Kommas mehr und nähme die ganze Zeile als ein Feld.
:::
:::

:::aufgabe Aufgabe 23 ★★ Ein kurzes Datum
<span class="anker" id="aufg-23"></span>

Forme das Datum mit `sed -E` in die Schreibweise `02.11.26` mit zweistelliger Jahreszahl um. Welche Gruppen brauchst du, und welcher Teil des Jahres gehört in keine Gruppe?

:::loesung
```console
$ sed -E 's/^[0-9]{2}([0-9]{2})-([0-9]{2})-([0-9]{2})/\3.\2.\1/' laeufe.csv | head -n 3
datum,name,km,minuten
02.11.26,Anna,5.0,28
02.11.26,Ben,10.5,62
```

Drei Gruppen: die letzten beiden Ziffern des Jahres, der Monat und der Tag. Die ersten beiden Ziffern des Jahres, `20`, müssen zum Treffer gehören, damit sie mit ersetzt werden und verschwinden, stehen aber in keiner Gruppe, weil sie im Ergebnis nicht vorkommen. Die Kopfzeile bleibt, weil sie nicht mit Ziffern beginnt.
:::
:::

:::aufgabe Aufgabe 24 ★★★ -n und -i zusammen
<span class="anker" id="aufg-24"></span>

Kopiere `laeufe.csv` nach `probe2.csv`. Sage voraus, was nach `sed -n -i 's/Ben/B./p' probe2.csv` in der Datei steht, und prüfe es. Warum ist diese Kombination gefährlich?

:::loesung
```console
$ cp laeufe.csv probe2.csv
$ sed -n -i 's/Ben/B./p' probe2.csv
$ cat probe2.csv
2026-11-02,B.,10.5,62
2026-11-05,B.,5.0,31
2026-11-08,B.,21.1,128
```

In der Datei stehen nur noch die drei geänderten Zeilen; die übrigen sieben sind verloren. `-n` schaltet die gewöhnliche Ausgabe ab, nur `p` schreibt, und das nur bei Zeilen, in denen `s` etwas ersetzt hat. Ohne `-i` wäre das eine bequeme Art, nur die geänderten Zeilen anzusehen. Mit `-i` landet genau diese Ausgabe in der Datei, und alle anderen Zeilen sind weg. Das Handbuch von GNU `sed` warnt ausdrücklich vor dieser Kombination; sie ist ein Grund, `-i` erst hinzuzufügen, wenn der Befehl ohne `-i` das Gewünschte ausgibt.
:::
:::

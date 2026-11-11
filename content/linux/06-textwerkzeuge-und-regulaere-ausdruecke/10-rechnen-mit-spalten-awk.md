---
title: Rechnen mit Spalten: awk
pfad: Informatik / Linux und Kommandozeile / Textwerkzeuge und reguläre Ausdrücke
adresse: informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke
knoten: Kapitel 6: Textwerkzeuge und reguläre Ausdrücke
order: 6111000
summary: Wie viele Kilometer kamen zusammen, wie weit lief jede Person im Mittel, wie schnell war jeder Lauf?
tags: awk, Regeln, assoziatives Array
lang: de
---

<span class="anker" id="stufe-9"></span>

:::zweck
Wie viele Kilometer kamen zusammen, wie weit lief jede Person im Mittel, wie schnell war jeder Lauf? Dafür muss man mit Feldern rechnen, auch mit Kommazahlen, und Werte nach Personen getrennt sammeln. Dieser Abschnitt zeigt ein Werkzeug, das genau dafür gebaut ist: eine kleine Sprache für Spalten und Summen.
:::

### Das Programm awk: Bedingung und Aktion

<span class="anker" id="stufe-9-1"></span>

`grep` wählt Zeilen aus, `cut` Felder, `sed` formt um. Gerechnet hat bisher nur die Shell, und nur mit ganzen Zahlen. Ein Werkzeug, das Zeilen auswählt, Felder kennt und rechnet, verbindet alle drei Aufgaben. Abbildung [30](#abb-30) zeigt, wie es ein Programm aus Regeln auf eine Datei anwendet.

:::abbildung linux/k6regeln 30
Links ein awk-Programm aus zwei Regeln, `/Clara/ {print "Clara ist gelaufen"}` und `{print "Zeile gelesen"}`. Rechts kommen die Zeilen nacheinander an. Für jede Zeile werden beide Regeln von oben geprüft: Passt die Bedingung, leuchtet die Regel auf und ihre Aktion schreibt eine Zeile in die Ausgabe; die zweite Regel ohne Bedingung leuchtet bei jeder Zeile.
:::

:::definition Definition 9.1 (awk, Regel)
<span class="anker" id="satz-9-1"></span>

Der Befehl __awk__ führt ein kleines Programm aus, das in seinem ersten Argument nach den Optionen steht. Das Programm besteht aus __Regeln__ der Form `bedingung {aktion}`. `awk` liest seine Eingabe Zeile für Zeile und prüft für jede Zeile jede Regel der Reihe nach: Ist die Bedingung erfüllt, führt es die Aktion aus. Fehlt die Bedingung, gilt die Regel für jede Zeile; fehlt die Aktion, schreibt `awk` die Zeile aus.
:::

Eine einfache Bedingung ist ein regulärer Ausdruck in Schrägstrichen; sie ist erfüllt, wenn die Zeile einen Treffer enthält. `awk` benutzt dabei die erweiterte Form. Die Aktion `print` schreibt etwas aus, Text in doppelten Anführungszeichen. Das ganze Programm steht in einfachen Anführungszeichen, damit die Shell nichts daran verändert.

::::beispiel Nur Bedingung, Bedingung und Aktion
```console
$ awk '/Clara/' laeufe.csv
2026-11-03,Clara,7.2,41
2026-11-07,Clara,8.0,44
$ awk '/Clara/ {print "Clara ist gelaufen"}' laeufe.csv
Clara ist gelaufen
Clara ist gelaufen
```

Ohne Aktion arbeitet `awk` wie `grep`. Mit Aktion schreibt es für jede passende Zeile den festen Text.
::::

⁠**Kurz gesagt:** Ein awk-Programm besteht aus Regeln `bedingung {aktion}`, die `awk` auf jede Zeile anwendet.

:::hintergrund Woher der Name kommt
`awk` entstand 1977 bei den Bell Labs, wo auch Unix entwickelt wurde. Der Name besteht aus den Anfangsbuchstaben der Nachnamen seiner drei Entwickler, Alfred Aho, Peter Weinberger und Brian Kernighan. Die Idee „erst Zeilen wählen, dann etwas mit ihnen tun“ teilt es mit den Zeilenadressen von `sed`; anders als `sed` hat es Variablen, Rechnungen und Felder von Anfang an eingebaut. Es gibt mehrere Fassungen derselben Sprache. Auf dem Testsystem ist `awk` die GNU-Fassung gawk; manche Systeme bringen stattdessen die schlankere Fassung mawk mit. Alle Beispiele dieses Kapitels liefern mit beiden dasselbe.
:::

### Felder: `$1`, `$0`, `NF` und `-F`

<span class="anker" id="stufe-9-2"></span>

Was `awk` von `grep` und `sed` unterscheidet: Es zerlegt jede Zeile von selbst in Felder, ohne dass man es darum bitten muss. Abbildung [31](#abb-31) zeigt, wie man diese Felder anspricht.

:::abbildung linux/k6awkfelder 31
Die Zeile `2026-11-08,Ben,21.1,128` mit `-F,`. Über den vier Feldern erscheinen ihre Namen `$1`, `$2`, `$3`, `$4`; ein Bogen über der ganzen Zeile trägt `$0`. Rechts steht `NF = 4`, und `$NF` zeigt auf dasselbe Feld wie `$4`. Links steht die Zeilennummer `NR = 9`.
:::

:::definition Definition 9.2 (Felder in awk)
<span class="anker" id="satz-9-2"></span>

`awk` zerlegt jede Zeile in Felder. `$1`, `$2` und so weiter sind die Felder von links, `$0` ist die ganze Zeile, und `NF` enthält die Zahl der Felder, `$NF` ist also das letzte Feld. Ohne Option trennt `awk` an Folgen von Leerzeichen und Tabulatoren und übergeht sie am Anfang und am Ende der Zeile. Mit `-F` und einem Zeichen trennt es an genau diesem Zeichen.
:::

In `awk` bedeutet das Dollarzeichen „Feld Nummer“, nicht wie in der Shell „Wert der Variablen“. Gerade deshalb muss das Programm in einfachen Anführungszeichen stehen: Zwischen doppelten setzte die Shell für `$1` ihren eigenen, meist leeren Wert ein ([Kapitel 5, Abschnitt 3.5](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/worttrennung-und-quoting.html#stufe-3-5)). `print` mit mehreren Werten durch Kommas getrennt schreibt sie mit einem Leerzeichen dazwischen.

::::beispiel Namen und Strecken, Leerzeichen, Feldzahl
```console
$ awk -F, '{print $2, $3}' laeufe.csv | head -n 3
name km
Anna 5.0
Ben 10.5
$ echo '  Anna   lief  5 km' | awk '{print NF, $1, $NF}'
4 Anna km
```

Ohne `-F` zerlegt `awk` den Satz an den Leerzeichen, egal wie viele es sind, in vier Felder. Dass jede Zeile des Lauftagebuchs genau vier Felder hat, prüft man so:

```console
$ awk -F, '{print NF}' laeufe.csv | sort -u
4
```
::::

⁠**Kurz gesagt:** `$1` bis `$NF` sind die Felder einer Zeile, `$0` die ganze Zeile, `NF` ihre Zahl; `-F,` trennt an Kommas.

### Zeilennummer und Bedingungen: NR

<span class="anker" id="stufe-9-3"></span>

Ein regulärer Ausdruck als Bedingung prüft die ganze Zeile. Für Fragen wie „Läufe über 10 km“ braucht man Bedingungen an ein einzelnes Feld und an die Position der Zeile in der Datei.

:::definition Definition 9.3 (NR, Bedingungen)
<span class="anker" id="satz-9-3"></span>

`NR` enthält die Nummer der Zeile, die `awk` gerade bearbeitet, von 1 an gezählt. Als Bedingung dienen Vergleiche mit `==`, `!=`, `<`, `<=`, `>` und `>=`, die man mit `&&` für „und“, `||` für „oder“ und `!` für „nicht“ verbindet. `feld ~ /ausdruck/` ist erfüllt, wenn das Feld einen Treffer für den regulären Ausdruck enthält. Ein Feld, das wie eine Zahl aussieht, vergleicht `awk` mit einer Zahl nach dem Wert, sonst als Text.
:::

`NR > 1` lässt so die Kopfzeile aus. Text in einem Vergleich steht in doppelten Anführungszeichen, `$2 == "Anna"`.

::::beispiel Lange Läufe, Namen mit A oder B
```console
$ awk -F, 'NR > 1 && $3 > 10' laeufe.csv
2026-11-02,Ben,10.5,62
2026-11-06,Anna,12.0,70
2026-11-08,Ben,21.1,128
$ awk -F, '$2 ~ /^[AB]/ {print NR, $2}' laeufe.csv | head -n 3
2 Anna
3 Ben
5 Anna
```

Drei Läufe über 10 km. Im zweiten Programm passt Feld 2 auf „beginnt mit A oder B“, und `awk` schreibt Zeilennummer und Namen.
::::

::::beispiel [Gegenbeispiel] Die Kopfzeile schlüpft durch
```console
$ awk -F, '$3 > 10' laeufe.csv
datum,name,km,minuten
2026-11-02,Ben,10.5,62
2026-11-06,Anna,12.0,70
2026-11-08,Ben,21.1,128
```

Ohne `NR > 1` erscheint die Kopfzeile. Ihr Feld 3 ist `km`, keine Zahl; `awk` vergleicht deshalb als Text, `km` mit `10`, und weil k in der Zeichenordnung hinter 1 steht, ist `km` „größer“.
::::

⁠**Kurz gesagt:** `NR` ist die Zeilennummer; Bedingungen vergleichen Felder mit Zahlen oder Text und verbinden sich mit `&&`, `||` und `!`.

### Variablen, Summen und END

<span class="anker" id="stufe-9-4"></span>

Für eine Summe muss `awk` sich von Zeile zu Zeile etwas merken und am Ende, wenn alle Zeilen gelesen sind, das Ergebnis ausgeben. Rechnen kann es dabei auch mit Kommazahlen:

```console
$ awk -F, 'NR > 1 {print $1, $2, $4 / $3}' laeufe.csv | head -n 3
2026-11-02 Anna 5.6
2026-11-02 Ben 5.90476
2026-11-03 Clara 5.69444
```

Minuten geteilt durch Kilometer ergibt das Tempo, Minuten je Kilometer: Anna brauchte am 2. November 5,6 Minuten für jeden Kilometer.

:::definition Definition 9.4 (Variable in awk, BEGIN, END)
<span class="anker" id="satz-9-4"></span>

Eine Variable in `awk` ist ein Name aus Buchstaben, Ziffern und Unterstrichen, ohne `$` davor. Vor ihrer ersten Zuweisung hat sie den Wert 0 oder den leeren Text, je nachdem, wie man sie benutzt. `s += $3` zählt Feld 3 zu `s` hinzu, `n++` erhöht `n` um 1. Eine Regel mit der Bedingung `END` wird einmal ausgeführt, nachdem die letzte Zeile gelesen ist, eine mit `BEGIN` einmal, bevor die erste gelesen wird.
:::

Mehrere Anweisungen in einer Aktion trennt ein Semikolon. Für eine schöne Ausgabe gibt es `printf` mit einer Vorlage wie das `printf` der Shell aus [Kapitel 5, Abschnitt 3.1](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/worttrennung-und-quoting.html#stufe-3-1): `%d` steht für eine ganze Zahl, `%.2f` für eine Kommazahl mit zwei Stellen nach dem Punkt, und das Zeilenende schreibt man selbst als `\n`.

::::beispiel Gesamtstrecke und Mittelwerte
```console
$ awk -F, 'NR > 1 {s += $3; n++} END {print s, n, s / n}' laeufe.csv
80.2 9 8.91111
$ awk -F, '$2 == "Anna" {s += $3; n++} END {printf "Anna: %.2f km im Mittel aus %d Läufen\n", s / n, n}' laeufe.csv
Anna: 7.10 km im Mittel aus 4 Läufen
```

Zusammen liefen die drei 80,2 km in neun Läufen, im Mittel 8,91 km. Für Anna zählt `awk` nur die Zeilen, deren Feld 2 genau `Anna` ist; die Kopfzeile ist dabei von selbst ausgeschlossen. Abbildung [32](#abb-32) rechnet ihren Mittelwert nach.

:::abbildung linux/k6mittel 32
Annas mittlere Strecke: $(5{,}0 + 6{,}4 + 12{,}0 + 5{,}0) / 4$. Zuerst wächst die Summe Schritt für Schritt, 5,0, 11,4, 23,4, 28,4; dann wird durch die Zahl der Läufe geteilt: $28{,}4 / 4 = 7{,}1$.
:::
::::

::::beispiel [Zweites Beispiel] Eine Überschrift mit BEGIN
```console
$ awk -F, 'BEGIN {print "Name km"} NR > 1 {print $2, $3}' laeufe.csv | head -n 3
Name km
Anna 5.0
Ben 10.5
```
::::

⁠**Kurz gesagt:** awk-Variablen sammeln Werte über alle Zeilen, beginnen bei 0; `END` gibt das Ergebnis nach der letzten Zeile aus, `printf` formatiert es.

### Werte nach Namen sammeln: assoziative Arrays

<span class="anker" id="stufe-9-5"></span>

Für jede Person einzeln die Mittelwerte zu bilden, hieße, das Programm für Anna, Ben und Clara je einmal laufen zu lassen. Bei hundert Personen geht das nicht mehr. Man braucht eine Variable, die viele Werte unter verschiedenen Namen aufnimmt. Abbildung [33](#abb-33) zeigt, wie sie sich beim Lesen füllt.

:::abbildung linux/k6array 33
Links laufen die Datensätze nacheinander ein. Rechts eine Tabelle mit den Spalten Schlüssel, `s` und `n`. Beim ersten Lauf von Anna entsteht die Zeile Anna mit 5,0 und 1, bei Ben die Zeile Ben, bei Clara die Zeile Clara; jeder weitere Lauf erhöht die Werte in der Zeile seines Namens. Am Ende stehen Anna 28,4 und 4, Ben 36,6 und 3, Clara 15,2 und 2.
:::

:::definition Definition 9.5 (Assoziatives Array)
<span class="anker" id="satz-9-5"></span>

Ein __assoziatives Array__ ist eine Variable in `awk`, die beliebig viele Werte speichert, jeden unter einem eigenen Schlüssel: `s["Anna"]` ist der Wert unter dem Schlüssel `Anna`. Der Schlüssel darf jeder Text sein, auch ein Feld wie `$2`; ein neuer Schlüssel entsteht bei der ersten Benutzung, mit dem Wert 0 oder dem leeren Text wie jede neue Variable. `for (k in s)` führt eine Anweisung für jeden vorhandenen Schlüssel aus, in einer Reihenfolge, die `awk` selbst bestimmt.
:::

Weil die Reihenfolge nicht festliegt, hängt man meist ein `sort` an.

::::beispiel Läufe und Mittelwerte je Person
```console
$ awk -F, 'NR > 1 {n[$2]++} END {for (p in n) print n[p], p}' laeufe.csv | sort -rn
4 Anna
3 Ben
2 Clara
$ awk -F, 'NR > 1 {s[$2] += $3; n[$2]++} END {for (p in s) printf "%s %.2f %d\n", p, s[p] / n[p], n[p]}' laeufe.csv | sort
Anna 7.10 4
Ben 12.20 3
Clara 7.60 2
```

Das erste Programm zählt die Läufe je Person, dasselbe Ergebnis wie die Häufigkeitstabelle aus Unterabschnitt [3.6](sortieren-und-zahlen-sort-und-uniq.html#stufe-3-6). Das zweite sammelt je Person die Strecken in `s` und die Zahl der Läufe in `n` und teilt am Ende: Ben lief im Mittel 12,2 km.
::::

⁠**Kurz gesagt:** Ein assoziatives Array speichert Werte unter Schlüsseln wie `$2`; so sammelt `awk` in einem Durchgang Summen und Zähler je Gruppe.

:::hintergrund awk oder sort und uniq?
Beide Wege zählen die Läufe je Person. `sort | uniq -c` muss erst alle Zeilen ordnen, damit gleiche Namen nebeneinanderstehen; `sort` hält dafür alle Zeilen fest oder lagert sie aus. `awk` liest jede Zeile genau einmal und merkt sich je Schlüssel nur einen Zähler; sein Speicher wächst mit der Zahl der verschiedenen Namen, nicht mit der Zahl der Zeilen. Dafür kennt ein assoziatives Array keine Ordnung: Intern verteilt `awk` die Schlüssel so, dass es jeden schnell wiederfindet, und `for (k in s)` geht sie in dieser inneren Anordnung durch. Das Handbuch von gawk sagt ausdrücklich, dass man sich auf diese Reihenfolge nicht verlassen kann. Für eine geordnete Ausgabe sorgt deshalb ein `sort` dahinter, und zwar nur noch über eine Zeile je Person.
:::

### Aufgaben zu Abschnitt [9](#stufe-9)

<span class="anker" id="stufe-9-6"></span>

:::aufgabe Aufgabe 25 ★ Felder ausgeben
<span class="anker" id="aufg-25"></span>

(a) Gib für alle Läufe über 40 Minuten Name und Datum aus, in dieser Reihenfolge. (b) Prüfe, dass jede Zeile von `/etc/passwd` gleich viele durch Doppelpunkte getrennte Felder hat. (c) Das letzte Feld jeder Zeile von `/etc/passwd` ist die Shell des Benutzers. Erstelle eine Häufigkeitstabelle dieser Shells.

:::loesung
```console
$ awk -F, 'NR > 1 && $4 > 40 {print $2, $1}' laeufe.csv
Ben 2026-11-02
Clara 2026-11-03
Anna 2026-11-06
Clara 2026-11-07
Ben 2026-11-08
$ awk -F: '{print NF}' /etc/passwd | sort -u
7
$ awk -F: '{print $NF}' /etc/passwd | sort | uniq -c | sort -rn
     24 /usr/sbin/nologin
      2 /bin/bash
      1 /bin/sync
      1 /bin/false
```

(a) Anders als `cut` schreibt `awk` die Felder in jeder gewünschten Reihenfolge. (b) Jede Zeile hat sieben Felder; `sort -u` lässt nur einen Wert übrig. (c) `$NF` ist das letzte Feld. Auf dem Testsystem haben 24 der 28 Konten `/usr/sbin/nologin`: Es sind Konten für Dienste, mit denen sich niemand anmelden soll. Nur zwei haben eine Shell zum Arbeiten, root und student; `/bin/sync` und `/bin/false` sind keine Shells: Das eine erledigt eine einzige Aufgabe und endet, das andere endet sofort. Auf deinem System können die Zahlen anders sein.
:::
:::

:::aufgabe Aufgabe 26 ★★★ Mittelwerte je Person
<span class="anker" id="aufg-26"></span>

(a) Berechne für jede Person die mittlere Dauer eines Laufs in Minuten, mit einer Nachkommastelle. (b) Gib für jede Person ihren längsten Lauf in Kilometern aus. Tipp: Ein Vergleich mit einem noch nicht benutzten Arrayeintrag vergleicht mit 0.

:::loesung
```console
$ awk -F, 'NR > 1 {m[$2] += $4; n[$2]++} END {for (p in m) printf "%s %.1f\n", p, m[p] / n[p]}' laeufe.csv | sort
Anna 40.0
Ben 73.7
Clara 42.5
$ awk -F, 'NR > 1 && $3 > max[$2] {max[$2] = $3} END {for (p in max) print p, max[p]}' laeufe.csv | sort
Anna 12.0
Ben 21.1
Clara 8.0
```

(a) Wie im Beispiel aus Unterabschnitt [9.5](#stufe-9-5), nur mit Feld 4: Anna $160 / 4 = 40{,}0$, Ben $221 / 3 \approx 73{,}7$, Clara $85 / 2 = 42{,}5$ Minuten. (b) Die Bedingung prüft, ob die Strecke größer ist als das bisherige Maximum der Person; beim ersten Lauf einer Person gibt es noch keinen Eintrag, und der Vergleich findet 0. Dann wird das Maximum ersetzt. Am Ende steht für jede Person ihr längster Lauf da. `awk` schreibt die Werte so, wie sie im Feld standen, deshalb `12.0` und nicht `12`.
:::
:::

:::aufgabe Aufgabe 27 ★★ Zahl oder Text
<span class="anker" id="aufg-27"></span>

Sage voraus, wie viele Zeilen die drei Befehle ausgeben, und prüfe es: (a) `awk -F, '$4 > 100' laeufe.csv`, (b) `awk -F, 'NR > 1 && $4 > 100' laeufe.csv`, (c) `awk -F, '$2 > "B"' laeufe.csv`. Erkläre bei jedem, ob `awk` als Zahl oder als Text vergleicht.

:::loesung
```console
$ awk -F, '$4 > 100' laeufe.csv
datum,name,km,minuten
2026-11-08,Ben,21.1,128
$ awk -F, 'NR > 1 && $4 > 100' laeufe.csv
2026-11-08,Ben,21.1,128
$ awk -F, '$2 > "B"' laeufe.csv | wc -l
6
```

(a) Zwei Zeilen. In der Kopfzeile ist Feld 4 `minuten`, keine Zahl, also vergleicht `awk` als Text: m steht in der Zeichenordnung hinter 1, `minuten` ist „größer“ als `100`. In den übrigen Zeilen ist Feld 4 eine Zahl, und nur 128 ist größer als 100. (b) Eine Zeile; `NR > 1` schließt die Kopfzeile aus. (c) Sechs Zeilen. Der Vergleich mit einem Text in Anführungszeichen ist immer ein Textvergleich. `Ben` ist größer als `B`, weil `B` sein Anfang ist; `Clara` beginnt mit C, das hinter B steht; `name` beginnt mit einem Kleinbuchstaben, und die stehen hinter allen Großbuchstaben. `Anna` ist kleiner. Also drei Läufe von Ben, zwei von Clara und die Kopfzeile.
:::
:::

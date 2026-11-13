---
title: Schleifen: `for` und `while`
pfad: Informatik / Linux und Kommandozeile / Shell-Skripte
adresse: informatik/linux-und-kommandozeile/shell-skripte
knoten: Kapitel 10: Shell-Skripte
order: 6150600
summary: Skripte lohnen sich vor allem, wenn dieselbe Arbeit für viele Dinge zu tun ist: für jede Datei, jede Zeile, jede Runde.
tags: for-Schleife, Durchgang, while-Schleife, break, continue
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Skripte lohnen sich vor allem, wenn dieselbe Arbeit für viele Dinge zu tun ist: für jede Datei, jede Zeile, jede Runde. Dieser Abschnitt zeigt die Schleifen der Shell: über eine Liste von Wörtern, über Dateien, über Zahlen und so lange, wie ein Befehl Erfolg meldet.
:::

### Die `for`-Schleife

<span class="anker" id="stufe-5-1"></span>

Dieselben Befehle für jedes Element einer Liste: für jeden Trainingstag eine Erinnerung, für jede Datei eine Zählung. Man schreibt die Befehle einmal und lässt sie für jedes Element wiederholen.

Ein Bild zur Orientierung: Ein Stapel Karteikarten wird Karte für Karte umgedreht. Jedes Mal steht etwas anderes oben, und mit der Karte, die gerade oben liegt, wird dasselbe getan.

:::definition Definition 5.1 (`for`-Schleife)
<span class="anker" id="satz-5-1"></span>

Die __`for`-Schleife__ `for name in wörter; do befehle; done` setzt die Variable `name` nacheinander auf jedes Wort der Liste und führt jedes Mal die Befehle zwischen `do` und `done` aus. Jede einzelne Ausführung dieser Befehle heißt ein __Durchgang__. Die Wortliste durchläuft vorher die übliche Expansion ([Kapitel 5, Abschnitt 3.9](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/worttrennung-und-quoting.html#stufe-3-9)).
:::

```console
$ for tag in Montag Mittwoch Freitag; do echo "Training am $tag"; done
Training am Montag
Training am Mittwoch
Training am Freitag
```

Über mehrere Zeilen getippt, wie in einem Skript:

```console
$ for tag in Montag Mittwoch Freitag
> do
>     echo "Training am $tag"
> done
Training am Montag
Training am Mittwoch
Training am Freitag
```

Lässt man `in wörter` weg, also `for datei; do`, läuft die Schleife über die Positionsparameter, genau wie `for datei in "$@"; do`. Die Variable behält nach der Schleife den letzten Wert. Abbildung [19](#abb-19) zeigt die Durchgänge.

:::abbildung linux/k10for 19
Drei Karteikarten `Montag`, `Mittwoch`, `Freitag` liegen auf einem Stapel. Bei jedem Durchgang wird die oberste Karte in die Schublade `tag` gelegt, der Schleifenkörper `echo "Training am $tag"` leuchtet auf und rechts erscheint eine Ausgabezeile. Nach dem dritten Durchgang ist der Stapel leer, die Schleife endet bei `done`; in der Schublade liegt noch `Freitag`.
:::

⁠**Kurz gesagt:** `for` setzt eine Variable nacheinander auf jedes Wort einer Liste und führt dabei jedes Mal dieselben Befehle aus.

### Schleifen über Dateien

<span class="anker" id="stufe-5-2"></span>

Der häufigste Fall: dieselbe Arbeit für alle Dateien, die zu einem Muster passen. Lege dafür drei leere Fotodateien an, zwei davon mit Leerzeichen im Namen:

```console
$ touch "fotos/strand 1.jpg" "fotos/strand 2.jpg" fotos/berg.png
$ for foto in fotos/*.jpg; do echo "Foto: $foto"; done
Foto: fotos/strand 1.jpg
Foto: fotos/strand 2.jpg
```

:::satz Satz 5.2 (Schleifen über Dateinamen)
<span class="anker" id="satz-5-2"></span>

Steht in der Wortliste von `for` ein Muster, ersetzt die Pfadnamen-Erweiterung es durch die passenden Namen, und jeder Name wird ein eigenes Wort, auch wenn er Leerzeichen enthält. Die Liste wird dabei nicht mehr an Leerzeichen zerlegt. Passt kein Name, bleibt das Muster als Text stehen ([Kapitel 5, Abschnitt 1.5](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/expansion-muster-klammern-und-tilde.html#stufe-1-5)), und die Schleife läuft einmal mit dem Muster selbst.
:::

Der Satz erklärt beide Beobachtungen der folgenden Zeilen. Wer die Liste mit `$(ls fotos)` baut, bekommt die Namen als einen Text, den die Shell an Leerzeichen zerlegt ([Kapitel 5, Abschnitt 3.2](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/worttrennung-und-quoting.html#stufe-3-2)), und zwei Namen zerbrechen in vier Wörter. Und ohne Treffer läuft die Schleife einmal mit dem Muster:

```console
$ for foto in $(ls fotos); do echo "Foto: $foto"; done
Foto: berg.png
Foto: strand
Foto: 1.jpg
Foto: strand
Foto: 2.jpg
```

```console
$ for doku in fotos/*.pdf; do echo "Dokument: $doku"; done
Dokument: fotos/*.pdf
```

Ein Skript fängt den Fall ohne Treffer ab, indem es im Schleifenkörper mit `[ -e "$datei" ]` prüft, ob es den Namen wirklich gibt. Abbildung [20](#abb-20) stellt die beiden Wege zur Namensliste nebeneinander.

:::abbildung linux/k10lsfalle 20
Links das Muster `fotos/*.jpg`: Die Pfadnamen-Erweiterung legt zwei ganze Kärtchen `fotos/strand 1.jpg` und `fotos/strand 2.jpg` in die Schleife, zwei Durchgänge. Rechts `$(ls fotos)`: `ls` liefert einen Textstreifen `berg.png strand 1.jpg strand 2.jpg` mit Zeilenenden; die Schere „Worttrennung“ schneidet an jedem Leerzeichen und Zeilenende, fünf Schnipsel fallen in die Schleife, vier davon (`strand`, `1.jpg`, `strand`, `2.jpg`) rot markiert als Bruchstücke von Namen.
:::

::::beispiel Jede Datei einzeln zählen
Die zweite Fassung von `zaehle.sh` durchläuft `"$@"` und prüft jeden Namen, bevor sie ihn zählt. `wc -l < "$datei"` liest die Datei über eine Umleitung und gibt deshalb nur die Zahl aus, ohne Namen ([Kapitel 4, Abschnitt 3.1](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/eingaben-umleiten.html#stufe-3-1)):

```bash zaehle.sh
#!/bin/bash
# zaehle.sh: zählt die Zeilen jeder angegebenen Datei
for datei in "$@"; do
    if [ -f "$datei" ]; then
        zeilen=$(wc -l < "$datei")
        echo "$datei: $zeilen Zeilen"
    else
        echo "$datei: keine Datei"
    fi
done
```

```console
$ ./zaehle.sh einkauf.txt "mein einkauf.txt" fotos gibtsnicht.txt
einkauf.txt: 4 Zeilen
mein einkauf.txt: 3 Zeilen
fotos: keine Datei
gibtsnicht.txt: keine Datei
```
::::

⁠**Kurz gesagt:** `for datei in muster` und `for datei in "$@"` liefern ganze Namen; `for datei in $(ls)` zerlegt sie an Leerzeichen.

### Die `for`-Schleife mit Zähler

<span class="anker" id="stufe-5-3"></span>

Manchmal will man nicht über Wörter laufen, sondern zählen: Runde 1 bis $n$, wobei $n$ erst beim Aufruf feststeht. Die Klammererweiterung hilft dabei nicht, denn sie geschieht vor dem Einsetzen der Variablen ([Kapitel 5, Abschnitt 3.9](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/worttrennung-und-quoting.html#stufe-3-9)):

```console
$ for (( i = 1; i <= 3; i++ )); do echo "Runde $i"; done
Runde 1
Runde 2
Runde 3
$ n=4
$ echo {1..$n}
{1..4}
$ for (( i = 1; i <= n; i++ )); do printf '%s ' "$i"; done; echo
1 2 3 4
```

:::definition Definition 5.3 (`for`-Schleife mit Zähler)
<span class="anker" id="satz-5-3"></span>

Die Schleife `for (( start; bedingung; schritt ))` mit `do befehle; done` dahinter führt zuerst den arithmetischen Ausdruck `start` aus. Dann prüft die Schleife `bedingung` wie `(( ))`: Ist ihr Wert nicht 0, führt sie die Befehle aus, danach `schritt`, und prüft erneut. Ist ihr Wert 0, endet die Schleife.
:::

`i++` erhöht `i` um eins. Diese Form stammt aus der Programmiersprache C und heißt deshalb auch „C-Stil“. Das letzte `echo` in der Zeile oben beendet nur die Ausgabezeile, weil `printf '%s '` kein Zeilenende schreibt. Abbildung [21](#abb-21) zeigt die drei Teile im Kreislauf.

:::abbildung linux/k10forc 21
Die Zeile `for (( i = 1; i <= 3; i++ ))` in drei farbige Teile zerlegt: „einmal am Anfang“ `i = 1`, „vor jedem Durchgang“ `i <= 3`, „nach jedem Durchgang“ `i++`. Darunter ein Kreislauf: Start setzt `i` auf 1, die Prüfung leuchtet grün, der Körper gibt `Runde 1` aus, `i++` macht 2 daraus, und so weiter, bis bei `i = 4` die Prüfung rot wird und der Pfeil aus dem Kreislauf hinausführt.
:::

⁠**Kurz gesagt:** `for (( i = 1; i <= n; i++ ))` zählt mit einer Variablen von einem Startwert bis zu einer Grenze, die auch aus einer Variablen kommen darf.

### Die `while`-Schleife

<span class="anker" id="stufe-5-4"></span>

Oft weiß man vorher nicht, wie viele Durchgänge nötig sind: Man spart jeden Monat einen festen Betrag, bis ein Ziel erreicht ist. Die Schleife soll laufen, solange eine Bedingung gilt.

:::definition Definition 5.4 (`while` und `until`)
<span class="anker" id="satz-5-4"></span>

Die __`while`-Schleife__ `while befehle; do befehle; done` führt die Befehle hinter `while` aus und, wenn der letzte davon den Exit-Status 0 hat, die Befehle zwischen `do` und `done`; dann beginnt sie von vorn. Sie endet, sobald die Bedingung einen anderen Status liefert. `until` arbeitet genauso, läuft aber, solange die Bedingung *nicht* 0 liefert.
:::

Wie `if` prüft `while` einen Exit-Status; jede Prüfung aus den Abschnitten [3](verzweigen-if-und-test.html#stufe-3) und [4](bequemer-prufen-und-case.html#stufe-4) kann die Bedingung sein.

```bash sparen.sh
#!/bin/bash
# sparen.sh: Wie viele Monate dauert es bis zum Sparziel?
#   Aufruf: sparen.sh ZIEL RATE   (beides in ganzen Euro)
ziel=$1
rate=$2
stand=0
monate=0
while (( stand < ziel )); do
    stand=$(( stand + rate ))
    monate=$(( monate + 1 ))
done
echo "Nach $monate Monaten sind $stand Euro gespart."
```

```console
$ chmod +x sparen.sh
$ ./sparen.sh 1000 75
Nach 14 Monaten sind 1050 Euro gespart.
$ ./sparen.sh 500 100
Nach 5 Monaten sind 500 Euro gespart.
```

Nach 13 Monaten sind es $13\cdot75=975$ Euro, noch weniger als 1000; erst der vierzehnte Monat erreicht das Ziel. Abbildung [22](#abb-22) verfolgt die Durchgänge. `until` ist manchmal natürlicher zu lesen, etwa beim Herunterzählen:

```console
$ i=3
$ until (( i == 0 )); do echo "$i ..."; i=$(( i - 1 )); done; echo "Los!"
3 ...
2 ...
1 ...
Los!
```

:::abbildung linux/k10while 22
Ein Sparschwein und ein Zielstrich bei 1000 Euro. Bei jedem Durchgang prüft ein Schild `stand < ziel?`, leuchtet grün, eine Münze `+75` fällt ins Schwein, die Zähler `stand` und `monate` springen weiter (75/1, 150/2, …, 975/13, 1050/14); die mittleren Durchgänge laufen schnell durch. Bei 1050 leuchtet das Schild rot, die Schleife endet, unten erscheint `Nach 14 Monaten sind 1050 Euro gespart.`
:::

:::warnung Schleifen, die nie enden
Ändert der Schleifenkörper nichts, wovon die Bedingung abhängt, läuft eine `while`-Schleife ewig, etwa `sparen.sh` mit der Rate 0. Ein laufendes Skript brichst du mit Strg+C ab ([Kapitel 8, Abschnitt 4.4](/wissen/informatik/linux-und-kommandozeile/prozesse-signale-und-dienste/signale.html#stufe-4-4)). Prüfe in eigenen Skripten vor der Schleife, ob die Werte das Ende überhaupt erlauben.
:::

⁠**Kurz gesagt:** `while` wiederholt, solange eine Bedingung den Status 0 liefert; `until`, solange sie es nicht tut.

### Schleifen steuern: `break` und `continue`

<span class="anker" id="stufe-5-5"></span>

Manchmal ist eine Schleife fertig, bevor die Liste zu Ende ist: Man sucht die erste Datei, in der ein Wort vorkommt, und braucht danach nicht weiterzusuchen. Und manchmal soll nur ein einzelner Durchgang übersprungen werden.

:::definition Definition 5.5 (`break` und `continue`)
<span class="anker" id="satz-5-5"></span>

Der eingebaute Befehl __`break`__ beendet die Schleife sofort; es geht hinter ihrem `done` weiter. __`continue`__ beendet nur den laufenden Durchgang und springt zum nächsten. In verschachtelten Schleifen wirken beide auf die innerste.
:::

```console
$ for datei in *.txt; do if grep -q Kaffee "$datei"; then echo "Kaffee steht in $datei"; break; fi; done
Kaffee steht in einkauf.txt
```

```console
$ for name in *; do if [ -d "$name" ]; then continue; fi; echo "Datei: $name"; done
Datei: alle.sh
Datei: art.sh
Datei: bewertung.sh
Datei: dateiinfo.sh
Datei: einkauf.txt
Datei: leer.txt
Datei: mein einkauf.txt
Datei: schiebe.sh
Datei: sparen.sh
Datei: ueberblick.sh
Datei: wechsle.sh
Datei: wer.sh
Datei: windows.sh
Datei: zaehle.sh
Datei: zehn.sh
Datei: zeige.sh
```

Die zweite Schleife überspringt die Verzeichnisse `bin` und `fotos`. Abbildung [23](#abb-23) zeigt beide Sprünge.

:::abbildung linux/k10break 23
Zwei Schleifen als Rundbahnen. Links `break`: Die Dateien `einkauf.txt`, `leer.txt`, `mein einkauf.txt` stehen an der Bahn; bei `einkauf.txt` meldet `grep` einen Treffer, ein Pfeil `break` führt aus der Bahn hinaus hinter `done`; die übrigen Dateien bleiben grau. Rechts `continue`: Bei einer Datei führt die Runde über die Station `echo`; bei `bin` und `fotos` führt eine Abkürzung direkt zum Anfang des nächsten Durchgangs, ohne an `echo` vorbeizukommen.
:::

⁠**Kurz gesagt:** `break` verlässt die Schleife, `continue` überspringt den Rest des laufenden Durchgangs.

:::aufgabe Aufgabe 16 ★ Ein Countdown
<span class="anker" id="aufg-16"></span>

Schreibe ein Skript `countdown.sh N`, das mit einer `for`-Schleife mit Zähler von `N` bis 1 herunterzählt und zum Schluss `Start!` ausgibt. Teste es mit 3.

:::loesung
Die Schleife beginnt bei `n` und zählt mit `i--` abwärts, solange `i` mindestens 1 ist:

```bash countdown.sh
#!/bin/bash
# countdown.sh: zählt von N bis 1 herunter
n=$1
for (( i = n; i >= 1; i-- )); do
    echo "$i"
done
echo "Start!"
```

```console
$ chmod +x countdown.sh
$ ./countdown.sh 3
3
2
1
Start!
```
:::
:::

:::aufgabe Aufgabe 17 ★★ Sicherungskopien mit Probelauf
<span class="anker" id="aufg-17"></span>

Schreibe eine Schleife, die von jeder Datei mit der Endung `.txt` im Übungsverzeichnis eine Kopie mit der zusätzlichen Endung `.bak` anlegt, aus `einkauf.txt` also `einkauf.txt.bak`. Lass sie zuerst mit `echo` vor dem `cp` laufen, um zu sehen, welche Befehle entstehen, dann echt. Was geschieht beim zweiten Lauf mit den `.bak`-Dateien?

:::loesung
```console
$ for datei in *.txt; do echo cp "$datei" "$datei.bak"; done
cp einkauf.txt einkauf.txt.bak
cp leer.txt leer.txt.bak
cp mein einkauf.txt mein einkauf.txt.bak
$ for datei in *.txt; do cp "$datei" "$datei.bak"; done
$ ls *.bak
 einkauf.txt.bak   leer.txt.bak   'mein einkauf.txt.bak'
$ for datei in *.txt; do cp "$datei" "$datei.bak"; done
$ ls *.bak
 einkauf.txt.bak   leer.txt.bak   'mein einkauf.txt.bak'
```

Der Probelauf zeigt die Befehle, aber `echo` verbindet seine Argumente mit Leerzeichen, so dass man die Grenze zwischen `mein` und `einkauf.txt` nicht sieht. Wer sie sehen will, schreibt `printf '[%s] ' cp "$datei" "$datei.bak"; echo`. Beim zweiten Lauf passen die `.bak`-Dateien nicht auf `*.txt`, denn sie enden auf `.bak`; es entstehen also keine Dateien `.bak.bak`. `cp` überschreibt die vorhandenen Kopien ohne Rückfrage ([Kapitel 3, Abschnitt 6.1](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/kopieren-verschieben-loschen.html#stufe-6-1)).
:::
:::

:::aufgabe Aufgabe 18 ★★ Eine Rate von 0 Euro
<span class="anker" id="aufg-18"></span>

Was geschieht bei `./sparen.sh 1000 0`? Probiere es aus und brich es ab. Ergänze `sparen.sh` vor der Schleife um eine Prüfung, die bei einer Rate von 0 oder weniger eine Meldung ausgibt und das Skript mit `exit 1` beendet ([Kapitel 4, Abschnitt 5.1](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/der-exit-status.html#stufe-5-1)).

:::loesung
Mit der Rate 0 wächst `stand` nie, die Bedingung `stand < ziel` bleibt wahr, und die Schleife läuft endlos. Strg+C bricht sie ab, mit dem Status 130:

```console
$ ./sparen.sh 1000 0
^C
$ echo $?
130
```

Die Prüfung gehört vor die Schleife:

```bash sparen.sh
#!/bin/bash
# sparen.sh: Wie viele Monate dauert es bis zum Sparziel?
#   Aufruf: sparen.sh ZIEL RATE   (beides in ganzen Euro)
ziel=$1
rate=$2
if (( rate <= 0 )); then
    echo "sparen.sh: Die Rate muss größer als 0 sein." >&2
    exit 1
fi
stand=0
monate=0
while (( stand < ziel )); do
    stand=$(( stand + rate ))
    monate=$(( monate + 1 ))
done
echo "Nach $monate Monaten sind $stand Euro gespart."
```

```console
$ ./sparen.sh 1000 0
sparen.sh: Die Rate muss größer als 0 sein.
$ echo $?
1
$ ./sparen.sh 1000 75
Nach 14 Monaten sind 1050 Euro gespart.
```
:::
:::

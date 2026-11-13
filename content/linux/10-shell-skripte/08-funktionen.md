---
title: Funktionen
pfad: Informatik / Linux und Kommandozeile / Shell-Skripte
adresse: informatik/linux-und-kommandozeile/shell-skripte
knoten: Kapitel 10: Shell-Skripte
order: 6150800
summary: Wenn ein Skript dieselbe Arbeit an mehreren Stellen braucht, schreibt man sie einmal und gibt ihr einen Namen.
tags: Funktion, local name=wert, lokale Variable, return n
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Wenn ein Skript dieselbe Arbeit an mehreren Stellen braucht, schreibt man sie einmal und gibt ihr einen Namen. Dieser Abschnitt zeigt, wie man solche Befehle innerhalb eines Skripts anlegt, ihnen Argumente gibt, ihre Variablen abschirmt und ein Ergebnis zurückbekommt.
:::

### Die Funktion

<span class="anker" id="stufe-7-1"></span>

Ein Skript braucht an mehreren Stellen dieselbe Meldung oder dieselbe Prüfung. Kopiert man die Zeilen, muss man jede Änderung an allen Kopien machen. Besser ist ein eigener Befehl innerhalb des Skripts.

Ein Bild zur Orientierung: ein Rezept im Kochbuch, auf das andere Rezepte verweisen: „Teig wie auf Seite 12“. Der Teig wird einmal beschrieben und überall benutzt.

:::definition Definition 7.1 (Funktion)
<span class="anker" id="satz-7-1"></span>

Eine __Funktion__ ist eine Gruppe von Befehlen mit einem Namen. `name() { befehle; }` legt sie an; danach ruft man sie mit `name` auf wie einen Befehl, und die Shell führt die Befehle zwischen den geschweiften Klammern aus. Eine Funktion muss angelegt sein, bevor sie aufgerufen wird.
:::

Die geschweiften Klammern sind Schlüsselwörter: Nach `{` steht ein Leerzeichen oder ein Zeilenende, und der letzte Befehl endet mit einem Semikolon oder einem Zeilenende ([Kapitel 4, Abschnitt 6.1](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/befehle-verketten.html#stufe-6-1)). In der Befehlszeile:

```console
$ gruesse() { echo "Hallo, $USER!"; }
$ gruesse
Hallo, student!
$ type gruesse
gruesse is a function
gruesse ()
{
    echo "Hallo, $USER!"
}
```

`type` kennt nun eine weitere Befehlsart ([Kapitel 2, Abschnitt 3.5](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/arten-von-befehlen.html#stufe-3-5)). Bei der Befehlssuche kommt eine Funktion vor den eingebauten Befehlen und vor dem Suchpfad ([Kapitel 5, Abschnitt 5.3](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/wie-die-shell-programme-findet-path.html#stufe-5-3)). In Skripten stehen Funktionen üblicherweise oben, vor dem Teil, der sie benutzt. Abbildung [29](#abb-29) zeigt, wie die Shell eine Funktion erst anlegt und dann aufruft.

:::abbildung linux/k10funktion 29
Ein Skript als helle Dateiansicht mit drei Teilen: oben die Definition `gruesse() { echo "Hallo, $USER!"; }`, darunter zwei Zeilen `gruesse`. Beim ersten Durchgang liest die Shell die Definition und legt eine Karteikarte „gruesse“ mit dem Inhalt in einem Kasten „bekannte Funktionen“ ab; ausgeführt wird dabei nichts. Bei jeder Zeile `gruesse` springt ein Pfeil zur Karteikarte, der Inhalt läuft ab, links unten erscheint `Hallo, student!`, und ein gestrichelter Pfeil kehrt zur nächsten Zeile zurück.
:::

⁠**Kurz gesagt:** `name() { befehle; }` legt einen eigenen Befehl an, den man danach wie jeden anderen aufruft.

### Die Argumente einer Funktion

<span class="anker" id="stufe-7-2"></span>

Eine Funktion, die immer dasselbe tut, nützt wenig. Wie ein Skript soll sie Argumente bekommen.

:::satz Satz 7.2 (Argumente einer Funktion)
<span class="anker" id="satz-7-2"></span>

Während eine Funktion läuft, enthalten `$1`, `$2`, …, `$#` und `"$@"` die Argumente des Funktionsaufrufs, nicht die des Skripts. Nach dem Ende der Funktion gelten wieder die Positionsparameter des Skripts. `$0` bleibt der Name des Skripts.
:::

```bash gruss.sh
#!/bin/bash
# gruss.sh: Argumente einer Funktion und des Skripts
gruss() {
    echo "In der Funktion: $# Argumente, das erste ist $1, \$0 ist $0"
}

echo "Im Skript: $# Argumente, das erste ist $1"
gruss Anna Ben Clara
echo "Wieder im Skript: das erste ist $1"
```

```console
$ chmod +x gruss.sh
$ ./gruss.sh Milch Brot
Im Skript: 2 Argumente, das erste ist Milch
In der Funktion: 3 Argumente, das erste ist Anna, $0 ist ./gruss.sh
Wieder im Skript: das erste ist Milch
```

`\$0` gibt das Zeichen `$` aus, damit der Text den Namen der Variablen zeigt ([Kapitel 5, Abschnitt 3.5](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/worttrennung-und-quoting.html#stufe-3-5)). Abbildung [30](#abb-30) zeigt, wie die Fächer für die Dauer des Aufrufs ausgetauscht werden.

:::abbildung linux/k10funktionsparameter 30
Die Fächer 1 bis 3 des Skripts mit `Milch`, `Brot` und leer, Zähler `$# = 2`. Beim Aufruf `gruss Anna Ben Clara` schiebt sich ein zweiter Satz Fächer davor: `Anna`, `Ben`, `Clara`, Zähler 3; die Fächer des Skripts verschwinden dahinter. Fach 0 mit `./gruss.sh` bleibt in beiden Sätzen dasselbe. Nach dem Ende der Funktion schiebt sich der vordere Satz weg, die Fächer des Skripts sind wieder sichtbar.
:::

⁠**Kurz gesagt:** In einer Funktion sind `$1`, `$#` und `"$@"` die Argumente des Aufrufs; danach gelten wieder die des Skripts.

### Lokale Variablen: `local`

<span class="anker" id="stufe-7-3"></span>

Eine Funktion braucht oft Hilfsvariablen. Heißen die zufällig so wie Variablen des Skripts, überschreibt die Funktion sie, denn ohne weiteres gibt es in einem Skript nur einen Satz Variablen für alle.

:::definition Definition 7.3 (`local`)
<span class="anker" id="satz-7-3"></span>

Der eingebaute Befehl __`local name=wert`__ legt innerhalb einer Funktion eine __lokale Variable__ an: Sie gilt nur, solange die Funktion läuft, und verdeckt dabei eine gleichnamige Variable des Skripts, ohne sie zu verändern. Ohne `local` ist jede Variable, die eine Funktion setzt, eine Variable des ganzen Skripts.
:::

```bash lokal.sh
#!/bin/bash
# lokal.sh: globale und lokale Variablen
anzahl=10

mit_local() {
    local anzahl=2
    echo "In mit_local: anzahl=$anzahl"
}

ohne_local() {
    anzahl=1
    echo "In ohne_local: anzahl=$anzahl"
}

mit_local
echo "Danach: anzahl=$anzahl"
ohne_local
echo "Danach: anzahl=$anzahl"
```

```console
$ chmod +x lokal.sh
$ ./lokal.sh
In mit_local: anzahl=2
Danach: anzahl=10
In ohne_local: anzahl=1
Danach: anzahl=1
```

Eine Funktion läuft in derselben Shell wie das Skript, nicht in einem Kindprozess; deshalb wirkt `ohne_local` auf die Variable des Skripts. Die Regel für eigene Funktionen: jede Hilfsvariable mit `local` anlegen. Abbildung [31](#abb-31) vergleicht die beiden Funktionen.

:::abbildung linux/k10local 31
Die Schublade `anzahl = 10` des Skripts. Links `mit_local`: Für die Dauer des Aufrufs schiebt sich eine eigene Schublade `anzahl = 2` davor, die Funktion schreibt hinein; danach verschwindet sie, dahinter steht unverändert `10`. Rechts `ohne_local`: keine eigene Schublade, die Funktion greift direkt in die Schublade des Skripts und schreibt `1` hinein; nach dem Aufruf bleibt `1`.
:::

:::hintergrund Wer eine lokale Variable sieht
Eine lokale Variable sieht nicht nur die Funktion, die sie anlegt, sondern auch jede Funktion, die von dort aus aufgerufen wird. Ruft `mit_local` eine zweite Funktion auf, liest diese `anzahl` als 2. Diese Regel heißt dynamische Sichtbarkeit: Welche Variable gemeint ist, hängt davon ab, wer gerade wen aufgerufen hat, nicht davon, wo eine Funktion im Text steht. Viele Programmiersprachen, auch Python, machen es anders: Dort zählt, wo eine Funktion geschrieben ist.
:::

⁠**Kurz gesagt:** `local` gibt einer Funktion eigene Variablen, die nach dem Aufruf verschwinden; ohne `local` schreibt sie in die Variablen des Skripts.

### Ein Ergebnis als Exit-Status: `return`

<span class="anker" id="stufe-7-4"></span>

Eine Prüffunktion wie „ist das eine Zahl?“ soll man in `if` benutzen können wie `grep -q`. Dafür muss sie mit einem Exit-Status enden.

:::definition Definition 7.4 (`return`)
<span class="anker" id="satz-7-4"></span>

Eine Funktion endet mit dem Exit-Status ihres letzten Befehls. Der eingebaute Befehl __`return n`__ beendet sie sofort mit dem Status `n`; ohne Zahl mit dem Status des zuletzt ausgeführten Befehls. Anders als `exit` beendet `return` nur die Funktion, nicht das Skript.
:::

```console
$ ist_zahl() { [[ $1 =~ ^[0-9]+$ ]]; }
$ ist_zahl 42
$ echo $?
0
$ ist_zahl 4x2
$ echo $?
1
$ if ist_zahl 17; then echo "eine Zahl"; fi
eine Zahl
```

`ist_zahl` braucht kein `return`: Ihr letzter und einziger Befehl ist die Prüfung, und deren Status wird zum Status der Funktion. Eine solche Prüfung fehlt in `bewertung.sh` aus Abschnitt [4.3](bequemer-prufen-und-case.html#stufe-4-3). Die Arithmetik behandelt ein Wort wie `abc` als Namen einer leeren Variablen, also als 0, und Werte über 100 lässt das Skript ungeprüft durch:

```console
$ ./bewertung.sh abc
nicht bestanden
$ ./bewertung.sh 101
sehr gut
$ cp bewertung.sh bewertung_alt.sh
```

Die Kopie `bewertung_alt.sh` hebt die alte Fassung auf, damit man beide vergleichen kann. Die neue Fassung prüft zuerst und bricht bei ungültigen Punkten ab; `exit 2` beendet das Skript mit dem Status 2, und `>&2` schickt die Meldung auf die Fehlerausgabe ([Kapitel 4, Abschnitt 2.5](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/ausgaben-umleiten.html#stufe-2-5)):

```bash bewertung.sh
#!/bin/bash
# bewertung.sh: macht aus Punkten (0 bis 100) eine Bewertung
ist_zahl() {
    [[ $1 =~ ^[0-9]+$ ]]
}

punkte=$1
if ! ist_zahl "$punkte" || (( punkte > 100 )); then
    echo "Aufruf: bewertung.sh PUNKTE   (eine ganze Zahl von 0 bis 100)" >&2
    exit 2
fi
if (( punkte >= 90 )); then
    echo "sehr gut"
elif (( punkte >= 75 )); then
    echo "gut"
elif (( punkte >= 50 )); then
    echo "bestanden"
else
    echo "nicht bestanden"
fi
```

```console
$ ./bewertung.sh 93
sehr gut
$ ./bewertung.sh abc
Aufruf: bewertung.sh PUNKTE   (eine ganze Zahl von 0 bis 100)
$ echo $?
2
$ ./bewertung.sh 101
Aufruf: bewertung.sh PUNKTE   (eine ganze Zahl von 0 bis 100)
$ echo $?
2
```

Die Reihenfolge in der Bedingung zählt: Ist `punkte` keine Zahl, ist `! ist_zahl` wahr, und `||` wertet den Vergleich gar nicht mehr aus.

⁠**Kurz gesagt:** Eine Funktion antwortet mit ihrem Exit-Status, dem ihres letzten Befehls oder dem aus `return n`; so lässt sie sich direkt in `if` benutzen.

### Ein Ergebnis als Ausgabe

<span class="anker" id="stufe-7-5"></span>

Der Exit-Status ist eine Zahl von 0 bis 255 und taugt nur für Ja und Nein. Ein Ergebnis wie `3,73 Euro` muss auf anderem Weg zurückkommen.

:::satz Satz 7.5 (Rückgabe über die Ausgabe)
<span class="anker" id="satz-7-5"></span>

Eine Funktion gibt ein Ergebnis zurück, indem sie es auf die Standardausgabe schreibt. Der Aufrufer fängt es mit der Befehlsersetzung ein: `wert=$(funktion argumente)` ([Kapitel 5, Abschnitt 2.3](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/variablen-befehlsersetzung-und-arithmetik.html#stufe-2-3)).
:::

Die Funktion `euro` macht aus einem Betrag in Cent einen Text in Euro. `%02d` in der Vorlage von `printf` schreibt eine ganze Zahl mindestens zweistellig, vorn mit Nullen aufgefüllt, aus 5 wird also `05`:

```bash euro.sh
#!/bin/bash
# euro.sh: schreibt Cent-Beträge als Euro
euro() {
    printf '%d,%02d Euro\n' $(( $1 / 100 )) $(( $1 % 100 ))
}

euro 373
euro 5
summe=$(( 249 + 119 + 5 ))
echo "Einkauf: $(euro "$summe")"
```

```console
$ chmod +x euro.sh
$ ./euro.sh
3,73 Euro
0,05 Euro
Einkauf: 3,73 Euro
```

`$(( $1 / 100 ))` ist der ganzzahlige Teil, `$(( $1 % 100 ))` der Rest bei der Teilung durch 100 ([Kapitel 5, Abschnitt 2.4](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/variablen-befehlsersetzung-und-arithmetik.html#stufe-2-4)): $373 = 3\cdot100 + 73$. Abbildung [32](#abb-32) stellt die beiden Rückwege einer Funktion nebeneinander.

:::abbildung linux/k10rueckgabe 32
Eine Funktion als Kasten mit zwei Ausgängen. Oben der Ausgang „Exit-Status“: `ist_zahl 42` schiebt ein kleines Schild `0` hinaus, das direkt in die Weiche eines `if` fällt. Unten der Ausgang „Standardausgabe“: `euro 373` schiebt den Text `3,73 Euro` auf ein Band; die Befehlsersetzung `$( )` fängt ihn auf und legt ihn in die Schublade `preis`. Darunter ein Hinweis: „Status: nur 0 bis 255, für Ja/Nein; Ausgabe: beliebiger Text“.
:::

⁠**Kurz gesagt:** Einen Wert gibt eine Funktion über ihre Ausgabe zurück, eingefangen mit `$(funktion)`; den Exit-Status nimmt man für Ja und Nein.

### Funktion oder Skript

<span class="anker" id="stufe-7-6"></span>

Funktionen und Skripte sehen ähnlich aus: Beide sind benannte Befehlsfolgen mit Argumenten. Ein Unterschied entscheidet, was sie können.

:::satz Satz 7.6 (Funktionen laufen in der eigenen Shell)
<span class="anker" id="satz-7-6"></span>

Eine Funktion läuft in der Shell, die sie aufruft, ohne Kindprozess. Was sie an Variablen und Arbeitsverzeichnis ändert, bleibt nach dem Aufruf bestehen. Ein Skript läuft dagegen in einem Kindprozess (Abschnitt [1.5](vom-befehl-zum-skript.html#stufe-1-5)).
:::

Ein Befehl, der ein Verzeichnis anlegt und hineinwechselt, kann deshalb nur als Funktion funktionieren:

```console
$ mcd() { mkdir -p "$1" && cd "$1"; }
$ mcd fotos/2026
$ pwd
/home/student/linuxk10/fotos/2026
$ cd ~/linuxk10
```

Dieselben Befehle als Skript wechseln nur im Kindprozess:

```bash mcd.sh
#!/bin/bash
# mcd.sh: Verzeichnis anlegen und hineinwechseln (als Skript)
mkdir -p "$1" && cd "$1" && echo "Im Skript: $PWD"
```

```console
$ bash mcd.sh fotos/2027
Im Skript: /home/student/linuxk10/fotos/2027
$ pwd
/home/student/linuxk10
```

Eine Funktion, die in der Befehlszeile angelegt wird, gilt nur in dieser Shell. Soll sie in jedem Terminal bereitstehen, schreibt man sie in die Startdatei `~/.bashrc` ([Kapitel 5, Abschnitt 6.4](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/startdateien-und-aliase.html#stufe-6-4)). Dort ersetzen Funktionen oft Aliase: Ein Alias ersetzt nur Text am Anfang einer Befehlszeile ([Kapitel 5, Abschnitt 6.5](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/startdateien-und-aliase.html#stufe-6-5)), eine Funktion kann ihre Argumente an beliebiger Stelle einsetzen und Entscheidungen treffen. Abbildung [33](#abb-33) zeigt den Unterschied.

:::abbildung linux/k10funktionskript 33
Zwei Spalten. Links `mcd fotos/2026`: Der Kasten „Shell, Verzeichnis ~/linuxk10“ führt die Funktion selbst aus; das Verzeichnis im Kasten springt auf `~/linuxk10/fotos/2026` und bleibt dort. Rechts `bash mcd.sh fotos/2027`: Aus dem Kasten wächst ein Kindprozess mit einer Kopie, nur in der Kopie springt das Verzeichnis auf `fotos/2027`; der Kindprozess verschwindet, der Kasten zeigt weiter `~/linuxk10`.
:::

:::hintergrund Derselbe Grund wie bei `cd`
[Kapitel 2, Abschnitt 3.3](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/arten-von-befehlen.html#stufe-3-3) hat erklärt, warum `cd` ein eingebauter Befehl sein muss: Jeder Prozess hat sein eigenes Arbeitsverzeichnis, und ein Programm in einem Kindprozess könnte nur sein eigenes ändern. Bei Funktionen führt dieselbe Überlegung zum umgekehrten Ergebnis: Weil die Shell sie selbst ausführt, so wie ihre eingebauten Befehle, wirken sie auf ihren Zustand. Deshalb sind Funktionen auch schneller als kleine Skripte: Es muss kein neuer Prozess entstehen und keine neue bash starten.
:::

⁠**Kurz gesagt:** Eine Funktion läuft in der aufrufenden Shell und kann deren Verzeichnis und Variablen ändern; ein Skript kann das nicht.

:::aufgabe Aufgabe 24 ★ Fahrenheit in Celsius
<span class="anker" id="aufg-24"></span>

Schreibe eine Funktion `celsius`, die eine ganze Zahl in Grad Fahrenheit bekommt und die Temperatur in Grad Celsius ausgibt, gerechnet als $(F-32)\cdot5/9$ in ganzen Zahlen. Rufe sie für 212, 32 und 100 auf. Warum muss man erst mit 5 malnehmen und dann durch 9 teilen?

:::loesung
```console
$ celsius() { echo $(( ($1 - 32) * 5 / 9 )); }
$ celsius 212
100
$ celsius 32
0
$ celsius 100
37
$ echo $(( (100 - 32) / 9 * 5 ))
35
```

Genau sind es $(100-32)\cdot5/9 = 340/9 \approx 37{,}8$; die ganzzahlige Teilung schneidet auf 37 ab. Teilt man zuerst, wird schon $68/9 \approx 7{,}6$ auf 7 abgeschnitten, und $7\cdot5=35$ liegt fast drei Grad daneben. Erst malnehmen, dann teilen hält den Fehler der ganzzahligen Teilung unter einem Grad.
:::
:::

:::aufgabe Aufgabe 25 ★★ Wer sieht welche Variable?
<span class="anker" id="aufg-25"></span>

Sage die Ausgabe voraus und prüfe sie, etwa indem du die Zeilen in eine Datei `wersieht.sh` schreibst und `bash wersieht.sh` aufrufst:

```bash wersieht.sh
x=aussen
zeige() { echo "zeige sieht $x"; }
f() { local x=innen; zeige; }
f
zeige
```

:::loesung
```console
$ bash wersieht.sh
zeige sieht innen
zeige sieht aussen
```

Beim ersten Aufruf läuft `zeige` innerhalb von `f`, und dort verdeckt die lokale Variable `x` die des Skripts; `zeige` sieht sie, obwohl sie in `f` angelegt wurde. Beim zweiten Aufruf ist `f` beendet, die lokale Variable verschwunden, und `zeige` sieht wieder `aussen`. Das ist die dynamische Sichtbarkeit aus dem Hintergrund in Abschnitt [7.3](#stufe-7-3).
:::
:::

:::aufgabe Aufgabe 26 ★★ zaehle.sh mit einer Funktion
<span class="anker" id="aufg-26"></span>

Baue `zaehle.sh` aus Abschnitt [5.2](schleifen-for-und-while.html#stufe-5-2) so um, dass eine Funktion `zaehle_datei` eine einzelne Datei bearbeitet: Sie gibt die Zeile mit der Zahl aus und endet mit dem Status 0, oder sie meldet „keine Datei“ und endet mit 1. Die Schleife ruft sie für jedes Argument auf und zählt mit, wie viele Aufrufe gescheitert sind.

:::loesung
Die Funktion meldet mit `return`, ob sie zählen konnte, und die Schleife wertet diesen Status mit `if !` aus. Die Datei heißt hier `zaehle2.sh`, damit die fertige `zaehle.sh` erhalten bleibt:

```bash zaehle2.sh
#!/bin/bash
# zaehle2.sh: zählt die Zeilen jeder angegebenen Datei (mit einer Funktion)
zaehle_datei() {
    local zeilen
    if [ -f "$1" ]; then
        zeilen=$(wc -l < "$1")
        echo "$1: $zeilen Zeilen"
        return 0
    fi
    echo "$1: keine Datei"
    return 1
}

gescheitert=0
for datei in "$@"; do
    if ! zaehle_datei "$datei"; then
        gescheitert=$(( gescheitert + 1 ))
    fi
done
echo "$gescheitert Aufrufe gescheitert"
```

```console
$ chmod +x zaehle2.sh
$ ./zaehle2.sh einkauf.txt fotos gibtsnicht.txt "mein einkauf.txt"
einkauf.txt: 4 Zeilen
fotos: keine Datei
gibtsnicht.txt: keine Datei
mein einkauf.txt: 3 Zeilen
2 Aufrufe gescheitert
```

In der Funktion ist `$1` das Argument des Aufrufs, also die einzelne Datei; `zeilen` ist lokal, damit sie keine Variable des Skripts überschreibt.
:::
:::

:::aufgabe Aufgabe 27 ★★★ Warum kein Alias?
<span class="anker" id="aufg-27"></span>

Warum lässt sich `mcd` nicht als Alias schreiben, etwa `alias mcd='mkdir -p "$1" && cd "$1"'`? Was würde `mcd fotos/2028` damit tun? Überlege es zuerst, probiere es dann aus und entferne den Alias anschließend mit `unalias mcd` ([Kapitel 5, Abschnitt 6.5](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/startdateien-und-aliase.html#stufe-6-5)).

:::loesung
Ein Alias ersetzt nur Text am Anfang der Befehlszeile; er hat keine eigenen Argumente. Aus `mcd fotos/2028` wird `mkdir -p "$1" && cd "$1" fotos/2028`. `$1` ist dabei der erste Positionsparameter der Shell, in der Befehlszeile also leer:

```console
$ alias mcd='mkdir -p "$1" && cd "$1"'
$ mcd fotos/2028
mkdir: cannot create directory '': No such file or directory
$ pwd
/home/student/linuxk10
$ unalias mcd
```

`mkdir` soll ein Verzeichnis mit leerem Namen anlegen und scheitert; `cd` läuft wegen `&&` gar nicht. Selbst wenn es liefe, stünde `fotos/2028` als überzähliges Argument hinter `cd ""`. Eine Funktion bekommt dagegen eigene Positionsparameter (Abschnitt [7.2](#stufe-7-2)). Ein Skript ginge ebenfalls nicht, weil es in einem Kindprozess liefe; nur `source` mit einem Argument wäre noch ein Weg.
:::
:::

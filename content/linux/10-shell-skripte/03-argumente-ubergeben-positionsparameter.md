---
title: Argumente übergeben: Positionsparameter
pfad: Informatik / Linux und Kommandozeile / Shell-Skripte
adresse: informatik/linux-und-kommandozeile/shell-skripte
knoten: Kapitel 10: Shell-Skripte
order: 6150300
summary: Ein Skript, das immer dieselbe Datei bearbeitet, ist wenig nützlich.
tags: Positionsparameter, shift
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Ein Skript, das immer dieselbe Datei bearbeitet, ist wenig nützlich. Dieser Abschnitt zeigt, wie ein Skript die Wörter erreicht, die man beim Aufruf hinter seinen Namen schreibt, und wie man sie weitergibt, ohne dass Namen mit Leerzeichen zerbrechen.
:::

### Der Positionsparameter

<span class="anker" id="stufe-2-1"></span>

Befehle wie `wc` oder `cp` bekommen ihre Dateinamen als Argumente ([Kapitel 2, Abschnitt 2.3](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/der-aufbau-einer-befehlszeile.html#stufe-2-3)). Ein Skript soll das genauso können: `./zeige.sh Milch Brot Käse`. Wie kommt es an die drei Wörter?

Ein Bild zur Orientierung: nummerierte Fächer. Beim Start legt die Shell das erste Argument in Fach 1, das zweite in Fach 2 und so weiter; das Skript greift über die Nummer darauf zu.

:::definition Definition 2.1 (Positionsparameter)
<span class="anker" id="satz-2-1"></span>

Die __Positionsparameter__ `$1`, `$2`, … enthalten die Argumente, mit denen ein Skript aufgerufen wurde, in ihrer Reihenfolge: `$1` das erste Argument, `$2` das zweite. Ab dem zehnten braucht der Name geschweifte Klammern: `${10}`, `${11}`. Ein Positionsparameter ohne zugehöriges Argument ist leer.
:::

Positionsparameter sind Parameter im Sinn von [Kapitel 5, Abschnitt 2.2](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/variablen-befehlsersetzung-und-arithmetik.html#stufe-2-2): Man setzt sie mit `$` in den Text ein, und es gelten dieselben Regeln für Worttrennung und Quoting. Das Skript `zeige.sh` gibt die ersten beiden aus; die Zeilen mit `$0` und `$#` zeigen zwei weitere Parameter, die du hier noch übergehen kannst:

```bash zeige.sh
#!/bin/bash
# zeige.sh: zeigt die ersten Positionsparameter
echo "Skript:  $0"
echo "Anzahl:  $#"
echo "Erstes:  $1"
echo "Zweites: $2"
```

```console
$ chmod +x zeige.sh
$ ./zeige.sh Milch Brot Käse
Skript:  ./zeige.sh
Anzahl:  3
Erstes:  Milch
Zweites: Brot
$ ./zeige.sh "Milch und Brot"
Skript:  ./zeige.sh
Anzahl:  1
Erstes:  Milch und Brot
Zweites:
$ ./zeige.sh
Skript:  ./zeige.sh
Anzahl:  0
Erstes:
Zweites:
```

Welche Wörter zu einem Argument werden, entscheidet die aufrufende Shell, bevor das Skript startet ([Kapitel 5, Abschnitt 3.3](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/worttrennung-und-quoting.html#stufe-3-3)): `"Milch und Brot"` ist ein einziges Argument, also landet alles in `$1`. Abbildung [5](#abb-5) zeigt die Verteilung auf die Fächer.

:::abbildung linux/k10parameter 5
Die Befehlszeile `./zeige.sh Milch Brot Käse` oben als Folge von Wörtern. Die Wörter fallen nacheinander in nummerierte Fächer: `./zeige.sh` in Fach 0, `Milch` in 1, `Brot` in 2, `Käse` in 3; die Fächer 4 bis 9 bleiben leer. Ein Zähler `$#` springt mit jedem gefüllten Fach ab 1 hoch bis 3. Zweiter Durchgang mit `./zeige.sh "Milch und Brot"`: Das ganze Wort in Anführungszeichen fällt in Fach 1, der Zähler steht auf 1.
:::

::::beispiel Der zehnte Parameter
Ohne Klammern liest die Shell `$10` als `$1` mit einer angehängten Null. Das Skript `zehn.sh` zeigt beides; die Klammererweiterung `{a..k}` erzeugt elf Argumente ([Kapitel 5, Abschnitt 1.6](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/expansion-muster-klammern-und-tilde.html#stufe-1-6)):

```bash zehn.sh
#!/bin/bash
# zehn.sh: der zehnte Positionsparameter
echo "Mit Klammern:  ${10}"
echo "Ohne Klammern: $10"
```

```console
$ chmod +x zehn.sh
$ ./zehn.sh {a..k}
Mit Klammern:  j
Ohne Klammern: a0
```
::::

⁠**Kurz gesagt:** `$1`, `$2`, … enthalten die Argumente des Skripts in ihrer Reihenfolge; ab dem zehnten schreibt man `${10}`.

### Der Name des Skripts: `$0`

<span class="anker" id="stufe-2-2"></span>

Meldungen eines Skripts sollen sagen, von wem sie stammen, etwa `zaehle.sh: Datei fehlt`. Dafür muss das Skript seinen eigenen Namen kennen.

:::definition Definition 2.2 (`$0`)
<span class="anker" id="satz-2-2"></span>

Der Parameter `$0` enthält den Namen, unter dem das Skript aufgerufen wurde, genau so, wie er in der Befehlszeile stand, also gegebenenfalls mit Pfad.
:::

Wie `$0` aussieht, hängt deshalb vom Aufruf ab:

```console
$ bash zeige.sh Milch
Skript:  zeige.sh
Anzahl:  1
Erstes:  Milch
Zweites:
$ ~/linuxk10/zeige.sh Milch
Skript:  /home/student/linuxk10/zeige.sh
Anzahl:  1
Erstes:  Milch
Zweites:
$ basename ~/linuxk10/zeige.sh
zeige.sh
```

Für Meldungen will man meist nur den Dateinamen ohne Verzeichnisse. Den liefert der Befehl `basename`; im Skript schreibt man `programm=$(basename "$0")` mit der Befehlsersetzung aus [Kapitel 5, Abschnitt 2.3](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/variablen-befehlsersetzung-und-arithmetik.html#stufe-2-3). Abbildung [6](#abb-6) vergleicht die Aufrufe.

:::abbildung linux/k10null 6
Drei Aufrufe desselben Skripts untereinander: `./zeige.sh`, `bash zeige.sh` und `~/linuxk10/zeige.sh`. Neben jedem erscheint das Fach 0 mit seinem Inhalt (`./zeige.sh`, `zeige.sh`, `/home/student/linuxk10/zeige.sh`). Ein Trichter `basename` macht aus allen drei Inhalten dasselbe `zeige.sh`.
:::

⁠**Kurz gesagt:** `$0` ist der Name, unter dem das Skript aufgerufen wurde; `basename "$0"` macht daraus den bloßen Dateinamen.

### Die Zahl der Argumente: `$#`

<span class="anker" id="stufe-2-3"></span>

Bevor ein Skript mit `$1` arbeitet, muss es wissen, ob überhaupt ein Argument da ist. Sonst bearbeitet es einen leeren Namen.

:::definition Definition 2.3 (`$#`)
<span class="anker" id="satz-2-3"></span>

Der Parameter `$#` enthält die Zahl der Positionsparameter, also die Zahl der Argumente, mit denen das Skript aufgerufen wurde. `$0` zählt nicht mit.
:::

Die Ausgaben von `zeige.sh` oben zeigen `$#` bei drei, einem und keinem Argument. Ein Argument kann leer sein und zählt trotzdem: Bei `./zeige.sh ""` ist `$#` gleich 1.

⁠**Kurz gesagt:** `$#` ist die Zahl der Argumente, ohne `$0`.

### Alle Argumente: `"$@"`

<span class="anker" id="stufe-2-4"></span>

Oft soll ein Skript alle Argumente an einen Befehl weiterreichen, egal wie viele es sind, etwa alle Dateinamen an `wc`. Man könnte `$1 $2 $3` schreiben, aber dann sind es immer genau drei. Und jedes Argument soll beim Weiterreichen genau ein Argument bleiben, auch `mein einkauf.txt`.

:::definition Definition 2.4 (`"$@"`)
<span class="anker" id="satz-2-4"></span>

Der Ausdruck `"$@"` in doppelten Anführungszeichen wird zu allen Positionsparametern ab `$1`, jeder als eigenes Wort und unverändert, als stünde jeder einzeln in doppelten Anführungszeichen: `"$1" "$2" "$3"` und so weiter. Gibt es keine Argumente, wird `"$@"` zu gar keinem Wort.
:::

Das ist eine Ausnahme von der Regel aus [Kapitel 5, Abschnitt 3.5](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/worttrennung-und-quoting.html#stufe-3-5), nach der doppelte Anführungszeichen immer genau ein Wort ergeben. Das Skript `alle.sh` zeigt jedes Wort, das ankommt, in eckigen Klammern; `printf` wiederholt seine Vorlage für jedes Argument ([Kapitel 5, Abschnitt 3.1](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/worttrennung-und-quoting.html#stufe-3-1)). Zum Vergleich zeigt es zwei weitere Schreibweisen, die in älteren Skripten häufig vorkommen:

```bash alle.sh
#!/bin/bash
# alle.sh: vergleicht "$@", $* und "$*"
echo 'Mit "$@":'
printf '  [%s]\n' "$@"
echo 'Mit $*:'
printf '  [%s]\n' $*
echo 'Mit "$*":'
printf '  [%s]\n' "$*"
```

```console
$ chmod +x alle.sh
$ ./alle.sh Milch "Äpfel und Birnen" '*.txt'
Mit "$@":
  [Milch]
  [Äpfel und Birnen]
  [*.txt]
Mit $*:
  [Milch]
  [Äpfel]
  [und]
  [Birnen]
  [einkauf.txt]
  [mein einkauf.txt]
Mit "$*":
  [Milch Äpfel und Birnen *.txt]
```

Nur `"$@"` gibt die drei Argumente so weiter, wie sie gemeint waren. Abbildung [7](#abb-7) stellt die drei Schreibweisen nebeneinander.

:::abbildung linux/k10at 7
Drei Argumente als Kärtchen: `Milch`, `Äpfel und Birnen`, `*.txt`. Darunter drei Bahnen. Bahn `"$@"`: Die drei Kärtchen kommen unverändert unten an. Bahn `$*`: Das mittlere Kärtchen zerfällt an den Leerzeichen in drei (Etikett „Worttrennung“), `*.txt` verwandelt sich in die beiden Dateinamen (Etikett „Pfadnamen-Erweiterung“), unten liegen sechs Kärtchen. Bahn `"$*"`: Alle Kärtchen werden mit Leerzeichen zu einem langen Kärtchen verklebt.
:::

::::beispiel Ein Skript, das alle Dateien zählt
Die erste Fassung von `zaehle.sh` reicht alle Argumente an `wc -l` weiter:

```bash zaehle.sh
#!/bin/bash
# zaehle.sh: zählt die Zeilen jeder angegebenen Datei
wc -l "$@"
```

```console
$ chmod +x zaehle.sh
$ ./zaehle.sh einkauf.txt "mein einkauf.txt"
 4 einkauf.txt
 3 mein einkauf.txt
 7 total
```

Ersetzt man im Skript `"$@"` durch `$*`, zerbricht der zweite Name, und `wc` bekommt drei Argumente, von denen eines zufällig wieder `einkauf.txt` heißt:

```console
$ ./zaehle.sh einkauf.txt "mein einkauf.txt"
 4 einkauf.txt
wc: mein: No such file or directory
 4 einkauf.txt
 8 total
```

Danach stellst du `"$@"` wieder her; die folgenden Abschnitte bauen auf der richtigen Fassung auf.
::::

:::hintergrund Warum es `"$@"` überhaupt gibt
Eine gewöhnliche Variable enthält einen einzigen Text. Die Argumente eines Skripts sind dagegen eine Liste von Texten, und beim Einsetzen kann die Shell eine Liste nur auf zwei Arten in Wörter verwandeln: zu einem einzigen Wort verklebt oder zu einzelnen Wörtern zerlegt. Verkleben verliert die Grenzen zwischen den Argumenten, Zerlegen an Leerzeichen erfindet neue Grenzen. Schon die Bourne-Shell, aus der die bash hervorgegangen ist, hatte deshalb für `$@` eine eigene Regel: In doppelten Anführungszeichen erhält jeder Positionsparameter sein eigenes Wort, die alten Grenzen bleiben exakt erhalten. Es ist die einzige Stelle, an der eine Ersetzung in doppelten Anführungszeichen mehr als ein Wort ergibt. Der Standard für Unix-Shells schreibt diese Regel bis heute vor.
:::

⁠**Kurz gesagt:** `"$@"` gibt jedes Argument als eigenes, unverändertes Wort weiter; es ist fast immer die richtige Schreibweise.

### `$*` und `"$*"`

<span class="anker" id="stufe-2-5"></span>

Neben `"$@"` gibt es eine zweite Schreibweise für alle Argumente. Sie sieht ähnlich aus, verhält sich aber anders, und sie steht in vielen älteren Skripten.

:::definition Definition 2.5 (`$*` und `"$*"`)
<span class="anker" id="satz-2-5"></span>

`$*` wird ohne Anführungszeichen zu allen Positionsparametern, die danach Worttrennung und Pfadnamen-Erweiterung durchlaufen ([Kapitel 5, Abschnitte 3.2](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/worttrennung-und-quoting.html#stufe-3-2) und [1.3](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/expansion-muster-klammern-und-tilde.html#stufe-1-3)). `"$*"` in doppelten Anführungszeichen wird zu einem einzigen Wort, in dem die Positionsparameter durch ein Leerzeichen getrennt aneinanderhängen. Auch `$@` ohne Anführungszeichen verhält sich wie `$*`.
:::

Die Ausgabe von `alle.sh` zeigt beide Fehler von `$*`: `Äpfel und Birnen` wird an den Leerzeichen zerlegt, und das Muster `*.txt`, das als Text gemeint war, wird zu Dateinamen. `"$*"` hat einen sinnvollen Zweck: wenn man alle Argumente bewusst zu einem Satz verbinden will, etwa für eine Meldung wie `echo "Suche nach: $*"`. Die Regel lautet daher: Argumente weiterreichen mit `"$@"`, zu einem Text verbinden mit `"$*"`, `$*` und `$@` ohne Anführungszeichen nie.

::::beispiel Weiterreichen oder verbinden
Mit den Argumenten `Milch` und `Äpfel und Birnen` ergibt `cp "$@" ziel/` den Aufruf `cp` mit den Argumenten `Milch`, `Äpfel und Birnen` und `ziel/`, also zwei Quellen; `echo "Gekauft: $*"` ergibt die eine Zeile `Gekauft: Milch Äpfel und Birnen`.
::::

⁠**Kurz gesagt:** `"$*"` verklebt alle Argumente zu einem Wort, `$*` zerlegt sie neu; zum Weiterreichen taugt nur `"$@"`.

### Argumente verschieben: `shift`

<span class="anker" id="stufe-2-6"></span>

Manche Skripte erwarten zuerst ein besonderes Argument, etwa ein Zielverzeichnis, und danach beliebig viele Dateien. Nach dem ersten Argument soll `"$@"` nur noch die Dateien enthalten.

:::definition Definition 2.6 (`shift`)
<span class="anker" id="satz-2-6"></span>

Der eingebaute Befehl __`shift`__ entfernt den ersten Positionsparameter und rückt alle übrigen um eine Stelle nach vorn: `$2` wird zu `$1`, `$3` zu `$2` und so weiter; `$#` wird um eins kleiner. `shift n` rückt um $n$ Stellen. `$0` bleibt unverändert.
:::

```bash schiebe.sh
#!/bin/bash
# schiebe.sh: zeigt, was shift mit den Positionsparametern macht
echo "Vorher:  $# Argumente, das erste ist $1"
shift
echo "Nachher: $# Argumente, das erste ist $1"
```

```console
$ chmod +x schiebe.sh
$ ./schiebe.sh Milch Brot Käse
Vorher:  3 Argumente, das erste ist Milch
Nachher: 2 Argumente, das erste ist Brot
```

Das typische Muster ist `ziel=$1`, dann `shift`, dann `"$@"` für den Rest. Abbildung [8](#abb-8) zeigt das Nachrücken.

:::abbildung linux/k10shift 8
Die Fächer 1 bis 3 mit `Milch`, `Brot`, `Käse` und der Zähler `$# = 3`. Bei `shift` fällt `Milch` aus Fach 1 heraus, `Brot` und `Käse` rutschen je ein Fach nach links, Fach 3 wird leer, der Zähler springt auf 2. Fach 0 mit `./schiebe.sh` bleibt fest an seinem Platz.
:::

⁠**Kurz gesagt:** `shift` wirft `$1` weg und lässt alle anderen Argumente eine Stelle nachrücken.

:::aufgabe Aufgabe 5 ★ Argumente zählen
<span class="anker" id="aufg-5"></span>

Im Übungsverzeichnis liegen die Dateien `einkauf.txt` und `mein einkauf.txt`, die Variable `leer` ist leer. Sage für jeden Aufruf voraus, was `zeige.sh` bei `Anzahl` und `Erstes` ausgibt, und prüfe es: (a) `./zeige.sh "a b" c`, (b) `./zeige.sh *.txt`, (c) `./zeige.sh ""`, (d) `./zeige.sh $leer`, (e) `./zeige.sh '$HOME'`.

:::loesung
```console
$ leer=
$ ./zeige.sh "a b" c
Skript:  ./zeige.sh
Anzahl:  2
Erstes:  a b
Zweites: c
$ ./zeige.sh *.txt
Skript:  ./zeige.sh
Anzahl:  2
Erstes:  einkauf.txt
Zweites: mein einkauf.txt
$ ./zeige.sh ""
Skript:  ./zeige.sh
Anzahl:  1
Erstes:
Zweites:
$ ./zeige.sh $leer
Skript:  ./zeige.sh
Anzahl:  0
Erstes:
Zweites:
$ ./zeige.sh '$HOME'
Skript:  ./zeige.sh
Anzahl:  1
Erstes:  $HOME
Zweites:
```

(a) Die Anführungszeichen machen `a b` zu einem Argument. (b) Die aufrufende Shell ersetzt das Muster durch zwei Namen, und `mein einkauf.txt` bleibt dabei ein Wort. (c) Ein leeres Argument in Anführungszeichen zählt mit. (d) Die leere Variable ohne Anführungszeichen ergibt gar kein Wort. (e) In einfachen Anführungszeichen wird `$HOME` nicht ersetzt; das Skript bekommt den Text `$HOME`, und auch beim Einsetzen von `$1` im Skript wird er nicht noch einmal ersetzt.
:::
:::

:::aufgabe Aufgabe 6 ★★ Ein Ziel und viele Dateien
<span class="anker" id="aufg-6"></span>

Schreibe ein Skript `kopiere.sh`, das als erstes Argument ein Zielverzeichnis bekommt und alle weiteren Argumente als Dateien dorthin kopiert. Benutze `shift` und `"$@"`. Teste es mit einem Verzeichnis `ablage` und den beiden Einkaufslisten. Was geht schief, wenn du `"$@"` durch `$*` ersetzt?

:::loesung
```bash kopiere.sh
#!/bin/bash
# kopiere.sh: kopiert alle Dateien ab dem zweiten Argument in das Verzeichnis im ersten
ziel=$1
shift
cp -- "$@" "$ziel"
```

```console
$ chmod +x kopiere.sh
$ mkdir ablage
$ ./kopiere.sh ablage einkauf.txt "mein einkauf.txt"
$ ls ablage
 einkauf.txt  'mein einkauf.txt'
```

Nach `ziel=$1` und `shift` enthält `"$@"` genau die Dateien. `--` schützt vor Dateinamen, die mit einem Strich beginnen. Mit `$*` statt `"$@"` zerbricht der zweite Name:

```console
$ rm ablage/*
$ ./kopiere.sh ablage einkauf.txt "mein einkauf.txt"
cp: cannot stat 'mein': No such file or directory
cp: warning: source file 'einkauf.txt' specified more than once
$ ls ablage
einkauf.txt
```

`cp` bekommt `einkauf.txt`, `mein` und noch einmal `einkauf.txt`; die zweite Einkaufsliste wird gar nicht kopiert.
:::
:::

:::aufgabe Aufgabe 7 ★★ Vorhersagen mit `$0` und `$10`
<span class="anker" id="aufg-7"></span>

Was geben (a) `./zehn.sh {1..12}` und (b) `bash zehn.sh {1..9}` aus? Warum gibt (b) bei „Ohne Klammern“ etwas aus, bei „Mit Klammern“ aber nichts?

:::loesung
```console
$ ./zehn.sh {1..12}
Mit Klammern:  10
Ohne Klammern: 10
$ bash zehn.sh {1..9}
Mit Klammern:
Ohne Klammern: 10
```

(a) `${10}` ist das zehnte Argument, also `10`. `$10` ist `$1` mit angehängter Null, also `1` und `0`, und das ergibt zufällig ebenfalls `10`. (b) Es gibt nur neun Argumente, `${10}` ist leer. `$10` ist wieder `$1` plus `0` und sieht deshalb aus wie ein zehntes Argument, das es gar nicht gibt. `$0` spielt in keinem Fall eine Rolle.
:::
:::

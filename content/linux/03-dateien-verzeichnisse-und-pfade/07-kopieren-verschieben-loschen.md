---
title: Kopieren, verschieben, löschen
pfad: Informatik / Linux und Kommandozeile / Dateien, Verzeichnisse und Pfade
adresse: informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade
knoten: Kapitel 3: Dateien, Verzeichnisse und Pfade
order: 6080700
summary: Mit Dateien arbeitet man nicht nur, man räumt sie auch um: eine Sicherheitskopie anlegen, einen Namen ändern, Altes wegwerfen.
tags: cp, -r, mv, rm, rmdir, Muster
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Mit Dateien arbeitet man nicht nur, man räumt sie auch um: eine Sicherheitskopie anlegen, einen Namen ändern, Altes wegwerfen. Dieser Abschnitt zeigt die Befehle dafür, warnt vor ihren Tücken und führt Muster ein, mit denen ein Befehl viele Dateien auf einmal trifft. Alle Beispiele laufen im Übungsverzeichnis `~/linuxk3`.
:::

### Kopieren: cp

<span class="anker" id="stufe-6-1"></span>

Bevor man eine Datei umbaut, hebt man gern den alten Stand auf. Dafür braucht man eine zweite, unabhängige Datei mit demselben Inhalt. Abbildung [21](#abb-21) zeigt, was „unabhängig“ dabei heißt.

:::abbildung linux/k3cp 21
Nach `cp einkauf.txt einkauf_alt.txt` gibt es zwei Dateien mit gleichem Inhalt. Wird danach eine von beiden geändert, bleibt die andere, wie sie war: Die Kopie ist eigenständig.
:::

:::definition Definition 6.1 (cp)
<span class="anker" id="satz-6-1"></span>

Der Befehl __cp__ (kurz für „copy“) kopiert eine Datei: `cp quelle ziel` legt unter dem Namen `ziel` eine neue Datei mit demselben Inhalt an. Ist `ziel` ein vorhandenes Verzeichnis, landet die Kopie darin unter dem alten Namen. Nennt man mehrere Quellen, muss das letzte Argument ein Verzeichnis sein.
:::

Gibt es eine Datei `ziel` schon, überschreibt `cp` sie ohne Rückfrage; ihr alter Inhalt ist dann verloren. Die Option `-i` (kurz für „interactive“) lässt `cp` vorher fragen, `-v` (kurz für „verbose“, gesprächig) meldet jede Kopie.

::::beispiel Eine Sicherheitskopie und eine Kopie in ein Verzeichnis
```console
$ cp einkauf.txt einkauf_alt.txt
$ cp einkauf.txt rezepte
$ ls rezepte
einkauf.txt  kuchen  suppen
$ cp einkauf.txt einkauf_alt.txt neu.txt
cp: target 'neu.txt': No such file or directory
```

Die erste Zeile legt eine Kopie unter neuem Namen an, die zweite eine Kopie in `rezepte` unter dem alten Namen. Die letzte scheitert: Bei drei Argumenten erwartet `cp` als Ziel ein Verzeichnis `neu.txt`, und das gibt es nicht.
::::

::::beispiel [Zweites Beispiel] Erst fragen, dann melden
```console
$ cp -i einkauf.txt einkauf_alt.txt
cp: overwrite 'einkauf_alt.txt'? n
$ cp -v einkauf.txt einkauf_alt.txt
'einkauf.txt' -> 'einkauf_alt.txt'
```

Mit `-i` fragt `cp`, ob es `einkauf_alt.txt` überschreiben soll; `n` und die Eingabetaste lassen die Datei in Ruhe, `y` hätte sie überschrieben. Ohne `-i` überschreibt der zweite Befehl kommentarlos; `-v` sagt wenigstens, was geschehen ist.
::::

⁠**Kurz gesagt:** `cp quelle ziel` legt eine eigenständige Kopie an und überschreibt ein vorhandenes Ziel ohne Rückfrage; `-i` fragt vorher.

### Verzeichnisse kopieren: cp -r

<span class="anker" id="stufe-6-2"></span>

Eine Sicherung soll oft ein ganzes Verzeichnis umfassen, mit allen Unterverzeichnissen und Dateien. Ohne besondere Option weigert sich `cp` aber, Verzeichnisse anzufassen.

:::abbildung linux/k3cpr 22
`cp -r rezepte sicherung` zweimal hintereinander. Beim ersten Mal gibt es `sicherung` noch nicht: Es entsteht als Kopie von `rezepte`. Beim zweiten Mal gibt es `sicherung` schon: Die Kopie landet darin als `sicherung/rezepte`.
:::

:::definition Definition 6.2 (cp -r)
<span class="anker" id="satz-6-2"></span>

Mit der Option __-r__ (kurz für „recursive“) kopiert `cp` ein Verzeichnis samt allem, was darin liegt, Ebene für Ebene. Gibt es das Ziel noch nicht, wird es die Kopie; ist das Ziel ein vorhandenes Verzeichnis, landet die Kopie darin.
:::

„Rekursiv“ heißt, dass `cp` für jedes Unterverzeichnis dasselbe noch einmal tut, bis keine Ebene mehr übrig ist. Das Verhalten beim Ziel folgt derselben Regel wie bei Dateien und überrascht trotzdem viele, wie Abbildung [22](#abb-22) zeigt.

::::beispiel Zweimal dieselbe Zeile
```console
$ cp rezepte sicherung
cp: -r not specified; omitting directory 'rezepte'
$ cp -r rezepte sicherung
$ ls sicherung
einkauf.txt  kuchen  suppen
$ cp -r rezepte sicherung
$ ls sicherung
einkauf.txt  kuchen  rezepte  suppen
```

Ohne `-r` lässt `cp` das Verzeichnis aus und sagt das. Beim ersten `cp -r` entsteht `sicherung` mit demselben Inhalt wie `rezepte`. Beim zweiten gibt es `sicherung` schon, also landet eine weitere Kopie als `sicherung/rezepte` darin.
::::

⁠**Kurz gesagt:** `cp -r` kopiert ganze Verzeichnisse; ist das Ziel schon da, entsteht die Kopie darin.

:::hintergrund Was eine Kopie nicht mitnimmt
Eine Kopie bekommt einen neuen Zeitstempel und gehört dem, der kopiert hat. Für eine Sicherung ist das unpraktisch, denn man will später sehen, wann das Original zuletzt geändert wurde. Die Option `-a` (kurz für „archive“) kopiert rekursiv wie `-r` und übernimmt dabei Zeitstempel, Zugriffsrechte und, soweit erlaubt, den Besitzer. Wer ein Verzeichnis sichern will, nimmt deshalb meist `cp -a`.
:::

### Verschieben und umbenennen: mv

<span class="anker" id="stufe-6-3"></span>

Eine Datei soll einen besseren Namen bekommen oder in ein anderes Verzeichnis wandern. Unter Linux ist beides derselbe Vorgang, und es gibt dafür einen einzigen Befehl. Abbildung [23](#abb-23) zeigt, warum.

:::abbildung linux/k3mv 23
`mv` ändert nur Einträge. Beim Umbenennen bekommt der Eintrag einen neuen Namen, beim Verschieben verschwindet er aus der einen Liste und erscheint in einer anderen. Die Daten der Datei bleiben dabei, wo sie sind.
:::

:::definition Definition 6.3 (mv)
<span class="anker" id="satz-6-3"></span>

Der Befehl __mv__ (kurz für „move“) gibt einer Datei oder einem Verzeichnis einen neuen Namen oder einen neuen Ort: `mv quelle ziel` benennt `quelle` in `ziel` um. Ist `ziel` ein vorhandenes Verzeichnis, verschiebt `mv` die Quelle hinein und behält ihren Namen.
:::

Danach gibt es den alten Namen nicht mehr. Eine vorhandene Datei `ziel` überschreibt `mv` ohne Rückfrage, genau wie `cp`; auch hier fragt `-i` vorher. Anders als `cp` braucht `mv` für Verzeichnisse keine Option.

::::beispiel Umbenennen, verschieben, ein Verzeichnis umbenennen
```console
$ mv einkauf_alt.txt einkauf_montag.txt
$ mv einkauf_montag.txt sicherung
$ ls
einkauf.txt  fotos  rezepte  sicherung
$ mv sicherung archiv
$ ls -F
archiv/  einkauf.txt  fotos/  rezepte/
```

Die erste Zeile benennt um. Die zweite verschiebt, denn `sicherung` ist ein Verzeichnis. Die vierte benennt das Verzeichnis `sicherung` samt Inhalt in `archiv` um, weil es `archiv` noch nicht gibt; gäbe es ein Verzeichnis `archiv`, landete `sicherung` darin.
::::

⁠**Kurz gesagt:** `mv` benennt um oder verschiebt, je nachdem, ob das Ziel ein vorhandenes Verzeichnis ist; ein vorhandenes Ziel wird ohne Rückfrage ersetzt.

:::hintergrund Warum mv sofort fertig ist
Ein Verzeichnis ist eine Liste von Einträgen (Unterabschnitt [1.3](dateien-verzeichnisse-und-der-verzeichnisbaum.html#stufe-1-3)). Verschiebt man eine Datei innerhalb desselben Dateisystems ([Kapitel 1, Abschnitt 5.3](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/datentrager-abbild-und-prufsumme.html#stufe-5-3)), muss `mv` keine Daten anfassen: Es trägt den Namen in der Zielliste ein und streicht ihn aus der alten. Dafür gibt es einen einzigen Systemaufruf, und der Kernel führt ihn in aller Regel so aus, dass auch ein Absturz mittendrin keinen halben Zustand hinterlässt: Danach gibt es entweder den alten oder den neuen Namen. Deshalb ist eine Datei mit vielen Gigabyte genauso schnell verschoben wie eine leere. Anders ist es, wenn Quelle und Ziel in verschiedenen Dateisystemen liegen, etwa auf zwei Datenträgern. Dann kann der Kernel keinen Eintrag umhängen, und `mv` kopiert die Daten wie `cp -a` und löscht danach das Original. Das dauert so lange wie eine Kopie.
:::

### Löschen: rm

<span class="anker" id="stufe-6-4"></span>

Was man nicht mehr braucht, soll weg. Wer von Windows kommt, erwartet einen Papierkorb, aus dem man Versehen wieder herausholen kann. An der Kommandozeile gibt es ihn nicht; Abbildung [24](#abb-24) stellt beide Wege gegenüber.

:::abbildung linux/k3papierkorb 24
Zwei Arten, eine Datei loszuwerden. Oben der Papierkorb einer grafischen Oberfläche: Die Datei wird nur in ein besonderes Verzeichnis verschoben und kann zurück. Unten `rm`: Der Eintrag verschwindet aus dem Verzeichnis, und es gibt keinen Weg zurück.
:::

:::definition Definition 6.4 (rm)
<span class="anker" id="satz-6-4"></span>

Der Befehl __rm__ (kurz für „remove“) entfernt die genannten Dateien aus ihren Verzeichnissen, sofort und in der Regel ohne Rückfrage. Es gibt keinen Befehl, der das rückgängig macht. Verzeichnisse lässt `rm` ohne weitere Option stehen.
:::

`rm -i` fragt vor jeder Datei nach, `rm -v` meldet jede gelöschte. Ein `rm` ohne Rückfrage ist für Linux der Normalfall: Wer den Befehl tippt, soll wissen, was er tut.

:::warnung Kein Papierkorb
Was `rm` entfernt, ist weg. Prüfe vor jedem `rm` den Namen, am besten mit `ls` und genau demselben Argument; die Tabulatortaste verhindert Tippfehler. Wichtige Dateien sicherst du vorher mit `cp`. Unter WSL 2 löschst du mit `rm` unter `/mnt/c` auch Windows-Dateien endgültig, an jedem Papierkorb von Windows vorbei.
:::

::::beispiel Eine Datei löschen und zwei Fehlversuche
```console
$ rm rezepte/einkauf.txt
$ rm gibtsnicht.txt
rm: cannot remove 'gibtsnicht.txt': No such file or directory
$ rm archiv
rm: cannot remove 'archiv': Is a directory
```

Die Kopie in `rezepte` ist ohne jede Meldung verschwunden. Eine Datei, die es nicht gibt, kann `rm` nicht entfernen, und an ein Verzeichnis geht es ohne Option nicht heran.
::::

::::beispiel [Zweites Beispiel] Mit Rückfrage
```console
$ rm -i einkauf.txt
rm: remove regular file 'einkauf.txt'? n
```

`rm` nennt die Art der Datei, eine gewöhnliche Datei, und wartet. Die Antwort `n` lässt die Einkaufsliste stehen.
::::

⁠**Kurz gesagt:** `rm` löscht Dateien sofort und endgültig; `rm -i` fragt vorher.

:::hintergrund Was der Papierkorb einer Oberfläche eigentlich ist
Auch unter Linux haben die grafischen Oberflächen einen Papierkorb. Er ist kein Teil des Kernels, sondern eine Abmachung zwischen den Dateimanagern: Wer eine Datei „in den Papierkorb legt“, verschiebt sie in das Verzeichnis `~/.local/share/Trash/files` und schreibt in `~/.local/share/Trash/info` eine kleine Textdatei mit dem ursprünglichen Pfad und dem Zeitpunkt. Daraus kann der Dateimanager die Datei an ihren alten Platz zurücklegen. Ein Papierkorb ist also ein `mv`, kein Löschen. `rm` kennt diese Abmachung nicht; es löscht wirklich.
:::

### Verzeichnisse löschen: rmdir und rm -r

<span class="anker" id="stufe-6-5"></span>

Auch Verzeichnisse will man irgendwann loswerden. Dafür gibt es zwei Wege: einen vorsichtigen, der nur leere Verzeichnisse entfernt, und einen gründlichen, der alles mitnimmt.

:::definition Definition 6.5 (rmdir, rm -r)
<span class="anker" id="satz-6-5"></span>

Der Befehl __rmdir__ (kurz für „remove directory“) entfernt ein Verzeichnis nur, wenn es leer ist. `rm` mit der Option __-r__ entfernt ein Verzeichnis samt allem, was darin liegt, Ebene für Ebene und ohne Rückfrage.
:::

Die Option `-f` (kurz für „force“) lässt `rm` zusätzlich nie nachfragen und über fehlende Dateien schweigen. Die Zeile `rm -rf` findet man deshalb in vielen Anleitungen, und sie ist der gefährlichste Befehl dieses Kapitels: Ein falscher Pfad, und ein ganzer Teilbaum ist verloren.

::::beispiel Das Archiv entfernen
```console
$ rmdir archiv
rmdir: failed to remove 'archiv': Directory not empty
$ rm -r archiv
$ mkdir leer
$ rmdir leer
$ ls -F
einkauf.txt  fotos/  rezepte/
```

`rmdir` weigert sich, weil `archiv` Dateien enthält; `rm -r` entfernt es mit allem. Das frisch angelegte, leere Verzeichnis `leer` entfernt `rmdir` ohne Fehlermeldung.
::::

⁠**Kurz gesagt:** `rmdir` löscht nur leere Verzeichnisse, `rm -r` ganze Teilbäume ohne Rückfrage.

:::warnung rm -r nur mit geprüftem Pfad
Lass dir vor jedem `rm -r` mit `ls` oder `tree` zeigen, was darunter liegt, und tippe den Pfad mit der Tabulatortaste. Gib `rm -r` nie einen Pfad, der mit `/` beginnt, wenn du nicht genau weißt, warum. Wer unsicher ist, nimmt `rm -ri` und beantwortet jede Frage einzeln.
:::

:::hintergrund Warum rmdir nur leere Verzeichnisse löscht
Ein Verzeichnis zu entfernen kann sehr viel mehr Daten treffen als eine einzelne Datei. Der Systemaufruf, mit dem man ein Verzeichnis entfernt, verlangt deshalb, dass es leer ist, also nur noch `.` und `..` enthält; sonst scheitert er. `rmdir` ist nur eine dünne Hülle um diesen Aufruf. `rm -r` dagegen geht den Baum selbst von unten nach oben durch: Es löscht zuerst alle Dateien eines Verzeichnisses, dann das nun leere Verzeichnis, und so weiter bis zum obersten. Die Sicherung im Kernel bleibt also bestehen; `rm -r` erfüllt sie nur, indem es die Vorarbeit selbst leistet.
:::

### Muster für Dateinamen

<span class="anker" id="stufe-6-6"></span>

Zwanzig Urlaubsfotos einzeln in ein Verzeichnis zu verschieben, ist mühsam. Schöner wäre ein Befehl, der sagt: alle Dateien, die auf `.jpg` enden. Abbildung [25](#abb-25) zeigt, wie ein Muster Namen auswählt.

:::abbildung linux/k3muster 25
Ein Muster wählt Namen aus einer Liste. Nacheinander werden `*.jpg`, `strand_?.jpg` und `*_[12].jpg` auf die sechs Dateien in `fotos/urlaub/2026` gelegt; die passenden Namen leuchten auf, die übrigen bleiben grau.
:::

:::definition Definition 6.6 (Muster für Dateinamen)
<span class="anker" id="satz-6-6"></span>

Ein __Muster__ ist ein Wort der Befehlszeile, das eines der Zeichen `*`, `?` oder `[` enthält. Die Shell ersetzt es vor dem Start des Befehls durch alle passenden Namen, nach Namen sortiert. Dabei steht `*` für eine beliebige Folge von Zeichen, auch für gar keine, `?` für genau ein beliebiges Zeichen, `[abc]` für genau eines der Zeichen in der Klammer, `[0-9]` für genau eines aus einem Bereich und `[!abc]` für genau ein Zeichen, das nicht in der Klammer steht.
:::

Ein Muster wirkt wie ein Sieb, durch das die Namen des Verzeichnisses fallen (ein Bild zur Orientierung). Namen, die mit einem Punkt beginnen, erfasst es nur, wenn es selbst mit einem Punkt beginnt; versteckte Dateien bleiben also auch hier verborgen. Wichtig ist, wer die Arbeit macht: die Shell, nicht der Befehl. `ls` bekommt nie das Muster zu sehen, sondern die fertige Liste der Namen, als hätte man sie einzeln getippt. Deshalb funktionieren Muster mit jedem Befehl, der Dateinamen als Argumente nimmt.

::::beispiel Fotos auswählen
```console
$ cd fotos/urlaub/2026
$ ls
berg_1.jpg  notiz.txt     strand_10.jpg
berg_2.jpg  strand_1.jpg  strand_2.jpg
$ ls *.jpg
berg_1.jpg  berg_2.jpg  strand_1.jpg  strand_10.jpg  strand_2.jpg
$ ls strand_?.jpg
strand_1.jpg  strand_2.jpg
$ ls strand_*.jpg
strand_1.jpg  strand_10.jpg  strand_2.jpg
$ ls [bn]*
berg_1.jpg  berg_2.jpg  notiz.txt
$ ls *_[12].jpg
berg_1.jpg  berg_2.jpg  strand_1.jpg  strand_2.jpg
$ ls strand_[!1]*
strand_2.jpg
```

`strand_?.jpg` trifft `strand_10.jpg` nicht, denn `10` sind zwei Zeichen; `strand_*.jpg` trifft es. `[bn]*` wählt alle Namen, die mit `b` oder `n` beginnen. `strand_[!1]*` verlangt nach `strand_` ein Zeichen, das keine 1 ist.
::::

::::beispiel [Zweites Beispiel] Sehen, was der Befehl bekommt
Weil `echo` seine Argumente nur wiederholt, zeigt es die Liste, die die Shell aus einem Muster gemacht hat:

```console
$ echo strand_?.jpg
strand_1.jpg strand_2.jpg
$ echo *.txt
notiz.txt
```

`echo` hat zwei Argumente bekommen, nicht das Muster. Auf dieselbe Weise lassen sich alle Bergfotos in ein eigenes Verzeichnis verschieben:

```console
$ mkdir berge
$ mv berg_*.jpg berge
$ ls -F
berge/  notiz.txt  strand_1.jpg  strand_10.jpg  strand_2.jpg
$ cd ~/linuxk3
```

`mv` hat drei Argumente bekommen, `berg_1.jpg`, `berg_2.jpg` und `berge`; das letzte ist ein Verzeichnis, also wandern die beiden Fotos hinein.
::::

⁠**Kurz gesagt:** Muster mit `*`, `?` und `[…]` wählen viele Namen auf einmal; die Shell ersetzt sie durch die passenden Namen, bevor der Befehl startet.

:::warnung Ein Leerzeichen zu viel
Wer alle Textdateien eines Verzeichnisses löschen will, tippt `rm *.txt`. Rutscht zwischen `*` und `.txt` ein Leerzeichen hinein, entstehen zwei Wörter: `*` trifft alle Namen im Verzeichnis, und `rm` löscht alle Dateien darunter, bevor es sich über eine fehlende Datei `.txt` beschwert. Probiere ein Muster deshalb erst mit `ls` oder `echo` aus; dann holst du die Zeile mit der Pfeiltaste zurück und ersetzt nur den Befehl durch `rm`.
:::

### Aufgaben zu Abschnitt [6](#stufe-6)

<span class="anker" id="stufe-6-7"></span>

:::aufgabe Aufgabe 18 ★ Kopieren oder verschieben?
<span class="anker" id="aufg-18"></span>

Im Arbeitsverzeichnis liegen die Datei `brief.txt` und das Verzeichnis `briefe`, aber keine Datei `brief2.txt`. Was bewirkt jede Zeile, und welche Namen gibt es danach? (a) `cp brief.txt brief2.txt` (b) `mv brief.txt briefe` (c) `mv briefe post` (d) `cp briefe kopie` (e) `cp -r briefe kopie`

:::loesung
Jede Zeile wird vom Anfangszustand aus betrachtet.

<ol class="al">

<li>

Es entsteht eine eigenständige Kopie `brief2.txt`; `brief.txt` bleibt.

</li>

<li>

`briefe` ist ein vorhandenes Verzeichnis, also wandert `brief.txt` hinein und heißt danach `briefe/brief.txt`; im Arbeitsverzeichnis gibt es keinen Eintrag `brief.txt` mehr.

</li>

<li>

`post` gibt es nicht, also wird `briefe` samt Inhalt in `post` umbenannt.

</li>

<li>

Nichts geschieht außer einer Meldung: Ohne `-r` lässt `cp` das Verzeichnis aus (`-r not specified; omitting directory 'briefe'`).

</li>

<li>

`kopie` gibt es nicht, also entsteht `kopie` als vollständige Kopie von `briefe`.

</li>

</ol>
:::
:::

:::aufgabe Aufgabe 19 ★★ Muster vorhersagen
<span class="anker" id="aufg-19"></span>

In einem Verzeichnis liegen `bild1.png`, `bild2.png`, `bild10.png`, `Bild3.png`, `bild_a.png` und `text.txt`. Welche Namen gibt `echo` aus bei (a) `bild?.png`, (b) `bild*.png`, (c) `[Bb]ild[0-9].png`, (d) `*[!0-9].png`? Prüfe in einem eigenen Verzeichnis `muster`, das du danach mit `rm -r` entfernst.

:::loesung
```console
$ mkdir muster
$ cd muster
$ touch bild1.png bild2.png bild10.png Bild3.png bild_a.png text.txt
$ echo bild?.png
bild1.png bild2.png
$ echo bild*.png
bild1.png bild10.png bild2.png bild_a.png
$ echo [Bb]ild[0-9].png
Bild3.png bild1.png bild2.png
$ echo *[!0-9].png
bild_a.png
$ cd ..
$ rm -r muster
```

(a) `?` verlangt genau ein Zeichen zwischen `bild` und `.png`: `bild10.png` hat dort zwei, `bild_a.png` ebenfalls, und `Bild3.png` beginnt mit großem `B`. (b) `*` lässt beliebig viele Zeichen zu; nur `Bild3.png` fällt wegen des großen `B` heraus. (c) Die erste Klammer lässt beide Schreibweisen zu, die zweite genau eine Ziffer; `bild10.png` hat zwei. Dass `Bild3.png` vorne steht, liegt an der Sortierung: Großbuchstaben kommen hier vor Kleinbuchstaben. (d) Verlangt wird ein Zeichen, das keine Ziffer ist, direkt vor `.png`; das trifft nur auf das `a` in `bild_a.png` zu.
:::
:::

:::aufgabe Aufgabe 20 ★★ Ein Bild mit falscher Endung
<span class="anker" id="aufg-20"></span>

Kopiere das Bild `/usr/share/pixmaps/ubuntu-logo-text.png` unter dem Namen `urlaub.txt` in dein Übungsverzeichnis. Was meldet `file urlaub.txt`? Was würde `cat urlaub.txt` anrichten, und warum? Lösche die Datei danach.

:::loesung
```console
$ cp /usr/share/pixmaps/ubuntu-logo-text.png urlaub.txt
$ file urlaub.txt
urlaub.txt: PNG image data, 187 x 72, 8-bit/color RGBA, non-interlaced
$ rm urlaub.txt
```

`file` erkennt das PNG-Bild an seinen ersten Bytes; die Endung `.txt` ist nur ein Teil des Namens und täuscht es nicht. `cat urlaub.txt` würde die Bytes des Bildes ins Terminal schreiben. Manche davon sind für das Terminal Steuerbefehle, und danach zeigt es womöglich nur noch Zeichensalat, bis man `reset` tippt (Warnung in Unterabschnitt [4.2](dateien-ansehen.html#stufe-4-2)).
:::
:::

:::aufgabe Aufgabe 21 ★★ Ein Name mit Leerzeichen
<span class="anker" id="aufg-21"></span>

Lege mit `touch` eine Datei `mein urlaub.txt` an. Wie zeigt `ls` sie an? Versuche dann `rm mein urlaub.txt` und erkläre beide Fehlermeldungen. Wie löschst du die Datei richtig? Finde zwei Schreibweisen.

:::loesung
```console
$ touch "mein urlaub.txt"
$ ls
 aktuell.txt   fotos              rezepte   verein
 einkauf.txt  'mein urlaub.txt'   urlaub    zettel.txt
$ rm mein urlaub.txt
rm: cannot remove 'mein': No such file or directory
rm: cannot remove 'urlaub.txt': No such file or directory
$ rm "mein urlaub.txt"
```

`ls` setzt den Namen in einfache Anführungszeichen, damit man das Leerzeichen sieht; die übrigen Namen rückt es um ein Zeichen ein, damit die Spalten bündig bleiben. Bei `rm mein urlaub.txt` zerlegt die Shell die Zeile in drei Wörter, und `rm` bekommt zwei Argumente, `mein` und `urlaub.txt`. Keine der beiden Dateien gibt es, daher zwei Meldungen; die gemeinte Datei bleibt unberührt. Richtig ist `rm "mein urlaub.txt"` oder `rm mein\ urlaub.txt`; die zweite Schreibweise erzeugt auch die Tabulatortaste.
:::
:::

:::aufgabe Aufgabe 22 ★★★ Ein Leerzeichen zu viel
<span class="anker" id="aufg-22"></span>

Jemand will den Inhalt von `~/projekt` löschen und tippt `rm -r ~/projekt /*` statt `rm -r ~/projekt/*`. Erkläre ohne es auszuführen, welche Argumente `rm` bekommt und was geschähe, wenn der Befehl als `root` liefe. Warum richtet er als gewöhnlicher Benutzer trotzdem Schaden an?

:::loesung
Die Shell ersetzt `~/projekt` durch `/home/student/projekt` und das Muster `/*` durch alle Einträge des Wurzelverzeichnisses: `/bin`, `/boot`, `/dev`, `/etc`, `/home` und so weiter. `rm -r` bekommt also das Projektverzeichnis selbst und dazu jedes Verzeichnis der obersten Ebene als Argument, nicht den Inhalt des Projekts. Als `root` löschte der Befehl das ganze System: Programme, Einstellungen, alle Heimatverzeichnisse, unter WSL 2 sogar die Dateien auf dem Windows-Laufwerk unter `/mnt/c`. Als gewöhnlicher Benutzer scheitert `rm` an den Systemverzeichnissen, aber nicht überall: Es löscht `~/projekt` ganz, und beim Argument `/home` steigt es in `/home/student` hinab, das dir gehört, und löscht den gesamten Inhalt deines Heimatverzeichnisses; nur das leere Verzeichnis selbst bleibt stehen, weil sein Eintrag in `/home` liegt, das du nicht verändern darfst. Unter WSL 2 kommt `/mnt` dazu, denn die Dateien unter `/mnt/c` darfst du in der Regel ebenfalls löschen. Ein einziges Leerzeichen macht aus „den Inhalt eines Verzeichnisses löschen“ also „fast alles löschen, was ich löschen darf“.
:::
:::

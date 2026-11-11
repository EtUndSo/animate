---
title: Expansion: Muster, Klammern und Tilde
pfad: Informatik / Linux und Kommandozeile / Wie die Shell eine Befehlszeile liest: Expansion, Quoting, Variablen, Umgebung
adresse: informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung
knoten: Kapitel 5: Wie die Shell eine Befehlszeile liest: Expansion, Quoting, Variablen, Umgebung
order: 6100200
summary: Kapitel 3 hat gezeigt, dass die Shell Muster wie .jpg und die Tilde durch Namen ersetzt, bevor ein Befehl startet.
tags: Expansion, Erweiterung, Pfadnamen-Erweiterung, Klammererweiterung, Tilde-Erweiterung
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
[Kapitel 3](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-verzeichnisse-und-pfade.html) hat gezeigt, dass die Shell Muster wie `*.jpg` und die Tilde durch Namen ersetzt, bevor ein Befehl startet. Dieser Abschnitt gibt diesem Schritt seinen Namen, die Expansion, und sieht sich die Ersetzungen genauer an: wie die Shell Muster auflöst, was mit versteckten Dateien und mit Mustern ohne Treffer geschieht, wie Klammern viele Wörter auf einmal erzeugen und wann die Tilde ersetzt wird.
:::

:::::vorwissen Was du dafür brauchst: Wörter, Muster und Prozesse

<span class="anker" id="stufe-1-1"></span>

Dieses Kapitel setzt die [Kapitel 1](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/ein-linux-zum-ueben.html) bis 4 voraus. Daraus brauchst du vor allem diese Dinge.

<ul>

<li>

Die Shell zerlegt eine Befehlszeile an Leerzeichen in Wörter. Das erste Wort ist der Befehl, die übrigen sind seine Argumente ([Kapitel 2, Abschnitt 2](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/der-aufbau-einer-befehlszeile.html#stufe-2)). Der eingebaute Befehl `echo` schreibt seine Argumente durch Leerzeichen getrennt in die Standardausgabe und zeigt deshalb, welche Argumente er bekommen hat.

</li>

<li>

Ein Muster ist ein Wort mit `*`, `?` oder `[…]`; die Shell ersetzt es vor dem Start des Befehls durch die passenden Dateinamen ([Kapitel 3, Abschnitt 6.6](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/kopieren-verschieben-loschen.html#stufe-6-6)). Namen, die mit einem Punkt beginnen, sind versteckte Dateien ([Kapitel 3, Abschnitt 3.2](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/den-inhalt-eines-verzeichnisses-anzeigen.html#stufe-3-2)). Die Tilde `~` am Anfang eines Worts steht für das Heimatverzeichnis ([Kapitel 3, Abschnitt 2.6](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/das-arbeitsverzeichnis-und-pfade.html#stufe-2-6)).

</li>

<li>

Einen Dateinamen mit Leerzeichen hält man mit Anführungszeichen oder mit einem umgekehrten Schrägstrich vor dem Leerzeichen zu einem Wort zusammen; die Shell entfernt die Anführungszeichen, bevor das Programm startet ([Kapitel 3, Abschnitt 3.7](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/den-inhalt-eines-verzeichnisses-anzeigen.html#stufe-3-7)).

</li>

<li>

Ein Prozess ist ein laufendes Programm mit eigenem Speicher; die Shell startet für jedes Programm einen neuen Prozess ([Kapitel 4, Abschnitt 1.2](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/prozesse-und-ihre-drei-strome.html#stufe-1-2)). `>` und `>>` leiten die Standardausgabe in eine Datei, `|` verbindet zwei Programme ([Kapitel 4, Abschnitte 2.1](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/ausgaben-umleiten.html#stufe-2-1), 2.2 und 4.1). `$?` liefert den Exit-Status des letzten Befehls; 127 heißt „Befehl nicht gefunden“ ([Kapitel 4, Abschnitte 5.1](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/der-exit-status.html#stufe-5-1) und [5.3](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/der-exit-status.html#stufe-5-3)).

</li>

</ul>

⁠**Kurz gesagt:** Du brauchst Befehl und Argumente, `echo`, Muster, versteckte Dateien und die Tilde, Anführungszeichen bei Dateinamen, den Prozess, Umleitung und Pipe sowie den Exit-Status.

:::warnung Nur im eigenen Übungsverzeichnis
Einige Befehle dieses Kapitels legen Dateien an oder löschen sie. Lege dir deshalb ein eigenes Übungsverzeichnis an und arbeite dort:

```console
$ mkdir ~/linuxk5
$ cd ~/linuxk5
```

Alle Dateinamen in den Beispielen beziehen sich auf dieses Verzeichnis.
:::

Lege darin die Dateien an, mit denen das Kapitel arbeitet: drei leere Fotodateien, eine leere Notiz, eine versteckte Datei und die Einkaufsliste aus [Kapitel 4](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/stroeme-umleitung-pipes-und-exit-status.html). Für die Liste tippst du nach `cat > einkauf.txt` die vier Zeilen `Milch`, `Brot`, `Äpfel`, `Kaffee` und zum Schluss Strg+D:

```console
$ touch notiz.txt foto1.jpg foto2.jpg foto10.jpg .einstellungen
$ cat > einkauf.txt
Milch
Brot
Äpfel
Kaffee
$ ls -A
.einstellungen  einkauf.txt  foto1.jpg  foto10.jpg  foto2.jpg  notiz.txt
```

:::::

### Die Expansion

<span class="anker" id="stufe-1-2"></span>

Muster und Tilde haben etwas gemeinsam: Was du tippst, ist nicht das, was das Programm bekommt. Die Shell schreibt die Zeile vorher um. Das tut sie nicht nur mit Mustern und der Tilde, sondern mit einer ganzen Reihe von Zeichen, und sie tut es immer im selben Schritt.

[Kapitel 2](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/die-shell-erste-befehle.html) hat die Shell mit einer Bedienung im Restaurant verglichen. Im selben Bild zur Orientierung: Du schreibst eine Bestellung mit Abkürzungen auf, etwa „2× Tagesgericht“. Bevor der Zettel in die Küche geht, schreibt die Bedienung jede Abkürzung aus. Die Küche bekommt nur den ausgeschriebenen Zettel und erfährt nie, wie die Bestellung ursprünglich aussah. Abbildung [1](#abb-1) zeigt dasselbe für eine Befehlszeile.

:::abbildung linux/k5expansion 1
Die Expansion von `ls *.txt`: Die Shell zerlegt die Zeile in die Wörter `ls` und `*.txt`, ersetzt das Muster durch die passenden Namen `einkauf.txt` und `notiz.txt` und startet erst dann `ls` mit diesen beiden Argumenten. Das Programm sieht das Muster nie.
:::

:::definition Definition 1.1 (Expansion)
<span class="anker" id="satz-1-1"></span>

Die __Expansion__ ist der Schritt, in dem die Shell bestimmte Teile der Wörter einer Befehlszeile durch anderen Text ersetzt. Sie geschieht, nachdem die Shell die Zeile in Wörter zerlegt hat, und bevor sie den Befehl ausführt; das Programm bekommt nur das Ergebnis als Argumente.
:::

Die Expansion umfasst mehrere Arten der Ersetzung. Jede dieser Arten heißt eine __Erweiterung__; jede „…erweiterung“ in diesem Kapitel ist also eine Art der Expansion. Das Ersetzen eines Musters ist eine Erweiterung, das Ersetzen der Tilde eine andere; dieses Kapitel lernt weitere kennen. Am Ergebnis einer Expansion kannst du nicht erkennen, was ursprünglich getippt war.

::::beispiel Muster oder Namen, das Programm merkt keinen Unterschied
```console
$ echo *.txt
einkauf.txt notiz.txt
$ ls *.txt
einkauf.txt  notiz.txt
$ ls einkauf.txt notiz.txt
einkauf.txt  notiz.txt
```

`echo` zeigt, was aus dem Muster geworden ist: zwei Namen. `ls` bekommt in der zweiten und in der dritten Zeile genau dieselben zwei Argumente; ob du das Muster oder die Namen getippt hast, kann es nicht wissen.
::::

⁠**Kurz gesagt:** Bei der Expansion schreibt die Shell Teile der Befehlszeile um, bevor das Programm startet; das Programm sieht nur das Ergebnis.

:::hintergrund Warum löst die Shell Muster auf und nicht jedes Programm selbst?
Schon in den ersten Unix-Systemen lösten nicht die einzelnen Programme Muster auf. In der sechsten Ausgabe des Unix-Handbuchs von 1975 gibt es dafür ein eigenes Hilfsprogramm namens `glob`: Die damalige Shell rief es auf, sobald ein Argument `*`, `?` oder `[` enthielt; es ersetzte die Muster durch die passenden Namen und startete dann den eigentlichen Befehl. Später wanderte diese Arbeit in die Shell selbst. Der alte Name lebt im Englischen weiter: Muster heißen dort oft „Globs“.

Unter Windows ist es anders. Dort bekommt ein Programm die getippte Zeile als Ganzes und entscheidet selbst, ob es `*.txt` als Muster deutet. Programme, die in der Sprache C mit den Werkzeugen von Microsoft gebaut werden, tun das von sich aus nicht; man muss es beim Bauen eigens einschalten. Ob ein Muster wirkt, hängt dort also vom einzelnen Programm ab.

Eine eigene Herleitung, die so nicht in den Handbüchern steht, erklärt den Vorteil der Unix-Lösung: Weil eine einzige Stelle die Muster auflöst, verhalten sie sich in jedem Programm gleich, und kein Programm muss dafür eine Zeile Code enthalten. Der Preis ist, dass ein Programm das Muster selbst nie zu sehen bekommt. Will ein Programm wie `find` ein Muster selbst auswerten, muss man es vor der Shell schützen, wie bei `find -name "*.txt"` in [Kapitel 3, Abschnitt 10.2](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-finden-und-platz-messen.html#stufe-10-2).
:::

### Die Pfadnamen-Erweiterung

<span class="anker" id="stufe-1-3"></span>

In [Kapitel 3](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-verzeichnisse-und-pfade.html) standen Muster meist allein und bezogen sich auf das Arbeitsverzeichnis. Ein Muster darf aber auch Teil eines Pfads sein, und die Treffer kommen in einer festen Reihenfolge. Beides lohnt einen genaueren Blick.

:::definition Definition 1.2 (Pfadnamen-Erweiterung)
<span class="anker" id="satz-1-2"></span>

Die __Pfadnamen-Erweiterung__ ist die Erweiterung, die ein Muster durch die Namen der vorhandenen Dateien und Verzeichnisse ersetzt, auf die es passt; jeder Treffer wird ein eigenes Wort. Die Treffer stehen sortiert da. Enthält das Muster Schrägstriche, prüft die Shell jeden Teil des Pfads für sich; ein Schrägstrich muss im Muster selbst stehen, denn `*`, `?` und `[…]` stehen nie für ihn.
:::

Sortiert wird nach der Spracheinstellung. Auf dem Testsystem dieses Kapitels vergleicht sie die Namen Zeichen für Zeichen nach den Nummern der Zeichen, wie bei der Einkaufsliste in [Kapitel 4, Abschnitt 2.7](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/ausgaben-umleiten.html#stufe-2-7). Deshalb steht `foto10.jpg` vor `foto2.jpg`: Beide Namen beginnen mit `foto`, danach entscheidet das nächste Zeichen, und die Ziffer `1` hat eine kleinere Nummer als die `2`. `foto1.jpg` steht noch davor, weil der Punkt eine kleinere Nummer hat als jede Ziffer.

::::beispiel Treffer im Arbeitsverzeichnis und in /etc
```console
$ echo *.jpg
foto1.jpg foto10.jpg foto2.jpg
$ echo foto?.jpg
foto1.jpg foto2.jpg
$ echo foto[12].jpg
foto1.jpg foto2.jpg
$ echo /etc/host*
/etc/host.conf /etc/hostname /etc/hosts
```

Das letzte Muster bezieht sich auf das Verzeichnis `/etc`: Der Teil `/etc` enthält kein Musterzeichen und bleibt, wie er ist; nur `host*` wird mit den Namen in `/etc` verglichen. Die Treffer kommen mit dem vollen Pfad zurück, so wie das Muster geschrieben war.
::::

⁠**Kurz gesagt:** Die Pfadnamen-Erweiterung ersetzt ein Muster durch die sortierten Namen, die darauf passen, auch in Pfaden; für einen Schrägstrich steht kein Musterzeichen.

### Versteckte Dateien und Muster

<span class="anker" id="stufe-1-4"></span>

Mit `rm *` löscht man alle Dateien eines Verzeichnisses, aber nicht alle: Versteckte Dateien enthalten oft Einstellungen, und es wäre ärgerlich, wenn jedes Muster sie mitnähme. [Kapitel 3](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-verzeichnisse-und-pfade.html) hat die Regel dafür in einem Satz genannt; Abbildung [2](#abb-2) zeigt sie an den Dateien des Übungsverzeichnisses.

:::abbildung linux/k5versteckt 2
Zwei Muster auf dieselben Namen gelegt. `*` passt auf alle sichtbaren Namen, `.einstellungen` bleibt grau. `.*` passt nur auf `.einstellungen`; die Einträge `.` und `..` hätten zwar die Form, werden aber übersprungen.
:::

:::satz Satz 1.3 (Versteckte Dateien in Mustern)
<span class="anker" id="satz-1-3"></span>

Ein Name, der mit einem Punkt beginnt, passt auf ein Muster nur, wenn das Muster an dieser Stelle selbst einen Punkt hat, also an seinem Anfang oder direkt nach einem Schrägstrich. Die Einträge `.` und `..` liefert bash in der Voreinstellung nie als Treffer.
:::

::::beispiel Sichtbare und versteckte Treffer
```console
$ echo *
einkauf.txt foto1.jpg foto10.jpg foto2.jpg notiz.txt
$ echo .*
.einstellungen
```

`*` erfasst alles außer `.einstellungen`. `.*` erfasst nur die versteckte Datei, obwohl auch `.` und `..` mit einem Punkt beginnen.
::::

⁠**Kurz gesagt:** Versteckte Dateien erfasst ein Muster nur, wenn es an dieser Stelle selbst einen Punkt hat; `.` und `..` gehören nie zu den Treffern.

:::hintergrund Was früher bei .* geschah
Dass `.` und `..` nicht auf `.*` passen, regelt in bash die Einstellung `globskipdots`, die seit der Version 5.2 von 2022 eingeschaltet ist. Ältere Fassungen von bash und manche anderen Shells liefern die beiden Einträge mit. Ein Befehl, der ganze Verzeichnisse bearbeitet, bekäme dann mit `..` auch das übergeordnete Verzeichnis als Argument und arbeitete womöglich weit über das gemeinte Verzeichnis hinaus. Wer versteckte Dateien auch auf älteren Systemen sicher erfassen will, schreibt `.[!.]*`: ein Punkt, danach ein Zeichen, das kein Punkt ist, danach beliebig viel; nur Namen, die mit zwei Punkten beginnen, entgehen ihm. Umgekehrt lässt sich bash mit `shopt -s dotglob` dazu bringen, versteckte Dateien auch bei `*` mitzunehmen; `shopt -u dotglob` schaltet das wieder aus. Die Einstellung gilt nur für die laufende Sitzung.
:::

### Ein Muster ohne Treffer

<span class="anker" id="stufe-1-5"></span>

Was geschieht, wenn ein Muster auf keinen einzigen Namen passt? Man könnte erwarten, dass es dann einfach verschwindet. Die Shell macht es anders, wie Abbildung [3](#abb-3) zeigt.

:::abbildung linux/k5ohnetreffer 3
`rm *.bak` in einem Verzeichnis ohne passende Datei. Die Shell vergleicht das Muster mit allen Namen, findet keinen Treffer und lässt das Wort unverändert. `rm` bekommt den Text `*.bak` als Argument, sucht eine Datei mit genau diesem Namen und meldet, dass es sie nicht gibt.
:::

:::satz Satz 1.4 (Muster ohne Treffer)
<span class="anker" id="satz-1-4"></span>

Passt ein Muster auf keinen Namen, lässt die Shell das Wort unverändert stehen. Das Programm bekommt das Muster dann als gewöhnlichen Text.
:::

::::beispiel Kein PDF, keine Sicherungskopie
```console
$ echo *.pdf
*.pdf
$ ls *.pdf
ls: cannot access '*.pdf': No such file or directory
$ rm *.bak
rm: cannot remove '*.bak': No such file or directory
```

Die Meldungen von `ls` und `rm` nennen das Muster selbst. Das beweist, dass beide Programme den Text `*.pdf` beziehungsweise `*.bak` bekommen haben und eine Datei mit genau diesem Namen gesucht haben.
::::

⁠**Kurz gesagt:** Ohne Treffer bleibt ein Muster stehen, wie es getippt wurde, und das Programm bekommt es wörtlich.

:::hintergrund Ein Muster ohne Treffer verschwinden lassen
Die Regel stammt aus dem Standard für Unix-Shells; bash und dash halten sich daran. Die Shell zsh, die unter anderem Kali Linux und macOS voreinstellen, meldet dagegen ohne Treffer von sich aus einen Fehler und startet den Befehl nicht. bash bietet zwei Einstellungen, die sie ändern. Mit `nullglob` verschwindet ein Muster ohne Treffer ganz, mit `failglob` meldet die Shell den Fehler selbst und startet den Befehl gar nicht. `shopt -s` schaltet eine Einstellung ein, `shopt -u` wieder aus:

```console
$ shopt -s nullglob
$ echo Treffer: *.pdf
Treffer:
$ shopt -u nullglob
$ shopt -s failglob
$ echo Treffer: *.pdf
bash: no match: *.pdf
$ shopt -u failglob
```

Mit `nullglob` bekam `echo` nur noch das Wort `Treffer:`. Mit `failglob` kam die Meldung von bash selbst; `echo` ist gar nicht gelaufen. Beide Einstellungen gelten nur für die laufende Sitzung. Im Alltag an der Befehlszeile lässt man sie meist aus; mit `nullglob` etwa würde `ls *.pdf` ohne Treffer zu `ls` ohne Argument und zeigte das ganze Verzeichnis.
:::

### Die Klammererweiterung

<span class="anker" id="stufe-1-6"></span>

Ein Muster findet nur Namen, die es schon gibt. Oft braucht man aber neue Namen nach einem Schema: zwölf Verzeichnisse für zwölf Monate, eine Datei für jeden Wochentag, dieselben Unterverzeichnisse für zwei Jahre. Dafür gibt es eine Erweiterung, die Wörter ganz ohne Blick auf die Dateien erzeugt. Als Bild zur Orientierung: Sie arbeitet wie eine Speisekarte, auf der jedes Gericht mit jeder Beilage kombiniert werden darf; Abbildung [4](#abb-4) zeigt das an zwei Klammern.

:::abbildung linux/k5klammer 4
Die Klammererweiterung von `urlaub/{2025,2026}/{sommer,winter}`: Jedes Element der ersten Klammer wird mit jedem der zweiten verbunden, in der Reihenfolge, in der sie geschrieben sind. Aus einem Wort werden $2 \cdot 2 = 4$ Wörter. Kein Verzeichnis muss dafür existieren.
:::

:::definition Definition 1.5 (Klammererweiterung)
<span class="anker" id="satz-1-5"></span>

Die __Klammererweiterung__ macht aus einem Wort mit geschweiften Klammern mehrere Wörter. In den Klammern steht entweder eine Liste mit Kommas, `{a,b,c}`, oder eine Folge `{x..y}` beziehungsweise `{x..y..s}` von ganzen Zahlen oder einzelnen Buchstaben, mit der Schrittweite $s$. Jedes Element der Liste oder Folge ergibt ein Wort; was im Wort vor der Klammer steht, kommt vor jedes Element, was danach steht, hinter jedes. Die Wörter stehen in der geschriebenen Reihenfolge da, nicht sortiert.
:::

Die Klammererweiterung ersetzt nur Text und sieht nicht nach, ob es Dateien dieses Namens gibt. Beginnt eine Zahl der Folge mit einer Null, bekommen alle Zahlen dieselbe Stellenzahl. Steht in den Klammern weder ein Komma noch eine gültige Folge, bleibt das Wort, wie es ist. Mehrere Klammern in einem Wort werden miteinander kombiniert.

::::beispiel Listen und Folgen
```console
$ echo foto{1,2,3}.jpg
foto1.jpg foto2.jpg foto3.jpg
$ echo {1..5} {a..e}
1 2 3 4 5 a b c d e
$ echo {01..12}
01 02 03 04 05 06 07 08 09 10 11 12
$ echo {0..20..5}
0 5 10 15 20
$ echo {a}
{a}
```

`foto3.jpg` gibt es nicht, und trotzdem steht der Name da. `{01..12}` schreibt jede Zahl zweistellig, weil die erste mit einer Null beginnt. `{a}` enthält weder Komma noch Folge und bleibt stehen.
::::

Im Übungsverzeichnis entsteht so mit einer Zeile ein kleiner Verzeichnisbaum für Urlaubsfotos, den das Kapitel weiter benutzt. Danach findet ein Muster mit zwei Musterteilen alle vier Unterverzeichnisse:

```console
$ mkdir -p urlaub/{2025,2026}/{sommer,winter}
$ echo urlaub/*/*
urlaub/2025/sommer urlaub/2025/winter urlaub/2026/sommer urlaub/2026/winter
```

`mkdir` hat die vier Pfade aus Abbildung [4](#abb-4) als Argumente bekommen; `-p` legt fehlende übergeordnete Verzeichnisse mit an ([Kapitel 3, Abschnitt 5.1](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-und-verzeichnisse-anlegen.html#stufe-5-1)). Im Muster `urlaub/*/*` prüft die Shell jeden Pfadteil für sich: Das erste `*` passt auf `2025` und `2026`, das zweite in jedem davon auf `sommer` und `winter`. Abbildung [5](#abb-5) zeigt diesen Gang durch die Ebenen.

:::abbildung linux/k5pfadmuster 5
Die Pfadnamen-Erweiterung von `urlaub/*/*`, Ebene für Ebene. Der Teil `urlaub` enthält kein Musterzeichen und bleibt. Das erste `*` wird mit den Namen in `urlaub` verglichen und trifft `2025` und `2026`; das zweite `*` wird in jedem dieser Verzeichnisse verglichen und trifft je `sommer` und `winter`. Heraus kommen vier Pfade, sortiert.
:::

::::beispiel [Gegenbeispiel] Klammern sind kein Muster
```console
$ ls foto[123].jpg
foto1.jpg  foto2.jpg
$ ls foto{1,2,3}.jpg
ls: cannot access 'foto3.jpg': No such file or directory
foto1.jpg  foto2.jpg
```

Das Muster `foto[123].jpg` liefert nur die zwei vorhandenen Namen. Die Klammern erzeugen alle drei Namen, und `ls` meldet den fehlenden.
::::

⁠**Kurz gesagt:** Die Klammererweiterung erzeugt aus einer Liste oder Folge in geschweiften Klammern mehrere Wörter, in der geschriebenen Reihenfolge und ohne nach Dateien zu sehen.

### Die Tilde-Erweiterung

<span class="anker" id="stufe-1-7"></span>

Die Tilde kennst du aus [Kapitel 3, Abschnitt 2.6](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/das-arbeitsverzeichnis-und-pfade.html#stufe-2-6). Auch sie ist eine Erweiterung, und mit diesem Wissen lassen sich ihre Regeln genauer fassen.

:::definition Definition 1.6 (Tilde-Erweiterung)
<span class="anker" id="satz-1-6"></span>

Die __Tilde-Erweiterung__ ersetzt eine Tilde am Anfang eines Worts. Ausgewertet wird alles von der Tilde bis zum ersten Schrägstrich oder bis zum Ende des Worts: Folgt auf die Tilde nichts, setzt die Shell den Pfad deines Heimatverzeichnisses ein, folgt ein Benutzername, den Pfad des Heimatverzeichnisses dieses Benutzers. Gibt es keinen solchen Benutzer, bleibt der Text unverändert; eine Tilde mitten im Wort bleibt in aller Regel ebenfalls stehen.
:::

::::beispiel Wo die Tilde ersetzt wird
```console
$ echo ~ ~/linuxk5 ~root
/home/student /home/student/linuxk5 /root
$ echo a~ ~gibtsnicht
a~ ~gibtsnicht
```

Bei `~/linuxk5` endet der ausgewertete Teil am Schrägstrich, der Rest bleibt angehängt. Bei `a~` steht die Tilde nicht am Wortanfang, und einen Benutzer `gibtsnicht` gibt es auf dem Testsystem nicht.
::::

⁠**Kurz gesagt:** Die Tilde-Erweiterung ersetzt eine Tilde am Wortanfang durch ein Heimatverzeichnis, das eigene oder das des genannten Benutzers.

### Aufgaben zu Abschnitt [1](#stufe-1)

<span class="anker" id="stufe-1-8"></span>

:::aufgabe Aufgabe 1 ★ Was bekommt echo?
<span class="anker" id="aufg-1"></span>

Sage für dein Übungsverzeichnis voraus, was diese Befehle ausgeben, und prüfe es danach: (a) `echo *.txt` (b) `echo foto*` (c) `echo f*.txt` (d) `echo *.gibts` (e) `echo .*` (f) `echo ~`.

:::loesung
```console
$ echo *.txt
einkauf.txt notiz.txt
$ echo foto*
foto1.jpg foto10.jpg foto2.jpg
$ echo f*.txt
f*.txt
$ echo *.gibts
*.gibts
$ echo .*
.einstellungen
$ echo ~
/home/student
```

(a) Die beiden Textdateien, sortiert. (b) Alle drei Fotos; `foto10.jpg` steht vor `foto2.jpg`, weil Zeichen für Zeichen verglichen wird und die `1` vor der `2` kommt. (c) Kein Name beginnt mit `f` und endet auf `.txt`; die Fotos enden auf `.jpg`. Ohne Treffer bleibt das Muster stehen. (d) Ebenso. (e) Nur die versteckte Datei, denn `.` und `..` liefert bash nicht als Treffer. (f) Die Tilde allein wird zum Heimatverzeichnis. In allen Fällen hat `echo` nur die fertigen Wörter bekommen.
:::
:::

:::aufgabe Aufgabe 2 ★ Klammern zählen
<span class="anker" id="aufg-2"></span>

(a) Wie viele Wörter erzeugt `echo {a,b,c}{1..4}`, und in welcher Reihenfolge stehen sie? (b) Was gibt `echo {1..3}{a,b}` aus? (c) Lege in deinem Übungsverzeichnis mit einer einzigen Zeile die zwölf Verzeichnisse `monat01` bis `monat12` an und prüfe das Ergebnis mit einem Muster.

:::loesung
```console
$ echo {a,b,c}{1..4}
a1 a2 a3 a4 b1 b2 b3 b4 c1 c2 c3 c4
$ echo {1..3}{a,b}
1a 1b 2a 2b 3a 3b
$ mkdir monat{01..12}
$ echo monat*
monat01 monat02 monat03 monat04 monat05 monat06 monat07 monat08 monat09 monat10 monat11 monat12
```

(a) Jedes der drei Elemente der ersten Klammer wird mit jedem der vier der zweiten verbunden, also $3 \cdot 4 = 12$ Wörter. Die Reihenfolge folgt der Schreibweise: Die erste Klammer ändert sich am langsamsten. (b) Dieselbe Regel mit $3 \cdot 2 = 6$ Wörtern. (c) `{01..12}` schreibt alle Zahlen zweistellig, weil die erste mit einer Null beginnt; `mkdir` bekommt zwölf Namen. Das Muster `monat*` findet sie wieder. Zweistellige Nummern haben einen Vorteil: Sortiert stehen die Monate in der richtigen Reihenfolge, `monat10` nach `monat09`.
:::
:::

:::aufgabe Aufgabe 3 ★★ Erst Klammern, dann Muster
<span class="anker" id="aufg-3"></span>

Sage voraus, was (a) `echo foto{10,2,1}.jpg` und (b) `echo foto{10,2,1}*` in deinem Übungsverzeichnis ausgeben, und prüfe es. Erkläre die Reihenfolge der Namen und warum in (b) ein Name zweimal vorkommt.

:::loesung
```console
$ echo foto{10,2,1}.jpg
foto10.jpg foto2.jpg foto1.jpg
$ echo foto{10,2,1}*
foto10.jpg foto2.jpg foto1.jpg foto10.jpg
```

(a) Die Klammererweiterung erzeugt drei Wörter in der geschriebenen Reihenfolge: `foto10.jpg`, `foto2.jpg`, `foto1.jpg`. Keines enthält ein Musterzeichen, also sortiert niemand etwas. (b) Hier erzeugt die Klammererweiterung zuerst die drei Muster `foto10*`, `foto2*` und `foto1*`. Danach ersetzt die Pfadnamen-Erweiterung jedes Muster für sich durch seine Treffer: `foto10*` passt auf `foto10.jpg`, `foto2*` auf `foto2.jpg`, `foto1*` auf `foto1.jpg` und `foto10.jpg`. Sortiert wird nur innerhalb der Treffer eines Musters, nicht über alle Wörter hinweg; deshalb erscheint `foto10.jpg` zweimal.
:::
:::

:::aufgabe Aufgabe 4 ★★ Was übrig bleibt
<span class="anker" id="aufg-4"></span>

Lege ein Unterverzeichnis `probe` mit den Dateien `a.txt` und `.b` an: `mkdir probe` und `touch probe/a.txt probe/.b`. (a) Sage voraus, welche Datei nach `rm probe/*` noch da ist, und prüfe es mit `ls -A probe`. (b) Was gibt danach `echo probe/*` aus, und warum?

:::loesung
```console
$ mkdir probe
$ touch probe/a.txt probe/.b
$ rm probe/*
$ ls -A probe
.b
$ echo probe/*
probe/*
```

(a) `probe/*` passt nur auf `probe/a.txt`. Der Name `.b` beginnt direkt nach dem Schrägstrich mit einem Punkt, und an dieser Stelle steht im Muster kein Punkt; `rm` bekommt ihn deshalb gar nicht als Argument, und die versteckte Datei bleibt. (b) Danach gibt es in `probe` keinen sichtbaren Namen mehr. Das Muster hat keinen Treffer und bleibt unverändert stehen; `echo` schreibt es wörtlich.
:::
:::

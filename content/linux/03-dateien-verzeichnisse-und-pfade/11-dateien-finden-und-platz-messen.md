---
title: Dateien finden und Platz messen
pfad: Informatik / Linux und Kommandozeile / Dateien, Verzeichnisse und Pfade
adresse: informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade
knoten: Kapitel 3: Dateien, Verzeichnisse und Pfade
order: 6081100
summary: Irgendwann weiß man nicht mehr, wo eine Datei liegt, oder der Platz wird knapp, und man sucht, was ihn belegt.
tags: find, -name muster, -type art, -size n, -mtime n, !, -maxdepth n, Aktion
lang: de
---

<span class="anker" id="stufe-10"></span>

:::zweck
Irgendwann weiß man nicht mehr, wo eine Datei liegt, oder der Platz wird knapp, und man sucht, was ihn belegt. Dieser Abschnitt zeigt `find`, das einen Teilbaum nach Namen, Art, Größe und Alter durchsucht, und `du`, das den belegten Platz zusammenzählt.
:::

### Suchen mit find

<span class="anker" id="stufe-10-1"></span>

`ls` zeigt, was in einem Verzeichnis liegt; `ls -R` und `tree` zeigen ganze Teilbäume. Wer aber nur bestimmte Dateien sucht, will nicht Tausende Zeilen lesen, sondern eine Auswahl.

:::abbildung linux/k3find 37
Wie `find` arbeitet: Es betritt das Startverzeichnis und geht jeden Eintrag durch, steigt in jedes Unterverzeichnis hinab und kehrt danach zurück. An jedem Eintrag prüft es die Bedingungen; was sie erfüllt, wird ausgegeben.
:::

:::definition Definition 10.1 (find)
<span class="anker" id="satz-10-1"></span>

Der Befehl __find__ durchläuft den Teilbaum unterhalb jedes genannten Startverzeichnisses, Eintrag für Eintrag und Ebene für Ebene. Für jeden Eintrag prüft er die Bedingungen, die nach den Startverzeichnissen folgen, die sogenannten Tests, und gibt den Pfad aller Einträge aus, die alle Tests bestehen. Ohne Tests gibt er jeden Eintrag aus.
:::

Die Pfade beginnen mit dem Startverzeichnis, so wie man es getippt hat. Die Reihenfolge ist die, in der die Einträge in den Verzeichnissen stehen; sortiert ist sie nicht. Abbildung [37](#abb-37) zeigt den Weg durch den Baum.

::::beispiel Alles unter rezepte
```console
$ find rezepte
rezepte
rezepte/kuchen
rezepte/kuchen/apfelkuchen.txt
rezepte/kuchen/kaesekuchen.txt
rezepte/zettel.txt
rezepte/suppen
rezepte/suppen/kuerbissuppe.txt
```

`find` beginnt mit dem Startverzeichnis selbst, steigt in `kuchen` hinab, kehrt zurück, nimmt den Link `zettel.txt` mit und steigt in `suppen` hinab.
::::

⁠**Kurz gesagt:** `find start tests` durchläuft einen Teilbaum und gibt die Pfade der Einträge aus, die alle Tests bestehen.

### Nach Namen suchen: -name

<span class="anker" id="stufe-10-2"></span>

Meist erinnert man sich an einen Teil des Namens: Die Datei endete auf `.txt`, oder irgendwo kam „strand“ vor. Dafür gibt es einen Test, der Muster versteht.

:::abbildung linux/k3quoting 38
Zwei Wege, dasselbe Muster zu tippen. Ohne Anführungszeichen ersetzt die Shell `*.txt` schon vor dem Start durch die passenden Namen im Arbeitsverzeichnis, und `find` bekommt eine falsche Bedingung. Mit Anführungszeichen erreicht das Muster `find` unverändert, und `find` legt es an jeden Namen im ganzen Teilbaum.
:::

:::definition Definition 10.2 (-name, -iname)
<span class="anker" id="satz-10-2"></span>

Der Test __-name muster__ besteht, wenn der Name eines Eintrags, also der letzte Teil seines Pfads, auf das Muster passt; das Muster folgt denselben Regeln wie in Unterabschnitt [6.6](kopieren-verschieben-loschen.html#stufe-6-6). Der Test `-iname` tut dasselbe, unterscheidet aber Groß- und Kleinbuchstaben nicht.
:::

Hier wendet nicht die Shell das Muster an, sondern `find`, und zwar auf jeden Namen im durchlaufenen Teilbaum. Damit das Muster bei `find` ankommt, muss man es in Anführungszeichen setzen; sonst ersetzt die Shell es schon vorher durch Namen aus dem Arbeitsverzeichnis, wie Abbildung [38](#abb-38) zeigt.

::::beispiel Alle Textdateien, alle Strandfotos
```console
$ find . -name "*.txt"
./aktuell.txt
./zettel.txt
./rezepte/kuchen/apfelkuchen.txt
./rezepte/kuchen/kaesekuchen.txt
./rezepte/zettel.txt
./rezepte/suppen/kuerbissuppe.txt
./fotos/urlaub/2026/notiz.txt
./einkauf.txt
$ find . -iname "STRAND*"
./fotos/urlaub/2026/strand_10.jpg
./fotos/urlaub/2026/strand_1.jpg
./fotos/urlaub/2026/strand_2.jpg
```

Das Startverzeichnis `.` ist das Arbeitsverzeichnis `~/linuxk3`. Gefunden werden auch die Links `aktuell.txt` und `zettel.txt`, denn `-name` prüft nur den Namen, nicht die Art. `-iname` findet die Strandfotos, obwohl das Muster in Großbuchstaben getippt ist.
::::

::::beispiel [Gegenbeispiel] Das Muster ohne Anführungszeichen
```console
$ find . -name *.txt
find: paths must precede expression: `einkauf.txt'
find: possible unquoted pattern after predicate `-name'?
```

Im Arbeitsverzeichnis liegen drei Namen auf `.txt`: `aktuell.txt`, `einkauf.txt` und `zettel.txt`. Die Shell hat das Muster durch diese drei ersetzt, und `find` bekam `-name aktuell.txt einkauf.txt zettel.txt`. Mit dem überzähligen `einkauf.txt` weiß es nichts anzufangen, und es vermutet sogar richtig, dass ein Muster ohne Anführungszeichen schuld ist.
::::

⁠**Kurz gesagt:** `-name "muster"` sucht nach Namen; die Anführungszeichen sorgen dafür, dass `find` und nicht die Shell das Muster anwendet.

### Nach Art suchen: -type

<span class="anker" id="stufe-10-3"></span>

Manchmal sucht man keine bestimmte Datei, sondern alle Verzeichnisse eines Teilbaums oder alle symbolischen Links, etwa um verwaiste zu finden.

:::definition Definition 10.3 (-type)
<span class="anker" id="satz-10-3"></span>

Der Test __-type art__ besteht, wenn ein Eintrag von der genannten Art ist: `f` für eine gewöhnliche Datei, `d` für ein Verzeichnis, `l` für einen symbolischen Link, `b` und `c` für Gerätedateien.
:::

Die Buchstaben entsprechen denen in der ersten Spalte von `ls -l`, nur steht `f` statt `-` für die gewöhnliche Datei.

::::beispiel Verzeichnisse und Links der Spielwiese
```console
$ find . -type d
.
./rezepte
./rezepte/kuchen
./rezepte/suppen
./fotos
./fotos/urlaub
./fotos/urlaub/2026
./fotos/urlaub/2026/berge
$ find . -type l
./aktuell.txt
./zettel.txt
./rezepte/zettel.txt
./urlaub
```

Acht Verzeichnisse, das Startverzeichnis eingeschlossen, und vier symbolische Links. Der Link `urlaub` zeigt auf ein Verzeichnis, wird aber als Link gezählt; `find` folgt symbolischen Links nicht, sondern betrachtet sie selbst.
::::

⁠**Kurz gesagt:** `-type f`, `-type d` und `-type l` wählen gewöhnliche Dateien, Verzeichnisse oder symbolische Links.

### Nach Größe suchen: -size

<span class="anker" id="stufe-10-4"></span>

Wird der Platz knapp, sucht man die großen Brocken. Umgekehrt helfen leere Dateien, vergessene Platzhalter aufzuspüren.

:::abbildung linux/k3findsize 39
Wie `-size` rundet: Dateien von 0, 32, 1024 und 1025 Bytes auf einem Zahlenstrahl, darüber ihre Größe in ganzen KiB, aufgerundet. `-size -1k` verlangt weniger als 1 und trifft nur die leere Datei; `-size -2k` trifft alle bis 1024 Bytes.
:::

:::definition Definition 10.4 (-size)
<span class="anker" id="satz-10-4"></span>

Der Test __-size n__ vergleicht die Größe eines Eintrags mit `n`; `+n` heißt größer als `n`, `-n` kleiner als `n`, `n` allein genau `n`. Ein Buchstabe hinter der Zahl nennt die Einheit: `c` für Bytes, `k` für 1024 Byte, `M` für $1024^2$, `G` für $1024^3$; ohne Buchstaben gilt die alte Einheit von 512 Byte. Vor dem Vergleich rundet `find` die Größe auf ganze Einheiten auf.
:::

Das Aufrunden ist eine Falle. Eine Datei mit 32 Bytes zählt als 1 KiB, weil sie angebrochen ist. `-size -1k` verlangt „weniger als 1 KiB“ und trifft deshalb nur leere Dateien, nicht etwa alle Dateien unter 1024 Bytes. Abbildung [39](#abb-39) zeigt die Rundung am Zahlenstrahl.

::::beispiel Große Programme und leere Dateien
```console
$ find /usr/bin -size +10M
/usr/bin/shellcheck
/usr/bin/x86_64-linux-gnu-lto-dump-15
/usr/bin/coreutils
/usr/bin/snap
/usr/bin/gdb
$ find . -type f -size 0
./.einstellungen
./fotos/urlaub/2026/strand_10.jpg
./fotos/urlaub/2026/strand_1.jpg
./fotos/urlaub/2026/strand_2.jpg
./fotos/urlaub/2026/berge/berg_2.jpg
./fotos/urlaub/2026/berge/berg_1.jpg
./fotos/urlaub/2026/notiz.txt
```

Auf dem Testrechner sind fünf Programme größer als 10 MiB, darunter `coreutils`, das Multicall-Programm von uutils aus [Kapitel 2, Abschnitt 7.2](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/zwei-fassungen-der-grundbefehle-gnu-und-uutils.html#stufe-7-2). Leer sind die Platzhalter für die Fotos und die versteckte Einstellungsdatei; `find` zeigt versteckte Einträge immer mit.
::::

::::beispiel [Zweites Beispiel] Die Rundungsfalle
```console
$ find . -type f -size -1k
./.einstellungen
./fotos/urlaub/2026/strand_10.jpg
./fotos/urlaub/2026/strand_1.jpg
./fotos/urlaub/2026/strand_2.jpg
./fotos/urlaub/2026/berge/berg_2.jpg
./fotos/urlaub/2026/berge/berg_1.jpg
./fotos/urlaub/2026/notiz.txt
$ find . -type f -size -2k
./.einstellungen
./rezepte/kuchen/apfelkuchen.txt
./rezepte/kuchen/kaesekuchen.txt
./rezepte/suppen/kuerbissuppe.txt
./fotos/urlaub/2026/strand_10.jpg
./fotos/urlaub/2026/strand_1.jpg
./fotos/urlaub/2026/strand_2.jpg
./fotos/urlaub/2026/berge/berg_2.jpg
./fotos/urlaub/2026/berge/berg_1.jpg
./fotos/urlaub/2026/notiz.txt
./einkauf.txt
```

`-size -1k` liefert genau dasselbe wie `-size 0`. Erst `-size -2k` findet auch die Rezepte und die Einkaufsliste mit ihren wenigen Dutzend Bytes, auf dem Testrechner 32 bis 59. Wer Dateien unter 1024 Bytes sucht, schreibt am sichersten `-size -1024c`.
::::

⁠**Kurz gesagt:** `-size +n` und `-size -n` suchen nach Größe; weil `find` auf ganze Einheiten aufrundet, nimmt man für genaue Grenzen Bytes (`c`).

### Nach Alter suchen: -mtime, -mmin und -newer

<span class="anker" id="stufe-10-5"></span>

„Die Datei von gestern“ ist oft die einzige Erinnerung, die man an eine Datei hat. Auch danach kann `find` suchen, mit dem Zeitpunkt der letzten Änderung des Inhalts. Abbildung [40](#abb-40) zeigt, wie es das Alter zählt.

:::abbildung linux/k3findzeit 40
Eine Zeitachse, die von jetzt nach links in die Vergangenheit reicht, eingeteilt in ganze Tage zu 24 Stunden. `-mtime -1` markiert den jüngsten Tag, `-mtime +7` alles, was mindestens acht ganze Tage zurückliegt; der Käsekuchen vom 1. Oktober liegt weit links.
:::

:::definition Definition 10.5 (-mtime, -mmin, -newer)
<span class="anker" id="satz-10-5"></span>

Der Test __-mtime n__ vergleicht das Alter der letzten Änderung in ganzen Tagen zu 24 Stunden mit `n`; angebrochene Tage fallen weg, und `+n` und `-n` heißen wie bei `-size` mehr und weniger. `-mmin n` tut dasselbe in Minuten. `-newer datei` besteht, wenn ein Eintrag später geändert wurde als die genannte Datei.
:::

`-mtime -1` heißt also „in den letzten 24 Stunden geändert“, `-mtime +7` „vor mindestens acht ganzen Tagen“, denn ein Alter von sieben Tagen und einigen Stunden zählt als 7 und ist nicht größer als 7. Mit `-newer` kann man eine Vergleichsdatei anlegen und später alles finden, was seitdem geändert wurde.

::::beispiel Alte und frische Dateien
Der Käsekuchen bekommt mit `touch -t` einen Änderungszeitpunkt im Oktober:

```console
$ touch -t 202610011200 rezepte/kuchen/kaesekuchen.txt
$ find . -type f -mtime +7
./rezepte/kuchen/kaesekuchen.txt
$ find rezepte -type f -mmin -60
rezepte/kuchen/apfelkuchen.txt
rezepte/suppen/kuerbissuppe.txt
```

Nur der Käsekuchen ist älter als sieben ganze Tage; die beiden anderen Rezepte wurden in der letzten Stunde geändert.
::::

::::beispiel [Zweites Beispiel] Was hat sich seit der Vergleichsdatei geändert?
```console
$ touch merker
$ touch rezepte/kuchen/apfelkuchen.txt
$ find rezepte -newer merker
rezepte/kuchen/apfelkuchen.txt
$ rm merker
```

Nur der Apfelkuchen wurde nach der Vergleichsdatei `merker` geändert. Programme zum Sichern von Daten arbeiten nach demselben Prinzip.
::::

⁠**Kurz gesagt:** `-mtime` und `-mmin` suchen nach dem Alter in ganzen Tagen oder Minuten, `-newer` im Vergleich mit einer anderen Datei.

### Tests verknüpfen und Treffer bearbeiten

<span class="anker" id="stufe-10-6"></span>

Eine Suche wird erst richtig nützlich, wenn man Bedingungen verbindet: gewöhnliche Dateien, die auf `.txt` enden und nicht älter als eine Woche sind. Und oft will man mit den Treffern mehr tun, als sie anzuzeigen.

:::definition Definition 10.6 (Verknüpfen, -maxdepth, Aktion)
<span class="anker" id="satz-10-6"></span>

Stehen mehrere Tests hintereinander, muss ein Eintrag alle bestehen. Ein __!__ vor einem Test kehrt ihn um. Die Angabe __-maxdepth n__ direkt nach den Startverzeichnissen begrenzt die Suche auf `n` Ebenen unterhalb des Startverzeichnisses. Was `find` mit einem Treffer tut, bestimmt eine __Aktion__; ohne Angabe ist das `-print`, die Ausgabe des Pfads.
:::

Zwei weitere Aktionen sind nützlich: `-ls` gibt jeden Treffer in einer Form aus, die `ls -l` ähnelt, und `-delete` löscht ihn. Zu Abschnitt [8](inode-und-links.html#stufe-8) passt der Test `-samefile datei`: Er findet alle Namen derselben Inode, also alle harten Links einer Datei.

::::beispiel Flach suchen, umkehren, harte Links finden
```console
$ find /etc -maxdepth 1 -name "h*"
/etc/host.conf
/etc/hosts
/etc/hostname
$ find . -type f ! -name "*.jpg"
./.einstellungen
./rezepte/kuchen/apfelkuchen.txt
./rezepte/kuchen/kaesekuchen.txt
./rezepte/suppen/kuerbissuppe.txt
./fotos/urlaub/2026/notiz.txt
./einkauf.txt
```

Mit `-maxdepth 1` bleibt `find` in `/etc` selbst und steigt in keines der 91 Unterverzeichnisse hinab. Die zweite Suche liefert alle gewöhnlichen Dateien, deren Name nicht auf `.jpg` endet. Für `-samefile` braucht die Einkaufsliste einen zweiten Namen:

```console
$ ln einkauf.txt fotos/liste.txt
$ find . -samefile einkauf.txt
./fotos/liste.txt
./einkauf.txt
$ rm fotos/liste.txt
```
::::

:::warnung -delete erst nach einer Probe
`-delete` löscht ohne Rückfrage alles, was die Tests bestehen, und steht man im falschen Verzeichnis oder ist ein Test zu weit gefasst, trifft es viel mehr als gedacht. Führe dieselbe Zeile deshalb immer erst ohne `-delete` aus und prüfe die Liste. `-delete` gehört ans Ende der Zeile: Steht es vor den Tests, löscht `find` jeden Eintrag, bevor es ihn prüft.
:::

::::beispiel [Zweites Beispiel] Aufräumen mit Probe
```console
$ touch rezepte/a.tmp rezepte/suppen/b.tmp
$ find . -name "*.tmp"
./rezepte/a.tmp
./rezepte/suppen/b.tmp
$ find . -name "*.tmp" -delete
$ find . -name "*.tmp"
```

Die Probe zeigt genau die beiden Dateien, die weg sollen; die gleiche Zeile mit `-delete` entfernt sie, und eine zweite Probe findet nichts mehr.
::::

⁠**Kurz gesagt:** Tests hintereinander müssen alle bestehen, `!` kehrt einen um, `-maxdepth` begrenzt die Tiefe; `-delete` nur nach einer Probe ohne.

:::hintergrund Oder, Klammern und ein schnellerer Weg zum Namen
Neben dem stillen „und“ kennt `find` auch ein „oder“: `-o`. Weil „und“ stärker bindet, braucht man oft Klammern, und die muss man vor der Shell schützen, etwa mit einem umgekehrten Schrägstrich: `find . \( -name "*.jpg" -o -name "*.png" \)` findet beide Bildarten. `find` wertet die Tests von links nach rechts aus und hört auf, sobald das Ergebnis feststeht; deshalb kommt es auf die Reihenfolge an, und deshalb löscht ein `-delete` am Anfang alles. Weil `find` bei jeder Suche den ganzen Teilbaum durchläuft, kann es auf großen Datenträgern lange dauern. Manche Systeme haben zusätzlich den Befehl `locate`, der in einer Liste aller Pfade sucht, die meist einmal am Tag neu erstellt wird: viel schneller, aber ohne die Dateien, die seit der letzten Erstellung hinzugekommen sind.
:::

### Den Platzbedarf messen: du

<span class="anker" id="stufe-10-7"></span>

`df` sagt, wie voll ein ganzes Dateisystem ist. Wer Platz schaffen will, muss wissen, welches Verzeichnis ihn belegt.

:::definition Definition 10.7 (du)
<span class="anker" id="satz-10-7"></span>

Der Befehl __du__ (kurz für „disk usage“) zählt für jedes genannte Verzeichnis und jedes Unterverzeichnis darin den Platz zusammen, den die Dateien auf dem Datenträger belegen, in Einheiten von 1024 Byte. Mit `-s` gibt er nur die Summe für jedes Argument aus, mit `-h` lesbare Einheiten wie `ls -h`.
:::

`du` zählt den belegten Platz, nicht die Zahl der Bytes im Inhalt. Ein Dateisystem teilt Platz in Blöcken zu, bei ext4 meist zu 4096 Byte; eine Datei belegt immer ganze Blöcke, auch wenn der letzte nur angebrochen ist. Eine Datei mit 32 Bytes belegt deshalb 4 KiB. Mit `--apparent-size` zählt `du` stattdessen die Bytes des Inhalts, wie `ls -l`. Eine Datei mit mehreren harten Links zählt `du` nur einmal.

:::abbildung linux/k3du 41
Der Platz des Verzeichnisses `rezepte`, zusammengezählt: das Verzeichnis selbst 4 KiB, `kuchen` mit zwei Rezepten $4 + 4 + 4 = 12$ KiB, `suppen` mit einem $4 + 4 = 8$ KiB, der symbolische Link 0. Zusammen $4 + 12 + 8 = 24$ KiB.
:::

::::beispiel Wer belegt den Platz?
```console
$ du rezepte
12      rezepte/kuchen
8       rezepte/suppen
24      rezepte
$ du -sh rezepte fotos
24K     rezepte
16K     fotos
$ du -sh ~/linuxk3
48K     /home/student/linuxk3
```

`kuchen` belegt 12 KiB: einen Block für das Verzeichnis selbst und je einen für die beiden Rezepte. `rezepte` kommt mit seinem eigenen Block auf 24, wie Abbildung [41](#abb-41) vorrechnet. `fotos` belegt 16 KiB, nämlich vier Verzeichnisse zu je einem Block; die leeren Fotodateien belegen nichts.
::::

::::beispiel [Zweites Beispiel] Inhalt und Platz einer kleinen Datei
```console
$ ls -l einkauf.txt
-rw-r--r-- 1 student student 32 Nov 10 02:42 einkauf.txt
$ du -h einkauf.txt
4.0K    einkauf.txt
$ du -h --apparent-size einkauf.txt
32      einkauf.txt
```

32 Bytes Inhalt, aber ein ganzer Block von 4096 Byte belegt. `stat` hat in Unterabschnitt [8.1](inode-und-links.html#stufe-8-1) dasselbe gezeigt: `Blocks: 8` zählt in alten Einheiten zu 512 Byte, und $8 \cdot 512 = 4096$.
::::

⁠**Kurz gesagt:** `du -sh` zeigt, wie viel Platz ein Verzeichnis belegt; gezählt werden ganze Blöcke, deshalb belegt auch eine winzige Datei 4 KiB.

:::hintergrund Warum ein Dateisystem in Blöcken rechnet
Ein Dateisystem könnte jedes Byte einzeln verwalten, doch dann bräuchte es für jede Datei eine riesige Liste, wo ihre Bytes liegen. Stattdessen teilt es den Datenträger in gleich große Blöcke und merkt sich in der Inode nur, welche Blöcke eine Datei belegt. Große Blöcke machen diese Verwaltung klein und das Lesen großer Dateien schnell, verschwenden aber bei kleinen Dateien Platz; 4096 Byte sind ein Kompromiss, der zur Seitengröße passt, mit der der Prozessor den Arbeitsspeicher verwaltet. Daraus folgt auch, warum `du` und `df` nicht immer zusammenpassen: `du` zählt nach, was die Dateien eines Teilbaums belegen, `df` fragt das Dateisystem nach seiner Verwaltung. Eine gelöschte Datei, die ein Programm noch geöffnet hat, findet `du` nicht mehr, denn sie hat keinen Namen; ihren Platz meldet `df` aber weiter als belegt, bis das Programm sie schließt (Unterabschnitt [8.4](inode-und-links.html#stufe-8-4)).
:::

### Aufgaben zu Abschnitt [10](#stufe-10)

<span class="anker" id="stufe-10-8"></span>

:::aufgabe Aufgabe 34 ★★ Suchaufträge
<span class="anker" id="aufg-34"></span>

Schreibe für jeden Auftrag eine Befehlszeile mit `find` und führe sie aus: (a) alle Dateien in `/etc` selbst, nicht in Unterverzeichnissen, deren Name auf `.conf` endet; (b) alle Verzeichnisse deiner Spielwiese; (c) alle Dateien in `/usr/bin`, die größer als 1 MiB sind; (d) alle gewöhnlichen Dateien in `~/linuxk3`, die in den letzten 24 Stunden geändert wurden.

:::loesung
(a) `find /etc -maxdepth 1 -name "*.conf"`. (b) `find ~/linuxk3 -type d`, die Ausgabe zeigt Unterabschnitt [10.3](#stufe-10-3). (c) `find /usr/bin -size +1M`; wegen des Aufrundens heißt `+1M` „mehr als 1 MiB“. (d) `find ~/linuxk3 -type f -mtime -1`. Auf dem Testrechner, gekürzt:

```console
$ find /etc -maxdepth 1 -name "*.conf"
/etc/xattr.conf
/etc/host.conf
/etc/pam.conf
...
/etc/debconf.conf
/etc/wsl-distribution.conf
$ find /usr/bin -size +1M
/usr/bin/x86_64-linux-gnu-gcc-15
/usr/bin/strace
...
/usr/bin/gdb
/usr/bin/perl
$ find ~/linuxk3 -type f -mtime -1
/home/student/linuxk3/.einstellungen
/home/student/linuxk3/verein/mitglieder/liste.txt
...
/home/student/linuxk3/einkauf.txt
```

Es sind 27 Einstellungsdateien und 23 Programme über 1 MiB. Bei (d) fehlt der Käsekuchen, dessen Änderungszeit im Oktober liegt; weil `find` nicht nach Namen sortiert, stehen die Treffer in der Reihenfolge der Verzeichnisse.
:::
:::

:::aufgabe Aufgabe 35 ★★ Das vergessene Anführungszeichen
<span class="anker" id="aufg-35"></span>

Wechsle nach `~/linuxk3/fotos/urlaub/2026`, wo es genau eine Datei auf `.txt` gibt, und vergleiche `find ~/linuxk3 -name *.txt` mit `find ~/linuxk3 -name "*.txt"`. Warum meldet die erste Zeile diesmal keinen Fehler, liefert aber zu wenig? Warum liefert die zweite Zeile in jedem Arbeitsverzeichnis dasselbe?

:::loesung
```console
$ cd fotos/urlaub/2026
$ find ~/linuxk3 -name *.txt
/home/student/linuxk3/fotos/urlaub/2026/notiz.txt
$ find ~/linuxk3 -name "*.txt"
/home/student/linuxk3/aktuell.txt
/home/student/linuxk3/verein/mitglieder/liste.txt
...
/home/student/linuxk3/einkauf.txt
$ cd ~/linuxk3
```

Im Arbeitsverzeichnis gibt es genau einen Namen auf `.txt`, `notiz.txt`. Die Shell ersetzt das Muster ohne Anführungszeichen durch diesen einen Namen, und `find` bekommt `-name notiz.txt`. Das ist eine gültige Bedingung, also gibt es keinen Fehler, aber gesucht wird nur noch nach Dateien namens `notiz.txt`. Mit Anführungszeichen bekommt `find` das Muster selbst und wendet es auf jeden Namen im Teilbaum an. Weil die Shell ein Muster in Anführungszeichen nie ersetzt, hängt das Ergebnis dann nicht davon ab, welche Dateien zufällig im Arbeitsverzeichnis liegen.
:::
:::

:::aufgabe Aufgabe 36 ★★★ Die Rundungsfalle von -size
<span class="anker" id="aufg-36"></span>

Sage voraus, was `find rezepte -type f -size -1M` und `find rezepte -type f -size -1024k` ausgeben, und prüfe es. Erkläre den Unterschied mit dem Aufrunden. Wie findest du zuverlässig alle Dateien, die kleiner als 1 MiB sind?

:::loesung
```console
$ find rezepte -type f -size -1M
$ find rezepte -type f -size -1024k
rezepte/kuchen/apfelkuchen.txt
rezepte/kuchen/kaesekuchen.txt
rezepte/suppen/kuerbissuppe.txt
```

Bei `-1M` rundet `find` jede Größe auf ganze MiB auf: Die Rezepte mit wenigen Dutzend Bytes zählen als 1 MiB, und 1 ist nicht kleiner als 1. Treffen würde nur eine leere Datei, und davon gibt es in `rezepte` keine. Bei `-1024k` rundet es auf ganze KiB auf: Die Rezepte zählen als 1 KiB, und das ist kleiner als 1024. Zuverlässig ist die Angabe in Bytes, bei der nichts gerundet wird: `find rezepte -type f -size -1048576c` findet alle Dateien unter $1024^2 = 1\,048\,576$ Byte.
:::
:::

:::aufgabe Aufgabe 37 ★★ Wie viel Platz belegt eine kleine Datei?
<span class="anker" id="aufg-37"></span>

Vergleiche für `rezepte/kuchen/kaesekuchen.txt` die Größe aus `ls -l`, den Platz aus `du -h` und `du -h --apparent-size`. Wie viel Platz belegten hundert solche Dateien, wie viele Bytes Inhalt hätten sie zusammen? Wie groß müsste eine Datei mindestens sein, damit sie zwei Blöcke belegt?

:::loesung
```console
$ ls -l rezepte/kuchen/kaesekuchen.txt
-rw-r--r-- 1 student student 32 Oct  1 12:00 rezepte/kuchen/kaesekuchen.txt
$ du -h rezepte/kuchen/kaesekuchen.txt
4.0K    rezepte/kuchen/kaesekuchen.txt
$ du -h --apparent-size rezepte/kuchen/kaesekuchen.txt
32      rezepte/kuchen/kaesekuchen.txt
```

Die Datei hat 32 Bytes Inhalt und belegt einen Block von 4096 Byte. Hundert solche Dateien belegten $100 \cdot 4 = 400$ KiB, obwohl sie zusammen nur $100 \cdot 32 = 3200$ Byte enthielten, gut 3 KiB. Zwei Blöcke belegt eine Datei ab $4096 + 1 = 4097$ Byte, denn dann reicht ein Block nicht mehr. Deine Rezepte sind vermutlich anders lang; solange sie unter 4097 Byte bleiben, belegt jedes genau 4 KiB.
:::
:::

**Zum Weiterüben.** Die frei zugängliche Übungsplattform pwn.college bietet unter dem Namen „Linux Luminarium“ kleine Aufgaben im Browser an; die Module „Pondering Paths“ und „File Globbing“ passen zu diesem Kapitel. Sie laufen auf einem fremden Rechner, nicht auf deinem eigenen.

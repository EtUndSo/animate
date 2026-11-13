---
title: Dateien übertragen: scp, sftp und rsync
pfad: Informatik / Linux und Kommandozeile / Auf entfernten Rechnern arbeiten: SSH, Dateien übertragen, tmux
adresse: informatik/linux-und-kommandozeile/auf-entfernten-rechnern-arbeiten-ssh-dateien-ubertragen-tmux
knoten: Kapitel 11: Auf entfernten Rechnern arbeiten: SSH, Dateien übertragen, tmux
order: 6160600
summary: Dieser Abschnitt bringt Dateien zwischen deinem Rechner und dem Server hin und her: einzeln mit scp , im Gespräch mit sftp und abgleichend mit rsync , das nur Änderungen überträgt.
tags: schnellen Vergleich, Blockvergleich
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Dieser Abschnitt bringt Dateien zwischen deinem Rechner und dem Server hin und her: einzeln mit `scp`, im Gespräch mit `sftp` und abgleichend mit `rsync`, das nur Änderungen überträgt. Alle drei benutzen eine SSH-Verbindung und die Einträge aus `~/.ssh/config`.
:::

### Kopieren über die Verbindung: scp

<span class="anker" id="stufe-5-1"></span>

Mit `cp` kopiert man innerhalb eines Rechners ([Kapitel 3, Abschnitt 6.1](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/kopieren-verschieben-loschen.html#stufe-6-1)). Für Kopien zwischen zwei Rechnern gibt es ein Gegenstück, das genauso aussieht, nur dass eine Seite auf einem anderen Rechner liegen darf.

:::definition Definition 5.1 (scp)
<span class="anker" id="satz-5-1"></span>

`scp quelle ziel` („secure copy“) kopiert Dateien über eine SSH-Verbindung. Quelle oder Ziel darf die Form `rechner:pfad` oder `benutzer@rechner:pfad` haben; der Doppelpunkt kennzeichnet die Seite auf dem anderen Rechner. Ein relativer Pfad hinter dem Doppelpunkt beginnt im Heimatverzeichnis auf dem Server. `-r` kopiert Verzeichnisse samt Inhalt, `-P` wählt den Port.
:::

Weil Client und Server hier derselbe Rechner sind, landet alles, was du „auf den Server“ kopierst, letztlich auch in deinem eigenen Heimatverzeichnis. Damit man trotzdem sieht, was wohin wandert, benutzt die Serverseite in allen Übungen ein eigenes Verzeichnis `linuxk11/server`. Lege es auf dem Server an, und lege lokal ein Verzeichnis `urlaub` mit drei kleinen Dateien an:

```console
$ ssh uebung 'mkdir linuxk11/server'
$ mkdir urlaub
$ printf '%s\n' 'Tag 1: Anreise, Regen' > urlaub/tag1.txt
$ printf '%s\n' 'Tag 2: Wanderung zum See' > urlaub/tag2.txt
$ printf '%s\n' 'Tag 3: Museum und Eis' > urlaub/tag3.txt
$ ls -l urlaub
total 12
-rw-r--r-- 1 student student 22 Nov 13 03:19 tag1.txt
-rw-r--r-- 1 student student 25 Nov 13 03:19 tag2.txt
-rw-r--r-- 1 student student 22 Nov 13 03:19 tag3.txt
```

::::beispiel Hin und zurück
```console
$ scp einkauf.txt uebung:linuxk11/server/
einkauf.txt                           100%   25    49.5KB/s   00:00
$ ssh uebung 'ls -l linuxk11/server'
total 4
-rw-r--r-- 1 student student 25 Nov 13 03:19 einkauf.txt
$ scp uebung:linuxk11/server/einkauf.txt zurueck.txt
einkauf.txt                           100%   25    33.6KB/s   00:00
$ cat zurueck.txt
Milch
Brot
Äpfel
Kaffee
```

Während der Übertragung zeigt `scp` eine Zeile mit dem Namen, dem Fortschritt in Prozent, der Größe in Bytes, der Geschwindigkeit und der Dauer. Die Richtung ergibt sich allein aus der Reihenfolge: zuerst die Quelle, dann das Ziel, wie bei `cp`. Ganze Verzeichnisse kopiert `-r`; die Reihenfolge der Dateien in der Ausgabe ist die, in der `scp` sie im Verzeichnis findet:

```console
$ scp -r urlaub uebung:linuxk11/server/
tag1.txt                              100%   22    79.4KB/s   00:00
tag3.txt                              100%   22    95.7KB/s   00:00
tag2.txt                              100%   25    85.4KB/s   00:00
$ ssh uebung 'ls linuxk11/server/urlaub'
tag1.txt
tag2.txt
tag3.txt
```
::::

:::warnung Der vergessene Doppelpunkt
Fehlt der Doppelpunkt, ist `uebung` kein Rechner, sondern ein gewöhnlicher Dateiname, und `scp` kopiert still auf deinem eigenen Rechner:

```console
$ scp einkauf.txt uebung
$ ls -l uebung
-rw-r--r-- 1 student student 25 Nov 13 03:19 uebung
$ rm uebung
```

Es erscheint weder eine Fortschrittszeile noch eine Fehlermeldung. Prüfe nach jeder wichtigen Übertragung auf der Zielseite, ob die Datei wirklich angekommen ist. Umgekehrt hält `scp` jeden Namen mit einem Doppelpunkt für einen Rechner; eine lokale Datei namens `a:b` schreibt man deshalb als `./a:b`.
:::

:::abbildung linux/k11scp 21
Zwei Rechner nebeneinander, „hier“ (`~/linuxk11`) und „uebung“ (`~/linuxk11/server`). Drei Befehle erscheinen nacheinander, jeder mit einem Pfeil von der Quelle zum Ziel: `scp einkauf.txt uebung:linuxk11/server/` (Pfeil nach rechts, Doppelpunkt rot hervorgehoben), `scp uebung:linuxk11/server/einkauf.txt zurueck.txt` (Pfeil nach links), `scp einkauf.txt uebung` (Pfeil bleibt auf der linken Seite und biegt in eine Datei `uebung`; Schild „kein Doppelpunkt: lokale Kopie“).
:::

:::hintergrund Warum scp heute anders arbeitet als früher
Bis 2022 benutzte `scp` ein eigenes, sehr altes Verfahren: Es startete auf dem Server über die Shell ein zweites `scp` und reichte ihm die Dateinamen als Befehlszeile. Die Shell auf dem Server deutete Muster, Leerzeichen und Sonderzeichen in diesen Namen, wie in Abschnitt [4.3](bequemer-verbinden-und-befehle-aus-der-ferne.html#stufe-4-3), und manche Sonderzeichen ließen sich sogar ausnutzen, um auf dem Server oder beim Empfänger etwas anderes zu tun als zu kopieren. Seit OpenSSH 9.0 benutzt `scp` deshalb ein anderes Protokoll, SFTP („SSH File Transfer Protocol“), bei dem keine Shell mehr Dateinamen deutet. Für die Bedienung ändert sich fast nichts; nur sehr alte Server ohne SFTP brauchen die Option `-O` für das alte Verfahren.
:::

⁠**Kurz gesagt:** `scp quelle ziel` kopiert wie `cp`, nur darf eine Seite `rechner:pfad` heißen; ohne Doppelpunkt bleibt alles lokal.

### Dateien im Gespräch übertragen: sftp

<span class="anker" id="stufe-5-2"></span>

Manchmal weiß man noch nicht genau, welche Datei man braucht, und will sich auf dem Server erst umsehen. Dafür gibt es ein Programm mit eigener Eingabeaufforderung.

:::definition Definition 5.2 (sftp)
<span class="anker" id="satz-5-2"></span>

`sftp rechner` („secure file transfer“) öffnet über eine SSH-Verbindung eine Sitzung, in der man Dateien auf dem Server ansieht und überträgt. Die Befehle ähneln denen der Shell: `ls`, `cd` und `pwd` wirken auf dem Server, `lls`, `lcd` und `lpwd` („local“) auf dem eigenen Rechner; `get datei [ziel]` holt eine Datei, `put datei [ziel]` schickt eine, `bye` beendet die Sitzung.
:::

::::beispiel Umsehen und holen
```console
$ sftp uebung
Connected to uebung.
sftp> cd linuxk11/server
sftp> ls
einkauf.txt   urlaub
sftp> lls
einkauf.txt  ssh_dateien.txt    uebungsschluessel.pub  zurueck.txt
server       uebungsschluessel  urlaub
sftp> get einkauf.txt aus_sftp.txt
Fetching /home/student/linuxk11/server/einkauf.txt to aus_sftp.txt
einkauf.txt                           100%   25    18.8KB/s   00:00
sftp> bye
```

`ls` zeigt das Verzeichnis auf dem Server, `lls` dein lokales Übungsverzeichnis, in dem auch das Verzeichnis `server` steht, weil beide Seiten auf demselben Rechner liegen. `get` holt die Datei unter neuem Namen ins lokale Arbeitsverzeichnis. Die Zeilen hinter `sftp>` sind deine Eingaben.
::::

:::abbildung linux/k11sftp 22
Terminalbild (dunkel, wie Ubuntu) der sftp-Sitzung aus dem Beispiel, Zeile für Zeile wie in der Mitschrift, von `sftp uebung` bis `sftp> bye`. Am Rand Etiketten: `cd`, `ls` mit „dort (Server)“, `lls` mit „hier (eigener Rechner)“, `get` mit „holt: Server → dein Rechner“.
:::

`sftp` spricht das Protokoll SFTP, dasselbe, das auch `scp` heute benutzt (Hintergrund in Abschnitt [5.1](#stufe-5-1)). Es braucht auf dem Server nur den SSH-Server; das Programm, das dort die Anfragen beantwortet, kam mit `openssh-server` als Paket `openssh-sftp-server`. Viele grafische Programme für Dateiübertragungen sprechen dasselbe Protokoll, so dass man mit ihnen per Maus auf einen SSH-Server zugreifen kann.

⁠**Kurz gesagt:** `sftp` ist eine Sitzung zum Umsehen und Übertragen mit eigenen Befehlen: `ls`/`cd` dort, `lls`/`lcd` hier, `get` holt, `put` schickt.

### Abgleichen statt kopieren: rsync

<span class="anker" id="stufe-5-3"></span>

Wer jeden Abend seine Fotos auf einen Server sichert, will nicht jedes Mal alle Fotos übertragen, sondern nur die neuen und die geänderten. `scp` kopiert immer alles. Ein anderes Werkzeug vergleicht erst und überträgt dann nur, was fehlt oder sich unterscheidet.

:::definition Definition 5.3 (rsync)
<span class="anker" id="satz-5-3"></span>

`rsync optionen quelle ziel` („remote sync“) gleicht das Ziel an die Quelle an. Wie bei `scp` darf eine Seite `rechner:pfad` heißen; dann benutzt `rsync` eine SSH-Verbindung und startet auf dem Server ein zweites `rsync`, mit dem es die Dateien vergleicht. Übertragen wird nur, was auf dem Ziel fehlt oder sich unterscheidet. Die übliche Option ist `-a` („archive“): Verzeichnisse samt Inhalt, und Rechte, Zeitstempel und symbolische Links bleiben erhalten. `-v` zählt die übertragenen Dateien auf.
:::

`rsync` muss deshalb auf beiden Rechnern installiert sein; unter Ubuntu ist es in der Regel von Anfang an dabei, sonst holt man es mit `sudo apt install rsync`. Ein Beispiel mit dem Urlaubsverzeichnis; der zweite Aufruf folgt sofort auf den ersten:

```console
$ rsync -av urlaub/ uebung:linuxk11/server/sicherung/
sending incremental file list
created directory linuxk11/server/sicherung
./
tag1.txt
tag2.txt
tag3.txt

sent 320 bytes  received 124 bytes  296.00 bytes/sec
total size is 69  speedup is 0.16
$ rsync -av urlaub/ uebung:linuxk11/server/sicherung/
sending incremental file list

sent 115 bytes  received 12 bytes  254.00 bytes/sec
total size is 69  speedup is 0.54
```

Beim ersten Lauf legt `rsync` das Zielverzeichnis an und überträgt alle drei Dateien; `./` steht für das Verzeichnis selbst, dessen Rechte und Zeit es angleicht. Beim zweiten Lauf ist nichts zu tun, und keine Datei erscheint in der Liste. Die beiden Schlusszeilen nennen die gesendeten und empfangenen Bytes, die Gesamtgröße der Dateien (69 Bytes) und den Quotienten aus Gesamtgröße und übertragenen Bytes (*speedup*); bei so kleinen Dateien überwiegt die Verwaltung, bei großen wird der Quotient groß. Kommt eine Datei hinzu, überträgt `rsync` nur sie:

```console
$ printf '%s\n' 'Tag 4: Heimreise' > urlaub/tag4.txt
$ rsync -av urlaub/ uebung:linuxk11/server/sicherung/
sending incremental file list
./
tag4.txt

sent 201 bytes  received 38 bytes  478.00 bytes/sec
total size is 86  speedup is 0.36
```

Abbildung [23](#abb-23) stellt die drei Läufe nebeneinander.

:::abbildung linux/k11rsync 23
Drei Läufe von `rsync -av urlaub/ uebung:linuxk11/server/sicherung/` nebeneinander. In jedem links das lokale Verzeichnis, rechts die Sicherung auf dem Server. Lauf 1: Die Sicherung ist leer, drei Dateien `tag1.txt`–`tag3.txt` wandern nach rechts. Lauf 2: Jede Datei wird links und rechts verglichen (Waage mit Größe und Zeit), alle Waagen im Gleichgewicht, nichts wandert. Lauf 3: `tag4.txt` ist neu, nur sie wandert. Unter jedem Lauf die übertragene Datenmenge aus der Ausgabe (`sent 320 bytes`, `sent 115 bytes`, `sent 201 bytes`).
:::

⁠**Kurz gesagt:** `rsync -av quelle ziel` gleicht das Ziel an und überträgt nur, was fehlt oder sich geändert hat; ein zweiter Lauf ohne Änderungen überträgt keine Datei.

### Der Schrägstrich am Quellverzeichnis

<span class="anker" id="stufe-5-4"></span>

In den Beispielen stand hinter `urlaub` ein Schrägstrich. Bei `rsync` ist er keine Nebensache:

```console
$ rsync -a urlaub uebung:linuxk11/server/mit_ordner/
$ rsync -a urlaub/ uebung:linuxk11/server/nur_inhalt/
$ ssh uebung 'ls linuxk11/server/mit_ordner linuxk11/server/nur_inhalt'
linuxk11/server/mit_ordner:
urlaub

linuxk11/server/nur_inhalt:
tag1.txt
tag2.txt
tag3.txt
tag4.txt
```

:::satz Satz 5.4 (Der Schrägstrich am Quellverzeichnis)
<span class="anker" id="satz-5-4"></span>

Ohne Schrägstrich am Ende kopiert `rsync` das Quellverzeichnis selbst in das Ziel; es entsteht `ziel/urlaub`. Mit Schrägstrich kopiert es nur den Inhalt des Verzeichnisses in das Ziel. Ein Schrägstrich am Ende des *Ziels* ändert bei einem Verzeichnis als Quelle dagegen nichts.
:::

Man kann sich `urlaub/` als „der Inhalt von `urlaub`“ vorstellen, ähnlich wie `urlaub/*`, nur dass auch versteckte Dateien mitkommen. Wer eine Sicherung regelmäßig aktualisiert, muss den Schrägstrich immer gleich setzen; sonst entsteht beim nächsten Lauf eine zweite Ebene neben der alten. Abbildung [24](#abb-24) zeigt den Unterschied.

:::abbildung linux/k11schraegstrich 24
Der Schrägstrich bei rsync. Links auf dem eigenen Rechner das Verzeichnis `urlaub` als Karton mit vier Dateien, rechts auf dem Server zwei Ziele. Obere Bahn `rsync -a urlaub …/mit_ordner/`: der ganze Karton wandert und steht im Ziel als `mit_ordner/urlaub/`. Untere Bahn `rsync -a urlaub/ …/nur_inhalt/`: der Karton wird geöffnet (der Schrägstrich leuchtet), nur die vier Dateien wandern und liegen direkt in `nur_inhalt/`.
:::

⁠**Kurz gesagt:** `urlaub` ohne Schrägstrich kopiert das Verzeichnis, `urlaub/` mit Schrägstrich seinen Inhalt.

### Abgleichen mit --delete und der Probelauf

<span class="anker" id="stufe-5-5"></span>

Löscht man in der Quelle eine Datei, bleibt sie in der Sicherung stehen; `rsync` ergänzt und erneuert nur. Soll das Ziel ein genaues Abbild der Quelle sein, löscht `--delete` im Ziel alles, was in der Quelle fehlt. Weil das Dateien vernichtet, probiert man es zuerst mit `-n` („dry run“) aus: `rsync` zeigt dann, was es tun würde, und tut nichts. Das ist dieselbe Idee wie der Probelauf mit `echo` in [Kapitel 10, Abschnitt 10.4](/wissen/informatik/linux-und-kommandozeile/shell-skripte/skripte-prufen-und-fehler-finden.html#stufe-10-4).

:::warnung --delete erst nach einem Probelauf
Mit `--delete` entscheidet die Quelle, was im Ziel bleiben darf. Vertauscht man Quelle und Ziel, nennt ein leeres Verzeichnis als Quelle oder setzt den Schrägstrich anders als sonst, löscht `rsync` im Ziel ohne Rückfrage, im schlimmsten Fall alles. Lass jeden neuen Aufruf mit `--delete` zuerst mit `-n` laufen und lies die Zeilen mit `deleting`, bevor du `-n` weglässt.
:::

::::beispiel Eine gelöschte Datei auch in der Sicherung löschen
`tag1.txt` wird lokal gelöscht. Der Probelauf kündigt an, was geschähe, und die Sicherung bleibt unverändert; erst der zweite Aufruf ohne `-n` löscht:

```console
$ rm urlaub/tag1.txt
$ rsync -avn --delete urlaub/ uebung:linuxk11/server/sicherung/
sending incremental file list
deleting tag1.txt
./

sent 130 bytes  received 38 bytes  336.00 bytes/sec
total size is 64  speedup is 0.38 (DRY RUN)
$ ssh uebung 'ls linuxk11/server/sicherung'
tag1.txt
tag2.txt
tag3.txt
tag4.txt
$ rsync -av --delete urlaub/ uebung:linuxk11/server/sicherung/
sending incremental file list
deleting tag1.txt
./

sent 130 bytes  received 34 bytes  328.00 bytes/sec
total size is 64  speedup is 0.39
$ ssh uebung 'ls linuxk11/server/sicherung'
tag2.txt
tag3.txt
tag4.txt
```

`(DRY RUN)` in der letzten Zeile erinnert daran, dass nichts geschehen ist.
::::

⁠**Kurz gesagt:** `--delete` macht das Ziel zum genauen Abbild der Quelle und löscht dabei; `-n` zeigt vorher, was geschähe.

### Wie rsync nur die Änderungen überträgt

<span class="anker" id="stufe-5-6"></span>

`rsync` spart auf zwei Stufen. Auf der ersten entscheidet es, welche Dateien es sich überhaupt genauer ansieht. Auf der zweiten überträgt es von einer geänderten Datei nur die geänderten Stücke.

:::definition Definition 5.5 (Schneller Vergleich und Blockvergleich)
<span class="anker" id="satz-5-5"></span>

Beim __schnellen Vergleich__ sieht `rsync` eine Datei als unverändert an, wenn sie im Ziel dieselbe Größe und dieselbe Änderungszeit hat wie in der Quelle, und rührt sie nicht an. Bei einer geänderten Datei arbeitet es mit dem __Blockvergleich__: Der Empfänger zerlegt seine alte Fassung in gleich große Blöcke und schickt für jeden Block kurze Prüfsummen. Der Sender sucht in seiner neuen Fassung nach Stellen mit denselben Prüfsummen und schickt für jeden gefundenen Block nur einen Verweis, für alles andere die Bytes selbst.
:::

Deshalb behält `-a` die Änderungszeiten bei: Nur dann erkennt der schnelle Vergleich beim nächsten Lauf, dass eine Datei unverändert ist. Dass nur die Änderungen übertragen werden, zeigt eine große Datei. `seq 1 200000` schreibt die Zahlen von 1 bis 200 000 untereinander ([Kapitel 6, Abschnitt 4.2](/wissen/informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke/nummerieren-zahlenfolgen-und-unterschiede-nl-seq-und-diff.html#stufe-4-2)); nach der ersten Übertragung kommt eine Zeile hinzu, und `--stats` zeigt die Zählung von `rsync`:

```console
$ seq 1 200000 > zahlen.txt
$ ls -l zahlen.txt
-rw-r--r-- 1 student student 1288895 Nov 13 03:19 zahlen.txt
$ rsync -a zahlen.txt uebung:linuxk11/server/
$ echo 200001 >> zahlen.txt
$ rsync -a --stats zahlen.txt uebung:linuxk11/server/ | grep -E '^(Total file size|Literal data|Matched data)'
Total file size: 1,288,902 bytes
Literal data: 726 bytes
Matched data: 1,288,176 bytes
```

Von 1 288 902 Bytes hat `rsync` nur 726 als Daten geschickt (*literal data*); den Rest, 1 288 176 Bytes, fand es in der alten Fassung auf dem Server wieder (*matched data*) und schickte dafür nur Verweise. Den Blockvergleich benutzt `rsync` von sich aus nur über eine Verbindung. Kopiert es innerhalb eines Rechners, etwa `rsync -a zahlen.txt kopie/`, schickt es geänderte Dateien ganz, weil das Lesen dort billiger ist als das Vergleichen; ein Versuch auf dem Testsystem meldete dafür 1 288 902 Bytes `Literal data`.

::::beispiel [Rechenbeispiel] Woher die 726 Bytes kommen
Für große Dateien wählt `rsync` als Blockgröße ungefähr die Wurzel der Dateigröße, abgerundet auf ein Vielfaches von 8. Die alte Fassung auf dem Server hatte 1 288 895 Bytes; $\sqrt{1\,288\,895}\approx 1135{,}3$, abgerundet auf ein Vielfaches von 8 sind das 1128 Bytes. Die alte Fassung besteht damit aus

$$1\,288\,895 = 1142\cdot 1128 + 719$$

Bytes: 1142 volle Blöcke und ein Rest von 719 Bytes. Die vollen Blöcke findet der Sender in der neuen Fassung unverändert wieder, $1142\cdot1128 = 1\,288\,176$ Bytes, genau die Zahl hinter `Matched data`. Der Rest von 719 Bytes steht in der neuen Fassung nicht mehr allein, denn dahinter folgt jetzt die neue Zeile `200001` mit Zeilenende, 7 Bytes. Dieses letzte Stück schickt der Sender als Daten: $719+7=726$ Bytes, genau die Zahl hinter `Literal data`. Abbildung [25](#abb-25) rechnet es Schritt für Schritt.

:::abbildung linux/k11delta 25
Rechenbild zum Blockvergleich, Zeile für Zeile: Blockgröße $\sqrt{1\,288\,895}\approx1135{,}3\to1128$ (Vielfaches von 8); $1\,288\,895 = 1142\cdot1128+719$; Matched data $=1142\cdot1128=1\,288\,176$; Literal data $=719+7=726$; Summe $1\,288\,176+726=1\,288\,902$ = Total file size. Darüber zwei Balken, nicht maßstäblich: die alte Fassung (1142 Blöcke und ein Rest von 719 Bytes) und die neue (dieselben 1142 Blöcke grün, „wiedergefunden“, und ein gelbes Endstück „719 + 7 Bytes: neu gesendet“).
:::
::::

:::hintergrund Wie der Sender die Blöcke wiederfindet
Der schwierige Teil des Blockvergleichs ist, dass sich Blöcke verschieben: Fügt man am Anfang einer Datei ein Byte ein, liegt jeder alte Block in der neuen Fassung um ein Byte versetzt. Der Sender muss deshalb an *jeder* Byteposition prüfen, ob dort ein Block der alten Fassung beginnt. Andrew Tridgell und Paul Mackerras von der Australian National University lösten das 1996 mit zwei Prüfsummen je Block. Die erste ist schwach, aber *rollend*: Rückt das Fenster um ein Byte weiter, lässt sie sich aus dem alten Wert mit wenigen Rechenschritten nachführen, indem man das herausfallende Byte abzieht und das neue hinzunimmt, statt den ganzen Block neu zu lesen. Mit ihr sucht der Sender schnell an allen Positionen nach Kandidaten. Erst bei einem Treffer berechnet er die zweite, starke Prüfsumme und bestätigt damit, dass der Block wirklich gleich ist. So genügt ein einziger Durchgang durch die neue Fassung, und übertragen wird nur, was sich nicht wiederfinden lässt. Ändert man eine Zeile mitten in der Datei, muss `rsync` nur den Block neu schicken, in dem sie liegt (Aufgabe [19](#aufg-19)); liegt sie über einer Blockgrenze, sind es die beiden betroffenen Blöcke.
:::

⁠**Kurz gesagt:** `rsync` überspringt Dateien mit gleicher Größe und Zeit und schickt von geänderten Dateien nur die Blöcke, die es in der alten Fassung nicht wiederfindet.

### Welches Werkzeug wofür

<span class="anker" id="stufe-5-7"></span>

Alle drei Werkzeuge übertragen über SSH, sind gleich sicher und benutzen dieselben Schlüssel und Einträge in `~/.ssh/config`. Sie unterscheiden sich darin, wofür sie gemacht sind; Tabelle [1](#tab-1) stellt es zusammen.

<span class="anker" id="tab-1"></span>

**Tabelle 1:** Werkzeuge zum Übertragen über SSH.

| Werkzeug | gut für | weniger gut für |
|---|---|---|
| `scp` | einzelne Dateien oder ein Verzeichnis einmal kopieren | wiederholte Sicherungen, abgebrochene große Übertragungen (beginnt immer von vorn) |
| `sftp` | sich auf dem Server umsehen und gezielt holen oder schicken | Skripte mit vielen Dateien |
| `rsync` | Verzeichnisse abgleichen, regelmäßige Sicherungen, große Dateien mit kleinen Änderungen | ein einzelnes kleines Kopieren (lohnt den Vergleich nicht) |
| `ssh` mit `tar` | ein Verzeichnis als ein Datenstrom, auch mit Pipe-Verarbeitung | Fortsetzen nach einem Abbruch |

::::beispiel Drei Aufgaben, drei Werkzeuge
Ein Foto für eine Mail vom Server holen: `scp uebung:fotos/see.jpg .`. Nachsehen, welche Berichte es auf dem Server gibt, und zwei davon holen: `sftp uebung`. Jeden Abend das Fotoverzeichnis sichern: `rsync -av fotos/ uebung:sicherung/fotos/`, weil nach dem ersten Abend nur noch die neuen Fotos übertragen werden.
::::

⁠**Kurz gesagt:** `scp` für einmalige Kopien, `sftp` zum Umsehen, `rsync` zum wiederholten Abgleichen.

:::aufgabe Aufgabe 16 ★ Richtungen lesen
<span class="anker" id="aufg-16"></span>

Gib für jeden Befehl an, was von wo nach wo kopiert wird: (a) `scp bericht.pdf uebung:`, (b) `scp uebung:bericht.pdf .`, (c) `scp -r uebung:fotos ~/bilder/`, (d) `scp bericht.pdf uebung.pdf`. Was ist bei (d) vermutlich ein Versehen?

:::loesung
(a) `bericht.pdf` vom eigenen Rechner ins Heimatverzeichnis auf `uebung` (nach dem Doppelpunkt steht nichts, das heißt: das Heimatverzeichnis). (b) `bericht.pdf` aus dem Heimatverzeichnis auf `uebung` ins lokale Arbeitsverzeichnis (`.`). (c) das Verzeichnis `fotos` vom Server samt Inhalt nach `~/bilder/fotos` auf dem eigenen Rechner. (d) eine lokale Kopie `uebung.pdf`; gemeint war vermutlich `uebung:` mit Doppelpunkt, also eine Kopie auf den Server. `scp` meldet dabei keinen Fehler.
:::
:::

:::aufgabe Aufgabe 17 ★★ Erst schauen, dann abgleichen
<span class="anker" id="aufg-17"></span>

Gleiche `urlaub/` mit einem neuen Verzeichnis `linuxk11/server/kopie/` auf dem Server ab. Ändere dann den Text in `urlaub/tag2.txt`, lass `rsync` zuerst mit `-n` laufen und prüfe auf dem Server, dass sich noch nichts geändert hat. Gleiche danach wirklich ab und prüfe erneut.

:::loesung
```console
$ rsync -a urlaub/ uebung:linuxk11/server/kopie/
$ printf '%s\n' 'Tag 2: Wanderung zum See, danach Pizza' > urlaub/tag2.txt
$ rsync -avn urlaub/ uebung:linuxk11/server/kopie/
sending incremental file list
tag2.txt

sent 110 bytes  received 19 bytes  86.00 bytes/sec
total size is 61  speedup is 0.47 (DRY RUN)
$ ssh uebung 'cat linuxk11/server/kopie/tag2.txt'
Tag 2: Wanderung zum See
$ rsync -av urlaub/ uebung:linuxk11/server/kopie/
sending incremental file list
tag2.txt

sent 189 bytes  received 41 bytes  460.00 bytes/sec
total size is 61  speedup is 0.27
$ ssh uebung 'cat linuxk11/server/kopie/tag2.txt'
Tag 2: Wanderung zum See, danach Pizza
```

Der Probelauf nennt `tag2.txt`, weil sich Größe und Änderungszeit geändert haben, und ändert nichts. Erst der Lauf ohne `-n` überträgt die neue Fassung. Die Byte-Zahlen hängen vom Inhalt von `urlaub` ab; bei dieser Mitschrift lagen darin nur `tag1.txt` und `tag2.txt`.
:::
:::

:::aufgabe Aufgabe 18 ★★ Schrägstriche vorhersagen
<span class="anker" id="aufg-18"></span>

Im lokalen Verzeichnis `fotos` liegen `a.jpg` und `b.jpg`; auf dem Server gibt es `sicherung/` noch nicht. Welche Pfade gibt es auf dem Server nach (a) `rsync -a fotos uebung:sicherung`, (b) `rsync -a fotos/ uebung:sicherung`, (c) `rsync -a fotos uebung:sicherung/`? Was geschieht, wenn man nach (a) versehentlich (b) aufruft?

:::loesung
(a) `sicherung/fotos/a.jpg` und `sicherung/fotos/b.jpg`: Ohne Schrägstrich kopiert `rsync` das Verzeichnis `fotos` selbst nach `sicherung`, das es dafür anlegt. (b) `sicherung/a.jpg` und `sicherung/b.jpg`: nur der Inhalt. (c) wie (a); ein Schrägstrich am Ziel ändert nichts. Ruft man nach (a) versehentlich (b) auf, liegen die Fotos danach doppelt: einmal in `sicherung/fotos/` und einmal direkt in `sicherung/`. Mit `--delete` wäre es noch schlimmer: (b) würde `sicherung/fotos` löschen, weil es in der Quelle `fotos/` kein Unterverzeichnis `fotos` gibt.
:::
:::

:::aufgabe Aufgabe 19 ★★★ Eine Zeile in der Mitte
<span class="anker" id="aufg-19"></span>

Übertrage die Datei `zahlen.txt` aus `seq 1 200000` auf den Server. Ersetze dann lokal die Zeile 100 000 durch `hunderttausend` (`sed -i '100000s/.*/hunderttausend/' zahlen.txt`, [Kapitel 6, Abschnitt 8.6](/wissen/informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke/umformen-im-strom-sed.html#stufe-8-6)) und übertrage erneut mit `--stats`. Sage vorher voraus, wie viele Bytes als `Literal data` gesendet werden, und erkläre das Ergebnis mit der Blockgröße 1128.

:::loesung
Die Zeile `100000` mit Zeilenende hat 7 Bytes, `hunderttausend` mit Zeilenende 15; die Datei wird um 8 Bytes länger. Die Zeile liegt in der alten Fassung vollständig in einem einzigen Block zu 1128 Bytes. Dieser eine Block passt nicht mehr; alle anderen findet `rsync` wieder, auch die dahinter, denn die rollende Prüfsumme findet sie an ihren um 8 Bytes verschobenen Stellen. Vorhersage: gesendet wird der Inhalt des geänderten Blocks, $1128+8=1136$ Bytes.

```console
$ seq 1 200000 > zahlen.txt
$ rsync -a zahlen.txt uebung:linuxk11/server/
$ sed -i '100000s/.*/hunderttausend/' zahlen.txt
$ sed -n '99999,100001p' zahlen.txt
99999
hunderttausend
100001
$ rsync -a --stats zahlen.txt uebung:linuxk11/server/ | grep -E '^(Total file size|Literal data|Matched data)'
Total file size: 1,288,903 bytes
Literal data: 1,136 bytes
Matched data: 1,287,767 bytes
```

Genau so: 1 136 Bytes als Daten, der Rest $1\,288\,903-1\,136=1\,287\,767$ Bytes als Verweise, das sind 1141 volle Blöcke und das Endstück von 719 Bytes ($1141\cdot1128+719=1\,287\,767$). `sed -n '99999,100001p'` zeigt zur Kontrolle die geänderte Zeile mit ihren Nachbarn ([Kapitel 6, Abschnitt 8.3](/wissen/informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke/umformen-im-strom-sed.html#stufe-8-3)).
:::
:::

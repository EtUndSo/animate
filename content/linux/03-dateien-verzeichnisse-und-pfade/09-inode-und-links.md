---
title: Inode und Links
pfad: Informatik / Linux und Kommandozeile / Dateien, Verzeichnisse und Pfade
adresse: informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade
knoten: Kapitel 3: Dateien, Verzeichnisse und Pfade
order: 6080900
summary: Bisher war ein Dateiname einfach der Name einer Datei.
tags: Inode, harter Link, Linkzähler, symbolischer Link, usr-merge
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Bisher war ein Dateiname einfach der Name einer Datei. Dieser Abschnitt schaut darunter: Name und Datei sind zwei verschiedene Dinge, die nur ein Eintrag im Verzeichnis verbindet. Daraus folgt, warum eine Datei mehrere Namen haben kann, warum `rm` keinen Papierkorb kennt und warum es zweierlei Verweise auf Dateien gibt.
:::

### Die Inode

<span class="anker" id="stufe-8-1"></span>

Eine Datei hat mehr Eigenschaften als ihren Inhalt: einen Besitzer, eine Größe, Zeitstempel, Zugriffsrechte. Irgendwo müssen diese Angaben stehen, und es stellt sich heraus, dass der Name nicht dazugehört.

:::abbildung linux/k3inode 29
Der Weg von einem Namen zu den Daten. Der Eintrag `einkauf.txt` im Verzeichnis enthält nur eine Nummer. Unter dieser Nummer findet das Dateisystem die Inode mit allen Angaben zur Datei, und die Inode verweist auf die Blöcke des Datenträgers, in denen der Inhalt steht.
:::

:::definition Definition 8.1 (Inode)
<span class="anker" id="satz-8-1"></span>

Eine __Inode__ ist der Verwaltungsblock einer Datei im Dateisystem. Sie enthält alle Angaben zur Datei außer ihrem Namen: Art, Zugriffsrechte, Besitzer und Gruppe, Größe, Zeitstempel, die Zahl ihrer Namen und die Lage der Blöcke, in denen der Inhalt gespeichert ist. Jede Inode hat eine Nummer, die Inode-Nummer, die innerhalb eines Dateisystems eindeutig ist.
:::

Abbildung [29](#abb-29) zeigt die drei Stufen: Name, Inode, Daten. Verzeichnisse haben ebenfalls eine Inode, ebenso Gerätedateien. Die Option `-i` lässt `ls` vor jeden Namen die Inode-Nummer setzen. Der Befehl `stat` zeigt, was in der Inode steht.

::::beispiel Die Inode der Einkaufsliste
```console
$ ls -i einkauf.txt
95361 einkauf.txt
$ stat einkauf.txt
  File: einkauf.txt
  size: 25              Blocks: 8          IO Block: 4096   regular file
Device: 8,48    Inode: 95361       Links: 1
Access: (0644/-rw-r--r--)  Uid: ( 1000/ student)   Gid: ( 1000/ student)
Access: 2026-11-10 02:41:57.014971387 +0100
Modify: 2026-11-10 02:41:56.714971764 +0100
Change: 2026-11-10 02:41:56.714971764 +0100
 Birth: 2026-11-10 02:41:54.890987095 +0100
```

Die Einkaufsliste hat die Inode 95361. `stat` liest darin: 25 Bytes, gespeichert in Blöcken, eine gewöhnliche Datei; `Links: 1` heißt, sie hat einen Namen; die Zugriffsrechte als Zahl und als Zeichen; Besitzer und Gruppe mit ihren Nummern aus [Kapitel 2, Abschnitt 6.2](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/das-system-erkunden.html#stufe-6-2); und die vier Zeitstempel aus dem Hintergrund in Unterabschnitt [5.2](dateien-und-verzeichnisse-anlegen.html#stufe-5-2). `Device: 8,48` ist der Datenträger, dieselben zwei Zahlen wie bei `/dev/sdd`. Die GNU-Fassung von `stat` schreibt `Size` mit großem S; das kleine s ist eine Eigenheit der uutils-Fassung 0.8 in Ubuntu 26.04, sonst sehen beide Ausgaben gleich aus.
::::

⁠**Kurz gesagt:** Die Inode ist der Verwaltungsblock einer Datei mit allen Angaben außer dem Namen; `ls -i` zeigt ihre Nummer, `stat` ihren Inhalt.

:::hintergrund Woher der Name Inode kommt
Das Wort geht auf die erste Beschreibung von Unix zurück, die Dennis Ritchie und Ken Thompson 1974 veröffentlichten. Dort ist ein Verzeichniseintrag nichts als ein Name und eine Zahl, die „i-number“, kurz für index number. Die Zahl ist ein Index in eine Tabelle an einer festen Stelle des Datenträgers, und der Eintrag in dieser Tabelle, der die Datei beschreibt, heißt „i-node“. Die Autoren nannten diese Tabelle selbst eine ungewöhnliche Eigenheit ihres Systems. Heutige Dateisysteme wie ext4 legen Inodes geschickter ab, aber die Idee ist geblieben: Die Datei wird über eine Nummer verwaltet, der Name ist nur ein Wegweiser zu dieser Nummer.
:::

### Das Verzeichnis als Tabelle

<span class="anker" id="stufe-8-2"></span>

Unterabschnitt [1.3](dateien-verzeichnisse-und-der-verzeichnisbaum.html#stufe-1-3) hat das Verzeichnis als Liste beschrieben, die Namen mit Dateien verbindet. Mit der Inode lässt sich genau sagen, woraus diese Verbindung besteht.

:::abbildung linux/k3tabelle 30
Das Verzeichnis `rezepte` als Tabelle mit zwei Spalten, Name und Inode-Nummer. Der Eintrag `.` trägt die eigene Nummer von `rezepte`, der Eintrag `..` die Nummer des übergeordneten Verzeichnisses, `kuchen` und `suppen` die Nummern ihrer Unterverzeichnisse. Pfeile führen von jeder Nummer zur passenden Inode.
:::

:::satz Satz 8.2 (Verzeichniseintrag)
<span class="anker" id="satz-8-2"></span>

Ein Eintrag in einem Verzeichnis besteht aus einem Namen und einer Inode-Nummer. Größe, Besitzer und alle übrigen Angaben stehen in der Inode, auf die die Nummer zeigt.
:::

Viele Dateisysteme, auch ext4, legen im Eintrag zusätzlich die Art ab, Datei oder Verzeichnis, damit Programme sie schneller erfahren; maßgeblich bleibt die Inode. Ein Dateiname ist also kein Merkmal der Datei, sondern ein Eintrag in einer Tabelle, der auf sie zeigt. Auch `.` und `..` sind solche Einträge: `.` zeigt auf die Inode des Verzeichnisses selbst, `..` auf die des übergeordneten. Abbildung [30](#abb-30) zeichnet ein Verzeichnis als Tabelle.

::::beispiel Nummern vergleichen
```console
$ ls -ai rezepte
95355 .  95352 ..  95359 kuchen  95360 suppen
$ ls -id rezepte rezepte/kuchen rezepte/suppen
95355 rezepte  95359 rezepte/kuchen  95360 rezepte/suppen
$ ls -ai rezepte/kuchen
95359 .  95355 ..  95362 apfelkuchen.txt  95363 kaesekuchen.txt
```

In `rezepte` trägt `.` die Nummer 95355, dieselbe wie `rezepte` selbst. In `rezepte/kuchen` trägt `..` die Nummer 95355: Es zeigt zurück auf `rezepte`. Die Sondernamen aus Unterabschnitt [2.5](das-arbeitsverzeichnis-und-pfade.html#stufe-2-5) sind also gewöhnliche Einträge mit passender Nummer.
::::

⁠**Kurz gesagt:** Ein Verzeichnis ist eine Tabelle aus Namen und Inode-Nummern; ein Dateiname ist nur ein Eintrag, der auf eine Inode zeigt.

:::hintergrund Warum ls -l mehr Arbeit hat als ls
Weil ein Verzeichnis im Wesentlichen nur Namen und Nummern enthält, kann `ls` ohne Optionen die Namen direkt aus der Tabelle lesen. Für `ls -l` reicht das nicht: Größe, Besitzer und Zeitpunkt stehen in den Inodes, also muss `ls` für jeden Eintrag zusätzlich dessen Inode abfragen. Bei einem Verzeichnis mit hunderttausend Dateien merkt man den Unterschied. Auch die Auflösung eines Pfads aus Unterabschnitt [2.5](das-arbeitsverzeichnis-und-pfade.html#stufe-2-5) lässt sich jetzt genau beschreiben: Der Kernel liest im Wurzelverzeichnis den Eintrag `usr` und erhält eine Inode-Nummer, liest in dieser Inode, wo die Tabelle von `usr` liegt, sucht darin den nächsten Namen, und so fort bis zum letzten. Ohne Nachschlagen kennt er nur zwei Inodes: die des Wurzelverzeichnisses und die des Arbeitsverzeichnisses. Dort beginnt jede Auflösung.
:::

### Der harte Link

<span class="anker" id="stufe-8-3"></span>

Wenn ein Name nur ein Eintrag ist, der auf eine Inode zeigt, liegt eine Frage nahe: Können zwei Einträge auf dieselbe Inode zeigen? Sie können, und das hat nützliche Folgen.

:::abbildung linux/k3hartlink 31
Ein zweiter Name für dieselbe Datei. `ln einkauf.txt liste.txt` legt einen zweiten Eintrag an, der auf dieselbe Inode zeigt, und der Zähler der Namen in der Inode springt von 1 auf 2. Nach `rm einkauf.txt` ist nur der erste Eintrag weg; der Zähler fällt auf 1, die Daten bleiben.
:::

:::definition Definition 8.3 (harter Link, Linkzähler)
<span class="anker" id="satz-8-3"></span>

Ein __harter Link__ ist ein weiterer Verzeichniseintrag für eine vorhandene Inode, also ein zusätzlicher Name für dieselbe Datei. Der Befehl `ln ziel name` legt ihn an. Die Inode zählt mit, wie viele Einträge auf sie zeigen; diese Zahl heißt __Linkzähler__.
:::

Nach `ln` gibt es keinen Unterschied mehr zwischen dem alten und dem neuen Namen: Beide sind gleichberechtigte Einträge, keiner ist das „Original“. Wer die Datei über den einen Namen ändert, sieht die Änderung über den anderen, denn es ist dieselbe Inode mit denselben Datenblöcken. Jetzt lässt sich auch die Zahl in der zweiten Spalte von `ls -l` lesen, die Unterabschnitt [3.4](den-inhalt-eines-verzeichnisses-anzeigen.html#stufe-3-4) offengelassen hat: Es ist der Linkzähler.

::::beispiel Zwei Namen, eine Liste
```console
$ ln einkauf.txt liste.txt
$ ls -li einkauf.txt liste.txt
95361 -rw-r--r-- 2 student student 25 Nov 10 02:41 einkauf.txt
95361 -rw-r--r-- 2 student student 25 Nov 10 02:41 liste.txt
```

Beide Namen tragen die Inode-Nummer 95361 und den Linkzähler 2. Öffne jetzt `nano liste.txt`, füge die Zeile `Butter` an und speichere. Dann zeigt der andere Name den neuen Inhalt:

```console
$ cat einkauf.txt
Milch
Brot
Äpfel
Kaffee
Butter
```
::::

**Der Linkzähler eines Verzeichnisses.** Ein Verzeichnis hat immer mindestens zwei Namen: seinen Eintrag im übergeordneten Verzeichnis und seinen eigenen Eintrag `.`. Dazu kommt für jedes Unterverzeichnis dessen Eintrag `..`, der ebenfalls auf es zeigt. Der Linkzähler eines Verzeichnisses ist deshalb 2 plus die Zahl seiner Unterverzeichnisse:

```console
$ ls -ld rezepte rezepte/kuchen
drwxr-xr-x 4 student student 4096 Nov 10 02:42 rezepte
drwxr-xr-x 2 student student 4096 Nov 10 02:41 rezepte/kuchen
```

`rezepte` hat zwei Unterverzeichnisse, also $2 + 2 = 4$; `kuchen` hat keines, also 2. Das `/etc` des Testrechners mit dem Zähler 93 aus Unterabschnitt [3.4](den-inhalt-eines-verzeichnisses-anzeigen.html#stufe-3-4) hat demnach 91 Unterverzeichnisse.

⁠**Kurz gesagt:** Ein harter Link ist ein zweiter Name für dieselbe Inode; der Linkzähler in der zweiten Spalte von `ls -l` zählt die Namen.

### Löschen heißt einen Namen entfernen

<span class="anker" id="stufe-8-4"></span>

Wenn eine Datei zwei gleichberechtigte Namen hat, was löscht dann `rm`? Die Antwort erklärt nebenbei, warum es an der Kommandozeile keinen Papierkorb gibt.

:::satz Satz 8.4 (Löschen)
<span class="anker" id="satz-8-4"></span>

`rm` entfernt nur den genannten Verzeichniseintrag und verringert den Linkzähler der Inode um 1. Erst wenn der Zähler 0 ist und kein laufendes Programm die Datei mehr geöffnet hat, gibt das Dateisystem die Inode und ihre Datenblöcke frei.
:::

Solange noch ein Name übrig ist, ist die Datei also nicht gelöscht, nur um einen Namen ärmer. Abbildung [31](#abb-31) zeigt das am Ende ihrer Animation.

::::beispiel Den ersten Namen löschen
```console
$ rm einkauf.txt
$ ls -li liste.txt
95361 -rw-r--r-- 1 student student 32 Nov 10 02:42 liste.txt
$ cat liste.txt
Milch
Brot
Äpfel
Kaffee
Butter
```

Der Name `einkauf.txt` ist weg, die Liste ist unter `liste.txt` vollständig da; der Linkzähler ist auf 1 gefallen. Die Größe ist jetzt 32 Bytes, weil `Butter` mit Zeilenende sieben Bytes dazugebracht hat.
::::

**mv behält die Inode.** Auch `mv` arbeitet nur mit Einträgen, wie der Hintergrund in Unterabschnitt [6.3](kopieren-verschieben-loschen.html#stufe-6-3) gesagt hat. Die Inode-Nummer bestätigt das:

```console
$ ls -i liste.txt
95361 liste.txt
$ mv liste.txt einkauf.txt
$ ls -i einkauf.txt
95361 einkauf.txt
```

Die Datei heißt wieder `einkauf.txt` und ist dieselbe Inode wie zuvor; kein Byte ihres Inhalts wurde bewegt.

⁠**Kurz gesagt:** `rm` entfernt einen Namen; die Datei verschwindet erst mit ihrem letzten Namen.

:::hintergrund Warum rm keinen Papierkorb hat
Der Systemaufruf hinter `rm` heißt nicht „delete“, sondern `unlink`: einen Verweis lösen. Das kann man selbst nachprüfen. Das Werkzeug `strace` zeigt die Systemaufrufe eines Programms; mit `-e trace=` beschränkt man die Anzeige auf bestimmte:

```console
$ touch muell.txt
$ strace -e trace=unlink,unlinkat rm muell.txt
unlinkat(AT_FDCWD, "muell.txt", 0)      = 0
+++ exited with 0 +++
```

`rm` ruft genau einmal `unlinkat` auf, die heutige Form von `unlink`, und das Ergebnis 0 heißt Erfolg. Der Kernel streicht den Eintrag und zählt den Linkzähler herunter; ist er bei 0, markiert das Dateisystem Inode und Blöcke als frei. Einen Zwischenschritt „in den Papierkorb“ gibt es auf dieser Ebene nicht, und genau diese Ebene benutzt `rm`. Die Bytes werden dabei übrigens nicht überschrieben, sondern nur zur Wiederverwendung freigegeben. Manchmal lassen sich deshalb Reste gelöschter Dateien wiederfinden; verlassen kann man sich darauf nicht, denn der Platz wird bei nächster Gelegenheit neu belegt. Die Ausnahme für geöffnete Dateien hat einen praktischen Grund: Ein Programm, das gerade aus einer Datei liest, soll nicht mitten im Lesen ins Leere greifen. Die Daten bleiben, bis es die Datei schließt.
:::

### Der symbolische Link

<span class="anker" id="stufe-8-5"></span>

Ein harter Link ist ein vollwertiger Name. Für den Alltag braucht man oft etwas anderes: einen Wegweiser, der auf eine Datei oder ein Verzeichnis zeigt, ohne selbst die Datei zu sein, ähnlich einer Verknüpfung unter Windows.

:::abbildung linux/k3symlink 32
Ein symbolischer Link ist eine eigene kleine Datei, in der ein Pfad steht. `zettel.txt` enthält den Text `einkauf.txt`; wer `zettel.txt` öffnet, wird zu `einkauf.txt` umgeleitet. Verschwindet das Ziel, steht der Pfad weiter im Link, führt aber ins Leere.
:::

:::definition Definition 8.5 (symbolischer Link)
<span class="anker" id="satz-8-5"></span>

Ein __symbolischer Link__ ist eine eigene Datei der Art `l`, deren einziger Inhalt ein Pfad ist. Fast jeder Zugriff auf den Link wird zu dem Ort umgeleitet, den dieser Pfad bezeichnet. Der Befehl `ln -s ziel name` legt ihn an.
:::

Ein relativer Pfad im Link gilt vom Verzeichnis des Links aus, nicht vom Arbeitsverzeichnis dessen, der ihn anlegt. Das Ziel muss nicht existieren; dann führt der Link ins Leere, und man nennt ihn verwaist. `ls -l` zeigt den Link mit `l` in der ersten Spalte und dem Pfad nach einem Pfeil `->`; seine Größe ist die Länge dieses Pfads in Bytes. `ls -F` hängt ein `@` an seinen Namen. `rm` löscht den Link selbst, nie sein Ziel.

::::beispiel Ein Wegweiser zur Einkaufsliste
```console
$ ln -s einkauf.txt zettel.txt
$ ls -li einkauf.txt zettel.txt
95361 -rw-r--r-- 1 student student 32 Nov 10 02:42 einkauf.txt
95257 lrwxrwxrwx 1 student student 11 Nov 10 02:42 zettel.txt -> einkauf.txt
$ cat zettel.txt
Milch
Brot
Äpfel
Kaffee
Butter
$ ls -F
einkauf.txt  fotos/  rezepte/  zettel.txt@
```

Der Link hat eine eigene Inode, 95257, und ist 11 Bytes groß, so lang wie der Text `einkauf.txt`. Der Linkzähler der Einkaufsliste bleibt 1: Ein symbolischer Link ist kein weiterer Name der Datei. `cat` liest durch den Link hindurch die Liste.
::::

::::beispiel [Zweites Beispiel] Ein relativer Pfad am falschen Ort
Derselbe Link soll in `rezepte` liegen:

```console
$ ln -s einkauf.txt rezepte/zettel.txt
$ cat rezepte/zettel.txt
cat: rezepte/zettel.txt: No such file or directory
$ ls -l rezepte/zettel.txt
lrwxrwxrwx 1 student student 11 Nov 10 02:42 rezepte/zettel.txt -> einkauf.txt
$ rm rezepte/zettel.txt
$ ln -s ../einkauf.txt rezepte/zettel.txt
$ cat rezepte/zettel.txt
Milch
Brot
Äpfel
Kaffee
Butter
```

Der erste Link enthält `einkauf.txt` und sucht die Datei deshalb in `rezepte`, wo es sie nicht gibt; `ln` hat das nicht geprüft. Der zweite enthält `../einkauf.txt`, vom Ort des Links aus eine Ebene höher, und funktioniert.
::::

::::beispiel [Drittes Beispiel] Ein verwaister Link und ein Link auf ein Verzeichnis
```console
$ touch entwurf.txt
$ ln -s entwurf.txt aktuell.txt
$ rm entwurf.txt
$ ls -l aktuell.txt
lrwxrwxrwx 1 student student 11 Nov 10 02:42 aktuell.txt -> entwurf.txt
$ cat aktuell.txt
cat: aktuell.txt: No such file or directory
```

Nach dem Löschen des Ziels steht der Link unverändert da und zeigt ins Leere. Nützlicher ist ein Link auf ein Verzeichnis, etwa auf das Fotoverzeichnis des laufenden Jahres:

```console
$ ln -s fotos/urlaub/2026 urlaub
$ ls urlaub
berge  notiz.txt  strand_1.jpg  strand_10.jpg  strand_2.jpg
$ ls -l urlaub
lrwxrwxrwx 1 student student 17 Nov 10 02:42 urlaub -> fotos/urlaub/2026
```

Nächstes Jahr löscht man den Link und legt ihn neu auf `fotos/urlaub/2027` an; alles, was über `urlaub` arbeitet, landet dann im neuen Jahr.
::::

⁠**Kurz gesagt:** Ein symbolischer Link ist eine kleine Datei mit einem Pfad darin; er leitet Zugriffe um und kann ins Leere zeigen, wenn das Ziel fehlt.

### Ein symbolischer Link im System: /bin

<span class="anker" id="stufe-8-6"></span>

[Kapitel 2, Abschnitt 3.3](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/arten-von-befehlen.html#stufe-3-3) hat gesagt, `/bin` sei auf Ubuntu nur ein zweiter Name für `/usr/bin`. Jetzt lässt sich genau sagen, was für ein Name das ist; Abbildung [33](#abb-33) zeigt den Schritt von früher zu heute.

:::abbildung linux/k3usrmerge 33
Die Verschmelzung von `/bin` mit `/usr/bin`. Früher zwei Verzeichnisse mit eigenen Programmen; heute ist `/bin` ein symbolischer Link mit dem Inhalt `usr/bin`, und jeder Pfad über `/bin` endet im selben Verzeichnis. Ebenso `/sbin` und `/lib`.
:::

:::definition Definition 8.6 (usr-merge)
<span class="anker" id="satz-8-6"></span>

Die __usr-merge__, die Verschmelzung von `/usr`, ist die heute übliche Anordnung, in der die Verzeichnisse `/bin`, `/sbin` und `/lib` symbolische Links auf `usr/bin`, `usr/sbin` und `usr/lib` sind. Alle Programme und Bibliotheken liegen dann unter `/usr`.
:::

Die Links bleiben, damit alte Pfade wie `/bin/bash`, die in unzähligen Programmen und Anleitungen stehen, weiter funktionieren. Fedora hat die Verschmelzung 2012 eingeführt, Debian verlangt sie seit Fassung 12 von 2023, und Ubuntu 26.04 hat sie ebenfalls. Der FHS von 2015 beschreibt noch getrennte Verzeichnisse.

::::beispiel Die Links nachsehen
```console
$ ls -ld /bin /sbin /lib
lrwxrwxrwx 1 root root 7 Apr 20  2026 /bin -> usr/bin
lrwxrwxrwx 1 root root 7 Apr 20  2026 /lib -> usr/lib
lrwxrwxrwx 1 root root 8 Apr 20  2026 /sbin -> usr/sbin
$ ls -l /etc/os-release
lrwxrwxrwx 1 root root 21 Aug 24 12:33 /etc/os-release -> ../usr/lib/os-release
```

Die Links enthalten relative Pfade: `usr/bin` gilt vom Ort des Links aus, also von `/` aus, und führt nach `/usr/bin`. Auch `/etc/os-release`, das [Kapitel 2](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/die-shell-erste-befehle.html) gelesen hat, ist ein Link, hier auf eine Datei unter `/usr/lib`.
::::

⁠**Kurz gesagt:** `/bin`, `/sbin` und `/lib` sind heute symbolische Links nach `/usr`; alte Pfade funktionieren weiter.

:::hintergrund Warum es einmal /bin und /usr/bin gab
Die Trennung stammt aus einer Zeit, in der Datenträger klein waren. Was man zum Starten und Reparieren des Systems brauchte, lag auf dem ersten Datenträger unter `/bin`, `/sbin` und `/lib`; alles Übrige lag auf einem zweiten, der unter `/usr` eingehängt wurde. Heute fassen Datenträger ein Vielfaches, und wo `/usr` doch einmal auf einem eigenen Datenträger liegt, hängt das System ihn schon ganz am Anfang des Startvorgangs ein. Der ursprüngliche Grund gilt also nicht mehr. Dafür hat die Zusammenlegung Vorteile: Alles, was die Distribution liefert, liegt unter einem einzigen Verzeichnis, das man als Ganzes schreibschützen, sichern oder mehreren Rechnern bereitstellen kann, und Skripte finden ein Programm unter beiden Pfaden.
:::

### Harte und symbolische Links im Vergleich

<span class="anker" id="stufe-8-7"></span>

Beide Arten von Links geben einer Datei einen weiteren Zugang, aber auf grundverschiedene Weise. Tabelle [3](#tab-3) stellt sie nebeneinander.

<span class="anker" id="tab-3"></span>

**Tabelle 3:** Harte und symbolische Links.

|  | harter Link | symbolischer Link |
|---|---|---|
| was er ist | ein weiterer Eintrag für dieselbe Inode | eine eigene Datei mit einem Pfad darin |
| eigene Inode | nein | ja |
| Linkzähler des Ziels | steigt um 1 | bleibt gleich |
| Ziel gelöscht | Daten bleiben über den Link erreichbar | Link zeigt ins Leere |
| auf Verzeichnisse | nicht erlaubt | erlaubt |
| in ein anderes Dateisystem | nicht möglich | möglich |
| in `ls -l` | wie jede gewöhnliche Datei, Linkzähler größer als 1 | Art `l`, Pfeil auf das Ziel |
| angelegt mit | `ln ziel name` | `ln -s ziel name` |

Zwei Zeilen der Tabelle sind Verbote für harte Links. Ein harter Link auf ein Verzeichnis ist nicht erlaubt, und ein harter Link kann nicht in ein anderes Dateisystem führen. Auf dem Testsystem liegt `/tmp` in einem eigenen Dateisystem im Arbeitsspeicher (Unterabschnitt [7.6](die-verzeichnisstruktur-von-linux.html#stufe-7-6)); ein harter Link dorthin scheitert deshalb:

::::beispiel Zwei verbotene harte Links
```console
$ ln rezepte rezepte2
ln: rezepte: hard link not allowed for directory
$ ln einkauf.txt /tmp/einkauf.txt
ln: failed to create hard link 'einkauf.txt' => '/tmp/einkauf.txt': Invalid cross-device link
```

„Invalid cross-device link“ heißt: Verweis über die Grenze eines Dateisystems, nicht erlaubt; „device“ steht hier für das Dateisystem. Die GNU-Fassung von `ln` meldet dasselbe, nennt die beiden Pfade aber in umgekehrter Reihenfolge, zuerst den neuen Namen. Die Reihenfolge oben ist ein Stand der uutils-Fassung 0.8 in Ubuntu 26.04.
::::

⁠**Kurz gesagt:** Ein harter Link ist ein gleichberechtigter Name derselben Inode, nur im selben Dateisystem und nur für Dateien; ein symbolischer Link ist ein Wegweiser, der überall hin zeigen darf, auch ins Leere.

:::hintergrund Warum harte Links diese Grenzen haben
Die Grenze zwischen Dateisystemen folgt direkt aus der Inode-Nummer: Sie ist nur innerhalb eines Dateisystems eindeutig. Ein Eintrag in einem Verzeichnis des einen Dateisystems kann nicht auf eine Inode eines anderen zeigen, weil die Nummer dort etwas ganz anderes bedeuten würde. Ein symbolischer Link enthält dagegen einen Pfad, und ein Pfad darf über jede Grenze führen. Das Verbot für Verzeichnisse schützt den Baum. Dürfte ein Verzeichnis einen harten Link auf ein höheres Verzeichnis enthalten, entstünde ein Kreis, und jedes Programm, das den Baum Ebene für Ebene durchläuft, könnte darin endlos kreisen. Schon die Erfinder von Unix nannten einen zweiten Grund: Mit beliebigen Links auf Verzeichnisse ließe sich kaum noch feststellen, wann ein Teilbaum keine Verbindung zur Wurzel mehr hat, also unerreichbar geworden ist, obwohl sein Linkzähler noch nicht 0 ist. Nur die Einträge `.` und `..` legt das System selbst an, und an ihnen erkennt es, wie der Baum aufgebaut ist.
:::

### Aufgaben zu Abschnitt [8](#stufe-8)

<span class="anker" id="stufe-8-8"></span>

:::aufgabe Aufgabe 27 ★★ Das Links-Experiment
<span class="anker" id="aufg-27"></span>

Lege in einem neuen Verzeichnis `links` mit nano eine Datei `original.txt` mit der Zeile `Zeile eins` an. Erzeuge darauf einen harten Link `hart.txt` und einen symbolischen Link `weich.txt`. (a) Vergleiche Inode-Nummern und Linkzähler mit `ls -li` und mit `stat -c "%i %h %n" original.txt hart.txt weich.txt`. (b) Lösche `original.txt` und lies beide Links mit `cat`. Erkläre jedes Ergebnis mit Abbildung [31](#abb-31) und Abbildung [32](#abb-32). Entferne das Verzeichnis danach.

:::loesung
```console
$ cd links
$ ln original.txt hart.txt
$ ln -s original.txt weich.txt
$ ls -li
total 8
95388 -rw-r--r-- 2 student student 11 Nov 10 02:42 hart.txt
95388 -rw-r--r-- 2 student student 11 Nov 10 02:42 original.txt
95389 lrwxrwxrwx 1 student student 12 Nov 10 02:42 weich.txt -> original.txt
$ stat -c "%i %h %n" original.txt hart.txt weich.txt
95388 2 original.txt
95388 2 hart.txt
95389 1 weich.txt
$ rm original.txt
$ cat hart.txt
Zeile eins
$ cat weich.txt
cat: weich.txt: No such file or directory
$ ls -li
total 4
95388 -rw-r--r-- 1 student student 11 Nov 10 02:42 hart.txt
95389 lrwxrwxrwx 1 student student 12 Nov 10 02:42 weich.txt -> original.txt
$ cd ..
$ rm -r links
```

(a) `original.txt` und `hart.txt` haben dieselbe Inode-Nummer und den Linkzähler 2: zwei Einträge für eine Inode. `weich.txt` hat eine eigene Inode mit dem Linkzähler 1 und ist 12 Bytes groß, so lang wie der Text `original.txt`. `stat -c` gibt nur die gewünschten Angaben aus: `%i` die Inode-Nummer, `%h` den Linkzähler, `%n` den Namen. (b) Nach `rm original.txt` ist ein Eintrag weg, der Zähler fällt auf 1, und die Daten sind über `hart.txt` vollständig lesbar (Abbildung [31](#abb-31)). `weich.txt` enthält weiter den Pfad `original.txt`, doch unter diesem Namen gibt es nichts mehr; der Link ist verwaist (Abbildung [32](#abb-32)). Die Inode-Nummern auf deinem Rechner sind andere.
:::
:::

:::aufgabe Aufgabe 28 ★ Wie viele Namen hat ein Verzeichnis?
<span class="anker" id="aufg-28"></span>

Sage voraus, welchen Linkzähler `ls -ld fotos/urlaub/2026` zeigt, nachdem du in Unterabschnitt [6.6](kopieren-verschieben-loschen.html#stufe-6-6) darin das Verzeichnis `berge` angelegt hast. Welche Einträge zeigen auf diese Inode? Prüfe am Rechner.

:::loesung
Vorhersage: 3. Auf die Inode von `fotos/urlaub/2026` zeigen der Eintrag `2026` in `fotos/urlaub`, der Eintrag `.` in `2026` selbst und der Eintrag `..` in `berge`, also $2 + 1$:

```console
$ ls -ld fotos/urlaub/2026
drwxr-xr-x 3 student student 4096 Nov 10 02:42 fotos/urlaub/2026
```
:::
:::

:::aufgabe Aufgabe 29 ★★ Kopie, Umbenennung, Link
<span class="anker" id="aufg-29"></span>

Du tippst nacheinander `cp einkauf.txt kopie.txt`, `mv kopie.txt neu.txt` und `ln neu.txt hart.txt`. Welche der Namen `einkauf.txt`, `neu.txt` und `hart.txt` haben am Ende dieselbe Inode-Nummer? Begründe mit dem, was jeder Befehl in den Verzeichnissen ändert, und prüfe mit `ls -i`. Lösche danach `neu.txt` und `hart.txt`.

:::loesung
`cp` legt eine neue Datei an, also eine neue Inode: `kopie.txt` hat eine andere Nummer als `einkauf.txt`. `mv` hängt nur den Eintrag um, die Inode bleibt: `neu.txt` hat die Nummer von `kopie.txt`. `ln` legt einen zweiten Eintrag für dieselbe Inode an: `hart.txt` hat dieselbe Nummer wie `neu.txt`.

```console
$ cp einkauf.txt kopie.txt
$ mv kopie.txt neu.txt
$ ln neu.txt hart.txt
$ ls -i einkauf.txt neu.txt hart.txt
95361 einkauf.txt  95387 hart.txt  95387 neu.txt
$ rm neu.txt hart.txt
```

`neu.txt` und `hart.txt` teilen die Inode 95387, `einkauf.txt` hat ihre eigene.
:::
:::

:::aufgabe Aufgabe 30 ★★★ Was cp mit einem Link macht
<span class="anker" id="aufg-30"></span>

Kopiere den symbolischen Link `zettel.txt` einmal mit `cp zettel.txt zettel_kopie.txt` und einmal mit `cp -P zettel.txt zettel_link.txt`. Vergleiche die drei Einträge mit `ls -l`. Was hat `cp` jeweils kopiert, den Link oder sein Ziel? Warum ist das Verhalten ohne `-P` für die meisten Zwecke das richtige?

:::loesung
```console
$ cp zettel.txt zettel_kopie.txt
$ cp -P zettel.txt zettel_link.txt
$ ls -l zettel.txt zettel_kopie.txt zettel_link.txt
lrwxrwxrwx 1 student student 11 Nov 10 02:42 zettel.txt -> einkauf.txt
-rw-r--r-- 1 student student 32 Nov 10 02:43 zettel_kopie.txt
lrwxrwxrwx 1 student student 11 Nov 10 02:43 zettel_link.txt -> einkauf.txt
$ rm zettel_kopie.txt zettel_link.txt
```

Ohne `-P` ist `cp` dem Link gefolgt und hat sein Ziel kopiert: `zettel_kopie.txt` ist eine gewöhnliche Datei mit den 32 Bytes der Einkaufsliste. Mit `-P` (kurz für „no dereference“, nicht folgen) hat es den Link selbst kopiert: `zettel_link.txt` ist wieder ein Link mit dem Inhalt `einkauf.txt`. Das Verhalten ohne Option passt zu dem, was man meist will: Wer eine Datei kopiert, will ihren Inhalt aufheben. Ein kopierter Link enthielte nur einen Pfad, und ein relativer Pfad kann am neuen Ort ins Leere führen, wie das zweite Beispiel in Unterabschnitt [8.5](#stufe-8-5) gezeigt hat.
:::
:::

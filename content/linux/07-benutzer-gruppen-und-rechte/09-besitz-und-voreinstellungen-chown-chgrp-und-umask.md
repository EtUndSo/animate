---
title: Besitz und Voreinstellungen: chown, chgrp und umask
pfad: Informatik / Linux und Kommandozeile / Benutzer, Gruppen und Rechte
adresse: informatik/linux-und-kommandozeile/benutzer-gruppen-und-rechte
knoten: Kapitel 7: Benutzer, Gruppen und Rechte
order: 6120900
summary: Bisher gehörten alle Dateien demjenigen, der sie angelegt hat, und bekamen ihre Rechte wie von selbst.
tags: umask
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Bisher gehörten alle Dateien demjenigen, der sie angelegt hat, und bekamen ihre Rechte wie von selbst. Dieser Abschnitt zeigt, wie man Besitzer und Gruppe einer Datei ändert, und woher die Rechte neuer Dateien kommen.
:::

### Den Besitzer ändern: chown

<span class="anker" id="stufe-8-1"></span>

Manchmal soll eine Datei jemand anderem gehören, etwa wenn du eine Datei für `anna` vorbereitest, die sie danach allein pflegen soll.

:::definition Definition 8.1 (chown)
<span class="anker" id="satz-8-1"></span>

`chown benutzer datei …` (englisch „change owner“) macht den genannten Benutzer zum Besitzer der Dateien. `chown benutzer:gruppe datei` ändert zugleich die Gruppe. Den Besitzer einer Datei darf unter Linux nur root ändern.
:::

```console
$ chown anna einkauf.txt
chown: changing ownership of 'einkauf.txt': Operation not permitted (os error 1)
$ sudo chown anna einkauf.txt
$ ls -l einkauf.txt
-rw-r--r-- 1 anna student 25 Nov 10 12:32 einkauf.txt
$ echo Butter >> einkauf.txt
bash: einkauf.txt: Permission denied
$ head -n 1 einkauf.txt
Milch
```

Ohne `sudo` lehnt der Kernel ab, auch wenn dir die Datei gehört; der Zusatz `(os error 1)` ist eine Eigenheit der uutils-Fassung in Ubuntu 26.04. Mit `sudo` gehört die Liste danach `anna`, die Gruppe bleibt `student`. Für `student` ist sie jetzt eine Datei der eigenen Gruppe: Er darf mit `r--` lesen, aber nichts mehr anhängen.

Wem welche Dateien gehören, findet `find` mit dem Test `-user` heraus, eine Ergänzung zu den Tests aus [Kapitel 3, Abschnitt 10](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-finden-und-platz-messen.html#stufe-10):

```console
$ find . -user anna
./einkauf.txt
$ sudo chown student einkauf.txt
```

Danach gehört die Liste wieder `student`.

⁠**Kurz gesagt:** `chown name datei` ändert den Besitzer, `chown name:gruppe` zugleich die Gruppe; das darf nur root.

:::hintergrund Warum nur root Dateien verschenken darf
Ältere Unix-Systeme erlaubten jedem Besitzer, seine Dateien anderen zu schenken. Linux erlaubt es nur root. Die Handbuchseite des Systemaufrufs nennt die Regel, die Gründe sind eine eigene Herleitung. Wer Dateien verschenken könnte, könnte anderen große Dateien unterschieben, deren Speicherplatz dann jenen angerechnet würde, oder es so aussehen lassen, als hätte jemand anderes eine Datei angelegt. Indem nur root den Besitzer ändert, bleibt die Zuordnung „wer hat das angelegt“ verlässlich.
:::

### Für den Kernel zählt die Nummer

<span class="anker" id="stufe-8-2"></span>

Unterabschnitt [2.1](die-rechte-einer-datei.html#stufe-2-1) hat gezeigt, dass in der Inode nur Nummern stehen. Was geschieht, wenn eine Nummer zu keinem Namen gehört?

:::satz Satz 8.2 (Besitzer ohne Namen)
<span class="anker" id="satz-8-2"></span>

Besitzer und Gruppe einer Datei sind Nummern, ganz gleich, ob es zu ihnen einen Eintrag in `/etc/passwd` oder `/etc/group` gibt. Fehlt der Eintrag, zeigt `ls -l` die Nummer selbst.
:::

```console
$ sudo chown 2000:2000 einkauf.txt
$ ls -l einkauf.txt
-rw-r--r-- 1 2000 2000 25 Nov 10 12:32 einkauf.txt
$ sudo chown student:student einkauf.txt
$ ls -l einkauf.txt
-rw-r--r-- 1 student student 25 Nov 10 12:32 einkauf.txt
```

Auf dem Testsystem gibt es keinen Benutzer und keine Gruppe mit der Nummer 2000. Der Kernel hat die Zahlen trotzdem ohne Einwand eingetragen, und `ls` fand keinen Namen und schrieb die Zahl.

⁠**Kurz gesagt:** Für den Kernel ist ein Benutzer eine Zahl; ein Name ist nur ein Eintrag in einer Datei, der auch fehlen kann.

:::hintergrund Warum der Kernel mit Nummern statt Namen arbeitet
Eine Zahl hat eine feste, kleine Größe; eine Benutzernummer belegt im Kernel vier Bytes, und zwei solche Zahlen vergleicht der Prozessor in einem Schritt. Namen wären verschieden lang und müssten Zeichen für Zeichen verglichen werden, bei jedem Zugriff. Dazu kommt ein Vorteil, der eine eigene Herleitung ist: Weil die Dateien nur die Nummer kennen, kann man einen Benutzer umbenennen, indem man eine Zeile in `/etc/passwd` ändert, ohne eine einzige Datei anzufassen.
:::

### Die Gruppe ändern: chgrp

<span class="anker" id="stufe-8-3"></span>

Um eine Datei mit einer Gruppe zu teilen, ändert man ihre Gruppe. Das ist weniger heikel als den Besitzer zu ändern, deshalb darf es auch der Besitzer selbst, mit einer Einschränkung.

:::definition Definition 8.3 (chgrp)
<span class="anker" id="satz-8-3"></span>

`chgrp gruppe datei …` (englisch „change group“) gibt den Dateien eine neue Gruppe. Der Besitzer darf das, aber nur für Gruppen, zu denen er selbst gehört; root darf jede Gruppe vergeben.
:::

Ein Rezept soll dem Kochclub gehören. `student` selbst gehört nicht zum Kochclub:

```console
$ printf 'Pfannkuchen: 3 Eier, 250 g Mehl\n' > rezept.txt
$ chgrp kochclub rezept.txt
chgrp: changing group of 'rezept.txt': Operation not permitted (os error 1)
$ sudo chgrp kochclub rezept.txt
$ ls -l rezept.txt
-rw-r--r-- 1 student kochclub 32 Nov 10 12:33 rezept.txt
```

Ohne `sudo` darf `student` die Gruppe `kochclub` nicht vergeben, denn er gehört nicht dazu. Mit `sudo` gehört das Rezept dem Kochclub, der Besitzer bleibt `student`.

::::beispiel Besitzer und Gruppe mit einem Befehl
`chown` kann beides zugleich, mit einem Doppelpunkt dazwischen:

```console
$ sudo chown anna:kochclub rezept.txt
$ ls -l rezept.txt
-rw-r--r-- 1 anna kochclub 32 Nov 10 12:33 rezept.txt
$ sudo chown student rezept.txt
$ ls -l rezept.txt
-rw-r--r-- 1 student kochclub 32 Nov 10 12:33 rezept.txt
```

`anna:kochclub` setzt beides, `student` allein nur den Besitzer; die Gruppe bleibt dann, wie sie ist. `:kochclub` mit Doppelpunkt am Anfang würde nur die Gruppe setzen, wie `chgrp`.
::::

⁠**Kurz gesagt:** `chgrp gruppe datei` ändert die Gruppe; der Besitzer darf nur eigene Gruppen vergeben, root jede.

### Die Voreinstellung für neue Dateien: umask

<span class="anker" id="stufe-8-4"></span>

Jede neue Datei hatte bisher `rw-r--r--`, jedes neue Verzeichnis `rwxr-xr-x`, ohne dass du etwas eingestellt hättest. Irgendjemand entscheidet das. Es sind zwei Beteiligte: das Programm, das die Datei anlegt, und eine Einstellung des Prozesses.

:::definition Definition 8.4 (umask)
<span class="anker" id="satz-8-4"></span>

Ein Programm, das eine Datei anlegt, verlangt dabei Rechte: Die Shell bei einer Umleitung und `touch` verlangen `rw-rw-rw-` (666), `mkdir` verlangt `rwxrwxrwx` (777). Die __umask__ eines Prozesses ist eine Maske aus neun Bits; jedes Recht, dessen Bit in der umask gesetzt ist, nimmt der Kernel von den verlangten Rechten weg. Der Befehl `umask` zeigt die Maske als Oktalzahl, `umask -S` zeigt die Rechte, die übrig bleiben dürfen.
:::

Das Handbuch von bash nennt sie „user file-creation mask“, die Maske des Benutzers für neue Dateien; daher der Name.

```console
$ umask
0022
$ umask -S
u=rwx,g=rx,o=rx
$ touch neu.txt
$ mkdir neuordner
$ ls -ld neu.txt neuordner
-rw-r--r-- 1 student student    0 Nov 10 12:33 neu.txt
drwxr-xr-x 2 student student 4096 Nov 10 12:33 neuordner
```

Die umask ist 022; die führende Null davor kannst du hier überlesen. 022 heißt: Die Gruppe verliert `w` (2), alle anderen verlieren `w` (2), der Besitzer verliert nichts (0). Aus den verlangten 666 wird so 644, aus 777 wird 755. Das zeigt auch `umask -S`: Gruppe und andere behalten höchstens `rx`. Zeigt `umask` bei dir 0002, verlieren nur die anderen das `w`: Aus 666 wird 664, aus 777 wird 775.

::::beispiel Die Rechnung Bit für Bit
Abbildung [23](#abb-23) rechnet für `touch` nach. Die verlangten Rechte 666 sind die Bits `110 110 110`, die umask 022 ist `000 010 010`. An jeder Stelle, an der die umask eine 1 hat, wird das Ergebnis 0; an allen anderen Stellen bleibt das verlangte Bit stehen. Heraus kommt `110 100 100`, also 644.

:::abbildung linux/k7umask 23
Rechenbild in drei Spaltengruppen u, g, o. Erste Zeile: verlangt 666 = `110 110 110`. Zweite Zeile: umask 022 = `000 010 010`. Dritte Zeile: die umask umgekehrt (`111 101 101`), die Einsen der umask werden zu Nullen. Vierte Zeile: Bit für Bit „verlangt und umgekehrte umask“ = `110 100 100`. Unten: 644 = `rw-r--r--`. Daneben dieselbe Rechnung für `mkdir`: 777 → 755.
:::
::::

⁠**Kurz gesagt:** Programme verlangen beim Anlegen Rechte (meist 666 oder 777), und die umask nimmt die Bits weg, die in ihr gesetzt sind.

### Bits wegnehmen, nicht abziehen

<span class="anker" id="stufe-8-5"></span>

Bei 666 und 022 sieht die Rechnung aus wie eine Subtraktion: $666 - 022 = 644$. Das ist Zufall, und der Zufall endet, sobald die umask ein Bit enthält, das gar nicht verlangt war.

:::satz Satz 8.5 (Rechte einer neuen Datei)
<span class="anker" id="satz-8-5"></span>

Die Rechte einer neuen Datei sind die verlangten Rechte UND NICHT umask: Ein Bit ist im Ergebnis genau dann gesetzt, wenn es verlangt war und in der umask nicht gesetzt ist. Eine Subtraktion der Oktalzahlen liefert dasselbe nur, wenn jedes Bit der umask auch verlangt war.
:::

::::beispiel umask 033
Eine umask 033 nimmt Gruppe und anderen `w` und `x`. Mit `bash -c` aus [Kapitel 4](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/stroeme-umleitung-pipes-und-exit-status.html) probierst du sie in einer neuen Shell aus, ohne deine eigene umask zu ändern:

```console
$ bash -c 'umask 033; touch probe.txt'
$ ls -l probe.txt
-rw-r--r-- 1 student student 0 Nov 10 12:33 probe.txt
$ umask
0022
```

Die Datei hat 644, nicht $666 - 033 = 633$. Abbildung [24](#abb-24) zeigt, wo die Subtraktion falsch wird: Die umask will `x` wegnehmen, das gar nicht verlangt war. Beim Wegnehmen bleibt die 0 eine 0. Beim Abziehen der Bits $110 - 011$ muss man sich für die hinteren Stellen etwas von der vorderen borgen, und dabei verschwindet das `r`. 633 wäre `rw--wx-wx`, für eine Datei ein unsinniges Ergebnis. Deine eigene Shell hat danach weiterhin 0022, denn `umask 033` galt nur in der neuen bash.

:::abbildung linux/k7undnicht 24
Rechenbild in zwei Spalten. Links „wegnehmen“: verlangt 666 = `110 110 110`, umask 033 = `000 011 011`, Ergebnis Bit für Bit `110 100 100` = 644 = `rw-r--r--`. Rechts „abziehen“: $666 - 033$ ziffernweise = 633 = `110 011 011` = `rw--wx-wx`. Die Stellen, an denen sich beide unterscheiden, leuchten rot auf: In der Gruppe ist links `r` da und kein `x`, rechts ist es umgekehrt.
:::
::::

⁠**Kurz gesagt:** Die umask nimmt Bits weg (verlangt UND NICHT umask), sie subtrahiert nicht.

### Die umask einstellen

<span class="anker" id="stufe-8-6"></span>

Wer an privaten Dingen arbeitet, möchte vielleicht, dass neue Dateien von vornherein vor fremden Blicken geschützt sind. Dafür ändert man die umask, statt jeder Datei einzeln Rechte zu nehmen.

:::definition Definition 8.6 (umask setzen)
<span class="anker" id="satz-8-6"></span>

`umask ziffern` setzt die umask der laufenden Shell. Wie die Benutzernummer gehört die umask zu einem Prozess, und ein neuer Prozess erbt sie als Kopie; sie gilt also für alles, was die Shell danach startet, aber nicht für andere Terminals und nicht über das Ende der Shell hinaus.
:::

```console
$ umask 027
$ touch privat.txt
$ mkdir privatordner
$ ls -ld privat.txt privatordner
-rw-r----- 1 student student    0 Nov 10 12:34 privat.txt
drwxr-x--- 2 student student 4096 Nov 10 12:34 privatordner
$ umask 022
```

Mit 027 behält die Gruppe nur Lesen (und bei Verzeichnissen Hindurchgehen), alle anderen bekommen nichts. Danach setzt `umask 022` den Ausgangswert zurück.

Dauerhaft wird eine umask, wenn der Befehl in einer Startdatei wie `~/.bashrc` steht ([Kapitel 5, Abschnitt 6.4](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/startdateien-und-aliase.html#stufe-6-4)). Auf dem Testsystem zeigt das Terminal von WSL die umask 0022. Wer sich über die gewöhnliche Anmeldung von Ubuntu anmeldet, etwa an einem Desktop oder mit `su - name`, bekommt dort 0002: Weil jeder Benutzer eine eigene Gruppe hat, darf die Gruppe neue Dateien dort auch ändern, ohne dass Fremde davon profitieren.

⁠**Kurz gesagt:** `umask 027` setzt die Maske für die laufende Shell und alles, was sie startet; dauerhaft wird sie über eine Startdatei.

:::hintergrund Warum es die umask gibt
Das Programm, das eine Datei anlegt, weiß, was für eine Datei es ist; der Mensch, der es benutzt, weiß, wie vorsichtig er sein will. Die umask trennt diese beiden Entscheidungen. Ein Texteditor verlangt 666, weil ein Text kein Programm ist. Ein Compiler, der aus Quelltext ein startbares Programm macht, verlangt 777; auf dem Testsystem bekam ein so erzeugtes Programm deshalb ohne weiteres Zutun `rwxr-xr-x`. Die umask legt einmal für alle Programme fest, was davon die Gruppe und die anderen bekommen sollen. Dass die Voreinstellung so wichtig ist, hat einen menschlichen Grund: Kaum jemand ändert die Rechte seiner Dateien nachträglich. Der Grundsatz der sicheren Voreinstellung verlangt deshalb, dass schon der Anfangszustand nichts Unnötiges erlaubt ([Cybersecurity, Kapitel 1, Abschnitt 5.4](/wissen/informatik/cybersecurity/sicherheit-schutzziele-und-spielregeln/sicherheitsprinzipien-rechte-vergeben-und-prufen.html#stufe-5-4)).
:::

### Aufgaben zu Abschnitt [8](#stufe-8)

<span class="anker" id="stufe-8-7"></span>

:::aufgabe Aufgabe 19 ★★ umask vorhersagen
<span class="anker" id="aufg-19"></span>

Sage für die umask 022, 027, 077 und 002 voraus, welche Rechte eine neue Datei (mit `touch`) und ein neues Verzeichnis (mit `mkdir`) bekommen. Prüfe mit je einem Aufruf von `bash -c '…'`, damit deine eigene umask unverändert bleibt.

:::loesung
```console
$ bash -c 'umask 022; touch u022.txt; mkdir u022d'
$ bash -c 'umask 027; touch u027.txt; mkdir u027d'
$ bash -c 'umask 077; touch u077.txt; mkdir u077d'
$ bash -c 'umask 002; touch u002.txt; mkdir u002d'
$ ls -ld u0*
-rw-rw-r-- 1 student student    0 Nov 10 12:53 u002.txt
drwxrwxr-x 2 student student 4096 Nov 10 12:53 u002d
-rw-r--r-- 1 student student    0 Nov 10 12:53 u022.txt
drwxr-xr-x 2 student student 4096 Nov 10 12:53 u022d
-rw-r----- 1 student student    0 Nov 10 12:53 u027.txt
drwxr-x--- 2 student student 4096 Nov 10 12:53 u027d
-rw------- 1 student student    0 Nov 10 12:53 u077.txt
drwx------ 2 student student 4096 Nov 10 12:53 u077d
```

`touch` verlangt 666, `mkdir` 777. Die umask 022 nimmt Gruppe und anderen `w`: 644 und 755. 027 nimmt der Gruppe `w` und den anderen alles: 640 und 750. 077 nimmt Gruppe und anderen alles: 600 und 700. 002 nimmt nur den anderen `w`: 664 und 775. Die Muster `u0*` sortiert die Shell nach Zeichen, deshalb steht 002 vorn.
:::
:::

:::aufgabe Aufgabe 20 ★★ Abziehen oder wegnehmen
<span class="anker" id="aufg-20"></span>

(a) Berechne für `touch` mit der umask 002 und für `touch` mit der umask 077 das Ergebnis einmal durch Wegnehmen der Bits und einmal durch Abziehen der Oktalzahlen. (b) Bei welcher der beiden stimmen die Wege überein, und warum? (c) Welche umask-Ziffern lassen beim Anlegen einer Datei das Abziehen scheitern, und warum geht es bei `mkdir` immer gut?

:::loesung
(a) umask 002: Wegnehmen ergibt $666$ UND NICHT $002$ = `110 110 110` UND `111 111 101` = `110 110 100` = 664. Abziehen ergibt $666 - 002 = 664$. umask 077: Wegnehmen ergibt `110 110 110` UND `111 000 000` = `110 000 000` = 600. Abziehen ergibt in Oktalzahlen $666 - 077 = 567$, also `r-xrw-rwx`, ein unsinniges Ergebnis. (b) Bei 002 stimmen beide überein, weil das einzige Bit der umask, `w` für andere, auch verlangt war; dann ist Wegnehmen dasselbe wie Abziehen. Bei 077 will die umask auch die `x`-Bits wegnehmen, die `touch` gar nicht verlangt hat, und beim Abziehen muss man sich deshalb etwas borgen. (c) Gefährlich sind die ungeraden Ziffern 1, 3, 5 und 7, denn sie enthalten das x-Bit, das eine Datei mit 666 nicht hat. Bei `mkdir` sind alle 777 Bits verlangt; jedes Bit der umask ist also auch verlangt, und Abziehen gibt immer dasselbe wie Wegnehmen.
:::
:::

:::aufgabe Aufgabe 21 ★★ Eine Datei an root verschenken
<span class="anker" id="aufg-21"></span>

Lege `probe.txt` mit den Rechten 640 an und gib sie mit `sudo chown root probe.txt` an root. (a) Zu welcher Klasse gehört `student` danach für diese Datei? (b) Kann `student` sie lesen, ergänzen, löschen? Sage voraus und prüfe.

:::loesung
```console
$ sudo chown root probe.txt
$ ls -l probe.txt
-rw-r----- 1 root student 0 Nov 10 12:52 probe.txt
$ cat probe.txt
$ echo x >> probe.txt
bash: probe.txt: Permission denied
$ rm probe.txt
rm: remove write-protected regular empty file 'probe.txt'? y
$ ls probe.txt
ls: cannot access 'probe.txt': No such file or directory
```

(a) Die Datei gehört root, ihre Gruppe ist weiterhin `student`. `student` ist nicht mehr Besitzer, aber Mitglied der Gruppe, also gilt für ihn die Klasse Gruppe mit `r--`. (b) Lesen klappt (`cat` meldet keinen Fehler, die Datei ist leer), Anhängen nicht, denn `w` fehlt. Löschen klappt nach der Rückfrage von `rm`, denn das Verzeichnis gehört `student`.
:::
:::

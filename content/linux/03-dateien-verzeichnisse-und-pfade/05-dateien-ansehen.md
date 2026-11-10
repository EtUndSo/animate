---
title: Dateien ansehen
pfad: Informatik / Linux und Kommandozeile / Dateien, Verzeichnisse und Pfade
adresse: informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade
knoten: Kapitel 3: Dateien, Verzeichnisse und Pfade
order: 6080500
summary: Viele Dateien eines Linux-Systems sind Text, den man direkt lesen kann: Einstellungen, Protokolle, Anleitungen.
tags: Textdatei, Zeilenende, cat, less, head, tail, wc, file
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Viele Dateien eines Linux-Systems sind Text, den man direkt lesen kann: Einstellungen, Protokolle, Anleitungen. Dieser Abschnitt erklärt, was eine Textdatei ausmacht, und zeigt die Werkzeuge, mit denen man Dateien ganz, seitenweise, am Anfang oder am Ende ansieht, sie vermisst und ihre Art bestimmt.
:::

### Was du dafür brauchst: die Textdatei

<span class="anker" id="stufe-4-1"></span>

Die Werkzeuge dieses Abschnitts arbeiten mit Zeilen und Zeichen. Dazu muss klar sein, wie Zeilen und Zeichen in einer Datei aus Bytes stecken.

**Zeichen als Zahlen.** Unterabschnitt [1.2](dateien-verzeichnisse-und-der-verzeichnisbaum.html#stufe-1-2) hat gezeigt, dass jedes Zeichen als Zahl gespeichert ist. Die Regel, nach der Linux heute Zeichen in Bytes übersetzt, heißt UTF-8. Für die Buchstaben ohne Akzent, die Ziffern und die üblichen Satzzeichen braucht UTF-8 genau ein Byte je Zeichen. Für Umlaute, Akzente und andere Schriften braucht es zwei bis vier Bytes; das `Ä` etwa wird zu den beiden Bytes 195 und 132.

:::abbildung linux/k3text 13
Eine Textdatei mit zwei Zeilen als Folge von Bytes. Nach jeder Zeile steht das Byte 10, das Zeilenende; ein Umlaut belegt zwei Bytes. Darunter dieselben Bytes so, wie ein Programm sie als Text anzeigt.
:::

:::definition Definition 4.1 (Textdatei, Zeilenende)
<span class="anker" id="satz-4-1"></span>

Eine __Textdatei__ ist eine Datei, deren Bytes ausschließlich Zeichen darstellen. Sie ist in Zeilen gegliedert: Am Ende jeder Zeile steht das unsichtbare Zeichen __Zeilenende__, das Byte mit dem Wert 10, das man in Programmen oft als `\n` schreibt.
:::

Was man eine Zeile nennt, ist also alles bis einschließlich eines Zeilenendes. Abbildung [13](#abb-13) zeigt eine kleine Textdatei als Bytes. Eine Datei, die nicht nur aus Zeichen besteht, etwa ein Foto oder ein Programm, nennt man im Gegensatz dazu eine Binärdatei.

::::beispiel Die Zeitzone als Zeichen
`od -c` zeigt jedes Byte als Zeichen; das Zeilenende erscheint als `\n`:

```console
$ od -An -c /etc/timezone
   E   u   r   o   p   e   /   B   e   r   l   i   n  \n
```

Die Datei hat eine einzige Zeile mit 13 Zeichen und dem Zeilenende, zusammen 14 Bytes.
::::

⁠**Kurz gesagt:** Eine Textdatei besteht nur aus Zeichen; jede Zeile endet mit dem Byte 10.

### Den ganzen Inhalt zeigen: cat

<span class="anker" id="stufe-4-2"></span>

Für eine kurze Datei genügt es, den ganzen Inhalt auf einmal ins Terminal zu schreiben. Dafür gibt es den einfachsten Befehl dieses Abschnitts.

:::definition Definition 4.2 (cat)
<span class="anker" id="satz-4-2"></span>

Der Befehl __cat__ liest die Dateien, die als Argumente genannt sind, der Reihe nach und schreibt ihre Bytes unverändert hintereinander aus.
:::

Der Name kommt von „concatenate“, aneinanderhängen: Mit mehreren Argumenten hängt `cat` die Inhalte Byte für Byte aneinander, ohne etwas dazwischenzusetzen. Für lange Dateien ist `cat` unpraktisch, denn der Anfang rauscht am oberen Rand des Fensters vorbei.

::::beispiel Zwei Dateien hintereinander
```console
$ cat /etc/hostname /etc/timezone
labor
Europe/Berlin
```

Weil jede der beiden Dateien mit einem Zeilenende aufhört, stehen die Inhalte auf zwei Zeilen.
::::

⁠**Kurz gesagt:** `cat` schreibt den Inhalt von Dateien hintereinander aus; für kurze Dateien ist das der schnellste Blick hinein.

:::warnung Keine Binärdateien mit cat ausgeben
`cat` schreibt auch die Bytes eines Programms oder Fotos ins Terminal. Manche dieser Bytes sind für das Terminal Steuerbefehle; danach zeigt es womöglich nur noch seltsame Zeichen. Gegen diesen Zustand hilft der Befehl `reset`, den du blind tippst und mit der Eingabetaste abschickst, oder ein neues Fenster. Eine Datei, deren Inhalt du nicht kennst, gibst du deshalb nicht blind mit `cat` aus.
:::

### Seitenweise lesen: less

<span class="anker" id="stufe-4-3"></span>

Eine lange Datei liest man besser wie ein Buch, Seite für Seite, mit der Möglichkeit, zurückzublättern und nach einem Wort zu suchen. Das leistet der Seitenanzeiger aus [Kapitel 2, Abschnitt 4.4](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/hilfe-finden.html#stufe-4-4).

:::definition Definition 4.3 (less mit einer Datei)
<span class="anker" id="satz-4-3"></span>

Bekommt __less__ eine Datei als Argument, zeigt es deren Inhalt seitenweise an. Es verändert die Datei nicht und lädt sie auch nicht auf einmal, deshalb öffnet es auch sehr große Dateien sofort.
:::

In `less` gelten dieselben Tasten wie bei den Handbuchseiten ([Kapitel 2, Abschnitt 4.4](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/hilfe-finden.html#stufe-4-4)). Merkt `less`, dass eine Datei keine Textdatei ist, fragt es nach, bevor es sie anzeigt.

::::beispiel Einen Lizenztext lesen
Tippe `less /usr/share/common-licenses/GPL-3`. Die erste Bildschirmseite der Lizenz erscheint, unten steht der Dateiname. Tippe `/Distribution` und die Eingabetaste, die Suche aus [Kapitel 2](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/die-shell-erste-befehle.html): `less` springt zur ersten Stelle mit diesem Wort und hebt es hervor. Mit `q` bist du zurück an der Eingabeaufforderung, und die Datei ist unverändert.
::::

⁠**Kurz gesagt:** `less datei` zeigt eine Datei seitenweise, mit Blättern und Suche, ohne sie zu verändern.

### Anfang und Ende: head und tail

<span class="anker" id="stufe-4-4"></span>

Bei vielen Dateien interessiert nur ein Stück: der Kopf mit einer Überschrift oder das Ende, an dem die neuesten Einträge eines Protokolls stehen.

:::abbildung linux/k3headtail 14
Eine Datei als Stapel von Zeilen. `head -n 3` hebt die ersten drei hervor, `tail -n 2` die letzten zwei; die Zeilen dazwischen bleiben grau.
:::

:::definition Definition 4.4 (head, tail)
<span class="anker" id="satz-4-4"></span>

Der Befehl __head__ schreibt die ersten Zeilen einer Datei aus, der Befehl __tail__ die letzten. Ohne Option sind es je zehn Zeilen; mit der Option `-n` und einer Zahl bestimmt man die Anzahl.
:::

`head -n 1` kennst du schon aus [Kapitel 2, Abschnitt 6.1](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/das-system-erkunden.html#stufe-6-1). Abbildung [14](#abb-14) zeigt, welche Zeilen die beiden Befehle aus derselben Datei herausgreifen.

::::beispiel Kopf einer Lizenz, Ende einer Benutzerliste
Die Datei `/etc/passwd` enthält in jeder Zeile einen Benutzer des Systems; wer zuletzt angelegt wurde, steht weit unten.

```console
$ head -n 3 /usr/share/common-licenses/GPL-3
                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

$ tail -n 2 /etc/passwd
student:x:1000:1000::/home/student:/bin/bash
tcpdump:x:986:986:tcpdump:/nonexistent:/usr/sbin/nologin
```

Die dritte Zeile der Lizenz ist leer; man sieht zwei Zeilen Text und eine leere Zeile. In der Benutzerliste stehen die Angaben durch Doppelpunkte getrennt; man erkennt den Namen `student` und das Heimatverzeichnis `/home/student`.
::::

::::beispiel [Zweites Beispiel] Die ersten zehn Zeilen
Ohne `-n` zeigt `head` zehn Zeilen. `/etc/os-release` hat dreizehn:

```console
$ head /etc/os-release
PRETTY_NAME="Ubuntu 26.04.1 LTS"
NAME="Ubuntu"
VERSION_ID="26.04"
VERSION="26.04.1 LTS (Resolute Raccoon)"
VERSION_CODENAME=resolute
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
```
::::

⁠**Kurz gesagt:** `head` zeigt den Anfang, `tail` das Ende einer Datei, je zehn Zeilen oder so viele, wie `-n` sagt.

### Zählen: wc

<span class="anker" id="stufe-4-5"></span>

Wie lang ist eine Datei? Je nach Zweck meint man damit Zeilen, Wörter oder Bytes. Ein Befehl liefert alle drei Zahlen auf einmal.

:::abbildung linux/k3wc 15
`wc` zählt an einem kleinen Text dreierlei: die Zeilenenden, die Wörter, also Folgen von Zeichen zwischen Leerraum, und die Bytes. Jede Zahl erscheint in ihrer eigenen Spalte.
:::

:::definition Definition 4.5 (wc)
<span class="anker" id="satz-4-5"></span>

Der Befehl __wc__ (kurz für „word count“) gibt für jede genannte Datei drei Zahlen aus: die Zahl der Zeilen, gezählt als Zahl der Zeilenenden, die Zahl der Wörter, also der Zeichenfolgen zwischen Leerzeichen, Tabulatoren und Zeilenenden, und die Zahl der Bytes. Mit `-l`, `-w` oder `-c` gibt er nur Zeilen, Wörter oder Bytes aus.
:::

Mehrere Dateien bekommen je eine Zeile, und am Ende steht eine Summe mit dem Wort `total`. Abbildung [15](#abb-15) zählt die drei Größen an einem kleinen Text nach.

::::beispiel Die Lizenz vermessen
```console
$ wc /usr/share/common-licenses/GPL-3
  674  5644 35149 /usr/share/common-licenses/GPL-3
$ wc -l /etc/passwd
28 /etc/passwd
$ wc -c /etc/hostname
6 /etc/hostname
```

Die Lizenz hat 674 Zeilen, 5644 Wörter und 35 149 Bytes; `ls -lh` hat dafür 35K gezeigt, aufgerundet aus 34,3 KiB. Auf dem Testrechner gibt es 28 Benutzerkonten. `/etc/hostname` hat die sechs Bytes aus Unterabschnitt [1.2](dateien-verzeichnisse-und-der-verzeichnisbaum.html#stufe-1-2).
::::

⁠**Kurz gesagt:** `wc` zählt Zeilen, Wörter und Bytes; `-l`, `-w`, `-c` wählen eine der Zahlen.

### Den Dateityp bestimmen: file

<span class="anker" id="stufe-4-6"></span>

Weil das System nicht festhält, was in einer Datei steht, und weil die Endung nur ein Teil des Namens ist, braucht man ein Werkzeug, das die Art einer Datei an ihrem Inhalt erkennt.

:::definition Definition 4.6 (file)
<span class="anker" id="satz-4-6"></span>

Der Befehl __file__ untersucht jede genannte Datei und beschreibt, was sie enthält, etwa Text, ein Bild in einem bestimmten Format, ein Programm oder ein Verzeichnis. Er urteilt nach dem Inhalt, nicht nach dem Namen.
:::

Zuerst prüft `file`, ob es sich um eine besondere Art wie ein Verzeichnis handelt. Dann vergleicht es die ersten Bytes mit einer langen Liste bekannter Kennungen, und erst zuletzt prüft es, ob die Bytes Text ergeben. Die erste Prüfung, die passt, liefert die Antwort. Abbildung [16](#abb-16) zeigt den mittleren Schritt.

:::abbildung linux/k3magie 16
Wie `file` eine Datei erkennt: Es liest die ersten Bytes und vergleicht sie mit bekannten Kennungen. Bei `/usr/bin/bash` passen die Bytes 127, `E`, `L`, `F` zur Kennung für Programme, beim Ubuntu-Logo die Bytes 137, `P`, `N`, `G` zur Kennung für PNG-Bilder; der Dateiname spielt keine Rolle.
:::

::::beispiel Drei Arten von Dateien
```console
$ file /etc/passwd /usr/bin/bash /etc
/etc/passwd:   ASCII text
/usr/bin/bash: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=a292b52b679fb438b940f1c17e2e4951ac52ac89, for GNU/Linux 3.2.0, stripped
/etc:          directory
$ file /usr/share/pixmaps/ubuntu-logo-text.png
/usr/share/pixmaps/ubuntu-logo-text.png: PNG image data, 187 x 72, 8-bit/color RGBA, non-interlaced
```

`/etc/passwd` ist Text aus dem ASCII-Zeichensatz, also nur Zeichen mit einem Byte. `/usr/bin/bash` ist ein Programm im Format ELF, dem Format für Programme unter Linux, übersetzt für 64-Bit-Prozessoren der Familie x86-64; der Name hat keine Endung, und trotzdem erkennt `file` es. Das Bild ist eine PNG-Grafik mit 187 mal 72 Bildpunkten.
::::

Damit hast du auch das Werkzeug für die Warnung aus Unterabschnitt [4.2](#stufe-4-2): Bevor du eine unbekannte Datei mit `cat` ausgibst, fragst du `file`, ob sie Text enthält.

⁠**Kurz gesagt:** `file` bestimmt die Art einer Datei aus ihrem Inhalt, unabhängig von Name und Endung.

:::hintergrund Woran file eine Datei erkennt
Viele Dateiformate beginnen mit einer festen Folge von Bytes, einer Art Kennung, die man magische Zahl nennt. Programme im Format ELF beginnen mit dem Byte 127 und den Buchstaben `E`, `L`, `F`; PNG-Bilder mit dem Byte 137 und den Buchstaben `P`, `N`, `G`. `od -c` zeigt das; Bytes, die kein druckbares Zeichen sind, schreibt es als Oktalzahl, also mit der Basis 8 statt 10 ($177_8 = 127$, $211_8 = 137$):

```console
$ od -An -c -N4 /usr/bin/bash
 177   E   L   F
$ od -An -c -N4 /usr/share/pixmaps/ubuntu-logo-text.png
 211   P   N   G
```

Die Option `-N4` liest nur die ersten vier Bytes. `file` hat eine Sammlung Tausender solcher Marken samt Regeln, welche weiteren Bytes es auswerten soll, etwa die Bildgröße bei PNG. Dass die Marke ganz am Anfang steht, hat einen praktischen Grund: Ein Programm muss nur wenige Bytes lesen, um zu wissen, ob es mit der Datei etwas anfangen kann. Auch der Kernel selbst prüft beim Start eines Programms die ersten Bytes, bevor er es ausführt.
:::

### Aufgaben zu Abschnitt [4](#stufe-4)

<span class="anker" id="stufe-4-7"></span>

:::aufgabe Aufgabe 11 ★ Welcher Befehl?
<span class="anker" id="aufg-11"></span>

Welchen Befehl aus diesem Abschnitt nimmst du, um (a) die letzten fünf Zeilen eines Protokolls zu sehen, (b) einen Text mit 2000 Zeilen in Ruhe zu lesen und darin ein Wort zu suchen, (c) herauszufinden, ob eine Datei namens `urlaub.jpg` wirklich ein Foto ist, (d) zu zählen, wie viele Zeilen eine Datei hat, (e) zwei kurze Dateien direkt nacheinander zu lesen?

:::loesung
(a) `tail -n 5 datei`. (b) `less datei`, darin `/wort` zum Suchen. (c) `file urlaub.jpg`; die Endung beweist nichts. (d) `wc -l datei`. (e) `cat datei1 datei2`.
:::
:::

:::aufgabe Aufgabe 12 ★★ Die Lizenz vermessen
<span class="anker" id="aufg-12"></span>

Arbeite mit `/usr/share/common-licenses/GPL-3`. (a) Wie viele Wörter stehen durchschnittlich in einer Zeile? (b) Zeige die letzten drei Zeilen. (c) Wie viele Bytes hat eine Zeile im Durchschnitt, das Zeilenende mitgezählt? (d) Warum stimmt die Zahl aus `wc -c` mit der Größe aus `ls -l` überein, aber nicht mit der aus `ls -lh`?

:::loesung
(a) $5644 / 674 \approx 8{,}37$ Wörter je Zeile; die Leerzeilen der Lizenz drücken den Schnitt.

(b) Die letzten drei Zeilen:

```console
$ tail -n 3 /usr/share/common-licenses/GPL-3
the library.  If this is what you want to do, use the GNU Lesser General
Public License instead of this License.  But first, please read
<https://www.gnu.org/licenses/why-not-lgpl.html>.
```

(c) $35\,149 / 674 \approx 52{,}1$ Bytes je Zeile, das Zeilenende mitgezählt.

(d) `wc -c` zählt die Bytes des Inhalts, und `ls -l` zeigt als Größe ebenfalls die Zahl der Bytes des Inhalts; beide sagen 35 149. `ls -lh` rechnet in Einheiten zu 1024 Byte um und rundet auf: $35\,149 / 1024 \approx 34{,}3$ wird zu `35K`.
:::
:::

:::aufgabe Aufgabe 13 ★★★ Die Art an den ersten Bytes erkennen
<span class="anker" id="aufg-13"></span>

Zeige mit `od -An -c -N2` die ersten beiden Bytes von `/usr/share/pixmaps/debian-logo.bmp`. Welche Buchstaben erscheinen? Prüfe dann mit `file`, um welches Format es sich handelt, und erkläre, warum ein Programm, das Bilder anzeigt, die Endung `.bmp` gar nicht bräuchte.

:::loesung
```console
$ od -An -c -N2 /usr/share/pixmaps/debian-logo.bmp
   B   M
$ file /usr/share/pixmaps/debian-logo.bmp
/usr/share/pixmaps/debian-logo.bmp: PC bitmap, Windows 98/2000 and newer format, 48 x 48 x 32, cbSize 9354, bits offset 138
```

Die Datei beginnt mit den Buchstaben `B` und `M`, der Kennung des Bildformats BMP; `file` nennt es „PC bitmap“ und liest aus den folgenden Bytes die Bildgröße von 48 mal 48 Bildpunkten. Ein Bildprogramm kann genauso vorgehen: die ersten Bytes lesen und an der Marke erkennen, welches Format vorliegt. Die Endung `.bmp` braucht es dafür nicht; sie hilft Menschen und Dateimanagern, die schon am Namen ein passendes Programm vorschlagen wollen, ohne die Datei zu öffnen.
:::
:::

---
title: Hilfe finden
pfad: Informatik / Linux und Kommandozeile / Die Shell: erste Befehle
adresse: informatik/linux-und-kommandozeile/die-shell-erste-befehle
knoten: Kapitel 2: Die Shell: erste Befehle
order: 6070500
summary: Niemand kennt alle Optionen aller Befehle, und das muss auch niemand.
tags: Kurzhilfe, help, Handbuchseite, man, Seitenanzeiger, Abschnitte, apropos
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Niemand kennt alle Optionen aller Befehle, und das muss auch niemand. Linux bringt zu fast jedem Befehl eine Anleitung mit, und zwar in drei Formen: eine Kurzhilfe des Programms, die Hilfe der Shell für eingebaute Befehle und ein ausführliches Handbuch mit Suchfunktion. Dieser Abschnitt zeigt alle drei und wann man welche nimmt.
:::

### Die Kurzhilfe

<span class="anker" id="stufe-4-1"></span>

Oft weiß man genau, welchen Befehl man braucht, hat aber eine Option vergessen. Dann reicht ein Spickzettel, der sich mit einem Blick lesen lässt.

:::definition Definition 4.1 (Kurzhilfe)
<span class="anker" id="satz-4-1"></span>

Die __Kurzhilfe__ ist eine knappe Beschreibung, die ein Programm ausgibt, wenn man es mit der Option `--help` aufruft. Sie nennt die Aufrufform und die Optionen mit je einer Zeile Erklärung; danach endet das Programm, ohne etwas anderes zu tun.
:::

::::beispiel Die Kurzhilfe von uname
```console
$ uname --help
Print certain system information.
With no OPTION, same as -s.

Usage: uname [OPTION]...

Options:
  -a, --all               Behave as though all of the options -mnrsvo were specified.
  -s, --kernel-name       print the kernel name.
  -n, --nodename          print the nodename (the nodename may be a name that the system is known by
                          to a communications network).
  -r, --kernel-release    print the operating system release.
  -v, --kernel-version    print the operating system version.
  -m, --machine           print the machine hardware name.
  -o, --operating-system  print the operating system name.
  -h, --help              Print help
  -V, --version           Print version
```

Jede Zeile nennt eine kurze Option und ihre lange Form. Die Zeile `Usage:` zeigt die Aufrufform: `uname`, dann beliebig viele Optionen. Auf anderen Linux-Systemen ist der Wortlaut etwas anders, die Optionen sind dieselben.
::::

⁠**Kurz gesagt:** `Befehl --help` zeigt die Optionen eines Programms auf einen Blick.

### Die Hilfe für eingebaute Befehle

<span class="anker" id="stufe-4-2"></span>

Eingebaute Befehle sind keine Programmdateien. Für sie gibt es meist auch keinen Eintrag im Handbuch, das der nächste Unterabschnitt vorstellt: `man cd` antwortet nur `No manual entry for cd`. Ihre Anleitung trägt die Shell selbst in sich.

:::definition Definition 4.2 (help)
<span class="anker" id="satz-4-2"></span>

Der eingebaute Befehl __help__ zeigt die Anleitung zu eingebauten Befehlen der Shell. Mit einem Namen als Argument beschreibt er diesen Befehl; mit der Option `-d` nur in einer Zeile; ohne Argument listet er alle eingebauten Befehle auf.
:::

::::beispiel Was cd, echo und type tun
```console
$ help -d cd echo type
cd - Change the shell working directory.
echo - Write arguments to the standard output.
type - Display information about command type.
$ help cd
cd: cd [-L|[-P [-e]]] [-@] [dir]
    Change the shell working directory.

    Change the current directory to DIR.  The default DIR is the value of the
...
```

Die erste Zeile von `help cd` zeigt die Aufrufform, die zweite den Zweck. Darunter folgen gut 30 weitere Zeilen mit allen Einzelheiten, die das Kapitel hier weglässt. In der Aufrufform stehen wahlweise Teile in eckigen Klammern; wie man sie liest, erklärt der nächste Unterabschnitt.
::::

⁠**Kurz gesagt:** Für eingebaute Befehle fragt man die Shell: `help` *Name*.

### Die Handbuchseite

<span class="anker" id="stufe-4-3"></span>

Die Kurzhilfe ist ein Spickzettel. Wer verstehen will, was ein Befehl genau tut, welche Dateien er liest und was seine Meldungen bedeuten, braucht die vollständige Anleitung. Unix-Systeme haben dafür seit über fünfzig Jahren ein eingebautes Handbuch, aufgeteilt in einzelne Seiten.

**Immer dieselbe Gliederung.** Jede Seite des Handbuchs ist gleich aufgebaut, damit man sich schnell zurechtfindet. Abbildung [14](#abb-14) zeigt den Aufbau an der Seite zu `uname`.

:::abbildung linux/k2manpage 14
Aufbau einer Handbuchseite am Beispiel `uname`: Kopfzeile mit Name und Abschnittsnummer, dann NAME, SYNOPSIS, DESCRIPTION, OPTIONS und weitere Teile in fester Reihenfolge.
:::

:::definition Definition 4.3 (Handbuchseite)
<span class="anker" id="satz-4-3"></span>

Eine __Handbuchseite__, englisch manual page oder kurz man page, ist die ausführliche Beschreibung eines Befehls, eines Dateiformats, eines Systemaufrufs oder eines anderen Teils des Systems, gesammelt im Handbuch, das jedes Linux mitbringt. Der Befehl __man__ mit dem Namen als Argument zeigt sie an.
:::

Die Teile einer Handbuchseite stehen immer in derselben Reihenfolge, allerdings hat nicht jede Seite alle:

<ul>

<li>

⁠**NAME:** Name und eine Zeile Beschreibung.

</li>

<li>

⁠**SYNOPSIS:** die Aufrufform.

</li>

<li>

⁠**DESCRIPTION:** was der Befehl tut, oft ausführlich.

</li>

<li>

⁠**OPTIONS:** jede Option mit Erklärung.

</li>

<li>

⁠**EXIT STATUS:** wie der Befehl Erfolg oder Misserfolg meldet.

</li>

<li>

⁠**FILES, ENVIRONMENT:** welche Dateien und Einstellungen er benutzt.

</li>

<li>

⁠**EXAMPLES:** Beispiele, leider nicht auf jeder Seite.

</li>

<li>

⁠**SEE ALSO:** verwandte Seiten.

</li>

</ul>

::::beispiel Die Seite zu uname
Ruft man `man uname` auf, füllt die Seite das Fenster. So beginnt sie in einem Fenster, das 81 Zeichen breit ist; in einem breiteren oder schmaleren Fenster bricht `man` die Zeilen anders um:

```text
UNAME(1)                     General Commands Manual                    UNAME(1)

NAME
       uname - Print certain system information.  With no OPTION, same as -s.

SYNOPSIS
       uname [-a|--all] [-s|--kernel-name] [-n|--nodename] [-r|--kernel-release]
       [-v|--kernel-version]  [-m|--machine] [-o|--operating-system] [-h|--help]
       [-V|--version]

DESCRIPTION
       Print certain system information.  With no OPTION, same as -s.

OPTIONS
       -a, --all
              Behave as though all of the options -mnrsvo were specified.

       -s, --kernel-name
              print the kernel name.

       -n, --nodename
              print the nodename (the nodename may be a name that the system  is
              known by to a communications network).
```

Die Kopfzeile nennt den Namen der Seite und in Klammern die Nummer des Teils des Handbuchs, in dem sie steht; davon handelt Unterabschnitt [4.5](#stufe-4-5).
::::

**Die Aufrufform lesen.** Die Zeile unter SYNOPSIS benutzt eine knappe Schreibweise, die auch in Kurzhilfen vorkommt. Abbildung [15](#abb-15) zeigt sie an zwei Beispielen.

<ul>

<li>

Was in **eckigen Klammern** steht, darf man weglassen.

</li>

<li>

Ein **senkrechter Strich** trennt Möglichkeiten, von denen man eine wählt: `[-a|--all]` heißt „`-a` oder `--all` oder keines von beiden“.

</li>

<li>

⁠**Drei Punkte** heißen: Das Vorige darf sich wiederholen. `[OPTION]...` steht für beliebig viele Optionen, auch keine.

</li>

<li>

Im Terminal ist **fett** gedruckter Text genau so zu tippen; **unterstrichener** oder in Großbuchstaben geschriebener Text wie `FILE` ist ein Platzhalter, den man durch etwas Passendes ersetzt, etwa einen Dateinamen.

</li>

</ul>

:::abbildung linux/k2synopsis 15
Zwei Aufrufformen gelesen: `uname [-a|--all] [-s|--kernel-name] …` und `cat [OPTION]... [FILE]...`. Eckige Klammern heißen „darf fehlen“, der senkrechte Strich „eines davon“, drei Punkte „darf sich wiederholen“, Großbuchstaben „hier etwas Passendes einsetzen“.
:::

⁠**Kurz gesagt:** `man` *Name* zeigt die vollständige Anleitung in fester Gliederung; die Aufrufform unter SYNOPSIS liest man mit den Zeichen `[ ]`, `|` und `...`.

:::hintergrund Woher die Handbuchseiten kommen
Am 3. November 1971 erschien die erste Ausgabe des „UNIX Programmer's Manual“ von Ken Thompson und Dennis Ritchie. Sie war bereits in nummerierte Teile gegliedert, vom Teil I mit den Befehlen über die Systemaufrufe bis zu den Dateiformaten, und jeder Eintrag hatte dasselbe Format mit Name, Aufrufform und Beschreibung. Schon damals hieß eine eckige Klammer in der Aufrufform „darf fehlen“ und drei Punkte „darf sich wiederholen“. Die Seiten entstanden aus einfachen Textdateien mit eingestreuten Formatierungsbefehlen, aus denen ein Programm die fertige Seite setzte, und so ist es bis heute: Jede Handbuchseite liegt als kleine, meist komprimierte Textdatei mit Formatierungsbefehlen in einem der Ordner `/usr/share/man/man1` bis `man8`, und `man` setzt sie beim Aufruf passend für die Breite deines Fensters. Weil das Format seit über fünfzig Jahren gleich geblieben ist, kann man eine Handbuchseite von heute mit dem Wissen von damals lesen. Nicht jede Seite ist leicht: Die Seite zu bash hat über 7 000 Zeilen.
:::

### Der Seitenanzeiger

<span class="anker" id="stufe-4-4"></span>

Schon die kurze Seite zu `uname` füllt das Fenster, und die meisten Handbuchseiten sind viel länger. Würde `man` eine Seite einfach ausgeben, liefe ihr Anfang oben aus dem Fenster, bevor man ihn lesen kann. Deshalb zeigt `man` die Seite nicht selbst an, sondern reicht sie an ein weiteres Programm weiter.

**Ein Buch, in dem man blättert.** Wie in einem Buch sieht man immer nur eine Seite, blättert vor und zurück und kann nach einem Wort suchen (ein Bild zur Orientierung). Der Text bleibt dabei, wie er ist; nur der Ausschnitt im Fenster wandert.

:::definition Definition 4.4 (Seitenanzeiger)
<span class="anker" id="satz-4-4"></span>

Ein __Seitenanzeiger__, englisch pager, ist ein Programm, das einen langen Text Bildschirmseite für Bildschirmseite zeigt und darin blättern und suchen lässt. `man` übergibt jede Handbuchseite einem Seitenanzeiger; unter Linux ist das meist das Programm `less`.
:::

Tabelle [2](#tab-2) nennt die wichtigsten Tasten von `less`. Nach `q` bist du wieder bei der Eingabeaufforderung.

<span class="anker" id="tab-2"></span>

**Tabelle 2:** Die wichtigsten Tasten im Seitenanzeiger `less`, in dem `man` die Handbuchseiten zeigt.

| Taste | Wirkung |
|---|---|
| Leertaste, Bild ab | eine Bildschirmseite weiter |
| `b`, Bild auf | eine Bildschirmseite zurück |
| Pfeiltasten | zeilenweise |
| `/`*wort* und Eingabetaste | vorwärts nach *wort* suchen |
| `n` bzw. `N` | nächster bzw. vorheriger Treffer |
| `g` bzw. `G` | an den Anfang bzw. an das Ende |
| `h` | Hilfe zu allen Tasten |
| `q` | beenden |

::::beispiel Eine Option in der Handbuchseite finden
Du suchst die Option von `uname`, die den Typ des Prozessors nennt, weißt aber nur das englische Wort „machine“. Tippe `man uname`, dann `/machine` und die Eingabetaste. Der Seitenanzeiger springt zum ersten Treffer und hebt ihn hervor; es ist schon die Zeile `[-m|--machine]` in SYNOPSIS. `n` springt zum nächsten Treffer, der Erklärung `-m, --machine` unter OPTIONS. `q` beendet die Anzeige.
::::

⁠**Kurz gesagt:** `man` zeigt seine Seiten im Seitenanzeiger `less`: Die Leertaste blättert, `/` sucht, `q` beendet.

### Die Abschnitte des Handbuchs

<span class="anker" id="stufe-4-5"></span>

Derselbe Name kann im System Verschiedenes bezeichnen. `uname` ist ein Befehl, aber auch der Name des Systemaufrufs, mit dem dieser Befehl den Kernel nach seinen Angaben fragt. Beide haben eine Handbuchseite, und das Handbuch muss sie auseinanderhalten.

:::abbildung linux/k2abschnitte 16
Das Handbuch als Regal mit nummerierten Fächern. Unter dem Namen `uname` liegt eine Seite im Fach 1 (Befehle) und eine im Fach 2 (Systemaufrufe), unter `passwd` eine im Fach 1 und eine im Fach 5 (Dateiformate).
:::

:::definition Definition 4.5 (Abschnitt des Handbuchs)
<span class="anker" id="satz-4-5"></span>

Das Handbuch ist in nummerierte __Abschnitte__ gegliedert, je einen für eine Art von Inhalt (Tabelle [3](#tab-3)). Man schreibt eine Seite mit ihrem Abschnitt als *Name*(*Nummer*), etwa `uname(1)` für den Befehl und `uname(2)` für den Systemaufruf. `man` mit einer Nummer vor dem Namen zeigt die Seite aus diesem Abschnitt; ohne Nummer zeigt es die erste, die es findet, und sucht dabei in einer festen Reihenfolge, die mit Abschnitt 1 beginnt.
:::

<span class="anker" id="tab-3"></span>

**Tabelle 3:** Die Abschnitte des Linux-Handbuchs. Für die Arbeit an der Kommandozeile braucht man vor allem 1, 5 und 8.

| Nr. | Inhalt | Beispiel |
|---|---|---|
| 1 | Befehle für alle Benutzer | `uname(1)`, `ls(1)` |
| 2 | Systemaufrufe des Kernels | `uname(2)`, `chdir(2)` |
| 3 | Funktionen von Programmbibliotheken | `printf(3)` |
| 4 | Gerätedateien | `null(4)` |
| 5 | Dateiformate | `passwd(5)`, `os-release(5)` |
| 6 | Spiele | `intro(6)` |
| 7 | Übersichten und Vereinbarungen | `man-pages(7)` |
| 8 | Befehle zur Systemverwaltung | `lsblk(8)` |

::::beispiel Zweimal uname, zweimal passwd
`whatis` nennt zu einem Namen die NAME-Zeile jeder passenden Seite, mit Abschnitt; `man -f` tut dasselbe:

```console
$ whatis uname
uname (1)            - Print certain system information. With no OPTION, same...
uname (2)            - get name and information about current kernel
$ man -f passwd
passwd (1)           - change user password
passwd (1ssl)        - OpenSSL application commands
passwd (5)           - the password file
```

`passwd(1)` ist der Befehl, mit dem man sein Passwort ändert, `passwd(5)` beschreibt die Datei `/etc/passwd`, in der das System seine Benutzerkonten verzeichnet. `1ssl` ist ein Unterabschnitt von 1 für die Befehle des Verschlüsselungsprogramms OpenSSL. Die Seite aus Abschnitt 5 bekommt man nur mit der Nummer:

```text
PASSWD(5)                File Formats and Configuration               PASSWD(5)

NAME
       passwd - the password file

DESCRIPTION
       /etc/passwd contains one line for each user account, with seven fields
       delimited by colons (“:”). These fields are:
```

Den Befehl dazu tippst du als `man 5 passwd`; `man passwd` allein zeigt die Seite aus Abschnitt 1.
::::

⁠**Kurz gesagt:** Das Handbuch hat nummerierte Abschnitte; `man 5 passwd` wählt die Seite aus Abschnitt 5, wenn ein Name mehrfach vorkommt.

### Die Suche im Handbuch

<span class="anker" id="stufe-4-6"></span>

`man` hilft nur, wenn man den Namen eines Befehls schon kennt. Oft weiß man aber nur, was man tun will: den freien Speicher anzeigen, den Namen des Rechners ändern. Dann braucht man eine Suche über alle Seiten.

:::abbildung linux/k2apropos 17
`apropos` durchsucht eine Datenbank aller NAME-Zeilen. Das Stichwort `host name` trifft zwei Zeilen; jede nennt Seite, Abschnitt und Kurzbeschreibung.
:::

:::definition Definition 4.6 (apropos)
<span class="anker" id="satz-4-6"></span>

Der Befehl __apropos__ durchsucht die Namen und Kurzbeschreibungen aller Handbuchseiten nach einem Stichwort und listet die Treffer mit ihrem Abschnitt auf. `man -k` tut dasselbe.
:::

Gesucht wird nur in der einen Zeile unter NAME, nicht im ganzen Text der Seiten, und die Zeilen sind englisch. Ein Stichwort aus mehreren Wörtern schreibt man in gerade Anführungszeichen, damit es als ein einziges Argument ankommt.

::::beispiel Befehle finden, deren Namen man nicht kennt
```console
$ apropos "host name"
hostname (1)         - show or set the system's host name
rust-hostname (1)    - Display or set the system's host name.
$ man -k "free and used"
free (1)             - Display amount of free and used memory in the system
$ apropos uptime
proc_uptime (5)      - system uptime
rust-uptime (1)      - Display the current time, the length of time the syste...
uptime (1)           - Tell how long the system has been running.
$ apropos xyzzy
xyzzy: nothing appropriate.
```

Die Treffer, deren Name mit `rust-` beginnt, sind eine Besonderheit von Ubuntu 26.04, das viele Grundbefehle in einer neu geschriebenen Fassung mitbringt; für die Suche liest du sie wie die Seite ohne `rust-`. Für die letzte Zeile gibt es keine Seite, deren Kurzbeschreibung das Wort enthält.
::::

⁠**Kurz gesagt:** `apropos` *Stichwort* findet Handbuchseiten, deren Kurzbeschreibung das Stichwort enthält.

:::hintergrund Warum apropos manchmal nichts findet
`apropos` liest nicht die Handbuchseiten selbst, das wäre bei Tausenden Seiten zu langsam. Es durchsucht eine kleine Datenbank, in der für jede Seite nur ihr Name, ihr Abschnitt und ihre Zeile unter NAME stehen. Diese Datenbank baut das Programm `mandb` auf, und Ubuntu bringt es nach jeder Installation neuer Programme auf den neuesten Stand. Daraus folgen drei Gründe für eine leere Suche: Das Stichwort steht zwar im Text, aber nicht in der Kurzbeschreibung, wie bei `disk usage`; es ist deutsch, während die Beschreibungen englisch sind; oder die Datenbank ist noch nicht auf dem neuesten Stand. Hilft ein Wort nicht, versucht man ein verwandtes, etwa `memory` statt `RAM`.
:::

### Welche Hilfe wofür

<span class="anker" id="stufe-4-7"></span>

Die drei Hilfen ergänzen sich. Welche passt, hängt davon ab, was du schon weißt und welche Art von Befehl du vor dir hast. Abbildung [18](#abb-18) fasst den Weg zusammen.

:::abbildung linux/k2hilfeweg 18
Welche Hilfe wofür: Kennst du den Namen nicht, suchst du mit `apropos`. Ist der Befehl eingebaut, fragst du `help`. Für eine Programmdatei genügt oft `--help`; die vollständige Anleitung zeigt `man`.
:::

::::beispiel Drei Fragen, drei Wege
Du willst wissen, wie lange der Rechner schon läuft, und kennst keinen Befehl dafür: `apropos uptime` oder `apropos running` führt zu `uptime(1)`. Du hast vergessen, wie `cd` in den vorigen Ordner zurückspringt: `type cd` sagt „builtin“, also `help cd`. Du suchst die Option von `head`, die die Zeilenzahl festlegt: `head --help` zeigt sie als zweiten Eintrag der Liste.
::::

⁠**Kurz gesagt:** Name unbekannt: `apropos`; eingebaut: `help`; Programmdatei: `--help` für den Überblick, `man` für alles.

### Aufgaben zu Abschnitt [4](#stufe-4)

<span class="anker" id="stufe-4-8"></span>

:::aufgabe Aufgabe 12 ★ Die passende Hilfe
<span class="anker" id="aufg-12"></span>

Welche Hilfe funktioniert für welchen Befehl: `man`, `--help` oder `help`? Probiere alle drei für `cd`, `uname`, `history` und `head` und halte fest, welche eine Antwort geben. Erkläre das Muster mit Abschnitt [3](arten-von-befehlen.html#stufe-3).

:::loesung
| Befehl | `man` | `--help` | `help` |
|---|---|---|---|
| `cd` | keine Seite | ja | ja |
| `uname` | ja | ja | nein |
| `history` | falsche Seite | ja | ja |
| `head` | ja | ja | nein |

Das Muster folgt aus Abschnitt [3](arten-von-befehlen.html#stufe-3). `cd` und `history` sind eingebaut, darum kennt `help` sie, und bash beantwortet bei eingebauten Befehlen auch `--help`. `uname` und `head` sind Programmdateien mit eigener Kurzhilfe und Handbuchseite; `help` kennt sie nicht und antwortet `no help topics match`. `man cd` findet nichts. `man history` zeigt dagegen eine Seite aus Abschnitt 3 über die Programmbibliothek, mit der Programme einen Verlauf verwalten, nicht den eingebauten Befehl. Das ist eine gute Erinnerung daran, bei einem eingebauten Befehl zuerst `help` zu fragen.
:::
:::

:::aufgabe Aufgabe 13 ★★ Eine Option im Handbuch finden
<span class="anker" id="aufg-13"></span>

Öffne `man ls`. Finde mit der Suche des Seitenanzeigers die Option, mit der `ls` die Dateien nach ihrer Größe sortiert. Welche Option zeigt Größen in gut lesbaren Einheiten wie `K` und `M`? Probiere `ls -S /etc` und vergleiche mit `ls /etc`.

:::loesung
Nach `man ls` tippst du `/size` und die Eingabetaste und springst mit `n` von Treffer zu Treffer. Unter OPTIONS steht:

```text
       -S     Sort by file size, largest first.
```

Die gut lesbaren Einheiten liefert `-h`, lang `--human-readable`: `Print human readable file sizes (e.g. 1K 234M 56G)`. Unter Ubuntu 26.04 ist das die Handbuchseite der uutils-Fassung; auf einem GNU-System lautet der Text anders, die Optionen `-S` und `-h` sind dieselben. `ls /etc` zeigt die Namen alphabetisch, `ls -S /etc` die größten zuerst.
:::
:::

:::aufgabe Aufgabe 14 ★★ Gleiche Namen, verschiedene Seiten
<span class="anker" id="aufg-14"></span>

(a) Was beschreiben `printf(1)` und `printf(3)`? Finde es mit `whatis`. (b) Warum zeigt `man printf` die Seite aus Abschnitt 1 und nicht die aus Abschnitt 3? (c) In welchem Abschnitt steht die Seite zu `os-release`, und was beschreibt sie?

:::loesung
(a)

```console
$ whatis printf
printf (1)           - Print output based off of the format string and procee...
printf (3)           - formatted output conversion
```

`printf(1)` ist ein Befehl, der Text nach einer Vorlage ausgibt; `printf(3)` ist eine Funktion der Programmbibliothek der Sprache C, die dasselbe innerhalb eines Programms tut.

(b) Ohne Nummer durchsucht `man` die Abschnitte in einer festen Reihenfolge, die mit Abschnitt 1 beginnt; Abschnitt 3 kommt erst später. Für die Seite aus Abschnitt 3 tippt man `man 3 printf`.

(c) `os-release(5)`, Kurzbeschreibung `Operating system identification`: Die Seite beschreibt den Aufbau der Datei `/etc/os-release` aus [Kapitel 1, Abschnitt 2.3](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/drei-wege-zu-einem-eigenen-linux.html#stufe-2-3), also eine Datei, deshalb Abschnitt 5.
:::
:::

:::aufgabe Aufgabe 15 ★★ Befehle suchen
<span class="anker" id="aufg-15"></span>

Finde mit `apropos` je einen Befehl, der (a) den Namen des Rechners anzeigt, (b) den belegten und freien Arbeitsspeicher zeigt, (c) die Datenträger als Liste zeigt. Notiere dein Stichwort. Warum findet `apropos festplatte` nichts?

:::loesung
```console
$ apropos "host name"
hostname (1)         - show or set the system's host name
rust-hostname (1)    - Display or set the system's host name.
$ man -k "free and used"
free (1)             - Display amount of free and used memory in the system
```

(a) `hostname`. (b) `free`; das Stichwort `memory` allein findet es auch, aber zwischen über hundert anderen Treffern. (c) `apropos "block devices"` führt zu `lsblk (8) - list block devices`; Datenträger heißen im Englischen der Linux-Welt block devices. `apropos festplatte` meldet `festplatte: nothing appropriate.`, weil `apropos` nur die englischen Kurzbeschreibungen durchsucht.
:::
:::

:::aufgabe Aufgabe 16 ★★★ Aufrufformen lesen
<span class="anker" id="aufg-16"></span>

Die Aufrufform von `head` lautet auf einem gewöhnlichen GNU-System `head [OPTION]... [FILE]...`. Welche der folgenden Zeilen passen zu dieser Form? (a) `head` (b) `head /etc/hostname /etc/os-release` (c) `head -n 1 -v /etc/hostname` (d) `head /etc/hostname -n 1`. Wie liest du `[-a|--all]` in der Aufrufform von `uname`, und darf man `uname -a --all` schreiben?

:::loesung
(a) passt: Optionen und Dateinamen sind beide in eckigen Klammern, dürfen also fehlen; ohne Dateinamen liest `head` dann, was du tippst. (b) passt: `[FILE]...` erlaubt beliebig viele Dateinamen. (c) passt: zwei Optionen, `-n` mit Wert und `-v`, dann ein Dateiname. (d) passt nicht zur Form, die Optionen vor die Dateinamen stellt; unter Linux funktioniert die Zeile trotzdem, weil die Auswertung der Optionen sie auch dahinter erlaubt.

`[-a|--all]` heißt: `-a` oder `--all` oder keines von beiden, aber nicht beide. uutils nimmt das wörtlich:

```console
$ uname -a --all
error: the argument '--all' cannot be used multiple times

For more information, try '--help'.
```

GNU `uname` ist großzügiger und gibt bei `gnuuname -a --all` einfach alle Angaben aus. Die Aufrufform beschreibt also, was sicher überall funktioniert.
:::
:::

Wer zusätzlich üben möchte, findet auf der Lernplattform pwn.college im Kurs „Linux Luminarium“ kurze Aufgaben, passend zu diesem Kapitel die Module „Hello Hackers“ und „Digesting Documentation“: [https://pwn.college/linux-luminarium/](https://pwn.college/linux-luminarium/).

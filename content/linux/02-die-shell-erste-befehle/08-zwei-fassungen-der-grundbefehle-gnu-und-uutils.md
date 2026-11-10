---
title: Zwei Fassungen der Grundbefehle: GNU und uutils
pfad: Informatik / Linux und Kommandozeile / Die Shell: erste Befehle
adresse: informatik/linux-und-kommandozeile/die-shell-erste-befehle
knoten: Kapitel 2: Die Shell: erste Befehle
order: 6070800
summary: Die meisten Befehle dieses Kapitels gehören zu einer Sammlung von Grundbefehlen, die jedes Linux-System mitbringt.
tags: coreutils, uutils coreutils, Vorsilbe gnu
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Die meisten Befehle dieses Kapitels gehören zu einer Sammlung von Grundbefehlen, die jedes Linux-System mitbringt. Ubuntu 26.04 liefert sie in einer neu geschriebenen Fassung aus und die bisherige zusätzlich. Dieser Abschnitt zeigt, woran man die beiden erkennt, wie man die bisherige aufruft und wo sie sich unterscheiden.
:::

### Die Grundbefehle: coreutils

<span class="anker" id="stufe-7-1"></span>

`uname`, `head`, `cat`, `date` und `ls` sind keine Einzelstücke von verschiedenen Herstellern, sondern stammen aus einer gemeinsamen Sammlung. Wer sie kennt, weiß, welche Befehle er auf jedem Linux-System erwarten darf. Abbildung [29](#abb-29) zeigt einen Ausschnitt.

:::abbildung linux/k2coreutils 29
Ein Ausschnitt aus der Sammlung der Grundbefehle, nach Aufgaben geordnet: Befehle für Dateien wie `ls` und `cp`, für Text wie `cat` und `head`, für Angaben über das System wie `uname`, `date` und `df`. Insgesamt sind es über hundert.
:::

:::definition Definition 7.1 (coreutils)
<span class="anker" id="satz-7-1"></span>

Die __coreutils__ („core utilities“, Kernwerkzeuge) sind eine Sammlung von über hundert grundlegenden Befehlen für Dateien, Text und Systemangaben, darunter `ls`, `cat`, `head`, `cp`, `uname`, `date` und `df`. Die klassische Fassung stammt vom GNU-Projekt und heißt GNU coreutils.
:::

Jede Linux-Distribution enthält eine Fassung der coreutils. Weil die GNU-Fassung seit Jahrzehnten der Standard ist, richten sich unzählige Anleitungen, Skripte und Hilfeforen nach ihrem Verhalten. Mit `--version` verrät jeder dieser Befehle, aus welcher Sammlung er stammt.

::::beispiel Wer hat cp geschrieben?
```console
$ cp --version
cp (GNU coreutils) 9.7
Packaged by Ubuntu (9.7-3ubuntu2)
Copyright (C) 2025 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by Torbjörn Granlund, David MacKenzie, and Jim Meyering.
```

Der Kopierbefehl `cp` stammt aus GNU coreutils in der Fassung 9.7, von Ubuntu als Paket zusammengestellt.
::::

⁠**Kurz gesagt:** Die coreutils sind die Sammlung der Grundbefehle; die klassische Fassung kommt vom GNU-Projekt.

:::hintergrund Woher die GNU coreutils kommen
Das GNU-Projekt begann 1983 damit, ein freies Unix-artiges Betriebssystem zu schreiben, Befehl für Befehl. Die Grundbefehle lagen lange in drei getrennten Paketen für Dateien, für Text und für die Shell; 2002 wurden sie zu den coreutils zusammengelegt. Zusammen mit dem Kernel Linux bilden diese Programme den Kern der Systeme, die [Kapitel 1, Abschnitt 1.5](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/betriebssystem-kernel-und-distribution.html#stufe-1-5) „GNU/Linux“ nennt, daher auch die Angabe `GNU/Linux` am Ende von `uname -a`.
:::

### uutils: die Neufassung in Rust

<span class="anker" id="stufe-7-2"></span>

Fragt man unter Ubuntu 26.04 `ls` nach seiner Fassung, kommt eine unerwartete Antwort:

```console
$ ls --version
ls (uutils coreutils) 0.8.0
```

Hier antwortet nicht die GNU-Fassung, sondern eine andere.

:::abbildung linux/k2zweifassungen 30
Zwei Werkzeugkästen auf einem Ubuntu 26.04. Unter den gewohnten Namen wie `ls`, `cat` und `uname` laufen die Befehle aus uutils; `cp`, `mv`, `rm` und `df` kommen noch aus GNU coreutils. Unter Namen mit der Vorsilbe `gnu` liegen alle GNU-Fassungen bereit.
:::

:::definition Definition 7.2 (uutils coreutils)
<span class="anker" id="satz-7-2"></span>

__uutils coreutils__, kurz uutils, ist eine Neufassung der coreutils in der Programmiersprache Rust, die sich so verhalten soll wie die GNU-Fassung. Das freie Projekt besteht seit 2013. Ubuntu benutzt es seit der Version 25.10 für die meisten Grundbefehle; in Ubuntu 26.04 kommen nur noch `cp`, `mv`, `rm`, `df` und `true` aus GNU coreutils.
:::

Andere Distributionen wie Debian, Fedora und Kali benutzen weiterhin die GNU-Fassung. Für fast alle Aufgaben ist das gleichgültig: Die Befehle heißen gleich, verstehen fast immer dieselben Optionen und liefern dieselben Ergebnisse. Unterschiede zeigen sich vor allem im Wortlaut von Hilfetexten und Fehlermeldungen.

::::beispiel Welcher Befehl kommt woher?
```console
$ uname --version
uname (uutils coreutils) 0.8.0
$ head --version
head (uutils coreutils) 0.8.0
$ df --version
df (GNU coreutils) 9.7
Packaged by Ubuntu (9.7-3ubuntu2)
Copyright (C) 2025 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by Torbjörn Granlund, David MacKenzie, and Paul Eggert.
```

`uname` und `head` aus diesem Kapitel sind uutils, `df` ist GNU.
::::

⁠**Kurz gesagt:** Ubuntu 26.04 benutzt für die meisten Grundbefehle uutils, eine Neufassung in Rust; `--version` zeigt, welche Fassung antwortet.

:::hintergrund Warum Ubuntu die Grundbefehle neu schreiben lässt
Die GNU coreutils sind in der Programmiersprache C geschrieben. C lässt dem Programm volle Kontrolle über den Arbeitsspeicher, und ein kleiner Fehler im Umgang damit kann ein Programm zum Absturz bringen oder zur Sicherheitslücke machen. Rust prüft schon beim Übersetzen des Programms, dass bestimmte Fehler dieser Art nicht vorkommen können. Canonical, die Firma hinter Ubuntu, begründete den Wechsel deshalb vor allem mit Sicherheit und Widerstandsfähigkeit; Geschwindigkeit sei nicht der Hauptgrund. Neuer Code bringt allerdings neue Fehler mit: Eine unabhängige Prüfung von uutils fand vor der Veröffentlichung von Ubuntu 26.04 über hundert Mängel unterschiedlicher Schwere, darunter Sicherheitslücken, die seither nach und nach behoben werden. `cp`, `mv` und `rm` blieben wegen noch offener Fehler vorerst bei GNU.
:::

:::hintergrund Ein Programm, viele Namen
uutils ist eine einzige Programmdatei von gut elf Megabyte, die unter über hundert Namen im System eingetragen ist: `/usr/bin/ls`, `/usr/bin/cat`, `/usr/bin/uname` und viele mehr führen alle zu ihr. Woher weiß sie, ob sie `ls` oder `date` spielen soll? Aus dem ersten Wort der Liste, die sie beim Start bekommt, also dem Namen, unter dem sie aufgerufen wurde (Hintergrund „Die Shell zerlegt, das Programm deutet“ in Unterabschnitt [2.3](der-aufbau-einer-befehlszeile.html#stufe-2-3)). Deshalb meldet `ls --version` den Namen `ls` und `uname --version` den Namen `uname`, obwohl dieselbe Datei antwortet. Man nennt ein solches Programm ein Multicall-Programm. Eine Kopie der Datei unter einem neuen, unbekannten Namen funktioniert deshalb nicht: Das Programm erkennt den Namen nicht und weiß nicht, welche Rolle es spielen soll.
:::

### Die GNU-Fassung aufrufen

<span class="anker" id="stufe-7-3"></span>

Manchmal verlangt eine Anleitung genau das Verhalten der GNU-Fassung, oder man will eine überraschende Ausgabe vergleichen. Dafür muss man an die GNU-Fassung herankommen, ohne das System umzubauen.

:::definition Definition 7.3 (Die Vorsilbe gnu)
<span class="anker" id="satz-7-3"></span>

Ubuntu 26.04 installiert die GNU-Fassung der coreutils zusätzlich, und zwar unter Namen mit der __Vorsilbe gnu__: `gnuls` ist das `ls` von GNU, `gnuuname` das `uname`, `gnudate` das `date` und so weiter.
:::

Auch zu diesen Namen gibt es Handbuchseiten: `man gnuls` zeigt die Seite der GNU-Fassung, `man ls` die der uutils-Fassung, die unter dem Namen `rust-ls` gespeichert ist; das erklärt die Treffer mit der Vorsilbe `rust-` bei `apropos` in Unterabschnitt [4.6](hilfe-finden.html#stufe-4-6). Auf Distributionen mit der GNU-Fassung gibt es die Namen mit `gnu` nicht; dort ist `ls` schon die GNU-Fassung.

::::beispiel Dasselbe ls, zweimal
```console
$ gnuls --version
ls (GNU coreutils) 9.7
Packaged by Ubuntu (9.7-3ubuntu2)
Copyright (C) 2025 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by Richard M. Stallman and David MacKenzie.
```

Die GNU-Fassung nennt sich selbst `ls`, nicht `gnuls`: Sie ist dasselbe Programm, das auf Debian oder Kali unter dem Namen `ls` liegt.
::::

⁠**Kurz gesagt:** Unter Ubuntu 26.04 erreicht man die GNU-Fassung jedes Grundbefehls mit der Vorsilbe `gnu`, etwa `gnuls`.

### Was sich unterscheidet

<span class="anker" id="stufe-7-4"></span>

Die beiden Fassungen sollen sich gleich verhalten, und bei gewöhnlicher Arbeit tun sie es auch. Wer genau hinsieht, findet aber Unterschiede an drei Stellen.

:::abbildung linux/k2fehlermeldung 31
Dieselbe falsche Option, zwei Antworten. Links die Fehlermeldung von uutils mit dem Wort `error` und einer Aufrufform, rechts die von GNU mit dem Hinweis auf `--help`. Beide bedeuten: Die Option `-x` gibt es nicht.
:::

<ul>

<li>

⁠**Fehlermeldungen.** uutils schreibt `error:` und oft einen Tipp, GNU nennt den Programmnamen und verweist auf `--help`.

</li>

<li>

⁠**Hilfetexte und Handbuchseiten.** Wortlaut und Aufbau unterscheiden sich, die Optionen sind dieselben.

</li>

<li>

⁠**Strenge in Randfällen.** uutils lehnt manches ab, was GNU stillschweigend hinnimmt, etwa dieselbe Option zweimal.

</li>

</ul>

::::beispiel Eine falsche Option, zwei Meldungen
```console
$ uname -x
error: unexpected argument '-x' found

Usage: uname [OPTION]...

For more information, try '--help'.
$ gnuuname -x
gnuuname: invalid option -- 'x'
Try 'gnuuname --help' for more information.
```

Auf Debian oder Kali sähe die zweite Meldung genauso aus, nur mit `uname` statt `gnuuname`. Wer eine Fehlermeldung in eine Suchmaschine tippt, sollte deshalb wissen, welche Fassung sie geschrieben hat.
::::

⁠**Kurz gesagt:** uutils und GNU liefern dieselben Ergebnisse, formulieren Hilfen und Fehlermeldungen aber verschieden.

### Aufgaben zu Abschnitt [7](#stufe-7)

<span class="anker" id="stufe-7-5"></span>

:::aufgabe Aufgabe 25 ★ Welche Fassung?
<span class="anker" id="aufg-25"></span>

Prüfe mit `--version`, aus welcher Sammlung `ls`, `cat`, `cp`, `rm`, `date` und `df` auf deinem System stammen. Passt das Ergebnis zur Definition in Unterabschnitt [7.2](#stufe-7-2)? Falls du kein Ubuntu 26.04 benutzt: Was erwartest du, und was siehst du?

:::loesung
Unter Ubuntu 26.04 melden `ls`, `cat` und `date` die Herkunft `uutils coreutils`, dagegen `cp`, `rm` und `df` die Herkunft `GNU coreutils`. Das passt zur Definition: Bis auf `cp`, `mv`, `rm`, `df` und `true` kommen die Grundbefehle aus uutils. Auf Debian, Fedora oder Kali melden alle sechs `GNU coreutils`; die Fassungsnummern hängen von der Distribution ab.
:::
:::

:::aufgabe Aufgabe 26 ★★ uutils und GNU vergleichen
<span class="anker" id="aufg-26"></span>

Vergleiche unter Ubuntu 26.04 jeweils die uutils- und die GNU-Fassung: (a) `ls --version` und `gnuls --version`, (b) `ls /gibtsnicht` und `gnuls /gibtsnicht`, (c) `head --lines=x /etc/hostname` und `gnuhead --lines=x /etc/hostname`, (d) `uname -a --all` und `gnuuname -a --all`. Wo unterscheiden sich die Antworten, und wo nur der Programmname?

:::loesung
(a) `ls (uutils coreutils) 0.8.0` gegen `ls (GNU coreutils) 9.7` mit Angaben zu Lizenz und Verfassern: verschiedene Programme mit eigener Zählung der Fassungen.

(b) Gleich bis auf den Programmnamen:

```console
$ ls /gibtsnicht
ls: cannot access '/gibtsnicht': No such file or directory
$ gnuls /gibtsnicht
gnuls: cannot access '/gibtsnicht': No such file or directory
```

(c) Fast gleich. Beide melden `invalid number of lines`, uutils setzt das `x` aber in gerade Hochkommas, GNU in typografische einfache Anführungszeichen, wie sie im Englischen üblich sind.

(d) Verschieden. uutils lehnt die doppelte Angabe mit `error: the argument '--all' cannot be used multiple times` ab, GNU gibt alle Angaben aus. Fehlermeldungen und Strenge unterscheiden sich, die eigentlichen Ergebnisse bei korrektem Aufruf nicht.
:::
:::

:::aufgabe Aufgabe 27 ★★★ Ein Programm, das seinen Namen liest
<span class="anker" id="aufg-27"></span>

Erkläre mit dem Hintergrund „Ein Programm, viele Namen“, warum `uname --version` mit `uname` und `head --version` mit `head` beginnt, obwohl dieselbe Datei antwortet. Welche Information aus der Wortliste, die die Shell übergibt, benutzt das Programm dafür? Warum würde eine Kopie dieser Datei mit dem Namen `meinbefehl` nicht funktionieren?

:::loesung
Die Shell übergibt jedem Programm eine Liste von Wörtern, deren erstes der Name ist, unter dem das Programm aufgerufen wurde. Bei `uname --version` lautet die Liste `uname`, `--version`, bei `head --version` `head`, `--version`. Beide Namen führen zu derselben Programmdatei von uutils. Sie liest zuerst das erste Wort, schlägt in ihrer Liste bekannter Befehle nach, welcher Befehl so heißt, und verhält sich dann wie dieser Befehl; deshalb nennt sie in ihrer Antwort auch diesen Namen. Eine Kopie mit dem Namen `meinbefehl` bekäme als erstes Wort `meinbefehl`. Diesen Namen findet sie in ihrer Liste nicht und weiß deshalb nicht, welchen Befehl sie spielen soll; sie meldet einen Fehler, statt etwas zu tun.
:::
:::

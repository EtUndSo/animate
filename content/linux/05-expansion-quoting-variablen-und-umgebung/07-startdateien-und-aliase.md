---
title: Startdateien und Aliase
pfad: Informatik / Linux und Kommandozeile / Wie die Shell eine Befehlszeile liest: Expansion, Quoting, Variablen, Umgebung
adresse: informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung
knoten: Kapitel 5: Wie die Shell eine Befehlszeile liest: Expansion, Quoting, Variablen, Umgebung
order: 6100700
summary: Alles, was du bisher in einer Shell eingestellt hast, verschwindet mit ihr.
tags: Startdatei, source, Anmelde-Shell, alias
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Alles, was du bisher in einer Shell eingestellt hast, verschwindet mit ihr. Dieser Abschnitt zeigt, welche Dateien die Shell bei jedem Start liest, wie man darin Variablen, den Suchpfad und Aliase dauerhaft einrichtet und wie man eine geänderte Datei sofort wirksam macht.
:::

### Die Startdatei

<span class="anker" id="stufe-6-1"></span>

Eine neue Shell beginnt fast von vorn: Sie bekommt die Umgebung ihres Elternprozesses, sonst nichts. Eine Variable, die du nicht exportiert hast, kennt sie nicht:

```console
$ wohnort=Hamburg
$ bash -i -c 'echo Wohnort: $wohnort Ende'
Wohnort: Ende
```

Die Option `-i` macht die neue bash zu einer interaktiven Shell, so wie die Shell, in die du tippst. Trotzdem kennt sie `wohnort` nicht. Und doch hat jede neue Shell die Aliase `ll` und `la` aus [Kapitel 2, Abschnitt 3.4](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/arten-von-befehlen.html#stufe-3-4). Irgendwoher muss sie diese Einstellungen bei jedem Start holen. Abbildung [24](#abb-24) zeigt, woher.

:::abbildung linux/k5startdatei 24
Der Start einer interaktiven bash. Bevor die erste Eingabeaufforderung erscheint, liest die Shell die Datei `~/.bashrc` Zeile für Zeile und führt jede aus, als wäre sie getippt worden, darunter `alias ll='ls -alF'` und `alias la='ls -A'`. Erst danach wartet sie auf deine Befehle, und die Aliase sind da.
:::

:::definition Definition 6.1 (Startdatei)
<span class="anker" id="satz-6-1"></span>

Eine __Startdatei__ ist eine Textdatei mit Befehlen für die Shell, die die Shell bei ihrem Start liest und ausführt, als hättest du die Zeilen getippt. Startest du in einem Terminal eine neue interaktive bash, liest sie die Datei `~/.bashrc` in deinem Heimatverzeichnis.
:::

Die Endung „rc“ ist unter Unix für Dateien mit Startbefehlen üblich, nach dem englischen „run commands“; der Punkt am Anfang macht die Datei zu einer versteckten Datei. Unter Ubuntu liest bash vorher noch die Datei `/etc/bash.bashrc`, die für alle Benutzer gilt. Ubuntu legt jedem neuen Benutzer eine `~/.bashrc` mit sinnvollen Voreinstellungen an.

::::beispiel Woher die Aliase kommen
```console
$ grep -n "alias l" ~/.bashrc
78:    alias ls='ls --color=auto'
91:alias ll='ls -alF'
92:alias la='ls -A'
93:alias l='ls -CF'
```

`grep` zeigt die Zeilen der Datei, die `alias l` enthalten, mit ihrer Nummer davor. Hier entstehen die Aliase, die [Kapitel 2](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/die-shell-erste-befehle.html) vorgefunden hat: Jede neue interaktive bash führt diese Zeilen aus. Die eingerückte Zeile 78 steht in einem Teil der Datei, den die Shell nur ausführt, wenn es das Hilfsprogramm `dircolors` für die Farben von `ls` gibt; unter Ubuntu ist das der Fall.
::::

⁠**Kurz gesagt:** Eine Startdatei enthält Befehle, die die Shell bei jedem Start ausführt; eine neue interaktive bash liest `~/.bashrc`.

:::hintergrund Warum ~/.bashrc ohne Terminal nichts tut
Ubuntus `~/.bashrc` beginnt mit einer Prüfung, ob die Shell interaktiv ist, und hört sofort auf, wenn nicht. Eine Shell, die mit `bash -c` einen Text ausführt, liest die Datei gewöhnlich gar nicht. Es gibt aber eine Ausnahme: Startet bash ohne Terminal über eine Netzverbindung, etwa weil jemand von einem anderen Rechner aus einen einzelnen Befehl schickt, liest sie `~/.bashrc` doch. Für diesen Fall ist die Prüfung da. Einstellungen für die Arbeit am Terminal, etwa Aliase und das Aussehen der Eingabeaufforderung, stören so keine Befehle, die ohne Terminal laufen.
:::

### source

<span class="anker" id="stufe-6-2"></span>

Eine Änderung an `~/.bashrc` wirkt erst in der nächsten Shell, denn die laufende hat die Datei schon beim Start gelesen. Man könnte ein neues Terminal öffnen. Einfacher ist es, die laufende Shell die Datei noch einmal lesen zu lassen.

:::definition Definition 6.2 (source)
<span class="anker" id="satz-6-2"></span>

Der eingebaute Befehl __source__ `datei` liest die Datei und führt ihre Zeilen in der laufenden Shell aus, als hättest du sie getippt. Ein einzelner Punkt ist eine Kurzform: `. datei` bedeutet dasselbe.
:::

Entscheidend ist „in der laufenden Shell“: Es entsteht kein Kindprozess. Zuweisungen, `export` und Aliase aus der Datei wirken deshalb in deiner Shell weiter, nachdem die Datei zu Ende gelesen ist. Abbildung [25](#abb-25) stellt das einem Kindprozess gegenüber.

:::abbildung linux/k5source 25
Dieselbe Datei `farbe.txt` mit der Zeile `farbe=blau`, zweimal gelesen. Oben in einer Kind-Shell: Die Zuweisung landet in der Kopie des Kindes und verschwindet mit ihm. Unten mit `source`: Die Zeile läuft in der Shell selbst, `farbe` bleibt danach gesetzt.
:::

::::beispiel Im Kind und in der Shell
```console
$ echo farbe=blau > farbe.txt
$ bash -c 'source ./farbe.txt; echo Im Kind: $farbe'
Im Kind: blau
$ echo In der Shell: $farbe Ende
In der Shell: Ende
$ source ./farbe.txt
$ echo In der Shell: $farbe
In der Shell: blau
```

Die Kind-Shell hat die Datei gelesen und kannte `farbe`; mit dem Kind ist die Variable verschwunden. Erst `source` in der Shell selbst setzt sie dauerhaft für diese Sitzung. Das `./` vor dem Namen sagt `source`, dass die Datei im Arbeitsverzeichnis liegt. Ohne Schrägstrich sucht `source` die Datei wie einen Befehl zuerst in den Verzeichnissen aus `PATH` und bash erst danach im Arbeitsverzeichnis; mit `./` gibt es keine Verwechslung.
::::

⁠**Kurz gesagt:** `source datei` führt eine Datei in der laufenden Shell aus; ihre Einstellungen bleiben, weil kein Kindprozess entsteht.

### Die Anmelde-Shell

<span class="anker" id="stufe-6-3"></span>

Nicht jede Shell startet auf dieselbe Weise. Eine Shell, die gleich nach dem Anmelden läuft, hat zusätzliche Aufgaben, etwa den Suchpfad einzurichten, der dann für die ganze Sitzung gilt.

:::definition Definition 6.3 (Anmelde-Shell)
<span class="anker" id="satz-6-3"></span>

Eine __Anmelde-Shell__ ist eine Shell, die bei einer Anmeldung startet, etwa nach Benutzername und Passwort an einer Textkonsole, bei einer Verbindung von einem anderen Rechner oder beim Öffnen des Terminals von WSL. bash liest dann zuerst `/etc/profile` und danach die erste vorhandene der Dateien `~/.bash_profile`, `~/.bash_login` und `~/.profile`; `~/.bashrc` liest sie nicht von sich aus.
:::

Ubuntu legt nur `~/.profile` an, und diese Datei holt `~/.bashrc` selbst nach. Abbildung [26](#abb-26) zeigt die drei üblichen Fälle. Im Terminal einer grafischen Oberfläche startet bash meist ohne Anmeldung, liest nur `~/.bashrc` und erbt die übrige Umgebung von dem Programm, das sie gestartet hat. Der eingebaute Befehl `shopt` zeigt Einstellungen der bash; `shopt login_shell` verrät, ob die laufende bash eine Anmelde-Shell ist. Die Option `-l` startet eine bash als Anmelde-Shell.

:::abbildung linux/k5startdateien 26
Welche Startdateien bash liest. Anmelde-Shell, etwa im Terminal von WSL: `/etc/profile`, dann `~/.profile`, das unter Ubuntu `~/.bashrc` nachholt. Interaktive Shell ohne Anmeldung, etwa eine neue `bash` im Terminal: `/etc/bash.bashrc`, dann `~/.bashrc`. `bash -c '…'`: keine Startdatei.
:::

::::beispiel Mit und ohne Anmeldung
```console
$ shopt login_shell
login_shell             off
$ bash -l -c 'shopt login_shell'
login_shell             on
```

Die Shell, in der die Beispiele dieses Kapitels liefen, war keine Anmelde-Shell. Tippst du die erste Zeile im Terminal von WSL, siehst du `on`, denn WSL startet dort eine Anmelde-Shell. Wie `~/.profile` unter Ubuntu die Datei `~/.bashrc` nachholt, zeigen die Zeilen 11 bis 17:

```console
$ head -n 17 ~/.profile | tail -n 7
```

```text
# if running bash
if [ -n "$BASH_VERSION" ]; then
    # include .bashrc if it exists
    if [ -f "$HOME/.bashrc" ]; then
        . "$HOME/.bashrc"
    fi
fi
```

Zeilen mit `#` am Anfang sind Kommentare, die die Shell überliest. Die übrigen Zeilen bedeuten: Läuft gerade bash und gibt es die Datei `~/.bashrc`, dann wird sie gelesen; der einzelne Punkt ist die Kurzform von `source` aus Unterabschnitt [6.2](#stufe-6-2). Weil `source` keinen Kindprozess startet, wirkt alles aus `~/.bashrc` in der Anmelde-Shell selbst. Am Ende der Datei richtet `~/.profile` den Suchpfad für eigene Programme ein:

```console
$ tail -n 9 ~/.profile
```

```text
# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/bin" ] ; then
    PATH="$HOME/bin:$PATH"
fi

# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/.local/bin" ] ; then
    PATH="$HOME/.local/bin:$PATH"
fi
```

Gibt es bei der Anmeldung ein Verzeichnis `~/bin` oder `~/.local/bin`, kommt es vorn in den Suchpfad, genau wie `~/linuxk5/bin` in Unterabschnitt [5.5](wie-die-shell-programme-findet-path.html#stufe-5-5).
::::

⁠**Kurz gesagt:** Eine Anmelde-Shell liest `/etc/profile` und `~/.profile`, das unter Ubuntu `~/.bashrc` nachholt; eine interaktive Shell ohne Anmeldung liest nur `~/.bashrc`.

:::hintergrund Eine Datei, die die andere verdrängt
Eine Anmelde-Shell liest nur die erste vorhandene der drei Dateien `~/.bash_profile`, `~/.bash_login` und `~/.profile`. Legt jemand, etwa nach einer Anleitung für eine andere Distribution, eine `~/.bash_profile` an, liest bash `~/.profile` nicht mehr, und mit ihr fallen der Suchpfad für eigene Programme und das Nachholen von `~/.bashrc` weg. Der Kommentar in den ersten Zeilen von Ubuntus `~/.profile` weist genau darauf hin. Woran eine Shell erkennt, dass sie eine Anmelde-Shell ist: Das Programm, das die Anmeldung erledigt, startet sie mit einem Aufrufnamen, der mit einem Minus beginnt, also `-bash`; ein Aufruf mit `-l` hat dieselbe Wirkung.
:::

### Eine Einstellung dauerhaft machen

<span class="anker" id="stufe-6-4"></span>

Jetzt lässt sich eine Einstellung so einrichten, dass jede neue Shell sie hat: Man schreibt sie in `~/.bashrc` und lässt die laufende Shell die Datei mit `source` neu lesen. Als Beispiel dient die Umgebungsvariable `EDITOR`. Viele Programme, die zwischendurch einen Text von dir brauchen, starten den Editor, dessen Name in `EDITOR` steht; `nano` kennst du aus [Kapitel 3, Abschnitt 5.3](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-und-verzeichnisse-anlegen.html#stufe-5-3).

:::warnung Erst sichern, dann ändern
Eine kaputte `~/.bashrc` stört jede neue Shell. Lege vor jeder Änderung eine Sicherungskopie an, hier in deinem Übungsverzeichnis:

```console
$ cp ~/.bashrc ~/linuxk5/bashrc.sicherung
```

Hänge neue Zeilen nur mit `>>` an. Ein einziges `>` statt `>>` macht die Datei leer, bevor die neue Zeile hineinkommt ([Kapitel 4, Abschnitt 2.1](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/ausgaben-umleiten.html#stufe-2-1)). Wer lieber im Editor arbeitet, öffnet die Datei mit `nano ~/.bashrc` und schreibt die Zeile ans Ende.
:::

::::beispiel EDITOR dauerhaft setzen
```console
$ echo 'export EDITOR=nano' >> ~/.bashrc
$ tail -n 1 ~/.bashrc
export EDITOR=nano
$ echo Editor: $EDITOR Ende
Editor: Ende
$ bash -i -c 'echo Editor: $EDITOR'
Editor: nano
$ source ~/.bashrc
$ echo Editor: $EDITOR
Editor: nano
```

Die einfachen Anführungszeichen geben `echo` die Zeile unverändert weiter. Danach steht sie am Ende der Datei. Die laufende Shell kennt `EDITOR` noch nicht, eine neue interaktive bash schon, weil sie die Datei beim Start liest. Nach `source` hat auch die laufende Shell den Wert. Abbildung [27](#abb-27) zeigt den Ablauf.

:::abbildung linux/k5dauerhaft 27
Eine Einstellung wird dauerhaft. 1: Die Zeile `export EDITOR=nano` kommt ans Ende von `~/.bashrc`; die laufende Shell bleibt unverändert, denn sie hat die Datei schon beim Start gelesen. 2: Eine neue Shell liest die Datei beim Start und hat `EDITOR`. 3: `source ~/.bashrc` lässt die laufende Shell die Datei noch einmal lesen; jetzt hat auch sie den Wert.
:::
::::

Für eigene Programme bietet Ubuntu das Verzeichnis `~/.local/bin` an. Gibt es dieses Verzeichnis, nimmt `~/.profile` es bei der nächsten Anmeldung vorn in den Suchpfad auf. Ohne dich ab- und wieder anzumelden, kannst du das mit einer Anmelde-Shell prüfen:

```console
$ mkdir -p ~/.local/bin
$ bash -l -c 'echo "$PATH"' | tr ':' '\n' | head -n 1
/home/student/.local/bin
```

Ein Programm, das du nach `~/.local/bin` kopierst, startet ab der nächsten Anmeldung mit seinem Namen allein, aus jedem Verzeichnis. Statt auf `~/.profile` zu setzen, kann man den Suchpfad auch mit einer Zeile wie `export PATH="$HOME/bin:$PATH"` in `~/.bashrc` erweitern; dann setzt allerdings jede Shell, die in einer anderen startet, das Verzeichnis ein weiteres Mal davor.

⁠**Kurz gesagt:** Dauerhafte Einstellungen gehören in `~/.bashrc`, eigene Programme nach `~/.local/bin`; `source ~/.bashrc` macht Änderungen sofort wirksam.

### Der Alias

<span class="anker" id="stufe-6-5"></span>

[Kapitel 2, Abschnitt 3.4](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/arten-von-befehlen.html#stufe-3-4) hat Aliase als Abkürzungen kennengelernt, die die Shell beim Einlesen einer Zeile durch hinterlegten Text ersetzt. Jetzt kannst du eigene anlegen und weißt, wo sie dauerhaft stehen.

:::definition Definition 6.4 (Alias anlegen)
<span class="anker" id="satz-6-4"></span>

Der eingebaute Befehl __alias__ `name='text'` legt einen Alias an: Steht `name` als erstes Wort eines Befehls, ersetzt die Shell es durch `text`. `unalias name` löscht den Alias, `alias` ohne Argumente zeigt alle. Aliase gelten nur in der Shell, in der sie angelegt wurden, und nur in interaktiven Shells.
:::

Die einfachen Anführungszeichen halten den Text zu einem Wort zusammen und verhindern, dass die Shell darin schon beim Anlegen etwas ersetzt; eine Tilde im Text wird erst bei jeder Benutzung ersetzt.

::::beispiel Ein Alias für die Einkaufsliste
```console
$ alias einkauf='cat ~/linuxk5/einkauf.txt'
$ einkauf
Milch
Brot
Äpfel
Kaffee
$ type einkauf
einkauf is aliased to `cat ~/linuxk5/einkauf.txt'
$ bash -c einkauf
bash: line 1: einkauf: command not found
$ unalias einkauf
$ einkauf
einkauf: command not found
```

Die Kind-Shell aus `bash -c` kennt den Alias nicht: Sie ist nicht interaktiv, und Aliase werden ohnehin nicht vererbt. Nach `unalias` ist er auch in der Shell selbst verschwunden.
::::

Dauerhaft wird ein Alias wie jede andere Einstellung über `~/.bashrc`. Weil die Zeile selbst einfache Anführungszeichen enthält, schützen hier doppelte Anführungszeichen sie auf dem Weg in die Datei:

```console
$ echo "alias einkauf='cat ~/linuxk5/einkauf.txt'" >> ~/.bashrc
$ tail -n 1 ~/.bashrc
alias einkauf='cat ~/linuxk5/einkauf.txt'
$ source ~/.bashrc
$ einkauf
Milch
Brot
Äpfel
Kaffee
```

Wer die angehängten Zeilen wieder loswerden will, kopiert die Sicherung zurück. In der laufenden Shell bleibt, was sie schon gelesen hat, bis zu ihrem Ende erhalten; neue Shells haben es nicht mehr:

```console
$ cp ~/linuxk5/bashrc.sicherung ~/.bashrc
$ tail -n 1 ~/.bashrc
fi
```

`fi` ist die letzte Zeile von Ubuntus ursprünglicher `~/.bashrc`.

⁠**Kurz gesagt:** `alias name='text'` legt eine Abkürzung für die laufende interaktive Shell an; dauerhaft wird sie in `~/.bashrc`.

:::hintergrund Eine eigene Datei für Aliase
Ubuntus `~/.bashrc` enthält Zeilen, die eine Datei `~/.bash_aliases` mit `source` einlesen, wenn es sie gibt. Wer viele eigene Aliase hat, schreibt sie dort hinein und lässt `~/.bashrc` unverändert. Für Abkürzungen, die Argumente an einer bestimmten Stelle brauchen, sind Aliase zu schlicht: Die Shell ersetzt nur das erste Wort und hängt alles Übrige unverändert an.
:::

### Aufgaben zu Abschnitt [6](#stufe-6)

<span class="anker" id="stufe-6-6"></span>

:::aufgabe Aufgabe 20 ★ Welche Startdatei?
<span class="anker" id="aufg-20"></span>

Welche Startdateien liest bash in diesen Fällen, und hat die Shell danach die Einstellungen aus `~/.bashrc`? (a) Du öffnest unter Windows das Terminal von WSL. (b) Du öffnest auf einem Ubuntu-Desktop das Programm „Terminal“. (c) Du tippst in einem Terminal `bash` und drückst die Eingabetaste. (d) Ein Befehl `bash -c 'll'` läuft.

:::loesung
(a) Das Terminal von WSL startet eine Anmelde-Shell. bash liest `/etc/profile`, das unter Ubuntu `/etc/bash.bashrc` einliest, und danach `~/.profile`, das `~/.bashrc` nachholt. Die Einstellungen sind also da. (b) Das Terminal einer grafischen Oberfläche startet meist eine interaktive Shell ohne Anmeldung; sie liest `/etc/bash.bashrc` und `~/.bashrc`. Die Einstellungen sind da. (c) Eine neue bash im Terminal ist ebenfalls interaktiv und ohne Anmeldung; sie liest dieselben Dateien wie in (b). (d) `bash -c` ist nicht interaktiv und liest keine Startdatei. Der Alias `ll` aus `~/.bashrc` fehlt deshalb, und selbst wenn er definiert wäre, ersetzte eine nicht interaktive Shell ihn nicht; die Zeile endet mit „command not found“.
:::
:::

:::aufgabe Aufgabe 21 ★★ Dauerhaft einrichten
<span class="anker" id="aufg-21"></span>

(a) Sichere deine `~/.bashrc` in dein Übungsverzeichnis. (b) Hänge zwei Zeilen an: `export LIEBLINGSOBST=Mango` und einen Alias `wo`, der `pwd` ausführt. (c) Prüfe vor und nach `source ~/.bashrc`, ob die laufende Shell `LIEBLINGSOBST` kennt, und probiere `wo` aus. (d) Sage voraus, was `bash -c 'echo Obst: $LIEBLINGSOBST; wo'` ausgibt, und erkläre den Unterschied zwischen Variable und Alias. (e) Stelle die ursprüngliche Datei aus der Sicherung wieder her und prüfe mit `cmp` und `$?`, dass beide Dateien gleich sind; `cmp` vergleicht zwei Dateien Byte für Byte und meldet nur Unterschiede.

:::loesung
```console
$ cp ~/.bashrc ~/linuxk5/bashrc.sicherung
$ echo 'export LIEBLINGSOBST=Mango' >> ~/.bashrc
$ echo "alias wo='pwd'" >> ~/.bashrc
$ echo Obst: $LIEBLINGSOBST Ende
Obst: Ende
$ source ~/.bashrc
$ echo Obst: $LIEBLINGSOBST
Obst: Mango
$ wo
/home/student/linuxk5
$ bash -c 'echo Obst: $LIEBLINGSOBST; wo'
Obst: Mango
bash: line 1: wo: command not found
$ cp ~/linuxk5/bashrc.sicherung ~/.bashrc
$ cmp ~/linuxk5/bashrc.sicherung ~/.bashrc
$ echo $?
0
```

(a) und (b) Die Sicherung zuerst, dann zwei Zeilen mit `>>`. Die zweite Zeile enthält einfache Anführungszeichen und steht deshalb selbst in doppelten. (c) Vor `source` kennt die laufende Shell die Variable nicht, danach schon, und auch der Alias wirkt. (d) Die Kind-Shell aus `bash -c` bekommt `LIEBLINGSOBST` über die Umgebung, weil die Zeile in `~/.bashrc` die Variable exportiert. Den Alias kennt sie nicht: Aliase werden nicht vererbt, und eine nicht interaktive Shell ersetzt sie ohnehin nicht. (e) `cmp` schreibt nichts und endet mit dem Exit-Status 0: Die Dateien sind gleich, die ursprüngliche `~/.bashrc` ist wiederhergestellt.
:::
:::

:::aufgabe Aufgabe 22 ★★ Der Punkt als Befehl
<span class="anker" id="aufg-22"></span>

Lege mit `echo haustier=Hund > tier.txt` eine kleine Datei an. Sage voraus, was `bash -c '. ./tier.txt; echo Im Kind: $haustier'` ausgibt und was danach `echo In der Shell: $haustier Ende` zeigt. Was ändert sich, wenn du `. ./tier.txt` direkt in deiner Shell eingibst? Was bedeuten die beiden Punkte in `. ./tier.txt`?

:::loesung
```console
$ echo haustier=Hund > tier.txt
$ bash -c '. ./tier.txt; echo Im Kind: $haustier'
Im Kind: Hund
$ echo In der Shell: $haustier Ende
In der Shell: Ende
$ . ./tier.txt
$ echo In der Shell: $haustier
In der Shell: Hund
```

Die Kind-Shell liest die Datei in ihrem eigenen Prozess; die Variable lebt nur dort und verschwindet mit dem Kind. Direkt in der Shell eingegeben, führt der Befehl die Zuweisung in der Shell selbst aus, und die Variable bleibt. Der erste Punkt ist der Befehl, die Kurzform von `source`. Der zweite Punkt gehört zum Pfad `./tier.txt` und bedeutet das Arbeitsverzeichnis ([Kapitel 3, Abschnitt 2.5](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/das-arbeitsverzeichnis-und-pfade.html#stufe-2-5)).
:::
:::

:::aufgabe Aufgabe 23 ★★★ Ein Alias kommt zu spät
<span class="anker" id="aufg-23"></span>

Sage voraus, was diese beiden Zeilen ausgeben, und prüfe es:

```console
$ alias begruessung='echo Guten Tag'; begruessung
$ begruessung
```

Erkläre das Ergebnis der ersten Zeile mit Schritt 1 der Reihenfolge aus Unterabschnitt [3.9](worttrennung-und-quoting.html#stufe-3-9).

:::loesung
```console
$ alias begruessung='echo Guten Tag'; begruessung
begruessung: command not found
$ begruessung
Guten Tag
```

Aliase ersetzt die Shell in Schritt 1, beim Zerlegen der Zeile in Wörter. Die erste Zeile liest sie vollständig ein, bevor sie irgendetwas davon ausführt; in diesem Augenblick gab es den Alias noch nicht, also blieb `begruessung` ein gewöhnliches Wort, für das die Shell ein Programm sucht. Erst beim Ausführen der Zeile entstand der Alias. Die zweite Zeile liest die Shell danach, und jetzt ersetzt sie das Wort. Deshalb gehört eine Alias-Definition in eine eigene Zeile.
:::
:::

**Zum Weiterüben.** Die frei zugängliche Übungsplattform pwn.college bietet unter dem Namen „Linux Luminarium“ kleine Aufgaben im Browser an; die Module „File Globbing“, „Shell Variables“ und „Pondering PATH“ passen zu diesem Kapitel. Sie laufen auf einem fremden Rechner, nicht auf deinem eigenen.

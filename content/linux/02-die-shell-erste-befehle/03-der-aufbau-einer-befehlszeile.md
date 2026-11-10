---
title: Der Aufbau einer Befehlszeile
pfad: Informatik / Linux und Kommandozeile / Die Shell: erste Befehle
adresse: informatik/linux-und-kommandozeile/die-shell-erste-befehle
knoten: Kapitel 2: Die Shell: erste Befehle
order: 6070300
summary: Eine Befehlszeile ist kein freier Text, sondern folgt wenigen festen Regeln.
tags: Befehlszeile, Wörter, Befehl, Argument, Option, kurze Option, lange Option, Option mit Wert
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Eine Befehlszeile ist kein freier Text, sondern folgt wenigen festen Regeln. Dieser Abschnitt zeigt, wie die Shell eine Zeile in Wörter zerlegt, welches Wort den Befehl nennt, welche ihm sagen, womit und wie er arbeiten soll, und wie man ein Wort, das wie eine Option aussieht, trotzdem als gewöhnliches Wort übergibt.
:::

### Die Befehlszeile

<span class="anker" id="stufe-2-1"></span>

Bevor die Shell etwas ausführen kann, muss sie herausfinden, aus welchen Teilen die getippte Zeile besteht. Dafür gibt es eine einfache, feste Regel.

**Wörter statt Buchstaben.** Die Shell liest die Zeile nicht Buchstabe für Buchstabe als Ganzes, sondern zerlegt sie zuerst an den Leerzeichen in einzelne Stücke. Erst danach schaut sie, was das erste Stück bedeutet. Abbildung [5](#abb-5) zeigt das an der Zeile `uname -r`.

:::abbildung linux/k2woerter 5
Die Shell zerlegt die Befehlszeile `uname -r` an den Leerzeichen in die Wörter `uname` und `-r`. Erst danach schaut sie, was die Wörter bedeuten.
:::

:::definition Definition 2.1 (Befehlszeile und Wort)
<span class="anker" id="satz-2-1"></span>

Eine __Befehlszeile__ ist alles, was du hinter der Eingabeaufforderung tippst, bevor du die Eingabetaste drückst. Die Shell zerlegt sie an Leerzeichen in __Wörter__; mehrere Leerzeichen hintereinander trennen wie eines.
:::

::::beispiel Wörter zählen
`uname -r` besteht aus den zwei Wörtern `uname` und `-r`. `echo Hallo` besteht ebenfalls aus zwei Wörtern, denn die drei Leerzeichen trennen wie eines. `uname-r` dagegen ist ein einziges Wort, weil kein Leerzeichen darin steht; der Bindestrich trennt nichts.
::::

⁠**Kurz gesagt:** Die Shell zerlegt jede Befehlszeile an den Leerzeichen in Wörter.

### Der Befehl

<span class="anker" id="stufe-2-2"></span>

Eine Zeile an die Shell muss vor allem sagen, was geschehen soll. Wie in einem kurzen Satz steht dieses Wichtigste ganz vorn.

:::definition Definition 2.2 (Befehl)
<span class="anker" id="satz-2-2"></span>

Das erste Wort einer Befehlszeile ist der __Befehl__: der Name dessen, was ausgeführt werden soll. Nur dieses Wort sucht die Shell; alle weiteren reicht sie an den Befehl weiter.
:::

Groß- und Kleinschreibung zählen: `uname` und `UNAME` sind für die Shell verschiedene Namen. Fehlt das Leerzeichen, wird aus zwei Wörtern eines, und die Shell sucht einen Befehl mit diesem langen Namen.

::::beispiel Drei Befehle und zwei Tippfehler
Die ersten drei Zeilen bestehen nur aus einem Befehl. `uname` nennt das Betriebssystem, `whoami` (englisch „who am I?“) den Benutzer, `hostname` den Namen des Rechners:

```console
$ uname
Linux
$ whoami
student
$ hostname
labor
$ UNAME -r
UNAME: command not found
$ uname-r
uname-r: command not found
```

Bei den letzten beiden Zeilen meldet die Shell, dass sie keinen Befehl dieses Namens kennt: einmal wegen der Großbuchstaben, einmal weil `uname-r` ohne Leerzeichen ein einziges Wort ist. Ubuntu schlägt bei manchen Tippfehlern zusätzlich ähnlich lautende Befehle vor; installieren musst du für dieses Kapitel nichts.
::::

⁠**Kurz gesagt:** Das erste Wort der Zeile ist der Befehl, und bei seinem Namen zählt jeder Buchstabe, auch ob groß oder klein.

### Das Argument

<span class="anker" id="stufe-2-3"></span>

Viele Befehle brauchen mehr als ihren Namen: Welche Datei soll angezeigt werden, welcher Text ausgegeben? Diese Angaben stehen in den übrigen Wörtern der Zeile.

**Die Shell reicht Wörter weiter, keine Leerzeichen.** Der Befehl `echo` schreibt einfach die Wörter hin, die er bekommt, getrennt durch je ein Leerzeichen. Mit ihm sieht man genau, was die Shell aus einer Zeile macht. Abbildung [6](#abb-6) zeigt es an einer Zeile mit vielen Leerzeichen.

:::abbildung linux/k2argumente 6
Aus `echo Hallo Welt` macht die Shell drei Wörter. `echo` bekommt nur die beiden Wörter `Hallo` und `Welt` und schreibt sie mit einem einzigen Leerzeichen dazwischen.
:::

:::definition Definition 2.3 (Argument)
<span class="anker" id="satz-2-3"></span>

Jedes Wort der Befehlszeile nach dem Befehl ist ein __Argument__. Die Shell übergibt dem Befehl die Argumente in der Reihenfolge, in der sie stehen. Was ein Argument bedeutet, legt der Befehl selbst fest.
:::

::::beispiel Wörter ausgeben und eine Datei zeigen
`echo` bekommt zwei Argumente und schreibt sie hin. Wie viele Leerzeichen zwischen den Wörtern standen, erfährt `echo` nicht:

```console
$ echo Hallo Welt
Hallo Welt
$ echo Hallo      Welt
Hallo Welt
```

Der Befehl `cat` zeigt den Inhalt der Dateien, deren Namen er als Argumente bekommt. Das Argument `/etc/hostname` nennt die Datei `hostname` im Systemordner `/etc`; der Schrägstrich trennt den Ordner vom Namen der Datei. In ihr steht der Name des Rechners:

```console
$ cat /etc/hostname
labor
$ cat /etc/Hostname
cat: /etc/Hostname: No such file or directory
```

Auch bei Dateinamen zählt die Groß- und Kleinschreibung: Eine Datei `Hostname` gibt es nicht. Die Fehlermeldung beginnt mit dem Namen des Befehls, damit man weiß, wer sich beschwert.
::::

⁠**Kurz gesagt:** Die Wörter nach dem Befehl sind seine Argumente; die Shell reicht sie der Reihe nach weiter, und der Befehl entscheidet, was sie bedeuten.

:::hintergrund Die Shell zerlegt, das Programm deutet
Die Shell übergibt einem Befehl eine Liste von Wörtern, und zwar ohne die Leerzeichen dazwischen. Für `echo Hallo Welt` lautet die Liste `echo`, `Hallo`, `Welt`; das erste Element ist der Name, unter dem der Befehl aufgerufen wurde. Startet die Shell dafür ein Programm, reicht sie die Liste mit einem Systemaufruf an den Kernel, und der Kernel legt sie dem neuen Programm in den Speicher. Das Programm sieht nie die Zeile, die du getippt hast, sondern nur diese Liste. Deshalb kann `echo` die vielen Leerzeichen nicht wiedergeben, und deshalb ist es allein Sache des Programms, ob es ein Wort als Dateinamen, als Zahl oder als Text versteht. Die Shell legt nur fest, wo ein Wort endet und das nächste beginnt.
:::

### Die Option

<span class="anker" id="stufe-2-4"></span>

Derselbe Befehl soll manchmal etwas anders arbeiten: mehr ausgeben, weniger ausgeben, rückwärts sortieren. Dafür gibt es eine eigene Sorte von Argumenten, die nicht sagen, *womit* ein Befehl arbeitet, sondern *wie*.

**Schalter am Gerät.** Eine Waschmaschine wäscht immer Wäsche, aber mit Schaltern wählt man Temperatur und Schleuderdrehzahl (ein Bild zur Orientierung). Optionen sind solche Schalter, und man erkennt sie am Minuszeichen vorn. Abbildung [7](#abb-7) zeigt drei Schalter von `uname` einzeln und gebündelt.

:::abbildung linux/k2buendeln 7
Drei kurze Optionen von `uname`, einzeln und hinter einem gemeinsamen Minuszeichen gebündelt. Alle Schreibweisen bedeuten dasselbe, und die Reihenfolge der Ausgabe legt das Programm fest, nicht die Reihenfolge der Buchstaben.
:::

:::definition Definition 2.4 (Option)
<span class="anker" id="satz-2-4"></span>

Eine __Option__ ist ein Argument, das mit einem Minuszeichen beginnt und festlegt, wie der Befehl arbeitet. Eine __kurze Option__ besteht aus einem Minuszeichen und einem einzigen Buchstaben, etwa `-r`. Mehrere kurze Optionen ohne Wert darf man hinter einem einzigen Minuszeichen bündeln: `-srm` bedeutet dasselbe wie `-s -r -m`.
:::

Welche Optionen es gibt und was ein Buchstabe bedeutet, legt jedes Programm selbst fest. Bei `uname` heißt `-r` „Version des Kernels“; andere Programme benutzen denselben Buchstaben für ganz andere Dinge. Kennt ein Programm eine Option nicht, bricht es mit einer Fehlermeldung ab.

::::beispiel Was uname alles verrät
Ohne Option nennt `uname` nur den Namen des Kernels. `-s` tut ausdrücklich dasselbe, `-r` nennt die Version des Kernels und `-m` den Typ des Prozessors:

```console
$ uname -s
Linux
$ uname -r
6.6.87.2-microsoft-standard-WSL2
$ uname -m
x86_64
$ uname -s -r -m
Linux 6.6.87.2-microsoft-standard-WSL2 x86_64
$ uname -srm
Linux 6.6.87.2-microsoft-standard-WSL2 x86_64
$ uname -mrs
Linux 6.6.87.2-microsoft-standard-WSL2 x86_64
```

Die letzten drei Befehle geben genau dasselbe aus. Das Programm sammelt zuerst alle Schalter ein und schreibt die Angaben dann in seiner festen Reihenfolge. Eine Option, die `uname` nicht kennt, beantwortet es mit einer Fehlermeldung:

```console
$ uname -x
error: unexpected argument '-x' found

Usage: uname [OPTION]...

For more information, try '--help'.
```

Die Meldung ist auf jedem Linux etwas anders formuliert; was sie bedeutet, ist überall gleich.
::::

⁠**Kurz gesagt:** Optionen beginnen mit einem Minuszeichen und stellen ein, wie ein Befehl arbeitet; kurze Optionen lassen sich bündeln.

### Die lange Option

<span class="anker" id="stufe-2-5"></span>

Ein einzelner Buchstabe ist schnell getippt, aber schwer zu merken: Steht `-r` für „release“, „recursive“ oder „reverse“? Wer einen Befehl aufschreibt, den andere lesen sollen, möchte lieber ganze Wörter.

:::definition Definition 2.5 (Lange Option)
<span class="anker" id="satz-2-5"></span>

Eine __lange Option__ beginnt mit zwei Minuszeichen, auf die ein ganzes Wort folgt, etwa `--kernel-release`. Viele kurze Optionen haben eine gleichwertige lange Form. Lange Optionen lassen sich nicht bündeln; jede ist ein eigenes Wort.
:::

Zwei lange Optionen verstehen fast alle Programme: `--help` zeigt eine Kurzhilfe, `--version` die Fassung des Programms, wie eben bei `bash --version`.

::::beispiel Dieselbe Frage in Langform
```console
$ uname --kernel-name --kernel-release
Linux 6.6.87.2-microsoft-standard-WSL2
$ uname --machine
x86_64
```

Die erste Zeile entspricht `uname -s -r`. Bei einem kurzen Befehl am eigenen Terminal tippt man die kurze Form; in einer Anleitung, die jemand anderes verstehen soll, ist die lange Form oft die bessere Wahl.
::::

⁠**Kurz gesagt:** Lange Optionen beginnen mit zwei Minuszeichen und einem ganzen Wort; sie sind länger, aber selbsterklärend.

:::hintergrund Abgekürzte lange Optionen
Viele Programme akzeptieren eine lange Option auch abgekürzt, solange die Abkürzung eindeutig ist: `uname --kernel-r` funktioniert wie `uname --kernel-release`. Ist sie mehrdeutig, gibt es einen Fehler, denn `--kernel` könnte `--kernel-name`, `--kernel-release` oder `--kernel-version` heißen. In Anleitungen und gespeicherten Befehlen schreibt man lange Optionen trotzdem aus: Bekommt das Programm in einer neuen Fassung eine weitere Option mit demselben Anfang, wird eine eben noch eindeutige Abkürzung mehrdeutig.
:::

### Die Option mit Wert

<span class="anker" id="stufe-2-6"></span>

Manche Schalter brauchen eine Angabe dazu. „Zeige die ersten Zeilen“ ist unvollständig, solange niemand sagt, wie viele.

:::definition Definition 2.6 (Option mit Wert)
<span class="anker" id="satz-2-6"></span>

Eine __Option mit Wert__ verlangt eine zusätzliche Angabe, etwa eine Zahl. Bei einer kurzen Option steht der Wert als nächstes Wort dahinter oder direkt angehängt: `-n 2` oder `-n2`. Bei einer langen Option steht er hinter einem Gleichheitszeichen oder als nächstes Wort: `--lines=2` oder `--lines 2`.
:::

Der Befehl `head` zeigt die ersten Zeilen einer Datei, ohne Option zehn. Mit der Option `-n` und einem Wert bestimmst du die Zahl. Abbildung [8](#abb-8) zerlegt eine solche Zeile vollständig.

:::abbildung linux/k2zerlegt 8
Die Befehlszeile `head -n 2 /etc/os-release`, vollständig zerlegt: der Befehl, eine kurze Option mit ihrem Wert und ein gewöhnliches Argument, das die Datei nennt.
:::

::::beispiel Vier Schreibweisen, ein Ergebnis
Die Datei `/etc/os-release` kennst du aus [Kapitel 1, Abschnitt 2.3](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/drei-wege-zu-einem-eigenen-linux.html#stufe-2-3). Ihre ersten beiden Zeilen, auf vier Arten verlangt:

```console
$ head -n 2 /etc/os-release
PRETTY_NAME="Ubuntu 26.04.1 LTS"
NAME="Ubuntu"
$ head -n2 /etc/os-release
PRETTY_NAME="Ubuntu 26.04.1 LTS"
NAME="Ubuntu"
$ head --lines=2 /etc/os-release
PRETTY_NAME="Ubuntu 26.04.1 LTS"
NAME="Ubuntu"
$ head --lines 2 /etc/os-release
PRETTY_NAME="Ubuntu 26.04.1 LTS"
NAME="Ubuntu"
```

In der ersten Zeile hat `head` drei Argumente bekommen: `-n`, `2` und `/etc/os-release`. Dass die `2` zur Option gehört und kein Dateiname ist, weiß `head`, weil es selbst festgelegt hat, dass `-n` einen Wert verlangt.
::::

⁠**Kurz gesagt:** Manche Optionen verlangen einen Wert, der als nächstes Wort, angehängt oder hinter einem Gleichheitszeichen steht.

:::hintergrund Woher die gemeinsamen Regeln kommen
Dass fast alle Programme Optionen gleich behandeln, ist kein Zufall. Der Standard POSIX, auf den sich Unix-artige Systeme geeinigt haben, empfiehlt in seinen Regeln für die Aufrufform von Programmen: Optionen bestehen aus einem Minuszeichen und einem Buchstaben, mehrere dürfen hinter einem Minuszeichen gebündelt werden, und Optionen stehen vor den übrigen Argumenten. Die langen Optionen mit zwei Minuszeichen hat das GNU-Projekt hinzugefügt. Die meisten Programme zerlegen ihre Argumente nicht selbst, sondern überlassen das einer fertigen Funktion, die diese Regeln umsetzt. Sie stammt aus einer Programmbibliothek, einer Sammlung fertiger Programmteile, die viele Programme gemeinsam benutzen. Unter Linux erlauben diese Funktionen meist sogar, Optionen nach den übrigen Argumenten zu schreiben: `head /etc/os-release -n 1` funktioniert. Auf anderen Unix-Systemen geht das nicht immer; wer überall richtig liegen will, schreibt die Optionen zuerst.
:::

### Das Ende der Optionen

<span class="anker" id="stufe-2-7"></span>

Ein Programm erkennt Optionen am Minuszeichen. Was aber, wenn ein gewöhnliches Argument selbst mit einem Minuszeichen beginnt, etwa eine Datei, die jemand `-l` genannt hat? Das Programm würde es für eine Option halten.

:::abbildung linux/k2ende 9
Das Wort `--` ist eine Grenze: Davor prüft das Programm, ob ein Wort eine Option ist; dahinter ist jedes Wort ein gewöhnliches Argument, auch `-l`.
:::

:::definition Definition 2.7 (Ende der Optionen)
<span class="anker" id="satz-2-7"></span>

Das Argument `--`, zwei Minuszeichen allein, beendet die Optionen. Alle Wörter dahinter behandelt das Programm als gewöhnliche Argumente, auch wenn sie mit einem Minuszeichen beginnen. Das `--` selbst zählt nicht als Argument.
:::

Fast alle Programme halten sich an diese Vereinbarung, denn sie gehört zu denselben gemeinsamen Regeln wie das Bündeln kurzer Optionen.

::::beispiel Eine Datei namens -l
Der Befehl `ls` zeigt, welche Dateien es gibt; seine Option `-l` macht daraus eine ausführliche Liste. Mit `--` davor ist `-l` keine Option mehr, sondern der Name einer Datei, die `ls` sucht. Weil es sie nicht gibt, meldet es einen Fehler, und genau daran sieht man, dass `-l` jetzt als Name gilt:

```console
$ ls -- -l
ls: cannot access '-l': No such file or directory
```

Manche Programme weisen selbst auf diesen Ausweg hin. `cat` kennt keine Option `-l` und schlägt unter Ubuntu 26.04 vor, das Wort mit `--` als Dateinamen zu übergeben:

```console
$ cat -l
error: unexpected argument '-l' found

  tip: to pass '-l' as a value, use '-- -l'

Usage: cat [OPTION]... [FILE]...

For more information, try '--help'.
```
::::

⁠**Kurz gesagt:** Nach `--` ist jedes Wort ein gewöhnliches Argument, auch wenn es mit einem Minuszeichen beginnt.

:::merke Typische Fehler beim Tippen
<ul>

<li>

⁠**Leerzeichen vergessen:** `uname-r` ist ein einziges Wort, also ein unbekannter Befehl.

</li>

<li>

⁠**Leerzeichen zu viel:** `uname - r` übergibt ein einzelnes Minuszeichen und ein `r`; `uname` kennt keines von beiden und meldet einen Fehler.

</li>

<li>

⁠**Groß und klein verwechselt:** `UNAME` ist ein anderer Name als `uname`, und `-R` eine andere Option als `-r`.

</li>

<li>

⁠**Schrägstrich verwechselt:** Linux trennt Ordner mit `/`, nicht mit `\` wie Windows.

</li>

</ul>
:::

### Aufgaben zu Abschnitt [2](#stufe-2)

<span class="anker" id="stufe-2-8"></span>

:::aufgabe Aufgabe 4 ★ Befehlszeilen zerlegen
<span class="anker" id="aufg-4"></span>

Zerlege jede Zeile in Befehl, Optionen (mit ihrem Wert, falls sie einen haben) und übrige Argumente. Du musst die Befehle dafür nicht kennen. (a) `ls -la /etc` (b) `cp -r urlaub sicherung` (c) `grep -i fehler protokoll.txt` (d) `head --lines=5 notizen.txt` (e) `tail -n 3 -- -liste.txt`

:::loesung
<ol class="al">

<li>

Befehl `ls`; die gebündelten kurzen Optionen `-l` und `-a`; Argument `/etc`.

</li>

<li>

Befehl `cp`; Option `-r`; Argumente `urlaub` und `sicherung`.

</li>

<li>

Befehl `grep`; Option `-i`; Argumente `fehler` und `protokoll.txt`.

</li>

<li>

Befehl `head`; lange Option `--lines` mit dem Wert `5`; Argument `notizen.txt`.

</li>

<li>

Befehl `tail`; kurze Option `-n` mit dem Wert `3`; danach beendet `--` die Optionen, und `-liste.txt` ist ein gewöhnliches Argument, obwohl es mit einem Minuszeichen beginnt.

</li>

</ol>

Was die Optionen bewirken, steht hier nicht zur Frage; die Zerlegung folgt allein aus den Regeln für Wörter, Minuszeichen und Werte. Nur bei (d) und (e) muss man wissen, dass `--lines` und `-n` einen Wert verlangen; das verrät die Kurzhilfe des jeweiligen Programms.
:::
:::

:::aufgabe Aufgabe 5 ★★ Vorhersagen und prüfen
<span class="anker" id="aufg-5"></span>

Sage vorher, was jede Zeile ausgibt, und prüfe es dann am Rechner: (a) `uname -mr` (b) `uname -r -s` (c) `uname --machine --kernel-name` (d) `uname - m` (e) `Uname -m` (f) `echo eins zwei drei`

:::loesung
```console
$ uname -mr
6.6.87.2-microsoft-standard-WSL2 x86_64
$ uname -r -s
Linux 6.6.87.2-microsoft-standard-WSL2
$ uname --machine --kernel-name
Linux x86_64
$ echo   eins zwei     drei
eins zwei drei
```

In (a) bis (c) bestimmt `uname` die Reihenfolge selbst: erst der Kernelname, dann die Version, zuletzt der Prozessortyp, ganz gleich, in welcher Reihenfolge die Optionen stehen. (d) `uname - m` übergibt die beiden Argumente `-` und `m`; `uname` kennt keines davon und meldet `error: unexpected argument '-' found`. (e) `Uname` mit großem U ist ein unbekannter Befehl. Die Shell findet nichts, und Ubuntu schlägt zusätzlich vor, dass es einen Befehl `uname` gibt; installieren muss man nichts, man hat sich nur vertippt. (f) `echo` bekommt die drei Wörter `eins`, `zwei`, `drei` und schreibt sie mit je einem Leerzeichen dazwischen; die Leerzeichen der Eingabe erfährt es nicht.
:::
:::

:::aufgabe Aufgabe 6 ★★ Drei Zeilen auf vier Arten
<span class="anker" id="aufg-6"></span>

Lass dir mit `head` die ersten drei Zeilen von `/etc/os-release` anzeigen, und zwar in vier verschiedenen Schreibweisen der Option. Welche der folgenden Zeilen funktionieren außerdem, und warum? (a) `head /etc/os-release -n 3` (b) `head -n -- 3 /etc/os-release` (c) `head -- -n 3 /etc/os-release`

:::loesung
Vier Schreibweisen:

<ul>

<li>

`head -n 3 /etc/os-release`

</li>

<li>

`head -n3 /etc/os-release`

</li>

<li>

`head --lines=3 /etc/os-release`

</li>

<li>

`head --lines 3 /etc/os-release`

</li>

</ul>

Alle zeigen die Zeilen `PRETTY_NAME`, `NAME` und `VERSION_ID`.

(a) Funktioniert unter Linux. Die Programmbibliothek, die die Optionen auswertet, erlaubt Optionen auch hinter den übrigen Argumenten (Hintergrund „Woher die gemeinsamen Regeln kommen“):

```console
$ head /etc/os-release -n 3
PRETTY_NAME="Ubuntu 26.04.1 LTS"
NAME="Ubuntu"
VERSION_ID="26.04"
```

(b) Funktioniert nicht. `-n` verlangt einen Wert und nimmt dafür das nächste Wort, also `--`. Das ist keine Zahl, und `head` bricht ab:

```console
$ head -n -- 3 /etc/os-release
head: invalid number of lines: '-'
```

Dass die Meldung nur ein Minuszeichen zeigt, hat einen Grund: Ein Minuszeichen vor der Zahl hat bei `head` eine eigene Bedeutung, wie `head --help` verrät. `head` nimmt deshalb das erste Minuszeichen von `--` weg und findet danach nur noch `-`. GNU `head` meldet dasselbe. Entscheidend ist: Das `--` war hier kein Ende der Optionen, sondern der Wert von `-n`.

(c) Läuft, tut aber etwas anderes. Nach `--` sind `-n` und `3` gewöhnliche Argumente, also Dateinamen. Diese Dateien gibt es nicht, und `head` meldet zwei Fehler. Die dritte Datei gibt es; weil `head` mehrere Dateinamen bekommen hat, schreibt es eine Überschrift mit dem Namen davor und zeigt, ohne Option, die üblichen zehn Zeilen:

```console
$ head -- -n 3 /etc/os-release
head: cannot open '-n' for reading: No such file or directory
head: cannot open '3' for reading: No such file or directory
==> /etc/os-release <==
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
:::
:::

:::aufgabe Aufgabe 7 ★★★ Wer entscheidet was?
<span class="anker" id="aufg-7"></span>

Erkläre mit dem Hintergrund „Die Shell zerlegt, das Programm deutet“: (a) Warum gibt `uname -mrs` die Angaben in derselben Reihenfolge aus wie `uname -srm`? (b) Warum kann `echo` nicht wissen, wie viele Leerzeichen zwischen zwei Wörtern standen? (c) Woher weiß `head` bei `head -n 2 /etc/os-release`, dass die `2` kein Dateiname ist?

:::loesung
(a) Die Shell übergibt `uname` die Liste `uname`, `-mrs`. Was die Buchstaben bedeuten und in welcher Reihenfolge die Angaben erscheinen, entscheidet `uname` allein. Es merkt sich zuerst, welche Angaben verlangt sind, und schreibt sie dann in seiner festen Reihenfolge. Die Reihenfolge der Buchstaben spielt dafür keine Rolle.

(b) Die Shell zerlegt die Zeile, bevor sie `echo` startet, und übergibt nur die Wörter; die Leerzeichen dazwischen dienen allein als Trennzeichen und werden nicht weitergegeben. `echo` bekommt also `echo`, `Hallo`, `Welt` und weiß nichts von den Leerzeichen.

(c) Die Shell weiß es nicht und muss es nicht wissen; sie übergibt drei gleichrangige Argumente. `head` selbst ist so programmiert, dass `-n` einen Wert verlangt, und nimmt deshalb das nächste Wort, die `2`, als diesen Wert. Erst `/etc/os-release` ist für `head` ein Dateiname.
:::
:::

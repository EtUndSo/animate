---
title: Umgebung und Vererbung
pfad: Informatik / Linux und Kommandozeile / Wie die Shell eine Befehlszeile liest: Expansion, Quoting, Variablen, Umgebung
adresse: informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung
knoten: Kapitel 5: Wie die Shell eine Befehlszeile liest: Expansion, Quoting, Variablen, Umgebung
order: 6100500
summary: Variablen leben in der Shell, Programme laufen in eigenen Prozessen.
tags: Kindprozess, Elternprozess, Umgebung, Umgebungsvariable, export, env
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Variablen leben in der Shell, Programme laufen in eigenen Prozessen. Dieser Abschnitt klärt, welche Werte ein Programm beim Start von der Shell mitbekommt: die Umgebung. Er zeigt, wie man eine Variable in die Umgebung aufnimmt, warum ein gestartetes Programm nur eine Kopie bekommt und nichts zurückgeben kann, und wie man einem einzelnen Befehl eine eigene Einstellung mitgibt.
:::

:::::vorwissen Was du dafür brauchst: Prozesse und bash -c

<span class="anker" id="stufe-4-1"></span>

<ul>

<li>

Ein Prozess hat seinen eigenen Speicher und sein eigenes Arbeitsverzeichnis; der Kernel hält Prozesse voneinander getrennt. Für jedes Programm startet die Shell einen neuen Prozess, einen eingebauten Befehl führt sie selbst aus. Deshalb muss `cd` eingebaut sein ([Kapitel 4, Abschnitt 1.2](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/prozesse-und-ihre-drei-strome.html#stufe-1-2); [Kapitel 2, Abschnitt 3.3](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/arten-von-befehlen.html#stufe-3-3)).

</li>

<li>

`bash -c '…'` startet eine weitere bash, die den Text in den Anführungszeichen als Befehlszeile ausführt ([Kapitel 4, Abschnitt 5.1](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/der-exit-status.html#stufe-5-1)).

</li>

<li>

Zwischen einfachen Anführungszeichen setzt die Shell nichts ein, zwischen doppelten setzt sie Werte mit `$` ein (Unterabschnitte [3.4](worttrennung-und-quoting.html#stufe-3-4) und [3.5](worttrennung-und-quoting.html#stufe-3-5)).

</li>

</ul>

⁠**Kurz gesagt:** Du brauchst den Prozess mit seinem eigenen Speicher, `bash -c` und den Unterschied zwischen einfachen und doppelten Anführungszeichen.

:::::

### Der Kindprozess

<span class="anker" id="stufe-4-2"></span>

Eine Variable, die du in der Shell anlegst, liegt im Speicher des Shell-Prozesses. Ein Programm, das die Shell startet, läuft in einem anderen Prozess mit eigenem Speicher. Kennt es die Variablen der Shell?

:::definition Definition 4.1 (Kindprozess, Elternprozess)
<span class="anker" id="satz-4-1"></span>

Startet ein Prozess einen anderen, ist der neue Prozess ein __Kindprozess__ des ersten. Der startende Prozess heißt sein __Elternprozess__.
:::

Jedes Programm, das du in der Shell startest, ist ein Kindprozess der Shell, auch eine zweite bash, die du mit `bash -c` startest. Abbildung [15](#abb-15) zeigt, was passiert, wenn so ein Kind eine Variable der Shell braucht.

:::abbildung linux/k5kind 15
Die Shell mit der Variablen `obst=Apfel` startet zweimal ein Kind. Oben mit einfachen Anführungszeichen: Das Kind bekommt den Text `echo Obst: $obst`, sucht selbst nach `obst` und findet nichts. Unten mit doppelten: Die Shell setzt den Wert vor dem Start ein, das Kind bekommt schon `echo Obst: Apfel`.
:::

::::beispiel Wer setzt den Wert ein?
```console
$ obst=Apfel
$ bash -c 'echo Obst: $obst'
Obst:
$ bash -c "echo Obst: $obst"
Obst: Apfel
```

In der ersten Zeile verhindern die einfachen Anführungszeichen, dass die Shell `$obst` ersetzt; die Kind-Shell bekommt den Text unverändert und kennt keine Variable `obst`. In der zweiten Zeile ersetzt die Shell `$obst` schon vor dem Start; das Kind muss nichts mehr nachschlagen. Die Variable selbst hat es in keinem der beiden Fälle bekommen.
::::

⁠**Kurz gesagt:** Ein Prozess, den ein anderer startet, ist dessen Kindprozess; die Variablen der Shell bekommt er nicht von selbst.

### Die Umgebung

<span class="anker" id="stufe-4-3"></span>

Manche Angaben braucht fast jedes Programm: wo das Heimatverzeichnis liegt, wie der Benutzer heißt, in welcher Sprache Meldungen erscheinen sollen. Dafür gibt es einen festen Weg von Prozess zu Prozess. Als Bild zur Orientierung: Jedes Programm bekommt beim Start zwei Zettel mit, einen mit seinen Argumenten und einen mit allgemeinen Einstellungen; Abbildung [16](#abb-16) zeigt beide.

:::abbildung linux/k5umgebung 16
Was ein Prozess beim Start mitbekommt: links die Argumentliste, hier `printenv HOME USER`, rechts die Umgebung, eine Liste von Einträgen der Form `NAME=wert` wie `HOME=/home/student` und `LANG=C.UTF-8`. `printenv` sucht in der Umgebung die Einträge zu seinen Argumenten heraus.
:::

:::definition Definition 4.2 (Umgebung)
<span class="anker" id="satz-4-2"></span>

Die __Umgebung__ eines Prozesses ist eine Liste von Texten der Form `NAME=wert`, die der Prozess beim Start mitbekommt, zusätzlich zu seinen Argumenten. Jedes Programm entscheidet selbst, welche Einträge es beachtet.
:::

Der Befehl `printenv` schreibt die Umgebung, eine Zeile je Eintrag. Mit Namen als Argumenten schreibt er nur deren Werte; fehlt ein Name in der Umgebung, schreibt er nichts und endet mit dem Exit-Status 1.

::::beispiel Einträge der Umgebung
```console
$ printenv HOME USER SHELL LANG
/home/student
student
/bin/bash
C.UTF-8
$ printenv obst
$ echo $?
1
```

`HOME` nennt das Heimatverzeichnis, `USER` den Benutzer, `SHELL` die Shell, die bei der Anmeldung startet, und `LANG` die Spracheinstellung. Die Variable `obst` steht nicht in der Umgebung von `printenv`, obwohl die Shell sie kennt.
::::

Auch die Tilde-Erweiterung benutzt einen solchen Eintrag: Für eine Tilde ohne Benutzernamen setzt die Shell den Wert von `HOME` ein, den sie selbst beim Start in ihrer Umgebung bekommen hat.

⁠**Kurz gesagt:** Die Umgebung ist eine Liste von Einträgen `NAME=wert`, die jeder Prozess beim Start mitbekommt; `printenv` zeigt sie.

### Die Umgebungsvariable: export

<span class="anker" id="stufe-4-4"></span>

Die Shell kennt also Variablen, die nicht in der Umgebung ihrer Kinder landen. Soll ein Programm einen Wert bekommen, muss man die Shell anweisen, ihn weiterzugeben. Abbildung [17](#abb-17) zeigt, was das in der Shell ändert.

:::abbildung linux/k5export 17
In der Shell liegen Variablen, ein Teil davon trägt eine Markierung zum Weitergeben. `export obst` setzt die Markierung auch an `obst`. Beim Start eines Kindes schreibt die Shell genau die markierten Variablen in dessen Umgebung; nicht markierte bleiben in der Shell.
:::

:::definition Definition 4.3 (Umgebungsvariable, export)
<span class="anker" id="satz-4-3"></span>

Eine __Umgebungsvariable__ ist eine Shell-Variable, die zum Weitergeben markiert ist; die Shell schreibt alle markierten Variablen in die Umgebung jedes Kindprozesses. Der eingebaute Befehl __export__ markiert eine Variable: `export NAME` markiert eine vorhandene, `export NAME=wert` weist zu und markiert in einem Schritt. Variablen, die die Shell bei ihrem eigenen Start in ihrer Umgebung vorfindet, sind von Anfang an markiert.
:::

Deshalb kennt jedes Programm `HOME` und `USER`: Die Shell hat sie selbst schon in ihrer Umgebung bekommen und gibt sie weiter. Eine Gewohnheit verhindert Verwechslungen: Umgebungsvariablen des Systems heißen in Großbuchstaben, eigene Variablen schreibt man klein, wie in diesem Kapitel.

::::beispiel Ein Wert für die Kinder
```console
$ export obst
$ bash -c 'echo Obst: $obst'
Obst: Apfel
$ printenv obst
Apfel
$ export gemuese=Karotte
$ bash -c 'echo Gemüse: $gemuese'
Gemüse: Karotte
```

Dieselbe Zeile wie in Unterabschnitt [4.2](#stufe-4-2) findet jetzt einen Wert, weil `obst` in der Umgebung der Kind-Shell steht. Auch `printenv` sieht die Variable nun.
::::

⁠**Kurz gesagt:** `export` markiert eine Shell-Variable als Umgebungsvariable; jedes Kind bekommt sie in seiner Umgebung.

:::hintergrund Markierung entfernen und Variablen löschen
`export -n NAME` nimmt die Markierung wieder weg; die Variable bleibt in der Shell, Kinder bekommen sie nicht mehr. `unset NAME` löscht die Variable ganz.

```console
$ export -n gemuese
$ bash -c 'echo Gemüse: $gemuese Ende'
Gemüse: Ende
$ echo Gemüse: $gemuese
Gemüse: Karotte
$ unset gemuese
$ echo Gemüse: $gemuese Ende
Gemüse: Ende
```
:::

### Die Vererbung als Kopie

<span class="anker" id="stufe-4-5"></span>

Bekommt ein Kind seine Umgebung, stellt sich die umgekehrte Frage: Was geschieht, wenn das Kind einen Wert ändert? Kommt die Änderung bei der Shell an? Abbildung [18](#abb-18) zeigt den Ablauf.

:::abbildung linux/k5vererbung 18
Die Vererbung der Umgebung als Zeitleiste. Beim Start bekommt das Kind eine Kopie der Umgebung der Shell, mit `obst=Apfel`. Das Kind ändert seine Kopie in `obst=Birne`. Der Weg zurück zur Shell ist durchgestrichen: Endet das Kind, verschwindet seine Kopie, und die Shell hat weiter `obst=Apfel`.
:::

:::satz Satz 4.4 (Vererbung der Umgebung)
<span class="anker" id="satz-4-4"></span>

Ein Kindprozess bekommt beim Start eine Kopie der Umgebung seines Elternprozesses. Was er danach an seinen Variablen ändert, ändert nur seine Kopie; nichts davon gelangt zum Elternprozess zurück. Ebenso erreicht eine spätere Änderung im Elternprozess ein Kind, das schon läuft, nicht mehr.
:::

::::beispiel Das Kind ändert nur seine Kopie
```console
$ bash -c 'obst=Birne; echo Im Kind: $obst'
Im Kind: Birne
$ echo In der Shell: $obst
In der Shell: Apfel
$ bash -c 'export neu=Zitrone; echo Im Kind: $neu'
Im Kind: Zitrone
$ echo In der Shell: $neu Ende
In der Shell: Ende
```

Die Kind-Shell hat `obst` geändert und sogar eine neue Variable exportiert. Bei der Shell ist davon nichts angekommen. Ein `export` im Kind wirkt nur für dessen eigene Kinder.
::::

Daraus folgt eine Regel, die oft überrascht: Kein Programm, das du startest, kann die Variablen deiner Shell ändern, auch keine zweite Shell. Es ist dieselbe Trennung, wegen der `cd` eingebaut sein muss.

⁠**Kurz gesagt:** Ein Kind erbt eine Kopie der Umgebung; es kann sie ändern, aber nichts davon zurückgeben.

:::hintergrund Warum es nur eine Kopie gibt
Unter Linux entsteht ein neuer Prozess in zwei Schritten, die [Kapitel 4, Abschnitt 2.1](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/ausgaben-umleiten.html#stufe-2-1) schon für Umleitungen beschrieben hat. Mit `fork` legt der Kernel eine Kopie des Elternprozesses an, mit eigenem Speicher; die Umgebung liegt in diesem Speicher und wird deshalb mitkopiert. Mit `exec` lädt der Kindprozess dann das neue Programm; dabei übergibt er die Umgebung, bei einer Shell die Liste ihrer exportierten Variablen, als Texte `NAME=wert`, und der Kernel legt sie in den Speicher des neuen Programms. Ab diesem Augenblick gibt es zwei getrennte Listen in zwei getrennten Speichern. Der Kernel hält die Speicher der Prozesse getrennt: Ein gewöhnliches Programm kann nicht in den Speicher eines anderen schreiben, und es gibt keinen Systemaufruf, der die Umgebung des Elternprozesses ändert.

Dass das so gewollt ist, steht schon in der Anleitung, mit der Stephen Bourne 1978 seine Shell vorstellte: Für ein aufgerufenes Programm werden Kopien der exportierten Variablen angelegt, und Änderungen darin wirken nicht auf die aufrufende Shell. Ein Programm soll den Zustand dessen, der es aufgerufen hat, nicht ohne dessen ausdrücklichen Wunsch ändern können. Als Bild zur Orientierung: Das Kind bekommt eine Fotokopie und kein Original; was es auf seine Kopie schreibt, steht nicht auf dem Original.
:::

### Eine Variable nur für einen Befehl

<span class="anker" id="stufe-4-6"></span>

Manchmal soll nur ein einziger Befehl eine andere Einstellung bekommen. Ein Beispiel ist die Zeitzone: Die Umgebungsvariable `TZ` bestimmt, in welcher Zeitzone Programme wie `date` die Uhrzeit anzeigen. Ist sie nicht gesetzt, gilt die Zeitzone des Systems. Wer wissen will, wie spät es gerade in Tokio ist, will dafür nicht die Einstellung der ganzen Shell ändern. Abbildung [19](#abb-19) zeigt, wie die Shell das löst.

:::abbildung linux/k5einbefehl 19
`TZ=Asia/Tokyo date`: Die Shell gibt dem Kind `date` eine Kopie ihrer Umgebung und hängt den Eintrag `TZ=Asia/Tokyo` an. Die Umgebung der Shell selbst bleibt ohne `TZ`; der nächste Befehl bekommt den Eintrag nicht mehr.
:::

:::definition Definition 4.5 (Zuweisung vor einem Befehl)
<span class="anker" id="satz-4-5"></span>

Stehen vor dem Befehlsnamen eine oder mehrere Zuweisungen `NAME=wert`, kommen sie nur in die Umgebung dieses einen Befehls. Die Shell selbst behält ihre Variablen, wie sie waren.
:::

Wirksam werden solche Zuweisungen erst, nachdem die Shell die übrigen Wörter der Zeile erweitert hat; ein `$NAME` in derselben Zeile bekommt also noch den Wert der Shell.

::::beispiel Wie spät ist es anderswo?
```console
$ date +%H:%M
07:26
$ TZ=Asia/Tokyo date +%H:%M
15:26
$ TZ=America/New_York date +%H:%M
01:26
$ echo TZ: $TZ Ende
TZ: Ende
```

`+%H:%M` verlangt nur Stunde und Minute. Das Testsystem steht in Berlin; im November ist Tokio acht Stunden voraus, New York sechs Stunden zurück. Die Namen der Zeitzonen haben die Form `Erdteil/Stadt`; sie entsprechen Dateien unter `/usr/share/zoneinfo`. Nach den beiden Befehlen hat die Shell weiterhin kein `TZ`. Bei dir stehen andere Uhrzeiten da, die Abstände bleiben gleich, solange keine der Städte gerade die Uhr umgestellt hat.
::::

::::beispiel [Zweites Beispiel] Eine Kirsche nur für das Kind
```console
$ obst=Kirsche bash -c 'echo Obst: $obst'
Obst: Kirsche
$ echo Obst: $obst
Obst: Apfel
```

Die Kind-Shell sieht `Kirsche`, die Shell selbst behält `Apfel`.
::::

⁠**Kurz gesagt:** `NAME=wert befehl` gibt nur diesem Befehl eine eigene Einstellung mit; die Shell bleibt unverändert.

### env und printenv

<span class="anker" id="stufe-4-7"></span>

Um zu verstehen, was ein Programm aus seiner Umgebung liest, hilft es, die Umgebung gezielt zu verändern: einen Eintrag weglassen oder ganz ohne Umgebung starten.

:::definition Definition 4.6 (env)
<span class="anker" id="satz-4-6"></span>

Der Befehl __env__ startet einen Befehl mit veränderter Umgebung. `env NAME=wert befehl` fügt Einträge hinzu, `env -u NAME befehl` lässt einen weg, und `env -i befehl` startet den Befehl mit leerer Umgebung. Ohne Befehl schreibt `env` die Umgebung wie `printenv`.
:::

Dasselbe wie `env NAME=wert befehl` erreicht man in bash mit einer Zuweisung vor dem Befehl. `env` ist aber ein eigenes Programm und funktioniert deshalb auch dort, wo keine Shell die Zeile liest.

::::beispiel Leer und ohne einen Eintrag
```console
$ env -i printenv
$ env -i bash -c printenv
PWD=/home/student/linuxk5
SHLVL=0
_=/usr/bin/printenv
$ env -u obst bash -c 'echo Obst: $obst Ende'
Obst: Ende
```

Mit leerer Umgebung findet `printenv` nichts. Eine bash, die mit leerer Umgebung startet, legt selbst drei Einträge an: das Arbeitsverzeichnis `PWD`, die Verschachtelungstiefe `SHLVL` und in `_` den Pfad des Programms, das sie startet. In der letzten Zeile fehlt `obst` in der Umgebung des Kindes, obwohl die Shell die Variable exportiert hat.
::::

Tabelle [2](#tab-2) nennt Umgebungsvariablen, die dir oft begegnen.

<span class="anker" id="tab-2"></span>

**Tabelle 2:** Häufige Umgebungsvariablen.

| Variable | Bedeutung |
|---|---|
| `HOME` | Heimatverzeichnis; die Tilde wird durch diesen Wert ersetzt |
| `USER` | Name des Benutzers |
| `SHELL` | die Shell, die bei der Anmeldung des Benutzers startet |
| `PWD` | Arbeitsverzeichnis; `cd` hält den Wert aktuell |
| `LANG` | Spracheinstellung: Sprache von Meldungen, Reihenfolge beim Sortieren; auf dem Testsystem `C.UTF-8` |
| `LC_ALL` | überstimmt `LANG`, wenn gesetzt; meist leer |
| `TERM` | Art des Terminals, damit Programme Farben und Steuerzeichen richtig senden |
| `TZ` | Zeitzone, meist nicht gesetzt |
| `PATH` | der Suchpfad aus Kapitel 2, Abschnitt 3.2 |

⁠**Kurz gesagt:** `printenv` zeigt die Umgebung, `env` startet einen Befehl mit veränderter oder leerer Umgebung.

### Aufgaben zu Abschnitt [4](#stufe-4)

<span class="anker" id="stufe-4-8"></span>

:::aufgabe Aufgabe 13 ★ Wer setzt ein?
<span class="anker" id="aufg-13"></span>

In deiner Shell gilt `tier=Katze`, die Variable ist nicht exportiert. Sage voraus, was diese drei Zeilen ausgeben, und prüfe es: (a) `bash -c 'echo Tier: $tier'` (b) `bash -c "echo Tier: $tier"` (c) `bash -c 'echo Heim: $HOME'`. Begründe insbesondere, warum (c) einen Wert zeigt, (a) aber nicht.

:::loesung
```console
$ tier=Katze
$ bash -c 'echo Tier: $tier'
Tier:
$ bash -c "echo Tier: $tier"
Tier: Katze
$ bash -c 'echo Heim: $HOME'
Heim: /home/student
```

(a) Die einfachen Anführungszeichen geben den Text unverändert an die Kind-Shell; diese sucht `tier` in ihren Variablen und findet nichts, weil `tier` nicht exportiert ist. (b) Die Shell setzt `Katze` schon vor dem Start ein. (c) Auch hier ersetzt erst die Kind-Shell, aber `HOME` ist eine Umgebungsvariable: Die Shell hat sie bei ihrem eigenen Start in der Umgebung vorgefunden, sie ist deshalb markiert, und das Kind bekommt sie in seiner Umgebung.
:::
:::

:::aufgabe Aufgabe 14 ★★ Vererbung Schritt für Schritt
<span class="anker" id="aufg-14"></span>

Führe nacheinander aus und sage vor jeder Zeile mit `echo` das Ergebnis voraus: `gruss=hallo`, `bash -c 'echo Gruß: $gruss'`, `export gruss`, dieselbe Zeile noch einmal, `gruss=servus bash -c 'echo Gruß: $gruss'`, `echo Gruß: $gruss`, `bash -c 'gruss=tschüss; export gruss'`, `echo Gruß: $gruss`. Erkläre danach in zwei Sätzen, warum ein Programm, das intern `export` benutzt, die Variablen deiner Shell nicht ändern kann.

:::loesung
```console
$ gruss=hallo
$ bash -c 'echo Gruß: $gruss'
Gruß:
$ export gruss
$ bash -c 'echo Gruß: $gruss'
Gruß: hallo
$ gruss=servus bash -c 'echo Gruß: $gruss'
Gruß: servus
$ echo Gruß: $gruss
Gruß: hallo
$ bash -c 'gruss=tschüss; export gruss'
$ echo Gruß: $gruss
Gruß: hallo
```

Vor `export` ist `gruss` nur eine Shell-Variable, das Kind bekommt sie nicht. Danach steht sie in jeder Kind-Umgebung. Die Zuweisung vor dem Befehl gilt nur für dieses eine Kind; die Shell behält `hallo`. Die letzte Kind-Shell ändert und exportiert `gruss`, aber nur in ihrer eigenen Kopie. Zur Erklärung: Ein Programm bekommt beim Start eine Kopie der Umgebung in seinem eigenen Speicher. Ein `export` darin ändert nur diese Kopie und wirkt höchstens auf die Kinder dieses Programms, nie zurück auf die Shell, die es gestartet hat.
:::
:::

:::aufgabe Aufgabe 15 ★★ Weltzeituhr
<span class="anker" id="aufg-15"></span>

Lass dir mit drei Zeilen die aktuelle Uhrzeit in Tokio, New York und Sydney ausgeben (Zeitzonen `Asia/Tokyo`, `America/New_York`, `Australia/Sydney`). Warum ist `TZ` danach in deiner Shell immer noch leer? Um wie viele Stunden ist Sydney im November Berlin voraus?

:::loesung
```console
$ TZ=Asia/Tokyo date +%H:%M
15:29
$ TZ=America/New_York date +%H:%M
01:29
$ TZ=Australia/Sydney date +%H:%M
17:29
$ echo TZ: $TZ Ende
TZ: Ende
```

Die Uhrzeiten hängen davon ab, wann du die Zeilen ausführst. `TZ` stand jedes Mal nur in der Umgebung des einen `date`-Prozesses; die Shell selbst hat keine Variable `TZ` bekommen. Die Testsitzung lief um 7:29 Uhr Berliner Zeit. Sydney zeigte 17:29, ist also zehn Stunden voraus: Berlin hat im November Winterzeit, eine Stunde vor der Weltzeit, Sydney dagegen Sommerzeit, elf Stunden vor der Weltzeit.
:::
:::

:::aufgabe Aufgabe 16 ★★★ Die Kirsche, die nicht ankommt
<span class="anker" id="aufg-16"></span>

In deiner Shell gilt `obst=Apfel`. Sage voraus, was (a) `obst=Kirsche echo Obst: $obst`, (b) `obst=Kirsche printenv obst` und (c) `obst=Kirsche bash -c 'echo Obst: $obst'` ausgeben, und prüfe es. Erkläre das Ergebnis von (a) mit der Reihenfolge, in der die Shell eine Zeile bearbeitet.

:::loesung
```console
$ obst=Apfel
$ obst=Kirsche echo Obst: $obst
Obst: Apfel
$ obst=Kirsche printenv obst
Kirsche
$ obst=Kirsche bash -c 'echo Obst: $obst'
Obst: Kirsche
```

(a) Die Shell expandiert zuerst die Wörter der Zeile, die keine Zuweisungen sind; dabei wird `$obst` durch den Wert der Shell ersetzt, `Apfel`. Erst danach wird `obst=Kirsche` für den Befehl wirksam, und da hat `echo` sein Argument schon. `echo` liest die Umgebung gar nicht, es schreibt nur seine Argumente. (b) `printenv` liest die Umgebung, in der `obst=Kirsche` steht. (c) Die einfachen Anführungszeichen verschieben das Einsetzen in die Kind-Shell, und deren Umgebung enthält `obst=Kirsche`.
:::
:::

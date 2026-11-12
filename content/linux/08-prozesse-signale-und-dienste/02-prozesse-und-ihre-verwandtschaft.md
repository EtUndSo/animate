---
title: Prozesse und ihre Verwandtschaft
pfad: Informatik / Linux und Kommandozeile / Prozesse, Signale und Dienste
adresse: informatik/linux-und-kommandozeile/prozesse-signale-und-dienste
knoten: Kapitel 8: Prozesse, Signale und Dienste
order: 6130200
summary: Für Linux ist jedes laufende Programm ein Prozess.
tags: Prozess, Zeitteilung, Planer, Prozessnummer, Nummer des Elternprozesses, fork, exec, wait
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Für Linux ist jedes laufende Programm ein Prozess. Dieser Abschnitt zeigt, was zu einem Prozess gehört, wie sich viele Prozesse wenige Rechenkerne teilen, wie Linux Prozesse nummeriert und wie ein neuer Prozess entsteht. Dabei zeigt sich, dass alle Prozesse eines Systems einen einzigen Stammbaum bilden.
:::

:::::vorwissen Was du dafür brauchst: Prozess, Exit-Status und Benutzer

<span class="anker" id="stufe-1-1"></span>

Dieses Kapitel setzt die [Kapitel 1](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/ein-linux-zum-ueben.html) bis 7 voraus. Daraus brauchst du vor allem diese Dinge.

<ul>

<li>

Ein Prozess ist ein Programm in Ausführung, mit eigenem Speicher, geöffneten Dateien und einem Arbeitsverzeichnis. Der Kernel hält Prozesse voneinander getrennt und gibt jedem eine Prozessnummer; unter `/proc/<Nummer>` zeigt er Angaben zu jedem Prozess, und `/proc/self` zeigt immer auf den Prozess, der gerade nachschaut ([Kapitel 4, Abschnitt 1.2](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/prozesse-und-ihre-drei-strome.html#stufe-1-2); [Kapitel 3, Abschnitt 7.8](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/die-verzeichnisstruktur-von-linux.html#stufe-7-8)).

</li>

<li>

Geöffnete Dateien führt der Kernel für jeden Prozess unter kleinen Zahlen, den Dateideskriptoren 0, 1 und 2 für die drei Standardströme. Ein neuer Prozess erbt sie. Die Shell richtet Umleitungen ein, bevor das Programm startet ([Kapitel 4, Abschnitte 1.7](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/prozesse-und-ihre-drei-strome.html#stufe-1-7) und [2.1](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/ausgaben-umleiten.html#stufe-2-1)).

</li>

<li>

Jedes Programm hinterlässt beim Ende einen Exit-Status, die Shell zeigt ihn mit `echo $?`. Endet ein Programm durch eine Unterbrechungsnachricht mit der Nummer $n$, meldet die Shell $128 + n$; Strg+C schickt die Nachricht 2, deshalb steht danach 130 ([Kapitel 4, Abschnitte 5.1](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/der-exit-status.html#stufe-5-1) und [5.3](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/der-exit-status.html#stufe-5-3); [Kapitel 2, Abschnitt 5.4](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/schneller-arbeiten-vervollstandigung-verlauf-tastenkurzel.html#stufe-5-4)).

</li>

<li>

Ein Prozess, den ein anderer startet, heißt Kindprozess, der startende Elternprozess. Das Kind bekommt eine Kopie der Umgebung und kann dem Elternprozess nichts zurückgeben. `bash -c 'befehle'` startet eine neue bash, die nur die angegebenen Befehle ausführt ([Kapitel 5, Abschnitte 4.2](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/umgebung-und-vererbung.html#stufe-4-2) und [4.5](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/umgebung-und-vererbung.html#stufe-4-5); [Kapitel 4, Abschnitt 5.1](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/der-exit-status.html#stufe-5-1)).

</li>

<li>

Jeder Prozess trägt die Benutzernummer seines Benutzers als Kopie bei sich; bei Programmen mit SUID-Bit unterscheiden sich reale und effektive Benutzernummer. `sudo befehl` führt einen Befehl als root aus ([Kapitel 7, Abschnitte 1.6](/wissen/informatik/linux-und-kommandozeile/benutzer-gruppen-und-rechte/benutzer-und-gruppen.html#stufe-1-6) und [9.2](/wissen/informatik/linux-und-kommandozeile/benutzer-gruppen-und-rechte/programme-ausfuhren-und-besondere-rechte.html#stufe-9-2); [Kapitel 7, Abschnitt 6.1](/wissen/informatik/linux-und-kommandozeile/benutzer-gruppen-und-rechte/kurzzeitig-root-sudo-und-su.html#stufe-6-1)).

</li>

<li>

`uptime` zeigt die Last, `nproc` die Zahl der Rechenkerne ([Kapitel 2, Abschnitt 6.3](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/das-system-erkunden.html#stufe-6-3)).

</li>

</ul>

⁠**Kurz gesagt:** Du brauchst den Prozess mit seiner Nummer und seinen Deskriptoren, den Exit-Status samt $128 + n$, Eltern- und Kindprozess sowie den Benutzer eines Prozesses.

:::warnung Nur eigene Versuchsprogramme beenden
In diesem Kapitel hältst du Programme an und beendest sie. Tu das nur mit Programmen, die du selbst für einen Versuch gestartet hast, meist mit `sleep`, das einfach eine Zeit lang wartet. Ein beendetes Programm kann nicht mehr speichern, was es gerade bearbeitet hat; trifft es ein Programm des Systems, kann der Rechner hängen bleiben. Dateien legst du nur in einem eigenen Übungsverzeichnis an:

```console
$ mkdir ~/linuxk8
$ cd ~/linuxk8
```

Öffnest du ein zweites Terminal, wechselst du auch dort mit `cd ~/linuxk8` in dieses Verzeichnis.
:::

:::::

### Programm und Prozess, genauer

<span class="anker" id="stufe-1-2"></span>

[Kapitel 4](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/stroeme-umleitung-pipes-und-exit-status.html) hat den Prozess als laufendes Programm eingeführt, so wie das Kochen eines Gerichts zum Rezept gehört. Für dieses Kapitel brauchst du ein genaueres Bild: Was muss der Kernel über einen Prozess wissen, damit er ihn anhalten und später genau dort weitermachen lassen kann, wo er stand?

Das Bild vom Kochen hilft weiter. Wer mitten im Rezept unterbrochen wird, muss sich merken, bei welchem Schritt er war, was schon in den Töpfen ist und welche Zutaten bereitliegen. Genauso merkt sich der Kernel für jeden Prozess alles, was zu seinem augenblicklichen Stand gehört.

:::definition Definition 1.1 (Prozess, genauer)
<span class="anker" id="satz-1-1"></span>

Ein __Prozess__ ist ein Programm in Ausführung zusammen mit allem, was zu seinem augenblicklichen Stand gehört: dem Programm, das er ausführt, seinem Speicher, der Stelle im Programm, an der er gerade steht, seinen geöffneten Dateien, seinem Arbeitsverzeichnis, seiner Umgebung und seinem Benutzer. Der Kernel führt diese Angaben für jeden Prozess in einem eigenen Eintrag.
:::

Das Programm selbst ist nur eine Datei auf dem Datenträger; es tut nichts, solange niemand es startet. Erst der Prozess arbeitet. Deshalb kann dasselbe Programm in beliebig vielen Prozessen gleichzeitig laufen, jeder mit eigenem Speicher und an seiner eigenen Stelle im Programm. Einen Teil des Eintrags zeigt der Kernel unter `/proc`: Für die laufende Shell sind `/proc/<Nummer>/exe` das Programm, `cwd` das Arbeitsverzeichnis und `fd` die geöffneten Dateien.

⁠**Kurz gesagt:** Ein Prozess ist ein laufendes Programm samt seinem ganzen augenblicklichen Stand; der Kernel führt für jeden Prozess einen Eintrag mit diesen Angaben.

### Viele Prozesse, wenige Kerne: die Zeitteilung

<span class="anker" id="stufe-1-3"></span>

Ein Rechner hat einige wenige Rechenkerne, auf dem Testsystem 14. Gleichzeitig existieren aber Dutzende oder Hunderte Prozesse. Trotzdem scheinen alle zugleich zu arbeiten: Die Uhr läuft weiter, während eine Datei kopiert wird. Wie geht das?

Stell dir eine Küche mit wenigen Herdplatten und vielen Gerichten vor. Ein Koch stellt einen Topf kurz auf die Platte, nimmt ihn wieder herunter, stellt den nächsten darauf, und so fort, so schnell, dass alle Gerichte vorankommen. Das ist ein Bild zur Orientierung; der Mechanismus im Rechner ist der folgende.

:::definition Definition 1.2 (Zeitteilung, Planer)
<span class="anker" id="satz-1-2"></span>

Bei der __Zeitteilung__ lässt der Kernel einen Prozess eine kurze Zeit auf einem Kern rechnen, hält ihn dann an, sichert seinen Stand und lässt einen anderen Prozess weiterrechnen. Den Teil des Kernels, der entscheidet, welcher Prozess als Nächstes rechnen darf, nennt man den __Planer__ (englisch „scheduler“). Ein Wechsel von einem Prozess zum nächsten heißt Kontextwechsel.
:::

Ein Prozess, der auf etwas wartet, etwa auf eine Taste, braucht keinen Kern. Er gibt seinen Platz sofort ab, und der Planer lässt ihn erst wieder rechnen, wenn das Erwartete eingetroffen ist. Abbildung [1](#abb-1) zeigt den Wechsel auf einem Kern.

:::abbildung linux/k8zeitteilung 1
Ein Rechenkern und drei Prozesse A, B und C, jeder mit einem Kästchen „Stand“ (Stelle im Programm). Eine Zeitleiste läuft nach rechts: Zuerst rechnet A, sein Stand-Zähler läuft; dann sichert der Kernel den Stand von A, lädt den Stand von B, und B rechnet; dann C. B wartet einmal auf eine Taste und gibt den Kern vor Ablauf seiner Zeit ab, bis die Taste kommt. Unter der Zeitleiste wächst ein Zähler „Kontextwechsel“. Am Ende sind alle drei Fortschrittsbalken gewachsen, obwohl immer nur einer rechnete.
:::

::::beispiel Der Kernel wechselt ständig
Wie viele Kerne der Rechner hat, nennt `nproc`. Wie oft der Kernel seit dem Start zwischen Prozessen gewechselt hat, steht in der Zeile `ctxt` der Datei `/proc/stat`. Liest man sie zweimal im Abstand von einer Sekunde, sieht man die Wechsel dieser Sekunde:

```console
$ nproc
14
$ grep ctxt /proc/stat; sleep 1; grep ctxt /proc/stat
ctxt 53338
ctxt 53495
```

In dieser Sekunde wechselte der Kernel $53\,495 - 53\,338 = 157$-mal, obwohl auf dem Testsystem fast nichts zu tun war. Auf einem Rechner mit Desktop und Browser sind es leicht Tausende in der Sekunde.
::::

⁠**Kurz gesagt:** Der Kernel teilt die wenigen Kerne in kurzen Abschnitten reihum zwischen den Prozessen auf; welcher als Nächstes rechnet, entscheidet der Planer.

### Die Prozessnummer: PID

<span class="anker" id="stufe-1-4"></span>

Um einen bestimmten Prozess anzusprechen, etwa um ihn zu beenden, braucht man einen eindeutigen Namen für ihn. Programmnamen taugen dafür nicht, denn dasselbe Programm kann in vielen Prozessen laufen. [Kapitel 4](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/stroeme-umleitung-pipes-und-exit-status.html) hat dafür schon die Prozessnummer benutzt; hier bekommt sie ihre übliche Abkürzung.

:::definition Definition 1.3 (Prozessnummer, PID)
<span class="anker" id="satz-1-3"></span>

Die __Prozessnummer__ (englisch „process identifier“, kurz PID) ist eine ganze Zahl, die der Kernel einem Prozess bei seiner Entstehung gibt. Solange der Prozess besteht, trägt kein anderer Prozess dieselbe Nummer.
:::

Die Shell kennt ihre eigene Nummer: Der Parameter `$$` wird durch die PID der Shell ersetzt, wie `$?` durch den Exit-Status ([Kapitel 5, Abschnitt 2.2](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/variablen-befehlsersetzung-und-arithmetik.html#stufe-2-2)).

::::beispiel Dasselbe Programm, verschiedene Prozesse
Die Shell und jede neue bash, die du mit `bash -c` startest, führen dasselbe Programm `/usr/bin/bash` aus. Trotzdem hat jede ihre eigene Nummer:

```console
$ echo $$
535
$ bash -c 'echo $$'
550
$ bash -c 'echo $$'
551
```

Die einfachen Anführungszeichen sorgen dafür, dass erst die neue bash `$$` ersetzt, nicht schon die Shell, in der du tippst ([Kapitel 5, Abschnitt 3.4](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/worttrennung-und-quoting.html#stufe-3-4)). Jede neue bash ist ein neuer Prozess und bekommt eine neue Nummer; der zweite Aufruf bekommt die nächste freie Nummer.
::::

Der Kernel vergibt die Nummern der Reihe nach aufsteigend. Ist die größte erlaubte Nummer erreicht, beginnt er wieder unten und überspringt Nummern, die noch vergeben sind. Die Obergrenze steht in einer Datei des Kernels:

```console
$ cat /proc/sys/kernel/pid_max
4194304
```

Der Wert ist $2^{22} = 4\,194\,304$; die größte Nummer, die der Kernel vergibt, ist um eins kleiner. Eine PID ist also nur eindeutig, solange der Prozess lebt: Nach seinem Ende kann irgendwann ein ganz anderer Prozess dieselbe Nummer bekommen. Abbildung [2](#abb-2) zeigt die Vergabe.

:::abbildung linux/k8pidvergabe 2
Ein Zähler „nächste PID“ steht auf 550. Nacheinander entstehen Prozesse und bekommen 550, 551, 552; der Zähler läuft mit. Prozess 551 endet, seine Nummer wird grau, bleibt aber übersprungen, bis der Zähler herum ist. Dann springt der Zähler im Zeitraffer bis 4 194 303 und von dort auf eine kleine Zahl zurück; bei der Suche überspringt es die Nummern, die noch vergeben sind (etwa die 535 der Shell), und vergibt die erste freie.
:::

⁠**Kurz gesagt:** Jeder Prozess hat eine Prozessnummer (PID), die ihn eindeutig bezeichnet, solange er lebt; `$$` ist die PID der Shell.

### Der Elternprozess: PPID

<span class="anker" id="stufe-1-5"></span>

Jeder Prozess wurde von einem anderen gestartet, seinem Elternprozess ([Kapitel 5, Abschnitt 4.2](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/umgebung-und-vererbung.html#stufe-4-2)). Oft muss man wissen, welcher das war: Wer hat dieses Programm gestartet, und wem meldet es sein Ende?

:::definition Definition 1.4 (Nummer des Elternprozesses, PPID)
<span class="anker" id="satz-1-4"></span>

Die __Nummer des Elternprozesses__ (englisch „parent process identifier“, kurz PPID) ist die PID des Prozesses, der einen Prozess gestartet hat. Der Kernel speichert sie im Eintrag jedes Prozesses.
:::

In der bash steht die PPID der Shell im Parameter `$PPID`. Eine neue bash, die du aus deiner Shell startest, ist ein Kind deiner Shell:

```console
$ echo $$
535
$ bash -c 'echo "Ich bin $$, mein Elternprozess ist $PPID"'
Ich bin 553, mein Elternprozess ist 535
```

Die neue bash hat die Nummer 553, ihr Elternprozess ist die Shell mit der Nummer 535.

⁠**Kurz gesagt:** Die PPID ist die PID des Elternprozesses; in der bash steht sie in `$PPID`.

### Wie ein Prozess entsteht: fork, exec und wait

<span class="anker" id="stufe-1-6"></span>

Tippst du `ls`, entsteht ein neuer Prozess, der das Programm `ls` ausführt, und die Shell meldet sich erst wieder, wenn er fertig ist. Unter Linux und allen Unix-Systemen geschieht das nicht in einem Schritt, sondern in drei Systemaufrufen ([Kapitel 1, Abschnitt 1.4](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/betriebssystem-kernel-und-distribution.html#stufe-1-4)). Jeder der drei tut genau eine Sache.

:::definition Definition 1.5 (fork, exec, wait)
<span class="anker" id="satz-1-5"></span>

<ol>

<li>

__fork__ erzeugt eine Kopie des aufrufenden Prozesses. Die Kopie ist der Kindprozess; sie führt dasselbe Programm aus, steht an derselben Stelle und hat Kopien von Speicher, Deskriptoren, Umgebung und Benutzer, aber eine neue PID.

</li>

<li>

__exec__ ersetzt das Programm des aufrufenden Prozesses durch ein anderes Programm. Es entsteht kein neuer Prozess: PID, Elternprozess, geöffnete Deskriptoren und, außer bei SUID-Programmen, der Benutzer bleiben; Speicher und Programm sind danach neu.

</li>

<li>

__wait__ lässt einen Prozess warten, bis eines seiner Kinder endet, und liefert ihm dessen Exit-Status.

</li>

</ol>
:::

Startet die Shell `ls`, ruft sie fork auf. Im Kindprozess, zunächst einer Kopie der Shell, folgt exec mit dem Programm `ls`. Die Shell selbst ruft wait auf und wartet. Endet `ls`, bekommt sie über wait den Exit-Status und zeigt die nächste Eingabeaufforderung. Abbildung [3](#abb-3) zeigt die drei Schritte auf einer Zeitleiste.

:::abbildung linux/k8forkexec 3
Zwei Spuren übereinander: oben die Shell (PID 535, Programm bash), unten zunächst leer. Schritt „fork“: Von der Shell spaltet sich eine Kopie ab und läuft auf der unteren Spur weiter (neue PID 558, Programm noch bash, Elternprozess 535). Schritt „Umleitung“: Die Kopie öffnet `liste.txt` und steckt sie auf Deskriptor 1. Schritt „exec“: In der unteren Spur wechselt das Programmschild von bash zu ls; die PID 558 bleibt hervorgehoben stehen. Gleichzeitig steht die Shell oben im Zustand „wait“. Am Ende der unteren Spur ein Kästchen „Exit-Status 0“, das nach oben zur Shell wandert; die Shell zeigt die nächste Eingabeaufforderung.
:::

Dass exec die PID behält, lässt sich direkt zeigen. Die bash kennt exec auch als eingebauten Befehl: `exec programm` ersetzt die Shell selbst durch das Programm. Als Programm dient hier `ps -o pid,ppid,comm -p nummer`; es zeigt für den Prozess mit dieser Nummer die PID, die PPID und den Namen des Programms, das er gerade ausführt.

```console
$ bash -c 'echo "Die bash hat die Nummer $$"; exec ps -o pid,ppid,comm -p $$'
Die bash hat die Nummer 554
    PID    PPID COMMAND
    554     535 ps
```

Die neue bash nennt ihre Nummer 554 und ersetzt sich dann durch `ps`. Die Zeile darunter zeigt: Der Prozess 554 führt jetzt das Programm `ps` aus, und sein Elternprozess ist weiter die Shell 535.

⁠**Kurz gesagt:** Ein neuer Prozess entsteht als Kopie (fork) und lädt dann ein anderes Programm (exec), wobei er seine PID behält; der Elternprozess wartet mit wait auf sein Ende und seinen Exit-Status.

:::hintergrund Warum zwei Schritte statt einem?
Ein einziger Aufruf „starte Programm X“ wäre doch einfacher. Der Grund für die Trennung liegt in der Lücke zwischen fork und exec. In dieser Lücke läuft schon der Kindprozess, aber noch mit dem Programm der Shell. Die Shell kann dort also beliebigen eigenen Code ausführen und den Stand des Kindes vorbereiten, bevor das neue Programm ihn übernimmt: Sie öffnet die Datei einer Umleitung und legt sie auf Deskriptor 1, sie verbindet eine Pipe, wechselt das Arbeitsverzeichnis oder ändert die Umgebung. Weil exec Deskriptoren, Arbeitsverzeichnis und Benutzer behält, findet das neue Programm alles fertig vor und muss von Umleitungen nichts wissen; die einzelnen Schritte einer Umleitung hat [Kapitel 4, Abschnitt 2.1](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/ausgaben-umleiten.html#stufe-2-1) gezeigt.

Ganz unumstritten ist der Entwurf nicht. Für Programme mit sehr viel Speicher ist eine Kopie aufwendig, und es gibt inzwischen auch einen Aufruf, der Kopie und Programmwechsel in einem erledigt. Die Shell und die meisten Programme benutzen trotzdem fork und exec.
:::

:::hintergrund Warum die Kopie trotzdem schnell geht
Ein fork kopiert den Speicher nicht sofort. Eltern und Kind benutzen dieselben Speicherseiten zunächst gemeinsam, und der Kernel markiert sie als nur lesbar. Erst wenn einer der beiden eine Seite verändern will, legt der Kernel für ihn eine eigene Kopie genau dieser Seite an. Das Verfahren heißt „Kopieren beim Schreiben“ (englisch „copy on write“). Folgt auf fork gleich exec, wird fast nichts kopiert, denn exec wirft den alten Speicher ohnehin weg.
:::

::::beispiel Den drei Schritten zusehen
Das Werkzeug `strace` aus [Kapitel 1, Abschnitt 1.4](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/betriebssystem-kernel-und-distribution.html#stufe-1-4) zeichnet Systemaufrufe auf. Mit `-f` folgt es auch den Kindprozessen, `-e trace=…` wählt die Aufrufe aus, und `-o spur.txt` schreibt alles in eine Datei. Beobachtet wird eine bash, die `ls` mit einer Umleitung startet:

```console
$ strace -f -o spur.txt -e trace=clone,execve,wait4,openat bash -c 'ls > liste.txt; true'
$ grep -E 'clone|execve|wait4|liste' spur.txt
557   execve("/usr/bin/bash", ["bash", "-c", "ls > liste.txt; true"], 0x7ffc6ee40318 /* 27 vars */) = 0
557   clone(child_stack=NULL, flags=CLONE_CHILD_CLEARTID|CLONE_CHILD_SETTID|SIGCHLD, child_tidptr=0x7504234d6a10) = 558
557   wait4(-1 <unfinished ...>
558   openat(AT_FDCWD, "liste.txt", O_WRONLY|O_CREAT|O_TRUNC, 0666) = 3
558   execve("/usr/bin/ls", ["ls"], 0x5c6f4978b1f0 /* 27 vars */) = 0
557   <... wait4 resumed>, [{WIFEXITED(s) && WEXITSTATUS(s) == 0}], 0, NULL) = 558
557   wait4(-1, 0x7ffee7efd514, WNOHANG, NULL) = -1 ECHILD (No child processes)
```

Jede Zeile beginnt mit der PID des Prozesses, der den Aufruf macht. Unter Linux erledigt die bash fork mit dem Systemaufruf `clone`; er liefert der bash 557 die PID des Kindes, 558. Danach wartet die bash in `wait4`. Das Kind 558 öffnet zuerst `liste.txt` für die Umleitung und ruft erst danach `execve` mit `/usr/bin/ls` auf, genau in der Lücke zwischen fork und exec. Dann endet `ls`, und `wait4` meldet der bash, dass das Kind 558 mit dem Status 0 geendet hat. Das angehängte `; true` verhindert eine Abkürzung: Steht hinter `bash -c` nur ein einziger Befehl, ruft die bash auf dem Testsystem gleich exec auf, ohne vorher eine Kopie anzulegen.
::::

### Der Prozessbaum und PID 1

<span class="anker" id="stufe-1-7"></span>

Jeder Prozess hat einen Elternprozess, der seinerseits einen Elternprozess hat. Verfolgt man diese Kette zurück, wo endet sie? Und wie sieht die Verwandtschaft aller Prozesse zusammen aus?

:::definition Definition 1.6 (Prozessbaum, PID 1)
<span class="anker" id="satz-1-6"></span>

Verbindet man jeden Prozess mit seinem Elternprozess, entsteht ein __Prozessbaum__. Seine Wurzel ist der erste Prozess, den der Kernel beim Hochfahren selbst startet; er hat die Nummer 1. Unter Ubuntu und den meisten heutigen Distributionen ist das Programm __systemd__.
:::

Den Baum zeichnet `pstree`; mit `-p` schreibt es die PIDs dazu, und eine Nummer als Argument wählt den Prozess, bei dem die Zeichnung beginnt. Im folgenden Beispiel startet die Shell eine bash, diese eine weitere, und die zeichnet den Baum ab der Shell:

```console
$ bash -c 'bash -c "pstree -p $PPID; true"; true'
bash(535)───bash(560)───bash(561)───pstree(562)
```

Die äußere bash setzt ihre eigene `$PPID` ein, also die Nummer der Shell, bevor sie die innere startet. Jede Stufe ist ein Kind der vorigen. Mit `-s` zeichnet `pstree` stattdessen die Vorfahren eines Prozesses bis zur Wurzel. In einem frisch geöffneten Terminal sieht das so aus; `-l` verhindert, dass `pstree` lange Zeilen abschneidet:

```console
$ pstree -l -p -s $$
systemd(1)---init-systemd(Ub(2)---SessionLeader(568)---Relay(570)(569)---bash(570)---pstree(573)
```

Ganz links steht `systemd` mit der Nummer 1. Die drei Stufen zwischen `systemd` und der Shell gehören zu WSL: `init-systemd(Ubuntu-26.04)` ist die Verbindung der Distribution zu Windows; der Name erscheint gekürzt, weil der Kernel den Programmnamen eines Prozesses nur mit höchstens 15 Zeichen speichert. `SessionLeader` und `Relay` gehören zu dem Terminal, das du in Windows geöffnet hast. WSL schreibt die Nummer der Shell in den Namen `Relay(570)`; die eigene PID des Prozesses, 569, hängt `pstree` wie überall dahinter. Auf einem Linux mit eigenem Desktop steht über der Shell stattdessen das Terminalprogramm, darüber führen weitere Stufen ebenfalls zu `systemd`. Wie der Baum über alle Prozesse aussieht, zeigt `pstree` ohne `-p` ab der Nummer 1; gleiche Zweige fasst es zusammen, etwa `2*[agetty]` für zwei gleiche Kinder:

```console
$ ps -o pid,ppid,user,cmd -p 1,2
    PID    PPID USER     CMD
      1       0 root     /sbin/init
      2       1 root     /init
$ pstree 1
systemd-+-2*[agetty]
        |-chronyd-starter---chronyd---chronyd
        |-cron
        |-dbus-daemon
...
        |-networkd-dispat
        |-rsyslogd---3*[{rsyslogd}]
        |-systemd---(sd-pam)
        |-systemd-journal
        |-systemd-logind
        |-systemd-resolve
        |-systemd-timedat
        |-systemd-udevd---8*[(udev-worker)]
        |-unattended-upgr---{unattended-upgr}
        `-wsl-pro-service---8*[{wsl-pro-service}]
```

Der erste Befehl ist `ps` mit derselben Auswahl wie oben, hier für die Prozesse 1 und 2 und mit der Spalte `user` für den Besitzer. Der Prozess 2 ist unter WSL das Programm `/init` von WSL; auf einem gewöhnlichen Linux trägt die Nummer 2 ein Prozess des Kernels selbst. Die weggelassenen Zeilen von `pstree` sind der Zweig von WSL mit den Terminals. Fast alle anderen Kinder von `systemd` sind Programme, die ohne Terminal für das System arbeiten. Namen in geschweiften Klammern sind Threads, also zusätzliche Ausführungsstränge innerhalb eines Prozesses, die sich seinen Speicher teilen. Der Prozess 1 erscheint als `/sbin/init`, denn unter diesem Namen startet ihn der Kernel. Abbildung [4](#abb-4) fasst den Baum zusammen.

:::abbildung linux/k8baum 4
Der Prozessbaum wächst von oben nach unten. Zuerst erscheint die Wurzel systemd(1). Dann die Kinder von systemd: cron, rsyslogd, systemd-journal und weitere als graue Sammelknoten, daneben der Zweig von WSL (init-systemd, SessionLeader, Relay) und darunter die Shell bash(535). Zuletzt die Kette bash(560) $\to$ bash(561) $\to$ pstree(562). Die Kante von jedem Kind zu seinem Elternprozess ist mit der PPID beschriftet; der Weg von pstree(562) bis zur Wurzel leuchtet am Ende auf.
:::

⁠**Kurz gesagt:** Alle Prozesse bilden über ihre Elternprozesse einen Baum mit dem Prozess 1, `systemd`, als Wurzel; `pstree` zeichnet ihn.

### Der Besitzer eines Prozesses

<span class="anker" id="stufe-1-8"></span>

[Kapitel 7, Abschnitt 1.6](/wissen/informatik/linux-und-kommandozeile/benutzer-gruppen-und-rechte/benutzer-und-gruppen.html#stufe-1-6) hat gezeigt, dass jeder Prozess die Nummern seines Benutzers trägt, und [Kapitel 7, Abschnitt 9.2](/wissen/informatik/linux-und-kommandozeile/benutzer-gruppen-und-rechte/programme-ausfuhren-und-besondere-rechte.html#stufe-9-2), dass es eine reale und eine effektive Benutzernummer gibt. Für dieses Kapitel zählt vor allem eine Folge davon: Wem ein Prozess gehört, entscheidet, wer ihn beobachten und steuern darf.

:::definition Definition 1.7 (Besitzer eines Prozesses)
<span class="anker" id="satz-1-7"></span>

Der __Besitzer__ eines Prozesses ist der Benutzer, dessen Nummern der Prozess trägt. Ein neuer Prozess erbt sie bei fork von seinem Elternprozess und behält sie bei exec; nur Programme mit SUID-Bit und Programme mit den Rechten von root, etwa das Anmeldeprogramm, ändern sie.
:::

Auch das Verzeichnis eines Prozesses unter `/proc` gehört seinem Besitzer:

```console
$ ls -ld /proc/$$ /proc/1
dr-xr-xr-x 9 root    root    0 Nov 10 15:24 /proc/1
dr-xr-xr-x 9 student student 0 Nov 10 15:24 /proc/535
```

Die Shell gehört `student`, der Prozess 1 gehört root. Weil jedes Kind die Nummern der Shell erbt, läuft jedes Programm, das du startest, mit allen deinen Rechten: Ein heruntergeladenes Programm kann alle deine Dateien lesen und löschen, aber keine Dateien des Systems, die nur root schreiben darf.

⁠**Kurz gesagt:** Jeder Prozess gehört dem Benutzer, dessen Nummern er von seinem Elternprozess geerbt hat.

### Aufgaben zu Abschnitt [1](#stufe-1)

<span class="anker" id="stufe-1-9"></span>

:::aufgabe Aufgabe 1 ★ Drei neue Prozesse
<span class="anker" id="aufg-1"></span>

Gib `echo $$` ein und dann dreimal hintereinander `bash -c 'echo $$ $PPID'`. Welche der Zahlen bleibt bei allen drei Aufrufen gleich, welche ändert sich, und warum?

:::loesung
```console
$ echo $$
534
$ bash -c 'echo $$ $PPID'
542 534
$ bash -c 'echo $$ $PPID'
543 534
$ bash -c 'echo $$ $PPID'
544 534
```

Die zweite Zahl, die PPID, ist bei allen drei Aufrufen 534: Jede neue bash ist ein Kind derselben Shell, und `echo $$` zeigt, dass die Shell genau diese Nummer hat. Die erste Zahl, die PID, ändert sich, denn jeder Aufruf erzeugt mit fork einen neuen Prozess, und der Kernel vergibt die Nummern aufsteigend. Dass sie hier lückenlos aufeinander folgen, liegt daran, dass gerade kein anderer Prozess entstand; auf einem beschäftigten Rechner liegen oft Lücken dazwischen.
:::
:::

:::aufgabe Aufgabe 2 ★★ exec vorhersagen
<span class="anker" id="aufg-2"></span>

Sage vorher, ob die beiden Zahlen jeweils gleich oder verschieden sind, und prüfe dann: (a) `bash -c 'echo $$; exec bash -c "echo \$\$"'` (b) `bash -c 'echo $$; bash -c "echo \$\$"; true'` (c) Warum steht vor dem inneren `$$` ein umgekehrter Schrägstrich? (d) Lass in (b) das `; true` weg. Was ändert sich, und welche Abkürzung der bash aus dem Beispiel „Den drei Schritten zusehen“ erklärt es?

:::loesung
```console
$ bash -c 'echo $$; exec bash -c "echo \$\$"'
545
545
$ bash -c 'echo $$; bash -c "echo \$\$"; true'
546
547
$ bash -c 'echo $$; bash -c "echo \$\$"'
548
548
```

(a) Beide Zahlen sind gleich: exec ersetzt das Programm der äußeren bash durch eine neue bash, legt aber keinen neuen Prozess an, und die PID bleibt. (b) Die Zahlen sind verschieden: Die äußere bash startet die innere mit fork, also als neuen Prozess mit neuer PID. (c) Der ganze Text steht für die Shell, in der du tippst, in einfachen Anführungszeichen und kommt unverändert bei der äußeren bash an. Diese sieht darin `"echo \$\$"` in doppelten Anführungszeichen; ohne den umgekehrten Schrägstrich ersetzte sie `$$` darin durch ihre eigene Nummer, bevor sie die innere bash startet, und beide Zeilen zeigten immer dieselbe Zahl ([Kapitel 5, Abschnitt 3.5](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/worttrennung-und-quoting.html#stufe-3-5)). (d) Ohne `; true` sind beide Zahlen wieder gleich. Der innere `bash -c` ist dann der letzte Befehl der äußeren bash, und für ihn ruft die bash auf dem Testsystem gleich exec auf, ohne vorher eine Kopie anzulegen; das ist die Abkürzung aus dem Beispiel in Unterabschnitt [1.6](#stufe-1-6).
:::
:::

:::aufgabe Aufgabe 3 ★★ Die Vorfahren deiner Shell
<span class="anker" id="aufg-3"></span>

Öffne ein neues Terminal und gib `pstree -l -p -s $$` ein. (a) Welcher Prozess ist die Shell, welcher `pstree`, welcher die Wurzel? (b) Welche Prozesse dazwischen gehören bei dir zu WSL oder zum Terminalprogramm? (c) Welche PPID hat die Shell?

:::loesung
```console
$ pstree -l -p -s $$
systemd(1)---init-systemd(Ub(2)---SessionLeader(553)---Relay(555)(554)---bash(555)---pstree(558)
```

(a) Ganz rechts steht `pstree` selbst (558), links davon die Shell (`bash`, 555), ganz links die Wurzel `systemd` mit der Nummer 1. (b) Unter WSL gehören `init-systemd(Ubuntu-26.04)`, `SessionLeader` und `Relay` zu WSL; das Terminalprogramm selbst läuft unter Windows und erscheint deshalb nicht. Auf einem Linux mit Desktop stehen dort stattdessen das Terminalprogramm und weitere Prozesse der Anmeldung. (c) Die PPID der Shell ist die Nummer des Prozesses links von ihr, hier 554. Er heißt `Relay(555)`, denn WSL schreibt die Nummer der Shell, für die er arbeitet, in seinen Namen; `pstree` hängt wie bei jedem Prozess seine eigene PID an.
:::
:::

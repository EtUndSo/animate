---
title: Prozesse beobachten
pfad: Informatik / Linux und Kommandozeile / Prozesse, Signale und Dienste
adresse: informatik/linux-und-kommandozeile/prozesse-signale-und-dienste
knoten: Kapitel 8: Prozesse, Signale und Dienste
order: 6130300
summary: Um ein Programm zu steuern, muss man es erst finden: Läuft es noch, unter welcher Nummer, wem gehört es, und was tut es gerade?
tags: steuernde Terminal, Zustand, Zombie
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Um ein Programm zu steuern, muss man es erst finden: Läuft es noch, unter welcher Nummer, wem gehört es, und was tut es gerade? Dieser Abschnitt zeigt die Werkzeuge dafür, `ps`, `pgrep` und `top`, erklärt die Zustände, in denen ein Prozess sein kann, und schaut in den Eintrag des Kernels unter `/proc`.
:::

### Die eigenen Prozesse: ps

<span class="anker" id="stufe-2-1"></span>

Damit es etwas zu beobachten gibt, öffne ein zweites Terminal, wechsle dort ins Übungsverzeichnis und starte ein Programm, das zehn Minuten lang wartet. Im zweiten Terminal:

```console
$ sleep 600
```

Lass es laufen und arbeite im ersten Terminal weiter. Das wichtigste Werkzeug, um Prozesse anzusehen, ist `ps` (englisch „process status“). Ohne Optionen zeigt es nur wenig:

```console
$ ps
    PID TTY          TIME CMD
    535 pts/2    00:00:00 bash
    597 pts/2    00:00:00 ps
$ tty
/dev/pts/2
```

`PID` ist die Prozessnummer, `CMD` das Programm, und `TIME` die Rechenzeit, die der Prozess bisher auf einem Kern verbraucht hat; eine Shell, die fast nur auf Eingaben wartet, bleibt lange bei null. Die Spalte `TTY` nennt das Terminal des Prozesses. `tty` zeigt den Namen des eigenen Terminals: `/dev/pts/2` ist ein Pseudoterminal ([Kapitel 2, Abschnitt 1.2](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/terminal-und-shell.html#stufe-1-2)).

:::definition Definition 2.1 (steuerndes Terminal, ps)
<span class="anker" id="satz-2-1"></span>

Das __steuernde Terminal__ eines Prozesses ist das Terminal, zu dessen Sitzung er gehört; von dort kommen seine Tastatureingaben, auch Strg+C. Ohne Optionen zeigt `ps` die Prozesse des eigenen Benutzers, die dasselbe steuernde Terminal haben wie `ps` selbst.
:::

Deshalb fehlt `sleep`: Es läuft im zweiten Terminal, also an einem anderen Pseudoterminal.

⁠**Kurz gesagt:** `ps` zeigt ohne Optionen die eigenen Prozesse am eigenen Terminal mit PID, Terminal, Rechenzeit und Programm.

### Alle Prozesse: ps -ef und ps aux

<span class="anker" id="stufe-2-2"></span>

Meist will man mehr sehen: alle Prozesse des Systems oder einen bestimmten Prozess an einem anderen Terminal. Dafür gibt es zwei Kombinationen von Optionen, die man sich am besten als feste Wörter merkt.

:::definition Definition 2.2 (ps -ef, ps aux)
<span class="anker" id="satz-2-2"></span>

`ps -ef` zeigt jeden Prozess (`-e`, „every“) in der ausführlichen Form (`-f`, „full“) mit den Spalten `UID` (Besitzer), `PID`, `PPID`, `C` (Rechenanteil), `STIME` (Startzeit), `TTY`, `TIME` und `CMD` (Befehlszeile). `ps aux` zeigt ebenfalls alle Prozesse, aber mit den Spalten `USER`, `PID`, `%CPU`, `%MEM`, `VSZ`, `RSS`, `TTY`, `STAT`, `START`, `TIME` und `COMMAND`.
:::

Die Liste ist lang; `head` zeigt den Anfang:

```console
$ ps -ef | head -n 5
UID          PID    PPID  C STIME TTY          TIME CMD
root           1       0  5 15:24 ?        00:00:01 /sbin/init
root           2       1  0 15:24 ?        00:00:00 /init
root           6       2  0 15:24 ?        00:00:00 plan9 --control-socket 7 --log-level 4 --server-fd 8 --pipe-fd 10 --log-truncate
root          49       1  1 15:24 ?        00:00:00 /usr/lib/systemd/systemd-journald
```

Ein Fragezeichen in der Spalte `TTY` heißt: Der Prozess hat kein steuerndes Terminal. `plan9` ist ein Dateiserver von WSL; er macht die Linux-Dateien unter Windows sichtbar ([Kapitel 1, Abschnitt 4.6](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/wsl-2-linux-neben-windows.html#stufe-4-6)). Die Befehlszeile in der letzten Spalte ist vollständig, mit allen Argumenten.

::::beispiel Einen Prozess in der Liste suchen
Ein Prozess an einem anderen Terminal lässt sich mit `grep` aus der Liste heraussuchen ([Kapitel 6, Abschnitt 5.1](/wissen/informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke/suchen-mit-grep.html#stufe-5-1)):

```console
$ ps -ef | grep sleep
student      596     587  0 15:24 pts/3    00:00:00 sleep 600
student      602     535  0 15:24 pts/2    00:00:00 grep --color=auto sleep
```

Das wartende `sleep` hat die Nummer 596 und läuft am Terminal `pts/3`, dem zweiten Fenster; sein Elternprozess 587 ist die Shell dort. Die zweite Zeile ist eine Falle: `grep` findet sich selbst, denn seine eigene Befehlszeile enthält das Wort `sleep`. Es läuft gleichzeitig mit `ps`, weil beide Stufen einer Pipeline sind.
::::

Die zweite Form zeigt andere Spalten:

```console
$ ps aux | head -n 4
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  5.1  0.0  24332 14060 ?        Ss   15:24   0:01 /sbin/init
root           2  0.0  0.0   3120  2048 ?        Sl   15:24   0:00 /init
root           6  0.0  0.0   3120  1792 ?        Sl   15:24   0:00 plan9 --control-socket 7 --log-level 4 --server-fd 8 --pipe-fd 10 --log-truncate
```

Abbildung [5](#abb-5) erklärt die Spalten an der ersten Zeile. Zwei davon brauchen einen Satz mehr. `%CPU` ist die verbrauchte Rechenzeit geteilt durch die Zeit seit dem Start, ein Mittel über das ganze Leben des Prozesses, kein Augenblickswert. `RSS` ist der Arbeitsspeicher, den der Prozess gerade wirklich belegt, in KiB; `VSZ` ist der Speicher, den er insgesamt angefordert hat, auch wenn noch nicht alles davon belegt ist. Die Spalte `STAT` zeigt in Buchstaben, ob der Prozess gerade rechnet, wartet oder angehalten ist.

:::abbildung linux/k8psspalten 5
Die Zeile `root 1 5.1 0.0 24332 14060 ? Ss 15:24 0:01 /sbin/init` wird in ihre Spalten zerlegt; unter jeder erscheint nacheinander die Bedeutung: Besitzer, PID, Anteil der Rechenzeit seit dem Start, Anteil am Arbeitsspeicher, angeforderter Speicher (KiB), belegter Speicher (KiB), kein Terminal, Zustand, Startzeit, verbrauchte Rechenzeit, Befehlszeile. Zum Schluss zeigen Pfeile, welche Spalten `ps -ef` ebenfalls hat (Besitzer, PID, Startzeit, Terminal, Rechenzeit, Befehlszeile) und welche nur dort steht (PPID).
:::

⁠**Kurz gesagt:** `ps -ef` und `ps aux` zeigen alle Prozesse, die erste Form mit PPID, die zweite mit Rechen- und Speicheranteil und Zustand.

:::hintergrund Warum zwei Schreibweisen mit und ohne Strich?
Das Werkzeug `ps` entstand in zwei Unix-Familien getrennt: In der Familie von AT&T schrieb man Optionen mit Strich (`ps -ef`), in der Familie von Berkeley (BSD) ohne (`ps aux`). Das `ps` unter Linux versteht beide Schreibweisen und zeigt je nach Schreibweise andere Spalten. Mischen sollte man sie nicht: `ps -aux` ist etwas anderes als `ps aux` und erzeugt auf manchen Systemen eine Warnung.
:::

### Eigene Spalten und Auswahl: ps -o

<span class="anker" id="stufe-2-3"></span>

Oft interessieren nur wenige Spalten und wenige Prozesse. Beides lässt sich bei `ps` genau einstellen.

:::definition Definition 2.3 (ps -o und die Auswahl)
<span class="anker" id="satz-2-3"></span>

`ps -o spalte,spalte,…` zeigt genau die genannten Spalten, in dieser Reihenfolge. Häufige Namen sind `pid`, `ppid`, `user`, `tty`, `stat`, `ni`, `pcpu`, `comm` (Programmname) und `cmd` (ganze Befehlszeile). Die Auswahl der Prozesse treffen `-p liste` (nach PID), `-C liste` (nach Programmname), `--ppid liste` (nach Elternprozess) und `-u benutzer` (nach Besitzer).
:::

So findest du das wartende `sleep` ohne `grep`:

```console
$ ps -o pid,ppid,user,tty,cmd -C sleep
    PID    PPID USER     TT       CMD
    596     587 student  pts/3    sleep 600
```

Der Programmname ist für `-C` das, was `ps` in der Spalte `comm` zeigt, also höchstens 15 Zeichen (Unterabschnitt [1.7](prozesse-und-ihre-verwandtschaft.html#stufe-1-7)). Mehrere Namen oder Nummern trennt ein Komma ohne Leerzeichen, wie bei `-p 1,2` in Unterabschnitt [1.7](prozesse-und-ihre-verwandtschaft.html#stufe-1-7). Eine Liste aller Spaltennamen steht in `man ps` unter „STANDARD FORMAT SPECIFIERS“.

⁠**Kurz gesagt:** `ps -o` wählt die Spalten, `-p`, `-C`, `--ppid` und `-u` wählen die Prozesse.

### Prozesse nach Namen finden: pgrep

<span class="anker" id="stufe-2-4"></span>

Meist sucht man die PID eines Programms, dessen Namen man kennt. Mit `ps` und `grep` geht das, aber umständlich und mit der Falle aus Unterabschnitt [2.2](#stufe-2-2). Dafür gibt es ein eigenes Werkzeug.

:::definition Definition 2.4 (pgrep)
<span class="anker" id="satz-2-4"></span>

`pgrep muster` gibt die PIDs aller Prozesse aus, deren Programmname zum erweiterten regulären Ausdruck `muster` passt ([Kapitel 6, Abschnitt 7.2](/wissen/informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke/regulare-ausdrucke-wiederholungen-gruppen-und-alternativen.html#stufe-7-2)), eine je Zeile, und sich selbst nie. Mit `-a` zeigt es die ganze Befehlszeile dazu, mit `-x` muss der Name genau passen, mit `-f` durchsucht es die ganze Befehlszeile statt nur des Namens, und mit `-u benutzer` nur die Prozesse dieses Besitzers.
:::

```console
$ pgrep sleep
596
$ pgrep -a sleep
596 sleep 600
$ pgrep -a -u root cron
160 /usr/sbin/cron -f -P
```

Ohne `-x` passt `pgrep sl` auf jedes Programm, dessen Name `sl` enthält. Wie `grep` endet `pgrep` mit dem Exit-Status 1, wenn es nichts findet; so lässt sich mit `&&` und `||` prüfen, ob ein Programm läuft ([Kapitel 4, Abschnitt 6.2](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/befehle-verketten.html#stufe-6-2)).

⁠**Kurz gesagt:** `pgrep` findet die PIDs von Prozessen über ihren Namen oder ihre Befehlszeile.

### Der Zustand eines Prozesses

<span class="anker" id="stufe-2-5"></span>

Von den vielen Prozessen eines Systems rechnet in jedem Augenblick nur ein kleiner Teil; die übrigen warten. Worauf ein Prozess gerade wartet, verrät, warum er nicht vorankommt. Der Kernel führt dafür in jedem Eintrag einen Zustand.

:::definition Definition 2.5 (Zustand eines Prozesses)
<span class="anker" id="satz-2-5"></span>

Der __Zustand__ eines Prozesses sagt, ob er gerade rechnen kann. `ps` zeigt ihn in der Spalte `STAT` als Buchstaben:

<ul>

<li>

`R` (running): Der Prozess rechnet gerade oder wartet nur darauf, dass der Planer ihm einen Kern gibt.

</li>

<li>

`S` (sleeping): Der Prozess wartet auf ein Ereignis, etwa eine Taste, Daten aus einer Pipe oder das Ablaufen einer Zeit; er lässt sich dabei unterbrechen.

</li>

<li>

`D` (disk sleep): Der Prozess wartet auf ein Gerät, meist auf einen Datenträger, und lässt sich in dieser kurzen Zeit nicht unterbrechen.

</li>

<li>

`T` (stopped): Der Prozess ist angehalten; er rechnet nicht, bis ihn jemand weiterlaufen lässt.

</li>

<li>

`t` (tracing stop): Der Prozess ist angehalten, weil ein Werkzeug wie `strace` ihn verfolgt.

</li>

<li>

`Z` (zombie): Der Prozess ist beendet, aber sein Elternprozess hat seinen Exit-Status noch nicht abgeholt.

</li>

<li>

`I` (idle): ein untätiger Ausführungsstrang des Kernels selbst.

</li>

</ul>

Dahinter können Zusatzzeichen stehen, unter anderem `s` (der Prozess leitet seine Sitzung, wie eine Shell), `+` (er gehört zum Vordergrund seines Terminals) und `l` (er hat mehrere Threads).
:::

Abbildung [6](#abb-6) zeigt, wie ein Prozess zwischen den Zuständen wechselt.

:::abbildung linux/k8zustaende 6
Fünf Kreise: R (rechnet oder rechenbereit), S (wartet), D (wartet auf ein Gerät), T (angehalten), Z (beendet, Status nicht abgeholt). Ein Punkt „Prozess“ entsteht in R und wandert: R $\to$ S „wartet auf eine Taste“, S $\to$ R „Taste kommt“, R $\to$ D $\to$ R „liest vom Datenträger“, R $\to$ T „angehalten“, T $\to$ R „weiter“, zuletzt R $\to$ Z „Programm endet“ und von Z ins Leere „Elternprozess holt den Status ab“. Innerhalb von R pendelt der Punkt kurz zwischen „rechnet“ und „wartet auf einen Kern“; beides ist R.
:::

`ps -o pid,stat,comm` zeigt die Zustände am eigenen Terminal, `-C sleep` den im zweiten Fenster:

```console
$ ps -o pid,stat,comm
    PID STAT COMMAND
    535 Ss   bash
    612 R+   ps
$ ps -o pid,stat,cmd -C sleep
    PID STAT CMD
    596 S+   sleep 600
```

Die Shell wartet auf deine nächste Eingabe (`S`) und leitet die Sitzung ihres Terminals (`s`). `ps` rechnet in dem Augenblick, in dem es sich selbst ansieht (`R`). `sleep` wartet auf das Ablaufen seiner Zeit (`S`); beide gehören zum Vordergrund ihres Terminals (`+`).

::::beispiel Ein Prozess, der dauernd rechnet
Beende `sleep` im zweiten Terminal mit Strg+C und starte dort ein Programm, das ohne Pause rechnet. `yes` schreibt endlos Zeilen mit `y`; die Umleitung nach `/dev/null` wirft sie weg, und `timeout 15` beendet das Ganze nach 15 Sekunden. Im zweiten Terminal:

```console
$ timeout 15 yes > /dev/null
```

Im ersten Terminal, innerhalb der 15 Sekunden:

```console
$ ps -o pid,stat,pcpu,cmd -C yes
    PID STAT %CPU CMD
    619 R+   98.9 yes
```

`yes` ist im Zustand `R` und hat seit seinem Start fast die ganze Zeit eines Kerns verbraucht.
::::

⁠**Kurz gesagt:** Der Zustand zeigt, ob ein Prozess rechnet (R), wartet (S, D), angehalten ist (T) oder schon beendet ist, aber noch nicht abgeholt (Z).

### Der Zombie

<span class="anker" id="stufe-2-6"></span>

Der Zustand Z wirkt merkwürdig: Ein Prozess, der beendet ist und trotzdem in der Liste steht. Wozu bleibt von einem beendeten Prozess etwas übrig?

:::definition Definition 2.6 (Zombie)
<span class="anker" id="satz-2-6"></span>

Ein __Zombie__ ist ein Prozess, der beendet ist, auf den sein Elternprozess aber noch nicht mit wait gewartet hat. Vom Prozess bleibt nur ein kleiner Eintrag beim Kernel mit seiner PID, seinem Exit-Status und seinem Verbrauch an Rechenzeit. Ruft der Elternprozess wait auf, bekommt er den Status, und der Eintrag verschwindet.
:::

Normalerweise ist ein Prozess nur einen Augenblick lang Zombie, denn die Shell und die meisten Programme warten auf ihre Kinder. Einen Zombie, der länger bleibt, erzeugt ein Elternprozess, der nie wait aufruft. Dafür reicht ein Trick mit exec: Das Zeichen `&` am Ende eines Befehls bedeutet, dass die bash den Befehl startet, aber nicht auf ihn wartet; Unterabschnitt [3.2](vordergrund-hintergrund-und-jobs.html#stufe-3-2) erklärt es ausführlich. Im zweiten Terminal:

```console
$ bash -c 'sleep 1 & exec sleep 30'
```

Die neue bash startet `sleep 1` als Kind, ohne zu warten, und ersetzt sich dann mit exec durch `sleep 30`. Das Kind hat damit einen Elternprozess, der das Programm `sleep` ausführt, und `sleep` ruft nie wait auf. Nach einer Sekunde ist das Kind fertig. Im ersten Terminal:

```console
$ ps -o pid,ppid,stat,cmd -C sleep
    PID    PPID STAT CMD
    628     587 S+   sleep 30
    629     628 Z+   [sleep] <defunct>
```

Der Prozess 629 ist ein Zombie: Zustand `Z`, und statt einer Befehlszeile steht `<defunct>` („erloschen“), denn sein Programm ist schon fort. Sein Elternprozess ist 628, das `sleep 30`. Nach 30 Sekunden endet auch dieser, und der Zombie ist verschwunden:

```console
$ ps -o pid,ppid,stat,cmd -C sleep
    PID    PPID STAT CMD
```

Abbildung [7](#abb-7) zeigt, wann ein Zombie entsteht und wer ihn beseitigt.

:::abbildung linux/k8zombie 7
Zwei Zeitleisten. Oben der gewöhnliche Fall: Kind endet, wird kurz zum Zombie (ein Grabstein mit PID 629 und Status 0), der Elternprozess ruft wait auf, nimmt den Status an sich, der Grabstein verschwindet. Unten der Fall aus dem Versuch: Der Elternprozess 628 ruft nie wait auf, der Grabstein bleibt stehen. Dann endet auch 628; der Grabstein wandert zu einem neuen Elternprozess „Prozess 1 oder ein Aufräumer“, der sofort wait aufruft, und der Grabstein verschwindet.
:::

⁠**Kurz gesagt:** Ein Zombie ist ein beendeter Prozess, dessen Exit-Status sein Elternprozess noch nicht mit wait abgeholt hat; er verschwindet mit dem wait.

:::hintergrund Warum es Zombies überhaupt gibt
Der Elternprozess will wissen, wie sein Kind geendet hat, die Shell zum Beispiel für `$?`. Endet das Kind, bevor der Elternprozess wait aufruft, muss der Kernel den Status irgendwo aufheben. Er gibt deshalb Speicher, Programm und Dateien des Kindes sofort frei, behält aber einen kleinen Rest des Eintrags mit PID und Exit-Status. Dieser Rest ist der Zombie. Er belegt kaum Arbeitsspeicher, aber einen Platz in der Tabelle der Prozesse und eine PID. Ein Programm, das massenhaft Kinder startet und nie wartet, kann die Tabelle füllen; dann lassen sich keine neuen Prozesse mehr starten.
:::

:::hintergrund Was mit Kindern geschieht, deren Elternprozess endet
Endet ein Elternprozess vor seinen Kindern, werden die Kinder zu Waisen. Der Kernel gibt jeder Waise einen neuen Elternprozess: den nächsten Vorfahren, der sich beim Kernel als „Aufräumer“ für seine Nachkommen angemeldet hat (englisch „subreaper“), sonst den Prozess 1. Der neue Elternprozess ruft für die übernommenen Kinder wait auf, sobald sie enden; so bleibt kein Zombie dauerhaft übrig. Auf einem gewöhnlichen Ubuntu übernimmt das meist `systemd`, entweder der Prozess 1 oder die `systemd`-Instanz des angemeldeten Benutzers. Unter WSL ist es auf dem Testsystem ein Prozess `/init` von WSL, der zur Sitzung des Terminals gehört. Ein Zombie, dessen Elternprozess noch lebt, lässt sich übrigens nicht beseitigen, indem man ihn beendet: Er ist ja schon beendet. Man muss den Elternprozess dazu bringen, wait aufzurufen, oder ihn beenden.
:::

### Laufend beobachten: top

<span class="anker" id="stufe-2-7"></span>

`ps` zeigt eine Momentaufnahme. Wer wissen will, welches Programm den Rechner gerade beschäftigt, braucht eine Anzeige, die sich laufend erneuert.

:::definition Definition 2.7 (top)
<span class="anker" id="satz-2-7"></span>

`top` zeigt oben eine Übersicht über das System und darunter eine Tabelle der Prozesse, sortiert nach dem augenblicklichen Rechenanteil, und erneuert beides alle drei Sekunden. Es läuft, bis man `q` drückt.
:::

Im Terminal füllt `top` das ganze Fenster. Mit `-b` schreibt es seine Anzeige stattdessen als gewöhnliche Ausgabe, mit `-n 1` nur einmal, und `-o -PID` sortiert die Tabelle hier nach aufsteigender PID statt nach Rechenanteil; so passt eine ruhige Momentaufnahme hierher:

```console
$ top -b -n 1 -o -PID | head -n 12
top - 15:25:53 up 1 min,  1 user,  load average: 0.20, 0.08, 0.03
Tasks:  29 total,   1 running,  28 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.0 us,  0.7 sy,  0.0 ni, 98.7 id,  0.7 wa,  0.0 hi,  0.0 si,  0.0 st
MiB Mem :  31846.7 total,  30985.9 free,    736.2 used,    433.1 buff/cache
MiB Swap:   8192.0 total,   8192.0 free,      0.0 used.  31110.5 avail Mem

    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
      1 root      20   0   24332  14060  10860 S   0.0   0.0   0:01.06 systemd
      2 root      20   0    3120   2048   1920 S   0.0   0.0   0:00.02 init-sy+
      6 root      20   0    3120   1792   1792 S   0.0   0.0   0:00.00 init
     49 root      19  -1   42192  15744  14720 S   0.0   0.0   0:00.24 systemd+
     83 systemd+  20   0   22412  14080  11648 S   0.0   0.0   0:00.11 systemd+
```

Die erste Zeile entspricht `uptime` ([Kapitel 2, Abschnitt 6.3](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/das-system-erkunden.html#stufe-6-3)). Die zweite zählt die Prozesse nach Zuständen. Die dritte teilt die Rechenzeit seit der letzten Erneuerung auf: `us` für Programme, `sy` für den Kernel, `ni` für Programme mit herabgesetzter Priorität, `id` für Leerlauf, `wa` für Warten auf Datenträger. Die beiden Zeilen zum Speicher entsprechen `free` ([Kapitel 2, Abschnitt 6.4](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/das-system-erkunden.html#stufe-6-4)). In der Tabelle ist `RES` dasselbe wie `RSS` bei `ps`, `S` der Zustand und `%CPU` der Anteil an der Zeit eines Kerns seit der letzten Erneuerung; ein Prozess mit mehreren Threads, die auf mehreren Kernen zugleich rechnen, kommt deshalb über 100. Zu lange Namen kürzt `top` mit einem `+`. Im laufenden `top` helfen einige Tasten:

<ul>

<li>

`q` beendet `top`, `h` zeigt die Hilfe;

</li>

<li>

`P` sortiert nach Rechenanteil, `M` nach Speicher;

</li>

<li>

`1` zeigt jeden Kern in einer eigenen Zeile;

</li>

<li>

`u` fragt nach einem Benutzer und zeigt nur seine Prozesse.

</li>

</ul>

Abbildung [8](#abb-8) zeigt die Momentaufnahme aus dem Block so, wie `top` sie im Terminal darstellt, und geht ihre Teile der Reihe nach durch.

:::abbildung linux/k8topbild 8
Die Momentaufnahme aus dem Block oben als Bildschirm von `top`. Nacheinander werden hervorgehoben und links nummeriert: die erste Kopfzeile mit Uhrzeit, Laufzeit, Zahl der Benutzer und Last wie bei `uptime` (1), die Prozesse nach Zuständen (2), die Aufteilung der Rechenzeit (3) und die beiden Zeilen zum Speicher wie bei `free` (4); dann die inverse Spaltenzeile (5) und zuletzt die oberste Prozesszeile (6). Dort steht wegen `-o -PID` der Prozess mit der kleinsten PID; ohne diese Option stünde dort der Prozess mit dem größten Rechenanteil.
:::

⁠**Kurz gesagt:** `top` zeigt laufend, welche Prozesse gerade rechnen und wie ausgelastet das System ist; `q` beendet es.

### Ein Blick in den Eintrag: /proc/<PID>

<span class="anker" id="stufe-2-8"></span>

`ps` und `top` erfinden ihre Angaben nicht; sie lesen sie aus `/proc`, wo der Kernel die Einträge seiner Prozesse als Dateien zeigt ([Kapitel 3, Abschnitt 7.8](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/die-verzeichnisstruktur-von-linux.html#stufe-7-8)). Wer genau wissen will, was der Kernel über einen Prozess weiß, kann selbst nachsehen.

:::definition Definition 2.8 (/proc/<PID>)
<span class="anker" id="satz-2-8"></span>

Für jeden Prozess gibt es ein Verzeichnis `/proc/<PID>`. Darin stehen unter anderem

<ul>

<li>

`status`: Name, Zustand, PID, PPID, Benutzer- und Gruppennummern und Speicherangaben, eine je Zeile;

</li>

<li>

`cmdline`: die Befehlszeile, die Argumente durch Nullbytes getrennt;

</li>

<li>

`environ`: die Umgebung beim Programmstart, ebenfalls durch Nullbytes getrennt; nur für den Besitzer und root lesbar;

</li>

<li>

`cwd` und `exe`: symbolische Links auf das Arbeitsverzeichnis und die Programmdatei;

</li>

<li>

`fd`: die geöffneten Deskriptoren ([Kapitel 4, Abschnitt 1.7](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/prozesse-und-ihre-drei-strome.html#stufe-1-7)).

</li>

</ul>
:::

Im zweiten Terminal startest du für den Versuch ein Programm als root:

```console
$ sudo sleep 700
```

Im ersten Terminal liest du dann den Eintrag der eigenen Shell und den des `sudo`-Prozesses. Dessen Nummer liefert `pgrep -n sudo`; `-n` wählt unter mehreren Treffern den jüngsten:

```console
$ grep -E '^(Name|State|PPid|Uid|Gid)' /proc/$$/status
Name:   bash
State:  S (sleeping)
PPid:   316
Uid:    1000    1000    1000    1000
Gid:    1000    1000    1000    1000
$ pgrep -n sudo
641
$ grep -E '^(Name|Uid)' /proc/641/status
Name:   sudo
Uid:    1000    0       0       0
```

Die Zeile `Uid` enthält vier Benutzernummern. Die erste ist die reale, die zweite die effektive Benutzernummer ([Kapitel 7, Abschnitt 9.2](/wissen/informatik/linux-und-kommandozeile/benutzer-gruppen-und-rechte/programme-ausfuhren-und-besondere-rechte.html#stufe-9-2)). Die dritte, die gespeicherte Benutzernummer, ist eine Kopie der effektiven Nummer vom Programmstart; mit ihr kann ein SUID-Programm vorübergehend zu seiner realen Nummer wechseln und danach zurück. Die vierte ist die Dateisystem-Benutzernummer, mit der Linux Zugriffe auf Dateien prüft; sie folgt immer der effektiven, solange ein Programm sie nicht eigens ändert. Bei der Shell sind alle vier 1000. Bei `sudo` ist nur die reale 1000, die übrigen sind 0: `sudo` ist ein SUID-Programm von root und weiß über die reale Nummer, wer es gestartet hat. Die Zeile `Gid` enthält dieselben vier Nummern für die Gruppe. Die Zeile `PPid` nennt den Elternprozess der Shell; bei dir ist das das Terminalprogramm, unter WSL der Prozess `Relay` aus Unterabschnitt [1.7](prozesse-und-ihre-verwandtschaft.html#stufe-1-7). Die Nummer 316 im Kapitel stammt vom Testaufbau, in dem ein Hilfsprogramm die beiden Terminals öffnet. Abbildung [9](#abb-9) ordnet die vier Spalten der Zeile `Uid` zu.

:::abbildung linux/k8procstatus 9
Zwei Zeilen `Uid:` übereinander, oben die der Shell (1000 1000 1000 1000), unten die von sudo (1000 0 0 0). Über den vier Spalten erscheinen nacheinander die Namen „real“, „effektiv“, „gespeichert“, „Dateisystem“; die ersten beiden sind aus [Kapitel 7](/wissen/informatik/linux-und-kommandozeile/benutzer-gruppen-und-rechte/benutzer-gruppen-und-rechte.html) bekannt und bleiben grau. Hervorgehoben werden die beiden neuen Spalten: Von der effektiven 0 wandert beim Programmstart eine Kopie in die Spalte „gespeichert“ („Kopie vom Start, für den Rückweg“), und die Spalte „Dateisystem“ folgt der effektiven Nummer („mit dieser Nummer prüft der Kernel Dateizugriffe“).
:::

Die Befehlszeile und die Umgebung enthalten Nullbytes; `tr` macht daraus Leerzeichen bzw. Zeilenenden ([Kapitel 6, Abschnitt 2.2](/wissen/informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke/spalten-ausschneiden-und-zeichen-ersetzen-cut-tr-und-paste.html#stufe-2-2)). Die Nummer von `sleep 700` nennt `pgrep -a -x sleep`:

```console
$ pgrep -a -x sleep
642 sleep 700
$ tr '\0' ' ' < /proc/642/cmdline; echo
sleep 700
$ tr '\0' '\n' < /proc/$$/environ | grep -E '^(HOME|USER|LANG)='
HOME=/home/student
LANG=C.UTF-8
USER=student
$ cat /proc/1/environ
cat: /proc/1/environ: Permission denied
$ ls -l /proc/$$/cwd /proc/$$/exe
lrwxrwxrwx 1 student student 0 Nov 10 15:25 /proc/535/cwd -> /home/student/linuxk8
lrwxrwxrwx 1 student student 0 Nov 10 15:25 /proc/535/exe -> /usr/bin/bash
```

Die Befehlszeile des Prozesses 642, des `sleep 700`, darf jeder lesen, obwohl er root gehört; die Umgebung des Prozesses 1 dagegen nicht. Daraus folgt eine wichtige Regel: Ein Passwort gehört nie als Argument in eine Befehlszeile, denn jeder Benutzer kann es mit `ps` lesen; was das für Angriffe bedeutet, ist Stoff der Reihe Cybersecurity. Beende `sudo sleep 700` im zweiten Terminal mit Strg+C.

⁠**Kurz gesagt:** `/proc/<PID>` zeigt den Eintrag des Kernels zu einem Prozess; `status` nennt unter anderem die vier Benutzernummern real, effektiv, gespeichert und Dateisystem.

### Aufgaben zu Abschnitt [2](#stufe-2)

<span class="anker" id="stufe-2-9"></span>

:::aufgabe Aufgabe 4 ★ Eine Zeile von ps aux deuten
<span class="anker" id="aufg-4"></span>

So oder ähnlich könnte `ps aux` den Dienst `cron` zeigen. Deute jede Spalte der Zeile `root 160 0.0 0.0 6084 2560 ? Ss 15:24 0:00 /usr/sbin/cron -f -P`. Hat der Prozess ein Terminal? Wie viel Arbeitsspeicher belegt er wirklich?

:::loesung
`root`: Besitzer ist root. `160`: die PID. `0.0` und `0.0`: Der Prozess hat seit seinem Start fast keine Rechenzeit verbraucht und belegt einen verschwindenden Teil des Arbeitsspeichers. `6084`: Er hat 6084 KiB Speicher angefordert (`VSZ`). `2560`: Davon belegt er wirklich 2560 KiB, also 2,5 MiB (`RSS`). `?`: Er hat kein steuerndes Terminal. `Ss`: Er wartet (`S`) und leitet eine eigene Sitzung (`s`). `15:24`: Startzeit. `0:00`: bisher verbrauchte Rechenzeit, weniger als eine Sekunde. `/usr/sbin/cron -f -P`: die Befehlszeile. Ein Terminal hat der Prozess also nicht; wirklich belegt er 2,5 MiB.
:::
:::

:::aufgabe Aufgabe 5 ★★ Zustände vorhersagen
<span class="anker" id="aufg-5"></span>

Welchen Buchstaben zeigt `ps` in der Spalte `STAT` jeweils, und warum? (a) eine Shell, die auf deine Eingabe wartet; (b) `yes > /dev/null`; (c) ein Programm, das gerade eine sehr große Datei vom Datenträger liest; (d) ein Kindprozess, der fertig ist, dessen Elternprozess aber noch nicht wait aufgerufen hat.

:::loesung
(a) `S`, meist als `Ss`: Die Shell wartet auf eine Taste und lässt sich dabei unterbrechen; das `s` sagt, dass sie die Sitzung ihres Terminals leitet. (b) `R`: `yes` rechnet ohne Pause; das Schreiben nach `/dev/null` muss auf nichts warten. (c) Abwechselnd `D` und `R`: Während das Programm auf den Datenträger wartet, ist es in `D`, dazwischen verarbeitet es die Daten in `R`. Bei einem schnellen Datenträger sieht man `D` nur selten. (d) `Z`: Das Kind ist ein Zombie, bis der Elternprozess wait aufruft.
:::
:::

:::aufgabe Aufgabe 6 ★★ Der Eintrag deiner Shell
<span class="anker" id="aufg-6"></span>

Lies mit `grep -E '^(Name|State|PPid|Uid|Gid)' /proc/$$/status` den Eintrag deiner Shell. (a) Woran erkennst du, dass die Shell gerade wartet? (b) Was bedeuten die vier Zahlen der Zeile `Uid`? (c) Wie müsste die Zeile `Uid` eines Programms aussehen, das du startest und das ein SUID-Bit von root hat?

:::loesung
```console
$ grep -E '^(Name|State|PPid|Uid|Gid)' /proc/$$/status
Name:   bash
State:  S (sleeping)
PPid:   316
Uid:    1000    1000    1000    1000
Gid:    1000    1000    1000    1000
```

Die Zeile `PPid` zeigt bei dir die Nummer deines Terminalprogramms bzw. unter WSL die des Prozesses `Relay`; die 316 stammt vom Testaufbau des Kapitels. (a) Die Zeile `State` zeigt `S (sleeping)`: Die Shell wartet. Sie rechnet nur kurz, während sie einen Befehl liest und startet. (b) Die vier Zahlen sind die reale, die effektive, die gespeicherte und die Dateisystem-Benutzernummer. Bei einer gewöhnlichen Shell sind alle vier deine Nummer. (c) Bei einem SUID-Programm von root bleibt die reale Nummer deine, die übrigen drei werden 0, also `Uid: 1000 0 0 0`, wie bei `sudo` in Unterabschnitt [2.8](#stufe-2-8).
:::
:::

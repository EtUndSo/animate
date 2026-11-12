---
title: Mit Signalen arbeiten
pfad: Informatik / Linux und Kommandozeile / Prozesse, Signale und Dienste
adresse: informatik/linux-und-kommandozeile/prozesse-signale-und-dienste
knoten: Kapitel 8: Prozesse, Signale und Dienste
order: 6130600
summary: Mit kill und einer PID lässt sich jedes eigene Programm erreichen.
tags: fängt, ab, SIGHUP
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Mit `kill` und einer PID lässt sich jedes eigene Programm erreichen. Dieser Abschnitt zeigt die Werkzeuge für die tägliche Arbeit: Signale an Programme nach ihrem Namen schicken, ein Signal abfangen, um aufzuräumen, einem Programm eine Zeitgrenze setzen und ein Programm so starten, dass es das Schließen des Terminals übersteht.
:::

### Signale nach Namen: pkill

<span class="anker" id="stufe-5-1"></span>

Erst mit `pgrep` die PID suchen und dann `kill` mit dieser PID aufrufen, ist umständlich. Es geht in einem Schritt, mit denselben Regeln für die Auswahl.

:::definition Definition 5.1 (pkill)
<span class="anker" id="satz-5-1"></span>

`pkill -signal muster` schickt allen Prozessen, die `pgrep muster` finden würde, ein Signal, ohne Angabe SIGTERM. Es versteht dieselben Optionen wie `pgrep`, etwa `-x`, `-f` und `-u`, und darf wie `kill` nur Prozesse erreichen, denen der Aufrufer Signale schicken darf.
:::

```console
$ sleep 500 &
[1] 700
$ sleep 501 &
[2] 703
$ pgrep -a -x sleep
700 sleep 500
703 sleep 501
$ pkill -x -f 'sleep 500'
[1]-  Terminated                 sleep 500
$ pgrep -a -x sleep
703 sleep 501
$ pkill -x -f 'sleep 501'
$ jobs
[2]+  Terminated                 sleep 501
```

Mit `-f` vergleicht `pkill` die ganze Befehlszeile, mit `-x` muss sie genau `sleep 500` lauten; so trifft das Signal nur diesen einen Prozess. Ähnlich arbeitet `killall name`, das allen Prozessen mit genau diesem Programmnamen ein Signal schickt.

:::warnung pkill und killall nur mit genauem Muster
`pkill sleep` würde jedem deiner Prozesse, in dessen Namen `sleep` vorkommt, SIGTERM schicken, auch solchen, die du vergessen hast oder die ein anderes Programm gestartet hat. Prüfe ein Muster deshalb immer zuerst mit `pgrep -a` und denselben Optionen, und schicke das Signal erst, wenn die Liste genau die gewünschten Prozesse enthält. Mit `sudo` erreichen `pkill` und `killall` auch die Prozesse des Systems; ein zu allgemeines Muster kann dann den Rechner lahmlegen. Ebenso gefährlich ist eine falsche Zahl bei `kill`: Die Angabe $-1$ als Ziel, etwa in `kill -9 -1`, steht für alle Prozesse, denen du Signale schicken darfst, auch deine Shell und deine Anmeldung.
:::

⁠**Kurz gesagt:** `pkill` schickt allen Prozessen, die zu einem Muster passen, ein Signal; prüfe das Muster vorher mit `pgrep -a`.

### Ein Signal abfangen: trap

<span class="anker" id="stufe-5-2"></span>

Unterabschnitt [4.5](signale.html#stufe-4-5) hat gezeigt, warum man zuerst SIGTERM schickt: damit ein Programm aufräumen kann. Dafür muss das Programm aber eine eigene Reaktion auf das Signal festlegen. Wie das geht, lässt sich mit der bash selbst ausprobieren.

:::definition Definition 5.2 (Signal abfangen, trap)
<span class="anker" id="satz-5-2"></span>

Ein Programm __fängt__ ein Signal __ab__, wenn es für dieses Signal eine eigene Reaktion festlegt; trifft das Signal ein, führt der Prozess dann diese Reaktion aus statt der Standardreaktion. In der bash legt der eingebaute Befehl `trap 'befehle' SIGNAL` eine solche Reaktion fest. `trap '' SIGNAL` lässt die bash das Signal ignorieren, `trap - SIGNAL` stellt die Standardreaktion wieder her. SIGKILL und SIGSTOP lassen sich nicht abfangen.
:::

Der folgende Versuch startet eine bash, die bei SIGTERM eine vorübergehende Datei löscht. Sie legt die Datei `entwurf.tmp` an und wartet dann mit `read -t 600` bis zu zehn Minuten auf eine Eingabezeile. Während sie wartet, siehst du im zweiten Terminal nach, ob die Datei da ist, und schickst der bash SIGTERM. Im ersten Terminal:

```console
$ bash -c 'trap "echo Aufräumen; rm -f entwurf.tmp; exit 1" TERM; touch entwurf.tmp; echo "Ich bin $$ und warte"; read -t 600'
Ich bin 708 und warte
Aufräumen
$ echo $?
1
$ ls entwurf.tmp
ls: cannot access 'entwurf.tmp': No such file or directory
```

Im zweiten Terminal:

```console
$ ls entwurf.tmp
entwurf.tmp
$ kill 708
```

Statt sofort zu enden, hat die bash ihre Reaktion ausgeführt: Sie schrieb `Aufräumen`, löschte `entwurf.tmp` und endete mit dem Exit-Status 1, den die Reaktion mit `exit 1` festlegt. Ein zweiter Versuch ignoriert SIGTERM; aus dem zweiten Terminal schickst du ihm zuerst SIGTERM und dann SIGKILL:

```console
$ bash -c 'trap "" TERM; echo "Ich bin $$ und warte"; read -t 600'
Ich bin 717 und warte
Killed                     bash -c 'trap "" TERM; echo "Ich bin $$ und warte"; read -t 600'
$ echo $?
137
```

Im zweiten Terminal:

```console
$ kill 717
$ kill -9 717
```

Das erste `kill` bleibt ohne Wirkung, die bash wartet weiter. Erst SIGKILL beendet sie, denn dafür kann kein Programm eine Reaktion festlegen. Abbildung [18](#abb-18) zeigt die Tabelle der Reaktionen, die der Kernel für jeden Prozess führt.

:::abbildung linux/k8trap 18
Die Reaktionstabelle eines Prozesses als Liste: SIGINT „Standard: beenden“, SIGTERM „Standard: beenden“, SIGKILL „beenden“ mit Schloss, SIGSTOP „anhalten“ mit Schloss. Ein Kärtchen `trap "…" TERM` legt sich auf die Zeile SIGTERM, die nun „eigene Reaktion: Aufräumen“ zeigt. Ein zweites Kärtchen `trap "" TERM` ersetzt das durch „ignorieren“. Ein drittes Kärtchen versucht sich auf SIGKILL zu legen und prallt am Schloss ab. Zuletzt trifft ein Signal SIGKILL ein und beendet den Prozess.
:::

Was erbt ein neuer Prozess von diesen Festlegungen? Beim fork bekommt das Kind eine Kopie der ganzen Tabelle. Beim exec setzt der Kernel eigene Reaktionen auf die Standardreaktion zurück, denn ihr Code gehörte zum alten Programm und ist danach fort. Ignorierte Signale bleiben dagegen ignoriert, auch über exec hinweg.

⁠**Kurz gesagt:** Ein Programm kann für die meisten Signale eine eigene Reaktion festlegen, in der bash mit `trap`; SIGKILL und SIGSTOP nie. Ignorierte Signale bleiben über exec ignoriert, eigene Reaktionen nicht.

:::hintergrund Warum read statt sleep?
Mit `sleep 600` statt `read -t 600` hätte der Versuch nicht funktioniert wie erwartet. Läuft in der bash ein Programm im Vordergrund und trifft ein Signal ein, für das sie eine Reaktion festgelegt hat, führt die bash die Reaktion erst aus, wenn das Programm geendet hat. `sleep` wartet aber zehn Minuten. `read` dagegen ist ein eingebauter Befehl; die bash wartet dabei selbst und kann sofort reagieren. Dasselbe gilt für den eingebauten Befehl `wait`. Außerdem kennt `trap` neben den Signalen das Ereignis `EXIT`: `trap 'befehle' EXIT` führt die Befehle aus, wann immer die bash endet, gleich aus welchem Grund außer SIGKILL. So muss man das Aufräumen nur an einer Stelle festlegen.
:::

### Eine Zeitgrenze: timeout

<span class="anker" id="stufe-5-3"></span>

Manche Programme hängen gelegentlich, etwa beim Warten auf eine Netzverbindung. Will man ihnen höchstens eine bestimmte Zeit geben, wäre ein zweites Terminal mit `kill` unpraktisch. Dafür gibt es ein Werkzeug, das in Unterabschnitt [2.5](prozesse-beobachten.html#stufe-2-5) schon einmal vorkam.

:::definition Definition 5.3 (timeout)
<span class="anker" id="satz-5-3"></span>

`timeout dauer befehl` startet den Befehl und schickt ihm SIGTERM, wenn er nach der Dauer noch läuft; die Dauer ist in Sekunden, mit `m` in Minuten. Endet der Befehl so, endet `timeout` mit dem Exit-Status 124, sonst mit dem Status des Befehls. `-s signal` wählt ein anderes Signal, `-k dauer` schickt zusätzlich SIGKILL, wenn der Befehl nach dem ersten Signal so lange weiterläuft.
:::

```console
$ timeout 2 sleep 20
$ echo $?
124
$ timeout -k 1 2 bash -c 'trap "" TERM; sleep 20'
$ echo $?
137
$ pgrep -a -x sleep
```

Nach zwei Sekunden beendet SIGTERM das `sleep 20`, und der Status 124 sagt: Die Zeit war um. Im zweiten Befehl ignoriert die bash SIGTERM, ebenso ihr Kind `sleep`, das die Ignorierung erbt. Eine Sekunde später schickt `timeout` SIGKILL, und der Status ist $137 = 128 + 9$. `pgrep` zeigt danach kein `sleep` mehr. Abbildung [19](#abb-19) zeigt den zeitlichen Ablauf.

:::abbildung linux/k8timeout 19
Eine Uhr läuft von 0 bis 3 Sekunden, darunter eine Zeitleiste für den Prozess `bash -c 'trap "" TERM; sleep 20'`. Bei 2 Sekunden schickt `timeout` SIGTERM; das Kärtchen trifft den Prozess, wird abgewiesen („ignoriert“), die Leiste läuft weiter. Bei 3 Sekunden (`-k 1`) schickt `timeout` SIGKILL; die Leiste endet sofort. Rechts erscheint der Exit-Status 137 = 128 + 9. Darüber zum Vergleich in grau: `timeout 2 sleep 20` endet schon bei 2 Sekunden mit 124.
:::

⁠**Kurz gesagt:** `timeout` beendet einen Befehl nach einer Zeitgrenze mit SIGTERM (Status 124), mit `-k` notfalls mit SIGKILL.

::::beispiel Stand der uutils-Fassung in Ubuntu 26.04
`timeout` gehört zu den Grundbefehlen, die Ubuntu 26.04 in der Fassung von uutils mitbringt ([Kapitel 2, Abschnitt 7.2](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/zwei-fassungen-der-grundbefehle-gnu-und-uutils.html#stufe-7-2)). Bei `-s KILL` unterscheiden sich die beiden Fassungen:

```console
$ timeout -s KILL 2 sleep 20
$ echo $?
124
$ gnutimeout -s KILL 2 sleep 20
Killed                     gnutimeout -s KILL 2 sleep 20
$ echo $?
137
```

Die uutils-Fassung meldet auch hier 124. Die GNU-Fassung schickt SIGKILL an ihre ganze Prozessgruppe und damit auch an sich selbst; die Shell meldet deshalb `Killed` und den Status 137. Auf einem System mit GNU-Werkzeugen, etwa Debian, steht nach `timeout -s KILL` also 137.
::::

### Das Signal beim Schließen: SIGHUP

<span class="anker" id="stufe-5-4"></span>

Was geschieht mit einem Programm im Hintergrund, wenn du das Terminalfenster schließt? Der Job gehört zur Shell dieses Fensters, und die gibt es danach nicht mehr. Auch hier entscheidet ein Signal.

:::definition Definition 5.4 (SIGHUP)
<span class="anker" id="satz-5-4"></span>

__SIGHUP__ (Nummer 1, „hang up“, auflegen) schickt der Kernel dem Prozess, der ein Terminal steuert, meist der Shell, wenn das Terminal verschwindet, etwa weil das Fenster geschlossen wird. Eine interaktive bash schickt SIGHUP vor ihrem Ende an alle ihre Jobs, laufende und angehaltene; angehaltene bekommen vorher SIGCONT, damit sie das Signal überhaupt bearbeiten. Die Standardreaktion auf SIGHUP ist beenden.
:::

Im zweiten Terminal startest du einen Job im Hintergrund:

```console
$ sleep 901 &
[1] 732
$ jobs
[1]+  Running                    sleep 901 &
```

Dann schließt du das zweite Terminalfenster und siehst im ersten nach:

```console
$ pgrep -a -x sleep
```

`sleep 901` ist fort, obwohl es im Hintergrund lief: Die Shell des geschlossenen Fensters hat ihm SIGHUP geschickt. Abbildung [20](#abb-20) zeigt die Kette. Anders ist es, wenn du die Shell mit `exit` beendest: Dann bekommt sie selbst kein SIGHUP und schickt auch ihren laufenden Jobs keines. Das täte sie nur als Anmelde-Shell ([Kapitel 5, Abschnitt 6.3](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/startdateien-und-aliase.html#stufe-6-3)) mit der Einstellung `huponexit`, die `shopt -s huponexit` einschaltet; voreingestellt ist sie aus.

:::abbildung linux/k8sighup 20
Ein Terminalfenster mit einer Shell und zwei Jobs (`sleep 901` läuft, ein angehaltener Job). Das Fenster wird geschlossen (ein Kreuz). Der Kernel schickt der Shell SIGHUP; die Shell schickt dem angehaltenen Job zuerst SIGCONT, dann beiden Jobs SIGHUP, und endet. Beide Jobs verschwinden. Eine Beschriftung oben: „Auflegen“ mit einem kleinen Telefonhörer.
:::

⁠**Kurz gesagt:** Wird ein Terminal geschlossen, bekommt seine Shell SIGHUP und schickt es an alle ihre Jobs, die daraufhin enden.

:::hintergrund Woher der Name „auflegen“ kommt
Früher saßen Benutzer an einem Terminal, das über eine Telefonleitung mit dem Rechner verbunden war. Legte die Gegenstelle auf, sollte der Rechner die Programme dieser Sitzung beenden, denn niemand war mehr da, der ihre Ausgabe lesen oder ihnen antworten konnte. Daher der Name des Signals. Heute erfüllt das Schließen des Fensters dieselbe Rolle. Viele Dienste, die gar kein Terminal haben, benutzen SIGHUP inzwischen für etwas anderes: als Aufforderung, ihre Einstellungen neu einzulesen, ohne neu zu starten.
:::

### Weiterlaufen nach dem Schließen: nohup und disown

<span class="anker" id="stufe-5-5"></span>

Manche Programme sollen das Schließen des Terminals überleben, etwa eine lange Rechnung, die man abends startet. Es gibt zwei Wege, die an verschiedenen Stellen der Kette aus Unterabschnitt [5.4](#stufe-5-4) ansetzen.

:::definition Definition 5.5 (nohup, disown)
<span class="anker" id="satz-5-5"></span>

`nohup befehl` startet einen Befehl, für den SIGHUP ignoriert wird. Ist die Ausgabe ein Terminal, leitet `nohup` sie in die Datei `nohup.out` um, und eine Eingabe vom Terminal ersetzt es durch `/dev/null`. Der eingebaute Befehl `disown jobangabe` streicht einen schon laufenden Job aus der Liste der Shell; ohne Angabe den aktuellen Job. Die Shell schickt ihm dann beim Ende kein SIGHUP mehr.
:::

`nohup` nutzt die Regel aus Unterabschnitt [5.2](#stufe-5-2): Es lässt SIGHUP ignorieren und ersetzt sich dann mit exec durch den Befehl; ignorierte Signale bleiben über exec ignoriert. Öffne ein neues zweites Terminal und wechsle dort mit `cd ~/linuxk8` ins Übungsverzeichnis; dann:

```console
$ sleep 903 &
[1] 741
$ disown
$ jobs
$ nohup sleep 902
nohup: ignoring input and appending output to 'nohup.out'
```

Nach `disown` ist die Jobliste leer, obwohl `sleep 903` weiterläuft. `nohup sleep 902` läuft im Vordergrund; während es wartet, schließt du das Fenster. Im ersten Terminal:

```console
$ pgrep -a -x sleep
741 sleep 903
742 sleep 902
$ ps -o pid,ppid,cmd -C sleep
    PID    PPID CMD
    741     315 sleep 903
    742     315 sleep 902
$ ps -o pid,user,cmd -p $(ps -o ppid= -p 742)
    PID USER     CMD
    315 root     /init
$ cat nohup.out
$ pkill -x -f 'sleep 902'
$ pkill -x -f 'sleep 903'
```

Beide überleben. `sleep 902` hat SIGHUP bekommen, aber ignoriert; `sleep 903` hat gar keins bekommen, weil die Shell es nicht mehr in ihrer Liste hatte. Beide haben einen neuen Elternprozess, denn ihre Shell ist mit dem Fenster verschwunden. Unter WSL ist das ein Prozess `/init` von WSL, auf einem gewöhnlichen Linux meist `systemd`. `nohup.out` ist leer, weil `sleep` nichts ausgibt. Zum Schluss beendest du die beiden Versuchsprogramme. Abbildung [21](#abb-21) stellt die drei Fälle nebeneinander.

:::abbildung linux/k8nohup 21
Drei Jobs einer Shell nebeneinander: `sleep 901 &` (gewöhnlich), `sleep 903 &` mit `disown` (aus der Jobliste gestrichen, die Liste zeigt ihn nicht mehr), `nohup sleep 902` (Reaktionstabelle: SIGHUP „ignorieren“). Das Fenster wird geschlossen, die Shell schickt SIGHUP an die Jobs in ihrer Liste: `sleep 901` endet; `sleep 902` bekommt das Signal, weist es ab; `sleep 903` bekommt keines. Die beiden Überlebenden wandern an einen neuen Elternprozess (`/init` bzw. systemd).
:::

⁠**Kurz gesagt:** `nohup` startet ein Programm, das SIGHUP ignoriert; `disown` nimmt einen laufenden Job aus der Liste der Shell, damit sie ihm kein SIGHUP schickt.

### Aufgaben zu Abschnitt [5](#stufe-5)

<span class="anker" id="stufe-5-6"></span>

:::aufgabe Aufgabe 15 ★★★ Aufräumen bei Strg+C und SIGTERM
<span class="anker" id="aufg-15"></span>

Ändere den Versuch aus Unterabschnitt [5.2](#stufe-5-2) so, dass die bash auch bei Strg+C aufräumt (Tipp: `trap` nimmt mehrere Signalnamen). (a) Prüfe, dass `entwurf.tmp` nach Strg+C verschwunden ist, und erkläre den Exit-Status. (b) Wiederhole den Versuch und beende die bash aus dem zweiten Terminal mit `kill -9`. Was bleibt zurück, und warum?

:::loesung
Im ersten Terminal:

```console
$ bash -c 'trap "echo Aufräumen; rm -f entwurf.tmp; exit 1" INT TERM; touch entwurf.tmp; read -t 600'
^C
Aufräumen
$ echo $?
1
$ ls entwurf.tmp
ls: cannot access 'entwurf.tmp': No such file or directory
$ bash -c 'trap "echo Aufräumen; rm -f entwurf.tmp; exit 1" INT TERM; touch entwurf.tmp; read -t 600'
Killed                     bash -c 'trap "echo Aufräumen; rm -f entwurf.tmp; exit 1" INT TERM; touch entwurf.tmp; read -t 600'
$ echo $?
137
$ ls entwurf.tmp
entwurf.tmp
$ rm entwurf.tmp
```

Im zweiten Terminal, während die zweite bash wartete:

```console
$ kill -9 622
```

`trap` nimmt mehrere Signalnamen hintereinander. (a) Strg+C schickt SIGINT; die bash führt ihre Reaktion aus, löscht `entwurf.tmp` und endet mit `exit 1`, deshalb ist der Status 1 und nicht 130. (b) Nach SIGKILL ist der Status $137 = 128 + 9$, und `entwurf.tmp` bleibt liegen: Für SIGKILL gibt es keine eigene Reaktion, die bash kam nicht mehr dazu, aufzuräumen. Genau deshalb schickt man zuerst SIGTERM.
:::
:::

:::aufgabe Aufgabe 16 ★★ Zeitgrenzen
<span class="anker" id="aufg-16"></span>

Sage den Exit-Status vorher und prüfe: (a) `timeout 3 yes > /dev/null`; (b) `timeout -s INT 2 sleep 10`; (c) `timeout --preserve-status 2 sleep 10`. Die Option `--preserve-status` findest du in `man timeout`.

:::loesung
```console
$ timeout 3 yes > /dev/null
$ echo $?
124
$ timeout -s INT 2 sleep 10
$ echo $?
124
$ timeout --preserve-status 2 sleep 10
$ echo $?
143
```

(a) Nach drei Sekunden beendet SIGTERM `yes`, der Status ist 124. (b) Auch mit SIGINT statt SIGTERM meldet `timeout` 124, denn 124 bedeutet nur: Die Zeit war um. (c) Mit `--preserve-status` gibt `timeout` den Status des Befehls selbst weiter; `sleep` endete durch SIGTERM, also $128 + 15 = 143$.
:::
:::

:::aufgabe Aufgabe 17 ★★ Was überlebt das Schließen?
<span class="anker" id="aufg-17"></span>

Im zweiten Terminal startest du nacheinander `sleep 910 &`, `nohup sleep 911 > /dev/null 2>&1 &`, `sleep 912 &` mit anschließendem `disown` und zuletzt `sleep 913` im Vordergrund. Dann schließt du das Fenster. Welche der vier laufen danach noch? Begründe für jeden und prüfe mit `pgrep -a -x sleep` im ersten Terminal. Beende die Überlebenden danach mit `pkill -x -f` und der genauen Befehlszeile.

:::loesung
Im zweiten Terminal, das danach geschlossen wurde, während `sleep 913` lief:

```console
$ sleep 910 &
[1] 637
$ nohup sleep 911 > /dev/null 2>&1 &
[2] 638
$ sleep 912 &
[3] 639
$ disown
$ sleep 913
```

Im ersten Terminal:

```console
$ pgrep -a -x sleep
638 sleep 911
639 sleep 912
$ pkill -x -f 'sleep 911'
$ pkill -x -f 'sleep 912'
```

`sleep 910` ist ein gewöhnlicher Job; die Shell schickt ihm beim Schließen SIGHUP, und es endet. `sleep 911` bekommt SIGHUP ebenfalls, ignoriert es aber, weil `nohup` es so gestartet hat; die Umleitungen sorgen dafür, dass `nohup` nichts meldet und keine `nohup.out` anlegt. `sleep 912` hat `disown` aus der Jobliste gestrichen; die Shell schickt ihm nichts. `sleep 913` lief im Vordergrund und bekommt SIGHUP wie jeder Job dieser Shell; es endet.
:::
:::

:::aufgabe Aufgabe 18 ★ Ein zu breites Muster
<span class="anker" id="aufg-18"></span>

Auf einem Rechner laufen die Programme `sleep`, `sleepwatch` und `asleep-helper`. Welche davon treffen `pkill sleep`, `pkill -x sleep` und `pkill -x -f 'sleep 600'`? Warum prüft man mit `pgrep -a` zuerst?

:::loesung
`pkill sleep` trifft alle drei, denn `sleep` kommt in jedem der drei Namen vor; das Muster ist ein erweiterter regulärer Ausdruck, der an jeder Stelle des Namens passen darf. `pkill -x sleep` trifft nur Prozesse, deren Name genau `sleep` lautet, dafür aber alle, gleich mit welchen Argumenten. `pkill -x -f 'sleep 600'` trifft nur Prozesse, deren ganze Befehlszeile genau `sleep 600` ist. Mit `pgrep -a` und denselben Optionen sieht man vorher, welche Prozesse das Signal bekämen, ohne einem davon etwas zu schicken.
:::
:::

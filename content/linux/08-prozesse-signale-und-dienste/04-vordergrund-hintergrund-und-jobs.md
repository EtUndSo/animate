---
title: Vordergrund, Hintergrund und Jobs
pfad: Informatik / Linux und Kommandozeile / Prozesse, Signale und Dienste
adresse: informatik/linux-und-kommandozeile/prozesse-signale-und-dienste
knoten: Kapitel 8: Prozesse, Signale und Dienste
order: 6130400
summary: Bisher hat die Shell nach jedem Befehl gewartet, bis er fertig war; für einen zweiten Prozess brauchtest du ein zweites Fenster.
tags: Vordergrund, Hintergrund, Job, Jobangabe, Strg+Z
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Bisher hat die Shell nach jedem Befehl gewartet, bis er fertig war; für einen zweiten Prozess brauchtest du ein zweites Fenster. Dieser Abschnitt zeigt, wie eine einzige Shell mehrere Programme gleichzeitig verwaltet: eines im Vordergrund, andere im Hintergrund oder angehalten, und wie man sie zwischen diesen Rollen hin- und herschiebt.
:::

### Der Vordergrund

<span class="anker" id="stufe-3-1"></span>

Startest du ein Programm, kehrt die Eingabeaufforderung erst zurück, wenn es fertig ist, und alles, was du in dieser Zeit tippst, geht an das Programm, auch Strg+C. Das hat einen Namen.

:::definition Definition 3.1 (Vordergrund)
<span class="anker" id="satz-3-1"></span>

Ein Programm läuft im __Vordergrund__, wenn die Shell auf sein Ende wartet und es die Eingaben des Terminals bekommt. Je Terminal ist zu jeder Zeit höchstens ein Befehl im Vordergrund, bei einer Pipeline alle ihre Programme zusammen; solange er läuft, nimmt die Shell keine Befehle an.
:::

```console
$ sleep 3
$ sleep 300
^C
```

Nach `sleep 3` erscheint die Eingabeaufforderung erst nach drei Sekunden: So lange war `sleep` im Vordergrund, und die Shell wartete mit wait. `sleep 300` beendest du mit Strg+C, das an das Programm im Vordergrund geht.

⁠**Kurz gesagt:** Das Programm im Vordergrund bekommt die Eingaben des Terminals, und die Shell wartet auf sein Ende.

### Der Hintergrund: &

<span class="anker" id="stufe-3-2"></span>

Ein Programm, das lange rechnet oder wartet, blockiert so das ganze Terminal. Schöner wäre es, wenn die Shell es startet und sofort wieder Befehle annimmt. Das Zeichen dafür hat Unterabschnitt [2.6](prozesse-beobachten.html#stufe-2-6) schon benutzt.

:::definition Definition 3.2 (Hintergrund)
<span class="anker" id="satz-3-2"></span>

Ein Befehl mit `&` am Ende läuft im __Hintergrund__: Die Shell startet ihn, wartet nicht auf ihn und zeigt sofort wieder die Eingabeaufforderung. Sie meldet in eckigen Klammern eine laufende Nummer und dahinter die PID des gestarteten Prozesses; die PID steht danach im Parameter `$!`.
:::

```console
$ sleep 300 &
[1] 654
$ echo $!
654
$ ps -o pid,stat,cmd -C sleep
    PID STAT CMD
    654 S    sleep 300
```

`sleep` wartet weiter (`S`), aber ohne das `+` aus Unterabschnitt [2.5](prozesse-beobachten.html#stufe-2-5): Es gehört nicht zum Vordergrund. Ein Programm im Hintergrund bekommt keine Tastatureingaben, auch Strg+C erreicht es nicht. Seine Ausgabe geht aber weiter ins Terminal; ein Hintergrundprogramm, das schreibt, mischt seine Zeilen deshalb mitten zwischen deine. Wer das nicht will, leitet die Ausgabe in eine Datei um. Abbildung [10](#abb-10) vergleicht beide Arten zu starten.

:::abbildung linux/k8vordergrund 10
Zwei Zeitleisten mit je einer Spur für die Shell und einer für sleep. Oben `sleep 3`: fork, die Shell steht drei Sekunden lang im Zustand „wartet“, ihre Eingabeaufforderung ist grau; die Tastatur zeigt mit einem Pfeil auf sleep; erst nach dem Ende kommt die Eingabeaufforderung. Unten `sleep 300 &`: fork, die Shell zeigt sofort wieder die Eingabeaufforderung und nimmt weitere Befehle an, der Tastaturpfeil zeigt auf die Shell; sleep läuft daneben weiter. Eine Uhr über beiden Leisten läuft mit.
:::

⁠**Kurz gesagt:** Mit `&` startet die Shell ein Programm im Hintergrund, nimmt sofort wieder Befehle an und merkt sich seine PID in `$!`.

:::hintergrund Warum Strg+C ein Hintergrundprogramm nicht erreicht
Die Tastenkombination Strg+C wertet der Kernel im Terminal aus, nicht die Shell ([Kapitel 2, Abschnitt 5.4](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/schneller-arbeiten-vervollstandigung-verlauf-tastenkurzel.html#stufe-5-4)). Er schickt die Unterbrechung an alle Prozesse, die gerade zum Vordergrund des Terminals gehören. Die Shell legt jeden Befehl, den sie startet, in eine eigene Prozessgruppe, und sie sagt dem Terminal bei jedem Wechsel, welche Gruppe gerade vorn ist. Ein Programm im Hintergrund gehört zu einer anderen Gruppe und bekommt die Unterbrechung deshalb nicht. Die Prozesse einer Pipeline bilden zusammen eine Gruppe; darum beendet Strg+C eine ganze Pipeline auf einmal.
:::

### Der Job

<span class="anker" id="stufe-3-3"></span>

Mit `&` kann eine Shell schnell mehrere Programme gleichzeitig laufen haben. Um sie auseinanderzuhalten, führt sie eine eigene Liste, die von der PID unabhängig ist.

:::definition Definition 3.3 (Job, Jobangabe)
<span class="anker" id="satz-3-3"></span>

Ein __Job__ ist ein Befehl oder eine Pipeline, die eine Shell gestartet hat und noch verwaltet. Die Shell nummeriert ihre Jobs ab 1. `jobs` zeigt die Liste, `jobs -l` zusätzlich die PIDs. Eine __Jobangabe__ bezeichnet einen Job in Befehlen: `%1` den Job 1, `%+` oder `%%` den aktuellen Job (in der Liste mit `+` markiert), `%-` den vorigen (mit `-` markiert) und `%sleep` den Job, dessen Befehl mit `sleep` beginnt.
:::

```console
$ sleep 301 &
[2] 656
$ jobs
[1]-  Running                    sleep 300 &
[2]+  Running                    sleep 301 &
$ jobs -l
[1]-   654 Running                    sleep 300 &
[2]+   656 Running                    sleep 301 &
```

Die laufende Nummer in eckigen Klammern, die die Shell beim Start mit `&` meldet, ist die Jobnummer: `[2] 656` heißt Job 2 mit der PID 656. Der zuletzt gestartete Job 2 ist der aktuelle, Job 1 der vorige. Abbildung [11](#abb-11) zerlegt eine Zeile von `jobs -l`.

:::abbildung linux/k8jobliste 11
Die Zeile `[2]+ 656 Running sleep 301 &` wird in Teile zerlegt; unter jedem erscheint nacheinander seine Bedeutung: Jobnummer (nur in dieser Shell gültig), Marke „aktueller Job“, PID (im ganzen System gültig), Zustand des Jobs, Befehl, `&` für „läuft im Hintergrund“. Darunter die Zeile von Job 1 mit der Marke `-` für „voriger Job“; zum Schluss zeigen zwei Pfeile, worauf sich `%+` und `%-` beziehen.
:::

Jobnummern gelten nur in der Shell, die die Jobs gestartet hat; eine andere Shell, etwa im zweiten Terminal, kennt sie nicht. Die PID dagegen gilt im ganzen System.

⁠**Kurz gesagt:** Ein Job ist ein Befehl, den die Shell gestartet hat und verwaltet; `jobs` listet die Jobs, `%1` oder `%+` bezeichnet einen davon.

### Anhalten mit Strg+Z

<span class="anker" id="stufe-3-4"></span>

Was, wenn ein Programm schon im Vordergrund läuft und du die Shell zurückhaben willst, ohne es zu beenden? Strg+C würde es beenden. Es gibt eine zweite Tastenkombination, die nur anhält.

:::definition Definition 3.4 (Strg+Z)
<span class="anker" id="satz-3-4"></span>

__Strg+Z__ hält das Programm im Vordergrund an, ohne es zu beenden. Es kommt in den Zustand T aus Unterabschnitt [2.5](prozesse-beobachten.html#stufe-2-5), die Shell meldet es als angehaltenen Job und nimmt wieder Befehle an.
:::

```console
$ sleep 302
^Z
[3]+  Stopped                    sleep 302
$ jobs
[1]   Running                    sleep 300 &
[2]-  Running                    sleep 301 &
[3]+  Stopped                    sleep 302
$ ps -o pid,stat,cmd -C sleep
    PID STAT CMD
    654 S    sleep 300
    656 S    sleep 301
    657 T    sleep 302
```

`sleep 302` ist angehalten (`Stopped`, Zustand `T`) und der neue aktuelle Job.

::::beispiel Ein Hintergrundprogramm, das lesen will
`cat` ohne Argument liest von der Tastatur ([Kapitel 4, Abschnitt 1.4](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/prozesse-und-ihre-drei-strome.html#stufe-1-4)). Im Hintergrund darf es das aber nicht, denn die Tastatur gehört dem Vordergrund:

```console
$ cat &
[4] 659
$ jobs
[1]   Running                    sleep 300 &
[2]   Running                    sleep 301 &
[3]-  Stopped                    sleep 302
[4]+  Stopped                    cat
$ fg
cat
Hallo
Hallo
```

Sobald `cat` vom Terminal lesen wollte, hat der Kernel es angehalten. `fg` holt den aktuellen Job, also `cat`, in den Vordergrund; nun darf es lesen. Die getippte Zeile `Hallo` schreibt `cat` gleich zurück. Strg+D beendet seine Eingabe ([Kapitel 2, Abschnitt 5.5](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/schneller-arbeiten-vervollstandigung-verlauf-tastenkurzel.html#stufe-5-5)). Abbildung [12](#abb-12) zeigt den Ablauf.

:::abbildung linux/k8hintergrundlesen 12
Ein Terminal mit Tastatur, darüber zwei Felder „Vordergrund“ (dort die Shell) und „Hintergrund“ (dort `cat`). `cat` streckt die Hand nach der Tastatur aus; der Kernel hält es an (Zustand T, ein Pausenzeichen), denn die Tastatur gehört dem Vordergrund. Dann holt `fg` das Kärtchen `cat` in das Feld Vordergrund, das Pausenzeichen verschwindet, die getippte Zeile „Hallo“ wandert zu `cat` und kommt als Ausgabe zurück.
:::
::::

⁠**Kurz gesagt:** Strg+Z hält das Programm im Vordergrund an (Zustand T) und gibt die Shell frei, ohne das Programm zu beenden.

### Weiterlaufen lassen: fg und bg

<span class="anker" id="stufe-3-5"></span>

Ein angehaltener Job wartet, bis du entscheidest, wie es weitergeht: im Vordergrund, wo er wieder die Tastatur bekommt, oder im Hintergrund, wo er neben der Shell weiterläuft. Für beides gibt es einen eingebauten Befehl.

:::definition Definition 3.5 (fg, bg)
<span class="anker" id="satz-3-5"></span>

`fg jobangabe` holt einen Job in den Vordergrund und lässt ihn weiterlaufen, falls er angehalten war; die Shell wartet dann auf ihn. `bg jobangabe` lässt einen angehaltenen Job im Hintergrund weiterlaufen. Ohne Jobangabe gilt der aktuelle Job.
:::

```console
$ bg
[3]+ sleep 302 &
$ jobs
[1]   Running                    sleep 300 &
[2]-  Running                    sleep 301 &
[3]+  Running                    sleep 302 &
$ fg %1
sleep 300
^C
$ fg
sleep 302
^C
$ fg
sleep 301
^C
$ jobs
```

`bg` schickt den angehaltenen Job 3 in den Hintergrund; `jobs` zeigt ihn mit `&` als laufend. `fg %1` holt Job 1 nach vorn; die Shell schreibt seinen Befehl aus und wartet, bis Strg+C ihn beendet. Die beiden übrigen Jobs holst du genauso nach vorn und beendest sie. Danach ist die Liste leer. Abbildung [13](#abb-13) fasst alle Übergänge zusammen.

:::abbildung linux/k8jobzustaende 13
Drei Felder: „Vordergrund“, „Hintergrund (läuft)“, „angehalten“. Ein Job-Kärtchen `[3] sleep 302` startet im Vordergrund (`sleep 302`), wandert mit Strg+Z nach „angehalten“, mit `bg` nach „Hintergrund“ und mit `fg` zurück in den Vordergrund. Zusätzliche Pfeile: Start mit `&` direkt in den Hintergrund, `fg` von „angehalten“ in den Vordergrund, Strg+C und das Ende des Programms aus dem Vordergrund ins Aus. Das Feld Vordergrund hat ein Tastatursymbol; es leuchtet jeweils dort auf, wo der Job die Eingaben bekommt.
:::

⁠**Kurz gesagt:** `fg` holt einen Job in den Vordergrund, `bg` lässt einen angehaltenen Job im Hintergrund weiterlaufen.

### Warten: wait

<span class="anker" id="stufe-3-6"></span>

Manchmal startet man mehrere Programme im Hintergrund und will erst weitermachen, wenn alle fertig sind. Die Shell kann dafür das tun, was sie im Vordergrund ohnehin tut: auf ihre Kinder warten.

:::definition Definition 3.6 (wait (Befehl))
<span class="anker" id="satz-3-6"></span>

Der eingebaute Befehl `wait` wartet, bis alle Hintergrundjobs der Shell geendet haben. Mit einer PID oder einer Jobangabe wartet er nur auf diesen Prozess und endet mit dessen Exit-Status.
:::

```console
$ sleep 3 &
[1] 660
$ sleep 5 &
[2] 661
$ wait
[1]-  Done                       sleep 3
[2]+  Done                       sleep 5
$ echo $?
0
```

`wait` kehrt nach fünf Sekunden zurück, als der längere Job fertig war. Die Shell meldet jeden beendeten Hintergrundjob mit `Done`. Solche Meldungen schreibt sie in der Regel erst, bevor sie die nächste Eingabeaufforderung zeigt; endet ein Hintergrundjob, während du tippst, erscheint seine Meldung deshalb erst nach deinem nächsten Befehl.

⁠**Kurz gesagt:** `wait` wartet auf alle Hintergrundjobs oder auf einen bestimmten und liefert dessen Exit-Status.

### Aufgaben zu Abschnitt [3](#stufe-3)

<span class="anker" id="stufe-3-7"></span>

:::aufgabe Aufgabe 7 ★★ Jobs steuern
<span class="anker" id="aufg-7"></span>

Starte `sleep 300 &` und danach `sleep 301` im Vordergrund. Halte `sleep 301` an, lass es im Hintergrund weiterlaufen, hole Job 1 in den Vordergrund und beende ihn mit Strg+C. Beende zuletzt den übrigen Job mit `fg` und Strg+C. Sieh nach jedem Schritt mit `jobs` nach und erkläre die Marken `+` und `-`.

:::loesung
```console
$ sleep 300 &
[1] 578
$ sleep 301
^Z
[2]+  Stopped                    sleep 301
$ jobs
[1]-  Running                    sleep 300 &
[2]+  Stopped                    sleep 301
$ bg
[2]+ sleep 301 &
$ jobs
[1]-  Running                    sleep 300 &
[2]+  Running                    sleep 301 &
$ fg %1
sleep 300
^C
$ fg
sleep 301
^C
$ jobs
```

Das `+` markiert den aktuellen Job, den `fg` und `bg` ohne Angabe nehmen; das ist der zuletzt angehaltene oder in den Hintergrund geschickte Job, hier Job 2. Das `-` markiert den vorigen. `bg` schickt den angehaltenen Job 2 in den Hintergrund, `fg %1` holt Job 1 nach vorn, und Strg+C beendet ihn. Danach ist Job 2 der einzige und damit der aktuelle; `fg` holt ihn nach vorn, Strg+C beendet ihn, und die Liste ist leer.
:::
:::

:::aufgabe Aufgabe 8 ★ Meldungen der Shell deuten
<span class="anker" id="aufg-8"></span>

Was bedeuten diese Zeilen? `[2] 4711` `[1]- Stopped sleep 302` `[2]+ Running sleep 400 &` `[2]+ Done sleep 400`

:::loesung
`[2] 4711`: Ein Befehl wurde mit `&` im Hintergrund gestartet; er ist Job 2, und sein Prozess hat die PID 4711. `[1]- Stopped sleep 302`: Job 1, `sleep 302`, ist angehalten, etwa durch Strg+Z, und ist der vorige Job. `[2]+ Running sleep 400 &`: Job 2 läuft im Hintergrund und ist der aktuelle Job. `[2]+ Done sleep 400`: Job 2 ist mit dem Exit-Status 0 fertig geworden; die Shell meldet es vor der nächsten Eingabeaufforderung und streicht ihn aus der Liste.
:::
:::

:::aufgabe Aufgabe 9 ★★ cat im Hintergrund
<span class="anker" id="aufg-9"></span>

`cat &` hält sofort an. Was geschieht bei `cat /etc/hostname > name.txt &`? Sage es vorher, prüfe mit `jobs` und `cat name.txt` und erkläre den Unterschied.

:::loesung
```console
$ cat /etc/hostname > name.txt &
[1] 586
$ jobs
[1]+  Done                       cat /etc/hostname > name.txt
$ cat name.txt
labor
```

Diesmal hält `cat` nicht an, sondern ist sofort fertig (`Done`). Mit einem Dateinamen als Argument liest `cat` aus der Datei, nicht vom Terminal, und schreibt in die Datei `name.txt`. Angehalten wird ein Hintergrundprogramm nur, wenn es vom Terminal lesen will, denn die Tastatur gehört dem Vordergrund.
:::
:::

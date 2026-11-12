---
title: Signale
pfad: Informatik / Linux und Kommandozeile / Prozesse, Signale und Dienste
adresse: informatik/linux-und-kommandozeile/prozesse-signale-und-dienste
knoten: Kapitel 8: Prozesse, Signale und Dienste
order: 6130500
summary: Strg+C beendet, Strg+Z hält an, und ein Hintergrundprogramm, das lesen will, wird angehalten.
tags: Signal, Standardreaktion, SIGTERM, SIGINT, SIGKILL, SIGSTOP, SIGTSTP, SIGCONT
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Strg+C beendet, Strg+Z hält an, und ein Hintergrundprogramm, das lesen will, wird angehalten. Hinter all dem steckt derselbe Mechanismus: kurze Nachrichten, die der Kernel einem Prozess zustellt. Dieser Abschnitt erklärt diese Signale, zeigt, wie man sie selbst schickt, warum es eines gibt, dem kein Programm entkommt, und wer wem Signale schicken darf.
:::

### Das Signal

<span class="anker" id="stufe-4-1"></span>

[Kapitel 2](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/die-shell-erste-befehle.html) und 4 haben von einer Unterbrechungsnachricht gesprochen, die Strg+C an das Programm im Vordergrund schickt. Solche Nachrichten gibt es viele, für verschiedene Zwecke. Ab hier tragen sie ihren üblichen Namen.

:::definition Definition 4.1 (Signal)
<span class="anker" id="satz-4-1"></span>

Ein __Signal__ ist eine kurze Nachricht, die der Kernel einem Prozess zustellt und die ihn in seiner Arbeit unterbricht. Jedes Signal hat eine Nummer und einen Namen, der mit `SIG` beginnt. Signale schickt der Kernel von sich aus, etwa wenn im Terminal Strg+C gedrückt wird, oder im Auftrag eines anderen Prozesses.
:::

Die Unterbrechungsnachricht von Strg+C ist das Signal `SIGINT` mit der Nummer 2 (englisch „interrupt“). Ein Signal überbringt keinen Text und keine Daten wie eine Pipe; seine Bedeutung liegt allein in seiner Art. Abbildung [14](#abb-14) zeigt den Weg eines Signals.

:::abbildung linux/k8signal 14
Links zwei Absender: eine Tastatur mit Strg+C (grau, der Weg ist aus [Kapitel 2](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/die-shell-erste-befehle.html) bekannt) und ein Prozess „kill“. Neu und betont: Jedes Signal ist ein Kärtchen mit Nummer und Namen (2 SIGINT bzw. 15 SIGTERM), und auch der Prozess „kill“ schickt sein Kärtchen über den Kernel in der Mitte. Der Kernel legt das Kärtchen beim Zielprozess rechts ab, dessen Programm gerade läuft. Der Zielprozess wird unterbrochen (seine Spur bricht ab), schaut in seiner Reaktionstabelle nach, was für dieses Signal gilt, und führt die Reaktion aus: hier „beenden“.
:::

⁠**Kurz gesagt:** Ein Signal ist eine kurze, nummerierte Nachricht des Kernels, die einen Prozess unterbricht.

### Die Standardreaktion

<span class="anker" id="stufe-4-2"></span>

Was tut ein Prozess, wenn ein Signal eintrifft? Die meisten Programme kümmern sich gar nicht um Signale. Für sie legt der Kernel fest, was geschieht.

:::definition Definition 4.2 (Standardreaktion)
<span class="anker" id="satz-4-2"></span>

Jede Signalart hat eine __Standardreaktion__, die der Kernel ausführt, wenn das Programm nichts anderes festgelegt hat. Es gibt fünf: den Prozess beenden; den Prozess beenden und ein Speicherabbild schreiben; das Signal ignorieren; den Prozess anhalten; einen angehaltenen Prozess weiterlaufen lassen.
:::

Ein Speicherabbild (englisch „core dump“) ist eine Kopie des Speichers des Prozesses im Augenblick seines Endes; damit kann man später untersuchen, woran ein Programm gescheitert ist. Tabelle [1](#tab-1) zeigt die Signale, die in diesem Kapitel vorkommen, mit ihren Standardreaktionen.

<span class="anker" id="tab-1"></span>

**Tabelle 1:** Wichtige Signale mit Nummer und Standardreaktion. Die Nummern 1 bis 15 sind auf allen Linux-Systemen gleich; die übrigen gelten für die Prozessorfamilien x86 und ARM, also für übliche PCs, Notebooks und den Raspberry Pi, und weichen auf einigen anderen ab. `kill -l` nennt sie für das eigene System.

| Nr. | Name | Standardreaktion | Wer es typischerweise schickt |
|---|---|---|---|
| 1 | SIGHUP | beenden | Terminal geschlossen („aufgelegt“) |
| 2 | SIGINT | beenden | Strg+C |
| 3 | SIGQUIT | beenden, Speicherabbild | Strg+`\` |
| 9 | SIGKILL | beenden; nicht abfangbar | `kill -9` |
| 11 | SIGSEGV | beenden, Speicherabbild | Kernel bei unerlaubtem Speicherzugriff |
| 13 | SIGPIPE | beenden | Kernel beim Schreiben in eine Pipe ohne Leser |
| 15 | SIGTERM | beenden | `kill` ohne Angabe, Herunterfahren |
| 17 | SIGCHLD | ignorieren | Kernel an den Elternprozess, wenn ein Kind endet |
| 18 | SIGCONT | weiterlaufen lassen | `fg`, `bg` |
| 19 | SIGSTOP | anhalten; nicht abfangbar | `kill -STOP` |
| 20 | SIGTSTP | anhalten | Strg+Z |
| 21 | SIGTTIN | anhalten | Kernel, wenn ein Hintergrundprogramm vom Terminal liest |
| 28 | SIGWINCH | ignorieren | Kernel, wenn sich die Größe des Terminalfensters ändert |

Alle Signale mit Nummern listet `kill -l`; mit einer Nummer oder einem Namen übersetzt es in die andere Richtung:

```console
$ kill -l | head -n 3
 1) SIGHUP       2) SIGINT       3) SIGQUIT      4) SIGILL       5) SIGTRAP
 6) SIGABRT      7) SIGBUS       8) SIGFPE       9) SIGKILL     10) SIGUSR1
11) SIGSEGV     12) SIGUSR2     13) SIGPIPE     14) SIGALRM     15) SIGTERM
$ kill -l 15
TERM
$ kill -l TERM
15
```

SIGPIPE mit der Nummer 13 kennst du schon: In [Kapitel 4, Abschnitt 6.5](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/befehle-verketten.html#stufe-6-5) endete `yes` mit dem Status 141, als `head` nicht mehr las.

⁠**Kurz gesagt:** Jedes Signal hat eine Standardreaktion, meist beenden, sonst ignorieren, anhalten oder weiterlaufen lassen; `kill -l` zeigt alle Signale.

### Signale senden: kill

<span class="anker" id="stufe-4-3"></span>

Bisher kamen Signale von der Tastatur. Ein Programm, das nicht im Vordergrund läuft, erreicht man so nicht. Dafür gibt es einen Befehl, dessen Name täuscht.

:::definition Definition 4.3 (kill)
<span class="anker" id="satz-4-3"></span>

`kill -signal ziel` schickt einem Prozess ein Signal. Das Ziel ist eine PID oder eine Jobangabe; das Signal steht als Nummer (`-15`) oder Name (`-TERM`, `-SIGTERM`, `-s TERM`). Ohne Signalangabe schickt `kill` SIGTERM.
:::

`kill` beendet also nicht selbst, es schickt nur; was der Prozess daraufhin tut, hängt vom Signal ab. In der bash ist `kill` ein eingebauter Befehl, damit es Jobangaben versteht. Daneben gibt es das Programm `/usr/bin/kill`; es versteht nur PIDs und meldet bei `%1` einen Fehler.

```console
$ sleep 400 &
[1] 665
$ kill 665
$ jobs
[1]+  Terminated                 sleep 400
$ sleep 401 &
[1] 667
$ kill -s TERM %1
$ jobs
[1]+  Terminated                 sleep 401
```

Beide Male endet `sleep` durch SIGTERM, und die Shell meldet den Job als `Terminated` („beendet“). Weil die Liste danach leer war, bekam der zweite Job wieder die Nummer 1.

⁠**Kurz gesagt:** `kill` schickt einem Prozess oder Job ein Signal, ohne Angabe SIGTERM.

### Bitten und unterbrechen: SIGTERM und SIGINT

<span class="anker" id="stufe-4-4"></span>

Es gibt mehrere Signale, die einen Prozess beenden. Zwei davon sind die gewöhnlichen Wege; sie unterscheiden sich vor allem darin, woher sie kommen.

:::definition Definition 4.4 (SIGTERM, SIGINT)
<span class="anker" id="satz-4-4"></span>

__SIGTERM__ (Nummer 15, „terminate“) ist die gewöhnliche Aufforderung an einen Prozess, sich zu beenden. __SIGINT__ (Nummer 2) ist die Unterbrechung von der Tastatur, die Strg+C auslöst. Beide beenden einen Prozess, der nichts anderes festgelegt hat; ein Programm darf für beide aber eine eigene Reaktion festlegen.
:::

Der Versuch braucht beide Terminals. Im ersten startest du zweimal `sleep 402` im Vordergrund. Während es wartet, schickst du ihm aus dem zweiten Terminal ein Signal, beim ersten Mal SIGTERM, beim zweiten Mal SIGINT; die Nummer liefert dort `pgrep sleep`. Im ersten Terminal:

```console
$ sleep 402
Terminated                 sleep 402
$ echo $?
143
$ sleep 402
$ echo $?
130
```

Im zweiten Terminal:

```console
$ kill 671
$ kill -INT 673
```

Nach SIGTERM meldet die Shell `Terminated` und den Exit-Status $143 = 128 + 15$. Nach SIGINT schreibt sie nichts, wie nach Strg+C, und der Status ist $130 = 128 + 2$. Ein SIGINT von außen wirkt also genau wie Strg+C.

::::beispiel Die Shell überhört SIGTERM
Eine interaktive Shell reagiert nicht auf SIGTERM:

```console
$ echo $$
535
$ kill $$
$ echo "Ich bin noch da"
Ich bin noch da
```

Die bash ignoriert SIGTERM, solange sie interaktiv ist. Manche Befehle schicken ein Signal an eine ganze Gruppe von Prozessen, zu der auch die Shell gehören kann; die Shell, an der man gerade arbeitet, soll dabei nicht verschwinden.
::::

⁠**Kurz gesagt:** SIGTERM bittet einen Prozess, sich zu beenden, SIGINT ist dasselbe von der Tastatur; beide kann ein Programm anders behandeln.

### Das Ende ohne Rückfrage: SIGKILL

<span class="anker" id="stufe-4-5"></span>

Ein Programm kann SIGTERM und SIGINT auch ignorieren, absichtlich oder weil es hängt. Damit trotzdem jedes Programm zu beenden ist, gibt es ein Signal, an dem kein Programm etwas ändern kann.

:::definition Definition 4.5 (SIGKILL)
<span class="anker" id="satz-4-5"></span>

__SIGKILL__ (Nummer 9) beendet einen Prozess sofort. Kein Programm kann für SIGKILL eine eigene Reaktion festlegen, es nicht ignorieren und nicht aufschieben; der Kernel beendet den Prozess, ohne dass dessen Programm noch einen einzigen Befehl ausführt.
:::

Wieder mit beiden Terminals: Im ersten startest du `sleep 403`, im zweiten schickst du ihm mit `kill -9` und seiner PID SIGKILL. Im ersten Terminal:

```console
$ sleep 403
Killed                     sleep 403
$ echo $?
137
```

Im zweiten Terminal:

```console
$ kill -9 675
```

Die Shell meldet `Killed`, der Status ist $137 = 128 + 9$. Eine Grenze hat auch SIGKILL: Ein Prozess im Zustand D (Unterabschnitt [2.5](prozesse-beobachten.html#stufe-2-5)) endet erst, wenn er diesen Zustand verlässt, also wenn das Gerät geantwortet hat. Abbildung [15](#abb-15) vergleicht das Ende durch SIGTERM mit dem durch SIGKILL.

:::abbildung linux/k8termkill 15
Zwei Prozesse nebeneinander, jeder mit einer offenen Datei `entwurf.tmp` und einem halb geschriebenen Satz im Speicher. Links trifft SIGTERM ein: Der Prozess darf noch reagieren, speichert den Satz, löscht `entwurf.tmp` und endet; zurück bleibt ein aufgeräumter Arbeitsplatz. Rechts trifft SIGKILL ein: Der Kernel greift direkt ein (ein Schloss an der Reaktionstabelle), der Prozess verschwindet sofort; `entwurf.tmp` bleibt liegen, der Satz ist verloren.
:::

⁠**Kurz gesagt:** SIGKILL beendet jeden Prozess sofort und lässt sich weder abfangen noch ignorieren; dafür kann das Programm nicht mehr aufräumen.

:::hintergrund Warum es ein unabfangbares Signal gibt und warum man trotzdem zuerst SIGTERM schickt
Dürfte jedes Programm alle Signale abfangen, könnte ein fehlerhaftes oder bösartiges Programm sich unbeendbar machen; nur ein Neustart des ganzen Rechners würde es loswerden. Deshalb behält sich der Kernel zwei Signale vor: SIGKILL zum Beenden und SIGSTOP zum Anhalten. Für sie gibt es keine eigene Reaktion; der Kernel führt sie aus, ohne das Programm zu fragen. So bleibt jeder Prozess beendbar und anhaltbar, zumindest für den, der ihm Signale schicken darf.

Gerade diese Rücksichtslosigkeit ist aber der Grund, SIGKILL erst als letztes Mittel zu benutzen. Ein Programm, das SIGTERM bekommt, kann noch aufräumen: Daten aus dem Speicher in eine Datei schreiben, vorübergehende Dateien löschen, Kindprozesse beenden, eine Datenbank in einen sauberen Zustand bringen. Nach SIGKILL bleibt alles liegen, wie es gerade war. Die Regel lautet deshalb: erst SIGTERM, ein paar Sekunden warten, und nur wenn der Prozess dann noch läuft, SIGKILL. Beim Herunterfahren hält sich das System selbst daran.
:::

### Anhalten und fortsetzen: SIGSTOP, SIGTSTP und SIGCONT

<span class="anker" id="stufe-4-6"></span>

Strg+Z hat in Unterabschnitt [3.4](vordergrund-hintergrund-und-jobs.html#stufe-3-4) ein Programm angehalten, und `fg` und `bg` haben es weiterlaufen lassen. Auch dahinter stecken Signale, und mit `kill` kann man sie jedem eigenen Prozess schicken, nicht nur dem im Vordergrund.

:::definition Definition 4.6 (SIGSTOP, SIGTSTP, SIGCONT)
<span class="anker" id="satz-4-6"></span>

__SIGSTOP__ (Nummer 19) hält einen Prozess an und lässt sich wie SIGKILL weder abfangen noch ignorieren. __SIGTSTP__ (Nummer 20, „terminal stop“) ist die Anhalte-Bitte von der Tastatur, die Strg+Z auslöst; ein Programm darf sie anders behandeln. __SIGCONT__ (Nummer 18) lässt einen angehaltenen Prozess weiterlaufen; `fg` und `bg` schicken es.
:::

```console
$ sleep 404 &
[1] 685
$ kill -STOP %1
$ jobs
[1]+  Stopped                    sleep 404
$ ps -o pid,stat,cmd -C sleep
    PID STAT CMD
    685 T    sleep 404
$ kill -CONT %1
$ jobs
[1]+  Running                    sleep 404 &
$ kill %1
$ jobs
[1]+  Terminated                 sleep 404
```

Auch ein Programm im Vordergrund lässt sich von außen anhalten. Im ersten Terminal startest du `sleep 405`, im zweiten schickst du ihm mit `kill -STOP` und seiner PID das Signal SIGSTOP:

```console
$ sleep 405
[1]+  Stopped                    sleep 405
$ echo $?
147
$ fg
sleep 405
^C
```

Die Shell bemerkt, dass ihr Vordergrundprogramm angehalten wurde, macht einen Job daraus und nimmt wieder Befehle an, genau wie nach Strg+Z.

⁠**Kurz gesagt:** SIGSTOP hält jeden Prozess an, SIGTSTP ist die abfangbare Bitte von Strg+Z, SIGCONT lässt einen angehaltenen Prozess weiterlaufen.

### Was der Exit-Status verrät: 128 + n

<span class="anker" id="stufe-4-7"></span>

In diesem Abschnitt kamen immer wieder Exit-Status über 128 vor. [Kapitel 4, Abschnitt 5.3](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/der-exit-status.html#stufe-5-3) hat die Regel dahinter schon genannt; mit den Signalnamen wird sie jetzt zu einem Werkzeug, um nachträglich herauszufinden, was einem Programm zugestoßen ist.

:::satz Satz 4.7 (Exit-Status nach einem Signal)
<span class="anker" id="satz-4-7"></span>

Endet oder hält ein Programm durch ein Signal mit der Nummer $n$, setzt die bash den Exit-Status auf $128 + n$. Umgekehrt verrät ein Status $s$ über 128 das Signal $n = s - 128$; `kill -l s` nennt seinen Namen.
:::

```console
$ kill -l 143
TERM
$ kill -l 130
INT
$ kill -l 137
KILL
$ kill -l 148
TSTP
```

`kill -l` rechnet bei Zahlen über 128 selbst $128$ ab. Ein Status über 128 bedeutet allerdings nicht zwingend ein Signal: Ein Programm darf auch von sich aus mit 143 enden. Die bash unterscheidet beide Fälle intern, denn wait meldet ihr getrennt, ob ein Kind mit einem Status geendet hat oder durch ein Signal; erst für `$?` fasst sie beides in eine Zahl.

::::beispiel [Rechenbeispiel] Vom Status zum Signal
Nach dem Versuch in Unterabschnitt [4.6](#stufe-4-6) stand 147 in `$?`, und `sleep 405` war nicht beendet, sondern angehalten. $147 - 128 = 19$, und 19 ist auf üblichen PCs SIGSTOP (Tabelle [1](#tab-1)). Nach Strg+Z steht dort $128 + 20 = 148$, denn Strg+Z schickt SIGTSTP mit der Nummer 20. Abbildung [16](#abb-16) rechnet die Fälle dieses Abschnitts nach.

:::abbildung linux/k8exitrechnung 16
Rechenbild, Zeile für Zeile: $143 - 128 = 15$ (SIGTERM, `kill`); $130 - 128 = 2$ (SIGINT, Strg+C); $137 - 128 = 9$ (SIGKILL, `kill -9`); $147 - 128 = 19$ (SIGSTOP, `kill -STOP`); $148 - 128 = 20$ (SIGTSTP, Strg+Z). In jeder Zeile erscheint zuerst der Status, dann die Subtraktion, dann die Nummer, zuletzt der Name.
:::
::::

⁠**Kurz gesagt:** Ein Exit-Status $128 + n$ verrät, dass das Signal $n$ das Programm beendet oder angehalten hat; `kill -l` übersetzt ihn in den Namen.

### Wer wem Signale schicken darf

<span class="anker" id="stufe-4-8"></span>

Signale sind mächtig: SIGKILL beendet jeden Prozess. Dürfte jeder Benutzer jedem Prozess Signale schicken, könnte jeder die Programme der anderen und die des Systems beenden. Deshalb prüft der Kernel bei jedem Signal, ob der Absender das darf.

:::satz Satz 4.8 (Erlaubnis für Signale)
<span class="anker" id="satz-4-8"></span>

Ein Prozess darf einem anderen ein Signal schicken, wenn seine reale oder effektive Benutzernummer gleich der realen oder gespeicherten Benutzernummer des Ziels ist. Ein Prozess von root darf jedem Prozess Signale schicken.
:::

Real und effektiv sind die Benutzernummern aus [Kapitel 7, Abschnitt 9.2](/wissen/informatik/linux-und-kommandozeile/benutzer-gruppen-und-rechte/programme-ausfuhren-und-besondere-rechte.html#stufe-9-2), gespeichert die aus Unterabschnitt [2.8](prozesse-beobachten.html#stufe-2-8). Zwei Feinheiten: Genau genommen braucht der Absender statt der Nummer 0 die Fähigkeit `CAP_KILL`, die root hat ([Kapitel 7, Abschnitt 6.4](/wissen/informatik/linux-und-kommandozeile/benutzer-gruppen-und-rechte/kurzzeitig-root-sudo-und-su.html#stufe-6-4)). Und SIGCONT darf ein Prozess jedem Prozess derselben Sitzung schicken, auch ohne passende Nummer. Für den Alltag heißt das: Du darfst deinen eigenen Prozessen Signale schicken, aber nicht denen anderer Benutzer oder des Systems. Ein Versuch mit einem Programm, das als root läuft:

```console
$ sudo sleep 700 &
[1] 689
$ ps -o user,pid,ppid,cmd -C sudo,sleep
USER         PID    PPID CMD
root         689     535 sudo sleep 700
root         691     689 sudo sleep 700
root         692     691 sleep 700
$ kill 692
bash: kill: (692) - Operation not permitted
$ sudo kill 692
$ wait
$ pgrep -a -x sleep
```

`sudo` läuft hier in zwei Prozessen; der zweite startet `sleep 700`, das root gehört. Dein `kill` scheitert mit „Operation not permitted“; erst `sudo kill` darf es, und mit `sleep` endet auch der Job. `wait` wartet, bis er ganz fertig ist (Unterabschnitt [3.6](vordergrund-hintergrund-und-jobs.html#stufe-3-6)), und `pgrep` findet danach kein `sleep` mehr. Abbildung [17](#abb-17) zeigt die Prüfung.

:::abbildung linux/k8wer 17
Links der Absender `kill` mit seinen Benutzernummern real 1000, effektiv 1000; rechts zwei Ziele: oben `sleep 600` des Benutzers student (real 1000, gespeichert 1000), unten `sleep 700` von root (real 0, gespeichert 0). Der Kernel vergleicht: Linien von „real“ und „effektiv“ des Absenders zu „real“ und „gespeichert“ des Ziels. Oben findet eine Linie eine Gleichheit (grün), das Signal geht durch. Unten findet keine eine Gleichheit (rot), es bleibt bei „Operation not permitted“. Zuletzt erscheint ein Absender mit effektiv 0 (sudo kill), und das Signal geht auch unten durch.
:::

⁠**Kurz gesagt:** Signale darfst du deinen eigenen Prozessen schicken; für fremde Prozesse braucht man die Rechte von root.

:::hintergrund Warum die reale und die gespeicherte Nummer des Ziels zählen
Die Regel vergleicht beim Ziel nicht die effektive Benutzernummer. Das hat einen praktischen Grund: Startest du ein SUID-Programm von root, etwa `passwd` oder `sudo`, hat sein Prozess die effektive Nummer 0, aber deine reale Nummer (Unterabschnitt [2.8](prozesse-beobachten.html#stufe-2-8)). Weil die reale Nummer zählt, darfst du ein solches Programm trotzdem beenden, etwa mit Strg+C, wenn du dich vertippt hast. Fremde Benutzer dagegen erreichen es nicht, denn ihre Nummern passen weder zur realen noch zur gespeicherten. Die gespeicherte Nummer spielt nur bei Programmen eine Rolle, die zwischen zwei Benutzernummern wechseln.
:::

:::hintergrund Warum der Prozess 1 besonders geschützt ist
Selbst root kann dem Prozess 1 nicht jedes Signal zustellen: Der Kernel stellt ihm nur Signale zu, für die `systemd` eine eigene Reaktion festgelegt hat; alle anderen verwirft er, auch SIGKILL. Der Grund: Endet der Prozess 1, gibt es keine Wurzel mehr, die Waisen übernimmt, und der Kernel hält das ganze System an. Ein versehentliches Signal soll das nicht auslösen können. `systemd` selbst nutzt einige Signale als Befehle, etwa um neu zu starten. Versuche nie, dem Prozess 1 Signale zu schicken.
:::

### Aufgaben zu Abschnitt [4](#stufe-4)

<span class="anker" id="stufe-4-9"></span>

:::aufgabe Aufgabe 10 ★★ Exit-Status nach Signalen
<span class="anker" id="aufg-10"></span>

Starte im ersten Terminal dreimal `sleep` im Vordergrund und beende es (a) mit Strg+C, (b) aus dem zweiten Terminal mit `kill` und der PID, (c) aus dem zweiten Terminal mit `kill -9`. Lies jedes Mal `echo $?` und erkläre die Zahl.

:::loesung
Im ersten Terminal:

```console
$ sleep 400
^C
$ echo $?
130
$ sleep 401
Terminated                 sleep 401
$ echo $?
143
$ sleep 402
Killed                     sleep 402
$ echo $?
137
```

Im zweiten Terminal, jeweils während `sleep` wartete, mit der PID aus `pgrep sleep`:

```console
$ kill 591
$ kill -9 600
```

(a) Strg+C schickt SIGINT mit der Nummer 2: $128 + 2 = 130$. (b) `kill` ohne Angabe schickt SIGTERM mit der Nummer 15: $128 + 15 = 143$. (c) `kill -9` schickt SIGKILL: $128 + 9 = 137$. In allen drei Fällen hat `sleep` keine eigene Reaktion festgelegt, und die Standardreaktion beendet es.
:::
:::

:::aufgabe Aufgabe 11 ★ Die Signaltabelle lesen
<span class="anker" id="aufg-11"></span>

Beantworte mit Tabelle [1](#tab-1): (a) Welche Signale halten einen Prozess an, und welches davon kann ein Programm nicht abfangen? (b) Welche Signale ignoriert ein Programm, das nichts anderes festgelegt hat? (c) Warum ist es sinnvoll, dass SIGWINCH nicht beendet?

:::loesung
(a) Anhalten können SIGSTOP, SIGTSTP und SIGTTIN. Nicht abfangen lässt sich SIGSTOP. (b) SIGCHLD und SIGWINCH werden standardmäßig ignoriert. (c) Ein Programm, das sich nicht um SIGWINCH kümmert, soll weiterlaufen, wenn jemand das Fenster größer zieht. Nur Programme, die den ganzen Bildschirm füllen, etwa `top` oder `less`, fangen SIGWINCH ab und zeichnen sich in der neuen Größe neu.
:::
:::

:::aufgabe Aufgabe 12 ★★ Vom Status zum Signal
<span class="anker" id="aufg-12"></span>

Welche Signale stecken hinter den Exit-Status 129, 141, 147 und 148? Rechne von Hand und prüfe mit `kill -l`. Bei welchem der vier ist das Programm nicht beendet?

:::loesung
```console
$ kill -l 129 141 147 148
HUP
PIPE
STOP
TSTP
```

$129 - 128 = 1$ (SIGHUP), $141 - 128 = 13$ (SIGPIPE), $147 - 128 = 19$ (SIGSTOP), $148 - 128 = 20$ (SIGTSTP). Bei 147 und 148 ist das Programm nicht beendet, sondern angehalten; es lässt sich mit `fg` oder `bg` fortsetzen.
:::
:::

:::aufgabe Aufgabe 13 ★★★ Ein Programm von root beenden
<span class="anker" id="aufg-13"></span>

Starte `sudo sleep 700 &`. (a) Warum scheitert `kill` an der PID von `sleep 700`? (b) Lies die Zeile `Uid` des `sudo`-Prozesses, der der Elternprozess von `sleep 700` ist. Darfst du ihm nach der Regel aus Unterabschnitt [4.8](#stufe-4-8) ein Signal schicken? (c) Probiere es mit `kill` und seiner PID aus und erkläre, warum danach auch `sleep 700` fort ist.

:::loesung
```console
$ sudo sleep 700 &
[1] 607
$ ps -o user,pid,ppid,cmd -C sudo,sleep
USER         PID    PPID CMD
root         607     540 sudo sleep 700
root         609     607 sudo sleep 700
root         610     609 sleep 700
$ grep Uid /proc/609/status
Uid:    1000    0       0       0
$ kill 610
bash: kill: (610) - Operation not permitted
$ kill 609
$ jobs
[1]+  Terminated                 sudo sleep 700
$ pgrep -a -x sleep
```

(a) `sleep 700` hat die reale und die gespeicherte Benutzernummer 0. Deine Shell hat 1000 als reale und effektive Nummer; keine davon stimmt mit einer der beiden Nummern des Ziels überein, also verweigert der Kernel das Signal. (b) Der `sudo`-Prozess 609 hat die reale Nummer 1000, denn du hast ihn gestartet. Nach der Regel genügt das: Deine reale Nummer ist gleich seiner realen. (c) `kill 609` gelingt. `sudo` leitet ein Signal, das es bekommt, an den Befehl weiter, den es gestartet hat, hier an `sleep 700`; das endet daraufhin, ebenso beide `sudo`-Prozesse. Deshalb meldet die Shell den Job als beendet, und `pgrep` findet kein `sleep` mehr.
:::
:::

:::aufgabe Aufgabe 14 ★★★ Einen Zombie loswerden
<span class="anker" id="aufg-14"></span>

Erzeuge mit `bash -c 'sleep 1 & exec sleep 20' &` einen Zombie wie in Unterabschnitt [2.6](prozesse-beobachten.html#stufe-2-6). Versuche, ihn mit `kill -9` und seiner PID zu beenden, und sieh mit `ps` nach. Was beobachtest du, und warum? Was hilft stattdessen?

:::loesung
```console
$ bash -c 'sleep 1 & exec sleep 20' &
[1] 570
$ ps -o pid,ppid,stat,cmd --ppid $!
    PID    PPID STAT CMD
    571     570 Z    [sleep] <defunct>
$ kill -9 $(ps -o pid= --ppid $!)
$ echo $?
0
$ ps -o pid,ppid,stat,cmd --ppid $!
    PID    PPID STAT CMD
    571     570 Z    [sleep] <defunct>
$ kill $!
$ ps -o pid,ppid,stat,cmd -C sleep
    PID    PPID STAT CMD
[1]+  Terminated                 bash -c 'sleep 1 & exec sleep 20'
```

`--ppid $!` wählt das Kind des Hintergrundjobs, `ps -o pid=` gibt nur seine PID ohne Überschrift aus. `kill -9` meldet Erfolg, aber der Zombie bleibt: Er ist schon beendet, ein Signal ändert an ihm nichts mehr. Was ihn beseitigt, ist ein wait. Sein Elternprozess, das `sleep 20`, ruft aber nie wait auf. Beendet man stattdessen den Elternprozess, wird der Zombie zur Waise, bekommt einen neuen Elternprozess, und der ruft sofort wait auf; danach ist der Zombie verschwunden. Die Meldung `Terminated` gehört zum Job, also zum beendeten `sleep 20`.
:::
:::

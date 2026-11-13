---
title: Programme weiterlaufen lassen: nohup, disown und tmux
pfad: Informatik / Linux und Kommandozeile / Auf entfernten Rechnern arbeiten: SSH, Dateien übertragen, tmux
adresse: informatik/linux-und-kommandozeile/auf-entfernten-rechnern-arbeiten-ssh-dateien-ubertragen-tmux
knoten: Kapitel 11: Auf entfernten Rechnern arbeiten: SSH, Dateien übertragen, tmux
order: 6160700
summary: Eine lange Rechnung auf dem Server soll nicht enden, nur weil das WLAN abbricht oder man das Fenster schließt.
tags: Terminal-Multiplexer, tmux, tmux-Sitzung, Präfixtaste, Fenster, Bereich, trennt, hängt
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Eine lange Rechnung auf dem Server soll nicht enden, nur weil das WLAN abbricht oder man das Fenster schließt. Dieser Abschnitt zeigt, warum sie normalerweise endet, wie `nohup` und `disown` das verhindern und wie der Terminal-Multiplexer `tmux` ganze Shells auf dem Server am Leben hält, so dass man sich später wieder anhängen kann.
:::

:::::vorwissen Was du dafür brauchst: SIGHUP, nohup und disown

<span class="anker" id="stufe-6-1"></span>

Aus [Kapitel 8](/wissen/informatik/linux-und-kommandozeile/prozesse-signale-und-dienste/prozesse-signale-und-dienste.html) brauchst du die Signale und ihre Rolle beim Schließen eines Terminals.

<ul>

<li>

Ein Signal ist eine kurze Nachricht des Kernels an einen Prozess, etwa SIGTERM oder SIGKILL; ohne eigene Reaktion endet der Prozess bei den meisten Signalen ([Kapitel 8, Abschnitte 4.1](/wissen/informatik/linux-und-kommandozeile/prozesse-signale-und-dienste/signale.html#stufe-4-1) und [4.2](/wissen/informatik/linux-und-kommandozeile/prozesse-signale-und-dienste/signale.html#stufe-4-2)).

</li>

<li>

Schließt man ein Terminal, schickt der Kernel der Shell darin das Signal SIGHUP („hang up“, auflegen). Die Shell schickt es an alle ihre Jobs weiter, und Programme, die SIGHUP nicht abfangen, enden ([Kapitel 8, Abschnitt 5.4](/wissen/informatik/linux-und-kommandozeile/prozesse-signale-und-dienste/mit-signalen-arbeiten.html#stufe-5-4)).

</li>

<li>

`nohup befehl &` startet einen Befehl so, dass er SIGHUP ignoriert; seine Ausgabe landet in der Datei `nohup.out`. `disown` nimmt einen schon laufenden Job aus der Jobliste der Shell, so dass sie ihm beim Schließen kein SIGHUP schickt ([Kapitel 8, Abschnitt 5.5](/wissen/informatik/linux-und-kommandozeile/prozesse-signale-und-dienste/mit-signalen-arbeiten.html#stufe-5-5)).

</li>

<li>

`timeout sekunden befehl` beendet einen Befehl nach der genannten Zeit ([Kapitel 8, Abschnitt 5.3](/wissen/informatik/linux-und-kommandozeile/prozesse-signale-und-dienste/mit-signalen-arbeiten.html#stufe-5-3)).

</li>

</ul>

Als lange Rechnung dient in diesem Abschnitt ein kleines Skript ([Kapitel 10, Abschnitt 1.6](/wissen/informatik/linux-und-kommandozeile/shell-skripte/vom-befehl-zum-skript.html#stufe-1-6)), das jede Sekunde einen Schritt weiterzählt, den Schritt ausgibt und den Stand in die Datei `fortschritt.txt` schreibt. Lege es im Übungsverzeichnis mit `nano` an:

```bash zaehler.sh
#!/bin/bash
# zaehler.sh: steht fuer eine lange Rechnung; zaehlt jede Sekunde einen Schritt weiter
n=0
while true; do
    n=$(( n + 1 ))
    echo "Schritt $n"
    echo "$n" > fortschritt.txt
    sleep 1
done
```

::::beispiel Der Zähler auf dem eigenen Rechner
```console
$ chmod +x zaehler.sh
$ timeout 3.5 ./zaehler.sh
Schritt 1
Schritt 2
Schritt 3
Schritt 4
$ cat fortschritt.txt
4
```

In 3,5 Sekunden schafft das Skript vier Schritte, bei 0, 1, 2 und 3 Sekunden; dann beendet `timeout` es. Die Datei hält den letzten Stand fest, auch wenn niemand die Ausgabe sieht.
::::

⁠**Kurz gesagt:** Beim Schließen eines Terminals bekommen Shell und Jobs SIGHUP und enden; `nohup` und `disown` schützen einzelne Programme davor.

:::::

### Was bei einem Verbindungsabbruch geschieht

<span class="anker" id="stufe-6-2"></span>

Jetzt läuft der Zähler auf dem Server. Im ersten Terminal meldest du dich an und startest ihn im Vordergrund:

```console
$ ssh uebung
Welcome to Ubuntu 26.04.1 LTS (GNU/Linux 6.6.87.2-microsoft-standard-WSL2 x86_64)
...
$ cd linuxk11
$ ./zaehler.sh
Schritt 1
Schritt 2
Schritt 3
Schritt 4
```

Nach dem vierten Schritt schließt du das Terminalfenster mit der Maus, während der Zähler läuft. Im zweiten Terminal, auf deinem eigenen Rechner, siehst du nach, ob er weiterzählt:

```console
$ cd ~/linuxk11
$ cat fortschritt.txt
4
$ sleep 3
$ cat fortschritt.txt
4
$ pgrep -f zaehler.sh
$ echo $?
1
```

Der Stand bleibt bei 4, und `pgrep` findet keinen Prozess mehr (Status 1, [Kapitel 8, Abschnitt 2.4](/wissen/informatik/linux-und-kommandozeile/prozesse-signale-und-dienste/prozesse-beobachten.html#stufe-2-4)). Die Rechnung ist mit dem Fenster gestorben, obwohl sie auf dem Server lief.

:::satz Satz 6.1 (Die Kette beim Verbindungsabbruch)
<span class="anker" id="satz-6-1"></span>

Schließt man das Fenster, in dem `ssh` läuft, bekommt der Client `ssh` SIGHUP und beendet die Verbindung. Auf dem Server schließt daraufhin `sshd-session` das Pseudoterminal der Sitzung. Der Kernel schickt der Shell auf dem Server SIGHUP, und diese schickt es an alle ihre Jobs weiter. Alle Jobs, die SIGHUP nicht abfangen oder ignorieren, enden, und mit ihnen die Shell.
:::

Auf dem Server geschieht also dasselbe wie beim Schließen eines Terminals auf dem eigenen Rechner ([Kapitel 8, Abschnitt 5.4](/wissen/informatik/linux-und-kommandozeile/prozesse-signale-und-dienste/mit-signalen-arbeiten.html#stufe-5-4)): Für die Shell dort ist die Verbindung ihr Terminal, und das Pseudoterminal von `sshd-session` hat aufgelegt. Bricht nicht das Fenster, sondern das Netz ab, läuft die Kette genauso, nur später: erst dann, wenn der Server bemerkt, dass die Verbindung tot ist. Abbildung [26](#abb-26) zeigt die Kette.

:::abbildung linux/k11abbruch 26
Die Kette beim Verbindungsabbruch, von links nach rechts. Links das Terminalfenster mit den Schritten des Zählers, darunter `ssh`; das Fenster wird mit dem Kreuz geschlossen (zurück bleibt ein gestrichelter Rahmen). Blitz „SIGHUP“ an `ssh`, `ssh` endet (grau), die Verbindung (Rohr) reißt. Rechts auf dem Server: `sshd-session` schließt `pts/3` (grau); Blitz „SIGHUP“ an `-bash`; von dort Blitz „SIGHUP“ an den Job `./zaehler.sh`; beide werden grau. Unten die Datei `fortschritt.txt`, deren Zahl bis 4 steigt und dort stehen bleibt.
:::

:::hintergrund Wann der Server einen Abbruch bemerkt
Schließt man das Fenster, beendet der Client die Verbindung ordentlich, und der Server erfährt es sofort. Bricht dagegen das WLAN ab oder klappt man den Laptop zu, kommt beim Server keine Nachricht an; aus seiner Sicht ist die Verbindung nur still. Er merkt den Abbruch erst, wenn er etwas schicken will und lange keine Bestätigung kommt, oder wenn eine Prüfnachricht unbeantwortet bleibt. Solche Prüfnachrichten verschickt der Kernel selbst, wenn ein Programm sie für eine Verbindung einschaltet; der SSH-Server tut das mit seiner voreingestellten Einstellung `TCPKeepAlive yes`. Unter Linux schickt der Kernel die erste Prüfnachricht bei einer stillen Verbindung voreingestellt aber erst nach zwei Stunden. Bis dahin laufen die Programme auf dem Server weiter, bleiben aber stehen, sobald sie etwas ausgeben wollen und der Puffer voll ist. Mit der Einstellung `ServerAliveInterval` in `~/.ssh/config` lässt der Client in festen Abständen nachfragen und bemerkt einen Abbruch so selbst schneller; auf dem Server leistet `ClientAliveInterval` dasselbe. Retten kann keine dieser Einstellungen die Programme; sie verkürzen nur die Wartezeit.
:::

⁠**Kurz gesagt:** Endet die Verbindung, schließt der Server das Pseudoterminal der Sitzung; die Shell dort bekommt SIGHUP und reißt ihre Jobs mit.

### nohup und disown über SSH

<span class="anker" id="stufe-6-3"></span>

Die Werkzeuge aus [Kapitel 8](/wissen/informatik/linux-und-kommandozeile/prozesse-signale-und-dienste/prozesse-signale-und-dienste.html) helfen auch hier. Diesmal startest du den Zähler mit `nohup` im Hintergrund und schließt danach das Fenster:

```console
$ ssh uebung
Welcome to Ubuntu 26.04.1 LTS (GNU/Linux 6.6.87.2-microsoft-standard-WSL2 x86_64)
...
$ cd linuxk11
$ nohup ./zaehler.sh &
[1] 2132
nohup: ignoring input and appending output to 'nohup.out'
```

Im zweiten Terminal zählt der Stand weiter, und `pgrep` findet den Prozess:

```console
$ cat fortschritt.txt
4
$ sleep 3
$ cat fortschritt.txt
8
$ pgrep -a -f zaehler.sh
2132 /bin/bash ./zaehler.sh
$ tail -n 2 nohup.out
Schritt 8
Schritt 9
$ pkill -f zaehler.sh
```

Der Zähler hat das SIGHUP überstanden. Seine Ausgabe, die vorher ins Terminal ging, steht jetzt in `nohup.out`. Mit `pkill -f` beendest du ihn am Ende selbst ([Kapitel 8, Abschnitt 5.1](/wissen/informatik/linux-und-kommandozeile/prozesse-signale-und-dienste/mit-signalen-arbeiten.html#stufe-5-1)). Genauso hilft `disown`, wenn das Programm schon läuft (Aufgabe [22](#aufg-22)).

Für eine Rechnung, die einfach durchlaufen soll, genügt das. Es hat aber Grenzen. Man muss sich vorher entscheiden, denn ein Programm, das schon im Vordergrund läuft, bekommt man ohne Anhalten nicht mehr in den Hintergrund. Man sieht seine Ausgaben nur noch in einer Datei und kann nichts mehr eingeben, auch nicht auf eine Rückfrage antworten. Und das Programm läuft ohne Terminal; nach einer neuen Anmeldung gibt es keinen Weg zurück zu dem Bildschirm, den man verlassen hat (Abbildung [27](#abb-27)).

:::abbildung linux/k11nohup 27
Nach dem Abbruch mit `nohup`. Links der geschlossene Fensterrahmen (grau). Rechts auf dem Server die Kette aus Abbildung [26](#abb-26): `-bash` bekommt SIGHUP und schickt es weiter, aber am Job `nohup ./zaehler.sh` prallt der Blitz ab (Schild „SIGHUP wird ignoriert“). Der Zähler läuft weiter, seine Ausgabe fließt in die Datei `nohup.out`, der Stand in `fortschritt.txt` steigt von 4 auf 8. Links darunter eine neue Anmeldung (`ssh uebung`): Sie erreicht nur die Dateien und mit `pkill` den Prozess, nicht aber den alten Bildschirm (durchgestrichener Pfeil).
:::

⁠**Kurz gesagt:** `nohup` und `disown` retten einzelne Programme über einen Verbindungsabbruch, aber ohne Terminal: Man kann ihnen nach einer neuen Anmeldung nur noch über Dateien und Signale folgen.

### Der Terminal-Multiplexer tmux

<span class="anker" id="stufe-6-4"></span>

Was man eigentlich will, ist ein Terminal auf dem Server, das nicht an der Verbindung hängt: Die Shell darin soll weiterlaufen, wenn man geht, und man soll später an genau diesen Bildschirm zurückkehren können, mit allem, was darauf steht.

Ein Bild zur Orientierung: ein Fernsehsender und ein Fernseher. Die Sendung läuft im Studio, ob jemand zusieht oder nicht; schaltet man den Fernseher aus, geht die Sendung weiter, und schaltet man ihn wieder ein, sieht man den aktuellen Stand. Das Bild hat eine Grenze: Bei tmux kann der Zuschauer auch mitspielen, denn seine Tasten gehen ins Studio.

:::definition Definition 6.2 (Terminal-Multiplexer)
<span class="anker" id="satz-6-2"></span>

Ein __Terminal-Multiplexer__ ist ein Programm, das selbst Pseudoterminals öffnet und darin Shells laufen lässt. Bei __tmux__ hält ein Hintergrundprozess, der *tmux-Server*, alle diese Pseudoterminals und die Programme darin. Das Programm `tmux`, das man in einem Terminal startet, ist nur ein *Client*: Es zeigt eines der Pseudoterminals des Servers an und reicht die Tasten dorthin weiter. Endet der Client, laufen der Server und alle Programme darin weiter.
:::

„Multiplexer“ heißt der Name, weil das Programm viele Terminals über ein einziges Fenster zugänglich macht. Der tmux-Server hat mit dem SSH-Server nichts zu tun; er ist ein gewöhnliches Programm, das jeder Benutzer für sich startet, auf dem eigenen Rechner wie auf einem Server. Auf vielen Ubuntu-Systemen ist `tmux` schon installiert, auf dem Testsystem ebenfalls; sonst holt man es mit `sudo apt install tmux`. Abbildung [28](#abb-28) zeigt die Aufteilung.

:::abbildung linux/k11tmuxserver 28
Der tmux-Server. Rechts ein Kasten „tmux-Server (läuft im Hintergrund, kein Terminal)“ mit drei kleinen Bildschirmen darin, jeder mit einem Pseudoterminal (`pts/4`, `pts/5`, `pts/6`) und einer Shell. Links ein Terminalfenster mit dem Client `tmux` daneben; eine Leitung verbindet ihn mit einem der drei Bildschirme, dessen Inhalt im Fenster erscheint. Dann wird das Fenster geschlossen (zurück bleibt ein gestrichelter Rahmen): Client und Leitung verschwinden, aber die drei Bildschirme im Server laufen weiter (ein Zähler auf einem von ihnen zählt hoch). Darunter öffnet sich ein neues Fenster, ein neuer Client verbindet sich mit demselben Bildschirm, der Zählerstand ist weitergelaufen.
:::

⁠**Kurz gesagt:** tmux lässt Shells in Pseudoterminals eines eigenen Hintergrundprozesses laufen; das Terminal, in dem man `tmux` aufruft, zeigt nur eines davon an.

### Die tmux-Sitzung und die Präfixtaste

<span class="anker" id="stufe-6-5"></span>

Bevor es auf den Server geht, lernst du tmux auf deinem eigenen Rechner kennen. Die Arbeit in tmux ist in Sitzungen gegliedert, und gesteuert wird es über eine besondere Taste.

:::definition Definition 6.3 (tmux-Sitzung)
<span class="anker" id="satz-6-3"></span>

Eine __tmux-Sitzung__, kurz Sitzung, ist eine benannte Arbeitsumgebung im tmux-Server, die eine oder mehrere Shells enthält. `tmux new -s name` legt eine Sitzung an und zeigt sie im aktuellen Terminal an; `tmux ls` listet die Sitzungen, `tmux kill-session -t name` beendet eine samt allen Programmen darin.
:::

Das Wort hat hier eine eigene Bedeutung: Die Sitzung einer Shell aus [Kapitel 2, Abschnitt 1.5](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/terminal-und-shell.html#stufe-1-5) endet mit der Shell, eine tmux-Sitzung kann viele Shells enthalten und besteht weiter, bis man sie beendet. Wo Verwechslungen drohen, sagt dieses Kapitel „tmux-Sitzung“. Läuft beim Anlegen noch kein tmux-Server, startet `tmux` ihn dabei selbst; endet die letzte Sitzung, beendet sich auch der Server. Eine Sitzung namens `probe`:

```console
$ tmux new -s probe
```

Das Terminal wird leer, eine neue Shell zeigt ihre Eingabeaufforderung, und am unteren Rand erscheint eine grüne Statuszeile: links der Name der Sitzung in eckigen Klammern, `[probe]`, daneben `0:bash*`, rechts der Titel des Fensters, die Uhrzeit und das Datum, etwa `"labor" 03:43 13-Nov-26`. In dieser Shell arbeitest du wie gewohnt. Tippe zur Probe `echo "Fenster 0"`.

:::definition Definition 6.4 (Präfixtaste)
<span class="anker" id="satz-6-4"></span>

Alle Tastenbefehle an tmux beginnen mit der __Präfixtaste__, voreingestellt Strg+B: Man drückt Strg+B, lässt los und drückt dann eine zweite Taste, die den Befehl wählt. Die Präfixtaste selbst gibt tmux nicht an das Programm weiter; wer Strg+B an das Programm schicken will, drückt sie zweimal.
:::

Ohne Präfixtaste gingen alle Tasten an die Shell und ihre Programme, und tmux könnte keine eigenen Befehle erkennen. Strg+B braucht man im Terminal selten: In der Shell bewegt es nur den Cursor ein Zeichen nach links, was auch die Pfeiltaste kann. Dieses Kapitel schreibt „Strg+B, dann c“ für „Strg+B drücken, loslassen, c drücken“. Die wichtigsten Tasten stehen in Tabelle [2](#tab-2); Strg+B, dann `?` zeigt alle (Ende mit `q`).

<span class="anker" id="tab-2"></span>

**Tabelle 2:** Die wichtigsten Tasten von tmux, jeweils nach Strg+B.

| nach Strg+B | Wirkung |
|---|---|
| `d` | vom Terminal trennen (die Sitzung läuft weiter) |
| `c` | neues Fenster |
| `n`, `p` | nächstes, vorheriges Fenster |
| `0` bis `9` | Fenster mit dieser Nummer |
| `w` | Fenster aus einer Liste wählen |
| `,` | aktuelles Fenster umbenennen |
| `&` | aktuelles Fenster schließen (mit Rückfrage) |
| `%` | Bereich in links und rechts teilen |
| `"` | Bereich in oben und unten teilen |
| `o`, Pfeiltasten | zum nächsten bzw. benachbarten Bereich |
| `z` | aktuellen Bereich auf das ganze Fenster vergrößern und zurück |
| `x` | aktuellen Bereich schließen (mit Rückfrage) |
| `[` | zurückblättern (Ende mit `q`) |
| `?` | alle Tasten anzeigen |

⁠**Kurz gesagt:** `tmux new -s name` legt eine Sitzung an und zeigt sie an; Befehle an tmux beginnen mit Strg+B.

### Das Fenster

<span class="anker" id="stufe-6-6"></span>

In einer Sitzung braucht man oft mehr als eine Shell: in einer läuft die Rechnung, in einer zweiten sieht man sich die Ergebnisse an.

:::definition Definition 6.5 (Fenster)
<span class="anker" id="satz-6-5"></span>

Ein __Fenster__ von tmux ist eine Seite der Sitzung, die das ganze Terminal ausfüllt, ähnlich einem Reiter im Browser. Jede Sitzung hat mindestens ein Fenster; die Fenster sind ab 0 nummeriert, und die Statuszeile zeigt sie alle.
:::

Mit Strg+B, dann `c` („create“) legst du in der Sitzung `probe` ein zweites Fenster an; darin läuft eine eigene, neue Shell. Tippe dort `echo "Fenster 1"`. Die Statuszeile zeigt jetzt `0:bash- 1:bash*`: Nummer und Name jedes Fensters, wobei `*` das angezeigte Fenster markiert und `-` das zuletzt angezeigte. Mit Strg+B, dann `0` kommst du zurück zu Fenster 0 und siehst die Zeile `Fenster 0` noch dort stehen; die Shell darin hat die ganze Zeit gewartet.

::::beispiel Zwei Fenster für eine Rechnung
In Fenster 0 läuft eine lange Rechnung und schreibt ihren Fortschritt. In Fenster 1 siehst du mit `cat fortschritt.txt` nach dem Stand oder liest eine Ergebnisdatei. Mit Strg+B, dann `,` gibst du den Fenstern sprechende Namen wie `rechnung` und `ergebnisse`, die dann in der Statuszeile stehen.
::::

⁠**Kurz gesagt:** Ein Fenster ist eine ganze Bildschirmseite einer Sitzung mit eigener Shell; Strg+B, dann `c` legt eines an, Strg+B mit einer Ziffer wechselt.

### Der Bereich

<span class="anker" id="stufe-6-7"></span>

Manchmal will man zwei Shells gleichzeitig sehen, etwa die Ausgabe der Rechnung und daneben eine Shell für Befehle. Dafür teilt man ein Fenster auf.

:::definition Definition 6.6 (Bereich)
<span class="anker" id="satz-6-6"></span>

Ein __Bereich__ (englisch *pane*) ist ein rechteckiges Stück eines Fensters mit einem eigenen Pseudoterminal und einer eigenen Shell. Strg+B, dann `%` teilt den aktuellen Bereich in einen linken und einen rechten, Strg+B, dann `"` in einen oberen und einen unteren. Die Tasten gehen immer an den aktuellen Bereich.
:::

Teilst du in Fenster 1 zuerst mit `%` und dann den neuen rechten Bereich mit `"`, hat das Fenster drei Bereiche. Bei einem Terminal mit 72 Spalten und 24 Zeilen ist der linke 36 Spalten breit und 23 Zeilen hoch, die beiden rechten sind je 35 Spalten breit und 11 Zeilen hoch; die übrigen Spalten und Zeilen nehmen die Trennlinien und die Statuszeile ein. Mit Strg+B, dann `o` oder einer Pfeiltaste wechselst du zwischen den Bereichen, Strg+B, dann `z` vergrößert einen Bereich vorübergehend auf das ganze Fenster. Die Hierarchie aus Sitzung, Fenster und Bereich zeigt Abbildung [29](#abb-29).

:::abbildung linux/k11hierarchie 29
Sitzung > Fenster > Bereich, am Beispiel der Sitzung `probe`. Außen ein Rahmen „Sitzung probe“. Darin zwei Karteikarten nebeneinander: „Fenster 0“ mit einem einzigen Bereich (Shell, Zeile `Fenster 0`) und „Fenster 1“ mit drei Bereichen: links einer mit 36×23 Zeichen (Zeile `Fenster 1`), rechts oben und rechts unten je einer mit 35×11. Jeder Bereich trägt sein Pseudoterminal (`pts/4` für Fenster 0, `pts/5`, `pts/6`, `pts/7` für die drei Bereiche) und eine Shell `bash`. Unten die grüne Statuszeile `[probe] 0:bash- 1:bash*` … `"labor" 03:43 13-Nov-26`. Nacheinander erscheinen die Ebenen mit den Tasten, die sie erzeugen: `tmux new -s probe`, Strg+B c, Strg+B %, Strg+B `"`.
:::

⁠**Kurz gesagt:** Ein Bereich ist ein Teil eines Fensters mit eigener Shell; die Hierarchie lautet Sitzung > Fenster > Bereich.

### Trennen und wieder anhängen

<span class="anker" id="stufe-6-8"></span>

Jetzt kommt die Eigenschaft, um die es eigentlich geht: Man kann eine Sitzung verlassen, ohne sie zu beenden.

:::definition Definition 6.7 (Trennen und anhängen)
<span class="anker" id="satz-6-7"></span>

Strg+B, dann `d` („detach“) __trennt__ den Client von der Sitzung: Der Client endet, das Terminal zeigt wieder die Shell, aus der man `tmux` gestartet hat, und die Sitzung läuft im tmux-Server weiter. `tmux attach -t name` __hängt__ einen neuen Client an die Sitzung *an* und zeigt sie im aktuellen Terminal so, wie sie gerade ist.
:::

Nach Strg+B, dann `d` meldet tmux, von welcher Sitzung es sich getrennt hat, und `tmux ls` zeigt, dass sie noch existiert, mit ihren zwei Fenstern:

```console
[detached (from session probe)]
$ tmux ls
probe: 2 windows (created Fri Nov 13 03:43:18 2026)
```

Danach hängst du dich wieder an, wechselst mit Strg+B, dann `0` in Fenster 0, findest dort die Zeile `Fenster 0` vor, trennst dich erneut und beendest die Übungssitzung:

```console
$ tmux attach -t probe
[detached (from session probe)]
$ tmux kill-session -t probe
```

Weil `probe` die einzige Sitzung war, endet mit ihr auch der tmux-Server. Hängen mehrere Clients an derselben Sitzung, etwa aus zwei Terminals, sehen alle dasselbe; so kann man jemandem über die Schulter schauen lassen.

⁠**Kurz gesagt:** Strg+B, dann `d` trennt das Terminal von der Sitzung, die weiterläuft; `tmux attach -t name` holt sie zurück.

### Warum tmux Programme am Leben hält

<span class="anker" id="stufe-6-9"></span>

Dass die Sitzung das Trennen übersteht, ist kein Zufall, sondern folgt aus der Frage, wer an welchem Terminal hängt. Während die Sitzung `probe` noch lief, zeigte `ps` aus einem zweiten Terminal den tmux-Server und seine Kinder; `pgrep -x` findet die Prozessnummer des Servers an seinem Namen ([Kapitel 8, Abschnitt 2.4](/wissen/informatik/linux-und-kommandozeile/prozesse-signale-und-dienste/prozesse-beobachten.html#stufe-2-4)):

```console
$ ps -o pid,ppid,tty,comm -p $(pgrep -x 'tmux: server')
    PID    PPID TT       COMMAND
   2188     318 ?        tmux: server
$ ps -o pid,ppid,tty,comm --ppid $(pgrep -x 'tmux: server')
    PID    PPID TT       COMMAND
   2189    2188 pts/4    bash
   2230    2188 pts/5    bash
   2270    2188 pts/6    bash
   2301    2188 pts/7    bash
```

Der Server hat kein steuerndes Terminal (`?`, [Kapitel 8, Abschnitt 2.1](/wissen/informatik/linux-und-kommandozeile/prozesse-signale-und-dienste/prozesse-beobachten.html#stufe-2-1)), und sein Elternprozess ist nicht die Shell, in der `tmux new` getippt wurde. Seine vier Kinder sind die Shells der vier Bereiche, jede an einem eigenen Pseudoterminal `pts/4` bis `pts/7`, das der Server geöffnet hat.

:::satz Satz 6.8 (Warum Programme in tmux das Trennen überstehen)
<span class="anker" id="satz-6-8"></span>

Die Programme in tmux hängen an Pseudoterminals des tmux-Servers, nicht an dem Terminal, in dem man arbeitet. Schließt man dieses Terminal oder bricht die Verbindung ab, betrifft das Auflegen nur das Terminal des Clients: Der Client bekommt SIGHUP und endet, der Server und die Shells in seinen Pseudoterminals bekommen kein Signal.
:::

:::hintergrund Wie sich der tmux-Server vom Terminal löst
Wenn `tmux new` den Server startet, löst sich der Server sofort von allem, was ihn mit dem Terminal verbindet. Er gibt das steuernde Terminal auf, das er vom Client geerbt hätte, und sein Elternprozess endet gleich nach dem Start, so dass ihn ein Prozess des Systems als Kind übernimmt ([Kapitel 8, Abschnitt 5.5](/wissen/informatik/linux-und-kommandozeile/prozesse-signale-und-dienste/mit-signalen-arbeiten.html#stufe-5-5)); deshalb die fremde Nummer in der Spalte `PPID`. Legt ein Terminal auf, trifft das nach den Regeln des Kernels nur die Prozesse, für die dieses Terminal das steuernde ist ([Kapitel 8, Abschnitt 5.4](/wissen/informatik/linux-und-kommandozeile/prozesse-signale-und-dienste/mit-signalen-arbeiten.html#stufe-5-4)), also hier nur den Client. Für jeden Bereich öffnet der Server ein eigenes Pseudoterminal, dessen eine Seite er selbst hält; die Shell im Bereich hängt an der anderen Seite. Solange der Server läuft, legt an diesen Pseudoterminals niemand auf. Das ist derselbe Mechanismus, mit dem `sshd-session` für eine SSH-Anmeldung ein Pseudoterminal bereitstellt (Abschnitt [3.6](anmelden-mit-einem-schlusselpaar.html#stufe-3-6)), nur dass der tmux-Server nicht endet, wenn die Verbindung endet. Eine Grenze gibt es: systemd lässt sich so einstellen, dass beim Abmelden alle Prozesse eines Benutzers enden, auch der tmux-Server (Einstellung `KillUserProcesses=yes` in `/etc/systemd/logind.conf`). Ubuntu lässt die Voreinstellung `no` stehen; auf anderen Systemen fragt man nach, bevor man sich auf tmux verlässt.
:::

⁠**Kurz gesagt:** tmux schützt Programme, weil sie an Pseudoterminals des tmux-Servers hängen; legt das Terminal des Clients auf, trifft das nur den Client.

### tmux über SSH: eine Rechnung übersteht den Abbruch

<span class="anker" id="stufe-6-10"></span>

Jetzt alles zusammen. Im ersten Terminal meldest du dich am Server an, startest dort eine tmux-Sitzung `rechnung` und darin den Zähler:

```console
$ ssh uebung
Welcome to Ubuntu 26.04.1 LTS (GNU/Linux 6.6.87.2-microsoft-standard-WSL2 x86_64)
...
$ cd linuxk11
$ tmux new -s rechnung
```

In der neuen Sitzung tippst du `./zaehler.sh`, und die Schritte laufen über den Bildschirm. Dann schließt du das Fenster, wie in Abschnitt [6.2](#stufe-6-2). Im zweiten Terminal meldest du dich neu an und siehst nach:

```console
$ ssh uebung
Welcome to Ubuntu 26.04.1 LTS (GNU/Linux 6.6.87.2-microsoft-standard-WSL2 x86_64)
...
$ tmux ls
rechnung: 1 windows (created Fri Nov 13 03:43:51 2026)
$ tmux attach -t rechnung
[detached (from session rechnung)]
$ cat linuxk11/fortschritt.txt
19
$ sleep 2
$ cat linuxk11/fortschritt.txt
22
$ exit
logout
Connection to localhost closed.
```

Die Sitzung `rechnung` existiert noch. Nach `tmux attach` steht der Bildschirm so da, wie du ihn verlassen hast, nur ist der Zähler inzwischen weitergelaufen (Abbildung [30](#abb-30)). Mit Strg+B, dann `d` trennst du dich wieder; der Stand in `fortschritt.txt` steigt weiter, auch nachdem du dich abgemeldet hast. Erst `tmux kill-server` beendet alle Sitzungen und damit den Zähler:

```console
$ tmux kill-server
$ pgrep -f zaehler.sh
$ echo $?
1
```

:::satz Satz 6.9 (tmux gehört auf den Server)
<span class="anker" id="satz-6-9"></span>

Damit Programme auf dem Server einen Verbindungsabbruch überstehen, muss tmux auf dem Server laufen: zuerst `ssh`, dann in der Shell auf dem Server `tmux new` oder `tmux attach`.
:::

Startet man umgekehrt tmux auf dem eigenen Rechner und darin `ssh`, schützt tmux nur den Client `ssh` vor dem Schließen des Fensters. Bricht dagegen das Netz ab, endet die Verbindung trotzdem, und auf dem Server reißt die Kette aus Abschnitt [6.2](#stufe-6-2) die Programme mit. Eine bewährte Gewohnheit: Nach jeder Anmeldung auf einem Server, auf dem man länger arbeitet, zuerst `tmux attach` versuchen und, falls es noch keine Sitzung gibt, `tmux new -s name` aufrufen.

:::abbildung linux/k11tmuxssh 30
Terminalbild (dunkel, wie Ubuntu) einer tmux-Sitzung auf dem Server nach dem Wiederanhängen: oben die Zeilen aus der echten Mitschrift, `student@labor:~/linuxk11$ ./zaehler.sh`, dann `Schritt 1` bis `Schritt 6` und weiter fortlaufend; unten die grüne Statuszeile `[rechnung] 0:bash*` … `"labor"` mit Uhrzeit und Datum. Darunter eine Zeitleiste, die mitläuft: „Fenster geschlossen“ (Kreuz; das Bild wird blass), „neue Anmeldung“, `tmux attach -t rechnung` (das Bild ist wieder da). Ein grüner Balken zeigt: Der Zähler lief über die ganze Zeitleiste ohne Unterbrechung, bis `Schritt 18`.
:::

⁠**Kurz gesagt:** Eine tmux-Sitzung auf dem Server übersteht das Schließen des Fensters und Verbindungsabbrüche; nach einer neuen Anmeldung holt `tmux attach` sie zurück.

### Aufräumen

<span class="anker" id="stufe-6-11"></span>

Zum Schluss entfernst du, was die Übungen angelegt haben. Zuerst die Einträge in `~/.ssh`. `ssh-keygen -R localhost` löscht alle Hostschlüssel von `localhost` aus `known_hosts`, es sind drei. Ob in `authorized_keys` noch etwas anderes steht als dein Übungsschlüssel, prüft `grep`: `-F` sucht feste Zeichenketten, `-x` nur ganze Zeilen, `-f datei` nimmt die Suchtexte aus einer Datei, und `-v` mit `-c` zählt die Zeilen, die *nicht* passen ([Kapitel 6, Abschnitte 5.2](/wissen/informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke/suchen-mit-grep.html#stufe-5-2) und [6.3](/wissen/informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke/regulare-ausdrucke-zeichen-klassen-und-anker.html#stufe-6-3)). Ist das Ergebnis 0, stand nur der Übungsschlüssel darin, und du löschst die Datei; sonst entfernst du nur seine Zeile mit `nano` und lässt die Datei im `rm`-Befehl unten weg. Ebenso mit `~/.ssh/config`: Hattest du die Datei schon vor diesem Kapitel, löschst du nur den Abschnitt `Host uebung` und lässt sie im `rm`-Befehl weg.

```console
$ cd ~/linuxk11
$ ssh-keygen -R localhost
```

```text
# Host localhost found: line 1
# Host localhost found: line 2
# Host localhost found: line 3
/home/student/.ssh/known_hosts updated.
Original contents retained as /home/student/.ssh/known_hosts.old
```

```console
$ grep -c -v -x -F -f uebungsschluessel.pub ~/.ssh/authorized_keys
0
$ rm ~/.ssh/authorized_keys ~/.ssh/config ~/.ssh/known_hosts.old
$ ls -lA ~/.ssh
total 4
drwx------ 2 student student 4096 Nov 13 03:43 agent
-rw------- 1 student student    0 Nov 13 03:44 known_hosts
$ cd
$ rm -r ~/linuxk11
```

Übrig bleiben die jetzt leere `known_hosts` und das leere Verzeichnis `agent`; beide schaden nicht und werden beim nächsten Gebrauch von `ssh` wieder benutzt. Die letzten beiden Befehle entfernen das Übungsverzeichnis samt Schlüsselpaar.

Den Übungsserver entfernst du, wenn du ihn wie in Abschnitt [1.5](entfernte-anmeldung-client-server-und-ein-ubungsserver.html#stufe-1-5) nur für dieses Kapitel installiert hast, in drei Schritten: die eigene Einstellungsdatei löschen, das Paket samt seinen Einstellungen und Hostschlüsseln mit `purge` entfernen und die Pakete, die nur für den Server mitkamen, mit `autoremove` ([Kapitel 9, Abschnitt 6.5](/wissen/informatik/linux-und-kommandozeile/software-installieren-paketverwaltung/installieren-entfernen-aktualisieren.html#stufe-6-5)):

```console
$ sudo rm /etc/ssh/sshd_config.d/10-linuxk11.conf
$ sudo apt purge openssh-server
The following packages were automatically installed and are no longer required:
  libwrap0  openssh-sftp-server
Use 'sudo apt autoremove' to remove them.

REMOVING:
  openssh-server*
...
Continue? [Y/n] Y
...
Purging configuration files for openssh-server (1:10.2p1-2ubuntu3.8) ...

$ sudo apt autoremove --purge
REMOVING:
  libwrap0*  openssh-sftp-server*
...
$ systemctl status ssh.socket --no-pager
Unit ssh.socket could not be found.
```

Mit dem Paket verschwinden die Hostschlüssel, `sshd_config`, die Units und das Systemkonto `sshd`. Zwei Pakete, die bei der Installation als Empfehlungen mitkamen, `ncurses-term` und `ssh-import-id`, entfernt `autoremove` auf dem Testsystem nicht, weil andere installierte Pakete sie empfehlen ([Kapitel 9, Abschnitt 1.6](/wissen/informatik/linux-und-kommandozeile/software-installieren-paketverwaltung/pakete-und-ihre-beziehungen.html#stufe-1-6)); wer den Stand von vorher genau wiederhaben will, entfernt sie mit `sudo apt purge ncurses-term ssh-import-id`. Hat apt bei der Installation den Client `openssh-client` aktualisiert, bleibt er in der neueren Version; auf dem Testsystem war das ein Sicherheitsupdate, das die automatischen Sicherheitsupdates ohnehin eingespielt hätten ([Kapitel 9, Abschnitte 8.1](/wissen/informatik/linux-und-kommandozeile/software-installieren-paketverwaltung/aktualisieren-als-schutz.html#stufe-8-1) und [8.4](/wissen/informatik/linux-und-kommandozeile/software-installieren-paketverwaltung/aktualisieren-als-schutz.html#stufe-8-4)).

**Zum Weiterüben.** Auf der Plattform OverTheWire ([https://overthewire.org/wargames/bandit/](https://overthewire.org/wargames/bandit/)) beginnt das Übungsspiel *Bandit* mit einer Anmeldung per SSH: Level 0 verlangt nur, sich als Benutzer `bandit0` am Rechner `bandit.labs.overthewire.org` anzumelden, und zwar am Port 2220 statt 22. Das Passwort für Level 0 steht auf der Seite des Levels; die Regeln der Plattform verbieten, Passwörter späterer Level oder Lösungen zu veröffentlichen, und dieses Kapitel nennt deshalb keine. Hinweise, wie man dorthin kommt, geben Aufgabe [24](#aufg-24) und ihre Lösung. Auf pwn.college übt das Modul *Terminal Multiplexing* des *Linux Luminarium* ([https://pwn.college/linux-luminarium/](https://pwn.college/linux-luminarium/)) das Trennen und Anhängen mit tmux und mit dem älteren Programm `screen`; für die Anmeldung per SSH hinterlegt man dort seinen öffentlichen Schlüssel in den Einstellungen des Kontos.

:::aufgabe Aufgabe 20 ★ Was überlebt?
<span class="anker" id="aufg-20"></span>

Auf dem Server läuft jeweils ein Programm, dann schließt du das Fenster mit `ssh`. Welches läuft weiter? (a) im Vordergrund gestartet, (b) mit `&` im Hintergrund gestartet, (c) mit `nohup … &` gestartet, (d) mit `&` gestartet und danach `disown`, (e) in einer tmux-Sitzung auf dem Server gestartet, (f) im Vordergrund gestartet, aber `ssh` lief in einer tmux-Sitzung auf dem eigenen Rechner, und statt des Fensters bricht das WLAN ab.

:::loesung
(a) Endet: Es ist der Job im Vordergrund und bekommt das SIGHUP, das die Shell auf dem Server weitergibt (Abschnitt [6.2](#stufe-6-2)). (b) Endet ebenfalls: Die Shell schickt SIGHUP an alle ihre Jobs, auch an die im Hintergrund. (c) Läuft weiter: `nohup` hat SIGHUP für das Programm abgeschaltet. (d) Läuft weiter: Nach `disown` steht es nicht mehr in der Jobliste, die Shell schickt ihm kein SIGHUP. (e) Läuft weiter: Es hängt an einem Pseudoterminal des tmux-Servers; der Abbruch trifft nur den tmux-Client (Abschnitt [6.9](#stufe-6-9)). (f) Endet, nur später: Die lokale tmux-Sitzung hält zwar den Client `ssh` am Leben, doch ohne Netz ist die Verbindung tot. Sobald der Server das bemerkt, schließt er das Pseudoterminal der Sitzung, und die Kette läuft wie in (a).
:::
:::

:::aufgabe Aufgabe 21 ★★ Eine Sitzung mit zwei Fenstern
<span class="anker" id="aufg-21"></span>

Lege auf deinem Rechner eine tmux-Sitzung `uebung` an, erzeuge ein zweites Fenster und teile es in einen oberen und einen unteren Bereich. Trenne dich, liste die Sitzungen und mit `tmux list-windows -t uebung` die Fenster. Erkläre die Angaben in der Ausgabe und beende die Sitzung.

:::loesung
`tmux new -s uebung` legt die Sitzung an, Strg+B, dann `c` erzeugt Fenster 1, Strg+B, dann `"` teilt es in oben und unten, Strg+B, dann `d` trennt:

```console
$ tmux new -s uebung
$ tmux ls
uebung: 2 windows (created Fri Nov 13 03:33:08 2026)
$ tmux list-windows -t uebung
0: bash- (1 panes) [72x23] [layout af1d,72x23,0,0,0] @0
1: bash* (2 panes) [72x23] [layout d4c6,72x23,0,0[72x11,0,0,1,72x11,0,12,2]] @1 (active)
$ tmux kill-session -t uebung
```

Jede Zeile von `tmux list-windows` beschreibt ein Fenster: Nummer und Name (`bash`, nach dem Programm im aktuellen Bereich), die Markierung `-` für das zuletzt und `*` für das gerade angezeigte Fenster, die Zahl der Bereiche, die Größe in Spalten und Zeilen (72×23, die 24. Zeile ist die Statuszeile) und die Aufteilung (*layout*): Fenster 1 besteht aus zwei Bereichen von je 72×11 Zeichen untereinander, der zweite beginnt in Zeile 12 (gezählt ab 0), dazwischen liegt eine Trennlinie. `@0` und `@1` sind die inneren Kennungen der Fenster, `(active)` markiert das aktive. Mit `kill-session` endet die einzige Sitzung und damit auch der tmux-Server.
:::
:::

:::aufgabe Aufgabe 22 ★★ disown nachträglich
<span class="anker" id="aufg-22"></span>

Melde dich am Übungsserver an, starte den Zähler mit `./zaehler.sh > /dev/null &` im Hintergrund, ohne `nohup`, und nimm ihn mit `disown` aus der Jobliste. Schließe das Fenster und prüfe im zweiten Terminal, ob er weiterzählt. Wozu ist hier die Umleitung nach `/dev/null` gut? Beende den Zähler danach.

:::loesung
```console
$ ssh uebung
Welcome to Ubuntu 26.04.1 LTS (GNU/Linux 6.6.87.2-microsoft-standard-WSL2 x86_64)
...
$ cd linuxk11
$ ./zaehler.sh > /dev/null &
[1] 3601
$ disown
$ jobs
```

`jobs` zeigt nichts mehr, der Zähler steht nicht mehr in der Jobliste. Nach dem Schließen des Fensters im zweiten Terminal:

```console
$ cd ~/linuxk11
$ cat fortschritt.txt
7
$ sleep 2
$ cat fortschritt.txt
10
$ pkill -f zaehler.sh
$ pgrep -f zaehler.sh
$ echo $?
1
```

Der Zähler hat überlebt, weil die Shell auf dem Server ihm beim Auflegen kein SIGHUP geschickt hat. Ohne Umleitung wäre seine Standardausgabe das Pseudoterminal der SSH-Sitzung. Nach dem Abbruch gibt es dieses Terminal nicht mehr, und jeder Versuch, darauf zu schreiben, scheitert mit einem Fehler. Der Zähler selbst übersteht das, denn `echo` meldet den Fehler, und das Skript macht weiter; ein Versuch auf dem Testsystem ohne Umleitung zeigte das. Seine Ausgabe wäre aber verloren, und ein Programm, das bei einem Schreibfehler abbricht, würde enden. Mit der Umleitung ist beides ausgeschlossen. `nohup` nimmt einem diese Überlegung ab, indem es die Ausgabe in `nohup.out` umleitet.
:::
:::

:::aufgabe Aufgabe 23 ★★★ Hier oder dort?
<span class="anker" id="aufg-23"></span>

Begründe mit der Kette aus Abschnitt [6.2](#stufe-6-2) und dem Satz aus Abschnitt [6.9](#stufe-6-9), warum tmux auf dem Server laufen muss und nicht auf dem eigenen Rechner. Gibt es einen Fall, in dem tmux auf dem eigenen Rechner trotzdem nützt?

:::loesung
Nach der Kette in Abschnitt [6.2](#stufe-6-2) sterben die Programme auf dem Server, weil die Shell *dort* SIGHUP bekommt, sobald die Verbindung endet. Läuft tmux auf dem eigenen Rechner und darin `ssh`, schützt tmux den Client `ssh` vor dem Schließen des Fensters, aber nicht die Verbindung vor einem Abbruch des Netzes oder vor dem Zuklappen des Laptops. Endet die Verbindung, gibt es auf dem Server nichts, was die Programme hält. Läuft tmux dagegen auf dem Server, hängen die Programme an Pseudoterminals des tmux-Servers dort (Satz in Abschnitt [6.9](#stufe-6-9)); die Verbindung trägt nur den Client, und ihr Ende trifft nur ihn. Auf dem eigenen Rechner nützt tmux trotzdem: für lokale Programme, die das Schließen eines Fensters überstehen sollen, für Fenster und Bereiche als Arbeitsfläche und, um mehrere SSH-Verbindungen in einem einzigen Terminal geordnet nebeneinander zu haben.
:::
:::

:::aufgabe Aufgabe 24 ★ Bandit Level 0
<span class="anker" id="aufg-24"></span>

Melde dich bei OverTheWire Bandit für Level 0 an (Link oben) und lies dort die Aufgabe für den nächsten Level. Welche Angaben aus der Beschreibung des Levels brauchst du für den Befehl `ssh`, und welche Option setzt den Port? Lege für den Rechner einen Eintrag in `~/.ssh/config` an. Denke an die erste Verbindung: Woran erkennst du, ob der Fingerabdruck stimmt?

:::loesung
Hier stehen bewusst nur Hinweise, keine Lösung und kein Passwort; die Regeln von OverTheWire verbieten, sie zu veröffentlichen.

<ul>

<li>

Hinweis 1: Die Seite zu Level 0 nennt Rechner, Port, Benutzername und das Passwort für diesen ersten Level. Der Benutzername steht vor dem `@`, wie in Abschnitt [3.5](anmelden-mit-einem-schlusselpaar.html#stufe-3-5).

</li>

<li>

Hinweis 2: Den Port setzt bei `ssh` die Option `-p` (klein), bei `scp` `-P` (groß). In `~/.ssh/config` gehören die Angaben in einen Abschnitt mit eigenem `Host`-Namen, mit `HostName`, `User` und `Port` wie beim Übungsserver; `IdentityFile` entfällt, weil Bandit Passwörter benutzt.

</li>

<li>

Hinweis 3: Bei der ersten Verbindung fragt `ssh` nach dem Fingerabdruck. Vergleiche ihn mit einer Angabe, die du auf einem anderen Weg bekommst, etwa von der Webseite der Plattform; steht dort keine, ist dir zumindest bewusst, dass du hier einem ersten Kontakt vertraust.

</li>

<li>

Hinweis 4: Die Aufgabe für den nächsten Level steht ebenfalls auf der Webseite; was du dafür brauchst, sind Befehle aus [Kapitel 3](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-verzeichnisse-und-pfade.html).

</li>

</ul>
:::
:::

---
title: Last und Priorität
pfad: Informatik / Linux und Kommandozeile / Prozesse, Signale und Dienste
adresse: informatik/linux-und-kommandozeile/prozesse-signale-und-dienste
knoten: Kapitel 8: Prozesse, Signale und Dienste
order: 6130700
summary: Kapitel 2 hat die Last als Zahl in der Ausgabe von uptime vorgestellt.
tags: Last, Nice-Wert
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
[Kapitel 2](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/die-shell-erste-befehle.html) hat die Last als Zahl in der Ausgabe von `uptime` vorgestellt. Mit den Zuständen aus Abschnitt [2](prozesse-beobachten.html#stufe-2) und dem Planer aus Unterabschnitt [1.3](prozesse-und-ihre-verwandtschaft.html#stufe-1-3) lässt sich jetzt genau sagen, was sie misst und wie sie sich mit der Zeit ändert. Danach geht es um die andere Seite: wie man einem Prozess weniger oder mehr Rechenzeit zuteilen lässt.
:::

### Die Last, genauer

<span class="anker" id="stufe-6-1"></span>

`uptime` zeigt drei Zahlen für die letzten 1, 5 und 15 Minuten ([Kapitel 2, Abschnitt 6.3](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/das-system-erkunden.html#stufe-6-3)). Was genau zählt der Kernel dafür, und warum reagieren die drei Zahlen verschieden schnell?

:::definition Definition 6.1 (Last)
<span class="anker" id="satz-6-1"></span>

Die __Last__ ist die Zahl der Prozesse, genauer der Ausführungsstränge, im Zustand R oder D, also der Prozesse, die gerade rechnen, auf einen Kern warten oder auf ein Gerät warten. Der Kernel zählt sie alle fünf Sekunden und bildet daraus drei gleitende Mittelwerte: einen, in dem die letzte Minute am stärksten zählt, einen für fünf und einen für 15 Minuten.
:::

Die drei Werte stehen auch in der Datei `/proc/loadavg`:

```console
$ cat /proc/loadavg
0.03 0.05 0.02 2/274 753
$ uptime
 15:27:37 up 3 min,  1 user,  load average: 0.03, 0.05, 0.02
```

Hinter den drei Mittelwerten zeigt die Datei die Zahl der Ausführungsstränge, die gerade rechnen können, und die Zahl aller, hier 2 von 274, und zuletzt die PID, die der Kernel zuletzt vergeben hat. Die Last enthält keine Angabe über die Zahl der Kerne: Eine Last von 2 lastet einen Rechner mit zwei Kernen voll aus, einen mit 14 Kernen zu einem Siebtel.

::::beispiel Vier Prozesse rechnen eine Minute lang
Vier `yes` rechnen im Hintergrund, jedes mit einer Zeitgrenze von 60 Sekunden; nach etwa 30 und nach 61 Sekunden zeigt `uptime` die Last:

```console
$ timeout 60 yes > /dev/null &
[1] 755
$ timeout 60 yes > /dev/null &
[2] 757
$ timeout 60 yes > /dev/null &
[3] 759
$ timeout 60 yes > /dev/null &
[4] 761
$ uptime
 15:28:09 up 3 min,  1 user,  load average: 1.60, 0.43, 0.14
$ uptime
 15:28:41 up 4 min,  1 user,  load average: 2.54, 0.77, 0.27
[1]   Exit 124                   timeout 60 yes > /dev/null
[2]   Exit 124                   timeout 60 yes > /dev/null
[3]-  Exit 124                   timeout 60 yes > /dev/null
[4]+  Exit 124                   timeout 60 yes > /dev/null
$ wait
```

Obwohl die ganze Minute lang genau vier Prozesse rechneten, steht der Wert für eine Minute nach 61 Sekunden erst bei 2,54, nicht bei 4. Die Werte für 5 und 15 Minuten steigen noch langsamer. Die vier Jobs enden mit dem Status 124 von `timeout`. Abbildung [22](#abb-22) zeigt den Verlauf.

:::abbildung linux/k8last 22
Ein Diagramm: waagrecht die Zeit von 0 bis 4 Minuten, senkrecht die Last von 0 bis 4. Eine graue Treppe zeigt die wirkliche Zahl rechnender Prozesse: 0, ab 0 s für 60 s auf 4, danach wieder 0. Ein Zeiger läuft über die Zeitachse; mit ihm wachsen drei Kurven: der 1-Minuten-Wert steigt schnell gegen 4 und fällt nach dem Ende ebenso schnell, der 5- und der 15-Minuten-Wert steigen und fallen träge. Bei 30 s und 61 s leuchten die gemessenen Punkte 1,60 und 2,54 auf; sie liegen auf der 1-Minuten-Kurve. Eine waagrechte Linie bei 14 markiert die Zahl der Kerne (am oberen Rand angedeutet).
:::
::::

Warum steigt der Wert so langsam? Der Kernel mittelt nicht einfach über die letzte Minute. Alle fünf Sekunden schiebt er den alten Wert ein Stück in Richtung der aktuellen Zahl $n$ der Prozesse in R und D:

$$L_{\text{neu}} = L_{\text{alt}} \cdot \mathrm{e}^{-5/60} + n \cdot \left(1 - \mathrm{e}^{-5/60}\right).$$

Dabei ist $\mathrm{e}^{-5/60} \approx 0{,}920$; der alte Wert behält also 92 Prozent seines Gewichts, die neue Zählung bekommt 8 Prozent. Für den 5- und den 15-Minuten-Wert steht statt 60 die Zahl 300 bzw. 900 im Exponenten; sie folgen deshalb noch langsamer. Rechnen $n$ Prozesse ab dem Zeitpunkt null dauernd, wächst der 1-Minuten-Wert nach $t$ Sekunden auf

$$L(t) = n \cdot \left(1 - \mathrm{e}^{-t/60}\right).$$

Nach einer Minute ist das $n \cdot (1 - \mathrm{e}^{-1}) \approx 0{,}63 \cdot n$. Hört die Last auf, fällt der Wert umgekehrt in jeder Minute auf etwa 37 Prozent.

::::beispiel [Rechenbeispiel] Die Messung nachrechnen
Mit $n = 4$ und einer Last von fast null zu Beginn ergibt die Formel nach 30 und nach 60 Sekunden die gemessenen Werte. Abbildung [23](#abb-23) führt die Rechnung aus.

:::abbildung linux/k8lastrechnung 23
Rechenbild in zwei Blöcken. Oben: $L(30\,\mathrm{s}) = 4 \cdot (1 - \mathrm{e}^{-30/60}) = 4 \cdot (1 - 0{,}607) = 4 \cdot 0{,}393 = 1{,}57$; daneben der gemessene Wert 1,60. Unten: $L(60\,\mathrm{s}) = 4 \cdot (1 - \mathrm{e}^{-1}) = 4 \cdot (1 - 0{,}368) = 4 \cdot 0{,}632 = 2{,}53$; daneben der gemessene Wert 2,54. Zeile für Zeile eingeblendet.
:::

Die kleinen Unterschiede kommen daher, dass die Last zu Beginn nicht ganz null war und die Messungen nicht genau bei 30 und 60 Sekunden lagen.
::::

⁠**Kurz gesagt:** Die Last ist die Zahl der Prozesse in R oder D, gleitend gemittelt über etwa 1, 5 und 15 Minuten; man vergleicht sie mit der Zahl der Kerne.

:::hintergrund Warum auch wartende Prozesse in D zählen
Ein Prozess im Zustand D rechnet nicht, er wartet auf ein Gerät. Trotzdem zählt Linux ihn zur Last, anders als einige andere Unix-Systeme. Die Last misst damit, wie viel Arbeit sich staut, nicht nur, wie beschäftigt die Kerne sind. Eine hohe Last bei untätigen Kernen deutet deshalb oft auf einen langsamen oder überlasteten Datenträger hin; `top` zeigt das in der Zeile `%Cpu(s)` als hohen Wert bei `wa`.
:::

### Die Priorität: der Nice-Wert

<span class="anker" id="stufe-6-2"></span>

Wollen mehr Prozesse rechnen, als Kerne frei sind, entscheidet der Planer, wer wie viel Zeit bekommt. Manchmal soll eine lange Rechnung im Hintergrund die übrigen Programme nicht ausbremsen. Dafür kann man einem Prozess sagen, dass er rücksichtsvoll sein soll.

:::definition Definition 6.2 (Nice-Wert)
<span class="anker" id="satz-6-2"></span>

Der __Nice-Wert__ eines Prozesses ist eine ganze Zahl von $-20$ bis $19$, die der Planer beim Aufteilen der Rechenzeit berücksichtigt. Der Standard ist 0. Je höher der Wert, desto „netter“ (englisch „nice“) ist der Prozess zu den anderen und desto weniger Rechenzeit bekommt er, wenn mehrere um einen Kern konkurrieren. Ein neuer Prozess erbt den Nice-Wert seines Elternprozesses.
:::

`nice -n wert befehl` startet einen Befehl mit einem um `wert` höheren Nice-Wert; ohne `-n` erhöht es um 10. `ps` zeigt den Wert in der Spalte `ni` und in `STAT` das Zusatzzeichen `N` für einen Nice-Wert über 0:

```console
$ nice -n 10 sleep 600 &
[1] 772
$ ps -o pid,ni,stat,cmd -p $!
    PID  NI STAT CMD
    772  10 SN   sleep 600
$ nice sleep 601 &
[2] 774
$ ps -o pid,ni,stat,cmd -C sleep
    PID  NI STAT CMD
    772  10 SN   sleep 600
    774  10 SN   sleep 601
$ kill %1 %2
$ jobs
[1]-  Terminated                 nice -n 10 sleep 600
[2]+  Terminated                 nice sleep 601
```

`nice` setzt den Wert und ersetzt sich dann mit exec durch den Befehl; deshalb steht in `ps` nur noch `sleep`. In `top` heißt die Spalte `NI`; die Spalte `PR` daneben ist $20 + \text{Nice-Wert}$.

⁠**Kurz gesagt:** Der Nice-Wert ($-20$ bis 19, Standard 0) sagt dem Planer, wie rücksichtsvoll ein Prozess ist; `nice -n wert` startet ein Programm mit höherem Wert.

### Wie viel ein Nice-Wert ausmacht

<span class="anker" id="stufe-6-3"></span>

Ein Nice-Wert von 10 heißt nicht „zehn Prozent weniger“. Wie viel weniger Rechenzeit ein Prozess bekommt, folgt aus einer festen Regel des Planers.

:::satz Satz 6.3 (Anteile bei verschiedenen Nice-Werten)
<span class="anker" id="satz-6-3"></span>

Konkurrieren Prozesse um einen Kern, bekommt jeder einen Anteil an der Rechenzeit, der seinem Gewicht entspricht. Jede Stufe des Nice-Werts teilt das Gewicht durch etwa 1,25. Ein Prozess mit dem Nice-Wert 0 hat also gegenüber einem mit dem Wert $k$ das $1{,}25^{k}$-fache Gewicht.
:::

So rechnet der Planer, den Linux für gewöhnliche Prozesse benutzt. Seit der Kernelversion 6.6 heißt er EEVDF (englisch „earliest eligible virtual deadline first“), davor hieß er CFS; die Gewichte sind dabei gleich geblieben. Welche Version bei dir läuft, zeigt `uname -r` ([Kapitel 2, Abschnitt 6.1](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/das-system-erkunden.html#stufe-6-1)); auf dem Testsystem ist es 6.6.87.

Der Versuch braucht zwei Prozesse, die wirklich um denselben Kern konkurrieren; auf einem Rechner mit 14 Kernen bekäme sonst jeder seinen eigenen. `taskset -c 0 befehl` startet einen Befehl, der nur auf Kern 0 laufen darf.

```console
$ timeout 15 taskset -c 0 yes > /dev/null &
[1] 776
$ timeout 15 taskset -c 0 nice -n 10 yes > /dev/null &
[2] 778
$ ps -o pid,ni,pcpu,stat,cmd -C yes
    PID  NI %CPU STAT CMD
    777   0 90.1 R    yes
    779  10  9.6 RN   yes
$ top -b -n 2 -d 2 -p $(pgrep -d, -x yes) | tail -n 3
    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
    777 student   20   0   16108   7168   6016 R  90.0   0.0   0:10.30 yes
    779 student   30  10   16108   7168   6016 R  10.0   0.0   0:01.07 yes
$ wait
[1]-  Exit 124                   timeout 15 taskset -c 0 yes > /dev/null
[2]+  Exit 124                   timeout 15 taskset -c 0 nice -n 10 yes > /dev/null
```

`pgrep -d,` trennt die PIDs durch Kommas, wie `top -p` sie erwartet; `top -n 2 -d 2` misst zweimal im Abstand von zwei Sekunden, und die zweite Messung zeigt den Anteil in diesen zwei Sekunden. Der Prozess mit dem Nice-Wert 0 bekommt etwa 90 Prozent der Zeit von Kern 0, der mit 10 etwa 10 Prozent.

::::beispiel [Rechenbeispiel] Der Anteil bei Nice-Wert 10
$1{,}25^{10} \approx 9{,}31$: Der Prozess mit dem Nice-Wert 0 wiegt gut neunmal so viel. Sein Anteil ist sein Gewicht geteilt durch die Summe beider Gewichte; der Planer von Linux rechnet dafür mit den Gewichten 1024 für den Nice-Wert 0 und 110 für den Wert 10. Abbildung [24](#abb-24) führt die Rechnung aus; das Ergebnis, 90,3 und 9,7 Prozent, trifft die Messung.

:::abbildung linux/k8niceanteil 24
Rechenbild: $1{,}25^{10} \approx 9{,}31 \approx 1024/110$. Dann: Anteil (Nice 0) $= 1024 / (1024 + 110) = 1024 / 1134 = 0{,}903$, also 90,3 Prozent; Anteil (Nice 10) $= 110 / 1134 = 0{,}097$, also 9,7 Prozent. Darunter zwei Balken, die zu 90,3 und 9,7 Prozent wachsen, und daneben die gemessenen Werte 90,1 und 9,6.
:::
::::

⁠**Kurz gesagt:** Jede Stufe des Nice-Werts teilt das Gewicht eines Prozesses durch etwa 1,25; bei Nice 0 gegen Nice 10 auf einem Kern ergibt das rund 90 zu 10 Prozent.

:::hintergrund Warum nice auf einem Desktop manchmal kaum wirkt
Der Planer der meisten Ubuntu-Kernel fasst die Prozesse jeder Sitzung, grob gesagt jedes Terminalfensters, zu einer Gruppe zusammen und teilt die Rechenzeit zuerst zwischen den Gruppen auf. Der Nice-Wert wirkt dann nur innerhalb der eigenen Gruppe: Startest du eine Rechnung mit `nice` in einem Terminal und arbeitest in einem anderen weiter, ändert er wenig, denn die beiden Fenster teilen sich die Zeit ohnehin gerecht. Der Kernel von WSL auf dem Testsystem bildet solche Gruppen nicht. Im Versuch oben liefen beide Prozesse im selben Terminal; dort wirkt `nice` in jedem Fall.
:::

### Die Priorität ändern: renice

<span class="anker" id="stufe-6-4"></span>

Oft merkt man erst während einer langen Rechnung, dass sie den Rechner ausbremst. Dann soll sich ihr Nice-Wert ändern, ohne sie neu zu starten.

:::definition Definition 6.4 (renice)
<span class="anker" id="satz-6-4"></span>

`renice -n wert -p pid` setzt den Nice-Wert eines laufenden Prozesses auf `wert`. Ein gewöhnlicher Benutzer darf den Wert seiner eigenen Prozesse nur erhöhen; senken, also mehr Rechenzeit verlangen, darf nur root.
:::

```console
$ sleep 602 &
[1] 787
$ renice -n 15 -p 787
787 (process ID) old priority 0, new priority 15
$ renice -n 5 -p 787
renice: failed to set priority for 787 (process ID): Permission denied
$ sudo renice -n 5 -p 787
787 (process ID) old priority 15, new priority 5
$ ps -o pid,ni,cmd -p 787
    PID  NI CMD
    787   5 sleep 602
$ kill %1
$ jobs
[1]+  Terminated                 sleep 602
```

Mit „priority“ meint `renice` den Nice-Wert. Von 0 auf 15 darf `student` ihn ändern, zurück auf 5 nicht; root darf es. Der Grund ist Gerechtigkeit zwischen den Benutzern: Dürfte jeder seine Prozesse beliebig bevorzugen, hätten bald alle den Wert $-20$, und die Werte bedeuteten nichts mehr.

⁠**Kurz gesagt:** `renice` ändert den Nice-Wert eines laufenden Prozesses; erhöhen darf jeder Besitzer, senken nur root.

### Aufgaben zu Abschnitt [6](#stufe-6)

<span class="anker" id="stufe-6-5"></span>

:::aufgabe Aufgabe 19 ★★ Die Last vorhersagen
<span class="anker" id="aufg-19"></span>

Zwei Prozesse rechnen 60 Sekunden lang ohne Pause; vorher war die Last fast null. (a) Welchen 1-Minuten-Wert erwartest du direkt danach? (b) Prüfe mit `timeout 60 yes > /dev/null &` (zweimal) und `cat /proc/loadavg` nach etwa 61 Sekunden. (c) Wie stark ist ein Rechner mit 14 Kernen dabei ausgelastet?

:::loesung
(a) Mit $n = 2$ und $t = 60$ Sekunden: $2 \cdot (1 - \mathrm{e}^{-1}) \approx 2 \cdot 0{,}632 = 1{,}26$. War die Last vorher nicht ganz null, kommt ein kleiner Rest dazu: Der alte Wert schrumpft in einer Minute auf etwa 37 Prozent.

```console
$ cat /proc/loadavg
0.17 0.06 0.02 1/273 644
$ timeout 60 yes > /dev/null &
[1] 645
$ timeout 60 yes > /dev/null &
[2] 647
$ cat /proc/loadavg
1.27 0.41 0.14 1/273 654
[1]-  Exit 124                   timeout 60 yes > /dev/null
[2]+  Exit 124                   timeout 60 yes > /dev/null
$ wait
```

(b) Vorher stand die Last bei 0,17; davon bleiben nach einer Minute $0{,}17 \cdot 0{,}37 \approx 0{,}06$, zusammen also etwa $1{,}26 + 0{,}06 = 1{,}32$. Gemessen sind 1,27. Die Messung kam kurz nach dem Ende der beiden `yes`; fiel die letzte Zählung des Kernels schon in die Zeit danach, zählte er null Prozesse und schob den Wert um 8 Prozent nach unten, auf $1{,}32 \cdot 0{,}92 \approx 1{,}21$. Der gemessene Wert liegt zwischen beiden. (c) Während der Minute rechneten zwei der 14 Kerne, die übrigen hatten fast nichts zu tun: $2 / 14 \approx 0{,}14$, also etwa 14 Prozent. Der gleitende 1-Minuten-Wert hinkt hinterher; $1{,}27 / 14 \approx 0{,}09$ unterschätzt die Auslastung deshalb.
:::
:::

:::aufgabe Aufgabe 20 ★★ Anteile bei Nice-Wert 5
<span class="anker" id="aufg-20"></span>

Zwei Prozesse auf einem Kern haben die Nice-Werte 0 und 5. (a) Rechne mit dem Faktor 1,25 je Stufe die Anteile aus. (b) Rechne dasselbe mit den Gewichten 1024 und 335, mit denen der Planer arbeitet. (c) Prüfe mit dem Versuch aus Unterabschnitt [6.3](#stufe-6-3) und `nice -n 5`.

:::loesung
(a) $1{,}25^5 \approx 3{,}05$: Der Prozess mit Nice 0 wiegt etwa dreimal so viel. Sein Anteil ist $3{,}05 / (3{,}05 + 1) \approx 0{,}753$, also 75,3 Prozent; der andere bekommt 24,7 Prozent. (b) $1024 / (1024 + 335) = 1024 / 1359 \approx 0{,}753$ und $335 / 1359 \approx 0{,}247$; auch das ergibt 75,3 und 24,7 Prozent.

```console
$ timeout 15 taskset -c 0 yes > /dev/null &
[1] 655
$ timeout 15 taskset -c 0 nice -n 5 yes > /dev/null &
[2] 657
$ ps -o pid,ni,pcpu,cmd -C yes
    PID  NI %CPU CMD
    656   0 76.0 yes
    658   5 24.5 yes
$ wait
[1]-  Exit 124                   timeout 15 taskset -c 0 yes > /dev/null
[2]+  Exit 124                   timeout 15 taskset -c 0 nice -n 5 yes > /dev/null
```

(c) Gemessen sind 76,0 und 24,5 Prozent, nahe an der Vorhersage. Die kleine Abweichung kommt daher, dass `ps` über die ganze Lebenszeit mittelt und die beiden Prozesse nicht im selben Augenblick starteten.
:::
:::

:::aufgabe Aufgabe 21 ★ Zurück zur alten Priorität
<span class="anker" id="aufg-21"></span>

Du hast eine lange Rechnung versehentlich mit `nice -n 19` gestartet. Warum kannst du sie mit `renice` nicht wieder auf 0 setzen? Welche zwei Wege bleiben?

:::loesung
Den Nice-Wert senken, also mehr Rechenzeit verlangen, darf nur root; `renice -n 0` scheitert deshalb mit „Permission denied“. Es bleiben zwei Wege: mit `sudo renice -n 0 -p pid` die Rechte von root benutzen oder die Rechnung beenden und ohne `nice` neu starten. Steht `sudo` nicht zur Verfügung, bleibt nur der zweite Weg.
:::
:::

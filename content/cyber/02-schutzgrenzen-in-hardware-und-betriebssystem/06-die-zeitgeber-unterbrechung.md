---
title: Die Zeitgeber-Unterbrechung
pfad: Informatik / Cybersecurity / Schutzgrenzen in Hardware und Betriebssystem
adresse: informatik/cybersecurity/schutzgrenzen-in-hardware-und-betriebssystem
knoten: Kapitel 2: Schutzgrenzen in Hardware und Betriebssystem
order: 6120600
summary: Der Kernel teilt die Kerne reihum zwischen den Prozessen auf.
tags: Zeitgeber, Zeitgeber-Unterbrechung, kooperativer Zeitteilung, erzwungener Zeitteilung
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Der Kernel teilt die Kerne reihum zwischen den Prozessen auf. Ein Programm, das keinen Systemaufruf macht und keine Ausnahme auslöst, gibt ihm aber nie Gelegenheit dazu. Dieser Abschnitt zeigt, wie der Kernel die Kontrolle trotzdem zurückbekommt und warum kein Programm das verhindern kann.
:::

:::::vorwissen Was du dafür brauchst: Zeitteilung und Planer

<span class="anker" id="stufe-5-1"></span>

Bei der Zeitteilung lässt der Kernel einen Prozess eine kurze Zeit auf einem Kern rechnen, hält ihn dann an, sichert seinen Stand und lässt einen anderen weiterrechnen. Der Teil des Kernels, der entscheidet, welcher Prozess als Nächstes rechnen darf, heißt Planer; ein Wechsel von einem Prozess zum nächsten heißt Kontextwechsel ([Linux, Kapitel 8, Abschnitt 1.3](/wissen/informatik/linux-und-kommandozeile/prozesse-signale-und-dienste/prozesse-und-ihre-verwandtschaft.html#stufe-1-3)). Mit `taskset -c` lässt sich ein Programm an einen bestimmten Kern binden, mit `timeout` nach einer festen Zeit beenden ([Linux, Kapitel 8, Abschnitte 5.3](/wissen/informatik/linux-und-kommandozeile/prozesse-signale-und-dienste/mit-signalen-arbeiten.html#stufe-5-3) und [6.3](/wissen/informatik/linux-und-kommandozeile/prozesse-signale-und-dienste/last-und-prioritat.html#stufe-6-3)).

⁠**Kurz gesagt:** Der Planer verteilt die Kerne in kurzen Abschnitten reihum; offen ist, wie der Kernel einem rechnenden Programm den Kern wieder wegnimmt.

:::::

### Der Zeitgeber

<span class="anker" id="stufe-5-2"></span>

In einem Mietshaus mit einer einzigen Waschküche könnte man darauf vertrauen, dass jeder nach einer Stunde von selbst geht. Sicherer ist ein Wecker in der Waschküche, den nur der Hausverwalter stellen kann und den die Mieter nicht abschalten können: Er klingelt nach einer Stunde, und der Verwalter schickt den Nächsten hinein. Das ist ein Bild zur Orientierung; im Rechner übernimmt ein Baustein diese Aufgabe.

:::definition Definition 5.1 (Zeitgeber)
<span class="anker" id="satz-5-1"></span>

Ein __Zeitgeber__ (englisch timer) ist ein Baustein im Rechner, der nach einer eingestellten Zeit eine Unterbrechung auslöst. Jeder Kern eines PC-Prozessors hat einen eigenen Zeitgeber.
:::

Den Zeitgeber stellt der Kernel; er legt auch fest, welche Einsprungstelle bei seiner Unterbrechung angesprungen wird. Beides ist privilegiert.

::::beispiel Die Einstellung des Testrechners
Der Linux-Kernel stellt den Zeitgeber eines beschäftigten Kerns so, dass er eine feste Zahl von Malen je Sekunde auslöst. Auf dem Testrechner dieses Kapitels sind es 250 Mal je Sekunde, also alle $1000\,\mathrm{ms}/250=4\,\mathrm{ms}$. Andere Systeme benutzen 100, 300 oder 1000 Mal je Sekunde.
::::

⁠**Kurz gesagt:** Ein Zeitgeber löst nach einer vom Kernel eingestellten Zeit eine Unterbrechung aus.

### Die Zeitgeber-Unterbrechung

<span class="anker" id="stufe-5-3"></span>

Eine Unterbrechung führt nach Unterabschnitt [4.2](der-eintritt-in-den-kernel.html#stufe-4-2) in den Kernel, ganz gleich, welcher Befehl gerade läuft. Beim Zeitgeber wird daraus das Werkzeug, mit dem der Kernel sich den Kern zurückholt.

:::definition Definition 5.2 (Zeitgeber-Unterbrechung)
<span class="anker" id="satz-5-2"></span>

Eine __Zeitgeber-Unterbrechung__ ist die Unterbrechung, die der Zeitgeber eines Kerns auslöst. Der Prozessor beendet den laufenden Befehl, sichert den Stand des Programms, wechselt auf Stufe 0 und springt an die Einsprungstelle, die der Kernel für den Zeitgeber eingetragen hat.
:::

An dieser Stelle zählt der Kernel die Zeit weiter, prüft, ob der laufende Prozess seinen Anteil verbraucht hat, und ruft gegebenenfalls den Planer auf. Wählt der Planer einen anderen Prozess, kehrt der Kernel nicht zum alten zurück, sondern stellt den gesicherten Stand des neuen her und kehrt dorthin zurück. Abbildung [18](#abb-18) zeigt das auf einem Kern.

:::abbildung cyber/k2zeitleiste 18
Eine Zeitleiste nach rechts mit Markierungen alle 4 ms. Zuerst rechnet Programm A (blauer Balken), der nie einen Systemaufruf macht. An der ersten Markierung blitzt „Zeitgeber“ auf, ein kurzer Kernel-Abschnitt (grau, Stufe 0) folgt: „Zeit zählen, Anteil von A verbraucht?“ – nein –, A rechnet weiter. An einer späteren Markierung lautet die Antwort ja: Der Planer wählt B, der Kernel sichert den Stand von A, lädt den von B, und B rechnet (grüner Balken). Unter der Leiste die Stufe: 3, kurz 0, 3, kurz 0, 3.
:::

::::beispiel Zwei rechnende Programme auf einem Kern
Zwei Programme A und B rechnen ohne Pause auf demselben Kern. Der Zeitgeber unterbricht alle 4 ms. Bei jeder Unterbrechung betritt der Kernel für einen kurzen Moment den Kern, zählt, und nach einigen Unterbrechungen wechselt er von A zu B oder zurück. Beide kommen voran, obwohl keines je freiwillig aufhört.
::::

⁠**Kurz gesagt:** Bei jeder Zeitgeber-Unterbrechung kommt der Kernel auf den Kern, und dort kann er einen anderen Prozess weiterlaufen lassen.

### Kooperativ oder erzwungen

<span class="anker" id="stufe-5-4"></span>

Ohne Zeitgeber käme der Kernel nur bei Systemaufrufen und Ausnahmen auf den Kern. Ein Betriebssystem kann so gebaut sein, und frühe Betriebssysteme für PCs waren es.

:::definition Definition 5.3 (kooperative und erzwungene Zeitteilung)
<span class="anker" id="satz-5-3"></span>

Bei __kooperativer Zeitteilung__ bekommt der Kernel den Kern nur zurück, wenn das laufende Programm in den Kernel eintritt, etwa durch einen Systemaufruf oder durch einen Befehl, der die Kontrolle ausdrücklich abgibt. Bei __erzwungener Zeitteilung__ holt sich der Kernel den Kern mit der Zeitgeber-Unterbrechung zurück, ohne dass das Programm mitwirken muss.
:::

Linux und alle heutigen Desktop-Betriebssysteme teilen die Zeit erzwungen. Abbildung [19](#abb-19) stellt beide Verfahren nebeneinander.

:::abbildung cyber/k2kooperativ 19
Zwei Zeitleisten untereinander, auf beiden startet Programm A eine Endlosschleife ohne Systemaufruf, Programm B wartet. Oben „kooperativ“: Der Balken von A läuft bis zum rechten Rand, B bleibt grau mit der Aufschrift „wartet für immer“. Unten „erzwungen“: Alle 4 ms blitzt „Zeitgeber“ auf, der Kernel kommt kurz auf den Kern, und A und B wechseln sich ab; beide Balken wachsen.
:::

::::beispiel Eine Endlosschleife ohne Systemaufruf
Die Shell-Zeile `while :; do :; done` ist eine Endlosschleife: Der eingebaute Befehl `:` tut nichts und meldet Erfolg, also läuft die Schleife ewig. Sie fragt den Kernel dabei nie etwas. Bei kooperativer Zeitteilung bekäme der Kernel diesen Kern nie wieder: Die anderen Programme, die dort warten, stünden still, bis jemand den Rechner ausschaltet. Bei erzwungener Zeitteilung unterbricht der Zeitgeber die Schleife alle paar Millisekunden, und der Planer lässt andere Prozesse rechnen.
::::

⁠**Kurz gesagt:** Kooperativ ist der Kernel auf die Mitarbeit jedes Programms angewiesen, erzwungen holt er sich den Kern mit dem Zeitgeber.

:::hintergrund Warum ein Betriebssystem sich nicht auf Mitarbeit verlassen darf
Die Zeitteilung ist eine Richtlinie: Jeder Prozess bekommt seinen Anteil. Ein Mechanismus, der nur funktioniert, wenn jedes Programm freiwillig mitmacht, setzt sie nicht durch. Ein einziges fehlerhaftes Programm mit einer Endlosschleife oder ein einziges böswilliges Programm genügt, um alle anderen zu blockieren. Das verletzt die Verfügbarkeit aus [Kapitel 1, Abschnitt 1.6](/wissen/informatik/cybersecurity/sicherheit-schutzziele-und-spielregeln/was-geschutzt-wird-schutzgut-und-schutzziele.html#stufe-1-6). Ältere Systeme für PCs, etwa die Windows-Versionen vor Windows 95 für ihre Fensterprogramme und das klassische Mac OS bis Version 9, teilten die Zeit kooperativ, und ein hängendes Programm brachte dort oft das ganze System zum Stehen. Der Zeitgeber ist außerdem die Voraussetzung dafür, dass der Kernel überhaupt zwischen Prozessen wechseln kann, wann er will, und nicht erst, wann das laufende Programm es zulässt.
:::

### Warum kein Programm den Wecker abstellen kann

<span class="anker" id="stufe-5-5"></span>

Der Zeitgeber hilft nur, wenn ein Programm ihn nicht abschalten, umstellen oder überhören kann. Genau dafür sorgen die privilegierten Befehle aus Unterabschnitt [3.4](privilegstufen-und-schutzringe.html#stufe-3-4).

:::satz Satz 5.4 (Der Kernel kommt immer wieder dran)
<span class="anker" id="satz-5-4"></span>

Den Zeitgeber stellen und abschalten, die Einsprungstelle für seine Unterbrechung eintragen und Unterbrechungen sperren kann nur Code auf Stufe 0. Ein Programm auf Stufe 3 kann deshalb nicht verhindern, dass der Kernel in regelmäßigen Abständen auf jeden Kern kommt, auf dem es rechnet.
:::

Versucht ein Programm, Unterbrechungen mit CLI zu sperren, löst der Prozessor eine Schutzverletzung aus, wie bei HLT in Unterabschnitt [3.5](privilegstufen-und-schutzringe.html#stufe-3-5). Abbildung [20](#abb-20) zeigt die drei Stellschrauben.

:::abbildung cyber/k2wecker 20
Ein Kern mit drei Stellschrauben, jede mit einem Schloss „nur Stufe 0“: „Zeitgeber stellen/abschalten“, „Einsprungstelle für den Zeitgeber“, „Unterbrechungen sperren (CLI)“. Ein Programm auf Stufe 3 greift nacheinander nach allen drei; jeder Griff prallt ab („auf Stufe 3 nicht erlaubt“). Zum Schluss blitzt der Zeitgeber, und der Kernel kommt auf den Kern.
:::

Der Kernel selbst sperrt Unterbrechungen gelegentlich für sehr kurze Zeit, etwa während er eine Tabelle umbaut, die eine Unterbrechung nicht halb fertig sehen darf.

::::beispiel Was das Programm in der Waschküche alles nicht kann
Das Programm mit der Endlosschleife kann den Zeitgeber nicht auf „nie“ stellen (privilegiert), nicht auf eigenen Code umleiten (die Einsprungtabelle setzt nur Stufe 0) und Unterbrechungen nicht sperren (CLI ist gesperrt). Es kann nur rechnen, und während es rechnet, kommt der Kernel alle 4 ms vorbei.
::::

⁠**Kurz gesagt:** Weil alles, was den Zeitgeber betrifft, privilegiert ist, kann kein Programm den Kernel von seinem Kern fernhalten.

### Zeitgeber-Unterbrechungen zählen

<span class="anker" id="stufe-5-6"></span>

Der Kernel zählt jede Unterbrechung je Kern und zeigt die Zähler in der Datei `/proc/interrupts` an, eine Zeile je Art und eine Spalte je Kern. Für den Zeitgeber gibt es zwei Zeilen, die in Frage kommen: `LOC` („Local timer interrupts“) auf einem PC oder in einer gewöhnlichen VM, `HVS` („Hyper-V stimer0 interrupts“) unter WSL 2, weil der Kernel dort den Zeitgeber benutzt, den der Hypervisor von Windows bereitstellt.

Ein zweiter Punkt erklärt, warum die Zahlen zunächst klein wirken. Ein Kern, der nichts zu tun hat, braucht keine regelmäßigen Unterbrechungen; der Linux-Kernel stellt den Zeitgeber eines untätigen Kerns deshalb erst auf das nächste tatsächlich anstehende Ereignis. Nur auf beschäftigten Kernen läuft der Takt von 250 Unterbrechungen je Sekunde.

::::beispiel Die Endlosschleife und der Zeitgeber
Welche Zeile auf deinem System zählt, zeigt ein erster Blick; `cut -c1-48` schneidet die Zeilen nach den ersten vier Kernen ab:

```console
$ grep -E 'LOC|HVS' /proc/interrupts | cut -c1-48
LOC:          0          0          0          0
HVS:       1446       1260       1902        938
```

Unter WSL 2 bleibt `LOC` bei null, es zählt `HVS`. Nun läuft die Endlosschleife zehn Sekunden lang, an Kern 3 gebunden; vorher und nachher zeigt `awk` die Zähler von Kern 0 (Feld 2) und Kern 3 (Feld 5). Ersetze in einer VM `HVS` durch `LOC`.

```console
$ grep HVS /proc/interrupts | awk '{print $2, $5}'
1447 938
$ timeout 10 taskset -c 3 bash -c 'while :; do :; done'
$ echo $?
124
$ grep HVS /proc/interrupts | awk '{print $2, $5}'
1570 3447
```

Der Exit-Status 124 meldet, dass `timeout` die Schleife nach zehn Sekunden beendet hat. Auf Kern 3 kamen $3447-938=2509$ Unterbrechungen hinzu, auf Kern 0 nur $1570-1447=123$. Abbildung [21](#abb-21) rechnet das in Unterbrechungen je Sekunde um.

:::abbildung cyber/k2rtakt 21
Rechenbild. Oben die Zählerstände von Kern 0 und Kern 3 vorher (1447 und 938) und nachher (1570 und 3447), darunter zwei Rechnungen. Kern 3 (Endlosschleife): $(3447-938)/10\,\mathrm s=2509/10\,\mathrm s=250{,}9$ je Sekunde, darunter „eingestellt: 250 je Sekunde, alle 4 ms“. Kern 0 (fast untätig): $(1570-1447)/10\,\mathrm s=123/10\,\mathrm s=12{,}3$ je Sekunde.
:::

Der beschäftigte Kern wurde also fast genau 250-mal je Sekunde unterbrochen, obwohl die Schleife selbst den Kernel nie gerufen hat. Bei jeder dieser Unterbrechungen hätte der Planer den Kern einem anderen Prozess geben können.
::::

⁠**Kurz gesagt:** `/proc/interrupts` zeigt, dass ein rechnender Kern rund 250-mal je Sekunde in den Kernel springt, ob das Programm will oder nicht.

### Aufgaben zu Abschnitt [5](#stufe-5)

<span class="anker" id="stufe-5-7"></span>

:::aufgabe Aufgabe 11 ★ Takt und Abstand
<span class="anker" id="aufg-11"></span>

(a) Ein Kernel stellt den Zeitgeber eines beschäftigten Kerns auf 1000 Unterbrechungen je Sekunde. Wie viele Millisekunden liegen zwischen zwei Unterbrechungen? (b) Wie viele Zeitgeber-Unterbrechungen gibt es je Sekunde auf dem Testrechner mit 14 Kernen, wenn alle Kerne beschäftigt sind und der Takt 250 je Sekunde beträgt? (c) Warum kann man aus den Zählern eines untätigen Kerns nicht auf den eingestellten Takt schließen?

:::loesung
(a) $1000\,\mathrm{ms}/1000=1\,\mathrm{ms}$.

(b) $14\cdot250=3500$ Zeitgeber-Unterbrechungen je Sekunde, wenn alle Kerne beschäftigt sind.

(c) Ein untätiger Kern bekommt keine regelmäßigen Unterbrechungen; der Kernel stellt seinen Zeitgeber erst auf das nächste tatsächlich anstehende Ereignis. Seine Zähler wachsen deshalb unregelmäßig und viel langsamer, auf dem Testsystem um etwa 12 je Sekunde auf Kern 0. Den eingestellten Takt sieht man nur auf einem Kern, der die ganze Zeit rechnet.
:::
:::

:::aufgabe Aufgabe 12 ★★ Selbst messen
<span class="anker" id="aufg-12"></span>

Wiederhole die Messung aus dem Beispiel „Die Endlosschleife und der Zeitgeber“ an deinem Rechner, und zwar zweimal: einmal mit der Schleife auf einem Kern deiner Wahl, einmal ohne Schleife. Berechne für den gewählten Kern die Unterbrechungen je Sekunde. Welchen Takt hat der Kernel deines Systems ungefähr?

:::loesung
Die Werte hängen vom Rechner ab. Auf dem Testsystem ergab die Messung mit der Schleife auf Kern 3 $(3447-938)/10=250{,}9$ Unterbrechungen je Sekunde, auf dem untätigen Kern 0 $(1570-1447)/10=12{,}3$. Der Takt des Testsystems beträgt also 250 je Sekunde; der kleine Überschuss entsteht, weil zum Takt einzelne andere Ereignisse hinzukommen und weil die Messung nicht exakt zehn Sekunden umfasst. Typische Ergebnisse auf anderen Systemen liegen nahe 100, 250, 300 oder 1000. Ohne Schleife bleiben alle Kerne weit unter dem Takt. Wichtig ist dabei, die richtige Zeile zu nehmen: `LOC` auf einem PC oder in einer gewöhnlichen VM, `HVS` unter WSL 2, und das Feld des gewählten Kerns (Kern $k$ steht in Feld $k+2$).
:::
:::

:::aufgabe Aufgabe 13 ★★ Ein Gedankenexperiment
<span class="anker" id="aufg-13"></span>

Angenommen, ein Prozessor hätte einen Fehler, durch den CLI auf Stufe 3 ausgeführt würde, statt eine Schutzverletzung auszulösen. (a) Was könnte ein Programm mit einer Endlosschleife damit anrichten? (b) Welches Schutzziel aus [Kapitel 1](/wissen/informatik/cybersecurity/sicherheit-schutzziele-und-spielregeln/sicherheit-schutzziele-und-spielregeln.html) wäre verletzt? (c) Welche der drei Forderungen an einen Referenzmonitor ist für den Kernel dann nicht mehr erfüllt?

:::loesung
(a) Das Programm sperrt mit CLI die Unterbrechungen und rechnet dann in seiner Endlosschleife. Der Zeitgeber löst zwar aus, aber der Prozessor nimmt die Unterbrechung nicht an. Der Kernel kommt auf diesem Kern nie wieder zum Zug: Kein anderer Prozess läuft dort mehr, und auch Tastatur und Netz werden auf diesem Kern nicht mehr bedient. Auf einem Rechner mit nur einem Kern stünde alles still.

(b) Verletzt ist die Verfügbarkeit: Berechtigte können den Rechner nicht mehr nutzen, wann sie wollen.

(c) Verletzt ist zuerst die Forderung „manipulationssicher“: Ein geprüftes Programm verstellt eine Einstellung, von der die Arbeit des Kernels abhängt. Die Folge ist, dass auch „immer aufgerufen“ nicht mehr gilt, denn der Kernel wird für diesen Kern nicht mehr gerufen. Deshalb ist CLI privilegiert.
:::
:::

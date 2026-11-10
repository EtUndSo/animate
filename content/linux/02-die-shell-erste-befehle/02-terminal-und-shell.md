---
title: Terminal und Shell
pfad: Informatik / Linux und Kommandozeile / Die Shell: erste Befehle
adresse: informatik/linux-und-kommandozeile/die-shell-erste-befehle
knoten: Kapitel 2: Die Shell: erste Befehle
order: 6070200
summary: In Kapitel 1 hieß das Fenster, in das man Befehle tippt, einfach Terminal.
tags: Terminalemulator, Shell, bash, Eingabeaufforderung, aktueller Ordner, root, Sitzung
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
In [Kapitel 1](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/ein-linux-zum-ueben.html) hieß das Fenster, in das man Befehle tippt, einfach Terminal. Genauer arbeiten darin zwei Programme mit getrennten Aufgaben zusammen. Dieser Abschnitt trennt die beiden, erklärt, was die Eingabeaufforderung verrät, und zeigt, wann eine Arbeitssitzung beginnt und endet.
:::

### Was du dafür brauchst: das Terminal aus Kapitel 1

<span class="anker" id="stufe-1-1"></span>

[Kapitel 1, Abschnitt 2.3](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/drei-wege-zu-einem-eigenen-linux.html#stufe-2-3) hat das Terminal eingeführt: ein Programm mit einem Fenster, in das man Befehle als Text eintippt und in dem die Antworten des Rechners als Text erscheinen. Ist es bereit, zeigt es am Anfang der Zeile eine Eingabeaufforderung, unter Ubuntu etwa `student@labor:~$`. Das Kapitel kürzt sie mit `$` ab.

Unter WSL 2 öffnest du das Terminal über das Startmenü, im Programm „Terminal“ von Windows über den Eintrag `Ubuntu-26.04` oder mit dem Befehl `wsl` in der PowerShell ([Kapitel 1, Abschnitt 4.4](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/wsl-2-linux-neben-windows.html#stufe-4-4)). In einer virtuellen Maschine oder im Live-System öffnest du das Programm „Terminal“ von Ubuntu, am schnellsten mit Strg+Alt+T.

Außerdem brauchst du drei Begriffe aus [Kapitel 1, Abschnitt 1](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/betriebssystem-kernel-und-distribution.html#stufe-1). Der Kernel ist der einzige Teil des Systems, der die Hardware direkt steuert. Alle anderen Programme laufen im Benutzermodus, in dem der Prozessor bestimmte Befehle sperrt. Dienste wie „lies diese Datei“ bekommen sie nur, indem sie den Kernel mit einem Systemaufruf darum bitten.

::::beispiel Ein erster Befehl
Öffne ein Terminal, tippe `uname -r` und drücke die Eingabetaste. Der Rechner antwortet mit der Version seines Kernels; unter WSL 2 endet sie auf `WSL2`, in einer virtuellen Maschine oder im Live-System auf `generic`.

```console
$ uname -r
6.6.87.2-microsoft-standard-WSL2
```
::::

⁠**Kurz gesagt:** Im Terminal tippt man Befehle als Text; die Eingabeaufforderung zeigt, dass es bereit ist.

### Der Terminalemulator

<span class="anker" id="stufe-1-2"></span>

Wenn du `uname -r` tippst, muss jemand die Buchstaben ins Fenster zeichnen, und jemand muss verstehen, dass das ein Befehl ist. Das sind zwei verschiedene Aufgaben, und unter Linux erledigen sie zwei verschiedene Programme. Das erste ist für das Fenster zuständig.

**Ein Gerät, nachgebaut als Programm.** Vor dem Siegeszug der Personal Computer war ein Terminal ein eigenes Gerät: ein Bildschirm mit Tastatur, über ein Kabel mit einem großen Rechner verbunden, den sich viele Menschen teilten. Das Gerät konnte selbst nichts rechnen. Es schickte jeden Tastendruck als Zeichen über das Kabel und zeigte jedes Zeichen an, das zurückkam. Heute ahmt ein gewöhnliches Programm dieses Gerät nach. Abbildung [1](#abb-1) zeigt, wo es sitzt.

:::abbildung linux/k2schichten 1
Vom Tastendruck zum Kernel. Der Terminalemulator gibt jeden Tastendruck als Zeichen an die Shell weiter und zeichnet, was zurückkommt. Die Shell versteht die Zeile und lässt den Befehl ausführen; an die Hardware kommt auch sie nur über Systemaufrufe an den Kernel.
:::

:::definition Definition 1.1 (Terminalemulator)
<span class="anker" id="satz-1-1"></span>

Ein __Terminalemulator__ ist ein Programm, das ein Fenster mit Textzeilen zeigt, jeden Tastendruck als Zeichen an ein anderes Programm weitergibt und jedes Zeichen, das dieses Programm zurückschickt, im Fenster darstellt. Was die Zeichen bedeuten, versteht er nicht.
:::

Unter Windows ist das meist das Programm „Terminal“ von Windows, englisch Windows Terminal, in dem auch WSL 2 läuft; das Kapitel nennt es kurz Windows-Terminal. Ubuntu bringt ein eigenes Programm mit, das im Menü „Terminal“ heißt; seit Ubuntu 25.10 ist das das Programm Ptyxis. Andere Linux-Systeme haben andere, etwa „Konsole“. Im Alltag sagt man zu allen einfach Terminal, und das Kapitel tut es ebenso, wenn es um das Fenster geht.

::::beispiel Was das Fenster bei einem Befehl tut
Du tippst `u`. Der Terminalemulator schickt das Zeichen `u` weiter, und erst wenn es von der Gegenseite zurückkommt, zeichnet er es ins Fenster. Dasselbe geschieht mit `name -r`. Die Eingabetaste schickt das Zeichen für das Zeilenende. Danach kommt die Antwort `6.6.87.2-microsoft-standard-WSL2` als Folge von Zeichen zurück, und der Terminalemulator zeichnet sie Buchstabe für Buchstabe. Dass es sich um einen Befehl handelte, hat er nie erfahren.
::::

⁠**Kurz gesagt:** Der Terminalemulator ist nur das Fenster: Er reicht Tastendrücke weiter und zeichnet Zeichen, ohne sie zu verstehen.

:::hintergrund Wie Fenster und Shell miteinander verbunden sind
Zwischen dem Terminalemulator und dem Programm, das die Zeichen versteht, liegt kein Kabel mehr, sondern ein *Pseudoterminal*: ein Paar von Geräten, die nur aus Software bestehen und die der Kernel bereitstellt. Was der Terminalemulator in die eine Seite schreibt, kann das Programm auf der anderen Seite lesen, als säße es an einem echten Terminal von früher, und umgekehrt. Die Programmseite heißt unter Linux `/dev/pts/0`, `/dev/pts/1` und so weiter; der Befehl `tty` zeigt, an welcher die eigene Shell hängt. Weil der Kernel in der Mitte sitzt, kann er bestimmte Tastenkombinationen selbst auswerten, bevor sie beim Programm ankommen. Für das Programm hinter dem Fenster ist so jedes Terminal gleich, ob Windows-Terminal, das Terminal von Ubuntu oder eine Verbindung über das Netz.
:::

### Die Shell

<span class="anker" id="stufe-1-3"></span>

Das Fenster versteht keine Befehle. Ein zweites Programm muss die getippte Zeile lesen, herausfinden, was gemeint ist, dafür sorgen, dass es geschieht, und danach auf die nächste Zeile warten. Dieses Programm ist der eigentliche Gesprächspartner an der Kommandozeile.

**Ein Kreislauf.** Man kann sich dieses Programm wie die Bedienung in einem Restaurant vorstellen: Sie nimmt eine Bestellung auf, gibt sie an die Küche weiter, bringt das Ergebnis an den Tisch und fragt nach dem nächsten Wunsch (ein Bild, kein Mechanismus). Abbildung [2](#abb-2) zeigt den Kreislauf, den dieses Programm immer wieder durchläuft.

:::abbildung linux/k2schleife 2
Der Kreislauf der Shell: Eingabeaufforderung zeigen, eine Zeile lesen, den Befehl suchen, ihn ausführen oder ausführen lassen, auf das Ende warten und von vorn beginnen.
:::

:::definition Definition 1.2 (Shell)
<span class="anker" id="satz-1-2"></span>

Eine __Shell__ ist ein Programm, das Befehle als Text entgegennimmt, sie ausführt oder von anderen Programmen ausführen lässt und danach auf den nächsten Befehl wartet. Sie zeigt die Eingabeaufforderung, sobald sie für den nächsten Befehl bereit ist.
:::

Es gibt viele Shells. Unter Ubuntu, Debian und Fedora öffnet das Terminal die Shell __bash__, kurz für „Bourne-Again Shell“. Kali Linux und macOS benutzen die sehr ähnliche zsh. Alles in diesem Kapitel gilt für bash; fast alles gilt auch für zsh.

::::beispiel Welche bash läuft hier?
Die Shell ist selbst ein Befehl, und wie viele Befehle nennt sie mit `--version` ihre Fassung:

```console
$ bash --version
GNU bash, version 5.3.9(1)-release (x86_64-pc-linux-gnu)
Copyright (C) 2025 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>

This is free software; you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
```

Ubuntu 26.04 liefert bash in der Fassung 5.3.9. `x86_64` bezeichnet den Prozessortyp, für den das Programm übersetzt ist, die übliche 64-Bit-Familie von Intel und AMD.
::::

⁠**Kurz gesagt:** Die Shell ist das Programm, das deine Befehle liest und ausführen lässt; unter Ubuntu ist es bash.

:::hintergrund Die Shell ist ein gewöhnliches Programm
Die Shell gehört nicht zum Kernel. Sie läuft im Benutzermodus wie ein Texteditor und kommt an Dateien, Bildschirm und andere Programme nur über Systemaufrufe heran ([Kapitel 1, Abschnitt 1.4](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/betriebssystem-kernel-und-distribution.html#stufe-1-4)). Um ein Programm wie `uname` zu starten, bittet sie den Kernel mit Systemaufrufen, ein neues laufendes Programm aus der Datei zu erzeugen, in der das Programm steht, und wartet, bis es fertig ist; dann zeigt sie wieder die Eingabeaufforderung. Weil die Shell nur ein Programm unter vielen ist, kann man sie austauschen, ohne am System etwas anderes zu ändern; die Datei `/etc/shells` listet die Shells, die ein Benutzer auf diesem Rechner als seine Shell wählen darf.

Das englische Wort bedeutet Schale; im Bild umgibt die Shell den Kern des Systems, den Kernel, wie eine Schale. Geprägt hat es der Informatiker Louis Pouzin Ende 1964 oder Anfang 1965 für das Betriebssystem Multics. Die erste Shell von Unix schrieb Ken Thompson 1971; 1979 folgte die Shell von Stephen Bourne, die bis heute das Vorbild ist. bash erschien 1989 als freie Neufassung für das GNU-Projekt, und ihr Name ist ein Wortspiel: „wiedergeborene“ Bourne-Shell.
:::

:::hintergrund Warum man überhaupt Befehle tippt
Eine grafische Oberfläche zeigt, was möglich ist; man muss sich nichts merken. Die Kommandozeile verlangt, dass man den Befehl kennt. Dafür hat sie vier Vorteile, die mit jeder Aufgabe wachsen.

<ul>

<li>

⁠**Genau.** Ein Befehl sagt vollständig, was geschehen soll. Eine Anleitung „klicke rechts oben auf das Zahnrad“ veraltet mit der nächsten Fassung des Programms, eine Befehlszeile meist nicht.

</li>

<li>

⁠**Wiederholbar.** Ein getippter Befehl lässt sich abschreiben, speichern und beliebig oft ausführen, auch von anderen Menschen.

</li>

<li>

⁠**Automatisierbar.** Wer 800 Urlaubsfotos nach Datum umbenennen will und für jedes Foto 15 Sekunden klickt, braucht 12 000 Sekunden, also 3 Stunden und 20 Minuten. Ein einziger Befehl, der die Fotos der Reihe nach umbenennt, erledigt dieselbe Arbeit in Sekunden, und er wird nicht müde.

</li>

<li>

⁠**Fernsteuerbar.** Text lässt sich mit sehr wenig Daten über das Netz schicken. Server im Rechenzentrum haben oft gar keinen Bildschirm; man bedient sie ausschließlich über eine Shell.

</li>

</ul>

Viele Werkzeuge der Informatik gibt es deshalb nur für die Kommandozeile.
:::

### Die Eingabeaufforderung

<span class="anker" id="stufe-1-4"></span>

Die Shell muss dir mitteilen, wann sie bereit ist. Ubuntu nutzt diese Gelegenheit, um zugleich zu sagen, wer du bist, auf welchem Rechner du arbeitest und wo du dich gerade befindest.

:::abbildung linux/k2prompt 3
Die Eingabeaufforderung von Ubuntu, zerlegt: Benutzer, Rechner, aktueller Ordner und das Schlusszeichen. Darunter dieselbe Stelle für das Konto `root`, das alles darf: Das Schlusszeichen ist `#`.
:::

:::definition Definition 1.3 (Eingabeaufforderung)
<span class="anker" id="satz-1-3"></span>

Die __Eingabeaufforderung__ ist der Text, den die Shell an den Anfang einer Zeile schreibt, wenn sie bereit ist, den nächsten Befehl zu lesen. Unter Ubuntu besteht sie aus dem Benutzernamen, dem Zeichen `@`, dem Namen des Rechners, einem Doppelpunkt, dem aktuellen Ordner und einem Schlusszeichen.
:::

Die Shell arbeitet immer in einem bestimmten Ordner. Dieser Ordner heißt __aktueller Ordner__. Nach dem Öffnen eines Terminals ist es dein persönlicher Ordner, den die Eingabeaufforderung mit `~` abkürzt; ausgeschrieben heißt er `/home/student`. Wechselst du den Ordner, ändert sich die Eingabeaufforderung mit. Der Befehl `cd` wechselt ihn; `cd` ohne Angabe führt zurück in den persönlichen Ordner. Ubuntu färbt Benutzer und Rechner grün und den Ordner blau.

::::beispiel Die Eingabeaufforderung wandert mit
So sieht es im Fenster aus, wenn man erst in den Systemordner `/etc` und dann zurück wechselt. Diesmal steht die ganze Eingabeaufforderung da, nicht nur ihr Schlusszeichen:

```text
student@labor:~$ cd /etc
student@labor:/etc$ cd
student@labor:~$
```
::::

**Das Schlusszeichen.** Jedes Linux-System hat ein Benutzerkonto, das alles darf: Dateien jedes anderen lesen, Systemdateien ändern, Programme installieren. Dieses Konto heißt __root__. Läuft die Shell als root, endet die Eingabeaufforderung mit `#` statt mit `$`, etwa `root@labor:~#`. Das Zeichen ist eine Warnung: Ein Tippfehler als root kann das System beschädigen, denn niemand hält dich auf. Gewöhnliche Arbeit erledigt man deshalb als gewöhnlicher Benutzer mit `$`, und alle Befehle in diesem Kapitel brauchen keine besonderen Rechte.

⁠**Kurz gesagt:** Die Eingabeaufforderung zeigt Benutzer, Rechner und aktuellen Ordner; `$` heißt gewöhnlicher Benutzer, `#` heißt root.

### Die Sitzung

<span class="anker" id="stufe-1-5"></span>

Du kannst mehrere Terminalfenster gleichzeitig öffnen, und jedes zeigt seine eigene Eingabeaufforderung. Das ist kein Zufall: In jedem Fenster läuft eine eigene Shell. Was eine Shell sich merkt, gilt deshalb nur in ihrem Fenster und nur, solange sie läuft.

:::abbildung linux/k2sitzungen 4
Zwei Fenster, zwei Shells, zwei Sitzungen. Wechselt die linke Shell nach `/etc`, bleibt die rechte in ihrem Ordner; endet die linke mit `exit`, läuft die rechte weiter.
:::

:::definition Definition 1.4 (Sitzung)
<span class="anker" id="satz-1-4"></span>

Eine __Sitzung__ ist die Zeit vom Start einer Shell in einem Terminal bis zu ihrem Ende. Jede Sitzung hat ihren eigenen aktuellen Ordner und ihre eigene Liste der bisher getippten Befehle; zwei Sitzungen wissen nichts voneinander.
:::

Beenden kannst du eine Sitzung mit dem Befehl `exit`. Die Shell endet dann, und das Terminal schließt meist sein Fenster oder seinen Tab. Schließt du umgekehrt das Fenster, beendet das auch die Shell darin.

::::beispiel Zwei Fenster nebeneinander
Öffne zwei Terminalfenster, im Windows-Terminal etwa mit einem zweiten Tab. Im ersten tippst du `cd /etc`; die Eingabeaufforderung dort endet auf `/etc$`. Im zweiten Fenster steht weiterhin `~$`, denn dessen Shell hat den Ordner nie gewechselt. Tippst du im ersten Fenster `exit`, verschwindet es; im zweiten arbeitest du ungestört weiter.
::::

⁠**Kurz gesagt:** Jedes Terminalfenster hat seine eigene Shell und damit seine eigene Sitzung, die mit `exit` endet.

### Aufgaben zu Abschnitt [1](#stufe-1)

<span class="anker" id="stufe-1-6"></span>

:::aufgabe Aufgabe 1 ★ Fenster oder Shell?
<span class="anker" id="aufg-1"></span>

Welches Programm erledigt die Aufgabe, der Terminalemulator, die Shell oder beide? (a) Den Buchstaben `u` ins Fenster zeichnen. (b) Erkennen, dass `uname` ein Befehl ist. (c) Den Text `student@labor:~$` erzeugen. (d) Ihn ins Fenster zeichnen. (e) Im Benutzermodus laufen. (f) Sich ohne Änderung am Kernel gegen ein anderes Programm austauschen lassen.

:::loesung
(a) Der Terminalemulator. Er zeichnet jedes Zeichen, das von der Shell zurückkommt; das `u` erscheint also, weil die Shell es zurückgeschickt hat, aber gezeichnet hat es das Fenster.

(b) Die Shell. Der Terminalemulator kennt keine Befehle; für ihn ist `uname` eine Folge von fünf Zeichen.

(c) Die Shell. Die Eingabeaufforderung ist Text, den die Shell schreibt, sobald sie bereit ist; Benutzer, Rechner und aktueller Ordner sind Angaben, die nur sie kennt.

(d) Der Terminalemulator, wie jedes andere Zeichen im Fenster auch.

(e) Beide. Weder das Fenster noch die Shell gehört zum Kernel; beide sind gewöhnliche Programme und kommen an Bildschirm und Tastatur nur über den Kernel heran.

(f) Beide. Man kann ein anderes Terminalprogramm benutzen, ohne dass sich an den Befehlen etwas ändert, und man kann statt bash eine andere Shell starten, ohne den Kernel anzufassen. Genau das ist der Vorteil der Trennung: Jedes der beiden Programme lässt sich unabhängig vom anderen austauschen.
:::
:::

:::aufgabe Aufgabe 2 ★ Eingabeaufforderungen lesen
<span class="anker" id="aufg-2"></span>

Was verrät jede dieser Eingabeaufforderungen? Bei welcher wärst du besonders vorsichtig, und warum? (a) `mira@notebook:~$` (b) `student@labor:/etc$` (c) `root@server:/var/log#` (d) `PS C:\Users\mira>`

:::loesung
(a) Benutzer `mira` auf dem Rechner `notebook`, im persönlichen Ordner, als gewöhnlicher Benutzer (`$`).

(b) Benutzer `student` auf dem Rechner `labor`, im Systemordner `/etc`, als gewöhnlicher Benutzer. Weil in `/etc` Einstellungen des ganzen Systems liegen, schaut man hier nur hin; ändern kann ein gewöhnlicher Benutzer dort ohnehin fast nichts.

(c) Das Konto `root` auf einem Rechner namens `server`, im Ordner `/var/log`. Das Schlusszeichen `#` zeigt: Diese Shell darf alles. Hier ist besondere Vorsicht geboten, denn jeder Tippfehler wird ausgeführt, ohne dass das System nachfragt oder etwas verweigert.

(d) Das ist keine Linux-Shell, sondern die PowerShell von Windows ([Kapitel 1, Abschnitt 2.3](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/drei-wege-zu-einem-eigenen-linux.html#stufe-2-3)), im Ordner `C:\Users\mira`. Linux-Befehle wie `uname` gibt es dort nicht.
:::
:::

:::aufgabe Aufgabe 3 ★★ Zwei Sitzungen
<span class="anker" id="aufg-3"></span>

Öffne zwei Terminalfenster oder zwei Tabs. Tippe im ersten `cd /etc` und vergleiche die beiden Eingabeaufforderungen. Tippe dann im ersten `exit`. Beschreibe, was du siehst, und erkläre es mit dem Begriff der Sitzung. Was zeigt das zweite Fenster, wenn du dort `cd /etc` und danach `cd` eingibst?

:::loesung
Nach `cd /etc` zeigt das erste Fenster `student@labor:/etc$`, das zweite weiterhin `student@labor:~$`. Nach `exit` schließt sich das erste Fenster oder sein Tab, das zweite bleibt unverändert und funktioniert weiter. Der Grund: In jedem Fenster läuft eine eigene Shell, jede Shell bildet eine eigene Sitzung mit eigenem aktuellem Ordner, und das Ende der einen Sitzung berührt die andere nicht. Im zweiten Fenster zeigt die Eingabeaufforderung nach `cd /etc` ebenfalls `/etc` und nach `cd` wieder `~`, genau wie in der Sitzung aus Unterabschnitt [1.4](#stufe-1-4).
:::
:::

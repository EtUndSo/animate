---
title: Privilegstufen und Schutzringe
pfad: Informatik / Cybersecurity / Schutzgrenzen in Hardware und Betriebssystem
adresse: informatik/cybersecurity/schutzgrenzen-in-hardware-und-betriebssystem
knoten: Kapitel 2: Schutzgrenzen in Hardware und Betriebssystem
order: 6120400
summary: Linux, Kapitel 1 hat gezeigt, dass der Prozessor zwei Betriebsarten kennt.
tags: Privilegstufe, aktuelle Privilegstufe, Schutzringe, Ausnahme, Schutzverletzung
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
[Linux, Kapitel 1](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/ein-linux-zum-ueben.html) hat gezeigt, dass der Prozessor zwei Betriebsarten kennt. Dieser Abschnitt klärt, woran der Prozessor erkennt, in welcher er gerade ist, welche Befehle genau gesperrt sind und was geschieht, wenn ein Programm einen davon versucht.
:::

:::::vorwissen Was du dafür brauchst: Signal und Exit-Status

<span class="anker" id="stufe-3-1"></span>

Ein Signal ist eine Nachricht des Kernels an einen Prozess mit einer Nummer und einem Namen. Hat der Prozess nichts anderes festgelegt, führt der Kernel die Standardreaktion aus. Das Signal 11 heißt SIGSEGV; der Kernel schickt es bei einem unerlaubten Speicherzugriff, und die Standardreaktion ist, den Prozess zu beenden und ein Speicherabbild zu schreiben ([Linux, Kapitel 8, Abschnitte 4.1](/wissen/informatik/linux-und-kommandozeile/prozesse-signale-und-dienste/signale.html#stufe-4-1) und [4.2](/wissen/informatik/linux-und-kommandozeile/prozesse-signale-und-dienste/signale.html#stufe-4-2)). Endet ein Programm durch das Signal mit der Nummer $n$, meldet die Shell den Exit-Status $128+n$ ([Linux, Kapitel 8, Abschnitt 4.7](/wissen/informatik/linux-und-kommandozeile/prozesse-signale-und-dienste/signale.html#stufe-4-7)); für SIGSEGV also $128+11=139$. Die Shell schreibt dazu die Meldung `Segmentation fault`, auf manchen Systemen mit dem Zusatz `(core dumped)`.

⁠**Kurz gesagt:** SIGSEGV beendet einen Prozess, und die Shell meldet dann den Exit-Status 139.

:::::

### Die Privilegstufe

<span class="anker" id="stufe-3-2"></span>

Der Prozessor muss bei jedem Befehl wissen, ob er ihn ausführen darf. Also muss er sich irgendwo merken, in welcher Betriebsart er gerade ist, und diese Angabe darf kein Programm selbst umstellen können.

:::definition Definition 3.1 (Privilegstufe, aktuelle Privilegstufe)
<span class="anker" id="satz-3-1"></span>

Eine __Privilegstufe__ ist eine Betriebsart des Prozessors, die festlegt, welche Befehle und Speicherzugriffe erlaubt sind. Die Stufe, in der der Prozessor gerade arbeitet, heißt __aktuelle Privilegstufe__, bei x86-Prozessoren abgekürzt CPL (current privilege level). Sie ist ein Zustand des Prozessors: Ein x86-Prozessor hält sie in den beiden untersten Bits eines Registers mit dem Namen CS. Er ändert sie nur bei kontrollierten Übergängen, beim Wechsel in den Kernel und bei der Rückkehr daraus.
:::

Es gibt keinen Befehl, mit dem ein Programm im Benutzermodus seine Stufe einfach auf die des Kernels setzen könnte. Ein Befehl, der die Stufe im Register CS auf 0 setzen wollte, wird vom Prozessor abgewiesen. Auf Stufe 0 kommt man nur durch einen der kontrollierten Übergänge, und an deren Ziel steht immer Code des Kernels. Abbildung [9](#abb-9) zeigt diese Angabe im Prozessor.

:::abbildung cyber/k2cpl 9
Ein Prozessor als Kasten, darin das Register CS mit seinen beiden untersten Bits hervorgehoben: zuerst `11` mit der Anzeige „Stufe 3: Benutzermodus“. Ein Programmbefehl „setze Stufe 0“ prallt am Prozessor ab (rotes Kreuz). Dann läuft ein Pfeil durch eine Tür mit der Aufschrift „kontrollierter Übergang“; die Bits wechseln zu `00`, die Anzeige zu „Stufe 0: Kernel“, und der Befehlszeiger zeigt in den Kernel. Ein zweiter Übergang führt zurück zu `11`.
:::

::::beispiel Die Stufe in zwei Bits
Zwei Bits können die Werte $00_2=0$, $01_2=1$, $10_2=2$ und $11_2=3$ annehmen. Läuft der Kernel, stehen in den beiden untersten Bits von CS die Bits `00`, also Stufe 0. Läuft die Shell oder `cat`, stehen dort `11`, also Stufe 3. Ein Programm, das als root läuft, ändert daran nichts: Auch `sudo cat /etc/shadow` läuft auf Stufe 3. root ist ein Begriff des Betriebssystems, nicht des Prozessors; der Kernel prüft bei root nur weniger, der Prozessor sperrt für root genau dieselben Befehle wie für jedes andere Programm. Abbildung [10](#abb-10) stellt die beiden Ebenen nebeneinander.

:::abbildung cyber/k2root 10
Zwei Programme nebeneinander: links `cat` der Benutzerin `student`, rechts `sudo cat` mit den Rechten von root. Bei beiden zeigt ein Kästchen „CS, unterste Bits: 11 = Stufe 3“. Darunter der Kernel mit „CS: 00 = Stufe 0“. Beide Programme schicken die Anfrage „/etc/shadow öffnen“ nach unten: Beim linken antwortet die Rechteprüfung des Kernels mit einem Kreuz, beim rechten mit einem Häkchen („root: Prüfung fast ganz übersprungen“). Dann versuchen beide den Befehl HLT; beide prallen am Prozessor ab. Unter dem Bild zwei Zeilen: „Benutzer und root: Sache des Kernels“, „Stufe 3 und Stufe 0: Sache des Prozessors“.
:::
::::

⁠**Kurz gesagt:** Die Privilegstufe ist ein Zustand des Prozessors, den kein Programm selbst umstellen kann.

### Die Schutzringe

<span class="anker" id="stufe-3-3"></span>

[Linux, Kapitel 1](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/ein-linux-zum-ueben.html) hat von zwei Betriebsarten gesprochen. Die Prozessoren in PCs kennen mehr Stufen, von denen Betriebssysteme aber nur zwei benutzen. Man stellt die Stufen gern als Ringe um einen Kern dar: Je weiter innen, desto mehr ist erlaubt.

:::definition Definition 3.2 (Schutzringe)
<span class="anker" id="satz-3-2"></span>

Die __Schutzringe__ sind die vier Privilegstufen 0 bis 3 eines x86-Prozessors. Stufe 0 ist die mächtigste, in ihr ist jeder Befehl erlaubt; Stufe 3 ist die schwächste. Linux und Windows benutzen nur zwei davon: Der Kernel läuft auf Stufe 0, alle Programme laufen auf Stufe 3.
:::

Der Kernel-Modus aus [Linux, Kapitel 1](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/ein-linux-zum-ueben.html) ist also Stufe 0, der Benutzermodus Stufe 3. Intels Handbuch für Systemprogrammierer empfiehlt genau das: Systeme, die nur zwei der vier Stufen benutzen, sollen die Stufen 0 und 3 nehmen. Abbildung [11](#abb-11) zeigt die Ringe.

:::abbildung cyber/k2ringe 11
Vier konzentrische Ringe mit den Zahlen 0 (innen) bis 3 (außen). Ring 0 erhält die Aufschrift „Kernel“, Ring 3 „Programme: Shell, Browser, auch Programme von root“. Die Ringe 1 und 2 werden grau und tragen „ungenutzt“. Ein Pfeil von außen nach innen trägt „nur durch kontrollierte Übergänge“.
:::

::::beispiel Wer auf welcher Stufe läuft
Auf Stufe 0 laufen der Linux-Kernel und seine Treiber. Auf Stufe 3 laufen die Shell, `cat`, `strace`, Python mit dem Programm `befehl.py`, der Dienstverwalter systemd mit der Prozessnummer 1 und jedes Programm, das mit `sudo` als root gestartet wurde.
::::

⁠**Kurz gesagt:** x86-Prozessoren haben vier Schutzringe, Betriebssysteme benutzen nur Ring 0 für den Kernel und Ring 3 für alle Programme.

:::hintergrund Warum nur Ring 0 und Ring 3 benutzt werden
Die vier Ringe gehören zur Segmentierung, einer älteren Art, Speicher einzuteilen, die 64-Bit-Betriebssysteme praktisch nicht mehr benutzen. Der Speicherschutz, mit dem heutige Systeme Programme voneinander trennen, kennt nur zwei Stufen: Zugriffe aus Stufe 3 gelten als Zugriffe eines Benutzers, Zugriffe aus den Stufen 0 bis 2 als Zugriffe des Systems. Die Ringe 1 und 2 brächten also keinen eigenen Schutz. Dazu kommt, dass Linux und Windows auch auf Prozessoren laufen, die von vornherein nur zwei Hauptbetriebsarten für Kernel und Programme haben, etwa ARM-Prozessoren in Handys. Ein Betriebssystem, das mit zwei Stufen auskommt, lässt sich leichter auf alle diese Prozessoren übertragen.
:::

:::hintergrund Andere Prozessoren und die Betriebsart für Gäste
Der offene Prozessorentwurf RISC-V kennt drei Betriebsarten: eine für die Firmware (machine mode), eine für den Kernel (supervisor mode) und eine für Programme (user mode). Das Prinzip ist dasselbe wie bei x86: Versucht ein Programm im user mode einen privilegierten Befehl, führt der Prozessor ihn nicht aus, sondern wechselt in den supervisor mode, damit der Kernel entscheiden kann.

Die Hardware-Virtualisierung aus [Linux, Kapitel 1, Abschnitt 3.4](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/virtuelle-maschinen-der-rechner-im-rechner.html#stufe-3-4) fügt bei x86 eine weitere Ebene hinzu: eine eigene Betriebsart, in der ein Gast-Kernel auf Stufe 0 seiner VM läuft, während der Hypervisor darüber die Kontrolle behält. Umgangssprachlich heißt die Ebene des Hypervisors manchmal „Ring $-1$“; einen solchen Ring gibt es in Intels Beschreibung nicht, es ist eine eigene Betriebsart.
:::

### Privilegierte Befehle

<span class="anker" id="stufe-3-4"></span>

Welche Befehle genau sind auf Stufe 3 gesperrt? Es sind nicht die gefährlich klingenden, sondern die, mit denen man die Grenzen selbst verstellen könnte. Tabelle [1](#tab-1) nennt einige davon mit ihrem Namen in Intels Handbuch.

<span class="anker" id="tab-1"></span>

**Tabelle 1:** Einige privilegierte Befehle eines x86-64-Prozessors. Auf Stufe 3 führt der Prozessor sie nicht aus. CLI ist auf Stufe 3 gesperrt, weil Linux und Windows eine zusätzliche Einstellung so setzen; diese Einstellung kann ihrerseits nur Stufe 0 ändern.

| Befehl | was er bewirkt | was ein Programm damit könnte |
|---|---|---|
| HLT | hält den Prozessor an, bis ein Gerät sich meldet | alle anderen Programme auf diesem Kern stilllegen |
| LIDT | legt fest, wohin der Prozessor bei bestimmten Ereignissen springt | eigenen Code an die Stelle des Kernels setzen |
| MOV in ein Steuerregister | stellt unter anderem ein, welchen Teil des Speichers ein Programm sieht | sich den Speicher fremder Programme und des Kernels sichtbar machen |
| WRMSR | schreibt besondere Einstellregister, darunter das Sprungziel für Systemaufrufe | jeden Systemaufruf in eigenen Code umleiten |
| CLI | hindert Geräte daran, den Prozessor zu unterbrechen | den Kern für sich behalten, sodass der Kernel nicht mehr drankommt |

:::satz Satz 3.3 (Was privilegiert ist)
<span class="anker" id="satz-3-3"></span>

Privilegiert ist jeder Befehl, mit dem ein Programm die Schutzgrenzen selbst verändern, umgehen oder abschalten könnte: Einstellungen des Speicherschutzes, Sprungziele in den Kernel, die Zuteilung des Prozessors und der direkte Zugriff auf Geräte.
:::

Gewöhnliche Rechenbefehle, Sprünge innerhalb des eigenen Programms und Zugriffe auf den eigenen Speicher sind nicht privilegiert. Deshalb läuft ein Programm die meiste Zeit mit voller Geschwindigkeit direkt auf dem Prozessor, ohne dass der Kernel jeden Befehl ansehen muss.

::::beispiel Warum gerade HLT gesperrt ist
HLT klingt harmlos, er hält den Prozessor nur an, bis sich ein Gerät meldet. Der Kernel benutzt ihn, wenn es nichts zu tun gibt, um Strom zu sparen. Dürfte jedes Programm ihn ausführen, könnte ein Programm den Kern anhalten, obwohl andere Programme warten, und zwar so oft es will. Der Befehl verändert also die Zuteilung des Prozessors, und das ist Sache des Kernels.
::::

⁠**Kurz gesagt:** Gesperrt sind genau die Befehle, mit denen man Speicherschutz, Sprungziele in den Kernel, die Zuteilung des Prozessors oder Geräte selbst einstellen könnte.

### Die Ausnahme und die Schutzverletzung

<span class="anker" id="stufe-3-5"></span>

Was geschieht, wenn ein Programm einen gesperrten Befehl trotzdem versucht? Der Prozessor kann ihn nicht ausführen, er kann ihn aber auch nicht einfach überspringen, als wäre nichts gewesen. Er braucht jemanden, der entscheidet.

:::definition Definition 3.4 (Ausnahme, Schutzverletzung)
<span class="anker" id="satz-3-4"></span>

Eine __Ausnahme__ ist ein Ereignis, bei dem der Prozessor den laufenden Befehl nicht ausführen kann. Der Prozessor unterbricht dann das Programm an diesem Befehl, wechselt auf Stufe 0 und springt an eine Stelle im Kernel, die für diese Art von Ausnahme vorgesehen ist. Eine __Schutzverletzung__ ist die Ausnahme, die ein x86-Prozessor bei einem auf der aktuellen Stufe verbotenen Befehl auslöst (englisch general protection fault, kurz #GP).
:::

Weitere Ausnahmen sind etwa eine Division durch null oder ein Zugriff auf eine Adresse, die das Programm nicht benutzen darf. Bei einer Schutzverletzung aus einem Programm heraus schickt Linux dem Prozess das Signal SIGSEGV; die Standardreaktion beendet ihn. Abbildung [12](#abb-12) zeigt den Ablauf.

:::abbildung cyber/k2ausnahme 12
Ein Programm auf Stufe 3 als Befehlsfolge; der Befehlszeiger wandert über zwei gewöhnliche Befehle und erreicht HLT. Der Befehl leuchtet rot auf, wird nicht ausgeführt, und ein Pfeil „Schutzverletzung“ führt auf Stufe 0 in den Kernel. Der Kernel schickt dem Prozess „SIGSEGV“, der Prozess wird beendet, und die Shell meldet `Segmentation fault` und den Status 139.
:::

::::beispiel Ein Programm versucht HLT
Das Programm `befehl.py` aus Unterabschnitt [2.4](code-und-daten-im-selben-speicher.html#stufe-2-4) kennt neben `rechnen` eine zweite Art: `anhalten` schreibt die Bytes `F4 C3` in den Speicher, also HLT und den Rücksprung, und setzt den Befehlszeiger darauf.

```console
$ python3 befehl.py anhalten
Segmentation fault         python3 befehl.py anhalten
$ echo $?
139
```

Der Prozessor hat HLT auf Stufe 3 nicht ausgeführt, sondern eine Schutzverletzung ausgelöst. Der Kernel hat daraufhin das Signal SIGSEGV geschickt, und $139=128+11$ zeigt, dass der Prozess daran geendet ist. Der Prozessor ist dabei nicht angehalten worden; alle anderen Programme liefen ungestört weiter.
::::

⁠**Kurz gesagt:** Kann der Prozessor einen Befehl nicht ausführen, löst er eine Ausnahme aus und übergibt dem Kernel die Entscheidung; bei einem verbotenen Befehl beendet Linux das Programm mit SIGSEGV.

:::hintergrund Warum die Hardware erkennt und der Kernel entscheidet
Der Prozessor erkennt den verbotenen Befehl, aber er beendet das Programm nicht selbst. Er übergibt nur an den Kernel. Das ist die Trennung von Mechanismus und Richtlinie aus [Kapitel 1, Abschnitt 4](/wissen/informatik/cybersecurity/sicherheit-schutzziele-und-spielregeln/richtlinie-und-mechanismus.html#stufe-4): Die Hardware liefert den Mechanismus, der Kernel legt fest, was im Einzelfall geschehen soll. Linux schickt ein Signal, das ein Programm abfangen könnte, etwa um vor dem Ende noch eine Fehlermeldung zu schreiben. Ein Hypervisor dagegen lässt sich auf ähnliche Weise bei bestimmten Befehlen eines Gast-Kernels rufen und bildet sie für ihn nach. Ein Prozessor, der bei jedem verbotenen Befehl fest „beenden“ verdrahtet hätte, ließe beides nicht zu.
:::

### Aufgaben zu Abschnitt [3](#stufe-3)

<span class="anker" id="stufe-3-6"></span>

:::aufgabe Aufgabe 5 ★ Auf welcher Stufe?
<span class="anker" id="aufg-5"></span>

Auf welcher Privilegstufe laufen: (a) der Treiber der Netzwerkkarte, (b) `sudo apt update`, (c) systemd mit der Prozessnummer 1, (d) der Teil des Kernels, der entscheidet, welcher Prozess als Nächstes rechnet, (e) ein Programm, das ein Angreifer mit den Rechten von root gestartet hat? Was folgt aus (e) für die Aussage „root kann alles“?

:::loesung
(a) Stufe 0: Treiber gehören zum Kernel. (b) Stufe 3: `sudo` und `apt` sind gewöhnliche Programme, auch wenn `apt` dann mit den Rechten von root läuft. (c) Stufe 3: systemd ist ein Programm, nur eben das erste. (d) Stufe 0: Der Planer ist Teil des Kernels. (e) Stufe 3.

„root kann alles“ stimmt also nur im Sinne des Betriebssystems: Der Kernel überspringt für root fast alle Rechteprüfungen. Der Prozessor sperrt für root dieselben Befehle wie für jeden. Allerdings kann root den Kernel bitten, Code auf Stufe 0 zu bringen, etwa indem er ein Kernelmodul laden lässt. Deshalb laden viele Distributionen bei eingeschaltetem Secure Boot nur Kernelmodule mit gültiger Signatur. Für die Sicherheit heißt das: Wer root wird, steht nur noch eine Bitte an den Kernel von Stufe 0 entfernt.
:::
:::

:::aufgabe Aufgabe 6 ★★ Gesperrt oder nicht?
<span class="anker" id="aufg-6"></span>

Entscheide für jeden Befehl, ob er privilegiert sein muss, und begründe mit dem Satz „Was privilegiert ist“: (a) zwei Register addieren, (b) festlegen, welchen Teil des Speichers ein Programm sieht, (c) an eine Adresse im eigenen Programm springen, (d) festlegen, wohin ein Systemaufruf springt, (e) eine Zahl aus dem eigenen Speicher in ein Register laden, (f) den Prozessor anhalten.

:::loesung
(a) Nicht privilegiert: Rechnen in Registern verstellt keine Grenze. (b) Privilegiert: Wer festlegt, welchen Speicher er sieht, kann sich jeden Speicher sichtbar machen; das ist eine Einstellung des Speicherschutzes. (c) Nicht privilegiert: Ein Sprung innerhalb des eigenen Programms bleibt auf Stufe 3 und im eigenen Speicher. (d) Privilegiert: Das ist ein Sprungziel in den Kernel; wer es setzen könnte, landete beim nächsten Systemaufruf mit Stufe 0 in eigenem Code. (e) Nicht privilegiert: ein Zugriff auf den eigenen Speicher. (f) Privilegiert: Anhalten greift in die Zuteilung des Prozessors ein, siehe das Beispiel zu HLT.
:::
:::

:::aufgabe Aufgabe 7 ★★ Eine Schutzverletzung beobachten
<span class="anker" id="aufg-7"></span>

Führe `python3 befehl.py anhalten` aus und frage danach mit `echo $?` den Exit-Status ab. Erkläre jede Stufe der Kette vom Befehl HLT bis zur Zahl, die die Shell zeigt. Was wäre geschehen, wenn derselbe Befehl im Kernel ausgeführt worden wäre?

:::loesung
Auf dem Testsystem endete der Versuch mit `Segmentation fault` und dem Status 139. Die Kette:

<ol>

<li>

Python setzt den Befehlszeiger auf das Speicherstück mit den Bytes `F4 C3`.

</li>

<li>

Der Prozessor holt `F4`, den Befehl HLT. Die aktuelle Privilegstufe ist 3, HLT ist privilegiert, also führt er ihn nicht aus.

</li>

<li>

Stattdessen löst er eine Schutzverletzung aus, eine Ausnahme: Er sichert den Stand, wechselt auf Stufe 0 und springt an die Einsprungstelle des Kernels für Schutzverletzungen.

</li>

<li>

Der Kernel stellt fest, dass die Ausnahme von Stufe 3 kam, und schickt dem Prozess das Signal SIGSEGV (Nummer 11).

</li>

<li>

Python hat für SIGSEGV keine eigene Reaktion festgelegt, also gilt die Standardreaktion: beenden. Ein Speicherabbild wurde auf dem Testsystem nicht geschrieben, weil seine Größe dort auf 0 begrenzt ist.

</li>

<li>

Die Shell erfährt, dass ihr Kindprozess durch das Signal 11 endete, schreibt `Segmentation fault` und setzt den Exit-Status auf $128+11=139$.

</li>

</ol>

Im Kernel, auf Stufe 0, wäre HLT einfach ausgeführt worden: Der Kern hätte angehalten, bis sich das nächste Gerät meldet. Genau so benutzt der Kernel den Befehl, wenn es nichts zu tun gibt.
:::
:::

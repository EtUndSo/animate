---
title: Der Eintritt in den Kernel
pfad: Informatik / Cybersecurity / Schutzgrenzen in Hardware und Betriebssystem
adresse: informatik/cybersecurity/schutzgrenzen-in-hardware-und-betriebssystem
knoten: Kapitel 2: Schutzgrenzen in Hardware und Betriebssystem
order: 6120500
summary: Ein Programm auf Stufe 3 muss regelmäßig in den Kernel, sei es, weil es einen Dienst braucht, weil sein Befehl nicht ausführbar war oder weil ein Gerät sich meldet.
tags: Einsprungstelle, Einsprungtabelle, Eintritt in den Kernel, Unterbrechung, Rückkehr in den Benutzermodus, Prüfung der Argumente
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Ein Programm auf Stufe 3 muss regelmäßig in den Kernel, sei es, weil es einen Dienst braucht, weil sein Befehl nicht ausführbar war oder weil ein Gerät sich meldet. Dieser Abschnitt zeigt, wie dieser Wechsel abläuft, warum das Programm das Ziel nicht wählen kann und wie der Kernel mit dem umgeht, was das Programm mitbringt.
:::

### Die Einsprungstelle und die Einsprungtabelle

<span class="anker" id="stufe-4-1"></span>

Beim Wechsel auf Stufe 0 springt der Prozessor in den Kernel. Wohin genau, darf nicht das Programm bestimmen, sonst könnte es mitten in eine Kernel-Funktion springen, hinter die Stelle, an der geprüft wird. [Linux, Kapitel 1, Abschnitt 1.4](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/betriebssystem-kernel-und-distribution.html#stufe-1-4) hat das als Hintergrund erklärt; hier folgt, wie der Prozessor das Ziel findet.

Man kann sich die Telefonzentrale einer großen Firma vorstellen. Ein Anrufer kann nicht direkt am Schreibtisch eines Mitarbeiters klingeln; er wählt die Nummer der Zentrale und nennt sein Anliegen, und die Zentrale entscheidet, wohin sie verbindet (ein Bild zur Orientierung).

:::definition Definition 4.1 (Einsprungstelle, Einsprungtabelle)
<span class="anker" id="satz-4-1"></span>

Eine __Einsprungstelle__ ist eine Adresse im Kernel, an die der Prozessor beim Wechsel auf Stufe 0 springt. Der Kernel trägt seine Einsprungstellen beim Start in die __Einsprungtabelle__ ein, eine Liste mit einer Stelle je Art von Ereignis, deren Ort er dem Prozessor mitteilt. Bei x86-Prozessoren heißt sie Interrupt-Deskriptor-Tabelle (IDT); ihren Ort setzt der privilegierte Befehl LIDT. Für den Befehl `syscall`, mit dem Programme auf x86-64 Systemaufrufe stellen, steht die Einsprungstelle in einem eigenen Einstellregister mit dem Namen IA32_LSTAR, das nur der privilegierte Befehl WRMSR beschreiben kann.
:::

Das Programm nennt nie eine Adresse im Kernel. Bei einem Systemaufruf legt es nur die Nummer des Dienstes in das Register `rax`, die übrigen Angaben in weitere Register, und führt `syscall` aus. Der Prozessor setzt die Stufe auf 0, merkt sich, wo das Programm stand, und lädt den Befehlszeiger aus IA32_LSTAR. An dieser Stelle liest der Kernel die Nummer aus `rax` und schlägt in seiner Tabelle der Dienste nach. Abbildung [13](#abb-13) zeigt beide Tabellen.

:::abbildung cyber/k2einsprung 13
Links ein Programm auf Stufe 3, das in `rax` die Nummer 1 legt und `syscall` ausführt. In der Mitte der Prozessor mit dem Register IA32_LSTAR, in dem eine Kerneladresse steht (Aufschrift „beim Start vom Kernel eingetragen“). Der Befehlszeiger springt an diese Adresse auf Stufe 0. Rechts der Kernel mit seiner „Tabelle der Dienste“: 0 read, 1 write, 2 open, …, 60 exit; die Zeile 1 leuchtet auf. Darunter die Einsprungtabelle IDT mit Zeilen „Division durch null“, „Schutzverletzung“, „Gerät meldet sich“.
:::

::::beispiel Was bei einem Systemaufruf write geschieht
`cat` gibt sechs Bytes aus, indem es den Dienst `write` mit der Nummer 1 aufruft. Es legt 1 in `rax`, den Deskriptor 1 der Standardausgabe ([Linux, Kapitel 4, Abschnitt 1.7](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/prozesse-und-ihre-drei-strome.html#stufe-1-7)), die Adresse der Bytes und die Zahl 6 in drei weitere Register und führt `syscall` aus. Der Prozessor sichert die Adresse des folgenden Befehls im Register `rcx` und die aktuellen Zustandsbits im Register `r11`, setzt die Stufe auf 0 und springt an die Adresse aus IA32_LSTAR. Der Kernel findet unter der Nummer 1 seine Funktion für `write`, prüft die Angaben und gibt die Bytes aus. Wo die Einsprungstelle liegt, hat der Kernel beim Start festgelegt, als noch kein Programm lief.
::::

⁠**Kurz gesagt:** Beim Wechsel in den Kernel springt der Prozessor nur an Stellen, die der Kernel selbst eingetragen hat, und eintragen kann man sie nur auf Stufe 0.

### Drei Wege in den Kernel

<span class="anker" id="stufe-4-2"></span>

Der Systemaufruf ist nicht der einzige Anlass, auf Stufe 0 zu wechseln. Die Ausnahme aus Unterabschnitt [3.5](privilegstufen-und-schutzringe.html#stufe-3-5) führt ebenfalls in den Kernel, und es gibt noch einen dritten Anlass, der gar nichts mit dem laufenden Programm zu tun hat.

:::definition Definition 4.2 (Eintritt in den Kernel, Unterbrechung)
<span class="anker" id="satz-4-2"></span>

Ein __Eintritt in den Kernel__ ist jeder Wechsel des Prozessors von Stufe 3 auf Stufe 0. Es gibt ihn auf drei Wegen:

<ol>

<li>

als *Systemaufruf*: Das Programm bittet absichtlich um einen Dienst (bei x86-64 mit `syscall`);

</li>

<li>

als *Ausnahme*: Der laufende Befehl kann nicht ausgeführt werden;

</li>

<li>

als __Unterbrechung__: Ein Gerät meldet dem Prozessor ein Ereignis, etwa eine gedrückte Taste oder ein angekommenes Datenpaket, unabhängig davon, welcher Befehl gerade läuft.

</li>

</ol>

In allen drei Fällen springt der Prozessor an eine Einsprungstelle, die der Kernel eingetragen hat.
:::

Englische Texte benutzen für diese Fälle die Wörter *system call*, *exception* und *interrupt*, dazu das Wort *trap*, das je nach Buch einen, zwei oder alle drei Fälle meint. Dieses Kapitel bleibt bei „Eintritt in den Kernel“ als Oberbegriff. Abbildung [14](#abb-14) zeigt die drei Wege.

:::abbildung cyber/k2dreiwege 14
Oben ein Programm auf Stufe 3, unten der Kernel auf Stufe 0, dazwischen die Grenze. Nacheinander laufen drei Pfeile nach unten: „Systemaufruf (`syscall`)“ vom Programm, „Ausnahme (Befehl nicht ausführbar)“ vom Programm, „Unterbrechung (Gerät meldet sich)“ von einer Tastatur am Rand. Alle drei treffen auf die Einsprungtabelle und landen an eingetragenen Stellen im Kernel. Zum Schluss ein gemeinsamer Pfeil zurück nach oben: „Rückkehr“.
:::

::::beispiel Eine Minute an der Tastatur
Jemand tippt in einem Textprogramm. Jeder Tastendruck löst eine Unterbrechung aus: Die Tastatur meldet sich, egal, was der Prozessor gerade rechnet. Das Textprogramm liest die Taste mit einem Systemaufruf. Hat das Programm einen Fehler und teilt eine ganze Zahl durch null, löst der Befehl eine Ausnahme aus. Alle drei Ereignisse führen in den Kernel, aber nur eines davon hat das Programm gewollt.
::::

⁠**Kurz gesagt:** In den Kernel gelangt man durch einen Systemaufruf, eine Ausnahme oder eine Unterbrechung, und jedes Mal springt der Prozessor an eine Stelle, die der Kernel eingetragen hat.

### Die Rückkehr in den Benutzermodus

<span class="anker" id="stufe-4-3"></span>

Hat der Kernel seine Arbeit getan, muss das Programm genau dort weiterlaufen, wo es stand, und wieder auf Stufe 3.

:::definition Definition 4.3 (Rückkehr in den Benutzermodus)
<span class="anker" id="satz-4-3"></span>

Die __Rückkehr in den Benutzermodus__ geschieht mit einem besonderen Befehl, der den beim Eintritt gesicherten Befehlszeiger und die gesicherten Zustandsbits wiederherstellt und die Stufe auf 3 setzt (bei x86-64 in der Regel `sysret` nach einem Systemaufruf, sonst `iretq`). Das Ergebnis eines Systemaufrufs legt der Kernel vorher in das Register `rax`.
:::

Die Rückkehr kann nie zu mehr Rechten führen. Wohin sie führt, bestimmt der Kernel: Er hat die Stelle des Programms beim Eintritt gesichert und gibt sie zurück. Nach einer Schutzverletzung kehrt er gar nicht zu dem verbotenen Befehl zurück, sondern beendet den Prozess. Abbildung [15](#abb-15) zeigt Hin- und Rückweg eines Systemaufrufs.

:::abbildung cyber/k2rueckkehr 15
Oben das Programm auf Stufe 3 mit dem Register `rip` an `syscall`, unten der Kernel auf Stufe 0. Beim Eintritt wandern zwei Werte in Kästchen: „Adresse des nächsten Befehls → `rcx`“, „Zustandsbits → `r11`“; die Stufe springt auf 0. Der Kernel arbeitet kurz (grauer Balken) und legt „6“ in `rax`. Dann die Rückkehr mit `sysret`: `rip` bekommt den Wert aus `rcx`, die Zustandsbits kommen aus `r11` zurück, die Stufe springt auf 3, und das Programm läuft am Befehl hinter `syscall` weiter. Am Rand eine Zeile wie bei `strace`: `write(1, …, 6) = 6`.
:::

::::beispiel Das Ergebnis in der Mitschrift von strace
`strace` zeigt für jeden Systemaufruf nach dem Gleichheitszeichen das Ergebnis, das der Kernel bei der Rückkehr in `rax` gelegt hat. In [Linux, Kapitel 1, Abschnitt 1.4](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/betriebssystem-kernel-und-distribution.html#stufe-1-4) stand bei `read(3, "labor\n", 262144) = 6` die Zahl 6 für sechs gelesene Bytes. Lehnt der Kernel einen Aufruf ab, legt er eine negative Fehlernummer in `rax`. `strace` schreibt dann $-1$ und den Namen des Fehlers, etwa `EFAULT`; unter diesem Fehlercode kann das Programm den Grund danach abfragen.
::::

⁠**Kurz gesagt:** Die Rückkehr stellt den gesicherten Stand des Programms wieder her, setzt die Stufe zurück auf 3 und liefert das Ergebnis.

:::hintergrund Warum der Kernel einen eigenen Stapel braucht
Während der Kernel arbeitet, braucht er Platz für Zwischenwerte, etwa für die gesicherten Register und für die Daten seiner Funktionen. Dafür benutzt jedes Programm einen Speicherbereich, den man Stapel nennt. Der Kernel darf den Stapel des Programms aber nicht verwenden: Das Programm könnte ihn auf eine unsinnige Adresse gestellt haben oder, auf einem zweiten Kern, gleichzeitig hineinschreiben. Deshalb hat jeder Prozess zusätzlich einen kleinen Kernel-Stapel im Speicher des Kernels, auf den das Programm keinen Zugriff hat, und beim Eintritt wird als Erstes auf ihn umgeschaltet, bei Unterbrechungen und Ausnahmen schon vom Prozessor selbst. So hängt nichts, was der Kernel während seiner Arbeit ablegt, von Werten ab, die das Programm kontrolliert.
:::

### Die Prüfung der Argumente

<span class="anker" id="stufe-4-4"></span>

Ein Systemaufruf bringt Angaben mit: Nummern, Längen und Adressen. Der Kernel arbeitet mit allen Rechten, und er arbeitet im Auftrag des Programms. Würde er einer Adresse, die das Programm nennt, einfach folgen, könnte ein Programm ihn bitten, „sechs Bytes ab dieser Adresse auszugeben“, und als Adresse eine Stelle im Speicher des Kernels angeben. Der Kernel würde dann seine eigenen Daten für das Programm lesen.

:::definition Definition 4.4 (Prüfung der Argumente)
<span class="anker" id="satz-4-4"></span>

Bei der __Prüfung der Argumente__ behandelt der Kernel jede Angabe eines Systemaufrufs als möglicherweise bösartig. Adressen, die das Programm übergibt, benutzt er nur über eigene Kopierfunktionen. Diese prüfen zuerst, ob der ganze genannte Bereich in dem Teil der Adressen liegt, der Programmen vorbehalten ist, und brechen beim Kopieren ab, wenn dort an einer Adresse kein Speicher des Programms liegt. Schlägt die Prüfung fehl, lehnt der Kernel den Aufruf mit dem Fehlercode `EFAULT` („Bad address“) ab.
:::

Unter Linux heißen diese Kopierfunktionen `copy_from_user` und `copy_to_user`; die Bereichsprüfung davor heißt `access_ok`. Auf x86-64 ist sie einfach, denn Linux trennt die Adressen in zwei Hälften: Programme benutzen nur Adressen unterhalb von `0x0000800000000000`, der Kernel nur Adressen ab `0xffff800000000000`. Abbildung [16](#abb-16) zeigt die Prüfung.

:::abbildung cyber/k2argumente 16
Ein Systemaufruf `write(1, Adresse, 6)` wird dreimal gestellt. Oben eine Adressleiste mit der Hälfte „Programm“ links und der Hälfte „Kernel“ rechts, darunter eine Tabelle mit Adresse, Bereichsprüfung, Kopieren und Ergebnis jedes Aufrufs. Erster Aufruf: Adresse im eigenen Text des Programms, die Prüfung zeigt ein Häkchen, `Hallo` erscheint. Zweiter Aufruf: Adresse `0`, die Bereichsprüfung lässt sie durch, beim Kopieren findet sich dort kein Speicher, Ergebnis `EFAULT`. Dritter Aufruf: Adresse `0xffffffff81000000` in der Kernelhälfte, die Bereichsprüfung weist sie sofort ab, Ergebnis `EFAULT`. Unten stehen die drei Zeilen, die `tuer.py` dabei wirklich ausgibt.
:::

Das zweite kleine Programm dieses Kapitels stellt genau diese drei Aufrufe. In einem Satz: Es bittet den Kernel dreimal, sechs Bytes auszugeben, jedes Mal ab einer anderen Adresse, und zeigt seine Antwort. Wie `befehl.py` benutzt du es als Rezept, und wie dieses ist es harmlos: Es stellt nur Anfragen, die jedes Programm stellen darf. Lege es als `tuer.py` an:

```python tuer.py
# tuer.py: übergibt dem Kernel beim Systemaufruf write drei verschiedene Adressen
# und zeigt, was der Kernel daraus macht. Nur für Linux.
import ctypes, os

libc = ctypes.CDLL(None, use_errno=True)
libc.write.argtypes = [ctypes.c_int, ctypes.c_void_p, ctypes.c_size_t]

text = ctypes.create_string_buffer(b"Hallo\n")    # sechs Bytes im eigenen Speicher
adressen = [("eigener Text", ctypes.addressof(text)),
            ("Adresse 0", 0),
            ("Kerneladresse", 0xffffffff81000000)]

for name, adresse in adressen:
    print(f"{name:14} {adresse:#018x}:", end=" ", flush=True)
    n = libc.write(1, adresse, 6)               # Systemaufruf: 6 Bytes ab adresse ausgeben
    if n < 0:
        print("abgelehnt:", os.strerror(ctypes.get_errno()))
```

::::beispiel Der Kernel liest nicht für das Programm
```console
$ strace -o spur.txt -e trace=write python3 tuer.py
eigener Text   0x00007e284d0e27a0: Hallo
Adresse 0      0x0000000000000000: abgelehnt: Bad address
Kerneladresse  0xffffffff81000000: abgelehnt: Bad address
$ grep EFAULT spur.txt
write(1, NULL, 6)                       = -1 EFAULT (Bad address)
write(1, 0xffffffff81000000, 6)         = -1 EFAULT (Bad address)
```

Die Option `-o spur.txt` schreibt die Mitschrift von `strace` in eine Datei, `-e trace=write` beschränkt sie auf den Dienst `write`. Beim eigenen Text gibt der Kernel die sechs Bytes aus. Die Adresse 0 gehört zwar zur Hälfte der Programme, aber dort hat das Programm keinen Speicher; der Kernel merkt es beim Kopieren und lehnt ab (`strace` schreibt die Adresse 0 als `NULL`). Die Kerneladresse weist schon die Bereichsprüfung ab. In keinem Fall ist das Programm abgestürzt, und in keinem Fall hat der Kernel etwas aus seinem eigenen Speicher verraten.
::::

⁠**Kurz gesagt:** Der Kernel folgt keiner Adresse, die ein Programm ihm nennt, ohne zu prüfen, dass sie in den Speicher des Programms zeigt.

:::hintergrund Warum der Kernel erst kopiert und dann prüft
Viele Systemaufrufe bekommen nicht nur eine Adresse, sondern einen ganzen Block von Angaben im Speicher des Programms, etwa einen Dateinamen. Der Kernel kopiert solche Angaben zuerst in seinen eigenen Speicher und prüft und benutzt danach nur noch die Kopie. Würde er den Dateinamen im Speicher des Programms prüfen und später ein zweites Mal von dort lesen, könnte das Programm ihn auf einem zweiten Kern genau dazwischen austauschen: Geprüft würde ein erlaubter Name, benutzt ein verbotener. Das ist der Fehler „Prüfen und Handeln nicht im selben Moment“ aus [Kapitel 1, Abschnitt 5.6](/wissen/informatik/cybersecurity/sicherheit-schutzziele-und-spielregeln/sicherheitsprinzipien-rechte-vergeben-und-prufen.html#stufe-5-6). Die Kopie im Kernel kann das Programm nicht mehr verändern, also gilt die Prüfung für genau das, was benutzt wird.
:::

### Der Systemaufruf als einzige Tür

<span class="anker" id="stufe-4-5"></span>

Jetzt lässt sich begründen, warum der Kernel die erste Forderung an einen Referenzmonitor erfüllt.

:::satz Satz 4.5 (Die einzige Tür)
<span class="anker" id="satz-4-5"></span>

Code auf Stufe 0 beginnt nach dem Start des Kernels nur an Einsprungstellen, die der Kernel selbst eingetragen hat, und die Orte dieser Stellen lassen sich nur auf Stufe 0 ändern. Ein Programm kann deshalb nur über einen Systemaufruf etwas vom Kernel verlangen, und dort prüft der Kernel. Die Forderung „immer aufgerufen“ ist für alles erfüllt, was nur der Kernel tun kann.
:::

Die Rechteprüfung beim Öffnen einer Datei aus [Linux, Kapitel 7, Abschnitt 5.3](/wissen/informatik/linux-und-kommandozeile/benutzer-gruppen-und-rechte/wie-der-kernel-rechte-pruft.html#stufe-5-3) sitzt genau hinter dieser Tür: im Systemaufruf, der die Datei öffnet. Dass ein Programm die Datei nicht stattdessen direkt vom Datenträger liest, stellt der Prozessor sicher, denn der direkte Zugriff auf Geräte ist privilegiert. Abbildung [17](#abb-17) fasst zusammen, welche Wege es gibt und welche versperrt sind.

:::abbildung cyber/k2einzigetuer 17
Oben Programme auf Stufe 3, unten Kernel und Geräte auf Stufe 0. Vier Versuche eines Programms laufen nacheinander nach unten: „direkt auf das Gerät“ (prallt am Prozessor ab, privilegiert), „mitten in eine Kernel-Funktion springen“ (prallt ab, keine eingetragene Stelle), „Einsprungtabelle umschreiben“ (prallt ab, nur Stufe 0), „Systemaufruf“ (geht durch die Tür an der eingetragenen Stelle und trifft dort auf die Prüfung). Zum Schluss leuchtet nur noch die Tür.
:::

::::beispiel Wie oft ein kleiner Befehl durch die Tür geht
`strace -c` zählt die Systemaufrufe eines Programms, statt jeden einzeln aufzuschreiben, und gibt am Ende eine Tabelle aus. Die letzte Zeile enthält die Summe:

```console
$ strace -c ls / > /dev/null 2> zaehlung.txt
$ tail -n 1 zaehlung.txt
100.00    0.000000           0       148        10 total
```

Die Ausgabe von `ls` geht nach `/dev/null`, die Tabelle von `strace` mit `2>` in eine Datei. Das Auflisten eines einzigen Verzeichnisses brauchte 148 Systemaufrufe; 10 davon hat der Kernel mit einem Fehlercode beantwortet, meist weil eine gesuchte Datei nicht existierte. Jeder Zugriff auf das Verzeichnis, jede Ausgabe und jede geladene Programmbibliothek ging durch die Tür. Die Zahlen sind bei dir etwas anders.
::::

⁠**Kurz gesagt:** Weil der Kernel nur an selbst eingetragenen Stellen betreten werden kann, kommt kein Programm an seiner Prüfung vorbei.

:::hintergrund Warum eine einzige Tür genügt
Die Privilegstufe ist ein Zustand des Prozessors, und auf Stufe 0 wechselt er nur bei einem Eintritt in den Kernel. Jeder Eintritt führt an eine eingetragene Stelle. Daraus folgt: Jeder Befehl, der nach dem Start auf Stufe 0 läuft, gehört zu einer Folge, die an einer vom Kernel gewählten Stelle begonnen hat. Der Kernel kann an jeder dieser Stellen zuerst prüfen, bevor er etwas tut. Es gibt keinen Weg, mitten in seinen Code zu gelangen, also auch keinen Weg hinter eine Prüfung. Damit diese Kette hält, müssen die Einsprungtabelle und die Tabelle der Dienste selbst geschützt sein; sie liegen im Speicher des Kernels, den Programme nicht beschreiben können. Ein einziger Fehler im Kernel, etwa eine vergessene Prüfung in einem seiner mehreren Hundert Dienste, öffnet allerdings ein Loch in der Tür selbst. Deshalb gehört der ganze Kernel zur vertrauenswürdigen Basis.
:::

### Aufgaben zu Abschnitt [4](#stufe-4)

<span class="anker" id="stufe-4-6"></span>

:::aufgabe Aufgabe 8 ★ Welcher Weg?
<span class="anker" id="aufg-8"></span>

Ordne jedes Ereignis einem der drei Wege in den Kernel zu: (a) Ein Programm öffnet eine Datei. (b) Die Netzwerkkarte hat ein Datenpaket empfangen. (c) Ein Programm führt CLI aus. (d) Ein Programm beendet sich mit dem Dienst `exit`. (e) Ein Programm teilt eine ganze Zahl durch null. (f) Die Maus wurde bewegt. Bei welchen Ereignissen kehrt der Kernel danach zu genau dem Befehl zurück, der gerade lief, oder zum Befehl dahinter?

:::loesung
(a) Systemaufruf. (b) Unterbrechung. (c) Ausnahme, und zwar eine Schutzverletzung. (d) Systemaufruf. (e) Ausnahme. (f) Unterbrechung.

Nach einer Unterbrechung kehrt der Kernel zu dem Befehl zurück, der als Nächstes an der Reihe gewesen wäre; das Programm merkt nichts. Nach einem Systemaufruf kehrt er zum Befehl hinter `syscall` zurück, mit dem Ergebnis in `rax`; bei `exit` (d) kehrt er gar nicht zurück, weil der Prozess endet. Nach den Ausnahmen in (c) und (e) beendet Linux das Programm mit einem Signal, sofern das Programm das Signal nicht abfängt; dann kehrt der Kernel nicht zu dem Befehl zurück. Bei einem Seitenfehler auf eine erlaubte, nur noch nicht geladene Seite kehrt er dagegen zu genau dem Befehl zurück, der den Fehler auslöste, und lässt ihn noch einmal laufen.
:::
:::

:::aufgabe Aufgabe 9 ★★ Systemaufrufe zählen
<span class="anker" id="aufg-9"></span>

Zähle wie im Beispiel „Wie oft ein kleiner Befehl durch die Tür geht“ die Systemaufrufe von `date`; schreibe die Tabelle dabei mit `2> zaehlung2.txt` in eine eigene Datei. Vergleiche mit `ls /`. Woran könnte es liegen, dass ein Programm, das nur die Uhrzeit ausgibt, so viele braucht? Schau dir dazu die ganze Tabelle mit `cat zaehlung2.txt` an.

:::loesung
Auf dem Testsystem:

```console
$ strace -c date > /dev/null 2> zaehlung2.txt
$ tail -n 1 zaehlung2.txt
100.00    0.005431          23       236         8 total
```

`date` brauchte 236 Systemaufrufe, `ls /` nur 148. Die ganze Tabelle zeigt, woher sie kommen. Sie ist nach dem Zeitanteil sortiert, deshalb wechselt die Reihenfolge der Zeilen von Lauf zu Lauf; die ersten Zeilen eines Laufs:

```text
% time     seconds  usecs/call     calls    errors syscall
------ ----------- ----------- --------- --------- ------------------
 16.52    0.000897          27        33         4 openat
 14.40    0.000782          24        32           getdents64
 14.25    0.000774          25        30           mmap
 11.71    0.000636          31        20           read
 10.51    0.000571          19        29           close
```

Das Programm versucht 33-mal, eine Datei zu öffnen (`openat`, davon 4-mal vergeblich), und liest 32-mal den Inhalt eines Verzeichnisses (`getdents64`). Um eine Uhrzeit richtig auszugeben, braucht es Angaben zur Zeitzone und zur Spracheinstellung, und die liegen in Dateien und Verzeichnissen des Systems. Dazu kommen wie bei jedem Programm die Aufrufe zum Laden der Bibliotheken (`mmap`, `mprotect`). Die eigentliche Arbeit, die Uhr abzufragen, ist ein winziger Teil. Die Zahlen hängen von der Fassung des Programms ab; auf einem System mit der GNU-Fassung von `date` sind sie anders.
:::
:::

:::aufgabe Aufgabe 10 ★★★ Wenn niemand die Bytes liest
<span class="anker" id="aufg-10"></span>

Lenke die Ausgabe von `tuer.py` nach `/dev/null` um und schreibe die Mitschrift in eine zweite Datei:

```console
$ strace -o spur2.txt -e trace=write python3 tuer.py > /dev/null
$ grep -E 'NULL|EFAULT' spur2.txt
write(1, NULL, 6)                       = 6
write(1, 0xffffffff81000000, 6)         = -1 EFAULT (Bad address)
```

Bei der Adresse 0 meldet der Kernel jetzt Erfolg, bei der Kerneladresse weiterhin `EFAULT`. Erkläre mit der Definition der Prüfung der Argumente, warum. Ist das eine Lücke?

:::loesung
Die Prüfung der Argumente hat zwei Teile, und die beiden Adressen scheitern an verschiedenen Teilen.

<ul>

<li>

Die Bereichsprüfung kommt sofort am Anfang des Systemaufrufs: Liegt der ganze Bereich in der Hälfte der Programme? Die Kerneladresse liegt in der Kernelhälfte und scheitert hier, egal wohin die Ausgabe geht. Deshalb bleibt es bei `EFAULT`.

</li>

<li>

Die Adresse 0 liegt in der Hälfte der Programme und besteht die Bereichsprüfung. Ob dort wirklich Speicher ist, merkt der Kernel erst, wenn er mit seiner Kopierfunktion die Bytes holt. Geht die Ausgabe an ein Terminal, holt er sie und scheitert mit `EFAULT`. Geht sie nach `/dev/null`, wirft der Kernel die Bytes weg, ohne sie je zu lesen, und meldet einfach, dass er 6 Bytes „geschrieben“ hat.

</li>

</ul>

Eine Lücke ist das nicht. Die Prüfung soll verhindern, dass der Kernel für ein Programm in Speicher greift, der ihm nicht gehört, vor allem in den eigenen. Das hat er in keinem Fall getan: Die Kerneladresse hat er nie benutzt, und bei der Adresse 0 hat er gar nichts gelesen. Ein Programm erfährt dadurch nichts, was es nicht ohnehin wüsste.
:::
:::

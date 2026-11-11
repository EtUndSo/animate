---
title: Das System erkunden
pfad: Informatik / Linux und Kommandozeile / Die Shell: erste Befehle
adresse: informatik/linux-und-kommandozeile/die-shell-erste-befehle
knoten: Kapitel 2: Die Shell: erste Befehle
order: 6070700
summary: Mit Befehl, Optionen und Hilfe ausgestattet, kannst du dein System befragen.
tags: 
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Mit Befehl, Optionen und Hilfe ausgestattet, kannst du dein System befragen. Dieser Abschnitt stellt eine Handvoll Befehle vor, die jeder Linux-Rechner kennt: Sie nennen den Kernel und die Distribution, den Benutzer, Datum und Laufzeit, den Arbeitsspeicher und den Platz auf den Datenträgern. Zusammen ergeben sie einen Steckbrief des Rechners.
:::

### Kernel und Distribution

<span class="anker" id="stufe-6-1"></span>

Bei einem Problem fragt jede Anleitung und jedes Hilfeforum zuerst: Welcher Kernel, welche Distribution? Zwei Befehle beantworten das.

:::abbildung linux/k2uname 24
Die Ausgabe von `uname -a` zerlegt: Name des Kernels, Name des Rechners, Version des Kernels, Angaben zum Bau des Kernels mit Datum, Typ des Prozessors und Name des Betriebssystems.
:::

Die Option `-a`, lang `--all`, lässt `uname` alle seine Angaben in einer Zeile ausgeben. Den Namen der Distribution schreibt der Kernel nicht hin, denn er kennt ihn nicht; er steht in der Datei `/etc/os-release` ([Kapitel 1, Abschnitt 2.3](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/drei-wege-zu-einem-eigenen-linux.html#stufe-2-3)), unter Ubuntu in der ersten Zeile.

::::beispiel Der Steckbrief beginnt
```console
$ uname -a
Linux labor 6.6.87.2-microsoft-standard-WSL2 #1 SMP PREEMPT_DYNAMIC Thu Jun  5 18:30:46 UTC 2025 x86_64 GNU/Linux
$ head -n 1 /etc/os-release
PRETTY_NAME="Ubuntu 26.04.1 LTS"
```

Auf den Kernelnamen `Linux` folgt der Rechnername `labor`, dann die Version. `#1 SMP PREEMPT_DYNAMIC` und das Datum beschreiben, wann und wie der Kernel gebaut wurde: `#1` ist die laufende Nummer des Baus, `SMP` heißt, dass er mehrere Prozessorkerne nutzt. Es folgen der Prozessortyp und `GNU/Linux` als Name des Betriebssystems. Unter WSL 2 ist es der Kernel von Microsoft aus [Kapitel 1, Abschnitt 4.1](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/wsl-2-linux-neben-windows.html#stufe-4-1); in einer virtuellen Maschine oder im Live-System steht dort ein Kernel von Ubuntu, dessen Version auf `generic` endet.
::::

⁠**Kurz gesagt:** `uname -a` nennt Kernel, Rechner und Prozessor, die erste Zeile von `/etc/os-release` die Distribution.

### Der Benutzer: whoami und id

<span class="anker" id="stufe-6-2"></span>

Was du an einem Linux-System darfst, hängt davon ab, wer du für das System bist. `whoami` nennt nur den Namen; `id` verrät, wie das System dich intern führt.

:::abbildung linux/k2id 25
Die Ausgabe von `id` zerlegt: die Benutzernummer mit dem Namen `student`, die Nummer der Hauptgruppe und die Liste aller Gruppen, darunter `sudo`.
:::

Für den Kernel ist ein Benutzer kein Name, sondern eine Zahl, die *Benutzernummer*; der Name ist nur eine Beschriftung für Menschen. Der erste Benutzer, den man bei der Einrichtung anlegt, bekommt unter Ubuntu die Nummer 1000. Außerdem gehört jeder Benutzer zu einer oder mehreren *Gruppen*, benannten Zusammenschlüssen von Benutzern, denen das System gemeinsam etwas erlauben kann. Auch Gruppen haben Nummern.

::::beispiel Wer bin ich?
```console
$ whoami
student
$ id
uid=1000(student) gid=1000(student) groups=1000(student),27(sudo)
```

`uid` ist die Benutzernummer. `gid` ist die Nummer der Hauptgruppe, der einen Gruppe, die jedem Benutzer fest zugeordnet ist; unter Ubuntu heißt sie so wie der Benutzer. `groups` listet alle Gruppen. Die Gruppe `sudo` mit der Nummer 27 ist eine Erlaubnis: Ihre Mitglieder dürfen einzelne Befehle mit den Rechten von root ausführen. Wie und wann man das tut, ist ein eigenes Thema; dieses Kapitel braucht es nicht.
::::

⁠**Kurz gesagt:** `whoami` nennt deinen Namen, `id` deine Benutzernummer und deine Gruppen.

### Datum und Laufzeit: date und uptime

<span class="anker" id="stufe-6-3"></span>

Uhrzeit und Datum braucht man oft, etwa um eine Ausgabe festzuhalten oder einen Dateinamen zu bilden. Und manchmal will man wissen, wie lange der Rechner schon läuft und wie beschäftigt er ist.

::::beispiel Die Uhr des Systems
`date` nennt Datum und Uhrzeit in der eingestellten Zeitzone, mit `-u` in Weltzeit (UTC). Ein Argument, das mit einem Pluszeichen beginnt, ist für `date` eine Vorlage für die Ausgabe; darin steht `%F` für das Datum in der Form Jahr-Monat-Tag:

```console
$ date
Tue Nov 10 00:31:31 CET 2026
$ date -u
Mon Nov  9 23:31:31 UTC 2026
$ date +%F
2026-11-10
```

Kurz nach Mitternacht mitteleuropäischer Zeit ist es in Weltzeit noch der Vortag. Die englischen Namen für Wochentag und Monat kommen von der Spracheinstellung des Testsystems; auf einem Rechner mit deutscher Spracheinstellung schreibt `date` sie deutsch. Die Form `2026-11-10` ist dagegen überall gleich und sortiert sich richtig, deshalb nimmt man sie gern für Dateinamen.
::::

:::abbildung linux/k2uptime 26
Die Ausgabe von `uptime` zerlegt: Uhrzeit, Laufzeit seit dem Start, angemeldete Benutzer und die drei Lastwerte, gemittelt über 1, 5 und 15 Minuten.
:::

`uptime` nennt die Uhrzeit, wie lange das System seit dem Start läuft, wie viele Benutzer angemeldet sind und drei Zahlen zur *Last*. Ein Lastwert ist die durchschnittliche Zahl laufender Programme, die gerade rechnen, auf einen freien Prozessorkern warten oder auf den Datenträger warten, gemittelt über die letzte Minute, die letzten fünf und die letzten fünfzehn Minuten. Genauer ist es ein gleitender Mittelwert, in dem jüngere Augenblicke stärker zählen als ältere. Ob ein Wert hoch ist, sieht man erst im Vergleich mit der Zahl der Prozessorkerne, die `nproc` nennt.

::::beispiel Wie lange läuft der Rechner?
```console
$ uptime
 00:31:31 up 1 min,  1 user,  load average: 2.47, 0.87, 0.31
$ nproc
14
```

WSL 2 startet seine kleine virtuelle Maschine erst, wenn man ein Terminal öffnet, und fährt sie nach dem Schließen des letzten Fensters bald wieder herunter; daher die eine Minute. Der Lastwert der letzten Minute ist mit 2,47 höher als die beiden anderen, weil beim Start viele Programme gleichzeitig loslaufen. Bei 14 Kernen ist auch das wenig: Im Mittel hätten noch über elf Kerne nichts zu tun gehabt.
::::

⁠**Kurz gesagt:** `date` nennt Datum und Uhrzeit, `uptime` die Laufzeit und die Last der letzten 1, 5 und 15 Minuten.

### Der Arbeitsspeicher: free

<span class="anker" id="stufe-6-4"></span>

Wird ein Rechner träge, fragt man als Erstes, ob der Arbeitsspeicher reicht. Die Antwort von `free` ist auf den ersten Blick verwirrend, auf den zweiten sehr aufschlussreich.

:::abbildung linux/k2free 27
Die Ausgabe von `free -h`: gesamt, belegt, frei, geteilt, als Zwischenspeicher genutzt und verfügbar. Der Zwischenspeicher zählt nicht als frei, ist aber zum größten Teil verfügbar.
:::

`free` zeigt den Arbeitsspeicher in Tabellenform, die Option `-h` („human“) in gut lesbaren Einheiten. Die Einheiten `Mi` und `Gi` sind Mebibyte und Gibibyte, also Vielfache von $2^{20}$ und $2^{30}$ Byte ([Kapitel 1, Abschnitt 5.1](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/datentrager-abbild-und-prufsumme.html#stufe-5-1)). Die wichtigsten Spalten:

<ul>

<li>

`total`: der gesamte Arbeitsspeicher, den das System hat.

</li>

<li>

`used`: was nicht verfügbar ist, vor allem weil laufende Programme und der Kernel es belegen; `free` rechnet es als `total` minus `available`.

</li>

<li>

`free`: was gar nicht benutzt wird.

</li>

<li>

`buff/cache`: was der Kernel als *Zwischenspeicher* für Dateien nutzt, damit er sie beim nächsten Lesen nicht wieder vom Datenträger holen muss.

</li>

<li>

`available`: was neu gestartete Programme bekommen könnten, ohne dass etwas auf den Datenträger ausgelagert werden muss.

</li>

</ul>

Die Zeile `Swap` beschreibt einen Bereich auf dem Datenträger, in den der Kernel selten benutzten Speicherinhalt auslagern kann, wenn der Arbeitsspeicher knapp wird.

::::beispiel Wie viel Speicher ist frei?
```console
$ free -h
               total        used        free      shared  buff/cache   available
Mem:            31Gi       765Mi        30Gi       3.5Mi       429Mi        30Gi
Swap:          8.0Gi          0B       8.0Gi
```

Die virtuelle Maschine von WSL 2 hat 31 GiB, knapp die Hälfte des Arbeitsspeichers des Testrechners ([Kapitel 1, Abschnitt 4.1](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/wsl-2-linux-neben-windows.html#stufe-4-1)). Belegt sind 765 MiB, als Zwischenspeicher dienen 429 MiB, und 30 GiB stehen neuen Programmen zur Verfügung.
::::

⁠**Kurz gesagt:** `free -h` zeigt den Arbeitsspeicher; maßgeblich ist die Spalte `available`, nicht `free`.

:::hintergrund Warum Linux scheinbar keinen freien Speicher hat
Auf einem Rechner, der schon länger läuft, zeigt die Spalte `free` oft einen erschreckend kleinen Wert, `buff/cache` dagegen einen großen. Das ist Absicht. Ungenutzter Arbeitsspeicher wäre verschenkt, also behält der Kernel darin Inhalte von Dateien, die schon einmal gelesen wurden. Liest ein Programm sie erneut, kommen sie aus dem Arbeitsspeicher statt vom viel langsameren Datenträger. Braucht ein Programm mehr Speicher, gibt der Kernel den Zwischenspeicher sofort frei. Deshalb rechnet `free` in `available` den größten Teil des Zwischenspeichers zum verfügbaren Speicher, und deshalb ist diese Spalte die richtige, wenn man wissen will, ob der Speicher reicht.
:::

### Der Platz auf den Datenträgern: df

<span class="anker" id="stufe-6-5"></span>

Ist der Datenträger voll, scheitern Programme auf überraschende Weise, etwa beim Speichern oder beim Installieren. `df` (englisch „disk free“) zeigt für jedes eingehängte Dateisystem, wie viel Platz es hat und wie viel davon belegt ist.

:::abbildung linux/k2df 28
Eine Zeile von `df`, zweimal: mit `-h` in Vielfachen von 1024, mit `-H` in Vielfachen von 1000. Dieselben 1 081 101 176 832 Byte erscheinen als `1007G` und als `1.1T`.
:::

Die Begriffe Dateisystem und Einhängen kennst du aus [Kapitel 1, Abschnitte 5.3](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/datentrager-abbild-und-prufsumme.html#stufe-5-3) und [8.1](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/das-live-system.html#stufe-8-1). Ohne Argument listet `df` alle eingehängten Dateisysteme, unter WSL 2 sind das rund zwanzig. Mit einem Ordner als Argument zeigt es nur das Dateisystem, in dem dieser Ordner liegt; `/` ist die Wurzel des ganzen Linux-Dateibaums. Auch hier macht `-h` die Zahlen lesbar, allerdings mit einem Haken: `df -h` rechnet in Vielfachen von 1024 und schreibt trotzdem nur `G`; gemeint ist GiB. Die Option `-H` rechnet in Vielfachen von 1000.

::::beispiel Platz unter Linux und unter Windows
```console
$ df -h /
Filesystem      Size  Used Avail Use% Mounted on
/dev/sdd       1007G  4.2G  952G   1% /
$ df -H /
Filesystem      Size  Used Avail Use% Mounted on
/dev/sdd        1.1T  4.5G  1.1T   1% /
$ df -h /mnt/c
Filesystem      Size  Used Avail Use% Mounted on
C:\             475G  318G  158G  67% /mnt/c
```

Das Linux-Dateisystem von WSL 2 ist 1 081 101 176 832 Byte groß und liegt auf dem Datenträger `/dev/sdd`. Durch $2^{30}$ geteilt sind das 1006,85 GiB, `df -h` rundet auf `1007G`. Durch $10^{12}$ geteilt sind es 1,08 TB, `df -H` rundet auf eine Nachkommastelle auf: `1.1T`. Dass Größe minus Belegung mehr ergibt als den freien Platz, liegt an einer Reserve von rund fünf Prozent, die das Linux-Dateisystem für das Konto root zurückhält. Die dritte Zeile zeigt das Laufwerk C: von Windows, das unter `/mnt/c` eingehängt ist ([Kapitel 1, Abschnitt 4.5](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/wsl-2-linux-neben-windows.html#stufe-4-5)).
::::

Welche Datenträger überhaupt angeschlossen sind, zeigt `lsblk`; seine Ausgabe unter WSL 2 erklärt [Kapitel 1, Abschnitt 8.1](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/das-live-system.html#stufe-8-1).

⁠**Kurz gesagt:** `df -h /` zeigt Größe, Belegung und freien Platz des Dateisystems; `-h` rechnet in Vielfachen von 1024, `-H` von 1000.

### Aufgaben zu Abschnitt [6](#stufe-6)

<span class="anker" id="stufe-6-6"></span>

:::aufgabe Aufgabe 21 ★ Ein Steckbrief deines Systems
<span class="anker" id="aufg-21"></span>

Ermittle für dein eigenes Linux mit je einem Befehl: Kernelversion, Distribution mit Version, deinen Benutzernamen und deine Benutzernummer, deine Gruppen, den gesamten und den verfügbaren Arbeitsspeicher, die Größe und den freien Platz des Dateisystems `/`, die Zahl der Prozessorkerne. Notiere Befehl und Antwort in einer Tabelle.

:::loesung
Auf dem Testsystem:

| Frage | Befehl | Antwort |
|---|---|---|
| Kernelversion | `uname -r` | `6.6.87.2-microsoft-standard-WSL2` |
| Distribution | `head -n 1 /etc/os-release` | `Ubuntu 26.04.1 LTS` |
| Benutzername | `whoami` | `student` |
| Benutzernummer, Gruppen | `id` | `uid=1000`, Gruppen `student` und `sudo` |
| Arbeitsspeicher | `free -h` | gesamt `31Gi`, verfügbar `30Gi` |
| Platz auf `/` | `df -h /` | Größe `1007G`, frei `952G` |
| Prozessorkerne | `nproc` | `14` |

Deine Werte unterscheiden sich; in einer virtuellen Maschine oder im Live-System endet die Kernelversion auf `generic`. Speicher und Kerne sind in einer virtuellen Maschine die, die du ihr zugeteilt hast, im Live-System die des Rechners selbst.
:::
:::

:::aufgabe Aufgabe 22 ★★ Einheiten nachrechnen
<span class="anker" id="aufg-22"></span>

`free -b` zeigt den Speicher in Byte. Auf dem Testsystem meldete es als `total` 33 393 664 000 Byte. Rechne nach, dass `free -h` dafür `31Gi` anzeigt. Was würde `free -h --si` anzeigen, das in Vielfachen von 1000 rechnet? Prüfe auch: `df` meldete als belegt 4 439 998 464 Byte. Warum zeigt `df -h` dafür `4.2G`, obwohl genau gerechnet 4,13 GiB herauskommen?

:::loesung
$33\,393\,664\,000 / 2^{30} = 31{,}10$, also rund 31 GiB; `free -h` zeigt `31Gi`. In Vielfachen von 1000 sind es $33\,393\,664\,000 / 10^{9} = 33{,}39$ GB; `free -h --si` zeigt `33G`.

$4\,439\,998\,464 / 2^{30} = 4{,}135$ GiB. `df` rundet bei `-h` und `-H` nicht kaufmännisch, sondern immer auf; aus 4,135 wird so `4.2G`. Mit `-H` sind es $4\,439\,998\,464 / 10^{9} = 4{,}44$ GB, aufgerundet `4.5G`, wie im Beispiel in Unterabschnitt [6.5](#stufe-6-5).
:::
:::

:::aufgabe Aufgabe 23 ★★ Datum als Vorlage
<span class="anker" id="aufg-23"></span>

Finde in `date --help` oder `man date` heraus, wie du (a) nur die Uhrzeit im Format Stunden:Minuten:Sekunden, (b) den Wochentag ausgeschrieben, (c) die Nummer der Kalenderwoche ausgeben lässt. Warum ist `+%F` ein Argument und keine Option?

:::loesung
In der Liste der Vorlagen von `date --help` stehen `%T` für die Uhrzeit, `%A` für den ausgeschriebenen Wochentag und `%V` für die Kalenderwoche nach ISO, bei der die Woche am Montag beginnt:

```console
$ date +%T
00:40:54
$ date +%A
Tuesday
$ date +%V
46
```

`+%F` beginnt nicht mit einem Minuszeichen, also ist es nach den Regeln aus Abschnitt [2](der-aufbau-einer-befehlszeile.html#stufe-2) keine Option, sondern ein gewöhnliches Argument. Dass ein Argument mit Pluszeichen eine Vorlage ist, hat `date` selbst festgelegt; für die Shell ist es ein Wort wie jedes andere.
:::
:::

:::aufgabe Aufgabe 24 ★★★ Last deuten
<span class="anker" id="aufg-24"></span>

Ein Server mit 4 Prozessorkernen meldet bei `uptime` die Lastwerte `6.10, 3.95, 1.20`. Ein anderer mit 32 Kernen meldet `6.10, 6.05, 6.12`. Was sagen die drei Zahlen jeweils über den Verlauf der letzten Viertelstunde? Welcher Rechner ist ausgelastet?

:::loesung
Der Server mit 4 Kernen: In der letzten Viertelstunde lag die Last im Mittel bei 1,20, in den letzten fünf Minuten bei 3,95, in der letzten Minute bei 6,10. Die Last steigt also gerade stark an. 6,10 Programme wollten im Mittel rechnen oder warteten auf den Datenträger, aber nur 4 Kerne standen bereit: Gut zwei mussten ständig warten. Dieser Rechner ist im Moment überlastet.

Der Server mit 32 Kernen: Die drei Werte sind fast gleich, die Last ist seit einer Viertelstunde gleichmäßig. 6 von 32 Kernen sind im Mittel beschäftigt, also knapp ein Fünftel. Dieser Rechner hat reichlich Reserven, obwohl seine Lastwerte genauso hoch sind wie die des ersten.
:::
:::

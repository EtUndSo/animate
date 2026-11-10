---
title: Die Verzeichnisstruktur von Linux
pfad: Informatik / Linux und Kommandozeile / Dateien, Verzeichnisse und Pfade
adresse: informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade
knoten: Kapitel 3: Dateien, Verzeichnisse und Pfade
order: 6080800
summary: In / stehen gut zwanzig Verzeichnisse mit kurzen, rätselhaften Namen.
tags: Filesystem Hierarchy Standard, /usr, Bibliothek, /etc, /home, /root, /var, Protokolldateien
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
In `/` stehen gut zwanzig Verzeichnisse mit kurzen, rätselhaften Namen. Sie folgen einem Plan, der auf fast allen Linux-Systemen gleich ist. Wer ihn kennt, weiß auf jedem fremden System, wo Programme, Einstellungen und Protokolle liegen. Dieser Abschnitt geht die wichtigsten Verzeichnisse durch.
:::

### Der Standard für die Verzeichnisstruktur

<span class="anker" id="stufe-7-1"></span>

Damit Programme ihre Teile auf jedem Linux finden, müssen sich alle Distributionen auf feste Orte einigen. Diese Einigung ist aufgeschrieben.

:::abbildung linux/k3fhs 26
Die oberste Ebene des Verzeichnisbaums, nach Zweck eingefärbt: Programme und Bibliotheken (`/usr`, `/opt`), Einstellungen (`/etc`), Benutzer (`/home`, `/root`), veränderliche Daten (`/var`, `/tmp`), Start (`/boot`), Einhängepunkte (`/mnt`, `/media`) und Verzeichnisse, die der Kernel erzeugt (`/dev`, `/proc`, `/sys`, `/run`).
:::

:::definition Definition 7.1 (Filesystem Hierarchy Standard)
<span class="anker" id="satz-7-1"></span>

Der __Filesystem Hierarchy Standard__, kurz FHS, legt fest, welche Verzeichnisse ein Linux-System haben soll und welche Art von Dateien in welches gehört. Die geltende Fassung 3.0 erschien 2015; heute betreut ihn freedesktop.org, ein Zusammenschluss von Entwicklern freier Software.
:::

Die großen Distributionen halten sich weitgehend daran, nicht immer in jeder Einzelheit. Tabelle [2](#tab-2) nennt die Verzeichnisse der obersten Ebene; Abbildung [26](#abb-26) ordnet sie nach Zweck.

<span class="anker" id="tab-2"></span>

**Tabelle 2:** Die Verzeichnisse der obersten Ebene nach dem FHS.

| Verzeichnis | Inhalt |
|---|---|
| `/usr` | Programme, Bibliotheken und Daten, die mit dem System geliefert werden |
| `/etc` | Einstellungen des ganzen Systems, fast nur Textdateien |
| `/home` | Heimatverzeichnisse der Benutzer |
| `/root` | Heimatverzeichnis von `root` |
| `/var` | Daten, die sich im Betrieb ändern, etwa Protokolle in `/var/log` |
| `/tmp` | vorübergehende Dateien, für alle beschreibbar |
| `/boot` | Kernel und Dateien für den Systemstart |
| `/dev` | Geräte als Dateien |
| `/proc`, `/sys` | Angaben des Kernels über laufende Programme und Geräte |
| `/run` | Angaben seit dem letzten Start, im Arbeitsspeicher |
| `/mnt`, `/media` | Einhängepunkte für weitere Datenträger |
| `/opt` | Zusatzprogramme, die nicht zur Distribution gehören |
| `/srv` | Daten für Dienste, die der Rechner anderen anbietet |
| `/bin`, `/sbin`, `/lib` | früher eigene Verzeichnisse für die wichtigsten Programme und Bibliotheken; heute unter `/usr` zu finden |

::::beispiel Ein Rundgang mit wenigen Befehlen
Für einen Rundgang reichen `cd`, `ls -l`, `file` und `less`: in ein Verzeichnis wechseln, die Einträge ansehen, bei einer interessanten Datei die Art prüfen und eine Textdatei lesen. Zerstören kannst du dabei nichts, denn als gewöhnlicher Benutzer darfst du in den Verzeichnissen des Systems nur lesen. Wo selbst das verboten ist, meldet Linux „Permission denied“, und du gehst einfach weiter.
::::

⁠**Kurz gesagt:** Der FHS legt fest, welches Verzeichnis wofür da ist; deshalb sehen alle Linux-Systeme in den Grundzügen gleich aus.

### Programme und Bibliotheken: /usr

<span class="anker" id="stufe-7-2"></span>

Der größte Teil eines Linux-Systems sind die Programme, die es mitbringt. Sie liegen gesammelt in einem Teilbaum.

:::definition Definition 7.2 (/usr)
<span class="anker" id="satz-7-2"></span>

Das Verzeichnis __/usr__ enthält die Programme, Bibliotheken und unveränderlichen Daten, die mit der Distribution geliefert werden. Die Programme liegen in `/usr/bin`, Programme für die Systemverwaltung in `/usr/sbin`, Bibliotheken in `/usr/lib` und Daten wie Handbuchseiten und Anleitungen in `/usr/share`.
:::

Eine __Bibliothek__ ist eine Datei mit Programmteilen, die viele Programme gemeinsam benutzen, statt sie jeweils selbst zu enthalten. `/usr/bin` kennst du als Ort der Programmdateien aus [Kapitel 2, Abschnitt 3.1](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/arten-von-befehlen.html#stufe-3-1); auf dem Testrechner liegen dort über tausend Einträge. Zwei weitere Orte sind für Software gedacht, die nicht von der Distribution stammt: `/usr/local` für Programme, die die Verwalterin des Rechners selbst installiert, und `/opt` für größere Zusatzprogramme, oft von Firmen, die alles in einem eigenen Unterverzeichnis mitbringen.

::::beispiel Wo die Handbuchseiten liegen
```console
$ ls /usr/share/man
ar  de  fr  id  ko    man3  man6  nl  pt_BR  sk  sv  zh
cs  es  hr  it  man1  man4  man7  pl  ro     sl  tr  zh_CN
da  fi  hu  ja  man2  man5  man8  pt  ru     sr  uk  zh_TW
```

`man1` bis `man8` sind die acht Abschnitte des Handbuchs aus [Kapitel 2, Abschnitt 4.5](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/hilfe-finden.html#stufe-4-5); die übrigen Verzeichnisse enthalten Übersetzungen, `de` etwa die deutschen.
::::

⁠**Kurz gesagt:** Unter `/usr` liegt alles, was die Distribution an Programmen und festen Daten mitbringt; eigene Zusatzsoftware gehört nach `/usr/local` oder `/opt`.

:::hintergrund Warum feste und veränderliche Daten getrennt liegen
Der FHS sortiert Dateien nach zwei Fragen. Erstens: Ändern sie sich im Betrieb? Programme und Handbuchseiten ändern sich nur, wenn jemand neue Software installiert; sie heißen statisch. Protokolle, Warteschlangen und Zwischenstände ändern sich ständig; sie heißen variabel. Zweitens: Könnten mehrere Rechner sie gemeinsam benutzen? Ein Programm ist auf jedem Rechner gleich, die Einstellung eines bestimmten Rechners nicht. Aus beiden Fragen folgt die Aufteilung:

|  | teilbar | an den Rechner gebunden |
|---|---|---|
| statisch | `/usr`, `/opt` | `/etc`, `/boot` |
| variabel | `/var/mail` | `/var/run`, `/var/lock` |

Der Nutzen: `/usr` kann auf einem schreibgeschützten Datenträger liegen oder über das Netz für viele Rechner bereitgestellt werden, und eine Sicherung muss vor allem `/etc`, `/home` und Teile von `/var` erfassen.
:::

### Einstellungen: /etc

<span class="anker" id="stufe-7-3"></span>

Jedes System ist ein wenig anders eingestellt: ein anderer Rechnername, eine andere Zeitzone, andere Benutzer. Diese Unterschiede stehen an einem einzigen Ort.

:::definition Definition 7.3 (/etc)
<span class="anker" id="satz-7-3"></span>

Das Verzeichnis __/etc__ enthält die Einstellungen, die für das ganze System gelten. Fast alle Dateien darin sind Textdateien, die man lesen und mit Verwalterrechten in einem Texteditor ändern kann.
:::

Drei Dateien aus `/etc` kennst du schon: `/etc/hostname` mit dem Rechnernamen, `/etc/timezone` mit der Zeitzone und `/etc/passwd` mit der Liste der Benutzer. Viele Programme haben in `/etc` eine eigene Datei, deren Name oft auf `.conf` endet, oder ein eigenes Unterverzeichnis.

::::beispiel Einstellungsdateien finden
Mit einem Muster aus Unterabschnitt [6.6](kopieren-verschieben-loschen.html#stufe-6-6) findet man Dateien mit gemeinsamem Anfang:

```console
$ ls /etc/h*
/etc/host.conf  /etc/hostname  /etc/hosts
```

Neben `hostname` gibt es `hosts`, eine Liste von Rechnernamen und ihren Adressen im Netz, und `host.conf`, das regelt, wie Namen nachgeschlagen werden. Alle drei sind Textdateien; `less` zeigt sie an.
::::

⁠**Kurz gesagt:** `/etc` ist der Ort der Einstellungen des ganzen Systems, als Textdateien.

### Die Benutzer: /home und /root

<span class="anker" id="stufe-7-4"></span>

Die eigenen Dateien der Menschen, die einen Rechner benutzen, gehören nicht zwischen die Programme. Sie bekommen einen eigenen Teilbaum.

:::definition Definition 7.4 (/home, /root)
<span class="anker" id="satz-7-4"></span>

Das Verzeichnis __/home__ enthält für jeden gewöhnlichen Benutzer ein Heimatverzeichnis mit seinem Namen. Das Heimatverzeichnis von `root` liegt getrennt davon in __/root__.
:::

Weil `/root` direkt unter der Wurzel liegt, kommt der Verwalter auch dann an seine Dateien, wenn `/home` auf einem eigenen Datenträger liegt, der gerade nicht eingehängt ist. Fremde Heimatverzeichnisse sind meist nicht oder nur eingeschränkt lesbar.

::::beispiel Wer wohnt hier?
```console
$ ls /home
student
$ ls /root
ls: cannot open directory '/root': Permission denied
```

Auf dem Testrechner gibt es einen einzigen gewöhnlichen Benutzer. In `/root` darf er nicht hineinsehen.
::::

⁠**Kurz gesagt:** Die Benutzer wohnen in `/home/<name>`, `root` wohnt in `/root`.

### Veränderliche Daten: /var und die Protokolle

<span class="anker" id="stufe-7-5"></span>

Während das System läuft, entstehen ständig Daten: Programme notieren, was sie getan haben, Warteschlangen füllen sich, Zwischenstände werden abgelegt. Diese Daten brauchen einen Ort, der wachsen darf.

:::definition Definition 7.5 (/var, Protokolldatei)
<span class="anker" id="satz-7-5"></span>

Das Verzeichnis __/var__ (kurz für „variable“) enthält Daten, die sich im laufenden Betrieb ändern. Ein wichtiger Teil davon ist `/var/log` mit den __Protokolldateien__: Dateien, an deren Ende ein Programm fortlaufend schreibt, was geschieht, jeweils mit Datum und Uhrzeit.
:::

Weil neue Einträge immer unten angehängt werden, liest man ein Protokoll meist mit `tail` von hinten: Die letzten Zeilen sind die jüngsten. Manche Protokolle darf nur `root` lesen, weil sie Hinweise auf Anmeldungen und andere heikle Vorgänge enthalten.

::::beispiel Ins Protokoll der Software-Installation schauen
```console
$ ls /var/log
README            chrony        dmesg.3.gz      landscape
alternatives.log  dist-upgrade  dmesg.4.gz      lastlog
apt               dmesg         dpkg.log        private
auth.log          dmesg.0       fontconfig.log  syslog
bootstrap.log     dmesg.1.gz    journal         unattended-upgrades
btmp              dmesg.2.gz    kern.log        wtmp
$ tail -n 3 /var/log/dpkg.log
2026-11-09 16:35:28 status config-files ubuntu-helper-virt-hwe:all 1:10.2.1+ds-1ubuntu4.4
2026-11-09 16:35:28 status not-installed ubuntu-helper-virt-hwe:all <none>
2026-11-09 16:35:28 startup packages configure
```

`dpkg.log` schreibt das Programm mit, das unter Ubuntu Software einrichtet und entfernt. Jede Zeile beginnt mit Datum und Uhrzeit. Dateien mit der Endung `.gz` sind ältere, komprimierte Protokolle, die weniger Platz belegen.
::::

⁠**Kurz gesagt:** `/var` nimmt alles auf, was sich im Betrieb ändert; die Protokolle stehen in `/var/log`.

### Vorübergehende Dateien: /tmp

<span class="anker" id="stufe-7-6"></span>

Viele Programme brauchen kurz eine Datei, etwa für einen Zwischenstand, den nach dem Ende niemand mehr braucht. Dafür gibt es einen gemeinsamen Platz.

:::definition Definition 7.6 (/tmp)
<span class="anker" id="satz-7-6"></span>

Das Verzeichnis __/tmp__ ist für vorübergehende Dateien gedacht. Jeder Benutzer darf dort Dateien anlegen; beim Neustart des Systems darf der Inhalt verschwinden.
:::

Auf dem Testsystem, Ubuntu 26.04 unter WSL 2, liegt `/tmp` im Arbeitsspeicher, als Dateisystem der Art tmpfs ([Kapitel 1, Abschnitt 8.4](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/das-live-system.html#stufe-8-4)); beim Ausschalten ist der Inhalt weg. Andere Systeme legen `/tmp` auf den Datenträger und leeren es beim Start. Dateien, die einen Neustart überstehen sollen, gehören nach `/var/tmp`. Eigene Dateien, die man behalten will, legt man weder hier noch dort ab, sondern im Heimatverzeichnis.

::::beispiel Zwei Verzeichnisse für vorübergehende Dateien
```console
$ ls -ld /tmp /var/tmp
drwxrwxrwt 7 root root  140 Nov 10 02:42 /tmp
drwxrwxrwt 5 root root 4096 Nov 10 02:42 /var/tmp
```

Beide gehören `root`, und die Zugriffsrechte enden auf ein `t` statt eines `x`; das hängt damit zusammen, dass alle dort schreiben dürfen. Die Größe von `/tmp` ist nicht 4096, sondern 140: Ein Dateisystem im Arbeitsspeicher berechnet die Größe eines Verzeichnisses anders als eines auf dem Datenträger.
::::

⁠**Kurz gesagt:** `/tmp` ist ein gemeinsamer Platz für kurzlebige Dateien; was bleiben soll, gehört ins Heimatverzeichnis.

### Geräte als Dateien: /dev

<span class="anker" id="stufe-7-7"></span>

Programme müssen mit Geräten sprechen: mit Festplatten, mit dem Terminal, mit Zufallsgeneratoren. Unter Linux brauchen sie dafür keine eigenen Befehle; Geräte sehen aus wie Dateien, wie Abbildung [27](#abb-27) zeigt.

:::abbildung linux/k3dev 27
Gerätedateien sind Türen zum Kernel. Ein Programm liest aus `/dev/zero`, `/dev/urandom` oder `/dev/sdd` mit denselben Mitteln wie aus einer gewöhnlichen Datei; hinter der Tür antwortet aber kein gespeicherter Inhalt, sondern ein Treiber im Kernel.
:::

:::definition Definition 7.7 (Gerätedatei)
<span class="anker" id="satz-7-7"></span>

Eine __Gerätedatei__ ist ein Eintrag im Verzeichnisbaum, hinter dem kein gespeicherter Inhalt steht, sondern ein Gerät, das ein Treiber im Kernel verwaltet. Wer aus ihr liest oder in sie schreibt, spricht mit diesem Gerät. Die Gerätedateien liegen in `/dev`.
:::

`ls -l` kennzeichnet sie mit eigenen Buchstaben: `c` für ein Gerät, das Daten Zeichen für Zeichen liefert, `b` für eines, das in Blöcken arbeitet, wie ein Datenträger. Statt einer Größe stehen zwei Zahlen da, mit denen der Kernel Treiber und Gerät auswählt. Vier Gerätedateien sind besonders bekannt: `/dev/null` verschluckt alles, was man hineinschreibt, und liefert beim Lesen nichts; `/dev/zero` liefert beliebig viele Nullbytes; `/dev/urandom` liefert Zufallsbytes; `/dev/sdd` ist auf dem Testrechner der Datenträger, auf dem das Linux liegt.

::::beispiel Aus Geräten lesen
```console
$ ls -l /dev/null /dev/zero /dev/urandom /dev/sdd
crw-rw-rw- 1 root root 1,  3 Nov 10 02:41 /dev/null
brw-rw---- 1 root disk 8, 48 Nov 10 02:41 /dev/sdd
crw-rw-rw- 1 root root 1,  9 Nov 10 02:41 /dev/urandom
crw-rw-rw- 1 root root 1,  5 Nov 10 02:41 /dev/zero
$ wc -c /dev/null
0 /dev/null
$ od -An -tu1 -N8 /dev/zero
   0   0   0   0   0   0   0   0
$ od -An -tu1 -N8 /dev/urandom
  14 237 103 241 210 228 133 123
```

`/dev/null` hat beim Lesen null Bytes. Aus `/dev/zero` kommen nur Nullen, aus `/dev/urandom` bei jedem Aufruf andere Zahlen; deine werden anders aussehen. Lesen darf `/dev/sdd` nur `root` und die Gruppe `disk`, denn wer den Datenträger direkt liest, sieht alle Dateien darauf.
::::

⁠**Kurz gesagt:** In `/dev` stehen Geräte als Dateien; man liest und schreibt sie mit denselben Werkzeugen wie gewöhnliche Dateien.

:::hintergrund „Alles ist eine Datei“
Einer der Grundgedanken von Unix lautet: Fast alles, womit ein Programm arbeitet, erscheint als Datei im einen Baum. Das hat einen handfesten Vorteil. Ein Programm braucht nur eine Handvoll Systemaufrufe, nämlich öffnen, lesen, schreiben und schließen, und kann damit gewöhnliche Dateien und Geräte gleichermaßen verarbeiten. `od` wusste in dem Beispiel nicht, dass es aus einem Zufallsgenerator las; für `od` war `/dev/urandom` eine Datei wie jede andere. Ebenso wichtig ist die gemeinsame Benennung: Weil Geräte Namen im Baum haben, gelten für sie dieselben Pfade und Zugriffsrechte wie für Dateien. Das Prinzip hat Grenzen, denn manche Geräte, etwa Netzwerkkarten, haben unter Linux keinen Eintrag in `/dev`; als Leitlinie prägt es das System trotzdem bis heute.
:::

### Der Kernel als Dateisystem: /proc und /sys

<span class="anker" id="stufe-7-8"></span>

Wie lange läuft der Rechner schon, welcher Prozessor steckt darin, wie groß ist der Datenträger? Diese Angaben kennt der Kernel. Damit man sie ohne besonderes Werkzeug abfragen kann, stellt er sie als Dateien bereit. Abbildung [28](#abb-28) zeigt, wie eine solche Datei entsteht.

:::abbildung linux/k3proc 28
Eine Datei, die es nur beim Lesen gibt. `cat /proc/uptime` fragt den Kernel; erst in diesem Moment erzeugt er die Textzeile mit der Laufzeit und reicht sie zurück. Auf keinem Datenträger liegt diese Datei.
:::

:::definition Definition 7.8 (virtuelles Dateisystem)
<span class="anker" id="satz-7-8"></span>

Ein __virtuelles Dateisystem__ ist ein Dateisystem, dessen Dateien auf keinem Datenträger liegen; der Kernel erzeugt ihren Inhalt in dem Moment, in dem ein Programm sie liest. `/proc` ist ein solches Dateisystem mit Angaben über den Kernel und über jedes laufende Programm, `/sys` eines mit Angaben über Geräte und Treiber.
:::

In `/proc` hat jedes laufende Programm ein Verzeichnis, dessen Name eine Zahl ist. Daneben gibt es Dateien wie `/proc/version` mit der Version des Kernels, `/proc/uptime` mit der Laufzeit in Sekunden und `/proc/cpuinfo` mit Angaben zum Prozessor. Die Befehle `uptime` und `free` aus [Kapitel 2, Abschnitte 6.3](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/das-system-erkunden.html#stufe-6-3) und [6.4](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/das-system-erkunden.html#stufe-6-4), lesen ihre Angaben aus `/proc/uptime` und `/proc/meminfo`.

::::beispiel Den Kernel befragen
```console
$ cat /proc/version
Linux version 6.6.87.2-microsoft-standard-WSL2 (root@439a258ad544) (gcc (GCC) 11.2.0, GNU ld (GNU Binutils) 2.37) #1 SMP PREEMPT_DYNAMIC Thu Jun  5 18:30:46 UTC 2025
$ ls -l /proc/version
-r--r--r-- 1 root root 0 Nov 10 02:42 /proc/version
$ cat /proc/uptime
46.54 642.08
$ ls -d /proc/[0-9]*
/proc/1    /proc/178  /proc/221  /proc/327  /proc/397  /proc/87
/proc/158  /proc/181  /proc/222  /proc/328  /proc/43
/proc/159  /proc/2    /proc/238  /proc/329  /proc/435
/proc/160  /proc/203  /proc/246  /proc/371  /proc/6
/proc/170  /proc/206  /proc/326  /proc/373  /proc/80
```

`/proc/version` hat laut `ls -l` die Größe 0 und liefert trotzdem eine lange Zeile: Der Inhalt entsteht erst beim Lesen. Die erste Zahl in `/proc/uptime` ist die Laufzeit in Sekunden, hier 46,5; die zweite zählt, wie lange alle Prozessorkerne zusammen untätig waren. Das Muster `[0-9]*` wählt alle Einträge, die mit einer Ziffer beginnen: ein Verzeichnis je laufendem Programm.
::::

::::beispiel [Zweites Beispiel] Die Größe des Datenträgers aus /sys
Für jeden Datenträger gibt es unter `/sys/block` ein Verzeichnis; die Datei `size` nennt seine Größe in Sektoren zu 512 Byte (Sektor: [Kapitel 1, Abschnitt 5.1](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/datentrager-abbild-und-prufsumme.html#stufe-5-1)):

```console
$ cat /sys/block/sdd/size
2147483648
```

$2\,147\,483\,648 \cdot 512 = 1\,099\,511\,627\,776$ Byte. Mit Zweierpotenzen geht es schneller: $2\,147\,483\,648 = 2^{31}$ und $512 = 2^9$, zusammen $2^{31} \cdot 2^9 = 2^{40}$ Byte, genau 1 TiB.
::::

⁠**Kurz gesagt:** `/proc` und `/sys` sind Fenster in den Kernel: Ihre Dateien entstehen beim Lesen und verraten Laufzeit, Prozessor, Geräte und laufende Programme.

:::hintergrund Warum eine Datei der Größe 0 Inhalt haben kann
Die Größe, die `ls -l` zeigt, ist eine Angabe aus der Verwaltung des Dateisystems. Bei gewöhnlichen Dateien stimmt sie mit der Zahl der gespeicherten Bytes überein. Bei `/proc` gibt es nichts Gespeichertes: Öffnet ein Programm `/proc/uptime`, ruft der Kernel eine kleine Funktion auf, die die Laufzeit in Text verwandelt, und gibt diesen Text als Inhalt zurück. Wie lang er wird, weiß der Kernel erst beim Erzeugen; deshalb meldet er als Größe 0. Programme, die Dateien bis zum Ende lesen, wie `cat`, kommen damit zurecht; ein Programm, das sich auf die Größe verlässt, würde nichts lesen. Die Idee, laufende Programme als Dateien darzustellen, stammt aus der Unix-Forschung von 1984; Linux hat sie zu einem Fenster auf fast alles erweitert, was der Kernel weiß.
:::

### Aufgaben zu Abschnitt [7](#stufe-7)

<span class="anker" id="stufe-7-9"></span>

:::aufgabe Aufgabe 23 ★★ Ein Rundgang
<span class="anker" id="aufg-23"></span>

Schreibe zu jedem der folgenden Orte einen Satz, was er ist und wozu er da ist, und prüfe deine Antwort mit `ls -ld`, `file` oder `head`: (a) `/etc/hostname`, (b) `/var/log`, (c) `/dev/null`, (d) `/proc/cpuinfo`, (e) `/usr/bin`.

:::loesung
(a) `/etc/hostname` ist eine Textdatei in `/etc` mit dem Namen des Rechners. (b) `/var/log` ist das Verzeichnis der Protokolldateien. (c) `/dev/null` ist eine Gerätedatei, die alles verschluckt, was man hineinschreibt, und beim Lesen nichts liefert. (d) `/proc/cpuinfo` ist eine Datei des virtuellen Dateisystems `/proc` mit Angaben zum Prozessor; der Kernel erzeugt sie beim Lesen. (e) `/usr/bin` ist das Verzeichnis mit den Programmen der Distribution. Die Probe:

```console
$ file /etc/hostname /var/log /dev/null /proc/cpuinfo /usr/bin
/etc/hostname: ASCII text
/var/log:      directory
/dev/null:     character special (1/3)
/proc/cpuinfo: empty
/usr/bin:      directory
```

Bemerkenswert ist (d): `file` hält `/proc/cpuinfo` für leer, weil die Datei die Größe 0 meldet. `head -n 5 /proc/cpuinfo` zeigt trotzdem Inhalt, denn `head` liest einfach, bis nichts mehr kommt. `file` nennt bei `/dev/null` das Gerät „character special“ mit den beiden Gerätenummern 1 und 3, die auch `ls -l` zeigt.
:::
:::

:::aufgabe Aufgabe 24 ★ Wohin gehört die Datei?
<span class="anker" id="aufg-24"></span>

In welches Verzeichnis gehört nach dem FHS: (a) die Einstellungsdatei eines Programms für das ganze System, (b) das Protokoll eines Dienstes, (c) ein Programm, das die Distribution mitliefert, (d) dein eigenes Urlaubsfoto, (e) eine Datei, die ein Programm nur während seiner Laufzeit braucht, (f) ein Zusatzprogramm einer Firma, das alles in einem eigenen Verzeichnis mitbringt?

:::loesung
(a) `/etc`. (b) `/var/log`. (c) `/usr/bin`. (d) Dein Heimatverzeichnis, etwa `/home/student/fotos`, unter `/home`. (e) `/tmp`. (f) `/opt`.
:::
:::

:::aufgabe Aufgabe 25 ★★ Laufzeit aus /proc
<span class="anker" id="aufg-25"></span>

Lies `/proc/uptime` und rechne die erste Zahl in Stunden und Minuten um. Vergleiche mit der Ausgabe von `uptime` aus [Kapitel 2, Abschnitt 6.3](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/das-system-erkunden.html#stufe-6-3). Warum stimmen beide überein, obwohl `/proc/uptime` laut `ls -l` leer ist?

:::loesung
```console
$ cat /proc/uptime
83.80 1163.22
$ uptime
 02:42:54 up 1 min,  1 user,  load average: 0.00, 0.00, 0.00
```

83,80 Sekunden sind eine Minute und 23,8 Sekunden, also 0 Stunden und 1 Minute; `uptime` zeigt genau das als `up 1 min`, auf ganze Minuten abgerundet. Die WSL-VM des Testrechners war hier gerade erst gestartet; auf deinem Rechner sind es vermutlich Stunden. Beide stimmen überein, weil `uptime` seine Angabe aus `/proc/uptime` liest. Dass die Datei laut `ls -l` die Größe 0 hat, spielt keine Rolle: Ihr Inhalt entsteht erst beim Lesen, frisch aus der Uhr des Kernels.
:::
:::

:::aufgabe Aufgabe 26 ★★ Die Größe des Datenträgers
<span class="anker" id="aufg-26"></span>

Auf einem anderen Rechner liefert `/sys/block/sda/size` den Wert `1000215216`. Wie viele Byte hat der Datenträger, wie viele GB und wie viele GiB? Welche der beiden Zahlen würde ein Händler auf die Verpackung schreiben?

:::loesung
$1\,000\,215\,216 \cdot 512 = 512\,110\,190\,592$ Byte. Durch $10^9$ geteilt sind das 512,11 GB, durch $1024^3$ geteilt 476,94 GiB. Auf der Verpackung stünde „512 GB“, denn Hersteller zählen in Zehnerpotenzen ([Kapitel 1, Abschnitt 5.1](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/datentrager-abbild-und-prufsumme.html#stufe-5-1)). `lsblk` und `ls -h` würden 476.9G anzeigen; beide meinen dieselbe Zahl von Bytes.
:::
:::

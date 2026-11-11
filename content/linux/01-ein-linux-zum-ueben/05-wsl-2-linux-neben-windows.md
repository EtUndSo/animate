---
title: WSL 2: Linux neben Windows
pfad: Informatik / Linux und Kommandozeile / Ein Linux zum Üben: WSL, virtuelle Maschine, Live-USB-Stick
adresse: informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick
knoten: Kapitel 1: Ein Linux zum Üben: WSL, virtuelle Maschine, Live-USB-Stick
order: 6060500
summary: Der schnellste Weg zu einem Linux unter Windows ist WSL 2.
tags: Windows-Subsystem für Linux
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Der schnellste Weg zu einem Linux unter Windows ist WSL 2. Dieser Abschnitt erklärt, was WSL 2 ist, nämlich eine kleine virtuelle Maschine, die Windows selbst verwaltet, wie man es einrichtet und prüft, wie Windows und Linux gegenseitig an ihre Dateien kommen und wo die Grenzen dieses Wegs liegen.
:::

### Das Windows-Subsystem für Linux

<span class="anker" id="stufe-4-1"></span>

Für die Arbeit an der Kommandozeile will man kein eigenes Fenster mit einem ganzen zweiten Rechner, sondern ein Linux-Terminal, das sich anfühlt wie jedes andere Programm unter Windows. Genau das bietet WSL 2, und unter der Oberfläche ist es eine virtuelle Maschine.

Abbildung [8](#abb-8) zeigt den Aufbau.

:::abbildung linux/k1wsl 8
WSL 2. Windows startet über den Hypervisor von Microsoft eine kleine virtuelle Maschine mit einem echten Linux-Kernel, in der die Distribution läuft. Dateien gehen über die Grenze der VM in beide Richtungen: Linux sieht Laufwerk C: unter `/mnt/c`, Windows sieht die Linux-Dateien im Explorer.
:::

:::definition Definition 4.1 (WSL 2)
<span class="anker" id="satz-4-1"></span>

Das __Windows-Subsystem für Linux__, Version 2 (WSL 2), ist ein Bestandteil von Windows, der einen echten Linux-Kernel in einer kleinen virtuellen Maschine startet, die Windows selbst anlegt, startet und anhält. In dieser VM laufen eine oder mehrere Distributionen, jede gegen die anderen abgeschirmt. Den Linux-Kernel baut Microsoft aus dem offiziellen Linux-Quelltext und liefert ihn mit Aktualisierungen aus; die Distribution kommt von ihrem Hersteller, bei Ubuntu also von Canonical.
:::

::::beispiel Die VM hinter WSL 2
Die VM von WSL 2 bekommt standardmäßig höchstens die Hälfte des Arbeitsspeichers des Rechners. Auf dem Testrechner dieses Kapitels meldet Windows 63,5 GB Arbeitsspeicher; das Ubuntu in WSL 2 meldet davon 31 GB, knapp die Hälfte. Ein Programm, das unter Windows läuft, merkt von dieser VM nichts; ein Programm in Linux sieht nur sie und nicht den Rest des Rechners.
::::

⁠**Kurz gesagt:** WSL 2 ist ein echtes Linux in einer kleinen VM, die Windows selbst verwaltet.

:::hintergrund WSL 1 und WSL 2
Die erste Fassung von WSL, heute WSL 1, hatte keinen Linux-Kernel. Sie übersetzte jeden Systemaufruf eines Linux-Programms in passende Aufrufe des Windows-Kernels. Das war elegant, aber nie vollständig: Manche Systemaufrufe hatten unter Windows keine Entsprechung, und Programme, die sie brauchten, liefen nicht. WSL 2 geht den umgekehrten Weg. Weil darin ein echter Linux-Kernel läuft, versteht es jeden Systemaufruf, und jedes Linux-Programm läuft. Der Preis ist, dass Linux und Windows nun in zwei getrennten Maschinen leben und Dateien über eine Grenze hinweg austauschen müssen. Wer heute WSL einrichtet, bekommt WSL 2.
:::

### WSL 2 einrichten

<span class="anker" id="stufe-4-2"></span>

Das Einrichten besteht aus einem einzigen Befehl, ein paar Minuten Warten und einem Neustart. Danach legst du in Ubuntu einen Benutzer an.

**Voraussetzungen.** Du brauchst Windows 11 oder Windows 10 ab Version 2004, die Rechte eines Administrators auf deinem Rechner und eine Internetverbindung. Windows Home genügt.

**Schritte.** So richtest du WSL 2 mit Ubuntu 26.04 ein:

<ol>

<li>

Klicke mit der rechten Maustaste auf das Startmenü und wähle „Terminal (Administrator)“, unter Windows 10 „Windows PowerShell (Administrator)“; bestätige die Rückfrage. Es öffnet sich eine PowerShell mit Administratorrechten.

</li>

<li>

Tippe den folgenden Befehl ein und drücke die Eingabetaste:

```console
PS> wsl --install -d Ubuntu-26.04
```

Windows schaltet die nötigen Funktionen ein, lädt den Linux-Kernel und die Distribution herunter und richtet beides ein.

</li>

<li>

Starte den Rechner neu, wenn du dazu aufgefordert wirst.

</li>

<li>

Nach dem Neustart öffnet sich Ubuntu von selbst, sonst startest du es über das Startmenü. Beim ersten Start fragt Ubuntu nach einem Benutzernamen und einem Passwort. Wähle einen kurzen Namen aus Kleinbuchstaben ohne Leerzeichen, etwa `student`. Beim Eintippen des Passworts erscheinen keine Zeichen; das ist Absicht. Merke dir das Passwort gut: Linux fragt später danach, wenn du Aufgaben der Systemverwaltung erledigst.

</li>

</ol>

Ist WSL auf dem Rechner schon eingerichtet, etwa mit einer anderen Distribution, zeigt `wsl --install` nur einen Hilfetext. Dann installiert der Befehl aus Schritt 2 die Distribution trotzdem, und `wsl --list --online` zeigt, welche es gibt.

::::beispiel Was WSL bei der Einrichtung herunterlädt
Die Distribution kommt als eine einzige Datei, die alle Dateien eines Ubuntu-Systems enthält. Canonical stellt sie für Ubuntu 26.04.1 unter dem Namen `ubuntu-26.04.1-wsl-amd64.wsl` bereit, rund 400 MB groß. WSL packt sie bei der Einrichtung in eine virtuelle Festplatte aus, die ab dann das Linux-System enthält.
::::

⁠**Kurz gesagt:** `wsl --install -d Ubuntu-26.04` in einer Administrator-PowerShell, Neustart, Benutzer anlegen.

:::hintergrund Wem das Linux-Konto gehört
Der Benutzer, den du beim ersten Start anlegst, gehört nur zu dieser einen Distribution und hat mit deinem Windows-Konto nichts zu tun. Er ist in Ubuntu ein Administrator des Systems: Mit seinem Passwort darf er Aufgaben erledigen, für die man besondere Rechte braucht, etwa Software installieren. Wie das funktioniert, erklärt [Kapitel 7](/wissen/informatik/linux-und-kommandozeile/benutzer-gruppen-und-rechte/benutzer-gruppen-und-rechte.html). Hast du das Passwort vergessen, lässt es sich von Windows aus zurücksetzen, weil Windows als Wirt die VM vollständig kontrolliert.
:::

### Die Distributionen anzeigen

<span class="anker" id="stufe-4-3"></span>

Nach der Einrichtung willst du wissen, ob alles geklappt hat. Drei Befehle in einer gewöhnlichen PowerShell, ohne Administratorrechte, geben Auskunft.

::::beispiel Was WSL über sich verrät
Der erste Befehl listet die Distributionen auf diesem Rechner, der zweite die Versionsnummern, der dritte alle Distributionen, die man einrichten könnte (hier gekürzt):

```console Windows (PowerShell)
PS> wsl -l -v
  NAME            STATE           VERSION
* Ubuntu-26.04    Stopped         2
PS> wsl --version
WSL-Version: 2.6.3.0
Kernelversion: 6.6.87.2-1
WSLg-Version: 1.0.71
MSRDC-Version: 1.2.6353
Direct3D-Version: 1.611.1-81528511
DXCore-Version: 10.0.26100.1-240331-1435.ge-release
Windows-Version: 10.0.26200.9711
PS> wsl -l -o
Im Folgenden finden Sie eine Liste gültiger Distributionen, die installiert werden können.
Mit "wsl.exe --install <Distro>" installieren.

NAME                            FRIENDLY NAME
Ubuntu                          Ubuntu
Ubuntu-26.04                    Ubuntu 26.04 LTS
Ubuntu-24.04                    Ubuntu 24.04 LTS
Ubuntu-22.04                    Ubuntu 22.04 LTS
kali-linux                      Kali Linux Rolling
Debian                          Debian GNU/Linux
archlinux                       Arch Linux
FedoraLinux-45                  Fedora Linux 45
```

In der ersten Liste steht eine Distribution namens `Ubuntu-26.04`; das Sternchen markiert sie als Standard, also als die, die WSL ohne weitere Angabe startet. `STATE` sagt, ob sie gerade läuft (`Running`) oder angehalten ist (`Stopped`), und `VERSION 2` bestätigt WSL 2. Der zweite Befehl nennt die Version von WSL selbst und die Version des Linux-Kernels von Microsoft; auf deinem Rechner können die Nummern neuer sein. In der dritten Liste steht `Ubuntu` ohne Nummer für die jeweils neueste LTS-Version, `Ubuntu-26.04` für genau diese.
::::

⁠**Kurz gesagt:** `wsl -l -v` zeigt, welche Distributionen eingerichtet sind und ob sie unter WSL 2 laufen.

### Das Terminal öffnen und prüfen

<span class="anker" id="stufe-4-4"></span>

Ein Linux-Terminal in WSL öffnest du auf einem von drei Wegen: über das Startmenü, in dem die Distribution mit ihrem Namen steht, im Programm „Terminal“ von Windows über den Pfeil neben dem Plus-Zeichen und den Eintrag `Ubuntu-26.04`, oder in einer PowerShell mit dem Befehl `wsl`. Es erscheint die Eingabeaufforderung `student@labor:~$`, wobei statt `student` dein Benutzername und statt `labor` der Name deines Rechners steht.

::::beispiel Drei Befehle zur Prüfung
Der erste Befehl ist dir aus Unterabschnitt [2.3](drei-wege-zu-einem-eigenen-linux.html#stufe-2-3) bekannt, hier nur mit der ersten Zeile; der zweite nennt die Version des laufenden Kernels, der dritte, ob das System in einer virtuellen Maschine läuft:

```console Linux (WSL 2)
$ cat /etc/os-release
PRETTY_NAME="Ubuntu 26.04.1 LTS"
...
$ uname -r
6.6.87.2-microsoft-standard-WSL2
$ systemd-detect-virt
wsl
```

Die drei Punkte stehen für die übrigen Zeilen der Datei. Der Kernel trägt `microsoft` im Namen, denn Microsoft hat ihn gebaut; er ist ein anderer als der Kernel, den Ubuntu auf einem echten PC benutzt. Der dritte Befehl bestätigt, dass Linux in der VM von WSL läuft.
::::

⁠**Kurz gesagt:** Im WSL-Terminal zeigen `cat /etc/os-release` die Distribution und `uname -r` den Kernel von Microsoft.

### Windows-Dateien in Linux: /mnt/c

<span class="anker" id="stufe-4-5"></span>

Oft liegt eine Datei, die man in Linux bearbeiten will, schon unter Windows, etwa im Ordner „Downloads“. Linux in WSL kommt an das ganze Laufwerk C: heran, aber unter einem ungewohnten Namen.

**Ein Baum ohne Laufwerksbuchstaben.** Unter Linux gibt es keine Laufwerksbuchstaben wie C: oder D:. Alle Dateien und Ordner hängen in einem einzigen Baum, dessen Wurzel `/` heißt; ein Ordner darin wird mit Schrägstrichen beschrieben, etwa `/etc` oder `/home/student`. Wie man sich in diesem Baum bewegt, erklärt [Kapitel 3](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-verzeichnisse-und-pfade.html). WSL zeigt das Laufwerk C: von Windows im Ordner `/mnt/c`, D: unter `/mnt/d` und so weiter.

::::beispiel Ein Windows-Ordner, von Linux aus gesehen
Der Befehl `ls` zeigt, was in einem Ordner liegt. Der Ordner `/mnt` enthält die Laufwerke, und in einem Ordner tief im Windows-Verzeichnis liegen Dateien, die Windows für das Netz braucht:

```console Linux (WSL 2)
$ ls /mnt
c  wsl  wslg
$ ls /mnt/c/Windows/System32/drivers/etc
hosts  hosts.ics  lmhosts.sam  networks  protocol  services
```

Die Regel lautet: Laufwerksbuchstabe klein unter `/mnt`, Schrägstriche statt umgekehrter Schrägstriche. Aus dem Windows-Ordner `C:\Windows\System32\drivers\etc` wird so in Linux der Ordner `/mnt/c/Windows/System32/drivers/etc`.
::::

Unter `/mnt/c` gilt eine Besonderheit. Linux unterscheidet sonst überall zwischen Groß- und Kleinbuchstaben, `Notiz.txt` und `notiz.txt` sind zwei verschiedene Dateien. Auf dem Windows-Laufwerk gelten aber die Regeln von Windows, und dort ist die Schreibweise egal: `/mnt/c/windows/system32` führt zum selben Ordner wie `/mnt/c/Windows/System32`.

⁠**Kurz gesagt:** Linux in WSL findet Laufwerk C: unter `/mnt/c`.

### Linux-Dateien in Windows: der Explorer

<span class="anker" id="stufe-4-6"></span>

Umgekehrt will man manchmal eine Datei, die in Linux entstanden ist, mit einem Windows-Programm öffnen. Der Windows-Explorer zeigt dafür links in der Navigationsleiste einen Eintrag „Linux“; darunter steht jede eingerichtete Distribution mit ihrem ganzen Baum.

Die Adresse eines Linux-Ordners beginnt im Explorer mit `\\wsl.localhost\` und dem Namen der Distribution. Der persönliche Ordner von `student` in Ubuntu-26.04 heißt also `\\wsl.localhost\Ubuntu-26.04\home\student`. Ältere Anleitungen schreiben `\\wsl$\` statt `\\wsl.localhost\`; beide Schreibweisen führen zum selben Ziel. Aus einem Linux-Terminal heraus öffnet der Befehl `explorer.exe .` den Explorer genau in dem Ordner, in dem man gerade arbeitet; der Punkt am Ende gehört dazu.

::::beispiel Eine Linux-Datei, von Windows aus gesehen
Im persönlichen Ordner in Ubuntu liegt ein Ordner `linuxk1` und darin ein Ordner `pruefung` mit drei kleinen Dateien. Die PowerShell zeigt sie unter der Explorer-Adresse an:

```console Windows (PowerShell)
PS> Get-ChildItem \\wsl.localhost\Ubuntu-26.04\home\student\linuxk1\pruefung

    Verzeichnis: \\wsl.localhost\Ubuntu-26.04\home\student\linuxk1\pruefung


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
------        09.11.2026     16:32             12 gruss2.txt
------        09.11.2026     16:32             76 PRUEFSUMMEN
------        09.11.2026     16:32             12 gruss.txt
```

Die Reihenfolge der Dateien ist hier nicht alphabetisch, sondern die, in der der Dateiserver auf der Linux-Seite sie liefert.
::::

:::warnung Die Dateien von WSL nur über `\\wsl.localhost` anfassen
Das ganze Linux-System von WSL steckt in einer einzigen Datei namens `ext4.vhdx`, die Windows tief im Ordner `AppData` deines Windows-Benutzers ablegt. Öffne, verschiebe oder lösche diese Datei nie mit Windows-Programmen, und bearbeite nichts in ihrem Ordner: Das kann die Distribution so beschädigen, dass sie nicht mehr startet. Der sichere Weg zu Linux-Dateien führt immer über den Eintrag „Linux“ im Explorer, also über `\\wsl.localhost`.
:::

⁠**Kurz gesagt:** Windows sieht die Linux-Dateien im Explorer unter „Linux“; die Adresse lautet `\\wsl.localhost\Ubuntu-26.04`.

### Wohin mit den Übungsdateien?

<span class="anker" id="stufe-4-7"></span>

Weil beide Seiten an beide Dateien kommen, liegt die Frage nahe, wo man seine Übungsdateien am besten ablegt. Die Antwort ist eindeutig: im Linux-Teil, zum Beispiel im persönlichen Ordner `/home/student`, und nicht unter `/mnt/c`, wenn man vor allem in Linux mit ihnen arbeitet. Auch Microsoft empfiehlt das.

::::beispiel Dasselbe Kopieren, zweimal gemessen
Für dieses Kapitel wurde ein Ordner mit 3 559 kleinen Dateien, zusammen 52 MB, in WSL zweimal kopiert: einmal in den persönlichen Ordner in Linux, einmal in einen Ordner auf C: unter `/mnt/c`. Im Linux-Teil dauerte das zwischen 0,13 und 0,69 Sekunden, unter `/mnt/c` jedes Mal etwa 37 Sekunden. Das ist rund fünfzig- bis dreihundertmal so lange, oder etwa 10 Millisekunden für jede einzelne Datei. Das Skript dazu liegt bei den Code-Dateien dieses Kapitels.
::::

⁠**Kurz gesagt:** Dateien, mit denen du in Linux arbeitest, gehören in den Linux-Teil, nicht nach `/mnt/c`.

:::hintergrund Warum der Weg über die Grenze so viel länger dauert
Linux und Windows laufen in zwei getrennten Maschinen, und keine kann die Datenträger der anderen direkt lesen. Greift Linux auf `/mnt/c` zu, wird jeder einzelne Schritt, also Datei anlegen, öffnen, schreiben, schließen, Eigenschaften setzen, zu einer Nachricht an ein Programm auf der Windows-Seite. Dieses Programm, ein Dateiserver, führt den Schritt mit dem Windows-Kernel aus und schickt die Antwort zurück. Die Nachrichten folgen einem festen Protokoll namens 9P. Beim Kopieren vieler kleiner Dateien besteht die Arbeit fast nur aus solchen Einzelschritten, und jeder kostet eine Hin- und Rückreise über die Grenze der VM. Im Linux-Teil dagegen erledigt der Linux-Kernel dieselben Schritte unmittelbar auf seiner eigenen virtuellen Festplatte. In der Gegenrichtung, wenn Windows über `\\wsl.localhost` Linux-Dateien liest, arbeitet ein Dateiserver auf der Linux-Seite nach demselben Muster.
:::

### Grenzen von WSL 2

<span class="anker" id="stufe-4-8"></span>

WSL 2 reicht für alles, was diese Reihe an der Kommandozeile, beim Programmieren und bei der Datenanalyse zeigt. An drei Stellen merkt man aber, dass Linux in einer eigenen VM lebt.

<ul>

<li>

⁠**Netz.** Die VM von WSL 2 hängt im NAT-Modus aus Unterabschnitt [3.6](virtuelle-maschinen-der-rechner-im-rechner.html#stufe-3-6) an Windows und bekommt eine eigene Adresse, die sich bei jedem Neustart ändern kann. Linux kommt ins Internet; von anderen Geräten im Heimnetz ist es ohne zusätzliche Einstellungen nicht erreichbar. Den Verkehr der echten Netzwerkkarte des Rechners sieht Linux nicht.

</li>

<li>

⁠**Geräte.** USB-Geräte, etwa ein USB-WLAN-Stick oder ein Kartenleser, sieht Linux nicht von selbst. Man kann sie mit einem Zusatzprogramm namens usbipd-win an WSL durchreichen; solange sie in WSL hängen, kann Windows sie nicht benutzen.

</li>

<li>

⁠**Aktualisierungen.** Windows aktualisiert WSL und den Linux-Kernel, aber nicht die Programme der Distribution. Die aktualisierst du in Linux selbst, wie Kapitel 9 zeigt.

</li>

</ul>

Wer mehrere Rechner in einem eigenen Netz aufbauen oder den Netzverkehr der echten Netzwerkkarte untersuchen will, nimmt eine VM mit VirtualBox oder den Live-USB-Stick.

⁠**Kurz gesagt:** WSL 2 ist ideal für Kommandozeile und Programmieren; für Netzlabore und eigene Geräte ist es zu weit von der Hardware entfernt.

### Aufgaben zu Abschnitt [4](#stufe-4)

<span class="anker" id="stufe-4-9"></span>

:::aufgabe Aufgabe 11 ★★ WSL 2 einrichten und prüfen
<span class="anker" id="aufg-11"></span>

Richte WSL 2 mit Ubuntu 26.04 ein, wie in Unterabschnitt [4.2](#stufe-4-2) beschrieben. Öffne danach eine gewöhnliche PowerShell und führe `wsl -l -v` aus, dann im Ubuntu-Terminal `cat /etc/os-release` und `uname -r`. Woran erkennst du an den drei Ausgaben, dass (a) Ubuntu 26.04 eingerichtet ist, (b) es unter WSL 2 läuft und (c) der Kernel von Microsoft stammt?

:::loesung
Auf dem Testrechner dieses Kapitels sehen die Ausgaben so aus:

```console Windows (PowerShell)
PS> wsl -l -v
  NAME            STATE           VERSION
* Ubuntu-26.04    Stopped         2
```

```console Linux (WSL 2)
$ cat /etc/os-release
PRETTY_NAME="Ubuntu 26.04.1 LTS"
...
$ uname -r
6.6.87.2-microsoft-standard-WSL2
```

(a) `PRETTY_NAME="Ubuntu 26.04.1 LTS"` und `VERSION_ID="26.04"` in `/etc/os-release` zeigen Ubuntu 26.04. (b) Die Spalte `VERSION` von `wsl -l -v` zeigt `2`. Läuft die Distribution gerade, steht unter `STATE` `Running`. (c) Der Kernel-Name enthält `microsoft-standard-WSL2`: Es ist der von Microsoft gebaute Kernel der VM von WSL 2. Die Nummern davor können auf deinem Rechner neuer sein.
:::
:::

:::aufgabe Aufgabe 12 ★ Dateien über die Grenze
<span class="anker" id="aufg-12"></span>

<ol class="al">

<li>

Lege unter Windows im Ordner „Dokumente“ mit dem Editor eine kleine Textdatei `hallo.txt` an. Wie lautet ihr Name in Linux? Zeige den Inhalt des Ordners mit `ls` an. (Dein Windows-Benutzername steht im Explorer in der Adresse des Ordners.)

</li>

<li>

Öffne im Ubuntu-Terminal mit `explorer.exe .` den Explorer. Welche Adresse zeigt er an?

</li>

</ol>

:::loesung
(a) Liegt die Datei unter Windows in `C:\Users\<Name>\Documents\hallo.txt`, heißt sie in Linux `/mnt/c/Users/<Name>/Documents/hallo.txt`; `<Name>` ist dein Windows-Benutzername. Achtung: Ein deutsches Windows zeigt den Ordner im Explorer als „Dokumente“ an, sein wirklicher Name auf der Platte ist aber `Documents`. Klickst du im Explorer in die Adresszeile, erscheint der wirkliche Pfad. Der Befehl lautet dann zum Beispiel `ls /mnt/c/Users/<Name>/Documents`, und in seiner Ausgabe steht `hallo.txt`. Ist bei dir die Sicherung der Ordner in OneDrive eingeschaltet, liegt „Dokumente“ dagegen im Ordner von OneDrive, und der Pfad beginnt mit `/mnt/c/Users/<Name>/OneDrive`.

(b) Der Explorer öffnet den Ordner, in dem das Terminal gerade arbeitet. Direkt nach dem Öffnen des Terminals ist das dein persönlicher Ordner; die Adresse lautet dann `\\wsl.localhost\Ubuntu-26.04\home\<dein Linux-Name>`.
:::
:::

:::aufgabe Aufgabe 13 ★★ Ist WSL 2 wirklich eine VM?
<span class="anker" id="aufg-13"></span>

Sammle in deinem WSL-Terminal drei Hinweise darauf, dass Linux in einer virtuellen Maschine läuft. Benutze `systemd-detect-virt`, `uname -r` und den Befehl `lsblk -o NAME,SIZE,MODEL`, der die Datenträger des Systems mit ihrer Größe und Bauart auflistet. Was fällt dir an der Bauart der Datenträger auf? Wie passt die Größe des größten Datenträgers zur freien Größe deiner echten SSD?

:::loesung
Auf dem Testrechner dieses Kapitels antworten die drei Befehle so:

```console Linux (WSL 2)
$ systemd-detect-virt
wsl
$ uname -r
6.6.87.2-microsoft-standard-WSL2
$ lsblk -o NAME,SIZE,MODEL
NAME   SIZE MODEL
sda  388.6M Virtual Disk
sdb    186M Virtual Disk
sdc      8G Virtual Disk
sdd      1T Virtual Disk
```

Erster Hinweis: `systemd-detect-virt` erkennt die Umgebung und meldet `wsl`; auf einem echten Rechner würde es `none` melden. Zweiter Hinweis: Der Kernel stammt von Microsoft und nicht von Ubuntu. Dritter Hinweis: Alle Datenträger heißen `Virtual Disk`; es sind virtuelle Festplatten, die WSL der VM als Dateien bereitstellt, keine echten Geräte. Die Größe von `sdd`, `1T`, also 1 TiB, ist nicht die Größe deiner SSD und auch nicht der freie Platz darauf, sondern die Höchstgröße, bis zu der die Datei `ext4.vhdx` wachsen darf. Tatsächlich belegt sie auf der SSD nur so viel, wie Linux an Daten hineingeschrieben hat.
:::
:::

:::aufgabe Aufgabe 14 ★★ Wohin mit dem Projekt?
<span class="anker" id="aufg-14"></span>

Ein Kommilitone legt sein Python-Projekt mit 2 000 kleinen Dateien unter `C:\Users\max\projekt` ab und arbeitet in WSL im Ordner `/mnt/c/Users/max/projekt`. Er wundert sich, dass jeder Testlauf eine halbe Minute braucht. Erkläre ihm, woran das vermutlich liegt, schätze mit den gemessenen Zeiten aus Unterabschnitt [4.7](#stufe-4-7) ab, wie viel Zeit allein das einmalige Anlegen aller Dateien über die Grenze kostet, und schlage eine bessere Ablage vor. Wie kommt er dann von Windows aus an seine Dateien?

:::loesung
Das Projekt liegt auf der Windows-Seite, und die Tests laufen in Linux. Jeder Dateizugriff der Tests geht deshalb als Nachricht über die Grenze der VM zum Dateiserver auf der Windows-Seite und zurück. Bei vielen kleinen Dateien kostet das ein Vielfaches der Zeit.

Abschätzung mit der Messung aus Unterabschnitt [4.7](#stufe-4-7): 37 Sekunden für 3 559 Dateien sind etwa 10 ms je Datei. Allein das einmalige Anlegen von 2 000 Dateien über die Grenze dauert damit grob

$$2\,000\cdot10\ \mathrm{ms}=20\ \mathrm{s}.$$

Das ist nur eine Schätzung, denn Lesen, Schreiben und Prüfen kosten je nach Art unterschiedlich viel; sie zeigt aber, dass eine halbe Minute je Testlauf leicht allein durch die Grenze entsteht.

Besser: Das Projekt in den Linux-Teil verschieben, etwa nach `/home/max/projekt`, und dort arbeiten. Von Windows aus erreicht Max es dann im Explorer unter „Linux“ bzw. unter `\\wsl.localhost\Ubuntu-26.04\home\max\projekt`. Jetzt geht der Weg über die Grenze nur noch dann, wenn er von Windows aus eine Datei öffnet, nicht bei jedem Testlauf.
:::
:::

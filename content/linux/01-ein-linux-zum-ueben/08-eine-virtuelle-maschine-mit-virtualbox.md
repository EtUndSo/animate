---
title: Eine virtuelle Maschine mit VirtualBox
pfad: Informatik / Linux und Kommandozeile / Ein Linux zum Üben: WSL, virtuelle Maschine, Live-USB-Stick
adresse: informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick
knoten: Kapitel 1: Ein Linux zum Üben: WSL, virtuelle Maschine, Live-USB-Stick
order: 6060800
summary: Dieser Abschnitt richtet den zweiten Weg ein: eine virtuelle Maschine mit VirtualBox, in der Ubuntu 26.04 installiert wird.
tags: 
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Dieser Abschnitt richtet den zweiten Weg ein: eine virtuelle Maschine mit VirtualBox, in der Ubuntu 26.04 installiert wird. Er setzt die Begriffe aus Abschnitt [3](virtuelle-maschinen-der-rechner-im-rechner.html#stufe-3), das Abbild aus Abschnitt [5](datentrager-abbild-und-prufsumme.html#stufe-5) und die Startkette aus Abschnitt [6](wie-ein-pc-startet.html#stufe-6) voraus. Am Ende hast du ein Übungs-Linux mit einem Snapshot, zu dem du jederzeit zurückkehren kannst.
:::

### VirtualBox einrichten

<span class="anker" id="stufe-7-1"></span>

VirtualBox ist der Hypervisor, mit dem dieser Weg arbeitet. Er ist kostenlos, läuft unter Windows, macOS und Linux und ist im Kern freie Software unter der GNU General Public License in Version 3.

**Schritte.** So richtest du VirtualBox ein:

<ol>

<li>

Lade auf [https://www.virtualbox.org](https://www.virtualbox.org) unter „Downloads“ das Paket für Windows-Wirte (Windows hosts) herunter. Diese Reihe benutzt VirtualBox 7.2.

</li>

<li>

Starte die Datei und folge dem Installationsprogramm mit den vorgeschlagenen Einstellungen. Es fragt nach Administratorrechten und richtet ein virtuelles Netzwerkgerät ein; die Netzverbindung kann dabei kurz abbrechen.

</li>

<li>

Das *Extension Pack*, das auf derselben Seite angeboten wird, brauchst du nicht. Es enthält Zusatzfunktionen, die für ein Übungs-Linux keine Rolle spielen, und steht unter einer eigenen Lizenz, die die kostenlose Nutzung auf private und schulische Zwecke beschränkt.

</li>

</ol>

::::beispiel VirtualBox neben WSL 2
Ist auf dem Rechner WSL 2 eingerichtet oder eine Sicherheitsfunktion aktiv, die den Hypervisor von Microsoft benutzt, kann VirtualBox nicht selbst direkt an die Hardware-Virtualisierung. Es benutzt dann den Hypervisor von Microsoft als Unterbau, wie im Hintergrund-Kasten in Unterabschnitt [3.3](virtuelle-maschinen-der-rechner-im-rechner.html#stufe-3-3) beschrieben. Die VM läuft trotzdem, aber spürbar langsamer; VirtualBox zeigt das unten rechts im Fenster der VM durch eine kleine grüne Schildkröte an. Für ein Übungs-Linux ist das kein Hindernis.
::::

⁠**Kurz gesagt:** VirtualBox von [https://www.virtualbox.org](https://www.virtualbox.org) installieren, ohne Extension Pack.

### Die Hardware-Virtualisierung einschalten

<span class="anker" id="stufe-7-2"></span>

Zeigt der Task-Manager „Virtualisierung: Aktiviert“ (Aufgabe [7](virtuelle-maschinen-der-rechner-im-rechner.html#aufg-7)), überspringst du diesen Unterabschnitt. Steht dort „Deaktiviert“, muss die Hardware-Virtualisierung aus Unterabschnitt [3.4](virtuelle-maschinen-der-rechner-im-rechner.html#stufe-3-4) in der Firmware eingeschaltet werden.

:::warnung Nur die eine Einstellung ändern
Eine Änderung in der Firmware ist ein Eingriff in die Startkette. Sichere vorher den Wiederherstellungsschlüssel, wie in Unterabschnitt [6.5](wie-ein-pc-startet.html#stufe-6-5) beschrieben. Ändere in der Firmware nur die Einstellung für die Virtualisierung und nichts anderes, auch nicht Secure Boot oder die Bootreihenfolge; Microsoft rät ausdrücklich, in der Firmware nur zu ändern, was man wirklich braucht. Bist du unsicher, verlasse die Firmware ohne zu speichern.
:::

**Schritte.** Öffne über Einstellungen $\to$ System $\to$ Wiederherstellung $\to$ Erweiterter Start $\to$ „Jetzt neu starten“ $\to$ „Problembehandlung“ $\to$ „Erweiterte Optionen“ $\to$ „UEFI-Firmwareeinstellungen“ die Firmware. Die Einstellung heißt je nach Hersteller etwa „Intel Virtualization Technology“, „Intel VT-x“, „SVM Mode“ oder „AMD-V“ und steht meist unter „Advanced“, „CPU Configuration“ oder „Security“. Stelle sie auf „Enabled“, speichere und starte neu. Danach zeigt der Task-Manager „Aktiviert“.

⁠**Kurz gesagt:** Ist die Hardware-Virtualisierung aus, schaltet man nur diese eine Einstellung in der Firmware ein, mit gesichertem Wiederherstellungsschlüssel.

### Eine VM anlegen

<span class="anker" id="stufe-7-3"></span>

Für die VM brauchst du das Abbild `ubuntu-26.04.1-desktop-amd64.iso` von [https://ubuntu.com/download/desktop](https://ubuntu.com/download/desktop), geprüft wie in Unterabschnitt [5.6](datentrager-abbild-und-prufsumme.html#stufe-5-6). Dann legst du in VirtualBox eine neue VM an.

**Schritte.** Klicke in VirtualBox auf „Neu“. Der Assistent fragt nacheinander:

<ol>

<li>

⁠**Name und Abbild.** Gib einen Namen ein, etwa `ubuntu-labor`, und wähle das geprüfte ISO-Abbild. VirtualBox erkennt daran Typ und Version des Systems.

</li>

<li>

⁠**Unbeaufsichtigte Installation überspringen.** VirtualBox bietet an, Ubuntu von selbst zu installieren. Lehne das ab: Je nach Version setzt du dafür ein Häkchen bei „Unbeaufsichtigte Installation überspringen“ oder entfernst das Häkchen bei der unbeaufsichtigten Installation. Mit neuen Ubuntu-Versionen klappt sie nicht immer, und von Hand siehst du, was geschieht.

</li>

<li>

⁠**Arbeitsspeicher und Prozessoren.** Ubuntu 26.04 braucht laut Hersteller mindestens 6 GB Arbeitsspeicher und einen Prozessor mit zwei Kernen. Gib der VM 6 GB (6 144 MB) und 2 Prozessoren, wenn dein Rechner 16 GB oder mehr hat.

</li>

<li>

⁠**Festplatte.** Lege eine neue virtuelle Festplatte mit mindestens 25 GB an. Lass die Voreinstellung, dass die Datei erst mit ihrem Inhalt wächst.

</li>

</ol>

Ob die VM mit UEFI oder der alten BIOS-Betriebsart startet, spielt für Ubuntu keine Rolle; lass die Voreinstellung.

::::beispiel Arbeitsspeicher planen
Auf einem Rechner mit 16 GB bleiben neben einer VM mit 6 GB noch 10 GB für Windows und seine Programme; das reicht. Mit 32 GB kann man der VM auch 8 GB geben, und es bleiben 24 GB. Auf einem Rechner mit nur 8 GB blieben für Windows bloß 2 GB, und beide Systeme würden quälend langsam. Dort nimmt man besser WSL 2, das sich seinen Arbeitsspeicher nach Bedarf nimmt und wieder freigibt.
::::

⁠**Kurz gesagt:** Neue VM mit dem geprüften Abbild, ohne unbeaufsichtigte Installation, mit 6 GB Arbeitsspeicher, 2 Prozessoren und 25 GB Platte.

:::hintergrund Warum eine 25-GB-Platte anfangs kaum Platz braucht
Die Datei einer neuen virtuellen Festplatte enthält zunächst nur ihre Verwaltungsangaben. Erst wenn der Gast einen Sektor beschreibt, legt VirtualBox den Platz dafür in der Datei an. Sektoren, die nie beschrieben wurden, liest der Gast als Nullen, ohne dass sie irgendwo gespeichert sind. Unter Linux gibt es dasselbe Prinzip für gewöhnliche Dateien: Bei den Versuchen für dieses Kapitel war eine Abbilddatei mit der Größe einer 512-GB-SSD, die nur eine Partitionstabelle enthielt, auf der echten Platte gerade 40 KiB groß.
:::

### Ubuntu in der VM installieren

<span class="anker" id="stufe-7-4"></span>

Startest du die neue VM, verhält sie sich wie ein frisch gekaufter Rechner mit eingelegter DVD: Ihre virtuelle Firmware findet auf der leeren Festplatte nichts und startet vom virtuellen DVD-Laufwerk, in dem das Abbild steckt. Es erscheint das Installationsprogramm von Ubuntu.

**Schritte.** Im Installationsprogramm wählst du nacheinander die Sprache, die Barrierefreiheit, die Tastaturbelegung und die Internetverbindung; im NAT-Modus hat die VM schon eine Verbindung. Dann folgt die Frage „Ubuntu ausprobieren“ oder „Ubuntu installieren“: Wähle hier, in der VM, das Installieren. Bei der Art der Installation wählst du die einfache Variante, die die ganze Festplatte benutzt, danach Benutzername, Passwort und Zeitzone. Nach der Installation startet die VM neu; das Abbild entfernt VirtualBox dabei in der Regel von selbst aus dem virtuellen DVD-Laufwerk.

::::beispiel „Festplatte löschen“ in der VM
Das Installationsprogramm bietet an, die ganze Festplatte zu löschen und Ubuntu darauf zu installieren. Auf einem echten Rechner würde das Windows mit allen Daten vernichten. In der VM betrifft es nur die virtuelle Festplatte, also die neue, leere Datei aus Unterabschnitt [7.3](#stufe-7-3). Die SSD des Wirts sieht der Gast gar nicht, er kann sie deshalb auch nicht löschen.
::::

⁠**Kurz gesagt:** In der VM installiert man Ubuntu ganz normal, denn alles, was das Installationsprogramm löscht, ist die virtuelle Festplatte.

### Der erste Snapshot

<span class="anker" id="stufe-7-5"></span>

Direkt nach der Installation ist das System sauber. Diesen Zustand hältst du fest, bevor du irgendetwas ausprobierst.

**Schritte.** Fahre Ubuntu in der VM herunter. Wähle in VirtualBox die VM aus und öffne über das Menü neben ihrem Namen die Ansicht der Snapshots; die deutsche Oberfläche nennt sie „Sicherungspunkte“. Erstelle dort einen neuen Snapshot und nenne ihn `sauber`. Willst du später zurück, wählst du ihn in derselben Ansicht aus und stellst ihn wieder her; VirtualBox bietet dabei an, den aktuellen Zustand vorher selbst als Snapshot zu sichern.

:::warnung Zurückspielen verwirft alles, was danach kam
Kehrst du zu einem Snapshot zurück, ist alles weg, was die VM seit diesem Snapshot gespeichert hat, auch deine eigenen Dateien. Willst du etwas behalten, sichere es vorher als neuen Snapshot oder kopiere es aus der VM heraus.
:::

⁠**Kurz gesagt:** Nach der Installation einen Snapshot „sauber“ anlegen; zurückkehren kann man jederzeit, verliert dabei aber alles Spätere.

### Das Terminal in der VM

<span class="anker" id="stufe-7-6"></span>

In Ubuntu öffnest du das Terminal mit der Tastenkombination Strg+Alt+T oder über die Programmübersicht, in der du „Terminal“ eintippst. Dort prüfst du wie bei WSL 2 die Distribution und den Kernel mit `cat /etc/os-release` und `uname -r`. Die Distribution meldet sich mit denselben Zeilen wie in Unterabschnitt [2.3](drei-wege-zu-einem-eigenen-linux.html#stufe-2-3). Der Kernel ist dagegen ein anderer als in WSL 2: In der VM läuft der Kernel, den Ubuntu selbst für PCs baut. Sein Name trägt kein `microsoft`, sondern endet bei Ubuntu für Arbeitsplatzrechner auf `-generic`.

Die VM ist im NAT-Modus aus Unterabschnitt [3.6](virtuelle-maschinen-der-rechner-im-rechner.html#stufe-3-6) mit dem Netz verbunden: Sie kommt ins Internet, ist aber von außen nicht erreichbar.

⁠**Kurz gesagt:** Strg+Alt+T öffnet in Ubuntu das Terminal; `uname -r` zeigt dort den Kernel von Ubuntu.

### Aufgaben zu Abschnitt [7](#stufe-7)

<span class="anker" id="stufe-7-7"></span>

:::aufgabe Aufgabe 21 ★★ Eine VM mit Snapshot
<span class="anker" id="aufg-21"></span>

Richte VirtualBox ein, lege eine VM mit Ubuntu 26.04 an, installiere Ubuntu darin und erstelle den Snapshot `sauber`. Prüfe im Terminal der VM mit `cat /etc/os-release` und `uname -r`. Lege dann auf dem Schreibtisch der VM eine Datei `test.txt` an, fahre die VM herunter und kehre zum Snapshot `sauber` zurück. Was erwartest du, bevor du die VM wieder startest? Prüfe es.

:::loesung
Nach dem Zurückkehren zum Snapshot `sauber` ist `test.txt` verschwunden. Die Datei wurde nach dem Snapshot angelegt und stand deshalb im Differenzabbild, das beim Zurückspielen verworfen wird. Die VM startet im Zustand direkt nach der Installation. In der Terminalausgabe der VM zeigt `cat /etc/os-release` dieselben Zeilen wie in Unterabschnitt [2.3](drei-wege-zu-einem-eigenen-linux.html#stufe-2-3), und `uname -r` einen Kernel, dessen Name auf `-generic` endet und kein `microsoft` enthält.
:::
:::

:::aufgabe Aufgabe 22 ★★ Warum „Festplatte löschen“ in der VM harmlos ist
<span class="anker" id="aufg-22"></span>

Erkläre mit den Begriffen Gast, Hypervisor und virtuelle Festplatte, warum die Wahl „Festplatte löschen und Ubuntu installieren“ in der VM die Dateien von Windows nicht gefährdet. Welche Datei auf dem Wirt verändert der Gast dabei tatsächlich? Was müsste geschehen, damit der Gast die SSD des Wirts doch beschreiben könnte?

:::loesung
Der Gast sieht nur die Hardware, die der Hypervisor ihm nachbildet. Als Festplatte sieht er die virtuelle Festplatte, und die ist auf dem Wirt eine gewöhnliche Datei, bei VirtualBox in der Voreinstellung `ubuntu-labor.vdi` im Ordner `VirtualBox VMs\ubuntu-labor` des Windows-Benutzers. Wenn das Installationsprogramm „die ganze Festplatte löscht“, schreibt der Gast-Kernel neue Partitionen und Dateisysteme auf diese virtuelle Festplatte. Jeder dieser Schreibzugriffe ist ein privilegierter Gerätezugriff, den der Hypervisor abfängt und in diese eine Datei schreibt. Die SSD des Wirts mit Windows ist kein Gerät der VM; der Gast weiß nicht einmal, dass es sie gibt.

Damit der Gast die SSD des Wirts beschreiben könnte, müsste man sie ihm ausdrücklich als Gerät zuteilen; VirtualBox kann das, aber nur über eine Einstellung für Fachleute, die man hier nie benutzt. An einzelne Dateien des Wirts käme der Gast außerdem, wenn man ihm einen Ordner des Wirts freigibt; auch das geschieht nur auf ausdrücklichen Wunsch. Sonst bliebe nur ein Fehler im Hypervisor selbst, der die Trennung zwischen Gast und Wirt durchbricht.
:::
:::

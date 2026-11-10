---
title: Das Wichtigste bis hier
pfad: Informatik / Linux und Kommandozeile / Ein Linux zum Üben: WSL, virtuelle Maschine, Live-USB-Stick
adresse: informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick
knoten: Kapitel 1: Ein Linux zum Üben: WSL, virtuelle Maschine, Live-USB-Stick
order: 6061100
summary: WSL 2, virtuelle Maschine und Live-USB-Stick: was dabei im Rechner geschieht und wie man es sicher macht
tags: 
lang: de
---

:::kern Das Wichtigste bis hier
<ul>

<li>

Das Betriebssystem verwaltet die Hardware; sein Kern, der Kernel, läuft als einziger Teil im Kernel-Modus. Programme laufen im Benutzermodus und bekommen Hardware-Dienste nur über Systemaufrufe.

</li>

<li>

Linux ist ein Kernel; eine Distribution wie Ubuntu 26.04 LTS macht daraus ein vollständiges System und pflegt es als LTS-Version fünf Jahre lang.

</li>

<li>

Eine virtuelle Maschine ist ein Rechner aus Software. Der Hypervisor teilt ihr Hardware zu; dank Hardware-Virtualisierung läuft der Gast direkt auf dem Prozessor, und alles, was die echte Maschine beträfe, landet beim Hypervisor. Ein Snapshot friert den Zustand ein, NAT lässt die VM hinaus, aber niemanden herein.

</li>

<li>

WSL 2 ist ein echter Linux-Kernel in einer kleinen VM, die Windows verwaltet. Linux sieht C: unter `/mnt/c`, Windows die Linux-Dateien unter `\\wsl.localhost`; Übungsdateien gehören in den Linux-Teil.

</li>

<li>

Ein Abbild ist ein ganzer Datenträger in einer Datei. Die SHA-256-Prüfsumme beweist, dass es unverändert ist, aber nicht, dass es echt ist; das belegt erst eine Signatur.

</li>

<li>

Beim Start lädt die Firmware den Bootloader und dieser den Kernel; Secure Boot lässt nur Startprogramme mit gültiger Signatur zu. Die Geräteverschlüsselung von Windows hängt an dieser Kette, deshalb sichert man vor jedem Eingriff den Wiederherstellungsschlüssel.

</li>

<li>

Ein Live-System legt ein beschreibbares tmpfs im Arbeitsspeicher als Overlay über ein schreibgeschütztes squashfs; nach dem Ausschalten ist alles weg, die interne SSD bleibt uneingehängt.

</li>

<li>

Beim Live-Stick entstehen fast alle Risiken durch einen falschen Datenträger oder Änderungen an der Startkette: andere Speicher abziehen, Stick an der Größe erkennen, „Neu starten“, Bootmenü, Secure Boot an, „Ubuntu ausprobieren“.

</li>

</ul>
:::

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Ein eigenes Linux zum Üben bekommt man unter Windows auf drei Wegen: mit WSL 2 als kleine VM neben Windows, mit einer virtuellen Maschine in VirtualBox oder als Live-System vom USB-Stick.

</li>

<li>

Alle drei schützen Windows, weil zwischen dem Übungs-Linux und den Windows-Daten eine Grenze liegt: der Hypervisor bei WSL 2 und der VM, der Arbeitsspeicher statt der SSD beim Live-System.

</li>

<li>

Gefährlich wird es nur dort, wo man diese Grenze selbst überschreitet, beim Beschreiben eines Datenträgers und bei Änderungen an der Startkette, und dagegen helfen ein geprüftes Abbild, der richtig erkannte Stick, der unveränderte Start über das Bootmenü und ein gesicherter Wiederherstellungsschlüssel.

</li>

</ol>
:::

**Ein Prinzip hinter allen Ergebnissen.** Fast alles in diesem Kapitel folgt aus einem Gedanken: Sicherheit entsteht durch Schichten, die eine untere vor einer oberen schützen, und jede Schicht ist nur so sicher wie der Weg durch sie hindurch. Der Kernel schützt die Hardware vor den Programmen, der Hypervisor den Wirt vor dem Gast, die Signaturprüfung die Startkette vor fremden Programmen, die schreibgeschützte Schicht das Live-System vor Änderungen.

| Ergebnis | Woher es kommt |
|---|---|
| Programme kommen nicht direkt an die SSD | Kernel-Modus und Benutzermodus, Systemaufruf als einziges Tor (Abschnitt [1](betriebssystem-kernel-und-distribution.html#stufe-1)) |
| Ubuntu und Kali teilen den Kernel, nicht das System | Linux ist der Kernel, die Distribution das Ganze (Abschnitt [1](betriebssystem-kernel-und-distribution.html#stufe-1)) |
| ein Gast kann den Wirt nicht steuern | was die echte Maschine beträfe, landet beim Hypervisor (Abschnitt [3](virtuelle-maschinen-der-rechner-im-rechner.html#stufe-3)) |
| ein Snapshot ist sofort fertig | Differenzabbild nach dem Prinzip copy on write (Abschnitt [3](virtuelle-maschinen-der-rechner-im-rechner.html#stufe-3)) |
| eine VM im NAT-Modus ist von außen unerreichbar | der Hypervisor stellt nur Antworten auf eigene Anfragen zu (Abschnitt [3](virtuelle-maschinen-der-rechner-im-rechner.html#stufe-3)) |
| `uname -r` zeigt in WSL 2 einen Kernel von Microsoft | WSL 2 ist eine VM mit eigenem Linux-Kernel (Abschnitt [4](wsl-2-linux-neben-windows.html#stufe-4)) |
| Kopieren unter `/mnt/c` dauert ein Vielfaches | jeder Dateizugriff wird zur Nachricht über die Grenze der VM (Abschnitt [4](wsl-2-linux-neben-windows.html#stufe-4)) |
| eine stimmende Prüfsumme beweist keine Herkunft | wer die Datei tauscht, kann auch die Liste tauschen (Abschnitt [5](datentrager-abbild-und-prufsumme.html#stufe-5)) |
| ein fremder Stick startet ohne Einrichtung | fester Startpfad für Wechseldatenträger in UEFI (Abschnitt [6](wie-ein-pc-startet.html#stufe-6)) |
| Ubuntu startet mit Secure Boot, Kali nicht | signierte Kette `shim`, GRUB, Kernel (Abschnitt [6](wie-ein-pc-startet.html#stufe-6)) |
| eine Firmware-Änderung kann den Wiederherstellungsschlüssel verlangen | der Schlüssel wird nur bei unveränderter Startkette freigegeben (Abschnitt [6](wie-ein-pc-startet.html#stufe-6)) |
| im Live-System ist nach dem Ausschalten alles weg | Änderungen landen im tmpfs über dem squashfs (Abschnitt [8](das-live-system.html#stufe-8)) |
| der falsche Datenträger ist das größte Risiko | ein Schreibwerkzeug ersetzt den ganzen gewählten Datenträger (Abschnitt [9](der-live-usb-stick-vorbereiten-schreiben-starten.html#stufe-9)) |

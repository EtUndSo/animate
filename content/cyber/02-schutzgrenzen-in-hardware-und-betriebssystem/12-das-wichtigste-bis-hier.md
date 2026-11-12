---
title: Das Wichtigste bis hier
pfad: Informatik / Cybersecurity / Schutzgrenzen in Hardware und Betriebssystem
adresse: informatik/cybersecurity/schutzgrenzen-in-hardware-und-betriebssystem
knoten: Kapitel 2: Schutzgrenzen in Hardware und Betriebssystem
order: 6121200
summary: Wer darf was, und wo wird geprüft? Privilegstufen, der Weg in den Kernel, Zeitgeber, Seitentabellen und eine gesicherte Startkette
tags: 
lang: de
---

:::kern Das Wichtigste bis hier
<ul>

<li>

Eine Schutzgrenze trennt Bereiche mit verschiedenen Rechten; die prüfende Stelle ist ein Referenzmonitor und muss immer aufgerufen, manipulationssicher und klein genug sein.

</li>

<li>

Befehle und Daten liegen im selben Speicher; ein Byte wird zum Befehl, wenn der Befehlszeiger darauf zeigt.

</li>

<li>

Die Privilegstufe ist ein Zustand des Prozessors (Ring 0 Kernel, Ring 3 Programme); privilegiert ist alles, womit man die Grenzen verstellen könnte; ein verbotener Befehl löst eine Schutzverletzung aus, Linux schickt SIGSEGV (Status 139).

</li>

<li>

In den Kernel führen Systemaufruf, Ausnahme und Unterbrechung, immer an Stellen, die der Kernel eingetragen hat; Zeiger aus Systemaufrufen prüft er und lehnt sonst mit `EFAULT` ab.

</li>

<li>

Die Zeitgeber-Unterbrechung holt den Kern zurück, rund 250-mal je Sekunde auf dem Testrechner; Zeitgeber und Sperren sind privilegiert.

</li>

<li>

Jeder Prozess hat eine eigene Seitentabelle; die MMU übersetzt und prüft jeden Zugriff, das Wurzelregister stellt nur der Kernel um; x86-64 zerlegt eine Adresse in $4\cdot9+12$ Bit.

</li>

<li>

Seitenrechte: U/S schützt den Kernel, NX und W^X trennen Code und Daten, SMEP und SMAP schützen den Kernel vor Programmspeicher; `/proc/self/maps` zeigt die Rechte.

</li>

<li>

Vor dem Kernel läuft die Startkette; Secure Boot startet nur, was über PK, KEK und Erlaubt-Liste zugelassen und nicht gesperrt ist, und braucht Widerruf für fehlerhafte Programme.

</li>

<li>

Measured Boot erweitert PCR mit $\mathrm{PCR}_\mathrm{neu}=H(\mathrm{PCR}_\mathrm{alt}\,\|\,m)$; das TPM versiegelt Geheimnisse an PCR-Werte und bescheinigt sie bei der Attestierung.

</li>

</ul>
:::

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Der Kernel kann schützen, weil die Hardware ihn schützt: Nur er darf auf Stufe 0 Einsprungtabellen, Zeitgeber und Seitentabellen einrichten, und Programme kommen nur durch seine Türen hinein.

</li>

<li>

Prozesse voneinander, den Kernel von den Programmen und Code von Daten trennt die MMU bei jedem Zugriff anhand der Seitenrechte, die nur der Kernel setzt.

</li>

<li>

Weil Code, der vor dem Kernel läuft, über all dem steht, sichert man die Startkette eigens: Secure Boot verhindert, Measured Boot mit dem TPM macht nachweisbar.

</li>

</ol>
:::

**Ein Prinzip hinter allen Ergebnissen.** Jede Grenze dieses Kapitels ist ein Referenzmonitor, und jedes Bauteil erfüllt eine seiner drei Forderungen für eine Schicht:

| Ergebnis | Forderung, die es erfüllt | Woher es kommt |
|---|---|---|
| Privilegierte Befehle nur auf Stufe 0 | manipulationssicher | Programme können Schutzeinstellungen nicht verstellen (Abschnitt [3](privilegstufen-und-schutzringe.html#stufe-3)) |
| Einsprung nur an eingetragenen Stellen | immer aufgerufen | kein Weg hinter die Prüfung des Kernels (Abschnitt [4](der-eintritt-in-den-kernel.html#stufe-4)) |
| Prüfung und Kopie der Argumente | immer aufgerufen | auch über Zeiger erreicht kein Programm den Kernelspeicher (Abschnitt [4](der-eintritt-in-den-kernel.html#stufe-4)) |
| Zeitgeber-Unterbrechung | immer aufgerufen | der Kernel kommt auf jeden Kern, auch ohne Mitwirkung (Abschnitt [5](die-zeitgeber-unterbrechung.html#stufe-5)) |
| Eigene Seitentabelle, MMU, Wurzelregister | immer aufgerufen, manipulationssicher | jeder Zugriff wird übersetzt, die Tabellen stellt nur der Kernel (Abschnitt [6](der-virtuelle-adressraum.html#stufe-6)) |
| U/S-Bit, SMEP, SMAP | manipulationssicher | Programme erreichen Code und Daten des Kernels nicht (Abschnitt [7](seitenrechte-kernel-code-und-daten-trennen.html#stufe-7)) |
| NX-Bit und W^X | immer aufgerufen | jedes Befehlsholen wird geprüft (Abschnitt [7](seitenrechte-kernel-code-und-daten-trennen.html#stufe-7)) |
| Secure Boot, Schlüsselrangfolge | manipulationssicher | niemand ersetzt den Kernel, bevor er läuft (Abschnitt [8](die-startkette-als-schutzgrenze.html#stufe-8)) |
| Widerruf | ergänzt die dritte, gegen Fehler | erkannte Fehler in der vertrauenswürdigen Basis lassen sich nachträglich ausschließen (Abschnitt [8](die-startkette-als-schutzgrenze.html#stufe-8)) |
| Erweitern statt Überschreiben | manipulationssicher | eine Messung lässt sich nicht zurücknehmen (Abschnitt [9](measured-boot-messen-statt-blockieren.html#stufe-9)) |
| Versiegeln, Attestierung | immer aufgerufen | das Geheimnis kommt nur nach der Prüfung heraus (Abschnitt [10](das-tpm-versiegeln-nachweisen-und-die-grenzen.html#stufe-10)) |

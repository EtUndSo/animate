---
title: Die Startkette als Schutzgrenze
pfad: Informatik / Cybersecurity / Schutzgrenzen in Hardware und Betriebssystem
adresse: informatik/cybersecurity/schutzgrenzen-in-hardware-und-betriebssystem
knoten: Kapitel 2: Schutzgrenzen in Hardware und Betriebssystem
order: 6120900
summary: Alle bisherigen Grenzen richtet der Kernel ein, wenn er startet.
tags: Bootkit, Vertrauensanker, Plattformschlüssel, Schlüsselaustausch-Schlüssel, Erlaubt-Liste, Sperrliste, Widerruf
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Alle bisherigen Grenzen richtet der Kernel ein, wenn er startet. Dieser Abschnitt fragt, was vor dem Kernel läuft, warum genau das eine eigene Schutzgrenze braucht und wie Secure Boot sie mit Schlüsseln und Sperrlisten zieht. Er zeigt auch, wo diese Grenze endet.
:::

:::::vorwissen Was du dafür brauchst: Firmware, Bootloader und Secure Boot

<span class="anker" id="stufe-8-1"></span>

Aus [Linux, Kapitel 1](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/ein-linux-zum-ueben.html) brauchst du die Startkette eines PCs.

<ul>

<li>

Die Firmware nach dem Standard UEFI steht in einem Speicherchip auf der Hauptplatine und läuft nach dem Einschalten als Erstes. Sie startet die Hardware und lädt ein Startprogramm aus der EFI-Systempartition ([Linux, Kapitel 1, Abschnitt 6.1](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/wie-ein-pc-startet.html#stufe-6-1)).

</li>

<li>

Der Bootloader ist das Startprogramm, das den Kernel in den Arbeitsspeicher lädt und startet; Linux benutzt meist GRUB ([Linux, Kapitel 1, Abschnitt 6.3](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/wie-ein-pc-startet.html#stufe-6-3)).

</li>

<li>

Eine digitale Signatur ist eine Art fälschungssicheres Siegel: Nur der Besitzer eines geheimen Schlüssels kann es anbringen, und jeder mit dem passenden Prüfschlüssel kann es kontrollieren. Wird die signierte Datei auch nur um ein Bit verändert, passt das Siegel nicht mehr ([Linux, Kapitel 1, Abschnitt 5.7](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/datentrager-abbild-und-prufsumme.html#stufe-5-7)).

</li>

<li>

Secure Boot ist eine Funktion der UEFI-Firmware, die ein Startprogramm nur ausführt, wenn es eine gültige Signatur trägt, deren Prüfschlüssel in der Firmware hinterlegt und nicht gesperrt ist. Bei Ubuntu prüft die Firmware das Programm `shim`, das Microsoft signiert hat und das den Prüfschlüssel von Canonical enthält; `shim` prüft GRUB, GRUB prüft den Kernel ([Linux, Kapitel 1, Abschnitt 6.4](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/wie-ein-pc-startet.html#stufe-6-4)).

</li>

</ul>

⁠**Kurz gesagt:** Die Firmware lädt den Bootloader, der Bootloader den Kernel, und mit Secure Boot prüft jedes Glied das Siegel des nächsten.

:::::

### Die Startkette als Schutzgrenze und das Bootkit

<span class="anker" id="stufe-8-2"></span>

Die Einsprungtabelle, der Zeitgeber, die Seitentabellen, das NX-Bit, SMEP und SMAP: Alles das stellt der Kernel ein, während er startet und noch niemand sonst läuft. Was vor ihm läuft, findet diese Grenzen noch gar nicht vor. Es kann sie anders einrichten oder den Kernel selbst verändern, bevor er die Kontrolle bekommt.

:::definition Definition 8.1 (Bootkit)
<span class="anker" id="satz-8-1"></span>

Ein __Bootkit__ ist Schadsoftware, die sich in der Startkette einnistet, also in der Firmware, im Bootloader oder in einem anderen Glied, das vor dem Kernel läuft. Weil sie vor dem Betriebssystem läuft und es lädt, kann sie alle seine Schutzgrenzen umgehen, und das Betriebssystem kann sie mit eigenen Mitteln nicht zuverlässig erkennen.
:::

Die Startkette ist damit selbst eine Schutzgrenze: zwischen dem Code, der vor dem Kernel läuft, und allem, was der Kernel schützt. Abbildung [32](#abb-32) zeigt, warum sie über allen anderen steht.

:::abbildung cyber/k2bootkit 32
Eine Zeitleiste des Starts: Firmware, Bootloader, Kernel, Programme. Beim Kernel erscheinen nacheinander die Grenzen als Schranken: „Einsprungtabelle“, „Zeitgeber“, „Seitentabellen“, „NX, SMEP, SMAP“. Dann wird der Bootloader rot: „verändert“. Ein Pfeil vom roten Bootloader greift in den Kernel, bevor die Schranken stehen, und ändert eine Zeile der Tabelle der Dienste. Die Programme rechts, darunter ein Virenscanner, sehen nur den fertigen Kernel und bemerken nichts.
:::

::::beispiel Was ein verändertes Startprogramm vermag
Ein Bootloader lädt den echten Kernel von Ubuntu, ändert aber vorher im Arbeitsspeicher einen Eintrag in dessen Tabelle der Dienste. Danach startet der Kernel wie immer, richtet alle Grenzen ein und prüft jeden Systemaufruf, nur dass einer davon auf Stufe 0 in Code des Angreifers führt. Ein Virenscanner läuft als Programm auf Stufe 3 und erfährt vom System nur, was der veränderte Kernel ihm mitteilt. Er hat keinen Standpunkt außerhalb, von dem aus er den Fehler sehen könnte.
::::

⁠**Kurz gesagt:** Was vor dem Kernel läuft, steht über allen seinen Grenzen; deshalb braucht die Startkette einen eigenen Schutz.

### Der Vertrauensanker

<span class="anker" id="stufe-8-3"></span>

Wenn jedes Glied der Kette das nächste prüft, wer prüft das erste? Irgendwo muss die Kette mit einem Teil beginnen, dem man ohne Prüfung vertraut.

:::definition Definition 8.2 (Vertrauensanker)
<span class="anker" id="satz-8-2"></span>

Ein __Vertrauensanker__ (englisch root of trust) ist ein Teil am Anfang einer Kette von Prüfungen, dem man vertrauen muss, ohne dass etwas vor ihm ihn prüft. Damit das vertretbar ist, muss er klein sein und sich nicht nachträglich verändern lassen, etwa weil er fest in einem Chip gespeichert ist.
:::

Bei Secure Boot sind die Firmware und die Schlüssel, die in ihr hinterlegt sind, der Vertrauensanker der Kette. Viele Rechner prüfen zusätzlich die Firmware selbst mit einem kleinen, unveränderlichen Stück Code, bevor sie sie starten; dann rückt der Anker noch eine Stufe nach vorn. Abbildung [33](#abb-33) zeigt die Kette mit ihrem Anker.

:::abbildung cyber/k2anker 33
Eine Kette aus vier Gliedern: „unveränderlicher Startcode“, „Firmware mit Schlüsseln“, „Bootloader“, „Kernel“. Von jedem Glied zeigt ein Pfeil „prüft“ auf das nächste. Am ersten Glied hängt ein Anker; ein Fragezeichen „wer prüft mich?“ erscheint und wird durch die Aufschrift „niemand: deshalb unveränderlich“ ersetzt. Ein Versuch, das erste Glied zu überschreiben, prallt ab.
:::

::::beispiel Der Anker beim Start vom Ubuntu-Stick
Die Firmware prüft `shim` mit einem Schlüssel von Microsoft, den sie gespeichert hat. Ob dieser Schlüssel echt ist, prüft niemand mehr; man vertraut darauf, dass der Hersteller ihn richtig eingetragen hat und dass kein Programm ihn ändern kann. Wer die Firmware oder ihre Schlüssel austauschen könnte, könnte jede Prüfung danach bestehen lassen. Deshalb nimmt eine gut gebaute Firmware Aktualisierungen ihrer selbst ebenfalls nur mit gültiger Signatur an.
::::

⁠**Kurz gesagt:** Jede Kette von Prüfungen beginnt mit einem Vertrauensanker, der unveränderlich sein muss, weil ihn niemand mehr prüft.

### Die Schlüssel von Secure Boot

<span class="anker" id="stufe-8-4"></span>

[Linux, Kapitel 1](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/ein-linux-zum-ueben.html) sprach von Prüfschlüsseln, die in der Firmware hinterlegt sind. Genauer verwaltet die Firmware vier Arten von Einträgen, die aufeinander aufbauen.

:::definition Definition 8.3 (PK, KEK, db, dbx)
<span class="anker" id="satz-8-3"></span>

Die Firmware speichert für Secure Boot in einem nichtflüchtigen Speicher:

<ul>

<li>

den __Plattformschlüssel__ (PK, platform key), den obersten Schlüssel, meist vom Hersteller des Rechners. Mit ihm signierte Änderungen dürfen die KEK-Liste ändern oder Secure Boot abschalten;

</li>

<li>

die __Schlüsselaustausch-Schlüssel__ (KEK, key exchange keys), eine Liste von Schlüsseln, mit deren Signatur die beiden folgenden Listen geändert werden dürfen;

</li>

<li>

die __Erlaubt-Liste__ (db, signature database) mit zugelassenen Unterzeichnern und Prüfsummen von Startprogrammen und Treibern;

</li>

<li>

die __Sperrliste__ (dbx, forbidden signature database) mit widerrufenen Unterzeichnern und Prüfsummen.

</li>

</ul>

Die Firmware startet ein Startprogramm nur, wenn seine Signatur oder seine Prüfsumme zur Erlaubt-Liste passt und es nicht in der Sperrliste steht. Steht etwas in beiden Listen, gilt die Sperrliste.
:::

Geprüft werden nicht nur Bootloader, sondern auch Treiber, die auf Erweiterungskarten mitgeliefert werden, und andere Programme, die die Firmware vor dem Betriebssystem startet. Abbildung [34](#abb-34) zeigt die Rangfolge.

:::abbildung cyber/k2schluessel 34
Eine Pyramide mit drei Ebenen. Oben „PK (Hersteller)“, darunter „KEK (z. B. Microsoft, Hersteller)“, darunter zwei Kästen nebeneinander „db: erlaubt“ (grün) und „dbx: gesperrt“ (rot). Pfeile „darf ändern“ führen von PK zu KEK und von KEK zu db und dbx. Ganz unten kommt ein Startprogramm an: Die Prüfung fragt zuerst „in dbx?“ (nein), dann „passt zu db?“ (ja), dann öffnet sich die Schranke.
:::

::::beispiel Die Einträge eines gewöhnlichen Windows-PCs
Auf einem typischen PC stammt der PK vom Hersteller. In der KEK-Liste steht ein Schlüssel von Microsoft, oft auch einer des Herstellers. Die Erlaubt-Liste enthält das Zertifikat, mit dem Microsoft den eigenen Bootmanager von Windows signiert, und meist auch das Zertifikat, mit dem Microsoft Startprogramme anderer Hersteller wie `shim` signiert. Startet man einen Ubuntu-Stick, findet die Firmware die Signatur von `shim` in der Erlaubt-Liste, prüft, dass weder dieser Unterzeichner noch die Prüfsumme von `shim` in der Sperrliste stehen, und startet es.
::::

⁠**Kurz gesagt:** Der PK erlaubt Änderungen an den KEK, die KEK erlauben Änderungen an Erlaubt- und Sperrliste, und gestartet wird nur, was erlaubt und nicht gesperrt ist.

### Wer die Schlüssel ändern darf

<span class="anker" id="stufe-8-5"></span>

Die Listen nützen nur, wenn Schadsoftware sie nicht einfach ergänzen kann, etwa um ein eigenes Startprogramm zuzulassen.

:::satz Satz 8.4 (Änderungen an Secure Boot)
<span class="anker" id="satz-8-4"></span>

Eine Änderung an der KEK-Liste braucht die Signatur des PK, eine Änderung an Erlaubt- oder Sperrliste die Signatur eines KEK. Ohne passende Signatur kann nur ein Mensch, der am Rechner sitzt, in den Menüs der Firmware etwas ändern. Ein Programm ohne solche Signatur, auch eines mit allen Rechten des Betriebssystems, kann die Einstellungen von Secure Boot deshalb nicht ändern. Das gilt im gewöhnlichen Zustand mit gesetztem PK und solange die Firmware selbst keinen Fehler hat.
:::

Das ist die zweite Forderung an einen Referenzmonitor, angewandt auf die Startkette: Die Prüfung lässt sich vom laufenden System aus nicht verändern. Abbildung [35](#abb-35) zeigt drei Versuche, die Listen zu ändern.

:::abbildung cyber/k2aendern 35
Rechts die Firmware mit den Listen PK, KEK, db und dbx hinter einem Schloss. Von links kommen nacheinander drei Änderungen. Erstens ein neuer Eintrag für die Sperrliste aus Windows Update mit dem Siegel „signiert mit KEK von Microsoft“: Die Firmware prüft das Siegel, Häkchen, der Eintrag landet in dbx. Zweitens ein Schadprogramm „mit Verwalterrechten“, das sich ohne Siegel in die Erlaubt-Liste eintragen will: Kreuz, prallt ab. Drittens ein Mensch an der Tastatur im Menü der Firmware: Er darf von Hand ändern (Häkchen, Aufschrift „nur am Rechner“).
:::

::::beispiel Eine neue Sperrliste über Windows Update
Microsoft verteilt neue Einträge für die Sperrliste über Windows Update. Windows reicht sie an die Firmware weiter, aber die Firmware übernimmt sie nur, weil sie mit dem Schlüssel von Microsoft aus der KEK-Liste signiert sind. Ein Schadprogramm, das sich auf demselben Weg selbst in die Erlaubt-Liste eintragen wollte, scheitert an der fehlenden Signatur, auch wenn es mit den Rechten des Verwalters läuft.
::::

⁠**Kurz gesagt:** Secure Boot ändert man nur mit der Signatur des darüberliegenden Schlüssels oder von Hand in der Firmware, nie per Software allein.

:::hintergrund Eigene Schlüssel für Linux: die MOK-Liste
Wer selbst übersetzte Kernelmodule benutzt, etwa für VirtualBox, hat keine Signatur von Microsoft oder Canonical dafür. `shim` führt deshalb eine eigene Liste zusätzlicher Prüfschlüssel des Rechnerbesitzers, die Machine Owner Keys (MOK). Ein neuer Schlüssel wird vom laufenden Linux nur vorgemerkt; aufgenommen wird er erst beim nächsten Start, wenn ein Mensch am Rechner ihn in einem Menü von `shim` mit einem vorher gewählten Passwort bestätigt. Auch hier gilt: Software allein ändert die Liste nicht.
:::

### Der Widerruf und seine Grenzen

<span class="anker" id="stufe-8-6"></span>

Eine Signatur beweist, wer ein Startprogramm freigegeben hat. Sie beweist nicht, dass das Programm fehlerfrei ist. Findet man in einem gültig signierten Bootloader eine Lücke, durch die man Secure Boot umgehen kann, bleibt dieser Bootloader trotzdem gültig signiert, auch wenn der Hersteller längst eine korrigierte Fassung herausgegeben hat. Ein Angreifer bringt dann einfach die alte Fassung mit.

:::definition Definition 8.5 (Widerruf)
<span class="anker" id="satz-8-5"></span>

Ein __Widerruf__ ist das Eintragen eines Unterzeichners oder der Prüfsumme eines Startprogramms in die Sperrliste, damit die Firmware es nicht mehr startet, obwohl seine Signatur gültig ist.
:::

Der Widerruf über die Sperrliste hat eine praktische Grenze: Der Speicher der Firmware dafür ist klein, typisch 32 kB. Nach einer Lücke in GRUB im Jahr 2020, die unter dem Namen BootHole bekannt wurde, mussten drei Zertifikate und 150 Prüfsummen einzelner Startprogramme gesperrt werden. Das belegte rund 10 kB, also fast ein Drittel des Platzes. Für Linux führte das Projekt `shim` deshalb einen zweiten Weg ein, SBAT: Jedes Startprogramm, das `shim` prüft, etwa GRUB, trägt eine Generationsnummer, die bei jeder Korrektur einer Sicherheitslücke steigt und nie sinkt. Gesperrt wird dann nicht jede alte Fassung einzeln, sondern „alles unter Generation $N$“, und dafür genügt ein einziger kurzer Eintrag. Diese Prüfung macht nicht die Firmware, sondern `shim` selbst, bevor es das nächste Glied startet; die verlangten Mindestgenerationen bringt `shim` mit und legt sie in einem eigenen kleinen Eintrag der Firmware ab, nicht in der Sperrliste. Abbildung [36](#abb-36) zeigt beide Wege.

:::abbildung cyber/k2widerruf 36
Links die Sperrliste als Kasten mit Füllstandsanzeige „32 kB“. Nacheinander fallen Einträge hinein: drei Zertifikate und 150 Prüfsummen; der Füllstand steigt auf knapp ein Drittel. Rechts daneben drei Fassungen eines Bootloaders mit „Generation 1“, „Generation 2“, „Generation 3“; ein einzelner kurzer Eintrag „GRUB: mindestens Generation 3“, den `shim` prüft und der nicht in der Sperrliste steht, sperrt die beiden alten auf einmal.
:::

::::beispiel Wie viel Platz ein Widerruf kostet
Belegen die Einträge nach BootHole 10 kB von 32 kB, sind das $10/32\approx0{,}31$, also rund 31 % des Speichers für einen einzigen Vorfall. Nach zwei weiteren Vorfällen dieser Größe wären 30 kB belegt, und für einen dritten wäre kein Platz mehr. Mit Generationsnummern kostet jeder weitere Vorfall nur das Erhöhen einer Zahl.
::::

⁠**Kurz gesagt:** Secure Boot prüft, wer unterschrieben hat, nicht, ob das Unterschriebene fehlerfrei ist; fehlerhafte Startprogramme muss man widerrufen, und dafür ist wenig Platz.

:::hintergrund Ein Fall aus der Praxis: BlackLotus
2023 beschrieb die Sicherheitsfirma ESET das erste öffentlich bekannte Bootkit, das Secure Boot auf einem vollständig aktualisierten Windows 11 umging. Es nutzte eine Lücke in älteren, gültig signierten Bootmanagern von Windows (CVE-2022-21894). Microsoft hatte die Lücke im Januar 2022 behoben, aber die alten Fassungen standen nicht in der Sperrliste. Das Bootkit brachte deshalb eine alte, gültig signierte Fassung mit, und die Firmware startete sie, während Secure Boot eingeschaltet blieb.

Microsofts Antwort (CVE-2023-24932) zeigt die Grenzen des Widerrufs: Einzelne Prüfsummen hätten nicht gereicht, also soll das ganze Zertifikat in die Sperrliste, mit dem die alten Bootmanager signiert sind, dazu eine Versionsnummer gegen das Zurückgehen auf alte Fassungen. Vorher muss jeder Rechner das Nachfolgezertifikat von 2023 und einen neu signierten Bootmanager haben, und alte Start- und Wiederherstellungsmedien starten auf ihm danach nicht mehr. Die Schritte lassen sich nicht rückgängig machen, solange Secure Boot eingeschaltet ist. Microsoft bietet die Schritte seit Juli 2024 an, schaltet sie aber nicht von selbst ein; einen Termin für die verpflichtende Umstellung hatte Microsoft bis Mitte November 2026 noch nicht genannt.
:::

:::hintergrund Zertifikate mit Ablaufdatum
[Linux, Kapitel 1, Abschnitt 6.4](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/wie-ein-pc-startet.html#stufe-6-4) hat erwähnt, dass das Zertifikat, mit dem Microsoft Startprogramme anderer Hersteller signiert, am 27. Juni 2026 abgelaufen ist. Im selben Jahr liefen auch der KEK-Schlüssel von Microsoft aus dem Jahr 2011 (24. Juni) und das Zertifikat für den Bootmanager von Windows (19. Oktober) ab; ihre Nachfolger stammen von 2023. Laut Microsoft starten Rechner ohne die neuen Zertifikate weiter, erhalten aber keine neuen Schutzmaßnahmen für die frühe Startphase mehr, also auch keine neuen Einträge für die Sperrliste. Auch ein Vertrauensanker muss gepflegt werden.
:::

### Aufgaben zu Abschnitt [8](#stufe-8)

<span class="anker" id="stufe-8-7"></span>

:::aufgabe Aufgabe 22 ★ Wer muss unterschreiben?
<span class="anker" id="aufg-22"></span>

Welche Signatur braucht jede Änderung, oder geht sie gar nicht per Software? (a) Ein neues Zertifikat in die Erlaubt-Liste aufnehmen. (b) Die Prüfsumme eines alten Bootloaders in die Sperrliste eintragen. (c) Einen weiteren KEK hinzufügen. (d) Ein Programm mit Verwalterrechten will Secure Boot abschalten. (e) Ein Besitzer will Secure Boot abschalten.

:::loesung
(a) Die Signatur eines Schlüssels aus der KEK-Liste. (b) Ebenfalls die Signatur eines KEK, denn auch die Sperrliste ändert man nur damit. (c) Die Signatur des PK. (d) Gar nicht: Software kann die Einstellungen von Secure Boot nicht ändern, auch nicht mit Verwalterrechten, außer mit einer passenden Signatur des PK. (e) Der Besitzer, der am Rechner sitzt, kann Secure Boot in den Menüs der Firmware von Hand abschalten; das ist der vorgesehene Weg ohne Signatur.
:::
:::

:::aufgabe Aufgabe 23 ★★ Secure Boot am eigenen Rechner nachsehen
<span class="anker" id="aufg-23"></span>

Windows legt beim Start ab, ob Secure Boot eingeschaltet ist. Lesen kannst du das ohne Verwalterrechte in der PowerShell, ohne etwas zu verändern:

```console Windows (PowerShell)
PS> $env:firmware_type
UEFI
PS> (Get-ItemProperty HKLM:\SYSTEM\CurrentControlSet\Control\SecureBoot\State).UEFISecureBootEnabled
0
```

Der Wert 1 bedeutet eingeschaltet, 0 ausgeschaltet. Dieselbe Angabe zeigt das Programm „Systeminformationen“ (`msinfo32`) in der Zeile „Sicherer Startzustand“. Auf dem Testrechner dieses Kapitels ist Secure Boot aus; das ist ein Befund an diesem einen Rechner, keine Empfehlung. Auf den meisten neueren PCs ist Secure Boot ab Werk eingeschaltet, und dort sollte es auch bleiben, denn es zieht die Grenze, die dieser Abschnitt beschreibt. Findest du es bei dir ausgeschaltet, ändere das nicht im Rahmen dieser Übung: Wer es einschalten will, informiert sich vorher beim Hersteller des Rechners und sichert den Wiederherstellungsschlüssel von BitLocker ([Linux, Kapitel 1, Abschnitt 6.5](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/wie-ein-pc-startet.html#stufe-6-5)). (a) Wie steht es bei deinem Rechner? (b) Welche Grenze aus diesem Abschnitt fehlt einem Rechner, bei dem Secure Boot aus ist, und welche Angriffe aus Unterabschnitt [8.2](#stufe-8-2) werden dadurch leichter? (c) Unter WSL 2 meldet `ls /sys/firmware/efi` „No such file or directory“. Warum sieht das Linux in WSL die Startkette des Rechners nicht?

:::loesung
(a) Das hängt vom Rechner ab; 1 bedeutet eingeschaltet. Auf dem Testrechner dieses Kapitels steht 0. Steht bei dir ebenfalls 0, ist das ein Befund, kein Grund für einen schnellen Eingriff: Einschalten sollte man Secure Boot erst nach den Angaben des Herstellers und mit gesichertem Wiederherstellungsschlüssel, nicht im Rahmen dieser Übung.

(b) Ohne Secure Boot fehlt die Prüfung, ob die Glieder der Startkette signiert und nicht gesperrt sind. Ein verändertes Startprogramm, wie das Bootkit aus dem Beispiel „Was ein verändertes Startprogramm vermag“, startet dann ohne jede Meldung. Ein Angreifer muss also keine Lücke in der Prüfung finden, sondern nur das Startprogramm austauschen können.

(c) Der Kernel von WSL 2 wird von Windows in einer kleinen virtuellen Maschine gestartet ([Linux, Kapitel 1, Abschnitt 4.1](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/wsl-2-linux-neben-windows.html#stufe-4-1)), nicht von der Firmware des Rechners. In dieser VM gibt es keine UEFI-Firmware und deshalb auch kein `/sys/firmware/efi`. Das Linux in WSL sieht die Startkette des Rechners also gar nicht; ob Secure Boot an ist, kann man nur unter Windows oder in einem direkt gestarteten Linux nachsehen.
:::
:::

:::aufgabe Aufgabe 24 ★★ Warum ein ganzes Zertifikat?
<span class="anker" id="aufg-24"></span>

Lies den Hintergrund „Ein Fall aus der Praxis: BlackLotus“. (a) Welche Forderung an einen Referenzmonitor war bei BlackLotus verletzt, obwohl Secure Boot eingeschaltet war? (b) Warum sperrt Microsoft das ganze Zertifikat statt der Prüfsummen der alten Bootmanager? (c) Warum müssen vorher alle Rechner das neue Zertifikat in ihrer Erlaubt-Liste haben?

:::loesung
(a) Verletzt war die dritte Forderung. Die Prüfung der Firmware lief: Die Signatur der alten Bootmanager war gültig. Aber die Bootmanager gehören selbst zur prüfenden Kette und damit zur vertrauenswürdigen Basis, und sie hatten einen Fehler. Sie waren also nicht so einfach, dass man ihre Korrektheit vollständig hätte prüfen können; das ist der Weg „Fehler“ aus dem Hintergrund zu den drei Forderungen. Über den Fehler ließ sich die Richtlinie von Secure Boot aus dem Speicher entfernen. In der Folge fiel auch die zweite Forderung, denn der Angreifer hat die Prüfung der späteren Glieder damit verändert.

(b) Über die Jahre sind sehr viele Fassungen des Bootmanagers mit diesem Zertifikat signiert worden. Jede einzeln über ihre Prüfsumme zu sperren, würde den kleinen Speicher der Sperrliste schnell füllen, und jede vergessene Fassung bliebe ein Weg hinein. Ein einziger Eintrag für das Zertifikat sperrt alle auf einmal.

(c) Auch der aktuelle, korrigierte Bootmanager war mit dem Zertifikat von 2011 signiert. Stünde das Zertifikat in der Sperrliste, bevor ein neu signierter Bootmanager und das neue Zertifikat in der Erlaubt-Liste da sind, würde der Rechner Windows nicht mehr starten. Deshalb kommen zuerst das Zertifikat von 2023 und der neue Bootmanager, dann die Sperre.
:::
:::

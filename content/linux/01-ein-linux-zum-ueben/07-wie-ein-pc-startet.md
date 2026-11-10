---
title: Wie ein PC startet
pfad: Informatik / Linux und Kommandozeile / Ein Linux zum Üben: WSL, virtuelle Maschine, Live-USB-Stick
adresse: informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick
knoten: Kapitel 1: Ein Linux zum Üben: WSL, virtuelle Maschine, Live-USB-Stick
order: 6060700
summary: Wer Linux von einem USB-Stick oder in einer virtuellen Maschine von einem Abbild starten will, muss wissen, was zwischen dem Druck auf den Einschaltknopf und dem laufenden Kernel geschieht.
tags: Firmware, UEFI, EFI-Systempartition, Bootreihenfolge, Bootmenü, Bootloader, GRUB, Secure Boot
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Wer Linux von einem USB-Stick oder in einer virtuellen Maschine von einem Abbild starten will, muss wissen, was zwischen dem Druck auf den Einschaltknopf und dem laufenden Kernel geschieht. Dieser Abschnitt verfolgt diese Kette Glied für Glied, so weit, wie man sie für einen sicheren Start vom Stick braucht: Wer startet zuerst, wie wählt man den Datenträger, wer lädt den Kernel, wie prüft der Rechner, ob er dem Startprogramm trauen kann, und warum hängt die Verschlüsselung von Windows an dieser Kette?
:::

### Die Firmware

<span class="anker" id="stufe-6-1"></span>

Nach dem Einschalten ist der Arbeitsspeicher leer, und noch kein Betriebssystem läuft. Trotzdem findet der Rechner nach wenigen Sekunden Windows auf der SSD. Irgendein Programm muss also schon vorher da sein und wissen, wo es suchen soll.

:::definition Definition 6.1 (Firmware, UEFI)
<span class="anker" id="satz-6-1"></span>

Die __Firmware__ ist ein Programm, das fest in einem Speicherchip auf der Hauptplatine (dem Mainboard) steht und beim Einschalten als Erstes läuft. Sie prüft und startet die Hardware und lädt dann ein Startprogramm von einem Datenträger. Heutige PCs benutzen eine Firmware nach dem Standard __UEFI__ (Unified Extensible Firmware Interface); ihr Vorgänger hieß BIOS, und viele Menschen sagen bis heute „BIOS“ zur Firmware.
:::

Eine UEFI-Firmware liest ihre Startprogramme aus einer eigenen, kleinen Partition mit einem FAT-Dateisystem, der __EFI-Systempartition__; es ist die erste der vier Partitionen aus dem Beispiel in Unterabschnitt [5.2](datentrager-abbild-und-prufsumme.html#stufe-5-2). In ihrem eigenen Speicher führt die Firmware eine Liste von Starteinträgen, jeder mit dem Datenträger und dem Pfad einer Startdatei. Für Windows zeigt ein Eintrag namens „Windows Boot Manager“ auf die Datei `\EFI\Microsoft\Boot\bootmgfw.efi` in der EFI-Systempartition der SSD.

::::beispiel Welche Firmware hat mein Rechner?
Die PowerShell kennt eine Angabe, die Windows beim Start von der Firmware übernimmt:

```console Windows (PowerShell)
PS> $env:firmware_type
UEFI
```

Auf älteren Rechnern steht hier `Legacy`; dann startet der Rechner in der alten BIOS-Betriebsart. Rechner mit Windows 11 starten praktisch immer mit UEFI.
::::

⁠**Kurz gesagt:** Die Firmware läuft nach dem Einschalten als Erstes und lädt ein Startprogramm aus der EFI-Systempartition.

:::hintergrund Warum ein fremder USB-Stick ohne Eintrag startet
Ein USB-Stick, der zum ersten Mal in einem Rechner steckt, hat in dessen Firmware noch keinen Starteintrag. Damit trotzdem jeder Stick auf jedem Rechner starten kann, legt der UEFI-Standard für Wechseldatenträger einen festen Pfad fest: Findet die Firmware auf einem solchen Datenträger eine EFI-Systempartition, sucht sie dort die Datei `\EFI\BOOT\BOOTX64.EFI` (für 64-Bit-PCs) und startet sie. Ein startfähiger Linux-Stick enthält genau diese Datei. Deshalb muss man für den Start vom Stick nichts in der Firmware einrichten, sondern ihn nur auswählen.
:::

### Bootreihenfolge und Bootmenü

<span class="anker" id="stufe-6-2"></span>

Stecken eine SSD mit Windows und ein USB-Stick mit Linux im Rechner, muss die Firmware entscheiden, wovon sie startet. Normalerweise soll das Windows sein, nur ausnahmsweise der Stick. Für „starten“ sagt man in diesem Zusammenhang oft *booten*.

:::definition Definition 6.2 (Bootreihenfolge, Bootmenü)
<span class="anker" id="satz-6-2"></span>

Die __Bootreihenfolge__ ist die Liste der Starteinträge in der Reihenfolge, in der die Firmware sie beim Einschalten ausprobiert. Das __Bootmenü__ ist eine Auswahl, die die Firmware auf einen Tastendruck beim Einschalten anzeigt; darin wählt man einmalig einen Eintrag, ohne die Bootreihenfolge zu ändern.
:::

::::beispiel Die Taste für das Bootmenü
Welche Taste das Bootmenü öffnet, hängt vom Hersteller ab; Tabelle [3](#tab-3) nennt die häufigsten. Man drückt sie gleich nach dem Einschalten mehrmals, bevor das Windows-Logo erscheint.

<span class="anker" id="tab-3"></span>

**Tabelle 3:** Tasten für das Bootmenü bei verbreiteten Herstellern. Einzelne Modelle können abweichen; maßgeblich ist die Anleitung des Geräts.

| Hersteller | Taste für das Bootmenü |
|---|---|
| Dell | F12 |
| HP | Esc, dann F9 |
| Lenovo | F12, bei vielen IdeaPads Fn+F12, oder die kleine Novo-Taste |
| ASUS (Notebook) | Esc gedrückt halten und dabei einschalten |
| MSI | F11 |
| Acer | F12, muss bei manchen Geräten erst in der Firmware freigeschaltet werden |

Hilft keine Taste, gibt es einen Weg über Windows: Einstellungen $\to$ System $\to$ Wiederherstellung $\to$ Erweiterter Start $\to$ „Jetzt neu starten“. Im blauen Menü, das danach erscheint, bieten viele Rechner den Punkt „Ein Gerät verwenden“, über den man direkt vom Stick startet. Andernfalls führt „Problembehandlung“ $\to$ „Erweiterte Optionen“ $\to$ „UEFI-Firmwareeinstellungen“ in die Einstellungen der Firmware.
::::

⁠**Kurz gesagt:** Für einen einmaligen Start vom Stick benutzt man das Bootmenü und lässt die Bootreihenfolge, wie sie ist.

### Der Bootloader

<span class="anker" id="stufe-6-3"></span>

Die Firmware kennt sich mit Partitionen und dem FAT-Dateisystem aus, aber nicht mit einem Linux-Kernel und dessen Einstellungen. Zwischen ihr und dem Kernel steht deshalb ein weiteres Programm.

:::definition Definition 6.3 (Bootloader)
<span class="anker" id="satz-6-3"></span>

Ein __Bootloader__ ist das Startprogramm, das die Firmware lädt und das seinerseits den Kernel des Betriebssystems in den Arbeitsspeicher lädt und startet. Er kann dabei ein Menü anzeigen, in dem man zwischen mehreren Systemen oder Startvarianten wählt.
:::

Linux-Distributionen benutzen meist den Bootloader __GRUB__.

::::beispiel [Beispiele] Zwei Bootloader
Windows benutzt den Windows Boot Manager, die Datei aus Unterabschnitt [6.1](#stufe-6-1), Ubuntu den Bootloader GRUB. Startet man einen Ubuntu-Stick, zeigt GRUB nach wenigen Sekunden ein kurzes Menü; der erste Eintrag startet Ubuntu und ist voreingestellt. Ist der Kernel geladen, übernimmt er die Kontrolle, und der Bootloader hat seine Arbeit getan.
::::

⁠**Kurz gesagt:** Die Firmware lädt den Bootloader, der Bootloader lädt den Kernel.

### Secure Boot

<span class="anker" id="stufe-6-4"></span>

Das Startprogramm läuft, bevor das Betriebssystem und jeder Virenscanner überhaupt da sind, und es bestimmt, welcher Kernel geladen wird. Ein heimlich ausgetauschter Bootloader hätte also den ganzen Rechner in der Hand. Davor schützt eine Prüfung in der Firmware.

**Ein Siegel auf dem Startprogramm.** Die Prüfung beruht auf der digitalen Signatur aus Unterabschnitt [5.7](datentrager-abbild-und-prufsumme.html#stufe-5-7), dem fälschungssicheren Siegel, das nur der Besitzer eines geheimen Schlüssels anbringen und jeder mit dem passenden Prüfschlüssel kontrollieren kann. Wird eine signierte Datei danach auch nur um ein Bit verändert, passt das Siegel nicht mehr.

:::definition Definition 6.4 (Secure Boot)
<span class="anker" id="satz-6-4"></span>

__Secure Boot__ ist eine Funktion der UEFI-Firmware, die ein Startprogramm nur dann ausführt, wenn es eine gültige digitale Signatur trägt, deren Prüfschlüssel in der Firmware als vertrauenswürdig hinterlegt und nicht gesperrt ist. Secure Boot ist eine Echtheitsprüfung, keine Verschlüsselung: Es verbirgt nichts, es verhindert nur den Start veränderter oder fremder Startprogramme.
:::

Abbildung [10](#abb-10) zeigt, wie ein Ubuntu-Stick mit eingeschaltetem Secure Boot startet. Ab Werk sind in fast allen PCs Prüfschlüssel von Microsoft hinterlegt. Ubuntu bringt deshalb als erstes Startprogramm ein kleines Programm namens `shim` mit, das Microsoft signiert hat. In `shim` steckt der Prüfschlüssel von Canonical, mit dem `shim` den Bootloader GRUB prüft, und GRUB prüft auf dieselbe Weise den Kernel.

:::abbildung linux/k1bootkette 10
Die Bootkette eines Ubuntu-Sticks mit Secure Boot. Jedes Glied prüft das Siegel des nächsten, bevor es ihm die Kontrolle übergibt. Die Firmware vertraut Microsoft, Microsoft hat `shim` signiert, und `shim` trägt den Schlüssel von Canonical weiter.
:::

::::beispiel Wer mit Secure Boot startet und wer nicht
Ein Ubuntu-Stick startet mit eingeschaltetem Secure Boot, weil jedes Glied seiner Kette passend signiert ist; man muss in der Firmware nichts ändern. Kali Linux dagegen bringt einen Kernel ohne Signatur mit; um es vom Stick zu starten, müsste man Secure Boot in der Firmware ausschalten. Für dieses Kapitel bleibt Secure Boot immer eingeschaltet.
::::

⁠**Kurz gesagt:** Secure Boot startet nur Startprogramme mit gültigem Siegel; es prüft Echtheit und verschlüsselt nichts.

:::hintergrund Wenn ein Stick mit „Security Violation“ nicht startet
Die Prüfschlüssel in der Firmware stecken in Zertifikaten mit Ablaufdatum. Das Zertifikat, mit dem Microsoft seit 2011 die Startprogramme anderer Hersteller wie `shim` signiert, ist am 27. Juni 2026 abgelaufen; sein Nachfolger stammt von 2023. Der Ablauf allein verhindert keinen Start, denn die Firmware prüft das Siegel gegen das hinterlegte Zertifikat und nicht gegen das Datum. Probleme entstehen an zwei Stellen. Ein sehr neuer Rechner, dessen Firmware nur noch das Zertifikat von 2023 kennt, startet ein Startprogramm nicht, das nur nach dem alten signiert ist. Umgekehrt startet ein älterer Rechner, dessen Firmware nie aktualisiert wurde, kein Startprogramm, das nur nach dem neuen signiert ist. Laut Canonical brauchen die Installationsmedien von Ubuntu 26.04 das Zertifikat von 2011 in der Firmware. Meldet ein Rechner beim Start vom Stick eine Sicherheitsverletzung, spielt man zuerst alle Aktualisierungen von Windows und des Herstellers für die Firmware ein und versucht es erneut, statt Secure Boot auszuschalten.
:::

### Die Geräteverschlüsselung von Windows

<span class="anker" id="stufe-6-5"></span>

Auf vielen Windows-Rechnern ist die SSD verschlüsselt, oft ohne dass die Besitzer es wissen. Für den normalen Betrieb merkt man davon nichts. Ändert man aber etwas an der Startkette, kann Windows beim nächsten Start einen langen Schlüssel verlangen, und wer ihn nicht hat, kommt nicht mehr an seine Daten.

:::definition Definition 6.5 (BitLocker, Wiederherstellungsschlüssel)
<span class="anker" id="satz-6-5"></span>

__BitLocker__ ist die Laufwerksverschlüsselung von Windows; in Windows Home heißt sie *Geräteverschlüsselung*. Sie verschlüsselt Laufwerk C:, und Windows entschlüsselt es beim Start selbst, wenn die Startkette unverändert ist. Ist sie verändert, verlangt Windows den __Wiederherstellungsschlüssel__, eine Zahl mit 48 Ziffern, die beim Einschalten der Verschlüsselung erzeugt wurde.
:::

Windows 11 schaltet die Geräteverschlüsselung auf geeigneten Rechnern von selbst ein, sobald man sich mit einem Microsoft-Konto anmeldet, und legt den Wiederherstellungsschlüssel in diesem Konto ab. Seit der Version 24H2 trifft das auf deutlich mehr Rechner zu als früher. Ob dein Laufwerk verschlüsselt ist, siehst du unter Einstellungen $\to$ Datenschutz und Sicherheit $\to$ Geräteverschlüsselung; fehlt dieser Punkt, ist die Funktion auf deinem Rechner nicht verfügbar. In den Ausgaben Pro und Enterprise findet man die Verschlüsselung außerdem unter dem Namen „BitLocker-Laufwerkverschlüsselung“ in der Systemsteuerung.

::::beispiel Was die Abfrage auslöst und was nicht
Microsoft nennt unter anderem diese Auslöser für die Abfrage des Wiederherstellungsschlüssels: Änderungen am Windows Boot Manager, ein Update der Firmware, Änderungen an Einstellungen, die in die Prüfung der Startkette eingehen, wozu Secure Boot gehört, und auf älteren Rechnern mit einem Sicherheitschip der Version 1.2 eine geänderte Bootreihenfolge. Der einmalige Start vom Stick über das Bootmenü, bei eingeschaltetem Secure Boot und ohne Änderung an der Firmware, steht nicht auf dieser Liste; danach startet Windows normalerweise wie immer. Den Schlüssel sichert man trotzdem vorher, denn Rechner verhalten sich nicht alle gleich.
::::

:::warnung Den Wiederherstellungsschlüssel sichern, bevor du etwas an der Startkette tust
Bevor du vom Stick startest oder irgendeine Einstellung in der Firmware änderst, prüfe, ob dein Laufwerk verschlüsselt ist. Wenn ja, sichere den Wiederherstellungsschlüssel so, dass du ihn ohne diesen Rechner lesen kannst:

<ul>

<li>

Melde dich auf einem anderen Gerät, etwa dem Handy, unter [https://aka.ms/myrecoverykey](https://aka.ms/myrecoverykey) mit deinem Microsoft-Konto an und prüfe, dass dort ein Schlüssel für deinen Rechner steht. Notiere ihn auf Papier oder drucke ihn aus.

</li>

<li>

Ist der Rechner ein Gerät deiner Hochschule oder deines Arbeitgebers, liegt der Schlüssel bei dessen IT-Abteilung. Starte ein solches Gerät nicht ohne deren Erlaubnis von einem Stick.

</li>

</ul>

Musst du eine Einstellung in der Firmware ändern, rät Microsoft, die Verschlüsselung vorher vorübergehend anzuhalten; nach dem nächsten Neustart schaltet sie sich von selbst wieder ein. In den Ausgaben Pro und Enterprise geht das in der Systemsteuerung unter „BitLocker-Laufwerkverschlüsselung“ mit „Schutz anhalten“. Windows Home hat dafür keinen Schalter; dort ist der gesicherte Schlüssel die Absicherung.
:::

⁠**Kurz gesagt:** Wer an der Startkette etwas tut, sichert vorher den 48-stelligen Wiederherstellungsschlüssel.

:::hintergrund Warum die Verschlüsselung an der Startkette hängt
Den Schlüssel, mit dem Windows das Laufwerk entschlüsselt, gibt nur ein Sicherheitschip auf der Hauptplatine frei, das TPM (Trusted Platform Module). Während des Starts schreibt die Firmware eine Art Fingerabdruck jedes geladenen Startprogramms und wichtiger Einstellungen, etwa ob Secure Boot eingeschaltet ist, in diesen Chip. Er gibt den Schlüssel nur heraus, wenn diese Fingerabdrücke genau dieselben sind wie beim Einschalten der Verschlüsselung. So kann jemand, der den Rechner mit einem eigenen Startprogramm hochfährt, den Schlüssel nicht abgreifen; die Kehrseite ist, dass auch eine harmlose Änderung den Schlüssel sperrt. Wie das TPM die Startkette misst, erklärt die Reihe Cybersecurity.
:::

### Aufgaben zu Abschnitt [6](#stufe-6)

<span class="anker" id="stufe-6-6"></span>

:::aufgabe Aufgabe 19 ★ Firmware und Verschlüsselung deines Rechners
<span class="anker" id="aufg-19"></span>

Stelle fest, ohne etwas zu verändern: (a) Startet dein Rechner mit UEFI? Benutze `$env:firmware_type` in der PowerShell. (b) Ist Secure Boot eingeschaltet? Das Programm „Systeminformationen“ (im Startmenü `msinfo32` eintippen) zeigt es in der Zeile „Sicherer Startzustand“. (c) Ist dein Laufwerk verschlüsselt, und findest du den Wiederherstellungsschlüssel unter [https://aka.ms/myrecoverykey](https://aka.ms/myrecoverykey)? (d) Mit welcher Taste öffnest du das Bootmenü deines Rechners? Suche in der Anleitung des Herstellers, statt es auszuprobieren.

:::loesung
Die Angaben hängen von deinem Rechner ab. Auf dem Testrechner dieses Kapitels lautet die Antwort auf (a):

```console Windows (PowerShell)
PS> $env:firmware_type
UEFI
```

(b) In den Systeminformationen steht „Sicherer Startzustand: Ein“, wenn Secure Boot eingeschaltet ist, und „Aus“, wenn nicht; „Nicht unterstützt“ erscheint bei Rechnern, die in der alten BIOS-Betriebsart starten. (c) Unter Einstellungen $\to$ Datenschutz und Sicherheit $\to$ Geräteverschlüsselung bzw. BitLocker siehst du, ob das Laufwerk verschlüsselt ist; unter [https://aka.ms/myrecoverykey](https://aka.ms/myrecoverykey) steht für jedes verschlüsselte Gerät, das mit deinem Microsoft-Konto verbunden ist, ein Schlüssel mit 48 Ziffern. Findest du dort keinen, obwohl die Verschlüsselung eingeschaltet ist, klärst du das, bevor du am Startvorgang irgendetwas änderst. (d) Die Taste steht in der Bedienungsanleitung oder auf der Support-Seite des Herstellers, meist unter „Boot Menu“ oder „Startmenü“; Tabelle [3](#tab-3) nennt die häufigsten.
:::
:::

:::aufgabe Aufgabe 20 ★★ Wo bricht die Kette?
<span class="anker" id="aufg-20"></span>

Ein Rechner hat Secure Boot eingeschaltet. An welchem Glied der Kette aus Abbildung [10](#abb-10) bricht der Start ab, oder startet das System? (a) Jemand hat in GRUB auf dem Stick ein Byte verändert. (b) Der Stick enthält einen Kernel, den niemand signiert hat. (c) Ein Ubuntu-Stick steckt in einem Rechner, dessen Firmware den Prüfschlüssel von Microsoft für fremde Startprogramme nicht enthält. (d) Ein Ubuntu-Stick wird über das Bootmenü gestartet. Löst (d) bei einem verschlüsselten Windows eine Abfrage des Wiederherstellungsschlüssels aus?

:::loesung
(a) Der Start bricht beim Übergang von `shim` zu GRUB ab. `shim` prüft das Siegel von GRUB mit dem Prüfschlüssel von Canonical; nach der Veränderung passt es nicht mehr.

(b) Der Start bricht beim Übergang von GRUB zum Kernel ab, denn GRUB findet am Kernel kein gültiges Siegel. Genau deshalb muss man für einen Kernel ohne Signatur, wie den von Kali Linux, Secure Boot ausschalten.

(c) Schon das erste Glied scheitert: Die Firmware kennt den Prüfschlüssel nicht, mit dem Microsoft `shim` signiert hat, und startet `shim` nicht. Manche Rechner liefern die Firmware so aus. Abhilfe ist eine Einstellung in der Firmware, die diesen Schlüssel erlaubt; das ist eine Änderung an der Startkette, für die vorher der Wiederherstellungsschlüssel gesichert sein muss.

(d) Das System startet: Firmware, `shim`, GRUB und Kernel sind passend signiert. Eine Abfrage des Wiederherstellungsschlüssels ist beim nächsten Start von Windows normalerweise nicht zu erwarten. Das Bootmenü ändert weder den Windows Boot Manager noch eine Einstellung der Firmware; die Startkette von Windows ist beim nächsten Start dieselbe wie vorher. Nur auf älteren Rechnern mit einem Sicherheitschip der Version 1.2 kann eine veränderte Startreihenfolge die Abfrage auslösen. Den Schlüssel hat man trotzdem gesichert, für den Fall, dass ein Rechner sich anders verhält.
:::
:::

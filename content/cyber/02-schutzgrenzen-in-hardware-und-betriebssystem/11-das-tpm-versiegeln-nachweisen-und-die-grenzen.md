---
title: Das TPM: versiegeln, nachweisen und die Grenzen
pfad: Informatik / Cybersecurity / Schutzgrenzen in Hardware und Betriebssystem
adresse: informatik/cybersecurity/schutzgrenzen-in-hardware-und-betriebssystem
knoten: Kapitel 2: Schutzgrenzen in Hardware und Betriebssystem
order: 6121100
summary: Measured Boot nützt nur, wenn jemand die Messwerte auswertet.
tags: diskretes TPM, integriertes TPM, Firmware-TPM, Software-TPM, Versiegeln, Attestierung
lang: de
---

<span class="anker" id="stufe-10"></span>

:::zweck
Measured Boot nützt nur, wenn jemand die Messwerte auswertet. Dieser Abschnitt zeigt die zwei wichtigsten Arten: das TPM selbst, das ein Geheimnis nur bei den richtigen Messwerten herausgibt, und einen entfernten Prüfer, dem das TPM die Messwerte fälschungssicher bescheinigt. Am Ende stehen die Grenzen und der Überblick über alle Schutzgrenzen des Kapitels.
:::

:::::vorwissen Was du dafür brauchst: die Geräteverschlüsselung

<span class="anker" id="stufe-10-1"></span>

BitLocker, in Windows Home Geräteverschlüsselung genannt, verschlüsselt das Laufwerk C:, und Windows entschlüsselt es beim Start selbst, wenn die Startkette unverändert ist. Ist sie verändert, verlangt Windows den Wiederherstellungsschlüssel, eine Zahl mit 48 Ziffern. Zu den Auslösern gehören Änderungen am Bootmanager, ein Update der Firmware und Änderungen an Secure Boot. Wer etwas an der Startkette tut, sichert den Wiederherstellungsschlüssel vorher ([Linux, Kapitel 1, Abschnitt 6.5](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/wie-ein-pc-startet.html#stufe-6-5)).

⁠**Kurz gesagt:** Die Geräteverschlüsselung entsperrt sich nur bei unveränderter Startkette selbst, sonst braucht man den Wiederherstellungsschlüssel.

:::::

### Die Bauformen des TPM

<span class="anker" id="stufe-10-2"></span>

Ein TPM muss kein eigener Chip sein. Es gibt vier Bauformen, die sich darin unterscheiden, wie gut sie das TPM selbst gegen Angriffe schützen.

:::definition Definition 10.1 (Bauformen des TPM)
<span class="anker" id="satz-10-1"></span>

Ein __diskretes TPM__ ist ein eigener Chip auf der Hauptplatine, mit dem Prozessor über eine Leitung verbunden. Ein __integriertes TPM__ ist ein eigener Block innerhalb eines größeren Chips, etwa des Prozessors. Ein __Firmware-TPM__ ist ein Programm, das in einer abgeschotteten Ausführungsumgebung des Prozessors läuft (bei Intel PTT, bei AMD fTPM genannt). Ein __Software-TPM__ ist ein gewöhnliches Programm, das ein TPM nachbildet, etwa für eine virtuelle Maschine oder für Tests.
:::

Gegen Angriffe auf das TPM selbst, etwa das Auslesen des Chips im Labor, gilt das diskrete TPM als die stärkste Bauform, Firmware- und Software-TPM als die schwächsten. Abbildung [42](#abb-42) zeigt die vier Formen.

:::abbildung cyber/k2bauformen 42
Vier Kästen nebeneinander. „Diskret“: eigener Chip auf der Hauptplatine, mit einer sichtbaren Leitung zum Prozessor. „Integriert“: ein Block im Prozessorchip. „Firmware-TPM“: ein Programm in einem abgeschotteten Bereich des Prozessors. „Software-TPM“: ein Programm neben anderen Programmen. Darunter ein Balken „Schutz des TPM selbst“, links hoch, rechts niedrig.
:::

::::beispiel Welche Bauform ein Rechner hat
Viele Notebooks der letzten Jahre benutzen ein Firmware-TPM im Prozessor, viele Hauptplatinen für Desktop-PCs ein diskretes TPM, manchmal als steckbares Modul. Virtuelle Maschinen bekommen ein Software-TPM vom Hypervisor, damit darin etwa Windows 11 installiert werden kann. Für Windows sind alle drei Bauformen ein TPM 2.0.
::::

⁠**Kurz gesagt:** Ein TPM kann ein eigener Chip, ein Block im Prozessor, ein abgeschottetes Firmware-Programm oder eine Nachbildung in Software sein.

### Schlüssel im TPM

<span class="anker" id="stufe-10-3"></span>

Ein TPM soll Schlüssel so verwahren, dass auch ein Programm mit allen Rechten sie nicht kopieren kann. Gleichzeitig hat es nur wenig eigenen Speicher.

:::satz Satz 10.2 (Schlüssel im TPM)
<span class="anker" id="satz-10-2"></span>

Ein TPM kann Schlüssel selbst erzeugen, und es benutzt sie selbst. Ihr geheimer Teil liegt im Klartext nur im geschützten Inneren des TPM. Muss das TPM einen Schlüssel auslagern, weil sein Speicher voll ist, gibt es ihn nur verschlüsselt mit einem eigenen Schlüssel heraus; einige Grundwerte, aus denen das TPM seine eigenen Schlüssel ableitet, verlassen es nie.
:::

Ein ausgelagerter Schlüssel ist für ein Programm nur ein unverständlicher Block. Benutzen kann es ihn nur, indem es ihn dem TPM zurückgibt und das TPM um eine Rechnung bittet.

::::beispiel Wer bei BitLocker was tut
Das Laufwerk ver- und entschlüsselt Windows selbst, mit einem Schlüssel im Arbeitsspeicher. Das TPM verschlüsselt das Laufwerk nicht. Es hütet den Schlüssel, mit dem der Laufwerksschlüssel geschützt ist, und gibt das Geheimnis beim Start nur unter einer Bedingung frei. Welche das ist, zeigt der nächste Unterabschnitt.
::::

⁠**Kurz gesagt:** Geheime Schlüsselteile gibt es im Klartext nur im TPM; nach außen gehen sie höchstens verschlüsselt.

### Das Versiegeln

<span class="anker" id="stufe-10-4"></span>

Jetzt lässt sich das Messen mit dem Verwahren verbinden. Ein Geheimnis soll nur herauskommen, wenn der Rechner genauso gestartet ist wie damals, als man es hineingegeben hat.

:::definition Definition 10.3 (Versiegeln)
<span class="anker" id="satz-10-3"></span>

Beim __Versiegeln__ (englisch sealing) gibt man dem TPM ein Geheimnis zusammen mit einer Bedingung über PCR-Werte. Das TPM gibt das Geheimnis später nur heraus, wenn die angegebenen PCR in diesem Moment genau die verlangten Werte haben.
:::

Das TPM wertet die Messung also selbst aus. Abbildung [43](#abb-43) zeigt das Prinzip.

:::abbildung cyber/k2versiegeln 43
Ein Tresor im TPM mit einem Schloss, auf dem „PCR = 66“ steht. Erster Start: Die Messkette 37, 52 ergibt 66, das Schloss öffnet sich, ein Schlüssel kommt heraus. Zweiter Start mit Bootkit: Die Messkette 37, 52, 81 ergibt 85, das Schloss bleibt zu, der Schlüssel bleibt drin, und Windows fragt nach dem Wiederherstellungsschlüssel.
:::

::::beispiel Versiegeln mit der Spiel-Prüfsumme
Beim Einrichten stand im PCR nach Firmware 37 und Bootloader 52 der Wert 66. Das Geheimnis wird an „PCR = 66“ versiegelt. Beim nächsten gewöhnlichen Start ergibt die Messkette wieder 66, und das TPM gibt das Geheimnis heraus. Startet der Rechner mit einem Bootkit, das den Messwert 81 hinterlässt, steht im PCR 85, und das TPM verweigert die Herausgabe. Das Bootkit läuft zwar, aber an das Geheimnis kommt es nicht.
::::

⁠**Kurz gesagt:** Ein versiegeltes Geheimnis gibt das TPM nur heraus, wenn die PCR dieselben Werte haben wie verlangt.

:::hintergrund Warum Versiegeln brüchig ist
Die Bedingung „genau diese Werte“ ist streng. Ein harmloses Update der Firmware ändert PCR 0, und das versiegelte Geheimnis kommt nicht mehr heraus; die Vorgabe der Trusted Computing Group nennt das „Brüchigkeit“. Deshalb fragt Windows nach manchen Updates den Wiederherstellungsschlüssel ab, und deshalb raten Hersteller, BitLocker vor einem Firmware-Update vorübergehend anzuhalten. Das TPM bietet auch einen Ausweg: Statt fester Werte kann die Bedingung lauten „Werte, die eine bestimmte Stelle mit ihrer Signatur freigegeben hat“. Dann kann der Hersteller für eine neue Firmware neue zulässige Werte freigeben, ohne dass man das Geheimnis neu versiegeln muss.
:::

### BitLocker mit PCR 7 und PCR 11

<span class="anker" id="stufe-10-5"></span>

Die Abfrage des Wiederherstellungsschlüssels aus [Linux, Kapitel 1, Abschnitt 6.5](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/wie-ein-pc-startet.html#stufe-6-5) lässt sich nun genau erklären. BitLocker versiegelt das Geheimnis, das den Laufwerksschlüssel schützt, im TPM, und zwar an zwei PCR.

:::satz Satz 10.4 (Die Bedingung von BitLocker)
<span class="anker" id="satz-10-4"></span>

Auf Rechnern mit Secure Boot bindet BitLocker das Geheimnis an PCR 7, die Richtlinie von Secure Boot. Wer Secure Boot ausschaltet oder seine Schlüssel ändert, verändert PCR 7, und das TPM gibt das Geheimnis nicht frei; Windows fragt nach dem Wiederherstellungsschlüssel. Zusätzlich bindet BitLocker das Geheimnis an den Anfangszustand von PCR 11. Bevor der Bootmanager von Windows die Kontrolle an irgendein Ladeprogramm übergibt, erweitert er PCR 11. Ab diesem Moment lässt sich das Geheimnis bis zum nächsten Neustart nicht mehr entsiegeln.
:::

Microsoft beschreibt das vereinfacht so: Versiegelt wird mit PCR 11 auf dem Wert 0, und beim Übergeben an ein Ladeprogramm setzt der Bootmanager PCR 11 auf den Wert 1. Weil PCR 11 nur erweitert und außer beim Neustart nie zurückgesetzt werden kann, wirkt es wie eine Sperrklinke an einem Zahnrad: Sie lässt das Rad nur in eine Richtung weiterdrehen, so wie sich ein Kabelbinder zuziehen, aber nicht lockern lässt. Abbildung [44](#abb-44) zeigt sie.

:::abbildung cyber/k2sperrklinke 44
Eine Zeitleiste des Starts: Firmware, Bootmanager von Windows, Ladeprogramm, Windows. Darunter PCR 11 als Zahnrad mit Sperrklinke. Solange der Bootmanager läuft, steht es auf „Anfang“, und das TPM gibt das BitLocker-Geheimnis heraus (Schlüssel wandert zum Bootmanager). Beim Übergang zum Ladeprogramm dreht der Bootmanager das Rad eine Raste weiter, die Klinke rastet ein. Ein zweites Ladeprogramm, das später nach dem Geheimnis fragt, bekommt ein rotes Kreuz. Ein Rückwärtsdrehen ist blockiert, erst „Neustart“ setzt das Rad zurück.
:::

::::beispiel Ein fremdes Betriebssystem fragt nach dem Schlüssel
Jemand startet über das Bootmenü des Windows-Bootmanagers ein anderes Betriebssystem und will von dort aus das TPM nach dem BitLocker-Geheimnis fragen. Bevor der Bootmanager an das fremde Ladeprogramm übergab, hat er PCR 11 erweitert. Das TPM vergleicht und verweigert die Herausgabe. Zurücknehmen lässt sich die Erweiterung nicht, also kommt bis zum Neustart niemand mehr an das Geheimnis, und nach dem Neustart steht wieder der echte Bootmanager am Anfang.
::::

⁠**Kurz gesagt:** PCR 7 bindet BitLocker an Secure Boot, PCR 11 sperrt das Geheimnis, sobald der Bootmanager abgegeben hat.

### Die Attestierung

<span class="anker" id="stufe-10-6"></span>

Nicht immer soll das TPM selbst entscheiden. Ein Firmennetz will vielleicht nur Rechner hereinlassen, deren Startkette bekannt und unverändert ist. Fragt es den Rechner einfach, kann ein Bootkit die Antwort fälschen: Einem Rechner, der vielleicht verändert ist, kann man nicht glauben, was er über sich selbst sagt.

:::definition Definition 10.5 (Attestierung)
<span class="anker" id="satz-10-5"></span>

Bei der __Attestierung__ bescheinigt das TPM einem entfernten Prüfer seine aktuellen PCR-Werte. Dazu signiert es die Werte zusammen mit einer frischen Zufallszahl des Prüfers mit einem eigenen Attestierungsschlüssel. Dieser verlässt das TPM nie im Klartext, und er ist so eingeschränkt, dass sich mit ihm keine Bescheinigung fälschen lässt: Fremde Daten, die wie eine Bescheinigung des TPM aufgebaut sind, signiert er nicht. Englisch heißt die Bescheinigung quote. Der Prüfer kontrolliert die Signatur, rechnet das Ereignisprotokoll nach und vergleicht mit bekannten guten Werten.
:::

Die frische Zufallszahl verhindert, dass ein Bootkit eine alte, echte Bescheinigung aus der Zeit vor seinem Einnisten wiederverwendet. Abbildung [45](#abb-45) zeigt den Ablauf.

:::abbildung cyber/k2attest 45
Links ein Prüfer, rechts ein Rechner mit TPM und Ereignisprotokoll. Schritt 1: Der Prüfer schickt eine Zufallszahl, etwa 4711. Schritt 2: Im TPM werden die PCR-Werte und 4711 zu einer Bescheinigung zusammengelegt und mit dem Attestierungsschlüssel signiert (Siegel). Schritt 3: Bescheinigung und Protokoll gehen zurück; der Prüfer kontrolliert das Siegel, rechnet das Protokoll nach und vergleicht mit seiner Liste guter Werte: Häkchen oder Kreuz. Schritt 4: Ein Bootkit schickt stattdessen eine alte Bescheinigung mit der Zahl 1234; der Prüfer sieht „$1234\ne4711$“ und lehnt ab.
:::

::::beispiel Einlass ins Firmennetz
Ein Notebook will sich mit dem Firmennetz verbinden. Der Prüfdienst der Firma schickt eine Zufallszahl, das TPM des Notebooks signiert PCR 0 bis 7 zusammen mit dieser Zahl, und das Notebook schickt Bescheinigung und Ereignisprotokoll zurück. Der Prüfdienst kennt den Prüfschlüssel des TPM, prüft die Signatur, rechnet das Protokoll nach und findet einen Bootloader, der nicht auf seiner Liste steht. Das Notebook bleibt draußen, obwohl es sich selbst für unverändert hält.
::::

⁠**Kurz gesagt:** Bei der Attestierung bescheinigt das TPM seine Messwerte mit einer Signatur, die kein Programm des Rechners fälschen kann.

### Die Grenzen des TPM

<span class="anker" id="stufe-10-7"></span>

Wie jede Grenze in diesem Kapitel hält auch die des TPM nicht alles auf. Drei Grenzen sind wichtig.

:::satz Satz 10.6 (Was das TPM nicht verhindert)
<span class="anker" id="satz-10-6"></span>

<ol>

<li>

⁠*Mitlesen auf der Leitung:* Ein diskretes TPM gibt das entsiegelte Geheimnis über eine Leitung auf der Hauptplatine an den Prozessor. Wer den Rechner öffnet und diese Leitung abhört, kann das Geheimnis bei einem gewöhnlichen Start mitlesen, wenn außer den PCR keine weitere Bedingung gilt.

</li>

<li>

⁠*Fehlende Auswertung:* Measured Boot und das TPM verhindern nichts, wenn niemand die Werte auswertet.

</li>

<li>

⁠*Angriffe auf den laufenden Rechner:* Ist das Laufwerk entsperrt, liegt der Schlüssel im Arbeitsspeicher. Geräte, die über bestimmte Schnittstellen direkt auf den Arbeitsspeicher zugreifen können, und Reste im Speicher kurz nach dem Ausschalten sind Wege, an die das TPM nicht heranreicht.

</li>

</ol>
:::

Gegen die erste und dritte Grenze empfiehlt Microsoft für Angreifer mit Fachwissen und längerem Zugriff auf das Gerät, BitLocker zusätzlich an eine PIN zu binden, die man vor dem Start eingibt, und den Rechner herunterzufahren oder in den Ruhezustand zu versetzen statt ihn nur zuzuklappen. Dann gibt das TPM das Geheimnis erst nach der PIN heraus, und auf der Leitung kommt bei einem Start ohne PIN nichts an. Abbildung [46](#abb-46) zeigt das Mitlesen.

:::abbildung cyber/k2bus 46
Eine Hauptplatine mit Prozessor und einem diskreten TPM, verbunden durch eine sichtbare Leitung. Beim Start wandert das Geheimnis als kleiner Schlüssel über die Leitung; eine Klemme mit einem kleinen Aufzeichnungsgerät an der Leitung zeichnet es auf (rot). Zweite Fassung „TPM mit PIN“: Der Schlüssel bleibt im TPM, bis jemand die PIN eingibt; die Klemme zeichnet nichts auf. Dritte Fassung „integriertes TPM“: Die Leitung liegt im Prozessorchip, die Klemme findet keinen Ansatzpunkt.
:::

::::beispiel Ein Angriff am geöffneten Gehäuse
2019 zeigte ein Sicherheitsforscher, dass sich der BitLocker-Schlüssel eines Rechners mit diskretem TPM und BitLocker ohne PIN mit einem günstigen Gerät mitlesen ließ, das er an die Leitung zwischen TPM und Prozessor anschloss und das alles aufzeichnete, was darüber lief; spätere Arbeiten wiederholten das an anderen Geräten. Bei einem integrierten oder Firmware-TPM gibt es diese offene Leitung nicht, dafür ist dort die Ausführungsumgebung des Prozessors selbst Teil der vertrauenswürdigen Basis, und auch sie wurde in Forschungsarbeiten schon angegriffen. Die Grenze verschiebt sich, sie verschwindet nicht.
::::

⁠**Kurz gesagt:** Das TPM schützt Geheimnisse gegen veränderte Startketten, nicht gegen jemanden, der die Leitung abhört, die Werte nie auswertet oder den laufenden Rechner angreift.

:::warnung Vor jeder Änderung an BitLocker: den Wiederherstellungsschlüssel sichern
Dieses Kapitel liest den Zustand nur aus. Wer BitLocker an eine PIN binden oder sonst etwas an der Verschlüsselung oder der Startkette ändern will, sichert vorher den Wiederherstellungsschlüssel so, dass er ihn ohne diesen Rechner lesen kann ([Linux, Kapitel 1, Abschnitt 6.5](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/wie-ein-pc-startet.html#stufe-6-5)). Rechner einer Hochschule oder eines Arbeitgebers ändert man nur nach Rücksprache mit deren IT-Abteilung.
:::

:::hintergrund Was Vorgaben für Unternehmen und Behörden verlangen
Das IT-Grundschutz-Kompendium des BSI, Edition 2023, verlangt in der Anforderung SYS.2.1.A8 „Absicherung des Bootvorgangs“ als Basisanforderung für jeden Client: „Der Startvorgang des IT-Systems („Booten“) MUSS gegen Manipulation abgesichert werden.“ Die Standardanforderung SYS.2.1.A11 „Beschaffung von Clients“ sieht vor, dass neue Clients eine Konfigurationsoberfläche der Firmware für Secure Boot und, sofern vorhanden, für das TPM haben SOLLTEN, damit die Institution beides selbst verwalten kann. Bei erhöhtem Schutzbedarf SOLLTEN nach SYS.2.1.A36 „Selbstverwalteter Einsatz von SecureBoot und TPM“ Bootloader, Kernel und alle benötigten Teile der Firmware mit selbst kontrolliertem Schlüsselmaterial signiert, nicht benötigtes Schlüsselmaterial entfernt und ein nicht benötigtes TPM abgeschaltet werden. Ende Oktober 2026 hat das BSI mit Grundschutz++ eine neue, maschinenlesbare Fassung seiner Anforderungen vorgestellt, deren Katalog das Kompendium ablösen soll; Zertifizierungen nach dem bisherigen IT-Grundschutz sind laut Zeitplan des BSI noch bis 2031 möglich. Im neuen Katalog heißen die passenden Anforderungen KONF.2.9 „Abgesicherter und authentisierter Bootprozess“ (bei erhöhtem Schutzbedarf, KANN) und KONF.3.1 „Kryptographischer Hardwarespeicher“ (SOLLTE), dessen Erläuterung auf TPM 2.0 verweist.
:::

### Zusammenschau: die Schutzgrenzen im Überblick

<span class="anker" id="stufe-10-8"></span>

Mit den vier Fragen aus Unterabschnitt [1.5](schutzgrenzen-und-der-referenzmonitor.html#stufe-1-5) lassen sich alle Grenzen dieses Kapitels in eine Tabelle bringen (Tabelle [3](#tab-3)).

<span class="anker" id="tab-3"></span>

**Tabelle 3:** Die Schutzgrenzen dieses Kapitels mit den vier Fragen aus Unterabschnitt [1.5](schutzgrenzen-und-der-referenzmonitor.html#stufe-1-5). Jede Zeile ist eine Grenze; die Spalten beantworten, wer sie erzwingt, womit und was sie nicht aufhält.

| Grenze | wer erzwingt | womit | was sie nicht verhindert |
|---|---|---|---|
| Programm $\leftrightarrow$ Kernel | Prozessor | Privilegstufe, privilegierte Befehle, Einsprungtabelle, Prüfung der Argumente (Abschnitte [3](privilegstufen-und-schutzringe.html#stufe-3) und [4](der-eintritt-in-den-kernel.html#stufe-4)) | Fehler im Kernel selbst, denn er ist die vertrauenswürdige Basis |
| Kernel behält die Kontrolle | Prozessor und Zeitgeber | Zeitgeber-Unterbrechung; Zeitgeber stellen und Unterbrechungen sperren nur auf Stufe 0 (Abschnitt [5](die-zeitgeber-unterbrechung.html#stufe-5)) | dass ein Programm seine eigene Rechenzeit verschwendet |
| Prozess $\leftrightarrow$ Prozess | MMU | eigene Seitentabelle je Prozess, Wurzelregister nur auf Stufe 0 (Abschnitt [6](der-virtuelle-adressraum.html#stufe-6)) | was der Kernel bewusst teilt: gemeinsame Seiten, Dateien mit passenden Rechten |
| Kernelspeicher $\leftrightarrow$ Programm | MMU | U/S-Bit; in Gegenrichtung SMEP und SMAP (Abschnitt [7](seitenrechte-kernel-code-und-daten-trennen.html#stufe-7)) | Fehler im Prozessor selbst |
| Daten $\leftrightarrow$ Code | MMU | NX-Bit, Regel W^X (Abschnitt [7](seitenrechte-kernel-code-und-daten-trennen.html#stufe-7)) | dass vorhandener Code in fremder Reihenfolge läuft |
| Startkette $\leftrightarrow$ Betriebssystem | Firmware | Secure Boot mit PK, KEK, Erlaubt- und Sperrliste (Abschnitt [8](die-startkette-als-schutzgrenze.html#stufe-8)) | gültig signierte, aber fehlerhafte Startprogramme, solange sie nicht widerrufen sind |
| Nachweis der Startkette | TPM | Measured Boot, Erweitern, Versiegeln, Attestierung (Abschnitte [9](measured-boot-messen-statt-blockieren.html#stufe-9) und [10](#stufe-10)) | nichts von selbst; nur wer auswertet, merkt etwas; Mitlesen auf der Leitung |

::::beispiel Die Tabelle lesen
Ein Programm will den Speicher eines anderen Prozesses lesen. Die Zeile „Prozess $\leftrightarrow$ Prozess“ sagt: Die MMU verhindert es, weil die Seitenrahmen des anderen in keiner Seitentabelle des Programms stehen und nur der Kernel das Wurzelregister umstellt. Was hilft dem Angreifer? Laut letzter Spalte nur, was der Kernel bewusst teilt, oder ein Fehler in der vertrauenswürdigen Basis aus der ersten Zeile.
::::

⁠**Kurz gesagt:** Jede Grenze hat einen Erzwinger, ein Mittel, das nur Berechtigte einstellen können, und eine Lücke, die man kennen muss.

### Aufgaben zu Abschnitt [10](#stufe-10)

<span class="anker" id="stufe-10-9"></span>

:::aufgabe Aufgabe 29 ★ Richtig oder falsch?
<span class="anker" id="aufg-29"></span>

Begründe jeweils: (a) „Das TPM verschlüsselt die Festplatte.“ (b) „Ein PCR enthält den Messwert des zuletzt gestarteten Programms.“ (c) „Measured Boot blockiert veränderte Bootloader.“ (d) „Ein versiegeltes Geheimnis kann ein Programm mit Verwalterrechten trotzdem aus dem TPM holen.“ (e) „Mit einem integrierten TPM ist BitLocker ohne PIN gegen jeden physischen Angriff sicher.“

:::loesung
(a) Falsch. Das Laufwerk ver- und entschlüsselt Windows. Das TPM hütet den Schlüssel, der den Laufwerksschlüssel schützt, und gibt das versiegelte Geheimnis nur bei passenden PCR-Werten frei.

(b) Falsch. Ein PCR enthält eine Verkettung aller Messwerte seit dem Start in ihrer Reihenfolge, nicht nur den letzten.

(c) Falsch. Measured Boot misst und zeichnet auf; es hält nichts an. Blockiert wird erst, wenn jemand die Werte auswertet, etwa das TPM beim Entsiegeln.

(d) Aus dem TPM nicht: Das TPM prüft die PCR-Werte, und Verwalterrechte im Betriebssystem ändern sie nicht. Ist das Laufwerk aber schon entsperrt, liegt der Laufwerksschlüssel im Arbeitsspeicher, und ein Verwalter kann im laufenden System ohnehin auf alle Daten und die Verwaltungswerkzeuge der Verschlüsselung zugreifen. Das Versiegeln schützt gegen einen Start mit veränderter Kette, nicht gegen den rechtmäßig gestarteten Verwalter.

(e) Falsch. Ein integriertes TPM nimmt dem Angreifer die offene Leitung, aber nicht die Angriffe auf den laufenden Rechner, etwa über Geräte mit direktem Zugriff auf den Arbeitsspeicher, und nicht Angriffe auf die Ausführungsumgebung im Prozessor. Die PIN bleibt die wirksamere Abhilfe gegen Angreifer mit dem Gerät in der Hand.
:::
:::

:::aufgabe Aufgabe 30 ★★ Das TPM am eigenen Rechner
<span class="anker" id="aufg-30"></span>

Öffne unter Windows die App „Windows-Sicherheit“, wähle „Gerätesicherheit“ und dort „Details zum Sicherheitsprozessor“. (a) Welche Version hat das TPM deines Rechners, und ist es bereit? (b) Welche Bauform vermutest du, und wie könntest du es herausfinden? (c) Ist die Geräteverschlüsselung eingeschaltet (Einstellungen $\to$ Datenschutz und Sicherheit $\to$ Geräteverschlüsselung)? Ändere nichts.

:::loesung
Die Antworten hängen vom Rechner ab. Unter „Details zum Sicherheitsprozessor“ stehen Hersteller, Herstellerversion und Spezifikationsversion, bei einem aktuellen Rechner `2.0`, und ob das TPM bereit ist. Ein Hinweis auf die Bauform ist die Herstellerkennung: `INTC` steht für das Firmware-TPM von Intel, `AMD` für das von AMD; Kennungen von Chipherstellern wie `IFX` (Infineon), `STM` (STMicroelectronics) oder `NTC` (Nuvoton) deuten auf ein diskretes TPM. Sicher ist die Bauform nur mit den Unterlagen des Rechners. Ob die Geräteverschlüsselung an ist, steht unter Einstellungen $\to$ Datenschutz und Sicherheit $\to$ Geräteverschlüsselung; fehlt der Punkt, bietet der Rechner sie nicht an.
:::
:::

:::aufgabe Aufgabe 31 ★★ Welche Grenze hält welchen Versuch auf?
<span class="anker" id="aufg-31"></span>

Nenne für jeden Versuch die Grenze aus Tabelle [3](#tab-3), die ihn aufhält, und den Teil, der prüft, oder begründe, warum keine Grenze dieses Kapitels ihn aufhält:

<ol class="al">

<li>

Ein Programm will den Speicher des Browsers lesen.

</li>

<li>

Ein Programm läuft in einer Endlosschleife und soll den Kern für sich behalten.

</li>

<li>

Ein Programm führt CLI aus.

</li>

<li>

Ein Programm schreibt Bytes in seinen Stapel und lenkt den Befehlszeiger darauf.

</li>

<li>

Ein Angreifer ersetzt den Bootloader durch eine veränderte Fassung, Secure Boot ist eingeschaltet.

</li>

<li>

Ein Angreifer bringt eine alte, gültig signierte Fassung eines Bootloaders mit einer bekannten Lücke mit.

</li>

<li>

Ein Angreifer öffnet ein Notebook mit diskretem TPM und BitLocker ohne PIN und hört die Leitung zum Prozessor ab.

</li>

</ol>

:::loesung
<ol class="al">

<li>

Prozess $\leftrightarrow$ Prozess: Die MMU findet für den Speicher des Browsers keine Adresse in den Seitentabellen des Programms, und das Wurzelregister stellt nur der Kernel um.

</li>

<li>

Kernel behält die Kontrolle: Die Zeitgeber-Unterbrechung holt den Kern zurück; der Planer lässt andere Prozesse rechnen.

</li>

<li>

Programm $\leftrightarrow$ Kernel: Der Prozessor führt den privilegierten Befehl auf Stufe 3 nicht aus, löst eine Schutzverletzung aus, und Linux beendet das Programm mit SIGSEGV.

</li>

<li>

Daten $\leftrightarrow$ Code: Der Stapel ist `rw-p`, also nicht ausführbar; die MMU löst beim Holen des ersten Befehls einen Seitenfehler aus.

</li>

<li>

Startkette $\leftrightarrow$ Betriebssystem: Die Firmware prüft die Signatur; die veränderte Fassung passt nicht zur Erlaubt-Liste und startet nicht.

</li>

<li>

Keine Grenze dieses Kapitels hält das sicher auf, solange die alte Fassung nicht widerrufen ist: Ihre Signatur ist gültig. Measured Boot zeichnet einen anderen Messwert in PCR 4 auf; das hilft nur, wenn jemand ihn auswertet, etwa BitLocker oder eine Attestierung.

</li>

<li>

Keine Grenze dieses Kapitels: Das TPM gibt das Geheimnis bei einem gewöhnlichen Start heraus, und auf der Leitung ist es mitzulesen. Abhilfe schafft eine PIN vor dem Start; ein integriertes TPM nimmt dem Angreifer die offene Leitung.

</li>

</ol>
:::
:::

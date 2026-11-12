---
title: Measured Boot: messen statt blockieren
pfad: Informatik / Cybersecurity / Schutzgrenzen in Hardware und Betriebssystem
adresse: informatik/cybersecurity/schutzgrenzen-in-hardware-und-betriebssystem
knoten: Kapitel 2: Schutzgrenzen in Hardware und Betriebssystem
order: 6121000
summary: Secure Boot hält auf, was nicht signiert ist.
tags: Measured Boot, TPM, Plattform-Konfigurationsregister, Erweitern, Ereignisprotokoll
lang: de
---

<span class="anker" id="stufe-9"></span>

:::zweck
Secure Boot hält auf, was nicht signiert ist. Dieser Abschnitt zeigt ein zweites Verfahren, das nichts aufhält, sondern aufschreibt, was gestartet wurde, und zwar so, dass sich die Aufzeichnung nachträglich nicht fälschen lässt.
:::

:::::vorwissen Was du dafür brauchst: die Prüfsumme

<span class="anker" id="stufe-9-1"></span>

Eine Prüfsumme ist ein kurzer Wert, den ein festgelegtes Verfahren aus dem Inhalt einer Datei berechnet. Das Verfahren SHA-256 liefert aus jeder Datei einen Wert aus 256 Bit, geschrieben als 64 Hexadezimalziffern. Jede Änderung, auch die eines einzigen Bits, ergibt einen völlig anderen Wert, und nach heutigem Wissen kann niemand gezielt eine zweite Datei mit demselben Wert herstellen. Unter Linux berechnet `sha256sum` die Prüfsumme einer Datei ([Linux, Kapitel 1, Abschnitt 5.5](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/datentrager-abbild-und-prufsumme.html#stufe-5-5)).

⁠**Kurz gesagt:** Eine Prüfsumme ist ein Fingerabdruck einer Datei, der sich bei jeder Änderung völlig ändert.

:::::

### Messen statt blockieren

<span class="anker" id="stufe-9-2"></span>

[Kapitel 1, Abschnitt 4.3](/wissen/informatik/cybersecurity/sicherheit-schutzziele-und-spielregeln/richtlinie-und-mechanismus.html#stufe-4-3) hat drei Ziele eines Sicherheitsmechanismus unterschieden: verhindern, erkennen, wiederherstellen. Secure Boot verhindert. Für das Erkennen braucht man eine Aufzeichnung darüber, was gestartet wurde.

:::definition Definition 9.1 (Measured Boot, Messen)
<span class="anker" id="satz-9-1"></span>

__Measured Boot__ ist ein Verfahren, bei dem jedes Glied der Startkette das nächste *misst*, bevor es ihm die Kontrolle übergibt, und den Messwert an einer geschützten Stelle aufzeichnet. Messen heißt dabei: eine Prüfsumme des Codes oder der Einstellungen berechnen. Measured Boot hält nichts auf; es zeichnet nur auf.
:::

Die Kette beginnt mit einem unveränderlichen Stück Code der Firmware, dem Vertrauensanker für das Messen. Es misst den Rest der Firmware, die Firmware misst den Bootloader, der Bootloader den Kernel. Secure Boot und Measured Boot schließen sich nicht aus; auf vielen Rechnern laufen beide. Abbildung [37](#abb-37) stellt sie nebeneinander.

:::abbildung cyber/k2zweiketten 37
Zwei Zeilen mit derselben Kette Firmware → Bootloader → Kernel. Obere Zeile „Secure Boot“: Vor jedem Pfeil eine Schranke mit Schloss; ein verändertes Glied (rot) lässt die Schranke geschlossen, der Start bricht ab („verhindert“). Untere Zeile „Measured Boot“: Vor jedem Pfeil eine Waage „messen“, deren Ergebnis in einen Kasten „aufgezeichnet“ fällt; ein verändertes Glied läuft weiter, aber sein Messwert ist anders („erkennbar“).
:::

::::beispiel Beide Verfahren beim Start vom Ubuntu-Stick
Die Firmware findet `shim` auf dem Stick. Für Secure Boot prüft sie die Signatur und startet `shim` nur, wenn sie passt. Für Measured Boot berechnet sie die Prüfsumme von `shim` und zeichnet sie auf, bevor sie startet. Hätte jemand `shim` verändert, hätte Secure Boot den Start verhindert; ohne Secure Boot wäre er weitergelaufen, aber mit einem anderen Messwert in der Aufzeichnung.
::::

⁠**Kurz gesagt:** Secure Boot verhindert, Measured Boot macht erkennbar, was gestartet wurde.

### Das TPM

<span class="anker" id="stufe-9-3"></span>

Die Aufzeichnung darf nicht im gewöhnlichen Arbeitsspeicher oder auf dem Datenträger liegen, denn dort könnte ein Bootkit sie nach Belieben umschreiben. Sie braucht einen eigenen, geschützten Ort.

:::definition Definition 9.2 (TPM)
<span class="anker" id="satz-9-2"></span>

Ein __TPM__ (Trusted Platform Module) ist ein Sicherheitsbaustein mit eigenem geschütztem Speicher und eigenen kryptographischen Funktionen, der Messwerte aufbewahrt und Schlüssel erzeugt, verwahrt und benutzt. Programme und Firmware sprechen das TPM nur über festgelegte Befehle an; in seinen Speicher schreiben oder seine Rechnungen verändern können sie nicht. Aufbau und Befehle legt die Trusted Computing Group fest, die heutige Fassung TPM 2.0 ist auch als Norm ISO/IEC 11889 veröffentlicht.
:::

Das TPM misst nicht selbst; messen und die Werte übergeben muss die Firmware. Es sorgt aber dafür, dass ein übergebener Messwert nicht mehr verschwindet. Abbildung [38](#abb-38) zeigt die Rollen.

:::abbildung cyber/k2tpm 38
Links die Startkette Firmware → Bootloader → Kernel, rechts das TPM als abgeschlossener Kasten mit Speicherplätzen und einem kleinen Rechenwerk. Jedes Glied der Kette schickt einen Messwert über eine schmale Öffnung „nur festgelegte Befehle“ in das TPM, wo er abgelegt wird. Ein Programm versucht, einen Speicherplatz direkt zu überschreiben, und prallt an der Wand des TPM ab.
:::

::::beispiel Ein TPM im eigenen Rechner
Windows 11 setzt ein TPM 2.0 voraus; die meisten PCs, die seit 2016 mit Windows verkauft wurden, haben eines, als eigenen Chip auf der Hauptplatine oder als Teil des Prozessors. [Linux, Kapitel 1, Abschnitt 6.5](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/wie-ein-pc-startet.html#stufe-6-5) hat im Hintergrund erwähnt, dass die Geräteverschlüsselung von Windows ihren Schlüssel einem solchen Sicherheitschip anvertraut.
::::

⁠**Kurz gesagt:** Das TPM ist ein eigener Sicherheitsbaustein, der Messwerte und Schlüssel so verwahrt, dass Programme sie nicht verändern können.

### Das Plattform-Konfigurationsregister

<span class="anker" id="stufe-9-4"></span>

Im TPM gibt es eigene Speicherplätze für die Messwerte der Startkette.

:::definition Definition 9.3 (Plattform-Konfigurationsregister)
<span class="anker" id="satz-9-3"></span>

Ein __Plattform-Konfigurationsregister__ (PCR, platform configuration register) ist ein Speicherplatz im TPM, der einen Wert von der Länge einer Prüfsumme hält, bei SHA-256 also 32 Byte. Beim Neustart des Rechners setzt das TPM alle PCR auf einen festen Anfangswert, meist lauter Nullen. Auf PCs hat das TPM mindestens 24 PCR, nummeriert von 0 bis 23, und zwar für jedes verwendete Prüfsummenverfahren einen eigenen Satz.
:::

Welches PCR welche Messungen aufnimmt, legt für PCs eine Vorgabe der Trusted Computing Group fest; Tabelle [2](#tab-2) zeigt die PCR, die die Firmware benutzt.

<span class="anker" id="tab-2"></span>

**Tabelle 2:** Belegung der PCR auf PCs mit UEFI-Firmware. Die PCR 0 bis 7 gehören der Firmware, 8 bis 15 dem Betriebssystem; die übrigen haben Sonderaufgaben.

| PCR | Messungen |
|---|---|
| 0 | Code der Firmware selbst |
| 1 | Einstellungen der Firmware und der Hauptplatine |
| 2 | Code von Treibern und Programmen, die die Firmware zusätzlich lädt, etwa von Erweiterungskarten |
| 3 | Einstellungen und Daten dieser Treiber und Programme |
| 4 | Code des Bootmanagers bzw. Bootloaders und die Startversuche |
| 5 | Einstellungen des Bootmanagers und die Partitionstabelle (GPT) |
| 6 | dem Hersteller vorbehalten |
| 7 | Richtlinie von Secure Boot: ob es eingeschaltet ist und der Inhalt von PK, KEK, Erlaubt- und Sperrliste |
| 8 bis 15 | für das Betriebssystem |

::::beispiel Was in PCR 7 landet
Schaltet jemand in der Firmware Secure Boot aus oder trägt einen neuen Schlüssel ein, misst die Firmware beim nächsten Start eine andere Secure-Boot-Richtlinie, und PCR 7 bekommt einen anderen Wert als zuvor. Ein Update der Firmware verändert dagegen PCR 0, ein anderer Bootloader PCR 4, eine neue Partitionstabelle PCR 5.
::::

⁠**Kurz gesagt:** PCR sind die Speicherplätze des TPM für Messwerte, und jedes PCR ist für bestimmte Teile der Startkette zuständig.

### Das Erweitern

<span class="anker" id="stufe-9-5"></span>

Ein PCR muss viele Messungen aufnehmen, in PCR 2 etwa jeden Treiber, den die Firmware lädt. Würde jede Messung den alten Wert einfach überschreiben, könnte ein Bootkit nach seinem eigenen Start den Wert eines unveränderten Rechners hineinschreiben. Deshalb gibt es kein Überschreiben.

:::definition Definition 9.4 (Erweitern)
<span class="anker" id="satz-9-4"></span>

Beim __Erweitern__ (englisch extend) eines PCR berechnet das TPM aus dem alten Inhalt und dem neuen Messwert den neuen Inhalt:

<span class="anker" id="gl-9-1"></span>
$$\mathrm{PCR}_\mathrm{neu}=H\bigl(\mathrm{PCR}_\mathrm{alt}\,\|\,m\bigr). \tag{9.1}$$

Dabei ist $m$ der Messwert, $\|$ bedeutet „hintereinanderschreiben“, und $H$ ist das Prüfsummenverfahren des PCR, etwa SHA-256. Bei den PCR 0 bis 15 ist das Erweitern außer dem Zurücksetzen beim Neustart der einzige Weg, ihren Inhalt zu ändern. Nur einige der übrigen PCR mit Sonderaufgaben dürfen auch im Betrieb zurückgesetzt werden.
:::

Der Inhalt eines PCR hängt damit von allen Messwerten ab, die es seit dem Start aufgenommen hat, und von ihrer Reihenfolge. Um das von Hand zu verfolgen, genügt ein Spielzeug-Verfahren.

::::beispiel [Rechenbeispiel] Erweitern mit einer Spiel-Prüfsumme
Als Spiel-Prüfsumme $h$ dient der Rest bei Division durch 97; nach demselben Rest prüfen Banken die Prüfziffern einer IBAN. PCR und Messwerte sind zweistellige Zahlen, und „hintereinanderschreiben“ heißt, die Ziffern aneinanderzuhängen. Das PCR beginnt mit 00. Die Firmware hat den Messwert 37, der Bootloader den Messwert 52.

Reihenfolge Firmware, dann Bootloader:

$$h(00\,37)=37 \bmod 97=37,\qquad h(37\,52)=3752 \bmod 97=3752-38\cdot97=66.$$

Reihenfolge Bootloader, dann Firmware:

$$h(00\,52)=52,\qquad h(52\,37)=5237 \bmod 97=5237-53\cdot97=96.$$

Dieselben zwei Messwerte ergeben 66 oder 96, je nach Reihenfolge (Abbildung [39](#abb-39)). Eine Quersumme wäre als Spiel-Prüfsumme ungeeignet: 3752 und 5237 haben dieselbe Quersumme 17, die Reihenfolge ginge verloren.

:::abbildung cyber/k2rpcr 39
Rechenbild mit zwei Zeilen. Oben: PCR 00, Messwert 37 → $h(0037)=37$, Messwert 52 → $h(3752)=3752-38\cdot97=66$. Unten: PCR 00, Messwert 52 → $h(0052)=52$, Messwert 37 → $h(5237)=5237-53\cdot97=96$. Jeder Schritt als Kasten „alt $\|$ neu“ mit Pfeil zum neuen PCR-Wert. Am Ende stehen 66 und 96 nebeneinander: „gleiche Messwerte, andere Reihenfolge, anderes Ergebnis“.
:::
::::

Mit SHA-256 lässt sich dasselbe an der Shell nachrechnen. Zwei kleine Dateien stehen für die gemessenen Programme. Ein PCR beginnt mit 64 Nullen, `printf '%064d' 0` schreibt sie. Das Werkzeug `xxd -r -p` verwandelt eine Folge von Hexadezimalziffern in die Bytes, die sie bezeichnen; so werden PCR und Messwert als Bytes hintereinandergeschrieben, bevor `sha256sum` die neue Prüfsumme bildet.

::::beispiel Erweitern mit SHA-256
```console
$ printf 'firmware' > firmware.txt
$ printf 'bootloader' > bootloader.txt
$ m1=$(sha256sum firmware.txt | cut -c1-64)
$ m2=$(sha256sum bootloader.txt | cut -c1-64)
$ pcr=$(printf '%064d' 0)
$ pcr=$(printf '%s%s' "$pcr" "$m1" | xxd -r -p | sha256sum | cut -c1-64)
$ echo "$pcr"
3e287e57770de15677579228044a2abe6ca7c39d61de4b8a47fd6b7209dd0bab
$ pcr=$(printf '%s%s' "$pcr" "$m2" | xxd -r -p | sha256sum | cut -c1-64)
$ echo "$pcr"
dd54e062881a8ffb7249e72173ab4900d2e947002641f4bb27d9fd99939fd027
```

In umgekehrter Reihenfolge, erst `$m2`, dann `$m1`, endet das PCR bei `e5e9b1232f49dfec…`, einem völlig anderen Wert. Abbildung [40](#abb-40) zeigt beide Rechnungen nebeneinander.

:::abbildung cyber/k2sha 40
Ein Terminal oben: Die Zeilen der Sitzung erscheinen nacheinander, die beiden Werte `3e287e57…` und `dd54e062…` werden hervorgehoben. Darunter zwei Ketten aus Kästchen. Obere Kette: 64 Nullen, dann „$\|$ Prüfsumme von firmware.txt“ → `3e287e57…`, dann „$\|$ Prüfsumme von bootloader.txt“ → `dd54e062…`. Untere Kette in umgekehrter Reihenfolge: 64 Nullen → … → `e5e9b123…`. Zum Schluss stehen `dd54e062…` und `e5e9b123…` nebeneinander: „gleiche Dateien, andere Reihenfolge, anderer Wert“.
:::
::::

⁠**Kurz gesagt:** Ein PCR wird nie überschrieben, sondern erweitert, und sein Inhalt hängt von allen Messwerten und ihrer Reihenfolge ab.

:::hintergrund Warum Erweitern statt Überschreiben
Angenommen, nach Firmware (37) und Bootloader (52) startet ein Bootkit, das den Messwert 81 hinterlässt. Mit der Spiel-Prüfsumme wird aus 66 der Wert $h(66\,81)=6681 \bmod 97=85$. Das Bootkit möchte, dass im PCR wieder 66 steht, der Wert eines unveränderten Rechners. Überschreiben kann es nicht, also müsste es einen Messwert $x$ finden, mit dem $h(85\,x)=66$ wird. Bei der Spiel-Prüfsumme gelingt das: $8505 \bmod 97=66$, also $x=05$. Genau deshalb benutzt das TPM keine Spiel-Prüfsumme, sondern SHA-256, bei dem nach heutigem Wissen niemand zu einem gewünschten Ergebnis einen passenden Messwert findet. Mit SHA-256 gilt deshalb: Ein Messwert, einmal aufgenommen, lässt sich bis zum Neustart nicht mehr zurücknehmen, und die Reihenfolge der Messungen ist im PCR festgehalten. Das Bootkit kann nur verhindern, dass es selbst gemessen wird, indem es vor dem Messen läuft, und deshalb muss das Messen bei einem unveränderlichen Vertrauensanker beginnen.
:::

### Das Ereignisprotokoll

<span class="anker" id="stufe-9-6"></span>

Ein PCR ist ein einziger Wert. Er verrät, *ob* die Startkette dieselbe war wie bei einem Vergleichsstart, aber nicht, *was* gestartet wurde. Dafür führt die Firmware ein Protokoll.

:::definition Definition 9.5 (Ereignisprotokoll)
<span class="anker" id="satz-9-5"></span>

Das __Ereignisprotokoll__ (event log) ist eine Liste, in die die Firmware bei jedem Erweitern einen Eintrag schreibt: welches PCR erweitert wurde, was gemessen wurde und welchen Messwert sie übergeben hat. Es liegt im gewöhnlichen Speicher und ist für sich nicht geschützt.
:::

Geschützt wird es durch die PCR. Ein Prüfer rechnet die Erweiterungen aus dem Protokoll nach und vergleicht das Ergebnis mit den PCR-Werten im TPM. Stimmen sie überein, ist das Protokoll echt, und er kann darin lesen, was gestartet wurde. Abbildung [41](#abb-41) zeigt das Nachrechnen.

:::abbildung cyber/k2protokoll 41
Links ein Ereignisprotokoll mit zwei Zeilen „Firmware, Messwert 37“ und „Bootloader, Messwert 52“. In der Mitte rechnet ein Prüfer mit der Spiel-Prüfsumme nach: 00 → 37 → 66. Rechts das TPM mit dem PCR-Wert 66: grünes Häkchen „Protokoll echt“. Dann eine zweite Fassung: Das Protokoll behauptet dieselben zwei Zeilen, das TPM zeigt aber 85; das Nachrechnen ergibt 66, rotes Kreuz „Protokoll passt nicht, eine Messung fehlt“.
:::

::::beispiel Ein Protokoll, das lügt
Nach Firmware 37 und Bootloader 52 startet ein Bootkit und hinterlässt den Messwert 81. Im PCR steht dann $h(66\,81)=6681 \bmod 97=85$. Das Bootkit hat seine Zeile aus dem Protokoll gelöscht, dort stehen nur noch Firmware 37 und Bootloader 52. Der Prüfer rechnet $00\to37\to66$ und vergleicht mit dem TPM: $66\ne85$. Er weiß damit nicht, was gefehlt hat, aber er weiß, dass dem Protokoll nicht zu trauen ist und dass die Startkette nicht die erwartete war.
::::

⁠**Kurz gesagt:** Das Ereignisprotokoll sagt, was gemessen wurde, und das Nachrechnen gegen die PCR zeigt, ob es stimmt.

### Was Measured Boot nicht tut

<span class="anker" id="stufe-9-7"></span>

Measured Boot wird oft missverstanden, als würde es manipulierte Startprogramme stoppen.

:::satz Satz 9.6 (Messen allein schützt nicht)
<span class="anker" id="satz-9-6"></span>

Measured Boot verhindert nichts. Ein verändertes Startprogramm läuft, und der Rechner startet. Nutzen entsteht erst, wenn jemand die Messwerte auswertet und daraus eine Folge zieht, zum Beispiel ein Geheimnis nicht herausgibt oder einen Rechner nicht ins Firmennetz lässt.
:::

Das ist das Gegenstück zum Grundsatz „Erkennen, wenn man nicht verhindern kann“ aus [Kapitel 1, Abschnitt 4.3](/wissen/informatik/cybersecurity/sicherheit-schutzziele-und-spielregeln/richtlinie-und-mechanismus.html#stufe-4-3): Erkennen hilft nur, wenn auf das Erkannte etwas folgt.

::::beispiel Ein Rechner ohne Auswertung
Ein Rechner hat ein TPM, und die Firmware misst jeden Start. Niemand fragt die PCR je ab, kein Schlüssel hängt an ihnen, kein Prüfer schaut sie an. Ein Bootkit verändert die Werte, und nichts geschieht. Die Messung ist da, aber wirkungslos.
::::

⁠**Kurz gesagt:** Measured Boot zeichnet auf, und schützen kann erst, wer die Aufzeichnung auswertet.

### Aufgaben zu Abschnitt [9](#stufe-9)

<span class="anker" id="stufe-9-8"></span>

:::aufgabe Aufgabe 25 ★ Drei Messungen, zwei Reihenfolgen
<span class="anker" id="aufg-25"></span>

Erweitere ein PCR mit dem Anfangswert 00 mit der Spiel-Prüfsumme aus dem Rechenbeispiel nacheinander um die Messwerte 37, 52 und 18. Rechne dann mit der Reihenfolge 52, 37, 18. Welche Endwerte ergeben sich?

:::loesung
Reihenfolge 37, 52, 18: $00\to37\to66$ wie im Rechenbeispiel, dann $h(66\,18)=6618 \bmod 97=6618-68\cdot97=22$.

Reihenfolge 52, 37, 18: $00\to52\to96$, dann $h(96\,18)=9618 \bmod 97=9618-99\cdot97=15$.

Gleiche Messwerte in anderer Reihenfolge führen zu den Endwerten 22 und 15. Dass die letzte Messung in beiden Fällen dieselbe war, gleicht den Unterschied nicht aus.
:::
:::

:::aufgabe Aufgabe 26 ★ Welches PCR ändert sich?
<span class="anker" id="aufg-26"></span>

Welches PCR aus Tabelle [2](#tab-2) nimmt einen anderen Wert an, wenn (a) ein Update der Firmware eingespielt wird, (b) jemand in der Firmware Secure Boot ausschaltet, (c) ein anderer Bootloader installiert wird, (d) eine neue Partition angelegt wird?

:::loesung
(a) PCR 0, der Code der Firmware. (b) PCR 7, die Richtlinie von Secure Boot. (c) PCR 4, der Code des Bootloaders. (d) PCR 5, denn dort wird die Partitionstabelle gemessen.
:::
:::

:::aufgabe Aufgabe 27 ★★ Erweitern an der Shell
<span class="anker" id="aufg-27"></span>

Rechne das Beispiel „Erweitern mit SHA-256“ in deinem Übungsverzeichnis nach, einmal in der Reihenfolge `firmware.txt`, `bootloader.txt` und einmal umgekehrt. Ändere dann in `bootloader.txt` einen einzigen Buchstaben und rechne erneut. Was zeigt der Vergleich der drei Endwerte?

:::loesung
Die beiden Reihenfolgen ergeben auf jedem Rechner dieselben Werte wie im Kapitel, weil SHA-256 festgelegt ist und die Dateien denselben Inhalt haben: `dd54e062…` für Firmware vor Bootloader, `e5e9b123…` für die umgekehrte Reihenfolge. Nach der Änderung eines einzigen Buchstabens in `bootloader.txt` entsteht ein dritter, völlig anderer Wert. Der Vergleich zeigt beide Eigenschaften des Erweiterns: Das Ergebnis hängt von der Reihenfolge ab und von jedem einzelnen Byte jedes Messwerts.
:::
:::

:::aufgabe Aufgabe 28 ★★ Den Messwert zurücknehmen?
<span class="anker" id="aufg-28"></span>

Ein PCR hat nach Firmware 37, Bootloader 52 und einem Bootkit mit Messwert 81 den Wert 85 (Spiel-Prüfsumme). (a) Finde alle zweistelligen Messwerte $x$, mit denen das Bootkit das PCR durch ein weiteres Erweitern auf 96 bringen könnte. (b) Warum hilft das dem Bootkit bei einem echten TPM mit SHA-256 nicht? (c) Was müsste das Bootkit stattdessen erreichen, um gar nicht erst gemessen zu werden?

:::loesung
(a) Gesucht ist $x$ mit $h(85\,x)=(8500+x) \bmod 97=96$. Es ist $8500 \bmod 97=8500-87\cdot97=61$, also muss $(61+x) \bmod 97=96$ sein, das heißt $x=35$. Probe: $8535 \bmod 97=8535-87\cdot97=96$. Die nächste Lösung wäre $35+97=132$, also nicht zweistellig; $x=35$ ist die einzige.

(b) Mit SHA-256 müsste das Bootkit einen Messwert $m$ finden, für den $H(\mathrm{PCR}\,\|\,m)$ genau einen vorgegebenen Wert ergibt. Nach heutigem Wissen kann das niemand, auch nicht mit sehr viel Rechenzeit. Das Bootkit kann das PCR also nur weiter verändern, nie gezielt auf einen gewünschten Wert bringen.

(c) Es müsste laufen, bevor es gemessen wird, also vor dem Glied, das es messen würde, oder dieses Glied so verändern, dass es nicht misst. Dieses Glied wird aber seinerseits vorher gemessen. Am Ende der Kette bleibt nur der Vertrauensanker für das Messen, und den kann es nicht verändern, wenn er wirklich unveränderlich ist.
:::
:::

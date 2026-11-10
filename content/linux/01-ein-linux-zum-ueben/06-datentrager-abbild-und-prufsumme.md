---
title: Datenträger, Abbild und Prüfsumme
pfad: Informatik / Linux und Kommandozeile / Ein Linux zum Üben: WSL, virtuelle Maschine, Live-USB-Stick
adresse: informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick
knoten: Kapitel 1: Ein Linux zum Üben: WSL, virtuelle Maschine, Live-USB-Stick
order: 6060600
summary: Für eine virtuelle Maschine und für den Live-USB-Stick lädt man ein ganzes Betriebssystem als eine einzige Datei herunter.
tags: Datenträger, Sektoren, Partition, Partitionstabelle, Dateisystem, Abbild, ISO-Abbild, Prüfsumme
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Für eine virtuelle Maschine und für den Live-USB-Stick lädt man ein ganzes Betriebssystem als eine einzige Datei herunter. Dieser Abschnitt erklärt, was in einer solchen Datei steckt, und wie man mit einer Prüfsumme feststellt, dass sie unterwegs nicht verändert wurde. Dafür braucht man zuerst drei Grundbegriffe über Datenträger.
:::

:::::vorwissen Was du dafür brauchst: der Datenträger

<span class="anker" id="stufe-5-1"></span>

Arbeitsspeicher vergisst alles, sobald der Strom weg ist. Was bleiben soll, muss auf einem Gerät stehen, das es dauerhaft festhält.

:::definition Definition 5.1 (Datenträger)
<span class="anker" id="satz-5-1"></span>

Ein __Datenträger__ ist ein Gerät, das Daten ohne Strom dauerhaft speichert, etwa eine SSD, eine Festplatte, ein USB-Stick oder eine Speicherkarte. Für das Betriebssystem ist er eine lange Reihe gleich großer, durchnummerierter Blöcke, meist zu je 512 Byte; diese Blöcke heißen __Sektoren__.
:::

::::beispiel Wie groß ist ein 8-GB-Stick?
Ein USB-Stick mit der Aufschrift „8 GB“ hat zum Beispiel 15 633 408 Sektoren zu 512 Byte, also 8 004 304 896 Byte. Hersteller zählen in Zehnerpotenzen: $1\,\mathrm{GB}=10^9$ Byte, der Stick hat also 8,00 GB. Windows und viele Linux-Programme rechnen dagegen in Zweierpotenzen, $1\,\mathrm{GiB}=2^{30}\,\mathrm{Byte}=1\,073\,741\,824$ Byte. In dieser Einheit hat der Stick

$$\frac{8\,004\,304\,896\ \mathrm{Byte}}{1\,073\,741\,824\ \mathrm{Byte/GiB}}=7{,}45\ \mathrm{GiB}.$$

Windows schreibt dafür „7,45 GB“, obwohl es GiB meint. Eine SSD mit der Aufschrift „512 GB“ hat meist etwas mehr als $512\cdot10^9$ Byte, nämlich 512 110 190 592 Byte, und erscheint deshalb als 476,9 GB. An solchen Zahlen erkennt man einen Datenträger in einer Liste sicher wieder.
::::

⁠**Kurz gesagt:** Ein Datenträger ist eine lange Reihe nummerierter Blöcke, die ihren Inhalt auch ohne Strom behalten.

:::::

:::::vorwissen Was du dafür brauchst: die Partition

<span class="anker" id="stufe-5-2"></span>

Eine SSD soll oft mehreren Zwecken dienen: einem Bereich für das Betriebssystem, einem für die Startdateien und einem für die Wiederherstellung im Notfall. Deshalb teilt man sie in Abschnitte.

:::definition Definition 5.2 (Partition)
<span class="anker" id="satz-5-2"></span>

Eine __Partition__ ist ein zusammenhängender Abschnitt eines Datenträgers, den das Betriebssystem wie einen eigenen Datenträger behandelt. Wo jede Partition beginnt und endet, steht in der __Partitionstabelle__ am Anfang des Datenträgers. Heute üblich ist eine Tabelle nach dem Verfahren GPT; ältere Datenträger und viele USB-Sticks benutzen das ältere Verfahren MBR.
:::

::::beispiel Die SSD eines Windows-Laptops
Auf der SSD eines typischen Windows-Rechners liegen vier Partitionen: vorn eine kleine EFI-Systempartition mit einigen hundert MB, die die Startdateien enthält; eine winzige Partition, die Windows für eigene Zwecke freihält; die große Partition, die Windows als Laufwerk C: zeigt; und am Ende eine Wiederherstellungspartition mit Werkzeugen für den Notfall. Nur Laufwerk C: hat einen Buchstaben, die anderen drei sieht man im Explorer nicht.
::::

⁠**Kurz gesagt:** Eine Partition ist ein Abschnitt eines Datenträgers; die Partitionstabelle am Anfang sagt, wo welcher liegt.

:::::

:::::vorwissen Was du dafür brauchst: das Dateisystem

<span class="anker" id="stufe-5-3"></span>

Eine Partition ist zunächst nur eine Reihe von Sektoren. Dass darin Dateien mit Namen und Ordnern stehen, ist eine Ordnung, die erst das Betriebssystem hineinbringt.

:::definition Definition 5.3 (Dateisystem)
<span class="anker" id="satz-5-3"></span>

Ein __Dateisystem__ ist die Ordnung, nach der ein Betriebssystem Dateien und Ordner in den Sektoren einer Partition ablegt. Es legt fest, wo die Namen stehen, in welchen Sektoren der Inhalt jeder Datei liegt und wo noch Platz frei ist; viele Dateisysteme halten außerdem fest, wer eine Datei lesen darf.
:::

::::beispiel [Beispiele] Fünf Dateisysteme
Windows benutzt für Laufwerk C: das Dateisystem NTFS. USB-Sticks und Speicherkarten sind meist mit FAT32 oder exFAT eingerichtet, weil fast jedes Gerät diese lesen kann. Linux benutzt für seine eigenen Partitionen meist ext4; auch die virtuelle Festplatte von WSL 2 enthält ein ext4. Die Startdateien in der EFI-Systempartition stehen in einem FAT-Dateisystem. CDs und DVDs schließlich benutzen das Dateisystem ISO 9660. Wenn Windows einen Stick „formatiert“, legt es auf ihm ein neues, leeres Dateisystem an; die alten Dateien sind danach nicht mehr auffindbar.
::::

⁠**Kurz gesagt:** Das Dateisystem macht aus den Sektoren einer Partition Dateien und Ordner.

:::::

### Das Abbild

<span class="anker" id="stufe-5-4"></span>

Ein Betriebssystem besteht aus Tausenden Dateien, dazu aus einer Partitionstabelle und den Startdateien, ohne die ein Rechner es nicht starten kann. Um es zu verteilen, packt man das alles in eine einzige Datei, und zwar so, dass man aus dieser Datei wieder einen startfähigen Datenträger machen kann.

:::definition Definition 5.4 (Abbild, ISO-Abbild)
<span class="anker" id="satz-5-4"></span>

Ein __Abbild__ (englisch image) ist eine Datei, die den Inhalt eines ganzen Datenträgers Sektor für Sektor enthält, mit Partitionstabelle, Dateisystemen und Startdateien. Ein __ISO-Abbild__ ist ein Abbild im Format einer CD oder DVD; es trägt die Endung `.iso`.
:::

Die ISO-Abbilder von Ubuntu und vielen anderen Distributionen sind so gebaut, dass dieselbe Datei als DVD und als USB-Stick funktioniert, auf älteren und auf neueren Rechnern.

::::beispiel Das Abbild von Ubuntu 26.04.1
Ubuntu stellt das System für Arbeitsplatzrechner als `ubuntu-26.04.1-desktop-amd64.iso` bereit. Die Datei ist 6 482 409 472 Byte groß, also 6,48 GB oder 6,04 GiB. Auf einen Stick mit 8 GB passt sie, mit gut 1,5 GB Rest; ein Stick mit 4 GB wäre zu klein. Der Name verrät auch, für welche Prozessoren das Abbild gebaut ist: `amd64` steht für die 64-Bit-Prozessoren der PCs, von Intel ebenso wie von AMD.
::::

Auch die Festplatte einer virtuellen Maschine aus Unterabschnitt [3.1](virtuelle-maschinen-der-rechner-im-rechner.html#stufe-3-1) und die Datei `ext4.vhdx` von WSL 2 sind Abbilder in einem weiteren Sinn: Dateien, die für ihren Gast einen ganzen Datenträger darstellen. Sie enthalten ihn allerdings nicht Sektor für Sektor, sondern in einem eigenen Format, das nur die beschriebenen Bereiche speichert.

⁠**Kurz gesagt:** Ein Abbild ist ein ganzer Datenträger in einer einzigen Datei.

:::warnung Ein Abbild wird geschrieben, nicht kopiert
Wer die ISO-Datei einfach auf einen USB-Stick kopiert, hat danach einen Stick mit einer Datei darauf, und von dem startet kein Rechner. Damit der Stick selbst zum Datenträger aus dem Abbild wird, muss ein eigenes Programm den Inhalt der Datei Sektor für Sektor auf den Stick schreiben. Dabei geht alles verloren, was vorher auf dem Stick war.
:::

:::hintergrund Wie eine Datei zugleich DVD und USB-Stick sein kann
Eine DVD und ein USB-Stick werden beim Start auf verschiedene Weise gelesen. Für DVDs gibt es einen eigenen Standard, der am Anfang des ISO-9660-Dateisystems einen Verweis auf die Startdateien vorsieht. Ein USB-Stick wird dagegen wie eine Festplatte gelesen: Die Startsoftware des Rechners sucht vorn eine Partitionstabelle und darin eine Partition mit Startdateien. Die Abbilder von Ubuntu enthalten beides zugleich. In die ersten Sektoren, die das DVD-Format frei lässt, ist zusätzlich eine Partitionstabelle eingetragen, und eine ihrer Partitionen zeigt auf einen kleinen Bereich mit den Startdateien. Je nachdem, ob die Datei als DVD oder als Platte gelesen wird, findet der Rechner die eine oder die andere Struktur. Man nennt solche Abbilder *hybrid*.
:::

### Die Prüfsumme

<span class="anker" id="stufe-5-5"></span>

Ein Download von 6,5 GB kann unterwegs beschädigt werden, und ein einziges falsches Bit kann ein Startprogramm unbrauchbar machen. Schlimmer wäre ein Abbild, in das jemand absichtlich Schadsoftware eingebaut hat. Man möchte also prüfen, ob die heruntergeladene Datei genau die ist, die der Herausgeber veröffentlicht hat, ohne dafür die 6,5 GB Byte für Byte mit dem Original vergleichen zu müssen.

**Ein Fingerabdruck der Datei.** Die Idee: Aus dem Inhalt der Datei berechnet ein festgelegtes Verfahren eine kurze Zahl, eine Art Fingerabdruck. Der Herausgeber veröffentlicht den Fingerabdruck seiner Datei, du berechnest den deiner Kopie, und stimmen beide überein, ist die Kopie unverändert. Abbildung [9](#abb-9) zeigt, dass schon die kleinste Änderung einen völlig anderen Fingerabdruck ergibt.

:::abbildung linux/k1pruefsumme 9
Die Prüfsumme als Fingerabdruck. Zwei Dateien, die sich in einem einzigen Buchstaben unterscheiden, ergeben mit dem Verfahren SHA-256 zwei völlig verschiedene Werte (hier gekürzt). Ein gleicher Wert bedeutet umgekehrt: gleicher Inhalt.
:::

:::definition Definition 5.5 (Prüfsumme, SHA-256)
<span class="anker" id="satz-5-5"></span>

Eine __Prüfsumme__ ist ein kurzer Wert, den ein festgelegtes Verfahren aus dem Inhalt einer Datei berechnet. Die Abbilder von Linux-Distributionen benutzen das Verfahren __SHA-256__, das der US-Standard FIPS 180-4 festlegt. Es liefert aus jeder Datei, gleich wie groß, einen Wert aus 256 Bit, geschrieben als 64 Hexadezimalziffern `0`–`9` und `a`–`f`. Gleicher Inhalt ergibt immer denselben Wert. SHA-256 ist so gebaut, dass jede Änderung, auch die eines einzigen Bits, einen völlig anderen Wert ergibt und dass nach heutigem Wissen niemand gezielt eine zweite Datei mit demselben Wert herstellen kann.
:::

::::beispiel Ein Buchstabe Unterschied
Die Datei `gruss.txt` enthält die Zeile `Hallo Linux`, die Datei `gruss2.txt` die Zeile `Hallo Linuy`. Der Befehl `sha256sum` berechnet unter Linux die Prüfsumme einer Datei:

```console Linux
$ sha256sum gruss.txt
99fe677717755bcd765dabb7092a68d674ecb79d8e1885a042ca5c90157c1098  gruss.txt
$ sha256sum gruss2.txt
bcfef736955e8b5f649a111842d4a17f4d9b8c9bf1ed32ea6ef7c179d102bdd5  gruss2.txt
```

Von den 64 Stellen stimmen nur 5 zufällig überein; bei zwei völlig fremden Werten wären im Mittel $64/16=4$ gleich. Ein einziger Buchstabe Unterschied hat den Wert also so gründlich verändert, als stammte er von einer ganz anderen Datei.
::::

⁠**Kurz gesagt:** Die Prüfsumme ist der Fingerabdruck einer Datei: gleicher Inhalt, gleicher Wert; jede Änderung, ein anderer Wert.

:::hintergrund Warum man dafür eine kryptographische Hashfunktion nimmt
Eine einfache Prüfsumme, etwa die Summe aller Bytes, würde zufällige Übertragungsfehler oft erkennen. Sie hat aber zwei Schwächen. Vertauscht man zwei Bytes, bleibt die Summe gleich. Und wer absichtlich etwas ändert, kann an anderer Stelle ein Byte so anpassen, dass die Summe wieder stimmt. SHA-256 gehört zu den *kryptographischen Hashfunktionen*, die gegen beides gebaut sind. Jedes Bit des Ergebnisses hängt in verwickelter Weise von jedem Bit der Eingabe ab, sodass eine kleine Änderung im Mittel die Hälfte aller Ergebnisbits umwirft. Und es ist kein Weg bekannt, zu einem gegebenen Wert eine passende Datei zu finden, der wesentlich schneller wäre als blindes Probieren. Bei $2^{256}\approx1{,}16\cdot10^{77}$ möglichen Werten ist blindes Probieren aussichtslos. Wie solche Funktionen aufgebaut sind, behandelt die Reihe Cybersecurity.
:::

### Prüfen: erst von Auge, dann mit dem Werkzeug

<span class="anker" id="stufe-5-6"></span>

Der Herausgeber veröffentlicht die Prüfsummen seiner Abbilder in einer kleinen Textdatei neben den Abbildern. Bei Ubuntu heißt sie `SHA256SUMS`. Für Ubuntu 26.04 sieht sie so aus:

```text SHA256SUMS
487f87faaf547ea30e0aba4d5b53346292571256b25333a978db1692bcee9dd2 *ubuntu-26.04-desktop-amd64.iso
dec49008a71f6098d0bcfc822021f4d042d5f2db279e4d75bdd981304f1ca5d9 *ubuntu-26.04-live-server-amd64.iso
96c7f5fb28a7fe28245331f9bfbe4375f18dd29a4850116ad3c4f60f6700c55c *ubuntu-26.04-wsl-amd64.wsl
601e30fbf5d97759367c632e2c33630665039b7e2158fd068403da3ccf1bda1f *ubuntu-26.04.1-desktop-amd64.iso
cc8a95cde20f6ced61a322420de00f10cc3c90ced545daa46cb9c1a117f1d927 *ubuntu-26.04.1-live-server-amd64.iso
48d56724b5c8e60f24893e83e73bbb58c60b3ca22fba3da977075420acd54104 *ubuntu-26.04.1-wsl-amd64.wsl
```

Jede Zeile enthält eine Prüfsumme, ein Leerzeichen, ein Sternchen und den Dateinamen. Das Sternchen sagt nur, dass die Datei als Folge von Bytes gelesen werden soll. Der Wert für das Abbild aus Unterabschnitt [5.4](#stufe-5-4) steht in der vierten Zeile.

**Von Auge.** Der einfachste Weg: Man berechnet die Prüfsumme seiner Kopie und vergleicht sie Zeichen für Zeichen mit der Zeile in `SHA256SUMS`. Das ist mühsam bei 64 Zeichen, und es verführt dazu, nur den Anfang und das Ende zu vergleichen. Gegen einen zufälligen Übertragungsfehler würde das reichen. Gegen eine absichtliche Fälschung reicht es nicht: Wer nur die ersten und letzten vier Zeichen vergleicht, prüft 8 Hexadezimalziffern, und eine Fälschung, die in genau diesen 8 Ziffern passt, findet ein Angreifer durch Probieren nach etwa $16^8=2^{32}\approx4{,}3$ Milliarden Versuchen. Jeder Versuch trifft nur mit der Wahrscheinlichkeit $1/16^8$, deshalb braucht man im Mittel genau so viele Versuche. Ein Rechner, der eine Milliarde Versuche je Sekunde schafft, braucht dafür im Mittel rund 4 Sekunden. Entweder vergleicht man also alle 64 Zeichen, oder man lässt das Werkzeug vergleichen.

**Mit dem Werkzeug unter Linux.** Der Befehl `sha256sum -c` liest eine Datei wie `SHA256SUMS`, berechnet für jede genannte Datei die Prüfsumme und vergleicht selbst. Das folgende Beispiel zeigt es an der kleinen Datei `gruss.txt`.

::::beispiel Eine eigene Prüfsummenliste prüfen
Die Datei `PRUEFSUMMEN` enthält eine einzige Zeile im selben Format wie `SHA256SUMS`. Danach wird `gruss.txt` in `Hallo Linuy` geändert und noch einmal geprüft:

```console Linux
$ cat PRUEFSUMMEN
99fe677717755bcd765dabb7092a68d674ecb79d8e1885a042ca5c90157c1098  gruss.txt
$ sha256sum -c PRUEFSUMMEN
gruss.txt: OK
$ sha256sum -c PRUEFSUMMEN
gruss.txt: FAILED
sha256sum: WARNING: 1 computed checksum did NOT match
```

`OK` heißt: gleiche Prüfsumme, unveränderter Inhalt. `FAILED` heißt: Die Datei ist nicht mehr die, deren Prüfsumme in der Liste steht.
::::

Für das Ubuntu-Abbild legst du `SHA256SUMS` in denselben Ordner wie die ISO-Datei und schreibst `sha256sum -c SHA256SUMS --ignore-missing`. Der Zusatz `--ignore-missing` überspringt die Dateien der Liste, die du nicht heruntergeladen hast. Steht danach `ubuntu-26.04.1-desktop-amd64.iso: OK` da, ist das Abbild unverändert. Meldet das Werkzeug stattdessen `no file was verified`, liegt die ISO-Datei nicht im selben Ordner wie die Liste.

**Mit dem Werkzeug unter Windows.** In der PowerShell berechnet `Get-FileHash` die Prüfsumme, standardmäßig nach SHA-256. Der Zusatz `| Format-List` schreibt das Ergebnis untereinander, damit der lange Wert nicht abgeschnitten wird.

::::beispiel Dieselbe Datei unter Windows
Die Datei `gruss.txt` liegt jetzt im Ordner „Downloads“ des Windows-Benutzers `student`:

```console Windows (PowerShell)
PS> Get-FileHash .\gruss.txt | Format-List

Algorithm : SHA256
Hash      : 99FE677717755BCD765DABB7092A68D674ECB79D8E1885A042CA5C90157C1098
Path      : C:\Users\student\Downloads\gruss.txt

PS> (Get-FileHash .\gruss.txt).Hash -eq "99fe677717755bcd765dabb7092a68d674ecb79d8e1885a042ca5c90157c1098"
True
```

Der Wert ist derselbe wie unter Linux, nur in Großbuchstaben. Die zweite Zeile lässt die PowerShell vergleichen: Zwischen die Anführungszeichen kopierst du den Wert aus `SHA256SUMS`. Der Vergleich `-eq` achtet nicht auf Groß- und Kleinschreibung und antwortet mit `True` bei Gleichheit, sonst mit `False`.
::::

⁠**Kurz gesagt:** Prüfsummen vergleicht man vollständig, am besten mit `sha256sum -c` oder mit `Get-FileHash` und `-eq`.

### Was die Prüfsumme beweist und was nicht

<span class="anker" id="stufe-5-7"></span>

Stimmt die Prüfsumme, ist die Datei genau die, deren Wert in `SHA256SUMS` steht. Das beweist, dass beim Herunterladen nichts kaputtgegangen ist. Es beweist aber nicht, dass die Datei vom Herausgeber stammt.

::::beispiel Ein ausgetauschter Spiegelserver
Große Dateien laden viele Leute nicht direkt beim Herausgeber, sondern von einem Spiegelserver, etwa einer Hochschule, die Kopien bereitstellt. Angenommen, ein Angreifer hat einen solchen Server übernommen und dort das Abbild gegen eines mit eingebauter Schadsoftware getauscht. Dann tauscht er auch die Datei `SHA256SUMS` daneben aus und trägt die Prüfsumme seines Abbilds ein. Wer beides von diesem Server lädt, bekommt beim Prüfen ein beruhigendes `OK`: Die Datei passt ja zur Liste. Nur sind Datei und Liste beide gefälscht.
::::

Die Prüfsumme beweist also die __Unversehrtheit__ der Datei gegenüber der Liste, nicht ihre Herkunft. Dass die Liste selbst echt ist, belegt erst eine __digitale Signatur__ des Herausgebers: eine Art fälschungssicheres Siegel, das nur der Besitzer eines geheimen Schlüssels anbringen kann und das jeder mit einem dazu passenden, öffentlichen Prüfschlüssel kontrollieren kann. Bei Ubuntu steht die Signatur der Liste in der Datei `SHA256SUMS.gpg`; wie eine Signatur mathematisch funktioniert und wie man sie prüft, erklärt die Reihe Cybersecurity. Für dieses Kapitel genügt: Lade Abbild und `SHA256SUMS` von der offiziellen Seite des Herausgebers, bei Ubuntu von [https://ubuntu.com/download/desktop](https://ubuntu.com/download/desktop) oder [https://releases.ubuntu.com](https://releases.ubuntu.com), und prüfe die Prüfsumme immer.

⁠**Kurz gesagt:** Eine stimmende Prüfsumme beweist, dass die Datei unverändert ist, aber nicht, dass sie echt ist.

### Aufgaben zu Abschnitt [5](#stufe-5)

<span class="anker" id="stufe-5-8"></span>

:::aufgabe Aufgabe 15 ★ Eine Prüfsumme auf beiden Seiten
<span class="anker" id="aufg-15"></span>

Lege unter Windows mit dem Editor eine Textdatei mit einer Zeile deiner Wahl an. Berechne ihre Prüfsumme in der PowerShell mit `Get-FileHash`. Falls du WSL 2 eingerichtet hast, berechne sie auch in Linux mit `sha256sum`; der Pfad beginnt dort mit `/mnt/c`. Stimmen die Werte überein? Ändere dann ein einziges Zeichen, speichere und berechne die Prüfsumme noch einmal.

:::loesung
Beide Werkzeuge lesen dieselben Bytes der Datei und wenden dasselbe Verfahren SHA-256 darauf an; die Werte stimmen deshalb überein, unter Windows in Großbuchstaben, unter Linux in Kleinbuchstaben. Liegt die Datei zum Beispiel unter `C:\Users\<Name>\Documents\notiz.txt`, lautet der Befehl in Linux `sha256sum /mnt/c/Users/<Name>/Documents/notiz.txt`. Nach der Änderung eines einzigen Zeichens ist der Wert völlig anders, wie im Beispiel „Ein Buchstabe Unterschied“.

Stimmten die Werte vor der Änderung nicht überein, haben die beiden Werkzeuge nicht dieselbe Datei gelesen, etwa weil der Editor die Datei noch nicht gespeichert hatte oder weil zwei Dateien mit ähnlichem Namen existieren. Prüfsummen vergleichen Bytes, nicht den sichtbaren Text: Ein unsichtbarer Unterschied, etwa ein zusätzliches Leerzeichen am Zeilenende, ergibt einen anderen Wert.
:::
:::

:::aufgabe Aufgabe 16 ★★ Wie viel verrät ein Teil des Werts?
<span class="anker" id="aufg-16"></span>

<ol class="al">

<li>

Zähle in den beiden Prüfsummen aus dem Beispiel „Ein Buchstabe Unterschied“ die Stellen, an denen beide Werte dieselbe Ziffer haben. Wie viele gleiche Stellen erwartest du bei zwei zufälligen Werten im Mittel, und warum?

</li>

<li>

Jemand vergleicht nur die ersten sechs Zeichen. Wie viele Versuche braucht ein Angreifer etwa, um eine Fälschung zu finden, deren Prüfsumme mit denselben sechs Zeichen beginnt? Wie viele wären es, wenn man alle 64 Zeichen vergleicht?

</li>

</ol>

:::loesung
(a) Die beiden Werte

```text
99fe677717755bcd765dabb7092a68d674ecb79d8e1885a042ca5c90157c1098
bcfef736955e8b5f649a111842d4a17f4d9b8c9bf1ed32ea6ef7c179d102bdd5
```

stimmen an 5 der 64 Stellen überein. Wenn zwei Werte ohne Zusammenhang sind, ist jede Stelle unabhängig eine der 16 Hexadezimalziffern, und die Wahrscheinlichkeit, dass sie an einer Stelle übereinstimmen, ist $1/16$. Im Mittel erwartet man deshalb $64\cdot\frac1{16}=4$ gleiche Stellen. 5 ist ein ganz gewöhnlicher Zufallswert; die beiden Prüfsummen verhalten sich wie zwei fremde Werte, obwohl sich die Dateien nur in einem Buchstaben unterscheiden.

(b) Sechs Hexadezimalziffern können $16^6=2^{24}=16\,777\,216$ verschiedene Werte haben. Ein Angreifer, der eine Fälschung an einer unwichtigen Stelle immer wieder abwandelt, trifft deshalb nach etwa 17 Millionen Versuchen eine Prüfsumme mit denselben sechs Anfangszeichen, für einen Rechner eine Sache von Sekundenbruchteilen bis Sekunden. Für alle 64 Zeichen bräuchte er etwa $16^{64}=2^{256}\approx1{,}16\cdot10^{77}$ Versuche; das ist mit keinem denkbaren Rechner zu schaffen. Ein Teilvergleich schützt also vor Zufallsfehlern, aber nicht vor Absicht.
:::
:::

:::aufgabe Aufgabe 17 ★ Passt das Abbild auf den Stick?
<span class="anker" id="aufg-17"></span>

Ein Abbild ist 6 482 409 472 Byte groß. Windows zeigt für drei Sticks die Größen 3,72 GB, 7,45 GB und 14,9 GB an. Auf welche Sticks passt das Abbild? Rechne die Größe des Abbilds dazu in dieselbe Einheit um, die Windows benutzt.

:::loesung
Das Abbild hat in der Einheit, die Windows benutzt,

$$\frac{6\,482\,409\,472\ \mathrm{Byte}}{1\,073\,741\,824\ \mathrm{Byte/GiB}}=6{,}04\ \mathrm{GiB}.$$

Es passt also nicht auf den Stick mit 3,72 (einen Stick mit der Aufschrift 4 GB), aber auf die Sticks mit 7,45 (8 GB) und 14,9 (16 GB). Wer stattdessen 6,48 aus der Herstellerangabe des Abbilds mit 7,45 aus der Anzeige von Windows vergleicht, kommt hier zum selben Ergebnis, vergleicht aber zwei verschiedene Einheiten; bei knappen Fällen führt das in die Irre.
:::
:::

:::aufgabe Aufgabe 18 ★★ Was hilft gegen den ausgetauschten Server?
<span class="anker" id="aufg-18"></span>

Im Beispiel mit dem Spiegelserver haben Abbild und `SHA256SUMS` denselben Fehler. Welche der folgenden Maßnahmen hätte die Fälschung aufgedeckt, welche nicht? (a) `sha256sum -c` statt Vergleich von Auge, (b) `SHA256SUMS` von [https://releases.ubuntu.com](https://releases.ubuntu.com), das Abbild vom Spiegelserver, (c) Abbild und Liste zweimal herunterladen, (d) die Signatur `SHA256SUMS.gpg` prüfen.

:::loesung
(a) Deckt die Fälschung nicht auf. `sha256sum -c` vergleicht nur genauer als das Auge; da Abbild und Liste zueinander passen, meldet es `OK`.

(b) Deckt sie auf. Die echte Liste von [https://releases.ubuntu.com](https://releases.ubuntu.com) enthält die Prüfsumme des echten Abbilds; das gefälschte Abbild hat eine andere, und der Vergleich meldet `FAILED` bzw. `False`. Voraussetzung ist, dass der offizielle Server selbst nicht verändert wurde.

(c) Deckt sie nicht auf. Der Spiegelserver liefert beide Male dieselbe gefälschte Datei und dieselbe gefälschte Liste.

(d) Deckt sie auf. Eine gültige Signatur über `SHA256SUMS` kann nur herstellen, wer den geheimen Schlüssel von Ubuntu besitzt; der Angreifer hat ihn nicht. Eine gefälschte Liste fällt bei der Prüfung der Signatur also auf, vorausgesetzt, man prüft mit dem echten Prüfschlüssel von Ubuntu.
:::
:::

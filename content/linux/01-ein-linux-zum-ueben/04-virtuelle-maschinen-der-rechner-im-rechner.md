---
title: Virtuelle Maschinen: der Rechner im Rechner
pfad: Informatik / Linux und Kommandozeile / Ein Linux zum Üben: WSL, virtuelle Maschine, Live-USB-Stick
adresse: informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick
knoten: Kapitel 1: Ein Linux zum Üben: WSL, virtuelle Maschine, Live-USB-Stick
order: 6060400
summary: Zwei der drei Wege beruhen auf derselben Idee: Ein Programm bildet einen ganzen Rechner nach, in dem ein zweites Betriebssystem läuft.
tags: virtuelle Maschine, Wirt, Gast, Hypervisor, Hardware-Virtualisierung, Snapshot, Adresse, NAT-Modus
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Zwei der drei Wege beruhen auf derselben Idee: Ein Programm bildet einen ganzen Rechner nach, in dem ein zweites Betriebssystem läuft. Dieser Abschnitt erklärt, wie das funktioniert, warum der Gast davon nichts merkt, wie man einen solchen Rechner in einem bestimmten Zustand festhält und wie er ins Internet kommt, ohne von dort erreichbar zu sein.
:::

### Die virtuelle Maschine

<span class="anker" id="stufe-3-1"></span>

Ein zweiter PC zum Ausprobieren wäre ideal: Man könnte darauf alles installieren, alles verstellen und im schlimmsten Fall neu anfangen, ohne dass der eigene Rechner etwas abbekommt. Einen solchen zweiten PC kann man auch in Software bauen.

Abbildung [5](#abb-5) zeigt die Idee. Auf dem echten Rechner läuft wie gewohnt Windows. Ein Programm stellt darin einen zweiten, nachgebildeten Rechner bereit, mit eigenem Prozessor, Arbeitsspeicher, eigener Festplatte und Netzwerkkarte. In diesem nachgebildeten Rechner läuft Linux, als säße es auf echter Hardware.

:::abbildung linux/k1vm 5
Eine virtuelle Maschine. Der Hypervisor, ein Programm auf dem Wirt, gibt dem Gast nachgebildete Hardware. Der Gast-Kernel steuert diese virtuelle Hardware, als wäre sie echt; seine Festplatte ist in Wahrheit eine Datei auf der SSD des Wirts.
:::

:::definition Definition 3.1 (Virtuelle Maschine)
<span class="anker" id="satz-3-1"></span>

Eine __virtuelle Maschine__ (VM) ist ein von Software nachgebildeter Rechner mit eigenem Prozessor, Arbeitsspeicher, eigenen Datenträgern und Netzwerkkarte. Auf ihr läuft ein vollständiges Betriebssystem mit eigenem Kernel, das sich verhält, als liefe es auf echter Hardware.
:::

::::beispiel Was eine VM von einem Laptop bekommt
Ein Laptop hat 8 Prozessorkerne, 16 GB Arbeitsspeicher und eine 512-GB-SSD. Eine VM für Ubuntu bekommt davon 2 Kerne, 6 GB Arbeitsspeicher und eine Festplatte von 25 GB. Für das Ubuntu in der VM gibt es nur diese 2 Kerne, diese 6 GB und diese 25 GB; den Rest des Laptops sieht es nicht. Die 25-GB-Festplatte der VM ist auf dem Laptop eine einzige Datei, die zu Beginn nur so groß ist wie die Daten, die tatsächlich darin stehen.
::::

⁠**Kurz gesagt:** Eine virtuelle Maschine ist ein Rechner aus Software, in dem ein ganzes Betriebssystem läuft.

### Wirt und Gast

<span class="anker" id="stufe-3-2"></span>

Sobald zwei Betriebssysteme auf einem Rechner laufen, braucht man Namen, um sie auseinanderzuhalten.

:::definition Definition 3.2 (Wirt, Gast)
<span class="anker" id="satz-3-2"></span>

Der __Wirt__ ist der echte Rechner mit dem Betriebssystem, unter dem die virtuelle Maschine läuft. Der __Gast__ ist das Betriebssystem, das in der virtuellen Maschine läuft.
:::

::::beispiel Ein Wirt, mehrere Gäste
Auf einem Laptop mit Windows 11 laufen zwei virtuelle Maschinen, eine mit Ubuntu 26.04 und eine mit Debian. Windows 11 ist der Wirt, Ubuntu und Debian sind zwei Gäste. Stürzt der Debian-Gast ab, laufen Windows und der Ubuntu-Gast weiter, denn jeder Gast hat seinen eigenen Kernel in seiner eigenen virtuellen Maschine.
::::

⁠**Kurz gesagt:** Der Wirt ist der echte Rechner, der Gast das System in der VM.

### Der Hypervisor

<span class="anker" id="stufe-3-3"></span>

Irgendein Programm muss die virtuelle Hardware bereitstellen, dem Gast einen Teil der echten Hardware zuteilen und aufpassen, dass er nicht mehr bekommt.

:::definition Definition 3.3 (Hypervisor)
<span class="anker" id="satz-3-3"></span>

Ein __Hypervisor__ ist die Software, die virtuelle Maschinen anlegt und betreibt. Er teilt ihnen Prozessorzeit, Arbeitsspeicher und Datenträger zu, bildet ihre Geräte nach und trennt sie voneinander und vom Wirt.
:::

::::beispiel [Beispiele] Vier Hypervisoren
Für Windows-Rechner kommen vor allem diese Hypervisoren in Frage: **VirtualBox** von Oracle, frei und kostenlos; **VMware Workstation Pro**, seit November 2024 für alle kostenlos; **Hyper-V** von Microsoft, das in Windows 10 und 11 in den Ausgaben Pro, Enterprise und Education enthalten ist, aber nicht in Windows Home; und **QEMU**, ein freier Hypervisor, der vor allem unter Linux benutzt wird. Dieses Kapitel richtet eine VM mit VirtualBox ein.
::::

⁠**Kurz gesagt:** Der Hypervisor baut die virtuellen Maschinen und wacht über sie.

:::hintergrund Zwei Bauarten von Hypervisoren
Ein Hypervisor wie VirtualBox ist ein gewöhnliches Programm, das unter Windows läuft und dessen Kernel für den Zugriff auf die Hardware benutzt. Man nennt ihn einen *Hypervisor vom Typ 2*. Ein *Hypervisor vom Typ 1* dagegen startet direkt auf der Hardware, noch vor jedem Betriebssystem, und alle Betriebssysteme laufen über ihm. Hyper-V ist ein solcher Typ-1-Hypervisor. Ist er eingeschaltet, läuft sogar Windows selbst nicht mehr direkt auf der Hardware, sondern in einem besonderen Bereich über dem Hypervisor, den Microsoft die Stammpartition (root partition) nennt; es hat dort aber als einziges System direkten Zugriff auf die Geräte. Das ist kein exotischer Fall. Der Hypervisor selbst, auf dem Hyper-V aufbaut, steckt auch in Windows Home; dort fehlen nur die Programme, mit denen man eigene VMs anlegt. Viele Windows-Rechner schalten diesen Hypervisor von Microsoft für Sicherheitsfunktionen und für WSL 2 ein, ohne dass man es merkt. Läuft er, benutzt VirtualBox ihn als Unterbau, statt selbst direkt auf die Hardware zuzugreifen.
:::

### Hardware-Virtualisierung

<span class="anker" id="stufe-3-4"></span>

Der Gast-Kernel ist ein gewöhnlicher Linux-Kernel. Er will im Kernel-Modus laufen und privilegierte Befehle ausführen, etwa um festzulegen, wohin ein Systemaufruf springt, oder um ein Gerät anzusprechen. Liefe er aber wirklich im Kernel-Modus des echten Prozessors, könnte er die ganze echte Maschine steuern, und der Hypervisor hätte nichts mehr zu sagen.

**Wie der Gast schnell und trotzdem eingesperrt läuft.** Der Ausweg ist derselbe wie beim Systemaufruf in Unterabschnitt [1.4](betriebssystem-kernel-und-distribution.html#stufe-1-4), nur eine Ebene tiefer. Der Gast-Kernel läuft direkt auf dem Prozessor, Befehl für Befehl, und deshalb fast so schnell wie auf echter Hardware. Der Prozessor führt ihn dabei aber in einer eigenen Betriebsart für Gäste aus. Einstellungen, die der Gast-Kernel darin vornimmt, gelten nur für seine VM. Sobald er etwas tun will, das die echte Maschine beträfe, etwa ein Gerät ansprechen, hält der Prozessor ihn an und übergibt die Kontrolle an den Hypervisor. Der Hypervisor schaut nach, was der Gast wollte, führt es an der virtuellen Hardware aus und lässt den Gast weiterlaufen. Der Gast merkt davon nichts.

:::definition Definition 3.4 (Hardware-Virtualisierung)
<span class="anker" id="satz-3-4"></span>

__Hardware-Virtualisierung__ ist eine Erweiterung des Prozessors, mit der ein Hypervisor Gast-Systeme direkt auf dem Prozessor ausführen lässt und selbst die Kontrolle bekommt, sobald ein Gast etwas tun will, das die echte Maschine beträfe. Bei Intel heißt sie VT-x (Virtualization Technology), bei AMD AMD-V. Alle heutigen PC-Prozessoren haben sie; bei manchen Rechnern ist sie aber ab Werk ausgeschaltet und muss in den Grundeinstellungen des Rechners eingeschaltet werden.
:::

::::beispiel Ob die Hardware-Virtualisierung eingeschaltet ist
Unter Windows öffnest du den Task-Manager (Strg+Umschalt+Esc), wählst links „Leistung“ und dann „CPU“. Unten rechts steht „Virtualisierung: Aktiviert“ oder „Deaktiviert“. Steht dort „Aktiviert“, sind beide Wege mit einer VM möglich. Einen zweiten Hinweis gibt der Befehl `systeminfo` in der PowerShell. Läuft auf dem Rechner schon ein Hypervisor von Microsoft, etwa weil WSL 2 eingerichtet ist, steht in seiner langen Ausgabe die Zeile „Anforderungen für Hyper-V: Es wurde ein Hypervisor erkannt.“ Dann ist die Hardware-Virtualisierung ohnehin eingeschaltet, denn ohne sie liefe kein Hypervisor.
::::

⁠**Kurz gesagt:** Mit Hardware-Virtualisierung läuft ein Gast-Kernel direkt auf dem Prozessor, aber alles, was die echte Maschine beträfe, landet beim Hypervisor.

:::hintergrund Warum PC-Prozessoren dafür eine Erweiterung brauchten
Ohne eine eigene Betriebsart für Gäste bleibt einem Hypervisor nur ein Weg: Er lässt den Gast-Kernel im Benutzermodus laufen und fängt dessen privilegierte Befehle ab. Dieses Verfahren „direkt ausführen, privilegierte Befehle abfangen“ funktioniert nur, wenn jeder Befehl, der den Zustand der Maschine verändern oder von ihm abhängen kann, im Benutzermodus tatsächlich abgefangen wird. Diese Bedingung haben Gerald Popek und Robert Goldberg 1974 genau formuliert. Die x86-Prozessoren der PCs erfüllten sie lange nicht: Rund siebzehn Befehle verhielten sich im Benutzermodus einfach anders, statt eine Unterbrechung auszulösen. Ein Beispiel ist der Befehl `POPF`, der unter anderem festlegt, ob Unterbrechungen von Geräten zugelassen sind; im Benutzermodus ignoriert er diesen Teil stillschweigend. Ein Gast-Kernel, der ihn benutzt, bekäme also eine falsche Antwort, und der Hypervisor erführe nichts davon. Frühe Hypervisoren mussten den Code des Gasts deshalb vor dem Ausführen umschreiben. Seit 2005 und 2006 bringen Intel und AMD einen eigenen Betriebsmodus für Gäste mit, in dem der Prozessor genau die nötigen Befehle an den Hypervisor weiterreicht.
:::

### Der Snapshot

<span class="anker" id="stufe-3-5"></span>

Der größte Vorteil einer VM für ein Labor ist, dass man Fehler rückgängig machen kann. Man hält den Zustand fest, bevor man etwas ausprobiert, und kehrt danach dorthin zurück, egal was man inzwischen angestellt hat.

Abbildung [6](#abb-6) zeigt, wie das bei der Festplatte der VM geht, ohne dass der Hypervisor die ganze Platte kopieren muss.

:::abbildung linux/k1snapshot 6
So hält ein Snapshot die Festplatte einer VM fest. Die bisherige Abbilddatei wird eingefroren; alle späteren Schreibzugriffe gehen in eine neue Datei, das Differenzabbild. Beim Lesen schaut der Hypervisor zuerst dort nach und sonst im Basisabbild. Wer zum Snapshot zurückkehrt, wirft das Differenzabbild weg.
:::

:::definition Definition 3.5 (Snapshot)
<span class="anker" id="satz-3-5"></span>

Ein __Snapshot__ ist ein gespeicherter Zustand einer virtuellen Maschine, zu dem man jederzeit zurückkehren kann. Er umfasst die Einstellungen der VM und den Inhalt aller ihrer virtuellen Festplatten; nimmt man ihn bei laufender VM auf, enthält er auch den Inhalt ihres Arbeitsspeichers.
:::

::::beispiel Ein Labor zurücksetzen
Nach der Installation von Ubuntu in der VM legst du einen Snapshot namens „sauber“ an. Danach probierst du Einstellungen aus, löschst versehentlich wichtige Systemdateien, und die VM startet nicht mehr. Du kehrst zum Snapshot „sauber“ zurück: Die VM ist genau so wie direkt nach der Installation. Auch eine Datei, die du nach dem Snapshot angelegt hast, ist dabei verschwunden, denn sie stand im verworfenen Differenzabbild.
::::

⁠**Kurz gesagt:** Ein Snapshot friert den Zustand einer VM ein, und das Zurückspielen verwirft alles, was danach kam.

:::hintergrund Warum ein Snapshot sofort fertig ist und kaum Platz braucht
Ein Snapshot kopiert nichts. Der Hypervisor erklärt nur die bisherige Abbilddatei für unveränderlich und legt eine leere neue Datei an, in die er ab jetzt jeden geschriebenen Block einträgt; das Verfahren heißt *copy on write*, kopieren erst beim Schreiben. Das Differenzabbild wächst also nur so stark, wie der Gast tatsächlich ändert. Mehrere Snapshots hintereinander ergeben eine Kette solcher Dateien. Löscht man einen Snapshot, ohne zu ihm zurückzukehren, muss der Hypervisor seine Änderungen in die Nachbardatei einrechnen; das kann bei großen Änderungen eine Weile dauern und vorübergehend viel Platz brauchen.
:::

### Das virtuelle Netz: NAT

<span class="anker" id="stufe-3-6"></span>

Eine VM soll ins Internet, etwa um Aktualisierungen zu laden. Andererseits soll niemand von außen an das Übungssystem herankommen, auf dem man vielleicht gerade etwas Unsicheres ausprobiert.

**Wie ein Router zu Hause.** Jedes Gerät in einem Netz hat eine Nummer, unter der andere es erreichen, seine __Adresse__. Zu Hause haben Laptop und Handy Adressen in einem kleinen privaten Netz, die im Internet nicht gelten. Der Router schickt ihre Anfragen unter seiner eigenen Adresse ins Internet, merkt sich, welches Gerät gefragt hat, und reicht die Antwort an dieses Gerät weiter. Eine Anfrage, die von außen kommt, ohne dass ein Gerät drinnen sie angestoßen hat, kann er niemandem zuordnen. Abbildung [7](#abb-7) zeigt, dass ein Hypervisor für seine VM genau diese Rolle spielen kann.

:::abbildung linux/k1nat 7
Der NAT-Modus. Die VM hat eine Adresse in einem kleinen Netz, das nur zwischen ihr und dem Hypervisor besteht. Der Hypervisor schickt ihre Verbindungen unter der Adresse des Wirts nach draußen und reicht die Antworten zurück. Eine Verbindung, die von außen beginnt, erreicht die VM nicht.
:::

:::definition Definition 3.6 (NAT-Modus)
<span class="anker" id="satz-3-6"></span>

Im __NAT-Modus__ (Network Address Translation, Übersetzen von Adressen) arbeitet der Hypervisor für die VM wie ein Router. Die VM hat eine eigene Adresse in einem privaten Netz, das nur zwischen ihr und dem Hypervisor besteht. Ihre Verbindungen schickt der Hypervisor unter der Adresse des Wirts weiter und reicht die Antworten an die VM zurück. Verbindungen, die von außen beginnen, erreichen die VM nicht, solange man keine Weiterleitung einrichtet.
:::

::::beispiel Was in NAT geht und was nicht
Eine Ubuntu-VM in VirtualBox läuft im NAT-Modus; das ist die Voreinstellung, und die VM bekommt dabei üblicherweise die Adresse 10.0.2.15. Aus der VM heraus kann man Webseiten öffnen und Aktualisierungen laden, denn die VM beginnt diese Verbindungen selbst. Ein Handy im selben WLAN kann einen Webserver in der VM dagegen nicht erreichen: Es kennt die Adresse 10.0.2.15 nicht, und selbst eine Anfrage an den Laptop würde der Hypervisor niemandem zuordnen können.
::::

⁠**Kurz gesagt:** Im NAT-Modus kommt die VM hinaus ins Netz, aber niemand von außen herein.

:::hintergrund Warum NAT von außen schützt, ohne dass man etwas einstellen muss
Der Schutz ist eine Nebenwirkung der Übersetzung. Damit der Hypervisor eine Antwort der richtigen VM zustellen kann, führt er eine Tabelle: Welche VM hat welche Verbindung zu welchem Ziel begonnen? Kommt ein Paket von außen, sucht er in dieser Tabelle. Hat keine VM die Verbindung begonnen, gibt es keinen Eintrag, und das Paket hat kein Ziel. VirtualBox kennt neben NAT weitere Netzbetriebsarten, in denen eine VM anders mit dem Wirt, mit anderen VMs oder mit dem Heimnetz verbunden ist; welche davon sich für ein abgeschottetes Übungslabor eignen, behandelt die Reihe Cybersecurity. Für ein erstes Übungs-Linux ist NAT die richtige Wahl.
:::

### Aufgaben zu Abschnitt [3](#stufe-3)

<span class="anker" id="stufe-3-7"></span>

:::aufgabe Aufgabe 7 ★ Steckbrief deines Rechners
<span class="anker" id="aufg-7"></span>

Sammle unter Windows vier Angaben über deinen Rechner. Du veränderst dabei nichts.

<ol class="al">

<li>

Ausgabe und Version von Windows: Einstellungen $\to$ System $\to$ Info, Abschnitt „Windows-Spezifikationen“.

</li>

<li>

Den eingebauten Arbeitsspeicher: an derselben Stelle unter „Gerätespezifikationen“.

</li>

<li>

Den freien Platz auf Laufwerk C: im Explorer unter „Dieser PC“.

</li>

<li>

Ob die Hardware-Virtualisierung eingeschaltet ist, wie im Beispiel in Unterabschnitt [3.4](#stufe-3-4).

</li>

</ol>

Ubuntu 26.04 braucht in einer VM mindestens 6 GB Arbeitsspeicher und 25 GB Platz. Reicht dein Rechner dafür, wenn Windows daneben noch mindestens 8 GB behalten soll? Steht dir Hyper-V zur Verfügung?

:::loesung
Die Angaben hängen von deinem Rechner ab. So wertest du sie aus:

<ul>

<li>

⁠**Arbeitsspeicher.** Die VM braucht 6 GB, Windows soll 8 GB behalten, zusammen also 14 GB. Mit 16 GB reicht es, mit 8 GB nicht; dann ist WSL 2 der bessere Weg.

</li>

<li>

⁠**Platz auf C:.** Die VM braucht 25 GB, das Abbild noch einmal 6,5 GB. Mit weniger als etwa 35 GB frei wird es eng.

</li>

<li>

⁠**Virtualisierung.** Steht im Task-Manager „Aktiviert“, ist alles bereit. Steht dort „Deaktiviert“, muss die Einstellung in der Firmware eingeschaltet werden; das zeigt Abschnitt [7](eine-virtuelle-maschine-mit-virtualbox.html#stufe-7).

</li>

<li>

⁠**Hyper-V.** Steht unter „Windows-Spezifikationen“ eine Pro-, Enterprise- oder Education-Ausgabe, kannst du Hyper-V benutzen; mit Windows Home nicht. VirtualBox und WSL 2 laufen auf allen Ausgaben.

</li>

</ul>

Zum Vergleich der Testrechner dieses Kapitels: Windows 11 Home, 63,5 GB Arbeitsspeicher. Arbeitsspeicher und Platz reichen reichlich; Hyper-V als eigene Funktion gibt es auf Home nicht. Trotzdem läuft auf diesem Rechner der Hypervisor von Microsoft: `systeminfo` meldet „Es wurde ein Hypervisor erkannt“, weil eine Sicherheitsfunktion von Windows und WSL 2 ihn benutzen.
:::
:::

:::aufgabe Aufgabe 8 ★★ Was der Gast-Kernel darf
<span class="anker" id="aufg-8"></span>

Ein Gast-Kernel will (a) eine Zahl im Arbeitsspeicher seiner VM verdoppeln, (b) festlegen, an welche Stelle seines Kernels ein Systemaufruf springt, (c) einen Block auf seine Festplatte schreiben. Wer erledigt jeweils die Arbeit, der Prozessor direkt oder der Hypervisor, und für wen gilt das Ergebnis? Warum wäre es gefährlich, wenn der Gast-Kernel (b) im echten Kernel-Modus selbst ausführen dürfte?

:::loesung
(a) Der Prozessor direkt. Eine Zahl im Arbeitsspeicher der VM zu verdoppeln, ist ein gewöhnlicher Rechenbefehl auf Speicher, den der Hypervisor der VM ohnehin zugeteilt hat. Er läuft ohne Umweg, und deshalb ist die VM fast so schnell wie echte Hardware.

(b) Die Einstellung gilt nur für den Gast. In der Betriebsart für Gäste führt der Prozessor für jeden Gast einen eigenen Satz solcher Einstellungen; je nach Prozessor und Hypervisor nimmt er die Einstellung dort direkt vor, oder er hält den Gast an und übergibt an den Hypervisor, der sie für den Gast verwaltet. In beiden Fällen landen Systemaufrufe der Programme im Gast beim Gast-Kernel, und die Einstellung des Wirts bleibt unberührt.

(c) Der Hypervisor. Ein Schreibzugriff auf ein Gerät ist privilegiert. Der Hypervisor fängt ihn ab und schreibt den Block in die Abbilddatei der virtuellen Festplatte; als Typ-2-Hypervisor benutzt er dafür einen Systemaufruf des Wirts.

Dürfte der Gast-Kernel (b) im echten Kernel-Modus ausführen, würde er die Einsprungstelle des echten Prozessors überschreiben. Dann landeten Systemaufrufe aller Programme, auch der Programme des Wirts, in seinem Code, und er hätte die ganze Maschine in der Hand. Genau das verhindert die Hardware-Virtualisierung.
:::
:::

:::aufgabe Aufgabe 9 ★★ Snapshots nachverfolgen
<span class="anker" id="aufg-9"></span>

Eine VM durchläuft nacheinander: Ubuntu installieren; Snapshot „A“; Datei `x.txt` anlegen; Snapshot „B“; Datei `y.txt` anlegen; `x.txt` löschen; zurück zu „B“; Datei `z.txt` anlegen; zurück zu „A“. Welche der drei Dateien gibt es am Ende? Wie viele Differenzabbilder hat der Hypervisor unterwegs angelegt, und welche hat er verworfen?

:::loesung
Am Ende gibt es keine der drei Dateien. Der Weg dahin, mit dem Modell aus Abbildung [6](#abb-6): Ein Snapshot friert das aktuelle Abbild ein und legt ein neues Differenzabbild an; Zurückspielen verwirft das aktuelle Differenzabbild und legt über dem Stand des Snapshots ein neues, leeres an.

<ol>

<li>

Snapshot „A“: Das Basisabbild mit dem frisch installierten Ubuntu wird eingefroren, Differenzabbild 1 entsteht.

</li>

<li>

`x.txt` wird in Differenzabbild 1 geschrieben.

</li>

<li>

Snapshot „B“: Differenzabbild 1 wird eingefroren und gehört ab jetzt zu „B“; Differenzabbild 2 entsteht.

</li>

<li>

`y.txt` anlegen und `x.txt` löschen: beides in Differenzabbild 2.

</li>

<li>

Zurück zu „B“: Differenzabbild 2 wird verworfen, Differenzabbild 3 entsteht über dem Stand von „B“. Jetzt gibt es `x.txt` wieder, `y.txt` nicht.

</li>

<li>

`z.txt` wird in Differenzabbild 3 geschrieben.

</li>

<li>

Zurück zu „A“: Differenzabbild 3 wird verworfen, Differenzabbild 4 entsteht direkt über dem Basisabbild. Der Stand ist der direkt nach der Installation: keine der drei Dateien.

</li>

</ol>

Angelegt wurden also vier Differenzabbilder, verworfen zwei (Nummer 2 und 3). Nummer 1 bleibt erhalten, weil der Snapshot „B“ weiter besteht; man könnte jederzeit zu ihm zurück und fände dort `x.txt`.
:::
:::

:::aufgabe Aufgabe 10 ★ Was erreicht eine VM im NAT-Modus?
<span class="anker" id="aufg-10"></span>

Eine VM läuft in VirtualBox im NAT-Modus. Funktioniert es, und warum (nicht)? (a) Die VM lädt Aktualisierungen aus dem Internet. (b) Ein Laptop im selben WLAN ruft eine Webseite auf, die ein Programm in der VM anbietet. (c) Die VM öffnet eine Webseite, die ein Programm auf dem Handy im selben WLAN anbietet.

:::loesung
(a) Funktioniert. Die VM beginnt die Verbindung selbst; der Hypervisor schickt sie unter der Adresse des Wirts weiter, merkt sich die Verbindung und reicht die Antworten zurück.

(b) Funktioniert nicht. Die Verbindung beginnt außen. Der andere Laptop kennt die Adresse der VM nicht, und selbst eine Anfrage an den Wirt könnte der Hypervisor keiner VM zuordnen, weil keine sie angestoßen hat. Erst eine eingerichtete Weiterleitung würde das ändern.

(c) Funktioniert. Auch hier beginnt die VM die Verbindung; für das Handy sieht es aus, als frage der Laptop. Ob das Ziel im Internet oder im eigenen WLAN steht, spielt keine Rolle.
:::
:::

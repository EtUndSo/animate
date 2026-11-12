---
title: Schutzgrenzen und der Referenzmonitor
pfad: Informatik / Cybersecurity / Schutzgrenzen in Hardware und Betriebssystem
adresse: informatik/cybersecurity/schutzgrenzen-in-hardware-und-betriebssystem
knoten: Kapitel 2: Schutzgrenzen in Hardware und Betriebssystem
order: 6120200
summary: Bevor einzelne Mechanismen an die Reihe kommen, braucht man einen Maßstab: Was ist eine Schutzgrenze, und woran erkennt man, ob sie hält?
tags: Schutzgrenze, Referenzmonitor
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Bevor einzelne Mechanismen an die Reihe kommen, braucht man einen Maßstab: Was ist eine Schutzgrenze, und woran erkennt man, ob sie hält? Dieser Abschnitt legt beides fest und wendet den Maßstab auf den Kernel an. Dabei zeigt sich, dass der Kernel allein nicht schützen kann.
:::

:::::vorwissen Was du dafür brauchst: Kernel, Systemaufruf und Prozess

<span class="anker" id="stufe-1-1"></span>

Dieses Kapitel setzt [Kapitel 1](/wissen/informatik/cybersecurity/sicherheit-schutzziele-und-spielregeln/sicherheit-schutzziele-und-spielregeln.html) und die [Kapitel 1](/wissen/informatik/cybersecurity/sicherheit-schutzziele-und-spielregeln/sicherheit-schutzziele-und-spielregeln.html) bis 8 des Bereichs „Linux und Kommandozeile“ voraus. Daraus brauchst du vor allem diese Dinge.

<ul>

<li>

Das Betriebssystem verwaltet die Hardware, stellt sie den Programmen über einheitliche Dienste bereit und schirmt die Programme voneinander ab ([Linux, Kapitel 1, Abschnitt 1.1](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/betriebssystem-kernel-und-distribution.html#stufe-1-1)).

</li>

<li>

Ein Prozessor kennt mindestens zwei Betriebsarten. Im Kernel-Modus ist jeder Befehl erlaubt, im Benutzermodus sind die privilegierten Befehle gesperrt, etwa der direkte Zugriff auf Geräte. Versucht ein Programm im Benutzermodus einen privilegierten Befehl, führt der Prozessor ihn nicht aus und übergibt die Kontrolle an das Betriebssystem ([Linux, Kapitel 1, Abschnitt 1.2](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/betriebssystem-kernel-und-distribution.html#stufe-1-2)).

</li>

<li>

Der Kernel ist der Teil des Betriebssystems, der im Kernel-Modus läuft; alle anderen Programme laufen im Benutzermodus ([Linux, Kapitel 1, Abschnitt 1.3](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/betriebssystem-kernel-und-distribution.html#stufe-1-3)).

</li>

<li>

Mit einem Systemaufruf bittet ein Programm den Kernel um einen Dienst: Es legt die Nummer des Dienstes und die Angaben dazu bereit und führt einen besonderen Prozessorbefehl aus. Der Prozessor wechselt in den Kernel-Modus und springt an eine Stelle, die der Kernel beim Start festgelegt hat. Das Werkzeug `strace` schreibt die Systemaufrufe eines Programms mit ([Linux, Kapitel 1, Abschnitt 1.4](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/betriebssystem-kernel-und-distribution.html#stufe-1-4)).

</li>

<li>

Ein Prozess ist ein Programm in Ausführung mit eigenem Speicher, geöffneten Dateien und einem Benutzer; der Kernel gibt jedem eine Prozessnummer. Unter `/proc/self` zeigt er Angaben über den Prozess, der gerade nachschaut ([Linux, Kapitel 4, Abschnitt 1.2](/wissen/informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status/prozesse-und-ihre-drei-strome.html#stufe-1-2); [Linux, Kapitel 8, Abschnitt 1.2](/wissen/informatik/linux-und-kommandozeile/prozesse-signale-und-dienste/prozesse-und-ihre-verwandtschaft.html#stufe-1-2); [Linux, Kapitel 3, Abschnitt 7.8](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/die-verzeichnisstruktur-von-linux.html#stufe-7-8)).

</li>

<li>

Ob ein Prozess eine Datei lesen darf, prüft der Kernel beim Öffnen anhand der Rechte der Datei; danach gilt der Dateideskriptor ([Linux, Kapitel 7, Abschnitt 5.3](/wissen/informatik/linux-und-kommandozeile/benutzer-gruppen-und-rechte/wie-der-kernel-rechte-pruft.html#stufe-5-3)). root, das Konto mit der Benutzernummer 0, überspringt diese Prüfung fast ganz ([Linux, Kapitel 7, Abschnitt 1.7](/wissen/informatik/linux-und-kommandozeile/benutzer-gruppen-und-rechte/benutzer-und-gruppen.html#stufe-1-7)).

</li>

</ul>

⁠**Kurz gesagt:** Programme laufen im Benutzermodus und bekommen alles, was sie nicht selbst dürfen, über Systemaufrufe vom Kernel, der dabei die Rechte prüft.

:::warnung Nur am eigenen Rechner, nur lesen und eigene kleine Programme
Die Versuche in diesem Kapitel lesen Angaben des eigenen Systems und starten zwei kleine, harmlose Programme, die du selbst anlegst. Nichts davon greift ein anderes System an, nichts verändert dein Windows oder deine Firmware. Es gelten die Spielregeln aus [Kapitel 1, Abschnitt 10.7](/wissen/informatik/cybersecurity/sicherheit-schutzziele-und-spielregeln/offenlegung-und-ethik.html#stufe-10-7): nur eigene Systeme, Lernplattformen innerhalb ihrer Regeln oder isolierte Labore. Wer ohne Erlaubnis auf fremden Rechnern Zugangssicherungen überwindet, Daten abfängt, verändert oder Systeme stört, kann sich nach den §§ 202a, 202b, 303a und 303b StGB strafbar machen, schon das Vorbereiten nach § 202c ([Kapitel 1, Abschnitt 8](/wissen/informatik/cybersecurity/sicherheit-schutzziele-und-spielregeln/computerstrafrecht-was-verboten-ist.html#stufe-8)); das Kapitel ist keine Rechtsberatung. Lege für die Versuche in WSL 2 oder in deiner Übungs-VM ein eigenes Verzeichnis an und arbeite nur darin:

```console
$ mkdir ~/cyberk2
$ cd ~/cyberk2
```

Einstellungen der Firmware, Secure Boot und die Verschlüsselung von Windows liest dieses Kapitel nur aus. Ändere dort nichts.
:::

:::::

:::::vorwissen Was du dafür brauchst: lückenlose Prüfung und vertrauenswürdige Basis

<span class="anker" id="stufe-1-2"></span>

Zwei Sicherheitsprinzipien aus [Kapitel 1](/wissen/informatik/cybersecurity/sicherheit-schutzziele-und-spielregeln/sicherheit-schutzziele-und-spielregeln.html) tragen dieses ganze Kapitel.

<ul>

<li>

Nach dem Prinzip der *lückenlosen Prüfung* wird jeder Zugriff auf jedes Schutzgut darauf geprüft, ob er erlaubt ist, und zwar bei jedem Zugriff aufs Neue. Im Bild aus [Kapitel 1](/wissen/informatik/cybersecurity/sicherheit-schutzziele-und-spielregeln/sicherheit-schutzziele-und-spielregeln.html) prüft im Hotel nicht nur der Haupteingang die Schlüsselkarte, sondern jede Zimmertür ([Kapitel 1, Abschnitt 5.5](/wissen/informatik/cybersecurity/sicherheit-schutzziele-und-spielregeln/sicherheitsprinzipien-rechte-vergeben-und-prufen.html#stufe-5-5)).

</li>

<li>

Die *vertrauenswürdige Basis* eines Systems besteht aus allen Teilen, auf deren korrektes Funktionieren die Sicherheit angewiesen ist. Ein einziger Fehler darin kann die ganze Sicherheit aufheben; deshalb hält man sie so klein wie möglich ([Kapitel 1, Abschnitt 6.3](/wissen/informatik/cybersecurity/sicherheit-schutzziele-und-spielregeln/sicherheitsprinzipien-systeme-robust-entwerfen.html#stufe-6-3)).

</li>

</ul>

⁠**Kurz gesagt:** Jeder Zugriff wird geprüft, und auf die Teile, die prüfen, muss man sich verlassen können.

:::::

### Die Schutzgrenze

<span class="anker" id="stufe-1-3"></span>

In einem Mietshaus hat jede Wohnung ihre eigene Tür. Die Mieter dürfen in ihre eigene Wohnung und ins Treppenhaus, aber nicht in die Wohnung nebenan und nicht in den Heizungskeller. Die Grenzen verlaufen entlang der Wände; wer hinüber will, muss durch eine Tür, und an der Tür entscheidet ein Schloss.

Auf einem Rechner gibt es solche Grenzen ebenfalls, nur sind die Wände unsichtbar. Ein Programm darf seine eigenen Daten lesen, aber nicht die eines anderen Programms; es darf eine Datei lesen, wenn die Rechte es erlauben, aber nicht den Datenträger direkt ansprechen.

:::definition Definition 1.1 (Schutzgrenze)
<span class="anker" id="satz-1-1"></span>

Eine __Schutzgrenze__ ist eine Trennlinie zwischen zwei Bereichen, in denen unterschiedliche Rechte gelten. Ein Zugriff von einem Bereich in den anderen ist nur über eine Stelle möglich, die ihn prüft und gegebenenfalls ablehnt.
:::

Der Begriff ist eine Arbeitsdefinition für dieses Kapitel; er fasst zusammen, was die folgenden Abschnitte im Einzelnen untersuchen. Abbildung [1](#abb-1) zeigt die Bestandteile.

:::abbildung cyber/k2grenze 1
Zwei Bereiche nebeneinander, links „Programm, wenig Rechte“, rechts „Kernel und Geräte, alle Rechte“, dazwischen eine dicke Linie. In der Linie gibt es genau eine Tür mit einer Prüfstelle (Häkchen und Kreuz). Ein Pfeil vom Programm geht durch die Tür und wird geprüft (Häkchen), ein zweiter Pfeil versucht, die Linie an anderer Stelle zu überqueren, und prallt ab.
:::

::::beispiel Eine fremde Datei lesen
Die Benutzerin `student` startet `cat /etc/shadow`. Die Datei gehört root, und nur root und die Gruppe `shadow` dürfen sie lesen ([Linux, Kapitel 7, Abschnitt 1.8](/wissen/informatik/linux-und-kommandozeile/benutzer-gruppen-und-rechte/benutzer-und-gruppen.html#stufe-1-8)). Das Programm `cat` läuft im Benutzermodus und kann die Datei nicht selbst vom Datenträger holen. Es muss den Kernel per Systemaufruf bitten, sie zu öffnen. Der Kernel prüft die Rechte und lehnt ab:

```console
$ cat /etc/shadow
cat: /etc/shadow: Permission denied
$ echo $?
1
```

Hier liegt die Grenze zwischen dem Programm und dem Kernel. Die prüfende Stelle ist der Systemaufruf zum Öffnen der Datei, und der Kernel prüft dort. Abbildung [2](#abb-2) zeigt den Weg der Anfrage.

:::abbildung cyber/k2shadow 2
Oben ein Terminal: `cat /etc/shadow` wird getippt. Darunter wandert die Anfrage des Programms `cat` (Benutzerin `student`) als Pfeil „öffnen“ zur Grenze und durch die Tür in den Kernel. Dort erscheinen die Rechte der Datei `-rw-r----- root shadow`; die Prüfung markiert „student: nicht Besitzer, nicht in der Gruppe shadow, also gelten die letzten drei Zeichen `---`“ und zeigt ein rotes Kreuz. Der Pfeil kehrt mit „abgelehnt“ zurück, und im Terminal erscheinen `cat: /etc/shadow: Permission denied` und nach `echo $?` die Zahl 1.
:::
::::

⁠**Kurz gesagt:** Eine Schutzgrenze trennt zwei Bereiche mit verschiedenen Rechten, und über sie hinweg kommt man nur durch eine prüfende Stelle.

### Der Referenzmonitor

<span class="anker" id="stufe-1-4"></span>

Eine Grenze ist nur so gut wie die Stelle, die an ihr prüft. Ein Pförtner am Haupteingang eines Bürogebäudes nützt nichts, wenn die Tür zur Tiefgarage offen steht, wenn ein Besucher ihn einfach gegen einen eigenen Pförtner austauschen kann oder wenn seine Vorschriften so verworren sind, dass niemand sagen kann, wen er hereinlassen wird. Das ist ein Bild zur Orientierung; die genaue Fassung ist die folgende.

:::definition Definition 1.2 (Referenzmonitor)
<span class="anker" id="satz-1-2"></span>

Ein __Referenzmonitor__ ist der Teil eines Systems, der jeden Zugriff eines Handelnden (eines Prozesses, eines Benutzers) auf ein Schutzgut gegen die Sicherheitsrichtlinie prüft. Er muss drei Forderungen erfüllen:

<ol>

<li>

Er wird *immer aufgerufen*: Es gibt keinen Weg zum Schutzgut an ihm vorbei.

</li>

<li>

Er ist *manipulationssicher*: Niemand, den er prüft, kann ihn verändern oder austauschen.

</li>

<li>

Er ist *klein und einfach genug*, um seine Korrektheit vollständig zu prüfen.

</li>

</ol>
:::

[Kapitel 1](/wissen/informatik/cybersecurity/sicherheit-schutzziele-und-spielregeln/sicherheit-schutzziele-und-spielregeln.html) hat den Referenzmonitor nur im Hintergrund zur vertrauenswürdigen Basis genannt. Hier wird er zum Maßstab für jede Grenze des Kapitels. Die erste Forderung ist die lückenlose Prüfung, die dritte der Grund für eine kleine vertrauenswürdige Basis (Unterabschnitt [1.2](#stufe-1-2)). Abbildung [3](#abb-3) stellt die drei Forderungen als Schilder an einer Tür dar.

:::abbildung cyber/k2monitor 3
Eine Tür mit Prüfstelle zwischen „Handelnde“ links und „Schutzgüter“ rechts. Nacheinander erscheinen drei Schilder: „1 immer aufgerufen: kein Weg daran vorbei“ (eine Hintertür wird zugemauert), „2 manipulationssicher: niemand tauscht den Prüfer aus“ (ein Versuch, die Prüfstelle zu ersetzen, prallt ab), „3 klein genug zum Prüfen“ (ein kurzer Regelzettel statt eines dicken Ordners).
:::

::::beispiel Der Kartenleser an der Hoteltür
Ein Hotel lässt jede Zimmertür durch einen Kartenleser prüfen. Erfüllt er die drei Forderungen?

<ol>

<li>

Immer aufgerufen: Nur, wenn es keinen anderen Weg ins Zimmer gibt. Eine Verbindungstür zum Nachbarzimmer, die sich ohne Karte öffnen lässt, verletzt die erste Forderung.

</li>

<li>

Manipulationssicher: Der Leser ist fest in die Tür eingebaut, und nur das Hotel kann ihn programmieren. Ließe sich die Zimmerliste mit einer selbst gebastelten Karte überschreiben, wäre die zweite Forderung verletzt.

</li>

<li>

Klein genug: Der Leser vergleicht nur die Nummer auf der Karte mit der Nummer des Zimmers und das Ablaufdatum mit der Uhrzeit. Das lässt sich vollständig prüfen. Ein Leser mit Dutzenden Sonderregeln für Stammgäste, Reinigung, Handwerker und Feiertage wäre es nicht mehr.

</li>

</ol>
::::

⁠**Kurz gesagt:** Ein Referenzmonitor prüft jeden Zugriff, und er taugt nur, wenn niemand an ihm vorbeikommt, niemand ihn verändern kann und man ihn vollständig prüfen kann.

:::hintergrund Warum es genau diese drei Forderungen sind
Wer an einer Prüfung vorbei will, hat drei grundsätzlich verschiedene Möglichkeiten. Er kann sie *umgehen*, also einen Weg nehmen, auf dem gar nicht geprüft wird. Er kann sie *verändern*, also dafür sorgen, dass die Prüfung anders entscheidet als vorgesehen. Oder er kann einen *Fehler* in ihr finden, eine Lage, in der die Prüfung aus Versehen etwas Verbotenes zulässt. Jede der drei Forderungen schließt genau eine dieser Möglichkeiten: „immer aufgerufen“ das Umgehen, „manipulationssicher“ das Verändern, „klein genug“ die Fehler, soweit Menschen sie durch sorgfältiges Prüfen finden können. Mehr Möglichkeiten gibt es nicht: Entweder findet die Prüfung gar nicht statt, oder sie entscheidet anders als gebaut, oder sie ist schon falsch gebaut. Die Forderungen stammen aus einer Studie für die US-Luftwaffe von 1972 und gelten seither als Maßstab für jede Stelle, die über Zugriffe entscheidet.
:::

### Der Kernel als Referenzmonitor

<span class="anker" id="stufe-1-5"></span>

Im Beispiel mit `/etc/shadow` hat der Kernel als Referenzmonitor gearbeitet: Er hat den Zugriff gegen die Rechte der Datei geprüft. Damit er diese Rolle wirklich ausfüllt, müssen die drei Forderungen für ihn gelten. Keine davon kann der Kernel allein sicherstellen.

<ol>

<li>

⁠*Immer aufgerufen:* Ein Programm darf nicht an ihm vorbei an die Datenträger, an die Geräte oder an den Speicher anderer Programme kommen. Einen direkten Zugriff kann nur der Prozessor verhindern, denn während das Programm auf einem Kern rechnet, läuft dort nicht der Kernel.

</li>

<li>

⁠*Manipulationssicher:* Ein Programm darf den Code und die Tabellen des Kernels nicht verändern, auch nicht, indem es vor ihm startet. Auch das muss die Hardware durchsetzen, und für die Zeit vor dem Kernel die Startkette.

</li>

<li>

⁠*Klein genug:* Zur vertrauenswürdigen Basis gehören der Kernel, der Prozessor und alles, was vor dem Kernel läuft. Jeder Fehler darin kann alle Grenzen aufheben.

</li>

</ol>

Für jede Grenze dieses Kapitels stellt man deshalb dieselben vier Fragen.

:::satz Satz 1.3 (Vier Fragen an jede Schutzgrenze)
<span class="anker" id="satz-1-3"></span>

<ol>

<li>

Welche Bereiche trennt die Grenze, und wer steht auf welcher Seite?

</li>

<li>

Wer erzwingt sie, und an welcher Stelle wird geprüft?

</li>

<li>

Womit wird sie erzwungen, und wer darf dieses Mittel einstellen?

</li>

<li>

Was hält sie nicht auf?

</li>

</ol>
:::

Abbildung [4](#abb-4) zeigt, wie die Grenzen aufeinander aufbauen.

:::abbildung cyber/k2schichten 4
Vier Schichten übereinander, unten beginnend: „Startkette (Firmware, Bootloader)“, „Prozessor“, „Kernel“, „Programme“. Ein Pfeil von jeder Schicht zur nächsten höheren trägt die Aufschrift „richtet ein und schützt“. Rechts daneben eine Klammer über Startkette, Prozessor und Kernel: „vertrauenswürdige Basis“. Ganz oben ein Programm, das zum Kernel zeigt: „wird geprüft“.
:::

::::beispiel Die vier Fragen für das Lesen von `/etc/shadow`
<ol>

<li>

Getrennt sind das Programm `cat` der Benutzerin `student` und die Datei, die nur root lesen darf.

</li>

<li>

Der Kernel erzwingt die Grenze, beim Systemaufruf zum Öffnen der Datei.

</li>

<li>

Er prüft mit den Rechten der Datei; ändern darf sie nur ihr Besitzer oder root.

</li>

<li>

Die Grenze hält kein Programm auf, das mit den Rechten von root läuft, und keinen Fehler im Kernel selbst.

</li>

</ol>
::::

⁠**Kurz gesagt:** Der Kernel prüft Zugriffe wie ein Referenzmonitor, aber dass niemand an ihm vorbeikommt und niemand ihn verändert, muss die Hardware sicherstellen.

### Aufgaben zu Abschnitt [1](#stufe-1)

<span class="anker" id="stufe-1-6"></span>

:::aufgabe Aufgabe 1 ★ Welche Forderung ist verletzt?
<span class="anker" id="aufg-1"></span>

Bestimme in jedem Fall, welche der drei Forderungen an einen Referenzmonitor verletzt ist, und begründe kurz.

<ol class="al">

<li>

Eine Bibliothek kontrolliert am Eingang den Ausweis. Die Tür zur Lieferrampe auf der Rückseite steht tagsüber offen.

</li>

<li>

Im Fitnessstudio kann jeder Kunde mit einem Generalcode, der auf der Rückseite jedes Schließfachs klebt, das Zahlenschloss eines beliebigen Fachs neu einstellen.

</li>

<li>

Eine Firma lässt Zugriffe auf ihre Kundendatenbank von einem Programm aus 400 000 Zeilen prüfen, das zwölf Abteilungen über Jahre erweitert haben und das niemand mehr ganz überblickt.

</li>

<li>

Eine Banking-App prüft die PIN nur in der App auf dem Handy. Der Server der Bank führt jeden Auftrag aus, der bei ihm ankommt.

</li>

</ol>

:::loesung
(a) Verletzt ist „immer aufgerufen“. Die Ausweiskontrolle prüft nur den Haupteingang; über die offene Lieferrampe kommt man an ihr vorbei ins Gebäude. Eine Prüfung, die man umgehen kann, ist für den Umgehenden keine.

(b) Verletzt ist „manipulationssicher“. Jeder Kunde kann mit dem Generalcode das Schloss eines fremden Fachs neu einstellen, also den Prüfer selbst verändern, statt ihn zu umgehen. Danach lässt das Schloss genau den herein, der es verstellt hat.

(c) Verletzt ist „klein und einfach genug“. Ein Programm aus 400 000 Zeilen, das niemand überblickt, kann man nicht vollständig prüfen. Irgendwo darin steckt mit hoher Wahrscheinlichkeit ein Fall, in dem es etwas Verbotenes zulässt, und niemand weiß, wo.

(d) Verletzt ist vor allem „immer aufgerufen“: Das Schutzgut ist das Konto auf dem Server, und an dessen Tür wird nicht geprüft. Wer Aufträge direkt an den Server schickt, ohne die App zu benutzen, kommt an der PIN-Prüfung vorbei. Zusätzlich ist „manipulationssicher“ verletzt, denn die App läuft auf dem Gerät des Benutzers, und ein Angreifer mit diesem Gerät kann sie verändern. Prüfungen gehören auf die Seite der Grenze, auf der das Schutzgut liegt.
:::
:::

:::aufgabe Aufgabe 2 ★★ Die vier Fragen am eigenen Rechner
<span class="anker" id="aufg-2"></span>

Führe in deinem Übungsverzeichnis `cat /etc/shadow` und danach `ls -l /etc/shadow` aus. Beantworte für den Versuch, die Datei zu lesen, die vier Fragen an eine Schutzgrenze. Was müsste ein Angreifer, der nur das Konto `student` kontrolliert, erreichen, um die Datei trotzdem zu lesen? Nenne zwei grundsätzlich verschiedene Wege, ohne auszuführen, wie man sie geht.

:::loesung
Die beiden Befehle liefern auf dem Testsystem:

```console
$ cat /etc/shadow
cat: /etc/shadow: Permission denied
$ ls -l /etc/shadow
-rw-r----- 1 root shadow 731 Nov 10 14:33 /etc/shadow
```

<ol>

<li>

Getrennt sind der Prozess `cat` der Benutzerin `student` (Benutzernummer 1000, Gruppen `student` und `sudo`) und die Datei `/etc/shadow`, die root gehört.

</li>

<li>

Der Kernel erzwingt die Grenze, beim Systemaufruf, der die Datei öffnet.

</li>

<li>

Er prüft mit den Rechten der Datei: Besitzer root darf lesen und schreiben, die Gruppe `shadow` lesen, alle anderen nichts. `student` ist weder Besitzer noch in der Gruppe `shadow`, also gelten die letzten drei Zeichen `---`. Ändern dürfen die Rechte nur der Besitzer root und Prozesse mit den Rechten von root.

</li>

<li>

Die Grenze hält nichts auf, was mit den Rechten von root läuft, und keinen Fehler im Kernel.

</li>

</ol>

Ein Angreifer, der das Konto `student` kontrolliert, hat zwei grundsätzlich verschiedene Wege. Erstens kann er die Richtlinie selbst benutzen: `student` ist in der Gruppe `sudo`; wer zusätzlich das Passwort kennt, darf nach den Regeln des Systems `sudo cat /etc/shadow` ausführen. Das ist keine Lücke der Grenze, sondern eine Frage der Rechtevergabe. Zweitens kann er versuchen, den Prüfer zu umgehen, statt ihn zu überzeugen: etwa einen Fehler im Kernel ausnutzen oder den Rechner von einem anderen Datenträger starten und die Datei lesen, während dieser Kernel gar nicht läuft. Gegen den zweiten Weg hilft keine Rechteeinstellung; dagegen braucht es Schutz, der vor dem Kernel ansetzt.
:::
:::

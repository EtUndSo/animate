---
title: Betriebssystem, Kernel und Distribution
pfad: Informatik / Linux und Kommandozeile / Ein Linux zum Üben: WSL, virtuelle Maschine, Live-USB-Stick
adresse: informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick
knoten: Kapitel 1: Ein Linux zum Üben: WSL, virtuelle Maschine, Live-USB-Stick
order: 6060200
summary: Bevor man ein Linux einrichtet, muss man wissen, was man da eigentlich einrichtet.
tags: Betriebssystem, Anwendungsprogramm, Kernel-Modus, Benutzermodus, privilegierter Befehl, Kernel, Treiber, Systemaufruf
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Bevor man ein Linux einrichtet, muss man wissen, was man da eigentlich einrichtet. Dieser Abschnitt klärt, was ein Betriebssystem tut, welcher Teil davon die Hardware wirklich steuert, wie gewöhnliche Programme an dessen Dienste kommen und was das Wort „Linux“ genau bezeichnet.
:::

### Das Betriebssystem

<span class="anker" id="stufe-1-1"></span>

Auf einem Laptop laufen gleichzeitig ein Browser, ein Editor, ein Musikprogramm und vielleicht ein Programm, das gerade Fotos vom Handy speichert. Alle brauchen den Prozessor, den Arbeitsspeicher, die SSD, das Netz und den Bildschirm. Irgendjemand muss diese Hardware aufteilen und dafür sorgen, dass der Browser nicht versehentlich die Fotos überschreibt. Und keines dieser Programme sollte wissen müssen, welche SSD genau eingebaut ist.

Abbildung [1](#abb-1) zeigt, wo diese Aufgabe erledigt wird: in einer eigenen Schicht zwischen der Hardware und den Programmen, mit denen man arbeitet.

:::abbildung linux/k1schichten 1
Das Betriebssystem liegt als Schicht zwischen der Hardware und den Programmen. Die Programme fordern bei ihm Dienste an; die Hardware steuert nur das Betriebssystem.
:::

:::definition Definition 1.1 (Betriebssystem)
<span class="anker" id="satz-1-1"></span>

Das __Betriebssystem__ ist die Software, die die Hardware eines Rechners verwaltet, sie den übrigen Programmen über einheitliche Dienste zur Verfügung stellt und die Programme voneinander abschirmt.
:::

Ein Programm, das unter einem Betriebssystem läuft und für den Benutzer eine Aufgabe erledigt, heißt __Anwendungsprogramm__, kurz Programm. Bekannte Betriebssysteme sind Windows, macOS, Android und die Linux-Systeme, um die es in dieser Reihe geht.

::::beispiel Eine Datei speichern
Du drückst im Editor Strg+S. Der Editor weiß nicht, ob die Datei auf einer SSD, einem USB-Stick oder einem Netzlaufwerk landet, und er muss es auch nicht wissen. Er bittet das Betriebssystem: „Schreibe diese 2 000 Zeichen in die Datei `notiz.txt`.“ Das Betriebssystem sucht freien Platz auf dem Datenträger, schreibt die Daten, merkt sich, wo sie liegen, und meldet dem Editor, ob es geklappt hat. Speichert gleichzeitig ein zweites Programm eine andere Datei, sorgt das Betriebssystem dafür, dass sich die beiden Schreibvorgänge nicht in die Quere kommen.
::::

⁠**Kurz gesagt:** Das Betriebssystem verwaltet die Hardware, bietet den Programmen Dienste an und hält sie voneinander fern.

:::hintergrund Warum es überhaupt eine Verwaltungsschicht gibt
Man kann die Aufgaben eines Betriebssystems auf drei Ideen zurückführen.

<ul>

<li>

⁠**Abstraktion.** Eine SSD kennt nur nummerierte Blöcke von je 512 oder 4 096 Byte. Das Betriebssystem macht daraus Dateien mit Namen und Ordnern. Jedes Programm arbeitet mit Dateien, und nur das Betriebssystem muss die Blöcke kennen.

</li>

<li>

⁠**Aufteilung.** Ein Prozessorkern kann zu einem Zeitpunkt nur ein Programm ausführen. Das Betriebssystem wechselt viele Male in der Sekunde zwischen den Programmen hin und her, und jedes bekommt einen eigenen Bereich des Arbeitsspeichers. So scheint jedes Programm einen eigenen Rechner zu haben.

</li>

<li>

⁠**Schutz.** Weil alle Zugriffe auf die Hardware über das Betriebssystem laufen, kann es prüfen, ob ein Programm etwas darf. Ein abgestürztes Programm reißt dann die anderen nicht mit.

</li>

</ul>

Die zweite Idee ist bemerkenswert: Das Betriebssystem erzeugt aus einer einzigen Hardware die Illusion vieler Maschinen.
:::

### Zwei Betriebsarten des Prozessors

<span class="anker" id="stufe-1-2"></span>

Schutz funktioniert nur, wenn ein Programm ihn nicht einfach umgehen kann. Ein bösartiges oder fehlerhaftes Programm könnte ja versuchen, die SSD selbst anzusprechen, statt das Betriebssystem zu fragen. Verhindern kann das nur die Hardware, und zwar der Prozessor selbst.

**Zwei Stufen der Erlaubnis.** Man kann sich den Prozessor wie eine Maschine mit einem Schlüsselschalter vorstellen. In der einen Stellung darf er alles, in der anderen nur das Ungefährliche. Umschalten kann man nur in der Stellung „alles“.

:::definition Definition 1.2 (Kernel-Modus und Benutzermodus)
<span class="anker" id="satz-1-2"></span>

Ein Prozessor kennt mindestens zwei Betriebsarten. Im __Kernel-Modus__ darf das laufende Programm jeden Befehl des Prozessors ausführen. Im __Benutzermodus__ sind bestimmte Befehle gesperrt, etwa der direkte Zugriff auf Geräte und das Einstellen, welches Programm welchen Teil des Arbeitsspeichers benutzen darf. Ein solcher gesperrter Befehl heißt __privilegierter Befehl__. Versucht ein Programm im Benutzermodus einen privilegierten Befehl, führt der Prozessor ihn nicht aus: Er unterbricht das Programm und übergibt die Kontrolle an das Betriebssystem.
:::

::::beispiel Ein Programm greift selbst auf die SSD zu
Ein Programm im Benutzermodus enthält einen Befehl, der Daten direkt an die SSD schicken soll. Der Prozessor erkennt den gesperrten Befehl und führt ihn nicht aus, sondern springt in das Betriebssystem. Das Betriebssystem stellt fest, dass das Programm etwas Verbotenes versucht hat, und beendet es. Die SSD hat von dem Versuch nichts bemerkt.
::::

⁠**Kurz gesagt:** Der Prozessor selbst sorgt dafür, dass gewöhnliche Programme die Hardware nicht direkt anfassen können.

### Der Kernel

<span class="anker" id="stufe-1-3"></span>

Wenn nur im Kernel-Modus alles erlaubt ist, muss es einen Teil des Betriebssystems geben, der in diesem Modus läuft. Dieser Teil ist so wichtig, dass er einen eigenen Namen hat.

:::definition Definition 1.3 (Kernel)
<span class="anker" id="satz-1-3"></span>

Der __Kernel__ (deutsch Kern) ist der Teil des Betriebssystems, der im Kernel-Modus läuft. Er steuert die Hardware unmittelbar, teilt Prozessor und Arbeitsspeicher unter den Programmen auf, verwaltet die Dateien und prüft bei jedem Zugriff, ob er erlaubt ist. Alle übrigen Programme laufen im Benutzermodus.
:::

Zum Kernel gehören auch die __Treiber__: Programmteile, die ein bestimmtes Gerät ansteuern können, etwa eine bestimmte Netzwerkkarte oder eine bestimmte SSD. Andere Teile eines Betriebssystems, zum Beispiel das Fenster, in dem man Befehle eintippt, oder die Programme zum Kopieren von Dateien, laufen dagegen im Benutzermodus wie jedes Anwendungsprogramm.

::::beispiel Wer was tut, wenn ein Video läuft
Ein Videoprogramm liest eine Datei, rechnet die gespeicherten Daten in Bilder um und zeigt sie an. Das Lesen der Datei erledigt der Kernel mit dem Treiber der SSD. Das Umrechnen der Daten in Bilder macht das Videoprogramm in diesem Beispiel selbst im Benutzermodus, denn dafür braucht es keine Geräte, nur Rechenbefehle. Das fertige Bild bringt wieder der Kernel mit dem Grafiktreiber auf den Bildschirm.
::::

⁠**Kurz gesagt:** Der Kernel ist der einzige Teil des Systems, der die Hardware direkt steuern darf.

### Der Systemaufruf

<span class="anker" id="stufe-1-4"></span>

Ein Programm im Benutzermodus darf die SSD nicht anfassen, muss aber trotzdem Dateien lesen und schreiben. Es braucht also einen Weg, den Kernel um einen Dienst zu bitten, ohne selbst in den Kernel-Modus zu gelangen.

**Ein Schalter mit festen Formularen.** Wie an einem Behördenschalter kann man nicht hinter den Tresen gehen; man füllt eines der vorgesehenen Formulare aus und reicht es durch. Die Behörde prüft den Antrag und erledigt ihn oder lehnt ihn ab (ein Bild, kein Mechanismus). Abbildung [2](#abb-2) zeigt den Mechanismus.

:::abbildung linux/k1systemaufruf 2
Ein Programm kommt an die Hardware nur über einen Systemaufruf: Es nennt die Nummer des gewünschten Dienstes und die Angaben dazu, ein besonderer Prozessorbefehl wechselt in den Kernel-Modus, und der Kernel prüft und erledigt den Auftrag. Ein direkter Zugriff aus dem Benutzermodus wird vom Prozessor gesperrt.
:::

:::definition Definition 1.4 (Systemaufruf)
<span class="anker" id="satz-1-4"></span>

Ein __Systemaufruf__ ist eine Anfrage eines Programms an den Kernel, einen bestimmten Dienst auszuführen, zum Beispiel eine Datei zu öffnen, Daten zu lesen oder Speicher bereitzustellen. Das Programm legt die Nummer des Dienstes und die nötigen Angaben bereit und führt einen besonderen Prozessorbefehl aus. Dieser schaltet in den Kernel-Modus und springt an eine Stelle im Kernel, die der Kernel beim Start des Rechners selbst festgelegt hat. Der Kernel prüft die Anfrage, erledigt sie, schaltet zurück in den Benutzermodus und gibt dem Programm das Ergebnis.
:::

::::beispiel Was ein kleines Programm vom Kernel will
Unter Linux gibt es ein Werkzeug namens `strace`, das jeden Systemaufruf eines Programms mitschreibt. Hier ist es dem Programm `gnucat` zugeschaltet, der klassischen Fassung eines Programms, das den Inhalt einer Datei anzeigt; gezeigt wird die Datei, in der der Name des Rechners steht. Zu sehen sind die Aufrufe zum Öffnen, Lesen, Schreiben und Schließen:

```text
openat(AT_FDCWD, "/etc/hostname", O_RDONLY) = 3
read(3, "labor\n", 262144)              = 6
write(1, "labor\n", 6)                  = 6
read(3, "", 262144)                     = 0
close(3)                                = 0
```

Die erste Zeile bittet den Kernel, die Datei `/etc/hostname` zum Lesen zu öffnen; er antwortet mit der Nummer 3, unter der das Programm die Datei danach anspricht. Die zweite Zeile liest bis zu 262 144 Byte; der Kernel liefert 6 Byte, das Wort `labor` und ein Zeilenende. Die dritte Zeile schreibt diese 6 Byte auf die Ausgabe mit der Nummer 1, das ist das Fenster, in dem das Programm läuft. Der zweite Leseversuch liefert 0 Byte: Die Datei ist zu Ende. Zuletzt schließt das Programm die Datei. Insgesamt stellt dieses winzige Programm 114 Systemaufrufe; die übrigen dienen vor allem dazu, beim Start Programmteile zu laden.
::::

⁠**Kurz gesagt:** Programme bekommen Hardware-Dienste nur, indem sie den Kernel über einen Systemaufruf darum bitten.

:::hintergrund Warum das Programm nicht selbst bestimmen darf, wohin es im Kernel springt
Ein Systemaufruf hebt die Rechte des Prozessors an. Dürfte das Programm dabei die Adresse im Kernel frei wählen, könnte es mitten in eine Kernel-Funktion springen, direkt hinter die Stelle, an der der Kernel die Berechtigung prüft, und hätte damit alle Rechte. Deshalb legt der Kernel beim Start, wenn der Prozessor ohnehin im Kernel-Modus läuft, im Prozessor eine feste Einsprungstelle fest: Jeder Systemaufruf springt genau dorthin. Ein Programm kann nur die Nummer eines Dienstes nennen. An der Einsprungstelle schlägt der Kernel selbst in seiner Tabelle der Dienste nach, welche Kernel-Funktion zu dieser Nummer gehört, und prüft die Angaben, bevor er sie ausführt. Die Einsprungstelle festzulegen ist selbst ein privilegierter Befehl, und die Tabelle liegt in einem Speicherbereich, den Programme im Benutzermodus nicht beschreiben dürfen. Der einzige Weg in den Kernel-Modus führt so durch ein Tor, das der Kernel selbst gebaut hat und bewacht.
:::

### Linux

<span class="anker" id="stufe-1-5"></span>

Mit dem Wort „Linux“ meinen Menschen zwei verschiedene Dinge: mal ein ganzes System mit Fenstern und Programmen, mal nur einen ganz bestimmten Teil davon. Für dieses Kapitel ist der Unterschied wichtig.

:::definition Definition 1.5 (Linux)
<span class="anker" id="satz-1-5"></span>

__Linux__ ist ein Kernel. Linus Torvalds hat ihn 1991 als Student in Helsinki begonnen; heute pflegen ihn Tausende Entwickler aus Firmen, Hochschulen und Freizeit. Sein Quelltext ist frei verfügbar unter der GNU General Public License (GPL) in Version 2. Im engeren Sinn bezeichnet „Linux“ nur diesen Kernel; umgangssprachlich meint man oft das ganze System, das auf ihm aufbaut.
:::

::::beispiel Ein Kernel, viele Systeme
Derselbe Linux-Kernel, jeweils etwas angepasst, steckt in sehr verschiedenen Geräten: in den meisten Servern des Internets, in Android-Smartphones, in vielen WLAN-Routern und Fernsehern und in den Linux-Systemen für PCs. Ein Android-Handy und ein Ubuntu-Laptop benutzen also beide Linux als Kernel, haben aber fast keine anderen Programme gemeinsam.
::::

⁠**Kurz gesagt:** Linux ist streng genommen nur der Kernel eines Betriebssystems.

:::hintergrund Warum es so viele verschiedene Linux-Systeme gibt
Die GPL erlaubt jedem, den Quelltext des Kernels zu benutzen, zu verändern und weiterzugeben, auch gegen Geld. Sie verlangt im Gegenzug, dass jeder, der eine veränderte Fassung weitergibt, auch deren Quelltext unter derselben Lizenz zugänglich macht. Deshalb kann jede Firma und jede Gruppe ein eigenes System um den Kernel bauen, und Verbesserungen fließen in den gemeinsamen Kernel zurück. Die Programme, die ein Linux-System um den Kernel herum braucht, stammen zu einem großen Teil aus dem GNU-Projekt, das Richard Stallman 1983 begonnen hatte, um ein freies Betriebssystem zu schaffen; ihm fehlte zu Beginn der 1990er-Jahre gerade noch ein Kernel. Manche sprechen deshalb von „GNU/Linux“.
:::

### Die Distribution

<span class="anker" id="stufe-1-6"></span>

Ein Kernel allein kann mit dir nicht reden. Er hat kein Fenster, in das man etwas eintippen könnte, keine Programme zum Kopieren von Dateien und keinen Browser. Damit ein benutzbares System entsteht, muss jemand Tausende Programme passend zum Kernel zusammenstellen, aufeinander abstimmen und über Jahre mit Fehlerbehebungen versorgen.

:::definition Definition 1.6 (Distribution)
<span class="anker" id="satz-1-6"></span>

Eine __Distribution__ ist ein vollständiges Betriebssystem, das ein Hersteller oder eine Gemeinschaft aus dem Linux-Kernel, Werkzeugen, Anwendungsprogrammen und Voreinstellungen zusammenstellt und als Ganzes pflegt. Zu jeder Distribution gehört eine __Paketverwaltung__: ein Programm, mit dem man Software aus den Quellen der Distribution installiert, aktualisiert und wieder entfernt. Wie sie arbeitet, erklärt Kapitel 9.
:::

::::beispiel [Beispiele] Vier Distributionen
Tabelle [1](#tab-1) nennt vier Distributionen, die in dieser Reihe vorkommen.

<span class="anker" id="tab-1"></span>

**Tabelle 1:** Vier Distributionen. Alle benutzen den Linux-Kernel, unterscheiden sich aber in der Auswahl der Programme, in der Paketverwaltung und darin, wie lange eine Version gepflegt wird.

| Distribution | Wer sie pflegt | Kennzeichen |
|---|---|---|
| Debian | eine weltweite Gemeinschaft von Freiwilligen | sehr stabil, Grundlage vieler anderer Distributionen |
| Ubuntu | die Firma Canonical mit einer Gemeinschaft | baut auf Debian auf, weit verbreitet, gut dokumentiert; diese Reihe benutzt Ubuntu 26.04 LTS |
| Fedora | eine Gemeinschaft, unterstützt von der Firma Red Hat | bringt neue Software früh, Grundlage für Red Hat Enterprise Linux |
| Kali Linux | die Firma OffSec | baut auf Debian auf, enthält Hunderte Werkzeuge für Sicherheitstests; ihre Herausgeber raten Linux-Neulingen ausdrücklich ab |
::::

⁠**Kurz gesagt:** Linux ist der Kern; eine Distribution macht daraus ein vollständiges System.

:::hintergrund Warum diese Reihe Ubuntu benutzt
Für ein Übungssystem zählen drei Dinge: dass es auf fast jedem Rechner läuft, dass man bei Problemen Hilfe findet und dass es lange gepflegt wird. Ubuntu ist eine der am weitesten verbreiteten Distributionen für Arbeitsplätze und Server, seine Dokumentation ist frei verfügbar, und Windows bringt einen eigenen Weg zu einem Linux mit, der standardmäßig Ubuntu einrichtet. Weil Ubuntu auf Debian aufbaut, gilt fast alles, was du hier lernst, auch für Debian und Kali Linux.
:::

### Version und Langzeitpflege

<span class="anker" id="stufe-1-7"></span>

Eine Distribution erscheint immer wieder in neuen Versionen. Wer ein Übungssystem einrichtet, muss sich für eine entscheiden, und bei Ubuntu verrät die Versionsnummer schon fast alles Nötige.

:::definition Definition 1.7 (Ubuntu-Version, LTS)
<span class="anker" id="satz-1-7"></span>

Eine Ubuntu-Version heißt nach Jahr und Monat ihres Erscheinens: `26.04` erschien im April 2026. Dazu hat jede Version einen Codenamen, `26.04` heißt „Resolute Raccoon“. Alle zwei Jahre im April erscheint eine __LTS-Version__ (Long Term Support, Langzeitpflege), für die Canonical fünf Jahre lang Sicherheits- und Fehlerkorrekturen liefert. Dazwischen erscheinen Zwischenversionen, die nur neun Monate gepflegt werden. Eine Nummer wie `26.04.1` bezeichnet eine __Punktversion__: dasselbe System mit den bis dahin gesammelten Korrekturen und neuen Installationsmedien.
:::

::::beispiel Drei Versionen einordnen
Ubuntu 26.04 LTS erschien am 23. April 2026 und wird bis April 2031 gepflegt; seine erste Punktversion 26.04.1 erschien am 27. August 2026. Ubuntu 26.10 erschien im Oktober 2026 und ist eine Zwischenversion; sie wird bis Juli 2027 gepflegt. Ubuntu 24.04 LTS, die vorige Langzeitversion, wird noch bis April 2029 gepflegt. Diese Reihe benutzt 26.04 LTS.
::::

⁠**Kurz gesagt:** Für ein Übungssystem nimmt man die aktuelle LTS-Version, weil sie fünf Jahre lang Korrekturen bekommt.

:::hintergrund Warum es Langzeitversionen gibt
Neue Versionen bringen neue Programme, aber auch neue Fehler und geänderte Bedienung. Wer einen Server, ein Labor oder einen Kurs betreibt, will ein System, das sich jahrelang gleich verhält und trotzdem jede neu entdeckte Sicherheitslücke geschlossen bekommt. Eine LTS-Version trennt beides: Sie bekommt fünf Jahre lang Korrekturen, aber keine neuen Funktionen, die etwas verändern könnten. Für noch längere Pflege gibt es bei Canonical ein Zusatzangebot namens Ubuntu Pro.
:::

### Aufgaben zu Abschnitt [1](#stufe-1)

<span class="anker" id="stufe-1-8"></span>

:::aufgabe Aufgabe 1 ★ Wer erledigt was?
<span class="anker" id="aufg-1"></span>

Ordne jede Tätigkeit zu: Läuft sie im Benutzermodus oder im Kernel-Modus? Ist ein Systemaufruf beteiligt?

<ol class="al">

<li>

Ein Tabellenprogramm berechnet den Durchschnitt von 1 000 Zahlen, die schon im Arbeitsspeicher stehen.

</li>

<li>

Das Tabellenprogramm speichert die Tabelle.

</li>

<li>

Der Treiber der SSD schreibt die Blöcke der Tabelle auf die SSD.

</li>

<li>

Ein Browser bittet um 200 MB zusätzlichen Arbeitsspeicher.

</li>

</ol>

:::loesung
(a) Benutzermodus, kein Systemaufruf. Die Zahlen stehen schon im Arbeitsspeicher des Programms, und Addieren und Dividieren sind gewöhnliche Rechenbefehle, die jedes Programm ausführen darf. Der Kernel ist daran nicht beteiligt.

(b) Das Tabellenprogramm selbst läuft im Benutzermodus, aber Speichern heißt, Daten auf einen Datenträger zu bringen, und das darf es nicht selbst. Es stellt Systemaufrufe, etwa zum Öffnen der Datei, zum Schreiben und zum Schließen. Die eigentliche Arbeit erledigt dann der Kernel im Kernel-Modus.

(c) Kernel-Modus. Der Treiber ist Teil des Kernels und spricht das Gerät direkt an. Er stellt selbst keinen Systemaufruf, sondern erledigt den Auftrag, der in (b) mit einem Systemaufruf hereinkam.

(d) Systemaufruf. Welches Programm welchen Teil des Arbeitsspeichers benutzen darf, stellt nur der Kernel ein; das ist ein privilegierter Vorgang. Der Browser bittet also den Kernel per Systemaufruf, der Kernel richtet den Speicher im Kernel-Modus ein und meldet dem Browser, wo er liegt.
:::
:::

:::aufgabe Aufgabe 2 ★ Kernel oder Distribution?
<span class="anker" id="aufg-2"></span>

Stimmt die Aussage? Begründe jeweils in einem Satz.

<ol class="al">

<li>

„Android ist ein Linux.“

</li>

<li>

„Ubuntu und Kali Linux benutzen denselben Kernel, also sind sie dasselbe System.“

</li>

<li>

„Wer Linux installiert, installiert eine Distribution.“

</li>

<li>

„Die Paketverwaltung gehört zum Kernel.“

</li>

</ol>

:::loesung
(a) Im engeren Sinn stimmt es: Android benutzt den Linux-Kernel. Eine Linux-Distribution wie Ubuntu ist Android aber nicht, denn um den Kernel herum stehen fast nur andere Programme. Wer „Linux“ im umgangssprachlichen Sinn meint, also ein System mit Terminal und den üblichen Werkzeugen, hat mit Android etwas anderes vor sich.

(b) Falsch. Beide benutzen den Linux-Kernel, jede baut ihn aber selbst in ihrer eigenen Fassung, und alles um den Kernel herum, die Auswahl der Programme, die Voreinstellungen und die Pflege, unterscheidet sich. Derselbe Kernel macht noch nicht dasselbe System.

(c) Richtig. Ein Kernel allein ist nicht benutzbar; was man herunterlädt und installiert, ist immer eine Distribution mit Kernel, Werkzeugen und Paketverwaltung.

(d) Falsch. Die Paketverwaltung ist ein gewöhnliches Programm der Distribution und läuft im Benutzermodus. Wenn sie Dateien installiert, stellt sie dafür Systemaufrufe wie jedes andere Programm.
:::
:::

:::aufgabe Aufgabe 3 ★★ Kann ein Programm den Kernel umgehen?
<span class="anker" id="aufg-3"></span>

Ein Programm im Benutzermodus versucht nacheinander drei Dinge: (1) direkt Daten an die Netzwerkkarte zu schicken, (2) die Einsprungstelle für Systemaufrufe oder die Tabelle der Dienste so zu ändern, dass ein Systemaufruf in seinen eigenen Code springt, (3) einen Systemaufruf mit einer Nummer zu stellen, die es gar nicht gibt. Was geschieht jeweils, und warum kann das Programm auf keinem der drei Wege die Kontrolle über den Rechner erlangen?

:::loesung
(1) Der direkte Zugriff auf die Netzwerkkarte ist ein privilegierter Befehl. Im Benutzermodus führt der Prozessor ihn nicht aus, sondern unterbricht das Programm und übergibt an den Kernel, und der beendet das Programm.

(2) Die Einsprungstelle festzulegen ist ein privilegierter Befehl; ein solcher Versuch geht genauso aus wie (1). Die Tabelle der Dienste liegt in einem Speicherbereich des Kernels, den Programme im Benutzermodus nicht beschreiben dürfen; auch dieser Versuch wird vom Prozessor unterbrochen. Der Kernel hat beides beim Start im Kernel-Modus eingerichtet, und aus dem Benutzermodus kann es niemand verändern.

(3) Der Systemaufruf selbst ist erlaubt. Der Prozessor springt dabei an die feste Einsprungstelle des Kernels, nicht an eine Stelle, die das Programm wählt. Dort sucht der Kernel die Nummer in seiner Tabelle, findet keinen Dienst dazu und gibt dem Programm einen Fehlercode zurück. Das Programm läuft weiter, hat aber nichts erreicht.

Der Grund für alle drei: Es gibt genau zwei Arten, in den Kernel-Modus zu gelangen, nämlich eine Unterbrechung, etwa wenn der Prozessor einen gesperrten Befehl abfängt, oder einen Systemaufruf, und beide landen an Stellen, die der Kernel selbst festgelegt hat. Alles, womit man diese Stellen ändern oder die Hardware direkt erreichen könnte, ist im Benutzermodus gesperrt.
:::
:::

:::aufgabe Aufgabe 4 ★ Versionen einordnen
<span class="anker" id="aufg-4"></span>

Gib für jede Version an, ob sie eine LTS-Version ist, in welchem Monat sie erschien und bis wann sie gepflegt wird: 24.04, 25.10, 26.04.1, 26.10. Welche würdest du am 9. November 2026 für ein Übungssystem wählen, das du drei Jahre lang benutzen willst?

:::loesung
| Version | LTS? | erschienen | gepflegt bis |
|---|---|---|---|
| 24.04 | ja | April 2024 | April 2029 |
| 25.10 | nein | Oktober 2025 | Juli 2026, abgelaufen |
| 26.04.1 | ja (Punktversion) | August 2026 | April 2031 |
| 26.10 | nein | Oktober 2026 | Juli 2027 |

25.10 wurde neun Monate gepflegt; 26.04.1 ist die erste Punktversion von 26.04, das im April 2026 erschien. Für drei Jahre ab November 2026, also bis November 2029, kommt nur Ubuntu 26.04 LTS in Frage, eingerichtet mit den Medien von 26.04.1. Die Version 24.04 endet im April 2029, und 26.10 schon im Juli 2027. Eine Punktversion ist keine eigene Version: Wer 26.04 installiert und aktualisiert, hat danach denselben Stand wie mit 26.04.1.
:::
:::

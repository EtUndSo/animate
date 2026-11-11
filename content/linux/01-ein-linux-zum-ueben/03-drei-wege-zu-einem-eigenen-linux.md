---
title: Drei Wege zu einem eigenen Linux
pfad: Informatik / Linux und Kommandozeile / Ein Linux zum Üben: WSL, virtuelle Maschine, Live-USB-Stick
adresse: informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick
knoten: Kapitel 1: Ein Linux zum Üben: WSL, virtuelle Maschine, Live-USB-Stick
order: 6060300
summary: Es gibt drei bewährte Wege, unter Windows an ein Linux zum Üben zu kommen.
tags: Terminal, Eingabeaufforderung
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Es gibt drei bewährte Wege, unter Windows an ein Linux zum Üben zu kommen. Dieser Abschnitt stellt sie nebeneinander, hilft mit einem Entscheidungsbaum bei der Wahl und erklärt, was am Ende jedes Wegs steht: ein Fenster, in das man Befehle eintippt.
:::

### Die drei Wege im Überblick

<span class="anker" id="stufe-2-1"></span>

Ein Linux zum Üben soll zwei Dinge leisten: Es soll ein echtes Linux sein, an dem alles funktioniert, was die Reihe zeigt, und es soll Windows und deine Dateien nicht gefährden. Abbildung [3](#abb-3) zeigt die drei Wege, die beides leisten, jeder auf seine Art.

:::abbildung linux/k1wege 3
Drei Wege zu einem Linux auf einem Windows-Rechner. WSL 2 lässt Linux unsichtbar neben Windows laufen, eine virtuelle Maschine bildet einen ganzen Rechner nach, und vom Live-USB-Stick startet der Rechner selbst ein Linux, während Windows unberührt auf der Platte ruht.
:::

<ul>

<li>

⁠**WSL 2.** Windows startet im Hintergrund einen kleinen, unsichtbaren Rechner im Rechner, in dem ein Linux läuft. Man öffnet ein Fenster und arbeitet in Linux, während daneben die gewohnten Windows-Programme weiterlaufen. Das ist der schnellste Weg, und er reicht für Programmieren, Datenanalyse und alle Übungen an der Kommandozeile.

</li>

<li>

⁠**Virtuelle Maschine.** Ein Programm wie VirtualBox bildet einen vollständigen Rechner nach, in dem man Linux wie auf einem echten PC installiert. Dieser Rechner ist vom echten getrennt, man kann seinen Zustand speichern und jederzeit zurückholen. Das ist der Weg für Labore, in denen man etwas kaputt machen darf.

</li>

<li>

⁠**Live-USB-Stick.** Man schreibt ein Linux auf einen USB-Stick und startet den Rechner davon. Dann läuft Linux direkt auf der echten Hardware, und Windows ruht unberührt auf der internen Platte. Nach dem Ausschalten ist alles wie vorher. Das ist die erste echte Linux-Praxis auf dem eigenen Gerät; sie erfordert aber die meiste Sorgfalt, weil man dabei einen Datenträger beschreibt und den Rechner auf ungewohnte Weise startet.

</li>

</ul>

Tabelle [2](#tab-2) stellt die drei Wege gegenüber.

<span class="anker" id="tab-2"></span>

**Tabelle 2:** Die drei Wege im Vergleich.

|  | WSL 2 | virtuelle Maschine | Live-USB-Stick |
|---|---|---|---|
| läuft | neben Windows | in einem Fenster unter Windows | statt Windows |
| gut für | Kommandozeile, Programmieren, Datenanalyse | Labore, Ausprobieren mit Rückweg | Linux auf echter Hardware erleben |
| braucht | Windows 10 ab Version 2004 oder Windows 11 | genug Arbeitsspeicher und Plattenplatz | einen USB-Stick ab 8 GB |
| Grenzen | eigenes kleines Netz, kein direkter Zugriff auf USB-Geräte | langsamer als der echte Rechner | ohne Zusatz ist nach dem Ausschalten alles weg |
| Risiko für Windows | sehr gering | sehr gering | gering, wenn man die Warnungen beachtet |

⁠**Kurz gesagt:** WSL 2 ist der schnellste Weg, die virtuelle Maschine das Labor und der Live-USB-Stick das echte Linux auf echter Hardware.

### Der Entscheidungsbaum

<span class="anker" id="stufe-2-2"></span>

Welcher Weg der richtige ist, hängt davon ab, was du mit Linux vorhast. Der Entscheidungsbaum in Abbildung [4](#abb-4) stellt zwei Fragen.

:::abbildung linux/k1entscheidung 4
Welcher Weg passt? Wer Linux zum Programmieren, für Datenanalyse oder zum Üben an der Kommandozeile braucht, landet bei WSL 2. Neben jedem Weg steht, welche Abschnitte dieses Kapitels er braucht; Abschnitte 1 und 2 gelten für alle.
:::

Die Wege schließen sich nicht aus. Viele arbeiten im Alltag mit WSL 2 und halten für Versuche, bei denen etwas schiefgehen darf, eine virtuelle Maschine bereit. Wer zum ersten Mal ein Linux auf echter Hardware sehen will, startet es einmal vom Stick, auch wenn er sonst WSL 2 benutzt.

::::beispiel Drei Studierende, drei Wege
Lea will in Python programmieren und Daten auswerten; ihr Laptop hat Windows 11. Für sie ist WSL 2 richtig: Sie muss nichts neu starten, und ihre Dateien sind von Windows und Linux aus erreichbar. Jonas will Netzwerkverkehr zwischen zwei Rechnern untersuchen, ohne sein Heimnetz zu stören, und dabei auch Einstellungen ausprobieren, die das System beschädigen können. Er braucht eine virtuelle Maschine. Mira will wissen, ob ihr Laptop mit Linux überhaupt zurechtkommt, ob WLAN, Grafik und Ton funktionieren. Sie startet Linux vom USB-Stick, denn nur so läuft es auf ihrer echten Hardware.
::::

⁠**Kurz gesagt:** Für Programmieren und Kommandozeile nimmt man WSL 2, für Labore eine virtuelle Maschine und für echtes Linux auf echter Hardware den Live-USB-Stick.

:::hintergrund Warum es nicht den einen besten Weg gibt
Die drei Wege liegen auf einer Skala zwischen zwei Zielen, die sich widersprechen. Je näher ein Linux an der echten Hardware läuft, desto echter ist die Erfahrung: Auf dem Live-Stick steuert Linux die Netzwerkkarte, die Grafik und die USB-Anschlüsse selbst. Je mehr Software zwischen Linux und der Hardware liegt, desto besser ist es abgeschottet, und desto leichter macht man Fehler rückgängig. WSL 2 opfert dafür etwas Abschottung zugunsten von Bequemlichkeit, denn es teilt Dateien mit Windows. Jeder der drei Wege ist ein anderer Kompromiss zwischen beiden Zielen.
:::

### Das Terminal

<span class="anker" id="stufe-2-3"></span>

Alle drei Wege enden an derselben Stelle: an einem Fenster, in das man Befehle eintippt. Die meiste Arbeit in dieser Reihe geschieht dort, denn ein getippter Befehl ist genau, wiederholbar und lässt sich aufschreiben.

:::definition Definition 2.1 (Terminal)
<span class="anker" id="satz-2-1"></span>

Ein __Terminal__ ist ein Programm mit einem Fenster, in das man Befehle als Text eintippt und in dem die Antworten des Rechners als Text erscheinen. Wenn es bereit ist, zeigt es am Anfang der Zeile eine __Eingabeaufforderung__.
:::

In einem Linux-Terminal sieht die Eingabeaufforderung etwa so aus: `student@labor:~$`. Vor dem `@` steht der Name des Benutzers, dahinter der Name des Rechners; das Zeichen `~` steht für den persönlichen Ordner des Benutzers. Unter Windows heißt das entsprechende Programm PowerShell, seine Eingabeaufforderung lautet etwa `PS C:\Users\student>`. [Python, Kapitel 1, Abschnitt 3.1](/wissen/informatik/programmieren/python/programme-und-der-python-interpreter/python-einrichten.html#stufe-3-1) zeigt das Terminal von Windows ausführlicher.

Dieses Kapitel schreibt die Eingabeaufforderung verkürzt: `$` für Linux und `PS>` für Windows. Die wenigen Befehle dieses Kapitels tippst du genau so ab, wie sie dastehen, und drückst danach die Eingabetaste. Was ein Befehl genau ist und wie er aufgebaut ist, erklärt [Kapitel 2](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/die-shell-erste-befehle.html).

::::beispiel Welches System läuft hier?
Der Befehl `cat /etc/os-release` zeigt den Inhalt einer Datei, in der jede Distribution ihren Namen und ihre Version einträgt. So antwortet Ubuntu 26.04.1:

```console
$ cat /etc/os-release
PRETTY_NAME="Ubuntu 26.04.1 LTS"
NAME="Ubuntu"
VERSION_ID="26.04"
VERSION="26.04.1 LTS (Resolute Raccoon)"
VERSION_CODENAME=resolute
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=resolute
LOGO=ubuntu-logo
```

Die Zeile `VERSION` enthält die Punktversion und den Codenamen aus Unterabschnitt [1.7](betriebssystem-kernel-und-distribution.html#stufe-1-7), und `ID_LIKE=debian` sagt, auf welcher Distribution Ubuntu aufbaut. Diese Ausgabe ist auf jedem der drei Wege dieselbe, denn die Datei gehört zur Distribution.
::::

⁠**Kurz gesagt:** Das Terminal ist das Fenster, in dem man mit dem System in Textform spricht; am Ende jedes Wegs öffnest du eines.

### Aufgaben zu Abschnitt [2](#stufe-2)

<span class="anker" id="stufe-2-4"></span>

:::aufgabe Aufgabe 5 ★ Den passenden Weg wählen
<span class="anker" id="aufg-5"></span>

Wähle mit dem Entscheidungsbaum einen Weg und begründe ihn in zwei Sätzen.

<ol class="al">

<li>

Tom hat einen Windows-11-Laptop und will im nächsten Semester Python lernen.

</li>

<li>

Sara will in einem Kurs zur IT-Sicherheit Einstellungen ausprobieren, die ein System beschädigen können, und danach jedes Mal wieder sauber anfangen.

</li>

<li>

Ali überlegt, sein altes Notebook ganz auf Linux umzustellen, und will vorher sehen, ob WLAN und Grafik funktionieren.

</li>

<li>

Und du? Für welchen Weg entscheidest du dich, und warum?

</li>

</ol>

:::loesung
(a) WSL 2. Tom braucht ein Linux für die Kommandozeile und zum Programmieren, nicht für die Hardware und nicht für ein Labor. Mit Windows 11 ist WSL 2 in wenigen Minuten eingerichtet, und er kann Windows und Linux gleichzeitig benutzen.

(b) Eine virtuelle Maschine. Sara will Dinge ausprobieren, die ein System beschädigen können, und danach sauber neu anfangen; genau das leistet ein Snapshot. Die VM ist dabei vom Wirt getrennt.

(c) Der Live-USB-Stick. Nur damit läuft Linux direkt auf Alis echter Hardware und muss WLAN und Grafik selbst ansteuern. In einer VM oder in WSL 2 sähe Linux nur virtuelle Geräte und würde über die echte Hardware nichts verraten.

(d) Hier gibt es keine falsche Antwort, solange die Begründung zur Frage im Entscheidungsbaum passt. Wer diese Reihe für das Programmieren oder die Datenanalyse liest, nimmt WSL 2; wer die Reihe Cybersecurity verfolgt, richtet zusätzlich eine VM ein und startet einmal vom Stick.
:::
:::

:::aufgabe Aufgabe 6 ★ Eingabeaufforderungen lesen
<span class="anker" id="aufg-6"></span>

Was verraten diese beiden Eingabeaufforderungen? `anna@werkbank:~$` und `PS C:\Users\anna\Documents>`. Was tippst du ein, wenn das Kapitel eine Zeile `$ uname -r` zeigt?

:::loesung
`anna@werkbank:~$` ist die Eingabeaufforderung eines Linux-Terminals: Der Benutzer heißt `anna`, der Rechner `werkbank`, `~` zeigt, dass das Terminal gerade im persönlichen Ordner von `anna` arbeitet, und `$` schließt die Aufforderung ab. `PS C:\Users\anna\Documents>` ist die PowerShell unter Windows; sie arbeitet gerade im Ordner `C:\Users\anna\Documents`.

Zeigt das Kapitel `$ uname -r`, tippst du nur `uname -r` ein und drückst die Eingabetaste. Das `$` und das Leerzeichen danach stehen schon in der Eingabeaufforderung.
:::
:::

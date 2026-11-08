---
title: Python einrichten
pfad: Informatik / Programmieren / Python / Programme und der Python-Interpreter
knoten: Python 1: Programme und der Python-Interpreter
order: 6020400
summary: Um Python-Programme auszuführen, braucht dein Rechner CPython.
tags: Terminal, Eingabeaufforderung, Python install manager, Versionsnummer
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Um Python-Programme auszuführen, braucht dein Rechner CPython. Dieser Abschnitt zeigt, wie du es unter Windows und unter Linux einrichtest und prüfst, welche Version du hast.
:::

### Was du dafür brauchst: ein Terminal öffnen

<span class="anker" id="stufe-3-1"></span>

Python startet man meist mit einem Befehl, den man in ein Terminal tippt. Ein __Terminal__ ist ein Fenster, in das man Befehle als Text eintippt; der Rechner führt jeden Befehl aus und schreibt seine Antwort darunter.

**Öffnen.**

<ul>

<li>

⁠**Windows 11:** Klicke mit der rechten Maustaste auf das Startsymbol und wähle „Terminal“, oder suche im Startmenü nach „Terminal“. Es öffnet sich ein Fenster mit der PowerShell, dem Befehlsprogramm von Windows.

</li>

<li>

⁠**Linux (Ubuntu):** Drücke Strg+Alt+T, oder suche in der Übersicht „Aktivitäten“ nach „Terminal“.

</li>

<li>

⁠**Linux unter Windows (WSL):** Starte im Startmenü die App „Ubuntu“.

</li>

</ul>

**Die Eingabeaufforderung.** Am Ende der letzten Zeile steht ein kurzer Text, hinter dem der Cursor blinkt. Er heißt __Eingabeaufforderung__ und zeigt, dass das Terminal auf einen Befehl wartet. Unter Windows sieht er etwa so aus: `PS C:\Users\student>`. Unter Linux etwa so: `student@labor:~$`. Darin steht der Benutzername `student`, der Rechnername `labor` und mit `~` der persönliche Ordner.

**Einen Befehl eingeben.** Tippe den Befehl hinter die Eingabeaufforderung und drücke Enter. Probiere es mit `echo Hallo`; der Befehl `echo` schreibt den Text dahinter zurück.

In diesem Kapitel stehen Terminal-Sitzungen in grauen Kästen. Die Eingabeaufforderung ist darin verkürzt: `PS>` unter Windows, `$` unter Linux. Du tippst nur, was dahinter steht. Zeilen ohne diesen Anfang sind die Antwort des Rechners.

```console Windows (PowerShell)
PS> echo Hallo
Hallo
```

```console Linux
$ echo Hallo
Hallo
```

Mehr zum Terminal, zu Ordnern und zu Befehlen steht ausführlich in Linux 2.

### Python unter Windows: der Python install manager

<span class="anker" id="stufe-3-2"></span>

Windows bringt kein Python mit. Seit Python 3.14 bietet `python.org` dafür ein eigenes Verwaltungsprogramm an; das frühere Installationsprogramm für einzelne Versionen gilt seitdem als veraltet und erscheint für Python 3.16 nicht mehr.

:::definition Definition 3.1 (Python install manager)
<span class="anker" id="satz-3-1"></span>

Der __Python install manager__ ist ein Programm für Windows, das Python-Versionen herunterlädt, installiert, auflistet, entfernt und startet. Man bedient ihn im Terminal mit dem Befehl `py`.
:::

**Schritt 1: den install manager installieren.** Es gibt ihn als App „Python install manager“ im Microsoft Store und als Download auf `python.org/downloads`; beide Fassungen sind gleich. Wer lieber einen Befehl benutzt, tippt im Terminal:

```console Windows (PowerShell)
PS> winget install 9NQ7512CXL7T -e --accept-package-agreements --disable-interactivity
```

**Schritt 2: eine Python-Version installieren.** Zum Beispiel die Version 3.14:

```console Windows (PowerShell)
PS> py install 3.14
```

Ist noch gar keine Version installiert, holt der erste Start von `py` oder `python` die neueste Version auch von selbst.

**Schritt 3: nachsehen, was installiert ist.** `py list` zeigt die installierten Versionen und welche davon die Standardversion ist. Welche Versionen es zum Herunterladen gibt, zeigt `py list --online`.

Danach startet `py` die Standardversion; das ist die neueste installierte, wenn du nichts anderes einstellst. Der Befehl `python` tut dasselbe. Eine bestimmte Version wählst du mit `py -V:3.14`. In diesem Kapitel steht unter Windows der Befehl `py`.

**Beispiel: die Version prüfen.** Die Option `--version` lässt Python seine Versionsnummer nennen, ohne sonst etwas zu tun. Auf dem Rechner, mit dem dieses Kapitel geprüft wurde, ist Python 3.13 installiert:

```console Windows (PowerShell)
PS> py --version
Python 3.13.9
```

**Zwei typische Probleme.**

<ul>

<li>

⁠**Statt Python öffnet sich der Microsoft Store.** Windows legt einen Platzhalter mit dem Namen `python` an, der den Store öffnet. Öffne im Startmenü „App-Ausführungsaliase verwalten“ und prüfe, dass die Einträge „Python (default)“ des install managers eingeschaltet sind.

</li>

<li>

⁠**`py list` meldet „legacy py.exe command“.** Dann ist noch der alte Starter „Python Launcher“ aus dem früheren Installationsprogramm vorhanden und hat Vorrang. Auf dem Prüfrechner sieht das so aus:

```console Windows (PowerShell)
PS> py list
WARNING: The 'list' command is unavailable because this is the legacy py.exe command.
If you have already installed the Python install manager, open Installed Apps and remove 'Python Launcher' to enable the new py.exe command.
C:\Users\student\AppData\Local\Programs\Python\Python313\python.exe: can't open file 'C:\\Users\\student\\list': [Errno 2] No such file or directory
```

Der alte Starter kennt den Befehl `list` nicht und gibt das Wort an Python weiter, das darauf eine Datei namens `list` sucht. Abhilfe: Einstellungen, „Installierte Apps“, „Python Launcher“ deinstallieren. Ein Python, das mit dem früheren Installationsprogramm eingerichtet wurde, darf bleiben; `py` findet es weiterhin.

</li>

</ul>

⁠**Kurz gesagt:** Unter Windows installierst du den Python install manager und startest Python danach mit `py`.

:::hintergrund Warum es unter Windows einen eigenen Starter gibt
Unter Windows gibt es keinen festen Ort, an dem Programme wie Python liegen müssen, und oft sind mehrere Python-Versionen nebeneinander installiert. Früher musste jedes Installationsprogramm selbst eintragen, wo Windows den Befehl `python` findet, und mehrere Versionen kamen sich dabei leicht in die Quere. Ein einziger Starter, der alle installierten Versionen kennt und die gewünschte auswählt, löst das. Der Python install manager übernimmt seit Python 3.14 zusätzlich das Installieren und Entfernen der Versionen.

Den Platzhalter, der den Store öffnet, hat Microsoft 2019 eingeführt: Wer `python` eintippt, ohne dass Python installiert ist, soll direkt zu einem Weg geführt werden, es zu installieren. Ist ein Python vorhanden, stört er nur, solange er eingeschaltet bleibt.
:::

### Python unter Linux

<span class="anker" id="stufe-3-3"></span>

Die meisten Linux-Systeme bringen Python mit, weil Teile des Systems selbst in Python geschrieben sind. Unter Linux heißt der Befehl `python3`.

**Prüfen.** Unter Ubuntu 26.04 ist Python 3.14 vorinstalliert:

```console Linux
$ python3 --version
Python 3.14.4
```

Den Befehl `python` ohne die 3 gibt es dort nicht. Ubuntu antwortet mit einem Hinweis:

```console Linux
$ python --version
Command 'python' not found, did you mean:
  command 'python3' from deb python3
  command 'python' from deb python-is-python3
```

In diesem Kapitel steht unter Linux deshalb immer `python3`.

**Falls Python fehlt.** Auf sehr knapp eingerichteten Systemen kann Python fehlen. Unter Ubuntu und Debian installiert es dieser Befehl:

```console Linux
$ sudo apt install python3
```

Darin ist `apt` die Paketverwaltung von Ubuntu: Sie lädt Programme aus geprüften Quellen und installiert sie. Das vorangestellte `sudo` führt den Befehl mit Verwalterrechten aus und fragt dazu nach deinem Passwort.

:::warnung Das Python des Systems nicht entfernen oder ersetzen
Unter Linux benutzt das System selbst sein Python. Auf dem Ubuntu-Rechner, mit dem dieses Kapitel geprüft wurde, würde die Paketverwaltung beim Entfernen von `python3` über hundert weitere Pakete mit entfernen, darunter die Befehlshilfe, die im Beispiel oben `python3` vorgeschlagen hat. Wer `python3` entfernt oder durch eine selbst gebaute Version ersetzt, kann diese Teile des Systems beschädigen. Lass das System-Python also so, wie es ist. Brauchst du einmal eine andere Version, installiere sie zusätzlich, ohne das vorhandene `python3` anzutasten.
:::

⁠**Kurz gesagt:** Unter Linux ist Python meist schon da und heißt `python3`.

:::hintergrund Warum der Befehl unter Linux `python3` heißt
Python 3 erschien 2008 und war bewusst nicht vollständig mit Python 2 verträglich: Manche Programme für Python 2 laufen unter Python 3 nicht. Viele Linux-Systeme hatten zu dieser Zeit eigene Werkzeuge in Python 2 geschrieben, die mit dem Befehl `python` gestartet wurden. Hätte man `python` einfach auf Python 3 umgestellt, wären sie kaputtgegangen. Deshalb bekam Python 3 den eigenen Befehl `python3`, und eine Empfehlung des Python-Projekts für Linux-Systeme legte fest, dass `python3` immer ein Python 3 startet.

Python 2 wird seit dem 1. Januar 2020 nicht mehr gepflegt. Seitdem lassen viele Systeme den Befehl `python` einfach weg, statt ihn auf eine der beiden Versionen zeigen zu lassen. Wer ihn trotzdem haben will, installiert unter Ubuntu das kleine Paket `python-is-python3`; es macht `python` zu einem zweiten Namen für `python3`.
:::

### Die Versionsnummer

<span class="anker" id="stufe-3-4"></span>

Python entwickelt sich weiter: Neue Versionen bringen neue Sprachmittel und bessere Fehlermeldungen. Damit du weißt, was dein Python kann, solltest du seine Version kennen.

:::definition Definition 3.2 (Versionsnummer)
<span class="anker" id="satz-3-2"></span>

Eine Python-__Versionsnummer__ hat die Form `3.14.4` und besteht aus drei Teilen:

<ul>

<li>

der Hauptversion, hier 3;

</li>

<li>

der Unterversion, hier 14; jedes Jahr im Oktober erscheint eine neue Unterversion mit neuen Sprachmitteln;

</li>

<li>

der Fehlerbehebungsnummer, hier 4; sie wächst, wenn eine Unterversion Korrekturen bekommt, ohne dass sich die Sprache ändert.

</li>

</ul>
:::

Versionsnummern vergleicht man Teil für Teil von links, nicht als Dezimalzahl: 3.14 ist neuer als 3.9, weil 14 größer ist als 9.

**Beispiel.** Der Prüfrechner unter Windows meldet `Python 3.13.9`, der unter Linux `Python 3.14.4`. Beide haben die Hauptversion 3; die Linux-Version ist eine Unterversion neuer. Im November 2026 ist 3.15 die neueste Unterversion, 3.14 erhält noch Fehlerbehebungen, 3.13 nur noch Sicherheitskorrekturen. Alle Beispiele dieses Kapitels laufen ab Python 3.12; ausprobiert sind sie unter Windows mit Python 3.13 und unter Linux mit Python 3.14. Wo sich die Ausgaben der beiden Versionen unterscheiden, steht es dabei.

⁠**Kurz gesagt:** Die Versionsnummer sagt, welches Python du hast; man vergleicht sie Teil für Teil.

:::hintergrund Wie lange eine Python-Version gepflegt wird
Seit Python 3.9 im Oktober 2020 erscheint jedes Jahr im Oktober eine neue Unterversion. Jede wird etwa fünf Jahre gepflegt: zuerst bekommt sie alle paar Monate Fehlerbehebungen, später nur noch Korrekturen von Sicherheitslücken, danach gar nichts mehr. Python 3.10 etwa wurde im Oktober 2026 eingestellt. Der feste Rhythmus macht planbar, wann man auf eine neue Version umsteigen sollte. Eine Version ohne Pflege läuft weiter, bekannte Sicherheitslücken werden darin aber nicht mehr geschlossen.
:::

### Aufgaben zu Abschnitt [3](#stufe-3)

<span class="anker" id="stufe-3-5"></span>

:::aufgabe Aufgabe 7 ★ Python einrichten und prüfen
<span class="anker" id="aufg-7"></span>

<ol class="al">

<li>

Öffne ein Terminal und gib `echo Hallo` ein.

</li>

<li>

Richte Python ein, falls es fehlt: unter Windows mit dem Python install manager, unter Linux mit der Paketverwaltung.

</li>

<li>

Lass dir die Versionsnummer anzeigen: `py --version` unter Windows, `python3 --version` unter Linux. Notiere sie. Ist sie mindestens 3.12?

</li>

<li>

Nur Windows: Was zeigt `py list`? Falls eine Warnung erscheint, löse das Problem wie in Unterabschnitt [3.2](#stufe-3-2) beschrieben.

</li>

</ol>

:::loesung
(a) Das Terminal antwortet mit `Hallo`.

(b) und (c) Auf den Prüfrechnern dieses Kapitels:

```console Windows (PowerShell)
PS> py --version
Python 3.13.9
```

```console Linux
$ python3 --version
Python 3.14.4
```

Beide Versionen sind mindestens 3.12, genügen also für diese Reihe. Deine Nummer kann eine andere sein; wichtig ist nur, dass die Unterversion mindestens 12 ist.

(d) Mit dem Python install manager zeigt `py list` eine Liste der installierten Versionen und kennzeichnet die Standardversion. Erscheint stattdessen die Warnung über „legacy py.exe command“, ist noch der alte „Python Launcher“ installiert. Deinstalliere ihn unter Einstellungen, „Installierte Apps“; danach antwortet `py list` mit der Liste.
:::
:::

:::aufgabe Aufgabe 8 ★ Versionen ordnen
<span class="anker" id="aufg-8"></span>

Ordne die Versionsnummern von alt nach neu: `3.14.10`, `3.9.18`, `3.13.9`, `3.14.4`, `3.12.0`. Welche davon erfüllen die Anforderung „ab Python 3.12“? Warum führt es in die Irre, die Nummern als Dezimalzahlen zu lesen?

:::loesung
Von alt nach neu: `3.9.18`, `3.12.0`, `3.13.9`, `3.14.4`, `3.14.10`. Bis auf `3.9.18` erfüllen alle die Anforderung „ab 3.12“.

Man vergleicht Teil für Teil von links: Die Hauptversion ist überall 3; bei der Unterversion ist 9 kleiner als 12, 13 und 14; bei gleicher Unterversion 14 entscheidet die dritte Zahl, und 4 ist kleiner als 10. Als Dezimalzahl gelesen wäre 3,9 größer als 3,14, weil $0{,}9>0{,}14$; und 3.14.10 sähe aus wie eine kleinere Zahl als 3.14.4. Beides ist falsch, weil jeder Teil eine eigene ganze Zahl ist und kein Nachkommaanteil.
:::
:::

:::aufgabe Aufgabe 9 ★★ Fehlersuche bei der Einrichtung
<span class="anker" id="aufg-9"></span>

Erkläre jeweils, was die Ursache ist und was du tust.

<ol class="al">

<li>

Unter Windows öffnet `python` den Microsoft Store, obwohl du den Python install manager installiert hast.

</li>

<li>

Unter Ubuntu antwortet `python hallo.py` mit „Command 'python' not found“.

</li>

<li>

Unter Windows antwortet `py list` mit einer Warnung über „legacy py.exe command“.

</li>

</ol>

:::loesung
(a) Der Platzhalter von Windows, der den Store öffnet, hat Vorrang vor dem Befehl des install managers. Öffne im Startmenü „App-Ausführungsaliase verwalten“ und sorge dafür, dass die Einträge „Python (default)“ des install managers eingeschaltet sind. Alternativ benutzt du `py`, wie in diesem Kapitel.

(b) Unter Ubuntu gibt es den Befehl `python` nicht, nur `python3`. Richtig ist `python3 hallo.py`. Wer unbedingt `python` tippen will, installiert das Paket `python-is-python3`.

(c) Der alte „Python Launcher“ aus dem früheren Installationsprogramm ist installiert und überdeckt den neuen Befehl `py`. Deinstalliere ihn unter Einstellungen, „Installierte Apps“. Bis dahin erreicht man den install manager auch unter dem zweiten Namen `pymanager`, also mit `pymanager list`.
:::
:::

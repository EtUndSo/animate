---
title: Code und Daten im selben Speicher
pfad: Informatik / Cybersecurity / Schutzgrenzen in Hardware und Betriebssystem
adresse: informatik/cybersecurity/schutzgrenzen-in-hardware-und-betriebssystem
knoten: Kapitel 2: Schutzgrenzen in Hardware und Betriebssystem
order: 6120300
summary: Ein Programm besteht aus Befehlen, und es arbeitet mit Daten.
tags: Arbeitsspeicher, Adresse, Register, Befehlszeiger, Von-Neumann-Prinzip
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Ein Programm besteht aus Befehlen, und es arbeitet mit Daten. Dieser Abschnitt zeigt, wie der Prozessor Befehle findet und ausführt, und dass Befehle und Daten im selben Speicher liegen. Daraus folgt eine Eigenschaft, die für die Sicherheit grundlegend ist: Für den Prozessor ist alles nur Speicher.
:::

:::::vorwissen Was du dafür brauchst: Byte, Hexadezimalzahl und Adresse

<span class="anker" id="stufe-2-1"></span>

Ein Byte sind acht Bit; als vorzeichenlose Binärzahl gelesen fasst es die Werte 0 bis 255 ([Python, Kapitel 2, Abschnitt 3.3](/wissen/informatik/programmieren/python/werte-typen-und-variablen/zahlen-im-binarsystem.html#stufe-3-3)). In der Hexadezimalschreibweise steht jede Ziffer `0` bis `9`, `a` bis `f` für vier Bit, ein Byte also für genau zwei Ziffern; die Vorsilbe `0x` kennzeichnet die Schreibweise, etwa $\texttt{0x2a}=2\cdot16+10=42$ ([Python, Kapitel 2, Abschnitt 3.5](/wissen/informatik/programmieren/python/werte-typen-und-variablen/zahlen-im-binarsystem.html#stufe-3-5)).

Neu ist die Adresse. Der Arbeitsspeicher eines Rechners ist eine sehr lange Reihe von Bytes, so wie eine Straße eine Reihe von Häusern ist.

:::definition Definition 2.1 (Arbeitsspeicher, Adresse)
<span class="anker" id="satz-2-1"></span>

Der __Arbeitsspeicher__ ist der Speicher, in dem Programme und ihre Daten liegen, während sie laufen; der Prozessor kann jedes seiner Bytes direkt lesen und schreiben. Jedes Byte hat eine Nummer, seine __Adresse__. Adressen schreibt man meist hexadezimal.
:::

Ein Wert, der mehrere Bytes braucht, belegt mehrere aufeinanderfolgende Adressen. Auf einem Rechner mit 64-Bit-Prozessor sind Adressen 64 Bit lang; die Werkzeuge schreiben sie mit bis zu 16 Hexadezimalziffern. Abbildung [5](#abb-5) zeigt den Speicher als Reihe von Bytes.

:::abbildung cyber/k2adressen 5
Eine waagerechte Reihe von acht Kästchen wie Häuser an einer Straße, darin Bytes in Hexadezimalschreibweise, darunter ihre Adressen `0x1000` bis `0x1007`. Zuerst erscheinen die Kästchen, dann die Hausnummern. Ein Zeiger springt auf `0x1000`: Das Byte `2a` leuchtet auf, daneben „$2\cdot16+10=42$“. Dann auf `0x1001`: `c3`, „$12\cdot16+3=195$“. Zum Schluss klammert eine Klammer vier aufeinanderfolgende Bytes ab `0x1004` ein: „ein Wert aus vier Bytes belegt vier Adressen“.
:::

::::beispiel Bytes an Adressen
An der Adresse `0x1000` steht das Byte `0x2a`, an `0x1001` das Byte `0xc3`. Als Zahlen gelesen sind das 42 und $12\cdot16+3=195$. Die Adresse des zweiten Bytes ist um eins größer als die des ersten, denn jedes Byte hat seine eigene Nummer.
::::

⁠**Kurz gesagt:** Der Arbeitsspeicher ist eine Reihe von Bytes, und die Adresse ist die Nummer eines Bytes.

:::::

### Der Befehlszeiger

<span class="anker" id="stufe-2-2"></span>

Ein Programm ist für den Prozessor eine Folge von Maschinenbefehlen, und jeder Befehl ist ein paar Bytes lang. Woher weiß der Prozessor, welchen Befehl er als Nächstes ausführen soll?

Man kann sich einen Koch vorstellen, der ein Rezept Zeile für Zeile abarbeitet und ein Lesezeichen an die nächste Zeile legt. Steht in einer Zeile „weiter bei Schritt 2“, legt er das Lesezeichen dorthin. Das ist ein Bild zur Orientierung; im Prozessor gibt es dafür einen eigenen Speicherplatz.

:::definition Definition 2.2 (Register, Befehlszeiger)
<span class="anker" id="satz-2-2"></span>

Ein __Register__ ist ein sehr schneller Speicherplatz im Prozessor selbst; ein x86-64-Prozessor hat 16 allgemeine Register zu je 64 Bit und einige besondere. Der __Befehlszeiger__ ist ein besonderes Register, das die Adresse des nächsten auszuführenden Befehls enthält; bei x86-64 heißt es `rip`.
:::

Der Prozessor arbeitet in einem festen Kreislauf, dem Befehlszyklus:

<ol>

<li>

Er holt den Befehl, der an der Adresse im Befehlszeiger steht.

</li>

<li>

Er erhöht den Befehlszeiger um die Länge dieses Befehls, sodass er auf den folgenden Befehl zeigt.

</li>

<li>

Er führt den Befehl aus. Ein Sprungbefehl setzt dabei den Befehlszeiger auf ein neues Ziel.

</li>

</ol>

Dann beginnt der Kreislauf von vorn. Abbildung [6](#abb-6) zeigt ihn an drei Befehlen.

:::abbildung cyber/k2zyklus 6
Ein Speicherstreifen mit Adressen `0x401000` bis `0x40100a`, darin drei Befehle als Kästen: A (5 Byte), B (3 Byte), C „springe nach 0x401000“ (2 Byte). Darüber das Register `rip`. Ein Pfeil vom Register zeigt nacheinander auf A, B und C; das Register zeigt dabei `0x401000`, `0x401005`, `0x401008`. Nach C springt der Pfeil zurück auf A und das Register zeigt wieder `0x401000`. Neben dem Streifen dreht sich ein kleiner Kreis „holen, weitersetzen, ausführen“.
:::

::::beispiel Der Befehlszeiger bei drei Befehlen
Befehl A steht ab `0x401000` und ist 5 Byte lang, Befehl B steht ab `0x401005` und ist 3 Byte lang, Befehl C steht ab `0x401008` und springt nach `0x401000`. Der Befehlszeiger durchläuft die Werte `0x401000` (A wird geholt), $\texttt{0x401000}+5=\texttt{0x401005}$ (B wird geholt), $\texttt{0x401005}+3=\texttt{0x401008}$ (C wird geholt). Nach dem Holen von C steht er zunächst auf $\texttt{0x40100a}$; erst das Ausführen des Sprungs setzt ihn auf `0x401000`. Die drei Befehle laufen so immer wieder.
::::

⁠**Kurz gesagt:** Der Prozessor führt stets den Befehl aus, auf den der Befehlszeiger zeigt, und setzt ihn danach weiter oder, bei einem Sprung, auf ein neues Ziel.

:::hintergrund Arbeitet ein Prozessor wirklich einen Befehl nach dem anderen ab?
Im Inneren nicht. Heutige Prozessoren holen viele Befehle im Voraus, bearbeiten mehrere gleichzeitig und führen manche sogar in anderer Reihenfolge oder auf Verdacht aus. Sie sind aber so gebaut, dass das *sichtbare* Ergebnis genau dem Kreislauf oben entspricht: Was ein Programm von seinen Registern und seinem Speicher sieht, ist so, als wäre ein Befehl nach dem anderen ausgeführt worden. Das Modell beschreibt also das Verhalten exakt, nicht den Bau.
:::

### Das Von-Neumann-Prinzip

<span class="anker" id="stufe-2-3"></span>

Wo liegen die Befehle eines Programms, während es läuft? Die Antwort ist so selbstverständlich geworden, dass man sie kaum noch bemerkt: im selben Arbeitsspeicher wie die Daten, mit denen das Programm rechnet.

:::definition Definition 2.3 (Von-Neumann-Prinzip)
<span class="anker" id="satz-2-3"></span>

Nach dem __Von-Neumann-Prinzip__, auch Prinzip des gespeicherten Programms genannt, liegen Befehle und Daten im selben Speicher und in derselben Darstellung, als Bytes an Adressen. Ob ein Byte ein Befehl ist, entscheidet allein, ob der Befehlszeiger darauf zeigt.
:::

Abbildung [7](#abb-7) zeigt einen Speicher, in dem Befehle und Daten nebeneinander liegen. Die Bytes selbst tragen keine Kennzeichnung, was sie sind.

:::abbildung cyber/k2vonneumann 7
Ein Prozessor oben mit dem Register `rip`, darunter ein einziger Speicherstreifen. Im Streifen liegen links Bytes, die ein Programm als Befehle benutzt, rechts Bytes, die es als Zahlen benutzt; alle sehen gleich aus, nur hexadezimale Werte. Zuerst erscheinen die Bytes ohne Farbe. Dann zeigt der Pfeil von `rip` auf die linken Bytes, und sie färben sich als „Befehl“; ein zweiter Pfeil „lesen/schreiben“ geht auf die rechten Bytes, sie färben sich als „Daten“. Ein Byte `c3` kommt in beiden Teilen vor.
:::

::::beispiel Ein Byte, zwei Bedeutungen
Das Byte `0xc3` ist als Zahl gelesen 195. Zeigt der Befehlszeiger darauf, versteht ein x86-64-Prozessor es als vollständigen Befehl: „kehre aus der laufenden Funktion zurück“. Im Speicher unterscheidet nichts die beiden Fälle. Ein Programm, das eine Liste von Punkteständen verwaltet, kann den Wert 195 an einer Adresse speichern, und ein Sprung genau dorthin würde ihn als Rücksprungbefehl ausführen.
::::

⁠**Kurz gesagt:** Befehle und Daten sind Bytes im selben Speicher; zum Befehl wird ein Byte erst, wenn der Befehlszeiger darauf zeigt.

:::hintergrund Warum fast alle Rechner Befehle und Daten mischen
Ein Programm zu starten heißt: die Bytes des Programms aus einer Datei lesen, sie als gewöhnliche Daten in den Arbeitsspeicher schreiben und dann den Befehlszeiger dorthin setzen. Das geht nur, weil Befehle Daten sind. Ein Übersetzer, der aus Quelltext Maschinenbefehle macht, schreibt seine Ausgabe ebenfalls als Daten. Ein Speicher für alles ist außerdem einfacher und flexibler: Jedes Programm nimmt sich so viel Platz für Befehle oder Daten, wie es braucht. John von Neumann beschrieb diese Bauweise 1945 in einem Bericht über einen der ersten speicherprogrammierten Rechner; seither bauen die meisten Rechner so.

Das Gegenmodell heißt *Harvard-Architektur*: Befehle und Daten liegen in getrennten Speichern mit getrennten Zugriffswegen. Dort kann ein Byte aus dem Datenspeicher grundsätzlich nicht als Befehl ausgeführt werden. Heutige PC-Prozessoren haben zwar intern getrennte Zwischenspeicher für Befehle und Daten, für Programme sieht der Arbeitsspeicher aber aus wie ein einziger Speicher für beides.
:::

### Wenn Daten zu Befehlen werden

<span class="anker" id="stufe-2-4"></span>

Aus dem Von-Neumann-Prinzip folgt etwas, das zunächst harmlos klingt.

:::satz Satz 2.4 (Daten können als Befehle laufen)
<span class="anker" id="satz-2-4"></span>

Der Prozessor prüft nicht, ob Bytes als Befehle gemeint waren. Zeigt der Befehlszeiger auf Bytes, die ein Programm als Daten in den Speicher geschrieben hat, so führt der Prozessor sie als Befehle aus.
:::

Das lässt sich am eigenen Rechner zeigen, mit einem kleinen Programm in Python. In einem Satz: Das Programm holt sich vom Kernel ein Stück Speicher, schreibt sechs Bytes hinein und lässt den Prozessor dort weiterarbeiten. Python musst du dafür nicht kennen, du benutzt das Programm wie ein Rezept; die Zeilen mit `#` sind Kommentare und sagen, was es tut. Wer die Sprache lernen möchte, beginnt mit [Python, Kapitel 1](/wissen/informatik/programmieren/python/programme-und-der-python-interpreter/programme-und-der-python-interpreter.html). Das Programm benutzt die Programmbibliothek `ctypes`, mit der Python die Grundfunktionen aufrufen kann, die unter Linux fast jedes Programm benutzt. Lege es mit dem Editor `nano` ([Linux, Kapitel 3, Abschnitt 5.3](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-und-verzeichnisse-anlegen.html#stufe-5-3)) als `befehl.py` in deinem Übungsverzeichnis an:

```python befehl.py
# befehl.py: schreibt Maschinenbefehle als Daten in ein Speicherstück
# und lässt den Prozessor dorthin springen. Nur für x86-64 unter Linux.
import ctypes, mmap, sys

BEFEHLE = {
    "rechnen":  bytes([0xB8, 0x2A, 0x00, 0x00, 0x00, 0xC3]),  # 42 als Ergebnis, zurück
    "anhalten": bytes([0xF4, 0xC3]),                        # Prozessor anhalten, zurück
}
art = sys.argv[1]                                  # rechnen oder anhalten
rechte = sys.argv[2] if len(sys.argv) > 2 else ""  # leer, rx oder rw

libc = ctypes.CDLL(None)                           # die C-Bibliothek des Systems
libc.mmap.restype = ctypes.c_void_p
libc.mmap.argtypes = [ctypes.c_void_p, ctypes.c_size_t, ctypes.c_int,
                      ctypes.c_int, ctypes.c_int, ctypes.c_long]
libc.mprotect.argtypes = [ctypes.c_void_p, ctypes.c_size_t, ctypes.c_int]

# 1. Ein neues Speicherstück (4096 Byte) vom Kernel holen: lesbar und schreibbar.
stueck = libc.mmap(None, mmap.PAGESIZE, mmap.PROT_READ | mmap.PROT_WRITE,
                   mmap.MAP_PRIVATE | mmap.MAP_ANONYMOUS, -1, 0)
# 2. Die Bytes als gewöhnliche Daten hineinschreiben.
ctypes.memmove(stueck, BEFEHLE[art], len(BEFEHLE[art]))
# 3. Außer bei "rw": den Kernel bitten, das Stück ausführbar statt schreibbar zu machen.
if rechte != "rw":
    libc.mprotect(stueck, mmap.PAGESIZE, mmap.PROT_READ | mmap.PROT_EXEC)
# 4. Bei "rx" oder "rw": die Rechte des Stücks aus /proc/self/maps zeigen.
if rechte:
    for zeile in open("/proc/self/maps"):
        von, bis = [int(x, 16) for x in zeile.split()[0].split("-")]
        if von <= stueck < bis:
            print(f"Stück {stueck:#x}: Rechte {zeile.split()[1]}")
# 5. Den Befehlszeiger auf das Stück setzen: die Bytes als Funktion aufrufen.
sys.stdout.flush()
ergebnis = ctypes.CFUNCTYPE(ctypes.c_int)(stueck)()
print("Ergebnis:", ergebnis)
```

Für diesen Abschnitt zählen die Schritte 1, 2 und 5. Das Programm holt sich ein Stück Speicher, schreibt sechs Bytes hinein, wie es jede Zahl hineinschreiben würde, und setzt dann den Befehlszeiger auf diese Bytes (Abbildung [8](#abb-8)). Die Schritte 3 und 4 betreffen die Rechte des Speicherstücks; ohne zweite Angabe erledigt das Programm Schritt 3 von selbst und lässt Schritt 4 aus. Die Bytes `B8 2A 00 00 00` bedeuten für einen x86-64-Prozessor „lege die Zahl `0x2a` als Ergebnis bereit“, das letzte Byte `C3` ist der Rücksprung aus dem Beispiel in Unterabschnitt [2.3](#stufe-2-3). Das Programm läuft nur auf Rechnern mit x86-64-Prozessor; `uname -m` muss `x86_64` melden.

Das Programm ist harmlos. Es verändert nur das Stück Speicher, das es sich eben selbst vom Kernel geholt hat, und benutzt dafür nur Wege, die der Kernel jedem Programm anbietet. Es öffnet keine Netzverbindung, schreibt keine Datei, umgeht keinen Schutz und hinterlässt nichts: Mit dem Ende des Prozesses verschwindet auch das Speicherstück. Der schlimmste mögliche Ausgang ist, dass der Kernel das Programm selbst beendet.

:::abbildung cyber/k2datenbefehle 8
Drei Schritte von `befehl.py`. Schritt 1: Ein leeres Speicherstück erscheint (lauter `00`). Schritt 2: Ein Pfeil „schreiben (als Daten)“ vom Python-Programm füllt die ersten sechs Bytes mit `B8 2A 00 00 00 C3`; sie sehen aus wie jede andere Zahlenliste. Schritt 5: Das Register `rip` zeigt auf das erste Byte, die sechs Bytes färben sich als „Befehl“, der Prozessor rechnet, und rechts erscheint „Ergebnis: 42“.
:::

::::beispiel Sechs Bytes Daten laufen als Befehl
```console
$ uname -m
x86_64
$ python3 befehl.py rechnen
Ergebnis: 42
```

Die Zahl 42 hat keine Zeile des Python-Programms berechnet. Sie stammt aus dem Befehl, den der Prozessor in den sechs Bytes gefunden hat, nachdem der Befehlszeiger auf sie gesetzt wurde. Python hat die Bytes vorher geschrieben wie jede andere Zahlenliste.
::::

⁠**Kurz gesagt:** Was als Daten in den Speicher geschrieben wurde, läuft als Befehl, sobald der Befehlszeiger darauf zeigt.

:::hintergrund Warum das die Wurzel von eingeschleustem Code ist
Viele Programme schreiben Daten in ihren Speicher, die von außen kommen: eine Nachricht aus dem Netz, ein Bild aus einer Datei, eine Eingabe aus einem Formular. Solange das Programm diese Bytes nur als Daten liest, schadet das nicht. Gelingt es einem Angreifer aber, durch einen Fehler im Programm den Befehlszeiger auf genau diese Bytes zu lenken, laufen sie als Befehle, und zwar mit allen Rechten des Programms. Das ist dasselbe Muster wie bei der Shell, die einen Dateinamen als Steuerzeichen deutet ([Linux, Kapitel 5, Abschnitt 3.8](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/worttrennung-und-quoting.html#stufe-3-8)): Daten werden zu Steuerung. Der Prozessor kann sich nicht selbst davor schützen, denn den Bytes sieht man nicht an, woher sie stammen; die Information „das waren Daten“ steht nirgends im Speicher. Will man die Grenze zwischen Code und Daten zurück, muss sie jemand anderes ziehen.
:::

### Aufgaben zu Abschnitt [2](#stufe-2)

<span class="anker" id="stufe-2-5"></span>

:::aufgabe Aufgabe 3 ★ Den Befehlszeiger verfolgen
<span class="anker" id="aufg-3"></span>

Ab der Adresse `0x401000` stehen vier Befehle: P (4 Byte), Q (7 Byte), R (2 Byte, springt nach `0x401004`) und S (3 Byte). Gib die Adressen aller vier Befehle an. Welche Werte nimmt der Befehlszeiger in den ersten sechs Durchläufen des Befehlszyklus jeweils beim Holen an? Wird S jemals ausgeführt?

:::loesung
Die Befehle beginnen an `0x401000` (P), $\texttt{0x401000}+4=\texttt{0x401004}$ (Q), $\texttt{0x401004}+7=\texttt{0x40100b}$ (R) und $\texttt{0x40100b}+2=\texttt{0x40100d}$ (S). Beim Holen nimmt der Befehlszeiger nacheinander diese Werte an:

$$\texttt{0x401000},\ \texttt{0x401004},\ \texttt{0x40100b},\ \texttt{0x401004},\ \texttt{0x40100b},\ \texttt{0x401004}.$$

Nach P und Q kommt R, und R setzt den Befehlszeiger auf `0x401004` zurück. Von da an laufen Q und R immer abwechselnd. S steht zwar im Speicher, wird aber nie geholt und nie ausgeführt: Der Befehlszeiger erreicht `0x40100d` nicht, weil R jedes Mal vorher springt.
:::
:::

:::aufgabe Aufgabe 4 ★★ Woher kam die 42?
<span class="anker" id="aufg-4"></span>

Führe `python3 befehl.py rechnen` aus. (a) Wo standen die sechs Bytes, bevor das Programm lief, und wo nach Schritt 2? (b) Was hat sie in Schritt 5 zum Befehl gemacht? (c) Ändere im Programm die Zahl `0x2A` in `0x07` und sage die Ausgabe voraus, bevor du es ausführst.

:::loesung
(a) Vor dem Lauf standen die sechs Bytes als Text im Programm, als Liste `[0xB8, 0x2A, ...]` in der Datei `befehl.py`. Beim Start hat Python daraus ein Objekt mit sechs Bytes in seinem eigenen Speicher gemacht. In Schritt 2 hat `ctypes.memmove` diese Bytes in das neue Speicherstück kopiert, wie es jede andere Zahlenfolge kopiert hätte.

(b) In Schritt 5 behandelt das Programm die Adresse des Stücks als Funktion und ruft sie auf. Dabei setzt der Prozessor den Befehlszeiger auf das erste Byte des Stücks. Erst das macht die Bytes zu Befehlen: Der Prozessor holt `B8 2A 00 00 00` als Befehl „lege `0x2a` als Ergebnis bereit“ und `C3` als Rücksprung.

(c) Mit `0x07` statt `0x2A` legt der Befehl die Zahl 7 als Ergebnis bereit. Auf dem Testsystem, mit einer geänderten Kopie des Programms:

```console
$ sed 's/0x2A, 0x00/0x07, 0x00/' befehl.py > befehl7.py
$ python3 befehl7.py rechnen
Ergebnis: 7
```
:::
:::

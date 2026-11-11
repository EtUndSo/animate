---
title: Das Wichtigste bis hier
pfad: Informatik / Linux und Kommandozeile / Dateien, Verzeichnisse und Pfade
adresse: informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade
knoten: Kapitel 3: Dateien, Verzeichnisse und Pfade
order: 6081200
summary: Der Verzeichnisbaum, Dateien anlegen, ansehen, kopieren und löschen, was hinter einem Dateinamen steckt und wie man Dateien wiederfindet
tags: 
lang: de
---

:::kern Das Wichtigste bis hier
<ul>

<li>

Eine Datei ist eine gespeicherte Folge von Bytes, ein Verzeichnis eine Liste von Einträgen. Alle Verzeichnisse hängen in einem einzigen Baum mit der Wurzel `/`; weitere Dateisysteme werden an Verzeichnisse eingehängt, statt einen Laufwerksbuchstaben zu bekommen.

</li>

<li>

Ein Pfad beschreibt einen Weg durch den Baum: absolut ab `/`, relativ ab dem Arbeitsverzeichnis. `.` ist das Verzeichnis selbst, `..` das übergeordnete, `~` das Heimatverzeichnis; `pwd` zeigt den Standort, `cd` wechselt ihn.

</li>

<li>

`ls` zeigt Einträge, mit `-a` auch versteckte, mit `-F` ihre Art, mit `-l` Art, Rechte, Linkzähler, Besitzer, Größe und Zeit, mit `-h` lesbare Größen. Dateinamen dürfen alles außer `/` und dem Nullbyte enthalten und unterscheiden Groß und Klein.

</li>

<li>

`cat`, `less`, `head`, `tail` und `wc` zeigen und vermessen Textdateien; `file` bestimmt die Art einer Datei aus ihren ersten Bytes, nicht aus der Endung.

</li>

<li>

`mkdir -p`, `touch` und `nano` legen an; `cp`, `cp -r` und `mv` kopieren und verschieben und überschreiben dabei ohne Rückfrage; `rm`, `rm -r` und `rmdir` löschen endgültig. Muster mit `*`, `?` und `[…]` ersetzt die Shell vor dem Start durch passende Namen.

</li>

<li>

Der FHS ordnet das System: Programme in `/usr`, Einstellungen in `/etc`, Benutzer in `/home`, Veränderliches in `/var`, Vorübergehendes in `/tmp`, Geräte in `/dev`, Angaben des Kernels in `/proc` und `/sys`.

</li>

<li>

Ein Verzeichniseintrag verbindet einen Namen mit einer Inode, die alle übrigen Angaben enthält. Ein harter Link ist ein weiterer Name derselben Inode, ein symbolischer Link eine Datei mit einem Pfad; `rm` entfernt nur einen Namen, die Daten verschwinden mit dem letzten.

</li>

<li>

`lsblk`, `findmnt` und `df` zeigen Datenträger, Einhängepunkte und Belegung; `find` sucht nach Name, Art, Größe und Alter, `du` zählt belegte Blöcke.

</li>

</ul>
:::

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Linux ordnet alle Dateien in einem einzigen Baum, in dem jeder Ort einen Pfad hat und jeder weitere Datenträger an einem Verzeichnis eingehängt ist; der FHS legt fest, welches Verzeichnis wofür da ist.

</li>

<li>

Mit Pfaden und wenigen Befehlen bewegt man sich durch diesen Baum, sieht Dateien an, legt sie an, kopiert, verschiebt und löscht sie, wählt viele auf einmal mit Mustern und findet sie mit `find` wieder.

</li>

<li>

Ein Dateiname ist dabei nur ein Eintrag in einem Verzeichnis, der auf eine Inode zeigt; daraus folgen harte und symbolische Links, das sofortige `mv` und das endgültige `rm`.

</li>

</ol>
:::

**Ein Prinzip hinter allen Ergebnissen.** Fast alles in diesem Kapitel folgt aus einem Gedanken: Namen und Dateien sind getrennt. Eine Datei ist eine Inode mit Datenblöcken, ein Name nur ein Eintrag in einer Liste, die selbst wieder eine Datei ist, und der ganze Baum ist ein Netz solcher Listen, über Datenträger hinweg durch Einhängen verbunden.

| Ergebnis | Woher es kommt |
|---|---|
| es gibt keine Laufwerksbuchstaben | weitere Dateisysteme werden an Verzeichnisse des einen Baums eingehängt (Abschnitte [1](dateien-verzeichnisse-und-der-verzeichnisbaum.html#stufe-1) und [9](datentrager-und-einhangen.html#stufe-9)) |
| `cd ..` in `/` bleibt in `/` | `..` ist ein Eintrag, der in der Wurzel auf die Wurzel selbst zeigt (Abschnitt [2](das-arbeitsverzeichnis-und-pfade.html#stufe-2)) |
| derselbe relative Pfad führt an zwei Orten zu verschiedenen Dateien | der Kernel löst ihn ab dem Arbeitsverzeichnis auf (Abschnitt [2](das-arbeitsverzeichnis-und-pfade.html#stufe-2)) |
| eine versteckte Datei erscheint im gewöhnlichen `ls` erst nach dem Umbenennen | „versteckt“ ist nur eine Regel für Namen mit Punkt (Abschnitt [3](den-inhalt-eines-verzeichnisses-anzeigen.html#stufe-3)) |
| `file` erkennt ein Bild auch unter dem Namen `urlaub.txt` | die Art steckt in den ersten Bytes, der Name ist nur ein Eintrag (Abschnitt [4](dateien-ansehen.html#stufe-4)) |
| `ls` bekommt nie ein Muster zu sehen | die Shell ersetzt es vorher durch Namen aus dem Verzeichnis (Abschnitt [6](kopieren-verschieben-loschen.html#stufe-6)) |
| `mv` einer großen Datei ist sofort fertig | es hängt nur einen Eintrag um, die Inode bleibt (Abschnitte [6](kopieren-verschieben-loschen.html#stufe-6) und [8](inode-und-links.html#stufe-8)) |
| `/proc/version` hat die Größe 0 und doch Inhalt | der Kernel erzeugt die Datei erst beim Lesen (Abschnitt [7](die-verzeichnisstruktur-von-linux.html#stufe-7)) |
| ein Verzeichnis mit zwei Unterverzeichnissen hat den Linkzähler 4 | sein Eintrag, sein `.` und zwei `..` zeigen auf seine Inode (Abschnitt [8](inode-und-links.html#stufe-8)) |
| nach `rm` des Originals ist der harte Link noch lesbar | `rm` entfernt nur einen Namen, die Inode lebt bis zum letzten (Abschnitt [8](inode-und-links.html#stufe-8)) |
| es gibt keinen Papierkorb | `rm` ruft `unlink` auf, ein Papierkorb wäre ein Verschieben (Abschnitte [6](kopieren-verschieben-loschen.html#stufe-6) und [8](inode-und-links.html#stufe-8)) |
| ein symbolischer Link kann ins Leere zeigen | er enthält nur einen Pfad, den niemand prüft (Abschnitt [8](inode-und-links.html#stufe-8)) |
| kein harter Link nach `/tmp` oder `/mnt/c` | Inode-Nummern gelten nur im eigenen Dateisystem (Abschnitte [8](inode-und-links.html#stufe-8) und [9](datentrager-und-einhangen.html#stufe-9)) |
| `find . -name *.txt` scheitert | die Shell hat das Muster ersetzt, bevor `find` startete (Abschnitt [10](dateien-finden-und-platz-messen.html#stufe-10)) |
| eine Datei mit 32 Bytes belegt 4 KiB | das Dateisystem teilt Platz in ganzen Blöcken zu (Abschnitt [10](dateien-finden-und-platz-messen.html#stufe-10)) |

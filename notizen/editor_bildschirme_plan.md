# Editor: Bildschirme und Fenster realistisch nachbauen (Vorschlag, 11.11.2026)

Wunsch des Users (11.11.2026): „Wir sollten für den Editor auch Funktionen einbauen, um einen Bildschirm bzw. Fenster darin möglichst realistisch nachbauen zu können. Also für Linux, Programmierung, Einstellungen, etc. Überlege dir, welche Funktionen wir am besten in den Editor einbauen, damit wir alle Fälle abbilden können.“
Stand: Vorschlag, noch nicht beauftragt.
**Entscheidung des Users (11.11.2026):** „Wir warten auf die Fertigstellung der Übersetzungen, dann machen wir die Änderungen am Editor. Wir müssen auch überlegen, wie wir das effizient umsetzen.“ Also erst nach der Englisch-Schleife; vorher den effizienten Weg festlegen (Abschnitt „Effizient umsetzen“ unten).

## Effizient umsetzen (Vorschlag, 11.11.2026)
1. **Nur bauen, was gebraucht wird:** Vor jeder Welle die Szenentabellen der nächsten Hefte auswerten (Linux 7/8: `uebergabe_kap7.md`/`uebergabe_kap8.md`, 58 Szenen; später Cyber 2, Python 4). Daraus entsteht die genaue Funktionsliste; der Rest des Plans bleibt Vorrat.
2. **Einmal bauen, überall nutzen:** Die neuen Vorlagen sind zusammengesetzte Objekte in der Python-Engine (`web/engine`), die beim Zeichnen in vorhandene Grundformen zerfallen. Editor (Pyodide), Export, Vektor-PDF und Spieler nutzen dieselbe Stelle. Kein neuer Renderweg, kaum JavaScript: Das Eigenschaftsfeld des Editors zeigt Props ohnehin generisch, neu sind nur die Palette-Einträge.
3. **Daten statt Handarbeit:** Terminalinhalt als Text mit ANSI-Kürzeln, Formulare als Liste, Stile als Tabellen. Ein Aufruf ersetzt Dutzende `tt`/`ttz`-Zeilen; die Agenten der Hefte sparen Zeit und Kontext.
4. **Klein und schlank im SVG:** Eine Terminalzeile wird ein `<text>` mit farbigen Abschnitten, nicht ein Objekt je Zeichen. Größenbudget je Bild wird beim Export geprüft.
5. **Pilot zuerst:** Drei vorhandene Linux-Szenen (je eine aus Kapitel 2, 4, 6) mit dem neuen Terminal nachbauen und neben die Handfassung legen. Erst wenn das überzeugt, die Welle fertig bauen. Bestehende Szenen werden nicht nachgerüstet (Plan vom 10.11.: Nachrüsten erst in den Nachrüstwellen).
6. **Zwei frische Agenten je Welle,** wie bei den Heften: ein Bau-Agent (API in `notizen/animationen.md`, Tests, Pilot), dann ein Prüf-Agent mit Kontaktblatt und Vertragstests. Kein Agent liest mehr als nötig (API-Teile gezielt).
7. **Gerade rechtzeitig:** F1 direkt nach der Schleife und vor Linux 7/8 2b; F2 in E4 (L8); F3/F4 kurz vor dem ersten Heft, das sie braucht.

## Ausgangslage
- **Linux 2–6:** etwa 1 740 einzeln gesetzte Terminalzeilen (`tt`/`ttz` in `tools/szenen/linux_teil*.py`). Spalten stimmen nur, weil jede Zeile von Hand nach Zeichenbreite gesetzt ist; Farben, Cursor und Rollen gibt es nicht.
- **Programmieren:** Im Abbildungs-Audit fehlt das Code-Objekt mit Zeilenmarke und Variablenstand (L8) in 7 Fällen (`notizen/abbildungen_audit/UEBERSICHT.md`); heute Behelf aus Textzeilen und wanderndem Rechteck.
- **Bedienschritte ohne Bild:** Die Hefte beschreiben Klicks und Dialoge (Startmenü mit Rechtsklick, „Terminal (Administrator)“, VirtualBox „Neu“, Formatieren-Dialog „Abbrechen“), zeigen sie aber nicht.
- **Kommend:**
  - Linux 7: `ls -l`, sudo-Passwortabfrage, Eigenschaften-Dialog.
  - Linux 8: `top`, `systemctl status`, `journalctl`.
  - Cybersecurity: Browser, Zertifikat, Phishing-Mail, Login, Firewall.
  - ML-Pfad: Notebook.
  - Python 4+, C/C++: Editor, Debugger, Dateien.

## Grundidee: drei Ebenen, Inhalt aus echter Quelle
1. **Bausteine:** Fensterteile und Steuerelemente.
2. **Vorlagen:** fertige Fenster, aus den Bausteinen zusammengesetzt (Terminal, Code-Editor, Dialog, Browser …).
3. **Bedien-Ebene:** Maus, Tasten, Lupe; über jedem Inhalt nutzbar.

**Korrektheit:** Terminal-Ausgaben und Programmabläufe kommen aus echten, geprüften Läufen (Mitschriften, echte Ausführung beim Export), nicht abgetippt.

## Ebene 1: Fenster und Bausteine
- **`s.fenster(titel, b, h, stil, dunkel)`:**
  - Rahmen, Titelleiste mit Fensterknöpfen, Schatten und ein Inhaltsbereich mit eigenen Koordinaten.
  - Das Fenster ist eine Gruppe: Es lässt sich als Ganzes einblenden, verschieben, skalieren und schließen.
- **Leisten:** Menüleiste, Werkzeugleiste, Registerkarten (aktiv/inaktiv), Statusleiste, Seitenleiste mit Baum, Bildlaufleiste (animierbar).
- **Steuerelemente:**
  - Knopf (normal, hervorgehoben, gedrückt, gesperrt), Kontrollkästchen, Optionsfeld, Schalter, Auswahlliste (aufklappbar), Textfeld (Platzhalter, Cursor, Passwortpunkte), Schieberegler, Fortschrittsbalken;
  - Tabelle/Liste mit Kopfzeile, Sortierpfeil und markierter Zeile;
  - Tooltip, Kontextmenü, Meldungsdialog (Info, Warnung, Frage mit Knöpfen), Benachrichtigung.
- **Zustände als Animation:** ankreuzen, umschalten, auswählen, tippen, drücken, aufklappen, Fortschritt füllen.
- **Formular-Kurzform:** `s.formular(titel, felder=[…])` setzt Beschriftungen und Elemente selbst untereinander. Ein Einstellungsdialog braucht dann nur wenige Zeilen.
- **Symbole:** ein kleiner eigener Satz neutraler Symbole (Ordner, Datei, Zahnrad, Schloss, Warnung, Suche, Schließen, Papierkorb, Terminal). Keine Markenlogos, keine Originalgrafiken.
- **Sprachen:**
  - eingebautes Wörterbuch für Oberflächenwörter (OK, Abbrechen, Weiter, Datei, Bearbeiten, Ansicht …) in sechs Sprachen;
  - alles andere über `s.tr`;
  - Terminal- und Codeinhalte bleiben in allen Sprachen gleich.

## Ebene 2: Vorlagen
**a) Terminal (wichtigste Vorlage)**
- **Aufruf:** `s.terminal(spalten, zeilen, prompt="student@labor:~$ ", stil)`. Das Terminal ist ein echtes Zeichenraster, damit Spalten exakt stimmen; Rahmen- und Blockzeichen (─ │ ┌ █) passen ins Raster.
- **Abläufe:**
  - `eingabe(befehl, tempo)`: tippen, Cursor blinkt;
  - `ausgabe(text)`: zeilenweise;
  - neuer Prompt;
  - `leeren()` (clear);
  - Rollen: Alte Zeilen wandern oben hinaus.
- **Shell-Bedienung:**
  - markieren;
  - Tab-Vervollständigung: Der Rest erscheint;
  - Verlauf mit Pfeil hoch;
  - Suche mit Strg+R;
  - `^C`.
- **ANSI-Farben und Attribute** (fett, invers, unterstrichen, 16/256 Farben) für `ls --color`, `grep --color`, `diff`, `git`.
- **Vollbild-Programme (TUI):**
  - `nano` (Kopf, Text, Tastenleiste ^O ^X);
  - `less`/`man` (Statuszeile);
  - `top` (Kopf und Tabelle, Werte ändern sich);
  - Textmodus-Dialoge (Installer, `whiptail`);
  - Bootmenü.
- **Aus Mitschrift:** `s.terminal_aus_mitschrift(datei, block)` liest eine echte, geprüfte Sitzung (`sitzung_kap*.txt`, Blöcke aus `heft_pruefen.py`). Wechselnde Teile wie Uhrzeiten lassen sich festlegen.
- **Stile:** neutral, an Ubuntu angelehnt, PowerShell/Windows-Terminal (für WSL).

**b) Code-Editor und Programmablauf (= geplantes L8)**
- **Aufruf:** `s.code(text, sprache, zeilennummern, thema)` mit Syntaxhervorhebung für Python, Bash, C/C++, JSON, YAML, INI und Markdown.
  - Tokenizer: Pygments beim Export; im Browser voraussichtlich dasselbe über Pyodide.
- **Randmarken:**
  - Haltepunkt, Fehler-/Warnsymbol, Änderung +/−, aktuelle Zeile;
  - Wellenlinie unter Fehlern mit Meldung, Auswahl, Einrückungslinien.
- **Animationen:**
  - tippen;
  - Zeile einfügen/löschen, der Rest rückt nach;
  - Zeile hervorheben;
  - Unterschiede (Diff) nebeneinander oder untereinander.
- **Programmablauf:**
  - `s.ablauf(code, eingaben)` führt den Code beim Export wirklich aus (Trace).
  - Die Zeilenmarke wandert, eine Variablentabelle bzw. ein Speicherbild (Namen → Objekte mit Pfeilen) und die Ausgabe füllen sich.
  - Alle Werte stammen aus der echten Ausführung.
- **Weitere Ansichten:**
  - Editor-Fenster mit Dateibaum, Registerkarten, Terminal-Bereich und Ausführen-Knopf;
  - Python-REPL (`>>>`, `...`);
  - Traceback mit markierter Zeile;
  - Notebook-Zelle (`In [1]`/`Out [1]`, Plot als Achsen).

**c) Dialoge und Einstellungen**
- Assistent mit Schritten (Weiter/Zurück), z. B. „Neue virtuelle Maschine“, Installer;
- Liste bearbeiten (Umgebungsvariable PATH unter Windows);
- Funktionen ein-/ausschalten;
- Eigenschaften-Dialog mit Rechten;
- BIOS/UEFI-Bootauswahl (Textmodus).

**d) Dateimanager**
- Pfadleiste, Seitenleiste;
- Liste mit Symbolen und Spalten (Name, Größe, Datum, Rechte);
- Kontextmenü, Ziehen und Ablegen.

**e) Browser**
- Adressleiste mit Schloss und hervorhebbarer Domain, z. B. ähnlich aussehende Domains beim Phishing;
- Registerkarten;
- Seite aus Bausteinen (Überschrift, Text, Login-Formular);
- Warnseite bei ungültigem Zertifikat, Zertifikatsdialog;
- Entwicklerwerkzeuge (Netzwerk-Tabelle, Cookies, Konsole).

**f) E-Mail**
- Liste und Ansicht mit Kopf (Von, An, Betreff);
- Link-Ziel beim Überfahren (Phishing).

**g) Desktop**
- Hintergrund, Taskleiste/Dock, Startmenü;
- mehrere Fenster (überlappend, Fokus, öffnen/minimieren/schließen mit Übergang);
- Benachrichtigungen.

**h) Tabellen-Werkzeuge**
- eine allgemeine Vorlage (Kopf, Spaltenbreiten, Auswahl, Sortierung) für Paketlisten (Wireshark-artig), Prozesslisten und Tabellenkalkulation (CSV aus Linux 6).

## Ebene 3: Bedien-Ebene (für alle Vorlagen)
- **Mauszeiger:**
  - Formen: Pfeil, Hand, Textcursor, Warten;
  - Bewegung entlang eines Wegs;
  - Klick (Welle), Doppelklick, Rechtsklick (öffnet Kontextmenü), Ziehen, Hover-Zustand des Ziels.
- **Tasten-Einblendung:**
  - Tastenkappen „Strg + C“ je Sprache (Strg/Ctrl, Entf/Del …) mit Druck-Animation;
  - Tastenfolgen.
- **Hinweise:**
  - Lupe (vergrößerter Ausschnitt mit Verbindungslinien);
  - Scheinwerfer: alles außer einem Bereich abdunkeln;
  - nummerierte Schrittmarken;
  - Rahmen mit Beschriftung.
- **Ausschnitt und Zoom:**
  - Ein großes Fenster zeigt nur den nötigen Teil, mit ausgeblendeter Kante. Damit reichen 548 px.
  - 2D-Zoom auf ein Element.

## Technische Leitplanken
- **Rendern:**
  - Alles entsteht aus vorhandenen Grundformen (Rechteck, Text, Pfad).
  - Damit funktionieren SVG, `.anim.svg`, Vektor-PDF und Spieler ohne neuen Renderweg.
- **Schrift und Raster:**
  - Die Zellbreite kommt aus der Schreibmaschinenschrift.
  - Fenster skalieren auf höchstens 548 px.
  - Der Export prüft die Mindestschriftgröße (Lehre aus Linux 5: 16 px wirkten auf der Seite wie 9 px).
- **Stile und Farben:**
  - Stile: neutral (Standard) sowie an Windows 11, Ubuntu GNOME und macOS angelehnt (Formen, Farben, Abstände), ohne Logos oder Originalgrafiken.
  - Im Nachtmodus der Website behalten Fenster ihre Farben, wie alle Abbildungen.
- **Editor-Oberfläche:**
  - neue Gruppe „Bildschirm & Fenster“ in der Palette;
  - Terminal- und Codeinhalt als Textfeld (ANSI-Kürzel erlaubt);
  - Zustände als Schritte in der Zeitleiste;
  - in der geplanten Ansicht Szene ↔ Code als `s.terminal(…)`-Aufrufe.
- **Tests:**
  - Vertragstests je Baustein (Export = Editor);
  - Kontaktblatt aller Vorlagen in sechs Sprachen;
  - Größenbudget (Terminal mit 24 Zeilen unter 100 KB).

## Wellen (Vorschlag)
| Welle | Inhalt | Nutzen sofort |
|---|---|---|
| **F1** | Fenster, Terminal mit Raster/ANSI/TUI, Mitschrift-Import, Bedien-Ebene (Maus, Tasten, Lupe, Scheinwerfer, Ausschnitt) | Linux 7/8 (58 Szenen offen), Linux 9–10; ersetzt die Handarbeit der Terminalbilder |
| **F2** | Code-Editor, Programmablauf mit echter Ausführung (L8), REPL, Traceback, Notebook | Python 4+, C/C++, ML-Pfad, 7 Audit-Fälle |
| **F3** | Steuerelemente, Formular, Dialoge/Einstellungen, Dateimanager, Tabellen-Vorlage | Linux 1 (WSL/VM/USB), Linux 7 (Rechte), Einrichtung in Python 1 |
| **F4** | Browser, E-Mail, Desktop mit mehreren Fenstern, Entwicklerwerkzeuge | Cybersecurity 2+ |

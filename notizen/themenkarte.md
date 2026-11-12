# Themenkarte: Wo ist welches Thema vollständig erklärt?

Regel des Users (06.11.2026): „Inhalte nicht mehrfach auf der Webseite vollständig erklären“. Jedes Thema hat genau einen
Ort, an dem es vollständig erklärt wird. Andere Hefte setzen es voraus, fassen es höchstens in ein bis drei Sätzen zusammen
und verweisen mit Link darauf.

## So benutzt du die Karte (Schreib-Agenten)
1. **Vor dem Schreiben nachsehen:** Für jeden Begriff deines Lernpfad-Eintrags mit Grep in dieser Datei suchen (Wortstamm,
   auch englisch), nicht die ganze Datei lesen. Jede Zeile beginnt mit der Verweis-Wendung des Abschnitts.
2. **Gefunden:** nicht neu erklären. Im Heft steht dann „Was du dafür brauchst“ mit einer kurzen, selbsttragenden
   Zusammenfassung (Definition, eine Formel, ein Mini-Beispiel) und dem Verweis in genau dieser Form; auf der Website wird er
   zum Link auf Artikel und Abschnitt (Benennung seit 09.11.2026, notizen/kapitel_umstellung.md):
   - aus einem anderen Bereich oder Modul genau die Wendung der Zeile: „Grundlagen, Kapitel 1, Abschnitt 13.5“,
     „Python, Kapitel 2, Abschnitt 3.1“, „Linux, Kapitel 2, Abschnitt 3.1“, „HöMa1, Kapitel 5, Abschnitt 8“ (später auch
     „C, Kapitel 1, …“, „C++, Kapitel 1, …“, „Machine Learning, Kapitel 1, …“ = Lernpfad-Heft T08);
   - im selben Bereich ohne Kurznamen: „Kapitel 2, Abschnitt 3.1“;
   - mehrere: „Grundlagen, Kapitel 1, Abschnitte 10.1 und 11.4“; das ganze Heft: „Grundlagen, Kapitel 1“.
   Übersetzungen: notizen/kapitel_umstellung.md (Formentabelle). Das gilt für alle Module, auch Elektrotechnik und Höhere
   Mathematik.
3. **Nicht gefunden:** Du erklärst es vollständig, wenn es zu deinem Heft gehört (siehe „Zuständigkeiten“ unten). Gehört es in
   einen anderen Bereich, der noch kein Heft dazu hat, trägst du es unten unter „Geplant“ mit dem vorgesehenen Ort ein und
   fragst im Bericht nach.
4. **Nach dem Heft:** `python tools/themenkarte.py` im Repo ausführen. Das Skript erzeugt alles unterhalb von „Erklärt in“
   neu aus den Heften; nur der Teil zwischen den Markierungen „von Hand“ bleibt stehen.

<!-- von Hand: Anfang -->
## Zuständigkeiten und geplante Themen (von Hand)
- **Programmieren** (Informatik / Programmieren / Python, Kapitel 1 bis 3 fertig): Python als Sprache, Datenstrukturen, Funktionen, Module,
  venv, NumPy-Grundlagen; später C und C++. ML und Cybersecurity setzen das voraus.
  - Python, Kapitel 1 erklärt vollständig: Programm/Anweisung, Maschinenbefehl, Programmiersprache, Syntax, Semantik, Quelltext,
    Compiler, Interpreter, CPython, Bytecode, Python installieren (Windows install manager `py`, Linux `python3`),
    Versionsnummer, interaktiver Modus, Wert, Ausdruck, Grundrechenzeichen `+ - * / **` (nur als Taschenrechner),
    Zeichenkette (nur Literal), Funktion und Funktionsaufruf (nur `print`), Editor, Skript, Kommentar, Syntaxfehler,
    Laufzeitfehler, Ausnahme (Art + Beschreibung), Traceback, Logikfehler.
  - Python, Kapitel 2 erklärt vollständig: Objekt, Typ, Identität (`id`), Methode, Attribut, `int` (beliebig groß), Operatoren und
    Rangfolge, `/`, `//`, `%` (auch negativ), `**`; Stellenwertsystem, Bit, Byte, Binär- und Hexadezimalzahl, Binärbruch,
    Verdopplungsverfahren; Gleitkommazahl und IEEE 754 binary64 (Exponenten-/Mantissenfeld), Darstellungsfehler, kürzeste
    Darstellung, Rundungsfehler, Maschinengenauigkeit, Absorption, Auslöschung, `inf`, `nan`; Variable, Zuweisung, Namensregeln,
    erweiterte Zuweisung; `bool`, Vergleichsoperatoren, Toleranzvergleich (`math.isclose`), `is`, `None`; Modul/`import` (nur
    `import x`), `math`, `sys.float_info`; `complex`, `cmath`; Zeichenketten-Operatoren und `len`, f-String, `input`,
    Typumwandlung, `round`. Cybersecurity (Bit/Byte/Hex nur als Voraussetzung, z. B. Kapitel 2 und 4) und Grundlagen, Kapitel 3,
    Abschnitt 11.3 (Gleitkommazahlen) verweisen darauf. Unicode-Nummern von Zeichen (U+201E): Python, Kapitel 9.
  - Python, Kapitel 3 erklärt vollständig: verkettete Vergleiche, Vergleich von Zeichenketten, `not`/`and`/`or`, Rangfolge,
    Kurzschlussauswertung, Wahrheitswert von Objekten (ohne Behälter), Ergebnis von `and`/`or`; `if`/`elif`/`else`, Block und
    Einrückung (Kopfzeile, IndentationError, TabError), `match` nur als Hintergrund; `while`, Endlosschleife, Strg+C/
    `KeyboardInterrupt`, Gleitkomma-Falle in Schleifen; `for`, `range`, Schleifenvariable; `break`, `continue`, `else` an Schleifen
    (Hintergrund), verschachtelte Schleifen, Akkumulator (Summe, Anzahl, Produkt, Mittelwert, Maximum); Raten und Prüfen,
    Näherung mit Toleranz, Zwischenwertsatz (Nullstellen-Fassung), Bisektion mit Schrittzahl, Tangente, Newton-Verfahren,
    quadratische Konvergenz, Heron = Newton, `math.sqrt`; Anwendung (seit 09.11.2026 ohne Elektrotechnik): Zinssatz eines
    Ratenkredits numerisch (Restschuld, Annuitätenformel, effektiver Jahreszins nur als Umrechnung (1+i)^12 − 1, Ableitung per
    Schleife, Absicherung von Newton durch Bisektion und Dämpfung als Hintergrund). Numerik-Hefte und ML-Grundlagen
    (Gradientenabstieg, Optimierung) können für Bisektion/Newton darauf verweisen. Eigene Funktionen: Python, Kapitel 4; Listen: Python, Kapitel 5.
- **Linux und Kommandozeile** (Informatik / Linux und Kommandozeile, Kapitel 1–9 fertig): Shell, Dateien, Rechte (vollständig erklärt in Linux, Kapitel 7 „Benutzer, Gruppen und Rechte“), Prozesse, Signale und Dienste (Linux, Kapitel 8).
  Cybersecurity hat seit 11.11.2026 einen Stamm mit 12 Teilen: Die alten Hefte „Linux vom USB-Stick“ und „Die Shell als Werkzeug“
  entfallen (Inhalt in Linux, Kapitel 1–6, 8, 10), Cybersecurity, Kapitel 3 ist das Fachheft „Linux-Sicherheit“ (siehe unten).
  - Linux, Kapitel 1 erklärt vollständig (spätere Hefte, auch Cyber und ML, verweisen mit „Linux, Kapitel~1, Abschnitt~M“): Betriebssystem,
    Anwendungsprogramm, Kernel-Modus/Benutzermodus, privilegierter Befehl, Kernel, Treiber, Systemaufruf (feste
    Einsprungstelle, Tabelle der Dienste), Linux als Kernel (GPL v2, GNU), Distribution, Paketverwaltung (nur Begriff),
    Ubuntu-Versionen/LTS/Punktversion (1.1–1.7); drei Wege und Entscheidungsbaum, Terminal, Eingabeaufforderung (2.x);
    virtuelle Maschine, Wirt/Gast, Hypervisor (Typ 1/2 im Hintergrund), Hardware-Virtualisierung (VT-x/AMD-V,
    Popek/Goldberg), Snapshot (Differenzabbild, copy on write), Adresse und NAT-Modus (3.x; andere Netzmodi nur erwähnt);
    WSL 2 (WSL 1 im Hintergrund), Einrichten, `wsl -l -v`, `/mnt/c`, `\\wsl.localhost`, Ablage der Übungsdateien, 9P,
    Grenzen (4.x); Datenträger, Sektor, GB/GiB, Partition, Partitionstabelle (GPT/MBR), Dateisystem, Abbild/ISO-Abbild
    (hybrid), Prüfsumme/SHA-256 (Lawineneffekt, kryptographische Hashfunktion nur als Eigenschaft), `sha256sum -c`,
    `Get-FileHash`, Prüfsumme ≠ Herkunft, digitale Signatur nur als Ausblick-Satz (5.x); Firmware/UEFI,
    EFI-Systempartition, Bootreihenfolge, Bootmenü, Bootloader, GRUB, Secure Boot als Echtheitsprüfung (shim-Kette),
    BitLocker/Geräteverschlüsselung, Wiederherstellungsschlüssel (6.x; TPM/Messen der Startkette nur ein
    Hintergrund-Kasten); VirtualBox-Praxis (7.x); Einhängen/Einhängepunkt, Live-System, squashfs, tmpfs, Overlay,
    initramfs/casper (Hintergrund), Persistenz (8.x); Schreibwerkzeug, Schnellstart, Risiken des Live-Sticks,
    `lsblk` im Live-System (9.x).
  - Bleibt Cybersecurity: Kali als Werkzeug und Laborumgebung mit Host-only/internem Netz (Kapitel 3), Signaturprüfung (GPG) als
    Kryptographie (Kapitel 10), Secure Boot vertieft, Measured Boot/TPM als Vertrauenskette (Kapitel 2), Aufbau von Hashfunktionen
    (Kapitel 9), Ventoy-Lieferkettenfrage (Kapitel 3, Hintergrund).
  - Linux, Kapitel 1 benutzt als Rezepte ohne Erklärung: `cat`, `ls`, `uname -r`, `systemd-detect-virt`, `lsblk`, `mount`,
    `strace` (nur Ausgabe), `explorer.exe .`; erklärt werden sie in Linux, Kapitel 2 (Befehl/Option/Argument), Linux, Kapitel 3
    (Pfade, Dateien, `cat`/`ls`, `lsblk`/Einhängen in der Praxis; seit 10.11.2026), Linux, Kapitel 7 (`sudo`, Rechte), Linux,
    Kapitel 9 (Paketverwaltung, Aktualisieren).
  - Terminal (Terminalemulator), Shell, Eingabeaufforderung, Sitzung, Befehl/Argument/Option, Suchpfad, eingebauter Befehl,
    Alias, Hilfe (`--help`, `help`, `man`, `less`, `apropos`), Vervollständigung, Verlauf, Strg+C/Strg+D und Tastenkürzel:
    vollständig erklärt in Linux, Kapitel 2, Abschnitte 1–5 (seit 10.11.2026); Kurzfassung in „Python, Kapitel 1, Abschnitt 3.1“
    (und 5.2). Python, Kapitel 1 verweist noch mit Text „Linux, Kapitel~2“ ohne Link: beim nächsten Überarbeiten auf
    „Linux, Kapitel 2, Abschnitt 1“ verlinken. `cd` als eingebauter Befehl in Linux, Kapitel 2, Abschnitt 3.3; Pfade, `cd`
    und `mkdir` in der Praxis in Linux, Kapitel 3, Abschnitte 2 und 5.
  - Dateien und Verzeichnisse, vollständig erklärt in Linux, Kapitel 3 (seit 10.11.2026): Datei, Verzeichnis, Verzeichnisbaum,
    Wurzel (1.x); Arbeitsverzeichnis (`pwd`, `cd`, `cd -`), Pfad, absoluter und relativer Pfad, `.` und `..`, Heimatverzeichnis
    und Tilde `~` (2.x); `ls` mit `-a`/`-A`, `-F`, `-l`, `-h`, `-S`/`-t`/`-r`/`-R`, versteckte Datei, Dateinamen (3.x); Textdatei,
    Zeilenende, `cat`, `less`, `head`/`tail`, `wc`, `file`, magische Zahl (4.x); `mkdir -p`, `touch`, Texteditor `nano`, `tree`
    (5.x); `cp`, `cp -r`, `mv`, `rm`, `rmdir`, `rm -r`, Muster für Dateinamen `*`, `?`, `[…]` (6.x); FHS mit `/usr`, `/etc`,
    `/home`, `/root`, `/var` (Protokolle), `/tmp`, `/dev` (Gerätedatei), `/proc`/`/sys` (virtuelles Dateisystem) (7.x); Inode,
    Verzeichnis als Tabelle, harter Link, Linkzähler, Löschen = Namen entfernen, symbolischer Link, usr-merge (8.x); Einhängen in
    der Praxis mit `lsblk`, `findmnt`, `df` mit Pfaden, `/mnt/c` als 9p (9.x); `find` (`-name`, `-type`, `-size`, `-mtime`,
    `-newer`, Aktionen), `du` (10.x). Muster und Quoting vertieft erst in Linux, Kapitel 5; Zugriffsrechte in Linux, Kapitel 7.
  - Ströme, Umleitung, Pipes und Exit-Status, vollständig erklärt in Linux, Kapitel 4 (seit 10.11.2026): Prozess (eingeführt in
    1.2, mit Prozessnummer und `/proc/self`), Strom und Ende des Stroms (1.3), Standardströme: Standardeingabe, Standardausgabe,
    Standardfehlerausgabe (1.4–1.6), Dateideskriptor (1.7); Umleitung `>`, `>>`, `2>`, `/dev/null` als Ziel, Kopie `2>&1`/`>&2`,
    `&>`, Reihenfolge der Umleitungen, Kürzungsfalle (2.x); `<`, Here-Document, Here-String (3.x); Pipe (mit `|&`), Filter
    (`sort`, `head`, `wc`, `grep`, `uniq`, `tr` je knapp), Pipeline, `tee`, Unix-Philosophie (4.x); Exit-Status und `$?`,
    `true`/`false`, Bedeutungen ungleich null, 126/127/128 + n (5.x); `;`, `&&`, `||`, `a && b || c`, `PIPESTATUS` (nur als
    Rezept), `pipefail` (6.x); Strom gegen Argument, `xargs` mit `-n`, Grenze der Argumentliste, `find -print0`/`xargs -0`,
    `find -exec … {} \;`/`{} +` (7.x; Kapitel 3 hatte `-exec`/`xargs` hierher abgegeben); die Filter dort sind knapp,
    vollständig erklärt in Linux, Kapitel 6. Zuständigkeiten: Linux, Kapitel 8
    (Prozesse, Signale) verweist auf Linux, Kapitel 4, Abschnitt 1.2 (Prozess) und Abschnitt 5.3 (128 + n, dort
    „Unterbrechungsnachricht“) zurück und vertieft fork/exec nur (Hintergrund in 2.1); Kapitel 5 erklärt die `$`-Ersetzung
    (Felder wie `${PIPESTATUS[@]}` bleiben hier Rezept, Kapitel 5 lässt sie aus); Kapitel 6 vertieft `sort`/`uniq`/`grep`/`tr`;
    Kapitel 10 `pipefail` in Skripten. Cybersecurity und ML setzen Umleitung, Pipe und Exit-Status voraus und verweisen hierher.
  - Expansion, Quoting, Variablen und Umgebung, vollständig erklärt in Linux, Kapitel 5 (seit 10.11.2026): Expansion und
    „Erweiterung“ als ihre Arten (1.2), Pfadnamen-Erweiterung mit Sortierung nach Spracheinstellung (1.3), versteckte Dateien in
    Mustern, `globskipdots`, `dotglob` (1.4), Muster ohne Treffer, `nullglob`/`failglob` (1.5), Klammererweiterung `{a,b}`,
    `{x..y}`, `{x..y..s}` (1.6), Tilde-Erweiterung `~`, `~root` (1.7); Shell-Variable, Wert, Zuweisung (2.1),
    Parametererweiterung `$NAME`/`${NAME}`, Parameter, `unset`, `${NAME:-vorgabe}`, `${#NAME}` (2.2), Befehlsersetzung `$(…)`
    und Gravis-Form (2.3), Arithmetik `$((…))` (2.4); `printf` (3.1), Worttrennung, `IFS` (3.2), Quoting, `$'…'` (3.3),
    einfache und doppelte Anführungszeichen (3.4, 3.5), umgekehrter Schrägstrich und Fortsetzungszeile (3.6), Entfernen der
    Anführungszeichen (3.7), Regel „Erweiterungen in doppelte Anführungszeichen“ (3.8), Reihenfolge der Expansion (3.9);
    Kindprozess, Elternprozess (4.2), Umgebung, `printenv` (4.3), Umgebungsvariable, `export`, `export -n` (4.4), Vererbung als
    Kopie (4.5), Zuweisung vor einem Befehl, `TZ` (4.6), `env`, Tabelle der üblichen Umgebungsvariablen (4.7); `PATH`,
    `type -a`, `command -v` (5.2), Befehlssuche, `hash` (5.3), `./programm` (5.4), `PATH` ändern (5.5); Startdatei
    `~/.bashrc` (6.1), `source`/`.` (6.2), Anmelde-Shell, `~/.profile`, `shopt login_shell`, `bash -l` (6.3), Einstellung
    dauerhaft machen, `EDITOR`, `~/.local/bin` (6.4), Alias anlegen und dauerhaft, `unalias`, `~/.bash_aliases` (6.5; Alias als
    Begriff bleibt in Kapitel 2, Abschnitt 3.4). Zuständigkeiten: Kapitel 6 reguläre Ausdrücke und „Muster sind keine regulären
    Ausdrücke“, `grep` vertieft, `seq`; Kapitel 7 Ausführungsrecht, `chmod`; Kapitel 8 Prozesse vertieft, `/proc/<PID>/environ`;
    Kapitel 10 Skripte, Positionsparameter, `if`, Schleifen (auch `{1..$n}`), Funktionen, `set -x`, Felder; Kapitel 11 SSH;
    Cybersecurity, Kapitel 12 Injection und Cybersecurity, Kapitel 3 PATH-Hijacking (in 3.8 nur ein Hinweis). Weggelassen: weitere `${…}`-Formen (nur Verweis auf
    `man bash`), extglob, globstar, `declare`, `BASH_ENV`.
  - Textwerkzeuge und reguläre Ausdrücke, vollständig erklärt in Linux, Kapitel 6 (seit 11.11.2026): Datensatz, Feld,
    Trennzeichen, Spalte (1.2), CSV-Datei, Kopfzeile (1.3), Wagenrücklauf und Windows-Zeilenende, `cat -A` (1.4), `tail -n +K`,
    `head -n -K` (1.5), `tail -f` (1.6); `cut` (2.1), `tr` mit `-d`/`-s` und Klassen (2.2), `paste` (2.3); `sort` mit
    Zeichenordnung (3.1), `sort -n` (3.2), Sortierschlüssel `-t`/`-k` (3.3), Spracheinstellung, `LANG`/`LC_ALL`, `locale -a`
    (3.4), `uniq` mit `-c`/`-d`/`-u` (3.5), Häufigkeitstabelle `sort | uniq -c | sort -rn`, `sort -u` (3.6); `nl` (4.1), `seq`
    (4.2), `diff` (4.3); `grep` ausführlich: Suchtext, Status (5.1), `-i -v -c -n` (5.2), `-o` (5.3), `-r`/`-l` (5.4);
    Zeichenkette, regulärer Ausdruck, Treffer (6.1), Punkt (6.2), `\` und `grep -F` (6.3), Klammerausdruck (6.4), Zeichenklasse
    `[[:digit:]]` usw. (6.5), Anker `^`/`$` (6.6); Stern (7.1), Grundform und erweiterte Form (BRE/ERE), `grep -E` (7.2),
    Quantor `+ ? {n} {n,m} {n,}` (7.3), Gruppe, Alternative (7.4), Grundform-Schreibweisen (7.5), längster Treffer (7.6), Form
    statt Bedeutung, endlicher Automat im Hintergrund (7.7), „Muster für Dateinamen sind keine regulären Ausdrücke“ (7.8);
    `sed`, Zwischenspeicher (8.1), `s///` mit `g` und `&` (8.2), Zeilenadresse, `-n`, `p` (8.3), `d`, `q` im Hintergrund (8.4),
    Rückverweis `\1`–`\9` (8.5), `sed -i`, `-i.bak` (8.6); `awk`, Regel aus Bedingung und Aktion (9.1), Felder `$1`…`$NF`, `$0`,
    `NF`, `-F` (9.2), `NR`, Vergleiche, `&& || !`, `~` (9.3), Variablen, `BEGIN`/`END`, `printf` (9.4), assoziatives Array,
    `for (k in s)` (9.5); Werkzeugwahl (10.1), Pipeline schrittweise bauen (10.2), Wörter zählen (10.3).
    Zuständigkeiten: Kapitel 10 verweist für Windows-Zeilenenden in Skripten (`bad interpreter`) auf „Linux, Kapitel 6,
    Abschnitt 1.4“ zurück und benutzt `awk` in Schleifen über Dateien (Kapitel 6 erklärt `awk` selbst, Kapitel 10 nur die
    Schleife); Cybersecurity, Kapitel 3 wertet Anmeldeprotokolle mit `grep`/`awk`/`sort | uniq -c` aus und verweist hierher; ein späteres
    Python-Heft zum Modul `re` verweist für reguläre Ausdrücke auf Linux, Kapitel 6, Abschnitte 6–7 und erklärt nur die
    Unterschiede (Hintergrund in 7.6: Python probiert der Reihe nach, kürzeste Treffer `*?`). Weggelassen: `join`, `comm`, `tac`, `rev`, `expand`, `sort -m/-b/-g/-V/-s`, `uniq -f/-s/-i`,
    `cut --complement`, `sed y/a/i/c/-f`, `grep -w/-x/-h/-L/-P`, `\b \< \>`, `awk -v`, awk-Funktionen, `getline`, `patch`.
  - Paketverwaltung `apt` und `sudo`: in Python, Kapitel 1, Abschnitt 3.3 nur je ein Satz; ausführlich im Linux-Bereich
    (Heftnummer laut Linux-Lernpfad).
- **Cybersecurity** (Informatik / Cybersecurity, Kapitel 1–2 fertig; Stamm seit 11.11.2026 mit 12 Teilen, Kapitel N = Teil N = Datei
  `Kap<N>`, Zuordnung und Einträge in `C:\Bücher\EtUndSo\Cybersecurity\Recherche\LERNPFAD.md`). Setzt Linux, Python und C voraus und
  erklärt nur das Sicherheitsspezifische. Geplant (noch ohne Heft; Einträge aus den Grenztabellen der Linux- und Programmieren-
  Lernpfade übernommen):
  - Cybersecurity, Kapitel 2 „Schutzgrenzen in Hardware und Betriebssystem“ (geplant) erklärt vollständig: Schutzgrenze,
    Referenzmonitor, Befehlszeiger, Von-Neumann-Prinzip, Privilegstufe/Schutzring (vertieft; Grundbegriff Kernel-/Benutzermodus:
    Linux, Kapitel 1, Abschnitt 1.2), privilegierte Befehle, Einsprungtabelle und drei Wege in den Kernel, Prüfung der Argumente
    (Grundbegriff Systemaufruf: Linux, Kapitel 1, Abschnitt 1.4), Unterbrechung, Zeitgeber-Unterbrechung (Zeitteilung: Linux,
    Kapitel 8, Abschnitt 1.3), virtueller Adressraum, Seite, Seitentabelle, MMU, Wurzelregister, Seitenfehler, Seitenrechte,
    NX/W^X, SMEP/SMAP, `/proc/self/maps`; Startkette als Schutzgrenze, Bootkit, Vertrauensanker, Secure Boot vertieft (PK, KEK,
    db, dbx, Widerruf, SBAT; Grundbegriff: Linux, Kapitel 1, Abschnitt 6.4), Measured Boot, PCR, Erweitern, Ereignisprotokoll,
    TPM, Versiegeln, Attestierung (Geräteverschlüsselung als Anwendung: Linux, Kapitel 1, Abschnitt 6.5). Bit/Byte/Hex nur als
    Voraussetzung (Python, Kapitel 2, Abschnitt 3).
  - Cybersecurity, Kapitel 3 „Linux-Sicherheit: Labor, Rechteausweitung, Fehlkonfigurationen“ (geplant): Labor (Host-only und
    internes Netz, Snapshot-Routine; VM, Snapshot, NAT: Linux, Kapitel 1, Abschnitt 3), Kali als Werkzeug-Distribution,
    Plattformzugänge; Rechteausweitung, SUID-Missbrauch und GTFOBins, zu weite sudo-Regeln, gespeicherte Benutzernummer als
    Angriffsfolge (Begriff: Linux, Kapitel 8, Abschnitt 2.8), PATH-Hijacking, schreibbare Startdateien, lesbare Geheimnisse,
    Geheimnisse in Verlauf und Prozessliste (`ps`), Symlink-/TOCTTOU-Angriffe in `/tmp`, „complete mediation“ und Deskriptor als
    Capability (Prüfung beim Öffnen: Linux, Kapitel 7, Abschnitt 5.3), DAC/MAC/Bell-LaPadula, Linux-Capabilities (Begriff
    „Fähigkeiten“: Linux, Kapitel 7, Abschnitt 6.4), Auswertung von `auth.log`/Journal, Updates als wichtigste Schutzmaßnahme,
    `curl | bash` als Lieferkettenrisiko. Mechanismus von Benutzern, Rechten, SUID/SGID/Sticky, sudo: Linux, Kapitel 7;
    Prozesse, Signale, Dienste, Journal: Linux, Kapitel 8; apt und Paketsignaturen („signierte Liste“): Linux, Kapitel 9.
  - Cybersecurity, Kapitel 4–5 „Netzwerke I/II“ (geplant): Schichten bis Firewall; die Netzbefehle `ip`, `ss`, `ping`, `dig`,
    `nc` werden dort erklärt (nicht im Bereich Linux); `python3 -m http.server` nur als Rezept mit Verweis Python, Kapitel 11.
  - Cybersecurity, Kapitel 6 „Python für die Sicherheitsarbeit“ (geplant): Hex/Base64/URL-Kodierung, „Kodierung ≠ Verschlüsselung“,
    `struct` und Netzwerk-Bytereihenfolge für Protokollköpfe, XOR auf Bytes, `subprocess` mit/ohne Shell (Command Injection,
    `--`), Sockets (TCP-Bytestrom, `recv`-Schleife, Echo-Server), pwntools, `hashlib` als Werkzeug. Voraussetzung: Python, Kapitel 9
    (`str`/`bytes`, Kodierung, Binärdateien, `int.to_bytes`, `re`, `hashlib`-Grundaufruf), Python, Kapitel 11 (venv, pip,
    `argparse`, `subprocess`-Grundaufruf).
  - Cybersecurity, Kapitel 7 „Speicherfehler: wenn ein Programm über den Rand schreibt“ (geplant): Speicherfehler als
    Schwachstellenklasse (räumlich/zeitlich), Vorzeichen-Falle bei Längenprüfungen (CWE-195/190), Überlauf bei der
    Größenberechnung, struct-Überlauf als Datenmanipulation, gefährliche String-Funktionen als Angriffsfläche, 70-%-Statistik mit
    Vorbehalt, speichersichere Sprachen (CISA/NSA/BSI), Fortify/Stack-Protector/PIE als Voreinstellungen, Fuzzing. Voraussetzung:
    C, Kapitel 1–9 (Typen, Zweierkomplement, Arrays, Strings, Zeiger, Speicherbereiche, Heap, UB, Sanitizer).
  - Cybersecurity, Kapitel 8 „Maschinencode, Assembler und Debugger“ (geplant): x86-64, Aufrufkonvention, Stackrahmen,
    Rücksprungadresse, Systemaufruf in Assembler, ELF/PLT/GOT, gdb auf Maschinenebene (`stepi`, `x`, Register). gdb für
    C-Programme (Haltepunkte, Variablen, Backtrace): C, Kapitel 9.
  - Cybersecurity, Kapitel 9 „Kryptographie I“ (geplant): kryptographische Hashfunktion und ihre Eigenschaften, Passwort-Hashing
    (Hash, Salt, yescrypt, Knacken; Linux, Kapitel 7, Abschnitt 1.8 sagt nur „Prüfwert“), CSPRNG und warum `random` vorhersagbar
    ist (Pseudozufall, Seed: Python, Kapitel 13).
  - Cybersecurity, Kapitel 10 „Kryptographie II“ (geplant): Signaturverfahren, GPG-Signaturprüfung, Zertifikate, TLS,
    SSH-Protokoll, Hostschlüssel/TOFU, Schlüsselaustausch (SSH-Bedienung, Schlüssel erzeugen: Linux, Kapitel 11).
  - Cybersecurity, Kapitel 11–12 „Das Web I/II“ (geplant): HTTP bis Zugriffskontrolle; Injection beginnt mit der ungequoteten
    Variable als Vorform (Linux, Kapitel 5, Abschnitte 3.2 und 3.8); Lieferkette als OWASP-Klasse; Python-/Flask-Übungen verweisen
    auf Python, Kapitel 11 (venv, pip).
  - Ast F (Verteidigung): Protokollauswertung und Angriffserkennung über Kapitel 3 hinaus; Lieferkettenangriffe und BSI-Lagezahlen
    vertieft.
- **ML-Grundlagen gegen Höhere Mathematik:** Was ein HöMa-Heft vollständig erklärt (Beweise, Herleitungen), steht in den
  Grundlagen nur als Kurzfassung mit Verweis. Prüfen bei der nächsten Überarbeitung der Grundlagen.
- **Geplant (noch ohne Heft):** Grundlagen, Kapitel 6 Optimierung (Lernpfad T06, vor dem Gradientenabstieg); ML-Pfad ab Machine Learning, Kapitel 1
  „Lernen aus Daten“ (T08).
<!-- von Hand: Ende -->

# Erklärt in (aus den Heften erzeugt, nicht von Hand ändern)

Je Zeile ein Abschnitt: Verweis-Wendung, Abschnittstitel, dann die Unterabschnitte mit Nummer.

## Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse

### ET1, Kapitel 1: Ladung, Feld und Potenzial (`Kap1_Feld`, Modul et1)

- ET1, Kapitel 1, Abschnitt 1 „Stufe 1: Größen, Kraft und Arbeit“
- ET1, Kapitel 1, Abschnitt 2 „Stufe 2: Ladung“
- ET1, Kapitel 1, Abschnitt 3 „Stufe 3: Die Kraft zwischen Ladungen“
- ET1, Kapitel 1, Abschnitt 4 „Stufe 4: Die Feldstärke“
- ET1, Kapitel 1, Abschnitt 5 „Stufe 5: Feldlinien und Leiter“
- ET1, Kapitel 1, Abschnitt 6 „Stufe 6: Arbeit im Feld“
- ET1, Kapitel 1, Abschnitt 7 „Stufe 7: Das Potenzial“
- ET1, Kapitel 1, Abschnitt 8 „Stufe 8: Spannung und Masse“
- ET1, Kapitel 1, Abschnitt 9 „Stufe 9: Was die Spannung mit einer Ladung macht“
- ET1, Kapitel 1, Abschnitt 10 „Stufe 10: Grenze des Bildes: Magnetismus und Induktion“

### ET1, Kapitel 2: Strom, Widerstand und Kirchhoff (`Kap2_Stromkreis`, Modul et1)

- ET1, Kapitel 2, Abschnitt 1 „Stufe 1: Strom ist bewegte Ladung“
- ET1, Kapitel 2, Abschnitt 2 „Stufe 2: Langsame Elektronen, sofortiger Strom“
- ET1, Kapitel 2, Abschnitt 3 „Stufe 3: Das ohmsche Gesetz aus Feld und Stößen“
- ET1, Kapitel 2, Abschnitt 4 „Stufe 4: Reale Widerstände: Werte und Temperatur“
- ET1, Kapitel 2, Abschnitt 5 „Stufe 5: Zweipole und Zählpfeile“
- ET1, Kapitel 2, Abschnitt 6 „Stufe 6: Knoten, Zweige, Maschen“
- ET1, Kapitel 2, Abschnitt 7 „Stufe 7: Die Knotenregel ist Ladungserhaltung“
- ET1, Kapitel 2, Abschnitt 8 „Stufe 8: Die Maschenregel ist Energieerhaltung“
- ET1, Kapitel 2, Abschnitt 9 „Stufe 9: Reihenschaltung und Spannungsteiler“
- ET1, Kapitel 2, Abschnitt 10 „Stufe 10: Parallelschaltung, Stromteiler und Belastung“

### ET1, Kapitel 3: Der Kondensator (`Kap3_Kondensator`, Modul et1)

- ET1, Kapitel 3, Abschnitt 1 „Stufe 1: Warum Strom in einen Isolator fließt“
- ET1, Kapitel 3, Abschnitt 2 „Stufe 2: Die Kapazität“
- ET1, Kapitel 3, Abschnitt 3 „Stufe 3: Strom und Spannung am Kondensator“
- ET1, Kapitel 3, Abschnitt 4 „Stufe 4: Plattenkondensator und Dielektrikum“
- ET1, Kapitel 3, Abschnitt 5 „Stufe 5: Bauformen und Selbstentladung“
- ET1, Kapitel 3, Abschnitt 6 „Stufe 6: Die gespeicherte Energie“
- ET1, Kapitel 3, Abschnitt 7 „Stufe 7: Parallel- und Reihenschaltung“
- ET1, Kapitel 3, Abschnitt 8 „Stufe 8: Ladungserhaltung beim Umschalten“
- ET1, Kapitel 3, Abschnitt 9 „Stufe 9: Aufladen über einen Widerstand“
- ET1, Kapitel 3, Abschnitt 10 „Stufe 10: Entladen und Zeitkonstante“

### ET1, Kapitel 4: Strom und Spannung messen (`Kap4_Messen`, Modul et1)

- ET1, Kapitel 4, Abschnitt 1 „Stufe 1: Das Messgerät ist ein Bauteil“
- ET1, Kapitel 4, Abschnitt 2 „Stufe 2: Den Messbereich erweitern“
- ET1, Kapitel 4, Abschnitt 3 „Stufe 3: Der Fehler beim Strommessen“
- ET1, Kapitel 4, Abschnitt 4 „Stufe 4: Der Fehler beim Spannungsmessen“
- ET1, Kapitel 4, Abschnitt 5 „Stufe 5: Strom und Spannung zugleich“
- ET1, Kapitel 4, Abschnitt 6 „Stufe 6: Die Wheatstonesche Brücke“
- ET1, Kapitel 4, Abschnitt 7 „Stufe 7: Die verstimmte Brücke“

### ET1, Kapitel 5: Quellen und Ersatzquellen (`Kap5_Ersatzquellen`, Modul et1)

- ET1, Kapitel 5, Abschnitt 1 „Stufe 1: Widerstände zusammenfassen“
- ET1, Kapitel 5, Abschnitt 2 „Stufe 2: Symmetrie nutzen“
- ET1, Kapitel 5, Abschnitt 3 „Stufe 3: Stern und Dreieck“
- ET1, Kapitel 5, Abschnitt 4 „Stufe 4: Ideale Quellen“
- ET1, Kapitel 5, Abschnitt 5 „Stufe 5: Reale Quellen und der Arbeitspunkt“
- ET1, Kapitel 5, Abschnitt 6 „Stufe 6: Spannungsquelle oder Stromquelle“
- ET1, Kapitel 5, Abschnitt 7 „Stufe 7: Quellen zusammenschalten“
- ET1, Kapitel 5, Abschnitt 8 „Stufe 8: Überlagerung“
- ET1, Kapitel 5, Abschnitt 9 „Stufe 9: Thevenin und Norton“
- ET1, Kapitel 5, Abschnitt 10 „Stufe 10: Der R-2R-Wandler“

### ET1, Kapitel 6: Zweitore (`Kap6_Zweitore`, Modul et1)

- ET1, Kapitel 6, Abschnitt 1 „Stufe 1: Vom Vierpol zum Zweitor“
- ET1, Kapitel 6, Abschnitt 2 „Stufe 2: Vier Größen, zwei Gleichungen, vier Zahlen“
- ET1, Kapitel 6, Abschnitt 3 „Stufe 3: Impedanzform und Leerlaufversuch“
- ET1, Kapitel 6, Abschnitt 4 „Stufe 4: Das Zweitor im Betrieb“
- ET1, Kapitel 6, Abschnitt 5 „Stufe 5: Admittanzform und Kurzschlussversuch“
- ET1, Kapitel 6, Abschnitt 6 „Stufe 6: Umrechnen, T und $\pi$“
- ET1, Kapitel 6, Abschnitt 7 „Stufe 7: Hybridform“
- ET1, Kapitel 6, Abschnitt 8 „Stufe 8: Kettenform“
- ET1, Kapitel 6, Abschnitt 9 „Stufe 9: Zusammenschaltung“
- ET1, Kapitel 6, Abschnitt 10 „Stufe 10: Eigenschaften und alle Formen im Überblick“

### ET1, Kapitel 7: Leistung, Anpassung und Wirkungsgrad (`Kap7_Leistung`, Modul et1)

- ET1, Kapitel 7, Abschnitt 1 „Stufe 1: Energie je Ladung mal Ladung je Zeit“
- ET1, Kapitel 7, Abschnitt 2 „Stufe 2: Warum der Widerstand warm wird“
- ET1, Kapitel 7, Abschnitt 3 „Stufe 3: Mittlere Leistung bei Sinusspannung“
- ET1, Kapitel 7, Abschnitt 4 „Stufe 4: Leitungsverluste“
- ET1, Kapitel 7, Abschnitt 5 „Stufe 5: Wohin die Leistung einer Quelle geht“
- ET1, Kapitel 7, Abschnitt 6 „Stufe 6: Leistungsanpassung“
- ET1, Kapitel 7, Abschnitt 7 „Stufe 7: Warum 50 %, und welches Ziel gilt“

### ET1, Kapitel 8: Maschenstrom- und Knotenpotentialverfahren (`Kap8_Netzwerkanalyse`, Modul et1)

- ET1, Kapitel 8, Abschnitt 1 „Stufe 1: Wie viele Größen sind frei?“
- ET1, Kapitel 8, Abschnitt 2 „Stufe 2: Maschenströme erfüllen die Knotenregel“
- ET1, Kapitel 8, Abschnitt 3 „Stufe 3: Das Maschenstromverfahren“
- ET1, Kapitel 8, Abschnitt 4 „Stufe 4: Potenziale erfüllen die Maschenregel“
- ET1, Kapitel 8, Abschnitt 5 „Stufe 5: Das Knotenpotentialverfahren“
- ET1, Kapitel 8, Abschnitt 6 „Stufe 6: Welches Verfahren wann?“
- ET1, Kapitel 8, Abschnitt 7 „Stufe 7: Stempel und Netzliste“
- ET1, Kapitel 8, Abschnitt 8 „Stufe 8: Gesteuerte Quellen und Verstärker“
- ET1, Kapitel 8, Abschnitt 9 „Stufe 9: Die modifizierte Knotenanalyse“

### ET1, Kapitel 9: Halbleiter und Dioden (`Kap9_Dioden`, Modul et1)

- ET1, Kapitel 9, Abschnitt 1 „Stufe 1: Warum Silizium kaum leitet“
- ET1, Kapitel 9, Abschnitt 2 „Stufe 2: Dotierung“
- ET1, Kapitel 9, Abschnitt 3 „Stufe 3: Die Raumladungszone“
- ET1, Kapitel 9, Abschnitt 4 „Stufe 4: Warum der Strom exponentiell wächst“
- ET1, Kapitel 9, Abschnitt 5 „Stufe 5: Kennlinie, Durchbruch und Spezialdioden“
- ET1, Kapitel 9, Abschnitt 6 „Stufe 6: Der Arbeitspunkt“
- ET1, Kapitel 9, Abschnitt 7 „Stufe 7: Lineare Ersatzschaltungen“
- ET1, Kapitel 9, Abschnitt 8 „Stufe 8: Kleine Änderungen um den Arbeitspunkt“
- ET1, Kapitel 9, Abschnitt 9 „Stufe 9: Gleichrichter und Ladungspumpe“

### ET1, Kapitel 10: Der Bipolartransistor (`Kap10_Bipolartransistor`, Modul et1)

- ET1, Kapitel 10, Abschnitt 1 „Stufe 1: Drei Schichten, zwei Spannungen“
- ET1, Kapitel 10, Abschnitt 2 „Stufe 2: Warum Strom durch die gesperrte Diode fließt“
- ET1, Kapitel 10, Abschnitt 3 „Stufe 3: Eine Fläche, viele Kennlinien“
- ET1, Kapitel 10, Abschnitt 4 „Stufe 4: Drei Bereiche, drei Ersatzschaltbilder“
- ET1, Kapitel 10, Abschnitt 5 „Stufe 5: Der Arbeitspunkt“
- ET1, Kapitel 10, Abschnitt 6 „Stufe 6: Der Transistor als Schalter“
- ET1, Kapitel 10, Abschnitt 7 „Stufe 7: Gegenkopplung hält den Arbeitspunkt fest“
- ET1, Kapitel 10, Abschnitt 8 „Stufe 8: Zwei Schaltungen, die $U_\mathrm{BE}$ nutzen“
- ET1, Kapitel 10, Abschnitt 9 „Stufe 9: Tangente statt Kurve“
- ET1, Kapitel 10, Abschnitt 10 „Stufe 10: Drei Grundschaltungen“

### ET1, Kapitel 11: Der Operationsverstärker (`Kap11_OPV`, Modul et1)

- ET1, Kapitel 11, Abschnitt 1 „Stufe 1: Rauschen“
- ET1, Kapitel 11, Abschnitt 2 „Stufe 2: Der Differenzverstärker“
- ET1, Kapitel 11, Abschnitt 3 „Stufe 3: Der OPV ohne Rückführung“
- ET1, Kapitel 11, Abschnitt 4 „Stufe 4: Gegenkopplung“
- ET1, Kapitel 11, Abschnitt 5 „Stufe 5: Die Regel und die virtuelle Masse“
- ET1, Kapitel 11, Abschnitt 6 „Stufe 6: Mehrere Eingänge, mehrere Stufen“
- ET1, Kapitel 11, Abschnitt 7 „Stufe 7: Rechnen mit Kondensator und Diode“
- ET1, Kapitel 11, Abschnitt 8 „Stufe 8: Strom als Signal“
- ET1, Kapitel 11, Abschnitt 9 „Stufe 9: Mitkopplung und der Schmitt-Trigger“
- ET1, Kapitel 11, Abschnitt 10 „Stufe 10: Wo die Regeln enden“

## Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1

### HöMa1, Kapitel 1: Mengen, Logik und reelle Zahlen (`Kap1_Zahlen`, Modul hm1)

- HöMa1, Kapitel 1, Abschnitt 1 „Stufe 1: Mengen und Aussagen“
- HöMa1, Kapitel 1, Abschnitt 2 „Stufe 2: Quantoren und indirekter Beweis“
- HöMa1, Kapitel 1, Abschnitt 3 „Stufe 3: Körperaxiome“
- HöMa1, Kapitel 1, Abschnitt 4 „Stufe 4: Anordnungsaxiome“
- HöMa1, Kapitel 1, Abschnitt 5 „Stufe 5: Vollständige Induktion, Summe und Produkt“
- HöMa1, Kapitel 1, Abschnitt 6 „Stufe 6: Das Vollständigkeitsaxiom“
- HöMa1, Kapitel 1, Abschnitt 7 „Stufe 7: Intervallschachtelung und Wurzeln“
- HöMa1, Kapitel 1, Abschnitt 8 „Stufe 8: Abstand und Betrag“
- HöMa1, Kapitel 1, Abschnitt 9 „Stufe 9: Elementare Ungleichungen“

### HöMa1, Kapitel 2: Komplexe Zahlen (`Kap2_Komplex`, Modul hm1)

- HöMa1, Kapitel 2, Abschnitt 1 „Stufe 1: Paare statt einzelner Zahlen“
- HöMa1, Kapitel 2, Abschnitt 2 „Stufe 2: Die komplexe Ebene“
- HöMa1, Kapitel 2, Abschnitt 3 „Stufe 3: Spiegeln an der reellen Achse“
- HöMa1, Kapitel 2, Abschnitt 4 „Stufe 4: Dividieren, und was verloren geht“
- HöMa1, Kapitel 2, Abschnitt 5 „Stufe 5: Betrag und Abstand“
- HöMa1, Kapitel 2, Abschnitt 6 „Stufe 6: Quadratische Gleichungen“

### HöMa1, Kapitel 3: Funktionen und Polynome (`Kap3_Funktionen`, Modul hm1)

- HöMa1, Kapitel 3, Abschnitt 1 „Stufe 1: Was eine Funktion ist“
- HöMa1, Kapitel 3, Abschnitt 2 „Stufe 2: Gerade, monoton, beschränkt“
- HöMa1, Kapitel 3, Abschnitt 3 „Stufe 3: Rückwärts: injektiv, surjektiv, bijektiv“
- HöMa1, Kapitel 3, Abschnitt 4 „Stufe 4: Verknüpfen und Umkehren“
- HöMa1, Kapitel 3, Abschnitt 5 „Stufe 5: Polynome und Koeffizienten“
- HöMa1, Kapitel 3, Abschnitt 6 „Stufe 6: Division mit Rest“
- HöMa1, Kapitel 3, Abschnitt 7 „Stufe 7: Das Horner-Schema“
- HöMa1, Kapitel 3, Abschnitt 8 „Stufe 8: Jede Nullstelle spaltet einen Linearfaktor ab“
- HöMa1, Kapitel 3, Abschnitt 9 „Stufe 9: Rationale Funktionen und Pole“

### HöMa1, Kapitel 4: Folgen und Grenzwerte (`Kap4_Folgen`, Modul hm1)

- HöMa1, Kapitel 4, Abschnitt 1 „Stufe 1: Folgen und ihr Verlauf“
- HöMa1, Kapitel 4, Abschnitt 2 „Stufe 2: Das Epsilon-Spiel“
- HöMa1, Kapitel 4, Abschnitt 3 „Stufe 3: Nullfolgen vergleichen“
- HöMa1, Kapitel 4, Abschnitt 4 „Stufe 4: Der Grenzwert“
- HöMa1, Kapitel 4, Abschnitt 5 „Stufe 5: Rechenregeln“
- HöMa1, Kapitel 4, Abschnitt 6 „Stufe 6: Einklemmen und Divergenz“
- HöMa1, Kapitel 4, Abschnitt 7 „Stufe 7: Monotone Folgen und die Vollständigkeit“
- HöMa1, Kapitel 4, Abschnitt 8 „Stufe 8: Cauchy-Folgen und die Axiome“

### HöMa1, Kapitel 5: Exponentialfunktion und Stetigkeit (`Kap5_Stetigkeit`, Modul hm1)

- HöMa1, Kapitel 5, Abschnitt 1 „Stufe 1: Von der Zinsrechnung zur Exponentialfunktion“
- HöMa1, Kapitel 5, Abschnitt 2 „Stufe 2: Wachstum, Logarithmus, allgemeine Potenz“
- HöMa1, Kapitel 5, Abschnitt 3 „Stufe 3: Grenzwerte von Funktionen“
- HöMa1, Kapitel 5, Abschnitt 4 „Stufe 4: Stetigkeit und Epsilon-Delta“
- HöMa1, Kapitel 5, Abschnitt 5 „Stufe 5: Stetigkeit vererben“
- HöMa1, Kapitel 5, Abschnitt 6 „Stufe 6: Teilfolgen und Häufungspunkte“
- HöMa1, Kapitel 5, Abschnitt 7 „Stufe 7: Maximum, Minimum, gleichmäßige Stetigkeit“
- HöMa1, Kapitel 5, Abschnitt 8 „Stufe 8: Zwischenwerte, Nullstellen, Umkehrfunktion“

### HöMa1, Kapitel 6: Unendliche Reihen (`Kap6_Reihen`, Modul hm1)

- HöMa1, Kapitel 6, Abschnitt 1 „Stufe 1: Eine Reihe ist eine Folge“
- HöMa1, Kapitel 6, Abschnitt 2 „Stufe 2: Nullfolge nötig, aber nicht genug“
- HöMa1, Kapitel 6, Abschnitt 3 „Stufe 3: Wechselnde Vorzeichen“
- HöMa1, Kapitel 6, Abschnitt 4 „Stufe 4: Rechenregeln und Klammern“
- HöMa1, Kapitel 6, Abschnitt 5 „Stufe 5: Absolute Konvergenz und Vergleich“
- HöMa1, Kapitel 6, Abschnitt 6 „Stufe 6: Quotient und Wurzel“
- HöMa1, Kapitel 6, Abschnitt 7 „Stufe 7: Verdichten und der Entscheidungsweg“
- HöMa1, Kapitel 6, Abschnitt 8 „Stufe 8: Umordnen“

### HöMa1, Kapitel 7: Potenzreihen und Eulersche Formel (`Kap7_Potenzreihen`, Modul hm1)

- HöMa1, Kapitel 7, Abschnitt 1 „Stufe 1: Der Konvergenzkreis“
- HöMa1, Kapitel 7, Abschnitt 2 „Stufe 2: Den Radius ausrechnen“
- HöMa1, Kapitel 7, Abschnitt 3 „Stufe 3: Sinus und Cosinus als Reihen“
- HöMa1, Kapitel 7, Abschnitt 4 „Stufe 4: Reihen multiplizieren“
- HöMa1, Kapitel 7, Abschnitt 5 „Stufe 5: Die Exponentialreihe, reell und komplex“
- HöMa1, Kapitel 7, Abschnitt 6 „Stufe 6: Die Eulersche Formel“
- HöMa1, Kapitel 7, Abschnitt 7 „Stufe 7: Die Zahl $\pi$ und die Wertetabelle“
- HöMa1, Kapitel 7, Abschnitt 8 „Stufe 8: Polardarstellung, Drehen und Strecken“
- HöMa1, Kapitel 7, Abschnitt 9 „Stufe 9: Die $n$-ten Wurzeln“

### HöMa1, Kapitel 8: Vektoren und Skalarprodukt (`Kap8_Vektoren`, Modul hm1)

- HöMa1, Kapitel 8, Abschnitt 1 „Stufe 1: Pfeile addieren und strecken“
- HöMa1, Kapitel 8, Abschnitt 2 „Stufe 2: Der Vektorraum“
- HöMa1, Kapitel 8, Abschnitt 3 „Stufe 3: Unterraum und Linearkombination“
- HöMa1, Kapitel 8, Abschnitt 4 „Stufe 4: Lineare Unabhängigkeit“
- HöMa1, Kapitel 8, Abschnitt 5 „Stufe 5: Skalarprodukt, Norm, Abstand“
- HöMa1, Kapitel 8, Abschnitt 6 „Stufe 6: Projektion und Abstand zur Geraden“
- HöMa1, Kapitel 8, Abschnitt 7 „Stufe 7: Winkel, Cauchy-Schwarz, Parallelogramm“
- HöMa1, Kapitel 8, Abschnitt 8 „Stufe 8: Kugel, Hyperebene, drei geometrische Probleme“

### HöMa1, Kapitel 9: Vektorprodukt und Basen (`Kap9_Basen`, Modul hm1)

- HöMa1, Kapitel 9, Abschnitt 1 „Stufe 1: Das Vektorprodukt“
- HöMa1, Kapitel 9, Abschnitt 2 „Stufe 2: Rechenregeln und Geometrie im Raum“
- HöMa1, Kapitel 9, Abschnitt 3 „Stufe 3: Spatprodukt und Volumen“
- HöMa1, Kapitel 9, Abschnitt 4 „Stufe 4: Orthonormalsysteme und Projektion“
- HöMa1, Kapitel 9, Abschnitt 5 „Stufe 5: Die Basis“
- HöMa1, Kapitel 9, Abschnitt 6 „Stufe 6: Die Dimension“
- HöMa1, Kapitel 9, Abschnitt 7 „Stufe 7: Orthonormalbasis und Gram-Schmidt“
- HöMa1, Kapitel 9, Abschnitt 8 „Stufe 8: Skalarprodukträume“

### HöMa1, Kapitel 10: Matrizen und lineare Gleichungssysteme (`Kap10_Matrizen`, Modul hm1)

- HöMa1, Kapitel 10, Abschnitt 1 „Stufe 1: Lineare Abbildungen“
- HöMa1, Kapitel 10, Abschnitt 2 „Stufe 2: Die Spalten sind die Bilder“
- HöMa1, Kapitel 10, Abschnitt 3 „Stufe 3: Kern, Bild und die Bilanz der Dimensionen“
- HöMa1, Kapitel 10, Abschnitt 4 „Stufe 4: Koordinaten und Darstellungsmatrix“
- HöMa1, Kapitel 10, Abschnitt 5 „Stufe 5: Hintereinanderausführen ist Multiplizieren“
- HöMa1, Kapitel 10, Abschnitt 6 „Stufe 6: Gleichungssysteme fragen rückwärts“
- HöMa1, Kapitel 10, Abschnitt 7 „Stufe 7: Der Gauß-Algorithmus“
- HöMa1, Kapitel 10, Abschnitt 8 „Stufe 8: Rang und Inverse“

## Elektrotechnik / 3. Semester / HöMa3 – Höhere Mathematik 3

### HöMa3, Kapitel 1: Differentialrechnung für Vektorfelder (`Kap1_Vektorfelder`, Modul hm3)

- HöMa3, Kapitel 1, Abschnitt 1 „Differenzierbarkeit und Kettenregel für Abbildungen“: 1.1 Was du dafür brauchst: Vektoren im $\mathbb{R}^n$ · 1.2 Was du dafür brauchst: das Skalarprodukt · 1.3 Was du dafür brauchst: Matrizen und Matrixprodukt · 1.4 Was du dafür brauchst: Transponieren und symmetrische Matrizen · 1.5 Was du dafür brauchst: Funktionen mehrerer Variablen · 1.6 Was du dafür brauchst: Grenzwert und Stetigkeit in mehreren Variablen · 1.7 Was du dafür brauchst: Partielle Ableitungen · 1.8 Was du dafür brauchst: Höhere partielle Ableitungen · 1.9 Was du dafür brauchst: Offene Mengen · 1.10 Abbildungen mit mehreren Ausgängen · 1.11 Vektorfelder · 1.12 Die Jacobi-Matrix · 1.13 Der Gradient · 1.14 Das Nabla-Symbol · 1.15 Gradient und Jacobi-Matrix: Spalte und Zeile · 1.16 Differentialoperatoren · 1.17 Totale Differenzierbarkeit · 1.18 Die Tangentialebene · 1.19 Partielle Ableitungen allein reichen nicht · 1.20 Stetig differenzierbar · 1.21 Mehrfach stetig differenzierbar · 1.22 Das Lemma von Schwarz · 1.23 Gradientenfelder und Skalarpotentiale · 1.24 Die Jacobi-Matrix eines Gradientenfelds ist symmetrisch · 1.25 Die Kettenregel · 1.26 Kurven · 1.27 Die Ableitung längs einer Kurve · 1.28 Die Richtungsableitung · 1.29 Wohin der Gradient zeigt · 1.30 Feldlinien · 1.31 Potentialfelder in der Physik · 1.32 Aufgaben
- HöMa3, Kapitel 1, Abschnitt 2 „Radialsymmetrische Funktionen und Felder“: 2.1 Was du dafür brauchst: Stammfunktionen · 2.2 Was du dafür brauchst: Kugelflächen · 2.3 Radialsymmetrische Funktionen · 2.4 Der radiale Einheitsvektor · 2.5 Der Gradient einer radialsymmetrischen Funktion · 2.6 Das Coulomb-Potential · 2.7 Zentralfelder · 2.8 Radialsymmetrische Vektorfelder · 2.9 Radialsymmetrische Vektorfelder sind Gradientenfelder · 2.10 Welche Zentralfelder Gradientenfelder sind · 2.11 Aufgaben
- HöMa3, Kapitel 1, Abschnitt 3 „Divergenz, Rotation und Laplace-Operator“: 3.1 Was du dafür brauchst: das Kreuzprodukt · 3.2 Was du dafür brauchst: Determinanten · 3.3 Was du dafür brauchst: die Spur einer Matrix · 3.4 Was du dafür brauchst: schiefsymmetrische Matrizen · 3.5 Die Divergenz · 3.6 Die Divergenz eines Gradientenfelds · 3.7 Der Laplace-Operator · 3.8 Harmonische Funktionen · 3.9 Die Produktregel der Divergenz · 3.10 Die Divergenz radialsymmetrischer Felder · 3.11 Das Coulomb-Potential ist harmonisch · 3.12 Die Rotation im Raum · 3.13 Levi-Civita-Symbole · 3.14 Die Rotation als Determinante · 3.15 Die Rotation in der Ebene · 3.16 Drehen um einen rechten Winkel vertauscht Divergenz und Rotation · 3.17 Eine Rotation für jede Dimension · 3.18 Die Integrabilitätsbedingungen · 3.19 Notwendig, aber nicht hinreichend · 3.20 Ein Skalarpotential ausrechnen · 3.21 Aufgaben
- HöMa3, Kapitel 1, Abschnitt 4 „Rechenregeln und Identitäten für Divergenz und Rotation“: 4.1 Was du dafür brauchst: das Kronecker-Symbol · 4.2 Was du dafür brauchst: das Spatprodukt · 4.3 Was du dafür brauchst: die Graßmann-Identität · 4.4 Rechnen mit dem Nabla-Symbol · 4.5 Produktregeln mit einer skalaren Funktion · 4.6 Die Produktregel der Rotation in der Ebene · 4.7 Die Ableitung eines Felds in Richtung eines anderen Felds · 4.8 Produktregeln mit dem Kreuzprodukt · 4.9 Rotationsfelder sind divergenzfrei · 4.10 Die doppelte Rotation · 4.11 Wirbelfelder und Vektorpotentiale · 4.12 Eichfreiheit · 4.13 Die Coulomb-Eichung · 4.14 Aufgaben

### HöMa3, Kapitel 2: Integralrechnung im Rⁿ (`Kap2_Integrale`, Modul hm3)

- HöMa3, Kapitel 2, Abschnitt 1 „Integrale mit Parameter über endlichen Intervallen“: 1.1 Was du dafür brauchst: das bestimmte Integral · 1.2 Was du dafür brauchst: der Hauptsatz · 1.3 Was du dafür brauchst: der Mittelwertsatz · 1.4 Was du dafür brauchst: abgeschlossene, beschränkte und kompakte Mengen · 1.5 Was du dafür brauchst: Stetigkeit mit $\varepsilon$ und $\delta$ · 1.6 Was du dafür brauchst: gleichmäßige Stetigkeit · 1.7 Das Parameterintegral · 1.8 Die Stetigkeit des Parameterintegrals · 1.9 Ableiten unter dem Integralzeichen · 1.10 Parameter aus einem abgeschlossenen Intervall · 1.11 Grenzen, die vom Parameter abhängen: die Leibnizregel · 1.12 Aufgaben
- HöMa3, Kapitel 2, Abschnitt 2 „Uneigentliche Parameterintegrale“: 2.1 Was du dafür brauchst: Supremum und Maximum · 2.2 Was du dafür brauchst: uneigentliche Integrale · 2.3 Was du dafür brauchst: absolute Konvergenz und Vergleich · 2.4 Was du dafür brauchst: die Substitutionsregel · 2.5 Was du dafür brauchst: Integrale komplexer Funktionen · 2.6 Das uneigentliche Parameterintegral · 2.7 Ein stetiger Integrand mit unstetigem Integral · 2.8 Gleichmäßige Konvergenz · 2.9 Majorante und Majorantenkriterium · 2.10 Die Fourier-Transformation · 2.11 Lokale Majoranten · 2.12 Die Gamma-Funktion · 2.13 Die Laplace-Transformation · 2.14 Aufgaben
- HöMa3, Kapitel 2, Abschnitt 3 „Mehrfachintegrale“: 3.1 Was du dafür brauchst: Quader · 3.2 Was du dafür brauchst: der Abschluss einer Menge · 3.3 Das iterierte Integral · 3.4 Der Satz von Fubini · 3.5 Das Mehrfachintegral · 3.6 Linearität und Monotonie · 3.7 Funktionen mit kompaktem Träger · 3.8 Über stetige Funktionen hinaus: das Lebesgue-Integral · 3.9 Aufgaben
- HöMa3, Kapitel 2, Abschnitt 4 „Integration über Mengen und Berechnung von Volumina“: 4.1 Das Integral über eine Menge · 4.2 Volumen und Flächeninhalt · 4.3 Das Prinzip von Cavalieri · 4.4 Aufgaben
- HöMa3, Kapitel 2, Abschnitt 5 „Integration über Normalbereiche“: 5.1 Normalbereiche · 5.2 Integration über Normalbereiche · 5.3 Zerlegung in reguläre Normalbereiche · 5.4 Räumliche Normalbereiche · 5.5 Aufgaben

### HöMa3, Kapitel 3: Kurvenintegrale (`Kap3_Kurvenintegrale`, Modul hm3)

- HöMa3, Kapitel 3, Abschnitt 1 „Integration längs regulärer Kurven“: 1.1 Was du dafür brauchst: Kurven und einseitige Ableitungen · 1.2 Was du dafür brauchst: streng monotone Funktionen und Umkehrfunktionen · 1.3 Was du dafür brauchst: die Cauchy-Schwarz-Ungleichung · 1.4 Stückweise stetig differenzierbare Kurven · 1.5 Reguläre Parametrisierung · 1.6 Geschlossene Kurven · 1.7 Einfache Kurven · 1.8 Das Kurvenintegral · 1.9 Linearität · 1.10 Umparametrisierung und Parameterinvarianz · 1.11 Entgegengesetzt durchlaufene Kurven · 1.12 Spur, reguläre Kurve und Orientierung · 1.13 Der Anfangspunkt einer geschlossenen Kurve · 1.14 Zusammengesetzte Kurven · 1.15 Linienelement und Einheitstangentenvektor · 1.16 Die Kurvenlänge · 1.17 Parametrisierung nach der Bogenlänge · 1.18 Die Standardabschätzung · 1.19 Aufgaben
- HöMa3, Kapitel 3, Abschnitt 2 „Erster Hauptsatz für Kurvenintegrale“: 2.1 Was du dafür brauchst: der Mittelwertsatz der Integralrechnung · 2.2 Gebiete · 2.3 Wegunabhängige Kurvenintegrale und konservative Felder · 2.4 Rundwege · 2.5 Der erste Hauptsatz · 2.6 Arbeit und Spannung in konservativen Feldern · 2.7 Konservative Felder sind rotationsfrei · 2.8 Ein rotationsfreies Feld, das nicht konservativ ist · 2.9 Aufgaben

### HöMa3, Kapitel 4: Koordinatentransformationen (`Kap4_Koordinaten`, Modul hm3)

- HöMa3, Kapitel 4, Abschnitt 1 „Stufe 1: Der Transformationssatz“
- HöMa3, Kapitel 4, Abschnitt 2 „Stufe 2: Der Beweis in der Ebene“
- HöMa3, Kapitel 4, Abschnitt 3 „Stufe 3: Polarkoordinaten“
- HöMa3, Kapitel 4, Abschnitt 4 „Stufe 4: Zylinder- und Kugelkoordinaten“
- HöMa3, Kapitel 4, Abschnitt 5 „Stufe 5: Integrale über eine Singularität“
- HöMa3, Kapitel 4, Abschnitt 6 „Stufe 6: Das Newtonpotential“
- HöMa3, Kapitel 4, Abschnitt 7 „Stufe 7: Krummlinige Koordinaten und der Gradient“
- HöMa3, Kapitel 4, Abschnitt 8 „Stufe 8: Divergenz und Laplace-Operator“

### HöMa3, Kapitel 5: Integralsätze im Raum (`Kap5_Integralsaetze`, Modul hm3)

- HöMa3, Kapitel 5, Abschnitt 1 „Stufe 1: Flächen beschreiben“
- HöMa3, Kapitel 5, Abschnitt 2 „Stufe 2: Das Oberflächenelement“
- HöMa3, Kapitel 5, Abschnitt 3 „Stufe 3: Drei Standardfälle“
- HöMa3, Kapitel 5, Abschnitt 4 „Stufe 4: Orientierung und Flussintegral“
- HöMa3, Kapitel 5, Abschnitt 5 „Stufe 5: Warum die Parametrisierung egal ist“
- HöMa3, Kapitel 5, Abschnitt 6 „Stufe 6: Der Satz von Stokes“
- HöMa3, Kapitel 5, Abschnitt 7 „Stufe 7: Wann ein Feld eine Rotation ist“
- HöMa3, Kapitel 5, Abschnitt 8 „Stufe 8: Der Satz von Gauß“
- HöMa3, Kapitel 5, Abschnitt 9 „Stufe 9: Poisson-Gleichung“
- HöMa3, Kapitel 5, Abschnitt 10 „Stufe 10: Der Hauptsatz der Vektoranalysis“

### HöMa3, Kapitel 6: Konvergenz von Funktionenfolgen (`Kap6_Funktionenfolgen`, Modul hm3)

- HöMa3, Kapitel 6, Abschnitt 1 „Stufe 1: Punktweise Konvergenz“
- HöMa3, Kapitel 6, Abschnitt 2 „Stufe 2: Gleichmäßige Konvergenz“
- HöMa3, Kapitel 6, Abschnitt 3 „Stufe 3: Stetigkeit und Integral bleiben erhalten“
- HöMa3, Kapitel 6, Abschnitt 4 „Stufe 4: Die Ableitung braucht mehr“
- HöMa3, Kapitel 6, Abschnitt 5 „Stufe 5: Funktionenreihen und der M-Test“
- HöMa3, Kapitel 6, Abschnitt 6 „Stufe 6: Potenzreihen“
- HöMa3, Kapitel 6, Abschnitt 7 „Stufe 7: Funktionen als Punkte eines Raums“
- HöMa3, Kapitel 6, Abschnitt 8 „Stufe 8: Konvergenz im quadratischen Mittel“

### HöMa3, Kapitel 7: Fourier-Reihen (`Kap7_Fourier`, Modul hm3)

- HöMa3, Kapitel 7, Abschnitt 1 „Stufe 1: Schwingungen als Bausteine“
- HöMa3, Kapitel 7, Abschnitt 2 „Stufe 2: Koeffizienten und Polynome“
- HöMa3, Kapitel 7, Abschnitt 3 „Stufe 3: Rechenregeln“
- HöMa3, Kapitel 7, Abschnitt 4 „Stufe 4: Der Sägezahn zu Fuß“
- HöMa3, Kapitel 7, Abschnitt 5 „Stufe 5: Die beste Näherung“
- HöMa3, Kapitel 7, Abschnitt 6 „Stufe 6: Konvergenz im quadratischen Mittel“
- HöMa3, Kapitel 7, Abschnitt 7 „Stufe 7: Mitteln mit Dirac-Scharen“
- HöMa3, Kapitel 7, Abschnitt 8 „Stufe 8: Punktweise Konvergenz“
- HöMa3, Kapitel 7, Abschnitt 9 „Stufe 9: Gleichmäßige Konvergenz und Glattheit“
- HöMa3, Kapitel 7, Abschnitt 10 „Stufe 10: Das Dirichlet-Problem“

### HöMa3, Kapitel 8: Wahrscheinlichkeitsrechnung (`Kap8_Wahrscheinlichkeit`, Modul hm3)

- HöMa3, Kapitel 8, Abschnitt 1 „Stufe 1: Ereignisse und Wahrscheinlichkeit“
- HöMa3, Kapitel 8, Abschnitt 2 „Stufe 2: Zählen“
- HöMa3, Kapitel 8, Abschnitt 3 „Stufe 3: Zusatzwissen, Unabhängigkeit und Bayes“
- HöMa3, Kapitel 8, Abschnitt 4 „Stufe 4: Zufallsvariablen und Verteilungsfunktion“
- HöMa3, Kapitel 8, Abschnitt 5 „Stufe 5: Drei diskrete Verteilungen“
- HöMa3, Kapitel 8, Abschnitt 6 „Stufe 6: Dichten“
- HöMa3, Kapitel 8, Abschnitt 7 „Stufe 7: Der Erwartungswert“
- HöMa3, Kapitel 8, Abschnitt 8 „Stufe 8: Varianz, Kovarianz und Tschebyschew“
- HöMa3, Kapitel 8, Abschnitt 9 „Stufe 9: Unabhängige Zufallsvariablen“
- HöMa3, Kapitel 8, Abschnitt 10 „Stufe 10: Zufallsvektoren mit Dichte“
- HöMa3, Kapitel 8, Abschnitt 11 „Stufe 11: Das Gesetz der großen Zahlen“
- HöMa3, Kapitel 8, Abschnitt 12 „Stufe 12: Der zentrale Grenzwertsatz“

## Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme

### ET3, Kapitel 1: LTI-Systeme und Faltung (`Kap1_Faltung`, Modul et3)

- ET3, Kapitel 1, Abschnitt 1 „Stufe 1: Signale beschreiben“
- ET3, Kapitel 1, Abschnitt 2 „Stufe 2: Ein erstes System, das RC-Glied“
- ET3, Kapitel 1, Abschnitt 3 „Stufe 3: Was ein LTI-System ist“
- ET3, Kapitel 1, Abschnitt 4 „Stufe 4: Das Faltungsintegral“
- ET3, Kapitel 1, Abschnitt 5 „Stufe 5: Die Faltung ausrechnen“
- ET3, Kapitel 1, Abschnitt 6 „Stufe 6: Rechenregeln der Faltung“
- ET3, Kapitel 1, Abschnitt 7 „Stufe 7: Der Dirac-Impuls“
- ET3, Kapitel 1, Abschnitt 8 „Stufe 8: Integrieren und Differenzieren“
- ET3, Kapitel 1, Abschnitt 9 „Stufe 9: Kausal und stabil“
- ET3, Kapitel 1, Abschnitt 10 „Stufe 10: Faltung ganz ohne System“

### ET3, Kapitel 2: Laplace-Transformation (`Kap2_Laplace`, Modul et3)

- ET3, Kapitel 2, Abschnitt 1 „Eigenfunktionen von LTI-Systemen“: 1.1 Was du dafür brauchst: die komplexe Exponentialfunktion · 1.2 Rückblick: die Antwort eines LTI-Systems · 1.3 Eigenfunktion und Eigenwert · 1.4 Die Exponentialfunktion $\mathrm{e}^{pt}$ als Eigenfunktion · 1.5 Die komplexe Frequenz und die $p$-Ebene · 1.6 Die Laplace-Übertragungsfunktion · 1.7 Zwei Systeme in Kette · 1.8 Die Laplace-Transformation eines Signals · 1.9 Die einseitige Laplace-Transformation
- ET3, Kapitel 2, Abschnitt 2 „Beispiele zur Laplace-Transformation“: 2.1 Der rechtsseitige Exponentialimpuls · 2.2 Der Konvergenzbereich · 2.3 Der linksseitige Exponentialimpuls · 2.4 Summen von Signalen · 2.5 Der zweiseitige Exponentialimpuls · 2.6 Polstellen · 2.7 Eine Summe aus drei Exponentialimpulsen · 2.8 Die Grundpaare
- ET3, Kapitel 2, Abschnitt 3 „Pole und Nullstellen in der $p$-Ebene“: 3.1 Nullstellen · 3.2 Die Produktform · 3.3 Das Pol-Nullstellen-Diagramm · 3.4 Wo der Konvergenzbereich liegt · 3.5 Faltung wird Multiplikation · 3.6 Ableiten im Zeitbereich · 3.7 Integrieren im Zeitbereich · 3.8 Der Dirac-Impuls
- ET3, Kapitel 2, Abschnitt 4 „Lösung von Differentialgleichungen“: 4.1 Lineare Differentialgleichungen mit konstanten Koeffizienten · 4.2 Die Gleichung im Bildbereich · 4.3 Die Übertragungsfunktion als Polynombruch · 4.4 Beispiel: das RLC-System · 4.5 Partialbruchzerlegung · 4.6 Zurück in den Zeitbereich · 4.7 Die Impulsantwort des RLC-Systems · 4.8 Konjugiert komplexe Polpaare · 4.9 Mehrfache Pole
- ET3, Kapitel 2, Abschnitt 5 „Stabilität“: 5.1 Rückblick: Stabilität im Zeitbereich · 5.2 Die Bedingung in der $p$-Ebene · 5.3 Beispiel: ein wachsender Exponentialimpuls · 5.4 Beispiel: ein System zweiter Ordnung
- ET3, Kapitel 2, Abschnitt 6 „Systemanalyse und -synthese“: 6.1 Rückkopplung · 6.2 Grundbausteine · 6.3 Ein System erster Ordnung aus Grundbausteinen · 6.4 Drei Aufbauten eines Systems zweiter Ordnung · 6.5 Die direkte Form · 6.6 Bauelemente im Bildbereich · 6.7 Ein System aus Messungen bestimmen
- ET3, Kapitel 2, Abschnitt 7 „Tabellen und Umkehrformel“: 7.1 Rechenregeln · 7.2 Transformationspaare · 7.3 Die Umkehrformel

### ET3, Kapitel 3: Fourier-Reihe und -Transformation (`Kap3_Fourier`, Modul et3)

- ET3, Kapitel 3, Abschnitt 1 „Stufe 1: Schwingungen als Eigenfunktionen“
- ET3, Kapitel 3, Abschnitt 2 „Stufe 2: Periodische Signale, die Fourier-Reihe“
- ET3, Kapitel 3, Abschnitt 3 „Stufe 3: Leistung, Konvergenz und LTI-Systeme“
- ET3, Kapitel 3, Abschnitt 4 „Stufe 4: Vom periodischen zum einmaligen Signal“
- ET3, Kapitel 3, Abschnitt 5 „Stufe 5: Symmetrien im Signal und im Spektrum“
- ET3, Kapitel 3, Abschnitt 6 „Stufe 6: Die Rechenregeln (Theoreme)“
- ET3, Kapitel 3, Abschnitt 7 „Stufe 7: Rechteck, si-Funktion und Dreieck“
- ET3, Kapitel 3, Abschnitt 8 „Stufe 8: Singuläre Signale und Linienspektren“
- ET3, Kapitel 3, Abschnitt 9 „Stufe 9: Hilbert-Transformation und analytisches Signal“
- ET3, Kapitel 3, Abschnitt 10 „Stufe 10: Kurzzeit-Fourier-Transformation“
- ET3, Kapitel 3, Abschnitt 11 „Stufe 11: Fourier und Laplace, Grenzen der Existenz“

### ET3, Kapitel 4: Abtastung und zeitdiskrete Systeme (`Kap4_Diskret`, Modul et3)

- ET3, Kapitel 4, Abschnitt 1 „Stufe 1: Signalklassen und ideale Abtastung“
- ET3, Kapitel 4, Abschnitt 2 „Stufe 2: Das Spektrum des abgetasteten Signals“
- ET3, Kapitel 4, Abschnitt 3 „Stufe 3: Abtasttheorem und Rückgewinnung“
- ET3, Kapitel 4, Abschnitt 4 „Stufe 4: Abtastung im Frequenzbereich“
- ET3, Kapitel 4, Abschnitt 5 „Stufe 5: Zeitdiskrete Signale und die diskrete Faltung“
- ET3, Kapitel 4, Abschnitt 6 „Stufe 6: Ein rekursives System“
- ET3, Kapitel 4, Abschnitt 7 „Stufe 7: Fourier-Transformation zeitdiskreter Signale“
- ET3, Kapitel 4, Abschnitt 8 „Stufe 8: Die diskrete Fourier-Transformation (DFT)“
- ET3, Kapitel 4, Abschnitt 9 „Stufe 9: FFT und schnelle Faltung“
- ET3, Kapitel 4, Abschnitt 10 „Stufe 10: Abtastrate ändern, Dezimation und Interpolation“
- ET3, Kapitel 4, Abschnitt 11 „Stufe 11: Die z-Transformation“

### ET3, Kapitel 5: Tiefpass- und Bandpasssysteme (`Kap5_Tiefpass`, Modul et3)

- ET3, Kapitel 5, Abschnitt 1 „Stufe 1: Das verzerrungsfreie System“
- ET3, Kapitel 5, Abschnitt 2 „Stufe 2: Der ideale Tiefpass“
- ET3, Kapitel 5, Abschnitt 3 „Stufe 3: Sprungantwort und Einschwingzeit“
- ET3, Kapitel 5, Abschnitt 4 „Stufe 4: Kausale Näherung“
- ET3, Kapitel 5, Abschnitt 5 „Stufe 5: Echomethode und Pulsformfilter“
- ET3, Kapitel 5, Abschnitt 6 „Stufe 6: Zeitdiskrete Tiefpässe, Entwurf mit Fenstern“
- ET3, Kapitel 5, Abschnitt 7 „Stufe 7: Der ideale Bandpass und sein äquivalenter Tiefpass“
- ET3, Kapitel 5, Abschnitt 8 „Stufe 8: Komplexe Hüllkurve und Quadraturkomponenten“
- ET3, Kapitel 5, Abschnitt 9 „Stufe 9: Bandpasssignal durch Bandpasssystem“
- ET3, Kapitel 5, Abschnitt 10 „Stufe 10: Quadraturschaltung und Bandpass-Abtastung“
- ET3, Kapitel 5, Abschnitt 11 „Stufe 11: Phasen- und Gruppenlaufzeit beim Bandpass“
- ET3, Kapitel 5, Abschnitt 12 „Stufe 12: Zeitdiskrete Bandpässe und Hochpässe“

### ET3, Kapitel 6: Korrelationsfunktionen (`Kap6_Korrelation`, Modul et3)

- ET3, Kapitel 6, Abschnitt 1 „Stufe 1: Energie und Leistung“
- ET3, Kapitel 6, Abschnitt 2 „Stufe 2: Ähnlichkeit messen, der Korrelationskoeffizient“
- ET3, Kapitel 6, Abschnitt 3 „Stufe 3: Korrelationsfunktion und Korrelationsprodukt“
- ET3, Kapitel 6, Abschnitt 4 „Stufe 4: Energiedichtespektrum“
- ET3, Kapitel 6, Abschnitt 5 „Stufe 5: Korrelation und LTI-Systeme“
- ET3, Kapitel 6, Abschnitt 6 „Stufe 6: Korrelation von Bandpasssignalen“
- ET3, Kapitel 6, Abschnitt 7 „Stufe 7: Zeitdiskrete und periodische Korrelation“

### ET3, Kapitel 7: Zufallssignale (`Kap7_Statistik`, Modul et3)

- ET3, Kapitel 7, Abschnitt 1 „Stufe 1: Der Zufallsprozess“
- ET3, Kapitel 7, Abschnitt 2 „Stufe 2: Stationarität und Ergodizität“
- ET3, Kapitel 7, Abschnitt 3 „Stufe 3: Mittelwert, Leistung, Varianz“
- ET3, Kapitel 7, Abschnitt 4 „Stufe 4: Autokorrelation, Kovarianz und Kreuzkorrelation“
- ET3, Kapitel 7, Abschnitt 5 „Stufe 5: Verteilungsfunktion und Verteilungsdichte“
- ET3, Kapitel 7, Abschnitt 6 „Stufe 6: Verbundverteilung, Unabhängigkeit, Unkorreliertheit“
- ET3, Kapitel 7, Abschnitt 7 „Stufe 7: Die Gauß-Verteilung“
- ET3, Kapitel 7, Abschnitt 8 „Stufe 8: Zufallssignale in LTI-Systemen, Leistungsdichte“
- ET3, Kapitel 7, Abschnitt 9 „Stufe 9: Weißes Rauschen und thermisches Rauschen“
- ET3, Kapitel 7, Abschnitt 10 „Stufe 10: Das Korrelationsfilter (Matched Filter)“
- ET3, Kapitel 7, Abschnitt 11 „Stufe 11: Fehlerwahrscheinlichkeit beim Binärempfang“
- ET3, Kapitel 7, Abschnitt 12 „Stufe 12: Zeitdiskrete Zufallssignale“

### ET3, Kapitel 8: Orthogonalentwicklung und Leitungen (`Kap8_Zusatz`, Modul et3)

- ET3, Kapitel 8, Abschnitt 1 „Stufe 1: Signale als Vektoren, die Orthogonalentwicklung“
- ET3, Kapitel 8, Abschnitt 2 „Stufe 2: Die Leitungsgleichungen“
- ET3, Kapitel 8, Abschnitt 3 „Stufe 3: Wellen bei sinusförmiger Anregung“
- ET3, Kapitel 8, Abschnitt 4 „Stufe 4: Die verlustlose Leitung“

## Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1

### GEMB1, Kapitel 1: Welle, Teilchen und Schrödinger-Gleichung (`Kap1_Schroedinger`, Modul gemb1)

- GEMB1, Kapitel 1, Abschnitt 1 „Stufe 1: Elektronen als Gas“
- GEMB1, Kapitel 1, Abschnitt 2 „Stufe 2: Teilchen und Wellen“
- GEMB1, Kapitel 1, Abschnitt 3 „Stufe 3: Die Wellenfunktion und ihre Deutung“
- GEMB1, Kapitel 1, Abschnitt 4 „Stufe 4: Die Schrödinger-Gleichung“
- GEMB1, Kapitel 1, Abschnitt 5 „Stufe 5: Freies Elektron, ebene Welle, Dispersion“
- GEMB1, Kapitel 1, Abschnitt 6 „Stufe 6: Das Wellenpaket“
- GEMB1, Kapitel 1, Abschnitt 7 „Stufe 7: Was die Parabel verrät“

### GEMB1, Kapitel 2: Das Teilchen in der Box (`Kap2_Box`, Modul gemb1)

- GEMB1, Kapitel 2, Abschnitt 1 „Stufe 1: Die Schrödinger-Gleichung auf einem Gitter“
- GEMB1, Kapitel 2, Abschnitt 2 „Stufe 2: Das Kosinus-Band“
- GEMB1, Kapitel 2, Abschnitt 3 „Stufe 3: Das Elektron zwischen zwei Wänden“
- GEMB1, Kapitel 2, Abschnitt 4 „Stufe 4: Die Box in der Ebene“
- GEMB1, Kapitel 2, Abschnitt 5 „Stufe 5: Gleiche Energie, verschiedene Zustände“
- GEMB1, Kapitel 2, Abschnitt 6 „Stufe 6: Die Box im Raum“
- GEMB1, Kapitel 2, Abschnitt 7 „Stufe 7: Ergänzung: Quantenfilm, Draht und Punkt“
- GEMB1, Kapitel 2, Abschnitt 8 „Stufe 8: Ergänzung: Zustandsdichten in Potentialkästen“

### GEMB1, Kapitel 3: Stufe, Barriere und Tunneleffekt (`Kap3_Tunnel`, Modul gemb1)

- GEMB1, Kapitel 3, Abschnitt 1 „Stufe 1: Zwei Gebiete an einer Kante zusammensetzen“
- GEMB1, Kapitel 3, Abschnitt 2 „Stufe 2: Reflexion trotz genügender Energie“
- GEMB1, Kapitel 3, Abschnitt 3 „Stufe 3: Die Welle dringt in die Wand ein“
- GEMB1, Kapitel 3, Abschnitt 4 „Stufe 4: Tunneln durch eine dünne Wand“
- GEMB1, Kapitel 3, Abschnitt 5 „Stufe 5: Die dicke Barriere“
- GEMB1, Kapitel 3, Abschnitt 6 „Stufe 6: Die Box mit endlich hohen Wänden“
- GEMB1, Kapitel 3, Abschnitt 7 „Stufe 7: Ergänzung: Scharfe Stufen und Nachweise“

### GEMB1, Kapitel 4: Atome und Orbitale (`Kap4_Atome`, Modul gemb1)

- GEMB1, Kapitel 4, Abschnitt 1 „Stufe 1: Der Kern als Kasten ohne Wände“
- GEMB1, Kapitel 4, Abschnitt 2 „Stufe 2: Das Wasserstoffatom“
- GEMB1, Kapitel 4, Abschnitt 3 „Stufe 3: Drei Quantenzahlen“
- GEMB1, Kapitel 4, Abschnitt 4 „Stufe 4: Die Formen der Orbitale“
- GEMB1, Kapitel 4, Abschnitt 5 „Stufe 5: Spin und Pauli-Prinzip“
- GEMB1, Kapitel 4, Abschnitt 6 „Stufe 6: Besetzung der Orbitale und Hundsche Regel“
- GEMB1, Kapitel 4, Abschnitt 7 „Stufe 7: Ergänzung: Das Periodensystem der Elemente“
- GEMB1, Kapitel 4, Abschnitt 8 „Stufe 8: Ergänzung: Elektronegativität und Valenz“

### GEMB1, Kapitel 5: Chemische Bindung (`Kap5_Bindung`, Modul gemb1)

- GEMB1, Kapitel 5, Abschnitt 1 „Stufe 1: Die Energiekurve der Bindung“
- GEMB1, Kapitel 5, Abschnitt 2 „Stufe 2: Ionische Bindung“
- GEMB1, Kapitel 5, Abschnitt 3 „Stufe 3: Zwei Atome teilen Elektronen“
- GEMB1, Kapitel 5, Abschnitt 4 „Stufe 4: Richtung und Vorzeichen der Orbitale“
- GEMB1, Kapitel 5, Abschnitt 5 „Stufe 5: Hybridisierung im Tetraeder“
- GEMB1, Kapitel 5, Abschnitt 6 „Stufe 6: Mehrfachbindungen und bewegliche Elektronen“
- GEMB1, Kapitel 5, Abschnitt 7 „Stufe 7: Metallische Bindung“
- GEMB1, Kapitel 5, Abschnitt 8 „Stufe 8: Dipol-Bindungen und reale Materialien“

### GEMB1, Kapitel 6: Kristallgitter (`Kap6_Kristall`, Modul gemb1)

- GEMB1, Kapitel 6, Abschnitt 1 „Stufe 1: Punktgitter und Basis“
- GEMB1, Kapitel 6, Abschnitt 2 „Stufe 2: Bravais-Gitter in einer und zwei Dimensionen“
- GEMB1, Kapitel 6, Abschnitt 3 „Stufe 3: Die Wigner-Seitz-Zelle“
- GEMB1, Kapitel 6, Abschnitt 4 „Stufe 4: Drei Dimensionen“
- GEMB1, Kapitel 6, Abschnitt 5 „Stufe 5: Koordinationszahl und Packungsdichte“
- GEMB1, Kapitel 6, Abschnitt 6 „Stufe 6: Punkte, Ebenen und Richtungen“
- GEMB1, Kapitel 6, Abschnitt 7 „Stufe 7: Beispiele für Kristallstrukturen“
- GEMB1, Kapitel 6, Abschnitt 8 „Stufe 8: Ergänzung: Ionenkristalle und Modifikationen“

### GEMB1, Kapitel 7: Kristallwachstum und reziprokes Gitter (`Kap7_Reziprok`, Modul gemb1)

- GEMB1, Kapitel 7, Abschnitt 1 „Stufe 1: Vom Quarz zum Rohsilizium“
- GEMB1, Kapitel 7, Abschnitt 2 „Stufe 2: Reinigung über die Gasphase“
- GEMB1, Kapitel 7, Abschnitt 3 „Stufe 3: Der Einkristall“
- GEMB1, Kapitel 7, Abschnitt 4 „Stufe 4: Das reziproke Gitter in einer Dimension“
- GEMB1, Kapitel 7, Abschnitt 5 „Stufe 5: Reziproke Gittervektoren in der Ebene und im Raum“
- GEMB1, Kapitel 7, Abschnitt 6 „Stufe 6: Die Brillouin-Zone“
- GEMB1, Kapitel 7, Abschnitt 7 „Stufe 7: Netzebenen und reziproke Vektoren“
- GEMB1, Kapitel 7, Abschnitt 8 „Stufe 8: Der Kristall im Überblick“

### GEMB1, Kapitel 8: Vom Atom zum Band (`Kap8_TightBinding`, Modul gemb1)

- GEMB1, Kapitel 8, Abschnitt 1 „Stufe 1: Was aus der Periodizität folgt“
- GEMB1, Kapitel 8, Abschnitt 2 „Stufe 2: Bänder und Lücken“
- GEMB1, Kapitel 8, Abschnitt 3 „Stufe 3: Zwei Atome“
- GEMB1, Kapitel 8, Abschnitt 4 „Stufe 4: Vier Atome und die Matrix“
- GEMB1, Kapitel 8, Abschnitt 5 „Stufe 5: Viele Atome“
- GEMB1, Kapitel 8, Abschnitt 6 „Stufe 6: Bandbreite, Abstand und Besetzung“
- GEMB1, Kapitel 8, Abschnitt 7 „Stufe 7: Zwei Orbitale je Atom“
- GEMB1, Kapitel 8, Abschnitt 8 „Stufe 8: Das Rezept“

### GEMB1, Kapitel 9: Bandstrukturen lesen (`Kap9_Bandstruktur`, Modul gemb1)

- GEMB1, Kapitel 9, Abschnitt 1 „Stufe 1: Das Band in der Ebene“
- GEMB1, Kapitel 9, Abschnitt 2 „Stufe 2: Graphen“
- GEMB1, Kapitel 9, Abschnitt 3 „Stufe 3: Silizium“
- GEMB1, Kapitel 9, Abschnitt 4 „Stufe 4: GaAs, direkte und indirekte Lücke“
- GEMB1, Kapitel 9, Abschnitt 5 „Stufe 5: Die effektive Masse im Kristall“
- GEMB1, Kapitel 9, Abschnitt 6 „Stufe 6: Masse und Richtung“
- GEMB1, Kapitel 9, Abschnitt 7 „Stufe 7: Das Loch“
- GEMB1, Kapitel 9, Abschnitt 8 „Stufe 8: Was man an einer Bandstruktur abliest“

### GEMB1, Kapitel 10: Zustandsdichte und Fermi-Verteilung (`Kap10_Fermi`, Modul gemb1)

- GEMB1, Kapitel 10, Abschnitt 1 „Stufe 1: Warum man Zustände zählt“
- GEMB1, Kapitel 10, Abschnitt 2 „Stufe 2: Kreisring und Kugelschale“
- GEMB1, Kapitel 10, Abschnitt 3 „Stufe 3: Leitungsband und Valenzband“
- GEMB1, Kapitel 10, Abschnitt 4 „Stufe 4: Anordnungen zählen“
- GEMB1, Kapitel 10, Abschnitt 5 „Stufe 5: Die Fermi-Verteilung“
- GEMB1, Kapitel 10, Abschnitt 6 „Stufe 6: Temperatur und Boltzmann-Näherung“
- GEMB1, Kapitel 10, Abschnitt 7 „Stufe 7: Elektronen und Löcher im Gleichgewicht“
- GEMB1, Kapitel 10, Abschnitt 8 „Stufe 8: Ergänzung: Das Metall als Potentialtopf“

### GEMB1, Kapitel 11: Eigenhalbleiter und Dotierung (`Kap11_Halbleiter`, Modul gemb1)

- GEMB1, Kapitel 11, Abschnitt 1 „Stufe 1: Welche Stoffe Halbleiter sind“
- GEMB1, Kapitel 11, Abschnitt 2 „Stufe 2: Der reine Kristall“
- GEMB1, Kapitel 11, Abschnitt 3 „Stufe 3: Fremdatome im Gitter“
- GEMB1, Kapitel 11, Abschnitt 4 „Stufe 4: Warum die Bindung so schwach ist“
- GEMB1, Kapitel 11, Abschnitt 5 „Stufe 5: Besetzung und Ladungsneutralität“
- GEMB1, Kapitel 11, Abschnitt 6 „Stufe 6: Hohe und mittlere Temperaturen“
- GEMB1, Kapitel 11, Abschnitt 7 „Stufe 7: Tiefe Temperaturen und die Lage von $E_\mathrm F$“
- GEMB1, Kapitel 11, Abschnitt 8 „Stufe 8: Hohe Dotierstoffdichten“

### GEMB1, Kapitel 12: Strom im Halbleiter (`Kap12_Transport`, Modul gemb1)

- GEMB1, Kapitel 12, Abschnitt 1 „Stufe 1: Strom aus besetzten Zuständen“
- GEMB1, Kapitel 12, Abschnitt 2 „Stufe 2: Ohne Stöße kein Gleichstrom“
- GEMB1, Kapitel 12, Abschnitt 3 „Stufe 3: Vom Wellenpaket zur Verteilungsfunktion“
- GEMB1, Kapitel 12, Abschnitt 4 „Stufe 4: Was das Gleichgewicht verlangt“
- GEMB1, Kapitel 12, Abschnitt 5 „Stufe 5: Der Streuterm und die Relaxationszeit“
- GEMB1, Kapitel 12, Abschnitt 6 „Stufe 6: Der stationäre Strom“
- GEMB1, Kapitel 12, Abschnitt 7 „Stufe 7: Beweglichkeit und Leitfähigkeit“
- GEMB1, Kapitel 12, Abschnitt 8 „Stufe 8: Ergänzung: Der Hall-Effekt“

### GEMB1, Kapitel 13: Diffusion, Rekombination und Grundgleichungen (`Kap13_Diffusion`, Modul gemb1)

- GEMB1, Kapitel 13, Abschnitt 1 „Stufe 1: Warum Teilchen ohne Kraft strömen“
- GEMB1, Kapitel 13, Abschnitt 2 „Stufe 2: Die Kontinuitätsgleichung“
- GEMB1, Kapitel 13, Abschnitt 3 „Stufe 3: Ergänzung: Diffusion aus unendlicher und endlicher Quelle“
- GEMB1, Kapitel 13, Abschnitt 4 „Stufe 4: Diffusionsstrom und Einstein-Beziehung“
- GEMB1, Kapitel 13, Abschnitt 5 „Stufe 5: Generation und Rekombination“
- GEMB1, Kapitel 13, Abschnitt 6 „Stufe 6: Die Grundgleichungen der Halbleiter“
- GEMB1, Kapitel 13, Abschnitt 7 „Stufe 7: Ergänzung: Raumladungen und Relaxation“
- GEMB1, Kapitel 13, Abschnitt 8 „Stufe 8: Die Diffusionslänge“

### GEMB1, Kapitel 14: Der p-n-Übergang (`Kap14_pn`, Modul gemb1)

- GEMB1, Kapitel 14, Abschnitt 1 „Stufe 1: Wie Ladung die Bänder verbiegt“
- GEMB1, Kapitel 14, Abschnitt 2 „Stufe 2: Der Übergang im Gleichgewicht“
- GEMB1, Kapitel 14, Abschnitt 3 „Stufe 3: Zwei Näherungen für die Ladung“
- GEMB1, Kapitel 14, Abschnitt 4 „Stufe 4: Feld, Potential und Weite der Zone“
- GEMB1, Kapitel 14, Abschnitt 5 „Stufe 5: Spannung anlegen“
- GEMB1, Kapitel 14, Abschnitt 6 „Stufe 6: Injektion und Minoritätsträger“
- GEMB1, Kapitel 14, Abschnitt 7 „Stufe 7: Die Diodenkennlinie“

### GEMB1, Kapitel 15: Die MOS-Kapazität (`Kap15_MOS`, Modul gemb1)

- GEMB1, Kapitel 15, Abschnitt 1 „Stufe 1: Drei Stoffe auf einer Energieskala“
- GEMB1, Kapitel 15, Abschnitt 2 „Stufe 2: Wie sich die Gatespannung aufteilt“
- GEMB1, Kapitel 15, Abschnitt 3 „Stufe 3: Abschirmung und Akkumulation“
- GEMB1, Kapitel 15, Abschnitt 4 „Stufe 4: Verarmung“
- GEMB1, Kapitel 15, Abschnitt 5 „Stufe 5: Inversion“
- GEMB1, Kapitel 15, Abschnitt 6 „Stufe 6: Die Schwellspannung“
- GEMB1, Kapitel 15, Abschnitt 7 „Stufe 7: Die Inversionsschicht als Quantentopf“
- GEMB1, Kapitel 15, Abschnitt 8 „Stufe 8: Die Kapazität in allen Bereichen“

### GEMB1, Kapitel 16: Der reale MOS-Kondensator (`Kap16_MOSreal`, Modul gemb1)

- GEMB1, Kapitel 16, Abschnitt 1 „Stufe 1: Verschiedene Austrittsarbeiten“
- GEMB1, Kapitel 16, Abschnitt 2 „Stufe 2: Feste Ladungen im Isolator“
- GEMB1, Kapitel 16, Abschnitt 3 „Stufe 3: Die reale Bilanz und die verschobene Schwelle“
- GEMB1, Kapitel 16, Abschnitt 4 „Stufe 4: Interfacezustände“
- GEMB1, Kapitel 16, Abschnitt 5 „Stufe 5: Kennlinien bei niedriger und hoher Frequenz“
- GEMB1, Kapitel 16, Abschnitt 6 „Stufe 6: Tiefenverarmung“
- GEMB1, Kapitel 16, Abschnitt 7 „Stufe 7: Messen und Auswerten“
- GEMB1, Kapitel 16, Abschnitt 8 „Stufe 8: Ergänzung: Charge-Coupled Devices“

### GEMB1, Kapitel 17: Der MOSFET (`Kap17_MOSFET`, Modul gemb1)

- GEMB1, Kapitel 17, Abschnitt 1 „Stufe 1: Zwei Kontakte am MOS-Kondensator“
- GEMB1, Kapitel 17, Abschnitt 2 „Stufe 2: Die Barriere im Kanal“
- GEMB1, Kapitel 17, Abschnitt 3 „Stufe 3: Gradual Channel Approximation“
- GEMB1, Kapitel 17, Abschnitt 4 „Stufe 4: Ausgangskennlinien“
- GEMB1, Kapitel 17, Abschnitt 5 „Stufe 5: Transferkennlinie und Schwellspannung“
- GEMB1, Kapitel 17, Abschnitt 6 „Stufe 6: Der Aus-Zustand“
- GEMB1, Kapitel 17, Abschnitt 7 „Stufe 7: Vier Typen von MOSFETs“
- GEMB1, Kapitel 17, Abschnitt 8 „Stufe 8: Ergänzung: Grundschaltungen“

### GEMB1, Kapitel 19: Licht und Laser (Ergänzung) (`Kap19_Licht`, Modul gemb1)

- GEMB1, Kapitel 19, Abschnitt 1 „Stufe 1: Absorption und Emission“
- GEMB1, Kapitel 19, Abschnitt 2 „Stufe 2: Fluoreszenz und Nanokristalle“
- GEMB1, Kapitel 19, Abschnitt 3 „Stufe 3: Spontane und stimulierte Emission“
- GEMB1, Kapitel 19, Abschnitt 4 „Stufe 4: Die Besetzungsumkehr“
- GEMB1, Kapitel 19, Abschnitt 5 „Stufe 5: Der Laser“

## Informatik / Programmieren / Python

### Python, Kapitel 1: Programme und der Python-Interpreter (`Kap1_Programme`, Modul prog)

- Python, Kapitel 1, Abschnitt 1 „Programme und Programmiersprachen“: 1.1 Das Programm · 1.2 Was der Prozessor versteht: Maschinenbefehle · 1.3 Die Programmiersprache · 1.4 Die Syntax · 1.5 Die Semantik · 1.6 Der Quelltext
- Python, Kapitel 1, Abschnitt 2 „Vom Quelltext zur Ausführung: Compiler und Interpreter“: 2.1 Der Compiler · 2.2 Der Interpreter · 2.3 Python und CPython · 2.4 Der Bytecode
- Python, Kapitel 1, Abschnitt 3 „Python einrichten“: 3.1 Was du dafür brauchst: ein Terminal öffnen · 3.2 Python unter Windows: der Python install manager · 3.3 Python unter Linux · 3.4 Die Versionsnummer
- Python, Kapitel 1, Abschnitt 4 „Der interaktive Modus“: 4.1 Der interaktive Modus · 4.2 Der Wert · 4.3 Der Ausdruck · 4.4 Rechnen wie mit dem Taschenrechner · 4.5 Das Rezept im interaktiven Modus: erst von Hand, dann fertig · 4.6 Text als Wert: die Zeichenkette · 4.7 Die Funktion · 4.8 Der Funktionsaufruf: `print`
- Python, Kapitel 1, Abschnitt 5 „Skripte schreiben und ausführen“: 5.1 Der Editor · 5.2 Das Skript · 5.3 Der Kommentar
- Python, Kapitel 1, Abschnitt 6 „Fehler lesen und verstehen“: 6.1 Der Syntaxfehler · 6.2 Der Laufzeitfehler · 6.3 Die Ausnahme · 6.4 Der Traceback · 6.5 Der Logikfehler

### Python, Kapitel 2: Werte, Typen und Variablen (`Kap2_Werte`, Modul prog)

- Python, Kapitel 2, Abschnitt 1 „Objekte und Typen“: 1.1 Das Objekt · 1.2 Der Typ · 1.3 Die Identität · 1.4 Die Methode
- Python, Kapitel 2, Abschnitt 2 „Ganze Zahlen und Rechenoperatoren“: 2.1 Der Typ `int` · 2.2 Operator und Operand · 2.3 Die Division · 2.4 Ganzzahldivision und Rest · 2.5 Die Potenz · 2.6 Die Rangfolge
- Python, Kapitel 2, Abschnitt 3 „Zahlen im Binärsystem“: 3.1 Das Stellenwertsystem · 3.2 Die Binärzahl · 3.3 Das Byte · 3.4 Ins Binärsystem umrechnen: erst von Hand, dann fertig · 3.5 Die Hexadezimalzahl · 3.6 Binärbrüche · 3.7 Das Verdopplungsverfahren
- Python, Kapitel 2, Abschnitt 4 „Gleitkommazahlen: der Typ `float`“: 4.1 Die Gleitkommadarstellung · 4.2 Der Typ `float` · 4.3 Das Exponentenfeld · 4.4 Das Mantissenfeld · 4.5 Einen `float` in seine Felder zerlegen · 4.6 Der Darstellungsfehler · 4.7 Die kürzeste Darstellung
- Python, Kapitel 2, Abschnitt 5 „Rechnen mit Gleitkommazahlen“: 5.1 Der Rundungsfehler einer Rechnung · 5.2 Die Maschinengenauigkeit · 5.3 Die Absorption · 5.4 Die Auslöschung · 5.5 Der Überlauf: `inf` · 5.6 Das ungültige Ergebnis: `nan`
- Python, Kapitel 2, Abschnitt 6 „Variablen: Namen für Objekte“: 6.1 Die Zuweisung · 6.2 Die Variable · 6.3 Neu binden statt kopieren · 6.4 Die Namensregeln · 6.5 Die erweiterte Zuweisung · 6.6 Variablen im Skript
- Python, Kapitel 2, Abschnitt 7 „Wahrheitswerte und Vergleiche“: 7.1 Der Typ `bool` · 7.2 Die Vergleichsoperatoren · 7.3 Gleitkommazahlen nicht auf Gleichheit prüfen · 7.4 Der Vergleich mit Toleranz · 7.5 Der Identitätsvergleich · 7.6 Der Wert `None`
- Python, Kapitel 2, Abschnitt 8 „Module: `math` und `sys`“: 8.1 Das Modul und `import` · 8.2 Das Modul `math` · 8.3 Der Toleranzvergleich, fertig: `math.isclose` · 8.4 Die Grenzen des Typs `float`, fertig: `sys.float_info`
- Python, Kapitel 2, Abschnitt 9 „Komplexe Zahlen“: 9.1 Was du dafür brauchst: komplexe Zahlen · 9.2 Der Typ `complex` · 9.3 Das Attribut: Real- und Imaginärteil · 9.4 Das Modul `cmath` · 9.5 Betrag und Phase: erst von Hand, dann fertig · 9.6 Anwendung: einen Punkt in der Ebene drehen
- Python, Kapitel 2, Abschnitt 10 „Zeichenketten, Eingabe und Ausgabe“: 10.1 Zeichenketten verketten und vervielfachen · 10.2 Der f-String · 10.3 Die Eingabe mit `input` · 10.4 Die Typumwandlung · 10.5 Runden: erst von Hand, dann fertig · 10.6 Anwendung: ein Rechner für das Lauftempo

### Python, Kapitel 3: Entscheidungen und Schleifen (`Kap3_Kontrollfluss`, Modul prog)

- Python, Kapitel 3, Abschnitt 1 „Bedingungen: Vergleiche und logische Operatoren“: 1.1 Rückblick: Wahrheitswerte und Vergleiche · 1.2 Verkettete Vergleiche · 1.3 Zeichenketten vergleichen · 1.4 Der Operator `not` · 1.5 Der Operator `and` · 1.6 Der Operator `or` · 1.7 Die Rangfolge der logischen Operatoren · 1.8 Die Kurzschlussauswertung · 1.9 Der Wahrheitswert von Objekten · 1.10 Was `and` und `or` als Ergebnis liefern
- Python, Kapitel 3, Abschnitt 2 „Entscheidungen: if, elif und else“: 2.1 Die bedingte Anweisung `if` · 2.2 Der Block und die Einrückung · 2.3 Die Alternative `else` · 2.4 Mehrere Fälle: `elif` · 2.5 Typische Fehler in Bedingungen · 2.6 Anwendung: eine Waage mit Unter- und Überlauf
- Python, Kapitel 3, Abschnitt 3 „Wiederholen mit while“: 3.1 Die `while`-Schleife · 3.2 Die Endlosschleife · 3.3 Die Gleitkomma-Falle · 3.4 Anwendung: Wie lange ein Tee zum Abkühlen braucht
- Python, Kapitel 3, Abschnitt 4 „Zählen mit for und range“: 4.1 Die `for`-Schleife · 4.2 Die Zahlenfolge `range` · 4.3 Gleitkomma-Schritte über einen ganzzahligen Zähler · 4.4 `for` oder `while`?
- Python, Kapitel 3, Abschnitt 5 „Schleifen steuern, verschachteln und Ergebnisse sammeln“: 5.1 Abbrechen mit `break` · 5.2 Überspringen mit `continue` · 5.3 Verschachtelte Schleifen · 5.4 Das Akkumulator-Muster · 5.5 Anwendung: Mittelwert und Maximum
- Python, Kapitel 3, Abschnitt 6 „Lösungen durch Probieren: Raten und Prüfen, Näherung mit Toleranz“: 6.1 Raten und Prüfen · 6.2 Die Näherung mit Toleranz · 6.3 Schrittweite und Toleranz
- Python, Kapitel 3, Abschnitt 7 „Die Bisektion“: 7.1 Was du dafür brauchst: der Zwischenwertsatz · 7.2 Das Bisektionsverfahren · 7.3 Die Wurzel durch Bisektion · 7.4 Die Schrittzahl der Bisektion
- Python, Kapitel 3, Abschnitt 8 „Das Newton-Verfahren“: 8.1 Was du dafür brauchst: Ableitung und Tangente · 8.2 Das Newton-Verfahren · 8.3 Die Wurzel durch Newton · 8.4 Die Konvergenzgeschwindigkeit · 8.5 Die Grenzen des Newton-Verfahrens · 8.6 Der fertige Weg: `math.sqrt`
- Python, Kapitel 3, Abschnitt 9 „Anwendung: der Zinssatz eines Ratenkredits“: 9.1 Was du dafür brauchst: Zinsen, Raten und Restschuld · 9.2 Der Zinssatz als Nullstelle · 9.3 Der Zinssatz durch Bisektion · 9.4 Der Zinssatz durch Newton

## Informatik / Linux und Kommandozeile

### Linux, Kapitel 1: Ein Linux zum Üben: WSL, virtuelle Maschine, Live-USB-Stick (`Kap1_Uebungslinux`, Modul linux)

- Linux, Kapitel 1, Abschnitt 1 „Betriebssystem, Kernel und Distribution“: 1.1 Das Betriebssystem · 1.2 Zwei Betriebsarten des Prozessors · 1.3 Der Kernel · 1.4 Der Systemaufruf · 1.5 Linux · 1.6 Die Distribution · 1.7 Version und Langzeitpflege
- Linux, Kapitel 1, Abschnitt 2 „Drei Wege zu einem eigenen Linux“: 2.1 Die drei Wege im Überblick · 2.2 Der Entscheidungsbaum · 2.3 Das Terminal
- Linux, Kapitel 1, Abschnitt 3 „Virtuelle Maschinen: der Rechner im Rechner“: 3.1 Die virtuelle Maschine · 3.2 Wirt und Gast · 3.3 Der Hypervisor · 3.4 Hardware-Virtualisierung · 3.5 Der Snapshot · 3.6 Das virtuelle Netz: NAT
- Linux, Kapitel 1, Abschnitt 4 „WSL 2: Linux neben Windows“: 4.1 Das Windows-Subsystem für Linux · 4.2 WSL 2 einrichten · 4.3 Die Distributionen anzeigen · 4.4 Das Terminal öffnen und prüfen · 4.5 Windows-Dateien in Linux: /mnt/c · 4.6 Linux-Dateien in Windows: der Explorer · 4.7 Wohin mit den Übungsdateien? · 4.8 Grenzen von WSL 2
- Linux, Kapitel 1, Abschnitt 5 „Datenträger, Abbild und Prüfsumme“: 5.1 Was du dafür brauchst: der Datenträger · 5.2 Was du dafür brauchst: die Partition · 5.3 Was du dafür brauchst: das Dateisystem · 5.4 Das Abbild · 5.5 Die Prüfsumme · 5.6 Prüfen: erst von Auge, dann mit dem Werkzeug · 5.7 Was die Prüfsumme beweist und was nicht
- Linux, Kapitel 1, Abschnitt 6 „Wie ein PC startet“: 6.1 Die Firmware · 6.2 Bootreihenfolge und Bootmenü · 6.3 Der Bootloader · 6.4 Secure Boot · 6.5 Die Geräteverschlüsselung von Windows
- Linux, Kapitel 1, Abschnitt 7 „Eine virtuelle Maschine mit VirtualBox“: 7.1 VirtualBox einrichten · 7.2 Die Hardware-Virtualisierung einschalten · 7.3 Eine VM anlegen · 7.4 Ubuntu in der VM installieren · 7.5 Der erste Snapshot · 7.6 Das Terminal in der VM
- Linux, Kapitel 1, Abschnitt 8 „Das Live-System“: 8.1 Was du dafür brauchst: das Einhängen · 8.2 Das Live-System · 8.3 Das komprimierte Abbild: squashfs · 8.4 Ein Dateisystem im Arbeitsspeicher: tmpfs · 8.5 Zwei Schichten übereinander: das Overlay · 8.6 Was beim Ausschalten geschieht · 8.7 Persistenz
- Linux, Kapitel 1, Abschnitt 9 „Der Live-USB-Stick: vorbereiten, schreiben, starten“: 9.1 Die Risiken im Überblick · 9.2 Den richtigen Datenträger erkennen · 9.3 Der Schnellstart von Windows · 9.4 Das Abbild laden und prüfen · 9.5 Das Schreibwerkzeug · 9.6 Vom Stick starten: „Ubuntu ausprobieren“ · 9.7 Im Live-System: Terminal und Datenträger · 9.8 Beenden und den Stick zurückverwandeln

### Linux, Kapitel 2: Die Shell: erste Befehle (`Kap2_Shell`, Modul linux)

- Linux, Kapitel 2, Abschnitt 1 „Terminal und Shell“: 1.1 Was du dafür brauchst: das Terminal aus Kapitel 1 · 1.2 Der Terminalemulator · 1.3 Die Shell · 1.4 Die Eingabeaufforderung · 1.5 Die Sitzung
- Linux, Kapitel 2, Abschnitt 2 „Der Aufbau einer Befehlszeile“: 2.1 Die Befehlszeile · 2.2 Der Befehl · 2.3 Das Argument · 2.4 Die Option · 2.5 Die lange Option · 2.6 Die Option mit Wert · 2.7 Das Ende der Optionen
- Linux, Kapitel 2, Abschnitt 3 „Arten von Befehlen“: 3.1 Die Programmdatei · 3.2 Der Suchpfad · 3.3 Der eingebaute Befehl · 3.4 Der Alias · 3.5 Was hinter einem Namen steckt: type und which
- Linux, Kapitel 2, Abschnitt 4 „Hilfe finden“: 4.1 Die Kurzhilfe · 4.2 Die Hilfe für eingebaute Befehle · 4.3 Die Handbuchseite · 4.4 Der Seitenanzeiger · 4.5 Die Abschnitte des Handbuchs · 4.6 Die Suche im Handbuch · 4.7 Welche Hilfe wofür
- Linux, Kapitel 2, Abschnitt 5 „Schneller arbeiten: Vervollständigung, Verlauf, Tastenkürzel“: 5.1 Die Vervollständigung · 5.2 Der Verlauf · 5.3 Die Rückwärtssuche · 5.4 Der Abbruch mit Strg+C · 5.5 Das Ende der Eingabe mit Strg+D · 5.6 Tastenkürzel für die Befehlszeile
- Linux, Kapitel 2, Abschnitt 6 „Das System erkunden“: 6.1 Kernel und Distribution · 6.2 Der Benutzer: whoami und id · 6.3 Datum und Laufzeit: date und uptime · 6.4 Der Arbeitsspeicher: free · 6.5 Der Platz auf den Datenträgern: df
- Linux, Kapitel 2, Abschnitt 7 „Zwei Fassungen der Grundbefehle: GNU und uutils“: 7.1 Die Grundbefehle: coreutils · 7.2 uutils: die Neufassung in Rust · 7.3 Die GNU-Fassung aufrufen · 7.4 Was sich unterscheidet

### Linux, Kapitel 3: Dateien, Verzeichnisse und Pfade (`Kap3_Dateien`, Modul linux)

- Linux, Kapitel 3, Abschnitt 1 „Dateien, Verzeichnisse und der Verzeichnisbaum“: 1.1 Was du dafür brauchst: Shell, Befehl und aktueller Ordner · 1.2 Die Datei · 1.3 Das Verzeichnis · 1.4 Der Verzeichnisbaum und die Wurzel
- Linux, Kapitel 3, Abschnitt 2 „Das Arbeitsverzeichnis und Pfade“: 2.1 Das Arbeitsverzeichnis · 2.2 Der Pfad · 2.3 Der absolute Pfad · 2.4 Der relative Pfad · 2.5 Die Sondernamen . und .. · 2.6 Das Heimatverzeichnis und die Tilde · 2.7 Das Verzeichnis wechseln: cd
- Linux, Kapitel 3, Abschnitt 3 „Den Inhalt eines Verzeichnisses anzeigen“: 3.1 Der Befehl ls · 3.2 Die versteckte Datei · 3.3 Die Art eines Eintrags: ls -F · 3.4 Die lange Form: ls -l · 3.5 Lesbare Größen: ls -h · 3.6 Sortieren und weitere Optionen · 3.7 Dateinamen
- Linux, Kapitel 3, Abschnitt 4 „Dateien ansehen“: 4.1 Was du dafür brauchst: die Textdatei · 4.2 Den ganzen Inhalt zeigen: cat · 4.3 Seitenweise lesen: less · 4.4 Anfang und Ende: head und tail · 4.5 Zählen: wc · 4.6 Den Dateityp bestimmen: file
- Linux, Kapitel 3, Abschnitt 5 „Dateien und Verzeichnisse anlegen“: 5.1 Ein Verzeichnis anlegen: mkdir · 5.2 Eine leere Datei anlegen: touch · 5.3 Der Texteditor nano · 5.4 Der Baum auf einen Blick: tree
- Linux, Kapitel 3, Abschnitt 6 „Kopieren, verschieben, löschen“: 6.1 Kopieren: cp · 6.2 Verzeichnisse kopieren: cp -r · 6.3 Verschieben und umbenennen: mv · 6.4 Löschen: rm · 6.5 Verzeichnisse löschen: rmdir und rm -r · 6.6 Muster für Dateinamen
- Linux, Kapitel 3, Abschnitt 7 „Die Verzeichnisstruktur von Linux“: 7.1 Der Standard für die Verzeichnisstruktur · 7.2 Programme und Bibliotheken: /usr · 7.3 Einstellungen: /etc · 7.4 Die Benutzer: /home und /root · 7.5 Veränderliche Daten: /var und die Protokolle · 7.6 Vorübergehende Dateien: /tmp · 7.7 Geräte als Dateien: /dev · 7.8 Der Kernel als Dateisystem: /proc und /sys
- Linux, Kapitel 3, Abschnitt 8 „Inode und Links“: 8.1 Die Inode · 8.2 Das Verzeichnis als Tabelle · 8.3 Der harte Link · 8.4 Löschen heißt einen Namen entfernen · 8.5 Der symbolische Link · 8.6 Ein symbolischer Link im System: /bin · 8.7 Harte und symbolische Links im Vergleich
- Linux, Kapitel 3, Abschnitt 9 „Datenträger und Einhängen“: 9.1 Was du dafür brauchst: Datenträger, Dateisystem und Einhängen · 9.2 Die Datenträger anzeigen: lsblk · 9.3 Was wo eingehängt ist: findmnt · 9.4 Wie voll ein Dateisystem ist: df mit Pfaden · 9.5 Das Windows-Laufwerk unter WSL 2: /mnt/c
- Linux, Kapitel 3, Abschnitt 10 „Dateien finden und Platz messen“: 10.1 Suchen mit find · 10.2 Nach Namen suchen: -name · 10.3 Nach Art suchen: -type · 10.4 Nach Größe suchen: -size · 10.5 Nach Alter suchen: -mtime, -mmin und -newer · 10.6 Tests verknüpfen und Treffer bearbeiten · 10.7 Den Platzbedarf messen: du

### Linux, Kapitel 4: Ströme, Umleitung, Pipes und Exit-Status (`Kap4_Stroeme`, Modul linux)

- Linux, Kapitel 4, Abschnitt 1 „Prozesse und ihre drei Ströme“: 1.1 Was du dafür brauchst: Kernel, Shell und Dateien · 1.2 Der Prozess · 1.3 Der Strom · 1.4 Die Standardeingabe · 1.5 Die Standardausgabe · 1.6 Die Standardfehlerausgabe · 1.7 Der Dateideskriptor
- Linux, Kapitel 4, Abschnitt 2 „Ausgaben umleiten“: 2.1 Die Umleitung der Ausgabe: > · 2.2 Das Anhängen: >> · 2.3 Die Umleitung der Fehlerausgabe: 2> · 2.4 Die Datei, die alles schluckt: /dev/null · 2.5 Einen Deskriptor kopieren: 2>&1 und &> · 2.6 Die Reihenfolge der Umleitungen · 2.7 Die Kürzungsfalle
- Linux, Kapitel 4, Abschnitt 3 „Eingaben umleiten“: 3.1 Die Umleitung der Eingabe: < · 3.2 Das Here-Document · 3.3 Der Here-String
- Linux, Kapitel 4, Abschnitt 4 „Pipes und Filter“: 4.1 Die Pipe · 4.2 Der Filter · 4.3 Die Pipeline · 4.4 Der Abzweig: tee · 4.5 Die Unix-Philosophie
- Linux, Kapitel 4, Abschnitt 5 „Der Exit-Status“: 5.1 Der Exit-Status · 5.2 Was die Zahlen ungleich null bedeuten · 5.3 Die Zahlen der Shell: 126, 127 und 128 + n
- Linux, Kapitel 4, Abschnitt 6 „Befehle verketten“: 6.1 Hintereinander: das Semikolon · 6.2 Nur bei Erfolg: && · 6.3 Nur bei Misserfolg: || · 6.4 && und || in einer Zeile · 6.5 Der Exit-Status einer Pipeline
- Linux, Kapitel 4, Abschnitt 7 „Aus einer Ausgabe Argumente machen“: 7.1 Strom oder Argument · 7.2 Der Befehl xargs · 7.3 Portionen: xargs -n und die Grenze der Argumentliste · 7.4 Namen mit Leerzeichen: das Nullbyte als Trenner · 7.5 Der Weg ohne Pipe: find -exec

### Linux, Kapitel 5: Wie die Shell eine Befehlszeile liest: Expansion, Quoting, Variablen, Umgebung (`Kap5_Expansion`, Modul linux)

- Linux, Kapitel 5, Abschnitt 1 „Expansion: Muster, Klammern und Tilde“: 1.1 Was du dafür brauchst: Wörter, Muster und Prozesse · 1.2 Die Expansion · 1.3 Die Pfadnamen-Erweiterung · 1.4 Versteckte Dateien und Muster · 1.5 Ein Muster ohne Treffer · 1.6 Die Klammererweiterung · 1.7 Die Tilde-Erweiterung
- Linux, Kapitel 5, Abschnitt 2 „Variablen, Befehlsersetzung und Arithmetik“: 2.1 Die Shell-Variable · 2.2 Die Parametererweiterung: `$NAME` und `${NAME}` · 2.3 Die Befehlsersetzung · 2.4 Die Arithmetik
- Linux, Kapitel 5, Abschnitt 3 „Worttrennung und Quoting“: 3.1 Argumente einzeln anzeigen: printf · 3.2 Die Worttrennung · 3.3 Das Quoting · 3.4 Einfache Anführungszeichen · 3.5 Doppelte Anführungszeichen · 3.6 Der umgekehrte Schrägstrich · 3.7 Das Entfernen der Anführungszeichen · 3.8 Die Regel: Erweiterungen in doppelte Anführungszeichen · 3.9 Die Reihenfolge aller Schritte
- Linux, Kapitel 5, Abschnitt 4 „Umgebung und Vererbung“: 4.1 Was du dafür brauchst: Prozesse und bash -c · 4.2 Der Kindprozess · 4.3 Die Umgebung · 4.4 Die Umgebungsvariable: export · 4.5 Die Vererbung als Kopie · 4.6 Eine Variable nur für einen Befehl · 4.7 env und printenv
- Linux, Kapitel 5, Abschnitt 5 „Wie die Shell Programme findet: PATH“: 5.1 Was du dafür brauchst: Suchpfad und Befehlsarten · 5.2 Die Variable PATH · 5.3 Die Befehlssuche · 5.4 Ein Programm im Arbeitsverzeichnis: ./ · 5.5 PATH ändern
- Linux, Kapitel 5, Abschnitt 6 „Startdateien und Aliase“: 6.1 Die Startdatei · 6.2 source · 6.3 Die Anmelde-Shell · 6.4 Eine Einstellung dauerhaft machen · 6.5 Der Alias

### Linux, Kapitel 6: Textwerkzeuge und reguläre Ausdrücke (`Kap6_Textwerkzeuge`, Modul linux)

- Linux, Kapitel 6, Abschnitt 1 „Textdaten: Datensätze, Felder und Zeilenenden“: 1.1 Was du dafür brauchst: Textdatei, Filter, Pipeline und Quoting · 1.2 Datensatz und Feld · 1.3 Die CSV-Datei und ihre Kopfzeile · 1.4 Das Zeilenende unter Windows · 1.5 Zeilen ab einer Stelle: tail -n +K und head -n -K · 1.6 Einer wachsenden Datei folgen: tail -f
- Linux, Kapitel 6, Abschnitt 2 „Spalten ausschneiden und Zeichen ersetzen: cut, tr und paste“: 2.1 Spalten ausschneiden: cut · 2.2 Zeichen ersetzen und löschen: tr · 2.3 Spalten zusammenfügen: paste
- Linux, Kapitel 6, Abschnitt 3 „Sortieren und Zählen: sort und uniq“: 3.1 Wie sort vergleicht: die Zeichenordnung · 3.2 Numerisch sortieren: sort -n · 3.3 Nach einer Spalte sortieren: -t und -k · 3.4 Die Spracheinstellung · 3.5 Gleiche Nachbarzeilen: uniq · 3.6 Häufigkeiten zählen: sort, uniq -c, sort -rn
- Linux, Kapitel 6, Abschnitt 4 „Nummerieren, Zahlenfolgen und Unterschiede: nl, seq und diff“: 4.1 Zeilen nummerieren: nl · 4.2 Zahlenfolgen erzeugen: seq · 4.3 Unterschiede finden: diff
- Linux, Kapitel 6, Abschnitt 5 „Suchen mit grep“: 5.1 Zeilen mit einem Suchtext: grep · 5.2 Umkehren, zählen, nummerieren: -i, -v, -c und -n · 5.3 Nur den Treffer ausgeben: -o · 5.4 In vielen Dateien suchen: -r und -l
- Linux, Kapitel 6, Abschnitt 6 „Reguläre Ausdrücke: Zeichen, Klassen und Anker“: 6.1 Der reguläre Ausdruck · 6.2 Der Punkt: ein beliebiges Zeichen · 6.3 Sonderzeichen wörtlich nehmen: der umgekehrte Schrägstrich und grep -F · 6.4 Eine Auswahl von Zeichen: der Klammerausdruck · 6.5 Zeichenklassen: [[:digit:]] und ihre Verwandten · 6.6 Anfang und Ende der Zeile: die Anker
- Linux, Kapitel 6, Abschnitt 7 „Reguläre Ausdrücke: Wiederholungen, Gruppen und Alternativen“: 7.1 Beliebig oft: der Stern · 7.2 Die erweiterte Form: grep -E · 7.3 Wiederholungen zählen: +, ? und {n,m} · 7.4 Gruppe und Alternative · 7.5 Grundform und erweiterte Form im Vergleich · 7.6 Der längste Treffer · 7.7 Form statt Bedeutung · 7.8 Muster für Dateinamen und reguläre Ausdrücke
- Linux, Kapitel 6, Abschnitt 8 „Umformen im Strom: sed“: 8.1 Der Strom-Editor sed · 8.2 Ersetzen: der Befehl s · 8.3 Zeilen auswählen: Zeilenadressen, -n und p · 8.4 Zeilen löschen: der Befehl d · 8.5 Gruppen und Rückverweise · 8.6 Die Datei selbst ändern: sed -i
- Linux, Kapitel 6, Abschnitt 9 „Rechnen mit Spalten: awk“: 9.1 Das Programm awk: Bedingung und Aktion · 9.2 Felder: `$1`, `$0`, `NF` und `-F` · 9.3 Zeilennummer und Bedingungen: NR · 9.4 Variablen, Summen und END · 9.5 Werte nach Namen sammeln: assoziative Arrays
- Linux, Kapitel 6, Abschnitt 10 „Eine Auswertung von Anfang bis Ende“: 10.1 Welches Werkzeug wofür · 10.2 Eine Pipeline Schritt für Schritt bauen · 10.3 Wörter zählen: eine berühmte Pipeline

### Linux, Kapitel 7: Benutzer, Gruppen und Rechte (`Kap7_Rechte`, Modul linux)

- Linux, Kapitel 7, Abschnitt 1 „Benutzer und Gruppen“: 1.1 Was du dafür brauchst: Prozess, Systemaufruf und Datei · 1.2 Der Benutzer und seine Nummer · 1.3 Die Gruppe und ihre Nummer · 1.4 Die Benutzerliste: /etc/passwd · 1.5 Hauptgruppe und Zusatzgruppen · 1.6 Der Benutzer eines Prozesses · 1.7 Der Verwalter: root · 1.8 Der Passwort-Prüfwert: /etc/shadow
- Linux, Kapitel 7, Abschnitt 2 „Die Rechte einer Datei“: 2.1 Besitzer und Gruppe einer Datei · 2.2 Drei Klassen: Besitzer, Gruppe, alle anderen · 2.3 Lesen, Schreiben, Ausführen · 2.4 Die Rechte-Spalte lesen: ls -l und stat
- Linux, Kapitel 7, Abschnitt 3 „Rechte ändern: chmod“: 3.1 Was du dafür brauchst: Bits und Binärzahlen · 3.2 chmod mit Buchstaben · 3.3 Die Oktalschreibweise · 3.4 chmod mit Zahlen
- Linux, Kapitel 7, Abschnitt 4 „Rechte bei Verzeichnissen“: 4.1 Lesen: die Namen sehen · 4.2 Ausführen: hindurchgehen · 4.3 Schreiben: Einträge ändern · 4.4 Löschen ändert das Verzeichnis
- Linux, Kapitel 7, Abschnitt 5 „Wie der Kernel Rechte prüft“: 5.1 Der Weg durch den Pfad · 5.2 Die erste passende Klasse · 5.3 Geprüft wird beim Öffnen
- Linux, Kapitel 7, Abschnitt 6 „Kurzzeitig root: sudo und su“: 6.1 Der Befehl sudo · 6.2 Die Erlaubnis: sudoers und sudo -l · 6.3 Als anderer Benutzer: sudo -u · 6.4 root und die Rechte · 6.5 Das Protokoll · 6.6 Die Umleitungsfalle: sudo und > · 6.7 su und die Shell des Verwalters
- Linux, Kapitel 7, Abschnitt 7 „Benutzer und Gruppen anlegen“: 7.1 Einen Benutzer anlegen: adduser · 7.2 Einen Benutzer in eine Gruppe aufnehmen · 7.3 Eine Gruppe anlegen: addgroup · 7.4 Neue Gruppen gelten ab der nächsten Anmeldung · 7.5 Die Klassen mit zwei Benutzern
- Linux, Kapitel 7, Abschnitt 8 „Besitz und Voreinstellungen: chown, chgrp und umask“: 8.1 Den Besitzer ändern: chown · 8.2 Für den Kernel zählt die Nummer · 8.3 Die Gruppe ändern: chgrp · 8.4 Die Voreinstellung für neue Dateien: umask · 8.5 Bits wegnehmen, nicht abziehen · 8.6 Die umask einstellen
- Linux, Kapitel 7, Abschnitt 9 „Programme ausführen und besondere Rechte“: 9.1 Das Ausführungsrecht für Programme · 9.2 Reale und effektive Benutzernummer · 9.3 Das SUID-Bit · 9.4 Wozu SUID: passwd und sudo · 9.5 Kein SUID für Skripte · 9.6 Das SGID-Bit · 9.7 Das Sticky-Bit · 9.8 Die besonderen Rechte als vierte Ziffer · 9.9 Aufräumen: Benutzer und Gruppe entfernen

### Linux, Kapitel 8: Prozesse, Signale und Dienste (`Kap8_Prozesse`, Modul linux)

- Linux, Kapitel 8, Abschnitt 1 „Prozesse und ihre Verwandtschaft“: 1.1 Was du dafür brauchst: Prozess, Exit-Status und Benutzer · 1.2 Programm und Prozess, genauer · 1.3 Viele Prozesse, wenige Kerne: die Zeitteilung · 1.4 Die Prozessnummer: PID · 1.5 Der Elternprozess: PPID · 1.6 Wie ein Prozess entsteht: fork, exec und wait · 1.7 Der Prozessbaum und PID 1 · 1.8 Der Besitzer eines Prozesses
- Linux, Kapitel 8, Abschnitt 2 „Prozesse beobachten“: 2.1 Die eigenen Prozesse: ps · 2.2 Alle Prozesse: ps -ef und ps aux · 2.3 Eigene Spalten und Auswahl: ps -o · 2.4 Prozesse nach Namen finden: pgrep · 2.5 Der Zustand eines Prozesses · 2.6 Der Zombie · 2.7 Laufend beobachten: top · 2.8 Ein Blick in den Eintrag: /proc/<PID>
- Linux, Kapitel 8, Abschnitt 3 „Vordergrund, Hintergrund und Jobs“: 3.1 Der Vordergrund · 3.2 Der Hintergrund: & · 3.3 Der Job · 3.4 Anhalten mit Strg+Z · 3.5 Weiterlaufen lassen: fg und bg · 3.6 Warten: wait
- Linux, Kapitel 8, Abschnitt 4 „Signale“: 4.1 Das Signal · 4.2 Die Standardreaktion · 4.3 Signale senden: kill · 4.4 Bitten und unterbrechen: SIGTERM und SIGINT · 4.5 Das Ende ohne Rückfrage: SIGKILL · 4.6 Anhalten und fortsetzen: SIGSTOP, SIGTSTP und SIGCONT · 4.7 Was der Exit-Status verrät: 128 + n · 4.8 Wer wem Signale schicken darf
- Linux, Kapitel 8, Abschnitt 5 „Mit Signalen arbeiten“: 5.1 Signale nach Namen: pkill · 5.2 Ein Signal abfangen: trap · 5.3 Eine Zeitgrenze: timeout · 5.4 Das Signal beim Schließen: SIGHUP · 5.5 Weiterlaufen nach dem Schließen: nohup und disown
- Linux, Kapitel 8, Abschnitt 6 „Last und Priorität“: 6.1 Die Last, genauer · 6.2 Die Priorität: der Nice-Wert · 6.3 Wie viel ein Nice-Wert ausmacht · 6.4 Die Priorität ändern: renice
- Linux, Kapitel 8, Abschnitt 7 „Dienste und systemd“: 7.1 Der Dienst · 7.2 systemd: der Prozess mit der Nummer 1 · 7.3 Die Unit · 7.4 Den Zustand ansehen: systemctl status · 7.5 Die Unit-Datei · 7.6 Ein eigener Dienst: starten und stoppen · 7.7 systemd wacht: Neustart nach einem Absturz · 7.8 Beim Start mitstarten: enable · 7.9 Dienste unter eigenen Benutzern
- Linux, Kapitel 8, Abschnitt 8 „Protokolle: das Journal“: 8.1 Das Journal · 8.2 Die Meldungen einer Unit: journalctl -u · 8.3 Mitlesen: journalctl -f · 8.4 Seit dem Start: journalctl -b und `--since` · 8.5 Wer welche Meldungen lesen darf · 8.6 Aufräumen

### Linux, Kapitel 9: Software installieren: Paketverwaltung (`Kap9_Pakete`, Modul linux)

- Linux, Kapitel 9, Abschnitt 1 „Pakete und ihre Beziehungen“: 1.1 Was du dafür brauchst: Distribution, Verzeichnisse, Bibliotheken und root · 1.2 Das Paket · 1.3 Die Paketbeschreibung · 1.4 Version und Architektur · 1.5 Die Abhängigkeit · 1.6 Empfehlung und Vorschlag · 1.7 Der Konflikt · 1.8 Das virtuelle Paket
- Linux, Kapitel 9, Abschnitt 2 „Die Paketverwaltung und ihre Datenbank“: 2.1 Die Paketverwaltung · 2.2 Zwei Ebenen: dpkg und apt · 2.3 Die Liste der installierten Pakete: dpkg -l · 2.4 Die Dateien eines Pakets: dpkg -L · 2.5 Zu welchem Paket gehört eine Datei: dpkg -S · 2.6 Der Zustand eines Pakets: dpkg -s · 2.7 Wo die Paketdatenbank liegt
- Linux, Kapitel 9, Abschnitt 3 „Paketquellen und Paketlisten“: 3.1 Die Paketquelle · 3.2 Der Spiegelserver · 3.3 Ausgabe und Bereich · 3.4 Die Quellenliste · 3.5 Die Paketliste · 3.6 Die Paketlisten holen: apt update
- Linux, Kapitel 9, Abschnitt 4 „Pakete suchen und ansehen“: 4.1 Suchen: apt search · 4.2 Ansehen: apt show · 4.3 Auflisten: apt list · 4.4 Die Kandidatenversion: apt policy · 4.5 Abhängigkeiten anzeigen: apt-cache depends
- Linux, Kapitel 9, Abschnitt 5 „Ein Paket von innen“: 5.1 Eine Paketdatei herunterladen: apt download · 5.2 Der Aufbau einer Paketdatei · 5.3 Der Steuerteil: dpkg-deb -I · 5.4 Der Datenteil: dpkg-deb -c und -x
- Linux, Kapitel 9, Abschnitt 6 „Installieren, entfernen, aktualisieren“: 6.1 Die Sperre: warum Installieren root braucht · 6.2 Die Simulation · 6.3 Installieren: apt install · 6.4 Manuell und automatisch installiert · 6.5 Entfernen: remove, purge und autoremove · 6.6 Aktualisieren: upgrade und full-upgrade
- Linux, Kapitel 9, Abschnitt 7 „Warum man den Paketen trauen kann“: 7.1 Was du dafür brauchst: die Prüfsumme · 7.2 Die Prüfsumme der Paketdatei · 7.3 Die Release-Datei · 7.4 Das Schlüsselpaar · 7.5 Die digitale Signatur · 7.6 Der Schlüsselbund und Signed-By · 7.7 Der Weg eines Pakets · 7.8 Was die Prüfung nicht leistet
- Linux, Kapitel 9, Abschnitt 8 „Aktualisieren als Schutz“: 8.1 Das Sicherheitsupdate · 8.2 Das Zeitfenster nach der Veröffentlichung · 8.3 Nach dem Update: laufende Programme · 8.4 Automatische Sicherheitsupdates · 8.5 Der Pflegezeitraum
- Linux, Kapitel 9, Abschnitt 9 „Alternativen: ein Befehl, mehrere Pakete“: 9.1 Das Alternativsystem · 9.2 sudo und sudo-rs · 9.3 Die Grundbefehle: coreutils-from-uutils · 9.4 Unverzichtbare und geschützte Pakete
- Linux, Kapitel 9, Abschnitt 10 „Software von außerhalb der Paketquellen“: 10.1 Eine zusätzliche Paketquelle · 10.2 Eine einzelne Paketdatei · 10.3 Installationsskripte aus dem Netz · 10.4 Snap und Flatpak · 10.5 Aufräumen

## Informatik / Cybersecurity

### Cybersecurity, Kapitel 1: Sicherheit, Schutzziele und Spielregeln (`Kap1_Sicherheit`, Modul cyber)

- Cybersecurity, Kapitel 1, Abschnitt 1 „Was geschützt wird: Schutzgut und Schutzziele“: 1.1 Das Schutzgut · 1.2 Berechtigte und Unbefugte · 1.3 Schutzziele · 1.4 Vertraulichkeit · 1.5 Integrität · 1.6 Verfügbarkeit · 1.7 Authentizität · 1.8 Verbindlichkeit · 1.9 Schutzbedarf
- Cybersecurity, Kapitel 1, Abschnitt 2 „Von der Schwachstelle zum Schaden“: 2.1 Schwachstelle · 2.2 Bedrohung · 2.3 Angreifer · 2.4 Angriff · 2.5 Exploit · 2.6 Der Schaden
- Cybersecurity, Kapitel 1, Abschnitt 3 „Risiko, Angreifermodell und Angriffsfläche“: 3.1 Was du dafür brauchst: Häufigkeit und Erwartungswert · 3.2 Was du dafür brauchst: unabhängige Ereignisse · 3.3 Risiko · 3.4 Das Gesamtrisiko · 3.5 Sicherheit ist Ökonomie · 3.6 Angreifermodell · 3.7 Angriffsfläche
- Cybersecurity, Kapitel 1, Abschnitt 4 „Richtlinie und Mechanismus“: 4.1 Sicherheitsrichtlinie · 4.2 Sicherheitsmechanismus · 4.3 Verhindern, erkennen, wiederherstellen · 4.4 Passiver und aktiver Angriff
- Cybersecurity, Kapitel 1, Abschnitt 5 „Sicherheitsprinzipien: Rechte vergeben und prüfen“: 5.1 Sicherheitsprinzipien · 5.2 Minimale Rechte · 5.3 Aufgabentrennung · 5.4 Sichere Voreinstellung · 5.5 Lückenlose Prüfung · 5.6 Prüfen und Handeln im selben Moment
- Cybersecurity, Kapitel 1, Abschnitt 6 „Sicherheitsprinzipien: Systeme robust entwerfen“: 6.1 Mehrere Verteidigungslinien · 6.2 Einfachheit · 6.3 Eine kleine vertrauenswürdige Basis · 6.4 Kein Verlass auf ein geheimes Verfahren · 6.5 Der Mensch als Teil des Systems · 6.6 Sicherheit von Anfang an
- Cybersecurity, Kapitel 1, Abschnitt 7 „Schwachstellen benennen und bewerten“: 7.1 CVE: der Name einer Schwachstelle · 7.2 CWE: die Art des Fehlers · 7.3 CVSS: die Schwere · 7.4 Wie aus dem Vektor die Zahl wird · 7.5 Der Lebenszyklus einer Schwachstelle · 7.6 Zero-Day
- Cybersecurity, Kapitel 1, Abschnitt 8 „Computerstrafrecht: was verboten ist“: 8.1 Was du dafür brauchst: wie ein Straftatbestand gebaut ist · 8.2 Ausspähen von Daten (§ 202a StGB) · 8.3 Abfangen von Daten (§ 202b StGB) · 8.4 Vorbereiten des Ausspähens und Abfangens (§ 202c StGB) · 8.5 Datenhehlerei (§ 202d StGB) · 8.6 Datenveränderung (§ 303a StGB) · 8.7 Computersabotage (§ 303b StGB) · 8.8 Computerbetrug (§ 263a StGB)
- Cybersecurity, Kapitel 1, Abschnitt 9 „Erlaubnis, Werkzeuge und gute Absicht“: 9.1 Die Erlaubnis des Berechtigten · 9.2 Antragsdelikt heißt nicht erlaubt · 9.3 Werkzeuge besitzen: der Beschluss von 2009 · 9.4 Gute Absicht schützt nicht
- Cybersecurity, Kapitel 1, Abschnitt 10 „Offenlegung und Ethik“: 10.1 Was du dafür brauchst: der Aufbau einer Webadresse · 10.2 Koordinierte Offenlegung · 10.3 Meldeprogramme und Bug-Bounty · 10.4 security.txt · 10.5 Was man bei einem Zufallsfund tut · 10.6 Hackerethik · 10.7 Die Spielregeln dieser Reihe

### Cybersecurity, Kapitel 2: Schutzgrenzen in Hardware und Betriebssystem (`Kap2_Schutzgrenzen`, Modul cyber)

- Cybersecurity, Kapitel 2, Abschnitt 1 „Schutzgrenzen und der Referenzmonitor“: 1.1 Was du dafür brauchst: Kernel, Systemaufruf und Prozess · 1.2 Was du dafür brauchst: lückenlose Prüfung und vertrauenswürdige Basis · 1.3 Die Schutzgrenze · 1.4 Der Referenzmonitor · 1.5 Der Kernel als Referenzmonitor
- Cybersecurity, Kapitel 2, Abschnitt 2 „Code und Daten im selben Speicher“: 2.1 Was du dafür brauchst: Byte, Hexadezimalzahl und Adresse · 2.2 Der Befehlszeiger · 2.3 Das Von-Neumann-Prinzip · 2.4 Wenn Daten zu Befehlen werden
- Cybersecurity, Kapitel 2, Abschnitt 3 „Privilegstufen und Schutzringe“: 3.1 Was du dafür brauchst: Signal und Exit-Status · 3.2 Die Privilegstufe · 3.3 Die Schutzringe · 3.4 Privilegierte Befehle · 3.5 Die Ausnahme und die Schutzverletzung
- Cybersecurity, Kapitel 2, Abschnitt 4 „Der Eintritt in den Kernel“: 4.1 Die Einsprungstelle und die Einsprungtabelle · 4.2 Drei Wege in den Kernel · 4.3 Die Rückkehr in den Benutzermodus · 4.4 Die Prüfung der Argumente · 4.5 Der Systemaufruf als einzige Tür
- Cybersecurity, Kapitel 2, Abschnitt 5 „Die Zeitgeber-Unterbrechung“: 5.1 Was du dafür brauchst: Zeitteilung und Planer · 5.2 Der Zeitgeber · 5.3 Die Zeitgeber-Unterbrechung · 5.4 Kooperativ oder erzwungen · 5.5 Warum kein Programm den Wecker abstellen kann · 5.6 Zeitgeber-Unterbrechungen zählen
- Cybersecurity, Kapitel 2, Abschnitt 6 „Der virtuelle Adressraum“: 6.1 Die virtuelle Adresse · 6.2 Seite und Seitenrahmen · 6.3 Die Seitentabelle · 6.4 Die MMU · 6.5 Das Wurzelregister · 6.6 Der Seitenfehler · 6.7 Gemeinsame Seiten · 6.8 Die mehrstufige Seitentabelle
- Cybersecurity, Kapitel 2, Abschnitt 7 „Seitenrechte: Kernel, Code und Daten trennen“: 7.1 Die Rechte eines Seitentabelleneintrags · 7.2 Der Kernel in jedem Adressraum · 7.3 Das NX-Bit · 7.4 Die Regel W^X · 7.5 SMEP und SMAP · 7.6 Seitenrechte beobachten: /proc/self/maps
- Cybersecurity, Kapitel 2, Abschnitt 8 „Die Startkette als Schutzgrenze“: 8.1 Was du dafür brauchst: Firmware, Bootloader und Secure Boot · 8.2 Die Startkette als Schutzgrenze und das Bootkit · 8.3 Der Vertrauensanker · 8.4 Die Schlüssel von Secure Boot · 8.5 Wer die Schlüssel ändern darf · 8.6 Der Widerruf und seine Grenzen
- Cybersecurity, Kapitel 2, Abschnitt 9 „Measured Boot: messen statt blockieren“: 9.1 Was du dafür brauchst: die Prüfsumme · 9.2 Messen statt blockieren · 9.3 Das TPM · 9.4 Das Plattform-Konfigurationsregister · 9.5 Das Erweitern · 9.6 Das Ereignisprotokoll · 9.7 Was Measured Boot nicht tut
- Cybersecurity, Kapitel 2, Abschnitt 10 „Das TPM: versiegeln, nachweisen und die Grenzen“: 10.1 Was du dafür brauchst: die Geräteverschlüsselung · 10.2 Die Bauformen des TPM · 10.3 Schlüssel im TPM · 10.4 Das Versiegeln · 10.5 BitLocker mit PCR 7 und PCR 11 · 10.6 Die Attestierung · 10.7 Die Grenzen des TPM · 10.8 Zusammenschau: die Schutzgrenzen im Überblick

## Informatik / Machine Learning / Mathematische Grundlagen

### Grundlagen, Kapitel 1: Vektoren und Matrizen (`Kap1_Vektoren`, Modul ml)

- Grundlagen, Kapitel 1, Abschnitt 1 „Vektoren: Daten als Zahlenlisten“: 1.1 Was du dafür brauchst: Summenzeichen und Indizes · 1.2 Beispiele und Merkmale · 1.3 Vektoren · 1.4 Addition und Vielfaches · 1.5 Linearkombinationen · 1.6 Die Einheitsvektoren
- Grundlagen, Kapitel 1, Abschnitt 2 „Das Skalarprodukt“: 2.1 Das Skalarprodukt zweier Vektoren · 2.2 Gewichte und gewichtete Summen · 2.3 Summe und Mittelwert als Skalarprodukt · 2.4 Das Skalarprodukt als Mustervergleich
- Grundlagen, Kapitel 1, Abschnitt 3 „Normen: die Größe eines Vektors“: 3.1 Die euklidische Norm · 3.2 Die Betragssummennorm · 3.3 Die Maximumnorm · 3.4 Was eine Norm ausmacht · 3.5 Der Fehlervektor und seine Größe · 3.6 Der quadratische Mittelwert
- Grundlagen, Kapitel 1, Abschnitt 4 „Abstände und Einheiten“: 4.1 Der Abstand zweier Datenpunkte · 4.2 Abstände hängen von den Einheiten ab · 4.3 Abweichungen vom Mittelwert · 4.4 Die Standardabweichung · 4.5 Standardisieren
- Grundlagen, Kapitel 1, Abschnitt 5 „Winkel und Ähnlichkeit“: 5.1 Die Cauchy-Schwarz-Ungleichung · 5.2 Der Winkel zwischen zwei Vektoren · 5.3 Orthogonale Vektoren · 5.4 Die Kosinus-Ähnlichkeit · 5.5 Das Skalarprodukt als Schattenlänge
- Grundlagen, Kapitel 1, Abschnitt 6 „Matrizen und die Datenmatrix“: 6.1 Matrizen · 6.2 Quadratische Matrizen und Diagonalmatrizen · 6.3 Die Datenmatrix
- Grundlagen, Kapitel 1, Abschnitt 7 „Das Matrix-Vektor-Produkt“: 7.1 Matrix mal Vektor · 7.2 Die Zeilensicht: viele Skalarprodukte · 7.3 Die Spaltensicht: eine Linearkombination der Spalten · 7.4 Der Spaltenraum
- Grundlagen, Kapitel 1, Abschnitt 8 „Lineare Abbildungen“: 8.1 Lineare Abbildungen · 8.2 Jede lineare Abbildung ist eine Matrix · 8.3 Lineare Abbildungen der Ebene · 8.4 Lineare Funktionen mit einem Ausgang · 8.5 Affine Abbildungen
- Grundlagen, Kapitel 1, Abschnitt 9 „Das Matrixprodukt“: 9.1 Das Matrixprodukt · 9.2 Viele Vektoren auf einmal · 9.3 Rechenregeln: Die Reihenfolge zählt · 9.4 Zwei lineare Stufen sind eine · 9.5 Das äußere Produkt
- Grundlagen, Kapitel 1, Abschnitt 10 „Transponierte, Symmetrie und Gram-Matrix“: 10.1 Die Transponierte · 10.2 Symmetrische Matrizen · 10.3 Die Gram-Matrix der Beispiele · 10.4 Die Gram-Matrix der Merkmale
- Grundlagen, Kapitel 1, Abschnitt 11 „Einheitsmatrix und Inverse“: 11.1 Die Einheitsmatrix · 11.2 Die inverse Matrix · 11.3 Die Inverse einer $2\times2$-Matrix · 11.4 Rechenregeln für Inverse · 11.5 Wann es keine Inverse gibt
- Grundlagen, Kapitel 1, Abschnitt 12 „Lineare Gleichungssysteme“: 12.1 Gleichungssysteme in Matrixform · 12.2 Zeilenbild und Spaltenbild · 12.3 Das Gauß-Verfahren · 12.4 Keine, eine oder unendlich viele Lösungen · 12.5 Mehr Gleichungen als Unbekannte
- Grundlagen, Kapitel 1, Abschnitt 13 „Unabhängigkeit, Basis und Rang“: 13.1 Der Spann · 13.2 Lineare Unabhängigkeit · 13.3 Basis und Dimension · 13.4 Der Rang einer Matrix · 13.5 Der Kern und der Rangsatz · 13.6 Abhängige Merkmale
- Grundlagen, Kapitel 1, Abschnitt 14 „Die Determinante“: 14.1 Die Determinante einer $2\times2$-Matrix · 14.2 Das Vorzeichen der Determinante · 14.3 Der Flächenfaktor gilt für jede Figur · 14.4 Determinanten größerer Matrizen · 14.5 Rechenregeln für Determinanten · 14.6 Determinante und Invertierbarkeit
- Grundlagen, Kapitel 1, Abschnitt 15 „Elementweise Rechnen und Tensoren“: 15.1 Das Hadamard-Produkt · 15.2 Elementweise Funktionen · 15.3 Einen Vektor zu jeder Zeile addieren · 15.4 Tensoren · 15.5 Bilder als Tensoren

### Grundlagen, Kapitel 2: Projektion, Eigenwerte und Zerlegungen (`Kap2_Eigenwerte`, Modul ml)

- Grundlagen, Kapitel 2, Abschnitt 1 „Orthonormalbasen und orthogonale Matrizen“: 1.1 Orthonormale Vektoren · 1.2 Orthonormalbasen · 1.3 Koordinaten in einer Orthonormalbasis · 1.4 Orthogonale Matrizen · 1.5 Längen und Winkel bleiben erhalten · 1.6 Matrizen mit orthonormalen Spalten
- Grundlagen, Kapitel 2, Abschnitt 2 „Projektion auf eine Gerade“: 2.1 Der Fußpunkt des Lots · 2.2 Der Fußpunkt ist der nächste Punkt · 2.3 Die Projektionsmatrix · 2.4 Projektionen im Allgemeinen
- Grundlagen, Kapitel 2, Abschnitt 3 „Die beste Näherungslösung“: 3.1 Rückblick: Mehr Gleichungen als Unbekannte · 3.2 Die beste Näherungslösung · 3.3 Die Normalgleichungen · 3.4 Warum die Normalgleichungen die beste Lösung liefern · 3.5 Wann die beste Näherungslösung eindeutig ist · 3.6 Eine Gerade durch drei Punkte · 3.7 Die Wohnungen: was Kapitel 1 offen ließ
- Grundlagen, Kapitel 2, Abschnitt 4 „Projektion auf einen Unterraum“: 4.1 Unterräume · 4.2 Die Projektionsmatrix eines Spaltenraums · 4.3 Orthonormale Spalten · 4.4 Das orthogonale Komplement · 4.5 Das Gram-Schmidt-Verfahren · 4.6 Die QR-Zerlegung · 4.7 Die beste Näherungslösung mit QR
- Grundlagen, Kapitel 2, Abschnitt 5 „Quadratische Formen“: 5.1 Quadratische Formen · 5.2 Nur der symmetrische Anteil zählt · 5.3 Schüssel, Rinne und Sattel · 5.4 Quadratisch ergänzen
- Grundlagen, Kapitel 2, Abschnitt 6 „Eigenwerte und Eigenvektoren“: 6.1 Was du dafür brauchst: komplexe Zahlen · 6.2 Eigenvektoren und Eigenwerte · 6.3 Das charakteristische Polynom · 6.4 Eigenvektoren berechnen · 6.5 Spur und Determinante · 6.6 Komplexe Eigenwerte · 6.7 Mehrfache Eigenwerte · 6.8 Wie viele Eigenvektoren es gibt · 6.9 Rechenregeln für Eigenwerte
- Grundlagen, Kapitel 2, Abschnitt 7 „Diagonalisierung und Spektralsatz“: 7.1 Basiswechsel · 7.2 Diagonalisierung · 7.3 Entkoppeln: Potenzen und Folgen · 7.4 Symmetrische Matrizen haben reelle Eigenwerte · 7.5 Eigenvektoren symmetrischer Matrizen stehen senkrecht · 7.6 Der Spektralsatz · 7.7 Hauptachsen
- Grundlagen, Kapitel 2, Abschnitt 8 „Positiv definite Matrizen“: 8.1 Positiv definit und positiv semidefinit · 8.2 Der Eigenwerttest · 8.3 Tests ohne Eigenwerte · 8.4 Gram-Matrizen sind positiv semidefinit · 8.5 Größter und kleinster Wert auf dem Einheitskreis · 8.6 Die Cholesky-Zerlegung
- Grundlagen, Kapitel 2, Abschnitt 9 „Die Singulärwertzerlegung“: 9.1 Senkrechte Richtungen, die senkrecht bleiben · 9.2 Singulärwerte · 9.3 Singulärvektoren · 9.4 Die Zerlegung · 9.5 Drehung, Streckung, Drehung · 9.6 Bausteine vom Rang 1 und die Räume einer Matrix · 9.7 Symmetrische Matrizen · 9.8 Die Spektralnorm
- Grundlagen, Kapitel 2, Abschnitt 10 „Näherung durch Matrizen von kleinem Rang“: 10.1 Die Frobeniusnorm · 10.2 Die abgeschnittene Zerlegung · 10.3 Die beste Näherung · 10.4 Ein Bild mit wenigen Zahlen
- Grundlagen, Kapitel 2, Abschnitt 11 „Die Pseudoinverse“: 11.1 Linksinverse · 11.2 Rechtsinverse · 11.3 Die Pseudoinverse · 11.4 Die kürzeste beste Näherungslösung
- Grundlagen, Kapitel 2, Abschnitt 12 „Die Konditionszahl“: 12.1 Ein empfindliches Gleichungssystem · 12.2 Die Konditionszahl · 12.3 Konditionszahl und Determinante · 12.4 Normalgleichungen quadrieren die Konditionszahl

### Grundlagen, Kapitel 3: Ableitung, Gradient und Kettenregel (`Kap3_Ableitung`, Modul ml)

- Grundlagen, Kapitel 3, Abschnitt 1 „Die Ableitung“: 1.1 Änderungsrate und Differenzenquotient · 1.2 Die Ableitung · 1.3 Die lineare Näherung · 1.4 Ableitungsregeln · 1.5 Die zweite Ableitung und die quadratische Näherung
- Grundlagen, Kapitel 3, Abschnitt 2 „Die Kettenregel“: 2.1 Verkettung · 2.2 Die Kettenregel · 2.3 Ketten aus vielen Gliedern · 2.4 Die logistische Funktion
- Grundlagen, Kapitel 3, Abschnitt 3 „Partielle Ableitungen und der Gradient“: 3.1 Funktionen mehrerer Variablen · 3.2 Partielle Ableitungen · 3.3 Der Gradient · 3.4 Die lineare Näherung im Raum · 3.5 Differenzierbarkeit
- Grundlagen, Kapitel 3, Abschnitt 4 „Richtungsableitung und steilster Anstieg“: 4.1 Die Richtungsableitung · 4.2 Die Richtung des steilsten Anstiegs · 4.3 Der Gradient steht senkrecht auf den Höhenlinien · 4.4 Steilster Abstieg und der tiefste Punkt
- Grundlagen, Kapitel 3, Abschnitt 5 „Die Jacobi-Matrix“: 5.1 Funktionen mit mehreren Ausgängen · 5.2 Die Jacobi-Matrix · 5.3 Die lineare Näherung mit der Jacobi-Matrix · 5.4 Zwei wichtige Jacobi-Matrizen
- Grundlagen, Kapitel 3, Abschnitt 6 „Die Kettenregel für mehrere Variablen“: 6.1 Die Kettenregel als Matrixprodukt · 6.2 Summe über alle Wege · 6.3 Der Gradient einer Verkettung · 6.4 Ableitung entlang einer Kurve
- Grundlagen, Kapitel 3, Abschnitt 7 „Ableiten nach Vektoren und Matrizen“: 7.1 Die Layout-Konvention · 7.2 Lineare Funktionen · 7.3 Quadratische Formen · 7.4 Die Quadratsumme eines Residuums · 7.5 Ableiten nach einer Matrix · 7.6 Rückwärts durch ein Matrixprodukt
- Grundlagen, Kapitel 3, Abschnitt 8 „Die Hesse-Matrix und die quadratische Näherung“: 8.1 Zweite partielle Ableitungen · 8.2 Die Hesse-Matrix · 8.3 Der Satz von Schwarz · 8.4 Die quadratische Näherung · 8.5 Die Krümmung in einer Richtung
- Grundlagen, Kapitel 3, Abschnitt 9 „Rechengraphen“: 9.1 Zwischenergebnisse · 9.2 Der Rechengraph · 9.3 Die Vorwärtsrechnung · 9.4 Lokale Ableitungen
- Grundlagen, Kapitel 3, Abschnitt 10 „Automatische Differentiation“: 10.1 Was automatische Differentiation ist · 10.2 Der Vorwärtsmodus · 10.3 Der Rückwärtsmodus · 10.4 Muster im Rückwärtsfluss · 10.5 Der Aufwand · 10.6 Klammerung: Vektor mal Jacobi-Matrix
- Grundlagen, Kapitel 3, Abschnitt 11 „Numerische Ableitung und Gradientenprüfung“: 11.1 Die Vorwärtsdifferenz · 11.2 Die zentrale Differenz · 11.3 Was du dafür brauchst: Gleitkommazahlen · 11.4 Die Fehlerkurve · 11.5 Die Gradientenprüfung · 11.6 Knicke und andere Fallstricke

### Grundlagen, Kapitel 4: Wahrscheinlichkeit (`Kap4_Wahrscheinlichkeit`, Modul ml)

- Grundlagen, Kapitel 4, Abschnitt 1 „Zufall und Ereignisse“: 1.1 Was du dafür brauchst: Mengen · 1.2 Zufallsexperiment und Ergebnisraum · 1.3 Ereignisse
- Grundlagen, Kapitel 4, Abschnitt 2 „Wahrscheinlichkeit“: 2.1 Die relative Häufigkeit · 2.2 Die Axiome der Wahrscheinlichkeit · 2.3 Rechenregeln · 2.4 Gleich wahrscheinliche Ergebnisse
- Grundlagen, Kapitel 4, Abschnitt 3 „Bedingte Wahrscheinlichkeit“: 3.1 Wahrscheinlichkeiten aus einer Zähltabelle · 3.2 Bedingte Wahrscheinlichkeit · 3.3 Die Produktregel · 3.4 Die totale Wahrscheinlichkeit
- Grundlagen, Kapitel 4, Abschnitt 4 „Der Satz von Bayes“: 4.1 Die Bedingung umdrehen · 4.2 Natürliche Häufigkeiten · 4.3 Die Basisrate
- Grundlagen, Kapitel 4, Abschnitt 5 „Unabhängigkeit“: 5.1 Unabhängige Ereignisse · 5.2 Unabhängig ist nicht unvereinbar · 5.3 Mehrere unabhängige Ereignisse · 5.4 Bedingte Unabhängigkeit
- Grundlagen, Kapitel 4, Abschnitt 6 „Zufallsvariablen und Verteilungen“: 6.1 Zufallsvariablen · 6.2 Diskrete Verteilungen · 6.3 Was du dafür brauchst: Integrale · 6.4 Dichten · 6.5 Die Verteilungsfunktion
- Grundlagen, Kapitel 4, Abschnitt 7 „Erwartungswert und Varianz“: 7.1 Der Erwartungswert · 7.2 Der Erwartungswert einer Funktion · 7.3 Die Linearität des Erwartungswerts · 7.4 Varianz und Standardabweichung · 7.5 Die Verschiebungsformel · 7.6 Umrechnen und Standardisieren · 7.7 Mittelwert der Daten und Erwartungswert
- Grundlagen, Kapitel 4, Abschnitt 8 „Wichtige Verteilungen“: 8.1 Die Bernoulli-Verteilung · 8.2 Die kategorische Verteilung · 8.3 Die Binomialverteilung · 8.4 Die Gleichverteilung · 8.5 Die Normalverteilung · 8.6 Standardisieren und die Verteilungsfunktion $\Phi$ · 8.7 Rauschen als Zufallsvariable
- Grundlagen, Kapitel 4, Abschnitt 9 „Mehrere Zufallsvariablen“: 9.1 Was du dafür brauchst: Doppelintegrale · 9.2 Die gemeinsame Verteilung · 9.3 Randverteilungen · 9.4 Bedingte Verteilungen · 9.5 Unabhängige Zufallsvariablen · 9.6 Unabhängig und identisch verteilt
- Grundlagen, Kapitel 4, Abschnitt 10 „Kovarianz und Korrelation“: 10.1 Die Kovarianz · 10.2 Die Varianz einer Summe · 10.3 Der Korrelationskoeffizient · 10.4 Die Kovarianz als Skalarprodukt · 10.5 Unkorreliert heißt nicht unabhängig · 10.6 Kovarianz und Korrelation eines Datensatzes
- Grundlagen, Kapitel 4, Abschnitt 11 „Zufallsvektoren und die Kovarianzmatrix“: 11.1 Zufallsvektoren · 11.2 Die Kovarianzmatrix · 11.3 Die Kovarianzmatrix eines Datensatzes · 11.4 Lineare Abbildungen von Zufallsvektoren · 11.5 Die Streuung in einer Richtung · 11.6 Kovarianzmatrizen sind positiv semidefinit
- Grundlagen, Kapitel 4, Abschnitt 12 „Die mehrdimensionale Normalverteilung“: 12.1 Die Dichte · 12.2 Höhenlinien und der Mahalanobis-Abstand · 12.3 Im Eigensystem zerfällt die Verteilung · 12.4 Lineare Abbildungen und das Erzeugen normalverteilter Vektoren · 12.5 Bedingte Verteilungen · 12.6 Unkorreliert und unabhängig
- Grundlagen, Kapitel 4, Abschnitt 13 „Mittelwerte vieler Zufallsvariablen“: 13.1 Der Mittelwert unabhängiger Zufallsvariablen · 13.2 Die Tschebyschow-Ungleichung · 13.3 Das Gesetz der großen Zahlen · 13.4 Der zentrale Grenzwertsatz

### Grundlagen, Kapitel 5: Statistik und Information (`Kap5_Statistik`, Modul ml)

- Grundlagen, Kapitel 5, Abschnitt 1 „Schätzen aus einer Stichprobe“: 1.1 Wahrscheinlichkeitsrechnung und Statistik · 1.2 Rückblick: Die Stichprobe · 1.3 Schätzer · 1.4 Die Stichprobenverteilung
- Grundlagen, Kapitel 5, Abschnitt 2 „Wie gut ist ein Schätzer?“: 2.1 Verzerrung und Erwartungstreue · 2.2 Varianz und Standardfehler eines Schätzers · 2.3 Der mittlere quadratische Fehler · 2.4 Konsistenz
- Grundlagen, Kapitel 5, Abschnitt 3 „Die Varianz schätzen“: 3.1 Teilen durch $N$ unterschätzt die Varianz · 3.2 Die Bessel-Korrektur · 3.3 Erwartungstreu heißt nicht genauer
- Grundlagen, Kapitel 5, Abschnitt 4 „Die Likelihood“: 4.1 Was du dafür brauchst: Logarithmen · 4.2 Die Likelihood · 4.3 Die Likelihood einer Stichprobe · 4.4 Die Log-Likelihood
- Grundlagen, Kapitel 5, Abschnitt 5 „Die Maximum-Likelihood-Schätzung“: 5.1 Was du dafür brauchst: Der höchste Punkt einer Kurve · 5.2 Der Maximum-Likelihood-Schätzer · 5.3 Die Normalverteilung: der Mittelwert · 5.4 Die Normalverteilung: die Varianz · 5.5 Umrechnen eines Maximum-Likelihood-Schätzers
- Grundlagen, Kapitel 5, Abschnitt 6 „Prior und Posterior“: 6.1 Der Satz von Bayes für Parameter · 6.2 Die Prior-Verteilung · 6.3 Was du dafür brauchst: Ein Integral über Potenzen · 6.4 Die Beta-Verteilung · 6.5 Die Posterior-Verteilung · 6.6 Konjugierte Prior-Verteilungen · 6.7 Der Posterior-Mittelwert und die Laplace-Regel
- Grundlagen, Kapitel 5, Abschnitt 7 „Die Maximum-a-posteriori-Schätzung“: 7.1 Der MAP-Schätzer · 7.2 Der Prior als Strafterm · 7.3 Ein Gauß-Prior für einen Mittelwert · 7.4 Drei Schätzer im Vergleich
- Grundlagen, Kapitel 5, Abschnitt 8 „Informationsgehalt und Entropie“: 8.1 Der Informationsgehalt · 8.2 Die Entropie · 8.3 Entropie und Codelänge · 8.4 Die binäre Entropie
- Grundlagen, Kapitel 5, Abschnitt 9 „Kreuzentropie und KL-Divergenz“: 9.1 Die Kreuzentropie · 9.2 Die KL-Divergenz · 9.3 Was du dafür brauchst: Die Ungleichung $\ln x\le x-1$ · 9.4 Die Gibbs-Ungleichung · 9.5 Die KL-Divergenz ist kein Abstand
- Grundlagen, Kapitel 5, Abschnitt 10 „Die größte Entropie“: 10.1 Die Gleichverteilung hat die größte Entropie · 10.2 Die Entropie einer Dichte · 10.3 Die KL-Divergenz für Dichten · 10.4 Die Normalverteilung hat bei fester Varianz die größte Entropie
- Grundlagen, Kapitel 5, Abschnitt 11 „Maximum Likelihood und KL-Divergenz“: 11.1 Rückblick: Die empirische Verteilung · 11.2 Die Log-Likelihood als Kreuzentropie · 11.3 Maximum Likelihood heißt kleinste KL-Divergenz · 11.4 Die kategorische Verteilung · 11.5 Stetige Daten: Normalverteilung und Quadratsumme
